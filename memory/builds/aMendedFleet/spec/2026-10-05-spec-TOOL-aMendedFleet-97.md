# TOOL-aMendedFleet-97 — held-red C1: the kits' Python stdio is UTF-8 on a host whose code page is cp1252

**Status:** CLOSED · rev-2 · 2026-10-05 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-05 · order 98

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Eight suites of the daily held job are red on cause C1 of unit 7's census
(`memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-7-1-held-red-census.md`). The
hosted runner runs Python outside UTF-8 mode, so a kit program's redirected stdout is cp1252: an em
dash or a middle dot reaches a UTF-8 reader as the byte 0x97 or 0xB7, and a check mark cannot be
encoded at all. Node a exports `PYTHONUTF8=1` and never sees it. This unit makes the six producers the
census's failing lines name, and the two codebase-map siblings sharing one of their lines, write UTF-8
on every host, and makes every in-tree reader of them decode UTF-8, so a producer and its readers
agree whatever the code page.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/row_grammar.py`, `tools/govkit/govkit.py`, `tools/settings-merge.py`
  and `tools/check-spec-tokens.py` reconfigure stdout to `encoding="utf-8"` and stderr to
  `encoding="utf-8", errors="backslashreplace"` inside their `__main__` block and nowhere else, so an
  importer keeps its own streams. Observed by AC1, AC2, AC4 and AC5.
- **S2** — The three codebase-map entry points `tools/codebase-map/gen_map.py`,
  `tools/codebase-map/map_diff.py` and `tools/codebase-map/reuse_lookup.py` already reconfigure stdout
  at import with `errors="replace"`; that one line gains `encoding="utf-8"` in place. Observed by AC3.
- **S3** — `tools/runlog/selftest.py` reconfigures its own stdout and stderr the same way as S1, in its
  `__main__` block, because the producer there is the suite itself printing a check mark. Observed by
  AC6.
- **S4** — The 15 in-tree captures of an S1 or S2 producer that decode with the locale codec decode
  `encoding="utf-8", errors="replace"`: 14 captures of `govkit.py` in `tools/govkit/selftest.py` and
  the `gen_map.py` capture in `tools/codebase-map/selftest.py`. The govkit suite's subprocess row of
  `memory/project/encoding-posture-sites.txt` falls by 14, and the codebase-map suite's subprocess
  row, which declares that one capture alone since units 86 and 88 drained its other three, is
  deleted. Observed by AC7.
- **S5** — The remote observation: the first scheduled run of the remote CI workflow after landing
  carries none of C1's failure signatures. Observed by AC8.

## 3. Non-goals (OUT)

- Setting `PYTHONUTF8` or `PYTHONIOENCODING` in `.github/workflows/remote-ci.yml`. F1 says why.
- The other Python entry points under `tools/` that print non-ASCII. A probe on 2026-10-05 found 46
  files with a `__main__` block and a non-ASCII byte on a print or write line, one of them unit 5's,
  already reconfigured (PINNED; re-derive with the loop in §4's Evidence). This unit takes 8 of the
  rest. None of the other 37 is named by a failing line of the census, and a producer switched to
  UTF-8 while a reader of it still decodes the locale codec is the break S4 exists to prevent, so each
  needs its readers found first. A later census red names the next one.
- A static gate for the class. `tools/gate-lint/encoding_posture.py` states in its header that a
  stdout-encoding check needs runtime context and is not attempted; the daily held job on a cp1252
  runner is the runtime observer, and this unit keeps it one (F1).
- The other causes red in the same suites: memory-hygiene's conf-example arm (C7, unit 103),
  foreign-prefix parity's review-replay row (C8, unit 104) and the unattended driver's views arms
  (C10, unit 1). Those suites can stay red after this unit for those reasons.
- Moving the kit versions of codebase-map, govkit, memory-tree and runlog. The build moves every kit
  version it owes once, after the last pass touching that kit; the close's `kit epoch` leg grades it.

### Edges

none

## 4. Design

### Evidence

Re-verified 2026-10-05 on node a at HEAD `34a99ad17`, whose bytes for every file below equal base
`7af5f564`. Node a's locale is cp1251, where 0x97 is an em dash and 0xB7 a middle dot, the same bytes
cp1252 uses, so node a reproduces the runner under `PYTHONUTF8=0` with `PYTHONIOENCODING` unset.

The decode probe used throughout §6 exits 0 only when its input is strict UTF-8 AND carries a
non-ASCII byte; the second clause is its liveness, since an all-ASCII capture decodes as anything:

```bash
python -c 'import sys; b = sys.stdin.buffer.read(); b.decode("utf-8"); sys.exit(0 if max(b, default=0) > 127 else 3)'
```

| Producer command, run under `env -u PYTHONIOENCODING PYTHONUTF8=0` | Probe at base | Under `PYTHONUTF8=1` |
|---|---|---|
| `python tools/memory-tree/row_grammar.py --check` | 1, a decode error | 0 |
| `python tools/govkit/govkit.py epoch --base HEAD~1` | 1 | not run |
| `python tools/govkit/govkit.py --help`, stderr merged | 1 | 0 |
| `python tools/codebase-map/map_diff.py --help` | 1 | 0 |
| `python tools/check-spec-tokens.py` | 1 | 0 |

- `env -u PYTHONIOENCODING PYTHONUTF8=0 python tools/settings-merge.py --selftest` exits 1 with
  `TypeError: argument of type 'NoneType' is not a container or iterable` at `_selftest`'s nested-copy
  assertion: the census's CI failure, reproduced on node a in about one second.
- The 15 locale captures were found by walking every tracked `tools/` and `skills/` Python file's AST
  for a `subprocess` call carrying `text=True` with no `encoding=` whose source names one of the S1 or
  S2 producers. `tools/govkit/selftest.py` holds 14, among them its `run` helper near line 225, and
  `tools/codebase-map/selftest.py` holds the `gen_map.py` capture near line 2465. No product file
  captures these producers with the locale codec; the bash readers read bytes and already expect
  UTF-8. `python tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt . tools skills`
  prints OK at base, declaring 38 sites for the govkit selftest and 4 for the codebase-map selftest.
- The population §3 counts, re-derived by:

  ```bash
  for f in $(git grep -l '__name__ == .__main__.' -- 'tools/*.py' 'skills/*.py'); do
    n=$(LC_ALL=C grep -P '[^\x00-\x7F]' "$f" | grep -c 'print\|write(\|sys.exit(\|SystemExit(')
    [ "$n" -gt 0 ] && echo "$(grep -c 'stdout.reconfigure(encoding' "$f") $f"
  done
  ```

- The runlog suite's red is its own `print` of a name carrying U+2713, built from
  `test_ac2_escape_round_trip`'s value list, into a cp1252 stdout: `UnicodeEncodeError`, census row.
- The census's failing lines map to producers as follows: codebase-map kit selftest to `gen_map.py
  --check`; govkit selftest to `govkit.py epoch`; row-grammar selftest and memory-hygiene's check-20
  arm to `row_grammar.py --check`; settings-merge selftest to its own nested `--selftest` copy;
  spec-tokens self-test and the unattended driver's `[bar]` arm to `check-spec-tokens.py`; runlog
  selftest to itself. Foreign-prefix parity's two C1 rows re-run row-grammar and settings-merge.

### Mechanism

S1 and S3 are the pair `tools/memory-tree/adopt-memory-tree.sh` and `tools/lib/render-doc.sh`
already carry, placed where units 5 and 6 placed theirs, first in the `__main__` block. `newline` is
untouched. S2 edits one existing line per file and does not move it, because those three programs
already chose import-time reconfiguration and keep `errors="replace"`. S4 adds the keywords unit 4
used in `tools/govkit/matrix.py`; `errors="replace"` keeps a stray byte from killing a reader thread,
which otherwise hands the arm a `None` stream and an unrelated `TypeError`.

### Files touched (estimate)

- `tools/memory-tree/row_grammar.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/settings-merge.py`
- `tools/check-spec-tokens.py`
- `tools/codebase-map/gen_map.py`
- `tools/codebase-map/map_diff.py`
- `tools/codebase-map/reuse_lookup.py`
- `tools/codebase-map/selftest.py`
- `tools/runlog/selftest.py`
- `memory/project/encoding-posture-sites.txt`

### Alternatives rejected

- **`PYTHONUTF8: 1` in the held job's env.** One line, and it greens the runner. It also makes the
  held job a UTF-8 host like node a, which deletes the only place this class is observed, and leaves
  every adopter's Windows host outside UTF-8 mode on the broken bytes. F1.
- **Readers decode the locale codec instead.** The bash readers grep UTF-8 literals and cannot.
- **Every Python entry point under `tools/` at once.** See §3: a producer switched without its
  readers found is a new break, and 43 of them are named by no failing line.

## 5. Production-readiness checklist

- security — N/A: output encoding of local tools, no write path or trust boundary.
- perf / scale — none; one reconfigure call per process.
- error / empty / loading states — `errors="replace"` on S4 captures keeps a stray byte from turning a
  stream into `None`; `backslashreplace` on stderr keeps an unencodable diagnostic printable.
- observability — unchanged text; only its bytes on a non-UTF-8 host change.
- risks — a reader outside this tree that decodes these programs' output with the locale codec on a
  Windows host outside UTF-8 mode now sees UTF-8. The govkit migration runbook's blocks export
  `PYTHONUTF8=1` already, so they read UTF-8 either way; its R3-7 arm, which runs them with UTF-8 mode
  off, may lose the case it discriminated, and the closing review reads that arm.
- testing — AC1 to AC5 reproduce each producer's CI failure on node a at base and observe it gone;
  AC7 is the encoding-posture checker over its own registry.
- migration — none.
- user docs — N/A: no operator-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `env -u PYTHONIOENCODING PYTHONUTF8=0 python tools/memory-tree/row_grammar.py --check`
  runs with its stdout piped to §4's decode probe, the probe exits 0.
  Red when: run against the base file, the probe exits 1 on a decode error, measured 2026-10-05.
- **AC2** — When `env -u PYTHONIOENCODING PYTHONUTF8=0 python tools/govkit/govkit.py epoch --base HEAD~1`
  runs piped to the decode probe, and again for `govkit.py --help` with stderr merged into stdout,
  both probes exit 0.
  Red when: at base both exit 1, measured 2026-10-05.
- **AC3** — When `env -u PYTHONIOENCODING PYTHONUTF8=0 python tools/codebase-map/map_diff.py --help`
  runs piped to the decode probe, it exits 0, and `grep -c 'reconfigure(encoding="utf-8", errors="replace")'`
  over each of the three S2 files prints `1`.
  Red when: at base the probe exits 1 and each grep prints `0`.
- **AC4** — When `env -u PYTHONIOENCODING PYTHONUTF8=0 python tools/check-spec-tokens.py` runs piped
  to the decode probe, the probe exits 0.
  Red when: at base the probe exits 1 on the report lines' 0xB7 separators.
- **AC5** — When `env -u PYTHONIOENCODING PYTHONUTF8=0 python tools/settings-merge.py --selftest`
  runs, it exits 0 and prints `settings-merge selftest: PASS`.
  Red when: at base it exits 1 with the `TypeError` §4 quotes, the census's CI line.
- **AC6** — When `git grep -n -F 'stdout.reconfigure(encoding="utf-8")'` runs over the runlog
  suite's own file, it prints one line, and that line sits in the file's `__main__` block.
  Red when: the suite still prints into the locale codec, so a cp1252 stdout raises on U+2713.
  permission: the behavioural observation is the runlog suite, which no pass runs; AC8 is its remote
  observation.
- **AC7** — When `python tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt . tools skills`
  runs, it prints OK, the registry's subprocess row reads 24 sites for the govkit suite's file, and
  the registry carries no subprocess row for the codebase-map suite's file.
  Red when: a capture S4 names still decodes the locale codec, so the scan measures one more site than
  the shrunk row declares and names the file.
  figure: PINNED from the counts at the pass's HEAD `ef26beda1`, 38 and 1, less the 14 and 1 S4
  changes; a concurrent unit touching either file re-derives them.
- **AC8** — When the first scheduled remote CI run after landing completes,
  `gh run view <id> --repo d41ly/coding-governance --log-failed` carries no `UnicodeDecodeError`,
  `UnicodeEncodeError` or U+FFFD expectation line in the eight C1 suites the census names.
  Red when: any of those suites still fails on a C1 signature on `windows-latest`.
  permission: observable only after the landing push, which the close performs.
  cost: one day, the schedule's period.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `row-grammar selftest` · `settings-merge selftest` · `spec-tokens self-test` · `memory-hygiene self-test` · `encoding posture (text IO names its encoding)` · `recall floor` · `spec tokens (a spec's own names resolve)`

No new arm: the held job on a cp1252 runner already grades every suite this unit fixes.

## 8. Open questions

- **F1** — Fix C1 in the code or in the workflow? The brief admits both. Setting `PYTHONUTF8: 1` in
  the held job is one line and greens the runner. Fixing the producers and their readers greens it too,
  fixes the same bytes on any adopter's Windows host outside UTF-8 mode, and keeps the held job a
  cp1252 host, the only runtime observer of the class: `tools/gate-lint/encoding_posture.py` declines a
  static stdout check, and unit 4 rejected the workflow line for the same leg class. Recommendation:
  the code. RESOLVED (agent, 2026-10-05, delegated): fix the six producers and their in-tree readers;
  the workflow keeps the runner's codec.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft; every producer's CI failure reproduced on node a under
  `PYTHONUTF8=0`, and the 15 locale captures of those producers counted.
- rev-2 · 2026-10-06 · S4 and AC7 re-derived at the pass's HEAD `ef26beda1`: units 86 and 88 left the
  codebase-map suite's subprocess row declaring 1 site, the `gen_map.py` capture, not 4, so that row
  is deleted rather than shrunk to 3; the 15 captures and the govkit row's 38 to 24 are unchanged.

## 10. Reuse audit

The seam is the stdio pair `tools/memory-tree/adopt-memory-tree.sh` and `tools/lib/render-doc.sh`
already carry, placed as `tools/memory-tree/transition_audit.py` (unit 5) and
`tools/lexicon/lexicon_conf.py` (unit 6) place it, plus the capture keywords
`tools/govkit/matrix.py` (unit 4) uses. No shared helper can carry it: each kit is copy-installed and
names nothing outside itself. `python tools/codebase-map/reuse_lookup.py "make a python program write
utf-8 to its stdout on a windows host whose code page is cp1252"` ranked name-stem neighbours only
(`write`, `write_text`, `python_symbols`), none of which touches a stream's codec; it reports `.sh` as
an unscanned layer, which is where two of the three precedents live, so they were found by grep for
`reconfigure(`. `python tools/memory-recall/query.py` returned units 4, 5 and 6, the gotcha
`memory/gotchas/fixture-inherits-ambient-machine-state.md`, and node d's dPolishedVitrine round-3
review recording that `govkit.py` never reconfigures its stdout, which is still true at base.

Recall terms used: PYTHONUTF8 PYTHONIOENCODING cp1252 locale codec stdout reconfigure utf-8 held remote-ci windows-latest em dash
