# TOOL-aThawedCorpus-3 — a declared SPAWN ceiling per memory leg, because wall clock cannot be a verdict here

**Status:** OPEN · rev-1 · 2026-08-27 · node a · Tier-2 · base 4f406bf7 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-review-TOOL-aThawedCorpus-5-spec-audit.md](../reviews/2026-08-27-review-TOOL-aThawedCorpus-5-spec-audit.md) | spec-audit | TOOL-aThawedCorpus-5 TOOL-aThawedCorpus-4 TOOL-aThawedCorpus-1 TOOL-aThawedCorpus-2 |

<!-- /gen:spec-records -->

## 1. Goal

The per-item-spawn defect has now been found and hand-fixed five times in this repo and nothing
gates the class, so it returns. Give every memory-tree gate leg a DECLARED ceiling on how many
processes it creates over this corpus, red on breach, and red on a leg that declares none. Spawns
rather than seconds, because seconds on this node are not a property of the code.

## 2. Scope (IN)

- **S1** — A counter: a `PATH`-prepended shim directory holding a wrapper for each external command
  the memory checkers call, which increments a counter file and then `exec`s the real tool.
- **S2** — A runner that executes a declared leg under the shim, compares the count against that
  leg's declared ceiling, and REDS on breach naming the leg, the count and the ceiling.
- **S3** — A declarations file, `tools/memory-tree/spawn-ceilings.txt`, one `<leg>\t<ceiling>` row per
  memory-tree leg, every value MEASURED against this corpus and none inherited.
- **S4** — An undeclared leg REDS by that fact, and a row naming a leg the manifest no longer carries
  REDS too, so the declaration cannot go stale in either direction.
- **S5** — The runner PRINTS its own coverage mode every run: which commands are shimmed, and the
  standing statement that the count is a LOWER BOUND because shell builtins and absolute-path
  invocations do not traverse `PATH`.
- **S6** — Byte-identity: the checker's stdout under the shim equals its stdout without it.

## 3. Non-goals (OUT)

- **N1** — No wall-clock ceiling. Measured on this node the same commit's pre-commit hook cost 913 s
  under load and 29 s quiet — a 31x spread on identical work. A seconds ceiling here would red on
  contention and pass on a quiet box, which is a gate that grades the machine.
- **N2** — No static scan for the defect shape. A predicate matching "a command substitution inside a
  loop" flags every legitimate small loop in the tree; run the candidate over the real corpus and it
  reds innocent files, which is the rule §7 states about candidate predicates.
- **N3** — Not extended beyond `tools/memory-tree/` in this unit. The class lives repo-wide, but a
  ceiling is only meaningful where it was measured, and pinning ceilings for legs this build has not
  measured would be the copied-pin defect this corpus keeps a record for.
- **N4** — The shim never rewrites, filters or reorders a command. It counts and it `exec`s.

## 4. Design

### Data model

`spawn-ceilings.txt`: `<leg name>` TAB `<integer ceiling>`, `#` comments, one row per leg. Values are
SHRINK-ONLY by convention and by the same reasoning `ARMS_FLOORS` uses — a ceiling that only ever
rises is a ceiling nobody defends.

The shim directory is built at runtime into a `mktemp -d`, holding one two-line script per shimmed
command. Each appends a byte to a counter file and `exec`s the real binary resolved from the
ORIGINAL `PATH`, captured before the shim is prepended.

### Inventory

Shimmed commands, derived from what the memory checkers actually invoke: `grep`, `sed`, `awk`, `tr`,
`cut`, `basename`, `head`, `sort`, `wc`, `xargs`, `git`, `python`, `python3`. The list is DECLARED in
the runner and printed every run, because a command nobody shimmed is a spawn nobody counted.

### Rollout

Landed after the two collapse units, so every ceiling is measured against the code that ships rather
than against the code being replaced. A ceiling measured against the current 1398 s implementation
would be satisfied by the defect it exists to prevent.

### Files touched (estimate)

`tools/memory-tree/spawn-ceilings.txt` (new) · `tools/memory-tree/check-spawn-ceilings.sh` (new) ·
`tools/gate-legs.json` (one leg) · `tools/memory-tree/kit.toml` (the new files declared) ·
`tools/memory-tree/README.md` (one row).

### Alternatives rejected

- **A wall-clock ceiling, the `BUDGET_*` shape from `run-unattended-gates.sh`.** Rejected under N1 on
  this build's own measurement. That precedent runs on suites whose spread is smaller; this one's
  subject is a leg measured at a 31x spread on the same bytes.
- **Counting with `strace`/`ltrace`.** Rejected: neither exists on the Windows nodes this kit ships
  to, and a gate that runs on one node's toolchain is a gate the fleet does not have.
- **Counting inside the checker itself.** Rejected: a guard that shares a variable with the thing it
  guards is not a guard — the checker would be counting its own spawns with a counter its own
  subshells reset.

## 5. Production-readiness checklist

- security — the shim prepends a temp dir to `PATH` for the duration of one leg. It is created with
  `mktemp -d`, holds only generated wrappers, and is removed in a trap. It never runs in a shell the
  operator keeps.
- perf / scale — the shim adds one `exec` per counted spawn. Measured before landing; if the overhead
  exceeds the signal the unit is re-specced rather than shipped with an unmeasured cost.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a counter file that cannot be created is an ABORT, not a pass.
  A count of zero with a non-empty shim list is the vacuous case and REDS, because a run that spawned
  nothing did not run.
- observability — S5's coverage line, every run.
- risks — the shim could change behaviour by resolving a different binary. S6's byte-identity check
  is the control. The lower-bound property is announced rather than hidden.
- testing + left-shift gates — this unit IS the left-shift for the class. Its own arms stage a
  breach and observe RED, per the rule that a gate whose failing case was never observed is an
  assertion about nothing.
- migration / rollback — additive: a new file, a new leg, no default changed.
- user docs — one row in the kit README naming the file and the lower-bound caveat.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/check-spawn-ceilings.sh` runs over the collapsed checker, it
  exits 0 and prints each leg's measured count beside its declared ceiling.
- **AC2** — When a row in `tools/memory-tree/spawn-ceilings.txt` is temporarily lowered below its
  measured count, the runner REDS naming the leg, the count and the ceiling — the breach observed
  RED, then restored.
- **AC3** — When a leg is added to `tools/gate-legs.json` under `tools/memory-tree/` with no row in
  `spawn-ceilings.txt`, the runner REDS naming that leg as undeclared.
- **AC4** — When a row in `spawn-ceilings.txt` names a leg `tools/gate-legs.json` no longer
  carries, the runner REDS naming the stale row.
- **AC5** — When the checker runs under the shim and without it, `diff` reports no difference in
  stdout.
- **AC6** — When the shim list in `check-spawn-ceilings.sh` is emptied, the runner REDS on a zero
  count rather than passing — the vacuous case observed RED.
- **AC7** — When `bash tools/memory-tree/check-spawn-ceilings.sh` runs, its stdout carries the
  shimmed command list and the lower-bound statement.

## 7. Gates

`memory hygiene` · `govkit selfcheck` (the new files must be declared in the tooling registry) ·
`run-gates canary` · `harness arms (fail branches armed or pinned)`. Adds one leg, itself.

## 8. Open questions

- **F1 — is the ceiling per LEG or per CORPUS ITEM?** A flat per-leg integer goes stale as the corpus
  grows: 71 builds today, and a ceiling measured now reds on a tree with 90. A per-item ratio
  (`spawns / tracked memory file`) survives growth but is a figure nobody can check by eye.
  Recommendation: a per-leg integer PLUS the corpus size it was measured at, on the same row, so a
  breach report can say whether the count grew or the corpus did. Resolve before code.

- **F2 — does the shim's own `exec` overhead swamp the signal on this node?** PROBE: run the
  collapsed checker with and without the shim on a quiet box and compare wall clock. OBSERVATION
  THAT DECIDES IT: if the shimmed run costs more than twice the unshimmed one, the gate is too
  expensive to keep on the bar and becomes an on-demand leg instead. LIVENESS: the probe can produce
  a negative — process creation on this node is the very thing this build measured at 0.2 s and up,
  and the shim adds one per spawn, so a 2x breach is the expected outcome rather than an unlikely
  one, and the on-demand branch is live.

## 9. Revision log

- rev-1 · 2026-08-27 · initial draft. Spawns rather than seconds, on this build's own 31x
  load-spread measurement.

## 10. Reuse audit

The seam for the DECLARATION shape is `tools/template-size-limits.txt` and
`tools/memory-tree/build-readme-slot-limits.txt` — both are `<subject>` TAB `<ceiling>` files read by
a checker, both split the advisory high-water into a second file so the write path cannot move the
bound, and `tools/check-template-size.sh` is the reader to copy. The seam for the CEILING IDEA is
`tools/unattended/run-unattended-gates.sh`'s `BUDGET_*` block, whose wall-clock form this unit
deliberately does not take, and whose "declare it or red by that fact" rule it does.

`python tools/codebase-map/reuse_lookup.py "skip re-checking a memory build folder whose content has
not changed since it was last verified"` surfaced no existing spawn-counting seam; there is none in
this tree, which is why the class has been hand-fixed five times.

Recall terms used, because M7 re-runs the query: `cache freeze closed build corpus walk hygiene gate
fingerprint incremental stale mtime tree-hash rescan`. It surfaced `TOOL-aMeteredTurnstile-6` and
`TOOL-aScannedThrottle-4`, which are the records establishing that process creation on this fleet is
load-dependent by up to an order of magnitude — the evidence N1 rests on.
