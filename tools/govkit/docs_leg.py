#!/usr/bin/env python3
"""docs_leg — the `docs` leg: each user-facing member's declared usage fingerprinted against the page
under `help/` that documents it, under the policy key `help.enforce` (TOOL-dSafePassage-13).

    python <prefix>/govkit/docs_leg.py                                          # the `docs` leg
    python <prefix>/govkit/docs_leg.py --list [--undocumented]                  # every row and its page
    python <prefix>/govkit/docs_leg.py --fixture --plant <case> [--enforce refuse|warn|off]

THE ROWS. `usage.toml` beside this file holds one `[[class]]` row per class of the step gate's class
registry (`surface-classes.toml`): its `usage` shape (`verb`, `key`, `hook`, `leg`, `page` or
`none`), its `rows` and a `why`. `rows` is where the class's usage rows come from: a reader spelled
`<path under the tool root>:<function>` returning each member's row from the registry that already
states it, or `usage.toml`, its `[[usage]]` rows. A `page` or `none` class carries no `rows`. A
`[[usage]]` row also declares a `script:<path>[#<verb>]` a page shows that no class holds.

THE ANCHOR. A row's fingerprint is the first eight hex of the SHA-256 of its shape fields (the row
less its `id`) as canonical JSON. A page documents a member with `<!-- usage: <id> <fp8> -->`, a
`page`-shaped member with `<!-- usage: <id> -->`. Each shaped member is anchored on exactly one page
or listed in `memory/project/docs-undocumented.txt`, a shrink-only list whose row count may not rise
above its first-parent low-water, read by drift-audit's `derive_low_waters`.

THE COMMANDS. Each line of a fenced `bash`, `sh` or `console` block, and each inline code span opening
`python`, `python3` or `bash`, is tested against the `verb` rows: its verb declared, each `--flag` a
declared flag of that verb. A command naming no tracked entrypoint is counted and not tested. Each
relative link outside a fence resolves to a tracked path, its `#fragment` to a heading or an anchor.

THE MODE. `help.enforce`, read once through govkit's `read_policy_value` at the landed revision:
`refuse` exits 1 on any finding, `warn` prints each as a WARN line and exits 0, `off` prints one
line and reads nothing else. `--enforce` is honoured under `--fixture` only.

WHAT IT DOES NOT CHECK. Prose: an anchor whose fingerprint is current over a wrong paragraph passes.
It runs no page command and fetches no external link. The `file` and `installable` classes carry
no usage shape, and an `agent` or `entry` member is graded for presence only.

Exit 0 green, 1 a finding under `refuse`, 2 not a verdict: a shaped class with no member, pages whose
commands none was tested, an unreadable declaration or a reader that will not load, no policy kit
or a refused `help.enforce` read.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import pathlib
import posixpath
import re
import shlex
import shutil
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import govkit as gk  # noqa: E402  the deployer beside this file, its policy reader called once
import step_gate as sg  # noqa: E402  the one population, its class rows and its loaders

Refusal = gk.Refusal
USAGE_FILE = "usage.toml"
LIST_REL = "memory/project/docs-undocumented.txt"
MODES = ("refuse", "warn", "off")
SHAPES = ("verb", "key", "hook", "leg", "page", "none")
FIELDED = ("verb", "key", "hook", "leg")
CLASS_KEYS = ("class", "usage", "rows", "why")
USAGE_KEYS = ("id", "shape", "entry", "verb", "flags", "values", "default")
ANCHOR_RE = re.compile(r"<!--\s*usage:\s*(?P<id>.+?)(?:\s+(?P<fp>[0-9a-f]{8}))?\s*-->")
FENCE_RE = re.compile(r"^\s*(```+|~~~+)\s*([\w-]*)")
INLINE_RE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$")
EXPLICIT_RE = re.compile(r"<a\s+(?:id|name)=\"([^\"]+)\"")
FLAG_RE = re.compile(r"(--[A-Za-z0-9][\w-]*)(=?)(\s+(?:<[^>]*>|[^\s\[\]|()<>]+=[^\s\[\]|()]+))?")
COMMAND_LANGS = ("bash", "sh", "console")
INTERPRETERS = ("python", "python3", "bash", "sh")
PLANTS = ("none", "stale-page", "bad-flag", "bad-verb", "unrowed", "broken-link", "broken-fragment",
          "external-link", "undocumented", "drained-row", "grown-list", "orphan-anchor", "restated-row",
          "reader-rows", "none-rows", "leg-row", "unclassed", "empty-class", "untested",
          "console-prompt", "continued-flag", "unbalanced-quote", "comment-apostrophe")


def derive_usage_fingerprint(row: dict) -> str:
    """The first eight hex of the SHA-256 of `row` less its `id`, as canonical JSON."""
    fields = {k: v for k, v in row.items() if k != "id"}
    return hashlib.sha256(json.dumps(fields, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()[:8]


# ------------------------------------------------------------------------------- the row readers
def read_hook_usage(root) -> dict:
    """Each tracked hook fragment's `name` -> its `event` and `matcher`."""
    root = pathlib.Path(root)
    out = {}
    for rel in filter(None, sg.run_git_text(root, "ls-files", "-z", "--", "*.fragment.json").stdout.split("\0")):
        if not (root / rel).is_file():
            continue
        try:
            d = json.loads((root / rel).read_text(encoding="utf-8"))
        except ValueError as e:
            raise Refusal(f"{rel}: not JSON: {e}") from None
        if isinstance(d, dict) and isinstance(d.get("name"), str) and d["name"]:
            out[d["name"]] = {"shape": "hook", "event": d.get("event"), "matcher": d.get("matcher")}
    return out


def read_policy_usage(root) -> dict:
    """Each `[[key]]` row of the policy catalogue -> its `allowed` values and its `default`."""
    p = gk.resolve_tool_path(root, "policy", "catalogue.toml")
    if not p.is_file():
        return {}
    return {k["name"]: {"shape": "key", "values": k.get("allowed"), "default": k.get("default")}
            for k in gk.load_toml(p).get("key", []) if isinstance(k, dict) and isinstance(k.get("name"), str)}


def read_verb_usage(root) -> dict:
    """Each `<cli>:<verb>` of step_gate's `VERB_SOURCES` -> its entry, its verb and the `--` flags its
    usage line states, a flag followed by `<...>` or `x=y` spelled with a trailing `=` as taking a
    value. A line continues onto the next lines indented past it that open `[` or `-`; two lines
    naming one verb join."""
    root = pathlib.Path(root)
    out: dict = {}
    for cli, parts, block, line_re in sg.VERB_SOURCES:
        p = gk.resolve_tool_path(root, *parts)
        if not p.is_file():
            continue
        text = p.read_text(encoding="utf-8")
        if block:
            m = re.search(block, text, re.S | re.M)
            text = m[1] if m else ""
        entry = p.relative_to(root).as_posix()
        lines = text.splitlines()
        for n, ln in enumerate(lines):
            m = re.match(line_re, ln)
            if not m:
                continue
            usage = ln[m.end():]
            for cont in lines[n + 1:]:
                body = cont[1:] if ln.startswith("#") and cont.startswith("#") else cont
                if re.match(r"\s{6,}[\[-]", body) and not re.match(line_re, cont):
                    usage += " " + body
                else:
                    break
            usage = re.split(r"\s{2,}#\s", usage)[0]
            row = out.setdefault(f"{cli}:{m[1]}", {"shape": "verb", "entry": entry, "verb": m[1], "flags": []})
            flags = set(row["flags"])
            for name, eq, val in FLAG_RE.findall(usage):
                if eq or val or name + "=" in flags:
                    flags.discard(name)
                    flags.add(name + "=")
                else:
                    flags.add(name)
            row["flags"] = sorted(flags)
    return out


def read_leg_usage(root) -> dict:
    """Each row of the leg manifest -> its `name` and its `argv`."""
    p = gk.resolve_tool_path(root, "gate-legs.json")
    try:
        legs = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise Refusal(f"{p.name}: unreadable: {e}") from None
    return {r["name"]: {"shape": "leg", "name": r["name"], "argv": r.get("argv")}
            for r in legs if isinstance(r, dict) and isinstance(r.get("name"), str)}


# ------------------------------------------------------------------------------- the declaration
def read_usage_classes(root, class_ids: list[str]) -> tuple[list[dict], list[str]]:
    """(the `[[class]]` rows of `usage.toml`, the findings joining them to the registry's ids).
    An unreadable file, an unknown key or shape is a refusal; a registered class with no row, a row
    naming no registered class, a shaped class with no `rows` or a `page`/`none` one carrying them
    is a finding."""
    path = gk.resolve_tool_path(root, gk.GOVKIT_DIR.name, USAGE_FILE)
    data = gk.load_toml(path)
    out, found, seen = [], [], set()
    for n, row in enumerate(data.get("class", []) or [], 1):
        at = f"{USAGE_FILE} [[class]] row {n}"
        if not isinstance(row, dict) or not isinstance(row.get("class"), str):
            raise Refusal(f"{at}: needs a `class`")
        bad = [k for k in row if k not in CLASS_KEYS]
        if bad or row.get("usage") not in SHAPES:
            raise Refusal(f"{at} ({row['class']}): " + (f"key {bad[0]} is not a class key" if bad else
                          f"usage '{row.get('usage')}' is not one of {', '.join(SHAPES)}"))
        cid, shape = row["class"], row["usage"]
        seen.add(cid)
        if cid not in class_ids:
            found.append(f"CLASS {cid}: a [[class]] row of {USAGE_FILE} naming no registered class")
        if shape in FIELDED and not row.get("rows"):
            found.append(f"CLASS {cid}: usage {shape} with no `rows`, so its members have no row")
        if shape not in FIELDED and "rows" in row:
            found.append(f"CLASS {cid}: usage {shape} carries `rows`, and a {shape} class has none")
        out.append({"class": cid, "usage": shape, "rows": row.get("rows")})
    for cid in class_ids:
        if cid not in seen:
            found.append(f"CLASS {cid}: a registered class with no [[class]] row in {USAGE_FILE}")
    return out, found


def read_usage_rows(root, classes: list[dict], population: set[str]) -> tuple[dict, list[str]]:
    """(every row by id, the findings): each class's rows from its `rows` reader, then each
    `[[usage]]` row; a `[[usage]]` row a reader already returns, or naming no member of a
    `usage.toml` class and no `script:`, is a finding."""
    rows: dict = {}
    for c in classes:
        if c["usage"] in FIELDED and c["rows"] and c["rows"] != USAGE_FILE:
            fn = sg.load_class_callable(root, "{prefix}/" + c["rows"], f"{USAGE_FILE} class {c['class']} key rows")
            got = fn(pathlib.Path(root))
            if not isinstance(got, dict):
                raise Refusal(f"{USAGE_FILE} class {c['class']}: its rows reader returned no table")
            rows |= {f"{c['class']}:{name}": dict(r) for name, r in got.items()}
    by_toml = {c["class"] for c in classes if c["rows"] == USAGE_FILE}
    found = []
    path = gk.resolve_tool_path(root, gk.GOVKIT_DIR.name, USAGE_FILE)
    for n, row in enumerate(gk.load_toml(path).get("usage", []) or [], 1):
        if not isinstance(row, dict) or not isinstance(row.get("id"), str):
            raise Refusal(f"{USAGE_FILE} [[usage]] row {n}: needs an `id`")
        bad = [k for k in row if k not in USAGE_KEYS]
        if bad or row.get("shape") not in FIELDED:
            raise Refusal(f"{USAGE_FILE} [[usage]] {row['id']}: " + (f"key {bad[0]} is not a usage key" if bad
                          else f"shape '{row.get('shape')}' is not one of {', '.join(FIELDED)}"))
        rid = row["id"]
        if rid in rows:
            found.append(f"RESTATED {rid}: a [[usage]] row restating what its class's own registry states")
            continue
        if not rid.startswith("script:") and not (rid.split(":", 1)[0] in by_toml and rid in population):
            found.append(f"ORPHAN {USAGE_FILE} [[usage]] {rid}: names no member of a usage.toml class and no script")
            continue
        rows[rid] = {k: v for k, v in row.items() if k != "id"}
    return rows, found


# ----------------------------------------------------------------------------------- the pages
def read_page_lines(text: str):
    """Yields (line number, line, the language of the fence it sits in or None outside one)."""
    fence, lang = None, None
    for n, ln in enumerate(text.splitlines(), 1):
        m = FENCE_RE.match(ln)
        if m and (fence is None or m[1][0] == fence[0] and len(m[1]) >= len(fence)):
            fence, lang = (m[1], (m[2] or "").lower()) if fence is None else (None, None)
            continue
        yield n, ln, lang if fence else None


def read_page_anchors(page, rel: str) -> list[tuple]:
    """(page, line, id, fingerprint or None) for each usage anchor outside a fence."""
    return [(rel, n, m["id"].strip(), m["fp"]) for n, ln, lang in read_page_lines(page.read_text(encoding="utf-8"))
            if lang is None for m in ANCHOR_RE.finditer(ln)]


def read_page_commands(page) -> list[tuple]:
    """(line, [token, ...]) for each segment of each command the page shows: a fenced `bash`, `sh` or
    `console` line, or an inline span opening `python`, `python3` or `bash`. Segments split on `|`,
    `&&` and `;`; a leading `NAME=value` and a `...` token are set aside, a `#` word ends the line.

    TOOL-dSafePassage-26 S36: in a `console` fence only a `$ ` or `> ` line is a command, its prompt
    stripped, and a line a trailing backslash continues joins it unprompted; in a `bash` or `sh`
    fence a comment goes through the shell grammar's own reading, `shlex`'s `#`, so an apostrophe in
    it splits nothing. A line that grammar cannot split is (line, None), a finding the caller names."""
    out, pending = [], ""
    for n, ln, lang in read_page_lines(page.read_text(encoding="utf-8")):
        cmds = []
        if lang in COMMAND_LANGS:
            body = ln.strip()
            if lang == "console" and not pending:
                body = body[2:] if body.startswith(("$ ", "> ")) else ""
            if body.endswith("\\"):
                pending += body[:-1] + " "
                continue
            body, pending = pending + body, ""
            if body and not body.startswith("#"):
                cmds.append(body)
        elif lang is None:
            cmds = [s for s in INLINE_RE.findall(ln) if s.split(" ", 1)[0] in ("python", "python3", "bash")]
        for body in cmds:
            lex = shlex.shlex(body, posix=True, punctuation_chars=";&|")
            lex.whitespace_split = True
            if lang not in ("bash", "sh"):
                lex.commenters = ""
            try:
                toks = list(lex)
            except ValueError:
                out.append((n, None))
                continue
            seg: list = []
            for t in [*toks, ";"]:
                comment = t.startswith("#")
                if comment or t in (";", "&&", "|", "||", "&"):
                    while seg and re.fullmatch(r"[A-Za-z_]\w*=.*", seg[0]):
                        seg.pop(0)
                    if seg:
                        out.append((n, seg))
                    seg = []
                    if comment:
                        break
                elif t != "...":
                    seg.append(t)
    return out


def check_page_command(cmd: list[str], rows_by_entry: dict, tracked: set[str]) -> tuple[str, str]:
    """(verdict, what): `tested`, `skipped` (no tracked entrypoint), `unrowed` (the entrypoint) or
    `red` naming the undeclared verb or flag."""
    i = 1 if cmd[0] in INTERPRETERS else 0
    if i and (len(cmd) < 2 or cmd[1].startswith("-")):
        return "skipped", cmd[0]
    entry = re.sub(r"^(<prefix>|\{prefix\})/", "tools/", cmd[i])
    entry = posixpath.normpath(entry[2:] if entry.startswith("./") else entry)
    if entry not in tracked:
        return "skipped", cmd[i]
    verbs = rows_by_entry.get(entry)
    if verbs is None:
        return "unrowed", entry
    args = cmd[i + 1:]
    if None in verbs and (not args or args[0] not in verbs):
        verb = None
    elif args and args[0] in verbs:
        verb, args = args[0], args[1:]
    else:
        return "red", f"verb '{args[0] if args else ''}' is not a declared verb of {entry} ({' '.join(sorted(v for v in verbs if v))})"
    flags = verbs[verb]
    k = 0
    while k < len(args):
        a = args[k]
        k += 1
        if not a.startswith("--") or a == "--":
            continue
        name, eq, _v = a.partition("=")
        if name + "=" in flags:
            k += 0 if eq else 1
        elif name not in flags or eq:
            return "red", f"flag '{name}' is not a declared flag of {entry}{' ' + verb if verb else ''}"
    return "tested", entry


def derive_heading_slugs(text: str) -> set[str]:
    """Each heading's GitHub slug, a repeat suffixed `-1`, `-2`, and each explicit `<a id>`."""
    slugs, seen = set(), {}
    for _n, ln, lang in read_page_lines(text):
        if lang is not None:
            continue
        slugs |= set(EXPLICIT_RE.findall(ln))
        m = HEADING_RE.match(ln)
        if m:
            s = re.sub(r"[^\w\- ]", "", m[1].lower()).replace(" ", "-")
            slugs.add(s if s not in seen else f"{s}-{seen[s]}")
            seen[s] = seen.get(s, 0) + 1
    return slugs


def check_page_links(root, page, rel: str, tracked: set[str]) -> tuple[int, int, list[str]]:
    """(links checked, external links counted, findings) for `page`, outside its fences."""
    checked, external, found = 0, 0, []
    for n, ln, lang in read_page_lines(page.read_text(encoding="utf-8")):
        if lang is not None:
            continue
        for target in LINK_RE.findall(re.sub(r"`[^`\n]*`", "", ln)):
            if re.match(r"(https?|mailto):", target):
                external += 1
                continue
            checked += 1
            path, _h, frag = target.partition("#")
            dest = posixpath.normpath(posixpath.join(posixpath.dirname(rel), path)) if path else rel
            if dest not in tracked and not any(t.startswith(dest.rstrip("/") + "/") for t in tracked):
                found.append(f"LINK {rel}:{n} {target}: {dest} is no tracked path")
            elif frag and dest.endswith(".md") and dest in tracked and \
                    frag not in derive_heading_slugs((pathlib.Path(root) / dest).read_text(encoding="utf-8")):
                found.append(f"FRAGMENT {rel}:{n} {target}: #{frag} is no heading or anchor of {dest}")
    return checked, external, found


# ----------------------------------------------------------------------------------- the list
def read_legacy_rows(root) -> list[str]:
    """The ids of the shrink-only list, one `<id>\\t<reason>` row each, `#` lines comments."""
    p = pathlib.Path(root) / LIST_REL
    if not p.is_file():
        raise Refusal(f"{LIST_REL}: absent, so the undocumented members have no list")
    return [ln.split("\t", 1)[0].strip() for ln in p.read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.strip().startswith("#")]


def check_legacy_low_water(root, count: int) -> tuple[int | None, list[str]]:
    """(the list's first-parent low-water, a finding where `count` rises above it), through
    drift-audit's `derive_low_waters`, loaded by path from this install; no history is no finding."""
    path = HERE.parent / "drift-audit" / "drift_report.py"
    try:
        spec = importlib.util.spec_from_file_location("docs_leg_drift_report", path)
        dr = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(dr)
    except Exception as e:  # any failure to load is "will not load", named
        raise Refusal(f"{path.name} will not load: {type(e).__name__}: {e}") from None
    low = dr.derive_low_waters(dr.Git(pathlib.Path(root), "HEAD"), [LIST_REL])[LIST_REL]
    if low is not None and count > low:
        return low, [f"GROWN {LIST_REL}: {count} rows, above its low-water {low}; the list only shrinks"]
    return low, []


# ------------------------------------------------------------------------------------ the leg
def read_docs_state(root, class_ids: list[str], population: set[str]) -> dict:
    """Everything the leg and `--list` read, with the findings and the non-verdict states."""
    root = pathlib.Path(root)
    classes, found = read_usage_classes(root, class_ids)
    shape_of = {c["class"]: c["usage"] for c in classes}
    rows, more = read_usage_rows(root, classes, population)
    found += more
    states = [f"class {c} has usage {s} and no member, so it grades nothing" for c, s in shape_of.items()
              if s != "none" and c in class_ids and not any(m.split(":", 1)[0] == c for m in population)]
    tracked = set(filter(None, sg.run_git_text(root, "ls-files", "-z").stdout.split("\0")))
    pages = sorted(p for p in (root / "help").rglob("*.md")) if (root / "help").is_dir() else []
    anchors = [a for p in pages for a in read_page_anchors(p, p.relative_to(root).as_posix())]
    graded = {m for m in population if shape_of.get(m.split(":", 1)[0]) not in (None, "none")}
    graded |= {r for r in rows if r.startswith("script:")}
    at: dict = {}
    for rel, n, aid, fp in anchors:
        at.setdefault(aid, []).append(f"{rel}:{n}")
        shape = "verb" if aid.startswith("script:") else shape_of.get(aid.split(":", 1)[0])
        if aid not in graded or (shape in FIELDED and aid not in rows):
            found.append(f"ORPHAN {rel}:{n} usage anchor {aid}: names no member or row")
        elif shape == "page" and fp:
            found.append(f"STALE {rel}:{n} {aid}: a page member's anchor carries a fingerprint, {fp}")
        elif shape in FIELDED and fp != (now := derive_usage_fingerprint(rows[aid])):
            found.append(f"STALE {rel}:{n} {aid}: the page holds {fp or 'no fingerprint'}, the row is now {now}")
    for aid, where in sorted(at.items()):
        if len(where) > 1 and aid in graded:
            found.append(f"TWICE {aid}: anchored on {len(where)} places, {', '.join(where)}; one page documents it")
    listed = read_legacy_rows(root)
    script_paths = {f"script:{t}" for t in tracked}
    for rid in listed:
        if rid in at and rid in graded:
            found.append(f"DRAINED {LIST_REL} row {rid}: anchored at {at[rid][0]}, so its row leaves the list")
        elif rid not in graded and rid not in script_paths:
            found.append(f"ORPHAN {LIST_REL} row {rid}: names no member, row or tracked script")
    for m in sorted(graded - set(at) - set(listed)):
        found.append(f"UNDOCUMENTED {m}: anchored on no page under help/ and not on {LIST_REL}")
    low, more = check_legacy_low_water(root, len(listed))
    found += more
    by_entry: dict = {}
    for rid, r in rows.items():
        if r.get("shape") == "verb" and r.get("entry"):
            by_entry.setdefault(r["entry"], {})[r.get("verb")] = set(r.get("flags") or [])
    counts = {"tested": 0, "skipped": 0, "unrowed": 0, "checked": 0, "external": 0}
    for p in pages:
        rel = p.relative_to(root).as_posix()
        for n, cmd in read_page_commands(p):
            if cmd is None:
                found.append(f"SPLIT {rel}:{n}: a command line the shell grammar cannot split, so no "
                             f"verb or flag on it was tested")
                continue
            verdict, what = check_page_command(cmd, by_entry, tracked)
            counts["tested" if verdict == "tested" else verdict if verdict != "red" else "tested"] += 1
            if verdict == "red":
                found.append(f"COMMAND {rel}:{n} {' '.join(cmd)}: {what}")
            elif verdict == "unrowed" and f"script:{what}" not in listed and \
                    not any(x.startswith(f"script:{what}#") for x in listed):
                found.append(f"UNROWED {rel}:{n} {what}: a tracked entrypoint with no [[usage]] row and no list row")
        c, e, more = check_page_links(root, p, rel, tracked)
        counts["checked"] += c
        counts["external"] += e
        found += more
    if counts["tested"] + counts["skipped"] + counts["unrowed"] and not counts["tested"]:
        states.append("the pages show commands and no page command was tested against a row")
    return {"classes": classes, "rows": rows, "anchors": at, "listed": listed, "low": low, "found": found,
            "states": states, "counts": counts, "graded": graded, "pages": len(pages),
            "stale": sum(f.startswith("STALE ") for f in found), "shape_of": shape_of}


def check_docs(root, class_ids: list[str], population: set[str], mode: str, source: str) -> int:
    """The leg: one mode line, one summary, one line per finding; exit as `mode` says."""
    print(f"docs: help.enforce = {mode} · {source}")
    if mode == "off":
        return 0
    s = read_docs_state(root, class_ids, population)
    c = s["counts"]
    print(f"docs: {len(s['classes'])} classes · {len(population)} members · {len(s['rows'])} rows · "
          f"{sum(len(v) for v in s['anchors'].values())} anchors on {s['pages']} pages · {s['stale']} stale · "
          f"commands {c['tested']} tested, {c['skipped']} skipped, {c['unrowed']} unrowed · "
          f"links {c['checked']} checked, {c['external']} external · "
          f"list {len(s['listed'])} rows, low-water {s['low'] if s['low'] is not None else 'none yet'}")
    for st in s["states"]:
        print(f"docs: REFUSED · {st}")
    for f in s["found"]:
        print(f"docs: {'WARN ' if mode == 'warn' else ''}{f}")
    return 2 if s["states"] else 1 if s["found"] and mode == "refuse" else 0


# -------------------------------------------------------------------------------- the fixture
FIXTURE_USAGE = '''[[class]]
class = "fx-verb"
usage = "verb"
rows = "usage.toml"
why = "a fixture verb"

[[class]]
class = "fx-key"
usage = "key"
rows = "usage.toml"
why = "a fixture key"

[[class]]
class = "fx-hook"
usage = "hook"
rows = "govkit/docs_leg.py:read_hook_usage"
why = "a fixture hook, its usage in its fragment"

[[class]]
class = "fx-leg"
usage = "leg"
rows = "govkit/docs_leg.py:read_leg_usage"
why = "a fixture leg, its usage in the manifest"

[[class]]
class = "fx-page"
usage = "page"
why = "presence only"

[[class]]
class = "fx-none"
usage = "none"
why = "no usage"

[[usage]]
id = "fx-verb:tool"
shape = "verb"
entry = "tools/fx/tool.py"
verb = "render"
flags = ["--role="]

[[usage]]
id = "fx-key:FX_ROOT"
shape = "key"
values = "a repo-relative directory"
default = "memory"

[[usage]]
id = "script:tools/fx/run.py#go"
shape = "verb"
entry = "tools/fx/run.py"
verb = "go"
flags = ["--part=", "--quiet"]
'''
FIXTURE_POPULATION = {"fx-verb:tool", "fx-key:FX_ROOT", "fx-hook:fx-hook", "fx-leg:fx-leg", "fx-page:guide",
                      "fx-none:blob"}
FIXTURE_MOD_ROW = {"shape": "key", "values": "a or b", "default": "a"}


def build_docs_fixture(tmp, plant: str) -> tuple[pathlib.Path, list[str], set[str]]:
    """A scratch git repository under `tmp` with `plant` staged on it: (its root, the class ids, the
    population), the class list and the population held in memory as the plants compose them."""
    if plant not in PLANTS:
        raise Refusal(f"no fixture plant '{plant}': the plants are {', '.join(PLANTS)}")
    root, hooks = pathlib.Path(tmp) / "r", pathlib.Path(tmp) / "h"
    hooks.mkdir(parents=True)
    files = {
        "tools/govkit/registry.toml": "# the fixture's tool root\n",
        "tools/govkit/usage.toml": FIXTURE_USAGE,
        "tools/hooks/fx-hook.fragment.json": json.dumps({"name": "fx-hook", "event": "Stop", "matcher": "*"}) + "\n",
        "tools/gate-legs.json": json.dumps([{"name": "fx-leg", "argv": ["python", "{prefix}/fx/run.py", "go"]}]) + "\n",
        "tools/fx/run.py": "", "tools/fx/tool.py": "", "tools/fx/other.py": "",
        LIST_REL: "# the fixture's undocumented members\nfx-page:guide\tseed\nfx-key:FX_ROOT\tseed\n",
    }
    for rel, text in files.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text, encoding="utf-8", newline="\n")
    shutil.copyfile(__file__, root / "tools/govkit/docs_leg.py")
    sg.run_git_text(root, "init", "-q")
    sg.run_git_text(root, "add", "-A")
    rows = read_usage_rows(root, read_usage_classes(root, [])[0], FIXTURE_POPULATION)[0]
    fp ={k: derive_usage_fingerprint(v) for k, v in rows.items()}
    pages = {
        "help/guide.md": (f"# Guide\n\n## Running it\n\n<!-- usage: script:tools/fx/run.py#go {fp['script:tools/fx/run.py#go']} -->\n"
                          "```bash\npython tools/fx/run.py go --part task\nsort -k1 notes.txt\n```\n\n"
                          f"Render with `python tools/fx/tool.py render --role builder`. "
                          f"<!-- usage: fx-verb:tool {fp['fx-verb:tool']} -->\n\n"
                          "See [more](more.md#the-hook) and [running](#running-it).\n"),
        "help/more.md": ("# More\n\n## The hook\n\n"
                         f"<!-- usage: fx-hook:fx-hook {fp['fx-hook:fx-hook']} -->\n"
                         f"<!-- usage: fx-leg:fx-leg {fp['fx-leg:fx-leg']} -->\n"
                         f"<!-- usage: fx-key:FX_ROOT {fp['fx-key:FX_ROOT']} -->\n\n"
                         "```text\n[not graded](absent.md) <!-- usage: fx-none:nothing 00000000 -->\n```\n"),
    }
    for rel, text in pages.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text, encoding="utf-8", newline="\n")
    sg.run_git_text(root, "add", "-A")
    sg.write_fixture_commit(root, hooks, "docs fixture: the seed")
    (root / LIST_REL).write_text("# the fixture's undocumented members\nfx-page:guide\tseed\n", encoding="utf-8", newline="\n")
    sg.run_git_text(root, "add", "-A")
    sg.write_fixture_commit(root, hooks, "docs fixture: fx-key documented, its row drained")
    class_ids = ["fx-verb", "fx-key", "fx-hook", "fx-leg", "fx-page", "fx-none"]
    population = set(FIXTURE_POPULATION)

    def edit(rel: str, old: str, new: str) -> None:
        p = root / rel
        text = p.read_text(encoding="utf-8")
        if old not in text:
            raise Refusal(f"the {plant} plant found no '{old}' in {rel}")
        p.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")

    usage, guide, more = "tools/govkit/usage.toml", "help/guide.md", "help/more.md"
    if plant == "stale-page":
        edit(usage, 'flags = ["--role="]', 'flags = ["--role=", "--dry-run"]')
    elif plant == "bad-flag":
        edit(guide, "--part task", "--section task")
    elif plant == "bad-verb":
        edit(guide, "tool.py render", "tool.py rendr")
    elif plant == "unrowed":
        edit(guide, "sort -k1", "python tools/fx/other.py --fast\nsort -k1")
    elif plant == "broken-link":
        edit(guide, "See [more]", "See [gone](gone.md), [more]")
    elif plant == "broken-fragment":
        edit(guide, "more.md#the-hook", "more.md#no-such-heading")
    elif plant == "external-link":
        edit(guide, "See [more]", "See [the site](https://example.invalid/x), [more]")
    elif plant == "undocumented":
        edit(LIST_REL, "fx-page:guide\tseed\n", "")
    elif plant == "drained-row":
        edit(more, "## The hook\n", "## The hook\n\n<!-- usage: fx-page:guide -->\n")
    elif plant == "grown-list":
        population.add("fx-page:extra")
        edit(LIST_REL, "fx-page:guide\tseed\n", "fx-page:guide\tseed\nfx-page:extra\tlater\n")
        sg.run_git_text(root, "add", "-A")
        sg.write_fixture_commit(root, hooks, "docs fixture: a row added")
    elif plant == "orphan-anchor":
        edit(more, "## The hook\n", "## The hook\n\n<!-- usage: fx-key:NOPE 0badf00d -->\n")
    elif plant == "restated-row":
        edit(usage, "[[usage]]\n", '[[usage]]\nid = "fx-hook:fx-hook"\nshape = "hook"\n\n[[usage]]\n')
    elif plant == "reader-rows":
        (root / "tools/fx/rows.py").write_text(
            f"def read_fx_rows(root):\n    return {{'thing': {dict(FIXTURE_MOD_ROW, default='b')!r}}}\n",
            encoding="utf-8", newline="\n")
        edit(usage, "[[usage]]\n", '[[class]]\nclass = "fx-mod"\nusage = "key"\nrows = "fx/rows.py:read_fx_rows"\n'
                                   'why = "a reader in a fixture module"\n\n[[usage]]\n')
        edit(more, "## The hook\n", f"## The hook\n\n<!-- usage: fx-mod:thing {derive_usage_fingerprint(FIXTURE_MOD_ROW)} -->\n")
        class_ids.append("fx-mod")
        population.add("fx-mod:thing")
    elif plant == "none-rows":
        edit(usage, 'usage = "none"\n', 'usage = "none"\nrows = "usage.toml"\n')
    elif plant == "leg-row":
        edit("tools/gate-legs.json", '"go"', '"go", "--quiet"')
    elif plant == "unclassed":
        class_ids.append("fx-extra")
    elif plant == "empty-class":
        population.discard("fx-key:FX_ROOT")
    elif plant in ("console-prompt", "continued-flag", "unbalanced-quote", "comment-apostrophe"):
        # TOOL-dSafePassage-26 S36: a `> ` prompt and a continued console line each carry a flag
        # the row does not declare; an unbalanced quote cannot split; an apostrophe in a comment is
        # no quote, the control that exits 0.
        edit(guide, "```bash\npython tools/fx/run.py go --part task\n", {
            "console-prompt": "```console\n> python tools/fx/run.py go --section task\n```\n\n```bash\n",
            "continued-flag": "```console\n$ python tools/fx/run.py go \\\n    --section task\n```\n\n```bash\n",
            "unbalanced-quote": "```bash\npython tools/fx/run.py go --part \"task\n",
            "comment-apostrophe": "```bash\npython tools/fx/run.py go --part task  # don't\n",
        }[plant])
    elif plant == "untested":
        text = (root / usage).read_text(encoding="utf-8")
        (root / usage).write_text(text[:text.index("[[usage]]\nid = \"fx-verb:tool\"")] +
                                  text[text.index("[[usage]]\nid = \"fx-key:FX_ROOT\""):text.index(
                                      "[[usage]]\nid = \"script:")], encoding="utf-8", newline="\n")
        for rel in (guide,):
            (root / rel).write_text(re.sub(r"<!-- usage: [^>]* -->", "", (root / rel).read_text(encoding="utf-8")),
                                    encoding="utf-8", newline="\n")
        edit(LIST_REL, "fx-page:guide\tseed\n", "fx-page:guide\tseed\nfx-verb:tool\tuntested\n"
             "script:tools/fx/run.py\tuntested\nscript:tools/fx/tool.py\tuntested\n")
    sg.run_git_text(root, "add", "-A")
    return root, class_ids, population


def run_docs_fixture(plant: str, mode: str) -> int:
    """The leg over the fixture with `plant` staged, under `mode`; `off` builds nothing."""
    if mode == "off":
        return check_docs(None, [], set(), mode, "--enforce")
    # The fixture's git must address its own repository: a GIT_DIR or GIT_INDEX_FILE a hook exported
    # would point every `git -C <fixture>` at the caller's repository instead.
    for k in [k for k in os.environ if k.startswith("GIT_")]:
        del os.environ[k]
    tmp =pathlib.Path(tempfile.mkdtemp(prefix="docs-"))
    try:
        root, class_ids, population = build_docs_fixture(tmp, plant)
        print(f"docs: fixture · plant {plant}")
        return check_docs(root, class_ids, population, mode, "--enforce" if mode != "refuse" else "the fixture's default")
    finally:
        sg.remove_scratch_tree(tmp)


def main(argv: list[str]) -> int:
    root = gk.repo_root()
    try:
        if argv[:2] == ["--fixture", "--plant"] and (len(argv) == 3 or (len(argv) == 5 and argv[3] == "--enforce")):
            mode = argv[4] if len(argv) == 5 else "refuse"
            if mode not in MODES:
                raise Refusal(f"--enforce '{mode}' is not one of {', '.join(MODES)}")
            return run_docs_fixture(argv[2], mode)
        if argv in (["--list"], ["--list", "--undocumented"]):
            classes = sg.read_surface_classes(root)
            s = read_docs_state(root, [c["id"] for c in classes], sg.read_surface_population(root, classes))
            for i in sorted(s["graded"]):
                if len(argv) == 2:
                    if i not in s["anchors"]:
                        print(i)
                    continue
                r = s["rows"].get(i, {})
                fields = " · ".join(f"{k} {' '.join(map(str, v)) if isinstance(v, list) else v}"
                                    for k, v in sorted(r.items()) if k != "shape")
                shape = r.get("shape") or s["shape_of"].get(i.split(":", 1)[0])
                where = ", ".join(s["anchors"].get(i, [])) or ("listed" if i in s["listed"] else "undocumented")
                print(f"docs: {i} · {shape}{' · ' + fields if fields else ''} · {where}")
            return 0
        if not argv:
            try:
                value, source, reason = gk.read_policy_value("help.enforce", root)
            except LookupError as e:
                print(f"docs: REFUSED · no policy kit, so help.enforce cannot be read: {e}")
                return 2
            if value not in MODES:
                print(f"docs: REFUSED · help.enforce reads '{value}', not one of {', '.join(MODES)}")
                return 2
            classes = sg.read_surface_classes(root)
            return check_docs(root, [c["id"] for c in classes], sg.read_surface_population(root, classes),
                              value, f"{source} · {reason}")
        sys.stderr.write("usage: python docs_leg.py | --list [--undocumented] | "
                         "--fixture --plant <case> [--enforce refuse|warn|off]\n")
        return 2
    except Refusal as e:
        print(f"docs: REFUSED · {e}")
        return 2


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    raise SystemExit(main(sys.argv[1:]))
