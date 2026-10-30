**Serves:** research DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-27 DEPL-dShippedRelease-30

# Reuse scout B — dShippedRelease

The scout's final return, extracted from its transcript by script, never retyped.

# Scout B: DEPL-dShippedRelease-11, -12, -27, -30

Verified at HEAD `f4597719e`. I wrote nothing to the repository.

- **Concurrent edit:** while I read, another process staged re-renders of `memory/LIVE.md`, the README and the packet at 11:10:58. My read-only commands did not touch them. The packet still shows my four clauses at hashes `62dc6590`, `027c3b9f`, `b595f1f2` and `13cc3301`, unchanged from the baseline.
- **Lookup:** I ran `reuse_lookup.py` five times. No partial-recall notice appears: the one run I read to its end carries none, the header's scan coverage reads "unscanned layers: none", and the other four were cut at 50 lines.
- **Not built at HEAD:** `tools/loop/`, `tools/runtime/`, `tools/lib/gov-ref.sh`, `tools/lib/commit_trailers.py` and `tools/playbook/namespaces.toml` do not exist. Every parent interface below is spec-only.

## (1) Units

### DEPL-dShippedRelease-11: `deps.landing` (cl-0421@62dc6590)

**Seam:** wire through. `seam: deploy.parents — reuse for the hold; extend via TOOL-dWellOiledMachine-18 WAIT_KINDS, TOOL-dDeclaredLoop-15's route and the parents front matter`.

| Field | Finding |
|---|---|
| Exists at HEAD | `parents:` parsed at `tools/memory-tree/gen_build_index.py:1212`. Landed reading per run: `check_work_landed`, `tools/unattended/lib-unattended.sh:1814`, and `read_landing_commit`, `:1688`. Neither reads another build. |
| Specced, not built | dWellOiledMachine-18 wait records and sweep. dDeclaredLoop-15 `deps.on-parent-withdrawn` route; its non-goal hands the `superseded` link move to `deploy.parents`. dWellOiledMachine-50. KICK-dKeptSession-7 `landed` notices, whose non-goal leaves the held landing here. |
| Design lines | flow-steps:436 (`deploy.parents` outcomes). flow-roles:228 (FR-7), :246. v2:1232. |
| Owned nodes | `item.deploy.parents`, `policy-key.deps.landing`, both owned by -11. |
| Policy keys | `deps.landing`: row at `tools/policy/catalogue.toml:580`, owner dShippedRelease, still on `tools/policy/unsummarised-keys.txt:49`, so this unit writes `summary` and `usage` and drains it. Reads `deps.on-parent-withdrawn` (dDeclaredLoop) and `flow.wait-ceiling` (dDeclaredLoop). |
| Product paths | New `tools/deploy/parents.py` (proposed kit home); a `tools/runtime/waits.py` WAIT_KINDS row; `tools/policy/catalogue.toml`; `tools/policy/unsummarised-keys.txt`. |

### DEPL-dShippedRelease-12: the landing queue (cl-0422@027c3b9f)

**Seam:** wire through, not the turnstile. `seam: cadence lease — reuse for the turn; extend via --lease acquire run landing <branch>`. dWellOiledMachine-18 S4 already uses `--lease acquire run wake <wait id>` this way, and cl-0425 names `release/<E>` as a cadence lease.

| Field | Finding |
|---|---|
| Exists at HEAD | `cmd_land`, `tools/push-main.sh:952`: tip read `:956`, carry check `:962`, marker `:967`, push `:978`, landed path `:981-983`, marker removal `:988`, retry bound `:188`. Compare-and-swap shape: `write_claim`, `tools/unattended/unattended.sh:2396`, push at `:2423`; `write_red_ref`, `tools/run-gates/post-merge.sh:275`. Attended push: `tools/push-main.sh:1128`. |
| Turnstile | `tools/run-gates/run-gates.sh:1467` is a host semaphore keyed on a host directory. It cannot serve across nodes. The only queue-shaped thing is its FIFO; do not extend it. |
| Specced, not built | dPlacedRequest-1 lease grammar and `derive_lease_ref`. dPlacedRequest-11 `write_gov_ref` and `build_gov_commit`. dPlacedRequest-15 fence and atomic push. dPlacedRequest-17 declared clock. dPlacedRequest-18 cadence segment. dPlacedRequest-29 retry class. dWellOiledMachine-60 atomic push with beat and notice. dWellOiledMachine-48 `raise_owner_item`. |
| Design lines | flow-steps:437 (`deploy.land`), :479-482 (landing order). v2:756, :1168, :1493. coordination:194-195. gap-register:113. |
| Owned nodes | `item.deploy.land`, `policy-key.landing.order`, both owned by -12. Gap `gap-flow-08`. |
| Policy keys | `landing.order`: row at `catalogue.toml:180`, on `unsummarised-keys.txt:94`. |
| Product paths | `tools/push-main.sh`, `tools/push-main.test.sh`, `tools/unattended/unattended.sh` (lease name only if the grammar needs it), new `tools/deploy/landing_queue.py`, `tools/gate-legs.json` through the leg factory. |

### DEPL-dShippedRelease-27: `carries`, squash, publications, Codex (cl-0437@b595f1f2)

This clause holds four separable behaviours, so consider parts 1/n to n/n.

**a) `carries` on the landing record.** `seam: commit_trailers.read_commits — reuse for the range read; extend via dWellOiledMachine-39 derive_act_range --default-tip`.
- At HEAD the trailer readers are `tools/memory-tree/routed_commits.py:231` and `:370`, and `tools/unattended/lib-unattended.sh:1064`.
- Not built: dDeclaredLoop-23 `read_commits`.
- Do not extend `derive_carry_set`, `tools/push-main.sh:548`. It computes something else (see record 7).

**b) `landing` native-id class.** `seam: [[native]] row in tools/playbook/namespaces.toml, shape PLAY-dOrderedCharter-28 S2`. Precedents are `commit` (dDeclaredLoop-23 S1) and `intake-key` (dWellOiledMachine-27).

**c) Publication.** Write a `release` record per (SHA, `artifact:<url>`), reusing the kind unit -15 owns. Source: research-git-pockets:90, and gap-register:413. The atlas is the first subject: `2026-10-16-build-PLAY-dClosedLoop-1-atlas.py`.

**d) `commits.squash`.** No lander seam exists; `tools/push-main.sh` has no squash path (records 8 and 9).

**e) Codex.** `seam: resolve_install_target — reuse for targets; extend via the codex adapter's [install] table (dWellOiledMachine-14 S5)`.
- At HEAD: `run_fragment_merges`, `tools/govkit/govkit.py:6109`, hard-defaults to `.claude/settings.json` at `:6133`. `tools/settings-merge.py` writes Claude's shape. Re-surfacing belongs in `cmd_apply` `:7503` and `cmd_update` `:9144`.
- Not built: dWellOiledMachine-36 (`hook-trust` row), dWellOiledMachine-37 S3 (trust store).

| Field | Finding |
|---|---|
| Design lines | v2:1392, :1712. research-git-pockets:50, :143, :153. research-harness-cli:52, :133. distribution-b:180. memory-plan:196, :219, :333. layer-memory:430. flow-steps:439 (`deploy.record`). |
| Owned nodes | `policy-key.commits.squash` owned by -27. `record-kind.landing` and `item.deploy.record` owned by -1, which -27 extends. `record-kind.release` owned by -15, which -27 extends. Gaps `gap-deploy-21`, `-22`, `-23`. |
| Policy keys | `commits.squash`: row at `catalogue.toml:1560`, on `unsummarised-keys.txt:35`. Reads `install.steps` (row exists, owner dShippedRelease; I read the name line only, not its `summary`) and `runtime.harnesses` (dWellOiledMachine-14). |
| Product paths | `tools/deploy/` landing reader; `tools/playbook/namespaces.toml`; `tools/runtime/harnesses/codex` adapter (exact filename not read); `tools/govkit/govkit.py`; `tools/settings-merge.py`; `tools/check-wiring.sh`; `.githooks/prepare-commit-msg` (created by dWellOiledMachine-33 S4). |

### DEPL-dShippedRelease-30: the patch build and shared budget (cl-0440@13cc3301)

**Seam:** wire through. `seam: tools/loop/budget.py record_draw — reuse for the draw; extend via a root walk and the --for draw wrapper`. `seam: tools/runtime/intake.py file — reuse for filing; extend via a deploy origin`. `seam: post-merge verdict — reuse for the red`.

| Field | Finding |
|---|---|
| Exists at HEAD | Red publication only: `tools/run-gates/post-merge.sh:252`, `:275`, `:301`, read at `.githooks/pre-push:1912`. |
| Specced, not built | dDeclaredLoop-30 S3 and S7. dPlacedRequest-16 S3, S4, S5, S7. dPlacedRequest-17. dPlacedRequest-21 S2 (`origin-slug`, `origin-sha`). dWellOiledMachine-27 S1. dWellOiledMachine-48 S1. dBoundRoles-11 (`park-build`). dWellOiledMachine-3 (park with lease released). |
| Design lines | flow-steps:40-44, :438, :443, :446. v2:737, :780, :1163, :1261. P39 at v2:1068. |
| Owned nodes | `item.deploy.released` owned by -5, which -30 extends with the count. `item.deploy.core` owned by -13, which -30 extends with the filing. |
| Policy keys | None owned. Reads `flow.rework-budget` (`catalogue.toml:761`, dDeclaredLoop), `leases.queued-claim-days` (`:148`, dPlacedRequest) and `patch.ratify` (`:1200`, dPlacedRequest). Each has a row. "The third" has no key (fork F9). |
| Product paths | `tools/loop/budget.py`, `tools/runtime/intake.py`, new `tools/deploy/patch.py`, the release-hold item code in `tools/deploy/`. |

**Roster note:** `item.deploy.released`, `item.deploy.core` and `item.deploy.land` each have two claimants across groups. The spec brief should name one owner for each.

## (2) Where records and source disagree

1. **The entry-point table's post-close row is cited and not defined.** flow-steps:438, :440, :495 and :574, and layer-flow:327, all cite it. I found no such row: v2 has no match for `post-close`, and the flow-steps `[entry]` section has none. No parent spec implements it. The `post-close` matches under `*/spec` are unrelated (aWokenSentinel, dLoggedFlight). So unit -30 and unit -13 must define it, or the brief must rule where it lives.

2. **Clause 0440's "one push" is three pushes in the spec.** dPlacedRequest-16's "The draw" block shows acquire, `budget.py draw`, then release, each its own step. A grep of -16, -17 and dDeclaredLoop-30 finds no atomic push for a draw, and dDeclaredLoop-30's non-goals leave serialization to leases. The clause says it "appends the draw and releases the lease terminal again in one push".

3. **The loser cannot re-read the budget as specced.** `record_draw` appends to a tracked transition record and commits it (dDeclaredLoop-30 S3). The row therefore sits on the patch's branch until landing. A second patch re-reading after losing the compare-and-swap sees the old count, so two draws can both pass where the budget admits one. dDeclaredLoop-30 concedes this ("two racing draws are two rows"). Pushing the row to the default branch needs the lander and the whole bar. See fork F4.

4. **"A chain of patch builds shares one budget" is not specced.** dDeclaredLoop-30 S7 draws on the patch's first `parents:` entry, and dPlacedRequest-21 carries `origin-slug`. Neither walks to the root: a patch of a patch draws on the middle patch. Its `gen_build_index.py:1204` cite also reads `:1212` at HEAD.

5. **"A draw on a closed root always finding the root's tombstone" is false for almost every build at HEAD.** The remote holds 35 `refs/gov/runs/*` refs and nothing else under `refs/gov/`, while 147 build READMEs read CLOSED.
   - The -16 scope lines I read define `--for draw` over a tombstone and over a draw's hold, not over an absent ref.
   - Its S3 excludes legacy claims from `foreign-tombstone`.
   - Its S7 prunes terminal legacy claims after `leases.queued-claim-days`.
   - So a patch on a root closed before dPlacedRequest lands has no tombstone to find.

6. **A live root is unhandled.** A red files its patch at `deploy.core`, while the root's lease is still live (dWellOiledMachine-60 S4). `deploy.unlease` comes later. -16's `--for draw` covers only the tombstone and hold cases, so a draw at that moment has no defined path.

7. **`check_carry_set` is not `carries`.** dWellOiledMachine-39 §8 F3 takes "the landing's `carries`" to mean `check_carry_set`, which reads commits that rode in through the local default branch (`tools/push-main.sh:540-558`). Clause 0437's set is all of `R..HEAD --no-merges`. Its S8 adds only a binding check, so no writer exists.

8. **`<current default>..HEAD` is empty when `deploy.record` runs.** `deploy.record` follows `deploy.core`, after the push, when the default equals the landed SHA. The read needs the pre-push tip: `R` at `tools/push-main.sh:956`, or `was` at `:1127`. Neither is recorded today. `write_lander_marker`'s line (`:392`) holds no prior tip.

9. **The re-emit design assumes a squash the lander never does.** research-git-pockets:153 says "the lander re-emits the union". `tools/push-main.sh` only makes `--no-ff` merges (`:881`, `:1070`). A hosted squash never runs the lander, so `refuse` "at the landing" cannot see it. `.githooks/pre-rebase:14` already states that blindness. Only a local `git merge --squash` is seeable, through `prepare-commit-msg`, which does not exist yet (I expect it to receive `squash` as its source argument, from git's hook contract, not checked here).

10. **The lease does not carry the verified tree.** coordination:194 says it does. dPlacedRequest-1's `witness` is the progress witness, and dWitnessedBar-4 S6 puts `tree` on `test.exit`'s transition. So the queue's input has no cross-node reader yet.

11. **`plan-priority-then-first-verified`, the default, has no input in dShippedRelease's closure.** The priority field is dRankedPlan's (`cl-dClosedLoop-0369`). dRankedPlan is outside dShippedRelease's parent closure and has zero specs. Its one child is dTendedCadence.

12. **The draw cause set refuses a release retry.** dDeclaredLoop-30 S3's closed set lacks a cause for "each release retry drawing on it too", and a cause outside the set refuses.

13. **`gap-deploy-15` in research-harness-cli:144 is the wrong id.** Register row `gap-deploy-15` is the retired-kit receipt (gap-register:405). The Codex gap is `gap-deploy-21` (:411).

14. **The task's parent list omits two deferred builds.** dPlacedRequest and dKeptSession are also DEFERRED, and most lease surfaces this group needs are dPlacedRequest's. Neither is a direct parent, but both are in the closure. dPlacedRequest supplies the units I cite.

15. **dWellOiledMachine-14 S5's `settings` kind is one path, but Codex needs two.** research-harness-cli:133 names `.codex/hooks.json` and `.codex/config.toml`. `resolve_install_target` returns one target per kind and refuses more than one.

16. **Lines that held when checked.** gap-flow-08's "`push-main.sh` never takes it" holds: there is no turnstile or `--hold` reference in that file, though the bar inside its push does take it. dPlacedRequest-15's `:978`, `:1128` and `:262`, dWellOiledMachine-39's `:962` and `:1022`, dPlacedRequest-11's `.githooks/pre-push:494` and `unattended.sh:2415`, and `:2423` for the claim push are all correct at HEAD. `GATE_POST_MERGE` is still undeclared here and `refs/gov/bar-red` is absent, as gap-deploy-02 says.

## (3) Interfaces (proposed names)

Within this group:
- `derive_landing_id <sha>`: the `landing` class form, shared by -27's `[[native]]` row and -30's records. Used with `landing_prior_tip` below, it fixes the record's range.
- `landing_prior_tip`: field written by the lander's outcome record. Produced by -12, read by -27.
- `read_parent_state <slug>` → `landed|held|withdrawn|superseded|absent`: -11 produces it, -12 reads it to drop a build not yet admissible.
- `resolve_budget_root <slug>`: walks `origin-slug` to the root; -30 owns it and it replaces dDeclaredLoop-30 S7's first-parent read.

With other groups:
- `read_landing_record <sha>` and fields `carries`, `outcome`, `patch-key`: -1 owns them, -27 and -30 extend them.
- `derive_red_key <landed sha>` → intake key for (`default-branch-red`, SHA): -30 owns it. -13 calls it, and dTendedCadence's `maintain.patch` must use the same function, which is not specced because dTendedCadence has no specs.
- `count_keep_waiting <build> <sha>` and wait kind `deploy.released`: -30 owns the count, -5 owns the kind and deadline. dWellOiledMachine-18 assigns both to dShippedRelease.
- WAIT_KINDS rows `parent-landing` (-11), `landing-turn` (-12), `deploy.released` (-5).
- OWNER_ITEM_KINDS rows `landing-order` (-12), `release-hold` (-5), `codex-retrust` (-27).
- Atomic landing refspecs: dWellOiledMachine-60's three, plus one `--force-with-lease` on the turn ref if F1 takes the fenced form.
- `release` record per (SHA, environment), with `artifact:<url>` as an environment: -15 owns the kind, -27 uses it. `release.environments` must accept or exclude this form.
- A new `cause` for release retries in `tools/loop/budget.py`: -30 with -15.

## (4) Order

- **Parents for -11:** dDeclaredLoop-15, dWellOiledMachine-18, KICK-dKeptSession-7.
- **Parents for -12:** dPlacedRequest-1, -11, -15, -17, -18, -29; dWellOiledMachine-48, -60.
- **Parents for -27:** dDeclaredLoop-23, dWellOiledMachine-14, -33, -36, -37, -39; PLAY-dOrderedCharter-28; dTotalRecall's kind registry.
- **Parents for -30:** dDeclaredLoop-30, dPlacedRequest-16, -17, -21; dWellOiledMachine-4, -18, -27, -48; dBoundRoles-11.
- **Inside the group:** -1 before -27 and -30. -11 before -12. -13 and -5 before the matching half of -30. -15 before -27's publication part.
- **Lander edit order:** -12 builds on dPlacedRequest-15 and dWellOiledMachine-60, both of which rewrite `:978` and `:1128`. Build it last among the lander units.
- **Hazard until dPlacedRequest-11 lands:** `write_claim` refuses while `push-main-active` exists (`unattended.sh:2415`), and the hook clears verdict files on every push (`.githooks/pre-push:494`). A turn write therefore must not run inside the marker window `:967-988`. Paths `:981`, `:982` and `:956-957` exit without passing `:988`, so a turn release must sit in the EXIT trap at `:217`.

## (5) Forks

Not settled from source:
- **F1. Turn release.** A separate write after the landing, or a fourth refspec in the atomic push? The fourth fences a stale holder, and a failed landing still needs a separate release.
- **F2. Turn staleness.** `leases.expiry-hours` defaults to 24, so a dead node could stall every landing for a day. A shorter bound needs a value no key owns. A bar can run 16 to 65 minutes (figures from `tools/push-main.sh:231-233`).
- **F3. Parent "landed" witness.** The lease reads `landed` only at `deploy.unlease` (dPlacedRequest-16 S2), well after the push. The `landed` notice or the landing record is earlier. `test-decides` also needs a defined "verdict without the parents' work".
- **F4. Where a draw lives.** Lease commit message, a new `refs/gov/` ledger, or a lander-carried default-branch commit. Only the first two satisfy "one push" without a bar, and both depart from dDeclaredLoop-30's transition record.
- **F5. Pre-lease roots (record 5).** Backfill tombstones, treat absent as the empty-budget case, or stop legacy pruning.
- **F6. Default order before dRankedPlan.** Fall back to first-verified with a recorded reason, or add dRankedPlan as a parent, which needs a `**Moved:**` line or a deviation.
- **F7. First-verified across nodes.** Node-stamped time is exposed to skew, and the declared clock (dPlacedRequest-17) judges deadlines, not order.
- **F8. Squash scope.** Whether `commits.squash` covers hosted squash at all, as a post-hoc Maintain reading, or local squash only. The clause says "seen on a planted squash" without saying which.
- **F9. Keep-waiting.** Whether "third" is a constant or a new key, and whether a silent owner's applied default counts. The count's store is also open: dPlacedRequest-12's decision refs are create-only, so three answers on one (item, fork) key cannot each write one.

Settled enough to recommend:
- Do not extend the turnstile.
- Do not use `check_carry_set` for `carries`.
- Split -27 into parts.

Relevant files:
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\tools\push-main.sh`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\tools\unattended\unattended.sh`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\tools\run-gates\post-merge.sh`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\tools\govkit\govkit.py`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\tools\policy\catalogue.toml`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\memory\builds\dPlacedRequest\spec\2026-10-25-spec-TOOL-dPlacedRequest-16.md`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-30.md`
- `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d\memory\builds\dWellOiledMachine\spec\2026-10-26-spec-TOOL-dWellOiledMachine-60.md`
