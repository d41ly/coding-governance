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


def check(label: str, cond: bool, detail: str = "") -> None:
    global PASSES
    if cond:
        PASSES += 1
    else:
        FAILURES.append(f"{label}{(' — ' + detail) if detail else ''}")


def run_case(files: dict, conf: str | None, waivers: dict | None = None, args: tuple = ()):
    """Build a throwaway repo, run the engine in it, return (exit_code, output)."""
    with build_tempdir() as td:
        root = Path(td)
        shutil.copytree(KIT, root / "tools" / "lexicon",
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
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
    conf_text = (root / ".lexicon.conf").read_text(encoding="utf-8")
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
    _seeded = load_conf(root / "seed.conf")["VERBS"]
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
# it made a number that moves when somebody writes a tutorial. Measured on the real tree: including
# `.md` reported 25.7% against 42.2%.
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

code, out = run_case(_U10, BASE_CONF, args=("--suggest", "build_index"))
check("--suggest: a declared verb answers OK and exits 0", code == 0 and out.startswith("OK"), out)

code, out = run_case(_U10, BASE_CONF, args=("--suggest", "fetch_remote"))
check("--suggest: an off-table token names the REPLACEMENT from the NOT clause",
      code == 0 and "load_remote" in out and "`load`" in out and "`fetch`" in out, out)
check("--suggest: ...and quotes the negative definition rather than only the token",
      "NOT `fetch`" in out, out)

code, out = run_case(_U10, BASE_CONF, args=("--suggest", "frobnicate_thing"))
check("--suggest: a token NO row bans says so, and still exits 0",
      code == 0 and "no row bans it by name" in out, out)

# S6 — the structural guards. A report that can exit 1, or that prints a pin, is a gate.
for _v in (("--suggest", "fetch_remote"),):
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
for _bad, _want in (
        ("fetch_remote", "load_remote"),
        ("_fetch_conf", "_load_conf"),
        ("__fetch_conf", "__load_conf"),
        ("fetchRemoteThing", "loadRemoteThing"),
        ("_fetchRemoteThing", "_loadRemoteThing"),
        ("fetch", "load"),
        ("_fetch", "_load"),
        # The shapes the round-2 review measured, where rebuilding the tail from `subtokens()` lost
        # information the original surface carried. Each was CORRECT before round 1 touched it, or
        # correct in neither version; all are correct now because the tail is sliced, not rebuilt.
        ("fetch_v2_data", "load_v2_data"),          # digit boundary: was `load_v_2_data`
        ("fetch_2fa", "load_2fa"),                  # digit boundary at the head of a token
        ("fetchXMLParser", "loadXMLParser"),        # acronym run: was `loadXmlParser`
        ("fetchHTTPServerData", "loadHTTPServerData"),
        ("FetchUserData", "LoadUserData"),          # PascalCase: the verb inherits the case
        ("FETCH_USER_DATA", "LOAD_USER_DATA"),      # SCREAMING_SNAKE, likewise
        ("fetch-user-data", "load-user-data"),      # kebab: the separator is the caller's
        ("fetch_conf_", "load_conf_"),              # trailing underscore survives
        ("__fetch__", "__load__"),                  # ...on both ends
):
    _c, _o = run_case(_U10, BASE_CONF, args=("--suggest", _bad))
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
    check(f"--suggest preserves shape and object: {_bad} -> {_want}",
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
                     BASE_CONF + "\nCELLS:\n  py.file  kebab\n\nPINS:\n  py.function.debt  3\n")
check("AC6: a PINS row with no CELLS row reds --check by cell",
      code != 0 and "py.function" in out and "has no CELLS row" in out, out)
code, out = run_case({"core/a.py": "def build_index():\n    pass\n"},
                     BASE_CONF + "\nCELLS:\n  py.file  kebab\n\n  py.function  snake\n\n"
                                 "PINS:\n  py.function.debt  3\n")
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
             "  py.file.conv  7\n\n  py.function.debt  9\n\n  py.type.suffix  4\n")
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

# The declared-but-unexercised surface ANNOUNCES itself. `constant` is in the closed surface set and
# this kit ships no extractor for it, so a cell naming it must say so rather than report a clean 0 —
# the population and its rule belong to the unit that arms `py.constant`.
code, out = run_case(_CLEAN, BASE_CONF + "\nCELLS:\n  py.constant  screaming\n")
check("a surface with no extractor is announced as UNEXERCISED, not reported at zero",
      "py.constant.conv SKIPPED" in out and "UNEXERCISED" in out, out)

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
_TS_CELLS = "\nCELLS:\n  ts.function  camel\n  ts.type      pascal\n"
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

if FAILURES:
    print(f"lexicon selftest FAILED — {len(FAILURES)} of {PASSES + len(FAILURES)} arm(s):")
    for f in FAILURES:
        print(f"  - {f}")
    raise SystemExit(1)
print(f"lexicon selftest OK — {PASSES} arm(s)")
