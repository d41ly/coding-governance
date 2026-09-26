# TOOL-aRepatriatedFork-36 — the recall kit converges at adopters

**Status:** CLOSED · rev-3 · 2026-09-26 · node a · Tier-2 · base 6f3fd77a · streams tooling · order 19

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-25-build-TOOL-aRepatriatedFork-36-1-acceptance-ledger.md](../build/2026-09-25-build-TOOL-aRepatriatedFork-36-1-acceptance-ledger.md) | journal | — |
| [2026-09-26-review-TOOL-aRepatriatedFork-36-closing-diff-round1.md](../reviews/2026-09-26-review-TOOL-aRepatriatedFork-36-closing-diff-round1.md) | diff-review | TOOL-aRepatriatedFork-31 TOOL-aRepatriatedFork-32 TOOL-aRepatriatedFork-35 TOOL-aRepatriatedFork-37 TOOL-aRepatriatedFork-38 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-recall/kit.toml` declared `extract.py`, `query.py` and `recall-opened.js` `forked`, so
govkit never writes them, while `TOOL-aRepatriatedFork-12` S8 has adopters take gov's recall files
byte for byte. At inCMS that blocks `corpus_ids.py --measure` and breaks `merge-rows.py`. And gov's
fragment names the hook beside the kit, so inCMS, which keeps its hook in `.claude/hooks/`, reads
UNWIRED in `check-wiring.sh`. Owner ruling, 2026-09-25.

## 2. Scope (IN)

- **S1** — The `forked` rule leaves `tools/memory-recall/kit.toml`, so the `**` engine rule ships
  `extract.py` and `query.py`. Each recall source's `FORKED from` header becomes `Ported from`, since
  selfcheck arm 3d binds that header to the role. Observed by AC1, AC2.
- **S2** — A hook the target keeps elsewhere is DECLARED through the existing `[[own]]` seam, not
  moved, and the join has ONE reader: `settings-merge.py` `resolve_owned_hook`, printed by its
  `--resolve-hook` verb, which `check-wiring.sh` calls instead of parsing the receipt itself. The join
  maps the fragment's resolved path to gov's engine receipt row there and returns the path of the
  `adopter-owned` row carrying the same `source`. No receipt, no engine row, or no owned row leaves
  the path as `{kit}` and `{here}` resolved it. A joined owned path is graded with govkit's own
  `[[own]].path` rule — the strict token class, normpath equality, containment — and REFUSED when it
  fails, when its file name differs from the hook's, or when the join is ambiguous. Observed by AC3,
  AC4.
- **S3** — The govkit selftest's `[dGV-3]` arms used the real memory-recall forked rule. They move
  to the synthetic `demo` fork, and the `[aRF-36]` arms assert what a fresh target receives.
  Observed by AC2, AC5.
- **S4** — Every scratch gov in the govkit selftest gets `adopters.toml` beside its `govkit.py`,
  the `a4`, `a5`, `a6` and `a13` builders among them. `TOOL-aRepatriatedFork-31`'s arm 10 refuses a
  gov without it, which redded every selfcheck those fixtures run. Observed by AC5.
- **S5** — memory-recall, check-wiring and settings-merge take their version bump in every carrier.
  Observed by AC6.
- **S6** — `check-wiring.sh` `wired` joins on the hook's RESOLVED PATH in the settings command, not
  on the marker and basename alone, so an entry running another copy of the hook is UNWIRED, named.
  Observed by AC3.
- **S7** — `recall-opened.js` stays an OPT-IN: its own file rule declares `opt_in = "with_hook"`, and
  govkit lands it only where the target's deploy.toml sets `[kit.memory-recall] with_hook = "yes"`.
  One predicate, `derive_opted_out`, is read by the rule expansion that plan, apply, update and check
  share; a skip names the key, the canonical ctx counts every opt-in taken, and selfcheck arm 4c
  refuses a malformed `opt_in`. Observed by AC1, AC2.

## 3. Non-goals (OUT)

- Moving inCMS's hook, or writing its `[[own]]` row. Both are inCMS's, under
  `DEPL-aRepatriatedFork-20`.
- A flat kit's hook kept elsewhere. The join needs gov's engine row at the resolved path, which a
  flat kit at a foreign prefix has; no case exists to test it against.

### Edges

- **hands-off** `DEPL-aRepatriatedFork-20` — inCMS's receipt still carries `forked` rows for the
  three files, and its blobs of `extract.py` and `query.py` match no gov vintage, so `update` alone
  re-records them `engine`/`unattributed` and writes nothing. The route is: take gov's
  `recall-opened.fragment.json`; copy gov's `extract.py` and `query.py` bytes over its own; declare
  `[kit.memory-recall] with_hook = "yes"` and `[[own]] path = ".claude/hooks/recall-opened.js"`
  implementing `memory-recall:recall-opened.js`; then run `adopt --re-adopt --write`, which both
  attributes the two programs `vintage-match` and records the `adopter-owned` row. Its
  `check-wiring.sh` then reports the hook ok.
- **hands-off** external — nc runs the same out-of-kit hook, `.claude/hooks/recall-opened.js`, beside
  a kit copy gov now updates, and this build's provenance scrub and check-21 rework add update
  conflicts in its carve-out files. Filed as backlog row DEPL-aRepatriatedFork-23.

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
receipt. The resolver only reads that row.

The round-1 closing-diff review measured what rev-2 left: two receipt readers that split on every
receipt not pretty-printed ASCII, an owned path reaching a command string ungraded, an owned file
named differently from the hook appending a duplicate entry per merge, a wiring join that could not
tell two copies of one hook apart, and the `**` rule landing an opt-in hook at every adopter. Its
record is `reviews/2026-09-26-review-TOOL-aRepatriatedFork-36-closing-diff-round1.md`.

### Inventory

`resolve_owned_hook` — a Python function in `tools/settings-merge.py`, verb `resolve`, and its
`--resolve-hook` CLI mode. `check-wiring.sh` keeps a `sh.function` of that name which only calls it.
`derive_opted_out` — a Python function in `tools/govkit/govkit.py`, verb `derive`. `opt_in` — a new
descriptor file-rule key. `check-hook-destinations.sh` does NOT compare the owned join: gov keeps no
receipt, so that comparison could not move; the recall block of `check-wiring.test.sh` grades it.

### Files touched (estimate)

`tools/memory-recall/kit.toml`, the three recall sources' headers, the recall kit's README and adopter,
`tools/check-wiring.sh`, `tools/settings-merge.py`, `tools/check-hook-destinations.sh`,
`tools/check-wiring.test.sh`, `tools/govkit/govkit.py`, `tools/govkit/selftest.py`, the two docs,
`tools/install-prefix-waivers.txt` (re-keyed), `tools/install-prefix-carried.txt`, the map, and the
version carriers.

### Alternatives rejected

- A conf key naming the hook's path. The build rule allows a new key for an adopter's decision,
  never its layout.
- A new fragment token. `{here}` already names gov's copy; the target's copy is a fact about the
  target, which only the target's declaration can carry.
- Keeping `recall-opened.js` forked. Its fork protected nothing gov could overwrite.
- Removing the owned-hook seam, the review skeptic's recommendation. The owner ruled it hardened.
- A separate registry entry for the hook. Entry selection is the existing opt-in, but an entry's
  `{kit}` is its own directory, so the hook would land beside nothing that runs it.

## 5. Production-readiness checklist

- security — an owned path is graded with govkit's `[[own]].path` rule and refused otherwise, so no
  receipt edit reaches a command Claude Code runs; a refusal is loud in both CLIs and in the arm.
- perf / scale — one read of the receipt per resolved fragment; check-wiring runs python only when
  the receipt can hold an owned row.
- error / empty / loading states — an absent or unparsable receipt leaves the path unchanged.
- observability — `--resolve-fragment` prints the resolved path in both readers; an opt-in skip
  names the key that takes it.
- risks — an adopter whose settings run a copy the resolver does not name now reads UNWIRED, which
  is the state the wiring check exists to report.
- testing — AC1 to AC5, each red first.
- migration — adopters' receipts carry `forked` rows until their next update; handed to
  `DEPL-aRepatriatedFork-20` and to backlog row DEPL-aRepatriatedFork-23.
- user docs — `tools/memory-recall/README.md` step 2, the hook's own header, the adopter's usage
  note, and the runbook's maintenance paragraph.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs on the built tree, it exits 0.
  Red when: a recall source keeps `FORKED from` in its head with no `forked` rule, which arm 3d
  names, or a rule's `opt_in` is not an identifier, which arm 4c names.
- **AC2** — When the `[aRF-36]` arms of `tools/govkit/selftest.py` run as a slice, `apply` lands
  `query.py` and `extract.py` on a fresh target, prints no INCOMPLETE line, and lands no
  `recall-opened.js` while naming the `with_hook` key; a target declaring the key receives the hook,
  one spelling the reserved key is refused, and `plan` agrees with `apply`.
  Red when: the descriptor ships the hook through its `**` rule.
- **AC3** — When the AC8 block of `tools/check-wiring.test.sh` runs as a slice, an `adopter-owned`
  receipt row moves the resolved hook to `.claude/hooks/recall-opened.js` in both CLIs, an entry
  running another copy reads UNWIRED until one merge rewrites it, both copies present with the
  undeclared one wired read UNWIRED, and every crafted owned row is refused by both CLIs.
  Red when: the rev-2 `check-wiring.sh` and `settings-merge.py` are swapped in.
- **AC4** — When `python tools/settings-merge.py --selftest` runs, arms 13b and 13c pass. Red when:
  the rev-2 `resolve_owned_hook` is swapped in.
- **AC5** — When the synthetic `DEPL-dCarriedReceipt-10` block and the `DEPL-dCarriedReceipt-6`
  block of `tools/govkit/selftest.py` run as slices, every arm passes. Red when: a scratch gov lacks
  `adopters.toml`, which arm 10 refuses.
- **AC6** — `bash tools/check-kit-versions.sh` exits 0 and `python tools/govkit/govkit.py epoch`
  reports no FAILED entry. Red when: a moved kit kept its old value in any carrier.

## 7. Gates

`govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `hook destinations (every declared hook path ships)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `harness arms (fail branches armed or pinned)` · `check-wiring self-test` · `settings-merge selftest` · `govkit selftest`

New arm: `tools/check-wiring.test.sh` · an adopter-owned receipt row for the recall hook, its control, the crafted receipts and the both-copies state · none

## 8. Open questions

- **F1 — keep `recall-opened.js` forked?** RESOLVED (agent, 2026-09-25): no. §4 Evidence finds no
  write gov could make over inCMS's copy, which lives at a path gov never ships to.
- **F2 — replace the owned-hook seam, or harden it?** RESOLVED (owner, 2026-09-26): hardened, with
  one resolver in `settings-merge.py` that `check-wiring.sh` calls, govkit's `[[own]].path` grade,
  and a refusal for an owned file named differently from the hook.
- **F3 — does the hook stay opt-in?** RESOLVED (owner, 2026-09-26): yes; it lands only where the
  adopter asked for it, and one that declined keeps a green wiring check.

## 9. Revision log

- rev-1 · 2026-09-25 · initial draft, from the owner's ruling.
- rev-2 · 2026-09-25 · §2 S4 · AC5 · the scratch-gov fixture repair added once the slice found
  `TOOL-aRepatriatedFork-31`'s arm 10 refusing every scratch gov. Built: every arm green, each new
  one red on the old bytes.
- rev-3 · 2026-09-26 · S1 · S2 · S4 · S5 · S6 · S7 · §3 · §4 · §5 · §8 · AC1 · AC2 · AC3 · AC4 · AC5
  · folds the round-1 closing-diff review under the owner's F2 and F3 rulings. The owned-hook join
  moves to one reader that grades and refuses; the wiring join reads the command's path; the hook
  becomes an opt-in rule; the four remaining scratch-gov builders take `adopters.toml`; the §3
  hand-off gains inCMS's real route and nc's backlog row. The base moves to the rewritten parent.
  Built: every new arm green, each red on the rev-2 bytes.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "resolve a fragment hook path to where the target installed
the hook"` ranked `resolve` in `recall_conf.py` and three other resolvers, none of which reads the
receipt; the map does not scan `.sh`. The seams reused are `[[own]]` and its `adopter-owned` receipt
row from `DEPL-aRepatriatedFork-13`, govkit's `[[own]].path` grade from `resolve_owned_rows` and
`measure_contract_parity`, the canonical `resolve_python` block, and the per-entry `[kit.<eid>]`
table `target_context` already reads.

Recall terms used: `forked role recall extract query recall-opened fragment hook_path here own
adopter-owned receipt opt-in with-hook selection`.
