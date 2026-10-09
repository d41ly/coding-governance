# TOOL-aDistilledCharter-2 — the fleet registry assigns every node one tag and the renderer generates the node table from it

**Status:** SPECCED · rev-2 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams tooling+deployer · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md) | journal | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 PLAY-aDistilledCharter-5 TOOL-aDistilledCharter-8 TOOL-aDistilledCharter-9 |
| [2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round1.md](../reviews/2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round1.md) | diff-review | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 |
| [2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round2.md](../reviews/2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round2.md) | diff-review | TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 DEPL-aDistilledCharter-2 |

<!-- /gen:spec-records -->

## 1. Goal

A node's tag is today the lowest free letter in each repository it joins, so one machine carries
different tags in different adopters and the first letter of its slugs stops separating it from the
others. This unit makes gov the one allocator: a fleet registry beside the renderer names every node
and its tag once, and every adopter's charter renders its node table from it.

## 2. Scope (IN)

- **S1** — `tools/playbook/fleet.toml` holds one `[[node]]` row per node: `tag` (one lowercase
  letter), `user`, `host` (may be empty), `projects_root`, `variances` (may be empty). Seeded with
  the four rows of gov's `AGENTS.md` registry at BASE, tags unchanged. It ships beside the engine
  through the `playbook-render` kit's existing `include = ["**"]` rule. Observed by AC1.
- **S2** — A `derived` placeholder `NODE_TABLE`, probe `node_table`, renders the five-column table
  `Tag | Machine/user | Primary tree | Worktree root | Variances`, rows sorted by tag, §4 "The
  table". The fleet is graded on every read: a duplicate tag, a tag that is not one lowercase
  letter, a duplicate `user`+`host` pair, or an empty `user` or `projects_root` is a refusal.
  Observed by AC1 and AC2.
- **S3** — An adopter's `deploy.toml` may carry `[nodes.<tag>]` with `primary_tree`,
  `worktree_root` and `variances`, each overriding that one cell for that one repository. A table
  naming a tag the fleet lacks, or another key, is a refusal. Observed by AC3.
- **S4** — `render_playbook.py --claim-node --user <u> --host <h> --projects-root <r>
  [--variances <v>]` appends a row with the lowest letter the FLEET has not used and prints it. It
  refuses an existing `user`+`host` pair, a full alphabet, and an installed copy of the engine,
  recognised by the descriptor sitting beside it. Observed by AC4.
- **S5** — The v4.0 template carries none of `TAG_A`, `MACHINE_A`, `PRIMARY_TREE_A`,
  `WORKTREE_ROOT_A`, `VARIANCES_A` or `PROSE_AUDIT`, nor the `when:node-table` and
  `when:security-outbound` fences, and the probe `derive_node_tag` goes. The descriptor KEEPS the
  six placeholder rows and the two block rows, marked legacy, because an adopter's template is a
  seed `govkit update` never rewrites: a v3.x template must keep rendering under the v4.0 engine,
  or the update rolls the kit back (closing review round 1, R1). A `drop_blocks` member naming a
  legacy block whose fence the template does not carry is a printed note, never a refusal. A
  template whose marker is below `v4.0` renders as before and prints a note to reseed it. Observed by
  AC5 and AC7.
  **Readers:** by name: `render_playbook.py` (`PROBES`), gov's `.governance/deploy.toml`
  (`drop_blocks`, the four `*_a` answers); by value: NO VALUE READERS — the legacy rows stay
  declared and keep their values for any template that still names them.
- **S6** — The write mode and `--check` print a note when the charter carries a
  `## Node registry` heading OUTSIDE the region, because the kickoff card reads the first one and
  that one would hold the repository's old tags. Observed by AC6.

## 3. Non-goals (OUT)

- Re-tagging any adopter. The note of S6 and DEPL-aDistilledCharter-1's runbook step make it
  mechanical; the act is the adopter's.
- Teaching the table's readers a host-aware match. They match the user cell today and the table keeps
  that shape; two rows sharing one user are reported UNKNOWN by `manifest-check.sh`, which is honest.
- Rewriting historical `node:` front matter or slugs. A tag change is forward-only; the all-time
  slug collision grep already protects every old id.

### Edges

- **consumes-from** `TOOL-aDistilledCharter-1` — both units edit `render_playbook.py`; this one
  lands second.
- **hands-off** `PLAY-aDistilledCharter-1` — the template's `## Node registry` section holding
  `{{NODE_TABLE}}`, and removing the `when:node-table` fence.
- **hands-off** `PLAY-aDistilledCharter-4` — gov's wrapper registry deleted, so the generated one is
  the first.
- **hands-off** `DEPL-aDistilledCharter-1` — the adopter's re-tag step.

## 4. Design

### Evidence

Read at `6473ae38` on 2026-10-09.

- `derive_node_tag` (`render_playbook.py:248`) returns the constant `a`; `TAG_A` is `defaulted` to
  `a` for that reason (`playbook.kit.toml:130`). Every adopter's first renderer is therefore `a`.
- `manifest-check.sh:271-296` reads the FIRST table under `## Node registry` of the `registry:`
  file, strips backticks, and matches `$USERNAME` against the Machine/user cell by equality or by
  the prefix `<user> @`. `run-selftests.sh:283` reads rows matching
  ``^\|\s*`([a-z])`\s*\|\s*`?([A-Za-z0-9_@.-]+)`?`` in `AGENTS.md`. Both read the rendered table.
- `tools/playbook/kit.toml` ships `include = ["**"]` to `{prefix}/playbook/`, so a file beside the
  engine reaches every adopter with no new rule, and `govkit update` refreshes it.
- `derive_gate_runner` (`:204`) already reads `.governance/deploy.toml` and the engine's own
  location from inside a probe, so the probe signature needs no change.

### The table

```
| Tag | Machine/user | Primary tree | Worktree root | Variances |
|-----|--------------|--------------|---------------|-----------|
| `a` | `daily-agent @ <host>` | `C:/projects/<dir>` | `C:/projects/<dir>/.claude/worktrees` | Windows + Git-Bash … |
```

- Machine/user is `` `<user> @ <host>` ``, or `` `<user>` `` when `host` is empty.
- Primary tree is the override, else `<projects_root>/<dir>`, where `<dir>` is the name of the
  rendering repository's primary checkout (`derive_primary_tree`). Every node of gov checks out under
  one directory name today.
- Worktree root is the override, else `<primary tree>/.claude/worktrees`.
- Variances is the override, else the fleet's `variances`, else `none recorded`. A `|` in any cell is
  escaped.

### The claim

The claim appends text, never a re-serialised file, so the registry's comments survive. Letters are
taken `a` to `z`; a fleet of 26 is a refusal naming the alphabet. In an installed copy the descriptor
`playbook.kit.toml` sits beside the engine (`resolve_declaration_paths`), and a claim there would edit
a vendored file the next update overwrites, so it refuses and names gov.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `read_fleet` | function | `py.function`; asked, OK |
| `derive_node_table` | function | `py.function`; asked, OK |
| `resolve_node_overrides` | function | `py.function`; asked, OK |
| `write_fleet_claim` | function | `py.function`; asked, OK |
| `RETIRED_BLOCKS` | constant | module constant |
| `NODE_TABLE` | placeholder | declared in `playbook.kit.toml` |

### Files touched (estimate)

`tools/playbook/render_playbook.py` · `tools/playbook/fleet.toml` · `tools/playbook/README.md` · `tools/govkit/entries/playbook.kit.toml` · `memory/map/generated/symbols.json`

### Alternatives rejected

- **A tag hashed from the machine identity.** Deterministic with no allocator, but 26 letters
  collide by the birthday bound well inside a small fleet, and a collision cannot be repaired without
  an allocator anyway.
- **A machine-local identity file.** Each machine would state its own tag and two could choose the
  same one; there would be no single place a collision is visible.
- **Per-kit charter rows in every kit descriptor.** Not this unit's question; the template's
  existing `kit:` fences already compose per-kit lines (PLAY-aDistilledCharter-1 §10).

## 5. Production-readiness checklist

- security — the claim writes one tracked file in gov and refuses in an installed copy.
- perf / scale — one TOML read per render.
- error / empty / loading states — an empty fleet is a refusal: a charter with no node table cannot
  identify any node.
- observability — the render prints `derived NODE_TABLE` with the row count; S6 prints the stale
  registry note.
- risks — an adopter whose deploy.toml drops `node-table` now renders the table anyway; the note
  says so and the wrapper registry, read first, keeps working until the adopter re-tags.
- testing — selftest arms in `render_playbook.py`.
- migration — gov's tags are the seed, so gov's rendered table matches its current registry.
- user docs — `tools/playbook/README.md` gains a "Nodes" section: the fleet, the claim, the overrides.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/render_playbook.py --selftest` renders two fixture targets
  whose checkouts have different directory names from one fleet fixture, the arm sees the same
  ordered list of `(tag, Machine/user)` pairs in both tables, and the same list after the fleet's
  rows are reordered. Red when: any pair differs.
- **AC2** — When the fleet fixture repeats a tag, repeats a `user`+`host` pair, or carries tag `ab`,
  the selftest sees a refusal for each. Red when: any of the three renders.
- **AC3** — When a fixture's `deploy.toml` sets `[nodes.b] variances = "x"`, row `b` carries `x`
  and no other row moves; `[nodes.q]` with no fleet row `q`, or `[nodes.b] colour = "x"`, is
  refused. Red when: an override leaks to another row or a bad table renders.
- **AC4** — When `--claim-node` runs against a scratch copy of `fleet.toml` holding tags `a`, `b`
  and `d`, it appends tag `c` and prints it; run again with the same user and host it refuses; run in
  a scratch tree with `playbook.kit.toml` beside the engine it refuses naming gov. Red when: it skips
  `c`, appends a duplicate, or writes an installed copy.
- **AC5** — When a fixture's `deploy.toml` carries `drop_blocks = ["node-table"]` over a template
  with no such fence, the render succeeds and its notes carry `retired`. Red when: it refuses.
- **AC6** — When a fixture charter holds `## Node registry` above the region, `--check` prints the
  stale-registry note. Red when: it is silent.
- **AC7** — When `render_playbook.py --selftest` renders the v3.5 template archived at
  `memory/archive/coding-governance-agents.template-v-3-5.md` with BASE's deploy answers, it
  succeeds and its notes carry `reseed`. Red when: it refuses on a legacy fence or placeholder.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/playbook/render_playbook.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · the BASE engine, which has no fleet and refuses a retired drop_blocks member · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-09 · S5 · AC7 · closing review round 1, R1 (BLOCKER): the retired names stay
  declared as legacy so a seeded v3.x template renders under the v4.0 engine and an update cannot
  roll back; a v3.x marker prints a reseed note.

## 10. Reuse audit

`reuse_lookup.py "render the node registry table into a charter"` returned no seam that builds a
table from data; the extended seams are `PROBES` and `build_substitution` in
`tools/playbook/render_playbook.py`, and the readers `manifest-check.sh` `derive_node_tag` and
`run-selftests.sh` `resolve_node_tag` are kept unchanged by keeping the rendered shape.

Recall terms used: `charter template playbook render AGENTS.md section parity size ceiling one-liner rule node registry tag` — surfaced `DEPL-aRepatriatedFork-1` (TAG_A defaulted, node values asked) and the aScouredKit review F3 (a one-row table cannot express four nodes).
