# TOOL-dTrackedAtlas-4 — acceptance ledger

**Serves:** journal TOOL-dTrackedAtlas-4

No merge bar, gate or self-test suite ran in this pass. The hook and its conf are the ones built in the
earlier pass and held outside the repository, unchanged, since rev-7 changes nothing of the hook's design;
the settings group, the dossier, the map's regenerated artifacts and the loop table's row are this pass's.
Every criterion was re-observed on this tree. AC1 to AC9 ran by the spec's own commands in a scratch clone
of the worktree at `%TEMP%/ta4fx`, its `origin` a bare clone at `%TEMP%/ta4o` and its page home `%TEMP%/ta4h`,
with the hook, the conf and the settings group carried in as one fixture commit, `78202caf7d48`, on top of
the pass's base `ed2912b4c`, pushed as the bare clone's `main`. The clone's conf named the page in its
drive-letter form, the spelling `cygpath -m` gives for `$P`: node reads an MSYS `/c/...` path as rooted on
the current drive. Each red was observed by a staged copy of the hook beside it in the clone's build folder,
one substitution each, run and deleted, so no tracked file was edited to stage a red. AC8 and AC10 ran in
the worktree itself. The clone, the bare clone and the home were removed after.

**The real page home was written once, by mistake, and restored.** The first runner start in the clone ran
before its conf edit had taken, so it read the tracked conf and handled the fixture tip against
`C:/projects/coding-governance-atlas/`: it logged `78202caf7d48 current`, left the page untouched (its
modification time stayed `10:44:37` local, before the run), and created the `.regen.log` and `.regen.tip`
sidecars there. Both held only that run's line and sha, and both were deleted, leaving the folder holding the
page alone. Every later run first checked that the clone's conf named `ta4h`.

**Evidences:** TOOL-dTrackedAtlas-4
- First run — `node "$C/$REGEN" --run` exited `0` in `49 s` and logged
  `78202caf7d48 regenerated — in 39 s, 17266 KB; the check answered atlas: absent — no page at <P>`; the
  page's check at `origin/main` exited `0` with `atlas: current`, its stamp's `commit` reading
  `78202caf7d48a83d102559ff889b2168c0f72947`.
- AC1 — with the stamp set `2 seconds ago`, the hook given the `ls` input exited `0` in `79 ms`, printed
  nothing, and `stat -c %Y` read `1795082080` before and after. Red: with the stamp set `2 minutes ago` by
  `touch -d`, the same call exited `0` in `80 ms` and the stamp moved from `1795081962` to `1795082082`; with
  the tip sidecar deleted too, the started runner's line, `78202caf7d48 current`, reached the log within `3 s`.
- AC2 — landing `cb774b8cbb13` appended to `memory/builds/dWitnessedBar/RUN.md`; with the stamp deleted the
  hook given the lander input exited `0` in `63 ms`, printing nothing; the log gained
  `cb774b8cbb13 regenerated — in 38 s, 17266 KB; the check answered atlas: stale — …` within `30` polls of
  `3 s`; the check at `origin/main` then exited `0` with `atlas: current — … match the stamp of cb774b8cbb13`,
  and the stamp's `commit` equalled `git rev-parse origin/main`, `cb774b8cbb134ff78b5ab99f72e64453ccc2a8ce`.
  Red: the same check run after the push and before the hook exited `1` with
  `atlas: stale — <P>: the inputs stamped at 78202caf7d48 moved by origin/main (cb774b8cbb13)`.
- AC3 — landing `9b48c0997e40` appended to `memory/builds/dTrackedAtlas/README.md`; the runner exited `0`,
  logged `9b48c0997e40 current — atlas: current — … match the stamp of cb774b8cbb13`, and `cmp` found the page
  byte-identical to the copy taken before. Red: with the tip sidecar deleted, a staged runner whose check
  branch reads `if (false)` exited `0`, logged `9b48c0997e40 regenerated — in 37 s, 17266 KB`, the page
  differed, and its stamp's `commit` read `9b48c0997e40479e1e91ebce7d6fa1ecf29ed976`.
- AC4 — with `atlas.regenerate` set `off`, landing `94b1ab291af2` on `RUN.md`: the runner exited `0`, logged
  `94b1ab291af2 skipped — atlas.regenerate is off`, the page was byte-identical, and the check at
  `origin/main` exited `1` with `atlas: stale — … moved by origin/main (94b1ab291af2)`. With `maybe`, landing
  `fe627e86e9cb`: exit `0`, `fe627e86e9cb skipped — atlas.regenerate is 'maybe', outside on off`, the page
  byte-identical. Red: set back to `on`, landing `b4597b9136e0`: exit `0`,
  `b4597b9136e0 regenerated — in 45 s, 17266 KB`, the stamp's `commit` `b4597b9136e021087931c727a09c83686b95dd81`.
- AC5 — with `atlas.page` at `%TEMP%/ta4none/closed-loop-atlas.html`: the hook given AC2's input exited `0`
  printing the one line `atlas-regen: nothing done — no page home at C:/Users/<user>/AppData/Local/Temp/ta4none on this node`,
  given AC1's input exited `0` printing nothing, `--run` exited `0` printing the same line, and `ls -d`
  found no `ta4none`. Red: a staged runner whose two folder checks read `if (false)` exited `0` printing
  nothing, its lock write failing on the absent folder; `ta4none` still did not exist.
- AC6 — the spec's `sed` inserted `raise SystemExit(3)` directly above `if __name__ == "__main__":`, landed
  as `44013f696eb9`; `"$PY" "$C/$ATLAS" --check --page "$P" --ref origin/main` exited `3` with stdout empty.
  The runner exited `1`, logged `44013f696eb9 failed — generation — exit 3; the check answered exit 3`, the
  page was byte-identical, `ls -d` found no `$H/regen-*` and no `$H/*.regen-*.html`, and
  `git worktree list` listed the clone alone. Red: with the tip sidecar deleted, a staged runner whose
  `finally` skips `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js#removeScratch`
  exited `1`, and `$H/regen-24104` remained, listed by `git worktree list` as `44013f696 (detached HEAD)`.
  The next real runner's leftovers pass removed it: no `regen-*` remained and the list held the clone alone.
- AC7 — after landing `120b811bd31b`, the revert of the plant, a lock written fresh by hand: the runner
  exited `0` in `51 ms` and the log stayed at `10` lines. With the lock set `41 minutes ago` by `touch -d`,
  the run logged `stale lock removed — 2460 s old`, then `120b811bd31b current — atlas: current — …`, and
  exited `0`. Red: landing `14d60e04322d`, a fresh lock again, and a staged runner calling
  `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js#writeLock` without
  reading its answer: it handled the tip, logging `14d60e04322d regenerated — in 79 s, 17266 KB`.
- AC8 — the `node -e` one-liner over `$W/.claude/settings.json` found `1` `PostToolUse` group with matcher
  `Bash|PowerShell` naming `$REGEN` with `timeout` `10`, and `$W/$REGEN` existed. Red: the same one-liner over
  `.claude/settings.json` at the base `ed2912b4c` found `0`.
- AC9 — after AC2 to AC7, `git status --porcelain` listed only ` M` `$CONF`, `git worktree list` one
  checkout, `git log ed2912b4c..origin/main` only the fixture's `9` commits authored `fx`, and `ls -A $H` the
  page and its `.regen.stamp`, `.regen.tip` and `.regen.log`. Red: landing `1f26b8392a79`, and a staged runner
  that runs `git commit --allow-empty -m "regen: the page"` in the root after its rename: `git log` then
  showed `e2b643f90 fx regen: the page` above the landing.
- AC10 — in the worktree, after `gen_map.py --write` rewrote `inventories.json`, `MAP.md` and `CARDS.md`
  and left `symbols.json` byte-identical: the spec's probe printed `[] []`, `gen_map.py --check` exited `0`,
  and `tools/loop/stage_coverage.py` exited `0` with no line naming `closed-loop-atlas` or
  `dTrackedAtlas`. Red: with the dossier's `harness-hooks` row emptied in the working copy, the probe printed
  the hook's key in its first list; with the `[[hook]]` row taken out of `tools/loop/loop.toml`, stage
  coverage exited `1` printing
  `stage-coverage: unclaimed hook PostToolUse memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js · no claim`.
  Both files were restored byte for byte and the probe read `[] []` again.

Probed beside the criteria:
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js#readConf` read the
tracked conf as `on` and `C:/projects/coding-governance-atlas/closed-loop-atlas.html` without touching that
folder, and answered null for a relative page, a `..` segment, a `.htm` page, a bare `.html` name, an
unparseable conf and an array, each behind a CRLF `//` comment line; a missing `atlas.regenerate` read as
`on`. `tools/loop/loop_lib.py#read_definition` parsed the edited `tools/loop/loop.toml` whole. Every
function name the hook declares was graded `OK` by `python tools/lexicon/lexicon.py --suggest <name> --as js.function`.

Owed to the close: the bar with the self-test suites on, as §7 and §8 F3 (a) name, with its legs
`codebase-map coverage + freshness`, `loop stage coverage`, `loop definition`, the kit epoch leg at the
push boundary, and `check-wiring self-test`. No new arm is declared, so no RED-first observation is owed.
