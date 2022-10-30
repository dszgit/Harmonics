\version "2.20.0"
\include "english.ly"

\paper{
  line-width = 6\in
}

\header{
  tagline = ##f
  title = \markup{
    \center-column {
      \vspace #10
      "Harmonics on the Cello"
      \vspace #2
    }
  }
  copyright = \markup{
    \center-column {
      "All rights to this work are granted under Creative Commons License CC0."
      "See https://creativecommons.org/publicdomain/zero/1.0/"
    }
  }
}

sharp = \markup{\musicglyph "accidentals.sharp"}

\markuplist {
  \column-lines {
    \vspace #1

    \line{This is a catalog of fingerings for harmonics on the cello.}
    
  } \vspace #1 \justify {

    For each string, and each of the first three octaves on that
    string, there is a double staff.  For each of the first 16
    harmonics (multiples of the open string pitch) one bar is shown,
    with the harmonic note in the upper staff and all the possible
    fingerings in the lower staff.

  } \vspace #1 \justify {

    Each bar corresponds to one harmonic note.  The number of the harmonic
    (\italic {i.e.} multiple of the string pitch) is shown above the bar.  Below
    the bar (on upper staff) is indicated the number of cents sharp (+) or flat
    (-) that the harmonic sounds relative to tempered tuning.

  } \vspace #1 \justify {

    The lower staff shows all the possible locations to play that
    harmonic, within the particular octave.  Below each note is
    indicated the number of cents above (+) or below (-) that note
    where the actual harmonic node is located.

  } \vspace #1 \justify {

    For example, referring to the next page, for the 1st octave on the A string,
    the 5th harmonic sounds as a C{\hspace #-.3 \raise #.8 {\abs-fontsize #8
    {\sharp}}} but is 14 cents flat.  It can be fingered at 14 cents below the
    C{\hspace #-.3 \raise #.8 {\abs-fontsize #8 {\sharp}}} in 1st position, or
    at 16 cents below the F-sharp in 4th position.

  }

}
