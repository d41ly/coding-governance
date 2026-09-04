#!/usr/bin/env bash
# Scaffold an empty, hygiene-passing structured memory tree from .memory-tree.conf.
# For a NEW project. (A project MIGRATING an existing docs tree does that once as its own landing —
# see README.md "Adopting into an existing tree"; the tree shape below is the target either way.)
#
#   tools/memory-tree/adopt-memory-tree.sh --scaffold
set -eu
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
HERE="$(cd "$(dirname "$0")" && pwd)"
# This install's own prefix, derived once and used for every path this script WRITES or PRINTS.
# Both sides are normalised through the same `cd ... && pwd` chain on purpose: under MSYS one
# directory has two spellings (a drive-letter one from `git rev-parse`, a mount-point one from
# `pwd`) and a raw strip across those flavors silently yields an ABSOLUTE path, which then
# substitutes nothing and looks like it worked.
ROOT_N="$(cd "$ROOT" && pwd)"
KIT_REL=${HERE#"$ROOT_N"/}
# CAPTURED, because the branch below REASSIGNS KIT_REL and the fact is needed again further down.
# Comparing $HERE against the raw $ROOT instead is the two-spellings trap this file's own header
# warns about twelve lines up: $ROOT is `C:/...` from `git rev-parse` and $HERE is `/c/...` from
# `cd && pwd`, so `case "$HERE/" in "$ROOT"/*)` never matches on any node in the registry. It shipped
# that way for one commit and made the ceiling strip DEAD everywhere while printing an else-arm
# instruction telling the operator to do what they had just done.
KIT_INSIDE=yes
if [ "$KIT_REL" = "$HERE" ]; then
  KIT_INSIDE=no
  # The kit dir is OUTSIDE the tree being scaffolded — the legitimate "run the shipped adopter from
  # the governance checkout against a fresh repo" flow, which the runbook's copy-then-run order does
  # not cover but people use. Scaffolding is still correct: every asset is read from $HERE and every
  # file is written under $ROOT. Only the PRINTED and RENDERED paths have no repo-relative answer, so
  # they name the DECLARED convention — which is where the operator is about to copy the kit anyway.
  # Refusing here would break a working flow to protect a cosmetic string.
  KIT_REL="tools/$(basename "$HERE")"
  echo "memory-tree: the kit dir is outside this repo — printed paths will name the declared '$KIT_REL' prefix." >&2
fi
TOOL_ROOT=${KIT_REL%/*}; [ "$TOOL_ROOT" = "$KIT_REL" ] && TOOL_ROOT=""   # "tools" at a prefix, "" at the root
[ -z "$TOOL_ROOT" ] || TOOL_ROOT="$TOOL_ROOT/"                          # trailing slash so a root install renders clean
MEMORY_ROOT=memory
# DISCIPLINES is a CLOSED ENUM of stream values, not a directory list (kit 1.5). The tree is flat.
DISCIPLINES="architecture deployment blocks design performance"   # demo defaults; a real .memory-tree.conf overrides these
FAMILIES="architecture:ARCH deployment:DEPLOY blocks:BLOCK design:DES performance:PERF"
FAMILY_of() { local p; for p in $FAMILIES; do case "$p" in "$1:"*) echo "${p#*:}"; return;; esac; done; }

[ "${1:-}" = "--scaffold" ] || { echo "usage: $0 --scaffold"; exit 2; }

# .memory-tree.conf is REQUIRED — never silently scaffold the built-in DEMO disciplines into a real repo.
if [ ! -f "$ROOT/.memory-tree.conf" ]; then
  cp "$HERE/.memory-tree.conf.example" "$ROOT/.memory-tree.conf"
  echo "created .memory-tree.conf from the example — EDIT IT (MEMORY_ROOT, DISCIPLINES, FAMILIES), then re-run." >&2
  exit 1
fi
. "$ROOT/.memory-tree.conf"
M="$MEMORY_ROOT"

# Idempotent converge: a tree already scaffolded by this kit (marker present) is a clean no-op; a
# foreign/half-scaffolded memory/ is refused with a recovery hint; otherwise fall through and scaffold.
if [ -d "$M" ]; then
  if [ -f "$M/HYGIENE.md" ] && grep -q 'gov:kit memory-tree@' "$M/HYGIENE.md"; then
    echo "$M/ already scaffolded by memory-tree — nothing to do."; exit 0
  fi
  echo "$M/ exists without a memory-tree marker — refusing to overwrite. If a prior scaffold crashed, 'rm -rf $M' and re-run; otherwise migrate manually (README: Adopting into an existing tree)." >&2
  exit 1
fi

# `project/` still needs creating even though it now holds only files: the registry printf
# redirects below cannot create their own directory.
mkdir -p "$M/project" "$M/builds" "$M/backlog" "$M/guides"
# root index + rules
# RENDERED, not copied: these two land in the adopter's tree as their committed rule set, so a
# verbatim copy would stamp whatever prefix the SHIPPING repo used into a document the adopter now
# owns. Every kit path in them is a placeholder; `render_doc` is what the parity gate grades.
# >>> render_doc — canonical copy: tools/lib/render-doc.sh (byte-identical; gated)
render_doc() {
  # No `sed`: a substituted value carrying `|` closes the s||| delimiter and `&` re-inserts the
  # whole match. Parameter substitution has neither, PROVIDED the replacement is quoted — bash
  # 5.1 gave an unquoted one the same `&` meaning sed has.
  # The `X` sentinel is because `$( )` strips ALL trailing newlines. `cat` runs in its own
  # subshell with an explicit `exit 1` because the substitution reports the LAST command's
  # status, which is printf's and always 0 — the guard was unreachable without it.
  local out
  out=$( cat "$1" || exit 1; printf X ) || return 1
  out=${out%X}
  out=${out//$'\r'/}
  out=${out//\{\{KIT_DIR\}\}/"$KIT_REL"}
  out=${out//\{\{TOOL_ROOT\}\}/"$TOOL_ROOT"}
  printf '%s' "$out"
}
# <<< render_doc
if [ -f "$HERE/HYGIENE.template.md" ]; then render_doc "$HERE/HYGIENE.template.md" > "$M/HYGIENE.md"; else echo "# ${M}/ retention & hygiene" > "$M/HYGIENE.md"; fi
if [ -f "$HERE/SPEC-TEMPLATE.template.md" ]; then render_doc "$HERE/SPEC-TEMPLATE.template.md" > "$M/TEMPLATE-SPEC.md"; fi
# The build method joins the same rendered set: an adopter that receives the spec format and the
# hygiene rules but not the method for using them has been handed two thirds of one contract.
if [ -f "$HERE/BUILD-METHOD.template.md" ]; then render_doc "$HERE/BUILD-METHOD.template.md" > "$M/guides/BUILD-METHOD.md"; fi
{ echo "# $M/ — project memory index"; echo
  echo "Structured, machine-linted project memory. Shape + rules: [HYGIENE.md](HYGIENE.md)."
  echo "Generated index: [LIVE.md](LIVE.md) + \`ledger/<month>.md\` shards ($KIT_REL/gen_build_index.py)."; echo
  echo "The discipline is a SIGNAL, not a directory. A build folder is named for its slug alone; which"
  echo "discipline it served is declared in each spec's status header as \`streams <value>[+<value>]\`,"
  echo "over the closed enum \`.memory-tree.conf\` declares."; echo
  echo "## Root files"; echo
  echo "- [DECISIONS.md](DECISIONS.md) — append-only decision index, every family, grouped for reading."
  echo "- [TEMPLATE-SPEC.md](TEMPLATE-SPEC.md) — the canonical spec / design-pass format (hygiene check 12)."
  echo "- [HYGIENE.md](HYGIENE.md) — the rule set; the check script is its enforcement."; echo
  echo "## Directories"; echo
  echo "- [builds/](builds/) — one folder per slug: \`README.md\` · \`RUN.md\` (unattended run-state, only while a run is or was live) · \`prompts/\` \`spec/\` \`build/\` \`reviews/\`."
  echo "- [backlog/](backlog/) — one mutable shard per id family."
  echo "- [project/](project/) — the gate's own waiver registries (\`*.txt\`) and nothing else. Read the directory rather than this line: it listed them by name until a seventh landed and the list did not."; echo
  echo "## Streams (the closed enum)"; echo
  echo "| Value | Family |"; echo "|---|---|"
  for d in $DISCIPLINES; do echo "| \`$d\` | \`$(FAMILY_of "$d")\` |"; done
} > "$M/README.md"
# ONE append-only decision log, every family, grouped for reading.
{ printf '# decisions — index

'
  printf '> One line per decision, APPEND-ONLY, every family in one file. Detail in `decisions/`.
'
  printf '> Grouped by family for reading; the file is never re-sorted and a landed row is never edited.
'
  for d in $DISCIPLINES; do printf '
## %s — %s

*(none yet)*
' "$(FAMILY_of "$d")" "$d"; done
} > "$M/DECISIONS.md"
# project/ — the gate's OWN waiver registries and nothing else. EVERY registry any gate reads is
# written here: several are NAMED by gates (corpus_ids.py's checks 14 and 15, check-arms.py,
# gen_build_index.py) and were created by nothing, so an adopter met them as a missing file rather
# than as an empty ratchet. Most gates read "absent" and "present and empty" identically, which is
# what makes an omission invisible — and where one does NOT, as the index generator does not, the
# omission is worse: it refuses, and the tree never scaffolds.
#
# THE COUNT USED TO BE WRITTEN HERE ("ALL SIX") AND IT WENT STALE THE MOMENT A SEVENTH LANDED,
# which is how `stale-header-waiver.txt` shipped missing. A number beside the thing it counts is
# wrong on the next commit and nobody notices; the list below is the count.
printf '# legacy-files.txt — recording files kept under historical names (permanent C5 exemption). Empty = strict.
' > "$M/project/legacy-files.txt"
printf '# curation-debt.txt — index files pending slimming (exempt from checks 6/7/8 while listed). Empty = fully strict.
' > "$M/project/curation-debt.txt"
printf '# id-orphan-waiver.txt — ids cited but never defined, deliberately (check 14). One id per line.
# Shrink-only against ORPHAN_ID_PIN; a waived id that now resolves is a stale row and reds.
' > "$M/project/id-orphan-waiver.txt"
printf '# corpus-path-unresolved.txt — rooted repo-path citations in the present-tense corpus that
# resolve to nothing (check 15). One row per (citing-file, cited-path), TAB-separated:
#   <citing-file>\t<cited-path>\t<occurrences>\t<absent|moved:DEST>
# Shrink-only against DEAD_PATH_PIN. Empty = every citation resolves.
' > "$M/project/corpus-path-unresolved.txt"
printf '# unarmed-branches.txt — `fail` branches with no positive assertion naming their own failure
# text (check-arms.py). Fields: gate<TAB>check<TAB>ordinal<TAB>signature.
# SHRINK-ONLY, and EMPTY is the working state: a row appears only when a new branch lands that no
# fixture can reach, and it carries the REASON — "not yet written" and "cannot be written from here"
# are indistinguishable in a bare pin and only one of them is acceptable.
' > "$M/project/unarmed-branches.txt"
# build-readme-slot-limits.txt ships with its ROWS and without the origin repo's VALUES. A ceiling
# measured against one corpus is a pin the adopter never measured, which is vacuous or permanently
# red — the same reasoning as the measured-pins hole, and the reason `slot-budget-ceilings` exists
# beside it. A row with no value is the ANNOUNCED unarmed state; a MISSING row is a refusal, so the
# rows survive and only the numbers go.
#
# GUARDED ON THE KIT LIVING INSIDE $ROOT, and that guard is the whole correction. The first cut wrote
# to "$HERE" unconditionally — the only write in this script landing outside $ROOT, against the
# invariant its own header states — so running the scaffolder FROM a governance checkout blanked that
# checkout's ceilings rather than an adopter's copy. It did exactly that here: five values were lost
# in a landed commit, and the bar kept printing "slot contract clean" because a blank ceiling is the
# legal unarmed state. The kit's own self-test re-triggered it on every run.
#
# Inside $ROOT the kit IS the adopter's copy and stripping it is the intended install step. Outside
# $ROOT it is somebody's source tree and must not be touched; that is the same case the KIT_REL
# branch above already detects and prints about.
case "$KIT_INSIDE" in
  yes)
    if [ -f "$HERE/build-readme-slot-limits.txt" ]; then
      awk -F'\t' 'BEGIN{OFS="\t"} /^## /{ print $1, ""; next } { print }' \
        "$HERE/build-readme-slot-limits.txt" > "$HERE/.slot-limits.tmp" \
        && mv "$HERE/.slot-limits.tmp" "$HERE/build-readme-slot-limits.txt"
    fi
    ;;
  *)
    echo "memory-tree: kit dir is outside the tree being scaffolded — leaving its \
build-readme-slot-limits.txt alone. The ceilings are stripped when the kit is copied INTO the target \
tree and the adopter runs it from there, which is the runbook order." >&2
    ;;
esac

# readme-contract.txt is SEEDED with every build README EXEMPT and none bound, because an absent
# registry is a refusal and an empty one reds the adopter's first run on the FORWARD assertion.
# Every row carries its reason inline and the pin equals the count, so the file the adopter receives
# already satisfies both directions and the equality.
#
# EVERY PROBE HERE IS TERMINATED. A no-match `grep` exits 1, and under `set -eu` that aborts the whole
# scaffold silently — which is exactly what happened: this block landed unterminated, the script died
# before rendering LIVE.md, and the adopter self-test caught it as a broken relative link rather than
# as a dead scaffolder. The charter names this class; the fix is `|| true`, not a cleverer pipeline.
_rc=$({ git ls-files 2>/dev/null || true; find . -type f -not -path './.git/*' 2>/dev/null | sed 's|^\./||' || true; } \
      | sort -u | grep -E "^$M/builds/[^/]+/README\.md$" || true)
_rn=$(printf '%s\n' "$_rc" | grep -c . || true)
{
  printf '# readme-contract.txt - which build READMEs the heading canon and the slot budgets BIND.\n'
  printf '# Asserted BOTH ways: a tracked build README named by no row refuses, and a row naming a\n'
  printf '# path that is not one refuses. A bare path is BOUND; an `!`-prefixed path is EXEMPT and\n'
  printf '# carries its reason after " - ". `exempt-pin:` is an EQUALITY with the measured count.\n'
  printf '# SEEDED at adoption: every build README present starts EXEMPT, so the contract binds\n'
  printf '# nothing on day one and the leg says so on every run. Convert a row to bound when you\n'
  printf '# conform that README.\n\n'
  printf 'exempt-pin: %s\n\n' "$_rn"
  printf '%s\n' "$_rc" | grep . | while IFS= read -r f; do
    printf '!%s - predates the contract in this tree; drains when its build is conformed\n' "$f"
  done || true
} > "$M/project/readme-contract.txt"

# method-carriers.txt is SEEDED, not written empty, and that is the whole point. The kit itself ships
# files that POINT AT the build method — this adopter is one, the kit README is another — so an
# adopter handed an empty registry reds on install with carriers they never wrote. The seed is
# measured from THEIR tree with the same predicate the leg uses, so gov's paths never travel.
{
  printf '# method-carriers.txt - every file outside %s/ that POINTS AT guides/BUILD-METHOD.md.\n' "$M"
  printf '# One "<path> . <why>" row each; the why is what a future author reads when deciding whether\n'
  printf '# their new carrier is the next pointer or the first summary. Keyed on PATH alone, never\n'
  printf '# <path>:<line> - that keying is what unpinned install-prefix-waivers.txt.\n'
  printf '# SEEDED at adoption from this tree: every row below was measured, not assumed.\n\n'
  # The runbook order is `cp -r` then `--scaffold` then commit, so `git ls-files` is EMPTY here and
  # a tracked-only seed writes a header and nothing else — after which the adopter's first run reds
  # on carriers they never wrote. Fall back to the working tree, which is what actually exists at
  # scaffold time. This is the vacuous-selector-empty-population class, met inside the block whose
  # own comment claims to prevent it.
  { git ls-files 2>/dev/null; find . -type f -not -path './.git/*' 2>/dev/null | sed 's|^\./||'; } \
    | sort -u | while IFS= read -r f; do
    case "$f" in
      "$M"/*) continue ;;
      "$KIT_REL"/BUILD-METHOD.template.md) continue ;;
      "$KIT_REL"/check-method-carriers.sh) continue ;;
      *.test.sh) continue ;;
    esac
    if grep -qF 'BUILD-METHOD.md' "$f" 2>/dev/null; then
      printf '%s \xc2\xb7 declared at adoption; replace this with why it points at the method\n' "$f"
    fi
  done
} > "$M/project/method-carriers.txt"

# stale-header-waiver.txt — SEEDED WITH ITS HEADER AND NO ROWS, and it must exist or the tree does
# not scaffold at all. `gen_build_index.py` REFUSES a missing one by design ("a file nobody created
# is a decision nobody made"), and the memory-tree descriptor already tells every adopter that this
# file ships with them — but nothing wrote it here, so `--scaffold` produced a tree whose very first
# index render died. Caught by the closing bar of TOOL-dRetiredFork-17: the memory-hygiene self-test
# is GREEN at the merge-base and red at HEAD, on the arm asserting a freshly scaffolded tree is
# clean. A descriptor claiming a file ships and an adopter that does not write it are two answers to
# one question, and this was the copy that was wrong.
printf '# stale-header-waiver.txt — build README headers the index generator may leave stale.
# EMPTY IS THE EXPECTED STATE: the rows a tree needs are the headers that actually rotted in THAT
# tree, so a list measured on another corpus is vacuous here. The file must EXIST even so — the
# generator refuses a missing one, because a file nobody created is a decision nobody made.
' > "$M/project/stale-header-waiver.txt"
# one mutable backlog shard per FAMILY
for d in $DISCIPLINES; do
  fam=$(FAMILY_of "$d")
  printf '# %s backlog (%s)

> Mutable. Each row leads with one status token (OPEN…WONTDO).
' "$fam" "$d" > "$M/backlog/$fam.md"
done
# builds/ starts empty; a .gitkeep would be an unsanctioned entry under check 3, so the first build
# is what makes the directory tracked. The empty-population guard says so out loud on the first run.
# Stage the tree FIRST so the generator (git ls-files) sees the files, then render + re-stage.
git add "$M" >/dev/null 2>&1 || true
# The resolver, INLINE. This kit is copy-installed as a standalone directory, so `../lib/` does
# not exist in an adopting repo. The block below is byte-identical to tools/lib/resolve-python.sh
# and tools/lib/resolve-python.test.sh reds if any copy drifts.
# >>> resolve_python — canonical copy: tools/lib/resolve-python.sh (byte-identical; gated)
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
_PY=$(resolve_python) || exit 2
"$_PY" "$HERE/gen_build_index.py" --write
git add "$M" >/dev/null 2>&1 || true

echo "Scaffolded $M/ ($(echo $DISCIPLINES | wc -w) disciplines) — staged."
echo "Next:"
echo "  1. git add $M/ .memory-tree.conf && commit."
echo "  2. Wire the gate: add 'bash $KIT_REL/check-memory-hygiene.sh' to CI + your local gate runner;"
echo "     add a pre-commit fast leg calling it with --staged on staged $M/** paths."
echo "  3. Verify: bash $KIT_REL/check-memory-hygiene.sh ; echo \$?   (expect 0)"
echo "  4. Arm the spec-format ratchet: set SPEC_FORMAT_CUTOFF=<today> in .memory-tree.conf"
echo "     (every spec dated >= it must follow $M/TEMPLATE-SPEC.md — hygiene check 12)."
echo "  5. Arm the streams ratchet: set STREAMS_CUTOFF in .memory-tree.conf STRICTLY AHEAD of every"
echo "     committed spec's filename date, so no landed spec is retroactively red. Every spec written"
echo "     from that date on must carry '· streams <value>' in its status header."
echo "  6. Arm the acceptance-witness ratchet: set SPEC_WITNESS_CUTOFF in .memory-tree.conf, also"
echo "     STRICTLY AHEAD of every committed spec. From that date on, every acceptance bullet must"
echo "     name a witness in backticks — the command, file or test that makes the observation."
echo "  7. MEASURE any pin/floor this kit gains against YOUR corpus — never inherit another repo's"
echo "     numbers. A pin copied from a larger tree is either vacuous or permanently red here."
echo "  8. Bind your records (hygiene check 21). If $M/builds/*/{build,prompts,reviews}/ already"
echo "     holds records, THE FIRST RUN IS RED: check 21 names every record carrying no Serves line,"
echo "     and no pin value changes that — RECORD_UNBOUND_PIN bounds the deliberate 'none' escape,"
echo "     never the absent line. Migrate in this ORDER:"
echo "       a. See what is unbound:  $_PY $KIT_REL/gen_build_index.py --print-bindings"
echo "          (read-only, writes nothing, always exits 0; 'A' rows are the work)"
echo "       b. One mechanical pass: add '**Serves:** none — <why>' to each. No judgement about what"
echo "          any document was about, so it is not a retrofit — and not a cutoff either: nothing"
echo "          is exempted by date and every record stays visible."
echo "       c. THEN measure: set RECORD_UNBOUND_PIN to the 'N' count that pass leaves."
echo "       d. Drain it as you bind records for real: '**Serves:** <kind> <id> [<id>…]', kinds"
echo "          spec-audit | diff-review | journal | research. Grammar: $M/HYGIENE.md, Record bindings."
