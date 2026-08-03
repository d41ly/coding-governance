# TOOL-aQuarriedLantern — build ledger

One entry per build unit. Every number below came from a command run in-session, not from the spec.

## U1 — `tools/memory-recall/` — the kit itself

**Landed** 2026-08-03 · node `a` · base `f564109e`

### Shipped — 9 files, `tools/memory-recall/`

| File | Category | Bytes |
|---|---|---|
| `recall_conf.py` | new — the project layer | 7 492 |
| `extract.py` | forked from inCMS `5318064` | 21 542 |
| `query.py` | forked from inCMS `5318064` | 45 572 |
| `bench.py` | verbatim upstream | 20 253 |
| `union.py` | verbatim upstream | 5 827 |
| `selftest.py` | new — 14 checks | 24 934 |
| `adopt-memory-recall.sh` | new | 5 701 |
| `README.md` | new | 7 786 |
| `verbatim.json` | new — digest pin for the two verbatim files | 69 |

`bench.py` and `union.py` were verified byte-identical to `/c/projects/incms/main/scripts/recall/`
with `cmp -s`, not assumed. `verbatim.json` pins their LF-normalised sha256 prefixes
(`bench.py 5a46060ffb2008fc`, `union.py a345199f5d901aae`) so a later silent edit reds the selftest.

### Measured

| Fact | Value |
|---|---|
| this repo's corpus | 66 tracked `.md` files, 496 153 B |
| first live query | `index 9 records + 1033 chunks (rebuilt 0.09s)`, 29 hits, 7 shown in 2 917 B |
| index build (`built_s`) | 0.18 s |
| warm query, wall | 1.584 / 2.230 / 2.274 s — interpreter start-up and `git`, not the index |
| full-corpus grep baseline | `grep -rIl "adopt" memory/` 0.077 / 0.092 / 0.447 s, 31 of 66 files |
| selftest | 14/14 checks, 24.2 s wall |
| conf digest, this repo | `9bcce30ca38b` |

At this corpus size retrieval is **slower** than the grep it replaces. What it buys is a ranked
handful instead of half the tree, and the README says so rather than implying a speed win.

### The three things that had to be right

1. **The silent zero (S7).** Upstream returns `index 0 records + N chunks` and exits 0 when the id
   families do not match the corpus. Reproduced in a throwaway repo with `FAMILIES="tooling:ZZZZ"`:
   the header still reads `index 0 records + 1 chunks`, and the CLI now also prints a `ZERO RECORDS`
   block on stderr naming the resolved families, the conf path and
   `` `python memory-recall/query.py --rebuild` ``. The same diagnosis fires on `extract.py`'s own
   path. Gated by the selftest arm *mis-declared FAMILIES is LOUD*, which asserts both paths.
2. **The cache freshness key (blocker F1).** `Conf.digest()` hashes the RESOLVED `MEMORY_ROOT`, the
   sorted families tuple and the node-tag class — not the conf file's bytes, so a comment edit costs
   no rebuild. It lands in the manifest and joins `ensure_cache`'s `fresh` predicate. Measured in
   both directions: `2 records (rebuilt) -> cached -> 0 (rebuilt) -> 2 (rebuilt)`.
3. **Writes nothing in the adopter's worktree (F5).** `sys.dont_write_bytecode = True` sits ABOVE
   the `sys.path` insert in `query.py`, `selftest.py` and `recall_conf.py`. Asserted by PATH: the
   arm walks the whole worktree — kit directory included — before and after a query, in a fixture
   repo with **no** `.gitignore` at all, and asserts the set is unchanged and that the 4 files
   created all sit under `<gitdir>/recall/`.

### Also folded

- **R1** — no `--memory-root`, no `--families`. The conf-absent refusal prints a two-key stub; the
  selftest pastes that stub verbatim into a fixture repo, asserts the next query returns 2 records,
  and asserts both flags are rejected as unknown.
- **F7** — every printed invocation derives from `__file__` through one `CLI` expression, reused by
  the module docstring, `REFUSAL`, the `--export` header and the qid hand-back. The selftest runs in
  a repo whose kit dir is `memory-recall/` (not this repo's `tools/memory-recall/`), harvests every
  `python <path>.py` the CLI prints across `--help`, the no-terms refusal and a successful query,
  and asserts each one resolves.
- **R5 / F14** — `evict_dead_siblings` deletes a sibling cache only when its manifest is readable
  AND records a `worktree` that no longer exists. No readable manifest = NEVER evicted (that is the
  shape of a sibling mid-first-build). All three cases are one selftest arm.
- **F9** — `adopt-memory-recall.sh` resolves `python3` first with a `python` fallback and a
  `RECALL_PY` override (the `tools/check-wiring.sh:69` form). The selftest runs it on a PATH cut
  down to a `python3` shim plus the bash/git directories, and asserts exit 0.
- `--export` writes beside the query log under the common git dir and requires `--tag`; upstream's
  `CLAUDE.md` node-registry lookup is deleted. `BUILD_QID_CUTOFF` ships empty — the mechanism, none
  of the inCMS data. No alias data ships; the alias mechanism does, and the empty-alias path is a
  gated arm.

### Bugs found and fixed while building, each by a run rather than a read

- `HERE` was resolved after `cd "$ROOT"`, so a relative `$0` made the adopt script look for
  `recall_conf.py` under `C:/Program Files/Git/`. Now resolved before the `cd`.
- `git rev-parse --show-toplevel` spells the root `C:/x` under MSYS while `pwd` spells it `/c/x`, so
  the prefix-strip that computes the kit's repo-relative path silently no-opped and printed an
  absolute path. Root is re-read through `pwd`.
- The `python`-off-PATH arm tested `"HAVE_PYTHON" in probe`, and `"HAVE_PYTHON3"` contains
  `"HAVE_PYTHON"` — so a correctly isolated PATH reported "python is still here" and the arm skipped
  for the wrong reason. It now matches exact tokens. Without this the AC14 arm would have shipped
  never running.

### Mutation verification — 8/8 killed

Green baseline asserted first (14/14). Each mutation was asserted APPLIED on disk (present-before /
absent-after) and each revert asserted byte-identical; a crash scores as a kill. Post-revert 14/14.

| Mutation | File | Arm that reddened |
|---|---|---|
| M1 drop `sys.dont_write_bytecode` | query.py | writes NOTHING in the worktree |
| M2 drop `conf_digest` from the `fresh` predicate | query.py | conf_digest joins freshness |
| M3 drop the zero-record diagnosis from the query path | query.py | mis-declared FAMILIES is LOUD |
| M4 `zero_record_diagnosis` always returns None | extract.py | mis-declared FAMILIES is LOUD |
| M5 evict cache dirs with no readable manifest | query.py | cache eviction |
| M6 hardcode the printed invocation to the upstream path | query.py | printed invocations resolve |
| M7 stop trimming unquoted conf values at whitespace | recall_conf.py | conf parser == bash |
| M8 edit a verbatim file | bench.py | byte-identical to upstream |

### Deviations from the rev-2 spec

- **`union.py` ships.** Spec §3 lists it under Non-goals; the orchestrator's ratified shipping set
  names it. Shipped byte-identical, with the README stating that its `main()` is inert without a
  `fixture.json` this kit does not ship — the same caveat `bench.py` carries.
- **`SKILL.template.md`, `recall-opened.js` and `recall-opened.fragment.json` are not in this
  unit.** `adopt-memory-recall.sh` ships their full contract and reports a three-state result:
  template absent → `skip` and exit 0 on `--check` (nothing rendered can drift), exit 1 on
  `--scaffold` (you asked to install it); a rendered `SKILL.md` with no template → exit 1, because
  that is the one genuinely unverifiable state. Placeholder contract for whoever writes the
  template: `{{FAMILIES}}`, `{{MEMORY_ROOT}}`, `{{QUERY_CLI}}` — an unsubstituted `{{...}}` reds.
- **Both gate legs and the `check-kit-versions.sh` pair assertion were registered here** rather than
  deferred: a kit that ships unwired is the defect the source feature spent a session repairing.
  `memory-recall skill wiring` is green-with-a-skip-line until the Skill template lands.
- The R1 selftest arm asserts the two flags are REJECTED, which is a stronger reading than the
  spec's "the refusal must not print them".
- The adopt script does **not** carry codebase-map's `-ef` fixed-kit-name check: this repo keeps its
  kits under `tools/`, and `--check` is a gate leg here, so a fixed `<root>/memory-recall` assertion
  would red the leg in the reference adopter.
