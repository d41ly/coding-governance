# TOOL-aRepatriatedFork-32 — every branch of hygiene check 21 honours `RECORD_SERVES_CUTOFF`

**Status:** CLOSED · rev-3 · 2026-09-26 · node a · Tier-1 · base a58011ef · streams tooling · order 17

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-25-build-TOOL-aRepatriatedFork-32-1-acceptance-ledger.md](../build/2026-09-25-build-TOOL-aRepatriatedFork-32-1-acceptance-ledger.md) | journal | — |
| [2026-09-26-review-TOOL-aRepatriatedFork-36-closing-diff-round1.md](../reviews/2026-09-26-review-TOOL-aRepatriatedFork-36-closing-diff-round1.md) | diff-review | TOOL-aRepatriatedFork-31 TOOL-aRepatriatedFork-35 TOOL-aRepatriatedFork-36 TOOL-aRepatriatedFork-37 TOOL-aRepatriatedFork-38 |

<!-- /gen:spec-records -->

## 1. Goal

inCMS declares `RECORD_SERVES_CUTOFF=2026-09-24`, and gov's engine still reds 55 legacy records and
two reviews that predate it. The cutoff reaches only check 21's missing-Serves branch. This unit
makes a record dated before it exempt from every check-21 branch, so inCMS renames nothing. Owner
ruling, `DEPL-aRepatriatedFork-20` §8 F8.

## 2. Scope (IN)

- **S1** — One filter in `tools/memory-tree/check-memory-hygiene.sh`, `extract_graded_rows`, drops
  a row whose record `legacy-files.txt` lists or whose filename date falls before the cutoff. The
  missing-Serves branch, the undefined-id branch and the filename-projection branch all read their
  rows through it. Observed by AC1, AC2.
- **S2** — The unbound pin counts only the records that filter keeps. `gen_build_index.py
  --print-bindings` prints one `U` row per unbound record for it; `N` stays the liveness total.
  Observed by AC1, AC3.
- **S3** — A generator printing `N` without its `U` rows reds check 21, instead of leaving the pin
  ungraded, and the generator contract in `tools/memory-tree/kit.toml` states the same demand, so a
  forked generator lacking the rows fails the contract before it reaches the consumer. Observed by
  AC3, AC6.
- **S4** — A record at or after the cutoff is graded exactly as before, and gov's own tree, whose
  cutoff is blank, still passes the engine in full. Observed by AC1, AC4.
- **S5** — memory-tree takes its version bump in every carrier. Observed by AC5.
- **S6** — Check 21 prints the pin's measurement on every run — the graded count, `N`, and the
  records exempt between them — and REDS a pin above the graded count. The pin is shrink-only, and
  since S2 an adopter who set it to `N` as the runbook said held slack equal to its exempt records,
  which that many new unbound records would spend silently. The runbook's step, the kit's adopter
  hint and the `HYGIENE.template.md` rule name the graded count; `memory/HYGIENE.md` is re-rendered
  from the template. Observed by AC4, AC6.

## 3. Non-goals (OUT)

- Renaming inCMS's legacy records, which this unit makes unnecessary.
- `RECORD_UNDATED_ARTIFACTS`, which stays a missing-Serves exemption: an undated artifact can reach
  no other branch.

### Edges

- **hands-off** `DEPL-aRepatriatedFork-20` — the 55 legacy names and two reviews its inCMS update
  reds, which gov's engine now exempts under inCMS's declared cutoff. nc's pin, 14 against a cutoff,
  is re-measured against its graded count when its engine next moves, under DEPL-aRepatriatedFork-23.

## 4. Design

### Evidence

Before this unit, check 21 ran the `in_legacy` loop and the cutoff awk over the missing-Serves rows
only. The undefined-id rows, the unbound count and the filename-projection rows read the bindings
parse unfiltered. `TOOL-aRepatriatedFork-10` built the grandfathering for the first branch alone.

The round-1 closing-diff review (C1, C2) measured what rev-2 left. The pin moved from `N` to the
graded count while the runbook still said `N`, and nothing refused a pin above the count, so the
slack equals the exempt records wherever a cutoff or legacy row is declared. The generator contract
still pinned only the `N` row that the consumer no longer reads alone.

### Inventory

`extract_graded_rows` — `sh.function`, snake, verb `extract`. The `U` row is a new kind in the
`--print-bindings` output; the check selects its rows by kind letter, so no other reader moves. One
new `[[contract.clause]]` under `memory-tree/gen-build-index`.

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/gen_build_index.py`,
`tools/memory-tree/check-memory-hygiene.test.sh`, `tools/memory-tree/.memory-tree.conf.example`,
`tools/memory-tree/kit.toml`, `tools/memory-tree/HYGIENE.template.md` and its rendering
`memory/HYGIENE.md`, `tools/memory-tree/adopt-memory-tree.sh`, `WIRE-INTO-PROJECT.md`, and the
memory-tree version carriers.

### Alternatives rejected

- Passing the cutoff into the generator. The engine already owns both exemptions, and a second
  reader of the key is two answers to one question.
- The cutoff alone, without the legacy registry. The missing-Serves branch applies both, and the
  scope is that every branch treats a record the same way.
- Warning on slack instead of redding. The pin is documented shrink-only; a warning is read by
  nobody, which is how the slack arrived unnoticed.

## 5. Production-readiness checklist

- security — none; a read-only filter over rows the engine already prints.
- perf / scale — builtins per row plus one awk per branch when a cutoff is declared.
- error / empty / loading states — an empty population prints nothing, as before.
- observability — every finding keeps its text; the pin's measurement prints on every run.
- risks — a narrower population. The preset block still refuses a future cutoff. An adopter holding
  slack reds once, and the finding names the value to lower it to.
- testing — the hygiene suite's cutoff block, sliced; a control run proves the branches fire.
- migration — an adopter whose pin sits above its graded count lowers it in one line.
- user docs — the key's comment in `.memory-tree.conf.example` now says every branch; the runbook
  step and the rendered rule name the graded count.

## 6. Acceptance criteria

- **AC1** — When this unit's block of the hygiene self-test runs as a slice, the control arm names all three pre-cutoff records with the cutoff blank, and with
  `RECORD_SERVES_CUTOFF` set the id, filename and pin branches pass over the pre-cutoff records.
  Red when: any of the three branches still names a record dated before the cutoff.
- **AC2** — When the same slice runs with the old engine and generator swapped in, the three cutoff
  arms fail naming `RECORD_SERVES_CUTOFF`. Red when: the arms pass on the old bytes.
- **AC3** — When a kit copy's `gen_build_index.py` loses its `U` row, check 21 reds with the
  bindings parse printed N 2 but 0 U rows. Red when: the pin goes silently ungraded.
- **AC4** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs on gov's tree, it exits 0
  and prints the pin's graded count beside `N`. Red when: the filter or the `U` rows move a verdict
  on a tree with no cutoff.
- **AC5** — `bash tools/check-kit-versions.sh` exits 0 and `python tools/govkit/govkit.py epoch`
  reports no FAILED entry. Red when: a memory-tree carrier kept the old value.
- **AC6** — When the same slice runs, a `RECORD_UNBOUND_PIN` above the graded count reds naming the
  slack and the value to lower it to, and the new clause in `tools/memory-tree/kit.toml` holds over
  a `--print-bindings` reply with `U` rows or `N 0` and fails one printing `N 2` alone. Red when:
  the rev-2 engine is swapped in, or the clause is removed.

## 7. Gates

`memory hygiene` · `build-index selftest` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `kit/dogfood doc parity` · `lexicon naming predicates` · `memory-hygiene self-test` · `govkit selfcheck`

New arm: `tools/memory-tree/check-memory-hygiene.test.sh` · three record pairs around a cutoff, a kit copy whose generator lost its `U` row, and a pin above its graded count · `FLOOR_ASSERTIONS` 454 to 456

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-25 · initial draft, from `DEPL-aRepatriatedFork-20` §8 F8.
- rev-2 · 2026-09-25 · §2 S3 · AC3 · the `N` without `U` guard added once check-arms demanded its
  arm. Built: five arms green on the new engine, the cutoff arms red on the old one.
- rev-3 · 2026-09-26 · S3 · S6 · §3 · §4 · §5 · AC4 · AC6 · folds the round-1 closing-diff review's
  C1 and C2: check 21 prints graded, total and exempt counts on every run and reds a pin above the
  graded count; the runbook, the adopter hint and the rendered rule name that count; the generator
  contract demands the `U` rows its consumer reads. Built: the whole hygiene suite green, the two
  new arms red on the rev-2 engine.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "exempt a record dated before a cutoff from a hygiene check"`
ranked `check`, `records` and `load_affordance_exempt`, none of which filters check 21's rows; the
map does not scan `.sh`. No existing seam fits beyond the engine's own `in_legacy` lookup and the
cutoff awk, which this unit lifts into one function every branch calls.

Recall terms used: `RECORD_SERVES_CUTOFF check 21 Serves grandfather legacy-files cutoff bindings
unbound pin filename projection`.
