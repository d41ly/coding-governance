**Serves:** research KICK-dKeptSession-1

# Brief — dKeptSession: KICK-dKeptSession-1 committed from its built and saved pass

## The prompt

> /unattended dKeptSession

## The brief

### Goal

Build every carried unit of dKeptSession, the Session build of the dClosedLoop chain, from its spec under
`memory/builds/dKeptSession/spec/`, one unit per pass in the order the specs' `order` verbs declare, so the 8
gaps its README names close and the build lands. The spec set was audited by the spec run (its chain stopped at
the owner's no-HIGH ruling of 2026-10-26) and re-grounded on this run's tree before each build; each spec as it
stands at the pass's base is the design.

### Items

1. Build the one unit the pass names, exactly as its spec states: its Scope, Design, Files touched and Acceptance
   criteria. Read the spec whole first; its Reuse audit names the seam to extend.
2. Probe every claim the spec makes about current code against the tree before the first edit: an earlier unit of
   this build, or a parent, may already have moved what the spec names. Where the tree disagrees with the spec in a
   way the design depends on, hand the divergence back rather than building around it.
3. Observe each acceptance criterion the pass can observe with a fixture or a probe of the unit's own code, and
   record each observation in the unit's acceptance ledger under the build folder, the way earlier builds' ledgers
   do. A criterion only a gate or a suite can observe, and every `New arm:` line's RED-first observation, is named
   in the return and left to the main loop.
4. Commit the unit as one pass on the run branch, the unit id in the subject and a `Pass: <unit id>` trailer, with
   the spec's status header flipped to CLOSED in that commit when every criterion the pass owns is observed.

### Acceptance

Each unit's commit carries the code its Files touched names and an acceptance ledger observing its criteria, and
the pass legs the main loop runs after the commit read green; the closing review and the full merge bar run once
after the last unit.

### Gates

None inside a pass: the main loop runs the pass legs after each unit commit and the full bar once at the close.

### Non-goals

No unit other than the one the pass names; no spec edit beyond the status cell (a divergence goes back to the main
loop, which has the spec writer revise the spec); no edit to the build README's goal; no write outside the build
folder and the paths the main loop declared with `--dispatch`, except one ask row in another build's BACKLOG.md
where a spec says so; no gate leg, merge bar or self-test suite inside the pass.

### Limitations

Windows with Git-Bash: give git forward-slash paths, write LF, and spell the session scratchpad literally because
TMPDIR is unset in the Bash tool. Product kits under `tools/` follow the charter's `[portable]` practice: Python for
logic, shell as a thin shim. Every new name is checked with the naming lexicon before it is written.

### Reuse

Each spec's Reuse audit names its seam and its recall terms; the build-level probe is in the kickoff card (terms:
preset policy mailbox notice card pointers context window compaction attendance deps.coordination actions.free
orient.budget).

The pass before this one (run `wf_2fada365-a7c`) built the unit at rev-9, observed every criterion a pass can observe, and was refused at its commit only for paths outside its declared write set. Its whole staged change is saved outside the repository and applies at this pass's base: `C:/Users/d41ly/AppData/Local/Temp/claude/39caabfa731fb66d/d5b6d4ab-72df-4e61-9a7c-05dde93b7f5b/scratchpad/k1/KICK-dKeptSession-1-rebuild-2.patch`, with its commit message beside it in `commit-msg.txt`. Apply it with `git apply` excluding the three generated renders it carries (`memory/LIVE.md`, `memory/backlog/KICK.md`, `memory/builds/dKeptSession/README.md`, which moved since and are re-rendered by `python tools/memory-tree/gen_build_index.py --write`), read it against the spec as a reviewer would, and then finish what its commit lacked: re-stamp the kickoff manifest `memory/guides/SESSION-KICKOFF.md` with a `manifest-audit:` delta line in the commit message, as its staged leg asks; regenerate `memory/map/generated/symbols.json` with `python tools/codebase-map/gen_map.py --write`; correct `help/loop.md`'s "Making a new part" section, which still says six factories and omits the preset one; and let the hook's index renders ride the commit. The write set now declares those paths.
