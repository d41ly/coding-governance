# TOOL-dWellOiledMachine-6 — the supervisor: `resume-tick.sh` grown into the executor's seam, one act session per role act, relaunch by policy, and a reconcile before the first beat

**Status:** DEFERRED · rev-3 · 2026-10-28 · node a · Tier-2 · base 0689e7fa · streams tooling · order 28 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0284@8ad94483 whole
**Carries:** node:point.command-adapters
**Carries:** node:policy-key.run.host
**Carries:** node:policy-key.runtime.relaunch

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-56 |
| [2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-66 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-71 TOOL-dWellOiledMachine-72 TOOL-dWellOiledMachine-73 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-77 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-79 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-82 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-90 TOOL-dWellOiledMachine-91 TOOL-dWellOiledMachine-92 TOOL-dWellOiledMachine-93 TOOL-dWellOiledMachine-94 TOOL-dWellOiledMachine-95 TOOL-dWellOiledMachine-96 TOOL-dWellOiledMachine-97 TOOL-dWellOiledMachine-98 TOOL-dWellOiledMachine-99 TOOL-dWellOiledMachine-100 TOOL-dWellOiledMachine-101 TOOL-dWellOiledMachine-102 TOOL-dWellOiledMachine-103 TOOL-dWellOiledMachine-104 TOOL-dWellOiledMachine-105 TOOL-dWellOiledMachine-106 TOOL-dWellOiledMachine-107 TOOL-dWellOiledMachine-108 TOOL-dWellOiledMachine-109 TOOL-dWellOiledMachine-110 TOOL-dWellOiledMachine-111 TOOL-dWellOiledMachine-112 TOOL-dWellOiledMachine-113 TOOL-dWellOiledMachine-114 TOOL-dWellOiledMachine-115 TOOL-dWellOiledMachine-116 TOOL-dWellOiledMachine-117 TOOL-dWellOiledMachine-118 TOOL-dWellOiledMachine-119 TOOL-dWellOiledMachine-120 TOOL-dWellOiledMachine-121 TOOL-dWellOiledMachine-122 TOOL-dWellOiledMachine-123 TOOL-dWellOiledMachine-124 TOOL-dWellOiledMachine-125 TOOL-dWellOiledMachine-126 TOOL-dWellOiledMachine-127 |
| [2026-10-27-build-TOOL-dWellOiledMachine-6-deviation-61.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-6-deviation-61.md) | deviation | — |
| [2026-10-28-build-TOOL-dWellOiledMachine-6-deviation-62.md](../build/2026-10-28-build-TOOL-dWellOiledMachine-6-deviation-62.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-crosscheck.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-79 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-90 TOOL-dWellOiledMachine-91 TOOL-dWellOiledMachine-92 TOOL-dWellOiledMachine-93 TOOL-dWellOiledMachine-94 TOOL-dWellOiledMachine-95 TOOL-dWellOiledMachine-96 TOOL-dWellOiledMachine-97 TOOL-dWellOiledMachine-108 TOOL-dWellOiledMachine-112 TOOL-dWellOiledMachine-115 TOOL-dWellOiledMachine-117 TOOL-dWellOiledMachine-120 TOOL-dWellOiledMachine-126 |
| [2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-reground.md](../prompts/2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-reground.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-79 TOOL-dWellOiledMachine-90 |
| [2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 |

<!-- /gen:spec-records -->

## 1. Goal

A model session decides every next act, and a stalled run is resumed by `claude -p --resume
--dangerously-skip-permissions` from the node tick (`tools/unattended/resume-tick.sh:385`), so with
hooks failing open a resumed session runs unguarded (gap-rt-01, gap-rt-04). This unit grows
`resume-tick.sh` into the supervisor's seam: the node tick starts and restarts a supervisor process
per build lease this node holds, where `run.host` says; the supervisor launches one act session per
role act through the one launcher, relaunches it fresh or resumed as `runtime.relaunch` says, capped
by `RESUME_ATTEMPTS`, holds launches through a limit, kills what an epoch it no longer holds launched,
runs command items only through command adapters that are idempotent or reconcile, writes the shared
records alone, and reconciles before its first beat, so a supervisor killed while an act runs and
restarted by the node tick leaves exactly one act session on the item (layer-runtime `[supervise]`).

## 2. Scope (IN)

- **S1** — The supervisor (I21), `tools/runtime/supervise.py`, run as `python supervise.py run <slug>
  --epoch <n> [--adopt <act>…]`. It writes its pid, image and start stamp to
  `<git-common-dir>/gov/supervisors/<slug>.pid`, and beats every `SUPERVISOR_BEAT_SECONDS` (60).
  Each beat, in order: S7's fence read; the owner's controls, so a `HELD` run launches nothing; the
  position engine's answer, read by running the loop kit's verb `python position.py <slug> --json`
  (TOOL-dDeclaredLoop-7 S7) as a bounded subprocess, found through the inlined `resolve_kit_dir`
  block, since a kit imports no sibling kit (oc7:202-205); a role act
  launched through S4 or a command item run through S8; then `unattended.sh --beat <slug>`
  (`write_claim_beat`, `tools/unattended/unattended.sh:2469`), its liveness, which renews the lease
  only as TOOL-dPlacedRequest-1's `renews` rule says. Observed by AC1, AC3.
- **S2** — Started and restarted by the node tick. `resume-tick.sh` gains `run_supervisors`, run
  after `scan_worktrees` (`:419`): for each build lease whose `fleet-tag` is this node's and whose
  status is live or held, read through `unattended.sh --claims`, a supervisor pid file naming a pid
  `check_pid_alive` (`tools/unattended/lib-unattended.sh:660`) reads `yes` prints `supervisor — <slug> ·
  live`; otherwise S3 decides the host, S6 reconciles, and `run_detached` (`:203`) starts S1 with the
  adopted acts, printing `supervisor — <slug> · started · adopted <n> · killed <m>`. `--dry-run` names
  the row and starts nothing. How many restarts an hour allows is TOOL-dWellOiledMachine-47's.
  Observed by AC1, AC6.
- **S3** — `run.host` (`policy-key.run.host`, catalogue `tools/policy/catalogue.toml:537`) read through
  `policy-shim.sh get run.host` (I31). Its value names a host adapter row at `point.host-adapters`
  (TOOL-dWellOiledMachine-13 S2), asked through `python hosts.py ready <name>`: exit 0 lets this node's
  tick start the supervisor, since `requesting-node` and `os-scheduler` are both the node tick; exit 1
  prints `supervisor — <slug> · not started: run.host <name> not registered`; exit 2 prints `could not
  ask` with the reason; a value with no row prints `no host adapter <name>`. None of the three starts
  anything. Observed by AC2.
- **S4** — One act session per role act. For an `act` answer whose actor is a role, the supervisor
  takes the workspace from `allocate_workspace` (TOOL-dWellOiledMachine-11 S3) and builds the argv and
  environment with `launch_act(item, work_order, harness, env)` (TOOL-dWellOiledMachine-1 S2), which
  mints the act and its pending record with the lease epoch (TOOL-dWellOiledMachine-32 S1 to S3); the
  supervisor writes its binding with `write_binding` (TOOL-dWellOiledMachine-39 S1), and the
  environment carries `GOV_ACT=<act>` (TOOL-dWellOiledMachine-12 S3) and `derive_act_identity`'s
  committer (TOOL-dWellOiledMachine-39 S3), the argv `--permission-mode auto` (TOOL-aMendedFleet-116)
  and `--max-turns` from `RESUME_TURNS`. It starts the session detached in the workspace, appends its
  pid to the slug's process ledger in `write_proc_record`'s line shape (`unattended.sh:1734`, path
  `resolve_procs_path`, `:1729`), and journals `act-launch` with `act`, `key`, `epoch`, `pid` and
  `image`; at the session's exit it calls `write_act_record <act> <result.json>`
  (TOOL-dWellOiledMachine-32 S7) and journals `act-exit`, with `witness=missing` when a commit the act
  made has no `commit-msg` line in `<git-common-dir>/gov/commit-witness.log` (TOOL-dWellOiledMachine-10
  S11), so that commit is never counted as its item's witness. A second launch on an instance key whose
  act session is alive is refused, journaled and not started. Observed by AC3, AC6.
- **S5** — Relaunch. An act session that exits non-zero, ends on a limit, or exhausts `--max-turns` is
  relaunched as `runtime.relaunch` (`policy-key.runtime.relaunch`, catalogue `:431`) says, read by
  running `<sys.executable> <policy kit>/policy.py get runtime.relaunch` as a bounded subprocess, the
  policy kit found through the inlined `resolve_kit_dir` block, since a kit imports no sibling kit
  (PLAY-dOrderedCharter-7, oc7:202-205, :379-380); on `get`'s exit 2 the supervisor journals
  `relaunch` with `refused · runtime.relaunch` and `get`'s stderr line and launches nothing on that
  key. `fresh`, the default, a new act with a fresh work order and
  no `--resume`; `resume`, `launch_act` given the dead session's harness session id, adding `--resume
  <id>`. Relaunches of one instance key stop at `RESUME_ATTEMPTS`, read by `read_bound_key`
  (`tools/unattended/lib-unattended.sh:235`) as the tick reads it (`resume-tick.sh:151`), counted over
  the instance's `relaunch` journal lines; past it the supervisor journals `relaunch` with
  `cap reached` and launches nothing more on that key. Observed by AC4.
- **S6** — The reconcile before the first beat, `run_reconcile <slug> <epoch>` in `resume-tick.sh`,
  run before S2 starts a supervisor. Every `act-launch` journal line of the slug with no `act-exit` after
  it names a candidate; each candidate whose ledger row and pid `check_pid_alive` reads `yes` and whose
  `epoch` is the lease's current epoch, read as §8 F4 picks, is adopted, passed to S1 as `--adopt <act>`, its slot
  reservation rebuilt by the hook TOOL-dWellOiledMachine-9 fills, and journaled `act-adopt`; every
  other live candidate has its tree killed through `run_kill_tree` (`:182`) and is journaled
  `act-killed`. So a supervisor killed while an act runs, and restarted by the tick, finds exactly one
  act session on the item. Observed by AC6.
- **S7** — Fencing epochs. Each beat re-reads the build lease from the remote: its fleet tag and
  status through `unattended.sh --claims`, which prints fields 1 to 5 only (TOOL-dPlacedRequest-1,
  pr1:206-208), and its epoch as §8 F4 picks, since `--claims` prints no epoch. A lease whose epoch
  moved past the one S1 was started with, which every take-over writes (pr1:74-75), or whose fleet
  tag names another node, makes the supervisor kill every act session it launched under the old epoch through
  `reap.py --kill <pid>` (`tools/process-monitor/reap.py:420-470`), journal `act-killed` with `reason=fenced`,
  clear its pid file and exit 3. Observed by AC5.
- **S8** — Command adapters: the `[[point]]` row `name = "point.command-adapters"` in
  `tools/runtime/points.toml` (I4), its contract that each `[[adapter]]` row there declares `run`, an
  argv, and `class`, `idempotent` or `reconcile`, a `reconcile` row adding `probe`, an argv that exits 0
  when the effect has already landed. `check_command_adapter_row(row)` in `supervise.py` refuses a
  row with no `class`, another class, or `reconcile` with no `probe`; `python supervise.py
  --check-adapters` runs it over every row. The supervisor runs a command item only through its row:
  a `reconcile` row's probe first, a landed effect recorded as the item's witness and not run again.
  This unit registers the lander, `push-main.sh`, `reconcile` with the probe "origin already holds the
  expected sha", as TOOL-dWellOiledMachine-10 §8 F3 hands it here; the record door, `idempotent`, being
  content-addressed; and the bar, `idempotent`, being re-runnable. Observed by AC7.
- **S9** — Limit holds. An act session whose stall line (`<git-dir>/unattended/stall.<slug>.log`,
  written by `tools/unattended/stall-recorder.js:78`) names a session limit with a reset time makes the
  supervisor launch nothing until that time, journaling `limit-hold` with the reset, while S1's beat
  goes on; the ceiling on the hold, its owner item and the lease hand-over are
  TOOL-dWellOiledMachine-47's. Observed by AC4.
- **S10** — The shared records written by the supervisor alone. A role act's pass may not declare a
  write overlapping `SHARED_RECORDS` (`--dispatch`, `tools/unattended/unattended.sh:13882-13886`); the
  supervisor writes the decision, backlog and run-record rows its acts return under those paths and
  commits them alone, through `enqueue_commit` (TOOL-dWellOiledMachine-11 S6), with `Pass: none`.
  Observed by AC8.
- **S11** — The stalled-run resume at `resume-tick.sh:385` builds its argv through `launch_act` with
  `--resume <session>` under S5's `resume` form, so the tick's last hand-built `claude` argv goes, and
  with it the skip-permissions flag; the suite's two assertions of that flag, at lines 368 and 385,
  are re-pointed in this unit to the argv `launch_act` builds. Observed by AC9.
  **Readers:** by name: `tools/unattended/resume-tick.sh`, whose header comment at line 59 names the
  flag and is rewritten in this unit; `tools/unattended/resume-tick.test.sh`, which asserts the flag in
  the argv. by value: NO VALUE READERS — no file reads the launcher's argv back except those two
  assertions, and `run_tick`'s attempt line records the session and pid, never the flags.
- **S12** — The journal classes `act-launch`, `act-adopt`, `act-killed`, `act-exit`, `relaunch` and
  `limit-hold` join `JOURNAL_CLASSES` (TOOL-dWellOiledMachine-16 S3), each line keyed by `act=`, written
  through `write_journal_line`. `help/runtime.md` gains the supervisor, its start, `run.host`,
  `runtime.relaunch`, the reconcile, the fence and the command-adapter contract. Observed by AC10.

## 3. Non-goals (OUT)

- Lifetime relaunch counting reset only by a new witness, the budget draw past the cap and the routing
  to the producer: TOOL-dWellOiledMachine-46.
- The hold ceiling, the owner item, the lease hand-over and `runtime.restarts`: TOOL-dWellOiledMachine-47.
- Slot reservations under `runtime.agents-in-flight`: TOOL-dWellOiledMachine-9 fills S6's hook and S4's
  launch reservation.
- The persisted returns a fresh relaunch hands back: TOOL-dWellOiledMachine-8.
- The preflight, the launch-environment allowlist and the credential order: TOOL-dWellOiledMachine-37.
- The supervisor as the only driver and `/build` a client of `run`: TOOL-dWellOiledMachine-25.
- `RESUME_SCHEDULE_*` and the unattended kit's dissolution: TOOL-dWellOiledMachine-28.
- The fenced push itself: TOOL-dPlacedRequest-15, and TOOL-dWellOiledMachine-60 for the lander.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-1` — `launch_act`, the one builder of every act session's argv and environment, which S5 and S11 give a `--resume` form
- **consumes-from** `TOOL-dWellOiledMachine-32` — `act`, minted by `launch_act` at each S4 launch, and `write_act_record`, which S4 calls at the act's exit
- **consumes-from** `TOOL-dWellOiledMachine-39` — `write_binding` and `derive_act_identity`, the binding S4 writes at launch and the committer it launches under
- **consumes-from** `TOOL-dWellOiledMachine-12` — `session-bindings`, whose `bind` writes `owner: <act>` for each act session S4 launches with `GOV_ACT=<act>`
- **consumes-from** `TOOL-dWellOiledMachine-11` — `allocate_workspace`, `integrate_unit` and `sweep_workspaces`, the workspace S4 launches in and `enqueue_commit`, through which S10 commits
- **consumes-from** `TOOL-dWellOiledMachine-10` — `commit-witness.log` and the lander's `[[adapter]]` row, which S8 registers at `point.command-adapters`
- **consumes-from** `TOOL-dWellOiledMachine-13` — `point.host-adapters`, whose `hosts.py ready` S3 asks for the host `run.host` names
- **consumes-from** `TOOL-dWellOiledMachine-16` — `write_journal_line`, with the six classes S12 adds
- **consumes-from** `TOOL-dWellOiledMachine-20` — `points.toml`, where S8 adds the `point.command-adapters` row
- **hands-off** `TOOL-dWellOiledMachine-37` — `supervise.py`, whose launches the preflight refuses or admits
- **hands-off** `TOOL-dWellOiledMachine-8` — `supervise.py`, whose fresh relaunch hands the act's persisted returns back
- **hands-off** `TOOL-dWellOiledMachine-7` — `supervise.py`, whose fence read keeps the lease ref the PermissionRequest epoch check reads current
- **hands-off** `TOOL-dWellOiledMachine-9` — `supervise.py`, whose launch and S6 reconcile reserve and rebuild an act's slots
- **hands-off** `TOOL-dWellOiledMachine-47` — `supervise.py`, whose limit hold that unit bounds and whose restarts it caps
- **hands-off** `TOOL-dWellOiledMachine-46` — `supervise.py`, whose relaunch count that unit makes lifetime and resets on a witness
- **hands-off** `TOOL-dWellOiledMachine-25` — `supervise.py`, which that unit makes the only driver
- **hands-off** `TOOL-dWellOiledMachine-28` — `supervise.py` and `resume-tick.sh`, the seam the unattended kit dissolves into
- **hands-off** `TOOL-dWellOiledMachine-29` — `point.command-adapters`, where `visual.capture` registers
- **consumes-from** external — TOOL-dDeclaredLoop-7's `position.py <slug> --json` verb, TOOL-dPlacedRequest-1's lease record, `--claims` and `renews` rule and the epoch read §8 F4 asks for, and dBoundRoles' work-order renderer

- **hands-off** `TOOL-dWellOiledMachine-26` — `supervise.py`, whose launch S4 precedes with the announcement and whose beat S5 reads attendance at
- **hands-off** `TOOL-dWellOiledMachine-45` — `supervise.py`, which gains the session executor and whose launches go through `admit`
- **consumes-from** `TOOL-dWellOiledMachine-63` — the record door's node writer, through which this unit's sessionless `--beat`, lease and wake writes are admitted; without it TOOL-dWellOiledMachine-58 refuses them `no-session`
- **hands-off** `TOOL-dWellOiledMachine-65` — `supervise.py`'s limit hold and its sidecar parser, which that unit re-points to the stall journal line and moves into the recorder (finding 3)
- **hands-off** `TOOL-dWellOiledMachine-78` — `run_supervisors` and the supervisor pid file, whose liveness read and start that unit makes exact and exclusive (finding 64)
- **hands-off** `TOOL-dWellOiledMachine-79` — `supervise.py`'s launch and binding write (finding 69), which the spec audit's minors batch repairs
## 4. Design

### Evidence

- The tick already proves what the supervisor keeps: the index-read lease and the stand-off from a
  foreign host (`resume-tick.sh:279-286`), login before kill and killing only what it launched
  (`:330-360`), the attempt cap (`:121`, `:151`, `:326`) and the detached launch (`:203-219`).
- Its one launch line is `:385`, the only hand-built `claude` argv in the kit, and the only readers of
  its flag are the header comment (`:59`) and two assertions (`resume-tick.test.sh:368`, `:385`).
- The process ledger has one writer, `write_proc_record` (`unattended.sh:1734`), and one classifier,
  `derive_proc_state` (`:1773`), whose comment refuses a second spelling of "is this ours and is it
  alive"; the tick's own launched-pid probe is `check_pid_alive` (`lib-unattended.sh:660`).
- `reap.py --kill <id>` kills a tree and proves each member died (`tools/process-monitor/reap.py:420-470`).
- `--dispatch` already refuses a pass declaring a path overlapping `SHARED_RECORDS`
  (`unattended.sh:13882-13886`).

### The node tick, after this unit

| Step | Owner |
|---|---|
| `scan_worktrees`: beat, skip or resume each bound unattended run, the resume argv from `launch_act` | today's tick, S11 |
| `run_supervisors`: for each build lease held here, live, or host check, reconcile and start | S2, S3, S6 |
| the supervisor's beats, until its fence moves or its lease ends | S1, S7 |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `supervise.py` with `run`, `--check-adapters`, `--fixture` | runtime kit file | none |
| `SUPERVISOR_BEAT_SECONDS` | constant, 60, PINNED | none |
| `run_supervisors`, `run_reconcile` | shell functions in `resume-tick.sh` | `run`, OK |
| `check_command_adapter_row` | Python function | `check`, OK |
| `act-launch`, `act-adopt`, `act-killed`, `act-exit`, `relaunch`, `limit-hold` | journal classes | none |
| `<git-common-dir>/gov/supervisors/<slug>.pid` | node-local pid file | none |

`SUPERVISOR_BEAT_SECONDS` is PINNED at 60, a sixth of the tick's 10-minute period, so a fence moved by
a take-over is read within a minute on the old holder's node.

### Files touched (estimate)

- `tools/runtime/supervise.py`
- `tools/runtime/launch.py`: `launch_act`'s `--resume` form and `--permission-mode auto`
- `tools/runtime/points.toml`: the `point.command-adapters` row and three adapter rows
- `tools/runtime/journal.py`: six classes in `JOURNAL_CLASSES`
- `tools/unattended/resume-tick.sh`: `run_supervisors`, `run_reconcile`, the `:385` argv from
  `launch_act`, the header
- `tools/unattended/resume-tick.test.sh`: the two flag assertions re-pointed
- `help/runtime.md`

### Alternatives rejected

- **A supervisor resident in the owner's session.** A desktop task wakes a model session, so it can host
  an act but never the supervisor (layer-runtime `[supervise]`); and a session dies with its window.
- **Reconciling inside the new supervisor.** The tick already holds `check_pid_alive` and
  `run_kill_tree`; a Python copy of either would be the second spelling `derive_proc_state`'s comment
  refuses.
- **Leaving `:385` for TOOL-dWellOiledMachine-28.** §8 F1.

## 5. Production-readiness checklist

- security — act sessions launch under `--permission-mode auto` and never a skip flag; a supervisor
  whose epoch moved kills what it launched and exits; a command item runs only through a registered
  adapter row; preflight is TOOL-dWellOiledMachine-37's, on the same launcher.
- perf / scale — one supervisor process per build lease held on the node, beating once a minute; one
  tick spawn per lease to read its pid file.
- error / empty / loading states — an unready or unregistered host starts nothing, named; a candidate
  that cannot be read alive is killed, never adopted.
- observability — every launch, adoption, kill, exit, relaunch and hold is one journal line keyed by
  `act=`; every tick decision is one `supervisor —` line.
- risks — a supervisor that crashes between a launch and its journal line leaves a ledger row with no
  `act-launch`; S6 reads only journaled candidates, and process-monitor's sweep reaps the orphan.
- testing — the fixture cases under AC1 to AC9 and the arms in §7.
- migration — none: the tick keeps its unattended-run rows; a node holding no build lease starts nothing.
- user docs — `help/runtime.md`.

## 6. Acceptance criteria

The fixture is `python supervise.py --fixture --plant <case>`: a bare remote and a clone under
`%TEMP%` with a short name, a build lease held by this node, a stub `claude` on `PATH` that records its
argv and exits as the case says, and the loop kit's position engine stubbed to answer one role act.

- **AC1** — When `--plant start` runs `resume-tick.sh` twice, the first prints `supervisor — fx ·
  started · adopted 0 · killed 0` and the second `supervisor — fx · live`.
  Red when: the second tick starts a second supervisor.
- **AC2** — When `--plant host-unregistered` sets `run.host` to `os-scheduler` with the tick's
  registration probe answering not registered, the tick prints `not started: run.host os-scheduler not
  registered` and no pid file appears; under `requesting-node` with the probe registered it starts.
  Red when: a supervisor starts on a host `hosts.py ready` refused.
- **AC3** — When `--plant one-act` beats twice over one role act, the stub records exactly one launch
  whose argv carries `--permission-mode auto` and not `--dangerously-skip-permissions`, and the journal
  carries one `act-launch` for the instance key; with the act's commit planted with no `commit-msg`
  line in `commit-witness.log`, its `act-exit` line carries `witness=missing`.
  Red when: the second beat launches a second session on the live instance, or an unwitnessed commit
  exits clean.
- **AC4** — When `--plant relaunch-fresh` and `--plant relaunch-resume` make the stub exit 1, the second
  launch's argv has no `--resume` under `fresh` and `--resume <id>` under `resume`; at
  `RESUME_ATTEMPTS=2` the third death journals `cap reached` and launches nothing; and `--plant
  limit` with a planted stall line resetting in an hour journals `limit-hold` and launches nothing that
  beat.
  Red when: a relaunch ignores `runtime.relaunch`, passes the cap, or launches through a hold.
- **AC5** — When `--plant takeover` moves the lease's epoch on the remote while an act runs, the next
  beat kills the act's tree, journals `act-killed` with `reason=fenced`, and the supervisor exits 3.
  Red when: an act launched under the old epoch survives the beat.
- **AC6** — When `--plant kill-restart` kills the supervisor while its act runs and runs the tick, the
  tick adopts the act, prints `adopted 1 · killed 0`, and the stub's process list holds exactly one act
  session on the item; with a second live candidate planted under an older epoch, the tick prints
  `killed 1` and one session remains.
  Red when: the restart leaves zero or two act sessions on the item, as a tick with `run_reconcile`
  removed shows.
- **AC7** — When `python supervise.py --check-adapters` runs over a planted row with no `class` and a
  `reconcile` row with no `probe`, it exits 1 naming both; over the lander row with its probe planted to
  find the sha already held, the item is recorded witnessed and `push-main.sh` is not run.
  Red when: a row with no class registers, or a landed effect runs twice.
- **AC8** — When `--plant shared-row` returns one decision row from an act, the supervisor's commit
  touches `memory/DECISIONS.md` alone and carries `Pass: none`.
  Red when: the row lands inside the act's own commit.
- **AC9** — When `grep -c -- "--dangerously-skip-permissions" tools/unattended/resume-tick.sh` runs, it
  prints 0, and `bash resume-tick.sh --dry-run` over a stale run names the resume row unchanged.
  Red when: the tick still hand-builds a skip-permissions argv.
- **AC10** — When `grep -n "run.host\|runtime.relaunch\|reconcile" runtime.md` runs over the help page,
  each term is named, and `python journal.py write act-adopt act=act-0a1b2c3d4e5f` exits 0.
  Red when: the page omits one, or the class is refused.

## 7. Gates

`unattended kit gate` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

The unattended kit's self-test suites, `resume-tick.test.sh` among them, are waived for this build's
landing (README rule 8); S11 still re-points its two assertions.

New arm: tools/runtime/supervise.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · each planted case staged against a tick with `run_reconcile` removed and a supervisor with its fence read removed · none

## 8. Open questions

- **F1 — Does this unit move the `resume-tick.sh:385` launch onto `launch_act`, or leave it to
  TOOL-dWellOiledMachine-28?** (a) Move it here, as I2 and TOOL-dWellOiledMachine-1 §3 hand it, so the
  skip-permissions launch ends with the supervisor and 28 inherits only the dissolution; (b) leave it,
  and 28 moves and retires it last. (b) keeps gap-rt-04's unguarded resume alive for thirty-three more
  orders of the build. Rung 3, the most capable option, the brief's I2 spelling. RESOLVED (agent,
  2026-10-26, delegated): (a). widens: none · relaxes: none
- **F2 — Where does the reconcile run?** (a) In the tick, before it starts the supervisor, with the
  tick's `check_pid_alive` and `run_kill_tree`; (b) inside `supervise.py` at start. (b) is a second
  spelling of the liveness classifier. Rung 3. RESOLVED (agent, 2026-10-26, delegated): (a). widens:
  none · relaxes: none
- **F3 — What does the supervisor ask each beat?** (a) The loop kit's `derive_position`
  (TOOL-dDeclaredLoop-7 S1) directly; (b) TOOL-dWellOiledMachine-2's `next.py --json`. Both answer the
  same engine; (b) adds an edge to a verb whose job is the human-readable line. RESOLVED (agent,
  2026-10-28, delegated): (a), the engine directly through its own verb `position.py <slug> --json`
  run as a subprocess, rung 1, PLAY-dOrderedCharter-7 (oc7:202-205): a kit imports no sibling kit, so
  the 2026-10-26 pick's in-process call of `derive_position` is ruled out, and the engine's verb is
  still the parent seam. widens: none · relaxes: none
- **F4 — Through which surface do the tick and the supervisor read the build lease's epoch?**
  `--claims` prints fields 1 to 5, name, fleet tag, status, beat-age and verdict, and `epoch` is
  field 12 of `CLAIM_ROWS` (pr1:203-208); the `--lease` verbs print `epoch <n>` (pr1:86) but each
  writes. Options: (a) an ask to dPlacedRequest for a read-only verb over `read_claims` printing a
  lease's `epoch`, best the same holder verb TOOL-dTotalRecall-2 §8 F6 asks dPlacedRequest for
  (tr2:335-345), gaining the field; (b) `--lease renew` on each beat, read for its `epoch <n>` line, a
  write every beat that the `renews` rule does not admit; (c) parsing the lease commit's `epoch:` key
  here, a second parser of the record `read_claims` is the one parser of (pr1:71). Recommendation:
  (a), the ask the build run would file to dPlacedRequest (TOOL-dPlacedRequest-1). Open for the owner;
  S6 and S7 build no epoch read before the pick.

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit round 1's
  promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-63, TOOL-dWellOiledMachine-65, TOOL-dWellOiledMachine-78, TOOL-dWellOiledMachine-79.
- rev-3 · 2026-10-28 · §2 S5, S6, S7 · §3 Edges · §8 F4 · re-grounded on the parents at `d1721ef20`
  by the cross-check record `build/2026-10-28-build-TOOL-dWellOiledMachine-1-parents-crosscheck.md`,
  rows 19 and 20: `--claims` is read for fleet tag and status alone, the lease's epoch waits on F4's
  read, and `runtime.relaunch` is read by a `policy.py get` subprocess with its refusal stated. Also
  §2 S1 · §3 Edges · §8 F3, writer-found, not a record row: the engine is read through `position.py
  --json` by subprocess, and F3 is re-resolved.

## 10. Reuse audit

The seam extended is `tools/unattended/resume-tick.sh` itself: its `run_detached` (`:203`),
`run_kill_tree` (`:182`), `read_bound_key` read of `RESUME_ATTEMPTS` (`:151`) and the library's
`check_pid_alive` (`lib-unattended.sh:660`) carry the start, the kill, the cap and the liveness, and
the supervisor launches through I2's `launch_act`, records pids in the slug ledger
`write_proc_record` already writes (`unattended.sh:1734`), and kills through `reap.py --kill`. The
probe `python tools/codebase-map/reuse_lookup.py "restart a supervisor and re-adopt or kill the
session it launched"` ranked `adopt`, `extract_session`, `resolve_session_tree` and `run_kill` by name
stem; `run_kill` is the reap the supervisor calls, and the rest read transcripts, not processes.
Scout A's row cites `run_tick` at `:279`, `scan_worktrees` at `:419` and the launch at `:385`, which
hold at this base.

Recall terms used: `python tools/memory-recall/query.py "how does the supervisor reconcile act
sessions after a restart" --terms "supervisor resume-tick node tick act session relaunch reconcile
re-adopt kill tree epoch run.host"`
