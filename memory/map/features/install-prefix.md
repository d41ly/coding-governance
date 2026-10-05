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
  "foreign-prefix parity (every self-test at three prefixes)",
]
kits = []
git-hooks = []
harness-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = ["inline-marker-breaks-a-line-continuation.md",
  "a-spelling-change-strands-its-readers.md"]
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/check-install-prefix.sh",
  "tools/check-install-prefix.test.sh",
  "tools/run-gates/foreign-prefix.gov.test.sh",
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

## A pure ban, since TOOL-aRepatriatedFork-30

ONE predicate, zero tolerance, a hit named by `<path>:<line>`, and no remedy but deriving the path.
The ban list, the waiver registry, both line markers, `--write-ratchet`, `--rebaseline` and the
predicate epoch are gone: each was an exemption a pass could grant itself, and the drain units
before this one emptied the first three before they were deleted. The old arms 1 and 3 folded into
the counter, which already saw every spelling either of them could.

The population is every tracked file under the gate's tool root, `skills/`, `.githooks/`, every
`*.template.*` and the runbook, LESS a render: a tracked file matching a `rendered` template the
registry ships, whole, with each `{{TOKEN}}` read as one line of any text. That is
`TOOL-aRepatriatedFork-29` §8 F3 (a), and it is structural — the template stays graded, so a literal
reaches a render only through a graded file, and a hand edit that breaks the match puts the render
back. It left out seven files on its first run: the four workflow harnesses gov runs, the fixture
playbook and its two fixture records.

A fixture that must lay itself out at a foreign prefix names each kit through a variable holding
that kit's DERIVED directory name — the one spelling the counter cannot see, and the gate's header
says so. The frozen inCMS receipt spells its adopter-side paths through `{prefix}` too, resolved by
FIELD on read: gov's root for a `source`, the recorded `target_tool_root` for a `path`.

`foreign-prefix parity` is the held leg that proves the drain by EXECUTION, which the ban cannot. It
moves gov's whole tool root with `git mv` in a scratch clone to `scripts/`, `vendor/gov/` and the repo
root, re-spells gov's own declarations by the old root's path head at each move, and runs every
population row there with `FOREIGN_PREFIX_PROBE=1`, under which each suite stops after its first
subject-touching arm (`TOOL-aRepatriatedFork-52`). Its baseline is the bar's own gate-run record,
never a calibrate, and it stops at the first red prefix. Its red control is a suite reading its gate through a literal gov prefix;
a literal prefix used only inside a suite's own scratch fixture is self-consistent and passes at
every host prefix, measured, so that spelling stays the ban's to grade.

**`--offenders` keys every hit** (`TOOL-dDerivedDocket-23`, carried onto the ban at the reconcile of
origin/main into aRepatriatedFork). One `<path><TAB>ban<TAB><spelling>` per counted spelling, a
repeat inside one file carrying `#<k>`, and nothing else on stdout; its exit is `--check`'s. The
keys leave the counter in one write at its end, so a refusal or a dead counter leaves no key, which
the bar's red attribution reads as a probe that could not answer. dDerivedDocket's `root`,
`carried` and `runtime` kinds named the three arms the ban folded into its one counter.

## What the predicate can see (epochs 3 to 6)

The counter reads ONE extension class, `sh py js md json toml txt tsv conf example`. The last four
joined at epoch 3
(`TOOL-cWidenedNet-1`): every kit keeps its declaration sidecars as `.txt` or `.tsv` and ships a
`.conf.example`, so those were the extensions the real literals used and the only ones neither arm
could see — including, until that unit, the two lines in the gate's own body that resolved its
waiver registry and its ban list. A gate blind to its own defect is not a special case here; it is
what an extension class does when it is written from the files somebody happened to think of.

The population is what an adopter RECEIVES. Tests, selftests and `*.conf.example` were excluded
outright until the same unit, on a reason that was half right: those files build root-prefix installs
ON PURPOSE, to exercise the dual-spelling support this repo keeps. What the file-level drop also
excused was their USAGE HEADERS, and six shipped files were telling an adopter to run a path that
resolves to nothing in their tree. They are now graded when a descriptor says they ship, and the
fixture exemption moved to the LINE, where the distinction actually lives.

Epoch 6 (`TOOL-aRepatriatedFork-46`) fixed two places the ban misjudged its own class. A quoted kit
segment after a quoted literal and a comma counts only inside an open path-join call, so a kit id
passed as an argument, a list member or a JSON key is no path. And only the render and prose tokens
drain a kit segment: a kit name typed after `${PFX}` or any other brace counts. The same unit drained
every kit segment under a derived base, so what the ban list holds now is the literal-prefix fixture
class `TOOL-aRepatriatedFork-30` owns.

The two exemptions this section used to describe — a `<path>:<line>` waiver registry frozen at its
rows and a per-line fixture marker — were deleted with the ban list by `TOOL-aRepatriatedFork-30`.

The homonym shapes the test proves clean are a CENSUS, not a wish list: each must still occur in
this tree, or its arm guards a spelling nobody writes. A shape leaves the census, with its fixture
line, when its last tree site goes — the `gd.resolve()` join did with the codebase-map closing
loop's sink path (TOOL-aMendedFleet-38).

## The other half of the class — a path dead because it was DELETED

`check-install-prefix.sh` holds a path that resolves nowhere because it is spelled at the wrong
PREFIX. `check-dead-paths.sh` holds the other half: a path that resolves nowhere because the file was
deleted. They are one class — a sentence nothing executes — and they are two gates because the
populations are derived from different sources and neither derivation can see the other's defect.

The two have DIVERGED in one respect since `TOOL-dHonouredPark-3`, deliberately.
`tools/dead-path-waivers.txt` is keyed by the carrier line's TEXT plus an occurrence ordinal; the
install-prefix gate's registry stayed `<path>:<line>` until `TOOL-aRepatriatedFork-30` deleted it.
Line keying cost this repo two cycles in one build — any insertion above a carrier unpinned its row
— and the owner ruled ONE file rather than moving the sibling by association.

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

- **A path assembled from two variables is invisible**, and the foreign-prefix fixtures use exactly
  that spelling on purpose. A kit name typed into such a variable by hand, rather than derived from
  a resolved directory, is a literal the counter cannot see; the review of a fixture is what holds it.
- **The extension class still ends somewhere.** `.yml`, `.ini` and `.cfg` are outside it because
  this tree contains no such file, and an alternative that matches nothing asserts nothing. The day
  one lands, the class widens, and its new hits are drained before the widening lands — there is no
  re-baseline to absorb them.
- **The render rule proves a file is a render for SOME token values, not which ones.** The owning
  kit's parity leg re-renders with the real values.
- **The gate polices what this repo SHIPS, not what a target INSTALLS.** A target that hand-edits a
  path back is not caught here. That belongs to the deployer's `check`, which reads target state and
  has a receipt to compare against.
- **Existing adopters are not retrofitted**, by decision. Every dual-spelling probe exists to serve
  them, which is why removing one is a behaviour change rather than a cleanup.

## Reuse affordance

seam: check-dead-paths.sh — reuse whenever a repo must forbid naming something it DELETED or
renamed away: derive the needle set from `git log --diff-filter=D` plus the source of every
`--diff-filter=R` row outside `memory/`, subtract every basename the tree still carries, and anchor
each half on its own frozen sentinel so an empty read reds instead of reporting clean. Extend by
widening the haystack; the sentinels are what stop it going quietly vacuous.

seam: check-install-prefix.sh — reuse whenever a repo must forbid a SPELLED path in files it ships
rather than in files it runs: derive the population from `git ls-files`, derive the alternation from
the tree, leave out only a file that matches its declared template whole, and grant no exception at
all. Extend by widening the population, never by relaxing the predicate.
