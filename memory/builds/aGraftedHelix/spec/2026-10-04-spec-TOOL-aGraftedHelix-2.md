# TOOL-aGraftedHelix-2 — the orientation card lists the remote run claims under a two-clock rule

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 5266d22e · streams kickoff · order 2 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 |

<!-- /gen:spec-records -->

## 1. Goal

A session starts with a card that names its node, tree, worktrees and the local `LIVE.md` count,
and nothing about runs other nodes are driving. This unit adds one `claims —` cell, read from the
driver's `--claims` verb, so every session opens knowing which slugs are claimed on the remote,
which of those are live, stale or held, and which ended recently, with old history hidden.

## 2. Scope (IN)

- **S1** — `render_card` in `skills/session-kickoff/manifest-check.sh` prints a `claims —` cell
  directly below `live —` and above `recent —`, so `CARD_PARTS_AWK` files it in the startup part.
  `derive_claims_line` builds it. Observed by AC1 and AC2.
- **S2** — Adoption is read from the tree: no `.unattended.conf` at the root prints
  `claims — skipped: no .unattended.conf in this tree`, the shape the `live —` cell already uses for
  `.memory-tree.conf`, and reads nothing. Observed by AC3.
- **S3** — The driver is found the way the card already finds the memory-tree id reader. The body
  of `resolve_id_reader` becomes `resolve_kit_file <home> <anchor>`, which `resolve_id_reader` then
  calls for `memory-tree corpus_ids.py`; the card calls it for `unattended unattended.sh`. No path
  of the unattended kit is spelled in the engine. Nothing resolving prints
  `claims — skipped: no unattended driver resolves in this tree`. Observed by AC7.
- **S4** — The read is bounded: `timeout -k 2 $CARD_CLAIMS_BOUND bash <driver> --claims`, default
  15 s, stdin from `/dev/null` so a hook's never-closing pipe cannot hold it, its stdout captured to
  a scratch file under the card's own directory and never through a command substitution. A fired bound prints `claims — skipped: --claims did not answer within
  15s, so the remote's claims are unknown, not none`. A node with no working `timeout -k` prints a
  `skipped:` line naming that and runs no read. Observed by AC5.
- **S5** — The two clocks. The first is the driver's: `live` and `stale` split on
  `RESUME_STALE_BOUND`, read inside `--claims` and never here. The second is the card's
  `CARD_CLAIMS_HIDE_S`, 86400 s: a `stale` or `terminal` claim whose beat is older is hidden and
  counted. A `live`, `held` or `unknown` claim is never hidden. Observed by AC1.
- **S6** — The forms. `claims: none` from the driver prints `claims — none on the remote`. Rows
  print a head `claims — <n> on the remote · <s> shown · <h> hidden`, where shown counts every
  claim the second clock keeps. At most `CARD_CLAIMS_ROWS` (8) of them print as indented rows
  `<slug> · <node> · <status> · beat <age>s · <verdict>`, ordered `live`, `held`, `unknown`,
  `stale`, `terminal` and then by slug, so a busy remote cannot push a live claim off the card; one
  `… <m> more` row follows past the cap. A non-zero exit prints `claims — skipped: ` and the driver's
  first refusal line, cut at 160 bytes. The rows are split with `awk -F'\t'`, never `read`. Observed
  by AC1, AC4 and AC5.
- **S7** — The remote contact is narrowed and recorded. The card moves no branch, no
  remote-tracking ref and writes no `FETCH_HEAD`; the driver's private claim cache is the only ref
  namespace its read touches. One `memory/DECISIONS.md` row under this unit's id records that the
  card now makes this one bounded read, narrowing the no-fetch clause KICK-aReplayedCard-1 S8 set.
  `--card --replay` makes no read and prints the stored cell. Observed by AC6 and AC10.
- **S8** — The engine's version and the manifest. `KIT_MANIFEST_VERSION` and its `gov:kit
  kickoff-manifest@` marker move once after the last edit; `MANIFEST_FORMAT` does not move. The
  kickoff manifest's `last-audit` is re-stamped with a delta line, because
  `skills/session-kickoff/manifest-check.sh` is on its watch list. The session-kickoff dossier gains
  one sentence on the cell. Observed by AC8 and AC9.
- **S9** — The cost of a card write with the cell is measured on node `a` and recorded in the
  unit's acceptance ledger. Observed by AC10.

## 3. Non-goals (OUT)

- **Re-deriving a verdict.** The card never reads `RESUME_STALE_BOUND` and never computes `live`
  or `stale`; a second spelling of the driver's predicate is the class
  `memory/gotchas/two-readers-of-one-config-one-re-derived.md` names.
- **Editing `skills/session-kickoff/SKILL.md`.** It is 25 bytes under its 18 KiB gate, and the cell
  is self-describing.
- **An adopter knob.** `CARD_CLAIMS_BOUND`, `CARD_CLAIMS_HIDE_S` and `CARD_CLAIMS_ROWS` are
  constants beside `CARD_CAP_BYTES`; the bound's environment override exists for the self-test, as
  `CARD_CAP_BYTES`'s does.
- **The `health —` cell** is `TOOL-aGraftedHelix-8`.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-1` — the `--claims` verb: `claims: none`, five
  TAB-separated fields per claim with the verdict last, and exit 2 with a named refusal.
- **hands-off** `TOOL-aGraftedHelix-8` — the card's `claims —` cell sits above `recent —` and below
  the local count, so that unit's cell goes between them, directly above `recent —`.

## 4. Design

### Evidence

Read at base `5266d22e`.

- `render_card` (`skills/session-kickoff/manifest-check.sh:247`) prints `live — skipped:` when the
  tree has no `.memory-tree.conf`, and its comment records why: this kit requires no other kit.
- `resolve_id_reader` (`skills/session-kickoff/manifest-check.sh:419`) tries `resolve_kit_dir` from
  the checker's own directory, then from the repo root, then the one tracked file the index names.
  The predicate `git ls-files -- unattended.sh '*/unattended.sh'` over this tree returns exactly
  `tools/unattended/unattended.sh`; near-miss: none.
- The card's self-test extracts `resolve_kit_dir` and `resolve_id_reader` from the checker with
  `awk` and `eval`s them, so `resolve_kit_file` joins that extraction or the suite's reader lookup
  breaks.
- `CARD_CAP_BYTES` is 8192. A head plus eight rows plus the more row is under 900 bytes.
- `skills/session-kickoff/SKILL.md` measured 18407 bytes against the 18432-byte gate.
- The SessionStart hook in `.claude/settings.json` declares no timeout, so the harness default
  bounds the whole card.
- Measured on node `a` 2026-10-04: the driver's `--version` startup took 1.89 s and an empty glob
  fetch of the claim namespace 0.67 s, so the 15 s bound leaves about five times the expected read.

### The cell

```
claims — 4 on the remote · 3 shown · 1 hidden
  aGraftedHelix · daily-agent · live · beat 312s · live
  dSlowBuild · agent-0 · held · beat 259200s · held
  cOldBuild · agent5 · landed · beat 7100s · terminal
```

The rows carry no path, sha or id-shaped token, so `--card --check` has nothing in them to grade.
Every field the driver prints is non-empty, and the card still splits on the TAB in `awk`, because
an empty field collapses under `read` (`memory/gotchas/empty-field-collapses-unless-it-is-last.md`).

### Why the bound is a file and a kill

`timeout` kills its direct child. A `$( )` capture then still waits for every grandchild holding
the pipe, such as the driver's `git fetch`, so the bound would decide the verdict and not the
clock (`memory/gotchas/bounded-through-a-pipe-is-unbounded.md`). Capturing to a file makes the
card wait for `timeout` alone; an orphaned fetch finishes inside the driver's own remote bound and
writes only the claim cache.

### Inventory

New functions in cell `sh.function`, each `OK` from `python tools/lexicon/lexicon.py --suggest
<name> --as sh.function` on 2026-10-04: `derive_claims_line`, `resolve_kit_file`. New constants
`CARD_CLAIMS_BOUND`, `CARD_CLAIMS_HIDE_S` and `CARD_CLAIMS_ROWS`. No new file, leg or conf key.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/DECISIONS.md`
- `memory/map/features/session-kickoff.md`

### Alternatives rejected

- **The card reads the remote itself.** It would need the claim format, the stale bound and the
  verdict table, a second implementation of the driver's
  (`memory/gotchas/second-implementation-is-not-a-second-opinion.md`).
- **One clock: list every claim.** A terminal claim is never taken off the remote, so the list
  grows with every run of every slug and reaches `CARD_CAP_BYTES`, where the card refuses to write.
- **The second clock as a multiple of the stale bound.** The card would have to read
  `RESUME_STALE_BOUND` and re-derive its default when the conf leaves it blank.
- **A stored cell refreshed by `--replay`.** A compaction would then pay a remote read the
  `startup|clear` card already paid; `--replay` stays local, as its `now —` line is.

## 5. Production-readiness checklist

- security — The card runs a tracked driver the resolver found in this tree, with the same
  bounded remote call the driver makes for itself. No credential is read or printed.
- perf / scale — One driver start and one remote read at session start, bounded at 15 s; AC10
  records the measured cost.
- error / empty / loading states — No conf, no driver, no `timeout -k`, a fired bound, a refusing
  driver and no claim each print their own `claims —` form, and the card is still written.
- observability — The cell is the observation; a `skipped:` form says why it has none.
- risks — Every card write in a tree adopting the unattended kit now starts the driver once, and
  that call adds its START and END lines to the driver's machine-local run log, which nothing reads
  back.
  Existing card arms in the self-test run in a clone whose remote is the local checkout, which
  answers `claims: none` in about two seconds per write.
- testing — New arms in the card suite, each observed RED on a staged break: claims seeded with
  real `gov-claim` messages over a bare remote, a slow-driver stub for the bound, and a remote URL
  that names nothing.
- migration — None: a tree without `.unattended.conf` reads `skipped:`.
- user docs — N/A: the card is self-describing, and the manifest names it.

## 6. Acceptance criteria

The fixture is a `git clone --local` of this repository under `%TEMP%`, its one remote re-pointed at
a bare repository whose claims are seeded with `git commit-tree` over the empty tree and pushed to
`refs/gov/runs/<slug>`.

- **AC1** — When the fixture's remote holds a fresh `live` claim, a `held` claim three days old, a
  `stale` claim two hours old, a `stale` claim three days old, a `landed` claim two hours old, an
  `aborted` claim three days old and one lacking `beat-utc`, `bash
  skills/session-kickoff/manifest-check.sh --card --write --session t2` prints
  `claims — 7 on the remote · 5 shown · 2 hidden` and rows for the first, second, third and fifth
  claims and the malformed one.
  Red when: a three-day `stale` or `aborted` claim is listed, or the `held` or `unknown` one is
  hidden.
- **AC2** — In that card the `claims —` head sits directly below `live —`, and
  `bash skills/session-kickoff/manifest-check.sh --card --check --session t2` prints no
  `UNVERIFIED` line for a row.
  Red when: the cell lands below `recent —` and the startup split files it in the tail.
- **AC3** — When the fixture's `.unattended.conf` is deleted and the card is written, it reads
  `claims — skipped: no .unattended.conf in this tree` and the exit is 0.
  Red when: the cell is absent, or the card is refused.
- **AC4** — When the fixture's remote URL names a path that does not exist, the card reads
  `claims — skipped: ` followed by `UNATTENDED check 91 FAILED`, and the card is written.
  Red when: the cell reads `none on the remote`, the empty answer a failed read must never give.
- **AC5** — When the fixture's `tools/unattended/unattended.sh` is replaced by a script that sleeps
  30 s and the card is written with `CARD_CLAIMS_BOUND=2`, the cell reads
  `claims — skipped: --claims did not answer within 2s` and the card write returns in under 10 s.
  Red when: the write waits for the sleeper, which is a capture through a pipe.
- **AC6** — When the card is written over the AC1 remote, `git rev-parse HEAD`, `git for-each-ref
  refs/heads refs/remotes` and the absence of `FETCH_HEAD` in the fixture's git dir are unchanged.
  Red when: the read moves a branch or remote-tracking ref, or writes `FETCH_HEAD`.
- **AC7** — When `bash tools/check-install-prefix.sh` runs after the edit, it names no line of
  `skills/session-kickoff/manifest-check.sh`.
  Red when: the engine spells the unattended kit's path.
- **AC8** — When `git diff --name-only 5266d22e -- skills/session-kickoff/` runs on the built tree,
  it lists `skills/session-kickoff/manifest-check.sh` and its self-test and nothing else, so
  `tools/check-wiring.sh` Check S compares the same three files; after the landing,
  `bash tools/check-wiring.sh` run in the primary tree prints `ok       skill`.
  Red when: a new engine file appears that the installed-engine comparison does not cover.
  permission: the post-landing half is observed by the main loop on the primary tree.
- **AC9** — When `bash tools/check-kit-versions.sh` and `bash skills/session-kickoff/manifest-check.sh`
  run after the re-stamp, both exit 0, and `python tools/govkit/govkit.py epoch --base 5266d22e`
  names no kickoff-manifest carrier left behind.
  Red when: the engine moved without its version or the manifest's watch stamp.
- **AC10** — When the card is written on node `a` with and without the cell, both wall times are in
  the unit's acceptance ledger; and `--card --replay --session t2` with the fixture's remote URL
  broken prints the stored `claims —` head unchanged.
  Red when: either figure is missing, or the replay reads the remote.
  figure: PINNED at the build pass, with the date and node.

## 7. Gates

`kickoff-manifest ratchet` · `manifest-check self-test` · `scratch-guard self-test` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `kickoff engine size <=18KiB` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: skills/session-kickoff/manifest-check.test.sh · the seven-claim remote, the missing conf,
the broken remote, the slow driver and the replay, each staged by reverting its branch · the
suite's floor rises by its new arm count

## 8. Open questions

- **F1 — Does the card keep KICK-aReplayedCard-1's "never contacts a remote"?** That clause's
  reasons were that a fetch mutates local refs from a hook nobody asked, inside a hook timeout, and
  that the fast-forward belongs to the engine's Step 1. The roster this build's owner authorized
  asks the card for the remote's claims, which no local file holds.
  RESOLVED (agent, 2026-10-04, delegated): one bounded read through the driver, which moves no
  branch or remote-tracking ref and writes no `FETCH_HEAD`, recorded as a narrowing row in
  `memory/DECISIONS.md`; the fast-forward stays Step 1's.
- **F2 — What is the second clock?** The README roster names three states, live, stale and
  hidden; the brief pins the driver's verdicts. A multiple of the stale bound needs a second reader
  of that bound; no second clock overflows the card cap as terminal claims accumulate.
  RESOLVED (agent, 2026-10-04, delegated): a card constant of one day, hiding `stale` and
  `terminal` claims older than it and never hiding `live`, `held` or `unknown`, since those want a
  reader whatever their age.
- **F3 — How does the engine reach a sibling kit's driver?** A typed path breaks every adopter
  installed at another prefix; a second copy of the id reader's three rungs is a second spelling.
  RESOLVED (agent, 2026-10-04, delegated): the id reader's body becomes `resolve_kit_file`, called
  for both kits.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the spec brief's unit 2 and the engine at base
  `5266d22e`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "the session start orientation card shows a line derived
from another kit"` ranked `resolve_kit_dir` as a seam and printed `unscanned layers: .sh`, so the
engine's own shell functions were invisible to it. The seams extended were found by reading the
engine at base: the `live —` cell's `skipped:` shape, `resolve_id_reader` and the inlined
`resolve_kit_dir` for the sibling lookup, and `CARD_CAP_BYTES` as the precedent for a constant
with a self-test override. The recall probe returned the card's own design (KICK-aReplayedCard-1),
whose no-fetch clause §8 F1 narrows, and the stdin fix that set the session id's precedence
(TOOL-cMendedVintage-9), which this unit does not touch.

Recall terms used: orientation card SessionStart live line skipped sibling resolver resolve_kit_dir receipt corpus_ids no fetch byte cap

The question passed with them: "why does the orientation card avoid fetching at session start, and
how does it reach a sibling kit's file".
