#!/usr/bin/env bash
# **Serves:** journal TOOL-aMooredAnchor-1  <!-- inferred: this build defines exactly one spec id, so the record can serve nothing else -->
# Reproduction harness for the residual half of D3 (unattended BASE anchor).
# Fixture mirrors check-unattended.test.sh exactly, then runs four defeats, each with a control.
set -u
HERE="$1"          # tools/unattended in the source tree
TMP=$(mktemp -d)
ORIGIN_DIR=$(mktemp -d)
trap 'rm -rf "$TMP" "$ORIGIN_DIR"' EXIT

cd "$TMP" || exit 2
git init -q -b main . && git config user.email t@t.test && git config user.name t \
  && git config core.autocrlf false
mkdir -p tools/unattended memory/guides
cp "$HERE/check-unattended.sh" "$HERE/unattended.sh" "$HERE/PROTOCOL.template.md" tools/unattended/
cp "$HERE/PROTOCOL.template.md" memory/guides/UNATTENDED-PROTOCOL.md
GATE="$TMP/tools/unattended/check-unattended.sh"
DRIVER="$TMP/tools/unattended/unattended.sh"

cat > .unattended.conf <<'EOF'
MEMORY_ROOT=memory
LANDER="echo land"
BYPASS_BAN="--no-verify"
GATE_CMD="true"
WIRING_CHECK="true"
CORE_FLOOR="6:6"
KEEPALIVE_CREATE="CronCreate"
KEEPALIVE_DELETE="CronDelete"
PHASES_EXTRA=""
DOD_EXTRA=""
EOF

mkdir -p memory/builds/tRun
cat > memory/builds/tRun/README.md <<'EOF'
# tRun

<!-- gen:build-index -->
**Build status:** OPEN · 1 unit(s)
<!-- /gen:build-index -->
EOF
runmd() { cat > memory/builds/tRun/RUN.md <<EOF
# tRun — run state

<!-- run:generated -->
**Build status:** OPEN · 1 unit(s)
<!-- /run:generated -->

## Mandate
<!-- run:mandate -->
$1
<!-- /run:mandate -->

## Run facts
phase: RUNNING
witness: WITNESS
base: BASE
EOF
}

# ---- the OWNER's tree, on main: the real mandate, committed before any run exists.
runmd "The owner authorizes tRun to merge and to push."
git add -A && git commit -q -m base --no-verify
ORIGIN="$ORIGIN_DIR/origin.git"
git init -q --bare "$ORIGIN" && git remote add origin "$ORIGIN" && git push -q origin main
git remote set-head origin main
ANCHOR0=$(git rev-parse main)

# ---- the RUN starts on its own branch and does one commit of honest work.
git checkout -q -b unit
git commit -q --allow-empty -m "unit work" --no-verify
HONEST=$(git rev-parse HEAD)
sed -i "s/^witness: WITNESS$/witness: $HONEST/" memory/builds/tRun/RUN.md
sed -i "s|^base: BASE$|base: $(git merge-base refs/remotes/origin/main HEAD)|" memory/builds/tRun/RUN.md
git add -A && git commit -q -m facts --no-verify
PRISTINE=$(git rev-parse HEAD)

# Restore BOTH the work tree and the whole refs/remotes namespace. --no-deref, or `update-ref -d`
# on the symbolic origin/HEAD deletes the ref it POINTS AT instead of itself.
reset() {
  git checkout -q unit 2>/dev/null; git reset -q --hard "$PRISTINE"; git clean -qfd
  local r
  for r in $(git for-each-ref --format='%(refname)' refs/remotes/); do
    git update-ref -d --no-deref "$r"
  done
  git update-ref refs/remotes/origin/main "$ANCHOR0"
  git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main
}
# Assert the fixture really is in the state the arm claims, or a green is meaningless.
assert_refs() {
  printf '  refs: origin/HEAD=%s origin/main=%s\n' \
    "$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null || echo UNSET)" \
    "$(git rev-parse --short refs/remotes/origin/main 2>/dev/null || echo UNSET)"
}
say()     { printf '\n======== %s\n' "$1"; }
verdict() { if [ -z "$2" ] && [ "$3" = 0 ]; then printf '  >>> GATE GREEN (exit 0, silent) — %s\n' "$1"
            else printf '  >>> gate reds (exit %s): %s\n' "$3" "$(printf '%s' "$2" | head -2)"; fi; }
# The run forges its own mandate, commits it, then commits again so the forged commit is NOT HEAD
# (base == HEAD is already refused). Echoes the forged sha.
forge() {
  runmd "FORGED — the run authorizes ITSELF to merge and to push."
  sed -i "s/^witness: .*/witness: $HONEST/" memory/builds/tRun/RUN.md
  git add -A && git commit -q -m "run's own forged mandate" --no-verify
  local f; f=$(git rev-parse HEAD)
  git commit -q --allow-empty -m "more run work" --no-verify
  sed -i "s/^base: .*/base: $f/" memory/builds/tRun/RUN.md
  git add -A && git commit -q -m facts --no-verify
  printf '%s' "$f"
}

# =========================================================================== CONTROL A
say "CONTROL A — honest tree, unmodified refs. Must be green."
reset; assert_refs; out=$(bash "$GATE" 2>&1); rc=$?
verdict "the honest state" "$out" "$rc"

# =========================================================================== CONTROL B
say "CONTROL B — forged mandate, refs UNTOUCHED. Must RED, or nothing below means anything."
reset; F=$(forge)
git update-ref refs/remotes/origin/main "$ANCHOR0"   # anchor honest; only the mandate is forged
assert_refs; out=$(bash "$GATE" 2>&1); rc=$?
verdict "a forged mandate with an honest anchor" "$out" "$rc"

# =========================================================================== DEFEAT 1
say "DEFEAT 1 — run rewrites refs/remotes/origin/main with update-ref (NO env var, no push)"
reset; F=$(forge)
git update-ref refs/remotes/origin/main "$F"          # <-- the whole attack, one command
assert_refs
echo "  merge-base=$(git merge-base refs/remotes/origin/main HEAD | cut -c1-12)  HEAD=$(git rev-parse --short=12 HEAD)"
out=$(bash "$GATE" 2>&1); rc=$?
verdict "same forged mandate, now accepted" "$out" "$rc"
pf=$(bash "$DRIVER" --preflight tRun --keepalive-id k1 2>&1); echo "  driver rc=$? :: $(printf '%s' "$pf" | head -1)"

# =========================================================================== DEFEAT 2
say "DEFEAT 2 — env-var shape: GOV_DEFAULT_BRANCH names a remote-tracking ref the run created"
reset; F=$(forge)
git update-ref refs/remotes/origin/fakedefault "$F"
assert_refs; out=$(GOV_DEFAULT_BRANCH=fakedefault bash "$GATE" 2>&1); rc=$?
verdict "the gate read the same env var the driver reads" "$out" "$rc"

# =========================================================================== DEFEAT 3
say "DEFEAT 3 — GOV_DEFAULT_BRANCH names nothing; recorded base is 40 zeros"
reset; sed -i "s/^base: .*/base: $(printf '0%.0s' $(seq 40))/" memory/builds/tRun/RUN.md; git add -A
assert_refs
out=$(bash "$GATE" 2>&1)
echo "  var UNSET      -> $(printf '%s' "$out" | grep -c 'check 9' || true) check-9 line(s)"
out=$(GOV_DEFAULT_BRANCH=nosuchref bash "$GATE" 2>&1); rc=$?
echo "  var=nosuchref  -> $(printf '%s' "$out" | grep -c 'check 9' || true) check-9 line(s)"
verdict "one env var disarms the only BASE assertion on the bar" "$out" "$rc"

# =========================================================================== DEFEAT 4
say "DEFEAT 4 — a clone with NO origin/HEAD (passive degradation, no attacker needed)"
reset; sed -i "s/^base: .*/base: $(printf '0%.0s' $(seq 40))/" memory/builds/tRun/RUN.md; git add -A
git update-ref -d --no-deref refs/remotes/origin/HEAD
assert_refs; out=$(bash "$GATE" 2>&1); rc=$?
verdict "recorded BASE is 40 zeros and the leg never looks" "$out" "$rc"
