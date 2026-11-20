**Serves:** research TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-17 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26

# Spec task — dQuietDisk: four forks marked resolved, and unit 26 authored

You write specs only, in `memory/builds/dQuietDisk/spec/`. You do not commit. Read the build's spec brief,
`memory/builds/dQuietDisk/prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md`, whole first. Its rules bind
this task: read code at `609cd40b1`, cite as `<path>@609cd40b1:<line>`, verdicts unchanged, the saving counted, the
cache a switch, safe fallback, and no unattended-kit suite.

## 1. Mark the resolved forks in place

The run resolved these under its mandate (BUILD-METHOD M3). Mark each in the shape `memory/TEMPLATE-SPEC.md` §8
states, `RESOLVED (agent, 2026-11-20, delegated): <pick>`, with the one-line reason given below. Then apply what the
pick changes to the spec's own scope, design and acceptance, bump its rev, and add a revision-log line naming this
task file by its stem.

- **TOOL-dQuietDisk-8, F1 → (b)**: each reader takes its own `--shared` clone of the repository, and nothing is
  handed between legs. Every reader mutates its copy, so (a) saves nothing over (b) and would add a runner surface.
- **TOOL-dQuietDisk-10, F1 → (b)**: unit TOOL-dQuietDisk-26 now carries `check-wiring.sh`'s one listing (section 2
  below). Point unit 10's design at 26 where it mentions the listing, and keep unit 10 on the suite's fixtures.
  Order: 10 stays at 3, and 26 is at 4 because it adds arms to `check-wiring.test.sh` after 10 has moved it.
- **TOOL-dQuietDisk-17, F1 → (a)**: build S1 to S5 as written. It is the most feature-rich option, it is what the
  owner's prompt asked for, and P18 ranks the decision rule above the YAGNI practice in an unattended fork. State in
  §6 the saving the narrow reuse actually buys.
- **TOOL-dQuietDisk-19, F1 → (b)**: write `awaiting: fix4-nicocares-landed.md`, name the session and what it owes,
  and close. A records commit adds the nicocares readings when they land. **F2 → (a)**: the main loop takes the M1
  and M3 readings during RUNNING, in a detached scratch clone. Unit 19 moves from order 4 to order 5, after unit 26.

## 2. Author TOOL-dQuietDisk-26 — `check-wiring.sh` lists the tree once per invocation

Tier 2, order 4, chain area dWitnessedBar (Test).

`tools/check-wiring.sh` re-lists the graded tree once per check. The analysis measured 1,679 `ls-files`, 421
`check-attr`, 400 `config` and 186 `ls-tree` among the suite's 3,786 git processes: see
`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md` §2.

Read `check-wiring.sh` at `609cd40b1`. dWitnessedBar changed it, and units 26 and 27 there touched it.

The change:
- One `git ls-files -s`, and one batched `git check-attr --stdin` where attributes are read, per invocation.
- Every check reads that listing in-process.
- The findings are byte-identical, with the same rc, on the suite's arms and on the real tree.
- Count the git processes of one `check-wiring.sh` run over the real tree, and of the whole suite, before and after.

Unit 10 has moved the suite onto the template cache, and this unit adds no fixture machinery. A new arm that pins
the one-listing shape goes on a `New arm:` line.

Before you return:
- run `bash tools/unattended/unattended.sh --check-specs dQuietDisk TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-17 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26`;
- run `check-memory-hygiene.sh --only 12 --spec <path>` on each spec you touched;
- run `python tools/check-spec-tokens.py --spec <path>` on each spec you touched;
- fix every finding.

Return the specs you changed and their new revs.
