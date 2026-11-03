**Serves:** research PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-24

# Brief: PLAY-dOrderedCharter-63 — the spec-token checker reads a spec's status from its header, and the foreign spec it misread

## The prompt

> dOrderedCharter

— owner, 2026-11-02, invoking `/unattended` for the build run. Unit 24's `--dispatch` (run wf_7db2dca6-39a) was
refused by check 49: `tools/check-spec-tokens.py` exits 1 over the tree on
`memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-12.md [guards] playbook render selftest <-
tools/memory-tree/design_lib.py`. That spec's header (line 3) reads `DEFERRED`, so it is not live; the checker's `LIVE`
pattern (`tools/check-spec-tokens.py:356`, `re.M`) matches the `**Status:** OPEN` line of a fenced markdown example at
its line 110 and grades it live. Unit 51's pass (`1f078024a`) added `design_lib.py` to the `playbook render selftest`
guard, which that spec's Files touched names. Every dispatch of this build is refused until the tree reads green, so the
foreign spec is fixed first and the checker defect is adopted as a unit (UNATTENDED-PROTOCOL §11).

## The brief

### Goal

Unblock every dispatch with the narrowest outside edit, and spec the checker repair that removes the class.

### Items

1. **TOOL-dIndexedDesign-12.** Add `playbook render selftest` to its §7 leg line, spelled byte for byte as in
   `tools/gate-legs.json`; bump its **Status:** rev by one, dated 2026-11-03, its status kept `DEFERRED`; add one §9 line
   naming this brief and the guard unit 51 widened. Change nothing else in it. This is an outside write the build's
   README lists in the departures report.
2. **Spec 63 (new).** The checker decides a spec's liveness from its status header (the first `**Status:**` line, or
   the first one outside any fenced block, decided by M3 against the tree, with the loser and its test in §8), never
   from a fenced example. ACs by fixture plants of the checker (a DEFERRED spec holding a fenced `**Status:** OPEN`
   example reads not live; a live spec still grades), and a measure over the real tree of how many specs change
   liveness under the rule, written into §6. Tier-2, `DEFERRED`, `order 7`, `streams playbook`, `base 8bec4cef`,
   `advances PLAY-dOrderedCharter-38`, `**Derived:** PLAY-dClosedLoop-2` on its own line under the Status line; §3 Edges
   name no sibling unit unless one is consumed. §7's leg line names every leg whose guard its Files touched trips;
   New arms on `New arm:` lines; no AC observes a suite or a bar.

In every spec you write or revise:

- Verify every path, count and line you cite against the tree at HEAD; stay under the 47000-byte authored budget.

For the run:

- Writes stay in the two spec files named and the files `gen_build_index.py --write` rewrites.
- This is an unattended run and nobody answers a question: a fork no option survives is written as an open §8 item
  with the options and the veto, and said in the return.
- Do not commit and run no check: the main loop re-renders the packet, runs the spec-token check, renders the index
  and commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return TOOL-dIndexedDesign-12's new rev and leg line, spec 63's path, its AC list in one line each, its §8 decision
  with the loser, and the measured count.

### Acceptance

- `grep -n 'playbook render selftest'` prints TOOL-dIndexedDesign-12's §7 leg line.
- `grep -n '^# PLAY-dOrderedCharter-63'` prints the new spec's H1, its Status line `DEFERRED` with `order 7`.

### Gates

The spec-token check, run by the main loop before the commit.

### Non-goals

No code; no other edit of TOOL-dIndexedDesign-12 or any other spec.

### Limitations

The items above, "For the run".

### Reuse

`tools/check-spec-tokens.py`'s `LIVE` pattern and the fence handling its other joins already use (`extract_acceptance`
and the claims join read outside fences).
