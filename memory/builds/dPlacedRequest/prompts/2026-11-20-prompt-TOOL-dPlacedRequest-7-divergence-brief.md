**Serves:** research TOOL-dPlacedRequest-7

# Brief — dPlacedRequest: TOOL-dPlacedRequest-7's divergence, resolved

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-7's builder returned a DIVERGENCE (run `wf_060498d5-d58`) and committed nothing. At rev-7 the
command actors fail `tools/loop/loop_lib.py#ACTOR_FORM`; the probe's method has no home, grammar or writer and the
`design` verb no flags; a `claimed` judgment has no place in the closed `Verdict` set; AC6's visual kind is outside
S4's closed `--kind`; and `pin` cannot commit an entry-time trigger's record, which lives outside the worktree. Revise
the spec to the main loop's rulings, each a fork in §8 marked
`RESOLVED (agent, 2026-11-20, delegated): <option>, rung 3; <reason>. widens: none · relaxes: none`.

### Items

1. F-actor: the §4 table spells the command actors `command:probe.trigger`, `command:probe.pin`, `command:probe.judge` and `command:probe.return`, as the review program spells `command:review.trigger` and `command:review.pin` in `tools/loop/loop.toml`. Reason: the loop's one actor grammar stands, and the sibling program is the precedent.
2. F-method: the method lives in the `probe` record itself, in a section of its own (one record, one fact), one entry per line holding the command and its predicted `<exit>:<hash>`, with the optional marks `judge claimed` and `visual` spelled as trailing ` · `-separated fields on that entry. `probe.py design` is the method's one writer: it appends one entry per call, takes the record's address and the entry's command, prediction and marks as flags you name from the tree's flag vocabulary, and refuses once the record is pinned. Amend S5 (what `run` reads), S6 (the method section in the `probe` record's shape) and §4 Inventory (the `design` verb's flags), and add one acceptance criterion observing `design` append an entry and refuse after `pin`. Reason: the method is part of the record the probe pins, so it is written before the pin and frozen by it.
3. F-judged: S6 gains a field `Judged: computed|claimed` beside `Verdict`, and `Verdict`'s closed set stays as it is; a `claimed` judgment, or an `unrunnable` verdict, routes to an owner item as S5 already says. Reason: the verdict and the way it was reached are two facts.
4. F-visual: "visual" is the method entry's mark (item 2), not a `--kind`; S4's closed `--kind` stays, and AC6's plant pins a verification whose method carries a `visual` entry.
5. F-entry: for an entry-time trigger, `pin` writes `<key>.probe.md` into the git-common-dir `requests/` store and commits nothing, the store being outside the tree; S4's "commits it alone before any command runs" becomes "records it, committed where the record lives in the tree, before any command runs", and AC4's red condition reads "a command runs before the losing outcome is recorded".
6. Stale citations: S7 cites `tools/loop/request.py#derive_request_content_key`; S10's reader line names `tools/playbook/core.py#run_meta_check` and the `core-pending.txt` row it reads; the new leg's argv is `python {prefix}/loop/probe.py --selftest`, as `loop request fixtures` runs `request.py --selftest`, printing the count line the `testsuite counts` leg reads; and §4 says the `[[computed-witness]] probe-rerun` row in `tools/loop/loop.toml` switches its `serves` to `item.probe.run`.
7. §4 Files touched lists only paths (no command words), and gains `tools/govkit/registry.toml` and `tools/run-gates/selftest-budgets.txt` for the new leg, as `loop request fixtures` is registered.

### Acceptance

Spec 7 at rev-8 carries the five resolved forks, S4 to S7, S10, §4 and AC4/AC6 amended, the new `design` criterion,
`path#symbol` citations, and one §9 line naming this brief and the divergence; `check-memory-hygiene.sh --only 12,25
--spec` and the spec-token checker over it report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays INPROGRESS), no spec other than
TOOL-dPlacedRequest-7. Pin every figure you write with DERIVED or PINNED, never let a section sign or a section
number stand before a unit word, never write a bare file-stem section reference, and never quote a check's hit
literally in prose.
