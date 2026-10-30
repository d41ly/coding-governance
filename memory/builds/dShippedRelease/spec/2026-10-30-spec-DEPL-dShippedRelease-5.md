# DEPL-dShippedRelease-5 — the `deploy.released` wait: `build.release-ceiling` as its deadline and the release hold's one owner item

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 15 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0508@68f388b5 whole
**Carries:** node:item.deploy.released
**Carries:** node:policy-key.build.closes
**Carries:** node:policy-key.build.release-hold
**Carries:** node:policy-key.build.release-ceiling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-1-reuse-scout-a.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-reuse-scout-a.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-4 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |

<!-- /gen:spec-records -->

## 1. Goal

A build closed under `build.closes: after-release-verifies` waits for the release slot's exit record with a
real deadline. This unit arms that wait on dWellOiledMachine's one sweep: past `build.release-ceiling` the
owner gets the release hold's one item, and a build whose supervisor died after `deploy.land` and before
`deploy.unlease` can still be taken over and closed by a second node.

## 2. Scope (IN)

**Build-run preconditions**, each specced and unbuilt at this base: `declare_wait`, `WAIT_KINDS`,
`WAIT_OUTCOMES` and the sweep (TOOL-dWellOiledMachine-18); `raise_owner_item` and `OWNER_ITEM_KINDS`
(TOOL-dWellOiledMachine-48); `read_first_seen` (TOOL-dPlacedRequest-17 S1); `write_gov_ref` and
`build_gov_commit` (TOOL-dPlacedRequest-11); `read_landing` (DEPL-dShippedRelease-1); `run_unlease` and the
walk `--deploy run` (DEPL-dShippedRelease-4); and the `release-exit` record (DEPL-dShippedRelease-15). Exit
records are planted until unit 15's run lands. Lease keeping is pin C4, owned by unit 4; this unit observes
it.

- **S1** — The item. `run_deploy_released(slug, sha, root)` in `tools/loop/deploy_items.py`, reached as
  `unattended.sh --deploy released <slug> <sha>`, reads the landing record's `closes` field, the value in
  force at landing. Under `at-landing` and `at-landing-maintain-owns` it prints
  `released — <sha8> · pass · <value>` and exits 0, the landing record its witness. Under
  `after-release-verifies`, with no `release.environments` listed or the integrations kit absent, the key
  `policy-file.on-missing-expansion` decides: `refuse` exits 2 naming the key and what is missing,
  `fallback-reported` passes with one report line. Otherwise S2 to S5 run. The `item.deploy.released` row of
  `tools/loop/loop.toml` gains `outcomes` `pass`, `waiting`, `verified` and `closed-unreleased`, and its
  `[[stand-in]]` row leaves. Observed by AC1, AC2.
- **S2** — The rows. `WAIT_KINDS` in `tools/runtime/waits.py` gains two kinds with one `wake`:
  `deploy.released`, default outcome `release-hold`, on the prefix `refs/gov/release-exit/`, and
  `release-hold`, default outcome `release-hold`, on the prefix `refs/gov/mail/<build>/`, which an owner's
  answer moves. `WAIT_OUTCOMES` gains `release-hold`, not `holder-only`, since by then the build may have no
  holder. `OWNER_ITEM_KINDS` gains `release-hold`, with options `close-unreleased` and `keep-waiting`,
  recommended `keep-waiting`. No sweep, tick or clock is added: `sweep_waits` raises this wait as it raises
  any. The `wake` runs `python <loop kit>/deploy_items.py released-wake <build> <sha>`, the loop kit found
  through the inline `resolve_kit_dir`. Observed by AC3, AC4.
- **S3** — The clock (§8 F1). `derive_release_clock(build, sha, root)` returns the seconds left of
  `read_policy_value("build.release-ceiling", root)` hours, counted from the owner's last `keep-waiting`
  answer where S4's chain holds one, else from the landing record. Each anchor's elapsed time is the
  earliest `read_first_seen` over that ref's chain, the observer clock of TOOL-dPlacedRequest-17, after one
  `add_feed_sightings` over it. An anchor no feed has sighted counts nothing elapsed, so a deadline is never
  shortened by a missing sighting. The wait is declared with those seconds, at least 0. Observed by AC5.
- **S4** — The answers' chain. `refs/gov/release-hold/<build>/<sha>`, one commit per answer built by
  `build_gov_commit` and written by `write_gov_ref` on the tip read, its message the header
  `gov-release-hold <build>/<sha>` and the keys of §4. `write_hold_answer` is its one writer, re-reading and
  re-applying on a lost compare-and-swap, three attempts at most. `read_hold_answers(build, sha)` is its one
  reader. `measure_keep_waiting(build, sha)` prints the number of `answer: keep-waiting` commits, shared
  interface I14. A decision past `run.owner-deadline` counts as an answer, so a silent owner is counted too.
  A ref per (build, SHA) survives the mailbox's close, and a create-only decision ref could hold one answer
  only. Observed by AC6.
- **S5** — The wake, `run_released_wake(build, sha, root)`, state-driven and re-runnable, so a spurious wake
  costs one read. (1) `read_release_exit_for(sha, root)` lists `refs/gov/release-exit/*` and takes the
  newest exit record whose SHA contains `<sha>`, `git merge-base --is-ancestor` deciding; an exit for an
  unrelated SHA is ignored. A `verified` one writes `answer: verified`, with `exit-id`, `environment` and
  `outcome`, and runs the walk, `--deploy run <slug> <sha>`, which re-runs the idempotent items through to
  `deploy.close`. Any other outcome goes to (3). (2) An answered item writes its answer: `close-unreleased`
  runs the walk, the outcome on the transition; `keep-waiting` re-declares the wait by S3. (3)
  `raise_release_hold(build, sha)` raises the item, then declares the `release-hold` wait. (4) Otherwise it
  re-declares `deploy.released` with the seconds S3 gives, so the clock survives a wake that ended the wait.
  Observed by AC3, AC6, AC7.
- **S6** — One item. `raise_release_hold` calls
  `raise_owner_item("release-hold", build, ["close-unreleased", "keep-waiting"], "keep-waiting", key=<sha12>-<n>)`,
  `<n>` being `measure_keep_waiting` plus one. The mailbox's duplicate rule then makes a second raise print
  `owner item — already open`, while an answer moves `<n>` so a later ceiling opens a new item. It runs from
  the outcome at the ceiling and from S5, one function for both routes. Observed by AC3.
- **S7** — `build.release-hold`. `test_release_held(sha, root)` reads
  `read_policy_value("build.release-hold", root)` and sets `--deploy released`'s exit while it waits. Under
  `close-only` it exits 0 printing `released — waiting · close held`, so the walk `run_deploy_items`
  (DEPL-dShippedRelease-4 S1) goes on to `deploy.snapshot` and `deploy.unlease`. Under `whole-close` it
  exits 3, which the walk reads as held, so the snapshot, the leases and the mailbox stay as they are, since
  `item.deploy.released` precedes both in table order. `check_released`, the term of `deploy.close` that
  unit leaves for this one, gains the `after-release-verifies` arm: it holds only once `read_hold_answers`
  ends in `verified` or `close-unreleased`. Observed by AC8.
- **S8** — The killed supervisor. No new code beyond S1 to S7: pin C4 keeps the build lease live through the
  landing, and `run_deploy_released` is idempotent, so a second node that takes the lease over re-runs the
  items by `--deploy run` and reaches `deploy.unlease` and the close. Observed by AC9.
- **S9** — The three keys. `build.closes`, `build.release-hold` and `build.release-ceiling`
  (`tools/policy/catalogue.toml:1064`, `:1070`, `:1076`) each gain `summary` and `usage`, each name drained
  from `tools/policy/unsummarised-keys.txt` by `policy.py lists --write`, no second row added, allowed
  values and defaults verbatim. Their literal readers are `read_policy_value("build.closes", root)` in unit
  1's `--deploy record` and the two named in S3 and S7. Observed by AC10.
- **S10** — The docs: `help/deploy.md` gains the hold, the ceiling and the two answers; `help/runtime.md`'s
  waits section gains the two kinds; `tools/unattended/VERBS.template.md`, rendered to
  `memory/guides/UNATTENDED-VERBS.md`, gains `--deploy released`. NOT OBSERVED by a criterion: prose, read
  by the memory hygiene leg at the close.

## 3. Non-goals (OUT)

- No exit record and no `release.*` program: DEPL-dShippedRelease-15's, and this unit only reads
  `release-exit`.
- No parking: the third keep-waiting answer's rule is DEPL-dShippedRelease-30's. This unit counts.
- No lease write: pin C4 and `run_unlease` are DEPL-dShippedRelease-4's.
- No second close and no new close term: `deploy.close` is unit 4's, and this unit extends its
  `check_released`.
- No new notification channel: `raise_owner_item` pushes through the point TOOL-dWellOiledMachine-48 S7
  owns.
- No change to `waits.py`'s sweep, deadline or wake, and no `after-release-verifies` under an absent kit:
  the key `policy-file.on-missing-expansion` decides.

### Edges

- **consumes-from** `DEPL-dShippedRelease-1` — `read_landing`, the anchor the wait counts from and the `closes` field
- **consumes-from** `DEPL-dShippedRelease-4` — `run_unlease`, the walk and `check_released`, without which a passed wait closes nothing
- **consumes-from** `DEPL-dShippedRelease-15` — `release-exit`, the record that wakes the wait
- **hands-off** `DEPL-dShippedRelease-30` — `measure_keep_waiting`, the count its third-answer rule reads
- **consumes-from** external — TOOL-dWellOiledMachine-18's waits, -48's owner items and TOOL-dPlacedRequest-17's clock, each specced and unbuilt at base `f4597719`

## 4. Design

### Evidence

- TOOL-dWellOiledMachine-18 §3 reads "dShippedRelease declares `deploy.released`'s wait kind, its deadline
  `build.release-ceiling`, and its keep-waiting count", and its S7 says each later kind joins in its own
  unit, TOOL-dWellOiledMachine-47 being the precedent for a later outcome.
- That unit's S5 raises only an `open` wait and counts from the declaration's first sighting, its S3 wakes
  on any move of a prefix, and its S6's `owner-item` offers `keep-waiting` and `default`. Scout A's
  disagreement 9 reads these as three misfits. Each is met here by the extension points the unit leaves, so
  none needs a parent change: a new outcome row carries the two options, S5 re-declares after a spurious
  wake, and S3 here declares the seconds left rather than the whole ceiling.
- `verb_park` (`tools/unattended/unattended.sh:12872`) needs a run-state file and refuses a terminal one
  (`refuse_if_terminal`), and -48 S4 parks through it. A landed build's item under `remind-then-park` or
  `wait` is therefore refused: §8 F3's ask.
- `--landed`'s terminal write is `tools/unattended/unattended.sh:6381-6384`, which pin C4 stops.

### The hold's chain

```
refs/gov/release-hold/<build>/<sha>    message:

gov-release-hold <build>/<sha>

answer: keep-waiting | close-unreleased | verified | parked
by: <session or the deciding witness>
exit-id: - | <exit record id>
environment: - | <E>
outcome: - | <the exit's outcome>
```

The witness the flow table asks of `deploy.released`, keyed by (exit record id, build), is the `verified`
commit. `parked` is written by DEPL-dShippedRelease-30. The namespace sits outside the door's four
coordination namespaces, as the wait refs do, because an answer here carries no authority beyond its item.

### The routes

| State | Route |
|---|---|
| `closes` is not `after-release-verifies` | pass |
| exit record `verified`, containing the SHA | `answer: verified`, the walk |
| exit record of any other outcome, containing the SHA | the item |
| no exit record, past the seconds S3 gave | the item, through the `release-hold` outcome |
| item answered `close-unreleased` | the walk, the outcome on the transition |
| item answered `keep-waiting` | the wait re-declared, the clock from this answer |
| a wake with none of these | the wait re-declared with the seconds left |

### Inventory

| Minted | Cell or kind |
|---|---|
| `run_deploy_released`, `run_released_wake`, `derive_release_clock`, `write_hold_answer`, `read_hold_answers`, `measure_keep_waiting`, `raise_release_hold`, `read_release_exit_for`, `test_release_held` | `py.function`, `deploy_items.py`, each OK from `lexicon.py --suggest` or put to it in the build pass |
| `deploy.released`, `release-hold` | `WAIT_KINDS` rows |
| `release-hold` | a `WAIT_OUTCOMES` row and an `OWNER_ITEM_KINDS` member |
| `refs/gov/release-hold/<build>/<sha>` | a ref namespace |
| `--deploy released`, `released-wake` | verbs |

`measure_keep_waiting` is the spelling of shared interface I14's proposed `count_keep_waiting`: the lexicon
refuses `count` on a population read and suggests `measure`.

### Rollout

Live at landing and inert by default: `build.closes` defaults to `at-landing`, so S1 passes at once.

### Files touched (estimate)

- `tools/loop/deploy_items.py`, `tools/loop/deploy_fixture.py`, `tools/loop/loop.toml`
- `tools/runtime/waits.py`, `tools/runtime/owner_items.py`
- `tools/unattended/unattended.sh`: `--deploy released`
- `tools/unattended/VERBS.template.md`, and its render `memory/guides/UNATTENDED-VERBS.md`
- `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`
- `help/deploy.md`, `help/runtime.md`

### Alternatives rejected

- **The count on the wait ref.** Each re-declaration appends an `open` commit, so the count looks free, but
  a spurious wake also appends one, and telling them apart needs a key TOOL-dWellOiledMachine-18 S1's fixed
  list lacks. Tested against S5's route (4), which re-declares with no answer.
- **The count in mailbox rows.** Under `close-only` the mailbox is closed and pruned before the first answer
  can arrive, so a reader over `--mail read` loses earlier answers. Tested against pin C5's order.
- **One exact `on` per SHA.** Declaring on `refs/gov/release-exit/<sha>` avoids a spurious wake and misses a
  later SHA that contains the landed one, which is the clause's other waker.
- **A `deadline-from` key on the wait.** It reads the landing record inside the sweep, a change to a
  parent's S5 for what remaining seconds give with no parent change.

## 5. Production-readiness checklist

- security: an answer on the hold's chain grants nothing but the item's outcome; the options are a closed
  pair checked by `owner_items.py`.
- perf / scale: one `git for-each-ref` over exit records per wake, one ancestor test per exit.
- error / empty / loading states: no exit, no answer and an unsighted anchor each read as still waiting, and
  a failed fetch is no answer.
- observability: `released —` lines, the wait's own `wait —` lines and the chain.
- risks: a wake may close late, since a wake runs only at a tick. A landed build's item under a non-default
  `run.on-owner-silence` is refused at the park (§8 F3). A post after the mailbox closed recreates a mail
  ref that nothing prunes (§8 F4).
- testing: planted exit records, planted answers and two clones, in `deploy_fixture.py`.
- migration: N/A — a default-inert wait.
- user docs: S10.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case released-pass` runs under a planted
  `.governance/policy.toml` reading `build.closes = "at-landing"`, then `"at-landing-maintain-owns"`,
  `--deploy released` prints `pass` and no wait is declared; under `"after-release-verifies"` it declares
  one, printing `wait — deploy.released`.
  Red when: a pass value declares a wait, or the wait is missing under the third.
- **AC2** — When `--case released-no-expansion` runs under `after-release-verifies` with
  `release.environments` emptied, `policy-file.on-missing-expansion = "refuse"` exits 2 naming the key, and
  `"fallback-reported"` passes with one report line.
  Red when: an emptied list waits forever, or passes silently.
- **AC3** — When `--case release-ceiling-twice` drives a planted `deploy.released` wait past its ceiling,
  the sweep raises one item, and a second pass of the ceiling while it is open prints
  `owner item — already open`, `--mail read project --open` listing exactly one `release-hold` row.
  Red when: the ceiling opens a second item while one is open.
- **AC4** — When
  `python waits.py declare deploy.released <sha> fx --on refs/gov/release-exit/ --seconds 0 --outcome release-hold`
  runs, it exits 0; `--outcome no-such` exits 2 before any write.
  Red when: a kind or outcome outside the tables is admitted.
- **AC5** — When `--case release-clock` plants `build.release-ceiling = 1` and a landing first sighted 40
  minutes ago, the wait declares at most 1200 seconds; after a planted `keep-waiting` answer it declares
  about 3600; and an unsighted anchor declares 3600.
  Red when: the clock restarts at the declaration, or a missing sighting shortens it.
  figure: 40 minutes and 1 hour are PINNED by the fixture; each read is within 60 seconds.
- **AC6** — When `--case keep-waiting-count` plants two `keep-waiting` answers,
  `python deploy_items.py measure-keep-waiting <build> <sha>` prints 2, a spurious-wake re-declaration
  leaves it at 2, and the count reads the same after `run_unlease` pruned the mailbox.
  Red when: a re-declaration counts, or closing the mailbox loses the count.
- **AC7** — When `--case released-exit` plants a `verified` exit for a later SHA that contains the landed
  one, the wake writes `answer: verified` with its `exit-id` and runs the walk; an exit for an unrelated SHA
  re-declares the wait with the seconds left; a `held` exit raises the item.
  Red when: an unrelated exit ends the wait, or a non-verified exit closes the build.
- **AC8** — When `--case release-hold-values` runs under `after-release-verifies`, a planted
  `build.release-hold = "whole-close"` exits `--deploy released` 3 and leaves the lease live and no
  snapshot, while `"close-only"` exits 0, the walk reaches a tombstone, and `--deploy close` prints
  `held · check_released`.
  Red when: `whole-close` releases the lease before the release answers, or `close-only` holds the unlease.
- **AC9** — When `--case killed-supervisor` lands a planted build, kills the holder between `deploy.land`
  and `deploy.unlease`, and a second clone takes the lease over and re-runs the items, `--claims` reads the
  lease live until then, and the build reads a terminal tombstone and a recorded close after, with one
  landing record.
  Red when: the lease reads terminal at `--landed`, so no second node can close the build.
- **AC10** — When `python policy.py get build.release-ceiling` runs with no file value it prints 72, a
  planted value 1 reads 1, and
  `grep -c -E 'build.(closes|release-hold|release-ceiling)' tools/policy/unsummarised-keys.txt` prints 0,
  each key holding a literal reader the reader-coverage arm counts.
  Red when: a row lacks `summary`, or no literal call reads it.

## 7. Gates

`policy fixtures` · `policy check` · `unattended kit gate` · `recall floor` · `recall floor arms`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 AC5 AC6 AC7 AC8 AC9 · each `--case` above, the failing case `release-ceiling-twice` with the duplicate rule bypassed · none
New arm: tools/runtime/waits_fixture.py · covers AC4 · a declaration naming `no-such` · none

## 8. Open questions

- **F1 — How does a clock "counted from the landing record or from the owner's last keep-waiting answer" fit
  a sweep that counts from a declaration's first sighting?** Options: (a) declare the seconds left, by the
  observer clock over the anchor; (b) a `deadline-from` key on the wait, a change to
  TOOL-dWellOiledMachine-18 S5; (c) count from the declaration and accept the drift. (c) fails the clause's
  word, and (b) moves a parent for what (a) gives. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3,
  scout A fork 7. widens: none · relaxes: none
- **F2 — Where do the answers live?** The count's store cannot be create-only decision refs (scout B F9).
  Options: (a) one chain per (build, SHA); (b) the wait ref; (c) the mailbox. §4 records (b) and (c)
  failing. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — An ask for dWellOiledMachine.** TOOL-dWellOiledMachine-48 S4 parks by
  `unattended.sh --park <build>`, which refuses a terminal run, so an item of a landed build cannot park
  under `remind-then-park` or `wait`. Ask, target dWellOiledMachine: accept `decide_owner_items` reads a
  refused park of a landed build's item as `held`, posting `--mail ack` with no `--park`, seen on a planted
  landed build under `run.on-owner-silence = "wait"`. RESOLVED (agent, 2026-10-30, delegated): the ask
  stands, filed by the main loop; the default `apply-recommendation` needs no park, so the unit builds
  without it. widens: none · relaxes: none
- **F4 — An ask for dKeptSession.** Under `close-only` the item is raised after `run_unlease` pruned the
  mailbox, so the post recreates a mail ref that the door lets no agent prune (TOOL-dWellOiledMachine-58
  S5). Ask, target dKeptSession: accept a post to a build whose mailbox closed either lands under a
  recipient-only ref or is pruned with its copy written, seen on a planted post after an unlease. RESOLVED
  (agent, 2026-10-30, delegated): the ask stands, filed by the main loop; the stray ref is harmless, and the
  answer's record is S4's chain. widens: none · relaxes: none
- **F5 — Must the wake be a parent change?** Scout A's disagreement 9 expected one. RESOLVED (agent,
  2026-10-30, delegated): no ask to TOOL-dWellOiledMachine-18 is owed, rung 1, its §3 and S7 leave these
  rows to this build, as §4 "Evidence" reads them. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, the spec run.

## 10. Reuse audit

The seam is `WAIT_KINDS` and `WAIT_OUTCOMES` in `waits.py` (TOOL-dWellOiledMachine-18 S6, S7) with
`OWNER_ITEM_KINDS` (TOOL-dWellOiledMachine-48), unbuilt at this base, extended by rows and never by a sweep.
`python tools/codebase-map/reuse_lookup.py "a keep-waiting answer counted per build and landed sha"` ranked
name-stem hits only (`counts`, `build_commit`), confirming no count exists at HEAD. Scout A's row stands
with two corrections read from source: `measure_keep_waiting` replaces the proposed name, and the misfits of
its disagreement 9 are met without a parent change, §4 says how. The recall hit TOOL-dWitnessedBar-30's
scout row concerns a different wait.

Recall terms used: release-hold deploy.released keep-waiting owner-item ceiling wait-kind sweep
landing-record lease unlease
