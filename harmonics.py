""".
# harmonics.py

Module for analyzing positions of natural harmonics on a stringed
instrument relative to positions of fingered notes.


## AUTHOR:

- David Zelinsky <dsz@dedekind.net>


## DISCUSSION:

A string has multiple modes of vibration.  The most common is the
fundamental, or open string.  But for each positive integer N there is
a mode in which the string appears to vibrate in N independent
segments of equal length, with a "node" that appears stationary
occurring at a fraction k/N of the distance from the nut to bridge,
for each of the N-1 multiples k/N of 1/N.  In this mode, the string
resonates at a frequency that is N times the fundamental.

The string can be induced to vibrate in its N-th harmonic mode by
touching it lightly at one of the N-1 nodes (provided that node is not
also a node for some lower harmonic).

Two questions arise concerning these harmonics:

  1. What is the pitch of the N-th harmonic on a given string?

  2. Where are the nodes?  That is, what fingered note is closest to
     each of the nodes?

This module has functions to answer each of those questions, with the
answer presented in various formats.  See the methods in the "Output"
section for more explanation.


A word about pitch notation used in the code:

All pitches refer to chromatic scale positions in **tempered tuning**.
It is also assumed that when multiple strings are involved, they are
tuned according to tempered pitch.

- Diatonic notes are referred to by letter names "A,B,..." in upper
  case (with lower case also recognized).

- Sharps and flats are denoted by a following "s" or "f" respectively.

- For absolute pitches, the octave is indicated using Scientific Pitch
  Notation: Each octave is numbered, starting on C, with middle C being
  octave number 4.

For example, "Ef3" denotes the E-flat in the octave below middle C.

Note that this differs from Lilypond notation (even in "English"
mode), since Lilypond requires lower case note names; and octaves are
denoted by a number of punctuation marks (single quotes or commas),
with an unadorned "c" representing C3.


## TABLE OF CONTENTS:

### Global Data


### Utility Functions

  - signed
  - ordinal
  - parse_note
  - note_with_accidental
  - note_to_number
  - number_to_interval
  - number_to_note
  - relative_octave
  - instrument_strings
  - note_in_staff

### Computation

  - harmonic_interval
  - note_positions_near_harmonic_number
  - notes_near_harmonic_on_string
  - note_positions_near_harmonic_pitch

### Output

  - print_harmonics
  - print_harmonics_by_position
  - print_harmonics_for_notes
  - lilypond_harmonics
  - lilypond_cello_strings

## COPYRIGHT NOTICE

    This program is free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

from math import log, gcd, floor
import re
import os


################################################################################
################################  Global Data  #################################
################################################################################

HS = 2**(1/12)                  # half step frequency multiple
note_nums =  {'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'A':9, 'B':11}
note_names = {num:name for name,num in note_nums.items()}
flat_symbol = 'f'
sharp_symbol = 's'

################################################################################
#############################  Utility Functions  ##############################
################################################################################

def signed(n):
  return str(n) if n<0 else '+{}'.format(n)

#############################  Utility Functions  ##############################

def ordinal(n):
  """
  Return the English ordinal ('1st', '2nd', etc.) corresponding to 0-based number n

  EXAMPLES:

    >>> ordinal(0)
    '1st'
    >>> ordinal(10)
    '11th'
    >>> ordinal(20)
    '21st'
    >>> ordinal(5)
    '6th'
    >>> ordinal(101)
    '102nd'
    >>> ordinal(111)
    '112th'
    >>> ordinal(121)
    '122nd'

  """
  n1 = n+1
  n1mod100 = n1 % 100
  n1mod10 = n1 % 10
  if n1mod10 in (1,2,3) and not 10 < n1mod100 < 20:
    if n1mod10 == 1: suf = "st"
    if n1mod10 == 2: suf = "nd"
    if n1mod10 == 3: suf = "rd"
  else:
    suf = "th"
  return str(n1) + suf


#############################  Utility Functions  ##############################


def parse_note(note, extract_accidental=False):
  r""".
  Return the note name and octave number

  INPUT:

  - ``note`` -- string; a note name, optionally including an octave number

  - ``extract_accidental`` -- boolean (default: False); whether separate the accidental from the note name

  OUTPUT:

  - pair ``(name,octave)``, or triple ``(name,accidental,octave)`` if ``extract_accidental=True``, where:
  
    - ``name`` -- the non-numeric part of ``note``, or just the first character if ``extract_accidental=True``

    - ``accidental`` -- (present only if ``extract_accidental=True) the
      non-numeric part of ``note`` following the first character, or None if
      there is none

    - ``octave`` -- the numeric part of ``note``, or None if no octave number is present

  EXAMPLE:

    >>> parse_note('A')
    ('A', None)
    >>> parse_note('A3')
    ('A', 3)
    >>> parse_note('Af')
    ('Af', None)
    >>> parse_note('A', extract_accidental=True)
    ('A', None, None)
    >>> parse_note('Af', extract_accidental=True)
    ('A', 'f', None)
    >>> parse_note('A3', extract_accidental=True)
    ('A', None, 3)
    >>> parse_note('Af3', extract_accidental=True)
    ('A', 'f', 3)

  """
  m = re.search('[0-9]',note)
  if m is None:
    name = note
    octave = None
  else:
    i = m.start()
    name = note[:i]
    octave = int(note[i:])
  if not extract_accidental:
    return (name, octave)
  acc = name[1:]
  if acc == '': acc = None
  name = name[0]
  return (name, acc, octave)
  

#############################  Utility Functions  ##############################

def note_with_accidental(note):
  r""".
  Return the note-name and the accidental as a tuple

  INPUT:

  - ``note`` -- a note name, optionally including an octave number

  OUTPUT:

  - tuple ``(name, acc)`` where

    - ``name`` is the letter name of the note

    - ``acc`` is the accidental, which is either a string or None. The string is
      usually either "f" or "s", but it is really just the non-numeric part of
      ``note`` following the single initial letter.  If the non-numeric part of
      ``note`` is a single letter, then ``acc`` will be None.


  EXAMPLES:

    >> note_with_accidental("Af3")
    ("A", "f")

    >> note_with_accidental("As3")
    ("A", "s")

    >> note_with_accidental("A3")
    ("A", None)
  """
  s, _ = parse_note(note)
  name = s[0]
  if len(s) > 1:
    acc = s[1:]
  else:
    acc = None
  return (name, acc)

#############################  Utility Functions  ##############################

def note_to_number(note, lilypond=False):
  """
  Return the note number specified by S
  
  INPUT:

  - ``note`` -- a python string representing a pitch, with or without
    octave specification

  - ``lilypond`` -- boolean (default: False); whether to interpret
    ``note`` in Lilypond format rather than Scientific Pitch Notation;
    in Lilypond format, an octave specification is always implicitly
    included

  OUTPUT:

  - if ``note`` has an octave specification, return the number of
    half steps between C0 to the note;

  - if ``note`` has no octave specification, return the number of half
    steps from the first C below the note

  EXAMPLES:

    >>> note_to_number("C")     # no octave specification
    0
    >>> note_to_number("C2")
    24
    >>> note_to_number('Fs')
    6
    >>> note_to_number("Fs3")
    42
    >>> note_to_number("fs3")   # lower case is allowed
    42
    >>> note_to_number("fs", lilypond=True)
    42
    >>> note_to_number("bf''", lilypond=True)
    70


  """
  err = TypeError('Illegal note specification')
  if lilypond:
    pp = re.compile('([a-g])({})?({})?(\'*)(,*)'.format(sharp_symbol,flat_symbol))
  else:
    pp = re.compile('([A-Ga-g])({})?({})?([0-9]*)'.format(sharp_symbol,flat_symbol))
  mm = pp.match(note)
  # get the note name
  name = mm.group(1).upper()
  # get the accidental
  s,f = [mm.group(i) for i in (2,3)]
  if None not in (s,f): raise err
  s,f = [0 if x is None else len(x) for x in (s,f)]
  acc = s - f                   # sharp,natural,flat = 1,0,-1
  # get the octave
  if lilypond:
    u,d = [mm.group(i) for i in (4,5)]
    if '' not in (u,d): raise err
    u,d = [0 if x is None else len(x) for x in (u,d)]
    octave = 3 + u - d          # Lilypond's "c" is C3
  else:
    v = mm.group(4)
    octave = 0 if v == '' else int(v)
  # compute the number
  n = note_nums.get(name)
  if n is None: raise err
  return n + acc + 12 * octave

#############################  Utility Functions  ##############################

def number_to_interval(n):
  r""".
  Return the musical interval corresponding to ``n`` half steps.

  INPUT:

  - ``n`` -- postive integer; the number of half steps

  OUTPUT:

  - string of the form "tN" or "tN+m", or just "+m", where

    - ``t`` is the type of interval:

      - "M" -- major

      - "m" -- minor

      - "P" -- perfect  (4th or 5th)

      - "d" -- diminished

    - ``N`` is the interval number

    - ``m`` is the number of full octaves

  EXAMPLES:

    >>> number_to_interval(3)
    'm3'
    >>> number_to_interval(4)
    'M3'
    >>> number_to_interval(5)
    'P4'
    >>> number_to_interval(6)
    'd5'
    >>> number_to_interval(16)
    'M3+1'
    >>> number_to_interval(36)
    '+3'
  """
  n,m = n%12, n//12
  intvls = {0:"", 1:'m2', 2:'M2', 3:'m3', 4:'M3', 5:'P4',
            6:'d5', 7:'P5', 8:'m6', 9:'M6', 10:'m7', 11:'M7'}
  s = intvls[n]
  if m > 0:
    s += "+{}".format(m)
  return s


#############################  Utility Functions  ##############################


def number_to_note(n, relative_to=0, no_octave=False, enharmonic=False, lilypond=False):
  """.

  Return the name of note with scale degree ``n`` in chromatic scale based on C

  INPUT:

  - ``n`` -- integer

  - ``relative_to`` -- integer or string (default: 0); absolute note number, or
    name in scientific notation; return note name with number of full octaves
    above this note.  The default value of 0 corresponds to absolute scientific
    or Lilipond notation.  Giving just note name with no octave number
    (e.g. ``relative_to="A"``) implies ``no_octave=True``.

  - ``no_octave`` -- boolean (default: False); whether to return only the note
    name with no octave indication.

  - ``lilypond`` -- boolean (default: False); whether to use Lilypond
    format rather than Scientific Pitch Notation

  - ``enharmonic`` -- boolean (default: False); whether to output the
    enharmonic note instead of the default.  This has no effect unless
    the note an accidental is required, in which case the default is
    to choose the accidental that comes first in the circle of fifths:
    Fs,Cs,Gs,... or Bf,Ef,Af,..., preferring sharps over flats for
    ties.  For example, Ds occurs 4th in the list and Ef 2nd, so Ef
    ios preferred; and Gs and Af are both 3rd in their lists, so Gs is
    preferred.  Setting ``enharmonic=True`` reverses these choices.

  OUTPUT:

  - Return the name and octave of the note that that is ``n`` half steps above
    the note specified by the value of ``relative_true`` in scientific notation,
    or in Lilypond notation with ``lilypond=True`` True.

  EXAMPLES:

    >>> print(number_to_note(32))
    Gs2
    >>> print(number_to_note(32, no_octave=True))
    Gs
    >>> print(number_to_note(32, enharmonic=True))
    Af2

    >>> print(number_to_note(32, lilypond=True))
    gs,
    >>> print(number_to_note(32, no_octave=True, lilypond=True))
    gs

    >>> print(number_to_note(32, relative_to="A1"))
    F4
    >>> print(number_to_note(44, relative_to="A1"))
    F5
    >>> print(number_to_note(20, relative_to="A1"))
    F3
    >>> print(number_to_note(20, relative_to="A1", no_octave=True))
    F
    >>> print(number_to_note(20, relative_to="A"))
    F

  """
  if type(relative_to) is str:
    name, octave = parse_note(relative_to)
    if octave is None:
      no_octave = True
    rel = note_to_number(relative_to)
  else:
    rel = relative_to
  n += rel
  m, octave = n%12, n//12
  name = note_names.get(m)
  acc = ''
  if name is None:
    # try sharp
    m_s, octave_s = (n-1)%12, (n-1)//12
    name_s = note_names.get(m_s)
    ind_s = 10 if name_s is None else ('F','C','G','D','A','E').index(name_s)
    # try flat
    m_f, octave_f = (n+1)%12, (n+1)//12
    name_f = note_names.get(m_f)
    ind_f = 10 if name_f is None else ('B','E','A','D','G').index(name_f)
    flat = ind_f < ind_s
    if enharmonic:
      flat = not flat
    if flat:
      name, octave = name_f, octave_f
      acc = flat_symbol
    else:
      name, octave = name_s, octave_s
      acc = sharp_symbol

  if not lilypond:
    if no_octave:
      return name + acc
    return '{}{}{}'.format(name, acc, octave)

  # Lilypond
  name = name.lower()
  if no_octave:
    return name + acc
  octave -= 3                 # since "c" means "C3"
  octave_symbol = "'" * octave if octave >= 0 else "," * abs(octave)
  return name + acc + octave_symbol

#############################  Utility Functions  ##############################

def relative_octave(note, base):
  r""".
  Return the octave number of ``note`` relative to ``base``.

  INPUT:

  - ``note, base`` -- strings, specifying absolute pitches in scientific notation

  OUPTUT:

  - the integer number of octaves from ``base`` to ``note``.

  EXAMPLES:

    >>> relative_octave("C4", "A3")
    0
    >>> relative_octave("A4", "A3")
    1
    >>> relative_octave("C3", "A3")
    -1
  """
  n = note_to_number(note)
  b = note_to_number(base)
  d = n-b
  oct = int(d/12)
  if d<0:
    oct -= 1
  return oct


#############################  Utility Functions  ##############################

def instrument_strings(instrument):
    instr = instrument.lower()
    if instr == 'violin':
      return ('E5','A4','D4','G3')
    elif instr == 'viola':
      return ('A4','D4','G3','C3')
    elif instr == 'cello':
      return ('A3','D3','G2','C2')
    elif instr == 'bass':
      return ('G2','D2','A1','E1')
    else:
      raise TypeError('unrecognized instrument: {}'.format(instrument))


#############################  Utility Functions  ##############################

def note_in_staff(note, top_notes=('C4','G4','C6'), lilypond=False):
  r""".
  Return data for producing Lilypond input to represent given note without ledger lines.

  INPUT:

  - ``note`` -- integer or string: number of half steps above C0; or
    an absolute pitch in scientific notatation, or in lilypond notation if ``lilypond=True``.

  OUTPUT:

  - a pair (clef, octave) where

    - ``clef`` -- the name of the clef to use, one of "bass", "tenor", or
      "treble"

    - ``octave`` -- an integer giving the number of ocataves up (if positive) or
      down (if negative) to offset the printed note, using "8va", etc.

  EXAMPLES:

    >>> note_in_staff('G2')
    ('bass', 0)

    >>> note_in_staff('C4')
    ('bass', 0)

    >>> note_in_staff('A4')
    ('treble', 0)

    >>> note_in_staff('A5')
    ('treble', 0)

    >>> note_in_staff("a''", lilypond=True)
    ('treble', 0)

  """
  if lilypond:
    note = number_to_note(note_to_number(note,lilypond=True))
  elif type(note) is not str:
    note = number_to_note(note)
  note, acc, note_oct = parse_note(note, extract_accidental=True)
  num = note_to_number(note+str(note_oct)) # note without accidental
  octave = 0
  top_nums = [note_to_number(s) for s in top_notes]
  if num <= top_nums[0]:
    clef = "bass"
  elif num <= top_nums[1]:
    clef = "tenor"
  elif num <= top_nums[2]:
    clef = "treble"
  else:
    clef = "treble"
    top = top_nums[2]
    d = num - top
    q = d//12
    octave = q + 1
  return (clef, octave)


################################################################################
################################  Computation  #################################
################################################################################


def harmonic_interval(h):
  """.
      
  Return the chromatic interval and offset of a harmonic.

  INPUT:

  - ``h`` -- positive integer; the harmonic number

  OUTPUT:

  - pair ``(note_num, offset)`` representing the pitch of the harmonic
    relative to the open string:

    - ``note_num`` -- integer; the number of half steps from the open
      string to the note in tempered tuning closest the sound of the harmonic

    - ``offset`` -- number of cents sharp (or flat if negative) that
      the harmonic note sounds relative to the tempered pitch
      ``note_num`` half steps above the open string


  EXAMPLES:

    >>> harmonic_interval(1)
    (0, 0)
    >>> harmonic_interval(2)
    (12, 0)
    >>> harmonic_interval(3)
    (19, 2)

  The last example indicates that the 3rd harmonic sounds 2 cents
  higher than the note one octave (12 half steps) and a tempered fifth
  (7 half steps) above the open string.

  """
  logh = log(h,HS)
  hint = int(round(logh))
  hoff = int(round(100*(logh - hint)))
  return hint, hoff

################################  Computation  #################################

def note_positions_near_harmonic_number(h, octave=None):
  """.
  Return list of fingered note positions nearest each node of given harmonic.

  INPUT:

  - ``h`` -- positive integer; the harmonic number

  - ``octave`` -- optional octave number, a non-negative integer; if
    given, limit output to just this octave

  OUTPUT:

  - ordered list of pairs ``(ind, steps, off)`` where

    - ``ind`` is the index of the harmonic node located at ind/h times the
      string length. These will range over all postive integers less
      than h and relatively prime to h.  But if ``octave=N`` is
      specified, only values for which the fingered note at the node
      is in the Nth octave of the string will be included (with N=0
      the first octave).

    - ``steps`` is the number of half steps above the open string of the
      note whose fingered location (in tempered pitch) is nearest the harmonic node

    - ``off`` is the offset in cents (hundredths of a half step) from
      the location of the fingered note to the harmonic node.
      Stopping the string at the location of the harmonic node will
      produce a note that is ``off`` cents sharp if ``off > 0`` or ``|off|``
      cents flat if ``off < 0``, relative to the note ``steps`` tempered
      half steps above the open string.

  EXAMPLES:

    >>> note_positions_near_harmonic_number(1)
    []
    >>> note_positions_near_harmonic_number(2)
    [(1, 12, 0)]
    >>> note_positions_near_harmonic_number(3)
    [(1, 7, 2), (2, 19, 2)]
    >>> note_positions_near_harmonic_number(4)
    [(1, 5, -2), (3, 24, 0)]

    >>> note_positions_near_harmonic_number(3, octave=0)
    [(1, 7, 2)]
    >>> note_positions_near_harmonic_number(3, octave=1)
    [(2, 19, 2)]

  """
  if h < 0:
    raise TypeError('argument must be a positive integer')
  notes = []
  N = octave
  for ind in range(1,h):
    if gcd(ind,h) > 1: continue
    if N is not None:
      # octave N is between 1-2^-N and 1-2^-(N+1)
      m = ind * 2**(N+1)
      if not ( h * 2 * (2**N - 1) <= m ): continue
      if not (m < h * (2**(N+1) - 1) ): break
    lg = log(h/(h-ind),HS)
    steps = int(round(lg))
    off = int(round(100*(lg-steps)))
    notes.append((ind,steps,off))
  return notes


################################  Computation  #################################

def notes_near_harmonic_on_string(h, string, octave=None, lilypond=False):
  r""".
  Return list of notes nearest each node of given harmonic on given string.

  INPUT:

  - ``h`` -- positive integer; the harmonic number

  - ``string`` -- string; note name and octave of open string, in scientific notation

  - ``octave`` -- optional octave number (0-based); if given, report only
    harmonic nodes in that octave of the string.

  - ``lilypond`` -- boolean (default: False); whether to give pitches in lilypond rather than
    scientific notation

  OUTPUT:

  - a list of triples (ind, pitch, err):

    - ``ind`` -- the index of the harmonic node, appearing at n/h of the string
      length from the nut

    - ``pitch`` -- string; the pitch in scientific notation (default), or
      lilypond notation if lilypond=True

    - ``err`` -- the offset in cents from the fingered note to the harmonic note

  EXAMPLES:

    >>> notes_near_harmonic_on_string(5, "A3", octave=0)
    [(1, 'Cs4', -14), (2, 'Fs4', -16)]
    >>> notes_near_harmonic_on_string(5, "A3", octave=0, lilypond=True)
    [(1, "cs'", -14), (2, "fs'", -16)]

  """
  ans = []
  for (ind,steps,off) in note_positions_near_harmonic_number(h, octave=octave):
    pitch = number_to_note(steps, relative_to=string, lilypond=lilypond)
    ans.append((ind,pitch,off))
  return ans

################################  Computation  #################################

def note_positions_near_harmonic_pitch(harmonic_pitch, instrument_or_strings):
  """.
  Return list of all fingerings of a given harmonic pitch for given instrument or list of strings.

  INPUT:

  - ``harmonic_pitch`` -- an absolute pitch name

  - ``instrument_or_strings`` -- name of a stringed instrument, or list of note names for open strings

  OUTPUT:

  - List of 5-tuples (stringnum, fingnote, fingoff, hnum, nodenum, hoff) of integers, where

    - ``stringnum`` -- the number of the string on which the harmonic is fingered

    - ``fingnote`` -- the nearest fingered note to the harmonic node

    - ``fingoff`` -- number of cents above (below if negative) the fingered note
      where the harmonic node occurs

    - ``hnum`` -- the harmonic number

    - ``nodenum`` -- number of the harmonic node (from 1 to hnum-1)

    - ``hoff`` -- number of cents sharp (flat if negative) the harmonic sounds
      relative to ``harmonic_pitch`` in tempered tuning

  EXAMPLES:

  Show all harmonics that sound like D one octave above middle C on the cello::

    >>> for hh in note_positions_near_harmonic_pitch('D5', 'cello'): print(hh)
    (1, 'G3', -2, 4, 1, 0)
    (1, 'D5', 0, 4, 3, 0)
    (2, 'Bf2', 16, 6, 1, 2)
    (2, 'D5', 2, 6, 5, 2)
    (3, 'D2', 4, 9, 1, 4)
    (3, 'E2', 35, 9, 2, 4)
    (3, 'Bf2', 18, 9, 4, 4)
    (3, 'D3', 4, 9, 5, 4)
    (3, 'D4', 4, 9, 7, 4)
    (3, 'D5', 4, 9, 8, 4)

    >>> strings = ['A3','D3','G2','C2']
    >>> for hh in note_positions_near_harmonic_pitch('D5', strings): print(hh)
    (1, 'G3', -2, 4, 1, 0)
    (1, 'D5', 0, 4, 3, 0)
    (2, 'Bf2', 16, 6, 1, 2)
    (2, 'D5', 2, 6, 5, 2)
    (3, 'D2', 4, 9, 1, 4)
    (3, 'E2', 35, 9, 2, 4)
    (3, 'Bf2', 18, 9, 4, 4)
    (3, 'D3', 4, 9, 5, 4)
    (3, 'D4', 4, 9, 7, 4)
    (3, 'D5', 4, 9, 8, 4)


  """
  if type(instrument_or_strings) is str:
    strings = instrument_strings(instrument_or_strings)
  else:
    strings = list(instrument_or_strings)
    strings.sort(key=lambda s: note_to_number(s), reverse=True)
  hh = []
  # parse note name and octave
  h_note, h_octave = parse_note(harmonic_pitch)
  h_note_num = note_to_number(h_note) + 12 * h_octave
  for s_ind, s in enumerate(strings):
    s_note, s_octave = parse_note(s)
    s_note_num = note_to_number(s_note) + 12 * s_octave
    # find the harmonic closest to harmonic_note
    sh = int(round(HS**(h_note_num - s_note_num)))
    sh_num, sh_off = harmonic_interval(sh)
    if h_note_num != sh_num + s_note_num: continue
    for node_num, note_num, note_off in note_positions_near_harmonic_number(sh):
      note_num += s_note_num
      note = number_to_note(note_num)
      hh.append((s_ind, note, note_off, sh, node_num, sh_off))
  return hh


################################################################################
###################################  Output  ###################################
################################################################################

def print_harmonics(string, max_harmonic=8, octave=None, show_octave_numbers=True):
  """.

  Print a table of locations of all harmonic nodes on a single string.

  INPUT:

  - ``string`` -- string; note name of an open string, optionally
    including octave number in Scientific Pitch Notation

  - ``max_harmonic`` -- positive integer (default: 8); largest
    harmonic number to include

  - ``octave`` -- optional non-negative integer; if given, show only
    harmonics fingered in this number octave (0-based) above open
    string; otherwise all octaves will be included.

  OUTPUT:

  - None

  EFFECT:

  - Prints a heading with the string name and octave if specified, followed by a
    table of harmonics data for that string.  If open string was given with an
    octave number (e.g. "A3") then all pitches will be printed in absolute
    scientific notation.  Otherwise the octave number on all pitches will
    indicate in which octave above the open string they occur.  For example,
    with string="A", the pitch "C0" indicates a minor third above the open
    string.

    Each row of the ensuing table has the following entries:

    - harmonic number H

    - integer from 1 to H-1, indicating the node of the harmonic

    - name of note closest to the sound of the harmonic

    - number of cents sharp or flat the harmonic sounds relative to the named
      note, in tempered pitch; positive means sharp, negative flat

    - name of fingered note closest to the indicated harmonic node

    - number of cents above (if positive) or below (if negative) the named note
      where the harmonic node occurs.

  EXAMPLES:

    >>> print_harmonics('A3', max_harmonic=5)
    <BLANKLINE>
    A3 string:
    <BLANKLINE>
     ------- harmonic -------   --- finger at ---
    <BLANKLINE>
      2  1  A4   ( +0 cents):    A4   ( +0 cents)
    <BLANKLINE>
      3  1  E5   ( +2 cents):    E4   ( +2 cents)
      3  2  E5   ( +2 cents):    E5   ( +2 cents)
    <BLANKLINE>
      4  1  A5   ( +0 cents):    D4   ( -2 cents)
      4  3  A5   ( +0 cents):    A5   ( +0 cents)
    <BLANKLINE>
      5  1  Cs6  (-14 cents):    Cs4  (-14 cents)
      5  2  Cs6  (-14 cents):    Fs4  (-16 cents)
      5  3  Cs6  (-14 cents):    Cs5  (-14 cents)
      5  4  Cs6  (-14 cents):    Cs6  (-14 cents)

    >>> print_harmonics('A3', octave=1)
    <BLANKLINE>
    A3 string, 2nd octave:
    <BLANKLINE>
     ------- harmonic -------   --- finger at ---
    <BLANKLINE>
      2  1  A4   ( +0 cents):    A4   ( +0 cents)
    <BLANKLINE>
      3  2  E5   ( +2 cents):    E5   ( +2 cents)
    <BLANKLINE>
      5  3  Cs6  (-14 cents):    Cs5  (-14 cents)
    <BLANKLINE>
      7  4  G6   (-31 cents):    C5   (-33 cents)
      7  5  G6   (-31 cents):    G5   (-31 cents)
    <BLANKLINE>
      8  5  A6   ( +0 cents):    D5   ( -2 cents)

  """
  string_name, string_octave = parse_note(string)
  if string_octave is None:
    raise TypeError('string must be an abolute pitch')
  print('\n{} string'.format(string),end='')
  if octave is not None:
    print(', {} octave'.format(ordinal(octave)),end='')
  print(':\n')
  print(' ------- harmonic -------   --- finger at ---')
  for h in range(2,max_harmonic+1):
    nodes = note_positions_near_harmonic_number(h,octave=octave)
    if len(nodes) == 0: continue
    hsteps, hoff = harmonic_interval(h)
    hnote = number_to_note(hsteps, relative_to=string)
    print('')
    for ind,steps,off in nodes:
      note = number_to_note(steps, relative_to=string)
      print(' {:>2} {:>2}  {:<4} ({:>3} cents):    {:<4} ({:>3} cents)'.format(h, ind, hnote, signed(hoff), note, signed(off)))


###################################  Output  ###################################


def print_harmonics_by_position(string, octaves=(0,), max_harmonic=8):
  """.

  Print a table of notes on given string in given octaves, and the harmonics nearest them.

  INPUT:

  - ``string`` -- absolute note name of the open string

  - ``octaves`` -- integer, or list of integers (default: 0); which octaves to show (0
    means first octave)

  - ``max_harmonic`` -- positive integer (default: 16); largest number harmonic
    to include

  OUTPUT:

  - a string, showing a table of each fingered note in the given octaves, and
    the harmonic nodes near each note.  The table is grouped by octave.  Each
    row of the table gives this data:

   - name of a fingered note in the indicated octave

   - number of cents above (if positive) or below (if negative) the indicated
     note where a harmonic node occurs

  - the harmonic number whose node occurs at the indicated note position

  - the name and octave of the note (in scientific notation) to which the sound
    of the harmonic is closest

  - number of cents sharp (positive) or flat (negative) that the harmonic sounds
    relative to the indicated note in tempered tuning


  EXAMPLES:

    >>> print_harmonics_by_position('A3')
    <BLANKLINE>
    A3 string:
    <BLANKLINE>
      --- finger at ---   ------ harmonic ------
    <BLANKLINE>
    1st octave
    <BLANKLINE>
      B    (+31 cents):    8   A6   ( +0 cents)
    <BLANKLINE>
      C    (-33 cents):    7   G6   (-31 cents)
      C    (+16 cents):    6   E6   ( +2 cents)
    <BLANKLINE>
      Cs   (-14 cents):    5   Cs6  (-14 cents)
    <BLANKLINE>
      D    ( -2 cents):    4   A5   ( +0 cents)
    <BLANKLINE>
      Ef   (-17 cents):    7   G6   (-31 cents)
    <BLANKLINE>
      E    ( +2 cents):    3   E5   ( +2 cents)
    <BLANKLINE>
      F    (+14 cents):    8   A6   ( +0 cents)
    <BLANKLINE>
      Fs   (-16 cents):    5   Cs6  (-14 cents)
    <BLANKLINE>
      G    (-31 cents):    7   G6   (-31 cents)

    >>> print_harmonics_by_position('A3', octaves=(0,1), max_harmonic=4)
    <BLANKLINE>
    A3 string:
    <BLANKLINE>
      --- finger at ---   ------ harmonic ------
    <BLANKLINE>
    1st octave
    <BLANKLINE>
      D    ( -2 cents):    4   A5   ( +0 cents)
    <BLANKLINE>
      E    ( +2 cents):    3   E5   ( +2 cents)
    <BLANKLINE>
    2nd octave
    <BLANKLINE>
      A    ( +0 cents):    2   A4   ( +0 cents)
    <BLANKLINE>
      E    ( +2 cents):    3   E5   ( +2 cents)

  """
  string_name, string_octave = parse_note(string)
  if string_octave is None:
    raise TypeError('string must be an absolute pitch')
  harms = []
  if type(octaves) in (list,tuple):
    octaves = tuple(octaves)
  else:
    octaves = (octaves,)
  print('\n{} string:'.format(string))
  print('')
  print('  --- finger at ---   ------ harmonic ------')
  for oct in octaves:
    harms = []
    for h in range(1,max_harmonic+1):
      hint, hoff = harmonic_interval(h)
      hnote = number_to_note(hint, relative_to=string)
      for _,steps,off in note_positions_near_harmonic_number(h, octave=oct):
        harms.append((steps,off,h,hnote,hoff))
    harms.sort()
    print('')
    print('{} octave'.format(ordinal(oct)))
    prev_note = None
    for (steps,off,h,hnote,hoff) in harms:
      note = number_to_note(steps,relative_to=string,no_octave=True)
      if note != prev_note:
        print('')
        prev_note = note
      print('  {:<4} ({:>3} cents):   {:>2}   {:<4} ({:>3} cents)'.format(note,signed(off),h,hnote,signed(hoff)))



###################################  Output  ###################################

def print_harmonics_for_notes(music, instrument_or_strings):
  """.
  Print a table of harmonics and their fingered positions for a sequence of notes.

  INPUT:

  - ``music`` -- string; a space-separated sequence of note/octave names in
    scientific notation

  - ``instrument_or_strings`` -- name of a stringed instrument, or a list of pitches of open strings

  EFFECT:

  - Prints a table of all possible harmonic data for each note in the sequence.
    For each note, the harmonic data are sorted in order of distance from the
    nut of the string.  Each row of the table has the following columns:

    - ``harmonic_note`` -- the pitch of harmonic

    - ``string`` -- number of the string, in Roman numerals, on which the harmonic occurs

    - ``fingered_note`` -- the note name and octave of the fingered note closest
      to the harmonic node; the octave is relative to the open string, with 0
      meaning within the first octave

    - ``fingered_offset`` -- number of cents above (if positive) or below (if
      negative) the fingered note in tempered pitch at which the harmonic node
      is located

    - ``harm_num`` -- harmonic number (multiple of open string frequence)

    - ``harm_node`` -- node number


  EXAMPLES:

    >>> print_harmonics_for_notes('G4 A4 B4', 'cello')
    <BLANKLINE>
      --- harmonic ---    -------- fingered --------
      note number node    string oct note   (offset)
      ----------------    --------------------------
    <BLANKLINE>
       G4     6     1       IV    0   Ef (+16 cents)
       G4     4     1      III    0   C  ( -2 cents)
       G4     4     3      III    2   G  ( +0 cents)
       G4     6     5       IV    2   G  ( +2 cents)
    <BLANKLINE>
       A4     3     1       II    0   A  ( +2 cents)
       A4     2     1        I    1   A  ( +0 cents)
       A4     3     2       II    1   A  ( +2 cents)
    <BLANKLINE>
       B4     5     1      III    0   B  (-14 cents)
       B4     5     2      III    0   E  (-16 cents)
       B4     5     3      III    1   B  (-14 cents)
       B4     5     4      III    2   B  (-14 cents)

    >>> strings = ('A3', 'D3', 'G2', 'C2')
    >>> print_harmonics_for_notes('G4 A4 B4', 'cello')
    <BLANKLINE>
      --- harmonic ---    -------- fingered --------
      note number node    string oct note   (offset)
      ----------------    --------------------------
    <BLANKLINE>
       G4     6     1       IV    0   Ef (+16 cents)
       G4     4     1      III    0   C  ( -2 cents)
       G4     4     3      III    2   G  ( +0 cents)
       G4     6     5       IV    2   G  ( +2 cents)
    <BLANKLINE>
       A4     3     1       II    0   A  ( +2 cents)
       A4     2     1        I    1   A  ( +0 cents)
       A4     3     2       II    1   A  ( +2 cents)
    <BLANKLINE>
       B4     5     1      III    0   B  (-14 cents)
       B4     5     2      III    0   E  (-16 cents)
       B4     5     3      III    1   B  (-14 cents)
       B4     5     4      III    2   B  (-14 cents)

  """
  romans = ['I','II','III','IV']
  if type(instrument_or_strings is str):
    strings = instrument_strings(instrument_or_strings)
  else:
    strings = list(instrument_or_strings)
    strings.sort(key=lambda s: note_to_number(s), reverse=True)
  str_nums = [note_to_number(s) for s in strings]
  print('  --- harmonic ---    -------- fingered --------')
  print('  note number node    string oct note   (offset)')
  print('  ----------------    --------------------------')
  def sort_key(s):
    return (note_to_number(s[1])-str_nums[s[0]], s[0])
  for note in music.split():
    print('')
    ss = note_positions_near_harmonic_pitch(note, strings)
    ss.sort(key=sort_key)
    for str_ind,fing,fing_off,harm,node,_ in ss:
      string = strings[str_ind]
      fing_oct = relative_octave(fing,string)
      fing_note,_ = parse_note(fing)
      print('   {:<3} {:>4}   {:>3}      {:>3}   {:>2}   {:<2} ({:>3} cents)'.format(
        note,harm,node,romans[str_ind],fing_oct,fing_note,signed(fing_off)))



################################################################################
##############################  Lilypond Output  ###############################
################################################################################
 

def lilypond_harmonics(filename, string, octave=0, max_harmonic=16,
                       clef=None, instrument="cello",
                       note_spacing=200, staff_spacing=10,
                       append=False, page_break=False,
                       lilypond_command='lilypond', process=False):
  
  """.

  Write lilypond output to engrave a harmonic fingering chart on given string
  and octave.

  INPUT:

  - ``filename`` -- name of Lilypond file in which to write the output

  - ``string`` -- pitch in scientific notation, or pair (name,octave)  where ``name`` is the letter name and ``octave`` is Lilypond octave number

  - ``octave`` -- non-negative integer (default: 0) or list of such; which
    octave or octaves of the string to show; 0 means the first ocatve.

  - ``max_harmonic`` -- positive integer (default: 16); largest number harmonic to include

  - ``clef`` -- optional string; the Lilypond name of a clef to use for the
    fingered note locations; if not given, an appropriate clef will be chosen
    based on the octave of the fingered notes to be indicated

  - ``instrument`` -- string (default: "cello"); the instrument name to show in the title

  - ``note_spacing`` -- positive integer (default: 200); affects the spacing of notes on the staff

  - ``staff_spacing`` -- positive integer (default: 10); affects the vertical spac between staff systems

  - ``append`` -- boolean (default: False); whether to append the output to the given file

  - ``page_break`` -- boolean (default: False); whether to insert a page break
    before the output; this is ignored unless ``append`` is True

  - ``lilypond_command`` -- string (default: "lilypond"); shell
    command to run, if ``process=True``

  - ``process`` -- boolean (default: False); whether to run lilypond
    on ``filename`` to produce the pdf file.


  OUTPUT:

  - None

  EFFECT:

  - Writes Lilypond source to the named file.  Subsequent processing by Lilypond
    will produce a pdf file showing a double staff, with unmetered bars.  Each
    bar shows all fingerings in the octave of one harmonic.  Each note pair (one
    on lower staff and one on upper) shows the following information:

    - Upper staff shows the approximate pitch of the harmonic, decorated with
      the harmonic number (above the staff), and the pitch offset in cents
      (below the staff) by which the harmonic sounds sharp or flat relative to
      tempered tuning.

    - Lower staff shows the fingered note closest to the harmonic node,
      decorated (below the staff) with the number of cents below or above the
      note where the harmonic node occurs.

  """
  if type(octave) in (list, tuple):
    first = True
    for i,n in enumerate(octave):
      args = {}
      args['filename'] = filename
      args['string'] = string
      args['octave'] = n
      args['max_harmonic'] = max_harmonic
      args['clef'] = clef
      args['instrument'] = instrument
      args['note_spacing'] = note_spacing
      args['staff_spacing'] = staff_spacing
      args['append'] = append or not first
      if type(page_break) in (list, tuple):
        args['page_break'] = page_break[i]
      else:
        args['page_break'] = page_break
      args['lilypond_command'] = lilypond_command
      lilypond_harmonics(**args)
      first = False
    if process:
      os.system('{} {}'.format(lilypond_command, filename))
    return

  lily_harmonic = ""
  lily_fingered = ""
  h_oct_prev = None
  f_oct_prev = None
  for h in range(2,max_harmonic+1):
    h_rel, h_off = harmonic_interval(h)
    h_off = signed(h_off)
    h_note = number_to_note(h_rel, relative_to=string, lilypond=True)
    h_clef, h_oct = note_in_staff(h_note, lilypond=True)
    first = True
    for _, f_note, f_off in notes_near_harmonic_on_string(h, string, octave, lilypond=True):
      f_off = signed(f_off)
      hh = ''
      ff = ''
      if first:
        if h_oct == h_oct_prev:
          h_oct_str = ''
        else:
          h_oct_str = ' \\ottava #{}'.format(h_oct)
          h_oct_prev = h_oct
        hh += '  % {0}\n\\bar "|"\n'.format(h)
        hh += ' \\cadenzaOn\n'
        ff += ' \\cadenzaOn\n'
        hh += '  \\clef "{}"{} {}\\harmonic_\\markup{{"{}"}}^\\markup{{ \\raise #3 {{"x{}"}} }}\n'.format(h_clef, h_oct_str, h_note, h_off, h)
        first = False
      else:
        hh = '  \\clef "{}" {}\\harmonic\n'.format(h_clef, h_note)
      lily_harmonic += hh
      f_clef, f_oct = note_in_staff(f_note, lilypond=True)
      if f_oct == f_oct_prev:
        f_oct_str = ''
      else:
        f_oct_prev = f_oct
        f_oct_str = ' \\ottava #{}'.format(f_oct)
      ff += '  \\clef "{}"{} {}_\\markup{{"{}"}}\n'.format(f_clef, f_oct_str, f_note, f_off)
      lily_fingered += ff
    if first == True:
      continue
      F.write('\n')
    
    lily_harmonic += '  \\cadenzaOff\n'
  
  # suffix to use for music variables, indicating string name and octave
  string_name, _ = parse_note(string)
  suff = '{}{}'.format(string_name, chr(ord('a')+octave))

  pre = ''
  pre += '\\version "2.20.0"\n'
  pre += '\\include "english.ly"\n'
  pre += '  \\header\n'
  pre += '  {\n'
  pre += '    copyright = \\markup{\n'
  pre += '      \\center-column {\n'
  pre += '        "All rights to this work are granted under Creative Commons License CC0."\n'
  pre += '        "See https://creativecommons.org/publicdomain/zero/1.0/"\n'
  pre += '    }\n'
  pre += '  }\n'
  pre += '    tagline = ##f\n'
  pre += '    print-all-headers = ##t\n'
  pre += '  }\n'
  pre += '#(set-default-paper-size "letter")\n'
  pre += 'global = \n'
  pre += '{\n'
  pre += '  \\omit Score.TimeSignature\n'
  pre += '}\n'

  post = ''
  post += '\\score\n'
  post += '{\n'
  post += '  \\header\n'
  post += '  {\n'
  post += '    tagline = ##f\n'
  post += '    piece = \\markup \\column {{ "{} {}-string, {} octave" \\vspace #1 }}\n'.format(instrument.title(), string_name, ordinal(octave))
  post += '  }\n'
  post += '  \\new StaffGroup\n'
  post += '  <<\n'
  post += '    \\new Staff = "pitch" \\with { instrumentName = "pitch" }\n'
  post += '    <<\n'
  post += '      \\new Voice = "pitch" {{ \\pitches{} }}\n'.format(suff)
  post += '    >>\n'
  post += '    \\new Staff = "location" \\with { instrumentName = "location" }\n'
  post += '    << \\locations{} >>\n'.format(suff)
  post += '  >>\n'
  post += '}\n'
  post += '\n'
  post += '\\layout\n'
  post += '{\n'
  post += '  \\context {\n'
  post += '    \\StaffGroup\n'
  post += '    \\consists #Span_stem_engraver\n'
  post += '  }\n'
  post += '  \\context {\n'
  post += '    \\Score\n'
  post += '    \\override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/{})\n'.format(note_spacing)
  post += '  }\n'
  post += '}\n'
  post += '  \n'
  post += '\\paper\n'
  post += '{\n'
  post += '  system-system-spacing = #\'((basic-distance . 1) (padding . {}))\n'.format(staff_spacing)
  post += '  top-margin = 25\n'
  post += '  left-margin = 25\n'
  post += '  right-margin = 25\n'
  post += '  ragged-bottom = ##t\n'
  post += '  print-page-number = ##f\n'
  post += '}\n'

  pitches = 'pitches{} =\n'.format(suff)
  pitches += '{\n'
  pitches += '  \\global\n'
  pitches += lily_harmonic
  pitches += '  \\bar "|."\n'
  pitches += '}\n'

  locations = 'locations{} =\n'.format(suff)
  locations += '{\n'
  locations += '  \\global\n'
  locations += lily_fingered
  locations += '  \\bar "|."\n'
  locations += '}\n'

  if append:
    F = open(filename,'a')
    F.write('\n\n')
    F.write('%'*60)
    F.write('\n\n')
    if page_break:
      F.write('\\pageBreak')
      F.write('\n\n')
  else:
    F = open(filename,'w')

  F.write(pre)
  F.write('\n')
  F.write(pitches)
  F.write('\n')
  F.write(locations)
  F.write('\n')
  F.write(post)
  F.write('\n')

  F.close()

  if process:
    os.system('{} {}'.format(lilypond_command, filename))



##############################  Lilypond Output  ###############################


def lilypond_cello_harmonics(filename_base, octaves=(0,1,2), intro_file=None, lilypond_command='lilypond'):
  r""".

  Produce a PDF fingering chart of harmonics on cello, for first 3
  octaves on all strings.

  Requires lilipond present on the system.

  For some reason the C string requires different spacing from the other
  strings, so is processed separately and a single PDF produced using pdftk.

  INPUT:

  - ``filename_base`` --  base of filenames to use for .ly and .pdf files

  - ``octaves`` -- tuple (default: (0,1,2)); octave numbers to include
    on each string, with 0 meaning the first octave.

  - ``intro_file`` -- optional string, giving name of a lilypond file to include as front matter.

  - ``lilypond_command`` -- string (default: "lilypond"); command to run to process the lilypond file

  OUTPUT:

  - None

  OUTPUT:

  - writes ``filename_base.ly`` and runs ``lilypond_command`` on it to
    produce ``filename_base.pdf` with typeset harmonics.  For each
    octave on each string, shows a double staff with harmonic pitces
    on upper staff and all possible fingerings on lower staff.

  """

  filename = filename_base + '.ly'

  F = open(filename,'w')
  if intro_file is not None:
    F.write('\\include "{}"\n\n'.format(intro_file))
  F.close()

  args = {'octave':octaves, 'page_break':(True,True,False), 'staff_spacing':5, 'append':True}
  lilypond_harmonics(filename, "A3", **args)
  lilypond_harmonics(filename, "D3", **args)
  lilypond_harmonics(filename, "G2", **args)
  lilypond_harmonics(filename, "C2", process=True, **args)



################################################################################
################################################################################
################################################################################
