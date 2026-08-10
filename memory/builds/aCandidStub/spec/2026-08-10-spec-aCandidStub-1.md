# PLAY-aCandidStub-1 — the playbook reconverges on the repo it governs

**Status:** INPROGRESS · rev-2 · 2026-08-10 · node a · Tier-2 · base e7ec3365 · streams playbook+tooling · ratified 2026-08-10

## 1. Goal

Close the fifteen confirmed convergence defects between the three shipped
`parallel-coding-governance*.md` files and the repo they govern, so an adopting agent following the
deploy chain lands a complete, self-consistent playbook instead of one that ships a single file,
prescribes a script the enforcement hook denies, and hands out a pre-flatten memory tree.

## 2. Scope (IN)

Every item below is a defect CONFIRMED by an adversarial skeptic in review `aCandidStub-1`
(`reviews/2026-08-10-review-aCandidStub-1.md`); the id in brackets is that review's finding id.

- **S1 — the deploy chain learns the companion exists.** `parallel-coding-governance.customize.md`
  names `parallel-coding-governance.domain-rules.md` zero times today, so its fill-and-verify
  procedure ships one file and greps one file, while 13 of the 36 placeholders it catalogues live
  only in the companion [23, blocker]. Rewrite the Who/how step to fill BOTH files, place the
  companion beside the playbook, and run the `grep -nE '\{\{[A-Z]'` verification over both. Split the
  placeholder catalogue into a template group and a companion group.
- **S2 — §8 stops prescribing a denied script.** Template `:146` names only the
  `gov:bounded-fanout` marker and never `gov:fixed-verifiers` nor the two accepted receiver shapes,
  so a script written exactly to that line exits 2 under `tools/hooks/agent-cap.js` [28, blocker].
  Spell the second marker and both shapes, and correct "DENIES raw-primitive scripts" to also cover
  an `agent()` fanned over a receiver the hook cannot prove bounded.
- **S3 — the adoption path stops handing out a pre-flatten conf.**
  `tools/memory-tree/.memory-tree.conf.example` is what `adopt-memory-tree.sh --scaffold` copies into
  a fresh repo, and its comments still define `DISCIPLINES` as folders each carrying `TREE.md`, ship
  inCMS's five discipline names, document build folders under a dated, family-qualified path
  (`builds/<date>-<FAMILY>-<slug>/`), claim nine canonical spec sections against ten, and name
  `gen-memory-tree.sh`, deleted in U2. It ships 4 of the 15 conf keys the kit reads [16, CORRECTED to
  medium — see §9 rev-2: the scaffolder ignores these comments and builds the correct flat tree, so
  the defect misinforms the adopter the script tells to EDIT IT, and does NOT red the gate].
  Re-render it to the flat shape with all 15 keys. Correct
  `customize.md:27`'s description of `{{MEMORY_DISCIPLINES}}` to match the conf's own words, a closed
  enum of stream values with `FAMILIES` as a separate key [7, high], and spell the adopter-side
  invocation path the kit's own usage string uses [21, medium].
- **S4 — companion routing and self-description agree.** Route the orphaned companion §14 or
  renumber it away from its collision with the template's own §14 [2, high]. Reconcile the companion
  header's "All are droppable-per-project" against `customize.md`'s four-section drop list closing
  with "Everything else is universal core" [24, high]. Correct the template header's section count
  [3, medium] and the companion header's own count and enumeration [4, medium].
- **S5 — the load-bearing summary stops contradicting its own section.** Template `:19` (§0 TL;DR)
  still prescribes memory as "per-node files"; `:99` (§5) now says "never a per-node shard" and the
  v2.4 header note calls the sharded ledger RETIRED [15, high]. Re-word §0 to the v2.4 rule.
- **S6 — the remaining stale facts.** The dead `memory/playbook/archive/` snapshot path [5, medium];
  "the two §5 memory-tree lines" against a §5 carrying one [6, low]; the conditional-drop entries
  still targeting multi-bullet bodies that v2.3 externalized [26, medium]; the companion's absent
  version marker and absent re-pull step [25, high]; and `~19 classes` against 25 bullets [8, low].

## 3. Non-goals (OUT)

- **Retiring companion §10 into `memory/gotchas/`.** The premise this unit was commissioned on did
  not survive the audit — see §8, fork 1. No content moves between the two corpora.
- **The two agent-cap defects this unit's reproduction surfaced.** An identifier bound from an EMPTY
  array literal is blessed as bounded and never re-examined when a later statement grows it, so
  `const batches = []` plus `batches.push(f)` per finding passes both the hook and the merge-bar leg
  while spawning one agent per item. Reproduced at exit 0 against
  `tools/hooks/agent-cap.js:171-181`, which already guards the `[].concat(x)` spelling of the same
  hole. Files as its own `TOOL-` unit; it is a kit defect, not a playbook one, and it is adjacent to
  the OPEN `TOOL-aNumeralWarden-2`.
- **The catalogue's missing adopter on-ramp.** `adopt-memory-tree.sh` scaffolds `project/ builds/
  backlog/` and not `gotchas/`, and `gotchas.py`'s `do_check` short-circuits on an empty record set,
  so a freshly scaffolded repo gets checks 17-19 passing over zero records and no catalogue. This is
  this repo's own `vacuous-selector-empty-population` class inside the kit that documents it. Its own
  `TOOL-` unit.
- **Raising the 32 KiB template gate.** The limit is not the variable; see §4 Rollout.
- **Re-numbering the template's own sections.** Every §-number an adopter's filled copy already
  carries stays stable; only the companion's §14 is in play, and only under fork 2.

## 4. Design

### Inventory

| Axis | Findings | Files touched | Size-gated |
|---|---|---|---|
| A — deploy chain | 23, 25, 26, 5, 6 | `customize.md` | no |
| B — §8 vs the hook | 28 | `template.md` | yes |
| C — adoption path | 7, 16, 21 | `customize.md`, `tools/memory-tree/.memory-tree.conf.example` | no |
| D — routing | 2, 24, 3, 4 | `template.md`, `domain-rules.md` | partly |
| E — superseded rule | 15 | `template.md` | yes |
| §10 | 8 | `template.md` | yes |

### Data model

S2's replacement text is not prose to be paraphrased. `agent-cap.js` accepts exactly two receiver
shapes on a line carrying `// gov:fixed-verifiers` — `chunk(x, Math.ceil(x.length / K))` and
`splitInto(x, K)`, with `K` an integer literal at most 5 or an identifier bound in the file to one —
plus, unmarked, an identifier assigned once from an array literal of at most 6 elements. §8 must
spell those tokens verbatim, because the marker is a claim and the gate checks the claim's SHAPE.

S3's re-render must state, in the conf example's own comments, the three facts the current file
denies: the tree is flat, the discipline is a closed enum declared in each spec's status header, and
a build folder is `builds/<slug>/`. It must also carry the conf keys the gate needs armed —
`SPEC_FORMAT_CUTOFF`, `STREAMS_CUTOFF`, `UNIVERSAL_BUDGET`, and the pins that are MEASURED per
corpus rather than inherited.

### Migration

None. All six scope items are edits to shipped documentation and one kit example file; no
instantiated adopter copy is rewritten by this unit, and the re-pull mechanism S6 repairs is how an
adopter picks the change up.

### Rollout

The template is at 32083 / 32768 bytes, 685 free, measured by `bash tools/check-template-size.sh` —
read that number from the gate, never from here. Template-side edits are S2 (~200 B, the expensive
one), S5 (~+25 B), S4's header set (~0 B), S6's count fix (−1 B), and S4's §14 stub if fork 2 resolves
that way (~150 B). The total lands near 400 B of 685. If the margin closes, the cheapest
externalization is template `:167`, whose 485 B of inlined LF and `git -C` rules are already
duplicated in companion §11 — moving them out funds every remaining fix twice over. Raising the
limit is not an option the gate's own header permits.

### Files touched (estimate)

`parallel-coding-governance.template.md` · `parallel-coding-governance.customize.md` ·
`parallel-coding-governance.domain-rules.md` · `tools/memory-tree/.memory-tree.conf.example` · the
new gate leg's script and its self-test · `tools/gate-legs.json` · `AGENTS.md` gate-suite list.

### Alternatives rejected

Fixing only the two blockers and filing the other thirteen. Rejected: eleven of the fifteen are
single-line edits in files that carry no size gate, and the audit that found them cost 1.19 M
subagent tokens. Deferring them re-buys that cost later.

## 5. Production-readiness checklist

- security — N/A. No write path, auth surface, or egress path is touched.
- perf / scale — N/A. Documentation edits plus one gate leg measured in milliseconds.
- a11y — N/A. No UI.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — the new cross-reference gate must red on an EMPTY stub set rather
  than pass, per `memory/gotchas/vacuous-selector-empty-population.md`.
- observability — the gate leg prints the orphaned section by name, not a bare exit code.
- risks — the §8 rewrite is the one item that can make things worse: text that misstates the
  accepted shapes is worse than text that omits them, because it reads as authoritative. AC2 gates
  it on the hook itself rather than on review.
- testing + left-shift gates — see §7; the stub/orphan check is the highest-value new leg.
- migration / rollback — every change is a documentation revert; no state moves.
- user docs — `AGENTS.md`'s gate-suite list gains the new leg; `WIRE-INTO-PROJECT.md` §2 gains the
  companion in the deploy step if S1 resolves that way.

## 6. Acceptance criteria

- **AC1** — When `grep -c 'domain-rules' parallel-coding-governance.customize.md` runs, it returns
  non-zero, and the file's verification step names both deployed files. Today it returns 0.
- **AC2** — When a workflow script written to the letter of the revised §8 is piped through
  `node tools/hooks/agent-cap.js`, it exits 0. The same script written to today's §8 exits 2 with
  "agent() fanned over `batches`, which this file does not show to be bounded" — both halves are
  observed, so the test is not vacuous.
- **AC3** — When `adopt-memory-tree.sh --scaffold` runs into a scratch repo and
  `check-memory-hygiene.sh` runs against the result, the gate exits 0 AND every conf key the kit
  reads is present in the copied example. The gate half is a CONTROL, not the proof: the pre-fix
  example also exits 0, measured, so the deliverable is the conf's correctness as documentation, and
  the key-coverage half is what actually moves.
- **AC4** — When the new cross-reference gate runs over the two playbook files, it exits 0; when a
  companion `##` section is added with no template stub routing to it, the gate exits non-zero and
  names that section. Both arms are fixtured.
- **AC5** — When `bash tools/check-template-size.sh` runs after the template edits, it exits 0 and
  reports a byte count at or below 32768.
- **AC6** — When the template header's section claim, the companion header's claim, and
  `grep -c '^## ' parallel-coding-governance.domain-rules.md` are compared, all three agree.
- **AC7** — When `bash tools/run-gates.sh` runs at the push boundary, every leg is green, including
  the new one.

## 7. Gates

Standing legs this unit must keep green: `tools/memory-tree/check-memory-hygiene.sh` ·
`skills/session-kickoff/manifest-check.sh` · `tools/check-template-size.sh` ·
`tools/check-kit-versions.sh` · `tools/memory-tree/kit-dogfood-parity.test.sh` ·
`tools/workflows/check-verifier-fanout.sh` · `tools/run-gates.test.sh`.

New leg this unit adds: a playbook cross-reference check, registered in `tools/gate-legs.json`. It
asserts that every `##` section in `parallel-coding-governance.domain-rules.md` is routed to by a
template stub, that the two headers' section claims match the derived count, and that every repo path
cited in the three files resolves under `git ls-files`. It ships with a self-test carrying a RED
fixture per arm, because a gate whose failing case has never been observed is an assertion about
nothing (companion §14, the section this unit un-orphans).

## 8. Open questions

### Fork 1 — the §10 retirement the unit was commissioned to design

The kickoff answer was "retire the static checklist into the catalogue: the 25 rows become
gotchas-shaped records the memory-tree kit ships as a seed corpus". The audit refuted the premise on
three independent grounds. First, `template.md:104` marks the whole memory-tree kit Optional, and a
universal §1-DoD/§7 rule cannot route to an optional kit's directory. Second, the separation is
chartered, not accidental: `memory/builds/aFoldedQuarry/spec/units/2026-08-08-spec-aFoldedQuarry-6-u4-gotchas.md`
§2 S8 says the catalogue "starts from THIS repo's own failure history" and that inCMS's records "are
not ported: they are its history, and here they would be anchors that match nothing", and its §3
Non-goals rejects wiring `--for-diff` into the review harness outright. Third, the mechanism forbids
it: anchors are DERIVED from backtick-quoted path-like tokens in a record body, so 25 product-generic
rows would derive zero anchors and red under check 19, and marking them `universal` instead would
blow `UNIVERSAL_BUDGET` (3, measured) and put 25 always-emitted rows on every checklist — the
"checklist nobody can finish" the kit exists to prevent.

**Recommendation: drop the retirement.** Keep the two corpora disjoint, fix the `~19` count, and add
one clause to §10 stating the relationship so the next reader does not re-open this. If the owner
still wants a shipped seed corpus, the seam is the existing `KINDS` enum — a non-`class` kind is
already exempt from checks 18 and 19 and already excluded from `--for-diff` — but that is a `TOOL-`
unit against the kit, not a playbook change, and it should be specced on its own merits.

**RESOLVED (owner, 2026-08-10): the memory-tree kit is MANDATORY, and the retirement is dropped.**
Making the kit required removes ground 1 outright — a universal rule may now name `{{MEMORY_ROOT}}`,
which is why §5's bullet reads "Required" and the customize companion no longer lists the kit as
droppable. Grounds 2 and 3 are untouched by that decision and remain fatal to the retirement: the
charter is ratified and derived anchors are a property of the mechanism, not of the kit's optional
status. The relationship clause is therefore the right shape, and it is now affordable to state
positively rather than defensively, because every adopter has the catalogue.

### Fork 2 — how the orphaned companion §14 is repaired

Adding a template §14 stub costs roughly 150 B against a 685 B margin and leaves two differently
titled §14s in the pair. Renumbering the companion section to §15 costs 0 B in the template but
breaks any adopter copy that already cites it. **Recommendation: renumber to §15 and route to it**,
because the companion is younger than the template and no instantiated copy is known to cite it —
verify that before landing.

### Fork 3 — whether the droppable set is widened or narrowed

S4 requires the two files to name one droppable set. Narrowing the companion's claim to §4, §9, §11
and §13 matches `customize.md` as written; widening `customize.md` to admit §8, §10, §12 and §14
matches the companion as written. **Recommendation: narrow the companion's claim.** §10 and §12
carry rules §1 and §7 reference unconditionally, so they are not in fact droppable.

## 9. Revision log

- rev-1 · 2026-08-10 · initial draft, written from review `aCandidStub-1` (workflow
  `wf_e8863e8c-821`, 34 raw findings, 15 confirmed, precision 0.44) plus two defects found while
  reproducing finding 28.
- rev-2 · 2026-08-10 · owner made the memory-tree kit MANDATORY and directed the blockers built.
  Fork 1 RESOLVED against the retirement, which the mandatory decision does not revive. S1, S2 and
  S3 are BUILT at template v2.5; S4 is partly built (the companion's count, droppable set and version
  marker) with its routing half still open as fork 2; S5 and the rest of S6 remain specced. Finding
  16's severity is CORRECTED from high to medium: the spec asserted a freshly scaffolded repo reds
  the gate, and scaffolding one proved otherwise — both the pre-fix and post-fix example confs exit 0
  and produce the same flat tree, because the scaffolder reads `DISCIPLINES` as an enum and never
  consults the stale comments. The defect is real but it misinforms rather than breaks, and the claim
  was confirmed by a skeptic who read the comments against the checks without running the scaffolder.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "ship a seed corpus of recurring bug-class records to an
adopting repo"` returned `records` in `tools/memory-tree/gotchas.py` at fan-in 8 as the top seam,
which is what fork 1's fallback would wire through. For the new gate leg in §7, the seam is the
existing gate-leg pattern rather than a new harness: `tools/gate-legs.json` single-sources the leg
list and `tools/run-gates.test.sh` asserts `run-gates.sh` hardcodes no leg command, so a new leg is
registered, not wired. The dead-path arm reuses the resolution rule already implemented in
`tools/memory-tree/corpus_ids.py` — `git ls-files` membership plus a prefix scan, never a filesystem
probe, so a checkout location classifies identically on every node. No existing check covers the
stub/orphan arm; that one is genuinely new.
