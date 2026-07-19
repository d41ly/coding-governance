# TOOL-aPrunedCeremony-1 — manifest-driven gate legs + a no-hardcode canary

**Status:** SPECCED · rev-2 · 2026-07-19 · node a · Tier-2 · base bf7f2c22 · reviewed wf_2f11fd07

## 1. Goal

Generalize `tools/run-gates.sh` from a runner with ~14 hardcoded `leg "name" cmd...` calls to a thin
iterator over a single-source leg manifest (`tools/gate-legs.json`), guarded by a canary that fails
if a runner inlines a leg command instead of sourcing it. This is the reusable core of inCMS
`ARCH-aTrimmedGauntlet-2`'s twin-runner design. The honest caveat, stated up front and sharpened in
rev-2: the manifest and the canary are COUPLED (the canary asserts the runner sources the manifest),
so the real choice is build-both or build-nothing — and with no second runner to keep in lockstep,
the recommendation is to DEFER the whole unit (§8 Fork A).

## 2. Scope (IN)

- S1 — `tools/gate-legs.json`: one array of legs, each `{name, argv, guard?}` — `argv` the command
  vector, optional `guard` the changed-path list that today drives `leg_if_changed`. LF-pinned in
  `.gitattributes` (runtime-read JSON; add an explicit rule — `* text=auto` normalizes but does not
  force `eol=lf`).
- S2 — Rewrite `run-gates.sh` to parse the manifest via `"$PYBIN"` (resolved at run-gates.sh **L8**,
  not L7) and iterate, preserving the exact current SUMMARY shape, exit codes (0/1/2), stdin-denial
  (`</dev/null`, L19), and `leg_if_changed` semantics. Because the parse makes Python a HARD startup
  dependency (today it is SOFT — only 2 of ~14 legs use `PYBIN`, and L8's fallback is unchecked), add
  a startup `command -v "$PYBIN"` probe that exits 2 with a clear message if absent (review
  R-TOOL-1-MED).
- S3 — `tools/run-gates.test.sh`: a canary asserting (a) every manifest leg's `argv[0]` is an allowed
  launcher (`bash`/`python`/`python3`), (b) the manifest is non-empty, and (c) the runner body sources
  the manifest and contains no inlined leg-command string outside the parse path.
- S4 — Register the new self-test leg in the gate suite (`run-gates.sh` + `AGENTS.md`).

## 3. Non-goals (OUT)

- No second (PowerShell) runner and no cross-runner byte-parity gate — that is the payoff this unit
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
| `tools/run-gates.sh` | rewritten iterator + `command -v "$PYBIN"` startup probe | edit |
| `tools/run-gates.test.sh` | new canary | to build |
| `.gitattributes` | add `tools/gate-legs.json text eol=lf` | edit |
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
  one bash runner.
- **"Defer the manifest, adopt only the canary" (rev-1's fallback).** WITHDRAWN — it was incoherent:
  the S3 canary asserts the runner SOURCES the manifest, so it cannot exist without the manifest
  (review R-TOOL-1-HIGH). A manifest-independent variant is possible (a test that greps the runner
  for known leg-command strings against a hand-maintained list) but it is a second hand-kept copy —
  weaker than either building both or deferring both. So the real fork is build-both vs
  build-nothing (§8 Fork A).

## 5. Production-readiness checklist

- security — the manifest names commands the gate runs; it is tracked and reviewed like the runner.
  No new trust boundary (same commands, relocated).
- perf / scale — neutral; one JSON parse per gate run (negligible vs the legs).
- a11y / i18n — N/A.
- error / empty / loading states — a malformed or empty manifest must FAIL loudly (exit 2), never
  run zero legs silently (green-by-absence, PLAY-aPrunedCeremony-3); the `command -v "$PYBIN"` probe
  must fail closed when Python is absent rather than skipping the parse.
- observability — SUMMARY shape is byte-preserved so existing transcript expectations hold. (Byte
  parity across shells — the inCMS PARITY-1 Write-Host/stream/newline hazard — is N/A here: one bash
  runner, no PowerShell twin.)
- risks — the refactor silently ESCALATES Python from a soft 2-leg dependency to a hard all-legs
  parser dependency; the startup probe (S2) is the mitigation. If the manifest and the runner's parse
  expectations drift, the canary (S3) catches it.
- testing + left-shift gates — S3 canary is the left-shift; it also asserts the manifest is non-empty
  and every `argv[0]` is an allowed launcher.
- migration / rollback — revert to the hardcoded runner; the manifest is inert data.
- user docs — update `AGENTS.md` gate-suite section to name the manifest as the leg source.

## 6. Acceptance criteria

- AC1 — When `bash tools/run-gates.sh` runs after the rewrite, it produces the same per-leg lines,
  SUMMARY, and exit code as the pre-change runner on a clean tree (green) and on an injected leg
  failure (red, naming the leg).
- AC2 — When a leg command is hardcoded into `run-gates.sh` outside the manifest-parse path,
  `tools/run-gates.test.sh` reds naming the offending string.
- AC3 — When `tools/gate-legs.json` is emptied or malformed, OR `"$PYBIN"` is absent, the runner
  exits non-zero with a clear message and runs zero legs — never prints "gates GREEN".
- AC4 — When `check-kit-versions.sh` and the memory-tree hygiene gate run, both stay green.

## 7. Gates

The existing gate suite (`run-gates.sh` self-hosts), plus the new `run-gates.test.sh` canary leg;
`.gitattributes` LF verification on `tools/gate-legs.json`.

## 8. Open questions

- **Fork A — build-both or defer-both (owner menu 1; rev-2 reframe).** The manifest and canary are
  coupled, so this is NOT "manifest vs canary" — it is build the pair or build nothing. RECOMMEND:
  DEFER the pair. The manifest's only payoff is a second runner staying in lockstep, and there is
  none; the CI-wiring follow-up (AGENTS.md L58) runs the SAME `run-gates.sh`, so it is not a second
  consumer. Building now is speculative generality — the exact call inCMS's own closing review would
  flag. Revisit the day a PowerShell runner or an independent CI runner is added.
- **Fork B — if built, JSON or a line-based manifest?** RECOMMEND: JSON via the required Python
  (CRLF-immune, structured), not line-oriented `sh` extraction (a stray CR breaks it, §11).

## 9. Revision log

- rev-1 · 2026-07-19 · initial draft (node a, aPrunedCeremony).
- rev-2 · 2026-07-19 · folded review wf_2f11fd07: withdrew the incoherent "canary-only" fallback (the
  canary is manifest-dependent) and reframed Fork A as build-both vs defer-both; corrected the PYBIN
  citation (L8, not L7) and the false "Python already a hard requirement" claim — it is soft today,
  the manifest makes it hard, so a startup `command -v` probe is added; added the explicit
  `.gitattributes` LF pin for the manifest; status → SPECCED.
