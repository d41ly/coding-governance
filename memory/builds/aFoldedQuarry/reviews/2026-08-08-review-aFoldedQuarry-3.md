# Review 3 — adversarial pass over the U2 build-index sub-spec

**Scope:** `spec/units/2026-08-08-spec-aFoldedQuarry-4-u2-build-index.md` at rev-1, before any code.
**Method:** walk the generator's inputs against the CORPUS THAT EXISTS, not the corpus the design
assumes. Three of the six findings come from a build folder in this repo that the design would have
crashed on or silently dropped.

| # | Severity | Where | Finding |
|---|---|---|---|
| G1 | blocker | §2 S1, §4 | four real builds have specs with NO parseable status header |
| G2 | high | §2 S8 | the byte-compare gate needs an LF pin or a Windows checkout reds every line |
| G3 | high | §2 S5, §6 AC3 | `--write` deleting "orphaned generated files" is an unbounded delete |
| G4 | medium | §4 | `---` opens front matter AND is a horizontal rule already used in this corpus |
| G5 | medium | §6 AC3 | `LIVE.md` cannot hold an orphan, so the criterion tests two different things |
| G6 | low | §2 S8 | `memory/README.md` links the file this unit deletes |

## G1 — the derived status has no input for four of the fourteen builds (blocker)

S3 makes a build's status a pure function of its unit statuses. Measured against the tree as it
stands, four builds carry no `**Status:**` header on any spec. The first draft of this finding said
three: `aKitHardener` was missed by reading and found by counting, which is the second time in this
build a claim about the corpus survived reading and died on measurement.

| Build | Spec | Why it has no header |
|---|---|---|
| `aDeployScout` | `governance-deployer-research.md` | grandfathered, listed in `legacy-files.txt` |
| `aKitHardener` | `2026-07-14-spec-aKitHardener-1.md` | dated before `SPEC_FORMAT_CUTOFF` |
| `aLeanRework` | `template-v2-rework-spec.md` | grandfathered, listed in `legacy-files.txt` |
| `aRatchetForge` | `manifest-ratchet-spec.md` | grandfathered, listed in `legacy-files.txt` |

Under rev-1 the derived status for each is the empty function. Every plausible default is wrong:
treating them as CLOSED asserts something the memory index contradicts (`aDeployScout` is awaiting
owner approval), and treating them as live parks finished builds in `LIVE.md` forever. Dropping
them from the index is the silent-departure blind spot S5 exists to close, arriving through a
different door.

The fix keeps ONE source of truth per build and makes the fallback explicit rather than default:

- If ANY spec under the build carries a parseable status header, the build status is DERIVED, and an
  authored `status:` in the front matter is an ERROR — two sources of truth for one fact is the
  drift this unit is removing.
- If NO spec carries one, `status:` in the front matter is REQUIRED, and its absence is a named
  error. Four builds author one line each, once, and say why.

That is stricter than upstream and it is the only arrangement where the answer is never invented.

## G2 — a byte-compare gate over generated files needs an LF pin (high)

`--check` compares tracked bytes against a fresh render. The renderer emits LF. On a Windows checkout
without an `eol=lf` attribute, the tracked working copy is CRLF and EVERY line differs — the gate
reds on a file nobody touched, and passes only when the working copy happens to have just been
rendered. That is green-by-accident, and this repo has already paid for it twice: once on the
rendered recall Skill (whose `.gitattributes` pin exists for exactly this reason) and once THIS
SESSION, when a worktree checkout landed CRLF on that same file despite the pin.

`.gitattributes` currently pins `memory/**/TREE.md`. That rule must not simply be deleted with the
file it names — it must be REPLACED by pins on `memory/LIVE.md` and `memory/ledger/*.md`, and the
kit's adopter documentation must say so, because an adopter who copies the generator without the
attribute inherits the same red.

## G3 — "removes the orphan" is an unbounded delete inside the memory tree (high)

S5 and AC3 say `--write` removes an orphaned generated file. A generator that deletes files inside
`memory/` on the strength of its own idea of what should exist is a data-loss path: one bug in the
month-shard naming and it deletes a real record. Bound it in the spec, not in a code comment:

`--write` may delete ONLY a path matching `<MEMORY_ROOT>/ledger/<four-digit year>-<two-digit
month>.md` that a fresh render did not produce. Anything else that looks orphaned is REPORTED and
left alone. `--check` reports both classes and deletes nothing, ever.

## G4 — `---` is already a horizontal rule in this corpus (medium)

Fork B chose a `---` block. `builds/aPrunedCeremony/README.md` — written earlier in this same build —
uses `---` as a section separator between its two merged halves. A parser that scans for the first
two `---` lines anywhere would read the whole first half as front matter.

Front matter therefore opens at LINE 1 and nowhere else, and closes at the first subsequent `---`.
A README whose line 1 is not `---` has no front matter, which is the named error from G1's fallback
path, not a scan that wanders into the body.

## G5 — `LIVE.md` is wholly regenerated, so it cannot hold an orphan (medium)

AC3 asserts an orphaned `LIVE.md` ROW is reported and removed. `LIVE.md` is rendered from scratch
every time, so a stale row cannot survive a render — the criterion is unfalsifiable for that file and
would pass without testing anything. The orphan class is real for exactly one artifact: a ledger
shard FILE that a fresh render does not produce, because nothing regenerates a file the renderer no
longer emits. AC3 is narrowed to that.

## G6 — the retired file is linked from the memory root README (low)

`memory/README.md` line 3 carries a markdown link to the generated tree file. Deleting the file
without that edit reds hygiene check 2 in the same commit. Cheap, but worth naming so it is not
discovered from a red bar.

## Disposition

All six folded into rev-2 before any code. G1 adds the `status:` fallback field and its two-way
error; G2 adds the `.gitattributes` scope item; G3 bounds the delete; G4 pins front matter to line 1;
G5 narrows AC3; G6 joins the doc sweep.
