\include "intro.ly"



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\pageBreak

\version "2.20.0"
\include "english.ly"
  \header
  {
    copyright = \markup{
      \center-column {
        "All rights to this work are granted under Creative Commons License CC0."
        "See https://creativecommons.org/publicdomain/zero/1.0/"
    }
  }
    tagline = ##f
    print-all-headers = ##t
  }
#(set-default-paper-size "letter")
global = 
{
  \omit Score.TimeSignature
}

pitchesAa =
{
  \global
  % 3
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #0 e''\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x3"} }
  \cadenzaOff
  % 4
\bar "|"
 \cadenzaOn
  \clef "treble" a''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x4"} }
  \cadenzaOff
  % 5
\bar "|"
 \cadenzaOn
  \clef "treble" cs'''\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x5"} }
  \clef "treble" cs'''\harmonic
  \cadenzaOff
  % 6
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #1 e'''\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x6"} }
  \cadenzaOff
  % 7
\bar "|"
 \cadenzaOn
  \clef "treble" g'''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x7"} }
  \clef "treble" g'''\harmonic
  \clef "treble" g'''\harmonic
  \cadenzaOff
  % 8
\bar "|"
 \cadenzaOn
  \clef "treble" a'''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x8"} }
  \clef "treble" a'''\harmonic
  \cadenzaOff
  % 9
\bar "|"
 \cadenzaOn
  \clef "treble" b'''\harmonic_\markup{"+4"}^\markup{ \raise #3 {"x9"} }
  \clef "treble" b'''\harmonic
  \clef "treble" b'''\harmonic
  \cadenzaOff
  % 10
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #2 cs''''\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x10"} }
  \clef "treble" cs''''\harmonic
  \cadenzaOff
  % 11
\bar "|"
 \cadenzaOn
  \clef "treble" ef''''\harmonic_\markup{"-49"}^\markup{ \raise #3 {"x11"} }
  \clef "treble" ef''''\harmonic
  \clef "treble" ef''''\harmonic
  \clef "treble" ef''''\harmonic
  \clef "treble" ef''''\harmonic
  \cadenzaOff
  % 12
\bar "|"
 \cadenzaOn
  \clef "treble" e''''\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x12"} }
  \clef "treble" e''''\harmonic
  \cadenzaOff
  % 13
\bar "|"
 \cadenzaOn
  \clef "treble" f''''\harmonic_\markup{"+41"}^\markup{ \raise #3 {"x13"} }
  \clef "treble" f''''\harmonic
  \clef "treble" f''''\harmonic
  \clef "treble" f''''\harmonic
  \clef "treble" f''''\harmonic
  \clef "treble" f''''\harmonic
  \cadenzaOff
  % 14
\bar "|"
 \cadenzaOn
  \clef "treble" g''''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x14"} }
  \clef "treble" g''''\harmonic
  \clef "treble" g''''\harmonic
  \cadenzaOff
  % 15
\bar "|"
 \cadenzaOn
  \clef "treble" gs''''\harmonic_\markup{"-12"}^\markup{ \raise #3 {"x15"} }
  \clef "treble" gs''''\harmonic
  \clef "treble" gs''''\harmonic
  \clef "treble" gs''''\harmonic
  \cadenzaOff
  % 16
\bar "|"
 \cadenzaOn
  \clef "treble" a''''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x16"} }
  \clef "treble" a''''\harmonic
  \clef "treble" a''''\harmonic
  \clef "treble" a''''\harmonic
  \cadenzaOff
  \bar "|."
}

locationsAa =
{
  \global
 \cadenzaOn
  \clef "tenor" \ottava #0 e'_\markup{"+2"}
 \cadenzaOn
  \clef "tenor" d'_\markup{"-2"}
 \cadenzaOn
  \clef "bass" cs'_\markup{"-14"}
  \clef "tenor" fs'_\markup{"-16"}
 \cadenzaOn
  \clef "bass" c'_\markup{"+16"}
 \cadenzaOn
  \clef "bass" c'_\markup{"-33"}
  \clef "tenor" ef'_\markup{"-17"}
  \clef "tenor" g'_\markup{"-31"}
 \cadenzaOn
  \clef "bass" b_\markup{"+31"}
  \clef "tenor" f'_\markup{"+14"}
 \cadenzaOn
  \clef "bass" b_\markup{"+4"}
  \clef "bass" cs'_\markup{"+35"}
  \clef "tenor" g'_\markup{"+18"}
 \cadenzaOn
  \clef "bass" b_\markup{"-18"}
  \clef "tenor" ef'_\markup{"+17"}
 \cadenzaOn
  \clef "bass" b_\markup{"-35"}
  \clef "bass" c'_\markup{"+47"}
  \clef "tenor" ef'_\markup{"-49"}
  \clef "tenor" f'_\markup{"-18"}
  \clef "tenor" g'_\markup{"+49"}
 \cadenzaOn
  \clef "bass" b_\markup{"-49"}
  \clef "tenor" fs'_\markup{"+33"}
 \cadenzaOn
  \clef "bass" bf_\markup{"+39"}
  \clef "bass" c'_\markup{"-11"}
  \clef "tenor" d'_\markup{"-46"}
  \clef "tenor" ef'_\markup{"+37"}
  \clef "tenor" f'_\markup{"+41"}
  \clef "tenor" gs'_\markup{"-28"}
 \cadenzaOn
  \clef "bass" bf_\markup{"+28"}
  \clef "bass" cs'_\markup{"+18"}
  \clef "tenor" f'_\markup{"-35"}
 \cadenzaOn
  \clef "bass" bf_\markup{"+19"}
  \clef "bass" b_\markup{"+48"}
  \clef "tenor" d'_\markup{"+37"}
  \clef "tenor" gs'_\markup{"-12"}
 \cadenzaOn
  \clef "bass" bf_\markup{"+12"}
  \clef "bass" cs'_\markup{"-41"}
  \clef "tenor" ef'_\markup{"+49"}
  \clef "tenor" g'_\markup{"-4"}
  \bar "|."
}

\score
{
  \header
  {
    tagline = ##f
    piece = \markup \column { "Cello A-string, 1st octave" \vspace #1 }
  }
  \new StaffGroup
  <<
    \new Staff = "pitch" \with { instrumentName = "pitch" }
    <<
      \new Voice = "pitch" { \pitchesAa }
    >>
    \new Staff = "location" \with { instrumentName = "location" }
    << \locationsAa >>
  >>
}

\layout
{
  \context {
    \StaffGroup
    \consists #Span_stem_engraver
  }
  \context {
    \Score
    \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/200)
  }
}
  
\paper
{
  system-system-spacing = #'((basic-distance . 1) (padding . 5))
  top-margin = 25
  left-margin = 25
  right-margin = 25
  ragged-bottom = ##t
  print-page-number = ##f
}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\pageBreak

\version "2.20.0"
\include "english.ly"
  \header
  {
    copyright = \markup{
      \center-column {
        "All rights to this work are granted under Creative Commons License CC0."
        "See https://creativecommons.org/publicdomain/zero/1.0/"
    }
  }
    tagline = ##f
    print-all-headers = ##t
  }
#(set-default-paper-size "letter")
global = 
{
  \omit Score.TimeSignature
}

pitchesAb =
{
  \global
  % 2
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #0 a'\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x2"} }
  \cadenzaOff
  % 3
\bar "|"
 \cadenzaOn
  \clef "treble" e''\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x3"} }
  \cadenzaOff
  % 5
\bar "|"
 \cadenzaOn
  \clef "treble" cs'''\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x5"} }
  \cadenzaOff
  % 7
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #1 g'''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x7"} }
  \clef "treble" g'''\harmonic
  \cadenzaOff
  % 8
\bar "|"
 \cadenzaOn
  \clef "treble" a'''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x8"} }
  \cadenzaOff
  % 9
\bar "|"
 \cadenzaOn
  \clef "treble" b'''\harmonic_\markup{"+4"}^\markup{ \raise #3 {"x9"} }
  \cadenzaOff
  % 10
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #2 cs''''\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x10"} }
  \cadenzaOff
  % 11
\bar "|"
 \cadenzaOn
  \clef "treble" ef''''\harmonic_\markup{"-49"}^\markup{ \raise #3 {"x11"} }
  \clef "treble" ef''''\harmonic
  \clef "treble" ef''''\harmonic
  \cadenzaOff
  % 12
\bar "|"
 \cadenzaOn
  \clef "treble" e''''\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x12"} }
  \cadenzaOff
  % 13
\bar "|"
 \cadenzaOn
  \clef "treble" f''''\harmonic_\markup{"+41"}^\markup{ \raise #3 {"x13"} }
  \clef "treble" f''''\harmonic
  \clef "treble" f''''\harmonic
  \cadenzaOff
  % 14
\bar "|"
 \cadenzaOn
  \clef "treble" g''''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x14"} }
  \cadenzaOff
  % 15
\bar "|"
 \cadenzaOn
  \clef "treble" gs''''\harmonic_\markup{"-12"}^\markup{ \raise #3 {"x15"} }
  \clef "treble" gs''''\harmonic
  \cadenzaOff
  % 16
\bar "|"
 \cadenzaOn
  \clef "treble" a''''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x16"} }
  \clef "treble" a''''\harmonic
  \cadenzaOff
  \bar "|."
}

locationsAb =
{
  \global
 \cadenzaOn
  \clef "treble" \ottava #0 a'_\markup{"+0"}
 \cadenzaOn
  \clef "treble" e''_\markup{"+2"}
 \cadenzaOn
  \clef "treble" cs''_\markup{"-14"}
 \cadenzaOn
  \clef "treble" c''_\markup{"-33"}
  \clef "treble" g''_\markup{"-31"}
 \cadenzaOn
  \clef "treble" d''_\markup{"-2"}
 \cadenzaOn
  \clef "treble" b'_\markup{"+4"}
 \cadenzaOn
  \clef "treble" fs''_\markup{"-16"}
 \cadenzaOn
  \clef "treble" b'_\markup{"-35"}
  \clef "treble" ef''_\markup{"-49"}
  \clef "treble" g''_\markup{"+49"}
 \cadenzaOn
  \clef "treble" c''_\markup{"+16"}
 \cadenzaOn
  \clef "treble" bf'_\markup{"+39"}
  \clef "treble" d''_\markup{"-46"}
  \clef "treble" f''_\markup{"+41"}
 \cadenzaOn
  \clef "treble" ef''_\markup{"-17"}
 \cadenzaOn
  \clef "treble" bf'_\markup{"+19"}
  \clef "treble" gs''_\markup{"-12"}
 \cadenzaOn
  \clef "treble" b'_\markup{"+31"}
  \clef "treble" f''_\markup{"+14"}
  \bar "|."
}

\score
{
  \header
  {
    tagline = ##f
    piece = \markup \column { "Cello A-string, 2nd octave" \vspace #1 }
  }
  \new StaffGroup
  <<
    \new Staff = "pitch" \with { instrumentName = "pitch" }
    <<
      \new Voice = "pitch" { \pitchesAb }
    >>
    \new Staff = "location" \with { instrumentName = "location" }
    << \locationsAb >>
  >>
}

\layout
{
  \context {
    \StaffGroup
    \consists #Span_stem_engraver
  }
  \context {
    \Score
    \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/200)
  }
}
  
\paper
{
  system-system-spacing = #'((basic-distance . 1) (padding . 5))
  top-margin = 25
  left-margin = 25
  right-margin = 25
  ragged-bottom = ##t
  print-page-number = ##f
}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\version "2.20.0"
\include "english.ly"
  \header
  {
    copyright = \markup{
      \center-column {
        "All rights to this work are granted under Creative Commons License CC0."
        "See https://creativecommons.org/publicdomain/zero/1.0/"
    }
  }
    tagline = ##f
    print-all-headers = ##t
  }
#(set-default-paper-size "letter")
global = 
{
  \omit Score.TimeSignature
}

pitchesAc =
{
  \global
  % 4
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #0 a''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x4"} }
  \cadenzaOff
  % 5
\bar "|"
 \cadenzaOn
  \clef "treble" cs'''\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x5"} }
  \cadenzaOff
  % 6
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #1 e'''\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x6"} }
  \cadenzaOff
  % 7
\bar "|"
 \cadenzaOn
  \clef "treble" g'''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x7"} }
  \cadenzaOff
  % 9
\bar "|"
 \cadenzaOn
  \clef "treble" b'''\harmonic_\markup{"+4"}^\markup{ \raise #3 {"x9"} }
  \cadenzaOff
  % 11
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #2 ef''''\harmonic_\markup{"-49"}^\markup{ \raise #3 {"x11"} }
  \cadenzaOff
  % 13
\bar "|"
 \cadenzaOn
  \clef "treble" f''''\harmonic_\markup{"+41"}^\markup{ \raise #3 {"x13"} }
  \clef "treble" f''''\harmonic
  \cadenzaOff
  % 14
\bar "|"
 \cadenzaOn
  \clef "treble" g''''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x14"} }
  \cadenzaOff
  % 15
\bar "|"
 \cadenzaOn
  \clef "treble" gs''''\harmonic_\markup{"-12"}^\markup{ \raise #3 {"x15"} }
  \cadenzaOff
  % 16
\bar "|"
 \cadenzaOn
  \clef "treble" a''''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x16"} }
  \cadenzaOff
  \bar "|."
}

locationsAc =
{
  \global
 \cadenzaOn
  \clef "treble" \ottava #0 a''_\markup{"+0"}
 \cadenzaOn
  \clef "treble" cs'''_\markup{"-14"}
 \cadenzaOn
  \clef "treble" \ottava #1 e'''_\markup{"+2"}
 \cadenzaOn
  \clef "treble" g'''_\markup{"-31"}
 \cadenzaOn
  \clef "treble" \ottava #0 b''_\markup{"+4"}
 \cadenzaOn
  \clef "treble" \ottava #1 ef'''_\markup{"-49"}
 \cadenzaOn
  \clef "treble" \ottava #0 bf''_\markup{"+39"}
  \clef "treble" \ottava #1 f'''_\markup{"+41"}
 \cadenzaOn
  \clef "treble" \ottava #0 c'''_\markup{"-33"}
 \cadenzaOn
  \clef "treble" \ottava #1 gs'''_\markup{"-12"}
 \cadenzaOn
  \clef "treble" d'''_\markup{"-2"}
  \bar "|."
}

\score
{
  \header
  {
    tagline = ##f
    piece = \markup \column { "Cello A-string, 3rd octave" \vspace #1 }
  }
  \new StaffGroup
  <<
    \new Staff = "pitch" \with { instrumentName = "pitch" }
    <<
      \new Voice = "pitch" { \pitchesAc }
    >>
    \new Staff = "location" \with { instrumentName = "location" }
    << \locationsAc >>
  >>
}

\layout
{
  \context {
    \StaffGroup
    \consists #Span_stem_engraver
  }
  \context {
    \Score
    \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/200)
  }
}
  
\paper
{
  system-system-spacing = #'((basic-distance . 1) (padding . 5))
  top-margin = 25
  left-margin = 25
  right-margin = 25
  ragged-bottom = ##t
  print-page-number = ##f
}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\pageBreak

\version "2.20.0"
\include "english.ly"
  \header
  {
    copyright = \markup{
      \center-column {
        "All rights to this work are granted under Creative Commons License CC0."
        "See https://creativecommons.org/publicdomain/zero/1.0/"
    }
  }
    tagline = ##f
    print-all-headers = ##t
  }
#(set-default-paper-size "letter")
global = 
{
  \omit Score.TimeSignature
}

pitchesDa =
{
  \global
  % 3
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #0 a'\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x3"} }
  \cadenzaOff
  % 4
\bar "|"
 \cadenzaOn
  \clef "treble" d''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x4"} }
  \cadenzaOff
  % 5
\bar "|"
 \cadenzaOn
  \clef "treble" fs''\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x5"} }
  \clef "treble" fs''\harmonic
  \cadenzaOff
  % 6
\bar "|"
 \cadenzaOn
  \clef "treble" a''\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x6"} }
  \cadenzaOff
  % 7
\bar "|"
 \cadenzaOn
  \clef "treble" c'''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x7"} }
  \clef "treble" c'''\harmonic
  \clef "treble" c'''\harmonic
  \cadenzaOff
  % 8
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #1 d'''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x8"} }
  \clef "treble" d'''\harmonic
  \cadenzaOff
  % 9
\bar "|"
 \cadenzaOn
  \clef "treble" e'''\harmonic_\markup{"+4"}^\markup{ \raise #3 {"x9"} }
  \clef "treble" e'''\harmonic
  \clef "treble" e'''\harmonic
  \cadenzaOff
  % 10
\bar "|"
 \cadenzaOn
  \clef "treble" fs'''\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x10"} }
  \clef "treble" fs'''\harmonic
  \cadenzaOff
  % 11
\bar "|"
 \cadenzaOn
  \clef "treble" gs'''\harmonic_\markup{"-49"}^\markup{ \raise #3 {"x11"} }
  \clef "treble" gs'''\harmonic
  \clef "treble" gs'''\harmonic
  \clef "treble" gs'''\harmonic
  \clef "treble" gs'''\harmonic
  \cadenzaOff
  % 12
\bar "|"
 \cadenzaOn
  \clef "treble" a'''\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x12"} }
  \clef "treble" a'''\harmonic
  \cadenzaOff
  % 13
\bar "|"
 \cadenzaOn
  \clef "treble" bf'''\harmonic_\markup{"+41"}^\markup{ \raise #3 {"x13"} }
  \clef "treble" bf'''\harmonic
  \clef "treble" bf'''\harmonic
  \clef "treble" bf'''\harmonic
  \clef "treble" bf'''\harmonic
  \clef "treble" bf'''\harmonic
  \cadenzaOff
  % 14
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #2 c''''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x14"} }
  \clef "treble" c''''\harmonic
  \clef "treble" c''''\harmonic
  \cadenzaOff
  % 15
\bar "|"
 \cadenzaOn
  \clef "treble" cs''''\harmonic_\markup{"-12"}^\markup{ \raise #3 {"x15"} }
  \clef "treble" cs''''\harmonic
  \clef "treble" cs''''\harmonic
  \clef "treble" cs''''\harmonic
  \cadenzaOff
  % 16
\bar "|"
 \cadenzaOn
  \clef "treble" d''''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x16"} }
  \clef "treble" d''''\harmonic
  \clef "treble" d''''\harmonic
  \clef "treble" d''''\harmonic
  \cadenzaOff
  \bar "|."
}

locationsDa =
{
  \global
 \cadenzaOn
  \clef "bass" \ottava #0 a_\markup{"+2"}
 \cadenzaOn
  \clef "bass" g_\markup{"-2"}
 \cadenzaOn
  \clef "bass" fs_\markup{"-14"}
  \clef "bass" b_\markup{"-16"}
 \cadenzaOn
  \clef "bass" f_\markup{"+16"}
 \cadenzaOn
  \clef "bass" f_\markup{"-33"}
  \clef "bass" gs_\markup{"-17"}
  \clef "bass" c'_\markup{"-31"}
 \cadenzaOn
  \clef "bass" e_\markup{"+31"}
  \clef "bass" bf_\markup{"+14"}
 \cadenzaOn
  \clef "bass" e_\markup{"+4"}
  \clef "bass" fs_\markup{"+35"}
  \clef "bass" c'_\markup{"+18"}
 \cadenzaOn
  \clef "bass" e_\markup{"-18"}
  \clef "bass" gs_\markup{"+17"}
 \cadenzaOn
  \clef "bass" e_\markup{"-35"}
  \clef "bass" f_\markup{"+47"}
  \clef "bass" gs_\markup{"-49"}
  \clef "bass" bf_\markup{"-18"}
  \clef "bass" c'_\markup{"+49"}
 \cadenzaOn
  \clef "bass" e_\markup{"-49"}
  \clef "bass" b_\markup{"+33"}
 \cadenzaOn
  \clef "bass" ef_\markup{"+39"}
  \clef "bass" f_\markup{"-11"}
  \clef "bass" g_\markup{"-46"}
  \clef "bass" gs_\markup{"+37"}
  \clef "bass" bf_\markup{"+41"}
  \clef "bass" cs'_\markup{"-28"}
 \cadenzaOn
  \clef "bass" ef_\markup{"+28"}
  \clef "bass" fs_\markup{"+18"}
  \clef "bass" bf_\markup{"-35"}
 \cadenzaOn
  \clef "bass" ef_\markup{"+19"}
  \clef "bass" e_\markup{"+48"}
  \clef "bass" g_\markup{"+37"}
  \clef "bass" cs'_\markup{"-12"}
 \cadenzaOn
  \clef "bass" ef_\markup{"+12"}
  \clef "bass" fs_\markup{"-41"}
  \clef "bass" gs_\markup{"+49"}
  \clef "bass" c'_\markup{"-4"}
  \bar "|."
}

\score
{
  \header
  {
    tagline = ##f
    piece = \markup \column { "Cello D-string, 1st octave" \vspace #1 }
  }
  \new StaffGroup
  <<
    \new Staff = "pitch" \with { instrumentName = "pitch" }
    <<
      \new Voice = "pitch" { \pitchesDa }
    >>
    \new Staff = "location" \with { instrumentName = "location" }
    << \locationsDa >>
  >>
}

\layout
{
  \context {
    \StaffGroup
    \consists #Span_stem_engraver
  }
  \context {
    \Score
    \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/200)
  }
}
  
\paper
{
  system-system-spacing = #'((basic-distance . 1) (padding . 5))
  top-margin = 25
  left-margin = 25
  right-margin = 25
  ragged-bottom = ##t
  print-page-number = ##f
}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\pageBreak

\version "2.20.0"
\include "english.ly"
  \header
  {
    copyright = \markup{
      \center-column {
        "All rights to this work are granted under Creative Commons License CC0."
        "See https://creativecommons.org/publicdomain/zero/1.0/"
    }
  }
    tagline = ##f
    print-all-headers = ##t
  }
#(set-default-paper-size "letter")
global = 
{
  \omit Score.TimeSignature
}

pitchesDb =
{
  \global
  % 2
\bar "|"
 \cadenzaOn
  \clef "tenor" \ottava #0 d'\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x2"} }
  \cadenzaOff
  % 3
\bar "|"
 \cadenzaOn
  \clef "treble" a'\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x3"} }
  \cadenzaOff
  % 5
\bar "|"
 \cadenzaOn
  \clef "treble" fs''\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x5"} }
  \cadenzaOff
  % 7
\bar "|"
 \cadenzaOn
  \clef "treble" c'''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x7"} }
  \clef "treble" c'''\harmonic
  \cadenzaOff
  % 8
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #1 d'''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x8"} }
  \cadenzaOff
  % 9
\bar "|"
 \cadenzaOn
  \clef "treble" e'''\harmonic_\markup{"+4"}^\markup{ \raise #3 {"x9"} }
  \cadenzaOff
  % 10
\bar "|"
 \cadenzaOn
  \clef "treble" fs'''\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x10"} }
  \cadenzaOff
  % 11
\bar "|"
 \cadenzaOn
  \clef "treble" gs'''\harmonic_\markup{"-49"}^\markup{ \raise #3 {"x11"} }
  \clef "treble" gs'''\harmonic
  \clef "treble" gs'''\harmonic
  \cadenzaOff
  % 12
\bar "|"
 \cadenzaOn
  \clef "treble" a'''\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x12"} }
  \cadenzaOff
  % 13
\bar "|"
 \cadenzaOn
  \clef "treble" bf'''\harmonic_\markup{"+41"}^\markup{ \raise #3 {"x13"} }
  \clef "treble" bf'''\harmonic
  \clef "treble" bf'''\harmonic
  \cadenzaOff
  % 14
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #2 c''''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x14"} }
  \cadenzaOff
  % 15
\bar "|"
 \cadenzaOn
  \clef "treble" cs''''\harmonic_\markup{"-12"}^\markup{ \raise #3 {"x15"} }
  \clef "treble" cs''''\harmonic
  \cadenzaOff
  % 16
\bar "|"
 \cadenzaOn
  \clef "treble" d''''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x16"} }
  \clef "treble" d''''\harmonic
  \cadenzaOff
  \bar "|."
}

locationsDb =
{
  \global
 \cadenzaOn
  \clef "tenor" \ottava #0 d'_\markup{"+0"}
 \cadenzaOn
  \clef "treble" a'_\markup{"+2"}
 \cadenzaOn
  \clef "tenor" fs'_\markup{"-14"}
 \cadenzaOn
  \clef "tenor" f'_\markup{"-33"}
  \clef "treble" c''_\markup{"-31"}
 \cadenzaOn
  \clef "tenor" g'_\markup{"-2"}
 \cadenzaOn
  \clef "tenor" e'_\markup{"+4"}
 \cadenzaOn
  \clef "treble" b'_\markup{"-16"}
 \cadenzaOn
  \clef "tenor" e'_\markup{"-35"}
  \clef "tenor" gs'_\markup{"-49"}
  \clef "treble" c''_\markup{"+49"}
 \cadenzaOn
  \clef "tenor" f'_\markup{"+16"}
 \cadenzaOn
  \clef "tenor" ef'_\markup{"+39"}
  \clef "tenor" g'_\markup{"-46"}
  \clef "treble" bf'_\markup{"+41"}
 \cadenzaOn
  \clef "tenor" gs'_\markup{"-17"}
 \cadenzaOn
  \clef "tenor" ef'_\markup{"+19"}
  \clef "treble" cs''_\markup{"-12"}
 \cadenzaOn
  \clef "tenor" e'_\markup{"+31"}
  \clef "treble" bf'_\markup{"+14"}
  \bar "|."
}

\score
{
  \header
  {
    tagline = ##f
    piece = \markup \column { "Cello D-string, 2nd octave" \vspace #1 }
  }
  \new StaffGroup
  <<
    \new Staff = "pitch" \with { instrumentName = "pitch" }
    <<
      \new Voice = "pitch" { \pitchesDb }
    >>
    \new Staff = "location" \with { instrumentName = "location" }
    << \locationsDb >>
  >>
}

\layout
{
  \context {
    \StaffGroup
    \consists #Span_stem_engraver
  }
  \context {
    \Score
    \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/200)
  }
}
  
\paper
{
  system-system-spacing = #'((basic-distance . 1) (padding . 5))
  top-margin = 25
  left-margin = 25
  right-margin = 25
  ragged-bottom = ##t
  print-page-number = ##f
}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\version "2.20.0"
\include "english.ly"
  \header
  {
    copyright = \markup{
      \center-column {
        "All rights to this work are granted under Creative Commons License CC0."
        "See https://creativecommons.org/publicdomain/zero/1.0/"
    }
  }
    tagline = ##f
    print-all-headers = ##t
  }
#(set-default-paper-size "letter")
global = 
{
  \omit Score.TimeSignature
}

pitchesDc =
{
  \global
  % 4
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #0 d''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x4"} }
  \cadenzaOff
  % 5
\bar "|"
 \cadenzaOn
  \clef "treble" fs''\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x5"} }
  \cadenzaOff
  % 6
\bar "|"
 \cadenzaOn
  \clef "treble" a''\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x6"} }
  \cadenzaOff
  % 7
\bar "|"
 \cadenzaOn
  \clef "treble" c'''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x7"} }
  \cadenzaOff
  % 9
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #1 e'''\harmonic_\markup{"+4"}^\markup{ \raise #3 {"x9"} }
  \cadenzaOff
  % 11
\bar "|"
 \cadenzaOn
  \clef "treble" gs'''\harmonic_\markup{"-49"}^\markup{ \raise #3 {"x11"} }
  \cadenzaOff
  % 13
\bar "|"
 \cadenzaOn
  \clef "treble" bf'''\harmonic_\markup{"+41"}^\markup{ \raise #3 {"x13"} }
  \clef "treble" bf'''\harmonic
  \cadenzaOff
  % 14
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #2 c''''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x14"} }
  \cadenzaOff
  % 15
\bar "|"
 \cadenzaOn
  \clef "treble" cs''''\harmonic_\markup{"-12"}^\markup{ \raise #3 {"x15"} }
  \cadenzaOff
  % 16
\bar "|"
 \cadenzaOn
  \clef "treble" d''''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x16"} }
  \cadenzaOff
  \bar "|."
}

locationsDc =
{
  \global
 \cadenzaOn
  \clef "treble" \ottava #0 d''_\markup{"+0"}
 \cadenzaOn
  \clef "treble" fs''_\markup{"-14"}
 \cadenzaOn
  \clef "treble" a''_\markup{"+2"}
 \cadenzaOn
  \clef "treble" c'''_\markup{"-31"}
 \cadenzaOn
  \clef "treble" e''_\markup{"+4"}
 \cadenzaOn
  \clef "treble" gs''_\markup{"-49"}
 \cadenzaOn
  \clef "treble" ef''_\markup{"+39"}
  \clef "treble" bf''_\markup{"+41"}
 \cadenzaOn
  \clef "treble" f''_\markup{"-33"}
 \cadenzaOn
  \clef "treble" cs'''_\markup{"-12"}
 \cadenzaOn
  \clef "treble" g''_\markup{"-2"}
  \bar "|."
}

\score
{
  \header
  {
    tagline = ##f
    piece = \markup \column { "Cello D-string, 3rd octave" \vspace #1 }
  }
  \new StaffGroup
  <<
    \new Staff = "pitch" \with { instrumentName = "pitch" }
    <<
      \new Voice = "pitch" { \pitchesDc }
    >>
    \new Staff = "location" \with { instrumentName = "location" }
    << \locationsDc >>
  >>
}

\layout
{
  \context {
    \StaffGroup
    \consists #Span_stem_engraver
  }
  \context {
    \Score
    \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/200)
  }
}
  
\paper
{
  system-system-spacing = #'((basic-distance . 1) (padding . 5))
  top-margin = 25
  left-margin = 25
  right-margin = 25
  ragged-bottom = ##t
  print-page-number = ##f
}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\pageBreak

\version "2.20.0"
\include "english.ly"
  \header
  {
    copyright = \markup{
      \center-column {
        "All rights to this work are granted under Creative Commons License CC0."
        "See https://creativecommons.org/publicdomain/zero/1.0/"
    }
  }
    tagline = ##f
    print-all-headers = ##t
  }
#(set-default-paper-size "letter")
global = 
{
  \omit Score.TimeSignature
}

pitchesGa =
{
  \global
  % 3
\bar "|"
 \cadenzaOn
  \clef "tenor" \ottava #0 d'\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x3"} }
  \cadenzaOff
  % 4
\bar "|"
 \cadenzaOn
  \clef "tenor" g'\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x4"} }
  \cadenzaOff
  % 5
\bar "|"
 \cadenzaOn
  \clef "treble" b'\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x5"} }
  \clef "treble" b'\harmonic
  \cadenzaOff
  % 6
\bar "|"
 \cadenzaOn
  \clef "treble" d''\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x6"} }
  \cadenzaOff
  % 7
\bar "|"
 \cadenzaOn
  \clef "treble" f''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x7"} }
  \clef "treble" f''\harmonic
  \clef "treble" f''\harmonic
  \cadenzaOff
  % 8
\bar "|"
 \cadenzaOn
  \clef "treble" g''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x8"} }
  \clef "treble" g''\harmonic
  \cadenzaOff
  % 9
\bar "|"
 \cadenzaOn
  \clef "treble" a''\harmonic_\markup{"+4"}^\markup{ \raise #3 {"x9"} }
  \clef "treble" a''\harmonic
  \clef "treble" a''\harmonic
  \cadenzaOff
  % 10
\bar "|"
 \cadenzaOn
  \clef "treble" b''\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x10"} }
  \clef "treble" b''\harmonic
  \cadenzaOff
  % 11
\bar "|"
 \cadenzaOn
  \clef "treble" cs'''\harmonic_\markup{"-49"}^\markup{ \raise #3 {"x11"} }
  \clef "treble" cs'''\harmonic
  \clef "treble" cs'''\harmonic
  \clef "treble" cs'''\harmonic
  \clef "treble" cs'''\harmonic
  \cadenzaOff
  % 12
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #1 d'''\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x12"} }
  \clef "treble" d'''\harmonic
  \cadenzaOff
  % 13
\bar "|"
 \cadenzaOn
  \clef "treble" ef'''\harmonic_\markup{"+41"}^\markup{ \raise #3 {"x13"} }
  \clef "treble" ef'''\harmonic
  \clef "treble" ef'''\harmonic
  \clef "treble" ef'''\harmonic
  \clef "treble" ef'''\harmonic
  \clef "treble" ef'''\harmonic
  \cadenzaOff
  % 14
\bar "|"
 \cadenzaOn
  \clef "treble" f'''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x14"} }
  \clef "treble" f'''\harmonic
  \clef "treble" f'''\harmonic
  \cadenzaOff
  % 15
\bar "|"
 \cadenzaOn
  \clef "treble" fs'''\harmonic_\markup{"-12"}^\markup{ \raise #3 {"x15"} }
  \clef "treble" fs'''\harmonic
  \clef "treble" fs'''\harmonic
  \clef "treble" fs'''\harmonic
  \cadenzaOff
  % 16
\bar "|"
 \cadenzaOn
  \clef "treble" g'''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x16"} }
  \clef "treble" g'''\harmonic
  \clef "treble" g'''\harmonic
  \clef "treble" g'''\harmonic
  \cadenzaOff
  \bar "|."
}

locationsGa =
{
  \global
 \cadenzaOn
  \clef "bass" \ottava #0 d_\markup{"+2"}
 \cadenzaOn
  \clef "bass" c_\markup{"-2"}
 \cadenzaOn
  \clef "bass" b,_\markup{"-14"}
  \clef "bass" e_\markup{"-16"}
 \cadenzaOn
  \clef "bass" bf,_\markup{"+16"}
 \cadenzaOn
  \clef "bass" bf,_\markup{"-33"}
  \clef "bass" cs_\markup{"-17"}
  \clef "bass" f_\markup{"-31"}
 \cadenzaOn
  \clef "bass" a,_\markup{"+31"}
  \clef "bass" ef_\markup{"+14"}
 \cadenzaOn
  \clef "bass" a,_\markup{"+4"}
  \clef "bass" b,_\markup{"+35"}
  \clef "bass" f_\markup{"+18"}
 \cadenzaOn
  \clef "bass" a,_\markup{"-18"}
  \clef "bass" cs_\markup{"+17"}
 \cadenzaOn
  \clef "bass" a,_\markup{"-35"}
  \clef "bass" bf,_\markup{"+47"}
  \clef "bass" cs_\markup{"-49"}
  \clef "bass" ef_\markup{"-18"}
  \clef "bass" f_\markup{"+49"}
 \cadenzaOn
  \clef "bass" a,_\markup{"-49"}
  \clef "bass" e_\markup{"+33"}
 \cadenzaOn
  \clef "bass" gs,_\markup{"+39"}
  \clef "bass" bf,_\markup{"-11"}
  \clef "bass" c_\markup{"-46"}
  \clef "bass" cs_\markup{"+37"}
  \clef "bass" ef_\markup{"+41"}
  \clef "bass" fs_\markup{"-28"}
 \cadenzaOn
  \clef "bass" gs,_\markup{"+28"}
  \clef "bass" b,_\markup{"+18"}
  \clef "bass" ef_\markup{"-35"}
 \cadenzaOn
  \clef "bass" gs,_\markup{"+19"}
  \clef "bass" a,_\markup{"+48"}
  \clef "bass" c_\markup{"+37"}
  \clef "bass" fs_\markup{"-12"}
 \cadenzaOn
  \clef "bass" gs,_\markup{"+12"}
  \clef "bass" b,_\markup{"-41"}
  \clef "bass" cs_\markup{"+49"}
  \clef "bass" f_\markup{"-4"}
  \bar "|."
}

\score
{
  \header
  {
    tagline = ##f
    piece = \markup \column { "Cello G-string, 1st octave" \vspace #1 }
  }
  \new StaffGroup
  <<
    \new Staff = "pitch" \with { instrumentName = "pitch" }
    <<
      \new Voice = "pitch" { \pitchesGa }
    >>
    \new Staff = "location" \with { instrumentName = "location" }
    << \locationsGa >>
  >>
}

\layout
{
  \context {
    \StaffGroup
    \consists #Span_stem_engraver
  }
  \context {
    \Score
    \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/200)
  }
}
  
\paper
{
  system-system-spacing = #'((basic-distance . 1) (padding . 5))
  top-margin = 25
  left-margin = 25
  right-margin = 25
  ragged-bottom = ##t
  print-page-number = ##f
}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\pageBreak

\version "2.20.0"
\include "english.ly"
  \header
  {
    copyright = \markup{
      \center-column {
        "All rights to this work are granted under Creative Commons License CC0."
        "See https://creativecommons.org/publicdomain/zero/1.0/"
    }
  }
    tagline = ##f
    print-all-headers = ##t
  }
#(set-default-paper-size "letter")
global = 
{
  \omit Score.TimeSignature
}

pitchesGb =
{
  \global
  % 2
\bar "|"
 \cadenzaOn
  \clef "bass" \ottava #0 g\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x2"} }
  \cadenzaOff
  % 3
\bar "|"
 \cadenzaOn
  \clef "tenor" d'\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x3"} }
  \cadenzaOff
  % 5
\bar "|"
 \cadenzaOn
  \clef "treble" b'\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x5"} }
  \cadenzaOff
  % 7
\bar "|"
 \cadenzaOn
  \clef "treble" f''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x7"} }
  \clef "treble" f''\harmonic
  \cadenzaOff
  % 8
\bar "|"
 \cadenzaOn
  \clef "treble" g''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x8"} }
  \cadenzaOff
  % 9
\bar "|"
 \cadenzaOn
  \clef "treble" a''\harmonic_\markup{"+4"}^\markup{ \raise #3 {"x9"} }
  \cadenzaOff
  % 10
\bar "|"
 \cadenzaOn
  \clef "treble" b''\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x10"} }
  \cadenzaOff
  % 11
\bar "|"
 \cadenzaOn
  \clef "treble" cs'''\harmonic_\markup{"-49"}^\markup{ \raise #3 {"x11"} }
  \clef "treble" cs'''\harmonic
  \clef "treble" cs'''\harmonic
  \cadenzaOff
  % 12
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #1 d'''\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x12"} }
  \cadenzaOff
  % 13
\bar "|"
 \cadenzaOn
  \clef "treble" ef'''\harmonic_\markup{"+41"}^\markup{ \raise #3 {"x13"} }
  \clef "treble" ef'''\harmonic
  \clef "treble" ef'''\harmonic
  \cadenzaOff
  % 14
\bar "|"
 \cadenzaOn
  \clef "treble" f'''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x14"} }
  \cadenzaOff
  % 15
\bar "|"
 \cadenzaOn
  \clef "treble" fs'''\harmonic_\markup{"-12"}^\markup{ \raise #3 {"x15"} }
  \clef "treble" fs'''\harmonic
  \cadenzaOff
  % 16
\bar "|"
 \cadenzaOn
  \clef "treble" g'''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x16"} }
  \clef "treble" g'''\harmonic
  \cadenzaOff
  \bar "|."
}

locationsGb =
{
  \global
 \cadenzaOn
  \clef "bass" \ottava #0 g_\markup{"+0"}
 \cadenzaOn
  \clef "tenor" d'_\markup{"+2"}
 \cadenzaOn
  \clef "bass" b_\markup{"-14"}
 \cadenzaOn
  \clef "bass" bf_\markup{"-33"}
  \clef "tenor" f'_\markup{"-31"}
 \cadenzaOn
  \clef "bass" c'_\markup{"-2"}
 \cadenzaOn
  \clef "bass" a_\markup{"+4"}
 \cadenzaOn
  \clef "tenor" e'_\markup{"-16"}
 \cadenzaOn
  \clef "bass" a_\markup{"-35"}
  \clef "bass" cs'_\markup{"-49"}
  \clef "tenor" f'_\markup{"+49"}
 \cadenzaOn
  \clef "bass" bf_\markup{"+16"}
 \cadenzaOn
  \clef "bass" gs_\markup{"+39"}
  \clef "bass" c'_\markup{"-46"}
  \clef "tenor" ef'_\markup{"+41"}
 \cadenzaOn
  \clef "bass" cs'_\markup{"-17"}
 \cadenzaOn
  \clef "bass" gs_\markup{"+19"}
  \clef "tenor" fs'_\markup{"-12"}
 \cadenzaOn
  \clef "bass" a_\markup{"+31"}
  \clef "tenor" ef'_\markup{"+14"}
  \bar "|."
}

\score
{
  \header
  {
    tagline = ##f
    piece = \markup \column { "Cello G-string, 2nd octave" \vspace #1 }
  }
  \new StaffGroup
  <<
    \new Staff = "pitch" \with { instrumentName = "pitch" }
    <<
      \new Voice = "pitch" { \pitchesGb }
    >>
    \new Staff = "location" \with { instrumentName = "location" }
    << \locationsGb >>
  >>
}

\layout
{
  \context {
    \StaffGroup
    \consists #Span_stem_engraver
  }
  \context {
    \Score
    \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/200)
  }
}
  
\paper
{
  system-system-spacing = #'((basic-distance . 1) (padding . 5))
  top-margin = 25
  left-margin = 25
  right-margin = 25
  ragged-bottom = ##t
  print-page-number = ##f
}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\version "2.20.0"
\include "english.ly"
  \header
  {
    copyright = \markup{
      \center-column {
        "All rights to this work are granted under Creative Commons License CC0."
        "See https://creativecommons.org/publicdomain/zero/1.0/"
    }
  }
    tagline = ##f
    print-all-headers = ##t
  }
#(set-default-paper-size "letter")
global = 
{
  \omit Score.TimeSignature
}

pitchesGc =
{
  \global
  % 4
\bar "|"
 \cadenzaOn
  \clef "tenor" \ottava #0 g'\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x4"} }
  \cadenzaOff
  % 5
\bar "|"
 \cadenzaOn
  \clef "treble" b'\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x5"} }
  \cadenzaOff
  % 6
\bar "|"
 \cadenzaOn
  \clef "treble" d''\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x6"} }
  \cadenzaOff
  % 7
\bar "|"
 \cadenzaOn
  \clef "treble" f''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x7"} }
  \cadenzaOff
  % 9
\bar "|"
 \cadenzaOn
  \clef "treble" a''\harmonic_\markup{"+4"}^\markup{ \raise #3 {"x9"} }
  \cadenzaOff
  % 11
\bar "|"
 \cadenzaOn
  \clef "treble" cs'''\harmonic_\markup{"-49"}^\markup{ \raise #3 {"x11"} }
  \cadenzaOff
  % 13
\bar "|"
 \cadenzaOn
  \clef "treble" \ottava #1 ef'''\harmonic_\markup{"+41"}^\markup{ \raise #3 {"x13"} }
  \clef "treble" ef'''\harmonic
  \cadenzaOff
  % 14
\bar "|"
 \cadenzaOn
  \clef "treble" f'''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x14"} }
  \cadenzaOff
  % 15
\bar "|"
 \cadenzaOn
  \clef "treble" fs'''\harmonic_\markup{"-12"}^\markup{ \raise #3 {"x15"} }
  \cadenzaOff
  % 16
\bar "|"
 \cadenzaOn
  \clef "treble" g'''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x16"} }
  \cadenzaOff
  \bar "|."
}

locationsGc =
{
  \global
 \cadenzaOn
  \clef "tenor" \ottava #0 g'_\markup{"+0"}
 \cadenzaOn
  \clef "treble" b'_\markup{"-14"}
 \cadenzaOn
  \clef "treble" d''_\markup{"+2"}
 \cadenzaOn
  \clef "treble" f''_\markup{"-31"}
 \cadenzaOn
  \clef "treble" a'_\markup{"+4"}
 \cadenzaOn
  \clef "treble" cs''_\markup{"-49"}
 \cadenzaOn
  \clef "tenor" gs'_\markup{"+39"}
  \clef "treble" ef''_\markup{"+41"}
 \cadenzaOn
  \clef "treble" bf'_\markup{"-33"}
 \cadenzaOn
  \clef "treble" fs''_\markup{"-12"}
 \cadenzaOn
  \clef "treble" c''_\markup{"-2"}
  \bar "|."
}

\score
{
  \header
  {
    tagline = ##f
    piece = \markup \column { "Cello G-string, 3rd octave" \vspace #1 }
  }
  \new StaffGroup
  <<
    \new Staff = "pitch" \with { instrumentName = "pitch" }
    <<
      \new Voice = "pitch" { \pitchesGc }
    >>
    \new Staff = "location" \with { instrumentName = "location" }
    << \locationsGc >>
  >>
}

\layout
{
  \context {
    \StaffGroup
    \consists #Span_stem_engraver
  }
  \context {
    \Score
    \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/200)
  }
}
  
\paper
{
  system-system-spacing = #'((basic-distance . 1) (padding . 5))
  top-margin = 25
  left-margin = 25
  right-margin = 25
  ragged-bottom = ##t
  print-page-number = ##f
}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\pageBreak

\version "2.20.0"
\include "english.ly"
  \header
  {
    copyright = \markup{
      \center-column {
        "All rights to this work are granted under Creative Commons License CC0."
        "See https://creativecommons.org/publicdomain/zero/1.0/"
    }
  }
    tagline = ##f
    print-all-headers = ##t
  }
#(set-default-paper-size "letter")
global = 
{
  \omit Score.TimeSignature
}

pitchesCa =
{
  \global
  % 3
\bar "|"
 \cadenzaOn
  \clef "bass" \ottava #0 g\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x3"} }
  \cadenzaOff
  % 4
\bar "|"
 \cadenzaOn
  \clef "bass" c'\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x4"} }
  \cadenzaOff
  % 5
\bar "|"
 \cadenzaOn
  \clef "tenor" e'\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x5"} }
  \clef "tenor" e'\harmonic
  \cadenzaOff
  % 6
\bar "|"
 \cadenzaOn
  \clef "tenor" g'\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x6"} }
  \cadenzaOff
  % 7
\bar "|"
 \cadenzaOn
  \clef "treble" bf'\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x7"} }
  \clef "treble" bf'\harmonic
  \clef "treble" bf'\harmonic
  \cadenzaOff
  % 8
\bar "|"
 \cadenzaOn
  \clef "treble" c''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x8"} }
  \clef "treble" c''\harmonic
  \cadenzaOff
  % 9
\bar "|"
 \cadenzaOn
  \clef "treble" d''\harmonic_\markup{"+4"}^\markup{ \raise #3 {"x9"} }
  \clef "treble" d''\harmonic
  \clef "treble" d''\harmonic
  \cadenzaOff
  % 10
\bar "|"
 \cadenzaOn
  \clef "treble" e''\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x10"} }
  \clef "treble" e''\harmonic
  \cadenzaOff
  % 11
\bar "|"
 \cadenzaOn
  \clef "treble" fs''\harmonic_\markup{"-49"}^\markup{ \raise #3 {"x11"} }
  \clef "treble" fs''\harmonic
  \clef "treble" fs''\harmonic
  \clef "treble" fs''\harmonic
  \clef "treble" fs''\harmonic
  \cadenzaOff
  % 12
\bar "|"
 \cadenzaOn
  \clef "treble" g''\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x12"} }
  \clef "treble" g''\harmonic
  \cadenzaOff
  % 13
\bar "|"
 \cadenzaOn
  \clef "treble" gs''\harmonic_\markup{"+41"}^\markup{ \raise #3 {"x13"} }
  \clef "treble" gs''\harmonic
  \clef "treble" gs''\harmonic
  \clef "treble" gs''\harmonic
  \clef "treble" gs''\harmonic
  \clef "treble" gs''\harmonic
  \cadenzaOff
  % 14
\bar "|"
 \cadenzaOn
  \clef "treble" bf''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x14"} }
  \clef "treble" bf''\harmonic
  \clef "treble" bf''\harmonic
  \cadenzaOff
  % 15
\bar "|"
 \cadenzaOn
  \clef "treble" b''\harmonic_\markup{"-12"}^\markup{ \raise #3 {"x15"} }
  \clef "treble" b''\harmonic
  \clef "treble" b''\harmonic
  \clef "treble" b''\harmonic
  \cadenzaOff
  % 16
\bar "|"
 \cadenzaOn
  \clef "treble" c'''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x16"} }
  \clef "treble" c'''\harmonic
  \clef "treble" c'''\harmonic
  \clef "treble" c'''\harmonic
  \cadenzaOff
  \bar "|."
}

locationsCa =
{
  \global
 \cadenzaOn
  \clef "bass" \ottava #0 g,_\markup{"+2"}
 \cadenzaOn
  \clef "bass" f,_\markup{"-2"}
 \cadenzaOn
  \clef "bass" e,_\markup{"-14"}
  \clef "bass" a,_\markup{"-16"}
 \cadenzaOn
  \clef "bass" ef,_\markup{"+16"}
 \cadenzaOn
  \clef "bass" ef,_\markup{"-33"}
  \clef "bass" fs,_\markup{"-17"}
  \clef "bass" bf,_\markup{"-31"}
 \cadenzaOn
  \clef "bass" d,_\markup{"+31"}
  \clef "bass" gs,_\markup{"+14"}
 \cadenzaOn
  \clef "bass" d,_\markup{"+4"}
  \clef "bass" e,_\markup{"+35"}
  \clef "bass" bf,_\markup{"+18"}
 \cadenzaOn
  \clef "bass" d,_\markup{"-18"}
  \clef "bass" fs,_\markup{"+17"}
 \cadenzaOn
  \clef "bass" d,_\markup{"-35"}
  \clef "bass" ef,_\markup{"+47"}
  \clef "bass" fs,_\markup{"-49"}
  \clef "bass" gs,_\markup{"-18"}
  \clef "bass" bf,_\markup{"+49"}
 \cadenzaOn
  \clef "bass" d,_\markup{"-49"}
  \clef "bass" a,_\markup{"+33"}
 \cadenzaOn
  \clef "bass" cs,_\markup{"+39"}
  \clef "bass" ef,_\markup{"-11"}
  \clef "bass" f,_\markup{"-46"}
  \clef "bass" fs,_\markup{"+37"}
  \clef "bass" gs,_\markup{"+41"}
  \clef "bass" b,_\markup{"-28"}
 \cadenzaOn
  \clef "bass" cs,_\markup{"+28"}
  \clef "bass" e,_\markup{"+18"}
  \clef "bass" gs,_\markup{"-35"}
 \cadenzaOn
  \clef "bass" cs,_\markup{"+19"}
  \clef "bass" d,_\markup{"+48"}
  \clef "bass" f,_\markup{"+37"}
  \clef "bass" b,_\markup{"-12"}
 \cadenzaOn
  \clef "bass" cs,_\markup{"+12"}
  \clef "bass" e,_\markup{"-41"}
  \clef "bass" fs,_\markup{"+49"}
  \clef "bass" bf,_\markup{"-4"}
  \bar "|."
}

\score
{
  \header
  {
    tagline = ##f
    piece = \markup \column { "Cello C-string, 1st octave" \vspace #1 }
  }
  \new StaffGroup
  <<
    \new Staff = "pitch" \with { instrumentName = "pitch" }
    <<
      \new Voice = "pitch" { \pitchesCa }
    >>
    \new Staff = "location" \with { instrumentName = "location" }
    << \locationsCa >>
  >>
}

\layout
{
  \context {
    \StaffGroup
    \consists #Span_stem_engraver
  }
  \context {
    \Score
    \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/200)
  }
}
  
\paper
{
  system-system-spacing = #'((basic-distance . 1) (padding . 5))
  top-margin = 25
  left-margin = 25
  right-margin = 25
  ragged-bottom = ##t
  print-page-number = ##f
}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\pageBreak

\version "2.20.0"
\include "english.ly"
  \header
  {
    copyright = \markup{
      \center-column {
        "All rights to this work are granted under Creative Commons License CC0."
        "See https://creativecommons.org/publicdomain/zero/1.0/"
    }
  }
    tagline = ##f
    print-all-headers = ##t
  }
#(set-default-paper-size "letter")
global = 
{
  \omit Score.TimeSignature
}

pitchesCb =
{
  \global
  % 2
\bar "|"
 \cadenzaOn
  \clef "bass" \ottava #0 c\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x2"} }
  \cadenzaOff
  % 3
\bar "|"
 \cadenzaOn
  \clef "bass" g\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x3"} }
  \cadenzaOff
  % 5
\bar "|"
 \cadenzaOn
  \clef "tenor" e'\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x5"} }
  \cadenzaOff
  % 7
\bar "|"
 \cadenzaOn
  \clef "treble" bf'\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x7"} }
  \clef "treble" bf'\harmonic
  \cadenzaOff
  % 8
\bar "|"
 \cadenzaOn
  \clef "treble" c''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x8"} }
  \cadenzaOff
  % 9
\bar "|"
 \cadenzaOn
  \clef "treble" d''\harmonic_\markup{"+4"}^\markup{ \raise #3 {"x9"} }
  \cadenzaOff
  % 10
\bar "|"
 \cadenzaOn
  \clef "treble" e''\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x10"} }
  \cadenzaOff
  % 11
\bar "|"
 \cadenzaOn
  \clef "treble" fs''\harmonic_\markup{"-49"}^\markup{ \raise #3 {"x11"} }
  \clef "treble" fs''\harmonic
  \clef "treble" fs''\harmonic
  \cadenzaOff
  % 12
\bar "|"
 \cadenzaOn
  \clef "treble" g''\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x12"} }
  \cadenzaOff
  % 13
\bar "|"
 \cadenzaOn
  \clef "treble" gs''\harmonic_\markup{"+41"}^\markup{ \raise #3 {"x13"} }
  \clef "treble" gs''\harmonic
  \clef "treble" gs''\harmonic
  \cadenzaOff
  % 14
\bar "|"
 \cadenzaOn
  \clef "treble" bf''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x14"} }
  \cadenzaOff
  % 15
\bar "|"
 \cadenzaOn
  \clef "treble" b''\harmonic_\markup{"-12"}^\markup{ \raise #3 {"x15"} }
  \clef "treble" b''\harmonic
  \cadenzaOff
  % 16
\bar "|"
 \cadenzaOn
  \clef "treble" c'''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x16"} }
  \clef "treble" c'''\harmonic
  \cadenzaOff
  \bar "|."
}

locationsCb =
{
  \global
 \cadenzaOn
  \clef "bass" \ottava #0 c_\markup{"+0"}
 \cadenzaOn
  \clef "bass" g_\markup{"+2"}
 \cadenzaOn
  \clef "bass" e_\markup{"-14"}
 \cadenzaOn
  \clef "bass" ef_\markup{"-33"}
  \clef "bass" bf_\markup{"-31"}
 \cadenzaOn
  \clef "bass" f_\markup{"-2"}
 \cadenzaOn
  \clef "bass" d_\markup{"+4"}
 \cadenzaOn
  \clef "bass" a_\markup{"-16"}
 \cadenzaOn
  \clef "bass" d_\markup{"-35"}
  \clef "bass" fs_\markup{"-49"}
  \clef "bass" bf_\markup{"+49"}
 \cadenzaOn
  \clef "bass" ef_\markup{"+16"}
 \cadenzaOn
  \clef "bass" cs_\markup{"+39"}
  \clef "bass" f_\markup{"-46"}
  \clef "bass" gs_\markup{"+41"}
 \cadenzaOn
  \clef "bass" fs_\markup{"-17"}
 \cadenzaOn
  \clef "bass" cs_\markup{"+19"}
  \clef "bass" b_\markup{"-12"}
 \cadenzaOn
  \clef "bass" d_\markup{"+31"}
  \clef "bass" gs_\markup{"+14"}
  \bar "|."
}

\score
{
  \header
  {
    tagline = ##f
    piece = \markup \column { "Cello C-string, 2nd octave" \vspace #1 }
  }
  \new StaffGroup
  <<
    \new Staff = "pitch" \with { instrumentName = "pitch" }
    <<
      \new Voice = "pitch" { \pitchesCb }
    >>
    \new Staff = "location" \with { instrumentName = "location" }
    << \locationsCb >>
  >>
}

\layout
{
  \context {
    \StaffGroup
    \consists #Span_stem_engraver
  }
  \context {
    \Score
    \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/200)
  }
}
  
\paper
{
  system-system-spacing = #'((basic-distance . 1) (padding . 5))
  top-margin = 25
  left-margin = 25
  right-margin = 25
  ragged-bottom = ##t
  print-page-number = ##f
}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\version "2.20.0"
\include "english.ly"
  \header
  {
    copyright = \markup{
      \center-column {
        "All rights to this work are granted under Creative Commons License CC0."
        "See https://creativecommons.org/publicdomain/zero/1.0/"
    }
  }
    tagline = ##f
    print-all-headers = ##t
  }
#(set-default-paper-size "letter")
global = 
{
  \omit Score.TimeSignature
}

pitchesCc =
{
  \global
  % 4
\bar "|"
 \cadenzaOn
  \clef "bass" \ottava #0 c'\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x4"} }
  \cadenzaOff
  % 5
\bar "|"
 \cadenzaOn
  \clef "tenor" e'\harmonic_\markup{"-14"}^\markup{ \raise #3 {"x5"} }
  \cadenzaOff
  % 6
\bar "|"
 \cadenzaOn
  \clef "tenor" g'\harmonic_\markup{"+2"}^\markup{ \raise #3 {"x6"} }
  \cadenzaOff
  % 7
\bar "|"
 \cadenzaOn
  \clef "treble" bf'\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x7"} }
  \cadenzaOff
  % 9
\bar "|"
 \cadenzaOn
  \clef "treble" d''\harmonic_\markup{"+4"}^\markup{ \raise #3 {"x9"} }
  \cadenzaOff
  % 11
\bar "|"
 \cadenzaOn
  \clef "treble" fs''\harmonic_\markup{"-49"}^\markup{ \raise #3 {"x11"} }
  \cadenzaOff
  % 13
\bar "|"
 \cadenzaOn
  \clef "treble" gs''\harmonic_\markup{"+41"}^\markup{ \raise #3 {"x13"} }
  \clef "treble" gs''\harmonic
  \cadenzaOff
  % 14
\bar "|"
 \cadenzaOn
  \clef "treble" bf''\harmonic_\markup{"-31"}^\markup{ \raise #3 {"x14"} }
  \cadenzaOff
  % 15
\bar "|"
 \cadenzaOn
  \clef "treble" b''\harmonic_\markup{"-12"}^\markup{ \raise #3 {"x15"} }
  \cadenzaOff
  % 16
\bar "|"
 \cadenzaOn
  \clef "treble" c'''\harmonic_\markup{"+0"}^\markup{ \raise #3 {"x16"} }
  \cadenzaOff
  \bar "|."
}

locationsCc =
{
  \global
 \cadenzaOn
  \clef "bass" \ottava #0 c'_\markup{"+0"}
 \cadenzaOn
  \clef "tenor" e'_\markup{"-14"}
 \cadenzaOn
  \clef "tenor" g'_\markup{"+2"}
 \cadenzaOn
  \clef "treble" bf'_\markup{"-31"}
 \cadenzaOn
  \clef "tenor" d'_\markup{"+4"}
 \cadenzaOn
  \clef "tenor" fs'_\markup{"-49"}
 \cadenzaOn
  \clef "bass" cs'_\markup{"+39"}
  \clef "tenor" gs'_\markup{"+41"}
 \cadenzaOn
  \clef "tenor" ef'_\markup{"-33"}
 \cadenzaOn
  \clef "treble" b'_\markup{"-12"}
 \cadenzaOn
  \clef "tenor" f'_\markup{"-2"}
  \bar "|."
}

\score
{
  \header
  {
    tagline = ##f
    piece = \markup \column { "Cello C-string, 3rd octave" \vspace #1 }
  }
  \new StaffGroup
  <<
    \new Staff = "pitch" \with { instrumentName = "pitch" }
    <<
      \new Voice = "pitch" { \pitchesCc }
    >>
    \new Staff = "location" \with { instrumentName = "location" }
    << \locationsCc >>
  >>
}

\layout
{
  \context {
    \StaffGroup
    \consists #Span_stem_engraver
  }
  \context {
    \Score
    \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/200)
  }
}
  
\paper
{
  system-system-spacing = #'((basic-distance . 1) (padding . 5))
  top-margin = 25
  left-margin = 25
  right-margin = 25
  ragged-bottom = ##t
  print-page-number = ##f
}

