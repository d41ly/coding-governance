**Serves:** journal TOOL-dTotalRecall-7

# Brief — dTotalRecall: TOOL-dTotalRecall-7's first build pass diverged; fold the spec to rev-6

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. The unit's first builder returned a DIVERGENCE at base `ed5a7d523`,
recorded whole in `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-7-1-builder-return.md`.

## The brief

### Goal

Revise the spec in place as a rev-6 bump, with one revision-log line naming this brief and the builder return by their
file stems, so the next builder can build it as written over HEAD.

### Items

1. Read the builder return whole. Settle its three gaps, each as a §8 fork decided by the build method's M3:
   (a) the `<FAMILY>` an ask id is minted in: the roster read the shell filers use (`unattended.sh#read_roster_family`,
   with the cost and refusal of `gen_build_index.py#read_derived_front_matter` the return measured), a cheaper rule, or
   a `--family` flag; state it in S2, §4 "The door verb", AC4 and the fixture text, including what the fixture plants;
   (b) the order of grade and mint: a refused filing must spend no counter number on the remote, so state the order
   that makes that true (TOOL-dTotalRecall-2's built `build_records.py#write_new_record` checks before it mints), or
   drop the sentence that claims it;
   (c) what a replayed `new ask` does, given `write_new_record` writes only `fields` kinds and a ask is two rows in
   BACKLOG.md; state the replay rule in §3 or §4 and give it a criterion.
2. A §8 resolution mark is exactly `RESOLVED (agent, 2026-11-22, delegated)`: nothing else inside the parentheses (check
   12 strips code spans and refuses the rest); cite the brief after the mark.
3. Keep every other rev-5 decision; a forced change is named in the revision-log line. The spec is TOOL-dTotalRecall-2's
   consumer: read unit 2 as built (`gov_record.py`, `d91388c2f`) and unit 3 as built (`gov-claim.sh`, `f8b950c13`).

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-7`,
`python tools/check-spec-tokens.py --spec <path>` and `python tools/playbook/writing_practice.py check pinned-facts`, and
fix every finding they name in this spec. The status header keeps `INPROGRESS`; the write grant is the spec file alone;
do not commit.

### Acceptance

The three commands exit 0 or read green; the spec carries rev-6 and one revision-log line naming this brief and the
return.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-7. No product code.
