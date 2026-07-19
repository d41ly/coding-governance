# TOOL-aPrunedCeremony-2 — pre-push full-gate enforcement (drift signal N/A here)

**Status:** OPEN · rev-1 · 2026-07-19 · node a · Tier-2 · base bf7f2c22

## 1. Goal

Give coding-governance the machine-enforced push boundary that PLAY-aPrunedCeremony-1 makes the
authoritative gate: a tracked `.githooks/pre-push` that runs the full `tools/run-gates.sh` on a push
to `main` and blocks a red push. This is the enforcement half of inCMS `ARCH-aTrimmedGauntlet-2`.
The other half of the inCMS work — a hook-staleness drift signal — is deliberately NOT ported: it
existed because inCMS COPIES hooks to an out-of-tree dir that goes stale, whereas coding-governance
points `core.hooksPath` at the tracked `.githooks/` directly, so there is no copy to drift and
`check-wiring.sh` already auto-wires an unset path.

## 2. Scope (IN)

- S1 — `.githooks/pre-push`: on a push whose ref set includes `refs/heads/main`, run
  `bash tools/run-gates.sh` (full) and exit non-zero (blocking the push) if it reds; on any other
  ref, do nothing. Classify by reading stdin ref lines; run the gate ONCE after the classify loop,
  with the gate's stdin redirected (`</dev/null`) so it cannot consume remaining ref lines.
- S2 — Preconditions before running: the hook runs in the tree the push originates from; assert a
  clean-enough tree per the existing branch-guard conventions and fail closed with a one-line
  message pointing the user to push `main` from the primary tree.
- S3 — `.githooks/pre-push.test.sh`: a scratch-repo fixture driving `git push` against a local bare
  remote through the hook, covering — docs-only-ok push blocked-if-red, non-`main` ref skips, a
  multi-ref push, and a stubbed gate via an env seam so the test never runs the real ~multi-second
  bar. Joins the gate suite.
- S4 — Wire the new self-test into `tools/run-gates.sh` (the gate suite) and `AGENTS.md`.
- S5 — Record, in the hook header and this repo's AGENTS.md, that the drift-signal is N/A for the
  tracked-dir hook model (with the one-line reason), so a future reader does not "helpfully" add it.

## 3. Non-goals (OUT)

- No hook-staleness drift signal / hash-of-installed-vs-tracked check — N/A for this repo's model
  (§4 Rollout), and `check-wiring.sh` already covers the analogous "dormant hooks" concern.
- No diff-scoping in the pre-push path — a push to `main` runs the FULL bar (that is the whole point
  of the boundary); scoped runs are the earlier DoR/merge runs (PLAY-aPrunedCeremony-1/-2).
- No CI wiring — running `run-gates.sh` in CI is a separate open follow-up (AGENTS.md L58); this
  spec is the local push hook only.

## 4. Design

### Data model

N/A — a shell hook + its test.

### Inventory

| Item | Kind | Status |
|------|------|--------|
| `.githooks/pre-push` | new tracked hook | to build |
| `.githooks/pre-push.test.sh` | new fixture | to build |
| `.gitattributes` | already pins `.sh`/hook files LF — verify `pre-push` matches | verify |
| `tools/run-gates.sh` + `AGENTS.md` | register the self-test leg | edit |

### Migration

None. On adoption each node already has `core.hooksPath=.githooks` (set by `check-wiring.sh` on
SessionStart, or `git config core.hooksPath .githooks`), so the new tracked `pre-push` activates on
the next push with NO per-node install step — unlike inCMS's copy model. This is the concrete reason
the drift signal is unnecessary here.

### Rollout

Lands on `main`. Because the hook is the tracked file the runner reads (not a copy), there is no
inert-until-reinstalled window; the SessionStart `check-wiring.sh` self-heal covers a fresh clone
whose `core.hooksPath` is unset. Risk of the boundary being dormant is therefore already gated —
which is exactly why inCMS's drift-signal does not port.

### Files touched (estimate)

2 new + 2 edited. ~90 lines.

### Alternatives rejected

- **Port the inCMS drift-signal too.** Rejected: it detects a stale COPY at an out-of-tree
  hooksPath; here hooksPath IS the tracked dir, so tracked==active by construction. Porting it would
  add a check that can never fire (or fires falsely) — itself the vacuous-gate class
  (PLAY-aPrunedCeremony-3).
- **Run the gate inside the per-ref read loop.** Rejected: a gate spawned inside `while read`
  inherits stdin and can swallow the remaining ref lines (the inCMS MECH-8 catch) — classify in the
  loop, run once after with stdin denied.
- **Make it a `pre-commit` extension instead of `pre-push`.** Rejected: the boundary is the push to
  shared `main`, not the local commit; commits stay fast (the existing pre-commit fast leg).

## 5. Production-readiness checklist

- security — the hook runs repo-local gate scripts already trusted; no new external surface.
- perf / scale — the full bar runs once per `main` push (~the suite's wall time); non-`main` pushes
  and all commits are unaffected. This is the cost the boundary trades for killing the triple-run.
- a11y / i18n — N/A.
- error / empty / loading states — a gate red must block with a clear message and the failing leg;
  `--no-verify` remains the deliberate operator bypass (consistent with the pre-commit guard).
- observability — the hook prints which run it is doing ("pre-push: full gate on main push") so a
  blocked push is self-explanatory in the transcript.
- risks — (a) the hook runs in whatever tree the push originates from, not necessarily the pushed
  tip — S2's clean-tree precondition + "push main from the primary tree" message bound this; (b) a
  multi-ref push must not let the gate eat ref lines — S1's stdin-deny + classify-then-run.
- testing + left-shift gates — S3's scratch-repo fixture is the left-shift; it must drive a real
  `git push` so it proves the hook FIRES (not just that the script exits right) — the "prove it
  catches" rule (PLAY-aPrunedCeremony-3).
- migration / rollback — delete the hook file; `core.hooksPath` and the pre-commit guard are
  unaffected.
- user docs — AGENTS.md gate-suite section notes the pre-push boundary and the drift-signal-N/A
  rationale (S5).

## 6. Acceptance criteria

- AC1 — When a push to `main` is attempted with a red gate (in the fixture, a stubbed-red gate), the
  push is blocked with a non-zero hook exit naming the failing leg.
- AC2 — When a push to a non-`main` ref runs, the hook does nothing and the push proceeds.
- AC3 — When a multi-ref push including `main` runs, the gate runs exactly once and classification is
  not corrupted by stdin consumption (fixture case).
- AC4 — When `.githooks/pre-push.test.sh` runs in the gate suite, it drives a real `git push`
  through the hook against a bare scratch remote and passes.
- AC5 — When the hook header and AGENTS.md are read, they record that the drift signal is N/A for the
  tracked-dir hook model, with the reason.

## 7. Gates

The gate suite plus the new `.githooks/pre-push.test.sh` leg; `.gitattributes` LF check on the hook
file. The pre-push hook itself becomes the enforcement gate PLAY-aPrunedCeremony-1 references.

## 8. Open questions

- **Fork A — adopt the pre-push hook (owner menu 2).** RECOMMEND: yes — small, high-value, and it is
  what makes PLAY-aPrunedCeremony-1's boundary machine-enforced rather than a convention. Without
  it, "the full bar runs at the push boundary" is honor-system.
- **Fork B — confirm drift-signal N/A (owner menu 3).** RECOMMEND: record N/A and do not port — the
  tracked-dir model plus `check-wiring.sh` already covers the dormant-hook concern the signal
  addressed. If coding-governance ever switches to a copy-install model, revisit.
- **Fork C — clean-tree precondition strictness.** RECOMMEND: reuse the existing branch-guard's
  notion of an acceptable tree rather than invent a new one, so the two hooks agree.

## 9. Revision log

- rev-1 · 2026-07-19 · initial draft (node a, aPrunedCeremony).
