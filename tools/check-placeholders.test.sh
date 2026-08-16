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

# ---- a fixture repo carrying a MINIATURE of the real playbook trio --------------------------------
# Not a copy of the real files: a fixture that mirrors production drifts with it and stops testing
# the predicate. Three placeholders, one of them deliberately shared.
mkfixture() { # $1 = dir, $2 = catalogue body
  local d="$1"
  mkdir -p "$d"
  printf '<!-- governance-template: v9.9 -->\n{{ALPHA}} and {{BETA}} and {{MEMORY_ROOT}}\n' \
    > "$d/parallel-coding-governance.template.md"
  printf '<!-- governance-template: v9.9 -->\n{{GAMMA}} and {{MEMORY_ROOT}}\n' \
    > "$d/parallel-coding-governance.domain-rules.md"
  printf '%s\n' "$2" > "$d/parallel-coding-governance.customize.md"
  # autocrlf off in the fixture: this repo's own `.gitattributes` does not reach a temp dir, so a
  # Windows global setting would emit a LF-to-CRLF warning per file per case and bury the arms.
  ( cd "$d" && git init -q && git config core.autocrlf false && git add -A \
      && git -c user.email=t@t -c user.name=t commit -qm f )
}

GOOD_CAT='## Placeholders
4 in total as a UNION. The two groups are not disjoint.

Shared between both files: `{{MEMORY_ROOT}}`.

### In `parallel-coding-governance.template.md` — 3
`{{ALPHA}}` `{{BETA}}` `{{MEMORY_ROOT}}`
### In `parallel-coding-governance.domain-rules.md` — 2
`{{GAMMA}}` `{{MEMORY_ROOT}}`'

# 1. the green case — a catalogue that agrees with its files
mkfixture "$TMPROOT/good" "$GOOD_CAT"
arm "green: an agreeing catalogue passes" 0 "check-placeholders OK" -- \
  bash -c "cd '$TMPROOT/good' && bash '$GATE'"

# 2. AC9 — the disjointness lie, the defect that funds the backlog row
mkfixture "$TMPROOT/disjoint" "${GOOD_CAT/The two groups are not disjoint./The two groups are **disjoint** — no placeholder appears in both.}"
arm "red: a **disjoint** claim over a shared placeholder" 1 "appear in BOTH files" -- \
  bash -c "cd '$TMPROOT/disjoint' && bash '$GATE'"

# 3. AC9 — an undeclared shared placeholder (no disjointness lie, just silence)
mkfixture "$TMPROOT/undeclared" "${GOOD_CAT/Shared between both files: \`{{MEMORY_ROOT}}\`./}"
arm "red: a shared placeholder not named on the Shared line" 1 "Shared between both files" -- \
  bash -c "cd '$TMPROOT/undeclared' && bash '$GATE'"

# 4. AC9 — a per-file tally that disagrees with the measurement
mkfixture "$TMPROOT/tally" "${GOOD_CAT/— 3/— 7}"
arm "red: a wrong per-file tally" 1 "claims 7" -- \
  bash -c "cd '$TMPROOT/tally' && bash '$GATE'"

# 5. AC9 — a placeholder used but absent from the catalogue
mkfixture "$TMPROOT/uncatalogued" "${GOOD_CAT/\`{{BETA}}\` /}"
arm "red: a used placeholder missing from the catalogue" 1 "is NOT listed" -- \
  bash -c "cd '$TMPROOT/uncatalogued' && bash '$GATE'"

# 6. AC11 — the marker lockstep across the TWO carriers
mkfixture "$TMPROOT/marker" "$GOOD_CAT"
sed -i 's/v9\.9/v8.8/' "$TMPROOT/marker/parallel-coding-governance.domain-rules.md"
( cd "$TMPROOT/marker" && git add -A && git -c user.email=t@t -c user.name=t commit -qm m ) >/dev/null 2>&1
arm "red: the two marker-carrying files disagree" 1 "disagree on governance-template" -- \
  bash -c "cd '$TMPROOT/marker' && bash '$GATE'"

# 7. the vacuity arm — an empty measurement must REFUSE, not pass
mkfixture "$TMPROOT/empty" "$GOOD_CAT"
printf '<!-- governance-template: v9.9 -->\nno placeholders here at all\n' \
  > "$TMPROOT/empty/parallel-coding-governance.template.md"
( cd "$TMPROOT/empty" && git add -A && git -c user.email=t@t -c user.name=t commit -qm e ) >/dev/null 2>&1
arm "red: an empty measurement refuses rather than passing" 1 "Refusing to pass" -- \
  bash -c "cd '$TMPROOT/empty' && bash '$GATE'"

# 8. the UNION total, which the catalogue states in prose
mkfixture "$TMPROOT/union" "${GOOD_CAT/4 in total as a UNION./9 in total as a UNION.}"
arm "red: a wrong UNION total" 1 "claims 9 in total as a UNION" -- \
  bash -c "cd '$TMPROOT/union' && bash '$GATE'"

# 9. coverage the OTHER direction — a catalogue entry no shipped file uses
mkfixture "$TMPROOT/ghost" "${GOOD_CAT/\`{{GAMMA}}\` /\`{{GAMMA}}\` \`{{NEVER_USED}}\` }"
arm "red: a catalogue entry appearing in NEITHER shipped file" 1 "appears in NEITHER shipped file" -- \
  bash -c "cd '$TMPROOT/ghost' && bash '$GATE'"

# 10. marker PRESENCE, not just distinctness. Counting distinct markers alone reads "one file has a
# marker and the other has none" as agreement — a comparison over a population of one.
mkfixture "$TMPROOT/nomarker" "$GOOD_CAT"
sed -i '/governance-template/d' "$TMPROOT/nomarker/parallel-coding-governance.domain-rules.md"
( cd "$TMPROOT/nomarker" && git add -A && git -c user.email=t@t -c user.name=t commit -qm n ) >/dev/null 2>&1
arm "red: a shipped file carrying NO marker at all" 1 "carries NO governance-template marker" -- \
  bash -c "cd '$TMPROOT/nomarker' && bash '$GATE'"

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

# The predicate must never be pointed at the tracked sources. This arm PROVES the bare leg and the
# survival mode are different questions: the real template would fail --check and passes bare.
arm "the tracked sources FAIL --check, which is why the bare leg does not run it" 1 "SURVIVING PLACEHOLDER" -- \
  bash "$GATE" --check "$ROOT/parallel-coding-governance.template.md" "$ROOT/parallel-coding-governance.domain-rules.md"

# ---- usage refusals ------------------------------------------------------------------------------
arm "--check with one path is a usage refusal" 2 "usage:" -- bash "$GATE" --check "$TMPROOT/filled-a.md"
arm "an unknown verb is a usage refusal" 2 "usage:" -- bash "$GATE" --frobnicate

if [ "$FAIL" -ne 0 ]; then
  echo "check-placeholders.test FAILED — $FAIL of $((PASS+FAIL)) arm(s)"
  exit 1
fi
echo "check-placeholders.test OK — $PASS arm(s)"
