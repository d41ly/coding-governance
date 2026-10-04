# PLAY-aMendedFleet-4 — the `AGENTS.md` wrapper carries one node registry

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams playbook+deployer · ratified 2026-10-04 · order 97

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`AGENTS.md` holds two node registries. The authored wrapper's `## Node registry` table lists nodes
`a` to `d`, and the rendered §2 lists node `a` alone, because the template's §2 table is one row of
placeholders. A session on node `b` that reads §2, the binding ruleset, finds no row for itself, and
the next §2 bullet tells it to claim the lowest free tag, which is `b` by that table: a tag collision,
the class §2 exists to prevent. Every reader that resolves a node reads the wrapper's table. This unit
drops the §2 table from gov's render through the renderer's existing `when:` fence and `drop_blocks`
list, and gives the wrapper's table the two columns §2 requires, so the charter carries one registry
and every adopter's render stays byte-identical.

## 2. Scope (IN)

- **S1** — In `coding-governance-agents.template.md`, the §2 node table, with the blank line above it,
  is wrapped in a `when:node-table` fence; the bullet above it and every other byte stay as they are.
  `tools/govkit/entries/playbook.kit.toml` declares the block with a `[[block]]` row whose `why`
  says a project lists it when its node registry lives in the file the kickoff manifest's
  `registry:` key names, outside the rendered region, so the charter carries one registry. Observed
  by AC3, AC5 and AC6.
- **S2** — `.governance/deploy.toml` adds `node-table` to `drop_blocks`, with a comment naming this
  unit, and `AGENTS.md` is re-rendered, so its region carries no node row. Observed by AC1 and AC2.
  **Readers:** by name: the renderer's `TAG_A`, `MACHINE_A`, `PRIMARY_TREE_A`, `WORKTREE_ROOT_A` and
  `VARIANCES_A` placeholders spell the dropped table, and the five answers stay in
  `.governance/deploy.toml` for a render that keeps the block. by value:
  `_resolve_node_tag` in `tools/drift-audit/drift_report.py` and `resolve_node_tag` in
  `tools/run-gates/run-selftests.sh` match every backticked tag row; the wrapper's rows precede the
  region and the run-selftests regex is anchored at column 0, which the indented §2 row never met, so
  neither answer changes, and AC4 observes the card's reader.
- **S3** — The wrapper's `## Node registry` table gains a `Worktree root` column after
  `Primary tree` and a `Variances` column after `Remote`, so it carries every field §2 names. Node
  `a`'s two cells take its rendered §2 values; nodes `b`, `c` and `d` take
  `C:/projects/coding-governance/.claude/worktrees`, this repository's one worktree convention, and
  `none recorded`. The Tag and Machine/user cells of all four rows stay byte-identical. One sentence
  above the table says it is the registry §2's rules refer to, that this render carries no §2 table,
  and that a new node adds its row here. Observed by AC2 and AC4.

## 3. Non-goals (OUT)

- Rendering every node's row into §2 from `.governance/deploy.toml` and deleting the wrapper's table.
  It is the fuller fix the 2026-08-30 aScouredKit review named, and it needs a repeating-row grammar
  in the renderer and a new answer shape for every adopter: a new deploy-time surface (§8 F1).
- `WIRE-INTO-PROJECT.md`'s claim that the charter's §2 serves as the `registry:` file, which the
  card's heading-keyed reader cannot find in an adopter's charter. It is an adopter-facing defect in
  another carrier; this unit changes nothing an adopter reads.
- Ending the template bullet above the table with a period instead of its colon. It would churn every
  adopter's render for the sake of gov's.
- Removing the five node answers from `.governance/deploy.toml`. They are inputs a render keeping the
  block consumes, not a registry an agent reads.
- The `## Node registry` heading text and the card's reader, `derive_node_tag` in
  `skills/session-kickoff/manifest-check.sh`, both unchanged.
- Bumping the playbook kit version for the template's moved bytes, owed once at the build's close.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564`; `AGENTS.md`, the template, the deploy answers and the playbook descriptor
are byte-identical at the worktree tip `8312d315`.

- `grep -n` for backticked one-letter tag rows over `AGENTS.md` finds five: four in the wrapper at
  lines 64-67 and one, node `a`, at line 156 inside the `gov:playbook` region. The template's §2 table
  is lines 85-87 and carries the five node placeholders and `DEFAULT_BRANCH`.
- `render_playbook.py` removes a dropped fenced block with its fences, line by line, and a kept
  block loses only its fence lines, so wrapping the table and its leading blank line leaves an
  adopter's render byte-identical and gov's render free of the table and of a doubled blank line.
- `drop_blocks` is checked against the descriptor's `[[block]]` rows both ways: a member declared
  nowhere refuses, and a `when:` fence naming no declared block refuses. `security-outbound` and
  `cross-os` are the two declared today, both kept by gov.
- The renderer resolves only placeholders left in the text after the drop, so the dropped table's
  placeholders need no answer and their present answers are read by nothing.
- `derive_node_tag` reads the FIRST table under `## Node registry` in the file the kickoff manifest's
  `registry:` key names, `AGENTS.md`, splitting each row on `|` and reading cells 2 and 3 only, so
  columns appended after Machine/user move nothing.
- `tools/check-template-size.sh` sizes the template at 48193 bytes against a 48378 high-water and a
  49152 ceiling, so the two fence lines, about 60 bytes, stay under the high-water. PINNED 2026-10-04.
- The aScouredKit statewave review of 2026-08-30 found the two tables, recommended the repeating-row
  renderer, and, failing that, a §2 that stops showing a one-row fleet.

### Files touched (estimate)

- `coding-governance-agents.template.md`
- `tools/govkit/entries/playbook.kit.toml`
- `.governance/deploy.toml`
- `AGENTS.md`

### Alternatives rejected

- **Delete the wrapper's table.** The card's `node —` cell and the drift report's node tag would stop
  resolving nodes `b`, `c` and `d`.
- **Render every node row into §2.** §3's first non-goal, and §8 F1's reason.
- **Point §2's table at the wrapper with a sentence and keep both.** Two tables in one file still
  disagree on cardinality, which is the defect.

## 5. Production-readiness checklist

- security — N/A — a fenced block and a table edit; no write path.
- perf / scale — `AGENTS.md` loses the §2 table and gains two columns, a net change of a few hundred
  bytes either way, DERIVED by the build.
- error / empty / loading states — a typo in `drop_blocks` or the fence is a renderer refusal by name.
- observability — the renderer's notes print `dropped   when:node-table` on every render.
- risks — a session reading §2 alone finds the rules and no table; S3's sentence and the heading above
  the region name where the table is.
- testing — AC1 to AC6 directly; the renderer's existing fence arms already cover a declared block.
- migration — N/A — no stored state.
- user docs — N/A — the charter is the doc.

## 6. Acceptance criteria

- **AC1** — When `bash tools/playbook/adopt-playbook.sh --target . --check` runs after the re-render,
  it exits 0, and the write run before it printed a `dropped   when:node-table` note.
  Red when: `AGENTS.md`'s region was not re-rendered, or `drop_blocks` names a block no fence carries.
- **AC2** — When `grep -cE '^ *\| [^ A-Za-z][a-z][^ A-Za-z] \|' AGENTS.md` runs it prints 4, and the region cut by
  `awk '/^<!-- gov:playbook -->/,/^<!-- \/gov:playbook -->/' AGENTS.md` and piped to the same grep
  prints 0; and `grep -c "Register every node once" AGENTS.md` prints 1.
  Red when: §2 still renders its table, the wrapper lost a node, or the §2 rule itself was dropped.
- **AC3** — When `node-table` is staged out of `drop_blocks` in `.governance/deploy.toml`, the same
  `--check` reports the region stale; and when instead the `[[block]]` row is staged out of
  `tools/govkit/entries/playbook.kit.toml`, the render refuses naming `node-table`. Both restored, it
  exits 0.
  Red when: the drop is not what removes the table, or an undeclared fence renders silently.
- **AC4** — When, in a clone of the unit's tip under a short `%TEMP%` path,
  `bash skills/session-kickoff/manifest-check.sh --card --write --session p4b` runs with
  `USERNAME=agent5`, the card's node cell reads `node — b · agent5 @ DESKTOP-3J1O6CD`, and with
  `USERNAME=daily-agent` under another session id it reads `node — a · daily-agent`; and
  `grep -c -e "| daily-agent |" -e "agent5 @" -e "agent-0 @" -e "| d41ly |" AGENTS.md` prints 4.
  Red when: the new columns shift the Machine/user cell, or a row's identity cells changed.
  cost: under a minute; the clone is the only thing written.
- **AC5** — When `bash tools/check-template-size.sh` runs, it exits 0 and prints no WARN line, and
  `grep -c "when:node-table" coding-governance-agents.template.md` prints 2.
  Red when: the fence is unbalanced or the template crossed its high-water.
- **AC6** — When, in that clone, `node-table` is removed from `drop_blocks` and
  `bash tools/playbook/adopt-playbook.sh --target .` re-renders, the region of the clone's `AGENTS.md`
  equals the region of the base `AGENTS.md` read with `git show`, compared with `diff` after both are
  cut by the AC2 `awk`.
  Red when: the fence changed what an adopter that keeps the block receives.

No new refusal is added: AC3 observes the renderer's existing refusal on the new name.

## 7. Gates

`playbook render wiring` · `template size <=48KiB` · `charter size` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `kickoff-manifest ratchet` · `agent-cap restatement` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

The three govkit legs and `recall floor arms` are owed by the descriptor's path under
`tools/govkit/`; all run once, at the close.

## 8. Open questions

- **F1** — Which registry goes?
  Options: render every node into §2 and delete the wrapper's table; drop §2's table from gov's render
  and complete the wrapper's; delete the wrapper's table. The first is the fuller fix and needs a
  repeating-row grammar and a new answer shape every adopter's deploy file could carry, which veto 2
  reserves to the owner and the diet grant does not name. The third strands three nodes from the
  card and the drift report. The second rides the declared `when:` fence and `drop_blocks` list,
  changes no adopter's render, and leaves one table carrying every field §2 asks for.
  RESOLVED (agent, 2026-10-04, delegated): drop §2's table from gov's render and complete the
  wrapper's, per S1 to S3; the repeating-row renderer stays an owner turn.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft; split from unit 79 at its F1, the two tables and their four
  readers read at base, and the renderer's fence semantics read from source.

## 10. Reuse audit

The seam extended is the renderer's project-property fence: `remove_fenced` and the `drop_blocks`
check in `tools/playbook/render_playbook.py`, declared by the `[[block]]` rows of
`tools/govkit/entries/playbook.kit.toml`, which already carry `security-outbound` and `cross-os`.
`python tools/codebase-map/reuse_lookup.py "drop a charter template block for one target so the
rendered charter carries one node registry"` returned `find_block`, `target_context` and other govkit
name-stem neighbours, none of which renders the charter, so the seam was found by reading the
renderer's fence code. Recall returned the aScouredKit statewave review's finding on the two tables,
`KICK-aReplayedCard-1`'s brief requiring the card's reader to take the wrapper's table over §2's, and
unit 79's F1. Where the report and the tree disagree: the report calls the rendered §2 table, at
`AGENTS.md` lines 154-156, the second registry and files it under the wrapper; it is the rendered one
and the incomplete one, which is why it is the one dropped.

Recall terms used: `python tools/memory-recall/query.py "why does AGENTS.md carry a second node
registry beside the rendered section 2 table, and which one do readers use" --terms "node registry
wrapper AGENTS.md section 2 table rendered region drop_blocks when fence machine_a variances_a
registry key card node cell"`
