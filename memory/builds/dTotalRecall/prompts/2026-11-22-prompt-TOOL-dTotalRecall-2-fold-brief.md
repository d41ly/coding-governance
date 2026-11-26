**Serves:** journal TOOL-dTotalRecall-2

# Brief — dTotalRecall: TOOL-dTotalRecall-2 folded against unit 3 as built and the landed lease reader

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. Unit 2 rev-11 cannot be built as written: its F6 lease check needs a
seventh `--lease status` field no landed code prints and no filed ask requests, and its rule for an ask-id mint in a
clone with no remote was the re-ground's own call, made before TOOL-dTotalRecall-3 was built
(`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-2-reground-return.md`).

## The brief

### Goal

Revise `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-2.md` in place as a rev-12 bump, with one
revision-log line naming this brief by its file stem, so a builder can build it as written over HEAD with no new field
and no unfiled ask.

### Items

1. Re-decide F6 against the landed `tools/loop/placement.py#read_build_lease`, which already compares fleet tag and
   session over the six `--lease status` fields. Use it, or the six fields as they print, for the authority-to-mint
   check; mark F6 RESOLVED (agent, delegated) with the reason, and restate every S-line, §4 passage and criterion that
   leaned on the seventh field. If no landed reader can answer "this lease is mine" at all, park the fork and say so.
2. Read TOOL-dTotalRecall-3 as built (`tools/memory-tree/gov-claim.sh`, commits `f8b950c13` and `dd15c0a8b`, its
   deviations 33 to 35) for what a clone with no remote answers on a claim and on an ask-counter mint, and make the
   door's rule agree with it. Unit 7's ask-door fixture (its rev-5) has no remote: state which answer that fixture
   gets, so unit 7's builder can plant it.
3. Unit 3's `read_own_claim` reads only the local cache; where the claim check needs a slug claim's `session` from the
   remote, use what unit 3 landed and state it.
4. Keep every other rev-11 decision. Tighten prose you touch: the spec sits 112 B under its 49152 B ceiling (PINNED
   2026-11-22 by the spec size check), and a criterion is never dropped to fit.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-2`,
`python tools/check-spec-tokens.py --spec <path>` and `python tools/playbook/writing_practice.py check pinned-facts`,
and fix every finding they name in this spec. The write grant is the spec file alone; do not commit.

### Acceptance

The three commands exit 0 or read green; the spec names no field or ask that does not exist at HEAD.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec. No product code.
