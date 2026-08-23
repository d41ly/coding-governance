**Serves:** journal TOOL-dScriptedRepeat-13 TOOL-dScriptedRepeat-14 TOOL-dScriptedRepeat-15

# The round-9 fold — the last one, and the guard became structural

Node `d`, 2026-08-24. Round 9 read the fold of round 8 and nothing else: one commit, `4db111fa`.
**BLOCKED** — raw 27, confirmed 19, refuted 8, precision 0.70, collapsing to eleven defects: one
blocker, two highs, two mediums, six lows. Two were landing-blocking. Both are folded, and the owner
authorised the landing after this fold with no round 10.

## The blocker: the conf could no longer END the leg and could still HIJACK it

Round 8 stopped `.unattended.conf` from terminating `check-unattended.sh` with a sentinel probe. The
probe was right about the shape it was written for and wrong about the file's actual reach, because
the real `. "$CONF"` still ran in the **main shell**, below `status=0` and below `fail()`.

- **`trap 'exit 0' EXIT` appended to the conf** satisfies the probe — the trap fires only when the
  probe subshell exits, which is *after* its sentinel is written — and then fires again on the
  script's own `exit "$status"`. Observed: **rc 0 with the FAILED line still printed.**
- **`fail() { :; }` appended to the conf** replaces the verdict recorder itself. Observed: **rc 0 with
  zero bytes of output** — byte-indistinguishable from a clean tree, and stealthier than the `exit 0`
  shape the previous fold had just graded a blocker.

`run-gates` classifies on the exit code alone, so both read `GATE ok`.

**The repair is structural rather than another probe.** Nothing from that file executes in this shell
any more. It is sourced inside a subshell and the declared keys come back as a NUL-delimited
name/value stream terminated by a sentinel; the names are read from the file as TEXT and validated
against `[A-Z][A-Z0-9_]*`, so the stream cannot introduce a name the leg does not expect. A trap, a
redefined function, an `exit`, a `set -x` — none of it crosses the boundary. The worst a hostile conf
can do now is fail to deliver the sentinel, which is a refusal.

That one change also closed **HIGH 2** by construction: the probe had omitted its sibling's
`|| exit 9`, so a bash parse error passed it, the real source loaded only the lines above the break,
and `LANDED_ANCHOR_CUTOFF` came back empty — which the leg reads as "grandfather every anchor". The
import carries the guard.

Six shapes measured against both versions:

| appended to the conf | pre-fold | post-fold |
|---|---|---|
| nothing | rc 1 | rc 1 |
| `trap 'exit 0' EXIT` | **rc 0**, FAILED line printed | rc 1 |
| `fail() { :; }` | **rc 0, zero output** | rc 1 |
| `exit 0` | rc 1 | rc 1 |
| a parse error | rc 1, wrong cause | rc 1 |
| `return 0` | rc 1 | rc 1 |

## The half nobody was testing: over-refusal

The other three findings share one root, and it is the more useful lesson. **Every arm in that suite
staged a break, so no arm could see a guard that refuses too much.**

- **HIGH 3.** The round-8 cross-check read "the file spells the key and the sourced view is empty" as
  "the source never got there" — false for a key deliberately declared empty, which is this kit's own
  documented idiom in **eleven** keys of its shipped example, with comments reading *"BLANK turns that
  check off"*. The sentinel carries `${VAR+SET}` now: the shell already knows the difference, and
  reading the file's text to guess at it was the mistake.
- **MEDIUM 4.** `|| exit 9` read the source's exit STATUS as a liveness verdict, so a conf whose last
  line is a false `[ ... ]` was refused having assigned everything correctly. The status is no longer
  a verdict; the sentinel and the set-marker are.
- **MEDIUM 5.** The per-root zero-records refusal fired on every freshly authored playbook — a
  declared records root holds nothing until a run writes into it, and the leg carries no guard. It
  reds only where a grain enumerates PIECES and the root holds no readable record: work exists and
  evidence does not.

Both over-refusals were verified gone (an empty `PLAYBOOK_GLOB` and a false-conditional tail both
leave the leg at rc 0) **and all four abort shapes were re-confirmed still redding**, which is the
pair that matters — a fix for an over-refusal that disarms the guard is not a fix.

Three arms were added for the legal shapes. They are the half that was missing.

## The lows

`CONF_SOURCE_OK` derived from one of two reads. The bypass note's two numbers counting different
populations and inviting a ratio. `_seen_here` counting READABLE records while the message said
ENUMERATED. **An arm whose assertion could not fail** — the root name it grepped for also appears in
the note the same run prints, so it now binds to the FAILED line. The help budget summing every
`BUDGET_`-prefixed variable in the ENVIRONMENT and evaluating its contents; it reads the names from
this file's own text now and skips a non-integer. And three spec headers left at the previous day
while their rev-5 entries said otherwise.

## Counts and what stays open

`check-playbook.test.sh` is at **123 assertions**, from 90 when this session started. Five of the new
arms were observed RED against the pre-fold leg in one control run; the hijack arms were verified with
a hermetic probe, because their suite is the one the owner stopped.

Unchanged from round 8 and still true: the newline-in-a-filename arm cannot exist on this node, round
7's blind-blame liveness arm is owed, and the gate selftest suite has not been run end to end.

**There is no round 10.** Nine rounds, every one BLOCKED, and rounds 7 through 9 each found defects the
previous fold introduced. The severity fell each time — round 9's blocker needs two hostile lines in a
tracked conf — and the owner's call is that the fold lands here.
