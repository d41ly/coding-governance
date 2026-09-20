# TOOL-aWokenSentinel-25 — `check-arms.py` names a STRANDED prefix beside its UNARMED row and prints the whole signature, so an arm that stops short of a long message is diagnosed rather than read as absent

**Status:** SPECCED · rev-1 · 2026-09-20 · node a · Tier-2 · base 830c46e8 · streams tooling · order 25

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-prompt-TOOL-aWokenSentinel-25-1-build-brief.md](../prompts/2026-09-20-prompt-TOOL-aWokenSentinel-25-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H1 (round 4, raw ids 12, 22 and 33): `TOOL-aWokenSentinel-22` wrote the first
`hit` of each arm pair as a readable prefix of the branch's sentence and said that prefix "is what
`check-arms.py` reads as an arm". `signature()` at `tools/memory-tree/check-arms.py:107` takes the
longest literal run before the first interpolation, which for spec 16's two sentences runs to
`marker holds` (123 characters) and to `is not the one` (115 characters), and `classify()` at `:235`
arms a branch only when a test line CONTAINS that whole run, so both branches the unit exists to arm
read UNARMED. The literals are folded at spec 22's rev-2. The CLASS is older than spec 22 and is
recorded twice already: the tool's own docstring says "an arm that stops at the last WORD reads as
unarmed with no hint why; run `--report` and copy the row it prints", and
`memory/gotchas/arm-literal-strands-on-message-edit.md` gives the same remedy. That remedy is broken
for exactly the messages that strand: `cmd_report()` at `:311` prints `b['sig'][:72]`, so for any
signature over 72 characters the row it tells the author to copy IS a prefix, and copying it
produces the defect it is the remedy for. This unit makes the tool say what it sees: `--report`
prints the whole signature, and an UNARMED branch whose test file carries a line holding the
signature's opening run but not the whole of it is reported as STRANDED at that test line, by
`--report` and in `--check`'s refusal, so the next author is told which line to lengthen rather than
that nothing arms the branch.

## 2. Scope (IN)

- **S1** — `cmd_report()` prints each branch's signature whole; the `[:72]` slice is removed, and
  nothing else in the row changes. Observed by AC1.
- **S2** — `classify()` records, for every branch that is not armed, the first non-comment,
  non-negative line of the test file that contains the signature's first `STRAND_MIN` characters
  (24, a module constant beside `NEGATIVE_RE`) but not the whole signature, as the branch's
  `stranded` line number, or `None`. A signature shorter than `STRAND_MIN` cannot strand by prefix,
  because a line containing all of it arms the branch. Observed by AC2 and AC3.
- **S3** — `cmd_check()`'s unarmed refusal, the sentence at `:255` beginning `has no POSITIVE
  assertion naming its own failure text`, gains the clause ` — a STRANDED prefix at <test>:<line>
  stops short of the signature; copy the whole row --report prints` when `stranded` is set, and is
  unchanged otherwise. `--report` prints `STRANDED <test>:<line>` at the end of the row for the same
  branches. Observed by AC2.
- **S4** — `cmd_selftest()` gains three arms over its scratch repo: a gate whose message is over 72
  characters and whose test quotes the first 40 of them reads UNARMED with `STRANDED` naming the
  test line in `--check` and in `--report`; the same gate with the test quoting the whole
  signature reads ARMED, which is the control; and the `--report` row for that gate contains the
  signature to its last character. Observed by AC3.
- **S5** — The docstring of `signature()` and the gotcha's remedy sentence say what is now true:
  `--report` prints the row whole, and a stranded prefix is named as such. The gotcha's body keeps
  its anchors and its `gated by` sentence; only the remedy paragraph moves. Observed by AC4.

## 3. Non-goals (OUT)

- **No change to `signature()`.** Where the run stops is the tool's contract with every existing
  arm and every pin row's fourth field; moving it re-keys the pin file. This unit reports against
  the signature as it is.
- **No arming by prefix.** A prefix that arms would be the vacuous shape one step further: any
  fragment would satisfy the leg. STRANDED is a diagnosis printed beside a refusal that still
  refuses.
- **No detection of a prefix shorter than `STRAND_MIN`.** A line quoting fewer than 24 characters
  of a long message is indistinguishable from prose about it; the header states the bound.
- **No kit-version bump.** `KIT_MEMORY_TREE_VERSION` dates the hygiene engine in
  `check-memory-hygiene.sh`; `check-arms.py` carries no marker and `tools/memory-tree/kit.toml`'s
  `version_from` does not read it.
- **No re-arm of spec 22's two branches.** Their literals are spec 22's rev-2; this unit is why the
  next prefix is caught with its line number.

### Edges

- **consumes-from** external — `tools/memory-tree/check-arms.py`'s `signature()`, `classify()`,
  `armed_signatures()`, `cmd_report()`, `cmd_check()` and `cmd_selftest()` with its `arm()` helper
  and scratch-repo fixture, and `memory/gotchas/arm-literal-strands-on-message-edit.md` whose
  remedy this unit corrects.
- **hands-off** external — nothing. Unit 22's two full-signature literals are its own rev-2, copied
  from `signature()` run at the disposal rather than from a report row; at its order the report
  still prints truncated rows and its AC3 reads only the ARMED flag, so no sibling waits on this
  unit and it is ordered last for that reason.

## 4. Design

### The stranded read, inside `classify()`

```
for b in gb:
    b["armed"] = any(b["sig"] in l for l in lines)
    b["stranded"] = None
    if not b["armed"] and len(b["sig"]) >= STRAND_MIN:
        head = b["sig"][:STRAND_MIN]
        for no, l in numbered:            # (line number, text) for the same lines `armed_signatures` keeps
            if head in l and b["sig"] not in l:
                b["stranded"] = (test_rel, no)
                break
```

`armed_signatures()` returns a set of lines and drops their numbers; the pass either has it return
the numbered pairs and derives the set from them at the one call site, or reads the file once more
beside it. Either way the population of lines the stranded read walks is EXACTLY the one the armed
read walks — comments and `miss` lines excluded — so a comment quoting the message can no longer
be reported as a stranded arm than it can be counted as one. `STRAND_MIN = 24` sits beside
`NEGATIVE_RE` with the reason in its comment.

### The two outputs

`cmd_report()`'s row becomes
`check <num> branch <ord>  line <line>  ARMED|      <sig whole>[  STRANDED <test>:<line>]`, and
`cmd_check()`'s refusal appends
` — a STRANDED prefix at <test>:<line> stops short of the signature; copy the whole row --report prints`
to the existing sentence when `stranded` is set. The leg's verdict does not move: a stranded branch
was unarmed before and is unarmed after, with a better sentence.

### The selftest arms

Three `arm()` calls after the existing ones, over the same scratch repo: a `tools/gate-c.sh` whose
one branch message is 90 literal characters followed by `: $x`, and a `tools/gate-c.test.sh`
quoting its first 40 characters. `--check` names `STRANDED` with `tools/gate-c.test.sh:1`;
`--report` prints the same and its row holds the whole 90-character signature, asserted by
containment of the full string; the test rewritten to quote the whole signature reads ARMED and no
`STRANDED` token prints for that gate.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `STRAND_MIN` | module constant in `check-arms.py` | no cell; not a function |
| `stranded` | a key on the branch dict `classify()` builds | no cell; not a function |

No function, verb or file is minted.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/memory-tree/check-arms.py` | `STRAND_MIN`; the stranded read in `classify()`; the whole-signature row and `STRANDED` suffix in `cmd_report()`; the clause in `cmd_check()`; three selftest arms; the `signature()` docstring's remedy sentence |
| `memory/gotchas/arm-literal-strands-on-message-edit.md` | the remedy paragraph: the row is printed whole and a stranded prefix is named; anchors unchanged |

### Alternatives rejected

- **Drop the `[:72]` slice and nothing else.** Fixes the remedy and leaves the diagnosis where it
  was: the author still reads "no POSITIVE assertion" for a line that is there and one word short.
  The line number is the half that saves the next fold.
- **A spec-time pre-flight in the build harness** that asserts every `hit "$out" "<literal>"` a
  spec's §4 writes contains a `--report` row. The audit's left-shift. It needs the driver at the
  spec's order, which for spec 22 is a driver unit 16 has not built, and the check would pass
  vacuously on every spec that writes its arms in prose. The tool at authoring time is the same
  tool at close time; making it say more is the smaller diff.
- **Report a stranded prefix as ARMED with a warning.** Vacuous by construction; see §3.

## 5. Production-readiness checklist

- security — N/A; a report string and a selftest fixture.
- perf / scale — one substring scan per unarmed branch over the test file's lines, already in
  memory; the population of unarmed branches on this tree is the pin file's row count.
- error / empty / loading states — a signature shorter than `STRAND_MIN` takes no stranded read; a
  test file with no candidate line leaves `stranded` at `None` and the sentence unchanged.
- observability — the refusal and the report both name the test file and line.
- risks — a test line that quotes the opening of a message in a `same` label rather than a `hit`
  would be named STRANDED; the sentence says "copy the whole row", which is the right remedy for
  that line too, and the branch was unarmed either way.
- testing — §6; the three selftest arms and the report over the real tree.
- migration — additive; no pin row moves, no signature changes.
- user docs — the docstring and the gotcha's remedy.

## 6. Acceptance criteria

- **AC1** — When `python3 tools/memory-tree/check-arms.py --report` runs at the tip, no row
  truncates its signature: for every branch row, the text after the ARMED column equals the
  branch's full signature as `signature()` returns it, checked by a `python3 -c` that loads the
  module by path with `importlib`, runs `classify()` and compares each `sig` against the printed
  row; at this unit's base
  `grep -c '\[:72\]' tools/memory-tree/check-arms.py` prints 1 and at the tip 0.
  Red when: a row still truncates, which is the remedy that strands the arm it exists to fix.
  figure: the row count is DERIVED by the report at observation.
- **AC2** — When `python3 tools/memory-tree/check-arms.py --check` runs, by absolute path, with a
  scratch repo as its working directory — the tool roots itself at `git rev-parse --show-toplevel`
  — holding a gate whose message is 90 literal characters and a test quoting its first 40, the
  refusal for
  that branch carries `STRANDED prefix at tools/gate-c.test.sh:1` and `copy the whole row`; over
  the same repo with the test quoting the whole signature the branch is not named at all; at this
  unit's base the first run's refusal carries no `STRANDED` token.
  Red when: the prefix is not named, which is the class unchanged; or the whole-signature test is
  named STRANDED, which is a prefix read that fires on its own control.
  fixture: the selftest's scratch repo under a short `%TEMP%` path, made by `cmd_selftest()`'s own
  `tempfile.TemporaryDirectory()`; never this worktree.
- **AC3** — When `python3 tools/memory-tree/check-arms.py --selftest` runs at the tip, its output
  carries three more `arm ok` lines than at this unit's base, their labels naming the stranded
  prefix, the whole-signature control and the untruncated report row, and it ends `PASS —
  check-arms: all arms held`; with the `[:72]` slice restored in a copy of the file the report-row
  arm prints `arm FAIL`.
  Red when: an arm fails, or the count did not move, which is a selftest that covers nothing new.
  figure: the `arm ok` count is DERIVED by `grep -c '^arm ok'` over the output at base and tip.
- **AC4** — When `grep -c 'copy the row it prints' tools/memory-tree/check-arms.py` runs at the tip
  it prints 0 and `grep -c 'STRANDED' memory/gotchas/arm-literal-strands-on-message-edit.md` prints
  at least 1; `python tools/memory-tree/gotchas.py --check` exits 0 at the tip.
  Red when: the docstring or the gotcha still tells the author to copy a row that was truncated,
  which is the remedy this unit exists to correct; or the gotcha's edit broke its anchors or its
  `gated by` sentence, which the memory hygiene leg reds at the close.

## 7. Gates

`check-arms selftest` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the `python3 -c` compare
of AC1, the two scratch-repo `--check` runs of AC2, the `--selftest` run and its counted output of
AC3, and the greps of AC4. Under `harness arms`, no branch's verdict moves; under `check-arms
selftest`, the three arms are the count this unit adds.

New arm: `tools/memory-tree/check-arms.py` · `cmd_selftest()`'s scratch gate with a 90-character message and a 40-character test literal, and the same test quoting the signature whole · no floor; the selftest counts no assertions

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 4 as the
  promotion of H1 (raw ids 12, 22, 33): the full-signature literals are spec 22's rev-2 fold, and
  the tool naming a stranded prefix, with its report row printed whole, is this unit. The `[:72]`
  truncation is this disposal's own reading of `cmd_report()`, not a report id.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "report a test assertion whose literal is a prefix of a
fail branch signature as stranded rather than absent"` ranked `report` in
`tools/drift-audit/selftest.py`, `render_report` in `tools/codebase-map/rank_harness.py` and
`branches` in `tools/memory-tree/check-arms.py`, and reported `unscanned layers: .sh`; the seam is
the last of those, read at source: `classify()` at `:220` to `:238`, which already walks the test
lines `armed_signatures()` keeps and is the one place a per-branch fact is derived; `cmd_report()`
at `:300` and `cmd_check()` at `:241`, which print it; and `cmd_selftest()`'s `arm()` and scratch
repo at `:341` to `:380`, which the three new arms join. The recall probe returned
`TOOL-dUnstalledConvoy-19` (the tool's blindness to reachability, a different class), the
aRatifiedRulings-1 spec (a message change alone turned the leg red because two arms quoted a
strict prefix of the new signature — the same class, one build earlier), `TOOL-aDeferredBar-13`
(pins keyed by ordinal, which is why this unit re-keys nothing) and the aHoistedPass-2 ledger ("an
arm must carry the WHOLE signature, not a prefix"); every hit records the instance and none the
diagnosis, and the `[:72]` row is named nowhere.

Recall terms used: `check-arms signature prefix stranded unarmed branch report arm literal interpolation gotcha harness arms`
