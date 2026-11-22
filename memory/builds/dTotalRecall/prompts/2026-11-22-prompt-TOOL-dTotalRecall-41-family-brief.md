**Serves:** journal TOOL-dTotalRecall-41

# Brief — dTotalRecall: TOOL-dTotalRecall-41's ask-door commands carry unit 7's required --family

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. TOOL-dTotalRecall-7 rev-6 (its §8 F6) makes `--family <FAMILY>` a required
flag of `gov_record.py new ask`, refused before any mint unless a `FAMILIES` pair in the conf declares it
(`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-7-divergence-return.md`). Unit 41 rev-3's criteria
call `new ask` without it, so each would exit 2 for the wrong reason.

## The brief

### Goal

Revise `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-41.md` in place as a rev-4 bump, with one
revision-log line naming this brief by its file stem, so every `new ask` command it states passes `--family`.

### Items

1. Add `--family <FAMILY>` to every `new ask` command in the spec, using a family its fixture's conf declares; where a
   criterion's fixture conf is unstated, state the `FAMILIES` line it plants.
2. Read unit 7 rev-6 for the door's other changes that touch this spec (its F7 grade-before-mint order, its F8
   content-key replay check, the `wrote <path> <id> key <key>` success line) and align any claim this spec makes about
   them. A §8 resolution mark is exactly `RESOLVED (agent, 2026-11-22, delegated)`, nothing else inside the parentheses.
3. Change nothing else; the status header keeps `DEFERRED`.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-41`,
`python tools/check-spec-tokens.py --spec <path>` and `python tools/playbook/writing_practice.py check pinned-facts`, and
fix every finding they name in this spec. The write grant is the spec file alone; do not commit.

### Acceptance

The three commands exit 0 or read green for this spec; every `new ask` command carries `--family`.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec; no product code.
