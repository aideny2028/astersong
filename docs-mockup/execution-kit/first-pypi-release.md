# first-pypi-release.md

The exact path to your first real `pip install xuanji`. Do TestPyPI before PyPI.
A name published to PyPI cannot be reused, so rehearse on TestPyPI first.

## One-time setup
1. Register accounts on both https://test.pypi.org and https://pypi.org.
2. Turn on 2FA on both (required).
3. Create an API token on each; store them in `~/.pypirc` or use them inline.
4. Confirm the name `xuanji` is free on PyPI before you get attached to it.

## Build
```
python -m pip install --upgrade build twine
python -m build            # produces dist/xuanji-0.3.1.tar.gz and the wheel
python -m twine check dist/*
```

## Rehearse on TestPyPI
```
python -m twine upload --repository testpypi dist/*
# then, in a clean virtualenv:
python -m venv /tmp/xj && source /tmp/xj/bin/activate
pip install --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ xuanji
python -c "import xuanji as xj; print(xj.__version__)"
```
If import fails or a dependency will not resolve, fix `pyproject.toml` and bump
to a fresh version number. You cannot overwrite a file already uploaded.

## Publish for real
```
python -m twine upload dist/*
```
Then verify from a clean venv with plain `pip install xuanji`.

## Tag and archive
1. Connect the repo to Zenodo (Zenodo GitHub settings, flip the repo on) BEFORE
   you tag, so the release is captured.
2. `git tag v0.3.1 && git push --tags`, then cut the GitHub release.
3. Zenodo mints the versioned DOI. Put the real DOI on the Cite page and in
   `CITATION.cff`, replacing the reserved placeholder.

## Version discipline
- Pre-1.0 means the API can still change; say so. The launch site's `v0.3.1`
  pill is honest about this.
- Bump the version for every upload. Keep `CHANGELOG.md` current.
