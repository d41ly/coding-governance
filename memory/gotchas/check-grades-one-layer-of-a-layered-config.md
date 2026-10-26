---
name: check-grades-one-layer-of-a-layered-config
description: an enforcement check reads one layer of a configuration its consumer layers, often through a resolver built to pick a write target, so a value in a layer it never reads runs past the check while the layer it grades is clean
kind: class
universal: false
---

# A check that grades one layer of a layered configuration

## Symptom

The consumer of a configuration applies several layers of it, each able to set the same key: a local
file over a project file over a user file, a flag over all three. A check meant to hold that key to a
bound reads one of them, or swaps one for another when a variable is set. Every case the check carries
plants its value in the layer it reads, so each one passes, and a value above the bound in a layer the
check skips is admitted.

The usual route in is reuse. A resolver already answers "which settings file", and it is built to
answer it for a WRITER: the one file a render should write. A check that asks the resolver which file
to read inherits that answer, and the question it needed answered was "what does the consumer apply",
which no single file answers.

## Where it bit

dGroundRules, the spec run's closing diff review, item H3, 2026-10-23
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`).
Rule 7 of `tools/hooks/agent-cap.js` read the settings file the way `settings_json` in
`tools/check-wiring.sh` resolves it: the file `GOV_SETTINGS_JSON` names, in the project file's place.
With the variable set, a value above the agent limit in `.claude/settings.json` was never compared
with the limit, and the case written for the variable planted no project file beside the declared one.
TOOL-dGroundRules-61 made rule 7 read every layer it can and bound each one that sets the key.

## The fix

- A check that reads configuration reads every layer its consumer applies, and bounds each layer that
  sets the key, unless the consumer's precedence is declared and verified; where it is not, grading
  one value by an assumed precedence is the same hole in the other order.
- A resolver built to locate a write target is never the reader of an enforcement check. Reuse the
  per-file read, never the choice of file.
- Each such check carries a case in which a higher-precedence or a declared layer violates while the
  layer it grades is clean, and one in which a declaration that names no file refuses rather than
  reading as a layer that sets nothing.
- The layers the check cannot read are named where its users read, so "the check passed" is never
  taken for "the consumer applies the bound".

Rule 7's instance is gated by the `policy fixtures` leg, through the `limit-settings-elsewhere`,
`limit-settings-elsewhere-project-over` and `limit-settings-declared-absent` cases of
`tools/policy/check_policy.py`, and by the rule-7 arms of `tools/hooks/agent-cap.test.sh`. The class
in general has no machine gate: no check can tell which layers an arbitrary consumer applies.
