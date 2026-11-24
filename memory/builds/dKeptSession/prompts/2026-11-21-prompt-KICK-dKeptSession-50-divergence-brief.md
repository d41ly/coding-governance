**Serves:** research KICK-dKeptSession-50 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-61

# Brief — dKeptSession: KICK-dKeptSession-50's divergence, resolved for its whole class

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-50's builder (run `wf_b0c09fd2-3f3`) returned a DIVERGENCE before any edit. S4 says its answer to
unit 40's superseded Migration and risks lines goes in unit 40's acceptance ledger. Unit 40 is CLOSED, and that
ledger is in neither this unit's Files touched nor its write set. This is the same divergence KICK-dKeptSession-49
returned and its rev-6 resolved. A grep finds six more specs that answer in an earlier unit's acceptance ledger:
47 and 48 (unit 30's), 51 (unit 22's), 53 and 55 (unit 42's), and 61 (unit 53's). Each of those earlier units
builds first, so each later builder would diverge the same way. Revise all seven to the main loop's ruling.

### Items

1. F-own-ledger: in each spec, every sentence that answers in another unit's acceptance ledger moves its answer to this unit's own ledger (`memory/builds/dKeptSession/build/2026-11-21-build-<this unit's id>-1-acceptance-ledger.md`). That ledger quotes the other unit's spec text it supersedes, and joins Files touched; where it trips a guarded leg, that leg joins section 7's leg line. Record the fork in each spec's open-questions section as resolved by the main loop: `RESOLVED (agent, 2026-11-21, delegated): (b), rung 3; a CLOSED unit's records are never written by a later unit, as KICK-dKeptSession-49 rev-6 ruled.` Rejected: (a), writing the earlier unit's ledger. Add a criterion, or extend an existing one, that observes the quoted passages in this unit's ledger.
2. F-ac3 (spec 50 only): AC3's grep for `rendered before` already matches `tools/policy/README.md` at this base, in unit 49's sentence about a mirror rendered before the store joined. AC3 must grep for a phrase only S3 adds, so its red side is observable at the pass base. Correct the rev-3 log's claim with a new line rather than editing the old one.
3. F-selfcheck (spec 50 only): govkit selfcheck 7l scans every tracked file under `tools/policy/`, docstrings included. Any sentence S3 or a new case adds that says `update` and `re-render` must also name `GOVKIT_RERENDER`. Say so where the spec describes the README and docstring text.
4. F-behaviour: run or read each changed criterion's command against the verb and fixture it relies on, and confirm the exit and output it names. No `path:number` token stands unless it is a blob pin. Re-cite every changed line as `path#symbol`. Keep within the live-spec size cap, pin every figure, and leave no fork open.

### Acceptance

Each spec is at a new rev, carrying the ruling and one revision-log line that names this brief by its file stem.
`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `python tools/check-spec-tokens.py --spec <path>`,
a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession <its id>` report nothing for each.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, and no status flip: spec 50 stays INPROGRESS and the others stay
DEFERRED. No spec outside these seven. Another writer may be checking specs 22, 31 and 5, and unit 54 may be
building: read them, never write them.
