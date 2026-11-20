**Serves:** research TOOL-dPlacedRequest-21

# Brief — dPlacedRequest: TOOL-dPlacedRequest-21's divergence, resolved

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-21's builder returned a DIVERGENCE (run `wf_cba5f454-c60`) and committed nothing. At rev-8, S4
leaves the patch or repeat README staged as `tools/memory-tree/gen_build_index.py#cmd_new_build` stages it, and S7's
`tools/loop/loop_transition.py#write_transition` refuses any staged index, so a patch or repeat claim can never reach
its first record in one run (AC7 cannot pass). And S1's `gen_build_index.py#check_slug_claimed` pre-check runs on
every run, so after the first claim it finds the claimant's own claim commit and transition commit and refuses before
S2, breaking S1's resume and AC3/AC6. Revise the spec to the main loop's rulings, each a fork in §8 marked
`RESOLVED (agent, 2026-11-20, delegated): <option>, rung 3; <reason>. widens: none · relaxes: none`.

### Items

1. F-scaffold: the claim verb commits the staged scaffold (the README and the contract registry it stages) in one commit of its own, before S7 writes the first record; S4 and §4 "The act, in order" say so, and AC7 observes the scaffold commit then the record. Reason: one verb completes its own act, the transition writer keeps its rule that a transition commit carries its records alone, and a resumed run finds the scaffold already committed.
2. F-precheck: S1's pre-check runs only when no claim by this claimant's key exists; the claim ref is read first, and a claimant resuming its own claim skips `check_slug_claimed` and resumes at the first of S2 to S7 not yet witnessed. Amend S1, §4's order and AC3/AC6 to it. Reason: the pre-check guards a fresh claim; a resume is already the claimant's.
3. S7 passes the claim's `facts` to `write_transition` and the writer derives the scenario through `tools/loop/scenario.py#derive_move_scenarios`; no `scenario` field is given.
4. S7's patch: the first move is recorded as B2's `item.plan.dedupe` with outcome `patch` into designing, under its stand-in row, since `tools/loop/loop.toml` has no `item.entry.claim` row for disposition `patch`.
5. The §3 edge cites `tools/loop/request.py#derive_request_content_key`.

### Acceptance

Spec 21 at rev-9 carries the two resolved forks, S1, S4, S7, §3, §4 and AC3/AC6/AC7 amended, and one §9 line naming
this brief and the divergence; `check-memory-hygiene.sh --only 12,25 --spec`, the spec-token checker and
`bash tools/unattended/unattended.sh --check-specs dPlacedRequest TOOL-dPlacedRequest-21` report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the driver's `--check-specs` and the naming
lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays INPROGRESS), no spec other than
TOOL-dPlacedRequest-21, and no fork left open. Pin every figure you write with DERIVED or PINNED, never let a section
sign or a section number stand before a unit word, never write a bare file-stem section reference, and never quote a
check's hit literally in prose.
