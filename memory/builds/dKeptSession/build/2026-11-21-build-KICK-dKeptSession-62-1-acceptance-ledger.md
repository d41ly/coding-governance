# KICK-dKeptSession-62 — acceptance ledger

**Serves:** journal KICK-dKeptSession-62

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32
from the pass's base `bca3d9f82`, over the working tree of the pass's commits, by the commands the
criteria state run by direct CLI, by `python -I` and `node` probes of the code each item changed, by
scratch fixtures under the session scratchpad and short `%TEMP%` directories, and by single loop
plants run alone, as the role allows.

## Reconciled at the build

The rev-5 spec was grounded on `71b22e42` with every unit ordered before it read as landed; all of them
have landed. Every claim the design reads held at this base. These figures and texts had moved, and
each was reconciled in place:

- The driver suite's floors read `FLOOR_ASSERTIONS` 4190 and `FLOOR_SHARD_8` 1407 at this base, not
  §4's 4137 and 1354 (DERIVED, the last assignment of each); the raise is taken from 4190 and 1407.
- The runlog selftest's `ASSERTION_FLOOR` read 1632 at this base (DERIVED, its assignment).
- `len(PLANTS)` in `tools/loop/loop_transition.py` reads 40 before and after this pass (DERIVED, the
  table): no plant is added, `acks-failed` gains a second B7 move inside its own case.
- AC12: `tools/loop/loop_transition.py#write_consumed_acks` holds one `read_mail_rows` call, the
  parent's sent read `read_mail_rows(root, <parent>, local=True, sent=True)` that `KICK-dKeptSession-61`
  S2 added after this spec's audit, a local read of another build's sent rows with no fetch. The
  build's own mailbox is read once, by `write_transition` (DERIVED, an `ast` walk naming each call's
  enclosing function), so the writer makes no read of the rows it acks: the criterion's intent holds and
  its "none inside `write_consumed_acks`" is read as none of the build's own mailbox.
- AC19 and `KICK-dKeptSession-56` AC20: the literal `grep -c "readCard" mail-notice.js` counts the
  lines holding `readCardBuild`, the hook's own card reader, and the header sentence saying `readCard` is
  not carried, so it prints 3 (DERIVED, that grep). The carried closure is read as the criterion means it:
  `grep -c 'function readCard('` prints 0 (DERIVED), and S21 names `readCard` as never carried.
- AC11 runs `--landed` through the driver sourced again inside the arm's subshell, not executed, so the
  arm's stub engine stands in for the loop kit's `loop_transition.py`; the failing `timeout` first on
  `PATH` is what the source-time probe reads either way.
- S1's unit 54 declares no Files touched at its CLOSED rev-4, so the query has no path to read and exits
  2 (DERIVED, the probe); its line names the leg its own §7 names.
- No criterion here counts over the `claude` binary, so the pinned version's absence on this node owes
  nothing.

## The legs each named unit's arm owes (S1)

`python tools/check-spec-tokens.py --legs-for <paths>` over the paths
`tools/check-spec-tokens.py#extract_files_touched` reads from each unit's `### Files touched (estimate)`
exited 0 for units 49, 50, 52, 53 and 55, with no path untracked and no UNEVALUATED row (DERIVED, that
probe). Each line names every leg the query printed on a row not marked `broad`, then the leg the unit's
own §7 names to run its arm at the close. `loop transition record` carries no `guard` in
`tools/gate-legs.json`, so the query never prints it; no `loop selftest` leg exists.

- OBSERVED KICK-dKeptSession-49: `routed-commits selftest` · `scratch-guard self-test` · `policy fixtures` · `recall floor` · `recall floor arms`; its arm's leg `policy fixtures`.
- OBSERVED KICK-dKeptSession-50: `routed-commits selftest` · `scratch-guard self-test` · `policy fixtures` · `recall floor` · `recall floor arms`; its arm's leg `policy fixtures`.
- OBSERVED KICK-dKeptSession-54: no path declared, so the query names nothing; its restated cases' leg `policy fixtures`, the first its §7 names.
- OBSERVED KICK-dKeptSession-52: `recall floor` · `recall floor arms`; and `loop transition record`, unguarded, for its `notices-repeat-key` plant.
- OBSERVED KICK-dKeptSession-53: `recall floor` · `recall floor arms`; and `loop transition record`, unguarded, for its chain's plants.
- OBSERVED KICK-dKeptSession-55: `recall floor` · `recall floor arms`; and `loop transition record`, unguarded, for its withdrawn plants.

## The sibling texts this unit answers (§8 F3)

Each unit named below is CLOSED, so neither its spec nor its ledger is written; each text is quoted as
it stands at that unit's rev and answered here.

- S12, `KICK-dKeptSession-47` S1's rule, a compaction joining `model`'s observation "only when the
  newest main-source `usage` event before it in the same transcript's event list is on `model`": the
  compaction's own `src` must now be `main` too, so a main-file record carrying `isSidechain`, which
  `extract_session` relabels `agent`, joins no model. The docstring of
  `tools/runlog/extract.py#derive_context_window` and the runlog README read "a main compaction".
- S13, `KICK-dKeptSession-56` AC21's half "with `GATE_BOUND_LIVE=0` a stub exiting 0 still emits its line":
  `load_driver_conf` assigns GATE_BOUND_LIVE from REMOTE_BOUND_LIVE, so a 0 assigned before it reads 1
  after it (DERIVED, a probe sourcing the driver over this tree's conf), and AC21's third arm reaches the
  bounded branch. AC11's arm stages the unbounded half by a stub `timeout` exiting 1 first on `PATH`:
  the driver's probe then reads REMOTE_BOUND_LIVE 0, the conf carries it into GATE_BOUND_LIVE and the
  GATE_BOUND note prints once (DERIVED, the same probe).
- S15, `KICK-dKeptSession-55` §4 "The step"'s per-row loop, "for r in eat: --mail ack <slug> r.id":
  the consumed ids are now posted in one call, `--mail ack <slug> <id> [<id> ...]`, landing in one ref
  update or none, and `write_consumed_acks` prints its per-id lines after that call.
- S18, `KICK-dKeptSession-56` S21's "`scan_preflights` keeps its `_check_inside` walk": `scan_preflights`
  now reads `derive_main_transcripts`, which applies `_check_inside` against the resolved root (S19), so
  the glob is spelled once.

## Plants re-read (the `loop transition record` row)

S15 moves `write_consumed_acks` to one call per move and `acks-failed` gains a second B7 move. Each plant
whose acks moved was run alone by direct CLI over this pass's tree on 2026-11-23 (PINNED, those runs):
`acks-failed` 13.3s against unit 56's 12.6s, `acks-superseded` 13.2s against 17.3s, `acks-takeover`
12.0s against 15.2s, `chain-two-dependents` 20.6s against 29.5s and `acks-landed` 6.7s against 6.6s, a
net 15.4s under the readings the row sums (DERIVED, those five differences). `acks-confirmed` 10.3s,
`acks-withdrawn` 5.7s, `acks-withdrawn-question` 3.0s, `acks-later-key` 3.0s, `acks-no-session` 3.6s,
`mail-disposed` 5.5s and `notices-reposted` 21s each held (PINNED, the same runs). The row reads 458,
unchanged, since no reading rose past it (PINNED, `tools/run-gates/selftest-budgets.txt` at this base);
the leg's 120s ceiling stays the owner's (PINNED 2026-11-23, `tools/gate-legs.json`).

## Criteria

**Evidences:** KICK-dKeptSession-62
- AC1 — the six lines above name `policy fixtures` for units 49, 50 and 54 and `loop transition record` for units 52, 53 and 55; the three quoted passages each appear once in this ledger squeezed by `tr -s`, and this pass's commits touch no acceptance ledger but this one; read at the pass commit, and the main loop confirms it.
- AC2 — `grep -c 'claude --version </dev/null' manifest-check.sh` printed 1, on the line inside `read_claude_version`'s range (DERIVED, that grep and the range's bounds).
- AC3 — the `derive_cli_line` range grepped for `--version` printed 0 and `grep -c 'cli — skipped: claude --version' manifest-check.test.sh` printed 2 (DERIVED, those commands).
- AC4 — `runlog.py context` beside `context-window-compact-own` printed `15%` and beside `context-window-compact-other` `75%` (DERIVED, a scratch-root probe).
- AC5 — 22 orient rows on one model built by `build_orient_transcript` made 1 `derive_context_window` call through `measure_orient_tree` (DERIVED, that probe).
- AC6 — `grep -c 'lru_cache\|functools' extract.py` printed 0, and `derive_context_window("fixture-model")` under two `CLAUDE_CONFIG_DIR` values in one process returned `no observation` then `observed 900000 on fixture-model` (DERIVED, that probe).
- AC7 — `--plant notices-reposted` printed `dA · confirmed pass 1` and `dB · confirmed pass 1`, its posts `build:dA rc 2 · build:dB rc 0 · build:dA rc 0`, and `held` (DERIVED, that run).
- AC8 — `runlog.py context` over the `context-fill` scenario's agent file printed `none`, wrote nothing on stderr and exited 0 (DERIVED, that probe).
- AC9 — `grep -n 'SessionTree(sid=p.stem, main=p)' extract.py` printed one line, inside `derive_context_window` (DERIVED, that grep and the function's range).
- AC10 — `runlog.py context` beside `context-window-compact-sidechain` printed `75%`, and a copy dropping the `src` test printed `15%` (DERIVED, a scratch-root probe and its staged copy); the selftest's check is owed to the close.
- AC11 — the staging was probed: under the failing stub the sourced driver reads REMOTE_BOUND_LIVE and GATE_BOUND_LIVE 0 and prints the GATE_BOUND note once (DERIVED, that probe); the arm's `--landed` runs are owed to the close.
- AC12 — the `ast` walk found the build's own mailbox read once, in `write_transition`, reconciled above (DERIVED, that walk).
- AC13 — over a scratch bare origin, `--mail ack tFix a b` with a's ack posted printed `mail — duplicate` and exited 1 with b read `open`; with neither acked, two `mail — posted` lines and exit 0, the session ref's tip answering the second id, its parent the first, seq 2 over 1 (DERIVED, a scratch-fixture probe of the driver); the suite's block is owed to the close.
- AC14 — `grep -n "read_consumes_from" design_lib.py` printed two lines of `read_spec_edges`' docstring (DERIVED, that grep).
- AC15 — over the four-bullet fixture both readers read `KICK-tFix-1` alone, and a staged Python reader taking the wrapped `none` bullet's id read two ids and disagreed (DERIVED, a probe); the suite's case is owed to the close.
- AC16 — `grep -c 'glob("\*/\*.jsonl")' extract.py` printed 1, inside `derive_main_transcripts` (DERIVED, that grep).
- AC17 — over a scratch root holding a project directory symlinked from outside it, `derive_main_transcripts` listed the root's own transcript alone and the window read its 150000-token turn, where a copy dropping `_check_inside` listed the linked one too (DERIVED, that probe and its staged copy).
- AC18 — the two new rows' blocks compared as the parity arm compares them read equal in `mail-notice.js`, and a one-byte edit to a scratch copy of its `extractRouteUnits` drifted (DERIVED, a probe of the arm's `blk`); the arm's run is owed to the close.
- AC19 — the marker grep printed 2 over `scratch-guard.js` and 2 over `mail-notice.js`; the `readCard` count is reconciled above (DERIVED, those greps).
- AC20 — `grep -c 'def extract_files_touched' gen_build_index.py` printed 0 and `grep -c 'read_spec_writes' gen_build_index.py` printed 1 (DERIVED, those greps).
- AC21 — the `render_scaffold` grep printed 0 (DERIVED, that grep); the four `--fixture` cases are a gate leg's and are owed to the close.
- AC22 — `readMirrorAt` over a scratch repository whose committed mirror lacks the `.agent-cap.conf` key read it stale, where the base's reader read it fresh, and the parity case over a `LEGACY_INPUTS` gaining a planted path printed WRONG naming it (DERIVED, a `node` probe and a `python -I` probe); the `mirror-legacy-expected` case's run is owed to the close.
- AC23 — `grep -n 'type(ev.get("pre_tokens")) is int' extract.py` printed one line, inside `derive_context_window` (DERIVED, that grep).
- AC24 — the env-read reader named no variable outside the guarded set over `extract.py`, and named `RUNLOG_PLANTED` over a copy adding it (DERIVED, a `python -I` probe of the two helpers); the selftest's check is owed to the close.
- AC25 — `grep -n '\.claude' extract.py` printed two lines, both inside `resolve_projects_root`, and the `derive_context_window` range less its docstring holds no `expanduser` or `.claude` (DERIVED, that grep and an `ast` probe).
- AC26 — `grep -n 'HOME=str(empty), USERPROFILE=str(empty)' selftest.py` printed one line, inside `test_extract_context_window_root` (DERIVED, that grep).
- AC27 — `grep -n "are a step, and" gen_build_index.py` printed `render_order`'s docstring line (DERIVED, that grep).

## What the close owes

§7's legs, with `python tools/policy/policy.py mirror --check`, which printed `policy: mirror fresh`
after this pass's policy commit (DERIVED, that command), and `python tools/gate-lint/sh_hygiene.py
memory/project/substitution-fed-loops.txt`, which the role may not run. Each `New arm:` line's RED-first
observation: the runlog selftest's AC10, AC17 and AC24 checks; the driver suite's AC11, AC13 and AC15
blocks; the parity arm's AC18 rows; and the policy fixtures' AC22 cases.
