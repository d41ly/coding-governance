# TOOL-aLeasedGauntlet-1 — port reconcile-before-gate into the kit

**Status:** CLOSED · rev-4 · 2026-07-20 · node a · Tier-2 · base d5ada669 · ports inCMS ARCH-aLeasedGauntlet-1 · reviewed wf_76540d9d,wf_e2be3386 · owner-ratified 2026-07-20 · built+closing-reviewed (wf_2a93910e, 7 findings folded)+landed 2026-07-20

## 1. Goal

Port the owner-ratified LIGHT gate-economy fix (inCMS `ARCH-aLeasedGauntlet-1` rev-3) into the
coding-governance kit, so any project adopting the pre-push boundary (`TOOL-aPrunedCeremony-2`) gets
it. Same premise: pre-push stays the authoritative full run (no CI dependency). Same design: the hook
is the SOLE mandated full gate, and a `push-main` lander reconciles the default branch BEFORE gating
so the hook never gates a stale tree — enforced by requiring `push-main` (block from day one). NO
distributed lease (the owner rejected it as disproportionate to a rare-race problem). The residual
re-gate on a genuine mid-gate race is accepted, bounded by a retry cap.

## 2. Scope (IN)

- S1 — **`tools/push-main.sh` — the lander (reconcile-before-gate).** `git fetch` the default branch;
  if it advanced, `git merge --no-ff` (on CONFLICT: `git merge --abort`, clear marker, exit "reconcile
  manually" — inCMS F4); set a LOCAL marker `$(git rev-parse --git-dir)/push-main-active` under a
  `trap … EXIT INT TERM` (Ctrl-C clears it; the marker is local, so a leak affects only this repo, not
  the fleet — the lighter design has no fleet-wide lock to leak); `git push`; on rejection (origin
  advanced during the gate) retry up to `GOV_PUSH_MAIN_MAX_RETRIES` (default 3) then abort; clear the
  marker. Reads the default branch/remote as the existing hooks do (origin/HEAD else main,
  `GOV_DEFAULT_BRANCH`). No `push-lease` helper — there is no lease.
- S2 — **`.githooks/pre-push` — block a raw default-branch push (ANY, not just code).** Extend the
  hook: on a default-branch push, refuse if the `push-main-active` marker is absent, pointing at
  `push-main`. Unlike inCMS's `gate.sh --docs-only` classifier, the kit hook has NO code/docs split
  (review wf_e2be3386 CORRECTNESS), so it blocks EVERY unmarked default-branch push, not "code" ones —
  `push-main` gates docs pushes cheaply anyway (the runner's own docs scoping). Block from day one
  (owner: block immediately). `--no-verify` bypasses.
- S3 — **`tools/run-gates.sh` — summary survives a `tail` AND a worktree.** Write the SUMMARY +
  failing-leg detail to `$(git rev-parse --git-dir)/gate-last-summary.txt` (RESOLVED gitdir — works in
  a linked worktree where `.git` is a file — inCMS F6); print its path on failure.
- S4 — **Playbook prose (`parallel-coding-governance.template.md`).** The pre-push hook is the SOLE
  mandated full gate; DoR/post-merge runs are optional developer-choice fail-fast checks; land the
  default branch via `push-main` (reconciles before gating). Byte-budgeted: reword existing §1 Landing
  + §7 lines in place, overflow to `.domain-rules.md` — the template has ~30 bytes of headroom
  (`check-template-size.sh`), re-measured after every edit (the PLAY-aPrunedCeremony discipline).
- S5 — **A cross-repo parity TEST, not a note.** inCMS and the kit hold two hand-kept copies of the
  lander; `tools/push-main.test.sh` pins the kit lander's observable contract (the fetch-reconcile-
  before-gate order, the marker path, the conflict-abort, the retry cap, the block-on-missing-marker)
  so the kit copy cannot silently drift from the inCMS reference (review INTEGRATION-MED). A shared
  file is rejected (parallel layouts, `scripts/` vs `tools/`); the parity test is the enforcement.
- S6 — **Register + wire + docs.** `push-main.test.sh` as a `gate-legs.json` leg; `.gitattributes` LF
  pins; `AGENTS.md` gate-suite + landing note; `WIRE-INTO-PROJECT.md` adopter step; bump `KIT_*`
  markers if the kit contract changes.

## 3. Non-goals (OUT)

- NOT a distributed lease / lock (owner-rejected). No `push-lease.sh`, no ref CAS, no `LEASE_MAX_HOLD`,
  no background refresher — all removed vs rev-2.
- NOT CI-authoritative gating (billing constraint).
- NOT test-impact analysis — a re-gate runs the full suite.
- NOT a `push-main.ps1` twin in this unit (bash-only; coding-governance nodes have git-bash); a `.ps1`
  is a follow-up if a PowerShell-only adopter appears.
- NOT re-porting the pre-push hook itself — `TOOL-aPrunedCeremony-2` shipped it; this EXTENDS it.

## 4. Design

### Relationship to inCMS

The design is shared and lives in inCMS `ARCH-aLeasedGauntlet-1` rev-3 (the lander flow, the hook
enforcement, the conflict-abort, the retry cap). This spec is the KIT implementation. inCMS keeps its
own `scripts/` copy (parallel, not shared, tooling — inCMS did not adopt the kit); the kit version is
what future adopters get. The two copies stay in lockstep via S5's parity TEST.

### Inventory

| Item | Kind | Status |
|------|------|--------|
| `tools/push-main.sh` | new lander (reconcile → marker → push → retry-capped → clear) | to build |
| `tools/push-main.test.sh` | scratch-bare-remote fixture + parity assertion | to build |
| `.githooks/pre-push` | edit: block a raw default-branch push without the marker | edit |
| `tools/run-gates.sh` | edit: worktree-safe `gate-last-summary.txt` + print path | edit |
| `tools/gate-legs.json` + `AGENTS.md` + `.gitattributes` | register self-test, LF pins, note | edit |
| `parallel-coding-governance.template.md` (+ `.domain-rules.md`) | S4 charter prose (byte-budgeted) | edit |
| `WIRE-INTO-PROJECT.md` | adopter step for `push-main` | edit |

### Migration / Rollout

Additive tracked tools; the hook's marker-check ships enabled (block immediately). coding-governance's
direct-wire `core.hooksPath` means the hook change is live on the next push with no reinstall (unlike
inCMS's copy-install).

### Files touched (estimate)

2 new + ~5 edited. ~140 lines + the byte-budgeted template edits. (Roughly half the rejected lease
port.)

### Alternatives rejected

- **The full lease port (rev-2, owner-rejected).** A reusable `push-lease.sh` kit tool implementing a
  cross-node git-ref CAS lock. Eliminates the race entirely but adds a distributed lock every adopter
  inherits. Rejected with the inCMS full lease.
- **A shared lease/lander script between inCMS and the kit.** Rejected: parallel layouts; the parity
  test (S5) is lighter than a cross-repo shared file.

## 5. Production-readiness checklist

- security — no new surface; tracked scripts; the marker is local + untracked.
- perf / scale — normal landing = one full gate; a genuine race adds ≤ `MAX_RETRIES` re-gates then
  aborts (bounded). Non-default pushes/commits unaffected.
- a11y / i18n — N/A.
- error / empty / loading states — red gate blocks (existing hook); conflict aborts + cleans; race
  exhausts the cap with a message; `--no-verify` bypasses.
- observability — `push-main` prints each attempt; the gate summary survives a `tail` + a worktree.
- risks — residual re-gate under genuine concurrency (accepted, capped); a raw push bypasses (closed
  by S2); a stale local marker (crash) is cleared on the next `push-main` and is single-session.
- testing + left-shift gates — `push-main.test.sh` drives two clones against a bare remote: reconcile-
  before-gate, mid-gate race → one re-gate → success, retry-cap-abort, conflicting-reconcile → clean +
  marker gone, hook-blocks-raw-push, worktree summary, SIGINT → marker cleared. Left-shift "gated a
  stale tree" + "raw push skipped reconcile".
- migration / rollback — delete the tools + revert the hook edit; no shared state.
- user docs — `WIRE-INTO-PROJECT.md` (adopter) + `AGENTS.md` (dogfood).

## 6. Acceptance criteria

- AC1 — When the default branch advanced pre-push, `push-main` reconciles first, then gates once — the
  gate never runs on a stale tree (fixture: a second clone pushes before the lander's push).
- AC2 — When origin advances DURING the gate (fixture: a second clone pushes mid-stubbed-gate),
  `push-main` re-reconciles/re-gates up to `MAX_RETRIES` then aborts — never unbounded.
- AC3 — A raw default-branch push (no marker) — code OR docs — is refused by `.githooks/pre-push` with
  the `push-main` pointer; `--no-verify` bypasses.
- AC4 — A conflicting reconcile and a Ctrl-C both leave the tree clean and the marker gone.
- AC5 — `bash tools/run-gates.sh | tail -1` red: `$(git rev-parse --git-dir)/gate-last-summary.txt`
  holds the full diagnosis (primary tree + a linked worktree); path printed.
- AC6 — `check-template-size.sh` stays ≤ 32768 after S4; the template + AGENTS state the hook as the
  sole mandated full gate and `push-main` as the lander.

## 7. Gates

The gate suite (self-hosting) + the new `push-main.test.sh` leg; `check-template-size.sh` (S4 budget);
`check-kit-versions.sh` (S6 markers). The fixture must prove it catches a mid-gate race and blocks a
raw push.

## 8. Open questions

none — all forks resolved (built + landed 2026-07-20 alongside inCMS ARCH-aLeasedGauntlet-1).

- **Fork A — port timing: after inCMS proves rev-3, or in parallel?** RESOLVED: built and landed in
  the same session as inCMS (the settled design ported directly).
- **Fork B — `push-main.ps1` twin in-scope?** RESOLVED: no — bash-only, as shipped.
- **Fork C — S4 template prose vs `.domain-rules.md`.** RESOLVED: the reconcile-before-gate discipline
  landed in `.domain-rules.md` §10 (uncapped companion); the template stayed under the 32 KiB gate.

## 9. Revision log

- rev-1 · 2026-07-20 · initial design pass (full push lease port).
- rev-2 · 2026-07-20 · folded review wf_76540d9d into the full-lease port; added a parity test.
- rev-3 · 2026-07-20 · owner ratified the lighter reconcile-before-gate + block; rewrote away the lease
  kit tool (`push-lease.sh`, ref CAS, refresher) — now a `push-main` lander + hook block + worktree-safe
  summary + a bounded retry cap; kept the parity TEST (S5) and the still-applicable folds.
- rev-4 · 2026-07-20 · folded review wf_e2be3386: the kit hook has NO code/docs split, so S2/AC3 block
  EVERY unmarked default-branch push (not just "code" — unimplementable in the kit hook); inherit the
  inCMS rev-4 efficacy honesty (the reduction is S1; S2/S3 are automation + enforcement) and the
  dropped `.ps1` (the kit already scoped it out).
