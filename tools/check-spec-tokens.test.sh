#!/usr/bin/env bash
# check-spec-tokens.test.sh — red/green arms for <prefix>/check-spec-tokens.py (TOOL-dRetiredFork-20).
# TOOL-aBlindedTrial-8 added the guards-join arms: a §4 files-touched path that trips a leg's guard
# owes that leg's name on the §7 leg line.
#
# HERMETIC: every arm runs in a scratch repo under mktemp -d — its own, or one of the two the bar
# arms share and reset between edits — and never touches the real tree, so the suite is safe beside
# the other heavy legs in a concurrent bar.
#
# Each arm asserts an EXIT CODE and, where the message is the point, a substring of stdout. The
# refusal arms matter most: this lint's own failure mode is passing over a population it never
# built, which is the class it exists to catch one level up.
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
KIT_REL=$(derive_self_rel "$HERE") || { echo "check-spec-tokens.test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
PFX="${KIT_REL:+$KIT_REL/}"

# The shrink-only assertion floor. A suite that stops running arms must RED rather than report a
# smaller success: `check-testsuite-counts.sh` reads this pin, the printed count, and the comparison
# between them, because a pin nothing reads is the same nothing as no pin.
FLOOR_ASSERTIONS=126
# RAISED 119 -> 126 at TOOL-aMendedFleet-75, by its seven covers-join `arm` calls: the dangling id,
# the count line, the defined id, `none` alone, `none` beside an id, the prose-only id and the field
# on a continuation line.
# RAISED 112 -> 119 at TOOL-aMendedFleet-25, by its seven size-join `arm` calls: the held spec and
# its count, the padded spec, the grown held spec, the terminal spec's stale row, the arm-off line
# and the non-number refusal.
# RAISED 109 -> 112 at TOOL-aRepatriatedFork-54, by its three root-install `arm` calls: the untracked
# bare name, the basename citation and the dotted non-file word.
# RAISED 32 -> 38 at the closing review's F2, F4, F9 and F10, by the static count of the arms they
# added: the quoted-empty flag, the selftest.py hit, the two parity assertions over the manifest,
# the requoted-cutoff arm and the non-ISO cutoff refusal.
# RAISED 38 -> 42 at closing round 2, by the count of `arm`/`pass=` lines its diff added: two
# leg-line cutoff refusals (R7, R11), the `py` launcher hit (R12) and the parity accounting (R3).
# RAISED 42 -> 55 at TOOL-aBlindedTrial-8, by the count of `arm`/`pass=` lines its diff added: the
# guards join's hit and clean pair, the pre-cutoff carrier, the blank key, the non-path token, the
# short sub-head spelling, the absent sub-head, the one-segment near-miss (rc and `--list`), the
# composite waiver and the bare-leg row that does not consume it, and the two refusals (non-ISO,
# relation).
# RAISED 55 -> 62 at the closing diff review of TOOL-aBlindedTrial-7/8 (round 1), by the count of
# `arm` lines its diff added: the breadth pair (R1), the declared-prefix pair (R3), the no-Gates
# precondition (R4) and the exact-file guard pair (R12).
# RAISED 62 -> 66 at round 2 of that review, by the count of `arm`/`pass=` lines its diff added: the
# one-segment root pair (R1: rc and the --list row), the duplicated-entry breadth arm (R7) and the
# no-Gates --list row (R8).
# RAISED 66 -> 67 at round 3 of that review: the dot-token count arm on the one-leg bare-`<prefix>/`
# fixture (R5), where the `<prefix>/./` refusal is load-bearing.
# RAISED 67 -> 80 at the merge of origin/main into TOOL-dDerivedDocket-37, by that unit's 13 `arm`
# calls, which it recorded as 42 -> 55 on a base without the rounds above: base + both deltas. The
# hands-off join's six fixtures add two each for the graded edge, the bullet shape and the counted
# silence, three each for the dated key and the edge-keyed waiver, and one for the H1 join at any
# depth.
# RAISED 67 -> 91 at TOOL-dGatedProse-2, by the count of `arm`/`pass=` lines its diff added: 3 `arm`
# calls and 21 inline increments. The claims join's direct half is fourteen — the two motivating
# blob sentences, the three closed specs' clears, the unwritten key, the fenced copy, the six
# per-arm, uppercase and shouted fixtures, and the live-key disjointness; its process half is ten —
# the six staged breaks, the report line twice, the --list rows and the hit as the report prints it.
# RAISED 91 -> 95 at the closing diff review of dGatedProse (round 1), by the count of `arm`/`pass=`
# lines its fold added: 2 `arm` calls for R1's composite claims token and 2 inline increments for
# R3's tilde fences, each observed RED against the checker before the fold.
# RAISED 95 -> 96 at round 2 of that review (F3): one inline increment for the arm that uses the
# composite waiver token alone and expects green, observed RED against a copy that never waives a claim.
# MERGED 109 at the dDerivedDocket x origin/main reconcile: base 67 + ours' 13 (67 -> 80, the hands-off
# join above) + theirs' 29 (67 -> 96, the claims join and its review rounds).
LINT="$(cd "$(dirname "$0")" && pwd)/check-spec-tokens.py"
# The launcher is RESOLVED by running it; `PY=` overrides. A bare default here was the
# parameter-default shape the resolver ban now catches. TOOL-aRepatriatedFork-46: the resolver is
# carried INLINE; it was sourced from the library directory beside this suite, which ships nowhere.
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
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
[ -n "${PY:-}" ] || PY=$(resolve_python) || exit 2
# TOOL-aRepatriatedFork-46: a kit is named by the name its directory has in THIS install, never
# as a literal segment: a sibling's through the resolver, which reads the install receipt first.
# A fixture mirrors that layout by the resolved NAME.
# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. A shell consumer runs it with the python it already resolved, so the receipt rung is
# read in Python and never parsed in bash. `resolve_kit_dir <python> <home> <anchor> <here>`
# prints the kit directory REPO-RELATIVE, or the resolver's named refusal on stderr and exits 1.
resolve_kit_dir() {
  "$1" -c "$(cat <<'RKD'
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — the `.governance/install.json` row whose `source` ends in <home>/<anchor> and
       whose `path` exists inside this tree. The only record of a RENAMED kit dir: no probe finds
       a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        if str(row.get("source") or "").split("/")[-2:] != [home, anchor]:
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
)"'
import sys
try:
    d = resolve_kit_dir(*sys.argv[1:4])
except LookupError as e:
    sys.exit(str(e))
r = next((p for p in (d, *d.parents) if (p / ".git").exists()), d.anchor)
print(d.relative_to(r).as_posix())' "$2" "$3" "$4"
}
RUN_GATES_DIR=$(resolve_kit_dir "$PY" run-gates run-gates.sh "$HERE") || exit 2
RUN_GATES="${RUN_GATES_DIR##*/}"
GOVKIT_DIR=$(resolve_kit_dir "$PY" govkit govkit.py "$HERE") || exit 2
GOVKIT="${GOVKIT_DIR##*/}"
RUNLOG_DIR=$(resolve_kit_dir "$PY" runlog runlog.py "$HERE") || exit 2
RUNLOG="${RUNLOG_DIR##*/}"
CODEBASE_MAP_DIR=$(resolve_kit_dir "$PY" codebase-map map_lib.py "$HERE") || exit 2
pass=0; fail=0

scratch() {          # $1 = dir. A repo with one live spec, a manifest and an empty waiver file.
  local d=$1
  git init -q "$d"; git -C "$d" config user.email t@t.test; git -C "$d" config user.name t
  mkdir -p "$d/memory/builds/tOne/spec" "$d/memory/project" "$d/${PFX}"
  printf '[{"name":"real leg"}]\n' > "$d/${PFX}gate-legs.json"
  # A tool root holds a gate script. At a root install the paths join grades a bare name only when
  # a tracked file carries its extension (TOOL-aRepatriatedFork-54), so without one `nope.sh` is prose.
  printf '#!/bin/sh\n' > "$d/${PFX}gate.sh"
  printf '# waivers\n' > "$d/memory/project/spec-token-waivers.txt"
  cat > "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md" <<'SPEC'
# TOOL-tOne-1 — a unit

**Status:** OPEN · rev-1 · 2026-09-02 · node t · Tier-1 · base 0123abcd · streams tooling

## 6. Acceptance criteria

- **AC1** — `{PFX}gate-legs.json` exists.

## 7. Gates

`real leg`.
SPEC
  sed -i "s#{PFX}#${PFX}#g" "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"   # the quoted heredoc cannot expand the prefix
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
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fail:-0}" = 0 ] && echo "PASS (${pass:-1} assertions)" || echo "FAIL (${pass:-1} assertions)"; [ "${fail:-0}" = 0 ] && exit 0; exit 1; fi

# 2 — a section 6 criterion naming an untracked path
d=$base/path; scratch "$d"
sed -i 's|`'"${PFX}gate-legs.json"'` exists|`'"${PFX}nope.sh"'` exists|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "an untracked witness path in section 6 REDS" 1 "$d" "not tracked by git ls-files"

# 3 — a section 7 name that is not a leg
d=$base/leg; scratch "$d"
sed -i 's|^`real leg`\.|`imaginary leg`.|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a section 7 name absent from the manifest REDS" 1 "$d" "not a name in ${PFX}gate-legs.json"

# 4 — a citation past end of file
d=$base/cite; scratch "$d"
sed -i 's|`'"${PFX}gate-legs.json"'` exists|see `'"${PFX}gate-legs.json"':9999`|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a citation beyond end of file REDS" 1 "$d" "lines"

# ---- TOOL-aRepatriatedFork-54: a REPO-ROOT install grades bare file names, whatever prefix this
# suite sits at. Each fixture is built at the root (PFX emptied in a subshell), so its manifest's
# tool root is the repository root. Observed RED-first on the 56c7befa checker: the first two arms.
rootspec=memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md
d=$base/rootbare; ( PFX=; scratch "$d" )
sed -i 's|`gate-legs.json` exists|`nope.sh` exists|' "$d/$rootspec"
git -C "$d" add -A >/dev/null
arm "at a root install an untracked bare file name in section 6 REDS" 1 "$d" "not tracked by git ls-files"
d=$base/rootbase; ( PFX=; scratch "$d" )
mkdir -p "$d/x"; : > "$d/x/kit.toml"
sed -i 's|`gate-legs.json` exists|`gate-legs.json` exists and `kit.toml` is cited|' "$d/$rootspec"
git -C "$d" add -A >/dev/null
arm "at a root install a basename citation of a tracked file is graded and resolves" 0 "$d" "3 token(s) graded"
d=$base/rootword; ( PFX=; scratch "$d" )
sed -i 's|`gate-legs.json` exists|`gate-legs.json` exists and `json.loads` reads it|' "$d/$rootspec"
git -C "$d" add -A >/dev/null
arm "at a root install a dotted word no tracked extension matches is not graded" 0 "$d" "2 token(s) graded"

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
printf '[{"name":"real leg"},{"name":"'"${PFX}thing"' self-test"}]
' > "$d/${PFX}gate-legs.json"
sed -i 's|^`real leg`\.|`'"${PFX}thing"' self-test`.|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a manifest leg name carrying a slash RESOLVES rather than being skipped" 0 "$d" "0 live spec(s) carry a Gates heading contributing NO leg name"

# AC10 — the other excluded shape: a manifest name whose first word is a command verb.
d=$base/verbleg; scratch "$d"
printf '[{"name":"real leg"},{"name":"bash the thing"}]
' > "$d/${PFX}gate-legs.json"
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

# TOOL-aRepatriatedFork-38 — the SAME cutoff with a trailing comment, quoted and then unquoted. The
# old reader demanded nothing after the closing quote, so the quoted one read as BLANK (arm off).
d=$base/leglinenote; scratch "$d"
printf 'SPEC_LEGLINE_CUTOFF="2026-09-01"   # a trailing note\n' > "$d/.memory-tree.conf"
sed -i 's|^`real leg`\.|The bar and whatever it drags in.|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a quoted cutoff with a trailing comment still arms the join" 1 "$d" "contributes no leg name"
printf 'SPEC_LEGLINE_CUTOFF=2026-09-01   # a trailing note\n' > "$d/.memory-tree.conf"
git -C "$d" add -A >/dev/null
arm "an unquoted cutoff with a trailing comment still arms the join" 1 "$d" "contributes no leg name"
# rev-3 (the closing review's C4): a `#` OPENING the value is part of the word, as bash reads it, so
# this cutoff is the non-date `#2026-09-01` and is REFUSED by name. The old reader read it as BLANK,
# which switched the join off without a word.
printf 'SPEC_LEGLINE_CUTOFF=#2026-09-01\n' > "$d/.memory-tree.conf"
git -C "$d" add -A >/dev/null
arm "a cutoff whose word opens with # is refused as a non-date, never read as off" 1 "$d" "is not an ISO date"

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
sed -i 's|`'"${PFX}gate-legs.json"'` exists|see `run-gates.sh:407`|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "an untracked citation path is skipped, not red" 0 "$d" "citation(s) skipped"

# 6 — a waiver with a reason silences the hit and the count is printed
d=$base/waived; scratch "$d"
sed -i 's|`'"${PFX}gate-legs.json"'` exists|`'"${PFX}nope.sh"'` exists|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
printf ''"${PFX}nope.sh"'\tdeliberate, for this arm\n' >> "$d/memory/project/spec-token-waivers.txt"
git -C "$d" add -A >/dev/null
arm "a waived hit with a reason passes" 0 "$d" "waiver(s)"

# 7 — a waiver nothing produces any more REDS: a stale exception cannot hide a live hit
d=$base/stale; scratch "$d"
printf ''"${PFX}gone.sh"'\tno spec names this\n' >> "$d/memory/project/spec-token-waivers.txt"
git -C "$d" add -A >/dev/null
arm "a stale waiver REDS" 1 "$d" "STALE WAIVER"

# 8 — a waiver row with no reason REDS
d=$base/noreason; scratch "$d"
printf ''"${PFX}nope.sh"'\n' >> "$d/memory/project/spec-token-waivers.txt"
git -C "$d" add -A >/dev/null
arm "a waiver carrying no reason REDS" 1 "$d" "STALE WAIVER"

# 9 — REFUSALS. An empty population is not a pass.
d=$base/nospec; scratch "$d"
git -C "$d" rm -q "memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
arm "no spec at all REFUSES" 1 "$d" "REFUSING"

# 10 — a TERMINAL spec is a frozen record and is not graded, so it cannot red
d=$base/frozen; scratch "$d"
sed -i 's|\*\*Status:\*\* OPEN|**Status:** CLOSED|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
sed -i 's|`'"${PFX}gate-legs.json"'` exists|`'"${PFX}nope.sh"'` exists|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a CLOSED spec is frozen, so it refuses rather than grading" 1 "$d" "REFUSING"

# 11 — the waiver registry itself must exist
d=$base/noreg; scratch "$d"
git -C "$d" rm -q memory/project/spec-token-waivers.txt
arm "an absent waiver registry REFUSES" 1 "$d" "REFUSING"

# 12 — a malformed manifest REFUSES rather than grading zero legs
d=$base/badlegs; scratch "$d"
printf 'not json\n' > "$d/${PFX}gate-legs.json"; git -C "$d" add -A >/dev/null
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
mkdir -p "$d/${PFX}${RUN_GATES}" "$d/${PFX}${GOVKIT}"; : > "$d/${PFX}${RUN_GATES}/run-gates.sh"; : > "$d/${PFX}${GOVKIT}/selftest.py"
git -C "$d" add -A >/dev/null; git -C "$d" commit -qm runner --no-verify
clean=$(git -C "$d" rev-parse HEAD)
spec="$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"

# AC1 — a post-cutoff §6 bullet backticking the flagged full bar REDS as [bar], with the substitute.
#       The token opens `GATE_`, which NOT_A_TOKEN drops unread unless the bar test runs first.
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
sed -i 's|`'"${PFX}gate-legs.json"'` exists|`GATE_SELFTESTS=1 bash '"${PFX}${RUN_GATES}/run-gates.sh"'` is green|' "$spec"
git -C "$d" add -A >/dev/null
arm "a post-cutoff §6 bullet naming the flagged bar REDS as [bar]" 1 "$d" '-spec-TOOL-tOne-1.md [bar] `GATE_SELFTESTS=1 bash '"${PFX}${RUN_GATES}/run-gates.sh"'` — a bar or suite is not an acceptance observation'
git -C "$d" reset -q --hard "$clean"

# AC2 — the same token on the §7 leg line REDS: NOT_A_LEG would discard it for its `bash ` opener.
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
sed -i 's|^`real leg`\.|`real leg` · `GATE_SELFTESTS=1 bash '"${PFX}${RUN_GATES}/run-gates.sh"'`.|' "$spec"
git -C "$d" add -A >/dev/null
arm "the same token on the §7 leg line REDS, read before NOT_A_LEG discards it" 1 "$d" '[bar] `GATE_SELFTESTS=1 bash '"${PFX}${RUN_GATES}/run-gates.sh"'`'
git -C "$d" reset -q --hard "$clean"

# AC3 — three placements that are NOT hits: §4 prose, a §7 `New arm:` line, and the un-backticked
#       body of a fence under a §6 bullet. `--list` prints the first two as NEAR and nothing at all
#       for the fence body, which is the fence exclusion asserted as silence.
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
cat > "$spec" <<'SPEC'
# TOOL-tOne-1 — a unit

**Status:** OPEN · rev-1 · 2026-09-02 · node t · Tier-1 · base 0123abcd · streams tooling

## 4. Design

The bar is `GATE_SELFTESTS=1 bash {PFX}{RUN_GATES}/run-gates.sh`, named here in prose.

## 6. Acceptance criteria

- **AC1** — `{PFX}gate-legs.json` exists.
  ```
  bash {PFX}{RUN_GATES}/run-selftests.sh
  ```

## 7. Gates

`real leg`.

New arm: `bash {PFX}check-spec-tokens.test.sh` · stages a break · none
SPEC
sed -i "s#{PFX}#${PFX}#g; s#{RUN_GATES}#${RUN_GATES}#g" "$spec"   # the quoted heredoc cannot expand either
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
sed -i 's|`'"${PFX}gate-legs.json"'` exists|`GATE_SELFTESTS=1 bash '"${PFX}${RUN_GATES}/run-gates.sh"'` is green|' "$d/memory/builds/tOne/spec/2026-08-30-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a PRE-cutoff carrier is green, counted and not graded" 0 "$d" "1 pre-cutoff live spec(s) carry one and are not graded"
git -C "$d" reset -q --hard "$clean"

# AC5 — a BLANK key turns the join off over the AC1 tree, and the OFF line still counts the carrier.
printf 'SPEC_DIRECT_CUTOFF=""\n' > "$d/.memory-tree.conf"
sed -i 's|`'"${PFX}gate-legs.json"'` exists|`GATE_SELFTESTS=1 bash '"${PFX}${RUN_GATES}/run-gates.sh"'` is green|' "$spec"
git -C "$d" add -A >/dev/null
arm "a blank SPEC_DIRECT_CUTOFF turns the join off and still counts the carrier" 0 "$d" "SPEC_DIRECT_CUTOFF blank (arm off) · 1 live spec(s) carry a bar token"
git -C "$d" reset -q --hard "$clean"

# AC15 — the LIGHT profile: criteria under `## 5.`, Gates under `## 6.`. The ordinal read graded the
#        Gates section as the bullet population and never saw the token; the heading read does.
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
sed -i 's|`'"${PFX}gate-legs.json"'` exists|`GATE_SELFTESTS=1 bash '"${PFX}${RUN_GATES}/run-gates.sh"'` is green|; s|^## 6. Acceptance criteria$|## 5. Acceptance criteria|; s|^## 7. Gates$|## 6. Gates|' "$spec"
git -C "$d" add -A >/dev/null
arm "a light-profile spec is graded where its criteria sit, not at the ordinal" 1 "$d" '[bar] `GATE_SELFTESTS=1 bash '"${PFX}${RUN_GATES}/run-gates.sh"'`'
git -C "$d" reset -q --hard "$clean"

# AC16 — the EMPTY flag assignment is the OFF spelling and no hit (rev-1's branch matched it); the
#        same assignment with a value is a hit whatever command follows it.
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
sed -i 's|`'"${PFX}gate-legs.json"'` exists|`GATE_FULL= cat '"${PFX}gate-legs.json"'` prints|' "$spec"
git -C "$d" add -A >/dev/null
arm "the EMPTY flag assignment is the OFF spelling and is no hit" 0 "$d" "2 token(s) examined in 1 live spec(s) at/after SPEC_DIRECT_CUTOFF 2026-09-01"
sed -i 's|`GATE_FULL= cat|`GATE_FULL=1 cat|' "$spec"
git -C "$d" add -A >/dev/null
arm "the same flag assignment with a value REDS" 1 "$d" '[bar] `GATE_FULL=1 cat '"${PFX}gate-legs.json"'`'
git -C "$d" reset -q --hard "$clean"

# closing review F9 — the QUOTED empty assignment is the OFF spelling too. rev-3's `\S` read the
# quote as a value and disagreed with the hook, which unquotes it; observed RED-first on that regex.
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
sed -i 's|`'"${PFX}gate-legs.json"'` exists|`GATE_FULL="" cat '"${PFX}gate-legs.json"'` prints|' "$spec"
git -C "$d" add -A >/dev/null
arm "the QUOTED empty flag assignment is the OFF spelling and is no hit" 0 "$d" "2 token(s) examined in 1 live spec(s) at/after SPEC_DIRECT_CUTOFF 2026-09-01"
git -C "$d" reset -q --hard "$clean"

# closing review F2 — a whole-suite `selftest.py` FILE is a suite invocation, the same rule as a
# `.test.sh`; the fixture tracks the file so the paths join stays green and the one hit is the bar's.
# A `--selftest` FLAG on another file is the direct check the child prompt admits and is not a hit.
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
sed -i 's|`'"${PFX}gate-legs.json"'` exists|`python '"${PFX}${GOVKIT}/selftest.py"'` is green|' "$spec"   # gov:literal-python — a fixture TOKEN the checker grades, never run
git -C "$d" add -A >/dev/null
arm "a post-cutoff §6 bullet naming a whole-suite selftest.py REDS as [bar]" 1 "$d" '[bar] `python '"${PFX}${GOVKIT}/selftest.py"'`'   # gov:literal-python — the expected hit line, never run
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
sed -i 's|`'"${PFX}gate-legs.json"'` exists|`py '"${PFX}${GOVKIT}/selftest.py"'` is green|' "$spec"   # gov:literal-python — a fixture TOKEN the checker grades, never run
git -C "$d" add -A >/dev/null
arm "a whole-suite selftest.py behind the py launcher REDS as [bar]" 1 "$d" '[bar] `py '"${PFX}${GOVKIT}/selftest.py"'`'   # gov:literal-python — the expected hit line, never run
git -C "$d" reset -q --hard "$clean"

# ---- TOOL-aBlindedTrial-8: the guards join, over the same shared repo and reset the same way. A
#      §4 `### Files touched` path that trips a leg's `guard` in the manifest owes that leg's name on
#      the §7 leg line. Each arm is observed RED-first on the checker at 987c5bec, which read no
#      sub-head and no guard: the hit arms graded clean, the report arms printed no guards line, and
#      the refusal arms never read the key. The fixture spec carries no `## 4.`, so each arm inserts
#      one above the acceptance heading; the manifest gains one leg guarded on `<prefix>/x/`.
GUARD_LEGS='[{"name":"real leg"},{"name":"guarded leg","guard":["'"${PFX}x/"'"]}]'
write_files_touched() {   # $1 = the sub-head line · $2 = the line under it (backticked tokens)
  sed -i "s|^## 6. Acceptance criteria\$|## 4. Design\n\n$1\n\n$2\n\n## 6. Acceptance criteria|" "$spec"
}

# AC2 — a post-cutoff spec declaring `<prefix>/x/thing.sh` whose leg line omits `guarded leg` REDS as
#       [guards], naming the spec, the leg and the path in one composite token.
printf '%s\n' "$GUARD_LEGS" > "$d/${PFX}gate-legs.json"
printf 'SPEC_GUARD_LEGS_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
write_files_touched '### Files touched (estimate)' '`'"${PFX}x/thing.sh"'`'
git -C "$d" add -A >/dev/null
arm "a post-cutoff spec whose files-touched trips a guard the leg line omits REDS as [guards]" 1 "$d" '-spec-TOOL-tOne-1.md [guards] `guarded leg <- '"${PFX}x/thing.sh"'` — §4 files-touched names '"${PFX}x/thing.sh"', which trips the guard of leg '"'"'guarded leg'"'"', absent from the §7 leg line'
# ...and the same tree with the leg NAMED is green, and the guards line reports what it examined.
sed -i 's|^`real leg`\.|`real leg` · `guarded leg`.|' "$spec"
git -C "$d" add -A >/dev/null
arm "the same tree with the guarded leg named on the leg line is green and counted as examined" 0 "$d" "guards join · 1 declared path(s) examined in 1 live spec(s) at/after SPEC_GUARD_LEGS_CUTOFF 2026-09-01"
git -C "$d" reset -q --hard "$clean"

# AC6 — the PRE-cutoff twin is green, and COUNTED on the guards line rather than silently skipped.
printf '%s\n' "$GUARD_LEGS" > "$d/${PFX}gate-legs.json"
printf 'SPEC_GUARD_LEGS_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
write_files_touched '### Files touched (estimate)' '`'"${PFX}x/thing.sh"'`'
git -C "$d" mv "$spec" "$d/memory/builds/tOne/spec/2026-08-30-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
arm "a PRE-cutoff spec missing a guarded leg is green, counted and not graded" 0 "$d" "1 pre-cutoff live spec(s) carry a missing guarded leg and are not graded"
git -C "$d" reset -q --hard "$clean"

# AC1 — a BLANK key turns the join off over the AC2 tree, announces it, and still counts the carrier.
printf '%s\n' "$GUARD_LEGS" > "$d/${PFX}gate-legs.json"
printf 'SPEC_GUARD_LEGS_CUTOFF=""\n' > "$d/.memory-tree.conf"
write_files_touched '### Files touched (estimate)' '`'"${PFX}x/thing.sh"'`'
git -C "$d" add -A >/dev/null
arm "a blank SPEC_GUARD_LEGS_CUTOFF turns the join off and still counts the carrier" 0 "$d" "guards join · SPEC_GUARD_LEGS_CUTOFF blank (arm off) · 1 live spec(s) carry a missing guarded leg"
git -C "$d" reset -q --hard "$clean"

# S2 — a token under the sub-head that is not path-shaped (`$KIT`, a deploy-time token) declares
#      nothing: zero paths examined, no hit, no carrier.
printf '%s\n' "$GUARD_LEGS" > "$d/${PFX}gate-legs.json"
printf 'SPEC_GUARD_LEGS_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
write_files_touched '### Files touched (estimate)' '`$KIT` · `last-audit`'
git -C "$d" add -A >/dev/null
arm "a non-path token under the sub-head declares no path" 0 "$d" "guards join · 0 declared path(s) examined in 1 live spec(s)"
git -C "$d" reset -q --hard "$clean"

# AC3 — the sub-head spelled WITHOUT the parenthetical is read the same way.
printf '%s\n' "$GUARD_LEGS" > "$d/${PFX}gate-legs.json"
printf 'SPEC_GUARD_LEGS_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
write_files_touched '### Files touched' '`'"${PFX}x/thing.sh"'`'
git -C "$d" add -A >/dev/null
arm "the short sub-head spelling is read and REDS the same omission" 1 "$d" '[guards] `guarded leg <- '"${PFX}x/thing.sh"'`'
git -C "$d" reset -q --hard "$clean"

# S2 — no sub-head at all is SILENT, and counted in its own field: nothing declared, nothing joined.
printf '%s\n' "$GUARD_LEGS" > "$d/${PFX}gate-legs.json"
printf 'SPEC_GUARD_LEGS_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
git -C "$d" add -A >/dev/null
arm "a post-cutoff spec with no Files touched sub-head is silent and counted apart" 0 "$d" "1 carry no Files touched sub-head"
git -C "$d" reset -q --hard "$clean"

# AC4 — a path under a BROAD guard only is excluded from the join: green, the report line prints the
#       excluded guard with its leg count, and `--list` prints the path as NEAR so the exclusion
#       announces itself. Broad is BREADTH (closing review round 1, R1): a guard carried by more than
#       BROAD_LEG_FLOOR legs, whatever its depth. The fixture is floor+1 legs sharing bare `<prefix>/`;
#       one leg on `<prefix>/` was the rev-1 fixture, and it is a HIT below now.
BROAD_LEGS='[{"name":"real leg"},{"name":"b1","guard":["'"${PFX}"'"]},{"name":"b2","guard":["'"${PFX}"'"]},{"name":"b3","guard":["'"${PFX}"'"]},{"name":"b4","guard":["'"${PFX}"'"]},{"name":"b5","guard":["'"${PFX}"'"]},{"name":"b6","guard":["'"${PFX}"'"]}]'
printf '%s\n' "$BROAD_LEGS" > "$d/${PFX}gate-legs.json"
printf 'SPEC_GUARD_LEGS_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
write_files_touched '### Files touched (estimate)' '`'"${PFX}x/thing.sh"'`'
git -C "$d" add -A >/dev/null
arm "a path matching only a broad guard (floor+1 legs on ${PFX}) is no hit, and the exclusion is printed with its count" 0 "$d" "excluded as broad (carried by more than 5 legs): ${PFX} (6)"
out=$(cd "$d" && "$PY" "$LINT" --list 2>&1)
if printf '%s\n' "$out" | grep -qF 'NEAR   [guards] memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md :: '"${PFX}x/thing.sh"' — matches only the broad guard(s) '"${PFX}"' (6 legs)'; then
  echo "arm ok    --list prints the broad-guard match as NEAR [guards]"; pass=$((pass+1))
else
  echo "arm FAIL  --list — expected a NEAR [guards] row for ${PFX}x/thing.sh naming the broad guard and its count"
  printf '%s\n' "$out" | grep -F 'NEAR' | head -3; fail=$((fail+1))
fi
git -C "$d" reset -q --hard "$clean"

# closing review round 1, R1 — the exclusion is BREADTH, not depth. rev-1's predicate read the guard's
# slash count, so on the real manifest `<prefix>/lib/` (30 legs) was joined and `.githooks/` (5 legs)
# was excluded. Two arms, observed RED-first on that checker: a TWO-segment guard carried by floor+1
# legs is excluded (rev-1 redded it), and a ONE-segment guard carried by one leg is joined and hits
# (rev-1 passed it).
printf '[{"name":"real leg"},{"name":"d1","guard":["'"${PFX}x/"'"]},{"name":"d2","guard":["'"${PFX}x/"'"]},{"name":"d3","guard":["'"${PFX}x/"'"]},{"name":"d4","guard":["'"${PFX}x/"'"]},{"name":"d5","guard":["'"${PFX}x/"'"]},{"name":"d6","guard":["'"${PFX}x/"'"]}]\n' > "$d/${PFX}gate-legs.json"
printf 'SPEC_GUARD_LEGS_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
write_files_touched '### Files touched (estimate)' '`'"${PFX}x/thing.sh"'`'
git -C "$d" add -A >/dev/null
arm "a two-segment guard carried by floor+1 legs is excluded by breadth, whatever its depth" 0 "$d" "excluded as broad (carried by more than 5 legs): ${PFX}x/ (6)"
printf '[{"name":"real leg"},{"name":"broad leg","guard":["'"${PFX}"'"]}]\n' > "$d/${PFX}gate-legs.json"
git -C "$d" add -A >/dev/null
arm "a one-segment guard carried by ONE leg is joined and REDS" 1 "$d" '[guards] `broad leg <- '"${PFX}x/thing.sh"'`'
# round 3, R5 — the dot tokens `./`, `../` and `<prefix>/./` declare nothing, asserted where the
# refusal is LOAD-BEARING: on this Gates-carrying spec under a bare `<prefix>/` guard, an admitted
# `<prefix>/./` is `<prefix>/.`, which starts with `<prefix>/` and counts as a second examined path (the R8
# no-Gates fixture could not see it: there the join never runs). Observed RED-first on a mutant
# checker refusing only a LEADING dot segment: `2 declared path(s) examined`.
sed -i 's|^`'"${PFX}x/thing.sh"'`$|`'"${PFX}x/thing.sh"'` · `./` · `../` · `'"${PFX}./"'`|' "$spec"
sed -i 's|^`real leg`\.|`real leg` · `broad leg`.|' "$spec"
git -C "$d" add -A >/dev/null
arm "dot tokens beside a real path declare nothing: one path examined, the named leg clean" 0 "$d" "guards join · 1 declared path(s) examined in 1 live spec(s)"
git -C "$d" reset -q --hard "$clean"

# closing review round 1, R3 — a DIRECTORY token under the sub-head is a declared PREFIX, not prose.
# rev-1 dropped every trailing-slash token before the join, so writing the folder instead of the
# files was a clean pass with no NEAR row. Symmetric: the declared prefix trips a guard it equals or
# sits under, AND a guard that sits under it — an exact-file guard included (round 2, R1 retargeted
# this arm from bare `<prefix>/`, which is a ROOT and declares nothing; observed RED on a staged break of
# the symmetric clause). Observed RED-first on the rev-1 checker, the first arm.
printf '%s\n' "$GUARD_LEGS" > "$d/${PFX}gate-legs.json"
printf 'SPEC_GUARD_LEGS_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
write_files_touched '### Files touched (estimate)' '`'"${PFX}x/"'`'
git -C "$d" add -A >/dev/null
arm "a declared directory equal to the guard trips it and REDS" 1 "$d" '[guards] `guarded leg <- '"${PFX}x/"'`'
printf '[{"name":"real leg"},{"name":"exact leg","guard":["'"${PFX}x/y.sh"'"]}]\n' > "$d/${PFX}gate-legs.json"
git -C "$d" add -A >/dev/null
arm "a declared directory that CONTAINS an exact-file guard trips it and REDS" 1 "$d" '[guards] `exact leg <- '"${PFX}x/"'`'
git -C "$d" reset -q --hard "$clean"

# closing review round 2, R1 — a ONE-SEGMENT root under the sub-head declares NOTHING. Round 1's fold
# kept `<prefix>/` as a declared prefix, so the corpus's most common negation — "No file under `<prefix>/`
# is touched" — owed every non-broad leg under `<prefix>/` (34 on the manifest at 315201b0). A root is
# prose;
# `--list` names it so the skip is not silent. Observed RED-first on the round-1 checker: exit 1.
printf '%s\n' "$GUARD_LEGS" > "$d/${PFX}gate-legs.json"
printf 'SPEC_GUARD_LEGS_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
# ONE segment whatever this install's depth: the host's first, or a stand-in at a root install.
# `${PFX}` is two segments at `vendor/gov/`, a declared prefix there, not a root (VERIFYING repair).
ONESEG="${PFX%%/*}"; ONESEG="${ONESEG:-kits}/"
write_files_touched '### Files touched (estimate)' 'New: `memory/builds/tOne/build/note.md`. No file under `'"${ONESEG}"'` is touched.'
git -C "$d" add -A >/dev/null
arm "a one-segment root in a negation sentence declares nothing and is no hit" 0 "$d" "guards join · 1 declared path(s) examined in 1 live spec(s)"
out=$(cd "$d" && "$PY" "$LINT" --list 2>&1)
if printf '%s\n' "$out" | grep -qF 'NEAR   [guards] memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md :: '"${ONESEG}"' — a one-segment root declares nothing, not joined - name the files or a directory of two or more segments'; then
  echo "arm ok    --list names the one-segment root as NEAR [guards], not joined"; pass=$((pass+1))
else
  echo "arm FAIL  --list — expected a NEAR [guards] row naming ${ONESEG} as a root that declares nothing"
  printf '%s\n' "$out" | grep -F 'NEAR' | head -3; fail=$((fail+1))
fi
git -C "$d" reset -q --hard "$clean"

# closing review round 2, R7 — breadth is counted in LEGS, not guard entries. A guard carried by
# exactly the floor with one leg listing it twice counted as floor+1 and left the join, dropping the
# motivating class silently. Observed RED-first on the round-1 checker: exit 0.
printf '[{"name":"real leg"},{"name":"f1","guard":["'"${PFX}x/"'","'"${PFX}x/"'"]},{"name":"f2","guard":["'"${PFX}x/"'"]},{"name":"f3","guard":["'"${PFX}x/"'"]},{"name":"f4","guard":["'"${PFX}x/"'"]},{"name":"f5","guard":["'"${PFX}x/"'"]}]\n' > "$d/${PFX}gate-legs.json"
printf 'SPEC_GUARD_LEGS_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
write_files_touched '### Files touched (estimate)' '`'"${PFX}x/thing.sh"'`'
git -C "$d" add -A >/dev/null
arm "a guard on exactly the floor's legs, one listing it twice, stays joined and REDS" 1 "$d" '[guards] `f1 <- '"${PFX}x/thing.sh"'`'
git -C "$d" reset -q --hard "$clean"

# closing review round 1, R4 — the join grades only a spec that CARRIES a Gates heading, the legline
# arm's own precondition: a Tier-1 spec under the light profile may omit the section, and rev-1 gave
# it one hit per tripped leg while the same run counted it as "no Gates heading to grade". Observed
# RED-first on the rev-1 checker: exit 1 with two [guards] rows. Round 2, R8: the skipped spec is
# NOT "examined" — that figure reads zero — and the path it skipped is named by a NEAR row; `./`,
# `../` and `<prefix>/./` are not declared paths at all. Observed RED-first on the round-1 checker.
printf '%s\n' "$GUARD_LEGS" > "$d/${PFX}gate-legs.json"
printf 'SPEC_GUARD_LEGS_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
write_files_touched '### Files touched (estimate)' '`'"${PFX}x/thing.sh"'` · `./` · `../` · `'"${PFX}./"'`'
awk '/^## 7[.] Gates$/{exit} {print}' "$spec" > "$d/.tmp.md"; mv "$d/.tmp.md" "$spec"
git -C "$d" add -A >/dev/null
arm "a post-cutoff spec with NO Gates heading is not joined, not examined, and is counted on the guards line" 0 "$d" "guards join · 0 declared path(s) examined in 0 live spec(s) at/after SPEC_GUARD_LEGS_CUTOFF 2026-09-01 · 0 pre-cutoff live spec(s) carry a missing guarded leg and are not graded · 0 carry no Files touched sub-head · 1 declare a path and carry no Gates heading, not joined"
out=$(cd "$d" && "$PY" "$LINT" --list 2>&1)
if [ "$(printf '%s\n' "$out" | grep -c 'NEAR   \[guards\]')" = 1 ] \
   && printf '%s\n' "$out" | grep -qF ':: '"${PFX}x/thing.sh"' — no Gates heading, not joined'; then
  echo "arm ok    --list names the skipped path as NEAR [guards] and nothing else (dot tokens declare nothing)"; pass=$((pass+1))
else
  echo "arm FAIL  --list — expected exactly one NEAR [guards] row, naming ${PFX}x/thing.sh as skipped for no Gates heading"
  printf '%s\n' "$out" | grep -F 'NEAR' | head -5; fail=$((fail+1))
fi
git -C "$d" reset -q --hard "$clean"

# closing review round 1, R12 — the EXACT-FILE branch of check_guard_trips, seen to fail. Every arm
# above uses the directory guard, so `path == guard` and the docstring's `x.sh.bak` non-prefix claim
# were asserted by prose alone; the live manifest carries exact-file guards. The `.bak` sibling is
# path-shaped (a slash and an extension) and untracked, which the guards join does not grade.
printf '[{"name":"real leg"},{"name":"exact leg","guard":["'"${PFX}x/thing.sh"'"]}]\n' > "$d/${PFX}gate-legs.json"
printf 'SPEC_GUARD_LEGS_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
write_files_touched '### Files touched (estimate)' '`'"${PFX}x/thing.sh.bak"'`'
git -C "$d" add -A >/dev/null
arm "an exact-file guard does not trip on a .bak sibling" 0 "$d" "guards join · 1 declared path(s) examined"
sed -i 's|^`'"${PFX}x/thing.sh.bak"'`$|`'"${PFX}x/thing.sh"'`|' "$spec"
git -C "$d" add -A >/dev/null
arm "an exact-file guard trips on the file itself and REDS" 1 "$d" '[guards] `exact leg <- '"${PFX}x/thing.sh"'`'
git -C "$d" reset -q --hard "$clean"

# AC5 — a waiver row keyed on the COMPOSITE token clears the hit and is counted; a bare row keyed
#       on the leg name alone does not consume it, so the hit stays live and the row reds as stale.
printf '%s\n' "$GUARD_LEGS" > "$d/${PFX}gate-legs.json"
printf 'SPEC_GUARD_LEGS_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
write_files_touched '### Files touched (estimate)' '`'"${PFX}x/thing.sh"'`'
printf 'guarded leg <- '"${PFX}x/thing.sh"'\t[guards] deliberate, for this arm\n' >> "$d/memory/project/spec-token-waivers.txt"
git -C "$d" add -A >/dev/null
arm "a [guards] waiver row keyed on the composite token clears the hit and is counted" 0 "$d" "1 waiver(s)"
sed -i 's|^guarded leg <- '"${PFX}x/thing.sh"'\t|guarded leg\t|' "$d/memory/project/spec-token-waivers.txt"
git -C "$d" add -A >/dev/null
arm "a waiver row keyed on the bare leg name does not consume a guards hit" 1 "$d" '[guards] `guarded leg <- '"${PFX}x/thing.sh"'`'
git -C "$d" reset -q --hard "$clean"

# closing review F10's rule, for the new key — a non-ISO value is REFUSED, never armed.
printf 'SPEC_GUARD_LEGS_CUTOFF="2026-9-8"\n' > "$d/.memory-tree.conf"
git -C "$d" add -A >/dev/null
arm "a non-ISO SPEC_GUARD_LEGS_CUTOFF is REFUSED like the other cutoff keys" 1 "$d" "REFUSING — SPEC_GUARD_LEGS_CUTOFF 2026-9-8 is not an ISO date"
git -C "$d" reset -q --hard "$clean"

# AC17's relation, for the new key — a COMMITTED value not strictly past its own commit day is
# REFUSED before grading. The relation block is one helper for both keys, so this observes the
# second caller rather than trusting the first.
printf 'SPEC_GUARD_LEGS_CUTOFF="2026-09-02"\n' > "$d/.memory-tree.conf"
git -C "$d" add -A >/dev/null; git -C "$d" commit -qm guardcutoff --no-verify
day=$(git -C "$d" log -1 --format=%cs)
arm "a committed SPEC_GUARD_LEGS_CUTOFF not strictly past its own commit day is REFUSED" 1 "$d" "REFUSING — SPEC_GUARD_LEGS_CUTOFF 2026-09-02 is not strictly past $day"
git -C "$d" reset -q --hard "$clean"

# The WAIVER family: its committed clean state IS the AC1 fixture, and the commit is dated the day
# before its cutoff so the relation holds and the arms grade rather than refuse.
d=$base/barwaiver; scratch "$d"
mkdir -p "$d/${PFX}${RUN_GATES}"; : > "$d/${PFX}${RUN_GATES}/run-gates.sh"
printf 'SPEC_DIRECT_CUTOFF="2026-09-01"\n' > "$d/.memory-tree.conf"
sed -i 's|`'"${PFX}gate-legs.json"'` exists|`GATE_SELFTESTS=1 bash '"${PFX}${RUN_GATES}/run-gates.sh"'` is green|' "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
git -C "$d" add -A >/dev/null
GIT_COMMITTER_DATE=2026-08-31T12:00:00 git -C "$d" commit -qm ac1 --no-verify
clean=$(git -C "$d" rev-parse HEAD)

# AC6 — a waiver row keyed on the token, reason opening `[bar]`, clears the hit and is counted.
printf 'GATE_SELFTESTS=1 bash '"${PFX}${RUN_GATES}/run-gates.sh"'\t[bar] deliberate, for this arm\n' >> "$d/memory/project/spec-token-waivers.txt"
git -C "$d" add -A >/dev/null
arm "a [bar] waiver row keyed on the token clears the hit and is counted" 0 "$d" "1 waiver(s)"
git -C "$d" reset -q --hard "$clean"

# AC7 — a [bar] row naming a token no spec carries REDS as stale, like any other row.
printf 'GATE_FULL=1 bash '"${PFX}${RUN_GATES}/run-gates.sh"'\t[bar] no spec names this\n' >> "$d/memory/project/spec-token-waivers.txt"
git -C "$d" add -A >/dev/null
arm "a [bar] waiver row nothing produces REDS as stale" 1 "$d" "STALE WAIVER"
git -C "$d" reset -q --hard "$clean"

# closing review F4 — a LATER commit that requotes the cutoff line (quoted to bare) is not the
# setting commit. `git log -G` matched the removed and the added line and re-dated the value to
# 2026-09-20, so the gate refused a cutoff nobody re-set; `--pickaxe-regex -S` reads the occurrence
# count, which a requote or a move leaves at one. The waiver row keeps the graded run at exit 0, so
# the two outcomes differ in rc and not only in text. Observed RED-first on the `-G` checker.
printf 'GATE_SELFTESTS=1 bash '"${PFX}${RUN_GATES}/run-gates.sh"'\t[bar] deliberate, for this arm\n' >> "$d/memory/project/spec-token-waivers.txt"
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
# ---- TOOL-dGatedProse-2: the claims join. A dossier-claim sentence whose backticked object is a
#      PATH, a GLOB or a CODE SYMBOL names a shape the codebase map cannot hold as a key, and reds.
#      TWO halves. The DIRECT half loads the checker as a module and calls `scan_claims` on
#      spec-shaped input, because AC1, AC2, AC3, AC7 and AC12 grade the scan's own return, and AC4
#      enumerates every key of every ratchet inventory from the real tree through it; each of its
#      verdicts is one assertion below. The PROCESS half runs the checker, or a broken copy of it,
#      in a scratch repo: AC6's staged breaks, AC8's report line and --list rows, and AC1's hit as the
#      report prints it. Each arm was observed RED on the checker before this join, which printed no
#      claims line, carried no `scan_claims` and exited 0 over every fixture here.
MAPKIT="$(git -C "$HERE" rev-parse --show-toplevel)/$CODEBASE_MAP_DIR"
cat > "$base/claims-direct.py" <<'PYEOF'
import importlib.util, os, sys
P = sys.argv[3]   # the install prefix with its slash, handed in by the suite
RL = sys.argv[4]  # the runlog kit's directory NAME in this install (TOOL-aRepatriatedFork-46)
spec = importlib.util.spec_from_file_location("cst", sys.argv[1])
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def print_verdict(label, ok, detail):
    print(("ok " + label) if ok else ("FAIL " + label + " :: " + str(detail)))

def check_one_hit(label, text, obj, cls, arm):
    runs, hits, clears = m.scan_claims(text)
    ok = len(hits) == 1 and hits[0][1] == obj and hits[0][2] == cls and arm in hits[0][3]
    print_verdict(label, ok, [(h[1], h[2], h[3]) for h in hits])

def check_clears_only(label, text):
    runs, hits, clears = m.scan_claims(text)
    print_verdict(label, runs >= 1 and not hits, "runs=%d hits=%s" % (runs, [(h[1], h[2]) for h in hits]))

# AC1 -- the two motivating sentences, copied verbatim from their blobs at 9f43bb26^.
check_one_hit("AC1 unit 25",
        "- **S6** The docs. The kit README's Summary section states the three closers and the lag S3 declares,\n"
        "  and `memory/map/features/runlog.md` claims `derive_window_closer`. NOT OBSERVED: prose, and the map's\n"
        "  coverage leg grades the claim at the close.\n", "derive_window_closer", "CODE SYMBOL", "active")
check_one_hit("AC1 unit 27",
        "- **S7** The docs. The kit README's paragraph on unknown values names `count_sources` and the\n"
        "  `withheld rows` fact, and `memory/map/features/runlog.md` claims `check_count_sources`. NOT OBSERVED:\n"
        "  prose, and the map's coverage leg grades the claim at the close.\n", "check_count_sources", "CODE SYMBOL", "active")
# AC2 -- three CLOSED specs' sentences, verbatim; the first wraps its object onto the next line.
check_clears_only("AC2 kickoff dossier",
            "- S10. A new codebase-map dossier at `memory/map/features/kickoff.md` claiming\n"
            "  `guides = [\"SESSION-KICKOFF.md\"]`, plus a regeneration of `memory/map/generated/`.\n")
check_clears_only("AC2 unattended dossier",
            "- **No dossier edit.** `memory/map/features/unattended.md` claims `unattended-unit.js` and measures\n"
            "  20470 bytes against a 20480-byte `DOSSIER_CAP_BYTES`; it describes the kit's gates and refusals,\n")
check_clears_only("AC2 run-gates dossier",
            "- **S12** — author `memory/map/features/run-gates.md` claiming the `kits` key and the gate-leg keys\n"
            "  THIS unit creates, and drop the now-claimed row from `memory/map/baseline.toml`.\n")
# AC3 -- the forward-looking claim: a key-shaped token no tree holds yet clears, since nothing resolves.
check_clears_only("AC3 unwritten key", "`memory/map/features/runlog.md` claims `tUnwrittenLeg-not-yet-built` once it lands.\n")
# AC7 -- the same refused sentence fenced and unfenced: one hit, on the unfenced line.
s = "`memory/map/features/runlog.md` claims `derive_window_closer`."
runs, hits, clears = m.scan_claims("prose\n```\n" + s + "\n```\n" + s + "\n")
print_verdict("AC7 fenced copy", len(hits) == 1 and hits[0][0] == 5, [(h[0], h[1]) for h in hits])
# AC12 -- one fixture per arm, then the active arm with an UPPERCASE verb and with a SHOUTED constant.
check_one_hit("AC12 active", "`memory/map/features/runlog.md` claims `derive_window_closer`.", "derive_window_closer", "CODE SYMBOL", "active")
check_one_hit("AC12 passive", f"`{P}{RL}/runlog.py` is claimed by `memory/map/features/runlog.md`.", f"{P}{RL}/runlog.py", "PATH", "passive")
check_one_hit("AC12 noun", f"`memory/map/features/runlog.md` makes a claim on `{P}{RL}/*.py` here.", f"{P}{RL}/*.py", "GLOB", "noun")
check_one_hit("AC12 fronted", "`check_count_sources`, which `runlog.md` now claims, stays.", "check_count_sources", "CODE SYMBOL", "fronted")
check_one_hit("AC12 uppercase verb", "`memory/map/features/runlog.md` CLAIMS `derive_window_closer`.", "derive_window_closer", "CODE SYMBOL", "active")
check_one_hit("AC12 shouted constant", "`memory/map/features/runlog.md` claims `KIT_MEMORY_TREE_VERSION`.", "KIT_MEMORY_TREE_VERSION", "CODE SYMBOL", "active")
# R3 (closing review, round 1) -- the fence machine is the engine's `_unfenced`. A tilde fence holding
# a lone backtick line closes on its OWN marker, so the claim after it is graded; a claim inside a
# tilde fence is blanked. The boolean toggle this replaced read both of these the other way round.
runs, hits, clears = m.scan_claims("prose\n~~~\n```\n~~~\n" + s + "\n")
print_verdict("R3 tilde fence closes on its own marker", len(hits) == 1 and hits[0][0] == 5, [(h[0], h[1]) for h in hits])
runs, hits, clears = m.scan_claims("prose\n~~~\n" + s + "\n~~~\n")
print_verdict("R3 a claim inside a tilde fence is blanked", not hits, [(h[0], h[1]) for h in hits])
# AC4 -- DISJOINTNESS over the live key set, never resolution: every key of every ratchet inventory,
# enumerated from the real tree by the map's own extractors, through the real scan. Both counts are
# the enumeration's, printed rather than typed.
try:
    os.environ.pop("CODEBASE_MAP_ROOT", None)
    sys.path.insert(0, sys.argv[2])
    import map_extractors
    inv = map_extractors.all_inventories()
    keys = [k for v in inv.values() for k in v]
    bad = [k for k in keys if (lambda r: r[0] != 1 or r[1])(m.scan_claims("`memory/map/features/x.md` claims `%s`." % k))]
    print("info AC4: %d key(s) examined over %d inventories, %d carrying a parenthesis" % (len(keys), len(inv), sum("(" in k for k in keys)))
    print_verdict("AC4 live keys", bool(keys) and not bad, "refused or unmatched: %s" % bad[:5])
except Exception as exc:  # the map kit absent or failing is a FAIL, never a skip
    print_verdict("AC4 live keys", False, "the key enumeration did not run: %r" % exc)
PYEOF
claims=$("$PY" "$base/claims-direct.py" "$LINT" "$MAPKIT" "$PFX" "$RUNLOG" 2>&1 | tr -d '\r')
printf '%s\n' "$claims" | grep '^info ' | sed 's/^info /          /'
check_claims_verdict() { printf '%s\n' "$claims" | grep -qxF "ok $1"; }   # $1 = a label the direct half printed
print_claims_detail() { printf '%s\n' "$claims" | grep -F "$1" | head -2; }
if check_claims_verdict "AC1 unit 25"; then echo "arm ok    AC1 unit 25's sentence yields one CODE SYMBOL hit on derive_window_closer"; pass=$((pass+1)); else echo "arm FAIL  AC1 unit 25"; print_claims_detail "AC1 unit 25"; fail=$((fail+1)); fi
if check_claims_verdict "AC1 unit 27"; then echo "arm ok    AC1 unit 27's sentence yields one CODE SYMBOL hit on check_count_sources"; pass=$((pass+1)); else echo "arm FAIL  AC1 unit 27"; print_claims_detail "AC1 unit 27"; fail=$((fail+1)); fi
if check_claims_verdict "AC2 kickoff dossier"; then echo "arm ok    AC2 the wrapped kickoff-dossier sentence matches an arm and clears"; pass=$((pass+1)); else echo "arm FAIL  AC2 kickoff dossier"; print_claims_detail "AC2 kickoff" ; fail=$((fail+1)); fi
if check_claims_verdict "AC2 unattended dossier"; then echo "arm ok    AC2 the unattended-dossier sentence matches an arm and clears"; pass=$((pass+1)); else echo "arm FAIL  AC2 unattended dossier"; print_claims_detail "AC2 unattended"; fail=$((fail+1)); fi
if check_claims_verdict "AC2 run-gates dossier"; then echo "arm ok    AC2 the run-gates-dossier sentence matches an arm and clears"; pass=$((pass+1)); else echo "arm FAIL  AC2 run-gates dossier"; print_claims_detail "AC2 run-gates"; fail=$((fail+1)); fi
if check_claims_verdict "AC3 unwritten key"; then echo "arm ok    AC3 a claim on a key no tree holds yet matches an arm and clears"; pass=$((pass+1)); else echo "arm FAIL  AC3 unwritten key"; print_claims_detail "AC3"; fail=$((fail+1)); fi
if check_claims_verdict "AC7 fenced copy"; then echo "arm ok    AC7 a fenced copy is blanked: one hit, on the unfenced line"; pass=$((pass+1)); else echo "arm FAIL  AC7 fenced copy"; print_claims_detail "AC7"; fail=$((fail+1)); fi
if check_claims_verdict "AC12 active"; then echo "arm ok    AC12 the active arm reaches its own fixture"; pass=$((pass+1)); else echo "arm FAIL  AC12 active"; print_claims_detail "AC12 active"; fail=$((fail+1)); fi
if check_claims_verdict "AC12 passive"; then echo "arm ok    AC12 the passive arm reaches its own fixture"; pass=$((pass+1)); else echo "arm FAIL  AC12 passive"; print_claims_detail "AC12 passive"; fail=$((fail+1)); fi
if check_claims_verdict "AC12 noun"; then echo "arm ok    AC12 the noun arm reaches its own fixture"; pass=$((pass+1)); else echo "arm FAIL  AC12 noun"; print_claims_detail "AC12 noun"; fail=$((fail+1)); fi
if check_claims_verdict "AC12 fronted"; then echo "arm ok    AC12 the fronted arm reaches its own fixture"; pass=$((pass+1)); else echo "arm FAIL  AC12 fronted"; print_claims_detail "AC12 fronted"; fail=$((fail+1)); fi
if check_claims_verdict "AC12 uppercase verb"; then echo "arm ok    AC12 an UPPERCASE verb is folded"; pass=$((pass+1)); else echo "arm FAIL  AC12 uppercase verb"; print_claims_detail "AC12 uppercase"; fail=$((fail+1)); fi
if check_claims_verdict "AC12 shouted constant"; then echo "arm ok    AC12 a SHOUTED constant refuses as CODE SYMBOL"; pass=$((pass+1)); else echo "arm FAIL  AC12 shouted constant"; print_claims_detail "AC12 shouted"; fail=$((fail+1)); fi
if check_claims_verdict "R3 tilde fence closes on its own marker"; then echo "arm ok    R3 a tilde fence holding a lone backtick line closes on its own marker: one hit, on the unfenced line"; pass=$((pass+1)); else echo "arm FAIL  R3 tilde fence closes on its own marker"; print_claims_detail "R3 tilde fence"; fail=$((fail+1)); fi
if check_claims_verdict "R3 a claim inside a tilde fence is blanked"; then echo "arm ok    R3 a refused claim inside a tilde fence is blanked: no hit"; pass=$((pass+1)); else echo "arm FAIL  R3 a claim inside a tilde fence is blanked"; print_claims_detail "R3 a claim inside"; fail=$((fail+1)); fi
if check_claims_verdict "AC4 live keys"; then echo "arm ok    AC4 no key of any ratchet inventory is refused, over the population printed above"; pass=$((pass+1)); else echo "arm FAIL  AC4 live keys"; print_claims_detail "AC4"; fail=$((fail+1)); fi

# The PROCESS half, over one scratch repo reset between fixtures.
d=$base/claims; scratch "$d"
clean=$(git -C "$d" rev-parse HEAD)
spec="$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"

# AC6 — the staged breaks: each arm in turn made to match nothing, the case fold dropped, and the
#       space clause dropped. Each broken COPY must refuse naming CLAIM_CANARY and print no claims
#       line. A substitution that missed leaves an unbroken copy, which exits 0 and reds the arm.
check_break_refuses() {   # $1 = a broken copy of the checker
  local out rc; out=$(cd "$d" && "$PY" "$1" 2>&1); rc=$?
  [ "$rc" != 0 ] && printf '%s' "$out" | grep -qF 'REFUSING — CLAIM_CANARY' && ! printf '%s' "$out" | grep -qF 'spec-tokens: claims join'
}
for a in active passive noun fronted; do sed "s|(\"$a\", r\"|(\"$a\", r\"(?!)|" "$LINT" > "$base/claims-break-$a.py"; done
sed 's|CLAIM_PARTS), re\.I)|CLAIM_PARTS))|' "$LINT" > "$base/claims-break-fold.py"
sed '/cleared by the space clause/d' "$LINT" > "$base/claims-break-space.py"
if check_break_refuses "$base/claims-break-active.py"; then echo "arm ok    AC6 the active arm matching nothing refuses naming CLAIM_CANARY"; pass=$((pass+1)); else echo "arm FAIL  AC6 active arm break — expected a CLAIM_CANARY refusal and no claims line"; fail=$((fail+1)); fi
if check_break_refuses "$base/claims-break-passive.py"; then echo "arm ok    AC6 the passive arm matching nothing refuses naming CLAIM_CANARY"; pass=$((pass+1)); else echo "arm FAIL  AC6 passive arm break — expected a CLAIM_CANARY refusal and no claims line"; fail=$((fail+1)); fi
if check_break_refuses "$base/claims-break-noun.py"; then echo "arm ok    AC6 the noun arm matching nothing refuses naming CLAIM_CANARY"; pass=$((pass+1)); else echo "arm FAIL  AC6 noun arm break — expected a CLAIM_CANARY refusal and no claims line"; fail=$((fail+1)); fi
if check_break_refuses "$base/claims-break-fronted.py"; then echo "arm ok    AC6 the fronted arm matching nothing refuses naming CLAIM_CANARY"; pass=$((pass+1)); else echo "arm FAIL  AC6 fronted arm break — expected a CLAIM_CANARY refusal and no claims line"; fail=$((fail+1)); fi
if check_break_refuses "$base/claims-break-fold.py"; then echo "arm ok    AC6 the arms compiled without the case fold refuse naming CLAIM_CANARY"; pass=$((pass+1)); else echo "arm FAIL  AC6 case-fold break — expected a CLAIM_CANARY refusal and no claims line"; fail=$((fail+1)); fi
if check_break_refuses "$base/claims-break-space.py"; then echo "arm ok    AC6 the space clause dropped refuses naming CLAIM_CANARY, the LOUDER direction"; pass=$((pass+1)); else echo "arm FAIL  AC6 space-clause break — expected a CLAIM_CANARY refusal and no claims line"; fail=$((fail+1)); fi

# AC8 — the join's line prints on EVERY run: a tree with no claim sentence reports three zeros.
arm "a tree with no dossier-claim sentence still prints the claims line, zeros and all" 0 "$d" "claims join · 0 dossier-claim sentence(s) examined · 0 live spec(s) carry one · 0 object(s) cleared"
# ...and the figures are COUNTED: two live specs, one carrying four clearing sentences and five
#    objects, the fourth sentence claiming two objects through a conjunction.
cat > "$spec" <<'SPEC'
# TOOL-tOne-1 — a unit

**Status:** OPEN · rev-1 · 2026-09-02 · node t · Tier-1 · base 0123abcd · streams tooling

## 4. Design

- S10. A new codebase-map dossier at `memory/map/features/kickoff.md` claiming
  `guides = ["SESSION-KICKOFF.md"]`, plus a regeneration of `memory/map/generated/`.
- **No dossier edit.** `memory/map/features/unattended.md` claims `unattended-unit.js` and measures
  20470 bytes against a 20480-byte `DOSSIER_CAP_BYTES`; it describes the kit's gates and refusals,
- **S12** — author `memory/map/features/run-gates.md` claiming the `kits` key and the gate-leg keys
  THIS unit creates.
- `memory/map/features/runlog.md` will claim `tUnwrittenLeg-a` and `tUnwrittenLeg-b` once they land.

## 6. Acceptance criteria

- **AC1** — `{PFX}gate-legs.json` exists.

## 7. Gates

`real leg`.
SPEC
sed -i "s#{PFX}#${PFX}#g; s#{RUN_GATES}#${RUN_GATES}#g" "$spec"   # the quoted heredoc cannot expand either
cat > "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-2.md" <<'SPEC'
# TOOL-tOne-2 — a second unit, carrying no dossier-claim sentence

**Status:** OPEN · rev-1 · 2026-09-02 · node t · Tier-1 · base 0123abcd · streams tooling

## 6. Acceptance criteria

- **AC1** — `{PFX}gate-legs.json` exists.

## 7. Gates

`real leg`.
SPEC
sed -i "s#{PFX}#${PFX}#g" "$d/memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-2.md"   # the quoted heredoc cannot expand the prefix
git -C "$d" add -A >/dev/null
arm "four clearing sentences and five objects in one of two live specs are COUNTED on the claims line" 0 "$d" "claims join · 4 dossier-claim sentence(s) examined · 1 live spec(s) carry one · 5 object(s) cleared"
out=$(cd "$d" && "$PY" "$LINT" --list 2>&1)
if [ "$(printf '%s\n' "$out" | grep -c 'NEAR   \[claims\]')" = 5 ] \
   && [ "$(printf '%s\n' "$out" | grep -cF ':: claims <- guides = ["SESSION-KICKOFF.md"] — ')" = 1 ] \
   && [ "$(printf '%s\n' "$out" | grep -cF ':: claims <- unattended-unit.js — ')" = 1 ] \
   && [ "$(printf '%s\n' "$out" | grep -cF ':: claims <- kits — ')" = 1 ] \
   && [ "$(printf '%s\n' "$out" | grep -cF ':: claims <- tUnwrittenLeg-a — ')" = 1 ] \
   && [ "$(printf '%s\n' "$out" | grep -cF ':: claims <- tUnwrittenLeg-b — ')" = 1 ] \
   && ! printf '%s\n' "$out" | grep -q 'HIT    \[claims\]'; then
  echo "arm ok    --list prints each cleared object once as NEAR [claims], and none as a hit"; pass=$((pass+1))
else
  echo "arm FAIL  --list — expected exactly five NEAR [claims] rows, one per cleared object, and no [claims] hit"
  printf '%s\n' "$out" | grep -F '[claims]' | head -6; fail=$((fail+1))
fi
git -C "$d" reset -q --hard "$clean"

# AC1, as the report prints it — the unit-25 sentence in a live spec REDS the checker, naming the
#      class, the arm and the contract sentence.
sed -i 's|^## 6. Acceptance criteria$|## 4. Design\n\n  and `memory/map/features/runlog.md` claims `derive_window_closer`. NOT OBSERVED: prose, and the map'"'"'s\n\n## 6. Acceptance criteria|' "$spec"
git -C "$d" add -A >/dev/null
arm "the unit-25 sentence in a live spec REDS as [claims], naming the class, the arm and the contract" 1 "$d" '-spec-TOOL-tOne-1.md [claims] `claims <- derive_window_closer` — CODE SYMBOL at line 7, arm(s) active — a codebase-map dossier claims EXACT inventory keys and no key is a CODE SYMBOL: the symbol tier feeds generated/symbols.json only'
git -C "$d" reset -q --hard "$clean"

# R1 (closing review, round 1) — a claims hit answers to its OWN composite token. A `[path]` waiver
#      on the bare string, used by the path hit, must not also swallow the claims refusal of it.
sed -i 's|`'"${PFX}gate-legs.json"'` exists|`'"${PFX}nope.sh"'` exists|' "$spec"
sed -i 's|^## 6. Acceptance criteria$|## 4. Design\n\n`memory/map/features/runlog.md` claims `'"${PFX}nope.sh"'`.\n\n## 6. Acceptance criteria|' "$spec"
printf ''"${PFX}nope.sh"'\t[path] deliberate, for this arm\n' >> "$d/memory/project/spec-token-waivers.txt"
git -C "$d" add -A >/dev/null
arm "R1 a [path] waiver on the bare string does not swallow a claims refusal of it" 1 "$d" '[claims] `claims <- '"${PFX}nope.sh"'`'
git -C "$d" reset -q --hard "$clean"

# R1 — ...and a claims hit keeps no `[path]` row alive: with the path hit gone, the row reads stale
#      while a claims sentence still names the string, under a row of its own that waives it.
sed -i 's|^## 6. Acceptance criteria$|## 4. Design\n\n`memory/map/features/runlog.md` claims `'"${PFX}nope.sh"'`.\n\n## 6. Acceptance criteria|' "$spec"
printf ''"${PFX}nope.sh"'\t[path] no path hit is left\nclaims <- '"${PFX}nope.sh"'\t[claims] deliberate, for this arm\n' >> "$d/memory/project/spec-token-waivers.txt"
git -C "$d" add -A >/dev/null
arm "R1 a [path] row whose path hit is gone reads stale though a claims sentence names the string" 1 "$d" 'STALE WAIVER `'"${PFX}nope.sh"'` — no spec produces this hit any more'
git -C "$d" reset -q --hard "$clean"

# R1 — ...and the remedy the fold documents works: the composite token, the only row, waives the
#      claims hit it names, so the run is green and --list reports the hit as WAIVED (round 2, F3).
sed -i 's|^## 6. Acceptance criteria$|## 4. Design\n\n`memory/map/features/runlog.md` claims `'"${PFX}nope.sh"'`.\n\n## 6. Acceptance criteria|' "$spec"
printf 'claims <- '"${PFX}nope.sh"'\t[claims] deliberate, for this arm\n' >> "$d/memory/project/spec-token-waivers.txt"
git -C "$d" add -A >/dev/null
# The VERDICT comes from a plain run, because --list exits 0 and returns before any stale row prints;
# --list is read only for the WAIVED row, which proves the hit exists and was waived rather than missed.
out=$(cd "$d" && "$PY" "$LINT" 2>&1); rc=$?
lst=$(cd "$d" && "$PY" "$LINT" --list 2>&1)
if [ "$rc" = 0 ] && printf '%s\n' "$lst" | grep -qF 'WAIVED [claims]' && ! printf '%s\n' "$out" | grep -qF 'STALE WAIVER'; then
  echo "arm ok    R1 the composite token alone in the registry waives the claims hit it names"; pass=$((pass+1))
else
  echo "arm FAIL  R1 the composite waiver — expected rc 0, a WAIVED [claims] row and no stale row, got rc $rc"
  printf '%s\n' "$out" | grep -E 'claims|STALE' | head -3; fail=$((fail+1))
fi
git -C "$d" reset -q --hard "$clean"

# ---- TOOL-aMendedFleet-25: the size join. One fixture tree with a class row at a small ceiling, a
#      second live spec over it HELD by a high-water row, and the first spec padded past it.
d=$base/size; scratch "$d"
sp=memory/builds/tOne/spec
cp "$d/$sp/2026-09-02-spec-TOOL-tOne-1.md" "$d/$sp/2026-09-02-spec-TOOL-tOne-2.md"
printf '%0700d\n' 0 >> "$d/$sp/2026-09-02-spec-TOOL-tOne-2.md"
held=$(tr -d '\r' < "$d/$sp/2026-09-02-spec-TOOL-tOne-2.md" | wc -c | tr -d '[:space:]')
printf '# limits\nmemory/builds/*/spec/\t600\n' > "$d/${PFX}template-size-limits.txt"
printf '%s\t%s\n' "$sp/2026-09-02-spec-TOOL-tOne-2.md" "$held" > "$d/${PFX}template-size-highwater.txt"
git -C "$d" add -A >/dev/null; git -C "$d" commit -qm size --no-verify; sized=$(git -C "$d" rev-parse HEAD)
arm "a spec over the class ceiling with a high-water row is HELD and the line counts it" 0 "$d" "size join · 2 live spec(s) · ceiling 600 from ${PFX}template-size-limits.txt · largest unheld"
arm "the held count rides the size line" 0 "$d" "1 held at a recorded high-water"
printf '%0700d\n' 0 >> "$d/$sp/2026-09-02-spec-TOOL-tOne-1.md"
arm "a live spec padded past the ceiling with no row REDS as [size]" 1 "$d" "[size] \`size <- $sp/2026-09-02-spec-TOOL-tOne-1.md\`"
git -C "$d" reset -q --hard "$sized"
printf 'one more line\n' >> "$d/$sp/2026-09-02-spec-TOOL-tOne-2.md"
arm "a held spec grown by one line REDS naming its recorded high-water" 1 "$d" "held at its recorded high-water $held"
git -C "$d" reset -q --hard "$sized"
sed -i 's/^\*\*Status:\*\* OPEN/**Status:** CLOSED/' "$d/$sp/2026-09-02-spec-TOOL-tOne-2.md"
arm "a high-water row for a terminal spec REDS as stale" 1 "$d" "STALE HIGH-WATER \`$sp/2026-09-02-spec-TOOL-tOne-2.md\` — in ${PFX}template-size-highwater.txt — terminal"
git -C "$d" reset -q --hard "$sized"
printf '# limits, no class row\n' > "$d/${PFX}template-size-limits.txt"
arm "no class row turns the size join off, announced" 0 "$d" "no class row in ${PFX}template-size-limits.txt (arm off)"
printf 'memory/builds/*/spec/\tlots\n' > "$d/${PFX}template-size-limits.txt"
arm "a class row that is not a number REFUSES" 1 "$d" "REFUSING — the size join's row for memory/builds/*/spec/"
git -C "$d" reset -q --hard "$sized"

# ---- TOOL-aMendedFleet-75: the covers join. The scratch spec defines only AC1; each edit appends
#      one `New arm:` line to its section 7 and the checker re-runs. Staged red by deleting the
#      scan_arm_covers call.
d=$base/covers; scratch "$d"
cs=memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md
cvbase=$(git -C "$d" rev-parse HEAD)
printf '\nNew arm: `x.test.sh` · covers AC1 AC9 · a dangling id · none\n' >> "$d/$cs"
arm "a covers field naming an id section 6 does not define REDS as [covers]" 1 "$d" "[covers] \`covers <- $cs AC9\`" "\`covers <- $cs AC1\`"
arm "the covers line counts the arm line, the carrier and both tokens" 1 "$d" "covers join · 1 New arm line(s) in 1 live spec(s) · 1 carry a covers field · 2 token(s) graded"
git -C "$d" reset -q --hard "$cvbase"
printf '\nNew arm: `x.test.sh` · covers AC1 · a defined id · none\n' >> "$d/$cs"
arm "a covers field naming a defined id is clean" 0 "$d" "1 carry a covers field" "[covers]"
git -C "$d" reset -q --hard "$cvbase"
printf '\nNew arm: `x.test.sh` · covers none · no criterion · none\n' >> "$d/$cs"
arm "covers none standing alone is clean" 0 "$d" "1 token(s) graded" "[covers]"
git -C "$d" reset -q --hard "$cvbase"
printf '\nNew arm: `x.test.sh` · covers none AC1 · none beside an id · none\n' >> "$d/$cs"
arm "covers none beside an id REDS naming none" 1 "$d" "[covers] \`covers <- $cs none\`"
git -C "$d" reset -q --hard "$cvbase"
printf '\nNew arm: `x.test.sh` · AC9 named in prose only · none\n' >> "$d/$cs"
arm "an id in the line's prose with no covers field is not graded" 0 "$d" "1 New arm line(s) in 1 live spec(s) · 0 carry a covers field" "[covers]"
git -C "$d" reset -q --hard "$cvbase"
printf '\nNew arm: `x.test.sh` · a field on the next line\n  · covers AC9 · none\n' >> "$d/$cs"
arm "a covers field on an indented continuation line is graded" 1 "$d" "[covers] \`covers <- $cs AC9\`"
git -C "$d" reset -q --hard "$cvbase"

total=$((pass+fail))
if [ "$total" -lt "$FLOOR_ASSERTIONS" ]; then
  echo "check-spec-tokens: $total assertion(s) executed, below the declared floor of $FLOOR_ASSERTIONS —"
  echo "  arms went missing rather than failing, which reports as success without this check."
  exit 1
fi
[ "$fail" = 0 ] && echo "PASS ($total assertions)"
[ "$fail" = 0 ] || { echo "check-spec-tokens: $fail of $total assertion(s) failed"; exit 1; }
