# TOOL-dBoundRoles-45 — a typed `--input` value is authored text: written unfenced, refused when a line would stand as an executor line, so the anchor check grades it

**Status:** OPEN · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 12 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 |
| [2026-10-26-build-TOOL-dBoundRoles-45-round2-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-45-round2-fix-return.md) | research | TOOL-dBoundRoles-43 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 |
| [2026-10-26-prompt-TOOL-dBoundRoles-45-round2-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-45-round2-fix-brief.md) | research | TOOL-dBoundRoles-43 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 |
| [2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-49 TOOL-dBoundRoles-46 TOOL-dBoundRoles-48 TOOL-dBoundRoles-47 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the eight promoted specs 37 to 44
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md`) confirmed
finding **id 17 at HIGH**, report item **H1**. Ids 1 and 9 share the item at HIGH and take
`TOOL-dBoundRoles-46` and `TOOL-dBoundRoles-47`.

`TOOL-dBoundRoles-38` S2 fences every block a `reads` value renders, "argument values included", and
`render_handoff` renders `input:question` as one of those blocks (`tools/roles/handoff.py:379-386`, the
`input` source at `:380`). `TOOL-dBoundRoles-41` S2 calls the same typed value authored text that
`check_anchors` must grade, and `TOOL-dBoundRoles-24` S2 strips fenced blocks before it scans. Built in
order, 38 at 11, 24 at 19 and 41 at 20, a backticked `record:` anchor planted in `--input question=` is
stripped and never graded: 24 AC2, 41 AC2 and 41 F2(a) go red against a correct build, and the easy way
to green them reopens the forging path 38 closes.

This unit gives the question one answer, the report's option (a): a typed value is authored, so the
render writes it without a fence and refuses it when any of its lines would stand as an executor line.
It repairs `TOOL-dBoundRoles-38` and builds one step after it (order 12).

## 2. Scope (IN)

- **S1** — What is fenced. `render_handoff`, as `TOOL-dBoundRoles-38` S2 leaves it, wraps every `reads`
  block's content in `render_handed_fence` except a typed input's. A typed input is a name in
  `INPUT_NAMES` that is not in `PATH_INPUTS` (`tools/roles/handoff.py:98-99`), today `question` and
  `diff`; the set is derived from those two constants, never typed a third time. Its block is the
  `### input:<name>` heading, a blank line, its fact line, a blank line, and the value's bytes. Observed
  by AC1.
- **S2** — The authored-line rule. `check_authored_lines(value, field)` in `tools/roles/roles_lib.py`
  returns one line per line of `value` that matches `^#{1,3} `, `FACT_RE`, `MARKER_RE` or `^Framed by:`,
  naming the field and the line number, plus one line when `read_unfenced_lines(value)` ends on its
  open-fence yield, naming the line the fence opened at. A fence the value opens and closes is legal.
  `render_handoff` calls it on each typed value before it composes the section; every line joins
  `refusals`, so the render raises and writes no file. Observed by AC2.
- **S3** — The docs. The handoff section of `tools/roles/README.md` that `TOOL-dBoundRoles-38` S6
  writes gains one sentence: a typed input is authored, is written unfenced, is refused when a line
  would read as a heading, fact, marker or `Framed by:` line or its fence never closes, and is graded by
  the anchor check. Observed by AC3.

## 3. Non-goals (OUT)

- The fence writer, the walker and the open-fence refusal: `TOOL-dBoundRoles-38`'s, read here.
- The same rule at spawn, in `checkHandoffSpawn`: `TOOL-dBoundRoles-46`'s, for id 1.
- The cross-unit criterion that renders with 24 and 41 landed and sees the planted anchor refused:
  `TOOL-dBoundRoles-47`'s, for id 9. At this unit's order neither 24 nor 41 exists.
- The block-boundary fence check over the composed section: `TOOL-dBoundRoles-48`'s, for id 34.
- The prompt writer's framing fields. `TOOL-dBoundRoles-43` S36 refuses the same four line shapes in
  them; that pass's reuse probe finds S2's function, and calling it is that unit's choice.
- 38 AC4's render half, which holds from this unit on (§4 "What 38 AC4 reads afterwards"); its answer in
  38's ledger and the end-state observation are `TOOL-dBoundRoles-50`'s, for id 10.

### Edges

- **consumes-from** `TOOL-dBoundRoles-38` — `render_handed_fence`, `read_unfenced_lines` and S2's fencing in `render_handoff`, which S1 narrows to every block but a typed input's (id 17)
- **hands-off** `TOOL-dBoundRoles-24` — a typed value that reaches the task section unfenced, so S3's whole-section check grades an anchor planted in it and AC2 holds as written (id 17)
- **hands-off** `TOOL-dBoundRoles-41` — a typed value written raw, so S2's "authored" block and §4's graded block are the value itself, with no fence for unit 24's strip to remove (id 17)
- **hands-off** `TOOL-dBoundRoles-47` — the unfenced typed block and S2's rule, which unit 47's cross-unit arm renders through (ids 9 and 17)
- **hands-off** `TOOL-dBoundRoles-50` — the unfenced typed value, through which unit 50 observes unit 38 AC4's render half on the built tree (id 10)
- **hands-off** `TOOL-dBoundRoles-58` — `check_authored_lines`, AC1 and §5, which unit 58 completes: the line split, the graded shapes, the control render and the risk line (ids 4, 12, 35, 37, 38, 42, 45 and 46 of the round-1 audit of units 45 to 51)
- **hands-off** `TOOL-dBoundRoles-64` — §3, which unit 64 extends by the hands-off bullet for unit 63 (id 26 of the round-1 audit of units 61 to 63)

## 4. Design

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `tools/roles/handoff.py:98-99` declares `INPUT_NAMES = ("spec", "diff", "question", "prompt")` and
  `PATH_INPUTS = ("spec", "prompt")`; `:331` resolves only the path inputs to files.
- `:380` maps the `input` source to `("arguments", None)`, and `:381-386` appends every filled `reads`
  value as `### <key>` and its bytes, so a typed value is one block among the handed ones.
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-13.md` §4 "The classes" keys a typed
  value `cmd:` over the argument, class `claimed`: it carries a fact line like a handed block, and S1
  keeps it.

### The one answer

| Block | Content source | Fenced | Graded by `check_anchors` |
|---|---|---|---|
| `input:spec`, `input:prompt`, `task:`, `card:`, `brief:`, an excerpt, `input:work-order` | a file or a record | yes, `TOOL-dBoundRoles-38` S2 | heading and fact line only, `TOOL-dBoundRoles-41` S2 |
| `input:question`, `input:diff` | the caller's argument | no, S1 | the whole block, under S2's rule |

`TOOL-dBoundRoles-24` S2 strips fenced blocks before it scans. After S1 the only fence inside a typed
block is one the value closes itself, so a span quoted inside it is skipped as an example, and every
other span is graded. That is the remedy `TOOL-dBoundRoles-41` §4 names, "fence the quotation", and S2
admits it because the fence closes.

### What 38 AC4 reads afterwards

`TOOL-dBoundRoles-38` AC4 hands `--input question=` a line of four backticks that nothing closes and
expects a refusal. At 38's own order S1 of 38 wraps that value in five, the walk closes, and nothing
refuses. From this unit on the value is unfenced and S2 refuses it, naming the open line, so the
criterion holds as written on the built tree.

### Inventory

Minted: `check_authored_lines` (`py.function`) and its refusal line. Its name is asked of
`python tools/lexicon/lexicon.py --suggest check_authored_lines --as py.function` at the pass.

### Migration

None: no stored data changes. A handoff rendered between orders 11 and 12 fences its typed value; a
re-render writes it raw.

### Rollout

Live at landing, at order 12. Dispatch is strictly sequential within a shared order
(`tools/workflows/unattended-build.js:76-80`), and this unit consumes from no unit at its order.
`TOOL-dBoundRoles-48` writes `handoff.py` and `roles_lib.py` at the same order, and `--dispatch` refuses
a pass whose declared write set meets an open one's.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/README.md`

### Alternatives rejected

- **Option (b): keep the fence and grade the raw value.** It needs `TOOL-dBoundRoles-41`'s graded text
  and a narrower strip in `TOOL-dBoundRoles-24`, neither of which exists before order 19, so 24 AC2 at 19
  and 41 AC2 at 20 stay red against a correct build, and 38 AC4's render half can never hold (§8 F2).
- **Fence the typed value and exempt it from the strip.** The strip cannot tell a typed value's fence
  from a handed block's without the render's extents, which only unit 41 builds.

## 5. Production-readiness checklist

- security — a typed value no longer sits inside a fence, and S2 refuses every line shape the readers
  act on, so no forged heading, fact, marker or framing line reaches them; no new write path.
- perf / scale — one pass over each typed value per render.
- error / empty / loading states — an empty typed value is a placeholder and refuses as before
  (`handoff.py:385`); each S2 refusal names the field and the line.
- observability — every refusal line names `input:<name>` and the line number.
- risks — a diff whose hunk context holds one fence line of a pair is refused; widen the context or hand
  the file as `input:spec`.
- testing — AC1 to AC3 by render and grep; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`; the README sentence by S3.

## 6. Acceptance criteria

- **AC1** — When `python handoff.py render --role gov-researcher --build tFix --unit TOOL-tFix-1
  --input question='plain words' --stdout` runs in a scratch adopter, the line after the
  `input:question` fact line's blank is `plain words`, with no backtick fence line between them; and a
  `--role gov-spec-writer` render of `--input spec=<scratch spec>` still wraps the spec's bytes in a fence.
  Red when: the typed value is fenced, or the file input loses its fence.
  fixture: a scratch repository with the roles kit installed, under `%TEMP%`, short-pathed.
- **AC2** — When the same render passes `--input question=` holding, one case each, a whole
  `<!-- gov:fact key=record:x@000000000000 class=witnessed -->` line, a `### allowance` line, a whole
  `gov:handoff` marker line, a `Framed by:` line, and a line of four backticks that nothing closes, each
  exits non-zero naming `input:question` and the line, and writes no file; a value holding a closed
  three-backtick fence renders.
  Red when: a forged executor line or an open fence passes, or a closed fence is refused.
- **AC3** — When `grep -n 'a typed input is authored' tools/roles/README.md` runs, it prints one line, in
  the handoff section.
  Red when: the README still says every argument value is fenced.

## 7. Gates

`roles adopter self-test` · `roles catalogue` · `roles render selftest` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 · a researcher render whose typed question holds plain words, then each forged line and an open fence, staged by a `render_handoff` that fences the typed value and skips `check_authored_lines` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 38 carries no
  clause, and unit 13's is carried whole; veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Is a typed value fenced and graded raw, or unfenced under a line rule?** Options: (a) unfenced
  under S2's rule, the report's first option; (b) fenced, with unit 41 grading the raw value and unit 24
  stripping only authored blocks. (b) leaves 24 AC2 and 41 AC2 red at their own passes and 38 AC4's
  render half unsatisfiable, three criteria already written; (a) satisfies all three from order 12.
  (a) costs a diff that cuts a fence pair in half, which §5 names with its remedy. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, the most criteria satisfied. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 37 to 44, id 17
  (HIGH, item H1, shared with ids 1 and 9), on the report's option (a).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-58, the minors batch of the round-1 audit of units 45 to 51; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-64, the minors batch of the round-1 audit of units 61 to 63; nothing else moved.

## 10. Reuse audit

The seams are `render_handoff`'s block loop (`tools/roles/handoff.py:381-386`), the two input constants
beside it (`:98-99`), and `TOOL-dBoundRoles-38`'s `read_unfenced_lines` and the `FACT_RE` and
`MARKER_RE` patterns in `tools/roles/roles_lib.py`, which S2 composes rather than restates.
`python tools/codebase-map/reuse_lookup.py "refuse a line that would read as a heading, fact or marker in an authored value"`
ranked `read`, `read_text`, `read_conf` and `read_journal`, none a line refusal, so no existing seam fits
beyond the patterns named; `TOOL-dBoundRoles-43` S36 specifies the same four shapes for framing fields
at order 28, after this unit, and can call S2's function.

Recall terms used: `python tools/memory-recall/query.py "how are typed input values kept from forging executor lines in a work order" --terms "typed input question diff fence handed content fact line marker forged authored framing refusal"`
