# TOOL-dDeclaredLoop-76 — the loop readers' no-own-conf-read rule is graded on the syntax tree, and the root's source is a value

**Status:** OPEN · rev-4 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 37 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-76-deviation-761.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-76-deviation-761.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-76-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-76-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-76-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-76-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 |
| [2026-10-24-review-TOOL-dDeclaredLoop-76-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-76-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-79 |

<!-- /gen:spec-records -->

## 1. Goal

The round-4 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md`)
confirmed finding **id 1 at HIGH**, its item **H1**, alone in that item. `TOOL-dDeclaredLoop-72` AC4 runs
`grep -c ".memory-tree.conf\|.unattended.conf"` over `tools/loop/budget.py` and `tools/loop/breakpoints.py`
and requires 0 in each. `TOOL-dDeclaredLoop-75` builds later (order 39; 72 is order 36) and requires those
literals in the same two files: S5 and S30 put `.unattended.conf` in the two module docstrings (AC5,
AC30), and S7 and S8 print `from .unattended.conf` (AC7, AC8). 72 S1 returns a bare root, so 75 has no
value to print the source from except a literal or a conf probe of its own. Built in order, 72 AC4 and
75's four criteria cannot all hold.

This unit states what 72 AC4 means, that neither reader reads a conf, as a rule over each module's syntax
tree rather than a substring count, and gives both readers the root's source as a value from the one
resolver. It builds immediately after 72, so 72's pass is untouched and 75's pass finds both in place.
It repairs `TOOL-dDeclaredLoop-72`.

## 2. Scope (IN)

- **S1** — `resolve_memory_root_source(tree)` in `tools/loop/loop_lib.py` returns `(root, source)`, where
  `source` is `.unattended.conf`, `.memory-tree.conf` or `default`, by 72 S1's own branches and with 72
  S2's refusal unchanged. `resolve_memory_root(tree)` returns that pair's root, so every caller 72 S3
  names keeps its call. Observed by AC3.
- **S2** — `derive_conf_reads(path)` in `tools/loop/loop_lib.py` parses a module with `ast` and returns
  one `(line, kind)` per conf read: a call whose callee name is `parse_conf` or `read_driver_conf`, and a
  string constant ending `.memory-tree.conf` or `.unattended.conf` anywhere but a module, class or
  function docstring. An f-string's literal part is a string constant and counts. Observed by AC2.
- **S3** — The plant `no-own-conf-read` joins `budget.py --fixture` and `breakpoints.py --fixture`: each
  runs S2 over its own module file and exits non-zero naming `<file>:<line> <kind>` for every hit.
  Observed by AC1.
- **S4** — From this pass on, 72 AC4's property is observed by S3's plant and not by its substring grep:
  the grep's `Red when` (a reader keeps its own conf read beside S1) is exactly S2's population, and a
  docstring naming the conf is not a read. The close records 72 AC4 against AC1 of this unit.
  Observed by AC1, AC4.

## 3. Non-goals (OUT)

- What either reader prints or documents: 75 S5, S7, S8 and S30, unchanged, now built over S1's source
  value and inside S2's rule, as this unit's hands-off bullet to 75 records.
- Which root wins, and when the two confs disagree: 72 S1 and S2, unchanged.
- A spec-set check that reds a later-ordered spec requiring a token in a file where an earlier sibling's
  criterion asserts its absence, the finding's left-shift: the class is recorded at the close; AC4 is this
  pair's observation.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-72` — `resolve_memory_root` in `tools/loop/loop_lib.py` and AC4's no-own-conf-read property, which this unit gives a source value and a syntax-tree grade
- **hands-off** `TOOL-dDeclaredLoop-75` — `resolve_memory_root_source`, from whose `source` S7's `--explain` line and S8's held line print the conf, and S2's rule, inside which S5's and S30's docstrings name it; that pass re-runs the `no-own-conf-read` plant
- **hands-off** `TOOL-dDeclaredLoop-80` — the `no-own-conf-read` plant's population, which that unit bounds at a function-name fixture boundary so the plants writing the confs sit outside it (the round-5 spec audit's id 20)
- **hands-off** `TOOL-dDeclaredLoop-82` — `derive_conf_reads`, `resolve_memory_root_source`, the `root-source` plant and §4, which that unit widens to cross-module conf constants, mid-string names and aliased calls, gives a source for every branch, and amends (the round-5 spec audit's ids 1, 10, 11, 12, 17, 30)
- **hands-off** `TOOL-dDeclaredLoop-86` — AC1's exit-0 half, which that unit moves to 80's pass commit where the plants sit inside the boundary, and S2 and §4's sketch, which it restates to a constant containing a conf name (the round-6 spec audit's ids 11, 12)
- **hands-off** `TOOL-dDeclaredLoop-95` — `resolve_memory_root_source`, whose `.memory-tree.conf` read that unit moves onto `read_tree_conf` (the round-11 spec audit's id 1)

## 4. Design

### Evidence

- 72 AC4's observation is a substring count over the two files and its stated break is "a reader keeps
  its own conf read beside S1" (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-72.md`,
  §6 AC4): the count cannot tell a docstring from a read.
- 75 AC5 and AC30 need `.unattended.conf` in `budget.__doc__` and `breakpoints.__doc__`; AC7 needs the line
  `root records · from .unattended.conf`; AC8 a held line ending `root from .unattended.conf` or
  `root from .memory-tree.conf` (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md`,
  §6). AC8's two endings need the source as a value: a literal can name only one of them.
- `ast.get_docstring` answers a node's docstring only where its first statement is a string expression;
  `tools/govkit/refusal_join.py:214` and `tools/gate-lint/encoding_posture.py:149` already walk a module
  with `ast.parse`, read at base `ed497191`.
- `tools/loop/` does not exist at base: every loop path below is a sibling unit's output.

### The rule

```
derive_conf_reads(path):
    tree = ast.parse(read(path))
    docs = { id(first statement's constant) for the module and every ClassDef and FunctionDef
             whose body opens with a string expression }
    for node in ast.walk(tree):
        Call whose func is Name or Attribute named parse_conf or read_driver_conf -> (line, "reader call")
        Constant str ending ".memory-tree.conf" or ".unattended.conf", id(node) not in docs
                                                                      -> (line, "conf name")
```

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/budget.py`
- `tools/loop/breakpoints.py`

### Alternatives rejected

- **Narrowing 72 AC4 alone.** 75 AC8's two endings still need the source; a reader would then probe for
  `.unattended.conf` itself, a path join S2 rightly counts, and the conflict returns one level down.
- **Rewording 75's four criteria to drop the literals.** The docstrings are where 75's ids 4 and 17 put the
  rationale, and the printed source is what id 42 asks for; removing them reopens those findings.
- **Admitting a conf name in any call argument but `open` and `Path`.** A module-level `CONF = ".unattended.conf"`
  read later through a name would pass; the constant rule sees it.

## 5. Production-readiness checklist

- security — a read-only parse of the kit's own modules.
- perf / scale — one `ast.parse` of one file per plant run, milliseconds.
- error / empty / loading states — a module that does not parse is a plant failure naming the file and
  the parse error, never zero hits.
- observability — each hit names the file, the line and its kind.
- risks — a read composed at run time, `"." + "unattended.conf"`, passes S2; S1 makes such a read
  unnecessary and the rule is stated so a reviewer can see the gap.
- testing — AC1 to AC4 as plants and probes; the arms under §7, observed at the close.
- migration — none: the readers are unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python budget.py --fixture --plant no-own-conf-read` and the same plant of
  `breakpoints.py --fixture` run in `tools/loop/`, each exits 0; in a scratch copy of `tools/loop/` whose
  `budget.py` gains the line `(tree / ".unattended.conf").read_text()`, the first exits non-zero naming
  that line and `conf name`.
  Red when: the plant greps substrings, or S2 skips a path join of a conf name.
- **AC2** — When a `python -c` probe calls `derive_conf_reads` on a scratch module holding a docstring that
  names `.unattended.conf` and nothing else, it returns an empty list; on one holding `parse_conf(text, {})`,
  `read_driver_conf(tree, ["MEMORY_ROOT"])`, `tree / ".memory-tree.conf"` and `print(f"from .unattended.conf")`
  it returns four hits, two `reader call` and two `conf name`.
  Red when: a docstring counts as a read, or an f-string literal part does not.
- **AC3** — When `python budget.py --fixture --plant root-source` calls `resolve_memory_root_source` in
  three scratch trees, `.unattended.conf` alone at `records`, `.memory-tree.conf` alone at `records`, and
  neither, it answers `(records, .unattended.conf)`, `(records, .memory-tree.conf)` and
  `(memory, default)`.
  Red when: the source is guessed from the root, so two trees with one root answer one source.
- **AC4** — When the main loop runs the `no-own-conf-read` plant of both fixtures after
  `TOOL-dDeclaredLoop-75`'s pass, at the close, each exits 0 while `grep -c ".unattended.conf"` over the
  two files prints at least 1.
  Red when: 75's printed lines carry the conf as a literal instead of S1's source value.
  fixture: 75 builds at order 39, so this is observed at the close and not at this pass.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

This pass keeps the sibling-minted `loop budget fixtures` leg (`TOOL-dDeclaredLoop-30`) and the
`loop breakpoints fixtures` leg (`TOOL-dDeclaredLoop-71`) green; both sit outside the base manifest.

New arm: tools/loop/budget.py · covers AC1 AC3 · the no-own-conf-read and root-source plants, staged by adding a path join of the conf name to a scratch copy · none
New arm: tools/loop/breakpoints.py · covers AC1 · the no-own-conf-read plant over its own module, staged the same way · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Narrow 72 AC4, or give 75 the source as a value?** The fix offers either. (a) grade "no conf
  read" on the syntax tree; (b) return `(root, source)` and print through it; (c) both. (a) alone leaves
  75 AC8's two endings with no source; (b) alone leaves 72 AC4's grep red over the docstrings 75 S5 and
  S30 write. (c) satisfies every criterion of both specs. RESOLVED (agent, 2026-10-24, delegated): (c).
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-4 spec audit's id 1 (HIGH, item H1).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-80 and TOOL-dDeclaredLoop-82, written by the round-5 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-86, written by the round-6 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-95, written by the round-11 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams are 72's `resolve_memory_root`, extended in place to carry its branch as a value, and Python's
`ast` walk as `tools/govkit/refusal_join.py:214` already uses it; no second resolver and no grep is minted.
`python tools/codebase-map/reuse_lookup.py "find calls that read a config file by walking a module's syntax tree"`
ranked `read`, `read_text`, `tree`, `walk` (`tools/memory-tree/corpus_ids.py`) and `read_conf`, none of which
classifies a module's conf reads, so no existing seam fits the rule itself; `tools/loop/loop_lib.py` is
unbuilt at base and its resolver is 72's spec.

Recall terms used: resolve_memory_root unattended.conf memory-tree.conf docstring ast conf read substring grep budget breakpoints source
