# DEPL-cMendedVintage-21 — the atomic write is one helper, and something fails when it is absent

**Status:** SPECCED · rev-1 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 30

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`DEPL-cMendedVintage-13` S6 makes the gate-runner manifest write-back atomic — `write_text` to a
sibling temp path, then `os.replace` — and names AC6 as its observation. AC6 compares the runner file
two runs of `apply` produce, which an ordinary in-place `write_text` produces identically, so the one
mitigation that unit's §4 Rollout elevates above every other can be dropped silently and the build
still closes green. Give the atomicity one named helper, route every write to a path an adopter's bar
reads through it, and observe it with a failure injected between the two steps.

## 2. Scope (IN)

- **S1** One module-level helper in `tools/govkit/govkit.py` performs the temp-sibling write and the
  `os.replace`, taking the destination and the bytes, cleaning up its temp path on any exception, and
  leaving the previous file untouched when the replace does not run. Observed by AC1.
- **S2** Every write to a path an adopter's bar reads — the gate-runner manifest at minimum, and the
  set derived at build time rather than pinned here — goes through that helper. `apply`'s write-back
  and the `update` call site `DEPL-cMendedVintage-13` S1 extracts both route through it. Observed by
  AC2.
- **S3** `tools/govkit/selftest.py` gains an arm that stages a raise BETWEEN the temp write and the
  replace and asserts two things at once: the previous runner file survives byte-identical, and no
  temp sibling is left in the directory. Observed by AC1.
- **S4** The same file gains the source-level routing assertion: no direct `write_text` or `open(...,
  "w")` targets a destination in the declared adopter-bar set, and staging one turns it RED. This is
  what makes the helper's absence observable rather than its presence merely likely. Observed by AC2.

## 3. Non-goals (OUT)

- No general atomic-write policy over every file govkit writes. The receipt, the orders and the engine
  rows are each written by paths with their own recovery stories, and widening this to all of them is
  a rewrite of the write loop rather than a mitigation for one file. The declared set is the one in
  S2 and it starts at one member.
- No fsync, no directory sync, no crash-consistency claim beyond `os.replace`. What this closes is a
  half-written file left by an exception mid-write; power loss is not in scope and the helper's header
  says so.
- No change to `DEPL-cMendedVintage-13`'s AC6. That criterion grades the extraction's byte parity,
  which is a real question, and it stays exactly as written. This unit adds the observation AC6 cannot
  make; it does not replace it.
- No lock, no concurrent-writer protocol. Two govkit runs against one target is already refused by the
  dirty precondition, and a lock invented here would be a second answer to that.

### Edges

- **consumes-from** `DEPL-cMendedVintage-13` — that unit extracts the emission and introduces the
  second writer of the manifest. Without it there is one caller, and the routing assertion in S4 has a
  population of one that cannot drift.
- **hands-off** external — nothing else in this build writes a path an adopter's bar reads.

## 4. Design

### Why AC6 cannot fail for S6's reason

AC6 runs `apply` against a fixture after the extraction and requires the runner file to be
byte-identical to the one the same command produced before it. Both the atomic write and a plain
in-place `write_text` produce those bytes; the two differ only in what is on disk when the write does
not finish. So the criterion grades the extraction, which is worth grading, and is silent on the
mechanism §4 Rollout calls the answer to the unit's sharpest risk. That is the ungraded-mitigation
shape, and the set already knows how to avoid it — `TOOL-cMendedVintage-9` AC5 and
`DEPL-cMendedVintage-6` AC2 are both source-level class assertions written for exactly this reason.

### The two observations, and why both

| observation | what it catches | what it misses |
|---|---|---|
| the injected raise (S3) | the helper is absent, or its cleanup is wrong, or the replace runs before the write completes | a second write site that never calls the helper |
| the routing assertion (S4) | a new or reverted direct write to a declared destination | a helper that is called and is itself wrong |

Either alone leaves a hole the other closes, and both are cheap. This is the same pairing the charter
asks for when it says a guard sharing state with the thing it guards is not a guard: the routing
assertion reads source, the injection reads behaviour, and no single edit satisfies both by accident.

### Inventory

| identifier | cell | what it is |
|---|---|---|
| `write_atomic` | `py.function` | the temp-sibling write and replace |
| `ADOPTER_BAR_PATHS` | `py.const` | the declared destination set the routing assertion reads |

`write_atomic` leads with `write`, the verb this module already spells for `write_text` and
`write_block`; `.lexicon.conf` declares `py.function` at `snake` over a closed verb table and
`py.const` at `UPPER`. `ADOPTER_BAR_PATHS` is a declared population rather than a directory listing,
because a set derived from a glob would grow silently and the assertion's whole value is that adding
a member is a deliberate act.

### Migration

None. No file's CONTENT changes, only how its bytes reach disk. A target mid-way through a crashed
earlier run may hold a stale `*.tmp` sibling from before this lands; the helper does not sweep those,
and that is stated rather than implied — an unknown temp file from an unknown vintage is not gov's to
delete.

### Rollout

Lands with `DEPL-cMendedVintage-13` and after it, inside the same build. There is no flag: the change
is from one write call to another and a default-OFF gate over it would mean shipping the half-written
failure mode deliberately.

### Alternatives rejected

- **Assert at source level that the write goes through a temp sibling and `os.replace`, and stop.**
  That is S4 alone. It passes over a helper whose cleanup leaks temp files on every failure, because
  it never runs one.
- **Stage the raise and stop.** That is S3 alone. It grades the one call site the arm reaches and is
  silent on the next one somebody adds.
- **Fold a stronger criterion into `DEPL-cMendedVintage-13` AC6.** M4 refuses a fold for a HIGH, and
  the finding is at HIGH because the mitigation is the one that unit's own §4 elevates: an observation
  written into the spec that owns the defect is graded by the same reading that missed it.
- **Write the manifest under a lock instead.** A lock answers concurrent writers, which is not the
  failure mode; a raise mid-write truncates the file with or without one.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/govkit.py` | the helper, the declared destination set, both call sites routed through it |
| `tools/govkit/selftest.py` | the injection arm and the routing assertion |

## 5. Production-readiness checklist

- security — the temp sibling is created inside the destination's own directory, never in a shared
  temp root, so no other principal can pre-create or swap it before the replace.
- perf / scale — one extra file create and one rename per manifest write.
- error / empty / loading states — a destination whose directory does not exist raises before the temp
  file is created and writes nothing; an exception after the temp write removes the temp file and
  leaves the previous destination; a destination that does not exist yet is created by the replace.
- observability — the helper prints nothing; its callers keep their own lines. A leaked temp file is
  what the arm asserts against, so the absence of output is not the absence of a check.
- risks — the sharp one is S2's declared set: a member nobody added is a destination nobody grades,
  and the assertion reads as coverage it does not have. The helper's header names the set and states
  that it grades the declared members only. Second: `os.replace` across a filesystem boundary raises,
  which cannot happen for a sibling path and is the reason the helper takes a sibling rather than a
  temp directory.
- testing — AC1 through AC3; AC1 and AC2 are arms over this repo's own source and need no install,
  AC3 is a fixture observation.
- migration — §4; stale temp siblings from earlier vintages are deliberately not swept.
- user docs — none. The helper is internal and changes no operator-facing behaviour.

## 6. Acceptance criteria

- **AC1** — When the arm stages a raise between the temp write and the replace and
  `python tools/govkit/govkit.py apply --target <fixture> --write` runs, the fixture's runner file is
  byte-identical to what it held before the run and the directory holds no temp sibling.
  Red when: the write is in place, so the file on disk is truncated at the raise and the adopter's
  whole bar reads a manifest that is not JSON.
  fixture: a scratch fixture target under the run's scratch root built with `intake` then `apply`;
  this repo keeps no `.governance/` receipt of its own.
- **AC2** — When the routing assertion runs over `tools/govkit/govkit.py`, no direct `write_text` or
  `open` in write mode names a destination in the declared set, and staging one turns it RED.
  Red when: the assertion is written against the two call sites by line number, which certifies the
  sites that exist and is silent on the third.
- **AC3** — When `python tools/govkit/govkit.py apply --target <fixture> --write` runs normally, the
  runner file it produces is byte-identical to what the same command produced before this unit landed.
  Red when: the helper writes a trailing newline the in-place write did not, or drops one, which reds
  an adopter's byte-comparing parity leg and is invisible to every behavioural arm.
  figure: DERIVED — the comparison is between two runs of the same command, never against a literal in
  this spec.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: `tools/govkit/selftest.py` · a raise injected between the temp write and the replace,
asserting the previous runner file survives and no temp sibling is left · no assertion floor to move.

New arm: `tools/govkit/selftest.py` · the source-level routing assertion over the declared
destination set, staged by adding one direct write to a declared destination · no assertion floor to
move.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "restore a snapshot entry whose kit key no rollback loop
selects"` was this promoted set's probe and returned no seam; its ranked rows are name-token
neighbours on `kit` and `key`, and `write_text` appears there only as a name stem in
`gen_build_index.py`, which is a different write with no atomicity requirement. So there is no
existing atomic-write seam in this repo and this unit mints the first one, which is the finding to
record rather than a phrasing to retry. What it does extend, read from source, is the arm STYLE:
`DEPL-cMendedVintage-4` S4 and `DEPL-cMendedVintage-6` AC2 are both source-level class assertions with
a staged break, and S4 here is a third instance of that shape rather than a new kind of check. The
recall probe returned the aScouredKit closing rounds by way of `DEPL-cMendedVintage-13` §10, which
record two ownership-blanking defects on this same emission step — the evidence that this file's write
path has been got wrong before and is worth an observer rather than a paragraph.

Recall terms used: `--terms "govkit rollback snapshot attributes receipt row kit orphan restore
touched_kits claimed verify outcome regenerate"`, with the question "what decided how govkit rollback
selects snapshot entries by kit and what owns the synthetic attributes row".
