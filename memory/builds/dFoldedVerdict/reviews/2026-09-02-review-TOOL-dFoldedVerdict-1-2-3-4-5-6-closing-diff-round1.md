**Serves:** diff-review TOOL-dFoldedVerdict-1 TOOL-dFoldedVerdict-2 TOOL-dFoldedVerdict-3 TOOL-dFoldedVerdict-4 TOOL-dFoldedVerdict-5 TOOL-dFoldedVerdict-6

# Closing diff review, round 1 — five lenses over the cumulative diff

*Node d, 2026-09-02, owner-present build under `memory/guides/BUILD-METHOD.md` M8.*

## Verdict: BLOCKED

**Scope: the diff range `adc0543c..8ce16163`**, 61 files, +5836/−334 — and for the protocol lens
specifically, that range **over both halves of the pair**, `memory/guides/UNATTENDED-PROTOCOL.md`
and `tools/unattended/PROTOCOL.template.md`, read as a DIFF and never as the post-image. A reviewer
handed the finished document reads a fluent file with nothing to compare against, which is how a
dropped claim survives a pass. The instrument is what LEFT the document.

The dropped-claim lens was briefed on the six categories that may never be cut: a RULE, a
MEASUREMENT, a stated COST, a REFUSAL'S REASON, a "what this does NOT do" clause, and a LIVENESS
assertion.

## Shape

Five parallel finder lenses, no skeptic stage. **The verify step was performed by the orchestrator
rather than delegated**, by reproducing each blocker and each high against the tree before acting on
it — stated plainly because §8's default shape is find → refute → synthesize, and a self-verified
finding is a weaker instrument than an adversarial one. Every finding acted on below was reproduced;
none was taken on the lens's word.

Lenses: driver-and-checker correctness · retrofit data integrity · hook predicate bypasses ·
dropped claims in carriers · gate and arm integrity.

## Verdict

**28 findings, 3 blockers, all confirmed and all folded.** The build does not land as it was written.

| # | Sev | Where | What |
|---|---|---|---|
| B1 | blocker | `agent-cap.js` C6 | the receiver clause matched the FIRST `of <ident>)` anywhere on the header LINE, so a block comment, a guard clause or an outer loop supplied a bounded token for a loop iterating caller-sized data. Four executed reproducers, one agent per element |
| B2 | blocker | `agent-cap.js` sweep | the one-call sweep counted admitted LINES, not CALLS. Five awaited calls on one line contributed one entry; 25 spawns admitted under a marker naming 5, and 40 in one `push()` |
| B3 | blocker | `check-unattended.sh:307` | no `--follow` on the first-commit date. `--preflight` rotates a terminal `RUN.md` to a NEW path, so every grandfathered record flips to GRADED on its next rotation and reds forever on an append-only archive. Eleven tracked records were live fuses |
| H1 | high | `agent-cap.js` | no script-wide total: two honest markers multiplied (5×5) and four sequential ones summed. An UNMARKED outer loop did it unboundedly |
| H2 | high | `check-unattended.sh:308` | an EMPTY first-commit date grandfathered, where the unit's own spec said in as many words to invert that clause. The in-flight run — the one case that can still record a disposition — got the proxy |
| H3 | high | `check-unattended.sh` | the closed set was RESTATED in the leg instead of read from the driver, against this file's own header rule. Widen the driver's set and the leg tells a record it was hand-edited when the driver wrote it |
| H4 | high | `unattended.sh:3935` | `case "|$SET|" in *"|$v|"*` matches any pipe-bounded SUBSTRING, so `--disposition 'fold\|promote'` was accepted, written to an append-only record, and reached the branch whose own comment certifies it unreachable |
| H5 | high | `check-unattended.test.sh` | the fixture never seeded `VERBS.template.md`, so three of unit 5's arms could never pass and two more passed VACUOUSLY. `check-arms` called all five ARMED — it matches the literal, and cannot tell an arm that can never pass from one that can |
| H6 | high | `check-unattended.test.sh` | `mkdisp` staged the record and never committed it, so the cutoff was inert: the 2099 and 2000 fixtures produced byte-identical output and the grandfathering arm proved nothing |
| H7 | high | `UNATTENDED-VERBS.md` | the new carrier inherited the protocol's parity hazard and said nothing about it — and the false `--review` sentence travelled into it under exactly that silence |
| H8 | high | `aClosedDocket/RUN.md` | the retire row takes that build's owed-parked count 0 → 1 against an attested `0 surfaced`, so a resumed `--close` refuses. Not repairable from here |
| H9 | high | `memory/LIVE.md` | retiring the last open unit dropped `aClosedDocket` from the derived index while its run still reads `phase: BUILDING` — the roster change the row exists to publish is absent from the one place §5 sends a resumer |
| H10 | high | `aClosedDocket-4` spec | a successor pointer is a CONTENT change; the flip landed at `rev-2` with no §9 line and the date unmoved, against `TEMPLATE-SPEC.md` and against this build's own spec |

Nine mediums and lows follow the same shapes: a derived count in prose (three separate instances), a
dangling `(§10)` in a file with no sections, two sibling carriers still describing a verb section the
protocol no longer has, a code comment still saying "both markers", the guides index missing the new
half, and the malformed-cutoff skip announcing one clause while skipping three.

## The four disposition values were CONFIRMED

The data-integrity lens went to every cited source and checked all seven blockers across the four
exits. All four values are right, including the mixed subject. It also confirmed that no other row,
key or byte moved in either append-only record, that `disposition-source` collides with no `fact()`
prefix, that the appended field is byte-identical to what the driver emits, and that the retire row
matches check 24's predicate while avoiding its successor arm.

## Three findings about this review's own instruments

**`check-arms` marked five arms ARMED that can never pass.** It matches the branch's literal message
in the paired test file; a fixture that cannot reach the branch is invisible to it. That is the same
could-not-fail shape the charter names, one level up, and it is now recorded in
`memory/gotchas/arm-literal-strands-on-message-edit.md` alongside the two limits unit 2 measured.

**The no-regress ratification tests NECESSITY, not soundness.** Every bypass B1–H1 was graded a
declared affordance by it: BASE denied, tip admits, strip the marker, denial returns. It cannot red
on this class by construction, and its population is one. Recorded rather than redesigned — the
bypasses it failed to catch are now closed at the source, and its own could-not-fail hole (passing
by never running) was already closed by the zero-ratifications refusal.

**Two of the three blockers were in the clause the unit claimed carried its weight.** Unit 4's build
record said the bounded-receiver clause and the one-call sweep were what made the marker real. Both
were the defects. A spec's own account of where its risk sits is a hypothesis, not a finding.

## What was filed rather than folded

- `TOOL-dFoldedVerdict-8` — `for await (` and `do{}while()` bypass the loop ban outright, both
  measured. The DENY side; mixing it with an ADMIT-side widening makes one diff unreviewable.
- `TOOL-dFoldedVerdict-9` — the two cross-build consequences H8 and H9. A cross-build amendment is a
  write into a state machine the writer does not own, and this kit has a verb for the row and nothing
  for the arithmetic the row moves.
- The `--verdict` membership test has H4's identical hole and is PRE-EXISTING. Fixing a second closed
  set inside this fold is the mixing the fold exists to avoid.
- Clause C5 of the sequential marker remains shipped unexercised; no fixture reaches it, because C2
  refuses first in every shape that gets close.
