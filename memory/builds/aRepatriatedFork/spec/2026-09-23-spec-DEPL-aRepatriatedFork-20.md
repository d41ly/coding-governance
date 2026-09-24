# DEPL-aRepatriatedFork-20 — inCMS converges onto gov's memory-tree programs

**Status:** BLOCKED · rev-4 · 2026-09-24 · node a · Tier-2 · base f8fdd873 · streams deployer · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-23-build-DEPL-aRepatriatedFork-20-incms-convergence-census.md](../build/2026-09-23-build-DEPL-aRepatriatedFork-20-incms-convergence-census.md) | research | — |
| [2026-09-24-build-DEPL-aRepatriatedFork-20-1-acceptance-ledger.md](../build/2026-09-24-build-DEPL-aRepatriatedFork-20-1-acceptance-ledger.md) | journal | — |
| [2026-09-24-build-DEPL-aRepatriatedFork-20-convergence-journal.md](../build/2026-09-24-build-DEPL-aRepatriatedFork-20-convergence-journal.md) | journal | — |
| [2026-09-24-prompt-DEPL-aRepatriatedFork-20-build-brief.md](../prompts/2026-09-24-prompt-DEPL-aRepatriatedFork-20-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

inCMS runs its own `gen_build_index.py`, `corpus_ids.py`, `gotchas.py` and `merge-rows.py` under
gov's filenames, and its own `check-docs-hygiene.sh` in place of gov's hygiene engine. The owner
ruled on 2026-09-23 that inCMS converges onto gov's copies rather than declaring them its own.
`DEPL-aRepatriatedFork-13` is the bridge that keeps inCMS's pulls unblocked until then. This unit
removes the need for it: inCMS runs gov's five programs verbatim, its tree passes them, and the
bridge rows go.

## 2. Scope (IN)

- **S1** — THE SWAP. inCMS's four programs are replaced by gov's bytes through `govkit update
  --write`, and its `memory-hygiene` leg and three git hooks call gov's `check-memory-hygiene.sh`,
  which is already installed there byte-identical and unwired. `check-docs-hygiene.sh` and its test
  leg retire. The `[[own]]` rows from `DEPL-aRepatriatedFork-13` S6 are deleted in the same change,
  where inCMS carries any. Because the four programs and `check-arms.py` are `unattributed` in the
  receipt, `update` has no base for them, so they first take gov's bytes at the receipt's own
  vintage, and their rows are pinned there.
  Observed by AC1, AC2.
  **Readers:** by name: READER NOT IN TREE — every reader that spells `check-docs-hygiene.sh` is
  inCMS's: two legs and three git hooks, each cited in the census record. The bridge rows are read
  by `govkit.py` once `DEPL-aRepatriatedFork-13` builds them. by value: `govkit.py` reads the
  bridge rows' role; inCMS's legs and hooks read only the engine's exit status, which gov's engine
  supplies in the same shape.
- **S2** — THE FRONT-MATTER MIGRATION. Every build README (326 at build time) moves to gov's syntax: `+`-joined
  `streams` and `roster`, space-joined `ids`, `roster` rewritten from session slugs to the families
  of the build's ids. The `BEGIN/END GENERATED` wrapper and the four stray second `gen:build-index`
  marker pairs are deleted. `status:` is authored where gov requires it, per F1. Each README's
  generated regions move below its authored text, and each README gains the authored
  `roster:units` pair gov's slot contract requires. The README contract and the stale-header waiver
  are seeded, with every README exempt. Then gov's `gen_build_index.py --write` renders every index.
  Observed by AC3.
- **S3** — THE TREE MIGRATION. What gov's engine reds that is inCMS's layout, not its policy, moves:
  the four registries under `scripts/` to `memory/project/`, the dead-path rows rewritten to gov's
  TAB grammar, the three root memory files and 18 `STATUS.md` files folded into sanctioned homes,
  `recurring-bug-classes.md` out of `gotchas/`, and the nested `metadata:` block stripped from every
  gotcha record. `.memory-tree.conf` declares `CHARTER`, `DISCIPLINES`, `SPEC_FORMAT_CUTOFF`, `TOMBSTONE_ROOTS`, the pins
  and the caps inCMS keeps as literals today, and re-measures `ARMS_FLOORS` for gov's engine.
  Observed by AC2.
- **S4** — WHAT RETIRES WITH INCMS'S PROGRAMS. The about 25 `corpus_ids` internals that
  `scripts/recall/selftest.py` imports are inCMS's implementation, not a contract. Those arms retire
  or move with it in the same change; gov does not grow the symbols. The lexicon pin is handled per
  F6. Observed by AC4.
  **Readers:** by name: READER NOT IN TREE — the only importer is inCMS's own recall selftest, run
  by its recall-regression leg, cited in the census record. by value: NO VALUE READERS — the arms test the
  implementation that retires with them, and nothing else reads what they return.
- **S5** — THE CHECKS GOV DOES NOT HAVE. The inCMS hygiene checks with no gov equivalent are
  disposed per F3 and F5, and nothing retires silently: the journal lists each inCMS check number
  with its gov replacement, its new inCMS home, or the owner ruling that retired it. Observed by AC5.
- **S6** — THE MIGRATION SCRIPT is inCMS's, one-shot, beside its existing `scripts/memory-reorg/`
  steps. Gov ships no migration tool: one adopter has this shape. Observed by AC3.

## 3. Non-goals (OUT)

- Gov-side fixes this convergence needs and another unit already owns: `encoding="utf-8"` on the
  eight subprocess sites and the printed `declares:` line (`TOOL-aRepatriatedFork-3`), sibling-kit
  lookup at inCMS's `scripts/recall/` (`TOOL-aRepatriatedFork-2`), and the recall-kit API
  `grammar_for` plus the two-argument `anchor_at`, reached by inCMS running gov's `extract.py`
  (`TOOL-aRepatriatedFork-12`). `PKG` is `TOOL-aRepatriatedFork-12` S2's `RECALL_CITED_FAMILIES`.
- `row_grammar.py` and `check-arms.py`. Both are gov engine rows at inCMS already; `TOOL-aRepatriatedFork-9`
  owns their bytes.
- Staging the five programs one at a time. Measured: gov's generator over the migrated tree reds
  inCMS's engine on checks 22, 23 and 31, so the generator and the engine converge together, and
  `corpus_ids` cannot run before the recall kit does. One landing at inCMS.
- nc, which runs gov's programs already.

### Edges

- **consumes-from** `TOOL-aRepatriatedFork-12` — gov's `extract.py` running at inCMS. Without it gov's
  `corpus_ids.py` and `merge-rows.py` cannot import `grammar_for`, and the swap reds.
- **consumes-from** `TOOL-aRepatriatedFork-2` — the sibling-kit resolver. Without it gov's
  `corpus_ids.py` looks for the recall kit only beside itself and finds nothing at inCMS.
- **consumes-from** `TOOL-aRepatriatedFork-3` — the eight encoding sites and the `declares:` line.
  Without it inCMS's `encoding-posture` leg reds on gov's bytes.
- **consumes-from** `DEPL-aRepatriatedFork-13` — the `[[own]]` bridge rows this unit deletes.
  Without them inCMS cannot pull any of the steps before this one verbatim.
- **consumes-from** `TOOL-aRepatriatedFork-10` — the engine's grandfathering, which decides how the
  1515 inCMS records with no Serves line are graded.
- **consumes-from** `TOOL-aRepatriatedFork-21` — the build-README population at exactly
  `builds/<slug>/README.md`. Without it the slot contract grades inCMS's 41 nested legacy READMEs
  and AC3 cannot pass.

## 4. Design

### Evidence

Measured READ-ONLY at inCMS `9a0e5ebb` against gov `f8fdd873`, in three shared scratch clones;
the record is `2026-09-23-build-DEPL-aRepatriatedFork-20-incms-convergence-census.md`. PINNED at
that run and re-derived at build time.

- A mechanical front-matter rewrite plus an empty stale-header waiver and four deleted marker pairs
  took gov's `gen_build_index.py --check` from a refusal on the first README to clean over 963 files.
  `--write` then touched 324 READMEs, `LIVE.md`, four ledger shards and 634 specs.
- Gov's engine over inCMS with gov's programs: red on checks 2 through 7, 9, and 17 through 21; 521
  of check 5's 676 lines were the registry location alone.
- 194 of 324 builds have no gov-parseable status header. 184 were opened in June or July 2026; ten
  opened in August or September need a real answer each.
- Gov's check 18 reds 68 gotcha records that inCMS's added-only check 25 grandfathers
  (`ARCH-dQuarriedLedger-1`).
- inCMS's `roster:` is session slugs (check 22) and its `ids:` is the minted list (checks 27, 28).
  Gov's are families and a derivation; the derived `ids` is a strict superset in 116 READMEs.
- The lexicon leg goes from 9816 to 9831 verb offenders, over its pin.

### The inCMS checks with no gov equivalent

| inCMS check | Property | Disposition |
|---|---|---|
| 13 | spec-section canon freshness | F5 |
| 16 | the recall fixture resolves into the corpus | F5 |
| 19 | the summed read-path ceiling | F4 |
| 21 | an added memory path is adopted | F5 |
| 22 | a recording's session slug is rostered in its folder | F3 |
| 25 | a new gotcha declares its gate, added-only | F2 |
| 26 | help/ and infra/ name no retired discipline dir | F5 |
| 27 | a minted id owns a recorded row | F3 |
| 28 | shipped ids are not SPECCED | F3 |
| 29 | a new memory .md carries no NUL byte | F5 |
| 30 | CLAUDE.md micro-formats parse under one grammar | F5 |
| 31 | front-matter keys nothing reads | F1, which contradicts it |
| 32 | no literal-credential fallback in memory scripts | F5 |

### Inventory

No gov symbol. inCMS gains one migration script and, per F5, one project leg.

### Rollout

The migration runs in an inCMS worktree and lands on inCMS's `main` through inCMS's own lander, and
that merge and push each need the owner's ask. Revert is one `--no-ff` revert at inCMS, plus
re-adding the `[[own]]` rows.

### Files touched (estimate)

Gov: none beyond this build's records. inCMS, named in prose because none of it is a gov path: its
scripts directory, its three git hooks, its memory-tree conf, its leg manifest, its deploy
descriptor, 324 build READMEs, the generated regions of 634 specs, its gotcha records and its
project registries.

### Alternatives rejected

- Keeping inCMS's programs as `adopter-owned` indefinitely. The owner ruled against it; it stays the
  bridge only.
- A gov migration tool in `tools/govkit/`. One adopter has this shape, and a second one would have
  another.

## 5. Production-readiness checklist

- security — the migration script writes only inside the inCMS worktree it runs in. inCMS's check 32
  (credential fallbacks) is disposed per F5 before its engine retires, so no credential guard lapses.
- perf / scale — gov's engine ran in 19 s over inCMS where inCMS's took about 2.5 min.
- risks — an inCMS check retiring unnoticed, which S5's per-check journal row prevents; and gov's
  derived `ids:` listing cited-but-unminted ids, which F3 accepts along with the loss of checks 27
  and 28.
- migration / rollback — one revert at inCMS; the bridge rows restore the pre-convergence pull.
- error / empty / loading states — the ten August/September builds without a status are not
  defaulted: F1 names who answers them.
- observability — the journal lists every inCMS check's disposition (S5).
- testing — inCMS's full bar is the witness; the red-first control is gov's refusal on the
  unmigrated tree.
- user docs — inCMS's `CLAUDE.md` passage defining `ids:` as the authored minted list is rewritten.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py update --target <inCMS>` runs from gov HEAD after the
  landing, no memory-tree row is `unattributed` or `adopter-owned`, and the run re-stamps
  `gov_commit`.
  Red when: any of the four programs or the engine is still inCMS's bytes.
- **AC2** — At inCMS, the `memory-hygiene` leg runs gov's engine and exits 0.
  Red when: the leg still names `check-docs-hygiene.sh`, or gov's engine reds on the tree.
- **AC3** — At inCMS, gov's `gen_build_index.py --check` and `--check-format` exit 0 over all 324
  READMEs.
  Red when: any README keeps list syntax, a slug roster, or a missing status.
  figure: 326, re-derived at build time on 2026-09-24. The 2026-09-23 measurement pinned 324.
- **AC4** — At inCMS, the `recall-regression` and `lexicon` legs are green after the swap.
  Red when: a recall selftest arm still imports an inCMS-only `corpus_ids` symbol.
- **AC5** — The journal lists every check `check-docs-hygiene.sh` defines with its disposition, and each check F5 keeps
  is observed red on a staged violation in its new home before the landing.
  Red when: a check disappears without a row, or a kept one was never seen failing.
- **AC6** — Red-first control: gov's `gen_build_index.py --check` over an unmigrated clone of inCMS
  refuses on the first README's roster, recorded in the journal.
  Red when: the unmigrated tree passes, so AC3 proves nothing.
- **AC7** — The build's done condition at inCMS: `govkit update --write` from gov HEAD lands every
  row, and inCMS's full bar is green with no hand edit between the update and the bar.
  Red when: any hand edit sits between them.
  cost: one full inCMS bar.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: none. The witnesses are inCMS's own legs, run at inCMS; gov's bar gains nothing.

## 8. Open questions

- **F1 — `status:` on the 194 grandfathered builds.** Gov requires it and refuses a code default;
  inCMS's `ARCH-aFerriedToolkit-1` forbids it. Options: (a) inCMS authors it — the owner ratifies one
  value, `CLOSED`, for the 184 opened before August, and the ten later ones are answered one by one;
  (b) a gov conf key that exempts builds opened before a cutoff. Recommendation: (a). Convergence is
  the ruling, the authoring is one-time, and gov's docstring records that every default it tried was
  wrong, which a bulk value the owner signs is not.
  RESOLVED (agent, 2026-09-23, delegated): (a), with no bulk default: each of the 194 values is
  derived from that build's own records at inCMS, and a build whose status no record decides is
  parked by name. (b) trips veto 2: its pin is documented in `memory/HYGIENE.md`, a governance
  carrier.
- **F2 — the gotcha-declaration scope.** Gov's check 18 is corpus-wide and reds 68 inCMS records.
  Options: (a) inCMS writes 68 declarations; (b) gov gains a shrink-only pin for check 18, the shape
  of its other `*_PIN` keys. Recommendation: (b). inCMS's reason, that a corpus-wide arm reds the bar
  on debt the committer did not write, holds for every adopter with a history, and a pin is gov's
  house form for debt.
  RESOLVED (agent, 2026-09-23, delegated): (a). (b) trips veto 2, because a check-18 pin changes
  `memory/HYGIENE.md`, a governance carrier the delegation does not reach. A record whose gate no
  evidence names is parked by name rather than given an invented one.
- **F3 — the three checks whose input the migration removes (22, 27, 28).** Options: (a) inCMS accepts
  the loss, and gov's backlog gets rows for 27 and 28 as candidate gov checks; (b) this build adds
  them to gov first. Recommendation: (a). Check 22 guards a meaning of `roster:` gov does not have,
  and 27 and 28 are properties worth having everywhere, which is a unit of its own, not a
  precondition here.
  RESOLVED (agent, 2026-09-23, delegated): (a). (b) trips veto 2: two new gov checks change
  `memory/HYGIENE.md`, a governance carrier. The two backlog rows ride the landing commit.
- **F4 — the summed read-path ceiling (inCMS check 19).** Gov retired the sum in 2.42. Options: (a)
  inCMS accepts the loss; (b) keep it as an inCMS project leg. Recommendation: (a). Gov already weighed
  and refused it.
  RESOLVED (agent, 2026-09-23, delegated): (b), against the recommendation. M3 ratifies the most
  feature-rich survivor, and (b) keeps a check (a) drops. It survives every veto: the leg is inCMS's
  own and touches no gov carrier. It joins F5's project leg.
- **F5 — the other inCMS-only checks (13, 16, 21, 26, 29, 30, 32).** Options: (a) inCMS extracts them
  into one project leg of its own; (b) they retire. Recommendation: (a). They guard inCMS's own
  surfaces, 32 is a credential guard, and none of them conflicts with gov's engine.
  RESOLVED (agent, 2026-09-23, delegated): (a), the most feature-rich survivor.
- **F6 — the lexicon leg, 15 over its pin.** Options: (a) inCMS re-pins once in the landing commit,
  naming the four swapped files as the cause; (b) gov renames. Recommendation: (a). Gov's own lexicon
  grades these files by gov's table, which differs from inCMS's, so a rename for one table is a red
  for the other.
  RESOLVED (agent, 2026-09-23, delegated): (a). (b) trips veto 2: renaming functions consumers
  import changes a public surface.

## 9. Revision log

- rev-1 · 2026-09-23 · opened after the owner ruled that inCMS converges and that this build carries
  the migration. Grounded at inCMS 9a0e5ebb and gov f8fdd873 by the convergence census.
- rev-2 · 2026-09-23 · §8 resolved under the aRepatriatedFork mandate (M3, delegated). F4
  keeps inCMS check 19 as a project leg beside F5's checks, which moves its row in §4 from a
  loss to a kept check.
- rev-3 · 2026-09-24 · the first build pass, and the unit is BLOCKED. The migration is prepared on
  inCMS branch `converge/aRepatriatedFork-20` at `2b8d9a5cd04089c8416670fe87c9026c01ddb09d`, which
  is not pushed and not merged. The landing is the owner's. The journal lists the S1, S3, S4 and S5
  work still owed on that branch before the landing. S1: inCMS has no `[[own]]` rows, because its
  last pull predates `DEPL-aRepatriatedFork-13`. The four programs and `check-arms.py` were
  `unattributed`, so they now carry gov's a7c78ad2 bytes, with their rows pinned at that vintage.
  S2 gains the README layout move and the two seeded registries; without them, gov's
  `--check-format` refused all 326 READMEs. S3 gains `TOMBSTONE_ROOTS`. AC3's figure is re-derived
  as 326.
- rev-4 · 2026-09-24 · §3 gains the **consumes-from** edge to `TOOL-aRepatriatedFork-21`, the gov fix for
  the nested-README population this unit's pass measured at inCMS.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "an adopter replaces its own memory-tree programs with gov's and migrates build README front matter"`
ranked `tree`, `build_reference_index`, `adopt` and `build_index`, none of which migrates an
adopter's records; no existing seam fits as a mapped symbol, and the probe does not scan `.sh`. The
gov-side fixes this needs already exist as units (§3). The migration reuses inCMS's own one-shot
memory-reorg step pattern and gov's `--write`, which renders every index the migration would
otherwise hand-edit.

Recall terms used: `adopter-owned converge gen_build_index corpus_ids gotchas merge-rows roster ids
status grandfathered front-matter migration hygiene`.
