# install prefix — one declared home for every kit an adopter lands

```toml
feature = "install-prefix"
title = "dead paths in shipped text — the wrong-prefix half and the deleted-file half, and the two gates that hold them"
status = "shipped"
streams = ["tooling"]
decisions = []

[claims]
gate-legs = [
  "install-prefix (shipped surface)",
  "install-prefix self-test",
  "dead-path carriers (deleted files still named)",
  "dead-path carriers self-test",
]
kits = []
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/check-install-prefix.sh",
  "tools/check-install-prefix.test.sh",
  "tools/install-prefix-waivers.txt",
  "tools/check-dead-paths.sh",
  "tools/check-dead-paths.test.sh",
  "tools/dead-path-waivers.txt",
]
```

## Constraints & why

A repo adopting this chain installs every kit under `tools/<kit>/`. The prefix is exactly ONE
segment, and that ceiling is not a preference: `tools/codebase-map/test_codebase_map.template.py`
resolves the kit at the repo root, at `<ancestor>/codebase-map` and nowhere deeper, and
`adopt-codebase-map.sh` refuses a two-segment prefix before it writes anything. A deeper convention
would half-adopt every other kit and be blocked only by that one.

The engines were never the problem. Every kit resolves its own root — from git, or by walking up for
a root-anchored config bounded by `.git` — and every one of them already worked at any prefix. What
strands an adopter is a path SPELLED in something they receive: a runbook step, a usage header, a
remedy string, a rendered artifact. Those fail quietly, because nothing executes a sentence.

Measured before this gate existed: a `tools/` install scaffolded the adopter's own committed hygiene
rule-set document with seven kit paths that resolve to nothing in their tree, and the hygiene gate
exited 0 over it. The check designed to catch exactly that — dead repo-path citations — was
structurally blind, because it classified a token as a repo path only when its first segment was a
tracked top-level directory, and at a prefixed install a bare kit name is not one.

## The other half of the class — a path dead because it was DELETED

`check-install-prefix.sh` holds a path that resolves nowhere because it is spelled at the wrong
PREFIX. `check-dead-paths.sh` holds the other half: a path that resolves nowhere because the file was
deleted. They are one class — a sentence nothing executes — and they are two gates because the
populations are derived from different sources and neither derivation can see the other's defect.

The two have DIVERGED in one respect since `TOOL-dHonouredPark-3`, deliberately.
`tools/dead-path-waivers.txt` is keyed by the carrier line's TEXT plus an occurrence ordinal;
`tools/install-prefix-waivers.txt` is still `<path>:<line>`. Line keying cost this repo two cycles in
one build — any insertion above a carrier unpinned its row — and the owner ruled ONE file. The
sibling moves when its own keying has actually failed, not by association, so a reader finding the
two grammars different is looking at a decision rather than at drift.

MEASURED, which is why the second gate exists. The v3.0 charter convergence deleted two companion
files and ELEVEN carriers kept naming them: the repo's front door, the charter every session reads,
the install runbook twice, a kit README an adopter receives, the kickoff engine's hand-back offer,
two self-test rule citations, a registry reason string, and `check-template-size.sh`'s own over-budget
REMEDY — a message that fires 1.4 KiB from the ceiling, at the one moment someone needs a followable
instruction. Four of the eleven sat on a line the same diff edited: the filename was updated and the
clause beside it was not.

THE NEEDLES ARE DERIVED FROM GIT, never listed: basenames this repo once tracked and no longer
tracks, plus each one's distinctive tail, minus any that still suffix a tracked path. That derivation
is what holds the false-positive rate at zero. The alternative — flagging any path-shaped token that
does not resolve — was measured at 217 hits, essentially all legitimate fixture literals inside
Python selftests, and would have been waived into uselessness on day one.

WHAT IT DOES NOT CATCH, recorded because a reader who over-trusts it is worse off than one who does
not use it: it matches FILENAMES. Three of the eleven carriers named the deleted thing in prose with
no filename — "per its customize companion", "its own 'Customize before use' block", "the product
template + its two companions" — and those were found by reading, not by the gate. It is a floor.

`memory/` is out of scope by rule, not convenience: specs, reviews and archived snapshots are
append-only records describing what WAS true, and rewriting one to please a gate falsifies the record.

## Shared seams

The prefix is DERIVED, never declared, in three shapes that all answer the same question. In shell,
`KIT_REL=${HERE#"$ROOT_N"/}` with both sides normalised through the same `cd … && pwd` chain, because
under MSYS one directory has two spellings and a raw strip across those flavors silently yields an
absolute path that substitutes nothing. In Python, a walk up for `.git` (`gen_build_index.kit_rel`,
`map_lib.resolve_root`). In a shipped document, a brace-delimited placeholder the adopter's own
adopter substitutes at scaffold time, which is what the two kit/dogfood parity gates now render
rather than approximate with a global strip.

The gate's kit-name alternation is derived from the tracked `tools/*` directories, so a kit is
covered the day it lands rather than the day someone remembers to add it to a list.

## Gaps

- **The waiver registry is shrink-only but not zero.** Eleven rows today, in two classes: dual-
  spelling probes that keep working for the adopters this repo does not retrofit, and the
  codebase-map `REGEN_CMD` legacy preserved for a pre-1.1 gate file that is project-owned and never
  overwritten. Both are deliberate; neither is permanent by right.
- **The gate polices what this repo SHIPS, not what a target INSTALLS.** A target that hand-edits a
  path back is not caught here. That belongs to the deployer's `check`, which reads target state and
  has a receipt to compare against.
- **Existing adopters are not retrofitted**, by decision. Every dual-spelling probe exists to serve
  them, which is why removing one is a behaviour change rather than a cleanup.

## Reuse affordance

seam: check-dead-paths.sh — reuse whenever a repo must forbid naming something it DELETED: derive
the needle set from `git log --diff-filter=D`, subtract every basename the tree still carries, and
anchor the derivation on a frozen sentinel so an empty needle set reds instead of reporting clean.
Extend by widening the haystack; the sentinel is what stops it going quietly vacuous.

seam: check-install-prefix.sh — reuse whenever a repo must forbid a SPELLED path in files it ships
rather than in files it runs: derive the population from `git ls-files`, derive the alternation from
the tree, and put deliberate exceptions in a tracked shrink-only registry that reds when a row
outlives the spelling it excused. Extend by widening the population, never by relaxing the predicate.
