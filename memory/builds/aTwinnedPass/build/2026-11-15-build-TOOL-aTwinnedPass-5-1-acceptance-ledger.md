# Acceptance ledger — TOOL-aTwinnedPass-5

**Serves:** journal TOOL-aTwinnedPass-5

Built against spec rev-1 in one pass commit, on node a, in the pass's own worktree reset to the
dispatch commit `d61f577ac`. The spec's forks carry their resolutions, and the build follows each:
F1 (c), spec 1 stays frozen and this spec with its arm carries the corrected needle; F2 (a), the
admission arm is kept and a negative control is placed before it.

Three readings of the spec, named here for the main loop. None changes what an arm asserts:
- Spelling. Every `agent-p<n>` literal of §4 is written in the tip's spelling, `worktree-agent-p<n>`,
  as §3 "Edges" orders, since `TOOL-aTwinnedPass-4` respelled the fixture.
- Placement. T6 and T7 sit after T5's last arm, as §4 says, but after the `TP4` block that unit 4
  put there, so `TP4` runs over the state unit 4 observed. T7's status arm then also reads that
  `TP4`'s worktrees stay out of `git status`: `agent-q2` and `agent-zz` under the excluded
  `.claude/worktrees/`, and `agent-q1` outside the fixture.
- S8. The pass-tree suite's header names the second row, both switches and what the new arms do not
  check. The harness and driver suites carry their new arms' staged breaks and blind spots in the
  changed block's comment alone, as units 1, 3 and 4 did there, and their headers are unchanged.
  AC8 observes the block comments and the pass-tree header.

The §4 line numbers in `pass-tree.sh` moved with unit 4, at `def02e16` against this tip: the run check
is now at `:84`, its LANDED/ABORTED case at `:93`, its rc-2 case at `:98`, the staging loop at
`:263` to `:265`, the NOTE at `:266`, and `main`'s usage exits at `:305` to `:332`. Each staged break
is named by what it changes, so each still reads.

The observations below are each criterion's own command, run in the worktree with the change in
place before the commit, or the changed code over a hand-built fixture. No suite, gate leg or bar ran
in the pass. `check-arms.py --check` was refused for this role by the scratch-guard hook and is owed.

Owed to the main loop at the close, each red under its break and then green, one break at a time:
- the corrected `TP1 T3 ... has no worktree paragraph` arm of `tools/workflows/unattended-build.test.sh`, under §7's first `New arm:` line;
- in `tools/unattended/pass-tree.test.sh`: the two `remains at its tip` arms, red at base on git's `+` marker; the four M4 text arms; the fifteen T6 arms; the five T7 arms; the two L1 control arms; each under §7's `New arm:` lines for AC2 to AC6;
- B1's stdout `miss` and stderr `hit`, and the M2 `hit` and `miss`, of `tools/unattended/unattended.test.sh` shard 4, with `FLOOR_ASSERTIONS` 3342 and `FLOOR_SHARD_4` 423;
- the pass-tree suite printing no `FAIL` line, and the legs of the spec's Gates section, `harness arms (fail branches armed or pinned)` among them.

**Evidences:** TOOL-aTwinnedPass-5
- AC1 — `THIS PASS BUILDS IN A WORKTREE OF ITS OWN` — `grep -cF "'OWN WORKTREE'"` over the harness
  suite printed `0`; the same count for the single-quoted opening printed `2`, T1's control and
  T3's absence; over `tools/workflows/unattended-unit.js` the opening counted `1`.
- AC2 — `rev-parse --verify -q refs/heads/` — over the pass-tree suite, `grep -cF "tr -d ' *'"`
  printed `0` and `grep -c 'rev-parse --verify -q refs/heads/'` printed `3`, the two `remains` arms
  and TP4's. In a scratch repository, `git init`, one commit and `git worktree add -b agent-p4`,
  `git branch --list agent-p4` printed `+ agent-p4`, and `git rev-parse --verify -q refs/heads/agent-p4`
  exited 0 printing the tip.
- AC3 — `so it takes no pass back` — counted `1`, and so did
  `names no run branch (neither run-branch nor branch-ref)` and `has no run-state file at`. The four
  `check_merge_refused` calls of the M4 block sit at lines 270 to 279, after the fork-point arm at 258.
  Each text was read against `pass-tree.sh`'s own refusal, and `$RUNMD` against `runmd_of`'s
  `$M/builds/$1/RUN.md` under the fixture's `MEMORY_ROOT=memory`.
- AC4 — `check_usage_refused` — `grep -c '^check_usage_refused '` printed `5`, and the same count for
  `^check_usage_refused()` printed `1`. Each call was traced through `main`'s parse to its exit 2.
- AC5 — `FX_RENDER_NEW=1 FX_RENDER_STRAY=1` — counted `1`, as did `path = "fx-new.txt"` and
  `no effective generated output covers them: fx-stray.txt`. The fixture `render.sh`, cut out of the
  suite's heredoc and run over a hand-built repository: `--check` with both switches set exited 0 and
  wrote nothing; a plain write left no untracked file; `FX_RENDER_NEW` alone left `fx-new.txt`; both
  left `fx-new.txt` and `fx-stray.txt`, and `--check` after them exited 0.
- AC6 — `subject names TOOL-tRun-4` — counted `1`, at line 202, before the arm reading the merge's
  message exits 0 at line 205. The needle was read against check 49's text at `unattended.sh:14319`.
- AC7 — `tp5-b1.err` — counted `2`, and `--pass ARCH-tRun-4 --writes work/idx)` counted `1`. The
  floor lines printed, after the shadowed 675 one, `FLOOR_ASSERTIONS=3342` and `FLOOR_SHARD_4=423`,
  each below a `RAISED` line naming `TOOL-aTwinnedPass-5`. `run_main_at_head` runs its command
  directly, so the `2>` on B1's call separates the driver's stderr from its stdout.
- AC8 — `bash -n` — exited 0 over each of the three suites. Above the pass-tree suite's first
  `set -u`, `fx-new.txt` counted `2`, and `FX_RENDER_NEW` and `FX_RENDER_STRAY` each `1`.
- AC9 — `check_usage_refused` — `lexicon.py --suggest check_usage_refused --as sh.function` printed
  `OK — check_usage_refused leads with check`; after `gen_map.py --write`,
  `memory/map/generated/symbols.json` carries `"check_usage_refused"` once, and no other generated
  file moved. `check-spec-tokens.py --spec` over this unit's spec exited 0.
