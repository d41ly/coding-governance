**Serves:** journal TOOL-dTotalRecall-53
**Caused-by:** TOOL-dTotalRecall-53

# Build brief — TOOL-dTotalRecall-53

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dTotalRecall's build run. Its spec run landed every spec DEFERRED at base `462d20f3`, and this run builds
  them in the build-order table's order from base `8b8b1374c`. This unit is build order 29, beside TOOL-dTotalRecall-59, which builds after it. A spec writer may be
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
  no `absorbs`). This unit is order 29, rev-5: its S20, S32, AC20 and AC32 ride with held unit 37 (§8 F3), build none
  of them. Its §4 marks a dozen items already true at HEAD (S2, S6, S7, S8, S11, S13, S15, S17, S25, S26, S29, S38):
  each keeps its criterion as a check, observed, never rebuilt. The `record-kinds` leg is red at HEAD on five
  `check_alias_compares` hits (the `gen_build_index.py` forwarders unit 20 rendered and
  `tools/govkit/steps/memory_journal_alias.py`), which this unit's S34 closes. A §8 resolution mark is exactly `RESOLVED (agent, YYYY-MM-DD, delegated)`. Verify each claim about current code
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
- On this node bash 5.3.9 (cygwin) turns a `$'\r'` written inside `$(...)` into an empty string; never feed a
  `while` loop from a here-string whose value came from `$(...)`. `tools/gate-legs.json` is GENERATED by
  `leg_factory.py --write`, never hand-edited. Python's `bash` subprocess is WSL's here: call the Git-Bash `bash`
  by its resolved path, or keep logic in Python.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dTotalRecall-53`, its FINAL trailer block carrying
  `Pass: TOOL-dTotalRecall-53` beside `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. Stage explicit paths
  only, never `git add -A`.
- Commit `memory/builds/dTotalRecall/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has
  landed. Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dTotalRecall/build/2026-11-23-build-TOOL-dTotalRecall-53-1-acceptance-ledger.md` in the pass commit:
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
- Return a divergence (your `why` opening `DIVERGENCE:`) when the spec cannot be built as written; save any draft
  you made as a patch under the scratch directory and name it.
