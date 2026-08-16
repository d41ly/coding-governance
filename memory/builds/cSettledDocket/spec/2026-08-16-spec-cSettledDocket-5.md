# TOOL-cSettledDocket-5 — one leg: every self-test prints a count, in one shape, against a floor

**Status:** OPEN · rev-2 · 2026-08-16 · node c · Tier-2 · base 1da67d9c · streams tooling

## 1. Goal

rev-1 of this spec said `skills/session-kickoff/manifest-check.test.sh` "prints no assertion summary
and carries no counter". **That is false.** It declares `pass=0; fail=0` at line 9, increments at
four sites, and prints `---- 62 passed, 0 failed ----`. rev-1 had grepped for the OTHER suites'
spelling — `PASS (`, `assertions`, `n=$((n+1))` — and reported a missing CAPABILITY after measuring a
missing CONVENTION. That is the vacuous-selector class, in a spec about counting.

Measuring the whole population instead of one file gives the real defect, and it is bigger:

- **27** tracked `*.test.sh` files.
- **12** print no count at all.
- **15** print one, in **four** different spellings: `$pass passed`, `PASS ($n`, `PASS ($ncase`, and
  one bare `echo "PASS"` carrying no number.
- **3** carry a `FLOOR_ASSERTIONS`.

So `TOOL-cBriefedPilot-23`'s floor — the thing that catches a block of arms stranded past an `exit` —
guards three suites out of twenty-seven, and there is no agreed shape for a leg to check.

## 2. Scope (IN)

- **S1** — a merge-bar leg asserting that every tracked `*.test.sh` reachable from
  `tools/gate-legs.json` prints a count in one agreed shape on a green run, and declares a
  `FLOOR_ASSERTIONS`.
- **S2** — the agreed shape is `PASS (<n> assertions)`, because it is the majority spelling among
  those that carry a number and the one `check-arms.py`'s siblings already use.
- **S3** — a SHRINK-ONLY registry beside the other waiver lists, seeded from the measured
  non-compliant population, so the leg lands green and the population drains. A leg with twelve
  silent exceptions checks nothing; a leg with twelve NAMED ones ratchets. A registry row whose file
  now complies REDS as stale, the way `install-prefix-waivers.txt` already does.
- **S4** — the leg is DERIVED from `tools/gate-legs.json`, never a hand-kept list. A hand-maintained
  second population is how `check-kit-versions.sh` grew the duplicate `TOOL-cBriefedPilot`'s review
  found, and it is the same mistake one file over.
- **S5** — `manifest-check.test.sh` converts to the agreed shape and gains a floor: it already
  counts, so this is a rename and a constant, not a counter.
- **S6** — a self-test for the leg: a suite printing no count reds; one printing a count with no
  floor reds; a registry row naming a compliant file reds as stale; a compliant suite is silent.

## 3. Non-goals (OUT)

- **Converting all twelve silent suites.** That is the registry's job to force over time. Doing it
  here is a twelve-file sweep with no evidence behind eleven of them, and this build has already
  learned what an unmeasured sweep costs.
- **Changing what any assertion asserts.** Counting is additive everywhere.
- **A shared helper library.** Twenty-seven files, four fixtures, one installed per-machine via a
  junction. The leg checks the OUTPUT shape, which is the contract; how each suite produces it is
  its own business.
- **Unit 4's inline-site sweep.** That makes one suite's count WHOLE; this makes every suite's count
  EXIST. Different defects, and unit 4's file is already compliant on shape.

## 4. Design

### Why a leg and not more per-suite edits

rev-1 proposed editing one suite. The measurement says twelve are silent and four spellings are in
use, so per-suite editing has no end and no ratchet: the twenty-eighth suite lands silent and nobody
notices. A leg over a derived population is the only form that binds files nobody has written yet.

This is the M4 audit's own recommendation, and it closes three of its findings at once — the false
premise here, the counter-name collision rev-1 would have caused, and the "only leg" claim that was
wrong by twelve.

### The shape, and why `PASS (<n> assertions)`

Among the fifteen that carry a number, `$pass passed` appears seven times and `PASS ($n` five, with
`PASS ($ncase` and a numberless `echo "PASS"` making up the rest. Neither majority is large. `PASS
(<n> assertions)` is chosen because the three suites that ALREADY have floors use it, so the shape
and the floor arrive together rather than as two conventions to reconcile later.

The leg asserts the shape by RUNNING nothing: it greps the file for the emitting line and for
`FLOOR_ASSERTIONS`. Running twenty-seven suites to read their output would re-run the whole bar
inside one leg, which §3 of `TOOL-cBriefedPilot-23` already rejected for the same reason.

### The registry, seeded honestly

Twelve rows on day one, each naming a file and nothing else. The count is not written into the spec
or the leg — it is derived, after this build twice wrote a figure the tree then moved underneath,
and after `govkit`'s spec did the same thing twice more.

### Files touched

`tools/check-testsuite-counts.sh` (new) + its `.test.sh` · `tools/gate-legs.json` (two legs) ·
`memory/project/testsuite-count-waivers.txt` (new registry) ·
`skills/session-kickoff/manifest-check.test.sh` (S5) · `AGENTS.md` (the gate-suite bullet).

### Alternatives rejected

- **Deriving the population from `git ls-files '*.test.sh'`.** Twenty-seven files, but not all are
  bar legs — a suite nobody runs has no count to check. The manifest is what the bar reads, so it is
  what the leg reads.
- **Enforcing a count without a floor.** A count nobody compares to anything is what
  `check-memory-hygiene.test.sh` had for its whole life, at a hardcoded 130.

## 5. Production-readiness checklist

One new leg, one new self-test, one new registry, one suite converted. No new dependency. The leg is
grep-only, so it costs milliseconds on a bar whose legs cost minutes.

## 6. Acceptance criteria

- **AC1** — a bar suite printing no count and absent from the registry makes
  `bash tools/check-testsuite-counts.sh` print a refusal naming that file.
- **AC2** — a bar suite printing `PASS (<n> assertions)` but declaring no `FLOOR_ASSERTIONS` reds.
- **AC3** — a row in `memory/project/testsuite-count-waivers.txt` naming a file that NOW complies
  reds as stale, so the list shrinks.
- **AC4** — the seeded registry makes `bash tools/check-testsuite-counts.sh` exit 0 over the real
  tree on the day it lands, proving it was seeded from a measured population and not an assumption.
- **AC5** — `skills/session-kickoff/manifest-check.test.sh` prints `PASS (<n> assertions)` with a
  floor, and its own arms still pass — its existing `---- N passed, M failed ----` line is replaced,
  not duplicated.
- **AC6** — the leg's population is derived: adding a `*.test.sh` leg to `tools/gate-legs.json`
  without a count makes the leg red with no edit to the leg itself.

## 7. Gates

`bash tools/check-testsuite-counts.sh` · `bash tools/check-testsuite-counts.test.sh` ·
`bash skills/session-kickoff/manifest-check.test.sh` · `bash tools/run-gates.test.sh` ·
`bash tools/run-gates.sh`.

## 8. Open questions

none — the two decisions were the shape (§4, against the three suites that already have floors) and
whether to convert the twelve now or ratchet them (§3, against an unmeasured twelve-file sweep). AC4
is what proves the registry was seeded from the tree rather than from a guess, which is the failure
rev-1 of this spec actually committed.

## 9. Revision log

- rev-1 · 2026-08-16 · authored from `TOOL-cBriefedPilot-35`.
- rev-2 · 2026-08-16 · M4 audit fold, and a full re-scope. The named defect was NOT REAL: the suite
  already counts and prints `---- 62 passed, 0 failed ----`; rev-1 had measured the absence of
  another suite's spelling. Re-measuring the population found 12 silent suites, 4 spellings and 3
  floors, so the unit became the leg the audit recommended. Tier moves 1 → 2: this is a new gate's
  contract, not a mechanical edit.

## 10. Reuse audit

The shrink-only registry reuses the shape of `install-prefix-waivers.txt`, `unarmed-branches.txt` and
the drift pins — same directory, same stale-row-reds rule — rather than inventing a list format. The
derived population reuses `tools/gate-legs.json`, which `run-gates.test.sh` already treats as the
single source for what the bar runs. `FLOOR_ASSERTIONS` and the `PASS (<n> assertions)` line are
`TOOL-cBriefedPilot-23`'s, unchanged. `mutate` is NOT reused: it lives in the two unattended suites
and copying a five-line helper into a third file for one arm is a third implementation — rev-1's
reuse audit claimed the opposite of its sibling spec 4's, and both were wrong about where it lives.
