# Build journal — TOOL-aFoldedQuarry

Node `a` · branch `branch/port-ledger-ttrove-governance-8b6ea4` · base `42c3f4dc`.
One section per unit, appended as it lands.

## Environment note found on arrival

`.claude/skills/memory-recall/SKILL.md` was CRLF in this worktree while `main`'s checkout of the same
commit is LF, so `adopt-memory-recall.sh --check` reported every line as drift before a single edit
was made. `.gitattributes` pins that path `eol=lf`, and the index normalises on commit, so
`git status` was clean and nothing pointed at the file. `rm` plus `git checkout --` restored LF.
Worth knowing because the symptom — a whole-file diff on a file the session never touched — reads
like a broken gate rather than a checkout artifact.

## U6 — index-keyed verdict join (spec `TOOL-aFoldedQuarry-2`, CLOSED)

### What landed

`tools/workflows/tier2-review.js` keeps its name, its four lenses, its cap-6 fan-out, its `args`
validation and all of its trust reporting. Only the join changed.

| Before | After |
|---|---|
| `verdictByRef[v.ref] = v` on a plain object | `verdictById` `Map` keyed on an integer |
| the skeptic re-typed `file:line` | the skeptic echoes `id=<n>` the orchestrator printed |
| two findings at one location shared one verdict | each finding carries its own id |
| a repeat verdict overwrote silently | agreeing repeat counted; disagreeing repeat demotes to UNVERIFIED |
| a verdict for an unknown key was stored | an unassigned id is counted `spurious` and discarded |
| nothing judged returned with NO report | the outstanding list is synthesized into the report |

Two gates ship with it. `tools/workflows/check-review-join.sh` bans three spellings of the retired
join across every tracked `tools/**/*.js`. `tools/workflows/check-workflow-syntax.js` parses each
workflow script as the async-function body its runtime evaluates.

### Three things measurement changed

**`node --check` is not a syntax gate.** It was in the acceptance criteria as AC7 until it was run:
on node v24 it exits 0 for `export const x=1` followed by `let y=(`. Module auto-detection retries
the parse and swallows the failure. The replacement constructs an `AsyncFunction` from the source
with the `export` keyword stripped, which is the only shape that accepts module export, top-level
`await` and top-level `return` at once — and it goes red on the same fixture with
`SyntaxError: Unexpected token '}'`.

**Comment stripping is load-bearing, not politeness.** The harness now carries a comment that spells
the retired join verbatim in order to explain why it is gone. A whole-file-text absence assertion
would red on the documentation of its own fix. The stripper is a character scan rather than a regex
on `//`, because a regex cannot tell the `//` that opens a comment from the one inside
`"https://…"`, and cutting on the wrong one turns a code line into prose and the ban into a no-op.
Both cases are armed in the self-test.

**A repeat verdict that AGREES is not a conflict.** The first draft demoted any id receiving a second
verdict to unverified. A chatty skeptic listing one finding twice with the same verdict would have
lost a real adjudication and inflated the unverified count, which then reads as harness degradation.
Only a DISAGREEING repeat is a conflict.

### The empty-population arm

Both gates fail rather than pass when they find nothing to look at. A discovery run over zero
workflow scripts, or an explicit run over files that do not exist, prints "which is not a pass" and
exits 1. A gate whose population evaporates otherwise prints a green line forever.

### Verification

`bash tools/workflows/check-review-join.test.sh` — 16 arms, every one asserting the SPECIFIC message
its branch emits, `PASS` printed after the last arm. Five red arms (three ban spellings, the
url-in-a-string case, the remedy text), three green arms (comment-only prose, the shipped tree, the
dialect fixture), one empty-population arm, three syntax-gate arms, and five positive assertions that
the shipped harness actually carries the indexed join — an absence ban alone proves only that the old
join is gone.

`bash tools/run-gates.sh` — 21/21 legs green, 1 skipped as unchanged. Three legs are new:
the ban, the syntax gate, and the self-test. `tools/run-gates.test.sh` needed `node` added to its
allowed launcher set, which is a deliberate widening recorded here rather than a quiet edit.

## U1 — the flatten (spec `TOOL-aFoldedQuarry-3`, CLOSED)

### What landed

The discipline directory axis is gone from the kit and from this repo's tree. `memory/` now holds one
append-only `DECISIONS.md`, per-family backlog shards under `backlog/`, and every build at
`builds/<slug>/` — no date prefix, no family prefix. Which discipline a spec served is a `streams`
value in its status header, validated against the closed `DISCIPLINES` enum whenever present and
required once the filename date reaches `STREAMS_CUTOFF`.

Tracked files under `memory/`: 86 before, 76 after. The delta is exactly the four discipline
`README.md`, the four discipline `TREE.md`, three of the four `DECISIONS.md` (merged into one), one
of the two `aPrunedCeremony` build READMEs (merged), and the two new records this unit wrote. No file
was dropped.

### One slug, two families

`playbook/builds/2026-07-19-PLAY-aPrunedCeremony` and `tooling/builds/2026-07-19-TOOL-aPrunedCeremony`
were ONE session under two disciplines. Flattening made that visible as a collision: two `README.md`
and two pairs of `spec-…-1.md` / `spec-…-2.md` wanting the same names. They merged into
`builds/aPrunedCeremony/`, which is the case the flatten exists for, and the recording grammar gained
an OPTIONAL FAMILY qualifier — `<date>-<kind>-<FAMILY>-<slug>-<seq>.md` — over the CLOSED alternation
from `FAMILIES`. A generic `[A-Z]+` there would have admitted a family that does not exist and made
the rejection arm vacuous.

### The finding that shaped the unit

Six path selectors changed segment count at once. A selector left at the old count matches nothing,
`grep … || true` yields empty, `[ -n "$bad" ]` is false, and the check prints nothing — which is
exactly what a passing check prints. The gate would have gone green over an unlinted tree with no
symptom at all.

So every retargeted selector now asserts a NON-EMPTY population. The first draft of that guard was
wrong in the opposite direction: it redded a freshly scaffolded tree, because a repo with no builds
yet legitimately has an empty build population. Measured by running `adopt-memory-tree.sh --scaffold`
into a scratch repo, not by reading the code. The guard therefore compares TWO granularities — a
PRECONDITION that asks whether a file of that KIND exists anywhere under the memory root, and the
POPULATION at the exact path the check expects. Equal-and-zero is a young tree. Precondition non-zero
with an empty population is a mis-segmented selector, and only that reds. Both states are armed in
the self-test, the half-migrated one built from the actual pre-flatten paths.

### The kit/dogfood divergence nobody was watching

`SPEC-TEMPLATE.template.md` — the file an adopter copies — still described a NINE-section canon and
carried no `SPEC10_CUTOFF` section, while this repo's installed `memory/TEMPLATE-SPEC.md` and the
gate had required TEN sections since 2026-08-04. An adopter would have installed a template the gate
rejects. Nothing connected the two files, so nothing caught it.

`tools/memory-tree/kit-dogfood-parity.test.sh` now does, as a gate leg: the shipped copies must equal
the installed ones modulo one declared substitution — the `tools/` install prefix, since the kit
ships tool-root-relative and an adopter chooses where the kits live. `--render` rewrites the shipped
copies from the live ones. Its first run reported the whole tree as drift because it derived the
prefix by string-stripping `git rev-parse --show-toplevel` (`C:/projects/…`) from `pwd`
(`/c/projects/…`) — the two-spellings trap already recorded in the kickoff manifest, arriving in new
code the same day it was read. Both sides now go through the same `cd … && pwd` chain.

### Verification

`bash tools/memory-tree/check-memory-hygiene.test.sh` — 64 assertions, up from 37. New arms: four
streams arms (post-cutoff with and without the field, an illegal value, and a TIER-1 post-cutoff
spec, which proves the check sits above the Tier-1 exit), the FAMILY-qualifier pair, the flat
folder-name rejection, the backlog shard-name rejection, and the two empty-population arms.

`bash tools/run-gates.sh` — 22/22 legs green, 1 skipped. The bar grew the kit/dogfood parity leg.
