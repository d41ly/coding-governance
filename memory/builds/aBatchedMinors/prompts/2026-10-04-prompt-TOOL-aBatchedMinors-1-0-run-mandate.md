# Run mandate — aBatchedMinors

**Serves:** journal TOOL-aBatchedMinors-1

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `a`, 2026-10-04. The value
carried whitespace and named no readable file, so it is the prompt itself. The bytes travel here
rather than as a reference, because the build folder is the authorization and may not point at a file
that can be edited after the run starts.

## The prompt

> Changes are required to the unattended build toolkit's protocol - currently, a closing review's
> findings of Blocking and High severity are promoted to their own build units, and Medium and Low are
> disposed on the spot through their spec. This needs to change - ALL of closing review round findings
> should be promoted, MEDIUM and LOW should be grouped together to 1 or 2 units. Review the current
> workflow, design an efficient improvement and build it per the protocol.

## How the run reads it

- "Closing review" is the build method's M8 closing diff review, whose `--review` subject is the
  build slug. A spec audit's mediums and lows are folded into the spec under review, which IS their
  fix, so that disposition is left as it is.
- "Grouped together to 1 or 2 units": one unit by default, whose `closes` list names every medium
  and low; two only when the findings split into two disjoint write sets, so the halves build
  concurrently. Never one unit per minor finding.
- No question was asked: ACCEPTANCE and GATES derive from the existing `--review` verb and check 2.
