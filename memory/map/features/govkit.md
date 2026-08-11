# govkit — the deployer, and the registry that is its population

```toml
feature = "govkit"
title = "govkit — a declared kit population, and the selfcheck that keeps it honest"
status = "building"
streams = ["deployer", "tooling"]
decisions = []

[claims]
gate-legs = ["govkit selfcheck"]
kits = ["govkit"]
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = ["DEPL.md"]
[paths]
globs = [
  "tools/govkit/*",
  "tools/govkit/entries/*",
  "tools/*/kit.toml",
]
```

## Constraints & why

**The registry is a DECLARATION, and that is the whole design.** No directory listing equals the
deployable set, and the ways it fails are not symmetric. Some `tools/*` directories are not
deployable — `tools/lib/` ships nothing, and the gate-runner cluster is a stated non-goal because
gov's runner sources `tools/lib/` and exits 2 with zero legs run without it. Some entries are not
`tools/*` directories at all: the playbook is root files, the kickoff ratchet lives under `skills/`
and lands renamed and flat, and several single-file gates sit directly under `tools/`. One directory
carries TWO entries, because `tools/workflows/` versions its files under two kit ids. And one entry
writes ONE source to TWO destinations, because the agent-cap parity arm fails outright when the wired
copy is absent. `map_extractors._tool_kits()`'s own docstring records the same lesson from the other
side: README-gating "would have silently dropped three of ten".

**No population count appears in the spec or the registry, on purpose.** The spec stated two counts
across its life and both were true when measured and false when read — the `tools/` directory count
moved when the unattended kit landed, and the playbook file count was always one high because the
customize companion is explicitly not shipped. `selfcheck` derives every figure at the moment it
checks. A number in that prose is now a defect in the document.

**The surface predicate is the ratchet.** Every tracked path in the declared surface — depth-1 under
`tools/`, everything under the hook and kickoff trees, and the shipped root playbook files — is an
entry, a member of exactly one entry's file rules, or an exemption carrying a non-empty reason. It is
asserted in BOTH directions, and an exemption naming a path that no longer exists reds: a stale
exemption silently widens the surface it was written to narrow. This replaces a predicate that
quantified over `tools/*` DIRECTORIES and therefore left every single-file deployable the runbook
already prescribes in no population at all.

**A new predicate is run over the real tree before it is trusted, and this one earned that rule.**
Its first run found seven problems, three of them real defects in the descriptors it was reading:
sources for an entry whose bytes straddle the install prefix and a verbatim repo-root path were being
resolved against the wrong tree, a destination TEMPLATE carrying `{relpath}` was being compared as if
it were a literal destination, and one tracked hook was claimed by nothing. All three are fixed and
the fix for the first is the `root_relative` rule flag.

**`repo_root()` walks up for the registry rather than asking git.** Two measured reasons. A
`git -C <dir> rev-parse --show-toplevel` returns `<dir>` itself when an absolute `GIT_DIR` is
inherited — which is exactly what git exports to a merge driver in a linked worktree, and how the
row-keyed merge driver was found to be inert in this repo. And a fixed `parents[]` index is correct
at only one install prefix. The walk inherits nothing and is correct at any prefix.

## Shared seams

- `tools/govkit/registry.toml` — the population: entries with their descriptor paths, the surface
  globs, and the exemptions with their reasons.
- `tools/govkit/govkit.py` — `selfcheck` today. `plan`, `check`, `apply`, `apply --resume` and
  `intake` are later rollout commits and are ABSENT rather than stubbed, because a subcommand that
  parses and does nothing is indistinguishable from one that works.
- `tools/<kit>/kit.toml` — a descriptor beside each kit that is a directory.
- `tools/govkit/entries/<id>.kit.toml` — a descriptor for each entry with no kit directory of its
  own.

## Reuse affordance

seam: `registry.toml` — reuse for any question of the form "what is the deployable population and who
owns this path"; extend via a new `[[entry]]` with its descriptor, or an `[[exempt]]` row carrying a
non-empty reason. Never by editing a listing.

seam: `govkit.py selfcheck` — reuse for asserting a declared population against a tracked surface in
both directions; extend via a new arm inside `selfcheck`, which is the single home for every
registry-shaped assertion this unit adds.

## Gaps

The deployer does not deploy yet: rollout commit 1 ships the registry and the ratchet only. `[[hole]]`
discharge probes are declared and are not yet RUN by anything — `check` is commit 2. The version
cross-check against `check-kit-versions.sh`, the guard-class partition assert, and the derived
`mutates_index` are specified in the unit's AC10 and are not yet implemented here.
