# TOOL-dTrueNorth-25 — the verdict-epoch gate sees deviation_join.py, and refuses a delegate list its imports outgrow

**Status:** OPEN · rev-1 · 2026-10-22 · node d · Tier-2 · base 271aa59d · streams tooling · order 9

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-22-build-TOOL-dTrueNorth-25-deviation-24.md](../build/2026-10-22-build-TOOL-dTrueNorth-25-deviation-24.md) | deviation | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-25-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-25-build-brief.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-23-spec-brief.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-23-spec-brief.md) | research | TOOL-dTrueNorth-23 TOOL-dTrueNorth-24 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review
(`memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md`)
confirmed **finding 11 at HIGH**, its item **H3**, and **finding 20 at MEDIUM**, its item **M7**,
which it judges the same defect. `DELEGATES` in `tools/memory-tree/check-verdict-epoch.sh:188` gained
`design_lib.py`, `asbuilt_view.py` and the spec-token checker, and left out the reader they hand off
to: `asbuilt_view.py:115-116` imports `read_records`, `read_record` and `read_baseline_line` from
`deviation_join.py`, and `asbuilt_view.py:208` returns `read_records(root, conf)`, which check 30's
`--check-asbuilt` renders and judges. A change to that module's record grammar moves check 30's
verdicts while `KIT_MEMORY_TREE_VERSION` stays put and this gate reports the constant honest. And
`TOOL-dTrueNorth-16`'s AC34, a grep for three names, cannot fail on the gap its own red-when names.
This unit takes the review's fix for both, which the skeptic judged sound: the module joins the
list, and the gate derives its delegates' sibling imports and refuses a list that misses one, the
class check M7 asks for. It repairs `TOOL-dTrueNorth-16` S34.

## 2. Scope (IN)

- **S1** — `DELEGATES` gains `${_kit}deviation_join.py`, H3's fix, and `${_kit}routed_commits.py` and
  `${_kit}backlog.py`, the two other siblings the delegates import today and the list omits
  (§4 Evidence). The S34 comment above it (`tools/memory-tree/check-verdict-epoch.sh:184-187`) names
  all three and why each is there. Observed by AC1 and AC3.
- **S2** — The class check. After the scan set is built
  (`tools/memory-tree/check-verdict-epoch.sh:190-198`), and where `resolve_python` answered
  (`:178`), one inline Python run reads every `.py` path the scan set holds, as UTF-8, parses each
  with `ast`, and walks every absolute `import` and `from … import` node in the file, nested ones
  included. A first name `<n>` is a sibling when `${_kit}<n>.py` is a file, and each sibling reached
  is walked the same way. Then:
  - a reached sibling the scan set does not hold exits 2, one line per sibling naming its path and
    the module that imports it;
  - a scanned module that does not parse exits 2 naming it, since its imports were not read;
  - otherwise one line, `verdict-epoch: the delegates' import closure is <N> sibling module(s), every one in DELEGATES`,
    prints before the verdict, `<N>` counting every module the walk read.
  Where no python resolves, one note line says the closure was not checked, as the recall kit's
  note does, and the verdict is unchanged. The check binds on and off the push boundary, because it
  grades the gate's own list, not a bump. Observed by AC2, AC3 and AC4.
- **S3** — **M7 is discharged here**, finding 20, so `TOOL-dTrueNorth-26`'s batch of minors carries
  no item for it. `TOOL-dTrueNorth-16`'s AC34
  (`memory/builds/dTrueNorth/spec/2026-10-21-spec-TOOL-dTrueNorth-16.md:512`) is superseded by AC3
  below, a check that can fail on the gap its red-when names. Observed by AC3.
- **S4** — The render's code is named whole in its two homes: the README's view-input sentence
  (`tools/memory-tree/README.md:28`) and `asbuilt_view.py`'s module docstring
  (`tools/memory-tree/asbuilt_view.py:31-32`) each list `deviation_join.py` beside
  `asbuilt_view.py`, `design_lib.py` and the host calls in `gen_build_index.py`. The README's row
  for `check-verdict-epoch.sh` (`tools/memory-tree/README.md:29`) says the gate refuses a delegate
  list its delegates' imports outgrow. Observed by AC5.

## 3. Non-goals (OUT)

- Deriving the scan set from the closure, so `DELEGATES` would hold only roots. It would leave a
  typed list beside a derived one that answers the same question; §4 "Alternatives rejected".
- The modules the engine runs by path and no delegate imports, handed off below.
- Following imports into another kit, and loads by name. The recall kit's `extract.py` and the
  spec-token checker are read as scanned files, and only their imports of this kit's siblings are
  followed. The checker's `load_kit_module` loads by name and is no `import` statement; every name it
  takes today (`tools/check-spec-tokens.py:678`, `:829`, `:855`) is already a delegate.
- The `KIT_MEMORY_TREE_VERSION` bump these edits owe, which `push-main.sh` mints.

### Edges

- **consumes-from** external — TOOL-dTrueNorth-16, CLOSED, so read as built rather than as an edge: S34's `DELEGATES` additions and AC34, which S1 extends and S3 supersedes
- **consumes-from** external — TOOL-dTrueNorth-17, CLOSED, so read as built rather than as an edge: the render's code list in the README and the view's docstring, which S4 completes
- **hands-off** `TOOL-dTrueNorth-26` — the view's module docstring, which S4 amends here and that unit's M8 edits after it, and M7, which S3 discharges so that unit carries no item for it
- **hands-off** external — `transition_audit.py`, check 26's delegate, which the engine runs at `tools/memory-tree/check-memory-hygiene.sh:1653-1655` and no delegate imports, so it is outside S2's walk and absent from `DELEGATES`; a later unit roots the walk at the engine's own invocations too

## 4. Design

### Evidence

Measured 2026-10-22 at `6f5f4ddec`, PINNED.

- The walk S2 specifies, run over the Python files `DELEGATES` names, reached eleven modules:
  `asbuilt_view`, `backlog`, `corpus_ids`, `design_lib`, `deviation_join`, `gen_build_index`,
  `gotchas`, `merge-rows`, `routed_commits`, `row_grammar` and `tree_lib`. Three of them are not in
  the list: `deviation_join` (imported by `asbuilt_view.py:115` and `gen_build_index.py:6212`),
  `routed_commits` (imported by `tools/memory-tree/deviation_join.py:124` at module level) and
  `backlog` (imported by `tools/memory-tree/gen_build_index.py:317` at module level, and lazily by
  `corpus_ids.py`, `row_grammar.py` and `merge-rows.py`). The walk took 0.6 s, the interpreter's
  start included.
- `TOOL-dTrueNorth-16` AC34 is the DELEGATES grep the review's M7 names. The spec brief for this
  unit calls it `TOOL-dTrueNorth-20`'s; that unit's AC34 greps a sentence about moved records, so
  the review and `memory/builds/dTrueNorth/spec/2026-10-21-spec-TOOL-dTrueNorth-16.md:512` are
  followed.
- The engine runs five sibling modules by path: `row_grammar.py`, `gen_build_index.py`,
  `gotchas.py`, `corpus_ids.py` and `transition_audit.py`. The first four are delegates.
- The gate already prints its scan set on its clean path
  (`tools/memory-tree/check-verdict-epoch.sh:325`) and the moved files on each failure (`:401`,
  `:413`), so AC1 and AC3 read existing lines.
- The suite runs the gate from its real path inside each fixture repository, and the gate derives
  `_kit` from its own directory (`tools/memory-tree/check-verdict-epoch.sh:175`), so a fixture laid
  out under the kit's prefix is what the walk reads.

### The walk

It over-counts on purpose, as the gate's header says the whole gate does: an import inside a
self-test function is walked like any other, so a module only a self-test imports is a delegate.
The cost is a version bump for a change that may move no verdict; the alternative is deciding from
source which imports a verdict reaches, the judgement call that let three modules drift out. A
relative import, and a name that is no file of the kit's directory, are not siblings.

What it does not check: a module loaded by computed path, through `importlib` or by a shell
invocation, is not an edge; a sibling of another kit is not walked; and with no python the check
does not run, which its note line says.

### Inventory

No identifier is minted outside the inline program. Its lines are the three S2 names.

### Files touched (estimate)

- `tools/memory-tree/check-verdict-epoch.sh`
- `tools/memory-tree/check-verdict-epoch.test.sh`
- `tools/memory-tree/README.md`
- `tools/memory-tree/asbuilt_view.py`

### Rollout

`asbuilt_view.py` is the render's code, so the commit that edits its docstring re-renders the view
through `gen_build_index.py --write` and stages it, as the README's rule requires; the docstring
moves no rendered byte. The new exit-2 branches are armed by the suite's new arms, which
`harness arms (fail branches armed or pinned)` reads.

### Alternatives rejected

- **The scan set derived from the closure.** It cannot go red, so it needs no remedy, but it makes
  `DELEGATES` a list of roots whose real reach is computed elsewhere, two answers to one question,
  and the review's fix asks that the list itself be complete.
- **The closure checked only in the suite.** It would run only where gov's suite runs, while the
  gate ships to every adopter; an adopter's kit is the same code, so the check costs it nothing to
  carry.

## 5. Production-readiness checklist

- security — no new surface: the inline program reads tracked kit files and writes nothing.
- perf / scale — one more python spawn per run, about 0.6 s at today's file sizes, against the leg's
  300 s ceiling.
- error / empty / loading states — a missing sibling and an unparseable delegate each exit 2 with
  their names; no python is one note line; the closure line reports its count, so an empty walk is
  visible.
- observability — the closure line on every run, and each refusal names the importer.
- risks — every change to `backlog.py` or `routed_commits.py` now owes a bump, which the lander
  mints; that is the over-count the header accepts.
- testing — AC1 to AC5; the arms under §7, observed red at the close against the base gate.
- migration — none.
- user docs — the README rows S4 names; no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When a probe clones this repository into a scratch directory, changes one
  behaviour-bearing line of `read_record` in the clone's `tools/memory-tree/deviation_join.py`,
  commits it with no version bump, and runs the clone's own `check-verdict-epoch.sh` with that
  commit's parent as `<base>`, it exits 1 and its `moved:` line names
  `tools/memory-tree/deviation_join.py`.
  Red when: `DELEGATES` omits the module, so the run exits 0 printing
  `clean — no behaviour-bearing engine line moved`.
  cost: a local clone of this repository, under a minute.
- **AC2** — When a probe builds a scratch repository holding, under `tools/memory-tree/`, an engine
  file carrying a `KIT_MEMORY_TREE_VERSION` line, a copy of `check-verdict-epoch.sh`, a
  `design_lib.py` whose body imports `newmod`, and `newmod.py`, and runs that copy with the base
  commit as `<base>`, it exits 2 naming `newmod.py` and `design_lib.py`.
  Red when: the gate scans only the typed list and exits 0 with a clean verdict.
- **AC3** — When AC1's clone runs its gate before the edit, with its `HEAD` as `<base>`, it exits 0,
  its closure line's count equals the number of modules the probe's own `ast` walk over the
  delegates reaches, and the scan set it prints holds `deviation_join.py`, `routed_commits.py` and
  `backlog.py`. This supersedes `TOOL-dTrueNorth-16`'s AC34.
  Red when: a sibling the walk reaches is absent from `DELEGATES`, which exits 2 naming it, or no
  closure line prints, so the check never ran.
  figure: DERIVED, the count read from the probe's own walk over the same scan set; at `6f5f4ddec`
  it reaches eleven kit modules, beside the checker and the recall kit's file where those are
  scanned.
- **AC4** — When AC2's repository instead holds a `design_lib.py` that does not parse, the copy
  exits 2 naming `design_lib.py` and saying its imports were not read.
  Red when: the parse error is caught and the walk reports the closure complete.
- **AC5** — When `git grep -n "deviation_join.py" -- tools/memory-tree/README.md tools/memory-tree/asbuilt_view.py`
  runs, it lists README line 28's render's-code sentence and the docstring's render's-code
  sentence, and `git grep -n "import closure" -- tools/memory-tree/README.md` lists the gate's row.
  Red when: either list names `asbuilt_view.py` and `design_lib.py` without `deviation_join.py`.

## 7. Gates

`verdict epoch (kit version dates the engine)` · `verdict-epoch self-test` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `build-index selftest` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-verdict-epoch.test.sh · covers AC1 AC2 AC4 · a fixture whose asbuilt_view.py imports deviation_join.py, edited with no bump; a design_lib.py importing a sibling the list omits; a delegate that does not parse · none

The suite's live-tree arm re-observes AC3 on this tree: with S1 the closure is complete, and without
it that arm exits 2.

## 8. Open questions

- **F1 — Which binding line does a unit the closing review promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it
  adds (ER:320). (b) None. (c) A `part k/n` carry of the repaired unit's clause. (b) reds
  `unbound` and (c) reds `parts`; veto 1 discards both. Recommendation (a). Rung 3. RESOLVED
  (agent, 2026-10-22, delegated): (a). widens: none · relaxes: none
- **F2 — How is the class closed?** (a) The gate refuses a list its delegates' imports outgrow,
  the review's fix. (b) The gate derives its scan set from the closure. (c) An arm in the suite
  alone. All three pass every veto. (a) is the most capable: it reds wherever the gate runs, and it
  keeps one complete list where (b) keeps two. §4 says why. Recommendation (a). Rung 3. RESOLVED
  (agent, 2026-10-22, delegated): (a). widens: none · relaxes: none
- **F3 — Where does the walk start?** (a) The Python files `DELEGATES` names. (b) Those and every
  module the engine runs by path, which reaches `transition_audit.py`. (b) dates check 26, which no
  dTrueNorth clause names, so it is a governance-carrier change outside the grant (veto 2); (a)
  passes every veto, so rung 3 takes it and (b)'s extra root is handed off. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-22, delegated): (a). widens: none · relaxes: none
- **F4 — Does the build's grant lift veto 2 for the edits here?** The gate dates checks 29 and 30,
  `cl-dClosedLoop-0002`'s carries join and `cl-dClosedLoop-0003`'s coverage region through check 29,
  and `cl-dClosedLoop-0006`'s view and gate through check 30, whose record reader is
  `cl-dClosedLoop-0004`'s. `TOOL-dTrueNorth-16` S34 edited the same list under the same grant.
  RESOLVED (agent, 2026-10-22, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants:
  PLAY-dClosedLoop-3 the verdict-epoch gate, its suite, the kit README and the view's docstring,
  for cl-dClosedLoop-0002, cl-dClosedLoop-0003, cl-dClosedLoop-0004 and cl-dClosedLoop-0006 ·
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-22 · initial draft, promoted from the closing diff review's finding 11 (HIGH,
  item H3), discharging finding 20 (MEDIUM, item M7).

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "derive the sibling module import closure of the
verdict epoch delegates"` ranked `derive_*` functions by name stem, none an import walk. The seam
this unit extends is the gate's own scan set, `DELEGATES` and the loop that builds `SCAN`
(`tools/memory-tree/check-verdict-epoch.sh:188-198`), and its `resolve_python` answer at `:178`,
already used for the recall kit. The nearest import walker in the kit is row_grammar's
`scan_engine_imports` (`tools/memory-tree/row_grammar.py:1748`), which reports any module importing
one of two named engines; it follows no edge, and the gate reads no kit module as a library, so it
is not reused. No existing seam fits the closure itself: the reuse probe returned none, and
grepping the kit for `ast.Import` found only that scan. The recall query returned the review's H3 and
M7, `TOOL-aBatchedTribunal-6o`'s decision that the engine is not one file, and the round-1 spec
audit's L9, whose left-shift asked for "a hygiene check that delegates must have its delegate in
DELEGATES"; that is F3's option (b), handed off.

Recall terms used: `python tools/memory-recall/query.py "how does the verdict epoch gate learn which
delegate modules move a verdict" --terms "check-verdict-epoch DELEGATES one-hop-short
KIT_MEMORY_TREE_VERSION delegate import closure scan_engine_imports move-inventory-misses-readers-by-path
deviation_join asbuilt_view"`
