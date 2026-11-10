# TOOL-aSmoothedDispatch-9 — the three driver-suite arms unit 1's split left red: the stale `--dispatch` hostile-value exemption, and two carriage-return arms whose byte the substitution drops

**Status:** CLOSED · rev-2 · 2026-11-10 · node a · Tier-1 · base ae6735c1 · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-build-TOOL-aSmoothedDispatch-1-1-acceptance-ledger.md](../build/2026-11-10-build-TOOL-aSmoothedDispatch-1-1-acceptance-ledger.md) | journal | TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-5 TOOL-aSmoothedDispatch-6 TOOL-aSmoothedDispatch-7 TOOL-aSmoothedDispatch-8 |
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-9-1-spec-writer.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-9-1-spec-writer.md) | journal | — |
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-9-diverged.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-9-diverged.md) | research | — |
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-9-stale-arms.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-9-stale-arms.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The close ran driver-suite shards 2 and 4 at the tip `55d65f5c` and at the base `ae6735c1`. Three FAIL
lines appear only at the tip, and all three are suite arms that unit 1's `--writes` split left
stale or unreachable. This unit corrects the suite, so each shard's FAIL lines equal the base's. No
product code changes, because each refusal already behaves as the CLOSED specs of units 1 and 8 say.

## 2. Scope (IN)

- **S1** — Shard 2. The `_rf_exempt` list in `tools/unattended/unattended.test.sh` drops its
  `dispatch|check 49: ...` row, so the hostile-value matrix grades `--dispatch` like every other
  verb. The `brief` row stays. Observed by AC1.
  **Readers:**
  by name: `tools/unattended/unattended.test.sh` spells `_rf_exempt` and the row, at `:4522-4524`;
  no other tracked file outside the build records spells the row, by a git grep at writing.
  by value: `tools/unattended/unattended.test.sh` reads the row's verb through `_rf_exempt_verbs`,
  in the stale-exemption test at `:4533` and in the second loop at `:4537`, which counts one
  assertion per listed verb.
- **S2** — Shard 4. The two carriage-return `--writes` arms carry their value in a variable, set
  outside the `$(run ...)` substitution, with a comment saying why. Their asserted texts and the
  `TOOL-aSmoothedDispatch-8 AC5` marker stay as they are. Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- No change to `tools/unattended/unattended.sh`. The split, the whitespace refusal and its comment
  stay as unit 1 shipped them.
- No vertical-tab arm. The brief asked for one, and §7 F1 records why the carriage return stays.
- No fix for the reds the base run shares: `--record-round` missing from the hostile matrix, the
  `GATE_REGEN_CHECK` scrub pair, the `write_bar_green` prologue check, and the five check-118 fixture
  refusals in shard 4.
- No floor moves. S1 lowers shard 2's executed count by one, and S2 leaves shard 4's count as it is.
- No edit to a CLOSED spec of this build. The literal `spells\r·\rseparator.sh` and the
  `TOOL-aSmoothedDispatch-8 AC5` marker stay in the file, so unit 8's AC5 greps still count 1 and 4.
- No gotcha record for "a `$'\r'` spelled inside a command substitution loses the byte on this
  node". The suite states it in two comments (`tools/unattended/unattended.test.sh:4445`, `:4542`)
  and `memory/gotchas/` holds no record for it. Writing one is a separate document, so it is a
  follow-up for the main loop's left-shift at the close (BUILD-METHOD M8).

## 4. Design

### What the tree holds, read at `c13b0b63`

| Fact | Where |
|---|---|
| `_rf_exempt` has two rows, `brief` and `dispatch`. The `dispatch` row says the form "carries a space". | `tools/unattended/unattended.test.sh:4522-4523` |
| The matrix reds a listed verb that accepted the one-line form, and adds one assertion per listed verb in a second loop. | `tools/unattended/unattended.test.sh:4525-4540` |
| The matrix drives `--dispatch` as `run --dispatch tRun --pass ARCH-tRun-1 --writes "$2"`. | `tools/unattended/unattended.test.sh:4418` |
| The `--writes` loop splits each value on space, tab and newline only. | `tools/unattended/unattended.sh:15197` |
| The whitespace refusal is `*[[:space:]]*` on each split path. | `tools/unattended/unattended.sh:14610-14612` |
| The two carriage-return arms spell `$'...\r...'` inside `hit "$(run ...)"`. | `tools/unattended/unattended.test.sh:9202`, `:9212` |
| The suite already carries carriage-return values in variables, because a `$'\r'` spelled inside a command substitution loses the byte on this node. | `tools/unattended/unattended.test.sh:4442-4445`, `:4541-4547` |
| Both arms sit in shard 4, the matrix in shard 2. | `if in_shard 4` at `:7768`, `if in_shard 2` at `:3491` |
| A shard reds when its executed count falls below its floor. | `tools/unattended/unattended.test.sh:19509-19513` |
| `FLOOR_SHARD_2` is 229 and `FLOOR_SHARD_4` is 390. | `tools/unattended/unattended.test.sh:19432`, `:19452` |

The close's logs give the tip counts: shard 2 executed 611 assertions and shard 4 executed 608. The
figures are PINNED from those runs at `55d65f5c`.

### S1 — the exemption row

Delete the `dispatch|check 49: ...` line at `:4523`, and move the closing quote of the `_rf_exempt`
string onto the `brief` line. Since unit 1, the one-line form `yes\nphase: LANDED` splits on its
space into two paths, and `--dispatch` declares them with exit 0. The matrix's phase-line and
carriage-return checks for `--dispatch` stay green, so the acceptance stores nothing forged.

The second loop iterates once less, so shard 2 executes 610 assertions at the tip, far above its
floor of 229.

### S2 — the carriage-return arms

The brief diagnosed the red as `case` matching a carriage return inconsistently. The probe below
measures otherwise. A `$'two\rwords/x.sh'` spelled inside the `$(run ...)` substitution reaches the
verb as "twowords/x.sh", every time. That value carries no whitespace, so the dispatch is declared,
which matches the shard 4 log's "dispatch declared". The same byte carried in a variable reaches
`*[[:space:]]*` every time and matches.

So the fix follows the suite's own idiom at `:4542`. Directly above the arm at `:9202`, add:

```bash
# The carriage returns ride variables: spelled as `$'\r'` inside the `$(run ...)` substitution, this
# node's bash drops the byte, and the verb would declare `twowords/x.sh` (TOOL-aSmoothedDispatch-9).
_cr_sep=$'spells\r·\rseparator.sh'; _cr_two=$'two\rwords/x.sh'
```

The arm at `:9202` passes `--writes "$_cr_sep"` and the arm at `:9212` passes `--writes "$_cr_two"`.
Each keeps its asserted text and its trailing comment. Both lines are at shard 4's top level, so
`_cr_two` is still set at `:9212`. Each arm line gains the marker `# TOOL-aSmoothedDispatch-9 AC3`.
The existing marker on `:9202` stays first on its comment.

The staged break is the one unit 8's spec S5 names: the split's IFS widened to `$' \t\n\r'`. Each
value then splits into paths that carry no whitespace, and neither arm meets the refusal.

### The pass probe, `$SCRATCH/sd9.sh`

`$SCRATCH` is the run's scratch directory. Every IFS value rides a variable, for the reason S2
fixes. This spec's author ran it three times at `c13b0b63`, on `GNU bash 5.3.9(1)-release
(x86_64-pc-cygwin)`.

```bash
set -u
ws() { case "$1" in *[[:space:]]*) echo WS ;; *) echo NOWS ;; esac; }
split() { local a=(); IFS=$2 read -r -d '' -a a <<<"$1" || :; echo "${#a[@]}"; }
v_two=$'two\rwords/x.sh'; v_sep=$'spells\r·\rseparator.sh'; ifs_ship=$' \t\n'; ifs_staged=$' \t\n\r'
echo "literal-in-substitution two=$(ws $'two\rwords/x.sh')"
echo "literal-in-substitution sep=$(ws $'spells\r·\rseparator.sh')"
echo "variable-in-substitution two=$(ws "$v_two") sep=$(ws "$v_sep")"
echo "shipped-split two=$(split "$v_two" "$ifs_ship") sep=$(split "$v_sep" "$ifs_ship")"
echo "staged-split two=$(split "$v_two" "$ifs_staged") sep=$(split "$v_sep" "$ifs_staged")"
```

It printed these lines on each of the three runs:

```
literal-in-substitution two=NOWS
literal-in-substitution sep=NOWS
variable-in-substitution two=WS sep=WS
shipped-split two=1 sep=1
staged-split two=2 sep=3
```

Two `$'...\r...'` literals inside substitutions on ONE line made bash refuse the script with
"unexpected EOF while looking for matching `)'", so the probe spells them on separate lines.

### The builder's own checks

The builder runs no suite. It runs `bash -n` over the edited suite, the probe above, and the greps
of AC1 and AC2. Each moved arm's RED and GREEN observation belongs to the main loop at the close.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`

### Rollout

One pass, after units 1 to 8, all CLOSED. The suite is shipped bytes of the unattended kit, so
`kit epoch` wants that kit's version moved. The lander's `mint` moves it, never a hand edit.

### Alternatives rejected

- **A vertical tab in both arms, as the brief asks.** The probe shows the `case` matches a carriage
  return every time once the byte arrives, so the brief's reason does not hold. A `\v` arm would
  also stop pinning the byte units 1 and 8 named, which is the class
  `memory/gotchas/staged-break-substitutes-a-synthetic-value.md` describes.
- **Raise or lower a floor.** Floors are minimums, and shard 2's count stays far above 229.

## 5. Acceptance criteria

- **AC1** — When `grep -c "^_rf_exempt='brief|check 49: .*hash'\$" tools/unattended/unattended.test.sh`
  runs, it prints 1, so the `_rf_exempt` string opens and closes on the `brief` row.
  `grep -c '^dispatch|check 49' tools/unattended/unattended.test.sh` prints 0. Both greps print the
  reverse, 0 and 1, at `6b636484`, and 1 and 0 on a scratch copy with S1 applied. At the close,
  shard 2 prints no `FAIL the exemption for --dispatch is stale` line, and its FAIL lines equal the
  base run's, the `--record-round` line alone.
  Red when: the `dispatch` row is put back on `_rf_exempt`, so the matrix reads exit 0 for a listed
  verb and prints the stale-exemption FAIL.
  figure: shard 2's count of 610 is DERIVED from the close's 611 at `55d65f5c`, less the one
  iteration of the second loop.
- **AC2** — When `grep -cF -- "--writes \$'" tools/unattended/unattended.test.sh` runs, it prints 0,
  and `grep -cF "spells\r·\rseparator.sh" tools/unattended/unattended.test.sh` prints 1. When
  `bash "$SCRATCH/sd9.sh"` runs, it prints the five lines in §4 exactly.
  Red when: an arm still spells its carriage return inside the substitution, so the first grep
  prints 1 or 2, or the probe's `variable-in-substitution` line reads `NOWS`.
- **AC3** — When `grep -c 'TOOL-aSmoothedDispatch-9 AC3' tools/unattended/unattended.test.sh` runs,
  it prints 2. At the close, shard 4 prints neither `missing: --dispatch was given a --writes path
  containing whitespace` line, and its FAIL lines equal the base run's. Both arms read RED with the
  split's IFS at `tools/unattended/unattended.sh:15197` widened to `$' \t\n\r'`, and GREEN once
  restored.
  Red when: the byte is lost before the verb, so "twowords/x.sh" is declared, or the split covers
  the carriage return.

## 6. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/unattended/unattended.test.sh · covers AC1 · the `dispatch` row put back on `_rf_exempt`, so shard 2 prints the stale-exemption FAIL · none
New arm: tools/unattended/unattended.test.sh · covers AC3 · the two carriage-return arms of region four, red with the split's IFS widened to `$' \t\n\r'` · none

The driver suite is no leg of the manifest. It runs as the shard rows of
`tools/run-gates/selftest-budgets.txt`, so its arms are declared above and not on the leg line. The
one path under Files touched trips only broad guards. The main loop re-runs shards 2 and 4, observes
each arm RED and then GREEN, and runs the bar once, at the close. This spec's author ran no gate but
the spec-token checker's one-spec mode over this file.

## 7. Open questions

- **FACT-QUESTION · F1 — Does the shard 4 red come from `case` missing a carriage return, as the
  brief says, or from the byte never reaching the verb?** The brief's answer moves both arms to a
  vertical tab. The other answer keeps the carriage return and carries it in a variable. Probe:
  `$SCRATCH/sd9.sh` in §4. Observation: the `literal-in-substitution` lines against the
  `variable-in-substitution` line. Liveness: the probe printed `NOWS` on its literal lines, so it
  can produce a negative. Recommendation: the variable, if the literal lines read `NOWS` while the
  variable line reads `WS`. RESOLVED (agent, 2026-11-10): the byte never reaches the verb. Three
  runs printed `NOWS` for both literals and `WS` for both variables, so the arms carry the carriage
  return in a variable, per S2.

## 8. Revision log

- rev-1 · 2026-11-10 · initial draft from the brief
  `2026-11-10-prompt-TOOL-aSmoothedDispatch-9-stale-arms`, grounded at `c13b0b63`. A probe found that
  the substitution drops the carriage-return byte, so the arms keep the carriage return in a
  variable rather than moving to a vertical tab.
- rev-2 · 2026-11-10 · AC1 · the builder's divergence record
  `2026-11-10-prompt-TOOL-aSmoothedDispatch-9-diverged` showed AC1's `sed` range cannot print one
  line: after S1 the string opens and closes on one line, and a `sed` range never tests its end
  address on its start line, so it printed to the next line ending in a quote. AC1 now greps the
  one-line `_rf_exempt` assignment. S1, S2 and the code they describe are unchanged.

## 9. Reuse audit

The unit extends seams already in the suite and adds no mechanism. S2 reuses the suite's own idiom
of carrying a carriage return in a variable (`tools/unattended/unattended.test.sh:4445`, `:4542`),
and both items keep the existing `hit` helper and the `_rf_exempt` list. `reuse_lookup.py` for "a
suite arm that passes a carriage return to a verb so the byte reaches the refusal" ranked the `arm`
SEAM (fan-in 37) of the other suites and nothing in this suite, so no existing seam fits better than
the in-file idiom. Recall ranked `TOOL-dWitnessedBar-74` and `TOOL-dWitnessedBar-76`, two canary
values that lose their carriage return after a read, which is a neighbouring class and not this one.
The checklist from `gotchas.py --for-paths` selected
`staged-break-substitutes-a-synthetic-value`, which is why the vertical tab was rejected. One
record disagreed with the code: the brief says `case` matches a carriage return inconsistently, and
the probe in §4 shows the match is constant and the byte is lost.

Recall terms used: `python tools/memory-recall/query.py "how does a suite arm carry a carriage return byte into a driver verb without losing it" --terms "carriage return command substitution loses byte variable hostile value matrix exemption stale dispatch writes split"`
