#!/usr/bin/env bash
# **Serves:** journal TOOL-aSparedSpawn-17
# The direct check TOOL-aSparedSpawn-17's pass ran. Usage: bash <this> <repo-root> <scratch-dir> <runner copy> aged|plain|sampled
#
# One hand-built scratch repo, two `bash -c` legs: `pa` reads FLIP, which no key holds, so its earned
# `ok` is wrong once FLIP is set; `pb` is green. The first bar earns the entries; the case then reds
# `pa` against its cached `ok`, by the age bound (aged), by a plain bar (plain) or by the sample
# (sampled, the control the change must leave alone), and prints whether the entry survived and
# whether the leg was quarantined. A clean green bar then earns the key again and a reuse bar shows
# whether `pa` executes. Run once over the changed runner and once over `git show <base>:` of it.
# No step runs a suite, a slice of one, or the tree's bar.
set -u
R=${1:?repo root}; S=${2:?scratch dir}; RUNNER=${3:?runner copy}; CASE=${4:?case}
mkdir -p "$S" || exit 2
T=$(mktemp -d -p "$S") || exit 2
mkdir -p "$T/tools/run-gates" "$T/tools/lib" "$T/ga" "$T/gb"
cp "$RUNNER" "$T/tools/run-gates/run-gates.sh" || exit 2
cp "$R/tools/run-gates/gate-fingerprint.sh" "$R/tools/run-gates/gate-profiles.txt" "$T/tools/run-gates/" || exit 2
cp "$R/tools/lib/resolve-python.sh" "$T/tools/lib/" || exit 2
echo x > "$T/ga/f"; echo y > "$T/gb/f"
printf '%s\n' '[' \
  '  {"name": "pa", "argv": ["bash", "-c", "[ -z \"${FLIP:-}\" ]"], "guard": ["ga/"]},' \
  '  {"name": "pb", "argv": ["bash", "-c", "exit 0"], "guard": ["gb/"]}' \
  ']' > "$T/tools/gate-legs.json"
cd "$T" && git init -q --template= -b main . && git add -A 2>/dev/null && git commit -qm seed || exit 2
E=$(git hash-object -w -t tree /dev/null)
run_bar() { env -u GATE_FULL -u GATE_REUSE -u GATE_REUSE_PUSH -u GATE_LEGS -u FLIP GATE_MEMPAUSE=0 GATE_BASE="$E" \
    GATE_REUSE_SAMPLE=0 "$@" bash tools/run-gates/run-gates.sh > "$T.out" 2>&1; echo "rc=$?"; }
read_key() { local c; IFS= read -r c < .git/gate-run/current; awk -F'\t' '$1 == "pa" { print $7; exit }' .git/gate-run/"$c"/[0-9]*.leg; }
run_bar >/dev/null
K=$(read_key); echo "key=$K"
[ -e ".git/gate-cache/${K:0:2}/$K" ] && echo "PRE entry exists" || echo "PRE entry MISSING"
case $CASE in
  aged)
    run_bar GATE_REUSE=1 >/dev/null
    for f in .git/gate-cache/age.*; do printf '10' > "$f"; done
    run_bar GATE_REUSE=1 FLIP=1 ;;
  sampled) run_bar GATE_REUSE=1 GATE_REUSE_SAMPLE=1 FLIP=1 ;;
  plain) run_bar FLIP=1 ;;
  *) echo "unknown case $CASE"; exit 2 ;;
esac
grep -E 'cache disagreement|in a row|^GATE ' "$T.out"
[ -e ".git/gate-cache/${K:0:2}/$K" ] && echo "POST entry SURVIVES" || echo "POST entry erased"
ls .git/gate-cache/quarantine.* >/dev/null 2>&1 && echo "POST quarantined" || echo "POST not quarantined"
run_bar >/dev/null
[ -e ".git/gate-cache/${K:0:2}/$K" ] && echo "RE-EARN entry back" || echo "RE-EARN entry missing"
run_bar GATE_REUSE=1
grep '^GATE ' "$T.out"
cd "$S" && rm -rf "$T" "$T.out"
