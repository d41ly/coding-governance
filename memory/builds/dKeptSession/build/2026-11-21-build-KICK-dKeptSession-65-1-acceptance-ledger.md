# KICK-dKeptSession-65 — acceptance ledger

**Serves:** journal KICK-dKeptSession-65

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32 at
the pass's base `1a6873936` over the working tree: by a scratch probe of the driver's `--mail` verbs, a
bare origin and two clones under `%TEMP%` built with the suite's own `mkconf` helper and unit 5's
two-clone recipe, running this unit's new block's driver calls by CLI, never the suite; by the runlog
suite's new arm called in-process by a `python -I` probe, never the suite; by a scratch repository under
`%TEMP%` built as the spec-token checker's self-test `scratch` function builds one, running the checker;
by `blk` copied from the resolver kit's test file over a scratch file; and by the greps the criteria
state. Every RED-first observation of a `New arm:` line is the close's.

## Reconciled at this base

The spec is rev-4, grounded at `f5beae3d` with the units ordered before it read as landed; every one has
landed, the last merges unit 64's at `337608fc0`. What the build found and how it was reconciled:

- Unit 64 landed the batched ack with the addressed-to check ahead of the `acked` skip, read off the
  state column of one `soft` read, and `#write_mail_post` binding `MAIL_DUPLICATE` so the ack turns a
  duplicate's exit 1 into 2. This pass replaces the skip's predicate and the read's mode as S1 and S12
  state and keeps unit 64's exits: `tools/unattended/unattended.sh#write_mail_ack` now returns 0 on an
  empty list before any read, reads `read_mailbox <slug> strict` once and
  `read_mailbox <slug> local sent` once, and skips an id some `sent` row of kind `ack` answers.
- The driver suite's effective floors read `FLOOR_ASSERTIONS` 4212 and `FLOOR_SHARD_8` 1429 at this base
  (DERIVED, the last assignment of each at `1a6873936`), not the spec's 4137 and 1354 (PINNED, the
  spec's §4 at `f5beae3d`); the SHADOWED pin reads 675 (DERIVED, the same read). The runlog suite's
  `ASSERTION_FLOOR` read 1651 (DERIVED, at `1a6873936`), not the spec's 1630 (PINNED, its §4).
- AC4's arm and unit 64's: unit 64 added `test_extract_env_dropped`, whose child runs `main` under both
  variables planted and reads what `rl_model.resolve_remote` resolves. `test_gov_remote_scrub` reads the
  scrub statements themselves, by `ast`, compiled alone: their form, a child with neither variable set
  and a child with both planted, reading `os.environ` after them. One fact per arm: the effect on
  `main`'s arms stays unit 64's, the statements' form and no-raise run are this arm's, and no check of
  one repeats a check of the other.
- S4 is met at this base: `tools/runlog/selftest.py#main` pops both with a `None` default ahead of its
  `try`, so no pop is edited.
- The refusal sites stay at the ceiling, `ceiling tools/unattended/unattended.sh 347/347` (DERIVED,
  `python tools/memory-tree/check-arms.py --report` after the edit): the new refusal is a `return 2`.
- The `help/loop.md` anchor reads `verb:unattended.sh:--mail 4c1a862e` after the edit (DERIVED,
  `python tools/govkit/docs_leg.py --fingerprints`), unmoved, since the usage row's flags did not change.
  The help page's duplicate sentence, which named "an ack already on the remote that your mailbox does
  not yet read as `acked`", is reworded: after the strict fetch such an ack is the skip, so the refusal
  left is a message under the ack's own id that is no ack of that id.
- `python tools/codebase-map/gen_map.py --write` rewrote `memory/map/generated/symbols.json` alone,
  gaining `test_gov_remote_scrub`, `read_main_scrub` and `GOV_SCRUB_VARS`.
- S20's ids: no minting verb prints a next id, so the ids were derived, not typed:
  `python tools/memory-tree/corpus_ids.py --print-defined-ids` read the family's highest defined id as
  `KICK-dKeptSession-69` at `1a6873936`, so the nine rows take `-70` to `-78`.
- S26 and the spec's `memory/builds/dKeptSession/spec/` row: no reconcile ran in this pass, so no spec's
  leg line moved; the rule is observed by AC6's fixture.
- S10's blob pin: `blk` is `tools/lib/resolve-python.test.sh#blk`, its blob `5d283eae4e07` at this base
  (DERIVED, `git rev-parse`), not the spec's `1498e7db1ab4`; its two markers read as the spec says.

## The budget rows, re-priced (left to the close)

`tools/run-gates/selftest-budgets.txt` is outside this write set; each figure below is the close's to
write.

- `unattended driver selftest shard 8/8` reads 6845 (PINNED, the row at `1a6873936`). The new block's
  driver calls, run alone by the scratch probe over a bare origin and two clones on this node,
  read 30s (DERIVED, the probe's own clock, 2026-11-23); x1.5 is 45, so the row reads 6890 (DERIVED, 6845 + 45),
  or 6962 with the 39s and 33s units 63 and 64 left owed beside it (DERIVED, the sums; unit 64's ledger).
- `runlog selftest` reads 117 (PINNED, the row at `1a6873936`). The new arm, imported and run alone by a
  `python -I` probe, read 0.54s (DERIVED, the probe's clock); r 77.4s plus 0.54s is 77.94s, x1.5 is
  116.9, so the row stays 117 (DERIVED, that sum).
- `loop transition record` reads 458 (PINNED, the row at `1a6873936`, `plants=40`, the same as
  `len(PLANTS)` in `tools/loop/loop_transition.py`). This unit adds no plant, but every real
  `--mail ack` call a plant makes now adds one `local sent` read: `acks-landed` alone by direct CLI read
  7.01s over the base driver and 7.37s over this one (DERIVED, `time`, 2026-11-23), 0.36s per call.
  ESTIMATE, at most ten such calls across the ack plants and `chain-two-dependents` (DERIVED, the plant
  descriptions in `tools/loop/loop_transition.py#PLANTS`), 3.6s: r 305.3s plus 3.6s is 308.9s, x1.5 is
  463.4, so the row reads 464 (DERIVED, that sum), past the leg's 120s ceiling (PINNED 2026-11-23,
  `tools/gate-legs.json`), which is parked for the owner.
- `manifest-check self-test` reads 5267 (PINNED, the row at `1a6873936`) and stays: no card-store plant
  calls `--mail ack` (DERIVED, `git grep` over `skills/session-kickoff` printing nothing).

## Criteria

**Evidences:** KICK-dKeptSession-65
- AC1 — observed, `mail — already acked g`. Over the scratch probe's fixture, g posted by fy to build:fx, answered by fx's s4 and
  then acked: the ack exited 0 posting one, and g's row read `answered`. A second `--mail ack fx g`
  through the copy printing `DUPCHECK` and `FETCH` printed exactly `FETCH` and `mail — already acked g`,
  exit 0, the tip unmoved; `--mail ack fx g h` exited 0 with one already-acked line, no `DUPCHECK g`,
  and `git rev-list --count` over the two tips printed `1`. RED probe, the base driver copied the same
  way: the second ack of g exited 2 printing `DUPCHECK` and `mail — duplicate`, and the mixed batch
  exited 2 landing nothing.
- AC2 — observed. B's session t5 acked i as fx and pushed; A's `--mail ack fx i` through the same copy
  printed `FETCH` first, `mail — already acked i` and no `DUPCHECK` line, exit 0, the tip unmoved. With
  A's origin URL set to an absent directory the same call printed `FETCH` and
  `mail — not read · the remote did not answer, git fetch exited 128` followed by the URL, exit 2, the tip unmoved. RED probe,
  the base driver: that call printed `mail — local copy` and exited 0.
- AC3 — observed. `grep -c -F -- "--mail ack <slug> [<id> ...]"` printed `1` over the template, the
  verbs guide and the usage row's line of the driver; `--mail ack fx` with no ids exited 0, printing
  nothing, the tip unchanged (the probe's last call).
- AC4 — observed. A `python -I` probe running `test_gov_remote_scrub` in-process: its four checks
  passed. The reader over `main` named both variables, each an `os.environ.pop(<name>, None)`; the
  child with neither set printed `[]`, exit 0; the child with both planted printed `[]`, exit 0; the
  bare-`del` copy graded GOV_REMOTE's statement raising and its child exited on `KeyError`. A second
  probe over five synthetic `main` bodies read a guarded `del` as no-raise and a bare `del`, a pop with
  no default and a pop after the `try` as not.
- AC5 — observed over the scratch repository: unit 64's copy at status OPEN with `policy fixtures` off
  its leg line and a tracked stub at the workflow template printed the `[guards]` hit
  `policy fixtures <- tools/workflows/unattended-build.template.js` and no
  `SPEC_GUARD_LEGS_CUTOFF blank (arm off)` line; with the name on the leg line, no `[guards]` hit. RED: with the manifest
  declaring the directory guard alone, no `[guards]` hit printed.
- AC6 — observed over the same repository, `planted leg <- tools/loop/loop_transition.py`: the name sets
  of the two manifests compared to `added ['planted leg'] dropped []`; unit 61's copy, stubs at its two loop paths, printed
  that hit and no `[path]` hit under `tools/loop/`, and after the step no `[guards]`
  hit. The rename compared to `added ['real leg two'] dropped ['real leg']`; the copy naming `real leg`
  printed its `[leg]` hit, and after the step, the old name off, neither a `[leg]` hit naming it nor a
  `[guards]` hit. RED: the add-only step left the `[leg]` hit for `real leg` standing.
- AC7 — observed by `git diff 1a6873936 HEAD -- tools/unattended/unattended.test.sh`: the SHADOWED line
  is unchanged; the effective `FLOOR_ASSERTIONS` rises 4212 to 4217 and `FLOOR_SHARD_8` 1429 to 1434
  (DERIVED, the diff's five added `same` calls, each unconditional and outside any loop, none taken out),
  each with a `RAISED` line; the block sits in region 8, so no other shard line moves.
- AC8 — observed. The `git grep` printed nothing (exit 1), and `grep -n "sent=True"` over the loop kit's
  transition module printed the parent's chain read in `write_consumed_acks`,
  `read_mail_rows(root, parent, local=True, sent=True)`.
- AC9 — observed. `grep -c -E "KICK-dKeptSession-6[345]"` over dPlacedRequest's BACKLOG printed `0`; over
  the `gov_ref_sh` block, comment lines dropped, the `git log` or `rev-list` count printed `0`, and `1`
  without the filter (DERIVED, at `1a6873936`).
- AC10 — observed. `grep -c "^- SEV · KICK-dKeptSession-"` over the build's BACKLOG printed `3` at the
  pass base and `12` after the edit (DERIVED, both read at the pass), nine more; each new id has its ask
  row under `## Asks`.
- AC11 — observed. `git diff 6123f4611^ HEAD` over the workflow template and over its render printed the
  same changed lines once CRs are stripped, two each (DERIVED, that diff), and
  `grep -c 'candidates for one parallel group'` printed `1` over each; this spec's §7 line names
  `review-protocol parity (kit vs dogfood)`, the leg the close runs over the render unit 64 left.
- AC12 — observed. `blk s` over a scratch file holding `// >>> s`, two lines, `// <<< s` and two trailing
  lines printed the block and no trailing line; the RED copy whose closer reads `^# <<< ` alone ran to
  the end of the file.
- AC13 — observed by reading this ledger: each named text below has its answer, `MET —` or `GONE —`
  line, and `git diff --name-only 1a6873936 HEAD -- memory/builds/dKeptSession/build/` lists this ledger
  alone.
- AC14 — observed at the pass, `"test_gov_remote_scrub"` counted once; the clean re-render read after the commit is owed to the close:
  `python tools/memory-tree/gen_build_index.py --write` ran before the commit and its output is
  committed, and `grep -c '"test_gov_remote_scrub"' memory/map/generated/symbols.json` printed `1`.
- seen-red — `runlog selftest` — red `f6a0d7aaf` — green `f6a0d7aaf` — `test_gov_remote_scrub`: the scrub is a bare `del`

## The unit 64 texts answered (AC13)

`KICK-dKeptSession-64` S1 reads: "Then the "already acked" read: that same row's `state`, its fourth
column, reads `acked`, unit 5 S7's state for a cached ack naming the id in `answers`; no second read is
made." Answered by KICK-dKeptSession-65 S1, S2 and S12: the skip reads the `kind` and `answers` columns
of `read_mailbox <slug> local sent`, whatever the state, after a `strict` read; a row both answered and
acked reads `answered` by unit 5 S7's precedence, so the state column misses that ack.

`KICK-dKeptSession-64` S3 reads: "A batch whose every id S1 skips exits 0 and writes nothing. A mixed
batch lands only the ids not skipped, in one `write_mail_ref`, and exits as that write does." Answered by
KICK-dKeptSession-65 S3: it holds for an id answered and then acked (AC1).

`KICK-dKeptSession-64` S7 reads: "This unit's own ledger carries the lines of units 58 to 61 by that
rule". Answered by KICK-dKeptSession-65 S7: the population is derived by
`python tools/check-spec-tokens.py --legs-for` over each unit's Files touched, never lines fixed in advance;
unit 64 is a member by its workflow template, which trips `policy fixtures`, so its line is a leg list
naming it.

`KICK-dKeptSession-64` S9 reads: "every leg that the reconciled base's `tools/gate-legs.json` declares
and HEAD's did not is added to the backtick leg line of every non-terminal spec of this build that the
guards join names for it". Answered by KICK-dKeptSession-65 S26: the comparison runs both ways, a name
HEAD's manifest declares and the base does not coming off every such leg line, and a renamed leg is the
pair (AC6).

`KICK-dKeptSession-64` S10 reads: "The place is `tools/runlog/selftest.py#main`, beside its
`CLAUDE_CODE_MAX_CONTEXT_TOKENS` pop and ahead of its arm loop". Answered by KICK-dKeptSession-65 S4:
each pop reads as `os.environ.pop(<name>, None)`, met at this base.

`KICK-dKeptSession-64` AC8 reads: "whose `tools/gate-legs.json` declares `policy fixtures` with guard
`{prefix}/policy/`, over a copy of unit 60's spec". Answered by KICK-dKeptSession-65 S7: it reads as also
declaring the file guard on the workflow template and copying unit 64, so the probe shows a file-level
hit (AC5).

`KICK-dKeptSession-64` AC9 reads: "over a copy of unit 61's spec with that name left off its leg line,
the join prints `planted leg <- tools/loop/...`". Answered by KICK-dKeptSession-65 S10: the copy holds
tracked stubs at unit 61's two loop-kit paths, `tools/loop/loop_transition.py` and `tools/loop/README.md`,
and none at `tools/loop/placement.py` (AC6).

`KICK-dKeptSession-64` AC10 reads: "a statement of `main`'s body ahead of its `try` removes `GOV_REMOTE`
and `GOV_DEFAULT_BRANCH` from `os.environ`". Answered by KICK-dKeptSession-65 S14 and S15: either
no-raise form is accepted, and the statements run alone in a child with neither variable set raise
nothing (AC4).

`KICK-dKeptSession-64` AC11 reads: "the last `FLOOR_ASSERTIONS=` and `FLOOR_SHARD_8=` lines each rise by
the counted cases of 63's arm and of this unit's S1 and S3". Answered by KICK-dKeptSession-65 S9: every
`FLOOR_SHARD_<k>=` line whose region holds a changed case moves by that region's share, the shares
summing to the effective rise; today region 8's is the one line (AC7).

`KICK-dKeptSession-64` §3 reads: "The report's left-shift gates: the ledger lint, the spec-tokens checks
and the reconcile step in the lander are each a separate gate". Answered by KICK-dKeptSession-65 S20:
each gate of the left-shift table has its owner, an ask row filed in this build's BACKLOG with its `SEV ·`
row: `KICK-dKeptSession-70` to `KICK-dKeptSession-75` for the round-4 audit's rows 1 to 6,
`KICK-dKeptSession-76` and `KICK-dKeptSession-77` for this audit's rows 7 and 8, and
`KICK-dKeptSession-78` for the bug-class checklist entries of row 9.

`KICK-dKeptSession-64` §4's sketch reads: "read_mailbox <slug> soft, once" and "the row's state column
-> acked: skip". Answered by KICK-dKeptSession-65 §4's sketch, which takes its place: an empty list exits
0 first, then `read_mailbox <slug> strict` once, `read_mailbox <slug> local sent` once, and per id the
row of the strict read, then an ack from `<slug>` answering the id in the `sent` rows.

`KICK-dKeptSession-64` §4 Files touched reads: "`memory/builds/dKeptSession/spec/`: S9's leg lines, at
reconcile". Answered by KICK-dKeptSession-65 S26: the leg lines move both ways at a reconcile; none ran
in this pass.

`KICK-dKeptSession-64` §4's S1 alternatives read: "the `acked` state of unit 5 S7 is the one predicate
that says an ack exists" and "A second mailbox read for the acked state, for S1. The addressed-to
check's read already prints the state, so a second read is a second fetch for one fact." Answered by
KICK-dKeptSession-65 S2 and S1: false, since a row both answered and acked reads `answered`; and the
second read is `local`, so it makes no fetch.

`KICK-dKeptSession-64` §7's runlog arm reads: "New arm: tools/runlog/selftest.py · covers AC10 · an
in-process `resolve_remote` over a remote-less scratch repository in a process started under
`GOV_REMOTE=planted`". Answered by KICK-dKeptSession-65 S5: two processes, one with both variables
planted and one with neither, this unit's `test_gov_remote_scrub`; unit 64's arm keeps its own fact.

`KICK-dKeptSession-64` §7's leg line names `policy fixtures` and no
`review-protocol parity (kit vs dogfood)`. Answered by KICK-dKeptSession-65 S21: this unit's §7 carries the parity leg, which the close
runs over the render unit 64 left.

## The unit 63 text answered (AC13)

GONE — KICK-dKeptSession-63 rev-5 · AC14's `build_arm_env` clause, "an environment without
`GOV_REMOTE`": AC14 read whole at rev-5 greps `main`'s pops and names no `build_arm_env` return.

## The met findings (AC13)

- MET — 2 · KICK-dKeptSession-63 rev-5 S14 and AC14: the unset sits in `#main`, and AC14 greps its pops.
- MET — 5 · KICK-dKeptSession-64 rev-5 AC8: it names `SPEC_GUARD_LEGS_CUTOFF` beside its `scratch`
  recipe, cites no line number, and its §4 sentence naming `#derive_legs_path` reads as naming the key too.
- MET — 7 · KICK-dKeptSession-64 rev-5 S18 and AC18: with no ask row, neither names a TOOL-dPlacedRequest-13
  item, and each outside item is spelled with its id.
- MET — 8 · KICK-dKeptSession-64 rev-5 S17: `tools/runlog/extract.py#_check_inside` and
  `#scan_preflights` cited by symbol, the callers taken from `git grep`; unit 64's ledger answers 63's
  sentence quoting "glob alone".
- MET — 9 · KICK-dKeptSession-64 rev-5 AC8: its fixture is built as the spec-token checker's self-test
  builds one in its `scratch` function, with `SPEC_GUARD_LEGS_CUTOFF` set as its guards arms set it.
- MET — 12 · KICK-dKeptSession-64 rev-5 §4 Evidence and §7: the manifest declares `policy fixtures`,
  with no summary of its guard list; at this base the leg carries 88 guards (DERIVED, a `python -c`
  count over `tools/gate-legs.json` at `1a6873936`).
- MET — 16 · KICK-dKeptSession-64 rev-5 S5 and AC5, over KICK-dKeptSession-61 S1: no `read_mail_chain`
  or `--mail chain` is minted (AC8).
- MET — 18 · KICK-dKeptSession-64 rev-5 S13: no dPlacedRequest ask row is filed, so dPlacedRequest's
  BACKLOG, `memory/backlog/TOOL.md` and its README move in neither unit (AC9).
- MET — 22 · KICK-dKeptSession-63 rev-5 S15: the usage row, the form refusal and the shipped texts spell
  `--mail ack <slug> [<id> ...]`, and an empty list exits 0 (AC3).
- MET — 23 · KICK-dKeptSession-63 rev-5 S16: a chained landing's feed lines come from the caller naming
  its lower commits to `write_gov_ref`; no walk exists, and no ask row is filed (AC9).
- MET — 25 · TOOL-dWitnessedBar-26 S4: `tools/lib/resolve-python.test.sh#blk` matches opener and closer
  as `^(# |// )`, so no `MARKER_LEAD` is minted (AC12).

Units 61, 63 and 64 are CLOSED, so no spec or ledger of theirs is written (F4, (b)).

## Owed to the close

- The two `New arm:` lines' RED-first observations: the driver block in region 8 staged red by a scratch
  `unattended.sh` whose skip reads the state column and whose read is `soft`, and `test_gov_remote_scrub`
  staged red by a copy whose scrub is a bare `del`.
- Every §7 leg, the shard 8 row and the runlog suite whole, and
  `shell hygiene (a loop fed by a command substitution)`, which the scratch-guard refused this pass.
- AC14's re-render read after the commit, and the budget rows above.
