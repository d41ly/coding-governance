# TOOL-aDrainedSluice-6 — V5: one python resolver, and it EXECUTES the candidate

**Status:** CLOSED · rev-3 · 2026-08-08 · node a · Tier-2 · base 76fcd09b · streams tooling

## 1. Goal

Six scripts resolve a python launcher, five of them with `command -v python3 || python`. On Windows
the Microsoft Store ships a `python3` **stub** that answers `command -v` and then exits 9009 without
running anything, so every one of those five picks a launcher that cannot execute. Resolve by
RUNNING the candidate, in one place.

## 2. Scope (IN)

- **S1** — `tools/lib/resolve-python.sh` holds the one resolver. It tries each candidate in order and
  accepts the first whose `<cand> -c "import sys"` EXITS ZERO. Answering `command -v` is not
  evidence; running is. It ECHOES the launcher and returns non-zero on failure, so every call site is
  `PY=$(resolve_python) || { …; exit 2; }` — a sourced function that merely `return 1`s cannot halt
  its caller, because six of the seven targets run `set -u` WITHOUT `set -e` (measured).
- **S2** — the candidate order is the caller's own override if it has one, then `$GOV_PYTHON`, then
  `python3`, `python`, `py`. Every candidate is ONE WORD. `py -3` was in the draft and cannot work:
  measured, `"py -3" -c "import sys"` exits 127 because the probe quotes the candidate, and
  word-splitting does not rescue it — every consumer uses `"$PY"` as one word and
  `tools/run-gates.sh` substitutes it into `argv[0]`, so a two-word value exits 127 on all ten python
  legs. `py` ALONE is a single word and resolves to Python 3.14 here, measured, which is what makes
  the Windows box this row was opened from work at all. An override that is SET and unusable is a
  NAMED failure, never a silent fall-through.
- **S2b** — `RECALL_PY` survives. It is a PUBLISHED contract — named in the memory-recall README, in
  `WIRE-INTO-PROJECT.md` and in the script's own usage line — so the recall site passes it as its
  first candidate rather than having it quietly replaced by `GOV_PYTHON`.
- **S3** — SOURCING IS ONLY FOR SCRIPTS THAT ARE NOT COPY-INSTALLED. `WIRE-INTO-PROJECT.md`
  copy-installs each kit as a standalone directory (`cp -r <gov>/tools/memory-tree
  <project>/memory-tree`), so a `../lib/` source resolves to nothing in an adopting repo and the kit
  breaks for everyone who adopted it. That is the same constraint that made the drift-audit kit COPY
  the conf parser rather than share it.
  So: `tools/run-gates.sh`, `tools/run-gates.test.sh`, `tools/check-wiring.sh` and
  `tools/check-wiring.test.sh` SOURCE the canonical file — measured against `WIRE-INTO-PROJECT.md`,
  those four are the only python-resolving scripts it never copies out.
  `skills/session-kickoff/manifest-check.test.sh` moved to the INLINE side during the build: the
  runbook copies `manifest-check.sh` ALONE into `<project>/scripts/`, and the skill directory is
  also reached through a per-machine junction, so nothing beside it is guaranteed to be there. Every copy-installed kit script carries the same function INLINE, and a PARITY gate
  asserts each inline copy is identical to the canonical one — copy plus gate, which is this repo's
  existing convention for exactly this situation.
- **S4** — the resolver is sourced, not executed, so the caller gets the resolved value in a
  variable and pays one probe per script rather than one per use.
- **S5** — a source-level gate bans the retired idiom, and its population is MEASURED rather than
  guessed. The draft scoped it to `tools/**/*.sh` and `.githooks/*`; measured, `.githooks/` contains
  ZERO python references — half the declared population is empty — while
  `skills/session-kickoff/manifest-check.test.sh:316` carries the idiom verbatim and is a live
  merge-bar leg, outside the drafted scope. `check-memory-hygiene.sh` has it at three sites and
  `pytest-parallel-guardrails.test.sh` at another, none of them in the draft's migration list, so the
  landing commit would have redded its own tree. The ban and the migration list are now derived from
  ONE scan. Comment lines are excluded, because the resolver's own file explains the idiom it
  replaces.
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
| `tools/memory-tree/check-memory-hygiene.sh` | THREE `_PY=` sites (measured, not two) | one inline copy, resolved once |
| `tools/codebase-map/adopt-codebase-map.sh` | `PY="${MAP_PY:-python}"` — the weakest of the three | inline; `MAP_PY` is the caller override |
| `tools/pytest-parallel-guardrails/pytest-parallel-guardrails.test.sh` | `PYBIN=` idiom | inline |
| `skills/session-kickoff/manifest-check.test.sh` | `PYBIN=` idiom | inline (see S3) |

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

- rev-3 · 2026-08-08 · CLOSED. Landed as one commit: `tools/lib/resolve-python.sh` + its 25-assertion
  test (behaviour against a real 9009 stub, inline-copy parity, the idiom ban), ten migrated call
  sites, `resolve_bash()` hardened with the same run-probe, a new gate leg. Two corrections against
  the drafted inventory, both measured: `check-memory-hygiene.sh` had THREE idiom sites rather than
  two, and `manifest-check.test.sh` belongs on the inline side because the runbook copies its gate
  out alone. Bar 32/32.
- rev-1 · 2026-08-08 · initial draft.
- rev-2 · 2026-08-08 · folded review 2, three blockers and two highs: N1 drops `py -3` for `py`
  (measured — the drafted probe form exits 127 and a two-word value breaks all ten python legs);
  N2 replaces the shared-source design with source-where-not-copied plus inline-with-parity, because
  kits are copy-installed as standalone directories and `../lib/` does not exist in an adopter;
  N3 derives the ban population and the migration list from one measured scan; N7 makes the resolver
  echo-and-return so a `set -u`-only caller can actually halt; N8 preserves `RECALL_PY`.

## 10. Reuse audit

The resolver replaces six copies rather than becoming a seventh, which is the whole unit. The
sourced-sibling pattern is the kits' existing one (`$HERE/<sibling>`); the ban rides the same
source-level-gate shape as `check-review-join.sh`, including its comment-stripping rule; the test
follows the batched-fixture, message-asserting, PASS-last shape every other self-test in this kit
uses. The bash-side probe hardens an existing function rather than adding a second resolver.
