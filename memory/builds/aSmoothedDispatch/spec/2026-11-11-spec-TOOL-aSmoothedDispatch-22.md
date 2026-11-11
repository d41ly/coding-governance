# TOOL-aSmoothedDispatch-22 — the reconcile merge with main at bdb633d94: TOOL-dPavedRoad-1's `--spec` kept in the spec-token checker, unit 5's duplicate retired

**Status:** INPROGRESS · rev-1 · 2026-11-11 · node a · Tier-2 · base bdb633d9 · streams tooling · order 12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-11-prompt-TOOL-aSmoothedDispatch-22-reconcile.md](../prompts/2026-11-11-prompt-TOOL-aSmoothedDispatch-22-reconcile.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Local `main` and `origin/main` sit at `bdb633d94`. TOOL-dPavedRoad-1 shipped a `--spec` mode in
`tools/check-spec-tokens.py` there, and this build's TOOL-aSmoothedDispatch-5 added its own
`--spec` mode to the same checker. On 2026-11-11 the owner said "Keep main's --spec"
(`memory/DECISIONS.md:140`). This unit makes the `--no-ff` merge of `bdb633d94` into
`branch/aSmoothedDispatch`. It keeps main's checker, which grades several named specs of any status,
retires unit 5's one-path, live-only mode, and keeps every other part of this build. Cross-stream
merge, so Tier-2 (`memory/TEMPLATE-SPEC.md`, "Tiers").

## 2. Scope (IN)

The conflict set is the trial merge `git merge-tree --write-tree HEAD bdb633d94`, run at
`ba6c2f1f9` while this spec was written. It printed tree `de33b5c7` and the merge base `b904a0f91`.
Every line number below cited as "trial" is in that tree. The builder re-takes the conflict set at
the merge and records any difference in the acceptance ledger.

| File | Conflict regions | Kind |
|---|---|---|
| `tools/check-spec-tokens.py` | 8 | product |
| `tools/check-spec-tokens.test.sh` | 2 | suite |
| `memory/guides/SESSION-KICKOFF.md` | 1 | manifest stamp |

- **S1** — The merge. `git merge --no-ff --no-commit bdb633d94` on the run branch, the sha and never
  the moving name `main`. The merge commit has two parents, the branch's pre-merge tip and
  `bdb633d94`, and no conflict marker survives. Every file git auto-merged is carried as git merged
  it, except the files S4 and S7 re-render. Observed by AC1 and AC7.
- **S2** — The checker. `tools/check-spec-tokens.py` is taken whole from `bdb633d94`, so the merged
  file is byte-identical to main's. No line of unit 5's `scope` code, its refusal texts, its
  `spec-tokens: scope ·` line or its usage paragraph remains. Observed by AC2.
  **Readers:**
  by name: `tools/check-spec-tokens.test.sh` spells the retired `scope · --spec` line and the
  retired refusal texts in its `SD5` arms, at `:1988-2026` on this branch, and S3 rewrites or
  drops each. `tools/roles/house/gov-spec-writer.md` spells the retired "one-spec mode", at `:1`,
  and S4 rewrites it. No other tracked file outside the build records spells either, by a
  `git grep` over the trial tree at writing.
  by value: `tools/check-spec-tokens.test.sh` compares the retired output in the same arms. The
  driver `tools/unattended/unattended.sh` reads the checker's output but never passes `--spec`, by
  the same grep, so it reads no retired value.
- **S3** — The checker suite. Main's seven `PR1` arms and their `onespec` fixture are kept as main
  wrote them. Of unit 5's twelve `SD5` arms, ten are dropped and two are kept and re-pointed at
  main's output, as §4's table states arm by arm. The two `SD8` overlay-parity arms are kept and
  read the overlay S4 leaves. `FLOOR_ASSERTIONS` keeps both sides' `RAISED` lines and gains one
  `MERGED` line naming this unit. Observed by AC3.
  **Readers:**
  by name: `tools/check-spec-tokens.test.sh` is the one file that spells an `SD5` arm label, by a
  `git grep` over the trial tree at writing; the build's own records quote them.
  by value: NO VALUE READERS, because an arm label is printed and counted by no reader, and the
  floor that counts the arms is the `FLOOR_ASSERTIONS` pin this item recounts.
- **S4** — The writer's overlay. `tools/roles/house/gov-spec-writer.md` keeps only what main's kit
  prompt `tools/roles/agents/gov-spec-writer.agent.md:36-38` lacks: the exit-1 row shape, the
  summary shape, and the three refusal signs. `.claude/agents/gov-spec-writer.md` is re-rendered by
  `tools/roles/render_agents.py --write`, never by hand. Observed by AC4.
- **S5** — The hook. `tools/hooks/scratch-guard.js` is carried as git merged it. Its role-gate arm
  already admits main's multi-operand form to `gov-spec-writer`, as §4's probe shows, so the hook
  and its suite take no edit. Observed by AC5 and AC7.
- **S6** — The kickoff manifest. `memory/guides/SESSION-KICKOFF.md` takes main's side of its one
  conflict region, then `last-audit` is re-stamped by the manifest's own stamp rule, and the merge
  commit's body carries the `manifest-audit:` delta line. Observed by AC6.
- **S7** — Generated outputs. The build index, LIVE, the ledger, `memory/map/generated/symbols.json`
  and the rest of the codebase map are re-rendered by their generators after the hand-resolved
  sources are staged, never hand-merged. Observed by AC7.

## 3. Non-goals (OUT)

- Any change to what main's `--spec` grades, refuses or prints.
- Any edit to `tools/hooks/scratch-guard.js` or its suite. A widening and its arm were owed only if
  the hook refused the multi-operand form, and it does not.
- Re-opening unit 5's, unit 7's or unit 8's spec. All three are CLOSED and stay frozen; the owner's
  ruling is recorded at `memory/DECISIONS.md:140`.
- The unattended driver and its suite.
- A kit version mint. The checker's `KIT_SPEC_TOKENS_VERSION` arrives as main wrote it, and the
  lander's `mint` moves any version this build's bytes owe.
- Pushing, and the `--no-ff` merge of this branch into `main`. Both are the main loop's.
- A contradiction the brief's items cannot resolve is not decided here. The pass runs
  `git merge --abort`, leaves the branch at its pre-merge tip, and returns the hunk and both sides'
  intent to the owner.

### Edges

- **consumes-from** external — `main` at `bdb633d94`, carrying TOOL-dPavedRoad-1's `--spec` and
  aShelvedLeg's landing. If `git rev-parse main` reads another sha when the pass starts, the pass
  still merges `bdb633d94` and records the moved sha in the ledger.

## 4. Design

### What each side did, read at `ba6c2f1f9` and `bdb633d94`

| Fact | Where |
|---|---|
| Unit 5's mode: one path, which must be LIVE, refusals ending `no file there` and `not a live spec`, hits filtered to the scope, and one `scope ·` line. | `git diff b904a0f91 HEAD -- tools/check-spec-tokens.py`, eight hunks; unit 8 (`55d65f5c8`) only reworded its docstring |
| Main's mode: `read_named_specs` takes every later operand not opening with `-`, refuses with exit 2, and grades each named spec whatever its status. | `tools/check-spec-tokens.py:1541-1563` and `:1581-1587` at `bdb633d94` |
| Main's mode prints `spec-tokens: --spec · <N> named spec(s) graded whatever their status · ` ahead of the usual population line. | `tools/check-spec-tokens.py:1945-1948` at `bdb633d94` |
| A hit prints `spec-tokens: <path> [<kind>]` then its backticked token, and the summary is `spec-tokens: <N> unwaived hit(s), <M> stale row(s)` before exit 1. | `tools/check-spec-tokens.py:2052-2058` at `bdb633d94` |
| Every refusal under `--spec` opens `spec-tokens: REFUSING — --spec`, and each returns 2. | `tools/check-spec-tokens.py:1547`, `:1553`, `:1560`, `:1585` at `bdb633d94` |
| The kit prompt already tells the writer to run `check-spec-tokens.py --spec <path>` over each spec it wrote, fix every hit, and run no other gate. | `tools/roles/agents/gov-spec-writer.agent.md:36-38` at `bdb633d94` |

### S2 — the checker

```bash
git checkout bdb633d94 -- tools/check-spec-tokens.py
```

Resolving only the eight conflict regions to main's side is not enough. Unit 5's lines also sit
outside them: its usage paragraph at trial line 265 and its `scope ·` print at trial line 2034, for
two. The second reads `scope`, which main's side of the region at trial lines 1602-1657 no longer
defines, so a hunk-wise resolution raises a `NameError` on every run.

### S3 — the suite resolution

**Every `SD5` arm, at this branch's line, and its disposition.**

| Line | Arm | Disposition |
|---|---|---|
| 1995 | `SD5 AC1` an untracked spec is graded and reds on its leg | dropped: `PR1 AC1` grades an untracked spec and reds, and the `SD8` row arm asserts this arm's exact needle |
| 1998 | `SD5 AC2` a hit only in the tracked spec is not reported | KEPT, re-pointed: no `PR1` arm can see it, because the tracked spec's hit in `onespec` is waived and prints nothing either way |
| 1999 | `SD5 AC2` the carries and packet joins say they did not run | dropped: the two `PR1 AC2` arms assert both lines |
| 2001 | `SD5 AC3` no value refuses with exit 2 | KEPT, re-pointed: main refuses an empty operand list, and no `PR1` arm runs one |
| 2003 | `SD5 AC3` a path outside the spec folders refuses | dropped: `PR1 AC4` refuses an operand that is not a spec |
| 2005 | `SD5 AC3` a path naming no file refuses | dropped: `PR1 AC4` refuses an operand that names no file |
| 2008 | `SD5 AC3` a CLOSED spec refuses | dropped: main's mode grades a spec of any status |
| 2012 | `SD5 AC5` an unproduced waiver row is STALE on the bare run | dropped: a bare-run control for the arm below, and the bare-run case is the suite's own `a stale waiver REDS` at `:538` |
| 2014 | `SD5 AC5` the same row is not reported under `--spec` | dropped: main skips the whole stale-waiver loop under `--spec`, the one branch `PR1 AC2` observes |
| 2021 | `SD5 AC4` a hand-off to an untracked sibling reds | dropped: `PR1 AC3` reds on the same join from an untracked sibling |
| 2023 | `SD5 AC4` the hand-off is green once the sibling names the token | dropped: both `PR1 AC2` arms run green after the sibling names the token |
| 2026 | `SD5 AC6` the bare run prints no scope line | dropped: main prints no scope line, and `PR1`'s bare-run arm asserts the bare population |

**The merged block.** The conflict region at trial lines 1995-2086 resolves to main's `PR1` block
as main wrote it, then the two kept arms below, then this branch's `SD8` block unchanged. The `SD8`
block reads `$d` and `$sc_spec`, which the kept block sets, so the order is fixed. The kept block's
header must not carry the string `SD5` followed by a space, which AC3 counts.

```bash
# ---- TOOL-aSmoothedDispatch-5: the two --spec arms the PR1 arms above do not cover, kept at
#      TOOL-aSmoothedDispatch-22's reconcile and re-pointed at main's --spec output. The named spec
#      is written and NEVER added. The overlay-parity arms below read the same scratch repo.
sc_spec="$SPECDIR/$HCUT-spec-TOOL-tOne-7.md"
d=$base/scope; scratch "$d"
write_handoff_spec "$d" "$sc_spec" TOOL-tOne-7 OPEN '## 7. Gates' '' '`real leg`.'
sed -i 's|^`real leg`\.|`imaginary leg`.|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
ARM_ARGS=(--spec "$sc_spec")
arm "SD5 AC2 a hit only in the tracked spec is not reported under --spec" 0 "$d" "--spec · 1 named spec(s) graded whatever their status · 1 live spec(s)" "2026-09-02-spec-TOOL-tOne-1.md"
ARM_ARGS=(--spec)
arm "SD5 AC3 --spec with no value REFUSES with exit 2" 2 "$d" "REFUSING — --spec names no spec"
ARM_ARGS=()
```

**The floor.** The region at trial lines 62-73 keeps this branch's two `RAISED` lines, then main's
one, then this line and the pin:

```bash
# MERGED at TOOL-aSmoothedDispatch-22's reconcile: the base 224, plus TOOL-dPavedRoad-1's 7, plus this
# branch's 14, less the ten unit 5 arms dropped there = 235. Counted by reading; OWED: observed at the close.
FLOOR_ASSERTIONS=235
```

The figure is DERIVED: each `arm` call above counts once, as every `RAISED` line beside it counts.
The builder recounts off the merged lines, and a count that differs wins and moves this spec by a rev.

### S4 — the overlay

`tools/roles/house/gov-spec-writer.md` is replaced whole by the text below. It drops what the kit
prompt already says: when to run the check, its command, fixing each hit, and that the bare leg is
not the writer's. It keeps the three facts the kit prompt lacks. Each backticked span stays on one
line, because the `SD8` arms read each span with a line-wise `grep -o`.

```text
A `check-spec-tokens.py --spec` run that finds a miss exits 1. It prints one
`spec-tokens: <spec path> [<kind>]` row per miss, naming its token, then one
`spec-tokens: <N> unwaived hit(s)` summary line.
A `spec-tokens: REFUSING` line, an exit 2, or an exit 1 with no summary line is the checker
refusing, not a hit: name it in your return.
```

Each shape is main's: the row and the summary at `tools/check-spec-tokens.py:2053` and `:2057`,
the refusal at `:1547-1560`, and an exit 1 with no summary at each `REFUSING` return between `:1577`
and `:1909`. Then `python tools/roles/render_agents.py --write` from the repository root re-renders
`.claude/agents/gov-spec-writer.md`. Any other file it writes is listed in the ledger.

### S5 — the hook probe

The role-gate arm refuses a G1 leg only when the command's words equal the leg's argv word for word
(`tools/hooks/scratch-guard.js:1440-1446`). The spec-token leg's argv is the checker with no
argument (`tools/gate-legs.json:1758-1762`), and the G3 suite shape needs a `.test.sh` head or
`--selftest` (`tools/hooks/scratch-guard.js:1401-1406`). So `--spec` with any number of operands
is neither. Main's hook diff from `b904a0f91` touches only `loadRoleIndex` and the version comment.
Unit 5 changed no hook code; its admission is this rule, pinned by its three rows at
`tools/hooks/scratch-guard.test.sh:1274-1281`.

The probe below, run at `ba6c2f1f9` while this spec was written, printed `exit=0` with an empty
stderr for the two-operand form, and `exit=2` naming `G1 leg` for the bare leg, its liveness
control. AC5 re-runs it at the merge. `$SCRATCH` is the run's scratch directory.

```bash
probe() {
  python -c 'import json,sys; print(json.dumps({"tool_name":"Bash","tool_input":{"command":sys.argv[1]},"cwd":sys.argv[2],"agent_type":"gov-spec-writer"}))' "$1" "$PWD" \
    | node tools/hooks/scratch-guard.js >/dev/null 2>"$SCRATCH/sd22-hook.err"
  echo "exit=$?"; cat "$SCRATCH/sd22-hook.err"
}
probe "python tools/check-spec-tokens.py --spec memory/builds/x/spec/a.md memory/builds/x/spec/b.md"
probe "python tools/check-spec-tokens.py"
```

### S6 — the manifest stamp

Both sides re-stamped `last-audit` in the one conflict region, at trial lines 5-9: this branch at
`1038ada92`, main at `2a55e3ff3`. Both keep `last-body-change: 1dc7a7932`. The resolution takes
main's line, then re-stamps it by the stamp rule at `skills/session-kickoff/MANIFEST-TEMPLATE.md:30`,
"sha = `HEAD` on any branch", with the datetime advanced to the merge's. During the merge `HEAD` is
the branch's pre-merge tip, which is the precedent merge `ccfa23ffe`'s choice. Its check 5
(`skills/session-kickoff/manifest-check.sh:1646-1663`) then finds the merge itself as the stamp
commit, at or after every watched change. The builder re-checks the §B claims against the files
main moved under `watch`, `tools/gate-legs.json` among them. The merge commit's body carries
`manifest-audit: delta <none|summary> · watch-commits-since-stamp: <n>`, with `n` counted before
the re-stamp as `git rev-list --count 2a55e3ff3..HEAD -- <watch…>`. It read 2 at `ba6c2f1f9`.

### S7 — generated outputs

After S2 to S6 are staged: `python tools/memory-tree/gen_build_index.py --write`, then
`python tools/codebase-map/gen_map.py --write`, and stage what they change. The trial merge printed
its `merge-rows:` line clean, so the `merge=rows` driver is wired in this clone.

### The commits

The shape follows unit 21's merge `0a3eef5ca`. The merge commit's subject is
`merge: main bdb633d94 into aSmoothedDispatch — TOOL-aSmoothedDispatch-22, main's --spec kept in the spec-token checker`.
Its body names each conflicted file's resolution and carries S6's delta line, and its trailer is
`Pass: none`, because a merge's index holds every path `main` moved. A pass commit follows it,
trailer `Pass: TOOL-aSmoothedDispatch-22`, carrying this spec's CLOSED header, the acceptance
ledger and the index re-render.

### Files touched (estimate)

- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `tools/roles/house/gov-spec-writer.md`
- `.claude/agents/gov-spec-writer.md`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/builds/aSmoothedDispatch/README.md`
- `memory/LIVE.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Keep both modes under two flag names.** The owner ruled for main's `--spec` alone.
- **Resolve only the conflict regions to main's side.** Unit 5's lines outside them survive, and
  one reads a name main's side no longer defines, as S2 states.
- **Keep all twelve `SD5` arms, re-pointed.** Ten would re-observe what a `PR1` arm or an older arm
  already observes, and three test behaviour main's mode does not have.
- **Drop every `SD5` arm.** Two cases no other arm covers would go unobserved.
- **Point the `SD8` arms at main's `onespec` fixture.** By the end of the `PR1` block that spec is
  green, so the arms would need a new red planted there. The kept block's repo already holds one.
- **Add a scratch-guard arm for the multi-operand form.** The hook admits it by a rule its existing
  rows pin, and the brief owes an arm only for a widening.

## 5. Production-readiness checklist

- security — the hook still refuses the bare leg and the checker suite to `gov-spec-writer`, AC5's
  control. Main's `--spec` is read-only and refuses an operand outside a build's `spec/` folder.
- perf / scale — N/A: main's mode runs the same per-spec joins over the named specs.
- error / empty / loading states — an empty operand list refuses with exit 2, the kept `SD5 AC3` arm.
- observability — the ledger records `main`'s sha at pass start, each file's resolution, the probe
  outputs and every file the renderer and the generators wrote.
- risks — a hunk-wise checker resolution breaks every run, which AC2 catches. A dropped arm that
  covered a case nothing else covers loses coverage, and §4's table names the covering arm per drop.
- testing — the probes in §6 for the pass, and the checker and scratch-guard suites at the close.
- migration — N/A: no record or schema moves.
- user docs — N/A: no `help/` page names the spec-token checker, by a `git grep` at writing.

## 6. Acceptance criteria

- **AC1** — When `git rev-list --parents -n 1 <merge>` runs, it prints the merge sha, the branch's
  pre-merge tip and `bdb633d94ec030f45a76670331fafa3fc7de4563`.
  Red when: the merge is squashed, rebased or made from `main` after it moved, so a parent differs.
- **AC2** — When `git diff bdb633d94 <merge> -- tools/check-spec-tokens.py` runs, it prints nothing.
  When `python tools/check-spec-tokens.py --spec` runs at the merge, it prints
  `spec-tokens: REFUSING — --spec names no spec` and exits 2.
  Red when: only the conflict regions are resolved, so unit 5's usage paragraph and `scope ·` print
  survive and the diff is not empty.
- **AC3** — When these run over the checker's suite file, the one the `New arm:` lines name, at the
  merge, they print as stated.
  `grep -c 'SD5 '` prints 2, and `grep -c 'arm "PR1 '` prints 7, and `grep -c 'arm "SD8 '` prints 2.
  `grep -c 'REFUSING — --spec names no spec'` prints 1.
  `grep -c 'graded whatever their status · 1 live spec(s)'` prints 1.
  `grep -cF 'scope · --spec'` and `grep -c 'not a live spec'` each print 0.
  `grep '^FLOOR_ASSERTIONS='` prints `FLOOR_ASSERTIONS=235`.
  `grep -c "MERGED at TOOL-aSmoothedDispatch-22's reconcile"` prints 1, and
  `grep -c 'RAISED 224 -> 236 by TOOL-aSmoothedDispatch-5'` and
  `grep -c 'RAISED 224 -> 231 by TOOL-dPavedRoad-1'` each print 1.
  `grep -cE '^(<<<<<<<|>>>>>>>) |^=======$'` prints 0, and `bash -n` over the file exits 0.
  Red when: an `SD5` arm covered by a `PR1` arm is kept, so the first count exceeds 2, or the floor
  takes one side's value, 238 or 231.
  figure: 235 is DERIVED from both parents' floors and §4's table; a recount that differs moves it
  by a rev of this spec.
- **AC4** — When these run over `tools/roles/house/gov-spec-writer.md` at the merge, they print as
  stated. `grep -c 'spec-tokens: <spec path> \[<kind>\]'`, `grep -c 'spec-tokens: <N> unwaived hit(s)'`
  and `grep -c 'spec-tokens: REFUSING'` each print 1. `grep -c 'one-spec mode'`,
  `grep -c 'Before you return'`, `grep -c 'is the gate leg'` and `grep -c '<prefix>'` each print 0.
  `python tools/roles/render_agents.py --check` exits 0, and
  `grep -c 'spec-tokens: <N> unwaived hit(s)' .claude/agents/gov-spec-writer.md` prints 1.
  Red when: the overlay keeps a sentence the kit prompt says, or the agent file is hand-edited or
  left stale.
- **AC5** — When §4's `probe` runs at the merge, the two-operand `--spec` command prints `exit=0`
  and an empty stderr, and the bare `python tools/check-spec-tokens.py` prints `exit=2` and a
  `G1 leg` line.
  Red when: the merged hook refuses the multi-operand form, which S5 would then owe a widening for.
- **AC6** — When these run at the merge, they print as stated. Over
  `memory/guides/SESSION-KICKOFF.md`, `grep -c '^last-audit: .* @ <the first parent, in full>$'`
  prints 1, `grep -c '^last-body-change: 1dc7a7932d57dda674832fcd143d97b7a06edd3d$'` prints 1, and
  the conflict-marker grep of AC3 prints 0. `git show -s --format=%B <merge>` piped to
  `grep -c '^manifest-audit: delta .* · watch-commits-since-stamp: '` prints 1.
  Red when: either side's stamp is kept as merged, so the stamp sha is `1038ada92` or `2a55e3ff3`.
- **AC7** — When `git diff --name-only de33b5c71e20ea4f4fd6d69044e976f4d5563b58 <merge> -- tools skills .claude`
  runs, it lists only `tools/check-spec-tokens.py`, the checker's suite file,
  `tools/roles/house/gov-spec-writer.md` and `.claude/agents/gov-spec-writer.md`. On the pass
  commit, `python tools/memory-tree/gen_build_index.py --write` then
  `python tools/codebase-map/gen_map.py --write` leave `git status --porcelain` empty.
  Red when: the hook or another auto-merged product file is hand-edited, or a generated file is
  committed stale or hand-merged.
  fixture: the trial tree is the one `git merge-tree --write-tree HEAD bdb633d94` printed at
  `ba6c2f1f9`; a builder whose pre-merge tip differs re-takes it with that command and uses its sha.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `scratch-guard self-test` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `roles render wiring` · `roles render selftest` · `roles catalogue` · `kickoff-manifest ratchet` · `memory hygiene` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `shell hygiene (a location probe asked from a moved directory)` · `install-prefix (shipped surface)` · `docs` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `codebase-map coverage + freshness` · `pass-order history` · `routed commits name a specced unit` · `brief-recorded`

New arm: tools/check-spec-tokens.test.sh · covers AC3 · the kept `SD5 AC2` arm, re-pointed at main's `--spec ·` population line; staged by making main's `--spec` population add every tracked spec, so the planted `imaginary leg` in the tracked spec reds with exit 1 · none, the floor moves by the merge as AC3 states
New arm: tools/check-spec-tokens.test.sh · covers AC3 · the kept `SD5 AC3` arm, re-pointed at `REFUSING — --spec names no spec`; staged by deleting the empty-operand refusal in `read_named_specs`, so the empty population refuses with exit 1 · none
New arm: tools/check-spec-tokens.test.sh · covers AC4 · the two `SD8` overlay-parity arms, now reading S4's overlay against main's checker; staged by respelling the overlay's summary span as `spec-tokens: <N> unwaived miss(es)`, which still parses and which the red run does not print · none

The main loop also runs the checker suite and the scratch-guard suite at the close, and each prints
no FAIL line. The bar runs once after that, through the lander. This spec's author ran no gate but
the spec-token checker's `--spec` mode over this file.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-11 · initial draft from brief `2026-11-11-prompt-TOOL-aSmoothedDispatch-22-reconcile`,
  grounded on the trial merge of `bdb633d94` into `ba6c2f1f9`. Item 4's "unit 5's allow" is read as
  the role-gate arm's exact-argv rule and unit 5's three suite rows, since unit 5 changed no hook
  code. Item 2's drop rule is applied arm by arm in §4; the bare-run `SD5 AC5` control is dropped
  with its scoped partner, its own case armed at the suite's `:538`.

## 10. Reuse audit

The seams this unit extends: main's `read_named_specs` (`tools/check-spec-tokens.py:1541` at
`bdb633d94`), kept whole; main's `PR1` arms and the suite's `arm` helper
(`tools/check-spec-tokens.test.sh:371`); the roles kit's renderer `tools/roles/render_agents.py
--write` for the agent file; the role-gate arm's G1 rule (`tools/hooks/scratch-guard.js:1440-1446`),
which already admits the multi-operand form; and the reconcile shape of unit 21's merge `0a3eef5ca`
and of `ccfa23ffe` for the stamp. `tools/codebase-map/reuse_lookup.py` ranked only generic name
stems (`check`, `merge`, `resolve_prefix_token`) for "keep one side's spec-token checker mode and
retire the other side's duplicate at a merge", so no existing code seam fits a merge, which is a
git operation. Recall's hits were unit 21's spec, this unit's decision row and brief, the open ask
`TOOL-dUnstuckLanding-26` for a gate on merges that drop one side's hunks, and the `[reconcile]`
rule that a generated region is re-rendered and never merged (`PLAY-dClosedLoop-35`).

Recall terms used: `python tools/memory-recall/query.py "how was a reconcile merge that kept main's side of a duplicated checker mode recorded" --terms "reconcile merge keep main side spec-token checker --spec duplicate retire arms floor overlay re-stamp"`
