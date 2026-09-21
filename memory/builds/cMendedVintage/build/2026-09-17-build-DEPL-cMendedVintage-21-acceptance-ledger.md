# cMendedVintage — the acceptance ledger for unit 21

**Serves:** journal DEPL-cMendedVintage-21 DEPL-cMendedVintage-13

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar, no self-test suite and
no `*.test.sh` ran in this pass. Every observation below was taken by running the shipped arms in a
standalone harness against scratch fixture targets, five times: once clean and once per staged break.*

## The one thing worth reading twice

**S1 was already written, so it was LIFTED rather than written a second time.**
`DEPL-cMendedVintage-13` S6 landed the temp-sibling write and the
`os.replace`
inline in the manifest write-back an hour before this pass. Minting a second atomicity beside it
would have been two answers to one question. What this unit does instead is extract that body into
`write_atomic`,
route the one call site through it, and — the actual deliverable — give it something that fails when
it is gone. rev-2 records the lift.

**The mitigation could have been deleted silently, and that is the whole unit.** `-13` AC6 compares
the runner two runs of
`apply`
produce. An ordinary in-place
`write_text`
produces those bytes identically, so the one mitigation that unit's Rollout elevates above every
other was gradeable by nothing. A helper that is present, correct and unobserved is exactly the shape
this build exists to close.

**Two observations, and the staged breaks prove they are two.** B1 and B2 below red DIFFERENT halves
of AC1. A single combined break would have shown the pair red together and said nothing about whether
either can fail alone.

**Evidences:** DEPL-cMendedVintage-21

- AC1 — OBSERVED — `apply --target <fixture>` — with a raise staged into a COPY of the engine at the
  one line between the temp write and the replace, the run dies where the break was staged, the
  fixture's previous runner file survives byte-identical, and the directory holds no temp sibling.
  The temp-sibling half is asserted separately from the survival half, because an arm grading only
  the surviving file passes for a helper that leaks
  `gate-legs.json.govkit-new`
  on every failure. A CONTROL run of the UNBROKEN engine against the same fixture is asserted to MOVE
  that runner, so the arm cannot pass for a run that refused before it ever reached the write — and a
  second liveness asserts the staged substitution MATCHED, so a renamed or reindented replace call
  reds rather than staging nothing.
- AC2 — OBSERVED — `ADOPTER_BAR_PATHS` — the routing assertion walks the engine's own syntax, follows
  every name a declared destination reaches through a path-shaped derivation, and finds no direct
  `write_text`
  ,
  `write_bytes`
  or open-for-write naming one. The declared set is read off the ENGINE's constant rather than
  restated in the harness. Two liveness halves are asserted: the set still reaches a destination, AND
  `write_atomic`
  is CALLED on one of them — a negative over an empty population passes identically to a negative
  over a routed one.
- AC3 — OBSERVED — `apply --target <fixture>` — the runner file this engine writes is byte-identical
  to the one the PRE-change engine wrote from the same fixture, over both shapes this unit could
  reach: the manifest write path at 247 bytes each, and the non-manifest order path at 160 bytes
  each. The pre-change engine is `HEAD`'s
  `govkit.py`
  , read out of git and run in its own scratch gov. Normalised stdout differs only in the gov commit
  sha and the fixture tag, both of which are fixture identity rather than engine behaviour; that is
  stated rather than claimed as identical.

**Evidences:** DEPL-cMendedVintage-13

- AC6 — `os.replace` — NO LONGER UNOBSERVED. That unit's ledger records the atomic write as
  implemented with no failing case, and its reason was correct at the time: nothing in that pass
  failed when it was absent. AC1 above is that failing case, staged and read. AC6 ITSELF IS UNCHANGED
  and is not re-graded here — it grades the extraction's byte parity, which is a real question and
  stays exactly as that unit wrote it. What arrives is the observation it could not make. That unit's
  own record is left as it stands, with a pointer added beside its OWED note.

## The derived write set, both lists

S2's adopter-bar set is DERIVED at build time. The candidate predicate was run over the real tree
BEFORE it was wired, and printed hits and near-misses:

- **34** write sites in the engine — `write_text`, `write_bytes`, `open` in write mode, `io.open` and
  `os.open` in write mode.
- **1 hit**, and it is the site `-13` left: the manifest write-back, reached through
  `rf = target / gr["file"]`
  . After the routing it is **0**, and the helper is the only writer.
- **33 near-misses**, every one considered and none flagged. The four worth naming, because each
  looks like a candidate until you ask who reads it: the deployed engine rows at
  `dp`
  (§3 puts these OUT — they are the bar, not a file it reads, and they have their own rollback
  story); the receipt and
  `install.sums`
  (also §3, and read by this engine rather than by a bar); the order documents under
  `.governance/outbox/`
  (prose for a human, not a manifest); and the target's
  `.gitattributes`
  pin block (read by git, not by any leg).

**The predicate was wrong on its first run and the tree said so.** A rule that propagated through any
RHS mentioning a destination pulled in three innocent names —
`existing`
,
`by_name`
and
`USAGE`
— by way of
`existing = json.loads(rf.read_text(...))`
and a usage banner that happens to contain the marker text. A later direct write to any of them would
have redded for no reason. The shipped rule propagates through path-shaped derivations only: a bare
name, a
`/`
join, a
`.parent`
, or a call to one of the path-returning methods. A read is not a derivation. This is exactly what
running a candidate over the real tree before wiring it is for, and it cost one iteration.

## The staged breaks

Four, each applied to the real engine, run, and unstaged — with the restore asserted afterwards.
Each reds its own arm and nothing else.

- **B1 — the write is IN PLACE**, the mitigation dropped:
  `dest.write_text(...)`
  where the helper had
  `tmp.write_text(...)`
  . AC1's survival half REDS, and the detail shows the runner holding gov's freshly written rows
  where it should still hold the target's own. The temp-sibling half stays GREEN, because an in-place
  write leaks nothing. This is AC1's declared RED-WHEN.
- **B2 — the cleanup is dropped**, the `finally` body replaced by `pass`. The temp-sibling half REDS
  naming
  `gate-legs.json.govkit-new`
  , and the survival half stays GREEN. This is the pair the brief warned about, separated.
- **B3 — a SECOND direct write** to the declared destination, added beside the routed call. AC2's
  routing assertion REDS naming the line and the destination. No behavioural arm moves, which is the
  whole reason S4 exists.
- **B4 — the declared set emptied** to `()`. BOTH of AC2's liveness halves RED. Without them the
  routing negative would have passed over a population of nothing, cheerfully.

## What did not run, and why

- **No gate, suite or bar ran in this pass.** The govkit self-test suite, `govkit selfcheck`, the
  refusal join and the acceptance matrix are all OWED and are named in the return. The arms this unit
  ships are not asserted by construction: their source was extracted verbatim from the shipped
  `selftest.py`
  by line span and exec'd against the suite's own `check`, `git` and `settle` and a real temp root,
  so what ran is the bytes that shipped rather than a paraphrase of them.
- **`gov` does not dogfood `govkit`** and keeps no receipt of its own, so no criterion here is
  observable against this repo. Every fixture is a throwaway target under the run's scratch root.
- **The lexicon gate did not run**, but every name this unit adds was put to
  `--suggest`
  , which is the authority: `write_atomic`, `build_runner21`, `read_bar_writes21`, `read_segment21`
  and `read_declared21` all lead with a declared verb and satisfy their cell. Five definitions, zero
  verb offenders, so the pin does not move.

## The bug classes this unit was graded against

`gate-you-have-only-seen-pass` is why there are four breaks rather than a green run and a paragraph,
and why B1 and B2 are two rather than one.

`fixture-passes-by-finding-nothing` is why AC1 carries a control. The arm watches a broken run leave
a file alone, and a run that refused three steps earlier leaves that file alone just as convincingly.
The control asserts the unbroken engine MOVES it.

`predicate-matches-nothing` is why AC2 has two liveness halves and why the predicate was run over the
real tree first. Both were earned: B4 shows the negative passing over an empty population, and the
first draft of the derivation flagged three innocent names.

`staged-break-substitutes-a-synthetic-value` is why B1 restores the pre-`-13` spelling — an in-place
`write_text`
— rather than a simpler synthetic raise. What reds is the real regression.

`ledger-token-wrapped-across-a-line-joins-nothing` was checked rather than assumed: every backticked
span in this record sits whole on its own line.
