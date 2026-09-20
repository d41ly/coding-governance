# TOOL-aWokenSentinel-13 — the resume tick sources the root conf before its bound reads, so a declared bound is honoured and the NOTE names the file

**Status:** CLOSED · rev-4 · 2026-09-21 · node a · Tier-2 · base 12b3701d · streams tooling · order 13 · ratified 2026-09-20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-build-TOOL-aWokenSentinel-13-1-acceptance-ledger.md](../build/2026-09-20-build-TOOL-aWokenSentinel-13-1-acceptance-ledger.md) | journal | — |
| [2026-09-20-prompt-TOOL-aWokenSentinel-13-1-build-brief.md](../prompts/2026-09-20-prompt-TOOL-aWokenSentinel-13-1-build-brief.md) | journal | — |
| [2026-09-20-review-TOOL-aWokenSentinel-8-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-8-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-14 |

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H5 (round 1, raw ids 26 and 33): `read_bound_key` reads `${!_bk_name:-}` from
the CALLING shell and interpolates `$CONF` into its NOTE (`tools/unattended/unattended.sh:358` to
`:368`); the driver makes that work by `. "$CONF"` at `:341` before the calls. `TOOL-aWokenSentinel-5`
hoists the function into `lib-unattended.sh` and calls it from the tick, but sources each worktree's
`.unattended.conf` only in a subshell for `MEMORY_ROOT` and never says which conf is sourced into
the tick's own shell or that `CONF` is set — so as specced every tick takes 6 and 40, prints
`declares no RESUME_ATTEMPTS … Declare one in  to change it` with an empty path even where the
project declares the key, and spec 5 AC5's only NOTE arm is green for the wrong reason. This unit
states the read — the tick's two knobs are ROOT-scoped, sourced once from `$ROOT/.unattended.conf`
into the tick's shell with `CONF` set, before the two `read_bound_key` calls — and proves it with
arms under a declared key and a NOTE that names a non-empty path.

## 2. Scope (IN)

- **S1** — In `tools/unattended/resume-tick.sh`, directly after the root is resolved and before
  any `read_bound_key` call: `CONF="$ROOT/.unattended.conf"`; an absent file is `resume-tick:
  REFUSED — <root> carries no .unattended.conf, so the tick has no bounds to read`, exit 2; then
  `RESUME_ATTEMPTS=""; RESUME_TURNS=""` — the driver's own clear-before-source at
  `unattended.sh:339`, so an exported value never stands in for a declaration — then `. "$CONF"`
  into the tick's own shell, so `RESUME_ATTEMPTS` and `RESUME_TURNS` resolve exactly as
  `GATE_BOUND` does in the driver. The knobs are ROOT-scoped: one repo, one pair of bounds,
  whatever worktree a run lives in. Spec 5 §4 is folded at its rev-2 to this read and cites this
  unit; unit 5 builds it at its own pass, and this unit's diff is the proof. Observed by AC1, AC2
  and AC3.
- **S2** — `MEMORY_ROOT` stays per-worktree and stays a subshell read, as spec 5 §4 has it: a
  worktree's memory root is that tree's fact, and sourcing a second conf into the tick's shell
  would let a worktree's declaration overwrite the root's bounds mid-walk. Observed by AC4.
- **S3** — The arms, each named with the break it is observed RED against: `RESUME_ATTEMPTS="2"`
  declared in the fixture's conf with two post-move attempt lines seeded → `ATTEMPTS EXHAUSTED`
  and no NOTE, red against a tick copy with the `. "$CONF"` line removed; `RESUME_TURNS="7"`
  declared → the launcher carries `--max-turns 7`, red against the same copy; the conf declaring
  neither key → the NOTE, once per key, whose interpolated path is the fixture's conf and exists,
  red against the BLOCK copy — the conf block removed by `sed '/^CONF=/,/^\. "\$CONF"$/d'`, which
  takes `CONF=`, the refusal, the two clearing assignments and `. "$CONF"` with the `shellcheck`
  comment between them and KEEPS the two `read_bound_key` calls — where at this unit's order the
  tick runs under `set -u`, so the first NOTE's `$CONF` is an unbound variable: exit 1, zero
  NOTEs, no launcher, and the arm reads zero `Declare one in ` lines where it wants two that name
  a file; and `RESUME_ATTEMPTS=abc` exported into the
  tick's environment with the conf declaring `2` → the cap is 2 and no refusal, red against a tick
  copy with the two clearing
  assignments removed, where the tick exits 2 blaming the conf for a value it never declared.
  Observed by AC1, AC2, AC3 and AC5.
- **S4** — A NOTE naming no file is the signature of this defect and is greppable: one arm
  asserts the two `Declare one in ` lines on the tick's stderr are present and each is followed
  by a path that exists. The source-line-only copy cannot red it — `CONF` stays set there — so its
  break is the BLOCK copy of S3, where at this unit's order `read_bound_key` is entered with `CONF`
  unset under the tick's `set -u` and dies at the NOTE's `$CONF` — `CONF: unbound variable`, exit
  1, zero NOTEs — so the arm's two-existing-paths assertion reads zero lines; unit 18, one order
  later, re-reads the same copy as exit 2 with the guard's own sentence and zero NOTEs, the
  signature made a refusal rather than a shell error. Observed by AC2.

## 3. Non-goals (OUT)

- **No change to `read_bound_key`'s read.** Its calling-shell contract is the driver's and the
  hoist keeps its bytes; this unit satisfies the contract from the tick as the driver does. The
  guard that makes an unset `CONF` a refusal rather than a shell error is unit 18's, one order
  later; this unit's NOTE arm reds against the BLOCK copy before that guard exists, on `set -u`'s
  unbound-variable exit, and unit 18 changes what the same copy prints, not whether the arm can fail.
- **No conf comment sentence.** The one sentence in the conf comments saying the two keys are read
  from the ROOT conf by the tick is spec 5's, written in its §4 Data model; unit 6 finds it
  present and adds nothing, and this unit declares no edge for a sentence it does not write.
- **No per-worktree bounds.** A run in a worktree reads the root's `RESUME_ATTEMPTS`; a worktree
  conf that declares a different value is not read for these two keys, and the tick's header says
  so. The driver's own read is per-tree because the driver runs in one tree; the tick walks them
  all from one root and one pair of numbers is the only answer a scheduler can act on.
- **No `RESUME_STALE_BOUND` read.** That is `--liveness`'s number, read by the driver in the
  worktree it runs in, as spec 5 §4 states.
- **No hoist of the driver's conf-sourcing block.** It initialises thirty keys the tick does not
  read; the tick sources the file and reads two.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-5` — the tick, the hoisted `read_bound_key` in
  `lib-unattended.sh`, the fixture with its `mkconf`-shaped conf and the stub `claude`. Without the
  tick there is no read to fix.
- **consumes-from** external — the driver's own idiom at `tools/unattended/unattended.sh:339`
  to `:341`, the keys cleared and then `. "$CONF"` before the bound reads, which this read copies
  whole.
- **hands-off** `TOOL-aWokenSentinel-18` — the guard inside `read_bound_key` that refuses a
  caller with no `CONF` naming a file, and the two arms that observe it: a bare-shell call and
  the BLOCK copy of S3, spelled there with the same `sed` range and the same kept calls, read as
  exit 2 with zero NOTEs from that unit's order on.
- **hands-off** `TOOL-aWokenSentinel-24` — the suite helper that makes the BLOCK copy from its
  two anchor lines and asserts its shape, replacing this arm's inline `sed` and unit 18's with one
  name.

## 4. Design

### The read, in the tick

After `ROOT` is resolved (spec 5 §4 'The walk') and before the walk begins:

```
CONF="$ROOT/.unattended.conf"
[ -f "$CONF" ] || { echo "resume-tick: REFUSED — $ROOT carries no .unattended.conf, so the tick has no bounds to read" >&2; exit 2; }
RESUME_ATTEMPTS=""; RESUME_TURNS=""
# shellcheck disable=SC1090
. "$CONF"
read_bound_key RESUME_ATTEMPTS "$RESUME_ATTEMPTS_DEFAULT" attempts "…"
read_bound_key RESUME_TURNS "$RESUME_TURNS_DEFAULT" turns "…"
```

`read_bound_key` then reads `${!_bk_name:-}` from a shell that has sourced the file, prints its
NOTE with `$CONF` interpolated to a path that exists, and refuses a malformed value with exit 2
exactly as the driver does — the same function, the same contract, satisfied the same way. The
clearing line is the driver's at `unattended.sh:339`: `${!name}` reads the calling shell INCLUDING
its environment, so without it an exported `RESUME_ATTEMPTS` would stand in for a declaration the
conf never made, silently when well-formed and as a refusal blaming the conf when junk. A
scheduler's environment is exactly the one nobody audits. The
per-worktree `MEMORY_ROOT` subshell read in the walk is untouched: it reads one key from one
tree's conf and never sources into the tick's shell.

### Why root-scoped

The tick is one process walking every worktree of one repo from one `--repo` root. A per-worktree
bound would mean the same run could be capped at 6 in one tree and 2 in another, decided by which
tree's conf a branch happened to carry; and sourcing each worktree's conf into the tick's shell
would overwrite `RESUME_ATTEMPTS` mid-walk with whatever the previous tree declared. `.unattended.conf`
is a tracked file, so the root's copy is the merged answer, and it is the file an owner registering
the tick edits.

### The NOTE-path arm

The signature of the specced defect was `Declare one in  to change it` — two spaces, no file. One
arm greps the tick's stderr for `Declare one in ` and asserts what follows, up to ` to change it`,
is a path that exists, and that exactly two such lines print. It is the liveness assertion for the
read: a NOTE that names a file proves `CONF` was set before the call. Its break is the BLOCK copy,
not the source line alone: with the block gone `CONF` is unset, and at this unit's order the
function runs unguarded into the NOTE's `$CONF` under the tick's `set -u` — `CONF: unbound
variable` from the library line, exit 1, zero NOTEs, no launcher — so the arm reads zero lines
where it wants two and is red on the copy. Measured at this pass (probe over the fixture,
2026-09-21, node a): the rev-3 reading of two EMPTY-path NOTEs and a launched attempt 1 needs
`CONF` SET AND EMPTY, which nothing in the copy or the suite does; `set -u` at the tick's top
decides it. Unit 18's guard, one order later, makes the same copy exit 2 with its own sentence
before the function reaches `$CONF`, and the arm still reads zero lines — the signature made a
refusal rather than a shell error; spec 18 records that reading against the same copy. The
copy is made by `sed '/^CONF=/,/^\. "\$CONF"$/d'` over the tick: the range takes the four conf
lines and the `shellcheck` comment between them and leaves both `read_bound_key` calls, which is
what lets the function be entered at all. Unit 24 makes that range a suite helper both arms call.

### Inventory

No identifier is minted; `CONF` is the driver's own variable name, used by `read_bound_key`'s NOTE
and set here for the same reason.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/resume-tick.sh` | the conf block of §4 — four lines plus the `shellcheck` comment — and the two calls below it, if unit 5's pass did not already build spec 5's rev-2 read; the header sentence on root scope |
| `tools/unattended/resume-tick.test.sh` | five arms: the declared cap, the two NOTEs with a non-empty path, the declared turns, the two-worktree walk with a differing declaration, the exported junk value |

### Alternatives rejected

- **Source each worktree's conf in a subshell and print the two resolved values for the walk to
  consume.** Correct but per-worktree, which is the wrong scope for a scheduler's bounds, and it
  puts a `printf`-and-`read` protocol between the tick and a function that already sets globals.
- **Read the two keys with a bare `grep` over the conf.** A second reader with its own default,
  the class spec 5 §4 refuses for `RESUME_STALE_BOUND`.

## 5. Production-readiness checklist

- security — the tick sources a tracked conf from the repo it was registered for, the same file
  the driver sources on every verb; no new input.
- perf / scale — one `source` per tick.
- error / empty / loading states — no root conf refuses with exit 2 and the file named; no
  declaration takes the announced default; junk refuses with exit 2 through `read_bound_key`.
- observability — the NOTE names the file; the refusal names the root.
- risks — a worktree conf declaring a different bound is silently not read for these keys; the
  tick's header says so and the conf comment says so.
- testing — §6, three arms and the NOTE-path assertion.
- migration — N/A; both keys are optional and defaulted.
- user docs — the conf comment sentence, unit 6's; the tick's header.

## 6. Acceptance criteria

The fixture is spec 5 §6's scratch repo under a short `%TEMP%` path with its stub `claude`. The
staged breaks are named per criterion, because one copy cannot red them all: the SOURCE copy has
the `. "$CONF"` line removed; the BLOCK copy has the conf block removed by
`sed '/^CONF=/,/^\. "\$CONF"$/d'` — `CONF=`, the refusal, the two clearing assignments, the
`shellcheck` comment and `. "$CONF"` gone, both `read_bound_key` calls kept, so the copy still
enters the function; the CLEAR copy has the two clearing assignments removed; the WORKTREE copy
sources each worktree's conf into the tick's own shell during the walk.

- **AC1** — When the fixture's conf declares `RESUME_ATTEMPTS="2"` and the sidecar is pre-seeded
  with two attempt lines dated after the fixture commit, `bash resume-tick.sh --repo <fixture>`
  prints `ATTEMPTS EXHAUSTED` and no `declares no RESUME_ATTEMPTS` line; against the SOURCE copy
  it launches attempt 3 and prints the NOTE.
  Red when: a declared cap is ignored, which is every tick reading the kit default.
- **AC2** — When the fixture's conf declares neither key, the tick's stderr carries `declares no
  RESUME_ATTEMPTS` and `declares no RESUME_TURNS` exactly once each, and each `Declare one in ` on
  stderr is followed by a path that `test -f` accepts; with no `.unattended.conf` at the root the
  tick prints `REFUSED` naming the root and exits 2. Against the BLOCK copy, at this unit's order,
  the tick exits 1 with `CONF: unbound variable` on stderr from the library's NOTE line, zero
  `Declare one in ` lines and no launcher — the reading this arm records, red because the
  two-existing-paths count is zero; from unit 18's order on the same copy exits 2 with
  `read_bound_key was called with CONF unset`, zero `declares no` lines and no launcher, which
  spec 18 AC2 records. The SOURCE copy leaves `CONF` set and cannot red this arm, and §7 says so.
  Red when: the NOTE's path is empty or absent, which is the specced defect's own signature and
  is what unit 18 makes a refusal; or the count of NOTEs is not two, which is a read that never
  happened; or a root with no conf walks on defaults silently.
- **AC3** — When the fixture's conf declares `RESUME_TURNS="7"`, the launcher file the tick writes
  carries `--max-turns 7` and `stub.log` shows the stub invoked with it; against the SOURCE copy
  it carries `40`.
  Red when: the launcher carries `40` under a declared `7`.
- **AC4** — When one worktree of the fixture carries a conf declaring `MEMORY_ROOT=mem2` AND
  `RESUME_ATTEMPTS="6"`, a bound record under `mem2/builds/` with two post-move attempt lines
  seeded in that worktree's sidecar, and the root conf declares `RESUME_ATTEMPTS="2"`, the tick
  walks that tree's record under `mem2`, prints `ATTEMPTS EXHAUSTED` for it, and writes no
  launcher; against the WORKTREE copy it launches attempt 3, which is the worktree's `6` read in
  place of the root's `2`.
  Red when: the worktree's declaration is read, which is the second conf sourced into the tick's
  shell; or the two values are the same, which makes the observation unable to tell the scopes
  apart.
  fixture: `git worktree add` inside the scratch repo; the second conf and the two attempt lines
  written by the arm.
- **AC5** — When `RESUME_ATTEMPTS=abc` is exported into the tick's environment and the fixture's
  conf declares `RESUME_ATTEMPTS="2"` with two post-move attempt lines seeded, the tick prints
  `ATTEMPTS EXHAUSTED` and no `REFUSING`; with the conf declaring neither key the tick prints the
  `declares no RESUME_ATTEMPTS` NOTE and caps at the kit default; against the CLEAR copy the
  SECOND case exits 2 with `REFUSING - RESUME_ATTEMPTS is declared as 'abc'`, blaming the conf for
  a value it never declared — the first case cannot red there, because `. "$CONF"` overwrites the
  export with the declared `2` whether or not the keys were cleared.
  Red when: an exported value overrides the conf or the default, which is a bound nobody declared
  in the one file the owner edits.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the tick over the
fixtures of AC1 to AC4.

New arm: `tools/unattended/resume-tick.test.sh` · the declared cap and the declared turns, red against the SOURCE copy; the two NOTEs with a non-empty path, red against the BLOCK copy on `set -u`'s unbound-variable exit at this order and on unit 18's refusal after it; the two-worktree walk with a differing declaration, red against the WORKTREE copy; the exported junk value, red against the CLEAR copy · `FLOOR_ASSERTIONS` rises by the arms' executed assertions

## 8. Open questions

- **F1 — root-scoped bounds sourced once, or per-worktree bounds read in a subshell.** (a) Once
  from `$ROOT/.unattended.conf` into the tick's shell. (b) Per worktree, a subshell sourcing that
  tree's conf, setting `CONF`, running the two reads and printing the values for the walk.
  RESOLVED (agent, 2026-09-20, delegated): (a). The scheduler acts on one pair of numbers per
  repo; (b) makes the cap depend on which branch a worktree carries and needs a print-and-read
  protocol around a function that sets globals. Vetoes: no new surface, no governance carrier, no
  widened write; the run-state file names the mandate.

## 9. Revision log

- rev-4 · 2026-09-21 · S3 · S4 · §3 · §4 · AC2 · §7 · FACT-QUESTION resolved by the pass's probe
  (M3): the BLOCK copy's reading at this order was recorded as two empty-path NOTEs and a launched
  attempt 1, which needs `CONF` set and empty; the tick runs under `set -u`, so the copy dies at
  the library's NOTE line with `CONF: unbound variable`, exit 1, zero NOTEs, no launcher — probed
  over the fixture with the `sed` range as spelled, copy shape `read_bound_key` 2 · `CONF=` 0 ·
  source 0. The arm's break is unchanged and the arm is still red on it, on a count of zero rather
  than on `test -f`; every carrier of the old reading is corrected. Spec 18 S4 and spec 24 S2
  paraphrase the rev-3 reading and inherit this one at their own passes; their mechanisms and the
  two phrases spec 18 AC4 greps here are untouched. AC5, the same way: the CLEAR copy was said to
  red the DECLARED case, but sourcing the conf overwrites an export whether or not the keys were
  cleared, so the observed red is the neither-declared case — `REFUSING … 'abc'`, exit 2, no
  NOTE, no launch — and AC5 now says so. The tick needed no edit — unit 5's pass built the block
  and the header sentence as §4 spells them — so this unit's diff to it is empty and the arms are
  the proof.
- rev-3 · 2026-09-20 · S3 · S4 · §3 · §4 · AC2 · §7 · folded spec-audit round 3: sibling
  agreement for the promoted `TOOL-aWokenSentinel-24` (H4, raw 18) — the BLOCK copy was defined
  as "the whole conf block of §4" (seven lines, calls included), "WHOLE four-line" and "five
  lines" in three places, and only the calls-kept reading can enter the function, so S3, §4, the
  §6 preamble and Files-touched spell it once as the `sed` range from `CONF=` through `. "$CONF"`
  with both `read_bound_key` calls kept, the same spelling spec 18 rev-2 carries, and a
  `hands-off` names unit 24's helper; M7 (raw 19) — AC2 and §7 recorded the BLOCK copy's reading
  as unit 18's exit 2, which does not exist at this unit's order, so they now record the reading
  at this order (two empty-path NOTEs refused by `test -f`, attempt 1 launched) and name unit
  18's as the re-read; M9 (raw 20, 33) — the phrase spec 18 AC4 greps is now the shared `sed`
  spelling and the `red against the BLOCK copy` clause of §7, both present here.
- rev-2 · 2026-09-20 · S1 · S3 · S4 · §3 · §4 · AC1 · AC2 · AC3 · AC4 · AC5 · §7 · folded
  spec-audit round 2: sibling agreement for the promoted `TOOL-aWokenSentinel-18` (H4, raw 4) —
  the NOTE-path arm's break is the whole conf block removed, where unit 18's guard refuses, and §7
  names a break per arm because the source-line copy leaves `CONF` set; M2 (raw 22) — the
  `hands-off` on unit 6 named a sentence spec 5's Data model writes, so the bullet is dropped and
  a non-goal states the writer; M3 (raw 18, 23) — AC4's worktree conf declared no value and seeded
  no attempts, so it now declares `6` against the root's `2` with two attempt lines and reads
  `ATTEMPTS EXHAUSTED`; M7 (raw 39) — §4 dropped the driver's clear-before-source it cited, so the
  two clearing assignments join the block and AC5 exports junk to observe them. Order 11 → 13 for
  the insertions of units 20 and 16.
- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 1 as the
  promotion of H5 (raw ids 26, 33).

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "source the project conf before reading a bound key in
a sibling script"` returned no seam and `unscanned layers: .sh`. The seam, read at source, is the
driver's own conf block: the empty initialisation at `tools/unattended/unattended.sh:336` to
`:339`, `. "$CONF"` at `:341`, and the two `read_bound_key` calls at `:369` and `:370` that the
sourcing makes work — the tick copies the sourcing and the calls and nothing else. The recall
probe's hits were `TOOL-aHoistedPass-40` (the kit gate's allow-list as a fourth spelling of the key
set, which does not bind a script that sources the conf directly), this build's audit at the H5
paragraph, and `TOOL-aCollapsedScan-11`; none records a bound read from an unsourced shell before
this one.

Recall terms used: `read_bound_key CONF sourced calling shell NOTE declares no default announced lib-unattended hoist tick`
