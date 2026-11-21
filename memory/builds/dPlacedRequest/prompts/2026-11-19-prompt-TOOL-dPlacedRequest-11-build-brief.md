**Serves:** research TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64

# Brief — dPlacedRequest: the build run, every carried unit built from its spec

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

Build every carried unit of dPlacedRequest, the Entry build of the dClosedLoop chain, from its spec under
`memory/builds/dPlacedRequest/spec/`, one unit per pass in the order the specs' `order` verbs declare, so the 18
gaps its README names close and the build lands. The spec set was audited for this run (three rounds, the chain
stopped on its own work); each spec as it stands at the pass's base is the design.

### Items

1. Build the one unit the pass names, exactly as its spec states: §2 Scope, §4 Design, §5 Files touched and §6
   Acceptance criteria. Read the spec whole first; its §10 names the seam to extend.
2. Probe every claim the spec makes about current code against the tree before the first edit: specs were written
   against older bases, and several name functions a parent build or an earlier unit of this build creates. Where
   the tree disagrees with the spec in a way the design depends on, hand the divergence back rather than building
   around it.
3. Observe each acceptance criterion the pass can observe with a fixture or a probe of the unit's own code, and
   record each observation in the unit's acceptance ledger under the build folder, the way earlier builds' ledgers
   do. A criterion only a gate or a suite can observe, and every `New arm:` line's RED-first observation, is named
   in the return and left to the main loop.
4. Commit the unit as one pass on the run branch, the unit id in the subject and a `Pass: <unit id>` trailer, with
   the spec's status header flipped to CLOSED in that commit when every criterion the pass owns is observed.

### Acceptance

Each unit's commit carries the code its §5 names and an acceptance ledger observing its §6 criteria, and the pass
legs the main loop runs after the commit read green; the closing review and the full merge bar run once after the
last unit.

### Gates

None inside a pass: the main loop runs the pass legs after each unit commit and the full bar once at the close.

### Non-goals

No unit other than the one the pass names; no spec edit beyond the status cell (a divergence goes back to the main
loop, which has the spec writer revise the spec); no edit to the build README's goal; no write outside the build
folder and the paths the main loop declared with `--dispatch`, except one ask row in another build's BACKLOG.md
where a spec says so; no unattended-kit self-test suite (owner waiver, the README's last build-level rule).

### Limitations

Windows with Git-Bash: give git forward-slash paths, write LF, and spell the session scratchpad literally because
TMPDIR is unset in the Bash tool. Product kits under `tools/` follow the charter's `[portable]` practice: Python for
logic, shell as a thin shim. Every new name is checked with the naming lexicon before it is written.

### Reuse

Each spec's §10 names its seam and its recall terms; the build-level probe is in the kickoff card (terms: lease claim
ref compare-and-swap epoch tombstone offer feed placement entry.claim request card).
