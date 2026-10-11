# TOOL-aSparedSpawn-5 — the held self-test tier in WSL2, from an ext4 mirror, with combined verdicts

**Status:** INPROGRESS · rev-3 · 2026-10-11 · node a · Tier-2 · base 22efab65 · streams tooling · order 1 · ratified 2026-10-10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aSparedSpawn-5-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aSparedSpawn-5-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Run the held self-test tier's Linux-safe legs inside WSL2, from a clone on WSL's own ext4 disk, and
its Windows-only legs natively, then combine the two halves into one verdict. The research measured a
spawn at 1.07 ms in WSL against 21 ms quiet and 818 ms loaded under MSYS on node `a`, so the tier's
hours are expected to fall to tens of minutes (estimate, not measured; `research2-wsl` §4).

## 2. Scope (IN)

- **S1** — A wrapper, `tools/run-gates/run-held-wsl.sh`, run from the Windows side. It refuses a dirty
  tree, pins `S` and the tree fingerprint, partitions the held legs, runs the two halves concurrently
  and hands both to the combiner. It never edits `tools/run-gates/run-gates.sh` behaviour: each half
  is an ordinary runner invocation over a partition manifest passed through `GATE_LEGS`, with
  `GATE_FULL=1 GATE_SELFTESTS=1` and `GATE_REUSE` unset. Each partition row runs its leg through the
  wrapper's `--leg` shim, which unsets `GATE_LEGS` and resolves a `python`/`python3` launcher before
  `exec`: the runner exports `GATE_LEGS` to every leg, and the two canaries read it as their subject,
  so the gov canary refused a subset and the run-gates canary graded one. Observed by AC1, AC6.
- **S2** — The WSL mirror. A `--setup` mode clones once from the Windows primary into the declared
  ext4 path, points `origin` at the GitHub URL, and adds a remote `win` used only as a fetch source.
  Every run does `git fetch win` and a detached `git worktree add` at `S` inside the mirror. No WSL
  process writes to the Windows `.git`: no `prune`, `gc`, `worktree` verb, or fetch into it, and no
  `GIT_DIR` or `GIT_COMMON_DIR` crosses into `wsl.exe`. Observed by AC3.
- **S3** — The Windows-only declaration, `tools/run-gates/windows-only-legs.txt`: one row per held leg
  that must run natively, each with its reason. It is gov's declaration over gov's legs, so the kit
  withholds it from adopters as `project-owned`, as it does `selftest-budgets.txt`, and the partition
  refuses by name where it is absent. The HELD population is the runner's own predicate, a leg whose
  `subject` is `kit` or whose `chunk` is `selftests`, so the six repo-subject self-tests are partitioned
  too. Every row must name a held leg of `tools/gate-legs.json`, so a stale row reds. The partition is
  derived from it and the manifest, never typed twice. Observed by AC1.
- **S4** — The combiner, `tools/run-gates/held_halves.py`, with a `--selftest` arm set. It refuses
  unless the union of both halves' legs equals the held population exactly once, both verdict files
  exist, both fingerprints equal the pinned one, the WSL half's `HEAD` equals `S`, neither half moved
  its tree, and both partitions derive from one manifest blob. It prints leg lines in manifest order
  and exits by the runner's precedence: 2, then 1, then 4, then 3, then 0. Observed by AC1, AC2.
- **S5** — Only the combiner writes a green record. Each half runs in a tree whose git dir no Windows
  boundary reads: the WSL half in the mirror's worktree, the Windows half in a scratch
  `git clone --local` of `S` under a short `TEMP` root. The combiner alone writes `held-green` into
  the Windows common git dir. Observed by AC4.
- **S6** — Paired runs. A `--paired` mode runs every Linux-safe held leg on BOTH hosts at one `S` and
  appends one per-leg verdict row per host to a machine-local parity file in the Windows common git
  dir. The combiner refuses to write `held-green` until the declared number of consecutive paired
  runs at the current manifest blob agree on every compared leg, and names each disagreeing leg. A
  paired run itself writes no `held-green`: its Windows half runs the whole held population, its
  verdict is that half's, and the record comes from a plain run once parity is proven.
  Observed by AC5.
- **S7** — The host declaration, PER NODE (owner ruling F2). Each node declares its own distro and
  mirror path in a node-local, untracked conf, `gate-wsl.conf` in that clone's common git dir, read
  beside the shared keys and never sourced. `.githooks/gate-env.sh` carries only what every node
  shares: `GATE_WSL_PARITY_RUNS` and the default mirror `/c/projects/coding-governance`. The combiner's
  `--host` mode resolves both values, prints each with its source, and the wrapper takes them from it.
  An undeclared node falls back to the default mirror and WSL's default distro and says so on every
  run. An unreachable host, or a node-local key outside the two admitted, refuses with exit 2 naming
  the file and the key. Observed by AC6 and AC8.
- **S8** — The WSL half's environment: `/mnt/*` stripped from `PATH` (a `command -v` miss costs
  48 ms with it and 0.87 ms without, research probe 3), `TMPDIR` on the mirror's ext4 filesystem, and
  no Windows interop binary reachable. Observed by AC3.
- **S9** — The first paired-run evidence: the parity rows and both halves' wall seconds, with the
  instrument, committed under `memory/builds/aSparedSpawn/build/`. Observed by AC7.

## 3. Non-goals (OUT)

- The push bar. No repo-subject leg runs in WSL, and `gate-full-green` is never written from a
  combined run. F1 recommends that ruling be explicit.
- Any reader of `held-green`. This unit writes the record and grants it no authority; a later unit
  may let a boundary read it.
- Budget-only rows of `tools/run-gates/selftest-budgets.txt` that are not manifest legs, such as the
  unattended driver shards. `GATE_LEGS` selects manifest legs only, so those suites stay native.
- Changing remote CI. It stays `windows-latest` by `TOOL-dDerivedDocket-32`'s reasoning. A
  non-required Linux job is a follow-up, not this unit.
- Lowering any ceiling or budget from WSL readings. The mirror keeps its own ledger; nothing from it
  enters `tools/run-gates/ceiling-evidence.txt`.
- A `GATE_HOST` mode inside the runner. The runner grades itself (`run-gates.sh:20-25`).

### Edges

- **hands-off** external — moving the push bar itself to a split Windows/WSL run, and any boundary
  that reads `held-green`, belong to a later unit once paired evidence exists.

## 4. Design

### Data model

The partition is two JSON manifests, each a filtered copy of the held rows of
`tools/gate-legs.json` whose `argv` is prefixed by the `--leg` shim, written to scratch and never
committed. Each half writes the runner's normal `gate-run/<runid>/` directory in its own git dir, and
the wrapper copies that run's `verdict` and `header`, the runner's stdout and a `meta` file (host, run
id, sha, the full manifest's blob read at `HEAD` of the half's tree, wall seconds) into a half
directory; the WSL half's comes back to Windows as a `tar` stream over `wsl.exe`. The combiner reads
each half's runner stdout through `parse_verdicts` (`tools/run-gates/profile_bar.py:103`), which
already splits on LF only and keeps one verdict per leg, reads each half's `verdict` file for
`verdict`, `fingerprint_end` and `tree_moved`, and its `header` for `head`.

`held-green`, written to the Windows common git dir, carries tab-separated `sha`, `fingerprint`,
`manifest_blob` (the FULL manifest's), `hosts windows:<runid>,wsl:<runid>`, `parity <n>/<k>` and
`stamped`. The parity file is one row per (run, host, leg): `sha`, `manifest_blob`, host, leg name,
verdict, run id.

### The per-node host declaration

The node registry in `AGENTS.md` records per-node variances, and `.githooks/gate-env.sh` is one file
every node shares, so a distro or a mirror path declared only there is one node's answer imposed on
all. The declaration therefore splits by who owns the value:

| value | lives in | why there |
|---|---|---|
| `GATE_WSL_DISTRO` | node-local `gate-wsl.conf` in the clone's common git dir | a distro name is one machine's fact |
| `GATE_WSL_MIRROR` | node-local `gate-wsl.conf`, else the shared default | the path is one machine's disk |
| default mirror `/c/projects/coding-governance` | `.githooks/gate-env.sh` | the same default for every node |
| `GATE_WSL_PARITY_RUNS` | `.githooks/gate-env.sh` | a trust threshold, owned by the repo |

The node-local file is `KEY=value` lines, parsed and never sourced, admitting only the two node keys,
so no node can lower the parity threshold for itself. The common git dir is per clone and therefore
per node, every worktree of a node reads the same file, and nothing in it is ever committed, pushed or
merged; `held-green` and the parity file already live there. The shared keys are read the way
`.githooks/pre-commit` reads `GOV_KITROOT`: the assignment is parsed, the file is not sourced.

Resolution prints one line per value, `wsl host: distro <value> (<source>)` and the same for the
mirror, where the source is `declared in <file>`, `shared default` or `WSL default distro`. An
undeclared distro runs `wsl.exe` with no `-d`, so WSL picks its own default.

### Flow of one run

1. Refuse a dirty tree, since WSL sees committed objects only. Pin `S=$(git rev-parse HEAD)` and
   `FP` from `tools/run-gates/gate-fingerprint.sh`; its rev and working-tree forms agree on a clean
   tree (`gate-fingerprint.sh:13-17`).
2. `held_halves.py --partition` writes the two manifests and prints both blobs.
3. WSL half: with `WSLENV` emptied, `wsl.exe -d <distro> -e git -C <mirror> fetch win` and a detached
   `worktree add` at `S`, then `wsl.exe -d <distro> -e bash <worktree>/tools/run-gates/run-held-wsl.sh
   --half <S> …`, so the half runs the wrapper as committed at `S` rather than the mirror's checkout.
   It verifies `HEAD` is `S`, strips the environment per S8, and runs the runner over the WSL
   partition with the self-tests switched on. The mirror's turnstile beacon
   serialises WSL halves from every Windows worktree.
4. Windows half, concurrently: the runner over the Windows partition, inside the scratch clone.
5. `held_halves.py --combine` grades both halves and, on acceptance with parity proven, writes
   `held-green`. A missing verdict, from `wsl --shutdown` or a reboot, is REFUSED with exit 2.

A half run alone never earns a usable record: its stamp sits in a git dir nobody reads, and its
`manifest_blob` is the partition's, which pre-push predicate 7 (`.githooks/pre-push:1225`) already
refuses.

### Inventory

New identifiers, each under the lexicon's verb table: `build_partition`, `check_halves`,
`write_held_stamp`, `add_parity_rows`, `resolve_wsl_host` and `main` in the combiner, with the
helpers `load_manifest`, `load_half`, `parse_conf`, `measure_parity` and `run_selftest`; `run_half`,
`run_leg` and `print_refusal` in the wrapper. The new held leg is `held-halves selftest`, unguarded as
`review-replay selftest` is, so no live spec owes it a §7 entry by guard. The node-local keys are `GATE_WSL_DISTRO` and `GATE_WSL_MIRROR`; the shared keys are
`GATE_WSL_MIRROR_DEFAULT` and `GATE_WSL_PARITY_RUNS`. The node-local file is `gate-wsl.conf`.

### Rollout

Land dark: nothing invokes the wrapper but the owner, and no boundary reads `held-green`. On each node
that will run it, the owner writes that node's `gate-wsl.conf` or accepts the printed defaults, runs
`--setup` once, then `--paired` until the combiner reports parity.

### Files touched (estimate)

- `tools/run-gates/run-held-wsl.sh` — new: setup, run, paired and half modes.
- `tools/run-gates/held_halves.py` — new: partition, combine, parity and `--selftest`.
- `tools/run-gates/windows-only-legs.txt` — new: the declared native legs, with reasons.
- `tools/run-gates/kit.toml` — the leg's `[[gate_leg]]` row, and the declaration withheld as `project-owned`.
- `tools/gate-legs.json` — one held leg for the combiner's `--selftest`.
- `tools/run-gates/selftest-budgets.txt` — that leg's budget row.
- `tools/run-gates/run-gates.sh` — the kit version line only, if `check-kit-versions.sh` asks.
- `.githooks/gate-env.sh` — the two shared keys: the default mirror and the parity-run count.
- `tools/run-gates/README.md` — the user page for the wrapper.

### Alternatives rejected

- **A `GATE_HOST` mode inside `run-gates.sh`.** Any diff to the runner makes every red read OWN, and
  the runner already takes an alternate manifest through `GATE_LEGS` (`run-gates.sh:216`).
- **Running WSL against the Windows checkout.** A linked worktree's `.git` names `C:/...`, which
  Linux git cannot open, and the primary costs 45 to 91 ms per git verb over 9P (research probe 2).
- **The whole held tier in WSL with no native half.** It would certify only the POSIX branch of every
  `uname` case, which no registered node runs (`resume-tick.sh:167-168`).
- **Sending the mixed suites to the native half wholesale.** The saving disappears; the govkit
  selftest alone was 3445 s on the last full Windows ledger (research §4).
- **A `"host"` key in `tools/gate-legs.json`.** It moves `manifest_blob` for every boundary and needs
  the canary's key-set pin; a sibling declaration file does not.
- **A distro and mirror column in the `AGENTS.md` node registry.** The registry is a rendered charter
  table, so the wrapper would parse Markdown a renderer owns, and a node changing its own path would
  need a tracked commit pushed through the bar before its next run could use it.
- **Per-node keys only in `.githooks/gate-env.sh`.** Every node sources the same file, so it can hold
  one answer, which the F2 ruling refuses.
- **An ignored `gate-env.local.sh` beside it.** The hook sources `.githooks/gate-env.sh` only when it is
  tracked and unmodified at the pushed sha (`.githooks/gate-env.sh:81-83`); an untracked sibling in the
  same directory invites exactly the unvetted sourcing that rule exists to stop.

## 5. Production-readiness checklist

- security: WSL must never write the Windows `.git` (a Linux prune would read every worktree as prunable); refusals pin it.
- perf / scale: estimated 10-30x on spawn-bound legs (research §4); RAM below 24000 MB drops the WSL profile to `modest`.
- error / empty / loading states: a missing half, verdict or leg, a moved tree or a sha mismatch is REFUSED, exit 2, never green.
- observability: the combiner prints both run ids, both hosts and `parity <n>/<k>` on every run, accepted or not.
- risks: host-caused reds on first contact, timing arms reordering on a fast host, and a WSL green certifying POSIX-only branches.
- testing: `held_halves.py --selftest` arms over synthetic halves, each refusal's failing case observed by a staged break.
- migration: none; new files and blank keys, with the run-gates kit version bump `check-kit-versions.sh` derives.
- user docs: a section in `tools/run-gates/README.md`: setup, the paired mode, what `held-green` does and does not certify.

## 6. Acceptance criteria

- **AC1** — When `held_halves.py --selftest` runs, its partition arms show every held leg of
  `tools/gate-legs.json` lands in exactly one half, and a row of `windows-only-legs.txt` naming
  no such leg is refused with exit 2 naming the row.
  Red when: a leg is in both halves or neither, or a stale row passes.
- **AC2** — When `held_halves.py --selftest` runs its combine arms, each of these synthetic halves is
  REFUSED with exit 2 and a line naming the cause: a missing `verdict` file, a fingerprint other than
  the pinned one, a WSL `HEAD` other than `S`, `tree_moved yes`, partitions from two manifest blobs,
  and a leg absent from both. A pair with one RED and one HOST leg exits 1.
  Red when: any of those cases is accepted, or the exit code breaks the runner's precedence.
  fixture: synthetic `gate-run` directories built inside the selftest; the tree holds none today.
- **AC3** — When `run-held-wsl.sh --half` runs, `git worktree list --porcelain` and
  `git for-each-ref` on the Windows primary print the same bytes before and after, the mirror's
  `git remote -v` shows `origin` as the GitHub URL, and `command -v tasklist.exe` inside the half finds
  nothing. Red when: either Windows listing changes, or a `/mnt` path is on the half's `PATH`.
- **AC4** — When a combined run completes, `git hash-object` of the Windows git dir's
  `gate-full-green` and `gate-full-green.shared` reads the same before and after, and `held-green`
  exists only when the combiner accepted. Red when: a half's runner wrote either file, or
  `held-green` appears after a refusal.
- **AC5** — When `held_halves.py --selftest` feeds a parity file holding one disagreeing leg, the
  combine refuses to write `held-green`, names the leg, and prints `parity` below the declared count.
  Red when: the record is written while any compared leg disagrees or fewer paired runs are recorded.
- **AC6** — When `wsl.exe` cannot reach the resolved distro, or the node-local `gate-wsl.conf` carries a
  key other than `GATE_WSL_DISTRO` and `GATE_WSL_MIRROR`, the wrapper exits 2 naming the file and key;
  when the tree is dirty it exits 2 before any half starts. Red when: any of the three starts a half.
- **AC7** — When the first `--paired` run reaches agreement, the build folder carries its parity rows
  and both halves' wall seconds with the instrument, per charter §8.
  Red when: the figures exist only in a scratch directory, or a paired run is reported without rows.
  cost: one paired run is the whole held tier natively plus its Linux-safe part in WSL, hours on node `a`.
  permission: the held tier is run on demand by the owner (owner ruling 2026-08-27), so the owner runs this.
  figure: PINNED at the paired run's date and sha; nothing re-derives it.
- **AC8** — When `held_halves.py --selftest` resolves the host over a scratch common git dir holding no
  `gate-wsl.conf`, it answers the mirror `/c/projects/coding-governance` and no `-d` distro, printing
  `shared default` and `WSL default distro` as their sources; with a conf declaring both, it answers
  the declared values and names the file. Red when: the undeclared case resolves silently, or a
  declared value loses to the shared default.
  fixture: scratch git dirs built inside the selftest; no node holds a `gate-wsl.conf` today.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `pre-push run-log line` · `push-main self-test` · `check-wiring self-test` · `settings-merge selftest` · `run-gates canary` · `run-gates evidence` · `run-gates turnstile` · `run-gates gov canary` · `foreign-prefix parity (every self-test at three prefixes)` · `run-gates run-log line` · `run-gates adopter e2e` · `profile-bar selftest` · `install-prefix self-test` · `dead-path carriers self-test` · `lexicon naming predicates` · `spec-tokens self-test` · `kit-placeholders self-test` · `branch-guard self-test` · `pre-push self-test` · `pre-push bar self-test` · `transition-audit arms` · `straggler-guard arms` · `every held leg is budgeted, every budget row resolves` · `kit version markers`

New arm: tools/run-gates/held_halves.py --selftest · covers AC1 AC2 AC5 AC8 · each refusal and the undeclared-host fallback staged by a synthetic half that breaks one precondition, RED observed before landing · a new held leg and its budget row

## 8. Open questions

- **F1 — May a Linux host produce the held self-test tier's verdict on a Windows-first repo whose CI
  is `windows-latest` on purpose?** `TOOL-dDerivedDocket-32` chose Windows because a Linux runner's
  first reds measure the host, not the tree.
  - (a) Yes, for the held tier only, never for the push bar, and only after the declared number of
    agreeing paired runs; Windows-only legs stay native and the daily `held` CI job keeps covering the
    Windows arms of the mixed suites.
  - (b) Yes, for the held tier and later the push bar behind the same combiner.
  - (c) No; WSL runs stay advisory and write no record.
  - Recommendation: (a), with `GATE_WSL_PARITY_RUNS` set to 3 consecutive agreeing paired runs.
  - RESOLVED (owner, 2026-10-10): (a) the held tier only, after the declared agreeing paired runs; never the push bar.
- **F2 — Which distro and clone path is the declared host?**
  - (a) Conf keys in `.githooks/gate-env.sh`: `GATE_WSL_DISTRO` defaulting to `claude-u26`, the
    machine's default distro, and `GATE_WSL_MIRROR` defaulting to `/c/projects/coding-governance`,
    which matches the charter render path and the `/c/` spelling in `.process-monitor.conf`.
  - (b) The same keys with the mirror at `~/gov-mirror`, which needs no root-owned `/c`.
  - (c) No keys; the wrapper takes both as arguments on every run.
  - Recommendation: (a). The keys are blank in the landed file, so nothing runs until the owner sets them.
  - RESOLVED (owner, 2026-10-10): per host, declared by the owner on each node; `/c/projects/coding-governance` is only the default.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-10 · §2 §4 §6 §7 S7 AC6 AC8 · folded the owner's F2 ruling: distro and mirror are
  declared per node in a node-local `gate-wsl.conf` in the clone's common git dir, the shared
  `.githooks/gate-env.sh` keeps only the default mirror and the parity count, an undeclared node
  falls back and says so, and the registry column and an ignored sibling file are rejected.
- rev-3 · 2026-10-11 · §2 §4 §6 S1 S3 S6 AC1 · the build pass. The held population is the runner's
  own predicate, kit subject or `selftests` chunk, not kit subject alone, which left six held legs in
  neither half. Partition rows run through a `--leg` shim that drops `GATE_LEGS`, because the runner
  exports it to every leg and both canaries read it as their subject. The Windows-only declaration
  moves into the kit directory as `project-owned`, beside `selftest-budgets.txt`, so the kit
  descriptor rather than a registry exemption claims it. A paired run writes no `held-green`. The
  half directories and their `tar` hand-back are named.

## 10. Reuse audit

The probe, `tools/codebase-map/reuse_lookup.py`, asked "run a subset of gate legs from an alternate
manifest and combine verdicts", names no seam that runs halves; its closest reader is `parse_verdicts` in
`tools/run-gates/profile_bar.py`, which the combiner imports for verdict lines instead of re-parsing
them. The runner seam extended is `GATE_LEGS` (`run-gates.sh:216`), already honoured by
`run-selftests.sh`.

Recall terms used: WSL linux host windows-latest remote-ci held self-tests gate-full-green stamp combiner parity platform
