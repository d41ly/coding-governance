# TOOL-dFinishedRecord-1 — check 24 stops grading a run that derived LANDED

**Status:** CLOSED · rev-1 · 2026-11-05 · node d · Tier-2 · base 51912ffc · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-05-build-TOOL-dFinishedRecord-1-1-acceptance-ledger.md](../build/2026-11-05-build-TOOL-dFinishedRecord-1-1-acceptance-ledger.md) | journal | — |
| [2026-11-05-build-TOOL-dFinishedRecord-1-agent-ledger.md](../build/2026-11-05-build-TOOL-dFinishedRecord-1-agent-ledger.md) | journal | TOOL-dFinishedRecord-2 |
| [2026-11-05-prompt-TOOL-dFinishedRecord-1-brief.md](../prompts/2026-11-05-prompt-TOOL-dFinishedRecord-1-brief.md) | research | — |
| [2026-11-05-review-TOOL-dFinishedRecord-1-closing-diff-round1.md](../reviews/2026-11-05-review-TOOL-dFinishedRecord-1-closing-diff-round1.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

Check 24 of `tools/unattended/check-unattended.sh` skips a run record only when its recorded phase
reads `LANDED` or `ABORTED`. An in-place landing leaves its record at `LANDING`, so a finished run is
still graded for roster amendments. The `--rescope` verb refuses to record one on a finished run, so
no record satisfies both. This unit makes check 24 ask `check_derived_landed`, the predicate checks 7
and 23 already share, and exclude a record whose landing commit the advertised tip reaches.

## 2. Scope (IN)

- **S1** — Check 24's roster loop calls `check_derived_landed "$f"` for every record that survives
  its existing skips: not a `RUN.md`, a recorded `LANDED|ABORTED` phase, and no build README. On 0
  it prints one `check 24 EXCLUDED` line on the default channel and skips the record. Observed by
  AC1, AC2, AC4 and AC5.
- **S2** — On 2 the loop prints one `check 24 exclusion UNAVAILABLE` line per run on the default
  channel, the first time the predicate returns 2, and grades that record as before. A guard
  variable `rs_unavail`, set to 0 before the loop, makes the line print once. Observed by AC3.
- **S3** — The leg's header exception TWO names check 24's two notices beside check 23's, so the
  header's "exit 0 + no output" contract still describes the code. Observed by AC7.
- **S4** — Three new arms in `tools/unattended/check-unattended.test.sh`, placed directly after the
  check 24 roster block's closing `reset_tree` and before the check 23 header, inside region 8.
  Observed by AC1, AC2 and AC3.
- **S5** — `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` in the same suite each rise by exactly the number
  of assertions the new arms execute. A `RAISED` comment line above `FLOOR_ASSERTIONS` names this
  unit and the count, in the house shape of the lines already there. Observed by AC8.
- **S6** — No second copy of the predicate's test. The change adds no call to `read_landing_commit`
  or `check_adv_reaches`. Observed by AC6.

## 3. Non-goals (OUT)

- **The driver's verbs and `refuse_if_terminal`** at `tools/unattended/unattended.sh:4558`, which
  `verb_rescope` calls at line 13991. The refusal of an amendment to a finished run is correct and
  stays.
- **Checks 7 and 23.** Their exclusion blocks and message strings do not move.
- **`check_derived_landed` itself**, at `tools/unattended/check-unattended.sh:692`, including its
  HELD-under-a-hand-off-code admission. This unit calls it and does not edit it.
- **dConvergedCharter's run-state file**, which stays as landed at `923954b61`.
- **Any other check's phase read**, such as check 15's fact-set arm or check 19's grant arm.
- **A recorded-LANDED control arm.** The predicate tests the phase first and returns 1 for a
  `LANDED` record before it reads the advertisement, so no break of this unit's code can red such an
  arm. TOOL-aSightedSkeptic-13 rev-2 records the same finding for check 23. The existing re-run arm,
  whose first run is recorded `LANDED`, already covers check 24's phase skip.
- **A hand bump of the kit version.** Kit versions move through the lander's `mint`.
- **A help page.** No verb, flag or conf key changes.

### Edges

- **consumes-from** external — `check_derived_landed`, `DERIVED_LANDING_COMMIT`, `ADV_HEAD` and
  `ADV_HEAD_OK` in `tools/unattended/check-unattended.sh`, all present at base; this unit builds
  none of them.
- **consumes-from** external — the lander's `--prepare`, which mints the unattended kit version into
  the prepared merge (`tools/push-main.sh` lines 26 to 33). Without it the kit epoch leg reds the
  landing.

## 4. Design

### Evidence

Read at base `51912ffc`. `tools/` is byte-identical at the build branch's tip `387d766c` and at the
advertised tip `923954b6` (`git diff --stat` printed nothing for both). Line numbers are PINNED to
that reading, and the builder locates each site by its quoted text.

| Site | Lines | What it does today |
|---|---|---|
| header exception TWO | 26–38 | names check 7's and check 23's default-channel notices |
| `check_adv_reaches` | 670 | ancestry against `ADV_HEAD`, from a reach set warmed once per shell |
| `check_derived_landed` | 680–704 | 0 derived LANDED and sets `DERIVED_LANDING_COMMIT`, 1 not, 2 UNAVAILABLE |
| `ADV_HEAD_OK` | 1720–1721 | 1 when the advertised tip resolves to a commit in this clone |
| check 7 exclusion | 3408–3440 | asks the predicate per live record and prints `check 7 EXCLUDED` |
| check 24 roster loop | 4186–4309 | skips at 4187, 4188, 4189 and 4193, then the ADD, RETIRE and supersession arms |
| check 24 ADD arm `fail 24` | 4269 | a unit absent from the BUILDING-time roster with no `add` or `supersede` row |
| check 23 exclusion | 4437–4451 | the shape this unit copies, messages included |
| check 23 guard init | 4386 | `ds_unavail=0` beside the loop's other counters |

The roster loop holds only check 24's arms. Its opening comment still says "22", from before the
check was renumbered; every `fail` in it is `fail 24`.

The live failure is reproducible from the tree. `memory/builds/dConvergedCharter/RUN.md` reads
`phase: LANDING`, and `git log -1 -- memory/builds/dConvergedCharter/RUN.md` names `923954b61` on
both the build branch and `main`. `git ls-remote origin HEAD` printed `923954b6` on 2026-11-05, so
that commit is the advertised tip. The README's units region carries `PLAY-dConvergedCharter-41`,
and `grep -c dConvergedCharter-41` over the RUN.md prints 0, so no `add` row names it.

### The change to the leg

Before the loop at line 4186, one line:

```bash
rs_unavail=0
```

In the loop, directly after `[ -f "$bre" ] || continue` at line 4193 and before the `# ---- 22:`
comment block:

```bash
  # ---- DERIVED LANDED IS NOT GRADED (TOOL-dFinishedRecord-1). An in-place landing leaves its record
  # ---- at LANDING, so the recorded-phase skip above never fires for it, and a roster that grows after
  # ---- the landing owes a rescope row the driver's --rescope refuses on a finished record (check 26).
  # ---- Check 7's predicate, asked AFTER every skip, as check 23 asks it: a record that was never
  # ---- graded stays silent. Default channel, for header exception TWO's reason.
  check_derived_landed "$f"; rs_dl=$?
  if [ "$rs_dl" = 0 ]; then
    printf 'unattended: check 24 EXCLUDED %s — derived LANDED: its landing commit %s is an ancestor of the advertised default-branch tip %s, so its roster is landed and an amendment after the landing owes a rescope row the driver refuses to write on a finished run\n' "$f" "$DERIVED_LANDING_COMMIT" "$ADV_HEAD"
    continue
  fi
  if [ "$rs_dl" = 2 ] && [ "$rs_unavail" = 0 ]; then
    rs_unavail=1
    printf 'unattended: check 24 exclusion UNAVAILABLE — no advertised default-branch tip resolves in this clone, so a LANDING record already on the remote cannot be told from a live one; every LANDING record is graded for roster amendments\n'
  fi
```

The call is a plain command and never inside `$(...)`, which the predicate's own header requires.
Placing it after the build-README skip copies check 23, which asks after both of its skips so a
record that was never graded prints nothing. Placing it after the `LANDED|ABORTED` skip keeps the
exclusion a no-op under `LANDER_MODE=primary`, where a landed record reads `LANDED` and never reaches
the predicate.

A HELD record under a hand-off code whose landing commit is on the tip is excluded too, because the
predicate admits it. That is the driver's attended reading, and checks 7 and 23 already share it.

Header exception TWO gains one clause after check 23's two notices: "and check 24's
`check 24 EXCLUDED` and `check 24 exclusion UNAVAILABLE`, over the same predicate
(TOOL-dFinishedRecord-1)".

### The arms (S4)

Each arm builds on the `seed_ros` fixture: tRos goes live with `ARCH-tRos-1`, its BASE pinned to that
commit. Each asserts only check 24's own strings, because a LANDING record also moves checks 7, 15 and
19. `c24_land` holds the landing commit inside the block and crosses no region boundary.

| Arm | Fixture | Asserts | Red against |
|---|---|---|---|
| A | phase set to `LANDING` and committed, `c24_land=$(git rev-parse HEAD)`, `git push -q -f origin HEAD:main`, then `add_u7` committed after the landing; origin restored to `$ANCHOR0` after | `hit` of `check 24 EXCLUDED memory/builds/tRos/RUN.md — derived LANDED: its landing commit $c24_land`; `miss` of `check 24 FAILED` | the parent leg, which grades the record and fails 24 for `ARCH-tRos-7` |
| B (control) | arm A's fixture, not pushed | `hit` of `so the scope moved with nothing on the record saying so: ARCH-tRos-7 in memory/builds/tRos/RUN.md`; `miss` of `check 24 EXCLUDED` | a staged break replacing `check_derived_landed "$f"; rs_dl=$?` with `rs_dl=0` |
| C | arm B's fixture, plus tRun's phase set to `LANDING` and committed, then `git --git-dir="$ORIGIN" symbolic-ref HEAD refs/heads/nothing-here`; restored to `refs/heads/main` after | `same` of `grep -c 'check 24 exclusion UNAVAILABLE'` against `1`; `hit` of the arm B failure line; `miss` of `check 24 EXCLUDED` | the parent leg (0 lines), and a staged break deleting the `rs_unavail` guard (2 lines) |

Arm A commits `add_u7` AFTER the landing commit, which is the dConvergedCharter shape: the roster
grew after the landing, and the landing commit `read_landing_commit` finds is still the commit that
last wrote the RUN.md.

Arm C puts two LANDING records in front of the predicate. With one, the count is 1 whether or not the
guard exists, so the arm could not tell a working guard from a missing one.

Arm B is a CONTROL. It is green against the parent leg by construction, so it is observed red against
its staged break instead.

The three arms execute seven assertions: two in A, two in B and three in C. The floor raise in S5 is
that count as the block is finally written, counted off its own `hit`, `miss` and `same` lines.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `rs_dl` | check 24 loop local | not graded; no shell-variable cell is declared |
| `rs_unavail` | check 24 run-wide guard | not graded; no shell-variable cell is declared |
| `c24_land` | suite block local | not graded |
| `check 24 EXCLUDED`, `check 24 exclusion UNAVAILABLE` | default-channel message heads | none |

### Rollout

1. Edit `tools/unattended/check-unattended.sh` in binary mode. It carries bare CR bytes inside awk
   regexes, and a text-mode read turns each into a newline (`memory/gotchas/text-mode-read-eats-a-bare-cr.md`,
   cited at `memory/guides/SESSION-KICKOFF.md:73`).
2. Write S1 to S3, then the arms and the floor raise.
3. Verify in the pass with `bash -n` on both files and the grep criteria AC6 to AC10. The pass runs
   no gate leg and no suite.
4. Commit once with the unit id in the subject. Do not bump `KIT_UNATTENDED_VERSION`.
5. The main loop observes arms A to C red and then green at the close, through the `New arm:` line,
   and observes AC5 over the live tree.

### Files touched (estimate)

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh`

### Alternatives rejected

- **Ask the predicate directly after the recorded-phase skip, as the brief's item 1 words it.** A
  derived-LANDED record whose build README is gone would then print an EXCLUDED line for a record the
  loop never graded. Check 23 asks after all of its skips for that reason. The brief's acceptance
  holds under either placement.
- **Inline the test.** Two inline copies of one question is how check 23 was left out of it, per the
  predicate's header at line 683.
- **Let `--rescope` write on a derived-LANDED record.** A non-goal: the brief keeps the driver's
  verbs. It would also re-open a finished record, which check 26 exists to refuse.
- **Announce on the report channel.** Header exception TWO records why: an exclusion changes the
  verdict, and a REPORT line is invisible on every bar run.

## 5. Production-readiness checklist

- security — N/A: a read-only gate leg, and the landing commit is found by the kit library from the
  record's history, never read from a field the run authors.
- perf / scale — one predicate call per LANDING record that reaches the loop's arms. The reach set is
  warmed once per shell, and each excluded record skips two `git show` walks and the three arms.
- error / empty / loading states — the predicate fails closed: an uncommitted record or no
  advertised tip keeps the record graded, and UNAVAILABLE says so once.
- observability — every exclusion prints the record, its landing commit and the tip on the default
  channel, and the header contract is amended to admit both lines.
- risks — the default output grows by one line per derived-LANDED record with a build README. The
  suite's whole-output green controls run on fixtures holding none, so `remove_announcements` is not
  widened. At the close, the kit epoch leg is green only over the minted prepared merge.
- testing — arms A to C, each observed red against its named break, and the existing check 24 arms.
- migration — N/A: no record and no conf key moves.
- user docs — N/A: no help page covers this leg's output, and no verb, flag or conf key changes.

## 6. Acceptance criteria

- **AC1** — When arm A runs, its `out` carries `check 24 EXCLUDED memory/builds/tRos/RUN.md — derived
  LANDED: its landing commit` followed by the fixture's landing commit, and carries no
  `check 24 FAILED`.
  Red when: run against the parent `tools/unattended/check-unattended.sh`, which grades the record and
  fails 24 for `ARCH-tRos-7`.
  permission: the suite runs at the main loop's close, never in a unit pass.
  fixture: the suite's own `seed_ros` fixture and bare origin; nothing in the tree is required.
- **AC2** — When arm B runs, its `out` carries `so the scope moved with nothing on the record saying
  so: ARCH-tRos-7 in memory/builds/tRos/RUN.md` and no `check 24 EXCLUDED`.
  Red when: the staged break `rs_dl=0` replaces the predicate call, so every record is excluded.
  permission: the suite runs at the main loop's close, never in a unit pass.
- **AC3** — When arm C runs, `grep -c 'check 24 exclusion UNAVAILABLE'` over its `out` prints 1, and
  `out` carries the `ARCH-tRos-7` failure line and no `check 24 EXCLUDED`.
  Red when: run against the parent leg (0 lines), with the `rs_unavail` guard deleted (2 lines), or
  with return 2 treated as excluded (no failure line).
  permission: the suite runs at the main loop's close, never in a unit pass.
- **AC4** — When the suite's region 8 runs, every existing `hit`, `miss` and `same` of the check 24
  roster block, from the `URO` row through the `seed_spc absent` arm, stays green, and
  `git diff 51912ffc -- tools/unattended/check-unattended.test.sh` shows no removed line inside it.
  Red when: the exclusion treats return 1 as excluded, so every live tRos record is skipped and the
  block's `hit` arms on the ADD and RETIRE messages red.
  permission: the suite runs at the main loop's close, never in a unit pass.
- **AC5** — When `bash tools/unattended/check-unattended.sh` runs over the build's tip, and over its
  prepared merge with a default branch at or after `51912ffce`, it prints
  `check 24 EXCLUDED memory/builds/dConvergedCharter/RUN.md` and no `check 24 FAILED`.
  Red when: run against the parent leg, which prints `check 24 FAILED` naming
  `PLAY-dConvergedCharter-41`.
  permission: a gate leg; the main loop observes it at the close.
  cost: about 222 s per run on node d, PINNED from TOOL-dThriftyLanding-7 (filed 2026-10-05).
  fixture: the live tree holds it today: dConvergedCharter's record is `LANDING`, last written by
  `923954b61`, which `git ls-remote origin HEAD` named on 2026-11-05. A later push keeps it an
  ancestor of the tip.
- **AC6** — When `grep -c '^check_derived_landed()' tools/unattended/check-unattended.sh` runs it
  prints 1, `grep -c 'check_derived_landed "\$f"; rs_dl=\$?'` over the same file prints 1, and
  `git diff 51912ffc -- tools/unattended/check-unattended.sh | grep -cE '^\+.*(read_landing_commit|check_adv_reaches)'`
  prints 0.
  Red when: the builder inlines the predicate's test in the loop instead of calling it.
- **AC7** — When `sed -n 1,45p tools/unattended/check-unattended.sh` runs, its output carries both
  `check 24 EXCLUDED` and `check 24 exclusion UNAVAILABLE`.
  Red when: the header's exception TWO still names checks 7 and 23 alone while check 24 prints on
  the default channel.
- **AC8** — When `grep -nE '^FLOOR_(ASSERTIONS|SHARD_8)='` runs over the suite, each value equals
  its base value plus the new block's assertion count, and `grep -c 'TOOL-dFinishedRecord-1'` over
  the suite prints at least 1.
  Red when: the arms land and either floor stays at its base value.
  figure: the base values 1133 and 208 are PINNED at `51912ffc`; the designed count is 7, and the
  raise is DERIVED from the block as written.
- **AC9** — When `bash -n tools/unattended/check-unattended.sh` runs it exits 0, and
  `grep -c $'\r' tools/unattended/check-unattended.sh` prints the same count before and after the
  edit.
  Red when: a text-mode edit turned a bare CR inside an awk regex into a newline.
  figure: the count is 4 at base, PINNED on 2026-11-05 in this worktree.
- **AC10** — When `grep -n '^KIT_UNATTENDED_VERSION=' tools/unattended/check-unattended.sh` runs at
  the pass's commit it prints `1.113`.
  Red when: the pass bumped the version by hand instead of leaving it to the lander's `mint`.
  figure: 1.113 is PINNED at `51912ffc`.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/check-unattended.test.sh · covers AC1 AC2 AC3 · arms A to C after the check 24 roster block in region 8, A and C red on the parent leg, B red on the staged break rs_dl=0, C also red with the rs_unavail guard deleted · FLOOR_ASSERTIONS and FLOOR_SHARD_8, each by the block's executed count

The suite runs as its eight shards at the close, after the last unit is terminal, and the full bar
runs at the landing.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-05 · initial draft, from the owner-answered brief, the leg, its suite and the kit
  library read at base `51912ffc`, and a read-only reading of dConvergedCharter's record against
  the advertised tip.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "skip a finished run record whose landing commit is on
the advertised tip when grading roster amendments"` reported every present layer scanned and ranked
name-stem neighbours only: `run`, `records`, `skip`, `roster`, `check_landed_facts_due` and
`extract_run_facts`. None of them reads a run record's phase against the remote. The seam was read
directly, and this unit extends it: `check_derived_landed` in
`tools/unattended/check-unattended.sh`, called the way check 23's exclusion block calls it.

The recall probe returned TOOL-aSightedSkeptic-13's spec, whose §3 names this loop's skip shape as a
follow-up. It also returned PLAY-dClosedLoop-27 in `memory/DECISIONS.md`, the same class in the
dClosedLoop packet's re-pin guard, and TOOL-dDerivedDocket-22's acceptance ledger, which introduced derived
LANDED. The hit was STALE on two facts: TOOL-aSightedSkeptic-13 calls the check "check 22" at lines
3434 to 3437. At base the loop is at lines 4186 to 4309 and every `fail` in it is `fail 24`. The
code was taken over the record.

Recall terms used: check 24 rescope item add roster derived LANDED landing commit advertised tip in-place LANDING exclusion

The question passed with them: "why does check 24 keep grading a run record that landed in place".
