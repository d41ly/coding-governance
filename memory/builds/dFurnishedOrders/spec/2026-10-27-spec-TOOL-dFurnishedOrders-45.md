# TOOL-dFurnishedOrders-45 — the fourth spec audit's 8 upgrade-step minors: a copied kit.toml matched on its own `home`, a top level compared as a file, every git child stripped of the leaking variables, live fixtures, one tool-root search and a deploy descriptor refused by name

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 47d3a464 · streams tooling · order 26 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-45-deviation-451.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-45-deviation-451.md) | deviation | — |
| [2026-10-27-review-TOOL-dFurnishedOrders-43-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-43-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-43 TOOL-dFurnishedOrders-44 TOOL-dFurnishedOrders-46 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-3 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md`)
confirmed 13 MEDIUM and 13 LOW findings. BUILD-METHOD M4 batches them, and they split into two
disjoint write sets by M6 (§4 "Why two units"): this unit takes the 8 that land on the govkit upgrade
step and its suite, and `TOOL-dFurnishedOrders-46` takes the other 18. Each report id is named once
below and closed by its own scope item; ids the report merged into one item still take one scope
item each.

| Report item | Report id | Severity | Lands on | Scope item |
|---|---|---|---|---|
| M1 | 25 | MEDIUM | unit 40 S1, §4; unit 41 S6 | S1 |
| M5 | 9 | MEDIUM | unit 41 S2, §4 | S2 |
| M5 | 31 | MEDIUM | unit 41 S2 | S3 |
| M12 | 32 | MEDIUM | unit 41 S2, §5 | S4 |
| L2 | 5 | LOW | unit 40 AC2, AC3; unit 41 AC3, AC5 | S5 |
| L5 | 13 | LOW | unit 40 §4 | S6 |
| L7 | 18 | LOW | unit 41 S5, §10 | S7 |
| L10 | 27 | LOW | unit 40 S1, S4, §5 | S8 |

## 2. Scope (IN)

- **S1** — id 25. A copied `kit.toml` matched on the `home` it spells. `read_descriptors` stores each
  descriptor through `resolve_descriptor_paths` (`tools/govkit/govkit.py:13232-13280`), which joins
  `home` to gov's tool root. Unit 41 S6 compares a target `kit.toml`'s `home` with gov's descriptor
  `home` as the descriptor file spells it: gov's joined value with gov's tool root and its slash
  stripped, `.` where the joined value is the tool root itself, and the value unchanged for a
  descriptor declaring `home_root_relative = true`. No target home in the step is built from
  `desc["home"]` and a target prefix; unit 43 S1 reads `desc["home"]` only as gov's own source
  directory. Observed by AC1.
- **S2** — id 9. A top level compared as a file, not as a string. Unit 41 S2's refusal compares
  `<target>` with `git -C <target> rev-parse --show-toplevel` by `os.path.samefile`, so the 8.3 short
  spelling of a top level that git prints long (`tools/run-gates/regen.py:281-283`) is that top level.
  Observed by AC2.
- **S3** — id 31. The same compare accepts `.` and a backslash spelling of a top level, and refuses
  a subdirectory as unit 41 AC2 states. Observed by AC2.
- **S4** — id 32. Every git child of the step runs without the leaking variables. The step carries the
  `git_env_leaks_py` block inline (`tools/lib/git_env_leaks.py:13`, under its row of
  `tools/lib/resolve-python.test.sh:185`), and every git child it starts, the `rev-parse` of unit 41 S2
  and the `ls-files` population read of unit 37 S23 included, runs with an environment holding none of
  the twelve `GIT_ENV_LEAKS` names. Unit 41 §5's security line holds with this item. Observed by AC3.
- **S5** — id 5. The fixtures select what they claim. Every adopter suite or script the `selftest.py`
  arms of unit 40 AC2 and AC3 and of unit 41 AC3's second and third cases and AC5 plant names
  `unattended-unit.js` and passes `checklist: 'x'`, as unit 25 S2's call-site predicate requires; and
  each such arm also runs a control copy of its fixture whose plant lacks only `unattended-unit.js` and
  expects exit 0. Unit 40's and unit 41's ledgers answer those criteria in the AMENDED form, naming this
  item. Observed by AC4.
- **S6** — id 13. The descriptor read unpacked. Every read of `read_shipped_descriptors` in the step
  takes the `(descriptor, descriptor path)` pair its signature returns (`tools/govkit/govkit.py:13283`),
  as `cmd_shipped` (`:13313-13315`) does; unit 43 S1 spells it so. Observed by AC5.
- **S7** — id 18. One tool-root search. `derive_tool_root` (`tools/govkit/govkit.py:154-175`) gains a
  keyword `tracked=False`; with `tracked=True` its candidates, on both branches, are the
  `govkit/registry.toml` paths at depth 0 to 2 that `git -C <root> ls-files` lists, and it refuses on
  none or more than one as it does today. Unit 41 S5's step calls `derive_tool_root(target,
  tracked=True)` and holds no search of its own. Observed by AC6.
- **S8** — id 27. A deploy descriptor refused by name. A target `.governance/deploy.toml` the step
  reads through `load_toml` (`tools/govkit/govkit.py:285-292`), which refuses bad TOML naming the file;
  and whose `kit` value is not a table, or whose `kit.<eid>` for a receipt kit is not a table, refuses
  the step at exit 1 naming the file and the key, before any scan and before `target_context`
  (`:1462`) reads it. Observed by AC7.

## 3. Non-goals (OUT)

- The HIGH findings of the same report: `TOOL-dFurnishedOrders-43` and `-44`.
- The other 18 minors: `TOOL-dFurnishedOrders-46`.
- Rewording the spec text of units 40 and 41: each item states the built tree's end state, and where a
  landed criterion cannot hold as written, that unit's ledger answers it AMENDED, naming the item.
- The report's left-shift gates, the spec-lint and checklist entries: no clause of this build names
  them.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-40` — S1's home sketch, S4's prefix read, §5 and AC2 and AC3's fixtures, which S1, S5, S6 and S8 settle (ids 25, 5, 13, 27)
- **consumes-from** `TOOL-dFurnishedOrders-41` — S2's top-level refusal, S5's tool-root search, S6's `kit.toml` compare and AC3 and AC5's fixtures, which S1 to S5 and S7 settle (ids 25, 9, 31, 32, 5, 18)
- **consumes-from** `TOOL-dFurnishedOrders-43` — `derive_receipt_homes`, whose deploy read and descriptor unpack S6 and S8 hold (ids 13, 27)
- **hands-off** `TOOL-dFurnishedOrders-48` — S4's environment, S7's tracked search, S8's shape guard and AC3, AC5, AC6 and AC7, which unit 48 S4 to S9, S19, S20, S25 and S26 settle (ids 2, 31, 3, 19, 24, 30, 13, 22, 32, 18 of the fifth audit)
- **hands-off** `TOOL-dFurnishedOrders-49` — §4 clause 1's write-set record, which unit 49 S1 re-reads from the pass commits (id 6 of the fifth audit)

## 4. Design

### Why two units

M6 admits two batch units when their write sets are disjoint by all three of its clauses, and these
minors split that way:

- **Clause 1.** This unit writes `tools/govkit/steps/retired_dispatch_args.py`,
  `tools/govkit/selftest.py` and `tools/govkit/govkit.py`; unit 46 writes the roles, run-gates,
  process-monitor and unattended kits, `tools/gate-legs.json`, `.lexicon.conf` and the kickoff
  manifest. No path is in both, and this unit writes no path on `memory/guides/SESSION-KICKOFF.md`'s
  `watch:` line, so the one re-stamp is unit 46's.
- **Clause 2.** Neither reads a file the other writes as a contract or an acceptance input. Unit 46
  S8's guard rows name the files the govkit arms read; this unit's arms read no sibling-kit file
  beyond `{prefix}/memory-recall/kit.toml`, which S8 already names, and add planted fixtures and a
  control copy of each.
- **Clause 3.** Neither touches `memory/DECISIONS.md`, a backlog shard, the run-state file or a
  generated index with its generator: unit 46 S15's ask rows are filed by the main loop.

### How an item closes

Each item states the built tree's end state, and the pass does what is missing or records that a
landed unit already left it so, as `TOOL-dFurnishedOrders-41` §4 does.

### The step's reads, after this unit

```
deploy.toml   := load_toml(...)          bad TOML, kit not a table, kit.<eid> not a table -> exit 1   S8
genv          := os.environ minus every GIT_ENV_LEAKS name, for every git child                     S4
top           := git -C <target> rev-parse --show-toplevel (env genv)
samefile(<target>, top) false             -> exit 1 naming both                                      S2 S3
tool root     := derive_tool_root(target, tracked=True)                                              S7
descriptor    := desc, _src = read_shipped_descriptors(gov_root)[eid]                                S6
kit.toml home := matched against the descriptor file's own home spelling                            S1
```

### Inventory

Minted: the keyword `tracked` of `derive_tool_root`. No function, flag or file; the inline
`git_env_leaks_py` block is a copy of an existing canonical.

### Migration

None: the steps have never run, and `derive_tool_root`'s default answers as it does today.

### Rollout

Live at landing, at order 26, after every unit it lands on and beside unit 46. govkit's version moves
for the kit epoch leg where the step ships under it.

### Files touched (estimate)

- `tools/govkit/steps/retired_dispatch_args.py`
- `tools/govkit/selftest.py`
- `tools/govkit/govkit.py`

### Alternatives rejected

- **`pathlib.Path.resolve()` equality (S2).** It also expands 8.3 names, but it compares spellings
  after a normalisation, and `samefile` compares the file the two spellings open.
- **Strip only `GIT_DIR` and `GIT_WORK_TREE` (S4).** A leaked `GIT_INDEX_FILE` or
  `GIT_OBJECT_DIRECTORY` still points the population read at another index or store.
- **Keep unit 41 S5's own search (S7).** Every other caller of `derive_tool_root` keeps counting an
  untracked or ignored copy, and the two searches drift.

## 5. Production-readiness checklist

- security — S4 keeps a hook's leaked git variables out of every child; S8 refuses a malformed target
  descriptor by name before any value reaches `target_context`.
- perf / scale — one `ls-files` read inside `derive_tool_root` when `tracked` is set.
- error / empty / loading states — S2's refusal names both spellings; S8 names the file and key.
- observability — every refusal names its cause on stderr, and the scan line is unchanged.
- risks — S7 changes no existing caller, whose default stays the filesystem glob.
- testing — AC1 to AC7 by fixtures and probes; the arm of §7 at the close.
- migration — none.
- user docs — none: the step's printed lines are what the walk shows.

## 6. Acceptance criteria

- **AC1** — When `witness <target> checklist` runs over a scratch target with no receipt that tracks a
  copy of `tools/memory-recall/kit.toml` under `<target>/scripts/recall/` beside a suite named
  x.test.sh there naming `unattended-unit.js` and spelling `"checklist":`, it exits 0; with the copy's
  `home` changed to `elsewhere`, it exits 1 naming that suite.
  Red when: the copy's spelled `home` is compared with gov's joined value and never matches.
  fixture: scratch targets under `%TEMP%`, built by the pass.
- **AC2** — When the step, retired_dispatch_args.py at unit 41 S1's path, runs `witness . checklist`
  from the repository root, and again with the target spelled as the root's absolute path with
  backslashes, each exits 0 with a scan line; and where the volume holding `%TEMP%` gives a scratch
  target an 8.3 short name, `witness` over that spelling exits 0 too.
  Red when: a string compare refuses a valid top level.
  fixture: the 8.3 arm needs a volume with short names enabled, which node `a` has
  (`tools/run-gates/regen.py:281-283`); the `.` and backslash arms run on every node.
- **AC3** — When `witness <target> checklist` runs over a scratch target holding one call site with
  `GIT_INDEX_FILE` set to the index of a second scratch repository holding none, it prints the same
  hit and the same scan line as without the variable.
  Red when: a leaked variable points the population read at another index.
  fixture: two scratch repositories under `%TEMP%`, built by the pass.
- **AC4** — When each fixture of unit 40 AC2 and AC3 and of unit 41 AC3's second and third cases and
  AC5 runs as S5 states, the planted copy exits 1 naming its plant and the control copy lacking
  `unattended-unit.js` exits 0.
  Red when: a criterion expecting exit 1 passes or fails for a reason other than its plant.
- **AC5** — When `git grep -n -E "read_shipped_descriptors\([^)]*\)\[" -- tools/govkit/` runs, it
  prints nothing.
  Red when: the step indexes the call's result as if it were a descriptor.
- **AC6** — When `python -c` imports `govkit` and calls `derive_tool_root(t, tracked=True)` on unit 41
  AC4's scratch target, whose ignored `nested/` holds a copy of `tools/govkit/`, it prints `tools`,
  while `derive_tool_root(t)` refuses with `2 ... candidate(s) found`; and `git grep -n
  "registry.toml" -- tools/govkit/` prints no line in the step outside a call to `derive_tool_root`.
  Red when: an untracked copy counts as a candidate, or the step keeps a search of its own.
- **AC7** — When `witness <target> checklist` runs over a receipt target whose `deploy.toml` under
  `.governance` is cut off mid-table, it exits 1 naming the file with no traceback; with `[kit]`
  `memory-recall = "x"`, it exits 1 naming `kit.memory-recall`.
  Red when: a malformed descriptor reaches `target_context` and stops the walk with a traceback.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `python resolver (behaviour + inline parity + idiom ban)` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 AC6 AC7 · a renamed `kit.toml` copy, `.` and backslash targets, a foreign `GIT_INDEX_FILE`, each fixture's control copy, a nested untracked govkit copy and two malformed deploy descriptors, staged by restoring a string compare and the joined-home compare · none

## 8. Open questions

- **F1 — How many units do the minors take?** Options: (a) one; (b) two, the govkit step's and the
  rest. (b) passes M6's three clauses (§4 "Why two units"), and the halves build concurrently.
  RESOLVED (agent, 2026-10-27, delegated): (b), rung 1, BUILD-METHOD M4's two-unit clause. widens:
  none · relaxes: none
- **F2 — How is a top level compared (S2, S3)?** Options: (a) `os.path.samefile`; (b)
  `pathlib.Path.resolve()` on both sides. Both expand an 8.3 name; (a) compares the file itself.
  RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the skeptic-judged fix of ids 9 and 31.
  widens: none · relaxes: none
- **F3 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F4 — The units this one lands on are unbuilt.** Units 40, 41 and 43 are specced and unbuilt at
  `47d3a464`. RESOLVED (agent, 2026-10-27, delegated): the build run re-grounds on each at the pass and
  records any item a landed unit already closed, rung 1, the brief's rule. widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, the spec audit of the round-3 promotions' govkit upgrade-step
  minors batched: 4 MEDIUM and 4 LOW.
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullets mirroring TOOL-dFurnishedOrders-48, TOOL-dFurnishedOrders-49, promoted from the spec audit of the round-4 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-43-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended: `derive_tool_root` (`tools/govkit/govkit.py:154-175`), widened by a keyword for
S7; the `git_env_leaks_py` canonical (`tools/lib/git_env_leaks.py`) and its parity row for S4, the
twelve names memory-tree already strips; `load_toml` (`tools/govkit/govkit.py:285-292`) for S8;
`read_shipped_descriptors` and `resolve_descriptor_paths` (`:13232-13283`) for S1 and S6.
`python tools/codebase-map/reuse_lookup.py "the directory a kit homes on a target"` ranked
`resolve_kit_dir`, `kit_rel`, `kit_dir` and `ask_home_of`, none a compare of a copied descriptor's
home, and every other item extends a seam named above, so no further seam fits. The recall probe
returned units 36 and 41 and the parent builds' reuse-scout records for TOOL-dTotalRecall-20 and
TOOL-dBoundRoles-18, none disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "which minor findings of the fourth
dFurnishedOrders spec audit land on the govkit upgrade step" --terms "upgrade step toplevel samefile
GIT_ENV_LEAKS derive_tool_root tracked deploy.toml kit.toml home fixture control"`
