# TOOL-dSkippedRecord-1 — acceptance ledger

**Serves:** journal TOOL-dSkippedRecord-1

No merge bar, no self-test suite, no `--selftest` and no leg argv ran in this pass. The pass started
at 25ac107a5, and this ledger rides in the product commit that closes the spec. AC1 to AC4 were
observed by a `bash` probe under the session scratchpad that sources `tools/unattended/lib-unattended.sh`,
slices `run_render_helper` out of the built `tools/unattended/unattended.test.sh` and `write_run_record`
out of a driver copy, and calls the helper in each mode in a repository under `%TEMP%`. The base
driver is `git show 81657e77c:tools/unattended/unattended.sh`.

**Evidences:** TOOL-dSkippedRecord-1
- AC1 — `HEAD: same` — the built driver printed `unattended: run record unchanged`, `HEAD: same`
  and no `its commit failed` in mode `same`. The base driver printed "its commit failed" with git's
  "no changes added to commit" beneath it, and no skip line, in the same mode.
- AC2 — `HEAD: moved` — the built driver printed `run record committed at`, `HEAD: moved` and
  `SUBJECT: records(tRun): the run record` in mode `moved`, and so did the base driver.
- AC3 — `git could not stage what the index render moved: memory/LIVE.md` — the built driver printed
  that line and `HEAD: same`, with no `run record committed at`. A copy with the `return 0` after
  that line deleted printed `run record committed at` and `HEAD: moved`.
- AC4 — `git could not test whether the stage holds a change (git diff --cached exited 128)` — the
  built driver printed that line and `HEAD: same`. A copy with the `case`'s catch-all arm removed,
  and the base driver, each committed and printed `HEAD: moved`.
- AC5 — `unchecked 0` — section 4's `scan_stage_file` probe over the built driver printed
  `unchecked 0` and a one-item list holding the `records($slug): the run record` commit line; over
  the base it printed `unchecked 1` and an empty list. The registry `grep -c` printed 0.
- AC6 — `grep -h -e 'unattended: run record' tools/unattended/unattended.sh` — against the
  `git grep` at 81657e77 it printed every base line unchanged and in order, plus the skip and
  refusal lines and nothing else. The `return [1-9]` count over `write_run_record` printed 0, and
  the `holds a diff` count over the comment and the function printed 2.

**Also probed:** the two existing no-mode calls of `run_render_helper` still answered their
`src/lu.sh` refusal and their `memory/LIVE.md` stage through the probe.

**Owed to the close (the main loop, after every unit is terminal):**
- New arm `tools/unattended/unattended.test.sh` region 8, mode `same` with `moved` as its control,
  covering AC1 and AC2: RED with `write_run_record` restored from 81657e77, GREEN once restored.
- New arm `tools/unattended/unattended.test.sh` region 8, modes `addfail` and `difffail`, covering
  AC3 and AC4: RED with the `return 0` after the second stage's refusal line deleted, and with the
  catch-all arm removed, GREEN once restored.
- The stage-commit leg's argv over the drained registry, and the gates section 7 names.

**Observed at the close (main loop, 2026-11-20):** the suite is held by the owner's standing
instruction, so each arm ran through the hermetic probe below, which sources the library, slices
`run_render_helper` out of the suite at `e56a3e698` and `write_run_record` and `scan_dirty_paths` out of a
driver copy, and calls the helper in each mode in a fixture repository under `%TEMP%`. The suite
at `e56a3e698` carries the red fix 26f99cdb0: the failed-stage modes fail their git call through a `git`
shim on PATH, not the two `GIT` overrides the spec's suite-arm design describes, because those
broke the lexicon's pins (red-fix records 1 and 2). Each break is a copy of the driver at `e56a3e698` in
the session scratchpad, never an edit in the tree.
- GREEN — the driver at `e56a3e698`: `same`, `moved`, `addfail` and `difffail` pass every line, and
  both no-mode calls answer as before. `STATUS 0`.
- Arm 1 (AC1, AC2) RED — the driver at 81657e77: mode `same` misses the skip line and carries
  "its commit failed"; mode `moved`, the control, passes, so the branch is reached and commits a real
  diff. Mode `difffail` commits too (HEAD moved), the base reading no failed test. `STATUS 1`.
- Arm 2 (AC3) RED — the `return 0` after the second stage's refusal line deleted (one line): mode
  `addfail` commits, "run record committed at" and no `HEAD: same`. Every other mode passes. `STATUS 1`.
- Arm 2 (AC4) RED — the `case`'s catch-all arm deleted (two lines): mode `difffail` misses the
  refusal line and moves HEAD. Every other mode passes. `STATUS 1`.
- AC5 — the stage-commit leg's own argv, `sh_hygiene.py --stage-commits` over the drained registry,
  run directly at e56a3e698: exit 0, "2 registered site(s) in 2 row(s) match the scan", and
  `tools/unattended/unattended.sh` reads only its two `unpaired` commits, neither the run record's.
  At the base, with the row standing, it read 3 sites in 3 rows.

The probe, as run (`probe.sh <driver> <suite> <lib> <fixture dir>`):

```bash
#!/bin/bash
# probe.sh <driver copy> <test file> <lib> <repo dir> -> the four modes' outputs, with run_render_helper sliced from the suite
SCRIPT=$1; TESTF=$2; LIB=$3; R=$4
. "$LIB"
st=0
hit()  { grep -qF -- "$2" <<<"$1" && echo "  ok hit: $2" || { echo "  FAIL missing: $2"; st=1; }; }
miss() { if grep -qF -- "$2" <<<"$1"; then echo "  FAIL unexpected: $2"; st=1; else echo "  ok miss: $2"; fi; }
slice_fn() {
  local s e
  s=$(grep -n "^$1()" "$SCRIPT" | cut -d: -f1)
  e=$(awk -v s="$s" 'NR>s && /^}/ {print NR; exit}' "$SCRIPT")
  eval "$(sed -n "${s},${e}p" "$SCRIPT")"
}
fixture() { git add -A >/dev/null && git commit -q -m fixture --no-verify; }
rm -rf "$R"; mkdir -p "$R"; cd "$R" || exit 2
git init -q -b unit .; git config user.email p@p; git config user.name p
printf 'base\n' > README; git add -A; git commit -q -m base --no-verify; UNIT0=$(git rev-parse HEAD)
reset_tree() { git reset -q --hard "$UNIT0"; git clean -qfd; printf 'MEMORY_ROOT="memory"\n' > .memory-tree.conf; }
s=$(grep -n '^run_render_helper()' "$TESTF" | cut -d: -f1)
e=$(awk -v s="$s" 'NR>s && /^}/ {print NR; exit}' "$TESTF")
eval "$(sed -n "${s},${e}p" "$TESTF")"
for m in same moved addfail difffail; do
  echo "== $m"
  out=$(run_render_helper "" write_run_record $m)
  printf '%s\n' "$out" | sed 's/^/   | /'
  case $m in
    same) hit "$out" "unattended: run record unchanged"; hit "$out" "HEAD: same"; miss "$out" "its commit failed" ;;
    moved) hit "$out" "run record committed at"; hit "$out" "HEAD: moved"; hit "$out" "SUBJECT: records(tRun): the run record" ;;
    addfail) hit "$out" "git could not stage what the index render moved: memory/LIVE.md"; hit "$out" "HEAD: same"; miss "$out" "run record committed at" ;;
    difffail) hit "$out" "git could not test whether the stage holds a change (git diff --cached exited 128)"; hit "$out" "HEAD: same" ;;
  esac
done
echo "== no mode (the existing calls)"
hit "$(run_render_helper 1 write_run_record)" "the index was not re-rendered: its inputs carry changes the index does not hold: src/lu.sh"
hit "$(run_render_helper "" write_run_record | grep '^STAGED:')" "memory/LIVE.md"
echo "STATUS $st"
```
