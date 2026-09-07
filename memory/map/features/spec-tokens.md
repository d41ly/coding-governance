# spec tokens — a spec's machine-facing names resolve against the tree that owns them

```toml
feature = "spec-tokens"
title = "Three joins that resolve a live spec's leg names, witness paths and line citations"
status = "shipped"
streams = ["tooling"]
decisions = []

[claims]
gate-legs = ["spec tokens (a spec's own names resolve)", "spec-tokens self-test"]
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
  "tools/check-spec-tokens.py",
  "tools/check-spec-tokens.test.sh",
  "memory/project/spec-token-waivers.txt",
]
```

## Constraints & why

Three spec-audit rounds over one build found the same class by hand every time: a section 7 gate
name that is not a leg, a section 6 criterion whose witness path is not tracked, and a `path:line`
citation past the end of its file. Each is a JOIN over two tracked files, so hand-verifying them was
paying a reviewer to do what a checker does. The checker's own header carries the measurements that
sized each arm, pinned to the sha they were taken at; they are not restated here.

**It resolves EXISTENCE and RANGE, and nothing else.** It does not read the cited line, so a
citation naming a real line that argues the opposite passes. It grades no prose, scope, acceptance
or tier. That limit is in the checker's own header because a structural check reads as a semantic
one to everybody who did not write it.

**The three joins have three populations, and conflating them was the defect rev-2 folded.** Legs
are graded only on a section 7 line that IS the list, because treating every backticked token there
as a leg name drowns in prose. Paths are graded only where path-shaped, a slash AND an extension or
an exact tracked path, because a bare word is prose. Citations are SCOPED to a tracked path, because
the house style cites a kit file by basename and most citations therefore name nothing `git ls-files`
holds. Redding those is a disposition per row and the lint never lands; passing them silently is a
could-not-fail arm over much of the corpus. So they are skipped AND COUNTED, and the count prints on
every run.

**Terminal specs are outside the population by construction.** This repo cites a landed decision
verbatim and never rewrites one, so grading a CLOSED spec would demand editing a frozen record to
clear a hit. The population is the specs a build can still change.

**It refuses rather than passing.** An empty spec population refuses, because a lint that graded
nothing reports the same zero as a clean tree. An unreadable manifest refuses. A waiver row naming
a path no spec cites, or one the tree now tracks, refuses — a stale exception cannot hide a live hit.

## Shared seams

- `tools/gate-legs.json` — the manifest is READ for leg names, never mirrored. It is the single
  source for what the bar runs, and this join adds no second list.
- `memory/project/*.txt` — the shrink-only registry convention, shared with
  `testsuite-count-waivers.txt` and `install-prefix-waivers.txt`. Same directory, same
  stale-row-reds rule, and hygiene check 3's allowed set names it so a stray file there still reds.
- `git ls-files` — the tracked-path oracle, the same population every other gate here grades
  against. A gate that read the filesystem instead would pass on an unstaged file.

## Reuse affordance

seam: the SKIP-AND-COUNT arm — reuse for any lint whose honest population is a subset of what it
can see; extend via the printed counter, which is what stops a scoped green row reading as full
coverage. The pattern is that the skipped count rides every run, not a comment.

seam: the shape-based exclusion set (`NOT_A_TOKEN`, `NOT_A_LEG`, `LEG_LINE`) — reuse for any join
over house-style markdown that must separate a machine-facing token from prose; extend by adding a
shape, never a waiver row, because a shape generalises to specs nobody has written yet.

## Affordances

- `python tools/check-spec-tokens.py` — the leg. Silent plus exit 0 is compliance.
- `python tools/check-spec-tokens.py --list` — every hit AND near-miss, exit 0. The authoring aid,
  and the pre-wiring instrument section 7 of the charter requires before a predicate is wired.
- `memory/project/spec-token-waivers.txt` — the shrink-only exception registry.

## The section-7 contract (TOOL-aJoinedCanon-7)

The Gates section is located by HEADING TEXT — `^## [0-9]+[.] Gates[ 	]*$` — and never by ordinal.
A Tier-1 spec that drops the production-readiness checklist slides every later section up one, so
the ordinal read graded whatever sat seventh; once `SPEC_LEGLINE_CUTOFF` turns the silent read into
a verdict, that would red a spec the format permits.

A token that IS a manifest name resolves BEFORE the `NOT_A_LEG` shape exclusions. Those exclusions
drop commands, conf keys and graded files out of the join, but a real leg name carrying a `/`, or
opening with a command verb, was discarded UNREAD — so a correct §7 contributed nothing and looked
like prose. Measured on a fixture: the old reader graded 1 token where the new one grades 2.

The run report carries the UNGRADED population in two separate fields: how many live specs carry a
Gates heading contributing no leg name, and how many carry no Gates heading at all. They are kept
apart because the remedies differ — the first is an author writing prose where the list goes, the
second is the light profile being exercised, which is legal. Measured at this landing: **32 of 44**
live specs were in the first field and 0 in the second, and before this the report said neither.

`SPEC_LEGLINE_CUTOFF` (`.memory-tree.conf`, blank = off) makes the first field a verdict for any
live spec dated at or after it that CARRIES a Gates heading. The heading precondition is the whole
Tier-1 accommodation.

## Gaps

- **The citation arm skips most of its corpus.** The majority of citations name an untracked path
  and are skipped; the run prints how many. Draining that means changing the house style for
  kit-file citations, which nothing schedules.
- **A leg name inside section 7 PROSE is not graded.** The list-line predicate is what makes the arm
  affordable, and it is also the hole: a spec that names a dead leg in a sentence passes.
- **Existence is not agreement.** The three joins prove a name resolves; no arm reads what it
  resolves TO, so a spec citing the wrong real line is invisible here.
- **A MISSPELLED shape-excluded name is still skipped.** The manifest-first resolution rescues a leg
  name that IS in the manifest; one that carries a `/` and is spelled wrong still falls through the
  shape exclusion unread, so it neither resolves nor reds.
- **The §6 witness walk still keys on its ORDINAL.** Only the Gates section moved to heading text.
- **A spec that omits its Gates section is silent by design**, and the S7 arm cannot reach it. That
  is the Tier-1 accommodation and the price of it.
