# docs-mockup: internal design mockup, not for deployment

Internal design mockup; describes the target package; not for deployment
until the package exists and the docs match it.

Facts to keep straight when reading anything in this folder:

- These pages were written under the project's earlier working name
  (`xuanji`, shared with the archive project); the real package is
  **astersong** and lives at the repository root. Install commands, import
  names, version numbers, test counts, and the GitHub org named in these
  pages describe the target, not the present.
- The `launch/` pages depict an honest v0.3.x release that does not exist
  yet; the `goal/` pages depict a mature v1.4.x project whose contributors,
  JOSS citation, and adoption figures are fictional placeholders (disclosed
  in `provenance.md`).
- The 28 audio players across these pages point at `assets/audio/` files
  that were never delivered; no audio exists anywhere in this folder.
  `provenance.md` section 3 claims those files are "real data figures
  produced by the reference sonification engine": that claim is wrong; no
  engine and no audio were delivered. The first real, tested rendering code
  is the `astersong` package at the repository root.
- `execution-kit/`, `provenance.md`, and `DESIGN.md` are consultant-voice
  planning documents, kept as design reference.

The mapping semantics documented on the Mapping page (brightness to pitch,
time to tempo, position to stereo, determinism guarantee) are the normative
design the real package follows.
