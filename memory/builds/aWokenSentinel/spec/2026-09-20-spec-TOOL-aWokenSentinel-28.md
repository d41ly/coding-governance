# TOOL-aWokenSentinel-28 — the `echo` and here-string spellings unit 23 does not stage get their own staged lines and RED readings, so every branch of the added-newline predicate has been seen to fail

**Status:** CLOSED · rev-3 · 2026-09-21 · node a · Tier-2 · base 830c46e8 · streams tooling · order 28

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-build-TOOL-aWokenSentinel-28-1-acceptance-ledger.md](../build/2026-09-20-build-TOOL-aWokenSentinel-28-1-acceptance-ledger.md) | journal | — |
| [2026-09-20-prompt-TOOL-aWokenSentinel-28-1-build-brief.md](../prompts/2026-09-20-prompt-TOOL-aWokenSentinel-28-1-build-brief.md) | journal | — |
| [2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md](../reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md) | diff-review | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24 TOOL-aWokenSentinel-25 TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 |
| [2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round2.md](../reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round2.md) | diff-review | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24 TOOL-aWokenSentinel-25 TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 |

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H6 (round 4, raw id 2): `TOOL-aWokenSentinel-23` bans three spellings of the
line count that reads an empty capture as one line — `printf '%s\n' "$x" | wc -l`,
`echo "$x" | wc -l` and `wc -l <<< "$x"` — and its S3 and AC1 stage one, the `printf` line. The
`echo` spelling shares the regex's first group and is exercised only weakly by it; the here-string
spelling is a separate top-level alternation with the variable on the OTHER side of `wc -l`, and
nothing in spec 23 ever sees it red, so a mis-escaped `<<<` branch passes every criterion and the
class gate lands with two of its three cases never observed to fail, which is the charter §7 rule
for a new gate broken twice. Spec 23 keeps its `printf` staging; this unit stages the other two
spellings in the same suite copy, each read RED by the checker naming the line, GREEN with the
line removed, with spec 23's near-miss beside them, and the suite arm carries all three so the
`harness arms` leg keeps every branch of the predicate covered by a line that once failed.

## 2. Scope (IN)

- **S1** — Two more staged lines in the arm spec 23 S4 adds to
  `tools/unattended/check-unattended.test.sh`, each spliced inside a function body of a fresh
  suite copy in turn, by the splice spec 23's arm uses: `_x=$(echo "$_o" | wc -l)` and
  `_x=$(wc -l <<< "$_o")`. For each, the copied checker prints unit 23's `fail` sentence naming
  the copy's basename and the line, and exits 1; with the line deleted from that copy it prints
  no failure for that check. Observed by AC1.
- **S2** — The three staged lines are assembled in the arm from fragments — the command word, the
  variable and the pipe joined at run time — so the suite's own bytes never match the predicate
  and the population exclusion spec 23 rev-2 names for this suite is belt beside braces, not the
  only thing keeping the close green. Observed by AC2.
- **S3** — The two readings are observed RED at the pass, before the arm is committed, over the
  scratch kit dir spec 23 §4 describes, with the `echo` line and then the here-string line
  spliced into the suite copy; and GREEN with each deleted from it. Observed by AC1.
- **S4** — `FLOOR_ASSERTIONS` (the `^FLOOR_ASSERTIONS=` line of `check-unattended.test.sh`) and
  the floor of the shard the arm joins rise by the readings' executed count, `mutate` calls
  included. Observed by AC3.

## 3. Non-goals (OUT)

- **No change to the predicate.** The three spellings, the code-line anchor and the population
  are unit 23's; this unit reads two branches of it and adds no fourth.
- **No re-stage of the `printf` line.** Spec 23 S3 and S4 own it; a second line with the same
  bytes is a duplicate the leg cannot tell from the first.
- **No fourth spelling.** `printf '%s\n' "${x}"` with braces and the unquoted forms are outside
  unit 23's predicate by its own header; a gate's suite reads what the gate reads.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-23` — the check with its three-branch predicate and
  `fail` sentence, the suite arm with the `printf` staged line and the near-miss, the scratch kit
  dir seeding at `check-unattended.test.sh:65` with the suite copy that unit's rev-2 adds to it,
  and the population exclusion for `check-unattended.test.sh`; without the check there is no
  refusal to read.
- **consumes-from** external — `check-unattended.test.sh`'s `hit` and `same` helpers and its
  quoted-heredoc staging idiom at `:188`.
- **hands-off** external — nothing.

## 4. Design

### The two lines, beside the first

```
# ECHO — the first group's other spelling. Assembled, so this file's own bytes are not a hit.
reset_tree
cp "$HERE/unattended.test.sh" $KIT_REL/
_lc_cmd="ec""ho"; _lc_line="  _x=\$($_lc_cmd \"\$_o\" | wc -l)"
printf '%s\n' "$_lc_line" > "$TMPBIN_PARENT/lc.line"
mutate $KIT_REL/unattended.test.sh "/^check_status_one_line() {/r $TMPBIN_PARENT/lc.line"
out=$(run)
hit "$out" "counts a captured variable's lines by adding a newline first"
hit "$out" "hits: unattended.test.sh:$_lc_at:"
mutate $KIT_REL/unattended.test.sh '/^check_status_one_line() {/{n;d;}'
miss "$(run)" "counts a captured variable's lines by adding a newline first"
# HERE-STRING — the second top-level alternation: the variable sits AFTER wc -l, not before it.
reset_tree
cp "$HERE/unattended.test.sh" $KIT_REL/
_lc_line="  _x=\$(wc -l <<""< \"\$_o\")"
… the same lines from `printf` on …
```

The copy and the splice are spec 23's arm as it stands: the copy is `$KIT_REL/unattended.test.sh`
(spec 23 names no `_lc_copy`), the checker runs as `run`, and the staged line goes INSIDE
`check_status_one_line() {` by the suite's `mutate` with sed `r` over a file — the one shape that
puts the line inside a function body, as S1 says, rather than after the suite's last line, which
is inside no function. `_lc_at` is the opener's line number plus one, read from the copy by
`grep -n` once, so each RED reading asserts the line the refusal names and not only the basename.
The line is REMOVED by a second `mutate` deleting the line after the opener, so the removal is
asserted a change by the same no-op guard the splice is, and the GREEN that follows reads the
shipped bytes without a fresh copy — a fresh copy is spec 23's restored-copy reading and would be a
duplicate of it. The split literals `"ec""ho"` and `<<""<` are joined by the shell at run time and
never appear contiguous in this file, so unit 23's `^[^#]*` predicate over
`check-unattended.test.sh` finds no hit here even without the population exclusion. The
`printf '%s\n' "$_lc_line" > file` that writes the staged line is a write to a file and not a
pipe into `wc -l`, and is outside the predicate.

### The near-miss stays where it is

Spec 23's `_x=$(printf '%s' "$_o" | wc -l)` reading is the control for the first group; the
here-string group's control is a here-string that is not a count, `read -r _y <<< "$_o"`, which
the arm splices into a fresh copy by the same `mutate` and reads GREEN once, so a `<<<` branch
escaped too loosely — matching every here-string — is seen.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `_lc_line`, `_lc_cmd`, `_lc_at` | locals in one suite arm, the `_lc_` prefix unit 23's check uses | no cell; not functions |

No function, key, verb or file is minted.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/check-unattended.test.sh` | two staged lines with their RED and GREEN readings and one here-string control in unit 23's arm; the two floors raised |

### Alternatives rejected

- **Fold the two lines into spec 23's S3 and S4.** The audit's own fix and the smaller record;
  the same shape round 3 refused for unit 16's arms, because a unit that owns the predicate and
  every reading of it is two mechanisms in one spec. Spec 23 keeps the `printf` reading that
  proves the check exists; this unit proves the other two branches can fail.
- **One staged line carrying all three spellings.** One `hit` for three branches is one
  observation; a regex whose `<<<` branch is dead passes it on the `printf` match.
- **Stage the lines as contiguous literals inside a quoted heredoc.** Spec 23's own idiom; it
  puts the banned bytes on a code line of this suite, which is round 4's M6, and the population
  exclusion would then be the only thing between the arm and a self-hit at the close.

## 5. Production-readiness checklist

- security — N/A; a suite arm over a scratch kit dir.
- perf / scale — two more kit-gate runs on the scratch copy per suite run and one control,
  199 s each on node `a` by the ledger spec 11 read on 2026-09-20; the suite's budget row moves if
  the first reading says so.
- error / empty / loading states — a delete of the line after the opener on a copy with no
  spliced line deletes a real line of the copy and the `miss` reads a different refusal; the arm
  splices before it deletes, in that order, and both edits are `mutate` calls that red on a no-op.
- observability — each `hit` prints the checker's sentence with the file and line it named.
- risks — a fourth spelling of the same defect still passes; unit 23's header says so.
- testing — §6; the two staged lines and the control at the pass, the arm at the close.
- migration — N/A.
- user docs — none.

## 6. Acceptance criteria

The fixture is spec 23's scratch kit dir under a short `%TEMP%` path, seeded as its §4 states and
holding the suite copy its rev-2 adds; never this worktree.

- **AC1** — When the copied checker runs over the suite copy with `_x=$(echo "$_o" | wc -l)`
  spliced inside a function, it prints `UNATTENDED check <n> FAILED` with `adding a newline
  first` naming the copy's basename and that line, and exits 1; with `_x=$(wc -l <<< "$_o")`
  spliced instead, the same; with each line deleted from its copy, no failure for that check;
  with `read -r _y <<< "$_o"` spliced, no failure for that check.
  Red when: either spelling passes, which is a branch of the predicate never seen to fail; or the
  here-string control reds, which bans every here-string rather than the counting one.
  fixture: the scratch kit dir with the suite copy.
  cost: three kit-gate runs beyond spec 23's three, 199 s each on node `a`; the pass runs the
  checker five times in total for this unit, two RED, two GREEN, one control.
  figure: `<n>` is DERIVED by unit 23's pass; 199 is PINNED as read by spec 11 from
  `<git-dir>/gate-ledger.tsv` on 2026-09-20.
- **AC2** — When `grep -cE "(printf '%s\\\\n'|echo) \"\\\$[A-Za-z_][A-Za-z0-9_]*\"[[:space:]]*\|[[:space:]]*wc -l|wc -l[[:space:]]*<<<" tools/unattended/check-unattended.test.sh`
  runs at the tip on code lines — the same predicate unit 23's check greps, `^[^#]*`-anchored —
  it prints 0, and `grep -c 'adding a newline first' tools/unattended/check-unattended.test.sh`
  prints at least 4, the four readings' `hit` and `miss` lines.
  Red when: the suite carries the banned bytes contiguously, which is a self-hit the close's kit
  gate reds; or the readings are absent.
  figure: both counts are DERIVED by the greps at observation.
- **AC3** — When `sed -n 's/^FLOOR_ASSERTIONS=//p' tools/unattended/check-unattended.test.sh` runs
  at the tip, its value is the value at the tip of unit 23's pass — the commit whose subject
  carries `TOOL-aWokenSentinel-23` — plus the executed count of this unit's readings, and the
  shard floor the arm joins has moved by the same count.
  Red when: the floors did not move, which is executed slack nobody declared.
  figure: DERIVED by the `sed` at observation over the two commits.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the five checker runs of
AC1 over the scratch kit dir and the greps of AC2 and AC3. Under `harness arms`, unit 23's `fail`
branch was armed by its own arm; this unit adds readings and moves no branch's verdict.

New arm: `tools/unattended/check-unattended.test.sh` · the `echo` and here-string staged lines in the suite copy, each RED then removed, and the non-counting here-string control · `FLOOR_ASSERTIONS` and the shard floor rise by the readings' executed count

## 8. Open questions

none

## 9. Revision log

- rev-3 · 2026-09-21 · S3 · AC1 · §4 · §10 · the bug-class checklist on the pass commit,
  amendment-leaves-its-other-half-standing: rev-2 moved the design to a splice and a delete but
  left S3, AC1 and §10 saying `appended` and `removed`, and the §4 sketch counting `the same six
  lines`, a count the code owns; one vocabulary now, `spliced` and `deleted`, and no count. No
  code moved; folded in the follow-up commit.
- rev-2 · 2026-09-21 · S1 · S4 · §4 · §5 · §7 · folded at the pass before the code, from reading
  spec 23's arm at source: §4's sketch appended the staged line to the copy's END with `>>` and
  deleted it with `sed -i '$d'`, which is outside every function body and disagrees with S1 and
  AC1 ("inside a function body"); the design is now spec 23's own splice — a fresh copy, the
  fragment file, `mutate` with sed `r` after `check_status_one_line() {` — and a second `mutate`
  deleting the line after the opener for the GREEN, with `_lc_at` asserting the line the refusal
  names. `run_check` is `run` and `_lc_copy` is `$KIT_REL/unattended.test.sh`, the names spec 23's
  arm has; the `:3252` line reference for `FLOOR_ASSERTIONS` is dropped for the `^FLOOR_ASSERTIONS=`
  anchor, since sibling units had already moved it.
- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 4 as the
  promotion of H6 (raw id 2): the fragment assembly and the population exclusion are spec 23's
  rev-2 fold, and the two spellings' arms are this unit.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "stage every alternation of a ban's regex as its own
failing line so each branch of the predicate is observed red"` ranked `owners_of` in
`tools/codebase-map/map_lib.py`, `branches` in `tools/memory-tree/check-arms.py` and
`test_every_inventory_key_is_claimed_or_baselined`, none a shell staging, and reported
`unscanned layers: .sh`; no Python seam fits. The seam, read at source, is spec 23's own arm as
its §4 and S4 write it, and the suite's scratch-kit seeding at
`tools/unattended/check-unattended.test.sh:65` with the `hit`/`miss` idiom every arm there uses;
`tools/gate-lint/sh_hygiene.py --selftest` stages one sample per CLASSES row in both directions,
which is the shape this unit copies into shell. The recall probe returned
`TOOL-dPolishedVitrine-10` (a suite whose arms went green with a variable unset — a fixture
that never staged its break), this build's round-4 audit at the H6 paragraph, and
`TOOL-cGradedDebt-4` (a meta-check whose staged break was a second copy appended to the file — the
write-then-read shape S1 uses, spliced rather than appended); no prior record stages these two
spellings.

Recall terms used: `staged break alternation regex predicate RED observed failing case near-miss kit gate check-unattended arm suite copy fixture`
