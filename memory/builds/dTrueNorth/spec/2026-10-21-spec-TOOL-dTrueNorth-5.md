# TOOL-dTrueNorth-5 — every spec audit pins the revision it read

**Status:** OPEN · rev-2 · 2026-10-21 · node d · Tier-2 · base 271aa59de · streams tooling · order 2 · ratified 2026-10-21

**Carries:** cl-dClosedLoop-0005@5417efbc whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-prompt-TOOL-dTrueNorth-1-spec-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-1-spec-brief.md) | research | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 |
| [2026-10-21-prompt-TOOL-dTrueNorth-5-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-5-build-brief.md) | journal | — |
| [2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md](../reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md) | spec-audit | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 |

<!-- /gen:spec-records -->

## 1. Goal

Every audit of a spec record names, on its `**Serves:**` line, the revision of each spec it read as
`<id>@rev-N` (the clause's `@rev-N`), check 21 refuses a dated audit record that does not, and the
build index reads a spec whose revision moved past its pin as unaudited. The builder's, the spec
reviewer's and the diff reviewer's rule lines carry the charter's `[docs]` rule. Today 1 of 280
`spec-audit` records under `reviews/` pins a revision (PINNED 2026-10-21 by
`git grep -h '^\*\*Serves:\*\* spec-audit' -- 'memory/builds/*/reviews/*'`), so nothing can tell a
spec and its code moving together after an audit from an audited spec (`gap-build-07`).

## 2. Scope (IN)

- **S1** — `tools/workflows/tier2-review.template.js` and its render
  `tools/workflows/tier2-review.js`:
  a spec-audit subject carries `id` and `rev` beside `path` and `blob`, a subject without both is
  refused at every round, and the synthesis prompt's binding line for the spec kind is the literal
  `renderAuditBinding` returns. Observed by AC1, AC2.
- **S2** — `tools/workflows/unattended-build.template.js` and its render
  `tools/workflows/unattended-build.js`: the subject resolver returns each spec's header `rev`, the
  stage maps each subject to its roster unit's `id`, a caller-supplied subject without `id` and `rev`
  is refused, and the clean-round record instruction writes the pinned line. Observed by AC3.
- **S3** — `tools/memory-tree/gen_build_index.py`: the Serves parse keeps each id's pin, and
  `--print-bindings` prints a `P` row per unpinned or over-pinned id of a `spec-audit` record dated on
  or after `SPEC_AUDIT_PIN_CUTOFF`, plus one `Q` liveness row. Observed by AC4.
- **S4** — `tools/memory-tree/check-memory-hygiene.sh` check 21: an audit-pin branch failing on the
  `P` rows through the check's one population filter, refusing a parse with no `Q` row, and printing
  what it graded on every run. Observed by AC5.
- **S5** — `tools/memory-tree/gen_build_index.py`'s build-index region: one line naming every unit id
  whose spec's header revision is past its highest pin. Observed by AC6.
- **S6** — the key `SPEC_AUDIT_PIN_CUTOFF`, dated in `.memory-tree.conf`, blank and documented in
  `tools/memory-tree/.memory-tree.conf.example`, listed in `tools/memory-tree/kit.toml`'s
  `optional_keys`. Observed by AC7.
- **S7** — the carriers that spell the line: `memory/HYGIENE.md` "Record bindings" and its check 21
  entry, and BUILD-METHOD M4's binding line, each in its kit template and its dogfood copy. Observed
  by AC8.
- **S8** — `docs` joins the `rules:` line of `tools/roles/agents/gov-builder.agent.md`,
  `tools/roles/agents/gov-spec-reviewer.agent.md` and `tools/roles/agents/gov-diff-reviewer.agent.md`,
  re-rendered into `.claude/agents/` and the roles README catalogue. Observed by AC9.
- **S9** — the suite arms the `New arm:` lines in §7 declare, each covering the criteria it names.
  Observed by AC1, AC2, AC3, AC4, AC5, AC6 through those lines, RED-first at the close.

## 3. Non-goals (OUT)

- No pin on a `diff-review`, `journal` or `research` record: the clause names audits of a spec.
- No rewrite of the unpinned `spec-audit` records already tracked, 279 of the 280 under `reviews/`
  as the Goal's count reads: the cutoff grandfathers them by filename date, as `RECORD_SERVES_CUTOFF`
  does for the Serves line itself.
- No change under `tools/unattended/`: the `specs-audited` term at `--close`
  (`tools/unattended/unattended.sh:11826-11848`) keeps joining any spec-audit record, and making it
  pin-aware is the follow-up F3 names.
- No deviation population and no join: that is `TOOL-dTrueNorth-4`, which reads the pins S3 exposes.
- No help page: `help/roles.md` describes the `rules` key without listing any role's tags
  (`help/roles.md:19`, `help/roles.md:27`), and no page under `help/` covers record bindings.
- No kit version constant moved: the lander mints them (`tools/push-main.sh:26-32`).
- No gate requiring `docs` on those three roles: nothing reds a later removal of the tag (§5 risks).

### Edges

- **hands-off** `TOOL-dTrueNorth-4` — the deviation population's revision-after-audit arm reads each
  spec-audit record's pins from this unit's Serves parse (§4 S3), the one Serves parser, and parses
  no Serves line itself
- **hands-off** external — a pin-aware `specs-audited` term in the unattended driver, filed as an
  ask at this build's close, because that driver is unit 7's alone in this build
- **hands-off** `TOOL-dTrueNorth-9` — `_expand_ids` kept at two values for its four callers, the pins read beside it (the round-1 spec audit's id 11)
- **hands-off** `TOOL-dTrueNorth-13` — `renderAuditBinding` and the grading for a design-document subject (the round-1 spec audit's id 39)
- **hands-off** `TOOL-dTrueNorth-14` — `cmd_print_bindings`' writer test for records written by a harness in flight (the round-1 spec audit's id 40)
- **hands-off** `TOOL-dTrueNorth-16` — `cmd_print_bindings`' docs and contract clauses (the round-1 spec audit's ids 17 and 35)

## 4. Design

### The grammar

```
**Serves:** spec-audit <id>@rev-<N> [<id>@rev-<N> …]
```

`<N>` is the integer of the `rev-N` field in the spec's `**Status:**` header at the blob the audit
read. One pin per id. A range `<id>..<m>` carries no pin, so on a graded record it is unpinned. The
pin may never exceed the spec's current header revision, because revisions only grow and a pin above
the header would read as audited forever.

Every reader of the line already tolerates the suffix, verified at writing time:
`_expand_ids` admits `@rev-\d+` and drops it (`tools/memory-tree/gen_build_index.py:603`),
`expand_id_runs` strips it (`tools/unattended/lib-unattended.sh:2083`), the deviations instrument
reads it (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py:198`),
and `tools/workflows/review_replay.py:66` reads only the kind prefix. So no reader is stranded by the
spelling.

### S1 · the review harness

The validator at `tools/workflows/tier2-review.js:339-386` gains, for the spec kind and at every
round, a refusal of a subject whose `id` does not match `^[A-Z]+-[A-Za-z0-9]+-[0-9]+$` (the id
grammar of `expand_id_runs`), whose `rev` is not a JavaScript integer of 1 or more, or whose `id`
repeats another subject's. The message names the field and says the pin is what makes a revision
past it read as unaudited. It refuses at round 1 too, unlike a malformed blob: the record is the
point of the run, and an unpinned record is what this unit exists to stop. The anchored regex is also
what keeps a newline out of the prompt line the id reaches.

`renderAuditBinding(subjects)` is a pure function defined beside `renderAgentLabel`
(`tools/workflows/tier2-review.js:298`), inside the prelude the suite extracts. It returns
`**Serves:** spec-audit ` followed by each subject's `<id>@rev-<rev>`, space-separated, in subject
order. The synthesis sentence at `tools/workflows/tier2-review.js:1794-1796` keeps its diff-kind text
and, for the spec kind, instructs the agent to copy that value as the record's first line, verbatim.
The agent no longer composes the id list, so the binding is the harness's value, not the prompt's
hope. The `args` header at `tools/workflows/tier2-review.js:98` documents `id` and `rev`, which the
suite's header arm asserts against the fields read. The refusal at :359 names the new shape.

The same edit lands in `tools/workflows/tier2-review.template.js` hunk for hunk. No line it touches
carries `{{FANOUT_CAP}}`, so the template and the render stay byte-equal outside the token lines, and
`review-protocol parity (kit vs dogfood)` grades the pair.

### S2 · the build harness

- `SUBJECTS_SCHEMA` (`tools/workflows/unattended-build.js:741`) gains a required
  `rev: { type: 'integer', minimum: 1 }` per item.
- The resolver prompt (`tools/workflows/unattended-build.js:1414-1436`) also reads the `rev-N` of
  each spec's `**Status:**` header from `git show HEAD:<specPath>` and returns it as `rev`.
- The mapping at `tools/workflows/unattended-build.js:1488` becomes
  `{ path, blob, id, rev }`, where `id` is the roster unit whose `specPath` equals the subject's path.
  The id comes from the roster the script holds, never from the agent. A subject no unit's path
  matches is refused by name.
- The caller-supplied check at `tools/workflows/unattended-build.js:1509-1517` also refuses a subject
  without a well-formed `id` and `rev`, with the grammar S1 uses.
- The clean-round instruction at `tools/workflows/unattended-build.js:2476-2522` writes line 1 as
  `**Serves:** spec-audit ` followed by each owed unit's `<id>@rev-<rev>`, read from its subject. That
  is the one other writer of a spec-audit record: the callee returns `report: null` on both clean
  paths (`tools/workflows/tier2-review.js:1244`, `:1599`), and the caller writes the record.
- The `args` header line for `subjects` and the resume remedy at
  `tools/workflows/unattended-build.js:578` name `{path, blob, id, rev}`. `prevSubjects` keeps
  `{path, blob}`: it carries only the previous blob.

The same edits land in `tools/workflows/unattended-build.template.js`.

### S3 · the parse and its rows

- `_expand_ids` (`tools/memory-tree/gen_build_index.py:599`) captures the `@rev-N` group and returns
  `(ids, bad, pins)`, `pins` mapping an id to its highest N on the line. Its two call sites in
  `read_bindings` take the third value, and each record gains `"pins"`, empty when none.
- `read_spec_revs(root, tracked, conf)` maps each spec id to its header revision as an integer,
  through `parse_spec_text` (`tools/memory-tree/gen_build_index.py:490`) over the files `spec_ids`
  walks. One header parser, so this read and the units table cannot disagree.
- `cmd_print_bindings` reads `SPEC_AUDIT_PIN_CUTOFF` from the loaded conf. A value neither blank nor
  an ISO date prints one line naming the key and exits 2, which check 21 already reds as a parse
  that did not complete. For each bound record of kind `spec-audit` whose basename date is on or
  after the cutoff, or whose basename carries no date, it prints per id either
  `P<TAB><path><TAB><id> carries no @rev-N pin` or
  `P<TAB><path><TAB><id>@rev-<N> pins a revision its spec has not reached, header rev-<M>`.
  It then prints `Q<TAB><records graded><TAB><cutoff, or off>`. A blank cutoff prints no `P` row and
  `Q<TAB>0<TAB>off`. An undated record is graded because unparseable is not old, the sibling rule at
  `tools/memory-tree/check-memory-hygiene.sh:1371-1380`.

### S4 · check 21's audit-pin branch

Beside branch 2 at `tools/memory-tree/check-memory-hygiene.sh:1413-1415`:

- the `P` rows, as `  <path> — <detail>`, pass through `extract_graded_rows` (:1365), so a record
  `legacy-files.txt` lists or `RECORD_SERVES_CUTOFF` exempts is exempt here too, the one population
  filter that function's comment requires;
- a non-empty result fails 21 naming every row;
- a parse that printed `N` and no `Q` row fails 21, as the `U`-row consistency test at :1425 does;
- one stderr line on every run, naming the graded count and the cutoff:
  `the audit-pin arm graded <k> spec-audit record(s) from SPEC_AUDIT_PIN_CUTOFF=<v>`, or
  `the audit-pin arm is off (SPEC_AUDIT_PIN_CUTOFF blank)`.

The predicate lives in the generator and the fail branch in the shell, the split check 21 already
uses, because `check-arms.py` finds its arms in tracked shell.

### S5 · the unaudited reading

In `render_region` (`tools/memory-tree/gen_build_index.py:1377`), after the line at :1462-1463,
`derive_past_pin_ids(units, records)` returns `<id>@rev-<N>` for each unit whose header `rev` exceeds
`N`, the highest pin any of the build's `spec-audit` records gives it. It renders, through
`_render_wrapped_ids`:

```
Ids whose spec moved past its audited revision: TOOL-x-3@rev-2.
Ids whose spec moved past its audited revision: none — <p> of <n> unit id(s) carry a pin.
```

The token names the pin, and the current revision is already the units table's `rev` column, so the
line does not type it twice. A unit with no pinned record is not judged, and the count says how many
were, so an empty population never reads as coverage. The comment at :1459-1461 is rewritten to say
the data now supports "unaudited" for pinned ids only. The line renders unconditionally, so every
build README's `gen:build-index` region gains it at the landing's re-render (README rule 7).

### S6 · the cutoff

`.memory-tree.conf` declares `SPEC_AUDIT_PIN_CUTOFF` by the relation `SPEC_DIRECT_CUTOFF` records
(`.memory-tree.conf:295-305`), applied to records: the day after the later of the newest
`spec-audit` record filename date on any ref or live worktree and the setting commit's own day,
re-derived at the build commit and again at landing, with the reading written in the comment above
the key. F4 records today's reading. The example conf ships it blank, BLANK MEANS OFF, beside
`RECORD_SERVES_CUTOFF` (`tools/memory-tree/.memory-tree.conf.example:362-368`).

### S7 · the carriers

- "Record bindings" (`memory/HYGIENE.md:577-580`): the trailing `@rev-N` sentence becomes the
  grammar above, required on a `spec-audit` record dated on or after `SPEC_AUDIT_PIN_CUTOFF`, and
  recorded but never validated on any other record. Check 21's entry
  (`memory/HYGIENE.md:443-451`) gains one sentence naming the branch.
- M4 (`memory/guides/BUILD-METHOD.md:139-140`): the binding line reads
  `**Serves:** spec-audit <each id you reviewed>@rev-<the revision you read>`. The file measures 29326
  bytes of its 30720 budget, PINNED 2026-10-21 by `wc -c`.
- Each edit lands in `tools/memory-tree/HYGIENE.template.md` and
  `tools/memory-tree/BUILD-METHOD.template.md` too, graded by `kit/dogfood doc parity`.

### S8 · the docs rule

`docs` is inserted before `security` in the builder's and the spec reviewer's `rules:` lines, and
after `class` in the diff reviewer's. `render_charter_blocks` renders section 1 lines in charter
order whatever the list order (`tools/roles/roles_lib.py:299-301`), so each render gains one line,
the charter's `[docs]` rule, under its `### Charter rules` heading. The tag is bare,
as the spec writer's already is (`tools/roles/agents/gov-spec-writer.agent.md:9`). The renders come
from `bash tools/roles/adopt-roles.sh --scaffold`, and the catalogue region from
`python tools/roles/check_roles.py --write`, its documented writer (`tools/roles/check_roles.py:9-10`).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `renderAuditBinding` | function, `tools/workflows/tier2-review.js` | `js.function`, OK |
| `read_spec_revs` | function, `tools/memory-tree/gen_build_index.py` | `py.function`, OK |
| `derive_past_pin_ids` | function, `tools/memory-tree/gen_build_index.py` | `py.function`, OK |
| `pins` | key of a `read_bindings` record | none |
| `P`, `Q` | `--print-bindings` row kinds | none |
| `SPEC_AUDIT_PIN_CUTOFF` | conf key | none |
| `id`, `rev` | spec-audit subject fields | none |

### Migration

None. Records dated before the cutoff keep their unpinned lines and are never re-read as owing a
pin. On the landing day the arm grades zero records, which its `Q` row announces.

### Rollout

The landing turns both writers to pinned lines at once. This build's own audit stage runs before
this unit is built, so its audit records are unpinned and dated before the cutoff F4 derives. The
first pinned records are the next build's.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/unattended-build.test.sh`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`
- `tools/memory-tree/BUILD-METHOD.template.md`
- `memory/guides/BUILD-METHOD.md`
- `tools/memory-tree/.memory-tree.conf.example`
- `tools/memory-tree/kit.toml`
- `.memory-tree.conf`
- `tools/roles/agents/gov-builder.agent.md`
- `tools/roles/agents/gov-spec-reviewer.agent.md`
- `tools/roles/agents/gov-diff-reviewer.agent.md`
- `.claude/agents/gov-builder.md`
- `.claude/agents/gov-spec-reviewer.md`
- `.claude/agents/gov-diff-reviewer.md`
- `tools/roles/README.md`

Existing suite arms that hand a spec-audit subject or a resolver return without `rev` and expect it
to proceed gain `id` and `rev`; that is part of the two workflow suites' edits above.

### Alternatives rejected

- **The synthesis agent reads each header and composes the pins.** The harness has no filesystem,
  and its own comment records that a prompt-held count did not hold under a merging synthesis
  (`tools/workflows/tier2-review.js:1801-1812`). A literal the harness renders cannot drift that way.
- **The pin as the blob instead of `rev-N`.** The record already names each blob on its subject line,
  and the clause, the deviations instrument and the build index all speak revisions.
- **The cutoff filter in the shell, as `RECORD_SERVES_CUTOFF`'s is.** It would put half the predicate
  where no pass can observe it, since the hygiene engine is a gate leg no role agent may run. The
  generator holds the predicate and the shell only fails on its rows.
- **Not refusing a pin above the header.** That pin would read as audited forever, the false pass
  the unaudited reading exists to remove.

## 5. Production-readiness checklist

- security — no new write path. The ids reaching the synthesis prompt are refused unless they match
  an anchored id grammar, so no control character or newline reaches a prompt line.
- perf / scale — one header parse per tracked spec in `--print-bindings`, through the parser the
  render already runs; no new process.
- error / empty / loading states — a malformed cutoff exits 2 naming the key; a missing `Q` row reds;
  a blank cutoff and a zero graded count are both announced, never silent.
- observability — the stderr line names the graded count and the cutoff on every run, and the build
  index names how many unit ids carry a pin whenever none is past it.
- risks — nothing reds a later removal of `docs` from the three `rules:` lines; the renders follow
  the sources, and `roles render wiring` grades only that agreement. A pin below the revision truly
  read makes a spec read unaudited, the safe direction.
- testing — the pass probes each half by a scratch fixture or an extracted prelude; the four suite
  arms in §7 are observed RED then GREEN by the main loop at the close.
- migration — none: forward-only by filename date, as §4 Migration says.
- user docs — none owed: §3 names the help page read and why it does not change.

## 6. Acceptance criteria

- **AC1** — When a scratch node probe evaluates the prelude of `tools/workflows/tier2-review.js`, cut
  the way `tools/workflows/tier2-review.test.sh:70-92` cuts it, with `kind: 'spec-audit'` and the
  subject `{path: 'a.md', blob: 'abc1234', id: 'TOOL-x-1'}`, it throws naming `rev` at round 1 and at
  round 2. With `rev: 0`, `rev: '2'`, `id: 'x-1'` or two subjects sharing an id, each throws naming
  its field. With `{path: 'a.md', blob: 'abc1234', id: 'TOOL-x-1', rev: 2}` it proceeds.
  Red when: the refusal is deleted and the rev-less subject proceeds.
- **AC2** — When the same probe calls `renderAuditBinding` on two subjects pinned `TOOL-x-1` rev 3
  and `TOOL-x-2` rev 1, it returns exactly `**Serves:** spec-audit TOOL-x-1@rev-3 TOOL-x-2@rev-1`;
  and `grep -c 'renderAuditBinding(subjects)'` finds the call in the synthesis prompt of both
  `tools/workflows/tier2-review.js` and `tools/workflows/tier2-review.template.js`.
  Red when: the spec-kind sentence still asks for "every unit id the reviewed spec set defines".
- **AC3** — When a scratch AsyncFunction run of `tools/workflows/unattended-build.js`, the shape
  `tools/workflows/unattended-build.test.sh:164-237` uses, has its resolver stub return
  `{path, blob, tree, rev: 2}` for unit `TOOL-x-1` and its callee stub a clean round, the callee's
  `subjects` carry `id: 'TOOL-x-1'` and `rev: 2`, and the returned `nextAction` carries
  `**Serves:** spec-audit TOOL-x-1@rev-2`. A resolver entry with no `rev`, and a caller-supplied
  subject with no `id`, are each refused naming the field.
  Red when: the clean-round line is still built from the bare `owed` ids.
  cost: a scratch harness of about 80 lines, modelled on that suite's stub agents.
- **AC4** — When `cmd_print_bindings` runs in-process over a fixture git repository whose
  `.memory-tree.conf` sets `SPEC_AUDIT_PIN_CUTOFF="2026-01-01"`, with spec `TOOL-tPin-1` at rev-2, it
  prints one `P` row for a 2026-02-01 `spec-audit` record naming `TOOL-tPin-1`, one for a record
  pinning `TOOL-tPin-1@rev-5`, none for one pinning `@rev-2`, none for an unpinned `diff-review`
  record, none for an unpinned `spec-audit` record dated 2025-12-31, and `Q` with 3 graded. With the
  key blank it prints no `P` row and `Q` with 0 and `off`. With the value `soon` it exits 2 naming the
  key. `read_bindings` gives the `@rev-2` record `pins == {'TOOL-tPin-1': 2}`.
  Red when: the `P` branch is removed and the unpinned 2026-02-01 record prints no row.
  fixture: a git repository built under `%TEMP%` with a short name, as the generator's own selftest
  fixtures are built; the tree holds none today.
- **AC5** — When the hygiene engine runs over the AC4 fixture with the cutoff set, check 21 fails
  naming the unpinned and the over-pinned records and prints `the audit-pin arm graded 3`; with a
  generator that prints no `Q` row it fails naming the missing row; with the key blank it prints
  `the audit-pin arm is off`. The pass observes `bash -n tools/memory-tree/check-memory-hygiene.sh`
  and AC4's rows.
  Red when: the branch reads the `P` rows without `extract_graded_rows`, so a record the legacy
  registry lists is failed.
  permission: the hygiene engine is a gate leg no role agent may run, so the branch itself is
  observed through the hygiene suite's `New arm:` line in §7, by the main loop at the close.
- **AC6** — When `render_region` renders the fixture build from `collect` over the AC4 fixture with
  the spec moved to rev-3 and its highest pin at rev-2, the region carries
  `Ids whose spec moved past its audited revision: TOOL-tPin-1@rev-2.`; with a pin at rev-3 it
  carries `none — 1 of 1 unit id(s) carry a pin.`; with no pinned record, `none — 0 of 1`.
  Red when: the line is absent, or a spec past its pin renders `none`.
- **AC7** — When `grep -n '^SPEC_AUDIT_PIN_CUTOFF=' <conf>` runs over `.memory-tree.conf` and
  `tools/memory-tree/.memory-tree.conf.example`, gov's value is a date strictly after the newest
  `spec-audit` record filename date on every ref at the build commit, read by the command the comment
  above it records, and the example's value is `""`. And `grep -c SPEC_AUDIT_PIN_CUTOFF` over
  `tools/memory-tree/kit.toml` prints 1.
  Red when: gov's value is on or before that newest date, so a record in flight reds at its merge.
- **AC8** — When `grep -n 'SPEC_AUDIT_PIN_CUTOFF'` runs over `memory/HYGIENE.md` and
  `tools/memory-tree/HYGIENE.template.md`, each file names the key in "Record bindings" and in
  check 21's entry. A `grep -n` for `@rev-<the revision you read>` finds M4's binding line in
  `memory/guides/BUILD-METHOD.md` and `tools/memory-tree/BUILD-METHOD.template.md`; and
  `wc -c memory/guides/BUILD-METHOD.md` prints at most 30720.
  Red when: a template is edited and its dogfood copy is not, so one grep finds the key and the
  other does not.
- **AC9** — When `grep -c '^- \[docs\]'` runs over `.claude/agents/gov-builder.md`,
  `.claude/agents/gov-spec-reviewer.md` and `.claude/agents/gov-diff-reviewer.md`, it prints 1 for
  each; `python tools/roles/render_agents.py --check` exits 0; and the three rows of the catalogue in
  `tools/roles/README.md` list `docs`.
  Red when: a `rules:` line lacks `docs`, so its render prints 0, or the render was not re-run, so
  `--check` names the file as drift.

## 7. Gates

`kit/dogfood doc parity` · `check-wiring self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `transition-audit arms` · `straggler-guard arms` · `memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `harness arms (fail branches armed or pinned)` · `testsuite counts (every bar self-test prints one)` · `build-method size` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 · a spec-audit subject with no rev, and the spec-kind synthesis prompt carrying no pinned binding line, each staged against the base harness · FLOOR_ASSERTIONS in that suite, raised by the arms added
New arm: tools/workflows/unattended-build.test.sh · covers AC3 · a resolver return with no rev, and a clean round whose instruction binds bare ids, against the base harness · that suite's assertion floor, raised by the arms added
New arm: tools/memory-tree/gen_build_index.py selftest · covers AC4 AC6 · an unpinned spec-audit record at the cutoff, a pin above its header and a spec past its pin, against the base generator · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC5 · a fixture tree holding an unpinned spec-audit record dated at the cutoff, and a generator stub printing no Q row · that suite's assertion floor, raised by the arms added

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a
  legal status?** Probe: `STATUS_TOKENS` in `tools/memory-tree/tree_lib.py:25`, which the header
  regex `HDR_RE` (`tools/memory-tree/gen_build_index.py:171-175`) joins. Observation: the set is
  `OPEN SPECCED INPROGRESS BLOCKED DEFERRED CLOSED WONTDO`, and `DRAFT` is not in it, so a `DRAFT`
  header parses as no header and the unit reads MISSING. Liveness: the probe reads a tuple that would
  carry `DRAFT` if the vocabulary admitted it. RESOLVED (agent, 2026-10-21, delegated): `OPEN`, the
  token `memory/TEMPLATE-SPEC.md` gives drafting.
- **F2 — One unit, or split the pin, its check 21 arm and the docs lines into units of their own
  (M2's one mechanism per spec)?** Options: (a) one unit, as the roster row and the clause bind them;
  (b) three units; (c) two, the pin and the docs lines. Every option meets every stated criterion. The
  check 21 arm is the grammar's own enforcement and the docs half adds no mechanism: it is a value in
  an existing declared field, rendered by the existing renderer. (b) and (c) add ids, roster rows, a
  deviation record and a split carry, so they leave more open. RESOLVED (agent, 2026-10-21,
  delegated): (a), by M3's tie-break on fewer open questions, rung 3.
- **F3 — Which readers treat a revision past its pin as unaudited?** Options: (a) the build-index line
  of S5, with the pins exposed to `TOOL-dTrueNorth-4`; (b) that, and the `specs-audited` term in the
  unattended driver. Both satisfy the clause, which states no reader. (b) edits `tools/unattended/`,
  making this a second driver-changing unit before unit 7, and its arm could not be observed at this
  landing, whose unattended suites README rule 8 waives. It also opens how this build's own unpinned,
  pre-cutoff audit records would read at `--close`. RESOLVED (agent, 2026-10-21, delegated): (a), by
  M3's tie-break on fewer open questions, rung 3; (b) is the ask §3 Edges hands off.
- **FACT-QUESTION · F4 — What date does `SPEC_AUDIT_PIN_CUTOFF` take?** Probe: the relation
  `.memory-tree.conf:295-305` records, over review records: `git for-each-ref` over every local and
  remote head, `git ls-tree -r --name-only` on each under `memory/builds`, the newest
  `<date>-review-` prefix, against `git log -1 --format=%cs`. Observation, 2026-10-21 on node d: the
  newest review record on any ref is dated 2026-10-20, and this run's audit stage writes records dated
  2026-10-21 before this unit is built. Liveness: the probe returns a later date whenever a later
  record exists on any ref. RESOLVED (agent, 2026-10-21, delegated): the day after the later of
  that newest date and the setting commit's day, re-derived at the build commit and at landing, so
  2026-10-22 at the earliest.
- **F5 — The carriers this unit changes need veto 2 lifted; does the build's grant cover each?**
  The clause names the Serves-line pin, the unaudited reading and the three rule lines, and
  `PLAY-dClosedLoop-3` grants the governance-carrier changes a build's own clauses name. RESOLVED
  (agent, 2026-10-21, delegated): covered, rung 3.
  grants: PLAY-dClosedLoop-3 the spec-audit pin grammar in memory/HYGIENE.md and M4's binding line, the subject contract of tier2-review.js and unattended-build.js, check 21's audit-pin arm, and the docs tag on three role rule lines

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft, from the packet's Items 5, the brief's S7, and the two record
  writers and four Serves readers read at base `271aa59de`.
- rev-2 · 2026-10-21 · §3 · the Edges block gains a hands-off to each unit the round-1 spec audit
  promoted against this one, TOOL-dTrueNorth-9, TOOL-dTrueNorth-13, TOOL-dTrueNorth-14 and
  TOOL-dTrueNorth-16, the mirror of its consumes-from; no other section moves.

## 10. Reuse audit

The seams extended are the ones check 21 and the build index already run on: `read_bindings` and
`_expand_ids` (`tools/memory-tree/gen_build_index.py:599-697`), `cmd_print_bindings` (:700-735),
check 21's branches and `extract_graded_rows` (`tools/memory-tree/check-memory-hygiene.sh:1324-1460`),
`render_region` and `_render_wrapped_ids` (`tools/memory-tree/gen_build_index.py:1377-1526`), the
subject validator and synthesis prompt of `tools/workflows/tier2-review.js`, the resolver and
clean-round writer of `tools/workflows/unattended-build.js`, and `render_charter_blocks`
(`tools/roles/roles_lib.py:284-303`). No new parser, row grammar or renderer.
`python tools/codebase-map/reuse_lookup.py` over the phrases "pin the spec revision an audit record
read on its binding line" and "classify each record binding line and its ids" ranked generic name
stems (`read`, `read_text`, `records`, `audit`) and named none of these seams, so they were found
by reading the source. `python tools/memory-recall/query.py` returned the phase-0 revision's
finding that `memory/HYGIENE.md:578` admits a pin "recorded and never validated", which disagrees
with source in one word: `_expand_ids` drops the pin, so it is recorded only in the file's bytes.
It returned the execution plan's note that the harness writes no pin (`tools/workflows/tier2-review.js:1794-1795`),
which agrees with source, and `TOOL-aProbedUnit-12`'s finding that a clean round writes no record,
which agrees and is why the build harness is the second writer here.

Recall terms used: spec-audit Serves binding rev-N pin record check 21 unreviewed revision audited
