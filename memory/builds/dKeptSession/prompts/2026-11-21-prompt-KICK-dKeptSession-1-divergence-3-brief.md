**Serves:** research KICK-dKeptSession-1

# Brief — dKeptSession: KICK-dKeptSession-1's third divergence, resolved

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-1's third builder (run `wf_b1359b32-6c1`) built the unit at rev-8, then returned a DIVERGENCE and
committed nothing. S3's pair rule in `policy.py#validate` (a file whose `review.design.round-count` is above its
`review.max-rounds` is invalid) breaks the review-bounds contract of TOOL-dDeclaredLoop-21 S4: under the default
`policy-file.on-invalid = "last-valid"` the reader falls back to the last valid revision, so
`tools/loop/review_bounds.py#read_review_bounds` reads the old bounds instead of refusing (the builder's probe: a
valid revision at seven and seven, then three and four, read back seven where the base refuses). That reds three
`write_tracking_policy` arms of `tools/unattended/unattended.test.sh` and the `count-above`, `no-driver` and `max-zero`
plants of `tools/loop/review_bounds.py`, and the rule already lives once in
`tools/loop/review_bounds.py#derive_review_bounds`, scoped to `review.design.rounds = "fixed-count"`. Three smaller
checks also failed: AC8's plain grep cannot print the selects row's value and point; the docs leg reds UNROWED on a
`presets.py` command in `help/policy.md` because `tools/govkit/usage.toml` has no row for it; and the four new
`policy fixtures` cases sit under a declared ceiling section 7 never revisits. Revise the spec to the main loop's
rulings below.

### Items

1. F-pair-home: add to the open-questions section, resolved by the main loop at rung 3: (a), the pair rule judges the preset STORE alone, the four shipped presets' assignments in `tools/policy/presets.toml`, through `presets.py check` and the arm's pairs case; `policy.py#validate` does not judge a repository policy file's pair, which stays `derive_review_bounds`'s refusal under `fixed-count`, its one home for that subject, so `review_bounds.py` and the `unattended.test.sh` arms are untouched. Rejected: (b) `validate` refusing the pair for every file, which turns a refusal into a silent fallback under `last-valid` and holds one rule in two homes with two scopes. Narrow S3, F1, AC4 and AC5 to it: say what `validate` still calls, if anything, and re-point AC4 and AC5 to observations the narrowed design makes (the store's pair refusal, and the base's review-bounds refusal unchanged over a repository file).
2. F-partial-kit-again: if the narrowed `validate` no longer imports `presets`, the four partial-kit suite copies of F9 serve nothing: drop them from F9, Files touched and the leg line (YAGNI), and say so; if it still imports, keep them.
3. F-small: AC8 names a command that prints the `[[selects]]` row's value and point (a short `python -c` over `tomllib`, or a grep with context lines); every `presets.py` command `help/policy.md` shows gets its `[[usage]]` row in `tools/govkit/usage.toml`, which joins Files touched; and section 7 states the `policy fixtures` leg's declared ceiling and the four cases' cost against it (the builder measured them in process), narrowing the core-only copy before any ceiling would have to move, since a declared ceiling is the owner's.
4. Re-cite every line you change as `path#symbol`, keep the spec within the live-spec size cap (trim prose you rewrite), pin every figure with DERIVED or PINNED, and leave no fork open.

### Acceptance

The spec at rev-9 carries the rulings and one revision-log line naming this brief by its file stem;
`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `python tools/check-spec-tokens.py --spec <path>`,
a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-1` report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (the spec stays INPROGRESS), and no spec other than
KICK-dKeptSession-1's. Other writers may be re-grounding later orders' specs: read them, never write them.
