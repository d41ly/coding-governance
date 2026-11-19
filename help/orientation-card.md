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

## Your build's card

A session's card lives under its session id, so a new session, another machine or a resumed one
cannot find it. The kickoff engine also keeps one card per build, keyed by the build's slug. When a
kickoff appends a `READY` line and a `## route` naming a build, the engine publishes that build's
card. Its first line names the build and the step it is at:

```text
card — dExample · step unrecorded · published 2026-11-19T10:00:00+0000 · by <session id>
```

Below that line come the card's cells, rendered afresh, then your session card's `## task`,
`## route` and `READY` line. The card has the same cap as the session card, `CARD_CAP_BYTES`.

The card is written to each store the `card.store` policy key selects. All three are selected by
default:

| Store | Where | What it is |
|---|---|---|
| `remote-ref` | the ref `refs/gov/builds/<slug>/card` on `origin` | the truth: one commit per write, each on the one before |
| `local-clone` | `<git common dir>/orientation/<slug>.md` | a cache, its first line `# card-ref <commit>`, trusted only while that commit is the ref's |
| `build-folder` | a `card` record in the build's `build/` folder | a snapshot, committed alone, as `card.snapshot` says |

The `remote-ref` store is written by the unattended driver, `--card-ref write`, and only while your
`.unattended.conf` sets `RUN_CLAIMS="on"`. With the switch off, or no `.unattended.conf`, the append
prints `card — remote-ref not written:` and the reason, writes nothing to the remote, and still writes
the other two stores; the cache's first line then reads `# card-ref local`. A driver that does not
answer within the card's fetch bound is named the same way, and the append goes on.

`card.snapshot` is `terminal-only` by default, so the build folder gets one record when the build
ends. With `every-transition` it gets a record at every stage move and at the `READY` publish too.
Snapshots need a clean index: if anything is staged, the snapshot is skipped and named.

Run `manifest-check.sh --card --publish --build <slug> --session <sid>` to publish again by hand.
Run `--card --path --build <slug>` to print the cache's path.

## The card follows the build

Each stage move the loop kit records runs `manifest-check.sh --card --follow --build <slug> --to
<state>`, adding `--terminal` when the state ends the build. The `card.follows` key decides what is
published:

- `re-render-at-transition` (the default): fresh cells, `step <state>`, and the stored card's
  task, route and `READY` line kept.
- `card-per-step`: fresh cells, `step <state>` and `READY — none yet` alone, so the next step
  orients afresh.
- `fixed-at-start`: nothing is published until a terminal move.

Every value publishes at a terminal move. If the build folder already holds a record for that
terminal state, a second terminal move keeps it and prints `card — snapshot kept: <state> already
recorded`. Once a build's card is at a terminal step, appending a route to that build is refused
with `route R7 REFUSED`.

## Finding the card on another session or machine

`manifest-check.sh --card --lookup --build <slug> --session <sid>` reads the build's card from the
first selected store that answers: the ref (one bounded fetch), then the cache, then the newest
snapshot. It writes the card into that session's own card, with the session's header and freshly
rendered cells, and prints one line:

```text
card — dExample · re-derived · ref 3f9c2a71 · cache rewritten · re-keyed into <sid>.md
```

`fresh` means the cache matched the ref. `re-derived` means the cache was rewritten from the ref.
`evidence` means the remote did not answer, so an older store was read. With nothing published, it
prints `card — none published for <slug>`.

## When a session resumes

When a replayed card's route names a build, the replay runs the lookup first, then checks the route
again and prints the resume lines after the card:

```text
route — re-checked · ok
resume — fresh recommended: idle 1840s past 300s (resume.context: fresh-when-idle)
partial — 2 uncommitted path(s) · resume.partial: continue-item · kept, the item continues, its witness still owed
```

`resume.context` decides the recommendation. `fresh-when-idle`, the default, recommends a fresh
session once the transcript has been idle more than 300 seconds (PINNED: `RESUME_IDLE_S`, the
prompt cache's lifetime), or when the transcript cannot be found. `always-fresh` always recommends a
fresh session. `always-resume` recommends resuming only while the card-import fixture's recorded
verdict is a pass, and otherwise reads as `fresh-when-idle` and says why. `resume.partial` names
what to do with uncommitted work: `continue-item`, `restart-item` (commit the work to
`partial/<slug>/<sid8>`, then restore the tree) or `ask-owner`. The kickoff skill's resume paragraph
states each act. The replay itself changes nothing in your tree.
