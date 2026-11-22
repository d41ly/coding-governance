# TOOL-dTotalRecall-25 deviation 253 — the fence arm's refusals the spec's lists do not name

**Serves:** deviation TOOL-dTotalRecall-25

- **Departs from:** `TOOL-dTotalRecall-25@rev-6` [§2 S3, S4, S7]
- **Hand-off:** spec-to-code
- **Before:** S3 lists the plan's reds as a stream with no units, a unit with no `order`, an `order` outside the `ORDER_RE` grammar, a unit id in two streams, and a missing or unparseable fence; S4 states the unarmed rule for a typed `fence` row and is silent on an untyped one, on a validator that raises, and on what the count line says for a row whose validator does not resolve; S7 names `--form fence` with `fields` as the default and is silent on any other `--form` value.
- **After:** `tools/memory-tree/record_kinds.py#check_stream_plan` also reds a fence holding no `[[stream]]` table, a stream `name` outside `build_records.py#SEG`'s shape (the shape S2 states), and a unit naming no `id`; `#check_fence_records` reds an untyped `fence` row whose home matches no tracked record, the rule the module already states for any other empty population, and turns a validator that raises into one red naming the record; `#check_record_kinds` counts a row whose validator does not resolve `<kind> fence 0 graded`; `#add_record_kind` exits 2 writing nothing on a `--form` that is neither `fields` nor `fence`. The function `#scan_fence_records` holds the population both the arm and the count line read, minted under §4 "Inventory"'s rule that each further function is asked of the lexicon.
- **Cause:** builder discovery
- **Reason:** a plan with no stream, or an untyped fence row with no record, would otherwise read green while grading nothing; a raising validator would abort the leg instead of naming the record; and `new` writes only the two forms whose rows it can make conforming.
- **Evidence:** the pass commit of TOOL-dTotalRecall-25; `record_kinds.py --fixture` and its `stream-*` plants over the worktree, and a probe of `new` over a scratch fixture refusing `--form header`.
- **Risk:** stricter
- **Approver:** author, under the build's `author-recorded` value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-25
