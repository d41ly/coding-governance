**Serves:** journal TOOL-dTotalRecall-5

# Brief — dTotalRecall: TOOL-dTotalRecall-5's second build pass diverged; fold the spec again

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. The unit's second builder returned a DIVERGENCE at base `a8748ffaa`
before writing anything, recorded whole in
`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-5-2-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-5.md` in place as a rev bump, with one
revision-log line naming this brief and the builder return by their file stems, so the next builder can build it as
written and its §7 gates can go green.

### Items

1. Read the builder return whole. Its main finding: §4 "The policy reads" and S6 refuse on a `ValueError` from
   `tree_lib.py#read_policy_value`, and `policy.py get` raises it in any repository where no landed revision resolves,
   which every fixture of `tools/memory-tree/check-memory-hygiene.test.sh` is by design (its master pin) and
   `tools/memory-tree/corpus_ids.py#_scratch` is too, so `memory-hygiene self-test` and `corpus-ids selftest` would
   red. Decide between the return's options (a) a no-landed-revision `ValueError` applies `SLUG_DEFAULTS` as
   `LookupError` does, with one stderr line per process, a value the reader refuses still refusing; (b) keep the
   refusal and widen the fixtures; (c) read the keys only where `.governance/policy.toml` is tracked; by the build
   method's M3, marked RESOLVED in §8. Read how checks 6 and 7 treat their policy read's refusal (the comment block
   in `check-memory-hygiene.test.sh` names it) and keep one rule with them where it fits. Re-state §4 "The policy
   reads", S6's module-failure sentence and every criterion that reads the refusal so they agree with the choice.
2. Its minor finding: S13 rebinds only `build_id_token_re`'s slug group, while `_expand_ids`'s range form `rng`
   keeps `[A-Za-z0-9]+`, so `TOOL-dX-1..3` would still expand to `TOOL-dX-2`. Say whether `rng` splices the same
   slug class and add a criterion observing it.
3. Before you return, trace every caller of the functions S4 and S13 change for the fallback each takes when the
   grammar's policy read fails, so a third pass does not meet a third reader: `merge-rows.py`, `transition_audit.py`
   and `drift_report.py` are the ones the return names.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-5`,
`python tools/check-spec-tokens.py --spec <path>` and `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec
<path>`, and fix every finding they name. The status header keeps `INPROGRESS`; the write grant is the spec file
alone; do not commit.

### Acceptance

Every command exits 0; the spec carries its next rev and one revision-log line naming this brief and the return.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec but unit 5's. No product code. No change to Goal or Scope intent beyond what the findings force.
