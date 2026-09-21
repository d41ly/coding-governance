# cMendedVintage — the acceptance ledger for unit 4

**Serves:** journal TOOL-cMendedVintage-4

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar and no `*.test.sh` suite
ran in this pass. Every line below was taken by replaying the criterion's own command at the shell,
against scratch git repositories under this run's scratchpad, never inside the worktree. Every
carrier was measured at BASE and at the tip, so each row has a RED behind it. Every observation was
then REPLAYED against the committed tree with the worktree clean, because an observation taken before
the last fold of the same commit is an observation of a tree the commit never held; all three
fixtures returned byte-identical verdicts.*

## The one thing worth reading twice

**Every criterion was run twice — once against the BASE blob and once against the tip — because the
whole unit is string derivation and a string that looks right proves nothing.** The three remedies
were replayed at a two-segment `scripts/gov/` install, which is the prefix where the old spelling and
the new one differ in both directions:

| carrier | what BASE printed | what the tip prints |
|---|---|---|
| `check-wiring.sh` agent-cap | `Fix: python3 tools/settings-merge.py` | `Fix: python3 scripts/gov/settings-merge.py` |
| `adopt-process-monitor.sh` wiring | `Wire each with: python $ROOT/tools/settings-merge.py` | `Wire each with: python $ROOT/scripts/gov/settings-merge.py` |
| `adopt-memory-recall.sh` copy line | `cp <gov>/tools/settings-merge.py tools/` | `cp <gov>/tools/settings-merge.py scripts/gov/` |
| `adopt-memory-recall.sh` invocation | `python tools/settings-merge.py --fragment …` | `python scripts/gov/settings-merge.py --fragment …` |

**The root install was checked as its own case, not inferred.** At a ROOT install `check-wiring.sh`
prints `Fix: python3 settings-merge.py` with no prefix segment at all, and `adopt-memory-recall.sh`
prints `cp <gov>/tools/settings-merge.py ./` — the `${TOOL_ROOT:-./}` branch, which is the only
branch the two-segment fixture never takes.

**The spec's Migration table was measured rather than trusted, and it was right to the occurrence.**
Running the gate's own `re_ship` predicate over the three carriers before and after gives
`tools/check-wiring.sh` 3 -> 2, `tools/memory-recall/adopt-memory-recall.sh` 8 -> 6 and
`tools/process-monitor/adopt-process-monitor.sh` 5 -> 5. The last row holds because `:219` is
`/`-preceded and the predicate never counted it, exactly as section 4 said.

**Two things this pass caught that the spec did not predict, both in its own new bytes.** A comment
quoting the dead spelling is itself a carried literal — the predicate's excluded lead class holds
`/`, `{`, `}`, alnum, `.`, `_` and `-`, and a backtick is not among them — so the first draft of the
`check-wiring.sh` and `adopt-process-monitor.sh` comments held the row at 3 and added a third AC2
hit. Both were reworded to name the prefix without the filename. The same trap caught the new test
arm: a negative assertion spelled `grep -q 'tools/settings-merge.py'` would have RAISED
`tools/check-wiring.test.sh` from 11 to 12, which `--write-ratchet` cannot absorb, so the pattern
deliberately stops before the extension and a comment beside it says not to complete it.

**Evidences:** TOOL-cMendedVintage-4

- AC1 — `bash <prefix>/check-wiring.sh --check` replayed in a scratch git repository holding a
  root install and a `scripts/gov/` install of this unit's `tools/check-wiring.sh`, an
  `agent-cap.js` under each, no `settings-merge.py` anywhere and no `settings.json`. The
  two-segment install prints
  `UNWIRED  agent-cap — agent-cap.js present but hook not in settings.json. Fix: python3 scripts/gov/settings-merge.py`.
  The same command against the BASE `859daa67` blob in the same fixture printed
  `tools/settings-merge.py` — the RED, measured before the deletion was made permanent.
- AC2 — `git grep -n 'tools/settings-merge.py' -- tools/check-wiring.sh` over the three carriers
  returns exactly two hits and they are the two the criterion sanctions: the usage line at
  `adopt-process-monitor.sh:16`, and the `<gov>/tools/…` source half of the memory-recall `cp`
  instruction at `:203`. Every other spelling in all three files is gone, not repathed. The run
  before the comment rewording returned three, and the third was this unit's own prose.
- AC3 — `bash <prefix>/process-monitor/adopt-process-monitor.sh --check` in a scratch repository
  with the kit at `scripts/gov/process-monitor/`, a parsing `.process-monitor.conf` declaring one
  root, and an empty `hooks` object in `settings.json`. The tip prints
  `Wire each with: python $ROOT/scripts/gov/settings-merge.py <that --fragment>` with `$ROOT`
  expanded; the BASE tree in the identical fixture printed `$ROOT/tools/settings-merge.py`. The
  derivation is from `KIT_REL`, so the two fragment paths one line above and the merger path now
  answer the same question the same way.
- AC4 — `bash <prefix>/memory-recall/adopt-memory-recall.sh --scaffold --with-hook` with the kit at
  `scripts/gov/memory-recall/` and no `settings-merge.py` present. The `cp` destination and the
  invocation on the next line both read `scripts/gov/`, so the operator copies the tool into the
  directory the following command runs it from; at BASE they read `tools/` and `tools/`, both dead
  at that prefix. The comment above them was rewritten to describe the resolution the code now
  performs. The root-install variant of the same fixture prints `./` and a bare
  `python settings-merge.py`, which is the `${TOOL_ROOT:-./}` branch.
- AC5 — `bash tools/check-install-prefix.sh --check` exits `0` after `--write-ratchet` ran in this
  same commit, and the ratchet diff is the two predicted falls and nothing else:
  `tools/check-wiring.sh` 3 -> 2 and `tools/memory-recall/adopt-memory-recall.sh` 8 -> 6, both
  lower than at BASE `859daa67`. Before the rewrite the same command reported both as `SLACK`,
  which is the red this criterion exists to close.

Nothing is OWED. The spec numbers five criteria and all five were observed against the real scripts.

## What did not run, and why

`tools/check-wiring.test.sh` gained one fixture and two arms and was NOT executed as a suite, by this
pass's own mandate. Its failing case WAS observed: the arms' bodies were replayed verbatim in a
scratch harness built to the same shape, once against the tip and once against the BASE blob. Tip:
both arms 1. BASE: both arms 0 — and the two are independent, one asserting the derived spelling is
present and the other that the dead one is absent. The file passes `bash -n` and carries no CR bytes.
That suite is in `memory/project/testsuite-count-waivers.txt`, so there is no assertion floor to
raise.

The four `tools/install-prefix-waivers.txt` rows keyed to `tools/check-wiring.sh` moved six lines
before this unit and seven more because of it, to `455`, `505`, `721` and `730`. The reposition was
proved live rather than assumed: reverting one row to its old `448` and re-running
`bash tools/check-install-prefix.sh --check` exits `1` and reds a line this unit never touched;
restoring it exits `0`. A pin nobody has seen unpin is a pin nobody has tested.

No gate ran here. `check-wiring self-test`, `install-prefix (shipped surface)`, `process-monitor
wiring`, `process-monitor adopter selftest`, `memory-recall skill wiring`, `hook destinations` and
`settings-merge selftest` are owed to the bar this run closes with. `install-prefix` is the one of
them this pass ran directly, in its `--check` form, because the ratchet had to be rewritten in the
same commit and a fall left unwritten is a red bar on a repair.

One thing this unit deliberately left standing: `tools/process-monitor/adopt-process-monitor.sh:16`
still spells the merger under `tools/`. It is a usage line a human reads, its ratchet row's fourth
column already records the reason, and deriving it would hand the operator a variable to expand.
`WIRE-INTO-PROJECT.md` §3c and §3e likewise still name gov's own prefix, and are runbook prose rather
than shipped carriers.
