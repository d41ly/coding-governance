#!/usr/bin/env bash
# **Serves:** journal TOOL-aSparedSpawn-12
# TOOL-aSparedSpawn-12 - the pass's direct checks of `GATE_SELFTESTS=changed`, over a HAND-BUILT
# repository in a scratch root carrying this runner, a stub govkit and a four-leg manifest of bash
# legs, plus a hand-built govkit registry for `shipped --epoch` and the UNEDITED `check_green_record`
# lifted out of `.githooks/pre-push`. No suite runs and no slice of one.
#
#   bash <this> <scratch-root>     # run from the repository root; prints one PASS/FAIL line per check
#
# What this does NOT check: the new suite arms themselves (owed at VERIFYING), and AC9's replay, which
# the select-sim instrument beside this file makes.
set -u
# The launcher, resolved before any cd from the repository this record sits in, four levels up.
_d=.; [[ ${BASH_SOURCE[0]} == */* ]] && _d=${BASH_SOURCE[0]%/*}; . "$_d/../../../../tools/lib/resolve-python.sh" || exit 2
PY=$(resolve_python) || exit 2
S=${1:?a scratch root}; mkdir -p "$S" || exit 2
GOV=$(pwd)
bad=0
ok() { echo "PASS $1"; }
nope() { echo "FAIL $1"; bad=1; }
expect() { # label · haystack · ERE that must match one line
  if printf '%s\n' "$2" | grep -qE -- "$3"; then ok "$1"; else nope "$1"; printf '%s\n' "$2" | sed 's/^/    /'; fi
}
refuse() { # label · haystack · ERE that must match no line
  if printf '%s\n' "$2" | grep -qE -- "$3"; then nope "$1"; printf '%s\n' "$2" | sed 's/^/    /'; else ok "$1"; fi
}

# ---- the fixture: kits kx and ky, an unowned suite uz, one repo leg --------------------------------
R="$S/r"; rm -rf "$R"; mkdir -p "$R/tools/run-gates" "$R/tools/govkit" "$R/kx" "$R/ky" "$R/uz" "$R/fx"
cp tools/run-gates/run-gates.sh tools/run-gates/gate-profiles.txt tools/run-gates/gate-fingerprint.sh "$R/tools/run-gates/"
cat > "$R/tools/govkit/govkit.py" <<'PY'
import os, sys
if os.environ.get("GOVKIT_STUB_OFF"):
    sys.exit(1)
here = os.path.dirname(os.path.abspath(__file__))
rows = [r.split("\t") for r in open(os.path.join(here, "..", "..", "fx", "shipped.tsv")).read().splitlines() if r]
keep = ("engine", "seed", "rendered", "merged") if sys.argv[2:] == ["--epoch"] else None
sys.stdout.write("".join("\t".join(r) + "\n" for r in rows if keep is None or r[1] in keep))
PY
printf 'kx\tengine\tkx/engine.sh\nkx\tengine\tkx/x.test.sh\nkx\tproject-owned\tkx/notes.txt\nky\tengine\tky/engine.sh\nky\tengine\tky/y.test.sh\n' > "$R/fx/shipped.tsv"
for f in kx/engine.sh ky/engine.sh fx/ok.sh; do printf '#!/usr/bin/env bash\nexit 0\n' > "$R/$f"; done
printf '#!/usr/bin/env bash\n[ -n "${KX_RED:-}" ] && { echo "FAIL kx asked to red"; exit 1; }\nexit 0\n' > "$R/kx/x.test.sh"
printf '#!/usr/bin/env bash\nexit 0\n' > "$R/ky/y.test.sh"
printf '#!/usr/bin/env bash\nexit 0\n' > "$R/uz/z.test.sh"
printf 'notes\n' > "$R/kx/notes.txt"; printf 'g\n' > "$R/uz/guarded.txt"; printf 'o\n' > "$R/uz/other.txt"
write_legs() { # extra JSON fields for the uz row
  printf '[{"name": "repo ok", "argv": ["bash", "fx/ok.sh"]},\n {"name": "kx suite", "argv": ["bash", "kx/x.test.sh"], "subject": "kit", "guard": ["kx/"]},\n {"name": "ky suite", "argv": ["bash", "ky/y.test.sh"], "subject": "kit", "guard": ["ky/"]},\n {"name": "uz suite", "argv": ["bash", "uz/z.test.sh"], "chunk": "selftests", "guard": ["uz/guarded.txt"]%s}]\n' "$1" > "$S/legs.json"
}
write_legs ""
( cd "$R" && git init -q --template= -b main . && git add -A && git commit -qm base ) >/dev/null 2>&1
bar() { # VAR=value... -> OUT
  OUT=$( cd "$R" && env GATE_FULL=1 GATE_BASE= GATE_REUSE= GATE_WALL= GATE_ATTRIBUTE= GATE_INHERITED_RED= \
      GATE_INHERITED_RED_MAX_AGE= GATE_RUN_ID= GATE_PROFILES= GATE_JOBS=4 GATE_PROFILE=minimal GATE_TURNSTILE=0 \
      GATE_SELFTESTS_MAX_LAG= GATE_LEGS="$S/legs.json" "$@" bash tools/run-gates/run-gates.sh 2>&1 )
}
commit() { ( cd "$R" && git add -A && git commit -qm "$1" ) >/dev/null 2>&1; }
REC="$R/.git/gate-selftest-last"
key() { printf '%s' "$1" | sha1sum | cut -c1-16; }

# ---- S4: a GATE_SELFTESTS=1 run on a clean tree seeds one record per executed held leg ------------
bar GATE_SELFTESTS=1
[ "$(ls "$REC" 2>/dev/null | wc -l)" = 3 ] && ok "S4 a full run writes three records" || { nope "S4 a full run writes three records"; printf '%s\n' "$OUT" | sed 's/^/    /'; }
[ -f "$REC/$(key 'kx suite')" ] && ok "S4 the record is named by the leg-name key" || nope "S4 the record is named by the leg-name key"
expect "S7 a GATE_SELFTESTS=1 green stamps selftests 1" "$(cat "$R/.git/gate-full-green" 2>/dev/null)" $'^selftests\t1$'

# ---- AC1/AC7: nothing moved -> every held leg is held, and the stamp reads `changed` ---------------
bar GATE_SELFTESTS=changed
expect "AC1 nothing moved: kx is held unchanged" "$OUT" '^GATE held  kx suite  \(self-test, unchanged since [0-9a-f]{8}\)$'
expect "AC1 nothing moved: ky is held unchanged" "$OUT" '^GATE held  ky suite  \(self-test, unchanged since [0-9a-f]{8}\)$'
expect "AC2 the fallback line names the unowned leg" "$OUT" '^run-gates: selftests changed: no kit ships the suite of 1 held leg\(s\).*: uz suite$'
expect "AC7 a changed run stamps selftests changed" "$(cat "$R/.git/gate-full-green" 2>/dev/null)" $'^selftests\tchanged$'
expect "S7 the run header records the mode" "$(cat "$R"/.git/gate-run/*/header 2>/dev/null)" $'^selftests\tchanged$'

# ---- AC1: only kx's engine moved -> kx executes, ky is held -----------------------------------------
printf '#!/usr/bin/env bash\n# moved\nexit 0\n' > "$R/kx/engine.sh"; commit "kx engine moves"
bar GATE_SELFTESTS=changed
expect "AC1 kx executes when its engine moved" "$OUT" '^GATE ok    kx suite$'
expect "AC1 ...and its selection line names the path" "$OUT" '^run-gates: selftests changed: kx suite runs \(kx/engine.sh moved since [0-9a-f]{8}\)$'
expect "AC1 ky is held unchanged" "$OUT" '^GATE held  ky suite  \(self-test, unchanged since'
refuse "AC1 ky does not execute" "$OUT" '^GATE ok    ky suite$'

# ---- S3: a project-owned row of kx moving selects nothing -------------------------------------------
printf 'notes moved\n' > "$R/kx/notes.txt"; commit "kx notes move"
bar GATE_SELFTESTS=changed
expect "S3 a non-epoch kx file moving holds kx" "$OUT" '^GATE held  kx suite  \(self-test, unchanged since'

# ---- AC2: only ky's suite file moved; only uz's guard moved ----------------------------------------
printf '#!/usr/bin/env bash\n# moved\nexit 0\n' > "$R/ky/y.test.sh"; commit "ky suite moves"
bar GATE_SELFTESTS=changed
expect "AC2 ky executes when only its suite file moved" "$OUT" '^GATE ok    ky suite$'
expect "AC2 uz is held while its guard has not moved" "$OUT" '^GATE held  uz suite  \(self-test, unchanged since'
printf 'g moved\n' > "$R/uz/guarded.txt"; commit "uz guard moves"
bar GATE_SELFTESTS=changed
expect "AC2 uz executes when only its guard moved" "$OUT" '^run-gates: selftests changed: uz suite runs \(uz/guarded.txt moved since'
[ "$(printf '%s\n' "$OUT" | grep -c '^run-gates: selftests changed: no kit ships')" = 1 ] && ok "AC2 the fallback line prints once" || nope "AC2 the fallback line prints once"

# ---- AC3: a deleted record, a non-ancestor sha, a changed manifest row ------------------------------
rm -f "$REC/$(key 'kx suite')"
dangle=$(cd "$R" && git commit-tree "HEAD^{tree}" -m dangling)
printf 'sha\t%s\nrow\t%s\n' "$dangle" "$(sed -n 's/^row\t//p' "$REC/$(key 'ky suite')")" > "$REC/$(key 'ky suite')"
write_legs ', "ceiling": 600'
bar GATE_SELFTESTS=changed
expect "AC3 a deleted record executes" "$OUT" '^run-gates: selftests changed: kx suite runs \(no last-run record\)$'
expect "AC3 a non-ancestor sha executes" "$OUT" '^run-gates: selftests changed: ky suite runs \(recorded [0-9a-f]{8} is not an ancestor of HEAD\)$'
expect "AC3 a changed manifest row executes" "$OUT" '^run-gates: selftests changed: uz suite runs \(its manifest row changed since its record\)$'
printf 'sha\tnot-a-sha\nrow\tx\n' > "$REC/$(key 'kx suite')"
bar GATE_SELFTESTS=changed
expect "AC3 an unreadable record executes" "$OUT" '^run-gates: selftests changed: kx suite runs \(its last-run record is unreadable\)$'

# ---- AC4: eleven commits behind HEAD with nothing moved ---------------------------------------------
for k in 1 2 3 4 5 6 7 8 9 10 11; do ( cd "$R" && git commit -q --allow-empty -m "empty $k" ) >/dev/null 2>&1; done
bar GATE_SELFTESTS=changed GATE_SELFTESTS_MAX_LAG=20
expect "AC4 control: under a bound of 20 an 11-behind record holds" "$OUT" '^GATE held  ky suite  \(self-test, unchanged since'
bar GATE_SELFTESTS=changed
expect "AC4 eleven behind under the default bound executes and names the lag" "$OUT" '^run-gates: selftests changed: ky suite runs \(recorded [0-9a-f]{8} is 11 first-parent commits behind HEAD, beyond the bound 10\)$'

# ---- AC5: a red leg loses its record; a dirty-tree green writes none --------------------------------
printf '#!/usr/bin/env bash\n# moved again\nexit 0\n' > "$R/kx/engine.sh"; commit "kx engine moves again"
[ -f "$REC/$(key 'kx suite')" ] && ok "AC5 setup: kx holds a record before the red run" || nope "AC5 setup: kx holds a record before the red run"
bar GATE_SELFTESTS=changed KX_RED=1
expect "AC5 kx executes and reds" "$OUT" '^GATE FAIL  kx suite'
[ -f "$REC/$(key 'kx suite')" ] && nope "AC5 the red leg's record is gone" || ok "AC5 the red leg's record is gone"
rm -f "$REC/$(key 'ky suite')"; printf 'dirt\n' >> "$R/uz/other.txt"
bar GATE_SELFTESTS=changed
expect "AC5 on a dirty tree ky executes green" "$OUT" '^GATE ok    ky suite$'
[ -f "$REC/$(key 'ky suite')" ] && nope "AC5 a dirty-tree green writes no record" || ok "AC5 a dirty-tree green writes no record"
( cd "$R" && git checkout -q -- uz/other.txt )

# ---- AC6: govkit unreachable -> every held leg selects by its guard, said once ----------------------
bar GATE_SELFTESTS=1
printf '#!/usr/bin/env bash\n# moved by the guard only\nexit 0\n' > "$R/ky/extra.sh"; commit "a ky file no kit ships"
bar GATE_SELFTESTS=changed
expect "AC6 control: with govkit reachable the unshipped ky file holds ky" "$OUT" '^GATE held  ky suite  \(self-test, unchanged since'
bar GATE_SELFTESTS=changed GOVKIT_STUB_OFF=1
[ "$(printf '%s\n' "$OUT" | grep -c '^run-gates: selftests changed: govkit is not reachable')" = 1 ] && ok "AC6 the unreachable line prints once" || { nope "AC6 the unreachable line prints once"; printf '%s\n' "$OUT" | sed 's/^/    /'; }
expect "AC6 ky selects by its guard" "$OUT" '^run-gates: selftests changed: ky suite runs \(ky/extra.sh moved since'
expect "AC6 kx is held on diff evidence" "$OUT" '^GATE held  kx suite  \(self-test, unchanged since [0-9a-f]{8}\)$'

# ---- the default mode is unchanged ----------------------------------------------------------------
bar GATE_SELFTESTS=
expect "default: a held leg still says set GATE_SELFTESTS=1" "$OUT" '^GATE held  kx suite  \(self-test, set GATE_SELFTESTS=1 to run\)$'
refuse "default: no selection line" "$OUT" '^run-gates: selftests changed'

# ---- AC7: the UNEDITED predicate 8 over a `changed` record ------------------------------------------
fn=$(awk '/^check_green_record\(\) \{/,/^}$/' "$GOV/.githooks/pre-push")
[ -n "$fn" ] && ok "AC7 check_green_record lifted from the unedited hook" || nope "AC7 check_green_record lifted from the unedited hook"
pp() { # GATE_SELFTESTS value -> the force text
  ( cd "$R" && eval "$fn" && main_local=$(git rev-parse HEAD) GATE_FULL_MAX_LAG=10 kitfp="" KP="" DOCS_ONLY="" \
      GATE_SELFTESTS="$1" && force="" && check_green_record "$main_local" "" "" changed "full green" && printf '%s' "$force" )
}
f_on=$(pp 1); f_off=$(pp "")
[ -n "$f_on" ] && ok "AC7 a self-tests-on push forces over a changed record ($f_on)" || nope "AC7 a self-tests-on push forces over a changed record"
[ -z "$f_off" ] && ok "AC7 a held push accepts a changed record" || nope "AC7 a held push accepts a changed record ($f_off)"
# Against the commit that opened this unit (76578ece), not the spec's base: units 1 to 5, 9 and 15
# of the same build moved `.githooks/` before this one started.
_moved=$(git -C "$GOV" diff --name-only 76578ece -- .githooks/ | tr '\n' ' ')
[ "$_moved" = ".githooks/pre-push.test.sh " ] \
  && ok "AC7 only .githooks/pre-push.test.sh moved under .githooks/ since the unit opened" \
  || nope "AC7 only .githooks/pre-push.test.sh moved under .githooks/ since the unit opened: [$_moved]"

# ---- AC8: `shipped --epoch` over a hand-built registry ----------------------------------------------
G="$S/g"; rm -rf "$G"; mkdir -p "$G/tools/govkit/entries" "$G/tools/demo"
cp "$GOV/tools/govkit/govkit.py" "$GOV/tools/govkit/adopters.toml" "$G/tools/govkit/"
printf '[[entry]]\nid = "demo"\ndescriptor = "{prefix}/govkit/entries/demo.kit.toml"\n' > "$G/tools/govkit/registry.toml"
printf 'id = "demo"\nhome = "demo"\n\n[[files]]\ninclude = ["run.sh"]\nrole = "engine"\nto = "{prefix}/{relpath}"\n\n[[files]]\ninclude = ["seed.txt"]\nrole = "generated"\nto = "{prefix}/seed.txt"\n' > "$G/tools/govkit/entries/demo.kit.toml"
( cd "$G" && git init -q --template= -b main . ) >/dev/null 2>&1
e=$(cd "$G" && "$PY" tools/govkit/govkit.py shipped --epoch | tr -d '\r'); a=$(cd "$G" && "$PY" tools/govkit/govkit.py shipped | tr -d '\r')
[ "$e" = $'demo\tengine\ttools/demo/run.sh' ] && ok "AC8 --epoch prints only the engine row" || nope "AC8 --epoch prints only the engine row: [$e]"
printf '%s\n' "$a" | grep -q $'\tgenerated\t' && ok "AC8 control: the plain verb prints the generated row" || nope "AC8 control: the plain verb prints the generated row"

[ "$bad" = 0 ] && echo "ALL PASS" || echo "SOME FAILED"
exit "$bad"
