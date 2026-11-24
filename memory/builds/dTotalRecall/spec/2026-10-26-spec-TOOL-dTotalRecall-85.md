# TOOL-dTotalRecall-85 — unit 76's S1 to S4 reads of units 55, 56 and 57 are made again at verified revisions, each count printed beside the sha it was read at

**Status:** CLOSED · rev-3 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 36 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-85-deviation-851.md](../build/2026-10-26-build-TOOL-dTotalRecall-85-deviation-851.md) | deviation | — |
| [2026-11-24-build-TOOL-dTotalRecall-85-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dTotalRecall-85-1-acceptance-ledger.md) | log | — |
| [2026-11-24-build-TOOL-dTotalRecall-85-1-builder-return.md](../build/2026-11-24-build-TOOL-dTotalRecall-85-1-builder-return.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-85-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-85-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-85-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-85-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-85-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-85-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-87 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-86 TOOL-dTotalRecall-88 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 71 to 76
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md`)
confirmed finding **id 11 at HIGH**, graded medium by its finder and high by the skeptic, whose
grade binds. It shares item **H3** with id 38, which is `TOOL-dTotalRecall-86`.

`TOOL-dTotalRecall-76` (order 35), as audited, read five amendment strings over the specs of units 55,
56 and 57 at each unit's `pass(T)^` by its blob probe, its S1 to S4, observed by its AC1. The probe
took its revision from the environment and never verified it. An empty revision reads the index blob,
exit 0, and a bare `^` reads nothing, exit 0. A row whose unit had no resolvable pass commit would have
read either a silent 0, which writes a fabricated deviation, or the text after later amendments, which
certifies a build from text the unit never saw.

Re-grounded at `aec378661`: unit 76 rev-4 resolves each revision before it reads it, so the fall-through
is gone from the text its pass builds from, and its S3 reads unit 55's criterion as unit 55's re-ground
re-worded it. What stands is the independent check the finding asks for. This unit makes those five
reads again at the parents the driver's own pass rule resolves, through `TOOL-dTotalRecall-81`'s guarded
read. It proves each string can print a 0 and a 1 over independent texts, and makes each decision unit
76's S1 to S4 owed from the verified count. It repairs `TOOL-dTotalRecall-76`, at step 36, one above
that unit's order.

## 2. Scope (IN)

- **S1** — The five reads. Each numbered string of §4's table is counted over its target spec at
  `"$(pass_of T)^"` by `read_at`. The ledger prints each sha and count beside the sha and count unit
  76's AC1 line recorded for that row. §4's table carries one more line, the control, which no decision
  reads. Observed by AC1.
- **S2** — The liveness. Each string is counted over its target spec at `653bed738` and over an
  independent text that holds it, the amending spec at the sha §4's table names, printing the pinned 0
  and the pinned count. Observed by AC1.
- **S3** — The decisions. A numbered row whose verified count is 0 owes a deviation record of its target
  unit naming the string, as unit 76's S1 to S4 state. It is written only where §4's write-once read
  lists none naming that string. Each of the five reads 1 at `aec378661` (§4), over blobs that cannot
  move, so none is owed. A row whose verified sha or count differs from unit 76's recorded one is named
  in a deviation record of `TOOL-dTotalRecall-76`, one record for every such row of this unit, written
  once. Observed by AC2.

## 3. Non-goals (OUT)

- Unit 76's S5 and S6 reads: `TOOL-dTotalRecall-86`, which shares item H3.
- Unit 76's AC1 greps at the tip, the two `git grep` commands its S3 names. They read code and not a
  revision, so the defect does not reach them.
- The read itself: `TOOL-dTotalRecall-81`.
- Editing a landed spec, frozen once its unit builds.

### Edges

- **consumes-from** `TOOL-dTotalRecall-76` — its S1 to S4 and its AC1 ledger line, whose five counts this unit re-reads at verified revisions
- **consumes-from** `TOOL-dTotalRecall-81` — `pass_of` and `read_at`, the guarded read every row runs through
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S3 writes through
- **hands-off** `TOOL-dTotalRecall-92` — its records and its write-once guard, which that batch scans for a malformed, duplicated or uncommitted record (the round-1 audit of units 77 to 88, ids 12, 15, 24, 26)

## 4. Design

### The rows

| Row | T | String | Count at `pass(T)^` | Liveness: target at `653bed738`, then the text that holds it |
|---|---|---|---|---|
| 1 | 55 | `holding only the build-folder rows this unit moves` | 1 | 0, and 1 over spec 61 at `653bed738` |
| 2 | 55 | `git grep -n "CAUSE_WRITER_KEPT\|KEPT_PINNED\|KEPT_OUTSIDE" -- tools` | 1 | 0, and 2 over spec 76 at `aec378661` |
| control | 55 | `git grep -n CAUSE_WRITER_KEPT -- tools` | 0 | 0, and 1 over spec 61 at `653bed738` |
| 3 | 56 | ``**hands-off** `TOOL-dTotalRecall-57` `` | 1 | 0, and 1 over spec 61 at `653bed738` |
| 4 | 56 | `git grep -n ALIAS_COMPARE_KEPT -- tools` | 1 | 0, and 1 over spec 61 at `653bed738` |
| 5 | 57 | ``**consumes-from** `TOOL-dTotalRecall-56` `` | 1 | 0, and 3 over spec 72 at `af814dba8` |

A numbered row wants at least 1. Row 2's string is unit 55's criterion as its re-ground re-worded it,
which unit 76's S3 reads. The control is unit 61's older spelling of it, which rev-2 made a row. Its 0
at `pass(55)^` is no departure, since the re-worded command greps for the name unit 61 added and two
more. It shows the read answering 0 at the revision the rows are read at. Spec 61 holds no line of row
2's spelling and spec 76 does not exist at `653bed738`, so row 2's liveness is the text that quotes it.

PINNED 2026-11-24 at `aec378661` with unit 81's `read_at`, every count of the table. The passes
`pass_of` printed and their parents, PINNED by the same run:

| T | `pass_of T` | The sha `read_at` printed |
|---|---|---|
| 55 | `5b5895a493d4a47a0be4e417b1c5550cde92b001` | `b9f735339150e39be311a1b75d9cbc755ecc8aa7` |
| 56 | `798f98fc1fa2c4af9feb68f8324f11c9d5339c8f` | `1e9a5ebabf0dfda59fc2e9ce55e263c23aa4e0f9` |
| 57 | `5ff76c2e273faa46b4490bde40ecb26478205de9` | `c736ff00f780c01f19115b40ef84efc8b7009590` |

The liveness counts of rows 1 and 3 to 5 and of the control are the ones measured 2026-10-26 at
`af814dba8`. A liveness count of 1 or more over the holding text is the reading S2 needs.

### The reads

```bash
# run from the repository root, with unit 81 §4's first bash fence sourced from a file under $SCRATCH;
# one strings file per target
cat > "$SCRATCH/s85-55.txt" <<'STRINGS'
holding only the build-folder rows this unit moves
git grep -n "CAUSE_WRITER_KEPT\|KEPT_PINNED\|KEPT_OUTSIDE" -- tools
git grep -n CAUSE_WRITER_KEPT -- tools
STRINGS
cat > "$SCRATCH/s85-56.txt" <<'STRINGS'
**hands-off** `TOOL-dTotalRecall-57`
git grep -n ALIAS_COMPARE_KEPT -- tools
STRINGS
cat > "$SCRATCH/s85-57.txt" <<'STRINGS'
**consumes-from** `TOOL-dTotalRecall-56`
STRINGS
for T in 55 56 57; do P=$(pass_of "$T") && read_at "$P^" "$T" "$SCRATCH/s85-$T.txt" || echo "red row $T $P"; done
live() { echo "live spec $2"; read_at "$1" "$2" "$SCRATCH/s85-$3.txt"; }   # revision · spec · strings file
for T in 55 56 57; do live 653bed738 "$T" "$T"; done
live 653bed738 61 55; live 653bed738 61 56; live aec378661 76 55; live af814dba8 72 57
```

`pass_of` prints its red line on stdout, so the substitution captures it and the `red row` line repeats
it. Run with 999 for T, the row read prints `red row 999 red 999 no pass commit` (DERIVED 2026-11-24). The
`live` line names the spec, since a count line carries its sha and string alone. Two of the `live` reads
print lines the table does not pin: spec 61 prints 0 for row 2's string, and spec 76 prints 2 for row 1's
and the control's (PINNED 2026-11-24, these reads).

A red line for a row stops that row's decision, and the ledger names the row as unresolved. It is
never read as a 0.

### The deviation records

Each is written by `python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit <id> --title <text>`,
which refuses a missing `--title` or required field (`tools/memory-tree/build_records.py#write_new_record`). It
takes one `--field` per required name of the deviation entry of `tools/memory-tree/build_records.py#KINDS`:

- `Departs from` `TOOL-dTotalRecall-76@rev-<n> [§6 AC1]`, or for a 0 row `TOOL-dTotalRecall-<T>@rev-<n>`,
  the rev that unit's header holds at its pass.
- `Hand-off` `spec-to-code`; `Cause` `review finding`; `Risk` `loosening`, as the recorded figure
  certifies a reading the blob does not hold.
- `Before` the recorded figure; `After` the verified sha and count; `Reason` the read that gave the
  recorded figure.
- `Approver` opening with the role `author`, under the chain's `author-recorded` value
  (`tools/memory-tree/deviation_join.py#HOST_APPROVAL`, `PLAY-dClosedLoop-4`).
- `Follow-through` `ask TOOL-dTotalRecall-27`; `Caused-by` `TOOL-dTotalRecall-85`.
- `Evidence` each row named with its string verbatim, the verified sha and count, the figure it departs
  from and item H3 of the round-7 audit (`2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1`).

The write-once read, for a 0 row of unit T and for unit 76's record:

```bash
git grep --untracked -F -l -e '<the row string>' -- 'memory/builds/dTotalRecall/build/*-TOOL-dTotalRecall-<T>-deviation-*.md'
git grep --untracked -F -l -e '- **Caused-by:** TOOL-dTotalRecall-85' -- 'memory/builds/dTotalRecall/build/*-TOOL-dTotalRecall-76-deviation-*.md'
```

A record is written only where it lists nothing. It reads the working tree, so a record not yet committed
counts, and its pathspec reads the unit's deviation records alone, so a file that quotes a Serves line
never counts. At `aec378661` it lists nothing for the five strings and for unit 76; with
`dTotalRecall [roster]` for the string it lists the roster record of each of units 55, 56 and 57, and with
`PLAY-dClosedLoop-2` for the cause `2026-10-26-build-TOOL-dTotalRecall-76-deviation-761` (DERIVED
2026-11-24), so it is seen both ways. `TOOL-dTotalRecall-86` shares the step and may write its own record
of unit 76, which the cause tells apart.

### Why order 36

Unit 76 records its S1 to S4 counts at step 35. Step 36 is the first step after it.

### Inventory

Minted: nothing in code; deviation records where §4's rows read 0 or differ from unit 76's.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger and the records of S3)

### Alternatives rejected

- **Rely on unit 76 rev-4's own resolve.** Its revisions are literals its spec names, never resolved by
  the driver's pass rule, and item H3 asks the counts be read again. Unit 81's guarded read already
  exists, so a second verifier would be a copy.
- **Read row 2 in unit 61's older spelling alone, as rev-2 did.** It prints 0 at `pass(55)^` and S3 would
  write a false deviation of unit 55.
- **Liveness copies built by deleting the string.** They read 0 by construction (item M1, id 2).
  Specs 55, 56 and 57 at `653bed738` and the holding specs are independent texts.

## 5. Production-readiness checklist

- security — no surface.
- perf / scale — three pass-commit walks and ten blob reads, 13 s with the red reads (DERIVED 2026-11-24, node a).
- error / empty / loading states — an unresolved pass or an absent blob is a red line for its row,
  never a 0. Once a run-state rotation moves a unit's dispatch row out of `RUN.md`, `pass_of` is that
  red, as unit 81 §5 states.
- observability — the ledger names each row's sha, count and unit 76's recorded count.
- risks — unit 76's counts are prose in its ledger, quoted by eye.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's reads run at this pass's base, each row prints the sha §4 pins for its T, equal to
  `git rev-parse "$(pass_of T)^"`, with the count §4 pins, the control among them, or a `red row` line
  naming T. The liveness reads print the values of §4's last column. In the same shell, the row read
  with 999 for T prints `red row 999 red 999 no pass commit`.
  Red when: a row prints a count with no sha or at another revision, a liveness read prints otherwise,
  or an unresolved pass prints nothing.
  figure: the shas and counts are PINNED in §4, measured 2026-11-24; the pass's own lines are DERIVED
  by it.
- **AC2** — When `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-85" -- memory/builds/dTotalRecall/build`
  runs after the pass, the ledger it names has an AC2 line naming each row's verified sha and count
  beside unit 76's, quoted with its ledger's file name; unit 76's sha is twelve digits long and is
  compared as a prefix. For a row that read 0, and for unit 76 where a row differs, §4's write-once read
  prints exactly one file; where neither holds, it prints nothing.
  Red when: a 0 row has no record, a row has two, a differing row is not named in a record of unit 76,
  or a record is written that no row owes.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is this pass's reads and their liveness reads.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 71 to 76, id 11
  (HIGH, item H3, shared with id 38).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-92, each the other end of an edge a
  unit the round-1 spec audit of units 77 to 88 promoted wrote; nothing else moved.
- rev-3 · 2026-11-24 · §1 S1 S2 S3 §3 §4 §5 AC1 AC2 §10 · re-grounded at `aec378661` per
  `2026-11-24-prompt-TOOL-dTotalRecall-85-reground-brief`, over unit 76 rev-4: the Goal's environment
  revision is history; row 2 is unit 55's re-worded criterion, its older spelling kept as a control that
  reads 0; the passes and every count are pinned; an unresolved pass prints its cause; the records spell
  every field `tools/memory-tree/build_records.py#KINDS` requires, with `--title`; the write-once read is keyed on the unit's
  deviation records and the string, untracked files included, in place of a grep the roster records answer.

## 10. Reuse audit

The seams, re-read at `aec378661`, are `TOOL-dTotalRecall-81` rev-4's guarded read, CLOSED, and the
record door `gov_record.py new deviation` of `TOOL-dTotalRecall-2`, CLOSED.
`python tools/codebase-map/reuse_lookup.py "read a file at a git revision and refuse an unresolved revision"`
ranked `read_git_output` and `read_blobs_at` as SEAM candidates, the two unit 81 calls; re-run 2026-11-24
it ranks `read_text`, `run_git` and their name-stem neighbours first. The recall
query below found this audit's fix text,
unit 74's §5 claim that `git show` refuses an empty revision, which the audit refuted and unit 74 rev-3
dropped, and the `aUnmannedHelm` review that guarded a base by `rev-parse --verify` before reading it. No
existing seam fits beyond them. `tools/memory-tree/id_grammar.py#read_kept_reason` and the build-folder
walks of the two censuses are no seam here: this unit reads no marker and no registry.

Recall terms used: `python tools/memory-recall/query.py "how does a probe read a spec at a pass commit and refuse an unresolved revision instead of reading the index" --terms "pass commit rev-parse verify git show index blob empty revision pass_commit read_blobs_at guarded probe"`
