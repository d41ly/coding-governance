# Acceptance ledger — TOOL-aCarriedStop-1

**Serves:** journal TOOL-aCarriedStop-1

Built against spec rev-2 in one pass commit. AC1 to AC7 are driver runs the builder made in the pass, on node a, in the spec's probe fixture, each from a fresh fixture. AC8 to AC11 are the criteria's own commands over the worktree. No suite, gate leg or bar ran in the pass. Owed to the main loop at the close: the five new suite arms' red-then-green runs, the legs of the spec's Gates section, and the third observation of AC11, the decision row, which the pass does not write because the dispatch refuses that shared record.

**Evidences:** TOOL-aCarriedStop-1
- AC1 — `run <pass>` — it exited 1 and printed the check 118 opening followed by the criterion's CONTINUE text whole, round 0, naming FIX-dFix-1 and FIX-dFix-2, and the dispatch-row grep printed 0.
- AC2 — `run --chain-verdict dFix` — the owner-stop call exited 0 and printed the recorded line at round 1; the index listed one record whose name ends `-build-FIX-dFix-1-chain-rounds.md`; its last line was the owner-stop row citing `<stop>`; and the verdict exited 0 with the criterion's line, byte for byte.
- AC3 — `run <pass>` — after the commit it exited 0, printed the dispatch line at round 1 with reason owner-stop and the cited record, and the dispatch-row grep printed 1.
- AC4 — `git ls-files '*-chain-rounds.md'` — each of the six calls exited 1 with the check 118 opening and the text beside it, the two flag cases ending `--subject` and `--finding`; after each the listing printed nothing and the build held no `build/` folder. Beyond the criterion, a fixture with no spec and no roster refused with the fourth value, naming dFix.
- AC5 — `run --chain-verdict dFix` — the audit round after the row printed a line holding `dFix · round 2 · `, the record held the round 2 subject row once, and the verdict printed the criterion's CONTINUE line, byte for byte.
- AC6 — `round 5 · STOP · reason owner-stop` — the first fixture read round 1 CONTINUE open and then round 2 STOP owner-stop; the second read round 4 HOLD ceiling, and after the row one line holding round 5 STOP owner-stop.
- AC7 — `run <pass>` — beside the review row on s2 and a committed owner-stop row it exited 1 and printed the check 118 opening followed by the criterion's text, ending `s2;`.
- AC8 — `grep -c 'chain round recorded' tools/unattended/unattended.sh` — the four counts printed 319, 1, 4 and 1, in the criterion's order. (PINNED, 2026-11-13)
- AC9 — `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` — it printed nothing after the adopter's re-render; the flag greps printed 2 and 1, the usage-header grep 1 and the record-tail grep 1.
- AC10 — `python tools/govkit/docs_leg.py --fingerprints` — it printed 0d0412b9 for the record-round row and 5fdc7c80 for the chain-verdict row, the page's anchor grep found each once, and the flag grep over the page printed 4. (DERIVED from the built header at the pass.)
- AC11 — `tr -d '\r' < .claude/skills/unattended/SKILL.md | wc -c` — it printed 10580, the figure on the Skill's row, and the comment above the row holds `by TOOL-aCarriedStop-1`. The decision-row grep printed 0 in the pass: the main loop adds that row after the pass and observes the count at the close. (DERIVED from the render at the pass.)
