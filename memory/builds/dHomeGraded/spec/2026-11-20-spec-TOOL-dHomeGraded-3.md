# TOOL-dHomeGraded-3 — `gen_map.py` runs under the interpreter `.codebase-map.conf` names

**Status:** CLOSED · rev-1 · 2026-11-20 · node d · Tier-1 · base 8cdee285 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

An adopter whose map extractors import its own application needs the generator to run where that
application's packages live. Run-gates' regen step and the lander both spawn `gen_map.py` under the
interpreter gov's resolver picks, floored at 3.15, so an adopter on an older application environment
cannot regenerate its map, and its lander aborts before the bar.

## 2. Scope (IN)

- **S1** — When `.codebase-map.conf` sets `GEN_MAP_PYTHON`, `gen_map.py` runs itself once under that
  command, with every argument it was given, and exits with that run's code; the re-run carries an
  environment marker so it never re-runs again. Unset, nothing changes. Observed by AC1.
  **Readers:** by name: `tools/codebase-map/kit.toml`, whose `optional_keys` lists it · by value:
  `gen_map.py`, the only reader of the command it names.

## 3. Non-goals (OUT)

- Any other generator: each kit that imports adopter code declares its own key when it needs one.
- The run-gates resolver's floor, which stays 3.15 for gov's own code.

### Edges

none

## 4. Design

`MAP_DIFF_CMD` is the precedent: an adopter already names the command its map diff runs under. The
new key names an interpreter command, split with `shlex`, and `gen_map.py` hands itself and its own
argument list to it with `GEN_MAP_REEXEC=1` in the environment. A command that cannot start exits 2
naming the key.

### Files touched (estimate)

- `tools/codebase-map/gen_map.py`
- `tools/codebase-map/kit.toml`
- `tools/codebase-map/README.md`
- `tools/codebase-map/selftest.py`

## 5. Acceptance criteria

- **AC1** — When `python tools/codebase-map/gen_map.py --check` runs in a tree whose
  `.codebase-map.conf` sets `GEN_MAP_PYTHON` to a command that exits 7, it exits 7, and with
  `GEN_MAP_REEXEC=1` already set it runs the map itself. Red when: the unchanged generator ignores the
  key, as it did on inCMS, whose extractors import FastAPI from a 3.12 venv.

## 6. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map coverage + freshness` · `codebase-map adopter e2e` · `govkit selftest` · `policy fixtures`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-20 · initial draft.
