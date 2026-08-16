# TOOL-aRuledFrontispiece-1 — the build README gets a slot contract and an immutable authored plan

**Status:** OPEN · rev-3 · 2026-08-17 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

Give the build README a declared order of named slots, so that "authored" and "generated" become
positions in a file rather than a convention an author remembers. Every later unit in this build
renders into a slot this unit defines, and the gate in unit 6 checks the slots rather than the prose.

## 2. Scope (IN)

- **S1** — the README's top level is a fixed slot sequence: front matter, the `#` title, ONE authored
  prose block, the `roster:units` pair, then the generated regions. `gen_build_index.py` learns the
  sequence and refuses a file that violates it, under a NEW `--check-format` verb.
- **S1a** — the slot refusal is NOT reachable from `plan()`, `--write` or `--check`. Build READMEs
  violate the sequence at this unit's base, so a refusal wired into the render path would red hygiene
  check 9 across the corpus the moment this unit lands. `--check-format` is the only caller until the
  leg at position 11 makes it binding and the surgery at position 9 conforms the corpus.
- **S1b** — `--write` CREATES a missing generated-region marker pair, at the slot position the
  sequence defines. This is what lets the three region units at positions 3, 4 and 5 ship a renderer
  without any unit hand-inserting a marker: their region appears the first time `--write` runs after
  their code lands.
- **S1c** — `--check` does NOT demand a missing pair, and the asymmetry with S1b is deliberate and
  load-bearing. If `--check` reported a build README lacking a new region as stale, hygiene check 9
  would red at the tip of every region unit, each would have to re-render the whole corpus inside its
  own commit, and the re-render at position 10 would have nothing left to do. `--check` compares what
  is THERE against a fresh render of what is there; `--write` is the only verb that adds a pair.
- **S1d** — this unit owns the `--check-format` verb ENTIRELY: the argument parsing, the mode tuple
  and the usage line. The leg unit at position 11 adds a manifest row, a charter bullet and a dossier
  claim, and touches no line of the engine. That split is not tidiness — `gen_build_index.py` is a
  scanned delegate of the verdict-epoch gate, so an engine change at position 11 would land after the
  kit version bump at position 10 and red the leg at the build tip, where the pre-push hook blocks
  the landing push.
- **S2** — a second marker pair, `<!-- roster:units -->` and `<!-- /roster:units -->`, holds the
  AUTHORED unit plan. The generator never writes between those markers and refuses when asked to.
- **S3** — `apply_region` is generalised to take the marker pair as an argument, **defaulting to the
  two module constants**. The default is required, not a convenience: `tools/memory-tree/
  marker-contract.test.sh` calls it positionally with three arguments, so a signature change without
  a default breaks a leg this unit's own §7 names as a gate it must keep green.
- **S3a** — the three existing refusals — no pair, more than one pair, closing marker before opening
  — keep their wording, except that the one interpolating the marker literals names the pair it was
  CALLED with rather than the constants. "Preserved verbatim per named pair" is impossible for that
  message, and an earlier revision claimed it: a message built from the module constants cannot be
  both unchanged and correct about a different pair.
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
| further generated regions | their own `<!-- gen:… -->` pairs | generated | `apply_region`, created by `--write` per S1b |

**The generated regions have a canonical order and it is the order their units land in**:
`gen:build-index` first, then the order region, the edge region and the document inventory. An
earlier revision deferred this question to a slot table that had one generated row, which was a
closed loop — the table could not answer it. `--write` inserts a missing pair at its canonical
position, so the order is a property of the generator rather than of whoever edited last.

The sequence is a total order. A slot may be absent; two slots may not swap. Absence is legal for
prose and plan, and an absent index is already a named failure today.

### Inventory

Three refusal branches are added and one is generalised. The generalisation is the load-bearing
half: `apply_region` at `tools/memory-tree/gen_build_index.py:493` already refuses a missing pair, a
duplicated pair and an inverted pair, and those three refusals are exactly what a second named pair
needs. Copying them would be a second implementation of a predicate this build exists to stop
duplicating.

### Migration

None for the corpus in THIS unit, and S1a is what makes that true rather than an assumption.

An earlier revision of this spec claimed every build README already satisfies the sequence and that
none carries a plan pair. Both were false, and both were falsified by measurement rather than by
argument. At this unit's base:

| Fact | Measured |
|---|---|
| build READMEs tracked | 39 — read the live number from `gen_build_index.py --check`, never from here |
| carrying a real `roster:units` marker pair | 1, `memory/builds/aStandingWrit/README.md` at its lines 90 and 104 |
| with authored prose after the closing generated marker | 5, the largest being `memory/builds/aSiftedPlaybook/README.md` |
| with the plan pair ordered before its prose | 1, the same `aStandingWrit`, whose prose sits between the plan close and the generated open |

The plan pair was added by `TOOL-aStandingWrit-1`, whose spec header reads CLOSED and ratified. An
earlier revision of this section called it SPECCED and not landed, having read the backlog row rather
than the spec header; **the backlog row is stale and the code is live.** That distinction is the whole
weight of the paragraph: the pair is not a pending experiment this unit may redefine, it is a landed
integrity surface that `check_authorization` already byte-compares across a base commit. This unit
conforms to it rather than the other way round.

`aStandingWrit` is therefore a live case for S2 and AC3 rather than a fixture, and no synthetic
fixture can prove more than it does.

The surgery at position 9 conforms the corpus; the leg at position 11 makes the refusal binding.
Neither is this unit's work, and the ordering is stated in the build README rather than here.

### Alternatives rejected

Bounding the prose by a marker pair of its own was rejected: it makes every README carry two more
lines to solve a problem that position already solves, and an author who puts prose in the wrong
place is not helped by being asked to wrap it.

Detecting the plan slot by heading text rather than by a marker was rejected because
`check_authorization` in the unattended kit byte-compares a marker-delimited region across a base
commit, and a heading is not a delimiter it can address.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` · its `--selftest` arms ·
`tools/memory-tree/marker-contract.test.sh`, the second positional caller of `apply_region`, which
gains a case for a named pair · `tools/memory-tree/HYGIENE.template.md`, edited FIRST, with
`memory/HYGIENE.md` re-rendered from it. The direction matters: the parity harness renders the live
copy from the template, so editing the pair "together" inverts it.

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
- **AC2** — When a README places prose after its first generated marker,
  `python tools/memory-tree/gen_build_index.py --check-format` fails naming that file and the line
  number of the offending prose.
- **AC2a** — When a README places prose BETWEEN the plan pair's close and the first generated marker,
  `--check-format` fails the same way. This is the second way to break S4 and the one an earlier
  revision named no trigger for, which would have let the predicate pass `aStandingWrit` — the very
  file the surgery at position 9 must relocate.
- **AC2b** — When `--check-format` runs over `memory/builds/` at this unit's tip, the set of files it
  names equals the set derived by the two triggers above, measured at that same commit rather than
  copied from any list written here. A predicate that names too few is the defect AC2a exists for; one
  that names too many would put the surgery unit to work on files that do not need it.
- **AC3** — When `--write` runs over `memory/builds/aStandingWrit/README.md`, every byte between its
  `roster:units` markers is unchanged, compared with `git diff --exit-code` on that path. This is a
  LIVE case rather than a fixture: the region already contains an authored table that a renderer
  walking the file blind would rewrite.
- **AC4** — When a README carries two `roster:units` opening markers, `--check-format` fails with the
  same wording `apply_region` already uses for a duplicated pair.
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
- rev-2 · 2026-08-16 · §4 Migration asserted that every build README already satisfies the slot
  sequence and that none carries a plan pair. Both were false: five carry prose after the closing
  generated marker and `aStandingWrit` carries a real pair, ordered after its prose. Measured while
  authoring the sibling specs. Added S1a scoping the refusal to a new `--check-format` verb, because
  a refusal on the render path would have redded hygiene check 9 across the corpus on this unit's own
  commit; retargeted AC2 and AC4 onto that verb; rewrote AC3 to use `aStandingWrit` as a live case
  instead of a fixture.
- rev-3 · 2026-08-17 · folded the M4 spec audit. Added S1b and S1c: `--write` creates a missing
  region pair and `--check` does not demand one. Without S1b no unit inserted the three new marker
  pairs and three units would have landed renderers with zero call sites, which the audit called the
  set's largest defect; without S1c the same blocker returns as a corpus re-render inside every
  region unit's commit. Added S1d taking the whole `--check-format` verb, because the leg unit lands
  after the kit version bump and an engine change there reds the verdict-epoch leg at the build tip.
  S3 now defaults the pair parameters, since `marker-contract.test.sh` calls `apply_region`
  positionally; S3a withdraws the impossible "verbatim per named pair" claim. Corrected §4: the
  `aStandingWrit` pair is CLOSED and live, not SPECCED — read from the spec header after an earlier
  revision trusted a stale backlog row. Added AC2a for the second violation shape, which the single
  stated trigger missed, and AC2b to keep the predicate neither vacuous nor over-broad. Stated the
  canonical inter-region order, previously deferred in a closed loop.

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
