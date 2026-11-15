**Serves:** research TOOL-aMeasuredDrag-1

# Skeptic verdicts — every batch

One line per finding: verdict · corrected cost · already addressed · duplicates.

## Batch adopters (skeptic 2)

- adopters-1 PLAUSIBLE · root cause of 2/3/4/6, no own weekly figure; c83ef509..HEAD = 899 kit commits, +145k lines · none · —
- adopters-2 CONFIRMED · guarded on .githooks/, so it runs only on forced-full: ~3.5/wk incms, ~10/wk nicocares; ~1374 slot-s per run (the 5069 s incms sample is load-inflated) · gov 894952cb6 (2026-10-09) fixed it; adopters lack it · adopters-4
- adopters-3 CONFIRMED · incms 22/43 landings over the lag bound (~3.5/wk), nicocares 59/118 (~10/wk); likely the largest adopter item per week · gov 89c20a6a7 + a01f7ed90 (first-parent lag); adopters lack it · —
- adopters-4 CONFIRMED · overstated per push: 10-09 is one loaded sample; nicocares 10-20 ~880 slot-s; still runs on every push including memory-only · partly: gov 3203e2ac4 holds the unattended kit gate; pass-order, brief-recorded, hygiene, marker contracts, drift-audit, playbook validity still unguarded in gov · adopters-2, adopters-10
- adopters-5 PLAUSIBLE · commit-mix observation, counts hold (incms 829/1576 governance-only, nicocares 881/1509) · none · adopters-6
- adopters-6 CONFIRMED · ~85 min/wk incms, ~65 nicocares; render re-timed 8.9 s / 4.5 s; incms also runs check-memory-local.sh · gov a55426071 (staged render skip) — adopters lack it · —
- adopters-7 PLAUSIBLE · not quantifiable; subject counts lexicon 48/25, red 68/74 · none (gov's lexicon guard has the same shape) · —
- adopters-8 PLAUSIBLE · ~4 small records commits/wk in nicocares (23 re-stamps since 10-01) · none · —
- adopters-9 CONFIRMED · 78-91 KB, ~20-23k tokens per agent start · gov template already 8,970 B (9760fb746); adopter CLAUDE.md needs a hand trim · —
- adopters-10 PLAUSIBLE · overstated: 14 unguarded legs, small wall share; premise wrong (adopters edit settings, hooks, guides) · none · adopters-4
- adopters-11 PLAUSIBLE · ~0.35 s per Bash call quiet (finder 2x high) · — · sessionhooks-3, sessionhooks-6
- adopters-12 REFUTED · incms `scripts/gate.sh (lines 334-350)` already scopes memory-only landings; the python suites do not run · incms ARCH-aYieldedFork-2 · adopters-4

## Batch gate (skeptic 1) — 14 CONFIRMED, 12 PLAUSIBLE, 1 REFUTED; host 6-10x busier than in the find phase (10 spawns 294-393 ms)

- githooks-1 CONFIRMED · ~6.8 h/wk (2268 of 2543 memory commits owe a render; 54 s under load) · none (TOOL-aTrimmedWait-3/-4 write only changed bytes but do not skip the check) · githooks-3/-7, legs-3 PINNED 2026-11-15
- githooks-2 CONFIRMED · ~2.1-2.8 h/wk (15 s, "graded 0") · none · legs-3 PINNED 2026-11-15
- githooks-3 PLAUSIBLE · ~7.9 h/wk but ~95% is githooks-1/-2/-5; not additive · none · githooks-1/-2/-5
- githooks-4 PLAUSIBLE · ~4.5-5 h/wk; 0 of 40 lander pushes covered; cited cause conflicts with gov's declared `LANDER_MODE="in-place"` (tools/unattended/unattended.sh@eb567029:750-754), real cause of 0 covered not established · partly (in-place mode) · bar-4
- githooks-5 PLAUSIBLE · 1.77 s loaded, ~5-15 min/wk (overstated) · none · githooks-3
- githooks-6 CONFIRMED · ~13 runner-h/wk (32 push runs in 13 days, mean 46 min; understated) · none · bar-11
- githooks-7 PLAUSIBLE · incms ~105 memory commits/wk; nicocares hooks not found at the cited path · none · githooks-1
- legs-1 CONFIRMED · ~219 leg-s/bar, ~1.6 leg-h/wk + its timeouts; an armed join that measures nothing can exit 2 · none · legs-9, bar-7
- legs-2 CONFIRMED · ~0.8 leg-h/wk saveable · none · legs-9
- legs-3 PLAUSIBLE · duplicate coverage read ~15 s per hygiene run, 10-20 min/wk · none · githooks-2 PINNED 2026-11-15
- legs-4 CONFIRMED · ~2 leg-h/wk duplicated + 19 timeouts · none · bar-6
- legs-5 PLAUSIBLE · saved only when the branch diff touches neither tools/ nor skills/ · TOOL-aTimedTurnstile-2 (open ask) · legs-9, bar-5, bar-10
- legs-6 CONFIRMED · ~0.5 leg-h/wk of wasted first attempts · none · bar-10, legs-5
- legs-7 PLAUSIBLE · the narrow guard is a correctness gap; widening costs more · none · bar-3
- legs-8 REFUTED · held off every automatic bar since 3203e2ac4 (TOOL-aShelvedLeg-1, 2026-11-10); last ran 2026-11-10
- legs-9 PLAUSIBLE · overstated: record-reading legs must run on records commits; only marker contracts, spawn budget, tags (~650 s) are guard candidates · TOOL-aTimedTurnstile-2 · legs-1/-2/-5, bar-5 PINNED 2026-11-15
- bar-1 CONFIRMED · credible 7-9 h/wk; 92% of 7040 leg rows ran beside foreign work · none · bar-2, bar-6
- bar-2 CONFIRMED · ≥4 h/wk serial wait · none · bar-1
- bar-3 CONFIRMED · matrix longest leg in 13 of 20 recent runs; leg-sum/wall 1.9-5.9 · none · legs-7
- bar-4 CONFIRMED · 201 bars / ~40 landings; pass bars are short so "5 bars" overstates wall · none · githooks-4
- bar-5 PLAUSIBLE · 4 of 201 bars reused any leg; saving likely overstated · TOOL-aTimedTurnstile-2 · legs-5/-9, bar-10
- bar-6 CONFIRMED · ~2.8 leg-h/wk of first attempts; some legs sit near their ceilings even alone · none · legs-4/-6, bar-1/-7
- bar-7 PLAUSIBLE · routed commits 510→760→3540, flips back and forth · none · legs-1, bar-6
- bar-8 CONFIRMED · 117 of 201 red; first red at 0.26 of wall; saving overstated (median 2 failed legs) · none · —
- bar-9 CONFIRMED · ~1.5 h/wk (regen 118 s) · none · — PINNED 2026-11-15
- bar-10 PLAUSIBLE · lower than claimed (guarded legs skip); re-filing to selftests = never runs (0 GATE_SELFTESTS bars since 2026-10-15) · none · legs-5/-6, bar-5
- bar-11 CONFIRMED · 45 of 45 CI runs failed 11-01..11-14, mean 46 min, ~18 runner-h/wk with no signal; spawn budget `check-wiring measured 47 · ceiling 45` · open asks TOOL-aNimbleMend-26, TOOL-aSparedSpawn-26 · githooks-6

Cross-cutting: zero GATE_SELFTESTS bars since 2026-10-15, so "hold it in selftests" means "never runs".

## Batch hooks (skeptic 3) — 9 CONFIRMED, 10 PLAUSIBLE, 2 REFUTED; hooks matching one event run in parallel, so costs are max, not sum

- sessionhooks-1 CONFIRMED · ~2.2-3.4 h/wk recoverable: 5,492 of 5,653 bound Stops had background tasks and still paid a 6.3 s `--liveness` first; leases >1 per session do occur · none · spawns-5
- sessionhooks-2 PLAUSIBLE · ~14 min/wk + ~107k chars; the 86% share is unverifiable (no block record) · partly TOOL-aTrimmedWait-7 (519bc24db caches handoff parses) · —
- sessionhooks-3 CONFIRMED · ~44 min/wk quiet (hook 221 ms throttled vs 124 ms gate-guard) · none · spawns-1
- sessionhooks-4 CONFIRMED · the two groups run in parallel: max(card 25.4 s, wiring 17.5 s) ≈ 13 min/wk + tail · partly ask TOOL-aBriskPreflight-8 · spawns-6
- sessionhooks-5 PLAUSIBLE · ~18 refusals/wk; per-refusal cost rests on this review's 339 s · none · — PINNED 2026-11-15
- sessionhooks-6 REFUTED · gate-guard reads gate-legs.json only when a run is live (`tools/unattended/gate-guard.js@e58690cf:810-821`); the two PreToolUse hooks already run in parallel, so a dispatcher saves CPU, not latency · — · spawns-1
- sessionhooks-7 REFUTED · `tools/roles/handoff.py@26689d0b:122, :1104-1108` already render a role's `gates`; the scratchpad path already reaches sessions; role-gate false refusals reworked by TOOL-aTrimmedWait-6/-9 · partly addressed · —
- spawns-1 CONFIRMED · the git spawn alone ~50 min/wk quiet (rest is the hook floor) · none · sessionhooks-3/-6
- spawns-2 PLAUSIBLE · well below 8.8 h/wk (full render forced only on add/delete; share not measured) · partly TOOL-aTrimmedWait-2/-3/-4/-8 · spawns-9/-11
- spawns-3 PLAUSIBLE · not measured; leg is held since 3203e2ac4 (see legs-8) · none · —
- spawns-4 CONFIRMED · ~1k spawns, 30-80 s per run for the cutoff alone; `sort -C` at :368 · none · legs-2
- spawns-5 PLAUSIBLE · overstated: the remote resolver runs once per call, not 6x; `--liveness` 6.3 s quiet; batched stat saves ~0.75 s/call, ~1 h/wk · none · sessionhooks-1
- spawns-6 CONFIRMED · counted inside sessionhooks-4 · partly TOOL-aBriskPreflight-8 · sessionhooks-4
- spawns-7 PLAUSIBLE · pre-push sets GATE_FULL so the push bar still pays; saving only on scoped bars · none · legs-5
- spawns-8 CONFIRMED · small; ~2 min per check-unattended.test.sh run · none · —
- spawns-9 CONFIRMED · ~4-6 min/wk from deduplicating staged diffs (resolve_python 3x, not 2x) · none · spawns-2
- spawns-10 PLAUSIBLE · remedy check; WSL seam covers only the held tier · seam exists · —
- spawns-11 CONFIRMED · the four-way corpus re-load in hygiene is real · partly TOOL-aTrimmedWait-2/-3 · spawns-2

## Batch records (skeptic 5) — 13 CONFIRMED, 12 PLAUSIBLE, 0 REFUTED; several costs overstated 2-4x

- records-1 CONFIRMED · ~6.6 h/wk of render (2272 of 2547 memory commits force it; 46 s); staged-builds-only render misses cross-build roster moves · none (TOOL-aTrimmedWait-3 adds a render) · githooks-1/2, records-4/7/8 PINNED 2026-11-15
- records-2 CONFIRMED · ~1.6-2.9 h/wk (spec-commit double render only; finder 7.9 overstated) · rewrite fixed on speedups b2c96fea3 (TOOL-aTrimmedWait-4) · records-1
- records-3 CONFIRMED · ~2 h/wk, but `--with-verdicts` alone recovers little: `read_carries_coverage` must be memoised per process · none · —
- records-4 PLAUSIBLE · 3.1 records commits per product commit; ~8 h/wk of commit wall (not 13) · none · records-1, derived-2/3
- records-5 PLAUSIBLE · table causes ~17% of spec revisions (not 39%) · none (deliberate, TOOL-dFramedEntrypoint-6) · records-4
- records-6 CONFIRMED · ~350 s/run of pickaxes, ~1.2 h/wk; memo per row buys nothing — one `git log -p` pass is the fix · none · legs-1 PINNED 2026-11-15
- records-7 CONFIRMED · ~3 h/wk leg time (10,777 leg-s / 13 runs) · none · records-1/8, derived-5
- records-8 CONFIRMED · grouping 3.0 s not 8.2 s; ~45 min/wk · none · records-1/7
- records-9 PLAUSIBLE · premise wrong: handoffs are read after spawn (`tools/roles/handoff.py@26689d0b:1043-1046`, `tools/memory-tree/deviation_join.py@c793df78:558`, check_roles R15) · none · derived-2
- derived-1 CONFIRMED · built_s 32.5 s (not 96); ~35 min/wk · none · —
- derived-2 CONFIRMED · 223 packet re-render commits since 10-15, declining (60/106/34/23 per week); ~0.6-0.9 h/wk now · none · records-4/9
- derived-3 PLAUSIBLE · ~7-10 re-stamps/wk, 15-30 min/wk · none · records-4
- derived-4 PLAUSIBLE · stragglers 6.5 s · ask TOOL-aBriskPreflight-8 · sessionhooks-4, spawns-6
- derived-5 CONFIRMED · ~6 min/wk, zero-risk memo · none · records-7
- derived-6 PLAUSIBLE · adding `*.sh` likely a net slowdown; value is left-shift · none · —
- derived-7 CONFIRMED · ~22 min/wk (6.5 s per lookup, ~225/wk) · none · —
- derived-8 PLAUSIBLE · leg median ~176 s; `--check` history write is deliberate (TOOL-aMendedFleet-48) · none · records-7 PINNED 2026-11-15
- suites-1 CONFIRMED · 16,356 leg-s in 12 of 28 runs (guarded, not every bar) · none · bar-3, legs-7, suites-2
- suites-2 PLAUSIBLE · tracked files 4,627 → 12,622 in a month; fixture cost not re-measured · none · suites-1
- suites-3 PLAUSIBLE · not verified; `GATE_SELFTESTS=changed` already exists, a new flag would re-implement it · existing mode · suites-7
- suites-4 CONFIRMED · ~14k leg-s/wk, concurrent · none · legs-5/-6, bar-10
- suites-5 PLAUSIBLE · govkit dedupes legs by name (`tools/govkit/govkit.py@37f075e4:4268-4275`); adopter numbers unverified here · none · adopters-2
- suites-6 PLAUSIBLE · `run_scoped` does have callers (:6852, ~17); held suite · none · —
- suites-7 PLAUSIBLE · paid daily in remote CI (`remote-ci.yml:40-41, :155-257`), not locally; "cannot be paid" overstated · TOOL-dDerivedDocket-32 · suites-3

## Batch process (skeptic 4) — 8 CONFIRMED, 17 PLAUSIBLE, 3 REFUTED; time concentrates in one large build (dOrderedCharter)

- pipeline-1 CONFIRMED · ~8-15 h/wk (not 20-30); dOrderedCharter is 18.9 of 25.9 dispatch-h and 7.1 of 8.2 audit-h; walk 71 s over 89 closed keys · none · pipeline-3/-4 PINNED 2026-11-15
- pipeline-2 PLAUSIBLE · <1 h/wk now · largely fixed by 4fed38fe1 (TOOL-aBriskDeclaration-1) · —
- pipeline-3 CONFIRMED · ~5 h/wk (65% of run commits carry `Pass: none`) · none · pipeline-1
- pipeline-4 PLAUSIBLE · the --audit hours are pipeline-1's walk; turn tokens real but unmeasured; `gov-resume-tick` registered but Disabled since 2026-10-21 · none · pipeline-1/-5
- pipeline-5 CONFIRMED · ~5.6 h/wk of driver CPU, decision-preserving fix (90% of 5,815 stops had background tasks) · none · sessionhooks-1, spawns-5 PINNED 2026-11-15
- pipeline-6 PLAUSIBLE · 19 closes / 15.6 h in 7 days; red-leg-only re-close conflicts with the GATE_REUSE scrub's purpose · none · contention-5, bar-8
- pipeline-7 PLAUSIBLE · unmeasured; README declared in 32/43 (aNimbleMend) and 95/127 (dOrderedCharter) dispatches · none · —
- pipeline-8 PLAUSIBLE · 52 of 80 pass runs RED (writing practice 28, install-prefix 24, runbook parity 23); "a whole new pass per red" not shown · none · ceremony-7
- pipeline-9 REFUTED · `bash -n` parses the driver in 65 ms; the ~1 s start-up is top-level git/awk/mktemp calls (:670, :782, :857-868) · — · — PINNED 2026-11-15
- pipeline-10 REFUTED · `covered` exists (`.githooks/pre-push:2197-2204`); it never fires because the close commits its record after its own bar, moving the tree · — · githooks-4, bar-4, contention-6
- ceremony-1 PLAUSIBLE · spec 498k vs product 133k lines since 10-15 (holds); token split not re-measured · none · ceremony-2/-9
- ceremony-2 PLAUSIBLE · understated: 1,582 Tier-2 vs 77 Tier-1 since 10-15 (95%); kickoff rule says a kit's CONTRACT, not any kit change · none · ceremony-6 PINNED 2026-11-15
- ceremony-3 PLAUSIBLE · overstated 2x: 367 turns, 146M context tokens (mostly cache) · none · ceremony-11
- ceremony-4 PLAUSIBLE · 81% of commits non-product (holds); folding status flips saves few commits; scratch-guard reads the spec from the working tree, so the separate INPROGRESS commit is method, not hook · none · ceremony-8/-9
- ceremony-5 CONFIRMED · per instance verified (441/470-line repair specs, ~1h19m) · none (owner ruling, BUILD-METHOD.md:144, 2026-10-04) · —
- ceremony-6 PLAUSIBLE · small today (Tier-1 rare); closing-review-recorded is overridable; `light` intensity exists · partly · ceremony-2/-9
- ceremony-7 CONFIRMED · writing practice is the top pass-leg red (28 of 52) · none · pipeline-8
- ceremony-8 PLAUSIBLE · 31 prompt records / 2,646 lines (finder overstated) · none · ceremony-4/-9 PINNED 2026-11-15
- ceremony-9 CONFIRMED · 5h57m, 12 commits, includes a 52-min owner ruling and a reconcile — the floor is not all ceremony · none · ceremony-1/-4/-6/-8 PINNED 2026-11-15
- ceremony-10 PLAUSIBLE · low · none · —
- ceremony-11 PLAUSIBLE · small (~2.4M cached tokens per long session) · none (auto-memory claim of a fix is wrong) · sessionhooks-2
- contention-1 PLAUSIBLE · 7.2 h/wk of queue confirmed, but serial was measured faster than concurrent (`tools/run-gates/run-gates.sh@bfc3ad49:1588-1592`); expired events are 10-09..10-11 · none · bar-1/-2
- contention-2 PLAUSIBLE · census over-counts foreign; 10-17 h unverified · none · bar-1
- contention-3 PLAUSIBLE · cleanup scans 5.3 s warm (not 61.4 s); co-timeouts real · none · legs-4, contention-7
- contention-4 PLAUSIBLE · 48 retries in week 46 confirmed; 11 ceiling commits since 10-20 (not 35) · none · bar-6/-7
- contention-5 CONFIRMED · week 46: 35 of 61 bars RED, 20.5 of 32.0 bar-hours; pass-legs gate catches less (tags, instruction edits, routed commits are not pass legs) · none · bar-8, pipeline-6
- contention-6 PLAUSIBLE · 27 of 39 push bars scoped, ~1,476 s · partly · pipeline-10 PINNED 2026-11-15
- contention-7 PLAUSIBLE · unmeasured · none · contention-3
