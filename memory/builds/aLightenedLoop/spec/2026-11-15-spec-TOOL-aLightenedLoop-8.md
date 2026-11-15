# TOOL-aLightenedLoop-8 — the reconcile with origin/main: the merge, and unit 3's input-keyed spec-token cache carried onto the check's start and read halves

**Status:** SPECCED · rev-1 · 2026-11-15 · node a · Tier-2 · base aebbb4a7 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aLightenedLoop-8-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aLightenedLoop-8-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aLightenedLoop-8-reconcile.md](../prompts/2026-11-15-prompt-TOOL-aLightenedLoop-8-reconcile.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Merge `origin/main` at `aebbb4a72` into `branch/alightenedloop-eb7b8b` and resolve its five
conflicts (`prompts/2026-11-15-prompt-TOOL-aLightenedLoop-8-reconcile.md`). The one that needs
design is `run_spec_token_check`. Main's TOOL-aBriskDeclaration-1 split it into a start half that
keys and starts the checker before the open-pass reader, and a read half that prints and refuses.
This branch's TOOL-aLightenedLoop-3 re-keyed its cache on the checker's recorded inputs, and
TOOL-aLightenedLoop-6 moved the key's derive inside the tree-state bracket. The owner chose to carry
unit 3's cache, as unit 6 left it, onto main's split. Main's overlap, silence and refusal order stay
as main shipped them, and unit 3's and unit 6's verdicts and lines stay as their specs state them.

## 2. Scope (IN)

- **S1** — The merge. `git merge --no-ff origin/main`, with `origin/main` at `aebbb4a72`, commits
  with both parents and leaves no conflict marker. The five conflicted files resolve by S2 to S7,
  and every other file keeps the merge's own resolution unless S10 to S12 say otherwise. Observed
  by AC1.
- **S2** — `memory/project/readme-contract.txt` keeps every row from both sides: main's
  `aClearedLedger` and `aBriskDeclaration` rows, then this branch's `aLightenedLoop` row. Observed
  by AC2.
- **S3** — `memory/guides/SESSION-KICKOFF.md` takes one `last-audit` value, re-stamped at this
  branch's tip before the merge with a datetime later than both sides' stamps, as the manifest's
  stamp rule says. Observed by AC3.
- **S4** — `tools/template-size-limits.txt` keeps one `memory/guides/UNATTENDED-PROTOCOL.md` row,
  whose value is the merged render's measured bytes. Both sides' `RAISED` comment blocks stay above
  it, and one `MERGED` line names the figure. `memory/DECISIONS.md` gains this unit's row, as the
  file's four raise terms require. Observed by AC4.
- **S5** — `FLOOR_ASSERTIONS` in `tools/check-spec-tokens.test.sh` becomes 259. That is the common
  base's 247, plus main's 7, plus this branch's 5, each named on one `RECONCILED` comment line. Both
  sides' comment lines stay. Observed by AC5.
- **S6** — The start half. `init_spec_token_check` keeps main's three early decisions and its
  silence. After the launcher resolves, it derives the lookup key over the existing input record
  with unit 3's three-argument `derive_spec_token_key`, and skips on a match with the stored key.
  Otherwise it reads the tree state into a new global, `ST_TREE`, clears the earlier record with
  `rm -f`, and starts the checker with `SPEC_TOKENS_INPUTS` naming the record path, held in a new
  global, `ST_IN`. Observed by AC6, AC7, AC9 and AC11.
- **S7** — The read half. `run_spec_token_check` prints the cache-off line when `ST_TREE` was empty,
  not when the lookup key was. Its synchronous fallback arms the record as the start does. After an
  admitted verdict it runs unit 6's S3 block unchanged: it derives the key over the new record, then
  re-reads the tree state, and records the key only when the two states match and the record
  replays. Otherwise it prints the one not-recorded line, with the reason unit 3 and unit 6 print.
  Observed by AC6, AC7, AC8, AC10 and AC11.
- **S8** — What stays main's. The three refusals, their texts and order, the skip line, the
  admit-with-note line, `check_spec_token_hits`, `verb_dispatch`'s code and
  `remove_spec_token_check`'s wait-and-discard are byte-identical to `aebbb4a72`. The three reset
  lines name all seven globals. Observed by AC9 and AC11.
- **S9** — The comments. The block above `ST_STATE` states the merged design once: main's
  TOOL-aSmoothedDispatch-4 paragraph takes this branch's text, unit 3's S6 paragraph stays, and
  main's two-halves paragraph says what the start half now does, with "seven ST_ globals". One
  sentence of `verb_dispatch`'s window comment is rewritten. Observed by AC11.
- **S10** — The driver suite. `tools/unattended/unattended.test.sh` keeps main's A1 to A6 arms and
  this build's cache arms as merged, and gains one assertion after the cache arm's first admitted
  dispatch. `FLOOR_ASSERTIONS` and `FLOOR_SHARD_3` are summed and named: 3329 + 0 + 5 = 3334 and
  445 + 0 + 5 = 450 at the merge, then 3335 and 451 for the new assertion. Observed by AC12.
- **S11** — The other auto-merged files keep both sides' intent: the stop-guard, the kit gate's
  check-39 allow-list, the kit version markers, the shared read filter in the checker and the policy
  kit, and the three unattended renders, re-rendered with `bash tools/unattended/adopt-unattended.sh`.
  Observed by AC13.
- **S12** — The generated outputs are regenerated after the resolution. Observed by AC14.

## 3. Non-goals (OUT)

- No change to TOOL-aBriskDeclaration-1's behaviour beyond what the port needs: where the checker
  starts, what the start half prints, which refusals wait for it, and its refusal order.
- No change to unit 3's or unit 6's verdicts, their recorded-or-not conditions, their precedence or
  their line texts. No change to `derive_spec_token_key` or `read_tree_state` as the merge keeps
  them from this branch.
- No change to the checker, its tracer or `--input-key`. No change to `remove_spec_token_check`
  beyond its reset line.
- No edit to a CLOSED spec, ledger or review record on either side.
- No kit version bump by hand. The lander mints it.
- No landing or push. Those are the owner's.
- No conflict resolved outside the five files. A conflict elsewhere stops the pass (§4, Rollout).
- No help page. No `help/` page names the dispatch cache in the merged tree, and the verbs guide's
  paragraph merged cleanly with both sides' sentences.
- Nothing under `memory/builds/dDeclaredLoop/`.

### Edges

- **consumes-from** external — TOOL-aLightenedLoop-3's and TOOL-aLightenedLoop-6's built cache at
  `d9f84ee14`, and TOOL-aBriskDeclaration-1's split at `aebbb4a72`. All three specs are CLOSED, so
  this unit reads them and edits none.

## 4. Design

### Evidence

Read on 2026-11-15. "The trial merge" is `git merge-tree --write-tree HEAD origin/main` at
`d9f84ee14` and `aebbb4a72`, which wrote tree `dcafc6b82` and named the five conflicted files of
the brief. Its merge base is `846d51d39`.

- The trial merge's driver, `tools/unattended/unattended.sh@dabd3ef3331c`, conflicts twice: the
  header comment and the run body (`:14564-14665`), and the record write (`:14674-14685`). It keeps
  this branch's `derive_spec_token_key` in its three-argument form (`:14527`) and `read_tree_state`
  (`:14540`), because main never changed them from the base.
- Main's split, `tools/unattended/unattended.sh@eb567029d1d3`: five globals (`:14477`), the start
  half (`:14478`), which derives a two-argument key over the fingerprint and HEAD (`:14487`) and
  starts the checker with `init_bounded` (`:14496`); `remove_spec_token_check` (`:14501`); and the
  read half (`:14506`), which prints the cache-off line when that key is empty (`:14522`) and writes
  the key after any admit (`:14538-14540`). `verb_dispatch` starts the check at `:14828` and reads it
  at `:14907`. The comment at `:14823-14827` states that nothing in the window writes the tree.
- This branch's cache, `tools/unattended/unattended.sh@77c9dc8be702`: the lookup over the record
  (`:14571-14579`), the first tree-state read and the cache-off line (`:14581-14584`), the record
  cleared and armed (`:14585-14586`), and unit 6's derive-then-read block with its three reasons
  (`:14595-14615`).
- A temporary assignment ahead of a function call reaches a child that function starts in the
  background. Probed on 2026-11-15 under the bash the bar runs: `f(){ bash -c 'echo ${X-unset}' &
  wait; }; X=1 f` prints `1`. So `SPEC_TOKENS_INPUTS=$ST_IN init_bounded ...` arms the started
  checker, as unit 3's `SPEC_TOKENS_INPUTS=$_stin run_bounded ...` armed the synchronous one.
- `bash -x` traces such a call on two lines, the assignment and then `+ init_bounded ...`, probed on
  the same date. The A2 arm's pattern for the started checker
  (`tools/unattended/unattended.test.sh@9ca63646a8db:8043`) still matches.
- The suite pins two launcher spellings by grep: `run_bounded "$_stpy" "$SPEC_TOKENS_CLI"` (`:4478`)
  and the pair `^  ST_PY=$(resolve_python 2>/dev/null)` and `init_bounded "$ST_PY"
  "$SPEC_TOKENS_CLI"` (`:4482`). Neither pattern is anchored after its first token, so a prefixed
  assignment keeps both true.
- The merged suite's cache arms call `run_spec_token_check` with no start before it (`:7838-7922`),
  so each runs the two halves back to back. Main's A1 to A6 trace real `--dispatch` processes
  (`:8005-8076`). No arm asserts that a first admitted dispatch prints no cache-off line: the two
  `cache off` lines are both `hit`s (`:7919`, `:7921`).
- The driver suite's floors: `FLOOR_ASSERTIONS` is 3329 at `846d51d39` and at `aebbb4a72`, and 3334
  at `d9f84ee14`. `FLOOR_SHARD_3` is 445, 445 and 450. Main's A1 to A6 raised no floor.
- The checker suite's `FLOOR_ASSERTIONS` is 247 at `846d51d39`, 254 at `aebbb4a72` and 252 at
  `d9f84ee14`. Main's comment counts from 245, which was aClearedLedger's own base before it took
  `846d51d3`'s two TOOL-aBatchedPacket arms. 247 already holds them, so main's net is 7.
- The protocol render in the trial merge measures 68130 bytes CR-stripped, and its template is <!-- PINNED 2026-11-15 -->
  byte-identical to it. The rows were 68092 on main and 68216 here. The Skill render measures 10668 <!-- PINNED 2026-11-15 -->
  against its 10744 row, so no Skill row moves.
- The `read_open_py` block is byte-identical across `tools/lib/read_open.py`,
  `tools/check-spec-tokens.py` and `tools/policy/check_policy.py` in the trial merge. Both Python
  files parse, `node --check` passes the stop-guard, every unattended marker reads `1.123`, and the
  check-39 allow-list keeps `print_wake`
  (`tools/unattended/check-unattended.sh@05d50d8bfa95:6228`).

### The plain conflicts

- `memory/project/readme-contract.txt@421437428525:241-246`: the three rows, main's two first.
- `memory/guides/SESSION-KICKOFF.md@3c2608d67c75:6-10`: one line,
  `last-audit: <ISO datetime with offset> @ <full sha of the pre-merge tip>`.
- `tools/template-size-limits.txt@694bd875ef93:166-179`: both comment blocks in date order, main's
  first, then this line and one row:

```text
# MERGED at TOOL-aLightenedLoop-8's reconcile of origin/main, 2026-11-15: the render measures <N>
# CR-stripped, both raises above kept, and the row is that figure because this block's rule is no
# headroom. A run's raise, on the four terms above (memory/DECISIONS.md, TOOL-aLightenedLoop-8).
memory/guides/UNATTENDED-PROTOCOL.md	<N>
```

  `<N>` is measured after the re-render, with `tr -d '\r' | wc -c`. The DECISIONS row follows its
  two neighbours' shape:

```text
- **TOOL-aLightenedLoop-8** - **the reconcile of origin/main sets the no-headroom size row of `memory/guides/UNATTENDED-PROTOCOL.md` to the merged render's measured bytes**: agent, 2026-11-15, under TOOL-aOrientedCast-23's four raise terms; coexists-with TOOL-aClearedLedger-2 and TOOL-aLightenedLoop-2. Detail `builds/aLightenedLoop/`.
```

- `tools/check-spec-tokens.test.sh@b78125e195b9:88-99` keeps both sides' comment lines, then:

```text
# RECONCILED to 259 at TOOL-aLightenedLoop-8's merge of origin/main: the common base 247 at
# 846d51d39, plus main's 7 (TOOL-aClearedLedger-5 and -11), plus this branch's 5
# (TOOL-aLightenedLoop-3's four and -6's one). Summed, not counted.
FLOOR_ASSERTIONS=259
```

### The port

The block from the `TOOL-aSmoothedDispatch-4 S2-S4` comment line to the closing brace of
`run_spec_token_check` becomes the text below. The comment lines above it, `derive_spec_token_key`
and `read_tree_state` stay as merged. On 2026-11-15 this text, its placeholders filled from main
and unit 6, was spliced into a scratch copy of the trial merge. The probe below printed every line
§6 names, and four staged breaks each turned their line red: the cache-off test on `_stkey`, the
first tree-state read moved to the read half, the lookup's skip deleted, and the start's
`init_bounded` line deleted.

```bash
# TOOL-aSmoothedDispatch-4 S2-S4 - MOVED HERE from `verb_dispatch` with its refusal texts and its
# announced skip unchanged, then SCOPED and CACHED. It refuses only on a red `check_spec_token_hits`
# cannot prove foreign. A key is recorded only after the verdict admits, so a refusal re-runs every
# time. The key is one file per slug under the sidecar root, read with `read -r` and written with one
# `printf`; a failed read or write costs a later miss and never refuses.
#
# TOOL-aLightenedLoop-3 S6 - RE-KEYED on what the checker READ. <this branch's paragraph, unchanged>
#
# TWO HALVES, AS `init_bounded` AND `read_bounded` ARE (TOOL-aBriskDeclaration-1 S3, S4), the cache
# above carried onto them at the reconcile (TOOL-aLightenedLoop-8). The start half,
# `init_spec_token_check`, looks the key up over the record, reads the tree state and starts the
# checker with the record armed, all before the open-pass reader, so the two run side by side; it
# prints nothing and refuses nothing, and records what it decided in the seven ST_ globals. This read
# half prints every line and makes every refusal where the call always sat, from those globals, then
# derives the key over the new record and closes the bracket; it empties the globals so a later call
# in the same shell never reads them. The bracket so spans the window between the halves, and a write
# there costs a not-recorded line, never a wrong key. A checker discarded by a refusal in the window
# leaves its record behind, which the next lookup reads safely because the key folds the record's
# bytes. A direct call with no start before it runs the two back to back, as `run_bounded` does.
ST_STATE=""; ST_PY=""; ST_KEY=""; ST_REC=""; ST_IN=""; ST_TREE=""; ST_HANDLE=""
init_spec_token_check() { # slug -> the decision in ST_STATE, and under `run` the checker started; prints nothing
  local _stdir="" _stwas=""
  ST_STATE=""; ST_PY=""; ST_KEY=""; ST_REC=""; ST_IN=""; ST_TREE=""; ST_HANDLE=""
  if [ -z "${SPEC_TOKENS_CLI:-}" ]; then ST_STATE=blank; return 0; fi
  [ -f "$ROOT/$SPEC_TOKENS_CLI" ] || { ST_STATE=missing; return 0; }
  # <main's three SILENCED HERE comment lines, unchanged>
  ST_PY=$(resolve_python 2>/dev/null) || { ST_PY=""; ST_STATE=nopython; return 0; }
  _stdir=$(resolve_sidecar_dir) && [ -n "$_stdir" ] && ST_REC="$_stdir/spec-tokens.$1.key" && ST_IN="$_stdir/spec-tokens.$1.inputs"
  if [ -n "$ST_REC" ] && [ -f "$ST_REC" ] && [ -f "$ST_IN" ]; then
    read -r _stwas <"$ST_REC" || :
    ST_KEY=$(derive_spec_token_key "$1" "$ST_PY" "$ST_IN") || ST_KEY=""
    if [ -n "$ST_KEY" ] && [ "$_stwas" = "$ST_KEY" ]; then ST_STATE=skip; return 0; fi
  fi
  ST_TREE=$(read_tree_state "$ST_PY") || ST_TREE=""
  ST_STATE=run
  if [ -n "$ST_IN" ]; then rm -f "$ST_IN" 2>/dev/null; mkdir -p "$_stdir" 2>/dev/null; fi
  # <main's two "A start that cannot make its capture" comment lines, unchanged>
  SPEC_TOKENS_INPUTS=$ST_IN init_bounded "$ST_PY" "$SPEC_TOKENS_CLI" && ST_HANDLE=$RB_HANDLE
  return 0
}
# <main's two NO CHECKER OUTLIVES THE VERB UNREAD comment lines, unchanged>
remove_spec_token_check() { # -> a started checker waited for and its answer discarded; prints nothing
  [ -z "${ST_HANDLE:-}" ] || read_bounded "$ST_HANDLE" || :
  ST_STATE=""; ST_PY=""; ST_KEY=""; ST_REC=""; ST_IN=""; ST_TREE=""; ST_HANDLE=""
  return 0
}
run_spec_token_check() { # slug -> 0 admitted or skipped, 1 refused under check 49
  local slug="$1" _stst _stpy _stkey _strec _stin _stat _sth _strc _stq _stnow="" _stwhy=""
  [ -n "${ST_STATE:-}" ] || init_spec_token_check "$slug"
  _stst=$ST_STATE; _stpy=$ST_PY; _stkey=$ST_KEY; _strec=$ST_REC; _stin=$ST_IN; _stat=$ST_TREE; _sth=$ST_HANDLE
  ST_STATE=""; ST_PY=""; ST_KEY=""; ST_REC=""; ST_IN=""; ST_TREE=""; ST_HANDLE=""
  # <main's blank, missing, nopython and skip branches, byte for byte>
  if [ -z "$_stat" ]; then
    echo "unattended: dispatch — spec-token cache off: <main's text, unchanged>"
  fi
  if [ -n "$_sth" ]; then
    read_bounded "$_sth"; _strc=$?
  else
    SPEC_TOKENS_INPUTS=$_stin run_bounded "$_stpy" "$SPEC_TOKENS_CLI"; _strc=$?
  fi
  # <main's verdict: the check 49 refusal and the admit-with-note line, byte for byte>
  [ -n "$_stat" ] || return 0
  # <unit 6's S3 comment and block from `_stkey=""` to the not-recorded echo, byte for byte; its
  #  comment's "the lookup above" reads "the lookup", since the lookup is in the start half now>
  return 0
}
```

What each piece keeps:

| Piece | Kept from | Changed by the port |
|---|---|---|
| blank, missing, nopython decisions and their silence | main | none |
| lookup over the record, skip on a match | unit 3 | runs in the start half, into `ST_KEY` |
| first tree-state read | unit 3 | runs in the start half, into `ST_TREE` |
| record cleared, checker armed | unit 3 | `init_bounded` instead of `run_bounded` |
| cache-off line | unit 3's condition, main's place | tested on `_stat` in the read half |
| verdict, refusal, admit note | main | none |
| derive, second read, three reasons, write | unit 6 | none |
| wait and discard on a window refusal | main | reset line names seven globals |

The record path is held in `ST_IN` rather than re-derived from `ST_REC` in the read half, so the
file name is spelled once. The lookup key stays in `ST_KEY` only for the skip line's prefix, as in
main.

### The window comment in `verb_dispatch`

At `tools/unattended/unattended.sh@eb567029d1d3:14823-14827`, line 14823 stays and the four lines
after it, from "file and `git diff-tree`" to the end of the comment, become:

```text
# file and `git diff-tree`, the rest reads strings -- so the tree state the start half reads is the
# tree the checker reads. A write moved above the read (the claim, `park`, `stage_or_fail`), a `git
# status` added between, or a writer added to the reader would move the state the read half compares
# it with, so every dispatch would record no key and re-run the checker; the arm over the window's
# returns does not see it.
```

### The suite

- One line is added after `hit "$o" "dispatch declared"` that follows the cache arm's first
  admitted declared dispatch (`tools/unattended/unattended.test.sh@9ca63646a8db:7830`):
  `  miss "$o" "spec-token cache off"`. That dispatch runs the real checker with a fingerprint copied
  and no key yet, so the port's cache-off test is the only thing that can print the line there.
- `FLOOR_ASSERTIONS` keeps its comment lines and gains two above its value:

```text
# MERGED at TOOL-aLightenedLoop-8's reconcile of origin/main: the base 3329 at 846d51d39, plus main's
# 0 (TOOL-aBriskDeclaration-1 raised no floor), plus this branch's 5 (TOOL-aLightenedLoop-3) = 3334.
# RAISED 3334 -> 3335 by TOOL-aLightenedLoop-8: one region-three `miss`, no cache-off line on a first
# admitted dispatch, so FLOOR_SHARD_3 carries the same 1. Counted off the line; OWED: observed at the close.
FLOOR_ASSERTIONS=3335
```

- `FLOOR_SHARD_3` gains `# MERGED at TOOL-aLightenedLoop-8's reconcile: the base 445, plus main's
  0, plus this branch's 5 = 450.` and `# RAISED 450 -> 451 by TOOL-aLightenedLoop-8: the same 1
  region-three assertion, see FLOOR_ASSERTIONS.`, then `FLOOR_SHARD_3=451`.
- No other arm changes. Each cache arm and each A-arm says what it says against the merged driver,
  as the Evidence shows, and §7 declares the ones whose subject the port moved.

### The other auto-merged files

| File | Main's side | This branch's side | Check |
|---|---|---|---|
| `tools/unattended/stop-guard.js` | the version marker | unit 5's liveness cache | `node --check`, marker |
| `tools/unattended/check-unattended.sh` | the version marker | `print_wake` on the allow-list | the list line, marker |
| `tools/check-spec-tokens.py` | TOOL-aClearedLedger-5, -11 and -13 | unit 3's tracer, unit 6's pre-read | parse, the `--input-key` probe |
| `tools/policy/check_policy.py` | the recall plant's grammar file | unit 3's `read_open_py` block | parse, block parity |
| the unattended templates | aBriskDeclaration's verbs and protocol text | units 2, 3 and 7 | re-render, `--check`, `cmp` |

The renders are re-rendered with `bash tools/unattended/adopt-unattended.sh`, never edited by hand.

### The generated outputs

After every resolution and before the commit: `bash tools/run-gates/run-gates.sh --regen`, then
`python tools/memory-tree/gen_build_index.py --write`, then `python tools/codebase-map/gen_map.py
--write`. The merge commit carries their output.

### The probe, `$SCRATCH/l8.sh`

`$SCRATCH` is the run's scratch directory. The probe runs from the root of the worktree after the
merge is resolved, and builds a fixture repository at `$TEMP/l8`. It is unit 3's `l3.sh` with its
verdict stubs dropped and three switches added: `L8_TOUCH` edits a read file during the run,
`L8_RACE` edits it during the replay, and `L8_POPEN` writes an unreplayable record. `GW` passes
the checker's path to a Windows Python in its own spelling.

```bash
set -u
G=$(pwd); GW=$(cygpath -m "$G" 2>/dev/null || echo "$G"); R="$TEMP/l8"; rm -rf "$R"; mkdir -p "$R/tools/run-gates"; cd "$R" || exit 2
git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
cp "$G/.unattended.conf" "$G/.memory-tree.conf" . && cp "$G/tools/run-gates/gate-fingerprint.sh" tools/run-gates/
cat > stub.py <<EOF
import importlib.util, os, subprocess, sys
rec = os.environ.get("SPEC_TOKENS_INPUTS", "")
if os.environ.get("L8_POPEN"):
    os.environ.pop("SPEC_TOKENS_INPUTS", None)
if os.environ.get("L8_RACE") and "--input-key" in sys.argv:
    open("a.txt", "a").write("r\n")
s = importlib.util.spec_from_file_location("cst", r"$GW/tools/check-spec-tokens.py")
cst = importlib.util.module_from_spec(s); s.loader.exec_module(cst)
if "--input-key" in sys.argv:
    sys.exit(cst.main(sys.argv[1:]))
open("a.txt").read(); subprocess.run(["git", "ls-files"], capture_output=True)
if os.environ.get("L8_TOUCH"):
    open("a.txt", "a").write("t\n")
if os.environ.get("L8_POPEN") and rec:
    open(rec, "w").write('{"kind":"popen","argv":["x"]}\n')
open(os.environ["L8_LOG"], "a").write("r\n")
sys.stdout.write(open(os.environ["L8_OUT"]).read()); sys.exit(int(os.environ["L8_RC"]))
EOF
printf 'seed\n' > a.txt; printf 'seed\n' > b.txt; git add -A; git commit -qm seed
. "$G/tools/unattended/unattended.sh" || exit 2
load_driver_conf || exit 2
export L8_LOG="$R/.git/l8.log" L8_OUT="$R/.git/l8.out" L8_RC=0
: > "$L8_LOG"; : > "$L8_OUT"; SPEC_TOKENS_CLI=stub.py
runs() { local n; n=$(wc -l < "$L8_LOG"); echo "${n// /}"; }
sk() { grep -c 'spec-token check skipped' <<<"$1"; }
K="$(resolve_sidecar_dir)/spec-tokens.tA.key"
kf() { [ -f "$K" ] && echo written || echo none; }
o=$(run_spec_token_check tA)
echo "cache first runs $(runs) off $(grep -c 'spec-token cache off' <<<"$o") said $(grep -c 'not recorded' <<<"$o") key $(kf)"
o=$(run_spec_token_check tA); echo "cache unchanged runs $(runs) skipped $(sk "$o")"
printf 'e\n' >> b.txt; o=$(run_spec_token_check tA); echo "cache unread runs $(runs) skipped $(sk "$o")"
git commit -qam two; o=$(run_spec_token_check tA); echo "cache commit runs $(runs) skipped $(sk "$o")"
printf 'e\n' >> a.txt; o=$(run_spec_token_check tA); echo "cache edited runs $(runs) skipped $(sk "$o")"
printf 'm\n' >> a.txt
o=$(L8_TOUCH=1 run_spec_token_check tA); run_spec_token_check tA >/dev/null; p=$(run_spec_token_check tA)
echo "cache moved runs $(runs) said $(grep -c 'the tree or HEAD moved while the checker ran' <<<"$o") skipped $(sk "$p")"
rm -f "$K"; o=$(L8_RACE=1 run_spec_token_check tA)
echo "cache raced runs $(runs) said $(grep -c 'the tree or HEAD moved while the checker ran' <<<"$o") key $(kf)"
rm -f "$K"; o=$(L8_POPEN=1 run_spec_token_check tA)
echo "cache popen runs $(runs) said $(grep -c 'the input record cannot be replayed' <<<"$o") key $(kf)"
init_spec_token_check tA >"$R/.git/l8.start" 2>&1
st=$ST_STATE; i=0; while [ "$(runs)" -lt 7 ] && [ "$i" -lt 100 ]; do sleep 0.1; i=$((i + 1)); done; b=$(runs)
run_spec_token_check tA >"$R/.git/l8.read" 2>&1
echo "order state $st started $b after $(runs) start $(wc -c < "$R/.git/l8.start" | tr -d ' ') skipped $(grep -c 'spec-token check skipped' "$R/.git/l8.read") key $(kf)"
rm -f "$K" tools/run-gates/gate-fingerprint.sh
o=$(run_spec_token_check tA; run_spec_token_check tA)
echo "cache off runs $(runs) said $(grep -c 'spec-token cache off' <<<"$o") key $(kf)"
```

The order step calls both halves in the probe's own shell, not under a substitution, because
`read_bounded` waits on a child of the shell that started it. It waits up to ten seconds for the
started stub to log its run before it calls the read half. The raced and popen steps clear the key
file first, so the lookup does not call the stub and the run itself writes the record.

### What it does not check

- A write between the read half's second `read_tree_state` and its key write, as unit 6 states.
- That nothing in `verb_dispatch`'s window writes the tree. A write there now costs a miss on every
  dispatch rather than a wrong key, and no arm sees the miss.
- That `origin/main` still resolves to `aebbb4a72` when the pass starts. The Rollout says what the
  builder does when it does not.
- Whether the merge's other auto-merged hunks are right beyond S11's list. The bar and the closing
  review read the whole merge.

### Inventory

| identifier | kind | where |
|---|---|---|
| `ST_IN` | sh global, the input record path | `tools/unattended/unattended.sh` |
| `ST_TREE` | sh global, the tree state read at the start | `tools/unattended/unattended.sh` |

No function, flag, conf key or check number is minted. No declared lexicon cell grades a shell
global: `python tools/lexicon/lexicon.py --suggest ST_TREE --as sh.constant` names `sh.function` as
the only declared shell cell.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/check-spec-tokens.test.sh`
- `tools/template-size-limits.txt`
- `memory/project/readme-contract.txt`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/DECISIONS.md`
- `.claude/skills/unattended/SKILL.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `memory/map/generated/symbols.json`

The merge commit also carries every file main changed. The list above is what this unit resolves,
re-renders or regenerates by hand.

### Rollout

One pass at order 8, as one merge commit. Before merging, the builder runs `git fetch` and
`git rev-parse origin/main`. If that is not `aebbb4a725d58dd69b12f1f319e82f5b5d8a8e8e`, or the merge
conflicts in any file outside the five, the builder aborts the merge and returns, naming the new sha
or the file. The build's limitations stand: no push, and the lander alone moves kit versions.

### Alternatives rejected

- **Keep main's key.** It keys on HEAD and the fingerprint, so every commit misses, which is what
  unit 3 exists to fix. The owner chose the port.
- **Look up and run inside the read half.** It drops the overlap with the open-pass reader that
  TOOL-aBriskDeclaration-1 built, and its A2 arm reds.
- **Read the first tree state in the read half.** The checker has already run by then, so an edit
  it made mid-run would be recorded under the edited tree. The moved-tree probe step reds.
- **Re-derive the record path from `ST_REC`.** It spells the file name twice for one global saved.
- **Leave the reset lines at five globals.** `ST_TREE` would then outlive a call. Nothing reads it
  before `init_spec_token_check` resets it, but main's comment promises the globals are emptied.

## 5. Production-readiness checklist

- security — No new write path. The record and the key stay in the per-worktree sidecar root.
- perf / scale — The start half adds unit 3's lookup and one tree-state read before the reader
  starts, where main derived its fingerprint key. A hit now skips without starting the checker.
- error / empty / loading states — No fingerprint prints the cache-off line and records nothing. A
  failed capture runs the synchronous form, armed the same way. A refusal in the window leaves a
  record that a later lookup reads soundly.
- observability — The skip, cache-off and not-recorded lines keep their texts.
- risks — The port sits in a verb every unattended pass calls. The probe and the re-pointed arms
  observe it, and the closing review reads the merge.
- testing — The probe for the pass. §7's arms observed RED then GREEN, and the driver suite pooled
  and the bar, at the close.
- migration — None. A record or key left by either side's driver is read by the merged lookup or
  costs one miss.
- user docs — None owed. No `help/` page names the cache, and the verbs guide merged with both
  sides' sentences.

## 6. Acceptance criteria

Each `cache` and `order` line below comes from one run of `bash "$SCRATCH/l8.sh"`, §4's fenced
probe, run from the worktree root after the resolution and removed after the pass.

- **AC1** — When `git log --merges -1 --format=%P` runs after the merge commit, it prints two ids:
  the branch tip before the merge, then `aebbb4a725d58dd69b12f1f319e82f5b5d8a8e8e`.
  `git grep -n '^<<<<<<< '` prints nothing, and `bash -n tools/unattended/unattended.sh` exits 0.
  Red when: the merge is squashed or fast-forwarded, a marker survives, or the resolved driver does
  not parse.
- **AC2** — When `grep -cE '^memory/builds/a(ClearedLedger|BriskDeclaration|LightenedLoop)/README[.]md$' memory/project/readme-contract.txt`
  runs it prints 3, and `python tools/memory-tree/gen_build_index.py --check-format` exits 0.
  Red when: a side's row is lost or doubled.
- **AC3** — When `grep -c '^last-audit: ' memory/guides/SESSION-KICKOFF.md` runs it prints 1, the
  line's sha is the pre-merge tip, and its datetime is later than `2026-11-15T00:53:03+02:00`.
  `bash skills/session-kickoff/manifest-check.sh` reports no stale or non-ancestor `last-audit`.
  Red when: a side's stamp is kept as it was, or the stamp names a sha that is not an ancestor.
- **AC4** — When `awk -F'\t' '$1=="memory/guides/UNATTENDED-PROTOCOL.md"' tools/template-size-limits.txt`
  runs it prints one row, whose value equals what `tr -d '\r' < memory/guides/UNATTENDED-PROTOCOL.md | wc -c`
  prints. `grep -c 'by TOOL-aClearedLedger-2\|by TOOL-aLightenedLoop-2' tools/template-size-limits.txt`
  prints at least 2, and `grep -c '^- \*\*TOOL-aLightenedLoop-8\*\*' memory/DECISIONS.md` prints 1.
  Red when: one side's row or comment is dropped, the row differs from the render, or the raise has
  no DECISIONS row.
  figure: the value is DERIVED from the render; 68130 is PINNED at the trial merge, 2026-11-15.
- **AC5** — When `grep -c '^FLOOR_ASSERTIONS=259$' tools/check-spec-tokens.test.sh` runs it prints
  1, and `grep -c '^# RECONCILED to 259' tools/check-spec-tokens.test.sh` prints 1. The same
  file read with `git show` at `846d51d39`, at `aebbb4a72` and at the pre-merge tip, piped to
  `grep '^FLOOR_ASSERTIONS='`, prints 247, 254 and 252.
  Red when: one side's raise is lost, or the sum is taken over 245.
  figure: 259 is DERIVED as 247 + (254 - 247) + (252 - 247).
- **AC6** — When `bash "$SCRATCH/l8.sh"` runs, it prints `cache first runs 1 off 0 said 0 key written`,
  `cache unchanged runs 1 skipped 1`, `cache unread runs 1 skipped 1`, `cache commit runs 1 skipped 1`
  and `cache edited runs 2 skipped 0`.
  Red when: the start half keys on HEAD or the fingerprint again, so the unread or commit step
  re-runs; the lookup is not made, so nothing skips; or the cache-off line is tested on the lookup
  key, so the first line reads `off 1`.
- **AC7** — When `bash "$SCRATCH/l8.sh"` runs, it prints `cache moved runs 4 said 1 skipped 1` and
  `cache raced runs 5 said 1 key none`.
  Red when: `ST_TREE` is read in the read half after the checker ran, so the moved step records; or
  the read half derives the key after its second `read_tree_state`, so the raced step records.
- **AC8** — When `bash "$SCRATCH/l8.sh"` runs, it prints `cache popen runs 6 said 1 key none`.
  Red when: the replay branch is merged into the record branch, so an empty key is written or the
  line is lost.
- **AC9** — When `bash "$SCRATCH/l8.sh"` runs, it prints
  `order state run started 7 after 7 start 0 skipped 0 key written`.
  Red when: the start half no longer starts the checker, so `started` reads one less than `after`;
  it prints, so `start` is not 0; or the read half runs the checker again, so `after` reads 8.
- **AC10** — When `bash "$SCRATCH/l8.sh"` runs, it prints `cache off runs 9 said 2 key none`.
  Red when: a missing fingerprint does not turn the cache off, or a key is recorded without one.
- **AC11** — When `grep -c 'SPEC_TOKENS_INPUTS=\$ST_IN init_bounded "\$ST_PY" "\$SPEC_TOKENS_CLI"' tools/unattended/unattended.sh`
  runs it prints 1, and the same over `SPEC_TOKENS_INPUTS=\$_stin run_bounded "\$_stpy" "\$SPEC_TOKENS_CLI"`
  prints 1. `diff` over `verb_dispatch`'s non-comment lines, cut with
  `sed -n '/^verb_dispatch() {/,/^}$/p' | grep -v '^[[:space:]]*#'` from `aebbb4a72` and from the
  working tree, prints nothing; the same over `check_spec_token_hits` prints nothing; and over
  `remove_spec_token_check` it shows the reset line alone changed. `grep -cF` prints 1 for each of
  `spec-token check skipped: its inputs match the check last admitted for`,
  `spec-token cache off: no run-gates gate-fingerprint.sh resolves`,
  `spec-token cache not recorded: $_stwhy, so the next dispatch runs the checker`,
  `the tree or HEAD moved while the checker ran`, `the checker wrote no input record` and
  `the input record cannot be replayed`. `grep -c 'seven ST_ globals'` prints 1, and
  `grep -c 'five ST_ globals\|the key derived at the start describes'` prints 0.
  Red when: a call goes unarmed, main's code or refusal order moves, a line text moves, or a comment
  still states the old design.
- **AC12** — When `grep -c '^FLOOR_ASSERTIONS=3335$\|^FLOOR_SHARD_3=451$' tools/unattended/unattended.test.sh`
  runs it prints 2, and `grep -cxF '  miss "$o" "spec-token cache off"' tools/unattended/unattended.test.sh`
  prints 1. `grep -c 'INVERTED by TOOL-aLightenedLoop-3\|brisk A2: \|stub-raced.py\|stub-popen.py' tools/unattended/unattended.test.sh`
  prints the same count as over the trial merge's suite.
  Red when: a floor is not summed, the new assertion is missing, or an arm of either side is lost.
  figure: the trial-merge count is DERIVED by the same grep over the suite read with `git show`
  from tree `dcafc6b82`.
- **AC13** — When the `read_open_py` block is cut with
  `sed -n '/^# >>> read_open_py/,/^# <<< read_open_py/p'` from `tools/lib/read_open.py`,
  `tools/check-spec-tokens.py` and `tools/policy/check_policy.py`, the three cuts are equal under
  `cmp`. `python -c` with `ast.parse` over the two Python files exits 0, and
  `node --check tools/unattended/stop-guard.js` exits 0. The `PHASE_RECORDED_FNS=` line of
  `tools/unattended/check-unattended.sh` holds `print_wake`.
  `git grep -h -o 'gov:kit unattended@[0-9.]*' -- tools/unattended .claude/skills/unattended memory/guides | sort -u`
  prints one line. `bash tools/unattended/adopt-unattended.sh --check` exits 0, and
  `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` and
  `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md` print nothing.
  Red when: a side's change in one of these files is lost, or a render was not re-rendered.
- **AC14** — When `python tools/run-gates/regen.py --check`,
  `python tools/memory-tree/gen_build_index.py --check` and `python tools/codebase-map/gen_map.py --check`
  run after the merge commit, each exits 0.
  Red when: a generated output still holds one side's render.
  cost: about two minutes.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `unattended skill size` · `kickoff-manifest ratchet` · `build README slot contract` · `spec-tokens self-test` · `memory hygiene` · `codebase-map coverage + freshness` · `kit version markers` · `check-wiring self-test` · `lexicon naming predicates` · `policy fixtures` · `recall floor` · `recall floor arms` · `scratch-guard self-test` · `tier2-review self-test`

The first ten grade this unit's resolutions directly. The last seven are owed because a path of the
estimate trips their guard, by `python tools/check-spec-tokens.py --legs-for` at `d9f84ee14`, less
the broad guards. The driver suite runs in the unattended kit's pooled tier, so the main loop runs
it pooled, with the bar, at the close. No leg is added.

New arm: tools/unattended/unattended.test.sh · covers AC6 · unit 3's inverted steps a, b and c, re-pointed onto the start half's lookup; staged by deleting the lookup's `if` block from `init_spec_token_check`, so each step re-runs · none
New arm: tools/unattended/unattended.test.sh · covers AC6 · the new `miss` after the first admitted declared dispatch; staged with the read half's cache-off test reading `_stkey` in place of `_stat` · `FLOOR_ASSERTIONS` 3334 to 3335 and `FLOOR_SHARD_3` 450 to 451
New arm: tools/unattended/unattended.test.sh · covers AC7 · unit 3's moved-stub call, re-pointed onto the split bracket; staged with the `"$_stnow" != "$_stat"` test deleted from the read half's three-way choice · none
New arm: tools/unattended/unattended.test.sh · covers AC7 · unit 6's raced stub; staged with the read half's `derive_spec_token_key` moved below its second `read_tree_state` · none
New arm: tools/unattended/unattended.test.sh · covers AC8 · unit 6's popen stub; staged with the replay branch merged into the record branch, so an empty key is written · none
New arm: tools/unattended/unattended.test.sh · covers AC9 · TOOL-aBriskDeclaration-1's A2 trace arm against the armed start; staged with the start half's `init_bounded` line deleted, so the read half starts the checker after the reader · none

What these arms do not check: the moved-stub arm cannot tell where `ST_TREE` is read, because its
stub also edits the tree on its `--input-key` call; the probe's moved step pins that. The checker
suite's floor moves by the reconcile alone and adds no arm.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft from
  `prompts/2026-11-15-prompt-TOOL-aLightenedLoop-8-reconcile.md`, grounded at `d9f84ee14` and
  `aebbb4a72`. The resolved block and the probe were run on a scratch copy of the trial merge.

## 10. Reuse audit

The seams this unit extends are main's split, `tools/unattended/unattended.sh#init_spec_token_check`
and `tools/unattended/unattended.sh#run_spec_token_check`, and this branch's
`tools/unattended/unattended.sh#derive_spec_token_key` and
`tools/unattended/unattended.sh#read_tree_state`, kept as merged. The probe is unit 3's `l3.sh`
with three switches added. The arms are the merged suite's own, with one `miss` added beside them.
`python tools/codebase-map/reuse_lookup.py "carry an input-keyed check cache onto a started-then-read async check"`
ranked generic name stems only (`read_text`, `read`, `key`, `check`), so no other caching seam fits,
which matches unit 3's finding. Of the task's named seams, `check_staged_render`,
`check_index_input`, `runLiveness` and `DRIVER_STEPS` are not touched: the merge keeps both sides'
code there and the port does not reach them. Recall's nearest records were TOOL-aSmoothedDispatch-21,
an earlier reconcile of this same check that resolved it into one `run_spec_token_check`, and
PLAY-dOrderedCharter-83, a reconcile with origin/main that resolved each conflict by its kind; this
spec follows both in summing floors and naming each side's raise.

Recall terms used: `python tools/memory-recall/query.py "how was a spec-token cache reconciled with the split start and read halves of the dispatch check" --terms "reconcile merge origin/main init_spec_token_check run_spec_token_check input record stability bracket FLOOR_ASSERTIONS summed conflict"`
