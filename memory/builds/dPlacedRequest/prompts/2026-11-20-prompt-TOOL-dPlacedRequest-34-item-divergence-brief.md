**Serves:** research TOOL-dPlacedRequest-34

# Brief — dPlacedRequest: TOOL-dPlacedRequest-34's S41, resolved against the landed request draw

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-34's builder (run `wf_f91dc448-f5b`) built most of the unit and listed one item as diverged: S41
adds a `--request-text` driver flag so a draw can create a missing request record, but
`tools/unattended/unattended.sh#run_request_draw` (TOOL-dPlacedRequest-14) already creates it from the clone's kept copy
`<git-common-dir>/requests/<key>.md` and refuses naming `--request <file>` when neither exists. Revise S41 and AC41 to
the main loop's ruling.

### Items

1. F-S41: add to §8, resolved: "How does a draw create a request record it cannot find, when the landed draw already reads the clone's kept copy?" (a) S41 and AC41 are rewritten around the kept copy: the draw creates the record from `<git-common-dir>/requests/<key>.md` and refuses, naming the request verb, when no kept copy exists; (b) a `--request-text` flag as a second path. Mark `RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; one path for one act, the landed draw already holds it, and the kept copy is what the request verb wrote. widens: none · relaxes: none`. Rewrite S41 and AC41 so they describe and observe the landed behaviour (AC41 observing the refusal with no kept copy and the creation with one), with `path#symbol` citations.
2. Leave every other item, the status (INPROGRESS) and the rev number's other content as they are; add one §9 line naming this brief.

### Acceptance

Spec 34 carries the resolved F-S41 fork and the rewritten S41 and AC41; `check-memory-hygiene.sh --only 12,25
--spec` and the spec-token checker over it report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`) and the spec-token checker; no other.

### Non-goals

No product code, no commit, no index render, no status flip, no other item and no other spec. Pin every figure you
write with DERIVED or PINNED, and never quote a check's hit literally in prose.
