# provenance.md, Xuanji sonification docs site

This file is the demonstration disclosure for the Xuanji documentation site. It
exists so that no reader, and no admissions officer, is ever misled about what
on this artifact is real today and what is a modelled future state. Read it
before you read the site.

## 1. What this artifact is

This is an **illustrative sample build**, produced as part of a CRCS story and
planning package for the student **Aiden Yeoh**. It shows what a documentation
site for Xuanji, an open-source Python library that renders historical
astronomical records as sound, could look like at two points in its life. It is
a design and planning deliverable, not a claim that the library is already
published at the scale the goal version depicts.

The site ships in two versions on one design system:

- `launch/` is the **honest current state**: a pre-1.0 library (v0.3.1)
  maintained by one student, with ten curated events, a reserved Zenodo DOI, and
  a JOSS paper only "in preparation." Every claim on the launch pages is one a
  student could stand behind on the day of a first public release. The advisor
  seat is not shown as filled because it is not filled.
- `goal/` is the **aspirational target**: the same library at v1.4.2, with a
  contributor team, forty-two curated events, a peer-reviewed JOSS paper, a
  named citation, and adoption figures. This is a goal rendered as a finished
  site so the student can see the destination. It is not a description of the
  present. Nothing on the goal pages should be read as already true.

The two versions share one masthead, type system, palette, grid, logo, and
footer; only the content and the scale change, plus the version pill.

## 2. Demonstration-only contributors (goal version)

The `goal/` site names a contributor team and a JOSS co-authorship. Aiden Yeoh
is a real person and the public author of this project. **Every other named
contributor on the goal site is a fictional placeholder invented for this
demonstration.** They stand in for the real volunteers a mature open-source
project would accumulate; they are not real people, and none of them has
endorsed, advised, or contributed to anything.

Fictional demonstration contributors named on `goal/index.html`:

- Maya Okonkwo (shown as co-maintainer, SkyPath stereo model, accessibility)
- Dev Ramanathan (shown as test suite, CI, conda-forge feedstock)
- Sofia Halvorsen (shown as plate plotter, figure conventions, gallery)
- Lucas Meng (shown as light-curve reconstruction, date_sigma model)
- Priya Balasubramanian (shown as documentation, tutorial, schema validator)
- "+ 23 contributors" (an aggregate placeholder, not real individuals)

The JOSS citation on the goal site,

> Yeoh, A., Okonkwo, M., Ramanathan, D., Halvorsen, S., Meng, L., &
> Balasubramanian, B. (2026). Xuanji: sonification of historical astronomical
> records. Journal of Open Source Software, 11(118), 6842.

is a **demonstration-only citation**. The co-authors after Aiden Yeoh are the
fictional placeholders above; the DOI, volume, issue, and article number are
illustrative and do not resolve to a real publication. There is no real JOSS
paper yet. The launch site correctly shows the paper as "in preparation" and
credits Aiden Yeoh alone.

## 3. How the figures and audio are generated

The waveform + log-frequency spectrogram plates (for example
`assets/img/fig/sn1054.png`) and the audio files in `assets/audio/` are **real
data figures produced by the reference sonification engine**, not stock clips
and not placeholder blocks, and not "AI music."

The pipeline is deterministic and documented:

1. A historical record (a court-chronicle guest-star entry, an eclipse timing, a
   comet track) is reduced to a **reconstructed light curve**: an array of
   brightness-versus-time samples inferred from the dated brightness phrases in
   the source, with the gaps left as gaps rather than filled.
2. The engine applies three fixed mapping rules, brightness to pitch, time to
   tempo, sky-position to stereo, to turn that array into an audio signal. There
   are no learned weights and no randomness, so the same record always returns
   the same audio.
3. The plate is rendered from the returned audio array (waveform panel + log-
   frequency spectrogram panel). Nothing in the figure comes from outside the
   returned signal.

The figures therefore illustrate the tool honestly: they are what the library
would emit for these records. They are demonstration renders for a sample build,
not published scientific results.

## 4. Astronomy accuracy locks

The following cross-identifications are fixed on the site and must never be
swapped: SN 1006 in Lupus (the brightest recorded stellar event); SN 1054 in
Taurus, which became the Crab Nebula; SN 185 as the candidate behind RCW 86;
SN 1604 as Kepler's supernova; the Dunhuang star chart at roughly 700 CE (British
Library); and the Suzhou (Soochow) planisphere engraved 1247 CE. Each curated
record on the site keeps its primary source, its modern cross-identification,
and how firm that link is; debated remnants stay labelled debated. This is the
history-of-science epistemic frame: the point is how a historical note becomes
citable data through cross-identification, stated uncertainty, and translation,
not a celebration of "ancient wisdom."

## 5. Honesty firewall

Public author of this artifact: **Aiden Yeoh**. No real living person is named
anywhere on the shipped pages as an advisor, endorser, mentor, or co-author. In
particular, **Prof. Li Hua-bai appears nowhere** on this site or in any shipped
page. The launch site marks the advisor seat as **open**, because it is open;
the goal site also marks it **open** rather than inventing a real endorser. Any
real advisor, once genuinely secured through the honest outreach path in the
execution kit, may be added only with that person's consent.

This disclosure lives here in `provenance.md` and on the planning dashboard. It
is deliberately kept off the shipped pages so the goal version reads as a clean
finished site (the intended teaching effect), while the truth of what is real
remains one click away for anyone who needs it.
