---
slug: aSealedCaravan
node: a
opened: 2026-08-10
streams: deployer+tooling
roster: DEPL+TOOL
ids: TOOL-aSealedCaravan-1 DEPL-aSealedCaravan-2
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

**State.** Unit 1 is BUILT — three commits, full bar green at 41/41 — and green on
`branch/governance-adoption-kit-9bc273`, not yet landed on `main`. Unit 2 is SPECCED at rev-4. Both
were reviewed once (Tier-2, 5 lenses, 48 confirmed findings, 6 blockers — all folded).

**Next action.** Merge unit 1 to `main`, then flip its spec to CLOSED — the status is INPROGRESS
rather than CLOSED because "built" and "landed" are different claims. Unit 2
(`DEPL-aSealedCaravan-2`) is unblocked the moment that lands: its install plan is written against
the prefix unit 1 just made true. Its rollout commit 1 is the registry plus `selfcheck`.

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

**Forks.** Six were open; four are resolved (2026-08-10) — the ratchet lands flat at
`tools/manifest-check.sh`, the prefix gate polices the shipping surface only, the memory-tree kit
ships its own `merge-rows.sh`, and `tools/govkit/` is ratified over the research's `deploy/`. Unit 1
is fully resolved and carries the ratified pointer. Unit 2's F2, F3 and F4 stay open deliberately:
none blocks a build, and each wants the read-only `plan`/`check` slice to exist first.

Records live under `spec/` and, once built, `build/` and `reviews/`. The table below is GENERATED
from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** INPROGRESS · 2 unit(s) · node a · opened 2026-08-10 · streams deployer+tooling · ids TOOL-aSealedCaravan-1 DEPL-aSealedCaravan-2

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [DEPL-aSealedCaravan-2 — govkit, the mechanical deployer](spec/2026-08-10-spec-DEPL-aSealedCaravan-2.md) | SPECCED | rev-4 | 2026-08-10 |
| [TOOL-aSealedCaravan-1 — one declared install prefix, and the gates that make it true](spec/2026-08-10-spec-TOOL-aSealedCaravan-1.md) | INPROGRESS | rev-4 | 2026-08-10 |
<!-- /gen:build-index -->
