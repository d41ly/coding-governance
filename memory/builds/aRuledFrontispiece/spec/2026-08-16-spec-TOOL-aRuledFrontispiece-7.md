# TOOL-aRuledFrontispiece-7 — the STATUS.md slot is retired

**Status:** OPEN · rev-1 · 2026-08-16 · node a · Tier-1 · base 96141aed · streams tooling

## 1. Goal

Delete the `STATUS.md` slot from the build-folder contract and from every place that documents,
selects or emits it, in one commit, so nothing in the tree describes a file the tree does not hold.

## 2. Scope (IN)

- **S1** — delete `memory/builds/aPrunedCeremony/STATUS.md`. Verified: it is the only instance under
  `memory/builds/`.
- **S2** — `tools/memory-tree/check-memory-hygiene.sh:284` drops `k=="F:STATUS.md"` from check 4's
  build-folder allowlist. The comment above it, at lines 261-266, stops calling `RUN.md` the THIRD
  whitelisted root file and stops explaining an exclusion from a check whose remaining population is
  `backlog/` alone.
- **S3** — `index_set()` at `check-memory-hygiene.sh:331` drops its `builds/*/STATUS.md` member, so
  checks 6 and 7 stop selecting a class that no longer exists.
- **S4** — check 8 sheds its second population: the `pop8` selector at `check-memory-hygiene.sh:430`,
  the `pop_guard` label at :431, and the `files8` selector at :432 each drop their `STATUS.md` half;
  the precondition `PRE_STATUSY` at :134 drops its `/STATUS\.md$` alternative; the check's header
  comment at :422 and its failure text at :456 stop naming STATUS.
- **S5** — `tools/memory-tree/check-memory-hygiene.test.sh:470` asserts check 8's failure text
  VERBATIM. Verified by reading both sites: the arm and the message are the only two occurrences of
  that string in the repo, and they move in the same commit or the self-test leg reds.
- **S6** — `tools/memory-tree/HYGIENE.template.md` drops the slot at lines 31, 40, 60, 72, 74, 115
  and 138. `memory/HYGIENE.md` is then re-rendered by
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render` and never hand-edited: that harness
  byte-pairs the two after substituting this install's prefix, and its declared direction is template
  to live copy.
- **S7** — `tools/memory-tree/adopt-memory-tree.sh:95` drops the slot from the `builds/` line it
  EMITS into an adopting repo's root index, and `memory/README.md:19` — the line that script emitted
  here — drops it too. Neither copy is byte-compared against the other, so both move together or the
  kit ships an adopter a shape this repo no longer has.
- **S8** — `.gitattributes:32` stops naming a build `STATUS.md` as its example of a file that joins
  the derived index set with no edit there. `RUN.md` is the live example.

## 3. Non-goals (OUT)

- Renaming the `memory hygiene (20 checks)` gate leg. Check 8 survives on `backlog/<FAMILY>.md`, the
  check count does not move, and `memory/map/baseline.toml` is untouched. That is what keeps this
  unit off the shrink-only-rename problem unit 6 prices.
- Changing the status vocabulary. The seven tokens stay exactly as they are; only one of check 8's
  two populations goes.
- Touching `RUN.md` or its four membership decisions. Fork 7 owns the run-state files.
- Draining `curation-debt.txt` or any other waiver registry.
- Any `LIVE.md` or ledger change. Fork 8 resolved those to no change.
- Rewriting the specs, reviews and build records that mention `STATUS.md` in the past tense. They
  record what was true when they were written, and the tree is append-only about that.

## 4. Design

### Inventory

Every site, verified against source at writing time. The commit is atomic because six of these are
pairs: a rule and its enforcement, a template and its render, an emitter and what it emitted.

| Site | What changes | Why it cannot wait |
|---|---|---|
| `memory/builds/aPrunedCeremony/STATUS.md` | deleted | the only instance |
| `check-memory-hygiene.sh:284` | check 4's allowlist | otherwise the shape rule still admits the file |
| `check-memory-hygiene.sh:261-266` | the RUN.md comment above it | it counts the whitelist and explains check 8's exclusion |
| `check-memory-hygiene.sh:331` | `index_set()` member | a selector over an extinct class |
| `check-memory-hygiene.sh:134` | `PRE_STATUSY` precondition | it would still answer "a file of that kind exists" |
| `check-memory-hygiene.sh:422,430,431,432,456` | check 8's comment, both selectors, its guard label and its failure text | the message is asserted verbatim elsewhere |
| `check-memory-hygiene.test.sh:470` | the check-8 arm | it pins the failure text byte for byte |
| `tools/memory-tree/HYGIENE.template.md:31,40,60,72,74,115,138` | the shipped rule set | it is what an adopter installs |
| `memory/HYGIENE.md` | re-rendered, not edited | `kit-dogfood-parity.test.sh` byte-pairs it |
| `tools/memory-tree/adopt-memory-tree.sh:95` | the emitted `builds/` line | it writes the next adopter's root index |
| `memory/README.md:19` | the same line, live | this repo's own copy of that emission |
| `.gitattributes:32` | the comment's example | a comment naming a retired class |

Two of those sites are not in the enumeration this unit was handed and are added here rather than
discovered during the build. `PRE_STATUSY` at line 134 is check 8's PRECONDITION, and it is
deliberately un-segmented — it asks what KIND of file exists, never where. Left carrying
`/STATUS\.md$`, it would keep answering yes for a stray file the check no longer selects, which is
precisely the shape `pop_guard` exists to red on. And the `pop_guard` label at line 431 spells the
population in prose the operator reads on failure, so it drifts the moment the selector above it
does.

### Migration

One file, and its state is the argument for the deletion rather than an aside. Verified:
`memory/builds/aPrunedCeremony/STATUS.md` line 1 reads `STATUS: IN-PROGRESS`, while the generated
region of the same build's `README.md` at line 115 reads `CLOSED · 6 unit(s)`. Its constraints
section still pins the template gate at 32 KiB, a ceiling the repo moved to 48 KiB. The authored half
rotted and the derived half did not, in the single file the slot exists for. `TOOL-aUnmannedHelm-1`
recorded that same contradiction as the argument for the mechanical split it built; this unit
finishes the move by removing the authored half that lost.

Nothing else reads the file. Verified by a repo-wide search: no gate, hook, skill, workflow script or
generator names `STATUS.md` outside the sites in Inventory, and no decision record created the slot.

### Alternatives rejected

**Deleting the file and leaving the contract.** Cheapest diff, and it produces exactly the state this
build exists to end: a documented slot with no instance, three selectors over an empty class, and a
rule set that promises adopters a file the reference tree does not keep.

**Keeping the slot and fixing the one file.** It makes one build folder answer the question the
generated region already answers, which is the `two-answers-to-one-question` gotcha class, and that
class is `universal: true`, so every reviewer of this diff is asked about it by machine.

### Files touched (estimate)

`memory/builds/aPrunedCeremony/STATUS.md` (deleted) · `tools/memory-tree/check-memory-hygiene.sh` ·
`tools/memory-tree/check-memory-hygiene.test.sh` · `tools/memory-tree/HYGIENE.template.md` and
`memory/HYGIENE.md` as a rendered pair · `tools/memory-tree/adopt-memory-tree.sh` and
`memory/README.md` as an emitter pair · `.gitattributes`. Not touched: `.memory-tree.conf`, because
no `fail` branch is added or removed and the `ARMS_FLOORS` entry
`tools/memory-tree/check-memory-hygiene.sh:14:14` still describes the gate.

## 5. Production-readiness checklist

- security — N/A. A deletion and prose edits; no input crosses a trust boundary.
- perf / scale — checks 6, 7 and 8 each lose a selector, so the gate does strictly less work.
- a11y — N/A. No user-facing surface.
- i18n — N/A. The edited strings are ASCII path literals.
- error / empty / loading states — check 8's REMAINING population must stay non-empty, or the check
  becomes the vacuous-selector-over-an-empty-population class this repo reds elsewhere. Verified:
  four shards exist at `memory/backlog/` — `DEPL.md`, `KICK.md`, `PLAY.md` and `TOOL.md` — so both
  `pop8` and `PRE_STATUSY` stay non-zero here, and in a freshly scaffolded tree both are zero
  together, which `pop_guard` correctly reads as a young tree rather than a disarmed check.
- observability — check 8's failure text and its `pop_guard` label both stop naming a class that
  cannot appear, so an operator reading either is not sent looking for a file that does not exist.
- risks — the failure text is asserted verbatim by one arm; changing the message without the arm reds
  the self-test leg, and changing the arm without the message makes it assert a string the gate never
  emits. Both directions are caught, but only if the two move in one commit.
- testing + left-shift gates — the existing check-8 arm keeps its two assertions on
  `memory/backlog/ARCH.md`, at the two-token row and the one-token control, so the check is still
  proved live after losing a population it never had a fixture for.
- migration / rollback — a single-commit revert restores the file and every rule that described it;
  no generated bytes and no ratchet numbers move.
- user docs — `HYGIENE.md` and `memory/README.md` are the two documents a session reads to learn the
  tree, and both are in the same commit.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs at this unit's tip, it exits 0
  and prints no `check 8:` population-guard line.
- **AC2** — When `git grep -n 'STATUS\.md' -- tools/ memory/HYGIENE.md memory/README.md .gitattributes`
  runs, it returns no match.
- **AC3** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, it passes with its
  check-8 arm asserting the reworded failure text and still hitting `memory/backlog/ARCH.md:8` while
  sparing `memory/backlog/ARCH.md:5`.
- **AC4** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, it reports parity between
  `tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md` with no `--render` left to do.
- **AC5** — When `python tools/memory-tree/check-arms.py --check` runs, it passes with `ARMS_FLOORS`
  unchanged at `tools/memory-tree/check-memory-hygiene.sh:14:14` and no new row in
  `memory/project/unarmed-branches.txt`.
- **AC6** — When `python3 tools/memory-tree/gen_build_index.py --check` runs, it is clean at the same
  artifact count it reports at `base 96141aed`, because no generated file names the deleted one.
- **AC7** — When a fixture backlog row carries two status tokens,
  `bash tools/memory-tree/check-memory-hygiene.sh` still reports it under check 8, proving the
  surviving selector is live rather than vacuous.

## 7. Gates

`bash tools/memory-tree/check-memory-hygiene.sh` · `bash tools/memory-tree/check-memory-hygiene.test.sh` ·
`bash tools/memory-tree/kit-dogfood-parity.test.sh` · `python tools/memory-tree/check-arms.py --check` ·
`bash tools/memory-tree/check-method-carriers.sh`, because both
`tools/memory-tree/HYGIENE.template.md` and `tools/memory-tree/adopt-memory-tree.sh` are declared
rows of `memory/project/method-carriers.txt` and the registry is keyed on path alone ·
`bash tools/memory-tree/check-verdict-epoch.sh`, which this unit does not discharge: it moves
behaviour-bearing lines of the engine, and the build's rules give the one
`KIT_MEMORY_TREE_VERSION` bump to unit 10.

## 8. Open questions

none — fork 6 at the build README resolved the slot to deletion, and the two sites this unit found
beyond its handed enumeration are recorded in §4 Inventory as findings rather than as forks.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft.

## 10. Reuse audit

Recall terms used, recorded so a resumed session re-runs the same query: `build folder allowlist
status file retirement hygiene check 8 index set precondition population guard kit dogfood parity
emitter`. The `tools/codebase-map/reuse_lookup.py` pass over that query returned `checks` in
`corpus_ids.py`, `do_check` in `row_grammar.py` and the hygiene gate-leg keys; none is a seam this
unit wires through, which is expected for a deletion.

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| keep a rule and its enforcement in step | `tools/memory-tree/kit-dogfood-parity.test.sh` and its `--render` direction | REUSE unchanged — the render is how `memory/HYGIENE.md` moves |
| prove a selector is not vacuous after losing a population | `pop_guard` at `check-memory-hygiene.sh:124` | REUSE unchanged — the precondition/population pair already answers this |
| keep the shipped root index and the live one identical | the emitting `echo` at `adopt-memory-tree.sh:95` | REUSE unchanged — no gate pairs them, so the pair is edited by hand and named in §2 |
| the precedent for the split this finishes | `TOOL-aUnmannedHelm-1`, which recorded the same rotted file | REUSE THE RECORD — no new decision id is minted for a slot no decision created |
