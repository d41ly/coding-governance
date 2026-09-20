# TOOL-aWokenSentinel-8 — the stop-guard's `landing-unstamped` row: a bound session at `FINISHED-UNSTAMPED` is blocked and told to run `--landed`

**Status:** CLOSED · rev-3 · 2026-09-20 · node a · Tier-2 · base 12b3701d · streams tooling · order 8 · ratified 2026-09-20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-build-TOOL-aWokenSentinel-8-1-acceptance-ledger.md](../build/2026-09-20-build-TOOL-aWokenSentinel-8-1-acceptance-ledger.md) | journal | — |
| [2026-09-20-prompt-TOOL-aWokenSentinel-8-1-build-brief.md](../prompts/2026-09-20-prompt-TOOL-aWokenSentinel-8-1-build-brief.md) | journal | — |
| [2026-09-20-review-TOOL-aWokenSentinel-8-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-8-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 |

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding B1 (round 1, raw ids 18, 29 and 43): `TOOL-aWokenSentinel-7` refuses `--landed`
until a stop-guard line recorded in phase `LANDING` exists and tells the session to END THE TURN so
the stop-guard "records the listing and continues you", but `--landed` runs after the lander, so at
every point that refusal fires the witness is already on `origin/<default>`, `--liveness` grades it
`FINISHED-UNSTAMPED`, and `TOOL-aWokenSentinel-3`'s decision table ALLOWS that stop. The turn ends,
nothing resumes the session, and the record sits at `LANDING` with its work on `main` — the
six-records defect the build cites, manufactured by the unit built to close it. This unit changes
the design: the stop-guard BLOCKS a bound session whose run is `FINISHED-UNSTAMPED`, bounded like
every other block, with a reason that names `--landed` as the one act left. The continuation the
remedy promises is then a row the table performs.

## 2. Scope (IN)

- **S1** — In `tools/unattended/stop-guard.js`, the decision row for verdict `FINISHED-UNSTAMPED`
  changes from `allow · finished-unstamped` to BLOCK with reason class `landing-unstamped`, under
  the same `background_tasks` allow and the same `STOP_GUARD_BLOCKS` cap as the `run-open` row, so
  the block is bounded by the count the sidecar already derives. Observed by AC1, AC2 and AC3.
- **S2** — The block reason for that row is a distinct text: it says the run is landed on the
  default branch and unstamped, that the stop-guard has just recorded the harness's cron listing,
  and that the one act left is `bash <kit-rel>/unattended.sh --landed <slug>`; it names neither
  `--plan` nor `--abort`, because a finished run has no unit to build and nothing to abort. Observed
  by AC1.
- **S3** — The reason class joins the hook's `REASONS` constant and the sidecar line grammar
  unit 3 states, so the `reason` field of a line written on this row is `landing-unstamped` and the
  line carries `session_crons` verbatim as every line does — the listing `--landed` reads next.
  Observed by AC1.
- **S4** — The hook's header states the row and why it exists: the `--landed` refusals of unit 7
  end the turn on the promise that this row continues the session, and an allow here is the wedge
  B1 names. Observed by AC4.
- **S5** — The suite's stub-driver arm for `FINISHED-UNSTAMPED` asserts the block, the reason text
  and the sidecar line; a second payload with the cap reached asserts `blocks-exhausted`; each is
  observed RED first against the hook with the row reverted to allow. Observed by AC1, AC2 and AC3.
- **S6** — `verdict: FINISHED-UNSTAMPED` remains an ALLOW for an UNBOUND record by construction —
  the hook never reaches its table for a session no record names — so every pre-unit-1 record at
  `LANDING` in this tree, none of which carries a `session:` fact, keeps ending its turns silently.
  Observed by AC5.

## 3. Non-goals (OUT)

- **No change to `--landed`'s refusal texts or to its read.** Unit 7 owns the verb; this unit makes
  its remedy true. The integration arm that drives refusal, stop, block and re-run to `LANDED` is
  unit 7's S8, which consumes this row and is sequenced after it.
- **No change to `--liveness`.** `FINISHED-UNSTAMPED` keeps unit 2's offline definition: phase
  `LANDING` and a sha-shaped witness that is an ancestor of the local `refs/remotes/origin/<d>`
  where that ref exists. A lander's push moves that ref, which is why the verdict is what a stop
  after the lander reads.
- **No new knob.** The block is bounded by `STOP_GUARD_BLOCKS`; a run whose reap cannot happen is
  blocked at most that many times and then allowed with `blocks-exhausted`, announced on the line,
  which is the same ceiling every other block has.
- **No prose carrier.** The protocol's section 5 and the Skill are unit 6's; unit 6 names the
  stop-guard by trigger and this row needs no sentence there. The hook's header is the documentation.
- **No `TERMINAL` change.** A `LANDED` record's stop allows; after `--landed` succeeds the next
  stop is silent, which is the exit of the loop this row opens.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-3` — the hook, its decision table, `measureBlocks`, the
  sidecar line grammar and the stub-driver fixture, and through unit 3's own edge on unit 2 the
  `verdict: FINISHED-UNSTAMPED` vocabulary with its offline ancestry test against the local
  remote-tracking ref. Without the hook there is no row to change, and without the verdict the
  row never selects; the row is provisional in unit 3's table at its order and replaced here one
  order later.
- **consumes-from** `TOOL-aWokenSentinel-16` — check 34 accepting the `--no-ff` landing the
  charter mandates: the marker's commit contains the witness and sits on the remote default
  branch, so step 3 of the loop below reaches `LANDED` from the run worktree. Without it every
  re-run on that landing shape refuses (OPEN `TOOL-dUnstalledConvoy-38`), each refusal spends one
  block of the shared budget, and the record wedges at `LANDING` by a longer route — audit H1.
- **hands-off** `TOOL-aWokenSentinel-7` — the integration arm over the driver suite's `--landed`
  fixture: refusal, one Stop payload through the real hook and the real driver, the block with
  this reason, the sidecar line in `LANDING`, and `--landed` re-run to `LANDED` without a second
  turn. Unit 7 owns the refusal and therefore the arm.

## 4. Design

### The decision, amended

The table unit 3's §4 states, with the one row moved. The first matching row wins.

| verdict from `--liveness` | `background_tasks` | blocks so far | decision | reason class |
|---|---|---|---|---|
| `TERMINAL` | any | any | allow | `terminal` |
| `FINISHED-UNSTAMPED`, `LIVE`, `STALE` or `UNBOUND` | non-empty | any | allow | `background-tasks` |
| `FINISHED-UNSTAMPED`, `LIVE`, `STALE` or `UNBOUND` | empty or absent | at or above `STOP_GUARD_BLOCKS` | allow | `blocks-exhausted` |
| `FINISHED-UNSTAMPED` | empty or absent | below | BLOCK | `landing-unstamped` |
| `LIVE`, `STALE` or `UNBOUND` | empty or absent | below | BLOCK | `run-open` |
| no `verdict:` line, non-zero exit, or the liveness bound | any | any | allow | `liveness-unreadable` |

`checkStop` gains one branch; `measureBlocks` counts a `landing-unstamped` line as a block because
its `decision` is `block`, so the cap needs no second counter. The `REASONS` constant gains the
class. Nothing else in the hook moves.

### Why a BLOCK is the right answer for a bound session

The `allow` row was written for the records in this tree at base: the non-terminal records whose
runs finished without a stamp, none of which carries a `session:` fact — the count is derived by
AC5's grep at observation, never typed here. Those never reach the table, because `resolveLease`
binds by session and an absent fact binds nothing. The
only session that reaches this row is one that HOLDS a run whose work is already on the default
branch and whose record still says `LANDING`, and the one thing such a session must do before it
ends is `--landed`. Allowing its stop is allowing the wedge; blocking it, once per stop and bounded,
is the resume this build exists to provide, at zero API cost and inside the turn.

The loop this closes, traced against unit 7's refusals with the sidecar wired and the session bound:

1. `--close`, commit, the lander pushes `main` — a `--no-ff` merge whose sha the marker records
   while the run worktree's HEAD stays the merge's second parent — and `--landed` runs. Check 34
   accepts that shape through unit 16 (before it, `TOOL-dUnstalledConvoy-38` refused every such
   re-run and the recorded workaround was a fast-forward of the run branch onto the merge). The
   newest stop line predates the close, so unit 7's second refusal fires: END THE TURN once, re-run
   `--landed`.
2. The session ends its turn. The hook binds, `--liveness` reads `FINISHED-UNSTAMPED`, this row
   BLOCKS, and the sidecar gains a line in phase `LANDING` carrying the harness's `session_crons`
   VERBATIM — written before the decision is printed, as unit 3's order of work has it.
3. The session continues and re-runs `--landed` in the SAME worktree. The newest line is in
   `LANDING`; the id is absent from the listing, so the verb prints `checked` and stamps `LANDED`;
   or the id is present, unit 7's first refusal names the reap, the session reaps, ends the turn,
   and step 2 repeats with a listing that no longer names the id. The clone-shared marker's
   overwrite by a concurrent landing (`TOOL-aUnblockedFleet-7`, OPEN) is tolerated by unit 16's
   predicate when the later landing contains this one, and refuses otherwise, costing one block.
4. After `LANDED` the next stop reads `TERMINAL` and allows silently.

Every iteration costs one block and the count is bounded by `STOP_GUARD_BLOCKS`, which every
block row shares, so a reap the harness never reflects — or a `--landed` refusal for any other
reason, each of which costs one block per turn — ends in `blocks-exhausted`, announced, rather
than a loop.

### The block reason

```
stop-guard: this session holds unattended run <slug>, phase LANDING, and its witness is already on
the default branch, so the run is finished and unstamped; block <n>/<N>. The stop-guard has just
recorded the harness's cron listing. Run `bash <kit-rel>/unattended.sh --landed <slug>` now: it
reads that listing against the recorded keepalive id and stamps LANDED, or names the reap still
owed. Never end the turn by asking.
```

`<kit-rel>`, `<n>` and `<N>` are derived exactly as in the `run-open` text; the
`stop_hook_active` trailing sentence is appended on the same rule. The text is one literal in the
hook beside the `run-open` literal; `renderBlock` selects by reason class.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `landing-unstamped` | reason class, a string in `REASONS` and on the sidecar line | no cell |

No function is minted; `checkStop` and `renderBlock` gain a branch each. Cell `js.function camel`
is unmoved.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/stop-guard.js` | the row in `checkStop`, the literal in `renderBlock`, the class in `REASONS`, the header paragraph |
| `tools/unattended/stop-guard.test.sh` | new arms: the `FINISHED-UNSTAMPED` block payload, the cap payload, the background-tasks payload and the unbound payload — spec 3 arms no allow row for this verdict at its order, so nothing is rewritten |

### Alternatives rejected

- **Mandate a turn boundary between `--close` and the lander** (the audit's option b). It moves
  the promise into the Skill's prose, where nothing checks it, and a session that lands in one turn
  still wedges; the row makes the order irrelevant.
- **Return to the brief's `unchecked` pass** (option c). It closes B1 by making unit 7 check
  nothing on the ordinary landing, which is the defect `TOOL-aPromptedMandate-11` records.
- **A phase-aware row that blocks only when the newest stop line is not in `LANDING`.** After the
  first block the newest line IS in `LANDING`, so the second iteration — reap, end the turn — would
  be allowed and the record would wedge with the id reaped and no stamp. The row must block on the
  verdict alone and let `--landed` decide; the cap bounds it.
- **A separate, smaller cap for this row.** A second knob for one row; `STOP_GUARD_BLOCKS` already
  bounds every block and the count is one file.

## 5. Production-readiness checklist

- security — no new input, no new write; the hook writes the same sidecar line and prints a
  different reason. A forged `LANDING` record with a witness on `main` is blocked at most
  `STOP_GUARD_BLOCKS` times, then allowed.
- perf / scale — none; one branch in a hook that already ran the driver.
- error / empty / loading states — an unreadable liveness still allows; a reached cap still allows
  with `blocks-exhausted`; an unbound session never reaches the row.
- observability — the reason text names the phase, the verdict, the count and the one verb; the
  sidecar line names the class.
- risks — the harness's own consecutive-block cap (see unit 3 §4 as folded at rev-2) ends a turn
  before `STOP_GUARD_BLOCKS` where the knob sits above it; the count persists in the sidecar so the
  hook's cap still binds across turns. The budget is SHARED with the `run-open` row, and a
  `--landed` refusal of any kind costs one block per turn. A landing whose `--landed` keeps
  refusing for a reason other than the reap — a dirty tree, an anchor mismatch — is blocked up to
  the cap and then allowed, and every block's reason text told the session which verb to run and
  what it printed. The check-34 refusal on the mandated `--no-ff` landing shape was that case for
  EVERY wired landing until unit 16 (`TOOL-dUnstalledConvoy-38`), which is why that unit is
  sequenced before this one.
- testing — §6, each arm against the copied hook and the stub driver, in milliseconds; the arm
  against the real driver is unit 7's.
- migration — additive; a reason class the pre-unit-8 hook never wrote.
- user docs — none; the hook's header, and unit 6's contract already names the stop-guard.

## 6. Acceptance criteria

`KIT`, `FIX`, `P` and `HOOK` are unit 3's §4 fixture paragraph's: a copied hook, a stub driver that
prints the file `$STOP_GUARD_TEST_LIVENESS` names, and a scratch tree with one bound record. Each
observation is one payload fed to the hook.

- **AC1** — When `FIX`'s record carries `session:` equal to `P`'s and the stub's liveness file holds
  `phase: LANDING` and `verdict: FINISHED-UNSTAMPED`, `printf '%s' "$P" | node "$HOOK"; echo "rc=$?"`
  prints `rc=0`, stdout is one JSON object with `decision` equal to `block` and a `reason` carrying
  `finished and unstamped`, `--landed` and `block 1/`, and not `--plan`; the sidecar's new line has
  `decision` `block`, `reason` `landing-unstamped`, `phase` `LANDING` and `session_crons`
  deep-equal to `P`'s, parsed with `python -c 'import json,sys;…'`. Observed RED first against the
  hook with the row reverted to allow.
  Red when: the stop is allowed, which is the wedge B1 names; or the reason tells the session to
  `--plan`, which sends a finished run to build nothing; or the line omits the listing.
- **AC2** — When the sidecar is pre-seeded with two `landing-unstamped` block lines for this
  session and `FIX`'s conf declares `STOP_GUARD_BLOCKS="2"`, the same invocation allows with
  `reason` `blocks-exhausted`; with one seeded line it blocks with `block 2/2` in the reason.
  Red when: the third stop is blocked, which is an unbounded loop on a run whose reap the harness
  never reflects.
- **AC3** — When `P` carries a non-empty `background_tasks` array and the liveness is
  `FINISHED-UNSTAMPED`, the invocation allows with `reason` `background-tasks`.
  Red when: a pending task's completion is blocked, which spends a turn to arrive where the harness
  was going.
- **AC4** — When `grep -c 'landing-unstamped' stop-guard.js` runs at the tip it
  prints at least 4 — the `REASONS` entry, the `checkStop` branch, the `renderBlock` selector and
  the header sentence — and prints 0 at this unit's base; the leading comment block alone, cut
  with `awk` at the first line that is not a comment, carries `landing-unstamped` at least once
  and 0 times at base; `grep -c 'finished-unstamped' stop-guard.js` prints 0.
  Red when: the old class survives, which is two rows for one verdict; or the header does not name
  the row, which leaves the next reader to rediscover B1 — observable only over the comment block,
  because the three code carriers satisfy the whole-file count on their own.
  figure: 4 and the header count are DERIVED by the greps at observation; 0 at base is PINNED as
  read from unit 3's spec.
- **AC5** — When `FIX` holds a record at `LANDING` with `session: absent` and the liveness file
  holds `verdict: FINISHED-UNSTAMPED`, a payload with any `session_id` prints `rc=0`, empty stdout,
  and writes no sidecar line; and `grep -L '^session: '` over every `RUN.md` under the memory
  tree's builds at the tip lists each record at a non-terminal phase, so the population this row
  never reaches is derived at observation rather than typed.
  Red when: an unbound finished record is blocked, which traps every owner session on this node
  for every such record the grep lists.
  figure: the record count is DERIVED by the grep at observation; no integer is written here.

## 7. Gates

`hook destinations (every declared hook path ships)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The pass runs none of these; it verifies with the payloads §6 names against the copied hook, and
the bar runs once at the close.

New arm: tools/unattended/stop-guard.test.sh · the `FINISHED-UNSTAMPED` payload against the stub driver with the row reverted to allow, the cap payload, the background-tasks payload and the unbound payload · `FLOOR_ASSERTIONS` rises by the arms' executed assertions

## 8. Open questions

- **F1 — which of the audit's three resolutions closes B1.** (a) The table row, this spec. (b) A
  mandated turn boundary between `--close` and the lander. (c) The brief's `unchecked` pass.
  RESOLVED (agent, 2026-09-20, delegated): (a). It satisfies unit 7's stated goal on every wired
  landing and leaves no follow-up; (b) leaves the promise in prose and (c) fails unit 7's own AC2
  and non-goal. Vetoes: no new dependency, surface or governance carrier; no widened write surface;
  the run-state file names the mandate and M3 delegates the forks the build's specs state.

## 9. Revision log

- rev-3 · 2026-09-20 · S6 · §3 · §4 · §5 · AC4 · AC5 · folded spec-audit round 2: sibling
  agreement for the promoted `TOOL-aWokenSentinel-16` (H1, raw 48) — the loop trace names the
  `--no-ff` landing shape, unit 16's check-34 predicate and the two OPEN rows
  `TOOL-dUnstalledConvoy-38` and `TOOL-aUnblockedFleet-7`, §5 says the block budget is shared and
  a refusal costs one block per turn, and §3 consumes unit 16; M1 (raw 6) — AC4's `grep -c`
  threshold was met by the three code carriers alone, so the header is now observed over the
  comment block cut with `awk` and the whole-file count names `renderBlock` as the fourth carrier;
  L1 (raw 27) — Files touched named an allow arm spec 3 never builds and omitted the
  background-tasks arm, so the row lists the four new payloads §7 names; L4 (raw 45) — "six
  records" was a typed count of a derived population and wrong at base, so S6, §4 and AC5 state
  the property and AC5 derives the count by grep. Order 6 → 8 for unit 16's insertion.
- rev-2 · 2026-09-20 · §3 · two edge-join findings from check 12: the `hands-off` bullet on unit
  6 declared an absence, which the join reads as an edge with no reciprocal, and is dropped
  because the `No prose carrier` non-goal already holds the fact; the `consumes-from` bullet on
  unit 2 had no `hands-off` back in spec 2, which this writer does not hold, so the verdict
  dependency is folded into the unit-3 bullet, unit 3 declaring its own reciprocated edge on
  unit 2. Observed by the full `check-memory-hygiene.sh` run over the tree at 12513c25.
- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 1 as the
  promotion of B1 (raw ids 18, 29, 43).

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "block a stop when the run is finished but its landed
stamp is missing and tell the session to run landed"` ranked the `run` name stem across thirteen
Python files and no hook seam, and reported `unscanned layers: .sh`; the map does not index kit
`.js` decision tables either, so no existing seam fits and the seam is unit 3's own table, cited
by section: `checkStop`, `renderBlock`, `measureBlocks` and `REASONS` in
`tools/unattended/stop-guard.js` as spec 3 §4 names them, and `is_terminal` with the offline
`finished-unstamped` test at `tools/unattended/unattended.sh:613` and `:1372` to `:1392` that unit
2 reuses. The recall probe's top hit is `TOOL-dUnstalledConvoy-38`, `--landed` evaluating its
idempotence guard after its own write, which binds unit 7; its second is this build's own audit
record at the B1 paragraph; `TOOL-aFusedCharter-4` records that three builds once sat at `LANDING`
together, the population the allow row was written for and this row never reaches.

Recall terms used: `finished-unstamped LANDING witness ancestor landed stamp stop hook block continue keepalive-reaped attestation wedge`
