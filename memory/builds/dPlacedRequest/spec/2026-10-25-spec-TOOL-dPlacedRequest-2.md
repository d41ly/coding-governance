# TOOL-dPlacedRequest-2 — the build's orientation card kept per build: a remote ref, a clone cache and a snapshot, following its build

**Status:** OPEN · rev-4 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 12 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0121@2f58beed whole
**Carries:** node:record-kind.card
**Carries:** node:policy-key.card.follows
**Carries:** node:policy-key.card.store
**Carries:** node:policy-key.card.snapshot
**Carries:** node:policy-key.resume.context
**Carries:** node:policy-key.resume.partial

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |

<!-- /gen:spec-records -->

## 1. Goal

A build's card cannot be found by its build: cards are keyed by session id in the clone's git
directory, so a new session, a dead process or another node never finds it, and no card exists on the
remote (gap-orient-11, `skills/session-kickoff/manifest-check.sh:310-317`). The card does not follow
its build across transitions (gap-flow-07), and a resumed route is never re-checked (gap-orient-02).
This unit keeps the build's card at level 1 per build, as the adopted research places it
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md:322-343`): a ref
per build on the remote, the truth; a cache in the clone keyed by build and the ref's object id; a
snapshot committed in the build folder as `card.snapshot` says; the stores `card.store` selects;
re-rendered as `card.follows` says; looked up and re-keyed in the session's own tree on resume, with a
fresh session recommended by `resume.context` and partial work handled by `resume.partial`.

## 2. Scope (IN)

- **S1** — The build card. `render_build_card <slug>` in `skills/session-kickoff/manifest-check.sh`
  prints one header line `card — <slug> · step <state> · published <iso> · by <sid>`, the session
  card's startup cells re-rendered by `render_card` (:517), `## pockets` among them
  (TOOL-dPlacedRequest-9 S4), and the session card's tail: its `## task`, `## route` and other body
  sections and its READY line, as `extract_card_parts` (:980) splits them. `<state>` is the state the
  caller names, `unrecorded` at the first publish. The card is refused past `CARD_CAP_BYTES` as
  `write_card` (:706) refuses. Observed by AC1.
- **S2** — The three stores, I13 of the brief: the ref `refs/gov/builds/<slug>/card`, a commit whose
  message carries the card, built by TOOL-dPlacedRequest-11's `build_gov_commit <tip read> <message>`
  (I2) and written through `write_gov_ref` (I1) with the tip read as the expected value, so the
  write joins the change feed `gov-feed.log` as every `write_gov_ref` call does (I4); the kickoff
  engine carries both blocks inline, `gov_ref_sh` and `gov_feed_sh`, under their parity rows; the cache `<git-common-dir>/orientation/<slug>.md`, its first line `# card-ref <oid>`, the
  ref's commit id or `local` when the ref is not selected; and the snapshot, a record of the new
  `card` kind (S8). `card.store` selects the set, any non-empty subset of `remote-ref`, `build-folder`
  and `local-clone`, all three by default (v2:1173); every publish writes each selected store and no
  other. Observed by AC2 and AC3.
- **S3** — The publish at READY. `--card --append` (:1143), when the appended body lands a READY line
  and a `## route`, publishes the build card for the route's `- build:` slug, after the append has
  succeeded: a store that cannot be written prints `card — <store> not written: <why>` and the append
  stands. Observed by AC2.
- **S4** — The follow at a transition. TOOL-dDeclaredLoop-3's `write_transition` gains a last step,
  after its commit: `manifest-check.sh --card --follow --build <slug> --to <state> [--terminal]`,
  resolved as an optional sibling of the loop kit, `--terminal` given when `<state>` is in the
  `terminal` set of `[states]` (TOOL-dDeclaredLoop-15 S1). Under `card.follows` (v2:1169):
  `re-render-at-transition`, the default, re-publishes the stored build card's tail under fresh
  startup cells and `step <state>`; `card-per-step` publishes a card holding the startup cells,
  `step <state>` and `READY — none yet` alone, so the next step orients afresh; `fixed-at-start`
  re-publishes nothing, except at a terminal state. Every value publishes at a terminal state. With
  no kickoff engine resolved the writer prints `card — skipped: no kickoff engine` and its transition
  stands. Observed by AC4.
- **S5** — The snapshot. Under `card.snapshot` (v2:1174), `terminal-only`, the default, writes a
  `card` record at the `--terminal` follow only, and `every-transition` at every follow and at the
  READY publish. The record is committed alone, subject `card snapshot(<slug>): <state>`, in the
  session's own tree; a dirty index refuses the snapshot, naming it, and the other stores are still
  written. With `build-folder` unselected no snapshot is written. Observed by AC5.
- **S6** — The lookup. `--card --lookup --build <slug> [--session <sid>]` reads the build card from
  the first selected store that answers, in the order remote-ref, local-clone, build-folder: the ref
  fetched by `git fetch --no-tags origin +refs/gov/builds/<slug>/card:refs/gov/builds/<slug>/card`
  under `CARD_FETCH_BOUND`, the cache trusted only while its `# card-ref` equals the fetched commit
  id, the snapshot the newest `card` record. It prints one `card —` line with TOOL-dDeclaredLoop-8
  S3's verdict word: `fresh` when cache and ref agree, `re-derived` when the cache was rewritten from
  the ref, `evidence` when the remote did not answer and an older store was read. It then re-keys the
  card into the session's file `<sid>.md` in the session's own tree: the session header, the startup
  cells re-rendered there, the build card's tail kept; and PLAY-dOrderedCharter-8 S2's
  `write_card_file` renders it into that tree's card file. Observed by AC6.
- **S7** — The resume. `print_replay` (:721), when the session card's `## route` names a build, runs
  S6's lookup first, re-runs `check_card_route` (:1006) over the re-keyed card and prints
  `route — re-checked · <verdict>`, then prints two lines: `resume — <recommendation>` under
  `resume.context` (v2:1177) and `partial — <n> uncommitted path(s) · resume.partial: <value>` under
  `resume.partial` (v2:1176). `fresh-when-idle`, the default, recommends a fresh session when the
  hook payload's `transcript_path` was last written more than `RESUME_IDLE_S = 300` seconds before
  the replay; `always-resume` recommends resuming, and reads as `fresh-when-idle` while gov's entry
  file `CLAUDE.md` carries no `@.claude/orientation-card.md` line, printing that override
  (v2:1177, `cl-dClosedLoop-0150`); `always-fresh` always recommends a fresh session. The
  `partial —` line names the value's act, which `skills/session-kickoff/SKILL.md`'s resume paragraph
  states: `continue-item` keeps the work and continues the routed item, its witness still owed;
  `restart-item` commits the work to a side branch `partial/<slug>/<sid8>` and restores the tree to
  `HEAD`, so nothing is lost; `ask-owner` asks the owner, or parks under a mandate. Observed by AC7
  and AC8.
- **S8** — The `card` record kind, `record-kind.card`, a row of the record factory
  `tools/memory-tree/build_records.py` (PLAY-dOrderedCharter-7 S7):
  `<date>-build-<anchor id>-card-<n>.md`, `**Serves:** journal <anchor id>`, fields `Build`, `Step`,
  `Ref` (the ref's commit id or `none`) and the card's text in one fenced block. The anchor is the
  lowest unit id a spec H1 under the build defines, TOOL-dDeclaredLoop-3 §8 F2's rule. Observed by
  AC5.
- **S9** — The terminal route. A route rule R7 in `check_card_route`: a route whose build's local
  ref `refs/gov/builds/<slug>/card` reads a `step` the follow marked terminal is refused at append,
  naming the build and its state, and reported by S7's re-check. Observed by AC9.
- **S10** — One path reader. `--card --path --build <slug>` prints the cache path, and `readCard` in
  `tools/hooks/scratch-guard.js` (:667) asks `--card --path --session <sid>` for the session card's
  path under a bound, as `resolve_card_path` in `tools/roles/handoff.py` (:255) already does; a
  checker that does not answer reads as no card, named. Observed by AC10.
- **S11** — The five keys, each read once per verb through dGroundRules' `policy.py get` (I24) by
  `read_card_policy <key>`, a bounded call resolved as an optional sibling; until that reader lands,
  each reads v2's catalogue default. Their catalogue rows land through TOOL-dDeclaredLoop-6 S4's
  `python tools/playbook/core.py new policy-key <name> … --owner dPlacedRequest`, each with its v2
  values and default. A refused read prints `card — skipped: <key> refused` and writes the session
  card only, as today. Observed by AC11.
- **S12** — The fixture, `bash skills/session-kickoff/card-store.fixture.sh --plant <case>`: a
  scratch repository and a bare remote in the system temp directory, a stub policy kit answering the
  planted values, and the case's observation printed, exit 0 when it holds. Observed by AC1 to AC11.

## 3. Non-goals (OUT)

- The level-1 delivery itself, the per-worktree card file, its import and its envelope:
  PLAY-dOrderedCharter-8's; S6 calls its `write_card_file`.
- The card's keys and verdict words: TOOL-dDeclaredLoop-8's `claims.py`, read here.
- Which session holds a build: the lease (TOOL-dPlacedRequest-1) and the claim
  (TOOL-dPlacedRequest-21); a route to another session's build is theirs to refuse.
- The orientation scout composing the card and the `entry.orient` item: dFurnishedOrders'
  `cl-dClosedLoop-0204` and TOOL-dPlacedRequest-3, which calls S3's publish and S6's lookup.
- Splitting partial work by the item's write set: the item's declared seed is TOOL-dPlacedRequest-8's
  and the act at an item boundary dWellOiledMachine's executor's; S7 reports the count and the value.
- A context-size leg of `fresh-when-idle`: the hook payload carries no context size, so idle alone
  decides.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-11` — `write_gov_ref`, the one compare-and-swap writer the card ref is written through, with its parented commit
- **consumes-from** `TOOL-dPlacedRequest-13` — `gov-feed.log`, the feed every `write_gov_ref` call appends to, whose `gov_feed_sh` block the kickoff engine carries inline beside `gov_ref_sh`
- **consumes-from** `TOOL-dPlacedRequest-9` — `## pockets`, the card section the build card carries in its startup cells
- **hands-off** `TOOL-dPlacedRequest-3` — `refs/gov/builds/<slug>/card`, published at READY and resolved through `manifest-check.sh --card --path`, the path reader `entry.orient` names as its body
- **consumes-from** external — dDeclaredLoop, built before this build run: `write_transition` (TOOL-dDeclaredLoop-3 S5), the `terminal` set (TOOL-dDeclaredLoop-15 S1), `claims.py`'s verdict (TOOL-dDeclaredLoop-8 S3), the policy-key factory (TOOL-dDeclaredLoop-6 S4)
- **consumes-from** external — dOrderedCharter's `write_card_file` (PLAY-dOrderedCharter-8 S2) and record factory (PLAY-dOrderedCharter-7 S7); dGroundRules' `policy.py get`
- **hands-off** `TOOL-dPlacedRequest-33` — the `remote-ref` store's publish and follow, which that unit routes through the driver's `--card-ref write`, dark behind `RUN_CLAIMS`
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names
- **hands-off** `TOOL-dPlacedRequest-49` — `skills/session-kickoff/card-store.fixture.sh`, which that unit's item for finding 3 gives the `publish-late` plant

## 4. Design

### The stores

| Store | Key | Written | Trusted |
|---|---|---|---|
| `remote-ref` | `refs/gov/builds/<slug>/card` | `write_gov_ref` with the tip read, a parented commit | always, the truth |
| `local-clone` | `<git-common-dir>/orientation/<slug>.md`, first line `# card-ref <oid>` | every publish and every lookup that re-derives | while `<oid>` equals the ref's commit id |
| `build-folder` | `<date>-build-<anchor id>-card-<n>.md` | S5's snapshot | evidence, the newest record |

A lost compare-and-swap (`write_gov_ref` rc 1) re-reads the tip, re-renders once on it and writes
again; a second loss prints `card — remote-ref not written: lost to <sha8>`.

### The card ref's commit

```
build_gov_commit <tip read> "gov-card <slug>

step: <state>
session: <sid>

<the build card's text>"
```

The empty tree and the `gov-claim` identity are `build_gov_commit`'s; a reader takes the card from
`git log -1 --format=%B refs/gov/builds/<slug>/card`, every line after its fifth.

### The follow, by value

| `card.follows` | Non-terminal transition | Terminal transition |
|---|---|---|
| `re-render-at-transition` | tail kept, cells fresh, `step <state>` | the same, and the snapshot under either `card.snapshot` |
| `card-per-step` | cells fresh, `step <state>`, `READY — none yet` | the same, and the snapshot |
| `fixed-at-start` | nothing written | tail kept, cells fresh, `step <state>`, and the snapshot |

### The resume lines

```
card — dExample · re-derived · ref 3f9c2a71 · cache rewritten
route — re-checked · ok
resume — fresh recommended: idle 1840s past 300s (resume.context: fresh-when-idle)
partial — 2 uncommitted path(s) · resume.partial: continue-item · kept, the item continues
```

`RESUME_IDLE_S` is the prompt cache's five-minute lifetime, PINNED 2026-10-25 and UNVERIFIED against
the platform's documentation in this tree; it is one constant beside `CARD_CAP_BYTES`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `render_build_card`, `publish_build_card`, `follow_build_card`, `lookup_build_card`, `read_card_policy` | shell functions | `sh.function`, asked at the pass |
| `--card --publish`, `--card --follow`, `--card --lookup`, `--build`, `--to`, `--terminal` | flags of `manifest-check.sh` | none |
| `CARD_FETCH_BOUND`, `RESUME_IDLE_S` | constants | none declared |
| `refs/gov/builds/<slug>/card` | ref | none |
| `card` | record kind of `build_records.py` | none |
| R7 | route rule | none |
| `card-store.fixture.sh` | fixture | none |

### Migration

None. A per-session card on disk keeps working: the session file is unchanged, and a build with no
published card reads `card — none published` at lookup.

### Rollout

Live at landing. The publish runs at the first READY after landing; the follow runs from the first
transition the loop kit records.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`: the verbs, and the inline `gov_ref_sh` and `gov_feed_sh` blocks; `KIT_MANIFEST_VERSION` moved
- `tools/lib/resolve-python.test.sh`: the two parity rows gain the kickoff engine's copies
- `skills/session-kickoff/manifest-check.test.sh`: the arms the §7 line declares
- `skills/session-kickoff/card-store.fixture.sh`
- `skills/session-kickoff/SKILL.md`: the resume paragraph's three acts; the installed skill is its machine-scoped link
- `tools/hooks/scratch-guard.js`: `readCard`
- `tools/loop/loop_transition.py`: the follow call after the commit
- `tools/memory-tree/build_records.py`: the `card` kind row
- `tools/policy/catalogue.toml`: five rows, through the factory
- `.governance/policy.json`: the mirror, regenerated by `policy.py mirror --write` in its own commit
- `help/orientation-card.md`: the build card's stores, the follow and the resume lines

### Alternatives rejected

- **The card in the run claim's message.** The claim carries eight keys
  (`tools/unattended/unattended.sh:2411-2412`) for a run, not a build, and mixing the two records
  would make one ref's history answer two questions.
- **A tree holding the card as a blob.** `build_gov_commit` builds over the empty tree; a second
  commit builder for one blob would be a second writer of the parented commit I2 fixes.
- **Keying the cache by session.** That is gap-orient-11 itself.
- **A follow on every beat.** The clause re-renders at transitions; a beat is no step change.

## 5. Production-readiness checklist

- security — the ref is written only through `write_gov_ref`'s compare-and-swap; the slug is held to
  the route grammar `[A-Za-z0-9]+` before it is joined into a ref or a path; the card carries no
  secret beyond what the session card carries today.
- perf / scale — one bounded fetch per lookup and per replay; publish is one push.
- error / empty / loading states — each store's failure prints its own `card —` line and never
  refuses the append or the transition; no published card prints `card — none published`.
- observability — every lookup prints its verdict word and the store it read.
- risks — two sessions on one build race the ref; the loser re-renders once on the winner's tip, so
  the history keeps both.
- testing — S12's plants, red and green.
- migration — none.
- user docs — `help/orientation-card.md`, TOOL-dPlacedRequest-9's page, gains the build card's
  sections.

## 6. Acceptance criteria

- **AC1** — When `bash card-store.fixture.sh --plant render` runs, the build
  card's first line reads `card — tFix · step unrecorded`, its `## pockets` and `## route` sections
  are present, and its READY line is last.
  Red when: the tail is dropped or the header names the session instead of the build.
- **AC2** — When the plant `publish` appends a READY body with a `## route` naming `tFix`, the bare
  remote holds `refs/gov/builds/tFix/card`, the cache's first line names that commit, and a second
  publish's commit has the first as its parent.
  Red when: a publish writes a parentless commit over a tip, or the cache names another object.
- **AC3** — When the plants `store-remote`, `store-local` and `store-folder` set `card.store` to one
  value each, only that store is written; with `store-empty`, `[]`, the read is refused and the
  session card alone is written.
  Red when: an unselected store is written, or an empty set publishes.
- **AC4** — When the plants `follow-rerender`, `follow-per-step` and `follow-fixed` record a
  transition to `designing`, the ref's card reads `step designing` with the tail kept, `step
  designing` with `READY — none yet`, and is unchanged, respectively; with `--terminal`, each value
  publishes.
  Red when: a value behaves as another, or a terminal transition leaves the card behind.
- **AC5** — When the plant `snapshot-terminal` records two transitions, the last terminal, the build
  folder holds one `card` record; with `snapshot-every`, two; and `python build_records.py read`
  grades each clean.
  Red when: `terminal-only` snapshots a non-terminal move, or a record misses `Build`, `Step` or `Ref`.
- **AC6** — When the plant `lookup` runs `--card --lookup --build tFix --session t2` in a second
  clone, it prints `card — tFix · re-derived`, writes `t2.md` with the session's header and the
  build card's tail; with `lookup-offline`, the remote unreachable, it prints `evidence` and reads
  the cache.
  Red when: a lookup trusts a cache whose `# card-ref` differs from the ref, or another node finds no card.
- **AC7** — When the plants `context-idle`, `context-always-resume` and `context-always-fresh` replay
  over a transcript last written 1800 seconds earlier, the `resume —` line recommends fresh, resume
  and fresh; with `context-no-import`, `always-resume` and no import line in `CLAUDE.md`, it
  recommends fresh and names the override.
  Red when: a value is ignored, or `always-resume` holds while the import is unwired.
- **AC8** — When the plants `partial-continue`, `partial-restart` and `partial-ask` replay over a
  tree with two uncommitted paths, the `partial —` line reads `2 uncommitted path(s)` and names its
  value, and `grep -n "partial/<slug>/<sid8>" skills/session-kickoff/SKILL.md` finds the restart act.
  Red when: the value is not printed, or the restart act can lose the work.
- **AC9** — When the plant `terminal-route` appends a route to a build whose local card ref reads a
  terminal step, the append exits 1 printing `route R7 REFUSED` and the card is unchanged; a replay
  over a card routed there prints `route — re-checked · R7`.
  Red when: a route to a terminal build lands.
- **AC10** — When `grep -n "'--card', '--path'" tools/hooks/scratch-guard.js` runs, it finds
  `readCard`'s call, and `grep -c "'orientation', sid" tools/hooks/scratch-guard.js` prints `0`.
  Red when: the hook derives the card path itself beside the checker's.
- **AC11** — When `python -c "import tomllib, sys; print(sorted(r['name'] for r in tomllib.load(open(sys.argv[1], 'rb'))['key'] if r.get('owner') == 'dPlacedRequest' and r['name'].split('.')[0] in ('card', 'resume')))" catalogue.toml`
  runs in the policy kit's directory, it prints the five keys, and `git grep -n "read_card_policy card.store" -- skills/session-kickoff/manifest-check.sh`
  finds the read.
  Red when: a key has no row, or is read in a shape the reader-coverage arm does not count.
  fixture: the catalogue is dGroundRules', untracked until it builds.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `spec tokens (a spec's own names resolve)`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC2 AC4 AC6 AC9 · the publish, follow, lookup and R7 arms over a scratch bare remote, the failing case a lookup trusting a stale cache · none

New arm: tools/hooks/scratch-guard.test.sh · covers AC10 · `readCard` against a stub checker, the failing case a checker that does not answer read as a card · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that
  legal?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:27`. Observation, 2026-10-25:
  the tuple does not hold `DRAFT`. Liveness: it would show `DRAFT` if the vocabulary held it.
  RESOLVED (agent, 2026-10-25, delegated): `OPEN`.
- **F2 — What does `card-per-step` re-render that `re-render-at-transition` does not?** FI-8 offered
  "One card per step" beside the default
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow-interactions.md:121-123`)
  and states no mechanism. Options: (a) a fresh card per step, its body cleared, so the step orients
  afresh; (b) a ref per step. (b) needs a ref beside the one I13 fixes. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the survivor, each value distinct on its plant (AC4).
- **F3 — Does `fixed-at-start` publish at a terminal transition?** RESOLVED (agent, 2026-10-25,
  delegated): yes, rung 3: the terminal transition is the snapshot point `card.snapshot`'s default
  names, and the terminal step is what S9's route rule reads, so a fixed card still records that its
  build ended.
- **F4 — Does the build's grant cover the kickoff skill's resume paragraph?** It is a governance
  carrier and the clause names `resume.partial`. RESOLVED (agent, 2026-10-25, delegated): covered,
  rung 3.
  grants: PLAY-dClosedLoop-3 the resume paragraph's three resume.partial acts in skills/session-kickoff/SKILL.md

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 2, the adopted preserve research, FI-8,
  OR-4, OR-5, OR-7 and v2:1169-1177.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: AC1 cites the fixture by its basename; the
  hands-off to TOOL-dPlacedRequest-3 names `manifest-check.sh --card --path`, the reader that unit calls, in
  place of `--card --lookup`.
- rev-3 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-33,
  hands-off TOOL-dPlacedRequest-34, each the mirror of that promoted unit's own edge.
- rev-4 · 2026-10-25 · §3 · the round-3 spec audit's disposal: the edge mirror hands-off TOOL-dPlacedRequest-49.

## 10. Reuse audit

The seams extended are the card verbs of `skills/session-kickoff/manifest-check.sh` (`CARD_DIR` and
`CARD_FILE` at :310-317, `render_card` at :517, `write_card` at :706, `print_replay` at :721,
`check_card_route` at :1006), all verified at base; the compare-and-swap writer TOOL-dPlacedRequest-11
extracts from `write_claim` (`tools/unattended/unattended.sh:2396`, its `commit-tree` at :2419);
TOOL-dDeclaredLoop-3's `write_transition` as the follow's trigger; and `resolve_card_path`
(`tools/roles/handoff.py:255`), the one caller already asking `--card --path`. Scout B's row cited
`scratch-guard.js:667-671` as deriving the path itself; source agrees (`readCard` joins
`orientation/<sid>.md` at :671). `python tools/codebase-map/reuse_lookup.py "publish a build's
orientation card to a remote ref and cache it by object id"` ranked name stems (`build`,
`build_commit`, `render_cards_md`), none a card store, so no existing seam holds the per-build key.
`python tools/memory-recall/query.py` returned scout B's row, KICK-aReplayedCard-1 (partly superseded
by TOOL-aGraftedHelix-2) and TOOL-dDeclaredLoop-8's scout row; the last is the re-key S6 reuses.

Recall terms used: `python tools/memory-recall/query.py "where does a build's orientation card live across sessions and nodes" --terms "orientation card refs/gov/builds card.store card.snapshot card.follows resume.context resume.partial cache object id"`
