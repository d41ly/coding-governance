**Serves:** research KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33

# Brief — dKeptSession: build orders 1-2 re-grounded on the landed tree before their builds

## The prompt

> /unattended dKeptSession

## The brief

### Goal

Specs 1, 19, 33 of this build, all DEFERRED, were written by the spec run against BASE 462d20f3 and its
parents' specs (a few took an owner-fork rev on 2026-11-05). Since then both parents, dDeclaredLoop and
dPlacedRequest, have built and landed, with many sibling builds, and this build run's BASE is
c2a407b0. Re-ground each of these specs on that tree so a builder can build it as written, with no
DIVERGENCE return. A fork you rule is marked in that spec's open-questions section as
`RESOLVED (agent, 2026-11-21, delegated): <option>, rung <n>; <reason>. widens: <value|none> · relaxes: <value|none>`,
and a rung 5 or 6 choice also follows the README's build-level rule on forks.

### Items

1. F-tokens: clear every spec-token hit these specs carry. Each Files-touched path whose guarded leg is absent from the Gates leg line gets that leg named there; every line-number citation becomes a `path#symbol` citation or a blob pin.
2. F-reground: probe every claim about current code, docs and records against the tree at HEAD and cite where it stands by `path#symbol`. A function, flag, key, section, count, path or file that moved, was renamed or was superseded is re-cited to what holds it now. An item a landed unit already satisfies is marked so and reduced to its observation or dropped. Narrow each unit to what is left, and say in its revision-log line what was narrowed.
3. F-agree: a name, path, config key, record kind or signature this build's other specs also spell stays spelled identically. Where re-grounding must change one that another spec of this build names, do not edit that spec: name the spec and the change in your return under `interface-changes`.
4. F-shape: keep each spec within the live-spec size cap, leave no fork open, pin every figure you write with DERIVED or PINNED on its own line, never let a section sign or section number stand before a unit word, and never quote a check's hit literally in prose.

### Acceptance

Each of specs 1, 19, 33 at a new rev carries its re-grounded text, its resolved forks and one revision-log
line naming this brief by its file stem; `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`,
`python tools/check-spec-tokens.py --spec <path>`, a PLAIN `python tools/playbook/writing_practice.py check pinned-facts`
and `bash tools/unattended/unattended.sh --check-specs dKeptSession <its id>` report nothing for each.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (every spec stays DEFERRED), and no spec other than
1, 19, 33. Other writers are re-grounding this wave's other specs at the same time: read them, never write them.

### Limitations

Return, per spec: its id, the rev it reached, what the re-grounding changed and narrowed, the forks ruled, and
`interface-changes` (or none). Temp files go under the session scratchpad the handoff names, never the repository.

### Reuse

Each spec's own Reuse audit section names its seam and recall terms; re-run that probe and correct the section where the seam moved.
