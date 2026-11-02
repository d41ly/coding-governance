# TOOL-dEasedEffort-1 — hand attribution of the close's seven red legs

**Serves:** journal TOOL-dEasedEffort-1

The close's flagged bar `unattended-1793576871074914266-1786` ran at the prepared merge `380196b73`
and read 7 of 144 legs red on a clean tree that did not move. Its attribution left `gates-green`
unmet: one leg OWN, one CONTENDED, four MIXED. Six legs were then run by hand at `529b98a4`, the tip
of `origin/main`, in a detached worktree with `GIT_GRAFT_FILE=/dev/null`, which is what the close's
bar inherits.

| Leg | Bar's label | Failing arms at `380196b73` | At `529b98a4` |
|---|---|---|---|
| `recall floor arms` | INHERITED, aged | not re-run | the bar's own run read byte-identical output |
| `spec-tokens self-test` | OWN, comparator `tools/roles/README.md` | 2 of 204, both the `measure_legs.py --selftest` parity pair | the same 2 |
| `pre-push self-test` | MIXED | `TOOL-aSparedSpawn-33 AC1` | the same arm |
| `measure-legs selftest` | MIXED | `AC15 the leg's own bar waited` | `AC15`, plus `AC6` and `AC7` |
| `govkit selftest` | MIXED | 7 failed arm names | the identical 7 names |
| `push-main self-test` | CONTENDED | none: 74 ok, then killed past its 580s ceiling and again on retry | none: 74 ok, the 580s ceiling fired and again on retry |
| `foreign-prefix parity` | MIXED | `policy fixtures`, `unattended gate selftest shard 1/8`, `measure-legs selftest` | `policy fixtures`, `unattended gate selftest shard 8/8`; `measure-legs selftest` is not graded there, being red in the baseline bar |

## Reading

No failing arm traces to this build's diff. Against `529b98a4` it touches no file under
`tools/unattended/`, `tools/policy/`, `tools/run-gates/` or `tools/govkit/`. The MIXED labels come
from a whole-output text comparison, since none of the four legs' rows declares a signature, so a
timing or a path in one line moves the label without moving an arm. The OWN label comes from the
comparator rule alone, which short-circuits before any run at R.

## What this does not establish

- `shard 1/8` was not run at `529b98a4`. The parity probe picks its shard from `HEAD` as an integer
  mod 8, 0 here and 7 there, so each end ran a different shard. The arm that failed, a helper defined
  inside a shard region, reads `tools/unattended/check-unattended.test.sh`, which this diff leaves
  byte-identical, so the same arm is expected there. That is an inference, and it stays one: the
  owner's standing instruction is not to run that suite by hand.
- The first hand run filtered its legs with `GATE_LEGS`, and nested bars inherit that. The `govkit`
  lines naming legs that were red after an install therefore differ by construction, and only its
  7 failed arm names are compared. `foreign-prefix parity` was re-run at `529b98a4` without the
  filter for the same reason.
- This is a comparison of failing arms, not the bar's verdict, and `gates-green` stays unmet.
