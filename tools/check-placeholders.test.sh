#!/usr/bin/env bash
# check-placeholders.test.sh — the arms for tools/check-placeholders.sh.
#
# EVERY ARM ASSERTS A MESSAGE, never an exit code alone. These fixtures are deliberately broken in
# several ways at once is exactly the trap: a fixture that reds for the wrong reason scores a pass
# for the arm that was supposed to prove the right one. So each negative arm greps for the sentence
# it is about.
#
# The `--check A B` arms are the ONLY place the survival predicate runs. It is never pointed at the
# tracked sources, which carry placeholders permanently and by design — a leg that did would red on
# its own landing commit.
set -u
ROOT="$(git rev-parse --show-toplevel)" || exit 2
GATE="$ROOT/tools/check-placeholders.sh"
PASS=0; FAIL=0
ok() { PASS=$((PASS+1)); }
bad() { FAIL=$((FAIL+1)); echo "  FAIL: $1"; }

# `arm <label> <want-rc> <want-substring> -- <command...>`
arm() {
  local label="$1" want="$2" needle="$3"; shift 4
  local out rc
  out=$("$@" 2>&1); rc=$?
  if [ "$rc" -ne "$want" ]; then bad "$label — wanted rc=$want got $rc: $out"; return; fi
  case "$out" in *"$needle"*) ok ;; *) bad "$label — rc was right but the message was not: $out" ;; esac
}

TMPROOT=$(mktemp -d)
trap 'rm -rf "$TMPROOT"' EXIT

# ---- a fixture repo carrying a MINIATURE of the real playbook file -------------------------------
# Not a copy of the real file: a fixture that mirrors production drifts with it and stops testing
# the predicate. ONE carrier since v3.0 — the companions the trio-shaped fixture used to write were
# deleted, and writing them here kept two dead paths alive in a file nothing else read.
mkfixture() { # $1 = dir
  local d="$1"
  mkdir -p "$d"
  printf '<!-- governance-template: v9.9 -->\n{{ALPHA}} and {{BETA}} and {{MEMORY_ROOT}}\n' \
    > "$d/coding-governance-agents.template.md"
  # autocrlf off in the fixture: this repo's own `.gitattributes` does not reach a temp dir, so a
  # Windows global setting would emit a LF-to-CRLF warning per file per case and bury the arms.
  ( cd "$d" && git init -q && git config core.autocrlf false && git add -A \
      && git -c user.email=t@t -c user.name=t commit -qm f )
}

# 1. the green case — the one carrier well-formed
mkfixture "$TMPROOT/good"
arm "green: the single marker carrier is present and well-formed" 0 "check-placeholders OK" --   bash -c "cd '$TMPROOT/good' && bash '$GATE'"

# 2. marker PRESENCE. With one carrier this is the whole marker question: there is no second file to
# be in lockstep WITH, so presence plus well-formedness is what survives.
mkfixture "$TMPROOT/nomarker"
sed -i '/governance-template/d' "$TMPROOT/nomarker/coding-governance-agents.template.md"
( cd "$TMPROOT/nomarker" && git add -A && git -c user.email=t@t -c user.name=t commit -qm n ) >/dev/null 2>&1
cp -r "$TMPROOT/good" "$TMPROOT/twomarkers"
printf '<!-- governance-template: v9.9 -->\n' >> "$TMPROOT/twomarkers/coding-governance-agents.template.md"
arm "red: the one carrier holds more than one marker" 1 "rather than exactly one" --   bash -c "cd '$TMPROOT/twomarkers' && bash '$GATE'"

arm "red: a shipped file carrying NO marker at all" 1 "carries NO governance-template marker" --   bash -c "cd '$TMPROOT/nomarker' && bash '$GATE'"

# ---- AC10 — the survival predicate, fixtures ONLY ------------------------------------------------
printf 'all filled in here\n' > "$TMPROOT/filled-a.md"
printf 'and here too\n'       > "$TMPROOT/filled-b.md"
arm "green: --check over two FILLED files" 0 "no placeholder survived" -- \
  bash "$GATE" --check "$TMPROOT/filled-a.md" "$TMPROOT/filled-b.md"

printf 'this one still says {{MEMORY_ROOT}}\n' > "$TMPROOT/unfilled-b.md"
arm "red: --check names a SURVIVING placeholder" 1 "SURVIVING PLACEHOLDER" -- \
  bash "$GATE" --check "$TMPROOT/filled-a.md" "$TMPROOT/unfilled-b.md"
arm "red: --check names the placeholder itself" 1 "{{MEMORY_ROOT}}" -- \
  bash "$GATE" --check "$TMPROOT/filled-a.md" "$TMPROOT/unfilled-b.md"

# The predicate must never be pointed at the tracked source. This arm PROVES the bare leg and the
# survival mode are different questions: the real template would fail --check and passes bare.
# The SECOND operand is the clean fixture, not the template again: passing one path twice would pass
# identically if the loop read only `$2`, leaving the first-position iteration unproven.
arm "the tracked source FAILS --check, which is why the bare leg does not run it" 1 "SURVIVING PLACEHOLDER" -- \
  bash "$GATE" --check "$ROOT/coding-governance-agents.template.md" "$TMPROOT/filled-a.md"

# ---- usage refusals ------------------------------------------------------------------------------
arm "--check with one path is a usage refusal" 2 "usage:" -- bash "$GATE" --check "$TMPROOT/filled-a.md"
arm "an unknown verb is a usage refusal" 2 "usage:" -- bash "$GATE" --frobnicate

if [ "$FAIL" -ne 0 ]; then
  echo "check-placeholders.test FAILED — $FAIL of $((PASS+FAIL)) arm(s)"
  exit 1
fi
echo "check-placeholders.test OK — $PASS arm(s)"
