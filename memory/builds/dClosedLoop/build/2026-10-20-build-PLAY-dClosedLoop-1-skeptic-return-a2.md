# Skeptic return: run A, batch 2

**Serves:** research PLAY-dClosedLoop-1

Dispatch 176's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-17-skeptic.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

- A5-F5: refuted
  The finding says another node may take over a build parked on the owner. v2 `cl-dClosedLoop-0332` (dWellOiledMachine) forbids that: discovery returns "hand-over releases and expired leases whose build has work ready, never a terminal tombstone and never a build parked on an open owner item". The release in `cl-dClosedLoop-0326` is a hand-over under `cl-dClosedLoop-0134`. Once the owner disposes the item, the build is no longer "parked on an open owner item". The normal pick then claims it and takes the lease with the epoch bumped. So no node takes it while it waits, and the late go does not leave it leaseless.

- A2-F5: confirmed medium (the walker graded high)
  coordination [6] refuses every transition while a message is "neither answered nor acknowledged", until `flow.wait-ceiling`. No flow-steps item, and no actor in [rules] ("the executor reads the build's mailbox"), answers or acks a `question`. `next` only "lists them as next actions". The block falls only on step transitions, so X's items run until its next exit. The default answers at 72h and X still reaches its terminal. That is a stall and lease churn, not a failed scenario.

- A2-F10: confirmed medium
  coordination [6] has the sender "(fleet tag, session, build)" as a message field, and `cl-dClosedLoop-0143` names the ref by `<fleet tag>/<session>`. `cl-dClosedLoop-0335` scans payloads for tokens and refuses only "an agent-forged request record". `cl-dClosedLoop-0160` derives a message id from the sender's session, which is not an identity check. layer-runtime:830 says that under Codex the invariants "hold only at the git boundary". No clause binds the writer of a mail, lease or tombstone ref to the identity it names.

- A4-F16: confirmed low
  The row is at fates:176 in the copy, not :111. It reads "govkit | install and update, receipt | … RESHAPED | … (dShippedRelease)" and omits dSafePassage, whose `cl-dClosedLoop-0019` and `cl-dClosedLoop-0020` reshape `update` and the receipt. The claimed consequence does not follow: `cl-dClosedLoop-0488` joins each path to its fate and grades no owner. "govkit | optional" agrees with v2's `distribution` layer row ("govkit's install by copy … and its receipt"). What is left is a wording defect.

- A3-F2: confirmed medium
  flow [Entry points, settled 2026-10-14]'s last row still reads "A failed verify after its build closed at landing | Plan's triage | filed as an ask, then a patch build or a planned build by its size". layer-flow:326-328 says the row "now covers a landing-review finding and a post-landing core red, each entering as a patch build". The table was never changed. `deploy.core`, `deploy.distill` and the landing review all route "through the entry-point table's post-close row".

- A4-F15: confirmed medium
  flow-steps:614 gives `adopt.decisions` the actor "reviewer, as two raters, and the owner where `retrofit.decisions` says". [rules] requires one actor of one kind, and one item per policy value. layer-roles:409 lists the item under reviewer only. Under `docs-owner-ratifies` (v2 catalogue), the owner's ruling has no item of its own.

- A5-F7: confirmed medium
  `grep -c "max-rounds\|CEILING"` over flow-steps returns 0. `review.dispose` routes "a follow-up round as `review.follow-up` says", and `review.fold` routes "the next round as `review.design.rounds` says". `cl-dClosedLoop-0117` refuses "the round after the limit" and the report reads CEILING, but no route says where a CEILING report's open findings go. `cl-dClosedLoop-0117` promotes only a NON-CONVERGENT round's findings.

- A1-F5: confirmed high
  `review.trigger` is "Proven by … the owner's request record". `grep "^| " layer-memory.md | grep -iE "request|disposition"` finds only `attendance override` and `disposition`, so no such kind or writer exists. `entry.place`'s closed set and `life.request`'s verbs carry no review request. `review.design` defaults to `opt-in` (v2 catalogue), so the default spec audit has no declared way to be opted into.

- A1-F4: confirmed high
  [breakpoint] says `run.on-owner-question` "resolves it when it is raised, never for a ratification", with "the supervisor's recorded choice under `best-effort-recorded`". The catalogue row agrees: it "decides an owner item when the item is raised". `confirm-steps` "adds a gate at every step's exit", and those gates are owner items. `cl-dClosedLoop-0207` says "best effort recorded once the wait passes" but names no key for that wait. Under the default, an attended owner's confirmations at a design go or a step exit are decided at once, so the guard loosens silently (c3).

- A1-F8: confirmed medium (the walker graded high)
  `build.reuse-check` routes "clean → the unit built", which is not an item. `build.recommend` needs "every unit built and reuse-checked", which is prose. Stage 0's first run (whole-audit [stage0]) lists "the Build step's five from `build.recommend` on" as reached from no entry. The intent, a join over the roster, is plain to a spec writer, so the declarations are wrong but no scenario fails. That makes it medium.

- A2-F9: confirmed medium
  flow-steps [deploy] says "Landings on a node are ordered by `landing.order`". P21 and flow-interactions FI-7 settle "plan priority, then first verified" with no per-node scope. `cl-dClosedLoop-0422` ("landings ordered through the landing queue it builds") and `gap-flow-08` name no shared ref or cross-node order. Builds verified at once on different nodes land in push order.

- A3-F1: confirmed high
  `deploy.core`'s Then reads "red → a patch build through the entry-point table's post-close row, and the close waits for its filing", with no route on to `deploy.record`. `deploy.close` needs only "`deploy.unlease` and `deploy.released`", so no witness of the filing exists to wait on. Reading Needs alone cannot rescue it: by the same reading, `test.seen-red` would follow a red `test.verdict`. layer-runtime [decide] then answers `stuck` and raises an owner item, but no declared route takes the originating build to `landed` (c2).

- A3-F7: confirmed medium (the walker graded high)
  `cl-dClosedLoop-0440` puts a landing's patch on the originating, already spent budget, and `cl-dClosedLoop-0116` ends a spent build by best effort, "raising the budget the owner's alone". No owner item is opened, so the default branch stays red. The pre-push hook (.githooks/pre-push:1909-1971) then forces FULL on every later landing, and `test.route` sends each later build's INHERITED red to its own fix unit. The outcome is still declared and the chain ends, so no scenario fails to terminate.

- A3-F5: confirmed medium (the walker graded high)
  `deploy.core` raises a patch, and layer-expansions' `default-branch-red` (indexed by `refs/gov/bar-red`, published at tools/run-gates/post-merge.sh:249) starts a Maintain event run. Patch builds skip `plan.dedupe`, and `cl-dClosedLoop-0440` covers only "a patch build raised by a landing". But `maintain.patch` opens a patch only for a reading whose fix is a tracked-content safe fix. Maintain "Does not change product code" (flow [Maintain]), so a product-code red goes to `maintain.file` and then triage, where `plan.dedupe` matches the live patch. The double filing happens only for the safe-fix class of red.

- A2-F4: confirmed medium
  `deploy.parents`' Then reads "a parent unlanded or paused → holds", with no deadline or outcome. The `flow.wait-ceiling` catalogue row names "a dependency hold", and `cl-dClosedLoop-0118` reds "a wait declaring no deadline". Deploy's policy list at flow-steps:414 omits `flow.wait-ceiling`. A paused parent keeps its leases renewed under [lifecycle], so it never expires.

- A3-F10: confirmed high
  The values are only named: layer-flow:311-312 says "`replan` by default, with `adopt-parent-work` and `withdraw-too` allowed". `cl-dClosedLoop-0100` builds the key with no arm per value. [transitions] has no row out of `deploying` to `planning`, and the engine "refuses any transition the table lacks". Under the default, Y at `deploy.parents` cannot replan. No item consumes `life.notify`'s `withdrawn` post before Deploy.

- A3-F11: confirmed medium (the walker graded high)
  The item's "holds" carries no deadline arm, and Deploy's list omits the key, as A2-F4 found. Two records do declare the hold's deadline and default: the `flow.wait-ceiling` catalogue row ("a dependency hold … past which the waiter takes its declared outcome"), and stall-and-loop point 6 ("dependency and mailbox waits: past their deadline, the waiter takes its declared default (replan…)"). So the item's missing arm is a spec-writer trip. The scenario failure past the ceiling is A3-F10's missing `replan` transition, not this finding.

- A3-F20: confirmed medium
  `design.input` routes "patch → `design.unit-spec`, as a micro-spec", which skips `design.overlaps`. Patches also skip `plan.dedupe`. `design.unit-spec` "acknowledges the unit's overlaps" with no overlap record to acknowledge. The worst case is under `strict`, where `design.overlap: refuse` (v2 presets) never applies to a patch. `build.unit-lease` only warns.

- A1-F10: confirmed low (the walker graded medium)
  flow-steps:192 still reads "none MISSING, THIN or FORKED", while `cl-dClosedLoop-0398` has "`design.ready` gaining an UNCARRIED class". Both belong to dIndexedDesign, and the carries join (whole-audit [instruments]) reds an uncarried clause at its Design exit. A spec writer cannot carry the item and drop `cl-dClosedLoop-0398`, so this is stale wording.

- `design.ready` S3: holds
  The patch path `design.unit-spec` → `design.recommend` → `design.reason` → `design.ready` is declared. THIN (tools/unattended/unattended.sh:4505) needs Scope, Acceptance and Gates, which a micro-spec can carry. A route back draws on the budget under [rules].

- `review.pin` S1: holds
  It pins the spec revisions or the commit range. `preset: design-audit` applies only when every pinned revision is a design or architecture record (review-system [lenses]), so a feature build's unit specs keep the unit-spec preset.

- `test.seen-red` S5: holds
  A withdrawn X never reaches Test. Y's and Z's own gates are checked against their own seen-red records, and nothing in S5 changes that item's needs or route.

- `build.acceptance` S5: holds
  `life.quiesce` "dispatches nothing new" and lets running acts finish, so no acceptance is dispatched after the withdrawal. A queued claim replayed against a withdrawn build is refused by `cl-dClosedLoop-0280`'s tombstones.

- `build.scope` S6: holds
  A stray routes "as `build.scope` says", and a refused stray goes to a revert pass on the unit. That pass is a repetition that draws on `flow.rework-budget`, and once the budget is spent the build ends as `flow.on-exhausted` says.

- `deploy.unlease` S6: holds
  An unreachable remote at the tombstone write or the mailbox copy is covered by layer-runtime [decide]: `stale-remote`, "lease or ref witnesses that cannot be read", "holds and retries, and parks once `leases.expiry-hours` passes". So an unreadable ref is never read as a missing one. The item is idempotent, with "a lease already terminal counting as done".

- `build.base` S7: holds
  dScopedBuild descends from dWellOiledMachine (v2 [chain] parents), so the intake record in its witness exists by the time the item is built. Before that, S7's stand-ins are today's tools, which pin the base.

- `build.scope` S3: holds
  A patch's unit carries its write set in its micro-spec's Scope section, which THIN requires. `build.scope` grades the commit against it through `--check-commit` and check 23, as for any unit.

- **Read outside the list above:** none. Broad `grep` runs over the copy's `build/*.md` also scanned the `*-compared.md`, `*-instruments.md` and session-log records, but their lines were filtered out with `grep -v` before display, and nothing from them was read. My one probe script is `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-a2/cl.py`.
