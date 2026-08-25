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
LAYER_OFFENDER_PIN="0"
ratified="2026-08-16 node d"

VERBS:
  build   create a new value and return it — NOT `create`
  load    read from a store into memory — NOT `fetch`
  add     append to an existing collection — NOT `push`

LAYERS:
  core/* -> adapters/*
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
        for name in ("lexicon-verb-waivers.txt", "lexicon-suffix-waivers.txt", "lexicon-layer-waivers.txt"):
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


# BOTH sides of the declared layer rule exist in every BASE_CONF fixture. The reachability arm reds a
# rule whose globs select nothing, and these fixtures declared `core/* -> adapters/*` while supplying
# only one side — so they were unreachable too, and the arm caught its own test data first.
LAYER_SIDES = {"adapters/db.py": "def build_db():\n    pass\n",
               "core/thing.py": "def build_thing():\n    pass\n"}

# ---- P1: the verb predicate ---------------------------------------------------------------------
code, out = run_case({"core/a.py": "def build_index():\n    pass\n", **LAYER_SIDES}, BASE_CONF)
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
code, out = run_case({"core/a.py": "def build_x():\n    pass\n\n\nclass Manager:\n    pass\n", **LAYER_SIDES}, BASE_CONF)
check("P2 red: a type named EXACTLY the banned suffix reds", code != 0 and "P2 suffix" in out, out)

# The F-A3 arm: a blanket ban breaks on contact with imported names and parameters. P2 is scoped to
# DEFINITION sites only, so neither of these is an offender.
code, out = run_case(
    {"core/a.py": "from elsewhere import ThingManager\n\n\ndef build_x(widget_manager, other: ThingManager):\n"
                  "    return ThingManager\n", **LAYER_SIDES},
    BASE_CONF)
check("P2 green: an IMPORTED type and a parameter carrying the suffix do not red", code == 0, out)

# ---- P3: the layer predicate --------------------------------------------------------------------
code, out = run_case({"core/a.py": "import adapters.db\n\n\ndef build_x():\n    pass\n"}, BASE_CONF)
check("P3 red: a forbidden import direction reds", code != 0 and "P3 layer" in out, out)

code, out = run_case({"adapters/a.py": "import core.thing\n\n\ndef build_x():\n    pass\n", **LAYER_SIDES}, BASE_CONF)
check("P3 green: the ALLOWED direction passes", code == 0, out)

# AC3 — an empty LAYERS block must report NOT ARMED and RED, never pass green over an absent
# declaration. This is the arm that keeps the predicate from being decorative in a fresh adopter.
code, out = run_case({"core/a.py": "def build_x():\n    pass\n"},
                     BASE_CONF.split("LAYERS:")[0] + "LAYERS:\n")
check("P3 unarmed: an empty LAYERS reds", code != 0, out)
check("P3 unarmed: it says NOT ARMED", "NOT ARMED" in out, out)

# AC3b — THE PRODUCTION SHAPE. The arms above use `core/*` -> `adapters/*` with `import adapters.db`,
# where the namespace happens to spell the path. That coincidence is what let a DEAD rule ship: this
# repo's real declaration names `tools/codebase-map/`, a directory whose hyphen NO module name can
# contain, and the flat `sys.path`-insert import that actually reaches it is a bare stem sharing no
# characters with its directory. Both arms below reproduce that shape, because a fixture easier than
# production certifies coverage the production rule does not have.
HYPHEN_CONF = BASE_CONF.split("LAYERS:")[0] + "LAYERS:\n  pkg/consumer/* -> pkg/shared-core/*\n"
code, out = run_case(
    {"pkg/consumer/a.py": "import shared_thing\n\n\ndef build_x():\n    pass\n",
     "pkg/shared-core/shared_thing.py": "def build_y():\n    pass\n"},
    HYPHEN_CONF)
check("P3 red: a BARE-STEM import into a HYPHENATED directory is caught", code != 0 and "P3 layer" in out, out)

code, out = run_case(
    {"pkg/consumer/a.py": "import unrelated_thing\n\n\ndef build_x():\n    pass\n",
     "pkg/consumer/unrelated_thing.py": "def build_z():\n    pass\n",
     "pkg/shared-core/shared_thing.py": "def build_y():\n    pass\n"},
    HYPHEN_CONF)
check("P3 green: a bare-stem import NOT under the forbidden dir is silent", code == 0, out)

# The reachability arm — the third vacuity defence. `NOT ARMED` tests whether LAYERS is EMPTY and
# DEAD PROBE tests whether an extractor selects anything; neither tests whether a NON-EMPTY rule can
# ever fire. A rule naming a directory that does not exist is the checkable form of that.
code, out = run_case({"core/a.py": "def build_x():\n    pass\n"},
                     BASE_CONF.split("LAYERS:")[0] + "LAYERS:\n  core/* -> nowhere/at-all/*\n")
check("P3 unselective: a rule whose TO glob matches no tracked file reds", code != 0, out)
check("P3 unselective: it says UNSELECTIVE", "UNSELECTIVE" in out, out)

# The OTHER end of the same check. Both branches need an arm or one of them is a claim nobody tests.
code, out = run_case({"core/a.py": "def build_x():\n    pass\n", **LAYER_SIDES},
                     BASE_CONF.split("LAYERS:")[0] + "LAYERS:\n  nowhere/at-all/* -> adapters/*\n")
check("P3 unselective: a rule whose FROM glob matches no tracked file reds",
      code != 0 and "UNSELECTIVE" in out, out)

# H1 — the stem lookup is SCOPED. Unscoped it returned every tracked file sharing a basename, so a
# LOCAL sibling import resolved into the forbidden directory it never touches. The only escape would
# have been a waiver, which then permanently silences the genuine violation it was hiding.
code, out = run_case(
    {"pkg/consumer/a.py": "import helper\n\n\ndef build_x():\n    pass\n",
     "pkg/consumer/helper.py": "def build_local():\n    pass\n",
     "pkg/shared-core/helper.py": "def build_far():\n    pass\n"},
    HYPHEN_CONF)
check("P3 green: an importer-local file WINS over a same-stem file in the forbidden dir", code == 0, out)

# And the extension half of that scoping: a `.py` import never denotes a `.md`.
code, out = run_case(
    {"pkg/consumer/a.py": "import notes\n\n\ndef build_x():\n    pass\n",
     "pkg/shared-core/notes.md": "# not a module\n"},
    HYPHEN_CONF.replace('LANGS="py:python-ast:parser conf::dark"',
                        'LANGS="py:python-ast:parser conf::dark md::dark"'))
check("P3 green: a same-stem file of a DIFFERENT extension is not a resolution", code == 0, out)

# H1 — a RELATIVE specifier must resolve against the IMPORTER's directory. Swapping dots for slashes
# mangles `../shared-core/x.js` into `///shared-core/x/js` and matches nothing, which made the
# predicate structurally incapable for the commonest JS import shape.
JS_CONF = ('BANNED_SUFFIXES="Manager"\nLANGS="js:js-regex:probe conf::dark"\n'
           'VERB_OFFENDER_PIN="9"\nSUFFIX_OFFENDER_PIN="0"\nLAYER_OFFENDER_PIN="0"\n'
           'ratified="2026-08-16 node d"\n\nVERBS:\n  build  make a thing\n\n'
           'LAYERS:\n  pkg/consumer/* -> pkg/shared-core/*\n')
code, out = run_case(
    {"pkg/consumer/a.js": "import x from '../shared-core/thing.js'\nexport function buildA(){}\n",
     "pkg/shared-core/thing.js": "export function buildB(){}\n"},
    JS_CONF)
check("P3 red: a RELATIVE js specifier resolves against the importer's dir", code != 0 and "P3 layer" in out, out)

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
code, out = run_case({"core/a.py": "def frobnicate_index():\n    pass\n", **LAYER_SIDES}, BASE_CONF,
                     {"lexicon-verb-waivers.txt": "frobnicate_index  deliberate, see the spec\n"})
check("a waiver on the matched TEXT silences its offender", code == 0, out)

# The whole reason for text keying: `install-prefix-waivers.txt` keys on <path>:<line>, so any edit
# ABOVE a waived line unpins it and reds a merge that touched nothing the waiver guards.
code, out = run_case({"core/a.py": "# a new comment line added above\n# and another\ndef frobnicate_index():\n    pass\n", **LAYER_SIDES},
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

# ---- CASE TABLES over the two helpers that carry P3's whole correctness --------------------------
# THIS IS THE LEFT-SHIFT, and it is the arm whose absence let three review rounds through. Every P3
# defect so far lived in `_glob_match` or `resolve_import`, and NOT ONE was visible to an end-to-end
# fixture: reverting the `_glob_match` rewrite verbatim left all 48 fixture arms green while the live
# gate stayed at exit 0. A fixture exercises a PATH through the engine; a case table exercises the
# FUNCTION. Both are needed and only one of them was here.
import lexicon as _lex  # noqa: E402

GLOB_CASES = [
    # (path, pattern, expected, why this row exists)
    ("tools/lexicon/a.py", "tools/lexicon/*", True, "the plain depth-1 case"),
    ("tools/lexicon/deep/a.py", "tools/lexicon/*", True, "a `<dir>/*` pattern covers nesting"),
    ("tools/other/a.py", "tools/lexicon/*", False, "a sibling directory must not match"),
    # THE B2 ROW. A wildcard EARLIER in the pattern used to be escaped literally by the nesting
    # branch, so this pair red at depth 1 and passed GREEN at depth 2.
    ("apps/a/internal/x.py", "apps/*/internal/*", True, "wildcard before the trailing /*, depth 1"),
    ("apps/a/internal/deep/x.py", "apps/*/internal/*", True, "the same pattern must still nest"),
    ("apps/a/public/x.py", "apps/*/internal/*", False, "the earlier wildcard is not a free pass"),
    # THE ANCHORING ROWS. The unanchored fallback accepted any path sharing a literal PREFIX, with
    # no path boundary required — this is the pair that catches it, and it is a real corpus shape.
    ("tools/lexicon-extra/a.py", "tools/lexicon/*", False, "a prefix that is not a path boundary"),
    ("tools/lexicon-extra", "tools/lexicon*", True, "a single * matches within one segment"),
    ("tools/lexicon-extra/a.py", "tools/lexicon*", False, "and a single * never crosses a slash"),
    # NOT a row: a doubled-slash path. `git ls-files` never emits one and the only thing that ever
    # produced it here was the deleted reachability synthetic. Treating it as nested is correct and
    # asserting otherwise would be testing malformed input the corpus cannot contain. Written down
    # because the first draft of this table DID assert it, and the table caught the author.
    ("tools/lexicon", "tools/lexicon/*", False, "the bare directory is not a member of `<dir>/*`"),
]
for path, pattern, want, why in GLOB_CASES:
    got = _lex._glob_match(path, pattern)
    check(f"glob: {path} vs {pattern} -> {want} ({why})", got == want, f"got {got}")

# `resolve_import` — what an import target may DENOTE. The index is a small fixed corpus so each row
# states the whole world it resolves against.
RI_INDEX = _lex.build_module_index([
    "src/pkg/consumer/a.py",
    "src/pkg/consumer/helper.py",
    "src/pkg/shared_core/helper.py",
    "src/pkg/shared_core/only_there.py",
    "src/pkg/shared_core/notes.md",
    "web/consumer/a.js",
    "web/shared/thing.js",
    # These three exist so the rows below can FAIL. Without them the arms passed because the corpus
    # held nothing to match, not because the code was right — a vacuous row is worse than no row,
    # and three of these were vacuous when first written.
    "web/shared/debounce.js",
    "web/shared/thingamajig/thing.js",
    "outside/thing.js",
])
IMPORTER_PY = "src/pkg/consumer/a.py"
TARGET_GLOB = "src/pkg/shared_core/*"


def _check_reaches(target, importer=IMPORTER_PY, glob=TARGET_GLOB):  # noqa: E302
    return any(_lex._glob_match(c, glob) for c in _lex.resolve_import(target, importer, RI_INDEX))


# THE B1 ROW. Importer-local precedence was applied to a FULLY-QUALIFIED dotted import, where the
# language grants the importer's directory none — so the genuine crossing resolved to the local
# sibling and vanished.
check("resolve: a FULLY-QUALIFIED dotted import reaches the forbidden layer even with a same-stem "
      "local sibling", _check_reaches("pkg.shared_core.helper"), "the B1 false negative is back")
check("resolve: a BARE import prefers the importer-local sibling",
      not _check_reaches("helper"), "importer-local precedence lost")
check("resolve: a bare import with NO local sibling still resolves across",
      _check_reaches("only_there"), "the stem lookup stopped working")
check("resolve: a same-stem file of a DIFFERENT extension is not a resolution",
      not _check_reaches("notes"), "extension scoping lost")
check("resolve: a relative js specifier resolves against the importer's dir",
      _check_reaches("../shared/thing.js", "web/consumer/a.js", "web/shared/*"),
      "relative resolution lost")
check("resolve: an unresolvable/external target denotes nothing",
      not _check_reaches("json"), "an external import must not resolve into the corpus")

# ---- round-4 rows. Written BEFORE the code that satisfies them. -----------------------------------
# The rev-9 fix keyed precedence on `"." in target`, which is a PYTHON namespace rule applied to
# every language, and gave a dotted target no directory scoping at all. It fixed one false negative
# and bought two false positives. These rows pin the design that replaces it: a dotted target
# resolves only to a candidate whose path is CONSISTENT with the dots.

# B1 — `from <pkg> import <name>`. The parser kept only `node.module`, discarding the imported NAME,
# so the commonest Python crossing spelling resolved to nothing.
_frm = _lex._python_defs("from pkg.shared_core import helper\n")[2]
check("extract: `from a.b import c` yields a target naming c, not just a.b",
      any(t.endswith("helper") for t, _ln in _frm), f"{_frm}")
check("resolve: `from pkg.shared_core import helper` reaches the forbidden layer",
      any(_check_reaches(t) for t, _ln in _frm), f"{_frm}")

# H1/H2 — the false positives that fix bought. Neither import touches this repo.
check("resolve: a dotted target whose PATH does not match is NOT a crossing (concurrent.helper)",
      not _check_reaches("concurrent.helper"), "false positive: any same-stem file matched")
check("resolve: nor thirdparty.helper", not _check_reaches("thirdparty.helper"),
      "false positive: any same-stem file matched")
check("resolve: a dotted target whose path DOES match is still a crossing",
      _check_reaches("pkg.shared_core.helper"), "path-consistent dotted resolution lost")

# H2 — a JS specifier is not a Python namespace. NOTE ON WHAT THIS ROW PINS: it is satisfied by the
# path-consistency rule as well as by the language branch, so it does NOT on its own prove the branch
# exists — verified by reverting the branch and watching this row stay green. It is kept because the
# behaviour is worth pinning; the row BELOW is the one that distinguishes the branch.
check("resolve: a JS bare specifier containing a dot does not resolve into the corpus",
      not _check_reaches("lodash.debounce", "web/consumer/a.js", "web/shared/*"),
      "a dotted JS specifier resolved onto a same-stem file")

# THE ROW THAT PINS THE LANGUAGE BRANCH. A leading dot means RELATIVE-TO-PACKAGE in Python and
# nothing of the sort elsewhere, and only the Python branch decodes `node.level`. `from . import
# helper` must resolve to the importer's OWN package, never to a same-stem file in the forbidden one.
_rel = _lex._python_defs("from . import helper\n")[2]
check("extract: a relative `from . import x` keeps its level as leading dots",
      any(t.startswith(".") for t, _ln in _rel), f"{_rel}")
check("resolve: `from . import helper` stays in the importer's own package",
      not any(_check_reaches(t) for t, _ln in _rel), f"{_rel}")
check("resolve: and it DOES resolve locally rather than to nothing",
      any(_check_reaches(t, IMPORTER_PY, "src/pkg/consumer/*") for t, _ln in _rel), f"{_rel}")

# A relative specifier that walks ABOVE the repo root is EXTERNAL, not clamped back in — clamping
# fabricates a candidate inside the repo and can invent a violation.
check("resolve: a relative specifier escaping the repo root denotes nothing",
      not _check_reaches("../../../outside/thing.js", "web/consumer/a.js", "outside/*"),
      "the walk was clamped at the root instead of failing")

# H3 — the relative branch matched on a bare `startswith`, with no path boundary: the exact defect
# class the glob anchoring removed, alive in the sibling helper.
# The exploit needs a DIRECTORY sharing the prefix, not a same-stem sibling: the stem index already
# constrains candidates to an exact basename, so `thingamajig.js` could never reach the comparison.
# The first version of this row asserted the wrong shape and passed under both implementations —
# caught by reverting the fix and seeing the suite stay green.
check("resolve: a relative specifier matches on a PATH BOUNDARY, not a prefix",
      not _check_reaches("../shared/thing", "web/consumer/a.js", "web/shared/thingamajig/*"),
      "boundary-free prefix match in the relative branch")

# H4 — `**` collapsed to `[^/]*[^/]*`, so it could not cross a slash and `<dir>/**` selected
# strictly LESS than `<dir>/*`.
for path, pattern, want, why in [
    ("a/b/c.py", "a/**", True, "** crosses slashes"),
    ("a/b.py", "a/**", True, "and still matches at depth 1"),
    ("z/b/c.py", "a/**", False, "but not another tree"),
    ("a/bc.py", "a/b?.py", True, "? matches exactly one character"),
    ("a/bcd.py", "a/b?.py", False, "and not two"),
]:
    got = _lex._glob_match(path, pattern)
    check(f"glob: {path} vs {pattern} -> {want} ({why})", got == want, f"got {got}")

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

# ---- verdict ------------------------------------------------------------------------------------
# ---- TOOL-dScaffoldedMirror-2: per-predicate populations, counts on green, an honest --measure ----
#
# WHAT THESE ARE NOT. None of them asserts a VERDICT change: this unit reports, and section 3 of its
# spec forbids moving an exit code except `--measure`'s. So every arm below reads OUTPUT, and the two
# that read an exit code read `--measure`'s, which is the one this unit is allowed to move.

_U2 = {"core/a.py": "def build_index():\n    pass\n", **LAYER_SIDES}

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

_U6 = {"core/a.py": "def build_index():\n    pass\n", **LAYER_SIDES}

code, out = run_case(_U6, BASE_CONF)
check("coverage: the fraction prints on a GREEN run",
      code == 0 and "coverage - armed" in out.replace("\u2014", "-").replace(chr(8212), "-")
      and "definition-carrying file(s)" in out, out)

# DERIVED, not a constant: an unarmed shell file joins the denominator and the fraction falls.
_SH_CONF = BASE_CONF.replace('LANGS="py:python-ast:parser conf::dark"',
                             'LANGS="py:python-ast:parser conf::dark sh::dark"')
code, out2 = run_case({**_U6, "scripts/go.sh": "build_it() {\n  :\n}\n"}, _SH_CONF)
check("coverage: an unarmed definition-carrying file LOWERS the fraction",
      code == 0 and "armed 3 of 4" in out2, out2)

# The PROSE judgement, armed. A fenced example inside documentation is not a definition, and counting
# it made a number that moves when somebody writes a tutorial. Measured on the real tree: including
# `.md` reported 25.7% against 42.2%.
_MD = "Example:\n\n```python\ndef build_thing():\n    pass\n```\n"
_MD_CONF = BASE_CONF.replace('LANGS="py:python-ast:parser conf::dark"',
                             'LANGS="py:python-ast:parser conf::dark md::dark"')
code, out3 = run_case({**_U6, "docs/guide.md": _MD}, _MD_CONF)
check("coverage: a fenced code block in PROSE does not join the denominator",
      code == 0 and "armed 3 of 3" in out3, out3)

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

code, out = run_case({"core/a.py": "def build_index():\n    pass\n", **LAYER_SIDES}, _S6_OK)
check("S6: a table whose every row carries a negative is silent",
      code == 0 and "carrying no negative" not in out, out)

# A row with no negative cannot draw a boundary, and the gate message degrades to "not in the table".
_S6_BARE = _S6_OK.replace("  load    read from a store into memory \u2014 NOT `fetch`",
                          "  load    read from a store into memory")
check("S6 fixture really differs (or the next arm proves nothing)", _S6_BARE != _S6_OK, "replace missed")
code, out = run_case({"core/a.py": "def build_index():\n    pass\n", **LAYER_SIDES}, _S6_BARE)
check("S6: a row with NO negative is a finding", code != 0 and "carrying no negative" in out, out)
check("S6: ...and it names the row", "load" in out.split("carrying no negative")[1][:80], out)

# A token that is both banned and declared bans and permits itself at once.
_S6_CLASH = _S6_OK.replace("NOT `fetch`", "NOT `add`")
check("S6 clash fixture really differs", _S6_CLASH != _S6_OK, "replace missed")
code, out = run_case({"core/a.py": "def build_index():\n    pass\n", **LAYER_SIDES}, _S6_CLASH)
check("S6: a banned token that is itself a row is a finding",
      code != 0 and "itself a row" in out, out)
check("S6: ...and it names the token", "add" in out.split("itself a row")[1][:60], out)

# ---- TOOL-dScaffoldedMirror-10: the two SUPPLY verbs ---------------------------------------------
#
# Every arm here asserts that neither verb can behave like a gate. That is S6, and it is the property
# that keeps "what the corpus does" from becoming "what the corpus should do": a report that can exit
# 1 is a gate with a softer name.

_U10 = {"core/a.py": "def build_index():\n    pass\n",
        "core/b.py": "def render_index():\n    pass\n", **LAYER_SIDES}

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
for _v in (("--suggest", "fetch_remote"), ("--brief", "core/a.py")):
    code, out = run_case(_U10, BASE_CONF, args=_v)
    check(f"S6: {_v[0]} never exits 1", code != 1, f"rc={code} {out}")
    check(f"S6: {_v[0]} prints no pin figure",
          "_OFFENDER_PIN" not in out and "over pin" not in out, out)

# --brief keys on the OBJECTS this file names, and reports every spelling live for each.
code, out = run_case(_U10, BASE_CONF, args=("--brief", "core/a.py"))
check("--brief: reports the file's object", code == 0 and "index:" in out, out)
check("--brief: names EVERY spelling live for that object across the corpus",
      "build" in out and "render" in out, out)
check("--brief: and flags an object spelled more than one way",
      "SPELLED MORE THAN ONE WAY" in out, out)
check("--brief: says it decides nothing", "decides nothing" in out, out)

# S3 — a dark extension REFUSES rather than printing an empty section, which would read as
# "nothing is established, invent freely" and is byte-identical to "this language is not extracted".
_DARK = BASE_CONF.replace('LANGS="py:python-ast:parser conf::dark"',
                          'LANGS="py:python-ast:parser conf::dark sh::dark"')
code, out = run_case({**_U10, "scripts/go.sh": "build_it() {\n  :\n}\n"}, _DARK,
                     args=("--brief", "scripts/go.sh"))
check("--brief: a dark extension is a NAMED refusal, not an empty section",
      code == 2 and "COVERAGE: dark" in out, out)
check("--brief: ...and it says why an empty section would be worse", "invent freely" in out, out)

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

    # --probe is legal against a repo with NO declaration and exits 0 either way.
    (_r / ".lexicon.conf").unlink()
    _got = subprocess.run([sys.executable, "tools/lexicon/lexicon.py", "--probe"],
                          cwd=_r, capture_output=True, text=True)
    check("--probe: legal with NO declaration, and exits 0",
          _got.returncode == 0 and "NO .lexicon.conf" in _got.stdout, _got.stdout[-300:])
    check("--probe: says it decides nothing",
          "corpus only decides which appear" in _got.stdout, _got.stdout[:300])

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
    _pin_lines = [l for l in _conf.split(chr(10)) if l.startswith(("VERB_OFFENDER_PIN",
                                                                  "SUFFIX_OFFENDER_PIN",
                                                                  "LAYER_OFFENDER_PIN"))]
    check("S8: all three pins are emitted, each on a line carrying no trailing comment",
          len(_pin_lines) == 3 and not any("#" in l for l in _pin_lines), str(_pin_lines))

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
_AGREE = {"core/a.py": "def build_index():" + chr(10) + "    pass" + chr(10), **LAYER_SIDES}
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

# M3 — an unparseable target is a NAMED refusal with its own exit code, never a traceback. `--brief`
# called the extractor with no guard while the corpus loop beside it caught and skipped, so the one
# mode pointed at a single file was the one mode that died on a file mid-edit.
_c, _o = run_case({"core/broken.py": "def build_x(:" + chr(10)}, BASE_CONF,
                  args=("--brief", "core/broken.py"))
check("--brief on an unreadable file refuses by name and exits 2 (not 1, not a traceback)",
      _c == 2 and "core/broken.py" in _o and "cannot be read as source" in _o,
      f"exit={_c} {_o[:200]}")
# ...and the guard catches the SAME exception pair the corpus loop 30 lines below it does. Round 1
# caught `(SyntaxError, ValueError)` against the loop's `(SyntaxError, OSError)`: it missed the
# unreadable-file case and swallowed any internal `ValueError` as "this file does not parse".
# Two readers of one question, differing. Asserted on the SOURCE, since no fixture reaches both.
_src = (KIT / "lexicon.py").read_text(encoding="utf-8")
check("...and it catches the same exception pair the corpus loop does",
      _src.count("except (SyntaxError, OSError)") >= 3,
      f"{_src.count(chr(101)+chr(120)+chr(99)+chr(101)+chr(112)+chr(116))} except clauses total")
check("...and exit 1 stays reserved for VERDICTS, so a refusal cannot read as a finding",
      "Traceback" not in _o, _o[:200])

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

# ---- TOOL-dPromptedSeam-3 — read_object_state, and the false rows it exists to stop -------------
#
# FOUR STATE ARMS, and they are FOUR because two rules decide the verdict and either alone passes
# half of them. `pin_of` dies by MEMBERSHIP; `boundedK` dies by LENGTH, and `k` is in no stopword
# list. A predicate carrying only the membership half answers `pin_of` correctly and `boundedK`
# wrong, which is the defect the spec's two-rule statement exists to make observable.
check("read_object_state: an all-stopword object is dead (membership)",
      lex.read_object_state("pin_of") == "dead", lex.read_object_state("pin_of"))
# SYNTHETIC, and saying so is the point. The only identifier in this repo that exercises the length
# rule is `boundedK` in tools/hooks/agent-cap.js, which is JavaScript and outside the Python corpus
# every other arm here walks. An arm over a population of zero would be a fixture that passes by
# finding nothing, so this one names its own syntheticity instead of implying coverage.
check("read_object_state: a one-character object is dead (length, SYNTHETIC — no python instance)",
      lex.read_object_state("boundedK") == "dead", lex.read_object_state("boundedK"))
check("read_object_state: a real object is live (the control that stops 'everything is dead')",
      lex.read_object_state("build_index") == "live", lex.read_object_state("build_index"))
check("read_object_state: a single-token name has NO object, which is not the same as dead",
      lex.read_object_state("main") == "none", lex.read_object_state("main"))
# ...and the three states must be THREE. A two-valued helper that maps `none` onto `dead` passes
# every arm above except this one, and that collapse is exactly what `run_brief`'s truthiness filter
# used to do.
check("...and the three states are distinct, so no two collapse",
      len({lex.read_object_state(n) for n in ("pin_of", "build_index", "main")}) == 3,
      str([lex.read_object_state(n) for n in ("pin_of", "build_index", "main")]))

# THE SET EQUALS map_lib's, and nothing but this arm says so. The layer ban forbids importing
# map_lib, so a parity gate cannot exist; the spec's Q1 records that and this asserts the count and
# two members rather than pretending the equality is watched.
check("the restated stopword set is 21 words, as map_lib declares",
      len(lex.DEAD_TOKENS) == 21, str(len(lex.DEAD_TOKENS)))
check("...and holds the members the corpus actually trips on",
      {"of", "at", "in", "for", "with"} <= lex.DEAD_TOKENS, str(sorted(lex.DEAD_TOKENS)[:8]))

# THE MARKER, both directions in one fixture. A dead shared object prints its row and must NOT claim
# a shared concept; a live shared object must. One arm cannot pass while the other fails on a build
# that suppresses the marker everywhere, which is the cheap wrong fix.
_BRIEF_SRC = """def build_index():
    pass


def render_index():
    pass


def pin_of():
    pass


def cache_of():
    pass


def main():
    pass
"""
_BRIEF = {"core/a.py": _BRIEF_SRC, **LAYER_SIDES}
_c, _o = run_case(_BRIEF, BASE_CONF, args=("--brief", "core/a.py"))
check("--brief keeps the marker on a LIVE shared object",
      "index:" in _o and "SPELLED MORE THAN ONE WAY" in _o.split("index:")[1].split(chr(10))[0], _o)
check("--brief WITHHOLDS the marker on a dead shared object, and still prints the row",
      "of:" in _o and "SPELLED MORE THAN ONE WAY" not in _o.split("of:")[1].split(chr(10))[0]
      and "DEAD tail" in _o.split("of:")[1].split(chr(10))[0], _o)
check("--brief reports the definitions with no object at all, rather than dropping them",
      "no object at all" in _o, _o)

if FAILURES:
    print(f"lexicon selftest FAILED — {len(FAILURES)} of {PASSES + len(FAILURES)} arm(s):")
    for f in FAILURES:
        print(f"  - {f}")
    raise SystemExit(1)
print(f"lexicon selftest OK — {PASSES} arm(s)")
