**Serves:** research KICK-dKeptSession-67

# Brief — dKeptSession: KICK-dKeptSession-67's three line-zero citations pinned

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-67 is CLOSED and merged, and the pass legs at the run head red on one leg: `positional (the citation
check alone)`, with three `unlisted` rows. All three are in `memory/builds/dKeptSession/spec/2026-11-22-spec-KICK-dKeptSession-67.md`,
and each spells a line-zero location that a quoted refusal line carries: one each for `pass-tree.sh`, `pass-tree.test.sh` and
`tools/policy/catalogue.toml`. A spec's pass-leg fix goes through the writer as a rev bump. The red-fix lane refuses spec paths.

### Items

1. Remove each of the three tokens. Either describe the quoted refusal without its line suffix, or blob-pin it with
   `python tools/playbook/positional.py pin <spec path>`, whichever keeps the criterion that quotes it true. A criterion
   whose grep counts the exact refusal text must still match what the verb prints. Change no other text.
2. Bump the spec to rev-3, with one revision-log line naming this brief by its file stem. The status stays CLOSED.

### Acceptance

`python tools/playbook/positional.py check` ends `tags: positional · green · 0 red`.
`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `python tools/check-spec-tokens.py --spec <path>`
and a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` report nothing.

### Gates

The positional check, the memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the pinned-facts check;
no other.

### Non-goals

No product code, no commit, no index render, and no spec other than KICK-dKeptSession-67's.
