# TOOL-aFrugalTurnstile-11 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-11

No merge bar and no self-test suite ran in this pass. AC1 to AC6 ran one scratch fixture script,
extended from TOOL-aFrugalTurnstile-2's, under a short temp root: a bare remote, a work clone whose
hooks dir holds a copy of the hook, a tracked wrapper bar over a stand-in runner that appends to a
marker file, and the lander marker, with `GATE_TURNSTILE_DIR` pointed at a scratch dir. Each case ran
the hook at HEAD 587b006f7 first (base bef97330 has no bar records at all), then the working hook. At
HEAD, AC1 left one `gate-bar-green` holding `kind scoped` and no scoped slot, AC2 found no
`gate-bar-green.scoped.shared`, AC3's third push read `FULL gate` naming its base as
`no full green this push can adopt`, AC4 was not covered and ran the bar, AC5 scoped from the runner stamp at F, and AC6 named no
record file: all RED. On the working hook all six were GREEN. AC6 also ran a staged break, the tie
compare `-lt` changed to `-le`, which named `gate-bar-green` instead. AC7 is a grep, `0` at HEAD.
The new arms in `.githooks/pre-push.test.sh` for AC1 to AC6 are written and not run; the close owes
every §7 leg, the pre-push self-test with those arms among them.

**Evidences:** TOOL-aFrugalTurnstile-11
- AC1 — `gate-bar-green.scoped` — after a FULL then a scoped wrapper-bar push, `gate-bar-green` held `kind full` at the first push's sha and `gate-bar-green.scoped` held `kind scoped` with that sha as its base.
- AC2 — `gate-bar-green.scoped.shared` — the scoped push from a linked worktree left the common dir's copy byte-identical to the worktree's scoped record, by `cmp`.
- AC3 — `scoped gate` — the third push from the same git dir read `scoped gate`, adopting the scoped record counted from its full base, where HEAD read `FULL gate`.
- AC4 — `gate-bar-green.scoped` — a planted scoped record only in the scoped slot covered the push of its tree, the marker staying at 0 with `no bar runs`.
- AC5 — `scoped bar green` — the line read `scoped bar green` at M `counted from its base` F and the bar ran with `GATE_BASE` M, where HEAD scoped from F.
- AC6 — `gate-full-green` — with a runner stamp and a full bar record at one sha the line read `full green` from `this git dir's gate-full-green`; the `-le` break named `gate-bar-green`.
- AC7 — `NEAREST ADOPTABLE GREEN WINS` — `grep -c` over the working hook printed `1`, and `0` over HEAD's.
