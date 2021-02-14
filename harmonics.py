""".
harmonics.py

Module for analyzing positions of natural harmonics on a string,
relative to positions of fingered notes.

AUTHOR:

- David Zelinsky <dsz@dedekind.net>


COPYRIGHT NOTICE

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


TABLE OF CONTENTS:

- Global Data

- Utility Functions

  - note_number
  - note_name
  - ordinal_string

- Computation

  - note_positions_near_harmonic
  - harmonic_interval

- Output

  - print_harmonics
  - print_harmonics_by_position
  - lilypond_harmonics
  - lilypond_cello_strings

"""

from math import log, gcd, floor

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


def note_number(S):
  """
  Return the note number specified by S
  
  INPUT:

  - ``S`` -- a string representing a note in the chromatic scale, with
    accidentals indicated by a following instance of ``flat_symbol`` or
    ``sharp_symbol`` (probably "f" or "s" respectively).

  OUTPUT:

  - the number of half steps above C represented by the note

  EXAMPLES:

    >>> note_number('Fs')
    6
    >>> note_number('bf')
    10

  """
  name = S[0].upper()
  n = note_nums[name]
  if len(S) > 1:
    acc = S[1]
    if acc == sharp_symbol:
      n +=1
    elif acc == flat_symbol:
      n -= 1
    else:
      raise ValueError('unknown accidental {}'.format(acc))
  return n

#############################  Utility Functions  ##############################

def note_name(n, lower_case=False, prefer_flat=False):
  """.

  Return the name of note with scale degree ``n`` in chromatic scale based on C

  INPUT:

  - ``n`` -- integer; will be reduced modulo 12

  - ``lower`` -- boolean (default: False); whether to return the note name in
    lower rather than upper case

  OUTPUT:

  - a one- or two-character string representing the note, with sharp or flat
    indicated by ``sharp_symbol`` or ``flat_symbol`` as second character.
    Sharps will be used rather than the enharmonic flat, unles ``prefer_flat``
    is True.

  EXAMPLES:

    >>> print(note_name(8))
    Gs
    >>> print(note_name(8, lower_case=True))
    gs
    >>> print(note_name(8, prefer_flat=True))
    Af

  """
  m = n % 12
  S = note_names.get(m)
  if S is not None:
    return S.lower() if lower_case else S
  if prefer_flat:
    m = (n+1) % 12
    acc = flat_symbol
  else:
    m = (n-1) % 12
    acc = sharp_symbol
  S = note_names.get(m)
  if S is None:
    raise ValueError('no known note numbered {}'.format(m))
  return (S.lower() if lower_case else S) + acc



################################################################################
################################  Computation  #################################
################################################################################


def note_positions_near_harmonic(h):
  """.
  Return the note numbers and offset of the fingered notes nearest the each node
  of given harmonic.

  INPUT:

  - ``h`` -- positive integer; the harmonic number

  OUTPUT:

  - ordered list of pairs ``(n,e)``, one for each of the ``h-1`` nodes of the harmonic, where

    - ``n`` is the number of half steps above the open string of the
      note whose fingered location (in tempered pitch) is nearest the harmonic node

    - ``e`` is the offset in cents (hundredths of a half step) from
      the location of the fingered note to the harmonic node.
      Stopping the string at the location of the harmonic node will
      produce a note that is ``e`` cents sharp if ``e > 0`` or ``|e|``
      cents flat if ``e < 0``, relative to the note ``n`` tempered
      half steps above the open string.

  EXAMPLES:

    >>> note_positions_near_harmonic(1)
    []
    >>> note_positions_near_harmonic(2)
    [(12, 0)]
    >>> note_positions_near_harmonic(3)
    [(7, 2), (19, 2)]
    >>> note_positions_near_harmonic(4)
    [(5, -2), (24, 0)]

  """
  if h < 0:
    raise TypeError('argument must be a positive integer')
  notes = []
  for m in range(1,h):
    if gcd(m,h) > 1: continue
    lg = log(h/m,HS)
    n = int(round(lg))
    e = int(round(100*(lg-n)))
    notes.append((n,e))
  notes.reverse()
  return notes

################################  Computation  #################################

def harmonic_interval(h):
  """Return the chromatic interval, octave, and offset of a harmonic.

  INPUT:

  - ``h`` -- positive integer; the harmonic number

  OUTPUT:

  - tuple ``(num, octave, offset)`` representing the pitch of the harmonic
    relative to the open string:

    - ``num`` -- non-negative integer; the number of half steps from the open
      string to the note N in tempered tuning closest the first octave shift of
      the harmonic

    - ``octave`` -- number of octaves from the note near N to the actual pitch
      of the harmonic

    - ``offset`` -- number of cents from note N (in tempered tuning) to the
      actual pitch of the octave-shifted harmonic.  If ``offset`` is positive,
      the harmonic sounds that much sharp relative to the tempered note; if
      negative it sounds flat but the indicated magnitude.

  EXAMPLES:

    >>> H.harmonic_interval(1)
    (0, 0, 0)
    >>> H.harmonic_interval(2)
    (0, 1, 0)
    >>> H.harmonic_interval(3)
    (7, 1, 2)

  The last example indicates that the 3rd harmonic sounds close to 7 half steps
  above the fundamental (a perfect 5th), shifted up one octave, and 2 cents
  sharp.

  """
  hoct0 = 0
  while h % 2 == 0:
    hoct0 += 1
    h //= 2
  logh = log(h,HS)
  hint = round(logh)
  hoff = round(100*(logh - hint))
  hoct, hint = hint // 12, hint % 12
  hoct += hoct0
  return hint, hoct, hoff



################################################################################
###################################  Output  ###################################
################################################################################

def print_harmonics(string, octave=0, max_harmonic=16):
  """.

  Print a table locations of all harmonic nodes in a given octave.

  INPUT:

  - ``string`` -- note name of an open string

  - ``octave`` -- integer (default: 0); octaves up from the first in which to
    show node locations

  - ``max_harmonic`` -- positive integer (default: 16); largest harmonic number
    to include

  OUTPUT:

  - a string, showing a table of harmonics and their node locations in the given
    octave.  Each row of the table gives this data:

   - harmonic number

   - name of note closest to the sound the harmonic, with a number of '+' signs
     prepended indicating the octaves above the open string

  - how much sharp or flat the harmonic sounds relative to the named note in
    tempered pitch; this is given in cents, with positive meaning sharp,
    negative flat

  - name of fingered note closest to a node of the harmonic

  - number of cents above (if positive) or below (if negative) the named note
    where the harmonic node occurs.

  EXAMPLES:

    >>> print_harmonics('A',octave=1,max_harmonic=8)

    A string, 2nd octave:

      ----- harmonic -----    -- finger at --


       3   +E  ( +2 cents):   E   ( +2 cents)

       4  ++A  ( +0 cents):   A   ( +0 cents)

       5  ++Cs (-14 cents):   Cs  (-14 cents)


       7  ++G  (-31 cents):   C   (-33 cents)
       7  ++G  (-31 cents):   G   (-31 cents)

       8 +++A  ( +0 cents):   D   ( -2 cents)

  """
  string_num = note_number(string)
  max_harm_oct = floor(log(max_harmonic,2))
  ndashes = 7+max_harm_oct
  ndashes0 = ndashes//2
  ndashes1 = ndashes - ndashes0
  dashes0 = '-'*ndashes0
  dashes1 = '-'*ndashes1
  print('\n{} string, {} octave:'.format(note_name(string_num), ordinal(octave)))
  print('')
  print('  {} harmonic {}    -- finger at --'.format(dashes0,dashes1))
  for h in range(2,max_harmonic+1):
    hint,hoct,hoff = harmonic_interval(h)
    print('')
    for n,e in note_positions_near_harmonic(h):
      if floor((n-1)/12) != octave: continue
      note = note_name(n+string_num)
      hnote = note_name(string_num + hint)
      e_sgn = '+' if e>=0 else '-'
      e = e_sgn + str(abs(e))
      note = note_name(string_num + n)
      hoff_sgn = '+' if hoff>=0 else '-'
      hoff_str = hoff_sgn + str(abs(hoff))
      print('  {0:>2} {1:>{2}}{3:<2} ({4:>3} cents):   {5:<2}  ({6:>3} cents)'.format(h,'+'*hoct,max_harm_oct,hnote,hoff_str,note,e))


###################################  Output  ###################################


def print_harmonics_by_position(string, octaves=(0,), max_harmonic=16):
  """.

  Print a table notes on given string in given octave, and the harmonics nearest them.

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

    A string:

      -- finger at --   ----- harmonic -----

    1st octave

      B   (+31 cents):   8 +++A  ( +0 cents)

      C   (-33 cents):   7  ++G  (-31 cents)
      C   (+16 cents):   6  ++E  ( +2 cents)

      Cs  (-14 cents):   5  ++Cs (-14 cents)

      D   ( -2 cents):   4  ++A  ( +0 cents)

      Ds  (-17 cents):   7  ++G  (-31 cents)

      E   ( +2 cents):   3   +E  ( +2 cents)

      F   (+14 cents):   8 +++A  ( +0 cents)

      Fs  (-16 cents):   5  ++Cs (-14 cents)

      G   (-31 cents):   7  ++G  (-31 cents)

      A   ( +0 cents):   2   +A  ( +0 cents)


    >>> print_harmonics_by_position('A', octaves=(0,1), max_harmonic=4)

    A string:

      -- finger at --   ---- harmonic -----

    1st octave

      D   ( -2 cents):   4 ++A  ( +0 cents)

      E   ( +2 cents):   3  +E  ( +2 cents)

      A   ( +0 cents):   2  +A  ( +0 cents)

    2nd octave

      E   ( +2 cents):   3  +E  ( +2 cents)

      A   ( +0 cents):   4 ++A  ( +0 cents)

  """
  string_num = note_number(string)
  notes = {h:note_positions_near_harmonic(h) for h in range(2,max_harmonic+1)}
  harms = {}
  for h,ne in notes.items():
    for n,e in ne:
      harms.setdefault(n,[])
      harms[n].append((e,h))
  for eh in harms.values():
    eh.sort()
  max_harm_oct = floor(log(max_harmonic,2))
  ndashes = 7 + max_harm_oct
  ndashes0 = ndashes//2
  ndashes1 = ndashes - ndashes0
  dashes0 = '-'*ndashes0
  dashes1 = '-'*ndashes1
  print('\n{} string:'.format(note_name(string_num)))
  print('')
  print('  -- finger at --   {} harmonic {}'.format(dashes0,dashes1))
  for a in octaves:
    print('')
    print('{} octave'.format(ordinal(a)))
    for b in range(12):
      n = a*12 + b + 1
      if n not in harms: continue
      print('')
      for e,h in harms[n]:
        hint, hoct, hoff = harmonic_interval(h)
        hnote = note_name(string_num + hint)
        e_sgn = '+' if e>=0 else '-'
        e = e_sgn + str(abs(e))
        note = note_name(string_num + n)
        hoff_sgn = '+' if hoff>=0 else '-'
        hoff = hoff_sgn + str(abs(hoff))
        print('  {0:<2}  ({1:>3} cents):  {2:>2} {3:>{4}}{5:<2} ({6:>3} cents)'.format(note,e,h,'+'*hoct,max_harm_oct,hnote,hoff))


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
  string_num = note_number(string_name)
  string_name = note_name(string_num)

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

    hnote_num = hint + string_num
    q,r = hnote_num // 12, hnote_num % 12
    hoct += q + string_octave + octave
    hnote_num = r
    hnote = note_name(hnote_num, lower_case=True)

    if hoct >= 0:
      hoct_str = "'"*hoct
    else:
      hoct_str = ","*abs(hoct)

    hoff_sgn = '+' if hoff>=0 else '-'
    hoff_str = hoff_sgn + str(abs(hoff))

    first = True

    for n,e in note_positions_near_harmonic(h):
      if floor((n-1)/12) != octave: continue
      note_num = n + string_num
      note_octave = string_octave
      q,r = note_num // 12, note_num % 12
      note_num = r
      note_octave += q
      note = note_name(note_num, lower_case=True)
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
