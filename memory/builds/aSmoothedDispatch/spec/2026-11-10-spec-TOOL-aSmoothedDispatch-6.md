# TOOL-aSmoothedDispatch-6 — a dispatched unit counts as routed, so its builder's product writes are not refused on a stale card route

**Status:** SPECCED · rev-1 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-1-brief.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-1-brief.md) | research | TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-5 |

<!-- /gen:spec-records -->

## 1. Goal

In dFairHearing the write gate refused builders' product edits 63 times, because the session card's
`## route` still named a CLOSED unit while the driver had dispatched the next one. This unit makes the
write gate in `tools/hooks/scratch-guard.js` count a unit that the build's run-state file records as
dispatched as routed, so the dispatch row is the one source of "this unit is being built now".

## 2. Scope (IN)

- **S1** — When no unit on the card's route is buildable, `checkRouted` reads the dispatch rows of
  the run-state file `RUN.md` in the folder of the build the route's `- build:` line names. Each unit
  those rows name that is not already on the card is judged by `checkBuildable`, against the spec
  under that build's `spec/` folder whose H1 names it. The first buildable one admits through step 9a,
  the role arm, exactly as a card-routed unit does. Observed by AC1 and AC4.
- **S2** — With no run-state file, or one holding no dispatch row, the refusal is byte for byte what
  it is today. With dispatch rows and none buildable, the refusal gains one line naming the run-state
  file and the count of dispatched units it judged. Observed by AC2 and AC3.
- **S3** — `renderRouteContext` reads the same dispatched units through the same function, and adds
  one line per BUILDABLE dispatched unit, so the SubagentStart context and the gate give one answer.
  Observed by AC5.
- **S4** — The H1 read inside `checkBuildable` moves into one function that both `checkBuildable` and
  the spec lookup of S1 call, so the two cannot read an H1 two ways. Observed by AC1 and AC3.
- **S5** — The run-state file name is one exported constant, `RUN_STATE_FILE`, and the hook suite
  compares it with the basename the driver's `runmd_of` spells. Observed by AC6.
- **S6** — The write gate section of `tools/hooks/README.md`, the `checkRouted` evaluation-order
  comment and the `renderRouteContext` comment state the dispatch fallback and what it does not check.
  Observed by AC7.

## 3. Non-goals (OUT)

- No change to `tools/unattended/unattended.sh`. `--dispatch` does not write the card. The driver
  holds no session id (no `session_id` or `CLAUDE_SESSION_ID` read anywhere in it), and the card lives
  at `<common dir>/orientation/<session id>.md`, so it cannot name the card to write.
- No JavaScript copy of the driver's pass-openness test (`check_pass_open`, which walks git for the
  pass commit). The hook reads "open" as "dispatched and its spec buildable", for the reason §4 gives.
- No dispatch rows read from any build but the one the card's `- build:` line names, and none from a
  rotated `RUN.LANDED.*` record.
- No change to the role arm, the spec-class arm, `BUILDABLE_STATUS`, or what a card route admits.
- No change to the card writer `skills/session-kickoff/manifest-check.sh`.
- No `help/` page. No page under `help/` describes the write gate. The only scratch-guard mention is a
  hook name in `help/step-gate.md:17`, and the kit's own page is `tools/hooks/README.md`, which S6
  updates.

### Edges

- **consumes-from** external — the dispatch row grammar the driver writes and its library reads,
  `<utc> dispatch · item <anchor> <unit> · reason <paths>` (`read_pass_declarations`,
  `tools/unattended/lib-unattended.sh:1117`). A grammar change there leaves this reader matching
  nothing, so the gate falls back to today's refusal and never admits more.
- **hands-off** external — TOOL-dWellOiledMachine-38 and TOOL-dScopedBuild-5, both DEFERRED, re-point
  or replace the write gate's card and route reads. Whichever builds after this unit must carry the
  dispatch fallback into its new reader.

## 4. Design

### What the tree does today, verified at `ae6735c1`

| Fact | Where |
|---|---|
| A Tier-2 unit admits writes only at INPROGRESS. | `tools/hooks/scratch-guard.js:796` |
| The route reader keeps one `- build:` value and every `- unit:` line. | `tools/hooks/scratch-guard.js:839` |
| `checkBuildable` reads the spec's H1 and status, and its H1 compare is inline. | `tools/hooks/scratch-guard.js:873`, `:895` |
| Step 9 loops the card's units only; the first buildable goes to `checkRoleWrite('product')`. | `tools/hooks/scratch-guard.js:1191` |
| The SubagentStart context gives one `checkBuildable` verdict per card unit. | `tools/hooks/scratch-guard.js:1470` |
| The driver's run-state file is the build folder's `RUN.md`. | `tools/unattended/unattended.sh:1540` |
| The driver's order gate matches a unit's dispatch row with an anchored regex. | `tools/unattended/unattended.sh:14378` |
| A unit's spec goes terminal in its own pass commit, and from then the guard refuses its writes. | the comment above `tools/unattended/unattended.sh:14098` |
| Two definitions of an open pass are named as the two-answers class. | the comment above `tools/unattended/unattended.sh:14129` |

The dFairHearing builders worked around the refusal by hand-appending a route with
`manifest-check.sh --card --append` (the builder returns of units 2 and 3, cited in §10). That second
write states again what the dispatch row already says.

### Which side keeps one source

The brief offers two mechanisms. `--dispatch` appending the unit's route to the card would make the
card a second copy of the dispatch row, and the driver cannot do it: it has no session id, so it
cannot locate the card. The hook reading the dispatch row keeps the row as the one source, and the
card keeps meaning what the kickoff routed. So the hook side is the mechanism.

### The dispatched units (S1, S4, S5)

One new function, `readDispatchedUnits(top, memRoot, build)`, returns `{ file, units }`. `file` is the
comparable path of `<top>/<MEMORY_ROOT>/builds/<build>/RUN.md`, and `units` is a list of
`{ unit, spec }` in first-appearance order, each unit once.

1. `build` empty, or the file absent or unreadable → `{ file, units: [] }`. A read error other than
   ENOENT is also an empty list: the fallback can only add an admission, so failing to read it must
   leave today's verdict standing.
2. Each line, `\r` stripped, matching
   `^\d{4}-\d{2}-\d{2}T[0-9:]+Z dispatch · item [0-9a-f]+ (\S+) · reason ` contributes its unit id.
   This is the order gate's own row match at `tools/unattended/unattended.sh:14378`.
3. With at least one id, the build's `spec/` folder is walked at any depth for `.md` files. Each file's
   H1 id is read by the S4 function, `readSpecH1Id(text)`, which is the block now inline in
   `checkBuildable`, moved verbatim. `checkBuildable` then calls it. A unit's `spec` is the repo-relative
   path of the first file whose H1 id equals it, spelled with the prefix `checkBuildable`'s `want`
   test accepts, or `''` when none does.

`RUN_STATE_FILE = 'RUN.md'` is a module constant and is exported. `readDispatchedUnits` is exported for
the suite.

### Step 9 (S1, S2)

After the card loop finds no buildable unit, and before the refusal, `checkRouted` calls
`readDispatchedUnits(top, memRoot.trim(), route.build)`. It skips every unit the card already routes,
since its reason is already listed. For each remaining unit, `checkBuildable(u, route.build, …)` is
asked in order. The first `''` admits through the same `checkRoleWrite('product', …)` call the card
loop makes, with the slug taken from the unit id the same way. A unit with `spec` `''` gets the reason
`the route line names no spec` from `checkBuildable` and is not buildable.

If none admits, the refusal is today's text. When `units` was not empty, one line is added under the
card reasons:

```
  the run-state file <file> records a dispatch for <n> unit(s) of <build>, and none is buildable
```

No per-unit reason is listed for dispatched units. A long run's file names dozens of CLOSED units, and
listing each would bury the card's own reasons.

### The SubagentStart context (S3)

`renderRouteContext` calls `readDispatchedUnits` with the same arguments once it has the card's route,
and only where the gate would reach step 9. For each dispatched unit not on the card for which
`checkBuildable` returns `''`, it adds one verdict line:

```
<unit> is buildable through its dispatch row in <file>, which scratch-guard counts as routed: <tier> at <status>.
```

These lines are budgeted against `ROUTE_CONTEXT_CAP` like a unit's verdict, after the route lines.
Non-buildable dispatched units are not listed, for the reason step 9 lists none.

### What "open" means here, and what this does not check

The hook does not ask whether the pass has committed. A pass's spec goes terminal in its own pass
commit, so "dispatched and buildable" holds exactly while the pass is open, as long as the run flips
the status in that commit. A run that commits a pass and leaves its spec INPROGRESS keeps admitting.
That is the exposure a card route to an INPROGRESS unit already carries.

Like a hand-written card, a dispatch row hand-appended to the run-state file is read as the driver's.
The guard stops forgetting, not evasion. The spec must still read INPROGRESS, and the role arm still
decides who writes.

### Inventory

| Minted name | Kind | Graded by |
|---|---|---|
| `readDispatchedUnits` | function, exported | the lexicon's `js` probe cell, verb `read` as `readCard` and `readConfKey` already use |
| `readSpecH1Id` | function | the same cell |
| `RUN_STATE_FILE` | constant, exported | the same cell |

### Files touched (estimate)

`tools/hooks/scratch-guard.js` · `tools/hooks/scratch-guard.test.sh` · `tools/hooks/README.md`

### Rollout

The hooks kit's version moves through the lander's `mint`, never by hand. Unit
TOOL-aSmoothedDispatch-5 adds rows to `tools/hooks/scratch-guard.test.sh` too, so the two units share a
write set and build in their declared order, 5 then 6. This unit touches no file of the driver, so it
is disjoint from units 1 to 4. The build README's build-level rule still lists unit 6 among the units
sharing `tools/unattended/unattended.sh`, and the build's committer owns that line.

### Alternatives rejected

- **`--dispatch` appends the route to the card.** The driver has no session id to locate the card, and
  the card would then hold a second copy of the dispatch row, with two writers.
- **A JavaScript port of `check_pass_open`.** It walks git history for the pass commit on every gated
  write, and it is a second definition of "open", the class the driver's own comment refuses.
- **Admit any unit a dispatch row names, without `checkBuildable`.** A CLOSED unit's row stays in the
  file for the rest of the run, so every product path would then be open to every dispatched unit.
- **List every dispatched unit's reason in the refusal and the context.** The dFairHearing run-state
  file holds dozens of dispatch rows, mostly for CLOSED units, so the list would bury the reasons that
  matter and press the context cap.

## 5. Production-readiness checklist

- security — the gate admits on one more source, the build's run-state file, which an agent can write.
  The spec status test and the role arm still bind, and every read failure keeps today's refusal.
- perf / scale — only a write the card route already refuses reads the run-state file. Only a file
  with a dispatch row walks the spec folder. dFairHearing's `RUN.md` measured 53319 bytes, PINNED on
  2026-11-10. A run whose card is stale pays one file read and one folder walk per product write.
- error / empty / loading states — an absent, unreadable or row-less run-state file, an empty build
  line, and a dispatched unit with no spec all leave today's refusal.
- observability — the refusal's added line names the run-state file and the count. The context line
  names the file and says the gate counts the unit as routed.
- risks — a pass that commits without flipping its spec keeps admitting, as §4 states. The DEFERRED
  re-pointing units could drop the fallback, which §3's hand-off names.
- testing — the suite rows §7 declares, observed RED and then GREEN at the close, and the probes in §6.
- migration — none. A session with no run-state file behaves as before.
- user docs — `tools/hooks/README.md`'s write gate section (S6). No `help/` page covers the gate.

## 6. Acceptance criteria

- **AC1** — In the hook suite's write-gate fixture, a card routes a CLOSED Tier-2 unit, and the
  fixture build's `RUN.md` holds a `dispatch · item <sha> TOOL-x-1 · reason …` row for the INPROGRESS
  unit `TOOL-x-1`. Piping a Write payload on the product target to `node tools/hooks/scratch-guard.js`
  exits 0 with an empty stderr.
  Red when: the hook reads the card alone, as at `ae6735c1`, and exits 2 naming `Tier-2 at CLOSED`.
- **AC2** — The same card with no `RUN.md`, and again with a `RUN.md` holding no dispatch row, exits 2.
  The stderr names the CLOSED unit and `Tier-2 at CLOSED`, and carries no `run-state file` line.
  Red when: an absent or row-less run-state file admits, or adds a line to the refusal.
- **AC3** — The same card with a `RUN.md` whose only dispatch rows name `TOOL-x-2`, a Tier-2 SPECCED
  unit, and `TOOL-x-6`, whose spec sits in another build's folder, exits 2. The stderr carries
  `the run-state file` and `2 unit(s)`.
  Red when: a dispatch row admits without `checkBuildable`, or the spec lookup reads outside the card's
  build folder.
  fixture: `TOOL-x-6`'s spec under the fixture build `other` already exists in the suite.
- **AC4** — With the fixture role index present and the AC1 card and run-state file,
  `agent_type=gov-builder` is admitted with an empty stderr, and the main loop is refused naming
  `gov-builder`.
  Red when: the dispatch fallback returns an admission without calling `checkRoleWrite`.
- **AC5** — A SubagentStart payload on the AC1 session gives context carrying `TOOL-x-1 is buildable`
  and `dispatch row`. Without the run-state file the context carries neither.
  Red when: `renderRouteContext` reads the card alone, so it names no buildable unit while the gate
  admits.
- **AC6** — `node -p "require('./tools/hooks/scratch-guard.js').RUN_STATE_FILE"` prints `RUN.md`, and
  the suite row comparing it with the basename in the driver's `runmd_of` passes.
  Red when: the hook's constant or the driver's spelling moves alone.
- **AC7** — `grep -n "dispatch" tools/hooks/README.md` finds the write gate section stating the
  fallback, and `grep -n "RUN_STATE_FILE" tools/hooks/scratch-guard.js` finds it named in the
  `checkRouted` evaluation-order comment.
  Red when: the README and the comment still say only a card route admits.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the AC1, AC4, AC5 and AC6 rows read RED against the hook at `ae6735c1`, and the AC2 and AC3 rows are staged RED by a fallback that admits any unit a dispatch row names · `FLOOR_ASSERTIONS` rises by the rows this unit adds, on top of unit 5's, and the close confirms the executed count

The leg line names every leg whose guard a path in Files touched trips, except those the checker
counts as broad. This spec's author may run only `memory hygiene` and the lexicon, so the main loop
runs every other leg and the arm at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft from the revision brief
  `2026-11-10-prompt-TOOL-aSmoothedDispatch-6-scope`, item 1, and the build brief's item 6, grounded at
  `ae6735c1`. The hook side is chosen because the driver holds no session id and the dispatch row stays
  the one source.

## 10. Reuse audit

The seam is step 9 of `checkRouted` (`tools/hooks/scratch-guard.js:1191`), which this unit extends with
a fallback after its card loop. `checkBuildable` (`:873`) judges each dispatched unit unchanged, and its
H1 block becomes the shared `readSpecH1Id`. `checkRoleWrite` (`:1064`) is the one admission path. The
row match reuses the driver's order-gate regex (`tools/unattended/unattended.sh:14378`). The suite rows
reuse `write_spec`, `write_route_card`, `run_write` and `run_sub`
(`tools/hooks/scratch-guard.test.sh:894`, `:907`, `:1311`), and the parity row follows the derived
`sg_driver` read at `:866`. `reuse_lookup.py "admit a product write for a unit the run-state file
records as dispatched"` ranked only generic name stems such as `run`, `write` and `records`, so no
other seam fits. Recall ranked TOOL-aRoutedQuill-2, the write gate's spec, and two dFairHearing builder
returns that hand-appended a route after this refusal
(`memory/builds/dFairHearing/build/2026-11-02-build-TOOL-dFairHearing-2-1-builder-return.md`,
`memory/builds/dFairHearing/build/2026-11-02-build-TOOL-dFairHearing-3-1-builder-return.md`). It also
ranked TOOL-dWellOiledMachine-38 and TOOL-dScopedBuild-5, DEFERRED units that move the card reads,
named in §3's hand-off. The records and the code disagree in one place: the brief offers the
driver-side card append, but the driver has no session id with which to locate a card.

Recall terms used: `python tools/memory-recall/query.py "how does the write gate treat a builder whose session card routes a closed unit while another unit is dispatched" --terms "scratch-guard write gate route card buildable dispatch row run-state RUN.md stale closed unit builder refused"`
