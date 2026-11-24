# KICK-dKeptSession-63 — acceptance ledger

**Serves:** journal KICK-dKeptSession-63

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32 at
the pass's base `fb72d2a5f` over the working tree: by the one policy case run alone by direct CLI
(`python tools/policy/check_policy.py --fixture mirror-input-parity`), in the worktree and over a staged
copy of the policy kit in a `git init` scratch directory with this tree's `.unattended.conf` beside it;
by a scratch probe sourcing `tools/lib/gov-ref.sh` with `gov-feed.sh` beside it over a bare origin and
one clone; by a scratch probe of the driver's `--mail` verbs over a bare origin and two clones built as
the suite's lease fixture builds them, never the suite; by the runlog suite's two touched arms called
in-process by a `python -I -c` probe, never the suite; and by the greps the criteria state.

## Reconciled at this base

The spec is rev-5, grounded at `ab9f0545`; every unit before it has landed, the last merges unit 62's at
`428c9b1c0`. What the build found and how it was reconciled:

- S12 is met by unit 62. `tools/unattended/unattended.sh#write_mail_ref` already takes `<message>
  [<message> ...]` and lands the chain with one `write_gov_ref`, and `#write_mail_post` gives message k
  the tip read's first-parent count plus k. This unit adds the comment naming that derivation and the
  lower commits S16 names; AC12 is observed over the landed chain.
- S4 is met: THE RULE in `tools/policy/README.md` already names both pairs, so the README is not edited.
- §4's grep, `git grep -n -E "duplicate|already acked" tools/loop`, found no sentence in
  `tools/loop/loop_transition.py` or `tools/loop/README.md` saying an acked id refuses the batch; the loop
  acks open rows alone, so neither file is edited.
- The driver suite's floors read `FLOOR_ASSERTIONS` 4199 and `FLOOR_SHARD_8` 1416 at this base, not the
  spec's 4137 and 1354 (DERIVED, the last assignment of each at `fb72d2a5f`). The new block's 7 `same`
  raise them to 4206 and 1423 (DERIVED, plus seven each). The runlog suite's `ASSERTION_FLOOR` read 1643
  and rises by 3 to 1646 (DERIVED, the three new checks, no new arm and so no decoy check).
- S15's skip moves unit 62's AC13 arm: with a's ack posted, `--mail ack tFix a b` now names a as
  already acked and posts b's ack, exit 0, so that block's first pair is re-armed for the skip and b
  reads `acked`; the KDS61 ack-form arm is re-armed for `--mail ack <slug> [<id> ...]`.
- S14's population, derived by the new `tools/runlog/selftest.py#derive_kit_imports`, is `extract`,
  `model`, `prose`, `record` and `runlog_lib` (DERIVED, the probe at the pass), the spec's five: the two
  roots are left out, and `runlog`, which one arm imports, reads no variable by name.
- Unit 58's Files touched declares no path at rev-6 ("None: S1 and S2 observe unit 34's landed case"),
  so its query refuses with exit 2; S17's rule makes its line a `GAP —` line, and the spec's "prints
  `policy fixtures` for units 58, 59 and 60" holds for 59 and 60 alone. Unit 58's line names the leg its
  own §7 line carries.
- The refusal sites stay at the ceiling, `ceiling tools/unattended/unattended.sh 347/347` (DERIVED,
  `python tools/memory-tree/check-arms.py --report` after the edit): S15 adds `echo` and `return` lines,
  S16 a loop, and the arm's form refusal moved in place. The `help/loop.md` anchor reads
  `verb:unattended.sh:--mail 4c1a862e` after the edit (DERIVED, `python tools/govkit/docs_leg.py
  --fingerprints`), unmoved, since the usage row's `--` flags did not change.

## The sibling texts superseded (AC27)

`KICK-dKeptSession-57` S3 reads: "It records one OBSERVED line per unit, each naming its unit, in this
unit's own acceptance ledger". Answered by S9 and S17 below: this unit's lines record the query's exit
and output, and a refused query writes a `GAP —` line; the lines units 57 and 62 wrote are not rewritten.

`KICK-dKeptSession-60` S1 reads: "THE RULE reads: a unit adding a repository-relative resolution input
adds its path to `LEGACY_INPUTS`; a unit adding a kit-relative input adds its name to
`derive_mirror_inputs` in `policy.py`". Superseded by S4: THE RULE names both pairs, `LEGACY_INPUTS` with
`MIRROR_LEGACY_INPUTS` and `derive_mirror_inputs` with `MIRROR_KIT_INPUTS`, and the README already
reads so at this base.

`KICK-dKeptSession-62` S1 reads: "naming the leg the unit's own §7 names to run its arm at the close".
Superseded by S17: a line names a leg carrying no `guard` only where `tools/gate-legs.json` at the pass
carries it, and otherwise opens `NOT RUN —`.

`KICK-dKeptSession-62` S15 reads: "A refused record or a lost update leaves every row open; one id keeps
today's lines and exits." Superseded by S15: an id whose row reads `acked` is skipped and named on
stderr, a list given empty or emptied by the skip exits 0 writing nothing, and one open id keeps the
post's lines and exits. Its AC13, "it prints `mail — duplicate` and exits 1", reads as the skip, exit 0.

`KICK-dKeptSession-62` §4 "The ack chain" reads: "`write_gov_ref <ref> T c_b` -> one update: both land".
Superseded by S12 and S16: `write_mail_ref` lands the chain and names its lower commits, `write_gov_ref
<ref> T c_b c_a`, whose success exit feeds `c_a`, then `c_b`.

`KICK-dKeptSession-62` S24 reads: "The `mirror-input-parity` case compares the JS list with
`policy.LEGACY_INPUTS` beside its kit-input compare." Superseded by S21: one join, the kit names by
`derive_kit_rel` with the legacy names as they stand, against `derive_mirror_inputs()`.

`KICK-dKeptSession-62` S26 reads: "The runlog selftest gains a class arm: every variable name
`extract.py` reads". Superseded by S14: the arm's population is the import graph's, and `main` pops
`GOV_REMOTE` and `GOV_DEFAULT_BRANCH` beside its window variable.

`KICK-dKeptSession-62` AC25 reads: "the `derive_context_window` range, its docstring removed, grepped with
`grep -cE 'expanduser|\.claude'`, prints `0`". Superseded by S18: the range is first asserted to open
with `def derive_context_window` and to hold more than one line, and only then grepped (AC18).

Units 57, 60 and 62 are CLOSED, so no spec or ledger of theirs is written (F2, (b)).

## S9 and S17 — one line per unit of the population

The population is units 57, 58, 59, 60, 61 and 62, the units this batch lands on. For each,
`python tools/check-spec-tokens.py --legs-for` ran at the base over the paths
`tools/check-spec-tokens.py#extract_files_touched` reads from its Files touched. Each line records the
exit, each path with the guarded legs it trips, and the count of its rows marked `broad`, which every
`tools/` path shares; no row read `UNEVALUATED` and no path `(not tracked at HEAD)` (DERIVED, those six
queries). `tools/gate-legs.json` at this pass carries `loop transition record`, with no `guard` (DERIVED,
the manifest read at the pass). Each exit-0 query closed with
`legs-for: 151 of 224 legs carry no guard and run whatever changed` (DERIVED, those five queries).

- OBSERVED — unit 57 · exit 0 · `.governance/policy.json` no guarded leg; its acceptance ledger: recall
  floor, recall floor arms (DERIVED, the query at the base).
- GAP — unit 58 · exit 2 · `legs-for: REFUSING — no path given, so there is nothing to join` (DERIVED,
  the query at the base): its Files touched declares none at rev-6. Its own §7 leg line names `policy
  fixtures`, which the close runs.
- OBSERVED — unit 59 · exit 0 · `tools/policy/check_policy.py`: routed-commits selftest, scratch-guard
  self-test, policy fixtures, broad 14; `memory/map/generated/symbols.json`: recall floor, recall floor
  arms · names `policy fixtures` (DERIVED, the query at the base).
- OBSERVED — unit 60 · exit 0 · `tools/policy/README.md`: routed-commits selftest, scratch-guard
  self-test, policy fixtures, broad 14; `tools/policy/policy.py`: build-index selftest, gotchas selftest,
  routed-commits selftest, recall floor, recall floor arms, scratch-guard self-test, memory-recall kit
  selftest, policy fixtures, broad 14 · names `policy fixtures` (DERIVED, the query at the base).
- OBSERVED — unit 61 · exit 0 · `tools/unattended/unattended.sh`: scratch-guard self-test, tier2-review
  self-test, broad 14; `tools/unattended/unattended.test.sh`, `tools/loop/loop_transition.py`,
  `tools/loop/README.md` and `tools/unattended/VERBS.template.md`: no guarded leg, broad 14 each;
  `tools/run-gates/selftest-budgets.txt`: broad 21; `memory/guides/UNATTENDED-VERBS.md` and its
  acceptance ledger: recall floor, recall floor arms; `help/loop.md` no guarded leg · beside the query,
  `loop transition record`, which its §7 names to run its plant and which the manifest carries with no
  `guard` (DERIVED, the query at the base).
- OBSERVED — unit 62 · exit 0 · `tools/runlog/extract.py`: format-guard self-test, runlog selftest,
  run-gates run-log line, pre-push run-log line, policy fixtures; `tools/runlog/selftest.py`,
  `tools/runlog/fixtures/transcripts.json` and `tools/runlog/README.md`: runlog selftest, run-gates
  run-log line, pre-push run-log line; `tools/unattended/unattended.sh`: scratch-guard self-test,
  tier2-review self-test; `tools/hooks/scratch-guard.js`: hook destinations self-test, scratch-guard
  self-test, format-guard self-test, agent-cap self-test, verifier fan-out self-test, review-join
  self-test, policy fixtures; `tools/memory-tree/design_lib.py`: playbook render selftest, recall floor,
  recall floor arms, memory-recall kit selftest, policy fixtures; `tools/policy/policy-mirror.js`,
  `check_policy.py` and `README.md`: routed-commits selftest, scratch-guard self-test, policy fixtures;
  `memory/guides/UNATTENDED-VERBS.md` and its acceptance ledger: recall floor, recall floor arms;
  `tools/unattended/unattended.test.sh`, `VERBS.template.md`, `mail-notice.js`,
  `tools/lib/resolve-python.test.sh`, `tools/loop/loop_transition.py` and `README.md`, `help/loop.md`:
  no guarded leg · every `tools/` path's broad rows counted, none listed · beside the query, `loop
  transition record`, which its §7 names and the manifest carries with no `guard` (DERIVED, the query at the base).

## Criteria

**Evidences:** KICK-dKeptSession-63
- AC1 — `grep -c 'files_touched_py'` printed `0` over `tools/check-spec-tokens.py` and `0` over `tools/memory-tree/gen_build_index.py` (DERIVED, those commands at the pass).
- AC2 — in `tools/memory-tree/`, `grep -c 'CITE_TAIL' gen_build_index.py` printed `0` and `grep -c 'read_spec_writes' gen_build_index.py` printed `1` (DERIVED, those commands).
- AC3 — `grep -n 'read_spec_writes' check-spec-tokens.py` printed the line of `extract_files_touched`' own body that calls `load_design_lib().read_spec_writes(text)`, inside that function's range (DERIVED, that command).
- AC4 — `awk '/THE RULE:/,/^$/' README.md | tr '\n' ' '` in `tools/policy/` named `LEGACY_INPUTS`, `MIRROR_LEGACY_INPUTS`, `derive_mirror_inputs`, `MIRROR_KIT_INPUTS` and `mirror-input-parity` (DERIVED, that command): the README is not edited.
- AC5 — `grep -n "MIRROR_LEGACY_INPUTS" policy.py` in `tools/policy/` printed the comment line above `LEGACY_INPUTS`, "and the tuple's JS copy is `MIRROR_LEGACY_INPUTS` in policy-mirror.js" (DERIVED, that command).
- AC6 — the `inspect.signature` probe in `tools/loop/` printed `(rows, chain)` (DERIVED, that probe).
- AC7 — `grep -c -e '--local --sent' unattended.test.sh` printed `3` (DERIVED, that command), unit 61's AC7 block among them.
- AC8 — over the staged kit whose `policy-mirror.js` opens with a comment line spelling `MIRROR_KIT_INPUTS = ["presets.toml"]` while the declaration holds `second.toml` too, the case printed `WRONG: tools/policy/second.toml in the JS lists alone` (DERIVED, that run). The same comment plant under the base's unanchored reader printed `WRONG: policy-mirror.js holds 2 MIRROR_KIT_INPUTS declaration(s), not one`, and the case's own comment plant read WRONG there, the arm's RED (DERIVED, a staged copy of `check_policy.py` with the anchor removed).
- AC9 — the six lines above, one per unit of the population, units 59 and 60 naming `policy fixtures`, unit 58's GAP line naming it from its §7, and unit 61's naming `loop transition record` (DERIVED, the queries at the base).
- AC10 — `tr -s ' \r\n' ' '` over unit 60's spec piped into `grep -c "to the next blank line and joined into one line"` printed `1` (DERIVED, that command).
- AC11 — `grep -c "read_mail_chain" unattended.sh` printed `0` (DERIVED, that command). The equality of `--mail read dA` and the sent read over unit 61's two-dependent clone is unit 61's AC7 block in the driver suite, which the close runs.
- AC12 — the driver probe acked one id from session x1, then `--mail ack tFix b c` on that ref at depth 1: two `mail — posted` lines, exit 0, the tip's `seq` 3 answering c and its parent's `seq` 2 answering b (DERIVED, that probe). The awk range over every `write_mail_` function but `write_mail_ref`, piped into `grep -c -E 'build_gov_commit|write_gov_ref'`, printed `0`, and over all five printed `2`, `write_mail_ref`'s two lines (DERIVED, those commands).
- AC13 — the query over the Files touched of each non-terminal spec, units 63, 64, 65 and 69, printed `policy fixtures` on a row not marked `broad` for 63, 64 and 69, and each of those carries it on its §7 leg line; unit 65 printed none (DERIVED, those queries and greps at the base).
- AC14 — the in-process probe of `test_extract_env_reads` passed its four checks: the population holds extract and model, every variable each module reads is aimed or dropped, and a copy of `model.py` adding `os.environ.get("RUNLOG_PLANTED")` is named `["RUNLOG_PLANTED"]` (DERIVED, that probe). With the two pops taken out of the guarded set, `model` read `['GOV_DEFAULT_BRANCH', 'GOV_REMOTE']`, the RED (DERIVED, that probe). `sed -n '/^def main(/,$p' selftest.py | grep -c -E 'pop\("GOV_(REMOTE|DEFAULT_BRANCH)"'` printed `2` (DERIVED, that command).
- AC15 — the driver probe: `--mail ack tFix d d` posted one ack, exit 0, and the ref held one record answering d; a second `--mail ack tFix d` printed `mail — already acked <d>` and exited 0; `--mail ack tFix` exited 0 printing nothing; `--mail ack tFix a 000000000000` exited 2 naming the unaddressed id; the tip moved on the first call alone (DERIVED, that probe, `git rev-parse` before and after).
- AC16 — over the driver probe's chained pair, `read_first_seen` printed a time for both commits and `--feed check` exited 0 (DERIVED, that probe). The library probe sourcing `tools/lib/gov-ref.sh` with `gov-feed.sh` beside it: a one-commit write naming no lower commit added one feed line; a write landing a three-commit chain naming its two lower commits added three lines in chain order, each read with a first sighting, `check_feed` exit 0; a lost write added none (DERIVED, that probe). The same probe over the base's `gov-ref.sh` added one line for the chain, read `-` for both lower commits, and `check_feed` exited 1 naming them missing, the RED (DERIVED, that probe).
- AC17 — unit 58's query exited 2 and its line opens `GAP —` carrying `exit 2` and the `legs-for: REFUSING` line (DERIVED, the query at the base). A scratch copy of `tools/gate-legs.json` with `loop transition record` removed rendered unit 61's line `NOT RUN — unit 61 · loop transition record is no row of gate-legs.scratch.json`, and the shipped manifest `OBSERVED` (DERIVED, that probe).
- AC18 — S18's range check, which asserts the `derive_context_window` range opens with its `def` and holds more than one line before it greps, printed `range 66 lines, docstring removed, grep -cE prints 0` over `tools/runlog/extract.py`; over a copy whose `def derive_context_window` is renamed it printed `RED: the range is empty` and exited 1 before any grep; over a copy adding an `expanduser("~/.claude/projects")` line it exited 1 printing `1` (DERIVED, those probes).
- AC19 — `tr -s ' \r\n' ' '` over unit 58's own acceptance ledger piped into `grep -c "preset-derived-cap"` printed `1` (DERIVED, that command).
- AC20 — the same over unit 61's own acceptance ledger with `grep -c "over one parent's rows of"` printed `1` (DERIVED, that command).
- AC21 — the case passed in the worktree, its join reading `3 input(s) on each side: .agent-cap.conf, .governance/instructions.toml, tools/policy/presets.toml`, the legacy names unprefixed; over the staged kit whose `MIRROR_LEGACY_INPUTS` declaration is absent it printed `WRONG: policy-mirror.js holds 0 MIRROR_LEGACY_INPUTS declaration(s), not one`, and over one prefixing `.agent-cap.conf` with the kit path it named both spellings (DERIVED, those runs).
- AC22 — `grep -n "derive_mail_chain(" tools/loop/loop_transition.py` printed the definition and three calls, each passing two arguments (DERIVED, that command).
- AC23 — the in-process probe of `test_extract_main_transcripts_inside` passed its three checks, `measure_tree` and `measure_ready_tree` each reading one session over the linked root; with `derive_main_transcripts` replaced by the raw glob both read two, the RED (DERIVED, that probe).
- AC24 — `grep -c 'the parallel group' gen_build_index.py` in `tools/memory-tree/` printed `0`, and `grep -c 'parallel group' memory/map/features/build-readme-surface.md` printed `0` (DERIVED, those commands).
- AC25 — `grep -c -F '(# |// )>>> ' resolve-python.test.sh` in `tools/lib/` printed `3` (DERIVED, that command).
- AC26 — over the staged kit declaring `MIRROR_KIT_INPUTS` twice the case printed `WRONG: policy-mirror.js holds 2 MIRROR_KIT_INPUTS declaration(s), not one`, and over one declaring `MIRROR_LEGACY_INPUTS` nowhere `WRONG: policy-mirror.js holds 0 MIRROR_LEGACY_INPUTS declaration(s), not one` (DERIVED, those runs).
- AC27 — this ledger quotes the nine superseded texts above. The `tr` and `grep -c` reads and the `git diff --name-only fb72d2a5f HEAD -- memory/builds/dKeptSession/build/` read are made at the commit, and the main loop confirms them.
- seen-red — `runlog selftest` — red `f6a0d7aaf` — green `f6a0d7aaf` — `test_extract_main_transcripts_inside`: a transcript linked from outside counted in
- seen-red — `runlog selftest` — red `f6a0d7aaf` — green `f6a0d7aaf` — `test_extract_env_reads`: `model.py` reads a planted variable no arm drops
- seen-red — `policy fixtures` — red `f6a0d7aaf` — green `f6a0d7aaf` — `mirror-input-parity`: a doubled declaration read by its first

## What the close owes

The driver suite's 7 new `same` (DERIVED, the block's lines) and its two re-armed arms, KDS62 AC13's
first pair and KDS61's ack form; the runlog suite's 3 new checks (DERIVED, the floor's block); the policy
case's three plant rows; §7's legs; and the three `New arm:` lines' RED-first observations: a scratch
`unattended.sh` whose `write_mail_ref` names no lower commit (AC12, AC15, AC16), a staged
`check_policy.py` reading the comment's literal (AC8, AC21, AC26), and a copy of `model.py` reading a
planted variable with the measures over the raw glob (AC14, AC23). The parity arm over the three
`gov_ref_sh` copies is owed too; the probe at the pass read the three blocks byte-identical (DERIVED,
a byte compare of the spans between the markers).

The driver probe ran its fixture, four posts and six acks in 25.5 s (PINNED 2026-11-23, one run on the
pass's node), the block's own load. Priced as the earlier units priced theirs, x1.5 is 39 s (DERIVED), so the
`unattended driver selftest shard 8/8` row would rise from 6845 to 6884 (DERIVED, plus 39). That row's
file, `tools/run-gates/selftest-budgets.txt`, is outside this pass's write set, so the re-price is the
main loop's. No loop plant is added, so the `loop transition record` row does not move.
