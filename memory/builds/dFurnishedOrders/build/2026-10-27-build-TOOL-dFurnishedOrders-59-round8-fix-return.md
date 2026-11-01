**Serves:** research TOOL-dFurnishedOrders-59 TOOL-dFurnishedOrders-60

# Round-8 fix pass — dFurnishedOrders, its return

The return of the agent dispatched from `memory/builds/dFurnishedOrders/prompts/2026-10-27-prompt-TOOL-dFurnishedOrders-1-6-spec-writer.md`, run direct/a2c23fb9bed8e9ce8, extracted from its transcript by script.

All three findings (R1–R3) are fixed in units 59 and 60. Hygiene checks 2, 12 and 25 now pass in a throwaway clone, and before the fix check 25 failed on exactly the five items you named. I couldn't run `python tools/check-spec-tokens.py` because scratch-guard blocks it for my role, so the token-check acceptance is still yours to run on the real tree. Both specs stay `rev-1` with no §9 line, and nothing outside the spec folder changed.

**Unit 59** (`memory/builds/dFurnishedOrders/spec/2026-10-27-spec-TOOL-dFurnishedOrders-59.md`)
- **R1:** none of S1, S4 or S5 actually retires a name; each describes a fixture edit or a staged break. So I reworded them and added no Readers clause:
  - S1 "drops every row…" now says it "keeps only the rows `g` … for which `check_guard_trips("tools/roles", g)` is false".
  - S4 "removed from the probe" is now "taken out of the probe".
  - S5 "a one-way rule that also drops a file" now says "misses a file".
- **R2:** AC2 no longer spells the suite path in backticks. It now calls `check_selftest_guard_coverage` from a scratch copy of the govkit self-test module whose probe has unit 53 S1's `rstrip("/")` taken out. The suite stays on §7's existing `New arm:` line.

**Unit 60** (`memory/builds/dFurnishedOrders/spec/2026-10-27-spec-TOOL-dFurnishedOrders-60.md`)
- **R1:** neither item retires a name, so both are reworded:
  - S2 now says the case "withholds exactly one input … lacking only the checker".
  - S10 now says "Unit 58 AC19 reads parsed rows in place of its `git log -S` search".
- **R2:** AC18 had the only backticked suite path in a criterion. It now reads "a scratch copy of the govkit self-test module whose `check_selftest_guard_coverage` holds a planted `read_legs_for(` call". The suite's `New arm:` line in §7 is kept. AC15's `git grep … -- tools/govkit/selftest.py` stays as it is, because the checker counts a grep over a suite file as not a run.
- **R3:** AC22 now reads "a line, after its two-space indent, starts `govkit selftest <- tools/check-spec-tokens.py [`", which matches the format at `tools/check-spec-tokens.py:666`. I made the same change in S24, the item behind AC22, so the two read alike.
- I reflowed the edited lines to at most 105 characters.

**What I checked**
- **Hygiene checks:** I committed every spec of the folder in the clone, plus the staged round-8 review record. Without that record, check 2 reports the links to it as broken, which is an artefact of the clone. With it, no line names unit 59 or 60.
- **Check 9 fails** because the build index is out of date. That is the index you render at commit, not one of these findings.
- **Token-check spot-checks (by reading its source):**
  - Neither spec has `tools/govkit/selftest.py` in backticks in §6 any more. The remaining spellings sit in §2 S20 and Files touched, outside what the check grades. Those can show as `NEAR` only under `--list`, never on the plain run (`tools/check-spec-tokens.py:1732-1736`).
  - No `tokens\.py` spelling is left in either spec.
