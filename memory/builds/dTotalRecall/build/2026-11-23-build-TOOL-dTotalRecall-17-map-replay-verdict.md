# the map loses its replay on recall

**Serves:** research TOOL-dTotalRecall-17
**Made-by:** owner
**Caused-by:** TOOL-dTotalRecall-17


**Verdict:** lose · recall

The map's losing test of spec 17 S4 to S6, run by the main loop on node d, 2026-11-23. Twelve harness calls of
`tools/workflows/tier2-review.js`, two per arm for each of the three audits, were scored by the `map-replay`
instance over the manifest beside this record. The recall term lost; the searches and bytes terms held. Under §8 F5
the build run holds units 14 and 15 unbuilt, and S7 routes the loss to three builds as asks.

## The manifest

`2026-11-23-build-TOOL-dTotalRecall-17-map-replay-manifest.json`, read by
`python tools/workflows/replay_scorer.py --experiment <it>`, which exits 0 and prints the lines quoted under the
terms below. Its transcripts and reports sit outside the repository: each report under its clone, each lens
transcript in the session's workflow transcript directory, as their absolute paths in the manifest name them.

The map is `2026-10-17-build-PLAY-dClosedLoop-1-map.py` run unedited in a clone at `01dcdd1ae`, with
`--unfold leg,conf-key,population,marker,kit` and `--out` written outside the clone: 30748 bytes (DERIVED
2026-11-23, `wc -c`), blob `d38a3a8f2ed8` (DERIVED, `git hash-object`). The design inventory's "checks" have no
registry namespace in the instrument at that commit, so the unfolds are the five it does register. The with-map
arm's `context` is the audit's sentence, then the map under one heading line; the without arm's is the sentence alone.

## The clones

Every clone was made by the README's replay recipe and per-arm block (`scratchpad/u17/mkclone.sh`), its status read
empty before its call, and each `run.log` line names the orchestrating head `9e3b88829`. After each call its status
lists one untracked path, the arm's own report.

| Clone | Audit | Arm | HEAD before the call | Run | Confirmed |
|---|---|---|---|---|---|
| f1n2 | systems-retrofit | without | `b2cd50818` (placement on `36fc6d572`) | `wf_4f12da86-3e1` | 41 |
| f1m1 | systems-retrofit | with | `da2ef801b` (placement on `36fc6d572`) | `wf_c6b9df2f-61b` | 34 |
| f1n3 | systems-retrofit | without | `3b1a14d2b` (placement on `36fc6d572`) | `wf_5e840fdd-b0b` | 42 |
| f1m2 | systems-retrofit | with | `2b2331ef8` (placement on `36fc6d572`) | `wf_101cec82-45f` | 45 |
| f2n1 | library | without | `aa9639d98` | `wf_dd3b57cc-2e6` | 12 |
| f2m1 | library | with | `aa9639d98` | `wf_5cea36db-931` | 14 |
| f2n2 | library | without | `aa9639d98` | `wf_b2b3824f-97b` | 14 |
| f2m2 | library | with | `aa9639d98` | `wf_ff8f5a7f-154` | 8 |
| f3n1 | debt-folds | without | `cdcea2c9b` | `wf_896ed966-1af` | 12 |
| f3m1 | debt-folds | with | `cdcea2c9b` | `wf_ef3ddab2-588` | 11 |
| f3n2 | debt-folds | without | `cdcea2c9b` | `wf_9a5b1901-b11` | 7 |
| f3m2 | debt-folds | with | `cdcea2c9b` | `wf_c3b2daac-5a3` | 12 |

The confirmed column is each run's own report count (DERIVED 2026-11-23 from each harness return). Clone f1n1 was
made at `36fc6d572` without a placement and was refused before any agent spawned (see Departures), so audit 1's
without-map runs are f1n2 and f1n3. In every with-map run the map context was found whole in each scored lens's
prompt, once the harness's per-line indent is folded (DERIVED 2026-11-23 over the lens transcripts).

## The terms

The instance printed (DERIVED 2026-11-23):

- `known r1: 37 item(s) over 45 finding(s)` · `known r2: 14 item(s) over 19 finding(s)` · `known r3: 16 item(s) over 18 finding(s)`
- recall without: r1 18 and 29 of 37 · r2 3 and 8 of 14 · r3 7 and 7 of 16
- recall with: r1 28 and 20 of 37 · r2 10 and 5 of 14 · r3 5 and 3 of 16
- `term recall: known items found with 35.5 · without 36 · rise -0.5 · twin difference 18 · loses below 23`
- `term searches: median existence searches with 32 over 20 lens run(s) · without 42 over 20 · fall 10 · loses below 1`
- `term bytes: median bytes before the first act with 0 · without 0 · rise 0 · map 30748 byte(s) · loses above 30748`
- `verdict lose recall`

The map lowered the lenses' existence searches (median 42 to 32, DERIVED) without raising the known items they found.
The twin difference (18, DERIVED) is large against the arms' gap: run-to-run variance swamps any map effect at two
runs per arm.

The bytes term reads 0 in every one of the 40 scored lens runs (DERIVED 2026-11-23, 20 per arm): each lens's first
tool call is a `Bash` call that runlog classes `other` and that is no existence search, so the first act precedes
any result. The term cannot lose as the instrument measures it; it decided nothing here, since recall lost alone.

## Departures

- **Audit 1's subjects are placed under dFairHearing.** The opt-in hook (`tools/workflows/spec-audit-optin.js`)
  refuses a spec audit whose build README declares `spec-audit:` under `authorized-by: prompt`, which dClosedLoop's
  README at `36fc6d572` does. Each audit-1 clone is therefore the README's placement on `36fc6d572` of
  `memory/builds/dFairHearing/README.md` as it stands at `3708a705` (owner-landed `spec-audit: 2026-10-21`) and of the
  two reviewed blobs under `memory/builds/dFairHearing/replay/<their own path>`, with `reviewDir`
  `memory/builds/dFairHearing/reviews`: the route the README's "A replayed spec audit passes the opt-in pack"
  paragraph gives. Both arms carry the same placement, so the one variable stands; `check_same_file` matches the
  placed paths to the known set by their suffix.
- **The calls reproduce each audit's kind, intensity, subjects or range and preset, not its `specs`, checklist or
  `byDesign`.** The records state those inputs only as counts, so neither arm is handed them and the checklist is
  left to the harness to acquire on the diff reviews. The `context` is one sentence per audit, the same in both arms
  but for the map.

## Routing

S7's three asks are filed through `gov_record.py new ask`, each naming TOOL-dTotalRecall-17 and the losing term,
with this record as its pointer: one in each of dBoundRoles, dWellOiledMachine and dCalibratedLens.
