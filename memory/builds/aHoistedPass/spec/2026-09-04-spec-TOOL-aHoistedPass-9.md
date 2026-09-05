# TOOL-aHoistedPass-9 — the adopter without the harness is told, on every bar

**Status:** CLOSED · rev-6 · 2026-09-05 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md](../build/2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md) | research | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 DEPL-aHoistedPass-1 |
| [2026-09-05-build-TOOL-aHoistedPass-9-1-acceptance-ledger.md](../build/2026-09-05-build-TOOL-aHoistedPass-9-1-acceptance-ledger.md) | journal | — |
| [2026-09-05-prompt-TOOL-aHoistedPass-9-brief.md](../prompts/2026-09-05-prompt-TOOL-aHoistedPass-9-brief.md) | journal | — |
| [2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round1.md) | spec-audit | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 DEPL-aHoistedPass-1 |
| [2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round2.md) | spec-audit | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 DEPL-aHoistedPass-1 |
| [2026-09-06-review-TOOL-aHoistedPass-1-closing-diff-round1.md](../reviews/2026-09-06-review-TOOL-aHoistedPass-1-closing-diff-round1.md) | diff-review | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 DEPL-aHoistedPass-1 |

<!-- /gen:spec-records -->

## 1. Goal

Add check 31 to `tools/unattended/check-unattended.sh` so that when the route the `passes-harnessed`
directive names does not resolve in the tree being graded, the leg says which case it could not reach
instead of exiting green with nothing printed. This is the gate-time half of ruling D4;
`DEPL-aHoistedPass-1` is the install-time half, and neither subsumes the other because they catch
different moments — the install-time arm runs once, at the act that creates the gap, and only for
installs made after it lands, while this one runs on every bar of every adopter forever, including
the population the install-time arm can never reach.

## 2. Scope (IN)

- **S1.** A new numbered check, **31**, in `tools/unattended/check-unattended.sh`, placed after check
  30 and before `exit "$status"` — outside both `SCOPE` blocks, exactly where check 30 sits.
- **S2.** The check reads the section the `passes-harnessed` handle names, out of the directive
  registry the leg has already parsed, rather than out of a literal `M6` typed into this check.
- **S3.** Five announced-skip branches on the kit's existing REPORT channel, one per case the check
  cannot compare, each in the file's own `check <n> skipped for <subject> — <why>` grammar.
- **S4.** One `fail 31` branch: a named route script that is absent while the directory holding it is
  present.
- **S5.** The directory under test is derived with `dirname` from the path the section itself names,
  never from a literal install prefix.
- **S6.** Staged-break arms plus one green control in `tools/unattended/check-unattended.test.sh`,
  of which one is the positive assertion `fail 31` owes under the arms meta-gate. **The count is
  SIX, not the four rev-1 wrote**, and the four was never consistent with this document's own §6:
  AC7 alone demands two observations (a foreign prefix whose directory is absent and one whose
  directory the arm creates), and AC2, AC3, AC5 and AC6 demand one each. The arms are one per branch
  of the §4 table that a fixture can reach — F1, S5, S2, S4, and S5-then-F1 at a foreign prefix —
  plus S1, which is armed by emptying the driver's `DIRECTIVES_CORE` rather than by a scoped run;
  §4's Placement paragraph says why that route and not the other.
- **S7.** ~~The `unattended` kit version bump 1.17 → 1.18 the payload change owes: three engine
  constants and the marker in all five tracked `tools/unattended/*.template.md`.~~ — **SPENT.**
  `DEPL-aHoistedPass-1`'s section 8 F1 took that single move at `order 2` — and then rev-5 of THAT
  spec PARKED it to the owner as an M3 veto-2 turn, so order 2 moved nothing and the tree is still at
  `1.17` when this unit runs. rev-3 wrote "already `1.18` by the time it runs" here and rev-4 recorded
  the park without coming back for this sentence; the assertion below never depended on the number,
  which is why it survived both. What this unit owes is an
  ASSERTION: `bash tools/check-kit-versions.sh` exits 0 at whatever version the tree carries,
  and this unit moves it no further. A kit version is a release, not a per-commit stamp, so a second
  bump inside one build records a release that never shipped.

## 3. Non-goals (OUT)

- **Not a whole-leg skip.** Not one of the leg's other numbered checks needs the route to exist, so a
  whole-leg skip would discard every one of their verdicts to announce this one — the
  green-by-absence class, one level up. The counts rev-1 wrote here are gone: the file's own header
  gives the recipe for the `fail`-number set and `check-arms.py --report` gives the branch pair, and
  both had already moved under this paragraph before the unit landed.
- **Not a refusal.** An absent route directory means the adopter never installed the kit that holds
  it. Redding a standing bar over an install decision the bar cannot undo punishes the wrong act on
  the wrong day; the refusal belongs at `govkit apply`, which is `DEPL-aHoistedPass-1`.
- **Not the default channel.** The kit's own ruling at `tools/unattended/check-unattended.sh:15-21`
  (`TOOL-dUnstalledConvoy-6`) routes skips to REPORT and admits only check 7's exclusion notice on
  stdout, because an exclusion is a positive finding that changed the verdict and this skip is not.
  Taking stdout anyway would leave the file's contract line at `:12-13` asserting something the code
  disproves.
- **Not the remedy.** The check names the absence, never the preflight `--waive` that would relax the
  directive. A gate handing out its own bypass is a different defect.
- **Not the M6 sentence.** `TOOL-aHoistedPass-2` writes the route sentence and its backticked paths.
  This unit reads whatever that sentence ends up saying, and lands after it.
- **Not a second reader of a missing section.** Check 16 arm B already refuses a directive naming a
  section that does not exist. Check 31 skips that case and names arm B as its owner.

## 4. Design

### Data model

The check has one input population: the backticked tokens inside the slice of
`memory/guides/BUILD-METHOD.md` that the `passes-harnessed` handle names, matching a route-script
shape. Call that set `P`.

| step | source read | derived value |
|---|---|---|
| the handle's section | `$core`, built at `tools/unattended/check-unattended.sh:1474-1487` from the driver's `DIRECTIVES_CORE` | `sec` — the section name for `passes-harnessed` |
| the carrier | `$M/guides/BUILD-METHOD.md`, with `M="$MEMORY_ROOT"` at `:165` — the same file arm B opens at `:1589` | the file, or its absence |
| the slice | `awk` from `^## <sec>( \|$)` to the next `^## ` | the section body |
| `P` | backticked tokens in that slice matching `(^\|/)workflows/<name>.js` | zero or more repo-relative paths |
| the directory | `dirname` of each element of `P` | the route's home in THIS tree |

### The outcome split, and why each branch falls where it does

Six branches. Five announce, one fails. The three cases that need justifying are marked.

| # | state | verdict | subject named |
|---|---|---|---|
| S1 | `${core:-}` carries no `passes-harnessed` handle | announced skip | the driver's registry |
| S2 | the carrier `$M/guides/BUILD-METHOD.md` is absent | **announced skip** | the carrier path |
| S3 | the carrier has no `^## <sec>` heading | announced skip | the carrier path |
| S4 | the section carries no backticked route path — `P` is empty | **announced skip** | the carrier path |
| S5 | a path in `P` whose `dirname` is not a directory | **announced skip** | that path |
| F1 | a path in `P` whose `dirname` IS a directory and which is not a file | **`fail 31`** | that path |

S5 and F1 are decided PER PATH, not per check, so a tree carrying one of two named scripts fails on
the one it lacks and says nothing about the one it has.

**S2 — why a skip and not silence, stated because the obvious reading is wrong.** Arm B's own
comment at `tools/unattended/check-unattended.sh:1586-1588` says it is *SILENT when the carrier is
absent*, and it is: the `if [ -f … ]` at `:1589` guards the whole loop and nothing is emitted. Check
31 takes arm B's **disposition** — do not fail an adopter who installed this kit without the
memory-tree one — and **rejects its silence**, because silence is precisely the shape this unit
exists to remove. An announced skip is the opposite of arm B's behaviour, not an inheritance of it.

**S4 — this is the case the tree is in today, and it is why the check is born skipping in an adopter
tree.** Measured at `c4fcf5ad`: the only `workflows/` path anywhere in `memory/guides/BUILD-METHOD.md`
is at `:225`, inside M8, and M6 spans `:161`–`:194` and names none. Since this unit lands AFTER
`TOOL-aHoistedPass-2`, gov's own tree will already carry the two backticked route paths by the time
check 31 exists, so **in this repo the check grades on its first run.** It is born skipping only in an
adopter tree whose `BUILD-METHOD.md` render predates the memory-tree kit version carrying the new M6
sentence — which is the whole population this unit was asked to reach.

**S5 against F1 — the split IS the ruling.** An absent DIRECTORY means the route's kit was never
installed here; that is an install-time fact and `DEPL-aHoistedPass-1` refuses it at the moment of the
act. A missing FILE inside a present directory means the kit was taken and the route is broken, which
is a defect in that tree and theirs to fix.

### The three shapes, and what makes them byte-distinguishable

| outcome | channel | bytes |
|---|---|---|
| pass | none | nothing at all — the contract line at `tools/unattended/check-unattended.sh:12-13` is *Exit 0 + no output = clean* |
| announced skip | REPORT, off by default (`REPORT=${GOV_UNATTENDED_REPORT:-0}` at `:590`, `report()` at `:591`) | `unattended-report: check 31 skipped for <subject> — <why>` |
| violation | stdout, and `status=1` | `UNATTENDED check 31 FAILED — <why>: <path>` (`fail()` at `:93`) |

The ` for <subject>` segment is not optional. Every existing skip line in the file carries one —
`:1033`, `:1815`, `:1839`, `:1852`, `:1929`, `:1938`, `:1942`, and the non-skip `observed` line at
`:1983` — so a line without it would be a second grammar in a file that has one.

Because the announcement is what makes each unreachable case visible, **the announced skip IS this
check's liveness assertion**, and no separate vacuity branch is owed. That is a claim about this
check only: it says nothing about whether the route it names is correct.

### Inventory

**The check number is 31, and the enumeration is the evidence.** Run at `c4fcf5ad` with the file's
own header recipe at `tools/unattended/check-unattended.sh:4-7`:

| axis | result |
|---|---|
| `fail <n>` numbers in use | **1–22 and 24–30** — 29 distinct numbers over 174 branches |
| numbers claimed as a LABEL with no `fail` | **23**, by four `report` calls (`:1929`, `:1938`, `:1942`, `:1983`) and three stdout `printf` violation lines (`:1981`, `:2002`, `:2018`) |
| stray `check <n>` mentions that claim nothing here | `check 34` at `:1242` and `check 48` at `:1806`, both naming OTHER checkers' numbers in prose |
| first genuinely free number | **31** |

23 is not free. It is a live check with its own stdout violations and its own skip announcements; it
simply reports through `printf` rather than `fail`, so the header recipe alone would hand it back as
available.

### Placement, and what it costs

Check 31 goes after check 30 and before `exit "$status"`, outside both scope guards. The line
numbers rev-1 recorded moved: at the run's BASE `e828f778` the file is 2952 lines, check 30 spans
`:2923`–`:2951`, `exit "$status"` is `:2952`, the `only28` block is `:110`–`:2352` and the `skip28`
block is `:2354`–`:2920`. The PLACEMENT is unchanged; only the citations moved. Consequences:

- Check 31 is outside both guards, so it runs under `--skip 28` as well as on a default bar. Its
  cost is one `awk` over one file plus two filesystem tests per named path, against a leg whose
  declared ceiling in `tools/gate-legs.json` is 16040.
- `$core` is built INSIDE the `only28` block, so under `--only 28` it is unset and `set -u` would
  kill the script. The check reads `${core:-}` and treats an empty value as branch S1.

**`--only 28` DOES NOT REACH CHECK 31 TODAY, and rev-4 asserted that it did.** Measured on this
branch at `e828f778`: `bash tools/unattended/check-unattended.sh --only 28` exits **1** printing
`tools/unattended/check-unattended.sh: line 2932: MEMORY_ROOT: unbound variable`. Check 30 sits
outside both guards and opens with `[ -d "$MEMORY_ROOT/builds" ]`, while `MEMORY_ROOT` is assigned
from the conf INSIDE the `only28` block — so under that flag the leg dies at check 30, twenty lines
before check 31 exists. This is a defect in check 30 (`TOOL-dHonouredPark`) and not in this unit, it
predates this unit, and it is filed as `TOOL-aHoistedPass-37` rather than fixed here: the one-token
fix `${MEMORY_ROOT:-}` trades a crash for a SILENT skip of check 30's corpus walk, which is the
class this whole build exists to remove, so the repair is a unit with its own reasoning.

Two things follow, and both are what this rev changes rather than assertions carried forward.
`${core:-}` is KEPT — not because it makes `--only 28` work, which nothing in this unit can, but
because it is what stops check 31 being the SECOND crash on that path the day check 30's is fixed.
And S1 is armed by emptying the driver's `DIRECTIVES_CORE` in the fixture, which reaches the same
branch by its own subject — a registry with no readable `passes-harnessed` handle — on a default
run that the suite can actually execute.

### The arms meta-gate, priced

`tools/unattended/check-unattended.sh:93` defines `fail() {`, which puts it in the discovered
population of `tools/memory-tree/check-arms.py` (`:9-12`: a tracked `*.sh` that DEFINES the helper,
tested by the sibling `<stem>.test.sh`). So `fail 31` owes either a POSITIVE assertion in
`tools/unattended/check-unattended.test.sh` naming its own failure text, or a row in the shrink-only
`memory/project/unarmed-branches.txt`. This spec takes the arm; a pin row would be dishonest, because
the branch is reachable by deleting one file in a fixture.

**What it does NOT owe, measured rather than assumed.** `.memory-tree.conf:203` declares
`ARMS_FLOORS="… tools/unattended/check-unattended.sh:101:100 …"`, and
the pin for that gate is `101:100`. The floor comparison at
`tools/memory-tree/check-arms.py:288-291` is `got < want`, one-sided upward, so adding one armed
branch cannot breach it and **no `ARMS_FLOORS` edit is owed.** Raising the floor to track reality is a
separate act with its own reasoning and is not smuggled into this unit. rev-1 wrote the live pair —
174 branches, 166 armed — into this paragraph and it was wrong by two before this unit's own commit,
because `TOOL-aHoistedPass-2` added a branch in between. `--report` owns that pair; ask it.

The arm's own EXECUTION is off the bar. `tools/unattended/check-unattended.test.sh` is not a leg —
`grep -c` against `tools/gate-legs.json` returns 0 — under the 2026-08-23 self-test ruling. The
compensating check is stated at `tools/unattended/run-unattended-gates.sh:25`: the DoD for work
touching this directory is a green `--selftests` verdict pasted into the landing report. That suite
is hours on node `a`; `tools/unattended/check-unattended.test.sh` accepts `--shard <i>/2`, which is
how to pay for it.

### Migration

None. No file is added, no leg is registered, no conf key is declared, and no inventory key is
minted, so `memory/map/features/unattended.md` keeps its `[claims]` block unchanged. The check adds no
`tools/` literal — every path it tests comes out of the carrier's own bytes — so
`tools/install-prefix-carried.txt` keeps its row for this file at 3.

### Rollout

Lands after `TOOL-aHoistedPass-2`, in one code commit plus one records commit for the fixes its own
bug-class checklist selected. It is a read-only check on a read-only leg; the
rollback is deleting the block.

**This unit is NOT an owner turn, and the correction matters more than the classification does.**
rev-1 derived owner-turn status transitively from carrying the `1.17 → 1.18` bump, because
`tools/check-kit-versions.sh:164-192` requires the marker in every tracked
`tools/unattended/*.template.md` and `SKILL.template.md` is one of the five. That coupling is spent:
`DEPL-aHoistedPass-1` performs the move at `order 2` and this unit no longer touches a template
marker at all. The files it does edit are `check-unattended.sh` and its test file, neither of which
is on ruling D1's veto-2 list. **A classification derived from an edit the unit does not make is the
one class of spec defect that changes whether an unattended run may land the unit at all**, which is
why this paragraph now names the carriers this unit actually edits rather than a bump it does not
own.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/check-unattended.sh` | the check-31 block after `:2903` |
| `tools/unattended/check-unattended.test.sh` | four staged arms plus a green control |

Two rows left this table at rev-2 with S7: `tools/unattended/unattended.sh` and
`tools/unattended/check-pass-order.sh` were booked for their `KIT_UNATTENDED_VERSION` constants, and
the five tracked `tools/unattended/*.template.md` for their `gov:kit unattended@` marker.
`DEPL-aHoistedPass-1` owns all seven at `order 2`. This unit reads them and edits none.

### Alternatives rejected

- **A literal `tools/workflows/` test.** `TOOL_ROOT` renders to `tools/` here but to the empty string
  at a root install (`tools/memory-tree/adopt-memory-tree.sh:36-37`), so a literal is wrong in an
  adopter's tree in both directions: it would fail a correct route installed at another prefix, or
  skip forever over a broken one. `dirname` of the named path is the same number of lines.
- **A new checker script.** It would need its own leg row, its own registry claim and its own arms
  sibling, to answer a question the leg that already reads this exact file can answer in one block.
- **Re-reporting the missing section.** Check 16 arm B already fails 16 when a directive names an
  absent section. Two legs answering one question is the class this file's own header exists to
  remove.

## 5. Production-readiness checklist

- **security** — N/A. The check is read-only, spawns nothing, and reads two tracked paths plus two
  filesystem tests.
- **perf / scale** — one `awk` over one file, plus `-f`/`-d` per named path. Against the leg's 16040
  ceiling in `tools/gate-legs.json` this is unmeasurable.
- **a11y** — N/A. A shell leg with no user surface.
- **i18n** — N/A. The messages are this kit's own English, like every other message in the file.
- **error / empty / loading states** — this IS the unit: five explicitly announced empty states, each
  naming its own subject and reason.
- **observability** — the REPORT channel, off by default. Named as a cost in §8 rather than argued
  away: a green default bar prints nothing, so the announcement reaches only a reader who asks for it
  with `GOV_UNATTENDED_REPORT=1`.
- **risks** — no concurrency, no writes, no rollback hazard. The one real risk is that the backtick
  key stops matching a reworded M6 sentence and the check degrades to a silent-by-default skip; §8
  fork F1 carries it.
- **testing + left-shift gates** — six staged arms and a green control, of which one is the positive
  arm `fail 31` owes. Their execution is off the bar by the 2026-08-23 ruling and rides
  `bash tools/unattended/run-unattended-gates.sh --selftests` by hand.
- **migration / rollback** — none owed; deleting the block reverts it.
- **user docs** — none. The check has no user-facing page; the four `##` sections of
  `tools/unattended/README.md` describe the kit, not per-check behaviour, and no count in them moves.

## 6. Acceptance criteria

- **AC1** — When `grep -oE 'fail [0-9]+' tools/unattended/check-unattended.sh | grep -oE '[0-9]+' | sort -un`
  is run on the landed file, it prints 1–22 and 24–31, and `git grep -n 'check 23'` on that file still
  shows 23 claimed only by `report` and `printf` labels with no `fail 23`.
- **AC2** — When the fixture deletes the route script `unattended-unit.js` out of `tools/workflows/`
  and leaves that directory in place, `bash tools/unattended/check-unattended.sh` prints
  `UNATTENDED check 31 FAILED — ` naming the deleted path and exits 1. **This is the failing case,
  staged and observed RED before the check lands, then unstaged.**
- **AC3** — When `rm -rf tools/workflows/` removes the directory entirely,
  `bash tools/unattended/check-unattended.sh` exits 0 printing nothing, and
  `GOV_UNATTENDED_REPORT=1 bash tools/unattended/check-unattended.sh` prints
  `unattended-report: check 31 skipped for ` naming that same path.
- **AC4** — When the intact tree is graded,
  `GOV_UNATTENDED_REPORT=1 bash tools/unattended/check-unattended.sh` emits no line containing
  `check 31` on either channel, so the three outcomes are byte-distinguishable from each other and a
  pass is distinguishable from a skip.
- **AC5** — When `memory/guides/BUILD-METHOD.md` is removed from the fixture,
  `GOV_UNATTENDED_REPORT=1 bash tools/unattended/check-unattended.sh` prints the carrier-absent skip
  naming that path, and no `fail 31` appears.
- **AC6** — When the route paths are deleted from the section but the carrier and its heading remain,
  the skip line naming the empty route set prints; and at base `c4fcf5ad` the same observation holds
  unmodified, because `memory/guides/BUILD-METHOD.md:161`–`:194` names no route script and the only
  `workflows/` path in that file is at `:225`, inside M8.
- **AC7** — When the section's route path is rewritten to a foreign prefix that is not `tools/`, the
  verdict follows the named path's own `dirname` rather than a literal, asserted by an arm that
  produces a skip for a foreign prefix whose directory is absent and a `fail 31` for one whose
  directory it creates.
- **AC8** — When `python tools/memory-tree/check-arms.py --check` runs, it exits 0, and
  `python tools/memory-tree/check-arms.py --report` shows check 31 branch 1 as ARMED for
  `tools/unattended/check-unattended.test.sh`, with no row added to
  `memory/project/unarmed-branches.txt` and no edit to `ARMS_FLOORS` in `.memory-tree.conf`.
- **AC9** — When `bash tools/unattended/check-unattended.sh --skip 28` is run on the intact tree it
  exits 0 and emits no `check 31` line, so the check is reached and silent outside the 28 region.
  **The `--only 28` half of this criterion is struck**, and the observation replaces it: that run
  exits 1 at `line 2932: MEMORY_ROOT: unbound variable` in check 30, before check 31, both before
  and after this unit lands. Rerun it to confirm the number is unchanged by this unit — the failure
  is check 30's and is filed as `TOOL-aHoistedPass-37`. The registry-unreadable branch is witnessed
  instead by AC14.
- **AC14** — When the fixture empties the driver's `DIRECTIVES_CORE`,
  `GOV_UNATTENDED_REPORT=1 bash tools/unattended/check-unattended.sh` prints
  `check 31 skipped for ` naming the driver as its subject and saying no `passes-harnessed` handle is
  readable, and no `fail 31` appears.
- **AC10** — When `bash tools/unattended/check-unattended.test.sh` is run to completion, sharded as
  `--shard 1/2` and `--shard 2/2`, it reports PASS with a raised assertion count and no existing
  `GOV_UNATTENDED_REPORT=1` arm flips on the new line.
- **AC11** — When `bash tools/check-kit-versions.sh` runs on the landing tree it exits 0, with the
  three `unattended` engine constants and the marker in all five tracked
  `tools/unattended/*.template.md` AGREEING — whatever value `DEPL-aHoistedPass-1` set. **No literal
  version number appears in this criterion, and that is the fix rather than an omission.** rev-1
  asserted `KIT_UNATTENDED_VERSION=1.18`, which at `order 6` is green because a different unit moved
  it; a criterion that passes on somebody else's work witnesses nothing about this one. AC13 below is
  what witnesses this unit.
- **AC12** — When `bash tools/check-install-prefix.sh` runs, it exits 0 and
  `tools/install-prefix-carried.txt` still records 3 for this checker, because the block spells no
  install-prefixed literal.
- **AC13** — When `bash tools/unattended/check-unattended.sh` runs on the landed tree with the route
  present, it exits 0 and its stdout is byte-identical to the same run before this unit landed. **Not
  "with no output", which rev-1 wrote and which is false of this repo for reasons that predate this
  unit**: check 7's EXCLUDED notices and check 23's dispatch-join notices both print on the DEFAULT
  channel by design — the two exceptions the file's own header at `:14`–`:28` names — and neither
  sets `status`. The claim worth making is that this unit adds nothing to that stream and does not
  move the verdict, which a before/after byte comparison says and "no output" cannot.

- **AC15** — When the suite's derived build-method carrier is rendered, it names every section the
  registry cites AND every handle that cites one, both counted from the registry rather than typed,
  and check 17's green control at `tools/unattended/check-unattended.test.sh` exits 0 again. This is
  the rev-5 AMEND, not part of the original design; it is here because a criterion nobody wrote down
  is a repair nobody re-checks.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `unattended skill wiring` · `install-prefix (shipped surface)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The first two are the ones that bind: `unattended kit gate` is the leg being changed, and both it and
the arms gate are chunk `declarations`, subject `repo`, with no guard, so both run on every bar.
`unattended skill wiring` is listed for its REAL footing, corrected at rev-4: its guard is empty, so
it runs on every bar whatever this unit touches. rev-1 justified it by "the version-marker bump is
what pulls in `unattended skill wiring`", and rev-3 struck S7 — the Rollout now states that this unit
no longer touches a template marker at all and the Files-touched table dropped the two constant rows
and the five-template-marker row. That sentence was the single surviving statement in this document
asserting a marker move the unit does not make, sitting in the section whose job is to justify the
leg list, one section from the paragraph rev-3 rewrote to kill exactly that derivation. No new leg is
registered and no map claim moves, so `codebase-map coverage + freshness` is unaffected and is
deliberately not listed.

This unit adds no gate leg. It adds one `fail` branch to an existing leg, and that branch's failing
case is AC2 — staged, observed RED, unstaged, before the check lands.

## 8. Open questions

- **F1 — the route paths are keyed on BACKTICKS, and a reworded sentence would silence the check.**
  Option (a): match only backticked tokens, as specified. Option (b): also scan bare tokens matching
  the route shape, which would then match a prose mention of the path and any fenced example, giving
  the check false subjects to grade. **Recommendation: (a).** `TOOL-aHoistedPass-2`'s own acceptance
  greps the backticked paths, so the two agree by construction; the residual — a later reword that
  drops the backticks degrades check 31 to a skip visible only under `GOV_UNATTENDED_REPORT=1` — is
  real, is held by nothing, and is disclosed rather than closed.
- **F2 — one report line per unresolved path, or one line naming the set.** Option (a): per path,
  matching the `for <unit> in <file>` per-item grammar the file already uses at
  `tools/unattended/check-unattended.sh:1938`. Option (b): one line naming all of them, which is
  shorter but leaves a reader unable to tell which path was the subject.
  **Recommendation: (a)**, on the grounds that a skip whose subject is a set is the shape this build
  exists to remove.

RESOLVED (agent, 2026-09-05, delegated): **F1 — (a), backticked tokens only.** `TOOL-aHoistedPass-2`'s own acceptance greps the
backticked paths, so the two agree by construction. The residual is disclosed rather than closed: a
later reword that drops the backticks degrades check 31 to a skip visible only under
`GOV_UNATTENDED_REPORT=1`, and nothing holds that. **F2 — (a), one report line per unresolved path**,
matching the per-item grammar the file already uses; a skip whose subject is a set is the shape this
build exists to remove.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, written against `c4fcf5ad` with every cited line re-opened.
  Five corrections to DESIGN-rev8 §4.5e were made silently in the body and are recorded here.
  **C1 — the carrier-absent skip does NOT "inherit arm B's silence rule verbatim."** Read at
  `tools/unattended/check-unattended.sh:1586-1589`: arm B guards its loop on `[ -f … ]` and emits
  nothing, so inheriting it verbatim would produce silence, which is the opposite of an announced
  skip. Check 31 takes arm B's disposition and rejects its silence; §4 says so.
  **C2 — the design's proposed skip line omits the ` for <subject>` segment.** All seven `report`
  lines in the file carry one (`:1033`, `:1815`, `:1839`, `:1852`, `:1929`, `:1938`, `:1942`), as does
  the `observed` line at `:1983`. The spec's lines carry it.
  **C3 — the design's outcome table hardcodes `tools/workflows/`.** `TOOL_ROOT` renders empty at a
  root install (`tools/memory-tree/adopt-memory-tree.sh:36-37`), so a literal is wrong in an adopter
  tree in both directions. The directory is `dirname` of the path the section names.
  **C4 — "born skipping" is true of an adopter tree, not of this one.** Because this unit lands after
  `TOOL-aHoistedPass-2`, gov's own render will already carry the route paths, so check 31 grades on
  its first run here. The tree's state at `c4fcf5ad` — M6 at `memory/guides/BUILD-METHOD.md:161`–`:194`
  naming no route script, the only `workflows/` path being M8's at `:225` — is what makes the
  born-skipping branch reachable at all, and it is now stated as an adopter fact.
  **C5 — the arms cost was priced and is smaller than it looks.** `ARMS_FLOORS` in
  `.memory-tree.conf:203` sits at 101/100 against a measured 174 branches / 166 armed, and the
  comparison at `tools/memory-tree/check-arms.py:288-291` is one-sided upward, so one armed branch
  owes no floor edit — only the positive arm itself. The design named the obligation and not its size.
  **C6 — the section is read from the registry, not typed as `M6`.** The design specifies a slice
  from `^## M6` to the next `^## `. That hardcodes into check 31 a fact the directive registry owns,
  so re-pointing the handle would leave the check grading a section the directive no longer names.
  The section comes out of `$core`, which is where arm B gets it, and an unreadable `${core:-}` is
  branch S1 rather than a crash under `set -u`.
  Two facts the design stated were re-derived and CONFIRMED unchanged: the free check number is 31,
  with 23 claimed as a label by four `report` calls and three `printf` violation lines; and
  `tools/unattended/check-unattended.test.sh` is not a gate leg.
- rev-2 - 2026-09-05 - M3 fork sweep under the standing mandate: F1 and F2 marked RESOLVED at
  their recommendations. Premise re-derived at the run's BASE `e828f778`:
  `tools/unattended/check-unattended.sh` still carries no check 31, so the number this unit claims is
  still free 66 commits after the spec's base.
- rev-3 - 2026-09-05 - folded round-1 spec-audit finding 20, which is one member of a four-unit
  collision the round found: `DEPL-aHoistedPass-1`, `TOOL-aHoistedPass-2`, `TOOL-aHoistedPass-7` and
  this unit each scoped the SAME single `unattended` 1.17-to-1.18 move. Section 8's F1 sweep gave it
  to `DEPL-aHoistedPass-1` at `order 2`; at `order 6` the whole of S7 was spent. S7 is struck rather
  than deleted, so the record keeps that it was claimed. Two consequences beyond the strike, and the
  second is the reason the finding was rated high rather than medium. AC11 asserted the literal
  `1.18` and would have stayed green because a different unit moved the version - a criterion
  witnessing somebody else's work - so it is restated as a pure agreement assertion with no literal.
  And section 4's Rollout derived this unit's OWNER-TURN status transitively from owning the bump,
  through `SKILL.template.md`'s marker under ruling D1. With the bump gone that derivation is hollow
  and the classification is WRONG in the direction that matters: it said an unattended run may not
  land this unit without an owner. Re-derived from the carriers this unit actually edits -
  `check-unattended.sh` and its test file, neither on the veto-2 list - it is not an owner turn.
  Files-touched loses the two constant rows and the five template-marker row.

- rev-4 - 2026-09-05 - folded round-2 spec-audit finding M5, before any code. Section 7 justified
  `unattended skill wiring` by "the version-marker bump is what pulls in" it, and rev-3 had already
  struck S7 as SPENT - `DEPL-aHoistedPass-1`'s section 8 F1 took that single move at `order 2`, the
  Rollout states this unit no longer touches a template marker at all, and the Files-touched table
  lost the two constant rows and the five-template-marker row. rev-3's own entry enumerated the
  strike's consequences and missed this one, so the sentence was the last statement in the file
  asserting a marker move the unit does not make. The leg keeps its place and gains its real footing:
  its guard is empty, so it runs on every bar regardless. **The premise moved again after that fold:**
  `DEPL-aHoistedPass-1` rev-5 PARKED the `unattended` bump to the owner as an M3 veto-2 owner turn, so
  order 2 sets nothing either. This unit's assertion is unaffected - `check-kit-versions.sh` grades
  agreement rather than movement, and every carrier still agrees at `1.17`.

- rev-5 - 2026-09-05 - the BUILD pass, and every change here is a measurement this document
  contradicted rather than a preference. THREE corrections, none of them cosmetic.
  **(1) `--only 28` does not reach check 31 and never did.** rev-1's Placement paragraph called a
  `--only 28` skip announcement "the correct answer"; measured at `e828f778` that command exits 1 at
  `line 2932: MEMORY_ROOT: unbound variable`, because check 30 reads a variable the `only28` guard
  skips assigning. AC9's `--only 28` half is struck and replaced by the observation, `${core:-}` is
  kept for the reason it is actually worth keeping, S1 gains an arm that a default run can reach,
  and the check-30 defect is filed as `TOOL-aHoistedPass-37` rather than repaired inside this unit -
  the one-token repair swaps a crash for a silent skip of a corpus walk, which is this build's own
  subject and owes its own reasoning.
  **(2) AC13 asked for "no output" from a leg that is documented to print.** Check 7's EXCLUDED
  notices and check 23's dispatch-join notices are the two DEFAULT-channel exceptions the file's own
  header names, and this repo's corpus emits both today. A criterion no landing tree can satisfy is
  not a bar, it is a line nobody will read twice; it is restated as a before/after byte comparison of
  the leg's stdout, which is the claim this unit can actually make.
  **(3) S6's arm count disagreed with section 6.** Four staged arms cannot witness AC2, AC3, AC5,
  AC6 and AC7, the last of which needs two observations by its own wording. Six.
  **(4) AN AMEND, in this unit's own write set: the suite's derived build-method carrier had fallen
  behind check 16's body term.** `tools/unattended/check-unattended.test.sh:1416` builds a carrier
  DERIVED from the registry, with a comment saying it is derived precisely so it cannot fall behind
  the thing it must satisfy. `TOOL-aHoistedPass-2` then made "satisfy" mean more than a heading, and
  a carrier of bare headings reds the body term seventeen times - MEASURED, all seventeen - so
  check 17's green control failed on a check-16 message about waivers it has nothing to do with.
  Observed on shard 2/2 and attributed at HEAD `c0a6d5ae` with this unit's edits reverted: the
  checker there already carries the body term and the fixture builder is byte-identical to BASE, so
  the arm was red before this pass began. The derivation now emits each section's handles as well as
  its heading, and a second counted assertion holds it there. AC15 is the criterion. This is an M2
  AMEND rather than scope creep: the file is in this unit's declared write set, the repair is the
  fixture's own stated intent, and leaving it would mean claiming a green from a suite that is the
  compensating check for this whole kit under the 2026-08-23 ruling.
  Line citations that MOVED between `c4fcf5ad` and `e828f778` and are now re-derived in place: check
  30, `exit "$status"`, and both scope-block spans. The citations re-opened and CONFIRMED unchanged:
  `fail()` at `:93`, `report()` at `:591` behind `REPORT=` at `:590`, and 31 still the first free
  `fail` number.

- rev-6 - 2026-09-05 - the post-commit bug-class checklist over this unit's own diff selected
  `amendment-leaves-its-other-half-standing`, and it was right. Two counts of a derived population
  were left standing in prose that rev-5's amendments had already falsified: §3's "thirty numbered
  checks and 174 `fail` branches" (31 and 176 once this unit lands) and §4's "prints **174 branches,
  166 armed** ... today" (176 and 168, and already wrong by two BEFORE this unit, because
  `TOOL-aHoistedPass-2` added a branch in between). Both now point at the source that owns the
  figure instead of restating it, which is the rule §7 of the charter states and which this document
  broke twice in one section. A THIRD of the same class was found in the same sweep: S7 still said
  the version is "already `1.18` by the time it runs", which `DEPL-aHoistedPass-1` rev-5's park made
  false and rev-4 recorded without coming back for the sentence. It survived because AC11 had already
  been rewritten to depend on no number — the amendment landed on the criterion and not on the scope
  item that motivated it. No code changed.

## 10. Reuse audit

Probe run at `c4fcf5ad`:
`python tools/codebase-map/reuse_lookup.py "announce a named skip when a gate cannot reach the subject it grades"`
over a corpus the tool reported as 645 symbols, 188 inventory keys, 19 affordance seams and 20
dossiers. **The seam this unit extends is the existing leg `unattended kit gate`** — returned as an
inventory key under `gate-legs`, and claimed by the dossier `memory/map/features/unattended.md`. Its
carrier is `tools/unattended/check-unattended.sh`, and the announcement primitive already lives there:
`report()` at `:591` behind `REPORT=${GOV_UNATTENDED_REPORT:-0}` at `:590`, with the grammar fixed by
seven existing skip lines. No new seam is created and no new file is written. Two other candidates
were opened and rejected: the `skip` symbol at `tools/drift-audit/selftest.py` is a test-harness
helper with no relation to a gate verdict, and the `memory-tree-hygiene` shared-seams entry ranked on
the words `skip` and `when` in prose rather than on a reusable mechanism.

Recall terms used: passes-harnessed, announced skip, REPORT channel, check-unattended, fail branch,
arms meta-gate, unarmed-branches pin, directive registry, build-method carrier, adopter tree,
green-by-absence, install prefix, TOOL_ROOT, gate leg guard
