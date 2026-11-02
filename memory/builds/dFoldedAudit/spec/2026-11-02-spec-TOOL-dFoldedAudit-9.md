# TOOL-dFoldedAudit-9 — a build cannot pass a chain verdict that is not STOP

**Status:** CLOSED · rev-2 · 2026-11-02 · node d · Tier-2 · base 74274869 · streams tooling · order 130 · ratified 2026-11-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md) | research | TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-12 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |
| [2026-11-02-build-TOOL-dFoldedAudit-9-2-spec-stage-returns.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-2-spec-stage-returns.md) | journal | TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-12 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |
| [2026-11-02-build-TOOL-dFoldedAudit-9-3-cross-read-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-3-cross-read-return.md) | journal | TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |
| [2026-11-02-build-TOOL-dFoldedAudit-9-4-builder-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-4-builder-return.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-9-ledger.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-ledger.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-9-1-spec-writer.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-9-1-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-9-build-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-9-build-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-9-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-9-fix-brief.md) | research | TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-12 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |
| [2026-11-02-prompt-TOOL-dFoldedAudit-9-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-9-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Past `SPEC_FOLD_CUTOFF`, `--dispatch` derives the spec-audit chain's verdict and refuses anything but
STOP, so the re-audit that pays for a fold is enforced and a HOLD holds for the owner. That cutoff is
read at the default-branch side of the record's BASE, so a run cannot move itself onto the fold rule.
This closes items H1 and M4 of the closing review, round 1.

## 2. Scope (IN)

- **S1** — `read_fold_cutoff`, in `tools/unattended/lib-unattended.sh`, answers one record's
  `SPEC_FOLD_CUTOFF`: the value the conf blob declares at the merge-base of the record's `anchor-sha:`
  and `base:` facts, read by `read_brief_cutoff`, which moves into the library unchanged. It takes
  no value from the sourced conf while a run-state file exists. Observed by AC9 and AC11.
- **S2** — `read_spec_exit_rule` takes its date from S1, below its subject test, so a closing review
  reads nothing new. An unknown reading sets `_se_why`, which `check_spec_exit` already refuses.
  Observed by AC9, AC12 and AC13.
- **S3** — Check 2's `rv_foldpast` takes its date from S1, per record, for a record holding a row on
  a subject other than its slug. An unknown reading feeds `rv_bad`. The `rv_foldcut` variable goes
  and its shape `case` over the working copy stays, and the blank-key announcement stops speaking for
  every record. Observed by AC10, AC12 and AC15.
- **S4** — `read_chain_verdict` holds what `print_chain_verdict` computes, so the word has one
  derivation and two readers. The verb's output keeps its bytes. Observed by AC14.
- **S5** — `check_chain_dispatch` runs from `verb_dispatch`. It answers nothing under a rule other
  than `folds`, announces a skip where no audit is declared or recorded, refuses CONTINUE, and admits
  STOP with one printed line. Observed by AC1, AC4, AC6, AC7 and AC8.
- **S6** — `read_unrecorded_exits` names each terminal spec exit row of the run whose subject no chain
  round carries, and `check_chain_dispatch` refuses them, so a skipped `--record-round` cannot leave
  an older STOP standing. Observed by AC5.
- **S7** — HOLD is refused whatever the run's own rows say. Only the verdict moving lets a dispatch
  through, which §8 F1 frames. Observed by AC2 and AC3.
- **S8** — Every refusal shares an existing site: `check_chain_fault`, check 37's `fail` and
  `rv_bad`. Observed by AC15.
- **S9** — The driver suite's `write_fold_fixture` commits its conf first and records that commit as
  `base:`, because S1 refuses a record with none. Observed by AC9.

## 3. Non-goals (OUT)

- Whether a chain record's counts or folds are true. A forged round passes this gate. Item H2 is
  `TOOL-dFoldedAudit-10` and item H3 is `TOOL-dFoldedAudit-11`.
- The verdict's own derivation. `derive_chain_verdict` keeps every byte here. Items M7, M8 and L3
  change what it answers and this unit reads whatever it answers.
- A check 2 presence clause, a `--close` term or a Definition-of-Done item. See "Alternatives
  rejected".
- The date read. `check_landed_facts_due` and `read_first_commit_date` keep their code. Items H6, M3
  and M5 move what they answer, and `TOOL-dFoldedAudit-14` owns H6.
- An attended run. It holds no run-state file, so `--dispatch` refuses it at check 10 before this gate.
  `TOOL-dFoldedAudit-13` owns what an attended caller reads.
- `review.spec-audit.*` at BASE. `read_spec_audit_switch` keeps reading the working copy.
  `tools/policy/guarded-paths.txt` stops an agent committing a change there.
- `tools/unattended/.unattended.conf.example`. "Graded on the day the run's record began" stays true.
- The carriers. §8 F2 holds M6's sentence. The verbs carrier already says `dispatch nothing` at
  `tools/unattended/VERBS.template.md:297`, so it stays true and gains no line.
- A kit version bump. The lander mints each version at the landing (`tools/push-main.sh:26-31`).

### Edges

- **consumes-from** `TOOL-dFoldedAudit-14` — the `tenancy` argument on both `check_landed_facts_due` calls this unit rewrites, and the check 2 clause that reads `SPEC_FOLD_CUTOFF` itself; without them the rewrite has no second reader to leave behind and drops what that unit's AC3 arm pins
- **consumes-from** external — `derive_chain_verdict`, `read_chain_record`, `check_chain_fault`, `read_spec_audit_switch` and `read_spec_exit_rule`, built by CLOSED units of this build whose frozen specs take no mirror; this gate has nothing to read without them

## 4. Design

### The gate

`check_chain_dispatch "$rel" "$slug"` runs in `verb_dispatch` straight after the `--writes` flag test
at `tools/unattended/unattended.sh:14020`. That is above the `load_spec_facts` at `:14033`, because
`read_chain_verdict` reloads those maps through `drop_working_specs`, and the order gate below reads
them. A refusal there writes no row, as every refusal above the row does.

`read_spec_exit_rule "$rel" "$slug" "$slug-spec-set"` picks the rule. The third argument is any
subject that is not the slug, and the function only compares it. Then:

| Reading | Answer |
|---|---|
| `_se_why` non-empty | refused, through `check_chain_fault "$_se_why"` |
| `_se_rule` is `old` or `counted` | returns 0, silent, today's bytes, which is [scope]'s pre-cutoff and `promote-all` |
| `folds`, with no `spec-audit` fact, no tracked chain record and no spec exit row | returns 0, printing the announced skip |
| a terminal spec exit row whose subject no round carries | refused, naming each subject |
| verdict CONTINUE | refused, naming the reason and the ids after `audit` |
| verdict HOLD | refused, naming the ceiling key |
| verdict STOP | returns 0, printing the verdict line |

The judged fix arms on "a declared audit has run". This gate arms on the declaration too, through the
`spec-audit` fact, because a run that skips both `--review` and `--record-round` leaves neither of the
other two inputs. N is then 0, and the verdict reads `CONTINUE · reason unreviewed`. The record arms it
as well, because an attended chain can hold a build an unattended run later picks up.

The row test is check 2's: a `review · item` row, on a subject that is not the slug, whose reason
carries `CONVERGED`, `NON-CONVERGENT`, `CEILING` or `BOUNDED`. The harness passes one `subject` to
`--review` and to `renderChainRecord`, so the join is exact. It is needed beside the verdict because
the verdict reads the record alone: round 1's STOP would stand over a later exit nobody recorded.

Printed lines, each beside its own check 118 prefix where it refuses:

```
--dispatch builds nothing while the chain reads CONTINUE: round <N>, reason <reason>; re-invoke the build harness with auditIds: <ids>
--dispatch builds nothing while the chain reads HOLD: round <N> stands at the ceiling of <C> round(s), and only the owner moves review.spec-audit.chain-ceiling; a parked decision or a hand-off row is the question, never the answer
--dispatch reads a terminal spec exit no chain round records, so the verdict would be read without it: <subjects>; run that round's --record-round and commit the record
unattended: dispatch — chain <slug> · round <N> · STOP · reason <reason>
unattended: dispatch — no spec audit is declared or recorded, so no chain verdict gates this dispatch: an announced skip, not a pass
```

### The verdict, one derivation

`print_chain_verdict` splits at `tools/unattended/unattended.sh:13662`. `read_chain_verdict "$slug"`
takes everything from `spec_ids` through `derive_chain_verdict`, and adds `_cv_ceiling` to the `_cv_*`
set. `print_chain_verdict` keeps `check_slug` and the two `printf`s. `read_chain_record` stays
inside it, so the gate's own earlier call is a second read of one index and costs one `git ls-files`.
The status loop moves too, so `TOOL-dFoldedAudit-15`'s S15, at order 150, lands in `read_chain_verdict`.

### HOLD

The owner's decision is a move of `review.spec-audit.chain-ceiling` in `.governance/policy.toml`.
`tools/policy/guarded-paths.txt` names that file, so an agent's commit to it is refused. M3 already
reads a declared ceiling as the owner's to move. Nothing a run writes passes a HOLD: `--park` writes
the question, `--handoff` writes the stop, and both are the run's own rows.

A raised ceiling moves the verdict to step 5, so the chain reads CONTINUE and takes another round.
That is the route `tools/unattended/unattended.sh:13643` states, and a HOLD stays the answer until
then. §8 F1 holds the one thing this cannot do.

### The cutoff read

```bash
read_fold_cutoff() { # run-state file -> the value on stdout · 2 when it cannot be known
  [ -f "$1" ] || { printf '%s' "${SPEC_FOLD_CUTOFF:-}"; return 0; }
  # base and anchor-sha, out of `extract_run_facts`, one awk and CR-stripped
  [ -n "$_fc_b" ] || return 2
  _fc_c=$_fc_b
  [ -z "$_fc_a" ] || _fc_c=$(GIT merge-base "$_fc_a" "$_fc_b" 2>/dev/null) || _fc_c=""
  _fc_v=$(read_brief_cutoff "$_fc_c" SPEC_FOLD_CUTOFF) || return 2
  case "$_fc_v" in ""|[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) printf '%s' "$_fc_v" ;; *) return 2 ;; esac
}
```

- **The merge-base is unconditional.** `check_authorization` selects on `ANCHOR_KIND` at
  `tools/unattended/unattended.sh:4082`, which it derived in that shell. A later verb has only the
  recorded `anchor-kind`, and `:2919` and `:7818` rule out branching on a value the run wrote. Nothing
  selects here: on the first anchor BASE is an ancestor of the anchor, so the merge-base is BASE.
- **The sentinel read is `read_brief_cutoff`'s.** It moves from `tools/unattended/unattended.sh:3675`
  to the library, so the driver and check 2 share one reader. Its name stays, as
  `check_landed_facts_due`'s does for the same reason.
- **No run-state file reads the sourced conf.** An attended caller has no BASE and an owner present.
  `--review` and check 2 always hold a file.
- **An absent `anchor-sha:` reads at `base:`.** Every tracked record with a spec row carries the fact,
  so this branch serves fixtures. See "What this does not check".
- **Unknown is never off**, the rule `read_brief_cutoff`'s callers keep. `_se_why` carries it to check
  37 at `--review` and to check 118 at `--dispatch`. Check 2 feeds `rv_bad`.
- **Two units ship first.** Citations here are at `f055a11b`, below both. `TOOL-dFoldedAudit-14`, at
  order 90, gives both `check_landed_facts_due` calls a `tenancy` third argument, and each call keeps
  it through this rewrite, which that unit's AC3 arm reds if it does not. Its check 2 clause reads
  `SPEC_FOLD_CUTOFF` itself, so `rv_foldcut` has no reader left when it goes. `TOOL-dFoldedAudit-13`, at
  order 100, calls `read_spec_exit_rule` with no run-state file, which S1's first line serves.

`read_spec_exit_rule` at `:12754` binds `cut` from S1 between its subject test and
`check_landed_facts_due`. On an unknown it sets `_se_why` and returns with `_se_rule` at `old`. The
comments at `:618` and `:12747` and at `tools/unattended/check-unattended.sh:838` say the value the
source binds decides nothing, in the shape `:613` uses.

Check 2's read at `tools/unattended/check-unattended.sh:843` becomes per record, and the test for a
row off the slug uses no process, reading the file with `read -d ''` and two parameter expansions. The
announcement at `:726` stops saying "every": it says a run preflighted from this tree keeps the old
rule and a record is graded by the conf at its own BASE. The comment at `:317` gains this second
evaluation.

### What this does not check

- That a run calls `--dispatch` at all. A commit with no `Pass:` trailer skips it, which is the limit
  M2's floor already has, and check 23 grades passes at the close.
- A round's truth, as §3 says. A forged STOP passes.
- An uncommitted edit of the guarded policy file. The verdict reads the working copy, and the guard
  refuses the commit, so no such value lands.
- A run that deletes `anchor-sha:` and whose BASE it wrote itself reads a date it chose. The local and
  second anchors allow such a BASE, the edit shows in the diff, and check 9 still grades the BASE.
- A subject outside `[A-Za-z0-9-]+` on a by-hand `--review` row, which `--record-round` refuses, so
  such a row holds the gate. The harness's subject always fits.

### Inventory

| Minted | Cell | Graded by |
|---|---|---|
| `read_fold_cutoff`, `read_chain_verdict`, `check_chain_dispatch`, `read_unrecorded_exits` | `sh.function` | `lexicon.py --suggest` answered OK on 2026-11-02 |
| `_cv_ceiling` | driver out-variable | the `_cv_*` set at `tools/unattended/unattended.sh:13638` |

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/lib-unattended.sh` ·
`tools/unattended/check-unattended.sh` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/check-unattended.test.sh`

### Rollout

Dark until the close writes `SPEC_FOLD_CUTOFF`, and then only for a run whose BASE carries the date.
This build's own record keeps the old rule: its conf at BASE is blank. New functions move the
generated symbol index, which the pass declares with the indexes it regenerates.

### Alternatives rejected

- **A Definition-of-Done item.** It reads after every unit is built, which is the failure H1 names.
  M6 places the refusal of a pass at `--dispatch`.
- **The check 2 clause the judged fix offers as an alternative.** It reds a landed record at the bar,
  after the code is written, and reaches the same subjects S6 reads at the act. `TOOL-dFoldedAudit-10`
  leaves a presence term out too, so S6 is the one reader of that population.
- **`check_chain_dispatch` keyed on `promote-all` too.** [scope] keeps today's rule there, and H1's
  compensation argument is about a fold.
- **Reading `AUTH_CONF_AT`.** Only `check_authorization` sets it, and neither `--review` nor check 2
  calls that. A fresh anchor observation at `--review` would add a network round per review.
- **A new fact pinning the default-branch side at preflight.** It is one more byte the run writes, and
  no landed record carries it.
- **A parsed read in check 2, as `read_origin_scope` does.** It would be a second reader of one key,
  the class `two-readers-of-one-config-one-re-derived` names, and the leg already sources the conf.
- **The working copy as a filter ahead of the BASE read.** A run blanking its date would then disagree
  with its own `--review`, which AC10's mirror forbids.

## 5. Production-readiness checklist

- security: the unit narrows a run's reach. The switch's date stops being run-writable, which is the
  claim TOOL-dFoldedAudit-7 made and M4 refuted. `read_brief_cutoff` evaluates a committed conf blob
  in a subshell, and check 2 becomes its second caller. That is no wider: the leg already sources the
  conf a run commits at `tools/unattended/check-unattended.sh:346`, and the result is a shape-checked
  date. `base:` and `anchor-sha:` are run-written evidence, and check 9 is what grades the pin.
- perf / scale: `--dispatch` adds one awk, one merge-base and one `git show` under every rule. Past
  the cutoff it adds the verdict's `git ls-files`, one awk and three policy reads. Check 2 adds one awk,
  two git calls and a subshell per record holding a spec row. PINNED 2026-11-02 at `f055a11b`: 62 of
  117 tracked records, at 24 ms a git call, about 4 s against the leg's ceiling of 16040 s.
- error / empty / loading states: no audit is an announced skip. An unknown conf refuses and is never
  read as off. A declared audit with no record reads `round 0 · CONTINUE`, which refuses.
- observability: a pass prints the verdict line, and each refusal names the word, the reason and the
  next act. The switch's own note reaches stderr as it does at `--chain-verdict`.
- risks:
  - A unit a closing review promotes under a declared audit reads `unreviewed`, so every dispatch stops
    until it is audited. That is M4's "audited as a SPEC", and its rounds count against the ceiling.
  - `--rescope --act add` after a STOP does the same, for the same reason.
  - The suites hold the change: `write_fold_fixture` moves, and so does any fixture recording a spec
    row with no `base:` that asserts check 2 green.
- testing: fixtures per §6, with no gate, and the arms on `New arm:` lines in §7. Each refusal reads
  its own text, because all share one signature that `harness arms (fail branches armed or pinned)`
  reads as one.
- migration: additive. No landed record moves. PINNED 2026-11-02 at `f055a11b`: all 62 records read a
  blank value, none read unknown, and 32 of them sit below their BASE. Check 2 therefore answers
  exactly as it does today for every tracked record.
- user docs: N/A. `help/` documents neither `--dispatch` nor the spec audit.

## 6. Acceptance criteria

Fixture G is a scratch git repository at `%TEMP%/fa9g` on branch `main` with no remote, built as the
suites' `write_switch_fixture` builds its own. It holds the build `dFix` of `write_chain_fixture`, with
a roster of `FIX-dFix-1` to `FIX-dFix-7` whose specs grade READY. BASE is the commit carrying
`.unattended.conf` with `MEMORY_ROOT=memory`, `DISPOSITION_CUTOFF="2000-01-01"`, `REVIEW_ROUNDS="1"` and
`SPEC_FOLD_CUTOFF="2026-11-01"`. `RUN.md` is committed after it, carrying `base: <BASE>`. `DATED` means
that commit is dated `2026-11-02T12:00:00 +0000`, and `EARLY` means `2026-10-30T12:00:00 +0000`. No
policy kit sits beside the driver unless a criterion says so, so the switches answer their defaults.
`$D` and `$G` are the fixture's own `unattended.sh` and `check-unattended.sh`, run from the fixture.
`$PASS` is `--dispatch dFix --pass FIX-dFix-1 --writes a.sh`. Fixtures clear `GOV_REMOTE` and
`GOV_DEFAULT_BRANCH`.

- **AC1** — When a `DATED` fixture records `$D --record-round dFix --subject s1 --audited "<all seven>" --blockers 0 --highs 1 --finding 1/HIGH/local/FIX-dFix-2/FIX-dFix-2/2`,
  `$D --chain-verdict dFix` prints `round 1 · CONTINUE · reason open · audit FIX-dFix-2`, and `$D $PASS`
  exits 1 printing `UNATTENDED check 118 FAILED` and `--dispatch builds nothing while the chain reads CONTINUE`.
  `RUN.md` gains no `dispatch · item` row.
  Red when: `verb_dispatch` never calls `check_chain_dispatch`, which is the failure H1 names.
- **AC2** — When a `DATED` fixture records the four promoting rounds of FA5's AC8, so the verdict reads
  `round 4 · HOLD · reason ceiling`, `$D $PASS` exits 1 printing `--dispatch builds nothing while the chain reads HOLD`
  and `review.spec-audit.chain-ceiling`. After `$D --park dFix --item spec-audit-chain-ceiling --reason r`
  and a hand-written `handoff · item owner-decision` row, it refuses the same way.
  Red when: a row the run wrote passes a HOLD.
- **AC3** — When that record stands beside a committed `.governance/policy.toml` reading
  `chain-ceiling = 6` and the policy kit, `$D $PASS` still exits 1 naming `CONTINUE`. A fifth round
  auditing `FIX-dFix-7` with no finding makes `$D $PASS` exit 0, and `RUN.md` gains its row.
  Red when: the gate reads a ceiling other than the verdict's, so the owner's move changes nothing.
  fixture: `tools/policy/policy.py` with `budgets.py` and `catalogue.toml` beside it.
- **AC4** — When a `DATED` fixture records a clean round auditing all seven, `$D $PASS` exits 0
  printing `unattended: dispatch — chain dFix · round 1 · STOP · reason clean`, and `RUN.md` gains a
  `dispatch · item` row. Over FA5's AC6 record it exits 0 printing `STOP · reason own-work`.
  Red when: the gate refuses a STOP, or passes one in silence.
- **AC5** — When AC4's fixture also runs `$D --review dFix --subject s2 --verdict "CLEAN WITH FIXES" --blockers 0 --highs 1 --minors 0 --folded 1 --promoted 0 --disposition fold`,
  `$D $PASS` exits 1 printing `--dispatch reads a terminal spec exit no chain round records` and `s2`.
  With no chain record at all and the same row, it refuses the same way. After that round's
  `--record-round`, the refusal names the verdict rather than the subject.
  Red when: the gate reads only the last round, so an older STOP stands over an unrecorded exit.
- **AC6** — When a `DATED` fixture's `RUN.md` carries `spec-audit: 2026-11-01` and holds no row and no
  chain record, `$D $PASS` exits 1 printing `round 0` and `reason unreviewed`.
  Red when: the fact is not read, so a run skipping both verbs builds unaudited.
- **AC7** — When AC1's record, committed by hand because `--record-round` refuses its `local` row on
  each of these since `TOOL-dFoldedAudit-13`, sits in a fixture whose BASE conf has a blank
  `SPEC_FOLD_CUTOFF`, in an `EARLY` fixture, and in a `DATED` fixture with the policy kit and
  `disposal = "promote-all"`, `$D $PASS` exits 0 each time and prints no `unattended: dispatch — chain` line.
  Red when: the word is read ahead of the rule, so an old-rule run is refused.
  fixture: the third case needs the policy kit, so the arm counts its assertions either way.
- **AC8** — When a `DATED` fixture's `RUN.md` carries no `spec-audit:` fact and one row on subject
  `dFix`, and no chain record exists, `$D $PASS` exits 0 printing `no spec audit is declared or recorded`.
  Red when: a closing review's row arms the gate, or the skip is silent.
- **AC9** — When BASE's conf has a blank `SPEC_FOLD_CUTOFF` and a later `DATED` run commit writes
  `SPEC_FOLD_CUTOFF="2026-11-01"`, `$D --review dFix --subject S1 --verdict "CLEAN WITH FIXES" --blockers 0 --highs 1 --minors 2 --folded 3 --promoted 0 --disposition fold`
  refuses with `--folded and --promoted are counted only at a spec audit's terminal exit past SPEC_FOLD_CUTOFF`.
  When BASE's conf is dated and the run commit blanks it, the same call exits 0.
  Red when: `read_spec_exit_rule` reads the sourced `$SPEC_FOLD_CUTOFF`, which is the failure M4 names.
- **AC10** — When AC9's two trees each hold that row committed by hand, `$G` prints
  `spec subject(s) S1 record a terminal row` for the first and no `UNATTENDED check 2 FAILED` line for
  the second. Red when: check 2 reads the sourced key.
- **AC11** — When `RUN.md` carries `anchor-sha: <main's tip>` and `base:` names a run commit above it
  that dates the key, AC9's call refuses and AC10's `$G` prints the first line. With `base:` at a dated
  commit on `main` and `anchor-sha:` at or above it, the call exits 0.
  Red when: `read_fold_cutoff` reads at `base:` and not at the merge-base, or branches on `anchor-kind`.
- **AC12** — When BASE's conf opens with `return 0`, when it spells `SPEC_FOLD_CUTOFF="soon"`, and when
  `RUN.md` carries no `base:`, each over a working copy a later commit restored and beside a committed
  spec subject's row, AC9's call exits 1 printing `--review cannot record this spec audit exit: `,
  `$D $PASS` exits 1 printing `UNATTENDED check 118 FAILED`, and `$G` names the record in a check 2 line.
  Red when: an unknown conf reads as blank, which puts the run on the old rule and off this gate.
- **AC13** — When `RUN.md` carries no `base:`, `$D --review dFix --subject dFix --verdict CLEAN --blockers 0 --highs 0 --minors 0`
  records its row as it does at this spec's HEAD.
  Red when: the read sits above the subject test, so a closing review changes.
- **AC14** — When `$D --chain-verdict dFix` runs over AC2's record, it prints `round 4 · HOLD · reason ceiling`
  and a second line carrying `--handoff dFix --code owner-decision`, the two FA5's AC8 arm pins, and
  `grep -c 'derive_chain_verdict "' tools/unattended/unattended.sh` prints 1.
  Red when: the gate carries a second derivation, or the split moves the verb's output.
- **AC15** — When `grep -cE '(^|[^a-zA-Z_])fail [0-9]+ "' tools/unattended/unattended.sh tools/unattended/check-unattended.sh`
  runs, each count equals its count at the pass's parent commit.
  Red when: a refusal took its own `fail` site, past a ceiling only the owner moves.
  figure: DERIVED at observation from the parent commit.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `routed-commits selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `kit version markers`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC4 AC5 · a fold on CONTINUE, a STOP beside it and an unrecorded exit, staged with the `check_chain_dispatch` call deleted from `verb_dispatch` · `FLOOR_ASSERTIONS` by the arm's executed count, and `FLOOR_SHARD_1` where it lands in that shard
New arm: tools/unattended/unattended.test.sh · covers AC2 AC3 · a HOLD with no owner decision, its park and hand-off rows, then the policy file's move, staged with the HOLD arm returning 0 where a park row exists · `FLOOR_ASSERTIONS` by the arm's executed count
New arm: tools/unattended/unattended.test.sh · covers AC6 AC7 AC8 · the declared-only, off-rule and no-audit populations, staged with the rule test deleted from the gate · `FLOOR_ASSERTIONS` by the arm's executed count
New arm: tools/unattended/unattended.test.sh · covers AC9 AC11 AC12 AC13 · a run commit moving the date either way, a run commit below the anchor, and each unknown shape, staged with `read_spec_exit_rule` reading the sourced key · `FLOOR_ASSERTIONS` by the arm's executed count
New arm: tools/unattended/check-unattended.test.sh · covers AC10 AC11 AC12 · the same fold row under a moved date, each side, and an unknown conf, staged with `rv_foldpast` reading the sourced key · `FLOOR_ASSERTIONS` by the arm's executed count
New arm: tools/unattended/unattended.test.sh · covers AC14 AC15 · the one derivation and the census over the driver's own text, staged with a second `fail 118` · `FLOOR_ASSERTIONS` by the arm's executed count

## 8. Open questions

- **F1 — What counts as the recorded owner decision that passes a HOLD?** The judged fix says "A HOLD
  should need a recorded owner decision to pass", and names no record. This repo has no row only an
  owner writes. So the choice is a real one, and option (a) is a departure from the fix's shape:
  nothing passes a HOLD, and the verdict moves instead.
  - (a) No pass-through. The owner moves `review.spec-audit.chain-ceiling`, a guarded path, and the
    verdict leaves HOLD for CONTINUE. It adds no row, no verb and no carrier line. It cannot say "build
    at the hold with no further round" in an unattended run: the owner finishes that attended, or
    takes the audit round the raised ceiling asks for. §4 is written to this option.
  - (b) A `decision · item spec-audit-chain-ceiling` row with a later `handoff · item owner-decision`
    row passes. It adds no surface, but the run writes both rows, so the "owner decision" is the run's
    own, and `tools/unattended/unattended.sh:7200` shows `--handoff` asks only for a parked row.
  - (c) A new owner record: a verb, or a `may:` token in an owner-committed README. It can say "build
    at the hold". A verb costs check 26's join on both carriers, with the Skill pinned at no headroom,
    and either form trips M3's veto 2 as a new public surface.
  Recommendation: (a). Option (b) fails the fix's own word "owner", and (c) is vetoed under a mandate.
  AC2 and AC3 are its discriminating arms. If the owner wants "build at the hold", that is (c) as a
  follow-up, and it reads this gate rather than changing it.
  RESOLVED (agent, 2026-11-02, delegated): (a). Nothing passes a HOLD, and the owner's move of the
  guarded ceiling key moves the verdict.
- **F2 — Who corrects M6's sentence?** `memory/guides/BUILD-METHOD.md:232` says `--dispatch` refuses
  "on a MISSING or THIN unit and on nothing else", and this unit makes that false. The method is a
  governance carrier, `RUN.md` records `may: none`, and the file stands at 30565 of 30720 bytes.
  - (a) No pass writes it. Whoever resolves this fork parks one `decision` row carrying the question,
    these options and the reason, as `RUN.md` did at 2026-11-02T00:33:44Z for the hygiene sentence, so
    the owner gets it at the wrap-up. The sentence stays false until then.
  - (b) This unit adds the clause to `tools/memory-tree/BUILD-METHOD.template.md` and its render, with
    `memory/guides/SESSION-KICKOFF.md` joining the write set for its `last-audit` and `Manifest delta:`
    line. About 40 bytes fit, and the method stops being wrong. M3's veto 2 discards it under
    `may: none`, and the accepted brief bars a carrier write beyond M4's stated change.
  Recommendation: (a), the only option past veto 2. It is written here and not as a hands-off line
  because the `orchestrator-hand-off-owed-a-disposition` class names a line no run reads, and §8 is
  what the main loop sweeps.
  RESOLVED (agent, 2026-11-02, delegated): (a). The `decision` row stands in `RUN.md` at
  2026-11-02T03:29:31Z, so no pass writes the sentence and the wrap-up carries it to the owner.

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, from items H1 and M4 of the closing review round 1, the promotion
  notes' tags and the design's [chain], [cutoff] and [scope].
- rev-2 · 2026-11-02 · §4 · §8 · AC7 · F1 and F2 are RESOLVED to (a), and the header gains `ratified`.
  M2's cross-read: AC7 read its three off-rule records as written by a verb `TOOL-dFoldedAudit-13`
  refuses there, so each is committed by hand; and §4 named `TOOL-dFoldedAudit-10` the owner of a
  presence term that spec's §3 rules out.

## 10. Reuse audit

`reuse_lookup.py` on "refuse a dispatch when a derived review verdict has not stopped" ranked name
stems and no gate over a verdict, and on "read a conf key from the blob at the default branch side of
the pinned base" it ranked `read_conf_key` and `read_blobs_at`, neither of which reads this conf. The
seams this unit extends are all in the driver and its library. `verb_dispatch` is where M2's floor
already refuses, at `tools/unattended/unattended.sh:14011`. `print_chain_verdict` at `:13646` and
`derive_chain_verdict` at `:13567` give the word, and `check_chain_fault` at `:13462` is the shared
refusal. `read_spec_exit_rule` at `:12754` gives the rule, and `read_brief_cutoff` at `:3675` is the
sentinel read, promoted to `tools/unattended/lib-unattended.sh` at its second caller beside
`check_landed_facts_due`. `tools/memory-tree/gotchas.py --for-paths` selected
`two-readers-of-one-config-one-re-derived`, which S1 answers with one reader, and
`fixture-passes-by-finding-nothing`, which AC4 and AC7 answer with a population either side.

Every line the review cited was re-read at `f055a11b`: H1's `:13646` and `:14971` and M4's `:623` held,
and `tools/policy/guarded-paths.txt` lists no conf file. One thing differs from the review's wording.
Its fix reads the conf "as `read_brief_cutoff` does", and both that function's callers pass
`AUTH_CONF_AT`, which `--review` and check 2 never set, so S1 derives the side itself, and `:2919` and
`:7818` rule out selecting on the recorded `anchor-kind`. A read-only probe ran the predicate over the
62 tracked records with a spec row: none read unknown, none lacks `anchor-sha:`, every merge-base
resolves, and 30 sit at BASE and 32 below it, so the unconditional merge-base refuses nothing landed.
The recall hits on TOOL-aWardedAudit-1 and TOOL-dIndexedDesign-21 agree that a key a run can write is
read at the default-branch side, and they name no reader of `SPEC_FOLD_CUTOFF`.

Recall terms used: `python tools/memory-recall/query.py "what stops a run dispatching before the spec audit chain verdict reads STOP and how is a HOLD released by the owner" --terms "chain-verdict dispatch refusal HOLD owner-decision ceiling SPEC_FOLD_CUTOFF read_brief_cutoff default-branch side BASE"`
