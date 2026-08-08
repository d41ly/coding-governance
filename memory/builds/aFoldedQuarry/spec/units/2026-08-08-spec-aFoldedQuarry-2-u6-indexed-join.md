# TOOL-aFoldedQuarry-2 — U6: index-keyed verdict join in the Tier-2 review harness

**Status:** CLOSED · rev-2 · 2026-08-08 · node a · Tier-2 · base 42c3f4dc · ratified 2026-08-08

## 1. Goal

Replace the string-echo verdict join in `tools/workflows/tier2-review.js` with an
orchestrator-assigned integer key, so that a finding's verdict cannot be lost to path drift and two
findings at one `file:line` cannot share a verdict. Every later unit's adversarial review runs on
this harness, so it goes first.

## 2. Scope (IN)

- **S1** — `allFindings` gains an `id` the ORCHESTRATOR assigns (`i + 1` over the flattened finder
  output), alongside the existing display-only `ref`.
- **S2** — `VERDICT_SCHEMA` requires `id` as an `integer` instead of `ref` as a `string`.
- **S3** — the skeptic prompt prints `id=<n>` per finding, states the exact count and the exact id
  list it must return, and instructs the skeptic to copy the integer rather than retype the path.
- **S4** — the verdict map becomes a `Map` keyed on the integer, populated only for
  `Number.isInteger(v.id)`, and only for an id the orchestrator actually assigned.
- **S5** — a second verdict for an already-decided id is judged on whether it AGREES. An identical
  repeat is idempotent and counted as a duplicate. A repeat whose verdict token differs is a
  CONFLICT: it is counted, logged with its id, and the finding is demoted to unverified rather than
  taking whichever verdict landed last.
- **S6** — the kit's existing trust reporting is kept verbatim in meaning: unverified is never
  refuted, precision excludes unverified, dead lenses and dead skeptic batches are counted, and the
  success return carries the same counters as every early return.
- **S7** — synthesis runs whenever `confirmed + unverified > 0`, and the synth prompt carries the
  unverified findings as OUTSTANDING work rather than dropping them. The nothing-was-judged early
  return is removed: its note text survives on the final return, but the report is still written.
- **S8** — a new gate leg `tools/workflows/check-review-join.sh` fails when a `.ref`-keyed verdict
  assignment or lookup reappears in any JavaScript file under `tools/`, and passes on the shipped
  tree. Its scanned population EXCLUDES the gate script itself and its test, both of which must hold
  the banned pattern verbatim in order to search for it.
- **S9** — a new gate leg `tools/workflows/check-workflow-syntax.js` parses every workflow script in
  the dialect the runtime evaluates — an async function body, after the `export` keyword is stripped
  — so top-level `await` and top-level `return` are accepted and a real syntax error is not.
- **S10** — the harness's `version` marker in `meta` bumps to the next two-part value, because the
  contract with the skeptic agent changed. `tools/check-kit-versions.sh` asserts that shape.

## 3. Non-goals (OUT)

- Renaming the file. `tools/workflows/tier2-review.js` is named by `AGENTS.md`, `README.md` and
  `WIRE-INTO-PROJECT.md`; keeping the name keeps those pointers live and keeps the build-record
  mentions under the memory tree honest.
- Adopting `tier2-review-indexed.js` wholesale. Its early returns drop the lens and skeptic mortality
  counters this harness already reports.
- Changing the concurrency cap, the lens set, the batch size, or the `args` validation.
- Executing the harness end to end as part of the gate. It needs the Workflow runtime's `agent`,
  `phase`, `log` and `parallel` globals, which do not exist in a plain node process.

## 4. Design

### Data model

A finding is `{file, line, severity, claim, impact, fix, ref, id}`. `ref` is `file:line` and is
DISPLAY ONLY from this unit onward — it appears in prompts and report lines and is never a map key.
`id` is a 1-based integer assigned once, after every lens has returned and the results are flattened,
and it is the only join key.

A verdict is `{id, verdict, reason}`. The join is:

```
verdictById : Map<integer, {verdict, reason}>
conflicts   : Set<integer>   // an id whose second verdict DISAGREED with its first
duplicates  : count of repeat verdicts that agreed (idempotent, not a conflict)
spurious    : count of verdicts whose id was never assigned
```

`confirmed`, `refuted` and `unverified` partition `allFindings` on that map, with a conflicted id
landing in `unverified`.

### Inventory

| Line region today | Change |
|---|---|
| `VERDICT_SCHEMA` | `ref: string` becomes `id: integer` |
| flatten of `liveResults` | append `.map((f, i) => ({ ...f, id: i + 1 }))` |
| skeptic prompt | print `id=`, demand the integer, state count and id list |
| `verdictByRef` object | `verdictById` Map with conflict, duplicate and spurious accounting |
| `confirmed` / `refuted` / `unverified` filters | key on `f.id`; a conflicted id is unverified |
| `judged === 0` early return | removed — the outstanding list is exactly what needs a report |
| `confirmed.length === 0` early return | becomes `confirmed + unverified === 0` |
| synth prompt | gains the UNVERIFIED block |
| success return | gains `conflicts`, `duplicates` and `spurious` counters |

### Migration

None. The harness has no persisted state and no callers inside the repo other than the three
documents that name its path, which do not change.

### Rollout

One commit: the harness edit, the new gate script, its leg registration, and the pointer-document
sentence that describes the join.

### Files touched (estimate)

`tools/workflows/tier2-review.js`, `tools/workflows/check-review-join.sh`,
`tools/workflows/check-review-join.test.sh`, `tools/workflows/check-workflow-syntax.js`,
`tools/gate-legs.json`, and `AGENTS.md`.

### Alternatives rejected

- **Normalise the ref on both sides before joining.** Rejected: normalisation cannot fix a line
  number the skeptic re-derived, and it cannot separate two findings that legitimately share one
  `file:line`.
- **Take the last verdict on a collision, as upstream does.** Rejected: silently applying one
  verdict to two findings is the catalogued collision class itself. A conflicting id is exactly the
  case where the harness does NOT know, and unverified is what "does not know" means here.
- **Delete the harness and ship the upstream file.** Rejected in the master spec: it loses the
  unverified and PARTIAL reporting this harness already has.

## 5. Production-readiness checklist

- security — N/A. The join is arithmetic over agent output; nothing is executed or interpolated into
  a shell.
- perf / scale — a `Map` lookup replaces an object property lookup. No change in complexity.
- a11y — N/A — no user interface.
- i18n — N/A — the harness prompt and report are English by construction.
- error / empty / loading states — every degraded shape already returns a note; this unit adds two
  more degraded shapes (conflicting and spurious verdicts) and gives each its own counter and log.
- observability — the run logs adjudicated counts, the unverified id list, conflicts and spurious
  ids, so a partial review cannot read as a clean one.
- risks — the only behavioural risk is a skeptic that ignores the integer instruction, which now
  produces unverified findings and a loud warning instead of a silent misjoin.
- testing + left-shift gates — the source-level join gate plus its own self-test.
- migration / rollback — none needed.
- user docs — the sentence in `AGENTS.md` describing the harness.

## 6. Acceptance criteria

- **AC1** — When the harness assigns ids, two findings sharing one `file:line` get distinct ids and
  the join returns their own verdicts independently.
- **AC2** — When a skeptic returns a verdict whose id was never assigned, the run counts it as
  spurious, logs it, and leaves every real finding's verdict untouched.
- **AC3** — When two DISAGREEING verdicts arrive for one id, the finding is reported UNVERIFIED and
  the conflict is logged with that id; when the repeat AGREES, the verdict stands and the run counts
  a duplicate.
- **AC4** — When no verdict arrives for a finding, it is reported UNVERIFIED, excluded from
  precision, and carried into the synth prompt as outstanding.
- **AC5** — When `bash tools/workflows/check-review-join.sh` runs on the shipped tree it exits 0;
  when a `.ref`-keyed verdict assignment is reintroduced into a JavaScript file under `tools/`, it
  exits non-zero and names that file and line. The gate's own source and its test are outside the
  scanned population, so the gate is green on the tree that contains it.
- **AC6** — When `bash tools/workflows/check-review-join.test.sh` runs, it proves the gate's RED arm
  against a fixture and its GREEN arm against the real tree, and prints its pass line last.
- **AC7** — When `node tools/workflows/check-workflow-syntax.js` runs over the shipped harness it
  exits 0, and when given a file with an unbalanced parenthesis it exits non-zero and prints that
  file's `SyntaxError`. A plain `node --check` does NOT satisfy this: measured on node v24, it exits
  0 on a file whose parse genuinely fails.

## 7. Gates

Existing: `bash tools/run-gates.sh` in full, and `bash tools/check-kit-versions.sh` for the bumped
version marker. New: `tools/workflows/check-review-join.sh`,
`tools/workflows/check-review-join.test.sh` and `tools/workflows/check-workflow-syntax.js`, all
registered in `tools/gate-legs.json`.

## 8. Open questions

none — the three forks below are RESOLVED (owner-ratified 2026-08-08); kept for the record.

- **Fork A — where the ban gate lives.** Options: a new script under `tools/workflows/`, or another
  predicate inside `tools/gate-lint/ps-hygiene.py`. RESOLVED (owner, 2026-08-08): a new script.
  `ps-hygiene.py` lints POSIX shell; a JavaScript join is not its population, and widening it would
  make its name a lie.
- **Fork B — how the ban avoids firing on prose.** Options: scan whole file text, or scan
  non-comment lines only. RESOLVED (owner, 2026-08-08): non-comment lines only. An absence assertion
  over whole file text reds on the comment that documents the fix, which is a trap this repo has
  already paid for once.
- **Fork C — how a workflow script is syntax-checked.** Options: `node --check`, or constructing an
  async function from the source. RESOLVED (owner, 2026-08-08): the async-function construction.
  Review 1 measured `node --check` exiting 0 on a file with an unbalanced parenthesis, and the
  harness dialect (module export plus top-level await plus top-level return) has no standard parser
  mode that accepts all three.

## 9. Revision log

- rev-1 · 2026-08-08 · initial draft.
- rev-2 · 2026-08-08 · folded review 1: R1 replaces the vacuous `node --check` with an
  async-function probe and adds S9; R2 splits an agreeing repeat verdict from a conflicting one;
  R3 excludes the ban gate from its own population; R4 widens the ban to every JavaScript file under
  the tool root; R5 removes the nothing-was-judged early return; R6 pins the version format.

## 10. Reuse audit

The seam already exists and this unit wires through it rather than around it. The harness is edited
in place at `tools/workflows/tier2-review.js`, keeping the three live pointer documents valid. The
new gate registers as a leg in `tools/gate-legs.json`, which `tools/run-gates.sh` already iterates,
so no runner is added. The self-test follows the shape of `tools/hooks/agent-cap.test.sh` — a
scratch fixture, a red arm and a green arm, assertions on the emitted message rather than the exit
code. The one rejected reuse is `tools/gate-lint/ps-hygiene.py`, recorded as Fork A in §8: it is a
POSIX-shell linter and a JavaScript predicate does not belong in its population.
