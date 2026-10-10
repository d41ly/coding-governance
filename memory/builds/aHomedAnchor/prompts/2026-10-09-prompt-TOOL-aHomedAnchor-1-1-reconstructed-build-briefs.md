# Reconstructed build briefs — aHomedAnchor

**Serves:** journal TOOL-aHomedAnchor-1 TOOL-aHomedAnchor-2 TOOL-aHomedAnchor-3 TOOL-aHomedAnchor-4 TOOL-aHomedAnchor-5 TOOL-aHomedAnchor-6 TOOL-aHomedAnchor-7

node a · 2026-10-09 · RECONSTRUCTED after the fact

**This is a reconstruction, not a brief.** All seven units were built INLINE by the run's own main
loop, and `--brief` never ran for any of them, so no build commit carries a brief row and the
`brief-recorded` leg reds all seven. History is append-only, so no honest row can be added; the
seven waiver rows in `memory/project/brief-recorded-waiver.txt` point here, after the
`DEPL-aHalvedInstall-5` precedent. Nothing below was handed to a builder before its build commit.

What the builder worked from, unit by unit, is the unit's own spec under `spec/` at the build
commit, plus these instructions held in the run's context:

| Unit | Build commit | What the builder was working to |
|---|---|---|
| `TOOL-aHomedAnchor-1` | `59c9719a`, `026f5eec` | spec §2 S1 to S8; fast checks only, no suite; arms written, observed at VERIFYING |
| `TOOL-aHomedAnchor-2` | `40a976d9` | spec §2 S1 to S4; the reader probed by hand; the leg's full run left to the bar |
| `TOOL-aHomedAnchor-3` | `4c80fedd` | re-render with `adopt-unattended.sh`, confirm `--check` |
| `TOOL-aHomedAnchor-4` | `d3b545f6` | the template-size leg's shape in `.githooks/pre-commit`; a throwaway-repo probe |
| `TOOL-aHomedAnchor-5` | `87f19159` | the AUTH_PARAM arms' shape in the adopter suite |
| `TOOL-aHomedAnchor-6` | `2d5f232c` | the review's skeptic-sound fix per item, at the site it names |
| `TOOL-aHomedAnchor-7` | `dd043ee7`, `51518b16` | the same, for the leg's four items |

Standing instructions over every unit: the kit self-test suites are not run (the owner's prompt);
the spec is committed before its code; each pass commits with a `Pass:` trailer after a `--dispatch`
naming its write set.
