**Serves:** research TOOL-dTotalRecall-25

# TOOL-dTotalRecall-25 build pass 1 — the builder's return

The gov-builder return of `unattended-unit.js` run `wf_6eff24a6-904`, at base `c2143acf3`, pass commit `a9f1e2a68`, follow-up `800177f3e`, saved in substance.

## why

TOOL-dTotalRecall-25 is built as its rev-6 spec states and committed with its spec status set to CLOSED. Every probe of the spec against the tree held, so there is no divergence. The fence red's inline triple backtick was paraphrased in a Pass: none commit after the M6 checklist selected inline-fence-swallows-the-rest-of-the-file.

## summary

Pass commit a9f1e2a68 (Pass: TOOL-dTotalRecall-25) holds the unit, with the spec status set to CLOSED. Follow-up 800177f3e (Pass: none) rewrites one acceptance ledger line that quoted a triple backtick inline; the M6 checklist flagged it.

What was built:
- `tools/memory-tree/record_kinds.py`:
  - The schema form list gains `fence` and the schema keys gain `validator`.
  - `check_row` reds a fence row with no validator or one that does not resolve, and a validator on any other form.
  - New functions: `resolve_validator` (only a bare module from this kit's own directory, its function at top level), `scan_fence_records`, `check_fence_records` (prefixes each red with `row <kind>: <path>:` and counts the row as `<kind> fence <n> graded`), and `check_stream_plan` with `STREAM_PLAN_UNARMED` beside it.
  - `new` takes `--form fence` and `--validator`. For a typed kind it writes the factory `source` and the typed `id-rule`.
  - The fixture gains a typed stream-plan row, a well-formed plan of two streams, and six stream plants. `--selftest` gains those plants, the two fence refusals of `new`, and a check that the green fixture really graded the plan (it must print `stream-plan fence 1 graded`).
- `stream-plan` joins the typed kind list in `tree_lib.py` and the factory table in `build_records.py`. The HYGIENE kind list now names it and says seventeen.
- The registry row was written by the exact `new` call in spec section 4. The view, `memory/HYGIENE.md`, `help/reference/kinds.md`, the README, `kinds.toml`, the registry header and `symbols.json` were all re-rendered or updated.
- I wrote deviation 253 (Risk: stricter) for refusals the spec did not list: a plan with no `[[stream]]` table, a stream name of the wrong shape, a unit with no id, an untyped fence row with no records, a validator that raises, and a `--form` other than `fields` or `fence`. The acceptance ledger has one line per criterion.
- Two `--dispatch` declarations were added beyond the starting set: the deviation record, and the dClosedLoop as-built view, whose deviation count the index generator moved. The first dispatch try hit its 120 s bound and recorded nothing; I ran it once more with a 590 s bound and it recorded. (DERIVED, the builder's own run)
- In the build README I staged only this unit's row, the build status line and the records count. The concurrent spec writer's rows for units 44, 46 and 63, and their spec edits (44, 45, 46, 5, 63), are left unstaged.

Checks that ran (each stands in for part of the `record-kinds` leg or for `--selftest`):
- `record_kinds.py --fixture`: green, with `stream-plan fence 1 graded`.
- Each stream plant exited 1 naming its subject: unordered, empty, order-text, unit-twice, fence-missing, validator-missing (AC2–AC4).
- A python -c probe of `check_record_kinds` on the fixture with the plan removed exited 0 and printed the unarmed line naming dIndexedDesign's planner (AC5 logic).
- A python -c probe of `new` on a fixture: the two fence refusals and four more each exited 2 with the registry bytes unchanged, and a fence row round-tripped (AC7).
- A tomllib probe of the real row (AC1).
- AC6: the tuple and table imports, the HYGIENE bullet, `read_bindings` on a scratch repo (malformed both ways, bound when correctly named), and `build_records.py --fixture --plant typed-kinds`, which exited 0 with 17 kinds bound. (DERIVED, the builder's own run)
- The naming lexicon's `--suggest` answered OK for all four new functions. All of them start with a declared verb, so `VERB_OFFENDER_PIN` does not move.

The hook refused `record_kinds.py --check` on the real tree, so these are owed to the close:
- AC1 and AC5 on the tree: `--check` exiting 0, its count line naming `stream-plan fence` and printing the unarmed line. It stays red until the stray `dHomedResolver/` pocket is moved (unit 18 §8 F2).
- The new arm's RED-first observation: `tools/memory-tree/record_kinds.py --selftest`, covering AC2, AC3, AC4 and AC7, staged red by making `check_stream_plan` accept a unit with no order, then green restored.
- The legs the gates section names: memory hygiene, memory-hygiene self-test, kit/dogfood doc parity, recall floor, recall floor arms, record-kinds, policy fixtures, playbook render selftest, govkit acceptance matrix, core kinds, help reference pages, docs. Also the `check-memory-hygiene.test.sh` arm that writes a record of every typed kind.

For the main loop: as after unit 16, the dTotalRecall packet may need re-rendering now that the as-built view's deviation count moved (2344 to 2345).
