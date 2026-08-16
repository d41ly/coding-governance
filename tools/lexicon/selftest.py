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

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

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
  add     append to an existing collection

LAYERS:
  core/* -> adapters/*
"""


def check(label: str, cond: bool, detail: str = "") -> None:
    global PASSES
    if cond:
        PASSES += 1
    else:
        FAILURES.append(f"{label}{(' — ' + detail) if detail else ''}")


def run_case(files: dict, conf: str | None, waivers: dict | None = None):
    """Build a throwaway repo, run the engine in it, return (exit_code, output)."""
    with tempfile.TemporaryDirectory() as td:
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
        r = subprocess.run([sys.executable, "tools/lexicon/lexicon.py"], cwd=root,
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
check("P1 red: an undeclared leading token reds", code != 0, out)
check("P1 red names the file", "core/a.py" in out, out)
check("P1 red names the identifier", "frobnicate_index" in out, out)
check("P1 red names the offending token", "'frobnicate'" in out, out)

# ---- P2: the banned-suffix predicate ------------------------------------------------------------
code, out = run_case({"core/a.py": "def build_x():\n    pass\n\n\nclass ThingManager:\n    pass\n"}, BASE_CONF)
check("P2 red: a type DEFINITION ending in a banned suffix reds", code != 0 and "ThingManager" in out, out)

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
check("P3 unreachable: a rule whose TO glob matches no tracked file reds", code != 0, out)
check("P3 unreachable: it says UNMATCHABLE", "UNMATCHABLE" in out, out)

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

# ---- the --scaffold path, end to end -------------------------------------------------------------
# Nothing exercised this before, which is how a scaffolder that could emit a row its OWN reader
# refuses went unnoticed: `leading_verb` can return a digit run (`2fa_check` -> `2`) and the conf
# reader requires an alphabetic verb. A kit whose first command writes a file its second command
# rejects has no working adoption path at all.
with tempfile.TemporaryDirectory() as td:
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

# ---- verdict ------------------------------------------------------------------------------------
if FAILURES:
    print(f"lexicon selftest FAILED — {len(FAILURES)} of {PASSES + len(FAILURES)} arm(s):")
    for f in FAILURES:
        print(f"  - {f}")
    raise SystemExit(1)
print(f"lexicon selftest OK — {PASSES} arm(s)")
