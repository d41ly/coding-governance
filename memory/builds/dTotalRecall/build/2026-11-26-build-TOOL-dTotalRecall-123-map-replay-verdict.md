# the map loses its second replay on recall and searches

**Serves:** research TOOL-dTotalRecall-123
**Made-by:** owner
**Caused-by:** TOOL-dTotalRecall-123


**Verdict:** lose · recall, searches

The map's second losing test, spec 123 S6 and S7, run by the main loop on node a, 2026-11-26. Thirty harness calls of
`tools/workflows/tier2-review.js`, five per arm for each of the three audits, were scored by the `map-replay` instance
over the manifest beside this record. The recall term lost under the noise rule of spec 123, the searches term lost, and
the bytes term held. The first experiment's verdict, `2026-11-23-build-TOOL-dTotalRecall-17-map-replay-verdict`, stands
beside this one; no run of it is pooled here.

## The manifest

`2026-11-26-build-TOOL-dTotalRecall-123-map-replay-manifest.json`, its `known` and `arms` and both `dispatched` (15) as
the pass commit left them, its `candidates` and `map` written at this verdict commit. It is read by
`python tools/workflows/replay_scorer.py --experiment <it>`, which exits 0 and prints the lines quoted under the terms
below (DERIVED 2026-11-26). Its reports and transcripts sit outside the repository, as their absolute paths name them:
each report under its clone, each scored lens's transcript in this session's workflow transcript directory. The scored
lenses are spec 17's: the spec audit's coherence and reuse, the library review's three and the debt-folds review's five.

The map is the first experiment's, derived again in a short-path clone at `01dcdd1ae` by the same command: 30748 bytes,
blob `d38a3a8f2ed8` (DERIVED 2026-11-25, `wc -c` and `git hash-object`), the same blob, so the same map. Each with-map
arm's `context` is the audit's sentence, then the map under one heading line; the without arm's is the sentence alone.
In every with-map run the map was found whole in each finder's prompt once the harness's per-line indent is folded
(DERIVED 2026-11-26, `mapchk.py` over each run's transcripts).

## The clones

Every clone was made by the README's replay recipe and per-arm block (`scratchpad/mkclones.sh`), its status read empty
when made, and all 30 `run.log` lines name the one orchestrating head `f3b88d294` (DERIVED 2026-11-26, `uniq -c` over
the log). After each call its status lists one untracked path, the arm's own report (DERIVED, `git status --porcelain
--untracked-files=all` per clone). Within an audit the calls alternate arms, without first.

| Clone | Audit | Arm | HEAD before the call | Run | Confirmed rows |
|---|---|---|---|---|---|
| f1n4 | systems-retrofit | without | `338be3211` (placement on `36fc6d572`) | `wf_87fed594-cf5` | 35 |
| f1m3 | systems-retrofit | with | `338be3211` (placement on `36fc6d572`) | `wf_69c47050-f1b` | 32 |
| f1n5 | systems-retrofit | without | `338be3211` (placement on `36fc6d572`) | `wf_27dbe093-f79` | 37 |
| f1m4 | systems-retrofit | with | `338be3211` (placement on `36fc6d572`) | `wf_8c4f6ddd-3e5` | 40 |
| f1n6 | systems-retrofit | without | `338be3211` (placement on `36fc6d572`) | `wf_de87148f-eb8` | 28 |
| f1m5 | systems-retrofit | with | `338be3211` (placement on `36fc6d572`) | `wf_7ad35cdd-71a` | 39 |
| f1n7 | systems-retrofit | without | `338be3211` (placement on `36fc6d572`) | `wf_3cef961d-a17` | 40 |
| f1m6 | systems-retrofit | with | `338be3211` (placement on `36fc6d572`) | `wf_bdecb87e-989` | 42 |
| f1n8 | systems-retrofit | without | `338be3211` (placement on `36fc6d572`) | `wf_9305a09b-59c` | 31 |
| f1m7 | systems-retrofit | with | `338be3211` (placement on `36fc6d572`) | `wf_4b892a7b-deb` | 35 |
| f2n3 | library | without | `aa9639d98` | `wf_060b4a87-f94` | 9 |
| f2m3 | library | with | `aa9639d98` | `wf_5f1b07ec-2ea` | 7 |
| f2n4 | library | without | `aa9639d98` | `wf_f5705b29-ad7` | 8 |
| f2m4 | library | with | `aa9639d98` | `wf_bf544ebc-aaf` | 8 |
| f2n5 | library | without | `aa9639d98` | `wf_8cdaf0a8-b8f` | 8 |
| f2m5 | library | with | `aa9639d98` | `wf_7564c556-822` | 7 |
| f2n6 | library | without | `aa9639d98` | `wf_b520af36-07a` | 12 |
| f2m6 | library | with | `aa9639d98` | `wf_c69ea283-ab3` | 10 |
| f2n7 | library | without | `aa9639d98` | `wf_afac5f3e-823` | 9 |
| f2m7 | library | with | `aa9639d98` | `wf_afbda4cf-f75` | 6 |
| f3n3 | debt-folds | without | `cdcea2c9b` | `wf_e76c6170-94a` | 9 |
| f3m3 | debt-folds | with | `cdcea2c9b` | `wf_f4386942-c99` | 6 |
| f3n4 | debt-folds | without | `cdcea2c9b` | `wf_971eedce-ec8` | 10 |
| f3m4 | debt-folds | with | `cdcea2c9b` | `wf_c75e2291-b9e` | 7 |
| f3n5 | debt-folds | without | `cdcea2c9b` | `wf_132ff504-a89` | 9 |
| f3m5 | debt-folds | with | `cdcea2c9b` | `wf_a3caa7f7-bf8` | 7 |
| f3n6 | debt-folds | without | `cdcea2c9b` | `wf_3c221a5a-d35` | 11 |
| f3m6 | debt-folds | with | `cdcea2c9b` | `wf_4a090f31-70e` | 9 |
| f3n7 | debt-folds | without | `cdcea2c9b` | `wf_8262b674-f92` | 4 |
| f3m7 | debt-folds | with | `cdcea2c9b` | `wf_48919174-44c` | 8 |

The confirmed-rows column is each report's confirmed appendix rows as `parse_candidates` reads them, all lenses
(DERIVED 2026-11-26). Audit 1's clones are one placement commit, `338be3211`, on `36fc6d572`, as the first experiment's
Departures describe.

**The one stopped call.** The first launch of `f1m4` (`wf_ac69e656-1b0`) carried a with-map `context` whose map was cut
short at its tail. The main loop stopped it once one probe agent had spawned and before any finder ran; no report was
written and the clone's status stayed empty (DERIVED 2026-11-26). The call was launched again in the same clean clone
with the whole map (`wf_8c4f6ddd-3e5`), the run above. It is a launch fault, not a re-run for a figure: no figure
existed. Spec 123's "The runs" asks a failed call to be re-run in a fresh clone under the next `<n>`; that departure is
listed below.

## The terms

The instance printed (DERIVED 2026-11-26):

- `known r1: 37 item(s) over 45 finding(s)` · `known r2: 14 item(s) over 19 finding(s)` · `known r3: 16 item(s) over 18 finding(s)`
- recall without: r1 20, 22, 23, 21 and 26 of 37 · r2 3, 4, 4, 6 and 3 of 14 · r3 3, 5, 1, 3 and 1 of 16
- recall with: r1 15, 15, 28, 25 and 27 of 37 · r2 5, 6, 0, 2 and 1 of 14 · r3 6, 3, 0, 2 and 3 of 16
- `term recall: known items found with 27.6 · without 29 · rise -1.4 · noise 7.0993 at 5 run(s) per arm · loses below 12.0993`
- `term searches: median existence searches with 38 over 50 lens run(s) · without 34 over 50 · fall -4 · loses below 1`
- `term bytes: median bytes before the first act with 13957 · without 13957 · rise 0 · map 30748 byte(s) · loses above 30748`
- `verdict lose recall, searches`

The map did not raise the known items found: the with arm found 27.6 on the summed audit means against 29 without, a
rise of -1.4 under a noise of 7.0993 at five runs per arm (DERIVED). The first experiment's rise was -0.5 at two runs
(PINNED, its record), so both experiments put the map's effect on recall at or below zero. Unlike the first experiment,
the searches term also lost here: the with arm's median existence searches were 38 against 34 without (DERIVED), where
the first experiment read 32 against 42. The searches fall is therefore not stable across the two experiments, and the
map's one favourable figure from the first does not reproduce.

The bytes term is armed here: both arms' median bytes before the first act read 13957 (DERIVED), not the first
experiment's 0, so the term was measured and held. Audit 1's recall spread is the widest: the with arm ranged 15 to 28
of 37 and the without arm 20 to 26 (DERIVED), so a single run decides little on that audit.

## Departures

- **Audit 1's subjects are placed under dFairHearing,** exactly as the first experiment's record states, one placement
  commit for every audit-1 clone.
- **The calls reproduce each audit's kind, intensity, subjects or range and preset,** not its `specs`, checklist or
  `byDesign`, as in the first experiment.
- **One stopped launch was relaunched in its own clean clone,** not a fresh clone under the next `<n>`: `f1m4`, above.
  The clone held no write from the stopped call, so the relaunch ran on the state every other clone ran on.

## Routing

The `lose` branch of spec 123 §4 "The routes". Units TOOL-dTotalRecall-14, TOOL-dTotalRecall-15 and TOOL-dTotalRecall-26
are to be retired as `WONTDO`, and their clauses cl-dClosedLoop-0225, cl-dClosedLoop-0226 and cl-dClosedLoop-0237
re-homed, as the accept clause of ask TOOL-dTotalRecall-111 says. This run does neither: the three units stay
`DEFERRED` and the ask stays open until the owner's turn. The three asks spec 17 S7 filed, TOOL-dBoundRoles-77,
TOOL-dWellOiledMachine-961 and TOOL-dCalibratedLens-57, stand, and nothing is filed again.
