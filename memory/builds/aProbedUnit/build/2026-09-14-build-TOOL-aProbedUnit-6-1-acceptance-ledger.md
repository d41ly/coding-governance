# TOOL-aProbedUnit-6 — acceptance ledger

**Serves:** journal TOOL-aProbedUnit-6

Every leg-shaped half below reads `observed at --close`: this pass ran no gate leg, no bar and no
suite whole, per the build README's rule five. Each pass half was observed by the grep or the single
arm the criterion names, run by the form the spec's section 4 gives: the driver suite's preamble
(`sed -n '1,/^# ---- REGION ONE/p'`) sourced by `bash -s` from `tools/unattended` so `HERE` resolves,
`slice_fn` sourced from region two, `bcsetup`, `slice_fn review_state`, then the arm's own `hit` or
`same` line, `TMPDIR` pointed at `%TEMP%/apu6` so the fixture lands under the sanctioned root. The
RED-first half is the same script with `SCRIPT` pointed at a FROZEN copy of the kit at HEAD
(`git archive HEAD tools/unattended tools/lib`, unpacked in the scratchpad): a first attempt froze the
driver file alone and every verb arm red on `the kit library is missing beside this script`, which
is an arm failing for the wrong reason, so it was discarded and the whole kit frozen instead. HEAD
for the base copies is 947d54fe, the pass's parent.

**Evidences:** TOOL-aProbedUnit-6
- AC1 — `run --status tRun` under the `NOCONF` conf, arm alone — OBSERVED: stderr carried `unattended: NOTE - this project declares no REVIEW_ROUNDS, so a spec-audit subject exits BOUNDED after the kit default of 1 round. Declare one in <conf> to change it.` on one line; the `hit` was silent at the tip and printed `FAIL missing` against the base kit.
- AC2 — `mkconf … "9"` then `run --status tRun` — OBSERVED: exit 2, stderr `REFUSING - REVIEW_ROUNDS is 9, above the runaway ceiling of 8, so the ceiling would fire first and the declared bound could never be reached.`; `mkconf … "0"` — exit 2, stderr `REFUSING - REVIEW_ROUNDS is declared as '0', which is not a positive integer of rounds.` on one line. Against the base kit both `hit`s printed `FAIL missing` and the driver exited 1 on the absent run-state instead, so both values were accepted there.
- AC3 — `slice_fn review_state` then the six sliced arms — OBSERVED: `'' 3 1` → `BOUNDED`, `'3' 2 2` → `BOUNDED`, `'' 3 8` → `CONVERGING`, `'2' 2 1` → `NON-CONVERGENT`, `'' 0 1` → `CONVERGED`, `'9 8 7 6 5 4 3' 2 8` → `CEILING`, every `same` silent at the tip; the seven existing two-argument arms silent against BOTH drivers; against the base driver the two `BOUNDED` arms printed `FAIL … expected [BOUNDED], got [CONVERGING]` and the four order arms held.
- AC4 — `bcopen`, `mkconf "true" "true" "2026-08-19" "3600" "" "1800" "1"`, then the B1 arms — OBSERVED: no `--disposition` printed `--review exits BOUNDED and requires --disposition` and `grep -c 'review · item B1'` printed `0`; with `--disposition promote` the echo carried `BOUNDED · disposition promote` and `the declared round bound of 1 is reached`, and the row `review · item B1 · reason verdict BLOCKED · blockers 3 · BOUNDED · disposition promote` counted `1`; a further B1 round printed the existing terminal-round refusal. Against the base kit the first printed `CONVERGING` and wrote a row (`expected [0], got [1]`), the promote call was refused, and the row count read `0`.
- AC5 — `crdrop`, then `--subject tRun --blockers 3 --disposition promote` and `--subject tRun --blockers 3` — OBSERVED: the first refused with `not a terminal exit`, the second printed `CONVERGING`; both silent against both drivers, which is the criterion — the closing review is unchanged.
- AC6 — `--subject B2 --blockers 3 --disposition fold` — OBSERVED: `BOUNDED · disposition fold` printed and the row carried it, count `1`; against the base kit `FAIL missing` and count `0`.
- AC7 — `grep -n 'CONVERGED\*|\*NON-CONVERGENT\*|\*CEILING\*|\*BOUNDED\*' tools/unattended/unattended.sh` — OBSERVED: one line, `3643`, inside the `diff-reviewed` term, its header saying the token is listed for parity and unreachable on the slug subject; `grep -c 'moves the stall earlier'` printed `0` at the tip where `git show HEAD:` printed `1`.
- AC8 — the two check-2 fixtures alone in the leg suite, `dispconf 2000-01-01` + `mkdisp` — OBSERVED: the `blockers 2 · BOUNDED` row with no disposition printed the `record NO disposition while this record is graded against DISPOSITION_CUTOFF` refusal, one `check 2` line; the same row with `· disposition promote` and the fixture's second unit (the `D_TWO` region in the leg suite) new in the region printed zero `check 2` lines. Against the base kit the first fixture printed zero `check 2` lines, the red-first observation. `grep -c 'CONVERGED|NON-CONVERGENT|CEILING|BOUNDED' tools/unattended/check-unattended.sh` printed `1`.
- AC9 — `grep -c "'BOUNDED'"` over template and render — OBSERVED: `1` and `1`; `grep -c -- '--disposition promote'` over both: `1` and `1`, where `git show HEAD:` prints `0`. The loop member alone from `tools/workflows` with the suite's preamble sourced and `returns BOUNDED 0` printed `ok   BOUNDED: hands out a roster` against the tip render; against `git show HEAD:tools/workflows/unattended-build.js` it printed `FAIL BOUNDED handed out no roster` with `THROW … "BOUNDED", which is not one of CONVERGING, CONVERGED, NON-CONVERGENT, CEILING`. The `workflow script syntax` and `review-protocol parity` legs — observed at --close.
- AC10 — `grep -c 'REVIEW_ROUNDS'` over `PROTOCOL.template.md`, `kit.toml`, `.unattended.conf`, `.unattended.conf.example` — OBSERVED: `1` each; `grep -c 'BOUNDED' VERBS.template.md` printed `3`; `grep -c 'declared round bound' SKILL.template.md` printed `1`; `grep -c 'one of four states' SKILL.template.md` printed `0`. `bash tools/unattended/adopt-unattended.sh` re-rendered the three; its `--check` mode is the `unattended skill wiring` leg and, with check 22 of the `unattended kit gate` leg — observed at --close.
- AC11 — `wc -c memory/guides/BUILD-METHOD.md` — OBSERVED: `26833` at the tip against `26846` from `git show HEAD:`, exactly 13 less; `grep -c 'exits BOUNDED'` printed `1` over template and render, `0` at HEAD for each; the render re-made by `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, whose three sibling renders came back byte-identical; `last-audit` re-stamped in the same commit. The `build-method size`, `kit/dogfood doc parity` and `kickoff-manifest ratchet` legs — observed at --close.
- AC12 — the 19 added arms run alone against the tip, 26 with the seven controls — OBSERVED: every `hit` and `same` silent, `st=0`; against the frozen base kit 12 of the 19 printed `FAIL` and `st=1`, the seven that held being the four sliced order arms, AC5's two slug-subject arms and the further-round refusal, as rev-5's AC12 now says — AMENDED, rev-5 with its section 9 line, because rev-4's "every verb arm prints FAIL" was contradicted by AC5's own criterion. `git diff tools/unattended/unattended.test.sh | grep -cE '^\+(hit|same|miss) '` printed `19` and the leg suite's `2`; `FLOOR_ASSERTIONS` 741 → 760 and `FLOOR_SHARD_2` 545 → 564 (`git show HEAD:… | grep '^FLOOR_'` read 675 SHADOWED, 741, 208, 545), the leg suite's 400 → 402 and 317 → 319. Whether the executed count meets the pins is the close's compensating run.

## What this ledger does not evidence

No merge-bar leg ran inside this pass — not `unattended kit gate`, `unattended skill wiring`, `harness
arms`, `review-protocol parity`, `workflow script syntax`, `kit/dogfood doc parity`, `build-method
size`, `kickoff-manifest ratchet`, `memory hygiene` or `spec tokens` — and no suite ran whole; each is
`--close`'s and each row above says so. `adopt-unattended.sh --check` was deliberately not run after
the render, because it IS the wiring leg; the render's own `installed`/`rendered` lines and the
AC10 greps over the renders are what this pass observed. The existing review-loop arms were not
re-run as a set: the seven two-argument sliced arms were re-run as controls and held against both
drivers, and every other review arm runs at `mkconf`'s new seventh default, the ceiling, which the
AC3 arm `'' 3 8` → `CONVERGING` shows is byte-for-byte the pre-bound behaviour.
