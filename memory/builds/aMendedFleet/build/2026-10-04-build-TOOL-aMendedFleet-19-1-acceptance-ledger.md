# TOOL-aMendedFleet-19 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-19

**Evidences:** TOOL-aMendedFleet-19
- AC1 — `python tools/memory-tree/gen_build_index.py --doctor zDoctorProbe` in a `git clone --local` under `%TEMP%/dr19`, with the README holding only a title line and added — exit 1, three failing-rule lines: `hygiene check 9`, `slot-contract registry` and `slot-contract slot`, then the summary naming both graders; 73 s wall
- AC2 — `gen_build_index.py --doctor aBatchedMinors` on the live tree — exit 0, no failing-rule line, the summary names `hygiene and slot-contract` and an elsewhere count of 1, derived at that run; 70 s wall
- AC3 — the AC1 clone with the probe README untracked — exit 2, `1 untracked file(s) and none tracked` with the `git add memory/builds/zDoctorProbe` remedy and `Nothing graded.`
- AC4 — `--doctor` with no slug, with `x_y`, with `memory/builds/aBatchedMinors` and with `zNoSuchFolder` — each exit 2 and each prints `usage: gen_build_index.py --doctor <slug>`
- AC5 — `--selftest` — hygiene outcomes of exit 2 and of exit 1 with no key each read `2 True True`: exit 2, a `hygiene did not answer` line, and the slot-contract registry finding beside it. RED on a staged break trusting `answered` alone: both arms failed
- AC6 — `--selftest` — four keys, zA's README, a zA id, zAB's README and a zAB id, attribute the first two to zA and count 2 elsewhere. RED on a staged break dropping both slug delimiters, then restored and green
- AC7 — `grep -n -- "--doctor" tools/memory-tree/README.md` — the Print modes paragraph names `--doctor`, the `hygiene` and `slot-contract` graders, its cost of one full hygiene run and the tracked-file precondition

## Owed at the close

- `memory/map/generated/symbols.json` — regenerated in this pass by `gen_map.py --write`; the
  codebase-map coverage and freshness legs are the close's.
- The lexicon leg grades the six new definitions; `lexicon.py --suggest --as py.function` answered
  OK for each, and the leg itself is the close's.
- `build-index selftest` ran here as the direct check, green; the bar's other section 7 legs are the
  close's.
