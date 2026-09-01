# TOOL-dBriefedPass-2 — the brief verb, and the staleness reader that building it corrected

**Serves:** journal TOOL-dBriefedPass-2

*Node `d`, 2026-09-01, unattended prompt-mode run under a standing mandate. Every token below names
the command that produced the observation. The verb was exercised against THIS build's own run-state
file, which is why the observations are live rather than fixture-only.*

## The divergence this pass found, and the M2 route it took

S3 at rev-4 said `--status` prints `STALE` for **any row** whose file no longer hashes to what was
recorded. The parked region is append-only, so re-briefing an edited file writes a second row and
the first keeps describing bytes that legitimately moved on. Observed live, in this order:

```
--brief                        -> brief recorded — TOOL-dBriefedPass-2 · 27a8086b8ae6
edit the file                  -> --status: parked 1 · noted 6 · STALE briefs 1
--brief again (re-record)      -> brief recorded — TOOL-dBriefedPass-2 · b5ea709eb4a5
--status                       -> parked 1 · noted 7 · STALE briefs 1     <-- never clears
```

A count that can only rise is indistinguishable from one that is stuck, so it tells a reader
nothing. **Spec first, then code**, which is M2's rule for a divergence: spec 2 went to rev-5 with
the §9 line, S3 now grades the LATEST row per unit, AC6 gained the clearing arm, and only then did
the reader change.

## The defect the bug-class checklist caught in that fix

The first cut of the per-unit reader used `sed` with a `\1` capture group, written through a shell
heredoc. **The back-reference did not survive the write**: the landed bytes read `/ /p`, so the unit
id was dropped and every row collapsed onto one key. It passed every check I had at that moment,
because this build had briefed exactly one unit — with two it would have kept one row in total and
reported a stale brief as clean.

That is `memory/gotchas/heredoc-escape-reaches-the-regex` in the write path rather than the read
path, and it was caught by running the checklist over the pass and then reading the landed bytes
instead of trusting the command that wrote them. The reader is now one `awk` pass splitting on the
literal separators it can see, with no escape to lose, and there is an arm for the two-unit case.

## Evidence

**Evidences:** TOOL-dBriefedPass-2
- AC1 — `unattended.sh --brief dBriefedPass --unit TOOL-dBriefedPass-2 --path <the brief>` — wrote
  one row and printed `brief recorded — TOOL-dBriefedPass-2 · 27a8086b8ae6`; an identical second call
  printed `brief already recorded, unchanged` and wrote nothing.
- AC2 — same verb with `--unit TOOL-dBriefedPass-99` — `UNATTENDED check 49 FAILED — --brief names a
  unit the build README's generated units region does not carry`. The roster is `unit_ids_of`, the
  same region `--plan` and `--status` take their set from, so the three cannot disagree.
- AC3 — same verb with `--path /tmp/untracked-brief.md` — `UNATTENDED check 49 FAILED — --brief names
  an UNTRACKED path`.
- AC4 — `bash tools/unattended/unattended.sh --status dBriefedPass` — `parked 1` before and after ten
  recorded briefs. The surfaced count did not move, which is what the `history` classification buys
  and what keeps a truthful `parked-decisions-surfaced` attestation from being refused.
- AC5 — same command — `· noted` moved on every recorded brief, reaching `noted 10`, while `parked`
  stayed at 1.
- AC6 — same command, both directions — an edited brief reported `STALE briefs 1`, and re-briefing
  the edited file cleared it to no `STALE` clause at all. The clearing half is the one that proves
  the reader grades the latest row; it is the arm rev-5 added and the reason rev-5 exists.
- AC7 — `bash tools/unattended/check-unattended.sh` exits 0 with `--brief` declared, which is check
  26 over the verb's three carriers and check 27 over the new park kind. And
  `bash tools/unattended/adopt-unattended.sh --check` — `unattended: in sync (skill rendered from
  template + .unattended.conf)`, which is the `unattended skill wiring` leg by its declared argv.
- AC8 — `bash tools/unattended/unattended.sh --status dBriefedPass` — the pair, asserted together:
  `noted` moved by one per brief and `parked` did not move at all.

## What this pass did NOT verify

The arms added to `tools/unattended/unattended.test.sh` were WRITTEN and the suite was **not run** —
standing owner instruction on this node, and the 2026-08-23 ruling took those suites off the merge
bar. Every criterion above was instead observed by running the verb against this build's own live
run-state file, which is a stronger observation than a fixture would have been but is not the same
thing as a green suite, and this line is here so nobody reads it as one.

A two-unit staleness case WAS exercised live: briefs for `TOOL-dBriefedPass-2` and
`TOOL-dBriefedPass-3`, editing only the second, reported exactly `STALE briefs 1`.
