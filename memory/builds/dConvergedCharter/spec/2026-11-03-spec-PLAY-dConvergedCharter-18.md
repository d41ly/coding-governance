# PLAY-dConvergedCharter-18 — the owner's cycle walked by key from a planted build's intake, red on a hop resolved by search or prose

**Status:** OPEN · rev-1 · 2026-11-03 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 23 · closes PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0492@a532274c whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-build-PLAY-dConvergedCharter-5-reuse-scout-d.md](../build/2026-11-03-build-PLAY-dConvergedCharter-5-reuse-scout-d.md) | research | PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-23 |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 PLAY-dConvergedCharter-40 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-21 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-14 |

<!-- /gen:spec-records -->

## 1. Goal

The memory plan's `[cycle]` lists each hop of the owner's cycle with how it is reached today, prose, search or
none for most of them, and the site that types it once the chain lands; nothing walks the cycle end to end, so a hop
that falls back to search or prose goes unseen (the shape audit's M11, `cycle-walk`). This unit walks every hop by
key from a planted build's intake, through the typed edges each hop's own build declares, and reds any hop no key
reaches, as convergence's acceptance and then as a standing leg.

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `0d1c1dda`, re-grounded by the build run, which stops this
unit when one is absent: PLAY-dOrderedCharter-24 (`tools/playbook/edges.toml`, `parse_edge_lines`,
`parse_edge_target`, `derive_inverse_edges` in `tools/playbook/edge_grammar.py`); PLAY-dOrderedCharter-28 (the twelve
new types, the site adapters of its S5 and the `[[native]]` rows of `tools/playbook/namespaces.toml` with their
`pattern` and `resolver`); and every hop's typing unit, §4 "The hops". The clause runs the walk "once every hop's
build has landed", so a typing unit absent at the build run is a stop, never a stand-in.

- **S1** — The hops, `tools/memory-tree/cycle.toml`, one `[[hop]]` row per hop in walk order, keys `id`, `from`,
  `to`, `type`, `inverse`, `site` and `typed-by`: `from` and `to` a native class or namespace that
  `tools/playbook/namespaces.toml` registers; `type` an `edges.toml` type, or `key` for the one hop that reaches its
  node by the same key; `inverse` true when the edge is declared at the `to` node's site; `site` the memory plan's
  "Planned site" words; `typed-by` the unit that types it. The rows are the 14 hops of `[cycle]` as 15 rows, the
  hop naming two sources split in two, and three hops `[cycle]` lacks that lead from the intake into it: intake →
  request and request → build, from TOOL-dWellOiledMachine-27 S5 and TOOL-dPlacedRequest-19 (scout D disagreement
  7), and build → work order through the `gov:handoff` marker's `build=` (PLAY-dOrderedCharter-28 S5): 18 rows,
  §4. Observed by AC1.
- **S2** — The reader, `read_cycle_hops(root)` in `tools/memory-tree/cycle_walk.py`: validated rows, refusing
  (exit 2, naming the row) a key outside the seven, an `id` twice, a `type` that is neither `key` nor a type
  `edges.toml` holds, a `from` or `to` no namespace or native row registers, and a row whose `from` no earlier row
  reaches, the first row's `from` being `intake-key`. `python cycle_walk.py --rows [--hops <path>]` prints the
  validated rows of the tree's table, or of the table at `<path>`. Observed by AC1 and AC5.
- **S3** — One hop resolved, `resolve_cycle_hop(root, hop, key)`, returning the keys of the `to` nodes. Forward, it
  reads the edges of `type` at the site of `key` through the site adapters `edge_grammar.py` already runs for its
  `--check` (PLAY-dOrderedCharter-28 S5); `inverse`, it reads the declared edges at the `to` class's sites through
  the same adapters and takes `derive_inverse_edges` (PLAY-dOrderedCharter-24 S5) at `key`; `key`, it asks the `to`
  class's `[[native]]` resolver for the same key. Each returned key must classify under `parse_edge_target` and
  resolve through the `to` class's `[[native]]` resolver; a key that does not is not a node and is named in the
  hop's line. The walker reads only what the adapters read, and runs no text search of its own. Observed by AC2
  and AC3.
- **S4** — The walk, `check_cycle_walk(root, start)`: from `start`, an intake's content key, it resolves the rows in
  order, each from the keys an earlier row reached for its `from`, and prints one line per hop,
  `cycle — <id> · <from> <key> → <to> <key> · <type>`. A hop that yields no key reds
  `cycle — <id> · <from> <key> → <to> · no <type> key at <site> · resolved by search or prose at best`. A last
  line counts, `cycle — <n> hop(s) · <k> by key · <r> red`, so a walk of no rows is announced. Exit 1 on a red
  hop, 2 on a refusal, else 0. Observed by AC2 and AC3.
- **S5** — The planted build, `write_planted_build(tree)`: in a scratch repository it writes one node of every class
  the rows name, from an intake to a promoted unit, each site through the writer its kind's registry row names in
  `tools/memory-tree/record-kinds.toml` (TOOL-dTotalRecall-1's `writer`) or its owning kit's verb (§4 "The hops",
  the site column), so a planted site has the shape the real writer gives it, and returns the intake's content key.
  `python cycle_walk.py --fixture` plants and walks; `--plant prose-hop` writes the return with the work order named
  only in its prose and no `answers` edge; `--plant search-hop` writes the act's commit with no `Gov-Act:`
  trailer, the act id only in a transcript line under the tree. Observed by AC2 to AC4.
- **S6** — The leg `cycle walk`, argv `python {prefix}/memory-tree/cycle_walk.py --fixture`, gov's own: its subject
  is the kits' code over a planted build, the class `tools/govkit/registry.toml` records for gov-only self-tests
  (owner ruling 2026-08-23), so `cycle_walk.py` and `cycle.toml` are withheld from the memory-tree payload with
  `role = "project-owned"` in `tools/memory-tree/kit.toml`, the leg is a row in `tools/gate-legs.json`, and an
  `[[exempt_leg]]` row in `tools/govkit/registry.toml` says why no adopter carries it. Where TOOL-dWitnessedBar-28
  has moved gov's own legs elsewhere by the build run, it is declared there. Observed by AC6.
- **S7** — Convergence's acceptance: the build run runs `python tools/memory-tree/cycle_walk.py --fixture` once its
  last unit is terminal, and this unit, the last in build order, closes PLAY-dConvergedCharter-24 on that run's
  verdict. Observed by AC2, through the same run.
- **S8** — The docs: `help/cycle.md`, a new page: the hops, what "by key" means, the two red cases and the leg; its
  row in `help/README.md`; `tools/memory-tree/README.md` names `cycle_walk.py` and `cycle.toml`. Observed by AC7.

## 3. Non-goals (OUT)

- Typing any hop. Each hop's site and the edge it declares are its typing unit's (§4 "The hops"); a hop this walk
  reds is a defect of that unit's landed code, filed as an ask on its build.
- A second edge parser, a second site adapter, a second inverse rule or a second native resolver: S3 calls
  PLAY-dOrderedCharter-24 and -28's.
- `gov why` and `gov trace` (TOOL-dWellOiledMachine-34): they walk causes upward from a key for a reader; this walk
  grades that every hop of the cycle is typed, and calls neither.
- Walking a real build of this repository: the clause plants one, so the walk is reproducible and its red cases are
  stageable.
- Shipping the walk to an adopter (S6).

### Edges

- **consumes-from** external — PLAY-dOrderedCharter-24 and -28 (`edges.toml`, the site adapters, `derive_inverse_edges`, the `[[native]]` rows) and every hop's typing unit in §4 "The hops", each DEFERRED at base and of an ancestor build, and each landed before this build's run

## 4. Design

### Evidence

No seam fits at base (scout D row 18): `tools/playbook/edge_grammar.py`, `tools/playbook/edges.toml` and
`tools/playbook/namespaces.toml` do not exist, nor do `tools/runtime/`, `tools/loop/` or `tools/integrations/`; `git
grep -n "Gov-Act\|resolve_edge" -- tools skills .githooks` finds nothing (PINNED, at `0d1c1dda`). The live
`corpus_ids.walk` (`tools/memory-tree/corpus_ids.py`) walks files, not edges. The shape of a row table whose rows
name loadable callables is live in `tools/govkit/step_gate.py` (`load_class_callable` at `:96`,
`read_surface_classes` at `:121`), and the hop rows follow it without callables, since every hop resolves through
one adapter set.

### The hops

The walk order. Rows 1 to 3 come from outside `[cycle]` and lead the intake into it; the rest are its rows, rows
16 and 17 one hop split by source. "Inverse" means
the edge is declared at the `to` node's site.

| # | `id` | From → to | `type` | Inverse | Site | Typed in |
|---|---|---|---|---|---|---|
| 1 | `intake-request` | intake → request | `key` | no | the request ref keyed by the intake's own content key | in TOOL-dPlacedRequest-19 S1, S3 |
| 2 | `request-build` | request → build | `caused-by` | yes | the build README's `**Caused-by:** <content key>` | in TOOL-dWellOiledMachine-27 S5 |
| 3 | `build-work-order` | build → work order | `serves` | yes | the `gov:handoff` marker's `build=` | in TOOL-dBoundRoles-17; PLAY-dOrderedCharter-28 S5 |
| 4 | `work-order-units` | work order → units | `instructs` | yes | the work order's rendered slots, by tag | in TOOL-dBoundRoles-17; PLAY-dOrderedCharter-24 |
| 5 | `practice-feature` | charter practice → feature-scoped units | `instructs` | no | the unit's `select` naming `feature.<name>` | in TOOL-dLinkedLibrary-20 |
| 6 | `work-order-act` | work order → act | `follows` | yes | the act record's `task-sha` | in TOOL-dWellOiledMachine-32 S7 |
| 7 | `act-session` | act → session | `runs-in` | no | the session binding | in TOOL-dWellOiledMachine-35 |
| 8 | `act-commit` | act → commit | `made-by` | yes | the `Gov-Act:` trailer | in TOOL-dWellOiledMachine-33; TOOL-dDeclaredLoop-23 |
| 9 | `commit-unit-item` | commit → unit and item | `serves` | no | `Gov-Unit:` and `Gov-Item:` trailers | in TOOL-dWellOiledMachine-33; TOOL-dDeclaredLoop-23 |
| 10 | `commit-landing` | commit → landing | `carries` | yes | the landing record | in DEPL-dShippedRelease-1 |
| 11 | `landing-verdict` | landing → verdict | `caused-by` | yes | the verdict record's parent | dWitnessedBar's verdict record |
| 12 | `work-order-return` | return → work order | `answers` | yes | the return's header | in TOOL-dBoundRoles-17 |
| 13 | `unit-record` | record → unit | `serves` | yes | the Serves line | in TOOL-dTotalRecall-19 |
| 14 | `finding-class` | finding → bug class | `caused-by` | yes | the class's header | in TOOL-dLinkedLibrary-22 |
| 15 | `commit-decision` | decision → feature, commit | `decides` | yes | the row's edge line; `Decided:` trailers | in TOOL-dLinkedLibrary-22 |
| 16 | `class-unit` | bug class → unit | `promoted-from` | yes | `instructions.edit`'s change record | in PLAY-dOrderedCharter-14; TOOL-dCalibratedLens-14 S8 |
| 17 | `decision-unit` | decision → unit | `promoted-from` | yes | `instructions.edit`'s change record | in PLAY-dOrderedCharter-14 |
| 18 | `feature-code` | feature → code | `part-of` | yes | annotations and claims | in TOOL-dLinkedLibrary-17 |

`[cycle]`'s last row names `part-of` and `implements`; row 18 walks `part-of`, and an `implements` row is added
beside it when `edges.toml` holds that type at the build run (UNVERIFIED at base, where the registry does not
exist; S2 refuses a row whose type it lacks, so a missing type is a refusal the build run reads, never a pass). Row
11's typing unit is named by the build run's reground; scout D names the record, not its unit. A finding is a
section of the review record row 13 reaches, addressed `<record id>#<finding tag>`, so row 14 reads the
`caused-by` edges whose target is that record or one of its sections.

### The lines

```
cycle — request-build · request 3f2a9c01b4de → build dPlanted · caused-by
cycle — work-order-return · work order wo-7c1e… → return · no answers key at the return's header · resolved by search or prose at best
cycle — 18 hop(s) · 17 by key · 1 red
```

### Inventory

Names this unit mints, each asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function` at this
base and answered OK: `read_cycle_hops`, `resolve_cycle_hop`, `check_cycle_walk`, `write_planted_build`. Files:
`tools/memory-tree/cycle_walk.py`, `tools/memory-tree/cycle.toml`, row kind `[[hop]]`. Hop type `key`. Plants:
`prose-hop`, `search-hop`. Leg: `cycle walk`.

### Migration

None: new files, gov's own.

### Rollout

Lands last, at order 23, once every typing unit's build has landed (the build-run preconditions). Its first green
run is convergence's acceptance (S7).

### Files touched (estimate)

- `tools/memory-tree/cycle_walk.py` (S2 to S5)
- `tools/memory-tree/cycle.toml` (S1)
- `tools/memory-tree/kit.toml` (S6, the `project-owned` rule)
- `tools/memory-tree/README.md` (S8)
- `tools/gate-legs.json` (S6, the leg row)
- `tools/govkit/registry.toml` (S6, the `[[exempt_leg]]` row)
- `help/cycle.md` (S8)
- `help/README.md` (S8)

### Alternatives rejected

- **`gov why <key>` as the walker.** The test: `derive_why_chain` (TOOL-dWellOiledMachine-34 S5) walks `caused-by`
  upward from a key to a request and stops where a record names no cause; the cycle's hops run both ways and over
  eight types, so a walk through it would grade only the hops on one cause chain and pass the rest unread.
- **One resolver callable per hop, named in its row.** The test: 18 rows would carry 18 adapters, each a second
  reader of a site PLAY-dOrderedCharter-28's adapters already read; a hop typed at one site and resolved by a
  different reader could pass while the site's own edge is malformed.
- **Walking this repository's own latest build.** The test: its hops change with every landing and the clause's red
  cases cannot be staged on it; the planted build holds both still.

## 5. Production-readiness checklist

- security — the walk writes only into its scratch repository and reads through the adapters; every subprocess an
  argv list; no key reaches a shell.
- perf / scale — one planted build of about 18 nodes and one adapter pass per hop; the leg's ceiling is set from
  its first evidenced runs, as every leg's is.
- error / empty / loading states — a missing `cycle.toml`, an empty one or an absent `edges.toml` is a refusal
  naming it, never a pass; the count line announces how many hops ran.
- observability — one line per hop and the count line.
- risks — a hop whose typing unit landed late reds the leg, which is the gate doing its work; the walk cannot see a
  site adapter that searches inside itself (§6's limit).
- testing — the plants of S5; the `New arm:` line in §7.
- migration — none.
- user docs — `help/cycle.md` (S8).

## 6. Acceptance criteria

Each run builds its scratch repository under `%TEMP%` with a short name and exits 0 only when every hop resolves by
key. What the walk does not check: a site adapter that finds its edge by searching inside itself, and whether the
planted build's shapes match every writer's options beyond the one each writes.

- **AC1** — When `python cycle_walk.py --rows` runs at the unit's build commit, it prints 18 rows in walk order,
  each with its `from`, `to`, `type` and `typed-by`, and every row of the memory plan's `[cycle]` is covered by at
  least one of them.
  Red when: a `[cycle]` row has no hop, or a row's `type` is outside `edges.toml`.
- **AC2** — When `python cycle_walk.py --fixture` runs, it prints one `cycle —` line per hop with a key on each side
  and `cycle — 18 hop(s) · 18 by key · 0 red`, and exits 0.
  Red when: a hop prints no key, or the count line is absent.
- **AC3** — When `python cycle_walk.py --fixture --plant prose-hop` runs, the hop `work-order-return` prints
  `no answers key at the return's header` and the walk exits 1; `--plant search-hop` reds `act-commit` naming
  `made-by`, the act id being findable only by a search of the transcript line.
  Red when: either planted hop passes.
- **AC4** — When `--plant prose-hop` runs with the return's `**Edges:** answers=<work order>` line restored, the walk
  exits 0.
  Red when: the fixed case stays red, so the plant reds for a reason other than the missing edge.
- **AC5** — When a scratch copy of `cycle.toml` gains a row whose `from` no earlier row reaches, or whose `type` is
  `mentions`, `python cycle_walk.py --rows --hops <copy>` exits 2 naming the row.
  Red when: an unreachable or unregistered row is read.
- **AC6** — When `grep -n '"name": "cycle walk"' tools/gate-legs.json`,
  `grep -n 'name = "cycle walk"' tools/govkit/registry.toml` and
  `grep -n "cycle_walk.py" tools/memory-tree/kit.toml` run, each prints its row.
  Red when: the leg, its exemption or the payload rule is missing.
- **AC7** — When `grep -n "by key" cycle.md` and `grep -n "cycle.md" README.md` run in `help/`, each prints a line.
  Red when: the page or its index row is missing.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `docs` · `policy fixtures` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selfcheck`

The close runs `python tools/memory-tree/cycle_walk.py --fixture` once, after the last unit is terminal, as
convergence's acceptance (S7).

New arm: tools/memory-tree/cycle_walk.py · covers AC2 AC3 AC4 AC5 · the `--fixture` plants `prose-hop` and `search-hop` and a scratch hop table with an unreachable row, staged red by a walker that accepts a hop with no key, and the new leg `cycle walk` itself run red with `--plant prose-hop` added to its argv · none

## 8. Open questions

- **F1 — Where does the walk begin, given `[cycle]` has no intake hop?** Options: (a) three rows ahead of `[cycle]`'s,
  intake → request by the shared content key and request → build by the README's `caused-by`, from
  TOOL-dWellOiledMachine-27 S5 and TOOL-dPlacedRequest-19 S1, and build → work order by the marker's `build=`;
  (b) at `[cycle]`'s first row, the charter practice.
  (b) fails the clause's "from a planted build's intake". Rung 1, v2's clause answers it (scout D disagreement 7).
  RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none
- **F2 — How is a hop resolved, and what counts as "by key"?** Options: (a) every hop through
  PLAY-dOrderedCharter-28's site adapters and `derive_inverse_edges`, each returned key classified by
  `parse_edge_target` and resolved by its class's native resolver; (b) one callable per hop named in its row; (c)
  `gov why`. (b) and (c) fail §4's alternatives. Rung 3. RESOLVED (agent, 2026-11-03, delegated): (a).
  widens: none · relaxes: none
- **F3 — A one-time acceptance, or a standing leg?** Options: (a) both: the build run's close runs the walk as
  convergence's acceptance, and the leg `cycle walk` keeps it on gov's bar; (b) the close's run only. (b) lets a
  later landing untype a hop unseen (`[gate]`). Rung 3. RESOLVED (agent, 2026-11-03, delegated): (a).
  widens: none · relaxes: none
- **F4 — Does the walk ship to an adopter?** Options: (a) no: its subject is the kits' code over a planted build,
  the class the registry's self-test exemptions hold gov-only (owner ruling 2026-08-23), so it is withheld as
  `project-owned`; (b) ship it as a memory-tree leg. (b) gives every adopter a self-test of gov's kits that has a
  job only when that source changes. Rung 1, the owner's ruling as the registry records it. RESOLVED (agent,
  2026-11-03, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, from the packet's Items 18 (`cl-dClosedLoop-0492@a532274c`), the spec brief's
  unit 18 row and I25, scout D's row for unit 18, its hop list and disagreement 7, the memory plan's `[cycle]`
  (:206-229), `[gates]` (:382-383) and `[chain]` (:335), and the shape audit's M11.

## 10. Reuse audit

No existing seam fits at HEAD. The probe `python tools/codebase-map/reuse_lookup.py "walk a chain of hops each
resolved by a typed edge key"` ranked `key`, `resolve`, `resolve_kit_dir`, `keys` and `walk`
(`tools/memory-tree/corpus_ids.py`, a file walker) by name stem, none of them an edge walk, and `git grep -n
"Gov-Act\|resolve_edge" -- tools skills .githooks` finds nothing at `0d1c1dda`. The seams the walk extends land with
its preconditions: PLAY-dOrderedCharter-24's `parse_edge_target` and `derive_inverse_edges` and
PLAY-dOrderedCharter-28's site adapters and `[[native]]` resolvers, called and never copied; the row-table shape
follows `tools/govkit/step_gate.py`'s class rows (`:96`, `:121`). Where scout D's row and source disagree: it
proposes `gov why` (`trace.py why`) as the per-hop resolver; §4's alternatives reject it, since it walks one cause
chain upward. Its "14 hops" holds for `[cycle]`; this spec walks 18 rows over them.

Recall terms used: `python tools/memory-recall/query.py "how is the owner's cycle walked by key from a build's
intake through every hop" --terms "cycle walk hop key typed edge intake caused-by serves made-by answers
promoted-from trailer resolver"`
