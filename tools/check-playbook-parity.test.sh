#!/usr/bin/env bash
# check-playbook-parity.test.sh — self-test for tools/check-playbook-parity.sh.
#
#   bash tools/check-playbook-parity.test.sh
#
# Exit 0 = every arm held · 1 = an arm failed · 2 = the harness could not set up.
#
# WHY EACH ARM IS A RED PROOF. The gate under test exists to catch coverage checks that pass by
# checking nothing, so a harness that only ever watched it pass would be the very defect it gates.
# `parallel-coding-governance.domain-rules.md`: "a new gate is not landed until its failing case has
# been observed."
#
# HOW THE ARMS WORK. Every arm builds a scratch WORKTREE-SHAPED fixture — a real git repo with its
# own tools/ and playbook trio — and runs the gate inside it. Nothing here mutates the real tree,
# which matters because the gate derives its kit set from `git ls-files` and would otherwise see
# this repo's own population.
set -u
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
GATE_SRC="$ROOT/tools/check-playbook-parity.sh"
fails=0
TMP=$(mktemp -d) || exit 2
trap 'rm -rf "$TMP"' EXIT

say_ok()   { printf 'arm ok    %s\n' "$1"; }
say_fail() { fails=$((fails+1)); printf 'arm FAIL  %s — %s\n' "$1" "$2"; }

# fixture <dir> — a minimal but VALID tree the gate passes on, so each arm breaks exactly one thing.
fixture() {
  local d=$1
  mkdir -p "$d/tools/memory-tree" "$d/tools/hooks" "$d/tools/lib" "$d/.claude"
  git -C "$d" init -q 2>/dev/null
  git -C "$d" config user.email t@t; git -C "$d" config user.name t
  cp "$GATE_SRC" "$d/tools/check-playbook-parity.sh"
  : > "$d/tools/memory-tree/engine.sh"
  # an UNDOCUMENTED kit, so the waiver row the fixture carries is live rather than stale
  : > "$d/tools/lib/inline.sh"
  printf 'const MAX_LENSES = 5\n' > "$d/tools/hooks/agent-cap.js"
  printf '{ "hooks": { "PreToolUse": [ { "matcher": "Workflow|Agent" } ] } }\n' > "$d/.claude/settings.json"
  # The PAIR. The charter converged to one file at v3.0 and the kit-adoption prose moved to the
  # runbook, so the haystack is charter + runbook. The charter names memory-tree and carries both
  # stated values; hooks is documented in the runbook and therefore NOT waivable.
  printf 'template {{ALPHA}} {{MEMORY_ROOT}}\ntools/memory-tree/ is the kit\nan array LITERAL of <=5 elements passes\nthe hook (matcher `Workflow|Agent`) denies\n' \
    | sed 's/<=/≤/' > "$d/coding-governance-agents.template.md"
  printf 'the runbook, where kit-adoption prose lives\ntools/hooks/ is reached here\n' > "$d/WIRE-INTO-PROJECT.md"
  printf '# waivers\nlib     gov-internal, ships nothing.\n' > "$d/tools/playbook-kit-waivers.txt"
  git -C "$d" add -A >/dev/null 2>&1
  git -C "$d" commit -qm f >/dev/null 2>&1
}

# arm <label> <expect: ok|red> <expected-substring-when-red> <mutator…>
arm() {
  local label=$1 expect=$2 want=$3; shift 3
  local d="$TMP/$(printf '%s' "$label" | tr -c 'a-zA-Z0-9' '_')"
  fixture "$d"
  ( cd "$d" && "$@" >/dev/null 2>&1 )
  git -C "$d" add -A >/dev/null 2>&1
  local out rc
  out=$(cd "$d" && bash tools/check-playbook-parity.sh 2>&1); rc=$?
  if [ "$expect" = ok ]; then
    if [ "$rc" -eq 0 ]; then say_ok "$label"
    else say_fail "$label" "expected the gate to PASS, it exited $rc"; printf '%s\n' "$out" | sed 's/^/      /'; fi
    return
  fi
  if [ "$rc" -eq 0 ]; then
    say_fail "$label" "expected the gate to RED, it exited 0 — the mutation was not caught"
    printf '%s\n' "$out" | sed 's/^/      /'; return
  fi
  case "$out" in
    *"$want"*) say_ok "$label" ;;
    *) say_fail "$label" "reds, but not naming: $want"; printf '%s\n' "$out" | sed 's/^/      /' ;;
  esac
}

# --- the control. Without it, every red proof below could be redding for an unrelated reason. -----
arm "control · a valid fixture passes" ok "" true

# --- the anchored matcher itself ---------------------------------------------------------------
# The gate's header calls a bare substring match "the vacuous-selector shape this gate exists to
# prevent, committed by the gate itself" — and nothing pinned it: loosening `named_in_playbook`
# to `grep -qF` left every other arm green. This fixture names a kit ONLY as a substring inside an
# unrelated word, so a loosened matcher certifies it documented and the arm goes red.
arm "S1 a kit named only as a substring is NOT documented" red \
  "a kit ships and the playbook never names it, with no waiver row to excuse it: ape" \
  sh -c 'mkdir -p tools/ape && : > tools/ape/x.sh && printf "the shape of a landscape\n" >> coding-governance-agents.template.md'

# --- AC1 · a kit named nowhere and waived nowhere --------------------------------------------------
arm "AC1 an undocumented kit reds by name" red \
  "a kit ships and the playbook never names it, with no waiver row to excuse it: orphankit" \
  sh -c 'mkdir -p tools/orphankit && : > tools/orphankit/x.sh'

# --- AC2 · the unit's central proof: a stated value drifting from the source that owns it ----------
arm "AC2 MAX_LENSES drifts from the template's stated bound" red \
  "a declared value pair disagrees with the source that owns it. Pair lens-array bound" \
  sh -c 'printf "const MAX_LENSES = 6\n" > tools/hooks/agent-cap.js'
arm "AC2b the hook matcher drifts from .claude/settings.json" red \
  "a declared value pair disagrees with the source that owns it. Pair agent-cap hook matcher" \
  sh -c 'printf "{ \"hooks\": { \"PreToolUse\": [ { \"matcher\": \"Workflow\" } ] } }\n" > .claude/settings.json'

# --- AC3 · a placeholder added and the catalogue counts not updated ---------------------------------

# --- AC4 · an extraction that matches nothing must never compare empty to empty ----------------------
arm "AC4 an unresolvable pair reds rather than passing" red \
  "an extraction matched NOTHING, so the pair was never compared" \
  sh -c 'sed -i "s/an array LITERAL of ≤5 elements passes//" coding-governance-agents.template.md'

# --- AC5 · the derivation broken to lose its sentinel -------------------------------------------------
arm "AC5 a derivation missing its sentinel reds" red \
  "the kit derivation lost its frozen sentinel member, so the derivation is broken rather than the tree being empty: expected to find " \
  sh -c 'git rm -q -r --cached tools/memory-tree >/dev/null 2>&1; rm -rf tools/memory-tree'

# --- AC6 · both waiver-drain arms ----------------------------------------------------------------------
arm "AC6a a waiver for a kit that is gone reds as stale" red \
  "a waiver row names a kit that no longer exists, so the row excuses nothing and is stale" \
  sh -c 'printf "ghostkit  gone\n" >> tools/playbook-kit-waivers.txt'
arm "AC6b a waiver for a kit the playbook DOES name reds" red \
  "a waiver row names a kit the playbook DOES document, so the row excuses nothing" \
  sh -c 'printf "memory-tree  redundant\n" >> tools/playbook-kit-waivers.txt'

# --- AC9 · the registry absent: red and STOP, never create one -------------------------------------------
arm "AC9 an absent waiver registry reds and stops" red \
  "the kit waiver registry is absent and this gate never creates it: expected " \
  sh -c 'git rm -q --cached tools/playbook-kit-waivers.txt >/dev/null 2>&1; rm -f tools/playbook-kit-waivers.txt'

# --- the two S2-stage integrity guards ----------------------------------------------------------
# Both mutate the fixture's OWN copy of the gate, which is what a red proof of THIS kind of guard
# looks like: the guard exists to notice that the stage did not run, so the fixture has to be a
# stage that did not run.
arm "S2 an uncreatable results file reds instead of reporting agreement" red \
  "the value-parity stage could not create its results file, so no pair was compared and this gate must not report agreement" \
  sh -c 'sed -i "s|^PPTMP=.*|PPTMP=/nonexistent-dir-for-the-arm/pp|" tools/check-playbook-parity.sh'
arm "S2 a lost results file reds rather than reading as no-disagreement" red \
  "the value-parity stage produced no completion sentinel, so its results were lost rather than empty and no pair was actually compared" \
  sh -c "sed -i \"/^printf 'PAIRSTAGE-RAN/d\" tools/check-playbook-parity.sh"

# --- the structural intersection check must not pass vacuously ---------------------------------------------

# --- the remaining five branches, armed rather than pinned as exceptions -------------------------
# check-arms refuses an unarmed branch that is not written into memory/project/unarmed-branches.txt,

# check 1 · the kit derivation returns an EMPTY set. Distinct from AC5, where the set is non-empty
# and merely lost its sentinel: here coverage would be vacuously true over nothing at all.
arm "S1 an empty kit derivation reds before reporting coverage" red \
  "the kit derivation returned an empty set, so coverage would pass by checking nothing" \
  sh -c 'git rm -q -r --cached tools >/dev/null 2>&1; rm -rf tools/memory-tree tools/hooks tools/lib'

# check 8 · a stated count that cannot be extracted at all. Without this the arithmetic block would
# compare three empty strings and report ok — the same vacuity the pair loop guards against.

# check 13 · the catalogue NAMES a shared placeholder that is not the measured intersection. The
# structural half of S3: check 12 catches naming none, this catches naming the wrong one.

if [ "$fails" -ne 0 ]; then
  printf 'check-playbook-parity.test.sh FAILED — %d arm(s)\n' "$fails"
  exit 1
fi
printf 'PASS — check-playbook-parity.test.sh: every arm held\n'
