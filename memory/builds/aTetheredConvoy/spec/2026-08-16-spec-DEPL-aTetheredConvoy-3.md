# DEPL-aTetheredConvoy-3 — the convergence ratchet: nothing new ships un-deployable

**Status:** OPEN · rev-1 · 2026-08-16 · node a · Tier-2 · base 0f0a121d · streams deployer+tooling

## 1. Goal

Make it mechanically impossible for a new moving part in this repo to ship without being deployable.
The surface predicate already forces a new `tools/` directory to be CLAIMED by a declaration; it does
not force that declaration to be complete, to name the kit's gate legs, to claim its version
constant, to cover a file added inside the kit, or to deploy anything at all. Four correspondences
and one execution close all five.

## 2. Scope (IN)

- **S1 — leg correspondence, both directions.** Every `[[gate_leg]]` a descriptor declares names a
  leg that exists in `tools/gate-legs.json`; every leg in that manifest is claimed by exactly one
  descriptor's `[[gate_leg]]` or carried by a new `[[exempt_leg]]` row in `registry.toml` with a
  non-empty reason. An `[[exempt_leg]]` naming a leg that no longer exists reds — the same shape and
  the same staleness rule as the existing path exemptions.
- **S2 — version correspondence, both directions, as a FAILURE.** The cross-check between each
  descriptor's `version_from` and the version gate's own list becomes a problem rather than a note.
  `version_from` accepts a LIST of tables, because one entry versions three files. A constant claimed
  by no entry is carried by an `[[exempt_version]]` row with a reason, on the same staleness rule.
- **S3 — per-file claim inside a kit home.** Every tracked file under an entry's `home` is matched by
  at least one of that entry's file rules. Derived from `git ls-files`; no new population. This is the
  arm that catches a file added to a kit whose includes are a literal list.
- **S4 — the surface widens to `skills/*`.** The deployer's own Skill becomes an exemption carrying
  its reason. A future skill then reds until a declaration claims it, which is the state every other
  tracked deployable surface is already in.
- **S5 — the deployability leg.** One new gate leg drives `plan` and two `apply` runs for EVERY
  registry entry into a hermetic scratch repo and asserts three things per entry: an entry declaring a
  landable role lands at least one byte; `plan`'s promised destination set equals the receipt's path
  set; and the second `apply` changes no path and no hash. Every other arm in this build compares a
  declaration against a declaration. This one executes the product.
- **S6 — an `[[exempt_leg]]` may not name a leg a descriptor also claims**, and the same for
  `[[exempt_version]]`. An exemption and a claim for one fact is the two-spellings class arriving
  through the escape hatch built to prevent it.
- **S7 — the repairs S1 and S2 surface at base**, listed in §4 rather than discovered by the builder:
  two version constants absent from the gate's list, three constants no entry claims, two entries that
  own a file a gov leg runs while declaring no leg, and one prose count inside the file whose own
  header bans prose counts.

## 3. Non-goals (OUT)

- **Repairing what the arms find beyond S7's list.** S7's repairs are the ones measured at base and
  needed to make the new arms green. A disagreement this spec has not named is a backlog row; a unit
  that repairs whatever its own new gate happens to find has no bounded diff.
- **Deciding which legs a target SHOULD receive.** The correspondence forces every leg to be either
  claimed or exempted with a reason. Whether a given leg is the right one for an adopter is the
  descriptor author's judgment, and this unit refuses to encode a second opinion about it.
- **Emitting a leg into a target.** That is unit 4. This unit asserts the declarations an emitter will
  read; it reads none of them at apply time.
- **Extending the arms-checker to a Python population.** Already an open backlog row, already reserved
  for the owner as a governance-carrier change. Unit 7's cross-check is where that guarantee lives.
- **A second harness.** S5's leg is per-registry-entry and unit 7's matrix is per-fixture-variant.
  Unit 7's spec folds S5's sweep in as one fixture family rather than shipping a second builder; the
  decision is recorded in BOTH specs so it cannot be re-decided by whichever lands second.

**Assumes:** unit 1 (S5's plan-equals-apply assertion is unit 1's AC4 quantified over every entry) and
unit 2 (S1 of that unit's role-completeness arm lives in the same `selfcheck`).

## 4. Design

### What escapes today, measured

**A1 — the descriptors and the leg manifest are two spellings of one fact, unasserted.** Reproduce by
reading both populations. Measured at base: seven declared leg names exist in no manifest leg at all,
and the large majority of manifest legs are claimed by no descriptor — including legs a target that
takes the kit plainly must receive: the memory-tree engine's own self-tests, the codebase-map adopter
end-to-end, the unattended kit's three, the review-harness's, and the flat gates'. The deployer
contract's own criterion specified the descriptor-to-manifest direction. Neither direction exists; the
one arm that reads the manifest reads it only to classify guard pathspecs, and it classifies GOV's
layout literals rather than the descriptors' token-spelled guards — the taxonomy has never been run
over the population it would grade.

**A2 — a disagreement about versions lives at exit 0.** `selfcheck` exits 0 today while reporting five
version disagreements as notes. That was correct for a unit that declared repairing them out of scope,
and it is wrong for a ratchet: a new kit whose version constant no entry claims is invisible.

**A3 — a new file inside a kit with a literal include list is claimed by nothing.** The surface is
depth-1 under `tools/`, so a file added inside an existing kit collapses to the directory, which is
already claimed. Measured exposure at base is one file, which is small and is not the point: the
predicate that would catch the next one does not exist.

**A4 — `skills/*` beyond the kickoff tree is outside every assertion.** A second skill directory is
already tracked and is in no entry, no exemption and no inventory the ratchet reads.

**A5 — a descriptor that parses and deploys nothing looks exactly like one that works.** The deployer
engine's own module docstring opens with that sentence about subcommands. It is now true of the
descriptors: the playbook entry has been in the default set landing zero bytes, and `plan` promised a
file set `apply` never wrote. Neither was caught by any declaration-versus-declaration arm, because
both declarations were internally consistent.

### Why four of the five arms add nothing to maintain

The tempting answer to "force new tooling to ship govkit-ready" is more declarations, and it is wrong
for the reason this whole tool exists: each new declaration is another spelling of a fact somebody
else already wrote. S1 through S4 assert correspondences between populations that ALREADY exist. The
two exemption tables they need are the minimum and are unavoidable — nothing in a leg's own row says
whether an adopter should receive it, and nothing in a version constant says whether it belongs to a
deployable — but they carry the same reason requirement and the same staleness rule as the path
exemptions, so a stale one reds rather than quietly widening the surface it was written to narrow.

S5 is the arm that does not compare declarations at all, and it is the one that would have caught both
of A5's defects.

### The deployability leg

Per registry entry, in a hermetic scratch repo: `intake` with synthetic answers derived from
`needed_answers` — already derived from the descriptors rather than hand-kept, so a kit that starts
needing a new token does not silently make this leg unrunnable — then `plan`, then `apply`, then
`apply` again.

Three assertions per entry, and one exclusion stated rather than assumed: entries whose adopter is
expected to fail are asserted on the LAND phase only, because `apply` already separates land from
configure and the known blocking hole in the default set is a designed state rather than a defect.
Entries declaring no landable rule at all are asserted to print the reason for each, which is unit 1's
role-landing closure quantified over the registry.

Cost is the real objection: the leg runs the deployer once per entry, twice for the idempotency half.
It is guarded on the descriptor and deployer paths, the runner is concurrent, and each fixture is its
own scratch tree. A records-only commit does not pay it.

### Liveness, for every arm

An assertion that finds nothing on a clean tree is indistinguishable from one that cannot find
anything, and this repo names that class. Each of S1–S5 gets a pair: silent against a scratch gov tree
where the two sides agree, red against a minimally violating one. S5's negative fixture retags a
landable rule to a role that lands nothing and asserts the leg reds — which is unit 1's measured
playbook defect reproduced deliberately.

One liveness half is specified more tightly than the others because the obvious version is vacuous:
the leg must also assert it EXAMINED every registry entry, by printing a derived count and reding when
that count is zero. A sweep that iterated an empty population and a sweep that found no problems
produce the same exit code otherwise.

### The repairs S7 carries

Measured at base by running `python tools/govkit/govkit.py selfcheck`, which reports the version half
as notes today, and by mapping every gov leg's argv paths to the entry that claims them:

- the playbook's template marker and the wiring checker's constant are absent from the version gate's
  list; two rows added.
- the two review-workflow scripts' constants are claimed by no entry; the review-harness entry claims
  them, which is what `version_from` becoming a list is for.
- the deployer's own constant is claimed by no entry and cannot be, because the deployer is a registry
  exemption; an `[[exempt_version]]` row states that rather than leaving a permanent note.
- two entries own a file a gov leg runs while declaring no `[[gate_leg]]` — so an emitter would deploy
  those kits without their gate. Both gain one.
- one exemption reason states the size of gov's leg manifest, which has grown. The number is deleted
  rather than restated, per the file's own charter rule.

### Rollout

1. **S1, S6 and the leg repairs** — the correspondence that closes A1, with both exemption tables.
2. **S2, S3, S4 and the remaining S7 repairs.**
3. **S5, the deployability leg**, with its four-gate obligations paid in the same commit.

### Files touched (estimate)

| Area | Files | Note |
|---|---|---|
| Core | `tools/govkit/govkit.py` | four new `selfcheck` arms |
| Registry | `tools/govkit/registry.toml` | two exemption tables, one surface glob, one prose repair |
| Descriptors | the entries whose legs or versions move | the count is DERIVED, and is deliberately not written here |
| Version gate | `tools/check-kit-versions.sh` | two rows; it is a `seed`, so adopters re-seed |
| Tests | `tools/govkit/selftest.py`, `tools/govkit/deployability.test.sh` | every arm plus its liveness half |
| Gates | `tools/gate-legs.json`, `AGENTS.md` | one new leg, cited in the charter |
| Map | `memory/map/features/govkit.md` | the new leg and the new seams |

### Alternatives rejected

**A contributing-docs checklist.** Rejected without argument: a rule no gate reads is a rule that
decays, and this repo's own trap list records that adding a moving part trips four gates precisely
because those four are mechanical.

**Key the leg correspondence on argv PATH rather than leg NAME.** Rejected. A path-keyed arm and a
name-keyed arm disagree about what may legally be unclaimed, and shipping both is the two-spellings
class inside the ratchet. The name is the identifier the manifest, the runner's output and the
descriptors all already use.

**Put `[[exempt_leg]]` beside the leg in `tools/gate-legs.json`.** Rejected: that file is read by the
runner on every invocation, and adding a deployer-only key makes the runner's input carry data the
runner ignores. The registry is already the home of "who owns this and why is that one exempt".

## 5. Production-readiness checklist

- security — read-only assertions plus one leg that writes into its own scratch trees. No target is
  touched.
- perf / scale — S5 is the cost: the deployer run three times per registry entry. Guarded, hermetic,
  and concurrent with the rest of the bar.
- a11y — N/A: gate legs with stdout only.
- i18n — N/A: developer tooling.
- error / empty / loading states — every arm reds naming the offender; the derived-count liveness half
  is what stops a zero-population run reading as clean.
- observability — `selfcheck`'s notes carry every derived count.
- risks — the arms red on a tree that is green today, which is the point and is still a landing cost:
  S7's repairs must be in the same commits as the arms that demand them. Second risk: S5's runtime
  grows with the registry, and a slow leg is a leg someone reaches for `GATE_JOBS=1` to avoid; the
  guard is what keeps it off records-only commits.
- testing + left-shift gates — the arms ARE the left-shift; each carries a liveness pair.
- migration / rollback — none; the arms are additive and the exemption tables start from the measured
  population.
- user docs — the charter's gate-suite section gains the leg.

## 6. Acceptance criteria

- **AC1** When `python tools/govkit/govkit.py selfcheck` runs, it reds naming the offender for a
  descriptor `[[gate_leg]]` whose name is in no `tools/gate-legs.json` leg, and separately for a
  manifest leg claimed by no descriptor and carried by no `[[exempt_leg]]`.
- **AC2** When an `[[exempt_leg]]` names a leg that no longer exists in the manifest, `selfcheck`
  reds calling it stale; and when a leg is BOTH exempted and claimed by a descriptor, it reds naming
  both sides.
- **AC3** When a descriptor declares a `version_from` file the version gate does not assert, or the
  gate asserts a constant no entry claims and no `[[exempt_version]]` carries, `selfcheck` exits
  non-zero — measured today the same conditions exit 0 as notes.
- **AC4** When an entry declares `version_from` as a LIST, every member is resolved and cross-checked
  independently, asserted against the review-harness entry claiming its three constants.
- **AC5** When a tracked file under an entry's `home` is matched by none of that entry's file rules,
  `selfcheck` reds naming the file and the entry.
- **AC6** When a tracked directory under `skills/` is claimed by no entry and no exemption,
  `selfcheck` reds; with the exemption row present it is silent; and removing the directory while
  leaving the row reds as stale.
- **AC7** When `bash tools/govkit/deployability.test.sh` runs, every registry entry declaring at least
  one landable role lands at least one byte into its own scratch fixture, and the leg prints a DERIVED
  count of entries examined. Liveness: a run over a registry with zero entries reds rather than
  passing.
- **AC8** When that leg runs, `plan`'s promised destination set equals the receipt's path set for
  every entry, and a second `apply` changes no path and no hash. Liveness: an entry retagged so no
  rule is landable makes the leg RED, which is the playbook defect reproduced deliberately.
- **AC9** When each of AC1 through AC6 is run against a scratch gov tree where the two sides AGREE, it
  is silent; against a minimally violating tree, it reds. Both halves per arm — `python
  tools/govkit/selftest.py` carries the pairs.
- **AC10** When `selfcheck` runs over gov after this unit lands, it exits 0 with every S7 repair in
  place, and its notes carry a derived figure for each correspondence rather than a spelled one.

## 7. Gates

`bash tools/run-gates.sh` green at the push boundary; `GATE_FULL=1` for the DoD. One new leg.

Adding a leg trips four gates at once, and this repo's manifest front-loads them as a trap worth doing
in one pass: the codebase-map coverage assert, the codebase-map freshness byte-compare, the
kickoff-manifest ratchet, and drift-audit's handkept charter signal, which is pinned with zero slack —
so the new leg's script path must be named in the charter's gate-suite section in the same commit.

`tools/check-kit-versions.sh` gains two rows and is a `seed` in its own entry, so the change reaches
adopters on their next re-seed rather than silently.

Before review: `python tools/memory-tree/gotchas.py --for-diff 0f0a121d..HEAD`.

## 8. Open questions

- **F1 — does S5's leg fold into unit 7's matrix, or stay its own?** RECOMMENDATION: stay its own, and
  unit 7 CITES it rather than re-asserting anything. The two answer different questions — every ENTRY
  deploys, versus the deployer behaves correctly across repo SHAPES — and the two assertions they would
  otherwise share, plan-equals-apply and apply-twice, stay here. The leg is bash and data-driven; the
  matrix must be Python for its source join, so neither can call the other. Deciding after both land
  costs a leg deletion, a charter edit, a drift re-drain and a map re-render. Recorded identically in
  unit 7's §3.
- **F2 — should S3 quantify over files a descriptor's rules match but that are UNTRACKED?**
  RECOMMENDATION: no. The population is `git ls-files`, matching every other predicate here, and an
  untracked file is not something gov ships. Stated because the natural implementation walks the
  filesystem and would then red on an operator's scratch file inside a kit directory.

## 9. Revision log

- rev-1 · 2026-08-16 · split out of the first unit's rev-1, which bundled the ratchet with the update
  verb and the prerequisite repairs. Two changes came out of the adversarial pass and are folded here:
  S6, because an exemption and a claim for one fact is the defect class arriving through its own escape
  hatch; and the derived-count liveness half on S5, because a sweep over an empty population and a
  sweep that found nothing are otherwise the same exit code. One arm proposed by that pass was DROPPED
  rather than adopted — a second leg correspondence keyed on argv path — because it would disagree with
  S1 about what may legally be unclaimed, and because once S1 lands it fires on nothing.

## 10. Reuse audit

Ran `python tools/codebase-map/reuse_lookup.py` for the correspondence assertions and the per-entry
sweep.

`selfcheck` is the declared single home for every registry-shaped assertion — the govkit dossier's own
reuse affordance says so — and all four correspondence arms land there rather than in a new engine.

The existing `[[exempt]]` rows, their non-empty-reason requirement and their stale-path refusal are
the shape `[[exempt_leg]]` and `[[exempt_version]]` copy exactly, including the refusal's sentence
about an exemption without a reason being an omission wearing a label.

The derived-`mutates_index` arm is the template for all four: derive the fact from the artifact,
assert it against the declaration, never trust the declared value.

`needed_answers` is reused unchanged as the source of S5's per-entry answers, because it is already
derived from the descriptors — a hand-kept answer list inside a test harness would be a fourth
spelling and would silently stop covering a kit that grew a token.

`mkrepo` in the codebase-map adopter's end-to-end test is the fixture builder S5 extends; the deployer
contract already committed to extending it rather than writing a second one, and this unit inherits
that.

No seam exists for the per-entry sweep's driver. It is a loop over the registry calling the product,
which is the point.
