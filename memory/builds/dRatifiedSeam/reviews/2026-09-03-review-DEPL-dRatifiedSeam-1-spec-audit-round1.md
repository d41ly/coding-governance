**Serves:** spec-audit DEPL-dRatifiedSeam-1 TOOL-dRatifiedSeam-1

# Spec audit round 1 — dRatifiedSeam

Tier-2 · node d · 2026-09-03 · subject: both specs at rev-1, before any code

## Verdict: CLEAN WITH FIXES

The audit was SELF-review, which is the weaker instrument, and this record says so rather than
implying a cold pass happened.

**This record exists because `--close` refused without it, and the refusal was right.** The audit
happened and its findings are folded into both revision logs, but no record carried a `spec-audit`
binding line, so the pre-code pass the build method makes must-by-default had left no evidence a
machine could read. An audit nobody can find is an audit nobody can check.

**Five cold reviewers died before any of them read a spec.** Two workflow fans lost all five lenses
to server 529s — the second failing at spawn with `subagent_tokens: 0`, so narrowing the fan bought
nothing — and three independent agents then died the same way. The fan's return in both cases was
`{"findings": [], "note": "five lenses returned nothing"}`, which is byte-identical to a clean
audit; only the `<failures>` block below the result distinguishes them.

So I audited my own specs. That is the weaker instrument and the record says so rather than
implying a cold pass happened.

## The eight findings, all verified against the tree

Four were acceptance criteria that could not fail, in the specs of a build about checks that cannot
fail:

- **DEPL AC1's antecedent did not exist.** It read *"when a write run adds a tracked file"*, and no
  fixture arm added one, so the criterion could pass with the relaxed direction never taken.
- **DEPL AC3 and AC6 were SELF-GRADED.** Each admitted a comment or a ledger sentence as its
  answer — the gate-satisfied-by-its-own-prose class. AC3 now demands the operator or a cited arm;
  AC6 is the exit status, with prose as evidence rather than as the criterion.
- **TOOL AC5 was ALREADY TRUE before the unit started.** Measured: `unattended-build.test.sh` exits
  0 at 21 arms today, so the criterion was satisfied by building nothing. It now requires the count
  to RISE.
- **TOOL AC6 named a witness that is not an interface.** `agent-cap` reads a PreToolUse payload from
  stdin (`readFileSync(0)`) and uses `process.argv` only for `--only=`; given a path it HANGS,
  measured `rc=124`.
- **TOOL AC4 graded an ABSENCE** over a scope no machine defines — deleting the prompt would have
  satisfied it.
- **DEPL AC8 and TOOL AC7 were bare green bars**, which `memory/TEMPLATE-SPEC.md` names as the
  unrelated-green-gate shape.

## What the audit did NOT catch, and could not have

The closing diff review then found sixteen more, including two blockers: `TOOL-dRatifiedSeam-1` did
not work at all, because `tier2-review.js` has never returned the `verdict` key its adapter read;
and the landing could write outside the adopter's repository three separate ways.

None of those is a spec defect. They exist only in code, and no reading of a spec would have
surfaced them. That is the argument for both passes rather than either — and it is also why the
cold pass on these specs remains genuinely owed, not discharged by the closing review having been
thorough.

## Disposition

Folded as `DEPL-dRatifiedSeam-1` rev-3 and `TOOL-dRatifiedSeam-1` rev-2, each finding named in the
revision log of the spec it belongs to. No finding was promoted to a unit; all eight were
corrections to acceptance wording, which is what a pre-code audit is for.
