# TOOL-aMouldedFolio-4 — one marker contract across four readers, and a test that drives all four

**Status:** CLOSED · rev-2 · 2026-08-11 · node a · Tier-2 · base 7890becf · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Settle the marker-region well-formedness contract and prove the four live readers obey it, so the
Python copy stops silently rewriting an author's file where the three awk copies refuse it.

## 2. Scope (IN)

- **S1** — the Python splice adopts the COLUMN-0, EXACT-EQUALITY contract the awk copies already
  enforce: a marker is a line that, after one trailing carriage return is stripped, equals the marker
  exactly. Leading whitespace, trailing whitespace and trailing text are each a refusal, not a marker
  that gets normalised.
- **S2** — a conformance test drives ALL FOUR readers over one shared case table and asserts they
  agree case by case. It rides the bar as its own leg.
- **S3** — the case table is the single written statement of the contract; no reader restates it.

## 3. Non-goals (OUT)

- **No shared engine across the language boundary.** Three readers are awk inside one shell kit and
  one is Python in another; no single implementation serves both. rev-1 justified this by kit
  independence, which was WRONG — all three awk copies live in `tools/unattended/`, so lifting a
  primitive between them is intra-kit and permitted. The real reason is the language boundary, and it
  only rules out a FOUR-way lift. A three-way awk lift inside the unattended kit is legitimate and is
  deliberately deferred, not refused.
- No change to any awk copy's behaviour. They are the stricter, non-mutating side.
- No insert mode.

## 4. Design

### Data model

Measured by driving the SHIPPED bytes of each reader over the same inputs:

| Input | awk ×3 | Python | Agree? |
|---|---|---|---|
| markers at column 0 | accept | accept | yes |
| trailing TEXT after a marker | refuse | refuse | yes |
| one trailing CR | tolerate | tolerate | yes |
| unpaired / reversed pair | refuse | refuse | yes |
| **indented marker** | **refuse** | **accept, rewrites to column 0** | **NO** |
| **trailing WHITESPACE on a marker** | **refuse** | **accept, rewrites away** | **NO** |

TWO divergences, not one. rev-1 claimed one and the reviewers reproduced the second: two trailing
spaces are a Markdown hard line break, so this is an authored construct rather than a pathological
one, and nothing in the hygiene gate forbids it. Both divergences run the same direction — Python is
permissive AND mutating, so an author's line comes back altered by a tool they ran for another reason.

**FOUR readers, not three.** rev-1 counted three and missed the one that matters most:

| Reader | Kind | Reads or writes |
|---|---|---|
| `gen_build_index.py:378` `apply_region` | Python | writes |
| `check-unattended.sh:138` `region()` | awk | reads |
| `unattended.sh:103` `region()` | awk | reads |
| **`unattended.sh:115` `splice()`** | **awk** | **WRITES** |

`splice()` carries its own copy of the predicate and is the awk side's mutating path — the one whose
absence, per its own comment, once destroyed data. A conformance test that skips it tests three
readers and the wrong three.

The contract that wins is awk's: it refuses rather than rewrites, it matches this kit's other
line-anchored readers (`parse_front_matter`, `apply_front_matter_ids`), and a shell implementation can
express it without a parser.

MIGRATION: rev-1 claimed zero indented markers anywhere and that was false — two exist, at
`memory/builds/aMooredAnchor/spec/2026-08-11-spec-aMooredAnchor-1.md:111` and `:113`, indented inside a
spec as quoted examples. They are `run:mandate` markers in a spec file, which `apply_region` never
reads, so the migration cost for THIS change is still zero — but the claim as written was wrong and
the correct statement is narrower: no indented `gen:build-index` marker exists in any file the Python
splice reads.

### Inventory

| Function | Change |
|---|---|
| `apply_region` | `l.strip() == MARK` becomes exact equality after one trailing CR is stripped |
| a new `tools/memory-tree/marker-contract.test.sh` | S2, S3 |
| `tools/gate-legs.json`, `AGENTS.md`, a dossier, regenerated map | the leg's obligations |

### Rollout

One commit; the predicate, the test, the leg and its obligations land together or the bar is red
between commits.

### Files touched (estimate)

| File | Why |
|---|---|
| `tools/memory-tree/gen_build_index.py` | S1 |
| `tools/memory-tree/marker-contract.test.sh` | S2, S3 |
| `tools/gate-legs.json` | the leg |
| `AGENTS.md` | the leg's script path — the completeness pin is at 0, tolerance 0 |
| a feature dossier + `memory/map/generated/*` | the leg is a new inventory key; baseline is reserved for the initial backfill |
| `tools/memory-tree/check-memory-hygiene.sh` + both rule-set halves | the version pair — see §8 |
| `.claude/SESSION-KICKOFF.md` | the audit stamp; `gate-legs.json` and the engine are both watched |

### Alternatives rejected

- **Lift a shared primitive across all four.** The language boundary rules it out; the intra-kit awk
  lift is deferred, not refused (§3).
- **Move awk to Python's permissive reading.** It would spread mutation to `splice()`, which writes a
  run-state file.
- **Leave them divergent and document it.** Documenting a defect is what this build undoes.
- **Skip the leg.** A conformance test off the bar asserts nothing after the day it is written.

## 5. Production-readiness checklist

| Concern | Position |
|---|---|
| Drives shipped code | The test invokes the kit's own functions rather than transcribing the awk; AC6 proves it by editing the kit and requiring the verdict to move. |
| Case-table completeness | Six cases, both divergences included. rev-1's table omitted trailing whitespace and would have shipped green over a live disagreement. |
| Empty population | Fixtures, not corpus-derived; cannot go vacuous. |
| **Drift pin, zero headroom** | `non_terminal_specs_cited_by_product_source` reads 2 against pin 2. A new file under `tools/` citing a non-terminal spec id reds it — so the test must NOT cite this spec by id. rev-1 omitted this obligation. |
| check-arms discovery | The new file is a `*.sh`. If it defines `fail() {` it joins the meta-gate's population and needs its own sibling test; the build therefore does NOT define `fail()` in it. |
| Failure visibility | A disagreement names the case, the reader, and both verdicts. |

## 6. Acceptance criteria

- **AC1** — the Python splice REFUSES an indented marker and a marker with trailing whitespace, with a
  named error, and rewrites neither.
- **AC2** — all four readers agree on every case: column-0 accepted; trailing text refused; **trailing
  whitespace refused, on the open marker and on the close marker**; indented refused; one trailing CR
  tolerated; unpaired and reversed refused.
- **AC3** — the test FAILS when the PYTHON reader is reverted to `.strip()`. A per-implementation
  revert control is not available for the awk copies because §3 leaves them unchanged; instead each
  awk reader gets a MUTATION control — a deliberate edit to its predicate must move the verdict —
  which is what AC6 asserts. rev-1's "negative control per implementation" was unsatisfiable.
- **AC4** — the corpus renders byte-identically before and after: no README, no catalogue index and no
  unattended fixture changes.
- **AC5** — the leg is in the manifest, cited in the charter by script path, and claimed by a dossier;
  the completeness pin stays at 0 and the non-terminal-spec pin stays at 2.
- **AC6** — the test binds the SHIPPED readers: a deliberate edit to each of the four changes the
  test's verdict, demonstrated once per reader and recorded in the build report at
  `build/2026-08-16-build-TOOL-aMouldedFolio-3-3-followups-controls.md` §5 2, which carries the transcripts.

## 7. Gates

`bash tools/run-gates.sh` green on a QUIESCENT tree at the push boundary. Affected legs: the new
conformance leg, memory hygiene, the build-index selftest, both unattended selftests, codebase-map
coverage + freshness, drift-audit records, the kit-version and verdict-epoch pair, and the kickoff
ratchet. The recurring-bug-class checklist runs over the diff before review.

## 8. Open questions

- **RESOLVED (agent, 2026-08-11, delegated): version value and landing order.** The three follow-up
  units bump one constant, and an identical bump on two branches merges without conflict while the
  epoch gate stays satisfied — so a parallel landing can leave a later engine change covered by an
  earlier unit's bump. They land SEQUENTIALLY on one branch, each taking the next value; this unit
  takes **2.10** if it lands after `-5`, and re-bumps rather than reusing a value if the order changes.

## 9. Revision log

- rev-1 · 2026-08-11 · first draft, after running the readers over the same inputs, which refuted the
  backlog row's "disagree in both directions".
- rev-2 · 2026-08-11 · Tier-2 review fold. The unit undercounted the readers — `splice()` is a fourth,
  and it is the awk side's WRITING path, so rev-1's test would have covered the wrong three. It also
  undercounted the divergences: trailing whitespace on a marker is a second, in the same
  permissive-and-mutating direction, and rev-1's case table would have gone green over it. The
  kit-independence argument was wrong — all three awk copies are in ONE kit — so §3 now refuses only
  the cross-language lift and defers the intra-kit one. AC3 was unsatisfiable as written. The
  zero-migration claim was false as stated and is narrowed. The drift pin's zero headroom and the
  check-arms `fail()` consequence are new obligations.

## 10. Reuse audit

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| The column-0 exact-equality contract | `parse_front_matter`, `apply_front_matter_ids` | REUSE the convention; this makes a third Python reader consistent |
| Drive a shell function from a test | the kit's `*.test.sh` suites, which invoke shipped scripts | REUSE that shape so the test binds shipped code |
| A gate leg and its obligations | `gate-legs.json` + the dossier/charter/map chain | REUSE the documented path; §4 and §5 enumerate them rather than discovering them at build time |
| Prove a test is not vacuous | the negative-control practice | REUSE as AC3 and AC6 |
