# TOOL-aMeasuredDrag-11 — acceptance ledger

**Serves:** journal TOOL-aMeasuredDrag-11

No merge bar, no self-test suite and no bar over a fixture ran in this pass. The pass started at
7c0a9bc9c, whose `tools/lib/resolve-python.sh` is the base `aebbb4a72` blob. Each probe below ran
from the worktree root in Git Bash as a script under the session scratchpad: `ac2.sh`, `ac3.sh`,
`ac6.sh` and `ac8.sh`, with the base block written there by `git show aebbb4a72:tools/lib/resolve-python.sh`.
The copies were re-synced by one scripted pass, `sync.py` in the same scratchpad, which replaced the
text between the two resolver markers of each file `git grep` names with the canonical block.

**Evidences:** TOOL-aMeasuredDrag-11
- AC1 — `/no/such/py` — the spec's AC1 command over the built block printed `/no/such/py`, wrote
  0 bytes to stderr and exited 0 (PINNED at 7c0a9bc9c).
- AC2 — `cmp` — `ac2.sh` ran the five variants (a 9009 `python3` stub prepended to `PATH`;
  `GOV_PYTHON` set to that stub; a caller override `resolve_python "$2"`; a `3.14` version line; a
  three-line memo), each with the memo unset and then set; `cmp` found stdout, stderr and the exit
  status equal in all five, and no set run printed `/no/such/py`.
- AC3 — `GATE_RESOLVED_PY` — `ac3.sh` ran the base block and the built block, each with
  `GATE_RESOLVED_PY` unset and then set to a memo naming the base run's launcher at its probed
  version 3.15: all four runs printed the same launcher, the same empty stderr and exit 0.
- AC4 — `python tools/lib/python_floor.py check` — the `sed -n` marker range of each of the 80 files PINNED 2026-11-15
  the S2 `git grep` names (PINNED at 7c0a9bc9c) compared with the canonical's by `cmp`: 0 differ.
  `python tools/lib/python_floor.py check` exited 0. The re-sync added the same 12 lines to each PINNED 2026-11-15
  file and changed no other line (PINNED at 7c0a9bc9c).
- AC5 — `PYBIN` — the spec's `grep -nE` over `tools/run-gates/run-gates.sh` prints four lines, in
  the order unset, `PYBIN`, digest, export.
- AC6 — `ENV_CLEARED` — `ac6.sh` sourced the `ENV_DROPPED_KNOBS` line and its loop from
  `.githooks/pre-push` with `GATE_RESOLVED_PY=x` exported: it read unset afterwards and
  `ENV_CLEARED` read ` GATE_RESOLVED_PY`; `grep -n '^ENV_DROPPED_KNOBS=' .githooks/pre-push` names it.
- AC7 — `git grep -n GATE_RESOLVED_PY -- help/python-floor.md` — prints the paragraph saying that
  inside a bar the resolver first takes the runner's own resolution, and under which three keys.
- AC8 — `/usr/bin/true` — `ac8.sh`, two rounds back to back, ten resolutions each over the built
  block (PINNED at 7c0a9bc9c):
  - round 1: memo unset 5.818 s, memo set 1.976 s, beside 0.650 s for ten `/usr/bin/true` and
    0.714 s for ten `bash -c true` (PINNED at 7c0a9bc9c).
  - round 2: memo unset 5.499 s, memo set 1.754 s, beside 0.429 s for ten `/usr/bin/true` and
    0.975 s for ten `bash -c true` (PINNED at 7c0a9bc9c).
  - the set loop is cheaper by 3.842 s and 3.745 s, about 375 ms per resolution, which is the spawn
    of ten probes (PINNED at 7c0a9bc9c). The spec's before loop is 2.342 s (PINNED at
    `aebbb4a72`), so this machine ran slower when sampled; the unset loop here is that same path.

**Owed to the close (the main loop, after every unit is terminal):**
- New arm `tools/lib/resolve-python.test.sh` (e2), covering AC1 and AC2: RED on a block copy with the
  memo rung deleted (the hit arm) and on one whose key compare drops `PATH` (the shadowed-PATH
  arm), GREEN once restored. Not run here.
- New arm `tools/run-gates/run-gates.test.sh` 1m, covering AC5: a scratch bar with an inherited
  sentinel memo and one leg recording the memo it sees and the launcher it resolves; RED with the
  runner's `unset GATE_RESOLVED_PY` deleted, GREEN once restored. Not run here.
- The gates in spec §7: `python resolver (behaviour + inline parity + idiom ban)`, `pre-push
  self-test` (its H49 knob-class arm now reads `GATE_RESOLVED_PY` in the runner's inline block, and
  S4 classifies it), `run-gates canary`, `measure-legs selftest`, `memory hygiene` and `spec tokens
  (a spec's own names resolve)`. `bash -n` over every edited script stands in for none of them.
