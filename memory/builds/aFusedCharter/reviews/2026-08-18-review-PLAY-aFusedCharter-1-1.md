# Spec audit — the aFusedCharter set, pre-code

## Verdict: BLOCKED

**Serves:** spec-audit PLAY-aFusedCharter-1 PLAY-aFusedCharter-2 PLAY-aFusedCharter-3 TOOL-aFusedCharter-1 TOOL-aFusedCharter-2 TOOL-aFusedCharter-3 DEPL-aFusedCharter-1

Workflow `wf_c1d36a63-158` · node a · base `497d25d0` · 7 agents, 1.33 M subagent tokens.
Shape: four primed document lenses, then batched default-refute skeptics, then one synthesis —
under the review protocol's fan-out and concurrency caps.

**The verdict above is the audit's, and every finding in it has since been folded.** All seven specs
were re-revved; the disposition table at the bottom maps each finding to the revision that answers
it. Nothing was waived. Two forks were raised to the owner rather than taken, and both carry a
recommendation the build can proceed on.

## What was audited, and how

The four lenses were underspecification, cross-set contradiction, unstated assumptions about the
tree, and missed blast radius. Each was primed with the build README, the spec format contract and
the build method, and told to verify every claim about existing code against SOURCE rather than
against the spec's assertion. The skeptics defaulted to REFUTED and re-read the cited source before
confirming. The synthesis re-verified every blocker and every source-side claim in the highs itself.

Precision was high and asymmetric in a useful way: ten claims were refuted, including two the build
had already self-caught and fixed between the audit's launch and its return, and several that were
simply wrong about the tree. Those are recorded below so a later reader does not re-raise them.

## The three blockers

Each of these reds a merge-bar leg on a landing pass, with no unit owning the fix.

**B1 — the parity gate's two value-parity rows extract from the bullet `PLAY-1` S7 moves out.**
`tools/check-playbook-parity.sh` declares two `PAIRS` rows; both take their stated side from the
template, and both extractions match exactly one line in the whole trio — the concurrency bullet
carrying the lens-array bound and the hook matcher. Moving that grammar to the hook's README leaves
both extractions matching nothing, and the gate's own anti-vacuity arm reds. Folded: `PLAY-1` S7 now
keeps both literals verbatim in the retained bullet and verifies by running the gate;
`TOOL-1` S3 records that `PAIRS` is deliberately not repointed, and F2 raises the alternative to the
owner.

**B2 — deleting the parity gate's catalogue stage trips its own arms floor.** That stage is six
`fail` branches, and `.memory-tree.conf` pins the gate at a branch/armed pair of 15 and 15;
post-deletion it reads 9 and `check-arms.py` refuses the shrink. Folded: new `TOOL-1` S4a lowers the
pair to the measured value in the same commit, with the reason beside it, and retires the matching
sibling arms.

**B3 — three units add a gate leg before the charter stops enumerating legs.** The drift signal
`handkept_inventories_disagreeing_with_source` measures 0 of 70 against a pin of 0 and is gateable:
a leg whose script path the charter does not name takes it over the pin. `DEPL-1`, `TOOL-2` and
`TOOL-3` each add a leg, and the charter bullets never arrive because `PLAY-3` deletes that section.
Folded by REORDERING the fix rather than the units: the signal retirement moves from `PLAY-3` S4 to
`TOOL-1` S10, which lands in the first pass, so every later unit is unblocked. Retiring it early
costs nothing — the charter still names every pre-existing leg until `PLAY-3` cuts the section.

## The highs

| id | what it found | folded into |
|---|---|---|
| H1 | `lexicon` is named ONLY in the file this build deletes and has no waiver row, so the kit-coverage arm reds; the same trap awaits the new `tools/playbook/` | `PLAY-1` S6 (an addition, not a move) · `DEPL-1` S1a |
| H2 | the registry's `[[exempt]]` row for the customize companion, and a reason string that becomes false | `TOOL-1` S5 |
| H3 | `tools/hooks/README.md` does not exist, and creating it under a non-flat kit home reds `selfcheck` without a file rule | `PLAY-1` S7 |
| H4 | `core.autocrlf` is true and the charter carries 302 CR against a 0-CR blob, so an LF render byte-compared against it mismatches on every line, on every node | `TOOL-1` S4b (attributes) · `DEPL-1` S5a (normalise) · `PLAY-3` S6a |
| H5 | three wrong facts about the drift-signal retirement mechanism — probe versus signal, `NOT ASKED` versus empty-by-declaration, and selftest arms that do not exist | `TOOL-1` S10 · `PLAY-3` S4 |
| H6 | shipping gov's own limits rows to adopters reds them on install day, which is the failure the spec's own fork calls decisive | `TOOL-3` S8 (seed from the adopter's tree) |
| H7 | four conditionals are keyed on a project property, not a kit, and have no registry id to be fenced with | `PLAY-1` S8 (a second `when:` namespace) · `DEPL-1` S4 |
| H8 | the marker-region helper RAISES with no marker pair, and the contract test slices reader bodies by hand — so neither "reuses that contract" claim held | `DEPL-1` S5 (a fifth reader, added to the case table) |
| H9 | a second registry entry named `playbook` would silently shadow the first | `DEPL-1` S1 (`playbook-render`) |
| H10 | "five glyphs are pinned" with no enumeration anywhere, while the gate undertook to grade them | `PLAY-2` S1 · `TOOL-2` S2 |
| H11 | three shapes still violate the grammar after the stated dispositions, one carrying no joiner at all | `PLAY-2` S4 · `TOOL-2` S2 (a joiner-POSITION predicate) |
| H12 | the gate keyed on a heading the section does not have, and a column-zero selector would swallow the whole section | `PLAY-2` S8 (a fence) · `TOOL-2` S1 |

## The mediums and lows

Fifteen mediums and ten lows, all folded. The ones worth naming here because they changed a number
or a mechanism rather than a sentence:

- **Units were mixed throughout.** Every section inventory was measured in CHARACTERS under a column
  headed "Bytes", while the size ceiling is bytes. The converged projection is ~44 400 bytes, not
  43 998, and the ruleset has FOUR lines over 450 characters, not five — one measures 462 bytes and
  449 characters and is already compliant. Folded into the README, `PLAY-1` `§4`, `PLAY-3` `§4` and
  `TOOL-3` S6.
- **The size high-water was nobody's job.** The record holds 37 381 and the converged file lands
  ~7 KB above it, so the gate would print its growth warning forever. `TOOL-3` S0 now owns the bump.
- **Two glob lists, not one.** `drift_signals.py` enumerates the three paths twice, in
  deliberately different-sized lists, and a half-repoint drifts a pin for an unrelated reason.
- **Three map dossiers carry falsified claims that spell none of the old filenames**, so the
  completeness grep is blind to them.
- **The manifest names the template at five lines**, two of which are separately-checked contracts,
  and one of which asserts a file count this build changes.
- **The assertion-count contract is three things**, not "prints a count" — a suite built to the
  earlier wording lands non-compliant.
- **A guard naming only the gate and its test skips the gate on exactly the diffs it exists for.**
- **The fence parser would be copy number six**, not a reuse; the hygiene gate's is a private shell
  function and that script already carries four inline copies.
- **`TOOL-1` F1 was closed before it was asked** — the dead-path counter reads 0 after the rename for
  two structural reasons, neither of them the exemption the fork asked about.

## Refuted — do not re-raise

- The placeholder census being short by one, and the frozen-record count of 60. Both were self-caught
  and fixed at rev-2 before the audit returned.
- Every part figure in `PLAY-3` being 2 to 201 low. They reproduce exactly as character counts;
  the defect was the column label, kept as a low.
- Multi-line answers having no transport through the deployer's answer writer. Every asked key is a
  phrase or a path.
- `selfcheck` being unable to see a new file under `tools/hooks/` because its surface predicate is
  depth-1. True of one arm, false of another — which is what makes H3's fix a file rule rather than
  a gate listing.
- The converged projection being wrong by ~2.3 KB. Two independent reconstructions land within about
  one per cent, fully explained by the character/byte unit error.
- No entry claiming a root-level `tools/check-*.sh`. Six such flat entries exist; the defect was that
  the specs did not choose a route, not that no route existed.
- The declared-empty mechanism offering three incompatible edits. One coherent edit exists; the real
  defects were the three wrong facts in H5.

## Left open — and what happened to each

- **Which conditional rows survive the kit-prose move.** Not sizeable from the specs. `PLAY-1` S8 now
  makes an ENUMERATION its first deliverable, performed against the folded file before any fence is
  written.
- **Whether the converged file fits under the ceiling in bytes.** Depends on prose not yet written.
  The README states the projection, labels its unit, and requires the build to measure and raise a
  fork rather than edit the constant.
- **Where the parity gate's rows should point.** Raised to the owner as `TOOL-1` F2, recommending the
  status quo, because changing what that gate is FOR is a governance-carrier change.
- **Whether the two new gates ship to adopters.** Resolved: both ship as flat registry entries marked
  conditional, so an adopter who takes the playbook can take the gate and `--all` does not force it.
- **The target descriptor's location against the root-conf convention.** Raised to the owner as
  `DEPL-1` F4, recommending the status quo.

## Disposition

| spec | rev after fold |
|---|---|
| `PLAY-aFusedCharter-1` | rev-2 |
| `PLAY-aFusedCharter-2` | rev-2 |
| `PLAY-aFusedCharter-3` | rev-2 |
| `TOOL-aFusedCharter-1` | rev-3 |
| `TOOL-aFusedCharter-2` | rev-2 |
| `TOOL-aFusedCharter-3` | rev-2 |
| `DEPL-aFusedCharter-1` | rev-3 |

Every blocker, high, medium and low is folded. Two owner forks are marked in place. Per the build
method, once a synthesis pass calls a design clean the review stops — this one did not call it clean,
so the set is folded and stands ready for a second pass only if the owner wants one before building.
