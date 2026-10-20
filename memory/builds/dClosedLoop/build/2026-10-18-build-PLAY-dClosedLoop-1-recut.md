# The chain re-cut: the build order's owed moves and open questions

**Serves:** research PLAY-dClosedLoop-1

Step 3 of the owner's convergence order (the state record's `[convergence]`). v2's `[owed]` carried the
chain's order questions to a re-cut, and the state revisit found three decided moves unapplied and seven
items undecided. This record holds the owner's answers, the moves applied to v2's `[chain]`, the chain rows
reconciled with the ownership table, and each owed item's state.

## [words] The owner's answers, 2026-10-17

Asked as RC-1 to RC-7, the owner answered, verbatim:
- RC-1, dOrderedCharter reading `instructions.*` from a policy file its child builds: "Conduct a full tier2 review of the build ORDER and ensure it's correctly arranged."
- RC-2, `gap-design-01`'s owner: "Move it to dTotalRecall (Recommended)"
- RC-3, the kit confs and the policy file: "Fold all at convergence (Recommended)"
- RC-4 to RC-7, the four confirmations, all ticked: "RC-4 Instruction layer first,RC-5 Confirm v2's [open] items,RC-6 instructions.edit as it is,RC-7 Roles details to unit specs"

While the re-cut was being applied, the owner also asked, verbatim:

> run a review of the ownership table in parallel - instruct 3 independent agents to re-verify ownership

Dispatches 89 to 91 run it, from `build/2026-10-17-build-PLAY-dClosedLoop-1-ownership-verify.md`.

## [applied] The moves applied to v2's `[chain]`

- **Decided on 2026-10-16** (the state record's `[undecided]`), applied now:
  - dIndexedDesign follows dTotalRecall, whose house index and reuse entries its "reuse and alternatives
    backed by recorded probes" use;
  - `gap-orient-08` moves from dDeclaredLoop to dWellOiledMachine, with the executor (RT-3);
  - the deployer's and the maintainer's definitions move to dShippedRelease, which delivers distribution
    and integrations, and dTendedCadence, which delivers observability. dBoundRoles keeps their
    registration through the layer contracts.
- **Answered now:**
  - `gap-design-01` moves from dDeclaredLoop to dTotalRecall, whose level-0 map and relation graph close
    it (RC-2);
  - every kit conf key folds into the policy file at convergence. dConvergedCharter folds them, and until
    then a kit conf is its keys' legacy home, on a shrink-only list. v2's `[policies]` says so (RC-3);
  - the instruction layer stays first: dOrderedCharter is the chain's root, ahead of the flow (RC-4);
  - v2's `[open]` interpretations are confirmed (RC-5);
  - `instructions.edit` keeps its three values, its default from the owner's words (RC-6);
  - the roles layer's lower-level design goes to dBoundRoles's unit specs: the answered-call hook's range
    matching, the excerpt keys and a repair's carry (RC-7).
- **Held for the order review:** RC-1. The owner asked for a full Tier-2 review of the build order, and its
  findings settle where the policy file, its schema and its reader land.
- **The counts move:** dDeclaredLoop owns 17 gaps, from 19; dWellOiledMachine 29, from 28; dTotalRecall
  27, from 26.

## [reconciled] The chain rows against the ownership table

The probe lists each chain row's backticked citation of a node the approved table gives to another build:

```python
"""Which chain rows cite an item or a key the approved ownership table gives to another build?

Usage: python row_owner_probe.py   (from the worktree root)

Reads the owners from their declared fields, through the map's derivation, and each chain row of v2's [chain].
A citation of another build's node is either a call (the row's build uses it) or a claim (the row says it
builds it). The probe lists them; a reader classes each.
"""
import importlib.util
import re

B = "memory/builds/dClosedLoop/build/"
spec = importlib.util.spec_from_file_location("projectmap", B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py")
mp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mp)
A, ns = mp.derive()
owner = {}
for name in ("item", "policy-key"):
    for n in ns[name]:
        owner[n["key"]] = dict(n["rels"])["owner"][0]
v2 = open(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md", encoding="utf-8").read()
rows = dict(re.findall(r"^\| (d[A-Z][a-z]+[A-Z]\w+) \|(.*)$", v2, flags=re.M))
total = 0
for build, text in rows.items():
    hits = []
    for key, own in owner.items():
        if own == build:
            continue
        m = re.search(r"(.{0,70})`" + re.escape(key) + r"(?=`|:|=|\s)(.{0,50})", text)
        if m:
            hits.append((key, own, (m.group(1) + "`" + key + m.group(2)).replace("\n", " ")))
    total += len(hits)
    for key, own, ctx in hits:
        print(f"{build} cites {key} ({own}'s): …{ctx}…")
print(f"citations of another build's node: {total}")
```

```text
$ python row_owner_probe.py
dOrderedCharter cites memory.map-purpose (dTotalRecall's): …stry's purpose field, today's namespaces and chain builds reviewed as `memory.map-purpose` says | gap-found-01, gap-found-02, gap-found-03,…
dFairHearing cites preset (dDeclaredLoop's): … the spec-audit kind for design and architecture records, chosen by a `preset` argument that Design's breakpoint passes when ev…
dDeclaredLoop cites build.closes (dShippedRelease's): … accept every value, since `strict` and `guarded` must be refused for `build.closes` on a core-only install; the guard, the TTY CLI a…
dBoundRoles cites placement.check (dRankedPlan's): …ement disposition and its reason, the driver recording it and running `placement.check`; the trust mechanism (P29): inputs handed as con…
dTotalRecall cites instructions.edit (dOrderedCharter's): … the card, and the auto-memory's standing directives promoted through `instructions.edit` (MS-1); the `gov:note` grammar and the `annotati…
dMindYourWords cites instructions.edit (dOrderedCharter's): …ack census selects for the kits it discovers and by the owner through `instructions.edit` (LX-1), and a noun canon seeded from the corpus …
dShippedRelease cites test.seed (dWitnessedBar's): … own scoped grant; the install and update hooks that call `adopt` and `test.seed`, attended; the integrations import of an adopter…
dCalibratedLens cites memory.item-budget (dTotalRecall's): … and its reasoning returned by the step's producing role; each role's `memory.item-budget` derived from its p90 over 30 sliced work orders …
citations of another build's node: 8
```

- **All 8 are calls:** each row uses, reads or runs the node, as the ownership record's `[look]` already
  judged. None needs a change.
- **One conflict was in plain prose, which the probe cannot see.** dRankedPlan's row built the
  prompt-submit hook that writes the intake log, which PM-9 gives to dWellOiledMachine. dRankedPlan's row
  now reads the log, and dWellOiledMachine's builds the hook.
- **dDeclaredLoop's row names the entry step's items,** which PM-9 gave it.

## [owed-state] Each owed item's state

| Owed item | State | By |
|---|---|---|
| Settled by the runtime layer: the executor, its harness and the compaction checks | settled before | RT-3, RT-1 |
| The roles layer's lower-level design | goes to dBoundRoles's unit specs | RC-7 |
| The expansion roles' home | applied: dShippedRelease and dTendedCadence define them, dBoundRoles registers them | decided 2026-10-16 |
| The roles layer's mechanical shape | settled by the systems round | `[design-role-shapes]` |
| dTotalRecall's place in the re-cut | applied: dIndexedDesign follows dTotalRecall; dTendedCadence already did | decided 2026-10-16 |
| dTotalRecall and its gaps' owners | `gap-plan-06`: its owner dRankedPlan follows dTotalRecall; `gap-design-01`: moved to dTotalRecall | RC-2 |
| The tooling order | the instruction layer first, as the chain stands | RC-4 |
| dMindYourWords' second-wave packs | still waiting for an adopter census, so for the owner's ask at that build | deferred |
| The `next` verb lands with Runtime | answered: dWellOiledMachine lands the check with the laggards on a shrink-only list | dWellOiledMachine's row |
| Kit confs beside the policy file | every kit conf key folds at convergence, on a shrink-only list till then | RC-3 |
| dOrderedCharter's policy consumers | held for the Tier-2 review of the build order | RC-1 |
| gap-orient-08 follows the executor | applied: dWellOiledMachine's | decided 2026-10-16 |

## [order-review] The build order reviewed, and arranged

The owner's RC-1 asked for a full Tier-2 review of the build order. It ran as dispatch 94 and wrote
`reviews/2026-10-18-review-PLAY-dClosedLoop-1-chain-order.md`: CLEAN WITH FIXES, no blocker, 32 of 35 raw findings confirmed, 23 items, 6 of them high. Its verdict
says the order was not yet correctly arranged. Three of its items were the owner's to choose, and the owner chose,
verbatim:
- RC-1, where the policy file, its schema and its reader land, restated over the 17 keys the two roots own: "A new root build for it"
- RC-8, the placing items' keys: "Move both keys to dDeclaredLoop (Recommended)"
- RC-9, Plan's ratification before the intake hook lands: "A fallback until the hook lands (Recommended)"

### [order-fold] Each item, folded

| Item | What changed | Where |
| --- | --- | --- |
| H1 | the reconciliation tests ancestry over every backticked citation, and each non-ancestor citation carries a class; the root's `memory.map-purpose` review moves to dTotalRecall's PM-5 unit; dBoundRoles's `placement.check` is its ancestor's under RC-8 | `[reconciled-order]`; v2 dOrderedCharter, dTotalRecall |
| H2, M1 | RC-9: dRankedPlan's ratification falls back to an owner breakpoint until dWellOiledMachine lands the intake hook, which then re-points it and drains the fallback | v2 dRankedPlan, dWellOiledMachine |
| H3 | RC-8: `placement` and `placement.check` move to dDeclaredLoop with `gap-orient-01`, and a disposition rides the claim commit until the intake kind lands | v2 [policies], dDeclaredLoop, dRankedPlan; ownership `[amended]` |
| H4, M2, M11 | RC-1: dGroundRules, ahead of both roots, holds the file, schema, reader and a minimal guard, reads a key's default when the file is absent, and an arm reds on a root-owned key with no reader | v2 dGroundRules, dOrderedCharter, dFairHearing, dDeclaredLoop |
| H5 | `resolve_compare_base`, `derive_baseline_additions` and the pure `drop_touched_exemptions` move to `tools/lib` beside `compute_coverage`; the touch join calls the pure seam, the map's writer sits behind a point, and the claim arm renders "not installed" on a core-only tree | v2 dOrderedCharter, dScopedBuild, dWitnessedBar |
| H6 | RC-3 folds every kit conf key the retrofit does not convert, with a reader inventory by value, `transition_audit.read_modes` reading both homes keyed by commit | v2 [policies], dConvergedCharter |
| M3 | dWellOiledMachine re-points the laggards it seeds, the closed builds' commands, before it closes | v2 dWellOiledMachine |
| M4 | dGroundRules declares the legacy-homes list, red on a planted new key; dWitnessedBar converts it into a ledger population when its factory lands; dConvergedCharter drains it | v2 dGroundRules, dWitnessedBar, dConvergedCharter |
| M5 | dOrderedCharter registers its own seven namespaces; step, item and policy are armed by dDeclaredLoop, role by dBoundRoles and record by dTotalRecall | v2 dOrderedCharter |
| M6, L2, L5 | the probe reads five of the six owned kinds; systems are cited in prose and left out, and it says so | `[reconciled-order]` |
| M7 | `.githooks/gate-env.sh` and `tools/roles/house/policy.toml` are named as legacy homes; the reader extends `read_policy_key`'s contract; dBoundRoles's effort home is spelled out | v2 [policies], dGroundRules, dBoundRoles |
| M8 | `recall_conf.resolve`, `Conf.digest` and `extract.grammar_for` join the import list, derived by `git grep` | v2 dOrderedCharter |
| M9 | dShippedRelease follows dBoundRoles, whose contract registers the deployer; the critical path holds | v2 dShippedRelease |
| M10 | the state record's `[undecided]` and `[revisit-recut]`, and layer-memory's fold paragraph, point at the re-cut | the state record; layer-memory |
| M12 | a losing replay is routed: the slot's "not installed" terminal, the map load and its read count skipped, and not-in-view from the slice manifest alone; no new policy value | v2 dTotalRecall |
| L1 | each settled `[owed]` bullet states its state inline | v2 [owed] |
| L3 | each `instructions.edit` value gets its arm, and `flow-only` is refused at load until dDeclaredLoop lands | v2 dOrderedCharter |
| L4 | the `gov:note` grammar and the positional-reference migration are each named once | v2 dTotalRecall, dConvergedCharter |

The review did not compute the critical path. `[critical-path]` does.

### [critical-path] The critical path

A build's units are its planned-units clauses. A build starts when all its parents have landed, so the critical path
is the largest sum of units along a parent chain. Before the fold it was 168 units, and the candidate edges priced
for RC-1, RC-9 and M9 below are measured from it.

### [reconciled-order] The rows against their ancestors

The probe below replaces `[reconciled]`'s. Each backticked citation of another build's node must be built by the
citing build or an ancestor in the after relation, or carry a class in this table. A citation with no class, or a
class with no citation, is a finding.

Since the design audit's fold, 2026-10-18, the table classes every dependency kind the reconciliation probe reads:
cites, stage, routes, reads and registers. Each row names the rule that reads its dependency, and is matched on
that rule and on its owner too, so a row one rule needs classes no other rule's dependency on its node (the
closing pair's reconcile-key-no-rule). Its class must be one of
tolerance, homonym, not a use and moved. That probe is the order's gate, kept as one committed script,
`build/2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py`, which also checks each routed disposition's transition row (the
night pass's closing review, M7 and H1). Its copies in the audit fold's `[review-instrument]` and the night pass's
instruments record are snapshots. The citations-only probe below is
superseded: re-run on the committed tree, it reds on the routes row it cannot read (FM5).

| Row | Rule | Node | Owner | Class | Why |
|---|---|---|---|---|---|
| dKeptSession | cites | `build.closes` | dShippedRelease | tolerance | the presets check refuses `strict` and `guarded` for it on a core-only install; it validates a value and never runs the key |
| dKeptSession | cites | `intake` | dWellOiledMachine | homonym | the mailbox's `intake` message kind, not the intake record kind |
| dFairHearing | cites | `class` | dTotalRecall | homonym | the `class:` prefix of `review.report`'s disposition grammar, not the `class` tag namespace |
| dFairHearing | cites | `preset` | dKeptSession | homonym | the review harness's own `preset` argument, not the policy key |
| dGroundRules | cites | `policy-file.guard` | dDeclaredLoop | not a use | the minimal guard enforces the key's default, owner-only, without reading the key |
| dGroundRules | cites | `policy-file.proof` | dDeclaredLoop | not a use | the minimal guard enforces the key's default, the TTY proof, without reading the key |
| dOrderedCharter | cites | `check` | dWitnessedBar | homonym | the resolver's `check` verb beside `show`, `where` and `refs`, not the `check` tag namespace |
| dOrderedCharter | cites | `memory.map-purpose` | dTotalRecall | moved | the review that reads the key is dTotalRecall's PM-5 unit; the row names the key only to say so (H1) |
| dRankedPlan | cites | `entry.intake` | dWellOiledMachine | tolerance | RC-9's fallback: dDeclaredLoop's owner gate (AF-1), witness "intake not installed", until dWellOiledMachine lands the hook and drains it |
| dFurnishedOrders | cites | `feature` | dTotalRecall | tolerance | the work order selects by `feature.*` only once dLinkedLibrary arms that selector (WK-4), and its code-notes and `code` slots render "not installed" until dTotalRecall lands, as the `map` slot does (night pass, point 4) |
| dFurnishedOrders | cites | `code` | dTotalRecall | tolerance | the work order's `code` slot renders "not installed" until dTotalRecall's `code` record lands, as the `map` slot does (night pass, point 3) |
| dOrderedCharter | cites | `code` | dTotalRecall | not a use | each role's load set budgets the `code` slot's bytes, and never reads the record (night pass, point 3) |
| dKeptSession | cites | `playbook` | dIndexedDesign | tolerance | the `repeat` disposition files an ask until dIndexedDesign lands the playbook record kind (the night pass's closing review, H2) |
| dTotalRecall | cites | `roster` | dIndexedDesign | homonym | the build README's derived `roster` front-matter field, not the roster record kind `design.decompose` writes (PM-12) |
| dFairHearing | cites | `review.trigger` | dDeclaredLoop | tolerance | cl-dClosedLoop-0070 runs `review.pin` directly with its pin arguments, a stand-in until dDeclaredLoop's `review.trigger` lands (the whole-design audit's C2-F6) |
| dFairHearing | routes | `review.trigger` | dDeclaredLoop | not a use | the harness takes the `preset` argument Design's breakpoint passes (RV-1); the breakpoint calls the harness, never the reverse (AF-1) |
| dDeclaredLoop | cites | `run.on-owner-question` | dBoundRoles | tolerance | the owner gate holds for the owner's disposition until dBoundRoles lands the key, and never reads it for a ratification (AF-1) |
| dKeptSession | cites | `hooks.bypass` | dWitnessedBar | not a use | the preset step's arm reads the key's resolved value in a planted strict file; it never implements the bypass (DA-M10) |
| dDeclaredLoop | cites | `decisions.major` | dLinkedLibrary | tolerance | cl-dClosedLoop-0104 names the key's `author-owner-ratifies` value only for the case its owner gate stands in for `build.ratify`, holding `build.recommend`'s route for the owner's disposition, until dLinkedLibrary lands the key and dScopedBuild `build.ratify` (the owner's FK-9-1) |
| dDeclaredLoop | reads | `decisions.major` | dLinkedLibrary | tolerance | `build.recommend` routes on the key only inside the Build step, whose build descends from dTotalRecall (FM4's reads rule) |
| dFairHearing | reads | `flow.route-backs` | dDeclaredLoop | not a use | dDeclaredLoop's program counts the bound as it routes the harness's report; the harness never reads it (FM4's reads rule) |
| dRankedPlan | reads | `run.host` | dWellOiledMachine | tolerance | `plan.exit` launches the executor only where the supervisor is installed; before dWellOiledMachine lands, the attended session carries the build into Design (FM4's reads rule) |
| dSafePassage | cites | `check` | dWitnessedBar | homonym | govkit's `check` verb beside `update`, which reads the `[[retired]]` rows, not the `check` tag namespace (the away pass; moved with the step kind's clause, AP-25) |
| dTotalRecall | cites | `journal` | dWellOiledMachine | homonym | the Serves kind named `journal`, which the registry renames `log`, not Runtime's journal record kind (the away pass) |
| dFairHearing | cites | `review.dispose` | dDeclaredLoop | tolerance | cl-dClosedLoop-0075 writes the report's dispositions to the review record, disposed by hand as today's reviews are, a stand-in until dDeclaredLoop lands `review.dispose` and routes them (flow-steps [breakpoint]'s stand-ins, C2-F6) |
| dFairHearing | routes | `review.dispose` | dDeclaredLoop | tolerance | `review.report`'s route into `review.dispose` reaches the review record, its dispositions disposed by hand as today's reviews are, until dDeclaredLoop lands `review.dispose` and routes them (cl-dClosedLoop-0075, flow-steps [breakpoint]'s stand-ins, C2-F6) |
| dKeptSession | cites | `memory.map-purpose` | dTotalRecall | tolerance | the policy namespaces' purposes are reviewed under the key's default, `review`, until dTotalRecall lands the key (cl-dClosedLoop-0154, CS4-F1) |
| dTrueNorth | cites | `deviation.approval` | dDeclaredLoop | tolerance | a deviation's approver is read against the by-risk table final-questions `[deviation]` sets, the risk class read from the record, until dOrderedCharter's classifier and dDeclaredLoop's key land and re-point it (cl-dClosedLoop-0004, C1-F9) |
| dPlacedRequest | reads | `build.unit-holders` | dWellOiledMachine | tolerance | a `unit` disposition is refused as under `driver-only`, the build's driver alone driving its units, until dWellOiledMachine lands the unit holders and the key (flow-steps [entry]'s stand-ins, AS4-F4) |
| dPlacedRequest | reads | `kickoff.runs` | dRankedPlan | tolerance | `entry.orient` runs the full kickoff where no READY card exists, the key's default `no-ready-card`, until dRankedPlan lands the key and re-points it (flow-steps [entry]'s stand-ins, B1-F11) |
| dFairHearing | reads | `leases.offline` | dPlacedRequest | tolerance | `review.report` refuses a `new:` slug's claim while the remote is unreachable, as `refuse` would: no slug claimed and no local id minted, the finding kept in the report with its slug marked unclaimed and disposed by hand, until dPlacedRequest lands the key (flow-steps [breakpoint]'s stand-ins, FK-6-1) |
| dDeclaredLoop | cites | `design.inventory` | dIndexedDesign | tolerance | under `adopt-parent-work`, the attended session's agent takes the withdrawn parent's kept units into the plan revision, flow-steps [rules]' stand-in for a role item, until dIndexedDesign lands `design.inventory` (cl-dClosedLoop-0100, FK-4-3, FK-4-9) |
| dWitnessedBar | cites | `build.acceptance` | dScopedBuild | tolerance | the attended session's agent observes each new arm red on its staged break and green once restored, and records both in the unit's acceptance ledger, which `test.seen-red` reads, until dScopedBuild lands `build.acceptance`'s seen-red write (cl-dClosedLoop-0345, flow-steps [test], FK-4-12) |
| dShippedRelease | cites | `build.distill` | dScopedBuild | tolerance | `deploy.distill` is unarmed: it records on the landing record that it measured nothing, is never green and routes on, as `test.seed` records an unarmed seed, until dScopedBuild lands `build.distill` (flow-steps [deploy]'s stand-in, FK-4-8) |
| dDeclaredLoop | routes | `build.distill` | dScopedBuild | tolerance | `build.distill` is unarmed, as FK-4-8's `deploy.distill` row above reads: no tool writes decision-log rows today, so no row is written and `build.recommend` routes on, until dScopedBuild lands `build.distill` (flow-steps [rules]' stand-in, the owner's FK-4-9 and FK-4-8) |
| dDeclaredLoop | cites | `build.ratify` | dScopedBuild | tolerance | cl-dClosedLoop-0104 names `build.ratify` as the item its owner gate stands in for under `decisions.major: author-owner-ratifies`, holding `build.recommend`'s route for the owner's disposition, until dScopedBuild lands it (flow-steps [build]'s stand-in, the owner's FK-9-1) |
| dDeclaredLoop | routes | `build.ratify` | dScopedBuild | tolerance | under `decisions.major: author-owner-ratifies`, `build.recommend`'s route reaches dDeclaredLoop's own owner gate, held for the owner's disposition, as RC-9's fallback holds `plan.exit`, until dScopedBuild lands `build.ratify` (cl-dClosedLoop-0104, flow-steps [build]'s stand-in, the owner's FK-9-1) |
| dDeclaredLoop | routes | `deploy.notify` | dShippedRelease | tolerance | `deploy.notify` is unarmed: the mailbox it posts `landed` to is dKeptSession's, so no post is made and the route goes on, until dShippedRelease lands `deploy.notify` (flow-steps [rules]' stand-in, the owner's FK-4-9 and FK-4-8) |
| dDeclaredLoop | routes | `design.input` | dIndexedDesign | tolerance | `design.input` is unarmed, no tool pinning the input today: it records that it pinned nothing, is never green, and the route goes on to Design's role items, which the attended session's agent does, until dIndexedDesign lands `design.input` (flow-steps [rules]' stand-in, the owner's FK-4-9 and FK-4-8) |
| dDeclaredLoop | routes | `design.ready` | dIndexedDesign | tolerance | a route into `design.ready` reaches today's tool, `tools/memory-tree/gen_build_index.py`, which reads each spec's status and tier, `design.handoff`'s `status-and-tier` arm as today, until dIndexedDesign lands `design.ready` (flow-steps [rules]' stand-in, the owner's FK-4-9) |
| dDeclaredLoop | cites | `plan.exit` | dRankedPlan | tolerance | cl-dClosedLoop-0104 cites `plan.exit` for RC-9's fallback, dDeclaredLoop's owner gate holding it for the owner's disposition (cl-dClosedLoop-0378), the owner-gate stand-in its own gate repeats for `build.ratify` (the owner's FK-9-1) |
| dDeclaredLoop | routes | `plan.exit` | dRankedPlan | tolerance | a route into `plan.exit` from `plan.recommend` or `plan.reason` reaches the fixture witness the transition table's row holds for an exit item whose build has not landed, the stand-in the clause declares, which wins over [rules]', until dRankedPlan lands and arms `plan.exit` (cl-dClosedLoop-0098, C2-F8, the owner's FK-8-1) |
| dDeclaredLoop | routes | `plan.input` | dRankedPlan | not a use | `plan.recommend` and `plan.reason` route a review to the Plan breakpoint, the breakpoint program at Plan's exit, which the probe reads as the Plan step's first item, and neither routes into `plan.input` |
| dDeclaredLoop | routes | `plan.record` | dRankedPlan | tolerance | a route into a role item reaches the attended session's agent, doing the planner's work, until dRankedPlan lands `plan.record` (flow-steps [rules]' stand-in, the owner's FK-4-9) |
| dDeclaredLoop | routes | `test.exit` | dWitnessedBar | tolerance | a route into `test.exit` from `test.recommend` or `test.reason` reaches the fixture witness the transition table's row holds for an exit item whose build has not landed, the stand-in the clause declares, which wins over [rules]', until dWitnessedBar lands and arms `test.exit` (cl-dClosedLoop-0098, C2-F8, the owner's FK-8-1) |
| dIndexedDesign | routes | `build.unit-pass` | dScopedBuild | tolerance | a route into a role item reaches the attended session's agent, doing the builder's work, until dScopedBuild lands `build.unit-pass` (flow-steps [rules]' stand-in, the owner's FK-4-9) |
| dLinkedLibrary | routes | `build.unit-pass` | dScopedBuild | tolerance | a route into a role item reaches the attended session's agent, doing the builder's work, until dScopedBuild lands `build.unit-pass` (flow-steps [rules]' stand-in, the owner's FK-4-9) |
| dPlacedRequest | routes | `build.unit-lease` | dScopedBuild | tolerance | a `unit` disposition is refused as under `driver-only`, the build's driver alone driving its units, until dWellOiledMachine lands the unit holders and dScopedBuild `build.unit-lease`, the stand-in flow-steps [entry] declares, which wins over [rules]' (flow-steps [entry]'s stand-ins, AS4-F4, the owner's FK-8-1) |
| dPlacedRequest | routes | `design.input` | dIndexedDesign | tolerance | a placement routed to Plan or Design files an owner item carrying the claim until dIndexedDesign lands `design.input`, the stand-in the clause declares for its own route, which wins over [rules]' (cl-dClosedLoop-0123, C2-F7, the owner's FK-8-1) |
| dPlacedRequest | routes | `plan.dedupe` | dRankedPlan | tolerance | a placement routed to Plan or Design files an owner item carrying the claim until dRankedPlan lands `plan.dedupe`, the stand-in the clause declares for its own route, which wins over [rules]' (cl-dClosedLoop-0123, C2-F7, the owner's FK-8-1) |
| dPlacedRequest | routes | `plan.input` | dRankedPlan | tolerance | a placement routed to Plan or Design files an owner item carrying the claim until dRankedPlan lands `plan.input`, the stand-in the clause declares for its own route, which wins over [rules]' (cl-dClosedLoop-0123, C2-F7, the owner's FK-8-1) |
| dPlacedRequest | routes | `plan.triage-rule` | dRankedPlan | tolerance | a placement routed to Plan or Design files an owner item carrying the claim until dRankedPlan lands `plan.triage-rule`, the stand-in the clause declares for its own route, which wins over [rules]' (cl-dClosedLoop-0123, C2-F7, the owner's FK-8-1) |
| dRankedPlan | routes | `design.input` | dIndexedDesign | tolerance | `design.input` is unarmed, no tool pinning the input today: it records that it pinned nothing, is never green, and the route goes on to Design's role items, which the attended session's agent does, until dIndexedDesign lands `design.input` (flow-steps [rules]' stand-in, the owner's FK-4-9 and FK-4-8) |
| dShippedRelease | routes | `maintain.patch` | dTendedCadence | not a use | `deploy.core` files a red landing's patch under the key Maintain's reading uses, so `maintain.patch` finds it open and files no second, and never routes to it |
| dWellOiledMachine | routes | `deploy.released` | dShippedRelease | tolerance | a landing ends at the lander, `push-main.sh`, until dShippedRelease lands `deploy.released`, so `life.quiesce` finds no landed build waiting there (flow-steps [rules]' stand-in, the owner's FK-4-9) |
| dWellOiledMachine | routes | `deploy.unlease` | dShippedRelease | tolerance | a landing ends at the lander, `push-main.sh`, until dShippedRelease lands `deploy.unlease`, so `life.quiesce` finds no build past it (flow-steps [rules]' stand-in, the owner's FK-4-9) |
| dWellOiledMachine | cites | `deploy.unlease` | dShippedRelease | tolerance | cl-dClosedLoop-0505 admits `deploy.unlease`'s terminal tombstones and mailbox close once dShippedRelease lands it, a landing ending at the lander, `push-main.sh`, until then, which writes neither, so `life.unlease` alone closes a build (flow-steps [rules]' stand-in, the closing pair's close-path-writes-refused) |
| dWitnessedBar | routes | `build.fix-pass` | dScopedBuild | tolerance | a route into a role item reaches the attended session's agent, doing the builder's work, until dScopedBuild lands `build.fix-pass` (flow-steps [rules]' stand-in, the owner's FK-4-9) |
| dWitnessedBar | routes | `build.resolve` | dScopedBuild | tolerance | a route into a role item reaches the attended session's agent, doing the builder's work, until dScopedBuild lands `build.resolve` (flow-steps [rules]' stand-in, the owner's FK-4-9) |
| dWitnessedBar | routes | `design.input` | dIndexedDesign | tolerance | `design.input` is unarmed, no tool pinning the input today: it records that it pinned nothing, is never green, and the route goes on to Design's role items, which the attended session's agent does, until dIndexedDesign lands `design.input` (flow-steps [rules]' stand-in, the owner's FK-4-9 and FK-4-8) |

Revised 2026-10-20 by the whole-design audit's fold: the five rows from dFairHearing's `review.dispose` to
`kickoff.runs` class the stand-ins its folds named. The owner's FK-6-2 moved `patch.ratify` to dPlacedRequest,
which clears dPlacedRequest's and dShippedRelease's reads of it, and FK-6-1's tolerance row classes
dFairHearing's read of `leases.offline`: `review.report` refuses an unreachable claim until dPlacedRequest lands
the key. The widened probe reads every forward route too, and the fold integration's rows class them (below).

Revised 2026-10-20 by the whole-design audit's fork answers (`build/2026-10-20-build-PLAY-dClosedLoop-1-fold-brief-w8.md`):
the four rows after `kickoff.runs` class the stand-ins the answers name. FK-6-1's row classes dFairHearing's read of
`leases.offline`. FK-4-9 adds no row: flow-steps `[rules]` names today's stand-ins for every route into a later
build, and each forward route this probe reads only under `--all-routes` would make its default run red on a class
row with no dependency, so those routes wait for the probe's change.

Revised 2026-10-20 by the whole-design audit's fold integration (`build/2026-10-20-build-PLAY-dClosedLoop-1-fold-brief-w9.md`):
the probe reads every route target in every run now, so the rows after `build.distill`'s class the forward routes
it reads on the folded records, generated from its lines. Each names the stand-in the route reaches: flow-steps
`[rules]`' for the target's actor, or the one a clause or [entry] declares for its own route, which wins (FK-4-9,
FK-8-1). Two are not a use: `deploy.core` names `maintain.patch` only as the reader of its patch's key, and
dDeclaredLoop's Plan recommendation names the Plan breakpoint, which the probe reads as the Plan step's first
item. dDeclaredLoop's route into `build.ratify`, an owner item, reaches dDeclaredLoop's own owner gate, as RC-9's
fallback holds `plan.exit` (FK-9-1). dTendedCadence's `red-leg` clause names distribution's currency leg in plain
words now, since it reads no currency record.

Revised 2026-10-20 by the closing pair's fold (`build/2026-10-20-build-PLAY-dClosedLoop-1-audit-closing-reviews-compared.md`): each row names its rule, and the
rows two rules needed are worded for each (reconcile-key-no-rule). Each route into a command names its real
stand-in: today's tool by its path, a clause's fixture witness, or `unarmed`, as FK-4-8's row reads
(tolerance-rows-unnamed-tool). dDeclaredLoop's `build.base` row and dWellOiledMachine's `deploy.current` row went
with the prose that made their edges (prose-stage-words-as-routes). dWellOiledMachine's cite of `deploy.unlease`
names `life.unlease` as its stand-in (close-path-writes-refused). `next` is a command, which the probe does not read as a node, so cl-0504 states its
stand-in in the clause and no row classes it (answer-dispatch-non-ancestor).

The critical path, its instrument and its runs:

```python
"""The chain's critical path: the longest chain of builds by planned units, over v2's [chain] after relation, and
what each candidate edge would add to it.

Usage: python critical_path.py [--edge <child>:<parent> ...]   (from the worktree root)

A build's units are its planned-units cell's clauses, counted as the map counts them (split on "; "). A build
starts when every parent has landed, so the path's length is the largest sum of units along a parent chain.
"""
import re
import sys

V = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
text = open(V, encoding="utf-8").read()
chain = text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
units, parents = {}, {}
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| ([^|]+) \| (.+) \| [^|]+ \|$", ln)
    if m:
        units[m.group(1)] = len([u for u in m.group(3).split("; ") if u.strip()])
        parents[m.group(1)] = [p.strip() for p in m.group(2).split(",") if p.strip() in
                               re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)]
assert len(units) == 16, len(units)


def longest(par):
    memo, via = {}, {}

    def f(b, seen=()):
        if b in seen:
            sys.exit(f"cycle through {b}")
        if b not in memo:
            best, arg = 0, None
            for p in par[b]:
                v = f(p, seen + (b,))
                if v > best:
                    best, arg = v, p
            memo[b], via[b] = best + units[b], arg
        return memo[b]

    for b in par:
        f(b)
    end = max(memo, key=memo.get)
    path, b = [], end
    while b:
        path.append(b)
        b = via[b]
    return memo[end], list(reversed(path)), memo


base, path, memo = longest(parents)
print(f"critical path: {base} units, {' > '.join(path)}")
print("each build's earliest finish, in units: " + ", ".join(f"{b} {memo[b]}" for b in sorted(memo, key=memo.get)))
for arg in [a for a in sys.argv[1:] if ":" in a]:
    child, parent = arg.split(":")
    par = {b: list(ps) for b, ps in parents.items()}
    par[child] = par[child] + [parent]
    length, p, _ = longest(par)
    print(f"with {child} after {parent}: {length} units ({length - base:+d}), {' > '.join(p)}")
```

```text
$ python critical_path.py --edge dFairHearing:dOrderedCharter --edge dRankedPlan:dWellOiledMachine --edge dShippedRelease:dBoundRoles --edge dBoundRoles:dRankedPlan   (before the fold)
critical path: 168 units, dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
each build's earliest finish, in units: dFairHearing 15, dOrderedCharter 22, dDeclaredLoop 59, dWitnessedBar 78, dBoundRoles 108, dTotalRecall 110, dIndexedDesign 119, dRankedPlan 122, dShippedRelease 129, dWellOiledMachine 133, dScopedBuild 142, dTendedCadence 143, dMindYourWords 149, dCalibratedLens 156, dConvergedCharter 168
with dFairHearing after dOrderedCharter: 183 units (+15), dOrderedCharter > dFairHearing > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
with dRankedPlan after dWellOiledMachine: 180 units (+12), dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dRankedPlan > dTendedCadence > dCalibratedLens > dConvergedCharter
with dShippedRelease after dBoundRoles: 168 units (+0), dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
with dBoundRoles after dRankedPlan: 210 units (+42), dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dRankedPlan > dBoundRoles > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
$ python critical_path.py   (after the fold)
critical path: 176 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
each build's earliest finish, in units: dGroundRules 6, dFairHearing 21, dOrderedCharter 28, dDeclaredLoop 65, dWitnessedBar 85, dBoundRoles 115, dTotalRecall 117, dIndexedDesign 126, dRankedPlan 128, dShippedRelease 136, dWellOiledMachine 141, dScopedBuild 150, dTendedCadence 151, dMindYourWords 157, dCalibratedLens 164, dConvergedCharter 176
```

- **It is 176 units now, from 168.** dGroundRules adds 6. RC-1's option priced its own work at about 3, and its
  row also carries the review's M4, M7 and H4 fixes. dWitnessedBar and dWellOiledMachine gain a unit each, from M4
  and RC-9.
- **The path:** dGroundRules, dOrderedCharter, dDeclaredLoop, dWitnessedBar, dTotalRecall, dWellOiledMachine,
  dTendedCadence, dCalibratedLens, dConvergedCharter.

Superseded on 2026-10-18 by the reconciliation probe (FM5). The ancestor probe, its green run, and the run with one
class planted away:

```python
"""The order's reconciliation gate: every node a chain row cites must be built by the row's build or one of its
ancestors in [chain]'s after relation, or carry a declared class saying why it may not be.

Usage: python ancestor_probe.py <recut-record> [--plant-drop <build>:<node>]   (from the worktree root)

Owners are read from their declared fields through the map's derivation, over five of the six owned kinds: items,
policy keys, points, record kinds and tag namespaces, each cited in backticks, bare or with a value. Systems are
cited in prose by name, and a prose match is not a citation the probe can trust, so it leaves them out and says
so. The classes live in the re-cut record's [reconciled-order] table: Row, Node, Owner, Class, Why. A citation of a
non-ancestor's node with no class row, or a class row no citation needs, is a finding. Exit 1 on any finding.
--plant-drop removes one class row in memory, to see the probe red.
"""
import importlib.util
import re
import sys

B = "memory/builds/dClosedLoop/build/"
spec = importlib.util.spec_from_file_location("projectmap", B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py")
mp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mp)
A, ns = mp.derive()
owner = {}
for kind in ("item", "policy-key", "point", "record-kind", "tag-namespace"):
    for n in ns[kind]:
        own = [v for k, vs in n["rels"] if k == "owner" for v in vs]
        if own:
            owner[(kind, n["key"])] = own[0]
v2 = open(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md", encoding="utf-8").read()
chain = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
rows, parents = {}, {}
names = re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| ([^|]+) \| (.+) \| [^|]+ \|$", ln)
    if m:
        rows[m.group(1)] = m.group(3)
        parents[m.group(1)] = [p.strip() for p in m.group(2).split(",") if p.strip() in names]


def ancestors(b, acc=None):
    acc = set() if acc is None else acc
    for p in parents[b]:
        if p not in acc:
            acc.add(p)
            ancestors(p, acc)
    return acc


cites = []
for b, text in rows.items():
    allowed = ancestors(b) | {b}
    tokens = set(re.findall(r"`([^`\s][^`]*?)(?::[^`]*)?`", text))
    for (kind, key), own in owner.items():
        spelled = key if kind != "record-kind" else key.replace("-", " ")
        if (key in tokens or spelled in tokens) and own not in allowed:
            cites.append((b, key, own))
recut = open(sys.argv[1], encoding="utf-8").read()
section = recut.split("### [reconciled-order]", 1)[1].split("\n## ", 1)[0] if "### [reconciled-order]" in recut else ""
classes = {}
for ln in section.split("\n"):
    c = [x.strip() for x in ln.strip().strip("|").split("|")]
    if ln.startswith("| d") and len(c) >= 5:
        classes[(c[0], c[1].strip("`"))] = c[3]
if "--plant-drop" in sys.argv:
    row, node = sys.argv[sys.argv.index("--plant-drop") + 1].split(":")
    classes.pop((row, node), None)
total = sum(len(re.findall(r"`[^`]+`", t)) for t in rows.values())
print(f"chain rows {len(rows)} · owned nodes read {len(owner)} (items, keys, points, record kinds, tag namespaces; "
      f"systems are cited in prose and left out) · backticked citations {total} · of a non-ancestor's node {len(cites)}")
findings = 0
for b, key, own in sorted(cites):
    cls = classes.get((b, key))
    print(f"  {b} cites `{key}` ({own}'s, not an ancestor): {cls or 'UNCLASSED'}")
    findings += cls is None
for (b, key), cls in sorted(classes.items()):
    if (b, key, owner.get(("item", key)) or "") and not any(c[0] == b and c[1] == key for c in cites):
        print(f"  class row with no citation: {b} `{key}` ({cls})")
        findings += 1
print(f"findings {findings}")
sys.exit(1 if findings else 0)
```

```text
$ python ancestor_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md
chain rows 16 · owned nodes read 344 (items, keys, points, record kinds, tag namespaces; systems are cited in prose and left out) · backticked citations 262 · of a non-ancestor's node 9
  dDeclaredLoop cites `build.closes` (dShippedRelease's, not an ancestor): tolerance
  dDeclaredLoop cites `intake` (dWellOiledMachine's, not an ancestor): homonym
  dFairHearing cites `class` (dTotalRecall's, not an ancestor): homonym
  dFairHearing cites `preset` (dDeclaredLoop's, not an ancestor): homonym
  dGroundRules cites `policy.guard` (dDeclaredLoop's, not an ancestor): not a use
  dGroundRules cites `policy.proof` (dDeclaredLoop's, not an ancestor): not a use
  dOrderedCharter cites `check` (dWitnessedBar's, not an ancestor): homonym
  dOrderedCharter cites `memory.map-purpose` (dTotalRecall's, not an ancestor): moved
  dRankedPlan cites `entry.intake` (dWellOiledMachine's, not an ancestor): tolerance
findings 0
$ python ancestor_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md --plant-drop dRankedPlan:entry.intake
chain rows 16 · owned nodes read 344 (items, keys, points, record kinds, tag namespaces; systems are cited in prose and left out) · backticked citations 262 · of a non-ancestor's node 9
  dDeclaredLoop cites `build.closes` (dShippedRelease's, not an ancestor): tolerance
  dDeclaredLoop cites `intake` (dWellOiledMachine's, not an ancestor): homonym
  dFairHearing cites `class` (dTotalRecall's, not an ancestor): homonym
  dFairHearing cites `preset` (dDeclaredLoop's, not an ancestor): homonym
  dGroundRules cites `policy.guard` (dDeclaredLoop's, not an ancestor): not a use
  dGroundRules cites `policy.proof` (dDeclaredLoop's, not an ancestor): not a use
  dOrderedCharter cites `check` (dWitnessedBar's, not an ancestor): homonym
  dOrderedCharter cites `memory.map-purpose` (dTotalRecall's, not an ancestor): moved
  dRankedPlan cites `entry.intake` (dWellOiledMachine's, not an ancestor): UNCLASSED
findings 1
```

- **Its first run, before the classes, found the 9 citations above unclassed** and exited 1. The table classes
  each one, and none needed an edge or a move beyond what the fold made.
- **It was the gate the review asks for** (H1's): a row that cites a later build's node without a class reds. The
  reconciliation probe superseded it on 2026-10-18 (FM5).
