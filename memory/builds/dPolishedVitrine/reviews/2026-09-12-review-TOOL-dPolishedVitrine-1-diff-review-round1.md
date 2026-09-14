**Serves:** diff-review TOOL-dPolishedVitrine-1

# dPolishedVitrine — Tier-2 diff review, round 1

*Node `d`, 2026-09-12. An adversarial pass over the branch diff of `TOOL-dPolishedVitrine-1`, the unit
that renders the unattended build harness at install. The shape was four primed finder lenses, four
skeptic batches prompted to REFUTE each finding, and one synthesis. The hunt brief named seven
things to look for: a consumer update that rolls back or leaves a stale render, a render that
differs from gov's dogfood file beyond the comments, a probe that guesses, a placeholder surviving a
render, a kit-version marker missed, a test arm that cannot fail, and a BAN-list ratchet that grew.
Every `file:line` below was re-opened at the tip in this worktree before it was written down. The
fixture reproductions quoted are the skeptics' own, and where this synthesis ran something itself,
the finding says so.*

**Range reviewed: `24f8c712...0c0e175741525d0dfc7c836f3b22d182f0e79bd8`** (tip `0c0e1757`, branch `cld/derived-harness-paths`, 44 files, +2317/-70). Round 1.

## Verdict: BLOCKED

One BLOCKER. `update` cannot deliver this release to either consumer it exists for. Both consumers'
receipts row the harness as an `engine` file, and `update` keys on the receipt's role. So it writes
gov's `tools/`-spelled dogfood render into the consumer, which is the exact defect this unit
removes, and on the next run it reports that row `current` at exit 0. There are five distinct
defects in total: 1 blocker, 1 high, 1 medium and 2 low. Gov's own tree is correct. Its parity leg
is green and AC1 holds as pinned. Every defect sits on the path from this release to its consumers,
or on the adopter population the kit's `requires` permits.

## Review shape

Raw 12 · confirmed 10 · refuted 2 · unverified 0 · precision 0.83.

The ten confirmed findings carried four co-reported duplicate sets. Raw ids 3 and 8 are the
receipt-role defect, raw ids 4 and 7 are the regenerate ordering, and raw ids 1, 5 and 10 are the
`requires` gap. Raw ids 9 and 12 are the guard. Merging those leaves **5 distinct defects**, F1 to F5
below, and each names the raw ids it absorbs. The merge is this synthesis's, and it is separate from
the pipeline's own duplicate count in the integrity section. The severity counts in this report are
over the five distinct defects. By raw id, 3 and 8 are BLOCKER and 4 and 7 are HIGH. Raw ids 2 and 6
were refuted by their skeptics. Their text did not reach synthesis and nothing of them is carried.

Two raw findings overstated one consequence, and the text below corrects it. Raw ids 1 and 10 said a
failed regenerate rolls the review-harness kit back. It does not. The kit's `[check]` is `none`, so
post-write verification grades it `landed-unmeasured` and restores nothing (F2 and F3).

## Run integrity

- Lenses: **4/4 returned, 0 DIED.**
- Skeptic batches: **4/4 returned, 0 DIED.**
- 0 contradictory verdicts demoted to unverified · 0 spurious verdicts discarded · 0 duplicates
  removed by the pipeline.
- 0 findings left UNVERIFIED. Nothing in this report is outstanding for lack of a skeptic verdict.

The run is COMPLETE. No lens died, so the zero counts above are measurements rather than gaps, and
"no finding in area X" means the area was looked at.

One caveat about the reproductions, which does not change any count. Two skeptics, for raw ids 4
and 7, report that they ran `rm -rf` on shared scratch fixtures before isolating their own work. One
of them also committed a file into a sibling skeptic's fixture repo. Each then re-ran its
reproduction in a private directory, and the outputs quoted here come from those private runs. Any
other reproduction that used the shared directories at that time may have been disturbed. F1 and F2
each rest on at least two independent reproductions that agree, and on the code order read here, so
neither depends on a single fixture that may have been disturbed.

## Findings

| # | Sev | Where | One line | Raw ids |
|---|---|---|---|---|
| F1 | **BLOCKER** | `tools/workflows/kit.toml:61` | an existing receipt still rows the harness as `engine`, so `update` writes gov's `tools/`-spelled render into the consumer and certifies it `current` | 3, 8 |
| F2 | **HIGH** | `tools/workflows/kit.toml:73` | the new `[[regenerate]]` runs before `update` lands the template it reads, so it refuses on every introducing update and never runs again | 4, 7 |
| F3 | MEDIUM | `tools/workflows/check-protocol-parity.test.sh:96` | the `MEMORY_TREE_DIR` refusal exits 2 before any pair is graded, so a review-harness install without memory-tree, legal under `requires`, loses `REVIEW-PROTOCOL.md` too | 1, 5, 10 |
| F4 | LOW | `tools/workflows/kit.toml:86` | the parity leg now reads the memory-tree kit's `gotchas.py`, and its guard does not cover it | 9, 12 |
| F5 | LOW | `tools/workflows/check-protocol-parity.test.sh:22` | five carriers say `update` re-renders the harness, or names it stale, and it does neither without `GOVKIT_RERENDER=1` | 11 |

---

### F1 — BLOCKER · `tools/workflows/kit.toml:61` · the release cannot reach an existing consumer through `update`

`kit.toml:58-62` claims `{kit}/unattended-build.js` as a `rendered` destination from the template.
That changes what `resolve_entry` pools for `apply` and `adopt`. It changes nothing about a row that
an existing receipt already carries:

- `_cmd_update` takes each row's role from the receipt (`tools/govkit/govkit.py:6197`). It re-resolves
  a role against the descriptor only when `schema < 2` (`:6207-6218`).
- Both consumer receipts are schema 3, and both carry `scripts/workflows/unattended-build.js` as role
  `engine` with source `tools/workflows/unattended-build.js`. Read on node `d` from core's and
  NicoCares' `.governance/install.json`.
- Gov still tracks that source as its own dogfood render, as spec §4 Rollout states. In this range
  it moved from `75763c4e` to `ac362480`, so `update` grades the consumer row the way it grades any
  engine file whose source changed.
- Core's row has `oid == gov_oid == 75763c4e`, so it grids `stale` and the RAW arm writes
  `ac362480`. NicoCares' recorded `oid` is `6aa46ddb`, which is not its `gov_oid`, so by the same grid
  its row takes the three-way arm and merges gov's three comment lines into its own delta. That
  NicoCares path is derived from the receipt data and was not reproduced. Neither consumer receives
  a render.
- `ac362480` carries every literal this unit exists to remove. Checked here against the blob:
  `bash tools/unattended/unattended.sh` at `:225`, `python tools/memory-tree/gotchas.py` at `:229`,
  `tools/workflows/tier2-review.js` at `:547` and `tools/workflows/unattended-unit.js` at `:909`.

Reproduced by two skeptics, independently. Each ran `govkit apply` at `24f8c712` with prefix
`scripts`, then `GOVKIT_RERENDER=1 govkit update --write` at `0c0e1757`. Both saw
`stale [engine] …/unattended-build.js` and found gov's dogfood bytes, blob `ac362480`, written into
the consumer. One of them ran `update` a second time. That run reported the row `current`, ran
`0 argv`, re-stamped the receipt at `0c0e1757` and exited 0, and the consumer's parity leg then
printed `DRIFT` at `DRIVER` and `CHECKLIST`.

A correct manual `--render` does not reach green either. After one, the receipt still rows the path
as `engine` with oid `ac362480`, and a later `update` graded it `patched [engine]`, which was
measured. Every later gov edit to the dogfood render then grids `diverged` and three-way-merges the
`tools/` spellings back in. Core's receipt-sync leg compares the index blob of every row outside the
exempt roles against the receipt oid. `rendered` is exempt and `engine` is not, so the correct
render reds that leg.

**Why BLOCKER, when the lenses filed it HIGH.** Gov was never broken. This unit's whole deliverable is
the consumer fix, and the build README promises "One kit release fixes both adopters". The one
delivery channel the spec names re-ships the defect to both named consumers and reports `current` at
exit 0, which is a silent green on the unit's own target. No documented step reaches green either:
§3 declares that govkit is not changed, and the §3 hand-off names only `update`.

**A route nobody ran.** `adopt --re-adopt --write` re-measures from `resolve_entry`
(`govkit.py:7915-7923`), so it should re-row the path as `rendered` from the template. Both consumer
receipts already record the earlier engine-to-rendered move, the playbook fixture of
`TOOL-dRetiredFork-12`, as `rendered`. That makes the route plausible. It is not verified, and
`adopt` refuses a dirty index (`demand_adopt_index_clean`).

**Fix.** There are two repairs, and only the first is inside this unit's scope.

- Inside scope: amend spec §4 Rollout and the §3 hand-off to the sequence that actually converges.
  The candidate is `update`, commit, `adopt --re-adopt --write`, `--render`, commit. It has to be
  verified on a schema-3 fixture before any consumer is handed it.
- The durable repair, outside §3's scope: in `_cmd_update`, re-resolve every row's role against the
  current descriptor at every schema. When a non-landable rule now claims the destination, report a
  role move, rewrite the row's role and source, drop `oid` and `gov_oid`, and never take the write
  arm. That is govkit work, so it needs its own spec, and F2 belongs in the same spec. Choosing only
  this route parks F1 (see Disposition below).

**Left-shift gate.** A govkit selftest arm over a schema-3 receipt. Apply at a revision where
`{kit}/x.js` is an engine row under prefix `scripts`. Then run `update --write` at a revision whose
descriptor claims that destination `rendered` while gov still tracks `x.js`. Assert that the row's
role becomes `rendered`, that gov's source bytes are not written to the destination, and that the
verdict is neither `stale` nor `current`. The arm reds today. For the class: a selfcheck that diffs
every kit's resolved destination-to-role map between the last released vintage and HEAD, and reds
on a role change govkit does not migrate. Then the next engine-to-rendered move is caught in gov
rather than at a consumer.

### F2 — HIGH · `tools/workflows/kit.toml:73` · the regenerate runs before its input lands

The new `[[regenerate]]` argv is the parity script's `--render`. In `_cmd_update` the re-render block
is `govkit.py:6954-7053`, and the unclaimed-source landing starts at `:7091`. The template is an `A`
in gov's diff and not an `R`, because gov still tracks `unattended-build.js`, checked here with
`git diff --name-status --find-renames`. No consumer receipt names it, so the landing is its only
route into a consumer, and the render has already run by then. The render hits
`missing shipped copy` at `check-protocol-parity.test.sh:161` and `nothing was written` at `:196`,
and exits 1. The render is all-or-nothing, so `REVIEW-PROTOCOL.md` is not rendered either.

Reproduced by two skeptics at two prefixes, `tools` and `scripts`:

- Run 1 printed `ran review-harness: … --render -> exit 1 REFUSED`, and only after that
  `landed …/unattended-build.template.js`. The run takes an `r.fail`, which writes the receipt rows
  but withholds the stamp (`govkit.py:7678-7687`).
- The `r.fail` text at `govkit.py:7037-7040` promises that "post-write verification below rolls this
  run back". For this kit it cannot. The kit's `[check]` is `none` (`kit.toml:88-93`), so the verify
  loop grades it `landed-unmeasured` and `continue`s (`govkit.py:7378-7382`), and the run reported
  `rolled back 0`. Run 1's writes stay staged, including F1's re-shipped harness.
- Run 2 finds no row verdict touching the kit and no source left to land. The kit drops out of
  `touched_kits`, and the regenerate never fires: `re-render: 0 argv run`, receipt re-stamped at
  `0c0e1757`, exit 0.

No sequence of `update` runs produces the render, which contradicts spec §4 Rollout and the promise
in `kit.toml:67`.

**Why HIGH and not BLOCKER.** F2 is recoverable in a way F1 is not. With F1 fixed, the harness row is
`rendered` and exempt from receipt-sync, and the parity leg's own `DRIFT` line prints the remedy that
works, `--render`. The declared mechanism fails, but a printed fix reaches green.

**Fix.** In govkit, move the unclaimed-source landing above the re-render block. It needs only
`withdrawn_rows`, and the write loop finishes building that before `:6954`. The comment at `:7085`
says the landing "MOVES NO EARLIER THAN" the end of that loop, so the move stays inside its own
stated bound. Also run a kit's regenerate when any of its rendered destinations differs from its
template's render, not only when a row verdict touched the kit. Separately, make the `r.fail` text
depend on whether the kit's check can roll anything back, or make a failed regenerate roll its own
kit back explicitly. All three are govkit changes, so all three belong in the govkit spec that F1's
durable repair needs. Until that spec lands, the hand-off must say that the introducing update needs
a manual `--render` after it.

**Left-shift gate.** A govkit selftest arm for a kit whose `[[regenerate]]` reads a source absent
from the base receipt. Run `update --write` with `GOVKIT_RERENDER=1` and assert that the regenerate
exits 0 in the same run and the render lands. Add the negative arm: a kit with `[check] none` whose
regenerate fails must not print a rollback promise.

### F3 — MEDIUM · `tools/workflows/check-protocol-parity.test.sh:96` · one pair's refusal blocks both pairs

The probe at `:82-104` runs unconditionally, before the unpaired-template arm and before the `PAIRS`
loop, and it exits 2. `REVIEW-PROTOCOL.template.md` carries no `MEMORY_TREE_DIR` token, but its
pair is never reached. The override cannot rescue the tree, because it too demands a tracked
`gotchas.py` (`:83-91`).

The install is legal. `tools/workflows/kit.toml:7` declares `requires = ["agent-cap"]`. The agent-cap
kit requires only `settings-merge` (`tools/hooks/kit.toml:7`), and settings-merge requires nothing
(`tools/govkit/entries/settings-merge.kit.toml:8`). So govkit's `requires` enforcement admits
review-harness without memory-tree. The kits in this repo that do
depend on memory-tree declare it: codebase-map, drift-audit, memory-recall and unattended, checked
here with `grep '^requires' tools/*/kit.toml`.

Reproduced by three skeptics independently. Two built a review-harness-only fixture, and one untracked
`gotchas.py` in a full tree. Each of those trees passes at `24f8c712` and exits 2 at `0c0e1757` with
`cannot derive MEMORY_TREE_DIR`. The two fixture runs saw that exit in both `--check` and `--render`. For
that adopter the parity leg is red permanently, and `REVIEW-PROTOCOL.md`, the document that states
the concurrency cap, can no longer be rendered or graded. Under `GOVKIT_RERENDER=1`, the regenerate
exits 2 with no declared `[[outcome]]`, so that run takes an `r.fail` and withholds its stamp.
Nothing is rolled back; see the correction in the review shape.

The unit's own reasoning rules against this refusal. The spec's §3 non-goal on the driver path and
backlog row `TOOL-dPolishedVitrine-8` both decline to probe the driver because "a review-harness
adopter need not install the unattended kit, and a refusal would red their parity leg over a harness
they never run". The checklist probe applies the opposite rule to the same adopter.

**Fix.** Preferred: scope the refusal to the pairs whose template carries the token. Resolve
`MEMORY_TREE_DIR` only when a template needs it, always grade `REVIEW-PROTOCOL.md`, and report the
harness pair as a named SKIP that says the memory-tree kit's `gotchas.py` is tracked nowhere. That is
the warn-when-absent, refuse-when-misplaced shape `TOOL-dPolishedVitrine-8` proposes for the driver.
The alternative is adding `"memory-tree"` to review-harness's `requires`, so that apply refuses the
incomplete install. That is simpler, but it makes every review-protocol adopter install the
memory-tree kit for a harness only the unattended kit runs.

**Left-shift gate.** Add a review-harness-only fixture arm to `tools/workflows/unattended-build.test.sh`,
with no `gotchas.py` tracked anywhere. Assert that `--check` exits 0 after grading
`REVIEW-PROTOCOL.md`, and that the output names the harness pair as skipped. It reds today. The arm's
shape is the class rule: a refusal that belongs to one pair's token never blocks a pair that does
not use that token.

### F4 — LOW · `tools/workflows/kit.toml:86` · the guard does not cover the leg's new input

The parity leg's verdict now depends on `git ls-files` for `${TOOLROOT}memory-tree/gotchas.py` and
`${TOOLROOT}gotchas.py` (`check-protocol-parity.test.sh:93-95`). Its guard is still `{kit}/` plus the
protocol at `kit.toml:86`. Gov's manifest row, `tools/gate-legs.json:523-527`, guards
`memory/guides/REVIEW-PROTOCOL.md`, `tools/lib/` and `tools/workflows/`, and this range does not
touch that file. The other carrier of the same checklist command, the `unattended skill wiring` leg
at `tools/gate-legs.json:834-843`, has no guard and runs every time. So one command gets two kinds
of coverage.

The reach is narrow. `run-gates.sh:147-157` lets a guard scope even the authoritative push, but only
inside the pre-push hook's bounded window (`GATE_FULL_MAX_LAG=10`, `.githooks/pre-push:192`). A
deleted or renamed `gotchas.py` reds the unguarded dead-path carriers leg, and a manifest change
forces a full run. The gap bites on a directory move, such as flattening the memory-tree kit, inside
that window: the stale harness lands and is caught within ten commits.

**Fix.** Set `guard = []` in both carriers, as the wiring leg already has it. Widening the guard
instead needs a sibling-kit token that `TOOL-aCollapsedScan-11` records does not exist. A literal
would be wrong in an adopter, and widening only `tools/gate-legs.json` would make the descriptor and
the manifest disagree in content again, which `govkit selfcheck` does not compare
(`TOOL-aPacedTurnstile-12`). Editing `tools/gate-legs.json` re-stamps the kickoff manifest in the
same commit, because that file is a watched pathspec.

**Left-shift gate.** None new. This is a live instance of the under-declared-guard class that the
open row `TOOL-aPacedTurnstile-9` exists to gate. Record it there, so that the complete-guard proof,
once it lands, has a known positive to be observed red against.

### F5 — LOW · `tools/workflows/check-protocol-parity.test.sh:22` · the carriers promise a re-render the default run does not do

Five carriers state behaviour that happens only with `GOVKIT_RERENDER=1`:

- `check-protocol-parity.test.sh:21-22`: "so an update re-renders them rather than leaving either a
  vintage stale".
- `tools/workflows/README.md:28`: "`kit.toml`'s `[[regenerate]]` block re-runs the render on an
  update".
- `kit.toml:67`, the `why_no_adopter` string: "so an update re-renders them".
- `kit.toml:69-70`: "Without it `update` lands a new template and names this kit one vintage stale".
- Spec §4 Rollout, at `:187-188`: "Without the flag, `update` names both kits as one vintage stale."

In govkit, a regenerate is declined when the flag is off (`govkit.py:7008-7011`). Declines are
printed only under `if _rerender_on` (`:7045-7053`), by `DEPL-dRetiredFork-3`'s silent-when-off
criterion. With the flag off, nothing is re-rendered and nothing is named. The per-row label reads
`re-rendered` either way (`:6331-6332`), which makes the misreading easy. For review-harness,
whose check is `none`, the result is silent staleness that only the parity leg catches at the next
bar, and core does not carry that leg yet. For the unattended kit the flag-off result is worse than
"named stale". The consumer rows `SKILL.template.md` as `engine`, so the write loop lands the changed
template and leaves the rendered Skill behind. Then the post-write `adopt-unattended.sh --check` goes
from green to red, and the kit is rolled back. That is the 2026-09-11 NicoCares event, which spec §4
says the regenerate block prevents. It prevents it only with the flag set. That mechanism was read
from the code and was not run.

This is LOW because the §3 hand-off does prescribe `GOVKIT_RERENDER=1`. It is still five false
statements, and they sit in the kit's own shipped files.

**Fix.** Name `GOVKIT_RERENDER=1` in each carrier's sentence. Correct the Rollout paragraph to say
what happens with the flag off: review-harness is left stale with no output, and unattended is
rolled back by its own post-write check. Optionally, add the flag to the parity leg's `DRIFT` fix
line next to `--render`.

**Left-shift gate.** A grep arm run beside the parity leg: any tracked line under `tools/workflows/`
or `tools/unattended/` that says `update` re-renders must name `GOVKIT_RERENDER` in the same
sentence. It is cheap, it reds today, and it covers the class, since every future kit that adds a
`[[regenerate]]` block will want to write the same sentence. Making govkit print its declines with the
flag off would also cover it, but that trades against the byte-identical-output criterion of
`DEPL-dRetiredFork-3`, and that trade is the owner's.

---

## What was checked and found clean

These are measurements, not silence. All four lenses returned, so a zero here means the area was
read.

- **Gov's own render.** Run here at the tip, `bash tools/workflows/check-protocol-parity.test.sh`
  printed `in parity — 2 rendered pair(s) match their templates for 'tools/workflows' (MEMORY_TREE_DIR
  'tools/memory-tree')` and exited 0. `git diff 24f8c712 0c0e1757 -- tools/workflows/unattended-build.js`
  changes lines 3, 76 and 228, which are the marker and two comments, and no code line. That is AC1
  as pinned. No render differs from gov's dogfood file beyond the comments.
- **Placeholders.** Counted here, the template carries `{{KIT_DIR}}` four times and `{{TOOL_ROOT}}` and
  `{{MEMORY_TREE_DIR}}` once each. The surviving-placeholder arm
  (`check-protocol-parity.test.sh:168-172`) matches `{{[A-Z_]*}}`, which covers all three, and gov's
  render holds none.
- **The probe.** It asks git (`ls-files --error-unmatch`, `:75`), refuses when neither rung is
  tracked, holds an override to the same test, and refuses a value outside a path's charset
  (`:108-114`). It does not guess. Its one defect is WHERE it refuses (F3). The driver path is a
  declared convention, not a probe (spec §3, `TOOL-dPolishedVitrine-8`).
- **Kit versions.** Run here at the tip, `bash tools/check-kit-versions.sh` exits 0, with
  review-harness at 1.8 and unattended at 1.19. One merge-time hazard sits outside this range, and the
  build journal already carries it under "Hand-off to the lander". `main` (`09a22d2b`) also took
  unattended from 1.18 to 1.19, for different content. Both sides write the same bytes, so the version
  gate would pass over two different kits at one version, and the lander must take unattended to 1.20
  at every carrier. It is not scored here.
- **Ratchets.** Run here at the tip, `bash tools/check-install-prefix.sh` exits 0, and
  `tools/install-prefix-carried.txt` dropped exactly its two rows. The one ratchet that grew is
  `.lexicon.conf`'s `VERB_OFFENDER_PIN`, from 984 to 986. That is a hand-justified raise for
  `boundedParallel` and `chunk`, which `tools/hooks/agent-cap.js` recognises by name. It was decided
  in spec §8 F3, and `TOOL-aWeldedTribunal-12` holds the owner-level tension. No lens raised a
  finding against it.
- **Arms that cannot fail.** No lens confirmed one. The build journal records every new arm observed
  red before its fix (AC2, AC6, AC8, AC12). This synthesis did not re-run those suites.

## Disposition

Round 1's confirmed-blocker count is 1. For a closing diff review, `memory/guides/BUILD-METHOD.md` M8
says to fix every blocker and then re-review the FIX, not the diff. It also says a blocker that cannot
be fixed inside the mandate's scope is a park, not a waiver, and that its unit does not close. F1 has
one repair inside this unit's scope: the fixture-verified receipt-migration sequence, written into
the §3 hand-off and the §4 Rollout. If only the govkit repair is chosen, which §3 excludes, F1 parks
and `TOOL-dPolishedVitrine-1` does not close until that govkit spec lands. That spec is also where F2
belongs. F3, F4 and F5 are repairs to this unit's own files. The hand-off to core and NicoCares waits
on F1 whichever route is taken.

## Scope and limits of this review

- Findings are anchored to this worktree at `0c0e1757`. Every cited line was re-read at the tip.
  This synthesis also ran some checks itself: the parity leg, `check-kit-versions.sh`,
  `check-install-prefix.sh`, the placeholder count, greps over gov's render blob, and reads of both
  consumer receipts.
- The fixture reproductions behind F1, F2 and F3 are the skeptics'. They were not re-run here.
- Not covered: a fresh `apply` at the tip. No lens exercised it. Reading the code, `rendered` is not a
  landable role (`govkit.py:2033-2041`, `:2060`) and this kit declares no adopter, so a fresh apply
  lands the template and no harness until someone runs `--render`. `REVIEW-PROTOCOL.md` already
  worked that way at base. This was not verified on a fixture.
- Not covered: the unattended kit's own `update` path with `GOVKIT_RERENDER=1`. No lens reported a
  defect there. The template that kit re-renders is an existing source, which the row walk writes
  before the regenerate runs, so F2's ordering should not reach it. That was read, not run.
- This is a diff review, not a gate run. The build's AC11 record is the full bar.
