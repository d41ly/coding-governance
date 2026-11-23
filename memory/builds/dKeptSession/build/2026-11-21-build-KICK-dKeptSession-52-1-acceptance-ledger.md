# KICK-dKeptSession-52 — acceptance ledger

**Serves:** journal KICK-dKeptSession-52

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32
at the pass's base `08c5e6725` over the working tree before the commit: by the unit's plant run alone
by direct CLI (`python tools/loop/loop_transition.py --fixture --plant notices-repeat-key`); by the
same plant over a scratch copy of `tools/` whose `write_dependency_notices` passes no `--pass`; and by
the greps and the Python one-liner AC3 and AC4 state.

Before the first edit the spec's cited code was probed at the base, units 24, 10, 25, 21, 6, 7, 35,
42, 8, 11 and 43 read as landed. `tools/unattended/unattended.sh#derive_message_id` hashes the eight
fields §4 names; `tools/unattended/unattended.sh#check_mail_duplicate` prints
`mail — duplicate <id> · <ref>` and returns 1, and `write_mail_post` calls it; the B21 row takes
`item.build.unit-pass` with outcome `interface-change` back to `designing`, and `flow.rework-budget`
defaults to `4+2`; `MAIL_COLUMNS` holds eleven names, so `read_mail_rows` carries no content key;
`tools/loop/loop_transition.py#write_dependency_notices` takes an `ordinal` and posts `--pass`, and a
non-zero post adds `notice — not posted <kind> to build:<dependent> · rc <n> · <first line>`. Unit 35's
spec is CLOSED at rev-7 and its §4 carries "The content key alone telling exits apart", S3's text.
`PLANTS` held 31 and the `loop transition record` row `plants=31` at value 279 (DERIVED, `len(PLANTS)`
and the grep at `08c5e6725`).

How the build reconciled the spec's text with what landed: §4's budget table counts the plants of units
53 and 55 as possibly landing first; at the base neither had, and unit 11's five had, so the token
moves in place from 31 to 32 (DERIVED, `len(PLANTS)` before and after), one above the count at the
base as §4 states. The plant is a third case of the landed `notices-` branch of
`tools/loop/loop_transition.py#run_transition_fixture`, reusing its rebound launcher and its saved and
restored environment rather than a copy of them; `write_transition_plant` writes `dA` alone for it
(`FX_DEPENDENTS[:1]`). The spec's rule that the unit stops where its reading takes `r` past the leg's
ceiling is superseded for this run by the main loop, which parked the ceiling for the owner: the row
is re-priced and the raise is not made here.

## S2 — the staged red, recorded

The copy was every file of `tools/` at the working tree, with `write_dependency_notices`' post argv
cut to seven values, `--pass` and its ordinal dropped. A copy outside any git repository records no
move: each `record` printed `loop: unanswered · the scenario composition does not read: git rev-parse
--show-prefix failed: fatal: not a git repository`, exit 2, and no post ran. So the copy sat in a
directory given `git init` under the host temp directory, beside the tree's `.unattended.conf`, which
`write_transition_plant` copies from the kit's folder or a parent. There the plant exited 1 and printed,
at the third Design exit:

    notice — not posted changed to build:dA · rc 1 · mail — duplicate cece2f8f0718 · refs/gov/remote/mail/tFix/a/s-notice

then `loop: fixture · notice confirmed · pass none` and `loop: fixture · notice changed · pass none`,
the second post's id `cece2f8f0718` being the one the third was refused as, and
`loop: fixture · notices-repeat-key · not held · the posts' first lines read [...]`, the first two
`mail — posted` and the third `mail — duplicate cece2f8f0718` (DERIVED, that run, scratch ids).

## Criteria

**Evidences:** KICK-dKeptSession-52
- AC1 — `notices-repeat-key` held, exit 0: B4, B5, B21, B5, B21 and B5 each printed `loop: fixture · record · exit 0`; three posts each printed `mail — posted`, and no `notice — not posted` line printed; the plant printed `loop: fixture · notice confirmed · pass 1 · key 1476fbb0a4a0`, `notice changed · pass 2 · key 96b7d551ba47` and `notice changed · pass 3 · key 96b7d551ba47`, then `loop: fixture · notices-repeat-key · held` (DERIVED, the plant; scratch keys).
- AC2 — over the staged copy the plant printed the `notice — not posted changed to build:dA · rc 1 · mail — duplicate` line S2 records and `notices-repeat-key · not held` (DERIVED, that run). `grep -c "mail — duplicate"` over this ledger and `git diff --name-only 08c5e6725 HEAD --` over unit 35's spec and acceptance ledger are read at the commit, the main loop's to confirm.
- AC3 — the probe printed `32` and the grep `plants=32`, and `notices-repeat-key` is a key of `PLANTS` (DERIVED, those commands at observation time).
- AC4 — `grep -l notices-repeat-key tools/loop/README.md help/loop.md` printed both paths; the anchor grep printed `930359dc`, and `docs_leg.py --fingerprints` printed `930359dc` on the `script:tools/loop/loop_transition.py` row with no verb (DERIVED, those commands at observation time), so the anchor did not move.

The plant read 30.6 s alone (PINNED 2026-11-23, `time`, node d), so the `loop transition record`
row's proxy `r` is 216.6 s, over unit 11's 186.0 s (DERIVED, their sum), and its value 325 (DERIVED,
x1.5 rounded up, over the row's 279), 205 s past the leg's 120 s ceiling (PINNED 2026-11-23,
`tools/gate-legs.json`): the raise is the owner's and is not made here. `gen_map.py --check` exited 0
after the edits, so `memory/map/generated/symbols.json` does not move; the plant adds no function.
`python tools/lexicon/lexicon.py` exited 1 on its verb-offender pin, 1432 over 1421 (DERIVED, that
run), the count unit 35's ledger records at its base, and no offender it lists is in this unit's files. The
`notices-repeat-key` case of `check --selftest`, §7's legs and the new arm's RED-first observation are
the close's.
