# KICK-dKeptSession-56 — acceptance ledger

**Serves:** journal KICK-dKeptSession-56

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32,
node d, from the pass's base `5ceb78bff` over the working tree of each of the pass's commits: by single
plants run alone by direct CLI (`loop_transition.py --fixture --plant`, `card-store.fixture.sh --plant`,
`check_policy.py --fixture <case>`); by `python -I` probes over scratch transcripts and scratch
repositories under the session's temp directory, driving the runlog CLI, the orient measure, the
transition writer and a sourced `print_progress`; by one scratch clone for the mirror reads; and by the
greps and one-liners the criteria state.

## Reconciled at the build

Every code claim the rev-6 spec makes held at the base, units 7, 35, 42, 44, 52, 53, 55 and 61 landed.
The driver suite's floors read 4187 and 1404, the runlog suite's 1632, the kickoff suite's 443, and
`len(PLANTS)` 38 (DERIVED, their last assignments and an import at the base), as the task stated.
The spec's design was built as written, with these readings of its text:

- S33's signature: the spec writes `write_dependency_notices(root, build, commit, repost=False)`,
  while the landed function takes KICK-dKeptSession-35's `ordinal` after `commit`. The keyword joins
  after it, and the re-post passes the latest Design exit's ordinal through it, the count of exits in
  `before`, as §4 "The re-post" names.
- S33's listing: the re-post keys the check and the post at the latest Design exit's commit, read off
  `before`, the commit the refused notice was keyed over, never the moving HEAD. A spec status flip
  during Build moves the listing at HEAD, and would read every dependent unconfirmed at every move.
- S32's cause is the ack's first non-empty output line, stdout before stderr as `run_sourced` joins
  them, `mail — not written: no session id` for AC27's case; a raise's is `<class>: <text>`.
- S32 moves the refusal text of the landed `acks-failed` plant, both its rows held for refused acks,
  so its refusal check is re-armed to `mail ack not posted: <id>` for each row in the same commit.
- S22's re-stamp: the kickoff ratchet takes the stamp at the commit's parent, so part 2 stamps at
  part 1 and the closing commit stamps again at part 5, after this unit's last edit to a watched path.
- AC20's literal `grep -c "readCard" mail-notice.js` prints 3 (DERIVED, that grep): the hook's own
  `readCardBuild`, its call, and the comment saying `readCard` is not carried. `grep -c "readCard("`
  prints 0 (DERIVED, that grep), so no `readCard` is defined or called; the four `scratch-guard` hits
  are all comment lines (DERIVED, `grep -n`). The criterion's intent holds; its count is stale text.
- The `loop transition record` leg's ceiling is parked for the owner, so the row is re-priced and the
  pass does not stop on it (§ "What the close owes").

## The sibling texts this unit answers (§8 F3)

- S12, `KICK-dKeptSession-30` §5's price, "one scan per call over at most 20 main transcripts", is
  superseded by name: `measure_orient_tree` holds one window per model per `--orient` run, so the 22
  rows of unit 9's AC3 fixture on one model cost one `derive_context_window` call (DERIVED, AC10's
  probe), and every other caller makes one call per process.
- S12, unit 30 §3's "S11 memoises it per model and root": answered by S11, which mints no memo; the
  rows of one run already share one window, and the boundary read and the context verb make one call.
- S39, `KICK-dKeptSession-32` §4's rejected alternative "Writing only `never` keys": its reason, "The
  rows a preset leaves unassigned would vanish", is withdrawn. The alternative reads "never keys with
  no comment lines", rejected because the posture is hidden; the unassigned rows are a separate class
  (`derive_derived_rows` less `literal`), which no preset carries a key on.
- S38, AC29: `KICK-dKeptSession-34` AC2, whose case reads "the two rows carrying one value and one
  source", is a regression observation only, and its `preset-derived-cap` case read 0 wrong (DERIVED,
  that run); unit 34's AC1 is decided by `KICK-dKeptSession-54` AC1's rewritten `preset-every-key`,
  which read 0 wrong (DERIVED, that run).
- S40: `KICK-dKeptSession-39` AC1 reads the tuple's membership, `'mailbox-message' in
  tree_lib.TYPED_RECORD_KINDS`, and cites PLAY-dOrderedCharter-42 S2's import refusal, `import
  build_records` exiting 0, for the equality (AC30 below).
- S43, AC33: `KICK-dKeptSession-44` §4's parenthetical pairs the two rows with two addresses in
  swapped order. Cited here by key alone: `.memory-tree.conf#REFUSAL_CEILINGS`, whose
  `tools/unattended/unattended.sh` row the census reads 347/347 (DERIVED, `check-arms.py --report`
  after the last edit), and `.memory-tree.conf#ARMS_FLOORS`, whose `manifest-check.sh` row this pass
  leaves unmoved, since `derive_version_order` adds no refusal arm.
- S19, AC16: the fact is the `PreToolUse` schema holding `additionalContext`, its minified builder
  matched as `[A-Za-z_$]*`. `grep -a -o 'hookEventName:[A-Za-z_$]*("PreToolUse"),permissionDecision[^}]*additionalContext'
  | wc -l` over the `claude` on PATH, version 2.1.319, printed 2 (PINNED 2026-11-23, node d). The
  `cli-version` RUN.md pins is 2.1.326 (PINNED 2026-11-23, RUN.md), whose binary is not installed on
  this node, so its count is owed to a node holding it; `KICK-dKeptSession-44` S7's deny-builder count
  is superseded by this one.
- S45, AC34: met by `KICK-dKeptSession-35` rev-3. A `record` over the `notices-two-dependents`
  scratch with `read_transitions` rebound to raise `ValueError` exited 2 printing `loop: unanswered`
  and the recorded launcher saw no post (DERIVED, that probe), so no no-ordinal line is owed.

## The legs each named unit's pass owes (S25 to S27, S44, AC22)

`python tools/check-spec-tokens.py --legs-for -` over the paths each unit's `Pass:` commits touched
printed `policy fixtures` for every unit below but 39 (DERIVED, that probe). `loop transition record`,
the leg running `loop_transition.py check --selftest`, and `loop position fixtures` carry no guard in
`tools/gate-legs.json`, so `--legs-for` names neither and both run on every change (DERIVED, the
registry's rows): they are the legs that run units 35, 36 and 42's plants in
`tools/loop/loop_transition.py` at the close, and unit 44's.

- KICK-dKeptSession-30: `policy fixtures`.
- KICK-dKeptSession-32: `policy fixtures`.
- KICK-dKeptSession-33: `policy fixtures`.
- KICK-dKeptSession-34: `policy fixtures`.
- KICK-dKeptSession-35: `policy fixtures`; `loop transition record` for its notices plants.
- KICK-dKeptSession-36: `policy fixtures`; `loop transition record` for its guard-launch plants.
- KICK-dKeptSession-37: `policy fixtures`.
- KICK-dKeptSession-38: `policy fixtures`.
- KICK-dKeptSession-39: none of the three; its records arms are the memory-tree legs'.
- KICK-dKeptSession-40: `policy fixtures`.
- KICK-dKeptSession-41: `policy fixtures`.
- KICK-dKeptSession-42: `policy fixtures`; `loop transition record` for its acks plants.
- KICK-dKeptSession-43: `policy fixtures`.
- KICK-dKeptSession-44: `policy fixtures`; `loop transition record` for `mail-read-crash` and
  `loop position fixtures`.

## Criteria

**Evidences:** KICK-dKeptSession-56
- AC1 — the grep printed step 7's row, `KICK-dKeptSession-16` and `KICK-dKeptSession-67`, reading `yes`, and step 27's, `KICK-dKeptSession-17` and `KICK-dKeptSession-61`, reading `no` (DERIVED, that grep).
- AC2 — `grep -c 'derive_parallel_step'` printed 3 and `grep -c 'def extract_files_touched'` printed 0 over `gen_build_index.py` (DERIVED, those greps).
- AC3 — the `ast` probe printed 11 functions naming `"unattended.sh"` and launching through `subprocess`, each `True` (DERIVED, that probe), and the bare-`bash` grep printed nothing.
- AC4 — the two `resolve_bash_py` blocks of `loop_witness.py` and `tools/lib/resolve_bash.py` compared byte-equal with CRs dropped (DERIVED, that probe).
- AC5 — with `GOV_BASH` naming the System32 `bash.exe`, `loop_witness.resolve_bash` answered `None` and `scan_bash`'s refusal named `GOV_BASH` and `answered Linux` (DERIVED, that probe).
- AC6 — the `presets-derived` case's `stage-default` plant read `arm_presets` naming `preset.standard · review.build`, `"off" is not the row's default "owed"`, and its unplanted run 0 findings; `presets.py check` over the shipped store exited 0, green (DERIVED, those runs).
- AC7 — `KICK-dKeptSession-51` AC2: the squeezed guide holds the ninth-field sentence once, `seventh field` 0 times, and the template and the guide compare equal; AC3: `dWellOiledMachine`'s backlog names `derive_message_id` in its one ask row (DERIVED, those greps).
- AC8 — `KICK-dKeptSession-49` AC1: `check_policy.py --fixture mirror-pre-unit-stale` read 0 wrong, the changed store answering `allowed` with its `mirror stale at` line (DERIVED, that run).
- AC9 — over one `--orient` dir the `context-window-sibling` turn's orient row read `context=90%` and `runlog.py context` read `90%` (DERIVED, that probe).
- AC10 — 22 orient rows on one model built by `build_orient_transcript` made 1 `derive_context_window` call through `measure_orient_tree` (DERIVED, that probe).
- AC11 — `git show --stat 6178a65e` listed both `tools/memory-tree/build_records.py` and `tools/memory-tree/tree_lib.py` (DERIVED, that command).
- AC12 — a `claude-` model's 150000-token turn under the variable at 200000 read `75%` with stderr `context: window 200000 · env, advisory`, and `fixture-model`'s the plain `env` (DERIVED, that probe); `grep -n "first-party" help/orientation-card.md` prints the `context —` paragraph's sentence.
- AC13 — `KICK-dKeptSession-45` AC1's probe printed `(1000000, 'observed 900000 on fixture-model')` (DERIVED, that probe).
- AC14 — the grep printed one line, inside `main` before its arm loop (DERIVED, that grep).
- AC15 — the `derive_cli_line` range holds `read_claude_version` once and no `--version`; `^read_claude_version()` and `claude --version </dev/null` each count 1, the second inside `read_claude_version` (DERIVED, those greps).
- AC16 — the `grep -a -o` of the builder pattern piped into `wc -l` over PATH's 2.1.319 printed `2` (PINNED 2026-11-23, node d); the pinned 2.1.326's count is owed, as S19 above records.
- AC17 — a Design exit whose parent README renders the no-edge sentence, and one whose region holds no `Child builds` line, each recorded with exit 0 and the launcher saw no post or check; `read_dependents` listed none for both and for an absent README (DERIVED, that probe).
- AC18 — `grep -c 'SID_RE.fullmatch(p.name' tools/runlog/extract.py` printed 1, inside `derive_main_transcripts`, where the base printed 3 (DERIVED, those greps).
- AC19 — `grep -c 'claude-code_\*' manifest-check.sh` printed 1, and `card-store.fixture.sh --plant fixture-cli-short` printed its row `held`, the `resume — resume recommended (resume.context: always-resume)` line; the sibling plants `fixture-cli-path-differs`, `fixture-cli-unknown`, `fixture-stale` and `context-always-resume` each printed every row `held` over the new compare (DERIVED, those runs).
- AC20 — `node mail-notice.js` from a scratch install holding only the unattended kit's files exited 0 (DERIVED, that probe); the counts are reconciled above.
- AC21 — a sourced `print_progress` over a stub starting a 30 s grandchild that holds its stdout returned in 0 s and printed its line, bounded and with `GATE_BOUND_LIVE=0`, where a `$( )` capture of the same stub waited 30 s (DERIVED, that probe); the `bash unattended.sh --landed <slug>` reading is the suite block's, owed.
- AC22 — `check-spec-tokens.py --legs-for` over each named unit's pass paths printed `policy fixtures` for every unit but 39, and `loop transition record`, unguarded, runs units 35, 36 and 42's plants at the close, one line per unit in the legs section above (DERIVED, that probe and the registry).
- AC23 — `grep -c "render_scaffold(rows)" check_policy.py` printed 0, and `check_policy.py --fixture scaffold-preset` read 0 wrong (DERIVED, those runs).
- AC24 — `policy.py mirror --check` in a scratch clone exited 0 at unit 41's closing commits `ce1a539e7` and `b9eae128f`, and exited 1 at unit 40's pass commit `f9e192e92`, naming `legacy_blobs`, and at unit 41's first commit `cca4b7039`, naming `catalogue_blob` (DERIVED, that probe). RED for those two commits: unit 40's pass moved a mirror input without re-rendering the mirror, which later fix commits re-stamped, and the mirror reads fresh at this pass's HEAD (DERIVED, that command). No later unit can rewrite those commits; the main loop owns the disposition.
- AC25 — `KICK-dKeptSession-47` AC1: the `context-window` turn beside `context-window-compact-other` read `75%`, `observed 150000 on fixture-model` (DERIVED, that probe).
- AC26 — the `presets-derived` case's `budget-cap` plant read `arm_presets` naming `preset.strict` and the census's first cap (DERIVED, that run).
- AC27 — `loop_transition.py --fixture --plant acks-no-session` printed `refused — tFix · mail ack not posted: a1a2a3a4a5a6 · mail — not written: no session id`, the row read `open`, and `held` (DERIVED, that run).
- AC28 — `--plant notices-reposted` printed `dA · confirmed pass 1`, `dB · confirmed pass 1`, its posts `build:dA rc 2 · build:dB rc 0 · build:dA rc 0`, so the second move posted to dA alone, and `held` (DERIVED, that run).
- AC29 — unit 34's AC2 is answered as a regression observation, and its AC1 by `KICK-dKeptSession-54` AC1's `preset-every-key`, as S38 above records (DERIVED, those runs).
- AC30 — the import probe printed `True` (DERIVED, that command).
- AC31 — the `derived` grep over `presets.py` printed nothing (DERIVED, that grep).
- AC32 — `grep -n "GOV_BASH" loop.md` printed unit 36's sentence, `grep -n "skipped" orientation-card.md` unit 43's lines, and `grep -n "presets.toml" README.md` in the policy kit its store row (DERIVED, those greps).
- AC33 — this ledger cites `ARMS_FLOORS` and `REFUSAL_CEILINGS` by key and by no line, as S43 above records.
- AC34 — `record` over the `notices-two-dependents` scratch with `loop_transition.read_transitions` rebound to raise `ValueError` and `breakpoints.run_sourced` wrapped exited 2, the wrapper recording no post (DERIVED, that probe), as S45 above records.
- AC35 — `tr -s ' \r\n' ' '` over this ledger piped into `grep -c` reads each of the four quoted passages once, and `git diff --name-only <pass base> HEAD -- memory/builds/dKeptSession/build/` lists this ledger alone, both read at the closing commit, and the main loop confirms it.

## What the close owes

The plants read alone: `acks-no-session` 3.8 s and `notices-reposted` 16.8 s (PINNED 2026-11-23, node d);
`deps-notices` re-read at 18.2 s and `notices-two-dependents` at 41.6 s against unit 44's 15.5 s and
35.3 s (PINNED 2026-11-23, node d), the re-post check every non-exit move after a Design exit now runs.
So the `loop transition record` row's proxy `r` is 305.3 s (DERIVED, 275.7 plus 20.6 plus 9.0), its
value 458 (DERIVED, x1.5 rounded up) and its token `plants=40`, 338 s past the leg's 120 s ceiling
(PINNED 2026-11-23, `tools/gate-legs.json`), the owner's to raise, not made here.
`fixture-cli-short` read 24 s alone (PINNED 2026-11-23, node d), so `manifest-check self-test` reads
5267 (DERIVED, 3487 plus 24, x1.5 rounded up); the runlog check's one context read 0.14 s (PINNED
2026-11-23, node d), so `runlog selftest` reads 117 (DERIVED, 77.4 x1.5 rounded up); the
`presets-derived` case read 3 s alone (PINNED 2026-11-23, node d), so `policy fixtures` stands at 1820
(DERIVED, 1210.6 x1.5 under it); the driver block's two landings are estimated at 20 s each, as unit 44
priced its two (PINNED 2026-11-23, an estimate), so shard 8/8 reads 6845 (DERIVED, 6785 plus 60). The
`unattended kit gate` row is held by owner ruling and is not moved; its re-read from the new block's
alone reading is owed to the close, which alone can run the block.

The close owes: §7's legs; the new `check --selftest` cases, two per new plant, and `acks-failed
refused`, which reads the re-armed plant's refusal; the runlog window arm's new check, `ASSERTION_FLOOR` unmoved at 1632
(DERIVED, a floor the added check exceeds); the kickoff suite's new `--list` row, `FLOOR_ASSERTIONS`
444 (DERIVED, plus 1); the driver suite's 3 new region-eight `same`, `FLOOR_ASSERTIONS` 4190 and
`FLOOR_SHARD_8` 1407 (DERIVED, plus 3 each); `presets-derived` under `policy fixtures`; the `docs` leg
over `help/loop.md` and `help/orientation-card.md`, whose anchors' fingerprints
`docs_leg.py --fingerprints` printed unchanged; and each `New arm:` line's RED-first observation
against its staged break.
