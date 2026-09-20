# TOOL-aWokenSentinel-17 — the driver suite reads `--status` by FIELD: one extraction helper armed on a suffixed line, and a one-line assertion armed against a two-line driver

**Status:** CLOSED · rev-3 · 2026-09-21 · node a · Tier-2 · base 12513c25 · streams tooling · order 16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-build-TOOL-aWokenSentinel-17-1-acceptance-ledger.md](../build/2026-09-20-build-TOOL-aWokenSentinel-17-1-acceptance-ledger.md) | journal | — |
| [2026-09-20-prompt-TOOL-aWokenSentinel-17-1-build-brief.md](../prompts/2026-09-20-prompt-TOOL-aWokenSentinel-17-1-build-brief.md) | journal | — |
| [2026-09-20-review-TOOL-aWokenSentinel-15-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-15-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 |

<!-- /gen:spec-records -->

## 1. Goal

Close audit findings H2 (round 2, raw ids 34 and 49) and H3 (raw id 3). H2: the driver's
`printf` at `tools/unattended/unattended.sh:2975` takes `$parked` as its LAST operand, so every
suffix — `parked`, `noted`, `STALE briefs`, `briefs gone`, unit 5's `resume-tick` field — prints
AFTER `next`; `TOOL-aWokenSentinel-9` §4 said the inverse, its AC1 required the line to end with
`next`, and the suite's whole-line reader `sed 's/.*· next //'` at
`tools/unattended/unattended.test.sh:1874` yields the unit id only because its fixture accumulates
no suffix, a precondition nothing states. H3: spec 9's one-line arm, `run --status tRun | wc -l`
printing `1`, was to be observed red against a driver copy with the field clause removed, and that
copy prints one line too, so the arm could only ever be seen passing. This unit puts the suite's
reading of the status line on two helpers, each observed red against its own staged break: `extract_next`
cuts the `next` field's value under any suffix, and `check_status_one_line` asserts the verb's
stdout is exactly one line. Spec 9 is folded at its rev-2 to the code's field order and reads
through both.

## 2. Scope (IN)

- **S1** — `extract_next` in `tools/unattended/unattended.test.sh`, beside `hit`, `miss` and
  `same`: takes a status line and prints the value of its `next` field, cut at the next ` · `
  separator — `sed -n 's/.*· next //p' | sed 's/ · .*//'` — so a line carrying any number of
  suffixes yields the unit id and a line with none yields the same bytes the raw reader did.
  Observed by AC1 and AC3.
- **S2** — `check_status_one_line` in the same file: runs `bash "$SCRIPT" --status <slug>` with
  stderr DROPPED, counts stdout lines with `printf '%s' "$_o" | grep -c ''` — which reads an EMPTY
  capture as `0`, where `printf '%s\n' "$_o" | wc -l` reads it as `1` — asserts `1` through
  `same`, and prints the line for the caller. Stderr is dropped because the driver's
  `read_bound_key` NOTEs go there and are not the promise the header at `unattended.sh:8` makes
  about stdout. Observed by AC2 and AC4.
- **S3** — The reader at `:1874` calls `extract_next` on the same fixture and keeps its control
  `want_unit` byte-identical, so the arm still compares the helper's row to an awk re-derivation;
  the `grep -c 'next '` reader at `:1859` is untouched, because a count is indifferent to suffixes.
  Observed by AC3.
- **S4** — Two arms in region two: on a fixture whose record carries one parked row, so the line
  ends `· next <unit> · parked 1`, `extract_next` yields the unit id, observed RED first against a
  copy of the helper reduced to the raw `sed 's/.*· next //'`; and `check_status_one_line tRun`
  asserts `1` on that fixture, observed RED first against a driver copy with `printf 'x\n'`
  appended after the status `printf`, which is unit 7 S4's retired second line. Observed by AC1
  and AC2.

## 3. Non-goals (OUT)

- **No driver change.** The field order is the code's and stays: `halt-code` before `next`, every
  other suffix after it. The suite learns to read it; the verb does not learn a new order.
- **No rewrite of the thirty-two `run --status` readers.** Those that grep a substring are
  indifferent to order and line count; at this unit's order the whole-line readers in the file are
  S3's two, and the units sequenced after it that add one — unit 7's AC5 and unit 9's arm — take
  the helpers, which is why this unit lands before both.
- **No field of its own.** The keepalive field is unit 9's; this unit is why unit 9's field can be
  the last suffix without moving a reader.

### Edges

- **consumes-from** external — the `printf` at `tools/unattended/unattended.sh:2975` and its
  operand order, the suite's helpers at `tools/unattended/unattended.test.sh:69` to `:71`, its
  `run` at `:359`, and the two whole-line readers at `:1859` and `:1874`.
- **hands-off** `TOOL-aWokenSentinel-7` — that unit's AC5, the one-line `--status` assertion over
  three fixtures, routes through `check_status_one_line` rather than `run --status | wc -l` over
  merged stderr, the shape §4 rejects; spec 7 is folded at its rev-4 to cite it, and the two units
  swapped orders so the helper exists when the arm is written.
- **hands-off** `TOOL-aWokenSentinel-9` — the one-line arm over that unit's fully populated
  fixture through `check_status_one_line`, and the keepalive field appended as the LAST suffix,
  which `extract_next`'s cut leaves out of the `next` value; spec 9's §4 field-order paragraph and
  AC1 are folded at its rev-2 to the code's order and read through these helpers.
- **hands-off** `TOOL-aWokenSentinel-23` — the CLASS the rev-1 helper carried: a line count over a
  captured variable that adds a newline before counting; that unit gates it in the kit gate and
  records it under `memory/gotchas/`, and this unit's helper is the instance it must not red.

## 4. Design

### The two helpers

```
extract_next() { # status-line -> the `next` field's value, cut at the next separator
  printf '%s\n' "$1" | sed -n 's/.*· next //p' | sed 's/ · .*//'
}
check_status_one_line() { # slug -> asserts --status wrote exactly one stdout line; prints it
  local _o; _o=$(bash "$SCRIPT" --status "$1" 2>/dev/null)
  same "--status $1 is one stdout line" "$(printf '%s' "$_o" | grep -c '')" "1"
  printf '%s\n' "$_o"
}
```

`grep -c ''` counts the lines of what it is given and prints `0` on empty input; `wc -l` counts
newlines, and `printf '%s\n'` adds one to an empty capture, so the rev-1 helper read a verb that
wrote NOTHING as one line (round-3 audit H3, measured: `_o=""; printf '%s\n' "$_o" | wc -l` prints
`1`, `printf '%s' "$_o" | grep -c ''` prints `0`). A capture that ends without a newline — one
line, since `$(…)` strips the trailing one — reads `1` under `grep -c ''` and `0` under `wc -l`,
which is the other half of why the count is this and not that.

`sed -n 's/.*· next //p'` prints only the line carrying the field, so a NOTE line that reached the
input through `run`'s `2>&1` is dropped rather than mangled; the second `sed` cuts at the first
` · ` after the value, which is the separator every suffix uses and the value never contains. The
value is the roster row's LABEL as the README's units pair spells it, `<id> — <title>` (measured at
the pass: `ARCH-tRun-1 — the unit`), whose joiner is an em dash and not the middle dot, so the cut
leaves the title in place — and the `want_unit` control derives the same label. On a line with no
suffix the cut matches nothing and the output is what the raw reader printed, which is why the
`:1874` arm's expected value does not move.

### Why the one-line assertion drops stderr

`run` merges stderr so that refusal arms can `hit` a `fail` sentence; the header's `# one line`
promise is about stdout, and the driver legitimately writes NOTEs to stderr when the conf declares
no bound. Counting `run`'s output would red on a conf that declares nothing and pass on one that
declares everything, which is a test of the fixture's conf and not of the verb.

### The staged breaks, one per arm

| arm | break | red reading |
|---|---|---|
| `extract_next` on the parked fixture | the helper's body reduced to `sed 's/.*· next //'` | the unit id followed by ` · parked 1` |
| `check_status_one_line` on the same fixture | a driver copy with `printf 'x\n'` inserted after the status `printf` | `2` |
| `check_status_one_line` on the same fixture | a driver copy with the status `printf` line deleted | `0` |

The second break is unit 7 S4's retired shape, the only way the base driver has ever printed a
second line; the third is the empty case, a verb that wrote nothing, which the rev-1 helper could
not tell from one line. Both are staged by copying the driver to a scratch path WITH
`lib-unattended.sh` copied beside it and pointing `SCRIPT` at the copy for that one invocation —
the stripped-copy idiom at `unattended.test.sh:2092`, whose comment says why the lib travels, and
not the L2 idiom at `:5022`, which copies the driver alone on purpose to observe the
missing-library refusal at `unattended.sh:73`. A copy without the lib exits 2 on stderr before
reaching its status `printf`, writes nothing to stdout, and reads `0` here for the wrong reason.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `extract_next` | shell function in the driver suite | `sh.function`, verb `extract`, snake — `--suggest` says OK |
| `check_status_one_line` | shell function in the driver suite | `sh.function`, verb `check`, snake — `--suggest` says OK |

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/unattended.test.sh` | the two helpers beside `hit`/`miss`/`same`; the `:1874` reader through `extract_next`; two arms in region two |

### Alternatives rejected

- **Reorder the `printf` so `next` is last.** Every suffix moves, every reader that keys on
  `parked`/`noted` position moves with it, and unit 5's field and unit 9's field would both have to
  re-spec; the readers are two lines and the verb is shared by `--resume`.
- **Extend `run` to assert one line on every `--status`.** `run` merges stderr and is called with
  every verb; a stdout-only variant for one verb is what `check_status_one_line` is.
- **Name a second break in spec 9 and leave the reader raw.** Closes H3 and leaves H2's reader
  one suffix away from red, which unit 9's own populated fixture would then be the first to hit.

## 5. Production-readiness checklist

- security — N/A; two suite helpers.
- perf / scale — two `sed` per read; nothing measurable.
- error / empty / loading states — a line with no `next` field yields empty output from
  `extract_next`, and the `:1874` `same` then reds naming the empty value; a verb that prints
  nothing reads `0` lines under `check_status_one_line` because the count is `grep -c ''` over a
  `printf '%s'`, which reds as loudly as `2` and is AC2's third reading.
- observability — each helper's `same` names the slug and the count.
- risks — a future suffix whose VALUE contains ` · ` would be cut early; no field prints one, and
  the field grammar unit 9 states forbids it. A roster TITLE carrying ` · ` would be cut early
  too; none in this tree does, and the awk control shares the exposure, so the arm would red
  rather than pass wrong.
- testing — §6; two arms and one edited reader, seconds each.
- migration — N/A.
- user docs — none; the helpers' comments.

## 6. Acceptance criteria

The fixture is the suite's `tRun` build after `--preflight`, plus one `--park tRun --item x
--reason y` so the record carries a parked row and the status line ends `· next <unit> · parked 1`.
Each observation runs in a scratch clone.

- **AC1** — When `extract_next "$(run --status tRun)"` runs on that fixture it prints the unit id
  the awk control at `unattended.test.sh:1872` derives, with no ` · parked` tail; against the
  helper reduced to `sed 's/.*· next //'` it prints the id followed by ` · parked 1`.
  Red when: a suffix reaches the `next` value, which is every reader keyed on the field's end
  breaking the day a fixture carries a suffix; or the cut eats part of the id.
- **AC2** — When `check_status_one_line tRun` runs on that fixture its `same` passes with `1` and it
  prints the line; against a driver copy with `printf 'x\n'` appended after the status `printf` the
  `same` reds with `2`; against a driver copy with the status `printf` line deleted it reds with
  `0`. Each copy is made with `lib-unattended.sh` beside it, and the copy's own stdout — not a
  missing-library refusal — is what is counted.
  Red when: the arm passes on the two-line copy, which is the H3 class — an arm only ever seen
  passing; or it passes on the empty copy, which is round-3 H3, the same class one helper down;
  or stderr is counted, which reds on a conf that declares no bound; or the copy lacks its lib
  and the `0` is the refusal's, not the verb's.
- **AC3** — When `grep -c 'extract_next' tools/unattended/unattended.test.sh` runs at the tip it
  prints at least 3 — the definition, the `:1874` reader and the arm — and 0 at this unit's base;
  and the `want_unit` control line at `:1872` is byte-identical between base and tip.
  Red when: the reader still cuts nothing, or the control was edited to admit the defect.
  figure: 3 is DERIVED by the grep at observation; 0 at base is DERIVED by the same grep over the
  file at `12513c25`.
- **AC4** — When the fixture's conf is rewritten with `GATE_BOUND` deleted, so the driver writes
  its `declares no GATE_BOUND` NOTE to stderr, `check_status_one_line tRun` still reads `1`.
  Red when: a NOTE counts as a second line, which makes the promise depend on the conf.

## 7. Gates

`unattended kit gate` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the helper invocations of
AC1, AC2 and AC4 over the fixture and the greps of AC3. Under `lexicon naming predicates`, the two
minted names are graded in cell `sh.function`.

New arm: `tools/unattended/unattended.test.sh` · the parked fixture read through `extract_next`, whose break is the helper reduced to the raw `sed`; the one-line assertion, whose breaks are a driver copy printing a second line and a driver copy printing none, each with the lib beside it · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` rise by the arms' executed count, region two

## 8. Open questions

none

## 9. Revision log

- rev-3 · 2026-09-21 · §4 · §5 · folded at the pass: §4 said the `next` value is a bare unit id in
  `[A-Za-z0-9-]`; the driver prints the roster row's label, `<id> — <title>`, and the pass measured
  `ARCH-tRun-1 — the unit`. The cut holds because the label's joiner is an em dash, and §5 names
  the title as the other place ` · ` could appear. No design change; the helpers are §4's bodies
  verbatim, the AC4 reading is a permanent arm beside the two S4 names, and the executed count is
  seven.
- rev-2 · 2026-09-20 · S2 · §3 · §4 · §5 · AC2 · §7 · folded spec-audit round 3: sibling agreement
  for the promoted `TOOL-aWokenSentinel-23` (H3, raw 28) — `check_status_one_line` counts with
  `printf '%s' "$_o" | grep -c ''`, so an empty capture reads `0`, §5's empty-state sentence is
  true, and AC2 gains the empty-copy reading; M5 (raw 29) — the driver copies are made with the
  lib beside them, the `:2092` idiom and not the `:5022` one, so the count is the verb's stdout
  and not a missing-library refusal; M6 (raw 23, 41) — spec 7's AC5 was a third whole-line reader
  one order before this unit in the shape §4 rejects, so §3 states the readers at this order, a
  `hands-off` on unit 7 routes its AC5 through the helper, and the two units swapped orders.
  Order 17 → 16, swapped with unit 7.
- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 2 as the
  promotion of H2 (raw ids 34, 49) and H3 (raw id 3), one unit because both are the suite's
  reading of one line.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "extract the next field from a status line under any
suffix and assert the output is one line"` returned no seam and `unscanned layers: .sh`, so the
suite is invisible to it; no existing seam fits. The seam, read at source: the suite's assertion
helpers at `tools/unattended/unattended.test.sh:69` to `:71`, its `run` at `:359`, the two
whole-line readers at `:1859` and `:1874` with the awk control at `:1872`, and the driver's
`printf` at `tools/unattended/unattended.sh:2975` whose operand order this unit reads rather than
changes. The recall probe returned a `dScriptedRepeat` acceptance-ledger row on the `same`
byte-equality helper, this build's round-2 audit at the H2 paragraph, and spec 9's own §10, which
names the `:1874` reader as the reason the listing is a field; no prior record names a field-wise
reader.

Recall terms used: `status line next field sed reader one line suffix parked noted printf whole-output fixture`
