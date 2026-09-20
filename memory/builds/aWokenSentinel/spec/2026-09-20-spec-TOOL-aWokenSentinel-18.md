# TOOL-aWokenSentinel-18 — `read_bound_key` refuses a caller that named no conf: a bound read from a shell with `CONF` unset exits 2 instead of taking a default with an empty NOTE

**Status:** SPECCED · rev-2 · 2026-09-20 · node a · Tier-2 · base 12513c25 · streams tooling · order 14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-prompt-TOOL-aWokenSentinel-18-1-build-brief.md](../prompts/2026-09-20-prompt-TOOL-aWokenSentinel-18-1-build-brief.md) | journal | — |
| [2026-09-20-review-TOOL-aWokenSentinel-15-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-15-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 |

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H4 (round 2, raw id 4): `TOOL-aWokenSentinel-13`'s NOTE-path arm — every
`Declare one in ` on the tick's stderr is followed by a path that exists — was to be observed red
against a tick copy with only the `. "$CONF"` line removed, and that copy leaves `CONF` assigned and
the `[ -f "$CONF" ]` refusal in place, so both NOTEs still name an existing file and the arm can only
be seen passing. The defect's own signature, `Declare one in  to change it` with an empty path, is
what the named break never produces. This unit makes the signature impossible rather than merely
observed: `read_bound_key`, hoisted into `tools/unattended/lib-unattended.sh` by unit 5, refuses
with exit 2 when the calling shell has no `CONF` naming an existing file. A bound read from a shell
that sourced no conf is then a refusal that names the contract, never a kit default announced with
nowhere to change it; the driver, which sets `CONF` at `tools/unattended/unattended.sh:323` before
every call, is untouched in behaviour. Spec 13's NOTE arm already reds against the BLOCK copy at
its own order — with the block gone the NOTE names no file and `test -f` refuses — so what this
unit adds is not a break but a stronger reading of the same copy: exit 2 and zero NOTEs, the
signature made impossible rather than merely observed. The BLOCK copy is one thing, spelled the
same way here and in spec 13 rev-3: the four lines `CONF=`, the `[ -f "$CONF" ]` refusal, the two
clearing assignments and `. "$CONF"`, removed by `sed '/^CONF=/,/^\. "\$CONF"$/d'`, the
`shellcheck` comment going with them uncounted and the two `read_bound_key` calls KEPT;
`TOOL-aWokenSentinel-24` makes that spelling a suite helper both arms call.

## 2. Scope (IN)

- **S1** — `read_bound_key` in `tools/unattended/lib-unattended.sh` opens with one guard:
  `[ -n "${CONF:-}" ] && [ -f "$CONF" ]`, else it writes `unattended: REFUSING - read_bound_key was
  called with CONF unset or naming no file, so its NOTE could name nowhere to declare the key and a
  default would be taken from nowhere; set CONF to the sourced conf before the call` to stderr and
  exits 2 — the same channel and code its malformed-value refusal already uses. The function's
  header comment states the contract in a sentence carrying `sourced the conf into THIS shell`:
  the caller sources the conf into this shell and names it in `CONF`. Observed by AC1, AC2 and
  AC3, which pins the header phrase.
- **S2** — The driver's two calls at `unattended.sh:369` and `:370`, made after `CONF` is set at
  `:323` and sourced at `:341`, are unchanged and still read their declared values, defaults and
  NOTEs exactly as before; the guard never fires on the driver's path. Observed by AC3.
- **S3** — Two arms in the tick's suite: sourcing the lib into a bare shell and calling
  `read_bound_key` with `CONF` unset, and again with `CONF=/nonexistent/path` exported, exits 2
  with the sentence both times; and a tick copy with the conf block removed — the four lines
  `CONF=` through `. "$CONF"` by `sed '/^CONF=/,/^\. "\$CONF"$/d'`, the two `read_bound_key` calls
  kept — exits 2 with the same sentence and writes no NOTE and no launcher. Each is observed RED
  first against the STAGED BREAK: the lib as it stands at the start of this unit's pass, the tip
  of order 13, which already holds `read_bound_key` hoisted by unit 5 and no guard — not the lib at
  `12513c25`, which holds no `read_bound_key` at all and would answer `command not found`. Against
  that break the bare-shell call prints a NOTE with an empty path and exits 0, the nonexistent
  path prints a NOTE naming it, and the copy walks on defaults with two empty-path NOTEs. Observed
  by AC1 and AC2.
- **S4** — Spec 13 rev-3 names, per arm, the break it is observed red against, and states the
  BLOCK copy's reading AT ITS OWN ORDER, one before this unit: two `Declare one in ` lines with an
  empty path, exit 0, attempt 1 launched — red because `test -f` refuses the empty path — and
  that this unit re-reads the same copy as exit 2 with zero NOTEs and no launcher. Spec 13 and
  this spec spell the copy with the same `sed` range and the same kept calls. Observed by AC4.

## 3. Non-goals (OUT)

- **No change to what a declared or defaulted value resolves to.** The guard precedes the read and
  changes nothing about a caller that set `CONF`.
- **No environment guard inside the function.** `${!name}` cannot tell an exported value from a
  sourced one; clearing the keys before sourcing stays the caller's line, as the driver has it at
  `unattended.sh:339` and spec 13's §4 has it at its rev-2.
- **No `fail` branch.** The function runs before `fail()` exists in the driver and refuses with
  exit 2, as its existing refusal does; the new sentence joins that shape.
- **No change to the tick's own refusal on a missing conf.** Unit 13's `REFUSED — <root> carries
  no .unattended.conf` fires first on the ordinary path; this guard is what fires when that line
  and its siblings are gone.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-5` — `read_bound_key` hoisted verbatim into
  `lib-unattended.sh` and sourced by the tick; without the hoist the guard would have to land in
  the driver's copy and the tick's separately.
- **consumes-from** `TOOL-aWokenSentinel-13` — the tick's conf block: `CONF=`, the `[ -f ]`
  refusal, the two clearing assignments and `. "$CONF"`, with the `shellcheck` comment between
  them; its removal by the `sed` range above, the two `read_bound_key` calls staying, is the
  staged break this unit's second arm reads, and it is the same copy spec 13's NOTE arm stages.
- **hands-off** `TOOL-aWokenSentinel-24` — the suite helper that makes the BLOCK copy from the two
  anchor lines and asserts its shape, so this arm and spec 13's call one name and neither carries
  an inline `sed` after that unit lands.
- **hands-off** external — nothing.

## 4. Design

### The guard, first line of the function

```
read_bound_key() { # NAME · DEFAULT · UNIT · NOTE — the caller sourced the conf into THIS shell and named it in CONF
  [ -n "${CONF:-}" ] && [ -f "$CONF" ] || {
    echo "unattended: REFUSING - read_bound_key was called with CONF unset or naming no file, so its NOTE could name nowhere to declare the key and a default would be taken from nowhere; set CONF to the sourced conf before the call" >&2
    exit 2; }
  local _bk_name="$1" ...
```

The NOTE interpolates `$CONF`; the guard is the assertion that the interpolation names a file. It is
a liveness assertion on the caller, in the function every caller shares, so the next script that
sources the lib and calls the function from an unsourced shell refuses on its first run instead of
taking `6` and `40` silently.

### Why exit 2 and not a NOTE

A NOTE says "declared nothing, took the default, declare one here"; from a shell with no conf named
the third clause is false and the second is the defect. The driver's malformed-value branch already
treats a value nobody could have set as a refusal, and an unset `CONF` is the same fact one level
up.

### Inventory

No identifier is minted; the guard is two lines inside a function unit 5 moves.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/lib-unattended.sh` | the guard and the header sentence on `read_bound_key` |
| `tools/unattended/resume-tick.test.sh` | two arms: the bare-shell call with `CONF` unset and with `CONF=/nonexistent/path`, and the tick copy made by the `sed` range of S3 with both calls kept |

### Alternatives rejected

- **Name a different staged break in spec 13 and leave the function as it is.** The audit's own
  fix. It makes one arm honest and leaves the function able to announce a default from nowhere for
  every future caller; the signature stays possible.
- **Default `CONF` inside the function to `$ROOT/.unattended.conf`.** A second derivation of the
  conf path in a sourced file, and it would source nothing — the value read would still be the
  environment's.

## 5. Production-readiness checklist

- security — N/A; a guard on a function that reads a sourced conf.
- perf / scale — two tests per call, four calls per process.
- error / empty / loading states — `CONF` unset, empty, or naming a missing file each refuse with
  one sentence, and AC1 observes the unset and the missing-file states separately because they
  are two conjuncts of one guard; a set `CONF` naming a file behaves as before.
- observability — the refusal names the contract and the remedy.
- risks — a third caller that sets `CONF` to a path it never sourced passes the guard and reads
  the environment; the header says the caller sources the file, and no such caller exists.
- testing — §6; two arms in the tick's suite, seconds each.
- migration — N/A; both existing callers set `CONF` before the call.
- user docs — none; the function's header.

## 6. Acceptance criteria

The fixture is spec 5 §6's scratch repo under a short `%TEMP%` path with its stub `claude` and
unit 13's conf block in the tick. The staged break for AC1 and AC2 is the lib at the start of this
unit's pass — the tip of order 13, after units 5 and 13 landed — which holds `read_bound_key` and
no guard; `12513c25` is the sha this design was grounded against and holds no `read_bound_key` in
the lib, so no reading below is taken there.

- **AC1** — When a bare `bash` sources `tools/unattended/lib-unattended.sh` with `CONF` unset and
  runs `read_bound_key RESUME_ATTEMPTS 6 attempts "n"`, it exits 2 and stderr carries
  `read_bound_key was called with CONF unset`; with `CONF=/nonexistent/path` exported into the same
  shell the same call exits 2 with the same sentence; against the staged break the unset call
  exits 0 and stderr carries `Declare one in  to change it`, the empty path, and the nonexistent
  path exits 0 with a NOTE naming `/nonexistent/path`.
  Red when: the empty-path NOTE is still producible, which is the specced defect's own signature;
  or a NOTE names a file that does not exist, which is the `-f` half of the guard missing; or the
  guard fires on a set `CONF` naming a file.
- **AC2** — When a tick copy made by `sed '/^CONF=/,/^\. "\$CONF"$/d'` over the tick — the conf
  block gone, both `read_bound_key` calls kept, `grep -c '^read_bound_key '` over the copy printing
  2 — runs as `bash resume-tick.sh --repo <fixture>`, it exits 2, stderr carries the same sentence,
  no `declares no` line prints, and no launcher file is written under the sidecar; against the
  staged break the copy walks, prints two NOTEs with an empty path, and launches attempt 1 — which
  is the reading spec 13's NOTE arm records at its own order.
  Red when: a tick that named no conf walks on defaults, which is the H4 arm's own green-by-absence;
  or the copy holds fewer than two calls, which is the block removed with the calls and a copy that
  never enters the function.
  fixture: the tick copy is made by the arm with the `sed` range above, in the scratch kit dir,
  until unit 24's helper replaces the inline `sed`.
- **AC3** — When `bash tools/unattended/unattended.sh --status tRun` runs over the driver suite's
  fixture with its conf declaring no `GATE_BOUND`, stderr carries `declares no GATE_BOUND` followed
  by `Declare one in ` and the fixture conf's path, exit 0;
  `grep -c 'CONF unset or naming no file' tools/unattended/lib-unattended.sh` and
  `grep -c 'sourced the conf into THIS shell' tools/unattended/lib-unattended.sh` each print 1 at
  the tip and 0 over the lib at the start of this unit's pass, where
  `grep -c '^read_bound_key() ' tools/unattended/lib-unattended.sh` already prints 1.
  Red when: the driver's own path regressed, which is every verb refusing on a conf that declares
  nothing; or the guard's sentence is absent; or the header does not state the contract, which the
  second grep alone sees, since the first matches the refusal echo.
  figure: every count is DERIVED by the greps at observation, over the tip and over the file at the
  tip of unit 13's pass — the commit whose subject carries `TOOL-aWokenSentinel-13` — never over
  `12513c25`, where the lib holds no `read_bound_key` and the zero would be vacuous.
- **AC4** — When `grep -c "sed '/^CONF=/" memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-13.md`
  runs it prints at least 1 — the same `sed` range this spec's S3 and AC2 spell — and
  `grep -c 'red against the BLOCK copy' memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-13.md`
  prints at least 1, which is that spec's §7 naming the BLOCK copy as one arm's break beside the
  SOURCE, WORKTREE and CLEAR copies it names for the others.
  Red when: the two specs spell the copy differently, which is round-3 H4 — four spellings across
  two documents, one of which cannot print the guard's sentence; or spec 13 names one break for
  every arm, which is round-2 H4 re-entering by prose.
  figure: both counts are DERIVED by the greps at observation; both are run at authoring time and
  print 1 and 1 over spec 13 rev-3.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the bare-shell calls of
AC1, the tick copy of AC2, the driver invocation and greps of AC3, and the greps of AC4.

New arm: `tools/unattended/resume-tick.test.sh` · the bare-shell call with `CONF` unset and with `CONF` naming no file, and the tick copy with the conf block removed by the `sed` range and both calls kept; the break is the lib at the tip of order 13, guard absent · `FLOOR_ASSERTIONS` rises by the arms' executed assertions

## 8. Open questions

none

## 9. Revision log

- rev-2 · 2026-09-20 · §1 · S1 · S3 · S4 · §3 · §5 · AC1 · AC2 · AC3 · AC4 · §7 · folded
  spec-audit round 3: sibling agreement for the promoted `TOOL-aWokenSentinel-24` (H4, raw 18) —
  the BLOCK copy is spelled once, in §1, S3, the Edges and AC2, as the `sed` range from `CONF=`
  through `. "$CONF"` with both `read_bound_key` calls KEPT, and a `hands-off` names the helper
  that makes it one artifact; M7 (raw 19) — §1 and S4 no longer claim this unit gives spec 13's
  arm its break: that arm reds at its own order on the empty path, and this unit re-reads the same
  copy as exit 2, which spec 13 rev-3 states; M8 (raw 10, 32) — the staged break is the lib at the
  tip of order 13, which holds the hoisted function, never the lib at `12513c25`, which holds none,
  and AC3's base figure is read there; M9 (raw 20, 33) — AC4's needle was case-sensitive prose
  that printed 0 at HEAD and its second clause had no command, so both read the shared `sed`
  spelling and the `red against the BLOCK copy` phrase, run at authoring time; M10 (raw 9) — AC1
  exports `CONF=/nonexistent/path` so the `-f` conjunct has a failing observation; L2 (raw 11) —
  AC3 pins the header phrase `sourced the conf into THIS shell`, which the refusal echo cannot
  satisfy.
- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 2 as the
  promotion of H4 (raw id 4).

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "refuse a bound key read when no conf file was named"`
returned no seam and `unscanned layers: .sh`; no existing seam fits. The seam, read at source:
`read_bound_key` at `tools/unattended/unattended.sh:358` to `:368`, whose malformed-value branch
already refuses with exit 2 on stderr and whose NOTE interpolates `$CONF`; the driver's own `CONF`
assignment and missing-file refusal at `:323` to `:325`; and `lib-unattended.sh`'s header rule
that a predicate two scripts share lives there. The recall probe returned `TOOL-aDeclaredCeiling-1`
(a ceiling that should be a declared pin, the same "where is the value from" question),
spec 13's §10, and `TOOL-aHoistedPass-40` (the kit gate's allow-list as a fourth spelling of the key
set); none records a bound read refusing on an unnamed conf.

Recall terms used: `read_bound_key CONF calling shell NOTE declares no default exit 2 sourced conf bound key refuse`
