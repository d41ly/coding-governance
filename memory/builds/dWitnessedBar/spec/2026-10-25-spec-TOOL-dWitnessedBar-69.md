# TOOL-dWitnessedBar-69 — both readers of the green record read it with a line read that keeps every byte, so their one-CR strip is the only thing that removes a CR

**Status:** OPEN · rev-4 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 39 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md) | research | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md) | research | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |
| [2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 66 and 67
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-66-spec-audit-round1.md`)
confirmed finding **id 19 at HIGH**, report item **H3**. No other id shares that item. Its defect
also underlies blocker id 10 (item B1, `TOOL-dWitnessedBar-70`) and id 20 (item H4,
`TOOL-dWitnessedBar-72`), which each take their own unit.

On the bar's platform the I/O layer removes the CR before either reader's strip sees it. Git for
Windows gawk reads its input in text mode and drops the CR before an LF, and bash `$(...)` drops a
trailing CR-LF. The hook reads each key with `rec_<x>=$(awk ...)` (`.githooks/pre-push:1354-1368`),
so deleting the CR strip `TOOL-dWitnessedBar-65` S15 adds changes nothing there. Python's default
text-mode open translates `\r\n`, and a lone `\r` too, so the local-hook reader's strip is unreachable
on every platform. Every `remote-ci` job is `runs-on: windows-latest`.

This unit changes how both readers read the record, so the bytes reach the strip: the hook through
one bash loop that reads whole lines, the local-hook reader through an open that keeps line endings.
It repairs `TOOL-dWitnessedBar-66`, whose arm grades that strip, and builds at order 39.

## 2. Scope (IN)

- **S1** — The hook's `read_green_file` reads the record in one loop,
  `while IFS= read -r _rg_l || [ -n "$_rg_l" ]; do ... done 2>/dev/null < "$1"`, in place of its seven
  `$(awk ...)` reads and of unit 65 S15's `END`-print awk form. For each line:
  - a line holding no TAB is skipped, as unit 63 S19 rules;
  - the key is the text before the first TAB, `${_rg_l%%$'\t'*}`, and the value the text after it,
    `${_rg_l#*$'\t'}`, as unit 62 S24 rules;
  - the value is stripped of one trailing CR, `${_rg_v%$'\r'}`, as unit 65 S15 rules;
  - a `case` on the key assigns the value to the one of the seven `rec_*` variables that key names,
    so a later line of a repeated key overwrites an earlier one, as unit 65 S15 rules.

  `_rg_l`, `_rg_k` and `_rg_v` are `local`. An unreadable file leaves all seven empty, as today.
  Observed by AC1, AC2 and AC3.
- **S2** — The local-hook reader `read_local_verdict` in `tools/run-gates/verdict_backends.py` opens
  the per-tree record with `newline=''`, splits its text on `'\n'` only, skips a line whose
  `partition('\t')` separator is empty, and strips one trailing `'\r'` from each value. A lone CR
  inside a value stays data. Observed by AC4.

## 3. Non-goals (OUT)

- Which keys the hook reads, and what predicates 2 to 9 do with them. The seven variables and their
  empty-when-absent contract are unchanged.
- The runner's `read_record_keys` (`tools/run-gates/run-gates.sh:2387-2397`), which unit 65 S14 and
  unit 67 S11 own. Its `IFS=$'\t'` split is not this unit's (§4 Alternatives rejected).
- The suite arm that proves the CR reaches the hook's strip on every run, which is
  `TOOL-dWitnessedBar-70`'s. The record planting every key is `TOOL-dWitnessedBar-73` S9's.
- The report's left-shift text: a checklist entry for a CR plant read through awk or `$(...)` on Git
  for Windows, and a selftest grepping the reader's form. AC3's grep is this unit's own probe; no
  clause of this build names that gate.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-65` — S15's one-CR strip and last-wins rule for both record readers, which S1 and S2 move onto reads that keep the CR (id 19)
- **hands-off** `TOOL-dWitnessedBar-70` — the CR-reach canary in the AC12 arm, which sources S1's loop with its strip deleted on every run (id 10)
- **hands-off** `TOOL-dWitnessedBar-72` — the `fingerprint` line's CR, which reaches `rec_fp` through S1's `fingerprint` case (id 20)
- **hands-off** `TOOL-dWitnessedBar-73` — the every-key record, whose key list is derived from S1's `case` labels (id 22)
- **hands-off** `TOOL-dWitnessedBar-74` — S1's `sha) rec_sha=$_rg_v` case assignment, which the liveness variant edits to `${_rg_v%?}` (id 10 of the round-1 spec audit of units 68 to 73, item H1)
- **hands-off** `TOOL-dWitnessedBar-76` — S1's `fingerprint) rec_fp=$_rg_v` case assignment, which the `fingerprint` liveness variant edits (id 9, item H2)
- **hands-off** `TOOL-dWitnessedBar-78` — S1's rules carried to `read_bar_file` and the inherited green and held by an arm, S2's open given its encoding and its error outcome, and the ledger lines for AC2 and AC3 (ids 6, 12, 18, 21, 22, 26, 27)
- **hands-off** `TOOL-dWitnessedBar-84` — S1's `<key>)` case arm in `read_green_file`, whose quoted spelling the liveness loop's edit admits (id 6 of the round-1 spec audit of units 74 to 78)
- **hands-off** `TOOL-dWitnessedBar-91` — S1's `read_green_file`, whose `sha)` arm unit 91 counts in 90 AC2's quoted clones and whose two resets it holds at the unedited count (id 1 of the round-1 spec audit of unit 90, item H1)
- **hands-off** `TOOL-dWitnessedBar-92` — S1's unquoted `sha) rec_sha=$_rg_v` arm, on which unit 92 reads the anchored count's baseline of 0 (id 6 of the round-1 spec audit of unit 90)

## 4. Design

### Evidence

Probed on this node at `df0a656d`: GNU Awk 5.4.0, GNU bash 5.3.9 (`x86_64-pc-cygwin`), git
2.54.0.windows.1. The record held `verdict<TAB>GREEN<CR><LF>`, `sha<TAB>` forty `a` `<LF>`, `sha<TAB>`
forty `b` `<CR><LF>` and `fingerprint<TAB>` forty `c` `<CR><LF>`.

- `awk -F'\t' '$1=="sha"{print length($2)}'` printed 40 and 40. The base read
  `x=$(awk -F'\t' '$1=="sha"{print $2}' rec)` gave 81 bytes, forty `a`, an LF and forty `b`, with no CR.
- `while IFS=$'\t' read -r k v` kept the CR: the last `sha` value was 41 bytes, and 40 after
  `${v%$'\r'}`.
- The same loop split `note<TAB>a<TAB>` into a value `a`, and `x<TAB><TAB>y` into `y`. TAB is IFS
  whitespace, so a trailing TAB is trimmed and a run of TABs collapses. Reading the whole line with
  `IFS= read -r` and splitting by parameter expansion gave `a<TAB>` and `<TAB>y`, the values unit 62
  S24's "the line after its first TAB" defines.
- A prototype of S1's loop gave `rec_sha` 40 bytes and `rec_fp` 40 bytes. With `%$'\r'` deleted from it
  by `sed 's/%[$].[\]r.}/}/'`, which changed exactly one line, both were 41 bytes ending in `\r`.
- Python's `open(p).read()` ended `...c\n`, and `open(p, newline='').read()` ended `...c\r\n`.
  `memory/gotchas/text-mode-read-eats-a-bare-cr.md` records that the default mode also turns a lone CR
  into a newline.
- `grep -n runs-on .github/workflows/remote-ci.yml` prints four `windows-latest` lines.
- The hook calls `read_green_file` once, at `.githooks/pre-push:1668`, and sources nothing from
  `tools/` (its one `.` line, `:657`, sources the gate env file).

### Inventory

Minted: the locals `_rg_l`, `_rg_k` and `_rg_v` inside `read_green_file`. No function, constant, plant,
flag or file. Naming cells: none apply.

### Migration

None: no stored data changes. Every record the runner writes holds one TAB-separated key per line, so
S1 and S2 read each such record to the same seven values the base reads give.

### Rollout

Live at landing, at order 39, after `TOOL-dWitnessedBar-66` (38). The tie at order 39 is recorded as
`TOOL-dWitnessedBar-68` §4 Rollout records it. `TOOL-dWitnessedBar-70` consumes this unit and sorts
after it within the tie, and the dispatch edge refusal holds 70 until this unit is CLOSED
(`tools/unattended/unattended.sh:13691-13760`).

### Files touched (estimate)

- `.githooks/pre-push`
- `tools/run-gates/verdict_backends.py`

### Alternatives rejected

- **`while IFS=$'\t' read -r k v`, the report's form.** It keeps the CR but trims a trailing TAB and
  collapses a run of TABs (§4 Evidence), so the hook would part from unit 62 S24's value rule and
  from the local-hook reader on a value holding a TAB.
- **Keep awk and stage the CR mid-field, the report's option (a).** The plant then reaches the strip
  only if unit 65 S15 strips the stored value rather than `$0`, and `$(...)` still eats a trailing
  CR-LF, so the arm would grade a fixture shape rather than the read.
- **`BINMODE=3` on each awk call.** It keeps the CR through awk, but `$(...)` still drops a trailing
  CR-LF in MSYS bash, and the variable is gawk-only.

## 5. Production-readiness checklist

- security — the hook's push decision reads the same seven values from every record the runner
  writes. A record with a CR now has it removed by the strip rather than by the platform.
- perf / scale — one read of the file replaces seven awk processes, each a fork.
- error / empty / loading states — an absent file returns early as today, and an unreadable one leaves
  every variable empty, its error discarded as `2>/dev/null` discards awk's today.
- observability — none changes: the hook's refusal messages name the predicates, not the read.
- risks — a key line with no TAB was read by awk as a key with an empty value; S1 skips it, as unit 63
  S19 already rules for the awk form.
- testing — AC1 to AC4 by probe and scratch copy. The arms of units 70 and 73 re-observe S1 at the
  close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a probe sources `read_green_file`, cut by `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push`,
  and calls it on a record holding `sha<TAB>` forty `a` `<LF>`, `sha<TAB>` forty `b` `<CR><LF>`,
  `manifest<TAB>x<TAB><LF>`, a bare `fingerprint<LF>` and a final `selftests<TAB>on` with no LF,
  `rec_sha` is forty `b` characters, `printf %s "$rec_man" | od -c` shows `x \t`, `rec_fp` is empty
  and `rec_st` is `on`.
  Red when: the read trims a value's trailing TAB, sets a variable from a line with no TAB, keeps the
  first of a repeated key, or drops an unterminated last line.
  fixture: a record the probe writes under `%TEMP%/<short-name>`.
- **AC2** — When the same probe sources the cut function after `sed 's/%[$].[\]r.}/}/'`, and
  `diff` of the two copies counts exactly one changed line, `printf %s "$rec_sha" | wc -c` prints 41
  and `printf %s "$rec_sha" | tail -c1 | od -c` shows `\r`, on this Windows node.
  Red when: the CR never reaches the strip, so deleting it leaves `rec_sha` at 40 bytes, as the base
  `$(awk ...)` reads do.
- **AC3** — When `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push` is piped to `grep -c 'awk'`, it
  prints 0, and piped to `grep -c 'IFS= read -r'`, it prints 1.
  Red when: any key of the record is read through a command substitution again.
- **AC4** — When `read --backend local-hook` runs over `TOOL-dWitnessedBar-68` S1's fixture, it prints
  `· GREEN ·`. Against a scratch copy of `verdict_backends.py` with the `'\r'` removal
  deleted, the same read does not print `· GREEN ·`. `grep -n "newline=''" verdict_backends.py`, run in
  `tools/run-gates/`, names the record's open.
  Red when: the open uses the default newline mode, so deleting the strip leaves the read `GREEN`.

## 7. Gates

`measure-legs selftest` · `pre-push self-test` · `run-gates gov canary` · `memory hygiene`

`measure-legs selftest` is owed because its guard names `.githooks/pre-push`. `pre-push self-test`
observes the hook's adoption over its own plants. All three suite legs are held unless the main loop
sets GATE_SELFTESTS at the close (`tools/run-gates/run-gates.sh:3129-3131`), which
`SELFTESTS_OWED_PATHS="tools/"` does (`.unattended.conf:40`).

No arm is added here. At the close the main loop stages this unit's two breaks, the hook strip deleted
and the Python strip deleted, against the AC12 arm that `TOOL-dWitnessedBar-70` and
`TOOL-dWitnessedBar-68` extend, and records each red with its failing line.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 66 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which bash read form carries the hook's record to its strip (id 19)?** Options: (a) whole-line
  `IFS= read -r` split by parameter expansion; (b) `IFS=$'\t' read -r k v`, the report's form;
  (c) awk under `BINMODE=3`. (b) trims a trailing TAB and collapses TAB runs, which fails unit 62 S24's
  value rule; veto 1 discards it. (c) still loses the CR to `$(...)` (§4 Alternatives rejected), so
  AC2 fails; veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the one
  survivor.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 66 and 67, id 19
  (HIGH, item H3).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-74, TOOL-dWitnessedBar-76 and TOOL-dWitnessedBar-78,
  promoted by the round-1 spec audit of units 68 to 73; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-84, promoted by the round-1 spec audit of units 74 to 78; nothing else
  moved.
- rev-4 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-91 and TOOL-dWitnessedBar-92, promoted by the round-1 spec audit of
  unit 90; nothing else moved.

## 10. Reuse audit

The seam is the runner's own record loop, `read_record_keys` (`tools/run-gates/run-gates.sh:2387-2397`),
whose `|| [ -n ... ]` guard and `${...%$'\r'}` strip S1 follows. It is not called, because the hook
sources nothing from `tools/` and its `IFS=$'\t'` split trims TABs (§4 Evidence).
`python tools/codebase-map/reuse_lookup.py "read a tab separated key value record file line by line keeping carriage return"`
ranked `read`, `read_text`, `key`, `keys`, `records`, `read_conf` and `read_journal`. None of them is
reachable from the hook, so no existing seam fits beyond the loop named above.

Recall terms used: `python tools/memory-recall/query.py "how does the green record reader keep a CR so the strip is exercised on Git for Windows" --terms "read_green_file rec_sha CR strip CRLF gawk text mode command substitution read -r canary staged red"`
