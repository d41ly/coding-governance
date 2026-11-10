#!/usr/bin/env bash
# adopt-playbook.sh — render the governance charter into a target, and verify it later.
#
#   bash <prefix>/playbook/adopt-playbook.sh --target <repo>            # write the region
#   bash <prefix>/playbook/adopt-playbook.sh --target <repo> --check    # assert it still matches
#   bash <prefix>/playbook/adopt-playbook.sh --selftest                 # the engine's own arms
#
# This is the shape every other adopter in this repo has, which is why the playbook entry no longer
# carries a `why_no_adopter` reason: installation stopped being a copy an operator finishes by hand.
#
# `--check` asserts TWO things with SEPARATE messages, because they are two questions: that the
# rendered region still equals a fresh render, and that no placeholder survived it. A target whose
# descriptor declares nothing for a key renders a region that is perfectly in sync and still tells
# the agent to invoke a placeholder's name.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)

# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  # THE FLOOR is declared once, in python-floor.txt in gov's lib dir. The literal below is its
  # generated copy, held equal to it by the floor module's `check` and by these blocks' parity rows,
  # because a copy-installed kit has no lib dir to read. A candidate that runs below it is passed
  # over and named, exactly as a candidate that does not run.
  _rp_floor="3.15"
  _rp_fv=$(( ${_rp_floor%%.*} * 1000 + ${_rp_floor#*.} ))
  _rp_tried=""; _rp_seen=""; _rp_best=""; _rp_bv=0; _rp_bver=""; _rp_o1=""; _rp_og=""; _rp_i=0
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    _rp_i=$((_rp_i + 1))
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    # ONE spawn per candidate, isolated: its major.minor and its own executable, forward-slashed,
    # because a backslashed C:\ path handed to MSYS bash loses its separators.
    _rp_out=$("$_rp_c" -I -c 'import sys; print("%d.%d" % sys.version_info[:2], sys.executable.replace("\\", "/"))' 2>/dev/null) || _rp_out=""
    _rp_out=${_rp_out%$'\r'}
    if [[ ${_rp_out%% *} =~ ^([0-9]+)\.([0-9]+)$ ]]; then
      _rp_cv=$(( 10#${BASH_REMATCH[1]} * 1000 + 10#${BASH_REMATCH[2]} ))
      if [ "$_rp_cv" -ge "$_rp_fv" ]; then
        # An override, the caller's or GOV_PYTHON, names the command a consumer spawns, a wrapper
        # or a venv launcher included, and is echoed as given. Only the three launcher names give
        # way to the direct executable where the probe named a file; the launcher's own name
        # otherwise. The `[ -f ]` HOLDS on a Windows App Execution Alias, so a Store Python whose
        # own sys.executable is an alias is echoed as printed: a gap the run-gates kit's
        # check_app_alias closes for the legs it measures, and this block does not.
        _rp_exe=${_rp_out#* }
        if [ "$_rp_i" -gt 2 ] && [ "$_rp_exe" != "$_rp_out" ] && [ -f "$_rp_exe" ]; then printf '%s\n' "$_rp_exe"; else printf '%s\n' "$_rp_c"; fi
        return 0
      fi
      _rp_why="ran ${_rp_out%% *}, below the floor $_rp_floor"
      if [ "$_rp_cv" -gt "$_rp_bv" ]; then _rp_best=$_rp_c; _rp_bv=$_rp_cv; _rp_bver=${_rp_out%% *}; fi
    else
      _rp_why="did not run"
    fi
    _rp_seen="${_rp_seen}resolve_python:   $_rp_c: $_rp_why"$'\n'
    [ "$_rp_i" != 1 ] || _rp_o1=$_rp_why
    [ "$_rp_i" != 2 ] || _rp_og=$_rp_why
  done
  {
    echo "resolve_python: no usable python launcher at the floor $_rp_floor (python-floor.txt in gov's lib dir)."
    echo "resolve_python: Each candidate was RUN with -I -c — being on PATH is not evidence (the Microsoft Store"
    echo "resolve_python: python3 stub answers \`command -v\` and exits 9009 without running anything)."
    printf '%s' "$_rp_seen"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and $_rp_o1."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and $_rp_og. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
    # THE INSTALL COMMAND, as platforms.provision says. The policy kit's own reader answers it at the
    # landed revision, run by the newest candidate that ran, since its tomllib needs 3.11, and never
    # through the policy shim, which resolves a launcher itself and would re-enter this refusal.
    _rp_prov=name; _rp_pwhy=""
    if [ -z "$_rp_best" ]; then
      _rp_pwhy="no reader ran, because no candidate ran"
    elif [ "$_rp_bv" -lt 3011 ]; then
      _rp_pwhy="no reader ran, because the newest candidate that ran, $_rp_best, is $_rp_bver, below the 3.11 the reader needs"
    else
      IFS= read -r -d '' _rp_rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
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
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
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
      case "${BASH_SOURCE[0]:-}" in */*) _rp_here=${BASH_SOURCE[0]%/*} ;; *) _rp_here=. ;; esac
      _rp_kit=$("$_rp_best" -I -c "${_rp_rkd%$'\n'}"'
import sys
try:
    print(resolve_kit_dir("policy", "policy.py", sys.argv[1]).as_posix())
except LookupError as e:
    sys.exit(str(e))' "$_rp_here" 2>&1) || _rp_pwhy="no reader ran, because ${_rp_kit%$'\r'}"
      if [ -z "$_rp_pwhy" ]; then
        _rp_kit=${_rp_kit%$'\r'}
        _rp_val=$("$_rp_best" "$_rp_kit/policy.py" get platforms.provision 2>/dev/null) || _rp_pwhy="the reader, policy.py get, exited $?"
        _rp_val=${_rp_val%$'\r'}
        case "$_rp_pwhy:$_rp_val" in
          :name|:uv|:off) _rp_prov=$_rp_val ;;
          :*) _rp_pwhy="the reader, policy.py get, printed '$_rp_val', which is no value of the key" ;;
        esac
      fi
    fi
    [ -z "$_rp_pwhy" ] || echo "resolve_python: platforms.provision reads its catalogue default, name: $_rp_pwhy."
    if [ "$_rp_prov" = uv ]; then
      if [ ! -t 2 ]; then _rp_no="not offered, because stderr is not a terminal"
      elif ! uv --version >/dev/null 2>&1; then _rp_no="not offered, because uv does not run"
      else
        printf 'resolve_python: platforms.provision is uv. Run `uv python install %s` now? [y/N] ' "$_rp_floor"
        _rp_a=""; read -r _rp_a </dev/tty || :
        if [ "$_rp_a" = y ]; then
          uv python install "$_rp_floor" || :
          echo "resolve_python: re-run once the floor is on PATH, or name it in GOV_PYTHON."
          _rp_prov=offered
        else
          _rp_no="declined at the prompt"
        fi
      fi
      [ "$_rp_prov" = offered ] || echo "resolve_python: platforms.provision is uv, and the install was $_rp_no."
    fi
    case "$_rp_prov" in
      off) echo "resolve_python: platforms.provision is off, so this refusal names no install command." ;;
      name|uv)
        echo "resolve_python: install the floor with: uv python install $_rp_floor"
        case "${OSTYPE:-}" in msys*|cygwin*|win*) echo "resolve_python: or, on Windows: py install $_rp_floor" ;; esac ;;
    esac
    # LAST, verbatim: the first line names the refusal and this one the candidates, and the lines
    # between them carry the outcomes, the overrides and the install (TOOL-dSafePassage-26 S20).
    echo "resolve_python: tried:$_rp_tried"
  } >&2
  return 1
}
# <<< resolve_python

PY_BIN=$(resolve_python "${PLAYBOOK_PY:-}") || exit 2

# The verbs this shim accepts, spelled here rather than only in the engine, so a reader of the
# adopter can see that `--check` exists without opening the Python. The engine parses argv itself;
# this case is a declaration, not a second parser.
case " $* " in
  *" --selftest "*) : ;;   # the engine's arms, over its own temp fixtures — no target is read
  *" --check "*)    : ;;   # the charter scope's compare: the region matches a fresh render, none survived
  *" --check-render "*) : ;;  # with --scope, one scope's compare; bare, the render gate over every scope
  *" --render-scope "*) : ;;  # write one scope: charter, or entry-files
  *)                : ;;   # write the region
esac

case " $* " in
  *" --selftest "*) ;;
  *) exec "$PY_BIN" "$HERE/render_playbook.py" "$@" ;;
esac
"$PY_BIN" "$HERE/render_playbook.py" "$@" || exit $?

# THE LAYER CHECK'S ARMS (PLAY-dOrderedCharter-16 S9). Each row plants one case into the check's own
# scratch tree, `<plant>|<exit>|<a line it must print>`; the exit and the named line are asserted
# together, so a check turned into a printer reds here. `none` is the control, green with no edge.
_lf=0
while IFS='|' read -r _lp _lrc _lwant; do
  [ -n "$_lp" ] || continue
  # shellcheck disable=SC2086  # the plant field carries its own flags, word-split on purpose
  _lout=$("$PY_BIN" "$HERE/check_layers.py" --fixture $( [ "$_lp" = none ] || echo "--plant $_lp" ) 2>&1); _lgot=$?
  case "$_lgot:$_lout" in
    "$_lrc:"*"$_lwant"*) printf 'arm ok    layers plant %s\n' "$_lp" ;;
    *) _lf=$((_lf+1)); printf 'arm FAIL  layers plant %s — wanted rc=%s + %s, got rc=%s\n' "$_lp" "$_lrc" "$_lwant" "$_lgot"
       printf '      %s\n' "${_lout//$'\n'/$'\n'      }" ;;
  esac
done <<'PLANTS'
none|0|0 allowed, 0 red; 0 contract red(s)
import|1|tools/corekit/core.py:9 · import · core kit corekit depends on non-core kit mapkit
dynamic|1|tools/corekit/core.py:10 · dynamic · core kit corekit depends on non-core kit mapkit
dynamic|1|tools/corekit/core.py:11 · dynamic · core kit corekit depends on non-core kit mapkit
probe|1|tools/corekit/core.py:9 · probe · core kit corekit depends on non-core kit mapkit
copy|1|tools/corekit/core.py:10 · copy · core kit corekit depends on non-core kit mapkit
shell|1|tools/corekit/run.sh:4 · shell · core kit corekit depends on non-core kit expkit
requires-if|1|tools/corekit/kit.toml:4 · requires-if · core kit corekit depends on non-core kit expkit
unslotted|1|tools/corekit/core.py:7 · import · core kit corekit depends on non-core kit mapkit
slotted --list|0|layers: edge tools/corekit/core.py:7 · import · corekit -> mapkit · allowed
flat-slotted --list|0|layers: edge tools/flatgo:2 · shell · flatkit -> expkit · allowed
flat-literal|1|optional row part 'tools/flatgo' spells the tool root literally: spell it {prefix}/flatgo
ex1-pair|1|row 'layer.exp' uses point.exp.hook, which 'layer.exp2' declares
no-layer|1|descriptor tools/mapkit/kit.toml declares no layer
unknown-layer|1|descriptor tools/mapkit/kit.toml names layer 'layer.nowhere', which no row holds
undeclared-point|1|row 'layer.exp' uses point.core.missing, which 0 core row(s) declare
quoted|1|tools/corekit/run.sh:6 · probe · core kit corekit depends on non-core kit expkit
quoted|1|0 allowed, 1 red;
unshipped|1|tools/corekit/core.py:9 · probe · core kit corekit depends on non-core kit mapkit
unshipped|1|0 allowed, 1 red;
unparsable|2|layers: UNREADABLE tools/corekit/core.py (SyntaxError
PLANTS
if [ "$_lf" != 0 ]; then echo "FAIL — $_lf layer-check arm(s) failed"; exit 1; fi
echo "PASS — the layer check's plants"

# THE TAG RESOLVER'S ARMS (PLAY-dOrderedCharter-19 S13, S14). Each row runs `gov_tag.py --fixture` over one
# plant in its own scratch repository, `<plant and --set flags>|<exit>|<a line it must print>|<a line it
# must not print>`, the last field optional; exit and lines are asserted together. Every policy key a plant
# reads is `--set`, so no row reads a policy file. The two `unclosed-` rows are PLAY-dOrderedCharter-68's: a
# fence that never closes is red on a live page and printed on a frozen record. The rows from `bad-ns` on are
# PLAY-dOrderedCharter-10's nine plants, the shape check and the joins; `dead-selector` and `file-name` print their second half's
# exit on a `rc=` line, read here as a line. PLAY-dOrderedCharter-75's `unscoped-unit`, beside them, leaves
# the `reader` join unarmed under a unit row with no `scope`. Then four are PLAY-dOrderedCharter-44's: the index's
# freshness keyed on blob, extractor and version, and its schema stamp. Then three rows are
# PLAY-dOrderedCharter-51's two plants: two worktrees whose extractor bytes differ keep their rows apart,
# re-parse nothing on a second alternating round, and `--gc` collects the pruned one's version; a worktree
# is never served another version's rows of a tree already built. The rows after them are
# PLAY-dOrderedCharter-22's `purpose` arm: the namespace rows' `owner` and `purpose-source`, and the chain
# registry joined to the fixture design's view; `pending-source` and `new-no-purpose` print their second
# half's exit on a `rc=` line. Then PLAY-dOrderedCharter-69's `git-env`: the `two-versions` and the edge
# grammar's `resolve-tag` fixtures, run as children under an exported `GIT_DIR`, touch only their scratch. The
# last six rows are PLAY-dOrderedCharter-70's: a TOML row placed on its own `tag =` line, a staged rename
# serving the new name alone, and a charter moved by a committed and by an uncommitted conf edit.
# run_plant_rows <label> <script>: one `<plant and flags>|<exit>|<must print>|<must not print>` row per stdin
# line, each run as `<script> --fixture --plant <plant and flags>`; every failed row adds one to `_tf`.
run_plant_rows() {
  while IFS='|' read -r _tp _trc _twant _tnot; do
    [ -n "$_tp" ] || continue
    # shellcheck disable=SC2086  # the plant field carries its own flags, word-split on purpose
    _tout=$("$PY_BIN" "$2" --fixture --plant $_tp 2>&1); _tgot=$?
    case "$_tgot:$_tout" in
      "$_trc:"*"$_twant"*)
        case "$_tout" in
          *"${_tnot:-<none>}"*) _tf=$((_tf+1)); printf 'arm FAIL  %s plant %s — printed %s\n' "$1" "$_tp" "$_tnot" ;;
          *) printf 'arm ok    %s plant %s\n' "$1" "$_tp" ;;
        esac ;;
      *) _tf=$((_tf+1)); printf 'arm FAIL  %s plant %s — wanted rc=%s + %s, got rc=%s\n' "$1" "$_tp" "$_trc" "$_twant" "$_tgot"
         printf '      %s\n' "${_tout//$'\n'/$'\n'      }" ;;
    esac
  done
}
_tk="--set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new"
_tf=0
run_plant_rows tags "$HERE/gov_tag.py" <<PLANTS
none $_tk|0|tags: green · 0 red
rebuild|0|dumps equal
two-paths|0|incremental rows equal a cold build's
dirty|0|both worktrees share one index|SERVES ANOTHER'S
one-commit|0|built, 1 blob parsed
slice --set tags.slice=leaf|0|tags: layer.memory · tools/corekit/core.tags:3|layer.memory.recall
slice --set tags.slice=subtree|0|tags: layer.memory.recall · tools/corekit/core.tags:4
retired $_tk|1|new text cites retired practice.old
retired --set tags.retired-cites=warn --set tags.bare-refs=charter-only|0|tags: WARN memory/guides/ALPHA.md:11 · new text cites retired practice.old
retired --set tags.retired-cites=allow --set tags.bare-refs=charter-only|0|tags: green · 0 red|cites retired
retired-old $_tk|0|tags: green · 0 red
retired-reminted $_tk|1|retired name minted again · practice.old
retired-reminted --set tags.retired-cites=warn --set tags.bare-refs=charter-only|1|retired name minted again · practice.old
retired-reminted --set tags.retired-cites=allow --set tags.bare-refs=charter-only|1|retired name minted again · practice.old
bare $_tk|0|bare \`land\` -> practice.land
bare --set tags.bare-refs=unique --set tags.retired-cites=refuse-new|1|bare \`memory\` is ambiguous: layer.memory and practice.memory
bare --set tags.bare-refs=never --set tags.retired-cites=refuse-new|1|bare \`land\` outside the charter
bare-charter --set tags.bare-refs=never --set tags.retired-cites=refuse-new|0|tags: green · 0 red
owned $_tk|1|kit expkit (layer.exp) mints layer.fixture-x in core namespace layer
owned-core $_tk|0|tags: green · 0 red
scope $_tk|0|tags: unarmed unit (1 not graded)|· unresolved ·
scope-guide $_tk|1|memory/guides/ALPHA.md:13 · unresolved · \`doc.nope\` names no row
unclosed-fence $_tk|1|· unclosed fence ·|unresolved
unclosed-record $_tk|0|unclosed fence, frozen record, printed
bad-ns $_tk|1|· shape · step.build · namespace 'step' is not registered
bad-seg $_tk|1|· shape · layer.Memory · segment 'Memory' is outside
long-tag $_tk|1|· over 64 bytes (66)
ns-word $_tk|1|· shape · practice.repo.x · first segment 'repo' is a namespace word
none $_tk|0|tags: green · 0 red|namespace word
escaped-word $_tk|1|namespace row 'a.b' is outside seg, so no tag is graded against it
escaped-word $_tk|1|· shape · a.b.c · namespace 'a' is not registered
unregistered-cite $_tk|1|\`layer.nowhere\` is cited and undeclared in layer
dead-selector $_tk|1|\`reader.ghost\` is declared and selects no unit
dead-selector $_tk|1|unused, a descriptor (not red): layer.memory layer.memory.lexicon
dead-selector $_tk|1|without reader.ghost: rc=0
unscoped-unit $_tk|0|tags: join reader · selects · unarmed|is declared and selects no unit
empty-ns $_tk|0|tags: join kind · unarmed|\`kind.x\`
file-name $_tk|0|1 file names not graded
file-name $_tk|0|· unresolved · \`kit.toml\` names no row
file-name $_tk|0|no tracked kit.toml: rc=1
new-extractor|0|incremental rows equal a cold build's|old blobs: 0
extractor-edit|0|the others ran 0 times, 4 skipped as fresh; 0 rows of the old version
tagless|0|1 blob parsed after one file changed, 0 on a build with no change
schema|0|tag-index — rebuilt: schema 0 to
two-versions|0|round 2 parsed 0 and 0 blobs; 2 versions of fixture_tags:extract_declared held side by side|DIFFER
two-versions|0|--gc left 0 rows of its version; the live dump unchanged
served-across|0|served 0 rows of one's version, and one serves 1
none $_tk|0|tags: purpose · no chain to read
no-owner $_tk|2|namespace row 1 lacks owner
ghost-owner $_tk|1|namespace 'doc' · owner 'dGhost' names no build of memory/project/chain.toml
no-purpose-source $_tk|2|namespace row 1 lacks purpose-source
bad-purpose-source $_tk|1|namespace 'doc' · purpose-source 'AGENTS.md#practices' reads a field in a .md file
member-no-field $_tk|1|namespace 'doc' · member doc.beta (memory/guides/BETA.md) lacks h1
pending-source $_tk|0|tags: purpose · pending reader · {prefix}/playbook/readers.toml#why
pending-source $_tk|0|members, 3 path-only, pending 1
pending-source $_tk|0|/readers.toml) lacks why
pending-source $_tk|0|readers.toml landed with a member lacking why: rc=1
registry-ghost $_tk|1|registry row 'dGhost' names no build of the design view
registry-missing $_tk|1|chain build 'dFixtureTwo' of the design view has no registry row
registry-joined $_tk|0|2 registry rows joined to 2 view builds, 2 rows awaiting PM-5's review
new-no-purpose $_tk|1|registry row 'dFixtureNew' carries no purpose, and no baseline [chain] row names it
new-no-purpose $_tk|1|with a purpose: rc=0
git-env|0|tags: plant git-env · both children green, core.bare false, the outer index unchanged
toml-row|0|tags: plant toml-row · rows [('practice.a', 'tag', 4, 5), ('practice.b', 'tag', 8, 9)] on their own lines
dirty-rename|0|doc.alpha resolves to [] and doc.beta to ['memory/guides/BETA.md']
charter-warm|0|incremental rows equal a cold build's
charter-warm|0|doc.charter resolves to ['CHARTER2.md']
charter-dirty|0|incremental rows equal a cold build's
charter-dirty|0|doc.charter resolves to ['CHARTER2.md']
reference-row $_tk|0|h1 = "The fixture's reference page"|lacks h1
reference-row $_tk|0|show: rc=0, check: rc=0
reference-no-h1 $_tk|1|member doc.reference.fixture (|resolves to no row
reference-no-h1 $_tk|1|/references.toml) lacks h1
PLANTS
if [ "$_tf" != 0 ]; then echo "FAIL — $_tf tag-resolver arm(s) failed"; exit 1; fi
echo "PASS — the tag resolver's plants"

# THE EDGE GRAMMAR'S ARMS (PLAY-dOrderedCharter-24 §4). Each row runs `edge_grammar.py --fixture` over one
# plant, the same row shape as the tag resolver's: the two-line block and a fenced line green, each
# malformed plant naming both its bad lines in one refusal, the closed set's reds, and a selector a fixture
# registry adds admitted with `edges.toml` unchanged. The rows from `promoted-elsewhere` on are
# PLAY-dOrderedCharter-28's §4 plants: the one-writer type, the pin reds, and each address form resolved
# over a scratch repository whose unit and clause texts moved under a second commit, beside the malformed
# section, block and note refs segment.
_tf=0
run_plant_rows edges "$HERE/edge_grammar.py" <<'PLANTS'
good-block|0|edges: site.md:6 · tests · kit.y, kit.z
good-block|0|edges: inverse · feature.x implemented-by site.md:5
good-block|0|edges: inverse · kit.z tested-by site.md:6
good-block|0|edges: green · 2 edge(s)
fenced-edge|0|edges: green · 0 edge(s)|site.md:4
space-target|1|site.md:1: `**Edges:** tests=kit.y kit.z` holds the target 'kit.y kit.z', and a target holds no space; the grammar is
space-target|1|site.md:3: `**Edges:** tests=kit.y, kit.z` holds the target ' kit.z'
comma-in-pair|1|site.md:1: `**Edges:** tests,implements=kit.y` names the type 'tests,implements'
comma-in-pair|1|site.md:3: `**Edges:** tests=kit.y,,kit.z` holds an empty target
bracket-target|1|site.md:1: `**Edges:** tests=[kit.y]` holds the target '[kit.y]', and a target holds no bracket
bracket-target|1|site.md:3: `**Edges:** tests=kit.y,kit.z]` holds the target 'kit.z]'
two-types-one-line|1|site.md:1: `**Edges:** tests=kit.y tests=kit.z` carries a second `type=` pair
two-types-one-line|1|site.md:3: `**Edges:** implements=kit.y · tests=kit.z` carries a second `type=` pair
no-equals|1|site.md:1: `**Edges:** tests kit.y` holds no `type=` pair
no-equals|1|site.md: 2 edge line(s) refused
unregistered-type|1|edges: site.md:1 · frobs · is no type of edges.toml's closed set
declared-inverse|1|edges: site.md:1 · implemented-by · is the inverse of implements
declared-cites|1|edges: site.md:1 · cites · is derived
outside-to|1|edges: site.md:1 · layer=kit.x · is outside layer's to [layer]
pin-on-none|1|part-of=kit.x@1a2b3c4d · pins a target, and part-of's row says pin = "none"
selector-registered|0|edges: green · 1 edge(s)
selector-registered|0|edges: edges.toml unchanged
selector-describes|1|edges: site.md:1 · instructs=feature.x · is outside instructs's to [selects]
promoted-elsewhere|1|is written by instructions.edit alone, its one writer
pin-no-at|1|holds the target 'practice.land:1a2b3c4d', and a pin is written `@<hash8>`
pin-bad-hash|1|holds the target 'practice.land@1a2b3c', whose pin hash is not eight hex digits
pin-no-text|1|pins 00000000, which matches no text in its unit's history
pin-other-type|1|part-of=kit.x@1a2b3c4d · pins a target, and part-of's row says pin = "none": a pin on a type whose row admits none
resolve-pinned-tag|0|edges: green · 1 edge(s)|matches no text
clause-no-rev|1|pins cl-dAlpha-0001@00000000, which matches no revision of its clause
resolve-pinned-clause|0|edges: resolved · spec.md:3 · carries-clause=cl-dAlpha-0001@|matches no revision
resolve-tag|0|edges: resolved · site.md:1 · layer=layer.memory · layer.memory · tools/corekit/core.tags:3
resolve-section|0|edges: resolved · site.md:1 · part-of=doc.build-method#m5-recall-and-reuse · doc.build-method#m5-recall-and-reuse · memory/guides/BUILD-METHOD.md
resolve-family|0|edges: resolved · site.md:1 · serves=PLAY-dOrderedCharter-28 · family-id PLAY-dOrderedCharter-28 (owner dOrderedCharter)
resolve-clause|0|edges: resolved · site.md:1 · carries-clause=cl-dAlpha-0001 · clause-id cl-dAlpha-0001
bad-section|1|site.md:5: `**Edges:** implements=doc.build-method#` holds the target 'doc.build-method#', a malformed section target
bad-block|1|site.md:5: `**Edges:** tests=kit.y implements=kit.z` carries a second `type=` pair
bad-note-refs|1|site.py:1: `# gov:note layer.memory — x → y refs=a b` refs segment holds the target 'a b'
PLANTS
if [ "$_tf" != 0 ]; then echo "FAIL — $_tf edge-grammar arm(s) failed"; exit 1; fi
echo "PASS — the edge grammar's plants"

# THE LOAD SETS' ARMS (PLAY-dOrderedCharter-11, its New arm line). Each row runs `load_sets.py --fixture` over one plant in
# its own scratch repository, the same row shape: a unit required by the builder and scoped only to the
# skeptic refused under `refuse`, the builder's handoff writing no prompt file, `budgets.enforce`'s `warn`
# leaving that refusal standing, and the gap printed under `warn` and `record`; a unit scoped
# `role.gov-builder` selected only once a `role` row selects, and one scoped `feature.roles` only once a
# `feature` row does, each unregistered part printed `unarmed`; a 40000-byte charter under a 50000 cap
# refused on CODEX_MAX under `warn`; a role block ten bytes past its ceiling warned under `warn` and
# refused under `refuse`. PLAY-dOrderedCharter-27's rows: every role's set lists its `code` slot, a stand-in
# budget prices it, a malformed one and a committed value the catalogue row refuses each refuse naming
# `memory.code-budget`, the derivation and the measure alike, and a code block one byte over the budget warns or refuses while one at it is quiet.
_tf=0
run_plant_rows load-sets "$HERE/load_sets.py" <<'PLANTS'
required-away --checks refuse|1|handoff: no prompt file written
required-away --checks refuse --budgets-enforce warn|1|missing unit.needed · instructions.checks=refuse
required-away --checks warn|0|Missing required unit: unit.needed|refused
required-away --checks record|0|**Load gaps:** role.gov-builder · unit.needed|Missing required unit
role-unregistered|0|role — unarmed — role.*|unit.builder
role-unregistered|0|item — unarmed|unit.skeptic
role-registered|0|  unit.builder|unit.skeptic
feature-unregistered|0|feature — unarmed — feature.*|selected: unit.roles
feature-registered|0|selected: unit.roles|unarmed — feature.*
charter-over --budgets-enforce warn|1|over CODEX_MAX 32768
role-block-over --budgets-enforce warn|0|BUDGET WARN · role.gov-builder
role-block-over --budgets-enforce refuse|1|BUDGET REFUSE · role.gov-builder
code-every-role|0|code slot listed for every role|NO code slot
role-unregistered --code-budget 4k|0|code — slot · budget 4000 · --code-budget 4k
role-unregistered --code-budget 16|1|memory.code-budget is '16', not <n>k
code-refused|1|refused · role.gov-builder · memory.code-budget did not read|budget 16000
code-refused-check|1|refused · memory.code-budget did not read|bytes of
code-over --budgets-enforce warn|0|BUDGET WARN · code ·
code-over --budgets-enforce refuse|1|BUDGET REFUSE · code ·
code-at --budgets-enforce refuse|0|bytes of|BUDGET
PLANTS
if [ "$_tf" != 0 ]; then echo "FAIL — $_tf load-set arm(s) failed"; exit 1; fi
echo "PASS — the load sets' plants"
