---
slug: aRepatriatedFork
node: a
opened: 2026-09-23
streams: tooling+deployer+playbook
roster: TOOL+DEPL
ids: DEPL-aRepatriatedFork-1 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 DEPL-aRepatriatedFork-17 DEPL-aRepatriatedFork-20 DEPL-aRepatriatedFork-21 DEPL-aRepatriatedFork-22 DEPL-aRepatriatedFork-23 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19 TOOL-aRepatriatedFork-20 TOOL-aRepatriatedFork-21 TOOL-aRepatriatedFork-22 TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-31 TOOL-aRepatriatedFork-32 TOOL-aRepatriatedFork-33 TOOL-aRepatriatedFork-34 TOOL-aRepatriatedFork-35 TOOL-aRepatriatedFork-36 TOOL-aRepatriatedFork-37 TOOL-aRepatriatedFork-38 TOOL-aRepatriatedFork-39 TOOL-aRepatriatedFork-40 TOOL-aRepatriatedFork-41 TOOL-aRepatriatedFork-42
---

# aRepatriatedFork — what the a7c78ad2 pull proved gov still does not carry, specced as gov's to fix

## The problem this build exists to solve

On 2026-09-23 inCMS and NicoCares were pulled from gov `fd240496` to `a7c78ad2`. `dRetiredFork`,
which promised that `govkit update --write` would be the whole update, closed DEFERRED. The pull
left 27 and 32 engine rows `unattributed`, kits half old and half new, and red bars; the rows were
pinned and three-way merged by hand, and that merge silently stripped 16 CR bytes from awk programs.
A per-file audit of every remaining difference then sorted it into adopter code gov lacks (two of
them security guards), gov defects that force the fork, and govkit mechanics that made the pull
unsafe. Nineteen units, each measured at gov HEAD and at both adopters.

## Expected improvements

- `govkit update --write` is the whole update at both adopters.
- Two security holes close in gov and every future adopter.
- inCMS's divergence map and nc's carve-out census shrink to what is genuinely theirs.
- Adopter bars stop redding on gov's own bytes.

## Detriments if this is not built

- Every pull stays a build: pin, hand-merge, audit, repeat.
- Hand merges keep corrupting gov bytes where no gate looks.
- Both security holes stay live in gov and its adopters.
- The adopters drift at gov's commit rate.

## Build-level rules

- **A unit retires a fork only by making gov's bytes run verbatim at the adopter.** Its acceptance
  names the command, run at inCMS and nc, that shows it.
- **An adopter fix is reproduced at gov HEAD before it is absorbed.** `TOOL-aRepatriatedFork-6` found
  nc's own guard bypassable through `awk -v`.
- **A path fix is a derivation or a render.** A new conf key is justified only for an adopter's
  decision, never its layout.
- **No new bar leg without its ceiling and testsuite-count row**, and every new gate's red case is
  observed before it lands.
- **The security units ship unflagged.** A guard that is off by default is the hole.

## Parked decisions

The owner resolved every §8 fork of the first nineteen units on 2026-09-23, each marked in place.
The ones that set build policy:

- **Kit suites ship to adopters** (`TOOL-aRepatriatedFork-18`), narrowing `TOOL-aQuenchedHarness-3`
  to legs only. Ratified.
- **A declared, lower-only fan-out cap** (`TOOL-aRepatriatedFork-7`), one key in `.agent-cap.conf`.
  Ratified.
- **Split `KIT_MANIFEST_VERSION`** from the manifest format number (`TOOL-aRepatriatedFork-15`).
  Ratified, with the charter bumping on rendered-output change.
- **Shell reading the receipt**: split by consumer. check-wiring alone reads it in awk
  (`TOOL-aRepatriatedFork-19`), and every other shell consumer imports the canonical reader
  (`TOOL-aRepatriatedFork-2`).
- **inCMS's own engines converge onto gov's**, and this build carries the migration
  (`DEPL-aRepatriatedFork-20`). `DEPL-aRepatriatedFork-13` is the bridge until then. Unit 20's six
  forks were resolved under the mandate at its rev-2. Its migration is prepared on an unpushed inCMS
  branch, and landing it there is the owner's call.
- **Adopter-side, not gov's**: inCMS's own pre-push `eval`s `INCMS_PUSH_GATE_CMD` and nc runs the
  bypassable `set_fact` guard until it pulls; `TOOL-aRepatriatedFork-5` and `-6` record both.
- **Re-opened 2026-09-25 by owner ruling** to drain every hard-coded kit prefix, fixtures and
  gov-side files included, before `TOOL-aRepatriatedFork-18`'s held leg: units 23 to 30.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `DEPL-aRepatriatedFork-1` | 2 | the charter renderer lets an answer win, and knows which file is its template |
| 1 | `TOOL-aRepatriatedFork-3` | 1 | shipped Python names its encoding on every text-IO call |
| 1 | `TOOL-aRepatriatedFork-4` | 2 | review-harness gates find harnesses where adopters keep them |
| 1 | `TOOL-aRepatriatedFork-5` | 2 | SECURITY: pre-push runs only a tracked, unmodified gate command |
| 1 | `TOOL-aRepatriatedFork-6` | 2 | SECURITY: unattended set_fact refuses a value that can forge a second fact |
| 1 | `TOOL-aRepatriatedFork-7` | 2 | agent-cap: the nested-interpolation fix, and a declared lower cap |
| 1 | `TOOL-aRepatriatedFork-9` | 2 | row_grammar and check-arms take nc's additions and stop importing sibling engines |
| 1 | `TOOL-aRepatriatedFork-10` | 2 | the memory-tree engine grandfathers what it says it does; its docs state the adopter's facts |
| 1 | `TOOL-aRepatriatedFork-16` | 2 | check-install-prefix grades only what a repo ships |
| 1 | `TOOL-aRepatriatedFork-21` | 1 | a build README is builds/<slug>/README.md, at exactly that depth |
| 2 | `TOOL-aRepatriatedFork-2` | 2 | every kit path a runtime string spells is derived |
| 2 | `TOOL-aRepatriatedFork-8` | 2 | the lander contracts inCMS carries |
| 2 | `DEPL-aRepatriatedFork-13` | 2 | an adopter's own engine is declared, not "unattributed" |
| 2 | `TOOL-aRepatriatedFork-15` | 2 | a kit whose shipped bytes move bumps its version |
| 3 | `DEPL-aRepatriatedFork-14` | 1 | hole probes and descriptors that cannot pass at an adopter |
| 3 | `DEPL-aRepatriatedFork-17` | 2 | govkit update is safe to run and says what it did |
| 3 | `DEPL-aRepatriatedFork-21` | 2 | apply never lands gov's bytes on a file the target owns |
| 4 | `TOOL-aRepatriatedFork-18` | 2 | the test suites that arm gov's gates reach adopters |
| 5 | `TOOL-aRepatriatedFork-19` | 2 | check-wiring judges every arm at a relocated layout |
| 6 | `TOOL-aRepatriatedFork-11` | 2 | unattended: pathspecs stop at the build root; a pull lands hooks wired and pins measurable |
| 6 | `TOOL-aRepatriatedFork-12` | 2 | memory-recall reads the adopter's corpus shape from conf |
| 8 | `TOOL-aRepatriatedFork-23` | 2 | the install-prefix ban counts every kit path it cannot see today |
| 9 | `TOOL-aRepatriatedFork-24` | 2 | no line that executes strands an adopter at another prefix |
| 10 | `TOOL-aRepatriatedFork-25` | 1 | printed and usage strings in received code name no install prefix |
| 11 | `TOOL-aRepatriatedFork-26` | 1 | the runbook and every shipped doc name no install prefix |
| 12 | `TOOL-aRepatriatedFork-27` | 1 | canonical-copy markers and comment prose name no install prefix |
| 13 | `TOOL-aRepatriatedFork-29` | 2 | gov's own gates and declarations derive the prefix they name |
| 14 | `TOOL-aRepatriatedFork-28` | 2 | every suite builds its fixtures at a prefix it derives |
| 15 | `TOOL-aRepatriatedFork-30` | 2 | the suites run at a foreign prefix; the install-prefix gate is a pure ban |
| 16 | `TOOL-aRepatriatedFork-31` | 1 | gov's shipped files carry no adopter name |
| 17 | `TOOL-aRepatriatedFork-32` | 1 | every branch of hygiene check 21 honours RECORD_SERVES_CUTOFF |
| 18 | `TOOL-aRepatriatedFork-35` | 1 | gov's shipped files name no adopter, inCMS included |
| 19 | `TOOL-aRepatriatedFork-36` | 2 | the recall kit converges at adopters: no forked rule, and an owned hook is declared |
| 19 | `TOOL-aRepatriatedFork-37` | 1 | the unattended suite derives the repair pointer it asserts |
| 19 | `TOOL-aRepatriatedFork-38` | 1 | every conf reader drops a trailing comment the way bash does |
| 19 | `TOOL-aRepatriatedFork-39` | 1 | hygiene check 14 counts present-tense citations only, as check 15 does |
| 19 | `TOOL-aRepatriatedFork-40` | 1 | recall anchors an id on the spec H1 that defines it |
| 19 | `TOOL-aRepatriatedFork-42` | 1 | the memory-tree renders take every adopter path from its own declarations |
| 20 | `DEPL-aRepatriatedFork-20` | 2 | inCMS converges onto gov's memory-tree programs |

The `#` column is the `order` each spec declares, derived from its `### Edges`: a unit's order is one
past the highest order it consumes from. Order 1 holds the independent units, the two security fixes
among them.

**The build is done when a `govkit update --write` from gov HEAD at inCMS and at nc lands every row,
re-stamps `gov_commit`, leaves no conflict order, and both adopters' full bars are green on the result
with no hand edit between the update and the bar.** One observation at each adopter, not a tally.

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 39 unit(s) · node a · opened 2026-09-23 · streams tooling+deployer+playbook
ids DEPL-aRepatriatedFork-1 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 DEPL-aRepatriatedFork-17 DEPL-aRepatriatedFork-20 DEPL-aRepatriatedFork-21 DEPL-aRepatriatedFork-22 DEPL-aRepatriatedFork-23 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5
ids TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19 TOOL-aRepatriatedFork-20
ids TOOL-aRepatriatedFork-21 TOOL-aRepatriatedFork-22 TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-31
ids TOOL-aRepatriatedFork-32 TOOL-aRepatriatedFork-33 TOOL-aRepatriatedFork-34 TOOL-aRepatriatedFork-35 TOOL-aRepatriatedFork-36 TOOL-aRepatriatedFork-37 TOOL-aRepatriatedFork-38 TOOL-aRepatriatedFork-39 TOOL-aRepatriatedFork-40 TOOL-aRepatriatedFork-41 TOOL-aRepatriatedFork-42

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [DEPL-aRepatriatedFork-1 — the charter renderer lets an answer win, and knows which file is its template](spec/2026-09-23-spec-DEPL-aRepatriatedFork-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-09-23 |
| [TOOL-aRepatriatedFork-10 — the memory-tree engine grandfathers what it says it does, and its rendered docs state the adopter's own facts](spec/2026-09-23-spec-TOOL-aRepatriatedFork-10.md) | 1 | 2 | CLOSED | rev-8 | 2026-09-24 |
| [TOOL-aRepatriatedFork-16 — check-install-prefix grades only what a repo ships](spec/2026-09-23-spec-TOOL-aRepatriatedFork-16.md) | 1 | 2 | CLOSED | rev-2 | 2026-09-23 |
| [TOOL-aRepatriatedFork-21 — a build README is `builds/<slug>/README.md`, at exactly that depth](spec/2026-09-24-spec-TOOL-aRepatriatedFork-21.md) | 1 | 1 | CLOSED | rev-2 | 2026-09-24 |
| [TOOL-aRepatriatedFork-3 — shipped Python names its encoding on every text-IO call](spec/2026-09-23-spec-TOOL-aRepatriatedFork-3.md) | 1 | 1 | CLOSED | rev-2 | 2026-09-23 |
| [TOOL-aRepatriatedFork-4 — review-harness gates find harnesses where adopters keep them](spec/2026-09-23-spec-TOOL-aRepatriatedFork-4.md) | 1 | 2 | CLOSED | rev-2 | 2026-09-23 |
| [TOOL-aRepatriatedFork-5 — pre-push runs only a tracked, unmodified gate command](spec/2026-09-23-spec-TOOL-aRepatriatedFork-5.md) | 1 | 2 | CLOSED | rev-5 | 2026-09-24 |
| [TOOL-aRepatriatedFork-6 — unattended set_fact refuses a value that can forge a second fact](spec/2026-09-23-spec-TOOL-aRepatriatedFork-6.md) | 1 | 2 | CLOSED | rev-6 | 2026-09-24 |
| [TOOL-aRepatriatedFork-7 — agent-cap: the nested-interpolation fix, and a declared lower cap](spec/2026-09-23-spec-TOOL-aRepatriatedFork-7.md) | 1 | 2 | CLOSED | rev-6 | 2026-09-24 |
| [TOOL-aRepatriatedFork-9 — row_grammar and check-arms take NicoCares' additions, and stop importing sibling engines](spec/2026-09-23-spec-TOOL-aRepatriatedFork-9.md) | 1 | 2 | CLOSED | rev-2 | 2026-09-24 |
| [DEPL-aRepatriatedFork-13 — an adopter's own engine is declared, not "unattributed"](spec/2026-09-23-spec-DEPL-aRepatriatedFork-13.md) | 2 | 2 | CLOSED | rev-6 | 2026-09-24 |
| [TOOL-aRepatriatedFork-15 — a kit whose shipped bytes move bumps its version](spec/2026-09-23-spec-TOOL-aRepatriatedFork-15.md) | 2 | 2 | CLOSED | rev-2 | 2026-09-24 |
| [TOOL-aRepatriatedFork-2 — every kit path a runtime string spells is derived](spec/2026-09-23-spec-TOOL-aRepatriatedFork-2.md) | 2 | 2 | CLOSED | rev-7 | 2026-09-24 |
| [TOOL-aRepatriatedFork-8 — the lander contracts inCMS carries](spec/2026-09-23-spec-TOOL-aRepatriatedFork-8.md) | 2 | 2 | CLOSED | rev-5 | 2026-09-24 |
| [DEPL-aRepatriatedFork-14 — hole probes and descriptors that cannot pass at an adopter](spec/2026-09-23-spec-DEPL-aRepatriatedFork-14.md) | 3 | 1 | CLOSED | rev-3 | 2026-09-24 |
| [DEPL-aRepatriatedFork-17 — govkit update is safe to run and says what it did](spec/2026-09-23-spec-DEPL-aRepatriatedFork-17.md) | 3 | 2 | CLOSED | rev-4 | 2026-09-24 |
| [DEPL-aRepatriatedFork-21 — apply never lands gov's bytes on a file the target owns](spec/2026-09-24-spec-DEPL-aRepatriatedFork-21.md) | 3 | 2 | CLOSED | rev-3 | 2026-09-24 |
| [TOOL-aRepatriatedFork-18 — the test suites that arm gov's gates reach adopters](spec/2026-09-23-spec-TOOL-aRepatriatedFork-18.md) | 4 | 2 | CLOSED | rev-4 | 2026-09-24 |
| [TOOL-aRepatriatedFork-19 — check-wiring judges every arm at a relocated layout](spec/2026-09-23-spec-TOOL-aRepatriatedFork-19.md) | 5 | 2 | CLOSED | rev-3 | 2026-09-24 |
| [TOOL-aRepatriatedFork-11 — unattended: build-root pathspecs stop at the build root, and a pull lands its hooks wired and its pins measurable](spec/2026-09-23-spec-TOOL-aRepatriatedFork-11.md) | 6 | 2 | CLOSED | rev-3 | 2026-09-24 |
| [TOOL-aRepatriatedFork-12 — memory-recall reads the adopter's corpus shape from conf](spec/2026-09-23-spec-TOOL-aRepatriatedFork-12.md) | 6 | 2 | CLOSED | rev-3 | 2026-09-24 |
| [TOOL-aRepatriatedFork-23 — the install-prefix ban counts every kit path it cannot see today](spec/2026-09-25-spec-TOOL-aRepatriatedFork-23.md) | 8 | 2 | SPECCED | rev-2 | 2026-09-25 |
| [TOOL-aRepatriatedFork-24 — no line that executes strands an adopter at another prefix](spec/2026-09-25-spec-TOOL-aRepatriatedFork-24.md) | 9 | 2 | SPECCED | rev-2 | 2026-09-25 |
| [TOOL-aRepatriatedFork-25 — printed and usage strings in received code name no install prefix](spec/2026-09-25-spec-TOOL-aRepatriatedFork-25.md) | 10 | 1 | SPECCED | rev-2 | 2026-09-25 |
| [TOOL-aRepatriatedFork-26 — the runbook and every shipped doc name no install prefix](spec/2026-09-25-spec-TOOL-aRepatriatedFork-26.md) | 11 | 1 | SPECCED | rev-2 | 2026-09-25 |
| [TOOL-aRepatriatedFork-27 — canonical-copy markers and comment prose name no install prefix](spec/2026-09-25-spec-TOOL-aRepatriatedFork-27.md) | 12 | 1 | SPECCED | rev-1 | 2026-09-25 |
| [TOOL-aRepatriatedFork-29 — gov's own gates and declarations derive the prefix they name](spec/2026-09-25-spec-TOOL-aRepatriatedFork-29.md) | 13 | 2 | SPECCED | rev-2 | 2026-09-25 |
| [TOOL-aRepatriatedFork-28 — every suite builds its fixtures at a prefix it derives](spec/2026-09-25-spec-TOOL-aRepatriatedFork-28.md) | 14 | 2 | SPECCED | rev-2 | 2026-09-25 |
| [TOOL-aRepatriatedFork-30 — the suites run at a foreign prefix, and the install-prefix gate is a pure ban](spec/2026-09-25-spec-TOOL-aRepatriatedFork-30.md) | 15 | 2 | SPECCED | rev-2 | 2026-09-25 |
| [TOOL-aRepatriatedFork-31 — gov's shipped files carry no adopter name](spec/2026-09-25-spec-TOOL-aRepatriatedFork-31.md) | 16 | 1 | CLOSED | rev-2 | 2026-09-25 |
| [TOOL-aRepatriatedFork-32 — every branch of hygiene check 21 honours `RECORD_SERVES_CUTOFF`](spec/2026-09-25-spec-TOOL-aRepatriatedFork-32.md) | 17 | 1 | CLOSED | rev-3 | 2026-09-26 |
| [TOOL-aRepatriatedFork-35 — gov's shipped files name no adopter, inCMS included](spec/2026-09-25-spec-TOOL-aRepatriatedFork-35.md) | 18 | 1 | CLOSED | rev-2 | 2026-09-25 |
| [TOOL-aRepatriatedFork-36 — the recall kit converges at adopters](spec/2026-09-25-spec-TOOL-aRepatriatedFork-36.md) | 19 | 2 | CLOSED | rev-3 | 2026-09-26 |
| [TOOL-aRepatriatedFork-37 — the unattended suite derives the repair pointer it asserts](spec/2026-09-25-spec-TOOL-aRepatriatedFork-37.md) | 19 | 1 | CLOSED | rev-2 | 2026-09-25 |
| [TOOL-aRepatriatedFork-38 — every conf reader drops a trailing comment the way bash does](spec/2026-09-25-spec-TOOL-aRepatriatedFork-38.md) | 19 | 1 | CLOSED | rev-3 | 2026-09-26 |
| [TOOL-aRepatriatedFork-39 — hygiene check 14 counts present-tense citations only, as check 15 does](spec/2026-09-28-spec-TOOL-aRepatriatedFork-39.md) | 19 | 1 | CLOSED | rev-2 | 2026-09-28 |
| [TOOL-aRepatriatedFork-40 — recall anchors an id on the spec H1 that defines it](spec/2026-09-28-spec-TOOL-aRepatriatedFork-40.md) | 19 | 1 | CLOSED | rev-2 | 2026-09-28 |
| [TOOL-aRepatriatedFork-42 — the memory-tree renders take every adopter path from the adopter's own declarations](spec/2026-09-29-spec-TOOL-aRepatriatedFork-42.md) | 19 | 1 | SPECCED | rev-1 | 2026-09-29 |
| [DEPL-aRepatriatedFork-20 — inCMS converges onto gov's memory-tree programs](spec/2026-09-23-spec-DEPL-aRepatriatedFork-20.md) | 20 | 2 | INPROGRESS | rev-10 | 2026-09-29 |
<!-- /gen:build-units -->

Records: 73 bound to this build, across 4 record folder(s).

Ids no record names: TOOL-aRepatriatedFork-42.

Ids no `spec-audit` record has ever named: DEPL-aRepatriatedFork-1 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 DEPL-aRepatriatedFork-17 DEPL-aRepatriatedFork-20 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16
TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 DEPL-aRepatriatedFork-21 TOOL-aRepatriatedFork-21
TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-31 TOOL-aRepatriatedFork-32 TOOL-aRepatriatedFork-35 TOOL-aRepatriatedFork-36
TOOL-aRepatriatedFork-37 TOOL-aRepatriatedFork-38 TOOL-aRepatriatedFork-39 TOOL-aRepatriatedFork-40 TOOL-aRepatriatedFork-42.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `DEPL-aRepatriatedFork-1`, `TOOL-aRepatriatedFork-10`, `TOOL-aRepatriatedFork-16`, `TOOL-aRepatriatedFork-21`, `TOOL-aRepatriatedFork-3`, `TOOL-aRepatriatedFork-4`, `TOOL-aRepatriatedFork-5`, `TOOL-aRepatriatedFork-6`, `TOOL-aRepatriatedFork-7`, `TOOL-aRepatriatedFork-9` | yes |
| 2 | `DEPL-aRepatriatedFork-13`, `TOOL-aRepatriatedFork-15`, `TOOL-aRepatriatedFork-2`, `TOOL-aRepatriatedFork-8` | yes |
| 3 | `DEPL-aRepatriatedFork-14`, `DEPL-aRepatriatedFork-17`, `DEPL-aRepatriatedFork-21` | yes |
| 4 | `TOOL-aRepatriatedFork-18` | no |
| 5 | `TOOL-aRepatriatedFork-19` | no |
| 6 | `TOOL-aRepatriatedFork-11`, `TOOL-aRepatriatedFork-12` | yes |
| 8 | `TOOL-aRepatriatedFork-23` | no |
| 9 | `TOOL-aRepatriatedFork-24` | no |
| 10 | `TOOL-aRepatriatedFork-25` | no |
| 11 | `TOOL-aRepatriatedFork-26` | no |
| 12 | `TOOL-aRepatriatedFork-27` | no |
| 13 | `TOOL-aRepatriatedFork-29` | no |
| 14 | `TOOL-aRepatriatedFork-28` | no |
| 15 | `TOOL-aRepatriatedFork-30` | no |
| 16 | `TOOL-aRepatriatedFork-31` | no |
| 17 | `TOOL-aRepatriatedFork-32` | no |
| 18 | `TOOL-aRepatriatedFork-35` | no |
| 19 | `TOOL-aRepatriatedFork-36`, `TOOL-aRepatriatedFork-37`, `TOOL-aRepatriatedFork-38`, `TOOL-aRepatriatedFork-39`, `TOOL-aRepatriatedFork-40`, `TOOL-aRepatriatedFork-42` | yes |
| 20 | `DEPL-aRepatriatedFork-20` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
