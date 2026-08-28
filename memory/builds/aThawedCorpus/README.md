---
slug: aThawedCorpus
node: a
opened: 2026-08-27
streams: tooling
roster: TOOL
ids: TOOL-aThawedCorpus-1 TOOL-aThawedCorpus-2 TOOL-aThawedCorpus-3 TOOL-aThawedCorpus-4 TOOL-aThawedCorpus-5
authorized-by: prompt
---

# aThawedCorpus — the memory tooling stops paying for a corpus that did not move

## The problem this build exists to solve
The `memory hygiene` leg costs 1398 s, node `a`, 2026-08-27. A WITHDRAWN claim sat
here: that this breached the leg's declared ceiling. It did against the 1270 then standing, but
`TOOL-aBoundedCeiling-1` rev-5 re-derived that to 12720 -- a ceiling bounds a HANG, and sizing one
like a cost budget reds it on ambient load. The speedup stands on its own numbers.
The cost is not the walk. Check 23 is 962.0 s of it and check 21 is 338.9 s — 93.1% between them —
and both are slow for one reason: they spawn a process per corpus item for work that is string
manipulation. Ten other checks total 32.4 s. Separately, the leg declares no `guard`, so
`run-gates.sh` keys it on the whole-tree fingerprint and the `GATE_REUSE` freeze it already has can
never match. The owner's mtime observation is reproduced, and what it implies is that no mtime-keyed
cache could ever hit here — git records none.

## Expected improvements
- The dominant term in the memory bar's cost stops being process creation this repo controls.
- A bar that touches no memory file stops re-deriving a verdict nothing could have invalidated.
- Adopters inherit both, from the kit, without hand-fitting anything to their tree.
- The saving is held by a declared SPAWN ceiling that REDS on breach, not asserted in prose.

## Detriments if this is not built
- A 23-minute leg whose cost grows with the corpus, on every node, forever.
- The next agent that reaches for `--staged` to dodge it also drops the checks that catch the
  defects the leg exists to catch.
- Every adopter inherits the same curve the day their tree gets interesting.

## Build-level rules
- **Verdicts are byte-identical, and that is proven not argued.** Every unit's acceptance
  diffs the checker's full-corpus output against the pre-change checker. A performance change that
  moves a verdict is a defect, not a trade.
- **A cache miss costs wall clock and never a verdict.** Absent, corrupt, unreadable or
  version-mismatched skip state means RUN. That is the law `gate-ledger.tsv`, `gate-full-green` and
  `run-gates.sh`'s reuse unit already run under, and it is not renegotiated here.
- **Seconds are not a verdict on this node.** The same commit's hook measured 913 s under load and
  29 s quiet — 31x on identical bytes. Every figure here carries the foreign-process count at both
  ends; the ceiling unit counts SPAWNS, which do not vary with load.
- **The key covers everything the verdict depends on, or the check is not keyed.** A checker whose
  answer depends on files other than the one in hand may not be skipped per file: check 2 reds on a
  DELETED link target, and checks 21 and 23 read an id set defined elsewhere. Whole input set or
  nothing.
- **Do not key on `CLOSED`.** Status is authored and can lie; content is derived and cannot. Keying
  on "unchanged" subsumes "fully closed" and covers the idle-but-open build too.
- **The kit stays standalone.** No `../lib/`, no `tools/run-gates/`. `resolve_python` is the
  precedent for what that costs and how it is paid.
- **The freeze already exists — do not build a second one.** `run-gates.sh`'s `input_key` plus
  `GATE_REUSE` already skip a leg whose content key is unchanged and whose last verdict was green:
  content-addressed, fail-open, gated. The memory legs sit outside it only because they declare no
  guard. Declaring the true input set is DATA; a parallel cache is a second answer to one question.

## Parked decisions
*(none yet — this section is where a refused decision lands, with its question, the options seen,
and why the run refused it.)*

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aThawedCorpus-5` | 1 | check 23 gets the `--staged` guard its four siblings already have — one line |
| 2 | `TOOL-aThawedCorpus-4` | 1 | check 23's three per-item loops become two `awk` passes |
| 3 | `TOOL-aThawedCorpus-1` | 1 | check 21's filename projection stops spawning per record |
| 4 | `TOOL-aThawedCorpus-2` | 2 | RETIRED (WONTDO) — guard-skip preempts reuse, and guarding this leg would break unit -5's compensating control |
| 5 | `TOOL-aThawedCorpus-3` | 2 | RETIRED (WONTDO) — per-leg ceilings already shipped as `TOOL-aBoundedCeiling-1`, and a `PATH` shim cannot see a fork |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 5 unit(s) · node a · opened 2026-08-27 · streams tooling
ids TOOL-aThawedCorpus-1 TOOL-aThawedCorpus-2 TOOL-aThawedCorpus-3 TOOL-aThawedCorpus-4 TOOL-aThawedCorpus-5

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aThawedCorpus-5 — check 23 gets the `--staged` guard its four siblings already have](spec/2026-08-27-spec-TOOL-aThawedCorpus-5.md) | 1 | 1 | CLOSED | rev-3 | 2026-08-27 |
| [TOOL-aThawedCorpus-4 — hygiene check 23 stops spawning a process per spec and per record](spec/2026-08-27-spec-TOOL-aThawedCorpus-4.md) | 2 | 1 | CLOSED | rev-6 | 2026-08-27 |
| [TOOL-aThawedCorpus-1 — hygiene check 21 stops spawning a process per record](spec/2026-08-27-spec-TOOL-aThawedCorpus-1.md) | 3 | 1 | CLOSED | rev-5 | 2026-08-27 |
| [TOOL-aThawedCorpus-2 — the memory legs declare what they read, so the freeze that exists can reach them](spec/2026-08-27-spec-TOOL-aThawedCorpus-2.md) | 4 | 2 | WONTDO | rev-2 | 2026-08-27 |
| [TOOL-aThawedCorpus-3 — a declared SPAWN ceiling per memory leg, because wall clock cannot be a verdict here](spec/2026-08-27-spec-TOOL-aThawedCorpus-3.md) | 5 | 2 | WONTDO | rev-2 | 2026-08-27 |
<!-- /gen:build-units -->

Records: 4 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aThawedCorpus-5` | no |
| 2 | `TOOL-aThawedCorpus-4` | no |
| 3 | `TOOL-aThawedCorpus-1` | no |
| 4 | `TOOL-aThawedCorpus-2` | no |
| 5 | `TOOL-aThawedCorpus-3` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
