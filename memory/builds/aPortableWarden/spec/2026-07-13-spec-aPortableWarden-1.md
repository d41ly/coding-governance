# TOOL-aPortableWarden-1 — worktree-guards kit, spec (port inCMS/nc worktree guards to a project-agnostic tools/ kit)

*2026-07-13 · TOOL-aPortableWarden-1 · status: SPECCED (pending adversarial review + owner approval).
Ports the inCMS `workflow-guards` (ARCH-aVigilantWarden-1) — the branch-guard hooks + `install-guards`
+ `new-stream` — plus their already-hand-copied nicocares twins, into ONE project-agnostic kit at
`tools/worktree-guards/`, cross-platform (bash + PowerShell). Fills the governance template's §3
"machine-enforce the branch rule … wired per node by an install script" + `{{WORKTREE_SCRIPT}}`, which
today are anticipated but ship no implementation.*

## 0 · Why (the problem this closes)

The template §3 mandates: feature work happens ONLY in sibling worktrees; a tracked pre-commit hook
refuses feature commits in the primary tree; wired per node by an install script; bootstrap worktrees
with one script. Two repos already implement this — and have **diverged into near-identical hand
copies**: inCMS (`incms-hooks`, `pnpm install` tail, "inCMS worktree guard" branding) and nicocares
(`nc-hooks`, no install, "NicoCares" branding). Same logic, three hardcoded seams. That is the
N-drifting-copies anti-pattern the deployer research (DEPL-aDeployScout) names; a single kit with the
per-repo seams parameterised is the fix, and it lets a third adopter get the guard for free.

Portability reality (correcting the "all PowerShell / Windows-only" framing): the **guard hooks are
already POSIX `sh`** (`pre-commit` + `post-checkout`, pure git); only the **installers** are PowerShell,
and **`new-stream.sh` already exists**. The real port surface is: the installer → bash, and a
cross-platform parameterisation of the three seams.

## 1 · What ships (`tools/worktree-guards/`)

- `pre-commit` · `post-checkout` — the two guard hooks (single-source POSIX `sh`; already portable).
  `pre-commit` BLOCKS a feature-branch commit in the primary tree; `post-checkout` is a non-blocking
  alarm when the primary tree is left parked off the default branch.
- `install-hooks.sh` · `install-hooks.ps1` — the out-of-tree hook installer (the reusable core:
  resolve the git **common** dir, copy the repo's tracked hooks to `<common>/<label>-hooks` OUTSIDE any
  working tree, point `core.hooksPath` there, CR-check, run a red/green proof that the guard fires).
- `new-stream.sh` · `new-stream.ps1` — worktree bootstrap: fetch → ff-only the default branch (only
  when the primary tree is on it) → `git worktree add` on `feature/<name>` → optional setup step.
- `worktree-guards.test.sh` — the self-test: the generalised red/green proof + a new-stream dry-run,
  in throwaway repos (mirrors `hooks/agent-cap.test.sh` / `manifest-check.test.sh`).
- `README.md` · `kit.toml` (govkit descriptor) · `.worktree-guards.conf.example`.

## 2 · Design principles (binding)

- **Single-source where the language allows it.** The hooks are `sh` (run by git on every platform —
  one copy). Only the installer + new-stream are dual bash/PS, because they are RUN BY THE USER and
  Windows genuinely needs the PS path (see the pnpm-under-Git-Bash gotcha, §3-G3). The two ports are
  behaviour-parity, not divergent logic; a parity check is an acceptance item (§8).
- **Derive, don't configure, what git already knows.** The hook-dir label and the guard's repo name
  come from `basename "$(git rev-parse --show-toplevel)"` — zero config reproduces the inCMS/nc
  `<repo>-hooks` pattern. Config exists only for what can't be derived (§3).
- **Single responsibility for the guard hook.** The kit's `pre-commit` guards ONE thing — the branch
  rule. It does NOT bundle memory-hygiene or any other leg (inCMS's copy did; that coupling is what
  makes it un-inheritable). Composition with other pre-commit legs is the installer's concern (§4-C),
  not the guard's.
- **Fail-open, never a footgun.** Every hook early-exits 0 on any resolution failure (not a repo,
  detached HEAD, linked worktree) — a guard that errors on an edge case would block honest commits.
  `--no-verify` stays the documented deliberate bypass.
- House kit conventions: `set -u`, LF, exit 0/1/2, self-contained messages, no deps beyond git +
  coreutils (bash) / git + PowerShell 5.1+ (PS). Overwrite-engine vs project-owned split declared in
  `kit.toml`.

## 3 · The three seams — generalisation decisions

- **G1 — hook-dir label** (inCMS `incms-hooks`, nc `nc-hooks`): **derive** `LABEL=$(basename
  toplevel)` → `<repo>-hooks`. No config. (Override: `HOOK_LABEL` in `.worktree-guards.conf` for the
  rare repo whose basename collides or is ugly.)
- **G2 — guard message branding** ("inCMS/NicoCares worktree guard"): use the derived repo name, e.g.
  "worktree guard (<repo>)". Neutral, no config.
- **G3 — new-stream post-create setup** (inCMS `pnpm install`; nc nothing): **convention over config**
  — after `worktree add`, if `.stream-setup.sh` (bash) / `.stream-setup.ps1` (PS) exists at the repo
  root, run the platform-matching one IN the new worktree; else do nothing (nc-style default). This is
  what makes it cross-platform-correct: on Windows the PS new-stream runs `.stream-setup.ps1` (so
  `pnpm install` runs natively — Git-Bash `pnpm` creates broken symlinks, the documented inCMS gotcha),
  while Linux/CI runs `.stream-setup.sh`. The template's `{{WORKTREE_SCRIPT}}` fill becomes "call
  `tools/worktree-guards/new-stream.<sh|ps1>`; declare deps in `.stream-setup.*`".
  *(Open for ratification: convention file vs a `STREAM_SETUP_CMD` conf var vs a `--install-cmd` flag —
  §9-Q1.)*

## 4 · Component specs

- **A · the hooks.** Copy the inCMS `sh` hooks VERBATIM in behaviour, with the two branding strings
  swapped for the derived repo name and the memory-hygiene leg REMOVED from `pre-commit` (that leg
  belongs to the memory-tree kit; see §4-C). Keep every git-mechanic exactly: `git-dir ==
  common-dir` ⇒ primary tree; on the default branch ⇒ pass; detached/linked/non-repo ⇒ exit 0. The
  default branch is `main` unless `DEFAULT_BRANCH` is set in the conf (§3 fleets may use `master`).
- **B · the installer** (`install-hooks.sh` + `.ps1`, parity). Steps, verbatim from install-guards.ps1
  with the label derived: (1) locate `.githooks/` in the checkout (error if absent); (2) CR-check both
  hooks (a stray CR breaks `sh`); (3) resolve `<common>=git rev-parse --git-common-dir` (absolute,
  forward-slashed); (4) copy hooks → `<common>/<LABEL>-hooks`; (5) `git config core.hooksPath` there;
  (6) **red/green proof** in a throwaway repo using the INSTALLED copy — a commit on the default branch
  in the primary tree PASSES, a feature-branch commit in the primary tree is BLOCKED; hard-fail the
  install if either proof is wrong; (7) print the one-time per-node reminders (SessionStart nudge +
  any PreToolUse hooks) as GENERIC guidance, not repo-specific paths.
- **C · composition with an existing pre-commit.** The installer installs whatever `.githooks/`
  contains — it is hook-content-agnostic. Adopters who already run other pre-commit legs (hygiene,
  manifest-check, template-size — e.g. coding-governance's own `.githooks/pre-commit`) keep them: the
  branch-guard is added as ONE leg. The kit ships the guard as BOTH a standalone `.githooks/pre-commit`
  (for repos with none) AND a sourceable snippet/`guard-lib.sh` a composite pre-commit can call, so it
  never fights an existing hook. *(Open: standalone-hook vs sourceable-fragment as the primary shape —
  §9-Q2.)*
- **D · new-stream** (`.sh` exists; `.ps1` exists): generalise both — parameterise the default branch
  (`DEFAULT_BRANCH`), replace the hardcoded `pnpm install` with the §3-G3 convention, keep the
  Windows-symlink warning in the bash variant's closing note. Derive `<root>` as the worktrees' parent
  (`toplevel/..`) — matching the sibling-worktree layout the template §3 describes.

## 5 · Self-test (`worktree-guards.test.sh`)

Throwaway git repos in `$TMPDIR`, global-git-config-isolated (`GIT_CONFIG_GLOBAL=/dev/null`, per the
manifest-check.test.sh precedent). Scenarios: install → default-branch primary commit passes · feature
primary commit blocked · linked-worktree feature commit passes · detached HEAD passes · doc-on-main
passes · post-checkout alarms off-default (exit 0, message on stderr) but is silent on default ·
new-stream creates `feature/<name>` at the sibling path and runs `.stream-setup.sh` when present ·
CR-in-hook aborts the installer · `master`-default repo honored via conf · re-run is idempotent
(core.hooksPath already set). PS-parity legs run under `pwsh` when available, else skip-with-note.

## 6 · Fit

- **Template §3**: the `{{WORKTREE_SCRIPT}}` fill and the "install script" line now point at this kit.
  The template gets a one-line pointer; the detail stays in the kit README (like memory-tree/codebase-map).
- **govkit deployer**: `kit.toml` declares engine files (hooks, installers, new-stream, test —
  overwrite-wholesale) vs project-owned (`.worktree-guards.conf`, `.stream-setup.*`). A future kit joins
  the deployer with zero deployer change; this is the second concrete kit.dogfood (after env-doctor).
- **Self-dogfood caveat**: coding-governance is single-checkout (manifest §B: "no worktree fan"), so it
  SHIPS this kit but does NOT wire the guard on itself — like it ships codebase-map without adopting a
  map. The kit's self-test rides `tools/run-gates.sh` (proving the kit works via the red/green proof),
  NOT an installed guard on this repo.

## 7 · Non-goals

- **Porting `gate.ps1`** — it is inCMS's gate instance (uv/pnpm/alembic/pg_serial); its value is a
  pattern, folded separately into `run-gates.sh` + template §7, not shipped as a kit (per the assessment).
- **A SessionStart nudge implementation** — the installer only REMINDS; the nudge hook is project +
  harness specific (settings.json), out of scope here.
- **Dropping the PS variant / PS5 rewrite to pwsh-only** — keep PS 5.1 compatibility (no `pwsh`-only
  syntax); none of these tools need 7.x. (The user's pwsh concern applies to `gate.ps1`'s `Start-Job`
  ergonomics, which we're not porting.)
- **Auto-installing on clone** — hooks are per-node local config by design; the install stays a
  deliberate one-time `install-hooks` run (matches the template's "wired per node" rule).

## 8 · Acceptance checks

1. `worktree-guards.test.sh` exits 0 — every §5 scenario green.
2. bash↔PS parity: the installer and new-stream produce equivalent results (same `core.hooksPath`,
   same worktree/branch) — a parity scenario asserts it (PS legs skip-with-note where `pwsh` absent).
3. Zero hardcoded `incms`/`nc`/`pnpm` seams survive: `grep -riE 'incms|nicocares|nc-hooks|pnpm'
   tools/worktree-guards/` → empty (except an explicit "e.g." in the README).
4. The guard hooks are byte-for-byte the inCMS behaviour on the git mechanics (a differential test
   against the documented pass/block matrix), only the branding + hygiene-leg removed.
5. Adopting into a repo with an EXISTING `.githooks/pre-commit` composes (the branch-guard as an added
   leg), not clobbers — demonstrated.
6. `kit.toml` validates; `grep '{{'` on the README/conf-example after a scaffold → empty.
7. `tools/run-gates.sh` gains the worktree-guards self-test leg and stays green; no collateral on the
   other kits.

## 9 · Open decisions to ratify (before build)

- **Q1 — new-stream setup mechanism (G3):** `.stream-setup.{sh,ps1}` convention (recommended —
  platform-correct, no conf) vs a `STREAM_SETUP_CMD` conf var vs `--install-cmd`. Recommend the
  convention pair.
- **Q2 — guard-hook shape (§4-C):** ship as a standalone `.githooks/pre-commit` AND a sourceable
  `guard-lib.sh` fragment (recommended, covers both no-hook and has-hook adopters) vs standalone only.
  Recommend both.
- **Q3 — cross-platform maintenance model:** dual-maintained bash + PS with a parity test (recommended,
  the ports are ~40 lines each) vs bash-canonical + a minimal PS shim that shells to bash where
  available. Recommend dual-maintained (a PS user without bash is the exact case the PS variant exists
  for). 
- **Q4 — where the two guard hooks live in an ADOPTING repo:** the repo's tracked `.githooks/`
  (recommended, matches inCMS/nc + the installer's source-of-truth) — confirm this is the deploy target
  the govkit descriptor writes.
