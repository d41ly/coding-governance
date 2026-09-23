---
slug: aRepatriatedFork
node: a
opened: 2026-09-23
streams: tooling+deployer+playbook
roster: TOOL+DEPL
ids: DEPL-aRepatriatedFork-1 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 DEPL-aRepatriatedFork-17 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19
---

# aRepatriatedFork — what the a7c78ad2 pull proved gov still does not carry, specced as gov's to fix

## The problem this build exists to solve

On 2026-09-23 both adopters were pulled from gov `fd240496` to `a7c78ad2`: inCMS, and NicoCares (nc),
which inCMS pins as a submodule. `dRetiredFork` promised that `govkit update --write` would be the whole
update and that adopter fixes would move upstream. It closed DEFERRED, and the pull measured what that
left. `govkit update` left 27 engine rows at inCMS and 32 at nc `unattributed`, so kits landed half old
and half new and both bars went red. The rows were pinned to their nearest gov vintage and three-way
merged by hand, 59 conflict hunks at inCMS alone. The hand merge then stripped 16 lone CR bytes out of
awk programs and reverted one gov fix, and neither was caught until an audit read every diff.

A per-file audit of every adopter file that still differs from gov HEAD then sorted what was left.
Some of it is adopter code gov lacks, including two security guards nc carries alone. Some is gov
defects that force the fork. The rest is govkit mechanics that made the pull unsafe to run unattended.
Nineteen units, each specced against gov HEAD and both adopters with `file:line` on both sides.

The evidence of record is in each spec. Two adopter landings carry the pull itself: inCMS `9a0e5ebbe`
(pending push at the time of writing) and nc `b6dfacac`, which records the charter migration and the
check-install-prefix deselection this build explains.

## Expected improvements

- `govkit update --write` is the whole update at both adopters: nothing to pin, nothing to hand-merge.
  That is `dRetiredFork`'s done-condition, and this build is what stands between it and the trees.
- Two security holes close in gov. The pre-push hook will run only a tracked, unmodified gate command,
  and unattended's `set_fact` will refuse a value that can forge a second run fact.
- inCMS's `.governance/kits.json` divergence map and nc's carve-out census both shrink to what is
  genuinely the adopter's own. The units that retire each row or carve-out name it.
- The gates adopters run stop redding on gov's own bytes: kit-versions, check-install-prefix,
  gate-arms, encoding-posture and the hole probes.

## Detriments if this is not built

- Every pull stays a build rather than a command: the next one repeats the pin, the merge and the audit.
- A hand merge of gov bytes keeps corrupting them silently. The CR loss this pull caused broke three
  programs, and no gate saw it.
- Both security holes stay live in gov and in every future adopter.
- The adopters keep diverging at gov's commit rate. Eight kits moved shipped bytes at an unchanged
  version inside this one pull.

## Build-level rules

- **A unit retires a fork only by making gov's bytes run verbatim at the adopter.** Each spec's
  acceptance names the command, run at inCMS and nc, that shows it. An argument that it should work is
  not acceptance.
- **Every absorbed adopter fix is reproduced at gov HEAD first.** `TOOL-aRepatriatedFork-6` found nc's
  own guard bypassable through `awk -v`, so taking an adopter fix as-is is not assumed safe.
- **A path fix is a derivation or a render**, per `dRetiredFork`'s rule. A new conf key is justified
  only where the value is an adopter's DECISION, not its layout.
- **No new bar leg without its ceiling and its testsuite-count row**, and every new gate's red case is
  observed before it lands.
- **The two security units land first within their order**, and neither ships behind a flag: a guard
  that is off by default is the hole.

## Parked decisions (owner turns)

- **Kit suites ship to adopters (`TOOL-aRepatriatedFork-18`).** This narrows `TOOL-aQuenchedHarness-3`,
  which withheld the suites, to legs only. That ruling never considered that check-arms reads the
  sibling suite at the adopter.
- **A declared fan-out cap (`TOOL-aRepatriatedFork-7`).** `dRetiredFork` parked "may the cap become a
  key" as an owner turn. nc runs 4 and forks five files to say so. The spec proposes a lower-only key.
- **`KIT_MANIFEST_VERSION` is also the manifest format number (`TOOL-aRepatriatedFork-15`).** Bumping
  it for a code change would ask every adopter to upgrade a format that did not change. The spec
  proposes splitting it into two constants.
- **Shell reading the receipt (`TOOL-aRepatriatedFork-2` vs `-19`).** Unit 2 would forbid it. Unit 19
  needs it at inCMS, where nothing else can find the renamed kit folders. One answer before either builds.
- **inCMS's own engines (`DEPL-aRepatriatedFork-13`).** Declare them adopter-owned against a contract,
  or converge them on gov's. The spec builds the declaration either way and lists the contract.

## Adopter-side findings (not this build's to fix, recorded so they are not lost)

- **inCMS `.githooks/pre-push` runs `eval "$INCMS_PUSH_GATE_CMD"`**, so `INCMS_PUSH_GATE_CMD=true` lands
  a push over a red bar. It is the same class as `TOOL-aRepatriatedFork-5`, in inCMS's own hook.
- **nc's `set_fact` newline guard is bypassed** by a literal `\n` that `awk -v` expands after the guard
  ran. `TOOL-aRepatriatedFork-6` specifies the upstream fix; nc runs the bypassable copy until it pulls.
- **`BASH_ENV` reaches both gov's and nc's hooks** and can fake the decision line and the lander marker.
  Recorded in `TOOL-aRepatriatedFork-5` as a residual of the protocol's existing tool-shim class, not
  closed.
- **inCMS's `kits.json` divergence claims are partly stale.** The settings.json walk-up, the SSH keepalive
  and `check-workflow-syntax.js`'s `diverged` role describe code that has since moved.

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
| 2 | `TOOL-aRepatriatedFork-2` | 2 | every kit path a runtime string spells is derived |
| 2 | `TOOL-aRepatriatedFork-8` | 2 | the lander contracts inCMS carries |
| 2 | `DEPL-aRepatriatedFork-13` | 2 | an adopter's own engine is declared, not "unattributed" |
| 2 | `TOOL-aRepatriatedFork-15` | 2 | a kit whose shipped bytes move bumps its version |
| 3 | `DEPL-aRepatriatedFork-14` | 1 | hole probes and descriptors that cannot pass at an adopter |
| 3 | `DEPL-aRepatriatedFork-17` | 2 | govkit update is safe to run and says what it did |
| 4 | `TOOL-aRepatriatedFork-18` | 2 | the test suites that arm gov's gates reach adopters |
| 5 | `TOOL-aRepatriatedFork-19` | 2 | check-wiring judges every arm at a relocated layout |
| 6 | `TOOL-aRepatriatedFork-11` | 2 | unattended: pathspecs stop at the build root; a pull lands hooks wired and pins measurable |
| 6 | `TOOL-aRepatriatedFork-12` | 2 | memory-recall reads the adopter's corpus shape from conf |

The `#` column is the `order` each spec declares, derived from its `### Edges`: a unit's order is one
past the highest order it consumes from. Order 1 is nine independent units, two of them the security
fixes.

**The build is done when a `govkit update --write` from gov HEAD at inCMS and at nc lands every row,
re-stamps `gov_commit`, leaves no conflict order, and both adopters' full bars are green on the result
with no hand edit between the update and the bar.** One observation at each adopter, not a tally.

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 19 unit(s) · node a · opened 2026-09-23 · streams tooling+deployer+playbook
ids DEPL-aRepatriatedFork-1 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 DEPL-aRepatriatedFork-17 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9
ids TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [DEPL-aRepatriatedFork-1 — the charter renderer lets an answer win, and knows which file is its template](spec/2026-09-23-spec-DEPL-aRepatriatedFork-1.md) | 1 | 2 | SPECCED | rev-1 | 2026-09-23 |
| [TOOL-aRepatriatedFork-10 — the memory-tree engine grandfathers what it says it does, and its rendered docs state the adopter's own facts](spec/2026-09-23-spec-TOOL-aRepatriatedFork-10.md) | 1 | 2 | SPECCED | rev-1 | 2026-09-23 |
| [TOOL-aRepatriatedFork-16 — check-install-prefix grades only what a repo ships](spec/2026-09-23-spec-TOOL-aRepatriatedFork-16.md) | 1 | 2 | SPECCED | rev-1 | 2026-09-23 |
| [TOOL-aRepatriatedFork-3 — shipped Python names its encoding on every text-IO call](spec/2026-09-23-spec-TOOL-aRepatriatedFork-3.md) | 1 | 1 | SPECCED | rev-1 | 2026-09-23 |
| [TOOL-aRepatriatedFork-4 — review-harness gates find harnesses where adopters keep them](spec/2026-09-23-spec-TOOL-aRepatriatedFork-4.md) | 1 | 2 | SPECCED | rev-1 | 2026-09-23 |
| [TOOL-aRepatriatedFork-5 — pre-push runs only a tracked, unmodified gate command](spec/2026-09-23-spec-TOOL-aRepatriatedFork-5.md) | 1 | 2 | SPECCED | rev-1 | 2026-09-23 |
| [TOOL-aRepatriatedFork-6 — unattended set_fact refuses a value that can forge a second fact](spec/2026-09-23-spec-TOOL-aRepatriatedFork-6.md) | 1 | 2 | SPECCED | rev-1 | 2026-09-23 |
| [TOOL-aRepatriatedFork-7 — agent-cap: the nested-interpolation fix, and a declared lower cap](spec/2026-09-23-spec-TOOL-aRepatriatedFork-7.md) | 1 | 2 | SPECCED | rev-1 | 2026-09-23 |
| [TOOL-aRepatriatedFork-9 — row_grammar and check-arms take NicoCares' additions, and stop importing sibling engines](spec/2026-09-23-spec-TOOL-aRepatriatedFork-9.md) | 1 | 2 | SPECCED | rev-1 | 2026-09-23 |
| [DEPL-aRepatriatedFork-13 — an adopter's own engine is declared, not "unattributed"](spec/2026-09-23-spec-DEPL-aRepatriatedFork-13.md) | 2 | 2 | SPECCED | rev-1 | 2026-09-23 |
| [TOOL-aRepatriatedFork-15 — a kit whose shipped bytes move bumps its version](spec/2026-09-23-spec-TOOL-aRepatriatedFork-15.md) | 2 | 2 | SPECCED | rev-1 | 2026-09-23 |
| [TOOL-aRepatriatedFork-2 — every kit path a runtime string spells is derived](spec/2026-09-23-spec-TOOL-aRepatriatedFork-2.md) | 2 | 2 | SPECCED | rev-1 | 2026-09-23 |
| [TOOL-aRepatriatedFork-8 — the lander contracts inCMS carries](spec/2026-09-23-spec-TOOL-aRepatriatedFork-8.md) | 2 | 2 | SPECCED | rev-1 | 2026-09-23 |
| [DEPL-aRepatriatedFork-14 — hole probes and descriptors that cannot pass at an adopter](spec/2026-09-23-spec-DEPL-aRepatriatedFork-14.md) | 3 | 1 | SPECCED | rev-1 | 2026-09-23 |
| [DEPL-aRepatriatedFork-17 — govkit update is safe to run and says what it did](spec/2026-09-23-spec-DEPL-aRepatriatedFork-17.md) | 3 | 2 | SPECCED | rev-1 | 2026-09-23 |
| [TOOL-aRepatriatedFork-18 — the test suites that arm gov's gates reach adopters](spec/2026-09-23-spec-TOOL-aRepatriatedFork-18.md) | 4 | 2 | SPECCED | rev-1 | 2026-09-23 |
| [TOOL-aRepatriatedFork-19 — check-wiring judges every arm at a relocated layout](spec/2026-09-23-spec-TOOL-aRepatriatedFork-19.md) | 5 | 2 | SPECCED | rev-1 | 2026-09-23 |
| [TOOL-aRepatriatedFork-11 — unattended: build-root pathspecs stop at the build root, and a pull lands its hooks wired and its pins measurable](spec/2026-09-23-spec-TOOL-aRepatriatedFork-11.md) | 6 | 2 | SPECCED | rev-1 | 2026-09-23 |
| [TOOL-aRepatriatedFork-12 — memory-recall reads the adopter's corpus shape from conf](spec/2026-09-23-spec-TOOL-aRepatriatedFork-12.md) | 6 | 2 | SPECCED | rev-1 | 2026-09-23 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: DEPL-aRepatriatedFork-1 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 DEPL-aRepatriatedFork-17 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19
TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9.

Ids no `spec-audit` record has ever named: DEPL-aRepatriatedFork-1 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 DEPL-aRepatriatedFork-17 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 TOOL-aRepatriatedFork-18
TOOL-aRepatriatedFork-19 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `DEPL-aRepatriatedFork-1`, `TOOL-aRepatriatedFork-10`, `TOOL-aRepatriatedFork-16`, `TOOL-aRepatriatedFork-3`, `TOOL-aRepatriatedFork-4`, `TOOL-aRepatriatedFork-5`, `TOOL-aRepatriatedFork-6`, `TOOL-aRepatriatedFork-7`, `TOOL-aRepatriatedFork-9` | yes |
| 2 | `DEPL-aRepatriatedFork-13`, `TOOL-aRepatriatedFork-15`, `TOOL-aRepatriatedFork-2`, `TOOL-aRepatriatedFork-8` | yes |
| 3 | `DEPL-aRepatriatedFork-14`, `DEPL-aRepatriatedFork-17` | yes |
| 4 | `TOOL-aRepatriatedFork-18` | no |
| 5 | `TOOL-aRepatriatedFork-19` | no |
| 6 | `TOOL-aRepatriatedFork-11`, `TOOL-aRepatriatedFork-12` | yes |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
