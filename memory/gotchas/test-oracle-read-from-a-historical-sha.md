---
name: test-oracle-read-from-a-historical-sha
description: a test reads its subject out of git at a fixed revision — a literal sha, so every later legitimate edit of the subject reds it and the fix is always "move the sha", or HEAD, read while the runner records the verdict against the working tree, so the check certifies bytes it never read
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

The same oracle with a moving revision is item H1 of dGroundRules' round-1 spec audit of units 22
to 25: the policy kit's fresh-target case ran `apply` from `tools/govkit/govkit.py`, whose `blob_at`
reads HEAD, from `tools/policy/check_policy.py`, while the gate runner records the case's green
against the working tree, so an uncommitted edit was never installed and the green certified bytes
the case never read. `tools/govkit/matrix.py` applies into its targets the same way.
`TOOL-dGroundRules-26` and `TOOL-dGroundRules-27` are the repair.

## The fix

State what the comparison was FOR and test that against the CURRENT subject. "A stage with no role
runs as the harness does without roles" became: a run with no `roles` key equals a run with
`"roles":{}` under the same harness, every untyped-only span is present, and every typed-only span is
absent. A comparison of two runs of the current code keeps its meaning across edits; a comparison
with a frozen copy measures the distance from that copy, which grows by design.

For the HEAD shape, install from a commit of the working tree made in a scratch clone
(`build_source_snapshot`), or refuse naming the dirty paths; never grade HEAD silently while the
verdict is recorded against the working tree.

No machine gate: a literal sha or a HEAD read in a test is sometimes the subject itself (a fixture
commit, a pinned base under test). The documented check, in a Tier-2 review of any `.test.sh` diff,
is a grep of the added lines for `git show` or `rev-parse` followed by a hex literal, and for each
hit the question "does this arm red when the subject is legitimately edited?". For a spec that
drives `govkit apply` from gov's own tree, the question is "which revision does it install?".
