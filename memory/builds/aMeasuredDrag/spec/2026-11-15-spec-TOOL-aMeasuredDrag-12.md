# TOOL-aMeasuredDrag-12 — the closing review's six minor items: an absolute-only launcher memo, and the arms and floor that make units 4, 10 and 11 fail when undone

**Status:** CLOSED · rev-1 · 2026-11-15 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aMeasuredDrag-12-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-12-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-12-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-12-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-12-2-builder.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-12-2-builder.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-12-promotion-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-12-promotion-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 closing review of this build (`2026-11-15-review-TOOL-aMeasuredDrag-1-11-closing-diff-round1`)
confirmed six minor items, which BUILD-METHOD M4 batches into this one unit. One is a narrow spurious
red: a relative launcher can enter the bar's memo. The other five are verification gaps that leave
units 4, 10 and 11 able to regress with every gate green. Each fix is the one the review's skeptic
judged sound or class-level, and no verdict, refusal or printed line moves for a correct input.

## 2. Scope (IN)

| brief item | review item | finding | scope items |
|---|---|---|---|
| 1 | 2 | 1 | S1 S2 S3 S4 S6 S8 |
| 2 | 1 | 2, 6 | S5 |
| 3 | 3 | 3 | S9 |
| 4 | 4 | 4 | S10 |
| 5 | 5 | 5 | S11 |
| 6 | 6 | 7 | S7 |

- **S1** — The runner's export. `tools/run-gates/run-gates.sh` exports `GATE_RESOLVED_PY` only when
  `PYBIN` is absolute: it begins with `/`, or with a drive letter, a colon and `/` or `\`. Any
  other `PYBIN` exports nothing, so every leg probes as it did before TOOL-aMeasuredDrag-11.
  Observed by AC1.
- **S2** — The resolver block. `tools/lib/resolve-python.sh#resolve_python` admits a memo only when
  its line 2 is absolute under the S1 predicate. A memo carrying a relative or bare-name launcher is
  a miss, from any producer. Observed by AC2.
- **S3** — The copies. Every inline copy of the block is re-synced byte-identically, over the
  population TOOL-aMeasuredDrag-11 S2 derives. Observed by AC3.
- **S4** — The help page. `help/python-floor.md` adds the absolute-launcher condition to the
  memo paragraph. Observed by AC6.
- **S5** — Arm 1m in `tools/run-gates/run-gates.test.sh` tells a memo hit from a re-probe with a
  counting wrapper, and proves the counter can move. NOT OBSERVED by a pass criterion: the arm's
  RED and GREEN are the main loop's at the close (M8), and the pass runs no suite.
- **S6** — Arm 1m2 in `tools/run-gates/run-gates.test.sh` drives the runner's export statement
  over an absolute, a drive-letter, a relative and a bare-name `PYBIN`. Observed by AC1.
- **S7** — Arm 1m3 in `tools/run-gates/run-gates.test.sh` holds the ordering half of
  TOOL-aMeasuredDrag-11's AC5: the unset, the resolution, the digest and the export appear in that
  order. Arm 1m's header stops naming that order as unchecked. Observed by AC4.
- **S8** — The resolver suite. `tools/lib/resolve-python.test.sh` arm (e2) refuses a relative and a
  bare-name memo launcher. Observed by AC2.
- **S9** — The floor. `FLOOR_ASSERTIONS` in `tools/run-gates/run-gates.test.sh` rises by arm 1m's
  two existing assertions and the four this unit adds, with a dated ledger line. Observed by AC5.
- **S10** — The tag switch. The instructions-edit fixture's tag arm, in
  `tools/playbook/instructions_edit.py`, pins both sides of the `tags` switch of `check_tree`: a
  write is refused naming the `unit.old` citation, and `run_check` does not name it.
  NOT OBSERVED by a pass criterion: the main loop observes it RED and GREEN at the close (M8).
- **S11** — The template trigger. `.githooks/pre-commit.test.sh` gains an arm that goes red when the
  `st_template` trigger TOOL-aMeasuredDrag-10 wrote breaks, with a control. NOT OBSERVED by a pass
  criterion: the main loop observes it RED and GREEN at the close (M8).

## 3. Non-goals (OUT)

- Editing TOOL-aMeasuredDrag-11's spec. It is CLOSED and frozen, so the review's §7 correction is
  recorded in §4 of this spec instead.
- Absolutizing a relative or bare-name launcher before export, which the review's fix offered. The
  brief rules that such a launcher is never exported.
- The review's left-shift gates: the spawn-counter rule for every memo arm, a floor-movement check in
  `testsuite counts (every bar self-test prints one)`, one arm per mode switch, a hook case-arm
  inventory in `.githooks/pre-commit.test.sh`, and the "covered by" claim checker. Each is a
  separate mechanism and a follow-up ask.
- Exporting from any other runner, and any change to the candidate order, the floor, the probe or the
  refusal text.
- Any change beyond the six items, any other unit's spec, and any self-test suite or the bar inside
  the pass.

### Edges

- **consumes-from** external — TOOL-aMeasuredDrag-11's memo, export and arm 1m, CLOSED on this run
  branch; this unit hardens them and fails to apply without them.
- **consumes-from** external — TOOL-aMeasuredDrag-4's `tags` switch and TOOL-aMeasuredDrag-10's
  `st_template` trigger, both CLOSED; S10 and S11 test them as built.

## 4. Design

### Evidence

Read at the run branch's HEAD `9b977f4d1`, blob-pinned. The base `aebbb4a72` predates units 4, 10
and 11, so every cited line is from the run branch.

- `tools/run-gates/run-gates.sh@33b623a2:352-353` unsets `GATE_RESOLVED_PY` and resolves `PYBIN`.
  `:3566` closes the toolchain digest. `:3571` derives `PY_MM` from `PY_ID`, and `:3572` exports
  the four-line memo unconditionally, whatever `PYBIN` looks like.
- `tools/lib/resolve-python.sh@522ccfe2:40` is the memo pattern. Its line-2 group is `([^\n]+)`, so
  any non-empty launcher is admitted. `:41-46` echoes `BASH_REMATCH[3]` on a hit. `:66` echoes an
  override as given, so a relative `GOV_PYTHON` becomes a relative `PYBIN`.
- `tools/run-gates/run-gates.sh@33b623a2:106` changes into the repository root before `:353`
  resolves, and `:4774` changes into a leg's own directory before the leg runs. A relative `PYBIN`
  therefore resolves at the root and goes dead in a leg that runs elsewhere, as the review records.
- On node a on 2026-11-15, `resolve_python` printed
  `C:/Users/daily-agent/AppData/Local/Python/pythoncore-3.15-64/python.exe` with `GOV_PYTHON` unset
  (PINNED). The common case is a drive-letter path, so S1 keeps the TOOL-aMeasuredDrag-11 saving.
- `tools/run-gates/run-gates.test.sh@e33c90b2:541-571` is arm 1m. Its two assertions compare the
  leg's launcher with memo line 2, and both are derived from `PYBIN`, so a re-probe passes them.
  Its header at `:546-547` says the export-after-digest order is not checked. `:289` holds
  `FLOOR_ASSERTIONS=450`, and the ledger's last line above it is TOOL-aNimbleMend-15's 440 -> 450.
  `:259` resolves the suite's own `PYBIN`.
- `tools/lib/resolve-python.test.sh@4bc5ec76:110-131` is arm (e2). Its loop at `:128-131` already
  feeds memos that must miss and asserts the launcher printed is not `/no/such/py`. The suite has no
  assertion floor.
- `tools/playbook/instructions_edit.py@7638c707:300` calls `check_tree(root, {rel: candidate.text})`
  on the write path, relying on the default. `:502` declares `tags=True`, `:528-532` runs
  `run_tag_check` under it, and `:539` is `run_check`, which passes `tags=False`. The fixture arm
  `arm_retired_rows` at `:1040-1064` commits `memory/guides/ALPHA.md` citing the retired
  `unit.old` and asserts that `run_tag_check` names `new text cites retired unit.old`. It never
  reaches that red through `check_tree`, the write path or `run_check`. `run_cli` at `:550-555`
  returns a verb's exit and its printed text.
- `.githooks/pre-commit@f1da4472:203` sets `st_template` from the staged list, and `:307-313` runs
  `check-template-size.sh` found by `resolve_kit_gate "" check-template-size.sh`. `:174-180` finds a
  gate at the repository root before `GOV_KITROOT`.
- `.githooks/pre-commit.test.sh@069c2dc0:171-190` is the wiring arm. It plants a stand-in adopter
  that prints a marker, commits an unrelated file and then the trigger file, and asserts one marker.
  No arm stages `coding-governance-agents.template.md`. The suite has no assertion floor.
- `help/python-floor.md@85f4839e:20-24` lists the memo's three conditions and not the launcher's form.

### Mechanism

- **The export (S1).** The unconditional export at `:3572` becomes a column-0 `case` on `PYBIN`
  whose one arm, for `/*` and a drive letter followed by `:/` or `:\`, holds the unchanged
  export line. No other arm is written: the unset at `:352` already clears an inherited value. The
  `case` opens on the line after `PY_MM=""` and closes on a column-0 `esac`, the shape AC1 extracts.
- **The block (S2).** The line-2 group of `_rp_re` becomes an alternation inside the same group: a
  `/` followed by any non-newline run, or a letter, a colon, `/` or `\`, and any non-newline run. No
  group is added, so the `BASH_REMATCH` indices at `:42-44` do not move. The comment above the
  pattern gains one sentence: only an absolute launcher is admitted, because a relative one names
  another file once a leg changes directory, and a bare name does too under a `PATH` holding `.`.
- **The copies (S3).** The text between the two resolver markers in every file that
  `git grep -l '^# >>> resolve_python' -- '*.sh' '*.py' '.githooks/*' WIRE-INTO-PROJECT.md` names is
  rewritten from the canonical in one scripted pass, in the same commit, as TOOL-aMeasuredDrag-11 S2
  did. The population was 80 files at `9b977f4d1` (PINNED).
- **Arm 1m (S5).** The arm builds a counting wrapper in its scratch directory: a bash script that
  appends one line to the file named by `RG1M_COUNT` when that variable is set, then execs the
  absolute executable the suite's `PYBIN` reports. The scratch bar runs with `GOV_PYTHON` set to the
  wrapper, and the sentinel memo carries the wrapper as its override field. The runner therefore
  resolves `PYBIN` to the wrapper, an absolute path. `leg.sh` exports `RG1M_COUNT` naming a hit
  counter, calls `resolve_python` with the memo it inherited, then calls it again with
  `GATE_RESOLVED_PY` unset and `RG1M_COUNT` naming a miss counter. The arm keeps its two assertions
  and adds two: the hit counter is absent or empty, and the miss counter is not empty. The second is
  the control that proves the counter moves, so an empty hit counter is evidence and not a dead probe.
- **Arm 1m2 (S6).** The arm extracts the runner's lines from `PY_MM=""` through the next column-0
  `esac` with `sed`, and sources them in a child shell five times with `PY_ID` set and `PYBIN` set
  to `/abs/py`, `C:/abs/py`, `C:\abs\py`, `rel/py` and `py`. One assertion: the first three export a
  memo whose line 2 is that `PYBIN`, and the last two leave `GATE_RESOLVED_PY` unset. The three
  absolute cases are the control: an empty extraction exports nothing and fails them. It drives no
  bar, so it costs milliseconds.
- **Arm 1m3 (S7).** The arm runs the AC4 grep over `$KITDIR/run-gates.sh`. One assertion: exactly
  four lines, in the order unset, `PYBIN`, digest, export. Arm 1m's header names arm 1m3 where it
  now says the order is the spec's grep.
- **The floor (S9).** `FLOOR_ASSERTIONS` moves from 450 to 456. That is arm 1m's two existing
  assertions, which TOOL-aMeasuredDrag-11 left uncounted, plus arm 1m's two new ones, arm 1m2's one
  and arm 1m3's one. None sits behind `HAVE_TIMEOUT`. A ledger line above it reads
  `450 -> 456, TOOL-aMeasuredDrag-12: arm 1m's four, arm 1m2's one and arm 1m3's one, none gated.
  Counted off the arms; this pass runs no suite.`
- **Arm (e2) (S8).** The arm's miss loop gains two memos, each matching `GOV_PYTHON` and `PATH` at
  the floor: one whose line 2 is `no/such/py` and one whose line 2 is `nosuchpy`. Each must print a
  launcher other than its memo's line 2. The header says what the two stage: a block whose line-2
  group admits any launcher.
- **The tag arm (S10).** In `arm_retired_rows`, after the existing `run_tag_check` check and over the
  same tree, two checks are added. An `add` through `run_cli`, with the fixture's record arguments
  and a fresh tag, exits 1 and its text names `cites retired unit.old`. This reaches `check_tree`
  through the write path at `:300` and its default. Then `run_check(root)` returns lines that do not
  name `cites retired`. Each half stages red alone: the default flipped to `tags=False` reds the
  first, and `run_check` passing `tags=True` reds the second.
- **The template arm (S11).** A section after the wiring arm builds a scratch repository on the same
  pattern. It plants a stand-in `check-template-size.sh` at the root that prints
  `TEMPLATE-SIZE RAN`, commits an unrelated file, then stages and commits
  `coding-governance-agents.template.md`. Two `ck` assertions: the template commit prints the marker
  and exits 0, and the marker appears exactly once across both commits.

### Correction of TOOL-aMeasuredDrag-11's §7

TOOL-aMeasuredDrag-11's §7 says its `run-gates.test.sh` arm covers AC5. That arm discharges only
AC5's unset half. From this unit, arm 1m3 discharges the ordering half. The CLOSED spec stays as
written, per M4, and this section is the record of the correction.

### Data model

The memo's four-line layout is unchanged. Line 2 narrows from any non-empty run to an absolute path.

### Inventory

One name is minted: `RG1M_COUNT`, an environment variable local to arm 1m's fixture. Only the arm's
wrapper reads it, and only the arm's `leg.sh` sets it. The suite labels `1m2` and `1m3` follow the
suite's existing letter-digit labels, such as `9e2` and `14a2`. `git grep -n RG1M_COUNT` returns no
hit at `9b977f4d1`.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.test.sh`
- `tools/lib/resolve-python.sh`
- `tools/lib/resolve-python.test.sh`
- `tools/playbook/instructions_edit.py`
- `.githooks/pre-commit.test.sh`
- `help/python-floor.md`

The inline copies of S3 are added to this unit's `--dispatch --writes` from the same `git grep`.

### Rollout

Live at landing, with no switch. For an absolute `PYBIN`, the common case, the memo, the hit and
every printed line are as TOOL-aMeasuredDrag-11 left them. For a non-absolute one, legs probe as
they did before unit 11. It builds at order 12, after every other unit of the build is terminal.

### Migration

None in this repository. At an adopter, a new block beside an old runner refuses a relative memo,
and an old block beside a new runner never receives one.

### Alternatives rejected

- **Absolutize at export** (the review's sketch). It adds a `cd` and `type -P` to the runner and
  still needs the block-side check against other producers. The brief rules that a non-absolute
  launcher is never exported.
- **Export-side check alone.** That cures this producer only. The block-side check makes every
  producer's non-absolute memo a miss, which is the class the skeptic named.
- **Truncate a shared counter in `leg.sh`** (the skeptic's literal wording). Any python the runner
  spawns between the truncation and the read would count. Here the leg names the counter, so only
  its own calls count.
- **The order arm in `run-gates.gov.test.sh`.** That suite holds facts true only in this
  repository. The runner and its line order ship to adopters, so arm 1m3 belongs in the kit's suite.
- **A second scratch bar for the relative case.** It would cost a whole bar run. Arm 1m2 sources
  the export statement itself in milliseconds.

## 5. Production-readiness checklist

- security: narrower than before. A memo now carries only an absolute launcher, so a value a leg
  inherits cannot name a different file after the leg changes directory.
- perf / scale: unchanged for an absolute `PYBIN`. Arm 1m adds one miss probe, about 176 ms by
  TOOL-aMeasuredDrag-11's figure (PINNED there), and arms 1m2 and 1m3 cost milliseconds. No bar run
  is added. The `run-gates canary` ceiling in `tools/gate-legs.json` is unchanged.
- error / empty / loading states: a non-absolute memo is a miss, and a miss prints nothing, so the
  refusal text and its order are unchanged.
- observability: none added.
- risks: a launcher spelled `//server/share/py` passes the predicate, and it is absolute. A drive
  letter followed by no separator, such as `C:py`, is drive-relative and is refused.
- testing: the six arms under §7, plus AC1 to AC6 as pass probes.
- migration: N/A — no data or format moves; the Migration sub-head covers adopter mixes.
- user docs: `help/python-floor.md`, S4.

## 6. Acceptance criteria

- **AC1** — When `sed -n '/^PY_MM=""/,/^esac/p' tools/run-gates/run-gates.sh` is written to scratch
  and sourced by `bash -c` with `PY_ID='3.15.0'` and `PYBIN` set in turn to `/abs/py`, `C:/abs/py`,
  `C:\abs\py`, `rel/py` and `py`, the first three print a `GATE_RESOLVED_PY` whose line 2 is that
  `PYBIN`, and the last two leave it unset.
  Red when: the export is unconditional, so `rel/py` is exported, or the predicate refuses a
  drive-letter path, so the common Windows case loses its memo.
- **AC2** — When `GATE_RESOLVED_PY="$(cat tools/lib/python-floor.txt)"$'\nno/such/py\n'"${GOV_PYTHON:-}"$'\n'"$PATH" bash -c '. "$1"; resolve_python' _ tools/lib/resolve-python.sh`
  runs, its stdout, stderr and exit status equal those of the same command with `GATE_RESOLVED_PY`
  unset, compared with `cmp`. The same holds with line 2 `nosuchpy`. With line 2 `/no/such/py` and
  then `C:/no/such/py`, it prints that line, writes nothing to stderr and exits 0.
  Red when: the block still admits a relative or bare-name launcher, or its predicate refuses an
  absolute one.
- **AC3** — When every file the S3 `git grep` names has the text between its two resolver markers
  compared with the canonical's by `sed -n '/^# >>> resolve_python/,/^# <<< resolve_python/p'` and
  `cmp`, no file differs; and `python tools/lib/python_floor.py check` exits 0.
  Red when: one inline copy was not re-synced.
- **AC4** — When `grep -nE '^unset GATE_RESOLVED_PY|^PYBIN=\$\(resolve_python\)|^\) && REUSE_DIGEST=|^[^#]*export GATE_RESOLVED_PY' tools/run-gates/run-gates.sh`
  runs, it prints exactly four lines, in the order unset, `PYBIN`, digest, export.
  Red when: the export precedes the digest, or the S1 `case` hides the export from the pattern.
- **AC5** — When `grep -n -B3 '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.test.sh` runs, it prints
  `FLOOR_ASSERTIONS=456` and, above it, the ledger line opening `450 -> 456, TOOL-aMeasuredDrag-12`.
  Red when: the floor stays below the arms it guards.
  figure: 456 is DERIVED: 450 plus the `n=$((n+1))` lines in arms 1m, 1m2 and 1m3, counted off the
  built arms at observation.
- **AC6** — When `grep -n 'absolute' help/python-floor.md` runs, it prints the memo paragraph's
  sentence saying the runner hands on only an absolute launcher.
  Red when: the page still lists three conditions.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `run-gates canary` · `branch-guard self-test` · `instruction edits selftest` · `instruction edits (manifest checks)` · `playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `pre-push self-test` · `measure-legs selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/lib/resolve-python.test.sh · covers AC2 · the line-2 group of `_rp_re` restored to any non-empty run admits `no/such/py` · none
New arm: tools/run-gates/run-gates.test.sh · covers none · arm 1m, staged by swapping the GOV_PYTHON and PATH fields of the export, or by replacing `PY_MM` with an empty string, so the hit counter fills · FLOOR_ASSERTIONS 450 -> 456, shared with the next two
New arm: tools/run-gates/run-gates.test.sh · covers AC1 · arm 1m2, staged by dropping the `case` so the export is unconditional · the same floor
New arm: tools/run-gates/run-gates.test.sh · covers AC4 · arm 1m3, staged by moving the export above the digest · the same floor
New arm: tools/playbook/instructions_edit.py · covers none · the tag arm in `arm_retired_rows`, staged by flipping the `check_tree` default to `tags=False` for the write half and by passing `tags=True` from `run_check` for the check half · none
New arm: .githooks/pre-commit.test.sh · covers none · the template arm, staged by misspelling the `st_template` case pattern · none

The pass legs run after the unit's commit, and the close runs the bar once.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.

## 10. Reuse audit

Each fix edits the function the review cites, in place. The seam for S1 to S3 is
`tools/lib/resolve-python.sh#resolve_python`: `reuse_lookup.py` ranks `resolve_python` a SEAM with 81
installs (PINNED at `9b977f4d1`). The runner's export at `tools/run-gates/run-gates.sh@33b623a2:3572`
is the producer it narrows. The copy re-sync follows TOOL-aMeasuredDrag-11 S2 and
TOOL-dSafePassage-23 S4. The arms extend existing arms in place: arm 1m, arm (e2),
`arm_retired_rows`, and the wiring arm's fixture pattern in `.githooks/pre-commit.test.sh`. The reuse
probe was `python tools/codebase-map/reuse_lookup.py "admit only an absolute launcher into the bar's resolved python memo"`.
Recall returned the closing review record, which states the counting-wrapper fix, and
TOOL-aSparedSpawn-11, whose §7 stages an arm with a logging stub on `PATH`, the same counting idiom.
The dispatch's recall named TOOL-dDerivedDocket-61 and TOOL-aBriskPreflight-9, and its asks probe
named TOOL-aTrimmedHook-8 for unit 10's trigger. None of them offers a seam this unit does not
already extend.

Recall terms used: `python tools/memory-recall/query.py "how is a memo or cache arm proven to skip the work, and how is a hook trigger arm tested" --terms "memo cache skipped spawn counter wrapper trigger arm pre-commit staged floor assertions absolute launcher"`
