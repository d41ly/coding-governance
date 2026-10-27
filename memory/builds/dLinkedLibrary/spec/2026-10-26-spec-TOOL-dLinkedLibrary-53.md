# TOOL-dLinkedLibrary-53 — the records-and-observations half of the round-1 audit's minors: 11 findings closed by a criterion, a waiver row or a declaration

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 27 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 |
| [2026-10-26-build-TOOL-dLinkedLibrary-53-deviation-531.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-53-deviation-531.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-52 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
50 MEDIUM and 14 LOW findings. BUILD-METHOD M4 batches them, and they split into two disjoint write sets
by M6: `TOOL-dLinkedLibrary-52` takes the 53 that change built code, a kit file, a generated map artifact
or the decision log, and this unit the 11 that touch none of these.

This unit's findings, each its own scope item, by report id: MEDIUM 12, 26, 13, 16, 35, 43, 56, 76; LOW
10, 27, 57. Most close a criterion a unit wrote that cannot pass or cannot fail on a correct build: this
unit observes what that criterion meant to, and the unit's acceptance ledger answers the criterion
AMENDED, naming this unit and the item. It lands after every unit (order 27): its items land on several
units, so it repairs none in particular.

## 2. Scope (IN)

- **S1** — id 12, R21. `TOOL-dLinkedLibrary-3` AC1's allowed hits include the succession row its S7
  writes in `tools/govkit/registry.toml`, id `codebase-map/reuse-lookup`; this unit's AC1 greps with
  that row allowed. Observed by AC1.
- **S2** — id 26, R21. The same allowance covers the generated `memory/map/generated/symbols.json` where
  it lists the step program's `retire_reuse_lookup`, an artifact rendered from a kept carrier. Observed by
  AC1.
- **S3** — id 13, R22. gap-mem-22, owned by this build, is observed: once TOOL-dTotalRecall-21 has landed,
  no per-worktree recall cache remains under `<git-common-dir>/recall/cache/`, and the one index file
  `<git-common-dir>/gov/index.db` is smaller than the 477 MB cache the gap measured; both figures go into
  this unit's ledger. Observed by AC2.
- **S4** — id 16, R25. `TOOL-dLinkedLibrary-6` AC7 compares the research view's count with one source
  predicate, `git grep -l '^kind: research-return$'` over the record folders, and its 72-record floor
  separately; this unit's AC3 makes that comparison. Observed by AC3.
- **S5** — id 35, R34. The `legacy` row sits in `marker-words.toml` and the `marker` namespace row holds
  no member list, as `TOOL-dLinkedLibrary-40` lands them; this unit observes both. Observed by AC4.
- **S6** — id 43, R37. Each carrier `TOOL-dLinkedLibrary-3` keeps that spells a basename its S1 takes out
  of the tree, the receipt fixture `tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json` (:64-69), the
  step program, the succession row and `help/reuse.md`'s section, carries a row in
  `tools/dead-path-waivers.txt` with its reason; `WIRE-INTO-PROJECT.md:527-535` is rewritten to name none
  of the three harness files. Observed by AC5.
- **S7** — id 56, R46. `TOOL-dLinkedLibrary-5`'s §7 leg line carries `policy fixtures`, the leg its Files
  touched trips through `tools/memory-tree/check-memory-hygiene.sh`: a rev bump of that spec with its §9
  line, at that unit's own pass or this one, whichever comes first. Observed by AC6.
- **S8** — id 76, R56. `.gitattributes` gives `memory/project/code-purpose-pending.txt` `merge=ours`, its
  `[[generated]]` row re-rendering it at landing; above the line for `memory/project/code-purposes.tsv` a
  comment says a conflict there is resolved by re-running `TOOL-dLinkedLibrary-15` S4's write, since
  `merge-rows.py` keys no TAB row and `union` duplicated rows in this repository before. Observed by AC7.
- **S9** — id 10, R60. `TOOL-dLinkedLibrary-25` AC8's failing case is planted: a scratch build holding a
  parsed spec header and a README `status:` key, over which `gen_build_index.py --check` names the key.
  Observed by AC8.
- **S10** — id 27, R60. The tree-level half of that criterion is a derived figure: the count of
  `memory/builds/*/README.md` carrying `status:` whose build holds a parsed spec, 0 at base, printed at
  this pass. Observed by AC8.
- **S11** — id 57, R69. `TOOL-dLinkedLibrary-3` S5's rewrite of `tools/unattended/PROTOCOL.template.md`
  leaves `memory/guides/UNATTENDED-PROTOCOL.md` at or under its high-water row in
  `tools/template-size-highwater.txt`, or the move is recorded by `check-template-size.sh --bump` naming
  that unit. Observed by AC9.

## 3. Non-goals (OUT)

- Every item that changes code, a kit file, a map artifact or the decision log:
  `TOOL-dLinkedLibrary-52`'s.
- Rewriting a closed spec's criteria: an item here observes the meaning, and the unit's ledger answers
  AMENDED. S7 is the one spec edit, a §7 leg line, since the leg join grades a live spec.
- Deleting the kept carriers of S6: `TOOL-dLinkedLibrary-3` keeps them as records of what an adopter was
  installed with.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-3` — AC1's allowed hits, the kept carriers of its deletion and S5's protocol rewrite, which S1, S2, S6 and S11 observe (ids 12, 26, 43, 57)
- **consumes-from** `TOOL-dLinkedLibrary-6` — AC7's comparison, which S4 restates (id 16)
- **consumes-from** `TOOL-dLinkedLibrary-40` — the `legacy` row of `marker-words.toml` and the member-free namespace row, which S5 observes (id 35)
- **consumes-from** `TOOL-dLinkedLibrary-5` — its §7 leg line, which S7 completes (id 56)
- **consumes-from** `TOOL-dLinkedLibrary-15` — `code-purposes.tsv` and `code-purpose-pending.txt`, whose merge lines S8 writes (id 76)
- **consumes-from** `TOOL-dLinkedLibrary-25` — S6 and AC8, whose failing case and figure S9 and S10 restate (ids 10, 27)
- **consumes-from** external — TOOL-dTotalRecall-21's move of recall's FTS tables into the one index file, which S3 measures
- **hands-off** `TOOL-dLinkedLibrary-64` — AC1, AC3 and AC8, which unit 64 re-observes after unit 52 (id 7 of the spec audit of units 37 to 53)

## 4. Design

### Why this half is disjoint

Its write set is `.gitattributes`, `tools/dead-path-waivers.txt`, `WIRE-INTO-PROJECT.md`,
`TOOL-dLinkedLibrary-5`'s spec, `tools/template-size-highwater.txt` where S11 records a move, and this
unit's acceptance ledger. `TOOL-dLinkedLibrary-52` writes none of them and reads none as a contract, and
this unit reads nothing that unit writes; neither touches a shared record of M6's condition 3.

### Evidence

- `tools/dead-path-waivers.txt` keys a row `<path>\t<ordinal>\t<line-text>\t<reason>`, and the leg
  `dead-path carriers (deleted files still named)` (`tools/gate-legs.json:1368`) runs
  `tools/check-dead-paths.sh`, whose `--list` prints every hit, waived or not.
- `WIRE-INTO-PROJECT.md:527-535` names `replay-phrases.py`, `rank_harness.py` and `scen-adversarial.json`.
- `.gitattributes:70` records that `merge=union` introduced a duplicate in 147 of 151 historical merges,
  and `merge.ours.driver` is configured.
- `wc -c memory/guides/UNATTENDED-PROTOCOL.md` printed 66859 at HEAD `823440497` against its high-water
  row of 66860.
- `query.py`'s `cache_dir` is `<git-common-dir>/recall/cache/<key>` (`tools/memory-recall/query.py:291`).

### Files touched (estimate)

- `tools/dead-path-waivers.txt`, `WIRE-INTO-PROJECT.md`: S6
- `memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-5.md`: S7
- `.gitattributes`: S8
- `tools/template-size-highwater.txt`: S11, only where the render grew

### Alternatives rejected

- **These items folded into `TOOL-dLinkedLibrary-52`.** That unit would pass the 49152-byte live-spec
  ceiling, and these eleven share no path with it, so M4 admits the split.
- **`merge=union` for the purposes file.** `.gitattributes:70` measured it duplicating rows.

## 5. Production-readiness checklist

- security — waiver rows and merge drivers only; `merge=ours` on a generated file is the house pattern.
- perf / scale — none.
- error / empty / loading states — S3 records the absence of the cache directory, never a zero size of a
  path not found.
- observability — each figure goes into the ledger with its command.
- risks — a waiver row hides a carrier that should have been rewritten; each row carries its reason.
- testing — AC1 to AC9 by probe and plant.
- migration — none.
- user docs — `WIRE-INTO-PROJECT.md`, S6.

## 6. Acceptance criteria

- **AC1** — When `git grep -n -E "reuse_lookup|reuse-lookup" -- . ':!memory/builds'` runs at this pass's
  tip, every hit sits in a file `TOOL-dLinkedLibrary-3` §4 keeps, in `tools/govkit/registry.toml`'s
  `[[retired]]` row, or in `memory/map/generated/symbols.json`.
  Red when: a live reader of the retired lookup remains, or a kept carrier is counted as one.
- **AC2** — When `git rev-parse --git-common-dir` locates the common dir, `ls <common>/recall/cache` finds
  no per-worktree cache, and `wc -c <common>/gov/index.db` prints fewer bytes than 477 MB.
  Red when: a per-worktree cache survives, or the one index is not smaller than the cache it replaced.
  fixture: TOOL-dTotalRecall-21 landed in this tree; until it lands the ledger records the criterion
  waiting, never green.
- **AC3** — When `python gen_build_index.py --check` prints the research view's count and
  `git grep -l '^kind: research-return$' -- 'memory/builds/*/build/'` counts the records, the two are
  equal, and the count is 72 or more.
  Red when: the view and its one source predicate disagree.
- **AC4** — When `grep -n 'word = "legacy"' marker-words.toml` runs in `tools/memory-tree`, it prints the
  row, and `grep -n "members" namespaces.toml` in `tools/playbook` prints no line in the `marker` row.
  Red when: the word is unregistered, or the namespace row carries members.
- **AC5** — When `bash tools/check-dead-paths.sh --list` runs at this pass's tip, each kept carrier of S6
  prints as waived, and `grep -c "rank_harness" WIRE-INTO-PROJECT.md` prints 0.
  Red when: a kept carrier is unwaived, or the runbook names a deleted file.
- **AC6** — When `grep -n "policy fixtures" memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-5.md`
  runs, it prints the §7 leg line, and that spec's §9 names the revision.
  Red when: the leg its Files touched trips is absent from its leg line.
- **AC7** — When `grep -n "code-purpose" .gitattributes` runs, it prints the `merge=ours` line for the
  pending file and the comment above the purposes file's resolution.
  Red when: either file is left without a stated merge behaviour.
- **AC8** — When `python gen_build_index.py --fixture --plant readme-status` runs over a scratch build
  holding a parsed spec and a README `status:` key, it exits 1 naming the key; and the tree count of S10
  prints 0.
  Red when: the planted key passes, or the figure is pinned rather than derived.
- **AC9** — When `wc -c memory/guides/UNATTENDED-PROTOCOL.md` runs at this pass's tip, it prints a figure
  at or under the high-water row `grep -n "UNATTENDED-PROTOCOL" tools/template-size-highwater.txt` prints,
  or that row names `TOOL-dLinkedLibrary-3`.
  Red when: the render grew past its row with no recorded move.

## 7. Gates

`dead-path carriers (deleted files still named)` · `unattended protocol size` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. (b) splits clauses the
  repaired units carry whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3,
  the precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — How is gap-mem-22 observed?** Options: (a) a criterion measuring the recall cache after
  TOOL-dTotalRecall-21; (b) a deviation moving the gap to dTotalRecall and the owned-gap list amended. (b)
  edits the README's goal statement, which a run may not amend (BUILD-METHOD M3). RESOLVED (agent,
  2026-10-26, delegated): (a), rung 1. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, 8
  MEDIUM and 3 LOW findings batched, split by write set from `TOOL-dLinkedLibrary-52`.
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-64, promoted from the spec audit of units 37 to 53; nothing else moved.

## 10. Reuse audit

Each item uses the seam its finding names: the dead-path waiver file and its `--list`, the house's
`merge=ours` driver, `gen_build_index.py --check`'s README refusal and the template high-water record;
nothing new is minted. `python tools/codebase-map/reuse_lookup.py "count the parts of a feature's reuse
entries"` ranked `counts` and `measure_typed_counts`, neither one of these mechanisms, so no existing
seam fits beyond the ones each item extends.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`
