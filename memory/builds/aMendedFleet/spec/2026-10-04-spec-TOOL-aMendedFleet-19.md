# TOOL-aMendedFleet-19 — `gen_build_index.py --doctor <slug>` prints every failing build-folder rule in one pass

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 19

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-19-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-19-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

A new build folder owes several independent things: the front matter's `ids:`, the generated marker
pairs, the authored roster pair, a row in the README contract registry, and the canonical slots under
their byte ceilings. Each is graded by a different checker, two of those checkers stop at their first
failure, and one runs only on the full bar, so a hand-written folder surfaces its rules one bar cycle
at a time; node a has paid four cycles for one folder twice. This unit adds `--doctor <slug>`, which
runs both graders that own those rules over the whole tree once, keeps going past every failure, and
prints every failure attributed to that folder, so one run names everything owed. Report `[A#23]`,
brief unit 19.

## 2. Scope (IN)

- **S1** — `python tools/memory-tree/gen_build_index.py --doctor <slug>` is a new mode, dispatched
  beside `--new-build` and named in the usage line. The slug must match `backlog.SLUG_RE`, and the
  folder `<MEMORY_ROOT>/builds/<slug>/` must exist on disk. Observed by AC1 and AC4.
- **S2** — Grader one is the hygiene gate's own `--offenders` mode, run as a child from the kit's own
  directory, which prints one `check <n><TAB><key>` per offender and exits as the full check does.
  A key is ATTRIBUTED to the folder when it contains the folder's path or an id token of the shape
  `<FAMILY>-<slug>-<seq>` with the slug delimited on both sides, so a longer slug that begins with
  this one is never attributed. Observed by AC1, AC2 and AC6.
- **S3** — Grader two is the slot contract, run in process for this folder's README only: its row in
  the contract registry, then `slot_violations` over its text, then `scan_slot_budget` when the
  registry binds it. A `Problem` raised by the registry check is caught and reported when it names
  this README, and counted as elsewhere when it does not; the slot walk runs either way. Observed by
  AC1.
- **S4** — Output, one line per failing rule attributed to the folder, `doctor <slug>: <grader> <rule>
  — <detail>`, with `<grader>` one of `hygiene` and `slot-contract`, and `<rule>` the hygiene check
  number or one of `registry`, `slot` and `budget`. Then one summary line naming the failing count,
  both graders, the count of offenders the graders named outside this folder, and that the spec-token
  checker outside this kit was not consulted. Exit 1 when any rule fails, 0 when none does.
  Observed by AC1 and AC2.
- **S5** — A grader that cannot answer is never read as clean. The hygiene child exiting anything but
  0 or 1, or exiting 1 with no key, or no `bash` on the path, makes the run exit 2 and name that
  grader; the other grader's findings still print. Observed by AC5.
- **S6** — Tracked state is what both graders read. When any file under the folder is untracked, the
  run prints how many and the `git add` remedy before grading; when no file under it is tracked, it
  exits 2 with that remedy and grades nothing. Observed by AC3.
- **S7** — Refusals, exit 2 with the usage line: no slug, a slug failing `backlog.SLUG_RE`, a value
  carrying a `/`, and a slug naming no folder. Observed by AC4.
- **S8** — The kit README's Print modes paragraph names `--doctor`, its two graders, its cost and the
  tracked-state precondition. Observed by AC7.
- **S9** — `memory/map/generated/symbols.json` is regenerated for the new
  definitions. NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at
  the close is its check, and §7 names the leg that reads it.

## 3. Non-goals (OUT)

- Fixing anything. The doctor reads and prints; `--write`, `--new-build` and the author do the writing.
- A `--new-spec` skeleton that satisfies every live cutoff: `TOOL-aMendedFleet-20`, which edits the
  same dispatch and so builds after this unit.
- A path-scoped mode of the hygiene gate. Scoping that engine is a second mechanism in another file;
  this unit filters the full run's keys instead and pays its wall clock.
- The spec-token checker. It is a repo-root tool of the shipping repo, outside this kit, and a kit
  file names nothing outside itself by literal; the summary line says it was not consulted.
- Calling the doctor from `/session-kickoff`, `--preflight` or a pre-commit hook. Each is a follow-up
  for whoever owns that caller.
- `--new-build`'s mandate semantics, which the synthesis's item says to leave alone.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564`, re-verified 2026-10-04 against the report's claim at `ac65de998`.

- The four owed things, in the order they fire, are recorded in node a's auto-memory note on new build
  folders (2026-09-04, re-hit 2026-09-05): `ids:` and the generated pair through hygiene check 9, then
  the contract row and the roster pair through the `build README slot contract` leg, which the
  `--staged` pre-commit path never runs, then the slot canon and its byte ceilings.
- `cmd_check_format` calls `check_contract_registry`, which RAISES `Problem` on its first missing or
  dead row, so today the slot walk never runs on a folder whose row is missing. `cmd_check`'s render
  path raises on an unparseable front matter the same way.
- `check-memory-hygiene.sh --offenders` runs the full check, sends every human line to `/dev/null`,
  and prints one `check <n><TAB><key>` per listed offender on its own descriptor, with line locators
  stripped. A refusal exits 2 and prints no key. This is the machine-readable offender set the bar
  already grades the leg by.
- Both graders read TRACKED files: the slot contract enumerates READMEs with `git ls-files`, and a new
  build README is invisible to the index generator until it is added (node a's auto-memory, the note
  on tracked files).
- Wall clock: the `memory hygiene` leg's last row in `<git-common-dir>/gate-ledger.tsv` on node a is
  170.780 s, and the slot contract's is 2.043 s. PINNED from those rows, 2026-10-04.

### Inventory

- `cmd_doctor`, the mode's entry; `read_doctor_args`, its parse; `run_hygiene_offenders`, the child;
  `scan_doctor_offenders`, the attribution of S2; `check_folder_slots`, grader two for one README;
  `derive_doctor_verdict`, the exit code from both graders' outcomes. `cmd`, `read`, `run`, `scan`,
  `check` and `derive` are declared verbs. A name the lexicon leg refuses is replaced with its
  `--suggest` answer at build time, and this list is amended with a rev bump.

### Data model

One grader outcome, the shape `derive_doctor_verdict` reads:

```
{"grader": "hygiene" | "slot-contract", "answered": bool, "why": "<when not answered>",
 "code": <the hygiene child's exit, absent for the slot contract>,
 "mine": [("<rule>", "<detail>"), ...], "elsewhere": <int>}
```

`derive_doctor_verdict` applies S5 to `code` itself, so an outcome a caller marked answered still
reads unanswered when its child exited 2, or exited 1 naming no key.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/README.md`
- `memory/map/generated/symbols.json`

### Rollout

Additive: one new mode, no change to any existing mode's output or exit. `TOOL-aMendedFleet-20` adds a
mode to the same dispatch and usage line, so it builds after this unit. The memory-tree kit version
bump is owed once, at this build's close.

### Alternatives rejected

- **Make each grader report every failure instead of the first.** That changes the exit and the output
  of two merge-bar legs that other builds' records were graded by, for a question one folder asks.
- **Host it in `tools/unattended/unattended.sh`.** The rules are the memory tree's, and an attended
  author with no run open needs them most.
- **A new kit script.** A new moving part needs its own descriptor and declaration, and
  `gen_build_index.py` already owns `--new-build` and the slot contract.

## 5. Production-readiness checklist

- security — read-only. The slug is validated before it is joined into a path, and a value carrying a
  `/` refuses, so no argument reaches outside `<MEMORY_ROOT>/builds/`.
- perf / scale — one full hygiene run, about three minutes on node a, plus two seconds for the slot
  contract. That replaces up to four bar cycles, and S8 states the cost where the mode is documented.
- error / empty / loading states — clean prints one summary line and exits 0; untracked and grader
  failures exit 2 with their reason.
- observability — the summary line names both graders and how many offenders lie elsewhere, so a
  folder reading clean beside a red tree says so.
- risks — a hygiene message naming neither the folder nor an id of its slug is counted elsewhere,
  never attributed; the elsewhere count is what keeps it visible.
- testing — `--selftest` arms for the attribution and the verdict, and a staged break in a scratch
  clone.
- migration — none.
- user docs — the kit README's Print modes paragraph, S8.

## 6. Acceptance criteria

- **AC1** — When a scratch clone of the branch gains a tracked build README for the slug zDoctorProbe,
  holding only a title line, and `python tools/memory-tree/gen_build_index.py --doctor zDoctorProbe`
  runs there once, it exits 1 and prints at least three failing-rule lines, among them a `hygiene
  check` line and a `slot-contract registry` line. This is the staged break for S2 to S4.
  Red when: the run stops after its first failure, names only one grader, or exits 0.
  cost: one full hygiene run, about 171 s on node a.
  fixture: a `git clone --local` under a short `%TEMP%` directory, because a clone under the
  scratchpad hits the Windows path limit; check that `$TEMP` holds no stray `.memory-tree.conf` first.
- **AC2** — When `gen_build_index.py --doctor` names the slug aBatchedMinors and runs on the live tree, the summary line
  names both graders and an elsewhere count, and every failing-rule line it prints, if any, names that
  folder or an id of that slug. Red when: a line names another folder, or the summary omits a grader.
  figure: the elsewhere count is DERIVED at observation time.
- **AC3** — When the AC1 clone instead holds the probe README untracked, the run exits 2 and prints
  the untracked count with the `git add` remedy, and grades nothing. Red when: it exits 0 or prints a
  clean summary.
- **AC4** — When `gen_build_index.py --doctor` is called four times, with no slug, with the
  invalid slug x_y, with the builds path of aBatchedMinors and with the absent slug zNoSuchFolder,
  each exits 2 and prints the usage line. These four calls are the staged breaks for S7.
  Red when: any exits 0 or 1.
- **AC5** — When `gen_build_index.py --selftest` runs, an arm handing `derive_doctor_verdict` a hygiene
  outcome of exit 2 with no key, and another of exit 1 with no key, reads exit 2 naming `hygiene` in
  both, while the slot-contract findings beside them still print.
  Red when: either reads as clean or as exit 1.
- **AC6** — When `gen_build_index.py --selftest` runs, an arm handing `scan_doctor_offenders` four keys,
  naming the README of slug zA, an id of slug zA, the README of slug zAB and an id of slug zAB,
  attributes exactly the first two to slug zA and counts two elsewhere.
  Red when: a key of slug zAB is attributed to slug zA.
- **AC7** — When `grep -n -- "--doctor" tools/memory-tree/README.md` runs, the Print modes paragraph
  names `--doctor`, both graders, the cost and the tracked-state precondition.
  Red when: any of the four is missing.

## 7. Gates

`build-index selftest` · `build README slot contract` · `memory hygiene` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `kit version markers` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness`

New arm: tools/memory-tree/gen_build_index.py --selftest · the attribution arm of AC6 and the verdict arms of AC5, against today's generator, which has no doctor mode · none

## 8. Open questions

- **F1 — Where does the mode live?**
  Options: `gen_build_index.py`, beside `--new-build` and the slot contract; `unattended.sh`, beside
  the run verbs; a new kit script. A new script is a new declared moving part, and the run driver is
  the wrong home for a rule an attended author hits.
  RESOLVED (agent, 2026-10-04, delegated): `gen_build_index.py`.
- **F2 — How does the hygiene gate grade one folder?**
  Options: a new path-scoped hygiene mode; the full run's `--offenders` keys, filtered. The first is a
  second mechanism in a 2,800-line engine whose `--staged` mode already holds the corpus checks back;
  the second reuses the signature the bar grades by and costs one full run.
  RESOLVED (agent, 2026-10-04, delegated): filter the full run's `--offenders` keys.
- **F3 — Does the doctor run the spec-token checker?**
  Options: run it by its repo-root path; leave it out and say so. It sits outside this kit, so naming
  it from a kit file is the literal the install-prefix ban refuses, and its rules are the specs', not
  the folder's.
  RESOLVED (agent, 2026-10-04, delegated): leave it out, and the summary line says it was not
  consulted.
- **F4 — Slug, or slug or path?**
  Options: the slug, as the brief words it; either, as the synthesis words it. A path adds a second
  parse for the same folder.
  RESOLVED (agent, 2026-10-04, delegated): the slug; a value with a `/` refuses with the usage line.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from `cmd_check_format`, `check_contract_registry`, the mode
  dispatch and the hygiene gate's `--offenders` mode at base.
- rev-2 · 2026-10-04 · §2 S9 · §4 · §7 · M2 cross-read: the definitions this unit adds
  move `memory/map/generated/symbols.json`, which `TOOL-aMendedFleet-82` and the build's other
  code units regenerate and declare; this spec omitted the write, its Files touched row and the leg.
- rev-3 · 2026-10-05 · §4 Data model · build: the outcome carries the hygiene child's exit `code`,
  because AC5 hands `derive_doctor_verdict` an exit with no key and the rev-2 shape had no field to
  carry it in; the verdict applies S5 to that field.

## 10. Reuse audit

The seams extended are the mode dispatch in `main`, `cmd_check_format`'s per-README work
(`check_contract_registry`, `slot_violations`, `scan_slot_budget`) in
`tools/memory-tree/gen_build_index.py`, `backlog.SLUG_RE` for the slug, and the hygiene gate's
`--offenders` signature in `tools/memory-tree/check-memory-hygiene.sh`, which the bar already grades
the leg by. `python tools/codebase-map/reuse_lookup.py "print every failing rule for one build folder
in one pass"` returned only `build_*` name-stem matches, none a folder grader, and printed
`unscanned layers: .sh`, so the hygiene seam was found by reading its header rather than by the probe.
No existing seam runs both graders for one folder. Recall returned the `--new-build` scaffold's spec
`TOOL-dDerivedDocket-15`, the owner ruling `TOOL-dHonouredPark-1` that makes the roster pair mandatory
on every README, and the gotcha `check-format-grades-two-populations`, which is the population trap
S3 must not repeat. The report's cost claim, four rules over four bar cycles, matches node a's
auto-memory record of two such folders.

Recall terms used: build folder README slot contract offenders hygiene check 9 ids marker pairs new-build scaffold doctor
