# TOOL-dCalibratedLens-40 — an isolated failure's `<why>` folded to one line with no field separator, and a reading the writer would refuse read as `unread · refused value`

**Status:** DEFERRED · rev-2 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 4 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-40-deviation-401.md](../build/2026-11-02-build-TOOL-dCalibratedLens-40-deviation-401.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md) | journal | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-41 |
| [2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md](../reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 31, HIGH, item H7 of the round-2 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`). Unit 27 isolates every reading
and proposer so a failure becomes `<name>: unread · <why>`, with `<why>` the raw exception class and
message. The record writer still refuses a value carrying a line break, so a multi-line message, which
the tree already raises with git's stderr, trips the walk's pre-render and exits it 1 on every wake:
nothing is filed, but the period never records and the lease is handed over each time. A `<why>`
holding ` · ` mis-splits under the last-separator rule, so the line reads `unread · <part>` and a
reader testing for `unread` misses it. And unit 21 S4 keeps the writer's refusal for a reading that
answers a multi-line value, against its own §5. This unit makes the isolation boundary's own output
always writable and parsable, and proves it with the two inputs that broke it. It repairs
`TOOL-dCalibratedLens-27`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in the sibling specs' text. Unit 3's
  id-49 bullet (rev-3, r2 id 31) and unit 27 S1 (rev-2, id 31): at the isolation boundary `<why>` is
  `<exception class>: <message>` with every line break made a space and every ` · ` made `, `, the
  fold `render_shape_line` applies to a field value (`tools/roles/handoff.py:708-719`); and a reading
  whose answered value or source carries a line break is written `<name>: unread · refused value`,
  never handed to the writer. For a reading that answers a list of pairs the refusal is per entry:
  the entry carrying the break is written `<name>: unread · refused value` in its place in list order,
  and the reading's other entries are written as answered, so a caller filtering by name still reads
  every good entry; a scalar answer is the one-entry case (round-3 id 32, unit 3's r3 id-32 bullet and
  unit 21 S4 at rev-3). Unit 21 S4 and its fourth criterion (rev-2, r2 id 31) read that line for a
  multi-line answer, so units 21 and 27 agree. Observed by AC1, AC2 and AC3.
- **S2** — The proof, a case `reader-raises-multiline` of unit 27's `reader-raises` plant in
  `tools/loop/loop_review.py`: one planted `METRICS` reader raises `RuntimeError` whose message is
  `git failed\nfatal: bad · ref`, and a second answers a value carrying a line break. `run --dry-run
  --key 2026-W45` exits 0, and `read_metrics_lines` over the printed record answers, for each of the
  two entries, one triple whose value is `unread`, the first with the source
  `RuntimeError: git failed fatal: bad, ref` and the second `refused value`. A third planted reader
  answers a list of two pairs, `(one, src)` and a value carrying a line break; the record answers
  `(<name>, one, src)` then `(<name>, unread, refused value)` for it, in list order (round-3 id 32).
  The case prints `reader-raises-multiline — ok`, and otherwise a FAIL line naming the entry and what
  it read. Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- Truncating a long `<why>`. The record has no length cap at base, and a cap is a second rule for
  the writer to hold.
- The gather item's count of unread readings on stdout: id 22, `TOOL-dCalibratedLens-41`.
- A proposal field the writer would refuse at the pre-render: unit 27's `record-refuses` plant,
  which plants one, unchanged in intent.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-3` — the walk's isolation, `render_loop_record` and `read_metrics_lines`, which S1 amends and the case reads through
- **consumes-from** `TOOL-dCalibratedLens-27` — the `reader-raises` plant, which the case extends; without it there is no planted raising reader

## 4. Design

### Evidence

- Unit 3's id-49 bullet at rev-2: a raise or a refusal becomes `<name>: unread · <why>`; unit 3 §4
  "The record": "The writer refuses a value carrying a line break".
- Unit 21 S4 and its fourth criterion at rev-1 keep the writer's refusal for a multi-line value; its §5
  says "a refusing reader is `TOOL-dCalibratedLens-27`'s `unread` line".
- Unit 21 §4 "The lines": a line splits on its first `: ` and its LAST ` · `.
- `tools/roles/handoff.py:708-719` at base: `render_shape_line` makes every ` · ` inside a value `, `
  and every line break a space, so a value cannot add a field.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `reader-raises-multiline` | case of the `reader-raises` plant | none |
| `refused value` | the `unread` reason for a refused answer | none |

### Files touched (estimate)

- `tools/loop/loop_review.py` — S2, the case

### Alternatives rejected

- **Escape the separator instead of folding it.** Every reader of a Metrics line would need an
  unescape step; the fold loses nothing a reader acts on, since `unread` is the value it tests.
- **Let the writer fold every value.** It would hide a producer's multi-line value inside a valid line,
  where the reading should say it was refused.

## 5. Production-readiness checklist

- security — the writer's refusal of a line break stands; the boundary folds before it is reached.
- perf / scale — two string replacements per isolated failure.
- error / empty / loading states — every isolated failure is one parsable `unread` line, and no
  isolation path can exit the walk.
- observability — the folded message keeps the exception class and the whole text.
- risks — a reader whose real value is the word `unread`: none of the set's readers answers it, and
  the source field tells the two apart.
- testing — AC1 to AC3 by the pass.
- migration — N/A: no period has run at base.
- user docs — N/A: `help/loop-review.md` gains the `unread` word through unit 3's amendment.

## 6. Acceptance criteria

- **AC1** — When `python loop_review.py --fixture --plant reader-raises` runs `run --dry-run --key
  2026-W45` from the loop kit directory, it exits 0 and prints `reader-raises-multiline — ok`.
  Red when: a multi-line message or answer exits the walk, or a `<why>` holding ` · ` mis-splits.
- **AC2** — When the case runs with the boundary's fold staged out, the walk exits 1 at the
  pre-render or the case prints a FAIL line whose value is not `unread`.
  Red when: the unfolded `<why>` passes, so the fold is unobserved.
- **AC3** — When the case runs with the refusal staged to cover the whole list reading, the record
  answers one `unread · refused value` triple for the third reader and no `one` triple, and the case
  prints a FAIL line naming that reader.
  Red when: one multi-line entry costs a list reading its good entries, or the scope goes unobserved.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11) is not in the manifest at base
and is named here in prose; it runs the plant once that unit lands.

New arm: tools/loop/loop_review.py · covers AC1 AC2 AC3 · the `reader-raises-multiline` case, staged red by the isolation boundary writing the raw exception message · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 31 (HIGH, item H7) of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`; units 3, 27 and 21 amended at the disposal
  (their rev-3, rev-2 and rev-2).
- rev-2 · 2026-11-03 · §7 §10 S1 S2 AC3 · amended at the disposal of the round-3 spec audit
  `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`, from `TOOL-dCalibratedLens-48`: the refusal's
  scope for a list answer is the entry, planted in S2 and staged by AC3 (id 32), and units 3 and 21
  carry the same rule; §10 records this unit's own probe phrase (id 21).

## 10. Reuse audit

The seams extended are unit 3's isolation boundary and its one splitter `read_metrics_lines`, and
the fold is the rule `render_shape_line` in `tools/roles/handoff.py` already applies to a field value,
restated for one writer rather than imported across kits. `python tools/codebase-map/reuse_lookup.py
"fold a value so it adds no field"` ranked name stems only (`field` in
`tools/run-gates/profile_bar.test.sh`, `add_health_event`, `add_scratch_worktree`,
`check_audit_fold`); none is a value fold the loop kit can import, and the loop kit is absent at
base. The recall probe returned TOOL-cMendedVintage-19, the
placement ruling this unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a staged break that an ancestor
clause cannot make red repaired, and how is a spec audit finding promoted to a repair unit" --terms
"staged break ancestor clause superseded red twin spec audit promoted repair unit order shape line
renderer"`
