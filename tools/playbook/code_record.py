"""code_record — the core `code` record: what a tree's code defines, calls and registers (TOOL-dTotalRecall-8).

    python code_record.py --check [--ceiling <s>]       re-derive HEAD's record and compare it to the cached text
    python code_record.py --dump [--tree <rev>]         print the record of one tree, HEAD's by default
    python code_record.py --time [--tree <rev>]         derive cold, no cached row read: seconds, bytes, facts
    python code_record.py neighbourhood <path>...       the definitions, callers, callees and tests of those paths
    python code_record.py --fixture adopter             build the adopter-scale repository, then --time there
    python code_record.py --selftest                    every fixture arm

THE RECORD is one UTF-8 text per tree, LF-ended, paths sorted, TAB between cells. An ordinal is a line's
place, from 0, among the `f` and `d` lines, so an `f` line's ordinal is its module's own:

    code-record 1 <extractors> <languages>
    f <path>                                  a code file
    i <module>[:<name>,...] ...               its imports, for a shell file the files it sources
    d <depth>[C] <name> <line>-<end> <hash>   a definition, C a class, its depth under its file
    c <ordinal> ...                           calls out of the f or d line above
    m <name> ...                              mentions out of it
    x <ordinal> ...                           files it invokes
    r <leg or kit> <ordinal>                  a registry edge
    a <language> <ambiguous>/<sites>          that language's edges ship as mentions
    s <path> <reason>                         a skipped input

A definition's key is `<path>::<qualified name>`; a name defined twice in one file reads as its first. What a
reader derives from the tree's listing or from a blob is stored nowhere: a file outside the languages, a test,
a kit, a call's line, a body's text. `derive_code_record` answers all of it, as rows.

STORAGE is two tables in the one index file `tag_index.load_index` opens (§2 S7): `code_facts`, one blob's
facts as `zlib` bytes, and `code_tree`, the text. `version` hashes this file and `extract_code.py`, the value of
`memory.code-languages` and the ctags version, so a changed extractor re-reads every blob and an unchanged one
re-reads only the blobs it has no row for, a blob yielding nothing included. A write keeps the trees a
worktree's HEAD names and the blobs they hold.

BOUNDS: `linguist-vendored` and `linguist-generated` paths are left out, read from the tree's own
`.gitattributes`; binary and LFS blobs are skipped by attribute, a submodule is a boundary row, a code file over
CODE_FILE_CAP is skipped, and a derivation over CODE_RUN_CEILING seconds answers `degraded`, is never
written, and leaves its reader the `git grep` floor.

WHAT IT DOES NOT SEE: dynamic dispatch, `eval`, a `bash -c` body, a call built at run time. A shell site is a
word, so an argument spelling a function's name is a site too.

Exit 0 green, 1 a stale text or an empty tree, 2 a refusal or a degraded record.
"""
from __future__ import annotations

import argparse
import collections
import functools
import hashlib
import json
import os
import pathlib
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
import tomllib
import zlib

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
if str(KIT_DIR) not in sys.path:
    sys.path.insert(0, str(KIT_DIR))

import extract_code as xc  # noqa: E402
import tag_index as ti  # noqa: E402
from policy_value import PolicyRefused, read_policy_value  # noqa: E402

CODE_FILE_CAP = 4194304   # bytes; a larger code file leaves a `skipped` row
CODE_RUN_CEILING = 30.0   # seconds of one derivation, PINNED by deviation 84 of TOOL-dTotalRecall-8
KEY = "memory.code-languages"
BUILTIN = {"py": "python", "sh": "shell", "js": "javascript", "mjs": "javascript", "cjs": "javascript"}
AMBIGUOUS_SHARE = 0.10    # past it a language's edges all ship as mentions
ATTRS = ("linguist-vendored", "linguist-generated", "diff", "filter")
TABLES = """
CREATE TABLE IF NOT EXISTS code_facts(blob TEXT NOT NULL, lang TEXT NOT NULL, version TEXT NOT NULL,
                                      facts BLOB NOT NULL, PRIMARY KEY(blob, lang, version));
CREATE TABLE IF NOT EXISTS code_tree(tree TEXT NOT NULL, version TEXT NOT NULL, record TEXT NOT NULL,
                                     PRIMARY KEY(tree, version));
"""
#: the ctags kinds read as a definition; every other kind a reader answers (a variable, a heading) is left out
CTAGS_FUNCTIONS = frozenset(("function", "func", "method", "procedure", "subroutine", "constructor", "singletonMethod"))
CTAGS_CLASSES = frozenset(("class", "struct", "interface", "trait", "enum", "type", "union", "record", "module",
                           "protocol", "object"))

#: A word that names an interpreter through a variable or an attribute: `$PY`, `${BASH}`, `$sys.executable`.
INTERPRETER_VAR = re.compile(r"\$\{?[\w.]*?(?:py|python3?|bash|node|executable)(?:_?bin)?(?::?-.*)?\}?", re.I)
#: A JavaScript argv literal: an interpreter, then the path it runs, as two members or as `spawn(x, ['p'])`.
JS_ARGV = re.compile(r"""(?:(['"])(?:bash|sh|python3?|node)\1|process\.execPath)\s*,\s*\[?\s*(['"])([^'"\n]+)\2""")
CODE_SUFFIXES = tuple("." + ext for ext in BUILTIN)


# >>> invocation_segments -- canonical copy: invocation_segments.py in the gov lib dir (byte-identical; gated)
ENV_ASSIGN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*=.*", re.S)
HEREDOC_RE = re.compile(r"<<-?[ \t]*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1")
WRAPPERS = frozenset({"sudo", "command", "exec", "time", "nice", "env", "nohup"})
INTERPRETERS = frozenset({"bash", "sh", "zsh", "dash", "python", "python3", "py", "node", "pwsh",
                          "powershell"})
SEPARATORS = ("&&", "||", "|&", "|", ";", "&", "\n", "(", ")")
# The characters a separator can start with. The tokenizer tries the separator list only at these, so
# an ordinary character costs one set lookup rather than one `startswith` per separator. Profiled over
# the largest local session, trying the whole list at every character cost more than parsing the JSON.
SEPARATOR_HEADS = frozenset(sep[0] for sep in SEPARATORS)


def _derive_basename(word: str) -> str:
    return word.replace("\\", "/").rsplit("/", 1)[-1]


def _remove_heredocs(command: str) -> str:
    """Drop every heredoc body, delimiter line included. A body is text, never a command."""
    if "<<" not in command:
        return command
    out, pending = [], []
    for line in command.split("\n"):
        if pending:
            if line.strip() == pending[0]:
                pending.pop(0)
            continue
        out.append(line)
        for m in HEREDOC_RE.finditer(line):
            if m.start() > 0 and line[m.start() - 1] == "<":
                continue
            pending.append(m.group(2))
    return "\n".join(out)


def _read_separator(text: str, i: int) -> str | None:
    for sep in SEPARATORS:
        if text.startswith(sep, i):
            if sep == "&" and ((i > 0 and text[i - 1] in "<>") or text.startswith("&>", i)):
                return None
            return sep
    return None


def extract_segments(command: str) -> list:
    """A shell command as `(words, separator-after)` pairs, honouring quotes, escapes and heredocs.

    A mention inside quotes stays inside ONE word and a heredoc body is dropped whole, so a commit
    message that names a destructive command is not one. This is not a shell: `$(...)` inside quotes,
    `bash -c` and `eval` are not descended into, and a call nested in one is not seen.
    """
    text = _remove_heredocs(command)
    segs, words, cur = [], [], []
    in_word = False
    i, n = 0, len(text)
    while i < n:
        ch = text[i]
        if ch == "'":
            j = text.find("'", i + 1)
            j = n if j < 0 else j
            cur.append(text[i + 1:j])
            in_word, i = True, j + 1
            continue
        if ch == '"':
            j, buf = i + 1, []
            while j < n and text[j] != '"':
                if text[j] == "\\" and j + 1 < n and text[j + 1] in '"\\$`':
                    buf.append(text[j + 1])
                    j += 2
                    continue
                buf.append(text[j])
                j += 1
            cur.append("".join(buf))
            in_word, i = True, j + 1
            continue
        if ch == "\\" and i + 1 < n:
            if text[i + 1] != "\n":
                cur.append(text[i + 1])
                in_word = True
            i += 2
            continue
        if ch in " \t\r":
            if in_word:
                words.append("".join(cur))
                cur, in_word = [], False
            i += 1
            continue
        if ch == "#" and not in_word:
            j = text.find("\n", i)
            i = n if j < 0 else j
            continue
        sep = _read_separator(text, i) if ch in SEPARATOR_HEADS else None
        if sep:
            if in_word:
                words.append("".join(cur))
                cur, in_word = [], False
            segs.append((words, sep))
            words = []
            i += len(sep)
            continue
        cur.append(ch)
        in_word = True
        i += 1
    if in_word:
        words.append("".join(cur))
    if words:
        segs.append((words, ""))
    return segs


def _derive_program(words: list) -> int | None:
    """The index of the word a segment RUNS: past env assignments and wrappers, and past an
    interpreter and its options, so `bash -x run.sh` runs `run.sh` and `grep x run.sh` runs grep.
    None when the segment runs inline code (`-c`) or nothing at all."""
    i = 0
    while i < len(words):
        word = words[i]
        if ENV_ASSIGN_RE.fullmatch(word) or word in WRAPPERS:
            i += 1
        elif word == "timeout":
            i += 2 if i + 1 < len(words) and words[i + 1][:1].isdigit() else 1
        else:
            break
    if i >= len(words):
        return None
    if _derive_basename(words[i]).lower().removesuffix(".exe") not in INTERPRETERS:
        return i
    j = i + 1
    while j < len(words) and words[j].startswith("-"):
        if words[j] == "-c":
            return None
        if words[j] == "-m" and j + 1 < len(words):
            return j + 1
        j += 1
    return j if j < len(words) else i
# <<< invocation_segments


class CodeRecordError(RuntimeError):
    """A refusal: the record cannot be built, and why."""


# ------------------------------------------------------------------------------------------ the inputs

def read_code_config(root) -> dict:
    """`{value, ctags, extractors, languages, version}` of a derivation at `root`: the policy value, the
    ctags that answers under a ctags value, and the facts' version key."""
    value = read_policy_value(KEY, root)[0][0]
    found, says = "", ""
    if value != "builtin":
        found = shutil.which("ctags") or ""
        if not found:
            raise CodeRecordError(f"{KEY} is {value} and no ctags is on PATH: install one, or set the key to builtin")
        try:
            out = subprocess.run([found, "--version"], capture_output=True, text=True, encoding="utf-8",
                                 errors="replace", stdin=subprocess.DEVNULL, timeout=60).stdout
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise CodeRecordError(f"{KEY} is {value} and {found} did not answer --version: {exc}") from None
        says = " ".join((out.splitlines() or [""])[0].split(",")[0].split())
    h = hashlib.sha256()
    for name in ("code_record.py", "extract_code.py"):
        h.update((KIT_DIR / name).read_bytes().replace(b"\r\n", b"\n"))
    h.update(f"\n{value}\n{says}".encode("utf-8"))
    return {"value": value, "ctags": found, "version": h.hexdigest()[:12],
            "extractors": "builtin" + (f",ctags {says}" if found else ""),
            "languages": "python,shell,javascript" + (",ctags" if found else "")}


def resolve_tree(root, rev) -> str:
    try:
        return ti.read_git(root, "rev-parse", "--verify", "--quiet", f"{rev}^{{tree}}").strip()
    except ti.TagError:
        raise CodeRecordError(f"{rev} names no tree") from None


def derive_language(path, cfg) -> str:
    """The language `path` is read as under `cfg`, "" for a file no extractor reads."""
    ext = xc.ext_of(path)
    if ext in BUILTIN:
        return BUILTIN[ext]
    return "ctags:" + ext if cfg["ctags"] and "." + ext in xc.DEFINITION_CARRYING_EXTS else ""


def read_code_inputs(root, tree, cfg) -> dict:
    """The tree's listing under §4's bounds: `entries` `[(path, blob)]` of every tracked path, `code`
    `[(path, blob, language)]` sorted, `skipped` `{path: reason}`, `kits` the directories holding a `kit.toml`."""
    tree_lib, _ = ti.load_memory_tree()
    entries, code, skipped, kits = [], [], {}, set()
    for rec in tree_lib.read_git_output(root, ("ls-tree", "-r", "-l", "-z", "--full-tree", tree)).split(b"\0"):
        meta, _, raw = rec.partition(b"\t")
        fields = meta.split()
        if len(fields) == 4:
            entries.append((raw.decode("utf-8", "surrogateescape"), fields[2].decode(), fields[0], fields[3]))
    stdin = b"".join(p.encode("utf-8", "surrogateescape") + b"\0" for p, *_ in entries)
    cells = tree_lib.read_git_output(root, ("check-attr", "--source", tree, "--stdin", "-z", *ATTRS),
                                     stdin).decode("utf-8", "surrogateescape").split("\0") if entries else []
    attrs: dict = collections.defaultdict(dict)
    for i in range(0, len(cells) - 2, 3):
        attrs[cells[i]][cells[i + 1]] = cells[i + 2]
    for path, blob, mode, size in entries:
        got = attrs[path]
        if mode == b"160000":
            skipped[path] = "submodule"
        elif "set" in (got.get(ATTRS[0]), got.get(ATTRS[1])):
            continue
        elif got.get("filter") == "lfs":
            skipped[path] = "lfs"
        elif got.get("diff") == "unset":
            skipped[path] = "binary"
        else:
            if path.rsplit("/", 1)[-1] == "kit.toml" and "/" in path:
                kits.add(path.rsplit("/", 1)[0])
            lang = derive_language(path, cfg)
            if lang and not path.isprintable():   # a TAB, a line break or a byte outside UTF-8 is no cell
                skipped[path] = "a path no cell holds"
            elif lang and int(size) > CODE_FILE_CAP:
                skipped[path] = f"over {CODE_FILE_CAP} bytes"
            elif lang and mode != b"120000":
                code.append((path, blob, lang))
    return {"entries": [(p, b) for p, b, _m, _s in entries], "code": sorted(code), "skipped": skipped, "kits": kits}


def derive_kit(path, kits) -> str:
    """The nearest directory above `path` holding a `kit.toml`, "" for none."""
    up = path.rpartition("/")[0]
    while up and up not in kits:
        up = up.rpartition("/")[0]
    return up


def check_test_path(path) -> bool:
    name = path.rsplit("/", 1)[-1]
    return name.endswith(".test.sh") or name == "selftest.py" or (name.startswith("test_") and name.endswith(".py"))


# ------------------------------------------------------------------------------------------ one blob's facts

def check_interpreter(word) -> bool:
    if word.startswith("$"):
        return INTERPRETER_VAR.fullmatch(word) is not None
    return _derive_basename(word).lower().removesuffix(".exe") in INTERPRETERS


def extract_invocations(src, lang, argv) -> list:
    """The code paths, as spelled, a blob hands an interpreter: in a shell segment, through `_derive_program`,
    an interpreter held in a variable included, or in a Python or JavaScript argv literal."""
    words: set = set()

    def add_path(word):
        if word.endswith(CODE_SUFFIXES) and len(word) < 200 and word.isprintable():
            words.add(word)

    if lang == "shell":
        for seg, _sep in extract_segments(src):
            at = _derive_program(seg)
            if at is None:
                continue
            if check_interpreter(seg[at]) and seg[at].startswith("$"):
                at = next((j for j in range(at + 1, len(seg)) if not seg[j].startswith("-")), at)
            if at and any(check_interpreter(w) for w in seg[:at]):
                add_path(seg[at])
    elif lang == "javascript":
        for m in JS_ARGV.finditer(src):
            add_path(m.group(3))
    for seg in argv:
        at = next((j for j in range(1, len(seg)) if not seg[j].startswith("-")), 0)
        if at and check_interpreter(seg[0]):
            add_path(seg[at])
    return sorted(words)


def render_facts(got) -> bytes:
    """One blob's facts as compressed JSON: `e` why it was not read, or `d` the definitions, `c` the call sites
    per scope, its index in `d` or -1, and name, `i` imports, `b` bases, `t` assigns, `x` invocations."""
    if "error" in got:
        return zlib.compress(json.dumps({"e": got["error"]}).encode("utf-8"), 6)
    at: dict = {"": -1}
    for n, d in enumerate(got["defs"]):
        at.setdefault(d[0], n)
    sites: dict = collections.defaultdict(lambda: collections.defaultdict(list))
    for scope, name, line in got["calls"]:
        sites[at.get(scope, -1)][name].append(line)
    heads = {name.partition(".")[0] for _s, name, _l in got["calls"] if "." in name}
    doc = {"d": [[q, int(k == "class"), a, z, h] for q, k, a, z, h in got["defs"]],
           "c": [[s, [[n, *lines] for n, lines in sorted(names.items())]] for s, names in sorted(sites.items())],
           "i": sorted(set(map(tuple, got["imports"]))),
           "b": {k: v for k, v in sorted(got["bases"].items()) if v},
           "t": sorted({(s, v, d) for s, v, d in got["assigns"] if v in heads}), "x": got["invokes"]}
    return zlib.compress(json.dumps(doc, separators=(",", ":"), ensure_ascii=False).encode("utf-8", "surrogatepass"), 6)


def parse_facts(data) -> dict:
    return json.loads(zlib.decompress(data).decode("utf-8", "surrogatepass"))


def read_ctags_defs(cfg, want) -> dict:
    """`{path: [definition]}` in `extract_ranges`'s shape for `want` `{path: text}`, from one ctags run over
    copies in a scratch directory, no shell."""
    out: dict = {}
    with tempfile.TemporaryDirectory(prefix="ct") as top:
        for path, text in want.items():
            f = pathlib.Path(top, path)
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_bytes(text.encode("utf-8"))
        try:
            p = subprocess.run([cfg["ctags"], "--output-format=json", "--fields=+neKS", "-f", "-", "-L", "-"], cwd=top,
                               input="".join(x + "\n" for x in sorted(want)).encode("utf-8"), capture_output=True)
        except OSError as exc:
            raise CodeRecordError(f"{KEY} is {cfg['value']} and {cfg['ctags']} did not run: {exc}") from None
    if p.returncode:
        raise CodeRecordError(f"{KEY} is {cfg['value']} and {cfg['ctags']} exited {p.returncode}: "
                              + (p.stderr.decode("utf-8", "replace").strip().splitlines() or ["no message"])[0])
    tags: dict = collections.defaultdict(list)
    for line in p.stdout.decode("utf-8", "replace").splitlines():
        try:
            row = json.loads(line)
        except ValueError:
            continue
        kind = row.get("kind") if isinstance(row, dict) else None
        path = str(row.get("path", "")).replace("\\", "/").removeprefix("./") if kind else ""
        if path in want and (kind in CTAGS_FUNCTIONS or kind in CTAGS_CLASSES) and isinstance(row.get("line"), int):
            scope = re.sub(r"::|[/#]", ".", str(row.get("scope") or ""))
            name = str(row.get("name", "")).replace(".", "_")
            tags[path].append((row["line"], int(row.get("end") or row["line"]), kind, scope, name))
    for path, rows in tags.items():
        lines, held, defs = want[path].split("\n"), set(), []
        for line, end, kind, scope, name in sorted(rows):
            if not name or not name.isprintable():
                continue
            qual = f"{scope}.{name}" if scope in held else name
            held.add(qual)
            defs.append((qual, "class" if kind in CTAGS_CLASSES else "function", line, max(end, line),
                         xc.derive_range_hash(lines, line, max(end, line))))
        out[path] = derive_preorder(defs)
    return out


def derive_preorder(defs) -> list:
    """`defs` with each nested definition after its parent's, whatever order a reader listed them in, so a depth
    and a name are enough to read a qualified name back."""
    first: dict = {}
    for n, d in enumerate(defs):
        first.setdefault(d[0], n)

    def derive_rank(qual):
        parts = qual.split(".")
        return [first.get(".".join(parts[:k + 1]), 0) for k in range(len(parts))]

    return [d for _r, _n, d in sorted((derive_rank(d[0]), n, d) for n, d in enumerate(defs))]


def extract_facts(text, path, lang, ctags_defs) -> dict:
    """`render_facts`'s input for one blob's text: `{"error": why}` where the extractor raises."""
    got = {"defs": [], "calls": [], "imports": [], "bases": {}, "assigns": [], "argv": []}
    if not lang.startswith("ctags:"):
        try:
            got = xc.extract_ranges(text, xc.ext_of(path))
        except (SyntaxError, ValueError, RecursionError) as exc:
            why = getattr(exc, "msg", None) or str(exc) or type(exc).__name__
            return {"error": " ".join(str(why).split())[:120]}
    if ctags_defs is not None:
        got["defs"] = ctags_defs
    got["imports"] = [i for i in got["imports"] if not re.search(r"\s", i[1])]   # a module the `i` line can hold
    got["invokes"] = extract_invocations(text, lang, got["argv"])
    return got


# ------------------------------------------------------------------------------------------ the resolution

def build_ordinals(code, facts) -> tuple:
    """`(rows, ordinal)`: `rows` `[(path, qualified name, "module", "function" or "class", line, end, hash)]`
    in record order, and `ordinal` `{(path, qualified name): its first row}`."""
    rows, ordinal = [], {}
    for path, blob, lang in code:
        ordinal[(path, "")] = len(rows)
        rows.append((path, "", "module", 0, 0, ""))
        for qual, is_class, line, end, digest in facts[(blob, lang)]["d"]:
            ordinal.setdefault((path, qual), len(rows))
            rows.append((path, qual, "class" if is_class else "function", line, end, digest))
    return rows, ordinal


def scan_sites(fact):
    """`(scope, name, line)` of each call site in one blob's facts, in line order within a scope and a name."""
    for at, names in fact["c"]:
        scope = fact["d"][at][0] if at >= 0 else ""
        for name, *lines in names:
            for line in lines:
                yield scope, name, line


def resolve_calls(code, facts, rows, ordinal, kits) -> dict:
    """Every call site over the tree: `sites` `[(source ordinal, language, target ordinal or None, name, line)]`,
    a None target a kept mention, `dropped` per language and `ambiguous` `{language: (ambiguous, sites)}`.

    Python resolves import-aware (§2 S3); shell and JavaScript under the ambiguity test (S4), where a language
    past AMBIGUOUS_SHARE has every edge read as a mention."""
    fact_of = {path: facts[(blob, lang)] for path, blob, lang in code}
    classes = {(r[0], r[1]) for r in rows if r[2] == "class"}
    stems: dict = collections.defaultdict(list)
    for path in fact_of:
        if path.endswith(".py"):
            stems[path.rsplit("/", 1)[-1][:-3]].append(path)

    @functools.cache
    def resolve_module(frm, mod):
        dots = len(mod) - len(mod.lstrip("."))
        here = frm.rpartition("/")[0]
        for _ in range(dots - 1):
            here = here.rpartition("/")[0]
        name = mod[dots:].replace(".", "/")
        near = "/".join(p for p in (here, name) if p)
        for cand in (f"{near}.py", f"{near}/__init__.py", *(() if dots else (f"{name}.py", f"{name}/__init__.py"))):
            if cand in fact_of:
                return cand
        held = stems[name.rsplit("/", 1)[-1]]
        return held[0] if len(held) == 1 else None

    @functools.cache
    def read_imports(path):
        return {local: (resolve_module(path, mod), name, mod) for local, mod, name in fact_of[path]["i"]}

    @functools.cache
    def resolve_name(path, dotted, depth=0):
        if depth > 6:
            return None
        if (path, dotted) in ordinal:
            return path, dotted
        head, _, rest = dotted.partition(".")
        mod, name, spelled = read_imports(path).get(head, (None, "", ""))
        if mod and name:
            hit = resolve_name(mod, name + ("." + rest if rest else ""), depth + 1)
            if hit:
                return hit
        elif mod and rest:
            return resolve_name(mod, rest, depth + 1)
        if name and rest:   # `from pkg import mod`, then `mod.f()`
            sub = resolve_module(path, spelled + ("" if not spelled.strip(".") else ".") + name)
            if sub and (sub, rest) in ordinal:
                return sub, rest
        return None

    @functools.cache
    def resolve_method(path, cls, name, depth=0):
        if depth > 8:
            return None
        if (path, f"{cls}.{name}") in ordinal:
            return path, f"{cls}.{name}"
        for base in fact_of[path]["b"].get(cls, ()):
            hit = resolve_name(path, base)
            if hit and hit != (path, cls):
                got = resolve_method(*hit, name, depth + 1)
                if got:
                    return got
        return None

    def scan_scopes(scope):
        while scope:
            yield scope
            scope = scope.rpartition(".")[0]
        yield ""

    def resolve_python(path, scope, dotted, assigned):
        for s in scan_scopes(scope):
            qual = f"{s}.{dotted}" if s else dotted
            if (path, qual) in ordinal and (path, s) not in classes:
                return path, qual
        hit = resolve_name(path, dotted)
        head, _, rest = dotted.partition(".")
        if hit or not rest or "." in rest:
            return hit
        if head in ("self", "cls"):
            cls = next((s for s in scan_scopes(scope) if (path, s) in classes), "")
            return resolve_method(path, cls, rest) if cls else None
        maker = next((assigned[(s, head)] for s in scan_scopes(scope) if (s, head) in assigned), None)
        for spelled in (maker, head):
            hit = spelled and resolve_name(path, spelled)
            if hit in classes:
                return resolve_method(*hit, rest)
        return None

    named: dict = {"python": set(), "shell": collections.defaultdict(list), "javascript": collections.defaultdict(list)}
    for path, qual in ordinal:
        lang = BUILTIN.get(xc.ext_of(path))
        if qual and lang == "python":
            named["python"].add(qual.rsplit(".", 1)[-1])
        elif qual and lang:
            named[lang][qual.rsplit(".", 1)[-1]].append((path, qual))

    @functools.cache
    def scan_reach(path, lang, name):
        """The candidates at the first level holding one: the caller's own file, its sourced files, its kit."""
        held = named[lang].get(name, ())
        own = derive_kit(path, kits)
        sourced = {mod.rsplit("/", 1)[-1].removesuffix(".js") for _l, mod, _n in fact_of[path]["i"]}
        for level in (lambda p: p == path, lambda p: p.rsplit("/", 1)[-1].removesuffix(".js") in sourced,
                      lambda p: own and derive_kit(p, kits) == own):
            got = [c for c in held if level(c[0])]
            if got:
                return got
        return []

    sites, dropped, total, doubt = [], collections.Counter(), collections.Counter(), collections.Counter()
    for path, _blob, lang in code:
        if lang not in named:
            continue
        fact, home = fact_of[path], ordinal[(path, "")]
        assigned = {(s, v): d for s, v, d in fact["t"]}
        for scope, name, line in scan_sites(fact):
            last = name.rsplit(".", 1)[-1]
            src = ordinal.get((path, scope), home)
            if lang == "python":
                hit = resolve_python(path, scope, name, assigned)
                if not hit and last not in named["python"]:
                    dropped[lang] += 1
                    continue
            else:
                reach = scan_reach(path, lang, last)
                if not reach:   # no candidate in reach is no site
                    continue
                total[lang] += 1
                doubt[lang] += len(reach) > 1
                hit = reach[0] if len(reach) == 1 else None
            sites.append((src, lang, ordinal[hit] if hit else None, last, line))
    ambiguous = {lang: (n, total[lang]) for lang, n in sorted(doubt.items()) if n > AMBIGUOUS_SHARE * total[lang]}
    if ambiguous:
        sites = [(s, lang, None if lang in ambiguous else d, n, ln) for s, lang, d, n, ln in sites]
    return {"sites": sites, "dropped": dropped, "ambiguous": ambiguous, "seen": dict(total), "doubt": dict(doubt)}


def resolve_invocations(code, facts, ordinal) -> set:
    """`{(source file's ordinal, invoked file's ordinal)}` over the tree's facts."""
    by_name: dict = collections.defaultdict(list)
    for path, _b, _l in code:
        by_name[path.rsplit("/", 1)[-1]].append(path)

    def resolve_path(word, frm):
        parts = word.replace("\\", "/").split("/")
        cut = max((n + 1 for n, p in enumerate(parts[:-1]) if re.search(r"[$\"'}){(`]", p)), default=0)
        parts[-1] = re.sub(r"^\$\{[^}]*\}", "", parts[-1])   # `${PFX}check.sh`
        word = "/".join(p for p in parts[cut:] if p != ".").removeprefix("../")
        here = frm.rpartition("/")[0]
        for cand in (word, f"{here}/{word}" if here else word):
            if (cand, "") in ordinal:
                return cand
        held = [p for p in by_name.get(word.rsplit("/", 1)[-1], ()) if p.endswith("/" + word)]
        return held[0] if len(held) == 1 else None

    out = set()
    for path, blob, lang in code:
        for word in facts[(blob, lang)]["x"]:
            hit = resolve_path(word, path)
            if hit and hit != path:
                out.add((ordinal[(path, "")], ordinal[(hit, "")]))
    return out


def read_registry_edges(manifest, kit_files, tool_rel, ordinal) -> list:
    """`[(leg or kit, the file's ordinal)]`: each manifest row's argv paths, and each `kit.toml`'s `version_from`."""
    out = set()
    try:
        legs = json.loads(manifest) if manifest else []
    except ValueError:
        legs = []
    for leg in legs if isinstance(legs, list) else (legs.get("legs") or []):
        for word in (leg.get("argv") or []) if isinstance(leg, dict) else []:
            path = ti.resolve_prefix_token(word, tool_rel).removeprefix("./")
            if (path, "") in ordinal:
                out.add((str(leg.get("name", "")), ordinal[(path, "")]))
    for path, text in kit_files.items():
        try:
            doc = tomllib.loads(text or "")
        except tomllib.TOMLDecodeError:
            continue
        ver, kid = doc.get("version_from"), doc.get("id")
        if isinstance(ver, dict) and isinstance(kid, str):
            dst = f"{path.rpartition('/')[0]}/{ver.get('file')}"
            if (dst, "") in ordinal:
                out.add((kid, ordinal[(dst, "")]))
    return sorted((n, o) for n, o in out if n and n.isprintable())


def derive_tool_rel(root) -> str:
    """The tool root the record's `gate-legs.json` sits in: this kit's parent relative to `root`, or `tools`
    for a repository this kit is not installed in."""
    try:
        return KIT_DIR.parent.resolve().relative_to(pathlib.Path(root).resolve()).as_posix()
    except ValueError:
        return "tools"


# ------------------------------------------------------------------------------------------ the text

def render_code_record(cfg, code, facts, rows, ordinal, calls, invokes, registers, skipped) -> str:
    """The record's one text, §4's grammar as the module docstring spells it."""
    out = [f"code-record 1\t{cfg['extractors']}\t{cfg['languages']}"]
    edges: dict = collections.defaultdict(set)
    names: dict = collections.defaultdict(set)
    runs: dict = collections.defaultdict(set)
    for src, _lang, dst, name, _line in calls["sites"]:
        if dst is None:
            names[src].add(name)
        else:
            edges[src].add(dst)
    for src, dst in invokes:
        runs[src].add(dst)
    imported = {}
    for path, blob, lang in code:
        mods: dict = collections.defaultdict(set)
        for _local, mod, name in facts[(blob, lang)]["i"]:
            mods[mod].update([name] if name else [])
        imported[path] = " ".join(m + (":" + ",".join(sorted(n)) if n else "") for m, n in sorted(mods.items()))

    def add_edges(at):
        for tag, held in (("c", edges), ("m", names)):
            if held.get(at):
                out.append(f"{tag}\t" + " ".join(map(str, sorted(held[at]))))

    for at, (path, qual, kind, line, end, digest) in enumerate(rows):
        if kind == "module":
            out.append(f"f\t{path}")
            if imported[path]:
                out.append(f"i\t{imported[path]}")
            add_edges(at)
            if runs.get(at):
                out.append("x\t" + " ".join(map(str, sorted(runs[at]))))
            continue
        out.append(f"d\t{qual.count('.')}{'C' if kind == 'class' else ''}\t{qual.rsplit('.', 1)[-1]}\t{line}-{end}\t{digest}")
        if ordinal[(path, qual)] == at:
            add_edges(at)
    out += [f"r\t{name}\t{at}" for name, at in registers]
    out += [f"a\t{lang}\t{n}/{m}" for lang, (n, m) in sorted(calls["ambiguous"].items())]
    out += [f"s\t{p if p.isprintable() else json.dumps(p)}\t{why}" for p, why in sorted(skipped.items())]
    return "\n".join(out) + "\n"


def parse_code_record(text) -> dict:
    """The text read back: `rows` as `build_ordinals` answers them, `calls`, `mentions` and `invokes` by source
    ordinal, `registers`, `ambiguous`, `skipped`, `extractors` and `languages`."""
    got = {"rows": [], "calls": {}, "mentions": {}, "invokes": {}, "registers": [], "ambiguous": {}, "skipped": {}}
    lines = text.split("\n")
    head = lines[0].split("\t")
    if len(head) != 3 or head[0] != "code-record 1":
        raise CodeRecordError(f"the record opens {lines[0][:60]!r}, no `code-record 1` line")
    got["extractors"], got["languages"] = head[1:]
    path, above = "", []
    for line in lines[1:]:
        tag, _, body = line.partition("\t")
        cells = body.split("\t")
        if tag == "f":
            path, above = body, []
            got["rows"].append((path, "", "module", 0, 0, ""))
        elif tag == "d":
            above[int(cells[0].rstrip("C")):] = [cells[1]]
            first, _, last = cells[2].partition("-")
            got["rows"].append((path, ".".join(above), "class" if cells[0].endswith("C") else "function", int(first),
                                int(last), cells[3]))
        elif tag in ("c", "x"):
            got["calls" if tag == "c" else "invokes"][len(got["rows"]) - 1] = [int(n) for n in body.split()]
        elif tag == "m":
            got["mentions"][len(got["rows"]) - 1] = body.split()
        elif tag == "r":
            got["registers"].append((cells[0], int(cells[1])))
        elif tag == "a":
            got["ambiguous"][cells[0]] = cells[1]
        elif tag == "s":
            got["skipped"][cells[0]] = cells[1]
        elif tag not in ("i", ""):
            raise CodeRecordError(f"the record holds a line of no known kind: {line[:60]!r}")
    return got


# ------------------------------------------------------------------------------------------ the derivation

def build_derivation(root, tree, cfg, held, ceiling) -> dict:
    """One derivation over `tree`: `text`, and what it was derived from. `held` is `{(blob, language): facts
    bytes}` already extracted at this version; `fresh` holds what this run extracted. Past `ceiling` seconds
    it stops with `degraded` set and no text."""
    start = time.perf_counter()
    tree_lib, _ = ti.load_memory_tree()
    inputs = read_code_inputs(root, tree, cfg)
    skipped, tool_rel = inputs["skipped"], derive_tool_rel(root)
    out = {"tree": tree, "inputs": inputs, "fresh": {}, "degraded": "", "text": "", "facts": {}}

    def check_ceiling():
        if time.perf_counter() - start > ceiling:
            out["degraded"] = "time ceiling"
        return bool(out["degraded"])

    todo: dict = {}
    for path, blob, lang in inputs["code"]:
        if (blob, lang) not in held:
            todo.setdefault((blob, lang), path)
    if check_ceiling():
        return out
    manifest = f"{tool_rel}/gate-legs.json" if tool_rel != "." else "gate-legs.json"
    tomls = sorted(f"{k}/kit.toml" for k in inputs["kits"])
    texts = tree_lib.read_blobs_at(root, [(tree, p) for p in [*todo.values(), manifest, *tomls]])
    want = {p: texts[(tree, p)] for (_b, lang), p in todo.items() if texts[(tree, p)] is not None
            and (cfg["value"] == "ctags" or lang.startswith("ctags:"))}
    tagged = read_ctags_defs(cfg, want) if want else {}
    for (blob, lang), path in todo.items():
        if check_ceiling():
            return out
        text = texts[(tree, path)]
        got = {"error": "binary"} if text is None else \
            extract_facts(text, path, lang, tagged.get(path, []) if path in want else None)
        out["fresh"][(blob, lang)] = render_facts(got)
    code = []
    for path, blob, lang in inputs["code"]:
        data = out["fresh"].get((blob, lang)) or held[(blob, lang)]
        fact = out["facts"].setdefault((blob, lang), parse_facts(data))
        if "e" in fact:
            skipped[path] = fact["e"]
        else:
            code.append((path, blob, lang))
        out.setdefault("sizes", {})[(blob, lang)] = len(data)
    rows, ordinal = build_ordinals(code, out["facts"])
    calls = resolve_calls(code, out["facts"], rows, ordinal, inputs["kits"])
    invokes = resolve_invocations(code, out["facts"], ordinal)
    registers = read_registry_edges(texts[(tree, manifest)], {p: texts[(tree, p)] for p in tomls}, tool_rel, ordinal)
    out.update(code=code, rows=rows, calls=calls, invokes=invokes, registers=registers)
    out["text"] = render_code_record(cfg, code, out["facts"], rows, ordinal, calls, invokes, registers, skipped)
    if check_ceiling():
        out["text"] = ""
    return out


class CodeRecord:
    """One tree's record: `text`, `degraded`, and the rows of §4 "The readers". `code_row`, `code_meta` and
    `edges`, the ordinals' own, are read from the text; `code_file` reads the listing; `code_edge`, which
    carries each call's line, resolves over the facts once."""

    def __init__(self, root, tree, cfg, text, degraded="", derived=None):
        self.root, self.tree, self.cfg, self.text, self.degraded = root, tree, cfg, text, degraded
        self._derived = derived

    def parse_edges(self) -> dict:
        return parse_code_record(self.text)

    edges = functools.cached_property(parse_edges)

    def read_inputs(self) -> dict:
        return self._derived["inputs"] if self._derived else read_code_inputs(self.root, self.tree, self.cfg)

    inputs = functools.cached_property(read_inputs)

    def derive_rows(self) -> list:
        """`(path, key, kind, name, line, end_line, hash)` per definition."""
        return [(p, f"{p}::{q}", k, q, a, z, h) for p, q, k, a, z, h in self.edges["rows"] if k != "module"]

    code_row = functools.cached_property(derive_rows)

    def derive_files(self) -> list:
        """`(path, blob, lang, kit, test, skipped)` per tracked path."""
        why, kits = self.edges["skipped"], self.inputs["kits"]
        return [(p, b, derive_language(p, self.cfg), derive_kit(p, kits), check_test_path(p),
                 why.get(p if p.isprintable() else json.dumps(p), "")) for p, b in self.inputs["entries"]]

    code_file = functools.cached_property(derive_files)

    def derive_edges(self) -> list:
        """`(src, dst, type, line)`: `calls` and `mention` per site, `invokes` and `registers` at line 0, and
        `tests` beside each `calls` or `invokes` out of a test file."""
        if self._derived is None:
            held, con = {}, ti.load_index(self.root)
            try:
                con.executescript(TABLES)
                held = read_held_facts(con, self.cfg["version"])
            finally:
                con.close()
            self._derived = build_derivation(self.root, self.tree, self.cfg, held, float("inf"))
        d = self._derived

        def render_key(at):
            path, qual = d["rows"][at][:2]
            return f"{path}::{qual}" if qual else path

        out = [(render_key(src), name if dst is None else render_key(dst), "mention" if dst is None else "calls", line)
               for src, _lang, dst, name, line in d["calls"]["sites"]]
        out += [(render_key(s), render_key(t), "invokes", 0) for s, t in sorted(d["invokes"])]
        out += [(s, t, "tests", n) for s, t, kind, n in out
                if kind != "mention" and check_test_path(s.partition("::")[0])]
        return out + [(name, render_key(at), "registers", 0) for name, at in d["registers"]]

    code_edge = functools.cached_property(derive_edges)

    def derive_meta(self) -> dict:
        if self.degraded:
            return {"extractors": self.cfg["extractors"], "languages": self.cfg["languages"], "ambiguous": {},
                    "degraded": self.degraded}
        return {k: self.edges[k] for k in ("extractors", "languages", "ambiguous")} | {"degraded": ""}

    code_meta = functools.cached_property(derive_meta)


def read_held_facts(con, version) -> dict:
    return {(b, lang): f for b, lang, f in con.execute("SELECT blob, lang, facts FROM code_facts WHERE version=?",
                                                       (version,))}


def write_code_rows(con, root, version, derived) -> None:
    """Store one whole derivation's new facts and its text, then drop what no worktree's HEAD holds, in one
    `BEGIN IMMEDIATE` transaction."""
    if derived["degraded"]:
        raise CodeRecordError("a degraded record is never written")
    try:
        with con:
            con.execute("BEGIN IMMEDIATE")
            con.executemany("INSERT OR REPLACE INTO code_facts VALUES (?,?,?,?)",
                            [(b, lang, version, f) for (b, lang), f in derived["fresh"].items()])
            con.execute("INSERT OR REPLACE INTO code_tree VALUES (?,?,?)", (derived["tree"], version, derived["text"]))
            remove_unheld_code_rows(con, root, derived["tree"])
    except sqlite3.OperationalError as exc:
        raise CodeRecordError(f"the index is locked or unwritable: {exc}") from None


def remove_unheld_code_rows(con, root, tree) -> None:
    """Drop the text of every tree no worktree's HEAD names, and the facts of every blob none of those trees holds,
    `tree` listed first, since it holds most of them.
    A facts row of another version stays while its blob is held: another worktree may derive that version."""
    trees, _tops = ti.read_worktree_trees(root)
    for (held,) in con.execute("SELECT DISTINCT tree FROM code_tree").fetchall():
        if held not in trees:
            con.execute("DELETE FROM code_tree WHERE tree=?", (held,))
    loose = {b for (b,) in con.execute("SELECT DISTINCT blob FROM code_facts")}
    for held in sorted(trees, key=lambda t: (t != tree, t)):
        if not loose:
            break
        loose -= {rec.split("\t", 1)[0].split()[-1] for rec in
                  ti.read_git(root, "ls-tree", "-r", "-z", "--full-tree", held).split("\0") if rec}
    con.executemany("DELETE FROM code_facts WHERE blob=?", [(b,) for b in sorted(loose)])


def derive_code_record(root, tree="HEAD", *, ceiling=CODE_RUN_CEILING) -> CodeRecord:
    """THE reader's door: `tree`'s record, from the cached text where the index holds one at this version, else
    derived and written. Degraded past `ceiling`, marked so and never written."""
    cfg, sha = read_code_config(root), resolve_tree(root, tree)
    con = ti.load_index(root)
    try:
        con.executescript(TABLES)
        row = con.execute("SELECT record FROM code_tree WHERE tree=? AND version=?", (sha, cfg["version"])).fetchone()
        if row:
            return CodeRecord(root, sha, cfg, row[0])
        derived = build_derivation(root, sha, cfg, read_held_facts(con, cfg["version"]), ceiling)
        if not derived["degraded"]:
            write_code_rows(con, root, cfg["version"], derived)
        return CodeRecord(root, sha, cfg, derived["text"], derived["degraded"], derived)
    finally:
        con.close()


# ------------------------------------------------------------------------------------------ the verbs

def print_degraded(why) -> int:
    print(f"code-record: degraded = {why}")
    print("code-record: floor · git grep -n -w <name>: a reader of a degraded record uses `git grep`")
    return 2


def check_code_record(root, ceiling) -> int:
    """`--check`: HEAD's record re-derived from the blobs and compared, byte for byte, to the cached text."""
    cfg, sha = read_code_config(root), resolve_tree(root, "HEAD")
    con = ti.load_index(root)
    try:
        con.executescript(TABLES)
        row = con.execute("SELECT record FROM code_tree WHERE tree=? AND version=?", (sha, cfg["version"])).fetchone()
        d = build_derivation(root, sha, cfg, read_held_facts(con, cfg["version"]), ceiling)
        if d["degraded"]:
            return print_degraded(d["degraded"])
        if not d["code"]:
            print("code-record: unarmed — the tree holds no code file the record reads")
            return 1
        if row is None or d["fresh"]:
            if row is None or row[0] == d["text"]:
                write_code_rows(con, root, cfg["version"], d)
    finally:
        con.close()
    kept = collections.Counter(lang for _s, lang, dst, _n, _l in d["calls"]["sites"] if dst is None)
    made = collections.Counter(lang for _s, lang, dst, _n, _l in d["calls"]["sites"] if dst is not None)
    defs = collections.Counter(derive_language(r[0], cfg) for r in d["rows"] if r[2] != "module")
    for lang in sorted(defs | made | kept):
        n, m = d["calls"]["doubt"].get(lang, 0), d["calls"]["seen"].get(lang, 0)
        print(f"code-record: {lang} · definitions {defs[lang]} · calls {made[lang]} · mentions kept {kept[lang]} · "
              f"mentions dropped {d['calls']['dropped'][lang]}" + (f" · ambiguous {n}/{m}" if m else ""))
    why = collections.Counter(d["inputs"]["skipped"].values())
    print("code-record: skipped · " + (", ".join(f"{r} {n}" for r, n in sorted(why.items())) or "none"))
    print(f"code-record: files {len(d['code'])} · parses {len(d['fresh'])} · invocations {len(d['invokes'])} · "
          f"registry edges {len(d['registers'])} · bytes {len(d['text'].encode('utf-8'))}")
    if row is not None and row[0] != d["text"]:
        old, new = row[0].split("\n"), d["text"].split("\n")
        n = next((i for i in range(max(len(old), len(new))) if old[i:i + 1] != new[i:i + 1]), 0)
        print(f"code-record: RED the cached text of tree {sha[:12]} differs at line {n + 1}: cached "
              f"{(old[n:n + 1] or ['<end>'])[0][:120]!r}, derived {(new[n:n + 1] or ['<end>'])[0][:120]!r}")
        print(f"code-record: remedy · delete {ti.derive_index_path(root).as_posix()}, which costs one rebuild")
        return 1
    print("code-record: green · " + ("the cached text is the derivation's" if row is not None else "derived and cached"))
    return 0


def measure_code_record(root, rev) -> int:
    """`--time`: one cold derivation, no row read or written, and its three figures."""
    start = time.perf_counter()
    cfg = read_code_config(root)
    d = build_derivation(root, resolve_tree(root, rev), cfg, {}, float("inf"))
    took = time.perf_counter() - start
    print(f"code-record: seconds {took:.2f} · bytes {len(d['text'].encode('utf-8'))} · facts {sum(d['sizes'].values())}")
    print(f"code-record: tree {d['tree'][:12]} · tracked {len(d['inputs']['entries'])} · files {len(d['code'])} · "
          f"definitions {sum(r[2] != 'module' for r in d['rows'])} · skipped {len(d['inputs']['skipped'])}")
    return 0


def print_neighbourhood(root, paths, ceiling) -> int:
    """`neighbourhood`: the rows around the seed paths' definitions, never a body line."""
    rec = derive_code_record(root, "HEAD", ceiling=ceiling)
    if rec.degraded:
        return print_degraded(rec.degraded)
    tracked = {p for p, _b in rec.inputs["entries"]}
    seeds = [p.replace("\\", "/").removeprefix("./") for p in paths]
    for p in seeds:
        if p not in tracked:
            raise CodeRecordError(f"{p} is no path HEAD tracks")
    rows, calls = rec.edges["rows"], rec.edges["calls"]
    mine = [n for n, r in enumerate(rows) if r[0] in seeds and r[2] != "module"]
    held, out = set(mine), []

    def render_def(at, tail):
        path, qual, kind, line, end, _h = rows[at]
        return (path, line, end, f"{path}:{line}-{end} · {kind} {qual} · {tail}")

    first: dict = {}
    for n, r in enumerate(rows):
        first.setdefault((r[0], r[1]), n)
    out += sorted(render_def(n, "def") for n in mine if first[rows[n][:2]] == n)
    near: dict = {"caller": set(), "test": set(), "callee": set()}
    for src, dsts in calls.items():
        path = rows[src][0]
        for dst in held.intersection(dsts):
            seed, tail = rows[dst][1], "test" if check_test_path(path) else "caller"
            if rows[src][2] != "module":
                near[tail].add(render_def(src, f"{tail} {seed}"))
                continue
            stem = path.rsplit("/", 1)[-1].partition(".")[0]
            for s, t, kind, line in rec.code_edge:
                if kind == "calls" and s == path and t == f"{rows[dst][0]}::{seed}":
                    near[tail].add((path, line, line, f"{path}:{line}-{line} · module {stem} · {tail} {seed}"))
        if src in held:
            near["callee"] |= {render_def(dst, f"callee {rows[src][1]}") for dst in dsts if rows[dst][2] != "module"}
    for tail in ("caller", "callee", "test"):
        out += sorted(near[tail])
    lines = [r[3] for r in out]
    homes = {derive_kit(rows[n][0], rec.inputs["kits"]) for n in mine} - {""}
    lines += [f"{p} · sibling" for p in sorted(tracked) if p not in seeds and derive_kit(p, rec.inputs["kits"]) in homes]
    if lines:
        print("\n".join(lines))
    return 0


# ------------------------------------------------------------------------------------------ the fixtures

def build_code_fixture(root, rev="HEAD") -> pathlib.Path:
    """`--fixture adopter`: a repository under the temp folder whose HEAD holds `root`'s tracked files at `rev`
    twice, at its root and under `vendor/` marked vendored, beside 50 binaries, 20 LFS pointers named `.py`, one
    submodule and five source files of 5 MiB. Built through an index alone, no file checked out, its objects
    borrowed from `root`'s, so no path is ever too long. The caller removes it."""
    from gov_tag import run_git
    base = resolve_tree(root, rev)
    top = pathlib.Path(tempfile.mkdtemp(prefix="cr"))
    run_git(top, "init", "-q", "-b", "main")
    objects = (ti.common_git_dir(pathlib.Path(root)) / "objects").as_posix()
    (top / ".git" / "objects" / "info" / "alternates").write_bytes((objects + "\n").encode("utf-8"))
    run_git(top, "read-tree", base)
    run_git(top, "read-tree", "--prefix=vendor/", base)
    attrs = run_git(top, "cat-file", "blob", f"{base}:.gitattributes") if run_git(
        top, "ls-tree", base, ".gitattributes").strip() else ""
    plants = {".gitattributes": attrs + "\nvendor/** linguist-vendored\n*.bin binary\n"
                                        "lfs/** filter=lfs diff=lfs merge=lfs -text\n"}
    plants |= {f"lfs/l{i}.py": f"version https://git-lfs.github.com/spec/v1\noid sha256:{i:064d}\nsize 1\n" for i in range(20)}
    plants |= {f"big/g{i}.py": f"x = {i}  # pad\n" + "x = 1  # pad\n" * 403299 for i in range(5)}
    plants |= {f"bin/b{i}.bin": f"\0\1\2{i}" * 64 for i in range(50)}
    scratch = top / "plant"
    info = [f"160000 {'1' * 40}\tsub"]
    for path, text in plants.items():
        scratch.write_bytes(text.encode("utf-8"))
        info.append(f"100644 {run_git(top, 'hash-object', '-w', '--no-filters', str(scratch)).strip()}\t{path}")
    scratch.unlink()
    tree_lib, _ = ti.load_memory_tree()
    tree_lib.read_git_output(top, ("update-index", "--add", "--index-info"), ("\n".join(info) + "\n").encode("utf-8"))
    run_git(top, "update-ref", "HEAD", run_git(top, "commit-tree", run_git(top, "write-tree").strip(), "-m", "fixture").strip())
    return top


#: the files of the resolution arms' repository, `{path: text}`
ARM_FILES = {
    "a.py": "import os\n\n\nclass K:\n    def m(self):\n        def inner():\n            return 1\n        return inner()\n"
            "\n    def n(self):\n        return self.m()\n\n\ndef f():\n    return 1\n\n\ndef _p():\n    return f()\n",
    "b.py": "from a import f\nfrom d import D\n\n\ndef g():\n    obj = D()\n    obj.g()\n    return f()\n\n\ndef h(x):\n"
            "    x.f()\n    x.nowhere()\n",
    "c.py": "class Base:\n    def g(self):\n        return 2\n",
    "d.py": "from c import Base\n\n\nclass D(Base):\n    pass\n",
    "s.sh": "#!/bin/sh\nrun_it() {\n  echo hi\n}\nrun_it\n",
    "j.js": "const LEAD = 'x'\nfunction jf(a) {\n  return jg(a)\n}\nconst jg = (a) => a\n",
    "test_a.py": "from a import f\n\n\ndef test_f():\n    f()\n",
    "top.py": "import a\n\na.f()\n",
    "go.sh": "#!/bin/sh\npython y.py --flag\n",
    "y.py": "def main():\n    return 0\n",
    "z.sh": "echo z\n",
    "tools/kx/kit.toml": 'id = "kx"\nversion_from = { file = "v.py", pattern = "^V = " }\n',
    "tools/kx/v.py": "V = 1\n",
    "tools/kx/w.py": "def w():\n    return 1\n",
    "tools/kx/note.md": "a note\n",
    "tools/gate-legs.json": '[{"name": "leg z", "argv": ["bash", "{prefix}/../z.sh"]}, '
                            '{"name": "leg v", "argv": ["python", "{prefix}/kx/v.py"]}]\n',
}


def run_selftest() -> int:
    """Every fixture arm of TOOL-dTotalRecall-8 §6 but the adopter-scale one, each over its own scratch repository.
    `build_code_fixture` itself is built by AC1's `--fixture adopter`, a cold derivation too long for a suite;
    the bounds it plants are planted here at their own size."""
    import contextlib
    import io

    from gov_tag import build_scratch_dir, run_git, write_commit
    failed: list = []

    def check_arm(name, held, shown=""):
        print(f"arm {'ok  ' if held else 'FAIL'}  code-record {name}" + ("" if held else f" — {shown}"[:900]))
        if not held:
            failed.append(name)

    def run_verb(verb, *args):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            try:
                rc = verb(*args)
            except (CodeRecordError, PolicyRefused) as exc:
                rc = 2
                print(f"refused · {exc}")
        return rc, out.getvalue()

    def read_parses(said):
        got = re.search(r" parses (\d+) ", said)
        return int(got.group(1)) if got else -1

    def build_repo(top, name, files):
        root = pathlib.Path(top) / name
        root.mkdir()
        run_git(root, "init", "-q", "-b", "main")
        run_git(root, "config", "core.autocrlf", "false")
        write_commit(root, files, name)
        return root

    def read_calls(rec, key):
        got = rec.edges
        at = next(n for n, r in enumerate(got["rows"]) if (f"{r[0]}::{r[1]}" if r[1] else r[0]) == key)
        dst = {f"{r[0]}::{r[1]}" for r in (got["rows"][n] for n in got["calls"].get(at, []))}
        return dst, got["mentions"].get(at, []), got["invokes"].get(at, [])

    with build_scratch_dir("cr-") as top:
        root = build_repo(top, "r", ARM_FILES)
        rec = derive_code_record(root)
        rows = {r[1]: r for r in rec.code_row}
        want = {"a.py::K": "class", "a.py::K.m": "function", "a.py::K.m.inner": "function", "a.py::f": "function",
                "a.py::_p": "function", "s.sh::run_it": "function", "j.js::jf": "function", "j.js::jg": "function"}
        check_arm("definitions", all(k in rows and rows[k][2] == v for k, v in want.items())
                  and "j.js::LEAD" not in rows and rows["a.py::K.m.inner"][4:6] == (6, 7)
                  and "d\t2\tinner\t6-7\t" in rec.text and "d\t0C\tK\t4-11\t" in rec.text, rec.text)
        files = {r[0]: r for r in rec.code_file}
        check_arm("tests and kits", ("test_a.py::test_f", "a.py::f", "tests", 5) in rec.code_edge
                  and files["tools/kx/note.md"][3] == "tools/kx" and files["test_a.py"][4] and not files["a.py"][4]
                  and files["a.py"][3] == "", rec.code_edge)
        before = {k: r[6] for k, r in rows.items()}
        write_commit(root, {"a.py": ARM_FILES["a.py"].replace("            return 1", "            return 9")}, "body")
        after = {r[1]: r[6] for r in derive_code_record(root).code_row}
        check_arm("body hash", {k for k in before if before[k] != after[k]} == {"a.py::K", "a.py::K.m", "a.py::K.m.inner"},
                  str([k for k in before if before[k] != after.get(k)]))
        rec = derive_code_record(root)
        dst, names, _x = read_calls(rec, "b.py::g")
        check_arm("import-aware calls", {"a.py::f", "c.py::Base.g", "d.py::D"} == dst and not names, f"{dst} {names}")
        dst, names, _x = read_calls(rec, "b.py::h")
        check_arm("mentions", dst == set() and names == ["f"], f"{dst} {names}")
        check_arm("self", read_calls(rec, "a.py::K.n")[0] == {"a.py::K.m"}, rec.text)
        at = {r[0]: n for n, r in enumerate(rec.edges["rows"]) if r[2] == "module"}
        check_arm("invocation", read_calls(rec, "go.sh")[2] == [at["y.py"]], rec.text)
        check_arm("registry", ("kx", at["tools/kx/v.py"]) in rec.edges["registers"]
                  and ("leg v", at["tools/kx/v.py"]) in rec.edges["registers"], str(rec.edges["registers"]))
        rc, said = run_verb(print_neighbourhood, root, ["a.py"], CODE_RUN_CEILING)
        got = [ln.split(" · ")[1:] for ln in said.splitlines()]
        check_arm("neighbourhood", rc == 0 and [g for g in got if g[-1].endswith(" f") or g[-1] == "def" and g[0] == "function f"]
                  == [["function f", "def"], ["function _p", "caller f"], ["function g", "caller f"],
                      ["module top", "caller f"], ["function test_f", "test f"]]
                  and "return" not in said and "top.py:3-3 · module top · caller f" in said
                  and "a.py:14-15 · function f · callee _p" in said, said)
        check_arm("neighbourhood empty", run_verb(print_neighbourhood, root, ["tools/kx/v.py"], 30.0) == (0, ""))
        check_arm("neighbourhood refusal", run_verb(print_neighbourhood, root, ["none.py"], 30.0)[0] == 2)
        rc, said = run_verb(print_neighbourhood, root, ["tools/kx/w.py"], 30.0)
        check_arm("neighbourhood siblings", said.splitlines() == [
            "tools/kx/w.py:1-2 · function w · def", "tools/kx/kit.toml · sibling", "tools/kx/note.md · sibling",
            "tools/kx/v.py · sibling"], said)

        root = build_repo(top, "amb", {"x/one.sh": "run() {\n  :\n}\n", "y/two.sh": "run() {\n  :\n}\n",
                                       "go.sh": '. "$D/x/one.sh"\n. "$D/y/two.sh"\nrun\n'})
        rec = derive_code_record(root)
        check_arm("ambiguity", "\na\tshell\t1/1\n" in rec.text and "\nc\t" not in rec.text and "\nm\trun\n" in rec.text, rec.text)

        root = build_repo(top, "cold", {"pkg/__init__.py": "", "bad.py": "def f(:\n", "ok.py": "def f():\n    return 1\n",
                                        "ok2.py": "def g():\n    return 1\n"})
        rc, said = run_verb(check_code_record, root, CODE_RUN_CEILING)
        check_arm("cold check", rc == 0 and read_parses(said) == 4 and "s\tbad.py\t" in derive_code_record(root).text, said)
        rc, said = run_verb(check_code_record, root, CODE_RUN_CEILING)
        check_arm("warm check parses nothing", rc == 0 and read_parses(said) == 0, said)
        write_commit(root, {"ok.py": "def f():\n    return 2\n"}, "edit")
        rc, said = run_verb(check_code_record, root, CODE_RUN_CEILING)
        check_arm("one edit parses one blob", rc == 0 and read_parses(said) == 1, said)
        con = ti.load_index(root)
        with con:
            con.execute("UPDATE code_tree SET record = replace(record, 'ok.py', 'no.py')")
        held = con.execute("SELECT COUNT(*) FROM code_tree").fetchone()[0]
        con.close()
        rc, said = run_verb(check_code_record, root, CODE_RUN_CEILING)
        check_arm("stale text", rc == 1 and "differs at line" in said and "no.py" in said and held == 1, said)

        root = build_repo(top, "slow", {"ok.py": "def f():\n    return 1\n"})
        for n in (1, 2):
            rc, said = run_verb(check_code_record, root, 0.0)
            check_arm(f"ceiling run {n}", rc == 2 and "degraded = time ceiling" in said and "floor · git grep" in said, said)
        con = ti.load_index(root)
        con.executescript(TABLES)
        held = con.execute("SELECT (SELECT COUNT(*) FROM code_tree) + (SELECT COUNT(*) FROM code_facts)").fetchone()[0]
        con.close()
        check_arm("degraded is never cached", held == 0, str(held))
        check_arm("degraded neighbourhood", run_verb(print_neighbourhood, root, ["ok.py"], 0.0)[0] == 2)
        rc, said = run_verb(check_code_record, root, CODE_RUN_CEILING)
        check_arm("after the ceiling", rc == 0 and read_parses(said) == 1, said)

        lfs = "version https://git-lfs.github.com/spec/v1\noid sha256:0\nsize 1\n"
        root = build_repo(top, "bound", {
            ".gitattributes": "vendor/** linguist-vendored\ngen.py linguist-generated\n*.bin binary\nlfs/** filter=lfs -text\n",
            "ok.py": "def f():\n    return 1\n", "vendor/v.py": "def vended():\n    return 1\n", "gen.py": "def made():\n    pass\n",
            "b.bin": "\0\1", "lfs/l.py": lfs, "big.py": "x = 1  # pad\n" * 330000, "latin.py": "x = 1\n"})
        (root / "latin.py").write_bytes(b"x = '\xff'\n")
        run_git(root, "add", "latin.py")
        run_git(root, "update-index", "--add", "--cacheinfo", "160000," + "1" * 40 + ",sub")
        run_git(root, "commit", "-q", "-m", "bounds")
        rec = derive_code_record(root)
        check_arm("bounds", "vendor" not in rec.text and "gen.py" not in rec.text and rec.edges["skipped"] == {
            "b.bin": "binary", "lfs/l.py": "lfs", "big.py": f"over {CODE_FILE_CAP} bytes", "latin.py": "binary",
            "sub": "submodule"}, rec.text)

        root = build_repo(top, "tags", {"a.go": "package a\n\nfunc Go() {\n}\n", "ok.py": "def f():\n    return 1\n",
                                        ".governance/policy.toml": "# unset\n"})
        check_arm("builtin reads no go", "a.go" not in derive_code_record(root).text
                  and any(r[0] == "a.go" for r in derive_code_record(root).code_file))
        write_commit(root, {".governance/policy.toml": '[memory]\ncode-languages = "builtin+ctags"\n'}, "ctags")
        path = os.environ["PATH"]
        try:
            os.environ["PATH"] = os.pathsep.join(p for p in path.split(os.pathsep) if not shutil.which("ctags", path=p))
            rc, said = run_verb(check_code_record, root, CODE_RUN_CEILING)
            check_arm("no ctags", rc == 2 and KEY in said, said)
            stub = pathlib.Path(top) / "bin"
            stub.mkdir()
            (stub / "ctags_stub.py").write_text(
                'import sys\nif "--version" in sys.argv:\n    print("Stub Ctags 9.9, a fixture")\nelse:\n'
                '    print(\'{"_type": "tag", "name": "Go", "path": "a.go", "line": 3, "end": 4, "kind": "func"}\')\n',
                encoding="utf-8")
            if os.name == "nt":
                (stub / "ctags.cmd").write_bytes(f'@"{sys.executable}" "{stub / "ctags_stub.py"}" %*\r\n'.encode("utf-8"))
            else:
                (stub / "ctags").write_text(f'#!/bin/sh\nexec "{sys.executable}" "{stub / "ctags_stub.py"}" "$@"\n', encoding="utf-8")
                (stub / "ctags").chmod(0o755)
            os.environ["PATH"] = str(stub) + os.pathsep + os.environ["PATH"]
            rec = derive_code_record(root)
            check_arm("ctags pack", "Stub Ctags 9.9" in rec.text.split("\n")[0] and "a.go::Go" in {r[1] for r in rec.code_row}
                      and "ok.py::f" in {r[1] for r in rec.code_row}, rec.text)
        finally:
            os.environ["PATH"] = path

        root = build_repo(top, "empty", {"note.md": "nothing\n"})
        rc, said = run_verb(check_code_record, root, CODE_RUN_CEILING)
        check_arm("unarmed", rc == 1 and "unarmed" in said, said)
    print(f"FAIL — {len(failed)} code-record arm(s) failed" if failed else "PASS — the code record's arms")
    return 1 if failed else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="code_record.py", description="the core code record of a tree")
    ap.add_argument("verb", nargs="?", choices=("neighbourhood",))
    ap.add_argument("path", nargs="*")
    for flag in ("--check", "--dump", "--time", "--selftest"):
        ap.add_argument(flag, action="store_true")
    ap.add_argument("--fixture", choices=("adopter",))
    ap.add_argument("--tree", default="HEAD")
    ap.add_argument("--ceiling", type=float, default=CODE_RUN_CEILING, help="the run ceiling, in seconds")
    a = ap.parse_args(argv)
    asked = [x for x in (a.verb, a.check, a.dump, a.time, a.selftest, a.fixture) if x]
    if len(asked) != 1 or bool(a.path) != bool(a.verb):
        ap.error("one of --check, --dump, --time, --fixture adopter, --selftest, or neighbourhood <path>...")
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", errors="backslashreplace", newline="\n")
    try:
        root = pathlib.Path(ti.read_git(os.getcwd(), "rev-parse", "--show-toplevel").strip())
        if a.selftest:
            return run_selftest()
        if a.verb:
            return print_neighbourhood(root, a.path, a.ceiling)
        if a.check:
            return check_code_record(root, a.ceiling)
        if a.time:
            return measure_code_record(root, a.tree)
        if a.fixture:
            top = build_code_fixture(root, a.tree)
            print(f"code-record: fixture {top.as_posix()}")
            return measure_code_record(top, "HEAD")
        rec = derive_code_record(root, a.tree, ceiling=a.ceiling)
        if rec.degraded:
            return print_degraded(rec.degraded)
        sys.stdout.write(rec.text)
        return 0
    except (CodeRecordError, ti.TagError, PolicyRefused, OSError) as exc:
        print(f"code-record: refused · {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
