#!/usr/bin/env bash
# check-kit-placeholders.test.sh — red/green arms for tools/check-kit-placeholders.py
# (TOOL-dRetiredFork-19).
#
# HERMETIC: every arm builds its own scratch tree under mktemp -d and never touches the real one, so
# the suite is safe beside the other heavy legs in a concurrent bar.
#
# THE ARM THAT MATTERS MOST is the ESCAPED-SPELLING one. The pre-wiring run over the real tree
# (section 7's rule, and this unit's S5) caught the first draft of the predicate redding 17 innocent
# tokens across five kits: the adopters write the substitution as `${out//\{\{KIT_DIR\}\}/...}` with
# the braces backslash-escaped for the shell, and a predicate matching only the bare `{{KIT_DIR}}`
# finds NOTHING in the one file it exists to read. That arm is what stops the fix regressing.
set -u

# The shrink-only assertion floor. A suite that stops running arms must RED rather than report a
# smaller success: `check-testsuite-counts.sh` reads this pin, the printed count, and the comparison
# between them, because a pin nothing reads is the same nothing as no pin.
FLOOR_ASSERTIONS=12
GATE="$(cd "$(dirname "$0")" && pwd)/check-kit-placeholders.py"
# The launcher is RESOLVED by running it (tools/lib/resolve-python.sh); `PY=` overrides. A bare
# default here was the parameter-default shape the resolver ban now catches.
if [ -z "${PY:-}" ] && [ -f "${GATE%/*}/lib/resolve-python.sh" ]; then . "${GATE%/*}/lib/resolve-python.sh"; PY=$(resolve_python) || exit 2; fi
PY=${PY:-python}   # gov:literal-python — last-resort fallback when lib/ is absent (adopter layout)
pass=0; fail=0

arm() {              # $1 = what it asserts, $2 = expected rc, $3 = actual rc, $4 = haystack, $5 = needle
  local ok=1
  [ "$2" = "$3" ] || ok=0
  if [ -n "${5:-}" ]; then case "$4" in *"$5"*) ;; *) ok=0 ;; esac; fi
  if [ "$ok" = 1 ]; then echo "arm ok    $1"; pass=$((pass+1))
  else echo "arm FAIL  $1 (want rc $2, got rc $3)"; echo "$4" | head -3; fail=$((fail+1)); fi
}

# A scratch tree: $1 = root, $2 = the placeholders list body, $3 = the adopter's SPELLING MODE,
# $4 = the [adopt] block body.
#
# $3 IS A MODE, NOT THE TEXT, and that is deliberate. Passing the spelling as a literal meant it
# crossed a single-quote, a printf `%s` (which does NOT expand backslashes in its argument) and a
# `sed` rewrite, and it arrived doubled as `\\{\\{` where a real adopter carries `\{\{` — so the arm
# for the escaped form failed against a fixture that never contained the escaped form. The bytes are
# written HERE, by the format string, where the escaping is read exactly once.
spell() {
  case "$1" in
    escaped) printf 'out=${out//\\{\\{KIT_DIR\\}\\}/"$V"}\n' ;;
    bare)    printf 'out=${out//{{KIT_DIR}}/"$V"}\n' ;;
    *)       printf 'out=$out  # substitutes nothing\n' ;;
  esac
}
scratch() {
  mkdir -p "$1/tools/demo"
  cat > "$1/tools/demo/kit.toml" <<TOML
[[files]]
include = ["t.md"]
role = "rendered"
placeholders = [$2]

[adopt]
$4
TOML
  { printf '#!/usr/bin/env bash\n# demo adopter\n'; spell "$3"; } > "$1/tools/demo/adopt-demo.sh"
}

run() { "$PY" "$GATE" --root "$1" ${2:-} 2>&1; }

# ---- AC3: every declared token substituted -> exit 0, and the run NAMES what it graded.
T=$(mktemp -d); scratch "$T" '"KIT_DIR"' escaped 'argv = ["bash", "{kit}/adopt-demo.sh"]'
o=$(run "$T"); rc=$?
arm "every declared token substituted exits 0" 0 "$rc" "$o" "1 kit(s) graded"
arm "...and the green line names the pair count" 0 "$rc" "$o" "rule-token pair(s)"

# ---- THE ESCAPED SPELLING. This is the defect S5's pre-wiring run found; without it the gate reds
# ---- every real adopter in the tree.
arm "the shell-ESCAPED spelling counts as substituted" 0 "$rc" "$o" "graded"

# ---- the BARE spelling must also count: a template-renderer may write it unescaped.
T2=$(mktemp -d); scratch "$T2" '"KIT_DIR"' bare 'argv = ["bash", "{kit}/adopt-demo.sh"]'
o2=$(run "$T2"); rc2=$?
arm "the BARE spelling counts as substituted too" 0 "$rc2" "$o2" "graded"

# ---- AC2: a declared token the adopter never substitutes REDS, naming token AND adopter.
T3=$(mktemp -d); scratch "$T3" '"KIT_DIR", "TOOL_ROOT"' escaped 'argv = ["bash", "{kit}/adopt-demo.sh"]'
o3=$(run "$T3"); rc3=$?
arm "an unsubstituted declared token REDS" 1 "$rc3" "$o3" "TOOL_ROOT"
arm "...and the refusal names the adopter that omits it" 1 "$rc3" "$o3" "adopt-demo.sh"

# ---- AC4: an EMPTY population REFUSES. A gate that scanned nothing reports the same zero as a
# ---- clean tree, which is the vacuous-selector shape this repo refuses.
T4=$(mktemp -d); mkdir -p "$T4/tools/demo"
printf '[[files]]\ninclude = ["t.md"]\nrole = "engine"\n\n[adopt]\nargv = []\n' > "$T4/tools/demo/kit.toml"
o4=$(run "$T4"); rc4=$?
arm "an EMPTY declaring population REFUSES rather than passing" 2 "$rc4" "$o4" "REFUSED"

# ---- a DECLARED `why_no_adopter` is honoured, counted and NAMED — an exemption is not coverage.
T5=$(mktemp -d); scratch "$T5" '"TOOL_ROOT"' none 'argv = []
why_no_adopter = "rendered by the parity gate"'
o5=$(run "$T5"); rc5=$?
arm "a declared why_no_adopter is exempt, not red" 0 "$rc5" "$o5" "exempt by a declared"

# ---- ...and an UNRESOLVABLE adopter with NO declared reason still REDS. The exemption must be
# ---- written down; a missing block is not a silent pass.
T6=$(mktemp -d); scratch "$T6" '"TOOL_ROOT"' none 'argv = []'
o6=$(run "$T6"); rc6=$?
arm "an adopter-less kit with NO stated reason REDS" 1 "$rc6" "$o6" "no resolvable"

# ---- TOOL-aRepatriatedFork-10 S7: a RENDERED template spelling `KEY=value` for a key its own kit's
# ---- conf example declares REDS, naming the key — the shipping repo's value would ship as every
# ---- adopter's. The key is in NO `[config]` list on purpose: the caps a template cites live in the
# ---- example alone, so an arm reading the lists only would pass this fixture by scanning nothing.
T7=$(mktemp -d); scratch "$T7" '"KIT_DIR"' escaped 'argv = ["bash", "{kit}/adopt-demo.sh"]'
printf '\n[config]\nfile = ".demo.conf"\noptional_keys = ["OTHER_KEY"]\n' >> "$T7/tools/demo/kit.toml"
printf 'INDEX_CAP_LINES="250"\n' > "$T7/tools/demo/.demo.conf.example"
printf 'This repo declares `INDEX_CAP_LINES=0`.\n' > "$T7/tools/demo/t.md"
o7=$(run "$T7"); rc7=$?
arm "a rendered template spelling its own kit's conf value REDS" 1 "$rc7" "$o7" "INDEX_CAP_LINES"
# ...and the render form passes: the same key through a placeholder is what the arm asks for.
printf 'This tree declares `INDEX_CAP_LINES={{KIT_DIR}}`.\n' > "$T7/tools/demo/t.md"
o8=$(run "$T7"); rc8=$?
arm "the same key rendered through a placeholder passes" 0 "$rc8" "$o8" "spell no conf value"

# ...and a FORMAT description of the value is not a value: a quoted `<placeholder>` states no
# ---- value of gov's, so it passes (gate repair at VERIFYING, TOOL-aRepatriatedFork-10).
printf 'Pinned per gate, `INDEX_CAP_LINES="<gate>:<n>"`.\n' > "$T7/tools/demo/t.md"
o9=$(run "$T7"); rc9=$?
arm "a quoted <placeholder> format description is not a conf value" 0 "$rc9" "$o9" "spell no conf value"

rm -rf "$T" "$T2" "$T3" "$T4" "$T5" "$T6" "$T7"
total=$((pass+fail))
if [ "$total" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "check-kit-placeholders: $total assertion(s) executed, below the declared floor of $FLOOR_ASSERTIONS —"
  echo "  arms went missing rather than failing, which reports as success without this check."
  exit 1
fi
[ "$fail" = 0 ] && echo "PASS ($total assertions)"
[ "$fail" = 0 ] || { echo "check-kit-placeholders: $fail of $total assertion(s) failed"; exit 1; }
