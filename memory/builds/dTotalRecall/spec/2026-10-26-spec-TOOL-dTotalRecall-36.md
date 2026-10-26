# TOOL-dTotalRecall-36 — every code writer of a record writes its `Caused-by` line, so the causes check stays green on the records written after its seed

**Status:** OPEN · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 17 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-1-spec-writer.md) | journal | TOOL-dTotalRecall-1 |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-39 TOOL-dTotalRecall-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, its item **H1**, alone in that item. `TOOL-dTotalRecall-19` S8 reds
every tracked record that has no legacy row, is not a root kind and carries no `Caused-by`, and its S7
seeds that legacy population once, shrink-only, at its landing. Only the door and the typed factory
write a cause. Every other writer keeps writing records with no cause line after the seed:

- the review harness's binding line (`tools/workflows/tier2-review.template.js:318-328` and `:1874-1878`);
- the build harness's clean-round record line (`tools/workflows/unattended-build.template.js:2557`);
- the roles kit's prompt record head and agent ledger (`tools/roles/handoff.py:422` and `:775`);
- the runlog run record (`tools/runlog/record.py:1137`);
- the as-built view head (`tools/memory-tree/asbuilt_view.py:150`).

The next record any of them writes reds `record causes (causes and orphans over the legacy population)`.
This unit makes each of those writers write `**Caused-by:**`, says so in the binding grammar a
hand-writer reads, backfills the records this run wrote between the seed and this pass, and adds a
writer census to the causes check so the next writer that omits the line is red at its own pass. It
repairs `TOOL-dTotalRecall-19`.

## 2. Scope (IN)

- **S1** — The review harness renders the cause line. `renderCauseLine(ids)` in
  `tools/workflows/tier2-review.template.js` returns `**Caused-by:** <the first id, bare>`, with any
  `@rev-<n>` pin stripped. The synthesis instruction names it as the record's second line, directly
  under the binding line, on both kinds: for the spec kind it sits inside the `<<<SERVES` block the
  agent copies verbatim, and for the diff kind the instruction spells it from the first unit id of the
  diff. `tools/workflows/tier2-review.js` is re-rendered from the template. Observed by AC1.
- **S2** — The build harness's clean-round record. The `nextAction` text of
  `tools/workflows/unattended-build.template.js` that hands the caller `pinnedLine` names line 2 as
  `**Caused-by:** <owed[0]>`, and `tools/workflows/unattended-build.js` is re-rendered. Observed by AC2.
- **S3** — The roles kit. `tools/roles/handoff.py` writes `**Caused-by:** <unit id>` on the line after the
  prompt record's `**Serves:**` line (`:422`), and the agent ledger it creates (`:775`) writes
  `**Caused-by:** <its first id>` under its Serves line. Rewriting an existing ledger's Serves line keeps
  a cause line already present and inserts one where none is. Observed by AC3.
- **S4** — The runlog run record and the as-built view. `render_markdown` in `tools/runlog/record.py`
  writes `**Caused-by:** <the first served id>` on the line after the Serves line, and the run record's
  head check (`check_serves_line`, `:1461`) gains its sibling `check_cause_line`, which reds a head with no
  cause line or a cause naming no served id. `VIEW_HEAD` in `tools/memory-tree/asbuilt_view.py` writes
  `**Caused-by:** {serves}` under its Serves line. Observed by AC4.
- **S5** — The grammar a hand-writer reads. The "Record bindings" section of
  `tools/memory-tree/HYGIENE.template.md` (`:616`) states that a record written after the causes seed
  carries `**Caused-by:** <target>` within the first `BIND_HEAD_LINES` lines (`tree_lib.py:401`), and
  names `gov_record.py new <kind> --caused-by <target>` as the door that writes it. The render reaches
  `memory/HYGIENE.md` through `adopt-memory-tree.sh --render`. NOT OBSERVED by a criterion: a prose
  rule, held equal to its render by the `kit/dogfood doc parity` leg at the close.
- **S6** — The backfill. Every tracked record that the legacy population of `TOOL-dTotalRecall-19` S7
  lacks and that carries no `Caused-by` at this unit's pass base gains `**Caused-by:** <its first
  Serves id>` on the line after its Serves line, in this unit's pass commit. These are the records the
  run wrote between unit 19's seed and this pass, its prompt records first among them. Observed by AC5.
- **S7** — The writer census, `check_cause_writers(root)` in `tools/memory-tree/record_causes.py`, run by
  `--check` beside `check_causes`. It lists every tracked `*.py`, `*.js` or `*.sh` file under the tool
  root, test-named files excepted (`*.test.sh`, `selftest.py`, `test_*.py`), that spells a
  `**Serves:** ` literal and spells no `Caused-by`. A file on the census is red unless the constant
  `CAUSE_WRITER_KEPT` in the same module lists it with a reason, for a file whose Serves literals are
  fixture or instruction text only. The candidate predicate is run over the real tree before the
  constant is written, and the pass commit's `Decided:` trailer names each kept file. Observed by AC6.

## 3. Non-goals (OUT)

- The causes check, the orphan check, the legacy population and the door's `--caused-by`:
  `TOOL-dTotalRecall-19`'s. This unit changes no rule of theirs.
- A cause richer than the first served unit. Each writer here serves a unit or an instrument, and the
  first of them is the cause the legacy reading already assumes (`TOOL-dTotalRecall-19` S8). A writer
  with a better-known cause, such as dWellOiledMachine's intake, writes that one when it lands.
- Rewriting a legacy record. S6 touches only records the population lacks.
- Proving that a census file writes the line at run time. The census grades spelling; each writer's
  own arm in §7 grades behaviour.

### Edges

- **consumes-from** `TOOL-dTotalRecall-19` — `check_causes`, the legacy population `legacy-records`
  and the door's `--caused-by`, whose cause grammar every writer here emits and whose module the
  writer census joins
- **hands-off** `TOOL-dTotalRecall-47` — S6's backfill rule, which that unit applies as a verb at its later tip (the round-1 audit of units 36 to 43, id 3)
- **hands-off** `TOOL-dTotalRecall-48` — `render_markdown`'s cause line and `check_cause_line`, which that unit admits into the run record's fixed head and narrows to shape (the round-1 audit of units 36 to 43, id 30)
- **hands-off** `TOOL-dTotalRecall-49` — `VIEW_HEAD`'s cause line, which that unit takes back out, and `CAUSE_WRITER_KEPT`, whose reasons it widens (the round-1 audit of units 36 to 43, id 31)
- **hands-off** `TOOL-dTotalRecall-50` — `check_cause_writers`, whose population that unit widens to the build folders' scripts (the round-1 audit of units 36 to 43, id 32)
- **hands-off** `TOOL-dTotalRecall-51` — S5's Record bindings sentence and S6's backfill, whose non-markdown records that unit gives their comment-prefixed form (the round-1 audit of units 36 to 43, id 40)
- **hands-off** `TOOL-dTotalRecall-53` — the writer census, `CAUSE_WRITER_KEPT`, AC4 and the writers `migrate_backlog.py` and the guide's record heads, which that unit extends (the round-1 audit of units 36 to 43, ids 4, 5, 14, 15, 16, 28, 29, 33, 34 and 41)
- **hands-off** `TOOL-dTotalRecall-60` — its AC4 arm in `tools/runlog/selftest.py`, which that unit rewrites to unit 48's narrowed rule (the round-1 audit of units 44 to 53, id 30)

## 4. Design

### The head each writer emits

```markdown
**Serves:** spec-audit TOOL-dTotalRecall-19@rev-1 TOOL-dTotalRecall-36@rev-1
**Caused-by:** TOOL-dTotalRecall-19
# Tier-2 review: ...
```

The cause line sits directly under the binding line, so it falls inside the first `BIND_HEAD_LINES`
(12) lines that `read_header_edges` reads (`TOOL-dTotalRecall-19` S1), and the binding line stays the
record's first line, which hygiene check 21's binding-head window and check 22's opening order read.
The target is a bare unit id: `TOOL-dTotalRecall-19` S5 resolves a `family-id` in the defined-id set,
and a pinned `@rev-<n>` token is not one.

### The census

| Census file at base | Disposition |
|---|---|
| `tools/workflows/tier2-review.template.js`, `unattended-build.template.js` and their renders | S1 and S2 write the line |
| `tools/roles/handoff.py` | S3 writes the line |
| `tools/runlog/record.py` | S4 writes the line |
| `tools/memory-tree/asbuilt_view.py` | S4 writes the line |
| `tools/memory-tree/deviation_join.py` | already spells `Caused-by` (`:147`), so it is off the census |
| `tools/memory-tree/gen_build_index.py`, `migrate_backlog.py`, `adopt-memory-tree.sh` | probed at the pass; kept only where every Serves literal is fixture or instruction text |

The table is the reading at base `462d20f3`, from `git grep -n "Serves:\*\* " -- tools`. The census
itself is derived at every run and never typed.

### Inventory

Minted: `renderCauseLine` in the review harness, `check_cause_line` in `tools/runlog/record.py`,
`check_cause_writers` and `CAUSE_WRITER_KEPT` in `tools/memory-tree/record_causes.py`. Naming cells:
each Python name is asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function` at the
pass, and `renderCauseLine` under the JavaScript cell.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/roles/handoff.py`
- `tools/roles/selftest.py`
- `tools/runlog/record.py`
- `tools/memory-tree/asbuilt_view.py`
- `tools/memory-tree/record_causes.py`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md` (the render)
- `memory/builds/dTotalRecall/prompts/` (S6's backfill)
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Grade only the kinds whose writer is the door, and exempt the rest with an ask each.** It keeps
  the leg green by narrowing what P35 covers, and every review, prompt and run record of the next
  build would sit outside the rule this build lands.
- **Re-seed the legacy population at this pass.** The ledger is shrink-only (`TOOL-dTotalRecall-19`
  S7), so a re-seed is refused, and it would launder exactly the records the rule is about.

## 5. Production-readiness checklist

- security — no new write surface: each writer gains one line in a file it already writes.
- perf / scale — the census is one `git grep` over the tool root per check run.
- error / empty / loading states — a census file with no reason in `CAUSE_WRITER_KEPT` is red and
  named; an empty census prints `0 writer(s) without a cause` and is a pass, because every writer was
  found and each writes the line.
- observability — `--check` names each census file and its first Serves literal's line.
- risks — the census grades spelling, so a writer that spells `Caused-by` in a comment and never
  writes it passes the census; the causes check itself still reds the record it writes.
- testing — AC1 to AC6 by the pass; the arms of §7 at the close.
- migration — S6's backfill of this run's own records, nothing landed.
- user docs — none under `help/`: no page covers record heads; `memory/HYGIENE.md` carries S5.

## 6. Acceptance criteria

- **AC1** — When a `node -e` probe loads `tools/workflows/tier2-review.js`'s body with
  `new Function(...)` and returns `renderCauseLine`, as `tier2-review.test.sh:237` loads
  `renderAuditBinding`, the call over the ids `TOOL-x-1@rev-2` and `TOOL-x-2` returns
  `**Caused-by:** TOOL-x-1`; and `grep -c "Caused-by" tools/workflows/tier2-review.js` counts the
  instruction text on both kinds' branches.
  Red when: the pin is kept on the target, or the diff kind's instruction names no cause line.
- **AC2** — When `grep -n "Caused-by" tools/workflows/unattended-build.js` runs at the pass tip, the
  clean-round `nextAction` text names line 2 as the cause line beside `pinnedLine`.
  Red when: the clean-round record the caller writes is instructed with the binding line alone.
- **AC3** — When `python tools/roles/handoff.py` writes a prompt record for a fixture unit in a
  scratch clone under `%TEMP%`, the line after its Serves line is `**Caused-by:** <the unit id>`; when the agent
  ledger is created and then rewritten with a second id, `grep -c "Caused-by"` over it prints `1`.
  Red when: the rewrite path drops or doubles the cause line.
  fixture: a scratch clone with one build folder and one spec; the pass makes it.
- **AC4** — When `render_markdown` from `tools/runlog/record.py` renders a fixture record serving
  `TOOL-x-1`, the line after its Serves line is `**Caused-by:** TOOL-x-1`, and `check_cause_line`
  over the same head with that line cut returns one finding; and `VIEW_HEAD.format(serves="FIX-y-6")`
  from `tools/memory-tree/asbuilt_view.py` holds `**Caused-by:** FIX-y-6`.
  Red when: the run record or the view is written with no cause, or the head check passes a head
  without one.
- **AC5** — When `python record_causes.py --check` runs at the pass tip, it prints
  `0 causeless`, and `git diff --stat <pass base>..HEAD` lists each record S6 backfilled.
  Red when: a record this run wrote after unit 19's seed still carries no cause.
- **AC6** — When `python record_causes.py --check` runs in a scratch copy of the
  tree where `tools/roles/handoff.py`'s two cause lines are cut, it exits 1 naming `handoff.py` under
  the writer census; at the pass tip the census names no file outside `CAUSE_WRITER_KEPT`.
  Red when: the census reads only the registry's writer cells, so a writer the registry does not
  name escapes it.
  fixture: a scratch copy under `%TEMP%`; the pass makes it.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `runlog selftest` · `runlog record schema` · `pre-push run-log line` · `run-gates run-log line` · `kit/dogfood doc parity` · `memory hygiene` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/record_causes.py · covers AC6 · the writer census plant `writer-without-cause`, a fixture file spelling a Serves literal and no cause, staged by cutting `check_cause_writers` from `--check` · none
New arm: tools/workflows/tier2-review.test.sh · covers AC1 · a pin on `renderCauseLine`'s output beside the `renderAuditBinding` pin, staged by returning the pinned id · none
New arm: tools/runlog/selftest.py · covers AC4 · a run record head with its cause line cut, staged by `check_cause_line` returning no finding · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — May this unit change `HYGIENE.template.md`, a governance carrier, to state the cause line?**
  Options: (a) yes, under the build's grant, the cause line being cl-dClosedLoop-0230's "each record's
  header (Serves, Made-by, Caused-by)"; (b) no, leaving hand-writers to learn the rule from the red.
  (b) leaves every hand-written record of the next build red with no instruction that prevents it.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 5, the grant the README's `may:` line names.
  grants: PLAY-dClosedLoop-3 HYGIENE.template.md's Record bindings section states the cause line ·
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's id 1 (HIGH, item H1).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off mirror of TOOL-dTotalRecall-47, TOOL-dTotalRecall-48, TOOL-dTotalRecall-49, TOOL-dTotalRecall-50, TOOL-dTotalRecall-51, TOOL-dTotalRecall-53, each a consumes-from edge of a unit the round-1 spec audit of units 36 to 43 promoted.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.

## 10. Reuse audit

The seams extended are the writers themselves, each at the line that already writes the binding
(`tools/workflows/tier2-review.template.js:318`, `tools/workflows/unattended-build.template.js:2557`,
`tools/roles/handoff.py:422` and `:775`, `tools/runlog/record.py:1137`,
`tools/memory-tree/asbuilt_view.py:150`), and `TOOL-dTotalRecall-19`'s `record_causes.py`, whose
`--check` the census joins. No existing seam fits the census: `python tools/codebase-map/reuse_lookup.py
"record writer emits a cause header line"` ranked name-stem neighbours (`write`, `write_text`,
`records`, `emit`) and no writer inventory. The recall probe returned the promotion precedent
`TOOL-cMendedVintage-19` and the dSafePassage promoted specs, which place a repair after its unit.

Recall terms used: `python tools/memory-recall/query.py "how is a confirmed spec audit finding promoted to a repair unit ordered after the unit it repairs" --terms "promoted HIGH repairs order spec-audit disposal batched minors rescope add Derived PLAY-dClosedLoop-2 hands-off"`
