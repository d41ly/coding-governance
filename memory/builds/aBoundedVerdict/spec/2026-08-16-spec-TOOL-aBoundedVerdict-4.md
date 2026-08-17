# TOOL-aBoundedVerdict-4 — a fork that says it is unresolved stops reading as resolved

**Status:** SPECCED · rev-4 · 2026-08-17 · node a · Tier-2 · base 96141aed · streams tooling · ratified 2026-08-17

## 1. Goal

Both machine readers of a spec's §8 Open questions decide resolution with an unanchored
case-sensitive substring, and both short-circuit on the section's first non-blank line, so a §8 whose
first line announces that a fork is NOT resolved classifies as resolved and any unresolved bullet
below it is invisible. Harden both readers so the fork rule every other unit in this build writes is
actually enforceable.

## 2. Scope (IN)

- **S1** — `tools/unattended/unattended.sh`'s `plan_state` stops testing for the bare resolution
  word anywhere on one line. The replacement walks every §8 ITEM and requires the documented mark:
  the resolution word followed by a parenthesised attribution whose first field is `owner` or
  `agent`, whose second is a date, and whose optional third is the delegation qualifier. The
  classifier is tightened unconditionally, with no date gate, because it grades only the specs of the
  build currently running.
- **S2** — the same predicate in `tools/memory-tree/check-memory-hygiene.sh` check 12, at both the
  per-item count and the first-line short circuit, gated by a new cutoff (S6). The two spellings are
  joined by ONE CASE TABLE driving both — an EXTENSION of `tools/memory-tree/marker-contract.test.sh`,
  whose display name and header move to cover two contracts, not a byte-comparison of two dissimilar
  languages and not a new leg.
- **S2a** — the table's MECHANISM, because that harness's existing shape does not transfer and rev-2
  cited it as a precedent without saying so. Three obstacles, each measured: the existing harness
  slices a NAMED shell function out of the shipped bytes by line range, and check 12's §8 predicate
  is inline inside one long single-quoted awk program with no function boundary to slice; the two
  readers grade DISJOINT status populations, since check 12's §8 block runs only under a terminal
  status while the planning verb discards its own classification for exactly those statuses; and S6's
  cutoff gates only the hygiene side, so an unresolved case legitimately gives the two readers
  different answers. So the table holds inputs plus a PER-READER expected verdict, the hygiene side
  is driven through a fixture repo the way its own sibling test already does, and the table records
  each side's fixture requirements — a terminal status and a filename date at or after the cutoff for
  check 12, a non-terminal status with non-empty scope, acceptance and gates sections for the
  planning verb. Lifting the hygiene predicate into a sliceable function first is the alternative and
  is left to the builder, named here so the choice is visible.
- **S3** — both readers stop deciding on the first non-blank line alone. The none form ends the
  section only when the section has ZERO items; with any item present, the per-item walk decides and
  no first line suppresses it.
- **S4** — the marker grammar becomes a stated contract in the two carriers that today describe the
  OLD behaviour: `memory/TEMPLATE-SPEC.md`'s §8 guidance, and `memory/guides/BUILD-METHOD.md` M3,
  whose sentence "Keep §8's first non-blank line machine-legal … the hygiene gate reads that line and
  nothing else" becomes false the moment S3 lands. Both ship from kits, so both templates move too.
- **S5** — the predicate is MEASURED against the whole tracked corpus before it tightens, and the
  measurement is recorded in the conf beside the cutoff it justifies, the way the acceptance-witness
  ratchet records its own. The measurement is evidence for the cutoff, not a repair worklist.
- **S6** — a new `.memory-tree.conf` cutoff key gating S2, set strictly ahead of every committed
  spec's filename date so nothing landed is retroactively red. This is the fourth instance of a
  pattern the conf already carries three times, and the reason it is used here rather than a waiver
  registry is that check 12 HAS no waiver mechanism — its population is selected only by the dated
  filename regex, the format cutoff and the diff-scope test.
- **S7** — `KIT_MEMORY_TREE_VERSION` moves, because S2 edits a non-comment line of the hygiene
  engine and the verdict-epoch gate dates the engine's verdicts by that constant. The constant is
  required present on every tracked memory-tree template, so the marker-only edits ride with it.

## 3. Non-goals (OUT)

- No change to what §8 MEANS, to the resolver-authority rules, or to who may sign a resolution. This
  unit changes only how a machine recognises the mark.
- No repair of any landed spec. S6's cutoff is what makes that unnecessary, and rewriting a ratified
  record is against the memory tree's own rule.
- No new gate LEG, and S2's case table therefore EXTENDS `tools/memory-tree/marker-contract.test.sh`
  rather than landing beside it. Rev-2 offered both and they are not interchangeable: a new sibling
  is either a row in `tools/gate-legs.json` — which pulls in the run-gates canary and the
  codebase-map leg inventory, whose baseline is closed to new keys, so the key reds until a dossier
  claims it — or it is a test nothing runs. Extending needs neither. The cost of extending is that
  the leg's display name and header must move to cover two contracts, and S2 says so.
- No enforcement that a delegated resolution is signed as delegated rather than as the owner. The
  attribution SHAPE is checked; whether the named resolver really decided is not checkable here.
- No repair of the planning verb's other known blindness beyond what S3 incidentally closes. The
  tracked backlog row for it keeps its own disposition.

## 4. Design

### Data model

**An ITEM** is a line opening with a bullet marker or a `###` sub-head, TOGETHER WITH every following
line until the next item or the end of the section. The block reading is not a preference: the spec
template explicitly sanctions a multi-line fork, and the corpus's dominant convention puts the mark
on an indented continuation line — the most recent closed build has both its §8 marks on the second
line of their bullets. Both existing readers grade one line and have no notion of an item spanning
lines, so block extraction is new work in both, and S1 and S2 each carry it.

**An item is RESOLVED** when its block carries the resolution word immediately followed by a
parenthesised attribution whose first field is `owner` or `agent`, whose second is a date, and whose
optional third is the delegation qualifier.

**A SECTION is resolved** when either of two conditions holds, and the ordering between them is the
whole of what rev-1 got wrong:

1. it has ZERO items and its first non-blank line is the bare none or not-applicable form; or
2. it has at least one item and EVERY item is resolved.

**The none form never suppresses the per-item walk.** With any item present, condition 2 decides
alone. Rev-1's §4 and its inventory row said the opposite of its own S3 and acceptance criteria, and
the two readings select mutually exclusive code — this ordering is the resolution.

The current predicate accepts three strings it must not: a line saying a fork is not resolved, a line
describing the resolution rule in prose, and a line quoting another spec's resolved fork. All three
are reachable in ordinary authoring and the first is reachable by accident.

### Inventory

| Site | Today | After |
|---|---|---|
| `unattended.sh` `plan_state` | the bare word, on the first non-blank line only | the shaped mark, over every item's block; the none form ends the section only when there are no items |
| `check-memory-hygiene.sh` check 12, per-item count | the bare word, on the item's opening line | the shaped mark, over the item's block |
| `check-memory-hygiene.sh` check 12, first-line short circuit | a none or not-applicable first line suppresses the verdict whatever the walk found | it ends the section only over a zero-item section |
| `memory/TEMPLATE-SPEC.md` §8 guidance | prose describing the mark | the same prose plus the shape the gate reads |
| `memory/guides/BUILD-METHOD.md` M3 | states the gate reads the first line and nothing else | states the per-item rule this unit installs |

The two gates cannot share source — one is a shell gate in the unattended kit, the other in the
memory-tree kit, and neither may import the other, because the kits are independently installable
and a cross-kit import would make one a dependency of the other. So the predicate is spelled twice
on purpose, and the defence against drift is the shared case table S2 names.

### Migration

**There is none on disk, and S6 is why.** The cutoff grandfathers every landed spec by filename date,
so the tightened predicate applies to specs written after it and to nothing else. This replaces
rev-1's plan to repair or waive the affected specs, which was unbuildable in both halves: check 12
has no waiver mechanism at all — its §8 grading block reads no registry and none of the six under
`memory/project/` is consulted by it — and repairing a landed spec rewrites a ratified record.

The consequence is that the corpus does NOT exercise the tightened arm, which this repo names as its
own vacuity class. The arm is therefore explicit red and green fixtures in each gate's sibling test,
which is the same disposition the streams ratchet took for the same reason and recorded in the conf.

### Alternatives rejected

- **Anchor the match without requiring the attribution.** Cheaper, and it closes the accidental case.
  It leaves the deliberate case open: a bare resolution word with no resolver still counts, in the
  exact remedy that makes agent-signed resolutions the norm. Rejected because the attribution is
  already mandatory in the authoring contract and checking a rule nobody enforces is how that rule
  rotted.
- **Grade the item's opening line only.** Cheaper in both readers and needs no block extraction.
  Rejected on the corpus, which measures 33 of 41 item-bearing terminal specs failing the
  opening-line reading against 13 for the block reading. **That is evidence about the AUTHORING
  CONVENTION, not a prediction about this unit** — S6's cutoff grandfathers every one of those specs,
  so neither reading reds anything landed, and rev-2's "newly red" phrasing described an outcome this
  unit cannot produce. The convention is what matters: it is what future specs will follow, so
  opening-line grading would red correct authoring from the cutoff forward, at roughly the same 2.5x
  rate.
- **Repair or waive the affected specs instead of a cutoff.** Rejected in §4 Migration, on measurement.
- **Fix only one reader.** The planning verb is what an unattended run consults before building a
  unit, and the hygiene gate is what holds the merge bar. Leaving either blind leaves half the rule
  unenforced.
- **Extract the predicate into a shared script both kits call.** Rejected on the install-prefix rule:
  each kit resolves its own prefix precisely so neither has to find the other.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` ·
`tools/memory-tree/check-memory-hygiene.sh` · `tools/memory-tree/check-memory-hygiene.test.sh` ·
`tools/memory-tree/marker-contract.test.sh`, EXTENDED with the shared case table, its display name
and header moving to cover two contracts ·
`memory/TEMPLATE-SPEC.md` and `tools/memory-tree/SPEC-TEMPLATE.template.md` ·
`memory/guides/BUILD-METHOD.md` and `tools/memory-tree/BUILD-METHOD.template.md` ·
`memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md` — marker-only, because the kit
version gate requires the constant present on every tracked memory-tree template and the parity test
byte-compares each against its installed copy · `.memory-tree.conf` (the new cutoff and its recorded
measurement) · `memory/guides/SESSION-KICKOFF.md` (the manifest re-stamp; the hygiene engine and the
conf are both on its watch list).

## 5. Production-readiness checklist

- security — N/A. No new input, no new write path, no new surface.
- perf / scale — the per-item walk already exists in check 12; both readers gain block extraction
  over a section that is a few dozen lines at most.
- a11y — N/A. No user-facing surface.
- i18n — N/A. The mark is a repo-internal grammar.
- error / empty / loading states — the one genuinely undecided shape is a §8 with NO items and no
  none form, reached today through the empty-first-line branch and silently resolved. §8's F1 decides
  it, and taking the refusal is the only thing in this unit that gives either gate a new `fail`
  branch.
- observability — the measurement S5 records is the observation, and it is committed beside the
  cutoff rather than run and discarded.
- risks — rev-1's risk was S5's blast radius. S6 removes it, and the residual risk moves to the
  opposite failure: a cutoff set so far ahead that the rule never binds anything. It is set to the
  landing date, which is the tightest value that grandfathers the corpus.
- testing + left-shift gates — the shared case table is the left-shift, and a future third reader of
  §8 is expected to join it rather than spell a third predicate.
- migration / rollback — no migration. Rollback is reverting both predicates and the cutoff; the
  version constant moves with them so a half-reverted tree reds rather than passing quietly.
- user docs — S4 is the doc change, in the two files authors and runs actually read.

## 6. Acceptance criteria

- **AC1** — When a spec's §8 opens with a line announcing the fork is not resolved,
  `bash tools/unattended/unattended.sh --plan <slug>` classifies it FORKED, not ready to build.
  Fixtured in `tools/unattended/unattended.test.sh` with the pre-change behaviour as the control.
- **AC2** — When a spec's §8 first line carries the none form and a LATER item is unresolved,
  `bash tools/unattended/unattended.sh --plan <slug>` classifies it FORKED. Same fixture file.
- **AC3** — When a spec dated at or after the new cutoff carries an unresolved §8 item below a
  none-form first line under a terminal status, `bash tools/memory-tree/check-memory-hygiene.sh`
  reds naming that file; when the same spec is dated before the cutoff, it is silent. Both arms in
  `tools/memory-tree/check-memory-hygiene.test.sh`.
- **AC4** — When an item's mark sits on a CONTINUATION line rather than the opening line, both
  readers treat the item as resolved. One case table drives both spellings, asserted beside
  `tools/memory-tree/marker-contract.test.sh`.
- **AC5** — When a §8 item carries the resolution word with no parenthesised attribution, both
  readers treat it as unresolved. Same case table beside `tools/memory-tree/marker-contract.test.sh`.
- **AC6** — When the corpus measurement is run, its result is recorded in `.memory-tree.conf` beside
  the new cutoff, in the shape `SPEC_WITNESS_CUTOFF`'s comment already uses.
- **AC7** — When `memory/guides/BUILD-METHOD.md` M3 is read, it describes the per-item rule and no
  longer says the gate reads the first line and nothing else, and
  `bash tools/memory-tree/kit-dogfood-parity.test.sh` is green.
- **AC8** — When a non-comment line of `tools/memory-tree/check-memory-hygiene.sh` moves,
  `bash tools/memory-tree/check-verdict-epoch.sh` and `bash tools/check-kit-versions.sh` are both
  green, which requires `KIT_MEMORY_TREE_VERSION` to move and every tracked memory-tree template's
  marker to move with it.
- **AC9** — When any NEW `fail` branch exists, it is armed in that gate's sibling test or pinned in
  `memory/project/unarmed-branches.txt` with its reason, and `python tools/memory-tree/check-arms.py
  --check` exits 0. The `ARMS_FLOORS` entries move only where `--report` shows the measured counts
  actually grew.
- **AC10** — `GATE_FULL=1 bash tools/run-gates.sh` is green.

## 7. Gates

`tools/memory-tree/check-memory-hygiene.sh` and its sibling test ·
`tools/memory-tree/check-verdict-epoch.sh` and its sibling · `tools/check-kit-versions.sh` ·
`tools/memory-tree/kit-dogfood-parity.test.sh` · `python tools/memory-tree/check-arms.py` ·
`tools/unattended/check-unattended.sh` and its two siblings ·
`tools/memory-tree/marker-contract.test.sh` · `skills/session-kickoff/manifest-check.sh` ·
`bash tools/run-gates.sh`.

## 8. Open questions

- **F1 — does a §8 with NO items and no none form refuse, or pass?** This is the shape reached
  through the empty-first-line branch and silently resolved today; it is the only genuinely
  undecided population, and it is exactly what §4's condition 1 protects. Options: refuse, which is
  this repo's stated rule about empty populations; or pass, which is a deliberate choice to keep a
  hollow section legal. **RESOLVED (owner, 2026-08-17): refuse.** Each gate therefore gains one new
  `fail` branch, each needing an armed assertion under AC9, and this is the only thing in the unit
  that could move an arms floor — so the floors are re-measured with the report mode rather than
  assumed unchanged.
- **F2 — is the attribution's DATE validated as a date, or only as a non-empty field?** Validating
  the shape costs one pattern and catches a mark whose date field holds prose. Recommendation: shape
  only, on the same grounds the acceptance-witness rule gives for checking that a bullet names
  something rather than that the thing exists.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft.
- rev-2 · 2026-08-16 · folded the M4 spec audit's first round. The predicate was specified two
  incompatible ways across §4, S3 and the acceptance criteria; §4 now states it once, with the
  section-resolution conditions ordered so the none form never suppresses the per-item walk. The item
  boundary was unstated and swung the affected population by 2.5x; §4 now defines an item as its
  opening line plus its continuation lines, and both scope items carry block extraction. The repair
  and waiver plan was unbuildable — check 12 has no waiver mechanism — and is replaced by a dated
  cutoff, which is this conf's fourth use of that pattern. The floor-raise instruction contradicted
  the green-bar criterion and is replaced by the pin-or-arm rule that actually binds. Added M3 as a
  carrier, the kit-version gate and its four marker files, the shared case table in place of a
  byte-compare, the manifest re-stamp, and the real output of the recorded reuse probe.
- rev-3 · 2026-08-16 · folded round 2. The rejection of the opening-line reading argued from specs
  going "newly red" under a unit whose own cutoff grandfathers all of them — the measurement is
  evidence about the authoring convention, and is now framed as that. The non-goal "no new gate leg"
  sat beside a files list offering a new sibling test as an alternative; the two carry different
  costs (a leg row, the run-gates canary, and a codebase-map key whose baseline is closed to new
  ones), so the extension is chosen and the alternative is priced rather than left open. S2a is new:
  the harness rev-2 cited as a precedent works by slicing a named function out of shipped bytes, and
  the hygiene predicate has no function to slice, the two readers grade disjoint status populations,
  and the cutoff makes their answers legitimately differ — so the table now carries a per-reader
  expected verdict and each side's fixture requirements.

- rev-4 · 2026-08-17 · §8 F1 RESOLVED by the owner: a §8 with no items and no none form REFUSES.
  Each gate therefore gains one new `fail` branch, which is the only thing in this unit that can move
  an arms floor, so AC9's floors are re-measured rather than assumed unchanged.
## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "decide whether a spec's open questions are resolved"`
returns neither reader. It returns the python-launcher resolvers, two codebase-map tests, a registry,
the install-prefix gate, the manifest checker, the map library, the merge skeleton and a spec parser.
The reason is recorded rather than worked around: the symbol tier of the corpus is Python-only, so a
shell function cannot appear in it at all, and a tracked backlog row already records the same
blindness for JavaScript. Rev-1 claimed this probe returned the two readers, which it does not.

The claim that there are exactly TWO readers rests instead on a grep of tracked shell and python for
the predicate, which is the evidence that actually establishes it and which the next session should
re-run rather than re-running the probe.

The seam this unit extends is `tools/memory-tree/marker-contract.test.sh`'s case-table shape — an
existing, gated arm that already drives four live readers of one marker grammar over a single table,
which is exactly the problem this unit has with two readers of another. No new seam is created.

Recall terms used, recorded for the reground: fork resolution marker attribution delegated owner
agent open questions predicate anchored substring plan_state hygiene check 12 cutoff ratchet.
