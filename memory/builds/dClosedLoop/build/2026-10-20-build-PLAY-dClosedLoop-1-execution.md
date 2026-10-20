# Execution: the chain built under today's gov, across nodes a, b and d

**Serves:** research PLAY-dClosedLoop-1

After the baseline, the owner asked how the chain is executed. This record holds the owner's words, the research
that answers them, and, once the owner has walked it, the plan. Nothing here opens the chain or starts a node's
work: the baseline's stop holds until the owner approves a plan (`whole-audit.md` `[baseline]`).

## [question]

The owner, 2026-10-20, verbatim:

> Our plan: this entire design is going to be built under the current GOV, by the current /unattended driver. Since
> the build is very large, I want to distribute both the speccing and building across nodes a, b and d. And specs
> still need to be strictly compared against any deviations from the design. I need fully-oriented handoffs,
> coordination and per-node task distribution steps. How do we execute this?

## [research]

Five researchers took one facet each, at the owner's medium effort, read-only, each with its own scratch folder and
no model or network calls. Each return is saved verbatim beside this record as it lands.

| Facet | Dispatch | Handoff | Return |
|---|---|---|---|
| The unattended driver, end to end | 214 | `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-51-researcher.md` | `build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-driver.md` |
| Coordination across nodes a, b and d | 215 | `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-52-researcher.md` | `build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-coordination.md` |
| Fully oriented handoffs | 216 | `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-53-researcher.md` | `build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-handoffs.md` |
| Per-node task distribution | 217 | `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-54-researcher.md` | `build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-schedule.md` |
| Specs held to the design, strictly | 218 | `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-55-researcher.md` | `build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-deviation.md` |

Every probe script the five left in their scratch folders is kept verbatim in
`build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-instruments.md`, so each table can be re-run. That record's
`[verified]` holds the main loop's two checks of claims the returns left open. First, a spec whose design pin is
stale passes today's spec-tokens leg, seen red on a control first, while the bootstrap `carries.py` reds it. Second,
a README the owner landed on main resolves at the default-branch anchor, where a `slug` run reads `spec-audit:` and
`may:`; that was read in the driver, not run.
