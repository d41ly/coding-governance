# TOOL-cSettledDocket-4 — the hygiene suite's floor covers its helpers and not its file

**Status:** CLOSED · rev-2 · 2026-08-16 · node c · Tier-1 · base 1da67d9c · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-16-review-TOOL-cSettledDocket-1-1.md](../reviews/2026-08-16-review-TOOL-cSettledDocket-1-1.md) | spec-audit | TOOL-cSettledDocket-1 TOOL-cSettledDocket-2 TOOL-cSettledDocket-3 TOOL-cSettledDocket-5 TOOL-cSettledDocket-6 |
| [2026-08-17-review-TOOL-cSettledDocket-1-2.md](../reviews/2026-08-17-review-TOOL-cSettledDocket-1-2.md) | diff-review | TOOL-cSettledDocket-1 TOOL-cSettledDocket-2 TOOL-cSettledDocket-3 TOOL-cSettledDocket-5 TOOL-cSettledDocket-6 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-cBriefedPilot-23` gave `tools/memory-tree/check-memory-hygiene.test.sh` a runtime assertion
count and a shrink-only floor, replacing a hardcoded `PASS (130 assertions)` that had no counter
behind it at all. The counter went into the seven assertion HELPERS plus `before()`. Roughly fifty
further sites in the same file assert INLINE — `<test> || { echo "FAIL …"; st=1; }` — and are not
counted.

So the floor guards part of the file. The label says `helper assertions`, which is honest, but a
block of inline arms could be stranded past an `exit` and the count would not move. That is the exact
failure the floor exists to catch, still live over most of the file.

Measured: 60 `st=1` sites; 8 increments. Main independently measured a static call-site count of 115
and recorded that it "reconciles with nothing" — the gap is these inline sites.

## 2. Scope (IN)

- **S1** — every inline assertion site in the file increments `n`, so the printed count covers the
  whole file rather than the helper subset.
- **S2** — the increment goes BEFORE the test, never inside the failure brace. Inside, it counts
  failures rather than assertions and the number moves only when something breaks.
- **S3** — the summary drops the `helper` qualifier once the count is whole, and `FLOOR_ASSERTIONS`
  is re-pinned to the new measured total in the same commit.
- **S4** — an arm proving the count is now whole: strand a block of INLINE arms past an early exit in
  a copy of the suite and assert the floor refuses. Today that mutation is invisible.
- **S5** — `TOOL-cBriefedPilot-34` is closed by this unit and `TOOL-cTracedPromise-4` — main's row for
  the same defect, filed independently — is reconciled rather than left as a duplicate.

## 3. Non-goals (OUT)

- **Rewriting the inline sites into helper calls.** That is a 60-site refactor of a gate's own proof,
  and it changes what each arm asserts. Counting them is additive; converting them is not.
- **A derived count that replaces the pin.** The pin is a ratchet and must be lowered deliberately;
  a number a script recomputes is not one. Main's deleted-count branch already tested that reasoning
  and this unit keeps the derived-runtime-count form that answered it.
- **The other suites.** `check-unattended.test.sh` and `unattended.test.sh` assert exclusively
  through counting helpers; their counts are already whole. `manifest-check.test.sh` is unit 5.

## 4. Design

### Why before the test and not inside the brace

The inline shape is `<test> || { echo "FAIL …"; st=1; }`. Putting `n=$((n+1))` inside the brace
counts only the failing cases, so a green run reports a count near zero and the floor either never
passes or must be pinned at zero — a floor over failures is not a floor over assertions. The
increment must be its own statement before the test.

That makes the change mechanical but not blind: each site needs the statement placed on the line
above, and a site inside a loop increments per iteration, which is correct — the loop runs the
assertion each time.

### Why this file is riskier than it looks

It is the proof that the hygiene gate can fail. A sweep that mis-edits one site can turn an arm into
a no-op while the suite still prints PASS with a plausible number — the two-answers defect landing in
the file whose subject is a count that was a lie. So S4's arm is written FIRST, and the sweep is
verified by re-running the suite and checking the count against a derivation of site-EXECUTIONS —
not site count: three inline sites sit inside five-iteration loops and contribute five each. A
cross-check that gets its own arithmetic wrong is an eyeball with extra steps.

### The reconciliation with main's row

Both branches found the hardcoded 130 within a day of each other. Main deleted the number and filed
`TOOL-cTracedPromise-4` to derive one; cBriefedPilot derived one and floored it. The merge kept the
derived form, because main's own objection — an authored tally is the two-answers defect wearing a
reassuring number — is an argument for deriving, not for deleting. This unit finishes the derivation
and closes both rows against one implementation.

### Files touched

`tools/memory-tree/check-memory-hygiene.test.sh` only, plus the two backlog rows.

## 5. Production-readiness checklist

No new dependency. One file, ~50 one-line insertions and one constant. The whole risk is a
mis-edited assertion, and S4 plus the derived count cross-check are what bound it.

## 6. Acceptance criteria

- **AC1** — the suite prints `PASS (` with a count at or above its re-pinned `FLOOR_ASSERTIONS`. The
  rise is NOT the number of sites edited: three of them sit inside five-iteration loops, so each
  contributes five. The expected total is derived by counting site-executions, and the derivation is
  written into the commit message so a future reader can re-check it rather than trust it.
- **AC2** — stranding a block of INLINE arms past an early `exit` makes the suite refuse with
  `arms are UNREACHABLE rather than absent`. The stranded block must NOT contain the summary line
  itself, or the suite prints nothing and the arm passes on absence rather than on the refusal —
  the observable has to survive the mutation that is being observed.
- **AC3** — no assertion changes meaning: `grep -c 'st=1'` is unchanged at 60 before and after.
- **AC4** — the summary no longer says `helper assertions`, because the count is whole.
- **AC5** — `bash tools/memory-tree/check-memory-hygiene.test.sh` exits 0.

## 7. Gates

`bash tools/memory-tree/check-memory-hygiene.test.sh` · `bash tools/memory-tree/check-memory-hygiene.sh` ·
`python tools/memory-tree/check-arms.py` · `bash tools/run-gates.sh`.

## 8. Open questions

none — the one decision, whether to count inline sites or convert them to helper calls, is taken in
§3 against the cost of refactoring a gate's own proof. AC3 is the guard that the additive choice
stayed additive.

## 9. Revision log

- rev-1 · 2026-08-16 · authored from `TOOL-cBriefedPilot-34`, folding in main's independently filed
  `TOOL-cTracedPromise-4`.
- rev-2 · 2026-08-16 · M4 audit fold. §10 named `mutate`, which does not exist in the one file this
  unit touches. AC1's arithmetic ignored that three inline sites sit inside five-iteration loops.
  AC2's stranding mutation could kill its own observable.

## 10. Reuse audit

The counter, the floor constant and the refusal message are all `TOOL-cBriefedPilot-23`'s, already in
this file — this unit widens their population and changes no mechanism. `mutate` is NOT available here: it lives in the two unattended suites and
not in this file, which is the only one this unit touches — rev-1's reuse audit claimed otherwise
and its sibling spec 5 claimed the opposite, so one of the two was always wrong. S4's fixture edit
does its own `git hash-object` before-and-after comparison inline, which is the same three lines
without a third copy of the helper. No new helper is added: the reason the inline sites are not converted to `hit`/`miss`
is in §3, and converting them would be the larger diff, not the smaller one.
