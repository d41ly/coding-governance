# Disk-churn analysis — the measured report this build was asked from

**Serves:** research TOOL-dQuietDisk-19

Copied whole below the rule, its headings demoted one level and nothing else changed, from the analysis session's notes folder (`side-session-notes/local_22c30fbd-4971-4107-b3d9-acd2fca20e6a/disk-churn-analysis.md`, 45,125 bytes, written 2026-11-20 04:31), because that folder is not durable. Its BASE is gov `608aa364c`.

---

## Why C: sits at 100% active time: small-file and git-process churn in gov, incms and nicocares

**Date:** 2026-11-20
**Scope:** analysis only. Nothing in `coding-governance`, `incms/main` or `nicocares-package` was edited, committed or deleted. All runs were in a throwaway `git clone --shared` of gov, made in a scratchpad with its own `TEMP`.

**Evidence labels:**
- **[M]** measured on this machine.
- **[C]** counted read-only from code or the file system.
- **[E]** estimate. The arithmetic is shown each time.

---

## 0. Summary

The disk is not short of bandwidth. It is serialized on **NTFS metadata updates**: MFT records, directory `$I30` indexes, `$LogFile` and the USN journal. On top of those sits **process creation**: every `git`, `python`, `node` and `bash` launch costs 10–40 ms even on an idle disk [M].

Four design habits create that load:

1. **Hermetic fixtures built from nothing, again and again.** Throughout the gov kit selftests, each case runs `git init` → configure → commit, or copies the kit or the whole 13.9k-file tree into a scratch dir.
   - The static count is 534 `git init`, 101 `worktree add`, 61 `clone`, 110 tree copies, 269 `mktemp -d` and 330 `mkdtemp`/`TemporaryDirectory` [C].
   - Adopters copy those selftests and run them again (incms gov-bar, nicocares nc-bar).
2. **Verdicts re-derived from history on every commit.** The history legs put `head $RG_HEAD` into their cache key (`tools/run-gates/run-gates.sh:3370`), so they never reuse a result across commits. They then ask git one question per process: about 11.5k git processes for `check-pass-order` alone [C/E].
3. **Whole-bar "baseline" runs and duplicate checks.** `govkit apply` runs the target's whole bar before writing and again after (`tools/govkit/govkit.py:7763`, `:8465`). Regen pre-flight repeats about 8 checks that are also legs in the same bar.
4. **Output that is never swept.**
   - 202,037 media files in incms `services/api/var/media` [M].
   - 447,230 files under gov `.claude/worktrees` and 308,338 under incms `.claude/worktrees` [M].
   - A 1.7 GB recall cache [M].
   - 11,442 `gate-cache` entry files [M].
   - Temp leaks whenever a run is killed.

Two machine settings multiply all of this, and both are easy to change:
- **8.3 short-name creation is ENABLED on C:** [M]. That is the known pathology for directories with hundreds of thousands of entries, which `%TEMP%` had.
- **Last-access updates are ENABLED** [M].

**Antivirus is not the multiplier** [M]: no AV minifilter is loaded, `ekrn.exe` is absent from disk, and the ESET entry in SecurityCenter2 is stale.

**Dev Drive is disabled by group policy** [M].

---

## 1. Machine facts (measured)

| Fact | Value | How |
|---|---|---|
| Physical disk | One "Intel Raid 0 Volume", 2.05 TB, holding **both C: and D:** | `Get-PhysicalDisk`, `Get-Partition` |
| C: | NTFS, 540 GB, 63 GB free (88% used) | `Get-Volume` |
| D: | NTFS, 1,367 GB, 145 GB free (89% used). **Same physical RAID**, so moving TEMP to D: does not remove contention | `Get-Partition` |
| V: | 2 GB FAT32, file-backed virtual disk labelled "OPSNEW". Purpose unknown, not considered | `Get-Volume` |
| Filter drivers | `bindflt, FsDepends, UCPD, storqosflt, wcifs, CldFlt, bfs, FileCrypt, npsvctrig, Wof, FileInfo`. **No WdFilter, no ESET eamonm/ehdrv** | `fltmc` |
| ESET | SecurityCenter2 still lists "ESET Security", but `C:\Program Files\ESET\ESET Security\ekrn.exe` does not exist and no service is running. **The entry is stale. AV is ruled out** | `Test-Path`, `Get-Service` |
| Windows Search | Service disabled | `Get-Service WSearch` |
| 8.3 names on C: | **ENABLED** (volume state 0) | `fsutil 8dot3name query C:` |
| Last-access updates | **ENABLED** (`DisableLastAccess = 2`, system managed) | `fsutil behavior query disablelastaccess` |
| Dev Drive | "Developer volumes are disabled, by group policy" | `fsutil devdrv query` |
| MFT | 5.07 GB valid data, about 5.3M file records at 1 KiB each. The MFT never shrinks after mass deletes | `fsutil fsinfo ntfsinfo C:` |
| USN journal | 32 MB ring; journal created 2023-09-09; next USN = 146 GB, about 1.46 **billion** change records over 1,167 days, **about 1.25M records/day on average** | `fsutil usn queryjournal C:` |
| Idle baseline right now | 98% idle, about 490 transfers/s, 3.8 MB/s | `Get-Counter` 10 s |
| Spawn cost, idle disk | `git rev-parse` **21 ms**, `python -c 0` 25 ms, `node -e 0` 39 ms, msys `true` 10 ms | 100× / 50× loops |
| `mktemp -d` + `git init` + `rm -rf` | **57 ms**, and a fresh `git init` makes **28** entries | 20× loop |
| Raw small-file rate (Python, uncontended) | create about 9–12k entries/s, stat-walk about 43k/s, delete about 17–20k/s | 10k-entry benchmark in scratch |
| `git checkout` of gov (13,882 files) | **12.5 s**, about 1,100 files/s | throwaway shared clone |
| Git `core.fsync` | Default. `committed` / `none` / `all` cost 84 / 80 / 93 ms per add+commit, so **fsync is not the multiplier; process spawn is** | 40-commit loop each |

The per-operation cost on an idle disk is small. The trouble is volume: hundreds of thousands to millions of operations per bar, 8 legs wide, across several concurrent sessions and worktrees. Every create or delete takes the same NTFS volume-wide resources: the MFT, the parent directory index, and the log. So Task Manager's "active time" sits at 100%, meaning there is always at least one outstanding I/O, while bytes/s stays low.

---

## 2. Representative runs (measured in an isolated copy)

All three runs used a `git clone --shared` of gov at `608aa364c`, with `TEMP`/`TMP`/`TMPDIR` pointed at a scratch dir and `GIT_TRACE2_EVENT` set to count git processes. A watcher sampled peak entries in TEMP every 0.5 s.

| Suite | Wall | git processes | Top git subcommands | Peak entries in TEMP | Residue |
|---|---|---|---|---|---|
| `tools/check-line-length.test.sh` (20 arms; uses `lib-selftest.sh`, the one shared-template helper) | 13.9 s | 57 | rev-parse 45 | 1,189 | 0 |
| `tools/govkit/census.test.sh` (12 arms) | 5.7 s | 65 | hash-object 14, config 8, init 4 | 234 | 0 |
| `tools/check-wiring.test.sh` (255 arms, 42 `newrepo` calls) | **307.7 s** | **3,786** | **ls-files 1,679**, rev-parse 511, check-attr 421, config 400, ls-tree 186, hash-object 178, remote 94, maintenance 46, commit 41 | 524 | 0 |
| `check-wiring` re-run, sampled with the C: USN journal | 350 s | 3,786 (identical) | same | 526 | 0 |

**What the USN sample shows.**
- The C: change journal advanced **10.46 MB** during the re-run, about **105k change records** at about 100 B each.
- The idle baseline measured just before was about 10 KB/s, or about 3.6 MB over 350 s. That leaves **about 6.9 MB, roughly 69k NTFS change records, attributable to one 255-arm suite: about 18 metadata records per git process.** These come mostly from `.git/index.lock` create/rename, `config.lock`, ref locks, loose objects, and the arm's own files.
- The disk-counter part of this sample failed (a regex bug in my wrapper), so only USN numbers are reported for it.

Two points about these numbers:
- **8 of check-wiring's 255 arms fail in the copy.** The copy has no `origin` and lives under a different path. This does not change the I/O picture.
- **check-wiring's cost is mostly processes, not temp files.** It averages 12 git processes per second for 5 minutes. 1,679 `ls-files` calls means the graded tree is re-listed once per check, not once per suite.
- **[E] Extrapolation.** The selftest population is 126 rows, whose budgets sum to about 125,500 s; those budgets are worst readings ×1.5, so about 84k s of real work. At check-wiring's density of about 12 git/s, a full `GATE_SELFTESTS=1` run is **on the order of 1M git processes**, plus the bash, python and node processes around them. Treat this as an order of magnitude, not a measurement.

---

## 3. Offending workflows

Here, "file ops" means create + write + delete of one entry; a stat or list is a "read op".

| # | Workflow (entry point) | Trigger and frequency | Operations per run | Evidence |
|---|---|---|---|---|
| **G1** | **Gov kit selftests**: `run-selftests.sh --serial/--pooled`; `GATE_SELFTESTS=1\|changed run-gates.sh`; chunk `selftests` legs | By hand / Definition of Done for kit work. `GATE_SELFTESTS=changed` runs only legs whose kit moved. Not on every push (`run-gates.sh:3277`; `AGENTS.md:236`). Daily CI runs off-box | [E] about 1,500–3,000 repos or repo copies, tens of thousands of commits, about 280 nested `run-gates.sh` bars, 7–10 full copies of the 13.9k-file tree (≈100–140k files written and deleted), **about 1M git processes** | §2; static counts in §0; `selftest-budgets.txt` (126 rows); `ceiling-evidence.txt` (govkit selftest 3,359 s, foreign-prefix 2,494 s, run-gates canary 2,305 s, memory-hygiene 1,970 s, manifest-check 1,401 s, run-gates evidence 1,385 s, turnstile 1,280 s, policy fixtures 1,210 s) |
| G1a | ↳ `unattended/unattended.test.sh` (8 shards) | in G1 | Prologue rebuilds repo + bare origin **in each of 8 shards**; 425 `reset_tree` calls (checkout + `reset --hard` + `clean -fd`); 1,509 driver runs | 53 `mktemp -d`, 36 `init`, 484 commit sites [C] |
| G1b | ↳ `govkit/selftest.py` | in G1, and the "govkit selftest" leg | 102 `build_target`/`build_scratch_gov` calls (each is `init` + 6 `config` + commit, about 9 spawns); 144 `apply` calls each writing kit files; one clone of gov at `:5867` | `fixture_target.py`; 63 `init`, 176 commit sites [C] |
| G1c | ↳ `run-gates/foreign-prefix.gov.test.sh` | in G1 | `clone --no-hardlinks` of all 13,882 files (`:453`), `git mv` of the tool root **×3 prefixes**, then every suite's prologue at each prefix | 2,494 s ceiling |
| G1d | ↳ `run-gates.test.sh`, `.turnstile`, `.evidence`, `.githooks/pre-push.test.sh` | in G1 | 134 + 70 + 39 + 39 nested **whole bars**, each with its own `gate-work.*` dir and run records; `pre-push.test.sh` has 49 fixture builders and 75 real pushes | [C] |
| G1e | ↳ `policy/check_policy.py --fixture`, `loop/factories.py` | in G1 | `build_source_snapshot` = `clone --shared` **+ full checkout** of the tree (`check_policy.py:1270-1290`), called at `:1411` and `:5127`, and twice more from `loop/factories.py` | [C] |
| G1f | ↳ `govkit/upgrade_walk.py` | its leg (7,177 s ceiling) | Full clone of gov checked out at the pin, then walked to the tip | [C] |
| **G2** | **Copies of the kit selftests in adopters**: incms `scripts/gov-bar.sh:34` (53 gov legs), nicocares `scripts/nc-bar.sh` (124 legs) | **Every incms bar** (`scope: always`) and every nc bar | [E] about 25 throwaway repos × about 28 entries + about 150 commits × about 4 loose objects ≈ **1.2k creates + 1.2k deletes**, plus a few hundred git processes per suite; kit selftests such as `pre-push.test.sh`, `push-main.test.sh`, `check-wiring.test.sh` and `check-microformats.test.sh` run in every adopter | incms `scripts/run-gates/gate-legs.json` [C] |
| **G3** | **History-grading legs**: `tools/unattended/check-pass-order.sh`, `check-brief-recorded.sh`, `routed_commits.py`, `skills/session-kickoff/manifest-check.sh` | **Every bar** (they declare `history`, so the key includes HEAD) | pass-order: 134 builds × about 5 + about 1,800 units × about 6 ≈ **11.5k git processes, about 17k processes in all** (1,054 s). brief-recorded: about 6–8k (404 s). routed_commits: a `git log --raw --numstat` over **all 9,856 commits** (1,761 s; it inflates packs rather than spawning). manifest-check: unscoped `git log -G` pickaxe (`:1971`) | `run-gates.sh:3370`; `lib-unattended.sh:1323`; `check-pass-order.sh:475-531, 599-630`; `check-brief-recorded.sh:520-619`; `routed_commits.py:353, 410-413` [C] |
| **G4** | **`govkit update`** | Each kit-upgrade step, per adopter | About 3 unbatched `git show` per receipt row × 242–293 rows ≈ **810 git processes**; `hash-object` + `show` per rendered row; each touched kit's `adopt-*.sh --check` **twice** (`:11169` pre-write, `:12507` verify), about 22 kits × 10–16 s. Likely the bulk of the 3.5 min | `govkit.py:9993, 9244-9245, 9481, 9490`; `upgrade_steps.py:2628` [C] |
| **G5** | **`govkit apply` baseline** | Each apply | **Two whole target bars**, about 100 legs each, before and after writing | `govkit.py:6239` docstring, `:7763`, `:8465` [C] |
| **G6** | **Fixed cost of each `run-gates.sh` bar** | Every bar, in every repo and worktree | regen pre-flight: 15 checks, 4 wide, about 8 of them duplicates of legs (`run-gates.sh:1580-1595`); a serial `git diff --quiet BASE -- guard` per guarded leg (`:3249-3295`); up to 11 `$WORK/$i.*` files per leg (about 1,000 per bar); about 120–300 `.leg`/log files kept per run in `.git/gate-run`; a list + stat of all **11,442** `gate-cache` entry files to prune (`:5669-5679`); about 100 interpreter starts, and 36 scripts probe for python up to 3 times each | [C]; `.git/worktrees/*/gate-run/*` holds 121–296 files per run [M] |
| **G7** | **nicocares `v3_seeded` fixture** (`tests/v3_harness.py:191-264`) | Every incms python-scope bar (`scripts/check-vendor-suite.sh:62`) **and** every nc bar (`scripts/run-core-venv.sh:45`). **The same suite runs twice across the two bars** | 31 seeded tests × about 85 entries (mkdtemp, `v3.db` + journal, `copytree` of 66 files / 11 dirs, inline media, an unused `tmp_path`) ≈ **2.6k creates + 2.6k deletes**, plus **31 × 44 = 1,364 permanent files** in `services/api/var/media` per run | Function-scoped fixture with `create_all` + RBAC + full package install per test; `STORAGE_LOCAL_PATH` unset, so storage falls back to `./var/media` (`services/api/app/core/config.py:1078`). **`var/media` now holds 202,037 files** [M]; 251 leaked `ncv3-test-*` dirs [M] |
| **G8** | **incms `pytest-parallel`** (`-n auto --dist loadfile`, 16 workers) | Every python-scope bar | 9,824 tests in 830 files. The DB layer is fine: session-scoped, 16 files, `synchronous=OFF`, `journal_mode=MEMORY` (`tests/conftest.py:684-752`). But 880 `tmp_path` tests × 5–20 files ≈ **5–15k creates**, plus 54 mkdtemp sites | [C]; leaked now: 1,129 `incms-test-media*`, 80 `companion-probe-*` [M] |
| **G9** | **incms `scripts/gate.sh`** itself | Every bar | Multiplies G7, G8, G10 and G11: it never redirects `TMPDIR` (unlike `run-gates.sh:2333-2358`), so a killed leg leaks into `%TEMP%`. Its own `mktemp` files leak too: the `PG_URL…TP_ARGV` table files leaked in pairs at 21:32, 22:10 and 22:53 on 11-19 | `gate.sh:121, 126, 346, 611, 689` [C]; leaked tmp files [M] |
| **G10** | **incms `web-build`** (`apps/web/build-check.sh:34`, `next build`, `output: "standalone"`) | Full bar | About **4.6k deletes + 4.6k creates** per run (`.next/server` 475 + `static` 281 + `standalone` 3,750 + `types` 102). It bypasses the turbo `build` cache | `next.config.mjs:143, 147` [C] |
| **G11** | **incms `reachability-e2e` + `a11y-e2e`** | Full bar, two packs | Two `next dev` compiles (`.next/dev` about 4.7k files), two 15 MB sqlite reseeds, and media ingest of about 900 files per pack into `var/media` [E] | `apps/web/e2e/reachability/run.sh:141-177` [C] |
| G12 | **incms `js-test`** (turbo, 720 vitest files) | Every bar | The cache is honoured, but every package's `test` inputs include `../../apps/web/**` and `../../packages/**`, so almost any change misses for all 4 packages. `.turbo-cache` has 4,308 entries and is never pruned. Leaks: `incms-pack-verdict-*`, `incms-a11y-verdict-*` (21 each) | `turbo.json:36-71`; `e2eStackContract.test.ts:724, 834` [C]; 11 MB cache [M] |
| **G13** | **Claude Code hooks** (`.claude/settings.json`) | **Every tool call**, in every session | Each Bash/PowerShell call starts 4 `node.exe` (scratch-guard, gate-guard, procmon-hook, the atlas hook) ≈ 160 ms of spawns [M: 39 ms each]. `procmon-hook` runs python `reap.py` → PowerShell `Get-CimInstance` every 300 s. `gate-guard` reads every `memory/builds/*/RUN.md` on gate- or push-like commands. The atlas hook does `git worktree add` (**13.9k files**), regenerates, then removes the worktree, about once a day | `tools/hooks/scratch-guard.js:735-758`, `tools/unattended/gate-guard.js:777-781`, `tools/process-monitor/procmon-hook.js:159-170` [C] |
| G14 | **memory-recall** (`tools/memory-recall/query.py`) | Each query, and each `Read` via `recall-opened.js` | One `chunks.db` of about 440 MB per worktree (`.git/recall/cache` = **1.7 GB**); each query stats every corpus file for freshness (`query.py:282-300`) | [M] size, [C] code |
| G15 | **Regen and generators**: `gen_build_index.py`, `codebase-map/gen_map.py`, `lexicon.py` | Regen stage of each bar, plus by hand | `gen_map._write` **rewrites unchanged files** (`gen_map.py:156-158, 268-269`), which bumps mtime and makes git re-hash them; extractors walk `tools/` several times with `os.walk`; the `gen_build_index` render stamp is keyed on HEAD, and computing the key needs `ls-files` + `diff HEAD` + an untracked walk (`:1184-1199`); `lexicon.py` reads all 13.9k tracked files each run | [C] |
| G16 | **Worktrees nested inside repos** | Always present | gov `.claude/worktrees`: 70 dirs, **447,230 files**. incms `.claude/worktrees`: 25 dirs, **308,338 files**. Plus 10 incms and 11 nicocares sibling worktrees. Hidden from git only by `.git/info/exclude`; any raw walk pays for them (`adopt-memory-tree.sh:756, 788`; the `map_lib.py:849` fallback; the VS Code watcher, with no `files.watcherExclude` set). `.git/worktrees/*` metadata holds another **29,204 files** | [M] |
| G17 | **`swy-*` leak** (not governance) | Each run of swydee's PowerShell analyze tests | `C:\projects\swydee\tests\Test-Analyze.ps1:411` makes `swy-<guid10>` under `GetTempPath()` for each `RunAnalyze` (116 calls) and never removes it: 5,198 / 116 ≈ **45 runs** | [C] |

---

## 4. Why each design churns: the goal and the mechanism

**G1/G2: hermetic per-case repos and "prove it can fail" arms.**
- **Goal.** Each check must be shown both RED and GREEN against a controlled tree, with no state shared between arms, so legs can run in parallel and a pass cannot come from ambient state.
  - `check-unattended.test.sh:2-4`: "every RED arm paired with a GREEN control. Silence proves nothing."
  - `run-gates.sh:31-32`: "each heavy leg is already hermetic — it builds its own `mktemp -d` scratch repo."
  - `check-unattended.test.sh:8-10`: the kit is copied in "because the leg resolves its own install prefix."
- **Mechanism.** Hermeticity is bought with **construction**, not **isolation**. Each arm rebuilds its world from nothing: `git init` (28 entries), 4–6 `config` calls, a commit, a copy of the kit, sometimes a bare origin. The only shared-template helper, `tools/lib/lib-selftest.sh`, is used by 3 suites. Two others have local templates (`check-wiring.test.sh:40-52` `NEWREPO_SEED`; `manifest-check.test.sh:60-70`).
- **Adopters pay again.** G2 runs gov's own kit selftests inside every adopter bar, re-proving the kit on every incms and nicocares change, even though the kit bytes only change on upgrade.

**G1c/G1e/G1f: whole-tree snapshots.**
- **Goal.** Prove the kit works at a moved install prefix (foreign-prefix), or grade the uncommitted working tree as a commit (policy snapshot).
- **Mechanism.** Every one of these does a full checkout. `--no-hardlinks` copies objects too. None shares one snapshot with another, and none uses `--no-checkout` plus a sparse or partial checkout of the paths it actually reads.

**G3: history-grading legs.**
- **Goal.** Durable process claims, such as "each unit had a spec before the commit that built it" or "each routed commit names a specced unit".
- **Mechanism, part 1: no reuse.** The claim about a CLOSED unit in an old build is **immutable**: it depends only on fixed commit ids. Yet the leg's cache key includes HEAD (`run-gates.sh:3370`), so every commit regrades all of history.
- **Mechanism, part 2: one question per process.** The grading asks git a separate process for each question (`show`, `ls-tree`, `grep`, `rev-list` per unit and per build). About 55 ms under load × 17k is the leg's 16-minute wall.
- **The fix is already proven nearby.** The `_SUBJ` subject cache cut a sibling leg from 3,977–5,401 s to 591 s (`check-brief-recorded.sh:450-459`). It just isn't persisted across runs.

**G4/G5: govkit update and apply.**
- **Goal.** A safe upgrade: re-verify each receipt row against gov history, and refuse an install that turns a green leg red. The docstring at `govkit.py:6239-6246` says the bar runs without `GATE_FULL` on purpose, because that "doubles the target's whole bar".
- **Mechanism.**
  - `blob_at(..., batch=)` exists in `upgrade_steps.py:2628`, but govkit never passes a batch handle, so each row is 2–3 `git show` processes.
  - The `adopt-*.sh --check` pass runs before writing and again in the verify pass.
  - The baseline bar is recomputed even though the target tree is the same tree its last green bar graded. The target's `GATE_REUSE` cache could answer it.

**G6: fixed cost of each bar.**
- **Goal.** A self-grading, crash-safe runner with per-leg evidence.
- **Mechanism.**
  - Everything is a file: about 11 per leg in `$WORK`, `.leg` ledgers kept forever, and `gate-cache` as one file per entry (11,442), listed in full on each prune.
  - The regen pre-flight repeats checks that are already legs.
  - Guard diffs run serially, one process each.

**G7: nicocares `v3_seeded`.**
- **Goal.** Seed a real brand package into a real core and check profile, parity and render.
- **Mechanism.**
  - The fixture is function-scoped. It rebuilds the schema, RBAC and a full package install, and `copytree`s 66 files, for every one of 31 tests, even though about 26 of them only read.
  - Storage falls back to a repo-relative `./var/media`. Every upload writes original + `_thumb` + `_medium` under a new random name, so nothing is ever overwritten, and nothing ever sweeps it.
  - The suite runs in both incms and nicocares bars.

**G8–G12: incms.**
- The DB design is already good.
- **pytest-parallel:** the churn is `tmp_path` trees and leaks on kill.
- **gate.sh:** it is the one runner without a swept, owned `TMPDIR`.
- **web-build:** it calls Next directly, so the turbo cache never hits, and `standalone` copies about 3.7k traced files on every build.
- **e2e:** it seeds media twice into an unswept directory.
- **turbo:** its inputs are too broad to ever hit the cache.

**G13: hooks.**
- **Goal.** Guardrails and a liveness census on every tool call.
- **Mechanism.** Four separate interpreter launches per call instead of one dispatcher. The atlas regen materializes a whole worktree to regenerate one page.

**G15: generators.**
- **Goal.** Generated indexes stay in step with the tree.
- **Mechanism.** Keys include HEAD, so any commit re-renders everything. `gen_map` writes unconditionally, which also invalidates git's stat cache.

**G16: worktrees under the repo root.**
- **Goal.** Parallel sessions, each with its own checkout.
- **Mechanism.** Putting them inside the repo puts about 750k extra files under every tool that walks the repo without git's exclude list. Leaving finished ones around keeps the MFT large; it is now 5.3M records.

---

## 5. Reworks, with estimated reduction

Reductions are [E] per affected workflow, as share of file and process operations removed. The list is ordered by payoff per effort.

### Machine level: no repo change, one-time

| # | Change | Expected effect |
|---|---|---|
| H1 | **Disable 8.3 name creation on C:**: `fsutil 8dot3name set C: 1` (admin; affects new files only). Then optionally `fsutil 8dot3name strip /s /v C:\Users\d41ly\AppData\Local\Temp` and the `C:\projects` tree, after checking that no legacy installer needs short names there | Removes an extra name-index insert and a collision search on every create. In a 100k+ entry dir, 8.3 generation is the known O(n) cliff. With the 1M-entry TEMP gone the cliff is gone, but every create still pays the extra entry: about 10–30% of the cost of a create in large dirs |
| H2 | **Disable last-access updates**: `fsutil behavior set disablelastaccess 1` | Removes deferred MFT writes on reads and dir listings, which matters for the stat-heavy walks in G3, G6 and G14 |
| H3 | **Put churn on a dedicated volume.** Best: enable the Dev Drive policy (gpedit → Computer Configuration → Administrative Templates → System → Filesystem → "Enable dev drive") and create a ReFS Dev Drive VHDX (about 100 GB) on **D:**. Point `TEMP`/`TMP`, `.claude/worktrees` (via the app's worktree location, or a junction) and `TURBO_CACHE_DIR` at it. Alternative: a 4–6 GB RAM disk (for example AIM / ImDisk) for `TEMP` only; 32 GB RAM allows it | The Dev Drive keeps C:'s MFT, log and USN out of the hot path; ReFS has no 8.3 and no last access; it is easy to wipe and recreate. **It shares the physical RAID**, so it cuts metadata lock contention and the size of C:'s MFT, not physical I/O. A RAM disk removes physical I/O for temp entirely: **about 100% of G1/G2/G7/G8 temp I/O** |
| H4 | **Add `files.watcherExclude`** in VS Code user settings for `**/.claude/worktrees/**`, `**/var/media/**`, `**/.next/**`, `**/.turbo-cache/**` and `**/node_modules/**` | Removes watcher enumeration of about 960k files |
| H5 | **One-time sweep** of incms `services/api/var/media` (202k files), stale `.claude/worktrees` in gov (70) and incms (25) via the repos' own `/cleanup` skill, and `.git/recall/cache` entries for dead worktrees | Shrinks the working set that every walk and every directory lookup pays for |

### Gov kit (G1, G2, G3, G4, G5, G6, G13, G15)

| # | Rework | Keeps the goal because… | Reduction |
|---|---|---|---|
| K1 | **Session-scoped fixture templates.** Generalize `tools/lib/lib-selftest.sh` and `fixture_target.py` into one "template cache": build each distinct base repo (kit copied in, configured, committed) **once per suite run**, keyed by the kit tree hash, under the bar's `$WORK`. Each arm then gets `git clone --shared --no-checkout` + `checkout` of only the paths it touches, or `git worktree add --detach` of the template. Arms that only read share one read-only checkout. Arms that mutate get a `--shared` clone (objects are not copied) | Each arm still has its own index, refs and work tree, so RED/GREEN isolation holds. The template build itself is still exercised once | init+config+commit chains → 1 per suite. **60–85% fewer git processes and creates** in G1a, G1b, G1d and check-wiring |
| K2 | **Reset instead of rebuild** where arms are sequential: one repo per shard plus `git read-tree -u --reset <tree>` + `clean -fdx -q` in a single process, or `git stash`-free tree swaps. `unattended.test.sh` already does this; its trap and prologue-per-shard should share one prebuilt bundle (`git bundle create` once, `git clone` from the bundle per shard) | Same states are reached | Prologue ×8 → ×1 build + 8 clones |
| K3 | **One shared moved-prefix snapshot** for `foreign-prefix`, `chain-packet:295`, policy/loop snapshots, `govkit :5867`, `matrix.py:976` and `upgrade_walk`: build once per bar as `clone --shared --no-checkout` + sparse checkout of `tools/`, `skills/`, `.githooks/`, `memory/` only, and hand the path to each. No `--no-hardlinks`: use `--shared` with a read-only object store | The prefix move only needs the kit paths | 7–10 × 13.9k files → about 1–2 × about 3–5k. **About 90% of the snapshot I/O** |
| K4 | **Don't re-run gov's kit selftests in adopters (G2).** Replace them in incms/nicocares bars with a **content-addressed attestation**: gov's CI or gov's own green bar records "kit tree `<hash>` passed selftests on host-class X"; adopters check that the vendored kit tree hash matches an attested hash, and run the selftests only when the hash is unattested (a local edit to the vendored kit) | The selftest proves the kit's behaviour, which is a property of kit bytes plus platform, not of the adopter's product code | **About 100% of G2 on every non-upgrade bar** |
| K5 | **Immutable-verdict cache for history legs (G3).** Split each history leg into (a) a per-unit / per-commit verdict keyed by **the commit ids it reads** (build commit, spec blob id, RUN.md blob id), stored in `gate-cache` (or better, one sqlite / append-only TSV under the common git dir), and (b) a cheap pass over units whose key is new since the last run (`git rev-list <last-graded>..HEAD`). Drop `head $RG_HEAD` from the key for the cached part | A CLOSED unit's verdict is a pure function of those blob and commit ids; only new or changed units are regraded | pass-order 17k processes → **tens**; brief-recorded similar; manifest-check pickaxe scoped by path and by `LA..HEAD`. **More than 95% for G3 after the first run** |
| K6 | **Batch git in the remaining loops.** One `git cat-file --batch` / `--batch-check` coprocess per leg (already used in `routed_commits.py:454,465` and `lexicon.py:4241-4292`). Use `git log --format=… --name-only` once per build instead of `show --name-only` per commit; `git ls-tree -r` once and look up in memory; `git diff --name-only BASE` once for all guarded legs instead of one `git diff --quiet` per leg (`run-gates.sh:3249-3295`) | Same answers | 10–100× fewer processes in the loops named in the G3/G6 evidence |
| K7 | **govkit: pass `batch=` everywhere** (`blob_at` in `upgrade_steps.py:2628`), and **run each `adopt-*.sh --check` once**: keep the pre-write result keyed by (kit tree hash, target tree hash) and skip the verify-pass re-run when neither changed between them | Same rows, same checks | about 810 processes → 1 coprocess; `--check` pass ×2 → ×1. **About 40–60% of `update` wall** [E]; the 3.5 min likely becomes about 1.5–2 min |
| K8 | **`apply` baseline from the reuse cache.** Before writing, ask the target's `run-gates.sh` with `GATE_REUSE=lineage` (or `push`) for HEAD's recorded verdicts; run only legs with no reusable verdict. After writing, run only legs whose guards intersect the files `apply` wrote (`git diff --name-only`) | "Green before / red after" is still computed per leg; legs the install cannot affect keep their verdict | **Two whole bars → about 0.1–0.3 of a bar** |
| K9 | **Bar fixed cost (G6).** Drop regen pre-flight checks that duplicate legs; let the leg verdict stand. Store `gate-cache` as one sqlite file (or packed append-only TSV) instead of 11k one-line files; prune by age in SQL. Keep only the last N `.leg` run dirs per worktree, or pack each finished run's per-leg files into one `run.tar`/JSONL. Collapse the `$WORK/$i.{rc,out,sec,pid,…}` set to one record file per leg | The same evidence, in fewer files | About 1,000 per-bar files → about 100; 11k-entry list+stat → 1 open |
| K10 | **Hooks (G13).** One `node` dispatcher per hook event that runs scratch-guard, gate-guard and procmon-check in-process; the atlas regen uses `git archive <rev> -- <paths> \| tar -x` or `git show` of the few inputs it needs, not a full `worktree add` | Same guards | 4 spawns → 1 per tool call (about 120 ms saved per call [M]); about 13.9k file writes saved per atlas regen |
| K11 | **Generators (G15).** `gen_map._write` gains the compare-before-write that `gen_build_index.write_text` already has; render stamps keyed on the tree ids of the inputs (`git rev-parse HEAD:memory/builds` etc.) instead of HEAD; one walk shared by all extractors | Output identical | Unchanged files are no longer rewritten; re-render only when inputs change |
| K12 | **Teardown that survives kill.** Every suite and runner puts all scratch under **one owned root per run** (`$WORK/tmp` as `run-gates.sh` already does), with an owner pid file; the next run of **any** runner sweeps dead owners. Python: `tempfile.tempdir = <owned root>` in one shared helper, `rmtree(onexc=` a chmod-and-retry handler`)` in place of `ignore_errors=True` / `ignore_cleanup_errors=True` | Same fixtures | Leak rate on kill → about 0 after the next run |

### incms and nicocares (G7–G12)

| # | Rework | Reduction |
|---|---|---|
| P1 | **`v3_seeded` once per session.** Seed one template `v3.db` + package dir per session (or per xdist worker). Each test gets `sqlite3.Connection.backup()` into `:memory:`, or one `shutil.copyfile`; read-only tests share the template; the package dir is a session-level read-only copy; drop the unused `tmp_path` | 31 seeds → 1: **about 2.6k → about 100 creates per run (about 96%)**, and CPU time with it |
| P2 | **Set `STORAGE_LOCAL_PATH`** to a per-session tmp dir in nicocares `tests/conftest.py` and in incms `scripts/check-vendor-suite.sh`, `scripts/run-core-venv.sh` and the e2e `run.sh`, removed at session end | Stops 1,364 + about 1,800 permanent files per bar; lets the 202k-file `var/media` be deleted once |
| P3 | **Run the vendor seed suite in one bar, not two.** incms `vendor-suite` should reuse nicocares' recorded verdict for the same submodule sha (or vice versa) | 50% of G7 |
| P4 | **`gate.sh` gets the `run-gates.sh` WORK/owner/sweep block**: export `TMPDIR`/`TEMP`/`TMP=$WORK/tmp`, and pass pytest `--basetemp=$WORK/tmp/pytest` | Leaks on kill → swept next run |
| P5 | **`web-build` through turbo** (`turbo run build --filter=@incms/web`), with `NEXT_OUTPUT` unset in the gate so `standalone` is skipped (the image build keeps it); skip the leg when `git diff --name-only` shows no `apps/web`/`packages` change | About 9.2k ops per bar → 0 on a cache hit |
| P6 | **e2e:** one template DB and media dir seeded once, copied for the second pack; both packs on one `next dev` | About half of G11 |
| P7 | **turbo:** narrow each package's `test` inputs to its own sources plus what it really imports; prune `.turbo-cache` by age in `gate.sh` | Cache hits on most changes |
| P8 | **`tmp_path` → `tmp_path_factory` (session)** for read-only plugin fixtures in `services/api/tests` | A large share of the 5–15k `tmp_path` creates |

### Combined estimate for a typical incms bar

**[E] about 70–85% fewer file operations and about 80–90% fewer process spawns.**
- Biggest contributions: K4 (adopter selftests gone), K5 (history legs incremental), P1+P2 (seed fixture) and P5 (web-build cache hit).
- For a gov kit selftest run: **about 60–80%**, from K1+K3.

---

## 6. Prevention: rules, gates, budgets

### 6.1 Design rules for spec authors

Proposed text; these belong in the gov docs named in §6.4.

- **R1 Build once, isolate cheaply.** A fixture that more than one arm needs is built once per suite run, from the shared template helper, and handed to each arm as a `--shared` clone, a worktree, or a read-only path. A new `git init` in a test file needs a one-line waiver saying why the template cannot serve.
- **R2 Immutable facts are cached by the ids they read.** A verdict that depends only on commit or blob ids is stored under those ids and never recomputed. A leg may put HEAD in its cache key only for the part of its work that reads HEAD.
- **R3 One process per question set, not per question.** Loops over units, rows, files or commits use `git cat-file --batch`, one `git log` with a format, or `ls-tree -r` once. A git spawn inside a loop is a lint finding.
- **R4 No whole-tree copies.** Snapshots are `--no-checkout` + sparse (or `git archive` of named paths); `--no-hardlinks` and `copytree` of the kit need a waiver.
- **R5 Every scratch path lives under one owned, swept root.** Nothing writes to ambient `%TEMP%` or to a repo-relative output dir (`var/media`) from a test. Python `tempfile.tempdir` and bash `TMPDIR` are set by the runner; storage roots are set by the test session.
- **R6 Prove behaviour where the bytes change.** A kit's selftests run where the kit's bytes change (gov), and adopters check an attestation of the kit tree hash, not a re-run.
- **R7 A baseline is a cache read, not a run.** Any "before/after" comparison uses recorded verdicts for the unchanged tree and runs only what the change can affect.
- **R8 Generators compare before writing.**

### 6.2 Mechanical enforcement, so the prose doesn't rot

**G-A: temp-entry and residue budget per selftest row.** The rows live in `tools/run-gates/selftest-budgets.txt`, which today has seconds only.
- Add two columns: `max_temp_entries` (peak) and `residue` (must be 0).
- `run-selftests.sh` already gives each pooled row its own `SWEEP_ROOT/<row>/tmp` (`:1479`). Sample its entry count (the same watcher as §2) and count what remains after the row exits.
- Red on residue > 0, or on a peak above the ceiling.
- Shrink-only, exactly like the existing `tools/gate-lint/fork-count.sh` ceiling discipline.

**G-B: git-process budget per leg and per selftest row.** Run each leg under `GIT_TRACE2_EVENT=<dir>` in `measure_legs.py` (the profiler that already exists) and record `git_procs` beside seconds in `ceiling-evidence.txt`. A shrink-only ceiling reds on growth. This is the count-not-clock argument that `fork-count.sh:6-9` already makes for forks.

**G-C: static lint** (in `tools/gate-lint/sh_hygiene.py` and a python sibling). It flags:
- `git init` outside the template helper;
- `git (show|ls-tree|cat-file -p|log -1|rev-parse)` inside a `for`/`while` body;
- `shutil.rmtree(..., ignore_errors=True)` and `ignore_cleanup_errors=True`;
- `copytree` of a kit dir;
- `clone --no-hardlinks`;
- `mkdtemp()` / `mktemp -d` without a dir argument rooted in the runner's owned root.

Each finding needs a waiver line in a registry, the same pattern as `dead-path-waivers.txt`.

**G-D: per-run I/O budget the runner measures.** `run-gates.sh` reads `\PhysicalDisk` counters or the C: USN `Next Usn` (`fsutil usn queryjournal`, no admin needed, as in §2) at bar start and end, and writes `usn_bytes` and `git_procs` (from trace2) into the run record. A bar that exceeds the declared budget for its profile prints which legs dominated. Make it a warning first, then a red once a baseline exists.

**G-E: residue sweep on start of every runner** (`run-gates.sh` already does this; add it to incms `gate.sh` and `run-selftests.sh --serial`).

### 6.3 Concurrency rule

- **Add a host-level turnstile across all repos.** `run-gates.turnstile` exists per common git dir. Several sessions in different repos (gov, incms, nicocares worktrees) each run 8-wide, which on this one RAID is 16–32 concurrent metadata writers.
- **Proposal.** Put a **host-wide** token file under `%LOCALAPPDATA%` that all runners take, sized from `gate-profiles.txt`, with heavy and selftest legs counted against it.

### 6.4 Where the rules belong in gov (named only; not edited)

| Content | File |
|---|---|
| R1–R8 as the design rules for any new leg, selftest or fixture | `memory/guides/BUILD-METHOD.md` (how units are built) and `memory/TEMPLATE-SPEC.md` (a required "I/O shape" line in each spec: fixtures built, git processes per run, scratch root) |
| Merge-bar acceptance: "no new leg without a git-process and temp-entry ceiling row" | `memory/guides/MERGE-BAR.md` |
| Selftest authoring rules (template helper, owned root, residue 0) | `tools/lib/lib-selftest.sh` header, and a short section in `AGENTS.md` near line 236 where `GATE_SELFTESTS` is described |
| One gotcha per mechanism | `memory/gotchas/`: e.g. `history-leg-keyed-on-head-regrades-all-history.md`, `rmtree-ignore-errors-leaves-readonly-git-objects.md`, `per-arm-git-init-is-the-io-budget.md`, `repo-relative-storage-default-accumulates.md`. Today's nearby entries are `fixture-inherits-ambient-machine-state.md` and `fixture-removes-the-path-under-test.md` |
| Lint rules G-C | `tools/gate-lint/sh_hygiene.py`, `tools/gate-lint/README.md` |
| Budgets G-A / G-B | `tools/run-gates/selftest-budgets.txt`, `ceiling-evidence.txt` (via `derive-ceilings.py`), `measure_legs.py`, `tools/gate-lint/fork-count.sh` (as the model) |
| Adopter attestation (K4) | `WIRE-INTO-PROJECT.md` and `tools/govkit/registry.toml` / receipt schema |
| Host setup (H1–H4) | `WIRE-INTO-PROJECT.md` "host prerequisites", and `tools/run-gates/gate-profiles.txt` comments |
| incms/nicocares rules (P2, P4) | incms `CLAUDE.md` or `.claude/SESSION-KICKOFF.md` testing section; nicocares `tests/conftest.py` header |

---

## 7. Hardware: is this harmful to the NVMe?

**Short answer: mostly a latency and throughput-of-operations problem, not a wear problem.** Fullness matters more for performance than for endurance. The numbers:

- **Lifetime metadata volume.** The C: USN journal has advanced 146 GB since 2023-09-09: about **1.25M change records/day** on average. A record is about 100 bytes, and one file create + write + close + delete is roughly 4–6 records, so that is very roughly 200–300k file lifecycles per day on average.
- **Write amplification per metadata operation.** Each create or delete dirties a 1 KiB MFT record, a 4 KiB directory index page, bitmap bits and a `$LogFile` record. NTFS's lazy writer **coalesces** dirty metadata pages (about 1 s cadence), so a burst of 10k creates in one directory rewrites the same few hundred pages, not 10k × 4 KiB. A realistic host-write cost is about **2–8 KiB per file lifecycle**, plus the file's own data cluster (4 KiB minimum even for a 64-byte file).
- **Host writes from metadata churn.** At 1M lifecycles/day, which is the leak-era peak and above the average, that is **about 2–12 GB/day**, ×1.5–3 inside the SSD, so about **5–35 GB/day of NAND writes**.
  - Consumer 1 TB NVMe drives are typically rated at about 600 TBW each; a RAID 0 of two is about 1.2 PB.
  - **35 GB/day is about 13 TB/year, about 1% of rated endurance per year.**
  - This is not a wear threat. Builds, `node_modules` installs, browser caches and pagefile writes are likely larger.
- **SMART wear counters are hidden behind Intel RST:** `Get-StorageReliabilityCounter` returns `Wear 0` and no hours, and `smartctl` is not installed. To confirm actual wear, use the Intel RST / Optane Memory and Storage Management app or `smartctl -d csmi`. Record "Percentage Used" and "Data Units Written" for each member drive, and recheck in a month. **This is the one number not measured.**
- **Near-full drive.** At 88% used on C: and 89% on D:, with TRIM supported and passed through, the controller has less free space for garbage collection. Small random writes then see more internal write amplification and more latency spikes. This **adds latency more than wear**. Freeing 15–20% of the RAID (the 202k media files, the about 750k worktree files, the 1.7 GB recall cache and the 682 MB `.git/gov/index-s3.db` are candidates) helps steady-state latency.
- **What actually hurts is serialization.**
  - NTFS takes per-volume and per-directory locks for create, delete and rename. `$LogFile` commits are write-through.
  - With 8 legs × several sessions all creating and deleting in `%TEMP%` and `.git`, most of the time is spent waiting on those locks and on short write-through I/Os.
  - Task Manager shows 100% active time, meaning at least one I/O is always queued, while MB/s is tiny.
  - Interactive apps doing ordinary file opens wait in the same queue, which is the unresponsiveness the user felt.
- **The MFT is now 5.07 GB (about 5.3M records) and never shrinks.** It lengthens every MFT scan; backup, indexing, `chkdsk` and the 8.3 strip all pay for it. A reformat is the only way to shrink it. Not recommended; just stop growing it.

**Verdict.** The pattern is **not dangerous to the hardware** at these rates. It is **a responsiveness problem**, made worse by 8.3 names, last-access updates, the full drive and concurrency. Fix the design (K1–K5, P1–P2) and the host settings (H1–H3).

---

## 8. Residual leaks seen after the 3 landed leak fixes

`%TEMP%` was counted on 2026-11-20 at about 01:30.

- **2,486 entries.**
  - Top groups: 1,129 `incms-test-media*`, 1,194 `incms-test*`, 251 `ncv3-test*`, 324 `tmp.*` (files), 171 `tmp*` (python, 52-entry git repos holding `.governance` + `scripts`), 80 `companion-probe*`, 21 + 21 `incms-*-verdict*`, 34 `uv-*.lock`.
  - Almost all are from 11-18 or earlier, before the fixes.
- **New since 11-19 noon:**
  - 12 `tmp.*` files, in pairs: the incms `gate.sh` PG table (`PG_URL … TP_ARGV`) plus an empty partner, at 21:32, 22:10 and 22:53;
  - `lib-unattended.sh:865` `resolve_generated_indexes` (`_rg_lf`/`_rg_rf`, kit.toml listings) at 16:49 and 01:21;
  - 1 each of `incms-pack-verdict` / `incms-a11y-verdict`;
  - 1 `uv-*.lock`.
- These are small, but they show **G-E and R5 are not yet universal**: function-local `mktemp` files are removed on the normal path and leak on any early exit or kill.

## 9. Method notes and limits

- I ran no gate bar, no heavy suite, and nothing in any `gov-upgrade` worktree.
- The only executions were three gov selftests in a scratch `--shared` clone, micro-benchmarks in the scratchpad, and read-only counters.
- Gov counts in §3 combine my own greps and reads with two read-only code surveys. The key claims were spot-checked:
  - the `head $RG_HEAD` key at `run-gates.sh:3370`;
  - `read_gate_verdicts` at `govkit.py:7763` and `:8465`;
  - 202,037 files in `var/media`;
  - 447,230 files in gov `.claude/worktrees`;
  - `swy-` at `Test-Analyze.ps1:411`.
- Process-count estimates for the history legs use 55 ms per spawn under load. Idle measurements were 21–39 ms.
