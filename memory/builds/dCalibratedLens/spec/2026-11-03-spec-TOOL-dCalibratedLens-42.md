# TOOL-dCalibratedLens-42 — the `graded-by-a-row` case calls `derive_record_kind` in the form TOOL-dTotalRecall-53 S21 gives it, and refuses any other form by name

**Status:** DEFERRED · rev-1 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 5 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-TOOL-dCalibratedLens-42-deviation-421.md](../build/2026-11-03-build-TOOL-dCalibratedLens-42-deviation-421.md) | deviation | — |
| [2026-11-03-prompt-TOOL-dCalibratedLens-42-1-spec-writer.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-42-1-spec-writer.md) | journal | — |
| [2026-11-03-prompt-TOOL-dCalibratedLens-42-promoted-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-42-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 1, HIGH, item H1 of the round-3 spec audit
(`reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`). Unit 35 S2 called
`derive_record_kind(path, text, rows)` and cited only TOOL-dTotalRecall-42 S5. TOOL-dTotalRecall-53
S21 changed the signature to `derive_record_kind(path, written_kind, rows)`, with no Serves line
parsed inside the function, and sibling unit 20 already consumes that form. One interface was
spelled two ways in one spec set. If -53 has landed, the old call passes a record's whole text where
a kind is expected, no row matches, and the case reds on a correct build; if it has not, the case is
built against an interface about to move. This unit re-grounds the call on -53 S21 and makes the
case name the signature it met whenever that signature is not the one it calls, so a skew between
the two ancestor revisions is a named refusal rather than a misgrade. It repairs
`TOOL-dCalibratedLens-35`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in unit 35's text (rev-2, id 1): S2 reads
  each planted record's written kind and calls `derive_record_kind(path, written_kind, rows)`; §4
  Evidence cites TOOL-dTotalRecall-53 S21 beside -42 S5, and its §3 Edges name both as a build-run
  precondition, as unit 20's external edge does. Observed by AC1.
- **S2** — The written kind. Before the case grades, it reads each planted record's kind with
  `tree_lib`'s own binding grammar, the `BIND_RE` match over the first `BIND_HEAD_LINES` lines that
  `unfenced` yields (`tools/memory-tree/tree_lib.py:401`, `:410`, `:515-532`), first Serves line
  winning. It does
  not call `read_bindings`, whose population is the build folders only (`record_paths`,
  `tools/memory-tree/tree_lib.py:421-425`), so no `memory/loop-review/` record reaches it. A planted
  record with no Serves line in that head prints `graded-by-a-row — FAIL · <path> · no written kind`.
  Observed by AC1.
- **S3** — The signature check. Once per plant run, before the first call, the case reads
  `inspect.signature(derive_record_kind)` from the shipped `record_kinds.py`. It holds when the
  parameter names are `path`, `written_kind` and `rows`, in that order. Otherwise it prints
  `graded-by-a-row — unread · derive_record_kind takes (<the names it read>)`, grades nothing and
  fails the plant. Observed by AC2.

## 3. Non-goals (OUT)

- Calling the -42 form when -53 is absent. Two call forms in one case would be the two spellings this
  unit removes from the spec set; the case names the form it met and the build run re-grounds.
- The case's pass line, its count and its zero-record red: id 5, `TOOL-dCalibratedLens-48`, landing
  on unit 35 S2.
- A spec-token check that reds two specs spelling one call with different parameter lists, the
  finding's left-shift line. It needs a parser of call sites inside spec prose, which no checker in
  the tree has.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-35` — the `graded-by-a-row` case and its record list, which S2 and S3 run ahead of; without the case there is no call to check
- **consumes-from** external — TOOL-dTotalRecall-42 S5 and TOOL-dTotalRecall-53 S21 (`derive_record_kind` and its `written_kind` form), DEFERRED at base; a build-run precondition, re-grounded at the build run

## 4. Design

### Evidence

- TOOL-dTotalRecall-42 S5
  (`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-42.md:53-58`):
  `derive_record_kind(path, text, rows)` returns the row whose `name` is the record's canonical
  Serves kind when that row's home matches the path.
- TOOL-dTotalRecall-53 S21
  (`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-53.md:94-96`):
  `derive_record_kind(path, written_kind, rows)`, callers passing the kind `tree_lib.read_bindings`
  classified, no Serves line parsed inside. Both specs are DEFERRED at base, and
  `git ls-files | grep record_kinds` prints nothing at `8bec4cef`.
- Unit 20 §3 Edges (`2026-11-02-spec-TOOL-dCalibratedLens-20.md:72`) consumes both clauses as a
  build-run precondition.
- `tools/memory-tree/tree_lib.py:421-425`: `record_paths` keeps only paths under a build's kind
  folders, so `read_bindings` (`:471`) never reads a `memory/loop-review/` record.

### Inventory

No identifier is minted. The `unread` line is the case's existing `unread` spelling.

### Files touched (estimate)

- `tools/loop/loop_review.py` — S2 and S3, inside the `graded-by-a-row` case

### Alternatives rejected

- **Classify with `read_bindings`, the review's fix as written.** Its population is the build
  folders, so every planted loop-review record would read no kind and the case would red on a
  correct build.
- **Catch the `TypeError` of a wrong call.** The -42 form takes three positional arguments too, so a
  wrong call raises nothing and the case would misgrade silently.

## 5. Production-readiness checklist

- security — reads only; one `inspect` call on the shipped module.
- perf / scale — one signature read per plant run.
- error / empty / loading states — a skewed signature is an `unread` line that fails the plant; a
  record with no written kind is a FAIL line.
- observability — the `unread` line names the parameters the case met.
- risks — a later ancestor revision renames a parameter: the case refuses by name, and the build run
  re-grounds the call.
- testing — AC1 and AC2 by the pass.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python loop_review.py --fixture --plant three-homes` runs from the loop kit
  directory over a `record_kinds.py` exposing `derive_record_kind(path, written_kind, rows)`, the
  `graded-by-a-row` case grades every planted record and prints no `unread` line.
  Red when: the case passes a record's text where the kind is expected, so a planted record reads
  graded by no row.
  fixture: `record_kinds.py` is a build-run precondition, absent at `8bec4cef`.
- **AC2** — When the plant runs with the shipped module's function staged as
  `derive_record_kind(path, text, rows)`, it prints
  `graded-by-a-row — unread · derive_record_kind takes (path, text, rows)` and the plant exits 1.
  Red when: the skewed form passes, or the case grades with it.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11) is not in the manifest at base
and is named here in prose; it runs the plant once that unit lands.

New arm: tools/loop/loop_review.py · covers AC2 · the `graded-by-a-row` signature check, staged red by the shipped function staged with the -42 parameter list · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, promoted from id 1 (HIGH, item H1) of the round-3 spec audit
  `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`; unit 35 amended at the disposal (its rev-2).

## 10. Reuse audit

The seams extended are unit 35's `graded-by-a-row` case and `tree_lib`'s binding grammar
(`BIND_RE`, `BIND_HEAD_LINES` and `unfenced` in `tools/memory-tree/tree_lib.py`), read rather than
copied. `python tools/codebase-map/reuse_lookup.py "check a function signature before calling it
across a kit"` ranked name stems only (`check`, `resolve_kit_dir`, `kit_rel`); none reads a
signature, so the case calls `inspect.signature` from the standard library. `read_bindings` was read
and rejected for its population (§4).

Recall terms used: `python tools/memory-recall/query.py "how does a fixture plant refuse an
interface or a listing that answers nothing" --terms "fixture plant case unread signature
derive_record_kind ls-tree pathspec glob empty listing vacuous"`
