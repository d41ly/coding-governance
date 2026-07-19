# TOOL-aPrunedCeremony-2 — pre-push full-gate enforcement (drift signal scoped, not dropped)

**Status:** INPROGRESS · rev-2 · 2026-07-19 · node a · Tier-2 · base bf7f2c22 · reviewed wf_2f11fd07 · ratified 2026-07-19

## 1. Goal

Give coding-governance the machine-enforced push boundary that PLAY-aPrunedCeremony-1 makes the
authoritative gate: a tracked `.githooks/pre-push` that runs the full `tools/run-gates.sh` on a push
to `main` and blocks a red push. This is the enforcement half of inCMS `ARCH-aTrimmedGauntlet-2`.
The inCMS hook-staleness drift signal is NOT ported for THIS repo's direct-wire dogfood (where
`core.hooksPath` points at the tracked `.githooks/` so tracked == active) — but rev-2 corrects the
rev-1 over-claim that it is N/A "by construction": the out-of-tree COPY install path that
`WIRE-INTO-PROJECT.md` recommends to adopting projects DOES reintroduce the drift, so the signal is a
scoped follow-up for that path, not universally moot (review R-TOOL-2-MED).

## 2. Scope (IN)

- S1 — `.githooks/pre-push`: on a push whose ref set includes `refs/heads/main`, run
  `bash tools/run-gates.sh` (full) and exit non-zero (blocking the push) if it reds; on any other
  ref, do nothing. Classify by reading stdin ref lines; run the gate ONCE after the classify loop
  with the gate's stdin redirected (`</dev/null`) so it cannot consume remaining ref lines.
- S2 — Precondition: the hook fires in the tree the push originates from, which may not be the pushed
  tip. Gate on what the existing branch guard actually provides — on the default branch in the
  primary tree (`git-common-dir == git-dir`, `branch == default`) — NOT on a "clean tree" notion the
  branch guard does not have (review R-TOOL-2-LOW). If uncommitted-change protection is genuinely
  wanted, state it as a NEW check, don't attribute it to the guard.
- S3 — `.githooks/pre-push.test.sh`: a scratch-repo fixture that installs `core.hooksPath` in the
  clone and drives a real `git push` against a local bare remote through the hook — covering
  blocked-if-red on a `main` push, non-`main` ref skips, a multi-ref push, and a stubbed gate via an
  env seam so the test never runs the real bar. Joins the gate suite.
- S4 — Wire the new self-test into `tools/run-gates.sh` and `AGENTS.md`.
- S5 — `.gitattributes`: ADD `.githooks/pre-push text eol=lf` (and `.githooks/pre-commit text eol=lf`
  to close the same latent gap on the existing hook) — the file pins `*.sh` but NOT the extensionless
  hook files, so `* text=auto` alone can ship a CRLF hook on a Windows checkout (review
  R-TOOL-2-MED). The rev-1 "already pinned, verify" was false.
- S6 — Record, in the hook header and AGENTS.md, that the drift signal is N/A for the direct-wire
  hooksPath model but NOT for the copy-install path (S7).

## 3. Non-goals (OUT)

- No hook-staleness drift signal in THIS build for the direct-wire model — but see S6/§8 Fork B: it
  is a scoped follow-up for the `WIRE-INTO-PROJECT.md` copy-install path, not dropped outright.
- No diff-scoping in the pre-push path — a push to `main` runs the FULL bar (that is the boundary);
  scoped runs are the earlier DoR/merge runs (PLAY-aPrunedCeremony-1/-2).
- No CI wiring — running `run-gates.sh` in CI is a separate follow-up (AGENTS.md L58).

## 4. Design

### Data model

N/A — a shell hook + its test.

### Inventory

| Item | Kind | Status |
|------|------|--------|
| `.githooks/pre-push` | new tracked hook | to build |
| `.githooks/pre-push.test.sh` | new fixture | to build |
| `.gitattributes` | ADD `.githooks/pre-push` + `.githooks/pre-commit` `text eol=lf` rules | edit (add, not verify) |
| `tools/run-gates.sh` + `AGENTS.md` | register the self-test leg | edit |

### Migration

None for the direct-wire model: each node has `core.hooksPath=.githooks` (set by `check-wiring.sh`
on SessionStart, or `git config core.hooksPath .githooks`), so the tracked `pre-push` activates on
the next push with NO per-node install step.

### Rollout

Lands on `main`. Because the active hook IS the tracked file (not a copy), there is no
inert-until-reinstalled window for this repo, and `check-wiring.sh` self-heals an unset
`core.hooksPath` on SessionStart. **Caveat (rev-2):** an adopting project that follows
`WIRE-INTO-PROJECT.md`'s COPY-to-out-of-tree install instead of the direct wire re-creates the inCMS
staleness class — where the drift signal (§8 Fork B) applies.

### Files touched (estimate)

2 new + 2 edited (+ `.gitattributes`). ~95 lines.

### Alternatives rejected

- **Port the drift signal into THIS build.** Rejected for the direct-wire dogfood: hooksPath IS the
  tracked dir, so tracked == active and the signal can never fire (or fires falsely) — itself the
  vacuous-gate class (PLAY-aPrunedCeremony-3). Deferred, not dropped, for the copy-install path (§8
  Fork B).
- **Run the gate inside the per-ref read loop.** Rejected: a gate spawned inside `while read`
  inherits stdin and can swallow the remaining ref lines (the inCMS MECH-8 catch) — classify in the
  loop, run once after with stdin denied.
- **Make it a `pre-commit` extension.** Rejected: the boundary is the push to shared `main`, not the
  local commit; commits stay fast (the existing pre-commit fast leg).

## 5. Production-readiness checklist

- security — the hook runs repo-local gate scripts already trusted; no new external surface.
- perf / scale — the full bar runs once per `main` push; non-`main` pushes and all commits are
  unaffected. This is the cost the boundary trades for killing the triple-run.
- a11y / i18n — N/A.
- error / empty / loading states — a gate red blocks with a clear message and the failing leg;
  `--no-verify` stays the deliberate operator bypass (consistent with the pre-commit guard).
- observability — the hook prints which run it is doing ("pre-push: full gate on main push") so a
  blocked push is self-explanatory.
- risks — (a) the hook fires in the originating tree, not necessarily the pushed tip — S2's
  primary-tree-on-default precondition bounds this, phrased in the guard's real terms; (b) a
  multi-ref push must not let the gate eat ref lines — S1's stdin-deny + classify-then-run; (c) a
  Windows CRLF hook that will not execute — S5's `.gitattributes` pin.
- testing + left-shift gates — S3's scratch-repo fixture is the left-shift; it must drive a real
  `git push` so it proves the hook FIRES (the "prove it catches" rule, PLAY-aPrunedCeremony-3), which
  requires installing `core.hooksPath` in the scratch clone.
- migration / rollback — delete the hook file; `core.hooksPath` and the pre-commit guard are
  unaffected.
- user docs — AGENTS.md notes the pre-push boundary and the scoped drift-signal rationale (S6).

## 6. Acceptance criteria

- AC1 — When a push to `main` is attempted with a red gate (fixture: a stubbed-red gate), the push is
  blocked with a non-zero hook exit naming the failing leg.
- AC2 — When a push to a non-`main` ref runs, the hook does nothing and the push proceeds.
- AC3 — When a multi-ref push including `main` runs, the gate runs exactly once and classification is
  not corrupted by stdin consumption (fixture case).
- AC4 — When `.githooks/pre-push.test.sh` runs in the gate suite, it installs `core.hooksPath` in a
  bare-remote scratch clone and drives a real `git push` through the hook, and passes.
- AC5 — When `git check-attr text eol -- .githooks/pre-push` is run after S5, it reports `eol: lf`.
- AC6 — When the hook header and AGENTS.md are read, they record the drift signal as N/A for the
  direct-wire model and applicable to the copy-install path.

## 7. Gates

The gate suite plus the new `.githooks/pre-push.test.sh` leg; the `.gitattributes` LF rule verified
via `git check-attr`. The pre-push hook itself becomes the enforcement gate PLAY-aPrunedCeremony-1
references.

## 8. Open questions

- **Fork A — adopt the pre-push hook (owner menu 2).** RECOMMEND: yes — small, high-value, and it is
  what makes PLAY-aPrunedCeremony-1's boundary machine-enforced rather than honor-system.
- **Fork B — the drift signal for the copy-install path (rev-2).** `WIRE-INTO-PROJECT.md`'s
  copy-to-out-of-tree install re-creates the inCMS staleness class. RECOMMEND: file it as a separate
  follow-up scoped to that install path (a hash-of-tracked-vs-installed check in `check-wiring.sh`),
  NOT in this build — this repo's own dogfood does not need it, and bundling it would ship a check
  that is inert here.
- **Fork C — uncommitted-change protection.** RECOMMEND: reuse the branch guard's actual predicate
  (primary tree, default branch) rather than invent a clean-tree notion; add an explicit
  dirty-tree-blocks-push check only if the owner wants it, named as new behavior.

## 9. Revision log

- rev-1 · 2026-07-19 · initial draft (node a, aPrunedCeremony).
- rev-2 · 2026-07-19 · folded review wf_2f11fd07: `.gitattributes` change is ADD not verify (the
  extensionless hook files were unpinned); scoped the drift-signal-N/A rationale to the direct-wire
  model and raised the copy-install drift as §8 Fork B (not universally moot); reframed the S2/Fork C
  precondition in the branch guard's real terms (primary-tree-on-default, not "clean tree"); status →
  SPECCED.
