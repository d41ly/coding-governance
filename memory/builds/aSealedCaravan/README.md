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

**State.** Two units, both SPECCED at rev-2, both reviewed once (Tier-2, 5 lenses, 48 confirmed
findings, 6 blockers — all folded). Nothing is built.

**Next action.** Unit 1 (`TOOL-aSealedCaravan-1`) is buildable and depends on nothing outside this
repo. Its three-commit rollout is in section 4. Unit 2 (`DEPL-aSealedCaravan-2`) should not start
until unit 1 lands, because govkit's install plan is written against one prefix and unit 1 is what
makes that prefix true.

**Two forks BLOCK work, and they are the same fork.** Unit 1's F3 asks whether `tools/lib/` becomes a
shipped kit. Unit 2's F5 cannot be answered without it, and unit 2's rollout commit 1 — the registry
plus `selfcheck`, its whole first deliverable — cannot be written until it is. Resolve F3 first.

**Read the grounding before either.** Both specs rest on a five-probe inventory that ran all eight
adoption entrypoints end to end in throwaway repos and proved four silent-green failures cold,
including one live here: `.claude/skills/drift-audit/SKILL.md` names two files that do not exist, and
the kit's own `--check` reports in sync. That is section 4 of unit 1, not background colour.

**The review's most useful correction was arithmetic.** Unit 1's enforcement predicate was sized by
reasoning at rev-1 and by running it at rev-2: 95 hits across 37 files naive, 50 across 22 narrowed.
That turned two invented scope items into two measured ones (S12, S13) and a guessed waiver list into
a four-entry registry. Every number in both specs is now measured or marked.

**Five forks are open** across the two specs.

Records live under `spec/` and, once built, `build/` and `reviews/`. The table below is GENERATED
from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** SPECCED · 2 unit(s) · node a · opened 2026-08-10 · streams deployer+tooling · ids TOOL-aSealedCaravan-1 DEPL-aSealedCaravan-2

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [DEPL-aSealedCaravan-2 — govkit, the mechanical deployer](spec/2026-08-10-spec-DEPL-aSealedCaravan-2.md) | SPECCED | rev-2 | 2026-08-10 |
| [TOOL-aSealedCaravan-1 — one declared install prefix, and the gates that make it true](spec/2026-08-10-spec-TOOL-aSealedCaravan-1.md) | SPECCED | rev-2 | 2026-08-10 |
<!-- /gen:build-index -->
