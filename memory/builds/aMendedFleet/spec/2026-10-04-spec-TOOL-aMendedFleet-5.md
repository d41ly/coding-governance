# TOOL-aMendedFleet-5 — `transition-audit arms` passes on the hosted runner: the audit writes UTF-8

**Status:** CLOSED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

`transition-audit arms` has been red on every push run of the remote CI workflow, always on one
assertion: AC11 reads `after=''`. The report suspected a fixture leaking `__pycache__`. The cause is
the audit's own stdout codec. `transition_audit.py` prints its `·` separators through Python's
default stdout encoding, which on a Windows host outside UTF-8 mode is the ANSI code page, so the
middle dot arrives as the single byte 0xB7 and the suite's `\xc2\xb7` pattern matches nothing. Node
a never sees it because its user environment exports `PYTHONUTF8=1`. This unit makes the audit write
UTF-8 on every host, and makes the suite run its fixtures under the hosted runner's conditions so
node a's environment can no longer hide the class. The `__pycache__` leak is real and is fixed here
too, because it is the same defect: a fixture inheriting ambient Python state it never declared.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/transition_audit.py` reconfigures its stdout to UTF-8 when it runs as
  a script, in its `__main__` block and nowhere else, so a module that imports it keeps its own
  stdout. Observed by AC1 and AC2.
- **S2** — The transition-audit suite declares the Python codec it runs under: it exports
  `PYTHONUTF8=0` and unsets `PYTHONIOENCODING` before its first Python call, so on a Windows node
  every arm sees the ANSI code page the hosted runner sees. Observed by AC3.
- **S3** — Where the host's redirected stdout codec is UTF-8 anyway, the suite prints one line
  saying the codec dependency is ungraded on this host, and never a FAIL. Observed by AC5.
- **S4** — The suite exports `PYTHONDONTWRITEBYTECODE=1` beside S2, and the F11 block asserts that
  each `checkout` it makes before an `accounted()` call landed on the commit it named, outside the
  command substitution so a failed assertion reaches the suite's status. Observed by AC4.

## 3. Non-goals (OUT)

- A repo-wide gate for the stdout-codec class. `tools/gate-lint/encoding_posture.py` says in its
  header that stdout encoding is out of its scope, and the class reaches every Python entry point
  that prints a non-ASCII byte. Whether the bar should run its legs with `PYTHONUTF8` unset is a
  question for this build's census of the held suites, which may find more members of the class.
- The matching fixes in other kits. `tools/govkit/matrix.py` is unit 4's, and `lexicon_conf.py` is
  unit 6's.
- Moving the memory-tree kit version. Several units of this build touch that kit, and a version moved
  before the last of them is owed again, so the build moves it once after its last memory-tree pass.
  The close's `kit epoch` leg grades that move.
- Changing the suite's `\xc2\xb7` patterns. They are correct once the producer writes UTF-8.

### Edges

- **hands-off** `TOOL-aMendedFleet-7` — whether other held suites red on the same stdout codec, and
  whether a bar-level class gate is owed, is that census's question.

## 4. Design

### Evidence

Read at base `7af5f564`, which carries the same bytes for both files as `origin/main` at `35438ba0`.

- The remote CI workflow `.github/workflows/remote-ci.yml` runs its `bar` job on `windows-latest`
  under Git-Bash, not on Linux. It sets `core.autocrlf false` globally and exports neither
  `PYTHONUTF8` nor `PYTHONDONTWRITEBYTECODE`.
- Push runs 36938524056, 37003260109, 37194768619, 37200259184 and 37220352485 each red this leg with
  `FAIL AC11: delta() before the merge and --report after it disagree`, `before` carrying one entry
  and `after` empty. Each also prints two `untracked working tree files would be overwritten by
  checkout` errors naming `tools/memory-tree/__pycache__/transition_audit.cpython-312.pyc`.
- Node a exports `PYTHONUTF8=1` and `PYTHONDONTWRITEBYTECODE=1` in its user environment. Without the
  first, a redirected Python stdout on node a reports `cp1251` and prints U+00B7 as the single byte
  0xB7.
- `PYTHONUTF8=0 PYTHONIOENCODING= python tools/memory-tree/transition_audit.py --report` over this
  tree printed 12 lines carrying a bare 0xB7 and none carrying the UTF-8 pair, in 1.5 s.
- A scratch slice of the suite, its prologue plus its F11 block with `KIT_MT` set by hand, discriminated
  the two defects on node a. With `PYTHONUTF8` unset it printed the CI's `FAIL AC11` line with
  `after=''`, whatever `PYTHONDONTWRITEBYTECODE` held. With `PYTHONUTF8=1` and bytecode writing on, it
  printed the two checkout errors and no FAIL. The same slice on Linux, under WSL on node a, passed
  in both bytecode modes and printed the checkout errors with bytecode writing on.

### Mechanism

S1 is one line, placed before the `sys.exit(main(...))` call in the `__main__` block, and it is the
first line of the pair `tools/memory-tree/adopt-memory-tree.sh` already carries:
`sys.stdout.reconfigure(encoding="utf-8")`. Newline translation is untouched, which is what the slice
measured as passing under `PYTHONUTF8=1`. The module's diagnostics go to stdout through `SAY`, and
its two stderr lines are usage refusals whose fixed text is ASCII, so stderr needs nothing here.

S2, S3 and S4 sit in one block directly after the suite resolves `PY`, because S3's probe needs it:

```bash
export PYTHONUTF8=0 PYTHONDONTWRITEBYTECODE=1
unset PYTHONIOENCODING
case "$("$PY" -c 'import sys; print(sys.stdout.encoding)' | tr -d '\r')" in
  utf-8|utf8|UTF-8) echo "transition-audit: this host's redirected stdout is UTF-8 anyway, so the codec dependency is UNGRADED here" ;;
esac
```

S4 moves the two `checkout` calls out of `acct()` and into the lines that call it, each followed by a
`git rev-parse HEAD` comparison that calls `bad` on a mismatch. Inside `$(acct ...)` a `bad` would
set `st` in a subshell and be lost. Without S4 the second `accounted()` arm is disarmed on any host
that writes bytecode: the aborted checkout leaves HEAD on the commit the arm passes as the tip, so
"read HEAD's tree" and "read the tip's tree" give the same answer. `FLOOR_ASSERTIONS` rises by the
assertions S4 adds, read from the suite's own `PASS` line.

### Files touched (estimate)

- `tools/memory-tree/transition_audit.py`
- `tools/memory-tree/transition-audit.test.sh`

### Alternatives rejected

- **Export `PYTHONUTF8=1` in the suite.** It fixes the suite and nothing else. Check 26 of the
  hygiene engine and the `.githooks/commit-msg` carrier run the same module, and the encoding-posture
  lint states this exact reasoning for its own class.
- **Match the bare 0xB7 in the suite's pattern as well.** It encodes a host's code page into a test
  and leaves every other consumer reading two byte spellings of one separator.
- **Split S4 into its own unit.** S2 and S4 are the same mechanism, the suite declaring the ambient
  Python state it depends on, in one block of one file. Two units would sequence two passes over that
  block.

## 5. Production-readiness checklist

- security — N/A: no new input, write path or surface.
- perf / scale — one extra Python process per suite run for S3's probe.
- error / empty / loading states — S3's announce line is the skip state, and it is never silent.
- observability — the announce line names the ungraded dependency on every UTF-8 host.
- risks — S2 runs every arm under node a's `cp1251`, where the hosted runner has `cp1252`; a Python
  call in the suite that prints a character only one of them encodes would red on one host only.
  AC3 runs the F11 arms under it, and the close's bar runs every arm under it.
- testing — AC1 to AC5, each with a staged break observed red.
- migration — N/A: no data shape moves.
- user docs — N/A: no user-facing surface; the class is already a section of
  `memory/gotchas/fixture-inherits-ambient-machine-state.md`.

## 6. Acceptance criteria

- **AC1** — When `PYTHONUTF8=0 PYTHONIOENCODING= python tools/memory-tree/transition_audit.py --report`
  runs on node a, piped into `LC_ALL=C grep -c $'\xc2\xb7'`, the count is at least 1 and no output
  line carries a 0xB7 byte without its 0xC2 lead.
  Red when: S1's line is absent, which at base printed 12 bare-0xB7 lines and no UTF-8 pair.
  cost: about 1.5 s with the delta cache warm.
  figure: the 12 is PINNED, measured on node a on 2026-10-04; the criterion's own count is DERIVED.
- **AC2** — When a scratch slice of the transition-audit suite, its prologue plus its F11 block with
  `KIT_MT` set by hand, runs on node a under `env -u PYTHONUTF8`, it prints no `FAIL AC11` line and
  `before` equals `after`.
  Red when: S1's line is absent, which at base printed `FAIL AC11` with `after=''`.
- **AC3** — When the same slice runs under node a's ambient `PYTHONUTF8=1`, with S2's block present and
  S1's line removed as a staged break, it prints `FAIL AC11`.
  Red when: S2's exports are absent, so the ambient UTF-8 mode masks the defect, which is how it
  stayed green on node a.
- **AC4** — When the slice runs with `PYTHONDONTWRITEBYTECODE` unset in the calling shell, it prints no
  `would be overwritten by checkout` line and S4's assertions pass; with
  `PYTHONDONTWRITEBYTECODE=1` removed from S2's export as a staged break, S4's assertion reds naming
  the commit it could not check out.
  Red when: S4 checks inside the command substitution, so the aborted checkout grades nothing.
- **AC5** — When the slice runs on Linux under `wsl` on node a, it prints S3's `UNGRADED` line and
  still passes.
  Red when: S3's probe is absent, so a green on a UTF-8 host reads as a graded codec arm.
  fixture: node a's WSL distro holds git and Python 3; the slice needs a copy of the three kit
  directories in a fresh repository, because Linux git cannot open the worktree's Windows gitdir.

## 7. Gates

`transition-audit arms` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/transition-audit.test.sh · S2 exports PYTHONUTF8=0, so AC11 is the codec arm on every Windows node, staged red by removing S1's line · none
New arm: tools/memory-tree/transition-audit.test.sh · S4's checkout assertions, staged red by removing PYTHONDONTWRITEBYTECODE=1 from the export · 62 rises by the assertions S4 adds

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the remote CI logs, the module and suite at base, and a
  scratch slice of the suite run on node a under Windows and under WSL.

## 10. Reuse audit

The seam is a line this repo already ships twice, and no symbol-level seam fits.
`python tools/codebase-map/reuse_lookup.py "python stdout encoding utf-8 on a windows locale codec"`
returned no function that reconfigures a stream; its nearest hit was `check_encoding` in
`tools/gate-lint/encoding_posture.py`, whose header puts stdout out of scope. The line S1 copies is
`tools/memory-tree/adopt-memory-tree.sh` line 204, also at `tools/lib/render-doc.sh` line 135. The
suite-level pin S4 copies is `.githooks/straggler-guard.test.sh` line 44, which exports
`PYTHONDONTWRITEBYTECODE=1` for this same checkout abort. The codec-forcing arm S2 follows
`tools/govkit/selftest.py`, which runs its blocks with `PYTHONUTF8=0` and `PYTHONIOENCODING` unset.
Recall returned the class as a section of `memory/gotchas/fixture-inherits-ambient-machine-state.md`.

Where the report and the tree disagree: the report places this leg's failure on Linux CI, and the
workflow runs on `windows-latest`. It names the `__pycache__` leak as the suspect; that leak is real,
but the slice shows AC11 reds without it and passes with it, so the cause is the stdout codec.

Recall terms used: `python tools/memory-recall/query.py "why does a python tool print wrong bytes on a Windows host without PYTHONUTF8, and how was it fixed before" --terms "PYTHONUTF8 cp1252 cp1251 stdout reconfigure encoding utf-8 locale codec Windows CI remote-ci host-dependent red"`
