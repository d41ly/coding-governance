# TOOL-aFrugalTurnstile-4 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-4

No merge bar and no self-test suite ran in this pass. AC1 to AC10 ran one scratch fixture script
under a short temp root: the three-leg scratch the spec names, with `pa` guarded on `ga/`, `pb`
guarded on `gb/` and red until fixed, and `pu` unguarded. Every run set `GATE_TURNSTILE=0` and a
scratch `GATE_TURNSTILE_DIR`. AC11 to AC13 ran a second script, shaped like the hook suite's H49
fixture: a scratch clone with a hook copy and a runner copy pushing to a bare remote. Each case ran
first against the runner and hook at `bef97330` and then against the working files. Base results:
AC1 wrote five-field rows; AC2 reused `pa` but stamped nothing; AC3, AC4 and AC5 each reused `pa`
under `GATE_REUSE=lineage`; AC7 stamped nothing; AC8's leg saw `lineage` and the header had no
`reuse` key; AC10 logged 3 ledger greps, and with the base moved it logged 8 `hash-object --stdin`
calls against 5 for the unset run; AC11's second push ran all three legs with no reuse clause. All
of those are RED. Three criteria guard behaviour the base already had, so their base runs were
green too. AC6: the base never stamps after a reuse. AC9: both readers already took extra trailing
fields. AC12 and AC13: the base hook already scrubbed an inherited `GATE_REUSE` and exported no mode.
A seventh hook case pushed H49's ORIGINAL shape, a row earned WITH the full flag, through the working
hook, and the red leg landed by reuse. That is why the H49 arm is re-staged. On the working files
all fourteen criteria were GREEN. The new suite arms were also run as scratch slices outside the
tree: each was a minimal prologue plus that block, and the slices were deleted before the map
regenerated. The evidence slice passed 12 of 12 assertions in 6 m 16 s, and the hook slice 5 of 5.
The close still owes every §7 leg: the whole evidence suite, including its nine-field AC6 line, the
whole hook suite, including the re-staged H49 `GATE_REUSE` arm, the canary, the run-log arm, the
profiler selftest, wiring, shell hygiene and memory hygiene. The evidence suite grows by about six
minutes, so its declared ceiling should be read at VERIFYING.

**Evidences:** TOOL-aFrugalTurnstile-4
- AC1 — `gate-ledger.tsv` — `awk -F'\t' 'NF != 9'` printed nothing; every row's field 6 equalled the header's `run_id`, field 7 read `1`, field 8 the header's `manifest_blob` and field 9 `git rev-parse HEAD`; with an untracked file present every field 7 was empty.
- AC2 — `GATE reuse pa` — the lineage run after the fix printed it with `GATE ok    pb` and `GATE ok    pu`, and `gate-full-green` carried `reused` 1.
- AC3 — `GATE reuse pa` — the lineage run over rows a run without the full flag earned printed no `GATE reuse` line; the `GATE_REUSE=1` control on the restored ledger printed `GATE reuse pa`.
- AC4 — `GATE reuse pa` — after a fourth leg joined the manifest, the lineage run printed no `GATE reuse` line and ran `pd`; the `GATE_REUSE=1` control on the restored ledger printed `GATE reuse pa`.
- AC5 — `GATE reuse pa` — over rows a sibling of HEAD earned, the lineage run printed no `GATE reuse` line; the `GATE_REUSE=1` control on the restored ledger printed `GATE reuse pa`.
- AC6 — `gate-full-green` — over lineage-qualifying rows, `GATE_REUSE=1` reused all three legs and `gate-full-green`, deleted before the run, was absent afterwards.
- AC7 — `impure` — with `pa` declared `impure`, the lineage run printed `GATE ok    pa`, `GATE reuse pb` and `GATE reuse pu`, and `gate-full-green` carried `reused` 2.
- AC8 — `unset` — the leg writing `${GATE_REUSE-unset}` wrote `unset` under `GATE_REUSE=lineage`, and the run's `header` carried `reuse` `lineage`.
- AC9 — `dispatch` — with `pb` given the largest seconds in a nine-field ledger, the header `dispatch` read `1 2 0`, and `profile_bar.read_timings` printed all three durations, `pb` 99.0.
- AC10 — `hash-object --stdin` — the lineage run logged no `grep` naming `gate-ledger.tsv`, out of 6 `grep` lines logged; with `refs/remotes/origin/main` moved it logged 5 calls, the same as the unset run, and the unmoved-base control logged 6.
- AC11 — `— reuse: lineage` — the red push was refused with `gate-red`; the fix push's FULL line ended `— reuse: lineage`, printed `GATE reuse pa`, landed with the remote at the local tip, and `gate-full-green` carried `reused` 1.
- AC12 — `reuse: lineage` — the `GOV_GATE_CMD_TEST` push's FULL line carried no `reuse: lineage`; the declared non-runner bar wrote `unset`; with `GATE_REUSE=1` inherited, `not honoured from the environment by this bar` named `GATE_REUSE` and the FULL line still ended `— reuse: lineage`.
- AC13 — `gate-red` — the row earned without the full flag was reused by the direct `GATE_REUSE=1` control, and the push with `GATE_REUSE=1` and the leg red was refused with `gate-red`.
- AC14 — `grep -n "never sets it" tools/run-gates/README.md` — `grep -n "WHAT LINEAGE REUSE DOES NOT CHECK"` printed one line over the README and one over the runner; `grep -n "never sets it" tools/run-gates/README.md` printed nothing, where the base README held one.
