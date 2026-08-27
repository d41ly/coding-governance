---
slug: aGroundedOrientation
node: a
opened: 2026-08-27
streams: tooling
roster: TOOL
ids: TOOL-aGroundedOrientation-1 TOOL-aGroundedOrientation-2 TOOL-aGroundedOrientation-3
authorized-by: prompt
---

# aGroundedOrientation — the prompt path runs its orientation probes before the roster it writes is comparable

## The problem this build exists to solve
The unattended prompt path orients at step 1 and writes the build folder — including the ROSTER, the
set of units the whole run is then measured against — at step 3. The probes that would inform that
decomposition live in the kickoff engine's Step 4, and the engine is invoked at step 6, two steps
after the roster is committed and pushed. Step 1 points at that engine in the manner form, "in the
`/session-kickoff` manner — steps 0 to 4", which describes a posture rather than instructing four
commands. So the most consequential decision a prompt-mode run makes is available to be made with no
probe having run, and under a `published` anchor a roster corrected afterwards costs a commit and a
push. The probes cost seconds.

## Expected improvements
- The reuse probe's seams and recall's prior records reach the roster while the roster is still free.
- A unit a prior decision already settled is found before it is specced, not after it is pushed.
- The gap between "in the manner of" and "run these" stops being the reader's to close.
- The class is left-shifted: a check holds the probe step ahead of the build-folder write.

## Detriments if this is not built
- Every prompt-mode run decides its unit set blind and pays a re-push to correct it.
- The three probes this repo ships stay reachable only through a hop the run makes after the
  decision they inform, which is indistinguishable from not shipping them for that decision.
- The kickoff engine keeps carrying an orientation contract that one of its two callers reaches late.

## Build-level rules
- **The probe LIST is not restated.** The kickoff engine's Step 4 owns which probes exist; this path
  adds WHEN. `two-answers-to-one-question` is a selected bug class for exactly these files, and a
  second spelling here would be it.
- **The lexicon kit is REFUSED for orientation, and the refusal is the measurement.** Two independent
  reasons, either sufficient. It has no input at orientation: `--suggest` needs an identifier not yet
  written and `--brief` needs a path in an armed language. And measured on this corpus, `.lexicon.conf`
  declares `md::dark` and `sh::dark`, so `--brief` over the unattended kit and the kickoff engine —
  every file this build touches — returns `COVERAGE: dark`. A clause there would be a probe that
  cannot move, which the charter bans by name. The capability is already reachable at the moment it
  has an input: the lexicon Skill is wired and its description triggers on naming a function.
- **The kickoff engine is not edited.** It is an M11 carrier, and it sits 207 bytes under its
  18432-byte gate. The delta this build owns is timing, and timing belongs to the caller.
- **`gotchas`, `memory-recall` and the map reuse probe were already named** in that Step 4. Three
  quarters of the reported gap is a reachability problem, not an absence, and the record says so
  rather than claiming four fixes.
- **The hygiene guard is unit 3 by OWNER RULING, 2026-08-27, and is built FIRST.** The run found the
  defect while trying to commit this build folder, parked it as outside the goal, and the owner
  overrode that with "fix hygiene first, then the rest". It is sequenced ahead of the other two
  because every later commit touching `memory/**` pays the difference: 963 s against 54 s, measured.
  The id is 3 and the order is 1 — ids are labels, not ranks (template §2).

## Parked decisions

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aGroundedOrientation-3` | 1 | check 23 of the memory hygiene gate gets the `--staged` guard its four siblings carry, taking the pre-commit leg from 963 s to 54 s |
| 2 | `TOOL-aGroundedOrientation-1` | 1 | the prompt path's step 1 runs the orientation probes before step 3 writes the roster, pointing at Step 4 for which they are |
| 3 | `TOOL-aGroundedOrientation-2` | 1 | a check arm ordering the probe step ahead of the build-folder write inside the prompt section, with a vacuity guard |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 1 unit(s) · node a · opened 2026-08-27 · streams tooling
ids TOOL-aGroundedOrientation-1 TOOL-aGroundedOrientation-2 TOOL-aGroundedOrientation-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aGroundedOrientation-3 — check 23 gets the `--staged` guard its four siblings carry](spec/2026-08-27-spec-TOOL-aGroundedOrientation-3.md) | 1 | 1 | INPROGRESS | rev-1 | 2026-08-27 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: TOOL-aGroundedOrientation-3.

Ids no `spec-audit` record has ever named: TOOL-aGroundedOrientation-3.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aGroundedOrientation-3` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
