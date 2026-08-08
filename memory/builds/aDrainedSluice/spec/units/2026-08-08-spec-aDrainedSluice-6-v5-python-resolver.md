# TOOL-aDrainedSluice-6 — V5: one python resolver, and it EXECUTES the candidate

**Status:** INPROGRESS · rev-1 · 2026-08-08 · node a · Tier-2 · base 76fcd09b · streams tooling

## 1. Goal

Six scripts resolve a python launcher, five of them with `command -v python3 || python`. On Windows
the Microsoft Store ships a `python3` **stub** that answers `command -v` and then exits 9009 without
running anything, so every one of those five picks a launcher that cannot execute. Resolve by
RUNNING the candidate, in one place.

## 2. Scope (IN)

- **S1** — `tools/lib/resolve-python.sh` is the one shell resolver. It tries each candidate in order
  and accepts the first whose `<cand> -c "import sys"` EXITS ZERO. Answering `command -v` is not
  evidence; running is.
- **S2** — the candidate order is `$GOV_PYTHON` (explicit override, tried first and, if set and
  unusable, a NAMED failure rather than a silent fall-through), then `python3`, then `python`, then
  `py -3`. A launcher that is present but broken is skipped and NAMED in the failure message when
  nothing works.
- **S3** — every current site sources it: `tools/run-gates.sh`, `tools/run-gates.test.sh`,
  `tools/check-wiring.sh`, `tools/check-wiring.test.sh`, `tools/memory-recall/adopt-memory-recall.sh`,
  `tools/memory-tree/adopt-memory-tree.sh`, plus the two `_PY=` sites inside
  `tools/memory-tree/check-memory-hygiene.sh`. None keeps a private copy.
- **S4** — the resolver is sourced, not executed, so the caller gets the resolved value in a
  variable and pays one probe per script rather than one per use.
- **S5** — a source-level gate bans the retired idiom in `tools/**/*.sh` and `.githooks/*`: a line
  that assigns a python launcher from `command -v` without running it. Comment lines are excluded,
  because the resolver's own file explains the idiom it replaces.
- **S6** — `tools/lib/resolve-python.test.sh` proves the resolver against a FAKE stub on `PATH` that
  answers `command -v` and exits 9009 — the exact defect — plus a working candidate behind it, an
  all-broken case, and the override in both its good and bad states.
- **S7** — the Python side gets the same treatment where it already exists:
  `tools/memory-tree/corpus_ids.py`'s `resolve_bash()` gains a run-probe on the candidate for the
  same reason, since a bash that cannot launch is the same class one interpreter over.

## 3. Non-goals (OUT)

- A python VERSION check. The kits declare a floor in their own docs and a version probe is a
  separate rule with a separate failure; this unit fixes "the launcher cannot run at all".
- Converging the BASH resolvers. There is one, in `corpus_ids.py`, and S7 hardens it in place.
- A PowerShell twin. No second runner exists yet; the row that would justify one is already DEFERRED
  in the playbook backlog.

## 4. Design

### Data model

```
resolve_python()  ->  echoes the working launcher, or exits non-zero with a named failure
GOV_PYTHON        ->  explicit override; set-but-unusable is a NAMED failure, never a fall-through
probe             ->  "<cand>" -c "import sys" >/dev/null 2>&1
```

An explicit override that silently falls through is worse than no override: the operator believes
they chose, and did not.

### Inventory

| Site | Today | After |
|---|---|---|
| `tools/run-gates.sh` | `PYBIN=` idiom | sources the resolver |
| `tools/run-gates.test.sh` | `PYBIN=` idiom | sources the resolver |
| `tools/check-wiring.sh` | `PY=` idiom | sources the resolver |
| `tools/check-wiring.test.sh` | `py=` idiom | sources the resolver |
| `tools/memory-recall/adopt-memory-recall.sh` | `PY=` idiom | sources the resolver |
| `tools/memory-tree/adopt-memory-tree.sh` | `_PY=` idiom | sources the resolver |
| `tools/memory-tree/check-memory-hygiene.sh` | two `_PY=` sites | sources the resolver once |

### Migration

None; each site's variable name is kept so the surrounding code is unchanged.

### Rollout

One commit: the resolver, its test, the seven call sites, the ban and its arm.

### Files touched (estimate)

One new file plus its test, seven edited scripts, the gate-leg manifest.

### Alternatives rejected

- **Keep the idiom and add a run-probe at each site.** Rejected: that is seven copies of one
  predicate, which is the two-answers class this repo has a catalogue record for.
- **Put the resolver inside one kit and have the others source it.** Rejected: the kits are
  independently deployable, so that makes every kit depend on one. A tiny shared file each kit copies
  is the shape the conf parser already has.

## 5. Production-readiness checklist

- security — the resolver executes a candidate interpreter with a fixed, non-interpolated argument.
- perf / scale — one process per script, not one per use.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — no working candidate is a NAMED failure listing every candidate
  tried and why each was rejected.
- observability — the failure names the candidates and the override.
- risks — sourcing a shared file adds a path dependency; each caller resolves it relative to its own
  location, which is the pattern the kits already use for sibling scripts.
- testing + left-shift gates — a fake stub on `PATH`, so the arm exercises the exact defect.
- migration / rollback — one commit.
- user docs — `WIRE-INTO-PROJECT.md` and the kit READMEs name the shared file.

## 6. Acceptance criteria

- **AC1** — When a fake `python3` that answers `command -v` and exits 9009 is first on `PATH`, the
  resolver skips it and returns the working candidate behind it.
- **AC2** — When no candidate runs, the resolver fails naming every candidate it tried.
- **AC3** — When `GOV_PYTHON` names a working launcher, it is used; when it names an unusable one,
  the failure NAMES the override rather than falling through.
- **AC4** — When any script under `tools/` reintroduces the `command -v` idiom for a python
  launcher, the ban fails naming the file and line; the resolver's own prose does not trip it.
- **AC5** — When the full bar runs, every leg still resolves its interpreter and stays green.
- **AC6** — When `resolve_bash()` in `corpus_ids.py` meets a bash that cannot launch, it skips it
  rather than returning it.
- **AC7** — When `tools/lib/resolve-python.test.sh` runs, every arm above has a red and a green side
  and the pass line prints last.

## 7. Gates

`bash tools/run-gates.sh` in full — every leg depends on the resolver, so the bar IS the integration
test. New legs: the resolver's self-test and the idiom ban.

## 8. Open questions

none — the two forks below are RESOLVED (owner-ratified 2026-08-08); kept for the record.

- **Fork A — where the shared file lives.** Options: `tools/lib/`, or inside one kit. RESOLVED
  (owner, 2026-08-08): `tools/lib/`. Kits deploy independently; a kit-owned resolver makes every
  other kit depend on that kit, which is a worse coupling than a copied file.
- **Fork B — `py -3` as a candidate.** Options: include it, or keep the list to two. RESOLVED
  (owner, 2026-08-08): include it. It is the launcher that works on a Windows box where the Store
  stub shadows `python3`, which is precisely the machine this row was opened from.

## 9. Revision log

- rev-1 · 2026-08-08 · initial draft.

## 10. Reuse audit

The resolver replaces six copies rather than becoming a seventh, which is the whole unit. The
sourced-sibling pattern is the kits' existing one (`$HERE/<sibling>`); the ban rides the same
source-level-gate shape as `check-review-join.sh`, including its comment-stripping rule; the test
follows the batched-fixture, message-asserting, PASS-last shape every other self-test in this kit
uses. The bash-side probe hardens an existing function rather than adding a second resolver.
