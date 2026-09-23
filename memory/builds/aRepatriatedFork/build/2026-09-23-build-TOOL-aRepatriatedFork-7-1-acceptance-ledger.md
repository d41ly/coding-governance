# TOOL-aRepatriatedFork-7 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-7

One unit pass under the mandate. It ran no merge bar and no self-test suite. Every criterion below
was observed by a direct run: the hook piped one payload, the new arms sliced out of
`tools/hooks/agent-cap.test.sh` with that suite's own prologue, the S10 byte comparator extracted
from the same file, the renderer in its render mode, and the version gate. No adopter tree was read
or written: the lowered-cap install is a fixture.

## The fixtures

- **Base bytes**: `tools/hooks/agent-cap.js` as a7c78ad2 wrote it (identical to this build's BASE),
  copied to the scratchpad. Every new arm ran against it first and redded: 13 of 34, the four nested
  forms a7c78ad2 admits at exit 0 and every conf arm that asserts a lowering or a refusal.
- **Checkout fixture**: a bare `.git` directory with the call standing in a subdirectory, and
  `.agent-cap.conf` written per arm.
- **Lowered install**: a `git clone --local --shared` of this worktree under `%TEMP%` carrying the
  unit's files, with `FANOUT_CAP=4` committed in `.agent-cap.conf`, then `--render`.

**Evidences:** TOOL-aRepatriatedFork-7
- AC1 — `tools/hooks/agent-cap.js` — the section 4 nested payload exited 2 naming the verify-stage rule; the a7c78ad2 copy exited 0
- AC2 — `tools/hooks/agent-cap.js` — all ten nesting-matrix fixtures, five nested and five flat, exited 2 with `spawns one agent per item`; a7c78ad2 admitted four of the five nested forms
- AC3 — `bodies-compared 3 drifted 0` — the S10 comparator from `tools/hooks/agent-cap.test.sh` printed exactly that against `d65da7ab`, exit 0
- AC4 — `FANOUT_CAP=4` — a cap-5 harness exited 2 naming `above the 4-agent cap` and `.agent-cap.conf`; the same harness at 4 exited 0; with no conf both exited 0
- AC5 — `FANOUT_CAP=4` — direct `Agent` spawns 1 to 4 exited 0 and the fifth exited 2 with `4 of 4 claimed`; with no conf the sixth was the first denied
- AC6 — `FANOUT_CAP=6` — 6, 0, `four` and an empty value each exited 2 with `.agent-cap.conf declares FANOUT_CAP`, and 6 denied a direct spawn too
- AC7 — `tools/workflows/check-verifier-fanout.sh` — in the lowered install it printed `clean — 6 workflow script(s) obey the ≤4-verifier rule`, exit 0
- AC8 — `FANOUT_CAP=4` — the render wrote 4 at every section 4 site of all four harnesses and the verifier gate judged them clean; restoring the cap-5 `tier2-review.js` there exited 1 naming it
- AC9 — `bash tools/check-kit-versions.sh` — exit `0` at agent-cap 1.19 and drift-audit 1.12; with the scratch-guard marker reverted to 1.18 it exited 1 naming `tools/hooks/scratch-guard.js`, and with `drift-audit-state.js` reverted to 1.11 it exited 1 naming it
