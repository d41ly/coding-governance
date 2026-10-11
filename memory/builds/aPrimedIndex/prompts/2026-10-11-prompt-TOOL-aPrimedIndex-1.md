# The owner's prompt, verbatim, and the brief this run was authorized with

**Serves:** research TOOL-aPrimedIndex-1 TOOL-aPrimedIndex-2 TOOL-aPrimedIndex-3 TOOL-aPrimedIndex-4

Handed to `/unattended` as the `--prompt` value on 2026-10-11, node `a`. The value carried whitespace
and named no readable file, so by the Skill's routing table it is the prompt itself and is taken
verbatim. It names no tracked id of this repo. No owner question was asked: acceptance and gates
derive from the prose and the code, and the brief rests on nothing said outside the prompt.

## The prompt

```text
One frequent case of gate bars failing and having to be restarted from scratch is generated indices not being regenerated prior to running the bars - sessions/agents wait for the bar results to regenerate them 100% of the time. Your task: ensure that regenerating every generated index (find all of them first - codebase map, gotchas, what else is there?) is ENFORCED before running any merge/landing bars.
```

## The brief

### Goal

No merge or landing bar starts over a stale generated output. Every output a bar leg grades for
freshness is found and declared once, one command regenerates them all, every bar refuses before
its first leg while one is stale, and the lander regenerates the ones its own merge leaves stale.

### Items

1. Find every generated index the bars grade: the codebase map, the gotchas index, and the rest [planned TOOL-aPrimedIndex-1]
2. Regenerating every one is enforced before any merge bar runs [planned TOOL-aPrimedIndex-2 TOOL-aPrimedIndex-3]
3. Regenerating every one is enforced before any landing bar runs [planned TOOL-aPrimedIndex-4]

### Acceptance

- Item 1: the runner's listing verb prints every declared output with its write and check
  commands, and every output a bar leg grades for freshness in this repo is on it. A declaration
  naming a generator that is absent is refused, observed on a staged break.
- Item 2: in a scratch clone, a staged stale output makes `bash tools/run-gates/run-gates.sh` exit
  2 before any leg line, naming that output and the regeneration command; after that command the
  same bar passes its preflight. A fresh tree prints one count line and runs its legs.
- Item 3: a lander merge that leaves an index stale yields a prepared merge whose tree the
  preflight reads as fresh, observed in a scratch clone.

### Gates

The merge bar, `bash tools/run-gates/run-gates.sh`, whose legs `tools/gate-legs.json` declares, run
once at the close. Each unit's direct check is named in its spec.

### Non-goals

- The bar never regenerates in place; it refuses and names the remedy.
- No leg changes what it checks; the preflight adds a refusal ahead of the legs.
- Not regenerated: ratchets (govkit's subject pins, the high-water files), minted kit-version
  carriers, node-local evidence (ceiling evidence, pooled self-test evidence, runlog records) and
  the kickoff manifest's audit stamp.
- No governance carrier is edited: the charter template, `AGENTS.md` prose, the runbook, the build
  method and the unattended protocol.

### Limitations

Node `a` is Windows with Git-Bash, and the host is heavily loaded (one python spawn measured 2.4 s).
Kit self-test suites stay held, and the owner runs them after landing. The bar runs once, at the
close. Every new shipped file obeys the install-prefix rule: it names nothing outside its kit by
literal.

### Reuse

The `[[generated]]` rows in `tools/memory-tree/kit.toml` and `tools/codebase-map/kit.toml`, which
`resolve_generated_indexes` in `tools/unattended/lib-unattended.sh` already reads. The
`[[regenerate]]` rows that govkit's `mint` runs. The lander's write-over-the-merge seam in
`tools/push-main.sh` (`run_minter`, then `commit-tree` with the merge's parents). The existing check
mode of every generator. Recall returned TOOL-aWindowedPass-4 (the `[[generated]]` declaration),
TOOL-aMendedFleet-65 (minting into the merge), and the class
`memory/gotchas/hand-named-gate-list-green-while-the-bar-reds.md`.

## Drawn from the session

none

## Owner confirmation

not asked — the brief draws on nothing outside the prompt
