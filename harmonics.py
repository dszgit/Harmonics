""".
# harmonics.py

Module for analyzing positions of natural harmonics on a stringed
instrument relative to positions of fingered notes.


** AUTHOR:

- David Zelinsky <dsz@dedekind.net>


** DISCUSSION:

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

A word about pitch notation:

All pitches refer to chromatic scale positions in **tempered tuning**.
It is also assumed that when multiple strings are involved, they are
tuned according to tempered pitch.

- Diatonic notes are referred to by letter names "A,B,..." in upper
  case (with lower case also recognized).

- Sharps and flats are denoted by a following "s" or "f" respectively.

- For absolute pitches, the octave indicated using Scientific Pitch
  Notation: Each octave is numbered, starting on C, with middle C
  octave number 4.

For example, "Ef3" denotes the E-flat in the octave below middle C.

Note that this differs from Lilypond notation (even in "English"
mode), since Lilypond requires lower case note names; and octaves are
denoted by a number of punctuation marks (single quotes or commas),
with an unadorned "c" representing C3.


** TABLE OF CONTENTS:

### Global Data

### Utility Functions

  - ordinal
  - parse_note
  - note_to_number
  - number_to_note

### Computation

  - note_positions_near_harmonic_number
  - note_positions_near_harmonic_pitch
  - harmonic_interval

### Output

  - print_harmonics
  - print_harmonics_by_position
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


def parse_note(note):
  """
  Return the note name and octave number

  INPUT:

  - ``note`` -- string; a note name, optionally including an octave number

  OUTPUT:

  - name,octave:
  
    - ``name`` -- the non-numeric part of ``note``

    - ``octave`` -- the numeric part of ``note``, or None if no octave number is present

  EXAMPLE:

    >>> parse_note('A')
    ('A', None)
    >>> parse_note('A3')
    ('A', 3)

  """
  m = re.search('[0-9]',note)
  if m is None:
    return note, None
  i = m.start()
  name = note[:i]
  octave = int(note[i:])
  return name, octave


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

def number_to_note(n, relative_to='C0', enharmonic=False, lilypond=False):
  """.

  Return the name of note with scale degree ``n`` in chromatic scale based on C

  INPUT:

  - ``n`` -- integer

  - ``relative_to`` -- string or integer or None (default: 0); absolute note
    number, or name in scientific notation; return note name with number of full
    octaves above this note.  The default value of 0 corresponds to absolute
    scientific or Lilipond notation.  If None, then no octave number is included.

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

  - If ``relative_to`` is None, return the note name with no octave number.

  - If ``relative_to`` is a note name or number, return the note name with
    octave number relative to the given relative_to note.  This is the actual
    number of full octaves contained in the interval from the relative_to note.
    For example, with relative_to="A3", the C above A3 (C4 in scientific
    notation) would be notated as "C0".  Notes below ``relative_to`` are given
    with negative octave numbers.  Setting ``relative_to=0`` (the default) gives
    the absolute pitch.

  EXAMPLES:

    >>> print(number_to_note(32))
    Gs2
    >>> print(number_to_note(32, relative_to=None))
    Gs
    >>> print(number_to_note(32, enharmonic=True))
    Af2

    >>> print(number_to_note(32, lilypond=True))
    gs,
    >>> print(number_to_note(32, relative_to=None, lilypond=True))
    gs

    >>> print(number_to_note(32, relative_to="A1"))
    Gs0
    >>> print(number_to_note(44, relative_to="A1"))
    Gs1
    >>> print(number_to_note(20, relative_to="A1"))
    Gs-1

  """
  rel = relative_to
  if rel is None:
    include_octave = False
    rel_num = 0
  else:
    include_octave = True
    rel_num = note_to_number(rel) if type(rel) is str else rel

  m, octave = n%12, (n-rel_num)//12
  name = note_names.get(m)
  acc = ''
  if name is None:
    # try sharp
    m_s, octave_s = (n-1)%12, (n-1-rel_num)//12
    name_s = note_names.get(m_s)
    ind_s = 10 if name_s is None else ('F','C','G','D','A','E').index(name_s)
    # try flat
    m_f, octave_f = (n+1)%12, (n+1-rel_num)//12
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
    if not include_octave:
      return name + acc
    return '{}{}{}'.format(name, acc, octave)

  # Lilypond
  name = name.lower()
  if not include_octave:
    return name + acc
  octave -= 3                 # since "c" means "C3"
  octave_symbol = "'" * octave if octave >= 0 else "," * abs(octave)
  return name + acc + octave_symbol

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

def note_positions_near_harmonic_number(h):
  """.
  Return list of fingered note positions nearest each node of given harmonic.

  INPUT:

  - ``h`` -- positive integer; the harmonic number

  OUTPUT:

  - ordered list of pairs ``(n,m,e)`` where

    - ``m`` is the index of the harmonic node; these will range over all numbers in [1,h-1] prime to h

    - ``n`` is the number of half steps above the open string of the
      note whose fingered location (in tempered pitch) is nearest the harmonic node

    - ``e`` is the offset in cents (hundredths of a half step) from
      the location of the fingered note to the harmonic node.
      Stopping the string at the location of the harmonic node will
      produce a note that is ``e`` cents sharp if ``e > 0`` or ``|e|``
      cents flat if ``e < 0``, relative to the note ``n`` tempered
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

  """
  if h < 0:
    raise TypeError('argument must be a positive integer')
  notes = []
  for m in range(1,h):
    if gcd(m,h) > 1: continue
    lg = log(h/m,HS)
    n = int(round(lg))
    e = int(round(100*(lg-n)))
    notes.append((h-m,n,e))
  notes.reverse()
  return notes


################################  Computation  #################################

def note_positions_near_harmonic_pitch(harmonic_pitch, strings=None, instrument=None):
  """.

  Return list of all fingerings of a given note on given strings.

  INPUT:

  - ``harmonic_pitch`` -- an absolute pitch name

  - ``strings`` -- optional list of string names and octaves in scientific pitch
    notation.  For example, the 4 strings on a cello are denoted
    ('A3','D3','G2','C2')

  - ``instrument`` -- name of a stringed instrument

  Exactly one of ``strings`` or ``instrument`` must be given.  If
  ``instruments`` given, all four strings of the named instrument will be used.


  OUTPUT:

  - List of 5-tuples (hoff, stringnum, hnum, nodenum, fingnote, fingoff) of integers, where

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

    >>> for hh in note_positions_near_harmonic_pitch('D5', instrument='cello'): print(hh)
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
  if len([arg for arg in (strings, instrument) if arg is not None]) != 1:
    raise TypeError('exactly one of "strings" or "instrument" must be given')
  if instrument is not None:
    strings = instrument_strings(instrument)
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

def print_harmonics(string, max_harmonic=16, octave=None):
  """.

  Print a table of locations of all harmonic nodes on a single string.

  INPUT:

  - ``string`` -- string; note name of an open string, optionally
    including octave number in Scientific Pitch Notation

  - ``max_harmonic`` -- positive integer (default: 16); largest
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

    >>> print_harmonics('A3', max_harmonic=4)
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

    >>> print_harmonics('A', max_harmonic=4)
    <BLANKLINE>
    A string:
    <BLANKLINE>
     ------- harmonic -------   --- finger at ---
    <BLANKLINE>
      2  1  A1   ( +0 cents):    A1   ( +0 cents)
    <BLANKLINE>
      3  1  E1   ( +2 cents):    E0   ( +2 cents)
      3  2  E1   ( +2 cents):    E1   ( +2 cents)
    <BLANKLINE>
      4  1  A2   ( +0 cents):    D0   ( -2 cents)
      4  3  A2   ( +0 cents):    A2   ( +0 cents)

    >>> print_harmonics('A', max_harmonic=8, octave=1)
    <BLANKLINE>
    A string, 2nd octave:
    <BLANKLINE>
     ------- harmonic -------   --- finger at ---
    <BLANKLINE>
      2  1  A1   ( +0 cents):    A    ( +0 cents)
    <BLANKLINE>
      3  2  E1   ( +2 cents):    E    ( +2 cents)
    <BLANKLINE>
      5  3  Cs2  (-14 cents):    Cs   (-14 cents)
    <BLANKLINE>
      7  4  G2   (-31 cents):    C    (-33 cents)
      7  5  G2   (-31 cents):    G    (-31 cents)
    <BLANKLINE>
      8  5  A3   ( +0 cents):    D    ( -2 cents)

  """
  _, string_octave = parse_note(string)
  string_name = string
  if string_octave is None:
    # octave numbers relative to string; but none on fingered notes if octave given
    string += '0'
    hnote_rel = string
    note_rel = string if octave is None else None
  else:
    # octave numbers absolute; but none on fingered notes if octave given
    hnote_rel = 0
    note_rel = 0 if octave is None else None
  string_num = note_to_number(string)
  max_harm_oct = floor(log(max_harmonic,2))
  if octave is not None:
    print('\n{} string, {} octave:'.format(string_name, ordinal(octave)))
  else:
    print('\n{} string:'.format(string_name))
  print('')
  print(' ------- harmonic -------   --- finger at ---')
  for h in range(2,max_harmonic+1):
    hint,hoff = harmonic_interval(h)
    first = True
    for node,n,e in note_positions_near_harmonic_number(h):
      if octave is not None and floor(n/12) != octave: continue
      note = number_to_note(string_num + n, relative_to=note_rel)
      hnote = number_to_note(string_num + hint, relative_to=hnote_rel)
      e_sgn = '+' if e>=0 else '-'
      e = e_sgn + str(abs(e))
      hoff_sgn = '+' if hoff>=0 else '-'
      hoff_str = hoff_sgn + str(abs(hoff))
      if first:
        print('')
        first = False
      print(' {:>2} {:>2}  {:<4} ({:>3} cents):    {:<4} ({:>3} cents)'.format(h, node, hnote, hoff_str, note, e))


###################################  Output  ###################################


def print_harmonics_by_position(string, octaves=(0,), max_harmonic=16):
  """.

  Print a table of notes on given string in given octave, and the harmonics nearest them.

  INPUT:

  - ``string`` -- note name of an open string

  - ``octaves`` -- list of integers (default: [0]); which octaves to show (0
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

  - the name of the note to which the sound of the harmonic is closest (in
    tempered tuning), with number of '+' signs prepended indicating the number
    of octaves above the open string

  - number of cents sharp (positive) or flat (negative) that the harmonic sounds
    relative to the indicated note in tempered tuning


  EXAMPLES:

    >>> print_harmonics_by_position('A', max_harmonic=8)
    <BLANKLINE>
    A string:
    <BLANKLINE>
      --- finger at ---   ------ harmonic ------
    <BLANKLINE>
    1st octave
    <BLANKLINE>
      B    (+31 cents):    8   A3   ( +0 cents)
    <BLANKLINE>
      C    (-33 cents):    7   G2   (-31 cents)
      C    (+16 cents):    6   E2   ( +2 cents)
    <BLANKLINE>
      Cs   (-14 cents):    5   Cs2  (-14 cents)
    <BLANKLINE>
      D    ( -2 cents):    4   A2   ( +0 cents)
    <BLANKLINE>
      Ef   (-17 cents):    7   G2   (-31 cents)
    <BLANKLINE>
      E    ( +2 cents):    3   E1   ( +2 cents)
    <BLANKLINE>
      F    (+14 cents):    8   A3   ( +0 cents)
    <BLANKLINE>
      Fs   (-16 cents):    5   Cs2  (-14 cents)
    <BLANKLINE>
      G    (-31 cents):    7   G2   (-31 cents)
    <BLANKLINE>
      A    ( +0 cents):    2   A1   ( +0 cents)

    >>> print_harmonics_by_position('A', octaves=(0,1), max_harmonic=4)
    <BLANKLINE>
    A string:
    <BLANKLINE>
      --- finger at ---   ------ harmonic ------
    <BLANKLINE>
    1st octave
    <BLANKLINE>
      D    ( -2 cents):    4   A2   ( +0 cents)
    <BLANKLINE>
      E    ( +2 cents):    3   E1   ( +2 cents)
    <BLANKLINE>
      A    ( +0 cents):    2   A1   ( +0 cents)
    <BLANKLINE>
    2nd octave
    <BLANKLINE>
      E    ( +2 cents):    3   E1   ( +2 cents)
    <BLANKLINE>
      A    ( +0 cents):    4   A2   ( +0 cents)

  """
  _, string_octave = parse_note(string)
  string_name = string
  if string_octave is None:
    # harmonic octave numbers relative to string
    string += '0'
    rel = string
  else:
    # octave numbers absolute
    rel = 0
  string_num = note_to_number(string)
  notes = {h:note_positions_near_harmonic_number(h) for h in range(2,max_harmonic+1)}
  harms = {}
  for h,_ne in notes.items():
    for _,n,e in _ne:
      harms.setdefault(n,[])
      harms[n].append((e,h))
  for eh in harms.values():
    eh.sort()
  max_harm_oct = floor(log(max_harmonic,2))
  print('\n{} string:'.format(string_name))
  print('')
  print('  --- finger at ---   ------ harmonic ------')
  for a in octaves:
    print('')
    print('{} octave'.format(ordinal(a)))
    for b in range(12):
      n = a*12 + b + 1
      if n not in harms: continue
      print('')
      for e,h in harms[n]:
        hint, hoff = harmonic_interval(h)
        hnote = number_to_note(string_num + hint, relative_to=rel)
        e_sgn = '+' if e>=0 else '-'
        e = e_sgn + str(abs(e))
        note = number_to_note(string_num + n, relative_to=None)
        hoff_sgn = '+' if hoff>=0 else '-'
        hoff = hoff_sgn + str(abs(hoff))
        print('  {:<4} ({:>3} cents):   {:>2}   {:<4} ({:>3} cents)'.format(note,e,h,hnote,hoff))


###################################  Output  ###################################

def print_harmonics_for_notes(music, strings=None, instrument=None):
  """.
  Print a table of harmonics and their fingered positions for a sequence of notes.

  INPUT:

  - ``music`` -- string; a space-separated sequence of note/octave names in
    scientific notation

  - ``strings`` -- optional list of string names and octaves in scientific pitch
    notation.  For example, the 4 strings on a cello are denoted
    ('A3','D3','G2','C2')

  - ``instrument`` -- name of a stringed instrument

  Exactly one of ``strings`` or ``instrument`` must be given.  If
  ``instruments`` given, all four strings of the named instrument will be used.

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

    >>> print_harmonics_for_notes('G4 A4 B4', instrument='cello')
    <BLANKLINE>
    G4    IV Ef0   16.  6  1
    G4   III C0    -2.  4  1
    G4   III G2     0.  4  3
    G4    IV G2     2.  6  5
    <BLANKLINE>
    A4    II A0     2.  3  1
    A4     I A1     0.  2  1
    A4    II A1     2.  3  2
    <BLANKLINE>
    B4   III B0   -14.  5  1
    B4   III E0   -16.  5  2
    B4   III B1   -14.  5  3
    B4   III B2   -14.  5  4

  """
  romans = ['I','II','III','IV']
  if strings is None:
    if instrument is None:
      raise TypeError('Either "strings" or "instrument" must be given')
    strings = instrument_strings(instrument)
  str_nums = [note_to_number(s) for s in strings]
  for note in music.split():
    print('')
    ss = note_positions_near_harmonic_pitch(note, strings=strings)
    ss.sort(key=lambda s: (note_to_number(s[1])-str_nums[s[0]], s[0]))
    for str_ind,fing,fing_off,harm,node,_ in ss:
      fing_num = note_to_number(fing)
      fing_rel = number_to_note(fing_num, relative_to=strings[str_ind])
      print('{:<4} {:>3} {:<4} {:>3}. {:>2} {:>2}'.format(note, romans[str_ind], fing_rel, fing_off, harm, node))

###################################  Output  ###################################
 

def lilypond_harmonics(filename, string, octave=0, max_harmonic=16,
                       clef=None, instrument="cello",
                       note_spacing=200, staff_spacing=10,
                       append=False, page_break=False):
  """.

  Write lilypond output to engrave a harmonic fingering chart on given string
  and octave.

  INPUT:

  - ``filename`` -- name of Lilypond file in which to write the output

  - ``string`` -- pair (name,octave)  where ``name`` is the letter name and ``octave`` is Lilypond octave number

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

  OUTPUT:

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
  if type(octave) in (list,tuple):
    kw = {}
    kw['filename'] = filename
    kw['string'] = string
    kw['max_harmonic'] = max_harmonic
    kw['clef'] = clef
    kw['instrument'] = instrument
    kw['note_spacing'] = note_spacing
    kw['staff_spacing'] = staff_spacing
    kw['page_break'] = page_break
    for i,n in enumerate(octave):
      kw['octave'] = n
      kw['append'] = i > 0
      lilypond_harmonics(**kw)
    return

  string_name, string_octave = string
  string_num = note_to_number(string_name)
  string_name = number_to_note(string_num)

  loc_ottava = 0
  if clef is None:
    min_note_num = string_num + 12 * (string_octave + octave)
    if min_note_num <= 2:       # d
      clef = "bass"
    elif min_note_num <= 9:     # a
      clef = "tenor"
    elif min_note_num <= 23:    # b'
      clef = "treble"
    else:
      clef = "treble"
      loc_ottava = (min_note_num - 23)//12 + 1


  line = lambda s: s + '\n'

  
  suff = '{}{}{}'.format(string_name, chr(ord('a')+string_octave), chr(ord('a')+octave))

  pre = ''
  pre += line('\\' + 'version "2.20.0"')
  pre += line('\\include "english.ly"')
  pre += line('  \\header')
  pre += line('  {')
  pre += line('    copyright = "All rights to this work are waived under Creative Commons Licens CC0.  See https://creativecommons.org/publicdomain/zero/1.0/"')
  pre += line('    tagline = ##f')
  pre += line('    print-all-headers = ##t')
  pre += line('  }')
  pre += line('#(set-default-paper-size "letter")')
  pre += line('global = ')
  pre += line('{')
  pre += line('  \\omit Score.TimeSignature')
  pre += line('  \\cadenzaOn')
  pre += line('}')

  post = ''
  post += line('\\score')
  post += line('{')
  post += line('  \\header')
  post += line('  {')
  post += line('    tagline = ##f')
  post += line('    piece = \\markup \\column {{ "{} {}-string, {} octave" \\vspace #1 }}'.format(instrument.title(), string_name, ordinal(octave)))
  post += line('  }')
  post += line('  \\new StaffGroup')
  post += line('  <<')
  post += line('    \\new Staff = "pitch" \\with { instrumentName = "pitch" }')
  post += line('    <<')
  post += line('      \\new Voice = "pitch" {{ \\pitches{} }}'.format(suff))
  post += line('    >>')
  post += line('    \\new Staff = "location" \\with { instrumentName = "location" }')
  post += line('    << \\locations{} >>'.format(suff))
  post += line('    \\new Lyrics \\with { alignAboveContext = "pitch" }')
  post += line('    {')
  post += line('      \\lyricsto "pitch" \\nums{}'.format(suff))
  post += line('    }')
  post += line('  >>')
  post += line('}')
  post += line('')
  post += line('\\layout')
  post += line('{')
  post += line('  \\context {')
  post += line('    \\StaffGroup')
  post += line('    \\consists #Span_stem_engraver')
  post += line('  }')
  post += line('  \\context {')
  post += line('    \\Score')
  post += line('    \\override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/{})'.format(note_spacing))
  post += line('  }')
  post += line('}')
  post += line('  ')
  post += line('\\paper')
  post += line('{')
  post += line('  system-system-spacing = #\'((basic-distance . 1) (padding . {}))'.format(staff_spacing))
  post += line('  top-margin = 25')
  post += line('  left-margin = 25')
  post += line('  right-margin = 25')
  post += line('  ragged-bottom = ##t')
  post += line('  print-page-number = ##f')
  post += line('}')

  nums = line('nums{} = \\lyricmode'.format(suff))
  nums += '{'

  pitches = line('pitches{} ='.format(suff))
  pitches += line('{')
  pitches += line('  \\global')
  pitches += line('  \\clef "treble"')

  locations = line('locations{} ='.format(suff))
  locations += line('{')
  locations += line('  \\global')
  locations += line('  \\clef "{}"'.format(clef))
  locations += line('  \\ottava #{}'.format(loc_ottava))

  for h in range(2,max_harmonic+1):
    hint,hoct,hoff = harmonic_interval(h)
    hoct,hint = hint//12, hint%12
    hnote_num = hint + string_num
    q,r = hnote_num // 12, hnote_num % 12
    hoct += q + string_octave + octave
    hnote_num = r
    hnote = number_to_note(hnote_num, lower_case=True)

    if hoct >= 0:
      hoct_str = "'"*hoct
    else:
      hoct_str = ","*abs(hoct)

    hoff_sgn = '+' if hoff>=0 else '-'
    hoff_str = hoff_sgn + str(abs(hoff))

    first = True

    for _,n,e in note_positions_near_harmonic_number(h):
      if floor((n-1)/12) != octave: continue
      note_num = n + string_num
      note_octave = string_octave
      q,r = note_num // 12, note_num % 12
      note_num = r
      note_octave += q
      note = number_to_note(note_num, lower_case=True)
      if note_octave >= 0:
        note_octave_str = "'"*note_octave
      else:
        note_octave_str = ","*abs(note_octave)
      e_sgn = '+' if e>=0 else '-'
      e_str = e_sgn + str(abs(e))

      if first:
        first = False

        nums += '\n  "{}"'.format(h)

        pitches += line('  % {}'.format(h))
        pitches += line('  \\bar "|"')
        if hoct < 1:
          ottava = -1
        elif hoct > 2:
          ottava = min(2,hoct - 2)
        else:
          ottava = 0
        pitches += line('  \\ottava #{}'.format(ottava))
        pitches += line('  {}{} \\harmonic _\\markup{{"{}"}}'.format(hnote, hoct_str, hoff_str))

        locations += line('  % {}'.format(h))
        locations += line('  {}{} _\\markup{{"{}"}}'.format(note, note_octave_str, e_str))

      else:
        nums += ' ""'
        pitches += line('  {}{} \\harmonic'.format(hnote, hoct_str))
        locations += line('  {}{} _\\markup{{"{}"}}'.format(note, note_octave_str, e_str))

  nums += line('\n}')
  pitches += line('\\bar "|."')
  pitches += line('}')
  locations += line('}')

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
  F.write(nums)
  F.write('\n')
  F.write(pitches)
  F.write('\n')
  F.write(locations)
  F.write('\n')
  F.write(post)
  F.write('\n')

  F.close()


###################################  Output  ###################################

def lilypond_cello_strings(filename_base):
  """
  Produce a PDF fingering chart of harmonics on cello, for first 3 octaves on
  all strings.

  Requires pdftk and lilipond present on the system.

  For some reason the C string requires different spacing from the other
  strings, so is processes separately and a single PDF produced using pdftk.

  INPUT:

  - ``filename_base`` -- base of the filenames to use

  OUTPUT:

  - produces a pdf file whose name is filename_base with ".pdf" appended;
    intermediate output is in other files with names starting with filename_base

  """
  import os

  file0 = filename_base+'_tmp0'
  file1 = filename_base+'_tmp1'
  file2 = filename_base+'_tmp2'

  def process(f,s,o,a,b,**kwargs):
    lilypond_harmonics(f+'.ly',s,octave=o,append=a,page_break=b,**kwargs)

  s = ('a',0)
  process(file0,s,0,False,False)
  process(file0,s,1,True,True)
  process(file0,s,2,True,False)

  s = ('d',0)
  process(file0,s,0,True,False)
  process(file0,s,1,True,True)
  process(file0,s,2,True,False)

  s = ('g',-1)
  process(file0,s,0,True,False)
  process(file0,s,1,True,True)
  process(file0,s,2,True,False)

  s = ('c',-1)
  process(file1,s,0,False,False,note_spacing=100)
  process(file2,s,1,False,True)
  process(file2,s,2,True,False)

  os.system('lilypond {}'.format(file0))
  os.system('lilypond {}'.format(file1))
  os.system('lilypond {}'.format(file2))
  pdf0 = file0+'.pdf'
  pdf1 = file1+'.pdf'
  pdf2 = file2+'.pdf'
  os.system('pdftk A={} B={} C={} cat A B C output {}'.format(pdf0,pdf1,pdf2,filename_base+'.pdf'))



################################################################################
################################################################################
################################################################################
