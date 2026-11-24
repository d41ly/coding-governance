**Serves:** research KICK-dKeptSession-1

# Brief — dKeptSession: KICK-dKeptSession-1's second divergence, resolved

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-1's builder returned a second DIVERGENCE (run `wf_73059b2b-dc2`) at rev-6 and committed nothing.
(1) AC4 and AC5 say `python policy.py check` exits 1, and it cannot: `tools/policy/policy.py#cmd_check` returns 0
(valid, absent, or invalid with a last valid revision it falls back to) or 2 (a refusal such as no valid revision
preceding the sha), and the `on-invalid-classes` case in `tools/policy/check_policy.py#run_on_invalid_classes` pins
those exits. (2) S3 calls `check_repo_presets` from `policy.py#validate`, but five suites copy a partial policy kit
without `presets.py` and `presets.toml` and then read a policy file through `validate`
(`tools/check-line-length.test.sh`, `tools/hooks/agent-cap.test.sh`, `tools/unattended/check-unattended.test.sh`,
`tools/unattended/unattended.test.sh`, `tools/workflows/unattended-build.test.sh`), so an unconditional import
raises ModuleNotFoundError there. Revise the spec to the main loop's rulings below.

### Items

1. F-check-exit: add to the open-questions section, resolved by the main loop at rung 3: (a), AC4 and AC5 observe the exit and the text `policy.py check` gives, exit 2 and its refusal line, over a fixture that commits no valid revision before the invalid one; `cmd_check`'s exit contract is untouched, and no criterion names an exit 1 from that verb.
2. F-partial-kit: add to the open-questions section, resolved by the main loop at rung 3: (a), the five suites that copy a partial policy kit also copy `presets.py` and `presets.toml`, so `validate` imports `presets` unconditionally and the pair rules fail closed; the five suites join Files touched (name the copy line of each by `path#symbol` or by the variable or function it sits in) and the leg line names every leg those paths trip. Rejected: (b) `validate` skipping where `presets.py` is absent, a silent pass under deny-by-default.
3. Re-cite every line you change as `path#symbol`, keep the spec within the live-spec size cap (it is close: trim prose you rewrite rather than grow it), pin every figure with DERIVED or PINNED, and leave no fork open.

### Acceptance

The spec at rev-7 carries both rulings and one revision-log line naming this brief by its file stem;
`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `python tools/check-spec-tokens.py --spec <path>`,
a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-1` report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (the spec stays INPROGRESS), and no spec other than
KICK-dKeptSession-1's. Other writers are re-grounding later orders' specs at the same time: read them, never write them.
