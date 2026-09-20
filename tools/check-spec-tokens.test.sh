#!/usr/bin/env bash
# check-spec-tokens.test.sh — red/green arms for tools/check-spec-tokens.py (TOOL-dRetiredFork-20).
#
# HERMETIC: every arm runs in a scratch repo under mktemp -d — its own, or one of the two the bar
# arms share and reset between edits — and never touches the real tree, so the suite is safe beside
# the other heavy legs in a concurrent bar.
#
# Each arm asserts an EXIT CODE and, where the message is the point, a substring of stdout. The
# refusal arms matter most: this lint's own failure mode is passing over a population it never
# built, which is the class it exists to catch one level up.
set -u

# The shrink-only assertion floor. A suite that stops running arms must RED rather than report a
# smaller success: `check-testsuite-counts.sh` reads this pin, the printed count, and the comparison
# between them, because a pin nothing reads is the same nothing as no pin.
FLOOR_ASSERTIONS=55
# RAISED 32 -> 38 at the closing review's F2, F4, F9 and F10, by the static count of the arms they
# added: the quoted-empty flag, the selftest.py hit, the two parity assertions over the manifest,
# the requoted-cutoff arm and the non-ISO cutoff refusal.
# RAISED 38 -> 42 at closing round 2, by the count of `arm`/`pass=` lines its diff added: two
# leg-line cutoff refusals (R7, R11), the `py` launcher hit (R12) and the parity accounting (R3).
# RAISED 42 -> 55 at TOOL-dDerivedDocket-37, by the 13 `arm` calls the hands-off join's six
# fixtures add: two each for the graded edge, the bullet shape and the counted silence, three each
# for the dated key and the edge-keyed waiver, and one for the H1 join at any depth.
LINT="$(cd "$(dirname "$0")" && pwd)/check-spec-tokens.py"
# The launcher is RESOLVED by running it (tools/lib/resolve-python.sh); `PY=` overrides. A bare
# default here was the parameter-default shape the resolver ban now catches.
if [ -z "${PY:-}" ] && [ -f "${LINT%/*}/lib/resolve-python.sh" ]; then . "${LINT%/*}/lib/resolve-python.sh"; PY=$(resolve_python) || exit 2; fi
PY=${PY:-python}   # gov:literal-python — last-resort fallback when lib/ is absent (adopter layout)
pass=0; fail=0

scratch() {          # $1 = dir. A repo with one live spec, a manifest and an empty waiver file.
  local d=$1
  git init -q "$d"; git -C "$d" config user.email t@t.test; git -C "$d" config user.name t
  mkdir -p "$d/memory/builds/tOne/spec" "$d/memory/project" "$d/tools"
  printf '[{"name":"real leg"}]\n' > "$d/tools/gate-legs.json"
  printf '# waivers\n' > "$d/memory/project/spec-token-waivers.txt"
  cat > "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md" <<'SPEC'
# TOOL-tOne-1 — a unit

**Status:** OPEN · rev-1 · 2026-09-02 · node t · Tier-1 · base 0123abcd · streams tooling

## 6. Acceptance criteria

- **AC1** — `tools/gate-legs.json` exists.

## 7. Gates

`real leg`.
SPEC
  git -C "$d" add -A >/dev/null; git -C "$d" commit -qm f --no-verify
}

arm() {              # $1 label · $2 expected rc · $3 dir · $4 expected substring · $5 FORBIDDEN one
  local out rc
  out=$(cd "$3" && "$PY" "$LINT" 2>&1); rc=$?
  if [ "$rc" != "$2" ]; then
    echo "arm FAIL  $1 — expected rc $2, got $rc"; echo "$out" | head -3; fail=$((fail+1)); return
  fi
  if [ $# -ge 4 ] && ! printf '%s' "$out" | grep -qF -- "$4"; then
    echo "arm FAIL  $1 — expected output to carry: $4"; echo "$out" | head -3; fail=$((fail+1)); return
  fi
  # TOOL-dDerivedDocket-37: $5 is a substring that must be ABSENT. One arm below needs it. An
  # implementation keying a waiver on the bare token — the exact defect that arm exists to catch —
  # reaches the expected exit code by the WRONG route, through a stale-waiver refusal rather than
  # through the hit, so an arm asserting rc alone passes it. Staged and observed.
  if [ $# -ge 5 ] && printf '%s' "$out" | grep -qF -- "$5"; then
    echo "arm FAIL  $1 — expected output NOT to carry: $5"; echo "$out" | head -3; fail=$((fail+1)); return
  fi
  echo "arm ok    $1"; pass=$((pass+1))
}

base=$(mktemp -d)
trap 'rm -rf "$base"' EXIT

# 1 — the clean case, and it must GRADE something rather than pass on an empty population
d=$base/clean; scratch "$d"
arm "a conforming spec passes and reports what it graded" 0 "$d" "token(s) graded"

# 2 — a section 6 criterion naming an untracked path
d=$base/path; scratch "$d"
sed -i 's|`tools/gate-legs.json` exists|`tools/nope.sh` exists|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "an untracked witness path in section 6 REDS" 1 "$d" "not tracked by git ls-files"

# 3 — a section 7 name that is not a leg
d=$base/leg; scratch "$d"
sed -i 's|^`real leg`\.|`imaginary leg`.|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a section 7 name absent from the manifest REDS" 1 "$d" "not a name in tools/gate-legs.json"

# 4 — a citation past end of file
d=$base/cite; scratch "$d"
sed -i 's|`tools/gate-legs.json` exists|see `tools/gate-legs.json:9999`|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a citation beyond end of file REDS" 1 "$d" "lines"

# ---- TOOL-aJoinedCanon-7: the eight arms this unit owes. Each is named by its own criterion.
# AC4 — a PROSE §7 contributes no leg name and raises the ungraded count, and stays GREEN while the
#       cutoff is blank. This is the silence the report used to keep to itself.
d=$base/prose; scratch "$d"
sed -i 's|^`real leg`\.|The bar, which is the `real leg` leg, plus whatever it drags in.|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a prose section 7 contributes nothing and is COUNTED" 0 "$d" "1 live spec(s) carry a Gates heading contributing NO leg name"

# AC5 — a manifest name carrying a `/`. The shape exclusion drops any token with a slash, so before
#       the manifest-first resolution this leg name was discarded UNREAD and the spec looked prose-y.
d=$base/slashleg; scratch "$d"
printf '[{"name":"real leg"},{"name":"tools/thing self-test"}]
' > "$d/tools/gate-legs.json"
sed -i 's|^`real leg`\.|`tools/thing self-test`.|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a manifest leg name carrying a slash RESOLVES rather than being skipped" 0 "$d" "0 live spec(s) carry a Gates heading contributing NO leg name"

# AC10 — the other excluded shape: a manifest name whose first word is a command verb.
d=$base/verbleg; scratch "$d"
printf '[{"name":"real leg"},{"name":"bash the thing"}]
' > "$d/tools/gate-legs.json"
sed -i 's|^`real leg`\.|`bash the thing`.|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a manifest leg name opening with a command verb RESOLVES" 0 "$d" "0 live spec(s) carry a Gates heading contributing NO leg name"

# AC8 — the dated demand. A post-cutoff spec whose §7 names no leg REDS...
d=$base/legline; scratch "$d"
printf 'SPEC_LEGLINE_CUTOFF="2026-09-01"
' > "$d/.memory-tree.conf"
sed -i 's|^`real leg`\.|The bar and whatever it drags in.|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a post-cutoff section 7 naming no leg REDS" 1 "$d" "contributes no leg name"

# ...and its PRE-cutoff twin is green, so nothing landed goes retroactively red.
d=$base/leglinepre; scratch "$d"
printf 'SPEC_LEGLINE_CUTOFF="2026-09-30"
' > "$d/.memory-tree.conf"
sed -i 's|^`real leg`\.|The bar and whatever it drags in.|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a PRE-cutoff section 7 naming no leg is green" 0 "$d" "carry a Gates heading contributing NO leg name"

# AC9 — a BLANK key turns the arm off over the same tree that reds when it is set.
d=$base/legblank; scratch "$d"
printf 'SPEC_LEGLINE_CUTOFF=""
' > "$d/.memory-tree.conf"
sed -i 's|^`real leg`\.|The bar and whatever it drags in.|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a blank SPEC_LEGLINE_CUTOFF turns the arm off" 0 "$d" "blank (arm off)"

# AC11 — the two TIER-1 fixtures. First: no Gates heading at all, post-cutoff. SILENT, and counted in
#        its own field, because under the light profile a spec may legally omit the section.
d=$base/nogates; scratch "$d"
printf 'SPEC_LEGLINE_CUTOFF="2026-09-01"
' > "$d/.memory-tree.conf"
awk '/^## 7[.] Gates$/{exit} {print}' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md" > "$d/.tmp.md"
mv "$d/.tmp.md" "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a post-cutoff spec with NO Gates heading is silent" 0 "$d" "1 carry no Gates heading to grade"

# AC11 second: a Gates section at ANOTHER ordinal is still graded there. This is the M13 class — a
# Tier-1 spec that drops the production-readiness checklist numbers its Gates section 6.
d=$base/otherord; scratch "$d"
printf 'SPEC_LEGLINE_CUTOFF="2026-09-01"
' > "$d/.memory-tree.conf"
sed -i 's|^## 7. Gates$|## 6. Gates|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
sed -i 's|^## 6. Acceptance criteria$|## 5. Acceptance criteria|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a Gates section at another ordinal is graded there" 0 "$d" "0 live spec(s) carry a Gates heading contributing NO leg name"

# 5 — an untracked citation path is SKIPPED and COUNTED, never red. Half the real corpus is this.
d=$base/skip; scratch "$d"
sed -i 's|`tools/gate-legs.json` exists|see `run-gates.sh:407`|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "an untracked citation path is skipped, not red" 0 "$d" "citation(s) skipped"

# 6 — a waiver with a reason silences the hit and the count is printed
d=$base/waived; scratch "$d"
sed -i 's|`tools/gate-legs.json` exists|`tools/nope.sh` exists|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
printf 'tools/nope.sh\tdeliberate, for this arm\n' >> "$d/memory/project/spec-token-waivers.txt"
git -C "$d" add -A >/dev/null
arm "a waived hit with a reason passes" 0 "$d" "waiver(s)"

# 7 — a waiver nothing produces any more REDS: a stale exception cannot hide a live hit
d=$base/stale; scratch "$d"
printf 'tools/gone.sh\tno spec names this\n' >> "$d/memory/project/spec-token-waivers.txt"
git -C "$d" add -A >/dev/null
arm "a stale waiver REDS" 1 "$d" "STALE WAIVER"

# 8 — a waiver row with no reason REDS
d=$base/noreason; scratch "$d"
printf 'tools/nope.sh\n' >> "$d/memory/project/spec-token-waivers.txt"
git -C "$d" add -A >/dev/null
arm "a waiver carrying no reason REDS" 1 "$d" "STALE WAIVER"

# 9 — REFUSALS. An empty population is not a pass.
d=$base/nospec; scratch "$d"
git -C "$d" rm -q "memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
arm "no spec at all REFUSES" 1 "$d" "REFUSING"

# 10 — a TERMINAL spec is a frozen record and is not graded, so it cannot red
d=$base/frozen; scratch "$d"
sed -i 's|\*\*Status:\*\* OPEN|**Status:** CLOSED|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
sed -i 's|`tools/gate-legs.json` exists|`tools/nope.sh` exists|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a CLOSED spec is frozen, so it refuses rather than grading" 1 "$d" "REFUSING"

# 11 — the waiver registry itself must exist
d=$base/noreg; scratch "$d"
git -C "$d" rm -q memory/project/spec-token-waivers.txt
arm "an absent waiver registry REFUSES" 1 "$d" "REFUSING"

# 12 — a malformed manifest REFUSES rather than grading zero legs
d=$base/badlegs; scratch "$d"
printf 'not json\n' > "$d/tools/gate-legs.json"; git -C "$d" add -A >/dev/null
arm "a manifest that does not parse REFUSES" 1 "$d" "REFUSING"

# ---- TOOL-aDeferredBar-2: the bar join. Ten arms over TWO shared scratch repos rather than ten
#      fresh ones, because the init and first commit are the cost of this leg, not the checker. Each
#      arm is one edit from its family's committed clean state, `git add -A` as above, and the repo is
#      returned to that state with a single reset — never a fresh init. The DATED family's clean state
#      is the `scratch` fixture plus an empty tracked runner, so the paths join stays green over a
#      runner token and the only hit an arm can produce is the bar's; its conf edits stay uncommitted,
#      so the bar line carries `relation unchecked` and a cutoff dated before the commit day is never
#      refused. AC17 alone commits, because the refusal it observes reads the value's commit date.
d=$base/bar; scratch "$d"
mkdir -p "$d/tools/run-gates" "$d/tools/govkit"; : > "$d/tools/run-gates/run-gates.sh"; : > "$d/tools/govkit/selftest.py"
git -C "$d" add -A >/dev/null; git -C "$d" commit -qm runner --no-verify
clean=$(git -C "$d" rev-parse HEAD)
spec="$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"

# AC1 — a post-cutoff §6 bullet backticking the flagged full bar REDS as [bar], with the substitute.
#       The token opens `GATE_`, which NOT_A_TOKEN drops unread unless the bar test runs first.
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
sed -i 's|`tools/gate-legs.json` exists|`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` is green|' "$spec"
git -C "$d" add -A >/dev/null
arm "a post-cutoff §6 bullet naming the flagged bar REDS as [bar]" 1 "$d" '-spec-TOOL-tOne-1.md [bar] `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — a bar or suite is not an acceptance observation'
git -C "$d" reset -q --hard "$clean"

# AC2 — the same token on the §7 leg line REDS: NOT_A_LEG would discard it for its `bash ` opener.
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
sed -i 's|^`real leg`\.|`real leg` · `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`.|' "$spec"
git -C "$d" add -A >/dev/null
arm "the same token on the §7 leg line REDS, read before NOT_A_LEG discards it" 1 "$d" '[bar] `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`'
git -C "$d" reset -q --hard "$clean"

# AC3 — three placements that are NOT hits: §4 prose, a §7 `New arm:` line, and the un-backticked
#       body of a fence under a §6 bullet. `--list` prints the first two as NEAR and nothing at all
#       for the fence body, which is the fence exclusion asserted as silence.
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
cat > "$spec" <<'SPEC'
# TOOL-tOne-1 — a unit

**Status:** OPEN · rev-1 · 2026-09-02 · node t · Tier-1 · base 0123abcd · streams tooling

## 4. Design

The bar is `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, named here in prose.

## 6. Acceptance criteria

- **AC1** — `tools/gate-legs.json` exists.
  ```
  bash tools/run-gates/run-selftests.sh
  ```

## 7. Gates

`real leg`.

New arm: `bash tools/check-spec-tokens.test.sh` · stages a break · none
SPEC
git -C "$d" add -A >/dev/null
arm "a bar token in §4 prose, on a New arm: line and in a fence body is no hit" 0 "$d" "0 pre-cutoff live spec(s) carry one and are not graded"
out=$(cd "$d" && "$PY" "$LINT" --list 2>&1)
if [ "$(printf '%s\n' "$out" | grep -c 'NEAR   \[bar\]')" = 2 ] \
   && [ "$(printf '%s\n' "$out" | grep -c 'outside the graded population')" = 2 ] \
   && ! printf '%s\n' "$out" | grep -q 'run-selftests.sh'; then
  echo "arm ok    --list prints exactly two NEAR lines and stays silent on the fence body"; pass=$((pass+1))
else
  echo "arm FAIL  --list — expected exactly two NEAR lines outside the graded population and no fence-body line"
  printf '%s\n' "$out" | grep -E 'NEAR|run-selftests' | head -5; fail=$((fail+1))
fi
git -C "$d" reset -q --hard "$clean"

# AC4 — a PRE-cutoff carrier is green, and COUNTED on the bar line rather than silently skipped.
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
git -C "$d" mv "$spec" "$d/memory/builds/tOne/spec/2026-08-30-spec-TOOL-tOne-1.md"
sed -i 's|`tools/gate-legs.json` exists|`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` is green|' "$d/memory/builds/tOne/spec/2026-08-30-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a PRE-cutoff carrier is green, counted and not graded" 0 "$d" "1 pre-cutoff live spec(s) carry one and are not graded"
git -C "$d" reset -q --hard "$clean"

# AC5 — a BLANK key turns the join off over the AC1 tree, and the OFF line still counts the carrier.
printf 'SPEC_DIRECT_CUTOFF=""\n' > "$d/.memory-tree.conf"
sed -i 's|`tools/gate-legs.json` exists|`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` is green|' "$spec"
git -C "$d" add -A >/dev/null
arm "a blank SPEC_DIRECT_CUTOFF turns the join off and still counts the carrier" 0 "$d" "SPEC_DIRECT_CUTOFF blank (arm off) · 1 live spec(s) carry a bar token"
git -C "$d" reset -q --hard "$clean"

# AC15 — the LIGHT profile: criteria under `## 5.`, Gates under `## 6.`. The ordinal read graded the
#        Gates section as the bullet population and never saw the token; the heading read does.
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
sed -i 's|`tools/gate-legs.json` exists|`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` is green|; s|^## 6. Acceptance criteria$|## 5. Acceptance criteria|; s|^## 7. Gates$|## 6. Gates|' "$spec"
git -C "$d" add -A >/dev/null
arm "a light-profile spec is graded where its criteria sit, not at the ordinal" 1 "$d" '[bar] `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`'
git -C "$d" reset -q --hard "$clean"

# AC16 — the EMPTY flag assignment is the OFF spelling and no hit (rev-1's branch matched it); the
#        same assignment with a value is a hit whatever command follows it.
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
sed -i 's|`tools/gate-legs.json` exists|`GATE_FULL= cat tools/gate-legs.json` prints|' "$spec"
git -C "$d" add -A >/dev/null
arm "the EMPTY flag assignment is the OFF spelling and is no hit" 0 "$d" "2 token(s) examined in 1 live spec(s) at/after SPEC_DIRECT_CUTOFF 2026-09-01"
sed -i 's|`GATE_FULL= cat|`GATE_FULL=1 cat|' "$spec"
git -C "$d" add -A >/dev/null
arm "the same flag assignment with a value REDS" 1 "$d" '[bar] `GATE_FULL=1 cat tools/gate-legs.json`'
git -C "$d" reset -q --hard "$clean"

# closing review F9 — the QUOTED empty assignment is the OFF spelling too. rev-3's `\S` read the
# quote as a value and disagreed with the hook, which unquotes it; observed RED-first on that regex.
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
sed -i 's|`tools/gate-legs.json` exists|`GATE_FULL="" cat tools/gate-legs.json` prints|' "$spec"
git -C "$d" add -A >/dev/null
arm "the QUOTED empty flag assignment is the OFF spelling and is no hit" 0 "$d" "2 token(s) examined in 1 live spec(s) at/after SPEC_DIRECT_CUTOFF 2026-09-01"
git -C "$d" reset -q --hard "$clean"

# closing review F2 — a whole-suite `selftest.py` FILE is a suite invocation, the same rule as a
# `.test.sh`; the fixture tracks the file so the paths join stays green and the one hit is the bar's.
# A `--selftest` FLAG on another file is the direct check the child prompt admits and is not a hit.
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
sed -i 's|`tools/gate-legs.json` exists|`python tools/govkit/selftest.py` is green|' "$spec"   # gov:literal-python — a fixture TOKEN the checker grades, never run
git -C "$d" add -A >/dev/null
arm "a post-cutoff §6 bullet naming a whole-suite selftest.py REDS as [bar]" 1 "$d" '[bar] `python tools/govkit/selftest.py`'   # gov:literal-python — the expected hit line, never run
git -C "$d" reset -q --hard "$clean"

# AC17 — a COMMITTED cutoff not strictly past its own commit day is REFUSED before grading, naming
#        the key, the value and the day it compared against. Today's checker grades this tree clean.
printf 'SPEC_DIRECT_CUTOFF="2026-09-02"\n' > "$d/.memory-tree.conf"
git -C "$d" add -A >/dev/null; git -C "$d" commit -qm cutoff --no-verify
day=$(git -C "$d" log -1 --format=%cs)
arm "a committed cutoff not strictly past its own commit day is REFUSED before grading" 1 "$d" "REFUSING — SPEC_DIRECT_CUTOFF 2026-09-02 is not strictly past $day"
git -C "$d" reset -q --hard "$clean"

# closing review F10 — a cutoff that is not an ISO date is REFUSED, never armed. rev-3's checker
# graded this fixture at exit 0 with `0 live spec(s) at/after SPEC_DIRECT_CUTOFF 2026-9-15`: set,
# and permanently off. Observed RED-first on that checker.
printf 'SPEC_DIRECT_CUTOFF="2026-9-15"\n' > "$d/.memory-tree.conf"
git -C "$d" add -A >/dev/null
arm "a non-ISO cutoff is REFUSED rather than reported as set while grading nothing" 1 "$d" "REFUSING — SPEC_DIRECT_CUTOFF 2026-9-15 is not an ISO date"
git -C "$d" reset -q --hard "$clean"

# closing round 2, R7 and R11 — the SAME refusal for EVERY cutoff key, and for the DATE rather than
# the shape. F10 gated SPEC_DIRECT_CUTOFF alone: the checker at 4d177329 printed
# `SPEC_LEGLINE_CUTOFF 2026-9-8` as set at exit 0 over a leg join it never armed, and `2026-13-45`
# passed the shape test with no day in it. Observed RED-first on that checker, both values.
printf 'SPEC_LEGLINE_CUTOFF="2026-9-8"\n' > "$d/.memory-tree.conf"
git -C "$d" add -A >/dev/null
arm "a non-ISO SPEC_LEGLINE_CUTOFF is REFUSED like the direct key, not reported as set" 1 "$d" "REFUSING — SPEC_LEGLINE_CUTOFF 2026-9-8 is not an ISO date"
printf 'SPEC_LEGLINE_CUTOFF="2026-13-45"\n' > "$d/.memory-tree.conf"
git -C "$d" add -A >/dev/null
arm "a cutoff with the ISO shape and no such day is REFUSED" 1 "$d" "REFUSING — SPEC_LEGLINE_CUTOFF 2026-13-45 is not an ISO date"
git -C "$d" reset -q --hard "$clean"

# closing round 2, R12 — `py`, the Windows launcher and the resolver's third candidate, is a launcher
# to this reader as it is to the hook. The checker at 4d177329 graded this bullet clean.
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
sed -i 's|`tools/gate-legs.json` exists|`py tools/govkit/selftest.py` is green|' "$spec"   # gov:literal-python — a fixture TOKEN the checker grades, never run
git -C "$d" add -A >/dev/null
arm "a whole-suite selftest.py behind the py launcher REDS as [bar]" 1 "$d" '[bar] `py tools/govkit/selftest.py`'   # gov:literal-python — the expected hit line, never run
git -C "$d" reset -q --hard "$clean"

# The WAIVER family: its committed clean state IS the AC1 fixture, and the commit is dated the day
# before its cutoff so the relation holds and the arms grade rather than refuse.
d=$base/barwaiver; scratch "$d"
mkdir -p "$d/tools/run-gates"; : > "$d/tools/run-gates/run-gates.sh"
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
sed -i 's|`tools/gate-legs.json` exists|`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` is green|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
GIT_COMMITTER_DATE=2026-08-31T12:00:00 git -C "$d" commit -qm ac1 --no-verify
clean=$(git -C "$d" rev-parse HEAD)

# AC6 — a waiver row keyed on the token, reason opening `[bar]`, clears the hit and is counted.
printf 'GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh\t[bar] deliberate, for this arm\n' >> "$d/memory/project/spec-token-waivers.txt"
git -C "$d" add -A >/dev/null
arm "a [bar] waiver row keyed on the token clears the hit and is counted" 0 "$d" "1 waiver(s)"
git -C "$d" reset -q --hard "$clean"

# AC7 — a [bar] row naming a token no spec carries REDS as stale, like any other row.
printf 'GATE_FULL=1 bash tools/run-gates/run-gates.sh\t[bar] no spec names this\n' >> "$d/memory/project/spec-token-waivers.txt"
git -C "$d" add -A >/dev/null
arm "a [bar] waiver row nothing produces REDS as stale" 1 "$d" "STALE WAIVER"
git -C "$d" reset -q --hard "$clean"

# closing review F4 — a LATER commit that requotes the cutoff line (quoted to bare) is not the
# setting commit. `git log -G` matched the removed and the added line and re-dated the value to
# 2026-09-20, so the gate refused a cutoff nobody re-set; `--pickaxe-regex -S` reads the occurrence
# count, which a requote or a move leaves at one. The waiver row keeps the graded run at exit 0, so
# the two outcomes differ in rc and not only in text. Observed RED-first on the `-G` checker.
printf 'GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh\t[bar] deliberate, for this arm\n' >> "$d/memory/project/spec-token-waivers.txt"
sed -i 's|^SPEC_DIRECT_CUTOFF="2026-09-01"$|SPEC_DIRECT_CUTOFF=2026-09-01|' "$d/.memory-tree.conf"
git -C "$d" add -A >/dev/null
GIT_COMMITTER_DATE=2026-09-20T12:00:00 git -C "$d" commit -qm requote --no-verify
arm "a later commit that requotes the cutoff line does not re-date the setting commit" 0 "$d" "1 waiver(s)"
git -C "$d" reset -q --hard "$clean"

# ---- closing review F2, the PARITY arm: the suite population is DERIVED from the gate manifest and
#      never restated here — EVERY `chunk = selftests` leg, the `--selftest` flag form included
#      (closing round 2, R3: the F2 arm dropped the flag form by rule and silently, and the
#      population it certified was eight legs short, one of them a 599 s suite). `BAR` must match
#      each whole-suite argv as a command string; a suite convention that drifts out of the
#      predicate reds here rather than walking past it, which is how six python legs did. ONE
#      assertion over the population, so the floor does not move with the manifest, one that the
#      population is non-empty, and one that the graded count plus the PRINTED exemptions equals the
#      manifest's own count — so no unannounced skip is left to grow.
#      THE ONE EXEMPTION RULE is a ceiling, not a flag: a `--selftest` leg whose manifest `ceiling`
#      is at or under DIRECT_CHECK_BOUND is the seconds-long direct check the child prompt admits,
#      exempt by that fact and printed with its ceiling; a `--selftest` leg ABOVE the bound is a
#      suite by cost that this reader cannot see (BAR reads a token, never a ceiling), so each one
#      is DECLARED below by script name with its ceiling and reason, and an undeclared one reds.
#      The bound is the manifest's own default ceiling — sixteen of its selftests legs sit exactly
#      at 300 — because a bound under it exempts nothing and names every flag form. Declared:
#        test_recall_floor.py — the pytest `test_*.py` convention, gov-only and 12 s to 34 s in the
#          ledger; a `test_*.py` shape would hit an adopter's single-file pytest run, which is
#          exactly the direct check a spec may name.
#        corpus_ids.py --selftest (ceiling 2690 s, 599 s in the ledger) and gen_build_index.py
#          --selftest (350 s) — flag-form suites above the bound; the backlog row this round owes
#          moves their entrypoints to a `selftest.py` file both readers already deny.
LEGS="$(dirname "$LINT")/gate-legs.json"
DIRECT_CHECK_BOUND=300
PARITY_EXEMPT="test_recall_floor.py corpus_ids.py gen_build_index.py"
# `-c`, not `python -` with a heredoc: the Windows python launcher reads the first argument after
# `-` as a script and runs its shebang, which is how a probe of this arm ran bash instead.
parity=$("$PY" -c 'import importlib.util, json, sys
spec = importlib.util.spec_from_file_location("cst", sys.argv[1])
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
exempt = set(sys.argv[3].split()); bound = int(sys.argv[4])
legs = [l for l in json.load(open(sys.argv[2], encoding="utf-8")) if l.get("chunk") == "selftests"]
seen, skipped, bad, graded = set(), [], [], 0
for l in legs:
    cmd = " ".join(l["argv"]); ceil = l.get("ceiling", 0)
    script = next((a.rsplit("/", 1)[-1] for a in l["argv"] if "/" in a), "")
    if script in exempt:
        seen.add(script); skipped.append("declared exempt (ceiling %ss): %s" % (ceil, cmd)); continue
    if "--selftest" in l["argv"]:
        if ceil <= bound:
            skipped.append("a --selftest direct check at or under the %ss bound (ceiling %ss): %s" % (bound, ceil, cmd)); continue
        bad.append("(a --selftest leg above the %ss bound is a suite BAR cannot see and is not declared exempt: %s, ceiling %ss)" % (bound, cmd, ceil)); continue
    graded += 1
    if not m.BAR.search(cmd): bad.append(cmd)
bad += ["(stale exemption: " + x + ")" for x in exempt - seen]
print(len(legs)); print(graded); print(len(skipped)); print("\n".join(skipped)); print("--"); print("\n".join(bad))' "$LINT" "$LEGS" "$PARITY_EXEMPT" "$DIRECT_CHECK_BOUND")
parity=$(printf '%s\n' "$parity" | tr -d '\r')
legn=$(printf '%s\n' "$parity" | sed -n 1p); popn=$(printf '%s\n' "$parity" | sed -n 2p); skipn=$(printf '%s\n' "$parity" | sed -n 3p)
printf '%s\n' "$parity" | sed -n '4,/^--$/p' | sed '$d' | sed 's/^/          skip: /'
unmatched=$(printf '%s\n' "$parity" | sed '1,/^--$/d' | grep -c .)
if [ "${popn:-0}" -gt 0 ] 2>/dev/null; then echo "arm ok    parity: the manifest holds $popn whole-suite selftests leg(s), $skipn exempt and printed above"; pass=$((pass+1))
else echo "arm FAIL  parity: the manifest holds no whole-suite selftests leg, so parity would be certified over nothing"; fail=$((fail+1)); fi
if [ "$unmatched" = 0 ]; then echo "arm ok    parity: BAR matches every whole-suite selftests argv of the manifest"; pass=$((pass+1))
else echo "arm FAIL  parity: a manifest suite invocation BAR does not match:"; printf '%s\n' "$parity" | sed '1,/^--$/d' | sed 's/^/          /'; fail=$((fail+1)); fi
if [ "$((${popn:-0} + ${skipn:-0}))" = "${legn:-x}" ]; then echo "arm ok    parity: graded $popn + exempt $skipn = the manifest's $legn selftests legs, no unannounced skip"; pass=$((pass+1))
else echo "arm FAIL  parity: graded $popn + exempt $skipn != the manifest's $legn selftests legs — a leg was skipped without being printed"; fail=$((fail+1)); fi

# ---- TOOL-dDerivedDocket-37: the hands-off join. THIRTEEN arms over SIX scratch repos, one per
#      criterion, and a criterion's later states edit that repo's files IN PLACE: the checker takes
#      its tracked list from `git ls-files` and then reads each tracked file's working-tree bytes,
#      so only a state that CREATES a file owes a `git add`. No arm here resets, which is also what
#      keeps the fixtures' LF bytes — a `reset --hard` under a global `core.autocrlf` re-checks them
#      out with CRLF and the `### Edges` sub-head then matches nothing, which is a silent zero.
#      EVERY `Red when:` these criteria name was staged into a copy of the checker and observed RED
#      before these arms were written: the join reading the source instead of the target, the first
#      line only, a bullet shape narrower than check 12's, absence redding as disagreement, a target
#      joined by filename, the key read through `read_conf_key`, and the bare-token waiver. That
#      last one is why AC5's third arm asserts a PRINTED KEY and a FORBIDDEN `STALE WAIVER` rather
#      than an exit code: the defect reaches rc 1 by the wrong route.
HCUT=2026-09-02      # the scratch repos' own SPEC_HANDOFF_CUTOFF, and the date their specs carry.
                     # The fixture FILENAMES are derived from it, so a re-derivation of the real
                     # key in `.memory-tree.conf` never has to move a literal in here.
SPECDIR=memory/builds/tOne/spec

write_handoff_spec() {   # $1 dir · $2 repo-relative path · $3 H1 uid · $4 Status word · rest: body
  local d=$1 p=$2 uid=$3 st=$4; shift 4
  mkdir -p "$d/${p%/*}"
  { printf '# %s — a unit\n\n' "$uid"
    printf '**Status:** %s · rev-1 · %s · node t · Tier-2 · base 0123abcd · streams tooling\n\n' "$st" "$HCUT"
    printf '%s\n' "$@"; } > "$d/$p"
}

# AC1 — a hands-off token the target never names, then named. The key carries BOTH uids, each read
#       from its own spec's H1, so a waiver can silence one edge without silencing the token.
d=$base/ho1; scratch "$d"
printf 'SPEC_HANDOFF_CUTOFF="%s"\n' "$HCUT" > "$d/.memory-tree.conf"
write_handoff_spec "$d" "$SPECDIR/$HCUT-spec-EXMP-tOne-1.md" EXMP-tOne-1 OPEN \
  '## 3. Non-goals (OUT)' '' '### Edges' '' \
  '- **hands-off** `EXMP-tOne-2` — it reads `--frob` from this unit.'
write_handoff_spec "$d" "$SPECDIR/$HCUT-spec-EXMP-tOne-2.md" EXMP-tOne-2 OPEN \
  '## 4. Design' '' 'It reads the flag this unit was handed.'
git -C "$d" add -A >/dev/null
arm "a hands-off token the target never names REDS, keyed on both H1 uids" 1 "$d" 'spec-EXMP-tOne-1.md [handoff] `EXMP-tOne-1>EXMP-tOne-2:--frob`'
sed -i 's|It reads the flag|It reads `--frob`, the flag|' "$d/$SPECDIR/$HCUT-spec-EXMP-tOne-2.md"
arm "the same token is green once the target names it, and the counts say what was graded" 0 "$d" "1 bullet(s) graded in live spec(s) · 1 payload token(s)"

# AC2 — the payload on the bullet's two-space CONTINUATION line, which check 12 never reads; then
#       check 12's other accepted shape, a `*` marker with a tab and an UNBACKTICKED target uid.
d=$base/ho2; scratch "$d"
printf 'SPEC_HANDOFF_CUTOFF="%s"\n' "$HCUT" > "$d/.memory-tree.conf"
write_handoff_spec "$d" "$SPECDIR/$HCUT-spec-EXMP-tOne-1.md" EXMP-tOne-1 OPEN \
  '## 3. Non-goals (OUT)' '' '### Edges' '' \
  '- **hands-off** `EXMP-tOne-2` — the flag it is handed is spelled on the' \
  '  next line, past the house width, and it is `--frob`.'
write_handoff_spec "$d" "$SPECDIR/$HCUT-spec-EXMP-tOne-2.md" EXMP-tOne-2 OPEN \
  '## 4. Design' '' 'It reads the flag this unit was handed.'
git -C "$d" add -A >/dev/null
arm "a payload wrapped onto the bullet's continuation line is graded, not skipped" 1 "$d" '[handoff] `EXMP-tOne-1>EXMP-tOne-2:--frob`'
printf '# EXMP-tOne-1 — a unit\n\n**Status:** OPEN · rev-1 · %s · node t · Tier-2 · base 0123abcd · streams tooling\n\n## 3. Non-goals (OUT)\n\n### Edges\n\n*\t**hands-off**\tEXMP-tOne-2 — it reads `--frob` from this unit.\n' "$HCUT" > "$d/$SPECDIR/$HCUT-spec-EXMP-tOne-1.md"
arm "a star marker, a tab and a bare target uid is check 12's shape and is graded here too" 1 "$d" '[handoff] `EXMP-tOne-1>EXMP-tOne-2:--frob`'

# AC3 — SILENCE, COUNTED. Absence is not disagreement: a CLOSED sibling is a frozen record nobody
#       may edit, and a source whose H1 carries no uid has no key to report a hit under.
d=$base/ho3; scratch "$d"
printf 'SPEC_HANDOFF_CUTOFF="%s"\n' "$HCUT" > "$d/.memory-tree.conf"
write_handoff_spec "$d" "$SPECDIR/$HCUT-spec-EXMP-tOne-1.md" EXMP-tOne-1 OPEN \
  '## 3. Non-goals (OUT)' '' '### Edges' '' \
  '- **hands-off** `EXMP-tOne-2` — it reads `--frob` from this unit.'
write_handoff_spec "$d" "$SPECDIR/$HCUT-spec-EXMP-tOne-2.md" EXMP-tOne-2 CLOSED \
  '## 4. Design' '' 'It reads the flag this unit was handed.'
git -C "$d" add -A >/dev/null
arm "a hands-off to a CLOSED sibling is silent and COUNTED, never red" 0 "$d" "0 payload token(s) · 1 silent"
sed -i 's|\*\*Status:\*\* CLOSED|**Status:** OPEN|' "$d/$SPECDIR/$HCUT-spec-EXMP-tOne-2.md"
sed -i 's|`EXMP-tOne-2`|`EXMP-tOne-9`|' "$d/$SPECDIR/$HCUT-spec-EXMP-tOne-1.md"
printf '# a source whose H1 carries no uid\n\n**Status:** OPEN · rev-1 · %s · node t · Tier-2 · base 0123abcd · streams tooling\n\n## 3. Non-goals (OUT)\n\n### Edges\n\n- **hands-off** `EXMP-tOne-2` — it reads `--frob` from this unit.\n' "$HCUT" > "$d/$SPECDIR/$HCUT-spec-EXMP-tOne-3.md"
git -C "$d" add -A >/dev/null
arm "an unspecced target uid and a source with no H1 uid each count silent" 0 "$d" "0 payload token(s) · 2 silent"

# AC4 — the dated demand and its refusal, over one tree that reds when the key is set correctly.
d=$base/ho4; scratch "$d"
printf 'SPEC_HANDOFF_CUTOFF=""\n' > "$d/.memory-tree.conf"
write_handoff_spec "$d" "$SPECDIR/$HCUT-spec-EXMP-tOne-1.md" EXMP-tOne-1 OPEN \
  '## 3. Non-goals (OUT)' '' '### Edges' '' \
  '- **hands-off** `EXMP-tOne-2` — it reads `--frob` from this unit.'
write_handoff_spec "$d" "$SPECDIR/$HCUT-spec-EXMP-tOne-2.md" EXMP-tOne-2 OPEN \
  '## 4. Design' '' 'It reads the flag this unit was handed.'
git -C "$d" add -A >/dev/null
arm "a blank SPEC_HANDOFF_CUTOFF turns the join off over a tree that reds when it is set" 0 "$d" "SPEC_HANDOFF_CUTOFF blank (arm off)"
printf 'SPEC_HANDOFF_CUTOFF="2026-09-30"\n' > "$d/.memory-tree.conf"
arm "a source dated before the key is not graded, and the bullet count says zero" 0 "$d" "0 bullet(s) graded in live spec(s)"
printf 'SPEC_HANDOFF_CUTOFF="2026-9-14"\n' > "$d/.memory-tree.conf"
arm "a key that is not an ISO date is REFUSED before grading, like every other cutoff" 1 "$d" "REFUSING — SPEC_HANDOFF_CUTOFF 2026-9-14 is not an ISO date"

# AC5 — the waiver is keyed on the EDGE, not the token. Three states over one repo: waived, stale,
#       and a SECOND edge carrying the same token, which that row must not reach.
d=$base/ho5; scratch "$d"
printf 'SPEC_HANDOFF_CUTOFF="%s"\n' "$HCUT" > "$d/.memory-tree.conf"
write_handoff_spec "$d" "$SPECDIR/$HCUT-spec-EXMP-tOne-1.md" EXMP-tOne-1 OPEN \
  '## 3. Non-goals (OUT)' '' '### Edges' '' \
  '- **hands-off** `EXMP-tOne-2` — it reads `--frob` from this unit.'
write_handoff_spec "$d" "$SPECDIR/$HCUT-spec-EXMP-tOne-2.md" EXMP-tOne-2 OPEN \
  '## 4. Design' '' 'It reads the flag this unit was handed.'
printf 'EXMP-tOne-1>EXMP-tOne-2:--frob\t[handoff] deliberate, for this arm\n' >> "$d/memory/project/spec-token-waivers.txt"
git -C "$d" add -A >/dev/null
arm "a waiver row keyed on the edge clears that hit and is counted" 0 "$d" "1 waiver(s)"
sed -i 's|It reads the flag|It reads `--frob`, the flag|' "$d/$SPECDIR/$HCUT-spec-EXMP-tOne-2.md"
arm "the same row REDS as stale once the target names the token" 1 "$d" "STALE WAIVER"
sed -i 's|It reads `--frob`, the flag|It reads the flag|' "$d/$SPECDIR/$HCUT-spec-EXMP-tOne-2.md"
write_handoff_spec "$d" "$SPECDIR/$HCUT-spec-EXMP-tOne-3.md" EXMP-tOne-3 OPEN \
  '## 3. Non-goals (OUT)' '' '### Edges' '' \
  '- **hands-off** `EXMP-tOne-2` — it reads `--frob` from this unit too.'
git -C "$d" add -A >/dev/null
arm "that row does not reach ANOTHER edge carrying the same token" 1 "$d" '[handoff] `EXMP-tOne-3>EXMP-tOne-2:--frob`' "STALE WAIVER"

# AC9 — the join is by H1 uid at any depth. A family-less, tailed spec inside a `units` sub-folder
#       of `spec/` is legal, and its filename says nothing about the unit it specs.
d=$base/ho6; scratch "$d"
printf 'SPEC_HANDOFF_CUTOFF="%s"\n' "$HCUT" > "$d/.memory-tree.conf"
write_handoff_spec "$d" "$SPECDIR/$HCUT-spec-tOne-1.md" EXMP-tOne-1 OPEN \
  '## 3. Non-goals (OUT)' '' '### Edges' '' \
  '- **hands-off** `EXMP-tOne-2` — it reads `--frob` from this unit.'
write_handoff_spec "$d" "$SPECDIR/units/$HCUT-spec-tOne-2-u1-part.md" EXMP-tOne-2 OPEN \
  '## 4. Design' '' 'It reads the flag this unit was handed.'
git -C "$d" add -A >/dev/null
arm "a family-less, tailed target in a units sub-folder is joined by its H1, not its filename" 1 "$d" '[handoff] `EXMP-tOne-1>EXMP-tOne-2:--frob`'

total=$((pass+fail))
if [ "$total" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "check-spec-tokens: $total assertion(s) executed, below the declared floor of $FLOOR_ASSERTIONS —"
  echo "  arms went missing rather than failing, which reports as success without this check."
  exit 1
fi
[ "$fail" = 0 ] && echo "PASS ($total assertions)"
[ "$fail" = 0 ] || { echo "check-spec-tokens: $fail of $total assertion(s) failed"; exit 1; }
