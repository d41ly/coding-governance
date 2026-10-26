# TOOL-dDeclaredLoop-99 — every `loop_lib.py` function that opens a conf is in `CONF_READERS`, checked both ways by a definition plant

**Status:** DEFERRED · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 50 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-99-deviation-991.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-99-deviation-991.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-12 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md`)
confirmed finding **id 19 at HIGH**, in its item **H1**. Ids 1 and 11 share that item, and each is its
own unit: `TOOL-dDeclaredLoop-97` (id 1) and `TOOL-dDeclaredLoop-98` (id 11).

Id 19 is the failure envelope of H1. 87 §3 and 89 S5 send a conf read made through a function call to
82's `reader call` kind. That kind names its readers by hand, so a reader minted later, as 95 mints
`read_tree_conf`, escapes the rule until someone adds its name. 82's `conf constant` kind does not catch
it either, because the path is built inside the function. 97 gives the rule one tuple,
`CONF_READERS`. Nothing yet checks that the tuple keeps up with `loop_lib.py`.

This unit derives, from the syntax of `loop_lib.py`, the functions that build a conf path and open it,
and compares that set with `CONF_READERS` both ways in a plant of `loop_lib.py --fixture`. The next
reader that `loop_lib.py` gains then reds the `loop definition fixtures` leg until it is declared, and
the `reader call` kind that 87 and 89 rely on covers it. It builds immediately after 95, beside 97, and
repairs `TOOL-dDeclaredLoop-95`.

## 2. Scope (IN)

- **S1** — `derive_conf_openers(loop_lib_path)` in `tools/loop/loop_lib.py` parses that file with `ast`
  and never imports it. It answers the sorted names of the module-level `FunctionDef` and
  `AsyncFunctionDef` nodes outside 80 S1's fixture boundary whose own body meets both tests below.
  Nested function and class definitions are not part of a body.
  - **Builds a conf path**: an operand of a `/` `BinOp`, or an argument of a call whose callee is named
    `join`, `Path` or `PurePath`, is a str `Constant` containing `.memory-tree.conf` or
    `.unattended.conf`, or a `Name` or `Attribute` naming a member of `derive_conf_constants(loop_lib_path)`.
  - **Opens content**: it holds a call whose callee, a `Name` or an `Attribute`, is named `parse_conf`,
    `open`, `read_bytes` or `read_text`, or any call of an attribute of the name `subprocess`, which is
    how 70 S1 sources the driver's conf.
  Observed by AC2.
- **S2** — The plant `conf-readers-declared` joins `loop_lib.py --fixture`, so the
  `loop definition fixtures` leg (67 S30) runs it. It compares S1's answer over its own module file
  with `CONF_READERS` and fails, exiting non-zero, in three cases:
  - a derived opener missing from the tuple: `<name> opens a conf and is not in CONF_READERS`;
  - a tuple member S1 does not derive: `<name> is in CONF_READERS and opens no conf`;
  - an empty derived set: `no conf opener found in loop_lib.py`, so a predicate that matches nothing
    cannot pass.
  On a pass it prints `conf readers declared: <n> — <names>`. Observed by AC1, AC3.
- **S3** — 87 §3's bullet "A conf path a function builds and returns, read through a call" and 89 S5's
  sub-bullet "a `def` or `class` name, read through a call" name the `reader call` kind over
  `CONF_READERS` (97 S2), which this unit's plant keeps complete, in place of "82's `reader call`
  kind". These land in this unit's rev bumps of 87 and 89, each with its §9 line. Observed by AC4.

## 3. Non-goals (OUT)

- The tuple and the rule reading it: id 1's mechanism, `TOOL-dDeclaredLoop-97`.
- The plant row proving that the rule answers each member: id 11's mechanism, `TOOL-dDeclaredLoop-98`.
- A conf read in `budget.py` or `breakpoints.py` themselves: the `no-own-conf-read` plant's (76 S3).
- A reader whose conf path is built in one function and opened in another, or a conf name composed at
  run time, such as `"." + "unattended.conf"`. S1 reads one body at a time and constant text only. A
  declared member split this way still reds the second case of S2, and an undeclared one is missed.
  76 §5 records the run-time composition gap for the rule itself.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-97` — `CONF_READERS`, which S2 compares both ways with S1's derived openers (the round-12 spec audit's ids 1, 19)
- **consumes-from** `TOOL-dDeclaredLoop-80` — S1's fixture boundary, outside which S1 derives the openers (the round-12 spec audit's id 19)
- **consumes-from** `TOOL-dDeclaredLoop-87` — `derive_conf_constants` as S1 states its class, whose members count as a conf path in S1, and §3's bullet on a conf read through a call, which S3 restates (the round-12 spec audit's id 19)
- **consumes-from** `TOOL-dDeclaredLoop-89` — S5's sub-bullet on a `def` or `class` name read through a call, which S3 restates (the round-12 spec audit's id 19)
- **consumes-from** `TOOL-dDeclaredLoop-67` — S30's `loop definition fixtures` leg, argv `loop_lib.py --fixture`, which runs S2's plant (the round-12 spec audit's id 19)
- **hands-off** `TOOL-dDeclaredLoop-100` — the `conf-readers-declared` plant, which that unit re-runs over the `read_tree_conf` body it rewrites (the round-12 spec audit's ids 10, 19, 20)

## 4. Design

### Evidence

Read or probed 2026-10-24 at the worktree tip on node `d`: PINNED, that date.

- 87 §3 (line 70) reads "A conf path a function builds and returns, read through a call: 82's
  `reader call` kind is the route for a call". 89 S5 (line 80) lists "a `def` or `class` name, read
  through a call (82's `reader call` kind)". Over 87's §3 range and 89's S5 range,
  `grep -c CONF_READERS` prints 0.
- 82 S10 (line 102) matches a `reader call` by the names `parse_conf` and `read_driver_conf` alone, as
  76 S2 (line 41) does.
- The conf readers the build specifies: 70's `read_driver_conf` builds `tree/.unattended.conf` and
  sources it in a bash subprocess (`TOOL-dDeclaredLoop-70` sketch, line 99; 79's sketch, line 197).
  95's `read_tree_conf` builds `tree / ".memory-tree.conf"` and calls `parse_conf` (`TOOL-dDeclaredLoop-95`
  sketch, line 119).
- `resolve_memory_root_source` builds both conf paths for its existence tests (95 S3, 82 S15) and opens
  neither itself. `derive_conf_reads` and `derive_conf_constants` hold the conf names as constants they
  compare against, never as path operands.
- 67 S30 (line 170) mints `loop definition fixtures`, argv `python {prefix}/loop/loop_lib.py --fixture`.
- 80 S1 (line 32) is the fixture boundary: a function whose name, split on `_`, holds `fixture` or
  `plant`.
- `tools/loop/` is absent at base, so every function this unit touches is sibling-minted.

### The check, after this unit

```
derive_conf_openers(loop_lib_path):
    tree   = ast.parse(read(loop_lib_path))                  # parsed, never imported
    consts = derive_conf_constants(loop_lib_path)            # 87 S1's class, 86 S13's refusal
    for each module-level FunctionDef | AsyncFunctionDef outside 80 S1's boundary:
        body = its nodes, nested FunctionDef, AsyncFunctionDef and ClassDef excluded
        builds = a conf-name str Constant, or a Name | Attribute in consts, as an operand of a "/" BinOp
                 or an argument of a call named join | Path | PurePath
        opens  = a call named parse_conf | open | read_bytes | read_text, or a call of subprocess.<any>
        builds and opens -> answer its name
    return sorted names

plant conf-readers-declared:
    derived = derive_conf_openers(this file) ; declared = CONF_READERS
    derived empty          -> fail "no conf opener found in loop_lib.py"
    derived - declared     -> fail "<name> opens a conf and is not in CONF_READERS"
    declared - derived     -> fail "<name> is in CONF_READERS and opens no conf"
    print "conf readers declared: <n> — <names>"
```

### Write set

This pass writes `tools/loop/loop_lib.py` (S1, S2). `derive_conf_openers` is a public module-level `def`,
so `memory/map/generated/symbols.json` gains its row. Inside this build's folder it amends the specs of
87 and 89 as rev bumps, one per spec, each with its §9 line (S3). The build README's regions are the
generator's render.

### Inventory

- `derive_conf_openers` — a public function in `tools/loop/loop_lib.py`, one row in
  `memory/map/generated/symbols.json`.
- `conf-readers-declared` — a plant name of `loop_lib.py --fixture`.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `memory/map/generated/symbols.json`
- `memory/builds/dDeclaredLoop/spec/`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **Leave the tuple hand-kept, with no check (97 alone).** The tuple then drifts exactly as the
  two-name pair did, and the next reader repeats H1. The report's left-shift asks for this check.
- **Derive the rule's reader set from S1 and drop the tuple.** The rule would then rest on a heuristic
  with no declared answer to compare against, and a predicate miss would shrink the rule silently. A
  declared tuple checked both ways turns a miss into a red.
- **Class a function as a reader when its body names a conf at all.** `resolve_memory_root_source`,
  `derive_conf_reads` and `derive_conf_constants` all name both confs, so the sanctioned route and the
  rule itself would be readers. S1 requires the name as a path operand and an open call in one body.
- **Follow calls, so a function calling a reader is a reader.** `resolve_memory_root_source` calls both
  readers and returns a resolved root. Following calls would class it as a reader and red the readers'
  sanctioned route.

## 5. Production-readiness checklist

- security — the readers' no-own-conf-read rule keeps covering every conf reader `loop_lib.py` gains,
  so the `confs-disagree` refusal (72 AC3) cannot be bypassed by a new reader.
- perf / scale — one `ast.parse` of `loop_lib.py` and one `derive_conf_constants` call per plant run.
- error / empty / loading states — an empty derived set fails by name, and a missing or unparseable
  `loop_lib.py` is 86 S13's refusal.
- observability — the pass line names every declared reader, and each failure names the function and
  the direction of the mismatch.
- risks — S1 is syntactic. §3 names its two blind spots, a path built in another function and a conf
  name composed at run time. A declared member split across functions still reds.
- testing — AC1 to AC4 as a plant run, a probe of S1, staged breaks and greps.
- migration — none: `tools/loop/` is unbuilt at base.
- user docs — none: no adopter-facing command or flag moves.

## 6. Acceptance criteria

- **AC1** — When `python loop_lib.py --fixture --plant conf-readers-declared` runs in `tools/loop/`, it
  exits 0 printing `conf readers declared: 2 — read_driver_conf read_tree_conf`.
  Red when: the plant is absent, or passes on a derived set that matched nothing.
  figure: 2 is DERIVED from `loop_lib.py` at observation time.
- **AC2** — When `python -c "import loop_lib as ll; print(ll.derive_conf_openers('loop_lib.py'))"` runs
  in `tools/loop/`, it prints `['read_driver_conf', 'read_tree_conf']`. Neither
  `resolve_memory_root_source`, `derive_conf_reads`, `derive_conf_constants` nor `derive_conf_openers`
  is in the list.
  Red when: the predicate classes the readers' sanctioned route or the rule itself as a reader, or
  misses a reader the build specifies.
- **AC3** — Take scratch copies of `tools/loop/`, `tools/lib/` and `tools/memory-tree/` under the run's
  scratch directory, and run `python loop_lib.py --fixture --plant conf-readers-declared` in each copy's
  `loop/`:
  - a copy whose `loop_lib.py` gains `def read_other_conf(tree): return (tree / ".unattended.conf").read_bytes()`
    exits non-zero printing `read_other_conf opens a conf and is not in CONF_READERS`;
  - a copy whose `CONF_READERS` also holds `resolve_memory_root` exits non-zero printing
    `resolve_memory_root is in CONF_READERS and opens no conf`;
  - a copy whose `loop_lib.py` gains the same reader named `seed_fixture_conf` exits 0, because 80 S1's
    boundary passes over it.
  Red when: a new conf reader in `loop_lib.py` passes undeclared, the report's consequence for id 19.
  fixture: the copies are made at observation time.
- **AC4** — When `awk '/^## 3/,/^### Edges/'` over the 87 spec and `awk '/^- \*\*S5\*\*/,/^## 3/'` over the
  89 spec are each piped to `grep -c CONF_READERS`, each prints at least 1.
  Red when: 87 and 89 still send a function's conf read to a kind that names its readers by hand.
  figure: each prints 0 at HEAD, PINNED 2026-10-24.

## 7. Gates

`recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted loop leg this pass keeps green, outside the base manifest, declared by the unit that
mints it: `loop definition fixtures`, not a leg at HEAD.

New arm: tools/loop/loop_lib.py · covers AC1 AC3 · the conf-readers-declared plant, staged with an undeclared reader and with a declared member that opens no conf · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Keep the tuple complete by a derived check, or derive the rule's set directly (id 19)?** (a) a
  plant comparing a syntactic derivation with `CONF_READERS` both ways; (b) the rule reads the
  derivation and no tuple exists. (b) loses the declared answer, so a predicate miss shrinks the rule
  with no signal. (a) turns a miss in either direction into a named red, as the report's left-shift
  states. RESOLVED (agent, 2026-10-24, delegated): (a), S1 and S2.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-12 spec audit's id 19 (HIGH, item H1,
  shared with ids 1 and 11).

## 10. Reuse audit

The seams are 86's and 87's `derive_conf_constants`, read for the conf-constant operand, 80 S1's fixture
boundary, read as stated, and the `loop_lib.py --fixture` plants that 67 S30's leg runs, extended by one
plant. S1's walk is the same `ast` walk shape as `derive_conf_reads`, and it reads one body where that
rule reads a module.
`python tools/codebase-map/reuse_lookup.py "check that every function which opens a conf file is listed in a declared tuple"`
ranked `check`, `load_conf`, `parse_conf`, `opened` (`tools/memory-recall/recall-opened.test.sh`),
`read_conf` and `read_conf_key`. None of these classifies the functions of a module by what they open,
so no existing seam fits S1's predicate. The memory-recall query returned the round-12 report's H1, 76's
spec, 80's fixture boundary and 82's sketch.

Recall terms used: derive_conf_reads reader call read_driver_conf read_tree_conf parse_conf no-own-conf-read plant callee set conf readers tuple
