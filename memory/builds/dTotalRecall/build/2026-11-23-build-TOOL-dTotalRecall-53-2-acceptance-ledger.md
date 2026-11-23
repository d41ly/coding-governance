# TOOL-dTotalRecall-53 — acceptance ledger, build pass 2

**Serves:** log TOOL-dTotalRecall-53
**Caused-by:** TOOL-dTotalRecall-53

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-6 over base
`6ab7625a1` and ran each probe below at the pass tip on node d, 2026-11-23, by `python -c` calls of the
unit's own functions, its CLIs over scratch fixtures, and scratch clones at the base and at the tip under
the system temp directory. §7's legs and every `New arm:` RED-first observation are owed to the close. S20 and S32 ride with `TOOL-dTotalRecall-37` (§8 F3) and S36 with owner ask
TOOL-dTotalRecall-113 (§8 F2), so their criteria are not built here.

**Evidences:** TOOL-dTotalRecall-53
- AC1 — `i-named-reader` — `id_grammar.py --flip-probe` over a scratch clone of the tip printed `flip slug-date in-slug hyphenated · i-named-reader: ok, the census fails as it must`, listing `tools/memory-recall/check-recall.py#derive_probe_labels`'s reverted `i.split` line; the probe exited 0 with the six flips ok (DERIVED 2026-11-23, this probe).
- AC2 — `--readers` — `id_grammar.scan_readers` at the tip lists no index-0 read of `gen_build_index.py#cmd_asks` or `backlog.py#render_family_view`, and no line `_READER_SPLIT_SHAPE` matches.
- AC3 — `git grep -ohE` — the flat-era and node-scoped ids under `memory/` (209, DERIVED 2026-11-23, this probe) are each refused by the tip's `parse_id_parts`, so every re-pointed reader takes its fallback; no base split answer of any of them equals a tracked build folder, and none is an ask row of a build `BACKLOG.md`, so each reader's verdict over them is the base's. The readers' whole-output parity in a worktree at base is owed to the close's review.
- AC4 — `--backfill` — the `causeless` plant's finding reads `names no Caused-by, and its kind is no root; run record_causes.py --backfill`, and the `backfill-selection` plant printed PASS, the backfill selecting by the one `ABSENT_CAUSE` spelling.
- AC5 — `git diff` — the first three lines of `2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` equal `462d20f3`'s, no `Caused-by` among them. The `--only 9` run is the close's (`memory hygiene`).
- AC6 — `compare_to_base` — in a scratch clone of the tip, one record's `causes` row taken from `memory/project/record-kinds-legacy.txt`, `read_ledger` still read its `kind-schema` row and `compare_to_base` answered no finding (`origin/main tip`).
- AC7 — `render_census` — `migrate_backlog.py#render_census` writes `**Caused-by:** <unit_id>` as line 2, after its Serves line; it holds at HEAD (DERIVED 2026-11-23, this probe).
- AC8 — `reader-prefix` — `record_causes.run_check` at the tip lists `review_replay.py`'s `LEGACY` and `ROUND1_BINDING` literals kept with reasons opening `reader-prefix`, its docstring reworded; a probe found `LEGACY` equal to base `7b27f765`'s, 351 characters (DERIVED 2026-11-23, this probe).
- AC9 — `literal-without-cause` — `record_causes.py --fixture --plant literal-without-cause` printed `red line(s) [7]` and PASS: the second literal answered three lines below, the third four below and red; `duplicate-cause` printed `[9]` and PASS. An `ast.get_docstring` probe found no `**Serves:** ` in the four docstrings §8 F5 rewords (DERIVED 2026-11-23, this probe).
- AC10 — `render_worksheet` — line 2 is `# **Caused-by:** TOOL-dTotalRecall-53`, and `tree_lib.read_header_edges` reads its `caused-by` edge.
- AC11 — `python record_causes.py --check` — over the unit 19 fixture with a causeless record and one holding two bare `**Caused-by:**` lines, `record_causes.run_check` reported both, the second `its header is refused` naming both lines, and walked on to its orphan lines; it holds at HEAD (DERIVED 2026-11-23, this probe).
- AC12 — `cardinality-refused` — `edge_grammar.py --fixture --plant cardinality-refused` printed the record's refused line, `read 1 edges`, and PASS, no edge of it read; exit 0 (DERIVED 2026-11-23, this probe).
- AC13 — `stream-plan` — `record_kinds.check_record_kinds` at the tip reds nothing on the `stream-plan` row and prints its unarmed line with its reason.
- AC14 — `unarmed-on-disallowed-form` — the plant exits 1 naming `row stream-plan: unarmed on a 'header' row` (DERIVED 2026-11-23, this probe).
- AC15 — `shape-run` — the tip's `check_record_kinds` passes the `shape-run` row, its unarmed line printed.
- AC16 — `--flip-probe` — the six flips over the tip clone listed no marked split; the `unmarked-split` case listed `.githooks/pre-push.runlog.test.sh`'s line once its marker was stripped; `--readers` lists no split line.
- AC17 — `read_header_edges` — a counter on `tree_lib.read_header_edges` read 3 calls (DERIVED 2026-11-23, this probe) while the edge walk read the `cardinality-branch` fixture; it holds at HEAD.
- AC18 — `git ls-files` — `tools/playbook/edge_grammar.py` is tracked at the pass base, so S18 files nothing.
- AC19 — `awk-regex-alias` — the plant lists its `awk` alternation and its bare `case` pattern red; at the tip `check-memory-hygiene.sh`'s awk line is listed kept, `both tokens`.
- AC21 — `written_kind` — `derive_record_kind(path, written_kind, rows)`; a planted record `read_bindings` calls malformed reads `None` through `read_written_kinds` and gets `None`; `scan_legacy_records` classifies the tree as the base did, every row's population and other-kind set equal.
- AC22 — `pinned instrument` — the tip's census lists `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py@30a1f15b:380` kept `pinned instrument`; `grep -c resolve_kind` over `memory/builds/dClosedLoop/BACKLOG.md` prints 1, ask PLAY-dClosedLoop-1003.
- AC23 — `homeless-empty` — the tip's line reads `309 file(s) under memory/ outside builds/ · 113 homed · 196 not records · 0 homeless` (DERIVED 2026-11-23, `check_record_kinds`); `homeless-record` names its file and `homeless-empty` reds `the arm selects nothing`.
- AC24 — `msys-d-drive` — `runlog.py memory --fixture --plant` counted `msys-d-drive` 450, `dot-relative` 300 and `parent-relative` 250 bytes (DERIVED 2026-11-23, each plant's pooled row); `test_memory_dtr53_paths` holds them in the runlog selftest, owed to the close.
- AC25 — `VIEW_HEAD.format` — the call returns no `Caused-by`; it holds at HEAD.
- AC26 — `render_markdown` — it writes `render_cause_line(serves)` as the head's line 4; it holds at HEAD (DERIVED 2026-11-23, this probe).
- AC27 — `build-order` — `gen_build_index.py --write` writes the line under each build-order table; the region is in this commit's README renders.
- AC28 — `record_kinds.py --check` — `check_record_kinds` at the tip reds only the two pockets `dHomedResolver` and `history-verdicts` of this machine's common git dir, which HEAD's code reds alike (inherited, node d); `record_causes.run_check` printed `0 causeless · 0 orphan(s)` and green, its census `314 code files under tools · 24 census file(s) · 108 kept · 0 red` (DERIVED 2026-11-23); `check_edge_cardinality --registry` printed `0 line(s) refused and not counted; 0 violations`, exit 0. The legs themselves are the close's.
- AC29 — `record-kinds-legacy` — `record_causes.py --fixture` registers `record-kinds-legacy`, its fields `path`, `section` and `check`; it holds at HEAD.
- AC30 — `journal` — the grep prints nothing at the tip; the tip's `journal` count is 5086 (DERIVED 2026-11-23, the `S` rows of `gen_build_index.py --print-bindings` whose kind cell is `journal`), beside `TOOL-dTotalRecall-18`'s frozen 1,443.
- AC31 — `gotchas.py --for-paths` — over this unit's spec path and a dClosedLoop spec path it lists `a-cmd-percent-var-in-a-bash-criterion-stays-literal`, and over `tools/memory-tree/tree_lib.py` it does not.
- AC33 — `derive_path_key` — `memory_measure.py` spells it 6 times and `def derive_folded_path` 0 (DERIVED 2026-11-23, `grep -c`).
- AC34 — `census: kept` — all 9 rows of `CAUSE_WRITER_KEPT` and `ALIAS_COMPARE_KEPT` name a file under `memory/builds/*/build/` (DERIVED 2026-11-23, this probe), and `git grep -c` over them prints nothing; the `unmarked-writer` plant reds its unmarked literal beside a kept one, PASS.
- AC35 — `--cause-writers` — `record_causes.py --cause-writers` prints the census's lines alone, each open literal with `kept <reason>` or `red`.
- AC37 — `unarmed` — `check_shape_runs` at the tip ends its unarmed line with the `shape-run` row's `unarmed` value, and `git grep -c "no writer calls the verb yet" -- tools` prints nothing.
- AC38 — `asbuilt_view` — `git diff 462d20f3` over `tools/memory-tree/README.md` moves no `asbuilt_view` line; it holds at HEAD.
- AC39 — `alias-constant` — the tip's census lists no line of `tools/runlog/model.py`, lists `KIND_ALIASES` and `SERVES_ALIASES` kept, and the plant `alias-constant` red at its line 1 (DERIVED 2026-11-23, this probe).
- AC40 — `exits 2` — over a scratch clone, the mint stubbed: a planted append between parse and write exits 2 with the planted row kept and no ask written; a planted read-back failure exits 3 naming `memory/builds/dClosedLoop/BACKLOG.md`, the bytes as before (DERIVED 2026-11-23, this probe).
- AC41 — `SQUASH_MSG` — `check_pockets` over a scratch repository holding a planted `SQUASH_MSG` names nothing.
