# TOOL-dTotalRecall-60 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-60
**Caused-by:** TOOL-dTotalRecall-60

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-3 over base
`74f2d411b` and ran each probe below on node a, 2026-11-24; a fixture is built under the system temp directory
and removed. §7's legs and its `New arm:` RED-first observations are owed to the close.

## S17's sites, recorded before AC17's probe ran

Each split line is the text its function holds at `7047890d5`, and the same at `462d20f3` unless the row says otherwise.

- `tools/memory-tree/backlog.py#derive_verdicts` at `7047890d5` — `` slug = ask.id.split("-")[1] if ask.id.count("-") >= 2 else "" `` (DERIVED 2026-11-24, `git show` of that file at that revision)
- `tools/memory-tree/backlog.py#derive_ready` at `7047890d5` — `` if len(rows) != 1 or rows[0].slug != (ask_id.split("-")[1] if ask_id.count("-") >= 2 else ""): `` (DERIVED 2026-11-24, `git show` of that file at that revision)
- `tools/memory-tree/backlog.py#build_ask_sort_key` at `7047890d5` — `` parts = ask.id.split("-") `` (DERIVED 2026-11-24, `git show` of that file at that revision)
- `tools/memory-tree/gen_build_index.py#build_grade_row` at `7047890d5` — `` ask_id.split("-")[1] if ask_id.count("-") >= 2 else ask_id) `` (DERIVED 2026-11-24, `git show` of that file at that revision)
- `tools/memory-tree/gen_build_index.py#cmd_new_build` at `7047890d5` — `` ids.sort(key=lambda i: (i.split("-")[1], i.split("-")[0], int(i.rsplit("-", 1)[1]))) `` (DERIVED 2026-11-24, `git show` of that file at that revision)
- `tools/memory-recall/check-recall.py#derive_probe_labels` at `7047890d5` — `` if i.split("-")[1] != spec["slug"] and i not in inside] `` (DERIVED 2026-11-24, `git show` of that file at that revision)
- `tools/memory-recall/query.py#measure_answer_used` at `7047890d5` — `` seg = rid.split("-") `` (DERIVED 2026-11-24, `git show` of that file at that revision)
- `tools/drift-audit/drift_report.py#_parse_slug` at `7047890d5` — `` parts = uid.split("-") `` (DERIVED 2026-11-24, `git show` of that file at that revision)
- `tools/memory-tree/migrate_backlog.py#build_id_sort_key` at `7047890d5` — `` parts = ident.split("-") `` (DERIVED 2026-11-24, `git show` of that file at that revision)
- `tools/memory-tree/migrate_backlog.py#read_slug` at `7047890d5` — `` parts = ident.split("-") `` (DERIVED 2026-11-24, `git show` of that file at that revision)
- `tools/branch-reconcile/branch_reconcile.py#derive_names` at `7047890d5` — `` names |= {i.split("-")[1] for i in list(names)} `` (DERIVED 2026-11-24, `git show` of that file at that revision)
- `tools/memory-tree/gen_build_index.py#render_spec_skeleton` at `7047890d5` — `` header = (f"**Status:** OPEN · rev-1 · {today} · node {spec_id.split('-')[1][0]} · Tier-{tier} " `` (DERIVED 2026-11-24, `git show` of that file at that revision)
- `tools/memory-tree/row_grammar.py#scan_records` at `7047890d5` — `` "slug": rid.split("-")[1]}) `` (DERIVED 2026-11-24, `git show` of that file at that revision)

Apart, held by no line of `462d20f3`:

- `tools/policy/check_policy.py#derive_run_kind` at `7047890d5` — `` if not any(a not in disposed and a.split("-")[1] == build for a in asks): `` (DERIVED 2026-11-24, `git show` of that file at that revision)

## The ledger items

- S17's thirteen sites and the one apart are the section above, by file and line text (DERIVED 2026-11-24, `git show`).
- S18's figure: the tip's `journal` count is 5108 (DERIVED 2026-11-24, the `S` rows of `python tools/memory-tree/gen_build_index.py --print-bindings` whose third TAB field is `journal`).
- S29's count: unit 53's minors that re-report a high unit's defect number nine, ids 13, 23, 2, 42, 15, 4, 43, 51 and 12 of the round-1 audit of units 36 to 43, under five high units as that audit of units 44 to 53 groups them: 44 with 45, 46, 47, 49 and 52 (TOOL-dTotalRecall-60 S29; `2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1`, its id 11).
- S32's citations of unit 51, corrected: `BIND_RE` is `tools/memory-tree/tree_lib.py@462d20f3:410-412` and `record_paths` is `:421` at that revision (DERIVED 2026-11-24, `git show` of that file at `462d20f3`).

**Evidences:** TOOL-dTotalRecall-60
- AC1 — `asbuilt_view.py --check` — exit 0, `findings 0`, and the instrument's own `--check` exit 0, `findings 0` (DERIVED 2026-11-24, this probe).
- AC2 — `Caused-by` — the spelled regex over the view matches 0 lines (DERIVED 2026-11-24, a Python probe of the same pattern). Its other half, `bash tools/memory-tree/check-memory-hygiene.sh --only 9`, is a gate leg and is owed to the close.
- AC3 — `--readers` — over the throwaway git tree `python id_grammar.py --readers` listed the line marked in the old spelling and not the one carrying the census marker (DERIVED 2026-11-24, this probe; the tree under the system temp directory, for its short path). The suite's plants `old-marker` and `new-marker` are owed to the close.
- AC4 — `git grep -n "slug-grammar: kept" -- tools` — printed nothing, exit 1, at the tip with the plants in place (DERIVED 2026-11-24, this probe).
- AC5 — `legacy-records` — the spelled grep printed nothing, exit 1 (DERIVED 2026-11-24, this probe).
- AC6 — `tomllib` — `registry.toml` holds one `record-kinds-legacy` ledger table and no `legacy-records`; `kit.toml` holds neither (DERIVED 2026-11-24, this probe).
- AC7 — `render_spec_skeleton(` — 9 sites, the definition with `slug` after a bare `*`, `cmd_new_spec` and seven self-test calls, every call read to its closing parenthesis and passing `slug` (DERIVED 2026-11-24, this probe).
- AC8 — `TOOL-x` — `gov_record.py new spec TOOL-x --tier 2` exited 2, refused naming `TOOL-x`, and the status listed no new file (DERIVED 2026-11-24, this probe).
- AC9 — `ARCH-aFix-3` — the header reads `node a` (DERIVED 2026-11-24, this probe).
- AC10 — `git merge-base --is-ancestor 74af3faa4 c6fcf603b` — exit 0, and unit 45's spec holds 1 `consumes-from` line naming TOOL-dTotalRecall-54 (DERIVED 2026-11-24, this probe).
- AC11 — `backfill-selection` — its `check` lines name the `-unbound.md` record under `causes` and no other, and the plant printed `PASS`, exit 0 (DERIVED 2026-11-24, this probe).
- AC12 — `a5f016658` — the spelled `git diff-tree` printed one line, `A` for unit 47's own ledger (DERIVED 2026-11-24, this probe).
- AC13 — `other-build-causeless` — `--backfill --build fRoot` wrote the `fRoot` record, listed the `fClaim` one `not backfilled` with `another build's record`, the status named the first alone, and the plant printed `PASS`, exit 0; with the plant's build unset in the probe process it printed FAIL and exited 1 (DERIVED 2026-11-24, this probe).
- AC14 — `TOOL-d2026-10-26ClosedLoop-3` — in a clone of `74f2d411b` flipped as unit 45 AC1 makes it, `gov_record.py new spec` refused, exit 2, on the build lease, `the clone does not declare exactly one remote`, neither the usage nor the id refusal; with a scratch bare repository as its one remote, its `main` the flipped commit, the same command exited 0 and wrote the spec, its header reading `node d` (DERIVED 2026-11-24, this probe). The added bare remote is a fixture detail the criterion does not state; this pass changes nothing that command reads.
- AC15 — `grammar_for(root).families` — in a scratch tree declaring `RECALL_CITED_FAMILIES="ZED"` the families read TOOL and ZED, `parse_id_parts` returned each, and an ARCH id raised `ValueError` (DERIVED 2026-11-24, this probe).
- AC16 — `TOOL-d119` — it and `TOOL-001` each raised `ValueError` (DERIVED 2026-11-24, this probe).
- AC17 — `7047890d5` — the tip's `--readers` over a scratch checkout of it, a shared clone in the place of a worktree, listed each of the thirteen site texts with its file, and `derive_run_kind`'s apart (DERIVED 2026-11-24, this probe, run after the section above was written).
- AC18 — `--print-bindings` — the count is the ledgered 5108, and the spelled `git grep` printed nothing, exit 1 (DERIVED 2026-11-24, this probe).
- AC19 — `pinned-ask-closed` — its `--check` exited 1 with one red naming the row, its ask and `not live: it reads WONTDO at HEAD`, and the plant printed `PASS`; with `record_causes.py#check_ask_live` answering None in the probe process it printed FAIL, its check exiting 0. At the tip `python record_causes.py --cause-writers` printed the PLAY-dClosedLoop-1002 row `filed`, no red, exit 0, in 13 s (DERIVED 2026-11-24, this probe).
- AC20 — `backfill-selection` — the `-probe.sh` record held one `# **Caused-by:** TOOL-fRoot-1` line, its second, after both backfills, the second printed `0 backfilled`, and `bash -n` over the same three lines exited 0 (DERIVED 2026-11-24, this probe).
- AC21 — `check_cause_line(4, line, ["X-xFixtureRun-1"])` — no finding for an empty line, one for `X-xFixtureRun-9` (DERIVED 2026-11-24, this probe).
- AC22 — `watch:` — the newest `last-audit` commit and the newest commit over the watched paths are both `6db81d070` (DERIVED 2026-11-24, this probe), and this pass touches no watched path.
- AC23 — `govkit:generated` — the spelled grep printed nothing, exit 1 (DERIVED 2026-11-24, this probe).
- AC24 — `split-maxsplit-two` — its line and `rsplit-bare`'s were listed, as were an unindexed `.split("-", 1)`, an unindexed `.rsplit("-", 1)` and `.rsplit("-", 2)[0]`; none of the four safe shapes, nor `.rsplit("-")[0]` or `.rsplit("-", 1)[-1]`, was; at the tip `--readers` printed the 16 lines it printed before the first edit, none of `check_policy.py` or `census.py` (DERIVED 2026-11-24, this probe).
- AC25 — `X-xFixtureRun-1..3` — `X-xFixtureRun-2` returned no finding and `X-xFixtureRun-4` one (DERIVED 2026-11-24, this probe).
- AC26 — `reason-on-other-file` — exit 1 with two `RED` lines, one per planted file, neither naming the renderer, whose own line printed `kept` (DERIVED 2026-11-24, this probe).
- AC27 — `[0]` — with the `[0]` exemption cut from `_READER_SPLIT_SHAPE` in the probe process, in the place of a copy on disk, the scan of this tree listed the reads of `cmd_asks` and `render_family_view` and no line of `row_grammar.py` (DERIVED 2026-11-24, this probe).
- AC28 — `slug="xFoo"` — the header reads `node x` (DERIVED 2026-11-24, this probe).
- AC29 — `nine` — S29's line above states it.
- AC30 — `Caused-by` — the spelled grep printed a line in "The committed record"'s head paragraph and one in "The schema leg"'s (DERIVED 2026-11-24, this probe).
- AC31 — `RECORD_SCHEMA["cause_line"]` — equals `CAUSE_LINE_RE.pattern`, and the source spells that pattern 1 time (DERIVED 2026-11-24, this probe).
- AC32 — `462d20f3` — lines 410 to 412 hold `BIND_RE` and 421 `def record_paths` there (DERIVED 2026-11-24, this probe), as S32's line above spells them.
- AC33 — `write_missing_causes` — `memory/map/generated/symbols.json` holds it, and `python tools/codebase-map/gen_map.py --check` exited 0 after this pass's `--write` (DERIVED 2026-11-24, this probe).
- AC34 — `| Step | Units | Parallel |` — 141 READMEs hold the table, each with S27's line under it, and no other README holds the line (DERIVED 2026-11-24, this probe).
- AC35 — `gen_build_index.py --check` — exit 0; the packet half was observed through `python tools/chain-packet.py --check dTotalRecall`, the instrument's own `main` and bytes (TOOL-aBatchedPacket-1): exit 0, `byte compare green`, `pin arm 7 instruments, 0 findings` (DERIVED 2026-11-24, this probe).
