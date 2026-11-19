# The orientation card

**What it is.** Every session start writes an orientation card: one file per session under the git
common directory's `orientation/` folder, written by the kickoff engine `manifest-check.sh --card`.
Its cells say where the session stands, the tree, the worktrees, the drift, the overlaps, the claims
and the health log, then `recent —`, the last commits, and the kickoff's `READY` line once one is
appended. A resumed or compacted session reads it back through the replay. Every cell is derived;
nothing on the card is typed by hand.

## The `## pockets` section

The card carries the repository's orientation facts under `## pockets`, immediately above
`recent —`. Each fact is a level-2 instruction unit of the overlay, `.governance/instructions.toml`,
scoped to the card's reader `reader.card`, and the section prints one whole line per unit in the
overlay's order:

```text
## pockets
- A build of more than one pass runs on `memory/guides/BUILD-METHOD.md`; it is in `watch:`, so editing it re-audits this manifest.
- … (+35) — instruction_units.py pockets --all
recent —
```

The playbook kit's `instruction_units.py pockets` verb prints the section. It reads the overlay at
`HEAD`, so a fact shows on the card once the commit that wrote it is `HEAD`. The facts come from
your kickoff manifest's `## §B` bullets, which the upgrade step `kickoff-manifest/facts-to-overlay`
moves ([upgrade steps](upgrade-steps.md)); a card written before the step ran reads
`- none declared`.

## Its room

The section has no cap of its own. The card has one cap, `CARD_CAP_BYTES` in `manifest-check.sh`,
8192 bytes by default (PINNED: that constant's default), and the section takes the room the card's
other parts leave under it, measured afresh each time a card is written, appended to or re-keyed by
a replay. The verb prints the facts that fit, whole lines from the first, then one closing line
counting the facts left out and naming the command that prints them all:

```text
- … (+<k>) — instruction_units.py pockets --all
```

A line is never cut. A long kickoff body shrinks the section, never the body, and a card is never
refused for its pockets: where the other parts leave too little room for the heading and that
closing line, the card carries no section. Run `instruction_units.py pockets --all` from the
playbook kit's directory, or with `--root <tree>`, to read every fact.

When the verb cannot run, the section is one `pockets — skipped: <why>` line in its place, for no
playbook kit, no Python, a read that refused or one that did not answer within
`CARD_POCKETS_BOUND` seconds, and the card still writes.

## Change a fact

A fact is a unit, so it changes through the instruction write command, as a proposal the owner
applies: `instructions_edit.py propose add --manifest overlay` with the row's flags for a new fact,
and `propose edit` for a stale one. Your manifest's §B names the command's path in your install.
The other sub-sections of §B, the pointer map, the gate commands and the traps, stay guide text and
are edited in the manifest as before.
