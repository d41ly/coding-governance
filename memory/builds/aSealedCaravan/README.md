---
slug: aSealedCaravan
node: a
opened: 2026-08-10
streams: deployer+tooling
roster: DEPL+TOOL
ids: DEPL-aSealedCaravan-2 DEPL-aSealedCaravan-3 PLAY-aSealedCaravan-1 TOOL-aSealedCaravan-1 TOOL-aSealedCaravan-2 TOOL-aSealedCaravan-3 TOOL-aSealedCaravan-4
---

# aSealedCaravan — one install prefix, and a deployer that lands the chain mechanically

Node `a` · opened 2026-08-10 · streams deployer and tooling.

Adoption today is one prose file, `WIRE-INTO-PROJECT.md`, that an agent reads and follows. It
prescribes five different homes for the kits it installs, omits three shipped kits entirely, and
carries fourteen claims that are provably false against source. Nothing in a target repo records what
was installed, from which commit, at which prefix. This build closes both halves: a declared install
prefix that gates enforce, and `govkit` — a mechanical deployer the owner or an agent runs instead of
reading the runbook.

## Start here

**State.** Unit 1 is CLOSED — built, reviewed, and landed on `main` at `82e6dcf`. Unit 2 is
INPROGRESS at rev-6 and is the whole remaining build. It has now been reviewed twice: once at rev-1
alongside unit 1, and again as an M4 spec audit at rev-5 that returned **BLOCKED** with seven
blockers, all folded at rev-6.

**Classification (M2), written before acting on it.** Unit 2 was FORKED — §8 carried three
unresolved items — became READY at rev-5, and the M4 audit then sent it back. It is READY again at
rev-6. §2, §6, §7 and §10 are all filled and name observable checks.

**Next action.** A tight re-audit of the rev-6 fold, then rollout commit 1 — `registry.toml`, a
`kit.toml` per registry entry, and `selfcheck`. The audit's verdict was BLOCKED rather than clean, so
M4's stop rule has not fired; the re-audit is scoped to the fold, not to the design that held.

**What rev-6 changed, because four blockers land inside rollout commit 1.** The registry could not be
written as specified: `[[files]]` carried no destination, so four entries had nowhere to land; two
selectable kits have no version constant, which the completeness criterion assumed; that criterion
quantified over `tools/*` directories and missed every single-file deployable the runbook already
prescribes; and the unattended kit — a full kit on `main` with an adopter, a rendered Skill and five
gate legs — appeared in no entry, no inventory row, no selection set and no exemption. Three more
blockers made criteria unsatisfiable rather than merely incomplete. Every population count is gone
from the spec: `selfcheck` derives them now, because both counts it previously stated were true when
measured and false when read.

**Nothing blocks either unit.** The one blocking pair — unit 1's F3 and unit 2's F5, both about
`tools/lib/` — resolved on 2026-08-10: it is not a kit, it ships nothing, and it becomes a permanent
registry exemption. A repo-wide consumer audit ran first, because "not a kit" is true and "leftover"
is not: it is the canon 11 inline resolver copies are gated against, five gates and the gate runner
source it at runtime, and `pyrun.sh` is named in the `merge.rows.driver` config where its absence
produces a silent ours-only merge with no conflict markers. Unit 1 S9 gives the memory-tree kit its
own launcher instead.

**Read the grounding before either.** Both specs rest on a five-probe inventory that ran all eight
adoption entrypoints end to end in throwaway repos and proved four silent-green failures cold,
including one live here: `.claude/skills/drift-audit/SKILL.md` names two files that do not exist, and
the kit's own `--check` reports in sync. That is section 4 of unit 1, not background colour.

**The review's most useful correction was arithmetic.** Unit 1's enforcement predicate was sized by
reasoning at rev-1 and by running it at rev-2: 95 hits across 37 files naive, 50 across 22 narrowed.
That turned two invented scope items into two measured ones (S12, S13) and a guessed waiver list into
a four-entry registry. Every number in both specs is now measured or marked.

**Forks.** All nine are resolved. Six on 2026-08-10 by the owner — the ratchet lands flat at
`tools/manifest-check.sh`, the prefix gate polices the shipping surface only, the memory-tree kit
ships its own `merge-rows.sh`, `tools/govkit/` is ratified over the research's `deploy/`, and
`tools/lib/` is a permanent registry exemption. The last three on 2026-08-11 by the agent under this
folder's standing mandate: the target descriptor lives in the target, `check-arms.py` stays
shell-only with the guarantee moved to the test layer, and a pre-existing red gate in a target is
measured as a baseline rather than treated as a refusal. Both specs carry the ratified pointer.
Deferring the last three until the `plan`/`check` slice existed was rev-4's plan; it was abandoned
because a fork resolved mid-build is a rewrite, and all three proved answerable from what the spec
already stated.

Records live under `spec/` and, once built, `build/` and `reviews/`. The table below is GENERATED
from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** INPROGRESS · 2 unit(s) · node a · opened 2026-08-10 · streams deployer+tooling · ids DEPL-aSealedCaravan-2 DEPL-aSealedCaravan-3 PLAY-aSealedCaravan-1 TOOL-aSealedCaravan-1 TOOL-aSealedCaravan-2 TOOL-aSealedCaravan-3 TOOL-aSealedCaravan-4

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [DEPL-aSealedCaravan-2 — govkit, the mechanical deployer](spec/2026-08-10-spec-DEPL-aSealedCaravan-2.md) | INPROGRESS | rev-6 | 2026-08-11 |
| [TOOL-aSealedCaravan-1 — one declared install prefix, and the gates that make it true](spec/2026-08-10-spec-TOOL-aSealedCaravan-1.md) | CLOSED | rev-4 | 2026-08-10 |
<!-- /gen:build-index -->
