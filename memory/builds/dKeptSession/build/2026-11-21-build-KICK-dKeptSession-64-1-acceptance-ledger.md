# KICK-dKeptSession-64 — acceptance ledger

**Serves:** journal KICK-dKeptSession-64

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32 at
the pass's base `30fef6346` over the working tree: by a scratch probe of the driver's `--mail` verbs built
from the suite's own helper and block lines (its `mkconf`, `seed_mail_at`, unit 5's two-clone mailbox
fixture and this unit's new block, run alone) over a bare origin and two clones under `%TEMP%`, never
the suite; by the runlog suite's new arm called in-process by a `python -I` probe, never the suite; by a
scratch repository under `%TEMP%` built as the spec-token checker's own fixture is built, running the
checker with `--spec`; by `python tools/check-spec-tokens.py --legs-for`, a query and not a gate, over
each unit's Files touched; and by the greps the criteria state.

## Reconciled at this base

The spec is rev-5, grounded at `ab9f0545`; every unit before it has landed, the last merges unit 63's at
`9c2233140`. What the build found and how it was reconciled:

- S1 and S3 were largely landed by unit 63: the batched ack already dedupes, reads the state off the one
  soft read's row, skips an `acked` row naming it on stderr, and exits 0 writing nothing on an emptied
  list. Unit 63 put the acked read ahead of the addressed-to check; this pass puts it after, as S1 orders
  it. The two orders agree on every input, since a row reading `acked` is a row the read holds, and the
  comment now states S1's order.
- S2 was not landed: an rc 1 of `check_mail_duplicate` reached the ack as `write_mail_post`'s exit 1.
  `tools/unattended/unattended.sh#write_mail_post` now binds `MAIL_DUPLICATE` to the id on that branch,
  empty on every other exit, and `#write_mail_ack` reads an exit 1 with it set as 2. `--mail post` and
  `--mail answer` keep their exits.
- The driver suite's floors read `FLOOR_ASSERTIONS` 4206 and `FLOOR_SHARD_8` 1423 at this base, not the
  spec's 4137 and 1354 (DERIVED, the last assignment of each at `30fef6346`); the shadowed pin reads 675
  (DERIVED, the same read). The runlog suite's `ASSERTION_FLOOR` read 1646, not 1630 (DERIVED, that
  read).
- §4's grep, `git grep -n -i 'parallel group' -- tools memory/map`, printed 7 lines (DERIVED, at `30fef6346`)
  at this base, not the spec's eight: unit 63's S24 reworded the `gen_build_index.py` comment to "one
  step", so it no longer spells the phrase. S16's population is the 6 lines (DERIVED, the same grep)
  left beside the excluded template line.
- S10 is met by unit 63: `tools/runlog/selftest.py#main` pops both variables ahead of its `try`, so no
  edit moves the pop. §7's runlog arm is added on top of it (AC10).
- S5, S13, S14 and S18 are met as the spec states; no code edit is owed for them.
- The refusal sites stay at the ceiling, `ceiling tools/unattended/unattended.sh 347/347` (DERIVED,
  `python tools/memory-tree/check-arms.py --report` after the edit): S1 moved one line, S2 adds an
  `rc=2` assignment and a variable, and S15 edits comments. The `help/loop.md` anchor reads
  `verb:unattended.sh:--mail 4c1a862e` after the edit (DERIVED, `python tools/govkit/docs_leg.py
  --fingerprints`), unmoved, since the usage row's flags did not change.
- `python tools/codebase-map/gen_map.py --write` rewrote `memory/map/generated/symbols.json` alone,
  gaining `test_extract_env_dropped`; it already held `derive_kit_imports`.

## The sibling texts superseded (S2, S4, AC2, AC4)

`KICK-dKeptSession-5` S5 reads: "It prints `mail — posted <id> · <ref>`, exit 0; a duplicate or a lost
write exits 1; a refusal or a write not completed, 2." Answered by KICK-dKeptSession-64 S2 for `--mail
ack` alone: an id read as `acked` is skipped and never reaches the duplicate check; an rc 1 on an id not
read as acked refuses the batch with exit 2; exit 1 stays a lost write. `--mail post` keeps unit 5's
exits.

`KICK-dKeptSession-22`'s red-case row "a post retried after a crash, same session", whose disposition is
`check_mail_duplicate` rc 1, refused: answered by KICK-dKeptSession-64 S2. For `--mail ack` that refusal
exits 2, and a retried ack whose row already reads `acked` is the skip, exit 0.

`KICK-dKeptSession-59` §4 "The case" sketches the literal read as `re.search(r"MIRROR_KIT_INPUTS\s*=\s*(\[[^\]]*\])",
text)`. Answered by KICK-dKeptSession-64 S4: superseded by 63 S8 and S26, the read anchored on the
declaration under `re.M` and taken by `findall`, exactly one declaration per JS list.

`KICK-dKeptSession-61` AC3 reads: "it prints `loop: fixture · sent fy · 4 row(s) · seq and after on 4`".
Answered by KICK-dKeptSession-64 S4 and S5: the chain read is the one reader's `sent` selection, the
`chain-two-dependents` plant of `tools/loop/loop_transition.py` reading a parent's rows through
`#read_mail_rows` with `sent=True`; no `read_mail_chain` and no `--mail chain` exist (AC5).

GONE — KICK-dKeptSession-61 rev-10 · §4 Files touched's "`derive_mail_chain` and its caller": the
section read whole at rev-10 names `derive_mail_chain`, `read_mail_rows` and `write_consumed_acks`, and
`grep -c "and its caller"` over the spec printed `0` (DERIVED, that command).

`KICK-dKeptSession-61` §5 reads: "`--mail read <parent> --local --sent` prints the rows the placement
read." Answered by KICK-dKeptSession-64 S5: true as it stands, the verb unit 21's `--local` with unit
61's `--sent`.

`KICK-dKeptSession-61` §7's arm reads: "New arm: tools/loop/loop_transition.py · covers AC1 AC2 AC3 · the
two-dependent take-over plant". Answered by KICK-dKeptSession-64 S5 and S7: the plant runs under `loop
transition record`, which the manifest declares; no `loop selftest` leg and no `tools/loop/selftest.py`
exist.

`KICK-dKeptSession-62` S19 reads: "`derive_main_transcripts` applies `extract.py#_check_inside` against
the resolved root, the rule `scan_preflights` applies today, and its docstring says so". Answered by
KICK-dKeptSession-64 S4 and S17: the callers are the set the grep below prints, `#scan_preflights` one
of them.

`KICK-dKeptSession-62` S31 reads: "`gen_build_index.py#render_order`'s docstring reads that units sharing
an `order` value are a step whose Parallel cell `derive_parallel_step` derives." Answered by
KICK-dKeptSession-64 S16: true, and every other shipped text that names the group says "candidates for
one parallel group".

GONE — KICK-dKeptSession-62 rev-5 · §5's "seven definitions": §5 read whole at rev-5 holds no such
passage; it survives only in the Edges bullet to this unit (DERIVED, `grep -n "seven definitions"` over
the spec printing that one bullet).

`KICK-dKeptSession-62` S15 and §4's ack-chain sketch: answered by KICK-dKeptSession-64 S1 to S3. In S15
and §4's ack-chain sketch the chain lands every ack or none; this unit orders each id's checks, the
addressed-to check, then the `acked` skip, then the duplicate check, and fixes the exits at 0, 1 and 2.

Units 5, 22, 59, 61 and 62 are CLOSED, so no spec or ledger of theirs is written (F2, (b)).

## The unit 63 texts superseded (AC17, AC19)

`KICK-dKeptSession-63` S7 reads: "That block reads the chain over a two-dependent clone through `--mail
read <slug> --local --sent`, and the floors rise with it." Answered by KICK-dKeptSession-64 S11:
`tools/unattended/unattended.test.sh` is a withheld suite, run by no leg of `tools/gate-legs.json` but by
the kit's shard runner and the `unattended driver selftest shard <k>/8` rows; the floors that rise are the
effective `FLOOR_ASSERTIONS` pin and `FLOOR_SHARD_8`, never the SHADOWED one, and the close observes the
case by running its shard row.

`KICK-dKeptSession-63` S11 reads: "no `read_mail_chain` or `--mail chain` is minted". Answered by
KICK-dKeptSession-64 S5: true as it stands (AC5).

`KICK-dKeptSession-63` S13 reads: "this unit's pass observes the step over every non-terminal spec of
this build itself." Answered by KICK-dKeptSession-64 S8, S9 and S19: on a tree whose manifest lacks the
leg that observation cannot fail, so the step's liveness is AC8's scratch probe; at each reconcile the
reconcile pass adds every leg the reconciled manifest declares and HEAD's did not, derived from the two
`name` sets, to the leg line of every non-terminal spec the guards join names for it, and records the
join's output.

GONE — KICK-dKeptSession-63 rev-5 · S13's "This unit's pass re-checks the step on its own tree": §2
read whole at rev-5 holds S13 as quoted above, and `tr -s ' \r\n' ' '` over the spec piped into `grep
-c` printed `0` (DERIVED, that command).

`KICK-dKeptSession-63` S14 reads: "`tools/runlog/selftest.py#main` pops both beside its
`CLAUDE_CODE_MAX_CONTEXT_TOKENS` pop, before any arm". Answered by KICK-dKeptSession-64 S10: met at this
base, and the new `test_extract_env_dropped` arm holds it (AC10).

`KICK-dKeptSession-63` S15 reads: "Each other id passes `KICK-dKeptSession-5` S8's addressed-to check,
and its ack passes S5's `derive_message_id` and `check_mail_duplicate`, before any commit is built."
Answered by KICK-dKeptSession-64 S1 to S3: the addressed-to check runs first on each id, then the
`acked` skip, and only an id not skipped reaches the duplicate check, whose rc 1 exits 2.

`KICK-dKeptSession-63` S17 reads: "A line names a leg carrying no `guard`, such as `loop transition
record`, only when `tools/gate-legs.json` at that pass carries it". Answered by KICK-dKeptSession-64 S7:
the class, for every leg a line names; the lines below follow it.

`KICK-dKeptSession-63` S24 reads: "The build-order verb comment above
`tools/memory-tree/gen_build_index.py#ORDER_RE` reads that units sharing an `order` value are one step".
Answered by KICK-dKeptSession-64 S16: the population is derived by the grep, and every line it prints
outside the excluded template says "candidates for one parallel group" (AC16).

`KICK-dKeptSession-63` S25 reads: "So no `MARKER_LEAD` is owed." Answered by KICK-dKeptSession-64 S14:
met, AC14 observed below.

`KICK-dKeptSession-63` AC9 reads: "the lines for units 58, 59 and 60 name `policy fixtures`, and the line
for unit 61 names `loop transition record`." Answered by KICK-dKeptSession-64 S6: AC9 reads as S7's
class, one line per unit of the population its query derives, never lines fixed in advance (AC6).

`KICK-dKeptSession-63` AC13 reads: "every spec for which it prints `policy fixtures` on a row not marked
`broad` carries that name on its §7 leg line." Answered by KICK-dKeptSession-64 S19: the criterion is
the `spec tokens (a spec's own names resolve)` leg's `guards` hits, the join
`tools/check-spec-tokens.py#scan_live_spec` makes, which prints no `<leg> <- <path>` hit for a spec of
this build at the reconciled tip; the query's population is withdrawn from this criterion.

`KICK-dKeptSession-63` AC15 reads: "A second `--mail ack <slug> <a>` prints `mail — already acked <a>`
and exits 0". Answered by KICK-dKeptSession-64 S3: true, and a mixed batch `<a> <c>`, `<a>` acked, lands
only `<c>`'s ack, in one commit (AC3).

`KICK-dKeptSession-63` AC24 reads: "`grep -c 'the parallel group' gen_build_index.py` ... prints `0`".
Answered by KICK-dKeptSession-64 S16: true, and the wider population holds the phrase only as
"candidates for one parallel group".

`KICK-dKeptSession-63` §4 Evidence reads: "56 S21 folds them into `derive_main_transcripts`, and 62 S18
and S19 fold `scan_preflights` and apply `_check_inside` there." Answered by KICK-dKeptSession-64 S17:
`tools/runlog/extract.py#_check_inside` has several callers, the set `git grep -n "_check_inside(" --
tools/runlog/extract.py` prints at this pass, five call lines beside the definition (DERIVED, that grep
at `30fef6346`), and `#scan_preflights` is one of them.

GONE — KICK-dKeptSession-63 rev-5 · §4 Evidence's "glob alone": the section read whole at rev-5 holds the
sentence quoted above, and the `tr` and `grep -c` read over the spec printed `0` (DERIVED, that command).

GONE — KICK-dKeptSession-63 rev-5 · "a selftest leg runs when": §2, §4 and §7 read whole at rev-5 hold no
such passage, and the `tr` and `grep -c` read over the spec printed `0` (DERIVED, that command).

`KICK-dKeptSession-63` §4 Files touched names `tools/runlog/selftest.py` for S14 and no
`memory/map/generated/symbols.json`. Answered by KICK-dKeptSession-64 S20: the map's render compares
that file's top-level functions, so `gen_map.py --write` re-renders it; it holds `derive_kit_imports`, and
this pass re-renders it for its own arm (AC20).

`KICK-dKeptSession-63` §7's first arm line reads: "`FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` rise by the
arm's count, counted off the diff". Answered by KICK-dKeptSession-64 S11: the effective pin, the file's
last `FLOOR_ASSERTIONS=` assignment, and `FLOOR_SHARD_8` rise, each with a `RAISED` line; the suite is
withheld and runs by its shard row, not by a leg.

`KICK-dKeptSession-63` §8 F1 reads: "The commits between are named by the caller rather than walked".
Answered by KICK-dKeptSession-64 S13 and S18 and its own §8 F1, re-resolved (e): `write_mail_ref` names
its chain's lower commits and every other caller names none, so no walk exists (AC13, AC18).

Unit 63 is CLOSED, so neither its spec nor its ledger is written (F2, (b)).

## S6 and S7 — the population's lines

63's population is units 57 to 62 (DERIVED, its S9). `python tools/check-spec-tokens.py --legs-for` ran
at this base over the paths `tools/check-spec-tokens.py#extract_files_touched` reads from each unit's
Files touched. `tools/gate-legs.json` at this pass declares `policy fixtures` and `loop transition
record` and no `loop selftest` (DERIVED, its `name` set read at the pass). By S7's rule, the lines for
units 58 to 61:

- GAP — unit 58 · exit 2 · `legs-for: REFUSING — no path given, so there is nothing to join` (DERIVED,
  the query at the base): its Files touched declares none. Its own §7 leg line names `policy fixtures`,
  which the manifest declares.
- OBSERVED — unit 59 · exit 0 · `tools/policy/check_policy.py`: routed-commits selftest, scratch-guard
  self-test, policy fixtures; `memory/map/generated/symbols.json`: recall floor, recall floor arms ·
  every `tools/` path's broad rows left out (DERIVED, the query at the base).
- OBSERVED — unit 60 · exit 0 · `tools/policy/README.md`: routed-commits selftest, scratch-guard
  self-test, policy fixtures; `tools/policy/policy.py`: build-index selftest, gotchas selftest,
  routed-commits selftest, recall floor, recall floor arms, scratch-guard self-test, memory-recall kit
  selftest, policy fixtures · broad rows left out (DERIVED, the query at the base).
- OBSERVED — unit 61 · exit 0 · `tools/unattended/unattended.sh`: scratch-guard self-test, tier2-review
  self-test; `memory/guides/UNATTENDED-VERBS.md` and its acceptance ledger: recall floor, recall floor
  arms; `tools/unattended/unattended.test.sh`, `tools/loop/loop_transition.py`, `tools/loop/README.md`,
  `tools/run-gates/selftest-budgets.txt`, `tools/unattended/VERBS.template.md` and `help/loop.md`: no
  guarded leg · beside the query, `loop transition record`, which its §7 names to run its plant and
  which the manifest carries with no `guard` (DERIVED, the query at the base).

63's own lines for these four units name only legs the manifest at this pass declares, so no 63 line is
quoted as breaking the rule (DERIVED, the legs each names read against the `name` set).

## Criteria

**Evidences:** KICK-dKeptSession-64
- AC1 — the driver probe: a scratch copy of the driver whose `check_mail_duplicate` prints `DUPCHECK <id>` on stderr acked a from session s3, exit 0, printing one DUPCHECK line; the second `--mail ack fx a` printed exactly `mail — already acked <a>` and no DUPCHECK line, exited 0, and the s3 ref's tip read by `git rev-parse` was the first call's (DERIVED, that probe).
- AC2 — this ledger answers unit 5's S5 exit and unit 22's retry row by this unit's id, above; `grep -c "already acked"` printed `1` over each of `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md` and `help/loop.md`, each sentence stating exit 0 for a skip, 1 for a lost write and 2 for a refusal; `grep -c "the post's exits"` over the usage row's line printed `0` (DERIVED, those commands). The `tr` and `grep -c` reads over this ledger are made at the commit, and the main loop confirms them.
- AC3 — the driver probe: `--mail ack fx a c`, a acked, exited 0 naming a already acked, `git rev-list --count <tip before>..<tip after>` printed `1`, and fy's mailbox read one ack of a and one of c; `--mail ack fx a a` exited 0, the tip unmoved (DERIVED, that probe).
- AC4 — this ledger holds an answer by this unit's id or a `GONE —` line for unit 59's sketch, unit 61's AC3, §4 Files touched, §5 and §7 arm, and unit 62's S19, S31, §5 and S15 and §4's ack-chain sketch, above; unit 62's S19 is quoted once. The `tr` and `grep -c` read is made at the commit.
- AC5 — `grep -c -e read_mail_chain -e "--mail chain"` printed `0` over each of the four files, and `grep -n "sent=True" tools/loop/loop_transition.py` printed the guard's parent read, `read_mail_rows(root, parent, local=True, sent=True)`, among its hits (DERIVED, those commands).
- AC6 — the probe re-derived 63's population, units 57 to 62, by the query over each unit's Files touched, and read 63's ledger: each unit carries exactly one line, opening `OBSERVED —` or, for unit 58, `GAP —`, and that ledger lists the population (DERIVED, that probe).
- AC7 — every leg named on the four lines above is a `name` of `tools/gate-legs.json` at this pass, read by `python -c`, and unit 61's line names `loop transition record`; no line names `loop selftest` (DERIVED, that read).
- AC8 — in a scratch repository under `%TEMP%` built as the checker's `scratch` fixture builds, `SPEC_GUARD_LEGS_CUTOFF="2026-09-01"` staged as its guards arms stage it, the manifest declaring `policy fixtures` guarded on `tools/policy/` and tracked stubs at unit 60's two policy paths, `--spec` over a copy of unit 60's spec at status OPEN with the name left off its leg line printed `[guards] \`policy fixtures <- tools/policy/README.md\``, and with the name on it printed no such hit (DERIVED, that probe). A first run with the key committed refused it as not strictly past the commit day, which is why the key is staged, never committed.
- AC9 — over the same repository, the `python -c` compare of the base manifest's `name` set with a reconciled one adding `planted leg` guarded on `tools/loop/` printed `['planted leg']`; `--spec` over a copy of unit 61's spec at status OPEN printed `[guards] \`planted leg <- tools/loop/loop_transition.py\``, and with `planted leg` added to its leg line it printed no `[guards]` hit (DERIVED, that probe).
- AC10 — the `ast` probe: `main`'s statements ahead of its `try` hold `os.environ.pop('GOV_REMOTE', None)` and `os.environ.pop('GOV_DEFAULT_BRANCH', None)`, and `build_arm_env`'s body names neither (DERIVED, that probe). The new arm `test_extract_env_dropped`, called in-process, passed its two checks: a child under both planted runs `main` over one injected arm reading `('', '', '', '')`, and `model` imported alone under the plant refuses naming GOV_REMOTE. The same child over a source with the two pops removed read the refusal `GOV_REMOTE names planted, which is no remote of this repository`, the RED (DERIVED, those probes).
- AC11 — the diff from `fb72d2a5f`, the parent of unit 63's pass, leaves `FLOOR_ASSERTIONS=675  # SHADOWED` unchanged; the effective `FLOOR_ASSERTIONS` rose 4199 to 4206 by unit 63's 7 and 4206 to 4212 by this unit's 6, and `FLOOR_SHARD_8` 1416 to 1423 and 1423 to 1429, each with a `RAISED` line (DERIVED, the diff at the pass). The `git diff` read over the commit is the main loop's to confirm.
- AC12 — the template was edited and copied whole to its render; `diff` over the two CR-stripped `sed` substitutions printed nothing (DERIVED, that command).
- AC13 — `grep -n "write_gov_ref "` over the three files printed, off comment lines, one call with a fourth argument, `write_mail_ref`'s, and every other call at most three, the three `remove_gov_ref` bodies passing `""` third; the three `gov_ref_sh` blocks, each 86 lines, compared byte-equal pairwise (DERIVED, those commands).
- AC14 — `grep -n '>>> \$stem' tools/lib/resolve-python.test.sh` printed the population read carrying `git grep -l -E` and the count carrying `grep -cE`; the count's command over a scratch file holding one `# >>> s` and one `// >>> s` block printed `2`, and the same as BRE printed `0` (DERIVED, those commands).
- AC15 — `git grep -n -i 'parallel group' -- tools/unattended/unattended.sh` printed the order gate's comment and the edge refusal's, each saying "candidates for one parallel group" (DERIVED, that grep).
- AC16 — the grep with the template excluded, piped into `grep -v -i 'candidates for one parallel group'`, printed nothing, and `grep -c 'candidates for one parallel group'` printed `1` over each of `tools/workflows/unattended-build.js` and `tools/workflows/unattended-build.template.js`, the render rewritten by `bash tools/workflows/check-protocol-parity.test.sh --render` (DERIVED, those commands).
- AC17 — this ledger holds an answer by this unit's id or a `GONE —` line for each 63 text listed, above. The three quoted passages each read `0` over 63's spec at its closing rev-5, so each takes a `GONE —` line. The `git diff --name-only` read over the build folder is made at the commit.
- AC18 — over `tools/lib/gov-ref.sh`'s `gov_ref_sh` block, the count with comment lines dropped printed `0` and without the filter `1`; the block's `write_gov_ref` calls `add_feed_event` once per trailing argument on the line before its `write_feed_success` call (DERIVED, those commands).
- AC19 — the answer to 63's AC13 above names the `spec tokens (a spec's own names resolve)` leg's `guards` hits as the criterion and carries no `--legs-for` population; AC8's probe read the join's `[guards]` output, never `print_legs_for`'s (DERIVED, the probe's own grep).
- AC20 — `python tools/codebase-map/gen_map.py --check` exited `0` after the re-render, and `grep -c '"derive_kit_imports"' memory/map/generated/symbols.json` printed `1` (DERIVED, those commands).

## What the close owes

The driver suite's 6 new `same` in the mailbox block of region eight (DERIVED, the block's lines) and the
runlog suite's 2 new checks with their 3 decoy checks (DERIVED, the floor's block); §7's legs; and the two
`New arm:` lines' RED-first observations: a scratch `unattended.sh` running `check_mail_duplicate` before
the state read (AC1, AC3), and a copy of the runlog selftest whose unset sits in `build_arm_env` (AC10).
The S2 case of the new driver block read exit 1 under the base driver at `30fef6346`, its RED (DERIVED,
the probe over a staged copy of that driver).

The driver probe ran this block's fixture, three posts, five ack calls and one read, in 22.1 s (PINNED
2026-11-23, one run on the pass's node). Priced as the earlier units priced theirs, x1.5:
33 s (DERIVED, 22.1 x 1.5 rounded up). So the `unattended driver selftest shard 8/8` row, which reads
6845 at this base (DERIVED, the row read at the pass), would rise to 6878, or to 6917 with unit 63's owed 39 s (DERIVED, the sums). That
row's file, `tools/run-gates/selftest-budgets.txt`, is outside this pass's write set, so the re-price is
the main loop's. The runlog arm ran in 0.3 s (PINNED 2026-11-23, one in-process call), so the `runlog
selftest` row does not move. No loop plant is added, so the `loop transition record` row does not move.
