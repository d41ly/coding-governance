# TOOL-aDistilledCharter-2 — the fleet registry assigns every node one tag and the renderer generates the node table from it

**Status:** SPECCED · rev-1 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams tooling+deployer · order 2

<!-- gen:spec-records -->

*No record names this unit.*

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
- **S5** — Retired: the placeholders `TAG_A`, `MACHINE_A`, `PRIMARY_TREE_A`, `WORKTREE_ROOT_A`
  and `VARIANCES_A`, the probe `derive_node_tag`, and the `[[block]]` rows `node-table` and
  `security-outbound`; the second goes because v4.0 keeps no outbound-specific charter line
  (PLAY-aDistilledCharter-1 moves them to the review protocol). A `drop_blocks` member naming a
  retired block is a printed note, never a refusal, so an adopter's next update re-renders instead
  of rolling back. Observed by AC5.
  **Readers:** by name: `render_playbook.py` (`PROBES`, the placeholder rows), the template's
  `when:node-table` and `when:security-outbound` fences and §2 table (PLAY-aDistilledCharter-1
  removes them), gov's `.governance/deploy.toml` (`drop_blocks`, the four `*_a` answers); by value: `manifest-check.sh`
  `derive_node_tag`, `run-selftests.sh` `resolve_node_tag` and `read_registry_tags`, and
  `drift_report.py` `_resolve_node_tag` read the RENDERED table, whose shape §4 keeps.
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

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/playbook/render_playbook.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · the BASE engine, which has no fleet and refuses a retired drop_blocks member · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

`reuse_lookup.py "render the node registry table into a charter"` returned no seam that builds a
table from data; the extended seams are `PROBES` and `build_substitution` in
`tools/playbook/render_playbook.py`, and the readers `manifest-check.sh` `derive_node_tag` and
`run-selftests.sh` `resolve_node_tag` are kept unchanged by keeping the rendered shape.

Recall terms used: `charter template playbook render AGENTS.md section parity size ceiling one-liner rule node registry tag` — surfaced `DEPL-aRepatriatedFork-1` (TAG_A defaulted, node values asked) and the aScouredKit review F3 (a one-row table cannot express four nodes).
