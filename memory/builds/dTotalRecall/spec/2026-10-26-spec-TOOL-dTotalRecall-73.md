# TOOL-dTotalRecall-73 — the census keep registry has one home under the conf's memory root, and a `census-kept-paths` registration naming another file is red

**Status:** CLOSED · rev-3 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 33 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-73-deviation-731.md](../build/2026-10-26-build-TOOL-dTotalRecall-73-deviation-731.md) | deviation | — |
| [2026-11-24-build-TOOL-dTotalRecall-73-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dTotalRecall-73-1-acceptance-ledger.md) | log | — |
| [2026-11-24-build-TOOL-dTotalRecall-73-1-builder-return.md](../build/2026-11-24-build-TOOL-dTotalRecall-73-1-builder-return.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-73-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-73-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-73-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-73-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-73-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-73-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-75 TOOL-dTotalRecall-74 TOOL-dTotalRecall-76 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 67 to 70
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md`)
confirmed finding **id 5 at HIGH**, its item **H1**. Item **M8** (id 20) addresses the same literal
home at MEDIUM with a corrected fix pointing the other way, and the report asks for one source of
truth applied to both. This unit is that source. The batch `TOOL-dTotalRecall-76` applies it to M8.

`TOOL-dTotalRecall-68` (order 32) registers the keep registry in gov's `tools/govkit/registry.toml`
alone, with `home = "memory/project/census-kept-paths.txt"`. The ratchet pack compares that literal
home with its base (`tools/memory-tree/ratchet.py#run_never_gains`). The censuses read
`<MEMORY_ROOT>/project/census-kept-paths.txt`, the memory root read from the conf
(`tools/memory-tree/tree_lib.py#read_kept_rows`). The two are one file only while the conf's root and
the registered home agree, and nothing compares them. A tree that registers the population under one
root and declares another has its censuses read one file while its ratchet grades a second, or an
absent one. Gov sets `MEMORY_ROOT=memory`, so gov cannot see the split. An adopter holds no
registration, so no ratchet reads its registry, and it has no split to see.

This unit gives the censuses' path one function, `resolve_kept_home(root)`. Each registration of the
population is joined to it, and one that names another file is a red finding naming both homes. The
writer census prints both homes, so the split is visible on one run. It repairs
`TOOL-dTotalRecall-68`, at step 33, one above that unit's order.

## 2. Scope (IN)

- **S1** — The one home. `resolve_kept_home(root)` in `tools/memory-tree/tree_lib.py` returns
  `<memory root>/project/<CENSUS_KEPT_REGISTRY>`, a repo-relative path spelled with `/`, the memory
  root read from the conf exactly as `read_kept_rows` reads it at HEAD. It reads no registration. An
  absent registration is not red: the kit ships to adopters that hold none, and unit 65's
  plant `adopter-no-registry` holds that tree green (§8 F3). Observed by AC1 and AC4.
- **S2** — The censuses read it. `read_kept_rows(census, root)` opens the file at
  `resolve_kept_home(root)`, joins no path of its own and reads the conf nowhere else. The memory root
  `TOOL-dTotalRecall-66` S11 builds the row domain from is that home's own, the home's second parent,
  so the domain and the path are one read. `read_kept_path` and both censuses reach the file through
  `read_kept_rows`, as at HEAD. Observed by AC3.
- **S3** — The join. `check_kept_home(root)` in `tools/memory-tree/record_causes.py` answers
  `(lines, reds)`, which `check_cause_writers` adds to its own, so `--check` and `--cause-writers`
  both print them. One line names the home the censuses read. One more line follows per registration
  whose population is `census-kept-paths`, naming its home and its source, or a single line saying
  none registers it. A registration whose home is another path is one red finding naming both homes
  and the source. Registrations that do not read are a refusal, exit 2. The
  base compare itself stays the ratchet pack's (`TOOL-dTotalRecall-68` §8 F2). Observed by AC2 and AC4.
- **S4** — The plant `kept-home-rooted` in `record_causes.py --fixture` builds a scratch tree whose
  conf sets `MEMORY_ROOT=docs/memory`, through the memory root `TOOL-dTotalRecall-66` gives
  `write_fixture` for `kept-row-docs-root`. Its govkit registry also registers `census-kept-paths`
  with the literal home under `memory/project/`. It writes no keep row. There `--check` exits 1 with
  one red, naming both homes. Observed by AC2.

## 3. Non-goals (OUT)

- The ledger factory, `tools/lib/legacy_ledger.py` and its inline copies, its `Registration` type and
  the ratchet pack. This unit reads `read_registrations` and edits none of them.
- A second base compare in `record_causes.py`, or a registration re-rooted in memory: §8 F3.
- The factory-side readers of a literal home: `compare_to_base`, the duplicate-home refusal, the CLI's
  verbs and the merge driver's header read. They read the registered path. That gap is the factory's,
  handed off below, and S3's red is what shows it.
- A red on an unregistered registry, in gov or elsewhere. Unit 68's AC1 observes gov's registration at
  its tip.
- Normalising or refusing a memory root's value: `TOOL-dTotalRecall-87`.
- The registry's row grammar, its census domain and its message text: units 66, 68 and 70, and the
  batch `TOOL-dTotalRecall-76` for item M8's consumers and item M4's messages.
- Editing unit 68's spec, frozen once its unit builds at order 32.

### Edges

- **consumes-from** `TOOL-dTotalRecall-68` — the `census-kept-paths` registration in gov's registry and the factory-grammar `read_kept_rows`, whose path this unit joins to the registered home
- **hands-off** `TOOL-dTotalRecall-76` — `resolve_kept_home`, the one home that batch's item for id 20 names to unit 66's docs-root plant and unit 70's messages and admission
- **hands-off** external — `TOOL-dWitnessedBar-13`'s owner: a `[[ledger]]` home that resolves under a tree's memory root, for `compare_to_base`, the duplicate-home refusal, the CLI's verbs and the header read
- **hands-off** `TOOL-dTotalRecall-87` — `resolve_kept_home` and its plant `kept-home-rooted`, whose memory-root read that unit routes through one resolver (the round-1 audit of units 71 to 76, id 39); §4 says what it can expect
- **hands-off** `TOOL-dTotalRecall-88` — its AC3, its hand-off and `resolve_kept_home`, which that batch observes by the join and completes by an ask; no registration is re-rooted, so its id 20 finds no join by basename (the round-1 audit of units 71 to 76, ids 3, 20, 24, 27, 30, 43)

## 4. Design

### The home

```python
def resolve_kept_home(root) -> str:
    """The keep registry's one path, repo-relative under `root`'s memory root (TOOL-dTotalRecall-73 S1)."""
    from design_lib import read_design_conf   # at call time, no cycle, as read_kept_rows imports it at HEAD
    memory = (read_design_conf(root).get("MEMORY_ROOT") or "memory").strip().strip("/") or "memory"
    return f"{memory}/project/{CENSUS_KEPT_REGISTRY}"
```

`read_kept_rows` opens `pathlib.Path(root, resolve_kept_home(root))`. Where its domain refusal needs the
memory root, it takes `str(pathlib.PurePosixPath(home).parents[1])`. Its row grammar, its refusals and
its answer are unit 68's and unit 66's, unchanged.

### The join

```python
def check_kept_home(root) -> tuple:
    home = tree_lib.resolve_kept_home(root)
    population = pathlib.PurePosixPath(tree_lib.CENSUS_KEPT_REGISTRY).stem
    regs = [r for r in ll.read_registrations(root) if r.population == population]
    ...
```

A registered home differs where `PurePosixPath(reg.home) != PurePosixPath(home)`, so `.` and doubled
separators do not red. A `ValueError` of `read_registrations` is re-raised with the text
`read_legacy_paths` gives it, which both callers of `check_cause_writers` print as `refused` with exit
2. The population's name is the registry file's stem, so the module spells the filename once.

The lines are, at gov:

```text
cause-writer · keep registry · read at memory/project/census-kept-paths.txt
cause-writer · keep registry · registered at memory/project/census-kept-paths.txt in tools/govkit/registry.toml
```

With no registration the second line reads `cause-writer · keep registry · registered nowhere`. No
line opens a field with the word `kept`, since the grade of `adopter-no-registry` reads that as a kept
hit. The red reads:

```text
cause-writer census-kept-paths.txt: the censuses read <home> and <source> registers <reg.home>, so the ratchet grades a file no census reads; register the home under the conf's MEMORY_ROOT
```

The alias census prints none of this. It reads the same file through the same reader, so one join
answers for both.

### Why a join and not one registration passed to both

At rev-2 this unit's `--check` made the base compare, so it could hand that compare a re-rooted
registration. Unit 68 rev-3 builds no such compare. The ratchet pack reads each registration itself, at
its literal home. A re-rooted copy would then change only what the census reads, and would hide the
split rather than close it. Where one fact is spelled twice and the factory owns one spelling, a gate
compares the two.

### What TOOL-dTotalRecall-87 can expect

`resolve_kept_home(root)` is the one join of a memory root to the registry's filename, called by
`read_kept_rows` and `check_kept_home`. Its root at this unit's tip, per conf value:

| `MEMORY_ROOT` | The home's root |
|---|---|
| absent, blank or only slashes | `memory` |
| `docs/memory/`, or `/docs/memory` | `docs/memory`, the slashes at both ends stripped |
| a backslash, or a `.`, `..` or doubled inner segment | as spelled |

So a trailing slash already reads one home, and a blank value falls back rather than refusing. No
census opens a path under `/project`. No compare line is printed beside the census line: the lines
to expect are the `read at` and `registered at` lines above. A `ValueError` a resolver raises reaches
the censuses through `read_kept_rows`, whose catch makes it one red. The same error from
`check_kept_home`'s call is outside that catch and prints as `refused` with exit 2. Unit 87 chooses
which it keeps.

### Order inside step 33

`TOOL-dTotalRecall-70` and `TOOL-dTotalRecall-75` share step 33. Unit 70 writes `tree_lib.py` and
`record_causes.py` too, so the two passes are not disjoint, and BUILD-METHOD M6 sequences them in
either order. Unit 70's items read the registry through `read_kept_rows` and `read_kept_path`, whose
signatures this unit keeps. Unit 75 writes only `memory/guides/SESSION-KICKOFF.md`. S4 rests on
`TOOL-dTotalRecall-66`'s fixture parameter, built a step earlier at order 32.

### What it does not check

That a registration exists. That the registered `fields` equal `KEPT_FIELDS`, which unit 68's AC1 reads
once. That the registry's file is present at either home: the censuses read an absent one as no rows.

### Inventory

Minted: `resolve_kept_home` in `tools/memory-tree/tree_lib.py`; `check_kept_home` in
`tools/memory-tree/record_causes.py`; the fixture plant `kept-home-rooted`. Naming cells: both functions
answer `OK` under `py.function` (`python tools/lexicon/lexicon.py --suggest <name> --as py.function`,
2026-11-24), led by the declared verbs `resolve` and `check`; a plant has none. The name
`resolve_kept_registration` of rev-2 is not minted, since what it returned has no reader left.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/record_causes.py`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **The literal home wins** (item H1's corrected fix). `read_kept_rows` reads the registered path. An
  adopter holds no registration, so its reader would have no path. Unit 66's AC7 plant
  `kept-row-docs-root` and unit 70's S8 messages, which name `<MEMORY_ROOT>/project/`, then contradict
  the engine (§8 F1).
- **The conf path and the literal home, uncompared** (item M8's corrected fix). That is the split this
  item names, kept.
- **A registration re-rooted under the conf's root, read by the census** (rev-2). §8 F3.
- **A `{memory_root}` token in the registered home.** The factory designs no token resolution, and
  its readers of `home` would read the token as a path (§3).

## 5. Production-readiness checklist

- security — no new write surface. The home stays where the censuses read it at HEAD.
- perf / scale — one more read of the registrations per writer census,
  0.16 s over 49 registrations (DERIVED 2026-11-24, node a, one timed `read_registrations` call).
- error / empty / loading states — no registration is a line and no red. An absent file is no rows, as
  at HEAD. Registrations that do not read are a refusal, exit 2.
- observability — the census prints the home it reads and each home registered.
- risks — the factory's readers still use the literal home, handed off in §3. S3 reds the split rather
  than resolving it.
- testing — AC1 to AC4 by the pass; the arm of §7 at the close.
- migration — none. No home moves.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When the probe below runs from `tools/memory-tree/` at the pass tip, it prints one path
  twice, the home `tools/govkit/registry.toml` registers for `census-kept-paths`.

  ```bash
  python -c "import tree_lib, legacy_ledger as ll; print(tree_lib.resolve_kept_home('../..'), *[r.home for r in ll.read_registrations('../..') if r.population == 'census-kept-paths'])"
  ```

  Red when: gov's resolved home differs from its registered one, or the population is unregistered and
  one path is printed.
- **AC2** — When `python record_causes.py --fixture --plant kept-home-rooted` runs from
  `tools/memory-tree/`, it exits 1 with one `record causes: RED ` line, naming the registry's file under
  the `project` folder of the fixture's memory root `docs/memory` and the one under `memory/project/`.
  The `read at` line names the first and the `registered at` line the second. With the comparison
  skipped in a probe process, the same plant exits 0.
  Red when: the split is green, or either line names the other's home.
  fixture: the plant's scratch tree, made and removed under the system temp directory as every plant's
  is.
- **AC3** — When `python -c "import inspect, tree_lib; s = inspect.getsource(tree_lib.read_kept_rows); print('resolve_kept_home' in s, 'read_design_conf' in s)"`
  runs from `tools/memory-tree/` at the pass tip, it prints `True False`, and the probe below, run
  there, prints `probe row`.

  ```bash
  python - <<'PROBE'
  import os, pathlib, sys, tempfile
  sys.path.insert(0, os.getcwd())
  import tree_lib
  path = "memory/builds/tOne/build/one.py"
  row = "\t".join(["check_cause_writers", path, "probe row", "-", "1", "a" * 12, "seeded"])
  with tempfile.TemporaryDirectory(prefix="kh") as d:
      f = pathlib.Path(d, "memory/moved/kept.txt")
      f.parent.mkdir(parents=True)
      f.write_text(row + "\n", encoding="utf-8")
      tree_lib.resolve_kept_home = lambda root: "memory/moved/kept.txt"
      print((tree_lib.read_kept_path("check_cause_writers", path, d) or {}).get("reason"))
  PROBE
  ```

  Red when: the reader joins its own path beside the resolver's, which makes the probe print `None`, as
  it does at the base of this pass.
- **AC4** — When `python record_causes.py --cause-writers` runs from `tools/memory-tree/` at the pass
  tip, it prints §4's two lines for gov, no red naming `census-kept-paths.txt`, and every other line as
  at the pass base. `python record_causes.py --fixture --plant adopter-no-registry` there prints `PASS`
  and the line ending `registered nowhere`.
  Red when: the join is not wired into the census, or an absent registration reds.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `record causes (causes and orphans over the legacy population)` · `record-kinds` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC2 · the plant `kept-home-rooted`, its exit 1 and its one red naming both homes, staged by skipping the comparison in `check_kept_home`, which exits the plant 0 · none

## 8. Open questions

- **F1 — Which file is the registry's one source of truth for both readers (ids 5 and 20)?** Options:
  (a) the registered literal home, read by the census and the compare alike; (b) the conf-derived
  path for the census and the literal home for the compare; (c) the registration with its home
  re-rooted under the conf's memory root, passed to both. (b) keeps the split this unit exists to
  close and fails AC2; veto 1 discards it. (a) passes AC2 only by moving an adopter's registry out of
  its memory tree, and contradicts unit 66's AC7 plant and unit 70's S8 messages. (c) satisfies every
  criterion above and both units' text. RESOLVED (agent, 2026-10-26, delegated): (c), rung 3, the
  most feature-rich survivor. widens: none · relaxes: none. Its source, the conf's memory root, stands;
  F3 settles its mechanism over HEAD.
- **F2 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F3 — What joins the two homes, now that the registration is gov's alone and the base compare is
  the ratchet pack's (unit 68 rev-3 S1, §8 F2)?** Options: (a) nothing is built, the two agreeing at
  gov; (b) rev-2's `resolve_kept_registration`, an absent registration red; (c) that function with a
  fallback for a tree registering none; (d) the conf's path as one function, and a red where a
  registration names another file. (a) leaves the split unseen and fails AC2, and (b) reds unit 65's
  plant `adopter-no-registry` and fails AC4; veto 1 discards both. (c) changes only what the census
  reads, since the pack reads the registration itself, so the split stays and AC2 fails; it also
  spells the filename twice and makes every keep read parse every descriptor.
  RESOLVED (agent, 2026-11-24, delegated): (d), the one survivor, per
  `2026-11-24-prompt-TOOL-dTotalRecall-73-reground-brief`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 67 to 70, id 5
  (HIGH, item H1).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-87, TOOL-dTotalRecall-88, each the other end of an edge a
  unit the round-1 spec audit of units 71 to 76 promoted wrote; nothing else moved.
- rev-3 · 2026-11-24 · §1 S1 S2 S3 S4 §3 §4 §5 AC1 AC2 AC3 AC4 §7 §8 §10 · re-grounded at HEAD
  `c0a707782` per `2026-11-24-prompt-TOOL-dTotalRecall-73-reground-brief`, over unit 68 rev-3 and unit
  66 rev-5: no `--check` compare stands and an adopter holds no registration, so S1's red on an absent
  one is cut and S3's compare becomes a join (F3). `resolve_kept_home` takes the place of rev-2's
  `resolve_kept_registration`; the reader is `read_kept_rows`; AC3 observes the read by behaviour; AC4 is
  new; the plant's arm sits in the hygiene suite, as its siblings' do.

## 10. Reuse audit

The seam extended is the path read `tools/memory-tree/tree_lib.py#read_kept_rows` makes through
`tools/memory-tree/design_lib.py#read_design_conf`, moved into one function, and
`tools/memory-tree/legacy_ledger.py#read_registrations`, selected by population as
`tools/memory-tree/record_causes.py#read_legacy_paths` selects it. The plant extends
`tools/memory-tree/record_causes.py#write_fixture` as unit 66 parameterises it, and
`tools/memory-tree/record_causes.py#check_cause_writers` carries the lines. The landed
`resolve_memory_root` readers sit in kits memory-tree does not import, and unit 87 routes this one read.
`python tools/codebase-map/reuse_lookup.py "the project registry path under the conf's memory root joined to a ledger registration home"`
ranks `read_design_conf` and `read_registrations` among its seams and names no reader that joins a
project registry's path to its registered home (DERIVED 2026-11-24, that command). No existing seam fits
the join itself.

Recall terms used: `python tools/memory-recall/query.py "how is a memory/project registry registered as a ledger population and ratcheted" --terms "ledger registration shrink-only legacy_ledger read_rows project registry PROJECT_REGISTRY_EXTRA census keep gained memory root"`
