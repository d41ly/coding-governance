---
slug: aRepatriatedFork
node: a
opened: 2026-09-23
streams: tooling+deployer+playbook
roster: TOOL+DEPL
ids: DEPL-aRepatriatedFork-1 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 DEPL-aRepatriatedFork-17 DEPL-aRepatriatedFork-20 DEPL-aRepatriatedFork-21 DEPL-aRepatriatedFork-22 TOOL-aRepatriatedFork-1 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19 TOOL-aRepatriatedFork-20 TOOL-aRepatriatedFork-21
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
| 7 | `DEPL-aRepatriatedFork-20` | 2 | inCMS converges onto gov's memory-tree programs |

The `#` column is the `order` each spec declares, derived from its `### Edges`: a unit's order is one
past the highest order it consumes from. Order 1 is nine independent units, two of them the security
fixes.

**The build is done when a `govkit update --write` from gov HEAD at inCMS and at nc lands every row,
re-stamps `gov_commit`, leaves no conflict order, and both adopters' full bars are green on the result
with no hand edit between the update and the bar.** One observation at each adopter, not a tally.

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** BLOCKED · 22 unit(s) · node a · opened 2026-09-23 · streams tooling+deployer+playbook
ids DEPL-aRepatriatedFork-1 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 DEPL-aRepatriatedFork-17 DEPL-aRepatriatedFork-20 DEPL-aRepatriatedFork-21 DEPL-aRepatriatedFork-22 TOOL-aRepatriatedFork-1 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5
ids TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19 TOOL-aRepatriatedFork-20
ids TOOL-aRepatriatedFork-21

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [DEPL-aRepatriatedFork-1 — the charter renderer lets an answer win, and knows which file is its template](spec/2026-09-23-spec-DEPL-aRepatriatedFork-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-09-23 |
| [TOOL-aRepatriatedFork-10 — the memory-tree engine grandfathers what it says it does, and its rendered docs state the adopter's own facts](spec/2026-09-23-spec-TOOL-aRepatriatedFork-10.md) | 1 | 2 | CLOSED | rev-4 | 2026-09-23 |
| [TOOL-aRepatriatedFork-16 — check-install-prefix grades only what a repo ships](spec/2026-09-23-spec-TOOL-aRepatriatedFork-16.md) | 1 | 2 | CLOSED | rev-2 | 2026-09-23 |
| [TOOL-aRepatriatedFork-21 — a build README is `builds/<slug>/README.md`, at exactly that depth](spec/2026-09-24-spec-TOOL-aRepatriatedFork-21.md) | 1 | 1 | CLOSED | rev-2 | 2026-09-24 |
| [TOOL-aRepatriatedFork-3 — shipped Python names its encoding on every text-IO call](spec/2026-09-23-spec-TOOL-aRepatriatedFork-3.md) | 1 | 1 | CLOSED | rev-2 | 2026-09-23 |
| [TOOL-aRepatriatedFork-4 — review-harness gates find harnesses where adopters keep them](spec/2026-09-23-spec-TOOL-aRepatriatedFork-4.md) | 1 | 2 | CLOSED | rev-2 | 2026-09-23 |
| [TOOL-aRepatriatedFork-5 — pre-push runs only a tracked, unmodified gate command](spec/2026-09-23-spec-TOOL-aRepatriatedFork-5.md) | 1 | 2 | CLOSED | rev-3 | 2026-09-24 |
| [TOOL-aRepatriatedFork-6 — unattended set_fact refuses a value that can forge a second fact](spec/2026-09-23-spec-TOOL-aRepatriatedFork-6.md) | 1 | 2 | CLOSED | rev-2 | 2026-09-23 |
| [TOOL-aRepatriatedFork-7 — agent-cap: the nested-interpolation fix, and a declared lower cap](spec/2026-09-23-spec-TOOL-aRepatriatedFork-7.md) | 1 | 2 | CLOSED | rev-3 | 2026-09-24 |
| [TOOL-aRepatriatedFork-9 — row_grammar and check-arms take NicoCares' additions, and stop importing sibling engines](spec/2026-09-23-spec-TOOL-aRepatriatedFork-9.md) | 1 | 2 | CLOSED | rev-2 | 2026-09-24 |
| [DEPL-aRepatriatedFork-13 — an adopter's own engine is declared, not "unattributed"](spec/2026-09-23-spec-DEPL-aRepatriatedFork-13.md) | 2 | 2 | CLOSED | rev-4 | 2026-09-24 |
| [TOOL-aRepatriatedFork-15 — a kit whose shipped bytes move bumps its version](spec/2026-09-23-spec-TOOL-aRepatriatedFork-15.md) | 2 | 2 | CLOSED | rev-2 | 2026-09-24 |
| [TOOL-aRepatriatedFork-2 — every kit path a runtime string spells is derived](spec/2026-09-23-spec-TOOL-aRepatriatedFork-2.md) | 2 | 2 | CLOSED | rev-4 | 2026-09-24 |
| [TOOL-aRepatriatedFork-8 — the lander contracts inCMS carries](spec/2026-09-23-spec-TOOL-aRepatriatedFork-8.md) | 2 | 2 | CLOSED | rev-3 | 2026-09-24 |
| [DEPL-aRepatriatedFork-14 — hole probes and descriptors that cannot pass at an adopter](spec/2026-09-23-spec-DEPL-aRepatriatedFork-14.md) | 3 | 1 | CLOSED | rev-2 | 2026-09-24 |
| [DEPL-aRepatriatedFork-17 — govkit update is safe to run and says what it did](spec/2026-09-23-spec-DEPL-aRepatriatedFork-17.md) | 3 | 2 | CLOSED | rev-2 | 2026-09-24 |
| [DEPL-aRepatriatedFork-21 — apply never lands gov's bytes on a file the target owns](spec/2026-09-24-spec-DEPL-aRepatriatedFork-21.md) | 3 | 2 | CLOSED | rev-2 | 2026-09-24 |
| [TOOL-aRepatriatedFork-18 — the test suites that arm gov's gates reach adopters](spec/2026-09-23-spec-TOOL-aRepatriatedFork-18.md) | 4 | 2 | CLOSED | rev-3 | 2026-09-24 |
| [TOOL-aRepatriatedFork-19 — check-wiring judges every arm at a relocated layout](spec/2026-09-23-spec-TOOL-aRepatriatedFork-19.md) | 5 | 2 | CLOSED | rev-3 | 2026-09-24 |
| [TOOL-aRepatriatedFork-11 — unattended: build-root pathspecs stop at the build root, and a pull lands its hooks wired and its pins measurable](spec/2026-09-23-spec-TOOL-aRepatriatedFork-11.md) | 6 | 2 | CLOSED | rev-2 | 2026-09-24 |
| [TOOL-aRepatriatedFork-12 — memory-recall reads the adopter's corpus shape from conf](spec/2026-09-23-spec-TOOL-aRepatriatedFork-12.md) | 6 | 2 | CLOSED | rev-3 | 2026-09-24 |
| [DEPL-aRepatriatedFork-20 — inCMS converges onto gov's memory-tree programs](spec/2026-09-23-spec-DEPL-aRepatriatedFork-20.md) | 7 | 2 | BLOCKED | rev-4 | 2026-09-24 |
<!-- /gen:build-units -->

Records: 50 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: DEPL-aRepatriatedFork-1 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 DEPL-aRepatriatedFork-17 DEPL-aRepatriatedFork-20 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16
TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 DEPL-aRepatriatedFork-21 TOOL-aRepatriatedFork-21.
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
| 7 | `DEPL-aRepatriatedFork-20` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
