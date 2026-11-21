**Serves:** research TOOL-dPlacedRequest-9

# Brief — dPlacedRequest: TOOL-dPlacedRequest-9's divergence, resolved

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-9's builder returned a DIVERGENCE (run `wf_2deb92d4-d95`) and committed nothing: at rev-4 the
fixed `## pockets` cap pushes today's largest session cards past `CARD_CAP_BYTES`, so the kickoff's append would be
refused; S6 and AC8 spell an `instructions_edit.py propose` command with no write verb and cite a SKILL.md sentence
that does not exist; and §4 Files touched misses the path that runs the step's fixture arm and the help page that
lists each upgrade step. Revise the spec to the main loop's rulings so it can be built as written.

### Items

1. F-cap, the section's size. Add to §8, resolved: "How big may the `## pockets` section be, when today's cards already reach most of `CARD_CAP_BYTES` and gov's §B has grown past the fixed cap?" (a) a smaller fixed `POCKETS_CAP_BYTES`; (b) the card passes the verb the room it has left (the cap minus the card's other parts), and the verb prints whole lines that fit, closing with one line counting the units left out and naming the command that prints them all; (c) the section lives only in the replay, not the stored card; (d) raise `CARD_CAP_BYTES`. Mark `RESOLVED (agent, 2026-11-19, delegated): (b), rung 3; the card's one cap stays the only figure (one fact), no card is ever refused for its pockets, and (a) fails again as cards grow, (c) drops the facts the goal puts on the card, (d) is rejected in §4 already. widens: none · relaxes: none`. Amend S3, S4 and §4 "The card section" to it, re-pin every figure from the tree today (gov's §B bullet count and bytes, the largest card on this node), and make one acceptance criterion observe a card at its cap: the append lands, the section ends with the left-out line, and the card's bytes stay at or under `CARD_CAP_BYTES`.
2. F-cmd: S6 and AC8 spell `instructions_edit.py propose add --manifest overlay` (`tools/playbook/instructions_edit.py#main` requires a write verb after `propose`). S6 names the sentence it rewrites in each file as the tree has it: in `skills/session-kickoff/SKILL.md`, Step 2b's repair sentence about re-checking §B claims; in `skills/session-kickoff/MANIFEST-TEMPLATE.md`, the ratchet section's write-back sentence. Quote neither in full; name each by its section heading.
3. F-paths: add `tools/govkit/selftest.py` to §4 Files touched with one scope line saying it calls the new step's `--fixture` the way it calls its neighbours (`fanout_cap.py`, `review_rounds.py`, `receipt_schema_4.py`), so §7's `govkit selftest` arm is run by a leg; add `help/upgrade-steps.md`, whose section on what this release's steps do gains the step's bullet and whose pinned count moves with it.
4. F-answer: the step's argv carries only `{gov}`, `{target}` and `{prefix}` (`tools/govkit/upgrade_steps.py` refuses any other placeholder), so S5 says the step reads `[answers] manifest_path` from the target's `.governance/deploy.toml` itself, and that `up` and `down` exit 0 with nothing to move when that answer is absent, as `tools/govkit/steps/adopter_rules_to_overlay.py` does for a missing key.
5. Replace every stale line citation in the revised sections with a `path#symbol` citation.

### Acceptance

Spec 9 at rev-5 carries the resolved fork, S3, S4, S5, S6, §4 and AC8 amended, the new criterion, the two paths in
Files touched, re-pinned figures, `path#symbol` citations, and one §9 line naming this brief and the divergence;
`check-memory-hygiene.sh --only 12,25 --spec` and the spec-token checker over it report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays INPROGRESS), no spec other than
TOOL-dPlacedRequest-9. Pin every figure you write with DERIVED or PINNED, never let a section sign or a section
number stand before a unit word, and never quote a check's hit literally in prose.
