**Serves:** research TOOL-dBoundRoles-65 TOOL-dBoundRoles-66

# Round-7 fix pass — dBoundRoles, its return

The return of the agent dispatched from `memory/builds/dBoundRoles/prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-9-spec-writer.md`, run direct/af2802e59e8ac2b45, extracted from its transcript by script.

I fixed the suite-path reds in four criteria of `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-66.md`. The spec stays `rev-1` and I changed no other file. I couldn't confirm the seven reds are gone: the guard hook won't let my role run `python tools/check-spec-tokens.py`, so you need to re-run it in the main session.

Criteria changed:
- **AC4** — `tools/roles/spawn-guard.test.sh` now reads "the spawn-guard suite unit 25 adds (its path in S2 and Files touched)". It still has the probe count the unit-50 arm's assertions against the `(TOOL-dBoundRoles-50)` term.
- **AC11** — `tools/roles/spawn-guard.test.sh` now reads "the spawn-guard suite unit 25 adds". It still has the probe read the first comment line above `FLOOR_ASSERTIONS`.
- **AC13** — `tools/roles/adopt-roles.test.sh` now reads "the roles adopter suite (its path in S1 and Files touched)". It still has the probe read the comment block above `FLOOR_ASSERTIONS`.
- **AC15** — "spec 62's `New arm:` line on `tools/roles/spawn-guard.test.sh`" now reads "spec 62's `New arm:` line on the spawn-guard suite unit 25 adds".

What I checked instead:
- I copied the tool's own bar pattern into a probe and ran it over every backticked token in §6: nothing matches.
- No `.test.sh` path is left in §6 except `scratch-guard.test.sh:1310-1320` in AC14. That is a line citation, which the pattern skips, and it was not one of the reported reds.
- Both full suite paths still appear in §2 (S1 and S2), §4 Evidence (the adopter suite) and Files touched (both suites).
- No §6 line is over 110 characters, and the memory hygiene gate exits 0.

The brief asks to keep each suite on a `New arm:` line in §7, but this spec never had one. Its §7 says no arm moves here, and spec 64's two `New arm:` lines re-observe both suites. I added none, because a new line would change the design beyond fixing the seven reds.

I committed nothing, and I did not run the build-index generator because my edits change nothing it reads.
