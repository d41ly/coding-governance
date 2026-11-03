"""positional — file:line citations held in the positional population, and the two forms that cannot drift
(PLAY-dOrderedCharter-26).

    python positional.py seed | shrink | check
    python positional.py pin <file> [--at <rev>]
    python positional.py producers [--seed]
    python positional.py --selftest

A file:line citation is `<path>.<ext>:<n>[-<m>]`, `<ext>` in CODE_EXTENSIONS. Every one the tree held at
the seed is a `<citing path>\\t<path>:<n>[-<m>]` row of unit 19's keyed list `positional-refs.txt`
beside this file, keyed by path and reference and never by the citing line; the list's `§n`, `Mn` and
`check n` rows are those `gov_tag.py --list-positional` prints. New text cites one of the stable forms:
a symbol, `path#symbol` as the whole text of a one-backtick span in tracked Markdown, its path's suffix
in SYMBOL_EXTENSIONS, or a blob-pinned line, `<path>@<oid>:<n>[-<m>]`.

`check` is the `positional` arm of `gov_tag.py check`, run alone: the tree against the list both ways,
as `tags.positional` says (`shrink-only`, `refuse` or `report`), every pinned line read against its
blob and every symbol citation against its file's definitions. An unresolved pin or symbol under
`<MEMORY_ROOT>/builds/` is printed and never red: those records are frozen. So is an unlisted file:line
citation in a record there whose adding commit does not descend from `L`, the commit that added this
module (PLAY-dOrderedCharter-47): it was written on a branch that never held the check, and prints
`positional — grandfathered:`. With no `L`, the module staged and not landed, every record is graded.
A record deleted and re-added after `L` is graded from its original add, the oldest the reader keeps,
so a record first added before `L` stays grandfathered. `seed` writes the rows
once and refuses a list already holding a file:line row; `shrink` drops the stale rows and never adds
one; `pin` rewrites a file's unlisted file:line citations to the blob-pinned line at `--at` (HEAD).
`producers` prints every hit of PRODUCER_RE over PRODUCER_PATHSPECS, the directive sources, a render's
hits carried by its `.template.` source (PLAY-dOrderedCharter-48); `--seed` writes `positional-producers.txt`
once, a `<path>\\t<line text>` row per hit naming no stable form. The arm's `producers` limb reds a hit
neither kept nor naming a stable form, and a kept row no hit carries.
Exit 0 green, 1 red, 2 a refusal (a refused policy read, an unreadable list, a git failure).
"""
from __future__ import annotations

import argparse
import ast
import os
import pathlib
import re
import subprocess
import sys

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
sys.path.insert(0, str(KIT_DIR))

import tag_index as ti  # noqa: E402
from policy_value import read_policy_value  # noqa: E402

CODE_EXTENSIONS = ("py", "sh", "js", "mjs", "cjs", "ts", "toml", "json")
SYMBOL_EXTENSIONS = ("py", "sh", "js")
LIST_NAME = "positional-refs.txt"
MODES = ("shrink-only", "refuse", "report")
PATH_CHARS = "A-Za-z0-9_./-"
#: a path character, `@` or `#` may not precede a reference, so a pinned or symbol form never matches
LEAD = rf"(?<![@#{PATH_CHARS}])"
FILE_LINE_RE = re.compile(LEAD + rf"([{PATH_CHARS}]+\.(?:{'|'.join(CODE_EXTENSIONS)})):([0-9]+(?:-[0-9]+)?)")
FILE_LINE_GREP = rf"\.({'|'.join(CODE_EXTENSIONS)}):[0-9]"
PINNED_RE = re.compile(LEAD + rf"([{PATH_CHARS}]+)@([0-9a-f]{{8,40}}):([0-9]+)(?:-([0-9]+))?")
PINNED_GREP = r"@[0-9a-f]{8,40}:[0-9]"
NAME = r"[A-Za-z_][A-Za-z0-9_]*"
SYMBOL_RE = re.compile(rf"([{PATH_CHARS}]+)\.([A-Za-z0-9]+)#({NAME}(?:\.{NAME})?)")
SH_DEF_RE = re.compile(r"^\s*(?:function\s+([A-Za-z_][\w-]*)|([A-Za-z_][\w-]*)\s*\(\s*\))", re.M)
JS_DEF_RE = re.compile(r"\b(?:function\*?\s+|class\s+)([A-Za-z_$][\w$]*)|\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=")
#: PLAY-dOrderedCharter-48: the directive sources a writer reads, and the spellings that tell it to cite a line
PRODUCER_RE = r"file:line|path and line|<path>:<line>"
PRODUCER_PATHSPECS = ("tools/roles/agents/", "tools/workflows/", "skills/", "coding-governance-agents.template.md",
                      "tools/*/SKILL.template.md", "tools/*/*.template.md")
PRODUCERS_NAME = "positional-producers.txt"
#: a producer line naming a stable form, spelled as a placeholder or as a real pin, directs no line citation
STABLE_FORM_RE = re.compile(r"#<?symbol>?|@<(?:oid|sha8?)>:|" + PINNED_RE.pattern)


def read_positional_mode(root, sets=None) -> str:
    """`tags.positional`: `--set`'s value under the fixture, else `root`'s committed policy."""
    sets = sets or {}
    mode = sets["tags.positional"] if "tags.positional" in sets else \
        read_policy_value("tags.positional", root)[0][0]
    if mode not in MODES:
        raise ti.TagError(f"tags.positional is '{mode}', not one of {', '.join(MODES)}")
    return mode


def derive_list_path(root, kit_rel) -> pathlib.Path:
    return pathlib.Path(root) / kit_rel / LIST_NAME


def read_list(path) -> list[str] | None:
    """The list's `<path>\\t<ref>` rows, or None where the file is absent."""
    try:
        text = pathlib.Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    except OSError as exc:
        raise ti.TagError(f"the positional list {pathlib.Path(path).as_posix()} is unreadable: {exc}") from None
    return [ln.rstrip("\r") for ln in text.split("\n") if ln.strip()]


def write_list(path, rows) -> None:
    pathlib.Path(path).write_bytes("".join(f"{r}\n" for r in sorted(set(rows))).encode("utf-8"))


def check_file_line_row(row: str) -> bool:
    return bool(FILE_LINE_RE.fullmatch(row.partition("\t")[2]))


def read_git_grep(root, pattern, kit_rel, paths=(".",), flags=(), numbered=False) -> list[tuple]:
    """(path, line), or (path, n, line) when `numbered`, for every line of a tracked text file in the
    working tree under `paths` matching ERE `pattern`, the positional list left out of its own scan."""
    argv = ["git", "-C", str(root), "grep", "-I", "-n", "-z", *flags, "-E", pattern, "--", *paths,
            f":!{kit_rel}/{LIST_NAME}"]
    try:
        p = subprocess.run(argv, capture_output=True, text=True, encoding="utf-8", errors="replace")
    except OSError as exc:
        raise ti.TagError(f"git grep could not run: {exc}") from None
    if p.returncode > 1:
        raise ti.TagError(f"git grep failed: {(p.stderr or '').strip()[:200]}")
    hits = []
    for rec in p.stdout.split("\n"):
        parts = rec.split("\0", 2)
        if len(parts) == 3:
            hits.append((parts[0], int(parts[1]), parts[2]) if numbered else (parts[0], parts[2]))
    return hits


def read_producers(root, kit_rel) -> list[tuple[str, int, str]]:
    """(path, n, trimmed line) for every hit of PRODUCER_RE over PRODUCER_PATHSPECS, case-insensitive; a
    render's hits are dropped where its `<stem>.template.<ext>` source sits beside it, which carries them."""
    hits = read_git_grep(root, PRODUCER_RE, kit_rel, PRODUCER_PATHSPECS, ("-i",), numbered=True)

    def check_render(path):
        head, dot, ext = path.rpartition(".")
        return bool(dot) and ".template." not in path and (pathlib.Path(root) / f"{head}.template.{ext}").is_file()
    return [(p, n, t.strip()) for p, n, t in hits if not check_render(p)]


def read_producer_rows(path) -> list[str] | None:
    """The kept producer list's `<path>\\t<line text>` rows, its `# ` reason lines left out; None if absent."""
    rows = read_list(path)
    return None if rows is None else [r for r in rows if not r.startswith("#")]


def check_producers(root, kit_rel, mode) -> tuple[list, list, dict]:
    """The `producers` limb: a hit neither kept nor naming a stable form is red, as is a kept row no hit
    carries; under `refuse` a kept hit is red too. -> (findings, lines, counts)."""
    say, rel = "tags: positional · producer", f"{kit_rel}/{PRODUCERS_NAME}"
    rows = read_producer_rows(pathlib.Path(root) / rel)
    kept = set(rows or ())
    hits = read_producers(root, kit_rel)
    carried = {f"{p}\t{t}" for p, _n, t in hits}
    remedy = (f"re-point it to `path#symbol` or a blob-pinned line `<path>@<oid>:<n>`, or keep it with a "
              f"`<path>\\t<line>` row under a `# ` reason in {rel}")
    findings = [f"{say} · {p}:{n} · {t} · {remedy}" for p, n, t in hits
                if f"{p}\t{t}" not in kept and not STABLE_FORM_RE.search(t)]
    unlisted = len(findings)
    findings += [f"{say} stale · {r.replace(chr(9), ' · ')} · no hit carries the row; drop it from {rel}"
                 for r in sorted(kept - carried)]
    if mode == "refuse":
        findings += [f"{say} listed · {p}:{n} · {t} · tags.positional is refuse; {remedy}"
                     for p, n, t in hits if f"{p}\t{t}" in kept]
    lines = [f"{say}s · {len(hits)} hits, {len(kept)} kept rows, {unlisted} unlisted, "
             f"{len(kept - carried)} stale{'' if rows is not None else f'; {rel} is absent, so nothing is kept'}"]
    return findings, lines, {"producers": len(hits), "producers_kept": len(kept), "producers_unlisted": unlisted,
                             "producers_stale": len(kept - carried)}


def run_producers(root, kit_rel, seed=False) -> int:
    """`positional.py producers`: every hit as `<path>:<n>\\t<line>`. `--seed` writes the kept list once, a
    row per hit naming no stable form, and refuses a list already holding a row."""
    hits = read_producers(root, kit_rel)
    if not seed:
        for p, n, t in hits:
            print(f"{p}:{n}\t{t}")
        return 0
    path = pathlib.Path(root) / kit_rel / PRODUCERS_NAME
    held = read_producer_rows(path) or []
    if held:
        print(f"positional: producers seed refused · {kit_rel}/{PRODUCERS_NAME} already holds {len(held)} rows; "
              "the seed runs once, and the list only ever shortens after it")
        return 1
    rows = sorted({f"{p}\t{t}" for p, _n, t in hits if not STABLE_FORM_RE.search(t)})
    head = ("# The producer hits kept: one `<path>\\t<the line's text, trimmed>` row each, keyed by text and never\n"
            "# by line number, a `# ` reason line above each group (PLAY-dOrderedCharter-48).\n")
    path.write_bytes((head + "".join(f"{r}\n" for r in rows)).encode("utf-8"))
    print(f"positional: producers seeded {len(rows)} rows" if rows else
          "positional: producers seeded a header and no row: the query found no hit naming no stable form")
    return 0


def read_file_line_rows(root, kit_rel) -> set[str]:
    """`<citing path>\\t<path>:<n>[-<m>]` for every distinct file:line pair in a tracked text file."""
    return {f"{path}\t{m.group(1)}:{m.group(2)}"
            for path, line in read_git_grep(root, FILE_LINE_GREP, kit_rel) for m in FILE_LINE_RE.finditer(line)}


def read_section_rows(root) -> set[str]:
    """Unit 19's `§n`, `Mn` and `check n` population, through its one predicate."""
    from gov_tag import read_positional
    return set(read_positional(root))


def read_symbol_defs(path: str, text: str) -> set[str]:
    """The symbols a py, sh or js file defines (S4's finder, which unit 49 S45 calls for unit 36's `parser=`
    sources). Python: module- and class-level `def`, `class` and assignment targets, a member written
    `Class.member`, the module-level assignments those `read_py_assigns` returns; shell: `name()` or
    `function name`; JavaScript: `function name`, `class name` or `const|let|var name =`."""
    suffix = path.rsplit(".", 1)[-1]
    if suffix == "py":
        try:
            body = ast.parse(text).body
        except (SyntaxError, ValueError):
            return set()
        names = set(ti.read_py_assigns(text))
        defs = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
        for node in body:
            if not isinstance(node, defs):
                continue
            names.add(node.name)
            for m in node.body if isinstance(node, ast.ClassDef) else ():
                if isinstance(m, defs):
                    names.add(f"{node.name}.{m.name}")
                targets = m.targets if isinstance(m, ast.Assign) else [m.target] if isinstance(m, ast.AnnAssign) else []
                names |= {f"{node.name}.{t.id}" for t in targets if isinstance(t, ast.Name)}
        return names
    if suffix == "sh":
        return {a or b for a, b in SH_DEF_RE.findall(text)}
    if suffix == "js":
        return {a or b for a, b in JS_DEF_RE.findall(text)}
    return set()


def read_symbol_citations(root) -> tuple[list, int]:
    """(path, line, citation, cited path, symbol) for every symbol citation in tracked Markdown: the whole
    text of a one-backtick span outside fences, read by the tag resolver's own span reader, its path's
    suffix in SYMBOL_EXTENSIONS; and how many spans of that shape it passed over at another suffix."""
    out = ti.read_git(root, "ls-files", "-z", "--", "*.md")
    cites, passed = [], 0
    for path in filter(None, out.split("\0")):
        try:
            text = (pathlib.Path(root) / path).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "#" not in text:
            continue
        for n, line in ti.scan_unfenced(text):
            for m in ti.CODE_SPAN_RE.finditer(line):
                s = SYMBOL_RE.fullmatch(m.group(2)) if m.group(1) == "`" else None
                if not s:
                    continue
                if s.group(2) not in SYMBOL_EXTENSIONS:
                    passed += 1
                    continue
                cites.append((path, n, m.group(2), f"{s.group(1)}.{s.group(2)}", s.group(3)))
    return cites, passed


def read_blob_lines(root, oids) -> dict:
    """{object name: line count, or the reason it is no blob} for each `<oid>` or `<oid>:<path>`."""
    names = sorted(set(oids))
    if not names:
        return {}
    git = ["git", "-C", str(root), "cat-file"]
    p = subprocess.run(git + ["--batch-check"], input="".join(f"{n}\n" for n in names).encode("utf-8"),
                       capture_output=True)
    if p.returncode:
        raise ti.TagError(f"git cat-file --batch-check failed: {p.stderr.decode('utf-8', 'replace').strip()[:200]}")
    found, blobs = {}, {}
    for name, rec in zip(names, p.stdout.decode("utf-8", "replace").splitlines()):
        word = rec.split()
        if len(word) == 3 and word[1] == "blob":
            blobs[name] = word[0]
        else:
            found[name] = f"names a {word[1]}, not a blob" if len(word) == 3 else f"is {word[-1]}"
    shas = sorted(set(blobs.values()))
    p = subprocess.run(git + ["--batch"], input="".join(f"{s}\n" for s in shas).encode("ascii"), capture_output=True)
    if p.returncode:
        raise ti.TagError(f"git cat-file --batch failed: {p.stderr.decode('utf-8', 'replace').strip()[:200]}")
    lines, buf, at = {}, p.stdout, 0
    for sha in shas:
        end = buf.index(b"\n", at)
        size = int(buf[at:end].split()[2])
        body = buf[end + 1:end + 1 + size]
        lines[sha] = body.count(b"\n") + (1 if body and not body.endswith(b"\n") else 0)
        at = end + 1 + size + 1
    found.update({name: lines[sha] for name, sha in blobs.items()})
    return found


def check_pins(root, kit_rel, frozen) -> tuple[list, list, int]:
    """Every blob-pinned line against its object: -> (findings red, findings printed, pins read)."""
    pins = [(path, m) for path, line in read_git_grep(root, PINNED_GREP, kit_rel) for m in PINNED_RE.finditer(line)]
    kinds = read_blob_lines(root, {m.group(2) for _p, m in pins})
    commits = {f"{m.group(2)}:{m.group(1)}" for _p, m in pins if kinds.get(m.group(2)) == "names a commit, not a blob"}
    kinds.update(read_blob_lines(root, commits))
    reds, printed = [], []
    for path, m in pins:
        oid, want = m.group(2), int(m.group(4) or m.group(3))
        got = kinds.get(oid)
        if got == "names a commit, not a blob":
            got = kinds.get(f"{oid}:{m.group(1)}")
            got = got if isinstance(got, int) else f"is a commit whose {m.group(1)} is no blob"
        if isinstance(got, int) and want <= got:
            continue
        why = f"holds {got} lines, not line {want}" if isinstance(got, int) else got
        line = f"{path} · {m.group(0)} · {oid} {why}; re-pin it: positional.py pin {path}"
        (printed if path.startswith(frozen) else reds).append(line)
    return reds, printed, len(pins)


def check_symbols(root, frozen) -> tuple[list, list, int, int]:
    """Every symbol citation against its file's definitions: -> (red, printed, read, passed over)."""
    cites, passed = read_symbol_citations(root)
    tracked = set(filter(None, ti.read_git(root, "ls-files", "-z").split("\0"))) if cites else set()
    defs, reds, printed = {}, [], []
    for path, n, cite, target, symbol in cites:
        if target not in defs:
            try:
                text = (pathlib.Path(root) / target).read_text(encoding="utf-8", errors="replace") \
                    if target in tracked else None
            except OSError:
                text = None
            defs[target] = None if text is None else read_symbol_defs(target, text)
        if defs[target] is not None and symbol in defs[target]:
            continue
        why = f"{target} is not tracked" if defs[target] is None else f"{target} defines no {symbol}"
        line = f"{path}:{n} · `{cite}` · {why}"
        (printed if path.startswith(frozen) else reds).append(line)
    return reds, printed, len(cites), passed


def read_grandfathered(root, kit_rel, frozen, paths) -> dict:
    """{path: adding sha} for each of `paths` under `frozen` added by a commit outside the set that holds
    the check: `L`, the oldest add of this module at `kit_rel`, and `git rev-list --ancestry-path L..HEAD`.
    Both adds are read through `tree_lib.read_adding_commits`; no `L` grandfathers nothing."""
    wanted = {p for p in paths if p.startswith(frozen)}
    if not wanted:
        return {}
    tree_lib, _id_grammar = ti.load_memory_tree()
    module = f"{kit_rel}/positional.py"
    try:
        landing = tree_lib.read_adding_commits(root, module, {module}).get(module)
        if not landing:
            return {}
        held = {landing, *tree_lib.read_git_output(
            root, ("rev-list", "--ancestry-path", f"{landing}..HEAD")).decode("utf-8").split()}
        added = tree_lib.read_adding_commits(root, f":(glob){frozen}**", wanted)
    except OSError as exc:
        raise ti.TagError(str(exc)) from None
    return {p: sha for p, sha in added.items() if sha not in held}


def check_positional(root, kit_rel, mode, memory_root) -> tuple[list, list, dict]:
    """The `positional` arm: the tree against the list both ways over both reference kinds, then every pin
    and every symbol citation. -> (reds, the lines it prints, its counts)."""
    say = "tags: positional · "
    rel = f"{kit_rel}/{LIST_NAME}"
    rows = read_list(derive_list_path(root, kit_rel))
    if rows is None:
        return [f"{say}the list {rel} is absent, so no positional population is read"], [], {"absent": True}
    listed = set(rows)
    tree = read_file_line_rows(root, kit_rel) | read_section_rows(root)
    aliases = ti.read_aliases(pathlib.Path(root) / kit_rel / "aliases.toml")
    frozen = f"{memory_root}/builds/"

    def derive_remedy(row):
        path, _, ref = row.partition("\t")
        if FILE_LINE_RE.fullmatch(ref):
            return f"cite `path#symbol` or a blob-pinned line: positional.py pin {path}"
        tag = aliases.get(ref)
        return f"cite `{tag}`, the alias row's tag" if tag else "cite the tag an aliases.toml row maps it to"

    unlisted, grandfathered = sorted(tree - listed), []
    old = read_grandfathered(root, kit_rel, frozen,
                             {r.partition("\t")[0] for r in unlisted if check_file_line_row(r)})
    for r in [r for r in unlisted if check_file_line_row(r) and r.partition("\t")[0] in old]:
        path, _, ref = r.partition("\t")
        grandfathered.append(f"positional — grandfathered: {path} {ref} (added in {old[path][:8]}, before the check)")
        unlisted.remove(r)
    findings = [f"{say}unlisted · {r.replace(chr(9), ' · ')} · {derive_remedy(r)}" for r in unlisted]
    findings += [f"{say}stale · {r.replace(chr(9), ' · ')} · the reference is gone from the tree; "
                 f"positional.py shrink drops the row" for r in sorted(listed - tree)]
    if mode == "refuse":
        findings += [f"{say}listed · {r.replace(chr(9), ' · ')} · tags.positional is refuse; {derive_remedy(r)}"
                     for r in sorted(tree & listed)]
    p_reds, p_printed, pins = check_pins(root, kit_rel, frozen)
    s_reds, s_printed, symbols, passed = check_symbols(root, frozen)
    findings += [f"{say}pin · {x}" for x in p_reds] + [f"{say}symbol · {x}" for x in s_reds]
    w_reds, w_lines, w_counts = check_producers(root, kit_rel, mode)  # PLAY-dOrderedCharter-48: the producers limb
    findings += w_reds
    lines = w_lines + grandfathered + [f"{say}pin, frozen record, printed · {x}" for x in p_printed]
    lines += [f"{say}symbol, frozen record, printed · {x}" for x in s_printed]
    held = sum(1 for r in rows if check_file_line_row(r))
    if not held:
        lines.append(f"{say}unarmed: {rel} holds no file:line row")
    counts = {"mode": mode, "file_line_rows": held, "section_rows": len(rows) - held,
              "unlisted": len(unlisted), "grandfathered": len(grandfathered), "stale": len(listed - tree), "pins": pins,
              "pins_red": len(p_reds), "pins_printed": len(p_printed), "symbols": symbols,
              "symbols_red": len(s_reds), "symbols_printed": len(s_printed), "passed_over": passed, **w_counts}
    lines.append(f"{say}{mode} · {held} file:line and {len(rows) - held} section rows listed, "
                 f"{counts['unlisted']} unlisted, {len(grandfathered)} grandfathered, "
                 f"{counts['stale']} stale; {pins} pins read, {len(p_reds)} red, "
                 f"{len(p_printed)} printed; {symbols} symbol citations read, {len(s_reds)} red, "
                 f"{len(s_printed)} printed, {passed} passed over at another suffix")
    if mode == "report":
        return [], [f"{say}report · {f[len(say):]}" for f in findings] + lines, counts
    return findings, lines, counts


def run_check(root, kit_rel, sets=None) -> int:
    """`positional.py check`: the arm alone, as the `tags` leg runs it inside `gov_tag.py check`."""
    root = pathlib.Path(root)
    _tree_lib, id_grammar = ti.load_memory_tree()
    memory_root = (id_grammar.load_conf(root).get("MEMORY_ROOT") or "memory").strip("/")
    reds, lines, _counts = check_positional(root, kit_rel, read_positional_mode(root, sets), memory_root)
    for line in lines + reds:
        print(line)
    print(f"tags: positional · {'RED' if reds else 'green'} · {len(reds)} red")
    return 1 if reds else 0


def run_seed(root, kit_rel) -> int:
    """S2's one-time seed: every file:line pair in the tree, and every row `--list-positional` prints that
    the list lacks. Refused once the list holds a file:line row."""
    path = derive_list_path(root, kit_rel)
    rows = read_list(path) or []
    held = [r for r in rows if check_file_line_row(r)]
    if held:
        print(f"positional: seed refused · {path.name} already holds {len(held)} file:line rows, "
              f"{', '.join(r.replace(chr(9), ' ') for r in held[:3])}{' …' if len(held) > 3 else ''}; "
              "the seed runs once, and `shrink` takes rows out")
        return 1
    fl = read_file_line_rows(root, kit_rel)
    joined = read_section_rows(root) - set(rows)
    write_list(path, set(rows) | fl | joined)
    print(f"positional: seeded {len(fl)} file:line rows, and joined {len(joined)} section rows the list lacked")
    return 0


def run_shrink(root, kit_rel) -> int:
    """Drop every row whose reference is gone from the tree; the list only ever shortens."""
    path = derive_list_path(root, kit_rel)
    rows = read_list(path)
    if rows is None:
        print(f"positional: shrink refused · {path.name} is absent", file=sys.stderr)
        return 2
    tree = read_file_line_rows(root, kit_rel) | read_section_rows(root)
    keep = [r for r in rows if r in tree]
    write_list(path, keep)
    print(f"positional: shrink dropped {len(rows) - len(keep)} stale rows, {len(set(keep))} remain")
    return 0


def run_pin(root, kit_rel, file, rev="HEAD") -> int:
    """S5: rewrite each unlisted file:line citation in `file` to `<path>@<oid>:<n>[-<m>]`, `<oid>` the
    blob at `rev`; a citation whose path is no blob at `rev` is refused and left, and a `file` outside
    the repository is refused with nothing written."""
    root = pathlib.Path(os.path.realpath(root))
    target = pathlib.Path(os.path.realpath(file))
    if root not in target.parents or not target.is_file():
        print(f"positional: pin refused · {pathlib.Path(file).as_posix()} is no file inside {root.as_posix()}")
        return 1
    rel = target.relative_to(root).as_posix()
    listed = {r.partition("\t")[2] for r in read_list(derive_list_path(root, kit_rel)) or [] if r.startswith(rel + "\t")}
    oids, refused, done = {}, [], []

    def read_oid(path):
        if path not in oids:
            p = subprocess.run(["git", "-C", str(root), "cat-file", "-t", f"{rev}:{path}"], capture_output=True, text=True)
            q = subprocess.run(["git", "-C", str(root), "rev-parse", "--verify", "--quiet", "--short=8", f"{rev}:{path}"],
                               capture_output=True, text=True)
            oids[path] = q.stdout.strip() if p.stdout.strip() == "blob" and not q.returncode else None
        return oids[path]

    def derive_pin(m):
        ref = f"{m.group(1)}:{m.group(2)}"
        if ref in listed:
            return m.group(0)
        oid = read_oid(m.group(1))
        if not oid:
            refused.append(ref)
            return m.group(0)
        done.append(f"{ref} -> {m.group(1)}@{oid}:{m.group(2)}")
        return f"{m.group(1)}@{oid}:{m.group(2)}"
    try:
        text = target.read_bytes().decode("utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"positional: pin refused · {rel} is unreadable as UTF-8: {exc}")
        return 1
    new = FILE_LINE_RE.sub(derive_pin, text)
    if new != text:
        target.write_bytes(new.encode("utf-8"))
    for d in done:
        print(f"positional: pin {rel} · {d}")
    for r in refused:
        print(f"positional: pin refused · {rel} · {r} · its path is no blob at {rev}")
    return 1 if refused else 0


# ------------------------------------------------------------------------------------------ the selftest

#: `<plant and flags>|<exit>|<a line it must print>`: each row reads `gov_tag.py --fixture --plant <row>`'s
#: run. `{code}` is the fixture's code file and `{x}` the forked-before plant's, so this file holds no
#: file:line citation and no pinned line.
SELFTEST_ROWS = """\
none|0|tags: positional · unarmed
positional-seed|0|seed: the list holds every expected row and no other
positional-seed|0|a second seed: rc=1
positional-new|1|tags: positional · unlisted · memory/guides/ALPHA.md · {code}:2 · cite `path#symbol`
positional-new|1|tags: positional · unlisted · memory/guides/ALPHA.md · BUILD-METHOD M9 · cite
positional-new|1|without the plants: rc=0
positional-new --set tags.positional=report|0|tags: positional · report · unlisted · memory/guides/ALPHA.md · BUILD-METHOD M9
positional-new --set tags.positional=report|0|tags: positional · report · unlisted · memory/guides/ALPHA.md · {code}:2
positional-stale|0|removed: rc=1, stale named
positional-stale|0|after shrink: 1 rows, rc=0
positional-stale|0|a new citation planted: shrink left 1 rows, rc=1
positional-listed|0|tags: green · 0 red
positional-listed --set tags.positional=refuse|1|tags: positional · listed · memory/guides/ALPHA.md · {code}:1
positional-symbol|1|tags: positional · symbol · memory/guides/ALPHA.md:17 · `tools/corekit/mod.py#ghost` · tools/corekit/mod.py defines no ghost
positional-symbol|1|symbol, frozen record, printed · memory/builds/x/record.md:1 · `tools/corekit/mod.py#ghost`
positional-symbol|1|8 symbol citations read, 1 red, 1 printed, 1 passed over at another suffix
positional-symbol|1|without the live ghost: rc=0
positional-pinned|1|tags: positional · pin · memory/guides/ALPHA.md · {code}@00000000:1 · 00000000 is missing
positional-pinned|1|holds 3 lines, not line 9
positional-pinned|1|pin, frozen record, printed · memory/builds/x/record.md · {code}@00000000:1
positional-pinned|1|without the live bad pins: rc=0
positional-pin|0|pin rewrote the citation to the blob at HEAD; check: rc=0
positional-pin|0|pin outside the repository: rc=1, nothing written
positional-forked-before|0|positional — grandfathered: memory/builds/x/build/record.md {x}:1 (added in
positional-forked-before|0|tags: positional · unlisted · memory/builds/x/build/after.md · {x}:2
positional-forked-before|0|tags: positional · unlisted · tools/notes.md · {x}:1
positional-forked-before|0|the pre-fork record: rc=0; a record after the merge: rc=1; the pre-fork record moved under tools: rc=1
positional-producer-new|1|tags: positional · producer · tools/roles/agents/gov-x.agent.md:3 · - cite it by file:line · re-point it
positional-producer-new|1|re-pointed to a stable form: rc=0
positional-producer-stale|0|tags: positional · producer stale · tools/roles/agents/gov-x.agent.md · - cite it by file:line · no hit
positional-producer-stale|0|kept: rc=0; a second seed: rc=1; the kept line re-pointed: rc=1
"""


def run_selftest() -> int:
    """The `tags positional selftest` leg: every positional plant, red and green, each row's exit and line."""
    failed, runs = 0, {}
    rows = [r.replace("{code}", "tools/corekit/code.py").replace("{x}", "x.py").split("|")
            for r in SELFTEST_ROWS.splitlines() if r.strip()]
    for plant, rc, want in rows:
        if plant not in runs:  # one run per plant and flags, read by each of its rows
            runs[plant] = subprocess.run([sys.executable, str(KIT_DIR / "gov_tag.py"), "--fixture", "--plant",
                                          *plant.split()], capture_output=True, text=True, encoding="utf-8",
                                         errors="replace")
        p = runs[plant]
        out = p.stdout + p.stderr
        if p.returncode == int(rc) and want in out:
            print(f"arm ok    positional plant {plant}")
            continue
        failed += 1
        print(f"arm FAIL  positional plant {plant} — wanted rc={rc} + {want}, got rc={p.returncode}")
        print("".join(f"      {ln}\n" for ln in out.splitlines()), end="")
    if failed:
        print(f"FAIL — {failed} of {len(rows)} positional plant rows failed")
        return 1
    print(f"PASS — the positional plants, {len(rows)} rows")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="positional.py", description="the positional population and its stable forms")
    ap.add_argument("verb", nargs="?", choices=("seed", "shrink", "pin", "check", "producers"))
    ap.add_argument("file", nargs="?")
    ap.add_argument("--at", default="HEAD")
    ap.add_argument("--seed", action="store_true", help="producers: write the kept list once")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return run_selftest()
    if not a.verb:
        ap.error("a verb, or --selftest")
    from gov_tag import derive_kit_rel, resolve_repo_root
    from policy_value import PolicyRefused
    try:
        root = resolve_repo_root()
        kit_rel = derive_kit_rel(root)
        if a.verb == "pin":
            if not a.file:
                ap.error("pin takes <file>")
            return run_pin(root, kit_rel, a.file, a.at)
        if a.verb == "producers":
            return run_producers(root, kit_rel, a.seed)
        return {"seed": run_seed, "shrink": run_shrink, "check": run_check}[a.verb](root, kit_rel)
    except PolicyRefused as exc:
        print(f"tags: refused · {exc.key} · {exc.line}", file=sys.stderr)
        return 2
    except ti.TagError as exc:
        print(f"tags: refused · {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
