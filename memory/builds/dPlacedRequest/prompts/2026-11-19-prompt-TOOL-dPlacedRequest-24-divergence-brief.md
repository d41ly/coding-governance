**Serves:** research TOOL-dPlacedRequest-24

# Brief — dPlacedRequest: TOOL-dPlacedRequest-24's divergence, a measured git behaviour

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-24's builder returned a DIVERGENCE (run `wf_495a7364-a80`) and committed nothing. A probe of git
2.54.0 against a scratch bare origin measured that `git push --porcelain --force-with-lease=<ref>: origin <c>:<ref>`,
with the remote ref already at `<c>`, exits 0 and prints `=` and `[up to date]`: git tests "up to date" before the lease,
and prints `[rejected] (stale info)` only when the remote tip is a different commit. In a true race the loser's update
fails as `[remote rejected]`, rc 2, the line is kept, and its next flush reads `[up to date]` and prints `flushed`. No
path prints a false `yield`. Revise the spec to that fact.

### Items

1. §1 Goal: replace the claim that the loser of two concurrent flushes prints a false `yield` with what git does: the loser's line is kept (rc 2) and the next flush resolves it as `flushed`.
2. §2 S5: delete it (its trigger, `write_gov_ref` returning 1 with the remote tip equal to the queued commit, cannot occur), and every reference to it in §3, §4, §5 and §10.
3. §6 AC2: delete it; renumber nothing (leave the gap, so the ledger's AC ids keep their meaning) and say in its place, one line, that it was removed and why.
4. §7: drop AC2 from the `New arm:` line's coverage.
5. §4: add one sentence recording the measurement, git 2.54.0, and the observation above, as the fact the design rests on, marked PINNED with today's date.
6. Leave S1 to S4 unchanged; the builder found every other claim held at the base. Note in §5 risks that `tools/run-gates/post-merge.sh` runs under `set -u` with no `ROOT` and no `add_health_event`, so the moved factory's stale-break path reaches those names there until TOOL-dPlacedRequest-36 lands, which S1 already defers to that unit.

### Acceptance

Spec 24 at rev-8 carries none of S5 or AC2 as live scope, the measured fact in §4, the corrected goal, and its §9 line
naming this brief and the divergence; `check-memory-hygiene.sh --only 12,25 --spec` over it and the spec-token checker
over it report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays INPROGRESS), and no spec other than
TOOL-dPlacedRequest-24. Pin every figure you write on its line with DERIVED or PINNED and cite code as `path#symbol`.
