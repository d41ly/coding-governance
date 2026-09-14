#!/usr/bin/env bash
# Runnable scenario suite for manifest-check.sh (spec: the manifest-ratchet design record, coding-governance §3).
# Run: bash skills/session-kickoff/manifest-check.test.sh    (exit 0 = all pass)
set -u
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null   # a runner's core.hooksPath/init.templateDir must not reach the throwaway repos
CHECK="$(cd "$(dirname "$0")" && pwd)/manifest-check.sh"
TMP=$(mktemp -d "${TMPDIR:-/tmp}/mfcheck.XXXXXX")
trap 'rm -rf "$TMP"' EXIT
pass=0; fail=0
echo 0 > "$TMP/.now"   # file-backed fake clock — stamp_line runs in subshells, so a plain
                       # variable would never advance and same-anchor re-stamps would no-op

# run <name> <repo> <want_exit> <want_grep|-> [args...]
run() {
  local name=$1 repo=$2 want=$3 pat=$4; shift 4
  local out got
  out=$(cd "$repo" && bash "$CHECK" "$@" 2>&1); got=$?
  if [ "$got" != "$want" ]; then
    echo "FAIL $name (exit $got, want $want)"; printf '%s\n' "$out" | sed 's/^/    /'; fail=$((fail+1)); return
  fi
  if printf '%s' "$out" | grep -q 'fatal:'; then   # the no-raw-fatal contract holds on EVERY path
    echo "FAIL $name (raw git fatal leaked)"; printf '%s\n' "$out" | sed 's/^/    /'; fail=$((fail+1)); return
  fi
  if [ "$pat" != "-" ] && ! printf '%s' "$out" | grep -qF "$pat"; then
    echo "FAIL $name (output lacks '$pat')"; printf '%s\n' "$out" | sed 's/^/    /'; fail=$((fail+1)); return
  fi
  if [ "$pat" = "-" ] && printf '%s' "$out" | grep -vE '^(WARN:|NOTE:)' | grep -q .; then
    echo "FAIL $name (green run not silent-clean)"; printf '%s\n' "$out" | sed 's/^/    /'; fail=$((fail+1)); return
  fi
  echo "ok   $name"; pass=$((pass+1))
}

# runm <name> <repo> <want_exit> <pat>... — one invocation, many signatures. `run` takes a single
# pattern, and check 2's missing-key branches are three independent `||` statements over one block:
# they all fire on the same fixture, so re-running it once per pattern would triple the git work to
# assert what one run already emitted.
runm() {
  local name=$1 repo=$2 want=$3; shift 3
  local out got pt bad=0
  out=$(cd "$repo" && bash "$CHECK" 2>&1); got=$?
  if [ "$got" != "$want" ]; then
    echo "FAIL $name (exit $got, want $want)"; printf '%s\n' "$out" | sed 's/^/    /'; fail=$((fail+1)); return
  fi
  if printf '%s' "$out" | grep -q 'fatal:'; then
    echo "FAIL $name (raw git fatal leaked)"; printf '%s\n' "$out" | sed 's/^/    /'; fail=$((fail+1)); return
  fi
  for pt in "$@"; do
    printf '%s' "$out" | grep -qF "$pt" || { echo "FAIL $name (output lacks '$pt')"; bad=1; }
  done
  if [ "$bad" = 1 ]; then printf '%s\n' "$out" | sed 's/^/    /'; fail=$((fail+1)); return; fi
  echo "ok   $name"; pass=$((pass+1))
}

# Every mkrepo starts from a byte-identical base repo — so build it ONCE and copy per case,
# turning 36 `git init`+config+commit chains into 1. The suite's whole cost was repo
# construction (~3m of git process spawns on Windows); cp -r of a single-commit repo with no
# remotes/worktrees/alternates carries no absolute paths, so the copies are fully independent.
TEMPLATE="$TMP/.template"; mkdir -p "$TEMPLATE/docs"
git -C "$TEMPLATE" init -q -b main
git -C "$TEMPLATE" config user.email t@test; git -C "$TEMPLATE" config user.name t; git -C "$TEMPLATE" config commit.gpgsign false
git -C "$TEMPLATE" config core.autocrlf false
printf 'all:\n\ttrue\n' > "$TEMPLATE/Makefile"; echo gov > "$TEMPLATE/docs/GOV.md"
git -C "$TEMPLATE" add -A; git -C "$TEMPLATE" commit -qm base
mkrepo() { R="$TMP/$1"; cp -r "$TEMPLATE" "$R"; }   # $1=name → sets R; a copy of the base repo (Makefile watch + docs/GOV.md anchor)

stamp_line() {
  local n; n=$(( $(cat "$TMP/.now") + 1 )); echo "$n" > "$TMP/.now"
  printf 'last-audit: 2026-07-12T12:%02d:%02d+00:00 @ %s' $((n/60)) $((n%60)) "$1"
}

write_manifest() { # $1=repo $2=sha $3=watch $4=vpaths [$5=marker] [$6=extra-body] [$7=last-body-change] [$8=extra audit-block line]
  local marker="${5:-kickoff-manifest: v1.4}"
  # The FIRST location `--locations` prints. The repo-root spelling this helper used to write is no
  # longer a discovery location, and most cases here call the checker with no path argument.
  mkdir -p "$1/memory/guides"
  cat > "$1/memory/guides/SESSION-KICKOFF.md" <<EOF
# Kickoff manifest — test
<!-- $marker · test instance -->
<!-- manifest-audit
$(stamp_line "$2")
watch: $3
verify-paths: $4
last-body-change: ${7:-$2}
${8:-}
-->
## §A
<!-- kickoff:task -->
> - **Title:** …
> - **Goal (1–2 sentences):** …
> - **IN scope:** …
> - **OUT / non-goals** (explicit cut-line): …
> - **Acceptance check** (the observation that proves THIS change — a test it adds, a gate it
>   moves, an observed behavior; *not* an unrelated green check): …
> - **Gates it must pass:** …
<!-- /kickoff:task -->
## §B
gate fence:
\`\`\`bash
make all
\`\`\`
${6:-}
EOF
}

restamp() { # $1=repo $2=sha — rewrite the last-audit line (datetime always advances)
  local nl; nl=$(stamp_line "$2")
  sed -i "s|^last-audit: .*|$nl|" "$1/memory/guides/SESSION-KICKOFF.md"
}

commit_all() { git -C "$1" add -A; git -C "$1" commit -qm "$2"; }
head_sha() { git -C "$1" rev-parse HEAD; }

# ---- 1 clean pass -------------------------------------------------------
mkrepo clean
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
run "clean pass → 0, silent" "$R" 0 -

# ---- 2 surviving placeholder → C1 --------------------------------------
mkrepo c1
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md" "" "{{GATE_COMMANDS}}"
commit_all "$R" manifest
run "surviving {{PLACEHOLDER}} → C1" "$R" 1 "unfilled {{PLACEHOLDER}} survives in"

# ---- 3 Actions/Go-template braces are NOT placeholders ------------------
mkrepo c1ok
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md" "" 'echo ${{ secrets.X }} && docker inspect --format {{.State.Status}} c'
commit_all "$R" manifest
run "\${{ secrets }} / {{.Go}} in fence → 0" "$R" 0 -

# ---- 4 missing block (v1.1 marker) → C2 ---------------------------------
mkrepo noblock
mkdir -p "$R/memory/guides"; cat > "$R/memory/guides/SESSION-KICKOFF.md" <<'EOF'
# manifest
<!-- kickoff-manifest: v1.1 · test -->
body only
EOF
commit_all "$R" manifest
run "missing audit block → C2" "$R" 1 "no manifest-audit block in"

# ---- 5 empty watch value → C2 -------------------------------------------
mkrepo emptywatch
write_manifest "$R" "$(head_sha "$R")" " ; " "docs/GOV.md"
commit_all "$R" manifest
run "empty watch value → C2" "$R" 1 "watch: holds no usable pathspec after splitting — list the gate-defining pathspecs (a missing watch silently disables the drift check)."

# ---- 6 bogus sha → C3 unknown -------------------------------------------
mkrepo bogus
write_manifest "$R" "0123456789abcdef0123456789abcdef01234567" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
run "bogus sha → C3 unknown" "$R" 1 "is unknown to this repo — the stamp is foreign or predates a history rewrite; re-verify §B, then re-stamp last-audit '<ISO datetime> @ <sha>' with"

# ---- 7 valid-but-non-ancestor sha → C3 second remedy --------------------
mkrepo nonanc
git -C "$R" checkout -qb side; echo s > "$R/side.txt"; commit_all "$R" side; SIDE=$(head_sha "$R")
git -C "$R" checkout -q main
write_manifest "$R" "$SIDE" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
run "non-ancestor sha → C3 rewrite remedy" "$R" 1 "is not an ancestor of HEAD — history was rewritten or the stamp was squash-merged; re-verify §B, then re-stamp last-audit '<ISO datetime> @ <sha>' with"

# ---- 8 dead verify-path → C4 --------------------------------------------
mkrepo deadvp
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GONE.md"
commit_all "$R" manifest
run "dead verify-path → C4" "$R" 1 "' is not tracked content — the tree restructured or the anchor is dead; fix the path (or the §B pointer it anchors)."

# ---- 9 untracked file at verify-path → C4 -------------------------------
mkrepo untrackvp
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/LOCAL.md"
commit_all "$R" manifest
echo local > "$R/docs/LOCAL.md"   # exists on disk, never tracked
run "untracked verify-path → C4" "$R" 1 "is not tracked content"

# ---- 10 watch commit without re-stamp → C5 ------------------------------
mkrepo drift
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
printf 'all:\n\ttrue\nx:\n\ttrue\n' > "$R/Makefile"; commit_all "$R" "watch drift"
run "watch commit, no re-stamp → C5" "$R" 1 "watched files changed since last-audit with no re-stamp at/after the change"

# ---- 11 bundled watch+re-stamp commit → 0 (W==S reflexive) --------------
mkrepo bundle
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
printf 'all:\n\ttrue\ny:\n\ttrue\n' > "$R/Makefile"
restamp "$R" "$(head_sha "$R")"          # stamps the PARENT sha — the one-commit remedy
commit_all "$R" "bundle: drift + re-stamp"
run "bundled drift+re-stamp → 0" "$R" 0 -

# ---- 12 follow-up re-stamp (frozen anchor, datetime moves) → 0 ----------
mkrepo followup
ANCHOR=$(head_sha "$R")
write_manifest "$R" "$ANCHOR" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
printf 'all:\n\ttrue\nz:\n\ttrue\n' > "$R/Makefile"; commit_all "$R" "watch drift"
restamp "$R" "$ANCHOR"                    # same anchor sha, new datetime — must still commit
commit_all "$R" "follow-up re-stamp"
run "follow-up re-stamp, frozen anchor → 0" "$R" 0 -

# ---- 13 cross-mode pair: staged bundle → C5s green, then full C5 green --
mkrepo xmode
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
printf 'all:\n\ttrue\nw:\n\ttrue\n' > "$R/Makefile"
restamp "$R" "$(head_sha "$R")"
git -C "$R" add -A
run "cross-mode: staged bundle → C5s green" "$R" 0 - --staged
commit_all "$R" "bundle"
run "cross-mode: same commit → full C5 green" "$R" 0 -

# ---- 14 true-merge laundering probe → RED, then post-merge re-stamp → 0 -
mkrepo laundering
ANCHOR=$(head_sha "$R")
write_manifest "$R" "$ANCHOR" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
git -C "$R" checkout -qb feat
printf 'all:\n\ttrue\nfeat:\n\ttrue\n' > "$R/Makefile"; commit_all "$R" "unaudited drift on feat"
git -C "$R" checkout -q main
restamp "$R" "$ANCHOR"; commit_all "$R" "independent mainline re-stamp"   # pre-merge stamp
git -C "$R" merge -q --no-ff --no-edit feat
run "true-merge laundering → C5 RED" "$R" 1 "check 5 FAILED"
restamp "$R" "$(head_sha "$R")"; commit_all "$R" "post-merge fresh audit"
run "post-merge re-stamp → 0" "$R" 0 -

# ---- 15 no-remote squash-merge with merge-base stamp → 0 ----------------
mkrepo squash
MAIN0=$(head_sha "$R")
write_manifest "$R" "$MAIN0" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
MB=$(head_sha "$R")                       # branch point = merge-base vs main
git -C "$R" checkout -qb work
printf 'all:\n\ttrue\nsq:\n\ttrue\n' > "$R/Makefile"
restamp "$R" "$MB"                        # §2 stamp rule: merge-base, not branch HEAD
commit_all "$R" "bundle on branch"
git -C "$R" checkout -q main
git -C "$R" merge -q --squash work >/dev/null
git -C "$R" commit -qm "squashed landing"
run "no-remote squash landing → 0 (C3+C5 hold)" "$R" 0 -

# ---- 16 merged orphan-root watch history → clean fail, no raw fatal -----
mkrepo orphan
write_manifest "$R" "$(head_sha "$R")" "Makefile; tools/" "docs/GOV.md"
mkdir -p "$R/tools"; echo t > "$R/tools/seed.txt"   # keeps the tools/ watch pathspec alive (C6)
commit_all "$R" manifest
git -C "$R" checkout -q --orphan lonely
git -C "$R" rm -qrf . >/dev/null 2>&1
mkdir -p "$R/tools"; echo o > "$R/tools/orphan.txt"   # watched path, no overlap with main
git -C "$R" add -A; git -C "$R" commit -qm "orphan root touching watch"
git -C "$R" checkout -q main
git -C "$R" merge -q --no-edit --allow-unrelated-histories lonely
run "merged orphan watch root → clean C5 red (no fatal)" "$R" 1 "check 5 FAILED"

# ---- 17 staged watch without staged stamp → C5s -------------------------
mkrepo stagedbad
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
printf 'all:\n\ttrue\nsb:\n\ttrue\n' > "$R/Makefile"; git -C "$R" add Makefile
run "staged watch, no staged stamp → C5s" "$R" 1 "staged changes touch watched files" --staged

# ---- 18 staged watch + unrelated manifest edit → C5s --------------------
mkrepo stagedside
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
printf 'all:\n\ttrue\nss:\n\ttrue\n' > "$R/Makefile"
printf '\nunrelated trap note\n' >> "$R/SESSION-KICKOFF.md"     # manifest edit, stamp untouched
git -C "$R" add -A
run "staged watch + unrelated manifest edit → C5s" "$R" 1 "check 5 FAILED" --staged

# ---- 19 trailing semicolon in watch → parsed clean → 0 ------------------
mkrepo trailsemi
write_manifest "$R" "$(head_sha "$R")" "Makefile;" "docs/GOV.md;"
commit_all "$R" manifest
run "trailing ';' → parsed clean, 0" "$R" 0 -

# ---- 20 dead watch pathspec → C6 ----------------------------------------
mkrepo deadwatch
write_manifest "$R" "$(head_sha "$R")" "gone-dir/" "docs/GOV.md"
commit_all "$R" manifest
run "dead watch pathspec → C6" "$R" 1 "' matches no tracked file — update the watch list to the restructured paths."

# ---- 21 broad watch pathspec → breadth WARN, still 0 --------------------
mkrepo broad
mkdir -p "$R/bulk"; for i in $(seq 1 101); do echo x > "$R/bulk/f$i.txt"; done
commit_all "$R" bulk
write_manifest "$R" "$(head_sha "$R")" "bulk/; Makefile" "docs/GOV.md"
commit_all "$R" manifest
run "watch matches 101 files → WARN + 0" "$R" 0 "WARN: watch pathspec"

# ---- 22 unmanaged manifest (no marker) → NOTE + 0 -----------------------
mkrepo unmanaged
mkdir -p "$R/memory/guides"; cat > "$R/memory/guides/SESSION-KICKOFF.md" <<'EOF'
# Session kickoff template (prototype — deliberately unmanaged)
No marker here; stable preamble; stream map.
EOF
commit_all "$R" manifest
run "unmanaged manifest → NOTE + 0" "$R" 0 "NOTE:"

# ---- 23 v1.0 marker, no block → C2 with retrofit ------------------------
mkrepo v10
mkdir -p "$R/memory/guides"; cat > "$R/memory/guides/SESSION-KICKOFF.md" <<'EOF'
# manifest
<!-- kickoff-manifest: v1.0 · instantiated from coding-governance -->
old body
EOF
commit_all "$R" manifest
run "v1.0 marker, no block → C2 retrofit" "$R" 1 "marker to v1.4 LAST"

# ---- 24 v1.0 marker WITH valid block → version WARN, 0 ------------------
mkrepo v10block
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md" "kickoff-manifest: v1.0"
commit_all "$R" manifest
run "v1.0 + valid block → WARN + 0" "$R" 0 "WARN: manifest format v1.0"

# ---- 25 shallow clone → WARN + skip C3/C5 → 0 ---------------------------
mkrepo shallowsrc
ANCHOR=$(head_sha "$R")
write_manifest "$R" "$ANCHOR" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
printf 'all:\n\ttrue\nmore:\n\ttrue\n' > "$R/Makefile"; commit_all "$R" more   # depth-1 clone misses ANCHOR
git clone -q --depth 1 "file://$R" "$TMP/shallow" 2>/dev/null
run "shallow clone → WARN, C3+C5 skipped, 0" "$TMP/shallow" 0 "WARN: shallow clone"

# ---- 26 exit 2 contract --------------------------------------------------
mkdir -p "$TMP/nogit"
run "non-repo → exit 2" "$TMP/nogit" 2 "env ERROR"
mkrepo nomanifest
run "no manifest → exit 2" "$R" 2 "env ERROR"

# ---- 27 manifest rename after unaudited drift → still C5 RED -------------
mkrepo rename
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
printf 'all:\n\ttrue\nrn:\n\ttrue\n' > "$R/Makefile"; commit_all "$R" "unaudited drift"
git -C "$R" mv memory/guides/SESSION-KICKOFF.md .claude/SESSION-KICKOFF.md 2>/dev/null   || { mkdir -p "$R/.claude"; git -C "$R" mv memory/guides/SESSION-KICKOFF.md .claude/SESSION-KICKOFF.md; }
commit_all "$R" "pure rename of the manifest"
run "manifest renamed after drift → C5 RED (no laundering)" "$R" 1 "check 5 FAILED"

# ---- 28 body decoy last-audit line does not count as a re-stamp ----------
mkrepo decoy
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md" "" 'last-audit: decoy @ 0000000000000000000000000000000000000000'
commit_all "$R" manifest
printf 'all:\n\ttrue\ndc:\n\ttrue\n' > "$R/Makefile"; commit_all "$R" "unaudited drift"
sed -i 's/^last-audit: decoy @ 0\{40\}/last-audit: decoy2 @ 0000000000000000000000000000000000000000/' "$R/memory/guides/SESSION-KICKOFF.md"
commit_all "$R" "edit only the body decoy line"
run "body decoy edit after drift → C5 RED" "$R" 1 "check 5 FAILED"

# ---- 29 block reorder without value change does not count ----------------
mkrepo reorder
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
printf 'all:\n\ttrue\nro:\n\ttrue\n' > "$R/Makefile"; commit_all "$R" "unaudited drift"
# The resolver, INLINE. This kit is copy-installed as a standalone directory, so `../lib/` does
# not exist in an adopting repo. The block below is byte-identical to tools/lib/resolve-python.sh
# and tools/lib/resolve-python.test.sh reds if any copy drifts.
# >>> resolve_python — canonical copy: tools/lib/resolve-python.sh (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  _rp_tried=""
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    if "$_rp_c" -c "import sys" >/dev/null 2>&1; then
      printf '%s\n' "$_rp_c"
      return 0
    fi
  done
  {
    echo "resolve_python: no usable python launcher. Each candidate was RUN with -c 'import sys' and"
    echo "resolve_python: none exited 0 — being on PATH is not evidence (the Microsoft Store python3"
    echo "resolve_python: stub answers \`command -v\` and exits 9009 without running anything)."
    echo "resolve_python: tried:$_rp_tried"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and did not run."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and did not run. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
  } >&2
  return 1
}
# <<< resolve_python
PYBIN=$(resolve_python) || { echo "manifest-check.test: no usable python"; exit 2; }
"$PYBIN" - "$R/memory/guides/SESSION-KICKOFF.md" <<'PY'
import sys
p = sys.argv[1]; lines = open(p, encoding='utf-8').read().split('\n')
la = next(i for i,l in enumerate(lines) if l.startswith('last-audit:'))
w  = next(i for i,l in enumerate(lines) if l.startswith('watch:'))
lines[la], lines[w] = lines[w], lines[la]      # swap the two lines, values untouched
open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines))
PY
if git -C "$R" diff --quiet -- memory/guides/SESSION-KICKOFF.md; then
  echo "FAIL block reorder after drift → C5 RED (mutation never landed — python missing?)"; fail=$((fail+1))
else
  commit_all "$R" "reorder block lines only"
  run "block reorder after drift → C5 RED" "$R" 1 "check 5 FAILED"
fi

# ---- 30 staged decoy line does not satisfy C5s ---------------------------
mkrepo stageddecoy
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
printf 'all:\n\ttrue\nsd:\n\ttrue\n' > "$R/Makefile"
printf 'last-audit: fake @ 0000000000000000000000000000000000000000\n' >> "$R/SESSION-KICKOFF.md"
git -C "$R" add -A
run "staged body decoy → C5s RED" "$R" 1 "check 5 FAILED" --staged

# ---- 31 repo-escaping watch pathspec → C6 red, no fatal ------------------
mkrepo escape
write_manifest "$R" "$(head_sha "$R")" "../outside; Makefile" "docs/GOV.md"
commit_all "$R" manifest
run "repo-escaping watch pathspec → C6, no fatal" "$R" 1 "check 6 FAILED"

# ---- 32 unborn HEAD (orphan checkout) → guided C3, no fatal --------------
mkrepo unborn
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
git -C "$R" checkout -q --orphan void
run "unborn HEAD → C3 'no commits', no fatal" "$R" 1 "HEAD has no commits on this branch — make the first commit, then re-verify §B and re-stamp last-audit at it."

# ---- 33 malformed datetime → C2 ------------------------------------------
mkrepo baddate
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
sed -i 's/^last-audit: [^@]*@/last-audit: banana breakfast @/' "$R/memory/guides/SESSION-KICKOFF.md"
commit_all "$R" manifest
run "malformed datetime → C2" "$R" 1 "') — want '<ISO-8601 datetime with offset> @ <full 40-hex sha>'."

# ---- 34 relative path arg from a subdirectory ----------------------------
mkrepo subdir
mkdir -p "$R/docs"
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
mv "$R/memory/guides/SESSION-KICKOFF.md" "$R/docs/SESSION-KICKOFF.md"
commit_all "$R" manifest
run "relative arg from subdir resolves" "$R/docs" 0 - "SESSION-KICKOFF.md"

# ---- 34b outside-repo path argument → env error 2 (relative ../ and absolute)
mkrepo escapearg
echo x > "$TMP/SESSION-KICKOFF.md"          # sibling of the repo, outside it
run "relative ../ arg escaping repo → 2" "$R" 2 "resolves outside" "../SESSION-KICKOFF.md"
run "absolute arg outside repo → 2" "$R" 2 "resolves outside" "$TMP/SESSION-KICKOFF.md"
rm -f "$TMP/SESSION-KICKOFF.md"

# ---- 36 two audit blocks → C2 'exactly one' ------------------------------
# The block is found by a `grep -c` and read by an awk that STOPS at the first `-->`. With two
# blocks the second one is unreachable — every value silently comes from the first — so a manifest
# that grew a second block during a merge would enforce against half of itself.
mkrepo twoblocks
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
cat >> "$R/memory/guides/SESSION-KICKOFF.md" <<'EOF'
<!-- manifest-audit
last-audit: 2026-07-12T13:00:00+00:00 @ 0000000000000000000000000000000000000000
watch: Makefile
verify-paths: docs/GOV.md
-->
EOF
commit_all "$R" manifest
run "two audit blocks → C2 'exactly one'" "$R" 1 "— exactly one is allowed; merge them."

# ---- 37 block present, all three keys absent → C2 x3 ---------------------
# The three key checks are independent `||` statements, so ONE fixture fires all three. A block with
# no keys is the shape a hand-written retrofit produces, and each missing key disables a different
# part of the gate: no watch is a silent false-green on drift, no verify-paths is a dead anchor set,
# no last-audit is no anchor at all.
mkrepo nokeys
mkdir -p "$R/memory/guides"; cat > "$R/memory/guides/SESSION-KICKOFF.md" <<'EOF'
# manifest
<!-- kickoff-manifest: v1.1 · test -->
<!-- manifest-audit
(the retrofit added the fences and forgot every key)
-->
## §B
EOF
commit_all "$R" manifest
runm "audit block with no keys → C2 names all three" "$R" 1 \
  "manifest-audit block lacks a last-audit value — stamp '<ISO datetime> @ <full sha>' after verifying §B." \
  "manifest-audit block lacks a watch value — list the gate-defining pathspecs (a missing watch silently disables the drift check)." \
  "manifest-audit block lacks a verify-paths value — list the 2-3 anchor paths."

# ---- 38 verify-paths that splits to nothing → C2 ------------------------
# The watch twin of this is scenario 5. Both matter: the split DROPS empty elements, so a value that
# is nothing but separators is non-empty as a string and empty as a list — two different branches,
# and the array one is the branch that stops `git ls-files` from being handed ''.
mkrepo emptyvp
write_manifest "$R" "$(head_sha "$R")" "Makefile" " ; "
commit_all "$R" manifest
run "verify-paths splits to nothing → C2" "$R" 1 \
  "verify-paths: holds no usable path after splitting — list the 2-3 anchor paths."

# ---- 35 unit-branch: bundle at merge-base anchor, then same-anchor re-stamp
mkrepo branchunit
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
MB=$(head_sha "$R")                       # branch point = merge-base vs main
git -C "$R" checkout -qb unit
printf 'all:\n\ttrue\nbu:\n\ttrue\n' > "$R/Makefile"
restamp "$R" "$MB"; commit_all "$R" "bundle on unit branch"
restamp "$R" "$MB"; commit_all "$R" "second same-anchor re-stamp (datetime only)"
n=$(git -C "$R" rev-list --count HEAD)
if [ "$n" -ne 4 ]; then echo "FAIL branch same-anchor re-stamps (want 4 commits, got $n — a re-stamp no-oped)"; fail=$((fail+1)); else
  run "unit branch: merge-base bundle + same-anchor re-stamp → 0" "$R" 0 -
fi

# ---- C7 size, C8 line length, C9 maintenance stall ---------------------------------------------
# Every arm below asserts the branch's OWN failure sentence, which is what the harness meta-gate
# counts. The sentences lead with literal prose and put the measured values LAST, because an
# interpolation splits a message into runs and a run under twelve characters cannot be asserted on.

# C7 — the limit arrives by environment so the fixture need not be 25 KiB. That override exists for
# this arm and says so in the failure text; it is not an adopter escape hatch.
mkrepo c7; write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"; commit_all "$R" manifest
out=$(cd "$R" && MAX_MANIFEST_BYTES=200 bash "$CHECK" 2>&1); got=$?
{ [ "$got" = 1 ] && printf '%s' "$out" | grep -qF "the manifest is over its size limit and must be trimmed, not have the limit raised"; } \
  && { echo "ok   C7 oversize manifest → check 7"; pass=$((pass+1)); } \
  || { echo "FAIL C7 oversize manifest → check 7"; printf '%s\n' "$out" | sed 's/^/    /'; fail=$((fail+1)); }
# and the same manifest passes under the real limit — the arm above is not passing by finding nothing
run "C7 a normal manifest is under the limit" "$R" 0 -

# C8 — a long BODY line reds; the audit block and fenced blocks do not. The exemption arm is the one
# that matters: the watch list is one machine-maintained line that grows as pathspecs are added.
mkrepo c8
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md" "" "$(printf 'x%.0s' $(seq 1 450))"
commit_all "$R" manifest
run "C8 an over-long body line → check 8" "$R" 1 "a manifest line is over the 400-byte limit; wrap the prose or move the detail out"
mkrepo c8b
LONGWATCH="Makefile$(printf '; docs/GOV.md%.0s' $(seq 1 40))"
write_manifest "$R" "$(head_sha "$R")" "$LONGWATCH" "docs/GOV.md"; commit_all "$R" manifest
run "C8 exempts the audit block's own long watch line" "$R" 0 -

# C2 — the fourth key. Absent is a NAMED failure carrying the retrofit instruction, never a skip.
mkrepo c2k; write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"; commit_all "$R" manifest
sed -i '/^last-body-change:/d' "$R/memory/guides/SESSION-KICKOFF.md"; commit_all "$R" "drop the key"
run "C2 a missing last-body-change is named" "$R" 1 "manifest-audit block lacks a last-body-change value — add the full sha of the commit where this manifest's BODY was last genuinely revised; it is what check 9 measures the stall against."

# C9 — the four ways a recorded baseline can be unusable, then the two thresholds.
mkrepo c9a; write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md" "" "" "not-a-sha"
commit_all "$R" manifest
run "C9 a malformed baseline sha is named" "$R" 1 "last-body-change is not a full 40-hex sha, so the stall check has no baseline to measure from: '"

mkrepo c9b; write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md" "" "" "0000000000000000000000000000000000000000"
commit_all "$R" manifest
run "C9 a baseline unknown to the repo is named" "$R" 1 "last-body-change names a commit unknown to this repository, so the stall baseline is foreign or predates a history rewrite"

# THE ARM THE PREVIOUS DESIGN COULD NOT SATISFY. A path-scoped log reports a `git mv` as an ADD, so a
# history walk read a relocated manifest as freshly created. A recorded baseline is indifferent to
# the rename, and this asserts that indifference rather than asserting the walk was fixed.
mkrepo c9r; write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"; commit_all "$R" manifest
mkdir -p "$R/.claude"; git -C "$R" mv memory/guides/SESSION-KICKOFF.md .claude/SESSION-KICKOFF.md
commit_all "$R" "relocate the manifest"
run "C9 survives a git mv of the manifest" "$R" 0 -

# A baseline on a side branch is real but unreachable from HEAD — the squash-merge shape.
mkrepo c9anc
git -C "$R" checkout -qb side2; echo s2 > "$R/s2.txt"; commit_all "$R" side2; SIDE2=$(head_sha "$R")
git -C "$R" checkout -q main
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md" "" "" "$SIDE2"
commit_all "$R" manifest
run "C9 a non-ancestor baseline is named" "$R" 1 "last-body-change is not an ancestor of HEAD, so the stall baseline was squash-merged or rewritten and measures nothing"

# THE COMMIT THRESHOLD. Ten non-merge commits touching a watched pathspec since the baseline. The
# manifest is re-stamped each time so C5 stays green and C9 is the only thing this fixture measures.
mkrepo c9n
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
commit_all "$R" manifest
BASE9=$(head_sha "$R")
sed -i "s|^last-body-change: .*|last-body-change: $BASE9|" "$R/memory/guides/SESSION-KICKOFF.md"
commit_all "$R" rebaseline
for i in $(seq 1 11); do
  printf 'all:\n\ttrue\nr%s:\n\ttrue\n' "$i" > "$R/Makefile"
  restamp "$R" "$(head_sha "$R")"
  commit_all "$R" "watched churn $i"
done
run "C9 ten or more watched commits since the baseline" "$R" 1 "the manifest body has not changed across ten or more watched commits, so its front-loaded claims are drifting unverified; re-read §B and advance last-body-change to a current sha"

# THE ELAPSED-TIME THRESHOLD, with fewer than ten commits so only the age arm can fire. The fixture
# AGES the baseline commit rather than waiting: committer date is what C9 reads, because a rebase
# preserves author date and the question is when this history last moved.
mkrepo c9age
export GIT_COMMITTER_DATE="2025-01-01T00:00:00 +0000" GIT_AUTHOR_DATE="2025-01-01T00:00:00 +0000"
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
commit_all "$R" "aged manifest"
AGED=$(head_sha "$R")
unset GIT_COMMITTER_DATE GIT_AUTHOR_DATE
sed -i "s|^last-body-change: .*|last-body-change: $AGED|" "$R/memory/guides/SESSION-KICKOFF.md"
restamp "$R" "$AGED"; commit_all "$R" rebaseline
run "C9 three months or more since the baseline" "$R" 1 "the manifest body has not changed in three months or more, so its front-loaded claims are drifting unverified; re-read §B and advance last-body-change to a current sha"

# ---- C10 the sealed task region -----------------------------------------------------------------
# Absence is a NAMED failure, never a skip: every manifest written before this format version has no
# region at all, so a skip would make the seal dormant in exactly the population it exists for.
mkrepo c10a; write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"; commit_all "$R" manifest
python_del() { grep -v '<!-- kickoff:task -->' "$1" | grep -v '<!-- /kickoff:task -->' > "$1.t" && mv "$1.t" "$1"; }
python_del "$R/memory/guides/SESSION-KICKOFF.md"; commit_all "$R" "strip the markers"
run "C10 an absent sealed region is named" "$R" 1 "the manifest carries no sealed task region, so its §A field set is prose that any edit can silently change; paste the region printed by this script's --task-skeleton verb into §A of"

# ONE CHARACTER inside the region. This is the whole point of the unit: §A used to be prose that any
# edit could change silently.
mkrepo c10b; write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"; commit_all "$R" manifest
sed -i 's/\*\*IN scope:\*\*/**IN SCOPE:**/' "$R/memory/guides/SESSION-KICKOFF.md"; commit_all "$R" "edit the sealed region"
run "C10 a one-character edit inside the region is caught" "$R" 1 "the sealed task region differs from the task contract this script carries, and that region is not hand-authorable; restore it from the --task-skeleton verb rather than editing it in"

# A TRANSPOSED pair satisfies a count-only check. The lifted region() refuses it; this asserts that.
mkrepo c10c; write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"; commit_all "$R" manifest
sed -i 's|<!-- /kickoff:task -->|<!-- KICKOFF-CLOSE-PLACEHOLDER -->|; s|<!-- kickoff:task -->|<!-- /kickoff:task -->|; s|<!-- KICKOFF-CLOSE-PLACEHOLDER -->|<!-- kickoff:task -->|' "$R/memory/guides/SESSION-KICKOFF.md"
commit_all "$R" "transpose the markers"
run "C10 a transposed marker pair is named" "$R" 1 "the sealed task region's markers are malformed, so the region cannot be compared with the contract it copies; the pair must be exactly one open and one close, close after open, each alone on its line in"

# A CRLF manifest must not read as drift — the region() lifted here CR-normalises, and this is the
# arm that fails if that half is dropped.
mkrepo c10d; write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
sed -i 's/$/\r/' "$R/memory/guides/SESSION-KICKOFF.md"; commit_all "$R" manifest
run "C10 a CRLF manifest is not reported as region drift" "$R" 0 -

# THE SHIPPED SEED. gov-only: the template an adopter instantiates must carry the same region the
# checker enforces, or the seed produces a manifest the gate rejects on arrival.
SEED="$(cd "$(dirname "$CHECK")" && pwd)/MANIFEST-TEMPLATE.md"
if [ -f "$SEED" ]; then
  if diff -q <(bash "$CHECK" --task-skeleton) \
             <(awk '/<!-- kickoff:task -->/{f=1} f{print} /<!-- \/kickoff:task -->/{if(f)exit}' "$SEED") >/dev/null; then
    echo "ok   the shipped seed's region equals the constant"; pass=$((pass+1))
  else
    echo "FAIL the shipped seed's region equals the constant"; fail=$((fail+1))
  fi
  # EVERY KEY THE CARD VERB READS is in the seed's audit block, or a fresh adopter's every card reads
  # UNKNOWN with no version WARN to say why. The list is the verb's, spelled here once.
  seedblock=$(awk '/<!-- manifest-audit/{f=1;next} f&&/-->/{exit} f' "$SEED")
  for k in registry; do
    if printf '%s\n' "$seedblock" | grep -qE "^[[:space:]]*$k:"; then
      echo "ok   the shipped seed's audit block carries the card key '$k:'"; pass=$((pass+1))
    else
      echo "FAIL the shipped seed's audit block carries the card key '$k:'"; fail=$((fail+1))
    fi
  done
fi

# ---- C11 the per-bullet traps cap ---------------------------------------------------------------
TRAPS_OK='
### Environment traps worth front-loading

- a short trap, well under the cap.
- another short one.
'
TRAPS_BIG="
### Environment traps worth front-loading

- a short trap, well under the cap.
- $(printf 'y%.0s' $(seq 1 450))
"
mkrepo c11a; write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md" "" "$TRAPS_OK"
commit_all "$R" manifest
run "C11 short traps bullets pass" "$R" 0 -

mkrepo c11b; write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md" "" "$TRAPS_BIG"
commit_all "$R" manifest
run "C11 an over-cap traps bullet is named" "$R" 1 "an environment-traps bullet is over the 400-byte cap; the template asks for one line each with the detail linked out, and a record under the memory tree is where the detail belongs"

# The cap is scoped to the traps SECTION. A long bullet elsewhere in §B is C8's business (per LINE),
# not C11's (per BULLET) — without the section scope C11 would silently police the whole document.
mkrepo c11c
write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md" "" "
### Some other section

- $(printf 'z%.0s' $(seq 1 200))
  $(printf 'z%.0s' $(seq 1 200))
  $(printf 'z%.0s' $(seq 1 200))
"
commit_all "$R" manifest
run "C11 does not police bullets outside the traps section" "$R" 0 -

# ---- the orientation card (--card --write | --replay | --path) ------------------------------------
# Every arm runs in a scratch CLONE of the repository that hosts the checker, inside a LINKED
# WORKTREE of that clone — never in this tree, because the card home is the git common dir every
# worktree on the node shares, and a fixture card left there is one a sibling session trips on. The
# last arm lists this repository's real common dir and asserts the suite left nothing in it.
# Session ids carry a per-run nonce so that listing can tell the suite's cards from anyone else's.
NONCE="mfc$$"
GOVROOT=$(git -C "$(dirname "$CHECK")" rev-parse --show-toplevel)
CCLONE="$TMP/card-clone"; CWT="$TMP/card-wt"
git clone -q --local "$GOVROOT" "$CCLONE" && git -C "$CCLONE" worktree add -q "$CWT" -b card-wt \
  || { echo "FAIL card fixture: cannot clone $GOVROOT and add a worktree under $TMP"; fail=$((fail+1)); }
CARD_HOME="$CCLONE/.git/orientation"
CUSER="${USERNAME:-${USER:-}}"

# run_card <name> <repo> <want_exit> <want_grep|-> [args...] — stdout+stderr to $CARD_OUT, stdin
# from /dev/null so the hook channel is provably empty; `run` cannot serve here because it strips
# the trailing newline AC1 compares, and a card's bytes are the thing under test.
CARD_OUT="$TMP/card.out"
run_card() {
  local name=$1 repo=$2 want=$3 pat=$4; shift 4
  local got
  (cd "$repo" && bash "$CHECK" "$@" </dev/null > "$CARD_OUT" 2>&1); got=$?
  if [ "$got" != "$want" ]; then
    echo "FAIL $name (exit $got, want $want)"; sed 's/^/    /' "$CARD_OUT"; fail=$((fail+1)); return 1
  fi
  if grep -q 'fatal:' "$CARD_OUT"; then
    echo "FAIL $name (raw git fatal leaked)"; sed 's/^/    /' "$CARD_OUT"; fail=$((fail+1)); return 1
  fi
  if [ "$pat" != "-" ] && ! grep -qF -- "$pat" "$CARD_OUT"; then
    echo "FAIL $name (output lacks '$pat')"; sed 's/^/    /' "$CARD_OUT"; fail=$((fail+1)); return 1
  fi
  echo "ok   $name"; pass=$((pass+1))
}
# check_eq <name> <want> <got>
check_eq() {
  if [ "$2" = "$3" ]; then echo "ok   $1"; pass=$((pass+1)); else
    echo "FAIL $1"; printf '    want: %s\n    got:  %s\n' "$2" "$3"; fail=$((fail+1)); fi
}
read_cell() { grep -m1 "^$1 — " "$CARD_HOME/$2.md"; }   # $1=cell $2=session id

# Two fixture registries. REG1: the Remote column repeats the user on EVERY row (a row-wide match
# hits all three), the matching Machine/user cell is BACKTICKED (equality after stripping), one
# decoy row carries the user after an `@` (never a match), a registry-shaped table sits BEFORE the
# heading with a matching row (`y`), and a second registry-shaped table sits AFTER the first one
# under another heading with a matching row (`z`). Exactly one row may answer, and it is `q`.
# REG2: the same Remote column, and no Machine/user cell matches.
cat > "$CWT/REG1.md" <<EOF
# fixture registry

| Tag | Machine/user | Primary tree | Remote |
|-----|--------------|--------------|--------|
| \`y\` | $CUSER | \`/x\` | \`origin\` (github \`$CUSER/repo\`) |

## Node registry

| Tag | Machine/user | Primary tree | Remote |
|-----|--------------|--------------|--------|
| \`p\` | someone-else @ \`HOST1\` | \`/x\` | \`origin\` (github \`$CUSER/repo\`) |
| \`q\` | \`$CUSER\` | \`/x\` | \`origin\` (github \`$CUSER/repo\`) |
| \`r\` | other @ \`$CUSER\` | \`/x\` | \`origin\` (github \`$CUSER/repo\`) |

## §2 — Nodes

| Tag | Machine/user | Primary tree | Remote |
|-----|--------------|--------------|--------|
| \`z\` | $CUSER @ \`HOST2\` | \`/x\` | \`origin\` (github \`$CUSER/repo\`) |
EOF
cat > "$CWT/REG2.md" <<EOF
## Node registry

| Tag | Machine/user | Primary tree | Remote |
|-----|--------------|--------------|--------|
| \`p\` | ${CUSER}x | \`/x\` | \`origin\` (github \`$CUSER/repo\`) |
| \`q\` | x$CUSER @ \`HOST\` | \`/x\` | \`origin\` (github \`$CUSER/repo\`) |
EOF

# AC1 — the write verb, in the linked worktree, with the manifest naming the real registry.
write_manifest "$CWT" "$(git -C "$CWT" rev-parse HEAD)" "AGENTS.md" "AGENTS.md" "" "" "" "registry: AGENTS.md"
t0=$(date +%s)
run_card "AC1 --card --write writes the card and prints it" "$CWT" 0 "orientation — $NONCE-t1 · written " --card --write --session "$NONCE-t1"
t1=$(date +%s)
[ -f "$CARD_HOME/$NONCE-t1.md" ] && { echo "ok   AC1 the card is at <common-dir>/orientation/<sid>.md (wall $((t1-t0))s)"; pass=$((pass+1)); } \
  || { echo "FAIL AC1 the card is at <common-dir>/orientation/<sid>.md"; ls "$CCLONE/.git" | sed 's/^/    /'; fail=$((fail+1)); }
if cmp -s "$CARD_OUT" "$CARD_HOME/$NONCE-t1.md"; then echo "ok   AC1 stdout equals the card's bytes"; pass=$((pass+1)); else
  echo "FAIL AC1 stdout equals the card's bytes"; diff "$CARD_OUT" "$CARD_HOME/$NONCE-t1.md" | sed 's/^/    /'; fail=$((fail+1)); fi

# AC2 — every startup cell, each derived by the suite from git and compared to the card.
wt_top=$(git -C "$CWT" rev-parse --show-toplevel); wt_head=$(git -C "$CWT" rev-parse HEAD)
wt_dirty=$(git -C "$CWT" status --porcelain | wc -l | tr -d '[:space:]')
check_eq "AC2 tree — the toplevel in git's own spelling, worktree, branch, BASE, dirty count" \
  "tree — $wt_top · worktree · branch card-wt · BASE $wt_head · dirty $wt_dirty" "$(read_cell tree "$NONCE-t1")"
check_eq "AC2 worktrees — the count of git worktree list" \
  "worktrees — $(git -C "$CWT" worktree list | wc -l | tr -d '[:space:]')" "$(read_cell worktrees "$NONCE-t1")"
memroot=$(sed -n 's/^MEMORY_ROOT=//p' "$CWT/.memory-tree.conf" 2>/dev/null | head -1 | tr -d '"')
if [ -n "$memroot" ] && [ -f "$CWT/$memroot/LIVE.md" ]; then
  check_eq "AC2 live — the table rows of LIVE.md minus its header" \
    "live — LIVE.md · $(grep -c '^| \[' "$CWT/$memroot/LIVE.md") non-terminal builds" "$(read_cell live "$NONCE-t1")"
else
  echo "skip AC2 live — this tree declares no memory root with a LIVE.md, so the count arm has no oracle (AC10 covers the skipped: shape)"
fi
check_eq "AC2 recent — the five subjects of git log --oneline -5" \
  "$(git -C "$CWT" log --oneline -5)" "$(awk '/^recent —/{f=1;next} /^READY —/{exit} f' "$CARD_HOME/$NONCE-t1.md")"
check_eq "AC2 the card ends with the READY sentinel" "READY — none yet" "$(tail -1 "$CARD_HOME/$NONCE-t1.md")"
grep -qE "^orientation — $NONCE-t1 · written [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}[+-][0-9]{4} · by manifest-check.sh --card --write$" "$CARD_HOME/$NONCE-t1.md" \
  && { echo "ok   AC2 the header names the session, the ISO time and the writer verb"; pass=$((pass+1)); } \
  || { echo "FAIL AC2 the header names the session, the ISO time and the writer verb"; head -1 "$CARD_HOME/$NONCE-t1.md" | sed 's/^/    /'; fail=$((fail+1)); }
# Counted with tr, not grep: an MSYS grep handed a CR pattern matches EVERY line (measured: 12 of 12 on a LF card).
[ "$(tr -dc '\r' < "$CARD_HOME/$NONCE-t1.md" | wc -c | tr -d '[:space:]')" = 0 ] && { echo "ok   AC2 the card is LF"; pass=$((pass+1)); } || { echo "FAIL AC2 the card is LF"; fail=$((fail+1)); }

# AC3 — no session id on either channel, then a path-shaped one; nothing is written under any of them.
before=$(ls "$CARD_HOME" | wc -l | tr -d '[:space:]')
run_card "AC3 no id on stdin and no --session → exit 2 naming both channels" "$CWT" 2 "none in the JSON on stdin (the SessionStart hook's channel) and no --session <sid> given" --card --write
run_card "AC3 a session id carrying '..' is refused" "$CWT" 2 "carries '..' and is not joined into a path" --card --write --session "$NONCE-..-t3"
run_card "AC3 a session id carrying a path separator is refused" "$CWT" 2 "carries a path separator or a byte outside" --card --write --session "$NONCE/t3"
run_card "AC3 an empty --session value is refused" "$CWT" 2 "has no session id" --card --write --session ""
check_eq "AC3 the refused ids wrote nothing under orientation/" "$before" "$(ls "$CARD_HOME" | wc -l | tr -d '[:space:]')"
# The hook channel: the SessionStart JSON on stdin, no --session.
(cd "$CWT" && printf '{"session_id":"%s","hook_event_name":"SessionStart"}\n' "$NONCE-t2" | bash "$CHECK" --card --write > "$CARD_OUT" 2>&1); got=$?
[ "$got" = 0 ] && [ -f "$CARD_HOME/$NONCE-t2.md" ] && { echo "ok   AC3 the session id is read from the hook's JSON on stdin"; pass=$((pass+1)); } \
  || { echo "FAIL AC3 the session id is read from the hook's JSON on stdin (exit $got)"; sed 's/^/    /' "$CARD_OUT"; fail=$((fail+1)); }

# AC4 — the node cell: the real registry at HEAD, then the two fixtures, then no key at all.
if [ "$CUSER" = daily-agent ]; then
  check_eq "AC4 node — resolves this node from the real AGENTS.md" "node — a · daily-agent" "$(read_cell node "$NONCE-t1")"
else
  echo "skip AC4 the exact tag against the real AGENTS.md: this node's user is '$CUSER', and the row the spec names is node a's (the fixture arms below decide the predicate)"
fi
write_manifest "$CWT" "$wt_head" "AGENTS.md" "AGENTS.md" "" "" "" "registry: REG1.md"
run_card "AC4 --card --write against fixture registry REG1" "$CWT" 0 - --card --write --session "$NONCE-t4a"
check_eq "AC4 node — exactly one Machine/user cell matches, backticks stripped, first table only" "node — q · $CUSER" "$(read_cell node "$NONCE-t4a")"
write_manifest "$CWT" "$wt_head" "AGENTS.md" "AGENTS.md" "" "" "" "registry: REG2.md"
run_card "AC4 --card --write against fixture registry REG2" "$CWT" 0 - --card --write --session "$NONCE-t4b"
check_eq "AC4 node — no Machine/user cell matches, and the Remote column does not vote" "node — UNKNOWN: no Machine/user cell in REG2.md matches $CUSER" "$(read_cell node "$NONCE-t4b")"
write_manifest "$CWT" "$wt_head" "AGENTS.md" "AGENTS.md" "" "" "" "registry: NOPE.md"
run_card "AC4 --card --write against a registry that is not a file" "$CWT" 0 - --card --write --session "$NONCE-t4c"
check_eq "AC4 node — a registry path that is not a file is UNKNOWN, and the card still writes" "node — UNKNOWN: registry NOPE.md is not a file in this tree" "$(read_cell node "$NONCE-t4c")"
write_manifest "$CWT" "$wt_head" "AGENTS.md" "AGENTS.md"
run_card "AC4 --card --write with no registry key" "$CWT" 0 - --card --write --session "$NONCE-t4d"
check_eq "AC4 node — an absent registry key is UNKNOWN: no registry" "node — UNKNOWN: no registry" "$(read_cell node "$NONCE-t4d")"

# AC5 — replay: the stored bytes, one `now —` line, the file untouched; a missing card is written
# fresh under the replay's own name, node cell resolved.
cp "$CARD_HOME/$NONCE-t1.md" "$TMP/t1.before"
run_card "AC5 --card --replay prints the stored card" "$CWT" 0 "orientation — $NONCE-t1 · written " --card --replay --session "$NONCE-t1"
check_eq "AC5 replay = the stored bytes then exactly one now — line" \
  "$(cat "$TMP/t1.before"; printf 'now — HEAD %s · card-wt · dirty %s\n' "$wt_head" "$(git -C "$CWT" status --porcelain | wc -l | tr -d '[:space:]')")" "$(cat "$CARD_OUT")"
cmp -s "$TMP/t1.before" "$CARD_HOME/$NONCE-t1.md" && { echo "ok   AC5 the file on disk is byte-identical after the replay"; pass=$((pass+1)); } \
  || { echo "FAIL AC5 the file on disk is byte-identical after the replay"; fail=$((fail+1)); }
run_card "AC5 a second replay" "$CWT" 0 - --card --replay --session "$NONCE-t1"
check_eq "AC5 a second replay still prints exactly one now — line" "1" "$(grep -c '^now — ' "$CARD_OUT")"
write_manifest "$CWT" "$wt_head" "AGENTS.md" "AGENTS.md" "" "" "" "registry: REG1.md"
run_card "AC5 --card --replay for a session with no card writes one" "$CWT" 0 "orientation — $NONCE-t5 · written " --card --replay --session "$NONCE-t5"
grep -q "^orientation — $NONCE-t5 · written .* · by manifest-check.sh --card --replay$" "$CARD_HOME/$NONCE-t5.md" \
  && { echo "ok   AC5 the replay-written card names --card --replay as its writer"; pass=$((pass+1)); } \
  || { echo "FAIL AC5 the replay-written card names --card --replay as its writer"; head -1 "$CARD_HOME/$NONCE-t5.md" | sed 's/^/    /'; fail=$((fail+1)); }
check_eq "AC5 the replay-written card resolves the node cell" "node — q · $CUSER" "$(read_cell node "$NONCE-t5")"
check_eq "AC5 the replay-written card is followed by one now — line" "1" "$(grep -c '^now — ' "$CARD_OUT")"

# AC6 — --path prints one line and touches nothing.
run_card "AC6 --card --path prints the card's path" "$CWT" 0 "/orientation/$NONCE-t6.md" --card --path --session "$NONCE-t6"
check_eq "AC6 --card --path prints exactly one line" "1" "$(wc -l < "$CARD_OUT" | tr -d '[:space:]')"
[ ! -e "$CARD_HOME/$NONCE-t6.md" ] && { echo "ok   AC6 --card --path wrote no card"; pass=$((pass+1))
 } || { echo "FAIL AC6 --card --path wrote no card"; fail=$((fail+1)); }

# AC7 — the cap forced under the startup card's size: a refusal naming cap and overage, no file.
(cd "$CWT" && CARD_CAP_BYTES=100 bash "$CHECK" --card --write --session "$NONCE-t7" </dev/null > "$CARD_OUT" 2>&1); got=$?
[ "$got" = 2 ] && grep -q "over the 100-byte cap" "$CARD_OUT" && [ ! -e "$CARD_HOME/$NONCE-t7.md" ] \
  && { echo "ok   AC7 a card over CARD_CAP_BYTES is refused with exit 2, naming the cap, and leaves no file"; pass=$((pass+1)); } \
  || { echo "FAIL AC7 a card over CARD_CAP_BYTES is refused with exit 2, naming the cap, and leaves no file (exit $got)"; sed 's/^/    /' "$CARD_OUT"; fail=$((fail+1)); }

# The dispatch itself: --card with no verb refuses; --write WITHOUT --card still reaches the manifest
# catch-all exactly as before this verb family existed.
run_card "--card with no verb → exit 2" "$CWT" 2 "--card needs one of --write, --replay or --path" --card --session "$NONCE-t8"
run_card "--write without --card is still a manifest path argument" "$CWT" 2 "'--write' not found" --write

# AC9 — no fetch and no ref move: a remote one commit ahead, refs identical after, no FETCH_HEAD.
mkrepo aheadremote; AHEAD_R="$R"
git clone -q "$AHEAD_R" "$TMP/aheadlocal" 2>/dev/null
echo ahead > "$AHEAD_R/ahead.txt"; commit_all "$AHEAD_R" "remote moves ahead"
h_before=$(git -C "$TMP/aheadlocal" rev-parse HEAD); o_before=$(git -C "$TMP/aheadlocal" rev-parse origin/main)
rm -f "$TMP/aheadlocal/.git/FETCH_HEAD"
run_card "AC9 --card --write in a repo whose remote is ahead, and with no manifest at all" "$TMP/aheadlocal" 0 "node — UNKNOWN: no registry" --card --write --session "$NONCE-t9"
check_eq "AC9 HEAD and origin/main are unchanged after the card" "$h_before $o_before" \
  "$(git -C "$TMP/aheadlocal" rev-parse HEAD) $(git -C "$TMP/aheadlocal" rev-parse origin/main)"
[ ! -e "$TMP/aheadlocal/.git/FETCH_HEAD" ] && { echo "ok   AC9 no FETCH_HEAD was written"; pass=$((pass+1)); } || { echo "FAIL AC9 no FETCH_HEAD was written"; fail=$((fail+1)); }
check_eq "AC9 a primary tree's card says primary" "tree — $(git -C "$TMP/aheadlocal" rev-parse --show-toplevel) · primary · branch main · BASE $h_before · clean" "$(grep -m1 '^tree — ' "$TMP/aheadlocal/.git/orientation/$NONCE-t9.md")"

# AC10 — no .memory-tree.conf: exit 0 and a skipped: live cell, never a refusal.
mkrepo noconf; write_manifest "$R" "$(head_sha "$R")" "Makefile" "docs/GOV.md"
run_card "AC10 --card --write with no .memory-tree.conf exits 0" "$R" 0 "live — skipped: no .memory-tree.conf in this tree" --card --write --session "$NONCE-t10"

# AC11 — this repository's REAL common dir holds no card the suite wrote.
real_common=$(cd "$(git -C "$GOVROOT" rev-parse --git-common-dir)" && pwd)
leaked=$(ls "$real_common/orientation" 2>/dev/null | grep -c "^$NONCE-" || true)
check_eq "AC11 the suite left no card in this repository's shared common dir ($real_common/orientation)" "0" "$leaked"

# TOOL-cSettledDocket-5 — the agreed shape, so one leg can read every suite's count. This file
# ALREADY counted; the spec that proposed adding a counter here had grepped for another suite's
# spelling and reported a missing capability after measuring a missing convention.
# 108 = every arm that runs on EVERY node. The card section holds one arm more on node a alone (the
# exact tag against the real AGENTS.md, which the spec words as "on this node"); it announces its
# skip elsewhere, and a floor that counted it would red the suite on b, c and d for an arm that is
# not theirs to reach. KICK-aReplayedCard-1.
FLOOR_ASSERTIONS=108
[ "$pass" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $pass assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent; look for a block stranded past an exit or a return"; fail=$((fail+1)); }
# GUARDED on the failure count. Printing PASS unconditionally meant a suite with failing arms still
# reported success on its last line — the exact shape the floor above exists to catch, introduced
# by the conversion that added the floor. `pass` counts SUCCESSES, so it is `fail` that decides.
[ "$fail" = 0 ] && echo "PASS ($pass assertions)"
[ "$fail" = 0 ] || echo "---- $fail failed ----"
[ "$fail" = 0 ]
