# TOOL-aShelvedLeg-1 — the `unattended kit gate` leg is `subject = "kit"`, off every automatic bar

**Status:** SPECCED · rev-1 · 2026-11-10 · node a · Tier-2 · base b904a0f9 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-prompt-TOOL-aShelvedLeg-1-brief.md](../prompts/2026-11-10-prompt-TOOL-aShelvedLeg-1-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The `unattended kit gate` leg runs `check-unattended.sh` on no automatic bar, merge or push, in gov
or in an adopter's tree, and still runs whenever someone asks for it. Its wall on node a is the
longest of most bars, 2039 s on the aSwiftRefusal branch bar and up to 3147 s in node a's retained
run records, so every bar stops paying it. The
owner chose this on 2026-11-10, knowing the price: a held leg cannot notice its own drift
(TOOL-aBoundedCeiling-10).

## 2. Scope (IN)

- **S1** — The leg's row declares `subject = "kit"` in `tools/unattended/kit.toml` and
  `"subject": "kit"` in `tools/gate-legs.json`. Every other key of both rows is unchanged, the
  `declarations` chunk and the 16040 s ceiling included. Observed by AC1 and AC2.
- **S2** — `tools/govkit/subject-pins.tsv` is regenerated with
  `python tools/govkit/govkit.py selfcheck --write`, so its row for the leg reads `kit` beside the
  unchanged `declarations` chunk and the move shows in the diff. Observed by AC2.
- **S3** — `tools/run-gates/selftest-budgets.txt` gains a row for the leg, because every held leg
  must carry one (§4, Evidence). Its argv field is blank, so the argv comes from the manifest, and
  its budget is 4721. Observed by AC3.
- **S4** — The descriptor records the ruling beside the leg. A comment above the leg's
  `[[gate_leg]]` row names the owner ruling of 2026-11-10 and this unit, and says the leg is `kit`
  by that ruling and not by the subject criterion in `run-gates.sh`. It names the price,
  TOOL-aBoundedCeiling-10, and the two on-demand routes. The block at `kit.toml:220`, which says
  the legs below stay on the bar and cost seconds, is corrected to except this leg. Observed by AC5.
- **S5** — Each sentence in the unattended kit saying this leg is a merge-bar leg is corrected:
  `run-unattended-gates.sh` lines 8, 419 and 559, and the `check-unattended.sh` line of
  `tools/unattended/README.md` under "Running the kit's own checks". Observed by AC6.

## 3. Non-goals (OUT)

- Making `check-unattended.sh` faster, or scoping its checks to what a commit moved. That is
  TOOL-dThriftyLanding-7, which stays open.
- A per-repository override of the hold. An adopter's bar holds the leg after its next
  `govkit update`, by the owner's "Every bar" answer in the brief.
- Any other leg's subject or chunk.
- Changing what the self-test variable runs, the hold predicate in `run-gates.sh`, or its
  `GATE held` wording. That line says "(self-test, ...)" for every held leg, this one included,
  although this leg reads records rather than a checker's source.
- `BUDGET_kit_gate=660` in `run-unattended-gates.sh:318`, the `--checks` half's own cost ceiling,
  which the recent readings exceed. That is a cost question, TOOL-dThriftyLanding-7's.
- A `tools/run-gates/windows-only-legs.txt` row. Its bar is a suite whose arms exercise Windows
  only, and this leg is no suite. It runs in the WSL half of a split held tier, as every unlisted
  held leg does.
- The kit version bump: the lander's `mint` moves it.

### Edges

- **hands-off** external — the next-steps text `adopt-unattended.sh` prints at `:1178` tells a
  hand-wiring adopter to add `bash $KIT_REL/check-unattended.sh` to its gate manifest and names no
  subject, so a hand-wired copy still runs the leg on every bar. A govkit-installed adopter
  receives the row with its subject. This is the gap DEPL-aBenchedProbe-5 closed for the lander
  self-test, and the main loop files it as an ask rather than widening this unit.

## 4. Design

### Evidence

All read at base b904a0f9.

- **The hold already exists.** `run-gates.sh:3249-3251` writes `ondemand` for a leg whose subject is
  `kit` or whose chunk is `selftests`, unless the self-test variable is set. `report_one` prints
  `GATE held  <name>` for it (`:4166-4167`), and the summary counts it (`:5413`). No new switch is
  built.
- **The criterion says `repo`.** `run-gates.sh:2929-2934` states it once: ask what a failure of
  the leg means, and "this repository is misconfigured" is `repo`. This leg reads run-state
  records, guides and the remote, so by that criterion it is `repo`. It becomes `kit` by the
  owner's ruling, and S4 writes that beside the row.
- **Three declarations must agree.** govkit's check 7h fails when the descriptor's subject and
  the manifest's disagree (`govkit.py:2599-2602`). Check 7h2, the subject pin ratchet, fails
  when a live subject moves without its pin (`govkit.py:2773-2781`), printing that the leg moves
  off the automatic bar. S1 and S2 move all three in one commit.
- **A held leg needs a budget row.** `run-selftests.sh --check`, the leg
  `every held leg is budgeted, every budget row resolves` (`gate-legs.json:1926`), fails for any
  held leg with no row in `selftest-budgets.txt` (`run-selftests.sh:944-961`). The brief missed
  this, and S3 closes it.
- **The push boundary holds it too.** `.githooks/pre-push:1653` compares a recorded green's
  `selftests` key only when the pusher set the self-test variable, and `tools/push-main.sh` never
  sets it. CI's `bar` job runs on push without it (`.github/workflows/remote-ci.yml:103-136`).
- **On demand stays on demand.** `run-unattended-gates.sh:549` runs `check-unattended.sh` in its
  `--checks` half, untouched. A bar with the self-test variable set runs every held leg. The
  unattended driver tells an operator to export it into a close whose range touches a declared
  self-test surface (`unattended.sh:10832`), which is that same request.
- **CI's daily held sweep gains the leg.** The `held-plan` and `held` jobs run on the daily
  schedule and on a manual dispatch, never on push (`remote-ci.yml:154-155`, `:313-315`), over
  the population `run-selftests.sh --list` resolves from the budget rows. With S3 that includes
  this leg. That job is no merge or push bar, and `run-unattended-gates.sh:24-27` already counts
  it as the after-landing check for every held suite. It runs on a hosted runner, not on node a.
- **Unaffected checks.** govkit's 7c2 grades only guarded bar legs (`govkit.py:2364`), and this leg
  carries no guard in the manifest. 7j4 grades self-test-shaped legs, and this leg's chunk is
  `declarations` and its argv names no test file. `held_halves.py:77` reads the same predicate and
  sends the leg to the WSL half.

### The budget

`selftest-budgets.txt` sizes a row as its worst observed reading times 1.5. The five retained
run-record readings of this leg on node a, taken from the common git dir's `gate-run` records on
2026-11-10, are 707, 772, 1290, 1308 and 3147 s; the worst ran beside six foreign gate processes.
3147 x 1.5 = 4721, PINNED at that date. The reading field says so, in the shape of the other rows:

```
unattended kit gate	4721		worst of 5 retained gate-run readings on node a 2026-11-10, 3147s beside six foreign gate processes, x1.5. TOOL-aShelvedLeg-1 held it by owner ruling
```

The budget is a cost verdict and never the hang bound. The hang bound stays the manifest ceiling,
16040 s.

### The pins

`selfcheck --write` regenerates the whole file from the manifest. Only the leg's row moves, from
`repo` to `kit`, with `declarations` unchanged. If the builder's role hook refuses that command, a
hand edit of that one row writes the same bytes, and the close's `govkit selfcheck` leg proves
it.

### Inventory

No identifier is minted. The budget row's name is the leg's existing name.

### Files touched (estimate)

- `tools/unattended/kit.toml`
- `tools/gate-legs.json`
- `tools/govkit/subject-pins.tsv`
- `tools/run-gates/selftest-budgets.txt`
- `tools/unattended/run-unattended-gates.sh`
- `tools/unattended/README.md`

### Alternatives rejected

- **`chunk = "selftests"` instead.** It also holds the leg, but the chunk names what kind of leg it
  is, and this leg is no self-test. The owner's question and answer were about the subject.
- **Removing the leg from the manifest**, as the 2026-08-23 ruling did for the kit's self-tests.
  A bar with the self-test variable set would then never run it, and every govkit-installed adopter
  would lose it from its manifest. The brief requires both routes to stay.
- **A new environment switch for this one leg.** The hold this needs already exists, and a second
  switch is a second answer to one question.

## 5. Production-readiness checklist

- security — no input, write path or surface; the leg's argv and its remote read are unchanged.
- perf / scale — a merge or push bar stops paying the leg, 707 to 3147 s on node a's retained
  readings. CI's daily held sweep gains it, on a hosted runner.
- error / empty / loading states — N/A: no code path changes; the hold's output already exists.
- observability — a default bar prints `GATE held  unattended kit gate` and counts one more held
  leg in its summary.
- risks — TOOL-aBoundedCeiling-10: the leg can go red on main with nothing reporting it until
  someone runs it, as it did in August 2026 (TOOL-aBoundedCeiling-9). The owner accepted that.
  Under `GATE_SELFTESTS=changed` the leg selects by the unattended kit's shipped sources
  (`run-gates.sh:3076-3080`), so a records-only change can hold it as unchanged; a plain
  self-test run does not.
- testing — AC1 to AC6, all probes of the changed files. The close's bar re-observes S1 to S3
  through the legs §7 names.
- migration — N/A: an adopter takes the new subject at its next `govkit update`.
- user docs — the kit README's "Running the kit's own checks" (S5). No page under `help/`
  describes held legs.

## 6. Acceptance criteria

- **AC1** — When `held_halves.py` partitions the held tier, it names the leg and counts one
  more held leg than at base:
  ```
  python tools/run-gates/held_halves.py --partition --half all --out <scratch>/held.json
  grep -c '"name": "unattended kit gate"' <scratch>/held.json
  ```
  The grep prints 1, and the announce line reads `75 leg(s)`.
  Red when: the manifest row keeps `"subject": "repo"`. At base the grep prints 0 and the line
  reads `74 leg(s)`, observed 2026-11-10 when this spec was written.
  figure: 74 is PINNED at base b904a0f9; a leg another build adds moves both counts together.
- **AC2** — When the probe below reads all three declarations, it prints
  `kit kit kit declarations`:
  ```
  python -c "import tomllib,json;n='unattended kit gate';k=[l['subject'] for l in tomllib.load(open('tools/unattended/kit.toml','rb'))['gate_leg'] if l['name']==n];m=[l for l in json.load(open('tools/gate-legs.json',encoding='utf-8')) if l['name']==n];p=[r.rstrip('\n').split('\t') for r in open('tools/govkit/subject-pins.tsv',encoding='utf-8') if r.startswith(n+'\t')];print(k[0],m[0]['subject'],p[0][1],p[0][2])"
  ```
  Red when: any one of the three still reads `repo`, or the pin's chunk moved. At base it prints
  `repo repo repo declarations`.
  permission: the close's `govkit selfcheck` leg re-observes the agreement; a role agent may not
  run it.
- **AC3** — When `awk -F'\t'` selects the row of `tools/run-gates/selftest-budgets.txt` whose
  first field is `unattended kit gate`, its budget is 4721 and its argv field is empty.
  Red when: the row is absent, which makes `run-selftests.sh --check` print the leg under "these
  HELD legs carry no budget row".
  permission: the `--check` run is a runner a role agent may not execute; the close's leg
  `every held leg is budgeted, every budget row resolves` observes it.
- **AC4** — When `git diff b904a0f9 -- tools/run-gates/run-gates.sh .githooks/pre-push` runs, it
  prints nothing, and `grep -c 'run_one "kit gate"'` over `tools/unattended/run-unattended-gates.sh`
  prints 1, with that row's argv still `bash "$HERE/check-unattended.sh"`.
  Red when: the hold predicate, the push hook or the `--checks` row is edited, which would change
  what the self-test variable or `--checks` runs.
- **AC5** — When `grep -n 'TOOL-aShelvedLeg-1'` runs over `tools/unattended/kit.toml`, a hit sits
  in the comment directly above the leg's `[[gate_leg]]` row, and that comment also names
  TOOL-aBoundedCeiling-10, `run-unattended-gates.sh --checks` and the self-test variable.
  Red when: the comment is missing, or it sits anywhere but above that row.
- **AC6** — When `grep -cE 'stay merge-bar legs|ALSO merge-bar legs|stay on the merge bar'` runs
  over `tools/unattended/run-unattended-gates.sh`, it prints 0, and the `check-unattended.sh` line
  in the code block of `tools/unattended/README.md` says the leg is held off the bar.
  Red when: any of the three phrases survives. At base the grep prints 3.

## 7. Gates

`govkit selfcheck` · `every held leg is budgeted, every budget row resolves` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `docs` · `lexicon naming predicates` · `routed commits name a specced unit` · `brief-recorded` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

The first two re-observe S1 to S3 at the close: `govkit selfcheck` fails on a pin left at `repo`,
and the budget leg fails on a missing row. The last eight are owed because a file in §4's estimate
trips their guards; each is held on a default bar, and the close runs them only if it asks for the
held tier. The close's bar output also shows the change itself: one more held leg, and a
`GATE held` line for this leg where base ran it.

No new arm: the unit adds and moves no suite arm. The two legs above are existing gates whose
failing case is the staged break each AC's "Red when" names.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft.

## 10. Reuse audit

The seam is the bar's existing hold: `run-gates.sh:3249-3251` holds a leg whose subject is `kit`,
and the unit changes data the hold already reads, plus the two declarations govkit grades beside
it. `python tools/codebase-map/reuse_lookup.py "hold a gate leg off the automatic bar so it runs
only on demand"` returned only name-stem neighbours (`run`, `legs`, `leg`, `check_gate_wall`), and
none of them holds a leg. The hold is a predicate inside the runner rather than a symbol, so the
probe does not reach it, and the source citation above is the evidence. Recall agreed with the
source: TOOL-aBenchedProbe-1 declared three hook self-tests `subject = "kit"` for cost, which is
the precedent this unit follows, and TOOL-aBoundedCeiling-10 is the price. Recall also returned
DEPL-aBenchedProbe-5, the hand-wired runbook gap, which is this unit's external hand-off.
`gotchas.py --for-paths` over the estimate selected `a-new-leg-trips-a-growing-set-of-meta-gates`,
which is how the budget-row requirement in S3 was found, and
`a-folded-field-leaves-its-row-shape-docs-behind`, which S5 answers.

Recall terms used: `python tools/memory-recall/query.py "how is a slow repository gate leg taken off
the merge bar and run only on demand" --terms "subject kit held leg GATE_SELFTESTS on demand merge
bar unattended kit gate check-unattended cost"`
