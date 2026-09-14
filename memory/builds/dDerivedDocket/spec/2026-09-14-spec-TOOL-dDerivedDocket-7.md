# TOOL-dDerivedDocket-7 — generated family view

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g2-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g2-round1.md) | spec-audit | TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 |

<!-- /gen:spec-records -->

## 1. Goal

Once asks are filed per build, a reader still needs one place per family to see what is live, and
that place must be generated, byte-compared and unable to erase what a straggler branch merged into
it. Wire the fold into the index generator: read every tracked `BACKLOG.md`, render one view per
declared family at the path the authored shards occupy today, report every fold verdict through the
check path, refuse to overwrite a view carrying authored rows, and answer "what decided this id"
through print modes. Everything here runs only under `BACKLOG_MODE=builds`, so this repo's output
does not move until the switch-over.

## 2. Scope (IN)

- **S1** Under `builds`, `collect()` reads every tracked `<MEMORY_ROOT>/builds/*/BACKLOG.md` through
  the ask parser, and hands the fold the spec index it already builds and the derived build-status
  map it already computes. The generator's source list grows from three to four in its own header;
  it still reads no history and no mtime. Observed by AC1.
- **S2** Filing homes: under `builds`, a folder whose only tracked file is `BACKLOG.md` is collected
  as a home, never raised on, and never reaches `LIVE.md` or a ledger shard. Under `shards` the
  existing refusal stands. Observed by AC8.
- **S3** Under `builds`, `rosters()` skips `<MEMORY_ROOT>/backlog/`, beside `LIVE.md` and the ledger;
  under `shards` it reads it exactly as today. Observed by AC9.
- **S4** Under `builds`, `plan()` renders `<MEMORY_ROOT>/backlog/<FAMILY>.md` for every family
  `FAMILIES` declares, in the §4 grammar; a family with no live ask renders `*No live ask.*`, so
  every declared family has a view. Observed by AC1 and AC2.
- **S5** The view defines no id: its first cell is link-wrapped and it carries no dash row, asserted
  with the real `extract.anchor_at` over every line. Observed by AC2.
- **S6** The view header carries the relocation recipe of design §18r.4, rendered from one constant
  with the kit prefix derived, never spelled — so a pre-switch branch that conflicts on a view reads
  the instruction inside the conflict region (design layer L4). The same constant feeds every
  message this unit prints. Observed by AC3.
- **S7** Verdicts: `--check` reports every fold verdict V1 to V12 and the three guards below, with
  its code, and exits 1; `--write` renders every artifact over a tree carrying any of them, prints
  them, and exits 0, because a render is not a verdict. Observed by AC4.
- **S8** The data-loss guard, the one exception to S7: before overwriting a view, `--write` reads it,
  and a line that leads with an id after a list marker, or a conflict marker, is authored content the
  grammar never emits. `--write` then writes every OTHER artifact, leaves that view byte-unchanged,
  names each line and the recipe's three entry points, and exits 1; `--check` reports the same in
  place of its usual `--write` remedy. Observed by AC5.
- **S9** The mode guard: under `shards`, a tracked `BACKLOG.md`, or a spec header carrying `closes`
  or `advances`, is a verdict — the half-migration shape (design critique A8). Observed by AC6.
- **S10** The archive guard: under `builds`, a tracked rotated archive whose stem is a declared
  family is a verdict, because the per-build model keeps no backlog archive (owner ruling D8,
  design A5). Observed by AC7.
- **S11** A liveness line on every run. Under `builds`: `build-index: backlog <a> ask(s) · <d>
  row(s) · <l> link(s) in <h> file(s) · <v> live · <k> verdict(s)`. Under `shards`: one line saying
  the layout is shards and no view is rendered. Observed by AC10.
- **S12** Print modes that write nothing and always exit 0: `--asks [FAMILY|ID] [--all] [--status
  <token>] [--build <slug>] [--json]`. The table form lists live asks, or every ask with `--all`; an
  id argument prints that ask's status and everything that decided it, terminal included. The JSON
  form is `{mode, examined, asks}` carrying the fields §4 names, which drift-audit and the agent
  carriers read. Under `shards` they print the mode notice and an empty set. Observed by AC11.
- **S13** One conf key, `BACKLOG_EXCERPT_CHARS`, default 72, declared in the kit's conf example and
  descriptor; a non-positive or non-numeric value is a refusal. Observed by AC12.
- **S14** Dark proof: with gov in `shards`, this tree's artifacts do not move. Observed by AC13.

## 3. Non-goals (OUT)

- The grammar, the fold and the verdict rules. All are the parser unit's; this unit calls them.
- The hygiene engine's checks 4, 6, 7, 8, 13, 15 and 20, and HYGIENE's text. The engine unit's.
- The row driver's refusal to merge a shard into a view, and the `.gitattributes` line for
  `BACKLOG.md`. The driver unit and the switch-over.
- `--ready`, `--tsv`, `--at` and the `--new-build` scaffold. The envelope unit's.
- Rendering a view in this repo, deleting an archive, or writing any `BACKLOG.md`. The switch-over's.
- A live-ask count or cap in the view (owner ruling D3); the report-only count is a drift signal the
  switch-over re-points at `--asks --json`.
- Deriving LANDED anywhere inside a committed generated file; that belongs to the derived-terminal
  unit, and only in `--status` and the leg.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-6` — the parser, the fold, the verdict function, the row
  renderers, the liveness counts and the two conf keys. Without them there is nothing to render and
  no verdict to report.
- **hands-off** `TOOL-dDerivedDocket-8` — the view file set, which leaves check 6's caps and stays in
  check 7's entry budget, and the verdict report check 9 surfaces.
- **hands-off** `TOOL-dDerivedDocket-10` — the view-recognition predicate and the recipe constant,
  which the row driver's shard-into-view refusal reads and prints.
- **hands-off** `TOOL-dDerivedDocket-11` — collect's spec index and build-status map under `builds`,
  the view renderer the planner measures prospective views with, and the `--asks --json` shape its
  per-id report is compared against after the switch.
- **hands-off** `TOOL-dDerivedDocket-12` — `--write` and its data-loss guard, which the relocation
  engine satisfies by restoring the views before it renders, and the recipe constant, which that
  unit's `--recipe` prints rather than holding a second copy.
- **hands-off** `TOOL-dDerivedDocket-15` — the bare `--asks` print mode that unit's `--ready`,
  `--tsv` and `--at` options extend, its link-wrapped first cell, and the `--write` render its
  scaffold runs.

## 4. Design

### Seams in the generator

| Seam | At BASE | Change, under `builds` only |
|---|---|---|
| module header | "THREE SOURCES" at `tools/memory-tree/gen_build_index.py:21` | four sources: `BACKLOG.md` files join, still no history |
| `collect()` | refuses a README-less folder at `:764` | a folder holding only `BACKLOG.md` is a filing home |
| `rosters()` | skips `LIVE.md` and the ledger at `:685` | also skips `<MEMORY_ROOT>/backlog/` |
| `plan()` | adds `LIVE.md` and the shards at `:1723` | adds one view per family, and runs the data-loss guard's read |
| `cmd_check()` | one DRIFT list and one `--write` remedy at `:1751` | a separate VERDICT list with codes; a guarded view gets the recipe, never `--write` |
| `cmd_write()` | writes every artifact at `:1897` | skips a guarded view and exits 1; prints verdicts and exits 0 otherwise |
| `main()` | a closed mode tuple at `:2757` | `--asks` joins it, with its own argument parse |

Under `shards` none of these branches is reached, so the rendered artifact set and every byte of it
are unchanged; AC13 observes that rather than this sentence asserting it.

### The view grammar

```text
<GEN_HEADER, the generator's existing first line>
# <MEMORY_ROOT>/backlog/<FAMILY>.md — live asks, family <FAMILY>

Derived, never authored. Each ask is filed once in builds/<slug>/BACKLOG.md; its status is
computed from that file, the specs that close or advance it, and disposition rows. An id NOT
listed here is terminal: `python <kit>/gen_build_index.py --asks <id>` prints what decided it.
Cite ids, never line numbers.

> If your branch edits this file as an authored shard, it predates the per-build backlog.
> <the relocation recipe, one quoted line per recipe line>

| Ask | Status | Sev | Decided by | Filed | Summary |
|---|---|---|---|---|---|
| [<id>](../builds/<slug>/BACKLOG.md) | <token> | <level or —> | <evidence> | <date> | <excerpt> |
```

- **The first cell is link-wrapped**, so the table-anchor shape misses it and the view defines
  nothing; no line opens with a list marker, so the dash-anchor shape and check 20's unkeyed-row
  rule never fire.
- **The recipe lines are quoted, never listed**, because the row driver classes a list line as a
  ROW and could key or detach it.
- **The summary**: the text before the first ` → `; links reduced to their text; backticks stripped,
  so a view carries no path token check 15 could grade; `|` becomes `/`; cut at the last space before
  `BACKLOG_EXCERPT_CHARS`, then `…`. Every line stays under check 7's 300-character entry budget: the
  design measured the widest row at 186 characters at excerpt 72.
- **Merge-stable**: rows sorted by slug, then by the numeric sequence, so `-10` sorts after `-2`; no
  count, total or per-status section anywhere.

### Recognising a view

One predicate, exported for the row driver: a text is a family view when its first line matches the
generator's header SHAPE with any kit prefix, and its second line is the family H1 above. Shape, not
bytes, because the prefix is each adopter's install location.

### The data-loss guard and its message

The guard exists because the remedy line printed today at `tools/memory-tree/gen_build_index.py:1751`
is `--write`, and `--write` over a view into which a straggler merged authored rows would erase them
silently — the class the generator's own docstring names at `:39-41`. The message lists each
offending line, then the recipe's three entry points: `--relocate --as <slug>` on the straggler,
`--repair <merge-sha>` after a landing, and `--ingest <ref>` from the default branch for a branch
nobody will revisit.

### The JSON projection

`--asks --json` prints one object: `mode`, `examined`, and `asks`, a list whose items carry `id`,
`home`, `file`, `line`, `filed`, `unit`, `status`, `decided_by`, `sev`, `closing`, `declining`,
`holds` and `live_specs`. The switch-over's three drift signals read exactly `closing`, `declining`,
`live_specs` and `sev`; an `examined` of zero while a `BACKLOG.md` is tracked is theirs to call a
DEAD PROBE.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| the view renderer, the view predicate and the recipe constant | functions and a constant in `backlog.py` | lexicon python function cell |
| `--asks` and its four options | CLI mode of the generator | a flag, not a function |
| `BACKLOG_EXCERPT_CHARS` | conf key | screaming snake |

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` · `backlog.py` (the parser unit's module) ·
`tools/memory-tree/.memory-tree.conf.example` · `tools/memory-tree/kit.toml`.

### Alternatives rejected

- **A raising parser on the render path.** One unannotated record would refuse every artifact; the
  generator's own rule at `:447-450` forbids it, and `main()` turns any refusal into an unwritten
  tree (design critique ops #6).
- **An unconditional roster skip of the backlog directory.** It changes 31 of 107 rosters in shards
  mode and reds every shards adopter's check 9 on upgrade (design critique ops #14).
- **A per-status section or a count line in the view.** Every merge of two branches touching one
  family would conflict on the count.
- **No view merge attribute.** Design §7 proposed it; amendment A2 keeps `merge=rows` so the row
  driver can refuse a shard merged into a view. This unit only makes a view recognisable.

## 5. Production-readiness checklist

- security — no execution, no network; the only new write refusal protects authored content, and
  the guard writes nothing into the view it refuses.
- perf / scale — one extra pass over the tracked `BACKLOG.md` files; the TOOL view was measured at
  50,067 B for 324 live rows at excerpt 72 (design §5.3, 2026-09-13), against a 359,423 B shard.
- error / empty / loading states — an empty family renders `*No live ask.*`; an undecidable status
  renders `UNRESOLVED`; the guard names lines; shards mode announces itself instead of printing a
  clean zero.
- observability — the liveness line, the verdict codes, and the print modes that answer "why".
- risks — a clean-but-stale view merge (design critique ops #17) is caught by `--check` at the next
  memory-staged commit or at pre-push, not at merge time; the lander runs `--check` after its merge.
- testing — arms in `tools/memory-tree/gen_build_index.py`'s `--selftest` on builds-mode fixture
  trees, each staged RED, plus the shards-mode zero-diff arm.
- migration — none here; every branch is dark until the switch-over sets the mode.
- user docs — the view header explains itself and names the print mode; HYGIENE and the kit README
  describe the view through the engine and docs units.

## 6. Acceptance criteria

- **AC1** — When `python3 tools/memory-tree/gen_build_index.py --selftest` renders a builds-mode
  fixture holding asks in three folders across two of four declared families, it writes four views,
  the two empty ones reading `*No live ask.*`, and each live ask appears once in its family's view.
  Red when: a family with no live ask renders no file, so an absent view and an empty family are the
  same byte.
- **AC2** — When the selftest runs every line of every rendered view through the real
  `extract.anchor_at`, none returns an id, and no view line opens with a list marker.
  Red when: the first cell is rendered as a bare or backticked id, which anchors it and makes the
  view a second claimant of every ask.
- **AC3** — When the selftest reads a rendered view's header and the data-loss guard's message, both
  carry the recipe lines byte-identical to the one constant, with the fixture's kit prefix rather
  than a spelled `tools/` literal.
  Red when: the view spells its own copy of the recipe and the two drift apart.
- **AC4** — When the selftest stages each verdict V1 to V12 into a builds-mode fixture, `--check`
  exits 1 naming that verdict's code and `--write` exits 0 having written every artifact.
  Red when: `--write` refuses on a content verdict, so one bad ask blocks every render.
- **AC5** — When a fixture view carries an appended authored dash row, and separately a conflict
  marker, `--write` exits 1, that view is byte-unchanged, every other artifact is written, and the
  message names the line and each of `--relocate`, `--repair` and `--ingest`; `--check` names the
  same line and not the `--write` remedy.
  Red when: `--write` overwrites the view, which is the silent erasure of a straggler's rows.
- **AC6** — When a shards-mode fixture tracks one `BACKLOG.md`, and separately carries a spec header
  with `closes`, `--check` exits 1 naming the mode guard and the file.
  Red when: a half-migrated tree renders clean in shards mode and its asks are never read.
- **AC7** — When a builds-mode fixture tracks a rotated archive named for a declared family, `--check`
  exits 1 naming it; a rotated decision-log archive raises nothing.
  Red when: the guard matches every archive name, so the decision log's archive reds too.
- **AC8** — When a builds-mode fixture holds a folder whose only tracked file is `BACKLOG.md`, its
  asks are collected and the folder appears in no `LIVE.md` or ledger row; the same folder in a
  shards-mode fixture still raises the existing no-README refusal.
  Red when: the tolerance is unconditional, so a shards adopter's README-less build stops being named.
- **AC9** — When the same fixture corpus is rendered in both modes, every build README's `ids:` is
  identical, and the builds-mode roster scan reads no file under the backlog directory.
  Red when: the backlog directory is skipped in shards mode too, which moves rosters in every shards
  adopter.
- **AC10** — When `--check` runs on a builds-mode fixture, the backlog liveness line prints counts
  that match the fixture; on this repo's shards tree it prints the shards announcement.
  Red when: a builds-mode tree whose `BACKLOG.md` files parse to nothing prints zero counts with no
  verdict, which reads as an empty clean backlog.
  figure: every count on the line is DERIVED at run time.
- **AC11** — When `--asks EXMP-aFoo-3`, `--asks TOOL --all --json` and `--asks --build aFoo` run on
  the fixture, each writes nothing and exits 0; the id form prints the terminal ask's status and its
  deciding evidence, and the JSON carries `mode`, `examined` and every field §4 names.
  Red when: `--asks` exits non-zero on a verdict-carrying tree, so the one tool meant to explain a
  verdict refuses to run while one exists.
- **AC12** — When `BACKLOG_EXCERPT_CHARS` is `0`, `abc` and absent in turn, the first two refuse by
  name and the third renders at 72.
  Red when: an unusable value falls back silently, so a typo re-cuts every summary with no message.
- **AC13** — When `python tools/memory-tree/gen_build_index.py --check` runs on this repo after the
  unit, it exits 0, and `--write` over a scratch clone changes no tracked file.
  Red when: any builds-mode branch runs under shards, so the dark unit moves this repo's artifacts.

## 7. Gates

`build-index selftest` · `memory hygiene` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/memory-tree/gen_build_index.py` `--selftest` · builds-mode fixture trees for every verdict, both guards, the mode guard, a filing home and both roster modes, plus the shards zero-diff fixture · none; the leg's ceiling moves only if its evidenced maximum does

## 8. Open questions

- **F1** — What does `--write` do on a verdict-carrying tree? (a) Refuse, as a verdict. (b) Render,
  print the verdicts, exit 0, and leave the refusal to `--check`. (a) is exactly the one-record-
  refuses-every-artifact shape the generator forbids. RESOLVED (agent, 2026-09-14, delegated): (b).
- **F2** — Which remedy does the data-loss guard name? (a) `--ingest`, as design §5.2 wrote. (b) The
  whole recipe. The guard cannot tell a straggler's own tree from the default branch after a landing,
  and each needs a different entry point. RESOLVED (agent, 2026-09-14, delegated): (b), naming all
  three, which the switch-over's staged break also reads.
- **F3** — Does the mode guard cover a `closes` header under shards? (a) Only a tracked `BACKLOG.md`,
  as design A8 wrote. (b) Both. A verb that links to asks no tree holds is the same half-migration
  seen from the spec side, and it cannot fire on today's tree, where no header carries one. RESOLVED
  (agent, 2026-09-14, delegated): (b).
- **F4** — Where does the tracked-archive verdict live? Amendment A5 calls it a check 9 verdict and
  the transition-audit spec leaves it to this unit or the engine unit. RESOLVED (agent, 2026-09-14,
  delegated): here, beside the mode guard, because both are properties of the generator's population.
- **F5** — Where does the recipe constant live? The relocation spec calls its `--recipe` the source
  and compares the view header and the driver banner against it, but this unit and the driver unit
  both print the recipe before that unit exists. (a) Here, in `backlog.py`, with `--recipe` printing
  it. (b) In the migrator, with this unit holding a copy until then. (b) is two copies for three
  units. RESOLVED (agent, 2026-09-14, delegated): (a); the relocation spec's parity arm then compares
  three renderings of one constant, and the M2 cross-read carries the location to that spec.
- The rulings this unit executes: D1 adopt; D3 no hard view cap; D7 the Sev column; D8 no backlog
  archive after the proof; D9 view text is ungraded while asks stay graded — all RESOLVED (owner,
  2026-09-13).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Adds two edges the brief's table does not list, hands-off to
  units 12 and 15, reciprocating the consumes-from lines those specs declare.

## 10. Reuse audit

The seam is the generator's own render path, `tools/memory-tree/gen_build_index.py`, which already
renders `LIVE.md` and the ledger shards as generated, byte-compared artifacts; `render_live` and
`render_shards` are the pattern the view renderer follows, and the orphan-shard deletion bound at
`:1725` is the precedent for a generator that refuses to delete what it did not produce.
`python tools/codebase-map/reuse_lookup.py "render a generated index file from records and refuse to
overwrite authored content"` returned only name-stem neighbours — the codebase map's renderers and
the lexicon canon's — none of which guards an overwrite, with the shell layer unscanned. Recall
returned `TOOL-aMendedLedger-1`, the retirement of an authored index into this same generator, whose
shape this repeats one family at a time.

Where the design and BASE disagree, re-read at `abac6d59`: every line the design cites in the
generator still holds its content, and design §7's "no merge attribute on views" is superseded by
amendment A2, which this spec follows. The design's size measurement is PINNED at 2026-09-13; the
TOOL shard has since grown, and the planner re-measures the view at flip time.

M12 losses are the design's tested rejections, carried in §4 Alternatives rejected with the
measurement that rejected each.

Recall terms used: `generated index render write check drift LIVE.md ledger orphan data-loss authored overwrite byte-compare`
