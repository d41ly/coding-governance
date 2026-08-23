# testsuite counts — every self-test on the bar reports how many assertions actually ran

```toml
feature = "testsuite-counts"
title = "Executed assertion counts, in one shape, against a shrink-only floor"
status = "shipped"
streams = ["tooling"]
decisions = []

[claims]
gate-legs = ["testsuite counts (every bar self-test prints one)", "testsuite counts self-test"]
kits = []
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = ["arm-literal-strands-on-message-edit.md"]
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/check-testsuite-counts.sh",
  "tools/check-testsuite-counts.test.sh",
  "memory/project/testsuite-count-waivers.txt",
]
```

## Constraints & why

The failure mode of a TEXT join is that the text moves. Editing a `fail` message strands its arm
silently: the signature runs to the FIRST interpolation, so lengthening a message always strands
it while shortening never does, and the sibling test still quotes enough of the old sentence to
look correct. Caught three times in one file in one session — `arm-literal-strands-on-message-edit`.

`check-arms.py` grades TEXT: it joins each `fail` branch to an assertion string somewhere in the
matching self-test. It cannot see whether that assertion ever RUNS. Build cBriefedPilot shipped nine
arms stranded past an unconditional `exit`; the suite printed `PASS (86 assertions)`, `check-arms`
certified all nine as armed, and `ARMS_FLOORS` had just been raised for exactly those dead branches.
Every other gate in the suite held.

The only signal that moved was the executed total, and nothing compared it to anything. So the
mechanism is a floor on that total, and this leg is what makes the mechanism universal rather than
per-suite goodwill.

**The population is DERIVED from `tools/gate-legs.json`.** A hand-kept second list is how
`check-kit-versions.sh` grew a duplicate assertion that printed two messages for one defect, and the
manifest is already the single source for what the bar runs. A suite nobody runs has no count worth
checking, which is why the population is the manifest's and not `git ls-files '*.test.sh'`.

**It runs nothing.** Executing every suite to read its output would re-run the whole bar inside one
leg. The shape is read from the file, which costs milliseconds against legs that cost minutes.

**The non-compliant set is a shrink-only registry, not a silence.** Measured when the leg landed: 27
tracked suites, 12 printing no count at all, four different spellings among the 15 that did, and 3
floors. A leg with twelve silent exceptions checks nothing; one with twelve NAMED exceptions
ratchets, and a row whose suite now complies REDS as stale — the same rule
`install-prefix-waivers.txt` carries, for the same reason.

## Shared seams

- `tools/gate-legs.json` — the manifest is READ, never mirrored. `run-gates.sh` and
  `run-gates.test.sh` already treat it as the single source for what the bar runs; this leg is the
  third reader and adds no second list.
- `memory/project/*.txt` — the shrink-only registry convention, shared with
  `install-prefix-waivers.txt`, `unarmed-branches.txt` and the method-carrier list. Same directory,
  same stale-row-reds rule, and hygiene check 3's allowed set names it so a stray file there still
  reds.
- `FLOOR_ASSERTIONS` — the constant `TOOL-cBriefedPilot-23` introduced in three suites. This leg does
  not define it; it requires it, which is what turns a local habit into a contract.

## Reuse affordance

seam: `check-testsuite-counts.sh`'s derived-population read — reuse for any gate that must grade
every leg the bar actually runs rather than a list someone maintains; extend via the `grep -oE` over
`tools/gate-legs.json` argv strings, which yields repo-relative paths and needs no JSON parser.

seam: the shrink-only registry pair — reuse for any ratchet that must land green over a
non-compliant population; extend via the two refusals this leg pairs, a row that no longer hides
anything and a row naming something outside the population. Either alone lets the list rot.

## Affordances

- `bash tools/check-testsuite-counts.sh` — the leg. Silent + exit 0 is compliance.
- `memory/project/testsuite-count-waivers.txt` — the shrink-only non-compliant set. Delete a row when
  its suite gains a count; the leg reds if you delete one too early or too late.
- The agreed shape is `echo "PASS ($n assertions)"` plus `FLOOR_ASSERTIONS=<int>` at the top.

## Gaps

- **The 21 seeded waivers are the work, and they are not done.** The leg forces new suites to comply
  and lets old ones drain; nothing schedules the draining.
- **The count is per-suite, not per-arm.** A suite that loses one arm and gains another nets to the
  same total. `check-arms.py` owns the per-branch join and this leg deliberately does not duplicate
  it — but the pair still cannot see a one-for-one swap.
- **`skills/session-kickoff/manifest-check.test.sh` was believed to have no counter and did.** The
  spec that proposed adding one had grepped for another suite's spelling and reported a missing
  capability after measuring a missing convention; the M4 audit caught it as a blocker. Recorded here
  because the same mistake is available to anyone extending this leg's population.
