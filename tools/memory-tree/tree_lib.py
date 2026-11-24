#!/usr/bin/env python3
"""tree_lib.py — the helpers two or more memory-tree engines share, and nothing else.

TOOL-aRepatriatedFork-9. `check-arms.py`, `row_grammar.py` and `gotchas.py` used to import these from
`corpus_ids.py` and `gen_build_index.py`, which made those two files a hard prerequisite of every
engine beside them. At an adopter whose copies of those two are its own programs — adopter ic, measured —
both gov engines died on import with an `ImportError`, so a fork of one file forced a fork of three.
The helpers live here now, and the two modules that defined them re-import them, so every caller
that reaches them through the old name keeps working.

WHAT BELONGS HERE: a name at least two engines in this directory read. A name one engine owns stays
in that engine; this is a seam, not a utility drawer. A shared name's helpers live beside it, because
this module imports no engine: `read_bindings` brought the record-kind, id-token and text readers it
calls (TOOL-dTrueNorth-29 S2). `row_grammar.py --selftest` carries the arm that refuses a sibling
engine importing from `corpus_ids` or `gen_build_index` again.

The module name follows the codebase-map kit's `map_lib.py` and the runlog kit's `runlog_lib.py`.
"""
from __future__ import annotations

import fnmatch
import itertools
import json
import os
import pathlib
import re
import sqlite3
import subprocess
import sys

# The lifecycle vocabulary, one declaration for the index generator's front-matter check, check 24's
# rotation grading and the backlog-row census.
STATUS_TOKENS = ("OPEN", "SPECCED", "INPROGRESS", "BLOCKED", "DEFERRED", "CLOSED", "WONTDO")
# What the INDEX generator and check 24 call terminal: a `DEFERRED` build or row stays in the live
# index, because parked work is still work somebody owes.
TERMINAL = ("CLOSED", "WONTDO")
# What the backlog-row CENSUS calls terminal, and it is DELIBERATELY WIDER (the unit's section 8 F1,
# owner-resolved). `memory/TEMPLATE-SPEC.md` names CLOSED / DEFERRED / WONTDO as the terminal set a
# spec header flips to, and a report-only census counting a deferred row as outstanding work would
# overstate the debt. The index answers "what must stay visible", the census "what is still owed";
# two questions, two tuples, and both are declared HERE so the difference is one decision in one place
# rather than two modules that happen to disagree.
CENSUS_TERMINAL = ("CLOSED", "WONTDO", "DEFERRED")

# A gotcha record's front-matter block: `---` at line 1, the column-0 `key: value` lines, `---`.
# Read by `gotchas.py` (checks 17-19, which grade the keys) and by `row_grammar.py`'s record
# enumeration (check 27, which ranks a record by its `description`). TOOL-aGraftedHelix-9 moved it
# here so the kit holds one copy: two engines spelling one block are free to disagree on where a
# record's front matter ends.
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)

# The red-fix lane's commit trailer, its one spelling (TOOL-aNimbleMend-8 S5): a fix commit carries
# `Red-fix: <leg name>`, one leg per trailer line, and `routed_commits.py` reads it through this name.
RED_FIX_TRAILER = "Red-fix"


# The one bash rule, carried inline once for the kit (TOOL-dWitnessedBar-57 S7): `row_grammar.py`'s
# `resolve_shell_ere` and `corpus_ids.py`'s `resolve_bash` import its `scan_bash` from here, and
# `resolve-python.test.sh` in the gov lib dir reds this copy once it drifts.
# >>> resolve_bash_py -- canonical copy: resolve_bash.py in the gov lib dir (byte-identical; gated)
BASH_NAMES = ("bash.exe", "bash")


def wrong_shell_at(path, wsl):
    """True when `path` is a Windows checkout under WSL: `wsl` set and `path` under a single-letter
    `/mnt/<drive>/`, WSL's mount of a Windows drive (TOOL-dWitnessedBar-27). The twin of the shell
    block `refuse_wrong_shell`'s `wrong_shell_at` in `refuse-wrong-shell.sh` in the gov lib dir; a
    WSL path on its own disk, and any path where no WSL marker is set, is green."""
    p = str(path)
    return bool(wsl) and len(p) > 6 and p.startswith("/mnt/") and "a" <= p[5] <= "z" and p[6] == "/"


def scan_bash(script="", host=""):
    r"""`(found, tried, refusal)`: the bash to run, found by RUNNING each candidate, never by its name.

    GOV_BASH first, and when it is set nothing after it is tried; then Git's own `bin/bash.exe`, the
    third parent of `git --exec-path`; then each PATH directory's BASH_NAMES, a System32 or
    WindowsApps launcher reported and never run. A candidate passes when one run prints `uname -s` as
    its first line and exits 0, `test -f` on `script` included when one is given; on a `windows` host
    the answer must start MINGW or MSYS, so WSL's launcher, which answers `Linux` and drops `$1`, is
    refused under any name (gotcha subprocess-resolves-a-different-shell). Past GOV_BASH every
    candidate is run, `tried` holding one `<candidate>: <why>` for each and a repeat never twice;
    `found` is the first that passed, or "" with `refusal` naming every `tried` line, and the bare name
    `bash` is never returned. `host` is `windows` or `posix`, this host's when empty. No memo: an
    adapter keeps its own, so this stays a function a truth table can call twice. On a `posix` host
    the hosting file is judged first: WSL running it from a Windows checkout under `/mnt/` returns
    no `found`, an empty `tried` and the wrong-shell refusal, before any candidate is tried."""
    host = host or ("windows" if os.name == "nt" else "posix")
    if host == "posix":
        here = os.path.abspath(__file__)
        wsl = bool(os.environ.get("WSL_DISTRO_NAME")) or os.path.exists("/proc/sys/fs/binfmt_misc/WSLInterop")
        if wrong_shell_at(here, wsl):
            return "", [], ("WSL is running " + here + " from a Windows checkout under /mnt/; "
                            "run it with Git's bash (C:/Program Files/Git/bin/bash.exe)")
    tried, seen = [], set()

    def run_probe(cand):
        try:
            r = subprocess.run([cand, "-c", 'uname -s && { [ -z "$1" ] || test -f "$1"; }', "_", str(script)],
                               stdin=subprocess.DEVNULL, capture_output=True, timeout=20)
        except (OSError, subprocess.SubprocessError):
            return "did not run"
        u = r.stdout.decode("utf-8", "replace").replace("\x00", "").split("\n")[0].strip()
        if not u:
            return "did not run"
        if host == "windows" and not u.startswith(("MINGW", "MSYS")):
            return "answered " + u
        return "runs" if r.returncode == 0 else "cannot see " + str(script)

    def check_candidate(cand):
        key = cand.lower() if host == "windows" else cand
        if key in seen:
            return False
        seen.add(key)
        low = cand.lower()
        why = "a launcher" if "/system32/" in low or "/windowsapps/" in low else run_probe(cand)
        tried.append(cand + ": " + why)
        return why == "runs"

    gov = os.environ.get("GOV_BASH", "")
    if gov:
        why = run_probe(gov)
        tried.append(gov + ": " + why)
        if why == "runs":
            return gov, tried, ""
        return "", tried, ("GOV_BASH is set to '" + gov + "' and " + why + ", so nothing after it is tried: "
                           "an override that is set and unusable is refused, never a fall-through")
    try:
        r = subprocess.run(["git", "--exec-path"], stdin=subprocess.DEVNULL, capture_output=True, timeout=20)
        ex = r.stdout.decode("utf-8", "replace").strip().replace("\\", "/") if r.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        ex = ""
    found = ""
    if not ex:
        tried.append("git --exec-path: did not run")
    else:
        cand = "/".join(ex.rstrip("/").split("/")[:-3]) + "/bin/bash.exe"
        if not os.path.isfile(cand):
            tried.append(cand + ": absent")
        elif check_candidate(cand):
            found = cand
    for d in os.environ.get("PATH", "").split(os.pathsep):
        for name in BASH_NAMES:
            cand = (d.rstrip("/\\") + "/" + name).replace("\\", "/")
            if d and os.path.isfile(cand) and check_candidate(cand):
                found = found or cand
    if found:
        return found, tried, ""
    return "", tried, ("no bash runs" + (" that can see " + str(script) if script else "") + ": "
                       + "; ".join(tried) + "; set GOV_BASH to Git's bash")
# <<< resolve_bash_py

def parse_leg_names(text: str) -> set:
    """The leg names a leg manifest's text declares: the `name` of each `{name: ...}` row of its
    top-level list. ValueError when the text is not JSON or its top level is not a list. The kit's
    one manifest parser (TOOL-aNimbleMend-8): `gotchas.py#load_leg_names` reads a working-tree
    manifest through it and the commit grader a blob at a commit."""
    import json

    rows = json.loads(text)
    if not isinstance(rows, list):
        raise ValueError("the top level is not a list of leg rows")
    return {r["name"] for r in rows if isinstance(r, dict) and isinstance(r.get("name"), str)}


def derive_docstring_ids(tree) -> set:
    """The `id()` of each docstring constant in a parsed module: the module's and that of every class,
    function and `async def` whose body opens with a string constant. A docstring is prose, so the
    walks that grade a module's string constants pass these over: `derive_constant_charges`
    and the loop kit's `derive_conf_reads` (TOOL-dDeclaredLoop-82 S8). The ids hold while `tree` lives."""
    import ast

    return {id(node.body[0].value) for node in ast.walk(tree)
            if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
            and node.body and isinstance(node.body[0], ast.Expr)
            and isinstance(node.body[0].value, ast.Constant) and isinstance(node.body[0].value.value, str)}


def derive_constant_charges(tree, module, is_needle) -> list:
    """The sorted pairs `(owner, rule)` the str constants of a parsed module whose value `is_needle`
    answers true for are charged to, one per owner a charge names, `rule` the number of the rule that
    charged it. A docstring `derive_docstring_ids` answers is prose and never counts; a comment is not
    in the tree. The one charge walk (TOOL-dDeclaredLoop-88 S13): `gen_build_index.py#scan_glob_readers`
    reads its owners and the loop kit's `derive_conf_constants` its rule-2 slice.

    THE CHARGE RULE (TOOL-dTrueNorth-32 S5, S9): each such constant is charged to exactly one name, the
    first of these that holds:
      1. the innermost enclosing function, its decorators and signature included, as
         `<module>.<qualified name>` joining every enclosing class and function name, so a class built
         inside a function is charged to that function, its one reader;
      2. else, outside every function, each `Name` in the targets of the innermost enclosing `Assign`,
         `AnnAssign` or `AugAssign`, qualified by the enclosing classes;
      3. else the innermost enclosing class, qualified, as a class-level `PATHS.append(...)` is;
      4. else the module, as `<module>`, as a module-level `SPECS.append(...)` is.
    The rule is total, so every shape the tree can hold has an owner."""
    import ast

    docs, found = derive_docstring_ids(tree), set()

    def scan_scope(node, qual, function, assign, klass):
        # `qual` is the module, then each enclosing class and function name; `function`, `assign` and
        # `klass` the charge rule's first three owners in force at `node`, None where none encloses it
        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.Constant) and isinstance(child.value, str) and id(child) not in docs \
                    and is_needle(child.value):
                found.update([(function, 1)] if function else [(a, 2) for a in assign] if assign
                             else [(klass, 3)] if klass else [(qual[0], 4)])
            elif isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                inner = [*qual, child.name]
                scan_scope(child, inner, ".".join(inner), None, klass)
            elif isinstance(child, ast.ClassDef):
                inner = [*qual, child.name]
                scan_scope(child, inner, function, None, ".".join(inner))
            elif function is None and isinstance(child, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
                targets = child.targets if isinstance(child, ast.Assign) else [child.target]
                names = [".".join([*qual, n.id]) for t in targets for n in ast.walk(t) if isinstance(n, ast.Name)]
                scan_scope(child, qual, None, names or assign, klass)
            else:
                scan_scope(child, qual, function, assign, klass)

    scan_scope(tree, [module], None, None, None)
    return sorted(found)


def read_policy_value(key, root):
    """`key` at `root`'s landed revision, through the policy kit's `policy.py get`, run as a process and
    found beside this kit by the inline resolver: memory-tree's `requires` is empty, so the policy kit may
    be absent, and that is a LookupError its caller degrades on (TOOL-dTotalRecall-43 S50); ValueError,
    the reader's last line in it, where the reader refuses. The kit's one policy read
    (TOOL-aNimbleMend-8 S7): each caller passes the key as a literal first argument."""
    import sys
    from backlog import resolve_kit_dir   # noqa: E402  the kit's inline copy of the sibling resolver
    kit = resolve_kit_dir("policy", "policy.py", pathlib.Path(__file__).resolve().parent)
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    p = subprocess.run([sys.executable, str(kit / "policy.py"), "get", key], cwd=str(root), env=env,
                       capture_output=True, text=True, encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL)
    said = p.stdout.split()
    if p.returncode != 0 or len(said) != 1:
        why = (p.stderr or p.stdout).strip().splitlines()
        raise ValueError(f"{key} did not read: {why[-1] if why else f'exit {p.returncode}'}")
    return said[0]


def kit_rel() -> str:
    """This kit's directory relative to the enclosing checkout, DERIVED and never spelled.

    Written into generated artifacts and into remedy strings an operator copies, so a hardcoded
    prefix lands a dead path in an adopter's tree. Falls back to the bare kit name when the module
    sits outside any checkout (a test fixture, an odd install); the result is a pointer, never a gate
    input.
    """
    here = pathlib.Path(__file__).resolve().parent
    for anc in [here] + list(here.parents):
        if (anc / ".git").exists():
            try:
                return here.relative_to(anc).as_posix()
            except ValueError:
                break
    return here.name


def parse_conf_line(line: str):
    """One `.memory-tree.conf` line -> `(key, value)`, or `None` for a line that declares nothing.

    TOOL-aScouredKit-19. SIX readers in this kit held this body and the shell gate SOURCES the same
    file in bash, so any spelling bash accepts and the python half mis-reads REMOVES coverage while
    the gate stays green. Reproduced: `MEMORY_ROOT=memory   # note` took `gotchas.py --check` from
    rc=1 to rc=0 over an identical planted violation, because the python half then walked a directory
    that does not exist. Coverage removed, not failed closed.

    TWO SPELLINGS BASH ACCEPTS THAT THE OLD BODY DID NOT, both measured against `set -a; . conf`:

        MEMORY_ROOT=memory   # note   ->  memory        (an unquoted inline comment is stripped)
        export FAMILIES="TOOL DEPL"   ->  TOOL DEPL     (the export prefix is not part of the key)

    AND ONE IT MUST NOT BREAK, which is why the comment strip is not unconditional:

        QUOTED="a # b"                ->  a # b         (a `#` inside quotes is DATA)

    Stripping `#` unconditionally would turn that into `a`, a silent wrong value where today's bug is
    at least a loud directory miss. So the strip runs BEFORE the quote peel and only on an unquoted
    `#` that begins a word, which is bash's own rule.

    NOT a general shell grammar, and deliberately: command substitution, parameter expansion, line
    continuations and quoted whitespace are all legal bash and none is in scope. These two are the
    spellings an adopter actually writes and the ones the kit's own example neither shows nor forbids.
    """
    line = line.strip()
    if not line or line.startswith("#") or "=" not in line:
        return None
    k, _, v = line.partition("=")
    k = k.strip()
    if k.startswith("export ") or k.startswith("export\t"):
        k = k[len("export"):].strip()
    if not k:
        return None
    # TOOL-aRepatriatedFork-38 rev-3 (the closing review's C4): the WORD rule, decided on the text
    # right after `=`. Whitespace there ends the assignment, so `K= x` and `K=   # note` are empty in
    # bash; a `#` begins a comment only AFTER whitespace, so `K=#x` keeps `#x`.
    if v[:1].isspace():
        return k, ""
    v = v.strip()
    # A QUOTED VALUE AND AN UNQUOTED ONE NEED DIFFERENT SCANS, and the first cut of this function
    # had only the second — so `KEY="v"  # note` kept both the comment AND a stray quote, which is
    # live on five lines of this kit's own shipped `.memory-tree.conf.example`. Found by the closing
    # diff review, reproduced against `set -a; . conf`.
    #
    # QUOTED: take the text between the opening quote and its MATCH, then treat only the remainder
    # as comment territory. That is what makes `Q="a # b"` keep its `#` while `Q="a"  # note` loses
    # its trailing one — the two directions this parser has to get right at once.
    if v[:1] in ("'", '"'):
        q = v[0]
        end = v.find(q, 1)
        if end >= 0:
            return k, v[1:end]
        # An UNTERMINATED quote is not something to guess at. Fall through to the unquoted scan,
        # which is what the old body did for every value, so this is no worse than before for a
        # spelling bash itself would reject.
    # UNQUOTED: a `#` that FOLLOWS whitespace starts a comment. Position 0 is not one: the
    # leading-whitespace case returned above, so a `#` there is the first character of the word.
    cut = -1
    for i, ch in enumerate(v):
        if ch == "#" and i > 0 and v[i - 1].isspace():
            cut = i
            break
    if cut >= 0:
        v = v[:cut].strip()
    return k, v.strip('"').strip("'")


def parse_conf(text: str, conf: dict) -> dict:
    """Merge every declaration in `text` into `conf`, which carries the caller's OWN defaults.

    The defaults stay per-reader on purpose: they differ (`CHARTER` and the pins for corpus_ids, the
    universal budget for gotchas, the arms floors for check-arms), and one merged dict would give
    every reader keys it has no use for and hide which reader depends on which.
    """
    for line in text.split("\n"):
        kv = parse_conf_line(line)
        if kv is not None:
            conf[kv[0]] = kv[1]
    return conf


def unfenced_lines(text: str):
    """Yield (lineno, line) for every line OUTSIDE a fenced block, then the open fence's line.

    The final yield is `(opened_at, None)` when the document ends inside a fence, and nothing when it
    does not. A caller that only wants the text ignores it; a caller that must REFUSE a document it
    could not fully read needs it, and no reader in either kit had it — the shell `_unfenced` and the
    index generator both ended silently with the fence still open, dropping every later line at
    exit 0. That is invisible by construction: a fence opened near the top of a row document hides
    every duplicate below it, and hiding duplicates is what the check that reads this exists to stop.
    """
    fence = ""
    opened_at = 0
    for n, line in enumerate(text.split("\n"), 1):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            mark = "```" if stripped.startswith("```") else "~~~"
            if not fence:
                fence, opened_at = mark, n
                continue
            # Only the marker that OPENED the fence closes it: a ``` line inside a ~~~ block is
            # content, not a toggle.
            if mark == fence:
                fence = ""
                continue
        if not fence:
            yield n, line
    if fence:
        yield opened_at, None


#: The declared-gap citation form (TOOL-aMendedFleet-26): this prefix written immediately before an
#: id says "this id has no record", so check 14 does not count it as an orphan and the roster
#: derivation does not file it on its slug's build. Spelled here and nowhere else.
MISSING_PREFIX = "missing:"


def scan_missing_citations(text: str, id_re) -> tuple[list, str]:
    """`(ids, blanked)`: every id written in the `missing:` form, and `text` with each form and its
    id overwritten by spaces of the same length, so offsets and line numbers still hold.

    `id_re` is the CALLER's own compiled id regex, so the form needs no second id grammar: each
    reader recognises a marked id by exactly the predicate it already uses for a cited one. A plain
    regex cannot tell the two apart on its own, because the colon is a word boundary.
    """
    pat = re.compile(re.escape(MISSING_PREFIX) + "(?:" + id_re.pattern + ")", id_re.flags)
    ids = [mm.group(0)[len(MISSING_PREFIX):] for mm in pat.finditer(text)]
    if not ids:
        return ids, text
    return ids, pat.sub(lambda mm: " " * len(mm.group(0)), text)


def build_spec_path_re(memory_root: str):
    """The path half of `parse_spec_h1`: a build's `spec/` folder, at any depth. Exposed so a caller
    walking a whole tree can skip reading a file the predicate would refuse on its path alone."""
    return re.compile(r"^" + re.escape(memory_root) + r"/builds/[^/]+/spec/")


def parse_spec_h1(rel: str, text: str, memory_root: str, families) -> tuple[int, str] | None:
    """`(lineno, id)` of the H1 that DEFINES a unit id in a spec file, or None.

    THE one predicate for "which id does this spec define" (TOOL-aRepatriatedFork-40). Two kits read
    it: `gen_build_index.spec_ids`, the index generator's resolution set, and the memory-recall
    kit's `extract_records`, which anchors a record on the same line. The recall kit reaches it
    through the sibling-kit resolver because it `requires` this kit; a copy of the regex there is
    the two-answers-to-one-question class.

    `rel` is repo-relative and must sit under `<memory_root>/builds/<slug>/spec/`, at any depth. The
    first UNFENCED H1 whose first token is `<FAMILY>-<slug>-<seq>` wins, one per file. `families`
    is the prefixes alone (`TOOL`, not `tooling:TOOL`).
    """
    if not build_spec_path_re(memory_root).match(rel):
        return None
    alt = "|".join(sorted(set(families))) or "(?!)"
    pat = re.compile(r"^#\s+[`*]*(?P<id>(?:" + alt + r")-(?:" + read_slug_class() + r")-\d+)\b")
    for n, line in unfenced_lines(text):
        if line is None:
            continue
        m = pat.match(line)
        if m:
            return n, m.group("id")
    return None


def build_git_env() -> dict:
    """The environment every pinned git call in this kit runs under — the kit's ONE pin policy.

    `GIT_GRAFT_FILE=/dev/null` is the spelling the unattended kit's history leg uses and it works
    under Git for Windows, whose MSYS layer maps the name. A graft file re-parents commits, so
    without this pin every ancestry answer could be honest about a sha and wrong about what that sha
    means. Callers add `--no-replace-objects` to the argv. Read by `transition_audit.py` and
    `routed_commits.py`; it moved here from the first when the second arrived (TOOL-aRoutedQuill-3).
    """
    env = dict(os.environ)
    env["GIT_GRAFT_FILE"] = "/dev/null"
    return env


#: What a git reader of this kit must not inherit, in TWO HALVES. ONE list for the kit: it moved here
#: from `gen_build_index.py`, which re-imports it, when the readers below became its second caller
#: (TOOL-dTrueNorth-20), and every runner that reads it strips both halves.
#:
#: The EIGHT location variables are the ones git EXPORTS to a hook, which then reach any subprocess
#: that hook starts: a reader started from a hook in a linked worktree inherits a `GIT_DIR` naming a
#: different tree than the one it was asked about, and reads it silently. TOOL-dRetiredFork-2,
#: absorbed from adopter nc `nc carve-out 16/20`, taken VERBATIM from gov's own hook-side scrub at
#: `.githooks/pre-push:100`, because these are two halves of ONE defect and a second list is where
#: they drift apart. That hook list is a subset of this one, unchanged.
#:
#: The FOUR pathspec-mode variables are taken VERBATIM from gov's own unset at
#: `<prefix>/check-playbook-parity.sh:334` (TOOL-aDistilledCharter-7 G6). Git exports none of them to a
#: hook, but a caller's own environment can carry one, and `GIT_LITERAL_PATHSPECS` turns every
#: `:(glob)` pathspec this kit reads into a literal name that matches nothing: the log answers empty,
#: exit 0, and a join over it reports green over a population it never read (TOOL-dTrueNorth-23).
GIT_ENV_LEAKS = (
    "GIT_DIR",
    "GIT_WORK_TREE",
    "GIT_INDEX_FILE",
    "GIT_OBJECT_DIRECTORY",
    "GIT_ALTERNATE_OBJECT_DIRECTORIES",
    "GIT_COMMON_DIR",
    "GIT_NAMESPACE",
    "GIT_PREFIX",
    "GIT_LITERAL_PATHSPECS",
    "GIT_GLOB_PATHSPECS",
    "GIT_NOGLOB_PATHSPECS",
    "GIT_ICASE_PATHSPECS",
)


def read_git_output(root, argv, stdin=None) -> bytes:
    """A git command's stdout as bytes, run at `root` under `build_git_env` less `GIT_ENV_LEAKS`, or
    `OSError` naming the command and git's first stderr line, or why it could not start. A caller
    reading through it never passes a failed call for an empty answer; each turns the error into its
    own named refusal.

    The four pathspec-mode variables are stripped with the location ones, because the caller's
    environment is not the reader's: under an ambient `GIT_LITERAL_PATHSPECS` a `:(glob)` pathspec
    matches nothing and git still exits 0, so the empty answer would be read as the true one, which
    no refusal above can catch (TOOL-dTrueNorth-23)."""
    cmd = ("git", *argv)
    shown = " ".join(cmd)
    env = {k: v for k, v in build_git_env().items() if k not in GIT_ENV_LEAKS}
    try:
        done = subprocess.run(cmd, cwd=root, input=stdin, capture_output=True, env=env)
    except OSError as exc:
        raise OSError(f"`{shown}` could not start: {exc}") from None
    if done.returncode:
        first = next((ln.strip() for ln in done.stderr.decode("utf-8", "replace").splitlines() if ln.strip()),
                     "git printed nothing on stderr")
        raise OSError(f"`{shown}` exited {done.returncode}: {first}")
    return done.stdout


def read_adding_commits(root, pathspec, wanted) -> dict:
    """`{path: sha}`, the commit that ADDED each path of `wanted`, the OLDEST where a path was added
    twice, from ONE `git log --reverse --no-renames --diff-filter=A` at HEAD over ONE glob `pathspec`.

    THE one adding-commit reader (TOOL-dTrueNorth-20 S32): the audit-writer test and the deviation
    join's pin anchors both call it, so the two cannot disagree on a record deleted and re-added. The
    argv is constant whatever `wanted` holds, never the paths themselves (TOOL-dTrueNorth-19 S1); every
    add outside `wanted` is ignored. A path with no add under the pathspec, staged and not committed
    say, is absent from the answer. A failed git call is `OSError` naming it; an empty `wanted` makes
    no call.
    """
    wanted = set(wanted)
    if not wanted:
        return {}
    log = read_git_output(root, ("log", "--no-renames", "--diff-filter=A", "--reverse", "--format=%x00%H",
                                  "--name-only", "--", pathspec))
    added: dict = {}
    for chunk in log.decode("utf-8", "replace").split("\x00")[1:]:
        sha, _, names = chunk.partition("\n")
        for name in names.split("\n"):
            name = name.rstrip("\r")
            if name in wanted:
                added.setdefault(name, sha.strip())      # oldest first, so the first add seen is kept
    return added


def read_blobs_at(root, requests) -> dict:
    """`{(rev, path): text, or None}` for every `(rev, path)` pair, in ONE `git cat-file --batch`.

    THE one `<rev>:<path>` bytes reader (TOOL-dTrueNorth-20 S33). THE STREAM IS BYTES: each body is
    sliced by its header's byte size before it is decoded, because a stream decoded first is shorter
    than its sizes after any multi-byte character and cuts the next blob short; then it is decoded as
    UTF-8 with CRLF folded, as a working-tree read is. None for an object the rev does not hold
    (`missing`, `ambiguous`), for one that is not a blob, its body skipped so the next header is read
    where it starts, and for one that is not UTF-8. A failed call, a stream ending before a request's
    header, or a header of no known shape is `OSError` naming it, never a partial answer.
    """
    requests = list(dict.fromkeys((str(rev), str(path)) for rev, path in requests))
    if not requests:
        return {}
    data = read_git_output(root, ("cat-file", "--batch"),
                            "".join(f"{rev}:{path}\n" for rev, path in requests).encode("utf-8"))
    out: dict = {}
    at = 0
    for rev, path in requests:
        end = data.find(b"\n", at)
        if end < 0:
            raise OSError(f"`git cat-file --batch` ended before {rev}:{path}, so its blob cannot be read")
        head, at = data[at:end], end + 1
        if head.endswith((b" missing", b" ambiguous")):
            out[(rev, path)] = None
            continue
        fields = head.rsplit(b" ", 2)
        if len(fields) != 3 or not fields[2].isdigit():
            raise OSError(f"`git cat-file --batch` answered `{head.decode('utf-8', 'replace')}` for {rev}:{path}, "
                          "so its blob cannot be read")
        size = int(fields[2])
        body, at = data[at:at + size], at + size + 1
        if fields[1] != b"blob":
            out[(rev, path)] = None
            continue
        try:
            out[(rev, path)] = body.decode("utf-8").replace("\r\n", "\n")
        except UnicodeDecodeError:
            out[(rev, path)] = None
    return out


# ------------------------------------------------------------------------------ record -> spec bindings
# TOOL-dTrueNorth-29 S2 -- the record-binding reader and the spec status-header grammar, read by the
# index generator and the deviation join, moved here verbatim from `gen_build_index.py`, which
# re-imports every name below so a caller reaching one through it keeps working.
RECORD_KINDS = ("spec", "build", "reviews", "prompts")

HDR_RE = re.compile(
    r"^\*\*Status:\*\* (?P<token>" + "|".join(STATUS_TOKENS) + r")"
    r" · rev-(?P<rev>\d+) · (?P<date>\d{4}-\d{2}-\d{2}) · node (?P<node>[a-z])"
    r" · Tier-(?P<tier>[12]) · base (?P<base>[0-9a-f]{8,})"
)


def read_text(path: str) -> str:
    # Bytes in, decode, normalise CR. Windows checkouts hand back CRLF and every comparison below
    # would then differ on every line — the exact green-by-accident shape a byte gate must not have.
    with open(path, "rb") as fh:
        return fh.read().decode("utf-8").replace("\r\n", "\n")


def unfenced(text: str):
    """The text-only view, kept as the one fence machine's façade rather than a second copy."""
    for _n, line in unfenced_lines(text):
        if line is not None:
            yield line


# Every record under a build's non-spec folders names the spec(s) it is
# evidence about, in its own head. This parser READS that and CLASSIFIES; it never raises, because
# `collect()` is reached by both --check and --write through one call site, so a raising parser would
# let one unannotated record refuse to render every artifact.
BIND_HEAD_LINES = 12
# `deviation` (TOOL-dTrueNorth-4 S2): a departure from the design or from a spec, its grammar the
# deviation join's (`deviation_join.read_record`). Its kind and its file name are joined both ways in
# `read_bindings`, so an untyped departure cannot pass for research and a typed one cannot hide from
# the join's glob.
# PLAY-dOrderedCharter-42 S1: the TYPED kinds, each a record the factory (`build_records.py`) names
# `<date>-build-<unit id>-<kind>-<n>.md` in a build's `build/` folder, joined to that name the same
# way. The factory's kind table is refused at import when its keys differ from this tuple: the
# reader owns the one list, and the factory reads it, because the reader importing the factory
# would cycle through `deviation_join.py`. `acceptance` (TOOL-dDeclaredLoop-17 S1) is a unit's acceptance
# commands re-run at a commit, written by a stand-in or an executor and never by a door. `transition`
# (TOOL-dDeclaredLoop-3 S2) is a build's stage move, written by the loop kit's transition writer alone.
# `recommendation` (TOOL-dDeclaredLoop-22 S1) is a stage exit's review recommendation, a command's score or a
# role's reason, written through the factory's door by the unattended driver's `--recommend`. `widen`
# (TOOL-dWitnessedBar-14 S5) is a population's growth admitted with its reason, written through
# `write_record` by the ratchet pack's `ratchet.py widen` alone. `leg-tail` (TOOL-dWitnessedBar-25 S6) is a
# failing leg's output tail kept by its hash, written through `write_record` by the run-gates kit's
# `keep_tails.py` alone. `flake` (TOOL-dWitnessedBar-8 S3) is one `test.flakes` run's per-leg verdicts,
# written through `write_record` by the run-gates kit's `verdict_flow.py flakes` alone. `gate-health`
# (TOOL-dWitnessedBar-1 S4) is one gate-health measurement, the reliability bar derived from the flake records,
# written through `write_record` by the drift kit's `drift_report.py --gate-health --write` alone. `card`
# (TOOL-dPlacedRequest-2 S8) is a build's orientation card at one step, its snapshot, written by the
# kickoff engine through the factory's `write_record`, no door. `probe-trigger` and `probe`
# (TOOL-dPlacedRequest-7 S6) are a probe opened at an item boundary and the probe it opened, its head, its
# method, its run lines and its verdict, written by the loop kit's probe.py through `write_record`, no door.
# `stream-plan` (TOOL-dTotalRecall-25 S6) is a build's units grouped into ordered streams, one TOML fence and
# no field, graded by `record_kinds.check_stream_plan`, written by dIndexedDesign's planner, no door.
# `shape-run` (TOOL-dTotalRecall-11) is one review exit's `review-shape` line as typed fields, written by
# `gov_record.py new shape-run` from the review record and compared back to that line by `shape_run.py --check`.
TYPED_RECORD_KINDS = ("deviation", "exception", "override", "change", "red-fix", "disposition", "acceptance",
                      "transition", "recommendation", "widen", "leg-tail", "flake", "gate-health", "card",
                      "probe-trigger", "probe", "stream-plan", "shape-run")
RECORD_KIND_TOKENS = ("spec-audit", "diff-review", "log", "research") + TYPED_RECORD_KINDS
# TOOL-dTotalRecall-18 S7: `journal` was the evidence kind's name until the kind became `log`. The old
# token is a READ-ONLY alias: a record written under it is bound as written, so no records region
# re-renders, and every comparison by value reads it through `resolve_kind`. No writer emits it.
KIND_ALIASES = {"journal": "log"}  # census: kept alias-compare the alias table itself


def resolve_kind(token):
    """The kind `token` names: an alias's target, any other token unchanged."""
    return KIND_ALIASES.get(token, token)
# Optional leading whitespace and an optional comment marker: the corpus holds a non-markdown record
# (a shell script), where the line can only be a comment. An extension-scoped rule would structurally
# exclude the one file most easily forgotten. TOOL-dTotalRecall-51 S1: the marker is the named group `prefix`,
# spelled once here, so the header edge lines' prefix and the Serves line's cannot drift.
BIND_PREFIX = r"^[ \t]*(?P<prefix>#+|//|;)?[ \t]*"
BIND_RE = re.compile(BIND_PREFIX + r"\*\*(?P<key>Serves|Commissions):\*\*[ \t]+(?P<rest>.*\S)[ \t]*$")
UNBOUND_RE = re.compile(r"^none\b[\s—–:-]*(?P<reason>\S.*)$")
EVIDENCES_RE = re.compile(r"^\*\*Evidences:\*\* `?([^`\s]+)`?")
# TOOL-dTotalRecall-19 S5: a record's key is its file stem, a dated stem whose kind word is `build`, `review` or
# `prompt`; the `record-key` native class of the playbook kit's namespace registry matches its targets with it.
RECORD_KEY_RE = re.compile(r"\d{4}-\d{2}-\d{2}-(?:build|review|prompt)-[A-Za-z0-9_-]+")
# TOOL-dTotalRecall-19 S1, TOOL-dTotalRecall-51 S1: an untyped record's header edge lines in its head, behind
# the prefix its Serves line wears
HEAD_EDGE_RE = re.compile(BIND_PREFIX + r"\*\*(?P<key>Made-by|Caused-by):\*\*[ \t]+(?P<rest>.*\S)[ \t]*$")
# TOOL-dTotalRecall-55 S1 S3: a census keeps a hit in a file no pass may edit by one path-keyed row held
# outside the file's bytes, `<census>\t<path>\t<reason>`: the census named by its function, one tracked file,
# and the reason printed beside the hit. The rows are the project's, in this registry under its memory root, and
# this kit ships none (TOOL-dTotalRecall-65 S1 S3). A file a pass may edit keeps its hit by the census marker on
# its line instead (`id_grammar.read_kept_reason`, TOOL-dTotalRecall-53 S34).
CENSUS_KEPT_REGISTRY = "census-kept-paths.txt"
#: TOOL-dTotalRecall-57 S1: the files a row may keep, the build folders' files no pass of a build may edit;
#: every other file keeps its hit by the census marker on its line
KEPT_PATH_DOMAIN = "memory/builds/*/build/*"


def read_kept_rows(census, root) -> dict:
    """`{path: reason}`: the rows of `root`'s CENSUS_KEPT_REGISTRY naming `census`, `{}` where the file is absent;
    its one reader (TOOL-dTotalRecall-55 S1, TOOL-dTotalRecall-65 S2). `#` comments and blank lines are skipped.
    ValueError naming the registry where any row of it, whatever census asked, holds fewer than three TAB fields,
    the line named, or names a path outside `KEPT_PATH_DOMAIN` (TOOL-dTotalRecall-57 S1). It does not check that
    a row's file exists, is tracked or is pinned, that a pair is unique, nor that a row is filed under the right
    census."""
    from design_lib import read_design_conf   # noqa: E402  the conf's one reader; at call time, no cycle
    memory = (read_design_conf(root).get("MEMORY_ROOT") or "memory").strip().strip("/") or "memory"
    registry = pathlib.Path(root, memory, "project", CENSUS_KEPT_REGISTRY)
    if not registry.is_file():
        return {}
    kept = {}
    for n, raw in enumerate(read_text(str(registry)).split("\n"), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        fields = line.split("\t", 2)
        if len(fields) < 3:
            raise ValueError(f"{CENSUS_KEPT_REGISTRY} line {n}: {line!r} holds {len(fields)} TAB field(s), and a row "
                             "is a census, a path and a reason")
        row_census, path, reason = fields
        if not fnmatch.fnmatchcase(path, KEPT_PATH_DOMAIN):
            raise ValueError(f"{CENSUS_KEPT_REGISTRY} row {path}: is no file under {KEPT_PATH_DOMAIN}, and an editable "
                             "file is kept by its census marker: mark the kept line `# census: kept <census> <reason>`")
        if row_census == census:
            kept[path] = reason
    return kept


def read_kept_path(census, path, root):
    """The reason `root`'s registry keeps `path` by for `census`, or None (TOOL-dTotalRecall-55 S1)."""
    return read_kept_rows(census, root).get(path)


def read_header_edges(text: str, path: str, binding=None) -> list:
    """A record header's edges, `{path, line, type, targets, site}` each, `site` `header`: the `**Serves:**`
    line as `serves`, its ids `binding`'s (the record's `read_bindings` row, None for a text it did not read,
    its kind carried as `kind`), and one `made-by` and one `caused-by` edge where the record names them,
    backticks cut (TOOL-dTotalRecall-19 S1). An untyped record names them as the lines
    `**Made-by:** <target>` and `**Caused-by:** <target>` in its first `BIND_HEAD_LINES` unfenced lines, read
    by `HEAD_EDGE_RE` behind the comment prefix its first Serves line wears, bare where that line is bare or
    absent (TOOL-dTotalRecall-51 S1); a record whose name a typed kind's grammar matches
    (`build_records.derive_record_name`) as its `- **Made-by:**` and `- **Caused-by:**` fields wherever they
    sit, read with `build_records.FIELD`. ValueError naming both lines where one key is given twice, or
    where an edge line's prefix differs from its Serves line's, whitespace ignored (TOOL-dTotalRecall-51 S2)."""
    import build_records   # noqa: E402  the factory's name grammar and field grammar; at call time, no cycle
    lines = text.replace("\r\n", "\n").split("\n")
    typed = any(build_records.derive_record_name(k).search(path) for k in TYPED_RECORD_KINDS)
    edges, seen, serves = [], {}, None
    head = [(n, ln) for n, ln in unfenced_lines("\n".join(lines))][:BIND_HEAD_LINES]
    for n, line in head:
        if line is None:
            break
        mb = BIND_RE.match(line)
        if mb and mb.group("key") == "Serves" and serves is None:
            serves = (n, line, mb.group("prefix") or "")
        if binding and binding.get("ids") and mb and mb.group("key") == "Serves":
            edges.append({"path": path, "line": n, "type": "serves", "targets": list(binding["ids"]),
                          "site": "header", "kind": binding.get("kind")})
            binding = None
    found = []
    if typed:
        for n, line in enumerate(lines, 1):
            m = build_records.FIELD.match(line)
            if m and m.group(1) in ("Made-by", "Caused-by"):
                found.append((n, m.group(1), m.group(2).strip()))
    else:
        for n, line in head:
            if line is None:
                break
            m = HEAD_EDGE_RE.match(line)
            if not m:
                continue
            if (m.group("prefix") or "") != (serves[2] if serves else ""):
                said = f"its Serves line {serves[0]} `{serves[1].strip()}`" if serves else "no Serves line, so the bare form"
                raise ValueError(f"{path}: {m.group('key')} line {n} `{line.strip()}` wears a prefix other than {said}")
            found.append((n, m.group("key"), m.group("rest")))
    for n, key, target in found:
        if key in seen:
            raise ValueError(f"{path}: {key} is given twice, at lines {seen[key]} and {n}")
        seen[key] = n
        edges.append({"path": path, "line": n, "type": key.lower(), "targets": [target.strip("`")], "site": "header"})
    return edges


def read_evidence_lines(text: str) -> list:
    """`(line number, unit, line)` for every line of `text` under an `**Evidences:** <unit>` block: a
    block opens at its `**Evidences:**` line and ends at the next one or at a line opening `#`, a
    heading. The walk `deviation_join.read_population`'s ledger arm did inline, extracted at its second
    Python instance, `seen_red.read_seen_red_records` (TOOL-dWitnessedBar-7 S2). It reads no binding:
    whether the text is a `log` record is each caller's test, through `read_bindings`."""
    out, unit = [], None
    for n, line in enumerate(text.split("\n"), 1):
        ev = EVIDENCES_RE.match(line)
        if ev or line.startswith("#"):
            unit = ev.group(1) if ev else None
            continue
        if unit:
            out.append((n, unit, line))
    return out


def _id_alternation(conf: dict) -> str:
    fams = [p.split(":", 1)[1] for p in conf.get("FAMILIES", "").split() if ":" in p]
    return "|".join(sorted(fams)) or "(?!)"


def record_paths(tracked: list, m: str) -> list:
    """Every tracked record: any depth, ANY extension, under a build's non-spec kind folders."""
    kinds = "|".join(k for k in RECORD_KINDS if k != "spec")
    sel = re.compile(r"^" + re.escape(m) + r"/builds/[^/]+/(?:" + kinds + r")/")
    return [p for p in tracked if sel.match(p)]


def read_slug_class(root=None) -> str:
    """The slug grammar's `slug_class` for `root`, None the default tree (TOOL-dTotalRecall-5 S13):
    the sibling `id_grammar`, imported at first call as `read_policy_value` imports `backlog`."""
    from id_grammar import derive_slug_grammar   # noqa: E402  the sibling, deliberately not at import
    return derive_slug_grammar(root).slug_class


def build_id_token_re(alt: str, root=None):
    """One id token with its optional `@rev-N` pin (TOOL-dTrueNorth-9 S3). The one spelling
    `_expand_ids` and `read_id_pins` both match through, so the reader of the ids and the reader of
    their pins cannot disagree on what an id is. Its slug is the slug grammar's class for `root`, None
    the default tree (TOOL-dTotalRecall-5 S13), never a looser literal."""
    return re.compile(r"^(?P<fam>" + alt + r")-(?P<slug>" + read_slug_class(root) + r")-(?P<seq>\d+)(?:@rev-(?P<rev>\d+))?$")


def _expand_ids(rest: str, alt: str, root=None) -> tuple:
    """Return (ids, bad_tokens). A contiguous run may be written N..M and EXPANDS here, at authoring
    time, to a fixed set — unlike a wildcard it cannot rot when the build later gains a unit.

    TWO VALUES, for all four callers (TOOL-dTrueNorth-9 S1): `backlog.read_header_verbs` and
    `read_idlist` unpack a pair, and a third value stranded both. A pin is `read_id_pins`' to read."""
    ids, bad = [], []
    one = build_id_token_re(alt, root)
    rng = re.compile(r"^(?P<fam>" + alt + r")-(?P<slug>" + read_slug_class(root) + r")-(?P<lo>\d+)\.\.(?P<hi>\d+)$")
    for tok in rest.split():
        mo = one.match(tok)
        if mo:
            ids.append(f"{mo.group('fam')}-{mo.group('slug')}-{mo.group('seq')}")
            continue
        mr = rng.match(tok)
        if mr and int(mr.group("lo")) <= int(mr.group("hi")):
            for n in range(int(mr.group("lo")), int(mr.group("hi")) + 1):
                ids.append(f"{mr.group('fam')}-{mr.group('slug')}-{n}")
            continue
        bad.append(tok)
    return ids, bad


def read_id_pins(rest: str, alt: str, root=None) -> dict:
    """`{id: N}`, the highest N each id carries as `@rev-N` on the line (TOOL-dTrueNorth-9 S2), the
    revision a spec-audit record read. A range token carries no pin, so its ids get none."""
    pins: dict = {}
    one = build_id_token_re(alt, root)
    for tok in rest.split():
        mo = one.match(tok)
        if mo and mo.group("rev") is not None:
            ident = f"{mo.group('fam')}-{mo.group('slug')}-{mo.group('seq')}"
            pins[ident] = max(pins.get(ident, 0), int(mo.group("rev")))
    return pins


def read_bindings(root: str, tracked: list, conf: dict, *, counts=None) -> dict:
    """path -> {state, kind, ids, pins, commissions, reason, bad}.

    Each record's head is its `unfenced-head` leg row where the index holds its unchanged blob, else
    its text parsed (TOOL-dTotalRecall-23 S4); `counts`, when passed, gains the call's `read_rows_at`
    counts.

    `ids` is the kind line's ids once each, in first-seen order (TOOL-dTrueNorth-20 S9). `pins` is the
    kind line's `{id: N}`, the highest `@rev-N` each id carries there, empty when none
    does (TOOL-dTrueNorth-5 S3), read by `read_id_pins` beside the `_expand_ids` call
    (TOOL-dTrueNorth-9 S2). A `**Commissions:**` line pins nothing.

    For each kind of `TYPED_RECORD_KINDS`: a file named `<date>-build-<unit id>-<kind>-<n>.md` in a
    build's `build/` folder must carry that kind, and a record of that kind must be so named there;
    either mismatch is `malformed` with its reason, naming the kind (TOOL-dTrueNorth-4 S2, generalised
    by PLAY-dOrderedCharter-42 S3). The name is read on that stem only, never on any name ending
    `-<kind>-<n>.md`, so a research record named `…-return-plan-2.md` stays bound.

    Does not raise for an UNREADABLE file — a decode or IO failure becomes a `state` row carrying
    `why`. It CAN still raise for a malformed conf. The former docstring said "Never raises."
    unqualified, which is what let the blanket catch at the caller look reasonable.

    state is one of: bound · unbound · malformed · absent.
    """
    m = conf["MEMORY_ROOT"]
    alt = _id_alternation(conf)
    typed_name = re.compile(r"^" + re.escape(m) + r"/builds/[^/]+/build/\d{4}-\d{2}-\d{2}-build-(?:" + alt
                            + r")-(?:" + read_slug_class(root) + r")-\d+-(?P<kind>" + "|".join(map(re.escape, TYPED_RECORD_KINDS))
                            + r")-\d+\.md$")
    out = {}
    rels = record_paths(tracked, m)
    heads, got = read_rows_at(root, rels, "unfenced-head")
    if counts is not None:
        add_leg_counts(counts, got)
    for rel in rels:
        rec = {"state": "absent", "kind": None, "ids": [], "pins": {}, "commissions": [], "reason": None,
               "bad": [], "why": "no Serves line in the first %d unfenced lines" % BIND_HEAD_LINES}
        head = heads[rel]
        if head.get("undecodable"):
            # NOT TEXT, so NOT A RECORD (TOOL-dScrubbedConduit-1 S1). A record is prose that carries a
            # `**Serves:**` line binding it to a spec; a file that does not decode cannot carry one,
            # and emitting it as an `A` row only moves the failure to hygiene check 21, which would
            # then demand a Serves line from a PNG. record_paths admits ANY extension by design — a
            # record's kind comes from its folder, not its suffix — so the exclusion belongs here,
            # where the bytes are actually read, rather than in a filename guess upstream.
            #
            # An adopter carrying a UI review screenshot under `reviews/` is the case this serves.
            continue
        if "unreadable" in head:
            # Present in the index and unreadable from disk is a REAL anomaly and stays a row.
            rec["why"] = f"unreadable: {head['unreadable']}"
            out[rel] = rec
            continue
        for line in head["head"]:
            mo = BIND_RE.match(line)
            if not mo:
                continue
            # A trailing HTML comment is a NOTE, not a token. The retrofit records the adjudication
            # rule that produced an inferred binding on the line itself, so a reviewer grades it in
            # the file rather than in a commit body no gate reads — and without this the note's
            # every word parsed as a malformed id.
            rest = mo.group("rest").split("<!--", 1)[0].strip()
            if not rest:
                continue
            if mo.group("key") == "Commissions":
                cids, bad = _expand_ids(rest, alt, root)
                rec["commissions"] = cids
                rec["bad"] += bad
                continue
            if rec["state"] != "absent":
                continue                      # first Serves line wins
            un = UNBOUND_RE.match(rest)
            if un:
                # The kind is OPTIONAL here and required below: an unbound record names no ids, so
                # there is no relation for a kind token to describe. The REASON is mandatory either
                # way — a bare `none` is malformed, because "no gate named" and "gate not yet
                # written" are indistinguishable from outside and only one of them is acceptable.
                rec["state"] = "unbound"
                rec["reason"] = un.group("reason")
                rec["why"] = ""
                continue
            toks = rest.split()
            if toks and (toks[0] in RECORD_KIND_TOKENS or toks[0] in KIND_ALIASES):
                served = " ".join(toks[1:])
                ids, bad = _expand_ids(served, alt, root)
                rec["kind"] = toks[0]
                # TOOL-dTrueNorth-20 S9, S36 — A REPEATED ID FOLDS HERE, in first-seen order, and never in
                # `_expand_ids`, whose base return its four callers keep: a record serving one id twice,
                # pinned at two revisions say, then renders it once in a records table and counts once in
                # the ids joins. Its pins are `read_id_pins`' below, the highest kept.
                rec["ids"] = list(dict.fromkeys(ids))
                rec["pins"] = read_id_pins(served, alt, root)
                rec["bad"] += bad
                if not ids:
                    rec["state"] = "malformed"
                    rec["why"] = "kind token with no resolvable id"
                else:
                    rec["state"] = "bound"
                    rec["why"] = ""
            else:
                rec["state"] = "malformed"
                got = toks[0] if toks else "(empty)"
                rec["why"] = (f"first token {got} is not one of "
                              + " ".join(RECORD_KIND_TOKENS) + " (" + ", ".join(
                                  f"{a} a read-only alias of {t}" for a, t in KIND_ALIASES.items())
                              + "), and the line is not the none form")
        # TOOL-dTrueNorth-4 S2, every typed kind by PLAY-dOrderedCharter-42 S3 — the kind joined to the
        # file name, both ways: a file on a typed kind's stem must say it is one, and a record saying so
        # must be on its stem. A record with no Serves line keeps its own reason.
        named = typed_name.match(rel)
        named_kind = named.group("kind") if named else None
        if named and rec["state"] in ("bound", "unbound") and rec["kind"] != named_kind:
            rec["state"] = "malformed"
            rec["why"] = (f"named as a {named_kind} record, -{named_kind}-<n>.md in a build/ folder, and its "
                          f"Serves kind is {rec['kind'] or 'the none form'}, not {named_kind}")
        elif rec["kind"] in TYPED_RECORD_KINDS and named_kind != rec["kind"]:
            rec["state"] = "malformed"
            rec["why"] = (f"Serves kind {rec['kind']}, and the file is not named "
                          f"<date>-build-<unit id>-{rec['kind']}-<n>.md in a build's build/ folder")
        out[rel] = rec
    return out


# ------------------------------------------------------------------------------ the memory legs' rows
# TOOL-dTotalRecall-23 — a memory leg's per-record parse is a pure READER of a blob's text and its
# params, and its product is stored as a row in the tag index, keyed by blob, so a leg reads rows for
# every unchanged blob the index holds and parses only the blobs that changed. The index's one writer,
# the playbook kit's `tag_index.build_index`, calls `build_leg_rows` in its transaction when a tree is
# first built (S1); a leg only reads, through `read_rows_at` (S3), so a cold or absent index costs the
# full parse it cost before, announced by `render_leg_line` (S6).
#
#: reader name -> (`<module>:<function>` reader, `<module>:<function>` params, None for an empty key),
#: the tag index's extractor spelling (S2). Each module is loaded from this kit's directory by a
#: COMPUTED path in `load_leg_module`, never imported here, so the tag index's closure, which takes this
#: file in, does not take the readers' modules in with it.
LEG_READERS = {
    "unfenced-head": ("tree_lib:extract_head_lines", None),
    "id-harvest": ("corpus_ids:extract_ids", "corpus_ids:derive_id_params"),
    "spec-head": ("design_lib:extract_spec_head", None),
}
LEG_TABLE = ("CREATE TABLE IF NOT EXISTS leg_row(blob TEXT, reader TEXT, version TEXT, payload TEXT, "
             "PRIMARY KEY (blob, reader, version))")
#: blobs per `SELECT ... IN (...)` in `read_leg_payloads` (S3)
LEG_QUERY_CHUNK = 999
#: blobs per `read_blobs_at` batch in `build_leg_rows`, so a cold build never holds every memory blob at once
LEG_READ_CHUNK = 500
_LEG_MODULES: dict = {}
_LEG_CLOSURES: dict = {}


def load_leg_module(mod_name):
    """The module `<mod_name>.py` of this kit's own directory: this one, one already loaded from that
    file under its own name or as `__main__`, else that file loaded by its computed path, once."""
    src = os.path.normcase(os.path.join(os.path.dirname(os.path.abspath(__file__)), mod_name + ".py"))
    for mod in (sys.modules.get(__name__), sys.modules.get(mod_name), sys.modules.get("__main__")):
        at = getattr(mod, "__file__", None)
        if at and os.path.normcase(os.path.abspath(at)) == src:
            return mod
    if src not in _LEG_MODULES:
        import importlib.util
        spec = importlib.util.spec_from_file_location("leg_reader_" + mod_name, src)
        if spec is None or not os.path.isfile(src):
            raise ImportError(f"leg reader module {mod_name}: no file {src}")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _LEG_MODULES[src] = mod
    return _LEG_MODULES[src]


def load_leg_reader(name, root) -> tuple:
    """`(reader, arg, version)` for the `LEG_READERS` row `name` at `root`: the version is
    `derive_leg_version`'s, `import_walk.derive_closure_version` over the module's closure keyed by the
    params' key, once per process per key."""
    spelled, params = LEG_READERS[name]
    mod_name, _, fn_name = spelled.partition(":")
    fn = getattr(load_leg_module(mod_name), fn_name)
    key, arg = "", None
    if params:
        p_mod, _, p_fn = params.partition(":")
        key, arg = getattr(load_leg_module(p_mod), p_fn)(root)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), mod_name + ".py")
    if (src, key) not in _LEG_CLOSURES:
        import import_walk  # noqa: E402  the one closure-version rule, the tag index's (TOOL-dTotalRecall-43 S21)
        _LEG_CLOSURES[(src, key)] = import_walk.derive_closure_version([src], [os.path.dirname(src)], key)
    return fn, arg, _LEG_CLOSURES[(src, key)]


def derive_leg_version(name, root) -> str:
    """The reader's version, DERIVED (S2): the first 12 hex of the SHA-256 over the bytes of every module
    of its module's closure under `import_walk.derive_module_closure`, in path order, then its params' key:
    `import_walk.derive_closure_version`, the one rule (TOOL-dTotalRecall-43 S21)."""
    return load_leg_reader(name, root)[2]


def extract_head_lines(text, arg=None) -> dict:
    """The `unfenced-head` reader: the first `BIND_HEAD_LINES` lines `unfenced` yields, which
    `read_bindings` classifies, or `{"undecodable": true}` for a blob that is not UTF-8."""
    if text is None:
        return {"undecodable": True}
    return {"head": list(itertools.islice(unfenced(text), BIND_HEAD_LINES))}


def load_tag_index():
    """The playbook kit's `tag_index`, reached at call time through this kit's inline `resolve_kit_dir`;
    LookupError where that kit does not resolve."""
    from backlog import resolve_kit_dir   # noqa: E402  the kit's inline copy of the sibling resolver
    kit = resolve_kit_dir("playbook", "tag_index.py", pathlib.Path(__file__).resolve().parent)
    if str(kit) not in sys.path:
        sys.path.append(str(kit))
    import tag_index  # noqa: E402
    return tag_index


def read_leg_payloads(root, reader, version, blobs):
    """`{blob: payload}` for each of `blobs` `leg_row` holds under `reader` at `version`, the index
    opened read-only, one `SELECT` per `LEG_QUERY_CHUNK` blobs; None for the index-absent case: an absent
    playbook kit, an absent file, a file without `leg_row`, or any `sqlite3.Error` (S3)."""
    try:
        db = load_tag_index().derive_index_path(root)
        if not db.is_file():
            return None
        con = sqlite3.connect(db.as_uri() + "?mode=ro", uri=True)
    except (LookupError, ImportError, OSError, ValueError, subprocess.CalledProcessError, sqlite3.Error):
        return None
    try:
        con.execute("SELECT 1 FROM leg_row LIMIT 0")
        out = {}
        for at in range(0, len(blobs), LEG_QUERY_CHUNK):
            part = blobs[at:at + LEG_QUERY_CHUNK]
            out.update(con.execute("SELECT blob, payload FROM leg_row WHERE reader = ? AND version = ? AND blob IN ("
                                   + ",".join("?" * len(part)) + ")", (reader, version, *part)).fetchall())
        return out
    except sqlite3.Error:
        return None
    finally:
        con.close()


def read_rows_at(root, paths, reader) -> tuple:
    """`({path: product}, {"index": n, "parsed": m, "absent": bool})` over working-tree `paths` (S3).

    One `git ls-files -s -z` names each path's blob and one `git diff --name-only --no-renames -z HEAD`
    the paths that differ from HEAD. A path absent from that diff whose blob `leg_row` holds at the
    reader's current version is answered from the row; every other path, edited, staged, untracked or
    absent from git's index, is read through `read_text` and parsed, a `UnicodeDecodeError` handing the
    reader None and an `OSError` standing as `{"unreadable": "<message>"}`. A git read that fails, an
    unborn HEAD say, parses every path."""
    fn, arg, version = load_leg_reader(reader, root)
    paths = list(dict.fromkeys(paths))
    blob_of: dict = {}
    try:
        for rec in read_git_output(root, ("ls-files", "-s", "-z")).decode("utf-8", "replace").split("\0"):
            meta, _, path = rec.partition("\t")
            fields = meta.split()
            if path and len(fields) == 3:
                blob_of[path] = fields[1]
        changed = {p for p in read_git_output(root, ("diff", "--name-only", "--no-renames", "-z", "HEAD"))
                   .decode("utf-8", "replace").split("\0") if p}
    except OSError:
        blob_of, changed = {}, set()
    held = {p: blob_of[p] for p in paths if p in blob_of and p not in changed}
    rows = read_leg_payloads(root, reader, version, sorted(set(held.values())))
    counts = {"index": 0, "parsed": 0, "absent": rows is None}
    rows = rows or {}
    out = {}
    for p in paths:
        payload = rows.get(held.get(p))
        if payload is not None:
            out[p] = json.loads(payload)
            counts["index"] += 1
            continue
        counts["parsed"] += 1
        try:
            text = read_text(os.path.join(root, p))
        except UnicodeDecodeError:
            text = None
        except OSError as exc:
            out[p] = {"unreadable": str(exc)}
            continue
        out[p] = fn(text, arg)
    return out, counts


def add_leg_counts(total: dict, got: dict) -> dict:
    """`total` gaining one `read_rows_at` call's counts: the two numbers summed, `absent` if any call's was."""
    total["index"] = total.get("index", 0) + got["index"]
    total["parsed"] = total.get("parsed", 0) + got["parsed"]
    total["absent"] = total.get("absent", False) or got["absent"]
    return total


def render_leg_line(reader, counts) -> str:
    """The announce line (S6): `leg rows: <reader> <n> from the index, <m> parsed`, or
    `leg rows: <reader> index absent, <m> parsed`."""
    if counts.get("absent"):
        return f"leg rows: {reader} index absent, {counts.get('parsed', 0)} parsed"
    return f"leg rows: {reader} {counts.get('index', 0)} from the index, {counts.get('parsed', 0)} parsed"


def build_leg_rows(con, root, tree, entries) -> None:
    """The one writer of `leg_row` (S1), inside `tag_index.build_index`'s `BEGIN IMMEDIATE` block after its
    sweep, over the tree's `(path, blob)` entries. For each blob under the conf's `MEMORY_ROOT` that
    `leg_row` lacks at a reader's current version, it reads the blob through `read_blobs_at` at `tree` and
    writes the reader's row; then it clears every row whose blob no `tree_path` or `dirty_path` row holds.
    A reader whose module, params or call raises writes no row for it and never fails the build."""
    con.execute(LEG_TABLE)
    try:
        conf = parse_conf(read_text(os.path.join(root, ".memory-tree.conf")), {})
    except (OSError, UnicodeDecodeError):
        conf = {}
    m = (conf.get("MEMORY_ROOT") or "memory").strip("/") + "/"
    blobs: dict = {}
    for path, blob in entries:
        if path.startswith(m):
            blobs.setdefault(blob, path)
    readers = []
    for name in LEG_READERS:
        try:
            fn, arg, version = load_leg_reader(name, root)
        except Exception:  # noqa: BLE001  a reader that does not load costs parses, never the tag build (S1)
            continue
        held = {b for (b,) in con.execute("SELECT blob FROM leg_row WHERE reader = ? AND version = ?",
                                          (name, version))}
        readers.append((name, fn, arg, version, held))
    todo = [(b, p) for b, p in blobs.items() if any(b not in r[4] for r in readers)]
    for at in range(0, len(todo), LEG_READ_CHUNK):
        part = todo[at:at + LEG_READ_CHUNK]
        try:
            texts = read_blobs_at(root, [(tree, p) for _b, p in part])
        except OSError:
            break
        rows = []
        for blob, path in part:
            for name, fn, arg, version, held in readers:
                if blob in held:
                    continue
                try:
                    product = fn(texts.get((str(tree), path)), arg)
                except Exception:  # noqa: BLE001  a reader's raise writes no row for it (S1)
                    continue
                rows.append((blob, name, version,
                             json.dumps(product, sort_keys=True, separators=(",", ":"), ensure_ascii=False)))
        con.executemany("INSERT OR REPLACE INTO leg_row VALUES (?,?,?,?)", rows)
    con.execute("DELETE FROM leg_row WHERE NOT EXISTS (SELECT 1 FROM tree_path t WHERE t.blob = leg_row.blob) "
                "AND NOT EXISTS (SELECT 1 FROM dirty_path d WHERE d.blob = leg_row.blob)")


#: the leg fixture's namespace registry, empty, and its planted records by role (S7)
LEG_FIXTURE_REGISTRY = "namespaces.toml"
LEG_FIXTURE = {
    "fenced": "memory/builds/tOne/build/2026-08-02-build-ARCH-tOne-1-fenced.md",
    "undecodable": "memory/builds/tOne/reviews/2026-08-02-review-shot.png",
    "crlf": "memory/builds/tOne/build/2026-08-02-build-ARCH-tOne-1-crlf.md",
    "spec": "memory/builds/tOne/spec/2026-08-01-spec-tOne-1.md",
    "cites": "memory/DECISIONS.md",
    "edited": "memory/builds/tOne/build/2026-08-02-build-ARCH-tOne-1-edited.md",
    "untracked": "memory/builds/tOne/build/2026-08-02-build-ARCH-tOne-1-untracked.md",
}


def write_leg_fixture(root) -> None:
    """A scratch git repository at `root` (S7): a conf, an empty namespace registry and a planted memory
    tree that `gen_build_index.py --check` accepts, rendered by this kit's own `--write` and committed.
    `LEG_FIXTURE` names its records: one carries its Serves line inside a fence, one is undecodable, one
    is CRLF, one is a spec, one cites an id and a dead path, one is edited and uncommitted, and one is
    untracked. A step that fails raises OSError naming it."""
    root = pathlib.Path(root)
    root.mkdir(parents=True, exist_ok=True)
    plant = {
        ".memory-tree.conf": 'MEMORY_ROOT=memory\nDISCIPLINES="arch"\nFAMILIES="arch:ARCH"\nCHARTER="AGENTS.md"\n',
        "AGENTS.md": "# charter\n\nRead `memory/README.md` first.\n",
        LEG_FIXTURE_REGISTRY: "# an empty namespace registry: the tag index runs extract_citations alone\n",
        "memory/README.md": "# memory\n",
        "memory/project/stale-header-waiver.txt": "# empty: the mechanism is inert until a header corrupts\n",
        "memory/builds/tOne/README.md": "---\nslug: tOne\nnode: a\nopened: 2026-08-01\nstreams: arch\nroster: ARCH\n"
                                        "ids: ARCH-tOne-1\n---\n\n# tOne\n\n<!-- gen:build-index -->\n"
                                        "<!-- /gen:build-index -->\n",
        LEG_FIXTURE["spec"]: "# ARCH-tOne-1 — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-08-01 · node a · "
                             "Tier-2 · base 0123abcd · order 1\n\n## 4. Design\n\n### Files touched (estimate)\n\n"
                             "- `src/leg.py`\n",
        LEG_FIXTURE["fenced"]: "# fenced\n\n```\n**Serves:** research ARCH-tOne-9\n```\n\n"  # census: kept cause-writer fixture: a record head its fixture plants
                               "**Serves:** research ARCH-tOne-1\n",  # census: kept cause-writer fixture: a record head its fixture plants
        LEG_FIXTURE["crlf"]: "# crlf\r\n\r\n**Serves:** research ARCH-tOne-1\r\n\r\nbody\r\n",  # census: kept cause-writer fixture: a record head its fixture plants
        LEG_FIXTURE["cites"]: "# d\n\n- ARCH-tOne-1 · a decision, its notes at `memory/nowhere/gone.md`\n",
        LEG_FIXTURE["edited"]: "# edited\n\n**Serves:** none — a scratch note\n\nfirst\n",  # census: kept cause-writer fixture: a record head its fixture plants
    }
    for rel, text in plant.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_bytes(text.encode("utf-8"))
    (root / LEG_FIXTURE["undecodable"]).parent.mkdir(parents=True, exist_ok=True)
    (root / LEG_FIXTURE["undecodable"]).write_bytes(b"\x89PNG\r\n\x1a\n\xff\xfe\x00 not text")
    who = ("-c", "user.name=t", "-c", "user.email=t@t.test", "-c", "core.autocrlf=false")
    read_git_output(str(root), ("init", "-q", "--template="))
    read_git_output(str(root), ("config", "core.autocrlf", "false"))
    read_git_output(str(root), ("add", "-A"))
    read_git_output(str(root), (*who, "commit", "-q", "--no-verify", "-m", "leg fixture"))
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    gbi = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gen_build_index.py")
    done = subprocess.run([sys.executable, gbi, "--write"], cwd=str(root), env=env, capture_output=True,
                          text=True, encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL)
    if done.returncode:
        raise OSError(f"the leg fixture's `gen_build_index.py --write` exited {done.returncode}: "
                      + (done.stdout + done.stderr).strip()[-400:])
    read_git_output(str(root), ("add", "-A"))
    read_git_output(str(root), (*who, "commit", "-q", "--no-verify", "-m", "leg fixture rendered"))
    with open(root / LEG_FIXTURE["edited"], "ab") as fh:
        fh.write(b"second\n")
    (root / LEG_FIXTURE["untracked"]).write_bytes(b"# untracked\n\n**Serves:** research ARCH-tOne-1\n")  # census: kept cause-writer fixture: a record head its fixture plants


def build_fixture_index(root) -> pathlib.Path:
    """Build the node index of a `write_leg_fixture` repository through the playbook kit's `load_view` over
    `derive_context(root, <its registry>)`, and return the index file's path."""
    ti = load_tag_index()
    ctx = ti.derive_context(root, pathlib.Path(root) / LEG_FIXTURE_REGISTRY)
    con = ti.load_index(root)
    try:
        ti.load_view(con, root, ctx)
    finally:
        con.close()
    return ti.derive_index_path(root)
