# TOOL-aHoistedPass-9 — the adopter without the harness is told, on every bar

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-aHoistedPass-1-design-pass.md](../build/2026-09-04-build-aHoistedPass-1-design-pass.md) | research | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 DEPL-aHoistedPass-1 |

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
- **S6.** Four staged-break arms plus one green control in `tools/unattended/check-unattended.test.sh`,
  of which one is the positive assertion `fail 31` owes under the arms meta-gate.
- **S7.** The `unattended` kit version bump 1.17 → 1.18 the payload change owes: three engine
  constants and the marker in all five tracked `tools/unattended/*.template.md`.

## 3. Non-goals (OUT)

- **Not a whole-leg skip.** The leg carries thirty numbered checks and 174 `fail` branches, and not
  one of the other twenty-nine needs the route to exist. A whole-leg skip would discard twenty-nine
  verdicts to announce one, which is the green-by-absence class one level up.
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

Check 31 goes after check 30 (`:2885`–`:2903`) and before `exit "$status"` at `:2905`. That is
outside both scope guards: the `only28` block is `:110`–`:2305` and the `skip28` block is
`:2307`–`:2873`. Consequences, both deliberate:

- Check 31 runs under `--only 28` and `--skip 28` alike, exactly as check 30 does. Its cost is one
  `awk` over one file plus two filesystem tests, against a leg whose declared ceiling in
  `tools/gate-legs.json` is 16040.
- `$core` is built INSIDE the `only28` block, so under `--only 28` it is unset and `set -u` would
  kill the script. The check reads `${core:-}` and treats an empty value as branch S1 — which means a
  `--only 28` run announces a skip rather than passing silently, which is the correct answer.

### The arms meta-gate, priced

`tools/unattended/check-unattended.sh:93` defines `fail() {`, which puts it in the discovered
population of `tools/memory-tree/check-arms.py` (`:9-12`: a tracked `*.sh` that DEFINES the helper,
tested by the sibling `<stem>.test.sh`). So `fail 31` owes either a POSITIVE assertion in
`tools/unattended/check-unattended.test.sh` naming its own failure text, or a row in the shrink-only
`memory/project/unarmed-branches.txt`. This spec takes the arm; a pin row would be dishonest, because
the branch is reachable by deleting one file in a fixture.

**What it does NOT owe, measured rather than assumed.** `.memory-tree.conf:203` declares
`ARMS_FLOORS="… tools/unattended/check-unattended.sh:101:100 …"`, and
`python tools/memory-tree/check-arms.py --report` prints **174 branches, 166 armed** for that gate
today. The floor comparison at `tools/memory-tree/check-arms.py:288-291` is `got < want`, one-sided
upward, so adding one armed branch cannot breach it and **no `ARMS_FLOORS` edit is owed.** Raising the
floor to track reality is a separate act with its own reasoning and is not smuggled into this unit.

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

Lands as one commit after `TOOL-aHoistedPass-2`. It is a read-only check on a read-only leg; the
rollback is deleting the block. The kit version bump 1.17 → 1.18 rides the same commit and, under
ruling D1, makes this an owner turn transitively, because `tools/check-kit-versions.sh:164-192`
requires the marker in every tracked `tools/unattended/*.template.md` and `SKILL.template.md` is one
of the five.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/check-unattended.sh` | the check-31 block after `:2903`; `KIT_UNATTENDED_VERSION` at `:40` |
| `tools/unattended/check-unattended.test.sh` | four staged arms plus a green control |
| `tools/unattended/unattended.sh` | `KIT_UNATTENDED_VERSION` at `:42` |
| `tools/unattended/check-pass-order.sh` | `KIT_UNATTENDED_VERSION` at `:29` |
| five tracked `tools/unattended/*.template.md` | the `gov:kit unattended@` marker |

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
- **testing + left-shift gates** — four staged arms and a green control, of which one is the positive
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
- **AC9** — When `bash tools/unattended/check-unattended.sh --only 28` and the same command with
  `--skip 28` are both run on the intact tree, both exit 0, and under
  `GOV_UNATTENDED_REPORT=1` the `--only 28` run prints check 31's registry-unreadable skip rather than
  nothing.
- **AC10** — When `bash tools/unattended/check-unattended.test.sh` is run to completion, sharded as
  `--shard 1/2` and `--shard 2/2`, it reports PASS with a raised assertion count and no existing
  `GOV_UNATTENDED_REPORT=1` arm flips on the new line.
- **AC11** — When `bash tools/check-kit-versions.sh` runs after the bump, it exits 0 with
  `KIT_UNATTENDED_VERSION=1.18` in the three engine constants and the matching marker in all five
  tracked `tools/unattended/*.template.md`.
- **AC12** — When `bash tools/check-install-prefix.sh` runs, it exits 0 and
  `tools/install-prefix-carried.txt` still records 3 for this checker, because the block spells no
  install-prefixed literal.
- **AC13** — When `bash tools/unattended/check-unattended.sh` runs on the landed tree with the route
  present, it exits 0 with no output — the leg this unit changes is green on its own subject.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `unattended skill wiring` · `install-prefix (shipped surface)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The first two are the ones that bind: `unattended kit gate` is the leg being changed, and both it and
the arms gate are chunk `declarations`, subject `repo`, with no guard, so both run on every bar. The
version-marker bump is what pulls in `unattended skill wiring`. No new leg is registered and no map
claim moves, so `codebase-map coverage + freshness` is unaffected and is deliberately not listed.

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
