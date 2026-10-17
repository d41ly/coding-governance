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
