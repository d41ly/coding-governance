# TOOL-dSafePassage-102 — ask 85's two red legs, by the owner's ruling: five fork ceilings raised to their measured counts, three evidence how texts respelled through the prefix token

**Status:** DEFERRED · rev-1 · 2026-11-01 · node a · Tier-2 · base 4f7ba0a30 · streams tooling · order 16 · closes TOOL-dSafePassage-85

**Derived:** TOOL-dSafePassage-85

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-prompt-TOOL-dSafePassage-102-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-102-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-102-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-102-build-brief.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-102-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-102-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The close's merge bar at `5fe2c7e34` reds two of 75 legs, and both are the records of the ask
TOOL-dSafePassage-85. The spawn budget reds on five rows of `memory/project/fork-ceilings.txt`. The
install-prefix leg reds on three rows of `tools/run-gates/ceiling-evidence.txt`. The owner ruled the
ask on 2026-11-01. This unit carries that ruling into the two records. It raises each of the five
ceilings to its measured count, and it respells each of the three `--how` texts through the
`<prefix>/` token. Nothing else in either file moves.

## 2. Scope (IN)

- **S1 — the five fork ceilings.** In `memory/project/fork-ceilings.txt`, the rows `run-gates-1leg`,
  `run-gates-2leg`, `memory-hygiene`, `manifest-check` and `check-wiring` each take a ceiling equal
  to the count the bar measured at `5fe2c7e34`, per §4 "The five rows". Each row's reason field keeps
  its text and gains one clause. That clause names the owner's ruling on ask TOOL-dSafePassage-85 and
  the cause the ask states. The `id`, `bash`, `base`, `setup` and `command` fields do not change.
  Observed by AC1, AC2 and AC3.
- **S2 — the three evidence how texts.** In `tools/run-gates/ceiling-evidence.txt`, lines 115, 134
  and 146 each change one word in their sixth field, the `--how` text. That word is a kit path
  spelled under the tool root, and it is respelled under the `<prefix>/` prose token, per §4 "The
  three rows". The leg, seconds, readings, node and date fields do not change. Observed by AC4, AC5
  and AC6.
- **S3 — no other record moves.** No other row of either file changes, and no comment line changes.
  Observed by AC3 and AC6.

## 3. Non-goals (OUT)

- A new verb on `tools/run-gates/derive-ceilings.py`, such as a respelling verb. Ask 85 lists that
  as an owner option, and the owner did not choose it.
- Any change to `tools/gate-lint/fork-count.sh`, to its counter, or to the resolver probe that
  TOOL-dSafePassage-11 inlined. Reshaping the probe was the other option ask 85 lists, and the owner
  did not choose it.
- Any change to `base` on any row. The file's header says it never moves (fork-ceilings.txt line 14).
- Retiring any of the three evidence rows. §4 "The ruling, and the one departure" gives the reason.
- Any edit to a CLOSED spec, a gate, its checker or its manifest row.
- A `RUN.md` row, and a help page. No page under `help/` names either record.

### Edges

- **consumes-from** external — the main loop's runs of the two legs' own checkers and of the
  ceiling checker at this unit's build commit. Scratch-guard row G1 refuses a leg's argv to a role
  whose allowlist does not name that leg (`tools/hooks/README.md`, the G1 row). Without those runs,
  AC2, AC4 and AC5 have no observation.
- **hands-off** external — the landing of dSafePassage with TOOL-dSafePassage-61 deferred, which the
  owner's ruling names as the step after this one.

## 4. Design

Every line cited here was read at `4f7ba0a30`, the HEAD this spec was written at, on 2026-11-01 on
node a. The bar log is the close's run at `5fe2c7e34`, copied to
`C:/Users/daily-agent/AppData/Local/Temp/dsp86-logs/bar-5fe2c7e34.log`. Between `5fe2c7e34` and
`4f7ba0a30`, `git diff --stat` names one file, the build's `RUN.md`, so every finding in the log
holds at HEAD.

### The ruling, and the one departure

The owner answered the hand-off's question "How should ask 85's two red legs be resolved before
landing?" by choosing **Raise the ceilings**. Its message reads: "Rule ask 85: raise the five fork
ceilings with evidence and retire the three ceiling-evidence lines, then land dSafePassage with 61
deferred." §9 quotes it as the brief records it.

The first half is carried as written. The second half departs from the word "retire". The run
decided ask 85's second record under gate-guard's rule, which takes the option that makes no
measured observable worse. It respells the three rows and does not retire them. That decision is
recorded in the spec brief,
`memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-102-spec-brief.md`, and this
unit carries it.

The reason is what a retired row would leave. The ceiling checker reads a leg with no evidence row
as unbacked (`tools/run-gates/derive-ceilings.py` lines 654-659), and it reports that state without
failing. So retiring the three rows would turn nothing red. It would leave the ceilings of
`routed commits name a specced unit`, `spec tokens (a spec's own names resolve)` and `upgrade-walk`
backed by nothing. Those ceilings were raised on the 253 s, 366 s and 7177 s readings the rows
carry. A respelled row clears install-prefix and keeps every reading. Ask 85 itself lists
"hand-respell the three how texts" as one of the owner's options
(`memory/builds/dSafePassage/BACKLOG.md` line 8).

### The five rows

The counter reds a count above its ceiling, and it reds a ceiling more than its margin above its
count. The margin is `FC_COUNT * 5 / 100`, floored at 3 (`tools/gate-lint/fork-count.sh` line 162).
A ceiling equal to its count trips neither branch. The counts below are PINNED: the bar measured
each one at `5fe2c7e34` on node a under bash 5.3 (log lines 43, 55, 67, 79 and 91).

| Row | Line | Ceiling now | Measured at `5fe2c7e34` | Ceiling after | Margin | `base`, unchanged |
|---|---|---|---|---|---|---|
| `run-gates-1leg` | 17 | 55 | 56 | 56 | 3 | 72 |
| `run-gates-2leg` | 18 | 57 | 58 | 58 | 3 | 97 |
| `memory-hygiene` | 19 | 189 | 190 | 190 | 9 | 219 |
| `manifest-check` | 20 | 74 | 76 | 76 | 3 | 108 |
| `check-wiring` | 21 | 44 | 45 | 45 | 3 | 55 |

The two rows the bar printed `ok`, `unattended-status` and `check-unattended`, do not change.

Each reason field keeps its text and gains one clause, appended after a `; `. The clause follows the
form the file's own raised rows use (line 17), and reads, for `run-gates-1leg`:

```
raised 55 -> 56 by the owner's ruling on ask TOOL-dSafePassage-85, 2026-11-01, measured 56 by the close's bar at 5fe2c7e34 on node a under bash 5.3: TOOL-dSafePassage-11's inlined resolver probe makes the counter see a fork the old form already spent, the real process count unchanged
```

The other four rows substitute their own two numbers. The clause holds no tab, because a row is
tab-separated with the reason as its seventh field (fork-ceilings.txt line 4), and the counter
reads that field as the row's remainder and never grades it (`tools/gate-lint/fork-count.sh`
line 147).

The cause is ask 85's diagnosis (`memory/builds/dSafePassage/BACKLOG.md` line 8), and this spec
does not re-derive it. That the counted fork is one the old form already spent, with the real
process count unchanged, is UNVERIFIED here. The reason text attributes it to the ask.

**The build re-measures before it edits.** The builder runs the leg's checker once with `--only`
for each of the five rows at the build's parent, before any edit. A count that differs from the
table means the tree moved under the ruling. Then the build stops and hands the count back to the
main loop. It does not write a different number in the owner's name.

### The three rows

Each `--how` text holds exactly one kit path under the tool root, measured by counting `tools/` in
each sixth field at `4f7ba0a30`. That one word is respelled, and nothing else in the row moves.

| Line | Leg | Word now | Word after |
|---|---|---|---|
| 115 | `routed commits name a specced unit` | `tools/memory-tree/routed_commits.py` | `<prefix>/memory-tree/routed_commits.py` |
| 134 | `spec tokens (a spec's own names resolve)` | `tools/check-spec-tokens.py` | `<prefix>/check-spec-tokens.py` |
| 146 | `upgrade-walk` | `tools/govkit/upgrade_walk.py,` | `<prefix>/govkit/upgrade_walk.py,` |

`<prefix>/` is one of the two prose tokens the leg drains (`tools/check-install-prefix.sh` lines
52-53 and 398). Its rule 3 skips a kit segment whose lead ends in a drained token (line 463). Its
rule 2 needs a literal `tools/` lead (line 386), which the respelled words no longer carry. The file
header already spells the derive-ceilings command through the same token (ceiling-evidence.txt
line 3), so the respelling matches the file's own style.

The leg printed the three hits as one kit-path spelling each, with kits `memory-tree`, `(loose)` and
`govkit` (log lines 110-112). That none of the three respelled words counts is DERIVED from the
rules above and was not run, because G1 refuses the leg's argv to this role.

**The header's ban on hand edits.** The file's header says not to hand-edit it (line 4). This edit
is the owner's ruling, carried by hand, because the tool has no path that respells an observed row.
`--write --observed` refuses a reading at or under the stored maximum and writes nothing
(derive-ceilings.py lines 581-586). A `--reset` before it would drop the row and write it afresh
with today's date (line 587), and it would delete run records outside the tree. Both break S2's "no
other field".

**The respelling survives later writes.** `cmd_write` holds a stored row unchanged when no new
reading beats it (derive-ceilings.py line 533), and it carries forward any row the run measured
nothing for (line 562). So a later `--write` keeps the respelled text until a higher reading
replaces the whole row with a `runner` row.

**The ceiling checker's verdict does not move.** It reads the source field only to tell an
out-of-band row from a runner row (lines 679 and 706). The three sources stay out-of-band, and no
value moves. With the margin at a 120 s floor and a 1.0 fraction (`tools/run-gates/ceiling-margin.txt`),
each leg's ceiling still clears its reading: 510 against 253, 740 against 366, and 14360 against
7177 (`tools/gate-legs.json`). The checker's out-of-band line prints each source verbatim (line
708), so after S2 it prints the respelled words, which AC5 reads.

### What it does not cover

- Whether a raised ceiling holds on a later run. The `run-gates-2leg` row's own history records a
  polled reading that varied before TOOL-aSparedSpawn-4 (fork-ceilings.txt line 18). A ceiling set
  equal to its count has no headroom, by the file's rule, so a reading one higher reds again.
- Any bash version other than 5.3. Every row declares 5.3, and a run under another bash prints the
  counter's NOT MEASURED shape (fork-count.sh line 186).
- Whether ask 85's diagnosis of the extra fork is right. That is the ask's claim, and S1 records it
  as the ask's.

### Inventory

Minted: nothing. No file, function, flag, conf key, gate leg, row id or receipt field.

### Migration

None.

### Rollout

Live at landing, at order 16, before the build lands with TOOL-dSafePassage-61 deferred.

### Files touched (estimate)

- `memory/project/fork-ceilings.txt` — S1.
- `tools/run-gates/ceiling-evidence.txt` — S2.
- The unit's acceptance ledger, under the build's own build-records folder.

### Alternatives rejected

- **Retiring the three evidence rows, the ruling's own word.** It leaves three ceilings unbacked by
  the readings they were raised on (§4 "The ruling, and the one departure").
- **A respelling verb on derive-ceilings.** It is new tool surface for three rows, and §3 rules it
  out.
- **`--write --reset` and then `--write --observed` per row.** It moves the date field and deletes
  run records outside the tree (§4 "The three rows").
- **Each ceiling set with headroom above its count.** Any value above the count by more than the
  margin reds as stale (fork-count.sh line 162). A value inside the margin but above the count is a
  number nobody measured. The brief asks for the count.
- **Reshaping the resolver probe so the counter sees no extra fork.** The owner did not choose it,
  and §3 rules it out.

## 5. Production-readiness checklist

- security: N/A — two tracked text records change, with no write path, surface or permission.
- perf / scale: N/A — no code changes. The real process count is unchanged, by ask 85's diagnosis.
- error / empty / loading states: N/A — no code path changes. A malformed row would be refused by
  the counter's parser by line (fork-count.sh line 126), and AC2 would read that refusal.
- observability: the ceiling checker's out-of-band line prints the respelled how texts.
- risks: a ceiling equal to its count has no headroom, so one more fork reds the leg again (§4 "What
  it does not cover"). A hand-edited evidence row could carry a typo, so AC6 compares the diff word
  by word.
- testing: AC1 to AC6.
- migration: N/A — no data or state changes.
- user docs: N/A — no page under `help/` names either record, checked with `git grep` on 2026-11-01.

## 6. Acceptance criteria

- **AC1** — When `grep -v '^#' memory/project/fork-ceilings.txt | cut -f1,3,4` runs from the
  repository root at the build commit, it prints seven lines. In order, each holds the row id, its
  ceiling and its base: `unattended-status` 47 57, `check-unattended` 684 709, `run-gates-1leg` 56
  72, `run-gates-2leg` 58 97, `memory-hygiene` 190 219, `manifest-check` 76 108 and `check-wiring`
  45 55, tab-separated.
  Red when: a ceiling stays below its count. At `5fe2c7e34` the spawn budget leg printed, among its
  lines:
  ```
  fork-count: RED run-gates-1leg · measured 56 · ceiling 55 · delta +1 · base 72 — the sites the most forked subshells first traced at:
  fork-count: RED run-gates-2leg · measured 58 · ceiling 57 · delta +1 · base 97 — the sites the most forked subshells first traced at:
  fork-count: RED memory-hygiene · measured 190 · ceiling 189 · delta +1 · base 219 — the sites the most forked subshells first traced at:
  fork-count: RED manifest-check · measured 76 · ceiling 74 · delta +2 · base 108 — the sites the most forked subshells first traced at:
  fork-count: RED check-wiring · measured 45 · ceiling 44 · delta +1 · base 55 — the sites the most forked subshells first traced at:
  ```
  figure: every number is PINNED from the bar at `5fe2c7e34`.
- **AC2** — When `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt .` runs from the
  repository root at the build commit under bash 5.3, it exits 0. It prints `fork-count: ok` for
  each of the seven rows, and its summary reads `fork-count: 7 passed · 0 red · 0 skipped — a skipped
  row is not a pass`.
  Red when: a measured count is above its new ceiling, or more than its margin below it. At
  `5fe2c7e34` the leg printed the five RED lines AC1 quotes, then
  `fork-count: 2 passed · 5 red · 0 skipped — a skipped row is not a pass`, and exited 1.
  fixture: a bash 5.3, as on node a. Another bash prints NOT MEASURED, which is not this
  observation.
  permission: scratch-guard row G1 refuses this argv to a role whose allowlist does not name the
  spawn budget leg.
- **AC3** — When
  `git diff -U0 4f7ba0a30 -- memory/project/fork-ceilings.txt | grep -E '^[-+][a-z]' | cut -c2- | cut -f1,2,4-6 | sort | uniq -u`
  runs from the repository root at the build commit, it prints nothing. When
  `git diff -U0 4f7ba0a30 -- memory/project/fork-ceilings.txt | grep -E '^\+[a-z]' | cut -f7 | grep -c -F 'TOOL-dSafePassage-85'`
  runs there, it prints `5`, and the same pipeline counting `TOOL-dSafePassage-11` prints `5`.
  Red when: a `base`, `setup`, `command`, `bash` or `id` field moves, or a sixth row changes. A
  moved `base` makes the first pipeline print that row twice, once per side. That was measured on a
  scratch copy on 2026-11-01, with check-wiring's base moved from 55 to 54. A reason without the
  ruling makes the count print less than `5`. The rows S1 moves are the five the spawn budget leg
  refused at `5fe2c7e34`, whose summary line read
  `fork-count: 2 passed · 5 red · 0 skipped — a skipped row is not a pass`.
  fixture: no other commit between `4f7ba0a30` and the build commit edits the file, read with
  `git log` at observation time.
- **AC4** — When `bash tools/check-install-prefix.sh` runs from the repository root at the build
  commit, it exits 0, and no line it prints names `tools/run-gates/ceiling-evidence.txt`.
  Red when: a respelled word keeps a literal tool-root lead. At `5fe2c7e34` the leg printed the
  three hits of lines 115, 134 and 146, then
  `install-prefix: RED — 450 tracked file(s) graded, 7 render(s) left out as matching their template, 3 kit-path spelling(s) on 3 line(s)`,
  and exited 1.
  permission: scratch-guard row G1 refuses this argv to a role whose allowlist does not name the
  install-prefix leg.
- **AC5** — When `python tools/run-gates/derive-ceilings.py --check` runs from the repository root at
  the build commit, it exits 0. Its out-of-band line opens
  `derive-ceilings: 7 ceiling(s) backed by a reading taken OUTSIDE the runner`, the count the main
  loop's run at `6d6fe589b` printed, as TOOL-dSafePassage-80's ledger records. That line names the
  three legs with their readings unchanged, 253.0 s, 366.0 s and 7177.0 s, and spells each
  respelled word from §4 "The three rows".
  Red when: a row loses its value or its out-of-band source, or a reading moves. A retired row reads
  as unbacked, which the checker reports without failing (derive-ceilings.py lines 654-659), so the
  count falls to 6 and the line names that leg nowhere. That is derived and not run. The rows this
  criterion reads are the three that the install-prefix leg refused at `5fe2c7e34`, in the lines
  AC6 quotes.
  permission: scratch-guard row G1 refuses the checker to a role agent.
- **AC6** — When
  `git diff -U0 --word-diff=porcelain 4f7ba0a30 -- tools/run-gates/ceiling-evidence.txt | grep -E '^[-+][^-+]'`
  runs from the repository root at the build commit, it prints exactly six lines in three pairs.
  Each pair is one removed word and one added word, the added word being the removed word with its
  leading tool-root segment replaced by the prefix token, as §4 "The three rows" tabulates. When
  `git diff -U0 4f7ba0a30 -- tools/run-gates/ceiling-evidence.txt | grep -E '^[-+][a-z]' | cut -c2- | cut -f1-5 | sort | uniq -u`
  runs there, it prints nothing.
  Red when: any other word in the file moves, such as a date or a seconds value. Then the first
  pipeline prints more than six lines, and the second prints the moved row on each side. Both
  pipelines were run on a scratch copy carrying S2's edit on 2026-11-01. The first printed the six
  lines §4 tabulates, and the second printed nothing. At `5fe2c7e34` the install-prefix leg refused
  the three rows as they stand, printing (log lines 106-113, each row's text cut by the leg):
  ```
  install-prefix: a tracked file spells a kit path. `govkit apply` writes these bytes verbatim,
  install-prefix: so at a target installed at any other prefix they resolve to nothing. Derive the
  install-prefix: path from the file's own location, route a sibling kit through resolve_kit_dir,
  install-prefix: or spell it through a drained token. This is a pure ban: there is no waiver.
    tools/run-gates/ceiling-evidence.txt:115  memory-tree  routed commits name a specced unit	253.0	1	a	2026-10-28	python3 tools/memory-tree/routed_c
    tools/run-gates/ceiling-evidence.txt:134  (loose)  spec tokens (a spec's own names resolve)	366.0	1	a	2026-10-28	python tools/check-spec-toke
    tools/run-gates/ceiling-evidence.txt:146  govkit  upgrade-walk	7177.0	1	a	2026-10-28	python tools/govkit/upgrade_walk.py, whole leg, timed b
  install-prefix: RED — 450 tracked file(s) graded, 7 render(s) left out as matching their template, 3 kit-path spelling(s) on 3 line(s)
  ```
  fixture: no other commit between `4f7ba0a30` and the build commit edits the file, as for AC3.

## 7. Gates

`spawn budget (forks per hot entrypoint)` · `install-prefix (shipped surface)` · `leg ceilings clear their evidenced maximum` · `memory hygiene` · `recall floor` · `recall floor arms`

The first two legs red at `5fe2c7e34`, and this unit clears them. `leg ceilings clear their
evidenced maximum` reads the evidence file S2 edits. `memory hygiene` grades this spec and its
ledger. `recall floor` and `recall floor arms` are the legs whose `memory/` guard
`memory/project/fork-ceilings.txt` trips. That guard is carried by two legs, under the checker's
broad floor of five (`tools/check-spec-tokens.py` line 368). The evidence file trips only broad
guards, the tool root's and the gate kit's, carried by 12 and 7 legs. That was read from
`tools/gate-legs.json` on 2026-11-01. This unit adds or moves no suite arm.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-102-1-spec-writer.md` and
  its brief `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-102-spec-brief.md`.
  The owner's ruling, in chat on 2026-11-01, answering the hand-off's question "How should ask 85's
  two red legs be resolved before landing?", chose **Raise the ceilings**, whose message reads:
  "Rule ask 85: raise the five fork ceilings with evidence and retire the three ceiling-evidence
  lines, then land dSafePassage with 61 deferred." The run then decided the second record under
  gate-guard's rule, taking the option that makes no measured observable worse. The three
  `tools/run-gates/ceiling-evidence.txt` rows are RESPELLED, not retired, because retiring them
  would leave the upgrade-walk, routed-commits and spec-tokens ceilings unbacked by the 7177 s, 253 s
  and 366 s readings they were raised on. Respelling their `--how` text through the `<prefix>/`
  token clears install-prefix and keeps every reading, and ask 85 lists hand-respelling as an owner
  option. §4 "The ruling, and the one departure" states the departure. Every cited line was read at
  `4f7ba0a30`.

## 10. Reuse audit

No existing seam fits a change to two tracked records, so this unit adds no code and extends none.
The seams it uses are the records' own forms. In `memory/project/fork-ceilings.txt` it uses the
raised-row clause the file's rows 17 and 18 already write. In `tools/run-gates/ceiling-evidence.txt`
it uses the `<prefix>/` prose token, which `tools/check-install-prefix.sh` drains (line 398) and
which `derive-ceilings.py` writes into the same file's header (line 594). It does not touch
`tools/govkit/`, `tools/lib/` or `tools/push-main.sh`, the seams the task names, because the
remedy is a record edit that reaches none of them.

`python tools/codebase-map/reuse_lookup.py "respell a kit path in a tracked record through the prefix token, and raise a fork ceiling row"`
ranked `resolve_kit_dir` as a SEAM, with fan-in 44 and 103 installs, and `resolve_prefix_token` as
a SEAM, with fan-in 11 and 12 installs. Neither fits. Both resolve a path in code at run time, and no
reader resolves a `--how` text: the ceiling checker prints it verbatim (derive-ceilings.py line 708).
`tools/lib/resolve_prefix_token.py` also resolves the brace token `{prefix}`, not the prose token
`<prefix>/` that a record spells. No candidate edits a ceilings row. The recall probe ranked the ask
TOOL-dSafePassage-85 first. It also ranked TOOL-dSafePassage-82's spec, whose §9 names the three
rows that `derive-ceilings.py` cannot respell, and TOOL-aSparedSpawn-8, the unit that landed the
fork ceilings file and its shrink-only rule.

Recall terms used: `python tools/memory-recall/query.py "raise a shrink-only fork ceiling to its measured count by owner ruling, and respell an out-of-band ceiling evidence how text through the prefix token" --terms "fork-ceilings spawn budget fork-count ceiling-evidence install-prefix drained prefix derive-ceilings observed how shrink-only"`
