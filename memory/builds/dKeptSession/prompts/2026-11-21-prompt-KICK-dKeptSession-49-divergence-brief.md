**Serves:** research KICK-dKeptSession-49

# Brief — dKeptSession: KICK-dKeptSession-49's divergence, resolved

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-49's builder (run `wf_fb418336-6e7`) returned a DIVERGENCE before any edit: S2 says the superseded
text of KICK-dKeptSession-40 is answered in unit 40's acceptance ledger, but unit 40 is CLOSED (built at order 4), its
ledger says nothing about the JS reader's input list, and that ledger is neither in this unit's Files touched nor its
write set. The builder also found that `tools/policy/README.md` describes the reader comparing each key of the mirror's
`legacy_blobs`, wording that is incomplete once S1 lands. Revise the spec to the main loop's rulings.

### Items

1. F-own-ledger: add to the open-questions section, resolved by the main loop at rung 3: (b), S2's answer to unit 40's superseded wording is recorded in this unit's own acceptance ledger (`memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-49-1-acceptance-ledger.md`), naming unit 40's spec text it supersedes; a CLOSED unit's records are never written by a later unit. Rejected: (a) writing unit 40's ledger, a record of a closed unit.
2. F-readme: `tools/policy/README.md`'s sentences on the reader comparing the mirror's `legacy_blobs` keys are corrected to the input list S1 derives, and the README joins Files touched with a criterion observing the corrected text.
3. F-behaviour: run or read each criterion's command against the verb and fixture it relies on and confirm the exit and output it names; no `path:number` token stands in the spec unless it is a blob pin; re-cite every changed line as `path#symbol`; keep within the live-spec size cap; pin every figure; leave no fork open.

### Acceptance

Spec 49 at a new rev carries the rulings and one revision-log line naming this brief by its file stem;
`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `python tools/check-spec-tokens.py --spec <path>`,
a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-49` report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (the spec stays INPROGRESS), and no spec other than
KICK-dKeptSession-49's. Another writer is checking specs 26, 15, 14, 30 and 9: read them, never write them.
