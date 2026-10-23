**Serves:** research TOOL-dFairHearing-1 TOOL-dFairHearing-17

# Re-pin brief — two specs pinned to clause hashes their own deviation records moved

`python tools/check-spec-tokens.py` reports two stale pins after the first spec commit `455442c67`:

- `TOOL-dFairHearing-1` pins `cl-dClosedLoop-0068@b4e6c04e`. Deviation 11 (`memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-1-deviation-11.md`) amends that clause, and the as-built view now hashes it `89c89732`.
- `TOOL-dFairHearing-17` pins `cl-dClosedLoop-0084@5c5896a3`. Deviation 171 (`memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-17-deviation-171.md`) amends it, and the view now hashes it `145be745`.

For each of the two specs:

- Set its `**Carries:**` line to the amended hash.
- Bump its status header to `rev-2`.
- Add a §9 line saying the pin follows the spec's own deviation record's `amends` row, and that nothing else changed.
- Read the clause's amended text in `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`, and confirm the spec still carries every word of it. Report any gap; do not fix it.

Change nothing else. Do not commit, do not stage, and do not run the build-index generator or any gate; the main loop runs them. Report each spec's new header line and §9 line.
