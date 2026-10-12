---
name: test-oracle-read-from-a-historical-sha
description: a test compares its subject with a copy read out of git at a literal sha, so every later legitimate edit of the subject reds it and the fix is always "move the sha"
kind: class
---

# A test oracle read from a historical sha rots on the next legitimate edit

## Symptom

An arm proves "this change altered nothing it should not" by running the subject as it stood at a
literal commit, `git show <sha>:<path>`, and comparing outputs byte for byte. It is green the day it
lands. The next unit that edits the same prompt or output on purpose reds it, although nothing is
wrong, and the only repair on offer is moving the sha forward, which builds the same oracle stale
again. Where the commit is absent (a shallow clone, an adopter's tree) the arm skips, so the
comparison it promises also silently covers nothing outside the repository that wrote it.

## Where it bit

`tools/workflows/unattended-build.test.sh`, the OC4 untyped arms of `TOOL-aOrientedCast-4`: the
untyped prompts were compared with harnesses read out of `git show 646d4a73:…`, and the closing
review of aOrientedCast (round 1, M4) found the oracle would red on the first prompt edit after
that commit. `TOOL-aOrientedCast-15` S1 replaced it.

## The fix

State what the comparison was FOR and test that against the CURRENT subject. "A stage with no role
runs as the harness does without roles" became: a run with no `roles` key equals a run with
`"roles":{}` under the same harness, every untyped-only span is present, and every typed-only span is
absent. A comparison of two runs of the current code keeps its meaning across edits; a comparison
with a frozen copy measures the distance from that copy, which grows by design.

No machine gate: a literal sha in a test is sometimes the subject itself (a fixture commit, a pinned
base under test). The documented check, in a Tier-2 review of any `.test.sh` diff, is a grep of the
added lines for `git show` or `rev-parse` followed by a hex literal, and for each hit the question
"does this arm red when the subject is legitimately edited?".
