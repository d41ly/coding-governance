---
name: staged-break-never-applied
description: the break you staged did not apply, so the RED you observed was the unmodified code and the gate is still untested
kind: class
universal: false
---

# A staged break that silently fails to apply

## Symptom

You stage a deliberate break, run the suite to watch a gate go RED, and read the result. The result
looks right. But the patch never landed — the patcher errored, matched nothing, or wrote somewhere
else — so what you actually measured was the UNCHANGED code. The gate has still never been observed
failing, and you have now recorded that it was.

This is worse than skipping the RED observation, because the record says the observation happened.

## Where it bit

`aPairedLexer`, 2026-08-30, twice in one session, on two different gates.

- The version-parity arm for `tools/hooks/agent-cap.js`. The break was staged by a `python - "$H"`
  heredoc. On this node `python` fed the script to **node**, which parsed `import sys, io` as an ES
  module and died with `Expected 'from', got 'ident'`. The `bash` script ignored that exit, ran the
  suite against the untouched hook, and printed `ok version parity … 125 passed, 0 failed`. Grepping
  for the parity line alone would have shown a clean pass and been read as a successful RED test.
- The `enumerate_exports` arm in `tools/codebase-map/selftest.py`. Here the break DID apply, and the
  arm went red — on `ValueError: … is not in the subpath of …`, because the fixture omitted
  `root=base` and `enumerate_exports` defaults `root` to the repo root. The arm never reached its own
  assertion. Red for the wrong reason is the same failure wearing the other mask: see
  [[fixture-passes-by-finding-nothing]], whose sub-shape is a GREEN arm that never reached its
  branch. Both are "the instrument did not measure the subject".

## The fix

**The staging must emit a witness, and the witness must be checked.**

- The patcher exits non-zero when its marker does not match, and the driver is `&&`-chained to it so
  a failed stage cannot proceed to the run.
- Print a countable proof AFTER staging and BEFORE running — `grep -c 'STAGED BREAK' "$file"` — so
  the log records that the tree really changed.
- Read the RED output for the EXPECTED failure text, not merely for non-zero. The second case above
  was non-zero, was genuinely a failure, and proved nothing.
- Restore by content hash and verify: capture `md5sum` before, compare after, and assert the marker
  count is back to `0`. A killed background job left a staged break standing in this same session's
  predecessor build, and the next staging captured the broken tree as its "good" baseline.

Prefer a patcher in a language you have confirmed runs here. `node` was already a hard dependency of
the subject under test; `python` was resolved by the suite through `tools/lib/resolve-python.sh` and
worked there, while a bare `python` in a sibling script did not.

## No machine gate

There is no machine gate for this class, and there cannot be a direct one: the RED observation
is a discipline applied WHILE authoring a gate, so there is no later run to enforce it. By the
time the suite exists, the evidence of how it was validated is gone. The
mechanical residue is the witness line in the build record: a unit claiming "observed RED" states the
staged marker count and the failing message it saw, so a reviewer can tell an observation from an
assertion. The version-parity arm in `agent-cap.test.sh` is the nearest structural cousin, bounding
regressions rather than validating its own authorship.
