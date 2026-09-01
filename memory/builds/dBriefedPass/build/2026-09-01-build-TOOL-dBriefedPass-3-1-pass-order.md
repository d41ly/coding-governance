# TOOL-dBriefedPass-3 — the refusal that makes the order real

**Serves:** journal TOOL-dBriefedPass-3

*Node `d`, 2026-09-01, unattended prompt-mode run under a standing mandate. Every token below names
the command that produced the observation.*

## Two mechanisms, because one of them is bypassable

`--dispatch` refuses a build pass whose unit is MISSING, THIN, or out of the build's own declared
`order`. That catches it at the moment of the act, and it is bypassed by simply not calling the verb.
`check-pass-order.sh` reads the COMMIT GRAPH instead: for every unit a build README carries as
CLOSED, the commit that built it must have had a conforming, non-THIN spec at its **first parent**.

The first parent and not the pinned BASE, which is the load-bearing choice. The build method
REQUIRES a run to author a missing spec, so a BASE-anchored test would refuse the shape the method
mandates. What the parent anchor refuses is authoring it AFTERWARDS.

## What the kit's own gates caught in this pass

**Check 28 named nine sites.** The first cut used bare `git` for every sha dereference. A
`git replace` ref rewrites what a sha MEANS for every read, and this leg's entire answer is "what did
the tree look like at that parent" — precisely the answer a substituted object flips. All nine now go
through the library's pinned `GIT` wrapper, and the header says why so the next reader does not
simplify it back.

**The order gate's own join was wrong and the passing case found it.** The guard skipped a sibling
that was already dispatched, matching `" dispatch · item $id "` — but a dispatch row's `item` field
is `<anchor-sha> <unit-id>`, so the match found nothing and every dispatched sibling read as still
blocking. Caught by arming the passing case rather than the refusal: unit 4 was refused with unit 3
named as a blocker while unit 3 was visibly dispatched. The join is now anchored on ` · reason ` at
the tail, which also makes the id a whole token — without that, `TOOL-x-1` matches `TOOL-x-11`'s row.

## Evidence

**Evidences:** TOOL-dBriefedPass-3
- AC1 — `unattended.sh --dispatch dBriefedPass --pass <a seq no spec defines>`, run with a `-77`
  suffix — refused with
  `which is M2's MISSING`. Observed against the live record, where the shipped driver accepted it.
- AC2 — `tools/unattended/unattended.test.sh` arm — a spec with an empty acceptance section is
  refused naming `grades THIN`, and the message names the id and the STATE, not the empty section.
- AC3 — `unattended.sh --dispatch dBriefedPass --pass TOOL-dBriefedPass-5` — refused naming
  `TOOL-dBriefedPass-3 (order 3, SPECCED)` and `TOOL-dBriefedPass-4 (order 4, SPECCED)` as blockers;
  the same call succeeded once those were dispatched. Both arms, live.
- AC4 — amended rev-5 — the criterion claimed `tools/unattended/unattended.test.sh` covered the
  order gate's equal-order and no-order branches, and it covers neither. No fixture spec in that
  suite carries an `order` verb, so the whole block is SKIPPED rather than passed in every arm
  including the one that reads as the passing case; the `tRun` units region emits one row, which
  makes the sibling population zero; and this build's own five units carry distinct orders 1-5, so
  live observation missed them too. The criterion now declares the gap and `TOOL-dBriefedPass-6`
  carries the fixture work. Section 9 logs it.
- AC5 — `bash tools/unattended/check-pass-order.test.sh` — the `build-first` fixture builds a real
  repository whose build commit precedes its spec commit; the leg exits 1 and names the unit and
  `BUILT before a conforming spec`. **The failing case, observed**, which is what makes this a gate
  rather than an assertion about nothing.
- AC6 — same suite — the `spec-first` fixture is byte-identical except for commit ORDER, and the leg
  exits 0 with `graded 1 closed unit`. The matched pair is what distinguishes a leg that reds
  correctly from one that reds on everything.
- AC7 — same suite, plus a live run — with `PASS_ORDER_CUTOFF` blank the leg prints
  `the ORDER term is OFF` and exits 0 over a tree that would otherwise red; with it set the live run
  prints `graded 2 closed unit(s) · 83 build(s) skipped by the 2026-09-01 cutoff · 0 with no pinned
  run BASE · 0 unit(s) unbuilt-in-range`. All three populations the leg walks are named.
- AC8 — `bash tools/unattended/check-unattended.sh` exits 0 with `PASS_ORDER_CUTOFF` declared, which
  is check 22 joining conf keys against the protocol's section-8 table in BOTH directions.
- AC9 — `tools/gate-legs.json` carries `pass-order history` with `chunk: declarations`,
  `subject: repo`, `guard: []` and `ceiling: 90`, measured at 6 s wall on this corpus of 85 builds.
- AC10 — `python tools/govkit/govkit.py selfcheck` and
  `python3 tools/codebase-map/test_codebase_map.py` both exit 0 with the leg declared. These are the
  two UNGUARDED enforcers, and they are what the five-declaration rule exists for: the manifest row,
  the `[[gate_leg]]` block in `tools/unattended/kit.toml`, the `tools/govkit/subject-pins.tsv` row,
  the `gate-legs` claim in `memory/map/features/unattended.md`, and the regenerated
  `memory/map/generated/`.

## What this pass did NOT verify, and one thing it dirtied

The arms added to `tools/unattended/unattended.test.sh` were WRITTEN and that suite was **not run** —
standing owner instruction, and the 2026-08-23 ruling took it off the bar. Its four dispatch arms are
therefore unexecuted; AC1 and AC3 were observed live against this build's own record instead, which
is where their evidence above comes from. **AC4's two branches were observed by nothing at all**, and
the arms that would cover them are not added here: the `tRun` fixture is shared by a four-thousand-
line suite this node may not run, so a second unit added to its roster could break arms I cannot
re-run to check. That is a deliberate refusal to write unverifiable test code, recorded rather than
taken quietly, and `TOOL-dBriefedPass-6` carries the work. `check-pass-order.test.sh` IS new and IS
run: 14 arms, exit 0.

**Two dispatch rows in this run's record are test residue and should be read as such.** Proving the
order gate's passing case required dispatching units 4 and 5, and one of those declared `tools/z.sh`,
a path that does not exist and that no commit will touch. The parked region is append-only so they
stand. They are `history`-kind rows and inflate no surfaced count, but a later reader comparing
declarations against commits will find them unmatched. Exercising a live record rather than a scratch
fixture was the wrong call and this is the record of it.
