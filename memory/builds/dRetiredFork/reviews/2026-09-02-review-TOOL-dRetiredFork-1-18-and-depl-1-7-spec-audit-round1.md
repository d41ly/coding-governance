**Serves:** spec-audit DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18

# Spec audit round 1 — the 25-unit spec set of dRetiredFork, authored in one session and unreviewed by definition

*Node d, 2026-09-02, round 1, on `branch/kit-update-complexity-af0fb0` against gov HEAD `b0108f13`. The lenses were primed on BUILD-METHOD M2's four cross-read axes — scope, interface, ordering, acceptance — because a set authored in ONE pass fails on those before it fails on anything else: no spec in it was read by a second author, and the corrections that exist inside the build did not reach the units that needed them. A finding survived here only where it joins a spec sentence to a MACHINE: a leg name resolvable in `tools/gate-legs.json`, a tracked path resolvable by `git ls-files`, a symbol at a cited line in `tools/govkit/govkit.py`, an awk arm in `tools/memory-tree/check-memory-hygiene.sh`, a fixture in `tools/hooks/agent-cap.test.sh`. Every citation below was re-derived against the tree by the author of this record before it was graded, and where a claim could be settled by running something it was run: the agent-cap nested-loop fixture was piped through the live hook in both shapes, the `runbook` and `ps-hygiene` leg names were grepped against every row of `tools/gate-legs.json`, `LANDABLE_ROLES` and `UPDATE_ROLE` were read at their definitions rather than from a spec's summary of them, and both adopters' `install.json` unattributed-row counts were measured.*

**Reviewed subjects, each pinned at the blob it was read at:** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-1.md@016805d3428b` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-2.md@7a37e1fe7e86` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-3.md@335000b313fe` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-4.md@1cfba5f3df07` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-5.md@0836c557a9a7` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-6.md@c04a40e5932a` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-7.md@fe1b7cfa3eeb` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-1.md@00ef960910de` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-2.md@2affb0871e2b` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-3.md@af96196d4f9e` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-4.md@0f7ceec27139` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-5.md@9ff358a43dd4` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-6.md@564badb0a0fc` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-7.md@a65cc062693b` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-8.md@aa3d0e823739` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-9.md@2f2581794f14` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-10.md@cea2e2af8567` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-11.md@afa99890866e` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-12.md@aa2cdecd8eb1` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-13.md@ae2ca4f9fbb7` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-14.md@73613b738dea` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-15.md@6fa6f15f79f3` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-16.md@2cd5233c4337` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-17.md@ac215d7bf1d8` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-18.md@d3612254600f`. **ROUND 1.**

## Verdict: BLOCKED

Six blockers stand after adjudication, and the first is about the build rather than any one unit: **the union of 25 acceptance criteria does not imply the README's acceptance.** The README makes one observation the whole verdict — "`govkit update --write` is the whole update at both adopters. That is one observation, not a tally" — and no spec in the set carries an acceptance criterion that observes a `--write` run against a real adopter. Every `--write` AC in the set targets a fixture; every AC naming `C:/projects/nicocares/main` or `C:/projects/incms/main` is explicitly read-only. The step that turns "the bytes arrived" into "the update ran" is `DEPL-dRetiredFork-3`'s re-render, which ships default-OFF by its own §4 Rollout with AC6 asserting byte-identical output while the flag is off. A second, independent measurement says the same thing from the other end: NicoCares' receipt holds 32 rows at `evidence: "unattributed"` and inCMS's holds 30, `govkit.py:6566-6573` withholds the `gov_commit` re-stamp while any such row exists, and no unit in the set drives that population to zero. Every unit can pass and the stated goal is never observed. One document must change, and the honest options are a new adopter-facing acceptance criterion or a README that stops claiming the write run as its done-condition.

The second blocker is the only item in the set that can destroy data in a repository gov does not own. `DEPL-dRetiredFork-2` S3 gates landing on `LANDABLE_ROLES`, which is derived at `govkit.py:1987` from `ROLE_KINDS` and therefore contains `seed` as well as `engine`, and S2 lands through `land_through_index`, which carries none of the copy-once protection `_cmd_apply` applies at `:4332-4338`. A new gov `seed` source whose destination already exists at the target is overwritten. The gate as written also admits a role that `update`'s own disposition table excludes: `UPDATE_ROLE["seed"]` is `"report-reseed"`, never written by that verb.

The remaining four cluster on two units. `TOOL-dRetiredFork-14` asserts that re-pointing the wired hook command "is a call-site change and not a new capability" — false at `tools/settings-merge.py`, whose dedup is a substring test on the basename marker `agent-cap.js` and whose own docstring says it "deliberately does NOT rewrite a stale hook path"; gov's tracked `.claude/settings.json` already carries that marker, so the repath is a no-op on every already-wired tree while S2 withdraws the copy the wired command still names. That is the silent unwiring of a security guard the unit's own §5 calls the build's highest risk, and `DEPL-dRetiredFork-3` S5 — the enforcement the unit delegates that risk to — has no acceptance criterion at all. `TOOL-dRetiredFork-4` is broken twice over: every acceptance observation is anchored on `.claude/hooks/agent-cap.test.sh`, which is not a tracked file, and its §1 premise about which way the hook fails is **inverted at HEAD** — measured here, the nested marked loop exits 2 and the unnested one exits 0, the exact opposite of what the spec says, so the unit's staged RED cannot be staged and its §4 justification is false.

Fifteen highs stand beside them, and they are not scattered. Read together this set has one dominant failure and it is the predecessor build's: **a scope item that names a deliverable no acceptance criterion observes**, five times over (B6, H13, H14, M2, M3). The second cluster is what one-pass authorship produces where parallel authorship produces something else: **a handoff into a unit whose own scope excludes the work** (H4, H8), and **an acceptance criterion that forward-depends on a unit five steps later** (H5). The third is the most mechanical and much the cheapest to gate: **a name spelled in a spec that resolves to nothing** — two gate legs that are not rows in `tools/gate-legs.json` and are named in five specs' §7 (H1), a test file that does not exist (B4), an arm number naming the wrong arm (H6), a placeholder no adopter can render (H12), and three helpers whose contracts are not what the specs say they are (H9, H10, H11).

The set is otherwise strong, and unusually well measured for a first pass. Its problem statement is arithmetically checkable and mostly checks out. `DEPL-dRetiredFork-7` correctly diagnoses that every number in the build rests on two registers that both undercount, and sequences itself at order 2 for exactly that reason. `TOOL-dRetiredFork-18` cites a helper, its docstring, its selftest arms and its two unwired call sites, and all four are correct at HEAD. The irony of this round is the one the corpus keeps recording: the three units that diagnose green-by-absence most sharply — `TOOL-dRetiredFork-5`, `TOOL-dRetiredFork-7` and `TOOL-dRetiredFork-1` — each close with an acceptance criterion that cannot fail.

## Review shape

- raw 76, confirmed 35, refuted 41, unverified 0, precision 0.46.
- confirmed by severity as ADJUDICATED in this report: **6 BLOCKER · 15 HIGH · 8 MEDIUM · 1 LOW**, over 30 reported items.
- confirmed blockers: 6.
- the 35 confirmed findings collapse into 30 items here. Every merge is named in the item's own header so the filing and this report stay reconcilable. There are four: B4 arrived twice from two lenses, B1 arrived once against `DEPL-dRetiredFork-3` and once against the README's acceptance paragraph, H2 arrived three times, and H4 and H5 twice each.
- ONE severity was moved at adjudication, and it is named rather than quietly applied. B5 was filed HIGH and is graded BLOCKER here on the ground stated in its own item: its §1 premise is not imprecise, it is inverted at HEAD in the direction that decides whether the unit has any work in it at all, and the reviewer reproduced both exit codes rather than reading the source. Every other severity is as filed.
- no finding went unverified: every confirmed item survived a skeptic prompted to refute it, and the author of this record re-derived each one against the tree before grading.

Precision 0.46 is below §8's ~0.5 tightening threshold and is reported as such rather than rounded up. The reading is not that the lenses were poor but that the surface was fresh and enormous — 25 unreviewed documents citing roughly a hundred distinct names across `govkit.py`, five checkers, three kits and two foreign repositories. A large share of the refutations were a lens reporting an interface disagreement between two specs that turned out to be two spellings of one true thing. The lever for round 2 is scope, not agent count: run it over the FOLD only, and prime it with this report so the same 41 are not re-manufactured.

## The findings

| # | Sev | Unit | Address | One line |
|---|---|---|---|---|
| B1 | BLOCKER | DEPL-3, set-wide | DEPL-3 §6 AC1-AC8 · README done-condition | no AC anywhere observes a `--write` run at a real adopter, so the union cannot imply the build's acceptance |
| B2 | BLOCKER | DEPL-2 | §2 S2, S3 | `LANDABLE_ROLES` admits `seed` and the landing path has no copy-once guard, so gov overwrites a target-owned file |
| B3 | BLOCKER | TOOL-14 | §2 S1 · §10 | settings-merge dedups on the BASENAME marker, so the repath is a no-op on every already-wired tree |
| B4 | BLOCKER | TOOL-4 | §2 S3 · §5 · §6 AC1-AC3 (+TOOL-14 AC3, AC5) | every acceptance observation names `.claude/hooks/agent-cap.test.sh`, which is not a tracked file |
| B5 | BLOCKER | TOOL-4 | §1 Goal · §4 · §6 AC1, AC2 | the nested-loop premise is INVERTED at HEAD; measured, nested exits 2 and unnested exits 0 |
| B6 | BLOCKER | DEPL-3 | §2 S5, absent from §6 | the build's named highest-risk mitigation, hook move before withdrawal, has no acceptance criterion |
| H1 | HIGH | TOOL-16, TOOL-17, DEPL-3, DEPL-6, DEPL-7 | each §7 · TOOL-16 AC4 | `runbook parity` and `gate-lint` are named as legs to keep green; neither is a row in `tools/gate-legs.json` |
| H2 | HIGH | DEPL-6 | §6 AC1, AC2 | the falsification counts are inverted against the roster — four NicoCares and six inCMS, not six and three |
| H3 | HIGH | set-wide | DEPL-1 §6 · DEPL-2 §6 · DEPL-3 §6 | the `gov_commit` re-stamp is withheld by 62 unattributed rows and no unit drives them to zero |
| H4 | HIGH | TOOL-8, TOOL-13 | TOOL-8 §3 · TOOL-13 §2 S1 | 39 literal sites handed to a unit whose declared population excludes the file that carries them |
| H5 | HIGH | TOOL-12 | §6 AC6 · §8 F1 | AC6 forward-depends on `DEPL-dRetiredFork-3` at order 7; this unit is order 2 |
| H6 | HIGH | TOOL-17 | §2 S3 | converts "arm 1" of the prefix checker, which is already a ban; the shrink-only ratchet is arm 2 |
| H7 | HIGH | TOOL-3 | §2 S3, S4 · §7 | the new registry file reds check 3's hardcoded whitelist at order 1; the generalizing key is order 5 |
| H8 | HIGH | DEPL-2, DEPL-7 | DEPL-2 §8 F2 · DEPL-7 §2 S5 | two specs take opposite dispositions of the same `--kits` dispatch defect |
| H9 | HIGH | TOOL-1 | §2 S1 · §6 AC1 | `pop_guard` refuses on a mis-segmented selector, not an empty population; AC1 states what it cannot produce |
| H10 | HIGH | TOOL-5 | §2 S1, S2 · §6 AC2 | "every arm skipped" is unreachable over 26 arms of which 2 are guarded; the predicate is dead on landing |
| H11 | HIGH | TOOL-16 | §2 S1 · §6 AC1 | "declines and reports" is a third behaviour: the refusal aborts the verb at exit 2 after the write loop |
| H12 | HIGH | TOOL-12 | §2 S1, S2 · §10 | the unattended adopter cannot render `{{TOOL_ROOT}}`; §10 checked the descriptor, not the adopter |
| H13 | HIGH | DEPL-4 | §2 S2, absent from §6 | the class-wide grep S2 requires has no criterion — gate the CLASS, failed in the spec's own words |
| H14 | HIGH | TOOL-8 | §2 S3, absent from §6 | the resolve-in-every-caller requirement has no criterion, and AC1's byte-identity cannot catch a residual |
| H15 | HIGH | TOOL-4 | §1 Goal · §10 | gov's own OPEN row `TOOL-aNumeralWarden-2` already decided this remedy, against the shape S1 absorbs |
| M1 | MEDIUM | TOOL-3 | §6 AC5 vs §5, §8 F2 | byte-identical output and an unconditional observability line cannot both hold |
| M2 | MEDIUM | TOOL-3 | §2 S4, absent from §6 | the adopter-facing half — the shipped waiver file and its `[[hole]]` — has no criterion |
| M3 | MEDIUM | DEPL-3 | §5 user docs, absent from §6 | the spec declares that the runbook shrinkage "is an acceptance criterion" and then does not write it |
| M4 | MEDIUM | DEPL-6 | §6 AC2 vs README | seventeen repath rows at one adopter against the README's fourteen across two |
| M5 | MEDIUM | TOOL-7, TOOL-10 | TOOL-7 AC5 · TOOL-10 AC6 | `check-kit-versions.sh` exits 0 whether or not the review-harness version moved |
| M6 | MEDIUM | TOOL-4 | §6 AC5 · §7 | the restatement gate is conflated with playbook parity, which owns the five machine-compared values |
| M7 | MEDIUM | TOOL-10 | §3 first bullet · §2 S2 | `check-verifier-fanout.sh` DOES apply a marker filter; the measured refusal came from the other script |
| M8 | MEDIUM | TOOL-3 | §10 | the probe and terms line belong to another unit's question, so M7 regrounding lands on the wrong corpus |
| L1 | LOW | TOOL-16 | §2 S1 · §6 AC4 | the refusal is cited four lines short, and AC4 runs a `python3` program with `bash` |

---

### B1 — BLOCKER — no acceptance criterion in the set observes a `--write` run at a real adopter

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-3.md` §6 (AC1-AC8), read against `memory/builds/dRetiredFork/README.md`'s "The build is done when…" paragraph. *(Filed twice, once against the spec and once against the README; merged here.)*

**The defect.** The README states one done-condition and says explicitly that it is one observation rather than a tally: a run that lands every stale row, re-renders every rendered row, re-runs every invalidated generator, re-stamps `gov_commit`, and leaves nothing for a person to merge. Grepped across all 25 specs, every `--write` acceptance criterion targets a fixture — DEPL-2 AC1, DEPL-3 AC1, AC3 and AC5 all read `--target <fixture>` — and every criterion naming a real adopter path is explicitly read-only: DEPL-1 AC4 "A read-only `update`", DEPL-2 AC5 "A read-only run", DEPL-3 AC7 "A read-only run", DEPL-5 AC4 "A read-only `check`", and DEPL-7 AC1-AC3 and DEPL-6 AC1-AC2 likewise. The step that converts "the bytes arrived" into "the update ran" is DEPL-3's re-render, and it ships default-OFF by that spec's own §4 Rollout, with AC6 asserting byte-identical output while the flag is off.

**Why it is a blocker and not a high.** BUILD-METHOD M2's acceptance axis is explicit that the overview's acceptance must be implied by the union of the sub-specs', and this union does not reach it. The consequence is not a missing test: the build can be declared done with 25 green units and the goal never once observed at either adopter, which makes the done-condition unfalsifiable and the whole roster unverifiable as a programme. It is also unowned — no unit's §3 defers it, so no reader can discover which document is supposed to carry it.

**Fix.** Add an acceptance criterion to DEPL-3 §6 of the form: with the re-render flag ON, `python tools/govkit/govkit.py update --target C:/projects/nicocares/main --write` lands every stale row, re-renders every rendered row, runs every declared generator, re-stamps `gov_commit`, and the adopter's tree afterwards needs no hand merge — recorded in the acceptance ledger. Add the mirror for inCMS. If a live `--write` at an adopter is genuinely out of this build's scope, say so in the README's acceptance paragraph and restate the done-condition as something the union actually reaches.

**Left-shift gate.** A build-level acceptance join in `gen_build_index.py --check-format`: extract the README's done-condition sentence's imperative clauses and refuse a build whose union of spec §6 criteria names none of them. Cheaper first cut, and the one worth landing: an arm that refuses a build README whose done-condition names a command (`update --write` here) that appears in no spec's §6 outside a `<fixture>` target.

---

### B2 — BLOCKER — the landing gate admits `seed`, so gov overwrites a file the target owns by design

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-2.md` §2 S2 and S3.

**The defect.** S3 reads "Only roles in `LANDABLE_ROLES` land." Verified at source: `LANDABLE_ROLES` is `tuple(k for k, v in ROLE_KINDS.items() if v == "write")` at `tools/govkit/govkit.py:1987`, and `ROLE_KINDS` at `:1960-1968` marks BOTH `engine` and `seed` as `"write"`. So the gate admits `seed`. S2 then lands new rows through `land_through_index` at `:5357`, which writes unconditionally through `hash-object` / `update-index` / `checkout-index` and carries no `dp.exists()` check — while `_cmd_apply` does carry one, at `:4332-4338`, with the reason written beside it: "seed: copied ONCE, then the target owns it." S6's arm list covers engine, rendered, withdrawn and none. There is no seed arm anywhere in the spec.

**Why it is a blocker.** A new gov `seed` source with no receipt row, whose destination already exists in the target, is overwritten — destroying a file the target owns by declared design, in a repository gov does not own, from a verb whose whole selling point in this build is that it needs no operator turn. It also contradicts `update`'s own disposition table: `UPDATE_ROLE["seed"]` is `"report-reseed"` at `:4958-4960`, meaning never written by this verb, so S3's gate admits a role the verb itself excludes. §5 names a `[[decline]]` risk and does not name this one.

**Fix.** Replace `LANDABLE_ROLES` in S3 with `UPDATE_ROLE`'s `table` disposition — engine only — or state explicitly that `seed` is excluded and why. Add a scope item carrying the copy-once guard into the new-source path, an S6 arm exercising it, and an AC observing that a new `seed` source whose destination already exists is REPORTED and not written. Name the risk in §5 beside the `[[decline]]` one.

**Left-shift gate.** A `selfcheck` arm asserting that every write path in `govkit.py` reachable with a `seed` row applies the copy-once guard — concretely, that no function writing target bytes takes a row whose `role` may be `seed` without a preceding `dp.exists()` branch. Stage the break by deleting the guard at `:4332` and confirm RED before wiring.

---

### B3 — BLOCKER — settings-merge dedups on the basename, so the hook repath is a no-op on every wired tree

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-14.md` §2 S1, and §10, which cites `merge()` as the extension point.

**The defect.** S1 says re-pointing the wired command is "a call-site change and not a new capability". Verified in full at `tools/settings-merge.py`: `HOOK_MARKER` is the bare basename `agent-cap.js` (line 53), and `merge()` returns the object unchanged when any command in the matcher group already contains that marker (lines 108-109, `return obj  # already wired — no change`). The module docstring states the limitation outright at line 37: dedup "is a substring test on the marker and deliberately does NOT rewrite a stale hook path (a Phase-3 upgrade concern, not Phase-0 wiring)." gov's own tracked `.claude/settings.json` line 9 already carries `node "${CLAUDE_PROJECT_DIR}/.claude/hooks/agent-cap.js"`, which contains the marker.

**Why it is a blocker.** Every tree already wired at `.claude/hooks/agent-cap.js` — gov's own and both adopters — is a no-op for a `--hook-path` repath: settings-merge prints "already wired" and exits 0 without moving the command. AC2 therefore cannot be satisfied on any already-wired settings file, and when S2 withdraws the `.claude/hooks/` destination the wired command names a path that no longer ships. That is the silent unwiring of the fan-out guard, which the unit's own §5 calls the highest risk in the build, and the unit's own mitigation (S4 reports, does not red) does not repair it. Rewriting a stale hook path is precisely the capability the tool defers, so S1's claim is inverted, and §10's "the exact extension point, already parameterised" does not survive the dedup branch it sits above.

**Fix.** Add a scope item for the capability settings-merge does not have: either a `--rewrite-stale-path` mode replacing a command whose marker matches but whose path differs, or a fragment-level `hook_path` compare distinct from the marker compare. Add an AC observing an already-wired `.claude/hooks/agent-cap.js` settings file being MOVED to the shipped copy. Correct §10 — `merge(obj, hook_path, frag)` at `:91` is parameterised for the FIRST write, not for a repath.

**Left-shift gate.** Extend `tools/check-wiring.sh` with an arm asserting that every wired hook command resolves to a TRACKED file, so a settings file naming a withdrawn copy reds instead of running with a dormant guard. That arm is the durable answer to the whole class and is worth landing whether or not TOOL-14 lands.

---

### B4 — BLOCKER — every acceptance observation in the fail-open unit names a file that does not exist

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-4.md` §2 S3, §5 "testing + left-shift gates", §6 AC1, AC2 and AC3; and `…-TOOL-dRetiredFork-14.md` §6 AC3 and AC5, which repeat the path. *(Filed twice by two lenses; merged here.)*

**The defect.** S3 puts the new arms in `.claude/hooks/agent-cap.test.sh`, and AC1-AC3 all invoke `bash .claude/hooks/agent-cap.test.sh`. That file does not exist, tracked or on disk. `git ls-files | grep agent-cap` returns `.claude/hooks/agent-cap.js`, `tools/hooks/agent-cap.js` and `tools/hooks/agent-cap.test.sh`; `.claude/hooks/` holds three `.js` files and no test file at all. The suite is `tools/hooks/agent-cap.test.sh`, which is what the `agent-cap self-test` leg runs. §5's assertion that "`.claude/hooks/agent-cap.test.sh` is already a bar leg" is therefore a checkable falsehood about existing code, and the spec is internally inconsistent besides: S1 puts the fix in `tools/hooks/agent-cap.js` while S3 puts its arms in a sibling path that does not exist.

**Why it is a blocker.** The unit closes a fail-open in the guard that enforces the fan-out bound, and it has zero performable acceptance criteria. A builder either runs nothing or silently substitutes a path the spec never sanctioned, and AC1's staged-RED observation cannot be recorded against any file. TOOL-14 repeats the path in two of its own criteria, where it is doubly wrong: that unit's S2 withdraws the `.claude/hooks/` destination entirely.

**Fix.** Replace `.claude/hooks/agent-cap.test.sh` with `tools/hooks/agent-cap.test.sh` in TOOL-4 S3, §5 and AC1-AC3, and in TOOL-14 AC3 and AC5. If the intent was that the suite moves alongside TOOL-14's single-ship change, say so explicitly and sequence it — TOOL-4 is order 1 and TOOL-14 is order 4.

**Left-shift gate.** A spec-audit leg over `memory/builds/*/spec/*.md` that extracts every path token appearing in a §6 criterion's command position and refuses one that `git ls-files` does not name, with a waiver registry for paths a unit is creating. This single arm would have caught B4 and L1 and would have flagged H12's template site.

---

### B5 — BLOCKER — the unit's §1 premise is inverted at HEAD, and its staged RED is unstageable *(filed HIGH, graded BLOCKER here)*

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-4.md` §1 Goal, §4 Migration, §6 AC1 and AC2.

**The defect.** §1 states that "a marked sequential-agent loop nested inside another loop exits `0` where the unnested form exits `2`". Reproduced against gov HEAD, in both shapes, through the live hook. The nested case — a marked `for` loop inside an unmarked outer `for`, the exact fixture from `tools/hooks/agent-cap.test.sh:357` — exits **2**, and the hook's own message names the enclosure: "the marked loop is itself inside a loop opened at line 3, which multiplies its bound by a count nothing here can size". The unnested marked loop exits **0**. The direction in the spec is backwards. The machinery it says is missing is already present: `checkSeqMarker` carries the enclosing-opener brace walk at `tools/hooks/agent-cap.js:729-740`, `:949` states the rule outright ("NESTED LOOPS FAIL CLOSED WITH NO EXTRA CLAUSE"), `tools/hooks/README.md:48` already owns the clause, and the suite already ships the fixture with expected exit 2.

**Why it is a blocker and why the severity moved.** It was filed HIGH as a factual error, and a factual error in a §1 would ordinarily be one. It is graded BLOCKER here because of which fact it is: §1 decides whether this unit has any work in it. §4's claim that the behaviour is "currently unenforceable because nothing computes depth" is false, S2 is already done at HEAD, and AC1's observation — "the pre-change hook exited 0 on the same input" — cannot be staged, so the unit's one required RED does not exist. Combined with B4, this unit as written has no observable acceptance and no established defect. Whatever inCMS actually measured, it is not the shape §1 describes, and it may well be a different defect: an unbounded product of outer iterations times an admitted inner bound.

**Fix.** Restate §1 as the measured reproduction — the exact fixture, the outer and inner loop shapes, which carries the marker, and the observed exit code for each — then reconcile it explicitly with the `agent-cap.js:949` comment, saying whether that comment is wrong or describes only the unmarked case. AC2's admitted case must agree with whatever §1 then says. If the adopter's finding does not survive re-measurement at HEAD, the unit should be withdrawn or rescoped rather than rewritten around.

**Left-shift gate.** The rule already exists in the charter and wants a carrier: a new gate is not landed until its failing case has been observed. Make it structural for absorptions — a spec claiming to absorb a foreign fix must record the reproduction command and its observed pre-change exit code in §1, and a spec-audit arm refuses an absorption unit whose §1 carries no observed exit code.

---

### B6 — BLOCKER — the build's named highest-risk mitigation has no acceptance criterion

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-3.md` §2 S5, absent from §6.

**The defect.** S5 is the engine-enforced ordering that a wired hook command must move to the surviving copy BEFORE the second copy is withdrawn. Read in full, §6 carries AC1 (re-render), AC2 (regenerate), AC3 (empty refuse and rollback), AC4 (role change), AC5 (inert), AC6 (flag off), AC7 (read-only NicoCares) and AC8 (selftest). None mentions hooks, wiring or ordering. S6's own arm list omits it too — "a rendered row re-rendered; a version bump triggering its declared generator; a role change surviving a round trip; a failed render rolling back" — so the requirement is unobserved twice over.

**Why it is a blocker.** `TOOL-dRetiredFork-14` §4 delegates this constraint here verbatim: "`DEPL-dRetiredFork-3` is what makes that ordering enforceable rather than a runbook instruction", and TOOL-14 §5 calls the resulting unwired window "the highest risk in the build". As specced, the build's own named highest-risk mitigation can ship unbuilt and unobserved while both units pass their Definition of Done. Read with B3, the exposure compounds: the repath is a no-op on wired trees, and nothing checks the ordering that would have caught it.

**Fix.** Add an AC of the shape: when a target's settings still name the withdrawn copy, `update --write` refuses the withdrawal (or refuses to proceed) naming the unwired window, observed against a fixture whose wired command points at the second copy. Name the S6 arm that exercises it.

**Left-shift gate.** The scope-to-acceptance join described at H13 covers this mechanically. The behavioural gate is the one named in B3 — a `check-wiring.sh` arm refusing a wired command that resolves to no tracked file — which turns this ordering constraint into something a bar can enforce at every adopter rather than something one verb remembers.

---

### H1 — HIGH — two gate legs named as obligations in five specs are not rows on the bar

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-16.md` §7 and §6 AC4; the same names in `…-TOOL-dRetiredFork-17.md` §7, `…-DEPL-dRetiredFork-3.md` §7, `…-DEPL-dRetiredFork-6.md` §7 and `…-DEPL-dRetiredFork-7.md` §7.

**The defect.** §7 names `runbook parity` and `gate-lint` as legs the unit must keep green. Neither is a row in `tools/gate-legs.json`: grepped over the full manifest, `runbook` occurs zero times and `ps-hygiene` zero times. Both scripts are tracked — `tools/govkit/check_runbook_parity.py` and `tools/gate-lint/ps-hygiene.py` — and neither is invoked by any leg. The repo's own backlog corroborates it: `TOOL-dScaffoldedMirror-15` records `check_runbook_parity.py` as having zero callers and being absent from `tools/gate-legs.json`, verified 2026-08-24, and aGuardedTally's review records `ps-hygiene` as wired to nothing over zero `.ps1` files.

**Why it is high and not medium.** These are not misspellings that resolve to a real leg under another name. They are obligations against legs that cannot run and cannot fail, in the §7 section whose entire job is to say what will catch this unit if it breaks. Five specs read as covered and are not. TOOL-16 AC4's direct invocation of `check_runbook_parity.py` is the only thing that actually exercises the runbook claim anywhere in the build, and it is a one-off with no leg behind it.

**Fix.** Either drop both names from every §7 that carries them and state plainly that the runbook claim is checked only by AC4's direct invocation, or add the missing legs — with their declared wall-clock ceilings and their `memory/project/testsuite-count-waivers.txt` rows, per the build-level rule — as an explicit scope item in the unit that needs them.

**Left-shift gate.** A spec-audit arm that resolves every leg name in a spec's §7 against `tools/gate-legs.json` and refuses an unresolvable one. This is the highest-yield mechanical check available to this build: it is a pure join over two tracked files, it cannot false-positive on a real leg, and it would have caught H1 and M6 in one pass.

---

### H2 — HIGH — the `contribute` falsification counts are inverted against the roster

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-6.md` §6 AC1 and AC2. *(Filed three times by three lenses; merged here.)*

**The defect.** AC1 requires the verb to propose "the six NicoCares fixes this build absorbed by hand" and AC2 "the three inCMS fixes". Read at the §1 of every order-1 unit, the actual split is the reverse. NicoCares sources TOOL-1 (`nc carve-out 5/20`), TOOL-2 (`nc 16/20` and `17/20`), TOOL-3 (`nc 9/20`) and the `nc 20/20` half of TOOL-9. inCMS sources TOOL-4 (`KIT_AGENT_CAP_DELTA` D1), TOOL-5 (`ABL-aFerriedToolkit-4`), TOOL-6 (the drift-audit derived note), TOOL-7 (`check-review-join.sh` ARM 2), TOOL-8 (`settings_json` and `check_settings_scope`) and the C21 half of TOOL-9. That is four NicoCares and six inCMS. The totals match at nine, which is how the swap hid.

**Why it is high.** §4 Rollout calls this pair "a genuine falsification test rather than a demonstration", and it is the unit's whole safety case: the verb must independently propose at least those nine or it does not work. As written, a CORRECT verb reds AC1 by proposing four at NicoCares and over-produces at AC2, so the test either fails a working implementation or gets silently re-read at acceptance time, which is the same as having no test. The set is also unlisted anywhere, so nobody can grade it without re-deriving the roster.

**Fix.** Replace both counts with an explicit table of the nine absorptions, each row naming the unit id, the adopter, and the adopter-side register row (`nc carve-out N/20` or the inCMS `KIT_*_DELTA` id). Derive the per-adopter counts from that table rather than restating them. Name the unit ids in the criteria so the population cannot drift from the roster again.

**Left-shift gate.** Put the absorption roster in the build README as a generated region and have `gen_build_index.py` derive the per-adopter counts from the order-1 units' own §1 provenance lines. A count typed beside a population the tree already owns is the rule this repo breaks most often, and this is a clean place to stop breaking it.

---

### H3 — HIGH — the `gov_commit` re-stamp is unreachable, and no unit owns the gap

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-2.md` §6 (the whole AC set), and the same absence in `…-DEPL-dRetiredFork-1.md` §6 and `…-DEPL-dRetiredFork-3.md` §6.

**The defect.** The README's build acceptance requires a run that re-stamps `gov_commit`. `_cmd_update` WITHHOLDS that stamp while any row carries `evidence: "unattributed"` — `tools/govkit/govkit.py:6566-6573`, which prints "The receipt is NOT re-stamped" and names the two escapes: `govkit adopt --re-adopt --write`, a different verb, or `--allow-ungraded`. Measured: NicoCares' `.governance/install.json` holds 32 such rows and inCMS's holds 30. DEPL-1 §1 independently states that every NicoCares row currently returns `rung=None`. Grepped across all 25 specs, no unit drives that population to zero — DEPL-1 S3 and DEPL-2 S5 only REPORT it.

**Why it is high rather than a second blocker.** It is a distinct mechanism from B1 and reaches the same wall from the other side, but unlike B1 it has an in-scope remedy already present in the engine, so it is a gap in the spec set rather than an unfalsifiable claim. It matters because `TOOL-dRetiredFork-12` F1 notes that `adopt --re-adopt` discards every other row's recorded base, which makes the obvious escape hatch expensive, and `--allow-ungraded` converts the build's stated verdict into an override.

**Fix.** Add a criterion — most naturally on DEPL-2, or on a new unit — that a read-only then `--write` run against each adopter leaves zero `evidence: "unattributed"` rows and re-stamps `gov_commit` without `--allow-ungraded`. If the residual-byte problem makes that unreachable, say so in the README's acceptance paragraph rather than burying it in a unit's non-goal.

**Left-shift gate.** A `govkit` selfcheck arm asserting that the stamp-withholding branch has a named clearing path in the same run, plus a drift-audit signal reporting each adopter's unattributed-row count so the number is observed continuously rather than at acceptance time.

---

### H4 — HIGH — 39 literal sites are handed to a unit whose declared population excludes them

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-8.md` §3 Non-goals, against `…-TOOL-dRetiredFork-13.md` §2 S1. *(Filed twice; merged here.)*

**The defect.** TOOL-8 §3 defers inCMS's residual "39 literal prefix sites" in `tools/check-wiring.sh` to `TOOL-dRetiredFork-13`. TOOL-13's S1 population is "the 32 remaining shipped test and selftest files", and its §3 excludes everything else; `tools/check-wiring.sh` is a checker, not a test file. The ratchet agrees: `tools/install-prefix-carried.txt:17` carries `tools/check-wiring.sh` with 6 occurrences as its own row, separate from `tools/check-wiring.test.sh` with 16 at `:18`. Grepping all 25 specs for `check-wiring` returns only TOOL-8, TOOL-14 (which calls it and adds S4 behaviour) and DEPL-7. No unit takes the sweep for the checker.

**Why it is high.** A §3 non-goal's job is to name the follow-up; naming one whose own scope excludes the work leaves the population undrained. The literals stay, so both adopters keep re-merging `check-wiring.sh` on every pull, and `TOOL-dRetiredFork-17`'s ban at order 9 lands over a population nobody drained — the "permanently red or immediately full of exceptions" state TOOL-17's own §4 says it must avoid, and against F2's stated requirement that the exception list start at zero. TOOL-8 §3's own arithmetic is also unreconciled: "+67/-25 residual lines of which roughly 90 travel" leaves about two lines, not 39 sites.

**Fix.** Either widen TOOL-13 S1 to name the non-test shipped checkers it must also sweep, re-deriving its population figure and naming the ratchet row, or add an S6 to TOOL-8 taking its own file's literal sites through the `KIT_REL` idiom in the same landing, with an AC on its ratchet row falling. Whichever is chosen, fix the pointer in TOOL-8 §3 so it names a unit that owns the work.

**Left-shift gate.** A spec-audit arm asserting that every unit id named in a §3 non-goal exists in the roster AND that the deferred work is named by a scope item in that unit — a cross-spec handoff join. Pair it with a pre-landing assertion for TOOL-17 that the carried-prefix ratchet's total is zero before the ban converts.

---

### H5 — HIGH — an acceptance criterion forward-depends on a unit five steps later

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-12.md` §6 AC6, with its own §8 F1. *(Filed twice; merged here.)*

**The defect.** AC6 requires that "a `govkit update` run reports the role change rather than silently reverting the file". Role-change-in-place handling is `DEPL-dRetiredFork-3` S3 at order 7; this unit declares `order 2`. Its own F1 recommends exactly that: "make `DEPL-dRetiredFork-3` handle a role change in place." Verified in the engine: `update` never rewrites a receipt row's role — there is no `row["role"] =` assignment anywhere in `tools/govkit/govkit.py` — and the write loop dispatches on the recorded role, with the comment at `:6026` stating "THE ROLE DECIDES, not the verdict". The only descriptor-versus-receipt role disagreement check is scoped `if schema < 2`, and both adopters are at schema 2 or 3.

**Why it is high.** M2's ordering axis forbids a sub-spec depending on a unit sequenced after it, and this is a real inversion rather than a stylistic one: at order 2 nothing in gov reports a role change, so AC6 is unmeetable when the unit is built. The unit then either lands with a waived criterion — which is how the `engine` to `rendered` revert its own §4 Migration warns about ships to both adopters — or sits unclosable for five steps.

**Fix.** Move AC6 into `DEPL-dRetiredFork-3` §6, which already owns S3 for exactly this, and replace it here with something observable at order 2: the parity arm in S3, plus a recorded statement that no re-pull happens before DEPL-3 lands. Alternatively raise TOOL-12's `order` above DEPL-3's 7 and re-sequence TOOL-13's dependency on it. Either way, state the dependency in §2 rather than only in §8.

**Left-shift gate.** An ordering arm in the spec-audit leg: parse each spec's `order <n>` from its status header, extract every sibling unit id named in §2 or §6, and refuse where a criterion names a unit whose order is greater. The declared orders and the ids are both already machine-readable, so this is a join, not a heuristic.

---

### H6 — HIGH — the ban conversion names the wrong arm, and two specs disagree about which arm it is

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-17.md` §2 S3, against `…-TOOL-dRetiredFork-13.md` §3.

**The defect.** S3 says "Convert arm 1 of `tools/check-install-prefix.sh` from a ratchet into a ban". Arm 1 is already a ban. The script's header at lines 4-6 declares `bash tools/check-install-prefix.sh` as "assert; exit 1 on an unwaived hit", against the reasoned exception registry `tools/install-prefix-waivers.txt`. The shrink-only RATCHET is the carried-prefix arm keyed on `tools/install-prefix-carried.txt`, invoked as `--write-ratchet`. TOOL-13 §3 states this correctly and in so many words — "arm 1 is the root-spelling ban, not the ratchet" — so the two specs contradict each other on which arm the closing unit's central mechanism changes.

**Why it is high.** The unit exists to make the fork class impossible to refill, and its central mechanism names an arm where the conversion is a no-op. The arm that actually carries the 656 recorded occurrences units 10-13 drain would be left untouched, so the class the build exists to close stays open — while §4's migration argument about draining a population before banning it is applied to an arm the spec never names.

**Fix.** Rewrite S3 to name the CARRIED-prefix arm and its ratchet file `tools/install-prefix-carried.txt`, and state what happens to arm 1's existing waiver registry — kept as-is, or merged into the new exception list. Reconcile the arm numbering with TOOL-13 §3 so one spelling survives the set.

**Left-shift gate.** Give the checker's arms explicit names in its header and have the spec-audit leg refuse a spec that names an arm of a tracked checker by a number the checker's header does not carry. Cheaper and nearly as good: a `--list-arms` mode on `check-install-prefix.sh` whose output is the vocabulary specs must quote.

---

### H7 — HIGH — the new registry file reds the unit's own named gate on landing

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-3.md` §2 S3 and S4, against §7.

**The defect.** S3 adds `memory/project/stale-header-waiver.txt`. Check 3 of `tools/memory-tree/check-memory-hygiene.sh` whitelists that directory by a hardcoded `case`, naming `legacy-files.txt`, `curation-debt.txt`, `id-orphan-waiver.txt`, `corpus-path-unresolved`, `unarmed-branches`, `method-carriers.txt`, `testsuite-count-waivers.txt`, `trace-waiver.txt` and `readme-contract.txt`, and echoing anything else into `fail 3 "unexpected entries (structure)"`. The population comes from `git ls-files`, so a new tracked registry file reds check 3. No scope item edits that case, and §7 names `memory hygiene` as a leg this unit must keep green.

**Why it is high.** The unit reds its own named gate the moment it lands. The mechanism for adding a registry without editing the engine is `PROJECT_REGISTRY_EXTRA` in `TOOL-dRetiredFork-15` S2 — order 5, three steps after this order-1 unit — so at order 1 the only available fix is the whitelist edit this spec does not scope. The precedent settles it: `readme-contract.txt` was added with its own case line, so the missing edit is a required scope item and not an inference.

**Fix.** Add an S7: "Add `F:stale-header-waiver.txt` to check 3's registry whitelist case in `tools/memory-tree/check-memory-hygiene.sh` in the same commit", and an AC observing `bash tools/memory-tree/check-memory-hygiene.sh` exiting 0 with check 3 reporting no unexpected entry for the new file.

**Left-shift gate.** This is the class `TOOL-dRetiredFork-15` S2 exists to end, so the durable gate is that key. Until it lands, add a check-3 arm that names the whitelist as the remedy in its failure text, so the next author of a registry file is told what to edit instead of discovering it on a red bar.

---

### H8 — HIGH — two specs take opposite dispositions of the same `--kits` dispatch defect

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-2.md` §8 F2, against `…-DEPL-dRetiredFork-7.md` §2 S5.

**The defect.** DEPL-7 S5 lists "the per-verb flag dispatch that parses `--kits` for `update` and discards it" among the defects it FILES because they "are not this build's to fix", with AC6 requiring a `memory/backlog/DEPL.md` row for each. DEPL-2 F2 recommends "fix the dispatch here". Both texts verified verbatim. DEPL-7 is order 2 and DEPL-2 is order 6.

**Why it is high.** M2 requires a disagreement between two specs to be fixed in exactly one document before the first code pass, and phrasing one side as a fork does not remove it — the fork never names DEPL-7's conflicting scope item. Built as written, DEPL-7 writes a backlog row saying the defect is unfixed, and DEPL-2 closes it four steps later, so the backlog ships a row that was already false. DEPL-2's own §3 also defers the sibling `--add-kits` defect to DEPL-7, which leaves the two flags handled inconsistently inside one spec.

**Fix.** Pick one owner. If DEPL-2 fixes it, promote F2 to a §2 scope item with its own AC and strike the `--kits` clause from DEPL-7 S5, leaving only `--add-kits` there. If DEPL-7 files it, change F2's recommendation to "do not fix here; the new-source pass runs unscoped until DEPL-7's filed row is built", and say what that means for AC5's read-only adopter run.

**Left-shift gate.** A spec-audit arm that extracts every `memory/backlog/*.md` row a spec proposes to WRITE and refuses where a sibling spec in the same build claims the same defect as scope. Failing that, the same cross-spec handoff join proposed at H4 covers it.

---

### H9 — HIGH — the criterion states behaviour the named helper cannot produce

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-1.md` §2 S1 and §6 AC1.

**The defect.** `pop_guard` takes four arguments — check-number, label, population-count, precondition-count (`tools/memory-tree/check-memory-hygiene.sh:199`) — and returns silently unless the PRECONDITION count is greater than zero (`[ "${4:-0}" -gt 0 ] || return 0` at `:202`). It does not refuse on an empty population; it refuses on a mis-segmented selector, and the comment above it says so deliberately: a freshly scaffolded repo with no builds yet is a legitimate empty. Every existing precondition — `PRE_ANYBUILD`, `PRE_RECORD`, `PRE_SPEC`, `PRE_STATUSY`, `PRE_BINDABLE` at `:206-216`, plus `PRE_REGISTRY` — keys on build, backlog or registry paths. None covers check 6's `INDEX_SET`, which spans guides, ledger shards, build READMEs and map dossiers. The spec, Tier-1 and correctly carrying no §4, names no precondition.

**Why it is high.** AC1 — "when check 6's population is empty … refuses naming check 6" — is false of the helper's actual contract. A call landing with a zero fourth argument returns silently and leaves check 6 exactly as green-by-absence as it is today, armed-looking and disarmed. The staged RED S2 requires cannot be produced without first authoring a `PRE_*` expression that does not exist, and nothing in the spec says so.

**Fix.** Add a scope item defining check 6's precondition expression — the un-segmented count of index-class files anywhere under `$M/` — and restate AC1 in `pop_guard`'s own terms: an empty check-6 population WITH a non-zero precondition reds naming the mis-segmented selector.

**Left-shift gate.** A `check-arms.py` assertion that every `pop_guard` call site passes a non-empty fourth argument, so a two-argument or three-argument call cannot land looking armed. Stage the break by dropping the fourth argument from an existing call and confirm RED.

---

### H10 — HIGH — the vacuity refusal's failing case is unreachable, and the arm count is wrong

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-5.md` §2 S1 and S2, §6 AC2.

**The defect.** AC2 requires observing that "when every arm is skipped, the same command exits non-zero naming the vacuity". `tools/codebase-map/selftest.py` defines 26 `test_*` functions, of which exactly two are guarded: `test_identifier_tokens_corpus_recall` (`:1165`, with guard exits at `:1186`, `:1194` and `:1218`) and `test_js_probe_against_the_lexicon` (`:1226`, guard exit at `:1246`). The other 24 are unconditional. S1's "four guarded arms" counts guard EXITS, not arms.

**Why it is high.** "Every arm skipped" is unreachable, so AC2 can never be observed and S2's refusal predicate is dead code the moment it lands — the same could-not-fail shape the unit exists to close, one level up. "Skip count equals arm count" is not even well defined against the suite's own registry while arms and guard exits are conflated.

**Fix.** Restate S1 as two guarded arms with four guard exits. Replace S2's all-arms-skipped refusal with a predicate that can actually fire — for instance, the corpus-recall arm skipping is itself a refusal in gov's own tree, where its guard (`coding-governance-agents.template.md` present, `:1184`) is satisfiable — and rewrite AC2 to observe that. Note in §4 that the same guard is unsatisfiable at any adopter by design, per the comment at `:1180-1183`, so a vacuity refusal keyed on it must be gov-only.

**Left-shift gate.** Make the suite print an arm census on every run — arms defined, arms run, arms skipped, with each skip naming its guard — and add a leg asserting the census's arms-defined figure against a derived count rather than a written one. That turns both the skip-that-looks-like-a-pass and the miscount into observable facts instead of prose.

---

### H11 — HIGH — "declines and reports" is a third behaviour the code does not have

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-16.md` §6 AC1, premise in §2 S1.

**The defect.** S1 says `govkit.py` "REFUSES to overwrite a leg the target wrote" and AC1 requires that "the run REPORTS that it declined to overwrite it". Verified: the refusal is `if nm in by_name and nm not in owned: raise Refusal(…)` — the guard at `:4680`, the raise spanning `:4681-4683` — inside `_cmd_apply` (`:4013`), with no local handler. The nearest `except Refusal` is `main`'s at `:7382`, which prints and returns 2, and it is reached AFTER the write and stage loop at `:4300-4341`. The refusal also fires only on a NAME COLLISION; a non-colliding project leg is carried in `existing` and rewritten at `:4734-4736` with no report at all.

**Why it is high.** Neither branch of AC1 is observable. A colliding name aborts the verb at exit 2 with a partially applied install, and a non-colliding name is preserved silently. "Declines and reports" exists in neither branch, and §4 says nothing in gov changes behaviourally, so the unit builds no such report. AC1 also pre-answers F1, which S3 declares a fact-question the observation is supposed to decide.

**Fix.** Correct the citation to `:4680`. Split AC1 into the two real branches — a non-colliding name survives with no report; a colliding name raises `Refusal` and exits 2 after the write loop — and add a scope item for whichever behaviour the unit actually wants.

**Left-shift gate.** A `selfcheck` arm asserting that every `raise Refusal` inside `_cmd_apply` is reached before the write loop, or is documented as a post-write abort. A refusal that fires after bytes have landed is a distinct and worse contract than one that fires before, and nothing currently distinguishes them.

---

### H12 — HIGH — the adopter that must render the new token cannot render it

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-12.md` §2 S1 and S2; §10 checked the memory-tree descriptor rather than the unattended adopter.

**The defect.** S1 declares `placeholders = ["KIT_DIR", "TOOL_ROOT"]` and S2 says the render is "produced by the adopter the descriptor already declares rather than by a new mechanism". `tools/unattended/adopt-unattended.sh` substitutes only `{{KIT_DIR}}` (line 222) and never computes or substitutes `TOOL_ROOT`. That pair exists solely in `tools/memory-tree/adopt-memory-tree.sh`, which computes it at lines 36-37 and substitutes it at line 85 — and whose `render()` is hard-wired to one template with a fixed token list, so it cannot execute this either.

**Why it is high.** The unattended adopter cannot render a `{{TOOL_ROOT}}` token, so an unresolved brace would ship to every adopter — the exact failure §5 says must be a refusal. §10 cites memory-tree's `role = "rendered"` rows as proof the pattern is live, which checks the DESCRIPTOR and not the adopter that has to execute it, so the unit's own reuse audit confirmed the wrong half. The token is unnecessary besides: all five literals in `playbook.fixture.md` (lines 11, 12, 13 and 16) are `tools/unattended/…`, entirely under the kit dir, so `{{KIT_DIR}}` alone covers them.

**Fix.** Drop `TOOL_ROOT` from S1's placeholder list, since `KIT_DIR` covers all five sites. If it is wanted for a reason not stated, add an explicit scope item porting the computation and substitution from `adopt-memory-tree.sh:36-37,85` into `adopt-unattended.sh`, with an AC observing the token filled at a foreign prefix.

**Left-shift gate.** A gate over every shipped template asserting that each `{{TOKEN}}` it contains is substituted by the adopter its descriptor names — a join between the template's tokens and the adopter's substitution list — and a post-adopt arm refusing any installed file containing a residual `{{`.

---

### H13 — HIGH — the class-wide sweep the scope requires has no criterion, in the spec's own words

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-4.md` §2 S2, absent from §6.

**The defect.** S2 requires the same stdin treatment "at every other site that builds a pathspec from a derived population, found by grep rather than by memory — one fixed call site leaves the class open". §6 holds only AC1 (the lf-pin dirty check at over 32 KiB), AC2 (S4's refusal instead of a traceback), AC3 (selftest with S3's arm) and AC4 (selfcheck). Nothing observes any other pathspec-building call site.

**Why it is high.** This is the charter's named failure — "fixing one file and scanning only that file certifies coverage you do not have" — committed by a spec that states the rule against itself one paragraph earlier. The unit can pass every criterion having fixed exactly the one call site whose crash was reported, leaving the remaining argv-bound sites to crash the next large adopter AFTER a partial write, which is the harm §1 correctly identifies as worse than a refusal.

**Fix.** Add an AC naming the grep and its result: the enumerated site list, each site's disposition, and a check or arm asserting that no remaining `git … -- <derived list>` argv construction survives in `tools/govkit/govkit.py`.

**Left-shift gate.** A `selfcheck` arm that greps `govkit.py` for a subprocess argv built by splatting a derived list into a git pathspec and refuses an unwaived hit. That is the class gate; AC1 is the instance. Run the candidate predicate over the tree before wiring it, printing hits and near-misses, per §7.

---

### H14 — HIGH — the resolver requirement has no criterion, and byte-identity cannot catch a residual literal

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-8.md` §2 S3, absent from §6.

**The defect.** S3 requires every existing arm in `tools/check-wiring.sh` to read through `settings_json()` "so no caller keeps a second answer to the same question", and no criterion observes it. AC1's byte-identity cannot: §4 Migration states outright that gov's own tree keeps its settings file in the worktree, so the resolver returns the same path the literal spells and gov's arm count is unchanged. AC3 grades the resolver's own refusal rather than each caller, and AC2's "still grades the wiring" is not written tightly enough to catch an arm passing by absence.

**Why it is high.** A caller left on the literal passes AC1-AC5 unchanged and reproduces at inCMS the precise false-green — `ARCH-dBriskLanyard-1 S10` — that this unit exists to close. The defect survives the unit that names it, and the acceptance set is structurally incapable of noticing.

**Fix.** Add an AC observing zero remaining `.claude/settings.json` literals outside `settings_json()` in `tools/check-wiring.sh`, or an arm run against an out-of-worktree fixture asserting that EVERY arm's verdict changes rather than only the resolver's.

**Left-shift gate.** The out-of-worktree fixture is the durable answer and should be a permanent arm of `check-wiring.test.sh`: point the settings file outside the repo root and assert each arm's verdict individually. A single-answer invariant is only provable where the two answers differ, and gov's own tree is the one place they cannot.

---

### H15 — HIGH — gov's own OPEN row already decided this remedy, against the shape the unit absorbs

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-4.md` §1 Goal, and §10.

**The defect.** gov holds an OPEN record for this exact defect — `TOOL-aNumeralWarden-2` at `memory/backlog/TOOL.md:79`: "agent-cap's enclosing-opener walk is defeated by two nested wrappers or 59 lines of distance between the `.map` and the `agent(` call; it needs a statement-level walk, not an opener count, and the 58/59 boundary is unfixtured." The spec cites only foreign ids — `KIT_AGENT_CAP_DELTA` D1 and `ABL-aFerriedToolkit-3` — and a grep of the whole build folder returns zero hits for `NumeralWarden`.

**Why it is high.** The row decided the remedy and decided AGAINST the shape S1 absorbs: `interpDepths` is a depth stack, an opener count one level smarter, over the same 60-line window the row names — real at `agent-cap.js`, `for (let k = i; k >= 0 && k > i - 60; k--)`, untouched by S1. Landing it would close the nested-wrapper arm, leave the distance arm open, and make the row read as fixed. The row is not on the by-design open list, so nobody re-opens it. The §10 probe claims terms including "nested loop" and "fail-open" and still missed the one gov record that binds the change, which is what makes this a review finding rather than an authoring preference.

**Fix.** Cite `TOOL-aNumeralWarden-2` in §1 and add a scope item deciding it explicitly: either the absorbed stack is a partial fix and the row stays OPEN with its residual restated — the distance arm, unfixtured — or S1 widens to the statement-level walk the row prescribes. Add an AC over the 59-line-distance case so the residual is observed rather than assumed.

**Left-shift gate.** A spec-audit arm that runs `memory-recall` over each unit's §1 subject and refuses a unit whose §1 cites no gov-family id where an OPEN backlog row names the same file. The corpus already holds the answer; nothing currently forces a spec to have asked it.

---

### M1 — MEDIUM — byte-identical output and an unconditional observability line cannot both hold

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-3.md` §6 AC5, against §5 observability and §8 F2.

**The defect.** AC5 requires that with no header malformed, `--check` output is "byte-identical to the pre-change run". §5 requires the run to name how many headers were tolerated by waiver "on every invocation", and F2 recommends printing `0 tolerated` unconditionally, on the stated ground that a clean run printing nothing is indistinguishable from a check that never ran. A new unconditional line makes the output non-identical; byte-identity forbids the line.

**Why it matters.** One of the two must be abandoned at build time with no record of which, and the casualty a builder is likeliest to drop is the observability line — which is the exact failure F2 invokes.

**Fix.** Resolve F2 in the spec, then scope AC5 to what should not change — the exit code and the check-6 and check-12 verdict lines — rather than to whole-output byte identity.

**Left-shift gate.** The liveness rule already in §7 wants a carrier: a leg asserting that every checker prints a non-empty count line on a clean run. Adopt it and AC5's byte-identity becomes impossible to write in this shape.

---

### M2 — MEDIUM — the adopter-facing half of the unit has no criterion

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-3.md` §2 S4, absent from §6.

**The defect.** S4 ships the waiver file to adopters with header rows and no entries, and gives the memory-tree `kit.toml` a matching `[[hole]]` with a discharge probe. AC1-AC6 all exercise gov's own tree: malformed header, waiver row, stale row, absent registry, byte-identity, kit-version bump. Nothing observes the adopter-facing half, and §7 does not list `govkit selfcheck` either, so no named gate covers the descriptor.

**Why it matters.** The consequence is adopter-breaking rather than cosmetic. AC4 makes an absent registry a REFUSAL, so an adopter pulling the new memory-tree kit without the shipped registry gets a `collect()` that refuses on their own bar. The corpus already records the neighbouring hazard: aFerriedDossier logged a `[[hole]]` whose discharge probe was hardcoded to `exit 1` and could never close.

**Fix.** Add an AC observing the `[[hole]]` and its discharge probe — `python tools/govkit/govkit.py selfcheck` accepting the new hole, and an `apply` against a fixture landing `memory/project/stale-header-waiver.txt` with its header rows and zero entries.

**Left-shift gate.** A `selfcheck` arm asserting that every `[[hole]]` has a discharge probe that has been observed to both pass and fail, so a probe that can never close cannot land.

---

### M3 — MEDIUM — the spec declares an acceptance criterion and then does not write it

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-3.md` §5 user docs, absent from §6.

**The defect.** §5 states that "WIRE-INTO-PROJECT.md maintenance section SHRINKS, because the obligations it lists become declarations. That shrinkage is an acceptance criterion, not a side effect." §6's AC1-AC8 contain no criterion touching `WIRE-INTO-PROJECT.md` or the maintenance section at all.

**Why it matters.** This is a self-contradiction on the document's face rather than a reviewer preferring an extra criterion. The consequence is the duplicate-carrier drift the build treats as a defect class elsewhere: the runbook keeps listing obligations the engine now performs, unobserved.

**Fix.** Add the criterion the spec says exists: the maintenance section's generator-obligation list is removed and `python3 tools/govkit/check_runbook_parity.py` passes against the reduced section, with the removed obligations enumerated in the acceptance ledger.

**Left-shift gate.** A spec-audit arm that flags the literal phrase "is an acceptance criterion" appearing outside §6 and refuses where §6 carries no criterion naming the same artifact. Crude, and it would have caught this one exactly.

---

### M4 — MEDIUM — seventeen repath rows at one adopter against the README's fourteen across two

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-6.md` §6 AC2, against `memory/builds/dRetiredFork/README.md`'s problem statement.

**The defect.** AC2 requires the verb to class "the seventeen repath rows" at inCMS as class 4, layout carriage. The README splits the 44 classified rows across BOTH adopters as five genuine, "fourteen are gov spelling `tools/` into bytes it ships", eight gov defects, and the remainder — and 44 minus 5 minus 14 minus 8 is 17, which the README explicitly assigns to the OTHER class, "checkers with no way to be told what to scan and numbers with no owner". DEPL-6 §2 class 4 is the README's fourteen by definition, and both figures are gov-side classifications from this build's own pass, so they cannot be different populations.

**Why it matters.** Both numbers are load-bearing: the README's fourteen is an expected-improvement claim and AC2's seventeen is a pass/fail threshold for `contribute`'s classification. One of them is wrong, and the arithmetic suggests the seventeen was lifted from the adjacent class.

**Fix.** Re-derive both from `DEPL-dRetiredFork-7`'s census once it runs, and until then state AC2 without a count: classes every inCMS row whose only difference is the install prefix as class 4, and names them. If seventeen turns out right, correct the README's fourteen in the same edit so the two documents agree.

**Left-shift gate.** Same as H2: make the census the source and generate every per-class count into the README from it, so no classification figure is authored beside the population it counts.

---

### M5 — MEDIUM — the version-bump criterion cannot fail

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-7.md` §6 AC5, and `…-TOOL-dRetiredFork-10.md` §6 AC6.

**The defect.** Both units close with "`bash tools/check-kit-versions.sh` exits `0` after the bump" as the observation of their review-harness version bump. That gate only presence-checks the review-harness version: line 24 is `need "tier2-review meta.version" tools/workflows/tier2-review.js "version: '$V'"`, a format assertion via the `need()` helper — unlike the drift-audit block in the same file, which does an explicit meta.version-versus-constant-versus-marker comparison. There is also no `gov:kit review-harness@` marker in `check-review-join.sh`, `check-verifier-fanout.sh` or `check-workflow-syntax.js`, so TOOL-7 S4's "its `gov:kit` markers" and TOOL-10 S5's "with their paired markers" name a pairing that does not exist for these files.

**Why it matters.** The gate exits 0 today and exits 0 whether or not the review-harness version moved, and neither unit edits `tier2-review.js` where the version actually lives. The bump is unobservable — green-by-absence, in the acceptance of the very unit absorbing an arm to catch that class. The repo already knows: `memory/backlog/TOOL.md:253` (`TOOL-dTieredTribunal-6`, OPEN) records the identical gap.

**Fix.** State the bump concretely — bump `version:` in `tools/workflows/tier2-review.js` — and replace the criterion with one that can fail: `tier2-review.js` reports a `version:` strictly greater than its value at `b0108f13`, and `bash tools/check-kit-versions.sh` exits 0. Drop the markers clause from TOOL-7 S4 and TOOL-10 S5, or add the markers and the pairing to `check-kit-versions.sh` as scoped work.

**Left-shift gate.** Close `TOOL-dTieredTribunal-6`: give the review-harness row the same three-way comparison drift-audit's row already has, so a bump that moves one token and not the other reds.

---

### M6 — MEDIUM — the restatement gate is conflated with the parity gate that owns the five values

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-4.md` §6 AC5, and §7.

**The defect.** AC5 reads: "`bash tools/check-agent-cap-restatement.sh` exits `0`, so the five machine-compared values in the charter still agree with the hook." That script's own header states a different job — no live prose ASSERTS a fan-out bound as a bare number — a bare-digit ban over prose carriers with a positional waiver registry. The five machine-compared values are the PAIRS list in `tools/check-playbook-parity.sh` S2, four of which extract from `tools/hooks/agent-cap.js`, the exact file this unit edits, and `AGENTS.md` §8 names that script explicitly for them.

**Why it matters.** The AC's stated inference is false: a green restatement gate says nothing about the five value-parity pairs. A builder who changes the hook's depth handling and reads this AC believes the charter's values were re-verified when the gate that verifies them was never run. §7 does not list `playbook parity` either, so the gate that would actually verify the claim is named nowhere in the unit, and §7's `agent-cap restatement parity` is not a leg name — the manifest has `agent-cap restatement`.

**Fix.** Split AC5 into its two observations, one per gate, and add `playbook parity` to §7.

**Left-shift gate.** The §7 leg-name join proposed at H1 catches the leg-name half. For the inference half, have each checker's header state what it does NOT check — the charter already requires this — and have the spec-audit arm quote that line back when a spec attaches a conclusion to a gate.

---

### M7 — MEDIUM — one of the three scripts already applies a marker filter

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-10.md` §3 Non-goals, first bullet, and §2 S2.

**The defect.** The non-goal states that "`check-review-join.sh:56` and `check-verifier-fanout.sh:45` apply no marker filter", and S2 builds on it: "`check-workflow-syntax.js` already applies `MARKER` … the other two do NOT". False for `check-verifier-fanout.sh`: after its prefix filter it applies a marker grep — `^[[:space:]]*export[[:space:]]+const[[:space:]]+meta[[:space:]]*=` — under a comment saying a workflow script identifies itself by exporting `meta`, the same marker `check-workflow-syntax.js` uses. Only `check-review-join.sh` is genuinely marker-less.

**Why it matters.** S2 prescribes basename anchoring for a script whose population is already narrowed by a marker, and the build-level measured refusal — deleting the filter admits `.claude/hooks/agent-cap.js` and reds the bar — was measured on review-join and does not transfer, because neither agent-cap copy exports `meta`. §5's risk about a basename anchor being wider than a path prefix is therefore mis-scoped across the three scripts.

**Fix.** Correct the non-goal to name `check-review-join.sh` alone. In S2, treat `check-verifier-fanout.sh` the way `check-workflow-syntax.js` is treated — its existing `meta` marker becomes the population — and keep basename anchoring only for `check-review-join.sh`, whose population has no marker to fall back on.

**Left-shift gate.** Have each of the three scripts print its resolved population size and its filter chain under a `--list` mode, and add a leg asserting the three populations against derived counts. A spec would then quote a measurement rather than a reading.

---

### M8 — MEDIUM — the reuse audit records a probe run for a different unit's question

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-3.md` §10.

**The defect.** §10 cites `python tools/codebase-map/reuse_lookup.py "derive a kit file's install prefix at runtime instead of spelling it"`, and its recall terms are `carve-out, install-prefix, KIT_REL, carried, relocate, rung, adopter, divergence, repath, govkit, receipt, unattributed, derive, prefix` — byte-identical to the terms line in `TOOL-dRetiredFork-10` and sharing `DEPL-dRetiredFork-1`'s tail. This unit is a `StaleHeader` parse-failure distinction in `gen_build_index.py` plus a waiver registry, and not one of the fourteen terms touches header parsing, `collect()`, waivers or the build index.

**Why it matters.** `TEMPLATE-SPEC.md` states the terms line's whole purpose: BUILD-METHOD M7's regrounding step 5 re-runs the query FROM that line. A resumed session therefore regrounds this unit against the install-prefix corpus and gets nothing about the question the unit actually asks. The section passes check 12 on shape while recording a probe that was never run for this unit — which is the hole `TEMPLATE-SPEC.md` itself names: the check cannot see whether either fact is TRUE.

**Fix.** Re-run the probe for this unit's actual question and record it — something along the lines of distinguishing a malformed header from an absent one when parsing build READMEs — with terms drawn from this unit's own jargon: `StaleHeader`, `collect`, `waiver registry`, `shrink-only`, `header region`, `parser`, `tolerance`, `gen_build_index`, `staleness arm`, `legacy-files`. Keep the finding paragraph before the terms marker.

**Left-shift gate.** A check-12 extension: refuse a §10 terms line that is byte-identical to another unit's in the same build unless the two units name the same file in §2. It cannot see truth, but it can see copy-paste, which is what this was.

---

### L1 — LOW — a citation four lines short, and a python program invoked with bash

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-16.md` §2 S1 and §6 AC4.

**The defect.** S1 cites `govkit.py:4676` for the refusal "overwriting a leg the target wrote silently deletes their own coverage". At HEAD the guard is at `:4680` and the raise spans `:4681-4683`; `:4676` is the condition of the guard-drop branch whose body at `:4677` is `dropped.append((s, "matches no tracked path in the target"))` — a different mechanism. The companion citation `:4627` for `owned` is correct, so this is not a uniform offset a reader can absorb. Separately, AC4 invokes `bash tools/govkit/check_runbook_parity.py`, which opens `#!/usr/bin/env python3`; it is the only `bash <python file>` in the 25-spec set.

**Why it is low.** Both are mechanical and neither changes the unit's design. They are reported because the unit's whole premise is "document the extension point that already exists", so a reader following the citation lands on the wrong mechanism, and because AC4 as written fails on invocation rather than on the property it grades.

**Fix.** Change the citation to `tools/govkit/govkit.py:4680`, or cite the symbol and the quoted string without a line number as the rest of the spec does. Change AC4's command to `python3 tools/govkit/check_runbook_parity.py`, and settle in §7 whether it is a bar leg — see H1; `runbook` appears zero times in `tools/gate-legs.json`.

**Left-shift gate.** A spec-audit arm resolving every `<file>:<line>` citation in a spec: the file must be tracked, the line must exist, and where the spec quotes a string it must appear within a few lines of the citation. Line numbers drift with every commit, so the durable form of the fix is to prefer symbol-plus-quote citations and let the gate enforce the quote.

## What round 2 should not re-derive

Three things were checked and are CLEAN, recorded here so a second round does not spend tokens on them.

`TOOL-dRetiredFork-18` is correct in every citation it makes: `_render_wrapped_ids` is at `gen_build_index.py:822`, its docstring says what the spec quotes, its selftest arms are where the spec says, and the two emission sites at `:773` and `:777` do not call it.

The Tier assignments were read against the work each unit describes and no unit is under-tiered. The set's Tier-1 units are genuinely mechanical, and the Tier-1 LIGHT profile is used correctly throughout — a Tier-1 spec here carrying only sections 1, 2, 3, 6, 7 and 9 is conformant and was not reported.

The parked decisions in the README were read against every §8 fork in the set, and no fork's recommendation contradicts one. `TOOL-dRetiredFork-14`'s treatment of the fan-out cap is the closest call and it stays on the right side: it halves the carrier count without touching the number, exactly as the parked decision reserves.
