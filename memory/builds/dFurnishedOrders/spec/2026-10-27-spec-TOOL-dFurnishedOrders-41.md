# TOOL-dFurnishedOrders-41 — the third spec audit's 12 upgrade-step minors: the walk run on the repository root, kit source narrowed to kit homes, kit homes matched to gov's descriptors, `project-owned` suites derived and mapped, and a scan that skips links and caps a read

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 08e30fef · streams tooling · order 25 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-38-round3-fix-return.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-38-round3-fix-return.md) | research | TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-42 |
| [2026-10-27-prompt-TOOL-dFurnishedOrders-38-round3-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dFurnishedOrders-38-round3-fix-brief.md) | research | TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-42 |
| [2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-42 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-2 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md`)
confirmed 28 MEDIUM and 3 LOW findings. BUILD-METHOD M4 batches them, and they split into two
disjoint write sets by M6 (§4 "Why two units"): this unit takes the 12 that land on the govkit
upgrade step, `tools/govkit/steps/retired_dispatch_args.py`, and `TOOL-dFurnishedOrders-42` takes the
other 19. Each report id is named once below and closed by its own scope item; ids the report merged
into one item still take one scope item each.

| Report item | Report id | Severity | Lands on | Scope item |
|---|---|---|---|---|
| M8 | 9 | MEDIUM | unit 35 AC2, S4 | S1 |
| M8 | 32 | MEDIUM | unit 35 AC2, S1; unit 36 AC2 | S2 |
| M8 | 10 | MEDIUM | unit 36 AC2 | S3 |
| M12 | 14 | MEDIUM | unit 35 S1, §4 | S4 |
| M15 | 19 | MEDIUM | unit 35 S1, §4 | S5 |
| M21 | 34 | MEDIUM | unit 35 S2, §4 | S6 |
| M13 | 15 | MEDIUM | unit 36 S1; unit 40 S3 | S7 |
| M14 | 17 | MEDIUM | unit 36 S1, §4, §10 | S8 |
| M14 | 24 | MEDIUM | unit 36 S1, §4 | S9 |
| M20 | 33 | MEDIUM | unit 36 S1, §5 | S10 |
| L1 | 8 | LOW | unit 36 S1, §5 | S11 |
| M19 | 31 | MEDIUM | unit 37 S23 | S12 |

## 2. Scope (IN)

- **S1** — id 9. Gov's own walk observed from the repository root. Unit 35's S4 observation runs
  `python tools/govkit/steps/retired_dispatch_args.py witness . checklist`, and the `prebuild` and
  `up` forms, from the repository root, so `.` is the root the `[[upgrade]]` row's `{target}` names;
  unit 35's ledger answers its AC2 in the AMENDED form, naming this item. Observed by AC1.
- **S2** — id 32. A target is a repository's top level. `derive_call_sites` resolves its target with
  `git -C <target> rev-parse --show-toplevel`, `GIT_DIR` and `GIT_WORK_TREE` unset in the child's
  environment, and a target that is not its own top level exits 1 naming the target and its top
  level, before any scan; a population read from a subdirectory never reaches `derive_tool_root`.
  Observed by AC2.
- **S3** — id 10. Unit 36's suite count observed from the repository root, as S1 states it; unit 36's
  ledger answers its AC2 in the AMENDED form, naming this item. Observed by AC1.
- **S4** — id 14. Kit source is the kit homes under the tool root, not the tool root. Where unit 35
  S1's test answers `<tr>`, the kit-file subtraction takes every directory under `<tr>` holding a
  `kit.toml`, and `<tr>/govkit`, and leaves every other path under `<tr>` in the population; unit 35
  AC3's `kit source <tr>/` rule word stands. An adopter that copied `govkit/` beside its own scripts
  keeps those scripts in the scan. Observed by AC1 and AC3.
- **S5** — id 19. The own-checkout branch checked against the target. When `derive_tool_root`
  answers through its own-ancestor branch (`tools/govkit/govkit.py:166-169`), the step accepts the
  answer only when `<answer>/govkit/registry.toml` is tracked by the target (`git ls-files
  --error-unmatch`); otherwise it takes the one tracked `govkit/registry.toml` at depth 0 to 2 of the
  target's own index as its tool root, refuses on more than one as `derive_tool_root` does, and falls
  through to the receipt and `kit.toml` rules on none. Observed by AC4.
- **S6** — id 34. A `kit.toml` home is a gov kit's copy. On a target with no receipt, a directory is a
  `kit.toml` home only when it is not the target root and its `kit.toml` parses and carries an `id`
  and a `home` equal to those of a descriptor `read_shipped_descriptors` (`govkit.py:13283`) returns
  from the step's own tool root; the directory's name is not compared, so a renamed copy still
  matches. A root `kit.toml`, or one naming no gov kit, takes nothing from the scan. Observed by AC3.
- **S7** — id 15. A flat entry is no directory home at its prefix. Beside unit 40 S3's target-root
  guard, a receipt entry whose resolved home equals its own prefix, which every entry whose descriptor
  `home` is `.` resolves to, adds no directory to the home set; its receipt rows stay subtracted by
  unit 35's receipt rule, and its `project-owned` suites by S8 and S9. Observed by AC5.
- **S8** — id 17. The `project-owned` rows derived as `govkit.py shipped` derives them. The step takes
  them from `read_shipped_descriptors` and `resolve_entry(gov_root, desc, canonical_ctx(eid))`'s
  `survivors` (`govkit.py:452-496`, `:498-508`) with `role` `project-owned`, as `cmd_shipped`
  (`:13312-13315`) does, never from a hand read of `<home>/kit.toml`; a descriptor kept outside its
  home, `tools/govkit/entries/push-main.kit.toml`, is read like any other. Each row's gov `src` maps onto
  the target: a `src` under gov's `<tool root>/<home>/` maps to the same rest under the target's home
  directory for that entry (unit 40 S1, or S6's directory); any other `src`, such as
  `.githooks/pre-push.runlog.test.sh`, maps verbatim. Unit 36 §10's "none a reader" is corrected by
  this item. Observed by AC5.
- **S9** — id 24. Only suites leave the scan. Of the S8 rows, only those whose file name matches
  `*.test.sh`, `selftest.py` or `test_*.py` are subtracted; `project-owned` means "the target authors
  it" (`govkit.py:406`), so an adopter's own `drift_signals.py`, `map_extractors.py` or
  `legacy-homes.txt` stays in the population. Unit 36 §4's reading of `project-owned` as "the suites
  a kit withholds" is corrected by this item. Observed by AC5.
- **S10** — id 33. A kit gov has no descriptor for. A receipt row whose `kit` names no descriptor
  `read_shipped_descriptors` returns adds no home, takes no `project-owned` rows, and is named on the
  scan line as `no gov descriptor: <kit>`, once per kit; the walk neither raises nor refuses on it.
  A home is matched to its descriptor by the receipt row's `kit` or the `kit.toml`'s `id`, never by
  its directory name. Observed by AC6.
- **S11** — id 8. A home at another prefix. A `kit.toml` home at `scripts/gov/workflows/`, matched by
  S6, maps its `project-owned` rows through S8 onto that directory, so the suite subtraction holds at
  any prefix and the subtraction falls to the `*.test.sh` rule alone only where S10 names the kit.
  Observed by AC6.
- **S12** — id 31. The scan skips links and caps a read. `derive_call_sites` (unit 37 S23) skips
  mode `120000` entries as it skips gitlinks, so a tracked link is never followed out of the target,
  and reads at most 4 MiB of a file, counting a file longer than that in unit 37 S23's
  `<u> unreadable`, unscanned. Observed by AC7.

## 3. Non-goals (OUT)

- The HIGH findings of the same report: `TOOL-dFurnishedOrders-38` to `-40`.
- The other 19 minors: `TOOL-dFurnishedOrders-42`.
- Rewording the spec text of units 35, 36 and 37: each item states the built tree's end state, and
  where a landed criterion cannot hold as written, that unit's ledger answers it AMENDED, naming the
  item.
- The report's left-shift gates, the spec-lint and checklist entries: no clause of this build names
  them.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-35` — S1's kit-source test, S2's `kit.toml` homes and AC2, which S1, S2, S4 to S6 settle (ids 9, 32, 14, 19, 34)
- **consumes-from** `TOOL-dFurnishedOrders-36` — S1's suite subtraction, its descriptor read and AC2, which S3 and S7 to S11 settle (ids 10, 15, 17, 24, 33, 8)
- **consumes-from** `TOOL-dFurnishedOrders-37` — S23's population read and its unreadable count, which S12 gives a link rule and a read cap (id 31)
- **consumes-from** `TOOL-dFurnishedOrders-40` — the declared-home derivation and its target-root guard, which S7, S8 and S10 extend (ids 15, 17, 33)
- **consumes-from** `TOOL-dFurnishedOrders-43` — the homes `derive_receipt_homes` answers, which S7's prefix guard, S8's `project-owned` mapping and S10's no-descriptor branch read (id 1 of the fourth audit)
- **hands-off** `TOOL-dFurnishedOrders-45` — S2's top-level refusal, S5's tool-root search, S6's `kit.toml` compare and AC3 and AC5's fixtures, which unit 45 S1 to S5 and S7 settle (ids 25, 9, 31, 32, 5, 18 of the fourth audit)
- **hands-off** `TOOL-dFurnishedOrders-46` — the govkit selftest arm whose sibling reads unit 46 S8 guards (id 22 of the fourth audit)

## 4. Design

### Why two units

M6 admits two batch units when their write sets are disjoint by all three of its clauses, and these
minors split that way:

- **Clause 1.** This unit writes `tools/govkit/steps/retired_dispatch_args.py` and
  `tools/govkit/selftest.py`; unit 42 writes the roles, runlog, hooks and kickoff suites and
  `tools/roles/roles_lib.py`. No path is in both, and neither writes a path on
  `memory/guides/SESSION-KICKOFF.md`'s `watch:` line.
- **Clause 2.** Neither reads a file the other writes as a contract or an acceptance input: this
  unit's criteria read the step and govkit, unit 42's the roles, runlog, unattended and kickoff kits.
- **Clause 3.** Neither touches `memory/DECISIONS.md`, a backlog shard, the run-state file or a
  generated index with its generator; each writes its own unit's ledger.

### How an item closes

Each item states the built tree's end state, and the pass does what is missing or records that a
landed unit already left it so, as `TOOL-dFurnishedOrders-37` §4 does.

### The kit files and suites, after this unit

```
target := git -C <target> rev-parse --show-toplevel; differs from <target> -> exit 1      S2
derive_tool_root(target) answers <tr>, <tr>/govkit/registry.toml tracked     -> kit source   S5
  kit files: every <d> under <tr> holding kit.toml, and <tr>/govkit          -> subtracted   S4
.governance/install.json present -> homes per unit 40 S1, none at the target root or at a prefix  S7
else  -> <d> holding a kit.toml whose id and home match a gov descriptor, <d> != target root     S6
suites: *.test.sh under each home (unit 36), and every shipped project-owned row of a receipt kit
  or a matched kit.toml kit, mapped by S8, whose name is *.test.sh | selftest.py | test_*.py      S9
receipt kit with no gov descriptor -> no home, "no gov descriptor: <kit>" on the scan line       S10
population read: skip 160000 and 120000; read <= 4 MiB, a longer file counted unreadable         S12
```

### The population on this repository after S4

At `08e30fef` one tracked file under `tools/` outside every `kit.toml` directory and `tools/govkit`
names `unattended-unit.js`, `tools/check-spec-tokens.test.sh`, and it spells neither key as a key
(PINNED, measured 2026-10-27 by `git grep -l "unattended-unit.js" -- tools ':!*.md'`). So gov's own
walk still passes after the narrowing; AC1 observes it at the pass, when the count is re-derived.

### What it does not check

- A gov flat entry's own file at gov's tool root, `tools/check-wiring.sh` say, is scanned on gov,
  since a flat entry has no directory home; one that names `unattended-unit.js` with a key would hit.
- A suite an adopter renamed away from the three suite names and that no `project-owned` row names,
  as unit 36 §4 already records.

### Inventory

Minted: the scan-line clause `no gov descriptor: <kit>` of S10; the 4 MiB read cap of S12, PINNED
by this spec. No function: every item is a branch of `derive_call_sites`.

### Migration

None: the steps have never run.

### Rollout

Live at landing, at order 25, after every unit it lands on. govkit's version moves for the kit
epoch leg where the step ships under it.

### Files touched (estimate)

- `tools/govkit/steps/retired_dispatch_args.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Climb to the top level when a subdirectory is the target (S2).** It changes unit 4 and 25's
  `{target}` contract silently; a refusal names the mistake instead.
- **Keep the whole tool root as kit source and list the copied-`govkit/` adopter as unchecked (S4).**
  It leaves an adopter's own scripts unscanned on exactly the targets that deploy kits.
- **Subtract every `project-owned` row (S9).** It hides adopter-authored code such as
  `drift_signals.py`, whose header says it is filled for the adopter's repo.

## 5. Production-readiness checklist

- security — S12 never follows a tracked link out of the target and caps every read; S2 reads git
  with the caller's `GIT_DIR` unset, so a hook environment cannot point the scan at another repo.
- perf / scale — one `git rev-parse`, one descriptor read and one `resolve_entry` per shipped entry
  per run; the read cap bounds memory per file.
- error / empty / loading states — S2's refusal, S10's named kit and S12's unreadable count each name
  their cause; none raises.
- observability — the scan line carries every rule word, count and named kit.
- risks — S4 scans gov's flat files at its tool root (§4 "What it does not check").
- testing — AC1 to AC7 by probes and fixtures; the arm of §7 at the close.
- migration — none.
- user docs — none: the step's printed line is what the walk shows.

## 6. Acceptance criteria

- **AC1** — When the step, retired_dispatch_args.py at S1's path, runs from the repository root as
  `witness . checklist`, `witness . prebuild`, `up . checklist` and `up . prebuild`, each exits 0,
  its scan line names `kit source tools/`, and its kit-suite count is at least 1.
  Red when: gov's own walk stops on a kit file, or the suite subtraction finds nothing on gov.
  figure: the counts are DERIVED at observation time.
- **AC2** — When the step, retired_dispatch_args.py at S1's path, runs from the repository root as
  `witness tools/govkit checklist`, it exits 1 naming `tools/govkit` and the repository's top level,
  and prints no scan line.
  Red when: a subdirectory target is scanned as if it were a repository.
- **AC3** — When `witness <target> checklist` runs over a scratch target with no receipt that tracks
  `<target>/scripts/govkit/registry.toml` beside a `<target>/scripts/run.js` naming
  `unattended-unit.js` and passing `checklist: 'x'`, it exits 1 naming that `run.js`; over one
  tracking a `kit.toml` at its root, and over one tracking `<target>/vendor/x/kit.toml` whose `id`
  names no gov kit, each beside an adopter `run.js` passing `checklist: 'x'`, each exits 1 naming
  that `run.js`; and over one tracking `<target>/scripts/recall/kit.toml` copied from
  `tools/memory-recall/kit.toml` beside a suite named x.test.sh in that directory passing
  `checklist: 'x'`, it exits 0.
  Red when: a copied `govkit/`, a root or a foreign `kit.toml` hides an adopter's script, or a renamed
  copy of a gov kit is not a home.
  fixture: scratch target repositories under `%TEMP%`, built by the pass.
- **AC4** — When a scratch target tracking `tools/govkit/registry.toml` holds, in an ignored
  `nested/` directory, a copy of this repository's `tools/govkit/` tree, and the copy's step runs as
  `witness <target> checklist`, its scan line names `kit source tools/`.
  Red when: the own-checkout branch answers a path the target does not track, and the walk stops
  on the kit files S4 subtracts.
  fixture: a scratch target under `%TEMP%` whose `.gitignore` lists `nested/`, built by the pass.
- **AC5** — When the scratch receipt target carries `prefix` `scripts`, an `engine` row for
  check-wiring.sh at the prefix root of kit `check-wiring`, an `engine` row of kit `drift-audit`
  under `scripts/drift-audit/`, and a `push-main` row, and tracks three files, an adopter suite
  mine.test.sh at the prefix root (A), an adopter `<target>/scripts/drift-audit/drift_signals.py`
  (B) and the kit's suite selftest.py beside B (C), A and B each passing `checklist: 'x'` and C
  spelling it as the kit's suite would, plus a copy of gov's pre-push runlog suite under the
  target's `.githooks/` spelling it too, `witness <target> checklist` exits 1 naming A and B and
  nothing else.
  Red when: a flat entry makes the prefix a home, an adopter-authored `project-owned` file leaves the
  scan, or a suite whose descriptor sits outside its home is scanned.
  fixture: a scratch receipt target under `%TEMP%`, built by the pass.
- **AC6** — When the receipt target also carries a row of kit `no-such-kit`, its scan line names
  `no gov descriptor: no-such-kit` and the exit is unchanged; and when a no-receipt target tracks
  `<target>/scripts/gov/workflows/kit.toml` copied from `tools/workflows/kit.toml` with a copy of the
  build-harness suite beside it spelling `"checklist": "CK"`, its scan line counts at least
  `1 kit suite(s)` and it exits 0.
  Red when: a kit gov no longer ships crashes the walk, or a home at another prefix loses its suites.
- **AC7** — When the unit 37 AC6 target also tracks a mode `120000` entry, written by `git
  update-index --add --cacheinfo` with a blob naming a path outside the target, and a 5 MiB text file,
  `witness` exits with no traceback and its unreadable count is exactly one more than it is without
  the two entries.
  Red when: a tracked link is followed out of the target, or a large file is read whole.
  fixture: the unit 37 AC6 scratch target under `%TEMP%`, extended by the pass.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `policy fixtures` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC2 AC3 AC4 AC5 AC6 AC7 · subdirectory, copied-`govkit/`, root, foreign, renamed, nested-checkout, flat-entry, `project-owned`, unknown-kit, other-prefix, link and over-cap targets, staged by restoring the whole-tool-root subtraction and the hand descriptor read · none

## 8. Open questions

- **F1 — How many units do the minors take?** Options: (a) one; (b) two, the govkit step's and the
  rest. (b) passes M6's three clauses (§4 "Why two units"), and the halves build concurrently.
  RESOLVED (agent, 2026-10-27, delegated): (b), rung 1, BUILD-METHOD M4's two-unit clause. widens:
  none · relaxes: none
- **F2 — What does a subdirectory target answer (S2)?** Options: (a) refuse, naming the top level;
  (b) climb to the top level. (b) changes the `{target}` contract of units 4 and 25 silently.
  RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the skeptic-judged alternative fix of ids 9,
  10 and 32. widens: none · relaxes: none
- **F3 — What does an over-cap file count as (S12)?** Options: (a) unit 37 S23's unreadable count;
  (b) a count of its own; (c) scanned on its first 4 MiB. (c) can miss a hit past the cap and report
  none; (b) mints a second "not scanned" word for one state. RESOLVED (agent, 2026-10-27,
  delegated): (a), rung 3, fewest new names. widens: none · relaxes: none
- **F4 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F5 — The units this one lands on are unbuilt.** Units 25, 35, 36, 37 and 40 are specced and
  unbuilt at `08e30fef`. RESOLVED (agent, 2026-10-27, delegated): the build run re-grounds on each at
  the pass and records any item a landed unit already closed, rung 1, the brief's rule. widens: none
  · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, the spec audit of the round-2 promotions' govkit upgrade-step
  minors batched: 11 MEDIUM and 1 LOW.
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **consumes-from** bullet mirroring TOOL-dFurnishedOrders-43 and the **hands-off** bullets mirroring TOOL-dFurnishedOrders-45, TOOL-dFurnishedOrders-46, promoted from the spec audit of the round-3 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended: `derive_call_sites` (`TOOL-dFurnishedOrders-25` S1, with units 35, 36, 37 and 40);
`derive_tool_root` (`tools/govkit/govkit.py:154-175`), whose branches S5 checks against the target;
`read_shipped_descriptors` (`:13283`), `resolve_entry` (`:452-496`) and `canonical_ctx` (`:498-508`),
the derivation `cmd_shipped` (`:13312-13315`) prints, for S8; `target_context` (`:1436-1477`) through
unit 40 S1. `python tools/codebase-map/reuse_lookup.py "files a kit homes on a target with no install
receipt"` ranked `resolve_kit_dir`, `kit_rel` and `kit_dir`, none a reader of a descriptor's
`project-owned` rows; `govkit.py shipped` is that reader, and S8 reuses its derivation, so no further
seam fits. The recall probe returned units 35 and 36 and the parent builds' reuse-scout records for
TOOL-dBoundRoles-18 and TOOL-dTotalRecall-20, none disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "which kit files and suites does the upgrade
step subtract on each target kind" --terms "upgrade step kit home kit.toml receipt project-owned
suite derive_tool_root toplevel symlink read cap"`
