# TOOL-aDrainedSluice-1 — drain the tooling backlog to zero

**Status:** CLOSED · rev-2 · 2026-08-08 · node a · Tier-2 · base 76fcd09b · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-08-review-TOOL-aBatchedTribunal-1-3.md](../reviews/2026-08-08-review-TOOL-aBatchedTribunal-1-3.md) | diff-review | TOOL-aDrainedSluice-2 TOOL-aDrainedSluice-3 TOOL-aDrainedSluice-4 TOOL-aDrainedSluice-5 TOOL-aDrainedSluice-6 TOOL-aDrainedSluice-7 TOOL-aDrainedSluice-8 TOOL-aDrainedSluice-9 TOOL-aBatchedTribunal-1 TOOL-aBatchedTribunal-6 TOOL-aBatchedTribunal-8 |

<!-- /gen:spec-records -->

## 1. Goal

Resolve every OPEN and DEFERRED row in `memory/backlog/TOOL.md`: build the fix, or close the row
WONTDO with the reason and its successor. A backlog that only grows is a list nobody reads, and four
of these rows are gaps in gates this repo relies on.

## 2. Scope (IN)

- **S1** — V1 drains `TOOL-aFoldedQuarry-8`: `check-arms.py` DISCOVERS its gate/test pairs instead of
  naming one. Measured: `skills/session-kickoff/manifest-check.sh` carries 16 `fail` calls behind six
  numbers and is entirely uncovered today.
- **S2** — V3 drains `TOOL-aRuledParchment-2`: hygiene check 5 governs recording files at ANY depth
  under the four subfolders, not only direct children. Measured: the nested population is currently
  six conforming files, so the ratchet arms clean.
- **S3** — V4 drains `TOOL-aBatchedLintel-2`: the §9 rev high-water scan gains a section reset, so a
  heading after §9 stops inflating it. This is a VERDICT change and ships with its own fixture.
- **S4** — V2 drains `TOOL-aFoldedQuarry-7`: every branch pinned in
  `memory/project/unarmed-branches.txt` gains a fixture that trips it and a POSITIVE assertion naming
  its own failure text. The pin ends empty or holds only branches with a written reason.
- **S5** — V5 drains `TOOL-aQuarriedLantern-2`: one python resolver that EXECUTES its candidate,
  shared by every site. Measured: six sites, five using the `command -v` idiom the MS-Store stub
  satisfies while exiting 9009.
- **S6** — V6 drains `TOOL-aQuarriedLantern-3`: the memory-recall cache gains a per-worktree byte cap
  and LRU eviction on `built_at`. Measured here at 1.9 MB, so the cap ships for adopters rather than
  for this repo.
- **S7** — V7 drains `TOOL-aFoldedQuarry-3`, `-4` and `-5`: the JavaScript gates see untracked files,
  `check-wiring.sh` self-heals a CRLF rendered Skill, and `hygiene-parity.test.sh` refuses a baseline
  older than the flatten.
- **S8** — V8 drains `TOOL-aFoldedQuarry-6`: the dead-path census. Measured 26 `(file, dead path)`
  pairs, of which four sit in the LIVE ledger and are invisible to check 15 because they are
  DIRECTORY citations and the harvest requires a file extension.
- **S9** — V9 closes `TOOL-bThriftyBellows-2` WONTDO: it is a performance idea for
  `gen-memory-tree.sh`, which was deleted with the authored tree index.
- **S10** — `memory/backlog/TOOL.md` ends this build with every row CLOSED or WONTDO, each carrying
  the id that resolved it.

## 3. Non-goals (OUT)

- The other three backlogs. `PLAY`, `KICK` and `DEPL` rows are out of scope; this build drains
  `TOOL` and says so.
- Retro-fitting the new checks over the frozen build records. A record of a moment is not a claim
  about now, and V8 states that boundary rather than eroding it.
- Rewriting any ratified id or renumbering a landed record.
- A second review harness, a second gate runner, or a second conf. Every unit wires through the seam
  that already exists.

## 4. Design

### Data model

Nothing new is invented. Each unit either widens an existing population, converges duplicated logic
onto one owner, or supplies a fixture for a branch that had none:

| Kind of change | Units |
|---|---|
| widen a population that was too narrow | V1, V3, V8, V7's untracked-files item |
| converge two or more copies onto one owner | V5 |
| supply the missing fixture and arm | V2, V4 |
| bound an unbounded resource | V6 |
| refuse an input that cannot mean what it claims | V7's parity-baseline item |

### Inventory

| Artifact | Units |
|---|---|
| `tools/memory-tree/check-arms.py` | V1, V2 |
| `tools/memory-tree/check-memory-hygiene.sh` + its test | V3, V4, V2 |
| `skills/session-kickoff/manifest-check.test.sh` | V1, V2 |
| `tools/memory-tree/corpus_ids.py` | V8 |
| `tools/memory-recall/` | V6 |
| `tools/lib/` or an equivalent shared home | V5 |
| `tools/check-wiring.sh`, `tools/workflows/check-*.sh`, `hygiene-parity.test.sh` | V7 |

### Migration

None. Every change is additive to a gate or a resolver; no tracked content moves.

### Rollout

One commit per unit, each closing with the full bar green. V1, V3 and V4 land before V2 because each
changes the branch set V2 arms.

### Files touched (estimate)

Roughly a dozen kit files, two test harnesses, the conf, and the backlog.

### Alternatives rejected

- **Close the rows as WONTDO and move on.** Rejected for all but one: four of them are gaps in gates
  the repo relies on, and a gap recorded but not closed is the vacuity this kit exists to remove.
- **One commit for the whole backlog.** Rejected: a unit whose bar is green is a unit that can be
  reverted alone.

## 5. Production-readiness checklist

- security — N/A across every unit; these are gates and resolvers over tracked text.
- perf / scale — V1 widens a source scan to a second file pair; V3 widens a path selector. Both are
  linear and small. V6 makes an unbounded cache bounded, which is a perf improvement.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — every widened population keeps the kit's empty-population
  discipline: a selector that matches nothing on a tree that has files of that kind is a failure.
- observability — each unit's failure names the file, the line and the rule.
- risks — V4 is a deliberate VERDICT change and could red a landed spec; the measurement decides,
  and the fixture pins both directions. V5 touches every python-invoking script at once.
- testing + left-shift gates — every unit adds or extends a self-test arm.
- migration / rollback — one commit per unit.
- user docs — `HYGIENE.template.md`, the kit READMEs and `AGENTS.md` follow each unit.

## 6. Acceptance criteria

- **AC1** — When `bash tools/run-gates.sh` runs at the end of this build, every leg is green.
- **AC2** — When `memory/backlog/TOOL.md` is read at the end, no row carries OPEN or DEFERRED.
- **AC3** — When `check-arms.py --report` runs, it covers every gate that has `fail` branches, and
  the pin holds only branches with a written reason.
- **AC4** — When a free-named file is added under a nested `spec/<sub>/`, check 5 fails naming it.
- **AC5** — When a spec carries a heading after §9, the rev high-water is unaffected.
- **AC6** — When a python-invoking script meets a launcher that answers `command -v` and then fails
  to run, the resolver rejects it and names the next candidate.
- **AC7** — When the recall cache exceeds its cap, the least recently built entries are evicted and
  the eviction is reported.
- **AC8** — When a DIRECTORY citation in the present-tense corpus resolves to nothing, check 15
  fails naming it.

## 7. Gates

`bash tools/run-gates.sh` in full at every unit boundary, plus
`python tools/memory-tree/gotchas.py --for-diff <base>..<head>` before each review.

## 8. Open questions

none — the two forks below are RESOLVED (owner-ratified 2026-08-08); kept for the record.

- **Fork A — where the shared python resolver lives.** Options: a new `tools/lib/` shared by every
  kit, or one kit owns it and the others ask. RESOLVED (owner, 2026-08-08): a new shared home. The
  kits are independently deployable, so "one kit owns it" makes every other kit depend on that kit;
  a tiny shared file each kit copies is the same shape the conf parser already has.
- **Fork B — what happens to the four dead ledger citations V8 surfaces.** Options: register them in
  the dead-path registry, or repair them. RESOLVED (owner, 2026-08-08): REPAIR. The ledger is live
  navigation in the present-tense corpus, not a frozen record; the registry exists for citations that
  cannot legally be edited.

## 9. Revision log

- rev-2 · 2026-08-08 · CLOSED. All nine units landed, `memory/backlog/TOOL.md` holds no OPEN or
  DEFERRED row, and the bar went 30 -> 32 legs (the python resolver's self-test is new; the gotchas
  leg stopped skipping). Nothing was re-scoped to make it close: eleven rows CLOSED against a landed
  change and one — the single-pass generator — WONTDO because U2 had already deleted its subject.
  Four drafted premises did not survive measurement and are corrected in their own units rather than
  quietly dropped: V2's batching rule and perf figures (an upstream tree's numbers), V5's inventory
  (three idiom sites in one file, not two) and its sourcing list, V7's CRLF bound and its
  `git checkout` claim, V8's registry-versus-repair choice. Each correction is written where the
  claim was, so the next reader meets the fix and not the draft.
- rev-1 · 2026-08-08 · initial draft, written after measuring every row.

## 10. Reuse audit

Every unit is a change to something that exists. V1 widens `check-arms.py`'s population using the
same discovery-over-enumeration rule the build index already follows. V3 and V4 edit two selectors
inside `check-memory-hygiene.sh` and ride its `fail` protocol. V2 writes fixtures into the two test
harnesses that already exist, in their existing batched shape. V5 converges six copies onto one file
rather than adding a seventh. V6 extends `tools/memory-recall/`'s existing cache directory handling.
V7 touches three existing gates. V8 widens `corpus_ids.py`'s existing harvest. Nothing new is
scaffolded, and the one genuinely new artifact — the shared python resolver — exists to DELETE five
copies, not to add a sixth.
