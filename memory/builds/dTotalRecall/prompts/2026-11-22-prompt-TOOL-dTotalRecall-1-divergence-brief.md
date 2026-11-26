**Serves:** journal TOOL-dTotalRecall-1

# Brief — dTotalRecall: TOOL-dTotalRecall-1's first build pass diverged; fold the spec to rev-7

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. The unit's first builder returned a DIVERGENCE at base `bd39b0a7f`,
recorded whole in `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-1-1-builder-return.md`.

## The brief

### Goal

Revise the spec in place as a rev-7 bump, with one revision-log line naming this brief by its file stem and the
builder return by its file stem, so the next builder can build it as written over HEAD.

### Items

1. Read the builder return whole. Its divergence: §4 "The rows" gives each typed kind the home
   `memory/builds/*/build/*-build-*-<kind>-*.md`, and that glob matches records of other kinds. The `probe` home
   matches `memory/builds/aQuenchedHarness/build/2026-09-08-build-TOOL-aQuenchedHarness-11-probe-design.md`, so
   AC8's `probe: unarmed — no record yet` line can never print; the `acceptance` home matches every tracked
   `*-<n>-acceptance-ledger.md` journal record, so the acceptance ledger each pass commit writes after the seed is
   graded as a typed `acceptance` record and AC1's `--check` reds at every later pass tip. §4's "Eight hold no
   tracked record yet" is nine by name grammar, as the return lists.
2. Settle the population rule against `tools/memory-tree/build_records.py#derive_record_name`, the one name grammar
   of a typed record. The two options the return names: (a) a typed row grades only the paths its
   `derive_record_name(<kind>)` grammar matches, the glob staying as the row's declared home; (b) the typed homes
   narrowed to a glob that cannot match a suffix, such as `memory/builds/*/build/*-build-*-<kind>-[0-9]*.md`. Decide
   it by the build method's M3 and mark it RESOLVED in §8 with the delegated mark; prefer the option that leaves one
   fact in one place (`[one-fact]`). Re-state S4, §4 "The rows", AC1, AC7 and AC8 so they agree with the choice, and
   re-derive the empty-kind count by the grammar, PINNED with today's date and the command.
3. Add `help/reference/kinds.md` to Files touched: the `kind.record-kind` usage change re-renders it from
   `tools/playbook/references.toml`, and the builder declared it with `--dispatch`. Name on the gates section's leg
   line any leg its guard trips.
4. Keep every other rev-6 decision (F5 to F7) unless the choice in item 2 forces a change; a forced change is named
   in the revision-log line. Keep the spec within its 49152 B ceiling (PINNED 2026-11-20 by the spec size check)
   counting the generated records region, which grows by two rows when this brief and the builder return are
   indexed: tighten prose you touch, never drop a criterion.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-1` and
`python tools/check-spec-tokens.py --spec <path>` over the spec, and fix every finding either names. Write no
numeric fact without an id, a path:line, PINNED or DERIVED on its line. The status header keeps `INPROGRESS`; the
write grant is the spec file alone; do not commit.

### Acceptance

Both commands exit 0 for the spec; it carries rev-7 and one revision-log line naming this brief and the return.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-1. No product code. No change to Goal or Scope intent beyond what the divergence forces.
