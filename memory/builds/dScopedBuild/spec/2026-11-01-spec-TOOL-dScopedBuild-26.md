# TOOL-dScopedBuild-26 — `reuse_check.py` reads its two policy keys through the memory-tree adapter, a call the `.py` reader shape counts

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 14 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 |
| [2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-30 TOOL-dScopedBuild-28 TOOL-dScopedBuild-34 TOOL-dScopedBuild-27 TOOL-dScopedBuild-29 TOOL-dScopedBuild-31 TOOL-dScopedBuild-25 TOOL-dScopedBuild-35 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 1 to 15
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md`)
confirmed finding **id 2 at HIGH**, report item **H2**. `TOOL-dScopedBuild-12` S4 and S8 have
`tools/codebase-map/reuse_check.py` read `build.reuse-check.second-pass` and `flow.route-backs` "as
`policy.py get <key>`" by subprocess, and its AC15 and AC11 only `git grep` the text `get <key>`. The
`.py` reader shape needs an identifier, `(`, then the key as a quoted first argument
(`tools/policy/check_policy.py:426-427`), so an argv-list `subprocess.run([py, cli, "get", key])`
yields nothing, while a comment can satisfy the grep. Either way the owned key has no counted reader
and the policy check reds at the build's close.

This unit has `reuse_check.py` call the memory-tree kit's one key reader with each key a literal
first argument, makes a refused read the CLI's exit 2, and asks the arm itself in place of the greps.
It repairs `TOOL-dScopedBuild-12` and builds one step after it (order 14).

## 2. Scope (IN)

- **S1** — The reader. `reuse_check.py` reads both keys through `read_policy_value(key, root)` in
  `tools/memory-tree/policy_value.py`, TOOL-dTotalRecall-8 S10's adapter, built to
  PLAY-dOrderedCharter-7 §4 "The policy reads". The module is loaded the way unit 12 S2 loads
  `routed_commits`, through the kit's inline `resolve_kit_dir("memory-tree", ...)` and `sys.path`; the
  codebase-map kit declares `requires = ["memory-tree"]` (`tools/codebase-map/kit.toml:7`). The calls
  are `read_policy_value("build.reuse-check.second-pass", root)` in `question` and `join` (unit 12 S4,
  S7) and `read_policy_value("flow.route-backs", root)` in `bound` (S8), each key a string literal
  first, on a line that does not open `#`. This supersedes unit 12 S4's and S8's "read as `policy.py
  get <key>`". Observed by AC1.
- **S2** — The value checked where it is used. The value is the adapter's first line. `second-pass`
  must be `off` or `on`, and `route-backs` a non-negative integer; anything else, and a
  `PolicyRefused` the adapter raises, is the CLI's exit 2 with one line naming the key and the
  reason. No default is read in its place. Observed by AC2.
- **S3** — Unit 12 AC15's third clause and AC11's last clause, each a `git grep -c 'get <key>' --
  tools/codebase-map/` that prints at least 1, are superseded by AC1. Their other clauses stand.
  Unit 12's acceptance ledger answers AC11 and AC15 with a note naming `TOOL-dScopedBuild-26 S3`.
  Observed by AC1.

## 3. Non-goals (OUT)

- A codebase-map copy of the adapter. The kit requires memory-tree, and its `policy_value.py` is the
  kit-local reader TOOL-dTotalRecall-8 §8 F4 rules for; a third reader would be the defect id 19
  names for unit 14.
- Unit 12's values, its `of 2` header and its bound. S2 refuses only what unit 12 never branches on.
- The left-shift gate the report names. No clause of this build names it.
- Rewording unit 12's spec text; each clause is superseded by name.

### Edges

- **consumes-from** `TOOL-dScopedBuild-12` — S4, S7 and S8's two policy reads in `reuse_check.py`, and AC11's and AC15's grep clauses, which S1 to S3 respell and supersede (id 2)
- **consumes-from** external — TOOL-dTotalRecall-8 S10's `read_policy_value` and `PolicyRefused` in `tools/memory-tree/policy_value.py`, DEFERRED at base and an ancestor's, landed before this build runs
- **hands-off** `TOOL-dScopedBuild-39` — S1 and S2's reads, AC1, §4 Inventory and §7's first arm line, which that unit's S6, S7, S18, S20, S21 and S29 complete, the second-pass read spelled through `check_gate_value` (ids 4, 12, 27, 8, 19, 25)

## 4. Design

### Evidence

- `READER_SHAPES`' first row (`tools/policy/check_policy.py:426-427`) matches
  `<identifier>(<quoted key>`; a call `read_policy_value("flow.route-backs", root)` is counted, and a
  list `[py, cli, "get", "flow.route-backs"]` is not, as the report's skeptic probed.
- `scan_reader_keys` (`:479-500`) skips lines opening `#`, so a comment carrying the key text is not a
  reader, and `selftest*.py` and `test_*.py` files are not read.
- PLAY-dOrderedCharter-7 §4 "The policy reads" (`memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md:196-211`)
  gives the contract: `get <key> --explain` run with `root` as its working directory, the stdout lines
  returned, `PolicyRefused` on exit 2 or a missing kit. `get` checks a value against the catalogue
  row (`tools/policy/policy.py:596`), so S2's check refuses only a value a future row widens past
  what this module branches on.
- The kit already reaches a sibling module through the inline resolver
  (`tools/codebase-map/map_extractors.py:271-274`), which the audit's refuted id 24 records.

### Inventory

Minted: nothing. `read_policy_value` is TOOL-dTotalRecall-8's; S2's check is inline at the two
reads. No lexicon cell applies.

### Migration

None: no stored data changes.

### Rollout

Built at order 14, one step after unit 12 (order 13). The adapter is an ancestor's and lands first.

### Files touched (estimate)

- `tools/codebase-map/reuse_check.py`

### Alternatives rejected

- **A local wrapper around the subprocess, the report's first form.** It mints a third key reader
  beside the memory-tree and playbook adapters, the shape id 19 refuses for unit 14.
- **Keep the subprocess and add a reader shape for argv lists.** The arm would count any list holding
  `"get"`, which no other consumer spells, and the module would still read no `PolicyRefused`.

## 5. Production-readiness checklist

- security — no new write path; the reads are at the landed revision, as `get` reads them.
- perf / scale — one `get` per key per CLI call, as unit 12 already pays.
- error / empty / loading states — a refused or unknown value is exit 2 naming the key (S2).
- observability — the refusal line names the key and the adapter's stderr line.
- risks — a builder keeping the subprocess passes no criterion here: AC1 asks the arm.
- testing — AC1 by probe over the built tree, AC2 through the module's fixture.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys; sys.path.insert(0, 'tools/policy'); import check_policy;
  k = check_policy.scan_reader_keys('.'); print('build.reuse-check.second-pass' in k,
  'flow.route-backs' in k)"` runs on the built tree, it prints `True True`.
  Red when: either read is an argv list, or only a comment spells the key.
  figure: DERIVED at observation; at base `f4597719` the set holds neither key.
- **AC2** — When `python reuse_check.py question` runs in unit 12's fixture with `read_policy_value`
  stubbed to raise `PolicyRefused`, it exits 2 printing `build.reuse-check.second-pass`; with the stub
  returning `["maybe"]` it exits 2 naming the value; with `["on"]` its header reads `of 2`.
  Red when: a refused or unknown value reads as `off`, or the CLI exits 0 or 1 on it.
  fixture: unit 12's `reuse_check.py --fixture` tree, with the adapter stubbed in-process.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `policy check` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/policy/check_policy.py · covers AC1 · reader coverage over both keys once dScopedBuild lands, staged by respelling one read as an argv list · none

New arm: tools/codebase-map/reuse_check.py · covers AC2 · the fixture's refused, unknown and `on` reads, staged by defaulting a refused read to `off` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause.
  (b) splits cl-dClosedLoop-0410, which unit 12 carries whole. RESOLVED (agent, 2026-11-01,
  delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-91` §8 F1 set. widens: none · relaxes:
  none
- **F2 — Which reader does `reuse_check.py` call?** Options: (a) the memory-tree adapter, loaded
  through the kit's declared requirement; (b) a codebase-map wrapper of its own, the report's first
  form. (b) mints a third reader of one question, the defect id 19 names. RESOLVED (agent,
  2026-11-01, delegated): (a), rung 3, the survivor that reuses a seam the build already depends on.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 1 to 15, id 2
  (HIGH, item H2).
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-39,
  the promotions of the round-1 spec audit of units 25 to 35 (ids 4, 8, 12, 19, 25, 27).

## 10. Reuse audit

The seam extended is TOOL-dTotalRecall-8 S10's `read_policy_value` in
`tools/memory-tree/policy_value.py`, the memory-tree kit's one policy reader, reached through the
inline `resolve_kit_dir` the codebase-map kit already uses for sibling modules
(`tools/codebase-map/map_extractors.py:271-274`).
`python tools/codebase-map/reuse_lookup.py "read a policy key from a python module of another kit by
subprocess"` ranked `read`, `read_text`, `key`, `keys` and `resolve_kit_dir`; only the last is a
seam here, and the adapter is not in the tree at base, so the map cannot see it.

Recall terms used: `python tools/memory-recall/query.py "how does a python module of the codebase-map kit read a policy key" --terms "read_policy_value policy_value.py PolicyRefused codebase-map memory-tree adapter resolve_kit_dir reader coverage literal"`
