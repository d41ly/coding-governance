**Serves:** journal TOOL-dWitnessedBar-26

# Brief — dWitnessedBar: unit 26's gate line, re-grounded before its build

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. The run's first `--dispatch` of TOOL-dWitnessedBar-26 refused at check
49, because the spec-token checker reds on this spec now that it is live.

## The brief

### Goal

Revise the spec of TOOL-dWitnessedBar-26 in place, as a rev bump with one revision-log line, so `--dispatch` admits it
and a builder can build it as written over HEAD.

### Items

1. `python tools/check-spec-tokens.py --spec memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-26.md`
   reds four `[guards]` hits: §4 Files touched names `tools/policy/check_policy.py`, which trips the guards of the legs
   `scratch-guard self-test` and `routed-commits selftest`; `tools/memory-tree/corpus_ids.py`, which trips
   `playbook render selftest`; and `tools/govkit/govkit.py`, which trips `policy fixtures`. None of the four is on the
   §7 leg line. Add each to that line, spelled as `tools/gate-legs.json` names it, or, where a path is not one this
   unit writes at HEAD, correct Files touched instead and say why.
2. While in the file, settle any claim HEAD has moved since the spec's base `cdfbd1cf`: dGroundRules landed
   `tools/lib/resolve_bash.py` with its `resolve_bash_py` block (so S1 is §8 F1's in-place rewrite), copies of that
   block sit in `tools/policy/check_policy.py`, `tools/loop/loop_witness.py` and `tools/playbook/render_playbook.py`,
   and govkit's resolver lives in `tools/govkit/upgrade_steps.py`. Where a copy the S6 query would now find is not in
   Files touched, add it and the legs its guard names. Change nothing else.

### Acceptance

`check-spec-tokens.py --spec <this spec>` exits 0, and the status header carries the next rev with its revision-log line.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No change to Scope, Design or Acceptance beyond what items 1 and 2 force. No other spec. No product code.

### Limitations

The status header stays `INPROGRESS`. The write grant is this spec file alone.

### Reuse

Not applicable: a re-ground of an existing spec.
