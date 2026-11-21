# TOOL-dWitnessedBar-66 — the CRLF record arm plants its CR on a key `read_green_file` reads, so removing the hook's CR strip turns the arm red

**Status:** INPROGRESS · rev-3 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 38 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-66-deviation-661.md](../build/2026-10-25-build-TOOL-dWitnessedBar-66-deviation-661.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-66-round6-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-66-round6-fix-return.md) | research | TOOL-dWitnessedBar-67 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-66-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-66-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-66-round6-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-66-round6-fix-brief.md) | research | TOOL-dWitnessedBar-67 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-66-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-66-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-66-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-66-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-66-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-66-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-66-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-66-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-67 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 64 and 65
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-64-spec-audit-round1.md`)
confirmed finding **id 6 at HIGH**, its item **H1**. The report keeps it apart from item M1 (ids 1
and 12), which describes the same AC12 defect at MEDIUM and which `TOOL-dWitnessedBar-67` takes.

`TOOL-dWitnessedBar-65` AC12, as landed at `139d6fea1`, plants its only CR on a `verdict<TAB>GREEN<CR>`
line (`tools/run-gates/run-gates.gov.test.sh@57bfdf31:826`). The hook's `read_green_file`
(`.githooks/pre-push#read_green_file`) reads seven keys, and `verdict` is not one of them. So the staged
red "removing the hook's CR strip" leaves the arm green, as unit 65's builder return records and hands
here. This unit moves the hook half's CR onto the second `sha` line, which `read_green_file` reads into
`rec_sha`, and names that variable as the one each staged break reaches. It repairs
`TOOL-dWitnessedBar-65` and builds one step after it (order 38).

## 2. Scope (IN)

- **S1** — The record the hook half reads. Unit 65's AC12 arm in
  `tools/run-gates/run-gates.gov.test.sh` (`@57bfdf31:817-838`) writes `$rgf_t/record` with
  `printf 'verdict\tGREEN\r\nsha\t%s\nsha\t%s\n'`. This unit ends its third line in `\r\n`, so the
  record holds these lines in this order:

  | line | bytes |
  |---|---|
  | 1 | `verdict<TAB>GREEN<CR><LF>` |
  | 2 | `sha<TAB>` followed by forty `a` characters (`$rgf_a`), then `<LF>` |
  | 3 | `sha<TAB>` followed by forty `b` characters (`$rgf_b`), then `<CR><LF>` |

  The CR the hook half depends on sits on line 3, a key `read_green_file` reads. Line 1 stays for
  `read_tag_lines` only. Observed by AC1 and AC3.
- **S2** — The hook half's assertion. The arm's cut-and-source compare (`@57bfdf31:827-831`) stays one
  assertion: `rgf_sha`, the `rec_sha` the cut `read_green_file` sets over S1's record, equals `$rgf_b`
  exactly. Where the CR reaches the strip, that one compare fails on a kept CR, the value then being
  forty-one bytes, and on every node it fails on a kept first line, the value then being two lines. Its
  failure line names `rec_sha` and prints the value with each newline as `|` and each CR as `\r`. The
  arm asserts nothing about `GREEN` on the hook side. Observed by AC1 and AC2.
- **S3** — The local-hook half. The arm's `read_tag_lines` compare (`@57bfdf31:832-837`) calls the
  reader `tools/run-gates/verdict_backends.py#read_local_verdict` goes through, over S1's record opened
  with `newline=""`, and prints `repr` of both `verdict` and `sha`, so a CR kept in either value
  survives the arm's `tr -d '\r'`, which is there for the CR-LF Python's stdout writes on Windows. It
  asserts `'GREEN'` and `'` + forty `b` characters + `'`. Observed by AC3.
- **S4** — Each staged break names the variable its plant reaches. The comment above the arm names
  `rec_sha` and the two breaks that turn S2 red: a `read_green_file` whose `sha` read lacks
  ` sub(/\r$/, "", v);`, and one whose `sha` read is `$1=="sha"{print $2}`, printing every match. Its
  WHAT THIS DOES NOT CHECK clause names, in place of the CR this unit now plants, that Git for Windows
  gawk and bash `$(...)` lose the CR before the strip sees it, so the first break reds only where both
  hand it on (§8 F3). This spec's §7 New arm line records both breaks, and neither is staged
  on the `verdict` line; unit 65, CLOSED, keeps its own. Observed by AC2.

## 3. Non-goals (OUT)

- The CR strip and the last-wins rule inside `read_green_file`, landed by unit 65's S15; this unit only
  makes the arm able to see them. The read form that lets a CR reach that strip on Git for Windows is
  `TOOL-dWitnessedBar-69` S1's, and until it lands S4's first break cannot go red on a Windows node
  (§4 Evidence, §8 F3).
- A `verdict` read in `read_green_file`. Nothing in this build designs one. The hook reads `verdict` in
  `.githooks/pre-push#read_bar_file`, for the tree verdict `check_tree_verdict` grades, and from a run
  dir's `verdict` file (`.githooks/pre-push@86500358:2657`, `:2695`); neither reads this record. The
  no-read assertion and the CRLF `fingerprint` line are `TOOL-dWitnessedBar-67`'s item for ids 1 and 12.
- The `key-no-tab` plant's record in `tools/run-gates/verdict_backends.py`, whose `sha` lines stay
  LF-ended. `read_local_verdict` reads it through `read_text`, whose newline translation drops a CR
  before `read_tag_lines` sees it, and re-siting the record onto a plant is `TOOL-dWitnessedBar-68`'s.
- The report's left-shift text, a checklist entry for "a staged red whose plant sits on input the
  changed code never reads". No clause of this build names that gate. S4's named variable is the
  regression this unit builds.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-65` — S15's CR strip and last-wins rule in `read_green_file`, and AC12's arm in `run-gates.gov.test.sh`, whose hook half this unit replants on `sha` (id 6)
- **hands-off** `TOOL-dWitnessedBar-67` — the CRLF `fingerprint` line beside this record and the assertion that the hook reads no `verdict` key, which the minors batch adds for the same AC12 defect at MEDIUM (ids 1 and 12, report item M1)
- **hands-off** `TOOL-dWitnessedBar-68` — the record, re-sited onto unit 56's `clean` plant at the path the local-hook reader reads, and AC3, regraded on the state the CLI prints (id 1 of the round-1 spec audit of units 66 and 67, item H1)
- **hands-off** `TOOL-dWitnessedBar-70` — the CR-reach canary that proves S1's CR reaches `read_green_file` before S2's compare counts, the staged reds of §7 recorded with their failing line from a Windows node, and §4 Evidence's "keeps a CR" answered in this unit's ledger (id 10, item B1)
- **hands-off** `TOOL-dWitnessedBar-73` — the every-key record beside S1, the gov canary guard naming `.githooks/pre-push`, the floor stated as a number, and the held-leg statement for §7 (ids 5, 12, 15 and 22 of the round-1 spec audit of units 66 and 67)

## 4. Design

### Evidence

- `read_green_file` sets `rec_sha`, `rec_fp`, `rec_blob`, `rec_man`, `rec_st`, `rec_reused` and
  `rec_reused_cache` from the keys `sha`, `fingerprint`, `manifest_blob`, `manifest`, `selftests`,
  `reused` and `reused_cache` (`.githooks/pre-push#read_green_file`).
  `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push | grep -c verdict` prints 0 at `9fde76576`
  (PINNED 2026-11-21).
- At HEAD each read is `awk -F'\t' '$1=="<key>"{v=$2} END{sub(/\r$/, "", v); print v}'`, unit 65 S15 as
  landed at `139d6fea1`: the last match wins and one CR is stripped. The hook calls `read_green_file`
  once, for its full-green record (`.githooks/pre-push@86500358:2074`).
- The arm at HEAD ends only its `verdict` line in CR-LF (`tools/run-gates/run-gates.gov.test.sh@57bfdf31:826`),
  and its two compares, at `:830` and `:836`, count one assertion each.
- A probe on this node (GNU Awk 5.4.0, bash 5.3.9 `x86_64-pc-cygwin`, git 2.54.0.windows.1) over S1's
  record, each scratch cut differing from HEAD's in one line, PINNED 2026-11-21: HEAD's cut set
  `rec_sha` to forty `b`; a cut with ` sub(/\r$/, "", v);` dropped from the `sha` read also gave 40
  bytes and matched; a cut whose `sha` read is `{print $2}` gave 81 bytes (PINNED 2026-11-21, this probe) and failed. gawk reads in text
  mode and drops the CR before an LF, and `x=$(printf 'abc\r\n')` leaves 3 bytes (PINNED 2026-11-21, this probe), so even
  `awk -v BINMODE=1`, which gives `length(v)` 41, loses the CR at `$(...)`. Unit 70 §4 Evidence measured
  the same.
- So over S1's record the arm is GREEN at HEAD, and its RED is staged (S4), never a base state.
- This unit adds and removes no `a=$((a+1))`, so `FLOOR_ASSERTIONS` does not move; the suite file owns
  its value.

### Inventory

Minted: nothing. No function, constant, plant, flag or file. The record of S1 is fixture data inside an
existing arm. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, one step after `TOOL-dWitnessedBar-65` (order 37, CLOSED at `139d6fea1`). Units 67,
68, 69 and 70 build at order 39; 67, 68 and 70 extend this arm, and 69 S1 moves the hook's read into a
bash loop that lets S4's first break go red on Git for Windows.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`

### Alternatives rejected

- **Add a `rec_verdict` read to `read_green_file`** so the original AC12 could pass. That changes what
  the pre-push hook reads to decide a push, with no design and no consumer behind it.
- **Plant the CR on `fingerprint` instead of `sha`.** It reaches the strip as well. `sha` is chosen
  because S1 already needs two `sha` lines for last-wins, so one key carries both breaks and one
  compare grades both. The `fingerprint` line goes to unit 67 as a second key.
- **Keep the CR on `verdict` and assert the hook ignores it.** An assertion that a value is absent
  cannot go red when the strip is removed, which is the finding.
- **Pull unit 69 S1's loop into this unit** so the CR reaches the strip on this node. It is a second
  mechanism and that unit's own scope (§8 F3).

## 5. Production-readiness checklist

- security — no new write path. The arm writes one record in the suite's scratch directory.
- perf / scale — one sourced function and one Python read over a three-line file.
- error / empty / loading states — N/A: the arm reads a fixture it writes itself.
- observability — the failure line names `rec_sha` and prints its value with CR made visible.
- risks — a later rewrite that renames `rec_sha` reds the arm loudly, at its sourced call.
- testing — AC1 to AC3 by fixture and scratch copy. The arm under §7 at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When the arm sources `read_green_file`, cut by `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push`
  from the built tree, and calls it on S1's record, `rec_sha` is forty `b` characters and
  `printf %s "$rec_sha" | wc -c` prints 40. `grep -c $'\r$'` over the record prints 2.
  `grep -n 'rec_sha' tools/run-gates/run-gates.gov.test.sh` names the arm's failure line.
  Red when: `read_green_file` keeps the first of two `sha` lines, keeps a CR that reached it on `sha`,
  or the record carries its CR on `verdict` alone.
  fixture: S1's record, written by the arm in the suite's scratch directory.
  figure: 40 and 2 are PINNED by S1's table.
- **AC2** — When the arm's hook-half compare runs with `ROOT` at a scratch tree holding a copy of
  `.githooks/pre-push` whose `read_green_file` `sha` read is `awk -F'\t' '$1=="sha"{print $2}'`, it
  fails, and its failure line names `rec_sha` and prints two values joined by `|`. Against a copy
  whose `sha` read lacks ` sub(/\r$/, "", v);`, it fails naming `rec_sha` with a trailing `\r` on a node
  whose awk and bash `$(...)` keep the CR; on Git for Windows it stays green, and §8 F3 says where that
  half is observed. Each copy differs from HEAD's cut in one line, counted by `diff` lines opening `>`.
  Red when: the arm stays green against the print-every-match copy, or its failure line does not name
  `rec_sha`.
  fixture: scratch copies of `.githooks/pre-push` under `%TEMP%/<short-name>`.
- **AC3** — When the arm's `read_tag_lines` compare reads S1's record, it prints `'GREEN'` and `'` +
  forty `b` characters + `'`, the same `sha` value AC1 reads.
  `grep -n 'repr(r.get("sha"))' tools/run-gates/run-gates.gov.test.sh` names the arm.
  Red when: `read_tag_lines` keeps the CR on `verdict` or `sha`, or the two readers part on `sha`.

## 7. Gates

`run-gates gov canary` · `pre-push self-test` · `memory hygiene`

`pre-push self-test` is named because S2 sources the hook's own `read_green_file`, and that leg
observes the hook's existing reads.

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC2 AC3 · the hook half replanted on the second `sha` line, staged red on a scratch copy of `.githooks/pre-push` by restoring print-every-match to `read_green_file`'s `sha` read, and, on a node whose awk and bash keep the CR, by removing its CR strip (§8 F3) · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 65 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which key carries the hook half's CR (id 6)?** Options: (a) the second `sha` line; (b) a
  `fingerprint` line; (c) a new `verdict` read in `read_green_file`. (c) adds an undesigned read to the
  push decision, which widens what the hook reads beyond this unit's tier; veto 3 discards it. (a) and
  (b) both reach the strip. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3. It grades the CR
  strip and last-wins with one compare on one variable, so it leaves the fewest open questions, and (b)
  is kept as unit 67's second key.
  widens: none · relaxes: none

- **F3 — Where is S4's CR-strip break observed red, when Git for Windows drops the CR before the
  strip?** §4 Evidence's probe leaves `rec_sha` at forty `b` with the strip removed on this node, and
  `remote-ci` runs on Windows. Options: (a) this unit's close stages the print-every-match break red on
  any node, and the CR-strip break red on a node whose awk and bash `$(...)` keep the CR; with no such
  node, this unit's ledger records that half beside AC2 as owed to `TOOL-dWitnessedBar-70` S3, which
  stages both of this unit's breaks on a Windows node after unit 69 S1; (b) pull unit 69 S1's bash
  loop into this unit; (c) order this unit after unit 69. (b) changes the read form §3 leaves to units
  65 and 69, so veto 1 discards it. (c) needs units 67, 68 and 70, which consume from this unit at
  order 39, reordered, and this re-ground touches no spec but this one. RESOLVED (agent, 2026-11-21,
  delegated): (a), the one survivor. It keeps S1 to S4 whole and opens no question unit 70 S3 does not
  already own.
  widens: none · relaxes: AC2's CR-strip half on a Windows node, observed at unit 70's close

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 64 and 65, id 6
  (HIGH, item H1).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-68, TOOL-dWitnessedBar-70 and TOOL-dWitnessedBar-73, promoted by the
  round-1 spec audit of units 66 and 67; nothing else moved.
- rev-3 · 2026-11-21 · §1 to §8 · §10 · S1 to S4 · AC1 to AC3 · re-grounded over unit 65 as landed
  at `139d6fea1`, per 2026-11-19-prompt-TOOL-dWitnessedBar-66-reground-brief: S1 to S3 name the arm's
  record, compares and `read_tag_lines` half as built; §4 Evidence replaces "keeps a CR" with this
  node's probe; AC2's CR-strip half is observed where the CR survives (§8 F3); the floor does not move;
  citations move to `path#symbol` or blob-pinned lines.

## 10. Reuse audit

The seam is unit 65's AC12 arm in `tools/run-gates/run-gates.gov.test.sh`, extended in place, and the
cut-and-source idiom unit 65 already names for both hook and runner readers
(`awk '/^read_green_file\(\)/,/^}/'`). `python tools/codebase-map/reuse_lookup.py "strip a trailing carriage return from a key value record line"`
ranked `key`, `keys`, `records` and `build_records` first at `9fde76576`. None of them reads the green
stamp, so no existing seam fits beyond the arm named above. The runner's own strip is `${_rk_v%$'\r'}`
in `tools/run-gates/run-gates.sh#read_record_keys`, which unit 65 S14 keeps and this unit does not
touch.

Recall terms used: `python tools/memory-recall/query.py "how does a staged red reach the variable the plant changes in the hook's green-stamp reader" --terms "staged red plant read_green_file rec_sha CR strip last key wins verdict record hook adoption"`
