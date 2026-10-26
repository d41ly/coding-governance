# TOOL-dDeclaredLoop-75 — the round-3 spec audit's 36 minors, batched

**Status:** DEFERRED · rev-8 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 39 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 |
| [2026-10-24-build-TOOL-dDeclaredLoop-75-deviation-751.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-75-deviation-751.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-75-deviation-752.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-75-deviation-752.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 |
| [2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-74 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md`)
exited CONVERGED with 43 confirmed findings over units 57 to 67, the round-2 promotions. Its seven highs
are units 68 to 74, one per id. This unit is the batch BUILD-METHOD M4 makes of the rest, every MEDIUM
and every LOW, each by its report id and each its own scope item, where the report merged ids into one
item too. The minors land on twelve units, so this unit repairs none in particular and builds after every
unit (order 39). Where a minor is the medium or low grade of a defect a high unit closes, the item here
is what that grade's fix asks beyond the high unit's mechanism.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 3, 13, 23, 43 | S1, S2, S3, S4 |
| M2 | MEDIUM | 4, 12, 42, 44 | S5, S6, S7, S8 |
| M3 | MEDIUM | 5 | S9 |
| M4 | MEDIUM | 6 | S10 |
| M5 | MEDIUM | 7 | S11 |
| M6 | MEDIUM | 8 | S12 |
| M7 | MEDIUM | 11, 40 | S13, S14 |
| M8 | MEDIUM | 14, 33 | S15, S16 |
| M9 | MEDIUM | 15 | S17 |
| M10 | MEDIUM | 16 | S18 |
| M11 | MEDIUM | 21 | S19 |
| M12 | MEDIUM | 27 | S20 |
| M13 | MEDIUM | 30 | S21 |
| M14 | MEDIUM | 31 | S22 |
| M15 | MEDIUM | 32 | S23 |
| M16 | MEDIUM | 34 | S24 |
| M17 | MEDIUM | 35 | S25 |
| M18 | MEDIUM | 36 | S26 |
| M19 | MEDIUM | 41 | S27 |
| M20 | MEDIUM | 46 | S28 |
| L1 | LOW | 10 | S29 |
| L2 | LOW | 17 | S30 |
| L3 | LOW | 18 | S31 |
| L4 | LOW | 20 | S32 |
| L5 | LOW | 24 | S33 |
| L6 | LOW | 25 | S34 |
| L7 | LOW | 26 | S35 |
| L8 | LOW | 38 | S36 |

That is 28 MEDIUM and 8 LOW findings by raw id. The report's three refuted findings, ids 9, 22 and 37,
are not in the disposal population.

## 2. Scope (IN)

- **S1** — id 3. `budget_state` collapses a draw row and its copies by `TOOL-dDeclaredLoop-61` S2's draw
  id, never by timestamp: 60 S4's timestamp twin rule is not built, so two distinct draws in one second
  stay two. Observed by AC1.
- **S2** — id 13. A draw row read with no draw id, which no shipped writer produces because
  `tools/loop/` is unbuilt at base, is counted as its own draw, 61 §5's rule, and named on
  `budget_state --explain` as `no draw id`. Observed by AC2.
- **S3** — id 23. One function, `derive_counted_draws(rows)` in `tools/loop/budget.py`, is the population's
  only dedup, called by 60's archive read and 61's id read alike. Observed by AC3.
- **S4** — id 43. The plant `pre-log-copy-twin` joins `budget.py --fixture`: a pre-log draw, its copy into
  the first log record by `TOOL-dDeclaredLoop-30` S9 and a rotation of the run-state file, counted once.
  Observed by AC4.
- **S5** — id 4. `tools/loop/budget.py`'s module docstring names the records root's owner,
  `.unattended.conf` through `TOOL-dDeclaredLoop-72`'s `resolve_memory_root`, citing
  `tools/unattended/unattended.sh:560` and :739, so the next change reads the driver's root and not 60
  S1's premise. Observed by AC5.
- **S6** — id 12. The plant `unset-driver-root` joins `budget.py --fixture`: `.unattended.conf` present
  with no `MEMORY_ROOT` and `.memory-tree.conf` at `records`, where the driver writes under `memory`;
  the read refuses by name. 60 AC2 planted under the root it read and passed either way; this plant
  discriminates. Observed by AC6.
- **S7** — id 42. `budget_state --explain` prints `root <r> · from <conf>` before the files it read, so a
  zero count read under a wrong root is visible. Observed by AC7.
- **S8** — id 44. The held line of `TOOL-dDeclaredLoop-64` S2 names where the root came from:
  `held — no commit adds <path> · root from <conf>`. Observed by AC8.
- **S9** — id 5. A row carrying ` · budget <slug>` counts only for the named build, never for the build
  whose file holds it, so a patch build's draw on its origin is charged once. Observed by AC9.
- **S10** — id 6. `TOOL-dDeclaredLoop-67` S29's property is observed, not read from bullets: for each of
  units 41 to 52, 54 and 55, the leg 67 §4's table names is run at that unit's pass commit in a detached
  scratch worktree, and each exit is recorded in this unit's acceptance ledger. Observed by AC10.
- **S11** — id 7. The concurrent-patch refusal of 67 S35 is the driver's: `tools/unattended/unattended.sh`
  reads live claims through `read_claims` (:2117) before it calls the budget draw for a patch build, and
  refuses there; `tools/loop/budget.py` takes no claim set and reads no claim. Observed by AC11.
- **S12** — id 8. The plant `fetch-other-branch` joins `position.py --fixture`: every source backdated,
  then `git fetch origin <other-branch>`; the answer is `stale-remote`, `TOOL-dDeclaredLoop-74` S1
  skipping that `FETCH_HEAD`. Observed by AC12.
- **S13** — id 11. `TOOL-dDeclaredLoop-57`'s refusal fixture commits the scratch target after `apply` and
  after the `gov_commit` edit, so `git status --porcelain` is empty before the update and an empty
  porcelain after it discriminates. Observed by AC13.
- **S14** — id 40. The refusal case runs on the write path, `update --write`: the refusal text, an empty
  porcelain, `install.json` equal to its committed bytes, and no `.governance/outbox/.update.lock` left
  behind (`tools/govkit/govkit.py:7039`). The read-only run checks the text alone. Observed by AC14.
- **S15** — id 14. Every draw-row writer, `TOOL-dDeclaredLoop-30` S9's, 48 S3's and 61 S1's, emits one
  order, `<ts> draw · <cause> · <item> · <spent>/<total>[ · budget <slug>] · <draw-id>`, and every reader
  parses the id by 61 S1's own regex, never by field position. Observed by AC15.
- **S16** — id 33. The ` · budget <slug>` field is matched as a whole field before the id, never anchored
  at the row's end, so a patch draw carrying both counts for the named build. Observed by AC16.
- **S17** — id 15. `position.py` resolves the common directory with
  `git rev-parse --path-format=absolute --git-common-dir`, never a path relative to its own cwd.
  Observed by AC17.
- **S18** — id 16. 67 AC12's observation reaches Python: a probe that duplicates `os.devnull` onto fd 0
  inside the interpreter and calls `check_terminal_proof` from `tools/lib/guarded_write.py`, asserting the
  refusal text that names `winpty` or a console, never a bare non-zero exit. Observed by AC18.
- **S19** — id 21. `check_transition_tables`' conf read resolves bash through `TOOL-dDeclaredLoop-70`'s
  `read_driver_conf`, and a PATH whose first `bash` is a stub exiting 1 neither reaches the stub nor reads
  an empty set. Observed by AC19.
- **S20** — id 27. 67 S21's two guards narrow to the files the class arm scans,
  `{prefix}/unattended/unattended.sh` and `{prefix}/runlog/model.py`. The spec-token join is run over a
  scratch copy carrying the edited manifest, and each live spec it still trips gets a dated row in
  `memory/project/spec-token-waivers.txt` keyed on its `routed-commits selftest <- <path>` hit and an ask
  row in that build's `BACKLOG.md`. Observed by AC20.
- **S21** — id 30. 67 S30's two legs carry the meta rows a new leg owes: `tools/govkit/subject-pins.tsv`
  by `govkit.py selfcheck --write`, their rows in `tools/run-gates/ceiling-evidence.txt`, and
  `memory/map/features/loop.md`'s `gate-legs` list. Their guards are `loop definition fixtures` <-
  `{prefix}/loop/loop_lib.py`, `{prefix}/loop/loop.toml`, and `loop selftest` <- `{prefix}/loop/`.
  Observed by AC21.
- **S22** — id 31. S10's probe also runs, at the pass commit of each of units 59, 60, 61, 62, 63 and 65,
  the sibling-minted leg running the file it edits: `loop guard fixtures` for 59, `loop budget fixtures`
  for 60 to 62, `loop transition tables` for 63 and `loop position fixtures` for 65. Each of those specs'
  hands-off bullets to this unit names its leg. Observed by AC22.
- **S23** — id 32. After 67 S15 and S52 change `tools/lib/commit_trailers.py`, its copies
  `tools/memory-tree/commit_trailers.py`, `tools/unattended/commit_trailers.py` and the
  `commit_trailers_py` block of `tools/runlog/model.py` are byte-identical with it, and §7 names the
  runlog legs and the resolver leg that guard them. Observed by AC23.
- **S24** — id 34. `TOOL-dDeclaredLoop-66`'s `render_order` carries a comment citing
  `TOOL-aSurfacedLexicon-17` and answering it: the cell derives from declared write sets and edges and
  says `no` wherever it cannot prove disjointness. An ask row in
  `memory/builds/aSurfacedLexicon/BACKLOG.md` names that ask as answered by 66, for its owner to dispose.
  The re-render population is every build README, 181 `| yes |` step rows in 43 READMEs, PINNED at
  `401ffdfb` on 2026-10-24; and `memory/map/features/build-readme-surface.md:109`'s "ties are the parallel
  group" reads that a tie is a parallel group only where `render_order` proves it. Observed by AC24.
- **S25** — id 35. `TOOL-dDeclaredLoop-63` §5's adopter-phase sentence lands in
  `tools/unattended/PROTOCOL.template.md` and its render `memory/guides/UNATTENDED-PROTOCOL.md`,
  regenerated in this pass. Observed by AC25.
- **S26** — id 36. The claimed-requires refusal's wider population is accepted and stated: every claimed
  kit's `requires` at `to_commit` is graded, a receipt predating the edges `tools/unattended/kit.toml`
  gained (`867b14a9f` review-harness, `a0116e508` settings-merge, `ff0b3dc32` kickoff-manifest) is
  refused until `apply --kits`, and the route names every unmet pair, never only the first.
  Observed by AC26.
- **S27** — id 41. The clean re-merge C is taken from `git merge-tree --write-tree`'s first output line on
  exit 0 or exit 1, and used when the policy path is not among the conflicted paths and its blob parses;
  any other exit code grades against the parents alone with 59 S3's printed line. Observed by AC27.
- **S28** — id 46. An unreadable claim set refuses the patch draw: `read_claims` returning 1 makes the
  driver print `budget: patch draw refused — claims unread: <CL_WHY>` and draw nothing, graded like a
  hold. Observed by AC28.
- **S29** — id 10. The leg-row key list of `tools/run-gates/README.md` names `stage`, as 67 S28 requires,
  and 67 AC20's version half is an invariant re-read after `TOOL-dDeclaredLoop-46` moves the version.
  Observed by AC29.
- **S30** — id 17. `tools/loop/breakpoints.py`'s module docstring states why the README path takes the
  driver's root: the driver reads each README at `$M/builds/<slug>/README.md`
  (`tools/unattended/unattended.sh:1348`), and the two confs are checked, not assumed, to agree.
  Observed by AC30.
- **S31** — id 18. `render_order`'s disjointness predicate is symmetric: two write sets intersect when some
  path of one equals, or lies under a directory of, some path of the other, in either direction.
  Observed by AC31.
- **S32** — id 20. `check_transition_tables` takes `PHASES_EXTRA` from `read_driver_conf` alone; 67 S23's
  own subshell source is not built, so `tools/loop/` carries one route to the population.
  Observed by AC32.
- **S33** — id 24. The transition-record merge weighing `TOOL-dDeclaredLoop-62` records, as 67 S17
  carries it into `tools/loop/README.md`, weighs a class-keyed `%P` census in
  `tools/memory-tree/merge-rows.py` keyed by draw id, mirroring `_BUILD_BACKLOG_RE` (:495), against
  union, and says why union is kept: a transition record is written once and only appended to.
  Observed by AC33.
- **S34** — id 25. `position.py --fixture` runs git with `GIT_CONFIG_GLOBAL` and `GIT_CONFIG_SYSTEM`
  pointed at empty files; the `unread` line names `core.logAllRefUpdates=false` where that setting left no
  `clone:` or tracking-ref reflog; and a plant clones with it set. Observed by AC34.
- **S35** — id 26. The criterion runner in `tools/loop/loop_witness.py` imports `GIT_ENV_LEAKS` from the
  memory-tree kit's `tree_lib` (:262) through `resolve_kit_dir`, which `TOOL-dDeclaredLoop-56` S17's
  requires edge makes reachable; no inline tuple ships. Observed by AC35.
- **S36** — id 38. 67 S42 and S43's citation re-spelling of 22 specs is not a material change
  (`memory/TEMPLATE-SPEC.md:67`), so it carries no rev bump; the 22 commit-addressed members
  `deviation_join.py` lists for it (:29-30) are named in this unit's acceptance ledger and each is recorded
  `author-recorded` at the close with that reason. Observed by AC36.

## 3. Non-goals (OUT)

- The seven highs' mechanisms: units 68 to 74, each its own unit.
- The report's left-shift gates and checklist entries: each class is recorded at the close, and each item
  above carries the observation that discharges its own defect.
- The refuted findings 9, 22 and 37.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-57` — the claimed-requires refusal and its fixture (ids 11, 36, 40)
- **consumes-from** `TOOL-dDeclaredLoop-59` — the merge grade's clean re-merge leg (id 41)
- **consumes-from** `TOOL-dDeclaredLoop-60` — the budget population and its archive read (ids 3, 4, 5, 12, 13, 23, 31, 42, 43)
- **consumes-from** `TOOL-dDeclaredLoop-61` — the draw id and its row grammar (ids 3, 13, 14, 23, 31, 33)
- **consumes-from** `TOOL-dDeclaredLoop-62` — the transition-record driver weighing (ids 24, 31)
- **consumes-from** `TOOL-dDeclaredLoop-63` — the adopter-phase reading and its protocol sentence (ids 31, 35)
- **consumes-from** `TOOL-dDeclaredLoop-64` — the held line and the README path (ids 17, 44)
- **consumes-from** `TOOL-dDeclaredLoop-65` — the last-fetch reading and its fixture (ids 8, 15, 25, 31)
- **consumes-from** `TOOL-dDeclaredLoop-66` — `render_order` and the re-render (ids 18, 34)
- **consumes-from** `TOOL-dDeclaredLoop-67` — S21's guards, S23's check, S28's README, S29's leg table, S30's legs, S35's refusal, S36's tuple, AC12, the trailer copies and the citation edits (ids 6, 7, 10, 16, 20, 21, 26, 27, 30, 32, 38, 46)
- **consumes-from** `TOOL-dDeclaredLoop-69` — the computable branch of the merge grade (id 41)
- **consumes-from** `TOOL-dDeclaredLoop-70` — `read_driver_conf` (ids 20, 21)
- **consumes-from** `TOOL-dDeclaredLoop-72` — `resolve_memory_root` (ids 4, 12, 17, 42, 44)
- **consumes-from** `TOOL-dDeclaredLoop-73` — the vintage-correct refusal (ids 11, 36, 40)
- **consumes-from** `TOOL-dDeclaredLoop-74` — the content-validated `FETCH_HEAD` population (ids 8, 15, 25)
- **consumes-from** `TOOL-dDeclaredLoop-76` — `resolve_memory_root_source`, from whose source S7 and S8 print the conf, and the syntax-tree rule inside which S5's and S30's docstrings name it; this pass re-runs the `no-own-conf-read` plant (the round-4 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-78` — the clean re-merge's three states, which S27 widens to a merge-tree exit 1 whose conflicts miss the policy path, a computable C that does not parse refusing by name (the round-4 spec audit's id 33)
- **consumes-from** `TOOL-dDeclaredLoop-80` — the fixture boundary, inside which S6's `unset-driver-root` plant writes both confs, so this pass's re-run of the `no-own-conf-read` plant exits 0 (the round-5 spec audit's id 20)
- **consumes-from** `TOOL-dDeclaredLoop-81` — the clean re-merge's exit table: S27 grades exit 1, and every other exit is the failed state, refused untrailered and never a fall to the parents (the round-5 spec audit's id 28)
- **consumes-from** `TOOL-dDeclaredLoop-83` — S27's fallback clause, restated to 81's exit table, and AC27's re-observation of `push-merge-tree-fatal`, which that unit writes before this pass (the round-6 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-79` — the pass-commit probe, S21's guards, S23's copies, S24's ask row, S25's protocol sentence and S29's key list, which that unit extends, mirrors in the descriptor, refreshes, re-observes, funds and pins (ids 3, 5, 9, 13, 18, 20, 21, 26, 28)
- **hands-off** `TOOL-dDeclaredLoop-82` — S27's exit-1 body, which that unit restates as present, absent or refused with its deleted-policy plant, and the share of `tools/loop/position.py` at step 39 (the round-5 spec audit's ids 4, 9)
- **hands-off** `TOOL-dDeclaredLoop-88` — S27's parent rows, which that unit completes with an exit 1 whose conflicted paths hold the policy path (the round-7 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-90` — the edge to 78 that counts C's states, which that unit restates to five (the round-8 spec audit's id 26)
- **hands-off** `TOOL-dDeclaredLoop-92` — S35's `GIT_ENV_LEAKS` route in `tools/loop/loop_witness.py`, which that unit moves onto the loop kit's `tree_lib` loader (the round-9 spec audit's id 14)
- **hands-off** `TOOL-dDeclaredLoop-94` — S35 as 92 restates it onto the loader, whose range that unit greps for `load_tree_lib` (the round-10 spec audit's id 4)

## 4. Design

### Write set

This pass writes the tools below; outside this build's folder it writes the shared renders S24 and S25
regenerate, one ask row each in `memory/builds/aSurfacedLexicon/BACKLOG.md` (S24) and in the BACKLOG of
each build S20 still trips, and S20's waiver rows, which the departures report lists. S10, S22 and S36
observe or record and write no code.

### The draw row, one grammar (S15, S16)

```
<ts> draw · <cause> · <item> · <spent>/<total>[ · budget <slug>] · <draw-id>
draw-id = 61 S1's regex, searched in the row, never taken by position
owner   = <slug> of " · budget <slug>" when present, else the build whose record holds the row   (S9)
```

### The pass-commit probe (S10, S22)

For each unit and leg of the two tables, the pass commit is the commit whose subject names the unit's id
as a built pass; `git worktree add --detach <scratch> <sha>` under a short `%TEMP%` path, the leg's argv
from `tools/gate-legs.json` at that sha run in it, the exit recorded, the worktree removed. A unit with
no pass commit is recorded `no pass`, never skipped.

### Evidence

- `read_claims` takes `strict`, `soft` or `quiet` and returns 1 with `CL_WHY` when the fetch fails or is
  killed by its bound (`tools/unattended/unattended.sh:2117-2140`).
- `WRITE_LOCK_REL = ".governance/outbox/.update.lock"` (`tools/govkit/govkit.py:7039`); `cmd_update` takes
  it through `demand_writable_target` only when `write` (:9228-9229), before 57's refusal runs.
- `routed-commits selftest` guards `{prefix}/lib/`, `{prefix}/memory-tree/` and
  `{prefix}/unattended/lib-unattended.sh` at base; `BROAD_LEG_FLOOR = 5` (`tools/check-spec-tokens.py:331`).
- `git log -G'^requires' -- tools/unattended/kit.toml` lists `ff0b3dc32`, `a0116e508` and `867b14a9f` after
  the file's first `requires`: PINNED 2026-10-24, re-derived by that command.
- `grep -c '| yes |$' memory/builds/*/README.md` totals 181 rows over 43 READMEs at `401ffdfb`: PINNED.

### Files touched (estimate)

- `tools/loop/budget.py`
- `tools/loop/breakpoints.py`
- `tools/loop/position.py`
- `tools/loop/loop_table.py`
- `tools/loop/guard.py`
- `tools/loop/loop_witness.py`
- `tools/loop/README.md`
- `tools/unattended/unattended.sh`
- `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/commit_trailers.py`
- `tools/memory-tree/commit_trailers.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/runlog/model.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/govkit/subject-pins.tsv`
- `tools/gate-legs.json`
- `tools/run-gates/ceiling-evidence.txt`
- `tools/run-gates/README.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `memory/map/features/loop.md`
- `memory/map/features/build-readme-surface.md`
- `memory/project/spec-token-waivers.txt`
- `memory/builds/aSurfacedLexicon/BACKLOG.md`
- `memory/builds/aOrientedCast/BACKLOG.md`, the build the narrowed guard is expected to leave tripped through
  TOOL-aOrientedCast-28's declaration of the unattended kit's directory, created with its heading where
  absent

### Alternatives rejected

- **One unit per minor.** M4 forbids it.
- **Two batch units.** The minors do not split into two disjoint write sets: `tools/loop/budget.py` and
  `tools/unattended/unattended.sh` are written by the budget, claim and grammar items alike, and
  `tools/gate-legs.json` by the guard and leg items.

## 5. Production-readiness checklist

- security — S11 and S28 fail closed on a patch draw the driver cannot clear; S6 refuses a misread root.
- perf / scale — S10 and S22 cost one scratch worktree and one leg run per named unit, minutes in total,
  once at this pass.
- error / empty / loading states — S2, S6, S28 and S34 each name the empty or unreadable case.
- observability — S7 and S8 print where the root came from; S28 prints the claim read's reason.
- risks — S26 refuses old unattended receipts on update until `apply --kits`, accepted and stated; S20
  writes waiver rows the departures report lists.
- testing — AC1 to AC36 as plants, probes and greps; the arms under §7, observed at the close.
- migration — none: every reader is unbuilt at base.
- user docs — S25's protocol sentence.

## 6. Acceptance criteria

- **AC1** — When `python budget.py --fixture --plant same-second-draws` writes two draws in one second,
  `budget_state` counts 2.
  Red when: twins are matched by timestamp and the two collapse.
- **AC2** — When `--plant idless-row` adds a draw row with no id, it is counted once and `--explain` prints
  `no draw id`.
  Red when: the row is dropped or merged silently.
- **AC3** — When `grep -c "def derive_counted_draws" budget.py` runs in `tools/loop/` it prints 1, and every dedup call
  site in the file calls it.
  Red when: a second dedup rule ships.
- **AC4** — When `--plant pre-log-copy-twin` runs, `budget_state` answers `open 1/<total>`.
  Red when: the copy and its twin count twice.
- **AC5** — When `python -c` prints `budget.__doc__` from the loop kit's `budget.py`, it names
  `.unattended.conf` and `resolve_memory_root`.
  Red when: the docstring credits `.memory-tree.conf` as the driver's root.
- **AC6** — When `--plant unset-driver-root` runs, the read exits non-zero printing `records root:`.
  Red when: `.memory-tree.conf`'s `records` is taken while the driver writes under `memory`.
- **AC7** — When `budget_state --explain` runs in that plant's agreeing variant, its first line reads
  `root records · from .unattended.conf`.
  Red when: the root goes unprinted.
- **AC8** — When `python breakpoints.py --fixture --plant wrong-root` runs, the held line ends
  `root from .unattended.conf` or `root from .memory-tree.conf`.
  Red when: the line names a path and not its root's source.
- **AC9** — When `--plant patch-archived` puts the archive in `dXPatch`'s own folder, `dX`'s count holds its
  rows and `dXPatch`'s does not.
  Red when: the row is charged to both builds.
- **AC10** — When the pass-commit probe runs `git worktree add --detach` at each pass commit of units 41
  to 52, 54 and 55 and runs that unit's leg, every exit is recorded in this unit's acceptance ledger and
  every one is 0.
  Red when: a pass broke its sibling-minted leg and only a hands-off bullet was read.
  cost: one scratch worktree per unit, minutes in total.
- **AC11** — When a scratch run of `unattended.sh` draws for a second patch build of one origin under a
  live claim of the first, the driver refuses naming the first run, and
  `grep -c read_claims budget.py` run in `tools/loop/` prints 0.
  Red when: the refusal lives in `budget.py` behind a stub claim set.
  cost: one scratch repository with a bare remote, seconds.
- **AC12** — When `python position.py --fixture --plant fetch-other-branch` runs, the answer is
  `stale-remote`.
  Red when: the other branch's `FETCH_HEAD` is counted.
- **AC13** — When 57's refusal fixture runs `update` over the committed target, `git status --porcelain`
  prints nothing before and after.
  Red when: the fixture leaves staged entries, so the clause cannot tell a refusal from a write.
- **AC14** — When the same fixture runs `govkit.py update --write --to <commit>`, it refuses, the porcelain
  is empty, the install receipt `install.json` equals its copy committed at `HEAD`, read by `git show`, and
  `test -e .update.lock` run in the target's `.governance/outbox/` exits 1.
  Red when: the write path leaves the lock or an edit behind.
- **AC15** — When `--plant id-after-budget` writes a patch draw carrying both fields and its twin copy,
  the row ends in the draw id and the twins collapse to one.
  Red when: a positional reader takes `budget <slug>` for the id.
- **AC16** — When `--plant patch-draw-with-id` reads that row for `dX`, it counts.
  Red when: the budget match anchors at the row's end.
- **AC17** — When `--plant cwd-outside-clone` runs the reader from a directory outside the scratch clone,
  it reads the clone's `FETCH_HEAD`, and `grep -c "path-format=absolute" position.py` run in `tools/loop/`
  prints 1 or more.
  Red when: the relative `.git` is stat'ed against the reader's cwd.
- **AC18** — When the probe `python -c` duplicates `os.devnull` onto fd 0 and calls `check_terminal_proof`
  on win32, the refusal names `winpty` or `console`.
  Red when: the shell fails the redirect before Python runs, or the device is admitted.
- **AC19** — When `python loop_table.py check` runs with a stub `bash` exiting 1 first on PATH and
  `PHASES_EXTRA="STAGING"` in the scratch conf, it passes with no `STAGING` row.
  Red when: the stub is run and the population reads empty.
- **AC20** — When `python tools/check-spec-tokens.py` runs in a scratch copy carrying the narrowed guards,
  it prints no `routed-commits selftest <-` hit outside a row of `memory/project/spec-token-waivers.txt`.
  Red when: a live spec of another build is tripped and unwaived.
- **AC21** — When `grep -c "loop selftest" tools/govkit/subject-pins.tsv tools/run-gates/ceiling-evidence.txt`
  runs, and `grep -c "loop selftest" loop.md` runs in `memory/map/features/`, and the same for
  `loop definition fixtures`, each file prints at least 1, and both rows of
  `tools/gate-legs.json` carry S21's guards.
  Red when: a meta row or a guard is missing.
- **AC22** — When the pass-commit probe runs `git worktree add --detach` at the pass commits of units 59 to
  63 and 65 and runs that unit's named leg, each leg exits 0, recorded in this unit's acceptance ledger.
  Red when: a pass broke the leg that runs its own file.
- **AC23** — When a probe compares the `commit_trailers_py` blocks of the canonical `commit_trailers.py`
  under the gov-internal lib, its two copies and `tools/runlog/model.py`, all four are byte-identical.
  Red when: a copy is stale after the canonical moved.
- **AC24** — When `grep -n "TOOL-aSurfacedLexicon-17" tools/memory-tree/gen_build_index.py
  memory/builds/aSurfacedLexicon/BACKLOG.md` runs, it prints the comment and the new ask row, and
  `grep -n "ties are the parallel group" memory/map/features/build-readme-surface.md` prints nothing.
  Red when: the ask goes uncited or the map line still asserts parallelism from a tie.
- **AC25** — When `grep -c "adopter phase"` runs over `tools/unattended/PROTOCOL.template.md` and
  `memory/guides/UNATTENDED-PROTOCOL.md`, both print at least 1.
  Red when: the sentence sits in one and the render is stale.
- **AC26** — When a probe calls `demand_claimed_requires` with a receipt claiming `unattended` without
  `review-harness` and `settings-merge`, the refusal names both pairs.
  Red when: the route names only the first unmet pair.
- **AC27** — When `python guard.py --fixture --plant push-merge-conflict-elsewhere` grades a merge whose
  merge-tree exits 1 on a non-policy file while the policy file's two-sided value merged cleanly, it
  exits 0.
  Red when: exit 1 drops the clean leg and the value is owed.
- **AC28** — When a scratch driver run draws for a patch build with its claim remote unreachable, it
  prints `claims unread` and records no draw row.
  Red when: the draw lands with the claim set unread.
- **AC29** — When `grep -n "stage" tools/run-gates/README.md` runs, the leg-row key list line is among its
  hits.
  Red when: `stage` appears only in the generated-files table.
- **AC30** — When `python -c` prints `breakpoints.__doc__`, it cites `README.md` under `$M` and
  `.unattended.conf`.
  Red when: the docstring keeps the false "driver defaults from" premise.
- **AC31** — When a probe renders a scratch build folder whose higher id declares a directory and whose
  lower id declares a file under it through `gen_build_index.py`, the group's cell reads `no`.
  Red when: containment is tested one way and the cell reads `yes`.
- **AC32** — When `grep -c "unattended.conf" loop_table.py` runs in `tools/loop/`, it prints 0.
  Red when: the check sources the conf itself beside `read_driver_conf`.
- **AC33** — When `grep -n "_BUILD_BACKLOG_RE" README.md` runs in `tools/loop/`, it prints the weighing line.
  Red when: the record omits the class-keyed option.
- **AC34** — When `--plant clone-without-reflog` clones with `core.logAllRefUpdates=false`, the `unread`
  line names that setting, and the other plants read alike under an empty global config.
  Red when: the fixture inherits the machine's git config.
- **AC35** — When `grep -c "GIT_ENV_LEAKS = (" loop_witness.py` runs in `tools/loop/` it prints 0, and
  `grep -c "GIT_ENV_LEAKS" loop_witness.py` there prints at least 1.
  Red when: an inline tuple ships.
- **AC36** — When this unit's acceptance ledger is read, it names the 22 members and the commit of each,
  and `deviations.py --report dDeclaredLoop` at the close lists each as recorded.
  Red when: the re-spelling folds silently into existing rev addresses.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `python resolver (behaviour + inline parity + idiom ban)` · `routed-commits selftest` · `tier2-review self-test` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted loop legs this pass keeps green, outside the base manifest, each declared by the unit
that mints it: `loop budget fixtures`, `loop breakpoints fixtures`, `loop position fixtures`, the leg
`loop guard fixtures`, the leg `loop transition tables`, the leg `loop definition fixtures` and the leg
`loop selftest`, none of them a leg at HEAD.

New arm: tools/loop/budget.py · covers AC1 AC2 AC4 AC6 AC9 AC15 AC16 · the same-second, id-less, pre-log twin, unset-root, archived-patch and two grammar plants · none
New arm: tools/loop/position.py · covers AC12 AC17 AC34 · the other-branch, outside-cwd and no-reflog plants under an empty git config · none
New arm: tools/loop/guard.py · covers AC27 · the conflict-elsewhere plant, staged against the exit-0-only clean leg · none
New arm: tools/loop/loop_table.py · covers AC19 · the stub-bash plant, staged against a bare bash · none
New arm: tools/govkit/selftest.py · covers AC13 AC14 AC26 · the committed-target refusal on both paths and the every-pair route · none
New arm: tools/memory-tree/gen_build_index.py · covers AC31 · the directory-in-higher-id fixture group · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — An unreadable claim set: refuse the patch draw, or admit it with a line (id 46)?** (a) refuse,
  naming `CL_WHY`; (b) admit with `claims unread`. (b) reopens the offline overdraw 67 S35 closes, which
  is a wider write than that unit priced, and veto 3 discards it. RESOLVED (agent, 2026-10-24,
  delegated): (a), S28. widens: none · relaxes: none
- **F3 — Scope the requires refusal to edges an update introduces, or accept the wider population (id
  36)?** (a) scope to `requires@to_commit - requires@gov_commit`; (b) accept, measure and name every pair.
  The receipts the finding names predate the three edges, so (a) refuses them too and adds a second
  vintage read; (b) satisfies the same criteria with one read and states the behaviour. RESOLVED (agent,
  2026-10-24, delegated): (b), S26. widens: none · relaxes: none
- **F4 — Dispose `TOOL-aSurfacedLexicon-17` here, or answer it and leave the disposal to its build (id
  34)?** (a) a dispose row in that build's BACKLOG; (b) a citing comment and an ask row its owner
  disposes. The build-level rule admits only an ask row in another build's BACKLOG, so (a) widens this
  build's write surface and veto 3 discards it. RESOLVED (agent, 2026-10-24, delegated): (b), S24.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-3 spec audit's 36 minors batched (28 MEDIUM, 8 LOW).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-76 and TOOL-dDeclaredLoop-78 and TOOL-dDeclaredLoop-79, written by the round-4 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-80 and TOOL-dDeclaredLoop-81 and TOOL-dDeclaredLoop-82, written by the round-5 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-83, written by the round-6 spec audit's disposal; nothing else moved.
- rev-5 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-88, written by the round-7 spec audit's disposal; nothing else moved.
- rev-6 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-90, written by the round-8 spec audit's disposal; nothing else moved.
- rev-7 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-92, written by the round-9 spec audit's disposal; nothing else moved.
- rev-8 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-94, written by the round-10 spec audit's disposal; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names, never a parallel copy: 61's draw id as the one dedup key
(S1 to S4), 72's `resolve_memory_root` (S5 to S8, S30), 70's `read_driver_conf` (S19, S32), the driver's
`read_claims` (S11, S28), `tree_lib.GIT_ENV_LEAKS` imported (S35), merge-rows' `_BUILD_BACKLOG_RE` class
census weighed (S33) and 66's `render_order` (S24, S31). `python tools/codebase-map/reuse_lookup.py
"read the adopter phase vocabulary from the driver conf"` and `"resolve the memory root the driver uses"`
ranked the driver's `phases`, `load_conf`, `resolve` and `resolve_kit_dir`, read above; no new reader is
minted where one of these exists.

Recall terms used: spec audit minors batch draw id budget root claims FETCH_HEAD merge-tree requires vintage render_order
