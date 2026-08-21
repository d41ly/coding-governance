# TOOL-aBoundedVerdict-4 — a fork that says it is unresolved stops reading as resolved

**Status:** CLOSED · rev-8 · 2026-08-20 · node a · Tier-2 · base 098bebd9 · streams tooling · ratified 2026-08-17

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
  whose display name and header move to cover the marker contracts it now drives rather than the one
  it was named for, not a byte-comparison of two dissimilar languages and not a new leg. **Its rows
  are keyed by CONTRACT**, because the table carries rows for more than one, and they are named:
  the §8 resolution mark across both readers (S1, S2); the fact-question prefix (S8); and the
  review-VERDICT token set `CLEAN` / `CLEAN WITH FIXES` / `BLOCKED`, whose canonical owner is this
  kit — `memory/HYGIENE.md` check 5 and `check-memory-hygiene.sh` enforce the record grammar, and
  `memory/guides/BUILD-METHOD.md` is rendered from this kit — but which the unattended kit cannot
  import, so the duplication is STATED and its drift is armed as a row here. That third row is added
  by the unit that needs it, not by this one: this unit builds the contract-keyed table, and a
  sibling contract joins it as a row instead of landing a second harness or a new leg.
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
- **S8** — **the FACT-QUESTION prefix grammar is SPELLED HERE**, because this unit owns the
  predicate that grades it and F3 bound the two marks to one place. The grammar: the literal token
  `FACT-QUESTION`, then ` · `, at the HEAD of the §8 bullet's bolded label and before the fork id —
  so a fact question reads `- **FACT-QUESTION · F1 — does X hold?**` and an ordinary fork's label is
  unchanged. The prefix is TRANSPARENT to resolution: it never marks an item resolved and never
  suppresses a resolution mark on the same item's block, so an item carrying the prefix alone is
  unresolved exactly like any other unmarked item, and one carrying the prefix AND the mark is
  resolved. Both readers of S1 and S2 recognise it, driven from S2's table by a row of its own.
  `TOOL-aBoundedVerdict-3` S4 CITES this grammar rather than restating it, so the dependency points
  forwards to the unit built earlier and there is one spelling of the token, not two.

## 3. Non-goals (OUT)

- No change to what §8 MEANS, to the resolver-authority rules, or to who may sign a resolution. This
  unit changes only how a machine recognises the mark.
- No repair of any landed spec. S6's cutoff is what makes that unnecessary, and rewriting a ratified
  record is against the memory tree's own rule.
- No new gate LEG, and S2's case table therefore EXTENDS `tools/memory-tree/marker-contract.test.sh`
  rather than landing beside it. Rev-2 offered both and they are not interchangeable: a new sibling
  is either a row in `tools/gate-legs.json` — which pulls in the run-gates canary and the
  codebase-map leg inventory, whose baseline is closed to new keys, so the key reds until a dossier
  claims it — or it is a test nothing runs. Extending needs neither. **Its cost is the display name,
  which is not spelled once.** No count is written here, because it grew twice already; the carriers
  are enumerated instead, and S2 carries every one of them: `tools/gate-legs.json` and
  `tools/memory-tree/kit.toml`, which must move in lockstep; the claiming dossier
  `memory/map/features/row-grammar.md`; and the codebase-map GENERATED artifacts
  `memory/map/generated/MAP.md` and `memory/map/generated/inventories.json`, which are re-rendered
  rather than edited, in the same commit as the claim edit. Re-derive the live carrier set with
  `grep -rn 'marker contract' tools memory/map` before touching any of them.
- No enforcement that a delegated resolution is signed as delegated rather than as the owner. The
  attribution SHAPE is checked; whether the named resolver really decided is not checkable here.
- No repair of the planning verb's other known blindness beyond what S3 incidentally closes. The
  tracked backlog row for it keeps its own disposition.

## 4. Design

### Data model

**An ITEM** is a line opening with a bullet marker or a `###` sub-head, TOGETHER WITH every following
line until the next item or the end of the section. The block reading is not a preference: the spec
template explicitly sanctions a multi-line fork, and BOTH placements occur across the tracked corpus
in comparable numbers — a large share of resolved items put the mark on an indented continuation
line, so an opening-line reading misgrades correctly-authored specs. **That categorical claim is the
argument; no ratio is written here.** Neither the "most recent closed build" appeal rev-2 made nor
the frozen per-item split rev-5 replaced it with survived four days: the first came to argue the
opposite of its own point and the second moved toward even. An argument anchored on a moving
superlative OR on a moving ratio is the same defect twice, so the figure lives only where S5 puts
it — measured at build time over `git ls-files 'memory/builds/*/spec/*.md'`, counting items whose
mark sits on the opening line against items whose mark sits on a continuation line, and recorded in
the conf beside the cutoff. Both existing readers grade one line and have no notion of an item
spanning lines, so block extraction is new work in both, and S1 and S2 each carry it.

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
| both readers, `FACT-QUESTION` prefix | no such token exists; a prefixed label would read as an unresolved fork | the token is recognised as a transparent prefix (S8) — never resolving, never suppressing a mark on the same block |
| `tools/memory-tree/marker-contract.test.sh` | one contract, one display name spelled across the carriers §3 enumerates | contract-keyed rows, the name moved in lockstep across those same carriers |
| `memory/TEMPLATE-SPEC.md` §8 guidance | prose describing the mark, and the false claim that the gate reads only §8's first non-blank line | the same prose plus the shaped mark, the per-item rule, and the S8 prefix |
| `memory/guides/BUILD-METHOD.md` M3 | states the gate reads the first line and nothing else | states the per-item rule this unit installs |

The two gates cannot share source — one is a shell gate in the unattended kit, the other in the
memory-tree kit, and neither may import the other, because the kits are independently installable
and a cross-kit import would make one a dependency of the other. So the predicate is spelled twice
on purpose, and the defence against drift is the shared case table S2 names.

### Migration

**There is none on disk, and S6 is why.** The cutoff grandfathers every landed spec by filename date,
so the tightened predicate applies to specs written after it and to nothing else. This replaces
rev-1's plan to repair or waive the affected specs, which was unbuildable in both halves: check 12
has no waiver mechanism at all — its §8 grading block reads no registry, and none of the registries
under `memory/project/` is consulted by it — and repairing a landed spec rewrites a ratified record.

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
  Rejected on the corpus: a large share of item-bearing specs put the mark on a continuation line and
  would fail the opening-line reading while being correctly authored. **No figure is written here** —
  the tracked spec population has grown twice while this spec was open, and every numeral this
  paragraph has carried went stale within days. `git ls-files 'memory/builds/*/spec/*.md' | wc -l`
  gives the population and S5's build-time run gives the split; that run is the authority, and this
  paragraph carries only the direction of the result. **It is evidence about the AUTHORING
  CONVENTION, not a prediction about this unit** — S6's cutoff grandfathers every landed spec, so
  neither reading reds anything already in the tree, and rev-2's "newly red" phrasing described an
  outcome this unit cannot produce. The convention is what matters: it is what future specs will
  follow, so opening-line grading would red correct authoring from the cutoff forward.
- **Repair or waive the affected specs instead of a cutoff.** Rejected in §4 Migration, on measurement.
- **Fix only one reader.** The planning verb is what an unattended run consults before building a
  unit, and the hygiene gate is what holds the merge bar. Leaving either blind leaves half the rule
  unenforced.
- **Extract the predicate into a shared script both kits call.** Rejected on the install-prefix rule:
  each kit resolves its own prefix precisely so neither has to find the other.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` ·
`tools/memory-tree/check-memory-hygiene.sh` · `tools/memory-tree/check-memory-hygiene.test.sh` ·
`tools/memory-tree/marker-contract.test.sh`, EXTENDED with the shared contract-keyed case table, its
display name and header moving to cover the contracts it drives ·
**the display-name carriers that must move with it** — `tools/gate-legs.json` ·
`tools/memory-tree/kit.toml` · `memory/map/features/row-grammar.md` · and the GENERATED
`memory/map/generated/MAP.md` and `memory/map/generated/inventories.json`, re-rendered in the same
commit as the dossier edit, never hand-edited ·
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
- **AC10** — `GATE_FULL=1 bash tools/run-gates/run-gates.sh` is green.
- **AC11** — When `memory/TEMPLATE-SPEC.md`'s §8 guidance is read, it states the shaped mark and the
  PER-ITEM rule and no longer says the hygiene gate reads only §8's first non-blank line, its kit
  template `tools/memory-tree/SPEC-TEMPLATE.template.md` matches it byte-for-byte, and
  `bash tools/memory-tree/kit-dogfood-parity.test.sh` is green. This is the document every future
  spec author reads, so S4 is not satisfied by M3 alone.
- **AC12** — When a §8 item's label carries the `FACT-QUESTION · ` prefix and the item's block
  carries NO resolution mark, the item is unresolved for both readers: `--plan` classifies the spec
  FORKED, and check 12 reds a terminal-status spec dated at or after the cutoff naming that file.
  Both arms driven from S2's table row for the prefix.
- **AC13** — When the same prefixed item's block ALSO carries the resolution mark, the item is
  resolved for both readers: `--plan` does not classify the spec FORKED, and check 12 is silent on
  it. Same table row; this arm is what proves the prefix does not suppress the mark, which is the
  failure F3 exists to prevent.

## 7. Gates

`tools/memory-tree/check-memory-hygiene.sh` and its sibling test ·
`tools/memory-tree/check-verdict-epoch.sh` and its sibling · `tools/check-kit-versions.sh` ·
`tools/memory-tree/kit-dogfood-parity.test.sh` · `python tools/memory-tree/check-arms.py` ·
`tools/unattended/check-unattended.sh` and its two siblings ·
`tools/memory-tree/marker-contract.test.sh` · `python tools/codebase-map/test_codebase_map.py`
(the display-name move edits a dossier and re-renders the generated map artifacts) ·
`skills/session-kickoff/manifest-check.sh` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none - every fork below is RESOLVED in place, each naming the resolver and the authority.
This line is the machine-read one; the bullets carry the reasoning.

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
  RESOLVED (agent, 2026-08-20, delegated): SHAPE only. Mechanism-only, and the grounds are the ones
  the bullet already states: this gate checks that a mark NAMES a date, not that the date is true,
  the same distinction the acceptance-witness rule draws. A validator that parses the value is a
  second answer to a question the shape already answers.

- **F3 — does the predicate recognise `TOOL-aBoundedVerdict-3`'s fact-question mark?** That unit's
  F2 resolved to a PREFIX on the fork's own bullet, which lands inside the population this unit's
  predicate grades. A prefix the predicate does not know reads as an unresolved fork and blocks the
  spec carrying it from ever going terminal.
  RESOLVED (agent, 2026-08-20, delegated): the predicate reads BOTH marks — the resolution mark it
  already grades, and the fact-question prefix — from one place, so the two units cannot drift into
  two spellings of one rule. Raised and resolved in the same sweep because it is a cross-unit
  constraint neither spec carried and both depend on.

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
- rev-5 · 2026-08-17 · M7 REGROUND onto the new merge base. Four claims moved. The appeal to "the
  most recent closed build" now argues the OPPOSITE — the newest closed build writes to the
  opening-line convention — so it is replaced by the per-item corpus split, which is the evidence
  that actually carries the point. The corpus measurement moved with 18 new tracked specs and is
  demoted to a sketch, with S5's build-time run as the authority. The marker-contract leg was RENAMED
  and its name is now spelled in four places, so the extension's cost is four-part rather than one.
  One of its four readers has had no caller since the unattended kit's 1.5.
- rev-6 · 2026-08-20 · M3 fork sweep, before any code. F2 RESOLVED as recommended, shape only.
  **F3 is NEW and is a cross-unit constraint the sweep surfaced:** `TOOL-aBoundedVerdict-3` F2
  resolved its fact-question mark to a bullet prefix, which lands inside the population this unit's
  hardened predicate grades, and neither spec said so. Both now do, and both name one predicate
  reading both marks. §8's first non-blank line is now the machine-legal `none` form — this spec of
  all of them, since it is the unit that makes that line load-bearing.
- rev-7 · 2026-08-20 · folded the second M4 spec audit
  (`reviews/2026-08-20-review-TOOL-aBoundedVerdict-1.md`): B7, H16, M9, M10, L1, plus the
  build-level decision about what the case table covers.
  **M10 — the base was wrong and the reground was overdue.** This spec alone declared `febba16b`
  while the rest of the set declared `098bebd9`, which is 209 commits later, and it is unit 4 in the
  dependency order, so it would have been built early on evidence the 08-19 re-decomposition never
  re-verified. The header now declares `098bebd9`. Two figures did not survive the move and are
  DELETED rather than refreshed: the per-item split in §4 Data model, and the "roughly 36 of 46",
  "118 to 136" and "2.5x" figures in §4 Alternatives. The split has moved toward even since rev-5
  measured it, so the moving-superlative defect rev-5 fixed had simply reappeared as a moving ratio.
  The argument is now the categorical one — both placements occur across the corpus in comparable
  numbers, so an opening-line reading misgrades correct authoring — and the figure lives only in
  S5's build-time run and the conf beside the cutoff. UNCHANGED by the reground: the two-reader
  population, check 12's total absence of a waiver mechanism, the cutoff-grandfathering argument,
  S2a's three obstacles, and every rejected alternative except the numerals inside one of them.
  **B7 — §3 priced the display-name move at four parts while Files touched named one file.** A
  builder working from that list moves the harness and leaves the name spelled elsewhere, which reds
  the leg inventory. The count is gone entirely, because it has already grown twice; the carriers are
  enumerated instead, in both §3 and Files touched — `tools/gate-legs.json`,
  `tools/memory-tree/kit.toml`, the dossier `memory/map/features/row-grammar.md`, and the two
  GENERATED map artifacts, marked re-rendered rather than edited. §7 gains
  `python tools/codebase-map/test_codebase_map.py`, the gate that actually observes the dossier claim
  and the regen.
  **H16 — the unit implemented a mark whose definition did not exist.** F3 bound the hardened
  predicate to read `TOOL-aBoundedVerdict-3`'s fact-question prefix "from one place", but no scope
  item mentioned it, no AC exercised it, and the grammar sat in a unit sequenced five later — and
  -3's F2 calls that coordination a hard constraint, because an unrecognised mark blocks the spec
  carrying it from ever going terminal. New **S8** spells the grammar here: the literal
  `FACT-QUESTION`, then ` · `, at the head of the bolded label before the fork id, transparent to
  resolution. New **AC12** and **AC13** are the pair — prefix alone, then prefix plus the resolution
  mark — with the expected verdict written per reader. -3 S4 cites this grammar rather than restating
  it, so the dependency points forwards to the unit built earlier.
  **M9 — S4 named two doc carriers and AC7 observed one.** `memory/TEMPLATE-SPEC.md` still told
  every future spec author that the mark is prose read only on §8's first non-blank line, which is
  the statement S3 falsifies. New **AC11** observes that file, its kit template and
  `kit-dogfood-parity.test.sh`.
  **The case table's rows are now CONTRACT-KEYED and the contracts are named:** the §8 resolution
  mark, the S8 prefix, and the review-VERDICT token set, whose canonical owner is this kit —
  `memory/HYGIENE.md` check 5 plus the hygiene engine, with `BUILD-METHOD.md` rendered from the same
  kit — and which the unattended kit cannot import, so the duplication is stated and armed here
  rather than left to drift. This unit builds the keying and does NOT add that third row: it touches
  no verdict vocabulary, and adding another unit's row is the scope widening the alternative offered.
  One harness, no new leg either way.
  **L1** — "none of the six registries under `memory/project/`" became "none of the registries";
  there are seven, the count was never load-bearing, and check 12 consults none of them regardless.

- rev-8 · 2026-08-20 · **built. Six things the building settled, three of them measurements this
  spec could not have carried.**
  **(1) S2a's open choice is TAKEN: the hygiene side is driven through a fixture repo, not by lifting
  its predicate into a sliceable function.** The alternative restructures a thousand-line single-quoted
  awk program to make a test convenient, and the risk of that lands on every other check in the same
  pass. The fixture-repo route is what this kit's own sibling test already does, and the conformance
  table writes each case TWICE — once terminal for the hygiene reader, once live for the planning
  verb — because the two readers grade disjoint status populations and no single document can be
  graded by both. That is why the table carries a per-reader verdict rather than one shared answer.
  **(2) The failing case was observed over the real corpus, and it is the number S6 exists for.** With
  `FORK_MARK_CUTOFF` set retroactively to 2026-01-01, check 12 reds **33 TERMINAL specs**. Repairing a
  ratified record is forbidden, so the cutoff carries the landed corpus instead — set to 2026-08-21,
  strictly ahead of the newest tracked spec filename date, which is 2026-08-20 because another node
  landed a spec today. The S5 measurement recorded in the conf beside it: 211 spec files carrying a
  section 8, 339 items, 246 conforming marks, 93 non-conforming across 38 files, with `builder`,
  `build` and `unattended build` among the resolver names in the wild.
  **(3) Two escape levels, and the first one cost a cycle.** The mark was first handed to awk with
  `-v mark=...`; awk processes escape sequences in a -v ASSIGNMENT, so `\(` arrived as a bare `(`,
  the pattern became a GROUP instead of a literal paren, it matched nothing, and every spec in the
  live build classified FORKED. It is spelled as a `/.../` literal now, which has no escape level to
  lose — and which also keeps `plan_state` SLICEABLE, since the conformance harness lifts that body
  out of the shipped bytes and a constant defined outside it would arrive empty. Then the second: an
  apostrophe in a comment inside the hygiene engine's single-quoted awk program closed the string and
  broke the shell parse. Neither is in this spec's Alternatives; both are in the code comments where
  the next editor stands.
  **(4) A fixture had to move, and saying which one matters.** `tFixture-61` exists to prove that a
  resolved fork on Tier-1 is as green as on Tier-2 — the TIER is its subject — and its mark was the
  bare word. Under the shaped grammar it was about to start testing mark shape by accident, so it now
  carries the documented attribution and keeps testing the tier. `tFixture-60` and `-63` are dated
  past the fixture cutoff and now carry the per-item message while `-44` and `-46`, dated before it,
  keep the loose wording. Those four ARE the cutoff-boundary arm: same defect, two eras, two
  messages, which is what proves the gate is dated rather than merely strict.
  **(5) The memory-tree version is SEVEN sites across seven files**, not the engine constant alone:
  the constant and its same-line marker in the engine, the marker in each of three shipped templates,
  and the marker in each of three INSTALLED halves, which the dogfood-parity leg byte-compares against
  those templates. Same shape as the sixth carrier `TOOL-aBoundedVerdict-13` found one kit over, and
  found the same way — by moving the shipped side and watching a parity gate red.
  **(6) The leg's display name is now plural and its header names both contracts.** The harness drove
  one contract and was named for it; it drives two. The rename touches the five carriers section 3
  enumerates, and the claiming dossier moves with them so the map's coverage assert stays balanced —
  the old inventory key disappears and the new one has to be claimed in the same commit.
  **The predicate was run over the real tree before it was wired**, per the merge-bar rule: on the
  live build it classifies all nine open units READY, identically to the loose reader, which is both
  the near-miss check and independent confirmation that this build's own fork sweep produced
  conforming marks.

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
existing, gated arm that already drives every reader of one marker grammar over a single table,
including one retained deliberately with no caller since the unattended kit's 1.5 — which is exactly
the problem this unit has with two readers of another. The harness prints the case × reader count it
actually ran, so no count of its readers is written here. No new seam is created.

Recall terms used, recorded for the reground: fork resolution marker attribution delegated owner
agent open questions predicate anchored substring plan_state hygiene check 12 cutoff ratchet.
