**Serves:** research KICK-dKeptSession-43

# Brief — dKeptSession: KICK-dKeptSession-43 built from its spec

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
5. Before the commit, run `python tools/lexicon/lexicon.py` and see it exit 0: every function the unit adds is graded, nested helpers included, and a name outside the declared verbs (the first units added `judge`, `ok` and `plant_…` helpers) is renamed with `lexicon.py --suggest`. Pin every figure the acceptance ledger states with DERIVED or PINNED on its line, and run `python tools/playbook/writing_practice.py check pinned-facts`. Both are your role's own checks. Where the ledger quotes an output line naming a file with a line suffix (a refusal's `<path>:0`), describe the line instead of quoting it: the positional leg reads any `<path>:<number>` token as a line citation.

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
