# TOOL-dWitnessedBar-48 — the bash query sees any candidate list holding a bare `bash`, and the row-grammar resolver becomes an adapter

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 2 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 |
| [2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`)
confirmed finding **id 27 at HIGH**, its item **H9**, alone in that item. `resolve_shell_ere` in
`tools/memory-tree/row_grammar.py:1980` keeps its own candidate list,
`[os.environ.get("GOV_BASH", ""), "bash", "C:/Program Files/Git/bin/bash.exe", "/bin/bash", "sh"]`
(`:1989-1990`), with a bare `bash` second. `TOOL-dWitnessedBar-26`'s site table omits it, and its query
misses it: shape 2 needs the literal `bash.exe`, shape 1 a literal argv head. AC7's `[]` passes with the
copy present, against the goal that the one resolver is the only way a gov Python file finds a bash.
This unit takes the report's fix. It repairs `TOOL-dWitnessedBar-26`.

## 2. Scope (IN)

- **S1** — The site. `resolve_shell_ere` becomes an adapter over the `resolve_bash_py` block, carried
  inline: it runs the block's `found` bash and no candidate of its own, and returns `None` on the
  block's refusal, its existing "no ERE" contract. Its `sh` candidate leaves with the list. Observed by
  AC1.
- **S2** — Shape 2 widened. `scan_bare_bash` shape 2 matches any list or tuple literal holding the
  constant `bash` beside another bash candidate: a constant ending `bash.exe`, the constant `/bin/bash`,
  or a call reading `GOV_BASH`. Observed by AC2.
- **S3** — A membership test is not a launch. A literal that is the right operand of an `in` or
  `not in` comparison spawns nothing and is skipped by shape 2, so `argv[0] not in ("bash", "bash.exe")`
  inside `resolve_shell_argv` (`tools/govkit/govkit.py:1210`), which unit 26 keeps, stays out of the
  query. Observed by AC2.

## 3. Non-goals (OUT)

- The block, its rule, its twin and the other sites: `TOOL-dWitnessedBar-26`'s.
- `shutil.which("bash")` call sites: `TOOL-dWitnessedBar-49`'s, which adds the query's fourth shape.
- The pinned count of shape 2's matches and its re-derivation at the base: the minors batch's ids 23
  and 43 (`TOOL-dWitnessedBar-51`).
- The wrong-shell predicate inside the new inline copy: `TOOL-dWitnessedBar-27` puts it in the canonical
  block, and the `resolve_bash_py` parity row carries it to this copy whichever of the two lands first.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-26` — the `resolve_bash_py` block, its parity row and `scan_bare_bash`, which this unit gives one more site and a wider shape
- **hands-off** `TOOL-dWitnessedBar-51` — shape 2's membership rule of S3, on which the minors batch's ids 23 and 43 re-pin the shape's count
- **hands-off** `TOOL-dWitnessedBar-57` — the row-grammar adapter and its inline copy, which the resolver and ledger minors batch binds to `shell_used`, moves into `tree_lib.py` and observes in sequence (ids 12, 29, 36)

## 4. Design

### Evidence

- `resolve_shell_ere(sh, cwd)` runs each candidate with `[c, sh, "--print-rotated-archive-ere"]` and keeps
  the one that answered in `shell_used` (`tools/memory-tree/row_grammar.py:1980-2004`); its docstring
  names the WSL launcher a bare `bash` reaches on Windows.
- Unit 26 §4 "The query": shape 1 a call whose first argument is a literal list or tuple opening with
  `bash`; shape 2 a literal holding both `bash.exe` and `bash`; shape 3 the JavaScript spawns.

### The widened shape

```
shape 2 := ast.List | ast.Tuple  with an element  Constant("bash")
           and another element that is  Constant(s) with s ending "bash.exe",  Constant("/bin/bash"),
           or a Call whose source text reads GOV_BASH
           and that is not the comparator of a Compare whose op is In or NotIn
           and that sits outside a resolve_bash_py block
```

### Inventory

Minted: nothing by name; one more inline copy of `resolve_bash_py`.

### Migration

None: `resolve_shell_ere`'s callers keep its `None` contract.

### Rollout

Live at landing. This unit, `TOOL-dWitnessedBar-49` and `TOOL-dWitnessedBar-27` share order 2; this
unit and `TOOL-dWitnessedBar-49` both write `tools/run-gates/measure_legs.py`, so the main loop
sequences those two within the group (BUILD-METHOD M6, clause 1).

### Files touched (estimate)

- `tools/memory-tree/row_grammar.py`
- `tools/run-gates/measure_legs.py`
- `tools/lib/resolve-python.test.sh`

### Alternatives rejected

- **Exempt `resolve_shell_ere` by name.** It would keep a bare-`bash` fall-back the clause forbids.
- **Narrow shape 2 to a literal a `for` iterates.** `resolve_shell_ere` binds the list to a name first,
  and the next copy might pass it to a helper; the membership exemption is the narrower cut.

## 5. Production-readiness checklist

- security — removes a path to WSL's launcher on a Windows node.
- perf / scale — one more `ast` predicate per literal in the scan.
- error / empty / loading states — no bash resolvable: `None`, as before, now with the block's refusal
  text available to the caller.
- observability — the scan prints each match with its file and line.
- risks — the adapter drops the `sh` fall-back; a node with no bash but an `sh` gets no ERE, which is the
  existing `None` path.
- testing — AC1 and AC2 by probe and fixture; the arm of §7 at the close.
- migration — none.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `grep -c '^# >>> resolve_bash_py' tools/memory-tree/row_grammar.py` runs, it prints 1,
  and `git grep -nE 'GOV_BASH.{0,30}"bash",' -- tools/memory-tree/row_grammar.py` prints nothing.
  Red when: the row-grammar resolver keeps its own candidate list.
- **AC2** — When `python measure_legs.py --selftest` runs in `tools/run-gates/` with a fixture `.py`
  holding a list of a `GOV_BASH` read, the constant `bash` and Git's own bash.exe path, the
  `test_no_bare_bash_argv` arm reds naming that line; with a fixture holding
  `if argv[0] not in ("bash", "bash.exe"): pass` it stays green.
  Red when: shape 2 misses the GOV_BASH-headed list, or flags a membership test.

## 7. Gates

`measure-legs selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene`

New arm: tools/run-gates/measure_legs.py · covers AC2 · `test_no_bare_bash_argv` over the two fixture literals, staged red by planting the GOV_BASH-headed list in a tracked `.py` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-26`'s clause. (b) reds the parts
  join; veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's id 27 (HIGH, item H9).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-57, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.

## 10. Reuse audit

The seams are unit 26's `resolve_bash_py` block, carried to one more site under its parity row, and
`scan_bare_bash`, widened in place. `python tools/codebase-map/reuse_lookup.py "find every bash
candidate list a python file probes"` ranked `probe`, `resolve_python`, `resolve_bash` (the sites unit
26 names) and generic list readers; it did not surface `resolve_shell_ere`, which the report's grep
found, so the map's blind spot is the nested function this unit adds.

Recall terms used: `python tools/memory-recall/query.py "which python resolvers probe a bash candidate list" --terms "resolve_shell_ere row_grammar bash candidates GOV_BASH bare bash scan_bare_bash shape loop WSL launcher"`
