# Brief — aTrimmedHook: a one-file commit's hooks cost seconds, not minutes

**Serves:** research TOOL-aTrimmedHook-1 TOOL-aTrimmedHook-2 TOOL-aTrimmedHook-3 KICK-aTrimmedHook-1

Handed to `/unattended` on 2026-10-11, node `a`, as `--prompt
C:/projects/coding-governance/.claude/worktrees/angry-engelbart-f0995c/HANDOFF-aTrimmedHook.md`. The
value carried no whitespace and named a readable file, so the FILE'S CONTENT is the prompt. It is
quoted below byte for byte (each line prefixed `> `), sha256
`5808ec6b25951c9f6d5f360fa9245104fb52a2844a2628d4c3bc7925ddc1d281`. The file was written by the
attended session that ran this build's kickoff and is itself the orientation; it holds the owner's
original prompt and the owner's three rulings verbatim. It cites prior records as background and
names no ask to build, so this is the prompt path and not the scaffold route. The run starts in the
session's own tree: the harness refuses writes into another worktree, and with the handoff file moved
aside the tree is clean and its branch carries nothing the default branch does not.

## The prompt

> # Handoff — aTrimmedHook: a one-file commit's hooks cost seconds, not minutes
>
> Handed from the attended session `4915eaea-c5b7-4db1-8f5e-490b4df290aa` (node `a`, 2026-10-11) to an
> unattended run. Start it with:
>
> ```
> /unattended --prompt C:/projects/coding-governance/.claude/worktrees/angry-engelbart-f0995c/HANDOFF-aTrimmedHook.md
> ```
>
> This file is the prompt. Take it whole, as the Skill's prompt path reads a prompt file. **Every fork
> is already decided by the owner**, quoted under "Owner decisions" below. The prompt path's one
> `AskUserQuestion` (step 2) has nothing left to ask, so skip it and quote these answers in the brief's
> `## Owner confirmation`.
>
> ## State at handoff
>
> - **Nothing is committed.** No build folder, spec or id exists under `aTrimmedHook`.
>   - The attended session minted the slug and grep-checked `memory/` clean, then committed nothing
>     under it.
>   - Re-run the collision grep: `git grep -nE '[A-Z]+-aTrimmedHook-[0-9]' -- memory` plus a scan of
>     `memory/LIVE.md`. If both come back clean, keep the slug for continuity with this file. Otherwise
>     mint your own slug.
> - **Base:** origin/main `b726385f2b5b8fd16802925c02104377253a9045`. Fetch first, because origin may
>   have moved.
> - **Work in a fresh worktree** off fast-forwarded origin/main. The handing-off worktree
>   `angry-engelbart-f0995c` holds this untracked file and nothing else; do not build in it.
> - **Manifest audit at handoff:** `manifest-check.sh` full run, rc=0, delta none, 0 watch commits since
>   the stamp.
> - **No concurrent edits seen:** `git log --all --since=3.days` shows no other branch touching
>   `check-memory-hygiene.sh`, `manifest-check.sh` or `.githooks/commit-msg`. Re-check this per the
>   manifest's §B kit bullet before the first pass.
> - **A baseline worktree exists** at `C:/projects/cgbase`, detached at `b726385f2`, kept clean for
>   timings. Reuse it for the "before" figures, and remove it at the close with `git worktree remove`.
>
> ## The prompt (the owner's words, verbatim)
>
> > Repo: C:/projects/coding-governance (gov), node a (Windows, Git-Bash; export PATH=/usr/bin:/mingw64/bin:$PATH). Work in a fresh worktree off origin/main per AGENTS.md §3, under your own session slug. This is kit work (memory-tree, session-kickoff, unattended kits). Its DoD owes kit version bumps, manifest stamps and each kit's self-test.
> >
> > ## Measured (2026-10-11, node a, a busy host with 18-28 bash processes from other sessions)
> > A one-file commit staging only memory/builds/<slug>/RUN.md costs about 165 s in hooks:
> > - `.githooks/pre-commit`, then `tools/memory-tree/check-memory-hygiene.sh --staged`: 123-129 s.
> >   - L1076-1078, check 9, runs `gen_build_index.py --check`: a full render of about 1315 artifacts, 31-33 s, on ANY commit touching memory/.
> >   - About 90 s is whole-tree setup and per-check passes over `$FILES`, the entire memory listing, even under --staged. Each costs 2-7 s: L751 (check 5 name scan), L455, L566, L501, L737, L1141-1144, L1350, L2243.
> >   - L2571-2573 builds TRACKED_SET from whole-repo `git ls-files` through a bash while-read loop for the legacy/debt stale-line guard, under --staged too.
> > - `skills/session-kickoff/manifest-check.sh --staged`: 27 s on that commit, 63-140 s on a 25-file one. It runs on EVERY commit. The C6 watch-liveness loop (around L1099-1100) spawns `git ls-files -- "$w" | wc | tr` per WATCH entry (17 git spawns). getval (L269) forks 3 processes per key.
> > - `.githooks/commit-msg`, then `tools/unattended/unattended.sh --check-commit`: 8-13 s. That's the 14k-line driver's top-level init: `--version` alone took 13 s, and `bash -n` parsing took 0.1 s. The check itself only matters when a non-terminal RUN.md names the current branch.
> > A 25-file commit measured hygiene 189 s, so about two-thirds of hygiene cost is fixed regardless of the staged set.
> >
> > ## Do (each one keeps the full check at the push boundary, where STAGED=0)
> > 1. Check 9 under --staged runs only when a staged path is a build-index INPUT or OUTPUT: a build README front matter, a spec status header, a BACKLOG.md, LIVE.md, ledger/ or backlog/. Otherwise it prints an announced skip, since a skip must announce itself (charter §7). Better still, `gen_build_index.py --check --builds <slugs>` renders only the touched builds plus the cross-build views.
> > 2. Under --staged, narrow `$FILES` early to the staged files plus their own build folders, so every per-check grep pass reads tens of lines instead of thousands. Leave the corpus joins HELD as they already are. Hold the legacy/debt stale-line guard under --staged unless its list file is staged.
> > 3. manifest-check --staged returns early, with an announced skip, when nothing staged touches the manifest or its watch list. Batch the C6 probe into one `git ls-files` call.
> > 4. The commit-msg hook skips the driver unless a tracked `memory/builds/*/RUN.md` names the current branch (a single `git ls-files | xargs grep -lF` takes about 0.7 s). Or make the driver's init lazy for the VERBS_INLINE verbs.
> > Target: a one-file commit's hooks under 30 s on node a. Report a before/after with the host's bash-process count beside each figure (see the memory note on polling loops and timings). Observe each new skip's failing case first: a staged build-index input must still trigger check 9.
>
> ## Owner decisions (asked at the attended READY hand-back, 2026-10-11)
>
> - **Check 9 skip: "Exact classifier (Recommended)".** The option text: skip only when every staged
>   memory path is a modification outside the structural set and its id set is unchanged between HEAD
>   and the index. It costs one python start and two git spawns.
> - **Item 2 depth: "Narrow + skip empties (Recommended)".** The option text:
>   - narrow FILES under --staged;
>   - skip the unread PRE_* preconditions;
>   - guard each costly pipeline so it runs only when its narrowed selection is non-empty;
>   - audit each guard for absence-type checks that would false-red on a narrowed set.
> - **Spec audit: "Don't declare".** Write no `spec-audit:` key. The `local` anchor refuses one on a
>   `slug`/`recipe` run in any case.
> - **Then: "write an oriented handoff to continue this build unattended"**, which is this file.
>
> ## What orientation found — two of the prompt's premises are REFUTED
>
> 1. **The check 9 trigger list in item 1 is incomplete.**
>    - `gen_build_index.py`'s `rosters()` (~L766) derives each build README's `ids:` line from id tokens
>      (`FAMILY-slug-N`) in the prose of EVERY tracked file under `memory/`. Only LIVE.md, ledger/ and,
>      under builds mode, backlog/ are excluded.
>    - So a staged RUN.md, gotcha or decision row that adds or drops an id moves a README, and a
>      path-list trigger would skip real drift.
>    - Hence the owner's pick: the exact classifier.
>    - The memory note "Citing a dangling id creates it as an orphan" is the same mechanism.
> 2. **Hygiene's per-check cost is process creation, not data volume.**
>    - Profiled at b726385f2 with `bash -x` and an `EPOCHREALTIME` PS4, interval attributed to the line
>      that ends it, on a one-file RUN.md stage at 64-82 host bash processes.
>    - The run totalled ~293 s. 53 source lines cost ≥2 s each (272 s together) and the remaining ~15600
>      traced lines cost ~0.
>    - Check 9 (L1079) was 51 s. The other 52 lines average ~4 s each, and each is one
>      `printf "$FILES" | grep | awk` pipeline or a single `$(…)`.
>    - Narrowing FILES alone therefore saves only per-element loops. Each pipeline must also be SKIPPED
>      when its narrowed selection is empty.
>    - The costly lines at b726385f2, with seconds:
>
>      | Line | Seconds | What |
>      |---|---|---|
>      | 1079 | 50.8 | check 9 render |
>      | 806 | 16.3 | `INDEX_SET=$(index_set)` |
>      | 1352 | 12.4 | check 10's archive loop |
>      | 518 | 7.0 | the check 2 staged intersect |
>      | 314 | 6.7 | `FAM_ALT` |
>      | 1104 | 6.1 | check 22 selection |
>      | 573 / 576 | 5.8 / 6.0 | check 3 `b3b` / `b3c` |
>      | 670 | 5.7 | `BUILD_N` |
>      | 1472 | 5.7 | `c12_all` |
>      | 2298 | 5.6 | `base12` |
>      | 436 | 5.4 | `DISC_ALT` |
>      | 750 | 5.3 | check 5's loop |
>      | 640 | 5.1 | check 3 `m1` |
>      | 463 / 466 / 472 | 4.7 / 4.7 / 4.1 | `PRE_*` (unread under --staged: `pop_guard` returns at L457 first) |
>      | 517 | 4.6 | `scan2` |
>      | 637 | 4.6 | check 3 project/ |
>      | 568 | 4.1 | check 3 root |
>      | 589 | 4.1 | check 3 `pop_guard` |
>      | 1143 | 4.1 | `c21_sel` |
>      | 2624 | 3.9 | `TRACKED_SET` |
>      | 2628 | 3.2 | `badD` |
>      | 2318-2409 | 1-3.7 each | `bad12_raw` post-processing |
>      | 271 / 265 / 278 / 339 / 340 / 434 / 502 | 2-3.7 each | irreducible setup |
>
>    - Raw trace, while it lasts: `/tmp/tmp.8EDvBtKmPP` on node a.
>
> **Consequence for the target.** The irreducible setup alone (HERE, conf reads, FAMILIES/DISCIPLINES,
> resolve_python, ls-files, the staged diff) is ~25-35 s at this host's load. A one-file commit under
> 30 s may be unreachable while 60-80 bash processes run. Report the figure you get with its bash
> count; never raise a timeout or a ceiling to reach it.
>
> ## Baseline (b726385f2, `C:/projects/cgbase`, one-line edit to `memory/builds/aBenchedProbe/RUN.md` staged, 2026-10-11 03:15+03:00)
>
> | Component | Seconds | Host bash processes, start..end |
> |---|---|---|
> | `check-memory-hygiene.sh --staged` | 307.5 | 75..78 |
> | `manifest-check.sh --staged` | 113.7 | 74..69 |
> | `unattended.sh --check-commit` (detached HEAD, so init cost only) | 49.7 | 71..78 |
> | `.githooks/pre-commit` total | 436.4 | 82..66 |
> | `.githooks/commit-msg` total | 49.7 | 67..77 |
>
> The host was ~3x slower than in the owner's 18-28-process measurement. The final comparison must
> therefore run BEFORE and AFTER back to back, under the same conditions, both trees on a named branch
> (not detached), so the commit-msg pre-filter's branch path is actually exercised.
>
> ## Units (one mechanism each; write a spec per unit before its code)
>
> | # | Unit | Kit | Tier | Mechanism |
> |---|---|---|---|---|
> | 1 | TOOL-<slug>-1 | memory-tree | 2 | `gen_build_index.py --check --staged` classifies the staged set; hygiene check 9 calls it under STAGED=1 |
> | 2 | TOOL-<slug>-2 | memory-tree | 2 | hygiene `--staged` narrows FILES, skips PRE_*, guards empty selections, holds the legacy/debt stale-line guard unless a list file is staged |
> | 3 | KICK-<slug>-1 | session-kickoff | 2 | `manifest-check.sh --staged` announces a skip when nothing staged touches the manifest, its watch or its verify-paths; C6 in one `git ls-files` |
> | 4 | TOOL-<slug>-3 | gov `.githooks` (no kit) | 1 | `commit-msg` runs the unattended driver only when a tracked RUN.md names the current branch |
>
> The tiers follow the manifest's tier rule. Units 1-3 are Tier 2 because they change the
> manifest-check gate semantics and the work spans kits. Unit 4 is Tier 1. Units 1 and 2 both write
> `check-memory-hygiene.sh`, so sequence them (1 then 2). Units 3 and 4 are disjoint from each other and
> from 1-2.
>
> ### Unit 1 — the check 9 classifier (design agreed)
>
> - **Where.** In `gen_build_index.py`, as a `--staged` modifier on `--check`. That keeps the predicate
>   next to `rosters()`, so the classifier and the renderer cannot disagree, which is the
>   "two answers to one question" class. Name the new function with a declared verb.
>   - The verbs: add arm build check cmd derive extract init load main measure parse print read remove
>     render resolve run scan seed set test write.
>   - Ask `python3 tools/lexicon/lexicon.py --suggest <name> --as py.function` before naming.
> - **Input.** `git diff --cached --name-status --no-renames -z` over the memory root, the conf and the
>   kit's own directory, plus ONE `git cat-file --batch` for each staged path's `HEAD:<p>` and `:<p>`
>   blobs. Two git spawns.
> - **Render (exit through the normal `--check`)** when any of these holds:
>   - a staged path is Added or Deleted;
>   - a staged path is a build `README.md`;
>   - a staged path is anything under a build's `spec|build|prompts|reviews/` (spec headers, record
>     bindings and record-filename dates are all read);
>   - a staged path is a build `BACKLOG.md`, `LIVE.md`, or under `ledger/`, `backlog/` or `project/`
>     (`stale-header-waiver.txt` lives there);
>   - `.memory-tree.conf` is staged;
>   - any file under the kit directory is staged;
>   - a modified non-structural file's roster id set differs between HEAD and the index. Compute it
>     with the SAME `id_re` and `scan_missing_citations` that `rosters()` uses: factor them out and
>     call one helper from both, so they are never retyped.
> - **Otherwise skip** with one announced line saying why (no staged path can move the index), that the
>   push boundary renders in full, and that a HEAD already drifted by a `--no-verify` commit is not seen
>   here.
> - **Hygiene side.** At L1078-1079, under STAGED=1, call `--check --staged`. Print the skip line through
>   and keep exit-code handling identical. STAGED=0 is byte-unchanged.
> - **Known, pre-existing, NOT this unit:**
>   - the renderer reads the WORKTREE, not the index;
>   - `LIVE_LANDED_UNCLOSED` reads product source that pre-commit never stages for hygiene;
>   - pre-commit invokes hygiene only when `memory/**` is staged, so a staged conf or kit file alone
>     never reaches check 9.
>
>   State all three in the spec's non-goals.
> - **Failing case first (owner's words).** A staged build-index input must still trigger check 9.
>   - Observe at least: a staged README front-matter edit renders, and a staged RUN.md line adding a
>     new FAMILY-slug-N id renders.
>   - A staged RUN.md edit with no id change skips. Its line is printed and the timing drops by the
>     render's cost.
>   - Arm these in `gen_build_index.py --selftest` (the "build-index selftest" leg), and stage the break
>     to see RED before trusting GREEN.
>
> ### Unit 2 — narrowing (design agreed, audit owed)
>
> - **FILES under STAGED=1** becomes the staged memory paths plus every tracked file in those paths' own
>   `builds/<slug>/` folders. Derive it from one `git ls-files` already in hand, never a second spawn
>   per build.
> - **Skip PRE_\* computation under STAGED=1.** `pop_guard` returns before reading them. Set them to 0
>   and say in a comment why that is safe.
> - **For each costly line above**, decide one of three, and write the decision into the spec per line:
>   - (a) safe on the narrowed set as is;
>   - (b) skip when its selection is empty, using a bash test on a variable and never a fork;
>   - (c) HOLD under --staged with an announced line, like the existing corpus joins.
> - **Audit for absence-type predicates**, which false-red on a narrowed set:
>   - check 3 compares directory entries against an allowed set. Confirm it asserts only unknown
>     entries, never required presence.
>   - check 10 resolves a rotated archive's live index from the whole file set. Narrowed, it would
>     mis-resolve, so it is likely (c) unless an archive or index file is staged.
>   - check 12's joins already hold under --staged (L2290 comment).
> - **Legacy/debt stale-line guard (~L2619-2630).** Under STAGED=1, run it only when
>   `memory/project/legacy-files.txt` or `curation-debt.txt` is staged; otherwise one announced HELD
>   line. `TRACKED_SET` is read nowhere else under STAGED=1; its other reader (~L2652) is STAGED=0 only.
> - **Failing cases.**
>   - A staged file with a check-5 name violation, a broken link (check 2) and an index-file cap breach
>     (check 6) each still red under --staged after narrowing.
>   - A staged edit to a legacy-listed path's list file still runs the guard.
>   - Observe each RED before trusting GREEN. Arms belong in the memory-hygiene self-test; slice it,
>     per the memory note "Slice a suite to debug one arm".
>
> ### Unit 3 — manifest-check (profile first)
>
> - **Profile `--staged` before designing.** The owner's 27-140 s may be dominated by the script's
>   top-level setup (1100+ lines of function definitions and the card machinery parse before any
>   check), not by C6. The `profile.sh` below takes any script.
> - **The early exit** sits right after the audit block parses (WATCH and VPATHS are needed). When
>   `git diff --cached --name-only -- "$MF" "${WATCH[@]}" "${VPATHS[@]}"` is empty, print one NOTE line
>   naming the three inputs and that the full leg runs at the push boundary, then exit 0.
>   - VERIFY-PATHS are added to the owner's "manifest or its watch list": a staged deletion of a
>     verify-path would otherwise escape C4.
>   - C1, C7, C8 and C12 read only the manifest file, so they cannot change unless the manifest is
>     staged. Moving them below the exit is safe; say so in the spec.
> - **C6 in one spawn.** Every WATCH entry in this repo is a literal path; a pathspec with glob magic
>   falls back to its own call.
> - **Watched-file trap.** `manifest-check.sh` is itself in `watch:`, so every commit touching it owes
>   a `last-audit` re-stamp in the SAME commit (C5s). See the stamps note under traps.
> - **Failing cases.** A staged watched file with no re-stamp still reds C5s, and a staged manifest edit
>   still runs C1/C7/C8. Arm them in `skills/session-kickoff/manifest-check.test.sh`.
>
> ### Unit 4 — commit-msg pre-filter (Tier 1)
>
> - **Before the driver call** in `.githooks/commit-msg`:
>   ```
>   ref=$(git symbolic-ref -q HEAD) || skip
>   git ls-files -- ':(glob)**/builds/*/RUN.md' | xargs -r grep -lF -- ": $ref"
>   ```
>   Empty means skip the driver.
> - This is the driver's own first narrowing (`check_commit_message`, ~L12829-12831), with a superset
>   glob so the error direction is "run the driver". Its silence is the driver's own silent no-run
>   answer; comment that in the hook header.
> - Keep the "conf present, kit absent" note untouched.
> - **Failing case.** On a branch that a non-terminal RUN.md names (`run-branch: refs/heads/<b>`), the
>   driver still runs and still refuses an undeclared staged path. On a branch nothing names, it does
>   not run (timing).
> - `tools/check-wiring.sh` grades the hook's wiring and mode (100755). Keep the mode.
>
> ## Definition of Done (owner: "kit version bumps, manifest stamps and each kit's self-test")
>
> - **Kit versions, ONCE each after the last move** (memory note "Bump kit versions once, after the last
>   move"):
>   - memory-tree `2.139` → next: `KIT_MEMORY_TREE_VERSION` in `check-memory-hygiene.sh` plus every
>     `gov:kit memory-tree@2.139` carrier (`grep -rln 'memory-tree@2.139' -- tools`);
>   - kickoff-manifest `1.24` → next: `KIT_MANIFEST_VERSION` in `manifest-check.sh` and its carriers.
>     Leave `MANIFEST_FORMAT` alone: the format does not move.
>   - Then `python tools/govkit/govkit.py epoch --base <BASE>` and `govkit selfcheck`.
> - **Manifest stamps:**
>   - `last-audit` re-stamped in each commit touching a watched file;
>   - `last-body-change` only if the manifest body changes. Body edits are probably not needed, but if
>     the hygiene or manifest-check staged behavior is front-loaded anywhere in §B, update it.
> - **Self-tests (the owner asked for them in this build's DoD, overriding the standing "on demand
>   only"):** memory-hygiene self-test, build-index selftest (`gen_build_index.py --selftest`),
>   check-arms selftest, and `manifest-check.test.sh`.
>   - Run them targeted and serially, OUTSIDE the final bar, on a frozen `git clone --local` under a
>     short `%TEMP%` root.
>   - `gate-guard` denies `*.test.sh` before VERIFYING.
> - **Final bar:** `GATE_FULL=1` only, never `GATE_SELFTESTS=1`.
> - **Codebase map:** a new shell function or Python def stales `symbols.json` (`gen_map.py --write`,
>   then stage), and a new key needs a dossier claim.
> - **Before/after table** in the run record and the wrap-up, both measured back to back on named
>   branches, with bash counts start..end beside every figure.
>
> ## Traps this build will hit (from node a's memory notes; read the notes themselves for detail)
>
> - A new build folder owes four things: `ids:`, the `gen:build-index` pair, a
>   `memory/project/readme-contract.txt` row plus the `roster:units` pair, and five canonical slots
>   within their byte caps. `## Parked decisions` counts among them.
> - A record filename must be family-qualified (`<date>-prompt-TOOL-<slug>-1-brief.md`).
> - A record's `Serves:` may name only ids a committed spec H1 defines (check 21). Commit the specs with
>   or before the brief.
> - Spec §6 cannot cite a file the unit creates (`check-spec-tokens.py`; the waiver file is shrink-only).
>   Run `check-spec-tokens.py --list` before dating a spec.
> - `gen_build_index --write` sees only TRACKED files, so `git add` the README first. The hygiene gate
>   likewise grades only tracked or staged files.
> - Hook timings lie under contention. Never poll in a foreground loop. Before trusting a figure, check
>   that no leftover hygiene or pre-commit process from an earlier attempt is still running, and report
>   the bash count.
> - Heredocs mangle backslashes, and the Python text mode eats bare CR in shell files. Author with
>   Write/Edit, or patch in binary mode.
> - CRLF working copies defeat a multi-line `str.replace`, and a count-based report still claims
>   success.
> - `install-prefix` waivers are line-keyed: inserting lines above a waived literal in a hook or kit
>   file reds that leg. Re-key the waiver; never re-waive.
> - A kit file names nothing outside itself by literal (charter §12). Derive paths in hooks the way
>   `commit-msg` already does.
> - `--check-format` is a second gate beside `--check`; run both.
> - The lexicon leg grades nested helpers too, and branch bars skip it as unchanged-vs-main, so it reds
>   only at the lander. Run `python3 tools/lexicon/lexicon.py --check` yourself.
> - `check-arms` wants the whole refusal text in an arm, not a prefix.
> - The bar green is recorded per git-dir. Never wrap the lander in `timeout`: launch it detached and
>   watch the pid.
> - Briefs must commit the spec before the code (pass-order). A pass commit must carry RUN.md.
>   Declare generated writes at `--dispatch`.
>
> ## Instruments (author with Write; heredocs mangle the escapes)
>
> `measure.sh <label> <tree>` stages a one-line RUN.md edit, times each hook component with the bash
> count, then restores the file:
>
> ```bash
> #!/usr/bin/env bash
> export PATH=/usr/bin:/mingw64/bin:$PATH
> cd "${2:?tree}" || exit 1
> label=${1:-run}
> f=memory/builds/aBenchedProbe/RUN.md
> cp "$f" "$f.bak"; printf '\n<!-- measure probe -->\n' >> "$f"; git add "$f"
> bc() { ps -W | grep -cE '/usr/bin/bash'; }
> t() { local s e b0 b1; b0=$(bc); s=$(date +%s.%N); "$@" >/dev/null 2>&1; rc=$?; e=$(date +%s.%N); b1=$(bc)
>       printf '%-28s %7.1fs rc=%s bash=%s..%s\n' "$name" "$(awk -v a=$s -v b=$e 'BEGIN{print b-a}')" "$rc" "$b0" "$b1"; }
> msg=$(mktemp); printf 'probe\n' > "$msg"
> echo "== $label $(date -Is) HEAD $(git rev-parse --short HEAD) branch $(git branch --show-current)"
> name=hygiene-staged;   t bash tools/memory-tree/check-memory-hygiene.sh --staged
> name=manifest-staged;  t bash skills/session-kickoff/manifest-check.sh --staged
> name=unattended-check; t bash tools/unattended/unattended.sh --check-commit "$msg"
> name=pre-commit-total; t bash .githooks/pre-commit
> name=commit-msg-total; t bash .githooks/commit-msg "$msg"
> git reset -q -- "$f"; mv "$f.bak" "$f"; git status --short
> ```
>
> `profile.sh <tree> <script> [args]` stages the same edit, then attributes wall time to the line that
> ENDS each interval. A `$(…)` traces its inner commands before its own line, so end-attribution is the
> correct one:
>
> ```bash
> #!/usr/bin/env bash
> export PATH=/usr/bin:/mingw64/bin:$PATH
> tree=$1; shift; script=$1; shift; cd "$tree" || exit 1
> f=memory/builds/aBenchedProbe/RUN.md
> cp "$f" "$f.bak"; printf '\n<!-- measure probe -->\n' >> "$f"; git add "$f"
> out=$(mktemp)
> PS4='+${EPOCHREALTIME} ${LINENO} ' bash -x "$script" "$@" >/dev/null 2>"$out"
> git reset -q -- "$f"; mv "$f.bak" "$f"
> awk 'FNR==NR { if ($0 ~ /^\+[0-9]+\.[0-9]+ [0-9]+ /) { t=substr($1,2)+0; l=$2; if (pt) d[l]+=t-pt; pt=t }; next }
>      (FNR in d) && d[FNR]>=1 { printf "%5d %5.1f  %s\n", FNR, d[FNR], substr($0,1,105) }' "$out" "$script"
> echo "trace: $out"
> ```
>
> Run both with `run_in_background: true` and wait for the notification. They take 5-8 minutes each at
> this load.
>
> ## Prior records
>
> - `TOOL-aGroundedOrientation-3` and `TOOL-aThawedCorpus-5` (its N2) named check 9's near-vacuous
>   staged disjunct and deferred it.
> - The `KICK-cKeyedLaunchpad-1` review explains why C9 stays out of the staged leg: the hook fires on
>   every commit.
> - Recall terms used: staged pre-commit hygiene check 9 gen_build_index fork spawn cost manifest-check
>   C6 commit-msg check-commit.
> - Bug classes for the touched paths, from `gotchas.py --for-paths`:
>   - staged-break-substitutes-a-synthetic-value
>   - vacuous-selector-empty-population
>   - swallowed-delegate-reads-as-clean
>   - shipped-checker-edit-is-an-adopter-contract-change
>   - two-answers-to-one-question
>   - inherited-git-dir-pins-the-work-tree-to-the-cwd
>   - pin-gated-checks-arm-nothing-without-a-pin
>   - a-grep-for-a-word-is-a-presence-probe

## The brief

### Goal

Cut the fixed cost of the pre-commit and commit-msg hooks on a small commit on node a, so a one-file
`RUN.md` commit costs seconds rather than minutes, while every check still runs whole at the push
boundary (`STAGED=0`) and every new skip announces itself.

### Items

1. Hygiene check 9 under `--staged` renders the build index only when a staged path can move it, decided by the exact classifier the owner chose (structural paths, adds and deletes, the conf and the kit dir always render; a modified file renders when its roster id set differs between HEAD and the index); otherwise an announced skip. [planned TOOL-aTrimmedHook-1]
2. Hygiene `--staged` narrows FILES to the staged files plus their own build folders, skips the PRE_* preconditions it never reads and every costly pipeline whose narrowed selection is empty, and holds the legacy/debt stale-line guard unless one of its list files is staged. [planned TOOL-aTrimmedHook-2]
3. `manifest-check.sh --staged` returns at once, announced, when nothing staged touches the manifest, its watch list or its verify-paths, and C6 probes the watch list in one `git ls-files`. [planned KICK-aTrimmedHook-1]
4. `.githooks/commit-msg` starts the unattended driver only when a tracked `RUN.md` names the current branch, the driver's own first narrowing run in the hook. [planned TOOL-aTrimmedHook-3]
5. The prompt's "better still" partial render, `gen_build_index.py --check --builds <slugs>`. [parked item 1's classifier already skips the render for the commit the owner measured; a partial render is a second mechanism in the renderer's cross-build views and is left to a follow-up build]

### Acceptance

Each skip's failing case is observed before its skip is trusted: a staged build-index input and a
staged `RUN.md` line adding a new id still run check 9; a staged check-5, check-2 or check-6 violation
still reds after narrowing; a staged watched file with no re-stamp still reds C5s; a branch named by a
non-terminal `RUN.md` still runs the driver. A before/after table of a one-file `RUN.md` commit's hook
components, measured back to back on named branches, with the host's bash-process count beside every
figure; the under-30 s target is reported as reached or not, never chased with a raised ceiling.

### Gates

`memory hygiene` · `build-index selftest` · `build README slot contract` · `memory-hygiene self-test` ·
`check-arms selftest` · `harness arms (fail branches armed or pinned)` · `kickoff-manifest ratchet` ·
`manifest-check self-test` · `branch-guard self-test` · `check-wiring self-test` ·
`codebase-map coverage + freshness` · `lexicon naming predicates` · `kit version markers`, and the
closing `GATE_FULL=1` bar.

### Non-goals

No change to any full (`STAGED=0`) run. No partial `--builds` render (item 5). No lazy init of
`tools/unattended/unattended.sh`. No change to `.githooks/pre-push`, `tools/run-gates/`, the push
boundary, or any check's verdict on the full tree. The three pre-existing gaps stay as they are and are
named in unit 1's non-goals: the renderer reads the worktree, `LIVE_LANDED_UNCLOSED` reads product
source, and pre-commit reaches hygiene only when `memory/**` is staged.

### Limitations

Node a is a contended host (60-80 bash processes at orientation); never kill a process this run did
not start, and never poll in a foreground loop. A pass runs no bar and no suite; the touched kits'
self-tests run targeted and serially outside the final bar, on a frozen clone, after VERIFYING, and
the final bar is `GATE_FULL=1` alone. One version bump per touched kit after the last move. Every
commit touching a watched file re-stamps the manifest's `last-audit` in the same commit. A shipped
checker's edit is an adopter contract change: hooks and kit files name nothing outside themselves by
literal.

### Reuse

`reuse_lookup.py` returned only name-stem matches for all four mechanisms (build, changed, check,
run). The seams this build extends are the renderer's own `rosters()` and `scan_missing_citations`
in `tools/memory-tree/gen_build_index.py` (unit 1 factors the id scan out and calls it from both
sides) and `check_commit_message`'s first narrowing in `tools/unattended/unattended.sh` (unit 4
replays it in the hook). Recall returned TOOL-aGroundedOrientation-3 and TOOL-aThawedCorpus-5, which
named check 9's near-vacuous staged disjunct and deferred it, and the KICK-cKeyedLaunchpad-1 review
on why C9 stays out of the staged leg. Recall terms used: staged pre-commit hygiene check 9
gen_build_index fork spawn cost manifest-check C6 commit-msg check-commit.

## Drawn from the session

none

## Owner confirmation

not asked — the brief draws on nothing outside the prompt
