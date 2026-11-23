# KICK-dKeptSession-80 — the run branch reconciled with origin/main at 525f3ab97 in one merge commit, each conflict resolved by its kind

**Status:** INPROGRESS · rev-1 · 2026-11-23 · node d · Tier-2 · base 0a39514a · streams tooling · order 38 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-23-build-KICK-dKeptSession-80-close-bar-attribution.md](../build/2026-11-23-build-KICK-dKeptSession-80-close-bar-attribution.md) | research | — |
| [2026-11-23-build-KICK-dKeptSession-80-widen-4.md](../build/2026-11-23-build-KICK-dKeptSession-80-widen-4.md) | widen | — |
| [2026-11-21-prompt-KICK-dKeptSession-80-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-80-build-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-80-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-80-1-spec-writer.md) | journal | — |
| [2026-11-23-prompt-KICK-dKeptSession-80-spec-brief.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-80-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`origin/main` stands at `525f3ab97`, past `8b8b1374`, the tip KICK-dKeptSession-69 reconciled with, and the
lander's `--prepare` refuses a run branch that does not merge onto it cleanly. This unit is the second
reconcile: one merge commit of `origin/main` whose conflicts are each resolved by their kind, by
KICK-dKeptSession-69's procedure re-keyed to `525f3ab97`, so `--prepare` can run again.

## 2. Scope (IN)

- **S1** — The reconcile commit, KICK-dKeptSession-69 S1 re-keyed. The main loop runs `git merge --no-ff
  --no-commit origin/main` in the run worktree. The builder resolves the conflicts by S2, S3, S5 and S6,
  makes S4 in that worktree, and commits nothing. The main loop then commits the merge with this unit's
  acceptance ledger and the trailer `Pass: KICK-dKeptSession-80`, through `git commit` with the hooks
  running. A refused commit goes back to the builder; the merge is never committed with a hook skipped.
  Observed by AC1, AC2.
- **S2** — The five generated outputs are re-rendered, never hand-merged, KICK-dKeptSession-69 S2's rule:
  `.governance/policy.json`, `help/reference/policy.md`, `memory/map/generated/MAP.md`,
  `memory/map/generated/symbols.json` and `tools/gate-legs.json`. Each is first checked out from main's
  side, `git checkout --theirs -- <file>`, to clear its markers, then rewritten by S4. Observed by AC3.
- **S3** — The product and configuration hunks, each resolved by keeping both sides' content, rows
  unioned and code joined, by the per-file rule of §4 "The five files". Observed by AC4, AC5, AC6, AC7,
  AC8.
- **S4** — The regeneration and the stamp, KICK-dKeptSession-69 S4 re-keyed. With every conflict resolved
  and staged, the builder regenerates over a provisional commit of the merge, as `run_pass_tree_regen`
  does (`tools/unattended/pass-tree.sh#run_pass_tree_regen`): `git write-tree`, `git commit-tree <tree>
  -p HEAD -p MERGE_HEAD -m provisional`, `git update-ref --no-deref HEAD <it>`, then the three renders of
  §4 "The provisional window" in its order, then `git symbolic-ref HEAD
  refs/heads/branch/unattended-dkeptsession-a0567a` whatever their exits. The kickoff manifest's block
  in `memory/guides/SESSION-KICKOFF.md` is resolved by §4 "The manifest stamp": one `last-audit:` line
  written over the merge, and the run's `last-body-change:` kept. Observed by AC3, AC10.
- **S5** — The chain packets, one per dClosedLoop build, by §4 "The chain packets": each checked out
  from the run's side whole, then re-rendered in S4's window by `python tools/chain-packet.py --write
  <slug>`. Observed by AC9.
- **S6** — The manifest's body keeps both sides' dated corrections, as the trial merge wrote them; only
  its audit block conflicts, and S4 resolves it. Observed by AC10.

## 3. Non-goals (OUT)

- The full bar's own reds on the merged tree. The brief records the close's full bar at `0a39514a6` RED
  against the run's pre-merge tree (UNVERIFIED here: no record in this tree holds that reading). Most of
  those legs grade registries and code main changed, so they can only be read on the merged tree. The
  main loop re-runs the bar after this commit, attributes each red against `origin/main`, and clears the
  run's own reds through the red-fix lane, one record each. This unit fixes none of them.
- The plain manifest check's check 5 at the merge commit. It reds there by construction (§4 "The
  manifest stamp"), and the close's re-stamp clears it, as `4d56510fe` did after KICK-dKeptSession-69.
- Any auto-merged file beyond what a resolution here needs. Each arrives as the merge writes it.
- Committing, rendering an index by hand, or starting the merge in this pass. Those are the main loop's.
- `memory/DECISIONS.md`, a shared record a pass may not declare.

### Edges

- **consumes-from** external — `origin/main` at `525f3ab97` and the primary tree's hooks, which grade the reconcile commit; this unit edits neither the hooks nor main's history
- **consumes-from** external — the main loop's commit of this spec, with the dKeptSession packet re-rendered over it and its spec-count fact widened, as `af51227c1` did for KICK-dKeptSession-79; without it the merge's packet render moves that fact and the facts ledger reds
- **hands-off** external — the full bar's reds on the merged tree and the manifest's post-merge re-stamp, each cleared by the main loop's red-fix lane with one record

## 4. Design

### Evidence

- `git merge-tree --write-tree --name-only HEAD origin/main` at `0a39514a6`, read-only, conflicts in
  the brief's 33 files, PINNED 2026-11-23 at trial tree 162162b7, and its merge base is `8b8b1374`.
  `origin/main` is 193 commits past `8b8b1374`, DERIVED by `git rev-list --count 8b8b1374..origin/main`.
- Hunk counts over that tree by `grep -c '^<<<<<<<'`, PINNED 2026-11-23: `.memory-tree.conf` 2,
  `tools/govkit/registry.toml` 3, `tools/lib/resolve-python.test.sh` 2, `tools/policy/catalogue.toml` 1,
  `tools/policy/check_policy.py` 1, `memory/guides/SESSION-KICKOFF.md` 1, each packet 1.
- `regen.py --list` names a write for `tools/gate-legs.json` (`leg_factory.py --write`, stage 1),
  `.governance/policy.json` (`policy.py mirror --write`, stage 2) and `memory/map/generated` (`gen_map.py
  --write`, stage 3). It names none for `help/reference/policy.md`, which
  `tools/playbook/render_playbook.py#render_reference_pages` writes under `--reference` from the
  working-tree catalogue, as `tools/playbook/references.toml` declares it.
- `cmd_mirror` renders a committed revision, and the lander and `pass-tree.sh` regenerate over a
  provisional commit for that reason (KICK-dKeptSession-67 §4, KICK-dKeptSession-69 S4).
- The packet instrument re-renders an existing packet keeping its instrument pins, its repin records and
  its `rendered at` where the render with that value equals the file, else it renders at `git rev-parse
  HEAD` (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py#render_packet`).
  Its `--check` byte-compares the packet with that render at the packet's own `rendered at`, so the
  value is text and is never resolved (`#cmd_check`, `#render_text` there). Parent states are read
  from HEAD by `schedule.py#tree_state("HEAD", …)` inside `#derive_sources`, so a render reads the tree
  HEAD names.
- Every packet's `- instrument:` pins are identical on both sides, and the run's carries two `-
  repinned inside a live chain run:` records where main's carries one, PINNED 2026-11-23 over all 22 by
  `grep` on each side. The run's extra record is the owner's console repin of the schedule instrument
  (`91d470117`), which only `--repin` writes and which refuses an agent inside a chain run
  (`#cmd_repin` there). Main's re-render `8d55c36e2` pinned the same blob, `6184e571`, with no record.
- Outside the repin record and `rendered at`, 21 packets are byte-identical across the two sides; the
  dKeptSession packet differs also in its coverage lines, where the run's side counts its later specs.
  The run's packets read fresh at `0a39514a6`: `chain-packet.py --check dKeptSession` printed `byte compare
  green`, PINNED 2026-11-23.
- The packet join grades only a build whose `RUN.md`'s last `phase:` is outside `LANDED`, `ABORTED` and
  `LANDING` (`tools/check-spec-tokens.py#scan_live_packets`). On the trial tree that is dKeptSession
  alone, at VERIFYING, PINNED 2026-11-23.
- The manifest's two sides differ in its block's `last-audit:` and `last-body-change:` lines only, and
  the trial carries both sides' body corrections. Check 9 reds at ten or more non-merge watched
  commits between `last-body-change` and HEAD (`skills/session-kickoff/manifest-check.sh@663b4f5a61:3393`).
  Counted as `git rev-list --count --no-merges HEAD 525f3ab97 ^<sha> -- <watch>`, the run's
  `95a4a1188` reads 9 and main's `8dbcc3586` reads 17, PINNED 2026-11-23.
- Check 5 takes the newest watch-touching commit since `last-audit` (`manifest-check.sh@663b4f5a61:3272`)
  and its stamp candidates from `git log -G'^last-audit:'` (`@663b4f5a61:3280`), which lists no merge
  commit (TOOL-dFoldedAudit-17 S10). A merge that moves watched files against both parents is that
  newest commit, and its own stamp is never a candidate. The staged leg compares the staged stamp with
  HEAD's alone (`@663b4f5a61:3405`). KICK-dKeptSession-69's merge passed the staged leg and its plain
  check 5 then red, cleared by `4d56510fe` (`2026-11-22-build-KICK-dKeptSession-69-red-fix-10`).
- The policy guard judges the staged `.governance/policy.json`. Its mirror shape refuses a render whose
  catalogue input is staged changed (`tools/policy/guard.py#check_mirror_render`), and a refused change
  is admitted on a live run's branch (`tools/policy/guard.py#check_run_mandate`), which this branch is
  while `RUN.md` reads VERIFYING.
- The merge driver `tools/memory-tree/merge-rows.py` resolved every registry row in the trial, its two
  report lines reading `0 row conflicts, 0 structure conflicts`, PINNED 2026-11-23.

### The five files

| File | Resolution |
|---|---|
| `.memory-tree.conf` | Hunk 1: main's `TWENTY-SECOND MEMBER, TOOL-dQuietDisk-9 S6` note first, as landed; the run's note after it, its head renumbered `TWENTY-THIRD AND TWENTY-FOURTH MEMBERS, KICK-dKeptSession-69 §8 F2`. Hunk 2: `PROJECT_REGISTRY_EXTRA` is main's word list with the run's `unnamed-keys.txt` and `unpurposed-namespaces.txt` appended, the only words either side holds alone. |
| `tools/govkit/registry.toml` | Each of the three guards, `recall floor`, `recall floor arms` and `memory-recall kit selftest`: main's two lines in main's order, then the run's `presets.py` and `design_lib.py` lines from KICK-dKeptSession-69 S9. |
| `tools/lib/resolve-python.test.sh` | Hunk 1: the run's two rows, then main's seven, so each side's rows keep their order. Hunk 2: the run's comment paragraph, then main's. |
| `tools/policy/catalogue.toml` | Main's three `[[key]]` rows first, so the keys stay contiguous, then the run's fourteen `[[namespace]]` rows, which close the file as at the run head. |
| `tools/policy/check_policy.py` | The run's `import presets` line directly after `import budgets`, beside the other two module imports, then main's `import atexit`, `import pathlib` and its three inline blocks byte for byte, since each is a gated copy of `owned_scratch.py`. |

### The provisional window

In S4's window, with HEAD on the provisional commit, the builder runs, in this order:

1. `python tools/playbook/render_playbook.py --reference`, which rewrites `help/reference/policy.md`
   from the merged catalogue.
2. `python tools/run-gates/regen.py --write`, which rewrites the other four generated outputs and the
   indexes. Stage 2 renders the build README the packets read, so this runs before 3.
3. `python tools/chain-packet.py --write <slug>` for each of the 22 dClosedLoop builds §4 "Files touched"
   lists.

Each output is then staged. The packets are rendered here, not after the re-attach, because their
parent states read HEAD's tree, and only the provisional commit holds the merged one.

### The chain packets

Each conflicted packet is checked out from the run's side whole, `git checkout --ours -- <packet>`. That
side carries the identical instrument pins and both repin records, and the owner's schedule record is
one no agent may write back. The window's `--write` then keeps those pins and records and re-renders
every derived section from the merged tree. Where the run's bytes already equal that render, it prints
`packet: <path> is current, nothing written` and the run's `rendered at` stays. Otherwise the packet
names the provisional commit as its `rendered at`, the HEAD it was rendered at, which no ref holds.

### The manifest stamp

The block's `last-audit:` line is written once, `<ISO-8601 now> @ <the full sha of the merge's first
parent>`, KICK-dKeptSession-69 S4's stamp, so the staged leg sees a stamp unlike HEAD's.
`last-body-change:` keeps the run's `95a4a1188a65ed95efba0d40c5624b38b8e2b3c1`. It reads 9 against check 9's
threshold of ten (DERIVED by §4 "Evidence"'s count), where main's reads 17 and reds. Both sides' `watch:`
and `verify-paths:` lines are identical and stay.

### What it does not check

- That the merged tree is green beyond the criteria below. Every other leg is the close's (§3).
- That a packet's `rendered at` names a reachable commit. No reader resolves the field.
- That check 9 stays green past this commit. It reads 9 at the merge, PINNED 2026-11-23, so the next
  non-merge watched commit reds it unless that commit advances `last-body-change`.

### Inventory

Nothing is minted. The one new record is this unit's acceptance ledger.

### Migration

None for adopters: nothing ships that main did not already ship. Reversal is `git revert -m 1` of the
reconcile commit.

### Rollout

Live at the commit. The main loop re-runs the bar on the merged tree, then `--prepare` again.

### Files touched (estimate)

Every other path `git diff --name-only HEAD origin/main` lists arrives as the merge writes it, and any
other output S4's window rewrites arrives as it writes it.

- `.memory-tree.conf`, `tools/govkit/registry.toml`, `tools/lib/resolve-python.test.sh`,
  `tools/policy/catalogue.toml`, `tools/policy/check_policy.py`: S3
- `.governance/policy.json`, `help/reference/policy.md`, `memory/map/generated/MAP.md`,
  `memory/map/generated/symbols.json`, `tools/gate-legs.json`: S2, rendered in S4's window
- `memory/guides/SESSION-KICKOFF.md`: S4's stamp, owed because `.memory-tree.conf` and
  `tools/gate-legs.json` sit on its `watch:` line
- The packets, S5:
  `memory/builds/dBoundRoles/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dCalibratedLens/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dConvergedCharter/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dDeclaredLoop/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dFairHearing/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dFurnishedOrders/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dGroundRules/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dIndexedDesign/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dKeptSession/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dLinkedLibrary/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dMindYourWords/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dOrderedCharter/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dPlacedRequest/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dRankedPlan/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dSafePassage/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dScopedBuild/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dShippedRelease/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dTendedCadence/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dTotalRecall/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dTrueNorth/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dWellOiledMachine/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`,
  `memory/builds/dWitnessedBar/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
- `memory/builds/dKeptSession/build/2026-11-23-build-KICK-dKeptSession-80-1-acceptance-ledger.md`: S1
- `memory/builds/dKeptSession/README.md`, `memory/LIVE.md`, `memory/backlog/KICK.md`: rendered by S4's
  regeneration and the memory-hygiene leg's staged write, never hand-edited

### Alternatives rejected

- **Hand-merge the generated outputs, or keep one side's bytes.** No hand can reproduce a render's bytes,
  and either side's bytes are stale against the merged inputs.
- **Commit the merge, then regenerate in a follow-up commit.** The merge's hooks would grade it before its
  outputs are fresh, and the brief allows one commit.
- **Keep main's side of each packet.** It drops the owner's schedule repin record, which no agent may
  write back.
- **Render the packets after the re-attach, at the merge's first parent.** HEAD would then name the
  run's tree alone, so the parent states and blobs `#derive_sources` reads at HEAD would not be the
  merged tree's, which `--check` reads at the commit.
- **Keep main's `last-body-change`.** It reads 17 against check 9's threshold, DERIVED by §4 "Evidence".
- **Name main's member note `TWENTY-THIRD`.** Main's text is landed, and the run's is the side that lands
  onto it.

## 5. Production-readiness checklist

- security — no new write path or surface. The staged mirror is judged by the policy guard and
  admitted on the live run's branch, as at KICK-dKeptSession-69. The commit goes through the hooks.
- perf / scale — one regeneration, one reference render and the packet renders, once.
- error / empty / loading states — a render that fails in the window still re-attaches HEAD, and the
  builder reports its exit; a stale output then reds AC3 or AC9.
- observability — `regen.py --check` and each `chain-packet.py --check` name what is stale.
- risks — a pre-commit leg red over the merged tree refuses the commit. The builder fixes what a
  resolution here caused; any other red goes to the close, as §3 says.
- testing — the criteria below, each a direct read of the merged tree. No suite is added.
- migration — none for adopters; §4 "Migration".
- user docs — `help/reference/policy.md` re-rendered (S2).

## 6. Acceptance criteria

Each criterion is observed in the run worktree, after the main loop's reconcile commit unless it says
"staged", which reads the resolved merge before that commit.

- **AC1** — Staged: `git ls-files -u` prints nothing. At the commit, `git grep -l -e '^<<<<<<< ' -e
  '^>>>>>>> ' HEAD --` prints nothing.
  Red when: a conflict is left unmerged or a marker is committed.
  figure: no tracked file of either parent carries a marker line, PINNED 2026-11-23.
- **AC2** — `git rev-parse HEAD^2` prints `525f3ab9766e1c117a600cfd756593de5b46a8b6`, `git rev-parse HEAD^1`
  prints the run head the merge started from, and `git log -1 --format=%B | grep -c '^Pass:
  KICK-dKeptSession-80$'` prints `1`.
  Red when: the reconcile is a rebase, a squash, a merge of another tip, or a commit without the trailer.
- **AC3** — `python tools/run-gates/regen.py --check` exits 0, and `python
  tools/playbook/render_playbook.py --reference --check` exits 0.
  Red when: a generated output is hand-merged or left at one side's bytes.
- **AC4** — `grep '^PROJECT_REGISTRY_EXTRA=' .memory-tree.conf | tr ' "' '\n\n' | grep -cx -e
  cleanup-sites.txt -e unnamed-keys.txt -e unpurposed-namespaces.txt` prints `3`, and `grep -c -e '^#
  TWENTY-SECOND MEMBER, TOOL-dQuietDisk-9 S6' -e '^# TWENTY-THIRD AND TWENTY-FOURTH MEMBERS,
  KICK-dKeptSession-69' .memory-tree.conf` prints `2`.
  Red when: either side's words or member note is dropped, or both notes claim one ordinal.
- **AC5** — Over `tools/govkit/registry.toml`, `grep -c` prints `3` for `presets.py`, `4` for
  `design_lib.py`, `5` for `legacy_ledger.py` and `5` for `coverage_join.py`.
  Red when: a guard keeps one side's lines alone.
  figure: PINNED 2026-11-23 from trial tree 162162b7, each the lines outside the hunks plus one per guard.
- **AC6** — `grep -c -e '^history_store_py|' -e '^history_store_sh|' -e '^template_cache_sh|' -e
  '^remove_tree_py|' -e '^owned_work_py|' -e '^owned_tempdir_py|' -e '^owned_work_sh|' -e
  '^extract_route_units_js|' -e '^card_file_rel_js|' tools/lib/resolve-python.test.sh` prints `9`, and
  `grep -c -e '^# history_store_py and history_store_sh' -e '^# extract_route_units_js and
  card_file_rel_js' tools/lib/resolve-python.test.sh` prints `2`.
  Red when: either side's parity rows or their comment paragraph is dropped.
- **AC7** — Over `tools/policy/catalogue.toml`, `grep -c '^\[\[key\]\]$'` prints `277`, `grep -c
  '^\[\[namespace\]\]$'` prints `14`, and `grep -c -e '^name = "install.baseline"$' -e '^name =
  "tests.history-verdicts"$' -e '^name = "tests.fixture-templates"$'` prints `3`.
  Red when: main's keys or the run's namespace purposes are dropped.
  figure: PINNED 2026-11-23, main's key count at `525f3ab97` and the run's namespace count at `0a39514a6`.
- **AC8** — Over `tools/policy/check_policy.py`, `grep -c -e '^import presets  # noqa: E402' -e '^def
  init_owned_tempdir() -> str:'` prints `2`, and `python -m py_compile tools/policy/check_policy.py`
  exits 0.
  Red when: the presets import or main's inline blocks are dropped, or the join does not parse.
- **AC9** — `python tools/chain-packet.py --check <slug>` exits 0 for each of the 22 slugs §4 "Files
  touched" lists. `grep -c '^- repinned inside a live chain run: '` over each packet prints `2`. A plain
  `python tools/check-spec-tokens.py` prints `spec-tokens: packet join · 1 live chain run(s) · 1
  packet(s) checked` and no row carrying `[packet]`.
  Red when: a packet keeps main's side, which drops the owner's record, or is left stale against the
  merged tree.
  cost: each `--check` walks the instrument once, about 20 seconds, PINNED 2026-11-23.
  figure: the live count is PINNED 2026-11-23 from the trial tree's `RUN.md` phases.
- **AC10** — Staged: `bash skills/session-kickoff/manifest-check.sh --staged` exits 0. At the commit,
  `grep -c '^last-audit: ' memory/guides/SESSION-KICKOFF.md` prints `1` and its sha is `git rev-parse
  HEAD^1`, `grep -c '^last-body-change: 95a4a1188a65ed95efba0d40c5624b38b8e2b3c1$'` prints `1`, `grep -c
  -e 'even if its repo is gone' -e 'over a harnessed unit'` prints `2`, and a plain `bash
  skills/session-kickoff/manifest-check.sh` prints no `MANIFEST check 9 FAILED` line.
  Red when: both stamps are kept, the stamp names a commit the audit did not read, main's
  `last-body-change` is kept, or a side's dated correction is lost.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `kickoff-manifest ratchet` · `policy fixtures` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `routed-commits selftest` · `scratch-guard self-test` · `kit/dogfood doc parity` · `straggler-guard arms` · `transition-audit arms`

No suite runs in this pass. The pass's own legs are `bash tools/run-gates/pass-legs.sh --base <the run
head>`, which the main loop runs over the staged merge before its commit.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-23 · initial draft, from the brief `2026-11-23-prompt-KICK-dKeptSession-80-spec-brief`,
  grounded at `0a39514a6` and at `origin/main` `525f3ab97` through `git show` and a read-only `git
  merge-tree`, with KICK-dKeptSession-69's S1, S2 and S4 re-keyed.

## 10. Reuse audit

The seam extended is KICK-dKeptSession-69's reconcile procedure, its S1, S2 and S4 and its §4 per-file
table, copied and re-keyed to `525f3ab97`. The regeneration reuses
`tools/unattended/pass-tree.sh#run_pass_tree_regen`'s provisional-commit condition by hand, the packets
reuse `tools/chain-packet.py#main` under `--write` and `--check`, and the reference page reuses
`tools/playbook/render_playbook.py#render_reference_pages`. Every registry row was resolved by the merge
driver `tools/memory-tree/merge-rows.py`, so no row rule is written here. `python
tools/codebase-map/reuse_lookup.py "reconcile a run branch with origin/main in one merge commit,
regenerating generated outputs over a provisional merge commit"`, run 2026-11-23 at `0a39514a6`, ranked
name stems only (`run`, `main`, `merge`); the `branch-reconcile` kit it surfaced sweeps stale
branches and merges nothing, so no further seam fits. The recall query returned PLAY-dOrderedCharter-83
and TOOL-dFoldedAudit-17, the two reconciles whose manifest handling §4 "The manifest stamp" follows.

Recall terms used: `python tools/memory-recall/query.py "second reconcile of a run branch with origin/main, chain packets re-rendered, kickoff manifest re-stamped over a merge" --terms "reconcile merge origin/main provisional regen chain-packet repin rendered-at last-audit last-body-change re-stamp union"`
