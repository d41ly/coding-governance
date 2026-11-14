# TOOL-aLightenedLoop-1 — acceptance ledger

**Serves:** journal TOOL-aLightenedLoop-1

No merge bar and no self-test suite ran in this pass. The criteria were observed by the spec's
parity instrument on node `a`, both sides in one sitting, one side at a time, each scenario run in
the foreground with nothing else of this pass running. Two departures from §4's instrument, neither
changing what it reads: the scratch tree is a `git clone` of this worktree at `%TEMP%/al1p` rather
than a `git worktree add`, and P0 took the tip's tool files from this worktree's uncommitted copies,
compared equal to them modulo CRLF before the run. P0 is `72c6aa59`, the worktree's HEAD `4377f637`
with the tip's files, `LIVE_LANDED_UNCLOSED` blanked and the tip's `--write` committed; Pb is
`751be9cd`, P0 with `tools/memory-tree/gen_build_index.py` and `tools/check-spec-tokens.py` checked
out of `846d51d3`. `diff -r -x ac1-newer.txt` over the base and tip capture folders printed only the
two declared deltas, AC3's and AC5's, and the two tip-only probe files.

The instrument, `parity_al1.sh`, run as `parity_al1.sh <worktree> %TEMP%/al1p <captures> setup` once,
then `<base|tip> g1` to `g6`:

```bash
set -u
SRC=$1 P=$2 OUT=$3 PHASE=$4 GROUP=${5:-}
BASE=846d51d3
GBI=tools/memory-tree/gen_build_index.py
AN=memory/builds/aLightenedLoop/build/2026-11-14-build-TOOL-aLightenedLoop-1-analysis.md
SP=memory/builds/aLightenedLoop/spec/2026-11-14-spec-TOOL-aLightenedLoop-2.md
DEV=memory/builds/aQueuedIndex/build/2026-11-12-build-TOOL-aQueuedIndex-1-deviation-11.md
SYS=memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md
QR=memory/builds/aQueuedIndex/README.md
WOM=memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-1.md
if [ "$PHASE" = setup ]; then
  mkdir -p "$OUT"
  if [ ! -f "$P/.git/index" ]; then rm -rf "$P"; git clone -q "$SRC" "$P" || exit 2; fi
  cd "$P" || exit 2
  git reset -q --hard; git checkout -q --detach "$(git -C "$SRC" rev-parse HEAD)"
  git config user.name t; git config user.email t@t.test
  for f in tools/memory-tree/gen_build_index.py tools/check-spec-tokens.py tools/memory-tree/README.md tools/check-spec-tokens.test.sh; do
    cp "$SRC/$f" "$f"
  done
  sed -i 's/^LIVE_LANDED_UNCLOSED="1"/LIVE_LANDED_UNCLOSED=""/' .memory-tree.conf
  python -B $GBI --write > "$OUT/p0-write.txt" 2>&1; echo "rc=$?" >> "$OUT/p0-write.txt"
  git add -A; git commit -qm P0; git tag -f P0 >/dev/null
  git checkout -q $BASE -- tools/memory-tree/gen_build_index.py tools/check-spec-tokens.py
  git commit -qm Pb; git tag -f Pb >/dev/null
  exit 0
fi
cd "$P" || exit 2
SIDE=$PHASE; REF=Pb; [ "$SIDE" = tip ] && REF=P0
mkdir -p "$OUT/$SIDE"
reset_to() { git reset -q --hard "$REF"; git clean -qfd; rm -f "$(git rev-parse --git-path gen-build-index-render-stamp)"; }
cap() {   # stdout and stderr merged, then the exit code; the seconds go to <side>.times
  local name=$1; shift
  local t0 t1 rc
  t0=$(date +%s.%N); "$@" > "$OUT/$SIDE/$name.txt" 2>&1; rc=$?; t1=$(date +%s.%N)
  echo "rc=$rc" >> "$OUT/$SIDE/$name.txt"
  echo "$name $(python -c "print(round($t1-$t0,1))")" >> "$OUT/$SIDE.times"
}
edit_spec() { sed -i '$ s/$/ edited/' "$SP"; }
probe() {
  python -B -c 'import sys, importlib.util
sys.path.insert(0, "tools/memory-tree")
import gen_build_index as g
s = importlib.util.spec_from_file_location("cst", "tools/check-spec-tokens.py"); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
v = m.derive_carries_coverage(".", conf=g.load_conf("."), building=True)
print(sys.argv[1], sorted({type(e["findings"]).__name__ for e in v["builds"].values()}))' "$1"
}
case $GROUP in
g1) reset_to; cap ac1-write1 python -B $GBI --write
    touch "$OUT/$SIDE.marker"; sleep 2
    cap ac1-write2 python -B $GBI --write
    find memory -type f -newer "$OUT/$SIDE.marker" | sort > "$OUT/$SIDE/ac1-newer.txt"
    reset_to; cap ac2-write python -B $GBI --write
    git status --porcelain > "$OUT/$SIDE/ac2-porcelain.txt"
    cap ac2-check python -B $GBI --check ;;
g2) reset_to; edit_spec; git add -A
    cap ac3-write python -B $GBI --write; git add -u
    cap ac3-staged python -B $GBI --check --staged
    reset_to; edit_spec; git add -A
    cap ac4a-write python -B $GBI --write; git add -u; printf 'x' >> "$SP"
    cap ac4a-staged python -B $GBI --check --staged ;;
g3) reset_to
    printf 'not a month shard\n' > memory/ledger/notes.txt; git add memory/ledger/notes.txt; git commit -qm ledger-notes
    edit_spec; git add -A
    cap ac4b-write python -B $GBI --write; git add -u
    cap ac4b-staged python -B $GBI --check --staged
    reset_to; printf '\nA plain line citing nothing.\n' >> "$AN"; git add "$AN"
    cap ac5-staged python -B $GBI --check --staged ;;
g4) reset_to; sed -i '1s/^\*\*Serves:\*\* research/**Serves:** journal/' "$AN"; git add "$AN"
    cap ac6-1-serves python -B $GBI --check --staged
    reset_to; printf '\nA body line.\n' >> "$DEV"; git add "$DEV"
    cap ac6-2-deviation python -B $GBI --check --staged
    reset_to; printf '\nA body line.\n' >> "$SYS"; git add "$SYS"
    cap ac6-3-design python -B $GBI --check --staged ;;
g5) reset_to; printf '\nNow citing TOOL-aQueuedIndex-1.\n' >> "$AN"; git add "$AN"
    cap ac6-4-id python -B $GBI --check --staged
    reset_to; printf '\nA plain line citing nothing.\n' >> "$AN"
    sed -i '/<!-- gen:build-index -->/{n;s/$/ hand/}' "$QR"; git add "$AN" "$QR"
    cap ac6-5-order python -B $GBI --check --staged ;;
g6) reset_to; printf '\nA plain line citing nothing.\n' >> "$AN"; git add "$AN"
    cap ac7-coverage python -B $GBI --check-coverage --staged
    [ "$SIDE" = tip ] && probe "AC7 probe" > "$OUT/tip/ac7-probe.txt" 2>&1
    reset_to; sed -i '0,/^\*\*Status:\*\* DEFERRED/s//**Status:** INPROGRESS/' "$WOM"; git add "$WOM"
    cap ac8-coverage python -B $GBI --check-coverage --staged
    [ "$SIDE" = tip ] && probe "AC8 probe" > "$OUT/tip/ac8-probe.txt" 2>&1 ;;
esac
reset_to
```

The wall-clock seconds, base then tip, every scenario:

| Scenario | Base s | Tip s | Exit, both sides |
|---|---|---|---|
| ac1-write1 | 65.4 | 36.4 | 0 |
| ac1-write2 (AC10) | 67.4 | 32.0 | 0 |
| ac2-write | 40.3 | 33.1 | 0 |
| ac2-check | 31.9 | 42.8 | 0 |
| ac3-write | 57.0 | 33.3 | 0 |
| ac3-staged (AC10) | 31.2 | 1.3 | 0 |
| ac4a-write | 30.3 | 30.3 | 0 |
| ac4a-staged | 28.8 | 29.3 | 0 |
| ac4b-write | 29.5 | 28.7 | 0 |
| ac4b-staged | 27.6 | 29.0 | 1 |
| ac5-staged (AC10) | 30.2 | 0.5 | 0 |
| ac6-1-serves | 32.3 | 29.8 | 1 |
| ac6-2-deviation | 31.1 | 28.3 | 0 |
| ac6-3-design | 33.8 | 27.8 | 0 |
| ac6-4-id | 34.1 | 30.4 | 0 |
| ac6-5-order | 31.7 | 27.6 | 1 |
| ac7-coverage (AC10) | 17.1 | 2.4 | 0 |
| ac8-coverage | 15.9 | 12.7 | 0 |

**Evidences:** TOOL-aLightenedLoop-1
- AC1 — `find memory -type f -newer <marker>` — after the tip's second `gen_build_index.py --write`
  on P0 it listed 0 files; on the base side it listed 3212, every artifact.
- AC2 — `diff -r` — over the `gen_build_index.py --write` and `gen_build_index.py --check`
  captures of both sides it printed nothing, each `--check` ending `build-index: clean (3212
  artifact(s))` and exit 0, and both `git status --porcelain` readings were empty.
- AC3 — `render answered by the stamp` — after the spec edit, `git add`, `gen_build_index.py --write`
  and `git add -u`, the tip's `gen_build_index.py --check --staged` printed the owed line then that
  stamp line and exited 0; the base's full check printed `build-index: clean (3212 artifact(s))` and
  exited 0; `grep -c "render SKIPPED"` counted 0 in both captures.
- AC4 — `gen_build_index.py --check --staged` — with one more working-tree byte the tip printed no
  stamp line and rendered in full, exit 0; with `memory/ledger/notes.txt` committed, `--write` warned
  of the unmanaged file, wrote no stamp, and the staged check exited 1 naming it; both captures
  diffed empty against the base's.
- AC5 — `render SKIPPED under --staged` — the tip printed it naming `1 of them build records whose
  binding head is unchanged` and exited 0 in 0.5 s; the base printed the `render owed` line naming
  the analysis record, rendered, and exited 0.
- AC6 — `render owed` — the `**Serves:**` edit, the deviation-11 body edit, the dClosedLoop systems
  append and the appended `TOOL-aQueuedIndex-1` each printed the owed line naming its own path on
  both sides, each pair diffing empty; the fifth, the quiet append with a hand edit in
  `memory/builds/aQueuedIndex/README.md`, exited 1 on both sides with the owed line naming the
  analysis record and identical captures.
- AC7 — `derive_carries_coverage(root, conf=conf, building=True)` — `gen_build_index.py
  --check-coverage --staged` printed the same `graded 0 INPROGRESS chain spec(s) in 0 of 22` count
  line on both sides, exit 0, captures identical; the tip's `python -B -c` probe printed
  `AC7 probe ['NoneType']`.
- AC8 — `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-1.md` — flipped
  to INPROGRESS and staged, `gen_build_index.py --check-coverage --staged` printed `graded 1
  INPROGRESS chain spec(s) in 1 of 22` on both sides, exit 0, captures identical; the tip's probe
  printed `AC8 probe ['list']`.
- AC9 — `tools/memory-tree/README.md` — the grep printed line 374 (`no chain spec stands at
  INPROGRESS`), line 606 (`build/ folder`) and line 612 (`render answered by the stamp`).
- AC10 — `a` — on node `a` in one sitting, base then tip: AC1's second `--write` 67.4 then 32.0 s,
  AC3's staged check 31.2 then 1.3 s, AC5's staged check 30.2 then 0.5 s, AC7's coverage check 17.1
  then 2.4 s; each tip reading is below its base reading.
