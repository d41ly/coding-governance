# TOOL-aTrimmedWait-13 — close repair: the driver suite's parity table gains the `--check-specs` row unit 1 owed

**Status:** SPECCED · rev-1 · 2026-11-16 · node a · Tier-1 · base 5d48501da · streams tooling · order 12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-16-prompt-TOOL-aTrimmedWait-13-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-aTrimmedWait-13-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-aTrimmedWait-13-brief.md](../prompts/2026-11-16-prompt-TOOL-aTrimmedWait-13-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The driver suite's parity arm reads `--check-specs` as a row, so its verb loop stops printing
`FAIL parity: the verb --check-specs has no row in the parity table`, and no other verdict moves
(`prompts/2026-11-16-prompt-TOOL-aTrimmedWait-13-brief.md`, the owner's ruling of 2026-11-16).

## 2. Scope (IN)

- **S1** — One `PARITY_ROWS` row in `tools/unattended/unattended.test.sh`, written
  `check-specs | : | --check-specs tRun ARCH-tRun-1` on the line after the
  `plan framed over two slugs` row. Observed by AC1 and AC2.
- **S2** — `FLOOR_ASSERTIONS` raised 3374 to 3377 and `FLOOR_SHARD_1` raised 734 to 737, each with
  one `RAISED` comment directly above its value, in the forms §4 gives. Observed by AC3.
- **S3** — The pass changes no other file under `tools/`, and `tools/unattended/unattended.sh` least
  of all. Observed by AC4.

## 3. Non-goals (OUT)

- The other 23 FAIL lines of the run at `c50583f10`: main's `KEEPALIVE_INTERVAL` and `--wake` rows,
  the parity rows of `register-task`, `release-task` and `liveness`, and the rows earlier builds
  recorded. They are filed as asks, not repaired here.
- Any change to `tools/unattended/unattended.sh`, its usage table or its verb lists.
- A setup that plants a spec so the row reaches the verb's clean line (§4, Alternatives rejected).
- Any other row, arm or comment of the suite moved or reworded.
- No self-test suite and no bar inside the pass, a sliced suite included.

## 4. Design

### Evidence

Read on 2026-11-16 at `0351ece20`. The suite's blob is the same at `c50583f10`
(`de652f66e052`), and so is the driver's (`69c5b9897a9d`).

- The parity table is `PARITY_ROWS` (`tools/unattended/unattended.test.sh@de652f66e052:2445`), 41
  rows of `label | setup | argv`. Its loop (`:2488`) resets the tree for each row, runs the argv as a
  process and through `run_inproc`, and makes three `same` calls: output through `render_stable`,
  exit status, and the tree through `derive_tree_digest`.
- The verb loop (`:2505`) walks `verbs_all` and `--overlaps`, makes one `n=$((n+1))` per verb whether
  or not it finds a row, and prints the FAIL line when `\| *<verb>( |$)` matches no row.
  `verbs_all` (`tools/unattended/unattended.sh#verbs_all`) prints `VERBS_SLUG` and `VERBS_INLINE`,
  and `VERBS_INLINE` carries `--check-specs` (`tools/unattended/unattended.sh@69c5b9897a9d:120`).
  The probe below found `--check-specs` the only verb with no row, at `c50583f10` and at `HEAD`.
- The table is region one's: it opens with `if in_shard 1; then` after
  `fi   # ---- region 1 continues below` (`:2423`). The tail compares the executed count with
  `FLOOR_ASSERTIONS` unsharded and with `FLOOR_SHARD_<k>` under `--shard k/8` (`:2184-2186`).
- Each row resets to `UNIT0` (`reset_tree`, `:622`), where the `tRun` build holds no spec (the
  comment at `:692`). `check_dispatch_specs` (`tools/unattended/unattended.sh#check_dispatch_specs`)
  therefore reaches `check_unit_spec`'s MISSING branch, prints its check-49 line, scans no edges and
  returns 1. Unit 1's arm grades the same refusal for a slug with no spec (`:8143`).
  `load_spec_facts` empties its three maps before it fills them, so the in-process side reads no
  map a previous call left in the suite's shell.
- The precedent row is TOOL-dFoldedAudit-7's `a malformed SPEC_FOLD_CUTOFF, rc 2`, which raised both
  floors in the same two places (`:19815` and `:20033`).

### The change

The row, after `plan framed over two slugs | : | --plan tRun tNone --framed`:

```text
check-specs | : | --check-specs tRun ARCH-tRun-1
```

Its setup is `:` like every slug row but `check-commit`'s, and it exits 1 on both sides. The verb
loop's count does not move, and neither do `parity: every declared row ran`, which derives its
figure from the table, or `parity: the rows reach exit 0, 1 and 2`. The loop's three `same` calls
run once more in region one, so both floors rise by 3.

Directly above `FLOOR_ASSERTIONS=3374`, after the `MERGED` comment of TOOL-aTrimmedWait-12:

```text
# RAISED 3374 -> 3377 by TOOL-aTrimmedWait-13: the parity table's `--check-specs` row, the loop's three `same`
# lines run once more in region one, every one unconditional, counted off the loop's own lines; no suite
# ran, and its RED-first observation is the close's.
FLOOR_ASSERTIONS=3377
```

Directly above `FLOOR_SHARD_1=734`:

```text
# RAISED 734 -> 737 by TOOL-aTrimmedWait-13: the same 3 region-one parity-row assertions, see FLOOR_ASSERTIONS.
FLOOR_SHARD_1=737
```

The parity block grows from 1218 lines to 1219, well under the 2500-line block arm. <!-- PINNED 2026-11-16 -->

### The probes

`$SCRATCH` is the run's scratch directory. Both probes run from the worktree root.
`bash "$SCRATCH/t13.sh"` reads the suite at `c50583f10` and in the worktree:

```bash
set -u
F=tools/unattended/unattended.test.sh; T=${1:-$F}
rows() { sed -n '/^PARITY_ROWS="/,/"$/p'; }
verbs=$(bash -c '. tools/unattended/unattended.sh >/dev/null 2>&1; verbs_all')
for side in c50583f10 tree; do
  if [ "$side" = tree ]; then t=$(rows < "$T"); else t=$(git show "$side:$F" | rows); fi
  m=""; for v in $verbs --overlaps; do grep -qE -- "\| *$v( |\$)" <<<"$t" || m="$m $v"; done
  echo "rowless $side${m:- none} rows $(printf '%s\n' "$t" | grep -c '|')"
done
echo "row $(grep -cxF 'check-specs | : | --check-specs tRun ARCH-tRun-1' "$T")"
echo "loop same $(sed -n '/^while IFS=.|. read -r _pt_l/,/^done <<< "\$PARITY_ROWS"/p' "$T" | grep -cE '^[[:space:]]*(same|hit|miss) ')"
echo "floors $(grep -cxE 'FLOOR_ASSERTIONS=3377|FLOOR_SHARD_1=737' "$T") raised $(grep -cE '^# RAISED (3374 -> 3377|734 -> 737) by TOOL-aTrimmedWait-13: ' "$T")"
bash -n "$T" && echo "syntax ok"
```

The `rowless` lines run the verb loop's own predicate over the table at both sides, so a row the
predicate cannot read shows. `bash "$SCRATCH/t13-parity.sh"` runs the row's argv both ways over a
scratch repository carrying the suite's own `mkconf` conf and no spec:

```bash
set -u
W=$(pwd); R=$(mktemp -d); cd "$R" || exit 2
git init -q -b main && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
eval "$(sed -n '/^mkconf() {/,/^}/p' "$W/tools/unattended/unattended.test.sh")"
mkconf; git add -A && git commit -qm base --no-verify
p=$(bash "$W/tools/unattended/unattended.sh" --check-specs tRun ARCH-tRun-1 2>&1); pr=$?; ps=$(git status --porcelain)
i=$( ( . "$W/tools/unattended/unattended.sh"; load_driver_conf && main --check-specs tRun ARCH-tRun-1 ) 2>&1); ir=$?; is=$(git status --porcelain)
echo "parity rc proc=$pr inproc=$ir output $([ "$p" = "$i" ] && echo same || echo differs) tree $([ "$ps" = "$is" ] && [ -z "$ps" ] && echo clean || echo moved)"
echo "missing $(printf '%s\n' "$p" | grep -c 'MISSING.*: ARCH-tRun-1$')"
cd "$W"; rm -rf "$R"
```

On 2026-11-16 both ran against a scratch copy of the suite carrying exactly the change above, read
as `bash "$SCRATCH/t13.sh" <copy>`. They printed every line §5 names, and the copy differed from
the tree by nine diff lines.

### What it does not check

- That the row passes in the suite's own shell. The probe's in-process side sources the driver into
  a fresh shell, while the suite's has run every earlier region-one arm. The close's run observes it.
- That either side agrees past the MISSING refusal. The row never reaches `plan_state`, the order
  read or the clean line, which unit 1's region-three arm grades through `run` alone.
- That the suite executes at least 3377 assertions, or region one at least 737. Both are DERIVED
  sums, first observed when the suite runs at the close.
- Any of the other 23 FAIL lines, which stay red.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`
- `memory/builds/aTrimmedWait/build/2026-11-16-build-TOOL-aTrimmedWait-13-1-acceptance-ledger.md`

### Rollout

One pass at order 12, in the branch's own worktree. The card must route to this unit with its spec
INPROGRESS before the pass, or the scratch-guard refuses the edit. One commit carries the suite and
the ledger, ending with `Pass: TOOL-aTrimmedWait-13` and the commit trailer, and the status flip to
CLOSED follows as a status-only commit.

### Alternatives rejected

- **A setup that plants a READY `tRun` spec, so the row reaches the clean line.** The row would then
  read `plan_state` and the order verb in process. But no other slug row plants a fixture, a spec
  written inside the double-quoted table cannot carry the backticks a scoped acceptance line uses,
  and the brief asks for a row the fixture's `tRun` build answers as it stands.
- **The argv `--check-specs tRun` with no unit.** It reaches only the check-14 refusal and never loads
  a spec.

## 5. Acceptance criteria

Each `rowless`, `row`, `loop`, `floors` and `syntax` line comes from one run of
`bash "$SCRATCH/t13.sh"` after the edit, and the `parity` and `missing` lines from one run of
`bash "$SCRATCH/t13-parity.sh"`.

- **AC1** — When `bash "$SCRATCH/t13.sh"` runs, it prints
  `rowless c50583f10 --check-specs rows 41`, `rowless tree none rows 42` and `row 1`.
  Red when: the row is missing, or spelled so the verb loop's predicate does not read it, or a second
  row is added.
  figure: 41 and 42 are DERIVED by the probe's count of the table's `|` lines.
- **AC2** — When `bash "$SCRATCH/t13-parity.sh"` runs, it prints
  `parity rc proc=1 inproc=1 output same tree clean` and `missing 1`.
  Red when: the argv is not a form the verb accepts, or its two sides disagree on output, status or
  tree.
  cost: about five seconds.
- **AC3** — When `bash "$SCRATCH/t13.sh"` runs, it prints `loop same 3` and `floors 2 raised 2`.
  Red when: a floor keeps its old value, rises by a count other than the loop's, or loses its
  `RAISED` comment.
  figure: 3 is DERIVED by the probe's count of the loop's own `same` lines, and 3377 and 737 are
  each floor's value at `0351ece20` plus that count.
- **AC4** — When `bash "$SCRATCH/t13.sh"` runs it prints `syntax ok`, and after the pass commit
  `git show --name-only --format= HEAD -- tools/ ':!tools/unattended/unattended.test.sh'` prints
  nothing.
  Red when: the suite no longer parses, or the commit changes the driver or any other tool.
- **AC5** — When `python tools/check-spec-tokens.py --spec` runs over this spec's path it exits 0, and `bash tools/unattended/unattended.sh --check-specs aTrimmedWait TOOL-aTrimmedWait-13`
  prints its `none carries a refusal` line.
  Red when: this spec carries a token the checker refuses, or a spec-file refusal `--dispatch` makes.

## 6. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

`python tools/check-spec-tokens.py --legs-for tools/unattended/unattended.test.sh` names only broad
`tools/` guards. The two recall floor legs are owed by the ledger path under `memory/`. The main loop runs the merge bar once at the close,
without the self-test suites, and the driver suite once at the close on a frozen clone.

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 · the parity table's check-specs row; RED is the run at c50583f10, where the verb loop printed FAIL parity: the verb --check-specs has no row in the parity table; GREEN is the close's run on a frozen clone, that line gone, no FAIL line naming parity check-specs, and every other FAIL line one the c50583f10 run printed · FLOOR_ASSERTIONS 3374 to 3377, FLOOR_SHARD_1 734 to 737

The suite still exits 1 at the close, on the 23 lines §3 leaves. Its GREEN is the comparison of FAIL <!-- PINNED 2026-11-16 -->
sets above, not its exit status.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-16 · initial draft from `prompts/2026-11-16-prompt-TOOL-aTrimmedWait-13-1-spec-writer.md`,
  grounded at `0351ece20`. Both probes were run over a scratch copy of the suite carrying the change.

## 9. Reuse audit

The seam is the parity table itself, `PARITY_ROWS` in `tools/unattended/unattended.test.sh`, extended
by one row as TOOL-dFoldedAudit-7 extended it, with no new helper. `python tools/codebase-map/reuse_lookup.py "a parity table row that runs the driver verb as a process and in process and compares output, exit status and tree"`
ranked generic name stems only (`rows`, `row`, `run`, `tree`), none of them this table. Of the
task's named seams, `verb_dispatch` and `check_unit_spec` are read for the row's refusal path, and
`check_dispatch_specs` is the verb the row drives. `plan_state` and `order_verb_of` are named in §4
as what the row does not reach. `scan_consumes_cycles` runs with no edges. `run_spec_token_check`,
`derive_spec_token_key`, check 12's loop and `--only`, the `--check --staged` render decision,
`scanCommandHeads`, `checkRoleGate` and `load_session_calls` are untouched. The parity probe reuses
the suite's own `mkconf` rather than a second conf.

Recall terms used: `python tools/memory-recall/query.py "how was a verb added to the driver given its parity table row and the floors raised" --terms "PARITY_ROWS parity table row verbs_all run_inproc derive_tree_digest render_stable FLOOR_SHARD_1 FLOOR_ASSERTIONS RAISED shard"`
