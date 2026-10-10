# Appendix — Running the gate bar or its self-test tier inside WSL2: feasibility, design and risks

**Serves:** research TOOL-aMeteredSweep-1

A read-only research pass by one of five agents on 2026-10-09, kept verbatim below its first heading. Figures are estimates from static counts and one-line timings unless marked measured; the ranked synthesis is `2026-10-09-build-TOOL-aMeteredSweep-1-research2-menu.md`.


This is read-only research on node `a` at worktree `gate-runner-profiling-optimization-5d1f1e`, HEAD `6bc6c949c`. No leg, suite or runner was executed. No repo file was edited and nothing was installed. The probes are listed at the end with their output. Line numbers refer to the worktree's files.

## Summary

- **It is feasible, and the spawn gap is real.** A spawn costs 1.07 ms in WSL. Under MSYS the same spawn cost 818 ms this session, under a neighbouring bar's load, against a recorded quiet floor of 21 ms. A whole scratch-repo fixture cycle (`init`, `add`, `commit`, `log`) takes 23 ms in WSL and 4052 ms under MSYS, which is 175x.
- **The bar cannot run against the Windows checkout.** A linked worktree's `.git` file holds `gitdir: C:/projects/...`, which Linux git cannot open. Even the primary tree costs 45 to 91 ms per git verb over 9P. A run needs its own clone on WSL's ext4 filesystem.
- **There is a hazard to the shared `.git`.** Linux git reads every Windows worktree as `prunable`. A `git worktree prune` or `gc` run from WSL against `C:/projects/coding-governance/.git` would delete the admin dirs of all 18 linked worktrees. The Windows repo may only ever be a read-only fetch source.
- **The premise about CI is wrong.** `.github/workflows/remote-ci.yml` runs `bar`, `held-plan` and `held` on `windows-latest` (lines 47, 88, 126 and 277). It avoided Linux on purpose: "a Linux runner's first reds would measure the host rather than the tree" (lines 19-20). No Linux evidence exists today.
- **The Windows-only set is small for the default bar and wider for the self-tests.** Among the repo-subject legs, only `process-monitor wiring` is sure to go red under Linux. About 15 self-test suites carry Windows-only arms: MSYS pid mapping, `tasklist`, the WSL-launcher guards, 8.3 paths, junctions, and PowerShell CIM. Under Linux those arms either take a branch that no registered node runs (`resume-tick.sh:167-168`: "no registered node is POSIX") or announce a SKIP.
- **Recommended order.** First move the self-test tier, which grants no landing authority. Then gather paired-run parity evidence. Only after that, split the bar behind a combiner that alone may write `gate-full-green`. The runner itself should not change, because it grades itself (`run-gates.sh:20-25`).
- **Expected saving, not measured.** Spawn-bound bash and git-fixture legs should gain 10-30x on a quiet host and more under load. Python-heavy legs should gain 5-15x and node-bound arms about 1-3.5x. The 13,324 s bar would land somewhere around 15 to 45 minutes, set by the longest leg and by the real-time sleeps inside the suites.

## Ranked findings

1. **[blocker, design] WSL cannot use the Windows trees, so it needs an ext4 mirror.** Probe 2 printed the worktree's `.git` file as `gitdir: C:/projects/coding-governance/.git/worktrees/...`. Probe 1 got `fatal: not a git repository` for every git call in the worktree. Against the primary tree over 9P, `rev-parse` cost 44.5 ms, `cat-file -p HEAD^{tree}` 91.2 ms and `log -1` 68.8 ms. On ext4 a whole `init`/`add`/`commit`/`log` cycle costs 23-41 ms.
2. **[data-integrity hazard] Linux git reads all 18 Windows worktrees as prunable** (probe 2, `git worktree list`). No WSL process may write to `C:/projects/coding-governance/.git`. That rules out `prune`, `gc`, `fetch` into it and `worktree` verbs. Reading it with `upload-pack`, as a fetch source, is safe.
3. **[authority] A WSL green certifies code paths that production does not run.** Every `case "$(uname -s)"` in the kits takes its non-MSYS branch under WSL. Examples are `lib-unattended.sh:506-532` (tasklist and CIM against `kill -0`), `resume-tick.sh:172-197` (taskkill and Start-Process against setsid and pgid kill), and the 7 MSYS blocks in `unattended.test.sh` (7292, 7433, 7479, 7648, 9147, 9673, 9837). `resume-tick.sh:167-168` calls the POSIX branch UNVERIFIED. A WSL green says nothing about the branch every node executes.
4. **[CI premise] Remote CI is Windows, deliberately** (`remote-ci.yml:19-24`, `47`, `88`). So the first WSL bars are a platform port. Expect host-caused reds before any tree-caused ones.
5. **[sure break] `process-monitor wiring` (leg 67) reds under Linux.** `.process-monitor.conf` declares `PROCMON_ROOTS="C:/projects/coding-governance /c/projects/coding-governance"`, and `adopt-process-monitor.sh:141-144` adds a problem for every root that is `! -d`. Neither spelling is a directory in WSL.
6. **[cost trap] Windows interop PATH.** WSL's PATH carries 31 `/mnt/c` directories. One `command -v` miss costs 48 ms with them and 0.87 ms without (probe 3). Every probe for an absent tool pays that, so the run must strip `/mnt/*` from PATH, or set `[interop] appendWindowsPath=false`. The same step keeps `tasklist.exe`, `powershell.exe` and `cmd.exe` out of reach. The code calls bare names today, so nothing leaks in yet.
7. **[width] WSL sees 16 GB, so the profile drops to `modest`, width 4.** `.wslconfig` sets no `memory=`, so the VM gets half the host: `MemTotal 16336540 kB`. `gate-profiles.txt` needs 24000 MB for the `capable` row. Fix it with `memory=` in `.wslconfig`, or with `GATE_PROFILE=capable` in the wrapper.
8. **[ceilings stop meaning anything]** Every leg ceiling and every `selftest-budgets.txt` row was measured on MSYS. They are 10-100x loose for WSL, so "cost is a verdict" (§7) cannot fire there. `derive-ceilings.py` is monotone (`ceiling-evidence.txt` header), so WSL readings would never lower a ceiling. The census `foreign` field cannot see Windows processes from inside WSL, though, so contended WSL readings would read as clean (`derive-ceilings.py` docstring, "WHAT THE CENSUS CANNOT SEE").
9. **[bytes] A Linux clone matches CI's line endings, not node `a`'s.** Node `a` has global `core.autocrlf=true`, and the worktree holds 110 `w/crlf` files plus 1 `w/mixed`: `.py`, `.js` and `.json` under `tools/` not pinned `eol=lf` by `.gitattributes`. CI forces `autocrlf=false` (`remote-ci.yml:53-56`), and so does a WSL clone, where the setting is unset. Byte-level legs grade different bytes than node `a` does. There is a benefit too: MSYS awk and grep drop CR (memory note `msys-awk-and-grep-drop-cr`), so CRLF arms that cannot red on node `a` can red in WSL.
10. **[new hazard] `claude-u26` is now the default WSL distro**, and it ships python 3.14 (`wsl -l -v` shows `* claude-u26`). The guarded class "a Windows python's bare `bash` resolves to the System32 WSL launcher" (`govkit.py:1012-1024`, `corpus_ids.py:391`, `row_grammar.py:1890`, `merge-rows.py:220`, `settings-merge.py:924`) used to fail loudly, because the launcher's distro had python 3.10 and no tomllib. It can now pass silently while reading `/mnt/c`. The `resolve_bash` guard arms (`govkit/selftest.py:14269-14282`) still catch it structurally, but only on a full bar.

## 1. What is Windows/MSYS-specific and must keep running on Windows

| leg (index in `gate-legs.json`) | Windows-only content | under Linux | evidence |
|---|---|---|---|
| 67 process-monitor wiring | roots `C:/...` and `/c/...` must be directories | **RED** | `.process-monitor.conf`; `adopt-process-monitor.sh:141-144` |
| 68 process-monitor census selftest | windows-join backend: CIM joined to `ps -W` | 4+ arms announce SKIP | `process-monitor/selftest.py:133,272-273,291-292,493-494,523-524`; `census.py:224,232` |
| 69 process-monitor adopter selftest | roots and live census bound | probably red or skip; verify | `.process-monitor.conf`; adopter roots checks |
| 25 scratch-guard self-test | `USERPROFILE`, `TEMP` 8.3 short names | arms run against fixture env, but the 8.3 contraction is never real | `hooks/scratch-guard.js:106-119`; `scratch-guard.test.sh:151-160,370-380` |
| 98 govkit selftest, 111 govkit matrix | `resolve_bash` must avoid System32/WindowsApps | arm trivially true | `govkit/selftest.py:14269-14282`; `govkit.py:1012-1024`; `matrix.py:753` |
| 35 corpus-ids, 37 row-grammar, 29 merge-rows, 100 lexicon, 65 drift-audit, 60 settings-merge, 70 runlog selftests | the same WSL-launcher and Windows-python class | arms trivially true or take the POSIX branch | `corpus_ids.py:391`; `row_grammar.py:1890`; `merge-rows.py:220`; `lexicon/selftest.py:48-52`; `drift-audit/selftest.py:158`; `settings-merge.py:924`; `runlog/selftest.py:2104-2124,8082` |
| 87 profile-bar selftest | PowerShell `Get-CimInstance` command lines | reports `unverified` | `profile_bar.py:211-215,285` |
| 46 check-wiring self-test | the remedy text differs per OS (PowerShell junction against `ln -sfn`) | the other branch runs | `check-wiring.sh:1241-1247` |
| 59 codebase-map adopter e2e | `cmd //c mklink //J` junction arm | the junction arm is not taken | `adopt-codebase-map.test.sh:235-238` |
| held: unattended driver shards 1-8 | winpid via `ps -p` col 4, `tasklist` stub arm, MSYS-only arms ("2 are the MSYS-only `tasklist`-stub arm") | the POSIX branch runs, which is UNVERIFIED in production | `unattended.test.sh:7292-7295,7433-7436,7479-7483,7648,9147,9673,9837,16452`; `unattended.test.sh:6713-6715` (junction) |
| held: resume-tick (the unattended kit suites) | `tasklist //FI`, `taskkill //T`, `Start-Process` | 11 MSYS branches switch | `resume-tick.test.sh:234-753`; `resume-tick.sh:167-197` |
| held: gate-guard, stall-recorder, stop-guard, recall-opened, pytest-guardrails | `cygpath -m` fallbacks | identity fallback | `gate-guard.test.sh:147`; `stall-recorder.test.sh:142`; `stop-guard.test.sh:141`; `recall-opened.test.sh:18-25`; `pytest-parallel-guardrails.test.sh:63-65` |
| held: adopt-unattended e2e | PowerShell junction arm | the arm is not taken | `adopt-unattended.test.sh:543-544` |

**Nothing to lose here:**

- `.ps1` scanning has no bar leg, and the repo tracks zero `.ps1` files (`gate-lint/README.md:164-169`).
- Event Viewer and WER appear only in prose and memory.
- `COMPUTERNAME` is read by the unattended driver (`lib-unattended.sh:423-427`), and its suite injects it as fixture env (`unattended.test.sh:15712-15944`), so that arm is portable.

**Gained under Linux:**

- `run-gates.test.sh:2763-2769`, the `/proc/<pid>/cmdline` absolute-argv arm, announces a SKIP on MSYS and would run in WSL.
- Linux enforces `chmod` modes, which MSYS does not (`run-gates.test.sh:2785`, `profile_bar.test.sh:213-215`).
- CRLF arms become observable.

## 2. What breaks or changes under WSL2

| subject | WSL reality (probed) | consequence |
|---|---|---|
| repo access | the worktree `.git` names `C:/...`, and git fails | an ext4 mirror clone is mandatory |
| 9P cost | `rev-parse` 44.5 ms, `cat-file` 91 ms, `bash -n` of `run-gates.sh` 20 ms on 9P against 11 ms on ext4 | the run must not touch `/mnt/c` |
| shared `.git` | Linux git sees 18 Windows worktrees as prunable | never write to the Windows `.git` from WSL |
| `python` | only `python3` (3.14.4); `python` and `py` absent | fine: `resolve_python` tries `python3` first (`resolve-python.sh:28`), and the runner maps `python`/`python3` argv[0] to `PYBIN` (`run-gates.sh:2368,3037`) |
| `node` | Linux ELF v22.22.1, 112 ms per start | node-bound arms gain little |
| `timeout -k`, `setsid`, `EPOCHREALTIME`, `nproc`, `/proc/meminfo` | all present: 16 cores, 16.3 GB, no cgroup `memory.max` | the runner's detection works (`run-gates.sh:376-437,703`); the profile becomes `modest` unless RAM is raised |
| `ps -W` | refused | the runner logs "no resolvable winpid; tree kills fall back" (`run-gates.sh:1017-1019`), announced and harmless |
| `ps -ef` | standard procps, argv cooked | the guard for cygwin raw argv (`run-gates.sh:763-766`) becomes inert |
| `cygpath` | absent; `wslpath` present | every caller already falls back (`cygpath ... 2>/dev/null \|\| ...`); CI's own steps use `cygpath` (`remote-ci.yml:172,321`) |
| TEMP/TMPDIR | unset, so the ambient is `/tmp`, a 7.8 GB tmpfs | `run-gates.sh:1477-1545` puts all leg scratch under it, in RAM. `foreign-prefix.gov.test.sh:143` clones `--no-hardlinks` (~100 MB each) and `manifest-check.test.sh:702` clones `--local` across filesystems, which copies. Point `TMPDIR` at an ext4 dir on the mirror's filesystem |
| `autocrlf` | unset, which equals CI | node `a`'s 110 CRLF working files become LF |
| `HOME` | `/home/ubuntu`, no `~/.claude` | checks of machine-local skill junctions see an empty install (`check-wiring.sh:1236-1247`) |
| charter render path | `derive_primary_tree` would answer `/home/...` (`render_playbook.py:259-268`) | `.governance/deploy.toml:38-39` now ANSWERS `primary_tree_a`/`worktree_root_a`, so the render should hold. `remote-ci.yml:20-22` still says the clone must sit at the primary path, so verify by experiment. A mirror at `/c/projects/coding-governance` is a cheap belt and also matches the `/c/` procmon spelling |
| impure legs 74-76 (`ls-remote`) | WSL networking is `Mirrored` | the mirror's `origin` must be the GitHub URL, never the Windows path, or these legs grade the local repo instead of the remote. Network and credentials from WSL were not probed |
| Windows tools via interop | `tasklist.exe` costs 2588 ms per call from WSL | strip interop from PATH |
| clock | not probed | WSL2 is known to skew after host sleep. Compare no timestamps across hosts in a combiner |

## 3. Design

**The shape: a wrapper, with no change to `run-gates.sh`.** The runner grades itself, and any diff touching it makes every red read OWN (`run-gates.sh:20-25`). The runner already accepts an alternate manifest through `GATE_LEGS` (`run-gates.sh:216`). So the split can be built outside it.

**The mirror, set up once.** Clone into ext4 at `/c/projects/coding-governance`, or `~/gov-mirror`, from `/mnt/c/projects/coding-governance`:

- Then `git remote set-url origin https://github.com/d41ly/coding-governance.git`.
- Add a remote `win` pointing at `/mnt/c/projects/coding-governance`, used only as a fetch source.
- Set `gc.auto=0` on nothing Windows-side.
- Size: 99 MB of objects, 82,596 packed in 7 packs, 50 refs and 3,642 tracked files (`git count-objects -vH`).
- Estimated time is 10-60 s over 9P plus about 2 s of checkout. That is not measured. The disk has 948 GB free.

**One run of `run-gates-wsl.sh` (proposed, Windows side):**

1. **Refuse a dirty tree.** WSL sees committed objects only. Pin `S=$(git rev-parse HEAD)` and `FP=$(gate-fingerprint.sh S)`. The two forms agree on a clean tree (`gate-fingerprint.sh:13-17`).
2. **Partition the manifest.** Write `legs-win.json` and `legs-wsl.json` from `gate-legs.json`, using a declared list of Windows-native leg names. That list starts with leg 67, plus whatever parity runs find. Ideally it becomes an additive manifest key such as `"host": "windows"`, read by the wrapper only. Note this moves `manifest_blob` and needs the canary's key-set pin (`run-gates.sh:56`).
3. **Run the WSL half.** Run `wsl.exe -d claude-u26 -- bash <mirror>/run-half.sh S`. Inside it:
   - `git fetch win <branch>`, then verify `S` exists.
   - `git worktree add --detach <mirror>/.wt/<runid> S`.
   - Export a PATH with `/mnt/*` stripped, `TMPDIR=<ext4 dir>` and `GATE_PROFILE=capable`, or raise RAM instead.
   - Run `GATE_LEGS=legs-wsl.json GATE_FULL=1 bash tools/run-gates/run-gates.sh`.
   - The mirror's own turnstile, beacon under the mirror common dir (`run-gates.sh:1044,1222`), serialises WSL halves from every Windows worktree.
4. **Run the Windows half at the same time.** Run `GATE_LEGS=legs-win.json GATE_FULL=1 bash tools/run-gates/run-gates.sh` natively. It takes the Windows beacon.
5. **Combine** with a small python script that reads both `gate-run/<runid>/*.leg` and `verdict` files. It REFUSES unless all of these hold:
   - the union of leg names equals the full manifest exactly once;
   - both verdict files exist;
   - both halves' fingerprints equal `FP`, and the WSL half's `HEAD` equals `S`;
   - neither half moved its tree;
   - both partition files derive from the same full `manifest_blob`.

   It then prints the leg lines in MANIFEST order, with the runner's own byte-stable shapes. It takes the worst exit code by the runner's precedence: 2, then 1, then 4, then 3, then 0 (`run-gates.sh:3-7`).
6. **Stamp.** Only the combiner writes `<windows gd>/gate-full-green`, with `sha S`, `fingerprint FP`, the full manifest's `manifest_blob`, `selftests` and `run_id`. It adds one additive field, for example `hosts windows:<runid>,wsl:<runid>`. A half run alone can never earn a usable stamp. Its `manifest_blob` is the partition's, so pre-push predicate 7 forces the full bar (`.githooks/pre-push:1225-1231`). That is a safe default, and it already exists.

**How each piece of state treats this design:**

- **Turnstile.** There are two beacons, one per common dir, so a Windows bar and a WSL half do not exclude each other. Both run on the same 16 cores. The Windows half is small, so the overlap is acceptable. A host-wide exclusion would be a wrapper-level lock.
- **Ledger and `gate-run`.** Each half writes its own git dir. Keep WSL readings out of `ceiling-evidence.txt`, or give that file a host column, because Windows ceilings must not be argued from Linux readings.
- **Spawn floor.** Each clone keeps its own `gate-spawn-floor` (`run-gates.sh:2274`), so HOST keeps its "this clone's floor" meaning. One caution: with a 1 ms floor and `GATE_HOST_RATIO=4` (`run-gates.sh:2271`), the 4 ms HOST threshold sits close to Linux noise. It matters only when legs time out twice.
- **Fingerprint.** Tree hashes come from objects, so they are identical across hosts. A clean Linux checkout reproduces the rev form.
- **Pre-push.** It is unchanged and stays the authority. It accepts the combined stamp only through its own predicates 2-8 (`.githooks/pre-push:1185-1240`), and its scoped legs still run natively.
- **CI.** It stays Windows. For low-cost continuous parity evidence, add a non-required `ubuntu-latest` job that runs the same bar report-only. That gives evidence without risking the per-sha verdict.

**The self-test tier is the low-risk first step.** `run-selftests.sh` grants no landing authority (`run-selftests.sh:12-17`). Run it in the mirror worktree, with `--attribute` L and R both inside WSL so attribution stays consistent within one host. The cost verdict against `selftest-budgets.txt`, measured on nodes `a` and `d`, is meaningless there, so print it as `n/a (host wsl)` rather than as under budget. The suites with Windows arms (section 1) still owe a Windows run, and the daily `held` job on `windows-latest` already provides one.

## 4. Expected savings

These are estimates from the probed spawn ratios, not measurements of any leg.

| class | per-call ratio (MSYS loaded / WSL) | quiet-host ratio | expected leg speedup | example legs (seconds on the last full Windows bar's ledger) |
|---|---|---|---|---|
| bash + coreutils spawn loops | `true` 818/1.07 = 760x; `$(:)` 284/0.97 = 290x; awk\|sed\|sort 1035/7.2 = 145x | ~20x (21 ms floor) | **10-30x** (CPU share ~7%, per `process-creation-is-the-suite-cost.md`) | manifest-check self-test 2162; run-gates canary 1340; evidence 823; agent-cap restatement; dead-paths; install-prefix |
| git-fixture suites | init+add+commit+log 4052/23 = 175x (ext4 41 ms, 100x) | ~20-40x | **15-40x** | row-keyed merge driver 886; memory-hygiene self-test 906; pre-push self-test 586; check-wiring 589 |
| python, startup plus git subprocesses | `python3 -c 0` 1107/14 = 79x; in-process CPU about 1x | ~5x | **5-15x** | govkit selftest 3445; drift-audit 755; memory-recall 656; lexicon 637; corpus-ids 599 |
| node-bound arms | `node -e 0` 398/112 = 3.5x | ~1x or worse | **1-3.5x** | agent-cap self-test 742; scratch-guard; workflow syntax |
| real-time sleeps and calibrated waits | 1x | 1x | none | turnstile suite (30 sleep sites, 2285 s red); canary (31); driver suite (34) |
| network (`ls-remote`) | 1x | 1x | the network part does not move | unattended kit gate 1538; pass-order 576; brief-recorded 490 |

**Legs that need the ext4 clone, because they are git-bound against the real repo:**

- Every repo-subject leg calls `git ls-files` or `rev-parse` at minimum.
- The heavy ones: memory hygiene (ceiling 12720), unattended kit gate (16040), pass-order (5400), playbook validity (4940), govkit acceptance matrix (7030), install-prefix and hook destinations (2940 each), manifest ratchet, dead-paths, codebase-map freshness, spec tokens, lexicon, and govkit epoch.
- Suites that clone the real repo: manifest-check self-test (`manifest-check.test.sh:702`) and foreign-prefix parity (`foreign-prefix.gov.test.sh:143`).

**Bar-level projection.** The profiled bar paid 54,049 pool leg-seconds over a 13,324 s wall at effective concurrency 4.06, and the record says the contended resource was process creation, not CPU (`research-runner.md`). At 10-20x that becomes about 2,700-5,400 leg-seconds. On WSL the bar turns CPU-bound, so width 8-16 is usable, and the wall is floored by the longest leg plus its sleeps: the canary or the turnstile suite. That gives about **15-45 minutes** against 3.7-6.9 hours. Adding the Windows half, about 10 small legs, adds little.

The saving disappears if the mixed suites go to the Windows half wholesale. govkit selftest alone was 3445 s. So they must run in WSL, with their Windows arms covered elsewhere.

## 5. Risks, and what must not change

**Must not change:**

- The exit-code set and precedence (`run-gates.sh:3-7`).
- Manifest-order, byte-stable reporting (`run-gates.sh:27-29`).
- The green-stamp preconditions: no fails, no skips, no reuses, no wall breach, no tree move, a clean tree and a written verdict (`run-gates.sh:3826-3829`).
- Pre-push predicates 2-8 and its authority to run the bar itself.
- `gate-legs.json` as the single source of legs.
- "A skip announces itself" and "a knob never turns a leg into PASS or SKIP" (`gate-profiles.txt` header).
- The rule that no grader grades itself.

**Risks:**

1. **Authority creep.** A WSL green exercises the POSIX branch of every `uname` case, and no registered node runs that branch. The Windows-native leg list must be declared and must be machine-checked to run on Windows, or the bar quietly certifies the wrong platform.
2. **Destroying the shared `.git`.** See finding 2. The wrapper must never export `GIT_DIR` or `GIT_COMMON_DIR` into WSL, and the mirror must never have a `/mnt/c` `.git`.
3. **Host-caused reds on first contact.** CI chose Windows for exactly this reason. Run N paired bars at the same `S`, one Windows and one WSL, and require equal per-leg verdicts before granting authority.
4. **Timing-tuned arms.** Arms calibrated or raced on a slow host may reorder on a fast one (`run-gates.test.sh:757,2307-2321,3151`; turnstile suite `:351,388`). Expect flakes the parity runs must catch.
5. **Ceiling and budget blindness.** WSL cannot red on cost, and its census cannot see Windows load. The two must stay host-separated, never merged into `ceiling-evidence.txt`.
6. **Memory.** The vmmem VM counts as used memory on the Windows side, so the Windows half's `mempause=90` holds more often. Inside the VM, `/tmp` is a 7.8 GB tmpfs.
7. **Mirror lag and identity.** The combiner must assert the WSL HEAD is exactly `S`, and must not trust a branch name.
8. **The default-distro side effect.** See finding 10. Mis-resolved `bash` from a Windows python now runs successfully instead of failing.
9. **Lifecycle.** `wsl --shutdown`, a Windows Update reboot (memory note `windows-update-reboot-kills-detached-runs`) or the VM idling out kills the WSL half. The combiner must treat a missing verdict as REFUSED, exit 2, never as green.
10. **Interop.** A stray `*.exe` call from WSL costs seconds (`tasklist.exe` 2.6 s) and mixes process namespaces. Strip it.

## Probes run (all read-only; scratch dirs removed)

Scripts are in this scratchpad: `wslprobe1.sh`, `wslprobe2.sh`, `wslprobe3.sh`, `msysprobe.sh`, `msysprobe2.sh`, with outputs `wslprobe2.out` and `wslprobe3.out`.

**Environment.** WSL: `Linux 6.18.33.2-microsoft-standard-WSL2`, Ubuntu 26.04 LTS, user `ubuntu`, nproc 16, MemTotal 16336540 kB, SwapTotal 16738304 kB, no cgroup `memory.max`, bash 5.3.9, git 2.53.0, Python 3.14.4, node v22.22.1 (Linux ELF), `python`/`py` ABSENT, `cygpath` ABSENT, `wslpath`/`setsid`/`timeout`/`flock` present, `timeout -k runs`, EPOCHREALTIME set, TMPDIR/TEMP unset, `ps -W refused`, autocrlf unset, `/etc/wsl.conf` `[boot] systemd=true [user] default=ubuntu`, 31 `/mnt/c` PATH entries, `/` 948 GB free, `/tmp` tmpfs 7.8 GB, `ulimit -u` 63771. `.wslconfig`: `networkingMode=Mirrored`, `swap≈16 GB`, no `memory=`. `wsl -l -v`: `* claude-u26 Running 2`, `docker-desktop Running 2`.

**WSL costs per call:**

| operation | cost |
|---|---|
| `/bin/true` | 1.066 ms |
| `$(:)` | 0.972 ms |
| `bash -c :` | 3.762 ms |
| `git --version` | 2.518 ms |
| `python3 -c 0` | 14.301 ms |
| `node -e 0` | 112.078 ms |
| awk\|sed\|sort | 7.15 ms |
| `date -u` | 4.09 ms |
| `command -v` miss, Windows PATH on | 48.07 ms |
| `command -v` miss, Windows PATH off | 0.87 ms |
| scratch repo cycle on tmpfs | 23.42 ms |
| scratch repo cycle on ext4 | 41.34 ms |
| `tasklist.exe` via interop | 2588 ms |
| loadavg | 0.15 |

**WSL git over 9P:**

- Primary tree: `rev-parse HEAD` 44.538 ms, `cat-file -p HEAD^{tree}` 91.185 ms, `log -1` 68.776 ms, `ls-files` 37 ms for 3667 files, `grep -c` over `tools/*.sh` 157 ms.
- Linked worktree: `fatal: not a git repository: .../C:/projects/coding-governance/.git/worktrees/...`.
- `git worktree list` marks the Windows worktrees `prunable`.
- CR bytes in `run-gates.sh` and `AGENTS.md` on the Windows checkout: 0 each.
- `bash -n run-gates.sh`: 20.2 ms on 9P, 10.8 ms on ext4.

**MSYS, same session, neighbour bar running, 12 bash.exe on the box:**

| operation | cost |
|---|---|
| `/usr/bin/true` | 818.3 ms |
| `$(:)` | 283.5 ms |
| `bash -c :` | 459.9 ms |
| `git --version` | 431.3 ms |
| `python3 -c 0` | 1106.5 ms |
| `node -e 0` | 397.6 ms |
| `rev-parse HEAD` | 668.7 ms |
| `bash -n run-gates.sh` | 570.1 ms |
| scratch repo cycle | 4051.6 ms, with "LF will be replaced by CRLF" warnings, so global autocrlf=true |
| awk\|sed\|sort | 1035.1 ms |

**Repo state:**

- `git count-objects -vH`: in-pack 82596, 7 packs, size-pack 84.83 MiB; `.git/objects` 99M; 50 refs; 19 worktrees.
- `git ls-files --eol`: 3528 `w/lf`, 110 `w/crlf`, 1 `w/mixed`, 3 `w/-text`.
- Last full ledger (`C:/projects/coding-governance/.git/gate-ledger.tsv`), leg-seconds by chunk: selftests 20329, declarations 4094, held unattended 1740, e2e 301, product 225, records 202, wiring 110; 27000 in total.
