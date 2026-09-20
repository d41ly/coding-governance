# TOOL-aWokenSentinel-24 — the tick's conf-block staged break is ONE artifact: `build_tick_without_conf_block` in the tick's suite makes the copy from two anchor lines and asserts its shape, so both arms that stage it name a helper and no count

**Status:** SPECCED · rev-1 · 2026-09-20 · node a · Tier-2 · base 830c46e8 · streams tooling · order 24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-review-TOOL-aWokenSentinel-21-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-21-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 |

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H4 (round 3, raw id 18): `TOOL-aWokenSentinel-18` spelled its second arm's
staged break two incompatible ways — its §3 Edges removed "the two calls" with the block, its S3
and AC2 removed "four lines" and kept them — and `TOOL-aWokenSentinel-13` defined the same BLOCK
copy as "the whole conf block of §4", a seven-line block with both calls, while its S3 said "WHOLE
four-line" and its Files-touched row said "five lines". Only the calls-kept reading can print the
guard's sentence, and the sibling agreement spec 18 AC4 required landed on the reading that cannot.
Both specs are folded to one spelling: the four lines `CONF=`, the `[ -f "$CONF" ]` refusal, the
two clearing assignments and `. "$CONF"`, removed by `sed '/^CONF=/,/^\. "\$CONF"$/d'`, the
`shellcheck` comment going with them uncounted and the two `read_bound_key` calls kept. This unit
makes that spelling an ARTIFACT rather than a sentence two documents must keep agreeing on: a
helper in `tools/unattended/resume-tick.test.sh` produces the copy from the two anchor lines and
asserts what the copy holds — two calls, no `CONF=`, no source line — so spec 13's NOTE arm and
spec 18's refusal arm stage the break by calling one name, and a count of lines is spelled nowhere.

## 2. Scope (IN)

- **S1** — `build_tick_without_conf_block` in `tools/unattended/resume-tick.test.sh`, beside that
  suite's assertion helpers: takes the tick's path and an output path, writes the copy with
  `sed '/^CONF=/,/^\. "\$CONF"$/d'`, and asserts through the suite's `same` that the copy holds
  exactly two lines matching `^read_bound_key `, zero matching `^CONF=` and zero matching
  `^\. "\$CONF"$`. A range that ate a call, or one that stopped short of the source line, reds the
  helper before either arm reads the copy. Observed by AC1 and AC2.
- **S2** — Spec 13's NOTE arm (its AC2) and spec 18's refusal arm (its AC2) each stage the BLOCK
  copy by calling the helper, and neither carries an inline `sed` over the tick any longer; their
  readings are unchanged — the empty-path NOTE refused by `test -f` at unit 13's order, exit 2 with
  the guard's sentence and zero NOTEs from unit 18's order on. Observed by AC3.
- **S3** — The helper is observed RED first against a tick copy whose `. "$CONF"` line was
  re-spelled `source "$CONF"`, where the range finds no end anchor, runs to end of file, and the
  copy holds zero calls; and against a tick with a second `read_bound_key` call added above the
  block, where the copy holds three. Observed by AC1.

## 3. Non-goals (OUT)

- **No change to the tick.** The block's four lines, the comment and the two calls are unit 13's
  and stay where and as they are; this unit reads the tick's own anchors and edits nothing in it.
- **No change to either arm's reading.** What the BLOCK copy prints at each order is spec 13 rev-3
  and spec 18 rev-2; this unit changes how the copy is MADE, not what it says.
- **No marker comments in the tick.** A `# conf-block: begin` pair would give the range a name at
  the cost of two shipped lines that exist for a test; the two anchors the block already has are
  its first and last lines, and the shape assertion is what catches an anchor that moves.
- **No hoist of the conf load into a lib function.** The driver's own block at `unattended.sh:323`
  to `:341` initialises thirty keys; spec 13 §3 already declines that hoist and this unit does not
  reopen it.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-13` — the conf block in the tick with its two anchor
  lines, and the NOTE arm that stages the BLOCK copy inline at that unit's order, in the tick's
  suite unit 5 created with its assertion helpers and the scratch kit dir its arms copy the tick
  into.
- **consumes-from** `TOOL-aWokenSentinel-18` — the refusal arm that stages the same copy inline at
  that unit's order, and the guard whose sentence the copy reads from there on.
- **hands-off** external — nothing.

## 4. Design

### The helper

```
build_tick_without_conf_block() { # <tick> <out> -> the BLOCK copy: CONF= through . "$CONF" removed, both read_bound_key calls kept
  sed '/^CONF=/,/^\. "\$CONF"$/d' "$1" > "$2"
  same "BLOCK copy keeps both read_bound_key calls" "$(grep -c '^read_bound_key ' "$2")" "2"
  same "BLOCK copy holds no CONF= line" "$(grep -c '^CONF=' "$2")" "0"
  same "BLOCK copy holds no source line" "$(grep -c '^\. "\$CONF"$' "$2")" "0"
}
```

The range is anchored on the block's first and last lines as spec 13 §4 writes them — `CONF=` at
column 0 and `. "$CONF"` alone on its line — so the `shellcheck` comment between them goes with
the block and the calls below the end anchor stay. The three `same` lines are the artifact: they
are what turns "the four-line block" from a phrase into a check, and they run on every copy the
suite makes, so a later edit of the tick that moves an anchor reds the helper naming which count
moved rather than silently changing what both arms stage.

### Why a helper and not one sentence in two specs

Three documents spelled this break four ways before any code existed — four lines, five lines,
seven lines, "the two calls" — and the audit's cross-read on the interface axis found them. The
fold makes the sentences agree today; nothing keeps them agreeing after the next fold, and a
sentence cannot fail. A helper both arms call is one spelling by construction (charter §12, one
shared core, thin callers), and its shape assertions are the failing case a sentence never has.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `build_tick_without_conf_block` | shell function in the tick's suite | `sh.function`, verb `build`, snake — `--suggest` says OK |

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/resume-tick.test.sh` | the helper beside the assertion helpers; spec 13's NOTE arm and spec 18's refusal arm re-pointed at it, their inline `sed` removed |

### Alternatives rejected

- **One agreed sentence in specs 13 and 18, no code.** The fold does that too, and it is the shape
  that produced four spellings; a sentence has no failing case.
- **Marker comments in the tick.** Two shipped lines for a test; the block's own first and last
  lines are anchors already, and the shape assertion catches a moved one.
- **A lib function `load_root_conf` the tick and the driver both call.** The ratified answer for a
  predicate two scripts share, but the driver's block initialises thirty keys the tick does not
  read, spec 13 §3 declines the hoist, and the break would then be a call line — one spelling, but
  a driver change a testability defect does not price.
- **Order this unit before unit 13.** It would then own the block and unit 13 would call it, which
  inverts which unit the conf load belongs to; landing last and re-pointing two arms is the
  promote-at-instance-two rule rather than a design change.

## 5. Production-readiness checklist

- security — N/A; a suite helper.
- perf / scale — one `sed` and three `grep` per copy.
- error / empty / loading states — a missing tick path makes `sed` fail and the first `same` reds
  on an empty count; an anchor that moved reds the helper naming which count.
- observability — each `same` names the property that failed and both counts.
- risks — a future third line matching `^CONF=` in the tick would widen the range; the
  `no CONF= line` assertion then passes while the copy loses more than the block, and the calls
  assertion is what reds it. A tick that re-spells the source line to `source` reds the helper on
  every run, which is the correct place to learn the anchor moved.
- testing — §6; the helper on the tick and on two staged copies, seconds.
- migration — N/A.
- user docs — none; the helper's comment.

## 6. Acceptance criteria

The fixture is spec 5 §6's scratch repo under a short `%TEMP%` path with the tick copied into a
scratch kit dir, as spec 13 and spec 18's arms already copy it.

- **AC1** — When `build_tick_without_conf_block resume-tick.sh <out>` runs over the tick at the
  tip, its three `same` pass and the copy's `grep -c '^read_bound_key '` prints 2; over a tick copy
  whose `. "$CONF"` line reads `source "$CONF"` the calls `same` reds with `0`; over a tick copy
  with a third `read_bound_key` line inserted above `CONF=` it reds with `3`.
  Red when: the range eats a call or stops short, which is the four-spellings class made code; or
  the helper passes on a copy that still sources the conf, which is spec 13's arm reading a
  fixture that never staged its break.
  fixture: the two staged copies are made by the arm with `sed` over one line each, in the scratch
  kit dir.
- **AC2** — When the copy the helper made runs as `bash <out> --repo <fixture>` at the tip, it
  exits 2 with `read_bound_key was called with CONF unset` on stderr, zero `declares no` lines and
  no launcher under the sidecar — spec 18 AC2's reading, unchanged by the helper.
  Red when: the copy walks on defaults, which is the helper having removed the calls with the
  block.
- **AC3** — When `grep -c 'build_tick_without_conf_block' resume-tick.test.sh` runs over the
  tick's suite at the tip it prints at least 3 — the definition, spec 13's NOTE arm and spec 18's
  refusal arm — and `grep -cE "sed '/\^CONF=/" resume-tick.test.sh` prints exactly 1, the helper's
  own line; over the file at the tip of unit 18's pass — the commit whose subject carries
  `TOOL-aWokenSentinel-18`, not `830c46e8`, where the suite does not exist — the first prints 0
  and the second prints 2.
  Red when: an arm still carries its own `sed` over the tick, which is the second spelling this
  unit exists to remove; or the helper exists and neither arm calls it.
  figure: every count is DERIVED by the greps at observation, over the tip and over the file at
  the tip of unit 18's pass, which is where the two inline spellings exist.

## 7. Gates

`unattended kit gate` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the helper over the
three tick copies of AC1, the copy's run of AC2 and the greps of AC3. Under `lexicon naming
predicates`, the minted name is graded in cell `sh.function`.

New arm: `tools/unattended/resume-tick.test.sh` · the helper's three shape assertions on every BLOCK copy, whose breaks are the re-spelled source line and the third call · `FLOOR_ASSERTIONS` rises by the helper's executed assertions, twice per suite run

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 3 as the
  promotion of H4 (raw id 18): the one spelling is spec 13's rev-3 and spec 18's rev-2 fold, and
  the helper that makes it an artifact is this unit.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "produce a script copy with one block removed by
anchored lines and assert the copy's shape before an arm reads it"` ranked `read_text` in
`tools/memory-tree/gen_build_index.py` and the `read` seam across six memory-tree modules, Python
readers with no bearing on a shell fixture, and reported `unscanned layers: .sh`; no existing seam
fits. The seam, read at source, is the driver suite's own copy idioms — the stripped copy at
`tools/unattended/unattended.test.sh:2092`, made by one `sed` over the driver into a scratch path
with the lib beside it, which is the shape every copy arm in the kit follows — and the block as
spec 13 §4 writes it, whose first and last lines are the anchors. The recall probe returned
`TOOL-cGradedDebt-4` (a meta-check whose predicate found a pre-existing re-spelling nobody had
noticed, routed through a helper — the same move), this build's run-state row for this unit, and
`TOOL-aDeferredBar-22`; no prior record names a fixture helper that asserts its own copy's shape.

Recall terms used: `staged break sed range copy fixture helper conf block line count two spellings resume-tick test.sh arm RED-first shape assertion`
