# TOOL-aBoundedVerdict-4 — a fork that says it is unresolved stops reading as resolved

**Status:** OPEN · rev-1 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

Both machine readers of a spec's §8 Open questions decide resolution with an unanchored
case-sensitive substring over the section's FIRST non-blank line, so a §8 whose first line announces
that a fork is NOT resolved classifies as resolved, and any unresolved bullet below that line is
invisible. Harden both readers so the fork rule every other unit in this build writes is actually
enforceable.

## 2. Scope (IN)

- **S1** — `tools/unattended/unattended.sh`'s `plan_state` stops testing `forkline ~ /RESOLVED/`.
  The replacement requires the resolution marker to appear as the documented mark rather than as any
  occurrence of the word: anchored to a bullet or sub-head, and carrying the attribution shape
  `memory/TEMPLATE-SPEC.md` already demands — a resolver of `owner` or `agent`, a date, and the
  optional `delegated` qualifier.
- **S2** — the same predicate in `tools/memory-tree/check-memory-hygiene.sh` check 12, at both the
  per-item count and the first-line short circuit. One predicate, spelled once per gate, with the
  two spellings byte-compared by an arm rather than trusted to stay in step.
- **S3** — both readers stop deciding on the first non-blank line alone. `plan_state` classifies
  FORKED when ANY §8 item is unresolved, matching what check 12 already attempts per item; check 12
  stops short-circuiting a terminal spec's §8 on the first line's shape.
- **S4** — the marker grammar becomes a stated contract in `memory/TEMPLATE-SPEC.md`'s §8 section,
  where an author reads it, phrased as the shape the gate reads rather than as advice.
- **S5** — a corpus pass before the predicate tightens: every tracked spec whose §8 currently passes
  and would newly fail is enumerated, and each is either repaired in this unit or registered with a
  reason. A predicate that reds landed work on the day it lands is not shippable.
- **S6** — `KIT_MEMORY_TREE_VERSION` moves, because S2 edits a non-comment line of the hygiene
  engine and the verdict-epoch gate dates the engine's verdicts by that constant.

## 3. Non-goals (OUT)

- No change to what §8 MEANS, to the resolver-authority rules, or to who may sign a resolution. This
  unit changes only how a machine recognises the mark.
- No new gate leg. Both readers already exist and both already run on the bar.
- No repair of the planning verb's other known blindness beyond what S3 incidentally closes; the
  tracked backlog row for it keeps its own disposition, and this spec's revision log names the
  overlap rather than silently absorbing it.
- No enforcement that a delegated resolution is signed as delegated rather than as the owner. The
  attribution SHAPE is checked; whether the named resolver really decided is not checkable here and
  this unit does not pretend otherwise.

## 4. Design

### Data model

A §8 item is a line opening with a bullet marker or a `###` sub-head, which is the population check
12 already walks. An item is RESOLVED when its text carries the mark in the documented shape:
the literal resolution word immediately followed by a parenthesised attribution whose first field is
`owner` or `agent`, whose second is a date, and whose optional third is the delegation qualifier.
The section is resolved when it has at least one item and every item is resolved, or when its first
non-blank line is the machine-legal none form.

The current predicate accepts three strings it must not: a line saying a fork is not resolved, a
line describing the resolution rule in prose, and a line quoting another spec's resolved fork. All
three are reachable in ordinary authoring and the first is reachable by accident.

### Inventory

| Site | Today | After |
|---|---|---|
| `unattended.sh` `plan_state` | unanchored substring over the first non-blank line only | the shaped mark over every item |
| `check-memory-hygiene.sh` check 12, per-item count | unanchored substring per item | the shaped mark per item |
| `check-memory-hygiene.sh` check 12, first-line short circuit | section skipped when the first line opens with the none form | the none form still exits early; any other first line no longer suppresses the per-item walk |
| `memory/TEMPLATE-SPEC.md` §8 guidance | prose describing the mark | the same prose plus the shape the gate reads |

The two gates cannot share source — one is a shell gate in the unattended kit, the other a shell
gate in the memory-tree kit, and neither may import the other. The kits are independently
installable and a cross-kit import would make one a dependency of the other. So the predicate is
spelled twice on purpose, and the defence against drift is an arm that feeds one case table to both
spellings, in the shape `tools/memory-tree/marker-contract.test.sh` already uses for the
generated-region markers: the contract lives in the table, not in prose.

### Migration

S5 is the migration and it runs BEFORE S1 and S2 land, not after. The enumeration is mechanical: run
the new predicate over every tracked spec, diff the resolved/unresolved verdict against the old
predicate's, and read every spec whose verdict moves. A spec whose §8 is genuinely resolved but
whose mark is malformed is repaired in place with a rev bump and a revision-log line. A spec that is
genuinely unresolved under a terminal status is a pre-existing defect this unit surfaces rather than
creates, and it gets a backlog row rather than a silent waiver.

### Alternatives rejected

- **Anchor the match without requiring the attribution.** Cheaper, and it closes the accidental case
  — a line saying a fork is not resolved no longer passes. It leaves the deliberate case open: a
  bare resolution word with no resolver still counts, in the exact remedy that makes agent-signed
  resolutions the norm. Rejected because the attribution is already mandatory in the authoring
  contract and checking a rule nobody enforces is how that rule rotted.
- **Fix only the hygiene gate.** The planning verb is what an unattended run actually consults
  before building a unit, so leaving it blind leaves the run building forked units. Rejected.
- **Fix only the planning verb.** Leaves a terminal spec with an unresolved fork passing the merge
  bar. Rejected.
- **Extract the predicate into a shared script both kits call.** Rejected on the install-prefix
  rule: it would put a memory-tree file on the unattended kit's dependency list, and each kit
  resolves its own prefix precisely so neither has to find the other.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` ·
`tools/memory-tree/check-memory-hygiene.sh` · `tools/memory-tree/check-memory-hygiene.test.sh` ·
`memory/TEMPLATE-SPEC.md` and its kit template · `.memory-tree.conf` (the arms floors) · whichever
specs S5's enumeration names.

## 5. Production-readiness checklist

- security — N/A. No new input, no new write path, no new surface.
- perf / scale — N/A. The per-item walk already exists in check 12; the planning verb gains one pass
  over a section it already reads.
- a11y — N/A. No user-facing surface.
- i18n — N/A. The mark is a repo-internal grammar, not prose for translation.
- error / empty / loading states — a §8 with no items and no none form is today silently resolved by
  the empty-first-line branch. The new predicate must decide it explicitly and the decision must be
  refuse, on this repo's own rule that a check never selects an empty population.
- observability — the enumeration in S5 is the observation, and it is recorded rather than run and
  discarded.
- risks — the real one is S5's blast radius: a predicate that reds landed specs. It is the reason S5
  precedes S1 and S2 rather than following them.
- testing + left-shift gates — the shared case table is the left-shift. A future third reader of §8
  is expected to join it.
- migration / rollback — rollback is reverting the two predicates; the version constant moves with
  them so a half-reverted tree reds rather than passing quietly.
- user docs — S4 is the doc change, and it is in the file authors actually read.

## 6. Acceptance criteria

- **AC1** — When a spec's §8 opens with a line announcing the fork is not resolved,
  `bash tools/unattended/unattended.sh --plan <slug>` classifies it FORKED, not `READY - build it`.
  Fixtured in `tools/unattended/unattended.test.sh` with the pre-change behaviour as the control.
- **AC2** — When a spec's §8 first line carries the none form and a LATER bullet is unresolved,
  `bash tools/unattended/unattended.sh --plan <slug>` classifies it FORKED. Same fixture file.
- **AC3** — When a spec under a terminal status carries an unresolved §8 item below a none-form
  first line, `bash tools/memory-tree/check-memory-hygiene.sh` reds naming that file, and the arm
  lives in `tools/memory-tree/check-memory-hygiene.test.sh`.
- **AC4** — When a §8 item carries the resolution word with no parenthesised attribution, both
  readers treat it as unresolved. One case table drives both, asserted by a new arm beside
  `tools/memory-tree/marker-contract.test.sh`.
- **AC5** — When the new predicate runs over every tracked spec, the enumeration of specs whose
  verdict moves is committed under this build's `build/` folder, and every named spec is repaired or
  carries a backlog row.
- **AC6** — When a non-comment line of `tools/memory-tree/check-memory-hygiene.sh` moves,
  `bash tools/memory-tree/check-verdict-epoch.sh` stays green, which requires
  `KIT_MEMORY_TREE_VERSION` to move in the same commit.
- **AC7** — When every new refusal branch is in place, `python tools/memory-tree/check-arms.py
  --check` exits 0, with the `ARMS_FLOORS` entries for both edited gates raised in the same commit.
- **AC8** — `GATE_FULL=1 bash tools/run-gates.sh` is green.

## 7. Gates

`tools/memory-tree/check-memory-hygiene.sh` and its sibling test ·
`tools/memory-tree/check-verdict-epoch.sh` and its sibling ·
`tools/memory-tree/kit-dogfood-parity.test.sh` (the spec template ships from the kit) ·
`tools/memory-tree/check-arms.py` · `tools/unattended/check-unattended.sh` and its two siblings ·
`tools/memory-tree/marker-contract.test.sh` · `bash tools/run-gates.sh`.

## 8. Open questions

- **F1 — does a §8 with items but no marks and no none form refuse, or pass?** The empty-section
  branch is what makes today's behaviour silent. Options: refuse, which is this repo's stated rule
  about empty populations and is what §5 recommends; or pass, preserving today's behaviour for a
  shape no landed spec is known to use. Recommendation: refuse, and let S5's enumeration price it.
- **F2 — is the attribution's DATE validated as a date, or only as a non-empty field?** Validating
  the shape costs one pattern and catches a mark whose date field holds prose. Not validating keeps
  the predicate readable. Recommendation: shape only, on the same grounds the acceptance-witness rule
  gives for checking that a bullet names something rather than that the thing exists.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft. Records that S3 incidentally closes the blindness a tracked
  backlog row raises against the planning verb's first-line-only read; that row keeps its own
  disposition and is not claimed closed here.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "decide whether a spec's open questions are resolved"`
returns the two readers named in S1 and S2 and no third, which is what makes the two-spellings
decision in §4 a bounded one rather than an open-ended one. The seam this unit extends is
`tools/memory-tree/marker-contract.test.sh`'s case-table shape — an existing, gated arm that already
drives four live readers of one marker grammar over a single table, which is exactly the problem
this unit has with two readers of another. No new seam is created.

Recall terms used, recorded for the reground: fork resolution marker RESOLVED attribution delegated
owner agent open questions predicate anchored substring plan_state hygiene check 12.
