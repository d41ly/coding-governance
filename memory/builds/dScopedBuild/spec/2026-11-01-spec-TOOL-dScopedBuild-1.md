# TOOL-dScopedBuild-1 — one exit contract with a history-derived base

**Status:** DEFERRED · rev-3 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 1 · advances TOOL-dScopedBuild-16

**Carries:** cl-dClosedLoop-0399@182b9f2d whole
**Carries:** node:item.build.base
**Carries:** node:item.build.exit

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-build-TOOL-dScopedBuild-1-reuse-scout-a.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-reuse-scout-a.md) | research | TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md) | research | TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-1-reuse-scout.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-1-reuse-scout.md) | journal | — |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-2-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-2-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-fix-brief.md) | research | TOOL-dScopedBuild-3 TOOL-dScopedBuild-6 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-owner-stop-chain.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-owner-stop-chain.md) | research | — |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md) | research | TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 |

<!-- /gen:spec-records -->

## 1. Goal

An attended build ends on a bare bar and an unattended one on `--close`'s DoD, so the two modes run
different exit contracts (gap-spine-03), and the attended one has no base, no attribution and no
refusal. This unit gives both modes one exit contract, `check_build_exit`, with its base derived from
history, the parent of the build's oldest first pass, deciding WHICH commits are the build's, and the
bar's attribution base R deciding WHOSE red it is; the exit is refused while a red the build's own
commits introduced stands.

## 2. Scope (IN)

- **S1** — `read_first_passes` and `read_commit_times` live in `tools/memory-tree/routed_commits.py`
  beside `read_routed_commits`, their bodies as `deviation_join.py:307-340` holds them at base, the
  one routed-path test inside them `test_routed_path` (`routed_commits.py:181`). `deviation_join.py`
  calls `routed_commits.read_first_passes` and `routed_commits.read_commit_times` at its two call sites
  (`:521`, `:578`) and defines neither; its population is unchanged. Observed by AC1.
- **S2** — `read_build_base(repo, slug)` in `routed_commits.py` returns `(sha or None, why)`: the
  roster units are the ids an H1 defines in a spec under `<MEMORY_ROOT>/builds/<slug>/spec/`, read by
  `load_spec_paths` (`:189`) and filtered to that prefix; the commits are one `read_routed_commits`
  pass over `HEAD`; the entries are `check_conf`'s `ROUTED_PATHS`; the first passes are S1's. The base
  is the first parent of the oldest first pass by committer date, a tie going to the commit the log
  lists last. The CLI `python routed_commits.py --build-base <slug>` prints the 40-hex base and exits
  0; prints `routed-commits: build-base none — <why>` and exits 1 when no roster unit has a first
  pass; and exits 2 `REFUSED` on a slug no spec of which defines an id, on an oldest first pass that
  is a root commit, and on every refusal the leg already raises (a shallow clone, an unarmed conf).
  Observed by AC2, AC3, AC9.
- **S3** — `read_gates_record` (`tools/unattended/unattended.sh:9617`) also sets `GR_OWN`, the
  comma-joined red legs whose attribution verdict is not `INHERITED`, in the loop that already reads
  each row (`:9635-9641`); `GR_STATE`, `GR_LEGS`, `GR_AGED`, `GR_WHY` and its decision table are
  unchanged. Observed by AC4.
- **S4** — `check_build_exit <slug> <R> <bar rc> <run dir>` in `unattended.sh`, the one exit
  contract, a function over its four arguments and the tree, sliceable as `plan_state` is, that
  writes no run-state file. Every exit arm of this build runs inside it and never in a verb body, so
  `--build-exit` and `--close` run one set: the deviation gate and `build.scope` through one
  `routed_commits.py --build <slug>` call (TOOL-dScopedBuild-14 S5, TOOL-dScopedBuild-3 S7, the touch
  join of TOOL-dScopedBuild-9 inside the scope arm), the closing-review predicate and the ratification
  (TOOL-dScopedBuild-4 S1, S8) and the core arm (TOOL-dScopedBuild-7 S2). Its only writes are those
  arms': the scope record and the map's grace file that `--build <slug> --write` writes, and the ask
  rows `write_gate_asks` stages (TOOL-dScopedBuild-14 S6); this unit's own body writes nothing. It
  derives the base by S2's CLI into `BX_BASE`, with `BX_BASE_FROM=history`; on exit 1 it sets
  `BX_BASE` to R and `BX_BASE_FROM=tip` and says so; on exit 2 it refuses. It reads the red by the
  table in §4 "The exit table", through `read_gates_record` alone. It prints `build-exit:` lines and
  returns 0 to pass or 1 to refuse. Observed by AC4, AC7.
- **S5** — The attended half, a slug verb `--build-exit <slug>` run by `run_build_exit`: it observes
  R through `observe_anchor` (`:1974`, which sets `ASHA` at `:2066`), pins a run id as the
  `gates-green` arm does (`:11174-11181`), runs `$GATE_CMD` once with `GATE_RUN_ID` and
  `GATE_ATTRIBUTE=<R>`, and calls S4 over that bar's record under the git dir's `gate-run/<id>`. It
  needs no run-state file and writes none; its only writes are S4's arms'. Exit 0 passed, 1 refused, 2 not graded: no `GATE_CMD`, an
  anchor `observe_anchor` refused, or S2's refusal. It joins `VERBS_SLUG` (`:112`), the usage header
  (`:5-35`) and the dispatch (`:14563`). Observed by AC5, AC7.
- **S6** — The unattended half: `--close`'s `build-complete` arm (`:11625`) gains a term calling
  `check_build_exit "$slug" "$ASHA" "$GG_BAR_RC" "$GG_BAR_DIR"`, two globals the `gates-green` arm
  sets beside `GG_RUN_FACT` (`:11324`, `:11386`) and `verb_close` clears where it clears that one
  (`:10768`). A `covered` close (`:11310`) sets the rc 0 and no dir. Where neither global is set, the
  term reads the run id the `gates-run` fact names. A refusal is `build-complete` UNMET with the exit's
  lines, through `verb_close`'s fail 13. The `gates-green` arm's own table is unchanged. Observed by
  AC6.
- **S7** — The attended `/build` Skill: `tools/roles/SKILL.template.md` Stage 7 runs
  `unattended.sh --build-exit <slug>` once after the last unit is terminal, in place of the bare bar
  at `:82-85`; the "Before stage 3" bullet at `:19-20` names `--build-exit` beside `--plan --paths` as
  the driver verbs an attended run uses; the `gate-bar` row of `tools/roles/workflows.toml` (`:72-78`)
  names the verb as its `harness`. The render `.claude/skills/build/SKILL.md` is `adopt-roles.sh`'s
  copy (`tools/roles/adopt-roles.sh:127-129`). Observed by AC8.
- **S8** — The docs: the `--build-exit` entry of `tools/unattended/VERBS.template.md`, copied to
  `memory/guides/UNATTENDED-VERBS.md`; the attended-build bullet of `help/roles.md` (`:30-31`) saying
  the last stage is the exit contract `--close` runs too; the usage lines of `routed_commits.py`'s
  docstring (`:7-11`) naming `--build-base`. Observed by AC8.

## 3. Non-goals (OUT)

- The core set. Until TOOL-dScopedBuild-7 narrows the graded legs to I18's core rows, every leg is
  graded (§8 F1); this unit invents no `core` tag or chunk.
- The closing-review predicate inside the exit, TOOL-dScopedBuild-4's I13, and the deviation gate's
  and `build.scope`'s reads at the exit, TOOL-dScopedBuild-14's and TOOL-dScopedBuild-3's. Each adds
  its arm into `check_build_exit`; this unit builds the function and its base.
- Telling a red introduced by an unlanded commit that is an ancestor of the base apart from one the
  build's passes introduced: both read OWN at R and are refused, as `gates-green` refuses both today.
- The `gates-green` arm's decision table, `INHERITED_RED` and the item map of TOOL-dDeclaredLoop-11,
  which ties `gates-green` to `item.test.verdict` and `build-complete` to `item.build.exit`: S6 puts
  the contract in the second and leaves the first as it is.
- A file-backed transition record for `build.exit`: the executor's (TOOL-dWellOiledMachine-6). Here
  the transition's evidence is the exit's `PASS` line and, under a mandate, `--close`'s records commit.
- The landing, the lander and `push-main.sh`.

### Edges

- **consumes-from** external — `observe_anchor`, `read_gates_record`, the bar's nine-column
  `attribution` row (`tools/run-gates/run-gates.sh:4341-4344`) and `GATE_ATTRIBUTE`, all landed; the
  exit reads no parent surface
- **hands-off** `TOOL-dScopedBuild-14` — `--build-exit` and `check_build_exit`, the exit host its
  deviation-gate arm and `write_gate_asks` call join, reading `BX_BASE`
- **hands-off** `TOOL-dScopedBuild-3` — `read_first_passes`, and `read_build_base` for "the unit's own
  commits" within the base (I8); and `check_build_exit` behind `--build-exit`, inside which its scope
  arm runs through `routed_commits.py --build <slug>` and its `--write` flag
- **hands-off** `TOOL-dScopedBuild-4` — `--build-exit` and `check_build_exit`, inside which its
  closing-review predicate runs for attended builds as for unattended ones
- **hands-off** `TOOL-dScopedBuild-7` — `read_first_passes` for the build's range and `--build-exit`,
  whose graded legs it narrows to the core set
- **hands-off** `TOOL-dScopedBuild-15` — `read_first_passes`, the base an attended build's acceptance
  passes as `--base`, since it has no `RUN.md`
- **hands-off** `TOOL-dScopedBuild-32` — S5's `run_build_exit` bar call, which that unit runs through `run_gate_bar` with `gates-green`'s knob scrub (id 22)
- **hands-off** `TOOL-dScopedBuild-33` — S1's move of `read_first_passes` and `read_commit_times`, which that unit supersedes: the readers stay in `deviation_join.py` and `read_build_base` imports them lazily (id 30)
- **hands-off** `TOOL-dScopedBuild-35` — S4's exit body, split by that unit's S1; AC5's and AC7's fixture, S2; S5's verb in the unattended Skill, S12; S6's fallback, S21; and S2's base by ancestry, S22 (ids 4, 5, 27, 39, 40)
- **hands-off** `TOOL-dScopedBuild-39` — S1's move of `read_first_passes`, `read_commit_times` and `derive_pass_units`, which this unit's builder does not make, building TOOL-dScopedBuild-33 S1 and S2's form instead, as that unit's S8 rules (id 5)

## 4. Design

### Evidence

Read at `5f0b11f12`; no product file differs from base `f4597719`.

- `read_first_passes(commits, units, entries, when)` is at `deviation_join.py:325-340` and
  `read_commit_times` at `:307-309`; `git grep` finds no caller of either outside that file.
- `read_gates_record` (`unattended.sh:9617-9651`) reads `verdict`, `tree_moved`, `failed` and
  `wall_breach` from the record's `verdict` file and one row per red leg from `attribution`; a GREEN
  verdict reads `none` (`:9632-9634`). `gates-green` acts on it at `:11378-11407` and refuses any
  state but `land`.
- The bar's attribution base R "IS THE LANDING BASE, never the branch point" (`run-gates.sh:4349`);
  `gates-green` passes `GATE_ATTRIBUTE=$ASHA` (`unattended.sh:11181`).
- The attended Skill's Stage 7 runs `bash {{TOOL_ROOT}}run-gates/run-gates.sh` with no attribution
  (`SKILL.template.md:82-85`), and the Skill says the one driver verb an attended run uses is
  `--plan <slug> --paths` (`:19-20`).
- `pass_commit` (`lib-unattended.sh:1026`) needs an anchor argument, so it reads a pass inside a
  known window and cannot derive the window itself.
- One `git log -z --root --no-renames --name-only HEAD` pass over this tree's 7300 commits took
  0.9 s, PINNED at `5f0b11f12`.

### The two bases

The base B is history's: the parent of the oldest commit `read_first_passes` attributes to a roster
unit. It answers WHICH commits are the build's, and `BX_BASE` hands it to every arm of the exit that
reads a range (TOOL-dScopedBuild-3, -4, -7, -14) and to an attended build's `--base` (-15). R is the
advertised tip `observe_anchor` saw, the base the bar's attribution re-runs a red leg at. It answers
WHOSE red it is. The exit never uses one base for both questions, because a branch point read as an
attribution base buys a "not mine" no tip measured (`run-gates.sh:4349-4353`). A build with no first
pass yet, a spec run's, takes R as its base, announced.

### The exit table

`check_build_exit` grades the first matching row:

| Bar rc | Record | Verdict | Line |
|---|---|---|---|
| any | S2 exits 2 | refuse | `build-exit: refused — the base cannot be derived: <why>` |
| 0 | not read | pass | `build-exit: PASS <slug> at <HEAD8> · base <B8> (<from>) · no red` |
| 1 | `GR_STATE` `land` | pass | `build-exit: PASS … · <legs> red, every one INHERITED at <R8>` |
| 1 | `GR_STATE` `other` | refuse | `build-exit: refused — <GR_OWN> red at <HEAD8>, introduced since <R8>` |
| 1 | `GR_STATE` `moved` or `none` | refuse | `build-exit: refused — <GR_WHY>` |
| any other | not read | refuse | `build-exit: refused — the bar ended <rc>, so no red was read` |

`read_gates_record` is called with the policy `land`, because the exit asks whose red it is and
never whether a run may land over an inherited one; that policy stays `gates-green`'s. Every leg is
graded and the function prints `build-exit: core set not-installed — no manifest row carries
enforces, so every leg is graded` until TOOL-dScopedBuild-7 narrows it.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_build_base` | python function, `routed_commits.py` | `py.function`, OK |
| `--build-base` | mode of `routed_commits.py` | none |
| `check_build_exit` | shell function, `unattended.sh` | `sh.function`, OK |
| `run_build_exit` | shell function, `unattended.sh` | `sh.function`, OK |
| `--build-exit` | driver slug verb | none |
| `GR_OWN`, `GG_BAR_RC`, `GG_BAR_DIR`, `BX_BASE`, `BX_BASE_FROM` | shell globals | none |

### Rollout

Live at landing. Under a mandate the change is one more `build-complete` term over the bar
`gates-green` already ran, so a close that is MET today stays MET: `gates-green` already refuses every
state the exit refuses. An attended build's last stage runs one bar, as it does today, now attributed.

### Files touched (estimate)

- `tools/memory-tree/routed_commits.py`: S1, S2, the docstring, its selftest arms
- `tools/memory-tree/deviation_join.py`: S1's two call sites
- `tools/unattended/unattended.sh`: S3 to S6
- `tools/unattended/unattended.test.sh`: the arms of §7
- `tools/roles/SKILL.template.md` and its render `.claude/skills/build/SKILL.md`: S7
- `tools/roles/workflows.toml`: S7
- `tools/unattended/VERBS.template.md` and its copy `memory/guides/UNATTENDED-VERBS.md`: S8
- `help/roles.md`: S8

### Alternatives rejected

- **A new DoD item for the exit.** Rejected by §8 F2: a `DOD_CORE` member is a new `--override`
  name and a new row in every reader of the item list, for a contract `build-complete` already maps.
- **The contract inside the `gates-green` arm.** Rejected by §8 F2: that arm is `item.test.verdict`'s
  (TOOL-dDeclaredLoop-11), and it already refuses every red the exit refuses.
- **`pass_commit` as the base reader.** Rejected by the Evidence: it takes the anchor as an
  argument, which is the value being derived.
- **The base from `RUN.md`'s pinned `base:` fact.** Rejected by gap-spine-03 itself: an attended build
  has no run-state file, which is the defect the clause names.

## 5. Production-readiness checklist

- security — the exit denies by default: an underivable base, an unread record, a moved tree and an
  unknown bar ending each refuse; R is the remote's advertised tip, never a local ref.
- perf / scale — one log pass for the base (0.9 s PINNED, §4) and one bar, the bar the attended stage
  ran before this unit.
- error / empty / loading states — a build with no first pass takes R, announced; a GREEN bar passes
  without reading attribution.
- observability — every verdict is one `build-exit:` line naming the base, its source, R and the legs.
- risks — an unlanded ancestor's red refuses the build's exit (§3); the attended exit needs the
  network `observe_anchor` needs, and exits 2 without it.
- testing — the arms of §7, over sliced functions and the driver suite's fixtures.
- migration — none; no record or conf key moves.
- user docs — `help/roles.md` and `memory/guides/UNATTENDED-VERBS.md` through its template.

## 6. Acceptance criteria

- **AC1** — When `grep -c "^def read_first_passes" tools/memory-tree/deviation_join.py` runs it prints
  0, the same over `tools/memory-tree/routed_commits.py` prints 1, and `python
  tools/memory-tree/deviation_join.py --fixture --plant pass-revision --policy refuse` exits 1 naming
  the revision member as it did at base.
  Red when: the function is defined in both files, or the moved reader changes the population.
- **AC2** — When `python routed_commits.py --build-base tFix` runs in a scratch repository whose
  history is a spec commit for `TOOL-tFix-1` touching no routed path, then `TOOL-tFix-1: code` writing
  a routed path, then a commit with trailer `Pass: TOOL-tFix-2` writing another, it prints the spec
  commit's sha and exits 0.
  Red when: it prints the first pass itself, or a commit that names the unit and writes no routed path.
  fixture: built by `routed_commits.build_fixture`; none exists in the tree.
- **AC3** — When the same `--build-base tFix` runs over a history holding only the spec commit, it
  prints `build-base none` and exits 1; `--build-base tNone` exits 2 printing `REFUSED`.
  Red when: an unpassed build prints a base, or an unknown slug exits 0 or 1.
- **AC4** — When `check_build_exit` and `read_gates_record` are sliced from `unattended.sh` and run
  over a planted run dir whose `verdict` reads RED with `failed 1` and whose `attribution` row reads
  leg `x` `OWN`, it returns 1 printing `build-exit: refused` naming `x`, and `GR_OWN` reads `x`; with
  the row `INHERITED` it returns 0 naming `x` INHERITED; with bar rc 0 it returns 0.
  Red when: the planted own red passes, or the planted inherited red is refused.
  fixture: the suite's nine-column record writer (`unattended.test.sh:13862-13894`).
- **AC5** — When `bash unattended.sh --build-exit tExit` runs in the driver suite's fixture repository
  with its bare remote and no run-state file, its `GATE_CMD` a stub that records the
  `GATE_ATTRIBUTE` it received and writes a RED record whose row reads `x OWN`, it exits 1 naming `x`,
  the stub's recorded value equals the remote's advertised tip, and no `RUN.md` exists after it; with
  the row `x INHERITED` it exits 0.
  Red when: the attended exit passes a planted own red, or attributes against a local ref.
  fixture: the driver suite's slug fixture; the stub is the suite's own.
- **AC6** — When `--close tExit` runs over a preflighted fixture run whose stub bar writes the
  `x OWN` record, its `build-complete` line is UNMET naming `build-exit` and `x`; with every row
  `INHERITED` under `INHERITED_RED=land`, `gates-green` is MET and `build-complete`'s exit term passes.
  Red when: `--close` meets `build-complete` over the planted own red.
  fixture: as AC5, preflighted.
- **AC7** — When `--build-exit tExit` runs over a fixture whose roster has no first pass, it prints
  `base` with `(tip)` and the advertised tip's short sha, and still refuses the planted `x OWN` row.
  Red when: a build with no pass reads no red, or prints a base S2 did not derive.
- **AC8** — When `grep -n "build-exit" tools/roles/SKILL.template.md .claude/skills/build/SKILL.md
  tools/roles/workflows.toml tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md
  help/roles.md` runs, it prints Stage 7's line in both Skill files, the `gate-bar` row's harness, the
  verb's entry in the template and its copy with the same bytes, and the help bullet.
  Red when: the Skill's Stage 7 still runs a bare bar, or the guide and its template differ.
- **AC9** — When `python tools/memory-tree/routed_commits.py --build-base dScopedBuild` runs on this
  tree after this unit's pass commit, it prints the sha of that commit's first parent and exits 0.
  Red when: it prints another commit, or exits 1 with the pass in history.
  figure: DERIVED at the pass commit; at base `f4597719` the same command exits 1.

## 7. Gates

`unattended kit gate` · `routed commits name a specced unit` · `routed-commits selftest` · `memory hygiene` · `policy fixtures` · `roles render wiring` · `roles render selftest` · `roles catalogue` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `kit version markers` · `harness arms (fail branches armed or pinned)` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC2 AC3 · the selftest's scratch histories for a passed, an unpassed and an unknown build, its failing case a first pass printed as the base · none

New arm: tools/unattended/unattended.test.sh · covers AC4 AC5 AC6 AC7 · the sliced exit over planted records and the attended and closing runs over the stub bar, its failing case an `x OWN` row that passes the exit · none

## 8. Open questions

- **F1 — Which reds does the exit refuse before a core set exists?** Options: (a) a red on every leg
  that reads OWN, MIXED, DEAD PROBE or CONTENDED at R, the core set announced `not-installed`; (b) none,
  the core set being empty; (c) a typed list of core legs. (b) fails the clause's seen-red case, a
  planted own red refused, and (c) is the `core` tag I18 forbids. RESOLVED (agent, 2026-11-01,
  delegated): (a), rung 3, the one survivor; TOOL-dScopedBuild-7 narrows it to I18's rows. widens: none · relaxes: none
- **F2 — Where does `--close` run the contract?** Options: (a) a term of `build-complete`, the item
  TOOL-dDeclaredLoop-11 maps to `item.build.exit`; (b) inside `gates-green`, `item.test.verdict`'s arm;
  (c) a new `DOD_CORE` item. (c) adds an `--override` name and a row to every item reader for one
  contract, and (b) puts a Build item in Test's arm. RESOLVED (agent, 2026-11-01, delegated): (a),
  rung 3, the survivor meeting AC6 with the fewest readers moved. widens: none · relaxes: none
- **F3 — What is the base of a build with no first pass?** Options: (a) R, announced as `(tip)`;
  (b) refuse the exit. (b) refuses every spec run's close, whose commits are records and passes none.
  RESOLVED (agent, 2026-11-01, delegated): (a), rung 3. widens: none · relaxes: none
- **F4 — Does the attended verb run the bar or read one?** Options: (a) it runs the stage's one bar,
  attributed at R; (b) it reads the newest record under the git dir's `gate-run/`. (b) reads a bar the
  main loop may have run with no `GATE_ATTRIBUTE`, so no record says whose red it is. RESOLVED (agent,
  2026-11-01, delegated): (a), rung 3, the attended Stage 7 becoming the verb; grants: PLAY-dClosedLoop-3 the attended `/build` Skill's last stage and its workflow row run the exit verb. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from the packet's Items 1, flow-steps:283-299, research-build:77-79
  and :120, scout A's row 1 and its disagreement 1, and the spec brief's I1, I2 and I3.
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-32, TOOL-dScopedBuild-33, TOOL-dScopedBuild-35, promoted by the round-1 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-39,
  the promotions of the round-1 spec audit of units 25 to 35 (id 5).

## 10. Reuse audit

The seams extended are `read_first_passes` (`tools/memory-tree/deviation_join.py:325`, its second
caller, so it is extracted beside `read_routed_commits` at `tools/memory-tree/routed_commits.py:228`
rather than copied), `read_gates_record` (`tools/unattended/unattended.sh:9617`, the one reader of the
bar's record, extended by `GR_OWN`), `observe_anchor` (`:1974`) for R, and the `build-complete` arm
(`:11625`) as the unattended host. `python tools/codebase-map/reuse_lookup.py "derive a build's base
commit from history as the parent of its oldest first pass and refuse its exit on a red its own
commits introduced"` scanned every layer and ranked `build_commit` (`lib-unattended.sh:1186`) and
`resolve_compare_base` first; neither derives a base from passes, and `pass_commit` needs the anchor
it would derive (§4). Scout A's row 1 holds against source at `5f0b11f12`: its `:11098`, `:11121`
and `:9617-9651` read as it says. The recall probe surfaced the chain-order review's note that
flow-steps' range rule governs the exit's own-commit reading (`flow-steps.md:98-100`), which §4 "The
two bases" keeps.

Recall terms used: `python tools/memory-recall/query.py "how does an attended build's exit refuse a red its own commits introduced, with a base derived from history" --terms "exit contract gates-green attribution INHERITED OWN first pass base read_first_passes attended Skill gate-bar"`
