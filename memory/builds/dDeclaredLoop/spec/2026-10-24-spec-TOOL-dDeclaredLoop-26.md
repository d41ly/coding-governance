# TOOL-dDeclaredLoop-26 — a build's composition pinned per step, its position read at the pin, and the move at the next step boundary

**Status:** CLOSED · rev-6 · 2026-11-16 · node d · Tier-2 · base ed497191 · streams tooling · order 23 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0111@313dbc9c whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-build-TOOL-dDeclaredLoop-26-deviation-261.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-26-deviation-261.md) | deviation | — |
| [2026-10-25-build-TOOL-dDeclaredLoop-26-deviation-262.md](../build/2026-10-25-build-TOOL-dDeclaredLoop-26-deviation-262.md) | deviation | — |
| [2026-11-05-build-TOOL-dDeclaredLoop-26-deviation-263.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-26-deviation-263.md) | deviation | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-26-deviation-264.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-26-deviation-264.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-26-1-acceptance-ledger.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-26-1-acceptance-ledger.md) | journal | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-26-1-builder-return.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-26-1-builder-return.md) | journal | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-26-deviation-265.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-26-deviation-265.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-26-deviation-266.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-26-deviation-266.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-56 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-26-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-26-1-spec-writer.md) | journal | — |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-3-owner-forks.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-3-owner-forks.md) | research | TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-56 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade.md) | research | TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-26-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-26-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-26-reground-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-26-reground-brief.md) | research | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-26-2-spec-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-26-2-spec-brief.md) | research | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-26-3-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-26-3-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-26-build-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-26-build-brief.md) | journal | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

A build runs each step under the composition it entered that step with, and moves to a newer one only
at its next step boundary, so an update or an overlay change landing mid-step never changes what the
build is doing (the owner's FA-7, "Next step boundary (Recommended)",
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md:376`).
Today nothing pins a build to a composition: `tools/loop/position.py#derive_position_into` reads the
item composition at `HEAD` through `tools/loop/loop_items.py#read_composed_items`, the composition's
rows where `read_composition` answers 0 and gov's own rows where it answers 2, unarmed, so a build
always reads the landed tip (`memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md:33`).

## 2. Scope (IN)

- **S1** — The composition revision (I17): the commit `HEAD` names at the moment of a move, recorded as
  its first eight hex digits. It is dOrderedCharter-46 S1's landed revision, the node's own last
  commit, not a remote ref. At it the overlay is the blob `tools/playbook/overlay.py#read_overlay` reads
  at `HEAD`, gov's item rows are the blob of the item namespace's `source` that
  `tools/playbook/overlay_rows.py#read_kind_source` reads at `HEAD`, and the policy values the
  composition reads are read at `HEAD` (`tools/playbook/overlay_rows.py#derive_kind_composition`).
  `derive_composition_revision(root)`, in the new module `tools/loop/composition.py`, answers it
  through `tools/loop/loop_witness.py#resolve_commit` over `HEAD`, ValueError where `HEAD` names no
  commit. Observed by AC2 and AC5.
- **S2** — The pin. `composition` joins `tools/loop/loop_transition.py#TRANSITION_FIELDS` after
  `stand-in`, so every move `tools/loop/loop_transition.py#write_transition` records carries
  ` · composition=<sha8>` on its trailer and a `Composition` field on its log record, read back through
  `tools/loop/loop_transition.py#read_transitions`. The writer sets the value from S1 itself; a
  `--field composition=<value>` is refused, exit 2, naming the field as derived. Observed by AC5.
- **S3** — The read at the pin. `read_step_composition(root, moves)` takes a build's moves, newest
  first as `read_transitions` returns them, and answers `(the commit, state)`: the newest move's
  `composition` resolved to its commit, state `pinned`. `read_composition_at(root, rev)` answers what
  `read_composition` answers, composed at `rev`: in place where `rev` is `HEAD`'s commit, and otherwise
  in a scratch worktree detached at `rev`, so every read the `compose --kind item` verb makes at `HEAD`
  reads the pin (§8 F4) while the code that runs is this tree's. `read_composed_items(root, rev=None)`
  takes the revision: where one is given it reads the triple through `read_composition_at(root, rev)`
  in place of `read_composition(root)`, and maps it as today, rows on 0, gov's own rows on 2, ValueError
  on 1, so the mapping keeps its one owner (§8 F9). `derive_position_into` reads the build's moves first
  and its items through `read_composed_items(repo, <read_step_composition's commit>)`, never at the tip,
  and appends `composition@<sha8> · <state>` to the position's reads. Observed by AC1.
- **S4** — The carry. A witness the build holds under an item tag its moves name carries to that
  tag's successor when the tag is absent from the composition at the pin and a change record ended it
  with exactly one successor that the composition holds. `derive_carried_witnesses(root, named, tags)`
  answers the position's named witnesses with each carried entry added under its successor, and
  `derive_position_into` reads its named witnesses through it. A successor is read through
  dOrderedCharter-19's one tag resolver, `tools/playbook/gov_tag.py`'s `show <tag> --json`, run as a
  subprocess: the copy under the repository being read, found by `resolve_kit_dir` with the playbook
  home, the anchor `gov_tag.py` and the loop kit's folder under `root`, that folder the parent of the
  tree-relative path `tools/loop/loop_items.py#derive_definition_rel` answers. A copy found beside
  `composition.py` would read this tree's tag index whatever its working directory, since
  `tools/playbook/gov_tag.py#resolve_repo_root` reads `rev-parse --show-toplevel` from the script's own
  folder. The resolver answers the `Successor` line for a tag no live row defines, extracted from the
  change records by the playbook kit; this kit parses no change record.
  `read_tag_successors(root, tag)` answers the list, `[]` for an ending with none, or None where no
  record ended the tag. Observed by AC2.
- **S5** — An item ending under a build. At a move whose previous move was pinned at another commit,
  `write_ended_orders(root, build, moves)` composes at `HEAD`, the new pin, and for each item tag the
  build's moves name that the composition lacks and that no single held successor carries (ended with
  none, or split), files one `item-ended` order naming the build, the item, both revisions and the
  successors read (§8 F6, F7). `write_transition` calls it after the move is answered and before any
  record is written, and `record` prints one `loop: order · <path>` line per order. Where that
  composition does not answer 0 the move files nothing, prints `loop: composition · unread · <why>`,
  and still records. Observed by AC4.
- **S6** — Policy values naming a renamed boundary. `read_tag_policy(key, root, build)` reads a
  tag-valued key at the build's pin through the policy kit's `resolve`, found by
  `tools/loop/loop_parents.py#read_policy_kit`, and answers each member redirected as S4 redirects a
  witness: a member absent from the composition at the pin with one held successor reads as that
  successor, so a value naming the old boundary acts on the new one from the boundary the build moved
  at. Each redirected member files one `policy-renamed` order naming the key, the old tag and the
  successor, for the owner to re-pin the guarded file (§8 F8). Observed by AC3.
- **S7** — A record with no pin. A move recorded before this unit carries no `composition`;
  `read_step_composition` then answers `HEAD`'s commit with the state `unpinned`, as it does for a
  build with no move, and the build's next move pins. A move whose previous move is unpinned files no
  order. Observed by AC6.
- **S8** — The fixture: `python <prefix>/loop/composition.py --fixture --plant <case>` runs one plant
  over a scratch repository built by `tools/loop/loop_items.py#build_scratch_tree`, and `--selftest`
  runs every plant through `tools/loop/loop_lib.py#run_selftest_cases`, one scratch base shared and
  reset per plant. The plants are `rename`, `ended`, `split`, `policy-rename` and `unpinned`. The leg
  `loop composition fixtures` in `tools/gate-legs.json`, argv `python {prefix}/loop/composition.py
  --selftest`, chunk `selftests`, subject `kit`, carries `enforces = ["principle.p8"]`, and is gov's own
  `[[exempt_leg]]` in `tools/govkit/registry.toml`, as every loop fixture leg is. P8's text in the
  design names a build's composition "pinned per step"
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:885-886`),
  and `tools/playbook/core-pending.txt` holds the row `principle principle.p8 dOrderedCharter`, which
  this pass deletes, as the meta-check reds it stale once the leg enforces the tag. Observed by AC1 to
  AC6 and AC8.
  **Readers:** by name: `tools/playbook/core-pending.txt` spells `principle.p8` in the row this pass deletes
  · by value: NO VALUE READERS — a pending row's value is its arming build, which the meta-check verb of `tools/playbook/core.py` prints only in its pending count.
- **S9** — The page `help/loop.md` gains a section on the pin after "Recording a build's move": a build
  runs each step under the composition it entered it with and moves at the next step boundary, the
  `composition` field, what an ended item and a renamed boundary file, the position's
  `composition@` read, and the fixture command with its usage anchor. The `trailer` bullet of
  "Recording a build's move" names `composition=<sha8>` beside `stand-in=<owner>`. Observed by AC7.

## 3. Non-goals (OUT)

- No composition mechanism: the overlay's rows, their composition and its landed revision are
  dOrderedCharter-35's, -32's and -46's and the item kind's TOOL-dDeclaredLoop-24, called through the
  `compose --kind item` verb, never re-specced. No revision argument is added to them: a pin is read by
  making `HEAD` the pin (§8 F4).
- No other kind composed at a pin: `read_composition_at` composes the item kind, the one the position
  engine reads. A later unit composing another kind at a pin passes it through
  `read_composition`'s kind argument, which TOOL-dDeclaredLoop-25 adds.
- No pin for `--check-refusal` of `tools/loop/position.py`: it names a tag and a key and no build, so it
  reads the composition at `HEAD` as today.
- No pin on the definition's steps and transition tables, which `tools/loop/loop_lib.py#read_definition`
  reads from the kit's own file: they are no registered kind.
- No scenario and no recorded change in the revision: the scenarios a build was placed under are
  TOOL-dDeclaredLoop-27's field on the same record, and its own recorded changes TOOL-dDeclaredLoop-28's.
- No write to `.governance/policy.toml`. The redirect is read-side and the order asks the owner to
  re-pin, since the file is guarded owner-only (dGroundRules-6).
- No position engine: the derivation is TOOL-dDeclaredLoop-7's, which this unit points at a pinned
  revision.
- No caller of the writer: `help/loop.md` states nothing calls `record` until the executor that moves a
  build at each item boundary lands, and this unit adds none.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-3` — `Gov-Transition`, the transition record into a step whose `composition` field this unit fills; without its writer there is nothing to pin on
- **consumes-from** `TOOL-dDeclaredLoop-7` — `position`, the engine this unit points at the pinned revision; without it nothing derives a position from the pin
- **hands-off** `TOOL-dDeclaredLoop-27` — composition revision, the value S1 derives and S3 reads, beside which the scenario field is pinned; the reader is `read_composition_at`, since the lexicon declares no `compose` verb
- **hands-off** `TOOL-dDeclaredLoop-19` — `read_tag_policy`, through which `review.breakpoints` is read so a renamed boundary keeps its breakpoint
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 9, 39, each a scope item of that unit

## 4. Design

### Data model

The value every move's trailer and log record carries after `stand-in`, where present:

```
composition = 3f9c2a71        # the HEAD commit the move was recorded at, its first eight hex digits
```

The read at the pin, in order:

1. the build's moves through `read_transitions(build, repo)`, newest first;
2. the newest move's `composition`, resolved to its commit by `resolve_commit`: state `pinned`; no
   move, or none on the newest, `HEAD`'s commit with state `unpinned`; a value naming no commit is a
   ValueError naming the move's commit;
3. `read_composition_at(root, rev)`: where `rev` is `HEAD`'s commit, `read_composition(root)`. Otherwise
   `git worktree add --detach <scratch> <rev>` under a fresh `tempfile.mkdtemp` directory, then
   `read_composition(<scratch>)`, so the `compose --kind item` verb this tree resolves runs with the
   pin as `HEAD`: its overlay, its namespace source, its policy file and its change records. Then
   `git worktree remove --force <scratch>` runs in a `finally`, so a refusal leaves no worktree.
   `read_composition` runs the verb with the scratch as its working directory, and
   `tools/playbook/overlay_rows.py#run_compose` composes over `pathlib.Path.cwd()`, so the verb found in this
   tree reads the scratch's tree;
4. `read_composed_items(root, rev)` maps that triple as it maps `read_composition`'s, importing
   `read_composition_at` inside the function, since `composition.py` imports `loop_items`; it is the
   read position makes.

### The carry and the orders

One rule serves S4, S5 and S6. A tag absent from the composition at a pin is redirected when
`read_tag_successors` answers exactly one successor and that successor is in the same composition;
otherwise it is not redirected. `read_tag_successors` runs `gov_tag.py show <tag> --json`, the copy S4
finds under `root`, with `root` as its working directory and the git leaks unset
(`tools/loop/loop_witness.py#read_clean_env`):
exit 1, no row, answers None; exit 0 answers the `Successor` line of its `retired` rows, comma-split,
`none` as `[]`, and None where every row is live; exit 2, or the playbook kit unresolved, is a
LookupError naming the resolver.

At a move, in order:

1. `derive_move` answers the move and the witness resolves, as today;
2. `read_step_composition(root, read_transitions(build, root))` gives the previous pin; where it is
   `pinned` at another commit than `HEAD`'s, `write_ended_orders` composes at `HEAD` and files one
   `item-ended` order per held tag the composition lacks and the rule does not redirect;
3. the move's fields take `composition`, the first eight hex digits of `derive_composition_revision`;
4. the back-fill, the record and the commit, as today.

An order is one file, `.governance/outbox/loop-<kind>-<slug>.md`, written by `write_loop_order(root,
kind, slug, text)` as UTF-8 with LF line ends. `<slug>` is `<build>-<tag>` for `item-ended` and
`<key>-<tag>` for `policy-renamed`, both already inside the tag grammar, so a retried boundary or a
repeated read rewrites the same file and files nothing twice.

### Inventory

| Minted | Kind |
|---|---|
| `derive_composition_revision`, `read_step_composition`, `read_composition_at`, `read_tag_successors`, `derive_carried_witnesses`, `write_ended_orders`, `read_tag_policy`, `write_loop_order` | functions, `tools/loop/composition.py` |
| `composition` | transition record field (I8) |
| `item-ended`, `policy-renamed` | order kinds, `loop-<kind>-<slug>.md` under the outbox |
| `pinned`, `unpinned` | the read states of a step's pin |
| `loop composition fixtures` | gate leg |

Each function name was put to `lexicon.py --suggest <name> --as py.function` on 2026-11-15 and leads
with a declared verb. The rev-4 name `compose_at` was refused there, its verb undeclared.

### The plants

The scratch base is `build_scratch_tree`'s, plus the build `tFix`: a README whose front matter
`parse_front_matter` reads, one spec `TOOL-tFix-1`, and a `.memory-tree.conf` naming the `TOOL`
family, so the writer has an anchor. The base's branch is renamed `main`, one `branch -M main` through
`run_fixture_git`. `build_scratch_tree`'s `init` takes the host's default branch name and the scratch
has no remote, so the policy kit's landed revision (`tools/policy/policy.py#derive_landed_revision`)
falls back to `refs/heads/main` and refuses where that names no commit. The builder's probe saw the
scratch's resolver refuse that read until the branch was named `main`, and then answer its `retired`
row. `GOV_DEFAULT_BRANCH` was not probed, and an environment value would have to reach every
subprocess the plant starts, where the rename is one call that `build_scratch_tree` and its other
callers never see.

Each plant records two moves through the writer, which commits each move on `HEAD`
(`tools/loop/loop_transition.py#write_transition`). The first, `planning -> designing` on
`item.plan.exit`, is recorded at the base commit and commits C1. The second, `designing -> planning`
on `item.design.decompose` (outcome `goal-fork`), is recorded at C1, so its `composition` is C1's
sha8, the pin AC1 reads, and it commits its own commit on C1; the build now holds a witness under
`item.design.decompose`. The plant then commits C2 on that commit, where the scratch definition's
`item.design.decompose` is re-tagged `item.design.regroup` throughout, with one change record through
the memory-tree kit's `write_change`:

| Plant | C2's change record | Owed |
|---|---|---|
| `rename` | rename, successor `item.design.regroup` | AC1, AC2, AC5 |
| `ended` | remove, successor none | AC4 |
| `split` | split, successors `item.design.regroup` and `item.design.regroup-b` | AC4 |
| `policy-rename` | rename, as `rename`; the base's `.governance/policy.toml` sets `review.breakpoints` to `item.design.decompose` | AC3 |
| `unpinned` | none; the build's one move is a hand-written trailer with no `composition`, in place of the two recorded moves | AC6 |

Each plant then records `planning -> designing` on `item.plan.exit` at C2 where it owes it, prints
each observation, and closes with `loop: fixture · <plant> · held` or `· MISSED <why>`.

### Migration

Builds in flight at landing carry moves with no `composition`; S7 reads them at the tip, and the first
move each records pins it. No record is rewritten.

### Rollout

Live at landing: the pin only narrows what a mid-step reader sees, and no caller records a move yet.

### Files touched (estimate)

- `tools/loop/composition.py` (new)
- `tools/loop/loop_transition.py`: `composition` in `TRANSITION_FIELDS`, the derived value and the
  `--field` refusal, `write_ended_orders` called before the records, the order lines, the `field` plant
- `tools/loop/position.py`: the moves read first, the items through `read_composed_items` at the pin,
  the named witnesses through `derive_carried_witnesses`, the `composition@` read, its docstring
- `tools/loop/loop_items.py`: `read_composed_items` takes `rev=None`, read through `read_composition_at`
  where given (§8 F9), its docstring and the module docstring's sentence on it
- `tools/loop/README.md`: a section on `composition.py` and its commands, and "The position engine"
  naming the pin and `read_composed_items`
- `tools/loop/kit.toml`: one comment paragraph on the module's reach
- `tools/gate-legs.json`: the leg `loop composition fixtures`
- `tools/govkit/registry.toml`: its `[[exempt_leg]]` row
- `tools/govkit/usage.toml`: the `script:{prefix}/loop/composition.py` row
- `tools/govkit/subject-pins.tsv`: regenerated, one row
- `tools/run-gates/selftest-budgets.txt`: the leg's row
- `tools/playbook/core-pending.txt`: the `principle.p8` row
- `help/loop.md`: the section of S9
- `memory/guides/SESSION-KICKOFF.md`: the audit block restamped
- `memory/map/features/loop.md`: `loop composition fixtures` in its `[claims]` `gate-legs` list
- `memory/map/generated/symbols.json`, `memory/map/generated/MAP.md`,
  `memory/map/generated/CARDS.md` and `memory/map/generated/inventories.json`: regenerated, §5
  registry and pins

### Alternatives rejected

- **A digest over the composed rows as the revision.** It names the composition but cannot be read
  back: the position engine needs the rows, and a digest gives no commit to read them from.
- **Moving at once.** FA-7's second option; the owner took the next step boundary.
- **Never moving until landing.** FA-7's third option; a build would run a composition gov has since
  fixed for its whole life.
- **Rewriting the policy file at the boundary.** An agent write to a guarded owner-only file, which
  dGroundRules-6 refuses and veto 3 discards.
- **Reading change records here.** The memory-tree kit's `read_changes` is in reach under the kit's one
  edge, but the redirect rule, the last record naming a tag, lives in the playbook kit's
  `derive_status` and the tag index's `retired` rows; a copy here would be a second owner of it, and
  moving it into `tools/memory-tree/build_records.py` changes a verdict-epoch delegate.

## 5. Production-readiness checklist

- security — the only writes are the move's records, as today, and order files under the outbox
  through one writer, each name built from values inside the tag and key grammars; the policy file is
  read only. A scratch worktree is created under the host temp directory and removed in a `finally`.
- perf / scale — the writer composes once at `HEAD` per move whose previous move was pinned elsewhere,
  and resolves a tag only where the composition lacks it. A position read at a pin other than `HEAD`
  checks out one scratch worktree, whose cost grows with the tree and was not measured; until the
  executor lands no build in this tree carries a pin, so every position read here stays in place.
- error / empty / loading states — no move, or a move with no pin, reads `unpinned` at the tip and
  says so in the position's reads; a pin naming no commit is a ValueError naming the move, which the
  engine answers `invalid-input`; a composition that does not answer at a move files no order and says
  `unread`; a resolver that does not answer is a LookupError the writer answers exit 2 `unanswered`.
- observability — every order prints its path, every position prints the pin it read and its state.
- risks — what this change could newly red, and what keeps each green:
  - `loop transition record`: every plant's trailer and record gain ` · composition=<sha8>` after
    `stand-in`; each case's needle is a substring the longer trailer still holds. The `field` plant
    registers no field in process any more, since `composition` is registered: it runs the
    `colour=red` move (refused as before), the `composition=3f9c2a71` move (refused as derived, a new
    case), then the plain move, whose trailer and read cases hold ` · composition=`. The plants with
    more than one move compose in a scratch that holds no playbook kit; the compose does not answer 0
    there, so each prints `loop: composition · unread` and records as before.
  - `loop guard fixtures`: `run_floor_readers` in `tools/loop/guard.py` records one move, unpinned, so
    nothing composes and the record it deletes is read as before.
  - `loop position fixtures`: every plant but `plan-line` and `status-line` passes a parsed definition,
    which this unit does not pin, and every move a plant writes is a hand-written trailer with no
    `composition` (`write_position_plant`'s `write_move`), so each composition read is `unpinned`, in
    place, as today, and adds one `read —` entry, while `check_plant` asks only that some read open
    `memory/`.
  - `loop item kind`: `read_composition` and `build_scratch_tree` are called, never changed;
    `read_composed_items` gains a parameter defaulting to None, under which it reads as today.
  - `loop upstream fixtures`: `tools/loop/upstream.py` calls `read_composed_items(root)` with no
    revision, and `print_check_refusal` in `tools/loop/position.py` does the same, so both read
    `read_composition` at `HEAD` as before.
  - `codebase-map gate coverage`: the map's inventories read every leg name in `tools/gate-legs.json`,
    so the new leg is claimed in `memory/map/features/loop.md`'s `gate-legs` list in the same commit.
  - `codebase-map coverage + freshness`: `symbols.json` indexes Python functions, so the eight new
    functions and `read_composed_items`' signature stale it until `gen_map.py --write` regenerates the
    four generated files in the same commit.
  - `core meta-check`: the leg enforces `principle.p8` and its pending row goes in the same commit.
  - `help page commands`: the new usage row's anchor, its fingerprint printed by
    `python tools/govkit/docs_leg.py --fingerprints`, sits on the S9 section's fixture line; the
    `record` row's flags do not move, so its anchor holds.
  - `install-prefix (shipped surface)`: the module ships under the kit's `**` include, so its
    docstring names itself and its siblings by file name or `<prefix>`, never a kit path.
  - `encoding posture (text IO names its encoding)`: `write_loop_order` names UTF-8.
  - `python reads (a name never bound, an import outside its guard)`: `write_transition` imports
    `composition` inside the function, since `composition.py` imports `loop_transition`, and
    `read_composed_items` does the same, since `composition.py` imports `loop_items`.
  - `lexicon naming predicates`: the eight functions of §4 Inventory each lead with a declared verb, so
    the offender count stays at `VERB_OFFENDER_PIN`, 1209 PINNED at `.lexicon.conf` on the branch
    `dac974418eab`.
  - the shared records: the pass writes neither `memory/DECISIONS.md` nor
    `memory/project/readme-contract.txt`, the `SHARED_RECORDS` of `.unattended.conf`, and owes no
    decision row, since no ceiling moves.
  - the guarded legs the touched files trip, `govkit selftest`, `govkit refusal join` and
    `govkit acceptance matrix` on `tools/govkit/registry.toml`, `policy fixtures` on `tools/gate-legs.json`,
    `playbook render selftest` on `tools/playbook/core-pending.txt`, and `recall floor` and
    `recall floor arms` on the kickoff manifest and the registry: this unit changes none of their code,
    and changes those files only by the rows and the audit line named in this section.
  - refusal ceilings and families: the population `tools/memory-tree/check-arms.py` reads is every
    tracked shell gate defining the `fail` helper; this unit writes Python, so no census, ceiling,
    `ARMS_FLOORS` pair or `.families.txt` family moves.
- dependency — order 23. Units 3, 7 and 24 are CLOSED and this spec is read on their landed code.
  TOOL-dDeclaredLoop-25 (order 21) gives `read_composition` a kind argument defaulting to `item`, read on
  its committed spec at rev-5; this unit calls it with none. TOOL-dDeclaredLoop-45 (order 18, in
  progress) changes `derive_unit_step` in `tools/loop/position.py`, not the composition read this unit
  moves; this pass starts from its landed bytes. Units 4, 6 and 25 add rows to the same registry,
  usage, pin, budget and pending files; each row is its own line. Unit 69 changes
  `tools/loop/guard.py`, whose `run_floor_readers` this unit reads and does not edit.
- registry and pins — one leg, so one `[[exempt_leg]]` row, one usage row, one `subject-pins.tsv` row
  regenerated by `python tools/govkit/govkit.py selfcheck --write`, and one `selftest-budgets.txt` row,
  a PINNED proxy from the builder's direct-CLI readings of the five plants until the main loop's first
  reading of the leg alone re-prices it. The leg's `ceiling` is 300, PINNED, the value
  `loop position fixtures` and `loop item kind` carry. The kickoff manifest watches `tools/gate-legs.json`, so the audit block of
  `memory/guides/SESSION-KICKOFF.md` is restamped with a `manifest-audit:` delta line. The verdict-epoch
  gate's delegate list holds memory-tree modules and the spec-token checker, no file of this unit, so it
  does not move. The loop dossier `memory/map/features/loop.md` claims the leg in its `gate-legs` list,
  and `python tools/codebase-map/gen_map.py --write` regenerates `symbols.json`, `MAP.md`, `CARDS.md`
  and `inventories.json` under `memory/map/generated/`. `tools/loop/README.md` gains the module's
  section, as every loop module has one. The kit versions are minted by the lander.
- testing — the five plants of §4 The plants, and the `field` plant's new case.
- migration — as §4 says.
- user docs — `help/loop.md` gains the pin's section and the trailer paragraph names the field;
  `tools/loop/README.md` gains the module's section.

## 6. Acceptance criteria

- **AC1** — When `python composition.py --fixture --plant rename` reads the build after C2 lands and
  before its next move, `read_step_composition` answers C1's commit `pinned`, C1 being the first move's
  commit and the one the second move was recorded at (§4 The plants),
  `read_composition_at` at it holds `item.design.decompose` and not `item.design.regroup`, and the
  position `derive_position` derives over the plant lists `composition@<C1's sha8> · pinned` among its
  reads.
  Red when: the engine reads the tip, so its read names C2 and its items hold `item.design.regroup`
  mid-step.
- **AC2** — When the same plant records `planning -> designing` at C2, that move's `composition` is
  C2's sha8, and `derive_carried_witnesses` over the build's moves and the composition at C2 holds the
  witness of `item.design.decompose` under `item.design.regroup`.
  Red when: the witness is keyed by the old tag only, so the re-tagged item reads unwitnessed after
  the move.
- **AC3** — When `python composition.py --fixture --plant policy-rename` reads `review.breakpoints`
  through `read_tag_policy`, it answers `item.design.decompose` before the move at C2 and
  `item.design.regroup` after it, and after it one order file whose name opens
  `loop-policy-renamed-review.breakpoints-` sits in the scratch's outbox folder.
  Red when: the value is read raw, so the breakpoint names a tag no item carries and never fires.
- **AC4** — When `python composition.py --fixture --plant ended` and then `--plant split` record the
  move at C2, each files one order whose name opens `loop-item-ended-tFix-item.design.decompose`, and
  `derive_carried_witnesses` carries no witness to `item.design.regroup`.
  Red when: a split redirects to its first successor, so a witness carries to an item it never
  witnessed.
- **AC5** — When the `rename` plant reads the move it recorded at C2 from its trailer and from its log
  record, each carries `composition` with the same value, the first eight hex digits
  `derive_composition_revision` answered.
  Red when: the field is written to one channel only, so `loop_transition.py check` holds the record to
  a trailer that names no pin.
- **AC6** — When `python composition.py --fixture --plant unpinned` reads a build whose one move
  carries no `composition`, `read_step_composition` answers `HEAD`'s commit `unpinned`, and the build's
  next move carries a `composition` and files no order.
  Red when: a move with no pin refuses, so every build in flight at landing stops.
- **AC7** — When `grep -n "next step boundary" help/loop.md` runs at this unit's commit, it finds the
  section naming the `composition` field, `item-ended` and `policy-renamed`.
  Red when: the pin ships and the page still says nothing of when a build moves to a newer
  composition.
- **AC8** — When `python -m json.tool tools/gate-legs.json` is read, the row named
  `loop composition fixtures` carries `enforces` holding `principle.p8`, and
  `python tools/playbook/core.py meta-check` exits 0, naming neither that leg nor a stale pending row.
  Red when: the leg carries no `enforces`, or the pending row stays, either of which the meta-check
  reds.

## 7. Gates

`loop transition record` · `loop position fixtures` · `loop guard fixtures` · `loop item kind` · `loop upstream fixtures` · `codebase-map gate coverage` · `codebase-map coverage + freshness` · `core meta-check` · `help page commands` · `lexicon naming predicates` · `python reads (a name never bound, an import outside its guard)` · `encoding posture (text IO names its encoding)` · `install-prefix (shipped surface)` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `playbook render selftest` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/composition.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · the `loop composition fixtures` leg's plants, its failing case staged by `rename` with the position engine reading the tip · none
New arm: tools/loop/loop_transition.py · covers none · the `field` plant's `composition=3f9c2a71` move, its failing case staged by accepting the field as given · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a
  legal status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`. Observation,
  2026-10-24: `DRAFT` is not in the tuple, so a `DRAFT` header parses as no header. Liveness: the
  tuple would list it if the vocabulary admitted it. RESOLVED (agent, 2026-10-24, delegated): `OPEN`.
- **F2 — What is a composition revision?** Options: (a) the landed commit the composition is read
  from; (b) a digest over the composed rows; (c) the overlay's blob alone. I17 names the overlay's
  landed revision plus gov's pack revisions, which one commit holds both of; (b) cannot be read back
  and (c) misses gov's packs. RESOLVED (agent, 2026-10-24, delegated): (a), by rung 3.
  widens: none · relaxes: none
- **F3 — How is a policy value naming a renamed boundary re-pointed?** Options: (a) a read-side
  redirect plus an order to the owner; (b) a write of the new value into the policy file; (c) the
  redirect alone. (b) is an agent write to a guarded file, discarded by veto 3; (c) leaves the file
  naming a dead tag for ever. RESOLVED (agent, 2026-10-24, delegated): (a), by rung 3.
  widens: none · relaxes: none
- **F4 — How is a composition read at a pin other than `HEAD`?** dOrderedCharter-46 S1 makes the
  overlay's landed revision `HEAD`, and its S6 has every `policy.py get` the composition makes pass
  `--rev HEAD`. Unit 35 S5 reads `instructions.exclude` that way, and unit 36 S4 the tag-valued keys.
  Unit 46 §3 adds no other revision, since "no caller needs one". Composing from a pin's blobs
  therefore mixes the pin's rows with `HEAD`'s policy values, the split unit 46 AC5 reds. Options: (a) `compose_at`
  composes in a scratch worktree detached at the pin, so every `--rev HEAD` read reads the pin and the
  parents are used as specced; (b) an ask to dOrderedCharter for a `rev` threaded through
  `compose_rows`, `check_rows` and unit 46 S6, with a `--rev` on every reader-command population.
  (a) costs one worktree checkout per compose at an older pin, and a reader-command population runs
  the pin's own code; a pin naming a commit the repository no longer holds is refused. (b) reverses a
  parent's stated non-goal for one caller. Specs 27, 28 and 33 compose through `compose_at` and point
  here. RESOLVED (agent, 2026-10-25, delegated): (a), rung 1, dOrderedCharter-46 S1, S6 and §3.
  widens: none · relaxes: none
- **F5 — How does the loop kit reach `compose_rows`, the playbook kit's function?** A kit imports no
  sibling kit (TOOL-dGroundRules-1 §4), and dOrderedCharter-11 S4, -19 S8 and -33 S3 each run the
  sibling's verb as a subprocess found through an inline `resolve_kit_dir`. dOrderedCharter-35 gives
  `compose_rows` no verb: it is a function whose callers import it inside the playbook kit. The same
  holds for every loop-kit caller, specs 24, 25, 27, 28 and 33. Options: (a) an ask to
  dOrderedCharter for a `compose` verb on `tools/playbook/overlay_rows.py` printing `compose_rows`'
  five returns for each registered kind as JSON, run as a subprocess in the worktree F4 makes; (b) a
  declared import row on `tools/loop/kit.toml` naming playbook, in the shape of
  `tools/memory-tree/kit.toml:8`'s `requires_if` rows, with its reason. (b) is the rule's precedent
  exception, but it keeps the loop kit bound to the playbook module's names. Recommendation: (a), since
  F4 already runs one process per pin. RESOLVED (owner, 2026-11-05): (a) the `compose` verb ask. The
  build run files in dOrderedCharter's `BACKLOG.md` the ask for "a `compose` verb on
  `tools/playbook/overlay_rows.py` printing `compose_rows`' five returns for each registered kind as
  JSON".
- **F6 — Where does the loop kit file an order?** The rev-4 body named `write_row_order`
  (dSafePassage-9 S2), which is `tools/govkit/govkit.py#write_row_order`, the deployer's writer of
  `update-<kind>-<slug>.md` orders, run by `update`. The deployer is no kit an adopter installs, and the
  loop kit takes no edge to it. Options: (a) one writer in `composition.py`, `write_loop_order`,
  writing `.governance/outbox/loop-<kind>-<slug>.md`, the folder an owner already reads gov's orders
  from, under a prefix no `update` order uses; (b) `govkit.py` found by `resolve_kit_dir` and imported,
  `unarmed` in every adopter, its `update-` names claiming orders `update` did not write; (c) no file,
  each order a `loop: order` line on the `record` verb's output and a field on the move. (b) files
  nothing where the loop runs, and (c) leaves the owner no standing order to act on. Recommendation:
  (a). RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: the [security] practice, the narrowest
  write, one file under the outbox, and no edge to the deployer.
  widens: none · relaxes: none
- **F7 — Which items does a build hold at a move?** S5 at rev-4 read "an item the build had witnessed,
  or was positioned on". The position engine reads a witness under a tag only where a recorded move
  names it (`tools/loop/position.py#derive_position_into`, its `named` map); every other item's
  witness is unread or state-keyed. Options: (a) the tags the build's recorded moves name; (b) those
  plus the next item `derive_position` answers at the old pin, derived at each move. (b) runs the
  engine, the driver's hand-over and a worktree at the old pin inside the writer, and an item the
  build was positioned on and never witnessed has no witness to lose: its successor is simply read
  from the new pin's frontier. Recommendation: (a). RESOLVED (agent, 2026-11-15, delegated): (a),
  rung 3: the [yagni] practice, since (b)'s order would report a loss that did not happen.
  widens: none · relaxes: none
- **F8 — When does a renamed policy value file its order?** The rev-4 move read every tag-valued key
  at each boundary. The loop kit reaches the policy kit's `resolve` but not the playbook kit's
  `tools/playbook/policy_value.py#read_tag_policy`, whose walk of the catalogue decides which keys are
  tag-valued. Options: (a) `read_tag_policy` files the order when a reader reads a key and a member
  redirects, so the keys this unit serves are exactly those a reader asks for, `review.breakpoints`
  first (TOOL-dDeclaredLoop-19 S4); (b) at each move, every key whose catalogue row's `allowed`
  registry reads "named item boundaries", a walk copied from the playbook kit and keyed on a prose
  field. (b) copies a walk and grades a key no reader acts on. Recommendation: (a). RESOLVED (agent,
  2026-11-15, delegated): (a), rung 3: the [one-fact] practice, the tag-valued walk kept in its one
  owner.
  widens: none · relaxes: none
- **F9 — How does position read its items at the pin?** Since unit 29 `derive_position_into` and
  `print_check_refusal` read through `tools/loop/loop_items.py#read_composed_items`, which maps
  `read_composition`'s exit 0 to the composed rows, exit 2 to gov's own rows and exit 1 to a
  ValueError, and `upstream.py` reads the same way. `read_composition_at` answers that triple at a pin,
  so position needs the mapping there. Options: (a) `read_composed_items` takes `rev=None` and, where
  one is given, reads the triple through `read_composition_at`, one parameter on a function this unit
  then edits in `tools/loop/loop_items.py`; (b) `position.py` copies the mapping beside its call of
  `read_composition_at`. Neither fails an acceptance criterion, gate or non-goal, and neither adds a
  dependency, a public surface or a write. (b) puts a second owner on the 0/1/2 mapping, which the
  [reuse] and [one-fact] practices refuse, and the tie-break takes the seam M5 found.
  Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated): (a), by the ratify rule's tie-break,
  the reuse of `read_composed_items`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 26, the flow adoption's items 14 and 15
  and FA-7, and dOrderedCharter-15, -35, -46 and dSafePassage-9 read at base `ed497191`; re-read at
  `462d20f35` for rev-3.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.
- rev-3 · 2026-10-25 · S1 S3 S6 S7 S8 · §3 · §4 · §5 · AC5 AC6 AC8 · §8 F4 F5 · §9 · §10 · re-grounded on
  dOrderedCharter's specs at `462d20f35` per
  `build/2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md` rows 81, 82 and 83: the
  composition revision is `HEAD` (unit 46 S1); a reader-command population runs in the pin's worktree;
  a pin is composed in a worktree detached at it (F4); the policy read, F5 and AC8 follow the
  sibling-kit and leg facts of `prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md`.
- rev-4 · 2026-11-05 · S3 S8 · §4 Files touched · AC8 · §8 F5 · the owner resolved F5 to (a), the
  `compose` verb ask, per the brief `2026-11-05-prompt-TOOL-dDeclaredLoop-3-owner-forks`; S3 names the
  subprocess route. TOOL-dDeclaredLoop-56 §8 F5 (a), per the brief
  `2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade`: the leg keeps `principle.p8`; S8 takes
  the stale pending row of its tag, and AC8 observes the core meta-check green.
- rev-5 · 2026-11-15 · S1 to S9 · §1 · §3 · §4 · §5 · AC1 to AC8 · §7 · §8 F6 F7 F8 · §10 · re-grounded
  on the code of branch `unattended-declared-loop-d56bf0` at `dac974418eab`, per the brief
  `2026-11-15-prompt-TOOL-dDeclaredLoop-26-1-spec-writer`. The `compose --kind item` verb and
  `read_composition` landed with unit 24, so `read_composition_at` wraps that read and position's call
  of it; no population runs, the item rows being the namespace source's blob at `HEAD`. The policy is
  read through `read_policy_kit`'s in-process `resolve`, as every loop module reads it. The pin is set
  by the writer and a passed value refused; `compose_at` is `read_composition_at`, the lexicon
  declaring no `compose` verb. The leg is gov's `[[exempt_leg]]`, as each loop fixture leg is, and runs
  `--selftest`; the pending row of `principle.p8` is present and its Readers clause names the tracked
  reader. Forks F6, F7 and F8 settle the order writer, the held items and the policy order's timing.
  §5 names every row, pin, budget and fixture the change reaches.
- rev-6 · 2026-11-16 · S3 S4 · §1 · §4 · §5 · AC1 · §7 · §8 F9 · §10 · answers the four findings of
  the builder return `2026-11-16-build-TOOL-dDeclaredLoop-26-1-builder-return`, re-read on branch
  `unattended-declared-loop-d56bf0` at `fa3b7151c`: Files touched and §5 gain the loop dossier's claim,
  the four generated map files and `tools/loop/README.md`; §1 and S3 read through `read_composed_items`,
  which takes the pin's revision (F9 (a)), adding `tools/loop/loop_items.py`; S4 and The carry find the
  tag resolver under the repository being read; The plants name the scratch's branch `main`; C1 is the
  first move's commit, the pin the second move records and AC1 reads. §7 gains the upstream and map
  legs those files trip.

## 10. Reuse audit

The seams this unit extends, each read at `dac974418eab`: `read_composition` and
`build_scratch_tree` in `tools/loop/loop_items.py`, the item composition and its scratch of real kits;
`TRANSITION_FIELDS`, `write_transition` and `read_transitions` in `tools/loop/loop_transition.py`;
`resolve_commit`, `read_git` and `read_clean_env` in `tools/loop/loop_witness.py`; `read_policy_kit` in
`tools/loop/loop_parents.py`; `run_selftest_cases` in `tools/loop/loop_lib.py`; and the one tag
resolver, `show` of `tools/playbook/gov_tag.py`, whose `retired` rows `derive_retired_rows` in
`tools/playbook/instruction_units.py` extracts from the change records. `python
tools/codebase-map/reuse_lookup.py "read the item composition at a pinned commit through a scratch
worktree"` ranked `read_git`, `read_blobs_at`, `read_definition` and `read_memory_tree`, none a
composition read at a revision, and the same lookup for "the successor a change record ends a tag
with" ranked `read_change_records`, `write_change`, `read_change` and `derive_successors`, the last a
practice's `replaces` map and the others the record's own readers, which §4 Alternatives rejected
weighs. No existing seam pins a composition on a move: scout A found every build reads the landed tip
(`memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md:33`). The
order writer has no reachable seam (§8 F6). At rev-6, read at `fa3b7151c`, position's item read is
`read_composed_items` in `tools/loop/loop_items.py`, the seam S3 extends with a revision (§8 F9), and
the resolver is found by the loop kit's `resolve_kit_dir` under the repository being read.

Recall terms used: composition revision pinned transition record step boundary successor rename change record overlay order worktree tag resolver
