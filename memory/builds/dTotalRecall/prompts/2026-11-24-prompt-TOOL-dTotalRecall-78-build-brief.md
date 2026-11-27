**Serves:** journal TOOL-dTotalRecall-78
**Caused-by:** TOOL-dTotalRecall-78

# Build brief — TOOL-dTotalRecall-78

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dTotalRecall's build run. Its spec run landed every spec DEFERRED at base `462d20f3`, and this run builds
  them in the build-order table's order from base `8b8b1374c`. This unit is build order 36, the second of seven, after TOOL-dTotalRecall-77. A spec writer may be
  revising another unit's spec in this working tree: stage explicit paths only, leave every file you did not write
  unstaged, and when the pre-commit hook re-renders the build README stage only your own rows.
- Built so far, CLOSED: TOOL-dTotalRecall-1 (`record_kinds.py`, `record_kinds.py new` for `fields` and `fence` rows), -13,
  -18, -16, -25, -5, -54, -38, -4, -63, -64, -44, -46, -40, -45, -6, -22 (edge cardinality: a new registry row needs its
  cardinality cell), -3, -2 (`tools/memory-tree/gov_record.py`, its `KIND_HANDLERS` table, `build_records.py#write_new_record`),
  -7 (`5688d011a`: the `ask` door, `gov_record.py`'s ask handler with `--family` and `--sev`, `build_records.py#write_seq_mint`),
  -11 (`71ce746a0`: the `shape-run` kind, `tools/memory-tree/shape_run.py`, `gov_record.py`'s `print_written`), -41
  (`c2814ccc0`: `backlog.py#check_row_value`, the ask door grading its rendered rows before any mint) , -10
  (`d735e47b9`: `tag_index.py#derive_anchor`, a repeated heading's anchor suffixed) , -42 (`53496c0d1`: the
  registry's `unarmed` column, `record_kinds.py#derive_record_kind`, rows graded by Serves kind) and -19 (`6ea003891`:
  `tree_lib.py#read_header_edges`, the door's `--caused-by` and `--edge`, `tools/memory-tree/record_causes.py`; from it on,
  every record this pass writes names a resolving `**Caused-by:**` or the record-causes leg reds), -21 (`bd6fe04f8`: recall
  reads its rows from the shared tag index) , -36 (`7ffe749aa`: every record writer the census found emits its cause line;
  `runlog/record.py`'s `render_cause_line` and `check_cause_line` minted unwired, unit 48 wires them), -39 (`d65380330`:
  the edge grammar reads headers through `tree_lib.py#read_header_edges`, `edge_grammar.py#check_header_edges`) and -51 (`30d1901d6`:
  `tree_lib.py#BIND_PREFIX` and `#HEAD_EDGE_RE`, comment-headed non-Markdown records graded by the causes and orphan checks,
  today's 139 admitted to `legacy-records` by widen-7) and -47 (`a5f016658`: `record_causes.py --backfill`, the
  verb `write_missing_causes`) and -48 (`4d1d9899a`, `5284138ed`: the run record's head admits the cause line at line 4,
  `record.py#check_cause_line` wired, `cause` in `RECORD_RULES`) and -49 (`60424d69e`: `VIEW_HEAD` back to its bytes before unit 36,
  `asbuilt_view.py` kept as a pinned instrument the census grades) and -50 (`7f51d13dd`: the census reads the build
  folders' code files, `CAUSE_WRITER_PINNED`, ask PLAY-dClosedLoop-1002) and -9 (`29b39e572`, `300ee1243`: the `record`, `section`,
  `feature`, `class` and `marker` tag namespaces, `tools/memory-tree/record_find.py` with `gov_record.py find`, `show` and
  `budget`, recall's ranking moved into `record_find.py`) and -23 (`30d52b595`: the `leg_row` table and its three readers in
  `tree_lib.py`, written inside `tag_index.py#build_index`), -61 (`778edd3a3`: the amendments to specs 53, 55, 56 and 57), -67
  (`56390bab8`: the probe reads them present), -24 (`5d632d67d`: record commits reach the change feed,
  `gov-feed.sh#add_record_events`), -20 (`c18aaf8ff`, `d0e02120b`: the journal, front-matter and retag steps, the
  scaffold verbs forwarded to `gov_record.py`, whose rendered verb shims derive their kit-relative paths at run time),
  -71 and -72 (`5e004ad39`, `35e956dc6`: unit 57's edge to unit 56 read present), and -81 and -82 (`7e151e666`,
  `f4e82dad9`: the guarded revision read, no deviation owed).
  -17 (`cb97caf03`: the map lost its replay on recall, `replay_scorer.py`'s `map-replay` instance). TOOL-dTotalRecall-8 and
  -37 are DEFERRED to owner ask TOOL-dTotalRecall-109; -14, -15 and -26 (the map renderer, its checks and the atlas) are
  DEFERRED to owner ask TOOL-dTotalRecall-111, so no `gov_map.py` exists and none is to be built. -12 (`6f7d5dd2c`: runlog's `memory` verb), -43 (`b9b6e584a`: the round-1 minors; its S19 merge moved here, unit 43 §8 F6)
  and -62 (`4975ccf29`), -52 (`926526b1c`, rev-7: ONE legacy registration `record-kinds-legacy`, home
  `memory/project/record-kinds-legacy.txt`, keyed by (`path`, `section`, `check`), the old `legacy-records` name retired,
  no `absorbs`). -53 (`6db81d070`, order 29: one census keep marker `<lead> census: kept <census> <reason>` read through
  `id_grammar.py#read_kept_reason`; the writer census grades each Serves literal), with its red-fixes `6cb81cf0c` and
  `1c93f20c2`. -59 (`47afc8937`). -55 (`5b5895a49`: `tree_lib.py#CENSUS_KEPT_PATHS` and its one reader `read_kept_rows(census, table=CENSUS_KEPT_PATHS)`,
  `read_kept_path` answering through it; `check_cause_writers` and `run_check` take `kept`; `CAUSE_WRITER_KEPT` retired).
  -56 (`798f98fc1`: the alias census's build-folder walk keeps through `read_kept_path("check_alias_compares", path)`,
  the deviations instrument's row moved into `CENSUS_KEPT_PATHS`, `ALIAS_COMPARE_KEPT` retired). -57 (`5ff76c2e2`: `tree_lib.py#KEPT_PATH_DOMAIN`, `read_kept_rows` refusing any row
  outside `memory/builds/*/build/*`; `check_alias_compares` takes `kept`, its local count `n_kept`; both censuses ask
  the table once before their build-folder walk and red the refusal). -58 (`7fd3f8e38`, rev-4: `id_grammar.py#check_marker_domain(path, text, census)` returning `(line number, finding)`
  pairs, called in the build-folder walks of `check_cause_writers` and `check_alias_compares` before any skip or keep;
  no suite runs its plant `marker-in-build-script`), -60 (`2ec3df383`, rev-3: the split census's widened shapes,
  `record_causes.py --backfill --build <slug>`, the cause line behind the Serves line's lead with `not markdown`
  dropped, `check_ask_live`, the renderer's kept reason admitted for its one file, `RECORD_SCHEMA["cause_line"]`, the
  runlog README), with red-fix `cb0e30d2e`, and -65 (`f1e11ac49`, rev-5: the keep rows in
  `memory/project/census-kept-paths.txt` named in `PROJECT_REGISTRY_EXTRA`, `tree_lib.py#read_kept_rows(census, root)`
  and `read_kept_path(census, path, root)`, the `kept` arguments and `CENSUS_KEPT_PATHS` gone, the kickoff manifest
  re-stamped in that commit, deviation 1012: `reason-on-other-file` and `marker-in-kept-script` write their fixture's
  own registry), and -68 (`7252440fd`, rev-3: the `census-kept-paths` `[[ledger]]` registration in `tools/govkit/registry.toml`,
  the rows rewritten by `write_rows`, `tree_lib.py#KEPT_FIELDS`, `read_kept_rows` through `legacy_ledger.read_rows`
  answering `{path: row}`, `read_kept_path` one row or None, the plants' `record_kinds.py#write_kept_fixture`; a row
  with a blank reason reads as keeping nothing, and no item reds it by name), and -66 (`17aac82e4`, rev-5: both build-folder walks red a keep row whose file is no hit, pinned rows included;
  `build_kept_path_re` from the conf's memory root, `KEPT_PATH_DOMAIN` retired; the pinned writer is a
  `census-kept-paths` row with a `records` glob read by `read_pinned_rows`, `CAUSE_WRITER_PINNED` and the `pinned`
  arguments gone; the `--backfill --build` refusal; `id_grammar.py#_token_cache`; `write_fixture(top, plant,
  memory="memory")`; the suite arm of `marker-in-build-script`), and -69 (`f7011dd6f`, rev-3: the manifest's stamp re-read over unit 65's commit, nothing stamped), and -70 (`408d05723`, rev-4: `tree_lib.py#KEPT_CENSUSES` and the two refusals by line in `read_kept_rows`, the `..` test
  by path parts, `check_marker_domain` naming the registry, check 3 admitting `census-kept-paths.txt`, the manifest
  re-stamped, the plants `kept-row-multiword`, `-arity`, `-unknown-census` and `-duplicate`, deviation 1013 of unit 38), and -73 (`6d0627dd6`, rev-3: `tree_lib.py#resolve_kept_home`, `record_causes.py#check_kept_home` at the end of
  `check_cause_writers` printing `read at` and `registered at` or `registered nowhere`, the plant `kept-home-rooted`), and -75 (`59c4af40d`, rev-3: the manifest's `last-body-change` advanced to `8b31081ac`, no section B claim stale), and -74 (`0114569d9`, tip `ff0bbc900`, rev-3: `s1-59 206422580b73 1`, `s1-46 254057fa6d5b 0`, no record written), and -87 (`073d03dd7`, rev-3: `tree_lib.py#resolve_memory_root`, `record_causes.py#run_cause_writers`, `read nowhere` for a
  refused root, the plants `kept-home-trailing-root` and `kept-root-blank`), and -76 (`67ffd1289`, rev-4: both census `run_fixture`s hold `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` aside, `reads` on the
  three ratchet rows, `census-kept-paths.txt` out of `PROJECT_REGISTRY_EXTRA`, the manifest re-stamped, its ledger holding
  the S19 sweep block), and -83 (`39ffc882e`, rev-4: `s1-59` 1 at `206422580b73`, no record of unit 59 or 74 owed or written), and -84 (`f1b815ced`, rev-3: `s1-46` 0 at `254057fa6d5b`, no record of unit 70 or 74 owed), and -77 (`049c4503d`, rev-4: `read_checker` probed in spec text, unit 76's `live` read taken).
  This unit is order 36, rev-3, the second of units 77, 78, 79, 80, 85, 86 and 90. The main loop ran section 4's sweep at
  `f1b815ced` (unit 84's pass) with unit 76's sweep output as `HAVE` (its `live` read was red, so its lines were taken
  over), and the whole output stands in "The sweep, as run" at the end of this brief: copy it into the ledger's AC1 block
  byte for byte, on separate lines, because units 79, 92 and 100 read it. Nothing printed on the error stream. The `?` in
  a line is unit 76's script's ASCII replacement of a non-ASCII byte. Run no checker and no gate leg. A §8 resolution mark is exactly `RESOLVED (agent, YYYY-MM-DD, delegated)`. Verify each claim about current code
  against source before building on it, and hand one that no longer holds back as a divergence.
- A pass that edits `tools/policy/catalogue.toml` re-renders `.governance/policy.json` with `python
  tools/policy/policy.py mirror --write` and commits it, or the pass legs refuse a stale mirror. A literal markdown
  link in prose, backticked or not, is read by hygiene check 2 as a real link: describe a link template in words.
- Pass-leg lessons, each a red an earlier pass met: name every helper, nested ones included, from `.lexicon.conf`'s
  VERBS table (`python tools/lexicon/lexicon.py --suggest <name> --as py.function`); a definition copied into a new
  kit copy counts once per copy, so re-measure `VERB_OFFENDER_PIN` in `.lexicon.conf` with `lexicon.py --measure`
  in the file's `RE-MEASURED` comment practice, naming each ARRIVED and LEFT offender (unit 13 re-measured it to its
  current value); spell no sibling kit's path (`<kit>/<file>`) in a shipped file, fixtures and selftests included
  (`install-prefix (shipped surface)`); a new surface class needs its `[[class]]` row in `tools/govkit/usage.toml`
  (`docs`); a new leg's ceiling clears its evidenced maximum by max(120 s, 1.0x) (PINNED 2026-11-22, deviation 15); every number in a record you write carries an id, a
  path:line, PINNED or DERIVED on its line.
- Inherited red you are not to fix: `memory hygiene` check 21 on dWitnessedBar's `replay.py`.
- Cite code lines in every record you write as `path#symbol` or blob-pinned, never a bare `path:line`, fixture text
  included. Write no numeric fact without an id, a path:line, PINNED or DERIVED on its line.
- This pass runs on node a (the run moved from node d on 2026-11-23). On node d bash 5.3.9 (cygwin) turns a `$'\r'` written inside `$(...)` into an empty string; never feed a
  `while` loop from a here-string whose value came from `$(...)`. `tools/gate-legs.json` is GENERATED by
  `leg_factory.py --write`, never hand-edited. Python's `bash` subprocess is WSL's here: call the Git-Bash `bash`
  by its resolved path, or keep logic in Python.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dTotalRecall-78`, its FINAL trailer block carrying
  `Pass: TOOL-dTotalRecall-78` beside `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. Stage explicit paths
  only, never `git add -A`.
- Commit `memory/builds/dTotalRecall/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has
  landed. Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-78-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells; a criterion
  whose observation is a gate leg or a `New arm:` RED-first observation is owed to the close.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A staged file on the kickoff
  manifest's `watch:` list needs the manifest (`memory/guides/SESSION-KICKOFF.md`) re-stamped in the same commit; new
  Python symbols owe `python tools/codebase-map/gen_map.py --write`; declare both.
- The pre-commit hook can run past two minutes: give every `git commit` a 600000 ms tool timeout.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed; a new suite's own
  file may be run directly to stage its refusals RED.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
- A command that runs past two minutes goes in the background with a 600000 ms bound and is waited for, never polled.
- `packet.py --check dTotalRecall` runs past ten minutes on node a: observe any criterion that names it through
  `python tools/chain-packet.py --check dTotalRecall`, the instrument's own `main` and bytes, and say so in the ledger.
- Name durations and counts in your return with `DERIVED 2026-11-24` on the line.
- Return a divergence (your `why` opening `DIVERGENCE:`) when the spec cannot be built as written; save any draft
  you made as a patch under the scratch directory and name it.

## The sweep, as run

Run on node a at f1b815ced, every line DERIVED 2026-11-24 by this run.

```text
1 360b653fd27b7fefa4839bfb44884207230a66c6 rc=0
13 3dc09b8610f0046dcad7c3546f25f9e234241df0 rc=0
8 red no pass commit
18 305b6e9d1370cf97a92976e073aa564ae567d569 rc=0
37 red no pass commit
16 f36ec323c01b38a775873b202a0a71b23898b933 rc=0
25 a9f1e2a6839369d0b40006c53759845b73fd6d01 rc=0
5 202a354a4bc8b7eb317c2355fdd8e9809ad55e69 rc=0
38 2f59e5acb7c45d9a72b1cbdbb140ef1f09d55fe0 rc=0
4 dcd8b10f714157fb08b2af09e45f7c425ece7a46 rc=0
54 74af3faa40216c7a2a19aefd66b19847ac31b84f rc=0
40 dc1fd17e7ac27e25ffd729869a99c8b56699a4b7 rc=0
44 376f76cd2606e7b0c71599b8f21c55089da6a194 rc=0
45 c6fcf603b9ba3762af845e457f851d4068b19803 rc=0
46 63f283ddd38397f94a706bf942859d31179fd515 rc=0
6 ce198f66033d762db9ffe3d46f64752c8bb16264 rc=0
63 818591fc2b0b529588d9056aba6d39dc40df5aac rc=0
64 86360f071302e833e1b567e93b4c9453abc9a082 rc=0
22 491dfe31c4fb9890ce3086eb73793d40f10dce1d rc=1
22 491dfe31c4fb9890ce3086eb73793d40f10dce1d MANIFEST check 9 FAILED ? the manifest body has not changed across ten or more watched commits, so its front-loaded claims are drifting unverified; re-read ?B and advance last-body-change to a current sha: 10 non-merge commits since 2c621083fd91278f33ba1baba1ea15f4dada31b0
3 f8b950c13a5268c83b972599a4995df20ad88e29 rc=0
2 d91388c2f5cad72e9210e620b90910740f7c2dee rc=0
7 5688d011aca6312152d38a3c502ad51dce1835f3 rc=0
11 71ce746a07bcd5c8461c1ede47047ede33135d01 rc=0
41 c2814ccc0621de338a675ad15016599601dbbcf4 rc=0
10 d735e47b952d119bbf2425701a5f70bd75600498 rc=0
42 53496c0d164b756f358793f9f57bfbbe6561099a rc=0
19 6ea0038917b88da100410fad7c6831935375fb5d rc=0
21 bd6fe04f88e71f9f62dd797dd1108649b445b2bd rc=0
36 7ffe749aaf3510c6b087269597432efb930ad644 rc=0
39 d653803302f67dd57a492196a8f178e96c763558 rc=0
47 a5f0166586158af426cc0cd3530d2bcb0b25f713 rc=0
48 4d1d9899acadbdd66f02af9e78d8100705447d85 rc=0
49 60424d69e5b45453e89edd5ce4aa4711a3c08916 rc=0
50 7f51d13ddb47c5ff3d66fd25fcff7d683349301f rc=0
51 30d1901d6aeaf615cab19366514dd0dadb1e52c0 rc=0
9 29b39e57245237223e3ce27112cc73f6ef547c89 rc=0
23 30d52b595b0b7c8477ac22b82eb14d4f92150be6 rc=0
61 778edd3a330784a2b68a75985d6fc629bf723145 rc=0
24 5d632d67de189b1025d43f044813223307d7bad3 rc=0
67 56390bab8cce52668b940893b8378621df78e4b7 rc=0
20 f6bdef7b4c6d70394c2ed7d0f80e7f905c829acb rc=0
71 5e004ad39095d3577d0368b8410c2fa190e39048 rc=0
72 35e956dc6b66e96e90e08f0a255b16aa61995d55 rc=0
17 30c21c834d24bdf968f0da62be6dd582add91642 rc=0
81 7e151e666b79e2438b7e65f8c8075b2843a3c7d5 rc=0
82 f4e82dad9d46c3e99619d3bdd96e461d0687537b rc=0
14 red no pass commit
15 red no pass commit
26 red no pass commit
12 6f7d5dd2c8773e973616589bc02b3f71e27d5e9b rc=0
43 b9b6e584a4812d37e37c2e18296f42a960c4a476 rc=0
52 926526b1c9125added7b6b2edbde490d99c0a3f4 rc=0
62 4975ccf29373577e7c1ba4608f13771144b4efb4 rc=0
53 6db81d070cea4ab52c719ffb0316748a32eaf840 rc=0
59 47afc89374e539d933728b5f0a06b9678a4ac388 rc=0
55 5b5895a493d4a47a0be4e417b1c5550cde92b001 rc=0
56 798f98fc1fa2c4af9feb68f8324f11c9d5339c8f rc=0
57 5ff76c2e273faa46b4490bde40ecb26478205de9 rc=0
58 7fd3f8e3817ee32b65edfd6f940d7dcc74518bcb rc=0
60 2ec3df383d4bf4be29d8b0cdc0ad6b9f073b69a9 rc=0
65 f1e11ac4933ff21ea5ee851f488dad17a313beef rc=0
66 17aac82e4c1eea50666618a8f62ead42d08364fa rc=0
68 7252440fd4871bbd72815d2f8dde38e4f404dbd5 rc=0
69 f7011dd6fc390d088e0d790c5e6c6901fd20edd6 rc=0
70 408d05723354b00d8e79aba5e6eb60868b8d15ce rc=0
73 6d0627dd6df306d627e2bbf841182d67499867a4 rc=0
75 59c4af40d0af08317a574eecf0485956a8c98429 rc=0
74 0114569d9558ebbd9440edadd97839306f60337b rc=0
87 073d03dd7df748eccc25079328c2199fa132c972 rc=0
76 67ffd12899cc7c20cc8399aca555360fec613886 rc=0
83 39ffc882ed18d2f5234fe4b86739ca4175a1d656 rc=0
84 f1b815ced4582351db667e5040288bdd9124d8f8 rc=0
population 72
```
