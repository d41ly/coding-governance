**Serves:** journal TOOL-dSafePassage-41

# TOOL-dSafePassage-41 — acceptance ledger

The unit as built, at spec rev-5. `tools/check-spec-tokens.py` gains the `ac-order` join inside the
spec loop of `main`: a live spec whose filename date, read as `SPEC_DATE.search("/" + f)`, is on or
after `ac_order_cut` (the `AC_ORDER_KEY` value TOOL-dSafePassage-34 reads through
`read_cutoff_key`) has its `AC_LABEL` labels inside `extract_acceptance` read in order, and the first
label listed before a lower one is a hit. Its run line prints the graded count and the key on every
run, or `blank (arm off)`. The docstring names the join and what it does not see. The suite gains
three top-level arms and its floor moves 200 to 203. `memory/map/features/spec-tokens.md` names the
join beside the key. The pass starts from the first dispatch's patch, unchanged.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows) by a probe of the changed code. The AC1 fixture is the suite's own `scratch()`
function, extracted from `tools/check-spec-tokens.test.sh`, built at `%TEMP%/ao41`, with the
checker run four times. That is not the suite.

Owed at the close: the `New arm:` line's RED-first observation (the three
`TOOL-dSafePassage-41` arms of `tools/check-spec-tokens.test.sh`, red on a checker copy whose join
ignores the key, green restored), the floor of 203, AC2's line from the leg itself, and the §7 legs.

**Evidences:** TOOL-dSafePassage-41
- AC1 — `python tools/check-spec-tokens.py` over the scratch repo: with `SPEC_AC_ORDER_CUTOFF` set to `2026-09-02`, the spec's date, and `AC2` listed before `AC1`, it exited 1 with the `[ac-order]` hit `ac-order <- AC2` naming `2026-09-02-spec-TOOL-tOne-1.md` and `1 of 1 live spec(s) · ... 1 out of order`. With the key blank it exited 0 with `0 of 1 live spec(s) · SPEC_AC_ORDER_CUTOFF blank (arm off)`. With the key at `2026-09-03` it exited 0 with `0 of 1 live spec(s) · ... 0 out of order`. Red when, observed: a copy whose grading condition was patched to `if True:` exited 1 on all three cases, naming `AC2` with the key blank and with the key a day past the spec.
- AC2 — `python tools/check-spec-tokens.py` over the tree was refused to this role by scratch-guard as the leg `spec tokens (a spec's own names resolve)`. The stand-in was the predicate probe `ao41_pred.py`, which loads the checker module and applies the join's predicate (`LIVE`, `SPEC_DATE`, `read_cutoff_key(AC_ORDER_KEY)`, `AC_LABEL` inside `extract_acceptance`) over `git ls-files`. With this spec at `INPROGRESS` it printed `key '2026-10-23' · live 37 · graded 1 · out of order 0`. The `ac-order` line of the leg itself is owed to the close, where it may grade 0 because this spec is CLOSED, and that 0 is not coverage.
- AC3 — `git log --reverse --format=%H -S "ac-order" -- tools/check-spec-tokens.py` printed nothing before this pass's commit, so the first commit to carry the join is this unit's pass commit. In that commit the grading condition reads `if ac_order_cut and m and m.group(1) >= ac_order_cut:`, and `ac_order_cut = read_cutoff_key(root, AC_ORDER_KEY)` comes from TOOL-dSafePassage-34's commit, so `git show <that-commit>:tools/check-spec-tokens.py` carries `AC_ORDER_KEY`.
