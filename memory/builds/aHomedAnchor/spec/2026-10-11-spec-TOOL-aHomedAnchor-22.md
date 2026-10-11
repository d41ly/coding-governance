# TOOL-aHomedAnchor-22 — command-line entry points write UTF-8 whatever the platform default

**Status:** INPROGRESS · rev-1 · 2026-10-11 · node a · Tier-1 · base b726385f · streams tooling · order 6 · closes TOOL-aHomedAnchor-10 TOOL-aHomedAnchor-11 TOOL-aHomedAnchor-14 · advances TOOL-aHomedAnchor-9 TOOL-aHomedAnchor-12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md](../prompts/2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md) | journal | TOOL-aHomedAnchor-23 TOOL-aHomedAnchor-24 TOOL-aHomedAnchor-25 |

<!-- /gen:spec-records -->

## 1. Goal

The held job's Python 3.12 on Windows writes a pipe in cp1252, so an em dash leaves `corpus_ids.py`, `lexicon.py` and `runlog.py` as byte 0x97 and every parent decoding UTF-8 reads garbage or crashes; `govkit/selftest.py` crashes printing a replacement character. Nodes set `PYTHONUTF8=1` and never see it.

## 2. Scope (IN)

- S1. The `__main__` guards of `tools/memory-tree/corpus_ids.py`, `tools/lexicon/lexicon.py`, `tools/runlog/runlog.py` and `tools/govkit/selftest.py` reconfigure stdout to UTF-8 and stderr to UTF-8 with `backslashreplace`, `govkit.py`'s own pattern. Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

Any other suite's red; running the unattended shard suites (owner, 2026-10-11).

### Edges

none

## 4. Design

The brief is `memory/builds/aHomedAnchor/prompts/2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md`. The red was read from the daily held job's run 38045767386 at `d006cfc5`.

### Files touched (estimate)

- `tools/memory-tree/corpus_ids.py`
- `tools/lexicon/lexicon.py`
- `tools/runlog/runlog.py`
- `tools/govkit/selftest.py`

## 6. Acceptance criteria

- **AC1** — When `corpus_ids.py --check` and `lexicon.py --suggest` run with `PYTHONUTF8=0`, their em dash is the UTF-8 bytes and no `0x97` byte appears. Red when: the guard is removed.
- **AC2** — When runlog selftest's `test_schema_*` functions run with `PYTHONUTF8=0`, none fails. Red when: `runlog.py` writes cp1252.
- **AC3** — When `python -m py_compile` runs over the four files, it exits 0. Red when: an edit breaks a guard.

## 7. Gates

`corpus-ids selftest` · `lexicon selftest` · `runlog selftest` · `govkit selftest` · `codebase-map kit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `pre-push run-log line` · `recall floor arms` · `run-gates run-log line`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

No existing seam fits beyond the site named in §2. Recall terms used: `--terms "held job red suite daily remote-ci PYTHONUTF8 cp1252 reconfigure fixture stale launcher overlaps"`.
