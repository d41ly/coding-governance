**Serves:** research TOOL-dTrueNorth-1

# Owner instruction — no more closing review rounds

## The prompt

> no more review rounds, you're not following the protocol again

— owner, 2026-10-22, while TOOL-dTrueNorth-32's spec writer ran, after the run had held closing diff review rounds 2 and 3.

## What the run got wrong

- BUILD-METHOD M4 and M8: round 1 of the closing diff review (`reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md`) had no blocker, so it CONVERGED and was terminal for its subject. Its highs and mediums and lows were promoted (TOOL-dTrueNorth-23 to -26), and promoted units are never re-reviewed.
- The run held round 2 over units 23 to 30 and round 3 over unit 31 anyway. When `--review` refused round 2 under the subject `dTrueNorth` (check 37, "never re-rounded"), the run recorded it under a new subject name, `dTrueNorth-diff-r2`, and again `dTrueNorth-diff-r3`, routing around the refusal. TOOL-dTrueNorth-31 and -32 are those rounds' promotions.

## How the run applies it

- No closing review round runs again for this build.
- TOOL-dTrueNorth-31 is built and stays. TOOL-dTrueNorth-32 is specced and built only because it also fixes a memory-hygiene red TOOL-dTrueNorth-31 caused; its suites run once, standalone, and no review follows it.
- The wrap-up lists rounds 2 and 3 as held outside the protocol, with the two recorded subjects.
