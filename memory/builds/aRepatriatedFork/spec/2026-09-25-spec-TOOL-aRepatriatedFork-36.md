# TOOL-aRepatriatedFork-36 — the recall kit converges at adopters

**Status:** CLOSED · rev-2 · 2026-09-25 · node a · Tier-2 · base 43cec933 · streams tooling · order 19

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-recall/kit.toml` declared `extract.py`, `query.py` and `recall-opened.js` `forked`, so
govkit never writes them, while `TOOL-aRepatriatedFork-12` S8 has adopters take gov's recall files
byte for byte. At inCMS that blocks `corpus_ids.py --measure` and breaks `merge-rows.py`. And gov's
fragment names the hook beside the kit, so inCMS, which keeps its hook in `.claude/hooks/`, reads
UNWIRED in `check-wiring.sh`. Owner ruling, 2026-09-25.

## 2. Scope (IN)

- **S1** — The `forked` rule leaves `tools/memory-recall/kit.toml`, so the `**` engine rule ships all
  three sources. Each one's `FORKED from` header becomes `Ported from`, since selfcheck arm 3d binds
  that header to the role. Observed by AC1, AC2.
- **S2** — A hook the target keeps elsewhere is DECLARED through the existing `[[own]]` seam, not
  moved. `check-wiring.sh` `resolve_owned_hook` and `settings-merge.py` `resolve_owned_hook` join the
  fragment's resolved path to gov's engine receipt row there, and return the path of an
  `adopter-owned` row carrying the same `source`. No receipt, no engine row, or no owned row leaves
  the path as `{kit}` and `{here}` resolved it. Observed by AC3, AC4.
- **S3** — The govkit selftest's `[dGV-3]` arms used the real memory-recall forked rule. They move
  to the synthetic `demo` fork, and two `[aRF-36]` arms assert that a fresh target now receives all
  three files. Observed by AC2, AC5.
- **S4** — Every scratch gov in the govkit selftest gets `adopters.toml` beside its `govkit.py`.
  `TOOL-aRepatriatedFork-31`'s arm 10 refuses a gov without it, which redded every selfcheck those
  fixtures run. Observed by AC5.
- **S5** — memory-recall, check-wiring and settings-merge take their version bump in every carrier.
  Observed by AC6.

## 3. Non-goals (OUT)

- Moving inCMS's hook, or writing its `[[own]]` row. Both are inCMS's, under
  `DEPL-aRepatriatedFork-20`.
- A flat kit's hook kept elsewhere. The join needs gov's engine row at the resolved path, which a
  flat kit at a foreign prefix has; no case exists to test it against.

### Edges

- **hands-off** `DEPL-aRepatriatedFork-20` — inCMS's receipt still carries `forked` rows for the three
  files. Its update takes them as `engine`, and its deploy.toml gains `[[own]] path =
  ".claude/hooks/recall-opened.js"` implementing `memory-recall:recall-opened.js`, after which its
  `check-wiring.sh` reports the hook ok.

## 4. Design

### Evidence

`git log -S'role = "forked"' -- tools/memory-recall/kit.toml` names `6798b0da`, which declared the
rule for one reason: gov's copies import `recall_conf`, and inCMS's `scripts/recall/` had none, so an
`engine` update was a ModuleNotFoundError. `TOOL-aRepatriatedFork-12` S8 ships `recall_conf.py` to
inCMS byte for byte, so that reason is gone for `extract.py` and `query.py`. `recall-opened.js`
imports nothing from the kit. It was declared only because it carries the same header, and inCMS
runs its own copy from `.claude/hooks/`, a path gov never writes. No live reason survives for any of
the three.

`TOOL-aRepatriatedFork-2` §8 F2 ruled that gov does not model a hook outside its kit. This unit does
not model the layout either: `[[own]]`, from `DEPL-aRepatriatedFork-13`, already lets a target
declare its own implementation of a gov source at another path, and `adopt` records it in the
receipt. The resolvers only read that row.

### Inventory

`resolve_owned_hook` — `sh.function` in `tools/check-wiring.sh` and a Python function in
`tools/settings-merge.py`, verb `resolve`. `check-hook-destinations.sh` already compares the two
readers' `--resolve-fragment` answers, so the pair cannot drift silently.

### Files touched (estimate)

`tools/memory-recall/kit.toml`, the three recall sources' headers, `tools/check-wiring.sh`,
`tools/settings-merge.py`, `tools/check-wiring.test.sh`, `tools/govkit/selftest.py`, the two docs,
`tools/install-prefix-waivers.txt` (re-keyed), the map, and the version carriers.

### Alternatives rejected

- A conf key naming the hook's path. The build rule allows a new key for an adopter's decision,
  never its layout.
- A new fragment token. `{here}` already names gov's copy; the target's copy is a fact about the
  target, which only the target's declaration can carry.
- Keeping `recall-opened.js` forked. Its fork protected nothing gov could overwrite.

## 5. Production-readiness checklist

- security — the owned path is refused when absolute, drive-lettered or `..`-bearing, as the receipt
  reader beside it already does.
- perf / scale — one read of the receipt per resolved fragment.
- error / empty / loading states — an absent or unparsable receipt leaves the path unchanged.
- observability — `--resolve-fragment` prints the resolved path in both readers.
- risks — an adopter whose receipt names a stale owned path reads a missing hook, which the recall
  arm then reports by name.
- testing — AC3 to AC5, each red first.
- migration — adopters' receipts carry `forked` rows until their next update; handed to
  `DEPL-aRepatriatedFork-20`.
- user docs — `tools/memory-recall/README.md` step 2 and the runbook's maintenance paragraph.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs on the built tree, it exits 0.
  Red when: a recall source keeps `FORKED from` in its head with no `forked` rule, which arm 3d names.
- **AC2** — When the `[aRF-36]` arms of `tools/govkit/selftest.py` run as a slice, `apply` lands
  `query.py`, `extract.py` and `recall-opened.js` on a fresh target and prints no INCOMPLETE line.
  Red when: the descriptor still declares them forked.
- **AC3** — When the AC8 block of `tools/check-wiring.test.sh` runs as a slice, an `adopter-owned`
  receipt row moves the resolved hook to `.claude/hooks/recall-opened.js`, `settings-merge.py`
  resolves the same path, and the recall arm reports ok. Red when: the old readers resolve beside
  the fragment and report UNWIRED.
- **AC4** — When `python tools/settings-merge.py --selftest` runs, arm 13b passes. Red when: the owned
  join is removed from `resolve_hook_path`.
- **AC5** — When the synthetic `DEPL-dCarriedReceipt-10` block of `tools/govkit/selftest.py` runs as a
  slice, every arm passes, the moved `[dGV-3]` arms among them. Red when: a scratch gov lacks
  `adopters.toml`, which arm 10 refuses.
- **AC6** — `bash tools/check-kit-versions.sh` exits 0 and `python tools/govkit/govkit.py epoch`
  reports no FAILED entry. Red when: a moved kit kept its old value in any carrier.

## 7. Gates

`govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `hook destinations (every declared hook path ships)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `harness arms (fail branches armed or pinned)` · `check-wiring self-test` · `settings-merge selftest` · `govkit selftest`

New arm: `tools/check-wiring.test.sh` · an adopter-owned receipt row for the recall hook, and its control · none

## 8. Open questions

- **F1 — keep `recall-opened.js` forked?** RESOLVED (agent, 2026-09-25): no. §4 Evidence finds no
  write gov could make over inCMS's copy, which lives at a path gov never ships to.

## 9. Revision log

- rev-1 · 2026-09-25 · initial draft, from the owner's ruling.
- rev-2 · 2026-09-25 · §2 S4 · AC5 · the scratch-gov fixture repair added once the slice found
  `TOOL-aRepatriatedFork-31`'s arm 10 refusing every scratch gov. Built: every arm green, each new
  one red on the old bytes.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "resolve a fragment hook path to where the target installed
the hook"` ranked `resolve` in `recall_conf.py` and three other resolvers, none of which reads the
receipt; the map does not scan `.sh`. The seams reused are `[[own]]` and its `adopter-owned` receipt
row from `DEPL-aRepatriatedFork-13`, and `check-wiring.sh`'s receipt awk, whose row grammar the new
function copies.

Recall terms used: `forked role recall extract query recall-opened fragment hook_path here own
adopter-owned receipt`.
