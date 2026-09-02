# TOOL-dRetiredFork-14 — one hook copy is shipped and wired, not two

**Status:** OPEN · rev-3 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams tooling · order 4 · ratified 2026-09-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

gov ships three hooks to two destinations each and the pairs are byte-identical. Measured
2026-09-02: `tools/hooks/agent-cap.js` and `.claude/hooks/agent-cap.js` are identical at 1610 lines,
`scratch-guard.js` at 394, and `tools/memory-recall/recall-opened.js` against
`.claude/hooks/recall-opened.js` at 207 — 2211 duplicated tracked lines. Every policy value in those
files is therefore stated twice, which is why `nc carve-out 13/20` occupies eleven files: the
dual-ship doubles it before anyone edits anything.

## 2. Scope (IN)

- **S1** — Point the wired command at `{prefix}/hooks/agent-cap.js`. `tools/settings-merge.py`
  takes `hook_path` as a parameter and defaults it to `.claude/hooks/agent-cap.js`, with
  `--hook-path` as the override. **This is NOT merely a call-site change**, which rev-1 claimed:
  `HOOK_MARKER` is the bare basename `agent-cap.js` at `tools/settings-merge.py:49`, and `merge()`
  returns the object unchanged when any command in the matcher group already contains it
  (`:108-109`). The module docstring says so at `:37` — the dedup "deliberately does NOT rewrite a
  stale hook path". Every already-wired tree, gov's own included, is a no-op today.
- **S1b** — Build the capability that is missing: either a `--rewrite-stale-path` mode replacing a
  command whose marker matches but whose path differs, or a fragment-level `hook_path` compare
  distinct from the marker compare. Without it S2's withdrawal leaves every wired tree naming a
  path that no longer ships, which is the silent unwiring §5 calls the highest risk in the build.
- **S2** — Drop the `.claude/hooks/` destinations from the hooks and memory-recall descriptors —
  which in `tools/hooks/kit.toml:43-46` covers `scratch-guard.js` as well as `agent-cap.js`, so
  one copy ships.
- **S3** — EVERY two-copy parity arm becomes SELF-ARMING on the resolved destination count —
  `tools/hooks/agent-cap.test.sh:810-817` and `tools/hooks/scratch-guard.test.sh:183-190`, the
  second of which hard-FAILS rather than skipping when the kit copy is tracked and the wired copy
  is absent, which is exactly the state AC1 requires after this unit lands. Each must
  assert what it finds rather than assume two, and it must REFUSE on zero. A parity arm over a
  population of one that assumes two is the green-by-absence class this repo has already recorded.
- **S4** — `tools/check-wiring.sh` verifies the wired command names the shipped copy, and reports —
  not reds — when a legacy second copy is still present, so an adopter mid-migration is told rather
  than blocked.
- **S5** — Bump `KIT_AGENT_CAP_VERSION`, `KIT_SETTINGS_MERGE_VERSION` and `KIT_MEMORY_RECALL_VERSION`
  with every paired marker, which `tools/check-kit-versions.sh` derives from every tracked `*.js`.

## 3. Non-goals (OUT)

- **The cap VALUE.** This unit changes how many files state the number, never the number. Whether it
  becomes a declared key is parked at build level as an owner turn.
- Deleting an adopter's second copy. gov stops SHIPPING one; removing an installed one is a
  withdrawal, which `govkit update --write-withdrawals` performs on the adopter's own timing.

## 4. Design

### Inventory

| pair | lines | destination after |
|---|---|---|
| `agent-cap.js` | 1610 | `{prefix}/hooks/agent-cap.js` |
| `scratch-guard.js` | 394 | `{prefix}/hooks/scratch-guard.js` |
| `recall-opened.js` | 207 | `{prefix}/memory-recall/recall-opened.js` |

### Migration

gov's own `.claude/settings.json` is rewritten to the new command in the same commit, and gov's
SessionStart wiring check must pass immediately — gov is its own first adopter here, so a mistake is
visible on the next session rather than at an adopter.

An adopter's transition is two steps and they are ordered: the wired command must move to the
surviving copy BEFORE the second copy is withdrawn, or the hook is unwired for the window between.
`DEPL-dRetiredFork-3` is what makes that ordering enforceable rather than a runbook instruction.

### Alternatives rejected

Keeping both destinations and adding a parity gate. A parity gate over two copies is what gov has,
and it costs 2211 lines plus a doubled edit surface to buy a property that one copy has for free.

## 5. Production-readiness checklist

- security — the agent-cap hook is a security-shaped guard. A window in which it is unwired is the
  risk, and S4 plus the migration ordering exist for it.
- perf / scale — one fewer file to read at SessionStart.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the parity arm REFUSES on a zero population; the wiring check
  REPORTS a legacy copy rather than redding.
- observability — `tools/check-wiring.sh` prints which copy is wired, every session.
- risks — an adopter whose settings file is not rewritten keeps pointing at a withdrawn path and
  loses the hook silently. This is the highest risk in the build and is why S4 reports rather than
  reds, and why the withdrawal is not part of this unit.
- testing + left-shift gates — the agent-cap suite, the scratch-guard suite, the wiring suite, the
  settings-merge selftest, and a fixture that verifies
  the two-step ordering.
- migration / rollback — restoring the second destination is a descriptor edit; nothing is deleted
  from an adopter by this unit.
- user docs — `WIRE-INTO-PROJECT.md` maintenance section, and `tools/hooks/README.md`.

## 6. Acceptance criteria

- **AC1** — After the change, `git ls-files` shows one tracked copy of each of the three hooks.
- **AC2** — When `python tools/settings-merge.py --hook-path tools/hooks/agent-cap.js` runs against
  gov's settings, the wired command names the shipped copy and `bash tools/check-wiring.sh` exits `0`.
- **AC3** — When only one copy exists, the parity arm asserts against a population of one and
  passes; when zero exist, it REFUSES. Observed via `bash .claude/hooks/agent-cap.test.sh`.
- **AC4** — When a legacy second copy is present, `bash tools/check-wiring.sh` REPORTS it and still
  exits `0`.
- **AC5** — `bash tools/hooks/agent-cap.test.sh` passes against the surviving copy.
- **AC7** — When a settings file is ALREADY wired at `.claude/hooks/agent-cap.js`, running the
  repath MOVES the command to the shipped copy; measured at `b0108f13`, `merge()` returns the
  object unchanged in that case, so this criterion fails against today's engine.
- **AC6** — `bash tools/check-kit-versions.sh` exits `0`, with every tracked `*.js` marker agreeing.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `check-wiring self-test` ·
`settings-merge selftest` · `kit version markers` · `govkit selfcheck` · `agent-cap restatement`.

## 8. Open questions

- **F0 — does the repath mode rewrite a path a FRAGMENT supplied, or only the built-in default?**
  S1b offers `--rewrite-stale-path` or a fragment-level `hook_path` compare and settles neither; a
  CLI-surface choice sitting outside §8 is one nothing forces before the first code pass.
  `TOOL-dRetiredFork-21` F1 asks the same question from the fragment side and the two must agree.
  Recommendation: a fragment-level compare, so a fragment gov owns and an adopter cannot edit
  without forking is repathed by the same run.

- **F1 — does `.claude/hooks/` remain a legal destination for a project that wants it?** Dropping it
  from gov's descriptors does not forbid an adopter choosing it via a per-entry `kit`. Recommendation:
  keep it expressible, ship it unused.
- **F2 — what withdraws the second copy at an adopter, and when?** `--write-withdrawals` is the only
  verb that deletes, it defaults off, and the ordering constraint above makes premature use unsafe.
  Recommendation: leave the withdrawal to the adopter and say so in the maintenance docs; do not
  automate a delete whose wrong ordering unwires a security guard.

**RESOLVED (owner, 2026-09-02): every fork above is settled by its own stated Recommendation.** The owner ratified them as written on 2026-09-02 with the instruction to fold the recommendations. No fork is resolved against its recommendation and none by silence; where a later measurement contradicts a ratified pick, that is a new fork with a new id.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft. Duplication measured directly at b0108f13 rather than cited.
- rev-2 · 2026-09-02 · folded spec-audit round 1, findings B3 and B4. B3 measured `merge()`'s dedup
  as a basename-marker substring test, so rev-1's "call-site change, not a new capability" was
  inverted and its AC2 was unsatisfiable on any wired tree; S1 is corrected, S1b adds the missing
  capability and AC7 observes it. B4 corrected AC5's untracked `.claude/hooks/agent-cap.test.sh`
  to the tracked `tools/hooks/agent-cap.test.sh`. §10 corrected: the seam is not already sufficient.
- rev-3 · 2026-09-02 · folded spec-audit round 2, findings 7, 8, 25, 26, 30a and 30b. Finding 7: the round-1
  fold prepended its §10 correction in front of the text it refutes, leaving both verdicts and a
  truncated sentence; §10 is rewritten to one claim. Finding 8: S2 withdraws scratch-guard's wired
  copy too, and `tools/hooks/scratch-guard.test.sh:183-190` hard-FAILS on the resulting state — S3
  now names every parity arm and §7 names that leg. Findings 25 and 26: §7 carried
  `check-wiring self-test` twice from the leg rename and named no leg for the central change.
  30a: `HOOK_MARKER` is at `:49`, not `:53`. 30b: S1b's either/or is promoted to F0.

## 10. Reuse audit

`merge(obj, hook_path, frag)` at `tools/settings-merge.py:91` is the extension point, and
`reuse_lookup.py` reports the `agent-cap` affordance seam covering install and prefix concerns as
the corpus's nearest neighbour. It is NOT sufficient: the dedup at `:108-109` returns the object
unchanged whenever a command already contains the bare marker, so the seam is parameterised for the
FIRST write and not for a repath. S1b builds the missing mode; this unit extends a seam rather than
reusing one whole.

Recall terms used: `agent-cap`, `dual-ship`, `settings-merge`, `hook_path`, `wiring`, `parity`,
`destination`, `descriptor`, `withdrawal`, `adopter`, `prefix`, `carve-out`.
