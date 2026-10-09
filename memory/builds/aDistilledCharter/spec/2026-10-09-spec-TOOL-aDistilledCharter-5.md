# TOOL-aDistilledCharter-5 — the node table's paths come from a stated name, identical on every node

**Status:** SPECCED · rev-1 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams tooling · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md) | journal | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 DEPL-aDistilledCharter-2 |

<!-- /gen:spec-records -->

## 1. Goal

`derive_node_table` builds every node's primary tree from the directory name of whichever checkout
runs the render, so two nodes with differently named clones commit two different charters and each
reds the other's wiring leg, and a submodule adopter renders `vendor`. This unit takes the name from
the `project_name` answer, which is committed and therefore the same on every node.

## 2. Scope (IN)

- **S1** — The default primary tree of a fleet row is `<projects_root>/<project_name>`, where
  `project_name` is the target's `[charter]` or `[answers]` value. No probe of the rendering
  checkout feeds the table. Observed by AC1.
- **S2** — With no `project_name` answer the render refuses naming the key, rather than guessing
  a directory. Observed by AC2.
- **S3** — `[nodes.<tag>] primary_tree` still overrides one node whose clone sits elsewhere.
  Observed by AC1.

## 3. Non-goals (OUT)

- Changing where a node actually clones a repository.
- A `checkout_name` key distinct from `project_name`. A node whose clone name differs takes the
  override, which already exists.

### Edges

- **consumes-from** `TOOL-aDistilledCharter-2` — `derive_node_table` and `[nodes.<tag>]`.
- **hands-off** `TOOL-aDistilledCharter-7` — the remaining renderer findings.

## 4. Design

The probe already reads the target's `deploy.toml` for `[nodes]`; it reads `project_name` from the
same parse, `[charter]` first, keys case-folded as `read_charter_table` and `read_deploy` fold them.
The rendering node's checkout no longer enters the table, so the fixture arm that renders two
differently named checkouts now expects the same Primary tree column in both.

### Files touched (estimate)

`tools/playbook/render_playbook.py` · `tools/playbook/README.md`

### Alternatives rejected

- **The origin URL's basename.** A repository may have no remote, and an adopter's remote name is not
  gov's to assume.
- **Keeping the probe with a submodule fallback.** Still node-dependent for two clones named apart.

## 5. Production-readiness checklist

- security — N/A — no new input surface; the value is already an answer.
- perf / scale — one fewer git call per render.
- error / empty / loading states — a missing answer refuses by name.
- observability — the refusal names `project_name`.
- risks — an adopter whose clone directory differs from its project name sees new paths in its node
  table; the override restores the old one.
- testing — selftest arms in `render_playbook.py`.
- migration — gov's paths do not move: its project name is its directory name.
- user docs — the playbook README's Nodes section.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/render_playbook.py --selftest` renders one fleet into two
  checkouts named apart with `project_name = "app"`, both tables read `C:/p/app` for the same row,
  and a `[nodes.b] primary_tree` override still wins. Red when: a table carries a checkout's name.
- **AC2** — When the fixture's `deploy.toml` gives no `project_name`, the render refuses naming it.
  Red when: it renders a guessed directory.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `govkit acceptance matrix`

New arm: tools/playbook/render_playbook.py · covers AC1 AC2 · the probe reading the checkout directory · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, promoted from the closing review round 1, R2 (HIGH).

## 10. Reuse audit

`reuse_lookup.py "render the node registry table into a charter"` is the set's probe; the seam
extended is `derive_node_table` and `resolve_node_overrides` in `tools/playbook/render_playbook.py`.

Recall terms used: `charter template playbook render AGENTS.md section parity size ceiling one-liner rule node registry tag`
