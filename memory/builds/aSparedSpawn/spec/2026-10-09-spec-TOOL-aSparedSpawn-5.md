# TOOL-aSparedSpawn-5 — the held self-test tier in WSL2, from an ext4 mirror, with combined verdicts

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base 22efab65 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

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
  is an ordinary runner invocation over a partition manifest passed through `GATE_LEGS`. Observed by
  AC1, AC6.
- **S2** — The WSL mirror. A `--setup` mode clones once from the Windows primary into the declared
  ext4 path, points `origin` at the GitHub URL, and adds a remote `win` used only as a fetch source.
  Every run does `git fetch win` and a detached `git worktree add` at `S` inside the mirror. No WSL
  process writes to the Windows `.git`: no `prune`, `gc`, `worktree` verb, or fetch into it, and no
  `GIT_DIR` or `GIT_COMMON_DIR` crosses into `wsl.exe`. Observed by AC3.
- **S3** — The Windows-only declaration, `tools/windows-only-legs.txt`: one row per held leg that must
  run natively, each with its reason. Every row must name a `subject: kit` leg of
  `tools/gate-legs.json`, so a stale row reds. The partition is derived from it and the manifest,
  never typed twice. Observed by AC1.
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
  runs at the current manifest blob agree on every compared leg, and names each disagreeing leg.
  Observed by AC5.
- **S7** — The host declaration. Two keys in `.githooks/gate-env.sh`, the distro and the mirror path,
  per F2. A blank or unreachable host refuses with exit 2 naming the key. Observed by AC6.
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

The partition is two JSON manifests, each a filtered copy of the `subject: kit` rows of
`tools/gate-legs.json`, written to scratch and never committed. Each half writes the runner's normal
`gate-run/<runid>/` directory in its own git dir. The combiner reads each half's runner stdout through
`parse_verdicts` (`tools/run-gates/profile_bar.py:103`), which already splits on LF only and keeps one
verdict per leg, and reads each half's `verdict` file for `verdict`, `fingerprint_end` and
`tree_moved`.

`held-green`, written to the Windows common git dir, carries tab-separated `sha`, `fingerprint`,
`manifest_blob` (the FULL manifest's), `hosts windows:<runid>,wsl:<runid>`, `parity <n>/<k>` and
`stamped`. The parity file is one row per (run, host, leg): `sha`, `manifest_blob`, host, leg name,
verdict, run id.

### Flow of one run

1. Refuse a dirty tree, since WSL sees committed objects only. Pin `S=$(git rev-parse HEAD)` and
   `FP` from `tools/run-gates/gate-fingerprint.sh`; its rev and working-tree forms agree on a clean
   tree (`gate-fingerprint.sh:13-17`).
2. `held_halves.py --partition` writes the two manifests and prints both blobs.
3. WSL half: `wsl.exe -d <distro> -- bash <mirror>/tools/run-gates/run-held-wsl.sh --half <S>`, which
   fetches from `win`, verifies `S`, adds a detached worktree, strips the environment per S8, and runs
   the runner over the WSL partition with the self-tests switched on. The mirror's turnstile beacon
   serialises WSL halves from every Windows worktree.
4. Windows half, concurrently: the runner over the Windows partition, inside the scratch clone.
5. `held_halves.py --combine` grades both halves and, on acceptance with parity proven, writes
   `held-green`. A missing verdict, from `wsl --shutdown` or a reboot, is REFUSED with exit 2.

A half run alone never earns a usable record: its stamp sits in a git dir nobody reads, and its
`manifest_blob` is the partition's, which pre-push predicate 7 (`.githooks/pre-push:1225`) already
refuses.

### Inventory

New identifiers, each under the lexicon's verb table: `build_partition`, `check_halves`,
`write_held_stamp`, `add_parity_rows` and `main` in the combiner; `run_half` in the wrapper. The
conf keys are `GATE_WSL_DISTRO`, `GATE_WSL_MIRROR` and `GATE_WSL_PARITY_RUNS`.

### Rollout

Land dark: with `GATE_WSL_DISTRO` blank the wrapper refuses and nothing else changes. The owner sets
the keys after F1 and F2, runs `--setup` once, then `--paired` until the combiner reports parity.

### Files touched (estimate)

- `tools/run-gates/run-held-wsl.sh` — new: setup, run, paired and half modes.
- `tools/run-gates/held_halves.py` — new: partition, combine, parity and `--selftest`.
- `tools/windows-only-legs.txt` — new: the declared native legs, with reasons.
- `tools/gate-legs.json` — one held leg for the combiner's `--selftest`.
- `tools/run-gates/selftest-budgets.txt` — that leg's budget row.
- `tools/run-gates/run-gates.sh` — the kit version line only, if `check-kit-versions.sh` asks.
- `.githooks/gate-env.sh` — the three host keys, blank by default until F1 and F2.
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

- **AC1** — When `held_halves.py --selftest` runs, its partition arms show every `subject: kit` leg of
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
- **AC6** — When `GATE_WSL_DISTRO` is blank in `.githooks/gate-env.sh`, the wrapper exits 2 and names
  the key; when the tree is dirty it exits 2 before any half starts.
  Red when: either case starts a half.
- **AC7** — When the first `--paired` run reaches agreement, the build folder carries its parity rows
  and both halves' wall seconds with the instrument, per charter §8.
  Red when: the figures exist only in a scratch directory, or a paired run is reported without rows.
  cost: one paired run is the whole held tier natively plus its Linux-safe part in WSL, hours on node `a`.
  permission: the held tier is run on demand by the owner (owner ruling 2026-08-27), so the owner runs this.
  figure: PINNED at the paired run's date and sha; nothing re-derives it.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `pre-push run-log line` · `push-main self-test` · `check-wiring self-test` · `settings-merge selftest` · `run-gates canary` · `run-gates evidence` · `run-gates turnstile` · `run-gates gov canary` · `foreign-prefix parity (every self-test at three prefixes)` · `run-gates run-log line` · `run-gates adopter e2e` · `profile-bar selftest` · `install-prefix self-test` · `dead-path carriers self-test` · `lexicon naming predicates` · `spec-tokens self-test` · `kit-placeholders self-test` · `branch-guard self-test` · `pre-push self-test` · `pre-push bar self-test` · `transition-audit arms` · `straggler-guard arms` · `every held leg is budgeted, every budget row resolves` · `kit version markers`

New arm: tools/run-gates/held_halves.py --selftest · covers AC1 AC2 AC5 · each refusal staged by a synthetic half that breaks one precondition, RED observed before landing · a new held leg and its budget row

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
- **F2 — Which distro and clone path is the declared host?**
  - (a) Conf keys in `.githooks/gate-env.sh`: `GATE_WSL_DISTRO` defaulting to `claude-u26`, the
    machine's default distro, and `GATE_WSL_MIRROR` defaulting to `/c/projects/coding-governance`,
    which matches the charter render path and the `/c/` spelling in `.process-monitor.conf`.
  - (b) The same keys with the mirror at `~/gov-mirror`, which needs no root-owned `/c`.
  - (c) No keys; the wrapper takes both as arguments on every run.
  - Recommendation: (a). The keys are blank in the landed file, so nothing runs until the owner sets them.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

The probe, `tools/codebase-map/reuse_lookup.py`, asked "run a subset of gate legs from an alternate
manifest and combine verdicts", names no seam that runs halves; its closest reader is `parse_verdicts` in
`tools/run-gates/profile_bar.py`, which the combiner imports for verdict lines instead of re-parsing
them. The runner seam extended is `GATE_LEGS` (`run-gates.sh:216`), already honoured by
`run-selftests.sh`.

Recall terms used: WSL linux host windows-latest remote-ci held self-tests gate-full-green stamp combiner parity platform
