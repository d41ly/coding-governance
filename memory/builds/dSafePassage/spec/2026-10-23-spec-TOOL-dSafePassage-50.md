# TOOL-dSafePassage-50 — the spec audit of units 43 to 46, its five minors on TOOL-46: the lander arm placed after the scan it reads, its locator cited by content, and one owner for the cutoff paragraph

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 12 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-50-deviation-96.md](../build/2026-10-23-build-TOOL-dSafePassage-50-deviation-96.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-prompt-TOOL-dSafePassage-50-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-50-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-47-48-49-50-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-47-48-49-50-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 43 to 46
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-43-44-45-46-spec-audit-round1.md`)
exited CONVERGED with 25 minors, which split into two disjoint write sets by BUILD-METHOD M6's
clauses. `TOOL-dSafePassage-49` batches the 20 whose writes are the step module. This unit batches the
other five, 1 MEDIUM and 4 LOW. Each is named by its report id and is its own scope item, including
where the report merged ids into one item.

All five land on TOOL-dSafePassage-46, so this unit repairs that unit and builds one above it, at
order 12. Where a minor would bite TOOL-dSafePassage-46's pass, that unit's own §3 hands-off bullet to
this unit names it, so that pass may build it.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| D-10 | MEDIUM | 30 | S1 |
| D-12 | LOW | 5 | S5 |
| D-15 | LOW | 8, 13, 17 | S2, S3, S4 |

The report refuted none of these five and left none unverified. The skeptic re-graded id 5 from
medium to low. D-15's fourth id, 25, cites TOOL-dSafePassage-43, -44 and -45 and is
`TOOL-dSafePassage-49`'s S14.

## 2. Scope (IN)

### The arm's place and its locator (D-10, D-15)

- **S1** — id 30. TOOL-dSafePassage-46 S2's derived-count arm in `tools/push-main.test.sh` sits after
  the suite's top-level scan, `_mt_rc=$(cd "$HERE" && for d in */; ...`, because the arm reads the
  variable that line sets. An arm above it reads `_mt_rc` unset, takes its `skip —` branch on every
  run, and every gate stays green. In gov's own tree, which holds the memory-tree kit beside the
  lander, the arm prints its `ok` line and no `skip —` line. Observed by AC1.
- **S2** — id 8. TOOL-dSafePassage-46's pin `tools/push-main.test.sh:872`, in S2, §4 "The arm's
  locator" and §10, is read as the scan cited by its content, `_mt_rc=$(cd "$HERE" && for d in */`.
  That line was 873 at 2828457d, and 872 is the closing `}` of `write_unit_spec`. NOT OBSERVED: a
  reading of a citation, which no code carries.
- **S3** — id 13. TOOL-dSafePassage-46 S2's "a sibling of `$HERE`" is read as "a subdirectory of
  `$HERE` holding `routed_commits.py`". `$HERE` is the lander's own directory
  (`tools/push-main.test.sh:17`, `HERE=$(cd "$(dirname "$0")" && pwd)`), and the scan lists its
  children. NOT OBSERVED: a reading of a description, which no code carries.
- **S4** — id 17. TOOL-dSafePassage-46 §10's sentence that `resolve_kit_dir` "installs into
  `tools/push-main.test.sh` already" is read as follows. `resolve_kit_dir` is the lander's own
  function (`tools/push-main.sh:670`), the suite only stubs it inside arm 27
  (`tools/push-main.test.sh:916`), and so S2 reuses the suite's top-level scan rather than that stub.
  NOT OBSERVED: a reading of a reuse record, which no code carries.

### One owner for the cutoff paragraph (D-12)

- **S5** — id 5. TOOL-dSafePassage-46 alone writes the `SPEC_AC_ORDER_CUTOFF` paragraph and the
  example row into `tools/memory-tree/SPEC-TEMPLATE.template.md`, `memory/TEMPLATE-SPEC.md` and
  `tools/memory-tree/.memory-tree.conf.example`. TOOL-dSafePassage-46 S3's sentence reading
  TOOL-dSafePassage-41's §4 Files touched with those three files is void. TOOL-dSafePassage-41's §3
  hands-off bullet to TOOL-dSafePassage-46 is amended by this disposal to say that TOOL-41's pass
  writes none of them. So TOOL-dSafePassage-46's AC3 is red before its pass, and no pass appends a
  second paragraph. Observed by AC2.

## 3. Non-goals (OUT)

- Every step-module minor: `TOOL-dSafePassage-49`.
- Both highs: `TOOL-dSafePassage-47` and `TOOL-dSafePassage-48`.
- The report's left-shift gates: a spec-token join resolving every `file:line` pin at HEAD, and one
  refusing a path that two units' readings both assign.
- Rewriting a built spec. An item that corrects a built spec's text states the reading here, and the
  amended TOOL-dSafePassage-41 bullet is the edge S5's finding asks the disposal to write.

### Edges

- **consumes-from** `TOOL-dSafePassage-46` — S2's arm and its locator, S3's three files and AC3, which S1 places, S2 to S4 cite and S5 gives one owner; without them there is no arm to place
- **hands-off** `TOOL-dSafePassage-52` — S1 read with the `set -u` abort a misplaced arm causes; the arm placed by content after the 28-32 block's `fi` and before the final line, with exactly one `_mt_rc=` scan; any template repair made in `tools/memory-tree/SPEC-TEMPLATE.template.md` and rendered; S4's `resolve_kit_dir` read as the shared primitive; and the Rollout read as disjoint from each of TOOL-dSafePassage-47 and -48, not all three, findings 7, 11, 16, 15, 17, 6 and 20 of the spec audit of units 47 to 50

## 4. Design

### The arm's place

| Line in `tools/push-main.test.sh` | Sets or reads `_mt_rc` | Where TOOL-dSafePassage-46 S2's arm may sit |
|---|---|---|
| the scan, `_mt_rc=$(cd "$HERE" && for d in */; ...` | sets it | after this line |
| arm 26's guard, the next line | reads it | unchanged |
| the derived-count arm | reads it | below the scan, appended after the last arm as the suite's arms are |

The scan was at line 873 and the suite's last arm ended at 1046 at 2828457d (PINNED; the probe of
AC1 re-derives both).

### The paragraph's owner

| Unit | Order | Writes the three files |
|---|---|---|
| `TOOL-dSafePassage-41` | 8 | none |
| `TOOL-dSafePassage-46` | 11 | the paragraph in the template and its rendered copy, and the blank example row |
| this unit | 12 | none unless AC2 finds a duplicate or a gap, which it then removes or fills |

### Inventory

Minted: none. No function, constant, conf key, gate leg, plant or policy key.

### Migration

None.

### Rollout

Live at landing. It builds at order 12, one above TOOL-dSafePassage-46 (order 11), whose arm and
paragraph it repairs. Its write set is `tools/push-main.test.sh` and the three files of S5. That set
does not meet `TOOL-dSafePassage-47`'s or `TOOL-dSafePassage-48`'s, which are the step module, its
self-test and its help page. Neither side writes a file the other reads as a contract or an acceptance
input, and neither writes a shared mutable record, so the three passes at order 12 are disjoint (M6).

### Files touched (estimate)

- `tools/push-main.test.sh`
- `tools/memory-tree/SPEC-TEMPLATE.template.md`
- `memory/TEMPLATE-SPEC.md`
- `tools/memory-tree/.memory-tree.conf.example`

### Alternatives rejected

- **Building S3 of TOOL-dSafePassage-46 in TOOL-dSafePassage-41's pass (S5).** The report's second
  option. It moves three files into an order-8 write set, and leaves TOOL-dSafePassage-46's AC3 needing
  a rewrite to an exactly-one count; the first option needs neither.
- **A second locator inside the arm (S1).** The arm would re-run the scan arm 26 already runs, the
  copy TOOL-dSafePassage-46 §10 rejects.

## 5. Production-readiness checklist

- security: N/A — a test arm's place, citations and documentation ownership.
- perf / scale: unchanged.
- error / empty / loading states: the arm's `skip —` line stays the honest outcome where no
  memory-tree kit sits beside the lander, and S1 makes it unreachable in gov's own tree.
- observability: the suite prints the arm's `ok` line in gov's own tree.
- risks: none beyond TOOL-dSafePassage-46's.
- testing: AC1's placement probe, AC2's counts, and the arm of §7.
- migration: none.
- user docs: N/A — `memory/TEMPLATE-SPEC.md` is the documentation S5 assigns, and no `help/` page
  covers the lander's suite.

## 6. Acceptance criteria

- **AC1** — When `grep -n -e '^_mt_rc=' -e 'check-arms.py' tools/push-main.test.sh` runs, the first line
  spelling `check-arms.py` has a greater line number than the `_mt_rc=` line.
  Red when: the arm's load sits above the scan, so it reads `_mt_rc` unset and skips on every run.
- **AC2** — When `grep -c 'SPEC_AC_ORDER_CUTOFF'` runs over
  `tools/memory-tree/SPEC-TEMPLATE.template.md` and over `memory/TEMPLATE-SPEC.md`, each prints `1`,
  the one line of the one paragraph TOOL-dSafePassage-46 §4 "The template paragraph" words to name the
  key once;
  and `grep -c '^SPEC_AC_ORDER_CUTOFF=""' tools/memory-tree/.memory-tree.conf.example` prints `1`.
  Red when: a second pass appended a duplicate paragraph or row, or no pass wrote one.

## 7. Gates

`push-main self-test` · `foreign-prefix parity (every self-test at three prefixes)` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `memory-hygiene self-test` · `spec tokens (a spec's own names resolve)`

New arm: tools/push-main.test.sh · covers AC1 · the derived-count arm run in gov's own tree, where it must print its `ok` line and no `skip —` line, its failing case staged by an arm copy moved above the `_mt_rc=` scan, under which the `ok` line goes missing · none

What the check does not cover: an arm that reads a variable set by any line other than the scan, and
a paragraph whose wording differs from the opening AC2 counts.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the batch of the spec audit of units 43 to 46's 1 MEDIUM and 4
  LOW findings on TOOL-dSafePassage-46, one scope item per raw id.
- rev-2 · 2026-10-23 · §3 · the Edges gain the end this unit owes the promotion `TOOL-dSafePassage-52` of the spec audit of units 47 to 50, written by the disposal stage; no other section moved.

## 10. Reuse audit

The seams extended are the lander suite's top-level kit scan and its skip-line convention in
`tools/push-main.test.sh`, and the template's cutoff paragraphs, which TOOL-dSafePassage-46 writes.
`python tools/codebase-map/reuse_lookup.py "place a test arm after the scan that sets the variable it reads"`
ranked `read`, `read_text`, `arm` (`tools/lib/lib-selftest.sh` among its homes) and `scan`,
name-token matches; none orders a shell arm against a top-level assignment, so no existing seam fits
beyond the scan the suite already runs. This unit re-read the suite as well: the only
`resolve_kit_dir` there is arm 27's stub (`tools/push-main.test.sh:916`).

Recall terms used: `python tools/memory-recall/query.py "how a spec audit finding on a submodule walk or a refused executor key is promoted and its reading carried to the faulted unit" --terms "spec audit promoted reading hands-off submodule walk repository shape refused executor sendemail identity"`
