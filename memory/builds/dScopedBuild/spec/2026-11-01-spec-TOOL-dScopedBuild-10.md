# TOOL-dScopedBuild-10 — a red-first `reproduction` before the fix of a reported bug: `--dispatch` refusing a unit that closes a bug report until a confirmed reproduction serves it

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 12 · advances TOOL-dScopedBuild-16

**Carries:** cl-dClosedLoop-0408@9fd076d5 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-10-deviation-101.md](../build/2026-11-01-build-TOOL-dScopedBuild-10-deviation-101.md) | deviation | — |
| [2026-11-01-build-TOOL-dScopedBuild-10-reuse-scout-d.md](../build/2026-11-01-build-TOOL-dScopedBuild-10-reuse-scout-d.md) | research | TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-fix-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-3 TOOL-dScopedBuild-6 TOOL-dScopedBuild-9 TOOL-dScopedBuild-11 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-prompt-TOOL-dScopedBuild-10-1-reuse-scout.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-10-1-reuse-scout.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

A fix for a reported bug can land without the bug ever having been made red first: the probe
program specs a `reproduction` kind (TOOL-dPlacedRequest-7 S3, S4) and nothing fires it, and Design
sends a patch straight to its unit spec (B4-F10, `…-walk-return-b4.md:119-129`). This unit makes the
first `build.unit-pass` of a unit that fixes a reported bug, `--dispatch` today, refuse until a
confirmed `reproduction` probe record serves that unit and names the bug, so the red-first witness
exists before any fix commit (the night pass, point 2; practice 12, "a failing test first for a bug").

## 2. Scope (IN)

No build-run precondition: the gate reads records by text, and TOOL-dPlacedRequest-7, which writes
them, is not this build's parent (§8 F2).

- **S1** — The bug report. `read_ask_seen <ask id>` in `tools/unattended/unattended.sh` runs
  `run_bounded $ASKS_CMD <ask id>` (`:262`), the generator's one-ask detail mode, and prints each
  line its output labels `seen`, the merged `seen` clause values `render_ask_detail` prints one per
  line (`tools/memory-tree/gen_build_index.py:3407-3409`). An ask with at least one `seen` value is a
  reported bug: its row says where the defect was observed, the reading the asks guide gives a `seen`
  locator ("the locator no longer shows the defect", `memory/guides/UNATTENDED-ASKS.md:78`).
  Observed by AC1, AC2.
- **S2** — What a unit owes. `check_reproduction_owed <slug> <unit id> <spec>` reads the ids the spec
  header's `closes` and `advances` verbs name, through `spec_ask_verbs` (`:4905`), and for each that
  S1 calls a reported bug, looks for its witness at HEAD: a tracked
  `<MEMORY_ROOT>/builds/<slug>/build/<date>-build-<unit id>-probe-<n>.md` whose text carries
  `**Serves:** probe <unit id>`, `**Kind:** reproduction` and `**Verdict:** confirmed`, and whose
  `**Trigger:**` value names a tracked `<date>-build-<unit id>-probe-trigger-<n>.md` in the same folder
  carrying `**Cause:** reproduction` and a `**Subject:**` naming the ask id as a whole token. Those
  are TOOL-dPlacedRequest-7 S6's two record kinds, read as text and written by its `probe.py` or, until
  that lands, by hand in the same shape with `**Writer:** stand-in`. It prints one line per ask owed
  and unwitnessed, `<ask id> · seen <first seen value>`, and returns 1 when it printed any.
  Observed by AC2, AC3, AC4.
- **S3** — The gate. `verb_dispatch` (`:13624`) calls S2 after its held-ask refusal (`:13841`) and
  before its `--writes` loop. A non-empty answer is fail 49: `--dispatch declares a build pass for a
  unit that fixes a reported bug that was never reproduced red: <unit> closes <ask> (seen <locator>)
  and no confirmed reproduction probe serves it`, then the route. Where `probe.py` is found
  (`tools/loop/probe.py`, the loop kit beside this one), the route is its two commands with the values
  filled, `python tools/loop/probe.py trigger --cause reproduction --asker item.build.unit-pass
  --subject <ask id> --build <slug>` and `pin --trigger <record> --sha <sha> --kind reproduction
  --question <text> --losing <text>`; elsewhere it names the stand-in, the two records of S2 written
  by hand. Every dispatch of the unit runs the gate, a fix pass's included, and a witnessed unit
  passes it each time. Observed by AC2, AC5.
- **S4** — The edges of the gate. With `ASKS_CMD` blank the gate prints `reproduction gate unarmed:
  ASKS_CMD is blank, so no ask is read for a seen clause` and admits, the announced-dark register of
  `read_ask_back` (`:9945`). An ask the generator does not answer within its bound, or answers with a
  non-zero exit, is refused under fail 49 naming the generator's verdict, never admitted. A spec whose
  header names no ask makes no bounded call. Observed by AC6, AC7.
- **S5** — The carrier. The `--dispatch` paragraph of `tools/unattended/VERBS.template.md` (`:712`),
  rendered to `memory/guides/UNATTENDED-VERBS.md`, says that a unit closing or advancing an ask with a
  `seen` clause is dispatched only once a confirmed reproduction probe serves it, and names the two
  `probe.py` commands. Observed by AC8.

## 3. Non-goals (OUT)

- The probe program, its records' writer, `probe.design`, `probe.run` and `probe.judge`:
  TOOL-dPlacedRequest-7. This unit reads two of its record kinds and fires nothing itself (§8 F3).
- Marking a placed patch build as coming from a bug report: no parent writes such a mark, and a patch
  placed from an owner's prose request carries no `seen` locator (§8 F4 names the ask).
- The `needs` row of `item.build.unit-pass` in `tools/loop/loop.toml`: TOOL-dDeclaredLoop-12's table,
  and the item's node is TOOL-dScopedBuild-8's.
- An attended build, which has no `--dispatch`: its write gate is TOOL-dScopedBuild-5's, and no
  record of an attended pass exists before its first commit for this gate to read.
- Judging whether the reproduction is a good one: `probe.judge` writes the verdict, and this gate
  reads `confirmed` and nothing else.

### Edges

- **consumes-from** external — TOOL-dPlacedRequest-7 S3, S4 and S6: the `probe` and `probe-trigger` record shapes the gate reads and the `trigger` and `pin` verbs its route names, DEFERRED at base and not a parent's, so the hand-written stand-in of S2 serves until it lands
- **hands-off** external — dPlacedRequest: a patch build placed from an owner's bug report given as prose files that report as an ask carrying a `seen` locator, the ask §8 F4 states

## 4. Design

### Evidence at base

- The trigger's table: `reproduction` is refused "never; a patch build's red-first reproduction
  (`cl-dClosedLoop-0408`)" (TOOL-dPlacedRequest-7 §4 "The trigger's refusals"), and flow-steps puts it
  "before its first `build.unit-pass`"
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:632`).
- No parent marks a build as coming from a bug report: TOOL-dPlacedRequest-21 S4 types a patch only by
  `parents: <origin slug>` on its derived README, and no spec of the four parents spells "bug report"
  (scout D row 10).
- The seen read, probed at writing: `python tools/memory-tree/gen_build_index.py --asks DEPL-aBenchedProbe-5`
  prints a `seen` line naming `WIRE-INTO-PROJECT.md` at `f1e828bd:782`, and the same mode over
  `TOOL-dScopedBuild-16` prints no `seen` line (§8 F1).
- The gate point: `verb_dispatch` is the first act of a unit's pass under the driver, and it already
  reads the spec's `closes` ids for its held-ask refusal (`unattended.sh:13820-13843`).

### The gate

```
--dispatch <slug> --pass <unit> --writes …
  spec  := the tracked spec defining <unit>                       (existing MISSING / THIN floor)
  ids   := spec_ask_verbs spec closes ∪ spec_ask_verbs spec advances
  for id in ids:
    seen := read_ask_seen id                                      -> none: not a bug report, skip
    witness := probe-<n>.md serving <unit>, Kind reproduction, Verdict confirmed,
               its Trigger record Cause reproduction, Subject naming id
    none -> owed
  owed non-empty -> fail 49, the route
```

### Inventory

Minted: the functions `read_ask_seen` and `check_reproduction_owed`, each answering `OK` from `python
tools/lexicon/lexicon.py --suggest <name> --as sh.function`, asked at writing; one fail-49 refusal and
the unarmed announce line. No record kind, flag or key is minted.

### Migration

None for the bar. A live run whose unit closes a `seen`-carrying ask and has not yet dispatched it is
refused at that dispatch until its reproduction is recorded. At base the asks a unit spec closes with a
`seen` clause are those an unattended `gates-green` filed for an inherited red; each now owes its red
reproduced before its fix.

### Rollout

Live at landing; the unattended kit's version moves (`KIT_UNATTENDED_VERSION`, `unattended.sh`).

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`
- `memory/guides/UNATTENDED-VERBS.md`

### Alternatives rejected

- **Every patch build owes a reproduction**, read off `parents:`. Tested against the parents: the
  marker is TOOL-dPlacedRequest-21's and absent at base, and a patch is not always a bug, so a feature
  patch would owe a reproduction of nothing.
- **A new README key naming the bug report.** No parent writes it, and adding one is a public-surface
  change none of this build's clauses names (veto 2 outside the grant).
- **The driver firing `probe.py trigger` itself.** It needs the loop kit at base, which is absent, and
  writes a record mid-dispatch the run must then stage; the trigger is a command any caller runs, and
  the gate is where it is owed.

## 5. Production-readiness checklist

- security — the gate executes no ask text: `--asks <id>` only renders a row, and an ask's `seen`
  command stays unrun, as `memory/guides/UNATTENDED-ASKS.md:71-73` requires.
- perf / scale — one bounded generator call per ask a unit's header names, only at `--dispatch`.
- error / empty / loading states — a blank `ASKS_CMD` is announced and admits; a generator that does not
  answer refuses; a header naming no ask makes no call.
- observability — the refusal names the unit, the ask, its `seen` locator and the commands that open
  the reproduction.
- risks — a unit closing an inherited-red ask now needs its red reproduced before it can be dispatched,
  which is the clause's intent and a new step for such runs (§4 "Migration").
- testing — AC1 to AC8 by a pass in a scratch clone; the arm of §7 at the close.
- migration — §4.
- user docs — `memory/guides/UNATTENDED-VERBS.md` (S5); no `help/` page covers the driver
  (`help/README.md`).

## 6. Acceptance criteria

- **AC1** — When `read_ask_seen` runs in a scratch clone, sliced from `tools/unattended/unattended.sh`
  with `run_bounded` beside it and `ASKS_CMD` as `.unattended.conf` declares it, over `DEPL-aBenchedProbe-5` it prints one line carrying `WIRE-INTO-PROJECT.md`, and over
  `TOOL-dScopedBuild-16` it prints nothing.
  Red when: an ask with no `seen` clause reads as a bug report, or one with it reads as none.
- **AC2** — When `bash tools/unattended/unattended.sh --dispatch tRun --pass TOOL-tRun-1 --writes "$W"`
  runs in a scratch clone whose preflighted run `tRun` holds a spec of `TOOL-tRun-1` closing an ask
  filed with a `seen` clause and no probe record, `W` naming the one planted script that spec's Files
  touched declares, it exits non-zero with fail 49 naming the ask and
  `reproduction`, and records no dispatch row.
  Red when: a planted patch build from a bug report reaches its first pass with no reproduction.
  fixture: a scratch clone under `%TEMP%`, its run built as the suite's `reset_tree` builds `tRun`.
- **AC3** — When the clone commits a `-probe-1.md` record serving `TOOL-tRun-1`, kind `reproduction`,
  verdict `confirmed`, and its `-probe-trigger-1.md` record whose subject names the ask, AC2's
  `--dispatch` exits 0.
  Red when: a confirmed reproduction of the bug does not admit its fix.
- **AC4** — When the clone's probe record reads `**Verdict:** refuted` instead, or its trigger's
  subject names another ask, AC2's `--dispatch` exits non-zero with fail 49.
  Red when: a reproduction that failed, or one of another bug, admits the fix.
- **AC5** — When AC2's refusal prints in a clone whose loop kit holds no `probe.py`, it names the
  hand-written records and `**Writer:** stand-in`; with a stub `probe.py` present, it names
  `probe.py trigger --cause reproduction`.
  Red when: the refusal names a route the tree cannot run.
- **AC6** — When the clone's ask carries no `seen` clause, AC2's `--dispatch` exits 0 with no probe
  record; and with `ASKS_CMD=` declared blank it exits 0 printing `reproduction gate unarmed`.
  Red when: a unit closing an ordinary ask is held, or the dark path is silent.
- **AC7** — When the clone's `ASKS_CMD` names a stub that exits 3, AC2's `--dispatch` exits non-zero with
  fail 49 naming the generator's exit.
  Red when: an ask the generator could not read is admitted as no bug report.
- **AC8** — When `grep -c 'reproduction' memory/guides/UNATTENDED-VERBS.md` runs at the pass tip, it
  prints at least 1, and the `--dispatch` paragraph names `probe.py trigger`.
  Red when: the gate refuses and the verbs carrier never says it will.

## 7. Gates

`unattended kit gate` · `pass-order history` · `memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC2 AC3 AC4 AC5 AC6 AC7 · the dispatch cases over the suite's `tRun` with a `seen`-carrying ask, staged red by returning 0 from `check_reproduction_owed` · none

## 8. Open questions

- **FACT-QUESTION · F1 — Can the driver read whether an ask carries a `seen` clause through the generator
  it already holds?** Probe: `python tools/memory-tree/gen_build_index.py --asks <id>` over an ask filed
  with a `seen` clause and over one filed without. The observation that decides: a `seen`-labelled line
  in the first output and none in the second. Liveness: the second case, `TOOL-dScopedBuild-16`, is an
  ask the probe must answer negatively, and it did. RESOLVED (agent, 2026-11-01, delegated): yes; run at `5f0b11f12`, `DEPL-aBenchedProbe-5` printed a `seen` line naming `WIRE-INTO-PROJECT.md` and `TOOL-dScopedBuild-16` printed no `seen` line, so S1 reads the detail mode and the 11-field TSV contract is untouched. widens: none · relaxes: none
- **F2 — How does the gate reach a probe program this build does not parent?** Options: (a) read
  TOOL-dPlacedRequest-7 S6's two record shapes as text, a hand-written pair standing in until `probe.py`
  lands; (b) a build-run precondition that TOOL-dPlacedRequest-7 lands first; (c) an ask to
  dPlacedRequest and no gate. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the most feature-rich survivor: the gate holds from landing, the record shape is the parent spec's own, and its S5 already names a `stand-in` writer; (b) assumes a non-parent lands first, which the brief forbids; (c) leaves the clause unbuilt. widens: none · relaxes: none
- **F3 — Does the driver fire the trigger, or refuse until it is fired?** Options: (a) refuse, naming
  the trigger and pin commands; (b) run `probe.py trigger` at the first refused dispatch.
  RESOLVED (agent, 2026-11-01, delegated): (a), rung 3: the reproduction needs a tester's method (`probe.design`) before it can be confirmed, so firing alone confirms nothing, and (b) writes a record mid-dispatch and needs the loop kit absent at base. widens: none · relaxes: none
- **F4 — What marks a build as coming from a bug report?** Options: (a) a unit's header closing or
  advancing an ask whose row carries a `seen` clause; (b) every patch build, by `parents:`; (c) a new
  README key. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3: it is derivable at base from the ask grammar and the header verbs, and it gates the fix itself, the unit that closes the report; (b) and (c) fail as §4 "Alternatives rejected" records. It reads no patch marker, so it is stricter than the clause on a non-patch build closing a reported bug, recorded as deviation 101 (`build/2026-11-01-build-TOOL-dScopedBuild-10-deviation-101.md`). Ask for dPlacedRequest, filed by the main loop: target TOOL-dPlacedRequest-21's placed patch build; accept a patch build placed from an owner's prose bug report files that report as an ask in its own `BACKLOG.md` carrying a `seen` locator, and the unit that fixes it closes that ask, seen on a fixture placed patch reaching its first dispatch. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from the packet's Items 10, scout D's row 10 and its probe CLI
  interface, and the sources read at `5f0b11f12`.

## 10. Reuse audit

The seams extended are `verb_dispatch` (`tools/unattended/unattended.sh:13624`), the gate point that
already refuses MISSING and THIN units and a unit closing a held ask (`:13841`); `spec_ask_verbs`
(`:4905`), the driver's one reader of a header's `closes` and `advances`; `run_bounded` and the
declared `ASKS_CMD` (`:262`, `.unattended.conf:216`), the generator the driver already calls; and
TOOL-dPlacedRequest-7 S6's record shapes, read rather than re-spelled. `python
tools/codebase-map/reuse_lookup.py "refuse a dispatch of a fix for a reported bug until a red-first
reproduction is recorded"` ranked name stems (`report`, `records`, `read_records`, `CensusRefused`),
none of which reads an ask's `seen` clause or a probe record: no seam fits for the predicate, the gap
scout D named ("The predicate 'comes from a bug report': no seam fits"). The scout placed the guard in
`verb_dispatch` at :13624, which held at `5f0b11f12`; its note that the guard needs a `needs` entry in
`tools/loop/loop.toml` is left to that table's owner (§3).

Recall terms used: `python tools/memory-recall/query.py "what makes a patch build reproduce a reported bug red before its first pass" --terms "reproduction probe trigger patch bug report red-first build.unit-pass verb_dispatch seen clause ask closes"`
