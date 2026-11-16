# TOOL-aTrimmedWait-12 — the reconcile with local main at 5d48501da: its eight conflicts resolved so the landing merge is clean

**Status:** INPROGRESS · rev-1 · 2026-11-16 · node a · Tier-2 · base 5d48501da · streams tooling · order 11 · ratified 2026-11-16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-16-build-TOOL-aTrimmedWait-12-1-acceptance-ledger.md](../build/2026-11-16-build-TOOL-aTrimmedWait-12-1-acceptance-ledger.md) | journal | — |
| [2026-11-16-prompt-TOOL-aTrimmedWait-12-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-aTrimmedWait-12-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-aTrimmedWait-12-brief.md](../prompts/2026-11-16-prompt-TOOL-aTrimmedWait-12-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Merge local main at `5d48501da` into `branch/speedups-9c2e63` and resolve its eight conflicts, so the
landing merge of the branch onto local main is conflict-free
(`prompts/2026-11-16-prompt-TOOL-aTrimmedWait-12-1-spec-writer.md`). Both sides' changes stay as each
shipped them, except main's partition helper, which the owner ruled out on 2026-11-16. The one
design question is `cmd_write`, where main's render stamp and this branch's staged write meet in one
function, and §4 shows that no decline and no undo can leave a stamp behind.

## 2. Scope (IN)

- **S1** — The merge. `git merge --no-ff --no-commit 5d48501da` on the branch, committed once with
  both parents and no conflict marker. The eight conflicted files resolve by S2 to S9. Every other
  file keeps git's own merge result, apart from the generated outputs S11 re-renders and the one
  `memory/DECISIONS.md` row S4 adds. Observed by AC1 and AC11.
- **S2** — `memory/project/readme-contract.txt` keeps every row: main's four, then this branch's one.
  Observed by AC2.
- **S3** — `memory/guides/SESSION-KICKOFF.md`. §B is re-read against both sides' watched changes, and
  the conflict line becomes one fresh stamp at the pre-merge tip, by the stamp rule. One follow-up
  records commit after the merge re-stamps it at the merge itself, because check 5 of
  `manifest-check.sh` never finds a merge commit as its stamp commit (§4). Observed by AC3 and AC12.
- **S4** — `tools/template-size-limits.txt`, the `.claude/skills/unattended/SKILL.md` row. Main's
  comment block, then this branch's, then one `MERGED` comment naming the measure, then the row at
  the merged Skill's CR-stripped size, 10716. One `memory/DECISIONS.md` row records it, as the file's <!-- PINNED 2026-11-16 -->
  fourth raise term asks. Observed by AC4.
- **S5** — `tools/memory-tree/gen_build_index.py`, `cmd_write`: one function carrying both sides.
  It clears any stamp first, then makes this branch's staged decline, then reads main's
  `before` state and opens `written`. This branch's body follows: the view decline, the undo and
  its `finally`, the moved-only writes and the staging. Each of its two writes is recorded in
  `written`, so main's settled-tree check reads the render's own writes. Main's stamp is written
  after the verdicts, as main ships it. The selftest calls all three of `test_staged_write`,
  `test_write_moved` and `test_render_stamp`. Observed by AC5 and AC6.
- **S6** — `tools/memory-tree/check-memory-hygiene.test.sh`. The partition arm is this branch's,
  byte for byte: the `derive_partition_lines` compare, its `diff` and its fixture arm. Main's
  `extract_hs_lines` and its comment block are retired, by the owner's ruling of 2026-11-16.
  `FLOOR_ASSERTIONS` becomes 750, below both sides' comment lines and one `MERGED` comment.
  Observed by AC7.
  **Readers:** by name: `tools/memory-tree/check-memory-hygiene.test.sh`, main's side of which
  defines it and calls it twice, and `memory/map/generated/symbols.json`, which S11 re-renders.
  by value: the partition arm's compare and its `diff` at main's
  `tools/memory-tree/check-memory-hygiene.test.sh@4d3242279140` hunk, its only readers, which this
  branch's two lines stand in for.
- **S7** — `tools/unattended/unattended.sh`. The `verb_dispatch` hunk takes this branch's side, the
  order read taken from `check_unit_spec`. In `check_unit_spec`, the command substitution
  `_d_ord=$(order_verb_of "$_d_spec")` becomes main's no-fork form,
  `order_verb_of "$_d_spec" >/dev/null; _d_ord=$_order_verb`, so no order read forks. Observed by AC8.
- **S8** — `tools/unattended/unattended.test.sh`: `FLOOR_ASSERTIONS` becomes 3374, `FLOOR_SHARD_3`
  469 and `FLOOR_SHARD_4` 431. Each keeps every comment line of both sides and gains one `MERGED`
  comment naming its sum. Observed by AC9.
- **S9** — `tools/workflows/unattended-build.test.sh`: `FLOOR_ASSERTIONS` becomes 1051, the same way.
  Observed by AC10.
- **S10** — The auto-merged places where one side reads the other's old behaviour, in
  `gen_build_index.py`, `unattended.sh` and `check-memory-hygiene.sh` especially. One was found and
  S7 resolves it. The rest were checked and need no edit (§4, "Where one side reads the other").
  Observed by AC5, AC6 and AC8.
- **S11** — The generated outputs are regenerated after the resolution and committed in the merge.
  Observed by AC11.
- **S12** — The landing merge of the branch onto `5d48501da` reports no conflict, and the build
  index selftest passes on a frozen clone of the merge. Observed by AC12 and AC13.

## 3. Non-goals (OUT)

- No landing and no push. The main loop makes the landing merge after the bar, and the owner asked
  for no push.
- No kit version bump by hand. `push-main.sh` mints them at the push boundary.
- No behaviour change on either side beyond what a conflict or the owner's ruling forces. In
  particular, the stamp a successful `--write-staged` may write is main's rule and stays (§4).
- No edit to `order_verb_of` or its comment. §4 shows the comment still holds.
- No new suite arm, and no arm of either side edited or moved, apart from main's partition compare
  that S6 sets aside.
- No edit to a CLOSED spec, ledger or review record on either side.
- No self-test suite and no bar inside the pass, a sliced suite included.
- No conflict resolved outside the eight files. A ninth conflict stops the pass (§4, Rollout).

### Edges

- **consumes-from** external — local main at `5d48501da`, aTwinnedPass's landing, and this branch's
  CLOSED units 1 to 11 at `766048903`. This unit reads their specs and edits none.
- **hands-off** external — the landing merge onto local main, the merge bar and the three suites'
  self-tests at the close, all the main loop's.

## 4. Design

### Evidence

Read on 2026-11-16. "The trial merge" is `git merge-tree --write-tree HEAD 5d48501da` at
`766048903`. It wrote tree `2a894b2fe` and named the brief's eight conflicted files. Its merge base
is `846d51d39`, this build's own base.

- The floors, read with `git show` at base, main and the branch tip. In
  `tools/unattended/unattended.test.sh`, `FLOOR_ASSERTIONS` is 3329, 3348 and 3355, `FLOOR_SHARD_3` <!-- PINNED 2026-11-16 -->
  is 445, 451 and 463, and `FLOOR_SHARD_4` is 410, 423 and 418. In <!-- PINNED 2026-11-16 -->
  `tools/workflows/unattended-build.test.sh`, `FLOOR_ASSERTIONS` is 950, 1043 and 958. In <!-- PINNED 2026-11-16 -->
  `tools/memory-tree/check-memory-hygiene.test.sh` it is 707, 708 and 749.
- Each side's raise comments name its parts. In the driver suite, main's 19 are <!-- PINNED 2026-11-16 -->
  TOOL-aLightenedLoop-3's 5 and -8's 1 in region three, and TOOL-aTwinnedPass-3's 10 and -5's 3 in
  region four. This branch's 26 are TOOL-aTrimmedWait-1's 18 in region three and -5's 5 and 3 in
  region four. In the workflow suite, main's 93 are TOOL-aLightenedLoop-3's 4 and TOOL-aTwinnedPass-1's <!-- PINNED 2026-11-16 -->
  50, -4's 28 and -11's 11, and this branch's 8 are TOOL-aTrimmedWait-1's. In the hygiene suite,
  main's 1 is TOOL-aClearedLedger-6's, and this branch's 42 are TOOL-aTrimmedWait-2's 38 and -11's 4.
- The trial driver suite's region ends are its `fi   # ---- end REGION` lines. Main's LL8 and LL3
  markers and this branch's TW1 marker fall in region three, and main's TP3 and this branch's TW5
  markers in region four, so each shard floor still counts its own side's raise.
- Main's partition helper and its two calls are
  `tools/memory-tree/check-memory-hygiene.test.sh@4d3242279140:1398-1411` in the trial. At main they
  are `:1307-1309`, below a four-line comment block. Main's helper folds only the `cache hits` count.
  This branch's `derive_partition_lines` also sets aside the `cache recomputed` lines, so it covers
  everything main's does. Both compares carry one `n=$((n+1))`, so the choice moves no floor.
- `gen_build_index.py`'s three hunks are `tools/memory-tree/gen_build_index.py@88ec0e93c0e0:3421-3444`
  (the `def` and each side's opening), `:3455-3537` (each side's write block) and `:9233-9238` (the
  selftest calls). Git merged main's `rc = print_verdicts(...)` and its stamp write after the
  verdicts into the tail on its own.
- Main's stamp: `resolve_render_stamp` (`:1258`), `check_render_settled` (`:1228-1255`), and
  `write_text` leaving identical bytes alone (`:298-310`). `check_render_settled` drops each path in
  `written` or `orphans` from both reads, then requires each written path to still hold its bytes.
  A write left out of `written` therefore withholds the stamp, which is what AC6's `write` line reads.
- This branch's staged mode returns or raises inside its `try` on every decline and on a refused
  `git add`. Its `finally` puts back each recorded path. The stamp write sits after the `try`, so no
  decline and no undo reaches it.
- `check_unit_spec` reads the order through a command substitution
  (`tools/unattended/unattended.sh@7efec1c489e7:14716`). Main's TOOL-aBriskDeclaration-1 made both
  of `verb_dispatch`'s order reads fork-free, and main's arm `brisk A1: no order verb is read through
  a substitution` counts `++ order_verb_of` lines in a traced dispatch
  (`tools/unattended/unattended.test.sh@24f12f1e396f:8043`). This branch's read would red it.
- After S7, `order_verb_of` has two call sites, `check_unit_spec` and the sibling loop in
  `verb_dispatch`. Both send stdout to `/dev/null`, as the function's comment says (`:4854`).
- In the trial `verb_dispatch`, `check_unit_spec` (`:14796`) and `check_edge_shape` (`:14901`) both
  run before `init_spec_token_check` (`:15046`). Main's window comment says every refusal above the
  start returns with no checker started, and both of this branch's lifted refusals keep that true.
- Main changed `tools/memory-tree/check-memory-hygiene.sh` only at its version marker line.
- `check_staged_render`: this branch moved its pathspec into `build_render_pathspec`, and main added
  the admitted build records. The two edits touch disjoint lines and neither reads the other.
- The hook's second hygiene run after `--write-staged` may now be answered by main's stamp. That is
  sound: the stamp keys the worktree the full `--check` grades, and `check_staged_write` has already
  required no unstaged change under the render's pathspec.
- This branch's §B bullet says a refused check 9 on a branch is cleared with `--write` and a hand
  stage. Main's stamp answers `--check --staged` after exactly that, so the bullet stays true.
- Main's watched changes since `846d51d39` are a kit marker in `memory/guides/BUILD-METHOD.md`, a
  refusal clause in `tools/check-template-size.sh`, the policy fixtures leg's guard list in
  `tools/gate-legs.json`, and the hygiene script's version marker. §B reads the leg list from the
  manifest and the size margin from the script and names neither, so the delta is none.
- `manifest-check.sh` check 5 (`skills/session-kickoff/manifest-check.sh@4d3d63c0fad1:1835-1861`)
  finds its stamp commit with `git log -G'^last-audit:'`. Under git 2.54 that never lists a merge:
  `git log --merges -G'^last-audit:' 5d48501da` printed nothing, while eight merges there moved the
  stamp. The merged `check-memory-hygiene.sh` differs from both parents, so the merge is the newest
  watched commit. Replayed at the precedent reconcile `31ecac0f5`, check 5 found the merge as its
  newest watched commit and a stamp commit not after it. Follow-up `0ea0b59f6` re-stamped at the
  merge. The staged leg (`:1973-1988`) separately requires the merge's staged stamp to differ from
  `HEAD`'s.
- The size file reserves a lowering to the owner (`tools/template-size-limits.txt`, main's `:24`).
  10716 is a raise over this branch's 10628 and sits below main's 10744. TOOL-aLightenedLoop-8's <!-- PINNED 2026-11-16 -->
  reconcile set the protocol row the same way, to 68130 between its sides' 68092 and 68216, with a
  `MERGED` comment and its own `memory/DECISIONS.md` row.
- In the trial, the Skill measures 10716 bytes CR-stripped, main's 10668 plus this branch's 48. <!-- PINNED 2026-11-16 -->
  The protocol render measures 68130, equal to its row, and `memory/guides/UNATTENDED-VERBS.md` and
  the protocol are the same blobs as their templates.
- No `RUN.md` exists under `memory/builds/aTrimmedWait/`, so this is an attended pass.

### The resolutions

Each conflict hunk resolves to the text below. Main's side goes first wherever both sides' lines
stay. `MERGED` comments follow every comment line of both sides and sit directly above the value.

- `memory/project/readme-contract.txt`: main's four rows, from `aClearedLedger` to `aTwinnedPass`,
  then `memory/builds/aTrimmedWait/README.md`.
- `memory/guides/SESSION-KICKOFF.md`: `last-audit: <ISO-8601 now, offset +02:00> @ <git rev-parse HEAD>`.
  The datetime is later than both sides' `2026-11-15T15:05:35+02:00`, and `HEAD` is the pre-merge tip.
- `tools/template-size-limits.txt`: main's four-line `RAISED 10580 -> 10744` block, this branch's
  four-line `RAISED 10580 -> 10628` block, then:

```text
# MERGED at TOOL-aTrimmedWait-12's reconcile of local main at 5d48501da, 2026-11-16: the render measures 10716
# CR-stripped, both raises above kept, and the row is that figure, with no headroom. A run's raise,
# on the four terms above (memory/DECISIONS.md, TOOL-aTrimmedWait-12).
.claude/skills/unattended/SKILL.md	10716
```

- `memory/DECISIONS.md`, appended after the TOOL-aLightenedLoop-8 row:

```text
- **TOOL-aTrimmedWait-12** - **the reconcile of local main sets the no-headroom size row of `.claude/skills/unattended/SKILL.md` to the merged render's measured bytes**: agent, 2026-11-16, under TOOL-aOrientedCast-23's four raise terms; coexists-with TOOL-aTrimmedWait-1 and TOOL-aLightenedLoop-2. Detail `builds/aTrimmedWait/`.
```

- `tools/memory-tree/gen_build_index.py`, the first two hunks, in this order: this branch's `def`
  line with `staged`; main's four stamp lines and their comment; this branch's comment and
  `if staged:` decline; main's `before` and `written` lines and their comment. Then this branch's
  whole second-hunk side, with `written[view["rel"]] = view["text"]` after the view's `write_text` and
  `written[rel] = text` after each artifact's. Main's second-hunk side does not survive, because this
  branch's moved-only writes are its successor. The third hunk keeps all three calls, this branch's
  two then main's.
- `tools/memory-tree/check-memory-hygiene.test.sh`: the first hunk takes this branch's side whole.
  The second keeps main's three `RAISED 707 -> 708` lines and this branch's four, then:

```text
# MERGED at TOOL-aTrimmedWait-12's reconcile of local main at 5d48501da: the base 707 at 846d51d39, plus main's 1
# (TOOL-aClearedLedger-6), plus this branch's 42 (TOOL-aTrimmedWait-2's 38 and -11's 4) = 750.
# Counted by reading; OWED: observed at the close.
FLOOR_ASSERTIONS=750
```

- `tools/unattended/unattended.sh`: the hunk takes this branch's side, and the one line in
  `check_unit_spec` takes main's form, as S7 states.
- `tools/unattended/unattended.test.sh`, one `MERGED` comment per floor:

```text
# MERGED at TOOL-aTrimmedWait-12's reconcile of local main at 5d48501da: the base 3329 at 846d51d39, plus main's 19
# (TOOL-aLightenedLoop-3's 5 and -8's 1, TOOL-aTwinnedPass-3's 10 and -5's 3), plus this branch's 26
# (TOOL-aTrimmedWait-1's 18 and -5's 8) = 3374.
FLOOR_ASSERTIONS=3374
# MERGED at TOOL-aTrimmedWait-12's reconcile of local main at 5d48501da: the base 445, plus main's 6, plus this branch's 18 = 469.
FLOOR_SHARD_3=469
# MERGED at TOOL-aTrimmedWait-12's reconcile of local main at 5d48501da: the base 410, plus main's 13, plus this branch's 8 = 431.
FLOOR_SHARD_4=431
```

- `tools/workflows/unattended-build.test.sh`:

```text
# MERGED at TOOL-aTrimmedWait-12's reconcile of local main at 5d48501da: the base 950 at 846d51d39, plus main's 93
# (TOOL-aLightenedLoop-3's 4, TOOL-aTwinnedPass-1's 50, -4's 28 and -11's 11), plus this branch's 8 (TOOL-aTrimmedWait-1) = 1051.
FLOOR_ASSERTIONS=1051
```

On 2026-11-16 all eight resolutions were applied to the trial merge's files in the scratch
directory. `bash -n` passed on the four shell files, `py_compile` on the generator, and both probes
below printed every line §6 names.

### Where one side reads the other

- **The order read forks.** This branch's `check_unit_spec` keeps the command substitution main
  removed, and main's `brisk A1` arm reds on it. S7 resolves it.
- **The stamp and the staged write.** Clearing the stamp first means every decline, the policy
  switch's included, leaves none. Every undo leaves the function before the stamp write. A staged
  render that lands may write a stamp by main's rule: the tree was settled, and the stamp keys the
  worktree and `HEAD`, which the commit then moves. `before` is read after the staged decline, so a
  declined hook run pays no state read.
- **The moved-only writes and `write_text`.** Main skips identical bytes inside `write_text` and this
  branch writes only moved artifacts. Both leave an unchanged file alone, so `test_write_moved`'s
  mtime arms and main's AC1 hold together. The merged print is this branch's
  `wrote <n> artifact(s), <m> unchanged`. No reader in either side's tree anchors main's shorter line.
- **Checked, no edit.** The window comment, the `order_verb_of` comment, `check_staged_render`, the
  hook's second run, the §B bullet and the hygiene script, each as the Evidence states.

### The probes

`$SCRATCH` is the run's scratch directory. Both probes run from the worktree root after the
resolution and before the commit. While the merge is in progress `HEAD` is the pre-merge tip and
`MERGE_HEAD` is `5d48501da`. `bash "$SCRATCH/t12.sh" HEAD MERGE_HEAD` reads the resolved files:

```bash
set -u
O=$1; M=$2; D=${3:-.}; B=$(git merge-base "$O" "$M")
R='^[[:space:]]*(hit|miss|same|mutate|has|hasnt_|hasnt|n=\$\(\(n\+1\)\))[[:space:]]'
for p in tools/unattended/unattended.test.sh tools/workflows/unattended-build.test.sh; do
  b=$(git show "$B:$p" | grep -cE "$R"); m=$(git show "$M:$p" | grep -cE "$R")
  o=$(git show "$O:$p" | grep -cE "$R"); r=$(grep -cE "$R" "$D/$p")
  echo "counts ${p##*/} merged $r expect $((m + o - b))"
done
H=tools/memory-tree/check-memory-hygiene.test.sh
hc() { grep -o 'n=$((n+1))' | wc -l | tr -d ' '; }
echo "counts ${H##*/} merged $(hc < "$D/$H") expect $(( $(git show "$M:$H" | hc) + $(git show "$O:$H" | hc) - $(git show "$B:$H" | hc) ))"
region() { awk -v pat="$1" -v label="$2" 'index($0, pat) && !f { print "region " r + 1 " " label; f = 1 } /^fi   # ---- end REGION/ { r++ }' "$D/tools/unattended/unattended.test.sh"; }
region '  miss "$o" "spec-token cache off"' main-LL8
region '# TOOL-aLightenedLoop-3 AC9:' main-LL3
region '# ---- TOOL-aTrimmedWait-1 - `--check-specs`' ours-TW1
region '# ---- TOOL-aTwinnedPass-3: CONDITION 1' main-TP3
region '# ---- TOOL-aTrimmedWait-5 - ONE GIT CALL' ours-TW5
U=tools/unattended/unattended.sh
fn() { sed -n "/^$1() {/,/^}/p" "$D/$U"; }
echo "order forks $(grep -c '\$(order_verb_of' "$D/$U") check_unit_spec $(fn check_unit_spec | grep -cxF '  order_verb_of "$_d_spec" >/dev/null; _d_ord=$_order_verb') verb_dispatch $(fn verb_dispatch | grep -cxF '  _d_ord=$_cu_ord')"
fn verb_dispatch | awk '/check_unit_spec "\$unit"/ && !a { a = NR } /check_edge_shape / && !e { e = NR } /init_spec_token_check "\$slug"/ && !i { i = NR } END { print "window", (a && e && i && a < i && e < i) ? "refusals-before-start" : "misordered" }'
arm() { awk '/^derive_partition_lines\(\) \{/ { f = 1 } f { print } f && /grep -qF .HYGIENE --only. <<<"\$out"/ { exit }'; }
cmp -s <(git show "$O:$H" | arm) <(arm < "$D/$H") && [ "$(arm < "$D/$H" | wc -l)" -gt 3 ] && p=ours || p=differs
echo "partition $p main-helper $(grep -c 'extract_hs_lines' "$D/$H")"
G=tools/memory-tree/gen_build_index.py
cw() { sed -n '/^def cmd_write(/,/^# -* selftest$/p'; }
echo "cw lost ours $(diff <(git show "$O:$G" | cw) <(cw < "$D/$G") | grep -c '^<') main $(diff <(git show "$M:$G" | cw) <(cw < "$D/$G") | grep -c '^<')"
cw < "$D/$G" | awk '/stamp = resolve_render_stamp\(root\)/ && !s { s = NR } /^    if staged:$/ && !d { d = NR } /before = read_render_state\(root\) if stamp else None/ && !b { b = NR } END { print "cw order", (s && d && b && s < d && d < b) ? "stamp-decline-before" : "misordered" }'
echo "cw written $(cw < "$D/$G" | grep -cE '^ +written\[(view\["rel"\]|rel)\] = ') selftest $(grep -cxE '    test_(staged_write|write_moved|render_stamp)\(arm\)' "$D/$G")"
echo "skill measured $(tr -d '\r' < "$D/.claude/skills/unattended/SKILL.md" | wc -c | tr -d ' ') row $(awk -F'\t' '$1 == ".claude/skills/unattended/SKILL.md" { print $2 }' "$D/tools/template-size-limits.txt")"
```

The `counts` lines compare each merged suite's assertion sites with main's plus this branch's less
the base's, so an arm the merge lost or doubled shows. The `region` lines name the region each
side's first marker falls in. `cw lost` counts the lines of each side's `cmd_write` the merge does
not carry: this branch's one is `print_verdicts(...)`, which main's `rc = ` form stands in for, and
main's 14 are its `def` line and its unconditional write block. <!-- PINNED 2026-11-16 -->

`python -I "$SCRATCH/t12-stamp.py" tools/memory-tree` drives the merged generator over its own
`_fixture`, with a stamp planted before each `--write-staged`:

```python
import os, subprocess, sys, tempfile
sys.path.insert(0, sys.argv[1])
import gen_build_index as g
gbi = os.path.join(sys.argv[1], "gen_build_index.py")
spec = "memory/builds/tOne/spec/2026-08-01-spec-tOne-1.md"
with tempfile.TemporaryDirectory() as base:
    t = os.path.join(base, "s"); os.makedirs(t)
    g._fixture(t)
    landed = {"GOV_DEFAULT_BRANCH": g.run("git", "symbolic-ref", "--short", "HEAD", cwd=t).strip(), "GOV_REMOTE": ""}
    g.write_text(os.path.join(t, ".governance", "policy.toml"), '[memory]\nstaged-render = "on"\n')
    g.run(sys.executable, gbi, "--write", cwd=t)
    g.run("git", "add", "-A", cwd=t)
    g.run("git", "commit", "-q", "-m", "rendered", "--no-verify", cwd=t)
    stamp = g.resolve_render_stamp(t)

    def flip_spec():
        g.run("git", "reset", "-q", "--hard", cwd=t)
        sp = os.path.join(t, spec)
        g.write_text(sp, g.read_text(sp).replace("INPROGRESS", "DEFERRED"))
        g.run("git", "add", spec, cwd=t)

    def run_case(label, mode, branch=None, lock=False):
        flip_spec()
        g.write_text(stamp, "planted\n")
        lk = os.path.join(t, ".git", "index.lock")
        if lock:
            open(lk, "w").close()
        env = dict(g._build_git_env(), **dict(landed, GOV_DEFAULT_BRANCH=branch or landed["GOV_DEFAULT_BRANCH"]))
        p = subprocess.run([sys.executable, gbi, mode], cwd=t, capture_output=True, text=True, encoding="utf-8", env=env)
        if lock:
            os.remove(lk)
        print(f"stamp {label} rc={p.returncode} left={os.path.exists(stamp)}")

    run_case("decline", "--write-staged", branch="no-such-branch")
    run_case("undo", "--write-staged", lock=True)
    run_case("landed", "--write-staged")
    run_case("write", "--write")
```

`decline` is a switch that does not read at a missing landed branch. `undo` is a refused `git add`
under an empty `index.lock`, so the undo puts the README back. `landed` stages the render, and
`write` is a plain render of the flipped spec. On 2026-11-16, staged breaks turned each kind red:
one TW1 `hit` deleted, the fork restored in `check_unit_spec`, main's compare taken, the stamp
clearing moved below the staged decline (`decline` read `left=True`), and `written[rel] = text`
deleted (`write` and `landed` read `left=False`).

### The generated outputs

After the resolutions and `git add` of each file, run in order:

```bash
python tools/run-gates/regen.py --write
git add -A
python tools/memory-tree/gen_build_index.py --write
python tools/codebase-map/gen_map.py --write
git add -A
```

`memory/LIVE.md` carries `merge=ours`, and the ledger shard and `memory/map/generated/symbols.json`
auto-merged. The writes above re-render all three, and `symbols.json` loses its `extract_hs_lines`
entry. Before the commit, `git status --porcelain` shows no `??` line. An untracked path stops the
pass and is named.

### What it does not check

- That each suite executes at least its new floor. 3374, 469, 431, 1051 and 750 are DERIVED sums.
  They are first observed when the suites run at the close, on the main loop's frozen clone.
- That the merged assertion counts are right inside a block. The `counts` lines catch a lost or
  doubled line, not a wrong one.
- That the regions hold any arm other than the five markers.
- That the view's `written` entry is right. AC6 reds on an artifact's missing entry only, because
  the fixture arms no view.
- That every auto-merged hunk outside the eight files is right. AC11 shows the commit kept git's
  result there, and the bar and any closing review read the whole merge.
- That a stamp a landed staged render writes is ever read. AC6's `landed` line shows it may exist.

### Inventory

No identifier is minted: no function, flag, conf key, check number or global. The `MERGED` comments
and the `memory/DECISIONS.md` row are prose.

### Files touched (estimate)

- `memory/guides/SESSION-KICKOFF.md`
- `memory/project/readme-contract.txt`
- `memory/DECISIONS.md`
- `tools/template-size-limits.txt`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/workflows/unattended-build.test.sh`
- `memory/map/generated/symbols.json`
- `memory/LIVE.md`
- `memory/ledger/2026-11.md`
- `memory/builds/aTrimmedWait/build/2026-11-16-build-TOOL-aTrimmedWait-12-1-acceptance-ledger.md`

The merge commit also carries every file main changed. The list above is what this unit resolves,
regenerates or writes by hand.

### Rollout

One pass at order 11, in the branch's own worktree. The card must route to this unit with its spec
INPROGRESS before the pass, or the scratch-guard refuses the resolution.

1. `git rev-parse main` must print `5d48501da9e5e07b0796bd935aaf4eae8cd4b804`. If it prints anything
   else, stop and return the new sha.
2. `git merge --no-ff --no-commit 5d48501da`. If `git diff --name-only --diff-filter=U` names any
   file outside the eight, run `git merge --abort` and return naming it.
3. Resolve the eight as above, add the `memory/DECISIONS.md` row, regenerate, run both probes and
   the checks of §6, and write the acceptance ledger.
4. Commit once with both parents. The body names the eight resolutions and carries
   `manifest-audit: delta none · watch-commits-since-stamp: <n>`, `n` being
   `git rev-list --count HEAD..MERGE_HEAD -- <watch>` read before the commit. It ends with
   `Pass: TOOL-aTrimmedWait-12` and the commit trailer. No `--no-verify`: a hook refusal is
   returned, not bypassed.
5. One records commit re-stamps `last-audit` at the merge commit's full sha, with a later datetime and
   the same delta line, `n` counted from the merge's stamp to `HEAD`.
6. The status flip to CLOSED is the pass's last change, a status-only commit.

### Alternatives rejected

- **Keep main's `extract_hs_lines`.** The owner ruled for this branch's helper on 2026-11-16, and
  main's leaves the `cache recomputed` lines in the compare.
- **Main's `cmd_write` order, the stamp clearing then `before` then the decline.** A declined hook
  run would pay four git calls for a state nobody reads.
- **The decline before the stamp clearing.** A planted stamp survives the decline, which AC6 reds on.
- **Keep main's row at 10744.** The block's rule is no headroom, and the precedent merge set its row to
  the measure.
- **Re-stamp only at the merge.** Check 5 never reads a merge as its stamp commit, so the full leg
  reds at the close, as it would have at `31ecac0f5` without `0ea0b59f6`.

## 5. Production-readiness checklist

- security — No new write path, surface or grant. The stamp lives under the git directory as before.
- perf / scale — The staged decline reads no render state, as before the merge.
- error / empty / loading states — A moved main or a ninth conflict stops the pass before anything
  is committed (Rollout).
- observability — The commit bodies, the `MERGED` comments and the `memory/DECISIONS.md` row name
  every figure.
- risks — A floor sum wrong by a miscount reds its suite at the close. The size row sits below main's,
  a lowering the size file reserves to the owner. The owner's merge order, the precedent at
  TOOL-aLightenedLoop-8 and the no-headroom rule carry it, and the `memory/DECISIONS.md` row records it.
- testing — The two probes and the direct checks in the pass. The bar, the three suites and the
  build index selftest at the close, the main loop's.
- migration — None.
- user docs — None owed. No user-facing behaviour changes, and S10 found no doc to correct.

## 6. Acceptance criteria

Each `counts`, `region`, `order`, `window`, `partition`, `cw` and `skill` line comes from one run of
`bash "$SCRATCH/t12.sh" HEAD MERGE_HEAD`, and each `stamp` line from one run of
`python -I "$SCRATCH/t12-stamp.py" tools/memory-tree`. Both run after the resolution and before the
commit.

- **AC1** — Before the commit, `git rev-parse MERGE_HEAD` prints
  `5d48501da9e5e07b0796bd935aaf4eae8cd4b804`, and both `git diff --name-only --diff-filter=U` and
  `git grep -n '^<<<<<<< '` print nothing. After it, the merge is `git rev-list --merges -n 1 HEAD`,
  and `git rev-list --parents -n 1` over it prints three ids: the merge, the pre-merge tip, then
  `5d48501da9e5e07b0796bd935aaf4eae8cd4b804`.
  Red when: the merge is squashed or fast-forwarded, or a marker or unmerged path survives.
  permission: the after-commit half is the main loop's, recorded with the close's observations,
  because the ledger is committed in the merge.
- **AC2** — When `grep -nE '^memory/builds/a(ClearedLedger|BriskDeclaration|LightenedLoop|TwinnedPass|TrimmedWait)/README[.]md$' memory/project/readme-contract.txt`
  runs, it prints five lines on consecutive line numbers in that order, and
  `python tools/memory-tree/gen_build_index.py --check-format` exits 0.
  Red when: a side's row is lost, doubled or out of order.
- **AC3** — When `git diff --cached -U0 -- memory/guides/SESSION-KICKOFF.md` runs it prints one
  `+last-audit:` line, ending `@ ` and the full `git rev-parse HEAD`, with a datetime later than
  `2026-11-15T15:05:35+02:00`, and no other `+` or `-` content line.
  Red when: the stamp keeps either side's value, names another sha, or the merge moves §B.
- **AC4** — When the probe runs it prints `skill measured 10716 row 10716`.
  `grep -cE 'RAISED 10580 -> 10744, 2026-11-14|RAISED 10580 -> 10628, 2026-11-14|^# MERGED at TOOL-aTrimmedWait-12' tools/template-size-limits.txt`
  prints 3, and `grep -c '^- \*\*TOOL-aTrimmedWait-12\*\* - ' memory/DECISIONS.md` prints 1.
  Red when: the row is either side's value, a side's comment is lost, or the raise goes unrecorded.
  figure: 10716 is DERIVED by the probe's `tr -d '\r' | wc -c` over the merged Skill.
- **AC5** — When `python -m py_compile tools/memory-tree/gen_build_index.py` runs it exits 0, and the
  probe prints `cw lost ours 1 main 14`, `cw order stamp-decline-before` and
  `cw written 2 selftest 3`.
  Red when: either side's body loses a line beyond those named, the stamp clearing or `before` moves,
  a write goes unrecorded, or a selftest call is lost.
  figure: 1 and 14 are PINNED, measured on the scratch resolution on 2026-11-16.
- **AC6** — When the stamp probe runs it prints `stamp decline rc=1 left=False`,
  `stamp undo rc=1 left=False`, `stamp landed rc=0 left=True` and `stamp write rc=0 left=True`.
  Red when: a decline or an undo leaves a stamp, or an artifact's write is missing from `written`.
  cost: about five seconds.
- **AC7** — When `grep -c '^FLOOR_ASSERTIONS=750$' tools/memory-tree/check-memory-hygiene.test.sh`
  runs it prints 1, and `grep -cE "^# MERGED at TOOL-aTrimmedWait-12's|RAISED 707 -> 708 by TOOL-aClearedLedger-6|RAISED 745 -> 749 by TOOL-aTrimmedWait-11" tools/memory-tree/check-memory-hygiene.test.sh`
  prints 3. `bash -n tools/memory-tree/check-memory-hygiene.test.sh` exits 0, and the probe prints
  `partition ours main-helper 0` and a `counts check-memory-hygiene.test.sh` line whose two numbers
  are equal.
  Red when: main's helper or compare survives, this branch's arm is edited, a raise comment is lost,
  or the floor is not the sum.
  figure: 750 is DERIVED as 707 + (708 - 707) + (749 - 707), each read with `git show` at
  `846d51d39`, `5d48501da` and the pre-merge tip.
- **AC8** — When `bash -n tools/unattended/unattended.sh` runs it exits 0, the probe prints
  `order forks 0 check_unit_spec 1 verb_dispatch 1` and `window refusals-before-start`, and
  `grep -c 'Both call sites read' tools/unattended/unattended.sh` prints 1.
  Red when: any order read forks, `verb_dispatch` reads its own order again, a lifted refusal moves
  below the checker's start, or main's comment is lost.
- **AC9** — When `grep -c -e '^FLOOR_ASSERTIONS=3374$' -e '^FLOOR_SHARD_3=469$' -e '^FLOOR_SHARD_4=431$' tools/unattended/unattended.test.sh`
  runs it prints 3, and `grep -c "^# MERGED at TOOL-aTrimmedWait-12's" tools/unattended/unattended.test.sh`
  prints 3. `bash -n tools/unattended/unattended.test.sh` exits 0. The probe prints a
  `counts unattended.test.sh` line whose two numbers are equal, then `region 3 main-LL8`,
  `region 3 main-LL3`, `region 3 ours-TW1`, `region 4 main-TP3` and `region 4 ours-TW5`.
  Red when: a raise comment is lost, a floor is not its sum, an arm line is lost or doubled, or a
  side's arms leave the region its shard floor counts.
  figure: each floor is DERIVED as base + (main - base) + (tip - base), read as AC7 reads its figure.
- **AC10** — When `grep -c '^FLOOR_ASSERTIONS=1051$' tools/workflows/unattended-build.test.sh` runs
  it prints 1, `grep -cE "^# MERGED at TOOL-aTrimmedWait-12's|RAISED 950 -> 958 by TOOL-aTrimmedWait-1|RAISED 1028 -> 1039 by TOOL-aTwinnedPass-11" tools/workflows/unattended-build.test.sh`
  prints 3, `bash -n tools/workflows/unattended-build.test.sh` exits 0, and the probe prints a
  `counts unattended-build.test.sh` line whose two numbers are equal.
  Red when: a raise comment is lost, the floor is not the sum, or an arm line is lost or doubled.
  figure: 1051 is DERIVED as AC9's figures are.
- **AC11** — Before the commit, `python tools/run-gates/regen.py --check` and
  `bash tools/unattended/adopt-unattended.sh --check` each exit 0, and
  `grep -c '"id": "extract_hs_lines"' memory/map/generated/symbols.json` prints 0. After it,
  `git show --remerge-diff --format= --name-only "$(git rev-list --merges -n 1 HEAD)" 2>/dev/null | sort -u` piped to
  `grep -vE '^(memory/(guides/SESSION-KICKOFF|DECISIONS|LIVE)[.]md|memory/project/readme-contract[.]txt|tools/template-size-limits[.]txt|tools/memory-tree/(gen_build_index[.]py|check-memory-hygiene[.]test[.]sh)|tools/unattended/unattended([.]test)?[.]sh|tools/workflows/unattended-build[.]test[.]sh|memory/(ledger/|map/generated/|builds/[^/]+/(README[.]md|spec/|build/2026-11-16-build-TOOL-aTrimmedWait-12-)))'`
  prints nothing.
  Red when: a generated output still holds one side's render, or the merge changes a file outside
  the eight, the generated outputs, the decisions row and the ledger against git's own result.
  cost: about two minutes for the regeneration check.
  permission: the after-commit half is the main loop's, as in AC1.
- **AC12** — After the re-stamp commit, `bash skills/session-kickoff/manifest-check.sh` exits 0,
  `git merge-tree --write-tree 5d48501da HEAD` exits 0, and
  `git merge-base --is-ancestor 5d48501da HEAD` exits 0.
  Red when: the stamp does not follow the merge, the landing merge would conflict, or `5d48501da` is
  not in the branch's history.
  permission: the main loop's, as in AC1.
- **AC13** — On a frozen clone of the branch after the re-stamp commit,
  `python tools/memory-tree/gen_build_index.py --selftest` exits 0.
  Red when: a selftest arm of either side fails over the merged `cmd_write`.
  permission: the main loop's, per the brief.
  cost: minutes, on the clone.

## 7. Gates

`kickoff-manifest ratchet` · `unattended skill size` · `unattended kit gate` · `unattended skill wiring` · `memory hygiene` · `build README slot contract` · `codebase-map coverage + freshness` · `kit version markers` · `policy fixtures` · `scratch-guard self-test` · `review-join self-test` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `recall floor` · `recall floor arms`

The first eight grade this unit's resolutions directly. The last eight are owed because a path of the
estimate trips their guard, by `python tools/check-spec-tokens.py --legs-for` at `766048903`, less
the broad guards. Per the brief, the main loop runs the bar once at the close without the self-test
suites, and the three conflicted suites and the build index selftest once on a frozen clone. No arm
is added or moved, so there is no `New arm:` line. Both sides' arms are each side's own, already
observed red and then green by the units that wrote them.

## 8. Open questions

- **F1 — Which partition helper survives the merge?** Main's `extract_hs_lines` folds the
  `cache hits` count. This branch's `derive_partition_lines` also sets aside the `cache recomputed`
  lines and carries a fixture arm. Recommendation: this branch's.
  RESOLVED (owner, 2026-11-16): `derive_partition_lines` and its fixture arm survive, and main's
  `extract_hs_lines` goes.

## 9. Revision log

- rev-1 · 2026-11-16 · initial draft from `prompts/2026-11-16-prompt-TOOL-aTrimmedWait-12-1-spec-writer.md`,
  grounded at `766048903` and `5d48501da`. The eight resolutions and both probes were run on the
  trial merge's files in the scratch directory.

## 10. Reuse audit

No existing seam fits a merge resolution. This unit writes no code, and both probes are one-off
observations. `python tools/codebase-map/reuse_lookup.py "reconcile a branch with local main: sum suite floors, merge a render stamp into a staged write, keep one partition helper"`
ranked generic name stems only (`write`, `sum`, `write_text`, `merge`, `stamp`). Of the task's named
seams, `order_verb_of` and `verb_dispatch` are read for S7 and S10, and `run_spec_token_check`'s
window for S10. `check_unit_spec`, `--check --staged` and its render decision are read for S10 and
not changed beyond S7. `plan_state`, `scan_consumes_cycles`, `derive_spec_token_key`, check 12's loop
and `--only`, `scanCommandHeads`, `checkRoleGate` and `load_session_calls` merged without a conflict
and are untouched. `regen.py --write` is the regeneration step. `_fixture` and
`resolve_render_stamp` are the stamp probe's harness, reused rather than rebuilt. The direct
precedents are TOOL-aTwinnedPass-13, whose `MERGED` lines and probe this spec follows, and
TOOL-aLightenedLoop-8, whose size-row reconcile S4 follows. `0ea0b59f6` is the precedent for S3's
follow-up re-stamp.

Recall terms used: `python tools/memory-recall/query.py "how was a reconcile merge with main resolved when both sides changed one function and raised suite floors" --terms "reconcile merge local main FLOOR_ASSERTIONS MERGED cmd_write render stamp staged kickoff manifest re-stamp size row"`
