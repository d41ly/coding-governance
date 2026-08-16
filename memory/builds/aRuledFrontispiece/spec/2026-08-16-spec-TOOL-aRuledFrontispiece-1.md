# TOOL-aRuledFrontispiece-1 — the build README gets a slot contract and an immutable authored plan

**Status:** OPEN · rev-1 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

Give the build README a declared order of named slots, so that "authored" and "generated" become
positions in a file rather than a convention an author remembers. Every later unit in this build
renders into a slot this unit defines, and the gate in unit 6 checks the slots rather than the prose.

## 2. Scope (IN)

- **S1** — the README's top level is a fixed slot sequence: front matter, the `#` title, ONE authored
  prose block, the `roster:units` pair, then the generated regions. `gen_build_index.py` learns the
  sequence and refuses a file that violates it.
- **S2** — a second marker pair, `<!-- roster:units -->` and `<!-- /roster:units -->`, holds the
  AUTHORED unit plan. The generator never writes between those markers and refuses when asked to.
- **S3** — `apply_region` is generalised to take the marker pair as an argument instead of closing
  over the two module constants. Its three existing refusals — no pair, more than one pair, closing
  marker before opening — are preserved verbatim and now apply per named pair.
- **S4** — the authored prose block is bounded: prose may appear between the title and the
  `roster:units` pair, and nowhere else at top level. Prose found after the first generated marker is
  a named failure that prints the offending line number.
- **S5** — a build README with no `roster:units` pair is LEGAL and unchanged. The pair is opt-in by
  presence, which is the branch `check_authorization` in the unattended kit already takes.
- **S6** — the refusals in S1, S2 and S4 name the file and the line, never a count alone, so an
  operator can act on the message without re-deriving where the violation is.

## 3. Non-goals (OUT)

- Rendering anything new. The document inventory is unit 4, the order region is unit 2 and the edge
  region is unit 3; this unit only declares where they may go.
- Requiring the `roster:units` pair. Making it mandatory is `TOOL-cBriefedPilot-18` on another node,
  and forks 1 and 5 both point at opt-in for this build.
- Changing `LIVE.md` or the ledger shards. Fork 8 resolved those to no change.
- Retrofitting any existing README. Unit 10 owns the corpus.
- Enforcing the slot contract on the merge bar. That is the leg in unit 6; this unit ships the
  predicate and its arms, the leg makes it binding.

## 4. Design

### Data model

The README is parsed as an ordered list of top-level slots. A slot is identified by what opens it,
not by its content:

| Slot | Opens with | Class | Writer |
|---|---|---|---|
| front matter | `---` at line 1 | generated in part | `apply_front_matter_ids` rewrites `ids:` |
| title | the first `#` heading | authored | nobody |
| prose | any non-marker content after the title | authored | nobody |
| plan | `<!-- roster:units -->` | authored, immutable | nobody |
| index | `<!-- gen:build-index -->` | generated | `apply_region` |

The sequence is a total order. A slot may be absent; two slots may not swap. Absence is legal for
prose and plan, and an absent index is already a named failure today.

### Inventory

Three refusal branches are added and one is generalised. The generalisation is the load-bearing
half: `apply_region` at `tools/memory-tree/gen_build_index.py:493` already refuses a missing pair, a
duplicated pair and an inverted pair, and those three refusals are exactly what a second named pair
needs. Copying them would be a second implementation of a predicate this build exists to stop
duplicating.

### Migration

None for the corpus. Every build README today has the front matter, title, prose and index slots in
the required order, and none has a `roster:units` pair, so S5's opt-in branch is the live case for
all of them. Unit 10 verifies that claim over the whole corpus rather than trusting this sentence.

### Alternatives rejected

Bounding the prose by a marker pair of its own was rejected: it makes every README carry two more
lines to solve a problem that position already solves, and an author who puts prose in the wrong
place is not helped by being asked to wrap it.

Detecting the plan slot by heading text rather than by a marker was rejected because
`check_authorization` in the unattended kit byte-compares a marker-delimited region across a base
commit, and a heading is not a delimiter it can address.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` · `tools/memory-tree/gen_build_index.py` selftest arms ·
`memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md` as a byte-paired edit.

## 5. Production-readiness checklist

- security — N/A. No new input crosses a trust boundary; the parser reads tracked files already read.
- perf / scale — one extra pass over each README during a render that already reads the file whole.
- a11y — N/A. No user-facing surface.
- i18n — N/A. Markers are ASCII literals.
- error / empty / loading states — a README with no prose, no plan, or an empty prose block is legal
  and must render unchanged; each is an arm.
- observability — every refusal names the file and the line.
- risks — the generalisation of `apply_region` touches the one function every other unit calls. A
  regression there is silent in `--check` because the byte compare would agree with the wrong render.
  Mitigated by keeping the three refusal messages byte-identical and arming each.
- testing + left-shift gates — arms in the generator's `--selftest`; the binding leg is unit 6.
- migration / rollback — revert is a single-file revert; no corpus bytes change in this unit.
- user docs — the slot table lands in `HYGIENE.md` and its kit template together.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --check` runs over the corpus at this
  unit's tip, it reports clean at the same artifact count it reports at `base 96141aed`.
- **AC2** — When a README places prose after its first generated marker, `--check` fails naming that
  file and the line number of the offending prose.
- **AC3** — When a README carries a `roster:units` pair, `--write` leaves every byte between those
  two markers unchanged, proved by a fixture whose plan block contains text that a naive renderer
  would rewrite.
- **AC4** — When a README carries two `roster:units` opening markers, `--check` fails with the same
  wording `apply_region` already uses for a duplicated pair.
- **AC5** — When a README carries no `roster:units` pair, `--write` and `--check` behave exactly as
  they do at `base 96141aed`, proved by a fixture asserting byte equality against the current render.
- **AC6** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, it passes and its arm
  count is strictly greater than at `base 96141aed`.

## 7. Gates

`python tools/memory-tree/gen_build_index.py --selftest` · hygiene check 9 via
`bash tools/memory-tree/check-memory-hygiene.sh` · `bash tools/memory-tree/kit-dogfood-parity.test.sh`
for the paired `HYGIENE.md` edit · `bash tools/memory-tree/marker-contract.test.sh`, because a second
marker pair enters the contract that test drives · `bash tools/memory-tree/check-verdict-epoch.sh`,
which unit 10 discharges for the whole build.

## 8. Open questions

none — fork 1 at the build README resolved the plan pair's contents to Option A, and forks 5 and 8
resolved the two questions this unit would otherwise have had to ask.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft.

## 10. Reuse audit

Recall terms used, recorded so a resumed session re-runs the same query: `authored derived section
front matter schema refused ids roster marker region truth-blind parity byte-compare generated
index`.

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| splice into a named marker pair | `apply_region` at `gen_build_index.py:493` | EXTEND — parameterise the pair, keep all three refusals |
| refuse an anchored rewrite that is ambiguous | `strip_records_sentence` at `gen_build_index.py:396` | REUSE THE SHAPE — refuse on more-than-one and on partial match |
| rewrite one anchored front-matter line | `apply_front_matter_ids` at `gen_build_index.py:473` | REUSE unchanged; this unit adds no front-matter key |
| byte-compare an authored region across a base commit | `check_authorization` in `tools/unattended/unattended.sh` | REUSE unchanged — S5's opt-in-by-presence is the branch it already takes |

The map probe for "render a marker-delimited generated region into a committed markdown file"
returned `apply_region` and `render_region` in `gen_build_index.py` as the only marker-region seams
in the corpus, and no seam for an immutable authored region outside the unattended kit. The claim
that `apply_region` carries exactly three refusals was verified against source at writing time.
