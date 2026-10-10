# Bars paid per landing, before and after, on two fixtures
**Serves:** journal TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-11
Measured on node a on 2026-10-09 (before) and 2026-10-10 (after), through gov's REAL pre-push hook
and REAL runner, copied into a scratch repo with four two-second stub legs: `leg a`, `leg b` and
`leg c`, each guarded on its own directory, and `leg whole`, which is unguarded. "Before" is the
tree at base `bef97330`; "after" is HEAD before the closing review. The two instruments are below,
verbatim, so either figure can be re-run.

**Legs executed at the boundary is the fair metric. Wall time is NOT comparable between the two
columns:** the host carried other sessions' bars at very different loads on the two days. The seed
push, the same four legs in both runs, took 124 s before and 34 s after. Within one column, wall
time still ranks the pushes.

## The owner's adopter shape (`adopter2.sh`)

GOV_GATE_CMD is a tracked wrapper that derives a manifest under the git dir and runs the runner
with `GATE_LEGS`, as inCMS's gov-bar does. The unattended in-place close is emulated as the driver
runs it: the build of 15 commits is merged onto main first, the wrapper bar runs `GATE_FULL=1` on
that merge, the driver's own `write_bar_green` records the green (absent at base), the close commits
its record on top, and that commit is pushed.

| Push | Before | After |
|---|---|---|
| landing after the close | FULL, 4 legs: "the leg manifest differs from the one the recorded green was earned on" | scoped from the close's `gate-bar-green`, 1 leg (the unguarded one) |
| 12 linear commits on main | FULL, 4 legs (12 commits behind) | FULL, 4 legs (12 first-parent landings behind, past the bound of 10) |

The landing row is the owner's measured case (ii); the second row is correct in both columns.

Before:

```text
B-seed · rc 0 · legs 4 · 82s · pre-push: FULL gate on main push (53927e07) — no recorded full green — bar: bash tools/wrap-bar.sh
B-main12 · rc 0 · legs 4 · 85s · pre-push: FULL gate on main push (dda5fd25) — the recorded full green is 12 commits behind the tip (bound 10) — bar: bash tools/wrap-bar.sh
B-close · rc 0 · legs 4 · 50s
B-close · the driver at this tree records no bar green
B-land · rc 0 · legs 4 · 61s · pre-push: FULL gate on main push (47c87ad1) — the leg manifest differs from the one the recorded green was earned on — bar: bash tools/wrap-bar.sh
```

After:

```text
B-seed · rc 0 · legs 4 · 83s · pre-push: FULL gate on main push (f0416b74) — the bar this push runs is not this kit's runner, so no runner stamp is a candidate (gate-full-green and gate-i
B-main12 · rc 0 · legs 4 · 87s · pre-push: FULL gate on main push (cd189035) — the bar this push runs is not this kit's runner, so no runner stamp is a candidate (gate-full-green and gate-i
B-close · rc 0 · legs 4 · 50s
B-land · rc 0 · legs 1 · 51s · pre-push: scoped gate on main push (f58dc93b) — full bar green c814d0c7 from this git dir's gate-bar-green is 1 first-parent landing(s) back, within 10 — bar:
```

## Gov's own shape (`landing.sh`)

The bar is the runner itself. S1: a close bar on the in-place merge, then that merge pushed. S1p: a
close bar on a 15-commit branch tip, then a `--no-ff` merge onto an unmoved main. S2: a red push on
`leg b`, then a one-line fix.

| Push | Before | After |
|---|---|---|
| S1 landing | scoped, 1 leg | covered, 0 legs, no bar |
| S1p landing | scoped, 1 leg | covered, 0 legs, no bar |
| S2 red, then fix | scoped, 4 then 3 legs | scoped, 4 then 3 legs |

S2 is unchanged by design: lineage reuse (design D5) applies on a FULL decision, and this fixture's
pushes scope. A fix pushed FULL re-runs the failed leg and the moved and unguarded legs, and reuses
the rest; TOOL-aFrugalTurnstile-4's acceptance ledger observes that directly.

Before:

```text
seed · rc 0 · bars 1 · legs 4 · 124s · pre-push: FULL gate on main push (023de7a0) — no recorded full green 
S1 close-bar · rc 0 · legs 4 · 75s
S1 landing  · rc 0 · bars 1 · legs 1 · 100s · pre-push: scoped gate on main push (e5918b5d) — full green e5918b5d is 0 commit(s) back, within 10 
S1p close-bar · rc 0 · legs 4 · 63s
S1p landing  · rc 0 · bars 1 · legs 1 · 73s · pre-push: scoped gate on main push (7cf6457f) — full green 650c3aaf is 1 commit(s) back, within 10 
S2 red push · rc 1 · bars 0 · legs 4 · 133s · pre-push: scoped gate on main push (ab82682e) — full green 650c3aaf is 3 commit(s) back, within 10 
S2 fix push · rc 0 · bars 0 · legs 3 · 128s · pre-push: scoped gate on main push (751aa26f) — full green 650c3aaf is 4 commit(s) back, within 10 
```

After:

```text
seed · rc 0 · bars 1 · legs 4 · 34s · pre-push: FULL gate on main push (03cc7b8f) — no recorded full green 
S1 close-bar · rc 0 · legs 4 · 28s
S1 landing  · rc 0 · bars 0 · legs 0 · 10s · 
S1p close-bar · rc 0 · legs 4 · 28s
S1p landing  · rc 0 · bars 0 · legs 0 · 9s · 
S2 red push · rc 1 · bars 1 · legs 4 · 62s · pre-push: scoped gate on main push (99e9506d) — full green 7662b950 from this git dir's gate-full-green is 3 first-parent landing(s) back,
S2 fix push · rc 0 · bars 1 · legs 3 · 55s · pre-push: scoped gate on main push (8f8a53ed) — full green 7662b950 from this git dir's gate-full-green is 4 first-parent landing(s) back,
```

## A real adopter push

Not measured here. Pushing inCMS's or NicoCares' main is outside this run's mandate, and neither
adopter carries this gov yet: the adoption session pulls it in after this build lands. The adopter
fixture above reproduces the owner's measured refusal byte for byte (case ii) and the decision that
replaces it.

## Instrument: `adopter2.sh`

```bash
#!/usr/bin/env bash
# adopter2.sh <gov-tree> <out-dir> — inCMS's shape, with the unattended IN-PLACE close emulated as
# the driver runs it: the build is merged onto main first (the prepared merge), the wrapper bar runs
# GATE_FULL=1 on that merge, the driver's own write_bar_green (sliced out of <gov-tree>'s
# unattended.sh when it has one) records the green, the close commits its run-state record on top,
# and the lander pushes that record commit. Main took 12 first-parent commits since its last full
# green. Prints one line per push: rc, legs executed at the boundary, wall seconds, decision.
set -u
SRC=$(cd "$1" && pwd); OUT=$2
mkdir -p "$OUT"; rm -rf "$OUT"/*
cd "$OUT" || exit 2
git init -q --bare remote.git
git init -q work; cd work || exit 2
git config user.email m@example.com; git config user.name m
git config core.autocrlf false
mkdir -p .githooks tools/run-gates a b c memory
cp "$SRC/.githooks/pre-push" .githooks/pre-push
printf 'GOV_KITROOT=tools\nINHERITED_RED=land\nGOV_GATE_CMD="bash tools/wrap-bar.sh"\n' > .githooks/gate-env.sh
printf 'GATE_CMD="bash tools/wrap-bar.sh"\n' > .unattended.conf
for f in run-gates.sh gate-fingerprint.sh lib-attribute.sh gate-profiles.txt kit.toml post-merge.sh; do
  [ -f "$SRC/tools/run-gates/$f" ] && cp "$SRC/tools/run-gates/$f" tools/run-gates/
done
cat > tools/leg.sh <<'EOF'
#!/usr/bin/env bash
echo "$1" >> "$LEG_LOG"
sleep "${LEG_SLEEP:-2}"
[ -f "$1/FAIL" ] && { echo "leg $1 red"; exit 1; }
exit 0
EOF
cat > tools/gate-legs.json <<'EOF'
[
  {"name": "leg a", "argv": ["bash", "tools/leg.sh", "a"], "guard": ["a/"], "ceiling": 120},
  {"name": "leg b", "argv": ["bash", "tools/leg.sh", "b"], "guard": ["b/"], "ceiling": 120},
  {"name": "leg c", "argv": ["bash", "tools/leg.sh", "c"], "guard": ["c/"], "ceiling": 120},
  {"name": "leg whole", "argv": ["bash", "tools/leg.sh", "whole"], "ceiling": 120}
]
EOF
cat > tools/wrap-bar.sh <<'EOF'
#!/usr/bin/env bash
legs="$(git rev-parse --git-dir)/wrap-legs.json"
{ echo "// derived"; cat tools/gate-legs.json; } | sed '1d' | sed 's/  {/ {/' > "$legs"
export GATE_LEGS="$legs"
exec bash tools/run-gates/run-gates.sh "$@"
EOF
echo x > a/f; echo x > b/f; echo x > c/f; echo run > memory/RUN.md
printf '* text eol=lf\n' > .gitattributes
git add -A; git commit -q -m init; git branch -M main
git remote add origin "$OUT/remote.git"
git config core.hooksPath .githooks
export GOV_DEFAULT_BRANCH=main LEG_LOG="$OUT/legs.log" GATE_TURNSTILE_DIR="$OUT/turnstile"
gd=$(git rev-parse --git-dir)
touch "$gd/push-main-active"
legs() { [ -f "$LEG_LOG" ] && wc -l < "$LEG_LOG" | tr -d ' ' || echo 0; }
push() {
  local l0 t0
  l0=$(legs); t0=$(date +%s)
  git push -q origin main > "$OUT/push-$1.log" 2>&1; P_RC=$?
  touch "$gd/push-main-active"
  P_LEGS=$(( $(legs) - l0 )); P_WALL=$(( $(date +%s) - t0 ))
  P_DEC=$(grep -m1 -oE 'pre-push: (FULL gate|scoped gate|covered|no bar)[^—]*— .{0,110}' "$OUT/push-$1.log" | head -1)
}
push seed
echo "B-seed · rc $P_RC · legs $P_LEGS · ${P_WALL}s · $P_DEC"
for i in $(seq 1 12); do echo "m$i" >> b/f; git commit -q -am "main $i"; done
push main12
echo "B-main12 · rc $P_RC · legs $P_LEGS · ${P_WALL}s · $P_DEC"
git checkout -q -b build main~12
for i in $(seq 1 15); do echo "$i" >> a/f; git commit -q -am "build $i"; done
git checkout -q main; git merge -q --no-ff build -m "merge: build (prepared)"
M=$(git rev-parse HEAD)
t0=$(date +%s); l0=$(legs)
GATE_FULL=1 bash tools/wrap-bar.sh > "$OUT/close.log" 2>&1; crc=$?
echo "B-close · rc $crc · legs $(( $(legs) - l0 )) · $(( $(date +%s) - t0 ))s"
U="$SRC/tools/unattended/unattended.sh"
if [ -f "$U" ] && grep -q '^write_bar_green() {' "$U"; then
  GIT() { git "$@"; }
  eval "$(awk '/^write_bar_green\(\) \{/,/^}/' "$U")"
  write_bar_green "$gd" "$M" "$crc" full "" "bash tools/wrap-bar.sh" "close-1"
else
  echo "B-close · the driver at this tree records no bar green"
fi
echo "LANDING" >> memory/RUN.md; git commit -q -am "records: close — LANDING"
push land
echo "B-land · rc $P_RC · legs $P_LEGS · ${P_WALL}s · $P_DEC"
```

## Instrument: `landing.sh`

```bash
#!/usr/bin/env bash
# landing.sh <gov-tree> <out-dir> — the owner's landing shape in a scratch repo, through gov's REAL
# pre-push hook and REAL runner from <gov-tree>, with four sleep legs. Prints one line per scenario:
#   scenario · pushes · bars run at the boundary · legs executed at the boundary · wall seconds
# A "bar" is a run directory the runner wrote under the git dir during the push; a "leg executed" is
# a leg marker file the stub legs append to. Both are POSITIVE artifacts of work, so an arm that
# exited early reads 0, never a pass.
set -u
SRC=$(cd "$1" && pwd); OUT=$2
mkdir -p "$OUT"; rm -rf "$OUT"/*
cd "$OUT" || exit 2
git init -q --bare remote.git
git init -q work; cd work || exit 2
git config user.email m@example.com; git config user.name m
git config core.autocrlf false
mkdir -p .githooks tools/run-gates a b c
cp "$SRC/.githooks/pre-push" .githooks/pre-push
printf 'GOV_KITROOT=tools\nINHERITED_RED=land\n' > .githooks/gate-env.sh
for f in run-gates.sh gate-fingerprint.sh lib-attribute.sh gate-profiles.txt kit.toml; do
  [ -f "$SRC/tools/run-gates/$f" ] && cp "$SRC/tools/run-gates/$f" tools/run-gates/
done
for f in post-merge.sh; do [ -f "$SRC/tools/run-gates/$f" ] && cp "$SRC/tools/run-gates/$f" tools/run-gates/; done
# The stub leg: appends its name to a marker OUTSIDE the tree, sleeps, fails when <dir>/FAIL exists.
cat > tools/leg.sh <<'EOF'
#!/usr/bin/env bash
echo "$1" >> "$LEG_LOG"
sleep "${LEG_SLEEP:-2}"
[ -f "$1/FAIL" ] && { echo "leg $1 red"; exit 1; }
exit 0
EOF
cat > tools/gate-legs.json <<'EOF'
[
  {"name": "leg a", "argv": ["bash", "tools/leg.sh", "a"], "guard": ["a/"], "ceiling": 120},
  {"name": "leg b", "argv": ["bash", "tools/leg.sh", "b"], "guard": ["b/"], "ceiling": 120},
  {"name": "leg c", "argv": ["bash", "tools/leg.sh", "c"], "guard": ["c/"], "ceiling": 120},
  {"name": "leg whole", "argv": ["bash", "tools/leg.sh", "whole"], "ceiling": 120}
]
EOF
echo x > a/f; echo x > b/f; echo x > c/f
printf '* text eol=lf\n' > .gitattributes
git add -A; git commit -q -m init; git branch -M main
git remote add origin "$OUT/remote.git"
git config core.hooksPath .githooks
export GOV_DEFAULT_BRANCH=main LEG_LOG="$OUT/legs.log" GATE_TURNSTILE_DIR="$OUT/turnstile"
gd=$(git rev-parse --git-dir)
touch "$gd/push-main-active"
runs() { ls -1 "$gd/gate-run" 2>/dev/null | grep -vc '^current$'; }
legs() { [ -f "$LEG_LOG" ] && wc -l < "$LEG_LOG" | tr -d ' ' || echo 0; }
# push <label>: one push, its bars and legs counted, its decision line kept.
push() {
  local r0 l0 t0 rc
  r0=$(runs); l0=$(legs); t0=$(date +%s)
  git push -q origin main > "$OUT/push-$1.log" 2>&1; rc=$?
  touch "$gd/push-main-active"
  P_BARS=$(( $(runs) - r0 )); P_LEGS=$(( $(legs) - l0 )); P_WALL=$(( $(date +%s) - t0 )); P_RC=$rc
  P_DEC=$(grep -m1 -oE 'pre-push: (FULL gate|scoped gate|no bar)[^—]*— [^—]{0,90}' "$OUT/push-$1.log" | head -1)
}
# the seed push: main's first green, bar 1.
push seed
echo "seed · rc $P_RC · bars $P_BARS · legs $P_LEGS · ${P_WALL}s · $P_DEC"

# S1 — a build of 15 commits, the close bar FULL on the prepared --no-ff merge, then the landing push.
git checkout -q -b build
for i in $(seq 1 15); do echo "$i" >> a/f; git commit -q -am "build $i"; done
git checkout -q main; git merge -q --no-ff build -m "merge: build"
t0=$(date +%s); l0=$(legs)
GATE_FULL=1 bash tools/run-gates/run-gates.sh > "$OUT/close-s1.log" 2>&1; crc=$?
CLOSE_LEGS=$(( $(legs) - l0 )); CLOSE_WALL=$(( $(date +%s) - t0 ))
push s1
echo "S1 close-bar · rc $crc · legs $CLOSE_LEGS · ${CLOSE_WALL}s"
echo "S1 landing  · rc $P_RC · bars $P_BARS · legs $P_LEGS · ${P_WALL}s · $P_DEC"

# S1p — the primary-lander and adopter shape: the close bar FULL on the BRANCH tip, then a --no-ff
# landing merge carrying 15 commits, so the recorded green is the merge's second parent.
git checkout -q -b build2
for i in $(seq 1 15); do echo "$i" >> c/f; git commit -q -am "build2 $i"; done
t0=$(date +%s); l0=$(legs)
GATE_FULL=1 bash tools/run-gates/run-gates.sh > "$OUT/close-s1p.log" 2>&1; crc=$?
CLOSE_LEGS=$(( $(legs) - l0 )); CLOSE_WALL=$(( $(date +%s) - t0 ))
git checkout -q main; git merge -q --no-ff build2 -m "merge: build2"
push s1p
echo "S1p close-bar · rc $crc · legs $CLOSE_LEGS · ${CLOSE_WALL}s"
echo "S1p landing  · rc $P_RC · bars $P_BARS · legs $P_LEGS · ${P_WALL}s · $P_DEC"

# S2 — a red at the boundary, then a one-line fix: leg b red on the first push, fixed, pushed again.
echo y >> b/f; touch b/FAIL; git add -A; git commit -q -m "change b, and break it"
echo y >> c/f; git commit -q -am "change c"
push s2a
echo "S2 red push · rc $P_RC · bars $P_BARS · legs $P_LEGS · ${P_WALL}s · $P_DEC"
git rm -q b/FAIL; git commit -q -m "fix b"
push s2b
echo "S2 fix push · rc $P_RC · bars $P_BARS · legs $P_LEGS · ${P_WALL}s · $P_DEC"
```
