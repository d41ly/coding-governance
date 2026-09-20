**Serves:** journal TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1

# dDerivedDocket — the build-pass brief

*Handed to every unit pass of the unattended build `dDerivedDocket`, beside that unit's spec. The spec
is the design. This brief carries the rules every pass shares, so no spec restates them.*

## What a pass does

Build ONE unit, the one named in your prompt. Read this brief and the unit's spec whole before you
touch code, then read `memory/guides/BUILD-METHOD.md` M6 and M7. Re-verify on the tree every claim the
spec makes about current code: other units of this build have landed on the branch since the spec's
`base` (`fb07ca25` for every spec after the regrounding), and a line citation may have moved. Where the spec is wrong, change the spec first,
as a rev bump with its section 9 line, then write the code.

## Hard rules

- Work only in this worktree, on its branch. Never push, merge, rebase, reset, stash or check out
  another branch, and never touch `main`.
- Never `--no-verify`. The pre-commit hook takes minutes, so give every commit a 600000 ms timeout.
  End each commit message with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
- Stage explicit paths, never `git add -A` or `git add .`.
- Call Python as `python`, never `python3`. In the Bash tool a heredoc loses an escape level, so write
  any helper script to a file and run it. Scratch goes under a `mktemp -d` directory, never the tree;
  do not trust `$TMPDIR`, which can be unset in this shell and then resolves to the MSYS root.
- **Run no gate** (owner rule). No section 7 leg, no `tools/gate-legs.json` row, no hand-run checker
  such as the hygiene gate or `tools/check-spec-tokens.py`, and never `tools/run-gates/run-gates.sh`.
  Every gate runs once, after all units are built. A criterion whose observation IS a gate leg is owed
  to that post-build run, and the orchestrator writes its ledger line then. The pre-commit hook still
  fires on your commit; that is the hook, not a gate you ran.
- **A fixture run needs the call's own working directory inside the fixture.** `tools/unattended/gate-guard.js`
  resolves the repository from the tool call's payload working directory, not from a `cd` inside the
  command, so a fixture suite run made from this tree is judged against this run's phase and denied.
- **The test file you are writing is the exception**: run it directly, because that is how its refusals
  are staged RED. Two limits apply. Only units 1, 3, 4, 5, 16, 17, 18, 22, 24, 27, 28 and 30 run
  unattended-kit suites, each once at the unit's end: the owner's scoped lift of a standing instruction
  that otherwise forbids running them. And a suite whose criterion carries a `permission:` line
  deferring it to the post-build bar is not run in the pass.
- **Dark until the flip.** Before unit 34, the shards mode stays byte-identical. New behaviour waits
  behind `BACKLOG_MODE="builds"`, a blank key, or inert data, exactly as the spec says.
- A kit file names nothing outside itself by literal (charter section 12). A kit's version moves only
  where the spec says it moves.

## Before the commit

1. Stage your paths, then run `python tools/memory-tree/gen_build_index.py --write` and stage what it
   rewrote.
2. When you added or renamed a symbol, a leg, a hook or a guide, claim it in its map dossier under
   `memory/map/features/`, refresh that dossier's prose, and run
   `python tools/codebase-map/gen_map.py --write`.
3. When you edited a file in `memory/guides/SESSION-KICKOFF.md`'s `watch:` list, re-verify the
   manifest claims derived from it, re-stamp `last-audit` with your real local time and the merge-base
   sha, and put a `manifest-audit: delta <...> · watch-commits-since-stamp: <n>` line in the commit
   message.
4. Set the spec's status header to `CLOSED`, keeping its rev, or to `WONTDO` with a reason, in the same
   commit as the code.
5. Write the acceptance ledger at
   `memory/builds/dDerivedDocket/build/<today>-build-<unit-id>-1-acceptance-ledger.md`: a
   `**Serves:** journal <unit-id>` line, a title, then `**Evidences:** <unit-id>` and one line per
   criterion you observed in this pass, in the form `memory/HYGIENE.md` "Acceptance ledger" states,
   sharing a backticked token with its criterion. A criterion whose `permission:` line defers it to
   the post-build bar, or to a run the orchestrator makes after your commit, gets NO line from you;
   the orchestrator writes it after that run. A criterion you found wrong gets the AMENDED form,
   naming the rev that changed it.

Commit with the unit id first in the subject, then run the checklist command your prompt names and act
on each class it lists before you return.

## Return

`committed`, `sha`, `why` and `summary`. Return `committed: false` with a reason rather than a commit
you cannot stand behind. A refusal from `--dispatch` is binding: stop and return it.
