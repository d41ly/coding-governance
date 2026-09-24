#!/usr/bin/env bash
# render-doc.sh — the ONE canonical `render_doc`, and the file every inline copy is gated against.
#
# WHAT IT DOES. Substitutes a kit template's placeholders — the two paths, `{{KIT_DIR}}` and
# `{{TOOL_ROOT}}`, and the conf facts `{{READINESS_ROWS}}`, `{{INDEX_CAP_LINES}}` and `{{ENTRY_CAP_UNIT}}`
# — and prints the result. It exists because a document the ADOPTER commits must not carry whatever
# prefix the SHIPPING repo happened to use: `apply` writes gov's bytes verbatim, so a verbatim copy
# of a template stamps gov's own layout into a file the adopter now owns.
#
# WHY IT IS A FILE. There were two spellings of it — one in `adopt-memory-tree.sh` and one in
# `kit-dogfood-parity.test.sh`, whose own comment named itself as the drift class and then left the
# drift in place. A kit that is COPY-INSTALLED as a standalone directory cannot source this file
# (`../lib/` does not exist in the adopting repo), so those scripts carry the block between the
# markers below INLINE, byte-identical, and `resolve-python.test.sh`'s parity table gates every copy
# against this one — the same mechanism, the same marker grammar, one more row.
#
# THE CALLER SUPPLIES `KIT_REL` AND `TOOL_ROOT`, and has sourced `.memory-tree.conf` for the rest.
# Both are the caller's, deliberately: the adopter script derives them from where it was invoked,
# and the parity test derives them from the kit it is grading. `KIT_PATHS` is the caller's too, and
# it is what `derive_kit_paths` below prints: every path the install RECEIPT answers, per row, before
# the parent-derived `TOOL_ROOT` answers the rest. It used to be a grep of the receipt's first
# `"prefix"` in each caller — two copies nothing compared, blind to a per-entry override (closing
# review round 1 L4, TOOL-aRepatriatedFork-10). A block that read them from its own location
# would answer for the wrong tree in one of the two callers, which is how the second spelling was
# born in the first place.
# DEPL-dCarriedReceipt-15 S6.

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
  # Closing review round 1 L4: the paths `derive_kit_paths` RESOLVED for this install go first, one
  # `<placeholder><TAB><path>` line each, so a sibling the receipt re-homes renders where its row
  # puts it; the parent-derived `TOOL_ROOT` then answers only what no line did. CRs go first: a
  # Windows python prints CRLF, and a CR kept in a path lands in the rendered doc.
  local kp kv kpaths=${KIT_PATHS:-}
  while IFS=$'\t' read -r kp kv; do
    [ -z "$kp" ] || out=${out//"$kp"/"$kv"}
  done <<<"${kpaths//$'\r'/}"
  out=${out//\{\{TOOL_ROOT\}\}/"$TOOL_ROOT"}
  # TOOL-aJoinedCanon-9: the §5 row set is DECLARED, not written into the skeleton. The transform
  # sits INSIDE the marked block rather than in the callers, so the parity table already gating this
  # block covers it too — a per-caller transform would be a second duplication nothing compares,
  # because gov's live copy is written by the parity test and an adopter's by the adopter, so the
  # two formatters never meet.
  local rows=${READINESS_ROWS//|/$'
'- }
  out=${out//\{\{READINESS_ROWS\}\}/"- $rows"}
  # TOOL-aRepatriatedFork-10 S5: two conf FACTS, rendered from the conf this tree declares, so an
  # adopter's rule set states its own values rather than the shipping repo's. An undeclared key names
  # the owner of its default instead of retyping a number that lives in the engine's preset block.
  out=${out//\{\{INDEX_CAP_LINES\}\}/"${INDEX_CAP_LINES:-undeclared — the engine default applies}"}
  out=${out//\{\{ENTRY_CAP_UNIT\}\}/"${ENTRY_CAP_UNIT:-undeclared — the engine default applies}"}
  printf '%s' "$out"
}
# <<< render_doc

# >>> derive_kit_paths — canonical copy: render-doc.sh in gov's lib dir (byte-identical; gated)
# `derive_kit_paths <python> <kit dir> <template>...` prints the KIT_PATHS `render_doc` applies: one
# `{{TOOL_ROOT}}<home>/<file><TAB><path>` line per such citation in the templates that this install
# RESOLVES through `resolve_kit_dir`, receipt row first, so a per-entry `prefix` or `kit` override
# is honoured where govkit records it, per row. Then one bare `{{TOOL_ROOT}}<TAB><prefix>/` line when
# the receipt carries a top-level `prefix`, read as JSON and never grepped, because a FLAT install's
# kit directory has an empty parent (TOOL-aRepatriatedFork-10 S6). A citation nothing resolves gets
# no line and falls through to that prefix, or to the caller's parent-derived `TOOL_ROOT`.
derive_kit_paths() {
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
    here = pathlib.Path(here).resolve()
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
        hit = (root / str(row["path"])).resolve()
        if hit.is_file() and root in hit.parents:
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
import json
import pathlib
import re
import sys
kit = pathlib.Path(sys.argv[1]).resolve()
root = next((p for p in (kit, *kit.parents) if (p / ".git").exists()), kit)
cites = []
for t in sys.argv[2:]:
    try:
        text = pathlib.Path(t).read_text(encoding="utf-8")
    except OSError:
        continue
    for m in re.finditer(r"\{\{TOOL_ROOT\}\}([\w.-]+)/([\w.-]+)", text):
        if m.group(0) not in cites:
            cites.append(m.group(0))
for cite in cites:
    home, anchor = cite[len("{{TOOL_ROOT}}"):].split("/")
    try:
        path = (resolve_kit_dir(home, anchor, kit) / anchor).relative_to(root)
    except (LookupError, ValueError):
        continue
    print("%s\t%s" % (cite, path.as_posix()))
try:
    pfx = json.loads((root / ".governance" / "install.json").read_text(encoding="utf-8")).get("prefix")
except (OSError, ValueError, AttributeError):
    pfx = None
pfx = str(pfx or "").strip("/")
if pfx and pfx != ".":
    print("{{TOOL_ROOT}}\t%s/" % pfx)' "$2" "${@:3}"
}
# <<< derive_kit_paths
