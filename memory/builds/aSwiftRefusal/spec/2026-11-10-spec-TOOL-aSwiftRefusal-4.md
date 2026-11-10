# TOOL-aSwiftRefusal-4 — round 1's mediums and lows: one deferral answer for `--rescope` and check 23, the floors, the `--audit` arm, the positive control and the contract text

**Status:** CLOSED · rev-2 · 2026-11-10 · node a · Tier-2 · base 17308b6c · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-build-TOOL-aSwiftRefusal-1-agent-ledger.md](../build/2026-11-10-build-TOOL-aSwiftRefusal-1-agent-ledger.md) | journal | TOOL-aSwiftRefusal-1 TOOL-aSwiftRefusal-2 TOOL-aSwiftRefusal-3 |
| [2026-11-10-prompt-TOOL-aSwiftRefusal-4-1-spec-writer.md](../prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-4-1-spec-writer.md) | journal | — |
| [2026-11-10-prompt-TOOL-aSwiftRefusal-4-round1-fix-brief.md](../prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-4-round1-fix-brief.md) | research | — |
| [2026-11-10-prompt-TOOL-aSwiftRefusal-4-token-fix-brief.md](../prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-4-token-fix-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing review of units 1 to 3 (`reviews/2026-11-10-review-TOOL-aSwiftRefusal-1-3-closing-diff-round1.md`,
CLEAN WITH FIXES) confirmed four mediums and three lows, and build method M4 promotes them into one
batched unit. This unit makes `--rescope` and check 23 read a deferral through the one predicate
units 2 and 3 read, pins the arms units 1 and 2 added under their floors, arms the `--audit` half of
the deferral skip, gives the unit-1 ordering arm a positive control, and brings one comment and one
contract sentence in line with the code.

## 2. Scope (IN)

- **S1** — M1, the re-defer. `verb_rescope` in `tools/unattended/unattended.sh` answers "amendment
  already recorded, unchanged" to a `defer` act only when a row matching it exists AND
  `check_unit_deferred "$rel" "$unit" DEFERRED` answers 0, which is the predicate's row half: the
  unit's latest defer row follows every dispatch row naming it. A same-reason defer after a later
  dispatch row of the unit appends a new defer row through `park`, as any first defer does. Every
  other act keeps the existing match unchanged. Observed by AC1.
- **S2** — M4, the predicate's home. `check_unit_deferred` and its header comment move from
  `tools/unattended/unattended.sh` into `tools/unattended/lib-unattended.sh`, the kit library both
  the driver and `tools/unattended/check-unattended.sh` source. Its body, its signature and its two
  driver call sites (the order gate and `read_open_passes`) stay as they are, and the driver keeps
  a one-line pointer comment where the definition stood. Observed by AC2.
- **S3** — M4, check 23's release. In check 23's no-commit case, a unit that is released by the
  question `read_open_passes` asks, terminal or deferred, has its window's upper bound lowered from
  `dstop` to its release commit, so a sibling's write admitted after that commit is not charged to
  it. Check 23 asks `check_unit_deferred` for the deferred half and prints one report-channel line
  per released row. A unit whose release is not committed inside its window keeps the bound it has
  today. Observed by AC3.
- **S4** — M2 and L1, the floors and the positive control. The unit-1 ordering arm gains one `hit`
  of the spec-token refusal text on a dispatch that clears every cheap refusal. `FLOOR_SHARD_3`,
  `FLOOR_SHARD_4` and `FLOOR_ASSERTIONS` in `tools/unattended/unattended.test.sh`, and
  `FLOOR_SHARD_8` and `FLOOR_ASSERTIONS` in `tools/unattended/check-unattended.test.sh`, rise by the
  assertion lines units 1 and 2 left unpinned and every block this unit adds, each with a RAISED
  comment counted off the blocks' own lines. Observed by AC4.
- **S5** — L2, the hook's comment. The comment inside `check_commit_message` that explains why
  `--check-commit` asks `check_pass_open` alone gains a sentence saying the deferred skip is left
  out on purpose, and why. The verb's code does not change. Observed by AC5.
- **S6** — L3, the `--audit` contract. The `--audit` entry of `tools/unattended/VERBS.template.md`
  and its dogfood copy `memory/guides/UNATTENDED-VERBS.md` says a unit whose spec is deferred is
  left out too. The two files stay byte-equal past their marker line. Observed by AC6.
- **S7** — The suite blocks on the §7 `New arm:` lines: the M1 block and the M3 block in the driver
  suite's region four, the positive control in its region three, and the M4 block in the gate
  suite's region eight. NOT OBSERVED by a criterion here: each is suite code, and the main loop
  observes each red, then green, at the close. AC4 counts their assertion lines, and AC1 and AC3
  observe the code two of them re-observe.

## 3. Non-goals (OUT)

- Any change to units 1 to 3's behaviour beyond what an item names. The order gate,
  `read_open_passes`, the spec-token block's position and every refusal's text stay as they are.
- `pass_commit`, `check_pass_open` and `read_pass_declarations`, as the brief names them.
- `--check-commit`'s behaviour. L2 takes the review's first option, the comment, so the hook keeps
  printing `o` for a deferred unit's open pass and grades a `Pass:` trailer naming it.
- `spec_facts`, `load_spec_facts` and `drop_working_specs`. They stay in the driver, for the reason
  §4 "Alternatives rejected" gives.
- New `memory/gotchas/` classes. Each finding's left-shift is the arm or the floor this unit adds,
  which M8 accepts as the regression gate, so no class is filed here.
- The dOrderedCharter branch, and any new rescope act, run-state row or refusal.

### Edges

- **consumes-from** `TOOL-aSwiftRefusal-2` — `check_unit_deferred <run-state file> <unit> <spec status>` as that unit built it; this unit moves it and calls it, and changes no line of its body
- **consumes-from** `TOOL-aSwiftRefusal-3` — the deferred skip in `read_open_passes`, whose release question check 23 now asks and whose `--audit` half the M3 block arms
- **consumes-from** external — check 24's read of the build README's generated units region (`tools/unattended/check-unattended.sh:4254`) and the kit library's `id_rows`, both as they stand at base `17308b6c`

## 4. Design

### Evidence

Read at base `17308b6c`, the tip of units 1 to 3 and the sha the brief names for the red
observation. The default branch is still `ae6735c1`, which lacks the code these items correct, so
grounding against it would describe a tree this unit does not edit. `tools/` and
`memory/guides/` are byte-equal between `17308b6c` and this branch's tip `88e73498`.

- `verb_rescope`'s idempotence loop (`tools/unattended/unattended.sh:13997-14006`) builds `want` and
  returns "amendment already recorded, unchanged" when any earlier `rescope · item` row equals it,
  whatever its position among the unit's dispatch rows.
- Probed on 2026-11-10 at this base: a run-state fixture holding a dispatch row, a defer row with
  reason `set aside` and a second dispatch row for `ARCH-x-1`, driven through `verb_rescope` with
  its run and roster reads stubbed, printed "amendment already recorded, unchanged — defer ARCH-x-1"
  and wrote no row. `check_unit_deferred` over the same file answered 1. AC1 stages the same probe.
- `check_unit_deferred` is defined at `tools/unattended/unattended.sh:14166-14172`, with its header
  comment at `:14158-14165`. It reads only the run-state file and the status it is passed, and its
  callers are the order gate (`:14371`) and `read_open_passes` (`:14116`). No other file calls it.
- The driver sources the kit library at `tools/unattended/unattended.sh:98-103`, and the gate at
  `tools/unattended/check-unattended.sh:81-86`. Sourcing the library alone works: a shell that
  sources it and asks `type id_rows` succeeds.
- Check 23's loop (`tools/unattended/check-unattended.sh:4435`) sets each row's upper bound `dstop`
  to the unit's next anchor or HEAD (`:4503-4504`), looks for a pass commit (`:4505`), records the
  window (`:4509`), scans ABSORB commits, and in the no-commit case (`:4520`) prints the dodged-join
  line on stdout (`:4540`) when a declared path moved inside `dsgrp..dstop`. Nothing there reads a
  spec status or a defer row.
- The gate reads unit statuses in one place: check 24 reads the build README's generated units
  region with `region` (`:4254`) and asks a row's status with `id_rows` and a `| WONTDO |` match
  (`:4305-4309`).
- Check 30 selects its population by grepping the DRIVER for the two patterns `spec_facts` spells
  (`tools/unattended/check-unattended.sh:5872-5881`), so moving `spec_facts` out of the driver
  reds check 30.
- `git log -G` reads an extended regex. Probed on 2026-11-10 in a scratch repository: over three
  commits of one file, `-G 'A-1 .*\| DEFERRED \|'` named only the commit that flipped the row to
  DEFERRED, and the same pattern with bare `|` named all three.
- The unit-1 and unit-2 region-three arms (`tools/unattended/unattended.test.sh:7653-7707`) hold 10
  assertion lines, and neither commit moved `FLOOR_SHARD_3` (405, `:19378`). `FLOOR_ASSERTIONS`
  (3266, `:19172`) and `FLOOR_SHARD_4` (393, `:19382`) rose only for unit 3. The gate suite's
  `FLOOR_ASSERTIONS` is 1142 (`tools/unattended/check-unattended.test.sh:7346`) and its
  `FLOOR_SHARD_8` is 217 (`:7358`). Measured 2026-11-10 at this base.
- `--audit` reads `read_open_passes "$rel" current` (`tools/unattended/unattended.sh:8657`), and
  the terminal-unit `--audit` arm sits at `tools/unattended/unattended.test.sh:9281-9294`.

### The re-defer (S1)

```
want="rescope · item $act $unit${succ:+ -> $succ} · reason $reason"   # unchanged
while IFS= read -r pl; do
  [ "$pl" = "$want" ] || continue
  # A DEFER IS RECORDED ONLY WHILE IT IS IN FORCE: a dispatch row after the matching defer row
  # re-took the unit, so the same reason is a new deferral and is appended.
  [ "$act" = defer ] && ! check_unit_deferred "$rel" "$unit" DEFERRED && break
  echo "unattended: amendment already recorded, unchanged — $act $unit"
  return 0
done <<RESCOPED ...
```

Passing the literal `DEFERRED` satisfies the predicate's status half, so its answer is the row half
alone. The spec's status is not read here because `--rescope` records the amendment and the spec
flip is a separate edit, as the verbs contract says. `--rescope` and the order gate then agree on
whether the unit's rows defer it: the row half is decided by one awk, in one function.

### The predicate's home (S2)

`check_unit_deferred` moves whole, comment included, to `tools/unattended/lib-unattended.sh`,
beside `read_pass_declarations` and `pass_commit`, the other readers of the run-state rows both
files share. The driver keeps the pointer comment the file already uses for moved helpers
(`tools/unattended/unattended.sh:5069` is that shape). The body uses `awk` only, so it needs no
driver global.

### Check 23's release (S3)

Inserted after `dshit` is computed (`tools/unattended/check-unattended.sh:4505`) and before
`dsend` (`:4509`), so the window record, the ABSORB scan and the dodged-join scan all read the
lowered bound. The record's units region is read at most once per record, on the first row that
needs it, with the region call check 24 uses.

```
if [ -z "$dshit" ]; then
  <the record's units region, read once: region "$M/builds/$dsslug/README.md" '<!-- gen:build-units -->' '<!-- /gen:build-units -->'>
  dsst=<CLOSED, WONTDO or DEFERRED, whichever `| <status> |` the unit's `id_rows` row carries; else empty>
  dsrel=""
  case "$dsst" in
    CLOSED|WONTDO) dsrel=$(GIT log -1 --format=%H -G "$dsunit .*\\| $dsst \\|" "$dsgrp..$dstop" -- "$readme") ;;
    DEFERRED)
      if check_unit_deferred "$f" "$dsunit" "$dsst"; then
        r1=$(GIT log -1 --format=%H -G "$dsunit .*\\| DEFERRED \\|" "$dsgrp..$dstop" -- "$readme")
        r2=$(GIT log -1 --format=%H -S " rescope · item defer $dsunit · reason " "$dsgrp..$dstop" -- "$f")
        <both found: dsrel is the later of r1 and r2, by GIT merge-base --is-ancestor; either missing: empty>
      fi ;;
  esac
  if [ -n "$dsrel" ]; then
    report "check 23 released $dsunit in $f — its spec reads $dsst, so its window ends at its release ${dsrel:0:8} and no write after it is charged to it"
    dstop=$dsrel
  fi
fi
```

The question is `read_open_passes`' own, asked in its order: terminal first, then
`check_unit_deferred`. Its status comes from the generated units region rather than the spec
headers, because the region is the gate's one status source (check 24) and the index generator
renders it from those headers. The release commit is where the driver began answering
"released": for a terminal unit the latest commit in the window that touched the unit's region row
at that status, and for a deferred unit the later of that commit and the latest commit that added a
defer row naming the unit, because the driver releases a deferred unit only once both halves hold.
Every lookup is bounded by `dsgrp..dstop`, and a release found nowhere in it means none is
committed, so the bound stays `dstop`, which is today's behaviour and the strict direction.

A write inside `dsgrp..dsrel` still prints the dodged-join line for the released unit: the release
ends the window, it does not excuse what happened before it. The M4 block's third case pins that.

`tools/unattended/check-unattended.sh` carries raw CR bytes in its awk regexes, so the builder edits
it in binary mode, and every git read goes through the `GIT` wrapper, as check 28 requires of
this kit.

### The suite blocks and the floors (S4, S7)

Each block opens with a `# ---- TOOL-aSwiftRefusal-4 <item>:` header comment and ends at the first
blank line after it, so AC4 can count it. A `mutate` counts as an assertion in both suites.

| Block | Suite and place | Assertion lines |
|---|---|---|
| L1 | driver suite, region three, inside the unit-1 arm after its last `miss` | 1 |
| M1 | driver suite, region four, directly after the unit-3 arm on its fixture | 5 |
| M3 | driver suite, region four, directly after the terminal-unit `--audit` arm | 5 |
| M4 | gate suite, region eight, directly after the no-commit dodged-join arm (`tools/unattended/check-unattended.test.sh:4552-4556`) | 10 |

- **L1.** With the stub key declared and ARCH-tRun-4 already dispatched on `${PFX}swift.sh`,
  `run --dispatch tRun --pass ARCH-tRun-5 --writes ${PFX}swift5.sh` clears the order gate and
  condition 1 and reaches the stub, and the block `hit`s
  `--dispatch refuses: the declared spec-token checker reds over the live tree`. The unit-2 arm
  restores RUN.md from its copy on every case, so the refused dispatch leaves nothing behind.
- **M1.** On the unit-3 arm's state, where ARCH-tRun-1 was re-dispatched after its defer row,
  `run --rescope tRun --act defer --item ARCH-tRun-1 --reason "set aside"` is `hit` for
  `amendment recorded — defer ARCH-tRun-1` and `miss`ed for `already recorded`. A second identical
  call is `hit` for `amendment already recorded, unchanged — defer ARCH-tRun-1`. Then
  `run --dispatch tRun --pass ARCH-tRun-2 --writes work/held` is `hit` for `dispatch declared` and
  for `ARCH-tRun-1 left out as deferred`.
- **M3.** `build_audit_fixture`, dispatch ARCH-tRun-1 on `work/one.txt`, append
  `rescope · item defer ARCH-tRun-1 · reason set aside` in `park`'s grammar, `mutate` the spec to
  DEFERRED and commit. `run --audit tRun` prints the "no unit is dispatched and open" line once
  (`same`) and no `unattended-audit: ARCH-tRun-1` line (`miss`). `mutate` the spec to INPROGRESS,
  and `run --audit tRun` is `hit` for `unattended-audit: ARCH-tRun-1`.
- **M4.** Three cases, each from `reset_tree` with ARCH-tRun-1's row inserted into the fixture
  README's empty units region at INPROGRESS by a plain `sed`, which is not counted, and committed,
  then `drow ARCH-tRun-1 "work/one.txt"`.
  DEFERRED: append a defer row for ARCH-tRun-1, `mutate` the region row to DEFERRED and commit;
  `drow ARCH-tRun-2 "work/one.txt"`; write `work/one.txt` in a commit carrying
  `Pass: ARCH-tRun-2`; with the report channel on, `miss` `was dodged: ARCH-tRun-1` and `hit`
  `check 23 released ARCH-tRun-1 in`; then `mutate` the region row back to INPROGRESS and `hit`
  `was dodged: ARCH-tRun-1`. WONTDO: `mutate` the region row to WONTDO and commit, then the same
  sibling dispatch and write, `miss` `was dodged: ARCH-tRun-1` and `hit` `check 23 released
  ARCH-tRun-1 in`. Before the release: a commit naming no pass writes `work/one.txt`, then the
  region row is `mutate`d to WONTDO and committed, and `hit` `was dodged: ARCH-tRun-1`.

| Floor | File | Base | Rise | New |
|---|---|---|---|---|
| `FLOOR_SHARD_3` | driver suite | 405 | 10 (units 1 and 2) + 1 (L1) | 416 |
| `FLOOR_SHARD_4` | driver suite | 393 | 5 (M1) + 5 (M3) | 403 |
| `FLOOR_ASSERTIONS` | driver suite | 3266 | 21 | 3287 |
| `FLOOR_SHARD_8` | gate suite | 217 | 10 (M4) | 227 |
| `FLOOR_ASSERTIONS` | gate suite | 1142 | 10 | 1152 |

Each RAISED comment follows its file's own form. The driver suite's names this unit, the counts by
block, and says they were counted off the blocks' own lines and that the RED-first observation is
the close's. The gate suite's single comment above `FLOOR_ASSERTIONS` names the region and says
`FLOOR_SHARD_8` carries the same rise, as its siblings there do.

### The comment and the contract (S5, S6)

L2: inside `check_commit_message`, after the sentence ending "every pass commit would be refused as
having no open dispatched pass" (`tools/unattended/unattended.sh:14213-14217`), add: "It leaves out
the deferred skip too, on purpose: a `Pass:` trailer naming a deferred unit is still graded against
the declaration it carries, and a unit dispatched again after its defer row commits against the key
it re-took." The verb's code is not touched.

L3: in the `--audit` entry (`tools/unattended/VERBS.template.md:130-131`), "open and whose spec is
not terminal:" becomes "open and whose spec is neither terminal nor deferred (DEFERRED, with its
latest rescope defer row after every dispatch row naming it):". The same edit lands in
`memory/guides/UNATTENDED-VERBS.md`, and the builder rewraps the paragraph identically in both.

### Red-first, by item

M1 and M4 correct code, so their blocks are red against the kit at `17308b6c`. M3, L1 and the
unit-1 and unit-2 floor pin cover code that is already right, so no base can show them red: the
close stages a break for each, named on its `New arm:` line. This is the one place the brief's
"observed red at 17308b6c3" cannot hold as written, and the staged break is the observation the
build method's gate rule asks for instead.

### What it does not see

- **A floor protects only below its headroom.** The floors are `-ge` minimums. Pinning the unit-1
  and unit-2 lines makes their loss red only when the shard's executed count stands less than 10
  above `FLOOR_SHARD_3`. The close reads that margin off the shard's trailer line and records it
  beside the observation, whichever way it falls.
- **A status the region has not rendered.** Check 23 reads the generated units region, so a spec
  flipped in the working tree before the index is regenerated is not released yet. That keeps
  today's bound, the strict direction, and the bar's index-freshness leg closes the gap at commit.
- **A release made outside the window.** A row whose next anchor came before the release commit
  is already bounded by that anchor, and the lookup finds nothing inside `dsgrp..dstop`, so the
  row keeps its bound.
- **What the release does to a sibling's overlap.** The lowered bound is the window `ds_win`
  records too, so a sibling dispatched after a release no longer counts the released unit as an
  overlapping pass. That is the brief's "a released unit's window ends at its release".

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `check 23 released` | report-channel line, S3 | `tools/unattended/check-unattended.sh` |

No function is minted. `check_unit_deferred` keeps its name and is graded by the lexicon where it
now lives.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`

The kit version marker moves through the lander's `mint`, never by hand (the build README).

### Alternatives rejected

- **M1 by refusal**, keeping the idempotence and telling the operator a re-defer needs a new
  `--reason`. The review judged both options sound, and the brief picks the append. A refusal makes
  the operator invent a reason to state a fact the rows already show.
- **The finder's instance fix for M4**, a DEFERRED-only release in the dodged-join branch. The
  review judged it INSTANCE-ONLY: a WONTDO unit with no pass commit is released by the driver too
  and would still be charged.
- **`spec_facts` into the library, so check 23 reads spec headers as the driver does.** Check 30
  selects its population by grepping the driver for the patterns `spec_facts` spells
  (`tools/unattended/check-unattended.sh:5872-5881`), so the move reds check 30 unless that
  sentinel is repointed, which widens this unit into a check it has no finding against.
- **A spec-header read written inside check 23.** It would spell the status pattern a third time
  beside `spec_facts` and check 30, the copy the reuse rule refuses. Check 24's region read is the
  gate's existing status seam.
- **Releasing at the defer row alone for a deferred unit.** The driver releases only once the
  status half holds too, so a write between the defer row and a later status flip was never
  admitted to a sibling, and charging it to the unit is right.

## 5. Production-readiness checklist

- security — no new write path. `--rescope` appends a row it already appends on a first defer,
  through `park`'s field refusals. Check 23 grades less only for a released unit after its release.
- perf / scale — check 23 reads the units region once per record, and only when a row has no pass
  commit. Each released row costs at most three bounded `git log` reads and one ancestry test.
- error / empty / loading states — an unreadable region, a missing row or a release not committed
  in the window leaves `dstop` as it is today. An unreadable run-state file makes
  `check_unit_deferred` answer 1, so the unit stays unreleased.
- observability — one report-channel line per released row (S3). `--rescope` prints the existing
  "amendment recorded" line when it appends.
- risks — a release lookup that matched too early would excuse a dodged join. The M4 block's third
  case pins that a pre-release write is still charged.
- testing — AC1 to AC6, and the four blocks on the §7 `New arm:` lines.
- migration — none. No row format changes. A run already holding a re-defer that wrote no row
  needs one more `--rescope --act defer`, which now appends.
- user docs — the verbs contract and its dogfood copy (S6). No page under `help/` covers the
  unattended verbs.

## 6. Acceptance criteria

The criteria run from the repository root of the pass's worktree. `S` is the pass's scratch
directory, spelled absolute. `D=.` is AFTER, the kit this pass built, and `D=$B` is BEFORE, the kit
at `17308b6c` extracted to a short path outside the worktree, because the driver sources its
library beside itself. The `rescope` probe was run BEFORE on 2026-11-10 and printed "amendment
already recorded, unchanged — defer ARCH-x-1" with three rows left in the file.

```
B="$TEMP/sr4b"; mkdir -p "$B"; git archive 17308b6c tools/unattended tools/lib | tar -x -C "$B"
export F="$S/run-rescope.md"
seed() { printf '%s\n' '2026-11-10T00:00:01Z dispatch · item deadbeef ARCH-x-1 · reason work/a' \
  '2026-11-10T00:00:02Z rescope · item defer ARCH-x-1 · reason set aside' \
  '2026-11-10T00:00:03Z dispatch · item deadbee2 ARCH-x-1 · reason work/b' > "$F"; }
rescope() { # one defer of ARCH-x-1 through verb_rescope, its run and roster reads stubbed (reads D, F)
  bash -c 'source "$0/tools/unattended/unattended.sh" >/dev/null 2>&1; BYPASS_BAN=""
    check_slug() { :; }; check_run_state() { :; }; refuse_if_terminal() { :; }; stage_or_fail() { :; }
    unit_ids_of() { echo ARCH-x-1; }; runmd_of() { _runmd=$F; }
    verb_rescope tX defer ARCH-x-1 "" "set aside" 2>&1' "$D"; }
lib() { # status -> the library's answer for ARCH-x-1 over F (reads D)
  bash -c '. "$0/tools/unattended/lib-unattended.sh"; check_unit_deferred "$F" ARCH-x-1 "$1"; echo "rc=$?"' "$D" "$1"; }
```

- **AC1** — When `seed` runs and then `rescope` runs with AFTER, it prints
  `unattended: amendment recorded — defer ARCH-x-1` and `grep -c 'rescope · item defer ARCH-x-1 · reason set aside' "$F"`
  prints `2`. A second `rescope` prints `amendment already recorded, unchanged — defer ARCH-x-1`
  and the count stays `2`. With BEFORE the first `rescope` prints
  `amendment already recorded, unchanged` and the count stays `1`.
  Red when: a same-reason defer after a re-dispatch writes no row, or a defer in force is appended
  again on every call.
- **AC2** — When `grep -c '^check_unit_deferred()' tools/unattended/lib-unattended.sh tools/unattended/unattended.sh`
  runs, it prints `1` for the library and `0` for the driver. After `seed`, `lib DEFERRED` with
  AFTER prints `rc=1`; once `printf '%s\n' '2026-11-10T00:00:04Z rescope · item defer ARCH-x-1 · reason r' >> "$F"`
  has run, `lib DEFERRED` prints `rc=0` and `lib INPROGRESS` prints `rc=1`. With BEFORE `lib`
  prints `rc=127`. `bash -c 'source tools/unattended/unattended.sh >/dev/null 2>&1; type check_unit_deferred'`
  exits 0, so the driver's two callers still reach it.
  Red when: the predicate is defined twice, or not in the library both scripts source, or its
  answer moved.
- **AC3** — When `grep -c 'check_unit_deferred "\$f" "\$dsunit"' tools/unattended/check-unattended.sh`
  runs, it prints `1`, and `grep -c 'check 23 released ' tools/unattended/check-unattended.sh`
  prints `1`. Both print `0` against `17308b6c`.
  Red when: check 23 answers the release question with a reading of its own, or never asks it.
  permission: the end-to-end observation runs the gate over a fixture, which a pass may not do; the
  M4 block on the §7 `New arm:` line re-observes it, red against `17308b6c` and green after.
- **AC4** — When `grep -E '^FLOOR_(SHARD_3|SHARD_4|ASSERTIONS)=[0-9]+$' tools/unattended/unattended.test.sh`
  runs, it prints `FLOOR_ASSERTIONS=3287`, `FLOOR_SHARD_3=416` and `FLOOR_SHARD_4=403`, and
  `grep -E '^FLOOR_(SHARD_8|ASSERTIONS)=' tools/unattended/check-unattended.test.sh` prints
  `FLOOR_ASSERTIONS=1152` and `FLOOR_SHARD_8=227`. `grep -c 'RAISED .*TOOL-aSwiftRefusal-4' tools/unattended/unattended.test.sh`
  prints `3`, and `grep -c 'RAISED .*TOOL-aSwiftRefusal-4' tools/unattended/check-unattended.test.sh` prints `1`.
  `sed -n '/TOOL-aSwiftRefusal-1 - THE SPEC-TOKEN CHECKER/,/end REGION 3/p' tools/unattended/unattended.test.sh | grep -cE '^(hit|miss|same|mutate) '`
  prints `11` (`10` at base), and for each of `M1`, `M3` and `M4`,
  `sed -n '/^# ---- TOOL-aSwiftRefusal-4 M1:/,/^$/p' <its suite> | grep -cE '^(hit|miss|same|mutate) '`
  prints `5`, `5` and `10`.
  Red when: an arm group's assertion lines are not counted into its region's floor, or a floor
  moves by a figure its blocks do not carry.
  figure: the base values are PINNED, measured at `17308b6c` on 2026-11-10. A builder whose tree
  carries other floor moves derives each new value as the value then current plus the same rise.
- **AC5** — When `sed -n '/^check_commit_message()/,/^  head=\$(GIT rev-parse/p' tools/unattended/unattended.sh | grep -c 'deferred'`
  runs, it prints at least `1` (`0` at base), and
  `bash -c 'source tools/unattended/unattended.sh >/dev/null 2>&1; type check_commit_message' | grep -c check_unit_deferred`
  prints `0`.
  Red when: the comment still claims full parity with `--dispatch` and `--audit`, or the hook
  starts asking the predicate the comment says it leaves out.
- **AC6** — When `grep -c "whose spec is neither terminal nor deferred" tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md`
  runs, it prints `1` for each file (`0` at base), and
  `diff <(tail -n +2 tools/unattended/VERBS.template.md ) <(tail -n +2 memory/guides/UNATTENDED-VERBS.md )`
  exits 0.
  Red when: the `--audit` contract still names only terminal units, or the dogfood copy drifts.

## 7. Gates

The close runs these legs once, after the last unit of the build is terminal, and observes each new
arm below red on its staged break and green once restored. No pass runs a leg or a suite.

`unattended kit gate` · `unattended skill wiring` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `pass-order history` · `routed commits name a specced unit` · `brief-recorded` · `routed-commits selftest` · `tier2-review self-test` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 · the M1 block in region four, red against the driver at 17308b6c, whose same-reason re-defer prints "already recorded" and writes no row, so the sibling stays refused · FLOOR_ASSERTIONS and FLOOR_SHARD_4, +5
New arm: tools/unattended/unattended.test.sh · covers none · the M3 block in region four, red once the close takes the `check_unit_deferred` skip out of `read_open_passes`, so `--audit` lists the deferred unit · FLOOR_ASSERTIONS and FLOOR_SHARD_4, +5
New arm: tools/unattended/unattended.test.sh · covers none · the L1 positive control in region three, red once the close blanks `SPEC_TOKENS_CLI` for its one dispatch, so the stub is never reached; the same close cuts the unit-1 and unit-2 arms' 10 lines and reads shard 3's margin over its floor · FLOOR_ASSERTIONS and FLOOR_SHARD_3, +11
New arm: tools/unattended/check-unattended.test.sh · covers AC3 · the M4 block in region eight, red against the gate at 17308b6c, which charges the sibling's admitted write to the released unit in both the DEFERRED and the WONTDO case · FLOOR_ASSERTIONS and FLOOR_SHARD_8, +10

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft from
  `memory/builds/aSwiftRefusal/prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-4-round1-fix-brief.md`
  and the review record `2026-11-10-review-TOOL-aSwiftRefusal-1-3-closing-diff-round1`, items M1
  to M4 and L1 to L3, grounded at base `17308b6c`.
- rev-2 · 2026-11-10 · the spec-token `[bar]` hit in §6 folded, from
  `memory/builds/aSwiftRefusal/prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-4-token-fix-brief.md`:
  AC4's bare backticked gate-suite path becomes the `grep -c` over that file it already meant, so
  the token opens with grep and names no suite run. The suite stays named on the §7 `New arm:`
  line only. No scope, design, criterion or fork changed.

## 10. Reuse audit

Every seam is an existing one. `check_unit_deferred` (`TOOL-aSwiftRefusal-2`) is the one deferral
predicate, now asked by `verb_rescope` and check 23 as well, and it moves into
`tools/unattended/lib-unattended.sh`, the library that already carries the run-state readers both
scripts share (`read_pass_declarations`, `pass_commit`). Check 23's status comes from check 24's
read of the generated units region (`tools/unattended/check-unattended.sh:4254`) through `id_rows`,
and its release follows the order of `read_open_passes`' terminal skip. The probe
`python tools/codebase-map/reuse_lookup.py "a history check ends a released unit's commit window at its release"`
ranked name stems only (`check`, `units`, `build_commit`, `baseline_units`, `check_gen_region_only`),
and none of them decides a release or bounds a window, so beyond the seams above no existing seam
fits. The recall probe returned `TOOL-aWindowedPass-1`, which set check 23's window shape this unit
bounds, `TOOL-aRoutedQuill-13`, which unit 2 closed, and an aUnblockedFleet run record of check 23
charging a dodged join for a file another build wrote, the same class from a different cause.

Recall terms used:
`python tools/memory-recall/query.py "a deferred or retired unit's window charged with a sibling's admitted write by the dodged-join check" --terms "check 23 dodged join window release deferred WONTDO sibling admitted rescope idempotence floor"`
