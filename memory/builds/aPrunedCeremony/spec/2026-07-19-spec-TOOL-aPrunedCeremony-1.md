# TOOL-aPrunedCeremony-1 — manifest-driven gate legs + a no-hardcode canary

**Status:** CLOSED · rev-4 · 2026-07-19 · node a · Tier-2 · base bf7f2c22 · reviewed wf_2f11fd07,wf_539c5419 · ratified 2026-07-19

## 1. Goal

Generalize `tools/run-gates.sh` from a runner with ~14 hardcoded `leg "name" cmd...` calls to a thin
iterator over a single-source leg manifest (`tools/gate-legs.json`), guarded by a canary that fails
if a runner inlines a leg's script path instead of sourcing it from the manifest. This is the
reusable core of inCMS `ARCH-aTrimmedGauntlet-2`'s twin-runner design; a future PowerShell/CI runner
inherits the ready contract.

## 2. Scope (IN)

- S1 — `tools/gate-legs.json`: one array of legs, each `{name, argv, guard?}` — `argv` the command
  vector, optional `guard` the changed-path list that today drives `leg_if_changed`. LF-pinned via a
  new `.gitattributes` rule (`* text=auto` normalizes but does not force `eol=lf`).
- S2 — Rewrite `run-gates.sh` to parse the manifest via `"$PYBIN"` (resolved at run-gates.sh **L8**,
  not L7) and iterate, preserving the exact current SUMMARY shape, exit codes (0/1/2), stdin-denial
  (`</dev/null`, L19), and `leg_if_changed` semantics. Add a startup `command -v "$PYBIN"` probe that
  exits 2 with a clear message if absent, BEFORE any leg runs (the manifest parse hard-depends on
  Python; today only 2 of ~14 legs use `PYBIN`, with an unchecked fallback).
- S3 — **`$PYBIN` substitution rule (review wf_539c5419 TOOL-1-HIGH).** The two Python self-test legs
  run under the DYNAMICALLY-resolved `$PYBIN` (run-gates.sh L44-45), which is `python3` or the
  `python` fallback. The manifest stores the canonical literal `"python3"` as `argv[0]` for such
  legs; at exec time the runner substitutes the resolved `$PYBIN` for any `argv[0]` in
  `{python, python3}`. This preserves the python-fallback (so the legs run on a `python3`-absent host
  like this Windows node) AND keeps `argv[0]` inside the canary's allowed launcher set. Storing a
  bare `"$PYBIN"` token (canary-illegal) or a fixed `"python3"`/`"python"` literal (reds on Windows
  or on Debian CI respectively) are both wrong — hence the substitution.
- S4 — `tools/run-gates.test.sh`: a canary asserting, for each manifest leg, (a) `argv[0]` is an
  allowed launcher (`bash`/`python`/`python3`), (b) the manifest is non-empty, and (c) the leg's
  SCRIPT-PATH arguments (`argv[1..]`, e.g. `tools/codebase-map/selftest.py`) do NOT appear literally
  in the `run-gates.sh` body — proving the runner sources them from the manifest, not inline.
  Launcher tokens (`bash`/`python`/`python3`) and the parse-path code are excluded from the grep to
  avoid false positives (review wf_539c5419 TOOL-1-MED).
- S5 — Register the canary as a LEG ENTRY in `tools/gate-legs.json` (argv
  `["bash", "tools/run-gates.test.sh"]`) and name it in the `AGENTS.md` gate-suite list (L46-56);
  `run-gates.sh` itself gains no hardcoded leg (review wf_539c5419 TOOL-1-LOW).

## 3. Non-goals (OUT)

- No second (PowerShell) runner and no cross-runner byte-parity gate — a future addition.
- No diff-scope tier surface — `leg_if_changed` guards stay per-leg in the manifest;
  PLAY-aPrunedCeremony-2 governs the scoping DISCIPLINE.
- No change to WHICH legs run or their effective commands — a pure single-source refactor (the
  `$PYBIN` substitution preserves the current resolved behavior exactly).

## 4. Design

### Data model

`tools/gate-legs.json` — an ordered array; order is the run order:

```
[
  { "name": "memory hygiene (12 checks)", "argv": ["bash", "tools/memory-tree/check-memory-hygiene.sh"] },
  { "name": "codebase-map kit selftest", "argv": ["python3", "tools/codebase-map/selftest.py"] },
  { "name": "manifest-check self-test", "argv": ["bash", "skills/session-kickoff/manifest-check.test.sh"],
    "guard": ["skills/session-kickoff/manifest-check.sh", "skills/session-kickoff/manifest-check.test.sh"] },
  ...
]
```

Exec rule: a leg with `argv[0] ∈ {python, python3}` runs under the resolved `$PYBIN` (S3); all others
run `argv` verbatim (`leg()` L19 semantics). A leg with no `guard` always runs; a leg with `guard`
runs only when `changed()` (L15) reports a diff vs `GATE_BASE`.

### Inventory

| Item | Kind | Status |
|------|------|--------|
| `tools/gate-legs.json` | new data file (incl. the canary leg entry, S5) | to build |
| `tools/run-gates.sh` | rewritten iterator + `command -v "$PYBIN"` probe + `$PYBIN` substitution | edit |
| `tools/run-gates.test.sh` | new canary (S4) | to build |
| `.gitattributes` | add `tools/gate-legs.json text eol=lf` | edit |
| `AGENTS.md` gate-suite list | name the canary leg | edit |

### Migration

The manifest is generated from the current runner's leg list at build time (one-time hand port,
verified by diffing an old-vs-new `--list`/dry enumeration against the ~14 known legs). No consumer
migration — `bash tools/run-gates.sh` is unchanged for callers.

### Rollout

Doc/tooling only; lands on `main`. The canary self-test joins the gate suite in the same commit.

### Files touched (estimate)

4 files (2 new, 2 edited) + the AGENTS.md leg line. ~130 lines net.

### Alternatives rejected

- **Store `"$PYBIN"` or a fixed `"python3"`/`"python"` literal for the Python legs.** Rejected: the
  bare token is canary-illegal; a fixed literal reds on a standard platform (no correct single
  choice). The substitution rule (S3) is the only option preserving current behavior.
- **Full twin-runner + byte-parity gate now.** Deferred — no second runner yet.

## 5. Production-readiness checklist

- security — the manifest names commands the gate runs; tracked and reviewed like the runner. No new
  trust boundary.
- perf / scale — one JSON parse per run (negligible).
- a11y / i18n — N/A.
- error / empty / loading states — a malformed/empty manifest or an absent `$PYBIN` FAILS loudly
  (exit 2), never runs zero legs silently (green-by-absence, PLAY-aPrunedCeremony-3).
- observability — SUMMARY shape byte-preserved. (Cross-shell byte parity is N/A — one bash runner.)
- risks — the refactor escalates Python from a soft 2-leg dep to a hard parser dep; the startup probe
  (S2) mitigates. The `$PYBIN` substitution (S3) is the load-bearing correctness rule — its own AC
  (AC5) guards it.
- testing + left-shift gates — S4 canary is the left-shift.
- migration / rollback — revert to the hardcoded runner; the manifest is inert data.
- user docs — `AGENTS.md` gate-suite section names the manifest as the leg source.

## 6. Acceptance criteria

- AC1 — When `bash tools/run-gates.sh` runs after the rewrite, it produces the same per-leg lines,
  SUMMARY, and exit code as the pre-change runner on a clean tree (green) and on an injected leg
  failure (red, naming the leg).
- AC2 — When a leg's script path is hardcoded into `run-gates.sh` outside the parse path,
  `tools/run-gates.test.sh` reds naming the offending path.
- AC3 — When `tools/gate-legs.json` is emptied or malformed, OR `"$PYBIN"` is absent, the runner
  exits non-zero with a clear message and runs zero legs — never prints "gates GREEN".
- AC4 — When `check-kit-versions.sh` and the memory-tree hygiene gate run, both stay green.
- AC5 — When `run-gates.sh` runs on a host where `python3` is absent from PATH (PYBIN resolves to
  `python`), the two Python self-test legs still execute under `python` — the manifest's `"python3"`
  literal is substituted, not run verbatim.

## 7. Gates

The existing gate suite (`run-gates.sh` self-hosts), plus the new `run-gates.test.sh` canary leg;
`.gitattributes` LF verification on `tools/gate-legs.json`.

## 8. Open questions

none — both forks below are RESOLVED (owner, 2026-07-19); kept for the record.

- **Fork A — build-both or defer-both.** RESOLVED (owner, 2026-07-19): BUILD the manifest+canary
  pair, overriding the defer recommendation.
- **Fork B — JSON or a line-based manifest?** RESOLVED (recommended): JSON via the required Python
  (CRLF-immune, structured), not line-oriented `sh` extraction.

## 9. Revision log

- rev-1 · 2026-07-19 · initial draft.
- rev-2 · 2026-07-19 · folded wf_2f11fd07: withdrew the incoherent canary-only fallback; corrected the
  PYBIN citation + soft-dep claim; added the `.gitattributes` pin.
- rev-3 · 2026-07-19 · owner ratified Fork A → BUILD; status → INPROGRESS.
- rev-4 · 2026-07-19 · folded pre-code review wf_539c5419: added the `$PYBIN` substitution rule (S3,
  the two Python legs were non-representable and would red the gate on a standard platform); pinned
  the canary grep to `argv[1..]` script paths excluding launchers (S4); corrected S5 — the canary is
  a `gate-legs.json` entry, not a `run-gates.sh` leg; added AC5.
