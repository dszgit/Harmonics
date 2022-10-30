# String Harmonics

Module for analyzing positions of natural harmonics on a stringed
instrument relative to positions of fingered notes.

## AUTHOR:

- David Zelinsky <dsz@dedekind.net>


## COPYRIGHT NOTICE:

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
section of the code for more explanation.



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

- harmonics.py

  - Global Data

  - Utility Functions

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

  - Computation

    - harmonic_interval
    - note_positions_near_harmonic_number
    - notes_near_harmonic_on_string
    - note_positions_near_harmonic_pitch

  - Output

    - print_harmonics
    - print_harmonics_by_position
    - print_harmonics_for_notes
    - lilypond_harmonics
    - lilypond_cello_harmonics

- intro.ly

  - introductory front-matter for lilypond_cello_harmonics

- cello-harmonics.ly

  - lilypond source file produced with lilypond_cello_harmonics

- cello-harmonics.pdf

  - typeset catalog of cello harmonics

