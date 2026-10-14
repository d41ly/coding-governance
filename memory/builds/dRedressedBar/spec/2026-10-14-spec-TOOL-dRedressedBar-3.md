# TOOL-dRedressedBar-3 — the govkit selftest's 56 reds, traced to four root causes and re-armed

**Status:** CLOSED · rev-3 · 2026-10-14 · node d · Tier-1 · base ebce889c · streams tooling · order 2 · ratified 2026-10-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md](../build/2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md) | research | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 |
| [2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md](../prompts/2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md) | research | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 |
| [2026-10-14-prompt-TOOL-dRedressedBar-3-2-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-3-2-revision.md) | research | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-3-3-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-3-3-spec-writer.md) | journal | — |
| [2026-10-14-review-TOOL-dRedressedBar-1-9-spec-audit-round1.md](../reviews/2026-10-14-review-TOOL-dRedressedBar-1-9-spec-audit-round1.md) | spec-audit | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 |

<!-- /gen:spec-records -->

## 1. Goal

`govkit selftest` reads 56 failures in the full bar with self-tests over `ebce889c`, and the
standalone run reproduces them. They trace to four causes, each a landing that moved code under a
fixture which no bar re-ran. This unit re-arms each fixture against the code as it stands, so the
suite grades its subjects again. Three arms of one cause witness a product defect, which
`TOOL-dRedressedBar-9` fixes. This unit leaves those three arms unscoped, so they read green only
over that fix.

## 2. Scope (IN)

- **S1** — The `[-PV]` cascade, 46 arms. The PV gov fixture's shared template text `_pvCAP_T`
  (`tools/govkit/selftest.py:14077`), written as `tier2-review.template.js` and both drift-audit
  templates (lines 14096-14098), gains the owner's `const AGENT_TYPE_SHAPE = ` line. The line is read
  at run time from `tools/workflows/tier2-review.template.js`, the owner the parity arm names, and is
  never typed. Observed by AC1.
- **S2** — aQuenchedHarness-3, 2 arms. The fixture's `deploy.toml` kits line (line 15293) and its
  `--kits` argument (line 15306) add `kickoff-manifest`. Its `[answers]` table gains the two answers
  that entry's destinations and leg read, `manifest_path` and `user_skills`, with `DEPLOY_FULL`'s
  values. Observed by AC2.
- **S3** — OC8 AC4 with the runner and OC13 AC4, 3 arms. In `check_roles_install`'s `runner` branch
  (lines 2770-2784), the deploy text's `[answers]` table gains `gate_file`. Its value is read from
  `tools/codebase-map/kit.toml`'s `[config]` `defaults` `GATE_FILE`, never typed. Observed by AC3.
- **S4** — The default-gained cluster's two `[-8]` arms, `[-8] AC1 the SECOND update` and
  `[-8] AC4 all four updates exit 0`, as §7 F1's resolution scopes them. Every writing `update` over
  the `d8-ac1` and `d8-ac4` fixtures passes `"--kits", "check-wiring"`. Those are the four calls at
  lines 8006, 8045, 8057 and 8060, numbered at the base. No other `update` call is scoped. Observed
  by AC4.
- **S5** — The cluster's other three arms, `and re-stamps the receipt at the new commit`,
  `[-12] AC4 NEGATIVE` and `[-12] AC9 NEGATIVE`, stay unscoped. Their writing calls over the `u2a`,
  `ac4` and `ac9` fixtures, lines 3299, 6886, 6900, 7064 and 7074 at the base, are unchanged. The product defect
  they expose is fixed by `TOOL-dRedressedBar-9`, not here, and the three arms are that fix's
  witness: they read green only over it. Observed by AC5.

## 3. Non-goals (OUT)

- No edit to `tools/govkit/govkit.py`, to any kit descriptor or to `tools/settings-merge.py`. Every
  red this unit re-arms is the suite's own fixture. The product defect S5's arms witness is a separate
  mechanism, and `TOOL-dRedressedBar-9` owns every product edit its fix needs.
- No scoping of the writing calls S5 names. A `--kits` scope there would stop the three arms from
  exercising the gaining path, so they would witness nothing of unit 9's fix.
- No fix for the `run-gates` an update to an older `--to` vintage gains, whose legs name files that
  vintage lacks. The owner's resolution of §7 F1 scoped the `[-8]` arms around it, and it is a
  follow-up for the owner, not a red this build carries.
- No edit to `tools/workflows/check-protocol-parity.test.sh`. Its agent-type arm is right to refuse a
  dead owner, and the PV fixture now gives it a live one.
- No change to `DEPLOY_REGISTRY_DEFAULT` itself. The `gate_file` answer is needed only where a runner
  is declared, and the constant feeds arms that declare none.
- No scoping of the read-only `update` calls at lines 3288, 3294 and 3311, or of `_p9c` at line 7088.
  Each reads green today and writes nothing the five arms read.
- No `ASSERTION_FLOOR` move and no new arm. Every arm here exists and is re-armed. The arm
  reproducing the narrow-receipt update is unit 9's.
- No kit version bump. govkit ships to no adopter, and `TOOL-dRedressedBar-7` measures the tree.

### Edges

- **hands-off** `TOOL-dRedressedBar-7` — the root-cause fixes to the govkit selftest land in a file
  no kit ships, so this unit leaves that unit no bump to make for it.
- **consumes-from** `TOOL-dRedressedBar-9` — its fix to a gained `settings-merge` whose adopter
  refuses without `agent-cap`. Without it, the three arms S5 leaves unscoped stay red and AC5 cannot
  pass, so this unit's order follows unit 9's.
- **hands-off** `TOOL-dRedressedBar-10` — what the round-1 spec audit found this spec cannot say
  (report ids 6, 10 and 16). AC2 reads no line of S2's fixture edit. AC5's guard regex cannot match a
  call scoped with `--kits`. §4's S5 paragraph restates unit 9's defect and contradicts it. That unit
  observes S2 and S5 in `tools/govkit/selftest.py` over the file this unit leaves, and corrects the
  paragraph to a pointer at unit 9.

## 4. Design

Each cause was read from the bar's `govkit selftest` leg log, kept under the profiling worktree's
git directory, and re-derived against the code at `ebce889c`. The counts are 46, 2, 3 and 5, which sum to the 56 the
log's summary names.

**S1, the PV cascade.** TOOL-aOrientedCast-4 (`e08135112`) gave
`tools/workflows/check-protocol-parity.test.sh` its agent-type arm (lines 420-491). The arm reads
the owner `tier2-review.template.js`, and when the owner yields no literal on a line declaring
`const AGENT_TYPE_SHAPE =` it prints `agent-type shape DEAD PROBE` and exits 1 (line 467). The PV
fixture copies that real parity script into its gov fixture (line 14114), but its owner template is
`_pvCAP_T`, `// a fixture harness, fan-out cap {{FANOUT_CAP}}`, which TOOL-aRepatriatedFork-7 wrote
before the arm existed. So every PV block 1 stops with `STOP: the parity check did not grade the
harness green`, and the other 45 arms read `STOP: block 1 has not finished clean` after it. The
parity population takes every tracked `*.template.js` directly in the kit (lines 436-448), so the
same line in the two drift-audit templates, which share `_pvCAP_T`, supplies the two copies the arm
also requires (line 487). Probed at spec time: the awk at lines 450-453, run over three files holding
`_pvCAP_T` plus the owner's line, prints three hits of the one literal
`/^[A-Za-z][A-Za-z0-9_-]{0,63}$/`. The fixture reads the line as the first `^const AGENT_TYPE_SHAPE = `
line of `tools/workflows/tier2-review.template.js`, so the fixture and the owner cannot drift. If block
1 stops on a further cause once this one clears, that cause is new evidence and goes back to the main
loop.

**S2, aQuenchedHarness-3.** TOOL-aRoutedQuill-5 S2 made `agent-cap` require `kickoff-manifest`
(`tools/hooks/kit.toml:9`), and `apply` refuses a selection with an unmet requirement. The fixture
selects `agent-cap,settings-merge`, so the apply exits non-zero with
`'agent-cap' requires 'kickoff-manifest'`, and its liveness arm finds no engine. The fixture's own
comment already gives the rule for the earlier requirement: govkit refuses a selection that omits a
dependency. `kickoff-manifest`'s descriptor reads `{manifest_path}` and `{user_skills}`
(`tools/govkit/entries/kickoff-manifest.kit.toml`), so the fixture's answers carry both, with the
values `DEPLOY_FULL` declares. The arm's subjects, the hooks kit's withheld self-tests and their
exempt legs, do not change.

**S3, the runner apply.** With `runner=True`, the deploy carries a `[gate_runner]`, so the LEGS step
renders every selected kit's `[[gate_leg]]`. `codebase-map`'s leg is `argv = ["python", "{gate_file}"]`
(`tools/codebase-map/kit.toml:104`), and `target_context` resolves tokens from the deploy's answers
alone. The fixture declares no `gate_file`, so the LEGS step fails with
`leg 'codebase-map coverage + freshness' argv still carries gate_file after rendering`
(`tools/govkit/govkit.py:4116`). It then withholds all 28 legs, and the apply exits 1 with no
manifest written, which is OC13's `None`. The docstring says the runner block is written as govkit's
intake writes it, and intake asks for every token `needed_answers` derives. Probed at spec time,
`needed_answers` over the registry default reads `gate_file`, `manifest_path`, `playbook_path` and
`user_skills`, and the fixture lacks `gate_file` alone. The arm likely never read green: aSweptBar-1
recorded `OC8 AC4` red at `53b25884`, before this build's base.
UNVERIFIED: whether the AFTER step, which runs the target's own runner over the now-written manifest,
leaves every new leg green or exempt. A spec-time probe of the apply queued behind the host
turnstile and was stopped unfinished, so it was not left beside the bar running on this host. A red
it reports is new evidence for the main loop.

**S4 and S5, the default-gained cluster.** TOOL-aRoutedQuill-5 S4 made a writing `update` install every
entry the registry's default set gained since the receipt's `gov_commit`, unless the run passes
`--kits` (`tools/govkit/govkit.py:8863-8879`, `derive_default_gained` at `:970`). The `stale_target`
and `delta_target` fixtures apply `--kits check-wiring` and rewind the receipt to `24f39915` or an
older `V8` vintage. Probed at spec time through the engine's own functions: the update to HEAD gains
`run-gates`, `check-microformats`, `agent-cap`, `settings-merge` and `roles`, and the requirement
filter leaves `run-gates` and `settings-merge`. The update to `9ddcc5c9` gains `run-gates`. The log
shows what follows. To HEAD, `default-gained settings-merge: adopter exit 2` fails the run, so it
neither exits 0 nor re-stamps. To `9ddcc5c9`, the gained `run-gates` declares legs naming
`check-receipt.py` and `held_halves.py`, which that vintage does not hold, and the run reports 2
problems. None of the five arms is about gaining. Each grades `check-wiring`'s rows: a re-stamp, the
dirty scope, a committed deletion, and a delta kept across vintages.

The owner's resolution of F1 as (c) splits the cluster by cause. The two `[-8]` arms red on the
`run-gates` gained at `9ddcc5c9` (`V8[3]`, line 7956), which no `settings-merge` fix reaches. So S4
gives their four writing calls the scope the arm already assumes, and `update` gives a `--kits` run
an empty gained set (`tools/govkit/govkit.py:8868`). The last call in the `d8-ac4` loop, line 8060,
carries no `--to`, so it updates to HEAD and would also gain `settings-merge`. The same scope covers
it, so `[-8] AC4` grades the delta and never unit 9. The other three arms update to HEAD only, where
the failure is `settings-merge`'s adopter alone, so S5 leaves them unscoped as unit 9's witness. The
paired halves at lines 6886 and 7064 stay unscoped beside their negatives, so each pair still differs
in one input only, the dirt.

**S5, the exposed defect, fixed by unit 9.** `settings-merge`
(`tools/govkit/entries/settings-merge.kit.toml`) and `agent-cap` (`tools/hooks/kit.toml:102-108`)
share one adopter argv, `python {prefix}/settings-merge.py`, which wires the built-in `agent-cap.js`
entry and refuses when that file is absent (`tools/settings-merge.py:1040-1052`). `apply` runs a
requirement-complete selection, so the two always arrive together there. `update`'s gaining drops
`agent-cap` alone for its unmet requirement and keeps `settings-merge`. So any receipt that does not
claim `kickoff-manifest` fails every writing update. `TOOL-dRedressedBar-9` fixes that, by a
mechanism its own spec chooses. This unit changes nothing for S5. It holds the three arms' calls as
they are and observes them over unit 9's fix.
UNVERIFIED: that the three arms read green once unit 9's fix lands. At the base the log shows only
the `settings-merge` adopter failing those updates, and a further red behind it, such as the gained
`run-gates` to HEAD, would surface only after that failure clears. A red there is new evidence for
the main loop, not a scope this unit widens.

### Files touched (estimate)

- `tools/govkit/selftest.py`

### Alternatives rejected

- S1 typing the regex literal into `_pvCAP_T`: a second copy of the owner's value, which drifts the day
  the owner's shape changes and turns the arm into a comparison of two fixtures.
- S1 giving only `tier2-review.template.js` the line: the arm then finds no copy and exits 1 with
  `no copy of the owner's literal was found` (line 488).
- S3 adding `gate_file` to `DEPLOY_REGISTRY_DEFAULT`: it changes the input of every arm that applies
  the registry default, and none of them renders legs.
- S3 having govkit skip legs of a kit its hole leaves inert: a product change. The hole's own `why`
  (`tools/codebase-map/kit.toml:113`) names an absent leg scoring green as the danger.
- S5 scoping the three HEAD-bound arms too, F1's option (a): it greens them without the fix, so no
  existing arm would witness unit 9. The owner chose (c).

## 5. Acceptance criteria

- **AC1** — When `grep -n 'AGENT_TYPE_SHAPE' tools/govkit/selftest.py` runs, its hits show `_pvCAP_T`
  built from the first `^const AGENT_TYPE_SHAPE = ` line of `tools/workflows/tier2-review.template.js`,
  read at run time. No hit carries the literal `{0,63}`. When the parity awk at
  `tools/workflows/check-protocol-parity.test.sh:450-453` runs over three scratch files holding the
  value that line builds, it prints three hits with one distinct literal.
  Red when: `_pvCAP_T` carries no shape line and the parity script prints `agent-type shape DEAD PROBE`.
- **AC2** — When `python tools/govkit/govkit.py apply --target <t> --kits agent-cap,settings-merge,kickoff-manifest`
  runs against a scratch target whose `deploy.toml` is the fixture's text as S2 leaves it, it exits 0
  and the target holds `tools/hooks/agent-cap.js`. The same call with `--kits agent-cap,settings-merge`
  prints `'agent-cap' requires 'kickoff-manifest'` and exits non-zero.
  Red when: the selection omits `kickoff-manifest`, or the answers omit `manifest_path` or
  `user_skills` and the apply names the unresolved token.
  fixture: a fresh `git init` target under `%TEMP%/<short-name>`, never inside the worktree.
- **AC3** — When `grep -n 'gate_file' tools/govkit/selftest.py` runs, it shows the runner branch of
  `check_roles_install` adding the answer from `tools/codebase-map/kit.toml`'s `GATE_FILE` default.
  When `govkit.py apply --target <t>` runs over a scratch target holding that runner deploy and the
  copied `AGENTS.md`, its output carries no `still carries gate_file after rendering` line and no
  `WITHHELD from` line, and the target holds a written `tools/gate-legs.json`.
  Red when: the answer is absent and the LEGS step withholds every leg over the one unresolved token.
  cost: the apply runs the target's runner, which waits at the host turnstile behind any bar already
  running on the node; observed at spec time.
  fixture: a fresh `git init` target under `%TEMP%/<short-name>`.
- **AC4** — When `grep -nE 'run\("update", "--target", str\((t8|t84)\)' tools/govkit/selftest.py`
  runs, every printed line carries `"--kits", "check-wiring"`, and it prints the four calls S4 names.
  A probe that imports `tools/govkit/govkit.py` prints `derive_default_gained` for a receipt claiming
  `check-wiring` at `24f39915` with `to_commit` `9ddcc5c9`, and its list holds `run-gates`.
  `grep -n 'if kits else derive_default_gained' tools/govkit/govkit.py` hits the line that gives a
  `--kits` run an empty gained set.
  Red when: a `[-8]` writing call stays unscoped, gains `run-gates` at `9ddcc5c9`, and the run
  reports the problems naming `check-receipt.py` and `held_halves.py`.
  figure: the four calls are PINNED, counted at `ebce889c`; the gained set is DERIVED from the
  registry at both vintages at observation.
- **AC5** — When `grep -nE 'run\("update", "--target", str\((up|u4|u9)\), "--write"\)' tools/govkit/selftest.py`
  runs, no printed line carries `--kits`. When `python tools/govkit/govkit.py update --target <t> --write`
  runs over a tree holding `TOOL-dRedressedBar-9`'s fix, against a target built as `stale_target`
  builds one (line 3237: `apply --kits check-wiring`, the receipt rewound to `OLD` by
  `write_vintage_receipt`, then settled), it exits 0, and the receipt's `gov_commit` in
  `.governance/install.json` is the gov HEAD.
  Red when: unit 9's fix is absent, and the update exits non-zero on
  `default-gained settings-merge: adopter exit 2`, which is what the base prints.
  fixture: a fresh `git init` target under `%TEMP%/<short-name>`, built only after unit 9 has landed
  on the branch; the tree holds no such target today.

## 6. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms`

New arm: tools/govkit/selftest.py · covers AC1 · drop the owner's line from `_pvCAP_T` and the first PV block-1 arm reds on `agent-type shape DEAD PROBE`, with 45 more cascading · none
New arm: tools/govkit/selftest.py · covers AC2 · remove `kickoff-manifest` from the aQuenchedHarness-3 selection and its apply arm reds on the unmet requirement · none
New arm: tools/govkit/selftest.py · covers AC3 · remove the `gate_file` answer and OC13 AC4 reads `None` for the manifest · none
New arm: tools/govkit/selftest.py · covers AC4 · remove the scope from the `d8-ac1` write at line 8045 and `[-8] AC1 the SECOND update` reds on the problems the gained `run-gates` reports · none
New arm: tools/govkit/selftest.py · covers AC5 · run the suite over a tree without `TOOL-dRedressedBar-9`'s fix and `and re-stamps the receipt at the new commit` reds on the old `gov_commit` · none

## 7. Open questions

- **F1 — How are the five default-gained arms re-armed, and who fixes the defect they expose?**
  RESOLVED (owner, 2026-10-14): (c). S4 scopes the two `[-8]` arms with `--kits check-wiring`, and
  `TOOL-dRedressedBar-9` fixes the defect, which the three arms S5 leaves unscoped witness.
  The arms red because `update` now gains `run-gates` and `settings-merge` into fixtures receipted
  before the default widened. `settings-merge`'s adopter then refuses without `agent-cap`, and the
  gained `run-gates` at `9ddcc5c9` names files that vintage lacks.
  - (a) Scope each writing update over those fixtures with `--kits check-wiring`, as S4 states. The
    arms grade `check-wiring` again, all five go green in this unit, and S5's defect goes to the owner
    as a recorded finding. The cost is that no arm witnesses the defect until a product unit adds one.
  - (b) Leave the arms unscoped, and ADD a product unit by M2 that fixes the gaining defect, for
    example by giving `settings-merge` no adopter of its own or by leaving it out of the gained set
    when `agent-cap` is left out. The three arms updating to HEAD would then witness the fix. The
    `[-8]` arms would still red, because a gained `run-gates` at an older `--to` vintage is a separate
    limitation, so they need (a)'s scope either way. It changes a kit contract or the deployer's
    gaining rule, which is an owner turn, and whether those three arms then read green is UNVERIFIED.
  - (c) Both: (a) for the `[-8]` arms, and (b) for the other three.
  Recommendation: (a). It is the only option whose acceptance this unit can observe in full, and it
  leaves one follow-up, the S5 finding, which the owner can schedule as its own unit with the
  witnessing arm that unit would add. (b) and (c) each need a new unit and a kit-contract change
  before this unit can close.

## 8. Revision log

- rev-1 · 2026-10-14 · initial draft. The four causes were traced from the bar log and re-derived at
  `ebce889c`. The brief's symptoms map onto them in full: 46, 2, 3 and 5 arms.
- rev-2 · 2026-10-14 · §1 · S4 · S5 · §3 · §4 · AC4 · AC5 · §6 · §7 · the owner resolved F1 as (c).
  S4 now scopes only the four `[-8]` writing calls, at lines 8006, 8045, 8057 and 8060. S5 stops
  being a recorded finding: it holds the other three arms unscoped as the witness of
  `TOOL-dRedressedBar-9`'s fix, observed by the new AC5. AC4 drops the HEAD-bound calls and probes the
  `9ddcc5c9` gain instead. Edges trade the external hand-off for consumes-from unit 9, the order moves
  from 1 to 2, and the header carries `ratified 2026-10-14`.
- rev-3 · 2026-10-14 · §3 · Edges gain the hands-off to TOOL-dRedressedBar-10, the batch the round-1
  spec audit's minors were promoted into, for report ids 6, 10 and 16. No scope, design or criterion
  moves.

## 9. Reuse audit

`tools/codebase-map/reuse_lookup.py "re-arm a suite fixture a landing disarmed so the arm grades its
subject again"` returned name-stem neighbours only, `arm`, `fixture`, `build_fixture` and `run_arms`.
None is a seam for a fixture input inside an existing arm, so no existing seam fits as a helper and
this unit mints none. The seams it reads instead of typing are the engine's own: `needed_answers` and
the codebase-map descriptor's `GATE_FILE` default for S3, the owner template for S1, `DEPLOY_FULL`'s
answers for S2, and `update`'s documented `--kits` scope for S4. The gotchas checklist for
`tools/govkit/selftest.py` selects `fixture-lacks-a-gate-the-consumer-has`, which is S1's class, and
`fixture-inherits-ambient-machine-state`. The recall probe returned TOOL-aSweptBar-1, whose non-goals
attributed `OC8 AC4` and the re-stamp arm to aOrientedCast with the cause UNVERIFIED. This unit traces
them to S3 and S4 instead. The brief and the code agree on every symptom. The brief's `outside the
selection` wording for aQuenchedHarness-3 is S2's unmet requirement. At rev-2 the three arms S5
holds are reused as unit 9's witness rather than scoped and replaced by a new arm.

Recall terms used: `python tools/memory-recall/query.py "why do suite arms go red after a bar-less
landing moves the code under them, and how were they re-armed" --terms "bar-less landing stale
fixture re-armed probe marker WHOLE_RUN GATE_SELFTESTS cleared default-gained verb offender pin"`
