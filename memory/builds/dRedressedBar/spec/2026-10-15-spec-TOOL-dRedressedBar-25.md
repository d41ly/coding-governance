# TOOL-dRedressedBar-25 — the round-2 review's profiler findings, batched: the A/B verdict gate grades the condition, the selftest's guard covers its kit dir, and AC9's orphan is waited on

**Status:** CLOSED · rev-1 · 2026-10-15 · node d · Tier-2 · base ebce889c · streams tooling · order 19

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-15-build-TOOL-dRedressedBar-25-1-acceptance-ledger.md](../build/2026-10-15-build-TOOL-dRedressedBar-25-1-acceptance-ledger.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-25-1-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-25-1-spec-writer.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-25-2-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-25-2-revision.md) | research | TOOL-dRedressedBar-18 TOOL-dRedressedBar-21 TOOL-dRedressedBar-22 |
| [2026-10-15-prompt-TOOL-dRedressedBar-25-3-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-25-3-spec-writer.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-25-brief.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-25-brief.md) | research | TOOL-dRedressedBar-26 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 closing diff review over `e114f1356..5b30e4b47`
(`reviews/2026-10-15-review-TOOL-dRedressedBar-21-24-diff-review-round2.md`) read CLEAN WITH
FIXES, and the owner promoted all 14 of its confirmed findings on 2026-10-15 ("All 14, then stop").
BUILD-METHOD M4 batches them by disjoint write set. This is the profiler's batch: every item lands
in `tools/run-gates/measure_legs.py`, its fixtures, its descriptor or its leg's row in
`tools/gate-legs.json`. Unit 26 takes the temp-name lint and the runner's temps. Order 19 follows
unit 24's 18.

It closes these findings, by report id, each with the report item it sits in:

| id | grade | item | sits in, at `5b30e4b4` | what is wrong | closed by |
|---|---|---|---|---|---|
| 15 | HIGH | H1 | `tools/run-gates/measure_legs.py:3497-3505` | AC15's gate counts a `verdict` read inside a failure message, so deleting an arm's verdict condition leaves it green | S15 |
| 4 | MEDIUM | M1 | `tools/gate-legs.json:1276-1290` | the `measure-legs selftest` guard misses `tools/run-gates/README.md`, which `test_signal_docs` reads | S4 |
| 11 | MEDIUM | M1 | the same guard, from the seams lens | as id 4, with the reuse key carried forward | S11 |
| 23 | MEDIUM | M1 | the same guard, from the intent lens | as id 4, and the guard is a snapshot of files, not a derived rule | S23 |
| 20 | LOW | L1 | `tools/gate-legs.json:1283` | the guard names run-gates `*.py` files one by one, not the population `test_write_atomic_temp` walks | S20 |
| 18 | LOW | L6 | `tools/run-gates/measure_legs.py:3519-3551` | AC9's liveness rests on two fixed sleeps landing in order | S18 |

Id 15's fix was judged UNSOUND, and S15 takes the skeptic's corrected fix. Ids 4, 11 and 23 are
one defect by the record's merge. Ids 1, 2, 3, 5, 9, 12, 14, 16 and 17 were refuted and stay
refuted. Ids 6, 7, 8, 10, 13, 19, 21 and 22 are unit 26's.

Specs 18, 21 and 22 are CLOSED and describe what S4, S15, S18, S20 and S23 change. Their
corrections are this unit's spec-writer pass, `<w25>`, which runs at this unit's turn and before
its build pass (§4 "What this unit corrects in each spec").

## 2. Scope (IN)

Item S<n> closes report id n, and S24 is the record. S11 shares report item M1 with S4 and is
observed with it. Every line cited is at `bc6a4c9f`, whose `tools/` equals the reviewed tip's.

- **S15** — id 15, H1, by the skeptic's corrected fix. A new `check_verdict_read(node)` reads True
  for an `ast.Subscript` whose slice is the constant `"verdict"`, and for a call of an attribute
  `get` whose first argument is that constant. A new `read_blind_ab_arms(tree)` returns
  `(found, blind)`. `found` is every top-level `test_*` function holding a subtraction whose two
  operands each read `procs_total`, the rule at `:3499-3502` unchanged. `blind` is each found
  function holding no verdict read once every `check_arm` call in it is walked through its
  condition alone, the second positional argument or the keyword `ok`. Its name and its detail,
  the third positional argument or any other keyword, are not walked. A new
  `derive_verdictless_tree(source, name)` parses `source`, and in the top-level function `name`
  takes out of each `check_arm` condition every `and` conjunct holding a verdict read. A condition
  that holds one and is no `and` becomes the constant `True`. It returns the tree and the count of
  conjuncts taken out, and never touches a name or a detail. `test_ab_arms_read_verdicts`
  (`:3486-3508`) calls `read_blind_ab_arms` over this file and keeps its two assertions. It then
  stages a copy of each found function through `derive_verdictless_tree` and requires each count to
  be at least 1, `read_blind_ab_arms` over each copy to name that function blind, and the staged
  names to hold `test_serial_run` and `test_fork_count`. Its docstring says it reds when an arm's
  verdict condition is taken out while its failure message still reads the verdict. Observed by AC15.
- **S4** — id 4, M1. The `measure-legs selftest` row's `guard` in `tools/gate-legs.json`
  (`:1276-1290`) becomes exactly `{prefix}/run-gates/`, `{prefix}/gate-legs.json`,
  `.githooks/pre-push`, `{prefix}/process-monitor/census.py`, `{prefix}/process-monitor/reap.py`
  and `{prefix}/process-monitor/scope.py`. The directory entry covers `tools/run-gates/README.md`
  and every file the nine run-gates entries named. The manifest entry is there because S23's arms
  read the row: a commit that narrows it must trip the leg it narrows. The product commit carries the
  kickoff-manifest re-stamp at its parent that the ratchet's staged check requires. A second commit,
  `<p25m>`, re-stamps `last-audit:` in `memory/guides/SESSION-KICKOFF.md` at the product commit
  after a section B re-read, with a `manifest-audit:` line in its body, as unit 21's `361003ae2`
  did. Observed by AC4.
- **S11** — id 11, M1. The seams lens's reading of S4's defect: the leg's reuse key is built from
  its guard paths, so a README edit did not move it. Closed by S4. Observed by AC4.
- **S20** — id 20, L1. The guard covers the population `test_write_atomic_temp` walks, every `*.py`
  under the kit dir, through S4's directory entry, so a `*.py` added later under
  `tools/run-gates/` trips the leg with no edit to the row. Observed by AC20.
- **S23** — id 23, M1, the record's left-shift gate. A new `read_guard_misses(paths, legs_path=None)`
  returns every path of `paths`, and always the manifest's own path, that no entry of this tool's
  own selftest leg's guard covers, each top-relative and forward-slashed. It reads the manifest
  at `legs_path`, by default `os.path.join(os.path.dirname(KITDIR), "gate-legs.json")` as
  `run_profile` does (`:1689`), through `held_halves.load_manifest`. The row is the one whose argv carries
  `--selftest` and a token that resolves, through `resolve_prefix_token` and the tool root, to this
  file's top-relative path. Each guard entry is resolved the same way. A path is covered when it
  equals an entry that does not end in `/`, or sits under an entry as a directory, the runner's
  plain-guard rule (`tools/run-gates/run-gates.sh:3236-3238`, `:3285`). An entry outside the
  runner's plain class (`:3258-3260`) is returned itself, as a miss naming it. No single such row,
  an unreadable manifest, or a row with no guard is returned as one string naming the cause, so the
  caller's assertion reds and never passes empty. `run_profile`'s kit-path lines (`:1697-1699`)
  become a new `derive_kit_rel(top)`, which `run_profile` and `read_guard_misses` both call. `test_signal_docs`
  (`:3559-3577`) asserts `read_guard_misses` over the README path it opens returns nothing.
  `test_write_atomic_temp` (`:3183-3223`) asserts the same over every `*.py` path its walk finds,
  one that fails to parse included. Observed by AC23.
- **S18** — id 18, L6. `tools/run-gates/fixtures/measure-legs/orphan.sh` takes an optional second
  argument, a mark path. With it, the background subshell prints `late`, closes its stdout and
  stderr, and then creates the mark. So once the mark exists, `late` is in the capture and no
  process of the leg holds it. Without it the fixture behaves as today, which `test_interrupt_capture`
  needs. A new fixture, `waitmark.py <path> <bound_s>`, polls every 0.1 s, exits 0 once `<path>`
  exists and exits 1 once `<bound_s>` seconds pass without it, printing nothing. It joins the literal
  `project-owned` list in `tools/run-gates/kit.toml` (`:108-115`), which `test_fixtures_withheld`
  compares with the fixture directory, and a module constant `WAITMARK_PY` names it beside
  `ORPHAN_SH` and `SPAWN_PY` (`:3300-3301`). `test_legs_table`'s manifest (`:3520-3522`) becomes
  `orphan.sh 2 <mark>` as `orphan`, then `waitmark.py <mark> 30` as `hold`, the mark under the arm's
  temp dir. Its liveness half also requires `hold` to read verdict `ok`, the mark having come
  within the bound. Observed by AC18.
- **S24** — The record, in two passes. Specs 18, 21 and 22 each take ONE rev bump in this unit's
  spec-writer pass, `<w25>`, which runs before the build pass. Each revision line names
  `TOOL-dRedressedBar-25` and every report id §4's table assigns that spec, and each spec's §3
  Edges gains `hands-off` `TOOL-dRedressedBar-25`. The build pass writes no spec file but this
  one's status and date cells. Every reading below goes to this unit's acceptance ledger under
  `memory/builds/dRedressedBar/build/`, carrying `**Serves:** journal TOOL-dRedressedBar-25`.
  Observed by AC24.

## 3. Non-goals (OUT)

- No finding outside the round-2 record. The temp-name lint, the reuse-cache writer's import, the
  runlog arm's leftover pattern and the registry count are unit 26's.
- No checklist line in `memory/gotchas/`. The record offers one for H1 under
  `ab-arm-never-did-the-work` and one for L6 under `fixed-sleep-does-not-place-a-signal`. Each is a
  record of its own, and each finding here is left-shifted by its own arm, observed red first at
  the close (BUILD-METHOD M8). The in-file gates the record names are in scope: H1's staged copies,
  M1's in-arm guard assertion and L1's population guard.
- No guard-completeness proof. `read_guard_misses` grades the files its two arms name, never every
  file the selftest opens. Running a leg with everything outside its guard perturbed is the open
  ask TOOL-aPacedTurnstile-9.
- No change to what the profiler measures, records or refuses. `derive_kit_rel` moves three lines
  of `run_profile` into a function and changes no value.
- No change to `test_interrupt_capture`, which runs `orphan.sh 6` with no mark.
- No re-price of the `measure-legs selftest` budget or ceiling (`tools/run-gates/selftest-budgets.txt:74`).
- No kit version move. The lander mints a version for a move of shipped bytes, so a branch owes none
  (`tools/govkit/govkit.py:13428`, "WHERE THE BUMP IS MADE").
- No help page or README change. No sentence of `help/measure-legs.md` or the README's profiler
  section describes an arm, a fixture's argv or the leg's guard.

### Edges

- **consumes-from** `TOOL-dRedressedBar-18` — the profiler's `run_profile`, whose kit-path lines S23
  extracts, the fixture directory, the `measure-legs selftest` row and its guard, and its spec,
  whose guard paragraph `<w25>` corrects.
- **consumes-from** `TOOL-dRedressedBar-21` — `test_write_atomic_temp`, which S23 extends, and S11's
  two guard entries, which S4 folds into the directory; its spec, which `<w25>` corrects.
- **consumes-from** `TOOL-dRedressedBar-22` — `test_ab_arms_read_verdicts`, `test_legs_table`,
  `test_signal_docs` and `orphan.sh`, which S15, S18 and S23 change; its spec, which `<w25>`
  corrects.
- **hands-off** external — the two checklist lines §3 names, for the build's close to dispose.

## 4. Design

### Evidence, read at `bc6a4c9f` on 2026-10-15

`git diff --stat 5b30e4b47 bc6a4c9f0 -- tools` prints nothing, so every line the record cites holds.

- `test_ab_arms_read_verdicts` builds `reads` from every `ast.Constant` value and `ast.Attribute`
  name in the function (`:3497-3498`) and checks `"verdict" in reads` (`:3505`).
  `test_serial_run`'s AC1 condition reads both verdicts (`:2332`) and its failure message reads
  them again, `six["verdict"]` (`:2334`). `test_fork_count`'s condition reads `.get("verdict")`
  (`:2717`), and so does its message (`:2718-2719`). `test_resolution_disabled` reads three verdicts
  in one `check_arm` condition (`:2435`) and subtracts in its sibling (`:2438`), whose message reads
  none.
- `check_arm(name, ok, detail="")` (`:2029-2031`) is every arm's assertion.
- The guard (`tools/gate-legs.json:1276-1290`) lists eight exact run-gates entries, the fixture
  dir, `.githooks/pre-push` and three process-monitor files. `check_guard_trips`
  (`tools/check-spec-tokens.py:494-503`), with `{prefix}` read as `tools`, returned False for
  `tools/run-gates/README.md` and for a `new_writer.py` under `tools/run-gates/`.
- `test_signal_docs` opens `os.path.join(KITDIR, "README.md")` (`:3564`). `test_write_atomic_temp`
  walks `os.walk(KITDIR)` for every `*.py` (`:3193-3198`).
- `{prefix}/run-gates/` is already a guard of six legs, and the whole guard of
  `profile-bar selftest` and `run-gates adopter e2e`. `BROAD_LEG_FLOOR` is 5
  (`tools/check-spec-tokens.py:262`), so the spec-tokens join already drops that entry as broad. govkit's guard taxonomy files `{prefix}/run-gates/` and
  `{prefix}/gate-legs.json` as kit-relative (`tools/govkit/govkit.py:2553-2581`), as it does for
  `run-gates gov canary`'s guard today.
- The runner selects a guarded leg with `git diff --quiet "$BASE" -- <guards>` (`run-gates.sh:416`)
  and slices its reuse key by exact path or directory (`:3201-3206`, `:3277-3288`). Its comment
  says that rule is git's pathspec for a plain guard (`:3236-3238`), and its plain class is
  `:3258-3260`. No guard in `tools/gate-legs.json` carries a glob.
- `run_profile` reads the manifest at `os.path.dirname(KITDIR)` (`:1689`) and derives `kitrel`
  and the tool root (`:1697-1700`); `kitrel` is read again at `:1739`.
- `test_legs_table` runs `orphan.sh 2`, then `spawn.py 0 5` (`:3520-3522`), and reads the orphan's
  `log_bytes` 11 with `raw_kept` empty (`:3549-3551`). The run end calls `write_final_capture` once
  per leg (`:1961-1968`), which deletes the capture only when no process holds it (`:1612-1615`).
- Measured on node d, 2026-10-15, with Git for Windows' bash 5.3.9 under Python 3.12.10: a Python
  parent opened a file and handed it as stdout and stderr to `bash -c`, whose background subshell
  printed `late`, created a mark and slept 4 s more. With `exec 1>&- 2>&-` before the mark,
  `os.remove` on the file succeeded the moment the mark appeared. Without it, the remove failed
  with WinError 32 while the subshell slept.

### The A/B verdict gate (S15)

```python
found, blind = read_blind_ab_arms(ast.parse(source))
# ... the two assertions of today, over found and blind
for name in found:
    copy, cut = derive_verdictless_tree(source, name)
    staged[name] = (cut, name in read_blind_ab_arms(copy)[1])
# LIVENESS: each cut >= 1 and each copy named blind; test_serial_run and test_fork_count staged
```

The two functions share what a verdict read IS, through `check_verdict_read`, and never where one
is skipped. Only `read_blind_ab_arms` skips a name and a detail, and `derive_verdictless_tree`
never touches either. So a predicate that walks a detail again sees the copies of
`test_serial_run` and `test_fork_count` still reading a verdict, and the arm reds. The predicate
reads the verdict forms the three arms use, a subscript and `.get`, rather than any constant
`"verdict"`, so a name string cannot satisfy it.

What it does not check: a verdict bound to a local name outside any `check_arm` and then used only
in a message counts as read at the binding. A verdict read in an `if` above a `check_arm` counts
too, though the staged copy keeps it, so that arm's copy is not named blind and this arm reds. A
future A/B arm therefore reads its verdicts in a `check_arm` condition, as all three do today.

### The guard and its in-arm assertion (S4, S20, S23)

A directory entry is the one population form every reader of a guard honours: the runner's
`changed`, its reuse-key slicer, the spec-tokens join and govkit's taxonomy. A glob entry would
reach `changed` through git's pathspec, but the slicer and the join read a guard as an exact file or
a directory, so a glob would key the leg on staged blobs alone and never trip the join. The
directory also covers `kit.toml`, the runner and the fixtures, which the nine entries named one by
one, and `README.md`, which they did not.

`read_guard_misses` restates the runner's plain-guard rule rather than asking git. A pure path rule
can be asked about a `*.py` no file holds yet, which is L1's case, while `git ls-files` lists only
files that exist. It cannot import `check_guard_trips`, a repo-root tool absent from an adopter and
from this kit. An entry outside the plain class is reported, because there the rule and git
disagree. The manifest path is always in the population, so the arm reads the row it grades and the
row's guard covers the file the arm reads.

What it does not check: a file outside the kit dir that an arm comes to read later, unless that arm
calls `read_guard_misses` over it. Today those are `.githooks/pre-push` and the three
process-monitor modules, which the profiler reads and AC4 grades once.

### The orphan and its waiter (S18)

```bash
s=${1:-6}; m=${2:-}
printf 'early\n'
if [ -n "$m" ]; then ( sleep "$s"; printf 'late\n'; exec 1>&- 2>&-; : > "$m" ) &
else ( sleep "$s"; printf 'late\n' ) &
fi
exit 0
```

`hold` ends on the mark, not on a clock, so the run end follows `late` and follows the orphan's
last handle on the capture. The measurement above is why the subshell closes both streams before the
mark: a mark alone would order `late` and still race the subshell's exit against the delete. The
mark is forward-slashed, which both the MSYS bash and Python open. `waitmark.py`'s 30 s bound turns
a mark that never comes into a failed `hold`, and the arm's existing 60 s admission deadline still
bounds the run.

### What this unit corrects in each spec

A corrected paragraph carries `TOOL-dRedressedBar-25` and one sentence naming the change, and this
spec's §2 and §4 hold the design. Under `.claude/roles.json` only `gov-spec-writer` writes spec
files, and scratch-guard admits a builder's spec edit only to the status and date cells of the spec
its card routes (`tools/hooks/scratch-guard.js:91-99`). So these rows are `<w25>`, M6's "a review's
fixes folded in", dispatched once this spec is committed and before the build pass. Each target
keeps its CLOSED status. A build pass that finds no `<w25>` returns that to the main loop before
any write.

| Spec | Ids | What moves |
|---|---|---|
| 18 | 4, 11, 20, 23 | §4 "The selftest and its leg": the guard paragraph (`:662-668`) gains one sentence: the run-gates entries fold into `{prefix}/run-gates/`, and `{prefix}/gate-legs.json` joins the guard; §3 Edges gain the mirror; a revision line naming §4 |
| 21 | 4, 11, 20, 23 | S5: the arm also requires every `*.py` it walks to trip its own leg's guard, through `read_guard_misses`; S11: its two entries now sit under `{prefix}/run-gates/`; §5 security (`:480-481`): a `*.py` added later under the kit dir trips the leg, and what stays unchecked is a file outside the kit dir that an arm comes to read; AC12 (`:634-640`): the guard holds `{prefix}/run-gates/`, where it named the two files; §3 Edges gain the mirror; a revision line naming S5, S11, §5 and AC12 |
| 22 | 15, 18, 4, 11, 23 | S15, AC15 and the arm-table row (`:288`): a verdict read counts only outside a `check_arm` failure message, as a subscript or a `.get`, and the arm stages a verdictless copy of each A/B function; S9, AC9 and the arm-table row (`:290`): `orphan.sh 2 <mark>` then `waitmark.py <mark> 30`, and `hold` reads `ok`; S16, AC16 and the arm-table row (`:292`): `test_signal_docs` also requires its README path to trip its own leg's guard; §3 Edges gain the mirror; a revision line naming S9, S15, S16, AC9, AC15 and AC16 |

Spec 19's S21 states the three entries its own unit added, and its criterion reads them at that
unit's commit, so no sentence of it is false after this unit and it takes no correction.

The three mirror bullets, worded so each backticked token occurs in this spec:

- spec 18: `- **hands-off** \`TOOL-dRedressedBar-25\` — the \`measure-legs selftest\` guard, whose run-gates entries that unit folds into \`{prefix}/run-gates/\` beside \`{prefix}/gate-legs.json\` (round 2, ids 4, 11, 20 and 23).`
- spec 21: `- **hands-off** \`TOOL-dRedressedBar-25\` — \`test_write_atomic_temp\`, which that unit makes call \`read_guard_misses\` over every \`*.py\` it walks, and S11's two guard entries, which it folds into \`{prefix}/run-gates/\` (round 2, ids 20 and 23).`
- spec 22: `- **hands-off** \`TOOL-dRedressedBar-25\` — \`test_ab_arms_read_verdicts\`, which that unit makes count a verdict read only outside a \`check_arm\` failure message (round 2, H1), \`test_legs_table\`, whose \`hold\` waits on the mark \`orphan.sh\` writes (L6), and \`test_signal_docs\`, which calls \`read_guard_misses\` (M1).`

Until `<w25>` lands, an unstaged `memory hygiene` run reds check 12's reciprocity join on §3's
three `consumes-from` edges, because specs 18, 21 and 22 name no `hands-off` back. The staged run
holds the joins (`memory/TEMPLATE-SPEC.md`, "§3 Edges").

### Order, and the symbol index

Order 19 is one above unit 24's. Unit 26 orders after this unit: both may re-stamp
`memory/guides/SESSION-KICKOFF.md` and regenerate `memory/map/generated/symbols.json`, so M6
sequences them. This unit mints functions in `measure_legs.py`, so the build pass runs
`python tools/codebase-map/gen_map.py --write` alone before its product commit, as unit 22's did.
`tools/gate-legs.json` is on the kickoff manifest's `watch:` line
(`memory/guides/SESSION-KICKOFF.md:6`), so S4's two re-stamps are owed.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `check_verdict_read` | function | `py.function`, `check` |
| `read_blind_ab_arms`, `read_guard_misses` | functions | `py.function`, `read` |
| `derive_verdictless_tree`, `derive_kit_rel` | functions | `py.function`, `derive` |
| `waitmark.py` | fixture | none |
| `WAITMARK_PY` | module constant | none; `py.constant` is no declared cell |

Each function name answered OK under `python tools/lexicon/lexicon.py --suggest <name> --as py.function` on
2026-10-15. `git grep` over `tools/` and `skills/` found none of them at `bc6a4c9f`.
`derive_kit_paths` was also proposed and set aside: `tools/lib/render-doc.sh:70` already defines a
bash function of that name with another meaning.

### Files touched (estimate)

- `tools/run-gates/measure_legs.py`
- `tools/run-gates/fixtures/measure-legs/`
- `tools/run-gates/kit.toml`
- `tools/gate-legs.json`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/map/generated/`
- `memory/builds/dRedressedBar/build/`

The fixture directory gains `waitmark.py` and changes `orphan.sh`. Specs 18, 21 and 22 are
`<w25>`'s write set, not the build pass's.

### Alternatives rejected

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| H1 by the finder's fix | the skeptic: UNSOUND; the record's corrected fix is the one to spec | Rejected; S15 |
| H1's mutation as "every verdict read outside a detail becomes `"ok"`" | it would decide what to cut through the predicate's own skip, so a predicate that walked details again would cut them too and still name the copies blind, the guard sharing state with what it guards | Rejected; `derive_verdictless_tree` cuts conditions only |
| H1's staged copies as the record's two text edits alone | a third A/B arm, `test_resolution_disabled`, and any later one would carry no red half | Rejected; every found function is staged, and the two the record names are required |
| L1 by a `*.py` glob entry | the reuse-key slicer and the spec-tokens join read a guard as a file or a directory, so the leg's key would miss an uncommitted edit (§4) | Rejected |
| L1 by the arm asserting each walked `*.py` is named, the guard kept as a list | a new `*.py` outside the list skips the leg, so the assertion that would red never runs on the commit that adds it | Rejected as the fix; kept as S23's left-shift over the directory |
| The directory plus an exact `{prefix}/run-gates/measure_legs.py` entry, so the spec-tokens join still owes this leg for its own file | a second spelling of a path the directory covers, whose one reader, the join, declines a broad guard by design; `profile-bar selftest` stands the same way | Rejected; §5 risks |
| `read_guard_misses` through `git ls-files -- <guard>` | it lists only files that exist, so L1's case, a `*.py` not yet written, cannot be asked | Rejected |
| L6 by a third argument to `spawn.py` | `test_launch_failure` already passes an inert marker there (`:2771`) | Rejected; a fixture of its own |
| L6's mark written right after `late`, the streams left open | the probe in §4: the capture stays held until the subshell exits, so the delete still races it | Rejected; S18 closes both streams first |
| The corrections to specs 18, 21 and 22 in the build pass's commit | scratch-guard refuses a builder's edit to another spec | Refused by the hook |

## 5. Production-readiness checklist

- security — N/A — no new write path, process kill or network call. The mark is created under the
  arm's own temp dir, and `read_guard_misses` reads one tracked manifest.
- perf / scale — `test_legs_table`'s `hold` ends about 2 s into the leg rather than at 5 s.
  `test_ab_arms_read_verdicts` parses this file once per found function, three today, each under a
  second. `read_guard_misses` reads the manifest twice per selftest. The leg runs on an edit to any
  file under `tools/run-gates/` or to `tools/gate-legs.json` when the self-tests are asked for, where
  it ran on its thirteen named entries. Those are ESTIMATES, not measured.
- error / empty / loading states — `read_guard_misses` answers a missing row, an unreadable
  manifest, an empty guard and a non-plain entry each with a named miss, never an empty list.
  `waitmark.py` exits 1 at its bound, so a mark that never comes is a failed `hold`.
- observability — Each new assertion prints its misses or its staged counts in its failure detail.
- risks — The spec-tokens join no longer owes `measure-legs selftest` for a path under
  `tools/run-gates/`, since the directory is broad; it still owes it for `tools/gate-legs.json`.
  S18 rests on MSYS bash closing the Windows handle when it closes a descriptor, measured once on
  node d (§4). Unit 26's edits to `run-gates.sh` now select this leg on a scoped self-test bar.
- testing — AC4 to AC24 are in-process programs over the tool's functions and arms, temp manifests
  and copies of the leg manifest, and `git` reads over specs. The moved arms are declared in §7.
- migration — N/A — no record field, flag or conf key moves, and a run dir from before reads as it did.
- user docs — N/A — the change is to the selftest's arms, a fixture and a guard, and no page under
  `help/` describes any of them (§3).

## 6. Acceptance criteria

The numbering follows report ids, so the criterion that observes S4 also observes S11. `<p25>` is
this unit's product commit, `<p25m>` its manifest re-stamp and `<w25>` its spec-writer commit,
each named in its ledger. A break said to be "as at `<p25>~1`" is the code the build pass starts
from. `<ml>` is `tools/run-gates/measure_legs.py`, imported as `measure_legs`; `<fx>` is its
fixture dir; `<o>` is a fresh dir under `%TEMP%`; `<sf>` is the selftest's flags
`--census-every 1 --stall-window 8 --stall-cpu 0.5`; `<old>` is a temp file holding
`git show <p25>~1:tools/gate-legs.json`. "Joined" means piped through `tr '\n' ' ' | tr -s ' '`.
Every command runs from the worktree root on node d.

- **AC15** — A python program reads `<ml>`'s source. `measure_legs.read_blind_ab_arms` over its
  parse returns a found list holding `test_serial_run`, `test_fork_count` and
  `test_resolution_disabled`, and an empty blind list. For each of the three,
  `measure_legs.derive_verdictless_tree(source, name)` returns a count of at least 1 and a tree over
  which `read_blind_ab_arms` names that function blind. `inspect.getsource` of
  `test_ab_arms_read_verdicts` carries `derive_verdictless_tree(`.
  Red when: the rule as at `<p25>~1`, `verdict` among every constant value and attribute name the
  function holds, is applied to the copies of `test_serial_run` and `test_fork_count`. It names
  neither blind, because each failure message still reads the verdict, which is the defect the
  record describes. And with `read_blind_ab_arms` walking every `check_arm` argument, the arm's
  staged half names those two functions as copies still reading a verdict.
- **AC4** — A python program loads `tools/gate-legs.json`. The `measure-legs selftest` row's
  `guard` equals S4's six entries in order. With `check_guard_trips` from
  `tools/check-spec-tokens.py` and `{prefix}` read as `tools`, each of these trips an entry:
  `tools/run-gates/README.md`, `tools/run-gates/kit.toml`, `tools/run-gates/run-gates.sh`, every
  path `git ls-files` lists under `tools/run-gates/`, `.githooks/pre-push`,
  `tools/process-monitor/census.py`, `tools/process-monitor/reap.py`,
  `tools/process-monitor/scope.py` and `tools/gate-legs.json`. The `last-audit:` line of
  `memory/guides/SESSION-KICKOFF.md` names a commit whose `tools/gate-legs.json` holds
  `{prefix}/run-gates/` in that row, and `git log -1 --format=%B <p25m>` carries `manifest-audit:`.
  Red when: over `<old>`, `tools/run-gates/README.md` and `tools/gate-legs.json` trip no entry, the
  record's probe.
- **AC20** — The same program joins `new_writer.py` under `tools/run-gates/`, a path no file holds.
  It trips `{prefix}/run-gates/` in the live row, and `measure_legs.read_guard_misses` over it
  returns an empty list.
  Red when: over `<old>`, it trips no entry, and `read_guard_misses` with `legs_path` set to
  `<old>` returns it.
- **AC23** — A python program imports `measure_legs`. `read_guard_misses` over the README path
  `test_signal_docs` opens returns an empty list. With `legs_path` set to `<old>` it returns that
  path. Over a copy of the live manifest whose row also carries a guard entry holding `*`, it
  returns that entry. Over a copy holding no row whose argv runs `measure_legs.py --selftest`, it
  returns one string. `inspect.getsource` of `test_signal_docs` and of `test_write_atomic_temp` each
  carry `read_guard_misses(`, and that of `run_profile` carries `derive_kit_rel(`. With
  `read_guard_misses` rebound to a partial whose `legs_path` is `<old>`, `test_signal_docs` adds
  one name to `measure_legs.ARM_FAILED`.
  Red when: as at `<p25>~1`, `test_signal_docs` and `test_write_atomic_temp` read no guard, so a
  README-only commit skips the one arm that grades the README.
- **AC18** — A python program runs `measure_legs.main` with `--serial --legs <m> --out <o>` and
  `<sf>`, where `<m>` is a temp manifest of two legs from `<fx>`: `orphan.sh 7 <mark>` under
  `bash`, named `orphan`, and `waitmark.py <mark> 30` under `python3`, named `hold`, the orphan's
  sleep set past the old fixed 5 s. `orphan`'s `<i>.log` carries `late`, its `<i>.json` reads
  `log_bytes` 11, `raw_kept` is empty and `hold` reads verdict `ok`.
  `inspect.getsource(measure_legs.test_legs_table)` carries `WAITMARK_PY`, and that constant ends
  in `waitmark.py`. The `project-owned` list in `tools/run-gates/kit.toml` names `waitmark.py` under
  the fixture dir, and `test_fixtures_withheld`'s set compare holds.
  Red when: the manifest as at `<p25>~1` runs with the orphan's sleep at 7 s, `orphan.sh 7` then
  `spawn.py 0 5`. The orphan then reads `log_bytes` 6 and `raw_kept` names it, the order two fixed
  sleeps set, which a loaded node reaches with the 2 s sleep.
  figure: 6 and 11 are the fixture's bytes, `early` and `late` each with an LF, DERIVED. 7 s is a
  chosen margin past `hold`'s 5 s.
  cost: about 25 s over the two runs.
- **AC24** — `git diff <w25>~1 <w25> -- memory/builds/dRedressedBar/spec/` shows specs 18, 21 and
  22, each with one header rev change and one new revision line naming `TOOL-dRedressedBar-25` and
  every report id §4's table assigns that spec. Each carries a CLOSED header at `<w25>~1` and a §3
  bullet `hands-off` `TOOL-dRedressedBar-25` at `<w25>`. Spec 18's "The selftest and its leg"
  section, cut and joined, carries `{prefix}/run-gates/`. Spec 21's AC12 bullet, cut from
  `- **AC12**` to the next `## `, carries `{prefix}/run-gates/`. Spec 22's AC15 bullet carries
  `check_arm` and its AC9 bullet carries `waitmark.py`.
  `git diff --name-only <p25>~1 <p25> -- memory/builds/dRedressedBar/spec/` names no file but this
  spec. The ledger S24 names exists and carries `**Serves:** journal TOOL-dRedressedBar-25`.
  Red when: a target takes no bump or two, a revision line misses one of its ids, or a build-pass
  commit writes another spec.

## 7. Gates

`measure-legs selftest` · `foreign-prefix parity (every self-test at three prefixes)` · `run-gates canary` · `run-gates gov canary` · `govkit selfcheck` · `kickoff-manifest ratchet` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `install-prefix (shipped surface)` · `python resolver (behaviour + inline parity + idiom ban)` · `shell hygiene (a fixed-name temp renamed into place)` · `shell hygiene (a fork spent on builtin work)` · `codebase-map coverage + freshness` · `codebase-map gate coverage` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `memory hygiene`

The line is a floor. Joined against the guards in `tools/gate-legs.json` with `BROAD_LEG_FLOOR`
applied, §4 Files touched owes `measure-legs selftest`, `run-gates canary`, `run-gates gov canary`,
`recall floor` and `recall floor arms`; the rest are legs the change moves: the guard's taxonomy,
the watched manifest, the kit's shipped bytes and descriptor, a fixture script, the symbol index,
new text IO and this spec.

New arm: tools/run-gates/measure_legs.py --selftest · covers AC15 · test_ab_arms_read_verdicts with read_blind_ab_arms walking every check_arm argument, detail included, so the staged copies of test_serial_run and test_fork_count still read a verdict · none
New arm: tools/run-gates/measure_legs.py --selftest · covers AC4 AC23 · test_signal_docs with the measure-legs selftest row's guard restored to its entries as at <p25>~1, so the README path is a miss · none
New arm: tools/run-gates/measure_legs.py --selftest · covers AC20 · test_write_atomic_temp under that restored guard with an untracked new_writer.py, holding no rename, beside measure_legs.py · none
New arm: tools/run-gates/measure_legs.py --selftest · covers AC18 · test_legs_table with orphan.sh creating its mark before its sleep, so hold ends at once and the run ends before late lands · none

The main loop observes each moved arm red on its staged break, then green, at the close, and runs
the bar once after the last unit is terminal.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-15 · initial draft, promoted from the round-2 closing diff review's profiler
  findings by the owner's ruling of 2026-10-15. Report ids 4, 11, 15, 18, 20 and 23 are batched by
  M4. Every citation was re-read at `bc6a4c9f`, whose `tools/` equals the reviewed tip's. Id 15
  takes the skeptic's corrected fix. The guard gains `{prefix}/gate-legs.json`, which the record
  does not name, because S23's arms read that row. The capture-handle release S18 rests on was
  measured on node d.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "check that every file a selftest arm reads is covered
by its own gate leg's guard pathspec"` ranked name stems only (`read`, `check`, `arm`, `legs`), and
no guard-coverage seam. `python tools/codebase-map/reuse_lookup.py "an ast walk that stages a
mutated copy of a test function and asserts the static predicate names it"` ranked `walk`,
`mutate` and `write_staged`, none an `ast` staging. `python tools/codebase-map/reuse_lookup.py "a
fixture process that waits with a bounded poll for a marker file another process writes"` ranked
`write`, `fixture` and `build_fixture`, none a waiter. All three are recorded as misses, and no
existing seam outside the file fits. The seams extended are these. `test_ab_arms_read_verdicts`'s
subtraction rule (`tools/run-gates/measure_legs.py:3499-3502`) moves unchanged into
`read_blind_ab_arms`. The source-as-argument shape of govkit's `read_bar_writes21`
(`tools/govkit/selftest.py:16549-16563`) is how `derive_verdictless_tree` stages a copy.
`held_halves.load_manifest` (`tools/run-gates/held_halves.py:80-94`), `resolve_prefix_token`
(`:104-113`) and `run_profile`'s manifest default (`:1689`) are how `read_guard_misses` finds the row, and
`run_profile`'s kit-path lines (`:1697-1699`) become `derive_kit_rel` for both callers. The runner's
plain-guard rule (`tools/run-gates/run-gates.sh:3236-3238`, `:3258-3260`, `:3285`) is the rule
`read_guard_misses` restates, with §4 saying why it is not imported. `read_hold_beacon`'s bounded
poll (`:2091-2109`) is `waitmark.py`'s shape, and `orphan.sh`'s background subshell is extended in
place. `profile-bar selftest`'s guard is the precedent for a directory guard on this kit.

The gotchas checklist for `tools/run-gates/measure_legs.py`, `orphan.sh`, `tools/gate-legs.json`
and `tools/run-gates/kit.toml` selected these classes, each answered here:
- `fixture-passes-by-finding-nothing`: S15's staged copies, S23's named misses and S18's `hold`
  verdict each give an arm a case that must red.
- `staged-break-substitutes-a-synthetic-value`: S15 stages the arms' real source, not a synthetic
  function.
- `held-suite-guard-misses-a-sibling-kit`: its fix prefers exact files for a SIBLING kit. The three
  process-monitor files stay exact, and the directory is this kit's own.
- `two-answers-to-one-question`: `derive_kit_rel` gives `run_profile` and the guard check one tool root.
- `a-spelling-change-strands-its-readers`: every reader of the guard was read (§4 Evidence), and
  each honours a directory entry.

The recall probe returned the round-2 record, spec 22's S15, and TOOL-aPacedTurnstile-9, the open
ask for a guard-completeness proof, which §3 leaves to it. The precedent aSweptBar-7, a closing
review's minors batched into one unit, corrected a CLOSED spec in a spec pass and left the
class-level checklist lines to the close, and this unit takes that shape. The record and the code
agree on every citation re-read.

Recall terms used: `python tools/memory-recall/query.py "does a static gate that grades an A/B
arm's verdict read still pass when the read sits only in the failure message, and should a selftest
leg's guard cover the directory its arm walks" --terms "test_ab_arms_read_verdicts check_arm verdict
detail ab-arm-never-did-the-work measure-legs selftest guard gate-legs.json check_guard_trips
BROAD_LEG_FLOOR orphan.sh fixed-sleep-does-not-place-a-signal"`
