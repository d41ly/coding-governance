# TOOL-aFrugalTurnstile-15 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-15

Direct checks ran in a scratch fixture extended from TOOL-aFrugalTurnstile-7's: a bare remote with a
hand-staged `refs/gov/bar-red`, planted `gate-bar-green` records and a stub wrapper bar, pushed through
the hook at the previous commit (ebbc83b7) and then through the edit. RED first: at ebbc83b7, AC1 printed
the cleared line and scoped from the scoped record's own sha, and AC2 printed the cleared line and was
covered. GREEN: the edit decided FULL with no cleared line in both, and AC3 cleared and scoped on both
hooks. The reshaped TOOL-aFrugalTurnstile-7 AC11 arm was observed too: a red before the full green
stays covered, a red at the green's own sha forces FULL. AC4 is a grep, `0` before and `1` after. The
new `.githooks/pre-push.test.sh` arms (AC1-AC3) and the reshaped AC11 arm were written, not run; the
close's bar owes the `pre-push self-test` leg.

**Evidences:** TOOL-aFrugalTurnstile-15
- AC1 — `FULL gate` — the edit decided FULL naming the red at X and the full green B, bar ran with `GATE_FULL=1`, no `cleared` line; ebbc83b7 printed `cleared` and scoped
- AC2 — `FULL gate` — with the scoped record covering the pushed tree, the edit decided FULL and ran the bar; ebbc83b7 printed `cleared` and was covered
- AC3 — `cleared` — with the record's base a full green strictly after X, both hooks printed the `cleared` line and scoped, the edit naming that base and ebbc83b7 the scoped record
- AC4 — `grep -c 'rev D8' memory/builds/aFrugalTurnstile/build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md` — printed `1` on the edit and `0` at ebbc83b7
