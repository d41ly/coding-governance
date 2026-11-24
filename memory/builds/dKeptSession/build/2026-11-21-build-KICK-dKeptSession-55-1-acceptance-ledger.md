# KICK-dKeptSession-55 — acceptance ledger

**Serves:** journal KICK-dKeptSession-55

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32,
node d, at the pass's base `e23cd7f50` over the working tree before the commit: by the unit's two new
plants, each run alone by direct CLI (`python tools/loop/loop_transition.py --fixture --plant <case>`);
by the six landed `acks-*` plants and `mail-open` run the same way, since S2 changes the writer they
hold; and by the greps and the Python one-liner AC3, AC5 and AC6 state.

Before the first edit the spec's cited code was probed at the base, units 42, 11, 52 and 53 read as
landed (unit 42 merged at `76d236067`, units 11, 52 and 53 by `252fc06a9`, all ancestors of the base).
`tools/loop/loop_transition.py#write_transition` binds `mail, unarmed = read_mail_rows(root, build)`,
appends the unarmed line to `said`, calls `write_consumed_acks(root, build, mail)` and raises `MailHeld`
over the `open` rows less the returned ids, before `derive_move`. `tools/loop/loop_transition.py#write_consumed_acks`
returned the ids acked with exit 0, never raised, consumed every `open` `landed`, `superseded` or
`withdrawn` and per parent the current interface row and each held row of equal `content-key` or placed
before it by `derive_mail_chain`, and posted every consumed id whatever else was open, writing only a
failed ack's line on stderr. `tools/loop/loop_transition.py#main` prints `said` only after
`write_transition` returns, and its `TransitionRefused` handler prints the refusal alone. `MAIL_COLUMNS`
holds eleven names and `MAIL_ORDER_COLUMNS` follows it (DERIVED, the tuples at `e23cd7f50`). `PLANTS`
held 34 and the `loop transition record` row read `plants=34` at value 355 (DERIVED, `len(PLANTS)` and the
grep at `e23cd7f50`), as §4's budget row expects after units 7, 35, 42, 11, 52 and 53.

How the build reconciled the spec's text with what landed. Unit 42's table "Who acknowledges what" in
`help/loop.md` spells its `When` cells "at its next move", not "at its next transition" as S6 quotes
them, so both cells that name the move's timing now read "at its next move with no other message
open", the cell under a current interface keeping its "once the parent's interfaces check names it
current" after that. Unit 53's `acks-later-key` plant owed acks of `a` and `b` and a refusal naming
`c` alone; under S2 its move posts no ack, so the plant now owes no ack and a refusal naming `a`, `b`
and `c`, its `PLANTS` text says so, its `run_selftest` refusal case reads the refusal's opening with
`c`'s id as the needle, and a new case owes its `loop: fixture · acks none` line. Unit 53 left one
sentence of `tools/loop/README.md`'s mail-guard paragraph false, that a `changed` the check does not
name is never acknowledged, while unit 53 acknowledges a superseded one; S7's rewrite of that
paragraph now reads "nor a `confirmed` or `changed` the check neither names nor finds superseded",
true for both units. The plants table asks `acks-withdrawn-question` to print each row's state after
the refusal, so it prints both the `withdrawn` and the `question` from one read. The spec's rule that
the unit stops where its reading takes `r` past the leg's ceiling is superseded for this run by the
main loop, which parked the ceiling for the owner; the row is re-priced here and the raise is not made.

## S4 — unit 42's superseded wording

`KICK-dKeptSession-42` S1 reads: "It acknowledges every row whose `state` is `open` and whose `kind` is `landed`, `superseded` or `withdrawn`: the transition has read it, and nothing else consumes it."
Its S3 reads: "It runs once per id and only while the row reads `open`, so a retried transition posts nothing twice."
This unit's S1 to S3 supersede both passages. The writer first computes, posting nothing, the ids it
would consume, unit 42's kinds and the interface rows unit 53 S3 consumes; it posts them only when
every `open` row of the guard's one read is among them, else it posts none and returns the empty set,
so the refusal names every open row; and each ack that posts with exit 0 writes `mail — acked <kind>
<id> from build:<parent>` to stderr as it happens. Unit 42's per-id posts run only under that
condition. Unit 42 is CLOSED, so neither its spec nor its ledger is written (F1, (b)).

## Criteria

**Evidences:** KICK-dKeptSession-55
- AC1 — `acks-withdrawn` held, exit 0: it printed `loop: fixture · record · exit 0`, `loop: fixture · stderr · mail — acked withdrawn 9a9b9c9d9e9f from build:fy`, `loop: fixture · acks 9a9b9c9d9e9f rc 0` and `loop: fixture · acks-withdrawn · held` (DERIVED, that run; a scratch id).
- AC2 — `acks-withdrawn-question` held, exit 0: B4 printed `refused — tFix · mail open 9a9b9c9d9e9f 8a8b8c8d8e8f · …` and `loop: fixture · record · exit 1`, no `mail — acked` line, then `loop: fixture · state 9a9b9c9d9e9f · open` and `loop: fixture · state 8a8b8c8d8e8f · open`, `loop: fixture · acks none` and `loop: fixture · acks-withdrawn-question · held` (DERIVED, that run).
- AC3 — `grep -n "mail — acked\|with no other message open\|acks-withdrawn" help/loop.md` printed the guard paragraph's new sentence, both table rows whose `When` cell it rewrites, the fixture-cases sentence naming both plants, and the sentence in `## Coordinating with a parent build` (DERIVED, that command at observation time). `docs_leg.py --fingerprints` printed `930359dc`, `53beaa6b`, `b7ddefe3`, `0eca9616` and `51794820` for the five `loop_transition.py` anchors, each equal to the one `help/loop.md` carries (DERIVED, that command), so no anchor moved.
- AC4 — this ledger quotes both of unit 42's passages in S4. The `tr` and `grep -c` pair and the `git diff --name-only e23cd7f50 HEAD` over unit 42's spec and build records are read at the commit, and the main loop confirms them.
- AC5 — the probe printed `36` and the grep `plants=36`, and `acks-withdrawn` and `acks-withdrawn-question` are keys of `PLANTS` (DERIVED, those commands at observation time).
- AC6 — `grep -n "all or nothing\|acks-withdrawn" tools/loop/README.md tools/loop/loop_transition.py` printed the README's mail-guard paragraph and fixture sentence, the module docstring's mail-guard paragraph and plant sentence, `write_consumed_acks`' docstring, `write_transition`'s docstring, the comment above its guard and the two `PLANTS` keys (DERIVED, that command at observation time).

The six landed `acks-*` plants still held, each run alone after the edit: `acks-landed`,
`acks-confirmed`, `acks-superseded`, `acks-failed` and `acks-takeover` posted as before, each posted ack
now beside its `mail — acked` line, and `acks-later-key` posted none, refused naming all three rows
(DERIVED, those runs). `mail-open` still refused on its lone question, writing nothing (DERIVED, that run).

`acks-withdrawn` read 5.8 s alone and `acks-withdrawn-question` 3.1 s (PINNED 2026-11-23, `time`,
node d). So the `loop transition record` row's proxy `r` is 245.2 s, over unit 53's 236.3 s (DERIVED,
their sum), and its value is 368 (DERIVED, x1.5 rounded up, over the row's 355). That is 248 s past the
leg's 120 s ceiling (PINNED 2026-11-23, `tools/gate-legs.json`), and the raise is the owner's, not made
here. The plants add no module-level symbol, so `memory/map/generated/symbols.json` does not move and
`gen_map.py --write` was not run. This unit adds no function. `python tools/lexicon/lexicon.py` exited
1 on its verb-offender pin, 1432 over 1421, the count unit 53's ledger records, and no offender it
lists is in this unit's files (DERIVED, that run). The close owes these: the eight `acks-*` plants' cases of `check
--selftest`, §7's legs, and the new arm's RED-first observation on scratch copies of
`write_consumed_acks` that write no `mail — acked` line (AC1) and that ack whatever the guard then
reads (AC2).
- seen-red — `loop transition record` — red `45016a2c4` — green `45016a2c4` — `acks-withdrawn`: a `withdrawn` row is never consumed
- seen-red — `loop transition record` — red `45016a2c4` — green `45016a2c4` — `acks-withdrawn-question`: acks posted although another row stays open
