# TOOL-dWitnessedBar-48 — the bash query sees any candidate list holding a bare `bash`, and the row-grammar resolver becomes an adapter

**Status:** CLOSED · rev-4 · 2026-11-19 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 2 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 |
| [2026-10-25-build-TOOL-dWitnessedBar-48-deviation-481.md](../build/2026-10-25-build-TOOL-dWitnessedBar-48-deviation-481.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-48-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-48-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-27-spec-tokens-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-27-spec-tokens-brief.md) | journal | TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-54 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-48-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-48-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-48-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-48-reground-brief.md) | journal | TOOL-dWitnessedBar-49 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-48-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-48-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-51 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`)
confirmed finding **id 27 at HIGH**, its item **H9**, alone in that item. `resolve_shell_ere`, nested
in `cmd_selftest` (`tools/memory-tree/row_grammar.py#resolve_shell_ere`), keeps its own candidate list,
`[os.environ.get("GOV_BASH", ""), "bash", "C:/Program Files/Git/bin/bash.exe", "/bin/bash", "sh"]`
(`tools/memory-tree/row_grammar.py@2b622305:1945`), with a bare `bash` second. `TOOL-dWitnessedBar-26`'s
site table omits it, and its query as landed (`tools/run-gates/measure_legs.py#scan_bare_bash`) misses
it: shape 2 needs both exact constants `bash.exe` and `bash`, and shape 1 a literal argv head or an `or`
falling back to the name. Unit 26's AC7 reads `[]` at `88352ca5` with the copy present (PINNED,
measured 2026-11-19), against the goal that the one resolver is the only way a gov Python file finds a
bash. This unit takes the report's fix. It repairs `TOOL-dWitnessedBar-26`.

## 2. Scope (IN)

- **S1** — The site. `resolve_shell_ere` becomes an adapter over the `resolve_bash_py` block, carried
  inline: it runs the block's `found` bash and no candidate of its own, and returns `None` on the
  block's refusal, its existing "no ERE" contract. Its `sh` candidate leaves with the list. Observed by
  AC1.
- **S2** — Shape 2 widened. `scan_bare_bash` shape 2 matches any list or tuple literal holding the
  constant `bash` beside another bash candidate: a constant ending `bash.exe`, the constant `/bin/bash`,
  or a call reading `GOV_BASH`. Observed by AC2.
- **S3** — A membership test is not a launch. A literal that is the right operand of an `in` or
  `not in` comparison spawns nothing and is skipped by shape 2, so a test such as
  `argv[0] not in ("bash", "bash.exe")` stays out of the query. No tracked file holds one at
  `88352ca5`: `resolve_shell_argv`, whose literal this item was written for, now tests
  `argv[0] not in BASH_NAMES` (`tools/govkit/upgrade_steps.py@a814a6ae:491`), and the rule stays for
  the class and for `TOOL-dWitnessedBar-51` S18, which reads it (§8 F2). Observed by AC2.

## 3. Non-goals (OUT)

- The block, its rule, its twin and the other sites: `TOOL-dWitnessedBar-26`'s.
- `shutil.which("bash")` call sites: `TOOL-dWitnessedBar-49`'s, which adds the query's fourth shape.
- The pinned count of shape 2's matches and its re-derivation at the base: the minors batch's ids 23
  and 43 (`TOOL-dWitnessedBar-51`).
- The wrong-shell predicate inside the new inline copy: `TOOL-dWitnessedBar-27` S4 puts it in the
  canonical block and builds before this unit, so the copy this unit adds is the canonical at its pass
  tip, predicate included, and the `resolve_bash_py` parity row holds it there.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-26` — the `resolve_bash_py` block, its parity row and `scan_bare_bash`, which this unit gives one more site and a wider shape
- **hands-off** `TOOL-dWitnessedBar-51` — shape 2's membership rule of S3, on which the minors batch's ids 23 and 43 re-pin the shape's count
- **hands-off** `TOOL-dWitnessedBar-57` — the row-grammar adapter and its inline copy, which the resolver and ledger minors batch binds to `shell_used`, moves into `tree_lib.py` and observes in sequence (ids 12, 29, 36)

## 4. Design

### Evidence

- `resolve_shell_ere(sh, cwd)` runs each candidate with `[c, sh, "--print-rotated-archive-ere"]` and
  appends the one that answered to `shell_used`, which `check_readers_agree` runs again as
  `shell_used[0]` (`tools/memory-tree/row_grammar.py#resolve_shell_ere`); its docstring names the WSL
  launcher a bare `bash` reaches on Windows. The module imports `os` and `subprocess`, all the block
  needs.
- `scan_bare_bash` as unit 26 landed it (`tools/run-gates/measure_legs.py#scan_bare_bash`): shape 1 a
  call whose first argument is a literal list or tuple opening with `bash` or `bash.exe`, or an `or`
  whose last operand is that name; shape 2 a literal holding both names; shape 3 the JavaScript spawns
  and fall-backs. It reads the two names from `profile_bar.BASH_NAMES`, because a literal pair in its
  own file was its own shape 2 hit (the `Decided:` trailer of `7526c98fa`), so the widened shape's
  constants are spelled where no tracked list holds them beside `bash`.
- The scan lists a language with no tracked file read as a line of its own
  (`tools/run-gates/measure_legs.py@95b532a7:2744`), so each fixture repo of AC2 also tracks one `.js`.
- The widened shape over the tree at `88352ca5` finds one literal outside a block, row_grammar's list
  above, and no membership comparator; every `BASH_NAMES` tuple it also matches sits inside a
  `resolve_bash_py` block (PINNED, measured 2026-11-19 with an `ast` probe over 241 tracked `*.py`).
- The parity row finds its copies by a `git grep` of the block marker
  (`tools/lib/resolve-python.test.sh@caa9482a:481`), so the new copy joins it with no edit there.

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

Live at landing. This unit, `TOOL-dWitnessedBar-49` and `TOOL-dWitnessedBar-27` share order 2, and
unit 27 builds first; this unit and `TOOL-dWitnessedBar-49` both write
`tools/run-gates/measure_legs.py`, so the main loop sequences those two within the group
(BUILD-METHOD M6, clause 1).

### Files touched (estimate)

- `tools/memory-tree/row_grammar.py`
- `tools/run-gates/measure_legs.py`

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
- **AC2** — When `scan_bare_bash` is called from `measure_legs.py` (imported with `tools/run-gates`
  on `sys.path`) with the root of a fixture repo under `%TEMP%` tracking one `.py` with a list of a
  `GOV_BASH` read, the constant `bash` and Git's own bash.exe path, and one `.js` holding
  `const x = 1;`, it names that `.py` line; with a fixture repo tracking the same `.js` and one `.py`
  holding `if argv[0] not in ("bash", "bash.exe"): pass` it returns `[]`.
  Red when: shape 2 misses the GOV_BASH-headed list, or flags a membership test.

## 7. Gates

`measure-legs selftest` · `row-grammar selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `policy fixtures` · `memory hygiene`

`row-grammar selftest` runs `cmd_selftest`, the only caller of the adapter S1 makes.

New arm: tools/run-gates/measure_legs.py · covers AC2 · `test_no_bare_bash_argv` over the two fixture literals, staged red by planting the GOV_BASH-headed list in a tracked `.py` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-26`'s clause. (b) reds the parts
  join; veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Does S3's membership rule stay once its one instance is gone?** Unit 26 rewrote
  `resolve_shell_argv` to test `argv[0]` against `BASH_NAMES`, so no tracked comparator holds a literal
  pair at `88352ca5`. Options: (a) keep S3, so shape 2 skips a membership comparator and AC2's second
  fixture observes it; (b) drop S3 and AC2's second fixture, so a membership literal is listed as a
  launch and answered by reading `BASH_NAMES`, as unit 26's F5 did. (b) fails AC2 as written, veto 1,
  and strands `TOOL-dWitnessedBar-51` S18, which consumes the rule; and a fork is not decided by a
  signal reading zero (M3's counter-rule). RESOLVED (agent, 2026-11-19, delegated): (a), the one
  option M3's veto 1 leaves. widens: none · relaxes: shape 2 stops listing a membership comparator
  holding both names, which the shape at `88352ca5` lists; none is tracked there

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's id 27 (HIGH, item H9).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-57, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.
- rev-3 · 2026-11-19 · §6 §7 · AC2 observes `scan_bare_bash` on two fixture repos instead of spelling
  the `measure-legs selftest` suite, which stays on the New arm line; the leg line gains
  `policy fixtures`, whose manifest guard holds the §4 path `tools/memory-tree/row_grammar.py`, per
  brief 2026-11-19-prompt-TOOL-dWitnessedBar-27-spec-tokens-brief; nothing else moved.
- rev-4 · 2026-11-19 · §1 §2 §3 §4 §6 §7 §8 §10 · S3 AC2 · re-grounded on unit 26 as landed at
  `88352ca5`: citations re-pinned as `path#symbol` or blob-pinned; S3 names `resolve_shell_argv` in
  `upgrade_steps.py` reading `BASH_NAMES`, and F2 keeps its rule; §4 Evidence re-derives the widened
  shape's population and drops `resolve-python.test.sh` from Files touched, its parity row finding the
  copy by marker; AC2's fixtures each track one `.js`, which the scan now requires; the leg line gains
  `row-grammar selftest`; unit 27 builds first, per brief
  2026-11-19-prompt-TOOL-dWitnessedBar-48-reground-brief.

## 10. Reuse audit

The seams are unit 26's `resolve_bash_py` block, carried to one more site under its parity row, and
`scan_bare_bash` (`tools/run-gates/measure_legs.py#scan_bare_bash`), widened in place; both re-verified
at `88352ca5`. `python tools/codebase-map/reuse_lookup.py "find every bash candidate list a python file
probes"`, re-run 2026-11-19, ranked `probe`, `resolve_bash` (the adapters unit 26 landed),
`run_probe` and generic file and list readers; it did not surface `resolve_shell_ere`, which the
report's grep found, so the map's blind spot is the nested function this unit adapts.

Recall terms used: `python tools/memory-recall/query.py "which python resolvers probe a bash candidate list" --terms "resolve_shell_ere row_grammar bash candidates GOV_BASH bare bash scan_bare_bash shape loop WSL launcher"`
