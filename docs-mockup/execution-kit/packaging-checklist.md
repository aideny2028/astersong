# packaging-checklist.md

The file skeleton for a defensible modern Python package. Match the claims the
launch site already makes (BSD-3-Clause, Python >= 3.10, built on Astropy).

## Repo layout
```
xuanji/
  pyproject.toml         # PEP 621 metadata, deps, build backend
  LICENSE                # BSD-3-Clause (matches the site)
  README.md              # install + first-sound example
  CHANGELOG.md           # keep current, one entry per release
  AUTHORS.md             # real contributors only; you alone at first
  CITATION.cff           # how to cite; real Zenodo DOI once minted
  CONTRIBUTING.md        # good-first-issues: add a record / translation / test
  src/xuanji/
    __init__.py          # exposes from_record, sonify, plot, __version__
    mapping.py           # the three fixed rules
    lightcurve.py        # LightCurve type + reconstruction
    skypath.py           # SkyPath stereo model
    record.py            # record schema + validator (source, cross-ID, firmness)
    plot.py              # the two-panel waveform + spectrogram plate
    data/records/        # the ten curated launch records (sourced, cross-ID'd)
  tests/
    test_determinism.py  # same record in -> identical audio out (the key test)
    test_mapping.py
    test_records.py      # every record validates; firmness stated
  docs/                  # Sphinx or MkDocs build; the launch/ pages front it
  .github/workflows/ci.yml  # pytest matrix, Python 3.10-3.13
```

## pyproject.toml essentials
- `requires-python = ">=3.10"`
- dependencies: `numpy`, `scipy`, `astropy`, `soundfile`
- optional `[audio]` extra if you split heavier playback deps
- version single-sourced (e.g. `xuanji.__version__`)
- license = BSD-3-Clause, classifiers set accordingly

## Before first release
- [ ] `python -m build` succeeds; `twine check dist/*` passes.
- [ ] Fresh-venv install works from TestPyPI (see `first-pypi-release.md`).
- [ ] `AUTHORS.md` and `CITATION.cff` name only real people.
- [ ] `IMAGE-CREDITS.md` in the docs matches shipped images.
- [ ] `provenance.md` shipped so the sample-versus-real line is clear.
