**Serves:** journal TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-12

# Build pass, steps 6 and 7 — the canon overlay, surface-aware suggest, and the arming commit

Node `a` · 2026-09-05 · build `aSurfacedLexicon` · streams tooling. The last three units, sequenced.
Unit 12 is the one that ARMS the build: it writes the full cell matrix into the declaration and flips
the undeclared-cell constant in the SAME change, which is what turns a report-only arm into a refusal.

**Evidences:** TOOL-aSurfacedLexicon-11
- AC1 — amended rev-7 — re-keyed off the exit code. All three of AC1, AC2 and AC3 graded the wiring check by its EXIT STATUS, and that check reds in any sandbox with no rendered Skill, so every scratch-tree run is non-zero whatever the stamp says. AC1 asked for an exit-0 its own fixture could never produce, and the other two asked for a non-zero that was true on every run and evidence about none. All three now read the MESSAGES.
- AC2 — an overlay block with a stamp carrying a date and node but no REASON — refused under its own wording, textually distinct from the empty-stamp refusal.
- AC3 — amended rev-7, with AC1 and AC2, for the same cause.
- AC4 — the posture line — printed ABOVE the counts on both a passing and a failing run, so an unfreeze cannot be read past.
- AC5 — the merge with no overlay declared — byte-identical to the shipped canon, asserted in-process against the constant rather than against a reading of it.
- AC6 — replace, add and delete — six arms, each asserted through all three canon accessors. All six red when the merge is suppressed.
- AC7 — the refusals — four, not the three the spec named, and a fourth arm asserts they are pairwise distinct so no refusal wears another's message.
- AC8 — a canon block staged into the scaffolder's output — refused, naming the file and line.
- AC9 — the guard's own population — measured, with the one near-miss pinned so a later reader knows the count is what it is by design.
- AC10 — the wiring check on the tracked tree — green, so the refusal branch does not fire on the frozen state every adopter who is not the author sits in.
- AC11 — a self-exercising arm inside the wiring check — suppressing the merge makes it say the overlay did not reach the answer.
- AC12 — the written statement that no machine check can tell a considered overlay from a mirror — present in both carriers, and deliberately ungated, because gating a sentence is how prose becomes a checkbox.
- AC13 — a stamped overlay that moves a pin — the run names the OVERLAY as the cause, observed in BOTH directions: present with the overlay, absent from a fixture that moves the same two rows without one.

**Evidences:** TOOL-aSurfacedLexicon-8
- AC1 — a name asked for in a declared cell — answered in that cell's convention.
- AC2 — the same name asked for in a different cell — a different answer, which is the whole point of the surface being an argument.
- AC3 — amended rev-6 — the criterion PASSED ON A RUN WITH THE GUARD DELETED. It asked that the message name the required flag, and the malformed-cell refusal names the same flag, so deleting the required-flag guard left it green. Re-keyed onto the wording only that guard prints, plus a second arm asserting the two neighbouring refusals are absent.
- AC4 — the re-caser over four names — including one whose acronym span must survive re-casing, which is the case the original headline input never reached because the classifier already accepted it.
- AC5 — a name carrying a character the splitter cannot see — refused rather than re-cased, and the refusal is NARROW: only for a character the target convention does not itself re-supply.
- AC6 — a bare surface with no extension — refused with the declared cells listed, so the refusal is a menu rather than a wall.
- AC7 — the answer for a cell whose convention is unset — falls back rather than inventing one.
- AC8 — the rendered Skill — byte-compares after the placeholder change.

**Evidences:** TOOL-aSurfacedLexicon-12
- AC1 — the declaration's pin region after the rewrite — the recorded-move narration is gone, measured by a head-anchored grep rather than a loose one.
- AC2 — amended — the criterion claimed a command emits a block of per-cell rows; it emits two scalar pin lines and no block. Re-keyed onto the two lines it can actually compare.
- AC3 — the three owed decision records — written, each carrying its supersession.
- AC4 — amended — the criterion banned a superseded figure from the supersession notes, and the notes carry it deliberately, because this repo quotes a superseded claim beside its supersession and a note saying the figure did not reproduce cannot say so without naming it. Re-keyed onto the figure a note ASSERTS.
- AC5 — the kill-rule reading — re-run and recorded as what the signal actually reports, which is ABOVE the threshold the rule watches and therefore BREAKS the downward chain rather than continuing it.
- AC6 — the status of a unit carried by three carriers — all three now agree.
- AC7 — the spec-template line — landed in both halves of the rendered pair.
- AC8 — the charter edit — measured on BOTH byte-capped halves, the rendered one being the tighter.
- AC13 — the pin rows blank-separated — verified on the raw lines.
- AC14 — the cell matrix and the arming constant — asserted over the COMMIT rather than the tree, because the two landing separately is the exact failure the item exists to prevent, and a tree-scoped check cannot see it.

## What the revert matrix found in this pass

**Seventeen mechanisms across this build were UNGATED when first written** — reverting each left a
fully green suite. This pass alone found ten, and the most serious was the canon door's entire
RECORDED half: replacing one row-count guard with a constant false deleted BOTH stamp refusals, and
nothing noticed. The build's own rule is that an unfreeze must be visible and recorded, so the
mechanism enforcing the record was the one mechanism that must not be silently removable.

**Two arms passed for the wrong reason**, which is worse than absent. One asserted a refusal by
grepping for a flag name that a NEIGHBOURING refusal also prints, so it stayed green on a run with
the guard deleted. Another asserted only that the word "line" appeared, which meant five sibling
refusals looked covered while a sixth had no fixture at all — any one firing satisfied any row.

**And removing a refusal does not always make a reader permissive; sometimes it makes the next line
crash.** Two staged breaks produced an unpacking error and an index error rather than a silent pass.
An arm catching only the domain error would have let those propagate and redded the suite with a
traceback naming the reader instead of the arm that knows which check went missing.

## The structural finding, filed rather than fixed

Every one of those seventeen was a PYTHON branch, and the kit's shell files are armed and clean
throughout. That is not a difference in discipline: `check-arms.py`, the meta-gate for unarmed refusal
branches, discovers its population as tracked shell files, so a Python refusal is outside it **by
construction** — not waived, not exempted, invisible. A reader who trusts that gate reads green over a
population it never scanned, which is the green-by-absence class inside the checker written to prevent
it. Filed as `TOOL-aSurfacedLexicon-21` with the shape of a fix and the reason it is not a one-liner.
