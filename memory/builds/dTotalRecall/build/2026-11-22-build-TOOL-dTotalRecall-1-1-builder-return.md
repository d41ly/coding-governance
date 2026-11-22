**Serves:** research TOOL-dTotalRecall-1

# TOOL-dTotalRecall-1 build pass 1 — the builder's return (DIVERGENCE)

The gov-builder return of `unattended-unit.js` run `wf_78b7bd37-30d`, at base `bd39b0a7f`, saved verbatim. Nothing was committed; the draft is a patch under the session scratchpad.

## why

DIVERGENCE: §4 "The rows" gives each typed kind the home `memory/builds/*/build/*-build-*-<kind>-*.md`. On the tree at bd39b0a7 that glob matches records that are not of that kind, and §6 cannot hold as written because of it.

(1) The `probe` home matches `memory/builds/aQuenchedHarness/build/2026-09-08-build-TOOL-aQuenchedHarness-11-probe-design.md`, which `build_records.py#derive_record_name("probe")` does not match. So probe's population is 1, not empty, and AC8's required `probe: unarmed — no record yet` line can never print. The S4 rule "a path a typed kind's name grammar matches is graded by that kind's row alone" does not take this file out, because no typed grammar matches it.

(2) The `acceptance` home matches all 1167 tracked `*-<n>-acceptance-ledger.md` records (journal-kind ledgers that HYGIENE "Acceptance ledger" describes). None of them is a typed acceptance record (DERIVED, a probe of the draft's `scan_legacy_records` at bd39b0a7). Seeding the legacy ledger tolerates the existing ones. But the acceptance ledger this brief requires in the pass commit, `2026-11-22-build-TOOL-dTotalRecall-1-1-acceptance-ledger.md`, is written after the seed. It would be graded as an `acceptance` record with no Sha, Writer or Caused-by, so AC1's `--check` exit 0 at the pass tip fails. The only way round it is to seed after writing it, which launders it, and every later unit's acceptance ledger would then red the `record-kinds` leg.

(3) §4 says "Eight hold no tracked record yet". By name grammar it is nine: exception, disposition, acceptance, transition, recommendation, gate-health, card, probe-trigger, probe.

What §4 and S4 would have to say: a typed row grades only the paths its `derive_record_name` grammar matches. Or the typed homes are narrowed so they cannot match a suffix, for example `memory/builds/*/build/*-build-*-<kind>-[0-9]*.md`, which matches neither `-probe-design.md` nor `-acceptance-ledger.md`. The eight-count line should also be corrected.

A smaller files-touched gap I already dealt with, not part of the divergence: the `kind.record-kind` usage change re-renders `help/reference/kinds.md` (generated from `tools/playbook/references.toml`, with a usage hash). It was missing from Files touched, and I declared it with `--dispatch`, which accepted it. The re-dispatch should keep it.

## summary

Nothing was committed. TOOL-dTotalRecall-1 stops on a spec divergence: as §4 writes the typed kinds' `home` globs, AC1 and AC8 cannot both hold.

**What I did before stopping**
- Base is bd39b0a7fbd27f15b561997f8e353d9c27c1443a. `--brief` reported the brief already recorded.
- I checked the spec's claims against the tree. They hold except the three in `why`: `TYPED_RECORD_KINDS`, `build_records.py#KINDS` (each `required` tuple is a pure literal), the step gate's `--fixture --plant`/`--with-row`, the script form of `edge_grammar.read_native_members`, the `[[ledger]]` grammar and `seed --population`, `leg_factory.py new --exempt`, `core.py#check_kind_row`, and `PROJECT_REGISTRY_EXTRA`.
- Every inventory name passed the naming lexicon's `--suggest --as py.function`.
- I declared `help/reference/kinds.md` with `--dispatch`, which accepted it.

**Draft and what it showed**
- I drafted `tools/memory-tree/record_kinds.py` and generated the 25-row `tools/memory-tree/record-kinds.toml`.
- Each fixture plant ran once through `python record_kinds.py --fixture [--plant <case>]`. This stands in for the `record-kinds` leg's `--selftest` arm.
  - Exit 1, each red line naming its subject: `writer-missing`, `check-unknown`, `source-drift`, `factory-kind-unrowed`, `field-missing`, `region-edited`, `gap-unresolved`.
  - Exit 0: the green fixture and `field-missing-legacy`.
- `--check` over the real tree finished in under 2 seconds.
- A population probe of the draft found the overlaps: the `acceptance` home matches 1167 acceptance-ledger records and the `probe` home matches one probe-design record. That is the divergence in `why`.
- Away from those two overlaps, no existing record misses a field or carries one out of order.

**State of the tree**
- I saved the draft as C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/TOOL-dTotalRecall-1-draft.patch and removed both files. The generator script is C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/gen_registry.py.
- `memory/builds/dTotalRecall/RUN.md` stays staged with only the rows the `--brief`/`--dispatch` verbs appended, including my dispatch row for `help/reference/kinds.md`. I left it rather than revert the verb's own record.
- The two untracked TOOL-dTotalRecall-13 prompt files are not mine.

**Owed to the close, not run here (no gate, suite or bar ran in this pass)**
- Both `New arm:` RED-first observations: `record_kinds.py --check`/`--selftest`, staged by deleting one row's `writer`; and `step_gate.py --fixture --plant record-kind-schema`.
- AC3 and AC4, which need a commit for the step gate's clone.
- AC5's `adopt-memory-tree.sh --render` parity.
- The §7 legs.

`gotchas.py --for-diff` did not run, because there is no commit. No command timed out or was skipped.
