# Revision — dTrackedAtlas: TOOL-dTrackedAtlas-4's AC6 names a break that runs

**Serves:** research TOOL-dTrackedAtlas-4

## The prompt

> Unit 4's builder returned `diverged: true` before writing code: AC6's fixture appends `raise SystemExit(3)` to the generator, after its closing `sys.exit(main(sys.argv[1:]))`, so the line never runs and AC6 would read red against correct code.

## The brief

### Goal
Revise AC6 of `memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-4.md` so its planted landing makes the generation in the scratch checkout fail. The generator `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py` ends `if __name__ == "__main__":` then `sys.exit(main(sys.argv[1:]))`, so a line appended after it is unreachable; the builder measured a same-shaped scratch file exiting zero with the line appended.

### Items
1. Rewrite AC6's fixture so the planted break runs before `main` returns, for instance a `raise SystemExit(3)` inserted above the `if __name__` guard, or the guard's last line replaced. Say in AC6 what the page check answers on that tree and why the runner then regenerates and logs `failed`.
2. Re-read the other criteria for the same fault, a planted line that cannot execute, and fix any you find the same way.
3. The status flip to CLOSED is the main loop's, not the builder's: if any section of the spec says the pass commit flips it, say the main loop does.
4. Bump the rev and add one revision-log line naming this record and what moved; no other design change.

### Acceptance
`bash tools/unattended/unattended.sh --plan dTrackedAtlas --paths` grades unit 4 READY; `--check-specs dTrackedAtlas TOOL-dTrackedAtlas-4` prints no refusal; `check-memory-hygiene.sh --only 12 --spec <path>` and `check-spec-tokens.py --spec <path>` are clean; every new function name the spec declares still gets an OK line from the lexicon's `--suggest`.

### Gates
The spec-format, spec-token and naming-lexicon checks the role allows; no other gate.

### Non-goals
No design change beyond the acceptance fixtures; no product code; no commit and no index render, which the main loop does.
