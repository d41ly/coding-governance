# Revision — aBriskDeclaration: the owner's answers to F1 and F2

**Serves:** research TOOL-aBriskDeclaration-1

## The prompt

> F1 rollout: Live, no switch (Recommended)

> F2 arm: Add its own arm

The owner's answers, 2026-11-14, to the two questions the session's question tool put from the spec's §8.

## The brief

### Goal
The owner answered the spec's two open questions on 2026-11-14, asked through the session's question tool. F1, "Does this land live, or dark behind a default-off switch?": "Live, no switch (Recommended)". F2, "Does the generator-pairing refusal owe a behavioural arm of its own?": "Add its own arm". Mark both forks RESOLVED with the owner's pick, and make F2's arm part of the spec: a traced driver-suite arm in which the dispatch is refused by the index-declared-with-its-generator refusal after the checker has started, showing the checker's `init_bounded` line, the refusal, a `read_bounded` line after it and no `kill`, and the refusal text with no spec-token line. Bump the spec's rev and add a revision-log line naming this record by its file stem. The code built at `4fed38fe1` and `fc4c62bfa` already follows F1's pick and stays as it is; only the new arm, its `New arm:` line and the criterion it covers are added.

### Items
1. In `memory/builds/aBriskDeclaration/spec/2026-11-14-spec-TOOL-aBriskDeclaration-1.md`, F1 and F2 each carry `RESOLVED (owner, 2026-11-14): <the pick>` in their own span.
2. A criterion for the generator-pairing arm, in the shape of AC4, and its `New arm:` line under §7, with the fixture it needs: a `GENERATED_INDEXES` pair declared for the suite's fixture, and a dispatch whose `--writes` names the index while a sibling or the same declaration names its generator.
3. The status stays INPROGRESS; the builder sets CLOSED after the arm lands.
4. Stage the spec and clear `python tools/check-spec-tokens.py --spec` over it. Do not commit.

### Acceptance
- The spec's two forks read RESOLVED with the owner's picks, its rev is 2, and its revision log names this record.
- The new criterion names an observation of the driver suite's traced dispatch, and its `New arm:` line names the base at which it reds.

### Gates
`check-spec-tokens.py --spec` over the spec.

### Non-goals
- Any change to the code at `4fed38fe1` and `fc4c62bfa` beyond the arm and its fixture.
- A conf key or switch: F1 is live.
- `memory/builds/dDeclaredLoop/`, its run's worktree and its branch.
