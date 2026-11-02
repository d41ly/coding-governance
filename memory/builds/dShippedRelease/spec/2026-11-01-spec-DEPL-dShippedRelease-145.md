# DEPL-dShippedRelease-145 — `mint-regenerate-kits` runs every kit through `cmd_mint`, so the break its arm names reaches it

**Status:** DEFERRED · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 32 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 |
| [2026-11-01-build-DEPL-dShippedRelease-140-round5-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-140-round5-disposal-return.md) | research | DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 3 of `reviews/2026-11-01-review-DEPL-dShippedRelease-126-spec-audit-round1.md`, HIGH, item H1. Unit 128 S1 grades
each entry at rc 0 under `derive_regenerate_ctx` and never enters `cmd_mint`, so its §7 failing case,
`target_context` restored in `cmd_mint`, cannot red `mint-regenerate-kits`. A probe at gov's root printed 11 entries
accepted while `target_context` raised for all 11. AC2 is the only criterion entering `mint`, on a clone whose
`govkit.py` is the committed one, and the arm omits `mint-no-outcome-kit`, which it claims. This unit runs the
population through `cmd_mint` on a clone carrying the working tree, and repairs unit 128, order 31, at the next
step. The same failing case is ids 19, 50 and 31, items M13 and M17, in DEPL-dShippedRelease-144.

## 2. Scope (IN)

- **S1** — The clone. `build_mint_clone(tmp)` in `tools/govkit/matrix.py` runs `git clone --local` of `ROOT` into a
  scratch folder and `git checkout -b fx`, sets `user.name`, `user.email` and `core.autocrlf false` in the clone,
  copies every path `git status --porcelain` lists under the install prefix at `ROOT` over the clone, and commits
  them on `fx`. That commit is `<rev>`, and the tracked `.governance/deploy.toml` stays as cloned. So an uncommitted
  edit to `tools/govkit/govkit.py` runs in the clone. Observed by AC2, AC3.
- **S2** — The context ahead of the loop. `cmd_mint` builds `ctx = derive_regenerate_ctx(root, eid, descs[eid][0])`
  for each minted entry ahead of that entry's `[[regenerate]]` argv loop, and every read of an exit in the loop takes
  that value. So a context that raises reds a run whose every argv exits 0. Observed by AC2, AC3, AC4.
- **S3** — The run. `--case mint-regenerate-kits` lists the entries carrying a `[[regenerate]]` row by
  `read_descriptors`, never typed. In one clone it appends one comment line to one shell or Python file of each
  entry's epoch set, the `version_from` file excluded, commits, and runs `python tools/govkit/govkit.py mint --base
  <rev>` once as a child from the clone. It prints `<eid> · accepted` for each entry whose
  `mint: <eid> · <old> -> <new>` line printed, then the count. A non-zero exit, a `FAILED` line, a listed entry with
  no such line, or an empty list exits 1 naming it. Observed by AC1, AC2.
- **S4** — The second arm. `mint-no-outcome-kit` carries its own `New arm:` line in §7 and runs on S1's clone, so
  `target_context` restored in `cmd_mint` reaches it as an uncommitted edit. Observed by AC3.
- **S5** — What the count reads. Every listed entry is minted, so every one reaches S2's context, and the count is
  how many entries the break can reach. `mint` stops at its first refusal, so a break names one entry and not
  each. Observed by AC2.

## 3. Non-goals (OUT)

- Where the cases live: DEPL-dShippedRelease-140.
- The clone's null global config, its reuse across cases, and a run branch for `--prepare`: review ids 16, 20 and 48,
  in DEPL-dShippedRelease-144.
- A liveness count over a population that cannot read the failing value, as a gate: the audit's left-shift item, a
  gate of its own.

### Edges

- **consumes-from** `DEPL-dShippedRelease-122` — S1's route, which this unit's population runs
- **consumes-from** `DEPL-dShippedRelease-126` — `derive_regenerate_ctx`, the context S2 places
- **consumes-from** `DEPL-dShippedRelease-128` — S1, AC1 and §7, which this unit restates
- **consumes-from** `DEPL-dShippedRelease-140` — `MINT_CASES` and `--case`, the home of S3's case; the two share `tools/govkit/matrix.py`, so that unit's pass runs first
- **hands-off** `DEPL-dShippedRelease-144` — `build_mint_clone` and the two arms, which ids 16, 19, 31, 32, 48 and 50 read

## 4. Design

### Evidence

- `tools/govkit/govkit.py:13497` is `cmd_mint`. Its regenerate loop at `:13582-13594` runs after every version write, and a non-zero exit returns 1.
- `tools/govkit/govkit.py:126` is `repo_root`, which walks up from the file, so `mint` in a clone runs the clone's bytes, and `:13373` reads `<base>..<head>`, so a move must be committed.
- `tools/push-main.test.sh:736-766` is arm 24, a clone of `$SRC` at its committed HEAD, so a clone that does not overlay reads no staged break.
- A read-only probe on a scratch clone at `e4c33972` appended one line to one epoch file of each of the 11 entries, committed, and ran `mint --base <rev>`: `git clone --local` took 4.6 s, `mint` exited 0 in 13.6 s, and it printed 11 `->` lines. PINNED at `e4c33972`.
- `tools/govkit/govkit.py:6541` returns true at rc 0 for a descriptor declaring no block, so an rc 0 read of four of those entries can read nothing else (report ids 19 and 50).

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `build_mint_clone` | function, `tools/govkit/matrix.py` | `py.function`, OK by `--suggest` at writing |
| `check_mint_population` | function, `tools/govkit/matrix.py` | `py.function`, OK by `--suggest` at writing |

### Supersedes

- Unit 128 S1's "prints `accepted` or `refused` per entry for rc 0 under `derive_regenerate_ctx`": S3 here.
- Unit 128 AC1: AC1 and AC2 here.
- Unit 128 §7's first New arm: the two lines of §7 here.
- Unit 128 S2's "in a gov clone": S1's clone.

### Files touched (estimate)

- `tools/govkit/matrix.py`: S1, S3, S4
- `tools/govkit/govkit.py`: S2

### Alternatives rejected

- **A single helper `cmd_mint` and the case both call, at rc 0.** It observes a function and not the verb: a break in `cmd_mint` outside the helper stays green, and the measured run costs 18 seconds.
- **Keeping the rc 0 read and staging `derive_regenerate_ctx` losing `kit`.** It gives the arm a break it can see and leaves the population unrun, the complaint of the goal.
- **One clone per entry.** Eleven clones for what one `mint` run proves, since it moves every kit at once.

## 5. Production-readiness checklist

- security — N/A — fixture code under a scratch folder, and one context built earlier.
- perf / scale — S3 costs one clone and one `mint`, 18 seconds on this node at `e4c33972`, inside a leg whose ceiling is 7030.
- error / empty / loading states — S3 names the four failures, and an empty list is one of them.
- observability — one line per entry, then the count, and on red the child's own line.
- risks — a kit whose regenerate needs a state a clone lacks reds here, and a real landing would refuse the same way. `mint` stops at its first refusal, so S5's count is reach and never a per-entry verdict.
- testing — the criteria of §6 and the arms of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/matrix.py --case mint-regenerate-kits` runs at gov's root on a clean tree, it
  prints one `accepted` line per entry `read_descriptors` lists with a `[[regenerate]]` row, then that count, and
  exits 0.
  Red when: a kit's regenerate is refused, or the list is empty.
  figure: DERIVED at observation; 11 at `e4c33972`, and `integrations` joins at order 27.
  cost: one clone and one `mint`, 18 seconds, PINNED at `e4c33972`.
- **AC2** — When that case runs with `target_context` restored in `cmd_mint` as an uncommitted edit, it exits 1 and
  prints the child's `answers.` refusal; with the edit reverted it exits 0.
  Red when: the clone holds the committed `govkit.py`, so the arm's own break stays green.
- **AC3** — When `python tools/govkit/matrix.py --case mint-no-outcome-kit` runs with that same uncommitted edit it exits
  1, and reverted it exits 0 with `review-harness`'s version moved.
  Red when: a `ctx` built on a non-zero exit alone leaves the restored call unreached.
- **AC4** — When `python -c` walks `cmd_mint` by `ast`, the `derive_regenerate_ctx` call sits ahead of the `subprocess.run`
  of the regenerate loop, in that entry's own scope.
  Red when: the context is built only after an exit is read, and an exit 0 never builds it.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/matrix.py · covers AC1 AC2 · `mint-regenerate-kits`, its failing case `target_context` restored in `cmd_mint` as an uncommitted edit · none

New arm: tools/govkit/matrix.py · covers AC3 · `mint-no-outcome-kit`, its failing case that same uncommitted edit · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 3 (HIGH, item H1) of the round-5 spec audit.

## 10. Reuse audit

The seams extended are `cmd_mint` at `tools/govkit/govkit.py:13497` and the `MINT_CASES` home DEPL-dShippedRelease-140 gives `tools/govkit/matrix.py`.
`python tools/codebase-map/reuse_lookup.py "run the deployer's mint verb over every kit with a regenerate row in a clone"`
ranked the name-stem helper `rows` and neither `cmd_mint` nor arm 24, so the probe and the source disagree and the
source stands. The recall probe surfaced unit 3's scout and unit 126, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does a fixture prove the mint verb over every regenerate kit" --terms "mint regenerate population cmd_mint clone working tree overlay staged break matrix read_descriptors liveness"`
