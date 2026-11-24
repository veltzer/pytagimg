# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `src/pytagimg/main.py:16` - the only command, `run` ("run gui to tag images"), is a bare `pass`, yet the package is published to PyPI as `Development Status :: 4 - Beta` (`pyproject.toml:23`); implement it or mark the project as `1 - Planning` / `2 - Pre-Alpha`.

## Low

- `src/pytagimg/configs.py:9` - `ConfigRemoveFolders` ("Parameters for the remove folder tool") is a copy-paste leftover from another project and is used nowhere; delete it.
- `doc/TODO.txt:1` - the TODO is about a "symlink install operation", which does not exist in this project (leftover from another repo); replace with the real TODO or delete.
- `pyproject.toml:85` - `mypy_path = "src:python:scripts"` names `python` and `scripts` directories that do not exist; reduce to `src`.
