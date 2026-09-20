# TOOL-aWokenSentinel-18 — `read_bound_key` refuses a caller that named no conf: a bound read from a shell with `CONF` unset exits 2 instead of taking a default with an empty NOTE

**Status:** SPECCED · rev-1 · 2026-09-20 · node a · Tier-2 · base 12513c25 · streams tooling · order 14

<!-- gen:spec-records -->

*No record names this unit.*

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
every call, is untouched in behaviour, and spec 13's arm gains a break it reds against — the whole
conf block removed from the tick.

## 2. Scope (IN)

- **S1** — `read_bound_key` in `tools/unattended/lib-unattended.sh` opens with one guard:
  `[ -n "${CONF:-}" ] && [ -f "$CONF" ]`, else it writes `unattended: REFUSING - read_bound_key was
  called with CONF unset or naming no file, so its NOTE could name nowhere to declare the key and a
  default would be taken from nowhere; set CONF to the sourced conf before the call` to stderr and
  exits 2 — the same channel and code its malformed-value refusal already uses. The function's
  header comment states the contract: the caller sources the conf into this shell and names it in
  `CONF`. Observed by AC1, AC2 and AC3.
- **S2** — The driver's two calls at `unattended.sh:369` and `:370`, made after `CONF` is set at
  `:323` and sourced at `:341`, are unchanged and still read their declared values, defaults and
  NOTEs exactly as before; the guard never fires on the driver's path. Observed by AC3.
- **S3** — Two arms in the tick's suite: sourcing the lib into a bare shell with `CONF` unset and
  calling `read_bound_key` exits 2 with the sentence, and a tick copy with unit 13's whole
  four-line conf block removed exits 2 with the same sentence and writes no NOTE and no launcher.
  Each is observed RED first against the lib at this unit's base, where the first prints a NOTE
  with an empty path and exits 0 and the second walks on defaults. Observed by AC1 and AC2.
- **S4** — Spec 13's §7 names, per arm, the break it is observed red against: the source-line-only
  copy for its declared-cap and declared-turns arms, and the whole-block copy — this unit's refusal
  — for its NOTE arm, whose count half reads zero NOTEs there. Observed by AC4.

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
- **consumes-from** `TOOL-aWokenSentinel-13` — the tick's conf block (`CONF=`, the refusal, the
  source, the two calls), whose whole removal is the staged break this unit's second arm reads.
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
| `tools/unattended/resume-tick.test.sh` | two arms: the bare-shell call, and the tick copy with the whole conf block removed |

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
  one sentence; a set `CONF` behaves as before.
- observability — the refusal names the contract and the remedy.
- risks — a third caller that sets `CONF` to a path it never sourced passes the guard and reads
  the environment; the header says the caller sources the file, and no such caller exists.
- testing — §6; two arms in the tick's suite, seconds each.
- migration — N/A; both existing callers set `CONF` before the call.
- user docs — none; the function's header.

## 6. Acceptance criteria

The fixture is spec 5 §6's scratch repo under a short `%TEMP%` path with its stub `claude` and
unit 13's conf block in the tick. The staged break for AC1 and AC2 is the lib at this unit's base.

- **AC1** — When a bare `bash` sources `tools/unattended/lib-unattended.sh` with `CONF` unset and
  runs `read_bound_key RESUME_ATTEMPTS 6 attempts "n"`, it exits 2 and stderr carries
  `read_bound_key was called with CONF unset`; against the lib at this unit's base the same call
  exits 0 and stderr carries `Declare one in  to change it`, the empty path.
  Red when: the empty-path NOTE is still producible, which is the specced defect's own signature;
  or the guard fires on a set `CONF`.
- **AC2** — When a tick copy with unit 13's whole four-line conf block removed runs
  `bash resume-tick.sh --repo <fixture>`, it exits 2, stderr carries the same sentence, no
  `declares no` line prints, and no launcher file is written under the sidecar; against the lib at
  this unit's base the copy walks, prints two NOTEs with an empty path, and launches attempt 1.
  Red when: a tick that named no conf walks on defaults, which is the H4 arm's own green-by-absence.
  fixture: the tick copy is made by the arm with `sed` over the four lines, in the scratch kit dir.
- **AC3** — When `bash tools/unattended/unattended.sh --status tRun` runs over the driver suite's
  fixture with its conf declaring no `GATE_BOUND`, stderr carries `declares no GATE_BOUND` followed
  by `Declare one in ` and the fixture conf's path, exit 0; and
  `grep -c 'CONF unset or naming no file' tools/unattended/lib-unattended.sh` prints 1 and 0 at
  this unit's base.
  Red when: the driver's own path regressed, which is every verb refusing on a conf that declares
  nothing; or the guard's sentence is absent.
  figure: 1 and 0 are DERIVED by the grep at observation over the tip and over the file at `12513c25`.
- **AC4** — When `grep -c 'whole four-line' memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-13.md`
  runs it prints at least 1, and spec 13's §7 names two breaks.
  Red when: spec 13 still names one break for every arm, which is H4 re-entering by prose.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the bare-shell call of
AC1, the tick copy of AC2, the driver invocation and grep of AC3, and the grep of AC4.

New arm: `tools/unattended/resume-tick.test.sh` · the bare-shell call with `CONF` unset and the tick copy with the whole conf block removed; the break is the lib at this unit's base · `FLOOR_ASSERTIONS` rises by the arms' executed assertions

## 8. Open questions

none

## 9. Revision log

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
