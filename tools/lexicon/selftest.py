#!/usr/bin/env python3
"""selftest.py — red and green fixtures for every predicate this kit ships.

    python tools/lexicon/selftest.py

EVERY ARM ASSERTS A MESSAGE OR AN EFFECT, never an exit code alone. An exit code tells you the run
failed; it does not tell you it failed FOR THE REASON THE ARM EXISTS TO PROVE, and a fixture that
reds for an unrelated parse error while the arm scores a pass is the fixture-passes-by-finding-
nothing class this tree has a record about.

Each case runs the kit AS INSTALLED: the kit directory is copied into a throwaway git repo and the
engine runs there. That is not ceremony — the waiver registries live in the kit directory, so an
in-place run would read THIS repo's waivers while grading a fixture corpus, and the waiver arms
would be judging the wrong file.
"""

import contextlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


@contextlib.contextmanager
def build_tempdir():
    """A temp dir whose CLEANUP cannot fail this program.

    WINDOWS, and measured on this repo's own bar: a scanner or a lingering git child can still hold
    a handle when the block exits, and `TemporaryDirectory` then raises PermissionError
    [WinError 32] AFTER every arm has already passed. The leg reports exit 1 while its own output
    says "OK - 80 arm(s)", and at width 8 it blocked a push whose bar had been green in another
    worktree minutes earlier. A green selftest reported as a red gate is worse than a leaked
    directory in the OS temp dir, which the OS reclaims.

    `shutil.rmtree(ignore_errors=True)` rather than
    `TemporaryDirectory(ignore_cleanup_errors=True)`: the latter is 3.10+, this kit ships to trees
    with no declared Python floor, and guessing wrong is a TypeError on an adopter first run.
    """
    td = tempfile.mkdtemp()
    try:
        yield td
    finally:
        shutil.rmtree(td, ignore_errors=True)


KIT = Path(__file__).resolve().parent
FAILURES: list[str] = []
PASSES = 0


# =================================================================================================
# THE CROSS-SURFACE ARM — every graded name, both verbs, one verdict.
#
# THE CLOSING REVIEW'S ONE STRUCTURAL FINDING, and it is worth more than the seventeen fixes under
# it: this kit's SUPPLY surface (`--suggest`, the scaffolder, the rendered Skill) was tested against
# SCRATCH declarations while its DEMAND surface (`--check`) was tested against the real tree. Every
# blocker and three of four highs lived in that gap. Three of them were one defect wearing three
# faces — the advisor gating P1 on a `vocab` flag the grader does not read (B2), routing on the raw
# argument while the grader routes on the stem (M1), and testing the surface AFTER routing had
# rewritten the cell key (H3) — and no arm anywhere could see any of them, because no arm ever asked
# the two verbs about ONE name.
#
# WHAT IT ASSERTS, over EVERY name an armed cell grades and not merely over the offenders:
#
#   1. VERDICT. `--suggest` says `OK` for a name exactly when the grader finds no offence in it —
#      no offence being (no convention violation in its cell) AND (not a P1 verb offender, where
#      the cell's surface is the one P1 grades) AND (not a P2 suffix offender, likewise).
#   2. CELL. Where the answer names the cell it answered in, that cell is the one the grader routed
#      the name into — selector and all. A `file` cell is asked with the PATH, which is what an
#      author holds and what forces the stemming and the routing to happen in the right order.
#
# THE POPULATION IS EVERY GRADED NAME, DELIBERATELY. Over offenders alone the arm goes blind on a
# clean cell, which is precisely the population a routing bug hides in — the routed cell that
# disagrees today may hold nothing that offends today. It also gives the arm a live population on a
# green tree, so `0 disagreements` is a measurement rather than an empty set.
#
# IT RUNS AS A SUBPROCESS AGAINST A ROOT so it can be pointed at a kit copy `run_case` has PATCHED.
# The break has to be staged inside the engine — no fixture corpus can reach an ordering defect —
# and two engines cannot be imported into one interpreter, because `lexicon.py` reaches its siblings
# through `sys.path`.
# =================================================================================================


def read_surface_disagreements(root):
    """`(verdict_rows, cell_rows, asked, cell_assertions)` for one repo root.

    Imports the engine from `root/tools/lexicon`, so the caller chooses WHICH engine is graded.
    Nothing here prints and nothing here decides; the `--agree` block below is the only reporter.
    """
    import contextlib as _ctx
    import io as _sio
    import re as _re
    root = Path(root).resolve()
    kit = root / "tools" / "lexicon"
    sys.path.insert(0, str(kit))
    import lexicon as _lex

    conf = _lex.load_conf(root / _lex.CONF_NAME)
    declared = {e: (p, m) for e, p, m in _lex.langs(conf)}
    measured = _lex.measure_pass(root, kit, conf, declared,
                                 _lex.canon.build_clusters(conf.get("CANON") or {}))
    cells = conf.get("CELLS") or {}

    # THE GRADER'S OFFENCES, keyed on `(ext, surface, name)` so a predicate reaches only the surface
    # it actually grades. `PREDICATE_SURFACES` is read rather than restated, for the reason
    # `run_suggest` reads it: a second copy of that mapping is a second answer waiting to disagree.
    offence = set()
    for kind in _lex.KINDS:
        surf = _lex.PREDICATE_SURFACES[kind]
        for o in measured["offenders"][kind]:
            offence.add((_lex.ext_of(o.path), surf, o.text))
    for cell, row in measured["cells"].items():
        if not row["graded"] or row["convention"] == "dark":
            continue
        ext, surf, _k, _l = _lex.parse_cell_key(cell)
        for _p, _l2, nm, _v, _m in row["verdicts"]:
            offence.add((ext, surf, nm))

    asks = []
    for cell, row in measured["cells"].items():
        if not row["graded"] or row["convention"] == "dark":
            continue
        ext, surf, _k, _l = _lex.parse_cell_key(cell)
        parent = f"{ext}.{surf}"
        # `--as` ADDRESSES THE PARENT and refuses a selector, so a selector'd row is asked through
        # its parent — which is exactly the ask an author makes and exactly where the routing has to
        # agree. A parent the declaration does not carry, or carries `dark`, has no answerable ask.
        if parent not in cells or cells[parent][0] == "dark":
            continue
        for path, _l2, nm in row["names"]:
            asks.append((path if surf == "file" else nm, parent, cell,
                         (ext, surf, nm) in offence))

    verdict_rows, cell_rows, seen, assertions = [], [], set(), 0
    for asked_name, parent, grader_cell, is_offence in asks:
        if (asked_name, parent) in seen:
            continue
        seen.add((asked_name, parent))
        buf = _sio.StringIO()
        with _ctx.redirect_stdout(buf):
            _lex.run_suggest(root, asked_name, parent)
        out = buf.getvalue()
        # `OK — ` AT THE HEAD OF A LINE IS THE SUPPLY VERB'S ONLY GREEN SHAPE. Asserted on the line
        # head rather than as a substring: the notes this verb appends can carry the word.
        said_ok = any(ln.startswith("OK — ") for ln in out.splitlines())
        if said_ok == is_offence:
            verdict_rows.append((asked_name, parent,
                                 "grader:offence" if is_offence else "grader:clean",
                                 (out.strip().splitlines() or ["<silent>"])[-1]))
        m = _re.search(r"cell `([^`]+)`", out)
        if m:
            assertions += 1
            if m.group(1) != grader_cell:
                cell_rows.append((asked_name, parent, grader_cell, m.group(1)))
    return verdict_rows, cell_rows, len(seen), assertions


if len(sys.argv) > 2 and sys.argv[1] == "--agree":
    # NOT A USER-FACING MODE. It exists so the arm can be pointed at a PATCHED kit copy; the suite
    # itself is still `python tools/lexicon/selftest.py` with no arguments.
    _v, _c, _asked, _assertions = read_surface_disagreements(sys.argv[2])
    print(f"AGREE asked={_asked} cell_assertions={_assertions} "
          f"verdict_bad={len(_v)} cell_bad={len(_c)}")
    for _r in _v[:15]:
        print("  VERDICT " + " | ".join(str(x) for x in _r))
    for _r in _c[:15]:
        print("  CELL " + " | ".join(str(x) for x in _r))
    raise SystemExit(1 if (_v or _c) else 0)

BASE_CONF = """\
BANNED_SUFFIXES="Manager Helper Util"
LANGS="py:python-ast:parser conf::dark"
VERB_OFFENDER_PIN="0"
SUFFIX_OFFENDER_PIN="0"
ratified="2026-08-16 node d"

VERBS:
  build   create a new value and return it — NOT `create`
  load    read from a store into memory — NOT `fetch`
  add     append to an existing collection — NOT `push`
"""


#: BASE_CONF plus the CELLS block `--suggest --as` needs, and SEPARATE FROM IT on purpose
#: (TOOL-aSurfacedLexicon-8). A `CELLS` block arms the convention predicate over the fixture corpus,
#: so folding these rows into `BASE_CONF` would re-grade the hundred-odd arms that use it for
#: `--check` and change what they measure. `--suggest` returns before the corpus walk, so nothing
#: here is ever walked.
#:
#: The `vocab` rows span five conventions because the shape table below asks each name for the cell
#: whose convention it ALREADY satisfies — which is what keeps every expected answer in that table
#: byte-identical to what it was before `--as` existed, while additionally proving each answer is
#: legal in the cell it was asked for.
SUGGEST_CONF = BASE_CONF.replace(
    'LANGS="py:python-ast:parser conf::dark"',
    'LANGS="py:python-ast:parser js:js-regex:probe md::dark sh:shell-tokens:parser conf::dark"'
).replace(
    "  add     append to an existing collection — NOT `push`",
    "  cmd     a subcommand entry point one level down — NOT `command`\n"
    "  add     append to an existing collection — NOT `push`"
) + """
CELLS:
  py.function  snake  vocab
  js.function  camel  vocab
  js.type      pascal  vocab
  py.constant  screaming  vocab
  md.file      kebab  vocab
  py.type      pascal
  py.file      snake
  sh.file      dark
  py.function+prefix:cmd_  camel  vocab
  py.function+decorator:route  snake
  py.function+prefix:Fetch  pascal
  py.function+prefix:FETCH  screaming
  sh.function  kebab
"""


def check(label: str, cond: bool, detail: str = "") -> None:
    global PASSES
    if cond:
        PASSES += 1
    else:
        FAILURES.append(f"{label}{(' — ' + detail) if detail else ''}")


def run_case(files: dict, conf: str | None, waivers: dict | None = None, args: tuple = (),
             patch: tuple | None = None, drop: tuple = ()):
    """Build a throwaway repo, run the engine in it, return (exit_code, output).

    `patch` is `(old, new)` applied to the COPIED `lexicon.py` before the run, and it exists for the
    two arms no fixture corpus can reach: a default-OFF promotion constant, whose refusing half must
    be observed at THIS unit's landing rather than at the order that flips it, and a mechanism that
    can only be broken from inside the engine. It edits the copy in the throwaway repo and never
    this tree. The replacement is ASSERTED to have happened — a `patch` whose `old` is not present
    would leave the arm running unmodified code and scoring a pass, which is the arm-that-cannot-
    fail class every staged break in this file exists to avoid.

    `drop` names kit files to DELETE from the copy, and it exists for the guards whose failing case
    is an ABSENT subject rather than a wrong one. Like `patch`, the deletion is ASSERTED: naming a
    file that is not there would leave the arm grading an untouched kit and scoring a pass.
    """
    with build_tempdir() as td:
        root = Path(td)
        shutil.copytree(KIT, root / "tools" / "lexicon",
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        if patch is not None:
            # A 3-tuple names the kit FILE to patch; a 2-tuple keeps the original `lexicon.py`
            # default byte for byte. The scaffold's S7 guard reads a sibling module, so the staged
            # break that proves it has to land in that file rather than in the engine.
            _rel, _old, _new = patch if len(patch) == 3 else ("lexicon.py", patch[0], patch[1])
            _engine = root / "tools" / "lexicon" / _rel
            _src = _engine.read_text(encoding="utf-8")
            if _old not in _src:
                raise SystemExit(f"selftest: patch target not found in {_rel}: {_old!r}")
            _engine.write_text(_src.replace(_old, _new), encoding="utf-8", newline="\n")
        for name in drop:
            _victim = root / "tools" / "lexicon" / name
            if not _victim.is_file():
                raise SystemExit(f"selftest: drop target not present in the kit copy: {name}")
            _victim.unlink()
        for name in ("lexicon-verb-waivers.txt", "lexicon-suffix-waivers.txt"):
            (root / "tools" / "lexicon" / name).unlink(missing_ok=True)
        for name, body in (waivers or {}).items():
            (root / "tools" / "lexicon" / name).write_text(body, encoding="utf-8")
        for rel, body in files.items():
            p = root / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(body, encoding="utf-8")
        if conf is not None:
            (root / ".lexicon.conf").write_text(conf, encoding="utf-8")
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        # Stage ONLY the fixture files. The kit is copied in so that its waiver registries and its
        # imports resolve the way an installed kit's do, but it is left UNTRACKED on purpose: the
        # corpus is `git ls-files`, so a tracked kit would put its own sources into the population
        # every arm is grading. The first cut staged `-A` and every case failed on the kit's own
        # identifiers — a fixture measuring itself rather than its fixture.
        subprocess.run(["git", "add", "--", *files, *([".lexicon.conf"] if conf is not None else [])],
                       cwd=root, check=True, capture_output=True)
        r = subprocess.run([sys.executable, "tools/lexicon/lexicon.py", *args], cwd=root,
                           capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr


# ---- P1: the verb predicate ---------------------------------------------------------------------
code, out = run_case({"core/a.py": "def build_index():\n    pass\n"}, BASE_CONF)
check("P1 green: a declared verb passes", code == 0, out)

code, out = run_case({"core/a.py": "def frobnicate_index():\n    pass\n"}, BASE_CONF)
check("P1 red: an undeclared leading token reds", code != 0 and "P1 verb" in out, out)
check("P1 red names the file", "core/a.py" in out, out)
check("P1 red names the identifier", "frobnicate_index" in out, out)
check("P1 red names the offending token", "'frobnicate'" in out, out)

# ---- P2: the banned-suffix predicate ------------------------------------------------------------
code, out = run_case({"core/a.py": "def build_x():\n    pass\n\n\nclass ThingManager:\n    pass\n"}, BASE_CONF)
check("P2 red: a type DEFINITION ending in a banned suffix reds", code != 0 and "ThingManager" in out, out)

# The bare case, which used to be EXEMPT via a `name != suf` guard — the purest instance of "a type
# nobody scoped" was the one the predicate let through.
code, out = run_case({"core/a.py": "def build_x():\n    pass\n\n\nclass Manager:\n    pass\n"}, BASE_CONF)
check("P2 red: a type named EXACTLY the banned suffix reds", code != 0 and "P2 suffix" in out, out)

# The F-A3 arm: a blanket ban breaks on contact with imported names and parameters. P2 is scoped to
# DEFINITION sites only, so neither of these is an offender.
code, out = run_case(
    {"core/a.py": "from elsewhere import ThingManager\n\n\ndef build_x(widget_manager, other: ThingManager):\n"
                  "    return ThingManager\n"},
    BASE_CONF)
check("P2 green: an IMPORTED type and a parameter carrying the suffix do not red", code == 0, out)

# ---- the self-containment refusal, which replaces the deleted P3 ---------------------------------
#
# IT GRADES THE KIT'S OWN DIRECTORY, never the fixture corpus, so these arms point it at a directory
# they build rather than at a `run_case` repo. That parameterised walk root is the whole reason the
# empty-population arm below can be STAGED at all: a predicate that can only read its own installed
# directory has a liveness arm nobody can run, which is the unfalsifiable shape one level up.
#
# THE FIRST IN-PROCESS IMPORT IN THIS FILE, so the path insert lives here. Every arm above runs the
# engine as a SUBPROCESS, which needs no path at all.
sys.path.insert(0, str(KIT))
import lexicon as _lex  # noqa: E402


def build_kit_copy(dest, edits=None):
    """A copy of the INSTALLED kit under `dest`, with `edits` appended to the named modules."""
    shutil.copytree(KIT, dest, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    for name, extra in (edits or {}).items():
        f = dest / name
        f.write_text(f.read_text(encoding="utf-8") + extra, encoding="utf-8", newline="\n")
    return dest


# GREEN, over the kit as installed. This is the control: without it every red arm below could be
# passing because the predicate reds on everything.
_probs, _mods, _imps = _lex.check_self_containment()
check("self-containment: the installed kit is silent", not _probs, str(_probs[:2]))
check("self-containment: ...over a NON-EMPTY population, or the green above means nothing",
      _mods >= 2 and _imps >= 2, f"{_mods} module(s), {_imps} import(s)")

# RED — a foreign import. `map_lib` is the real one this rule exists to forbid: `subtokens.py` is a
# PORT of a `codebase-map` function precisely so this import never has to exist.
with build_tempdir() as _td:
    _kit = build_kit_copy(Path(_td) / "lexicon", {"scaffold_lexicon.py": "\nimport map_lib\n"})
    _probs, _mods, _imps = _lex.check_self_containment(_kit)
    _hit = [x for x in _probs if "NOT SELF-CONTAINED" in x]
    check("self-containment: a foreign import REDS", len(_hit) == 1, str(_probs))
    check("self-containment: ...and the refusal names the file, the line and the target",
          bool(_hit) and "scaffold_lexicon.py" in _hit[0] and "map_lib" in _hit[0]
          and any(c.isdigit() for c in _hit[0].split("scaffold_lexicon.py:")[-1][:4]), str(_hit))

# THE DEDUPE, and it is a real shape rather than a hypothetical: `_python_defs` emits BOTH `map_lib`
# and `map_lib._STOPWORDS` for this statement, so an undeduped refusal names one import twice.
with build_tempdir() as _td:
    _kit = build_kit_copy(Path(_td) / "lexicon",
                          {"scaffold_lexicon.py": "\nfrom map_lib import _STOPWORDS\n"})
    _probs, _, _ = _lex.check_self_containment(_kit)
    check("self-containment: `from x import y` reds ONCE, not once per emitted target",
          len([x for x in _probs if "NOT SELF-CONTAINED" in x]) == 1, str(_probs))

# A RELATIVE import cannot leave the directory, so it is not judged. Without this arm the predicate
# could red every `from . import x` in an adopter's kit and no fixture would say so.
with build_tempdir() as _td:
    _kit = build_kit_copy(Path(_td) / "lexicon",
                          {"scaffold_lexicon.py": "\nfrom . import canon\nimport subprocess\n"})
    _probs, _, _ = _lex.check_self_containment(_kit)
    check("self-containment: a RELATIVE import and a stdlib import are both silent",
          not [x for x in _probs if "NOT SELF-CONTAINED" in x], str(_probs))

# THE LIVENESS ARM. Zero offenders over zero imports is exactly the clean green a broken probe
# prints, which is what the deleted `P3 NOT ARMED` refusal was bought to keep distinguishable. Both
# empty shapes are staged: no modules at all, and modules that yield no imports.
with build_tempdir() as _td:
    _empty = Path(_td) / "nothing"
    _empty.mkdir()
    _probs, _mods, _imps = _lex.check_self_containment(_empty)
    check("self-containment: a directory with NO modules REDS as DEAD PROBE",
          any("DEAD PROBE" in x for x in _probs) and _mods == 0 and _imps == 0, str(_probs))
    _quiet = Path(_td) / "importless"
    _quiet.mkdir()
    (_quiet / "a.py").write_text("def build_x():\n    pass\n", encoding="utf-8", newline="\n")
    _probs, _mods, _imps = _lex.check_self_containment(_quiet)
    check("self-containment: modules that yield NO imports RED too, and the refusal counts them",
          any("DEAD PROBE" in x for x in _probs) and _mods == 1 and _imps == 0, str(_probs))

# END TO END, and through BOTH modes. The refusal sits above the `measure_mode` return so `--check`
# and `--measure` see the same thing; this file's own history has three refusals that landed on the
# wrong side of it, each armed and unreachable from one mode.
with build_tempdir() as _td:
    _r = Path(_td)
    build_kit_copy(_r / "tools" / "lexicon", {"scaffold_lexicon.py": "\nimport map_lib\n"})
    (_r / "core").mkdir(parents=True, exist_ok=True)
    (_r / "core" / "a.py").write_text("def build_index():\n    pass\n", encoding="utf-8", newline="\n")
    (_r / ".lexicon.conf").write_text(BASE_CONF, encoding="utf-8", newline="\n")
    subprocess.run(["git", "init", "-q"], cwd=_r, check=True)
    subprocess.run(["git", "add", "--", "core/a.py", ".lexicon.conf"], cwd=_r, check=True,
                   capture_output=True)
    _both = {}
    for _mode in ("--check", "--measure"):
        _got = subprocess.run([sys.executable, "tools/lexicon/lexicon.py", _mode], cwd=_r,
                              capture_output=True, text=True)
        _both[_mode] = (_got.returncode, _got.stdout + _got.stderr)
    for _mode, (_rc, _o) in _both.items():
        check(f"self-containment: {_mode} exits 1 on a foreign import in the installed kit",
              _rc == 1, f"rc={_rc} {_o[-300:]}")
        check(f"self-containment: ...and {_mode} names the file and the target",
              "scaffold_lexicon.py" in _o and "map_lib" in _o, _o[-300:])

# ...and the population is REPORTED on a green run, so the absence of a refusal is a measurement.
# A printed zero would still be a green, which is why the arm above reds on an empty population.
code, out = run_case({"core/a.py": "def build_index():\n    pass\n"}, BASE_CONF)
check("self-containment: a green run prints the population it judged",
      code == 0 and "self-contained — judged" in out and "module(s)" in out, out)

# THE TWO EXTRACTOR PROPERTIES THE REFUSAL RESTS ON. Both were pinned by the deleted P3 case table
# and neither is testable from the fixture side: `_python_defs` must emit the imported NAME as well
# as its package (which is what the dedupe above exists to handle) and must keep a relative import's
# leading dots (which is how the walk tells relative from bare).
_frm = _lex._python_defs("from pkg.shared_core import helper\n")[2]
check("extract: `from a.b import c` yields a target naming c, not just a.b",
      any(t.endswith("helper") for t, _ln in _frm), f"{_frm}")
_rel = _lex._python_defs("from . import helper\n")[2]
check("extract: a relative `from . import x` keeps its level as leading dots",
      any(t.startswith(".") for t, _ln in _rel), f"{_rel}")

# ---- S6 / AC4: the DEAD PROBE arm ---------------------------------------------------------------
# A declared parser/probe language whose definition population is EMPTY, against a corpus that
# CONTAINS that extension. This is HYGIENE rule 5 applied to this gate: a check must not select an
# empty population, and this is the arm the corpus-side vacuity failure trips.
code, out = run_case({"core/a.py": "X = 1\nY = 2\n"}, BASE_CONF)
check("DEAD PROBE: a declared language with no definitions reds", code != 0, out)
check("DEAD PROBE: it says DEAD PROBE", "DEAD PROBE" in out, out)

# ---- S4: the undeclared-extension refusal -------------------------------------------------------
code, out = run_case({"core/a.py": "def build_x():\n    pass\n", "notes.md": "# hi\n"}, BASE_CONF)
check("undeclared extension reds by name", code != 0 and "md" in out, out)
check("undeclared extension says UNDECLARED", "UNDECLARED EXTENSIONS" in out, out)

# ---- S8 / AC8: waivers key on matched TEXT ------------------------------------------------------
code, out = run_case({"core/a.py": "def frobnicate_index():\n    pass\n"}, BASE_CONF,
                     {"lexicon-verb-waivers.txt": "frobnicate_index  deliberate, see the spec\n"})
check("a waiver on the matched TEXT silences its offender", code == 0, out)

# The whole reason for text keying: `install-prefix-waivers.txt` keys on <path>:<line>, so any edit
# ABOVE a waived line unpins it and reds a merge that touched nothing the waiver guards.
code, out = run_case({"core/a.py": "# a new comment line added above\n# and another\ndef frobnicate_index():\n    pass\n"},
                     BASE_CONF, {"lexicon-verb-waivers.txt": "frobnicate_index  deliberate, see the spec\n"})
check("an edit ABOVE a waived occurrence does NOT unpin it", code == 0, out)

code, out = run_case({"core/a.py": "def build_index():\n    pass\n"}, BASE_CONF,
                     {"lexicon-verb-waivers.txt": "frobnicate_index  the offender is long gone\n"})
check("a waiver whose hit is gone reds as STALE", code != 0 and "STALE WAIVERS" in out, out)

# ---- the opt-in arm -----------------------------------------------------------------------------
code, out = run_case({"core/a.py": "def whatever_x():\n    pass\n"}, None)
check("no conf: the kit is inert and green (opt-in)", code == 0 and "NOT ADOPTED" in out, out)

# ---- AC6: the case-style arm --------------------------------------------------------------------
sys.path.insert(0, str(KIT))
from subtokens import leading_verb  # noqa: E402

for name in ("addTask", "add_task", "AddTask", "add-task"):
    check(f"case style {name} yields 'add'", leading_verb(name) == "add", leading_verb(name))
check("an identifier with no word characters is UNGRADEABLE, not an offender", leading_verb("__") == "")

# ---- AC5: a frozen SENTINEL per shipped pattern set ----------------------------------------------
# The kit-side vacuity arm. The corpus-side one (DEAD PROBE, above) is defeated by an empty corpus,
# so each shipped regex set is run against a frozen fixture that MUST yield a non-zero count. A
# pattern set that goes inert fails HERE rather than passing green over a real repo forever.
import lexicon as lex  # noqa: E402

SENTINELS = {
    "js-regex": (
        "export function buildThing(a) { return a }\n"
        "const loadThing = async (x) => x\n"
        "export class ThingManager {}\n"
        "import fs from 'node:fs'\n"
        "const p = require('node:path')\n"
    ),
}
check("every shipped pattern set has a sentinel",
      set(SENTINELS) == set(lex.PATTERN_SETS), f"{set(lex.PATTERN_SETS) ^ set(SENTINELS)}")
for pset, src in SENTINELS.items():
    funcs, types_, imports = lex._probe_defs(src, pset)
    check(f"sentinel {pset}: functions found", len(funcs) >= 2, f"{funcs}")
    check(f"sentinel {pset}: types found", len(types_) >= 1, f"{types_}")
    check(f"sentinel {pset}: imports found", len(imports) >= 2, f"{imports}")


# ---- TOOL-aSurfacedLexicon-14: the shell parser --------------------------------------------------
#
# EVERY FIXTURE IS KEYED ON THE CONSTRUCT, never on a line in a tracked file. Both live miscount
# instances this parser was built for MOVED LINE while its own spec was being audited — one from
# 1187 to 1211, the other from 287 to 291 — so an arm anchored on a file position grades that file's
# edit history rather than the parser. The constructs are reproduced here instead, which is also the
# only shape an adopter can run: a kit self-test that reads a sibling this repo happens to track is
# a test nobody else has the fixture for.

#: The frozen SHELL sentinel (S4). Same job as the `SENTINELS` above and a separate constant because
#: the shell parser is not a pattern set: a parser that goes inert must fail HERE rather than pass
#: green over a real repo forever, which is the one thing a single tree cannot tell you.
SHELL_SENTINEL = (
    "#!/usr/bin/env bash\n"
    "posix_form() {\n"
    "  echo one\n"
    "}\n"
    "function bash_form {\n"
    "  echo two\n"
    "}\n"
    "function combined_form() {\n"
    "  echo three\n"
    "}\n"
    "subshell_form() (\n"
    "  echo four\n"
    ")\n"
)


def test_shell_sentinel():
    """AC5 — the frozen fixture that tells an INERT parser from a corpus with nothing to find."""
    funcs, types_, imports = lex.parse_shell_defs(SHELL_SENTINEL)
    check("shell sentinel: the frozen fixture yields a non-zero definition count",
          len(funcs) == 4, f"{funcs}")
    check("shell sentinel: it yields no types and no imports, which shell has neither of",
          types_ == [] and imports == [], f"{types_} {imports}")


def test_shell_constructs():
    """One arm per recognised definition form, and one per construct that defeats a line regex."""
    got = lex.parse_shell_defs(SHELL_SENTINEL)[0]
    check("shell: the four recognised definition forms, each at its NAME's line",
          got == [("posix_form", 2), ("bash_form", 5), ("combined_form", 8),
                  ("subshell_form", 11)], f"{got}")

    got = lex.parse_shell_defs("later_brace()\n{\n  :\n}\nfunction later_kw\n{\n  :\n}\n")[0]
    check("shell: a body opening on a LATER line is still a definition",
          got == [("later_brace", 1), ("later_kw", 5)], f"{got}")

    # AC2 — the confirmed live OVER-count. A JavaScript function inside a quoted heredoc body is not
    # a shell definition, and the naive same-line pattern reports it as one.
    got = lex.parse_shell_defs(
        "real_one() {\n"
        "  cat <<'EOF' > /tmp/x\n"
        "function f() { return 'parallel (nope)' }\n"
        "heredoc_body_def() {\n"
        "  :\n"
        "}\n"
        "EOF\n"
        "}\n")[0]
    check("shell: a definition inside a heredoc BODY is not returned (AC2's construct)",
          got == [("real_one", 1)], f"{got}")

    # AC3 — the confirmed live UNDER-count. A heredoc-aware LINE regex reads `<< ours` inside this
    # quoted run of `<` characters as an opener whose terminator never arrives, and blanks every
    # definition below it. A tokenizer never enters that branch: the run is inside single quotes.
    src = ("grep_arm() {\n"
           "  grep -c '^<<<<<<< ours$' \"$1\"\n"
           "}\n") + "".join("below_%d() {\n  :\n}\n" % i for i in range(10))
    got = [n for n, _l in lex.parse_shell_defs(src)[0]]
    check("shell: a quoted run of `<` is not a heredoc opener, and the TEN definitions below it "
          "survive (AC3's construct)",
          got == ["grep_arm"] + ["below_%d" % i for i in range(10)], f"{got}")

    got = [n for n, _l in lex.parse_shell_defs(
        'here_string() {\n  cat <<< "$1"\n}\nafter_here_string() {\n  :\n}\n')[0]]
    check("shell: `<<<` opens no heredoc body", got == ["here_string", "after_here_string"],
          f"{got}")

    # The two `word ( )`-shaped runs this corpus carries by the dozen, neither of them a definition.
    got = lex.parse_shell_defs("names=()\ncase $1 in\n  a) echo a ;;\n  (b) echo b ;;\nesac\n")[0]
    check("shell: an array assignment and a `case` arm are not definitions", got == [], f"{got}")

    # Command substitution is CODE, including inside a double-quoted string, and its parentheses are
    # not the definition form's. BOTH spellings below cost real definitions on the tracked tree
    # before the tokenizer suspended the string state across `$(` — the first lost four, the second
    # twenty, and the two fixes are opposite, which is why this arm carries both.
    # WRAPPED, because the failure this arm guards against is a DESYNC: a string state that is
    # not restored across a command substitution swallows the rest of the file and the parser
    # raises instead of returning a wrong list. An uncaught raise here would red this suite
    # with a traceback naming a line rather than with the arm that knows what broke.
    try:
        got = [n for n, _l in lex.parse_shell_defs(
            'x=$(sed "1s/^[a-z_]*()/y()/")\n'
            'z="$(printf %s "$e" | sed -n \'s/.*FAILED (\\(.*\\))/\\1/p\')"\n'
            "after_subst() {\n  :\n}\n")[0]]
    except SyntaxError as exc:
        got = [f"RAISED {exc}"]
    check("shell: a command substitution does not desync the string state", got == ["after_subst"],
          f"{got}")

    got = [n for n, _l in lex.parse_shell_defs(
        'trim() {\n  echo "${1#x}"   # a real comment\n}\n')[0]]
    check("shell: `${x#y}` is a parameter expansion and not a comment", got == ["trim"], f"{got}")


def test_shell_refusals():
    """The three refusals of `parse_shell_defs`, each observed the only way it CAN be observed."""
    # THE LAST TWO ARE ONE CONSTRUCT AND TWO RAISES, which is why both are here. An unterminated
    # heredoc whose opener is followed by a newline is refused by the body-drain loop, which runs at
    # that newline and walks off the end of the source. An opener on the FINAL line with no newline
    # after it never reaches that loop at all — the queue is still full when the scan ends, and the
    # only thing that refuses it is the tail check after the loop. Deleting that tail check leaves
    # every other arm in this file green and launders a truncated file into a clean parse.
    # THE THIRD COLUMN IS THE POINT. Every message here starts "unterminated ", so an arm asserting
    # only that, or only that a line is named, scores a pass whenever ANY sibling refusal fires
    # first — which is how `$((` sat unarmed while five neighbours looked covered. Each row names
    # the CONSTRUCT its refusal must print, and no two of those needles are substrings of another.
    for label, src, needle in (
            ("an unterminated single quote", "f() {\n  echo 'oops\n}\n", "unterminated ' quote"),
            ("an unterminated double quote", 'f() {\n  echo "oops\n}\n', 'unterminated " quote'),
            ("an unterminated heredoc", "f() {\n  cat <<EOF\nbody\n}\n",
             "unterminated heredoc <<EOF"),
            ("a heredoc opened on the FINAL line, with no newline after it", "f() {\n  cat <<EOF",
             "unterminated heredoc <<EOF"),
            ("an unterminated ${", "f() {\n  echo ${x\n", "unterminated ${"),
            # The sixth construct, and the one with no fixture until now: `$((` is found by a plain
            # `find("))")` whose miss is the ONLY thing standing between a truncated arithmetic
            # expansion and a silently short definition list. Its whole body is swallowed into one
            # token, so nothing downstream reds — the refusal is the entire signal.
            ("an unterminated $((", "f() {\n  echo $((1 + 2\n}\n", "unterminated $((")):
        try:
            lex.parse_shell_defs(src)
        except SyntaxError as exc:
            check(f"shell refusal: {label} RAISES, names the CONSTRUCT and its line",
                  needle in str(exc) and "line" in str(exc), str(exc))
        else:
            check(f"shell refusal: {label} RAISES, names the CONSTRUCT and its line", False,
                  "returned a list instead of raising")

    got = [n for n, _l in lex.parse_shell_defs(
        '. "$HERE/lib.sh"\neval "gen_$n() { :; }"\nreal_def() {\n  :\n}\n')[0]]
    check("shell refusal: a sourced or eval-constructed definition is not found, the real one is",
          got == ["real_def"], f"{got}")

    # THE ONLY OBSERVATION THE `eval`/`source` REFUSAL GETS BEYOND THE ARM ABOVE, and it is owed:
    # that refusal has no failing runtime behaviour to stage, so without this a header naming one
    # refusal and omitting the other two would pass every arm in this file.
    doc = lex.parse_shell_defs.__doc__ or ""
    for token in ("name() { … }", "function name { … }", "function name() { … }", "name() ( … )",
                  "SyntaxError", "eval", "source", "HEREDOC BODY"):
        check(f"shell header: the docstring enumerates {token!r}", token in doc,
              "missing from the docstring")


test_shell_sentinel()
test_shell_constructs()
test_shell_refusals()

#: A declaration that arms shell and NOTHING else, for the end-to-end arms below. Separate from
#: `BASE_CONF` because that one declares `py` and `conf` and would put the fixture's own extensions
#: into a population these arms are not about.
SH_CONF = """\
BANNED_SUFFIXES="Manager"
LANGS="sh:shell-tokens:parser conf::dark"
VERB_OFFENDER_PIN="0"
SUFFIX_OFFENDER_PIN="0"
ratified="2026-09-05 node a"

VERBS:
  build   create a new value and return it — NOT `create`
"""

code, out = run_case({"core/ok.sh": "build_thing() {\n  :\n}\n"}, SH_CONF)
check("shell end to end: an armed shell corpus grades and passes", code == 0, out)
check("shell end to end: the run reports .sh=parser", ".sh=parser" in out, out)

code, out = run_case({"core/ok.sh": "build_thing() {\n  :\n}\n",
                      "core/broken.sh": "build_other() {\n  echo 'oops\n}\n"}, SH_CONF)
check("AC6: an untokenizable shell file under an armed declaration REFUSES", code != 0, out)
check("AC6: the refusal names the file", "core/broken.sh" in out, out)
check("AC6: the refusal names the position", "line 2" in out, out)
check("AC6: and does NOT report an empty definition list for it",
      "does not parse" in out and "DEAD PROBE" not in out, out)

code, out = run_case({"core/ok.sh": "build_thing() {\n  :\n}\n"},
                     SH_CONF.replace("shell-tokens", "no-such-parser"))
check("a LANGS `parser` row naming an unshipped parser REFUSES rather than silently grading Python",
      code != 0 and "does not ship" in out and "no-such-parser" in out, out)

# ---- the --scaffold path, end to end -------------------------------------------------------------
# Nothing exercised this before, which is how a scaffolder that could emit a row its OWN reader
# refuses went unnoticed: `leading_verb` can return a digit run (`2fa_check` -> `2`) and the conf
# reader requires an alphabetic verb. A kit whose first command writes a file its second command
# rejects has no working adoption path at all.
with build_tempdir() as td:
    root = Path(td)
    shutil.copytree(KIT, root / "tools" / "lexicon",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (root / "src").mkdir()
    (root / "src" / "a.py").write_text(
        "def build_x():\n    pass\n\n\ndef load_y():\n    pass\n\n\ndef 十_bad():\n    pass\n"
        .replace("十_bad", "_2fa_check"), encoding="utf-8")
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    subprocess.run(["git", "add", "--", "src/a.py"], cwd=root, check=True, capture_output=True)
    r = subprocess.run([sys.executable, "tools/lexicon/scaffold_lexicon.py", str(root / ".lexicon.conf")],
                       cwd=root, capture_output=True, text=True)
    check("scaffold: exits 0", r.returncode == 0, r.stdout + r.stderr)
    # GUARDED, because the arm above is allowed to FAIL and this line is not allowed to crash the
    # run when it does. An unconditional read here raised FileNotFoundError the moment the
    # scaffolder exited non-zero, which killed the interpreter before the summary printed — so a
    # named arm failure came out as a traceback with no arm in it, and every arm below went
    # unexercised and unreported. Found by staging an unrelated break upstream of it.
    _cf = root / ".lexicon.conf"
    if not _cf.exists():
        _cf.write_bytes(b"")
    conf_text = _cf.read_text(encoding="utf-8")
    check("scaffold: marks the seed PROPOSED", "PROPOSED" in conf_text, conf_text[:200])
    check("scaffold: leaves ratified EMPTY", 'ratified=""' in conf_text, conf_text[:200])

    sys.path.insert(0, str(KIT))
    from lexicon_conf import ConfError, load_conf  # noqa: E402
    try:
        parsed = load_conf(root / ".lexicon.conf")
        check("scaffold: the file it wrote PARSES through its own reader", True)
        check("scaffold: every seeded verb is alphabetic, as the reader requires",
              all(v.isalpha() for v in parsed["VERBS"]), f"{sorted(parsed['VERBS'])}")
        check("scaffold: a non-alphabetic leading token is FILTERED, not emitted",
              "2" not in parsed["VERBS"], f"{sorted(parsed['VERBS'])}")
    except ConfError as e:
        check("scaffold: the file it wrote PARSES through its own reader", False, str(e))

    r = subprocess.run(["bash", "tools/lexicon/adopt-lexicon.sh", "--check"], cwd=root,
                       capture_output=True, text=True)
    out = r.stdout + r.stderr
    check("scaffold: --check REDS on the unratified seed", r.returncode != 0, out)
    check("scaffold: and says the seed is unratified", "ratified" in out, out)

    # BOTH HALVES OF THE CRLF FIX, ARMED. Reverting either one used to leave every arm green, which
    # made the fix a claim rather than a behaviour. The failure it prevents is an INVERSION: an
    # anchored `s/"$//` cannot strip a quote a carriage return follows, so `ratified=""` in a CRLF
    # conf yields `"\r` — a NON-EMPTY value — and the one check that stops an uncurated table
    # reaching the merge bar passes exactly when it must fire.
    check("scaffold: the conf it wrote contains NO CR bytes",
          b"\r" not in (root / ".lexicon.conf").read_bytes(),
          repr((root / ".lexicon.conf").read_bytes()[:120]))

    crlf = (root / ".lexicon.conf").read_bytes().replace(b"\n", b"\r\n")
    (root / ".lexicon.conf").write_bytes(crlf)
    r = subprocess.run(["bash", "tools/lexicon/adopt-lexicon.sh", "--check"], cwd=root,
                       capture_output=True, text=True)
    out = r.stdout + r.stderr
    check("scaffold: --check STILL reds on an unratified seed in a CRLF conf (the reader strips CR)",
          r.returncode != 0, out)
    check("scaffold: and still names it unratified rather than passing", "ratified" in out, out)

    # ---- B3: THE SCAFFOLDED ADOPTER'S FIRST `--suggest` HAS TO WORK ---------------------------
    #
    # The seed emitted `LANGS`, `VERBS` and both scalar pins and NO `CELLS` block, while `--as
    # <ext>.<surface>` is REQUIRED and `resolve_cell` refuses any spec no `CELLS` row names. So the
    # very command the Skill this same `--scaffold` run installs documents exited 2 with "Declared
    # cells: none", on every fresh adoption, and nothing surfaced the gap. This arm binds the
    # scaffolder to the Skill it installs, which is the actual contract.
    #
    # THE CELL IS READ OUT OF THE SEED, never spelled here: an arm naming `py.function` would pass
    # on a scaffolder that emitted that one row and nothing else, and would red on an adopter whose
    # corpus is JavaScript. What is asserted is that the seed carries an ANSWERABLE cell at all.
    _seed = load_conf(root / ".lexicon.conf") if (root / ".lexicon.conf").read_text(
        encoding="utf-8").strip() else {}
    _seed_cells = {k: v for k, v in (_seed.get("CELLS") or {}).items()
                   if v[0] != "dark" and "+" not in k}
    check("B3: --scaffold emits a CELLS block with at least one ARMED cell",
          bool(_seed_cells), f"CELLS={_seed.get('CELLS')}")
    if _seed_cells:
        _cell = sorted(_seed_cells)[0]
        _r = subprocess.run([sys.executable, "tools/lexicon/lexicon.py",
                             "--suggest", "fetch_thing", "--as", _cell],
                            cwd=root, capture_output=True, text=True)
        _o = _r.stdout + _r.stderr
        check(f"B3: ...and the Skill's documented invocation succeeds on it (--as {_cell})",
              _r.returncode == 0 and "UNDECLARED" not in _o, f"rc={_r.returncode} {_o}")

    # ---- B1: THE DECLARATION IS GRADED ON THE UNGUARDED LEG -----------------------------------
    #
    # The only leg that computed a verdict over `.lexicon.conf` was guarded on `tools/` and three
    # sibling dirs, and the conf is at the repo ROOT — so a branch whose entire diff was the
    # declaration skipped its own verifier, and the tool's own red text instructs an author to
    # produce exactly that commit ("Paste this row into .lexicon.conf"). The guard could not be
    # widened: govkit's guard taxonomy has no class for a root-level conf and declaring one reds
    # `govkit selfcheck`, a ruling written into this kit's `kit.toml`. So the grade moved into
    # `adopt-lexicon.sh --check`, which is the argv of the one leg here carrying an EMPTY guard.
    #
    # RATIFIED FIRST, because the unratified-seed refusal above would otherwise supply the red and
    # this arm would pass on the wrong refusal — the fixture-reds-for-another-reason class.
    _conf_p = root / ".lexicon.conf"
    _conf_p.write_text(_conf_p.read_text(encoding="utf-8")
                       .replace('ratified=""', 'ratified="2026-09-06 node a"'),
                       encoding="utf-8", newline="\n")
    subprocess.run(["git", "add", "--", ".lexicon.conf"], cwd=root, capture_output=True)
    subprocess.run(["bash", "tools/lexicon/adopt-lexicon.sh", "--render"], cwd=root,
                   capture_output=True, text=True)
    _r = subprocess.run(["bash", "tools/lexicon/adopt-lexicon.sh", "--check"], cwd=root,
                        capture_output=True, text=True)
    _o = _r.stdout + _r.stderr
    check("B1 control: a ratified scaffolded seed passes --check, grade included",
          _r.returncode == 0 and "declaration grades clean" in _o, _o)
    # THE CONF-ONLY EDIT, which is the whole shape of the finding: nothing under `tools/` moves.
    _conf_p.write_text(_conf_p.read_text(encoding="utf-8")
                       .replace('VERB_OFFENDER_PIN="', 'VERB_OFFENDER_PIN="9'),
                       encoding="utf-8", newline="\n")
    _r = subprocess.run(["bash", "tools/lexicon/adopt-lexicon.sh", "--check"], cwd=root,
                        capture_output=True, text=True)
    _o = _r.stdout + _r.stderr
    check("B1: a CONF-ONLY pin change reds --check, which is the leg no guard scopes off a bar",
          _r.returncode != 0 and "THE DECLARATION DOES NOT GRADE" in _o, _o)
    check("B1: ...and the engine's own output rides along, naming the row to paste",
          "pin" in _o and "VERB_OFFENDER_PIN=" in _o, _o)

    # A FLAG IS NOT A PATH. This script guarded its argv by ARITY alone, so
    # `scaffold_lexicon.py --help` is a well-formed one-argument call and `--help` became the
    # DESTINATION: the run derived a whole seed and wrote it to a file literally named `--help`.
    # Measured on a real adopter (incms/main, 2026-08-23), where that file was committed and pushed
    # and then survived every leg of a 62-leg bar — nothing there enumerates root-level filenames,
    # and this kit's own `--check` looks for `.lexicon.conf` BY NAME, so a stray sibling is invisible
    # to it. The wrapper already refuses an unknown flag; the script it calls did not, and the script
    # is the one that writes. A file whose name is a flag is also a live hazard for every unquoted
    # glob in its directory: `wc -l *` in that adopter's root printed wc's usage instead of counting.
    for flag in ("--help", "-h"):
        r = subprocess.run([sys.executable, "tools/lexicon/scaffold_lexicon.py", flag],
                           cwd=root, capture_output=True, text=True)
        out = r.stdout + r.stderr
        check(f"scaffold: refuses {flag} as a destination rather than writing it",
              r.returncode != 0, out)
        check(f"scaffold: and NAMES the refusal rather than failing silently ({flag})",
              "usage" in out.lower(), out)
        check(f"scaffold: no file named {flag} is left behind",
              not (root / flag).exists(), f"{flag} exists in {root}")

# ---- RE-SCAFFOLDING MEASURES OVER THE EXISTING DECLARATION, and this arm is the gate for it -------
#
# NOTHING EXERCISED IT. Reverting `scan_corpus(root, declared, sets)` in `scaffold_lexicon.py` to the
# shipped `scan_corpus(root, KNOWN)` left every arm in this file green, so a mechanism the unit
# reports as satisfied was carried by no check at all. The failure it prevents: a repo that armed a
# language through a `PATTERNS:` row gets re-scaffolded, that language is silently outside the walk,
# and every pin the scaffolder MEASURES is derived over a corpus with it missing — a number the tool
# itself wrote, against a population the tool itself could not see.
#
# The `.ts` file carries the ONLY definition of a verb the `.py` corpus never spells, so the seeded
# table holds it exactly when the declaration was read. Both revert flavours red here: dropping
# `declared` leaves `.ts` unarmed, and dropping `sets` alone makes `scan_corpus` refuse `ts-regex` as
# an unshipped set one line earlier, which is why the NOT EXTRACTED assertion rides along.
with build_tempdir() as td:
    root = Path(td)
    shutil.copytree(KIT, root / "tools" / "lexicon",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (root / "src").mkdir()
    (root / "src" / "a.py").write_text("def build_x():\n    pass\n", encoding="utf-8", newline="\n")
    (root / "web").mkdir()
    (root / "web" / "widget.ts").write_text("export function loadWidget() {}\n",
                                            encoding="utf-8", newline="\n")
    (root / ".lexicon.conf").write_text(
        'BANNED_SUFFIXES="Manager"\n'
        'LANGS="py:python-ast:parser ts:ts-regex:probe conf::dark"\n'
        'VERB_OFFENDER_PIN="0"\nSUFFIX_OFFENDER_PIN="0"\n'
        'ratified="2026-09-04 node a"\n\n'
        'VERBS:\n  build   create a new value and return it — NOT `create`\n\n'
        'PATTERNS:\n'
        r'  ts-regex.functions  ^\s*(?:export\s+)?function\s+([A-Za-z_$][\w$]*)' '\n',
        encoding="utf-8", newline="\n")
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    subprocess.run(["git", "add", "--", "src/a.py", "web/widget.ts", ".lexicon.conf"],
                   cwd=root, check=True, capture_output=True)
    r = subprocess.run([sys.executable, "tools/lexicon/scaffold_lexicon.py", str(root / "seed.conf")],
                       cwd=root, capture_output=True, text=True)
    check("re-scaffold: exits 0 over an existing declaration", r.returncode == 0, r.stdout + r.stderr)
    check("re-scaffold: the PATTERNS-armed language is not refused as unextractable",
          "NOT EXTRACTED" not in (r.stdout + r.stderr), r.stdout + r.stderr)
    # GUARDED for the reason the scaffold block above is: the two arms before this one are
    # allowed to FAIL, and an unconditional read here turns their failure into a traceback
    # that kills the summary and leaves every arm below unexercised and unreported.
    _seeded = (load_conf(root / "seed.conf")["VERBS"]
               if (root / "seed.conf").exists() else {})
    check("re-scaffold: a verb defined ONLY in the PATTERNS-armed language reaches the seed",
          "load" in _seeded, f"seeded={sorted(_seeded)} stderr={r.stderr!r}")
    check("re-scaffold: ...and the Python half is still seeded beside it",
          "build" in _seeded, f"seeded={sorted(_seeded)}")

# ---- verdict ------------------------------------------------------------------------------------
# ---- TOOL-dScaffoldedMirror-2: per-predicate populations, counts on green, an honest --measure ----
#
# WHAT THESE ARE NOT. None of them asserts a VERDICT change: this unit reports, and section 3 of its
# spec forbids moving an exit code except `--measure`'s. So every arm below reads OUTPUT, and the two
# that read an exit code read `--measure`'s, which is the one this unit is allowed to move.

_U2 = {"core/a.py": "def build_index():\n    pass\n"}

code, out = run_case(_U2, BASE_CONF)
check("counts on GREEN: every predicate reports graded/offenders/waived",
      code == 0 and "P1 verb" in out and "graded=" in out and "offenders=" in out and "waived=" in out,
      out)
check("counts on GREEN: the SUFFIX predicate reports its own population, not a folded one",
      "P2 suffix graded=" in out, out)

# The armed-but-empty pair. `js` declares a types extractor and this fixture has no class, which is a
# repo that writes no JavaScript classes rather than an extractor gone inert — so it is NAMED and the
# run stays GREEN. Making it red was rev-1's design and the spec's section 4 records why that is wrong.
_JS_CONF = BASE_CONF.replace('LANGS="py:python-ast:parser conf::dark"',
                             'LANGS="py:python-ast:parser js:js-regex:probe conf::dark"')
code, out = run_case({**_U2, "web/app.js": "function build_widget() {}\n"}, _JS_CONF)
check("armed but empty: the (extension, predicate) pair is NAMED", ".js suffix=0" in out, out)
check("armed but empty: ...and it is a REPORT, so the run stays green", code == 0, out)
check("armed but empty: the wording says it is not a refusal", "not a refusal" in out, out)

# ...and the count is DERIVED, not a constant: give the same fixture a class and it moves. Without
# this arm the one above passes against a hardcoded zero.
code, out = run_case({**_U2, "web/app.js": "class Widget {}\nfunction build_widget() {}\n"}, _JS_CONF)
check("the suffix population is derived: a class makes it non-zero",
      ".js suffix=0" not in out and "P2 suffix graded=1" in out, out)

# `--measure` exits on its own refusals. It printed them as `# NOTE:` under an unconditional 0, and
# three later units use it as a discharge probe.
code, out = run_case(_U2, BASE_CONF, args=("--measure",))
check("--measure on a clean tree still exits 0", code == 0 and "VERB_OFFENDER_PIN" in out, out)

code, out = run_case({**_U2, "notes.R": "x <- 1\n"}, BASE_CONF, args=("--measure",))
check("--measure exits NON-ZERO over an undeclared extension", code != 0, out)
check("--measure still prints the pins it was asked for", "VERB_OFFENDER_PIN" in out, out)
# THE EXTENSION IS ASSERTED AS A TOKEN IN THE LIST, not as a substring of the output. A bare "R" is
# satisfied by the R inside UNDECLA-R-ED, so the conjunct could not independently fail and the arm
# was half decoration -- and the first fix, `": R"`, was no better: it is satisfied by the header's
# own `): R...` whenever the value happens to start with an R. Parsing the line is what makes the
# break observable. Closing review L1.
_undec = [ln for ln in out.splitlines() if "UNDECLARED EXTENSIONS" in ln]
check("--measure names the undeclared extension",
      len(_undec) == 1 and "R" in [t.strip() for t in _undec[0].rsplit(":", 1)[-1].split(",")], out)

# ---- TOOL-dScaffoldedMirror-6: the coverage sniffer, its fraction, and its liveness --------------

_U6 = {"core/a.py": "def build_index():\n    pass\n"}

code, out = run_case(_U6, BASE_CONF)
check("coverage: the fraction prints on a GREEN run",
      code == 0 and "coverage - armed" in out.replace("\u2014", "-").replace(chr(8212), "-")
      and "definition-carrying file(s)" in out, out)

# DERIVED, not a constant: an unarmed shell file joins the denominator and the fraction falls.
_SH_CONF = BASE_CONF.replace('LANGS="py:python-ast:parser conf::dark"',
                             'LANGS="py:python-ast:parser conf::dark sh::dark"')
code, out2 = run_case({**_U6, "scripts/go.sh": "build_it() {\n  :\n}\n"}, _SH_CONF)
check("coverage: an unarmed definition-carrying file LOWERS the fraction",
      code == 0 and "armed 1 of 2" in out2, out2)

# The PROSE judgement, armed. A fenced example inside documentation is not a definition, and counting
# it made a number that moves when somebody writes a tutorial. Measured on the real tree when this
# arm landed, against an armed share that has since moved: including `.md` dragged the reported
# coverage DOWN by more than a third of its own value. Both operands are historical and neither is
# restated here, because the arm below tests the judgement rather than the figure.
_MD = "Example:\n\n```python\ndef build_thing():\n    pass\n```\n"
_MD_CONF = BASE_CONF.replace('LANGS="py:python-ast:parser conf::dark"',
                             'LANGS="py:python-ast:parser conf::dark md::dark"')
code, out3 = run_case({**_U6, "docs/guide.md": _MD}, _MD_CONF)
check("coverage: a fenced code block in PROSE does not join the denominator",
      code == 0 and "armed 1 of 1" in out3, out3)

# S6 — the liveness. What it asserts is AGREEMENT: every file an armed extractor found a definition
# in must also sniff positive. Staged by blinding the sniffer inside a fixture copy of the kit.
with build_tempdir() as _td:
    _r = Path(_td)
    shutil.copytree(KIT, _r / "tools" / "lexicon", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    _eng = _r / "tools" / "lexicon" / "lexicon.py"
    _src = _eng.read_text(encoding="utf-8")
    _i = _src.index("DEFINITION_SNIFF = re.compile(")
    _j = _src.index("re.M | re.X,", _i)
    _eng.write_text(_src[:_i] + 'DEFINITION_SNIFF = re.compile(\n    "ZZZ_NO_MATCH",\n    ' + _src[_j:],
                    encoding="utf-8", newline="\n")
    for _rel, _body in _U6.items():
        _p = _r / _rel
        _p.parent.mkdir(parents=True, exist_ok=True)
        _p.write_text(_body, encoding="utf-8")
    (_r / ".lexicon.conf").write_text(BASE_CONF, encoding="utf-8")
    subprocess.run(["git", "init", "-q"], cwd=_r, check=True)
    subprocess.run(["git", "add", "--", *_U6, ".lexicon.conf"], cwd=_r, check=True, capture_output=True)
    _got = subprocess.run([sys.executable, "tools/lexicon/lexicon.py"], cwd=_r,
                          capture_output=True, text=True)
    _all = _got.stdout + _got.stderr
    check("S6: a BLIND sniffer reds as DEAD SNIFFER rather than reporting perfect coverage",
          _got.returncode != 0 and "DEAD SNIFFER" in _all, _all[-300:])
    check("S6: ...and it names the reading it contradicts",
          "ARMED extractor did" in _all, _all[-300:])

# ---- TOOL-dScaffoldedMirror-8 S6: the table's own shape ------------------------------------------
#
# These two grade the DECLARATION rather than the corpus, which makes them the only checks in this
# suite whose fixture is a conf and not a tree. Both directions are armed: a table that satisfies
# them, and a table that does not.

_S6_OK = BASE_CONF   # every row in BASE_CONF already carries a NOT clause

code, out = run_case({"core/a.py": "def build_index():\n    pass\n"}, _S6_OK)
check("S6: a table whose every row carries a negative is silent",
      code == 0 and "carrying no negative" not in out, out)

# A row with no negative cannot draw a boundary, and the gate message degrades to "not in the table".
_S6_BARE = _S6_OK.replace("  load    read from a store into memory \u2014 NOT `fetch`",
                          "  load    read from a store into memory")
check("S6 fixture really differs (or the next arm proves nothing)", _S6_BARE != _S6_OK, "replace missed")
code, out = run_case({"core/a.py": "def build_index():\n    pass\n"}, _S6_BARE)
check("S6: a row with NO negative is a finding", code != 0 and "carrying no negative" in out, out)
check("S6: ...and it names the row", "load" in out.split("carrying no negative")[1][:80], out)

# A token that is both banned and declared bans and permits itself at once.
_S6_CLASH = _S6_OK.replace("NOT `fetch`", "NOT `add`")
check("S6 clash fixture really differs", _S6_CLASH != _S6_OK, "replace missed")
code, out = run_case({"core/a.py": "def build_index():\n    pass\n"}, _S6_CLASH)
check("S6: a banned token that is itself a row is a finding",
      code != 0 and "itself a row" in out, out)
check("S6: ...and it names the token", "add" in out.split("itself a row")[1][:60], out)

# ---- TOOL-dScaffoldedMirror-10: the two SUPPLY verbs ---------------------------------------------
#
# Every arm here asserts that neither verb can behave like a gate. That is S6, and it is the property
# that keeps "what the corpus does" from becoming "what the corpus should do": a report that can exit
# 1 is a gate with a softer name.

_U10 = {"core/a.py": "def build_index():\n    pass\n",
        "core/b.py": "def render_index():\n    pass\n"}

code, out = run_case(_U10, SUGGEST_CONF, args=("--suggest", "build_index", "--as", "py.function"))
check("--suggest: a declared verb answers OK and exits 0", code == 0 and out.startswith("OK"), out)

code, out = run_case(_U10, SUGGEST_CONF, args=("--suggest", "fetch_remote", "--as", "py.function"))
check("--suggest: an off-table token names the REPLACEMENT from the NOT clause",
      code == 0 and "load_remote" in out and "`load`" in out and "`fetch`" in out, out)
check("--suggest: ...and quotes the negative definition rather than only the token",
      "NOT `fetch`" in out, out)

code, out = run_case(_U10, SUGGEST_CONF, args=("--suggest", "frobnicate_thing", "--as", "py.function"))
check("--suggest: a token NO row bans says so, and still exits 0",
      code == 0 and "no row bans it by name" in out, out)

# S6 — the structural guards. A report that can exit 1, or that prints a pin, is a gate.
for _v in (("--suggest", "fetch_remote", "--as", "py.function"),):
    code, out = run_case(_U10, BASE_CONF, args=_v)
    check(f"S6: {_v[0]} never exits 1", code != 1, f"rc={code} {out}")
    check(f"S6: {_v[0]} prints no pin figure",
          "_OFFENDER_PIN" not in out and "over pin" not in out, out)

# ---- TOOL-dScaffoldedMirror-8: the canon, and the rule that makes it worth having ----------------

import canon as _canon   # noqa: E402

# The canon's own shape. A form in two clusters makes the representative depend on iteration order.
_idx = _canon.build_form_index()
_dupes = []
_seen = {}
for _rep, _g, _others in _canon.CLUSTERS:
    for _f in (_rep,) + tuple(_others):
        if _f in _seen and _seen[_f] != _rep:
            _dupes.append(_f)
        _seen[_f] = _rep
check("canon: no surface form appears in two clusters", not _dupes, str(_dupes))
check("canon: every representative maps to itself",
      all(_idx[r] == r for r, _g, _o in _canon.CLUSTERS), "a representative resolved elsewhere")
check("canon: every row can render a negative",
      all(_canon.render_negative(r) for r, _g, _o in _canon.CLUSTERS), "a cluster with no alternative")

# ARM (a) — VOLUME CANNOT PROMOTE. Five hundred sites of a token in no cluster must not enter.
_many = {"core/a%d.py" % i: "def frobnicate_thing%d():\n    pass\n" % i for i in range(60)}
_many["core/z.py"] = "def build_it():\n    pass\n"
with build_tempdir() as _td:
    _r = Path(_td)
    shutil.copytree(KIT, _r / "tools" / "lexicon", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    for _rel, _b in _many.items():
        _p = _r / _rel
        _p.parent.mkdir(parents=True, exist_ok=True)
        _p.write_text(_b, encoding="utf-8")
    subprocess.run(["git", "init", "-q"], cwd=_r, check=True)
    subprocess.run(["git", "add", "--", *_many], cwd=_r, check=True, capture_output=True)
    subprocess.run([sys.executable, "tools/lexicon/scaffold_lexicon.py", ".lexicon.conf"],
                   cwd=_r, capture_output=True, text=True)
    _conf = (_r / ".lexicon.conf").read_text(encoding="utf-8")
    check("canon: 60 sites of an off-canon token do NOT put it in the proposed table",
          "frobnicate" not in _conf, _conf[-400:])
    check("canon: ...while the one in-canon site DOES enter", "\n  build " in _conf, _conf[-400:])

# ARM (b) — THE POLARITY ARM, and the one a dominance table fails. `get` and `fetch` each have a
# live site and `load` has NONE, so a count-based rule proposes get or fetch. The first-element rule
# proposes `load`, which is in neither file.
_pol = {"core/a.py": "def get_row():\n    pass\n", "core/b.py": "def fetch_row():\n    pass\n"}
with build_tempdir() as _td:
    _r = Path(_td)
    shutil.copytree(KIT, _r / "tools" / "lexicon", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    for _rel, _b in _pol.items():
        _p = _r / _rel
        _p.parent.mkdir(parents=True, exist_ok=True)
        _p.write_text(_b, encoding="utf-8")
    subprocess.run(["git", "init", "-q"], cwd=_r, check=True)
    subprocess.run(["git", "add", "--", *_pol], cwd=_r, check=True, capture_output=True)
    subprocess.run([sys.executable, "tools/lexicon/scaffold_lexicon.py", ".lexicon.conf"],
                   cwd=_r, capture_output=True, text=True)
    _conf = (_r / ".lexicon.conf").read_text(encoding="utf-8")
    check("POLARITY: a corpus of get and fetch proposes `read` and `load`, the forms it does not use",
          "\n  read " in _conf and "\n  load " in _conf, _conf[-400:])
    check("POLARITY: ...and proposes NEITHER spelling the corpus actually wrote",
          "\n  get " not in _conf and "\n  fetch " not in _conf, _conf[-400:])

# S8 — `conf` is seeded whether or not the corpus contains one, because the scaffold runs before the
# file it writes is tracked.
with build_tempdir() as _td:
    _r = Path(_td)
    shutil.copytree(KIT, _r / "tools" / "lexicon", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (_r / "core").mkdir(parents=True, exist_ok=True)
    (_r / "core" / "a.py").write_text("def build_it():\n    pass\n", encoding="utf-8")
    subprocess.run(["git", "init", "-q"], cwd=_r, check=True)
    subprocess.run(["git", "add", "--", "core/a.py"], cwd=_r, check=True, capture_output=True)
    subprocess.run([sys.executable, "tools/lexicon/scaffold_lexicon.py", ".lexicon.conf"],
                   cwd=_r, capture_output=True, text=True)
    _conf = (_r / ".lexicon.conf").read_text(encoding="utf-8")
    check("S8: `conf::dark` is seeded even though no .conf file was tracked at scaffold time",
          "conf::dark" in _conf, [l for l in _conf.split(chr(10)) if l.startswith("LANGS=")])
    # The conf grammar forbids a comment after a value on the same line, and the first cut of the
    # canon scaffold put one there -- the reader then REFUSED the file the scaffold had just written.
    # THE EXPECTED SET IS `PIN_KEYS`, not a list retyped here. It read three when the kit declared
    # three predicates, and a literal beside a population is wrong on the commit that moves it.
    _pin_lines = [l for l in _conf.split(chr(10)) if l.startswith(tuple(lex.PIN_KEYS.values()))]
    check("S8: every declared pin is emitted, each on a line carrying no trailing comment",
          len(_pin_lines) == len(lex.PIN_KEYS) and not any("#" in l for l in _pin_lines),
          str(_pin_lines))
    check("S8: ...and a DEAD pin key is not emitted either",
          "LAYER_OFFENDER_PIN" not in _conf, _conf[:200])

# ---- closing-review left-shifts (round 1) --------------------------------------------------------
#
# Both arms below gate a CLASS. The review's own words on why: "a single-site fix certifies coverage
# the script does not have, and the shape will recur the next time a mode is added."

# H1 — `--measure` and `--check` must AGREE, and agreement is on the REASON as well as the code.
# Round 1 asserted the exit codes alone and this comment claimed the arm "would have caught the DEAD
# SNIFFER defect as well". It would not have, twice over: DEAD SNIFFER was not one of the trees the
# loop enumerated, and it set `exit_code` directly seventy-nine lines below the measure-mode return,
# so `--measure` exited 0 with three clean pins over a tree `--check` redded by name. Measured on an
# isolated tree on 2026-08-25 — one whose ONLY problem was the blind sniffer, because every earlier
# probe reused a conf that raised two other problems and masked it. A claim of class coverage,
# written into the fix for the class of claims that are not true. Found by the round-2 review.
#
# THE DEAD SNIFFER ROW IS NOW IN THE LOOP, and each row names the text both modes must carry. A
# shared exit code of 1 for two different reasons is not agreement, and asserting the number alone
# cannot tell those apart.
ZZZ_STALE = "zzz_gone_symbol  a waiver whose target text is gone" + chr(10)
# A `def` split by a line continuation: `ast` parses it, and a line-anchored `def` sniff sees nothing
# on either line. That disagreement between extractor and sniffer IS the DEAD SNIFFER condition, and
# it is the only shape in this file that produces it.
BLIND_DEF = "def " + chr(92) + chr(10) + "build_thing():" + chr(10) + "    pass" + chr(10)
_AGREE = {"core/a.py": "def build_index():" + chr(10) + "    pass" + chr(10)}
for _label, _files, _waiv, _reason in (
        ("a clean tree", _AGREE, None, None),
        ("a STALE waiver", _AGREE, {"lexicon-verb-waivers.txt": ZZZ_STALE}, "STALE WAIVERS"),
        ("an UNDECLARED extension", {**_AGREE, "notes.R": "x <- 1" + chr(10)}, None,
         "UNDECLARED EXTENSIONS"),
        ("a DEAD SNIFFER", {**_AGREE, "core/blind.py": BLIND_DEF}, None, "DEAD SNIFFER"),
):
    _c, _co = run_case(_files, BASE_CONF, _waiv)
    _m, _mo = run_case(_files, BASE_CONF, _waiv, args=("--measure",))
    check(f"--measure and --check agree on the exit code over {_label}",
          (_c == 0) == (_m == 0), f"check={_c} measure={_m} | {_mo[:200]}")
    if _reason:
        check(f"...and both name the SAME reason over {_label}",
              _reason in _co and _reason in _mo,
              f"check={_reason in _co} measure={_reason in _mo} | {_mo[:200]}")

# ...and the agreement arms are only worth anything if the non-clean cases are NON-trivial: trees
# where both modes exit non-zero. Without this, every green row above could be the clean case. The
# fixture is `ZZZ_STALE`, the same object the loop uses — round 1 declared that constant and then
# hardcoded a DIFFERENT waiver string in the loop, so this arm certified a case the loop never ran.
_c, _ = run_case(_AGREE, BASE_CONF, {"lexicon-verb-waivers.txt": ZZZ_STALE})
_m, _ = run_case(_AGREE, BASE_CONF, {"lexicon-verb-waivers.txt": ZZZ_STALE}, args=("--measure",))
check("...and the stale-waiver case is a NON-trivial agreement (both non-zero)",
      _c != 0 and _m != 0, f"check={_c} measure={_m}")
_c, _ = run_case({**_AGREE, "core/blind.py": BLIND_DEF}, BASE_CONF)
_m, _ = run_case({**_AGREE, "core/blind.py": BLIND_DEF}, BASE_CONF, args=("--measure",))
check("...and the DEAD SNIFFER case is a NON-trivial agreement (both non-zero)",
      _c != 0 and _m != 0, f"check={_c} measure={_m}")

# ---- TOOL-aSurfacedLexicon-3 AC4: the two modes see ONE refusal set ------------------------------
#
# THE CLASS, not the three instances. `lexicon.py` confessed three separate times to a refusal
# written BELOW the `measure_mode` return: armed from `--check`, unreachable from `--measure`, so one
# mode could not fail while its sibling redded the same tree by name. Each was repaired by hoisting
# one `.append` above that return, which fixes an instance and leaves the next author one `return`
# away from re-earning it. `measure_pass` now computes every refusal before either mode branches, and
# THIS is the arm that fails if a later edit unpicks that.
#
# THE LIVE POPULATION OF THE DEFECT IS ZERO, so this arm was watched red against a STAGED break and
# not against the tree: a `problems.append` inserted into `run()`'s `--measure` branch, which made
# the two sets differ by one and redded both arms below by name.
#
# THE CHECK-SIDE REFUSAL SET IS DERIVED, never a list of refusal headers typed here — a hand-kept
# vocabulary of refusals is one fact in two places and goes stale on the next refusal added. `--check`
# prints its report lines and its refusals under ONE prefix, so its refusals are exactly what a
# CONTROL run over the same tree does not print. `--measure` prints its own under `#   `.
_CTRL = {"core/a.py": "def build_index():" + chr(10) + "    pass" + chr(10)}
_DIRTY = {**_CTRL, "notes.R": "x <- 1" + chr(10)}
_SETS = {}
_RCS = {}
for _tag, _files, _waiv in (("control", _CTRL, None),
                            ("dirty", _DIRTY, {"lexicon-verb-waivers.txt": ZZZ_STALE})):
    _cr, _cout = run_case(_files, BASE_CONF, _waiv)
    _mr, _mout = run_case(_files, BASE_CONF, _waiv, args=("--measure",))
    _RCS[_tag] = (_cr, _mr)
    _SETS[_tag] = (
        {ln[len("lexicon: "):] for ln in _cout.splitlines() if ln.startswith("lexicon: ")},
        {ln[4:] for ln in _mout.splitlines() if ln.startswith("#   ")},
    )
_check_refusals = _SETS["dirty"][0] - _SETS["control"][0]
_measure_refusals = _SETS["dirty"][1]
check("--check and --measure see ONE refusal set; a refusal only one mode can reach is the "
      "armed-but-unreachable class",
      _check_refusals == _measure_refusals,
      "only --check: " + str(sorted(_check_refusals - _measure_refusals))
      + "; only --measure: " + str(sorted(_measure_refusals - _check_refusals)))
# ...over a NON-EMPTY set naming BOTH staged refusals. Set equality over two empty sets is a fixture
# passing by finding nothing, and it is the shape this whole suite exists to refuse.
check("...over a non-empty set that names both refusals the fixture stages",
      len(_measure_refusals) == 2
      and any("STALE WAIVERS" in _r for _r in _measure_refusals)
      and any("UNDECLARED EXTENSIONS" in _r for _r in _measure_refusals),
      str(sorted(_measure_refusals)))
# ...and the CONTROL tree is clean in BOTH modes. Measured blind spot, not a hypothetical: the
# subtraction above cancels a refusal that fires on EVERY tree, so a `problems` entry appended inside
# `check_pass` alone was staged and this pair stayed green while twelve other arms redded. An exit
# code of 0 in each mode is the assertion that closes it, because `problems` non-empty forces 1 in
# both — so no refusal at all reached either mode on a tree the subtraction is about to trust.
check("...and the CONTROL tree those sets are measured against is clean in BOTH modes",
      _RCS["control"] == (0, 0), str(_RCS["control"]))

# H3 — every call of a function that can fail must be checked. `adopt-lexicon.sh` runs under `set -u`
# and NOT `-e`, so a bare call takes the next command's status: the --scaffold path printed
# "wrote .lexicon.conf" and exited 0 with no Skill on disk. Grepping the CALL SITES gates the shape
# for any mode added later, which a single-site fix does not.
# THE PREDICATE MATCHES A CALL ANYWHERE ON THE LINE, and the population it considered is asserted
# per function. Round 1 required the call at column 0 after stripping and excluded any line holding
# `$(` or `=`, which between them removed BOTH of `render_skill`'s real call sites -- they are
# `rendered="$(render_skill)"` -- and left exactly two `write_skill` lines, both already `||`-checked.
# Half the named population was structurally out of reach, and the sibling arm counted substring
# MENTIONS, which includes the definition, so it could not notice. The round-2 review reintroduced H3
# in full, as `[ -n "$CONF" ] && write_skill`, and watched the suite report 146 arms green.
_sh = (KIT / "adopt-lexicon.sh").read_text(encoding="utf-8")
_FNS = ("write_skill", "render_skill")
_seen = {_fn: 0 for _fn in _FNS}
_unchecked = []
for _i, _line in enumerate(_sh.splitlines(), 1):
    _t = _line.strip()
    if _t.startswith("#") or _t.startswith(("function ", "local ")):
        continue
    for _fn in _FNS:
        if _fn not in _t:
            continue
        # The DEFINITION is not a call. Matched by shape rather than by an exact trailing `() {`,
        # because `render_skill() { # -> stdout` carries a comment after the brace.
        if re.match(r"^(function\s+)?" + _fn + r"\s*\(\s*\)", _t):
            continue
        _seen[_fn] += 1
        # A call is STATUS-CHECKED when its own status is consumed: `||`, `&&`, an `if`/`while`
        # head, a `$(...)` capture whose assignment is checked on the next line, or an explicit
        # `return`/`exit` on the same line. `&&` BEFORE the call is the reintroduction shape the
        # review used -- it makes the call conditional and discards its status -- so a `&&` only
        # counts when it FOLLOWS the call.
        _pre, _, _post = _t.partition(_fn)
        _checked = ("||" in _post or "&&" in _post
                    or _pre.strip().startswith(("if ", "while ", "until ", "! "))
                    or "$(" in _pre)
        if not _checked:
            _unchecked.append(f"{_i}: {_t}")
check("every write_skill/render_skill CALL is status-checked (set -u, no -e)",
      not _unchecked, "; ".join(_unchecked))
# ...and the population is asserted PER FUNCTION. A zero for either name means the predicate never
# looked at it, which reads identically to a clean result and is the whole defect above.
for _fn in _FNS:
    check(f"...and the arm actually considered {_fn}'s call sites (or it proves nothing)",
          _seen[_fn] >= 2, f"{_fn}: {_seen[_fn]} line(s) considered")
# ...and the predicate must REJECT the exact reintroduction the review staged, or it is tuned to the
# current file rather than to the shape. Run over a synthetic line, not over the tracked script.
_BAD = '[ -n "$CONF" ] && write_skill'
_pre, _, _post = _BAD.partition("write_skill")
check("...and the predicate rejects a call made conditional by a PRECEDING &&",
      not ("||" in _post or "&&" in _post or "$(" in _pre), _BAD)

# ---- closing-review left-shifts (round 1, second batch) ------------------------------------------
#
# M4 + M5 — THE SUGGESTION IS GATED AS A CLASS, over a table of NAME SHAPES, not on the two names the
# review happened to try. Both defects were in the rejoin: `_fetch_conf` came back as `_load` with
# the object silently gone (the raw slice disagreed with `leading_verb` about where the verb starts),
# and `getUserData` came back as `read_UserData` (an underscore glued in front of a camelCase tail).
# Each row asserts the two properties a rename must preserve whatever the shape: every non-verb
# subtoken survives, and the separator style the caller wrote is the one they get back.
#
# EACH ROW NOW CARRIES ITS CELL, and the cell is the one whose convention the answer ALREADY
# satisfies (TOOL-aSurfacedLexicon-8). Every expected value below is byte-identical to what it was
# before `--as` existed, which is the point: a name that already satisfies its cell's convention must
# come back untouched, so these sixteen rows now gate the re-caser's do-nothing path as well as the
# swap's shape preservation. A row asked for a cell it does NOT satisfy is re-cased instead, and that
# is the table further down.
for _bad, _want, _cell in (
        ("fetch_remote", "load_remote", "py.function"),
        ("_fetch_conf", "_load_conf", "py.function"),
        ("__fetch_conf", "__load_conf", "py.function"),
        ("fetchRemoteThing", "loadRemoteThing", "js.function"),
        ("_fetchRemoteThing", "_loadRemoteThing", "js.function"),
        ("fetch", "load", "py.function"),
        ("_fetch", "_load", "py.function"),
        # The shapes the round-2 review measured, where rebuilding the tail from `subtokens()` lost
        # information the original surface carried. Each was CORRECT before round 1 touched it, or
        # correct in neither version; all are correct now because the tail is sliced, not rebuilt.
        ("fetch_v2_data", "load_v2_data", "py.function"),   # digit boundary: was `load_v_2_data`
        ("fetch_2fa", "load_2fa", "py.function"),           # digit boundary at the head of a token
        ("fetchXMLParser", "loadXMLParser", "js.function"),  # acronym run: was `loadXmlParser`
        ("fetchHTTPServerData", "loadHTTPServerData", "js.function"),
        # THESE THREE ASK A `function` CELL, and they used to ask a `type`, a `constant` and a
        # `file` one. Since closing review B2 the verb swap runs on the surface P1 grades and
        # nowhere else, which is what the GRADER does — `measure_vocab_cells` refuses a `vocab`
        # flag on any of those three surfaces by name, so the old rows were measured against a
        # declaration `--check` would have redded. The first two route through a `+prefix:`
        # selector, which buys the routing a live population here as a side effect; the third asks
        # a shell function cell, where a kebab name is legal shell and not a contrivance.
        ("FetchUserData", "LoadUserData", "py.function"),   # PascalCase: the verb inherits the case
        ("FETCH_USER_DATA", "LOAD_USER_DATA", "py.function"),   # SCREAMING_SNAKE, likewise
        ("fetch-user-data", "load-user-data", "sh.function"),   # kebab: the separator is the caller's
        ("fetch_conf_", "load_conf_", "py.function"),       # trailing underscore survives
        ("__fetch__", "__load__", "py.function"),           # ...on both ends
):
    _c, _o = run_case(_U10, SUGGEST_CONF, args=("--suggest", _bad, "--as", _cell))
    # EVERY ROW MUST ACTUALLY REACH THE REJOIN. `BASE_CONF` declares three verbs and bans exactly
    # one token, so a row naming any other off-table token gets "no row bans it by name" and its
    # negative sibling below would then pass by finding nothing -- this repo's own
    # `fixture-passes-by-finding-nothing` class, inside the fix for a different one. Asserting the
    # suggestion was PRODUCED is what stops that.
    # THE SWAP IS ASSERTED EXACTLY, as the first backticked token. Round 1 asserted `` `<want>` `` was
    # somewhere in the output, and the message template ALWAYS prints "the declaration says `load`",
    # so the row `("fetch", "load")` passed on the template rather than on the suggestion -- observed
    # by replacing the whole `swap` expression with a constant and watching that one row stay green.
    # L1's own class, reproduced inside the fix for L1. Found by the round-2 review.
    _got = _o.split("`")[1] if _o.startswith("use `") else "<no suggestion>"
    check(f"--suggest preserves shape and object: {_bad} --as {_cell} -> {_want}",
          _c == 0 and _got == _want, f"got {_got!r} | {_o}")

# The two arms that used to sit here are DELETED rather than repaired. Each asserted that a specific
# wrong spelling was absent from a line the row above had already pinned exactly, so neither could
# fail while its partner passed -- and both named forms the current code cannot produce at all, since
# they were spellings of an implementation that no longer exists. The round-2 review staged three
# separate defects and watched both stay green through all of them. An exact assertion on the swap
# makes an absence assertion beside it redundant by construction.

# M7 — ONE extension catalog, asserted by IDENTITY. The two copies had already diverged on the `py`
# pattern-set id inside a single build, which is what makes an equality assertion too weak here: a
# future re-fork that happens to start equal would pass it and drift on the next edit.
import scaffold_lexicon as _scaf  # noqa: E402
check("the scaffold and the engine share ONE extension catalog object",
      _scaf.KNOWN is lex.KNOWN_EXTS,
      f"scaffold={_scaf.KNOWN!r} engine={lex.KNOWN_EXTS!r}")
check("...and that catalog is non-empty, or the identity above holds vacuously",
      len(lex.KNOWN_EXTS) >= 2, repr(lex.KNOWN_EXTS))

# N1 — an unreadable KIT_LEXICON_VERSION must REFUSE, not render a version-less marker. The capture
# is a pipeline, and a pipeline takes its LAST command's status, so `head -1` succeeding on empty
# input is a zero: the emptiness has to be tested for. The round-2 review renamed the constant in a
# sandbox, watched `--render` succeed with `gov:kit lexicon@` and nothing after the `@`, and watched
# `--check` still report "Skill in sync" — because that gate re-renders and byte-compares, so both
# sides carried the same empty version. A drift gate cannot see a defect present in both operands.
# THE SANDBOX LIVES UNDER THE REPO ROOT, not under the system temp dir. This bash reaches the system
# temp dir under neither the drive-colon spelling nor the MSYS drive-prefix one -- both answer "No
# such file or directory" with exit 127 on a file python can stat -- and every one of those failures
# is NON-ZERO, so the refusal arm below would have passed on a broken invocation rather than on the
# version check. Its sibling caught that twice, which is why a refusal arm needs one. A path under
# the repo is one bash already resolves, since every other arm here runs scripts from it. Untracked,
# so no gate sees it, and `TemporaryDirectory` removes it on either outcome.
with tempfile.TemporaryDirectory(dir=str(KIT.parent.parent)) as _td:
    # A REAL REPO, because the script resolves its own kit-relative path with `git rev-parse` before
    # it reads the version and refuses with "not a git repo" otherwise -- a non-zero exit for the
    # wrong reason, which the sibling arm caught. The sandbox is shaped like an adopter: a git repo
    # with the kit under `tools/lexicon/` and no declaration, which is exactly where the version is
    # read and one step before any conf check.
    subprocess.run(["git", "init", "-q", "."], cwd=_td, capture_output=True)
    _kit = Path(_td) / "tools" / "lexicon"
    shutil.copytree(KIT, _kit, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    _lx = _kit / "lexicon.py"
    _lx.write_text(_lx.read_text(encoding="utf-8").replace("KIT_LEXICON_VERSION = ", "RENAMED_AWAY = "),
                   encoding="utf-8", newline=chr(10))
    # ...AND A VALID DECLARATION, so that removing the guard makes `--render` SUCCEED. Without one
    # the script refuses later for a missing conf, which is also non-zero -- so the refusal arm below
    # would pass with the guard deleted and could not independently fail. That is the same vacuity
    # class this round is fixing, reproduced inside the arm written to close it; observed by staging
    # the deletion and watching the arm stay green.
    (Path(_td) / ".lexicon.conf").write_text(BASE_CONF, encoding="utf-8", newline=chr(10))
    subprocess.run(["git", "add", "-A"], cwd=_td, capture_output=True)
    # THE MSYS DRIVE FORM, `/c/...`, not `C:/...`. Neither `str()` nor `.as_posix()` is enough: the
    # first gives bash `C:Users...` and the second gives it a path it answers "No such file or
    # directory" to with exit 127, even though python can stat the file. Both are NON-ZERO, so the
    # refusal arm above would have passed on a bash error rather than on the version check -- the
    # sibling arm below caught exactly that, twice, which is the whole reason a refusal arm needs one.
    _r = subprocess.run(["bash", "tools/lexicon/adopt-lexicon.sh", "--render"],
                        capture_output=True, text=True, cwd=_td)
    check("a kit whose version constant cannot be read REFUSES to render",
          _r.returncode != 0, f"exit={_r.returncode} {(_r.stdout + _r.stderr)[:200]}")
    check("...and says which file it could not read it from",
          "KIT_LEXICON_VERSION" in (_r.stdout + _r.stderr), (_r.stdout + _r.stderr)[:200])


# ---- TOOL-aSurfacedLexicon-4: the CELLS and PINS declaration grammar -----------------------------
#
# EVERY REFUSAL BELOW IS GATED AS A CLASS, over a table of row shapes, rather than on the one row
# that happened to be typed first. The reds are run through `load_conf` in-process because that is
# where the refusals live -- S5 and S10 put them at the tail of the READER, not in a verdict path,
# so all four consumers of this module inherit them and a conf-only commit reaches them on a leg
# with no guard. The two arms that go end to end through the engine are the ones whose criteria are
# written against `lexicon.py --check`.
import lexicon_conf as _lc  # noqa: E402

_CELLS_HEAD = BASE_CONF + "\nCELLS:\n"

# The GENERIC splitter, asserted directly: `<row-key> <rest>` on the first run of whitespace, with
# no alphabetic test. That missing test is the whole reason `py.function` can be written down now,
# and it is what a later PATTERNS or CANON block rides.
_rows = _lc._parse_rows([(5, "a.b  x y"), (7, "c")], Path("x"))
check("_parse_rows keeps a DOTTED row key and carries the line number",
      _rows == {"a.b": (5, "x y"), "c": (7, "")}, repr(_rows))

with build_tempdir() as _td:
    _cp = Path(_td) / "c.conf"

    # AC1 — the CELLS row parses, and `--print-rows CELLS` emits it.
    _cp.write_text(_CELLS_HEAD + "  py.function  snake vocab\n", encoding="utf-8", newline="\n")
    _c = _lc.load_conf(_cp)
    check("AC1: a CELLS row parses to (convention, flags)",
          _c["CELLS"] == {"py.function": ("snake", frozenset({"vocab"}))}, repr(_c.get("CELLS")))
    _r = subprocess.run([sys.executable, str(KIT / "lexicon_conf.py"), "--print-rows", "CELLS",
                         str(_cp)], capture_output=True, text=True)
    check("AC1: --print-rows CELLS prints the row",
          _r.returncode == 0 and _r.stdout.split() == ["py.function", "snake", "vocab"],
          f"rc={_r.returncode} {_r.stdout!r} {_r.stderr!r}")

    # AC9 — with NO block key it is byte-identical to what it printed before this unit, which is
    # what keeps `adopt-lexicon.sh`'s Skill render in sync.
    _r2 = subprocess.run([sys.executable, str(KIT / "lexicon_conf.py"), "--print-rows", str(_cp)],
                         capture_output=True, text=True)
    check("AC9: --print-rows with no block key still prints the VERBS rows",
          _r2.returncode == 0 and _r2.stdout.startswith("build\t") and "load\t" in _r2.stdout,
          f"rc={_r2.returncode} {_r2.stdout!r}")

    # AC3 + S3 + S4 — the row-grammar refusals, as a table.
    for _label, _body, _want in (
            ("an unknown surface", "CELLS:\n  py.frobnicate  snake\n", "unknown surface"),
            ("an unknown convention", "CELLS:\n  py.function  wiggly\n", "unknown convention"),
            ("`dot`, which is a classifier form", "CELLS:\n  py.function  dot\n",
             "not a declarable convention"),
            ("an unknown cell flag", "CELLS:\n  py.function  snake vocub\n", "unknown cell flag"),
            ("a key that is not <ext>.<surface>", "CELLS:\n  pyfunction  snake\n",
             "a CELLS row key is"),
            ("a row declaring no convention", "CELLS:\n  py.function\n", "declares no convention"),
            ("a duplicate row key", "CELLS:\n  py.function  snake\n\n  py.function  camel\n",
             "duplicate row key"),
            ("AC3: a non-integer pin count",
             "CELLS:\n  py.file  kebab\n\nPINS:\n  py.file.conv  seven\n",
             "must be a non-negative integer"),
            ("an unknown pin predicate",
             "CELLS:\n  py.file  kebab\n\nPINS:\n  py.file.frobbed  7\n",
             "unknown pin predicate"),
            ("a pin key that is not <ext>.<surface>.<predicate>",
             "CELLS:\n  py.file  kebab\n\nPINS:\n  py.file  7\n", "a PINS row key is"),
            ("AC2: a CELLS extension LANGS does not declare", "CELLS:\n  rs.function  snake\n",
             "which LANGS does not declare"),
            ("AC6: a PINS row whose cell has no CELLS row",
             "CELLS:\n  py.file  kebab\n\nPINS:\n  py.function.debt  3\n", "which has no CELLS row"),
            ("S10: two PINS rows on consecutive lines",
             "CELLS:\n  py.file  kebab\n\n  py.function  snake\n\n"
             "PINS:\n  py.file.conv  7\n  py.function.debt  3\n", "are adjacent"),
    ):
        _cp.write_text(BASE_CONF + "\n" + _body, encoding="utf-8", newline="\n")
        try:
            _lc.load_conf(_cp)
            _msg = "<NO REFUSAL>"
        except _lc.ConfError as _e:
            _msg = str(_e)
        check(f"grammar red: {_label}", _want in _msg, _msg)

    # THE CROSS-BLOCK REFUSALS NAME THE LINE, not just the file. They run after every parsed value
    # shape has dropped its line number, so these two were the only ROW-LEVEL refusals in this module
    # printing a bare filename while every other one printed a position.
    # The expected line is DERIVED from the row's real position in the text just written, so an
    # implementation that hardcodes a number, or that reports the block header instead of the row,
    # cannot pass this.
    for _label, _body, _row in (
            ("a CELLS extension LANGS does not declare",
             "CELLS:\n  rs.function  snake\n", "rs.function  snake"),
            ("a PINS row whose cell has no CELLS row",
             "CELLS:\n  py.file  kebab\n\nPINS:\n  py.function.debt  3\n", "py.function.debt  3"),
    ):
        _text = BASE_CONF + "\n" + _body
        _cp.write_text(_text, encoding="utf-8", newline="\n")
        _want_ln = [i for i, l in enumerate(_text.splitlines(), 1) if l.strip() == _row][0]
        try:
            _lc.load_conf(_cp)
            _msg = "<NO REFUSAL>"
        except _lc.ConfError as _e:
            _msg = str(_e)
        check(f"the refusal for {_label} names the ROW's line, not just the file",
              f":{_want_ln}:" in _msg, f"want line {_want_ln} in: {_msg}")

    # THE DISPATCH IS THE GUARD. `_BLOCK_PARSERS.get(key, _parse_rows)` sat under a membership test
    # against `BLOCK_KEYS` that had already raised for every key outside it, so the default could not
    # be taken by any input — dead code reading as a safety net, and one that would have parsed an
    # unvalidated block silently had it ever been reachable. Guarding on the parser table instead
    # makes the state observable: a key listed as a block with no parser written is now a named
    # refusal. Monkeypatched, because no declaration a user can write reaches it.
    _saved_keys = _lc.BLOCK_KEYS
    try:
        _lc.BLOCK_KEYS = _saved_keys + ("FROBS",)
        _cp.write_text(BASE_CONF + "\nFROBS:\n  a b\n", encoding="utf-8", newline="\n")
        try:
            _lc.load_conf(_cp)
            _msg = "<NO REFUSAL>"
        except _lc.ConfError as _e:
            _msg = str(_e)
        check("a block key with NO parser refuses by name rather than falling back to a generic one",
              "no block parser for 'FROBS'" in _msg, _msg)
    finally:
        _lc.BLOCK_KEYS = _saved_keys

    # The GREEN counterparts, so none of the reds above is passing because everything reds.
    _cp.write_text(BASE_CONF + "\nCELLS:\n  py.file  kebab\n\n  py.function  snake vocab\n\n"
                              "PINS:\n  py.file.conv  7\n\n  py.function.debt  0\n",
                   encoding="utf-8", newline="\n")
    _c = _lc.load_conf(_cp)
    check("AC3 green: a PINS count parses to the INTEGER, not the string",
          _c["PINS"] == {"py.file.conv": 7, "py.function.debt": 0}, repr(_c.get("PINS")))
    check("S10 green: blank-separated PINS rows parse", len(_c["CELLS"]) == 2, repr(_c["CELLS"]))

    # ...and a comment line separates two rows just as well, because the block scanner drops `#`
    # rows while still advancing the line counter. Without this arm the refusal would be a ban on
    # commenting a pin row rather than a merge property.
    _cp.write_text(BASE_CONF + "\nCELLS:\n  py.file  kebab\n\n  py.function  snake\n\n"
                              "PINS:\n  py.file.conv  7\n  # drained by TOOL-x-1\n"
                              "  py.function.debt  0\n", encoding="utf-8", newline="\n")
    check("S10 green: a COMMENT line separates two pin rows too",
          _lc.load_conf(_cp)["PINS"] == {"py.file.conv": 7, "py.function.debt": 0}, "")

    # AC4 — the regression arm on widening BLOCK_KEYS: an unlisted header must still refuse.
    _cp.write_text(BASE_CONF + "\nFOO:\n  bar baz\n", encoding="utf-8", newline="\n")
    try:
        _lc.load_conf(_cp)
        _msg = "<NO REFUSAL>"
    except _lc.ConfError as _e:
        _msg = str(_e)
    check("AC4: an unknown block header still refuses after BLOCK_KEYS widened",
          "'FOO:'" in _msg, _msg)

    # A declaration written BEFORE these blocks existed parses exactly as it did: an absent block
    # resolves to its empty container rather than to a refusal.
    _cp.write_text(BASE_CONF, encoding="utf-8", newline="\n")
    _c = _lc.load_conf(_cp)
    check("migration: a conf with no CELLS/PINS parses, both empty",
          _c["CELLS"] == {} and _c["PINS"] == {}, repr((_c.get("CELLS"), _c.get("PINS"))))

    # ---- the reader's remaining unarmed refusals -------------------------------------------------
    #
    # A REVERT SWEEP FOUND EACH OF THESE GREEN WITH ITS `raise` REMOVED. Every needle below names
    # the offending TOKEN as well as the rule, because this module also refuses a non-alphabetic
    # CANON representative and a non-alphabetic CANON alternative: an arm matching only
    # "alphabetic", or only "LANGS", cannot tell which refusal fired.

    # The unreadable declaration. It is the one refusal here with no line to name, so the arm asserts
    # the FILE instead — a message that dropped the path would leave the reader saying only that
    # something, somewhere, could not be read.
    _missing = Path(_td) / "no-such-declaration.conf"
    try:
        _lc.load_conf(_missing)
        _msg = "<NO REFUSAL>"
    except _lc.ConfError as _e:
        _msg = str(_e)
    check("reader red: an unreadable declaration refuses, naming the file it could not read",
          "cannot read" in _msg and "no-such-declaration.conf" in _msg, _msg)

    # A non-alphabetic VERBS key. The verb table is a CLOSED set of words the corpus is graded
    # against; a row keyed `b3ild` would enter that set and grade names by a token no gloss can
    # define. `_parse_verbs` splits its own rows, so this red is appended INSIDE the VERBS block
    # rather than added as a second one.
    _cp.write_text(BASE_CONF + "  b3ild   not a word — NOT `build`\n", encoding="utf-8",
                   newline="\n")
    try:
        _lc.load_conf(_cp)
        _msg = "<NO REFUSAL>"
    except _lc.ConfError as _e:
        _msg = str(_e)
    check("reader red: a non-alphabetic VERBS key refuses as a VERB, naming the token",
          "a verb must be alphabetic" in _msg and "'b3ild'" in _msg, _msg)
    check("reader red: ...and is NOT the CANON refusal, which says the same word",
          "CANON" not in _msg, _msg)

    # The two PATTERNS row-key halves, each refused by its own rule. Both rows are otherwise
    # well-formed — one capturing group, a compilable regex — so the only thing either arm can be
    # observing is the key check it is named for.
    # The last two rows were not on the sweep's list; they sit one and four lines from the two that
    # were, in the same parser, and were unarmed for the same reason. Each `_want` names its BLOCK,
    # because `CELLS` and `PINS` refuse a bad row key and an empty value with sentences of the same
    # shape and an arm matching only "row key is" cannot tell the three apart.
    for _label, _row, _want in (
            ("a pattern-set id outside `[A-Za-z0-9_-]+`", r"  b@d.functions  ^\s*fn\s+(\w+)",
             "pattern-set id 'b@d'"),
            ("an extractor part outside the closed set", r"  ts-regex.frobs  ^\s*fn\s+(\w+)",
             "unknown extractor part 'frobs'"),
            ("a row key that is not <pattern-set-id>.<part>", r"  functions  ^\s*fn\s+(\w+)",
             "a PATTERNS row key is"),
            ("a row declaring no regex at all", "  ts-regex.functions",
             "PATTERNS row 'ts-regex.functions' declares no regex"),
    ):
        _cp.write_text(BASE_CONF + "\nPATTERNS:\n" + _row + "\n", encoding="utf-8", newline="\n")
        try:
            _lc.load_conf(_cp)
            _msg = "<NO REFUSAL>"
        except _lc.ConfError as _e:
            _msg = str(_e)
        except Exception as _e:  # noqa: BLE001 — see the LANGS arms below for why this is caught
            _msg = f"<{type(_e).__name__} instead of ConfError: {_e}>"
        check(f"reader red: {_label} refuses, naming the offending part of the row",
              _want in _msg, _msg)

# The `LANGS` refusals, called directly. `check_declaration` only reaches `langs()` when a CELLS
# block exists, so a declaration carrying neither would carry a malformed LANGS all the way to the
# engine's dispatcher — and an unrecognised MODE arriving there is a coverage claim nobody made:
# `parser`, `probe` and `dark` mean three different things about what a green run proves, and a
# fourth word means none of them while still reporting a clean scan.
for _label, _langs, _want in (
        ("a LANGS entry that is not <ext>:<pattern-set-id>:<mode>", "py:python-ast",
         "LANGS entry must be"),
        ("a LANGS entry carrying a FOURTH field", "py:python-ast:parser:extra",
         "LANGS entry must be"),
        ("an unrecognised LANGS mode", "py:python-ast:skim", "LANGS mode must be"),
):
    # ANY exception that is not a ConfError is caught and scored as a FAILED arm rather than left to
    # propagate. Removing the first refusal below does not make `langs` permissive — it makes the
    # very next line unpack a two-element list into three names — and an unhandled ValueError would
    # red this suite with a traceback naming a line in the reader instead of the arm that knows
    # which refusal went missing.
    try:
        _lc.langs({"LANGS": _langs})
        _msg = "<NO REFUSAL>"
    except _lc.ConfError as _e:
        _msg = str(_e)
    except Exception as _e:  # noqa: BLE001
        _msg = f"<{type(_e).__name__} instead of ConfError: {_e}>"
    check(f"reader red: {_label} refuses, naming the offending entry",
          _want in _msg and repr(_langs) in _msg, _msg)

# ...and the green counterpart, so none of the three above is passing because `langs` reds on
# everything. `dark` with an empty pattern-set id is the shape the reds must not have swallowed.
check("LANGS green: a well-formed declaration still parses to its triples",
      _lc.langs({"LANGS": "py:python-ast:parser conf::dark"})
      == [("py", "python-ast", "parser"), ("conf", "", "dark")],
      repr(_lc.langs({"LANGS": "py:python-ast:parser conf::dark"})))

# AC2 + AC6 END TO END, through the engine rather than through the reader, because those two
# criteria are written against `lexicon.py --check`.
code, out = run_case({"core/a.py": "def build_index():\n    pass\n"},
                     BASE_CONF + "\nCELLS:\n  rs.function  snake\n")
check("AC2: an undeclared CELLS extension reds --check by name",
      code != 0 and "rs" in out and "LANGS does not declare" in out, out)
code, out = run_case({"core/a.py": "def build_index():\n    pass\n"},
                     BASE_CONF + "\nCELLS:\n  py.function  snake\n")
check("AC2 green: ...and it greens once LANGS declares it", code == 0, out)

code, out = run_case({"core/a.py": "def build_index():\n    pass\n"},
                     BASE_CONF + "\nCELLS:\n  py.file  kebab\n\nPINS:\n  py.function.conv  0\n")
check("AC6: a PINS row with no CELLS row reds --check by cell",
      code != 0 and "py.function" in out and "has no CELLS row" in out, out)
code, out = run_case({"core/a.py": "def build_index():\n    pass\n"},
                     BASE_CONF + "\nCELLS:\n  py.file  kebab\n\n  py.function  snake\n\n"
                                 "PINS:\n  py.function.conv  0\n")
check("AC6 green: ...and it greens once the CELLS row is added", code == 0, out)

# ---- AC10: the pin is a TWO-SIDED equality ------------------------------------------------------
# One offender in the fixture corpus. The pin is walked one step in each direction, and BOTH steps
# must red: a count that FALLS was silent before this unit, which is how a pin sits eleven moves
# above a corpus that already drained under it.
_U4 = {"core/a.py": "def frobnicate_index():\n    pass\n"}
code, out = run_case(_U4, BASE_CONF.replace('VERB_OFFENDER_PIN="0"', 'VERB_OFFENDER_PIN="1"'))
check("AC10 control: offenders == pin is green", code == 0, out)
code, out = run_case(_U4, BASE_CONF.replace('VERB_OFFENDER_PIN="0"', 'VERB_OFFENDER_PIN="0"'))
check("AC10 rise: a count ABOVE the pin reds and names the offenders",
      code != 0 and "over pin 0" in out and "frobnicate_index" in out, out)
code, out = run_case(_U4, BASE_CONF.replace('VERB_OFFENDER_PIN="0"', 'VERB_OFFENDER_PIN="2"'))
check("AC10 fall: a count BELOW the pin reds too",
      code != 0 and "UNDER pin 2" in out, out)
check("AC10 fall: ...and prints the exact replacement row to paste",
      'VERB_OFFENDER_PIN="1"' in out, out)

# ---- AC5: two branches draining DIFFERENT pin rows merge clean ----------------------------------
# The property fork F1 ratified option (c) for. It is a standing arm that performs the merge, not a
# one-time measurement -- but its INPUT is a block this arm writes, so it merges clean however dense
# the tracked declaration becomes and it can never observe a later tidying edit. That hazard is
# S10's refusal above, over the tracked file, on a leg with no guard.
with build_tempdir() as _td:
    _r = Path(_td)
    _base = ("CELLS:\n"
             "  py.file  kebab\n\n  py.function  snake\n\n  py.type  pascal\n\n"
             "PINS:\n"
             "  py.file.conv  7\n\n  py.function.debt  9\n\n  py.type.conv  4\n")
    _cf = _r / ".lexicon.conf"
    _cf.write_text(_base, encoding="utf-8", newline="\n")
    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=_r, check=True, capture_output=True)
    for _k, _v in (("user.email", "s@e"), ("user.name", "s")):
        subprocess.run(["git", "config", _k, _v], cwd=_r, check=True, capture_output=True)
    subprocess.run(["git", "add", "-A"], cwd=_r, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-qm", "base"], cwd=_r, check=True, capture_output=True)
    # ADJACENT CELLS -- the likeliest concurrent pair, because related cells sit together, and the
    # pair a dense block conflicts on.
    for _br, _old, _new in (("drainA", "py.file.conv  7", "py.file.conv  6"),
                            ("drainB", "py.function.debt  9", "py.function.debt  8")):
        subprocess.run(["git", "checkout", "-q", "-b", _br, "main"], cwd=_r, check=True,
                       capture_output=True)
        _cf.write_text(_base.replace(_old, _new), encoding="utf-8", newline="\n")
        subprocess.run(["git", "commit", "-qam", _br], cwd=_r, check=True, capture_output=True)
    subprocess.run(["git", "checkout", "-q", "drainA"], cwd=_r, check=True, capture_output=True)
    _m = subprocess.run(["git", "merge", "--no-edit", "drainB"], cwd=_r, capture_output=True,
                        text=True)
    _merged = _cf.read_text(encoding="utf-8")
    check("AC5: two branches draining ADJACENT cells merge with no conflict",
          _m.returncode == 0 and "<<<<<<<" not in _merged,
          f"rc={_m.returncode} {_m.stdout}{_m.stderr}")
    check("AC5: ...and BOTH drains survive the merge",
          "py.file.conv  6" in _merged and "py.function.debt  8" in _merged, _merged)

# ---- TOOL-aSurfacedLexicon-5: the convention predicate -------------------------------------------
#
# THE FORM TABLE IS GATED AS A TABLE, not on the one spelling that happened to be typed first, and
# every row carries a NEGATIVE. A form asserted only by what it matches cannot be told apart from a
# looser form that also matches it — `^[a-z].*$` passes every positive `snake` row in this block and
# is not snake. The negatives are the whole predicate.
from subtokens import check_convention, classify, read_core, read_stem  # noqa: E402

for _form, _yes, _no in (
        ("snake", ("build_index", "run", "x2"), ("buildIndex", "Build_Index")),
        ("screaming", ("PIN_KEYS", "RUN"), ("Pin_Keys", "pin_keys")),
        ("camel", ("buildIndex", "run"), ("BuildIndex", "build_index")),
        ("pascal", ("BuildIndex", "Run"), ("buildIndex", "Build_Index")),
        ("kebab", ("check-arms", "run"), ("checkArms", "check_arms")),
        ("dot", ("gate.legs", "run"), ("Gate.Legs", "gate_legs")),
):
    for _n in _yes:
        check(f"form {_form} matches {_n}", _form in classify(_n), repr(sorted(classify(_n))))
    for _n in _no:
        check(f"form {_form} does NOT match {_n}", _form not in classify(_n),
              repr(sorted(classify(_n))))

# AC8 — the SET contract at the seam, not only through the report. `run` satisfying four forms at
# once is the whole reason `classify` returns a set: a single-label classifier would have to pick one
# and report a violation against the other three.
check("AC8: classify('run') is set-valued and holds snake, camel and kebab",
      {"snake", "camel", "kebab"} <= classify("run"), repr(sorted(classify("run"))))
check("AC8: classify('_build_index') strips the affix and holds snake",
      "snake" in classify("_build_index"), repr(sorted(classify("_build_index"))))
check("the affix strip is why: without it __init__ would be a snake violation",
      "snake" in classify("__init__") and read_core("__init__") == "init", read_core("__init__"))

# S6 — the stem splits at the FIRST dot. The last-dot alternative is what would red every compound
# extension in the tree, so the arm asserts the property rather than one filename.
for _base, _stem in (("map_extractors.template.py", "map_extractors"),
                     ("check-arms.test.sh", "check-arms"),
                     ("plain", "plain"),
                     (".gitignore", "")):
    check(f"read_stem({_base!r}) is {_stem!r}", read_stem(_base) == _stem, read_stem(_base))

# AC10 second arm — the empty core, called directly. `def _():` is legal Python and the classifier
# has nothing to grade, which is AMBIGUOUS and not a skip. Its in-corpus population is NOT zero: nine
# tracked files in this repo have a dot-leading basename and therefore an empty first-dot stem, so
# the same verdict fires on a filename the day one of those cells is armed.
check("AC10: read_core('_') is the empty string", read_core("_") == "", repr(read_core("_")))
check("AC10: an EMPTY core is AMBIGUOUS, not a fall-through that prints nothing",
      check_convention("_", "snake")[0] == "AMBIGUOUS", repr(check_convention("_", "snake")))
check("AC5: a NON-empty core satisfying nothing is AMBIGUOUS too",
      check_convention("FAMILY_of", "snake")[0] == "AMBIGUOUS",
      repr(check_convention("FAMILY_of", "snake")))
check("AMBIGUOUS never says VIOLATION", "VIOLATION" not in check_convention("_", "snake")[1])
check("a VIOLATION names what the name DOES satisfy",
      check_convention("loadUserData", "snake") == (
          "VIOLATION", "VIOLATION  loadUserData  satisfies camel, not snake"),
      repr(check_convention("loadUserData", "snake")))
# ...and it names ALL of them, comma-joined and sorted. FOUND BY STAGING THE BREAK: with only the
# single-form `loadUserData` and `user_record` arms above, replacing the join with `sorted(forms)[0]`
# left this whole file GREEN — a message arm that cannot fail on the one input shape it exists for.
check("a VIOLATION names EVERY form the name satisfies, not just the first",
      check_convention("run", "pascal") == (
          "VIOLATION", "VIOLATION  run  satisfies camel, dot, kebab, snake, not pascal"),
      repr(check_convention("run", "pascal")))
check("SATISFIED is membership, NOT being the set's only member",
      check_convention("run", "kebab")[0] == "SATISFIED" and len(classify("run")) > 1,
      repr(sorted(classify("run"))))

# END TO END through the engine, which is where AC1, AC2, AC5 and AC10 are written.
_CELL_PY = BASE_CONF + "\nCELLS:\n  py.function  snake\n\n  py.type  pascal\n"
_CLEAN = {"core/a.py": "def build_index():\n    pass\n\n\nclass BuildIndex:\n    pass\n"}
code, out = run_case(_CLEAN, _CELL_PY)
check("cells green: a conforming corpus passes both cells", code == 0, out)
check("...and the row is printed on GREEN with its population",
      "py.function.conv 0 of 1" in out and "py.type.conv 0 of 1" in out, out)

code, out = run_case({"core/a.py": "def loadUserData():\n    pass\n"}, _CELL_PY)
check("AC1: a camelCase function reds a snake cell",
      code != 0 and "VIOLATION  loadUserData  satisfies camel, not snake" in out, out)
code, out = run_case({"core/a.py": "class user_record:\n    pass\n"}, _CELL_PY)
check("AC2: a snake_case class reds a pascal cell",
      code != 0 and "VIOLATION  user_record  satisfies snake, not pascal" in out, out)
code, out = run_case({"core/a.py": "def FAMILY_of():\n    pass\n"}, _CELL_PY)
check("AC5: a name satisfying NO form reds as AMBIGUOUS",
      code != 0 and "AMBIGUOUS  FAMILY_of" in out, out)
code, out = run_case({"core/a.py": "def _():\n    pass\n"}, _CELL_PY)
check("AC10: an EMPTY core reds as AMBIGUOUS through the engine",
      code != 0 and "AMBIGUOUS  _ " in out, out)
check("AC10: ...and NOT as a VIOLATION, and NOT by printing nothing",
      "VIOLATION" not in out and "py.function.conv 1 of 1" in out, out)

# The FILE cell, and with it the dot-leading basename. `run_case` writes `.lexicon.conf` into the
# fixture and stages it, so the fixture's own declaration IS the empty-stem instance — the same shape
# as this repo's nine tracked dotfiles, exercised rather than described.
code, out = run_case(_CLEAN, BASE_CONF + "\nCELLS:\n  conf.file  kebab\n")
check("a dot-leading basename stems to nothing and reds AMBIGUOUS on a file cell",
      code != 0 and ".lexicon.conf" in out and "AMBIGUOUS" in out, out)
code, out = run_case({**_CLEAN, "core/loadUser.py": "def build_x():\n    pass\n"},
                     BASE_CONF + "\nCELLS:\n  py.file  snake\n")
check("a file cell grades the BASENAME, not the path",
      code != 0 and "VIOLATION  loadUser  satisfies camel, not snake" in out, out)

# AC6 — the TEETH, observed as the printed line rather than as the figure behind it. A cell that
# prints a violation count and nothing else is indistinguishable from a cell that cannot fail, so
# the arm is a predicate over every `.conv` row in the output. It is staged against a copy of that
# output with the teeth clause deleted, because a predicate nobody has seen fail is an assertion
# about nothing.
_conv_rows = [ln for ln in out.splitlines() if ".conv " in ln and " of " in ln]
_teeth_ok = bool(_conv_rows) and all(" teeth " in ln for ln in _conv_rows)
check("AC6: every armed cell row carries a teeth figure beside its count", _teeth_ok,
      repr(_conv_rows))
_stripped = [ln.split(" teeth ")[0] for ln in _conv_rows]
check("AC6: ...and that same predicate REDS on a row with the teeth clause removed",
      not all(" teeth " in ln for ln in _stripped), repr(_stripped))

code, out = run_case(_CLEAN, BASE_CONF + "\nCELLS:\n  py.function  camel\n")
check("AC6: the teeth report what the OTHER conventions would fail",
      "teeth" in out and "camel=" not in out.split("teeth")[1].split("\n")[0], out)

# ---- TOOL-aSurfacedLexicon-6: the cell refusals and the per-cell population report ---------------
#
# The `constant` surface now HAS a population rule, so the arm that used to assert it announced
# itself as UNEXERCISED is retired here rather than left asserting an absence this unit filled.
_CONSTS = {"core/a.py": "PUBLIC_ONE = 1\n_private = 2\nA, B = 3, 4\n_d = {}\n_d['k'] = 5\n"
                        "TYPED: int = 6\n\n\ndef build_x():\n    LOCAL_ONLY = 7\n    return LOCAL_ONLY\n"}
code, out = run_case(_CONSTS, BASE_CONF + "\nCELLS:\n  py.constant  screaming\n  py.function  dark\n")
check("S5: a constant cell grades the PUBLIC SIMPLE targets and narrows from every bound target",
      code == 0 and "py.constant.conv 0 of 2" in out and "population 2 of 6" in out, out)
check("S5: ...and it names its population RULE beside the count",
      "(rule: public simple module-body assignments)" in out, out)

# The counting rule is the load-bearing half, so each clause of it gets an arm rather than the
# aggregate alone. `d['k'] = 5` binds nothing, `_private` and the tuple targets are excluded from
# the GRADED population but counted in the denominator, and a function-body assignment is invisible.
code, out = run_case({"core/a.py": "D = {}\nD['k'] = 1\nD.attr = 2\n"},
                     BASE_CONF + "\nCELLS:\n  py.constant  screaming\n")
check("S5: a subscript or attribute target binds no name and is not counted",
      "population 1 of 1" in out, out)
code, out = run_case({"core/a.py": "loadUser = 1\n"},
                     BASE_CONF + "\nCELLS:\n  py.constant  screaming\n")
check("AC9: a public module-body assignment that is not SCREAMING reds the constant cell",
      code != 0 and "VIOLATION  loadUser  satisfies camel, not screaming" in out, out)

# AC1 / S2 — DEAD CELL. An armed cell whose population rule selects NOTHING is a refusal now; the
# shipped tree printed that same fact as a report for the whole life of the declaration and nothing
# ever acted on it.
_NOTYPES = {"core/a.py": "def build_x():\n    pass\n"}
code, out = run_case(_NOTYPES, BASE_CONF + "\nCELLS:\n  py.type  pascal\n")
check("AC1: an armed cell with a ZERO population reds as DEAD CELL",
      code != 0 and "DEAD CELL — `py.type`" in out, out)
check("AC1: ...and the refusal names the population RULE that selected nothing",
      "every extracted type definition" in out, out)
code, out = run_case(_NOTYPES, BASE_CONF)
check("AC1 green: ...and with the row removed the same corpus exits 0", code == 0, out)

# A `dark` row is EXEMPT by construction: its population is zero because nothing extracts it, and
# redding it would make the honest declaration the failing one. Staged against the arm above, which
# reds the identical corpus one convention away.
code, out = run_case(_NOTYPES, BASE_CONF + "\nCELLS:\n  py.type  dark\n  py.function  dark\n")
check("AC1: a DARK cell at zero population is exempt from DEAD CELL",
      code == 0 and "DEAD CELL — " not in out and "py.type.conv dark" in out, out)

# The other exemption, and it is why the INERT DECLARATION report one arm over still means what it
# says: an extension the corpus carries NO file of cannot prove a cell dead. `ts` is declared and
# this fixture writes no `.ts` file at all.
_TSCONF = BASE_CONF.replace('LANGS="py:python-ast:parser conf::dark"',
                            'LANGS="py:python-ast:parser ts:ts-regex:probe conf::dark"')
code, out = run_case(_CLEAN, _TSCONF + "\nCELLS:\n  ts.function  camel\n"
                     "  py.function  dark\n  py.type  dark\n"
                     "\nPATTERNS:\n  ts-regex.functions  ^fn ([a-z]+)\n")
check("AC1: a cell on an INERT extension is exempt from DEAD CELL, like its sibling report",
      code == 0 and "DEAD CELL — " not in out and "INERT DECLARATION" in out, out)

# AC7 — DEAD PROBE is NOT subsumed. It sees an armed EXTENSION with no definitions at all, which is
# a population no CELLS row need exist for; fork F1 keeps both and this arm is what proves the newer
# refusal did not quietly replace the older one.
code, out = run_case({"core/a.py": "X = 1\n"}, BASE_CONF + "\nCELLS:\n  py.constant  screaming\n")
check("AC7: DEAD PROBE still fires beside DEAD CELL, on a population DEAD CELL cannot see",
      code != 0 and "DEAD PROBE" in out and "DEAD CELL — " not in out, out)

# AC3 / AC6 / S7 — THE REPORT'S LIVENESS. One printed row per parsed CELLS row, dark included, and
# the parity is asserted against the declaration rather than against a number typed here.
_THREE = (BASE_CONF + "\nCELLS:\n  py.function  snake\n\n  py.type  dark\n\n"
          "  py.constant  screaming\n")
code, out = run_case(_CONSTS, _THREE)
# The pin-replacement line carries `.conv ` too, so the row filter is the same discriminator the
# teeth arm above uses: a REPORT row is the one carrying a population, `N of M`.
_rows = [ln for ln in out.splitlines()
         if ln.startswith("lexicon: ") and ".conv " in ln and " of " in ln]
check("AC3: the report prints one row per CELLS row, dark rows included",
      code == 0 and len(_rows) == 3, f"{code}: {_rows}")

# AC4 — every printed row carries its rule, staged against a copy of the same output with the clause
# deleted, because a predicate nobody has seen fail is an assertion about nothing.
check("AC4: every printed cell row carries a population rule beside its count",
      bool(_rows) and all("(rule: " in ln for ln in _rows), repr(_rows))
check("AC4: ...and that same predicate REDS on a row with the rule clause removed",
      not all("(rule: " in ln.split(" (rule: ")[0] for ln in _rows),
      repr([ln.split(" (rule: ")[0] for ln in _rows]))

# AC6 — the row source emptied from INSIDE the engine. A declaration with rows whose report builds
# none is the empty table under a green line this assertion exists to make impossible.
code, out = run_case(_CONSTS, _THREE,
                     patch=('    cells = conf.get("CELLS") or {}', "    cells = {}"))
check("AC6: a report that builds NO rows against a non-empty declaration REFUSES",
      code != 0 and "DEAD CELL REPORT" in out and "carries 3 CELLS row(s)" in out, out)
code, out = run_case(_CONSTS, _THREE,
                     patch=("    for cell in order:\n", "    for cell in order[1:]:\n"))
check("AC6: ...and so does a report that drops ONE row while printing the others",
      code != 0 and "DEAD CELL REPORT" in out and "the report built 2" in out, out)

# S7's OWN BOUNDARY, stated as an arm rather than as prose: a declaration carrying no CELLS block is
# a legal inert state and must NOT red, or every tree that installed this kit before the block
# existed reds on upgrade.
code, out = run_case(_CLEAN, BASE_CONF)
check("S7: a declaration with NO CELLS block is inert, not a DEAD CELL REPORT",
      code == 0 and "DEAD CELL REPORT" not in out, out)

# A declarable surface with no population rule is a REFUSAL, not a skip. Staged by deleting the rule
# row from the copied engine, which is the only way to reach a state the closed sets forbid.
code, out = run_case(_CONSTS, BASE_CONF + "\nCELLS:\n  py.constant  screaming\n",
                     patch=('    "constant": (scan_module_constants, '
                            '"public simple module-body assignments"),\n', ""))
check("a declarable surface carrying no population rule REDS as UNRULED SURFACE",
      code != 0 and "UNRULED SURFACE" in out and "py.constant" in out, out)

# AC2 / S1 — UNDECLARED CELL. It landed REPORT-ONLY behind a default-OFF constant and
# TOOL-aSurfacedLexicon-12 ARMED it with the full matrix, so the two halves swapped which one needs
# staging: the refusal is now the shipped behaviour and runs unpatched, and the report-only half is
# reached by patching the constant back OFF. Both are still observed, which is the whole point of
# writing them as a pair — an arm that only ever saw one of them proves nothing about the other.
_JS = BASE_CONF.replace('LANGS="py:python-ast:parser conf::dark"',
                        'LANGS="py:python-ast:parser js:js-regex:probe conf::dark"')
_MATRIX = (_JS + "\nCELLS:\n  py.function  snake\n\n  py.type  pascal\n\n  js.function  camel\n")
_JSFILES = {**_CLEAN, "web/a.js": "function loadThing() {}\n"}
code, out = run_case(_JSFILES, _MATRIX)
check("AC2 green: a complete matrix over the extracted space names no undeclared cell",
      code == 0 and "UNDECLARED CELL — 0 extracted population(s)" in out, out)
code, out = run_case({**_JSFILES, "web/b.js": "class Cap {}\n"}, _MATRIX)
check("AC2: an extracted population with no CELLS row REFUSES, naming js.type",
      code != 0 and "UNDECLARED CELL (an extracted population" in out and "js.type at 1" in out,
      out)
check("AC2: ...and the report states what it does NOT check",
      "NOT CHECKED by that list — the `file` and `constant` surfaces" in out, out)
code, out = run_case({**_JSFILES, "web/b.js": "class Cap {}\n"}, _MATRIX,
                     patch=("UNDECLARED_CELL_ARMED = True", "UNDECLARED_CELL_ARMED = False"))
check("AC2: ...and with the promotion constant forced back OFF it only REPORTS",
      code == 0 and "js.type at 1" in out and "[reported, not a refusal]" in out, out)

# THE ARMED REFUSAL'S OWN BOUNDARY, and it is the same one the DEAD CELL REPORT arm above draws: a
# declaration carrying NO `CELLS` block is a legal inert state and must not red, or arming this
# promotes every adopter that installed the kit before cells existed straight to a broken bar. The
# pair is what makes it a boundary rather than a hole — the same corpus reds the moment ONE cell is
# declared, because from there the matrix is the owner's and an incomplete one is a real gap.
# TOOL-aSurfacedLexicon-12.
code, out = run_case(_JSFILES, _JS)
check("a declaration with NO CELLS block does not fire the armed UNDECLARED CELL refusal",
      code == 0 and "py.function at 1" in out and "[reported, not a refusal]" in out, out)
code, out = run_case(_JSFILES, _JS + "\nCELLS:\n  py.function  snake\n")
check("...and the SAME corpus reds once one cell is declared and js.function is not",
      code != 0 and "UNDECLARED CELL (an extracted population" in out
      and "js.function at 1" in out, out)

# AC5 — THE DECLARATION'S OWN COMMENT. It is the carrier of the three readings and the counting rule
# that produced them, and the armed row's figure is asserted against it rather than typed here, so
# the arm moves with the corpus instead of pinning it. GUARDED and the skip ANNOUNCES itself: an
# adopter's conf declares no `py.constant` row and this arm has nothing to grade there.
_ROOT_CONF = KIT.parent.parent / ".lexicon.conf"
_conf_text = _ROOT_CONF.read_text(encoding="utf-8") if _ROOT_CONF.exists() else ""
if "py.constant" in _conf_text:
    _r = subprocess.run([sys.executable, str(KIT / "lexicon.py"), "--check"],
                        cwd=KIT.parent.parent, capture_output=True, text=True)
    _armed = [ln for ln in _r.stdout.splitlines() if "py.constant.conv " in ln]
    _figs = re.search(r"population (\d+) of (\d+)", _armed[0]) if _armed else None
    check("AC5: the constant cell's comment carries the counting rule that produced its numbers",
          "module BODY statements only" in _conf_text and "AnnAssign" in _conf_text
          and "Starred" in _conf_text, _ROOT_CONF.name)
    check("AC5: ...and the command that re-derives them",
          "python tools/lexicon/lexicon.py --check" in _conf_text, _ROOT_CONF.name)
    # EACH FIGURE IS READ FROM THE ROW THAT OWNS IT, never searched for in the file. A bare
    # substring over the whole comment is green on any conf that happens to carry those digits
    # anywhere, and a falsified denominator survived exactly that — some other line held the
    # number. The graded count is the ARMED row's own; the denominator is the WIDEST reading's
    # graded count, which is what the rule narrows from.
    _armed_row = re.search(r"^#.*<-- ARMED\s+(\d+) graded", _conf_text, re.M)
    _wide_row = re.search(r"^#\s+every module-body target.*?(\d+) graded", _conf_text, re.M)
    check("AC5: ...and the ARMED row states the graded figure `--check` prints",
          bool(_figs) and bool(_armed_row) and _armed_row.group(1) == _figs.group(1),
          f"{_armed} vs row {_armed_row.group(1) if _armed_row else '(no ARMED row)'}")
    check("AC5: ...and the WIDEST reading's row states the denominator it prints",
          bool(_figs) and bool(_wide_row) and _wide_row.group(1) == _figs.group(2),
          f"{_armed} vs row {_wide_row.group(1) if _wide_row else '(no widest row)'}")
    check("AC5: ...and so do the two readings it was chosen OVER",
          _conf_text.count(" graded, ") == 3, f"{_conf_text.count(' graded, ')} reading(s)")
else:
    print("lexicon selftest SKIP — AC5's conf-comment arms: the repo-root .lexicon.conf declares "
          "no `py.constant` cell, so there is no comment to grade. Four arms unexercised.")

# A `dark` cell is a declared refusal to grade, and it too prints rather than vanishing.
code, out = run_case({"core/a.py": "def loadUserData():\n    pass\n"},
                     BASE_CONF + "\nCELLS:\n  py.function  dark\n")
check("a dark cell grades nothing and says so, and does not red", code == 0 and "dark" in out, out)

# The `conv` pin is the same TWO-SIDED equality the other pins carry.
code, out = run_case({"core/a.py": "def loadUserData():\n    pass\n"},
                     BASE_CONF + "\nCELLS:\n  py.function  snake\n\nPINS:\n  py.function.conv  1\n")
check("a declared conv pin equal to the count is green", code == 0, out)
code, out = run_case(_CLEAN, BASE_CONF + "\nCELLS:\n  py.function  snake\n\n"
                                         "PINS:\n  py.function.conv  1\n")
check("a conv count BELOW its declared pin reds and prints the replacement row",
      code != 0 and "py.function.conv  0" in out, out)

# ---- TOOL-aSurfacedLexicon-9: the owner-declarable PATTERNS block --------------------------------
#
# THE FIXTURE ARMS A LANGUAGE THIS KIT DOES NOT SHIP, which is the whole capability. `ts-regex` is
# not in `PATTERN_SETS` and is not becoming one: choosing TypeScript regexes on an adopter's behalf
# is the ruling this kit defers to the owner who has that corpus. So every arm below runs through the
# DECLARATION and none of them through a second shipped set.
#
# The `ts` CELLS rows cost one line each and buy order-independence: the (extension, surface) matrix
# reds an UNDECLARED cell with a non-empty population once that arm is promoted from a report, and
# this fixture's `ts.function` population is non-empty by construction. They declare `camel` and
# `pascal` rather than `snake` — those are the conventions the fixture's own TypeScript actually
# uses, so the arming moves no verdict here and both cells sit at zero against a zero pin.
_TS_PATTERNS = (
    "\nPATTERNS:\n"
    r"  ts-regex.functions  ^\s*(?:export\s+)?function\s+([A-Za-z_$][\w$]*)" "\n"
    r"  ts-regex.types      ^\s*(?:export\s+)?(?:interface|class)\s+([A-Za-z_$][\w$]*)" "\n"
)
#: `py.function  dark` is not decoration. The fixture corpus carries `core/a.py`, so its `py.function`
#: population is non-empty, and since TOOL-aSurfacedLexicon-12 armed `UNDECLARED_CELL_ARMED` a
#: declaration that opens a `CELLS` block owes a row for every surface it extracts. `dark` is the
#: row that declares "not graded here", which is what these arms mean: they are about `ts`.
_TS_CELLS = "\nCELLS:\n  ts.function  camel\n  ts.type      pascal\n  py.function  dark\n"
_TS_BASE = BASE_CONF.replace('LANGS="py:python-ast:parser conf::dark"',
                             'LANGS="py:python-ast:parser conf::dark ts:ts-regex:probe"')
TS_CONF = _TS_BASE + _TS_PATTERNS + _TS_CELLS
TS_FILES = {
    "core/a.py": "def build_x():\n    pass\n",
    "web/widget.ts": ("export function buildWidget(a: number): number { return a }\n"
                      "export interface WidgetSpec { id: string }\n"),
}
_armed_of = lambda o: re.search(r"coverage — armed (\d+) of (\d+)", o)   # noqa: E731

# AC7, first half — the SHIPPED refusal, with the LANGS triple and NO extractor rows. This is the
# state every adopter of an unshipped language is in today, and it is the reason the block exists:
# the language is declared, no set answers it, and the walk refuses one line before any predicate.
code, out = run_case(TS_FILES, _TS_BASE)
check("PATTERNS absent: a LANGS row naming an unshipped set is still refused",
      code != 0 and "does not ship" in out and "'ts-regex'" in out, out)
_before = _armed_of(out)

# AC7, second half, and AC1 — the SAME command over the SAME files, with the two rows added and
# NOTHING else changed. The coverage numerator is what site `:726` decides, and it moves by exactly
# the one file while the denominator does not: the empty diff against the engine is a supporting
# clause, this is the observation.
code, out = run_case(TS_FILES, TS_CONF)
check("AC1: a PATTERNS-declared set grades its language and the run is green", code == 0, out)
_after = _armed_of(out)
check("AC7: the declared extension enters the ARMED coverage numerator",
      bool(_before) and bool(_after)
      and int(_after.group(1)) == int(_before.group(1)) + 1
      and _after.group(2) == _before.group(2),
      f"before={_before and _before.group(0)!r} after={_after and _after.group(0)!r}")
check("AC1: the run names the declared extractor rows",
      "PATTERNS — 2 declared extractor row(s)" in out and "ts-regex.functions" in out, out)
check("a declaration touching no SHIPPED key prints no REPLACES line", "REPLACES" not in out, out)

# AC2 — the offender. The point of arming a language at all: its definitions are graded by the same
# predicate everything else is, and the refusal names the file and the line.
_off = dict(TS_FILES)
_off["web/widget.ts"] = TS_FILES["web/widget.ts"] + "export function frobnicateWidget() {}\n"
code, out = run_case(_off, TS_CONF)
check("AC2: an undeclared leading token in the DECLARED language reds",
      code != 0 and "P1 verb" in out and "frobnicateWidget" in out, out)
check("AC2: the red names the file and the line", "web/widget.ts:3" in out, out)

# AC3 — DEAD PROBE over a DECLARED set. The arm is shipped code and this unit widens its POPULATION:
# before the merge, `scan_corpus` refused the extension one line earlier, so the arm had never
# graded a declared set at all. Which refusal fires is the whole observation.
code, out = run_case(TS_FILES, _TS_BASE + "\nPATTERNS:\n"
                     r"  ts-regex.functions  ^\s*fn\s+([A-Za-z_]\w*)" "\n" + _TS_CELLS)
check("AC3: a declared set that matches NOTHING reds as DEAD PROBE",
      code != 0 and "DEAD PROBE" in out and "ts-regex" in out, out)
check("AC3: and NOT for the unshipped-set reason", "does not ship" not in out, out)

# AC4 — the OTHER zero population, reported differently on purpose. `.ts` is declared, the corpus
# carries none of it, so DEAD PROBE's guard correctly cannot judge it — and silence there is
# indistinguishable from a language being graded.
code, out = run_case({"core/a.py": "def build_x():\n    pass\n"}, TS_CONF)
_inert = [ln for ln in out.splitlines() if "INERT DECLARATION" in ln]
check("AC4: a declaration with no file of that extension is reported INERT",
      bool(_inert) and ".ts=probe" in _inert[0], out)
check("AC4: and is NOT reported as DEAD PROBE", "DEAD PROBE" not in out, out)
check("AC4: INERT is a report, not a refusal", code == 0, out)

# AC9 — a duplicated row key REFUSES rather than taking the last one. A repeated key in a hand-edited
# declaration is a typo far more often than an intent, and last-wins silently retires the row the
# owner believes is live.
code, out = run_case(TS_FILES, _TS_BASE + _TS_PATTERNS
                     + r"  ts-regex.functions  ^\s*fn\s+([A-Za-z_]\w*)" "\n" + _TS_CELLS)
check("AC9: a duplicate PATTERNS row key refuses and names the first line",
      code != 0 and "duplicate row key" in out and "ts-regex.functions" in out, out)

# AC6 — the regex validation, at PARSE time and never as a dropped row. Zero groups raises inside the
# walk with no line number; two groups grades the wrong half of every name it matches and reports a
# clean run. Both become one refusal naming the file and the line.
for _rows, _label, _needle in (
    (r"  ts-regex.functions  ^\s*function\s+[A-Za-z_]\w*", "zero capturing groups", "0 capturing group"),
    (r"  ts-regex.functions  ^(\s*)function\s+([A-Za-z_]\w*)", "two capturing groups", "2 capturing group"),
    (r"  ts-regex.functions  ^\s*function\s+([A-Za-z_]\w*", "an uncompilable regex", "not a Python regex"),
):
    code, out = run_case(TS_FILES, _TS_BASE + "\nPATTERNS:\n" + _rows + "\n")
    check(f"AC6: {_label} refuses", code != 0 and _needle in out, out)
    check(f"AC6: the refusal for {_label} names the line", ".lexicon.conf:" in out, out)

# AC6, through the CLI the bash adopter uses. One reader, two output shapes — a refusal that only
# fired on the engine path would leave `adopt-lexicon.sh` green over a declaration the engine reds.
with build_tempdir() as _td:
    _conf = Path(_td) / ".lexicon.conf"
    _conf.write_text(_TS_BASE + "\nPATTERNS:\n"
                     r"  ts-regex.functions  ^\s*function\s+[A-Za-z_]\w*" "\n", encoding="utf-8")
    _r = subprocess.run([sys.executable, str(KIT / "lexicon_conf.py"), "--print-rows", "PATTERNS",
                         str(_conf)], capture_output=True, text=True)
    check("AC6: --print-rows PATTERNS raises the same ConfError, naming the file and the line",
          _r.returncode != 0 and "capturing group" in _r.stderr and ".lexicon.conf:" in _r.stderr,
          _r.stdout + _r.stderr)

# ---- the MERGE itself, which no end-to-end fixture above can distinguish -------------------------
#
# EVERY ARM ABOVE DECLARES A NEW SET, and a per-key merge and a per-set replacement behave
# identically on one of those. The risk this unit actually carries is the merge landing on a SHIPPED
# set, where a per-set replacement silently retires the two keys the owner did not name — an
# extractor grading a smaller population while reporting a clean run. These arms are the gate for
# that, and they FAIL if the merge goes wrong rather than merely exercising it.
_shipped_js = lex.PATTERN_SETS["js-regex"]
_resolved = lex.resolve_pattern_sets(
    {"PATTERNS": {"js-regex.types": re.compile(r"^\s*type\s+([A-Za-z_$][\w$]*)", re.M)}})
check("the merge REPLACES the key the row names",
      [r.pattern for r in _resolved["js-regex"]["types"]] == [r"^\s*type\s+([A-Za-z_$][\w$]*)"],
      f"{_resolved['js-regex']['types']}")
check("the merge leaves the UNNAMED keys of a shipped set standing",
      _resolved["js-regex"]["functions"] == _shipped_js["functions"]
      and _resolved["js-regex"]["imports"] == _shipped_js["imports"],
      f"functions={len(_resolved['js-regex']['functions'])} "
      f"imports={len(_resolved['js-regex']['imports'])}")
check("the merge does NOT mutate the shipped constant",
      [r.pattern for r in lex.PATTERN_SETS["js-regex"]["types"]]
      == [r"^\s*(?:export\s+)?class\s+([A-Za-z_$][\w$]*)"],
      f"{lex.PATTERN_SETS['js-regex']['types']}")

# AC5 — with nothing declared, the resolution IS the shipped mapping. An adopter who writes no block
# is on exactly the previous behaviour, asserted rather than assumed.
check("AC5: no PATTERNS declared resolves to the shipped sets exactly",
      lex.resolve_pattern_sets({}) == lex.PATTERN_SETS, f"{lex.resolve_pattern_sets({})}")

# A set reachable ONLY through the declaration still answers the three-list contract `_probe_defs`
# reads, so a row arming `functions` alone cannot raise a KeyError halfway through a walk.
_partial = lex.resolve_pattern_sets(
    {"PATTERNS": {"ts-regex.functions": re.compile(r"^fn ([a-z]+)", re.M)}})
check("a declared set arming ONE part still carries all three",
      sorted(_partial["ts-regex"]) == ["functions", "imports", "types"],
      f"{sorted(_partial['ts-regex'])}")
check("and its unnamed parts are EMPTY rather than absent",
      _partial["ts-regex"]["types"] == [] and _partial["ts-regex"]["imports"] == [],
      f"{_partial['ts-regex']}")

# ---- TOOL-aSurfacedLexicon-13: the prefix selector, and why these fixtures are SYNTHETIC ---------
#
# THE FIXTURES BELOW ARE SYNTHETIC, deliberately, and the spec says so in as many words. The
# population this mechanism was ruled in FOR has no instance in this tree at all: measured on the
# run that wrote them, zero PascalCase function definitions across all 49 tracked `.py` files and
# zero type definitions across all 8 tracked `.js` files. The 1,072 PascalCase `.tsx` bindings that
# motivated it were measured against an ADOPTER's tree by TOOL-dScaffoldedMirror-13 and are
# unverified here — that tree is outside this build's read-only scope. So four cases have no
# in-repo population to exercise them and are fixtures instead: a parent and its selector
# DISAGREEING, a name matching NO selector, a name matching TWO, and a selector whose subset is
# EMPTY. The routing half IS exercised against the real corpus, by the staged break the build record
# carries; what is synthetic is the population that makes a verdict move.
#
# AC8 is the odd one out and is not about selectors at all: it pins the ARITY of the function entry,
# because the decorator capability arrives beside that shape rather than inside it.

def read_conv_row(out: str, cell: str) -> int:
    """The DENOMINATOR off one `.conv` report row, or `-1` when that row is absent.

    `-1` rather than a raised AttributeError, because the arms below are allowed to FAIL: a regex
    read straight through `.group(1)` turns a missing row into a traceback that kills the summary,
    and every arm after it then goes unexercised and unreported. Found by staging the reverts these
    arms exist for — three of them died that way before the row was ever compared.
    """
    m = re.search(re.escape(cell) + r"\.conv \d+ of (\d+)", out)
    return int(m.group(1)) if m else -1


# AC8 — the frozen entry shape, asserted the way its two out-of-kit consumers read it.
# The drift-audit kit's `drift_report.py` runs `for nm, _ln in got[0]` at two call sites, BOTH outside
# any catch naming `ValueError`, and one of them runs on `drift-audit records` — a leg with no
# guard, so it reds every bar. Widening the pair to carry decorators would raise there uncaught.
# This arm exists so that break is caught in this kit's own selftest first.
_funcs, _types, _imports = _lex.extract_text(
    "@deco\ndef build_x():\n    pass\n\n\nclass BuildY:\n    pass\n", "parser", "python-ast")
check("AC8: every function entry unpacks as EXACTLY two elements",
      bool(_funcs) and all(len(e) == 2 for e in _funcs), repr(_funcs))
check("AC8: ...and the positional unpack drift-audit performs still works",
      [nm for nm, _ln in _funcs] == ["build_x"], repr(_funcs))
check("AC8: ...and a decorated definition is still ONE entry, not two",
      len(_funcs) == 1 and len(_types) == 1, repr((_funcs, _types)))

# The row-key grammar, as a table of shapes rather than on the one row typed first.
for _key, _want in (("py.function", ("py", "function", None, None)),
                    ("py.function+prefix:load", ("py", "function", "prefix", "load")),
                    ("js.type+decorator:route", ("js", "type", "decorator", "route"))):
    # The ConfError is CAUGHT and scored as a failed arm rather than left to propagate. A refusal
    # raised out of a `check(...)` argument kills the interpreter before the summary prints, which
    # turns a named arm failure into a bare traceback and leaves every arm below unexercised.
    try:
        _got = _lc.parse_cell_key(_key)
    except _lc.ConfError as _e:
        _got = f"REFUSED: {_e}"
    check(f"parse_cell_key({_key!r})", _got == _want, repr(_got))
for _key, _frag in (("py.function+wiggly:load", "a CELLS selector is"),
                    ("py.function+prefix", "a CELLS selector is"),
                    ("py.function+prefix:a.b", "is not `[A-Za-z0-9_]+`"),
                    ("py.function+prefix:", "is not `[A-Za-z0-9_]+`"),
                    ("pyfunction+prefix:load", "a CELLS row key is"),
                    ("py.frobnicate+prefix:load", "unknown surface")):
    try:
        _lc.parse_cell_key(_key)
        check(f"a malformed selector key {_key!r} REFUSES", False, "no ConfError raised")
    except _lc.ConfError as _e:
        check(f"a malformed selector key {_key!r} REFUSES naming why", _frag in str(_e), str(_e))

# AC6 — a decorator selector on a PROBE language is a declaration-time refusal naming the language
# AND the mode, rather than a subset that is empty because nothing could ever fill it.
_JSCONF = BASE_CONF.replace('LANGS="py:python-ast:parser conf::dark"',
                            'LANGS="py:python-ast:parser js:js-regex:probe conf::dark"')
with build_tempdir() as _td:
    _cp = Path(_td) / "c.conf"
    _cp.write_text(_JSCONF + "\nCELLS:\n  js.function+decorator:route  camel\n",
                   encoding="utf-8", newline="\n")
    try:
        _lc.load_conf(_cp)
        check("AC6: a decorator selector on a probe language REFUSES", False, "no ConfError")
    except _lc.ConfError as _e:
        check("AC6: a decorator selector on a probe language REFUSES", True)
        check("AC6: ...naming the language and the mode",
              "'js'" in str(_e) and "'probe'" in str(_e), str(_e))
    # ...and the SAME row on the parser language parses, which is what makes the refusal a
    # discrimination rather than a blanket ban.
    _cp.write_text(_JSCONF + "\nCELLS:\n  py.function+decorator:route  camel\n",
                   encoding="utf-8", newline="\n")
    try:
        _cells = _lc.load_conf(_cp)["CELLS"]
    except _lc.ConfError as _e:
        _cells = {f"REFUSED: {_e}": None}
    check("AC6 green: the same selector on a `parser` language parses",
          "py.function+decorator:route" in _cells, repr(list(_cells)))

    # S4 — the selector'd cell's own PINS row. The key is `<cell>.<predicate>` split on the DOT, so
    # this is what the dot-free literal buys: a pin for the subset that is not the parent's.
    _cp.write_text(BASE_CONF + "\nCELLS:\n  py.function  snake\n\n  py.function+prefix:load  pascal\n"
                               "\nPINS:\n  py.function.conv  1\n\n  py.function+prefix:load.conv  2\n",
                   encoding="utf-8", newline="\n")
    try:
        _pins = _lc.load_conf(_cp)["PINS"]
    except _lc.ConfError as _e:
        _pins = f"REFUSED: {_e}"
    check("S4: a selector'd cell carries its own PINS row, keyed on the selector'd cell string",
          _pins == {"py.function.conv": 1, "py.function+prefix:load.conv": 2}, repr(_pins))

# ---- end to end: the four cases this tree has no population for ---------------------------------
_SEL_PARENT = BASE_CONF + "\nCELLS:\n  py.function  snake\n"
_SEL_BOTH = _SEL_PARENT + "\n  py.function+prefix:load  pascal\n"
_SEL_FILES = {"core/a.py": "def build_index():\n    pass\n\n\ndef load_user():\n    pass\n"}

# 1 — the parent and its selector DISAGREE. The routed name reds against the selector's convention
# and the parent stays green, which is the whole mechanism in one run.
code, out = run_case(_SEL_FILES, _SEL_BOTH)
check("a routed name is graded against the SELECTOR's convention, not the parent's",
      code != 0 and "VIOLATION  load_user  satisfies snake, not pascal" in out, out)
check("...and the RED is attributed to the selector's own row, not the parent's",
      "py.function+prefix:load.conv 1 of 1" in out and "py.function.conv 0 of 1" in out, out)
check("...and the selector row carries its own denominator and rule, like every other row",
      "py.function+prefix:load.conv 1 of 1 against pascal" in out
      and "population 1 of 2 (rule: every extracted function definition)" in out, out)

# S5 — the selector row prints BENEATH its parent. Declaration order alone does not buy this: a
# selector declared above its parent must still print below it, which is the arm.
_ROWS = [ln for ln in out.splitlines() if ".conv " in ln and " of " in ln]
check("S5: the selector row prints directly beneath its parent",
      len(_ROWS) == 2 and "py.function.conv" in _ROWS[0]
      and "py.function+prefix:load.conv" in _ROWS[1], repr(_ROWS))
code, _revout = run_case(_SEL_FILES, BASE_CONF + "\nCELLS:\n  py.function+prefix:load  pascal\n"
                                                 "\n  py.function  snake\n")
_REVROWS = [ln for ln in _revout.splitlines() if ".conv " in ln and " of " in ln]
check("S5: ...even when the selector is DECLARED above it",
      len(_REVROWS) == 2 and "py.function.conv" in _REVROWS[0]
      and "py.function+prefix:load.conv" in _REVROWS[1], repr(_REVROWS))

# 2 — the EXCLUSION, as the identity that proves it: a routed name LEAVES the parent's population.
# Read from two runs in one session rather than against a literal, so it survives a fixture edit.
_code, _alone = run_case(_SEL_FILES, _SEL_PARENT)
_parent_alone = read_conv_row(_alone, "py.function")
_parent_split = read_conv_row(out, "py.function")
_sel_split = read_conv_row(out, "py.function+prefix:load")
check("the routed subset LEAVES the parent's population, and the two sum to the whole",
      _parent_split + _sel_split == _parent_alone,
      f"{_parent_split} + {_sel_split} != {_parent_alone}")
check("...and the graded name is graded ONCE, not once per cell",
      out.count("VIOLATION  load_user") == 1, out)

# 3 — a name matching NO selector stays with the parent. The control for case 1: without it, an
# implementation that routed EVERYTHING to the selector would pass every arm above.
check("a name matching no selector is graded by the PARENT",
      "py.function.conv 0 of 1" in out, out)
# The selector is declared at the PARENT's own convention here, so the only thing that can red is
# the unrouted name — an implementation routing everything would print nothing at all.
code, out = run_case({"core/a.py": "def buildUser():\n    pass\n\n\ndef load_user():\n    pass\n"},
                     _SEL_PARENT + "\n  py.function+prefix:load  snake\n")
check("...and it reds against the PARENT's convention when it is wrong for it",
      code != 0 and "VIOLATION  buildUser  satisfies camel, not snake" in out
      and "py.function.conv 1 of 1" in out, out)

# 4 — a name matching TWO selectors is refused, naming BOTH literals, and graded by neither.
code, out = run_case({"core/a.py": "def load_user_data():\n    pass\n"},
                     _SEL_PARENT + "\n  py.function+prefix:load  pascal\n"
                                   "\n  py.function+prefix:load_user  camel\n")
check("AC3: a name matching TWO selectors REFUSES as AMBIGUOUS SELECTOR",
      code != 0 and "AMBIGUOUS SELECTOR" in out and "load_user_data" in out, out)
# Read off the REFUSAL LINE, not the whole output: both literals appear in the cell rows above it
# whatever the refusal says, so a whole-output membership test passes on a message naming neither.
# Found by staging the revert — that weaker arm stayed green with the refusal deleted.
_amb = [ln for ln in out.splitlines() if "AMBIGUOUS SELECTOR" in ln]
check("AC3: ...naming BOTH selector literals, on the refusal line itself",
      len(_amb) == 1 and "+prefix:load " in _amb[0] and "+prefix:load_user" in _amb[0], repr(_amb))
check("AC3: ...and neither convention is applied to it",
      "VIOLATION  load_user_data" not in out, out)

# 5 — an EMPTY subset is a DEAD CELL through TOOL-aSurfacedLexicon-6's arm, not a clean zero. This
# is where a selector that matches nothing is caught, and it is the other half of case 4's argument:
# two selectors that CAN both match either do both match some name, or one of them is dead here.
code, out = run_case(_SEL_FILES, _SEL_PARENT + "\n  py.function+prefix:add  pascal\n")
check("AC4: a selector matching NOTHING reds as DEAD CELL, not as a clean zero",
      code != 0 and "DEAD CELL — `py.function+prefix:add`" in out, out)

# ---- the decorator selector -----------------------------------------------------------------
_DECO = {"core/a.py": "def build_index():\n    pass\n\n\n@load_registered\ndef build_x():\n"
                      "    pass\n\n\n@app.route('/x')\ndef build_y():\n    pass\n"}
code, out = run_case(_DECO, _SEL_PARENT + "\n  py.function+decorator:load_registered  pascal\n")
check("AC5: a decorator selector routes the DECORATED definition and nothing else",
      code != 0 and "py.function+decorator:load_registered.conv 1 of 1" in out
      and "VIOLATION  build_x  satisfies snake, not pascal" in out, out)
code, out = run_case(_DECO, _SEL_PARENT + "\n  py.function+decorator:route  pascal\n")
check("AC5: ...and a DOTTED decorator is selectable by its last segment",
      code != 0 and "VIOLATION  build_y  satisfies snake, not pascal" in out, out)

# ---- S4: the selector's pin, and what an ABSENT one means ---------------------------------------
#
# A selector'd key with NO pin row of its own reads as a pin of `0`. It never inherits the parent's
# count and its offenders are never folded back into the parent's row — folding is the one
# implementation that satisfies every criterion above while defeating the ratchet this exists to
# build, which is why it is refused by an arm rather than left to taste.
_PINNED = (_SEL_BOTH + "\nPINS:\n  py.function.conv  0\n\n  py.function+prefix:load.conv  1\n")
code, out = run_case(_SEL_FILES, _PINNED)
check("S4: with a pin row for each cell at its own count, the run is GREEN", code == 0, out)
code, out = run_case(_SEL_FILES, _SEL_BOTH + "\nPINS:\n  py.function.conv  0\n")
check("S4: with the selector's pin row DELETED it reads as 0 and reds on its OWN count",
      code != 0 and "py.function+prefix:load.conv 1 against declared pin 0" in out, out)
check("S4: ...and the parent's row stays green, so nothing was folded into it",
      "py.function.conv 0 against declared pin" not in out, out)
# The ratchet is SEPARATE in both directions: one row moving leaves the other's verdict alone.
code, out = run_case({**_SEL_FILES, "core/b.py": "def buildUser():\n    pass\n"}, _PINNED)
check("S4: a new PARENT offender reds the parent's row and leaves the selector's green",
      code != 0 and "py.function.conv 1 against declared pin 0" in out
      and "py.function+prefix:load.conv 1 against declared pin" not in out, out)
code, out = run_case({**_SEL_FILES, "core/b.py": "def load_more():\n    pass\n"}, _PINNED)
check("S4: a new SELECTOR offender reds the selector's row and leaves the parent's green",
      code != 0 and "py.function+prefix:load.conv 2 against declared pin 1" in out
      and "py.function.conv 0 against declared pin" not in out, out)

# ---- TOOL-aSurfacedLexicon-7: the P1 split into DEBT and UNRULED --------------------------------
#
# `fetch` is banned by BASE_CONF's own `load … NOT fetch` clause AND sits in the canon's `load`
# cluster, so it is DEBT under either source; `frobnicate` is in no cluster and no clause, so it is
# UNRULED. One fixture, both halves, and the two are asserted to be textually DISTINCT — a reader
# who cannot tell a rename from a scoping question has the refusal this unit exists to replace.
_SPLIT_FILES = {"core/a.py": "def fetch_user():\n    pass\n\n\ndef frobnicate_it():\n    pass\n"}
# PINNED AT THE COUNT IT PRODUCES, so `--list` prints each offender ONCE. Under a red pin the
# authoring listing and the refusal block both print the same line, and every `== 1` below would be
# asserting against the wrong number for the wrong reason.
_SPLIT_CONF = BASE_CONF.replace('VERB_OFFENDER_PIN="0"', 'VERB_OFFENDER_PIN="2"')
code, out = run_case(_SPLIT_FILES, _SPLIT_CONF, args=("--list",))
check("S1: the split's own fixture is GREEN, so every line below is read from a passing run",
      code == 0, out)
_DEBT_LINE = [ln for ln in out.splitlines() if "fetch_user" in ln]
_UNRULED_LINE = [ln for ln in out.splitlines() if "frobnicate_it" in ln]
check("AC5: a canon-clustered leading token is classified DEBT",
      len(_DEBT_LINE) == 1 and "DEBT:" in _DEBT_LINE[0], repr(_DEBT_LINE))
check("AC5: ...and the DEBT line names the REPLACEMENT IDENTIFIER, not just the verb",
      len(_DEBT_LINE) == 1 and "rename to `load_user`" in _DEBT_LINE[0], repr(_DEBT_LINE))
check("AC6: a token in NO cluster is classified UNRULED",
      len(_UNRULED_LINE) == 1 and "UNRULED:" in _UNRULED_LINE[0], repr(_UNRULED_LINE))
check("AC6: ...and the UNRULED line proposes NO replacement",
      len(_UNRULED_LINE) == 1 and "rename to" not in _UNRULED_LINE[0], repr(_UNRULED_LINE))
check("AC6: ...and the two messages are textually distinct",
      len(_DEBT_LINE) == 1 and len(_UNRULED_LINE) == 1
      and "DEBT:" not in _UNRULED_LINE[0] and "UNRULED:" not in _DEBT_LINE[0],
      repr(_DEBT_LINE + _UNRULED_LINE))
# S2 — the per-token site census, which is the figure that tells a one-off name from a house idiom.
check("S2: the UNRULED line carries its token's corpus-wide site count",
      len(_UNRULED_LINE) == 1 and "1 definition(s) corpus-wide lead with it" in _UNRULED_LINE[0],
      repr(_UNRULED_LINE))
_MANY = {"core/a.py": "def frob_a():\n    pass\n\n\ndef frob_b():\n    pass\n\n\ndef frob_c():\n"
                      "    pass\n"}
_c, _many_out = run_case(_MANY, BASE_CONF.replace('VERB_OFFENDER_PIN="0"',
                                                  'VERB_OFFENDER_PIN="3"'), args=("--list",))
check("S2: ...and the count is the TOKEN's, not a constant",
      _many_out.count("3 definition(s) corpus-wide lead with it") == 3, _many_out)

# S6 — the split on the count line, and the identity that it is a SPLIT of the offender total.
_SPLIT_ROW = [ln for ln in out.splitlines() if "P1 verb" in ln and "graded=" in ln]
check("S6: the P1 count line carries debt and unruled beside the sum they add to",
      len(_SPLIT_ROW) == 1 and "offenders=2 (debt=1 + unruled=1)" in _SPLIT_ROW[0], repr(_SPLIT_ROW))

# AC8, arm one — THE CLASSIFIER OVER THE WHOLE INDEX, not over the two tokens a fixture happens to
# carry. A classifier that collapses to one bucket satisfies every end-to-end arm above with either
# constant substituted, which is why the population is asserted rather than sampled.
import canon as _canon  # noqa: E402

_FORMS = _canon.build_form_index()
_MISCLASSED = sorted(f for f in _FORMS if not _lex.read_debt_gloss(f)[0])
check("AC8: EVERY key of canon.build_form_index() classifies as DEBT",
      not _MISCLASSED and len(_FORMS) > 0, f"{len(_FORMS)} keys, unclassified: {_MISCLASSED}")
check("AC8: ...and a token the index does not hold classifies as UNRULED",
      _lex.read_debt_gloss("frobnicate") == ("", "") and "frobnicate" not in _FORMS)
check("AC8: ...and the representative it names is the cluster's, not the token itself",
      _lex.read_debt_gloss("fetch")[0] == "load" and _lex.read_debt_gloss("get")[0] == "read",
      repr((_lex.read_debt_gloss("fetch"), _lex.read_debt_gloss("get"))))

# S3 — THE PRECEDENCE, in a fixture that MANUFACTURES the disagreement, so this arm holds in an
# adopter's tree whatever their declaration says. `install` is `init`'s cluster-mate in the canon;
# the fixture declares `add … NOT install`, and the declaration must win.
_PREC_CONF = SUGGEST_CONF.replace("add     append to an existing collection — NOT `push`",
                                  "add     append to an existing collection — NOT `install`")
_c, _prec = run_case({"core/a.py": "def build_x():\n    pass\n"}, _PREC_CONF,
                     args=("--suggest", "install_thing", "--as", "py.function"))
check("AC3: --suggest follows the DECLARATION where it and the canon disagree",
      "use `add_thing`" in _prec and "the declaration says" in _prec, _prec)
check("AC3: ...and it does NOT answer the canon's representative for that token",
      "init_thing" not in _prec, _prec)
_c, _canon_only = run_case({"core/a.py": "def build_x():\n    pass\n"}, SUGGEST_CONF,
                           args=("--suggest", "install_thing", "--as", "py.function"))
check("AC3: ...while with NO clause naming it, the canon answers instead",
      "use `init_thing`" in _canon_only and "the shipped canon says" in _canon_only, _canon_only)
# Fork F2, decided as its recommendation: the canon's representative is proposed even where the
# declaration carries no row for it, and the line SAYS the row is owed. Suppressing the advice
# leaves the author with a refusal and nothing else.
check("F2: a canon representative absent from the declaration is proposed AND flagged",
      "use `init_thing`" in _canon_only and "carries NO row for it" in _canon_only, _canon_only)
_c, _scope = run_case({"core/a.py": "def build_x():\n    pass\n"}, SUGGEST_CONF,
                      args=("--suggest", "frobnicate_thing", "--as", "py.function"))
check("AC6: --suggest names a token in neither source a SCOPING question, and proposes nothing",
      "SCOPING question" in _scope and "use `" not in _scope, _scope)

# AC8, arm two — OVER THE DECLARATION THIS KIT IS INSTALLED BESIDE, so AC3 cannot decay into a
# criterion that cannot fail without something going red first. A declaration whose every negative
# agrees with the canon adds no boundary the canon did not already supply, and the precedence rule
# is then unobservable in that tree — which is the arm-that-cannot-fail shape one level up. This leg
# is `subject = kit` and runs only under GATE_SELFTESTS=1, so it cannot red an adopter's push.
_PREC_ROOT = KIT.parent.parent
_PREC_PATH = _PREC_ROOT / ".lexicon.conf"
if _PREC_PATH.exists():
    from lexicon_conf import load_conf as _load_conf  # noqa: E402

    _rban = _lex.build_banned_index(_load_conf(_PREC_PATH))
    _DISAGREE = sorted(t for t, v in _rban.items() if t in _FORMS and _FORMS[t] != v)
    check("AC8: this tree's declaration names at least one token the canon spells differently",
          bool(_DISAGREE),
          f"{_PREC_PATH}: every NOT clause agrees with the canon, so --suggest's precedence rule "
          f"has no observable case here; declare a negative the canon does not already supply")
    if _DISAGREE:
        _tok = _DISAGREE[0]
        # THIS TREE'S DECLARATION, PLUS THE ONE CELL THAT MAKES THE VERB PATH ASKABLE. `--as` became
        # required at TOOL-aSurfacedLexicon-8 and the leading-token check runs only on a cell arming
        # `vocab`; this repo's tracked CELLS block arms none until TOOL-aSurfacedLexicon-12 writes
        # the matrix, so a run against the tracked file as it stands would observe an
        # undeclared-cell refusal rather than the precedence this arm exists to grade. The NEGATIVE
        # is still read from the tracked declaration — `_rban` above is parsed from it — so the arm
        # keeps grading the file it names and only the CELL is supplied.
        _PCONF = _load_conf(_PREC_PATH)
        _PCELLS = _PCONF.get("CELLS") or {}
        _vocab_cell = next((c for c, (_cv, _fl) in _PCELLS.items()
                            if "vocab" in _fl and "+" not in c and c.endswith(".function")), "")
        _prec_text = _PREC_PATH.read_text(encoding="utf-8")
        if not _vocab_cell:
            # The cell is SYNTHESISED from the declaration's own LANGS rather than spelled here: a
            # CELLS row naming an extension LANGS does not declare is a `load_conf` refusal, so a
            # literal `py.function` would work on this repo and refuse on an adopter declaring no
            # python. The first declared extension with no `function` row is the one that cannot
            # collide with a row already there.
            from lexicon_conf import langs as _langs  # noqa: E402

            _ext = next((e for e, _ps, _md in _langs(_PCONF)
                         if f"{e}.function" not in _PCELLS), "")
            _vocab_cell = f"{_ext}.function" if _ext else ""
            _prec_text = _prec_text.replace("\nCELLS:\n",
                                            f"\nCELLS:\n  {_vocab_cell}  snake  vocab\n\n", 1)
    if _DISAGREE and not _vocab_cell:
        check("AC8: SKIPPED — this declaration arms no `vocab` function cell and every extension it "
              "declares already carries a `function` row, so the precedence arm has no cell to ask "
              "through", True)
    elif _DISAGREE:
        with build_tempdir() as _ptd:
            _proot = Path(_ptd)
            subprocess.run(["git", "init", "-q"], cwd=_proot, check=True, capture_output=True)
            (_proot / ".lexicon.conf").write_text(_prec_text, encoding="utf-8", newline="\n")
            _sr = subprocess.run([sys.executable, str(KIT / "lexicon.py"), "--suggest",
                                  f"{_tok}_thing", "--as", _vocab_cell],
                                 cwd=_proot, capture_output=True, text=True)
        check("AC8: ...and --suggest answers the DECLARATION's verb for it, not the canon's",
              f"use `{_rban[_tok]}_thing`" in _sr.stdout
              and f"use `{_FORMS[_tok]}_thing`" not in _sr.stdout,
              f"token {_tok!r}: conf {_rban[_tok]!r} vs canon {_FORMS[_tok]!r} -> {_sr.stdout!r}")
else:
    check("AC8: SKIPPED — no .lexicon.conf beside the kit, so the precedence arm has no "
          "declaration to read", True)

# ---- S4/S5: the per-cell pin rows, and the emission that produces them ---------------------------
#
# THE ROWS ARE SCOPED TO DECLARED `vocab` CELLS. With none declared the emission is EMPTY and the
# scalar is the only verb ratchet — which is the state this unit LANDS in on the tracked tree, so it
# is asserted rather than assumed.
_c, _no_vocab = run_case(_SPLIT_FILES, _SPLIT_CONF, args=("--measure",))
check("S4: with no `vocab` cell declared, --measure emits NO pin rows",
      ".debt" not in _no_vocab and ".unruled" not in _no_vocab
      and 'VERB_OFFENDER_PIN="2"' in _no_vocab, _no_vocab)

_VOCAB = _SPLIT_CONF + "\nCELLS:\n  py.function  dark vocab\n"
_c, _meas = run_case(_SPLIT_FILES, _VOCAB, args=("--measure",))
check("S5: --measure emits both rows for an armed `vocab` cell",
      "  py.function.debt  1" in _meas and "  py.function.unruled  1" in _meas, _meas)
# S5 — THE BLANK LINE IS THE CONTRACT, not the formatting. `_parse_pins` refuses two rows whose line
# numbers differ by one, so a dense emission is bytes the wiring leg rejects.
#
# THE INDICES ARE SEARCHED, NEVER `.index()`d. A revert that empties the emission would make
# `.index()` raise, and a suite that CRASHES has failed no NAMED arm — which is the one outcome the
# build rule behind this file forbids. Found by running exactly that revert.
_ML = _meas.splitlines()
_di = next((i for i, ln in enumerate(_ML) if ln.startswith("  py.function.debt ")), -1)
_ui = next((i for i, ln in enumerate(_ML) if ln.startswith("  py.function.unruled ")), -1)
check("S5: ...separated by exactly one blank line, which is what its reader REQUIRES",
      _di >= 0 and _ui == _di + 2 and _ML[_di + 1] == "", repr((_di, _ui, _ML)))

# THE ROUND TRIP: the emitter's own bytes, pasted, leave the reader green. This is the arm that
# would have caught a dense emission by contradiction rather than by inspection.
_PINNED_VOCAB = _VOCAB + "\nPINS:\n  py.function.debt  1\n\n  py.function.unruled  1\n"
code, out = run_case(_SPLIT_FILES, _PINNED_VOCAB)
check("AC7: the emitted rows, pasted back, leave the declaration GREEN",
      code == 0 and "py.function.debt 1 against declared pin 1" in out
      and "py.function.unruled 1 against declared pin 1" in out, out)
code, _dense = run_case(_SPLIT_FILES,
                        _VOCAB + "\nPINS:\n  py.function.debt  1\n  py.function.unruled  1\n")
check("AC7: ...and the SAME rows written dense are a refusal naming both line numbers",
      code != 0 and "are adjacent" in _dense and "'py.function.debt'" in _dense
      and "'py.function.unruled'" in _dense, _dense)

# AC9 — THE REDISTRIBUTION. A DEBT-leading definition renamed to an UNRULED-leading token holds the
# corpus total, so the scalar greens and only the per-cell pair can see it. Both directions red,
# because the pin is a two-sided equality on each row.
_MOVED = {"core/a.py": "def demand_user():\n    pass\n\n\ndef frobnicate_it():\n    pass\n"}
code, _redis = run_case(_MOVED, _PINNED_VOCAB)
check("AC9: a DEBT->UNRULED rename reds BOTH moved rows",
      code != 0 and "py.function.debt MOVED 1 -> 0" in _redis
      and "py.function.unruled MOVED 1 -> 2" in _redis, _redis)
check("AC9: ...while the corpus offender TOTAL is unchanged, so the scalar stays green",
      "verb offenders" not in _redis and "offenders=2 (debt=0 + unruled=2)" in _redis, _redis)
_code, _scalar_only = run_case(_MOVED, _SPLIT_CONF)
check("AC9: ...and the SAME rename under the single scalar alone exits 0",
      _code == 0, _scalar_only)

# THE TWO REFUSALS `measure_vocab_cells` raises, because a `vocab` row whose pair would count a
# population it does not describe is a pin ratcheting the wrong thing.
code, out = run_case(_SPLIT_FILES, _SPLIT_CONF + "\nCELLS:\n  py.constant  dark vocab\n")
check("S4: `vocab` on a surface P1 does not grade is a NAMED refusal",
      code != 0 and "VOCAB ON THE WRONG SURFACE" in out and "py.constant" in out, out)
code, out = run_case(_SPLIT_FILES,
                     _SPLIT_CONF + "\nCELLS:\n  py.function  dark\n\n"
                                   "  py.function+prefix:fetch  dark vocab\n")
check("S4: `vocab` on a ROUTED subset is a NAMED refusal, not a parent's count under its name",
      code != 0 and "VOCAB ON A ROUTED SUBSET" in out, out)

# ---- TOOL-aSurfacedLexicon-11: the canon overlay, and the stamp that records it ------------------
#
# THE MERGE IS ASSERTED THROUGH ALL THREE ACCESSORS, never through the index alone. Two of the three
# iterate `CLUSTERS` themselves and never call `build_form_index`, so an arm checking only the index
# is the probe that missed this unit's design defect for two revisions of its own spec.

# AC5 — with NO overlay, every accessor returns exactly what the SHIPPED tuple gives it. Compared
# against the module's own constant in this process, not against a reading remembered at a sha.
_MERGED_NOOP = _canon.build_clusters({})
check("AC5: an EMPTY overlay leaves the cluster tuple identical to canon.CLUSTERS",
      _MERGED_NOOP == _canon.CLUSTERS, repr(_MERGED_NOOP[:2]))
check("AC5: ...and all three accessors answer identically with it and with no argument",
      _canon.build_form_index(_MERGED_NOOP) == _canon.build_form_index()
      and all(_canon.read_gloss(r, _MERGED_NOOP) == _canon.read_gloss(r)
              and _canon.render_negative(r, _MERGED_NOOP) == _canon.render_negative(r)
              for r, _g, _o in _canon.CLUSTERS))

# AC6 — the three row directions, each through build_form_index AND read_gloss AND render_negative.
#
# EVERY INDEX READ IS A `.get()`, NEVER A SUBSCRIPT, and that is not style. Reverting the merge was
# the staged break these arms exist to fail under, and with a subscript the revert raised `KeyError`
# instead: the suite CRASHED and failed no NAMED arm, which is the one outcome the build rule
# behind this file forbids. Found by running exactly that revert.
_REPLACED = _canon.build_clusters({"load": ("siphon",)})
check("AC6: a row naming an existing representative REPLACES that cluster's alternatives",
      _canon.build_form_index(_REPLACED).get("siphon") == "load"
      and "fetch" not in _canon.build_form_index(_REPLACED),
      repr(_canon.build_form_index(_REPLACED).get("fetch")))
check("AC6: ...and the other two accessors read the replacement, not the shipped tuple",
      _canon.render_negative("load", _REPLACED) == " — NOT `siphon`"
      and _canon.read_gloss("load", _REPLACED) == _canon.read_gloss("load"),
      repr(_canon.render_negative("load", _REPLACED)))

_ADDED = _canon.build_clusters({"frobnicate": ("frob", "fnord")})
check("AC6: a row naming a NEW representative ADDS a cluster",
      _canon.build_form_index(_ADDED).get("frob") == "frobnicate"
      and "frob" not in _canon.build_form_index(),
      repr(_canon.build_form_index(_ADDED).get("frob")))
check("AC6: ...and an ADDED cluster renders a negative but carries NO gloss, which is the "
      "limit S8 records",
      _canon.render_negative("frobnicate", _ADDED) == " — NOT `frob`"
      and _canon.read_gloss("frobnicate", _ADDED) == "",
      repr((_canon.render_negative("frobnicate", _ADDED),
            _canon.read_gloss("frobnicate", _ADDED))))

_DELETED = _canon.build_clusters({"-measure": ()})
check("AC6: a row leading with a minus DELETES a shipped cluster",
      "measure" not in _canon.build_form_index(_DELETED)
      and "count" not in _canon.build_form_index(_DELETED)
      and "measure" in _canon.build_form_index(),
      repr(_canon.build_form_index(_DELETED).get("count")))
check("AC6: ...and the other two accessors answer for a deleted cluster as for one never shipped",
      _canon.read_gloss("measure", _DELETED) == ""
      and _canon.render_negative("measure", _DELETED) == "",
      repr((_canon.read_gloss("measure", _DELETED),
            _canon.render_negative("measure", _DELETED))))


def read_canon_refusal(rows):
    """The refusal message `build_clusters` raises for `rows`, or `""` where it does not raise."""
    try:
        _canon.build_clusters(rows)
    except ValueError as exc:
        return str(exc)
    return ""


# AC7 — the FOUR refusals, each asserted to be TEXTUALLY DISTINCT from the other three. A config
# grammar with an undefined branch grows one by accident, and four refusals that read alike are
# one refusal wearing four hats.
#
# FOUR, not the three this block used to carry. `build_clusters`'s own docstring has named four
# since the door landed, and the missing one was the minus row that ALSO carries alternatives:
# deleting that branch left this whole suite green, because a `-build frobnicate` row then deletes
# the cluster and silently discards the alternatives the owner typed — an overlay row half of which
# did nothing, with no refusal and no report.
_DUPE = read_canon_refusal({"frobnicate": ("fetch",)})
_NOALT = read_canon_refusal({"frobnicate": ()})
_ABSENT = read_canon_refusal({"-frobnicate": ()})
_MINUSALT = read_canon_refusal({"-build": ("frobnicate",)})
check("AC7: an overlay row putting one form in TWO clusters raises",
      "two clusters" in _DUPE and "'fetch'" in _DUPE, _DUPE)
check("AC7: an ADD row carrying no alternative raises",
      "no alternative" in _NOALT, _NOALT)
check("AC7: a minus row naming no shipped cluster raises, rather than silently doing nothing",
      "does not carry" in _ABSENT, _ABSENT)
# THE ALTERNATIVES ARE NAMED BACK, which is the half a bare exit-code assertion would miss: an
# owner who typed a delete and a replacement on one row has to be told WHICH tokens the grammar
# will not honour, or the refusal sends them back to guess.
check("AC7: a minus row that ALSO carries alternatives raises, rather than deleting the cluster "
      "and discarding the alternatives it was handed",
      "must carry no alternatives" in _MINUSALT and "frobnicate" in _MINUSALT, _MINUSALT)
check("AC7: ...and the four messages are pairwise distinct",
      len({_DUPE, _NOALT, _ABSENT, _MINUSALT}) == 4
      and all((_DUPE, _NOALT, _ABSENT, _MINUSALT)),
      repr((_DUPE, _NOALT, _ABSENT, _MINUSALT)))

# AC7, ONE LEVEL UP: the two token-shape refusals in the DECLARATION READER, which are a different
# guard in a different module from the four above. `_parse_canon` validates the row's token shape and
# nothing else — the merge owns every rule about what a row MEANS — so these are the only refusals
# standing between a punctuation-carrying row and `build_clusters`. Both were revertible with the
# whole suite green: `if not head.isalpha()` replaced by `if False` let `bui-ld` reach the merge as a
# representative naming a cluster that cannot exist, and an empty `bad` list let `frob-nicate` land
# as an alternative no corpus token can ever equal. Each arm reads the file-and-line prefix too,
# because a refusal that cannot say WHERE sends the owner to grep their own declaration.
_CANON_STAMP = '\ncanon_unfrozen="2026-09-05 node a — the arms that grade the row shape"\n'
_c, _o = run_case({"core/a.py": "def build_x():\n    pass\n"},
                  BASE_CONF + _CANON_STAMP + "\nCANON:\n  bui-ld  frobnicate\n")
check("CANON: a row KEY carrying punctuation is refused at the line, rather than reaching the "
      "cluster builder as a representative no shipped cluster can match",
      _c != 0 and "a CANON representative is alphabetic" in _o and "'bui-ld'" in _o,
      f"rc={_c} {_o}")
# THE POSITION PREFIX, matched as a SHAPE rather than by the declaration's filename. The refusal is
# `f"{p}:{lineno}: …"` and what the owner needs from it is a file and a line to open, so the shape is
# the whole assertion; the filename is the run's own scratch path and naming it here would also put
# a root-install spelling in a kit file, which is what the install-prefix ban keeps out.
check("CANON: ...and the refusal carries the file-and-line prefix the owner has to open",
      bool(re.search(r"\S+:\d+: a CANON representative", _o)), _o)
_c, _o = run_case({"core/a.py": "def build_x():\n    pass\n"},
                  BASE_CONF + _CANON_STAMP + "\nCANON:\n  build  frob-nicate\n")
check("CANON: a row naming a non-alphabetic ALTERNATIVE is refused, naming the offending token",
      _c != 0 and "non-alphabetic alternative(s)" in _o and "frob-nicate" in _o, f"rc={_c} {_o}")
check("CANON: ...and that refusal is textually distinct from the row-key one, so an owner who "
      "typed punctuation on either half is told which half",
      "a CANON representative is alphabetic" not in _o, _o)

# THE MERGE REACHES THE PRODUCT, end to end, through the two calls `run_suggest` actually makes.
_OVERLAY_TAIL = '\ncanon_unfrozen="2026-09-05 node a — the arm that proves the door"\n' \
                "\nCANON:\n  build  frobnicate\n"
_OVERLAY_CONF = BASE_CONF + _OVERLAY_TAIL
# TWO OVERLAY CONFS, and the split is not cosmetic. `--suggest --as` needs a CELLS block; a `--check`
# run over a one-function fixture with that same block reds on DEAD CELL for every row the fixture
# has no population for, which would make the posture arms below pass or fail for the wrong reason.
_OVERLAY_SUGGEST_CONF = SUGGEST_CONF + _OVERLAY_TAIL
_c, _ov = run_case({"core/a.py": "def build_x():\n    pass\n"}, _OVERLAY_SUGGEST_CONF,
                   args=("--suggest", "frobnicate_thing", "--as", "py.function"))
check("S2: --suggest answers the OVERLAY's representative for a form the shipped canon cannot "
      "resolve", "use `build_thing`" in _ov, _ov)
# THE OFFSETS ARE SEARCHED, NEVER `.index()`d: a revert that removes either string would make
# `.index()` raise, and a suite that CRASHES has failed no NAMED arm.
_POSTURE_AT, _ANSWER_AT = _ov.find("CANON UNFROZEN"), _ov.find("use `build_thing`")
check("S4: ...with the posture line, naming the row count and the stamp, ABOVE the answer",
      _POSTURE_AT >= 0 and _ANSWER_AT >= 0 and _POSTURE_AT < _ANSWER_AT
      and "1 owner row(s)" in _ov and "the arm that proves the door" in _ov, _ov)
_c, _frozen = run_case({"core/a.py": "def build_x():\n    pass\n"}, SUGGEST_CONF,
                       args=("--suggest", "frobnicate_thing", "--as", "py.function"))
check("S4: ...and with NO block declared the posture line is ABSENT, so it reports a state rather "
      "than decorating every run", "CANON UNFROZEN" not in _frozen, _frozen)

# S4 on the GATE path too, green and red alike, and above the counts on both.
_c, _ov_check = run_case({"core/a.py": "def build_x():\n    pass\n"}, _OVERLAY_CONF)
_CHK_POSTURE, _CHK_COUNTS = _ov_check.find("CANON UNFROZEN"), _ov_check.find("P1 verb")
check("AC4: the posture line prints on a --check run that exits 0, above the P1 count line",
      _c == 0 and _CHK_POSTURE >= 0 and _CHK_COUNTS >= 0 and _CHK_POSTURE < _CHK_COUNTS,
      f"rc={_c} {_ov_check}")
_c, _ov_red = run_case({"core/a.py": "def build_x():\n    pass\n\n\ndef frobnicate_it():\n    pass\n"},
                       _OVERLAY_CONF)
check("AC4: ...and on a run that exits non-zero",
      _c != 0 and "CANON UNFROZEN" in _ov_red, f"rc={_c} {_ov_red}")
check("AC4: ...where the overlay has made the offender DEBT rather than UNRULED, which is the "
      "merge reaching the offender line and not only the index",
      "rename to `build_it`" in _ov_red, _ov_red)

# S2 — THE PAIRING ITSELF: `read_debt_gloss` resolves the representative out of the merged INDEX and
# reads the gloss out of the merged TUPLE, and both arguments have to travel together. Passing a
# merged index beside the shipped tuple was the defect two revisions of this unit's spec carried,
# and every arm above is blind to it: on a REPLACE row the gloss is the shipped one either way, and
# an ADD row carries no gloss at all in either tuple. The ONE overlay that separates them deletes a
# shipped cluster and re-adds it under the same representative — legal in this grammar, two rows —
# which drops the shipped gloss while leaving the representative standing. `measure` is the cluster
# because `BASE_CONF` declares no row for it, so the declaration cannot supply the gloss instead.
_REGLOSS_CONF = BASE_CONF \
    + '\ncanon_unfrozen="2026-09-05 node a — the arm that pairs the index with the tuple"\n' \
      "\nCANON:\n  -measure\n  measure  count\n"
_c, _regloss = run_case({"core/a.py": "def count_rows():\n    pass\n"}, _REGLOSS_CONF)
check("S2: the DEBT line resolves its representative through the MERGED index",
      _c != 0 and "rename to `measure_rows`" in _regloss, _regloss)
check("S2: ...and reads its gloss out of the MERGED tuple, not the shipped one",
      "no gloss declared" in _regloss and "count a population" not in _regloss, _regloss)

# AC13 — F2's attribution line, observed in BOTH directions. An arm that only ever sees the line
# cannot tell it from the bare mismatch the ratchet already prints.
_AC13_FILES = {"core/a.py": "def frobnicate_a():\n    pass\n\n\ndef fetch_b():\n    pass\n"}
_c, _no_cause = run_case(_AC13_FILES, _PINNED_VOCAB)
check("AC13: without an overlay this fixture is GREEN, so the movement below is the overlay's",
      _c == 0, _no_cause)
# THE PHRASE, not the word. A bare `"CAUSE" not in …` matches inside `BECAUSE` and would report on
# a string this arm does not gate — the same defect one level down as an arm searching a whole file
# for its figure.
_CAUSE_LINE = "CAUSE — the CANON overlay is unfrozen"
check("AC13: ...and no CAUSE line is printed on it", _CAUSE_LINE not in _no_cause, _no_cause)
_AC13_OVERLAY = _PINNED_VOCAB \
    + '\ncanon_unfrozen="2026-09-05 node a — the arm that proves the cause"\n' \
      "\nCANON:\n  build  frobnicate\n"
_c, _cause = run_case(_AC13_FILES, _AC13_OVERLAY)
check("AC13: a stamped overlay MOVES the P1 pins, exactly as owner ruling Q2 makes it",
      _c != 0 and "py.function.debt MOVED 1 -> 2" in _cause
      and "py.function.unruled MOVED 1 -> 0" in _cause, _cause)
check("AC13: ...and the run names the OVERLAY as the cause, not the bare mismatch alone",
      _CAUSE_LINE in _cause and "1 owner row(s)" in _cause, _cause)
# The redistribution fixture from AC9 above moves the same two rows with NO overlay declared. This
# is the arm that stops the CAUSE line from decaying into a second spelling of "MOVED".
check("AC13: ...while the SAME two rows moving with no overlay carry no CAUSE line",
      "MOVED" in _redis and _CAUSE_LINE not in _redis, _redis)

# S7 — the structural guard, and its own failing case. The scaffold derives from the corpus; an
# overlay it proposed would be the mirror arriving through the door built for a human.
_c, _guard_green = run_case(_SPLIT_FILES, _SPLIT_CONF)
check("AC8: with no `CANON:` header in the scaffold's emitted body, the run exits 0",
      _c == 0 and "SCAFFOLD EMITS" not in _guard_green, _guard_green)
_c, _guard_red = run_case(
    _SPLIT_FILES, _SPLIT_CONF,
    patch=("scaffold_lexicon.py", 'body.append("")',
           'body.append("CANON:")\n    body.append("")'))
check("AC8: ...and with one staged into it the run exits non-zero, naming the file and the line",
      _c != 0 and "SCAFFOLD EMITS A `CANON:` BLOCK HEADER" in _guard_red
      and "scaffold_lexicon.py:" in _guard_red, _guard_red)
# THE THIRD STATE, and it was a SILENT PASS. The guard's `if _scaffold.is_file()` carried no `else`,
# so deleting or renaming the file it reads turned a structural refusal into a green run that said
# nothing — a skip wearing a pass's clothes, over the one arm standing between the scaffold and the
# canon door. The kit copy is run with that file DROPPED, which is the only way this branch is
# reachable at all: the guard reads the installed kit, never a fixture corpus.
check("AC8: ...and with the file PRESENT nothing is announced, so the line below reports a state",
      "SCAFFOLD GUARD SKIPPED" not in _guard_green, _guard_green)
# THIS FILE GOES WITH IT, and the reason is worth a line: `selftest.py` imports `scaffold_lexicon`
# for the shared-catalog arm, so dropping the scaffolder alone reds the SELF-CONTAINMENT guard on a
# dangling sibling import — a real refusal, but a different one, and an arm asserting the run stays
# green would have been measuring that instead. The pair is what an adopter who took the kit without
# the scaffolder actually has.
_c, _guard_gone = run_case(_SPLIT_FILES, _SPLIT_CONF,
                           drop=("scaffold_lexicon.py", "selftest.py"))
check("AC8: an ABSENT scaffold ANNOUNCES the skip and names the file it could not read",
      "SCAFFOLD GUARD SKIPPED" in _guard_gone and "scaffold_lexicon.py" in _guard_gone,
      _guard_gone)
check("AC8: ...and says the arm went UNEXERCISED rather than letting a green row read as verified",
      "UNEXERCISED" in _guard_gone, _guard_gone)
check("AC8: ...and it is a REPORT, so an adopter who took the kit without the scaffolder is green",
      _c == 0, f"rc={_c} {_guard_gone}")
# AC9 — the NEAR-MISS the narrowed predicate deliberately does not count, pinned here so a later
# reader knows the loose form's count of 1 is by design rather than an oversight.
_SCAFFOLD_SRC = (KIT / "scaffold_lexicon.py").read_text(encoding="utf-8").splitlines()
_LOOSE = [i + 1 for i, ln in enumerate(_SCAFFOLD_SRC) if "CANON" in ln]
_NARROW = [i + 1 for i, ln in enumerate(_SCAFFOLD_SRC) if _lex._CANON_HEADER_RE.search(ln)]
check("AC9: the narrowed predicate matches nothing in the shipped scaffold", not _NARROW,
      repr(_NARROW))
check("AC9: ...while the LOOSE form matches exactly one line, the descriptive comment it would "
      "have forced a rewording of", len(_LOOSE) == 1
      and "PROPOSED from the SHIPPED CANON" in _SCAFFOLD_SRC[_LOOSE[0] - 1], repr(_LOOSE))

# S5 — THE RECORDED HALF OF THE DOOR, on `adopt-lexicon.sh --check`, and it was the largest hole in
# this unit. NOTHING exercised either stamp refusal: this repo declares no `CANON:` block, so the
# row-count guard arming them is false on every real bar, and replacing that guard with a constant
# false deleted BOTH refusals with every leg in the suite still green. The mechanism that enforces
# RECORDING is the one mechanism that must not be silently removable, because a quiet unfreeze is
# the mirror defect with an extra step.
#
# EVERY CASE RUNS THE SCRIPT and asserts its MESSAGE, never its exit code: `check_skill` reds in a
# sandbox that carries no rendered Skill, so all four runs are non-zero whatever the stamp says and
# an exit-code arm here would pass on the Skill and prove nothing about the door.
_STAMP: dict = {}
for _label, _tail in (
        ("empty", "\nCANON:\n  build  frobnicate\n  load  hydrate\n"),
        ("noreason", '\ncanon_unfrozen="2026-09-05 node a"\n\nCANON:\n  build  frobnicate\n'),
        ("stamped", '\ncanon_unfrozen="2026-09-05 node a — our stores are `hydrate`"\n'
                    "\nCANON:\n  load  hydrate\n"),
        ("frozen", "\n")):
    with build_tempdir() as _td:
        _sroot = Path(_td)
        shutil.copytree(KIT, _sroot / "tools" / "lexicon",
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        (_sroot / ".lexicon.conf").write_text(BASE_CONF + _tail, encoding="utf-8", newline="\n")
        subprocess.run(["git", "init", "-q"], cwd=_sroot, check=True)
        _sr = subprocess.run(["bash", "tools/lexicon/adopt-lexicon.sh", "--check"], cwd=_sroot,
                             capture_output=True, text=True)
        _STAMP[_label] = _sr.stdout + _sr.stderr
_EMPTY_STAMP_MSG = "declares a CANON: overlay"
_NO_REASON_MSG = "stamp carries no REASON"
check("S5: a `CANON:` block with an EMPTY `canon_unfrozen` is REFUSED by the wiring leg",
      _EMPTY_STAMP_MSG in _STAMP["empty"], _STAMP["empty"])
# THE COUNT IS THE GUARD. A refusal that fires is not evidence the ROWS were read — the two-row
# fixture is what separates a derived count from a constant, and the derivation is the half a
# `if false` revert removes.
check("S5: ...and the refusal reports the row count it read through the declaration reader",
      "(2 row(s))" in _STAMP["empty"], _STAMP["empty"])
check("S5: a stamp carrying a date and a node but NO reason is refused, under its own wording",
      _NO_REASON_MSG in _STAMP["noreason"] and _EMPTY_STAMP_MSG not in _STAMP["noreason"],
      _STAMP["noreason"])
check("S5: ...so the two refusals are distinguishable rather than one refusal wearing two hats",
      _EMPTY_STAMP_MSG in _STAMP["empty"] and _EMPTY_STAMP_MSG not in _STAMP["noreason"]
      and _NO_REASON_MSG in _STAMP["noreason"] and _NO_REASON_MSG not in _STAMP["empty"],
      repr((_STAMP["empty"][:80], _STAMP["noreason"][:80])))
check("S5: a reason-bearing stamp draws NEITHER refusal, so the two above are not a wall",
      _EMPTY_STAMP_MSG not in _STAMP["stamped"] and _NO_REASON_MSG not in _STAMP["stamped"],
      _STAMP["stamped"])
check("S5: ...and a declaration with no block draws neither either, which is the FROZEN state "
      "every adopter who is not the author sits in",
      _EMPTY_STAMP_MSG not in _STAMP["frozen"] and _NO_REASON_MSG not in _STAMP["frozen"],
      _STAMP["frozen"])

# AC12 gets NO arm here, and that is deliberate rather than missed: it is a `grep` over two
# documents, one of which is an adopter's own curated declaration. An arm asserting a sentence in
# that file would red every adopter whose conf predates this kit version — a gate on prose nobody
# but this repo can satisfy. §7 of the spec files it as a landing observation for the same reason.

# ---- TOOL-aSurfacedLexicon-8: `--suggest` becomes surface-aware -----------------------------------
#
# EVERY ARM BELOW NAMES THE DECLARATION IT IS MEASURED AGAINST, which is `SUGGEST_CONF` and never the
# tracked one: the tracked declaration arms two cells, so a criterion phrased against any other cell
# would observe this unit's OWN undeclared-cell refusal instead of the behaviour it asserts.


def read_suggestion(out: str) -> str:
    """The name `--suggest` proposed, as the FIRST backticked token of a `use ...` line, or `""`.

    Asserting the answer by VALUE rather than by substring, for the reason the round-2 review found
    one level up: the message template always prints the verb it wants, so a substring assertion
    passes on the template rather than on the suggestion.
    """
    for line in out.splitlines():
        if line.startswith("use `"):
            return line.split("`")[1]
    return ""


# AC1 — the banned TAIL, named in the answer. `FooManager` leads with `foo`, which is neither
# declared nor banned, so before this unit it exited on the "not in the declared table" branch
# answering about the wrong end of the name entirely.
#
# THE ARMING IS THE SURFACE, NOT A FLAG, since closing review B2: P2 grades every extracted type
# whatever any `CELLS` row says, so `--suggest` runs the tail check on any `type` cell and the
# `notail` flag — whose only reader was the branch that made the two surfaces disagree — is gone from
# the grammar. This row now declares `py.type  pascal` and nothing else, and the arm reads the
# message the surface arming prints.
_c, _o = run_case(_U10, SUGGEST_CONF, args=("--suggest", "FooManager", "--as", "py.type"))
check("AC1: a `type` cell answers about the banned SUFFIX, naming it",
      _c == 0 and "`Manager`" in _o and "P2 bans on the `type` surface" in _o, _o)
check("AC1: ...and does not answer about the leading token instead",
      "not in the declared table" not in _o, _o)

# AC2 — the everyday defect this unit exists to remove: the swap answered in the CALLER's case on a
# cell that declares another one.
_c, _o = run_case(_U10, SUGGEST_CONF, args=("--suggest", "fetchUserData", "--as", "py.function"))
check("AC2: a camel name on a snake cell comes back re-cased, verb swapped",
      _c == 0 and read_suggestion(_o) == "load_user_data", f"got {read_suggestion(_o)!r} | {_o}")

# AC3 — `--as` is REQUIRED. Asserted on the exit code AND on the REQUIRED-flag wording, because the
# obvious form was satisfied by the wrong refusal: with the guard in `main` deleted, `cell_spec` is
# the empty string, `resolve_cell` refuses it as a malformed cell key, and that message spells
# `--as` too — so an arm greping for the bare flag scored a pass on a run that had no guard at all.
# A message that passes for the wrong reason is the fixture-passes-by-finding-nothing class, so
# both halves are asserted: the wording only the guard prints, and the ABSENCE of the refusal that
# stands in for it.
_c, _o = run_case(_U10, SUGGEST_CONF, args=("--suggest", "fetchUserData"))
check("AC3: --suggest with no --as exits 2 under the REQUIRED-flag refusal",
      _c == 2 and "--as is REQUIRED" in _o, f"rc={_c} {_o}")
check("AC3: ...and not under the malformed-cell refusal, which names the same flag",
      "MALFORMED" not in _o and "BARE SURFACE" not in _o, _o)

# AC4 — THE ROUND-2 REGRESSION CORPUS, asserted by value on a camel cell.
#
# WHICH ARM PROVES WHAT, corrected: `getUserURLs` NEVER REACHES THE SPAN LOOP. The swap answers
# `readUserURLs`, `classify` already calls that camel, and `render_convention` returns it untouched
# on its own first line — so that row grades `render_swapped_name` and says nothing whatever about
# the re-caser's span rebuild. It is kept, because the splice is exactly what round 1 broke; the
# fourth row below is the one that carries the CASE claim, and it was missing.
_AC4 = (("getUserURLs", "readUserURLs"),     # the SWAP; the re-caser returns this one unchanged
        ("fetch_v2_data", "loadV2Data"),     # separators: re-supplied, so dropped rather than refused
        # THE SPAN PATH, with case to lose. The swap gives `load_userURLs`, which satisfies no
        # convention at all, so the loop runs — and the acronym run is a NON-LEADING span whose
        # interior case only survives because the renderer re-cases the first character and passes
        # the rest of the caller's own surface through. Rebuilding the span instead answers
        # `loadUserUrLs`, which is still legal camel, so no self-check and no classifier can catch
        # it: this row is the only thing standing between that spelling and the product.
        ("fetch_userURLs", "loadUserURLs"),
        # LAST ON PURPOSE — the arm below this loop reads the FINAL iteration's output.
        ("create$data", "build$data"))       # `$`: NOT re-supplied, so refused rather than re-spelled
for _bad, _want in _AC4:
    _c, _o = run_case(_U10, SUGGEST_CONF, args=("--suggest", _bad, "--as", "js.function"))
    check(f"AC4: {_bad} --as js.function -> {_want}",
          _c == 0 and read_suggestion(_o) == _want, f"got {read_suggestion(_o)!r} | {_o}")
check("AC4: ...and the refused one SAYS it was not re-cased, rather than answering silently",
      "NOT re-cased" in _o, _o)

# AC4a — THE RENDERER'S OWN FINAL GUARD, which nothing reached. `create$data` above is refused one
# test EARLIER, at the unseen-character check, so `return out if convention in classify(out) else ""`
# could be cut to `return out` and every arm in this file stayed green. `2fa_check` is the input that
# lands on it: every character outside a span is an underscore, so the character test passes and the
# loop builds `2FaCheck` — which no camel name may be, because camel opens with a lower-case letter
# and this opens with a digit. Called DIRECTLY, because both refusals print the one `NOT re-cased`
# line and only the return value tells them apart.
check("AC4a: a render the convention does not accept is REFUSED rather than printed",
      _lex.render_convention("2fa_check", "camel") == "",
      repr(_lex.render_convention("2fa_check", "camel")))
check("AC4a: ...and it is the CLASSIFIER refusing the renderer's OWN output, which is the guard",
      "camel" not in _lex.classify("2FaCheck") and not _lex.classify("2fa_check"),
      repr((sorted(_lex.classify("2FaCheck")), sorted(_lex.classify("2fa_check")))))

# AC5 — a `file` cell takes a BASENAME and grades `read_stem`'s stem: the basename up to its FIRST
# dot. `map_extractors.template.py` is the input that makes the rule visible — a last-dot rule would
# grade `map_extractors.template` and answer differently.
_c, _o = run_case(_U10, SUGGEST_CONF,
                  args=("--suggest", "checkKitPlaceholders.py", "--as", "py.file"))
check("AC5: a file cell re-cases the STEM of the basename",
      _c == 0 and read_suggestion(_o) == "check_kit_placeholders",
      f"got {read_suggestion(_o)!r} | {_o}")
_c, _o = run_case(_U10, SUGGEST_CONF,
                  args=("--suggest", "map_extractors.template.py", "--as", "py.file"))
check("AC5: ...stemming at the FIRST dot, so a compound extension answers unchanged",
      _c == 0 and "map_extractors" in _o and "map_extractors.template" not in _o, _o)
check("AC5: ...and a cell arming neither flag runs no verb check at all",
      "not in the declared table" not in _o and "NOT `" not in _o, _o)

# AC6 — the `dark` refusal. Distinct from the undeclared one, which AC9 compares it against.
_c, _DARK = run_case(_U10, SUGGEST_CONF, args=("--suggest", "fetchUserData", "--as", "sh.file"))
check("AC6: a dark cell refuses rather than answering, and exits non-zero",
      _c != 0 and "dark" in _DARK, f"rc={_c} {_DARK}")

# AC7 — `leading_verb`'s contract, preserved. Its population is the underscore-only and the
# non-ASCII names; a DIGIT-leading name is graded rather than refused.
for _u in ("__", "_", "é"):
    _c, _o = run_case(_U10, SUGGEST_CONF, args=("--suggest", _u, "--as", "py.function"))
    check(f"AC7: {_u!r} is UNGRADEABLE and nothing is re-spelled for it",
          _c == 0 and "ungradeable" in _o and read_suggestion(_o) == "", _o)

# AC9 — the UNDECLARED refusal, and its second half: with the cell's row gone, the same run refuses.
_c, _UNDECL = run_case(_U10, SUGGEST_CONF, args=("--suggest", "FooBar", "--as", "ts.type"))
check("AC9: an undeclared cell refuses, exits non-zero, names the cell and says UNDECLARED",
      _c != 0 and "ts.type" in _UNDECL and "UNDECLARED" in _UNDECL, f"rc={_c} {_UNDECL}")
_c, _o = run_case(_U10, BASE_CONF, args=("--suggest", "FooBar", "--as", "py.type"))
check("AC9: ...and a declaration carrying NO CELLS block refuses every cell the same way",
      _c != 0 and "UNDECLARED" in _o, f"rc={_c} {_o}")
check("AC9: ...and that refusal is TEXTUALLY DISTINCT from the dark one",
      _UNDECL != _DARK and _UNDECL and _DARK, f"{_UNDECL!r} vs {_DARK!r}")

# AC10 — MALFORMED, over a table of shapes rather than the one that was typed first. The selector'd
# key is the S9 boundary: `--as` addresses the parent cell and the selector is applied from the name.
_MALFORMED = []
for _spec in ("py..function", "pyfunction", "py.function.extra", "py.function+prefix:cmd_"):
    _c, _o = run_case(_U10, SUGGEST_CONF, args=("--suggest", "fetchUserData", "--as", _spec))
    _MALFORMED.append(_o)
    check(f"AC10: `--as {_spec}` refuses as MALFORMED and exits non-zero",
          _c != 0 and "MALFORMED" in _o, f"rc={_c} {_o}")
check("AC10: ...and the malformed refusal differs from the undeclared one",
      all(_m != _UNDECL for _m in _MALFORMED), _MALFORMED[0])

# AC11 — the BARE SURFACE refusal is a MENU. The cell list is the clause that makes it one, so the
# arm reads the list rather than only the exit code.
_c, _BARE = run_case(_U10, SUGGEST_CONF, args=("--suggest", "fetchUserData", "--as", "function"))
check("AC11: a bare surface refuses, exits non-zero, and LISTS the declared cells carrying it",
      _c != 0 and "BARE SURFACE" in _BARE and "py.function" in _BARE and "js.function" in _BARE,
      f"rc={_c} {_BARE}")
check("AC11: ...and does not list a cell on another surface",
      "py.type" not in _BARE and "md.file" not in _BARE, _BARE)
check("AC11: ...and its message differs from the malformed one",
      all(_m != _BARE for _m in _MALFORMED), _BARE)

# AC12 — THE CONVENTION-ONLY PATH. Nothing is wrong with this name but its case, and the leading
# token IS declared, so before this unit it returned an `OK` line before any convention check ran.
_c, _o = run_case(_U10, SUGGEST_CONF, args=("--suggest", "buildUserIndex", "--as", "py.function"))
check("AC12: a declared verb in the wrong case still gets an answer",
      _c == 0 and read_suggestion(_o) == "build_user_index", f"got {read_suggestion(_o)!r} | {_o}")
check("AC12: ...and the answer names the convention the input currently satisfies",
      "camel" in _o and "snake" in _o, _o)

# S9 — a `prefix` selector is applied FROM THE NAME, the way the grader applies it, so a cell can
# answer differently for `cmd_*` than for its complement. A `decorator` selector cannot be resolved
# from an identifier, so the parent answers and SAYS SO.
_c, _o = run_case(_U10, SUGGEST_CONF, args=("--suggest", "cmd_fetch_thing", "--as", "py.function"))
check("S9: a name matching a prefix selector is answered in the SELECTOR's convention",
      _c == 0 and read_suggestion(_o) == "cmdFetchThing", f"got {read_suggestion(_o)!r} | {_o}")
_c, _o = run_case(_U10, SUGGEST_CONF, args=("--suggest", "fetch_thing", "--as", "py.function"))
check("S9: ...while its complement is answered in the parent's",
      _c == 0 and read_suggestion(_o) == "load_thing", f"got {read_suggestion(_o)!r} | {_o}")
check("S9: a decorator selector on the cell is DISCLOSED rather than silently ignored",
      "decorator" in _o and "cannot be resolved from an identifier" in _o, _o)

# THE AFFIX THE RE-CASER PUTS BACK. `render_convention` splits the name into a leading run of
# underscores, a core and a trailing run, re-cases the core alone, and re-attaches both runs. Every
# arm above passes a name with no affix at all, so dropping either re-attachment left the whole
# suite green while the tool answered `_load_user_data` as `load_user_data` — a suggestion that
# renames a module-private function into a public one, in a re-caser whose own docstring calls
# itself the one place in the kit that WRITES a name instead of grading one.
#
# TWO ARMS, ONE PER RUN, because one name carrying both affixes cannot tell the two re-attachments
# apart: it reds whichever is dropped and names neither.
_c, _o = run_case(_U10, SUGGEST_CONF, args=("--suggest", "_fetchUserData", "--as", "py.function"))
check("affix: a LEADING underscore survives the re-case, so a private name stays private",
      _c == 0 and read_suggestion(_o) == "_load_user_data", f"got {read_suggestion(_o)!r} | {_o}")
_c, _o = run_case(_U10, SUGGEST_CONF, args=("--suggest", "fetchUserData_", "--as", "py.function"))
check("affix: a TRAILING underscore survives the re-case, so a keyword-avoiding name keeps the "
      "character that avoids the keyword",
      _c == 0 and read_suggestion(_o) == "load_user_data_", f"got {read_suggestion(_o)!r} | {_o}")

# ---- the three STAGED BREAKS, each redding a NAMED arm ------------------------------------------
#
# A mechanism is not landed until reverting it reds an arm by name. Each break below is applied to a
# copy of the kit in a throwaway repo and the arm it is supposed to red is re-run there.

# BREAK 1 — the re-caser rebuilds from `subtokens()` instead of from the spans. This is the round-1
# body, verbatim in its behaviour: no already-satisfies early return, no unseen-character refusal,
# and every token lowercased.
_SPAN_BODY = """    if convention in classify(name):
        return name
    lead, core, trail = _AFFIX.match(name).group(1, 2, 3)
    spans = list(_SUBTOKEN_RE.finditer(core))
    if not spans:
        return ""
    covered = {i for m in spans for i in range(*m.span())}
    if any(c not in _SEPARATORS for i, c in enumerate(core) if i not in covered):
        return ""
    toks = []
    for i, m in enumerate(spans):
        t = m.group(0)"""
_REBUILD_BODY = """    lead, core, trail = _AFFIX.match(name).group(1, 2, 3)
    spans = list(_SUBTOKEN_RE.finditer(core))
    if not spans:
        return ""
    toks = []
    for i, t in enumerate(subtokens(core)):
        t = t"""
for _bad, _want in (_AC4[0], _AC4[2]):
    _c, _o = run_case(_U10, SUGGEST_CONF, args=("--suggest", _bad, "--as", "js.function"),
                      patch=("subtokens.py", _SPAN_BODY, _REBUILD_BODY))
    check(f"STAGED: a subtokens-rebuild re-caser REDS the AC4 arm for {_bad}",
          read_suggestion(_o) != _want, f"stayed green with {read_suggestion(_o)!r} | {_o}")
# `fetch_v2_data` is deliberately NOT in that loop and the omission is measured rather than assumed:
# its expected answer is byte-identical under a slice and under a lowercased rebuild, because every
# character it carries is already lowercase. It is redded by BREAK 2 instead, and an arm that cannot
# fail under a break is worth naming rather than counting.

# BREAK 2 — the refusal predicate WIDENED to every unseen character, which is the form fork F1
# rejected. It refuses every separator-bearing name asked for in a camel cell and hands back the
# caller's own snake spelling, which the camel predicate then reds.
for _bad, _want in (("fetch_v2_data", "loadV2Data"), ("fetch_remote", "loadRemote")):
    _c, _o = run_case(_U10, SUGGEST_CONF, args=("--suggest", _bad, "--as", "js.function"),
                      patch=("subtokens.py", '_SEPARATORS = "_-"', '_SEPARATORS = ""'))
    check(f"STAGED: the WIDE unseen-character refusal REDS the camel answer for {_bad}",
          read_suggestion(_o) != _want, f"stayed green with {read_suggestion(_o)!r} | {_o}")

# BREAK 3 — the renderer wired ONLY into the banned-verb branch, which is what a reader of the old
# Inventory would have built. Every other arm here greens through it; AC12's `:806`-equivalent exit
# is the one that reds.
_c, _o = run_case(_U10, SUGGEST_CONF, args=("--suggest", "buildUserIndex", "--as", "py.function"),
                  patch=("lexicon.py", "    recased = render_convention(answer, conv)",
                         "    recased = render_convention(answer, conv) if want else answer"))
check("STAGED: a renderer reached only from the banned-verb branch REDS AC12",
      read_suggestion(_o) != "build_user_index", f"stayed green | {_o}")
_c, _o = run_case(_U10, SUGGEST_CONF, args=("--suggest", "fetchUserData", "--as", "py.function"),
                  patch=("lexicon.py", "    recased = render_convention(answer, conv)",
                         "    recased = render_convention(answer, conv) if want else answer"))
check("STAGED: ...while AC2's banned-verb arm stays GREEN through that same break, which is why "
      "AC12 had to exist",
      read_suggestion(_o) == "load_user_data", f"got {read_suggestion(_o)!r} | {_o}")

# ---- closing-review left-shifts (the CODE review, round 1) --------------------------------------
#
# One arm per finding, each with its own staged break where a break is stageable. The grouping is
# the review's, not this file's, so a reader holding the report can find the row.

# M3 — `--suggest` used to RESOLVE an overlap the grader REFUSES. `read_routed_cell` returned the
# first prefix selector in dict order while `scan_routes` calls that resolution disqualifying in its
# own docstring and grades the name by NEITHER cell. Two verdicts, one name, and the confident one
# came from the verb an author reads BEFORE writing.
_AMBIG_CONF = ('BANNED_SUFFIXES="Manager"\n'
               'LANGS="py:python-ast:parser conf::dark"\n'
               'VERB_OFFENDER_PIN="1"\nSUFFIX_OFFENDER_PIN="0"\n'
               'ratified="2026-09-06 node a"\n\n'
               'CELLS:\n'
               '  py.function  snake\n\n'
               '  py.function+prefix:Test  pascal\n\n'
               '  py.function+prefix:Te  camel\n\n'
               'VERBS:\n'
               '  build   create a new value and return it - NOT `create`\n')
_AMBIG_FILES = {"core/a.py": "def TestThing():\n    pass\n"}
_c, _o = run_case(_AMBIG_FILES, _AMBIG_CONF)
check("M3: --check refuses an overlapping-selector name as AMBIGUOUS SELECTOR",
      _c != 0 and "AMBIGUOUS SELECTOR" in _o and "graded by NEITHER" in _o, _o)
_c, _o = run_case(_AMBIG_FILES, _AMBIG_CONF, args=("--suggest", "TestThing", "--as", "py.function"))
check("M3: ...and --suggest refuses the SAME name with the SAME wording rather than picking a row",
      _c == 2 and "AMBIGUOUS SELECTOR" in _o and "+prefix:Test" in _o and "+prefix:Te" in _o, _o)
_c, _o = run_case(_AMBIG_FILES, _AMBIG_CONF, args=("--suggest", "TestThing", "--as", "py.function"),
                  patch=("lexicon.py", "    if len(hits) > 1:", "    if False:"))
check("STAGED: collapsing the overlap check to the FIRST hit makes --suggest answer confidently "
      "where --check refuses",
      _c == 0 and "AMBIGUOUS" not in _o, f"rc={_c} {_o}")

# M2 — three `PINS` shapes that parsed, passed `check_declaration`, and were graded by nothing. The
# refusal is DERIVED (declared keys minus consumed keys), so each shape below is an instance of one
# arm rather than three hand-written cases.
_M2_FILES = {"core/a.py": "def build_x():\n    pass\n\n\nclass Widget:\n    pass\n"}
_M2_BASE = ('BANNED_SUFFIXES="Manager"\n'
            'LANGS="py:python-ast:parser conf::dark"\n'
            'VERB_OFFENDER_PIN="0"\nSUFFIX_OFFENDER_PIN="0"\n'
            'ratified="2026-09-06 node a"\n\n'
            'VERBS:\n  build   create a new value and return it - NOT `create`\n\n')
_c, _o = run_case(_M2_FILES, _M2_BASE + "CELLS:\n  py.function  snake\n\n  py.type  dark\n\n"
                                        "PINS:\n  py.type.conv  777\n")
check("M2: a `.conv` pin on a `dark` cell is refused as an UNREAD PIN",
      _c != 0 and "UNREAD PIN" in _o and "py.type.conv" in _o, _o)
_c, _o = run_case(_M2_FILES, _M2_BASE + "CELLS:\n  py.function  snake\n\n  py.type  pascal\n\n"
                                        "PINS:\n  py.function.debt  9999\n\n"
                                        "  py.function.unruled  4242\n")
check("M2: a `.debt`/`.unruled` pair on a cell with no `vocab` flag is refused the same way",
      _c != 0 and "UNREAD PIN" in _o
      and "py.function.debt" in _o and "py.function.unruled" in _o, _o)
# THE CONTROL, and it is the half that stops this arm redding every honest declaration: the SAME
# rows on a cell that DOES arm `vocab` are consumed, so they must not appear in the refusal.
_c, _o = run_case(_M2_FILES, _M2_BASE + "CELLS:\n  py.function  snake  vocab\n\n  py.type  pascal\n\n"
                                        "PINS:\n  py.function.debt  0\n\n"
                                        "  py.function.unruled  0\n")
check("M2 control: the same pair on a `vocab` cell is consumed and NOT reported unread",
      "UNREAD PIN" not in _o, _o)
check("M2: and the third shape cannot be declared at all — `suffix` left PIN_PREDICATES",
      "suffix" not in _lc.PIN_PREDICATES, str(_lc.PIN_PREDICATES))

# H4 — the `PATTERNS REPLACES` report had exactly one arm and it asserted ABSENCE, so it passed
# precisely when the mechanism was deleted. This is the positive twin, over a SHIPPED key.
_JS_REPLACE = (BASE_CONF.replace('LANGS="py:python-ast:parser conf::dark"',
                                 'LANGS="py:python-ast:parser conf::dark js:js-regex:probe"')
               + "\nPATTERNS:\n"
                 r"  js-regex.types  ^\s*class\s+([A-Za-z_$][\w$]*)" "\n"
               + "\nCELLS:\n  py.function  dark\n  js.function  dark\n  js.type  dark\n")
_c, _o = run_case({"core/a.py": "def build_x():\n    pass\n",
                   "web/w.js": "class Widget {}\n"}, _JS_REPLACE)
check("H4: a PATTERNS row landing on a SHIPPED extractor key PRINTS the REPLACES line, naming it",
      "PATTERNS REPLACES a SHIPPED extractor key" in _o and "js-regex.types" in _o, _o)
_c, _o = run_case({"core/a.py": "def build_x():\n    pass\n",
                   "web/w.js": "class Widget {}\n"}, _JS_REPLACE,
                  patch=("lexicon.py",
                         "        over = [k for k in patterns if k.split(\".\")[0] in PATTERN_SETS]",
                         "        over = []"))
check("STAGED: deleting the REPLACES computation reds that arm rather than passing green",
      "PATTERNS REPLACES a SHIPPED extractor key" not in _o, _o)

# M4 — `render_swapped_name`'s case-inheritance branches. Replacing the three-branch block with
# `cased = want` left the whole suite green and both CLI modes byte-identical, because every AC
# input is lowercase-leading and `--suggest` re-cases the answer afterwards, masking the difference.
# The one unmasked consumer is the P1 DEBT detail line, so the arm reads THAT.
_M4_FILES = {"core/a.py": "def FetchThing():\n    pass\n\n\ndef GETData():\n    pass\n"}
_M4_CONF = ('BANNED_SUFFIXES="Manager"\n'
            'LANGS="py:python-ast:parser conf::dark"\n'
            'VERB_OFFENDER_PIN="2"\nSUFFIX_OFFENDER_PIN="0"\n'
            'ratified="2026-09-06 node a"\n\n'
            'CELLS:\n  py.function  dark\n\n'
            'VERBS:\n  build   create a new value and return it - NOT `create`\n')
_c, _o = run_case(_M4_FILES, _M4_CONF, args=("--list",))
check("M4: the DEBT rename inherits a PASCAL-led caller's case", "`LoadThing`" in _o, _o)
check("M4: ...and a SCREAMING-led caller's", "`READData`" in _o, _o)
_c, _o = run_case(_M4_FILES, _M4_CONF, args=("--list",),
                  patch=("lexicon.py", "    return lead + cased + rest",
                         "    return lead + want + rest"))
check("STAGED: dropping the case-inheritance branches reds BOTH M4 arms",
      "`LoadThing`" not in _o and "`READData`" not in _o, _o)

# L1 — the `<<-` tab-stripping terminator match. `git grep -l -- '<<-' -- '*.sh'` returns nothing in
# this repo, so the branch was correct code with zero coverage; reverted, the tokenizer runs past the
# heredoc into the next definition and raises `unterminated heredoc`, which the walk turns into a
# `declared 'parser' but does not parse` refusal — a red gate for any adopter whose shell uses `<<-`.
_L1_SH = ("run_it() {\n"
          "\tcat <<-EOF\n"
          "\tbody line\n"
          "\tEOF\n"
          "}\n"
          "\n"
          "build_after() {\n"
          "\t:\n"
          "}\n")
_L1_CONF = ('BANNED_SUFFIXES="Manager"\n'
            'LANGS="sh:shell-tokens:parser conf::dark"\n'
            'VERB_OFFENDER_PIN="1"\nSUFFIX_OFFENDER_PIN="0"\n'
            'ratified="2026-09-06 node a"\n\n'
            'CELLS:\n  sh.function  snake\n\n'
            'VERBS:\n  build   create a new value and return it - NOT `create`\n')
_c, _o = run_case({"bin/x.sh": _L1_SH}, _L1_CONF)
check("L1: a `<<-` heredoc with a TAB-indented terminator parses, and the definition after it is "
      "reached", _c == 0 and "does not parse" not in _o, _o)
_c, _o = run_case({"bin/x.sh": _L1_SH}, _L1_CONF,
                  patch=("lexicon.py", r'(raw.lstrip("\t") if strip else raw) == delim',
                         "raw == delim"))
check("STAGED: dropping the tab strip turns that file into an unterminated heredoc refusal",
      _c != 0 and "does not parse" in _o, _o)

# L3 — `check_self_containment`'s UNJUDGED branch. Every SIBLING branch is staged; this one reads as
# covered by association and its failing case had never been observed. It decides whether a broken
# sibling module degrades the walk silently or reds.
with build_tempdir() as _td:
    _kit = build_kit_copy(Path(_td) / "kitL3")
    _victim = _kit / "subtokens.py"
    _victim.write_text(_victim.read_text(encoding="utf-8") + "\ndef (:\n",
                       encoding="utf-8", newline="\n")
    _problems, _mods, _imports = lex.check_self_containment(_kit)
    check("L3: a sibling module that will not parse is reported UNJUDGED, naming the file",
          any("UNJUDGED" in p and "subtokens.py" in p for p in _problems), str(_problems))

# L4 — the `cannot be read as source` refusal, split from the SyntaxError one precisely because the
# two say different things. Nothing exercised the distinction, so a future edit re-merging them reds
# nothing. Reachable in the wild: `tracked_files` does not filter for existence.
with build_tempdir() as _td:
    _rr = Path(_td)
    shutil.copytree(KIT, _rr / "tools" / "lexicon",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (_rr / "core").mkdir()
    (_rr / "core" / "a.py").write_text("def build_x():\n    pass\n", encoding="utf-8", newline="\n")
    (_rr / "core" / "gone.py").write_text("def build_y():\n    pass\n", encoding="utf-8",
                                          newline="\n")
    (_rr / ".lexicon.conf").write_text(_L4_CONF := _M2_BASE + "CELLS:\n  py.function  snake\n",
                                       encoding="utf-8", newline="\n")
    subprocess.run(["git", "init", "-q"], cwd=_rr, check=True)
    subprocess.run(["git", "add", "--", "core", ".lexicon.conf"], cwd=_rr, check=True,
                   capture_output=True)
    (_rr / "core" / "gone.py").unlink()          # TRACKED, and no longer on disk
    _r = subprocess.run([sys.executable, "tools/lexicon/lexicon.py"], cwd=_rr,
                        capture_output=True, text=True)
    _o = _r.stdout + _r.stderr
    check("L4: a tracked file missing from the worktree is refused as `cannot be read as source`",
          _r.returncode != 0 and "cannot be read as source" in _o and "gone.py" in _o, _o)
    check("L4: ...and NOT as `does not parse`, which is the distinction the split bought",
          "gone.py: declared `parser` but does not parse" not in _o, _o)

# H3 — THE IDIOM IS BANNED, not the instance. `cell.split(".")[1]` reads a cell key by position and
# is wrong for every selector'd row: on `py.file+prefix:test` it answers `file+prefix:test`. That
# defect was live in `run_suggest` (a false refusal on a stem the gate SATISFIES) and mis-labelling
# in two `check_pass` messages, which is three instances of one habit — so the arm gates the habit.
# `parse_cell_key` is the one reader of a cell key in this kit.
_ENGINE_LINES = (KIT / "lexicon.py").read_text(encoding="utf-8").splitlines()
_SPLIT_HITS = [f"{_i}: {_ln.strip()}" for _i, _ln in enumerate(_ENGINE_LINES, 1)
               if not _ln.lstrip().startswith("#") and "cell.split(" in _ln]
check("H3: `cell.split(` appears in no CODE line of lexicon.py — parse_cell_key is the one reader",
      not _SPLIT_HITS, "; ".join(_SPLIT_HITS))
# ...and the predicate is shown to MATCH, over a synthetic line rather than over the tracked file.
# A ban asserted only by its own silence is the arm-that-cannot-fail shape one level up: a typo in
# the needle would read exactly like a clean tree.
check("H3: ...and the predicate actually matches that idiom when it is present",
      "cell.split(" in '    ext = cell.split(".")[0]'
      and not '    ext = cell.split(".")[0]'.lstrip().startswith("#"))
check("H3: ...and does not fire on a COMMENT naming it, which this file and the engine both do",
      '    # the surface test was cell.split(".")[1]'.lstrip().startswith("#"))

# H2 — the rendered Skill described the pin as one-sided long after every pin became a two-sided
# equality, and `--check` byte-compares a render against a render, so the sentence was GATED AS
# CORRECT and could not drift into notice. The template is the source; this arm reads it.
_TPL = (KIT / "SKILL.template.md").read_text(encoding="utf-8")
check("H2: the Skill template describes no pin as one-sided",
      "exceeds the declared pin" not in _TPL and "over the declared pin" not in _TPL, _TPL[:400])
check("H2: ...and says TWO-SIDED, in the section that grades",
      "TWO-SIDED EQUALITY" in _TPL, _TPL[:400])


# ---- the cross-surface arm's call sites, and the breaks that red it -----------------------------
#
# THE REAL TREE IS THE FIRST CALL SITE and it is the point of the whole arm: the supply half was
# only ever measured against scratch declarations, so it answered `OK` for names this repo's own bar
# reds on. Asked here against THIS declaration and THIS corpus.


def read_agreement(root, patch=None):
    """`(rc, output)` from the cross-surface arm over `root`, optionally against a PATCHED kit copy.

    `patch` is `(kit-file, old, new)` and is applied to a COPY, never to this tree. The replacement
    is ASSERTED, like `run_case`'s: a patch whose `old` has moved would leave the arm grading an
    unmodified engine and scoring a pass, which is the arm-that-cannot-fail class the break exists
    to disprove.
    """
    if patch is None:
        _r = subprocess.run([sys.executable, str(KIT / "selftest.py"), "--agree", str(root)],
                            capture_output=True, text=True)
        return _r.returncode, _r.stdout + _r.stderr
    _rel, _old, _new = patch
    _f = Path(root) / "tools" / "lexicon" / _rel
    _src = _f.read_text(encoding="utf-8")
    if _old not in _src:
        raise SystemExit(f"selftest: agreement patch target not found in {_rel}: {_old!r}")
    _f.write_text(_src.replace(_old, _new), encoding="utf-8", newline="\n")
    _r = subprocess.run([sys.executable, str(Path(root) / "tools" / "lexicon" / "selftest.py"),
                         "--agree", str(root)], capture_output=True, text=True)
    _f.write_text(_src, encoding="utf-8", newline="\n")
    return _r.returncode, _r.stdout + _r.stderr


def read_agree_field(out, key):
    """One `key=<int>` field out of the arm's summary line, or -1 if the line never printed."""
    _m = re.search(rf"\b{key}=(\d+)\b", out)
    return int(_m.group(1)) if _m else -1


_GOV_ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                           cwd=str(KIT))
_GOV_ROOT = Path(_GOV_ROOT.stdout.strip()) if _GOV_ROOT.returncode == 0 else None
if _GOV_ROOT is not None and (_GOV_ROOT / ".lexicon.conf").is_file():
    _rc, _out = read_agreement(_GOV_ROOT)
    check("AGREE: --check and --suggest agree on THIS repo's own corpus, verdict and cell",
          _rc == 0, _out)
    # A LIVENESS ASSERTION ON BOTH COUNTERS, because an arm reporting zero disagreements over zero
    # names is indistinguishable from a clean run and is the whole class this file exists against.
    check("AGREE: ...and the arm actually asked this repo something",
          read_agree_field(_out, "asked") > 0, _out)
    check("AGREE: ...and made at least one CELL assertion, not verdicts alone",
          read_agree_field(_out, "cell_assertions") > 0, _out)
else:
    # THE SKIP ANNOUNCES ITSELF rather than passing. An adopter running this suite in a tree with no
    # declaration has not exercised the arm, and a green row there would say otherwise.
    check("AGREE: SKIPPED over the host repo — no .lexicon.conf at its root, so the arm's real-tree "
          "half went UNEXERCISED on this run (reported, not a pass)", True)


# THE SECOND CALL SITE IS A FIXTURE WITH A ROUTED `file` CELL, and it exists because this repo's own
# declaration carries no selector at all — H3, M1 and M3 are three defects on a code path with zero
# in-corpus population. `core/check_arms.py` stems to `check_arms`, which the `+prefix:check` row
# claims and `kebab` reds, while the parent row would call it clean: one file, two cells, and the
# only fixture shape in which the two surfaces can be caught disagreeing.
_ROUTED_CONF = ('BANNED_SUFFIXES="Manager"\n'
                'LANGS="py:python-ast:parser conf::dark"\n'
                'VERB_OFFENDER_PIN="0"\nSUFFIX_OFFENDER_PIN="0"\n'
                'ratified="2026-09-06 node a"\n\n'
                'CELLS:\n'
                '  py.function  snake\n\n'
                '  py.file  snake\n\n'
                '  py.file+prefix:check  kebab\n\n'
                'VERBS:\n'
                '  build   create a new value and return it - NOT `create`\n')
with build_tempdir() as _td:
    _rr = Path(_td)
    shutil.copytree(KIT, _rr / "tools" / "lexicon",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (_rr / "core").mkdir()
    (_rr / "core" / "check_arms.py").write_text("def build_thing():\n    pass\n",
                                                encoding="utf-8", newline="\n")
    # `fetch_thing` IS THIS FIXTURE'S P1 OFFENDER, and it is here because BREAK B needs one. Without
    # it every function in the corpus leads with a declared verb, so gating P1 on a flag nothing arms
    # changes no answer and the break scores a pass. Measured rather than assumed: the first cut of
    # this fixture carried only `build_*` names and BREAK B came back GREEN.
    (_rr / "core" / "plain_mod.py").write_text(
        "def build_other():\n    pass\n\n\ndef fetch_thing():\n    pass\n",
        encoding="utf-8", newline="\n")
    (_rr / ".lexicon.conf").write_text(_ROUTED_CONF, encoding="utf-8", newline="\n")
    subprocess.run(["git", "init", "-q"], cwd=_rr, check=True)
    subprocess.run(["git", "add", "--", "core", ".lexicon.conf"], cwd=_rr, check=True,
                   capture_output=True)

    _rc, _out = read_agreement(_rr)
    check("AGREE: the two surfaces agree over a corpus with a ROUTED file cell", _rc == 0, _out)
    check("AGREE: ...and the routed fixture made cell assertions of its own",
          read_agree_field(_out, "cell_assertions") > 0, _out)

    # BREAK A — M1, restored as the one line it was: route on the caller's RAW argument instead of
    # on the graded stem. The grader's `scan_routes` matches on the stem, so a `file` cell asked
    # with a path misses the `+prefix:` row here and hits it there. Both halves of the arm red, and
    # they red for different reasons — the verdict half because the parent's `snake` calls
    # `check_arms` clean, the cell half because the answer names the parent rather than the routed
    # row. The sibling defect H3 (the surface tested with `cell.split(".")[1]` AFTER routing) is not
    # separately stageable: once the stemming precedes the routing there is no ordering left for it
    # to occupy. It was staged by hand at the fix and is recorded in the closing-review fold.
    _rc, _out = read_agreement(_rr, patch=(
        "lexicon.py",
        'read_routed_cell(conf.get("CELLS") or {}, cell, graded)',
        'read_routed_cell(conf.get("CELLS") or {}, cell, name)'))
    check("STAGED: routing on the caller's RAW argument rather than the graded stem REDS the arm",
          _rc != 0, _out)
    check("STAGED: ...on the VERDICT half", read_agree_field(_out, "verdict_bad") > 0, _out)
    check("STAGED: ...and on the CELL half, which is the one no verdict could show",
          read_agree_field(_out, "cell_bad") > 0, _out)

    # BREAK B — the B2 defect itself: P1 gated on the cell's `vocab` flag, which the grader does not
    # read. The routed fixture declares no flag on any row, so every function in it becomes a name
    # the grader calls an offender and the advisor calls OK.
    _rc, _out = read_agreement(_rr, patch=(
        "lexicon.py",
        '    graded_by_p1 = surface == PREDICATE_SURFACES["verb"] and bool(verbs)',
        '    graded_by_p1 = "vocab" in flags'))
    check("STAGED: gating P1 on the `vocab` flag the grader never reads REDS the arm",
          _rc != 0 and read_agree_field(_out, "verdict_bad") > 0, _out)


if FAILURES:
    print(f"lexicon selftest FAILED — {len(FAILURES)} of {PASSES + len(FAILURES)} arm(s):")
    for f in FAILURES:
        print(f"  - {f}")
    raise SystemExit(1)
print(f"lexicon selftest OK — {PASSES} arm(s)")
