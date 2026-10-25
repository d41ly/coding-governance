# TOOL-dTotalRecall-20 — this build's own upgrade steps: the journal alias, the scaffold verbs forwarded to record, the front matter graded, and the retag

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 21 · advances TOOL-dTotalRecall-27

**Carries:** cl-dClosedLoop-0231@392c9e56 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-a.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-7 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-22 TOOL-dTotalRecall-25 |
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |

<!-- /gen:spec-records -->

## 1. Goal

Carry every adopter across the three changes this build makes to what an adopter can see, each as
a declared step that `update` walks (P38). The Serves kind `journal` is read through its alias, and
no record is rewritten. The `--new-build` and `--new-spec` scaffold verbs keep working, forwarded to
`record` by dSafePassage's shim and warning until their window closes. An adopter's README front
matter is graded against the schema before unknown keys are refused. The retag step rewrites an
adopter's own records only under `memory.legacy-anchors: retag`.

## 2. Scope (IN)

The step grammar, its reader and the walk are TOOL-dSafePassage-1 S1 and S3 (`[[upgrade]]` rows read
by `tools/govkit/upgrade_steps.py`) and TOOL-dSafePassage-2 S2. The shim declaration, its generator
and its call rule are TOOL-dSafePassage-6 S1 to S5 (`tools/govkit/shims.toml`,
`tools/govkit/shims.py`, `install.on-shim-call`). The policy read is PLAY-dOrderedCharter-19 S8's
`read_policy_value` (shared interface I8). All are DEFERRED at base `462d20f3`.

- **S1** — The journal step, `memory-tree/serves-journal-read-as-log`, an `[[upgrade]]` row in
  `tools/memory-tree/kit.toml` with `surfaces = ["serves-kind:journal"]` and `resume = "atomic"`.
  Its program, `tools/govkit/steps/memory_journal_alias.py`, runs gov's own `read_bindings` over the
  target's records. It prints the count of records whose Serves kind is `journal` and exits 0 when
  each is read as `log` through unit 18's alias. It exits 1 naming any that does not grade, and it
  writes no file. The witness is the same read. Observed by AC1.
- **S2** — The two forwards, `[[shim]]` rows `memory-tree/new-build-to-record` and
  `memory-tree/new-spec-to-record` in `tools/govkit/shims.toml`, of a new kind `verb`. `from` is
  `{prefix}/memory-tree/gen_build_index.py --new-build` (and `--new-spec`), and `to` is
  `{prefix}/memory-tree/gov_record.py new build-readme` (and `new spec`). Every argument after the
  flag passes through unchanged. Observed by AC2.
- **S3** — The `verb` kind in `tools/govkit/shims.py`. A `verb` row's `from` and `to` are a script
  path followed by its argv words. `--write` renders the forward as a block between
  `# >>> gov:shim <id>` and `# <<< gov:shim <id>` inside the `from` script, from one `verb` template.
  The template is the `py` command template's prelude (S4 of TOOL-dSafePassage-6: the stderr line
  under `warn`, the journal line under both) and a `runpy.run_path` of the `to` script with the
  mapped argv. The script's dispatch calls the block for the flag. `--check` compares the block with
  its render while the row is open and refuses it when the row is closed. The window is S5's,
  unchanged. Observed by AC2 and AC3.
- **S4** — The front-matter step, `memory-tree/readme-front-matter-graded`, with
  `surfaces = ["front-matter:build-readme"]`. Its program,
  `tools/govkit/steps/memory_front_matter.py`, grades every build README's front matter in the target
  against unit 4's `FRONT_MATTER_KEYS`, read from gov's `gen_build_index.py`. It prints
  `<path>: <key> unknown` or `<path>: <key> derived` per finding, and exits 1 on any finding, so the
  walk stops before the adopter's next hygiene run refuses the key. It writes no file. The witness
  is the same grade. Observed by AC4.
- **S5** — The retag step, `memory-tree/legacy-anchors-retag`, with
  `surfaces = ["record-headings:memory-root"]`. Its program, `tools/govkit/steps/memory_retag.py`, has
  the verbs `plan`, `up [--dry-run]`, `down` and `witness`, after `migrate_backlog.py`'s
  `--plan`, `--dry-run` and `--write`. Each verb reads the target's `memory.legacy-anchors`
  through `read_policy_value`. Under `derived` or `none` it writes nothing and exits 0. Under
  `retag`, `plan` lists each untagged heading of the target's records with the anchor unit 19
  derives for it (`derive_anchor`, I15), and `up` writes each as the heading's authored tag,
  `## [<anchor>] <heading>`. Observed by AC5 and AC6.
- **S6** — The retag's conservation. Before writing, and again after, each rewritten record equals
  its earlier bytes once every inserted `[<anchor>] ` is cut. Every untagged heading it planned is
  then tagged, and no other byte moves. `up` writes through TOOL-dSafePassage-1's before-image
  helpers, so `down` restores every file byte-identical. `--dry-run` prints the plan and the
  conservation table and writes nothing. Observed by AC5 and AC6.
- **S7** — Gov runs every step on itself first. S1 and S4 exit 0 over gov's tree, and S5 writes
  nothing on gov, whose `memory.legacy-anchors` is the default `derived`. Observed by AC7.

## 3. Non-goals (OUT)

- The `journal` to `log` rename itself, its alias in `tree_lib.py` and the inventory of its
  readers: unit 18's.
- The `record` door and its `new build-readme` and `new spec` verbs: unit 2's. This unit forwards
  to them as they land.
- The front-matter schema and its refusal: unit 4's. This unit grades against it and never
  rewrites a README.
- The derived anchors and the `memory.legacy-anchors` row: unit 19's and unit 10's.
- Retagging spec files. Check 12 grades a spec's section headings by their text, so a spec's
  sections keep the table-derived anchors and are never rewritten. Generated regions and fenced
  blocks are skipped too.
- Re-pointing the guides and kits that spell `--new-build` and `--new-spec` (`memory/TEMPLATE-SPEC.md`,
  `memory/guides/SESSION-KICKOFF.md`, `tools/unattended/unattended.sh`, among those
  `git grep -l -e --new-build -e --new-spec` prints): the forward keeps every one working, and
  re-pointing them before the window closes is the door's own unit's choice.

### Edges

- **consumes-from** `TOOL-dTotalRecall-18` — `log`, the Serves kind `journal` is read as through its alias; S1 grades the target's records against it
- **consumes-from** `TOOL-dTotalRecall-4` — `FRONT_MATTER_KEYS`, the schema S4 grades an adopter's README front matter against
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py`, the `record` door the two scaffold verbs are forwarded to
- **consumes-from** `TOOL-dTotalRecall-19` — `memory.legacy-anchors`, whose `retag` value alone lets S5 write, and the derived anchor it writes

## 4. Design

### The rows

```toml
# tools/memory-tree/kit.toml
[[upgrade]]
id = "memory-tree/serves-journal-read-as-log"
up = ["python", "{gov}/govkit/steps/memory_journal_alias.py", "up", "{target}"]
down = ["python", "{gov}/govkit/steps/memory_journal_alias.py", "down", "{target}"]
witness = ["python", "{gov}/govkit/steps/memory_journal_alias.py", "witness", "{target}"]
resume = "atomic"
surfaces = ["serves-kind:journal"]
needs-target = false

# tools/govkit/shims.toml
[[shim]]
id = "memory-tree/new-build-to-record"
kind = "verb"
from = "{prefix}/memory-tree/gen_build_index.py --new-build"
to = "{prefix}/memory-tree/gov_record.py new build-readme"
closed = false
```

The front-matter and retag rows follow the journal row's shape with their own programs.
`needs-target = false` holds for all three: each runs gov's code over the target's files and runs
none of the target's. The journal step's `down` is a no-op that exits 0, since its `up` writes
nothing.

### The forward

Today `--new-build <slug> --asks <IDLIST>` and `--new-spec <ID> --tier <1|2> [--order <n>]
[--base <sha>]` dispatch at `gen_build_index.py:8707-8709` to `cmd_new_build` (`:4050`) and
`cmd_new_spec` (`:8586`). After this unit the two dispatch lines call the rendered blocks, and
`cmd_new_build` and `cmd_new_spec` stay only as long as unit 2 still calls them. The arguments pass
through unchanged, so unit 2's two verbs take the flags their usage strings state
(`gen_build_index.py:3887`, `:8488`).

### The retag, in an adopter

Under `retag` the step reads each record's headings outside fences and generated regions. It
skips a heading that already carries a `[tag]`, and gives each other heading the anchor unit 19
derives under `derived`. A repeated heading takes the `-2` or `-3` suffix (unit 10). The plan is the
whole rewrite, so `--dry-run` shows the exact bytes `up` would write. An adopter that sets `retag`
after the walk applied the step gets it on its next `update`, because the witness exits 1 while an
untagged heading remains under `retag`.

### Inventory

Minted: the step ids `memory-tree/serves-journal-read-as-log`, `memory-tree/readme-front-matter-graded`
and `memory-tree/legacy-anchors-retag`; the shim ids `memory-tree/new-build-to-record` and
`memory-tree/new-spec-to-record`; the shim kind `verb` and its template; the programs
`tools/govkit/steps/memory_journal_alias.py`, `memory_front_matter.py` and `memory_retag.py`; the
surface classes `serves-kind`, `front-matter` and `record-headings`.

### Migration

The steps are the migration. Gov runs each on itself first (S7).

### Rollout

The forwards print their `warn` line from landing until their window closes under
`install.deprecation-window`. Until a release is cut the window holds every row, as TOOL-dSafePassage-6
S5 says.

### Files touched (estimate)

- `tools/memory-tree/kit.toml`: three `[[upgrade]]` rows
- `tools/govkit/shims.toml`: two `[[shim]]` rows
- `tools/govkit/shims.py`: the `verb` kind and its template
- `tools/govkit/steps/memory_journal_alias.py` (new)
- `tools/govkit/steps/memory_front_matter.py` (new)
- `tools/govkit/steps/memory_retag.py` (new)
- `tools/memory-tree/gen_build_index.py`: the two rendered blocks and the dispatch lines that call them

### Alternatives rejected

- **A `command` shim.** It writes its forwarder at the `from` path, which here would overwrite the
  index generator itself.
- **Forward in-process with no shim row.** Nothing would then hold the flags for a window or close
  them, which fails the clause's "by dSafePassage's shim".
- **Rewrite unknown front-matter keys.** An unknown key's meaning is the adopter's, and the clause
  asks for a grade before the refusal, not a migration.

## 5. Production-readiness checklist

- security — the retag is the one step that writes, and only an adopter's committed `retag` arms it;
  its before-image makes every write reversible.
- perf / scale — each program makes one pass over the target's memory root.
- error / empty / loading states — a target with no build README, no `journal` record or no
  untagged heading prints its zero count and exits 0.
- observability — each step prints its count or its findings; the forwards print the shim's line and
  journal it.
- risks — an adopter whose README carries an unknown key cannot finish `update` until it edits the
  key, which is the clause's grade-first order.
- testing — AC1 to AC7 by a pass; the arms of §7 at the close.
- migration — the steps themselves.
- user docs — none under `help/`: `update`'s own output carries each step's lines, and its page is
  dSafePassage's.

## 6. Acceptance criteria

- **AC1** — When `python memory_journal_alias.py up <target>` runs over a planted adopter under
  `%TEMP%` holding two `**Serves:** journal` records and one `log` record, it prints a `journal`
  count of 2, exits 0, and `git -C <target> status --porcelain` prints nothing.
  Red when: a `journal` record is rewritten, or one fails to grade through the alias.
- **AC2** — When `python tools/memory-tree/gen_build_index.py --new-build <slug> --asks <IDS>` runs
  in a fixture repository under `install.on-shim-call` `warn`, it writes the same bytes as
  `python gov_record.py new build-readme <slug> --asks <IDS>` in a twin fixture, prints one stderr
  line naming both, and adds one journal line; `--new-spec` does the same against `new spec`.
  Red when: the forward drops an argument, or writes through the old scaffold.
- **AC3** — When `python shims.py --check` runs after one byte of the rendered block is edited, and
  again with the row set `closed = true` and the block still present, it exits 1 each time naming
  the row.
  Red when: the `verb` kind is not compared, or a closed row's block passes.
- **AC4** — When `python memory_front_matter.py up <target>` runs over a planted README carrying
  `parent: dX` and `node: d`, it exits 1 printing `parent unknown` and `node derived` for that path,
  and the README's bytes are unchanged; over a README carrying only authored keys it exits 0.
  Red when: an unknown key passes, or the step writes the README.
- **AC5** — When the planted adopter commits `memory.legacy-anchors` as `retag` and
  `python memory_retag.py up <target> --dry-run` runs, it prints a plan tagging each untagged
  heading of one record, the second of two `## Notes` headings as `[notes-2]`, and a conservation
  table; `up` then writes those bytes, a planted spec is untouched, and `down` restores every file
  byte-identical.
  Red when: a byte outside an inserted tag moves, a spec's heading is rewritten, or `down` leaves a
  difference.
- **AC6** — When the same target holds `derived`, or no policy row for the key, `up` and `plan`
  write nothing and exit 0, and `witness` exits 0.
  Red when: the retag writes under any value but `retag`.
- **AC7** — When `python upgrade_steps.py list` runs at the pass tip, it prints the three
  `memory-tree/` step rows; when each program's `witness` runs against gov's own root, each exits 0.
  Red when: a row is unread or out of order, or gov's own tree fails a step it ships.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `tier2-review self-test` · `build-index selftest` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC4 AC5 AC6 AC7 · the three step programs over a planted adopter, staged by the retag writing under `derived` · that suite's arm count, raised by the arms
New arm: tools/govkit/govkit.py · covers AC3 · selfcheck arm 11 grades the two `verb` rows, staged by one byte changed in a rendered block · none
New arm: tools/memory-tree/gen_build_index.py · covers AC2 · a `--selftest` arm comparing the forwarded `--new-spec` with `new spec`'s bytes, staged by the forward dropping `--order` · none

## 8. Open questions

- **F1 — How does a shim forward a flag of a script that stays?** The two verbs are flags of
  `gen_build_index.py`, and TOOL-dSafePassage-6's kinds (`command`, `hook`, `module`) each replace a
  whole path. Options: (a) a `verb` kind whose forward is a rendered block inside the script; (b)
  forward in-process with no row; (c) a `command` shim at a new wrapper path. (b) leaves no window,
  against the clause. (c) leaves `gen_build_index.py --new-build`, the surface itself, unforwarded.
  (a) changes TOOL-dSafePassage-6's kind set, a public-surface change this clause names.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, veto 2 lifted by the README's grant.
  grants: PLAY-dClosedLoop-3 the shim declaration's kind set gains `verb` for the two forwarded
  scaffold verbs · widens: none · relaxes: none
- **F2 — What does the journal step change, when no record is rewritten?** Options: (a) a read-only
  step that grades the target's `journal` records through the alias, so the step gate sees the
  renamed surface declared; (b) no step. (b) leaves a renamed surface with no step, which
  dSafePassage's step gate reds (P38). RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, the
  clause's "its own upgrade steps: the `journal` alias". widens: none · relaxes: none
- **F3 — Does the front-matter grade also report typed derived keys?** Options: (a) unknown and
  typed derived keys, both of which unit 4 refuses; (b) unknown keys only. (b) lets `update` finish
  over a README that the adopter's next run refuses. RESOLVED (agent, 2026-10-26, delegated): (a),
  rung 3. widens: none · relaxes: none
- **F4 — The step reader, the walk, the shim generator, the door, the schema and the anchors are
  unbuilt at base `462d20f3`.** RESOLVED (agent, 2026-10-26, delegated): this spec calls each as its
  spec names it, and the build run re-grounds on the landed code, rung 1. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 20, the brief's I2, I3, I6 and I8,
  scout A's row for cl-0231, and the parents TOOL-dSafePassage-1, -2 and -6.

## 10. Reuse audit

The seams extended are TOOL-dSafePassage-1's `[[upgrade]]` row (its §4 Data model and the
`agent-cap/fanout-cap-to-agents-in-flight` precedent, whose program sits under
`tools/govkit/steps/`) and TOOL-dSafePassage-6's shim generator. The retag copies
`tools/memory-tree/migrate_backlog.py`'s plan, dry-run and write discipline and its conservation
table (`:17`, `:764`, `:2459`), the precedent scout A named. `python
tools/codebase-map/reuse_lookup.py "upgrade step that rewrites adopter records with plan dry-run and
write"` ranked `write`, `records`, `plan` (`gen_build_index.py`) and `run_arms`, and did not list
`migrate_backlog.py`'s verbs, which the scout found by reading. No existing seam forwards a flag of
a script that stays, so the `verb` kind is new (§8 F1). Scout A's rows held at `462d20f3`. The
scaffold verbs dispatch at `gen_build_index.py:8707-8709`.

Recall terms used: `python tools/memory-recall/query.py "how does an adopter upgrade carry the journal alias and the retag of its records" --terms "upgrade steps kit.toml shim journal alias retag legacy-anchors migrate_backlog adopter front matter"`
