#!/usr/bin/env bash
# run-gates.sh — the coding-governance merge bar: run every gate this repo dogfoods, report per leg.
# The full bar green at the push boundary; earlier runs scoped. Exit 0 = all passed · 1 = one or more failed · 2 = must run from the repo.
#   bash tools/run-gates.sh
# Legs live in tools/gate-legs.json (single source); this runner is a thin iterator over it.
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "run-gates: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
. "$ROOT/tools/lib/resolve-python.sh"
PYBIN=$(resolve_python) || { echo "run-gates: no usable python — required to parse tools/gate-legs.json"; exit 2; }
fails=0; n=0; skips=0

# The leg manifest, overridable so a fixture can drive this runner without re-running the real bar.
# Without a seam here the only way to exercise run-gates.sh is to invoke it against the repo, which
# re-runs the whole bar recursively and clobbers the live gate-last-summary.txt mid-run -- so the
# evidence guarantee below had no way to be tested at all (TOOL-dNomadicAtlas-1).
LEGS_FILE="${GATE_LEGS:-tools/gate-legs.json}"

# ---- durable per-leg evidence (TOOL-dNomadicAtlas-1) --------------------------------------------
# leg() already holds every leg's merged output in $out and PRINTS it on failure, then keeps only the
# ROW for the durable summary. The reason is in scope at the exact line the durable record is built,
# and dropped there -- so a `| tail` still loses the WHY while keeping the WHICH. inCMS hit this for
# real: a red leg inside a push piped through `tail -45`, unidentifiable afterwards, and the
# reflexive re-run passed, so the evidence was gone for good.
#
# Resolved ONCE, and a path is never composed from an empty root: `git rev-parse --git-dir` yields
# nothing outside a repo, and composing "/gate-logs/<leg>.log" from that would write outside the tree.
GD="$(git rev-parse --git-dir 2>/dev/null)" || GD=""
LOGDIR=""
if [ -n "$GD" ] && mkdir -p "$GD/gate-logs" 2>/dev/null; then
  LOGDIR="$GD/gate-logs"
  chmod 700 "$LOGDIR" 2>/dev/null || true
else
  echo "run-gates: evidence capture OFF (no usable git dir) — leg output is stdout-only this run" >&2
fi

leg_log() {   # NAME -> the log path, or rc 1 when capture is off
  [ -n "$LOGDIR" ] || return 1
  printf '%s/%s.log' "$LOGDIR" "$(printf '%s' "$1" | tr -c 'A-Za-z0-9._-' '_')"
}
# A leg's output can carry an operator-exported credential; mask URL userinfo before it becomes
# durable. Terminal output was ephemeral, a file is not.
redact() { sed -E 's#://[^/@[:space:]]+:[^/@[:space:]]+@#://***:***@#g'; }

# Baseline for conditional legs: the mainline tip we gate against. Override with GATE_BASE.
# Unresolvable (no remote / shallow / detached) → empty, and changed() fails safe to "run".
DEFBR=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null); DEFBR=${DEFBR#origin/}
BASE=$(git rev-parse --verify -q "${GATE_BASE:-origin/${DEFBR:-main}}" 2>/dev/null) || BASE=
changed() { [ -z "$BASE" ] && return 0; ! git diff --quiet "$BASE" -- "$@" 2>/dev/null; }

leg() { # name · command...
  local name=$1; shift; n=$((n+1))
  local out; out=$("$@" </dev/null 2>&1); local rc=$?   # legs never read stdin — deny it so a stray reader can't hang the bar
  # Persist EVERY leg, not only the failing one: a passing leg's output is what a later bisect reads,
  # and the cost is one write of bytes already in memory.
  local lf; lf="$(leg_log "$name")" || lf=""
  if [ -n "$lf" ]; then
    { printf '# run-gates | leg %s | exit %s\n' "$name" "$rc"; printf '%s\n' "$out"; } | redact >"$lf" 2>/dev/null || true
    chmod 600 "$lf" 2>/dev/null || true
  fi
  if [ "$rc" = 0 ]; then printf 'GATE ok    %s\n' "$name"
  else fails=$((fails+1)); printf 'GATE FAIL  %s (exit %d)\n' "$name" "$rc"; printf '%s\n' "$out" | sed 's/^/    /'
       FAILED_LEGS="${FAILED_LEGS:-}GATE FAIL  $name (exit $rc)"$'\n'   # TOOL-aLeasedGauntlet-1 S3: keep for the durable summary
       # TOOL-dNomadicAtlas-1: and a POINTER at the leg's own output, so the durable summary answers
       # WHY and not only WHICH. A pointer, never the bytes — this file is what an operator quotes.
       [ -n "$lf" ] && FAILED_LEGS="${FAILED_LEGS}    log: $lf"$'\n'; fi
}

leg_if_changed() { # guard-path[,guard-path...] · name · command...  (leg() counts n on run; skip counts here)
  local guard=$1 name=$2; shift 2
  local paths; IFS=, read -ra paths <<<"$guard"
  if changed "${paths[@]}"; then leg "$name" "$@"
  else n=$((n+1)); skips=$((skips+1)); printf 'GATE skip  %s (unchanged vs %s)\n' "$name" "${DEFBR:-baseline}"; fi
}

# Read the leg manifest as name<RS>guard(comma-joined)<RS>argv(joined by <US>) per line, where
# RS=\x1e and US=\x1f (non-whitespace, so an empty guard field survives `read`; a tab would collapse).
# Command-substitution surfaces a parse failure (a `< <()` process-sub would swallow it).
legs=$("$PYBIN" -c '
import json, sys
try:
    data = json.load(open(sys.argv[1]))
except Exception as e:
    sys.stderr.write("parse error: %s\n" % e); sys.exit(3)
if not isinstance(data, list) or not data:
    sys.stderr.write("gate-legs.json empty or not a list\n"); sys.exit(3)
rows = [l["name"] + "\x1e" + ",".join(l.get("guard", [])) + "\x1e" + "\x1f".join(l["argv"]) for l in data]
sys.stdout.buffer.write(("\n".join(rows) + "\n").encode())   # LF bytes (Windows text stdout is CRLF); \x1e field sep is non-whitespace so an empty guard field is preserved (a tab would collapse)
' "$LEGS_FILE") || { echo "run-gates: cannot parse $LEGS_FILE"; exit 2; }

while IFS=$'\x1e' read -r name guard argvraw; do
  [ -z "$name" ] && continue
  IFS=$'\x1f' read -ra argv <<<"$argvraw"
  case "${argv[0]}" in python|python3) argv[0]=$PYBIN ;; esac   # the manifest stores the canonical python3; run under the resolved PYBIN
  if [ -n "$guard" ]; then leg_if_changed "$guard" "$name" "${argv[@]}"
  else leg "$name" "${argv[@]}"; fi
done <<<"$legs"

echo "----"
skipnote=""; [ "$skips" -gt 0 ] && skipnote=" ($skips skipped)"
# TOOL-aLeasedGauntlet-1 S3: write the verdict + failing-leg rows to a durable file (worktree-safe
# gitdir) so a `| tail`/`Select-Object -Last N` can't discard which leg failed.
gd="$(git rev-parse --git-dir 2>/dev/null)"; sfile=""; [ -n "$gd" ] && sfile="$gd/gate-last-summary.txt"
if [ "$fails" = 0 ]; then
  [ -n "$sfile" ] && printf 'gates GREEN — %s/%s legs passed%s\n' "$((n-skips))" "$((n-skips))" "$skipnote" >"$sfile" 2>/dev/null || true
  echo "gates GREEN — $((n-skips))/$((n-skips)) legs passed$skipnote"; exit 0
else
  [ -n "$sfile" ] && { printf '%s' "${FAILED_LEGS:-}" >"$sfile"; printf 'gates RED — %s/%s legs failed%s\n' "$fails" "$n" "$skipnote" >>"$sfile"; } 2>/dev/null || true
  # TOOL-dNomadicAtlas-1: a SECOND copy on RED ONLY. gate-last-summary.txt is overwritten by every
  # run, so the reflexive "let me just re-run it" — which passes, when the red was a flake — erases
  # the evidence of the run that failed. This one is only ever overwritten by the next RED run.
  if [ -n "$gd" ]; then
    ffile="$gd/gate-last-failure.txt"
    { printf '%s' "${FAILED_LEGS:-}"; printf 'gates RED — %s/%s legs failed%s\n' "$fails" "$n" "$skipnote"; } >"$ffile" 2>/dev/null || true
    chmod 600 "$ffile" 2>/dev/null || true
  fi
  echo "gates RED — $fails/$n legs failed$skipnote"
  [ -n "$sfile" ] && echo "gate summary saved to $sfile"
  [ -n "$gd" ] && [ -f "$gd/gate-last-failure.txt" ] && echo "gate failure record saved to $gd/gate-last-failure.txt"
  exit 1
fi
