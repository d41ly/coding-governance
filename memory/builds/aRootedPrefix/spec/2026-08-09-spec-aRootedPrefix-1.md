# TOOL-aRootedPrefix-1 — codebase-map: make the kit correct at any install prefix

**Status:** CLOSED · rev-3 · 2026-08-10 · node a · Tier-2 · base 663ca427 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-09-review-TOOL-aRootedPrefix-1-1.md](../reviews/2026-08-09-review-TOOL-aRootedPrefix-1-1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

`map_lib.repo_root()` hardcodes the kit's `<repo-root>/codebase-map/` install convention by taking
the kit dir's grandparent, so every repo that installs kits under a prefix resolves one segment
short. Two CLIs then answer confidently from an empty corpus instead of failing, which is this
repo's own `vacuous-selector-empty-population` class shipped inside the tool that exists to catch it.

## 2. Scope (IN)

- **S1** `map_lib.resolve_root(kit_dir)` — a pure function of the kit dir: walk UP looking for
  `.codebase-map.conf`, stop at the git boundary, fall back to the grandparent convention.
  `repo_root()` becomes `CODEBASE_MAP_ROOT` override, else `resolve_root` of its own directory.
- **S2** `map_lib.require_adopted_root()` — the repo root ASSERTED to carry the conf, or a `MapError`
  carrying a printable refusal that names the resolved root, the kit dir and the remedy.
- **S3** `reuse_lookup.py` and `map_diff.py` call S2 in `main()` and exit 2 on the refusal, so neither
  can print a shortlist or a convergence report derived from a root that was never adopted.
- **S4** `adopt-codebase-map.sh` accepts a kit dir at any prefix under the repo root, deriving the
  prefix with `git rev-parse --show-prefix` rather than comparing path spellings.
- **S5** `test_codebase_map.template.py::_kit_dir()` resolves the kit from a gate file installed
  anywhere in the repo, at a root or one-segment-prefix install.
- **S6** `selftest.py` cases covering both install shapes, the git-boundary bound, the override
  precedence, the grandparent fallback, and both CLI refusals driven through their own `main()`.
- **S7** `KIT_CODEBASE_MAP_VERSION` 1.0 -> 1.1, plus the kit `README.md` and
  `.codebase-map.conf.example` prose that today states the convention as fixed.
- **S8** `WIRE-INTO-PROJECT.md` §3b and its Maintenance section: the prefixed-install path and the
  regeneration an adopter owes after the version bump.
- **S9** (`TOOL-aRootedPrefix-2`, folded in at rev-2) every path the kit PRINTS resolves from the
  repo root: `kit_rel()`/`regen_cmd()` replace the hardcoded `REGEN_CMD` in the three renderers and
  the two gates, `gen_map.py` parameterizes the scaffolded map `README.md`, the three CLIs resolve
  `<kit>` in their `--help` text, and the adopter stamps `MAP_DIFF_CMD` with the real prefix when it
  creates the conf.
- **S10** (folded in at rev-3, from the Tier-2 review) the adopter resolves its root LOGICALLY and
  refuses before writing when the operator's tree is not the tree the kit resolves to; the stamp
  cannot corrupt the conf it later sources; every entrypoint uses `abspath`, never `resolve()`; the
  gate's kit search stops at the conf as well as `.git`; and `tools/codebase-map/adopt-codebase-map.test.sh`
  becomes a gate leg, because 4 of 7 review defects lived in the one changed file no leg ran.

## 3. Non-goals (OUT)

- **Adopting the map in this repo.** The adoption lives on `branch/cd-memory-rework-alignment-005661`
  at `f9cf666` and is not merged here. This unit changes the KIT so that adoption can drop its
  `CODEBASE_MAP_ROOT` workaround; it does not merge or edit that branch.
- **Retiring `map_lib.REGEN_CMD`.** S9 stops the kit reading it, but the constant stays: a
  `GATE_FILE` installed before 1.1 references `m.REGEN_CMD`, and the maintenance rule overwrites
  ENGINE files, never `GATE_FILE`. Deleting it would break those gates on an ordinary engine
  update. It is pinned EQUAL to the accessor's root-install answer instead, so one fact stays one
  fact. Retire it when no pre-1.1 gate remains.
- **Install prefixes deeper than one segment** for the GATE FILE's kit search (S5). `resolve_root`
  itself is depth-unbounded; only the gate template's downward probe is capped, and it names every
  path it probed when it fails.
- **A `KIT_DIR` conf key.** A second declaration of a location the filesystem already answers is the
  hand-kept-second-copy defect; the dir NAME stays the fixed convention and only the PREFIX is free.
- **Retiring the kit dir's fixed name.** The gate template resolves the kit by that name; renaming it
  is a separate contract change with its own blast radius.

## 4. Design

### Data model

One resolution rule, in one function, called by everything:

| Step | Rule | Why |
|---|---|---|
| 1 | `CODEBASE_MAP_ROOT` set -> that path | tests and exotic layouts, unchanged |
| 2 | nearest ancestor of the kit dir holding `.codebase-map.conf` | the conf marks the adopted root |
| 3 | stop after the ancestor holding `.git` | a conf ABOVE that belongs to a different tree |
| 4 | otherwise the kit dir's parent | the pre-existing grandparent convention, verbatim |

Step 3 is not defensive decoration. This repo keeps its worktrees at
`.claude/worktrees/<name>/` INSIDE the primary tree, so an unbounded walk from a worktree's kit dir
reaches the primary tree's conf and resolves `MAP_ROOT` into a different checkout. `.git` is a FILE
in a worktree and a directory in a primary tree, so one `exists()` covers both.

Steps 2 and 4 are pure path math on `os.path.abspath`, never `resolve()`. The kit already documents
that a junctioned kit dir must anchor to the ADOPTING repo rather than to the link target's parent,
and this preserves that: resolving symlinks would move the anchor.

`require_adopted_root()` is the second half. Resolution answers WHERE; the assertion answers WHETHER
anything was adopted there. Splitting them keeps the library layer fail-open — `load_corpus` on a
thin corpus is a thin shortlist by design — while the CLIs refuse.

### Inventory

Measured on two fixture repos built from this branch's kit, identical in every byte except the
install prefix, over one range that ships a genuine reinvention (`slugToUrl` beside a `slugify` seam
at fan-in 3, no reference edge added):

| Entrypoint | Root install | Prefixed install (before) | Exit |
|---|---|---|---|
| `reuse_lookup.py` | 2 symbols, `slugify` ranked first | `corpus: 0 symbols`, `no seam fits` | 0 |
| `map_diff.py --converge` | `collision_flags: 1` | `collision_flags: 0` | 0 |
| `map_diff.py` digest | `mapped 1/1` | `MapError` traceback | 1 |
| `adopt-codebase-map.sh` | scaffolds | refuses, names the convention | 1 |

The `--converge` row is the load-bearing one: the same reinvention, in the same range, reports one
WARN or a clean all-clear purely on where the kit dir sits, and the clean answer exits 0. It is
structural rather than incidental — the reference index is built from a root with no source under
it, so no seam ever reaches the fan-in threshold and no collision can ever be flagged.

The digest row is why S3 targets the two CLIs and not `gen_map.py` or the gate: those import the
project layer, whose extractors fail closed by kit law, so a mis-rooted run already raises there.

### Migration

Existing root-installed adopters are unaffected by S1: for a kit at `<root>/codebase-map/`, the
conf sits at `<root>` and step 2 returns the same path step 4 already did. Adopters DO owe one
`gen_map.py --write`, because `KIT_CODEBASE_MAP_VERSION` rides `inventories.json`, `MAP.md` and
`symbols.json` as `codebase-map@<v>`, and the freshness gate byte-compares them.

An already-installed gate file at `GATE_FILE` is project-owned and is not overwritten by the
maintenance rule, so an adopter keeps its old `_kit_dir()` until they re-copy the template. That is
safe: the old walk still resolves a root install.

### Rollout

Additive. The kit is the deliverable; nothing in this repo consumes it yet on this branch, so the
merge bar exercises it only through `python tools/codebase-map/selftest.py`. The adoption branch
picks up the fix when it reconciles and can then delete the `os.environ.setdefault` line from its
`map_extractors.py` — the workaround and the fix agree on the answer, so the order does not matter.

### Files touched (estimate)

`tools/codebase-map/map_lib.py` · `reuse_lookup.py` · `map_diff.py` · `adopt-codebase-map.sh` ·
`test_codebase_map.template.py` · `selftest.py` · `README.md` · `.codebase-map.conf.example` ·
`WIRE-INTO-PROJECT.md` · `memory/DECISIONS.md` · `memory/backlog/TOOL.md` · this build folder.

### Alternatives rejected

**`git -C <kit dir> rev-parse --show-toplevel`**, the shape `memory-recall/recall_conf.py::repo_root`
already ships at fan-in 7 and the reuse pass ranked third. Rejected on the junction case: git
resolves the physical path, so a junctioned kit dir would anchor to the LINK TARGET's repo, and the
kit's current docstring makes anchoring to the ADOPTING repo an explicit guarantee. It would also
add a third root-rule shape to a kit that already walks up twice.

**Walking up unbounded, with no `.git` stop.** Rejected by the worktree layout above: measured
against this very branch, the walk would leave the worktree.

**Keeping the grandparent rule and requiring `CODEBASE_MAP_ROOT` everywhere.** That is today's
workaround. Rejected: it is set by the project layer, which the two failing CLIs do not import, so
the entrypoints that need it most are exactly the ones that cannot get it.

**Passing the regen string into the renderers as a parameter** (S9), to keep them pure. Rejected:
it changes three signatures across `gen_map.py`, the gate template and the selftest to remove an
environment dependence that is not one. The install prefix is a property of the repo being
rendered — identical on every machine, POSIX-joined so it is identical on both platforms — and a
`CODEBASE_MAP_ROOT` pointed outside the kit falls back to the bare dir name, so fixture renders
stay byte-stable too. The freshness gate renders twice in one process against one repo.

**Leaving `--help` and the scaffolded README on the bare convention** while fixing only the gate
remedy. Rejected: they are the same defect wearing different clothes, and the acceptance test is
the same one line — does the path the kit printed exist.

## 5. Production-readiness checklist

- **security** — N/A — path resolution over the adopter's own tree; no new input, no network.
- **perf / scale** — the walk is a handful of `exists()` calls bounded by the git boundary, replacing
  one `parents[1]`. No subprocess is added to the engine.
- **a11y** — N/A — command-line output.
- **i18n** — N/A — internal tooling.
- **error / empty / loading states** — the unit IS this line: an unadopted resolved root becomes a
  refusal on stderr with a non-zero exit instead of a confident empty answer.
- **observability** — the refusal prints the resolved root, the kit dir and whether the override was
  set, so the reader can tell "wrong prefix" from "not adopted yet" without reading source.
- **risks** — the real risk is a false REFUSAL breaking a working adopter. Bounded by step 4: with no
  conf found the answer is byte-identical to today's, and only the two CLIs refuse on it.
- **testing + left-shift gates** — `selftest.py` gains both install shapes, the boundary case and
  both CLI refusals driven through `main()`; the whole bar stays green.
- **migration / rollback** — revert the kit dir; the only adopter-visible obligation is the one
  `gen_map.py --write` the version bump forces.
- **user docs** — kit `README.md`, `.codebase-map.conf.example`, `WIRE-INTO-PROJECT.md` §3b.

## 6. Acceptance criteria

- **AC1** When `python tools/codebase-map/selftest.py` runs, cases for a root install, a prefixed
  install, the git-boundary stop, the override, and the grandparent fallback all pass.
- **AC2** When `reuse_lookup.py` runs against a resolved root carrying no `.codebase-map.conf`, it
  exits 2 with a refusal on stderr and prints no shortlist.
- **AC3** When `map_diff.py --converge` runs on one range in two copies of a repo differing only in
  install prefix, both report `collision_flags: 1` — measured 1 against 0 before the change.
- **AC4** When `adopt-codebase-map.sh --scaffold` runs from `<root>/tools/codebase-map/`, it
  scaffolds the map tree and the gate it installs exits 0.
- **AC5** When the gate file is installed outside the kit dir in a prefixed install, `_kit_dir()`
  returns the kit dir instead of raising.
- **AC6** When `bash tools/check-kit-versions.sh` runs, `KIT_CODEBASE_MAP_VERSION` is present and
  well-formed at 1.1.
- **AC7** When `bash tools/run-gates.sh` runs, every leg is green.
- **AC8** When an artifact is staled in a prefixed install, the regen command the gate PRINTS names
  a path that exists, and running that command verbatim clears the staleness.
- **AC9** When the adopter is run by path from a repo other than the kit's, it refuses naming both
  roots and writes nothing; when the kit dir is a symlink or junction, adoption lands in the
  ADOPTING repo, never the link target's.
- **AC10** When the install prefix cannot be expressed in the conf grammar, the conf holds the
  example's untouched default — never a half-written value — and sourcing it executes nothing.
- **AC11** When `bash tools/codebase-map/adopt-codebase-map.test.sh` runs, every arm passes, and
  each arm reds under a mutation that reintroduces the defect it names.

## 7. Gates

One new leg at rev-3: `codebase-map adopter e2e` (`tools/codebase-map/adopt-codebase-map.test.sh`). Existing legs this unit must keep green: `codebase-map kit selftest` (the leg that grows)
· `kit version markers` · `python resolver (behaviour + inline parity + idiom ban)`, because
`adopt-codebase-map.sh` carries the inline resolver block byte-identically and S4 edits that file ·
`memory hygiene (19 checks)` for this build folder · `run-gates canary`.

## 8. Open questions

none. The one genuine fork — walk up for the conf, or shell out to git like `memory-recall` — was
resolved by the junction guarantee already written into `map_lib.repo_root`'s docstring and is
recorded under Alternatives rejected rather than left open. The `REGEN_CMD` papercut is deferred
with a backlog row rather than being an open question: it is a wrong command, not a wrong answer.

## 9. Revision log

- rev-1 · 2026-08-09 · initial spec. Written after reproducing both CLI failures on paired fixture
  repos and after a reuse-lookup pass over this repo's real corpus, run from the adoption branch's
  tree with the `CODEBASE_MAP_ROOT` workaround this unit removes.
- rev-3 · 2026-08-09 · folded the Tier-2 review (2 blockers, 2 high, 2 medium, 1 low; raw 18,
  confirmed 11, precision 0.61) as S10 + AC9-AC11. The engine was clean; every defect but one was
  in `adopt-codebase-map.sh`, which no gate leg executed — so the fix is a new leg as much as it is
  new code. The blocker was self-inflicted: S4 shipped `git rev-parse --show-toplevel`, the exact
  physical-path mechanism §4 rejects for `map_lib` two paragraphs above, into the one file that
  writes to disk.
- rev-2 · 2026-08-09 · folded `TOOL-aRootedPrefix-2` in as S9 at the owner's ask, so the deferred
  remedy-path work lands in the same version rather than as a second 1.x bump against the same
  artifacts. rev-1's §3 deferral is replaced by the narrower non-goal that survives it (retiring
  the `REGEN_CMD` constant, which pre-1.1 gate files still reference). AC8 added; its arm executes
  the remedy the gate printed rather than asserting an expected string.

## 10. Reuse audit

The map is not adopted on this branch, so the pass ran against the adoption branch's tree extracted
to a scratch dir — `git archive f9cf666 | tar -x`, then
`CODEBASE_MAP_ROOT=<dir> python tools/codebase-map/reuse_lookup.py "resolve the repo root of a kit
installed under a path prefix by finding its conf"` over 244 symbols and 70 inventory keys.

- **`memory-recall/recall_conf.py::repo_root`** (fan-in 7, ranked third) is the fleet's existing
  answer to this exact question and is deliberately NOT wired through. Its mechanism is
  `git rev-parse --show-toplevel`, which resolves junctions and would break the anchoring guarantee
  codebase-map documents. Recorded under §4 Alternatives rejected, which is what a reuse audit is
  for: the seam was found, read, and declined for a stated reason.
- **`map_lib.map_root`** (fan-in 4) already layers conf-relative paths over `repo_root`, so S1 is an
  edit to the one root accessor those four callers share rather than a new path helper.
- **`map_lib.load_conf`** is reused verbatim for step 2's marker; the walk tests for the conf FILE
  and never parses a second copy of it.
- **`test_codebase_map.template.py::_kit_dir`** and `adopt-codebase-map.sh` already walk up from
  their own location. S1 adopts that same shape rather than introducing a third, which is why the
  git-based alternative was the weaker fit even before the junction case.
- The bug-class catalogue's `grammar-bound-to-the-wrong-root` and `vacuous-selector-empty-population`
  both name this failure mode; the fix is the same shape as the former's — one accessor, bindable to
  an explicit root.
