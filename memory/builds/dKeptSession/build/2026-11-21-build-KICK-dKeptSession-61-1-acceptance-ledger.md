# KICK-dKeptSession-61 — acceptance ledger

**Serves:** journal KICK-dKeptSession-61

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32,
node d, at the pass's base `2e35be083` over the working tree before the commit: by the unit's new
plant run alone by direct CLI (`python tools/loop/loop_transition.py --fixture --plant
chain-two-dependents`); by the four landed plants whose move reaches a current interface row, run the
same way, since S2 gives their writer a chain read; by a scratch probe running the suite block's own
helpers and eight driver calls over a bare origin and one clone, never the suite; and by the greps and
the Python one-liner AC4 to AC6 state.

Before the first edit the spec's cited code was probed at the base, units 6, 7, 35, 42, 8, 11, 43, 52,
53, 55 and 17 read as landed. `tools/unattended/unattended.sh#read_mailbox` took `<who>
soft|strict|local`, ran one `git log --first-parent --source` and one `awk`, and kept a row in its last
loop where `check_mail_addressed` passed its `to`, its sixteen columns `ref` 9 and `after` 13 (DERIVED,
its last `printf` at the base). `tools/unattended/unattended.sh#print_mailbox` took `who · open · ids ·
[soft|local]`; the `--mail` arm's unknown-flag refusal named thirteen flags and its `read` form refusal
and the usage-header row read `[--local]` last (DERIVED, the refusal's list and the row at the base).
`tools/loop/loop_transition.py#read_mail_rows` took `local=False`; `derive_mail_chain(rows)` was pure
over one parent's rows; `write_consumed_acks` placed held rows over `derive_mail_chain` of that parent's
rows of the read. `tools/loop/placement.py#write_fixture_gov_ref` takes `parent=None` and returns the
commit's sha, as unit 53 S7 landed it. The driver's refusal sites read `347/347` (DERIVED,
`check-arms.py --report`'s ceiling row at the base), and `--sent` was on no line of the driver or the suite.

How the build reconciled the spec's text with what landed. The spec's floors, 4156 and 1373, were read at
`c18b223b`; at this base they are 4176 and 1393 (DERIVED, the suite's last assignments), so the block's
four `same` raise them to 4180 and 1397 (DERIVED, plus four each). The spec's `r` before this unit,
209.1 s, predates units 53 and 55's re-reads; the row's note reads 245.2 s at this base (PINNED
2026-11-23, unit 55's re-read), and this unit's reading is added to that. The spec's rule that the unit
stops where its reading takes `r` past the leg's ceiling is superseded for this run by the main loop,
which parked the ceiling for the owner; the row is re-priced here and the raise is not made. The arm
carries `MV_SENT` as the selection word itself, empty or `sent`, so it passes on to `print_mailbox` and
`read_mailbox` unchanged and the form tests of `post` and `notice` read it beside the flags they refuse.
The loop README's sentence that the chain "is read off the parent's rows of the one read" is false under
S2, so it now reads that the chain is placed over every message the parent wrote, beside S5's sentence.

## S3 — the sibling texts superseded

`KICK-dKeptSession-53` S1 reads: "`derive_mail_chain(rows)` in `tools/loop/loop_transition.py`, over one
parent's rows of `read_mail_rows`' one read (`KICK-dKeptSession-5` S9 and F9), the rows whose
`from-build`, column 6, is that parent, returns the set of `(earlier id, later id)` pairs".
`KICK-dKeptSession-55` S1 reads: "It makes no read of its own."
This unit's S2 supersedes both passages. The order is read over every row the parent wrote, `--mail read
<parent> --local --sent` over the cache the guard's read has just fetched, and the ack set over the rows
addressed to the dependent; the one read of the dependent's mailbox is kept, and S2 adds one cache read
per parent judged. Units 53 and 55 are CLOSED, so neither spec nor ledger of theirs is written (F2, (b)).

## Criteria

**Evidences:** KICK-dKeptSession-61
- AC1 — `chain-two-dependents` held, exit 0: it printed `loop: fixture · record · exit 0` for tFix's B4 and again for tTwo's, `loop: fixture · state <id> · acked` for each of the sent read's four rows, `a1a1a1a1a1a1`, `b1b1b1b1b1b1`, `a2a2a2a2a2a2` and `b2b2b2b2b2b2`, four `mail — acked` lines on stderr and `loop: fixture · chain-two-dependents · held` (DERIVED, that run; scratch ids).
- AC2 — the same run printed `loop: fixture · chain tFix · a1a1a1a1a1a1 precedes a2a2a2a2a2a2 · sent yes · filtered no` (DERIVED, that run): the chain line's `<a1> precedes <a2> · sent yes · filtered no`, not the copy's `sent no`.
- AC3 — the same run printed `loop: fixture · sent fy · 4 row(s) · seq and after on 4` and `loop: fixture · sent build:fy · refused · mail unknown: --mail read build:fy exited 2: mail — not read · --sent reads one build's own mail refs, and 'build:fy' is no build's slug` (DERIVED, that run).
- AC4 — this ledger quotes unit 53's and unit 55's passages in S3. The `tr` and `grep -c` pair and the `git diff --name-only 2e35be083 HEAD` over units 53 and 55's specs and ledgers are read at the commit, and the main loop confirms them.
- AC5 — the probe printed `37` and the grep `plants=37`, and `chain-two-dependents` is a key of `PLANTS` (DERIVED, those commands at observation time).
- AC6 — `docs_leg.py --fingerprints` printed `4c1a862e` for `verb:unattended.sh:--mail`, the fingerprint `help/loop.md`'s anchor now carries, re-stamped from `e05e3012` (DERIVED, that command and the grep); `script:tools/loop/loop_transition.py` stayed `930359dc` (DERIVED, that command). `grep -c -- '--sent'` printed at least 1 for `help/loop.md`, `tools/unattended/VERBS.template.md` and `tools/loop/README.md`, `chain-two-dependents` is in `help/loop.md`, and `cmp` of the template and `memory/guides/UNATTENDED-VERBS.md` printed nothing (DERIVED, those commands at observation time).
- AC7 — the scratch probe ran the block's helpers and its lines verbatim, outside the suite: sessions `s1` and `s2` of build `fx` post to `build:fy` and `build:fz`, and its `same` lines on `--mail read fy` and on the `--sent` read of `fx` held (DERIVED, that probe). The suite's own run is the close's.
- AC8 — the same probe ran the block's `--mail read build:fx --sent` and `--sent` ack lines, and its four `same` held, `assertions 4 status 0` (DERIVED, that probe). The suite's own run is the close's.

## What the close owes

The four landed plants still held, each run alone after the edit: `acks-confirmed` 10.5 s,
`acks-superseded` 17.3 s, `acks-takeover` 15.2 s with its chain line `yes` and `yes`, and `acks-later-key`
3.2 s, refused naming all three rows with no ack posted (PINNED 2026-11-23, `date` around each run, node
d). Against units 42 and 53's 45.9 s for the same four (PINNED 2026-11-23, the row's note) they read 46.2 s
(DERIVED, their sum), so the chain read adds 0.3 s (DERIVED, the difference). `chain-two-dependents` read
29.5 s alone (PINNED 2026-11-23, node d). So the `loop transition record` row's proxy `r` is 275.0 s
(DERIVED, 245.2 plus 29.5 plus 0.3), its value 413 (DERIVED, x1.5 rounded up, over the row's 368) and its
token `plants=37`; that is 293 s past the leg's 120 s ceiling (PINNED 2026-11-23, `tools/gate-legs.json`),
the owner's to raise, not made here. The suite block's probe read 13.7 s (PINNED 2026-11-23, node d), so
the `unattended driver selftest shard 8/8` row rises by 21 to 6690 (DERIVED, x1.5 rounded up, over 6669).
The plant adds no module-level name, so `memory/map/generated/symbols.json` does not move. The close
owes: the nine `chain-two-dependents` cases (DERIVED, the case table) and the re-armed `acks-takeover` call of `check --selftest`;
the suite's four new `same` and the KDS25 read-form arm re-armed for `[--sent]`; §7's legs; and the two
new arms' RED-first observations, on a copy of `derive_mail_chain` reading `rows` in place of `chain`
(AC1, AC2) and a scratch `unattended.sh` whose `read_mailbox` keeps the address filter under `sent`
(AC3, AC7).

The spec's status flip to CLOSED was not made in this pass: scratch-guard refused the builder's
status-only Edit of the spec in this pass's own worktree, its card route not read as naming that spec
there, and the refusal was not routed around. The flip is the main loop's, which the guard admits.
