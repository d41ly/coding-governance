**Serves:** journal TOOL-dTotalRecall-7

# Brief — dTotalRecall: TOOL-dTotalRecall-7's quoted refusal names no path:line

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 7's pass legs read `positional (the citation check alone)` red on one
unlisted citation in its spec: AC7's quoted `policy.py` refusal spells `.governance/policy.toml:1`, the fixture seed's
own policy file, which the citation check reads as a bare path:line into this repository.

## The brief

### Goal

Revise `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-7.md` in place as a rev-7 bump, with one
revision-log line naming this brief by its file stem and saying the change is a record-only rewording to a CLOSED
spec, no criterion moved.

### Items

1. In AC7's quoted refusal, replace `.governance/policy.toml:1` with `<the seed's policy file and line>`, so the quote
   names no path:line; keep every other byte of the criterion.
2. The status header keeps `CLOSED`; change nothing else.

Before returning, run `python tools/playbook/positional.py check` (it must list no line of this spec as unlisted),
`python tools/check-spec-tokens.py --spec <path>` and `bash tools/memory-tree/check-memory-hygiene.sh --only 12
--spec <path>`, and fix every finding they name in this spec. The write grant is the spec file alone; do not commit.

### Acceptance

The positional check lists no line of the spec; the other two commands exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other change to spec 7; no other spec.
