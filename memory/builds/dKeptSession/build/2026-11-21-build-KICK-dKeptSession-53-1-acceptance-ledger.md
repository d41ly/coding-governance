# KICK-dKeptSession-53 — acceptance ledger

**Serves:** journal KICK-dKeptSession-53

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32,
node d, at the pass's base `8b8f792b2` over the working tree before the commit: by the unit's two new
plants, each run alone by direct CLI (`python tools/loop/loop_transition.py --fixture --plant <case>`);
by `acks-superseded` and `acks-confirmed` run the same way, since S3 changes the writer they hold; by a
`python -I -c` probe of `derive_mail_chain` over hand-built rows; and by the greps and the Python
one-liner AC4, AC5 and AC6 state.

Before the first edit the spec's cited code was probed at the base, units 24, 10, 7, 35, 42, 11 and 52
read as landed (unit 42 merged at `76d236067`, unit 52 at `2df978aa8`, both ancestors of the base).
`tools/unattended/unattended.sh#read_mailbox` prints sixteen TAB columns, 12 `seq`, 13 `after` and 14
`content-key`, then 15 `deadline` and 16 `default`, read from the message's keys, and walks each mail
ref by `--first-parent`, so a second commit on a ref is a second row; `tools/unattended/unattended.sh#write_mail_post`
writes `after` on `seq` 1 alone. `tools/loop/loop_transition.py#read_mail_rows` zipped each row with
`MAIL_COLUMNS` alone, its floor `len(MAIL_COLUMNS) - 1` TABs, and the comment above `MAIL_COLUMNS` named
the later columns 12 to 14 alone. `tools/loop/loop_transition.py#write_consumed_acks` consumed the
current row and every held row whose `first-seen` sorted strictly before it, a `-` stamp read as `~`.
`tools/loop/loop_transition.py#render_fixture_mail` took `content_key`, `deadline` and `default`.
`tools/loop/placement.py#write_fixture_gov_ref` pushed one parentless commit and returned nothing. The
guard in `tools/loop/loop_transition.py#write_transition` raises `MailHeld` over the open rows less the
ids `write_consumed_acks` returns, so a stood-in ack answering 0 clears its row for that move.
`PLANTS` held 32 and the `loop transition record` row read `plants=32` at value 325 (DERIVED,
`len(PLANTS)` and the grep at `8b8f792b2`).

How the build reconciled the spec's text with what landed: unit 55's two plants had not landed at the
base, so the token moves in place from 32 to 34 (DERIVED, `len(PLANTS)` before and after), §4's first
case. The plants reuse the acks branch's `write_notice`, whose ref is `refs/gov/mail/fy/z/s-<n>`, so
§4's `s1` and `s2` are spelled `s-1` and `s-2`; `write_notice` gains the `seq` and `after` keys and a
`tip` passed to `write_fixture_gov_ref` as `parent`, and returns the sha that helper returns.
`acks-takeover` shares `acks-confirmed`'s lease, listing and key steps in one branch.
S3's key test compares the `content-key` columns as read, so two rows that both read `-` count as
equal. The landed `acks-superseded` plant writes its `confirmed` and `changed` with no key and no
`seq`, so it still holds: the `changed` the stand-in check names current supersedes the `confirmed` by
that equal `-` and not by the chain. A real `confirmed` or `changed` always carries a key, because
`write_mail_post` refuses one with no interface, and `check_interface_notice` names a row current only
when its key equals the derived twelve-hex key, so a real current row never reads `-`. The close's
review can rule on it. The spec's rule that the unit stops where its reading takes `r` past the leg's
ceiling is superseded for this run by the main loop, which parked the ceiling for the owner. The row
is re-priced here, and the raise is not made.

## S5 — unit 42's superseded wording

`KICK-dKeptSession-42` S2 acknowledges the current row and every `open` `confirmed` or `changed` from
the same parent with that subject "whose `first-seen`, as `read_mailbox` orders it, is strictly
earlier", and its §4 table "Who acknowledges what" gives the row "`confirmed`, `changed`, strictly
earlier than the current one | the same | with the current one". This unit's S1 and S3 supersede both
passages. A row is superseded when its `content-key` equals the current row's, or when
`derive_mail_chain` places it before the current row: an earlier `seq` on its ref, or a row of the
session the current row's session took over through the `after` of its `seq` 1 row, applied
transitively. `first-seen` and arrival are never read. Unit 42 is CLOSED, so neither its spec nor its
ledger is written (F1, (b)).

## Criteria

**Evidences:** KICK-dKeptSession-53
- AC1 — `acks-takeover` held, exit 0: it printed `loop: fixture · key 254cd6c106e2`, `loop: fixture · record · exit 0` with no manual ack, `loop: fixture · state aa11aa11aa11 · acked` for `a` and `loop: fixture · state bb22bb22bb22 · acked` for `b`, `loop: fixture · acks bb22bb22bb22 rc 0 · aa11aa11aa11 rc 0` and `loop: fixture · acks-takeover · held` (DERIVED, that run; a scratch key).
- AC2 — the same run printed `loop: fixture · chain · a precedes b · yes · first-seen swapped · yes` (DERIVED, that run). The `python -I -c` probe of `derive_mail_chain` gave `('a', 'b'), ('a', 'c'), ('a', 'e'), ('b', 'c')` over `a` and `e` on one ref, `b` and `c` on another with `b` naming `a` in `after`, `d` with `seq` `-` and `f` with no order columns, so neither `d` nor `f` is in any pair; two seq 1 rows that each name the other gave both pairs and no reflexive one (DERIVED, that probe).
- AC3 — `acks-later-key` held, exit 0: B4 printed the refusal naming `mail open cc33cc33cc33` alone and `loop: fixture · record · exit 1`, and then `loop: fixture · acks bb22bb22bb22 rc 0 · aa11aa11aa11 rc 0`, which does not name `c` (DERIVED, that run). `c` was pushed onto `b`'s ref with `parent` set to the sha returned for `b`, and the driver's read gave it as a row of its own.
- AC4 — `grep -n "content key or by the session chain" help/loop.md` printed the guard table's superseded row, and `grep -c "acks-takeover"` printed 1, 1 and 8 for `help/loop.md`, `tools/loop/README.md` and `tools/loop/loop_transition.py` (DERIVED, those commands at observation time). `docs_leg.py --fingerprints` printed `930359dc` on the `script:tools/loop/loop_transition.py` row with no verb (DERIVED, that command), so the anchor did not move.
- AC5 — this ledger quotes both of unit 42's passages in S5. The `tr` and `grep -c` pair and the `git diff --name-only 8b8f792b2 HEAD` over unit 42's spec and build records are read at the commit, and the main loop confirms them.
- AC6 — the probe printed `34` and the grep `plants=34`, and `acks-takeover` and `acks-later-key` are keys of `PLANTS` (DERIVED, those commands at observation time).

`acks-takeover` read 17.2 s alone and `acks-later-key` 2.5 s (PINNED 2026-11-23, `time`, node d). So
the `loop transition record` row's proxy `r` is 236.3 s, over unit 52's 216.6 s (DERIVED, their sum),
and its value is 355 (DERIVED, x1.5 rounded up, over the row's 325). That is 235 s past the leg's 120 s
ceiling (PINNED 2026-11-23, `tools/gate-legs.json`), and the raise is the owner's, not made here.
`acks-superseded` and `acks-confirmed` still held, run alone after the edit (DERIVED, those runs).
`gen_map.py --write` moved `memory/map/generated/symbols.json` by the one `derive_mail_chain` entry
and rewrote no other map file (DERIVED, `git status` after it). `lexicon.py --suggest derive_mail_chain
--as py.function` answered OK. `python tools/lexicon/lexicon.py` exited 1 on its verb-offender pin,
1432 over 1421, the count unit 52's ledger records at its base, and no offender it lists is in this
unit's files (DERIVED, that run). The close owes these: the two plants' and the other acks cases of
`check --selftest`, §7's legs, and the new arm's RED-first observation on scratch copies of
`write_consumed_acks` selecting by `first-seen`, of `derive_mail_chain` ordering by `first-seen`, of
one acking every row the chain relates, and of `write_fixture_gov_ref` with no `parent`.
- seen-red — `loop transition record` — red `45016a2c4` — green `45016a2c4` — `acks-takeover`: the session chain places no row
- seen-red — `loop transition record` — red `45016a2c4` — green `45016a2c4` — `acks-later-key`: every row the parent wrote is acked, placed or not
