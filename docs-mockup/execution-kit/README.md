# Xuanji execution kit, from sample to shipped library

This kit is for you, Aiden. The docs site in this folder shows two states:
`launch/` (an honest first release) and `goal/` (where the project could get to).
This kit is the road between them: the concrete, ordered steps to turn the
reference engine into a real Python package that other people can install, cite,
and contribute to.

It is written to be honest. Nothing here asks you to claim something before it is
true. The `launch/` site is the version you ship first, and every claim on it is
one you can stand behind on release day. The `goal/` site is a destination, not a
starting position.

Read `../provenance.md` first so you are clear on what is real versus modelled.

## The one rule that governs everything

**The tool interprets the data; it does not author it.** Deterministic mapping,
sources cited, uncertainty kept, gaps left as gaps. Every decision below serves
that rule. If a "feature" would make the audio prettier by inventing data, it
does not ship.

## Milestones, in order

### Milestone 0, the private repo (a weekend)
- Create a private GitHub repo `xuanji` under an org you control
  (`xuanji-project`). Keep it private until v0.3.0 is real.
- Scaffold a modern package: `pyproject.toml` (PEP 621), `src/xuanji/` layout,
  `LICENSE` (BSD-3-Clause, matching the site), `README.md`, `CHANGELOG.md`,
  `AUTHORS.md` (you, alone, honestly).
- Pin dependencies: numpy, scipy, astropy, soundfile. Set `requires-python
  >= 3.10`.
- See `packaging-checklist.md` for the exact file list.

### Milestone 1, the engine you can defend (the core work)
- Implement the three mapping rules exactly as documented on the Mapping page:
  brightness to pitch, time to tempo, sky-position to stereo. No learned weights,
  no randomness.
- Implement the `LightCurve` and `SkyPath` types, `from_record`, `sonify`,
  `write`, and `plot`.
- Write the record schema (source, cross-identification, firmness of link) and a
  validator. A debated remnant stays labelled debated.
- Curate **ten** real records for the launch gallery (SN 1006, SN 1054, SN 185,
  SN 1604, a solar eclipse timing, a sunspot record, a comet track, and three
  more). Each keeps its primary source and modern cross-ID.
- Tests: a real `pytest` suite. The determinism test (same record in, same bytes
  out) is the one that matters most. Aim for meaningful coverage, not a number.
- CI: a GitHub Actions matrix over Python 3.10 to 3.13.

### Milestone 2, the first public release (v0.3.x)
- Reserve a Zenodo DOI (GitHub-Zenodo integration): the site already links a
  "reserved" DOI; make it real, then let the release mint the versioned DOI.
- Publish to **TestPyPI** first, install into a clean venv, confirm
  `pip install xuanji` then `import xuanji` works. Only then publish to real
  **PyPI**. See `first-pypi-release.md` for the exact commands.
- Tag `v0.3.1`, cut the GitHub release; Zenodo archives it and issues the DOI.
- Ship the `launch/` docs (see Milestone 3). This is your honest public debut.

### Milestone 3, docs hosting
- The `launch/` HTML in this folder is your content. Host it for free on GitHub
  Pages or Read the Docs. For a library, Read the Docs plus a Sphinx or MkDocs
  build that renders your docstrings is the long-term path; the hand-built pages
  here are the marketing overview that sits in front of it.
- Wire the `pip install xuanji` chip, the version pill, and the GitHub link to
  the real repo. Confirm `IMAGE-CREDITS.md` matches the images you actually ship.

### Milestone 4, the advisor (do this in parallel, early)
- The advisor seat is **open** on purpose. You need one real reviewer: a
  historian of science or an observational astronomer who will check your
  cross-identifications and lend real rigor. Do not name anyone until they say
  yes in writing.
- Use the CRCS professor-cold-email finder to build a target list. Good fits:
  faculty in history of astronomy, archaeoastronomy, or time-domain astronomy;
  authors of the papers your cross-IDs already rely on.
- See `advisor-outreach.md` for who to target, what to send, and the honesty
  rules (you are a high-school student; the project is real but early; you are
  asking for review, not a co-authorship you have not earned).

### Milestone 5, growth toward the goal (v0.4 and beyond)
- Open contribution: write `CONTRIBUTING.md`, label good-first-issues (add a
  record, add a translation, add a mapping test). The goal site's contributor
  team is what this milestone builds, one real person at a time.
- Add records past the first ten only when each is sourced and cross-identified.
- conda-forge feedstock once PyPI is stable and versions are settled.

### Milestone 6, the JOSS paper (only when the software earns it)
- The Journal of Open Source Software reviews the **software**, openly, on
  GitHub. Submit only when the package is tagged, archived (Zenodo DOI), tested,
  documented, and genuinely usable by someone who is not you.
- The `paper.md` + `paper.bib` are short. Authorship is everyone who made a
  substantial contribution, and no one who did not. Until then, the site
  correctly says "JOSS paper in preparation."
- See `joss-submission.md` for the readiness checklist and the honest authorship
  rule.

## What "done" looks like for the first release

- [ ] `pip install xuanji` works in a clean venv.
- [ ] Ten sourced, cross-identified records, each with firmness of link stated.
- [ ] Determinism test passes: same record returns identical audio bytes.
- [ ] Real Zenodo DOI minted by a tagged GitHub release.
- [ ] `launch/` docs hosted, all links and the install chip live.
- [ ] `IMAGE-CREDITS.md` verified against shipped images.
- [ ] `AUTHORS.md` lists only real contributors (you), advisor seat open.
- [ ] `provenance.md` present so the sample-versus-real line stays clear.

Ship that, and the launch site is true. Everything on the goal site is then a
matter of doing the work in the open, in public, with your name on it.
