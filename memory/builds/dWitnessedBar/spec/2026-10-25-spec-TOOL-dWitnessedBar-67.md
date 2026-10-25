# TOOL-dWitnessedBar-67 — the round-1 audit of units 64 and 65, its 19 minors batched: fixtures git cannot reshape, seed routes and probes that are bounded and stated, sweeps and readers that keep every case, and arms graded on the tree they build on

**Status:** DEFERRED · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 39 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-66-round6-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-66-round6-fix-return.md) | research | TOOL-dWitnessedBar-66 |
| [2026-10-25-build-TOOL-dWitnessedBar-67-deviation-671.md](../build/2026-10-25-build-TOOL-dWitnessedBar-67-deviation-671.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-66-round6-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-66-round6-fix-brief.md) | research | TOOL-dWitnessedBar-66 |
| [2026-10-25-review-TOOL-dWitnessedBar-66-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-66-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-66 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 64 and 65
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-64-spec-audit-round1.md`)
exited CONVERGED with 20 confirmed findings: one HIGH, id 6, which `TOOL-dWitnessedBar-66` takes, and
19 minors. BUILD-METHOD M4 batches every MEDIUM and LOW into one unit, or two only where they split
into disjoint write sets by M6's clauses so that both build concurrently. §4 "Why one unit" says why
these stay one. Each finding is named by report id and is its own scope item, including where the
report merged ids into one item. The minors land on both `TOOL-dWitnessedBar-64` and
`TOOL-dWitnessedBar-65`, so this unit repairs no single unit and builds above every unit in the build
(order 39). The report's ids 2, 8 and 10 were refuted by the audit itself and are no finding here.

| Report item | Severity | Report ids | Lands on | Scope items |
|---|---|---|---|---|
| M1 | MEDIUM | 1, 12 | unit 65 AC12 | S1, S2 |
| M2 | MEDIUM | 3 | unit 65 §4 Rollout, AC9 | S3 |
| M3 | MEDIUM | 7 | unit 65 S16, AC13, AC14 | S4 |
| M4 | MEDIUM | 11 | unit 65 §7 | S5 |
| M5 | MEDIUM | 13 | unit 64 S4 | S6 |
| M6 | MEDIUM | 15 | unit 65 S9, AC7, unit 64 S2 | S7 |
| M7 | MEDIUM | 16 | unit 65 S8, S9, AC7, unit 64 AC1 | S8 |
| M8 | MEDIUM | 17 | unit 65 S10, AC8 | S9 |
| M9 | MEDIUM | 18 | unit 65 S11, AC9 | S10 |
| M10 | MEDIUM | 19 | unit 65 S14, AC11 | S11 |
| L1 | LOW | 4, 21 | unit 64 S4 | S12, S13 |
| L2 | LOW | 5 | unit 65 AC4 | S14 |
| L3 | LOW | 9 | unit 65 §10, S3 | S15 |
| L4 | LOW | 14 | unit 65 S6, unit 64 §4 Rollout | S16 |
| L5 | LOW | 20 | unit 65 S17, §10 | S17 |
| L6 | LOW | 22 | unit 64 S3 | S18 |
| L7 | LOW | 23 | unit 65 S2, S3 | S19 |

That is 11 MEDIUM and 8 LOW findings by raw id.

## 2. Scope (IN)

- **S1** — id 1. The hook half of unit 65's AC12 is graded on variables `read_green_file` sets and on
  nothing else. No `verdict` read is added to the hook's adoption path, and the arm asserts no `GREEN`
  on the hook side. `TOOL-dWitnessedBar-66` replants the hook half on `rec_sha`. Observed by AC1.
- **S2** — id 12. The hook's CR strip is exercised on a second key. Beside unit 66's record, the arm
  writes a line `fingerprint<TAB>` followed by forty `c` characters and `<CR><LF>`, and asserts that
  `rec_fp` is forty `c` characters exactly. Its staged break, a `read_green_file` whose `fingerprint`
  read keeps the CR, reaches `rec_fp`. Observed by AC2.
- **S3** — id 3. Unit 65's AC9 gets a regression arm. `tools/run-gates/run-gates.gov.test.sh` runs the
  `os.unlink` stand-in probe over two aged `peer-signers-` files and an aged `peer-signers-d`
  directory, and asserts AC9's outcome. Its staged breaks are a sweep with no `OSError` catch, which
  reaches the read's exit, and a sweep that tests existence where unit 65 S11's sweep calls
  `is_file(follow_symlinks=False)`, which reaches the directory. Observed by AC3.
- **S4** — id 7. Unit 65's AC13 and AC14 are graded on the tree the unit builds on, which unit 60 S2
  has already changed. The arm evaluates, in a subshell, exactly the lines its awk reader spanned,
  from the `PM_SCRUB="` line to the line holding the closing quote, and compares bash's word list with
  the reader's. The first word is `GIT_DIR`. The last word is bash's last word, never a literal. AC14's
  "the base list" is the list the unmodified `tools/run-gates/post-merge.sh` holds at the build's
  HEAD. Observed by AC4.
- **S5** — id 11. This unit's §7 names `run-gates run-log line` and `pre-push run-log line`. Unit 65
  S14's `read_record_keys` has only two callers, both inside `write_runlog_verdict`
  (`tools/run-gates/run-gates.sh:2444-2445`), and they build the run-log line. Unit 65 S15's
  `read_green_file` feeds the push decision `.githooks/pre-push.runlog.test.sh:673-682` asserts.
  NOT OBSERVED: the item is this spec's declared gate set, which the close runs; no criterion of a
  unit observes its own §7.
- **S6** — id 13. Unit 64's fixtures are built so the machine's git config cannot reshape them:
  - each is made by `git -c init.defaultBranch=master init -q --ref-format=files`, so each is
    files-backed by construction;
  - the branch file each writes is `.git/` plus the output of `git symbolic-ref HEAD`, never a literal
    branch name;
  - section `2l`'s git calls run with `GIT_CONFIG_NOSYSTEM=1` and `GIT_CONFIG_GLOBAL` naming an empty
    scratch file, the form `tools/check-wiring.test.sh:1819` already uses.

  Observed by AC5.
- **S7** — id 15. Every git call of the seed's SHA resolution passes `timeout=60` (PINNED, the bound
  `tools/lib/health_log.py:44` already uses). That covers the HEAD probe, unit 64 S2's
  `symbolic-ref` and `for-each-ref` probes, and unit 65 S10's `--sha` resolution. Unit 65 S9's
  `subprocess.TimeoutExpired` handler then has a call that can raise it. Observed by AC6.
- **S8** — id 16. The seed resolves its SHA once per run. Under `--all` where a repository root
  resolves and HEAD does not, it reads the registration names only, prints
  `unarmed <name> no HEAD: <reason>` for each with the run's one reason, and writes nothing. Unit 65
  S9's "goes on to the next population" reads as that line for every population. Unit 65 AC7's
  stand-in replaces only the call whose argv holds `--verify`, so root discovery is untouched, and its
  two populations each carry the one reason of that run. Observed by AC7.
- **S9** — id 17. After unit 65 S10's `git rev-parse --verify --quiet <sha>^{commit}` exits 0, the full
  SHA it prints must start with the given hex, lowercased. Otherwise the seed exits 2 naming `--sha`
  and writes no home, so a branch or tag with an all-hex name cannot stand in for the object the
  operator abbreviated (§8 F3). Observed by AC8.
- **S10** — id 18. Unit 65 S11's hardening covers every filesystem call of the sweep: the listing of
  the git dir, `DirEntry.is_file(follow_symlinks=False)`, the stat that reads the entry's age, and the
  unlink. `FileNotFoundError` is silent. Any other `OSError` writes one stderr line naming the entry or
  the directory, and the read goes on. Observed by AC3.
- **S11** — id 19. Unit 65 S14's rewrite of `read_record_keys` keeps a third normalisation: an
  unterminated final line is read. The rewritten loop keeps a `|| [ -n "<line>" ]` guard over the
  variable it reads into, as today's loop does with `|| [ -n "$_rk_k" ]`
  (`tools/run-gates/run-gates.sh:2392`). Observed by AC9.
- **S12** — id 4. Unit 64's symbolic-loop fixture writes both files of the loop:
  `.git/<branch ref>` holds `ref: refs/heads/other`, and `.git/refs/heads/other` holds
  `ref: <branch ref>`, where `<branch ref>` is S6's `git symbolic-ref HEAD` output. Observed by AC10.
- **S13** — id 21. The one-file dangling chain is held from the clean side. Section `2l` gains a fifth
  fixture where only the branch file holds `ref: refs/heads/other` and no `refs/heads/other` exists. A
  commit would create `other`, so the seed reads it as unborn. Observed by AC11.
- **S14** — id 5. Unit 65's AC4 header half is read per file, with
  `grep -H ' order [0-9]* '` over unit 47's and unit 61's specs, so each file's line is named. AC4 is
  graded on its RUN.md and merge-base halves, and unit 65's AC4 ledger line names this item. Observed
  by AC12.
- **S15** — id 9. A comment beside the Python form of the segment rule in `tools/govkit/govkit.py` names
  the other Python spelling, the `--asks --path` check at `tools/memory-tree/gen_build_index.py:3267-3268`.
  It says that check is not imported because kits are copy-installed. It also says this rule refuses
  `1:x` by its second-character test, as S1's table and S2's bash `?:*` do, where that check's
  `[A-Za-z]:` admits it. Observed by AC13.
- **S16** — id 14. The two shared orders the report names:
  - Order 36 holds `TOOL-dWitnessedBar-64` alone, and `TOOL-dWitnessedBar-65` takes order 37. This half
    is applied in the commit that lands this spec, as unit 65's rev-2 and unit 64's rev-2, each with its
    §9 line, because a move made at order 39 would land after both units had built (§8 F2). Unit 66
    then repairs unit 65 at order 38.
  - Order 6 keeps `TOOL-dWitnessedBar-22` and `TOOL-dWitnessedBar-47`. M6 condition 2 does not hold
    for them: `read_registrations` reads every tracked `kit.toml` (spec-13:131), and unit 22 writes 26
    of them. They stay a tie the id-string sort orders, 22 before 47, and §4 Evidence records why no
    integer is free for unit 47 (§8 F2).

  Observed by AC14.
- **S17** — id 20. Unit 65 S17's arm asserts that
  `grep -cE '^[[:space:]]*(export[[:space:]]+)?PM_SCRUB\+?=' tools/run-gates/post-merge.sh` prints 1,
  so a second assignment, an append or a substitution reds it. §10 records that the arm re-reads the
  assignment text, guarded by this count, rather than reusing post-merge's fold. Observed by AC15.
- **S18** — id 22. Unit 64 S3's reason covers a probe that exits 0 and still ends the predicate. A
  `for-each-ref` that lists a row gives `git for-each-ref listed <first stdout line>`, and a
  `symbolic-ref` that prints a line not starting `refs/` gives `git symbolic-ref printed <line>`.
  Observed by AC16.
- **S19** — id 23. The segment rule's second-character test counts bytes in all three readers. The
  bash `case` runs under `local LC_ALL=C` inside the function holding it. The Python form compares
  `p.encode('utf-8', 'surrogateescape')[1:2] == b':'`. S1's table of unit 65 gains the row `é:x`,
  admitted by all three. Observed by AC17.

## 3. Non-goals (OUT)

- Re-wording unit 64's or unit 65's spec text, except S16's order move and the order sentences it
  makes stale, which unit 64's and unit 65's rev-2 §9 lines name. Each other item is closed by what
  this pass builds or observes, and a criterion it replaces is answered in that unit's acceptance
  ledger by name.
- The derived build-order region's `yes` beside order 6. S16 records why it stays, and the class gate
  the report names, a write-set check per shared order in `gen_build_index.py`, is not built. No clause
  of this build names it.
- The spec lints and checklist entries the report names as left-shift gates. No clause of this build
  names them. The staged breaks of §7 each name the variable or output their plant reaches, which is
  the regression this batch builds.
- An exact-match `for-each-ref`. S18 changes the reason only. A HEAD naming `refs/heads/a` beside an
  existing `refs/heads/a/b` keeps taking the no-HEAD route, since a commit could not create that ref.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-64` — its fixtures, its S3 reason rule, its two probes and its AC1, which S6, S7, S8, S12, S13 and S18 amend (ids 4, 13, 15, 16, 21, 22)
- **consumes-from** `TOOL-dWitnessedBar-65` — its AC12 arm, sweep, seed routes, `--sha` check, record reader, `PM_SCRUB` reader, segment rule, AC4 and order, which every other item amends (ids 1, 3, 5, 7, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 23)
- **consumes-from** `TOOL-dWitnessedBar-66` — the AC12 hook half replanted on `rec_sha`, beside which S1 and S2 add the `fingerprint` line and the no-`verdict` assertion (ids 1 and 12, report item M1)
- **hands-off** `TOOL-dWitnessedBar-71` — AC5's hostile config, which S6's isolation masks, planted at command scope through `GIT_CONFIG_COUNT` and proven in effect before the fixtures are graded (id 11 of the round-1 spec audit of units 66 and 67, item H2)
- **hands-off** `TOOL-dWitnessedBar-72` — S2's `fingerprint` line, put under the CR-reach canary so AC2's break can turn red on Windows, and that red recorded with its failing line (id 20, item H4)
- **hands-off** `TOOL-dWitnessedBar-73` — the round-1 spec audit of units 66 and 67's minors on this unit: the branch defences, the recorder's scope and members, the sweep grid, the later probes' stand-ins, the `PM_SCRUB` count and fold, the bytecode rule, the no-`verdict` arm, the govkit comment's spelling, AC14's reading, the held-leg statement, the cited seam and the empty no-HEAD `--all` (ids 2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 16, 17, 18, 21, 23, 24, 25, 26, 27, 28)

## 4. Design

### Why one unit

M4 admits a second unit only so that the two halves build concurrently. The seed half (ids 4, 13, 15,
16, 17, 21 and 22) writes the three `legacy_ledger.py` copies and `tools/lib/resolve-python.test.sh`.
The rest writes nine other files. So the two write sets are disjoint. Dispatch is strictly sequential,
a shared order included (`tools/workflows/unattended-build.js:76-80`), so a split would buy no
concurrency, and it would add one more shared order whose parallel declaration nothing acts on. One unit
holds all 19 findings.

### Evidence

- `read_green_file` sets seven variables, none from a `verdict` key (`.githooks/pre-push:1351-1369`).
  Its `fingerprint` read is `.githooks/pre-push:1355`.
- `PM_SCRUB` spans `tools/run-gates/post-merge.sh:35-38`. Its last word at `2a8eed0d` is
  `GATE_TURNSTILE_HOLDER`, and it holds no `GATE_SELECTION`. Unit 60 S2 adds seven names, among them
  `GATE_SELECTION`, at no stated position. At `2a8eed0d`, S17's `grep -cE` prints 1.
- `read_record_keys` loops with `while IFS=$'\t' read -r _rk_k _rk_v || [ -n "$_rk_k" ]`
  (`tools/run-gates/run-gates.sh:2392`) and strips the CR at `:2393`.
- On git 2.54.0.windows.1, `git -c init.defaultBranch=master init -q --ref-format=files` made a
  repository whose `git rev-parse --show-ref-format` printed `files`. With both loop files written,
  `git symbolic-ref -q HEAD` exited 128 with `fatal: No such ref: HEAD`.
- In a repository with one commit, `git branch a/b` then `git symbolic-ref HEAD refs/heads/a`,
  `git for-each-ref refs/heads/a` exited 0 and listed `refs/heads/a/b`.
- Under `LC_ALL=C.UTF-8`, a bash function holding `local LC_ALL=C` matched `é:x` against `?:*` as no
  match, and the same `case` without it matched. Python's `'é:x'.encode('utf-8')[1:2] == b':'` is
  False. The report cited `tools/unattended/lib-unattended.sh:301` as the `LC_ALL=C` idiom, but that
  file holds no `LC_ALL` at all; the repository's prefix form is `tools/check-wiring.sh:1155`.
- `gen_build_index.py:3268` refuses `folded.startswith("/") or re.match(r"^[A-Za-z]:", folded) or ".." in folded.split("/")`.
- The units at orders 7, 8 and 9, `TOOL-dWitnessedBar-19`, `-11`, `-14` and `-45`, each list a
  `kit.toml` under Files touched, so none can share an order with unit 47 under M6 condition 2. No
  integer between unit 61's order 5 and unit 46's order 10 is free.

### Inventory

Minted: the reasons `git for-each-ref listed <line>` and `git symbolic-ref printed <line>`, and the
fixture rows of S2, S13 and S19. No function, constant, plant, flag or file. Naming cells: none apply.

### Migration

None: no item changes stored data. S11 reads every record today's reader reads.

### Rollout

S16's order move is applied in the commit that lands this spec. Every other item is live at landing,
at order 39, after `TOOL-dWitnessedBar-64` (36), `TOOL-dWitnessedBar-65` (37) and
`TOOL-dWitnessedBar-66` (38). S1 to S4, S6 to S13 and S15 to S19 stage the regression arms under §7.
S5 is this spec's gate set, and S14 is observed by the main loop at the close.

### Files touched (estimate)

- `tools/lib/legacy_ledger.py`
- `tools/memory-tree/legacy_ledger.py`
- `tools/gate-lint/legacy_ledger.py`
- `tools/lib/resolve-python.test.sh`
- `tools/run-gates/run-gates.gov.test.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/verdict_backends.py`
- `tools/run-gates/regen.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/unattended/lib-unattended.sh`

### Alternatives rejected

- **Two batches, seed half and the rest.** §4 "Why one unit".
- **`git rev-parse --disambiguate=<hex>` for S9.** It lists every object with the prefix, trees and
  blobs included, so it needs a type filter and an ambiguity rule (§8 F3).
- **A literal last word for AC13 updated to unit 60's list.** It goes stale at the next edit of
  `PM_SCRUB`, which is the finding.
- **Hard-coding `master` in the fixtures without `-c init.defaultBranch=master`.** The branch file and
  HEAD then part on any machine whose default differs.

## 5. Production-readiness checklist

- security — S9 refuses a `--sha` a ref name can shadow, at the write boundary. S19 makes the
  containment rule byte-identical in three readers.
- perf / scale — no new git call; S7 bounds the existing ones at 60 seconds each.
- error / empty / loading states — S8, S10 and S18 turn a no-HEAD `--all`, a racing sweep and a
  silent ending probe into named outcomes, never a traceback or `exit 0`.
- observability — S18's reasons name what disqualified the probe; S10 names an entry it could not
  read or remove.
- risks — S17's count reds if unit 60 built its names as a second assignment, loudly and naming
  `PM_SCRUB`.
- testing — AC1 to AC17 by fixture, stand-in and scratch copy. The arms under §7 at the close.
- migration — none.
- user docs — none under `help/`. No user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'rec_verdict' .githooks/pre-push` runs on the built tree, it prints nothing.
  `grep -nE 'rec_[a-z_]+.*GREEN' tools/run-gates/run-gates.gov.test.sh` prints nothing, so no
  hook-side assertion compares a `read_green_file` variable with `GREEN`.
  Red when: the build adds a `verdict` read to `read_green_file`, or the arm expects `GREEN` from it.
- **AC2** — When the AC12 arm calls the sourced `read_green_file` on a record holding S2's
  `fingerprint` line, `rec_fp` is forty `c` characters and `printf %s "$rec_fp" | wc -c` prints 40.
  Against a scratch copy of `.githooks/pre-push` with the CR strip removed from the `fingerprint` read,
  the arm fails naming `rec_fp`.
  Red when: the `fingerprint` read keeps its CR, or the arm stays green with the strip removed.
- **AC3** — When a probe importing `verdict_backends.py` runs the peer read over two aged
  `peer-signers-` files and an aged `peer-signers-d` directory, three stand-ins each leave the read's
  verdict unchanged, no `Traceback` on stderr, and the directory in place:
  - `os.unlink` raising `FileNotFoundError` for one file and `PermissionError` for the other, with
    stderr naming the second file once;
  - the age read raising `FileNotFoundError` for one entry, with stderr silent about it;
  - the listing of the git dir raising `PermissionError`, with one stderr line naming the directory.

  `grep -n 'peer-signers-d' tools/run-gates/run-gates.gov.test.sh` names the arm.
  Red when: any filesystem call of the sweep raises into the read, changes its verdict, or touches an
  entry that is not a regular file.
- **AC4** — When unit 65's `PM_SCRUB` arm runs on the built tree, the reader's word list equals the
  word list bash evaluates from the same lines, its first word is `GIT_DIR`, and its last word is bash's
  last word. Over a scratch copy with `GATE_SELECTION` cut from the list at the build's HEAD, the arm
  fails naming `GATE_SELECTION`.
  Red when: the arm pins a literal last word, or compares against the list at base `cdfbd1cf`.
- **AC5** — When section `2l` builds unit 64's corrupt fixtures with `GIT_CONFIG_GLOBAL` exported to a
  file setting `init.defaultBranch=main` and `init.defaultRefFormat=reftable`, each fixture's
  `git rev-parse --show-ref-format` prints `files` and the seed still reads no HEAD in each.
  `grep -n -- '--ref-format=files' tools/lib/resolve-python.test.sh` names the fixture builder.
  Red when: a fixture inherits the outer config and reads as a clean unborn repository.
- **AC6** — When a probe importing `legacy_ledger.py` replaces `subprocess.run` with a stand-in that
  records the keyword arguments of every call whose argv opens with `git`, and runs the seed in the
  missing-object fixture and with `--sha` in a one-commit fixture, every recorded call carries
  `timeout=60`.
  Red when: any git call of the SHA resolution runs without a timeout.
- **AC7** — When `seed --all` runs over two registrations in the broken-ref fixture, stdout carries two
  lines opening `unarmed <name> no HEAD: `, one per registration, with the same reason, and no home is
  written. Under unit 65 AC7's two stand-ins, which replace only the call holding `--verify`, each
  population carries `git not runnable: ` under the timeout and `git rev-parse exit 2` under the silent
  exit.
  Red when: `--all` prints empty stdout where a root resolves, stops at its first population, or a
  stand-in breaks root discovery.
- **AC8** — When `seed --sha deadbeef` runs in a fixture with two commits and branches named `deadbeef`
  and `cafe1234` at HEAD~1, whose SHA does not start with `deadbeef`, it exits 2 naming `--sha` and
  writes no home. `seed --sha cafe1234` does the same.
  Red when: a hex-named ref's commit is stamped as the abbreviated object.
- **AC9** — When `read_record_keys`, cut and sourced as unit 65's AC11 does, reads a record whose last
  line `head<TAB>z` carries no trailing LF, it gives `head` as `z`. With the unterminated-line guard
  dropped in a scratch copy, the same case reads `head` as absent and the arm fails.
  Red when: the rewrite drops a final line that has no LF.
- **AC10** — When the seed runs in the symbolic-loop fixture, `git symbolic-ref -q HEAD` there exits
  128, and the seed's stdout opens `unarmed p no HEAD: fatal: No such ref: HEAD`.
  Red when: the fixture writes only the branch file, and the seed reads it as unborn.
- **AC11** — When the seed runs in S13's one-file fixture, it prints the `armed p` line unit 64's AC2
  prints and each row's SHA field is forty `0` characters.
  Red when: the predicate refuses a branch whose chain names a ref that does not exist yet.
- **AC12** — When `grep -n 'AC4' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-65*acceptance-ledger*`
  runs at the close, the line names this unit's S14 and the per-file
  `grep -H ' order [0-9]* '` reading.
  Red when: unit 65's AC4 is recorded green on a `sed -n 3p` over two files.
- **AC13** — When `grep -n 'gen_build_index' tools/govkit/govkit.py` runs on the built tree, it names a
  comment beside the segment rule's Python form that also names `1:x`.
  Red when: the comment is absent, so the two Python spellings part unseen.
- **AC14** — When `grep -H ' order [0-9]* '` runs over unit 64's and unit 65's specs, unit 64 reads
  `order 36` and unit 65 reads `order 37`. In the rendered build README, the build-order rows 36, 37,
  38 and 39 each read `no`.
  Red when: units 64 and 65 share an order again.
- **AC15** — When the `PM_SCRUB` arm runs over a scratch copy of `tools/run-gates/post-merge.sh` with
  `PM_SCRUB="${PM_SCRUB/GATE_SELECTION/}"` added after the assignment, it fails naming `PM_SCRUB` and
  the count 2. Over the unmodified file, the same `grep -cE` prints 1.
  Red when: a second statement that edits `PM_SCRUB` leaves the arm green.
- **AC16** — When the seed runs in a one-commit fixture after `git branch a/b` and
  `git symbolic-ref HEAD refs/heads/a`, stdout opens `unarmed p no HEAD: git for-each-ref listed ` and
  names `refs/heads/a/b`.
  Red when: the reason reads `git for-each-ref exit 0`.
- **AC17** — When the govkit selftest's `exists:` arm feeds the table row `é:x` to the three readers
  with `LC_ALL=C.UTF-8` exported, all three admit it. With `local LC_ALL=C` removed from the bash
  reader in a scratch copy, the bash reader refuses it and the arm fails naming `é:x`.
  Red when: the readers part on a non-ASCII first character.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `routed-commits selftest` · `shell-hygiene selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `run-gates gov canary` · `run-gates evidence` · `run-gates run-log line` · `pre-push run-log line` · `pre-push self-test` · `memory-hygiene self-test` · `codebase-map adopter e2e` · `codebase-map kit selftest` · `drift-audit selftest` · `memory hygiene`

`run-gates run-log line` and `pre-push run-log line` are S5's: their suites observe the two readers
unit 65 changes. The unattended kit's own suites are waived for this build's landing (README rule), so
S19's bash reader is observed through the govkit selftest arm. The four kit legs are held unless the
main loop sets GATE_SELFTESTS at the close.

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC2 AC3 AC4 AC15 · the `fingerprint` CRLF line, the three sweep stand-ins, the evaluated `PM_SCRUB` compare and the single-assignment count, staged red by removing the `fingerprint` CR strip (reaches `rec_fp`), dropping the sweep's `OSError` catch (reaches the read's exit), and adding a second `PM_SCRUB` statement (reaches the count) · FLOOR_ASSERTIONS raised by these assertions
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC9 · the unterminated final line, staged red by dropping the guard (reaches `head`) · FLOOR_ASSERTIONS raised by these assertions
New arm: tools/lib/resolve-python.test.sh · covers AC5 AC6 AC7 AC8 AC10 AC11 AC16 · section `2l`'s config-proof fixtures, the timeout recorder, the no-HEAD `--all`, the hex-named refs, the two-file loop, the one-file chain and the child-ref reason, staged red by dropping `--ref-format=files` (reaches the fixture's ref store), dropping the prefix check (reaches the stamped SHA) and dropping `timeout=` (reaches the recorded kwargs) · none
New arm: tools/govkit/selftest.py · covers AC17 · the `é:x` row, staged red by removing `local LC_ALL=C` from the bash reader (reaches its `case` result) · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. Units 64 and 65 are
  themselves derived and carry no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — How are the two shared orders the report names made honest (id 14)?** Options: (a) unit 65 to
  order 37 at this spec's landing commit, and orders 7 to 37 each raised by one so unit 22 takes order
  7 alone; (b) unit 65 to order 37, and unit 47 moved to share order 7, 8 or 9; (c) unit 65 to order
  37, and order 6 kept as a tie whose condition-2 failure §4 records; (d) both moves made in this
  unit's build pass. (d) lands at order 39, after units 64 and 65 have built, so AC14 cannot pass;
  veto 1 discards it. (b) has no slot, since every unit at orders 7 to 9 writes a `kit.toml` unit 47's
  reader reads, and it breaks unit 65 AC4's `order 6`; veto 1 discards it. (a) rewrites the status header of
  every unit at order 7 or above, 45 of them at `2a8eed0d` (DERIVED from the build-order region), most
  of which the audit did not name. That widens this LOW's write surface well past its tier; veto 3
  discards it. RESOLVED (agent, 2026-10-25, delegated): (c), rung 3, the one survivor. Its order-37
  half follows unit 65 §8 F3's precedent of a move applied at the landing commit.
  widens: none · relaxes: none
- **F3 — How does S9 stop a hex-named ref standing in for an abbreviated object (id 17)?** Options:
  (a) require the SHA `rev-parse` prints to start with the given hex; (b) resolve through
  `git rev-parse --disambiguate=<hex>`. Both pass AC8. (b) lists trees and blobs too, so it needs a
  type filter and an ambiguity rule, and more git calls under S7's bound. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, on the tie-break of fewer open questions. It reuses the one call unit 65 S10
  already makes, and a shadowed abbreviation is refused with exit 2 rather than stamped.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 64 and 65: 11
  MEDIUM and 8 LOW findings, batched.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-71, TOOL-dWitnessedBar-72 and TOOL-dWitnessedBar-73, promoted by the
  round-1 spec audit of units 66 and 67; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names. S1 and S2 extend unit 66's replanted AC12 arm. S3 and
S10 extend unit 65's AC9 stand-in probe. S6 reuses the config isolation `tools/check-wiring.test.sh:1819`
already writes, and S7 the 60-second bound of `tools/lib/health_log.py:44`. S11 keeps the guard of
`tools/run-gates/run-gates.sh:2392`. S19 reuses the `LC_ALL=C` form of `tools/check-wiring.sh:1155`.

For S15, the Python spellings of the segment rule in the tree are
`tools/memory-tree/gen_build_index.py:3267-3268`, which S15's comment cites, and three that were
considered and not used: `tools/runlog/runlog_lib.py:407`, `tools/settings-merge.py:180` and
`tools/memory-tree/routed_commits.py:161`. None is imported, because kits are copy-installed.

For S17, unit 65's §10 sentence "S16 and S17 reuse post-merge's own fold" does not describe S17. The
arm re-reads the assignment text with an awk range, and S17's single-assignment count is what guards
that re-derivation; post-merge's fold (`tools/run-gates/post-merge.sh:43`) is not reused.

`python tools/codebase-map/reuse_lookup.py "bound a git subprocess call with a timeout"` ranked `git`,
`run_git`, `GIT` and `read_git_output`. None is reachable from the copy-installed `legacy_ledger.py`,
so no existing seam fits beyond the bound named above.

Recall terms used: `python tools/memory-recall/query.py "what did the round-1 audit of units 64 and 65 find" --terms "staged red plant read_green_file rec_sha fingerprint sweep peer-signers timeout seed all hex ref ref-format PM_SCRUB"`
