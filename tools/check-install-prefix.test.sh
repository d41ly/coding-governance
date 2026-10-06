#!/usr/bin/env bash
# check-install-prefix.test.sh — red/green arms for the install-prefix gate, a PURE BAN since
# TOOL-aRepatriatedFork-30. Exit 0 = every arm held.
#
#   bash <prefix>/check-install-prefix.test.sh
#
# DISCIPLINES (same as the sibling gate tests):
#  * Every arm asserts the SPECIFIC message, never the exit code alone — a probe that reads only `$?`
#    reports success while exercising nothing.
#  * Every red arm has a green control over the SAME mechanism, so an arm cannot pass because the
#    gate rejects everything.
#  * The population guards get their own arms: an empty kit list, a dead counter and a python that
#    does not run would otherwise be silent success — the vacuous-selector class this repo catalogues.
#
# THIS FILE IS IN THE POPULATION IT TESTS, so it may not spell a kit path either. Every fixture uses
# `qdemo`, a kit that exists only inside the fixture, and gov's own prefix is assembled from `TL` at
# run time: the bytes a fixture writes carry the literal, and the bytes of this file do not. The
# sibling kits a fixture copies in are found by the FILE they hold, never by a typed directory name.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
# >>> derive_self_rel — canonical copy: kit-rel.sh in gov's lib dir (byte-identical; gated)
derive_self_rel() {
  local _dsr_p _dsr_rel=""
  _dsr_p=$(cd "$1" 2>/dev/null && pwd) || return 1
  while [ ! -e "$_dsr_p/.git" ]; do
    [ "$(dirname "$_dsr_p")" = "$_dsr_p" ] && return 1
    _dsr_rel="$(basename "$_dsr_p")${_dsr_rel:+/$_dsr_rel}"
    _dsr_p=$(dirname "$_dsr_p")
  done
  printf '%s\n' "$_dsr_rel"
}
# <<< derive_self_rel
KIT_REL=$(derive_self_rel "$HERE") || { echo "check-install-prefix.test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty at a
# root install. Every fixture lays its kits out under the same prefix as the host.
PFX="${KIT_REL:+$KIT_REL/}"
GATE="$HERE/check-install-prefix.sh"
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
GATE_REL="${PFX}${GATE##*/}"
# The deployer the kit-source test resolves, found by its ENGINE file rather than by a typed name.
GK_SRC=$(git ls-files -- "${PFX}*/govkit.py" | head -1)
[ -n "$GK_SRC" ] || { echo "check-install-prefix.test: no govkit engine under ${PFX:-the repo root}"; exit 2; }
GK=${GK_SRC%/*}; GK=${GK##*/}
TL=tool   # gov's own prefix is "${TL}s", assembled so that this file does not spell it
T=$(printf '\t')
# RAISED 39 -> 40 by TOOL-aMendedFleet-111: the NONKIT liveness arm (1).
FLOOR_ASSERTIONS=40
fails=0; passed=0; GRADED=0
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

bad()  { fails=$((fails+1)); printf 'arm FAIL  %s\n' "$*"; }
good() { passed=$((passed+1)); printf 'arm ok    %s\n' "$*"; }

# A repo shaped like a KIT SOURCE: the gate, a copy of govkit's engine and a registry at the tool root,
# and one kit `qdemo` whose descriptor ships everything it holds plus one rendered template.
build_source_fixture() { # $1 = dir · $2 = the line to put in the kit README
  local d="$1"
  mkdir -p "$d/${PFX}$GK" "$d/${PFX}qdemo"
  git -C "$d" init -q
  git -C "$d" config user.email t@t.test; git -C "$d" config user.name t
  cp "$GATE" "$d/$GATE_REL"
  cp "$ROOT/$GK_SRC" "$d/${PFX}$GK/govkit.py"
  printf 'version = 1\n\n[surface]\nglobs = ["{prefix}/*"]\n\n[selection]\ndefault = ["qdemo"]\n\n[[entry]]\nid = "qdemo"\ndescriptor = "{prefix}/qdemo/kit.toml"\n' \
    > "$d/${PFX}$GK/registry.toml"
  printf 'id = "qdemo"\nhome = "qdemo"\nversion_from = { none = "fixture" }\n\n[check]\nnone = "a fixture kit"\n\n[[files]]\ninclude = "**"\nrole = "engine"\n\n[[files]]\ninclude = ["page.template.md"]\nrole = "rendered"\nto = "{kit}/page.md"\nplaceholders = ["KIT_DIR"]\n\n[adopt]\nargv = []\nmutates_index = false\n' \
    > "$d/${PFX}qdemo/kit.toml"
  printf '%s\n' "$2" > "$d/${PFX}qdemo/README.md"
  printf '#!/usr/bin/env bash\necho qdemo\n' > "$d/${PFX}qdemo/thing.sh"
  printf 'Run {{KIT_DIR}}/thing.sh by hand.\n' > "$d/${PFX}qdemo/page.template.md"
  printf 'Run %sqdemo/thing.sh by hand.\n' "$PFX" > "$d/${PFX}qdemo/page.md"
  git -C "$d" add -A >/dev/null 2>&1
}

# ONE runner for every graded arm. `GRADED` counts the arms whose output proves the counter ran, so a
# suite whose fixtures all stopped short of it reds by that fact rather than reporting on nothing.
run_arm() { # label · want-substring · want-rc · dir · [gate path inside dir] · [argv...]
  local label="$1" want="$2" wrc="$3" dir="$4" g="${5:-$GATE_REL}" out rc
  shift 5 2>/dev/null || shift $#
  out=$(cd "$dir" && bash "$g" "$@" 2>&1); rc=$?
  case "$out" in *"install-prefix: clean — "*|*"install-prefix: RED — "*) GRADED=$((GRADED+1)) ;; esac
  if [ "$rc" != "$wrc" ]; then bad "$label (exit $rc, wanted $wrc): $(printf '%s' "$out" | tail -3)"; return; fi
  case "$out" in *"$want"*) good "$label" ;; *) bad "$label (message missing '$want'): $(printf '%s' "$out" | tail -3)" ;; esac
}
LAST_OUT=""
read_gate() { # dir -> the gate's --check output in LAST_OUT, its exit status returned
  local rc
  LAST_OUT=$(cd "$1" && bash "$GATE_REL" 2>&1); rc=$?
  case "$LAST_OUT" in *"install-prefix: clean — "*|*"install-prefix: RED — "*) GRADED=$((GRADED+1)) ;; esac
  return "$rc"
}

# ==================== the GREEN control and the population ====================================
G="$TMP/green"; build_source_fixture "$G" "The engine lives at {prefix}/qdemo/thing.sh in this repo."
run_arm "a kit source spelling only drained forms is clean" "install-prefix: clean — " 0 "$G"
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fails:-0}" = 0 ] && echo "PASS (${passed:-1} assertions)" || echo "FAIL (${passed:-1} assertions)"; [ "${fails:-0}" = 0 ] && exit 0; exit 1; fi
read_gate "$G"
case "$LAST_OUT" in *"clean — 0 tracked file(s)"*) bad "LIVENESS the green fixture graded NO file" ;;
  *"tracked file(s) graded"*) good "LIVENESS the green fixture graded a non-empty population, and says how many" ;;
  *) bad "LIVENESS the green fixture printed no population size: $LAST_OUT" ;; esac

# ==================== AC5 — one literal of each epoch-6 spelling, one file ======================
# Each line below is ONE spelling the predicate counts, and the arm asserts every <path>:<line>, so a
# spelling the gate stopped counting fails by its own line number rather than hiding in a total.
S="$TMP/spellings"; build_source_fixture "$S" 'A qdemo kit.'
{
  printf '%s\n' "kit = pathlib.Path(\".\") / \"${TL}s\" / \"qdemo\""       # 1: a quoted gov segment, joined
  printf '%s\n' "Run ${TL}s/qdemo/thing.sh from the checkout."             # 2: gov's prefix and a kit
  printf '%s\n' "Run ${TL}s/ghost.sh first."                               # 2: gov's prefix and a loose name
  printf '%s\n' 'Run qdemo/thing.sh from the root.'                         # 3: the root spelling
  printf '%s\n' 'Run vendor/qdemo/thing.sh at a vendor install.'            # 3: any literal prefix
  printf '%s\n' 'bash "$HERE/../qdemo/thing.sh"'                            # 3: after a derived shell base
  printf '%s\n' 'bash "$ROOT/${PFX}qdemo/thing.sh"'                         # 3: after a brace that is no token
  printf '%s\n' 'kit = HERE.parent / "qdemo"'                               # 4: a quoted kit joined by /
  printf '%s\n' 'w = os.path.join(w, "scripts", "qdemo")'                   # 4: a quoted kit inside a join
  printf '%s\n' "Copy it to <project>/${TL}s/qdemo/thing.sh by hand."       # 2: a /-led gov prefix
} > "$S/${PFX}qdemo/spellings.py"
git -C "$S" add -A >/dev/null 2>&1
read_gate "$S"; _src=$?
[ "$_src" = 1 ] && good "AC5 the spellings fixture exits 1" || bad "AC5 the spellings fixture exited $_src, wanted 1: $(printf '%s' "$LAST_OUT" | tail -2)"
for _n in 1 2 3 4 5 6 7 8 9 10; do
  case "$LAST_OUT" in *"  ${PFX}qdemo/spellings.py:$_n  qdemo"*|*"  ${PFX}qdemo/spellings.py:$_n  (loose)"*)
    good "AC5 spelling on line $_n is named by <path>:<line>" ;;
    *) bad "AC5 spelling on line $_n passed unnamed — $(sed -n "${_n}p" "$S/${PFX}qdemo/spellings.py")" ;; esac
done
case "$LAST_OUT" in *"there is no waiver"*) good "AC5 the refusal says there is no waiver to take" ;;
  *) bad "AC5 the refusal does not say the ban has no waiver" ;; esac
# ...and with the literals gone, the SAME file in drained and homonym forms exits 0.
{
  printf '%s\n' 'Run {prefix}/qdemo/thing.sh, or {{TOOL_ROOT}}qdemo/thing.sh.'
  printf '%s\n' 'Run <prefix>/qdemo/thing.sh, or <tool-root>/qdemo/thing.sh.'
  printf '%s\n' "cfg = {\"${TL}s\": 1}"
  printf '%s\n' 'run("plan", "--kits", "qdemo")'
  printf '%s\n' 'x = ["bin", "qdemo"]'
  printf '%s\n' "ci = root / '.github' / 'qdemo'"
  printf '%s\n' '# its Skill lands at .claude/skills/qdemo/SKILL.md'
  printf '%s\n' 'The `qdemo/` kit is described in prose.'
  printf '%s\n' 'hook = git_dir() / "qdemo"'
  printf '%s\n' 'log = session_root / "qdemo"'
  printf '%s\n' 'tx = transcript_dir / "qdemo"'
} > "$S/${PFX}qdemo/spellings.py"
git -C "$S" add -A >/dev/null 2>&1
run_arm "AC5 ...and the drained forms and homonyms in the same file are clean" "install-prefix: clean — " 0 "$S"
HOMONYM_LINES=$(cat "$S/${PFX}qdemo/spellings.py")

# The homonym shapes above are CENSUS shapes: each must still exist in THIS tree, or the rule guards a
# spelling nobody writes.
CENSUS_SITES=('common / "codebase-map" / "lookups.jsonl"' "root / '.github' / 'workflows'" 'sdir / "workflows"')
for _site in "${CENSUS_SITES[@]}"; do
  if git -C "$ROOT" grep -qF -- "$_site"; then good "census homonym still present: $_site"
  else bad "census homonym GONE, so its arm matches nothing: $_site"; fi
done
# TOOL-aMendedFleet-111 AC10: EVERY `NONKIT` alternative is exercised by a clean homonym fixture line
# or a census site, so an exemption whose spelling nobody writes reds here naming itself. The
# alternatives are read off the checker, never retyped. Staged red by re-adding `\bgd\b`; staging
# `session` out of it reds the clean-homonym arm above, on the fixture line that spells it.
_nk=$(sed -n 's/^NONKIT = re\.compile(r"(?i)\(.*\)")$/\1/p' "$GATE")
_nkpy=""; for _c in python3 python py; do "$_c" -c "import sys" >/dev/null 2>&1 && { _nkpy=$_c; break; }; done
if [ -z "$_nk" ] || [ -z "$_nkpy" ]; then
  bad "the NONKIT liveness arm could not read the checker's alternatives (or run python), so it graded nothing"
else
  _nkdead=$(printf '%s\n' "$HOMONYM_LINES" "${CENSUS_SITES[@]}" | "$_nkpy" -c 'import re, sys
alts = sys.argv[1].split("|")
lines = sys.stdin.read().splitlines()
print(" ".join(a for a in alts if not any(re.search("(?i)" + a, l) for l in lines)))' "$_nk")
  if [ -z "$_nkdead" ]; then good "every NONKIT alternative is exercised by a homonym fixture line or a census site: $_nk"
  else bad "NONKIT alternative(s) no homonym fixture line or census site exercises, so they guard a spelling nobody writes: $_nkdead"; fi
fi

# ==================== the POPULATION is every tracked file, shipped or not =====================
P1="$TMP/population"; build_source_fixture "$P1" 'A qdemo kit.'
mkdir -p "$P1/${PFX}notes"
printf 'Run %sqdemo/thing.sh by hand.\n' "${TL}s/" > "$P1/${PFX}notes/aside.md"
git -C "$P1" add -A >/dev/null 2>&1
run_arm "a tracked file NO descriptor resolves is graded" "  ${PFX}notes/aside.md:1  qdemo" 1 "$P1"
git -C "$P1" rm -q --cached "${PFX}notes/aside.md"
run_arm "...and the same file UNTRACKED is not" "install-prefix: clean — " 0 "$P1"

# ==================== AC9 — the render rule ====================================================
R="$TMP/render"; build_source_fixture "$R" 'A qdemo kit.'
read_gate "$R"
case "$LAST_OUT" in *"1 render(s) left out"*) good "AC9 a file matching its template whole is left out, and counted" ;;
  *) bad "AC9 the fixture render was not left out: $(printf '%s' "$LAST_OUT" | tail -2)" ;; esac
_list=$(cd "$R" && bash "$GATE_REL" --list 2>&1)
case "$_list" in *"render  ${PFX}qdemo/page.md  <- ${PFX}qdemo/page.template.md"*) good "AC9 --list names the render and its template" ;;
  *) bad "AC9 --list does not name the render: $(printf '%s' "$_list" | head -3)" ;; esac
printf 'And also %sqdemo/thing.sh.\n' "$PFX" >> "$R/${PFX}qdemo/page.md"
git -C "$R" add -A >/dev/null 2>&1
run_arm "AC9 ...and one appended line puts it back in the population, named" "  ${PFX}qdemo/page.md:1  qdemo" 1 "$R"
# A token is ONE LINE of text: a value spanning a newline is not a render of this template.
printf 'Run %sqdemo\n/thing.sh by hand.\n' "$PFX" > "$R/${PFX}qdemo/page.md"
git -C "$R" add -A >/dev/null 2>&1
read_gate "$R"
case "$LAST_OUT" in *"0 render(s) left out"*) good "AC9 a token value spanning a newline does not match" ;;
  *) bad "AC9 a multi-line token value matched the template: $(printf '%s' "$LAST_OUT" | tail -1)" ;; esac

# ==================== AC3 — no mode writes anything ==========================================
for _m in --write-ratchet --rebaseline; do
  run_arm "AC3 $_m is refused with the usage line" "a pure ban has no mode that writes anything" 2 "$G" "$GATE_REL" "$_m"
done

# ==================== the prefix is DERIVED: a two-segment install ============================
# The WHOLE tool root moves, the gate with it: a gate still spelling gov's prefix would enumerate no
# kit there and refuse, and one pinning the kit's awk field at 2 would name `gov` as every kit.
V="$TMP/vendor"; build_source_fixture "$V" 'A qdemo kit.'
if [ -n "$PFX" ]; then (cd "$V" && mkdir -p vendor && git mv "${PFX%/}" vendor/gov)
else (cd "$V" && mkdir -p vendor/gov && git mv "$GK" qdemo "${GATE##*/}" vendor/gov/); fi
run_arm "a gate at vendor/gov/ grades its own tool root" "install-prefix: clean — " 0 "$V" "vendor/gov/${GATE##*/}"
printf 'Run vendor/gov/qdemo/thing.sh there.\n' >> "$V/vendor/gov/qdemo/README.md"
git -C "$V" add -A >/dev/null 2>&1
run_arm "...and names a literal of its own prefix by <path>:<line>" "  vendor/gov/qdemo/README.md:2  qdemo" 1 "$V" "vendor/gov/${GATE##*/}"

# ==================== the SKIP, and the refusals that keep a dead probe from passing ==========
# A CONSUMER: kits under a prefix, a receipt naming no deployer, no registry. It ships nothing, so it
# is SKIPPED out loud — and it carries a spelling a grading gate WOULD red on, or the skip proves nothing.
N="$TMP/consumer"; mkdir -p "$N/scripts/qdemo" "$N/.governance"
git -C "$N" init -q; git -C "$N" config user.email t@t.test; git -C "$N" config user.name t
cp "$GATE" "$N/scripts/${GATE##*/}"
printf 'Run qdemo/thing.sh by hand.\n' > "$N/scripts/qdemo/README.md"
printf '{"schema": 2, "gov_source": "local", "kits": [], "files": []}\n' > "$N/.governance/install.json"
git -C "$N" add -A >/dev/null 2>&1
nout=$(cd "$N/scripts" && bash "${GATE##*/}" 2>&1); nrc=$?
[ "$nrc" = 0 ] && good "a consumer exits 0 — it ships nothing" || bad "a consumer redded (rc $nrc) on bytes it received: $nout"
case "$nout" in *"SKIPPED — this repo is not a kit SOURCE"*) good "...and SAYS its files went ungraded" ;;
  *) bad "the consumer skip was silent — a skip that looks like a pass is indistinguishable from coverage" ;; esac

# NO KIT DIRECTORIES: the receipt points the resolver at a deployer outside the gate's own root, so the
# kit-source test passes and the kit walk under the gate's directory finds nothing to enumerate.
E="$TMP/nokits"; mkdir -p "$E/solo" "$E/elsewhere/gk" "$E/.governance"
git -C "$E" init -q; git -C "$E" config user.email t@t.test; git -C "$E" config user.name t
cp "$GATE" "$E/solo/${GATE##*/}"; cp "$ROOT/$GK_SRC" "$E/elsewhere/gk/govkit.py"
printf 'version = 1\n' > "$E/elsewhere/gk/registry.toml"
printf '{"schema": 3, "files": [{"source": "x/%s/govkit.py", "path": "elsewhere/gk/govkit.py"}]}\n' "$GK" > "$E/.governance/install.json"
git -C "$E" add -A >/dev/null 2>&1
run_arm "no kit directories under the gate's root -> refuses, not a silent pass" "that is not a pass" 1 "$E" "solo/${GATE##*/}"

# A COUNTER THAT DIES refuses. GOV_PYTHON hands the gate a wrapper that runs python for everything
# but the ban's counter, so the kit-source test stays alive and only the counter is dead.
D="$TMP/deadcounter"; build_source_fixture "$D" 'A qdemo kit.'
_realpy=""
for _c in python3 python py; do "$_c" -c "import sys" >/dev/null 2>&1 && { _realpy=$_c; break; }; done
printf '#!/usr/bin/env bash\ncase "${2:-}" in *"the ban'"'"'s counter"*) exit 3 ;; esac\nexec "%s" "$@"\n' "$_realpy" > "$D/pywrap.sh"
chmod +x "$D/pywrap.sh"
dout=$(cd "$D" && GOV_PYTHON="$D/pywrap.sh" bash "$GATE_REL" 2>&1); drc=$?
case "$drc:$dout" in 1:*"COUNTER died"*) good "a dead counter REFUSES and names itself" ;;
  *) bad "a dead counter did not refuse by name (rc $drc): $(printf '%s' "$dout" | tail -2)" ;; esac

# NO USABLE PYTHON: all three launcher names exit 9009, first on PATH. That is a REFUSAL, never a
# consumer's skip, which would pass a kit source's whole verdict at exit 0.
mkdir -p "$TMP/nopy"
for _np in python3 python py; do printf '#!/usr/bin/env bash\nexit 9009\n' > "$TMP/nopy/$_np"; chmod +x "$TMP/nopy/$_np"; done
pout=$(cd "$G" && PATH="$TMP/nopy:$PATH" bash "$GATE_REL" 2>&1); prc=$?
case "$prc:$pout" in 2:*"cannot tell whether this repo is a kit"*) good "no usable python REFUSES rather than skipping" ;;
  *) bad "no usable python did not refuse (rc $prc): $(printf '%s' "$pout" | tail -2)" ;; esac

# ==================== --offenders: the SIGNATURE the merge bar grades this leg with ===========
# TOOL-dDerivedDocket-23 S3, carried onto the pure ban at the reconcile with aRepatriatedFork. ONE
# KEY PER COUNTED SPELLING AND NOTHING ELSE, because the bar's red attribution compares two trees' key
# SETS. Graded on the three ways a set goes wrong: a key carrying its line number (it moves when an
# unrelated line lands above it), two identical hits collapsing into one, and prose leaking into the
# set — the exact-equality comparisons below catch the third. Its exit is `--check`'s.
O="$TMP/offenders"; build_source_fixture "$O" 'Run qdemo/thing.sh, or qdemo/thing.sh again.'
_owant=$(printf '%sqdemo/README.md\tban\tqdemo/thing.sh\n%sqdemo/README.md\tban\tqdemo/thing.sh#2' "$PFX" "$PFX")
oout=$(cd "$O" && bash "$GATE_REL" --offenders 2>/dev/null); orc=$?
(cd "$O" && bash "$GATE_REL" >/dev/null 2>&1); ocrc=$?
[ "$oout" = "$_owant" ] && good "--offenders prints exactly the two keys, the repeat carrying its ordinal" \
  || { bad "--offenders printed a different key set"; printf '%s\n' "$oout" | sed 's/^/      /' | head -6; }
{ [ "$orc" = "$ocrc" ] && [ "$orc" = 1 ]; } && good "--offenders exits as --check does (1)" \
  || bad "--offenders exited $orc where --check exited $ocrc"
{ printf 'an unrelated first line\n\n'; cat "$O/${PFX}qdemo/README.md"; } > "$O/readme.tmp" && mv "$O/readme.tmp" "$O/${PFX}qdemo/README.md"
printf 'unrelated\n' > "$O/${PFX}qdemo/other.md"; git -C "$O" add -A >/dev/null 2>&1
oout2=$(cd "$O" && bash "$GATE_REL" --offenders 2>/dev/null)
[ "$oout2" = "$_owant" ] && good "--offenders keys do not move when an unrelated line and file land above them" \
  || { bad "--offenders keys moved under an unrelated edit"; printf '%s\n' "$oout2" | sed 's/^/      /' | head -6; }
# ITS GREEN CONTROL: a clean kit source prints NO key and exits 0, so the arms above are not passed
# by a mode that prints the same two lines over every tree.
gout=$(cd "$G" && bash "$GATE_REL" --offenders 2>/dev/null); grc=$?
{ [ -z "$gout" ] && [ "$grc" = 0 ]; } && good "--offenders over a clean source prints nothing and exits 0" \
  || bad "--offenders over a clean source printed '$gout' (rc $grc)"
# A DEAD COUNTER under --offenders leaves NO key and a non-zero exit: the attribution reads a keyless
# red as a probe that could not answer, never as an empty — clean — set.
dkout=$(cd "$D" && GOV_PYTHON="$D/pywrap.sh" bash "$GATE_REL" --offenders 2>/dev/null); dkrc=$?
{ [ -z "$dkout" ] && [ "$dkrc" != 0 ]; } && good "--offenders with a dead counter exits $dkrc and prints no key" \
  || bad "--offenders with a dead counter printed '$dkout' (rc $dkrc)"

# ==================== THE LIVENESS ASSERTION ON THE SUITE ITSELF =============================
if [ "$GRADED" -ge 8 ]; then good "LIVENESS $GRADED arm(s) reached the counter"
else bad "LIVENESS only $GRADED arm(s) reached the counter — the rest stopped short of it, so this suite reports on arms that did not run"; fi

[ "$passed" -ge "$FLOOR_ASSERTIONS" ] || bad "only $passed assertion(s) ran, under the floor of $FLOOR_ASSERTIONS"
[ "$fails" = 0 ] && echo "PASS ($passed assertions)"
[ "$fails" = 0 ] || { printf 'FAIL — %d arm(s) failed\n' "$fails"; exit 1; }
