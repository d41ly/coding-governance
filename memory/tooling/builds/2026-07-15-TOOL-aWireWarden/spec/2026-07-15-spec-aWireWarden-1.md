# TOOL-aWireWarden-1 — Wiring-health check + SessionStart nudge for per-clone tool wiring

**Status:** INPROGRESS · rev-3 · 2026-07-15 · node a · Tier-2 · base 06f5632f · review wf_f0164aef · ratified 2026-07-15

## 1. Goal

Detect coding-governance tools that are installed in a repo but not wired, and surface or auto-wire
them once per session so a fresh clone never runs with dormant gates. The motivating case:
`core.hooksPath` is per-clone git config that git never sets on clone, so every fresh checkout starts
with all `.githooks/` gates — including the branch guard — silently inert.

## 2. Scope (IN)

- S1 `tools/check-wiring.sh` with three modes. `--check` (default) reports each installed-but-unwired
  tool with its exact fix command and exits 1 when any is unwired. `--fix` performs the zero-risk
  wiring and prints what it changed. `--session` performs the same zero-risk wiring, prints a one-line
  result, and always exits 0; it is the only mode the SessionStart hook calls.
- S2 Check H (hooks): installed when a tracked `.githooks/pre-commit` exists; wired when
  `git config core.hooksPath` is set and resolves to a directory that contains an executable
  `pre-commit`. `--fix` and `--session` run `git config core.hooksPath .githooks` only when
  `core.hooksPath` is unset or empty, and never overwrite an already-set different value — they report
  that value instead.
- S3 Check A (agent-cap): installed when `.claude/hooks/agent-cap.js` exists; wired when
  `python tools/settings-merge.py --check` exits 0. No mode mutates `settings.json`; `--fix` and
  `--session` print the `settings-merge.py` command to run. Agent-cap wiring is never auto-applied,
  because the SessionStart hook must not rewrite the file it lives in.
- S4 A SessionStart hook entry in cg's `.claude/settings.json` that runs `check-wiring.sh --session`.
  The hook auto-wires only the zero-risk `core.hooksPath` case and exits 0 unconditionally.
- S5 Wire agent-cap on cg (Fork 2): place `agent-cap.js` at `.claude/hooks/agent-cap.js` and run
  `python tools/settings-merge.py` so the agent-cap PreToolUse hook and the SessionStart nudge coexist
  in one `.claude/settings.json`.
- S6 `tools/check-wiring.test.sh` — fixture self-test covering the safety-critical paths, wired as a
  `run-gates.sh` leg.
- S7 A `KIT_CHECK_WIRING_VERSION` constant (check-wiring.sh deploys into target repos via
  WIRE-INTO-PROJECT.md, so it follows the versioned-deployed-tool pattern), a WIRE-INTO-PROJECT.md
  section, an AGENTS.md gate-suite line, and the manifest `last-audit` re-stamp the `run-gates.sh`
  touch forces.

## 3. Non-goals (OUT)

- No general environment or toolchain doctor — encoding, ports, and toolchain-presence health — which
  was assessed and declined as inCMS-specific in TOOL-aWardenGraft-1. This unit checks WIRING only.
- No auto-mutation of `settings.json` from any mode. `core.hooksPath` is the only value `--session`
  and `--fix` write, and only when unset. Agent-cap wiring stays a printed instruction.
- No re-implementation of agent-cap wiring detection. Check A delegates to `settings-merge.py --check`,
  which is a structural JSON test, so the wired-signal lives in exactly one place.
- No `check-kit-versions.sh` entry for the new version constant — it follows `manifest-check.sh`,
  which carries a version constant without a `check-kit-versions.sh` line.
- No process-global auto-fix env knob. Auto-fix scope is the per-repo committed SessionStart hook
  itself, never a shell-wide `GOV_WIRING_AUTOFIX` that would arm hooks across unrelated clones.

## 4. Design

`check-wiring.sh` resolves the repo root from `git rev-parse --show-toplevel` and runs an ordered
list of independent checks, each emitting one status line of `ok`, `UNWIRED`, or `skip`. In `--check`
only `UNWIRED` sets a failure exit. `--fix` runs the safe wiring action for each check that declares
one, then re-reports, exiting non-zero only if something unwired remains. `--session` is `--fix` that
always exits 0, for use where a non-zero result must not disturb session start. The script is bash
with stdlib git only and prints ASCII markers so it is safe on any console.

### Inventory

| Check | Installed signal | Wired signal | Auto-fix action (`--fix` / `--session`) | Risk |
|---|---|---|---|---|
| H hooks | tracked `.githooks/pre-commit` | `core.hooksPath` resolves to a dir holding an executable `pre-commit` | set `core.hooksPath .githooks` ONLY when unset/empty | opts into running repo hooks — a trust boundary |
| A agent-cap | `.claude/hooks/agent-cap.js` present | `settings-merge.py --check` exits 0 | none, prints the `settings-merge.py` command | `settings.json` mutation, never auto-applied |

Check H's wired test resolves both the configured value and the candidate dir to an absolute path
before comparing, so `.githooks`, `./.githooks`, a trailing slash, and the out-of-tree absolute copy
WIRE-INTO-PROJECT.md §5 recommends for multi-worktree repos all read as WIRED. Auto-fix never rewrites
a non-empty `core.hooksPath`; against the §5 out-of-tree setup it is a no-op, so it cannot undo that
hardening. A check whose installed signal is absent prints `skip` and never fails, so a repo that has
not adopted a tool stays green. `.githooks` is hardcoded as the fix target — it is the fixed hooks-dir
name used in `.githooks/pre-commit`, `run-gates.sh`, and WIRE-INTO-PROJECT.md §5.

### Rollout

The SessionStart hook lives in cg's `.claude/settings.json`, created by this unit alongside the
agent-cap PreToolUse hook. The hook command is `bash "${CLAUDE_PROJECT_DIR}/tools/check-wiring.sh"
--session`, which auto-wires the hooks case and always exits 0. The hook runs committed script;
Claude Code's folder-trust prompt is the gate that makes that acceptable, and the settings-json
no-write rule (S3) keeps the hook from rewriting its own file. This channel reaches Claude Code
session starts only — a maintainer committing with plain git never sees it, a known efficacy gap
accepted here rather than met with a second delivery channel. Auto-fix is confined to the fresh-clone
`core.hooksPath`-unset case, which is precisely the dormant-guard scenario the unit targets.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/check-wiring.sh` | new — the checker, with `KIT_CHECK_WIRING_VERSION` |
| `tools/check-wiring.test.sh` | new — fixture self-test |
| `.claude/hooks/agent-cap.js` | new — cg's adopted copy of the agent-cap kit |
| `.claude/settings.json` | new — SessionStart `--session` hook + agent-cap PreToolUse hook |
| `tools/run-gates.sh` | add the `check-wiring self-test` leg, a watched-file touch |
| `AGENTS.md` | gate-suite line and the SessionStart nudge note |
| `WIRE-INTO-PROJECT.md` | a numbered section promoting this from the §5 placeholder |
| `.claude/SESSION-KICKOFF.md` | `last-audit` re-stamp for the `run-gates.sh` touch |

### Alternatives rejected

Baking auto-wiring into the `/session-kickoff` engine is rejected: the engine is project-agnostic and
machine-shared, so cg-specific tool knowledge violates the `CLAUDE.md > manifest > skill` separation.
A full env-doctor is rejected in TOOL-aWardenGraft-1. Making `core.hooksPath` a tracked value is
impossible by git's design. Shrinking the unit to a single `run-gates.sh` warning was weighed in §8
fork 3 and rejected: a merge-bar leg would false-warn in CI where `core.hooksPath` is correctly unset.

## 5. Production-readiness checklist

- security: the only auto-written value is local `core.hooksPath`, set only when unset and never
  overwriting a deliberate value, gated per-repo by the committed hook and by Claude Code folder-trust.
  Agent-cap wiring is never auto-applied. If the committed script were attacker-modified in a branch
  the hook would run it, so the no-config-write-beyond-hooksPath rule is the containment.
- perf / scale: a handful of `git config` reads and file-existence tests; the `--session` path stays
  well under a session-start latency budget.
- a11y: N/A — a non-interactive CLI tool.
- i18n: N/A — operator-facing ASCII diagnostics.
- error / empty / loading states: not-a-git-repo, a missing `.githooks`, a missing `settings.json`,
  and a missing bash launcher each resolve to skip-or-noop, never a crash or a broken session start.
- observability: one status line per check plus the fix command printed on any unwired result.
- risks: a SessionStart hook that hung or spewed could disturb session start, mitigated by bounded
  git/file ops and the always-zero `--session`; the clobber hazard is mitigated by the set-only-when-
  unset invariant.
- testing + left-shift gates: `check-wiring.test.sh` on temp-repo fixtures, riding `run-gates.sh`.
- migration / rollback: additive; rollback is deleting the files and unsetting `core.hooksPath`.
- user docs: the WIRE-INTO-PROJECT.md section and the AGENTS.md gate-suite line.

## 6. Acceptance criteria

- AC1 When `core.hooksPath` is unset in a clone whose `.githooks/pre-commit` is tracked, `bash
  tools/check-wiring.sh --check` prints the hooks check as UNWIRED with its fix command and exits 1.
- AC2 When `bash tools/check-wiring.sh --fix` runs in that state, `git config core.hooksPath` becomes
  `.githooks` and a re-run of `--check` exits 0.
- AC3 When `core.hooksPath` already points at a valid out-of-tree hooks dir, `--check` reports the
  hooks check WIRED and neither `--fix` nor `--session` changes the value.
- AC4 When `core.hooksPath` is set to an equivalent-but-non-literal value such as `./.githooks`,
  `--check` reports the hooks check WIRED.
- AC5 When every installed tool is wired, `--check` prints only ok and skip lines and exits 0; in a
  non-git dir and a repo with no `.githooks`, every check prints skip and the exit is 0.
- AC6 `bash tools/check-wiring.sh --session` auto-wires an unset `core.hooksPath` to `.githooks` and
  exits 0, and still exits 0 when Check A remains unwired.
- AC7 `bash tools/check-wiring.test.sh` exercises AC1 through AC6 plus the agent-cap-adopted-but-unwired
  path, and is a green leg of `bash tools/run-gates.sh`.
- AC8 After the build, cg's `.claude/settings.json` carries both the SessionStart `--session` hook and
  the agent-cap PreToolUse hook, and `python tools/settings-merge.py --check` exits 0.

## 7. Gates

- The full `bash tools/run-gates.sh` suite stays green, extended by one leg named
  `check-wiring self-test`.
- Memory hygiene stays green, including this spec under check 12.
- The kickoff-manifest ratchet stays green; the `run-gates.sh` edit is a watched-file touch closed by
  a bundled `last-audit` re-stamp.

## 8. Open questions

### Fork 1 — SessionStart hook: nudge-only or auto-fix

RESOLVED (owner, 2026-07-15): auto-fix on session start. The SessionStart hook runs `--session`, which
auto-wires the hooks case when `core.hooksPath` is unset, never overwrites a set value, and always
exits 0. No process-global `GOV_WIRING_AUTOFIX` env — the per-repo committed hook is itself the
per-repo gate, which answers the security review's granularity objection.

### Fork 2 — dogfood scope of the new `.claude/settings.json`

RESOLVED (owner, 2026-07-15): also wire agent-cap on cg. This build places `agent-cap.js` at
`.claude/hooks/` and runs `settings-merge.py`, so cg dogfoods the fan-out cap it ships; the agent-cap
PreToolUse hook and the SessionStart nudge share one `.claude/settings.json`.

### Fork 3 — full machinery or a minimal run-gates warning

RESOLVED (owner, 2026-07-15): full machinery. check-wiring ships to adopter repos, the multi-clone
case where the value lives — the same rationale under which cg ships every kit it cannot fully
dogfood. The `run-gates.sh` warning alternative was rejected because a merge-bar leg would false-warn
in CI where `core.hooksPath` is correctly never set.

## 9. Revision log

- rev-1 · 2026-07-15 · initial draft.
- rev-2 · 2026-07-15 · folded review wf_f0164aef: path-aware Check H with never-clobber auto-fix;
  Check A delegates to `settings-merge.py --check`; added always-zero hook mode; added a version
  constant; dropped `GOV_HOOKS_DIR` and `GOV_WIRING_AUTOFIX`; added scope fork 3 and ACs for
  out-of-tree, non-literal, and skip paths.
- rev-3 · 2026-07-15 · owner ratified §8: auto-fix on session start via `--session` (fork 1), wire
  agent-cap on cg (fork 2), full machinery (fork 3); status to INPROGRESS; build underway.
