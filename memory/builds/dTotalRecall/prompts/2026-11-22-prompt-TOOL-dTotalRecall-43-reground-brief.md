**Serves:** journal TOOL-dTotalRecall-43
**Caused-by:** TOOL-dTotalRecall-43

# Brief — dTotalRecall: TOOL-dTotalRecall-43 re-grounded on the tree as built, before dispatch

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. The spec run wrote every spec DEFERRED at base `462d20f3`; 4140
commits (DERIVED, `git log --oneline 462d20f3..8b8b1374c | wc -l`) have landed since, the three parent builds
dDeclaredLoop, dWitnessedBar and dPlacedRequest among them, so each spec is re-grounded before its dispatch.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem,
so a builder can build it as written over HEAD. Where every claim already holds, change nothing and say so.

### Items

1. Read the spec whole against the code at HEAD and settle every claim the landed code has moved: every path,
   symbol, line citation, section name, count, population and edge, and every parent spec it leans on (the
   PLAY-dOrderedCharter, TOOL-dWitnessedBar, TOOL-dPlacedRequest, TOOL-dSafePassage and TOOL-dDeclaredLoop ids it
   cites): read what each parent actually landed, not what its spec planned. Re-derive each PINNED count with the
   command the spec states and re-pin it with today's date. A population the spec enumerates is re-derived, every
   new member listed in Files touched with the legs its guard names on the gates section's leg line. Cite moved
   code-file lines as `path#symbol` or blob-pinned at a commit HEAD holds, never a bare `path:line`; leave a
   carried clause token (`**Carries:**` lines) byte-identical.
   What is built so far, CLOSED: TOOL-dTotalRecall-1 (the record-kind registry `tools/memory-tree/record-kinds.toml`,
   `record_kinds.py`, `LATER_COLUMNS`; its ledger in `tools/govkit/registry.toml`, never the shipped `kit.toml`), -13, -18
   (`tree_lib.py#resolve_kind`; the lexicon refuses `canonical_kind`), -16, -25, -5 (the slug grammar), -54
   (`id_grammar.py#parse_id_parts`), -38, -4 (`gen_build_index.py`'s declared front matter), -63, -64, -44, -46, -40, -45,
   -6 (typed relations), -22 (edge cardinality, `design_lib.py#check_edge_bounds`), -3 (`tools/memory-tree/gov-claim.sh`)
   and -2 (`tools/memory-tree/gov_record.py new <kind>`, the one record write door: it refuses a kind a factory command
   writes and takes `--name` for a kind with no naming rule). TOOL-dTotalRecall-7 (order 13, CLOSED at `5688d011a`: the ask door with its required
   `--sev <LEVEL> <why>` and `--family`), -11 (order 14, CLOSED at `71ce746a0`: the `shape-run` kind and
   `tools/memory-tree/shape_run.py`), -41 (order 14, CLOSED at `c2814ccc0`: `backlog.py#check_row_value`, the ask
   door grading its rendered rows before any mint), -10 (order 15, CLOSED at `d735e47b9`: `tag_index.py#derive_anchor`,
   a repeated heading's anchor suffixed), -42 (order 15, CLOSED at `53496c0d1`: the registry's `unarmed` column,
   `record_kinds.py#derive_record_kind`, rows graded by Serves kind), -19 (order 16, CLOSED at `6ea003891`: the door's
   `--caused-by` and `--edge`, `record_causes.py`; every record names a resolving `**Caused-by:**`) and -21 (order 17, CLOSED
   at `bd6fe04f8`: recall reads its rows from the shared tag index, `memory-recall` requires `playbook-render`), -36
   (`7ffe749aa`: every record writer the census found emits its cause line), -39 (`d65380330`), -51 (`30d1901d6`), -47
   (`a5f016658`: `record_causes.py --backfill`), -48 (`4d1d9899a`), -49 (`60424d69e`) and -50 (`7f51d13dd`: the census reads the
   build folders' code, `CAUSE_WRITER_PINNED`); -9 (order 18) builds now; -23, -61, -24, -67, -20, -71, -72, -17, -81, -82, -14, -15, -26 and -12 (orders 19 to 26) are re-grounded: read each spec where this
   one consumes from it. Unit 19 rev-9 lands `edge_grammar.py#read_header_edges(text, path, binding=None)` as the header
   reader's contract and puts its ledgers in `tools/govkit/registry.toml`. TOOL-dTotalRecall-8 and -37 are DEFERRED to owner
   ask TOOL-dTotalRecall-109. A §8 resolution mark is exactly `RESOLVED (agent, YYYY-MM-DD, delegated)` with nothing else
   inside the parentheses (check 12 strips code spans and refuses the rest); cite a brief after the mark. Unit 43 (order 27) is being re-grounded now; units 26 (rev-4) and 12 (rev-3) are re-grounded and DEFERRED: edit no spec but yours,
   and name in your return any edge you need from one of them.
   Unit 36 rev-4 leaves two parts for units 48 and 49 to finish (the run-record head and VIEW_HEAD's pin); unit 47 rev-3 names unit 51 as a fourth order-18 writer of record_causes.py, beside 49 and 50; unit 51's S3 premised that unit 36's S6 inserted into non-Markdown records, which rev-4 no longer does.
2. Trace behaviour, not only text: (a) run or read each acceptance criterion's command for its real exit codes and
   output; (b) grep every caller of a function the unit changes and every suite that copies the files it touches;
   (c) check each new rule against the fallback its reader takes on an invalid or absent file; (d) where the spec
   names a seam (a factory, a ledger, a leg row, a class row), confirm the seam exists at HEAD with the shape the
   spec uses, and re-point the spec where a parent landed it differently.
3. Settle every unwaived spec-token hit that names this spec (`python
   tools/check-spec-tokens.py --spec <path>` lists them), each by naming the tripped leg on the gates section's leg
   line or by correcting Files touched.
4. A choice the re-ground forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return. A fork whose only survivor needs a new
   external dependency or a governance-carrier change is parked, not decided: name it in your return.
5. A `[[ledger]]` home spelled under `tools/<kit>/` reds `install-prefix (shipped surface)`; keep every home under
   `memory/project/`. A spec over its ceiling of 49152 B (PINNED 2026-11-20 by the spec size check) is tightened
   in prose you touch, never by dropping a criterion. Name every new function the spec introduces with a verb from
   `.lexicon.conf`'s VERBS table, nested helpers included. A new leg's `ceiling` clears its evidenced maximum by max(120 s, 1.0x) (PINNED 2026-11-22)
   (`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-1-deviation-15.md`), and a new surface
   class needs its `[[class]]` row in `tools/govkit/usage.toml`; every number the spec states carries an id, a
   path:line, PINNED or DERIVED on its line (`python tools/playbook/writing_practice.py check pinned-facts`).

6. A `consumes-from` edge to an unbuilt sibling needs that sibling's matching `hands-off`, or hygiene check 12 refuses both. Where the sibling's spec (DEFERRED, not CLOSED) lacks it, add that one bullet to the sibling's edges as a rev bump with a revision-log line naming this brief; that sibling spec joins your write grant for that bullet alone. A CLOSED sibling stays frozen: state the dependency in Scope and name it in your return.
7. This spec is 51974 B (DERIVED, `wc -c` at HEAD) against the 49152 B ceiling: tighten it below the ceiling with
   headroom for its records region, never by dropping a criterion; the notes below remove several clauses outright.
8. Earlier units' re-grounds and builds moved these claims; settle each against HEAD and the named spec:
   - S10/AC10 (a `requires_if` naming `code_record.py`), S29/AC29 (a code-record leg's meta-gate rows), S55/AC55, S56/AC56
     and their Files touched lean on unit 8, DEFERRED to ask TOOL-dTotalRecall-109; S11, S12 and S50 lean on a
     `tools/memory-tree/policy_value.py` nobody mints. Policy reads go through `tree_lib.py#read_policy_value` (unit 14
     rev-3 and unit 26 rev-4 read through it); AC11's grep for `policy_value` would match that name.
   - S18's cycle walker already exists as `backlog.py#scan_cycles`.
   - S3's ask-row rewrite is a no-op after unit 7 (CLOSED); S59 moves to `claimant-key` and unit 3's claim row.
   - S4's deviation-row premise is overtaken by unit 2's F7 (the door refuses a kind a factory command writes).
   - S2, S31 and S27's restamp are absorbed by unit 21 (CLOSED, `bd6fe04f8`): recall writes its rows in the shared tag
     index in its own transaction (its F5), keyed by path and blob (its F6).
   - `record_extract.py` lives in `tools/playbook/` (unit 9 F7); S13 is met by unit 9; S10 declares `record_find.py`'s
     reach into the playbook kit and memory-recall.
   - S6: unit 20 rev-5 (order 21) retags headings as `## [<anchor>]` while unit 9 reads `## [section.<seg>]` as authored;
     this unit's S6 corrects it at order 27. State the window between orders 21 and 27.
   - S48 is met by unit 14's AC7; unit 14's cache stamps the body's byte length, covering AC42 (id 58).
   - S20 mints `check_front_matter`, which unit 20 rev-5 F7 grades against `FRONT_MATTER_KEYS`, `DERIVED_KEYS` and
     `read_typed_derived_paths` until this unit merges the two graders.
   A clause a CLOSED unit already met is restated as a re-observation or retired with its reason, never rebuilt.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-43` and
`python tools/check-spec-tokens.py --spec <path>` over the spec, and fix every finding either names. Write no
numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0 for the spec; it carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-43. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

The status header keeps its status (`DEFERRED`). The write grant is
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-43.md` alone. Temporary files go under the
scratch directory the task names. Do not commit: the main loop commits the re-ground.

### Reuse

The spec's §10 seam, re-verified at HEAD.
