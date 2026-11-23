# The orientation card

**What it is.** Every session start writes an orientation card: one file per session under the git
common directory's `orientation/` folder, written by the kickoff engine `manifest-check.sh --card`.
Its cells say where the session stands, the tree, the worktrees, the drift, the overlaps, the claims
and the health log, then `recent —`, the last commits, and the kickoff's `READY` line once one is
appended. A resumed or compacted session reads it back through the replay. Every cell is derived;
nothing on the card is typed by hand.

The `node —` cell names your machine's row of the node registry: the row whose tag `GOV_NODE` names
when you set it, as the gate runner and the unattended driver read it, else the row whose user is
yours; a `GOV_NODE` that names no row reads `node — UNKNOWN:` with the reason.

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
| `remote-ref` | the ref `refs/gov/builds/<slug>/card` on the clone's one remote | the truth: one commit per write, each on the one before |
| `local-clone` | `<git common dir>/orientation/<slug>.md` | a cache, its first line `# card-ref <commit>`, trusted only while that commit is the ref's |
| `build-folder` | a `card` record in the build's `build/` folder | a snapshot, committed alone, as `card.snapshot` says |

The `remote-ref` store is written by the unattended driver, `--card-ref write`, and only while your
`.unattended.conf` sets `RUN_CLAIMS="on"`. With the switch off, or no `.unattended.conf`, the append
prints `card — remote-ref not written:` and the reason, writes nothing to the remote, and still writes
the other two stores; the cache's first line then reads `# card-ref local`. A read of the card ref
that does not answer within the card's fetch bound wrote nothing and is named the same way, and the
append goes on. The write has its own, longer publish bound, `CARD_PUBLISH_BOUND`, so it is not
stopped while the remote is still answering; a write stopped at that bound prints `card —
remote-ref unknown:` instead, because it may have landed first, and a landed one is picked up at
the next read of the remote. The append goes on either way.

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

## The card's pointers

The build's card, and a session card once its first item boundary is crossed, carry a `## pointers`
section directly above the `READY` line, saying where the build is now rather than where it started:

```text
## pointers
records — journal memory/builds/dExample/build/2026-10-27-build-KICK-dExample-1-agent-ledger.md · spec-audit memory/builds/dExample/reviews/2026-10-27-review-KICK-dExample-1-spec-audit.md
forks — memory/builds/dExample/spec/2026-10-27-spec-KICK-dExample-3.md §8
item — item.build.base@KICK-dExample-2#3f9c2a71 · at 8c1e0b42
budget — open 3/10
mail — 6299617af701
```

- `records —` names the build's newest record of each kind, one per kind, read by the memory-tree
  kit's `gen_build_index.py --latest-records <slug>`.
- `forks —` names the spec of each unit whose open questions are still unresolved, with its `§8`, or
  `none`.
- `item —` names the item in flight, the loop kit's instance key, or `none` while the build waits on
  something other than an item, and the commit it was read at. While the remote is stale or the
  build's inputs do not read, the item already named is kept.
- `budget —` shows the build's remaining rework budget, the line the loop kit's `budget.py state`
  prints, one of three: `budget — open <n>/<total>`, `budget — spent` or `budget — unfrozen <n>/<total>`.
  `open` is a frozen budget with `<n>` of its `<total>` draws made, `spent` one with none left, and
  `unfrozen` one not yet frozen at the end of design. Only you, the owner, raise the budget;
  nothing on the card does. With no loop kit in the repository it reads `budget — skipped:
  no loop kit`, which hides the budget rather than showing it as zero.
- `mail —` names each open message addressed to the build or one of its units, by id, the unattended
  driver's `--mail read <slug> --open --ids`, or `none`. An open message holds the build's moves until
  it is answered, acknowledged or past its deadline ([the loop's moves](loop.md)). With `RUN_CLAIMS`
  off it reads `mail — skipped: RUN_CLAIMS is off`, never `none`.

A line whose source does not answer reads `<word> — skipped: <why>`. `manifest-check.sh --card
--check` refuses a stored section missing one of its lines and names `--card --pointers`, which
renders the section afresh; a card written before a line was added reads that way until then.

**When the section is rewritten.** Every publish and every follow writes a fresh section into the
build's card. Between those, the item boundary does: after a commit, the session's next shell call
notices that HEAD has moved past the `at` of its card's `item —` line and starts `manifest-check.sh
--card --boundary --build <slug> --session <sid>` in the background, so the call is not held up. The
verb moves `at` to HEAD and reads the build's current item. When the item has changed it prints
`boundary — <old> → <new>` and rewrites your session card's section. The verb then lists each open
message addressed to the build as an `interrupt — mailbox` line, as `mailbox.reads` says; see "Where a
build is, and what runs next" in [the loop page](loop.md). The `card.pointers` policy key
decides whether the build's card is published too: <!-- usage: policy:card.pointers 6940ded3 -->

- `every-item` (the default): the build's card is published at every item boundary.
- `at-transitions`: only your session card is rewritten; the build's card gets a fresh section at the
  next stage move.

The verb's lines are reported to the session at the shell call after it finishes. Run
`manifest-check.sh --card --pointers --build <slug> --session <sid>` to write the section by hand.
A card the section would push past `CARD_CAP_BYTES` is not written and prints `card — pointers not
written: <n> bytes over the cap`.

## Finding the card on another session or machine

`manifest-check.sh --card --lookup --build <slug> --session <sid>` reads the build's card from the
first selected store that answers: the ref (the unattended driver's `--card-ref lookup`, one bounded
fetch into this node's cache ref that writes no `FETCH_HEAD`), then the cache, then the newest
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
resume — fresh recommended: idle 1840s past 300s · in C:/work/repo/.claude/worktrees/dExample (resume.context: fresh-when-idle)
partial — 2 uncommitted path(s) · resume.partial: continue-item · kept, the item continues, its witness still owed
position — act · next item.build.unit-pass
lead — the compaction summary is a lead, never a source: check it against the position above and the card's pointers
context — 72% of window · past 60% · fresh at next item boundary (context.on-full: fresh-at-boundary)
```

`resume.context` decides the recommendation. `fresh-when-idle`, the default, recommends a fresh
session once the transcript has been idle more than 300 seconds (PINNED: `RESUME_IDLE_S`, the
prompt cache's lifetime), or when the transcript cannot be found. `always-fresh` always recommends a
fresh session. `always-resume` recommends resuming only while the card-import fixture's recorded
verdict is a pass, and otherwise reads as `fresh-when-idle` and says why. `resume.partial` names
what to do with uncommitted work: `continue-item`, `restart-item` (commit the work to
`partial/<slug>/<sid8>`, then restore the tree) or `ask-owner`. The kickoff skill's resume paragraph
states each act. The replay itself changes nothing in your tree.

The `position —` line is where the build stands, as the loop kit's position engine re-derives it from
witnesses (`position.py <slug> --json`): its answer, and for `act` the next item, else `next none`.
It is always the engine's answer, never the card's stored `item —` pointer; where the two differ, trust
the position line. A card that routes no build, a tree with no loop kit, or an engine that does not
answer within its bound prints `position — skipped:` and why, and the card still prints. After a
compaction, and only then, a `lead —` notice follows the `position —` line: the harness's summary of
the conversation is a paraphrase nothing checks, so read it as a lead and check what it claims against
the position line and the card's `## pointers` before you act on it. A resume restores the transcript
itself and prints no notice.

The `context —` line shows how full the session's context window is, as a whole percent: the tokens
its last request read, as its transcript records them, over the window derived per model from this
node's observed usage: `CLAUDE_CODE_MAX_CONTEXT_TOKENS` where the harness sets it, else the largest
context this node's recent transcripts show on that model, rounded up to the 200k or the 1M window.
No transcript names the window a session runs, so on a node that runs one model at both windows a
200k session reads its fill against the 1M window unless the owner starts it with
`CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000` set.
A subagent's requests never count. The `context.on-full` policy key decides what a filling window leads to, and
`context.threshold` where it starts: <!-- usage: policy:context.on-full 50e931f0 --> <!-- usage: policy:context.threshold ba7d79dc -->

- `fresh-at-boundary` (the default): once the share reaches `context.threshold` (`60%` by default),
  end the session at its next item boundary and start a fresh one, which reorients from the card.
  The replay prints `context — 72% of window · past 60% · fresh at next item boundary
  (context.on-full: fresh-at-boundary)`, or `context — 41% of window · under 60%` below it. At the
  item boundary itself, the background boundary verb adds `context — 72% of window · past 60% · fresh
  now, at this item boundary (context.on-full: fresh-at-boundary)` to the lines reported at your next
  shell call: that is the point to stop. Below the threshold the boundary prints nothing.
- `compact-with-card`: nothing is measured at a boundary; the harness compacts the session when its
  window fills and the replay puts the card back. The replay prints `context — 41% of window
  (context.on-full: compact-with-card)`.

When the transcript cannot be read, or the measure does not answer within its bound, the replay
prints `context — skipped:` and why, and the card still prints; a boundary prints nothing.

The card-import fixture's verdict lives in one file per clone, `card-fixture.verdict` in the
`orientation` folder of the git common directory, so every worktree reads the same one. Record it on
a machine by running `manifest-check.sh --card --fixture-run <empty-dir>`: it runs
`card-compaction.fixture.sh` in that directory, which starts two headless sessions and takes
minutes, then writes and prints one line such as `card-fixture — pass · fixture 3f9c2a71 · cli
2.1.308 · 2026-10-27T09:14:02+0000`. The version is that of the `claude` first on PATH, the
binary the fixture launches. A pass counts only while the fixture file is still the one it names and
the tested version is both PATH's `claude` now and the version of the session reading it, so editing
the fixture, upgrading the CLI on PATH, or starting a session whose harness runs another version
makes it stale, and the override returns until you run the fixture again. The reason names the two
versions that differ: `recorded under cli <old>, PATH now <new>` or `fixture ran cli <x>, this
session runs <y>`. A version that cannot be read on any side, the recorded one, PATH's or the
session's, is red too, as `cli version unknown` with the side named. A machine whose IDE harness and
PATH binary run different versions never passes until the two run one version and the fixture is
run again. With no file, the reason printed is `no recorded run`. Every fresh recommendation names the tree to start in after `· in`: the worktree the
build's card was published from, when `git worktree list` still lists it, else `a new worktree of
<slug>`.
