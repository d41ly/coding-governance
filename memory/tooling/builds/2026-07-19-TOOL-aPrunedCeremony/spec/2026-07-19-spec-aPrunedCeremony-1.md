# TOOL-aPrunedCeremony-1 — manifest-driven gate legs + a no-hardcode canary

**Status:** OPEN · rev-1 · 2026-07-19 · node a · Tier-2 · base bf7f2c22

## 1. Goal

Generalize `tools/run-gates.sh` from a runner with ~14 hardcoded `leg "name" cmd...` calls to a thin
iterator over a single-source leg manifest (`tools/gate-legs.json`), guarded by a canary test that
fails if any runner inlines a leg command instead of sourcing it. This is the reusable core of
inCMS `ARCH-aTrimmedGauntlet-2`'s twin-runner design. The honest caveat, stated up front: the full
value (a second runner staying byte-identical) only materializes with a SECOND consumer; for a
single bash runner this is a refactor, not a capability gain — hence the §8 defer recommendation.

## 2. Scope (IN)

- S1 — `tools/gate-legs.json`: one array of legs, each `{name, argv, guard?}` — `argv` the command
  vector, optional `guard` the changed-path list that today drives `leg_if_changed`. LF-pinned in
  `.gitattributes` (runtime-read JSON, §11).
- S2 — Rewrite `run-gates.sh` to parse the manifest (via the Python already required — `PYBIN` at
  L7) and iterate, preserving the exact current SUMMARY shape, exit codes (0/1/2), stdin-denial
  (`</dev/null`, L19), and `leg_if_changed` semantics.
- S3 — `tools/run-gates.test.sh`: a canary asserting (a) every manifest leg's `argv[0]` is an
  allowed launcher (`bash`/`python`/`python3`), and (b) no leg-command string is hardcoded in the
  runner body outside the manifest-parse path — the drift guard.
- S4 — Register the new legs (self-test) in the gate suite (`AGENTS.md` §"gate suite" + the runner
  itself dogfoods it).

## 3. Non-goals (OUT)

- No second (PowerShell) runner and no cross-runner byte-parity gate — that is the payoff this spec
  DEFERS. Building the twin without a consumer is the over-engineering inCMS's own review flagged.
- No diff-scope tier surface (`gate-scope.json`) — `leg_if_changed` guards stay per-leg in the
  manifest; PLAY-aPrunedCeremony-2 governs the scoping DISCIPLINE, not a new artifact.
- No change to WHICH legs run or their commands — a pure single-source refactor.

## 4. Design

### Data model

`tools/gate-legs.json` — an ordered array; order is the run order:

```
[
  { "name": "memory hygiene (12 checks)", "argv": ["bash", "tools/memory-tree/check-memory-hygiene.sh"] },
  { "name": "manifest-check self-test", "argv": ["bash", "skills/session-kickoff/manifest-check.test.sh"],
    "guard": ["skills/session-kickoff/manifest-check.sh", "skills/session-kickoff/manifest-check.test.sh"] },
  ...
]
```

A leg with no `guard` always runs; a leg with `guard` runs only when `changed()` (L15) reports a
diff in any guard path vs `GATE_BASE` — identical to today's `leg_if_changed`.

### Inventory

| Item | Kind | Status |
|------|------|--------|
| `tools/gate-legs.json` | new data file | to build |
| `tools/run-gates.sh` | rewritten iterator | edit |
| `tools/run-gates.test.sh` | new canary | to build |
| `.gitattributes` | LF pin for `tools/gate-legs.json` | edit |
| `AGENTS.md` gate-suite list | add the canary leg | edit |

### Migration

The manifest is generated from the current runner's leg list at build time (one-time hand port,
verified by diffing a `--list` of old vs new against the ~14 known legs). No consumer migration —
`bash tools/run-gates.sh` is unchanged for callers.

### Rollout

Doc/tooling only; lands on `main`. The canary self-test joins the gate suite in the same commit.

### Files touched (estimate)

4 files (2 new, 2 edited) + the AGENTS.md leg line. ~120 lines net.

### Alternatives rejected

- **Full twin-runner + byte-parity gate now (the inCMS shape).** Rejected as premature: inCMS needed
  gate.sh AND gate.ps1 because it runs on POSIX and Windows dev nodes; coding-governance's gate is
  one bash runner. Ship the manifest + canary (which a future twin would need anyway) and stop.
- **Keep hardcoded legs, add only the canary.** Viable and cheaper — the canary alone catches an
  inlined command. Offered as the fallback in §8; the manifest is what a second runner needs, so it
  is the forward-looking half.

## 5. Production-readiness checklist

- security — the manifest is code-adjacent (it names commands the gate runs); it is tracked and
  reviewed like the runner. No new trust boundary (same commands, relocated).
- perf / scale — neutral; one JSON parse per gate run (negligible vs the legs).
- a11y / i18n — N/A.
- error / empty / loading states — a malformed manifest must FAIL the runner loudly (exit 2, like
  "not a git repo"), never run zero legs silently (the green-by-absence class, §10 / PLAY-3).
- observability — SUMMARY shape is byte-preserved so existing transcript expectations hold.
- risks — the parse step depends on Python (already a hard requirement, L7). If the manifest and the
  runner's parse expectations drift, the canary (S3) catches it.
- testing + left-shift gates — S3 canary is the left-shift; it also asserts the manifest is
  non-empty and every `argv[0]` is an allowed launcher.
- migration / rollback — revert to the hardcoded runner; the manifest is inert data.
- user docs — update `AGENTS.md` gate-suite section to name the manifest as the leg source.

## 6. Acceptance criteria

- AC1 — When `bash tools/run-gates.sh` runs after the rewrite, it produces the same per-leg lines,
  SUMMARY, and exit code as the pre-change runner on a clean tree (green) and on an injected leg
  failure (red, naming the leg).
- AC2 — When a leg command is hardcoded into `run-gates.sh` outside the manifest-parse path,
  `tools/run-gates.test.sh` reds naming the offending string.
- AC3 — When `tools/gate-legs.json` is emptied or malformed, the runner exits non-zero with a clear
  message and runs zero legs — never prints "gates GREEN".
- AC4 — When `check-kit-versions.sh` and the memory-tree hygiene gate run, both stay green.

## 7. Gates

The existing gate suite (`run-gates.sh` self-hosts), plus the new `run-gates.test.sh` canary leg.
`.gitattributes` LF verification on `tools/gate-legs.json` (§11 staged-bytes check).

## 8. Open questions

- **Fork A — build now or defer (owner menu 1).** RECOMMEND: DEFER the manifest; adopt only the
  canary (S3) over the current hardcoded runner if any hardening is wanted now. Rationale: the
  manifest's payoff is a second runner staying in lockstep, and there is no second runner. Building
  it now is speculative generality — the exact call inCMS's own closing review would flag. Revisit
  the day a PowerShell runner or a CI matrix runner is added.
- **Fork B — if built, JSON or a simpler line-based manifest?** RECOMMEND: JSON parsed via the
  already-required Python (CRLF-immune, structured), not line-oriented `sh` extraction (which a
  stray CR breaks, §11).

## 9. Revision log

- rev-1 · 2026-07-19 · initial draft (node a, aPrunedCeremony).
