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
FLOOR_ASSERTIONS=32
LINT="$(cd "$(dirname "$0")" && pwd)/check-spec-tokens.py"
PY=${PY:-python}
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

arm() {              # $1 label · $2 expected rc · $3 dir · $4 optional expected substring
  local out rc
  out=$(cd "$3" && "$PY" "$LINT" 2>&1); rc=$?
  if [ "$rc" != "$2" ]; then
    echo "arm FAIL  $1 — expected rc $2, got $rc"; echo "$out" | head -3; fail=$((fail+1)); return
  fi
  if [ $# -ge 4 ] && ! printf '%s' "$out" | grep -qF -- "$4"; then
    echo "arm FAIL  $1 — expected output to carry: $4"; echo "$out" | head -3; fail=$((fail+1)); return
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
mkdir -p "$d/tools/run-gates"; : > "$d/tools/run-gates/run-gates.sh"
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

# AC17 — a COMMITTED cutoff not strictly past its own commit day is REFUSED before grading, naming
#        the key, the value and the day it compared against. Today's checker grades this tree clean.
printf 'SPEC_DIRECT_CUTOFF="2026-09-02"\n' > "$d/.memory-tree.conf"
git -C "$d" add -A >/dev/null; git -C "$d" commit -qm cutoff --no-verify
day=$(git -C "$d" log -1 --format=%cs)
arm "a committed cutoff not strictly past its own commit day is REFUSED before grading" 1 "$d" "REFUSING — SPEC_DIRECT_CUTOFF 2026-09-02 is not strictly past $day"
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

total=$((pass+fail))
if [ "$total" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "check-spec-tokens: $total assertion(s) executed, below the declared floor of $FLOOR_ASSERTIONS —"
  echo "  arms went missing rather than failing, which reports as success without this check."
  exit 1
fi
[ "$fail" = 0 ] && echo "PASS ($total assertions)"
[ "$fail" = 0 ] || { echo "check-spec-tokens: $fail of $total assertion(s) failed"; exit 1; }
