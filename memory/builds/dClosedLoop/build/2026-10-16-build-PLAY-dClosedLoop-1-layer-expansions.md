# Layer review: the expansion layers, observability, integrations and distribution

The core's five layers are designed, reviewed and folded. This round designs the three expansions that
architecture v2 `[layers]` names. Each is researched twice, independently, and the design rests on what
both runs of a layer agree on.

## [words] The owner's words, 2026-10-16

> let's move on to the expansion layers - launch a concurrent set of research agents each targeting
> their own expansion layer design given their fit into the new architectural design. Run each of
> them twice at medium effort. Then, base your own design against what the agents agree on.

## [scope] What this round designs

- **The three expansions**, as v2 `[layers]` defines them:
  - `observability`: signals about the loop and the runtime, and the cadence steps that act on them,
    Maintain and the Loop Review;
  - `integrations`: adapters to outside services: remote CI, notifications, cloud hosts, trackers,
    and deploy engines that promote a landed tree through environments;
  - `distribution`: the product's delivery: govkit, the adopt scripts, overlays, the install of the
    render targets Runtime's harness adapters define, and currency.
- **What each fills.** Each fills the layer contract P28 names, attaches only at extension points a
  core layer declares, and leaves the core whole when it is absent, its optional slots rendering the
  core's fallback.
- **What the core rounds left to this one:**
  - Maintain and the Loop Review as items: a detector register by layer, intakes rendered from keyed
    readings, event runs keyed by event, and a declared home for each report (flow-steps
    `[expansions]`);
  - Deploy's extensions: kit versions and release notes from distribution, and promotion through
    environments with a verify per SHA from integrations (flow-steps `[expansions]`);
  - `runtime.journal`, left open because the run record is observability's (layer-runtime
    `[policies]`).
- **The method.** One handoff per layer, run twice from identical text by `gov-researcher` at medium
  effort, as the owner asked. Where a layer's two returns agree, the design takes it. Where they
  split, the split is measured or put to the owner as a fork.

## [research] Dispatched, 2026-10-16

| Dispatch | Layer | Run | Handoff | Returned |
|---|---|---|---|---|
| 51 | observability | A | `prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-19-researcher.md` | pending |
| 52 | observability | B | the same | pending |
| 53 | integrations | A | `prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-20-researcher.md` | pending |
| 54 | integrations | B | the same | pending |
| 55 | distribution | A | `prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-21-researcher.md` | pending |
| 56 | distribution | B | the same | waits for a spawn slot |

- **Why the sixth run waits.** The agent-cap hook gives a prompt five direct spawns. A slot frees 45
  minutes after its claim (`tools/hooks/agent-cap.js`, the slot ledger). Dispatches 51 to 55 claimed
  all five at 16:43 +03:00, so dispatch 56 starts once the first slot frees. No more than five run at
  once.
- **What every handoff hands over.** The same settled facts: the layer table, P28 and the layer
  contract, the optional slot, the item and record rules, and Runtime's nine extension points. Each
  layer's part adds that layer's settled decisions, its policy keys and the register's gaps it
  touches. The design records each run may read are named in its part.
- **The return shape**, the same for all six: verdict, today, attach points, candidates with their
  losing tests, the contract filled, items and policies, gaps, and forks.
