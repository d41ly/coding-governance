**Serves:** diff-review TOOL-dHonouredPark-1 TOOL-dHonouredPark-2 TOOL-dHonouredPark-3 TOOL-dHonouredPark-4

*Range `c68956ee...HEAD`, the cumulative diff landing on main, reviewed once at the integration
boundary per §8 rather than per increment. **ROUND 3.** Node d, 2026-08-25.*

# Closing diff review, round 3 — the fold that gated the instance and shipped the class

Round 2 confirmed eight defects, every one introduced by round 1's own fold. This round reviews the
fix for those eight. The pattern held: five of the seven defects below were introduced by round 2's
fold, and three of them are the *same class* the fold's own comments cite while fixing it one branch
over.

**Review shape.** Raw 15, confirmed 13, refuted 2, unverified 0, precision 0.87. The 13 confirmed
reports collapse to **7 distinct defects** — four lenses independently found the `scan_canon`
suppression, and two pairs found the `--plan` vacuity and the `_renderable` divergence.

## Verdict: BLOCKED

One blocker, one high, five medium, zero low. The blocker is live on the tracked corpus today, not
latent: five builds answer the unattended run's pick-up-work verb with an affirmatively false
terminal-status claim at exit 0.

| Severity | Distinct defects | Confirmed reports |
|---|---|---|
| BLOCKER | 1 | 2 |
| HIGH | 1 | 1 |
| MEDIUM | 5 | 10 |
| LOW | 0 | 0 |

Two severities were raised from what the lenses graded, and both raises are stated where they occur.

---

## BLOCKER

### R3-B1 — the empty-region guard's new `_renderable` conjunct restores the false all-clear its sibling fix removed

**Where.** `tools/unattended/unattended.sh:1643` (the guard), surfacing at
`tools/unattended/unattended.sh:1715` (the tail echo).

**Raised from HIGH.** Both lenses graded this high. It is graded a blocker here because it is live on
the tracked corpus rather than reachable in principle, it sits on the one verb the kit's own skill
text tells an unattended agent to read, and the arm covering that branch does not assert the line
that is wrong.

**What.** R2-H2 correctly stopped the empty-region guard refusing builds whose specs render no row,
because the repair it named could not change those trees. It did so by conditioning the guard on
`[ "$_renderable" -gt 0 ]`. That removes the refusal and leaves nothing in its place: with
`_renderable` at zero, `_ids` is empty, the grading loop runs zero times, `next` stays unset, and the
verb falls through to `next: none - every tracked spec is terminal` at exit 0 — over a build it
graded nothing on.

**Evidence.** Reproduced on the real corpus, not a fixture. `bash tools/unattended/unattended.sh
--plan aDeployScout` prints `NOT A UNIT (no status header)`, then the roster line, then `next: none -
every tracked spec is terminal`, and exits 0. A sweep over every tracked build finds five in this
state today: aDeployScout, aKitHardener, aLeanRework, aPortableWarden, aRatchetForge. In each, the
only tracked spec is reported one line above as not a unit — so it is not terminal, and not even
gradeable. The pre-fold driver at `c68956ee` held the guard unconditionally and above the spec
listing, so it refused these same trees with fail 42 at exit 1.

**Not a pure regression, and it does not matter.** One lens noted honestly that at round 1's base the
same tail line already printed for these five builds; the intervening guard masked it behind a
check-42 refusal, and R2-H2 correctly removed that refusal and restored the false tail with it. The
defect is real and unfixed on either reading.

**The rule this breaks is the build's own.** Round 2's graded record states it verbatim while fixing
R2-H1: the verb must never print `next: none` over a region it could not grade, because that is a
false all-clear on the verb an agent reads to pick up work. R2-H1 gated the foreign-slug instance.
This is the sibling instance of the same class, one branch over.

**Why it is worse than a wrong string.** The failure mode is corruption-shaped. A spec whose status
header stops parsing — a one-space indent, a CRLF or BOM smudge, a truncated write — silently
converts from a gradeable unit into "nothing left to do", instead of into a refusal.

**Fix.** Keep the reordered guard and the removed refusal. Make the tail honest instead: track
whether any unit row was actually graded, and branch the final line on it. Set a `_graded` flag
inside the `for id in $_ids` loop, and where nothing graded and nothing is missing, emit a distinct
verdict — `next: none - no tracked spec grades as a unit (see the NOT A UNIT rows above)` — rather
than the terminal wording. The terminal wording at `:1715` must be reachable only when at least one
spec was graded.

**Left-shift gate.** A corpus leg, not a fixture leg: run `--plan` over every tracked build and red
on any run whose output carries both a `NOT A UNIT` row and the terminal verdict line. That predicate
reds on all five live builds today, which is the failing case observed before the gate lands (§7),
and it gates the class rather than the branch — a future widening of any exemption trips it wherever
it is written.

---

## HIGH

### R3-H1 — the R2-H2 arm asserts only that the refusal went away, never what the verb says instead

**Where.** `tools/unattended/unattended.test.sh:1736-1737`.

**Raised from MEDIUM.** Graded medium by the lens. Raised because it is the left-shift half of the
blocker above: without it, the blocker's own fix lands with no observed failing case, which is the
defect §7 names outright.

**What.** The new arm is `hit "$out" "NOT A UNIT (no status header)"` plus `miss "$out" "so the
region is stale"`. Both assertions pass over output whose last line is the false all-clear at exit 0.
That is exactly how R3-B1 shipped green.

**Evidence.** Both of the arm's immediate siblings guard the line this one omits. The empty-region
arm at `:1722` carries `miss "$out" "every tracked spec is terminal"`, and the R2-H1 foreign-slug arm
at `:1748` carries it too. The one arm covering the branch that actually reaches the honest-verdict
question is the one that drops it. Rebuilding the fixture in a scratch repo produces the NOT A UNIT
row, the roster line, then the terminal verdict at exit 0 — and both assertions hold.

**Same class the fold names about itself.** The driver comment at `unattended.sh:1601` describes
R2-M3's defect as an arm that asserted the refusal TEXT without looking at the table above it, which
is how it shipped. This arm asserts the refusal's ABSENCE without looking at the line below it. Same
shape, opposite polarity, one branch over.

**Fix.** Add `miss "$out" "every tracked spec is terminal"` to the arm, plus a positive `hit` on
whatever honest verdict line R3-B1's fix emits. Add a second arm for the realistic shape — a spec
whose `**Status:**` line is merely indented, so the build has a would-be unit that failed to parse —
because the current fixture uses a file that was never a spec at all.

**Left-shift gate.** Adding that `miss` today reds the suite, so it is a failing case observed before
the gate lands. Beyond it: an arms-floor rule for this verb, asserting that every `--plan` arm in the
suite pins the `next:` line, positively or negatively. Three of the four already do; the floor makes
the fourth's omission impossible to repeat.

---

## MEDIUM

### R3-M1 — the near-miss early return skips the heading-canon scan entirely, and nothing says so

**Where.** `tools/memory-tree/gen_build_index.py:1310-1311`, whose early return sits above the
`scan_canon` pass at `:1328`.

Found independently by four lenses, graded low to medium. Recorded medium.

**What.** R2-M2 correctly stopped the marker-count branch misdiagnosing a whitespace-perturbed marker
as absent or duplicated. It did so with an early return out of the whole function. The count branch
is what the near-miss invalidates; the canon scan reads headings and has no relationship to the
roster marker at all. So one stray space on one marker line silently suppresses every heading-canon
finding in the same file.

**Evidence.** Reproduced against a live bound README. Calling `slot_violations` on
`memory/builds/dFramedEntrypoint/README.md` with canon enabled returns empty on the clean file.
Renaming the canonical heading `## The problem this build exists to solve` yields six findings — one
missing slot, four out-of-order, one heading outside the canon. Indenting the roster open marker by
two spaces in that same text collapses the result to the single near-miss line, and all six canon
findings vanish. Running the same fixture against `a2832066^` returns the marker finding AND all six
canon findings, so this is a behavioural regression of this fold and not prior behaviour.

**Scope, stated honestly.** No false green. Both callers red on any non-empty list, and
`--check-format` is clean today at 338 artifacts, so the merge bar still blocks. The harm is a
truncated report: a fixer repairs the whitespace, re-runs, and is handed findings the gate already
knew about. It is also asymmetric in a way no design rationale covers — triggers 1 and 2 still report
because they populate the output list earlier, and only trigger 3 is dropped.

**The class is this project's own.** A skip must announce itself (§7). The canon pass does not run
and the output does not say so.

**Fix.** Do not return early. Accumulate the near-miss rows, then guard only the marker-count and
transposition block with an `else:`, and leave the canon call on the unconditional path before the
single return.

**Left-shift gate.** A selftest arm asserting that a canon-bound README with BOTH a perturbed marker
and a broken canonical heading reports both classes. It reds on today's code, which is the observed
failing case. The generalisable version: an arm per trigger asserting no trigger can suppress
another, since the function's whole contract is that its findings are a union.

### R3-M2 — the near-miss predicate misses a marker that is both indented and carries trailing text

**Where.** `tools/memory-tree/gen_build_index.py:1307`.

**What.** The predicate tests the raw line against the marker, the stripped line for equality, and
the raw line for a prefix. The strip arm catches pure indentation; the prefix arm catches pure
trailing text; neither catches the combination. So a marker that is both indented and trailed falls
through to the count branch and gets the exact false-absence diagnosis R2-M2 was written to
eliminate.

**Evidence.** A README whose roster open line is two spaces, then the marker, then a trailing token
returns exactly `the authored roster pair is not exactly one open and one close marker — found 0 open
and 1 close`. The open marker is present and merely malformed, and the reader is told zero were
found. A tab-indented, tab-trailed variant behaves identically. The inconsistency is the proof it is
a defect rather than a scoping choice: the same trailing text with no indent IS correctly named "not
the marker alone", and adding two leading spaces flips the same file to a wrong diagnosis.

**Fix.** Test the stripped line for the prefix as well — bind the stripped line once, and match when
it equals the marker, starts with the marker, or the raw line starts with the marker.

**Left-shift gate.** A third arm beside the two added at `:2032` and `:2038`, driving an indented AND
trailed marker and asserting the not-the-marker-alone message. The class-level version, which is what
§7 asks for: drive the arm from a small matrix of perturbations — indent, trail, both, tab forms —
rather than one arm per remembered case, so the next unenumerated combination cannot ship unarmed.

### R3-M3 — the negative-control arm asserts a string no message in the module can emit

**Where.** `tools/memory-tree/gen_build_index.py:2034-2036`.

**What.** The arm named "...and is NOT reported as duplicated" tests whether the retired word appears
in the violations and expects the answer to be false. The same commit reworded the count message away
from that word, so the substring is now unreachable for every input. The arm is a tautology, and
R2-M2's ordering fix therefore ships with no failing case ever observed.

**Evidence.** Grepping the module for the retired word returns four hits: three comments and the arm
itself. No violation message emits it. Staging the break in a scratch copy — reverting R2-M2's fix so
the near-miss rows are merely appended after the counts — produces the two-finding output R2-M2 names
as the defect, the false-absence count line alongside the near-miss row, and both new arms still
pass. Same result for the trailing-space fixture.

**Fix.** Assert the count branch is ABSENT rather than the retired word: check that the phrase "not
exactly one open and one close" does not appear in the violations for the perturbed fixture.

**Left-shift gate.** The generalisable form is a negative-control audit for this module's arm
harness: for each arm whose expectation is a bare false or an absence, assert the probe string occurs
somewhere in the module's emitted message set. An arm asserting the absence of a string the code can
never produce is a fixture that passes by finding nothing, which is already on this diff's own
checklist — this makes it machine-detectable instead of remembered.

### R3-M4 — `_renderable` is a looser third spelling of "is this spec a unit", so the stale-region refusal can still name an inert repair

**Where.** `tools/unattended/unattended.sh:1620-1632`, consumed by the guard at `:1643`.

Found by two lenses, one framing it as a divergence from the generator and one as a duplication of
the file's own `spec_ids()` helper at `:1517`. Same defect.

**What.** The driver's inline awk pair accepts any uppercase status token after the status label and
any alphanumeric first word after an H1 hash, whole-file and fence-blind. The renderer that owns the
answer requires the full status tail — rev, date, node, tier, base sha — and matches it only within
the first five unfenced lines, plus an H1 carrying the em-dash separator. Where they disagree,
`_renderable` is positive while the renderer emits no row, and the guard fires fail 42 naming
`--write` as the repair on a tree `--write` provably cannot change. That is precisely the
inert-repair defect R2-H2's own comment says it removed — narrowed by one notch rather than
eliminated.

**Evidence.** The divergence is verified directly: the generator's header regex rejects a status line
lacking the tier and base fields, and its H1 regex rejects a heading without the em-dash separator,
while the driver counts both as renderable. Reproduced end to end in a scratch repo: a spec with a
tier-less, base-less status header plus a valid H1 makes `--plan` exit 1 with the stale-region
refusal and the `--write` repair. Scanned all 277 tracked specs — zero disagree today, so this is
latent, not firing. Reachable via a staged spec, since the driver reads `git ls-files`, and in an
adopter repo where the hygiene cutoff is blank and the strict-header check is off entirely.

**Caveat on the obvious fix.** Reusing `spec_ids()` deduplicates the spelling but does not close the
divergence, because that helper spells the same loose patterns.

**Fix.** Condition the guard on something the renderer itself publishes, so the two tools cannot
answer differently. Failing that, tighten the driver's two awk patterns to the generator's exact
shape and gate the pair.

**Left-shift gate.** A parity leg: for every tracked spec, compare the driver's renderable verdict
against the generator's parsed verdict, and red on any disagreement in either direction. That is the
single-source-to-generated-artifact-to-parity-gate rule from §7 applied to a predicate rather than a
file, and it is the only form that survives a fourth spelling being added later.

### R3-M5 — R2-M3 moved the roster guard above the listing and left the arm that was meant to catch that unchanged

**Where.** `tools/unattended/unattended.test.sh:1759-1760`.

Found by two lenses; one executed nothing and said so, the other verified against the commit. Same
defect, same fix.

**What.** R2-M3's stated purpose was ordering: resolve the roster before a single row prints, because
the old placement produced a complete-looking table and only then a refusal. The commit moved the
code and left the arm byte-unchanged. That arm does a `hit` on the refusal text and a `miss` on a
sentence that is unreachable in both orderings, so reverting the move keeps the suite green.

**Evidence.** The test diff for `a2832066` touches the driver and not this arm. The pre-fix guard sat
at the bottom of the verb with a byte-identical message, so the `hit` matches either way. The `miss`
targets a sentence in an else-branch that an early return skips in both orderings. The fixture is
genuinely capable of printing a table under the revert: its units region carries one row, so neither
sibling guard would preempt the roster refusal, and the helper's exit 3 is consumed by a `for` loop
that discards it. Nothing else in the arm distinguishes the two orderings — the refusal message
carries only the README path and never a unit id.

**The fold names this defect about itself.** The driver comment at `unattended.sh:1600` says the arm
meant to catch the old ordering asserted the refusal TEXT without looking at the table above it,
which is how it shipped. The fix repaired the code and left the arm that shipped it.

**Fix.** Add a `miss` on the fixture's unit id after line 1760. With the guard at the top the verb
returns immediately and prints no unit row, so the id appears nowhere; with the guard back below the
listing the row prints it and the arm reds.

**Left-shift gate.** Ordering is not gateable by string membership in general, so the durable form is
structural: assert the refusal path emits **exactly one line**. That holds for every guard in the
verb, not just this one, and it is the assertion round 2's own left-shift column already proposed and
the fix did not land.

---

## The two refuted findings

Both were dropped after a skeptic re-established neither reachability nor impact, and neither is
recorded here as an open item. Precision for the round is 0.87, comfortably above the ~0.5 floor at
which §8 says to tighten scope before adding agents — consistent with a small, dense diff over code
two prior rounds had already hardened.

## Left-shift summary

Seven defects, seven proposed gates. Five of them gate a CLASS rather than the instance found, which
is the distinction §7 draws and the one this fold kept missing:

- A corpus leg running `--plan` over every tracked build, redding on a NOT A UNIT row beside a
  terminal verdict. Reds on five builds today.
- An arms floor requiring every `--plan` arm to pin the `next:` line.
- A union assertion for the slot-violation function — no trigger may suppress another.
- A perturbation matrix for the marker predicate, replacing one arm per remembered case.
- A negative-control audit for the arm harness — an expectation of absence must name a string the
  module can actually emit.
- A parity leg comparing the driver's renderable verdict against the generator's parsed verdict.
- A one-line assertion on every refusal path in the verb.

## What this round says that round 2 could not

Round 2 found that round 1's fold introduced every defect it confirmed. Round 3 finds the same of
round 2's fold, and can now name why rather than noting the coincidence. Three of the seven defects
here sit one branch over from a comment, written in the same commit, describing that exact defect.
The fold is not failing to see the class — it is writing the class down, gating the instance in front
of it, and moving on. Every gate proposed above is therefore scoped to the class deliberately, and
the two severity raises both turn on the same question: whether the fix ships with its failing case
observed.
