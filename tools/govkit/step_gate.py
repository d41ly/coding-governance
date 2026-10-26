#!/usr/bin/env python3
"""step_gate — the step gate: the adopter-visible surface population diffed between a landing's
base and its tip (TOOL-dSafePassage-10).

    python <prefix>/govkit/step_gate.py [--base <rev>]                      # the `step-gate` leg
    python <prefix>/govkit/step_gate.py --list                              # each class, counted at the tip
    python <prefix>/govkit/step_gate.py --print-base [--base <rev>]         # the base the leg grades from
    python <prefix>/govkit/step_gate.py --fixture --plant <case> [--with-row]   # the gate, observed

THE POPULATION. `surface-classes.toml` beside this file declares one `[[class]]` row per class of
adopter-visible member: its `id`, its `reader` and its `plant`, each `<path under the tool root>:
<function>` spelled through `{prefix}`, a `summary`, and an optional `witness`, a reader of the
class's own change record. A member is `<class>:<name>`, split on its first colon; a path-valued name
spells the tool root as `{prefix}`, so one id names one member at every install prefix. The readers,
the plants and the witnesses are loaded from the TIP's tree and run over both sides, so one predicate
grades the base and the tip and a class joining in the range is never red for its own arrival.

THE BASE is govkit's `resolve_landing_base`, the one `epoch` grades from: `--base`, else a non-zero
`GATE_PUSH_BASE`, else the merge-base with the default branch. The base side is read in a detached
worktree at that commit, sparse past `memory/` (no class reads it), removed in a `finally`.

THE VERDICT. Every member present at the base and absent at the tip is a vanish. It is witnessed when
an `[[upgrade]]` row (the descriptors and `steps.toml`) or a `[[retired]]` row (the registry) at the
tip names it in `surfaces`, read through `upgrade_steps.py`, or when its class's own witness names
it. Each unwitnessed vanish prints a RED line. A content-only edit moves no member and needs no row.

WHAT IT DOES NOT CHECK. A change of meaning behind an unchanged name. Whether a step's up carries the
member it names (the `upgrade-walk` leg's question). Any member no class reader sees: a conf key a kit
reads and never declares in `[config]`, a verb of a CLI no `VERB_SOURCES` row names, an agent or a
Skill an adopter wrote for itself. A wider reader joins by changing its class row.

Exit 0 green, 1 a vanished member no row names, 2 a refusal: a class empty at the tip, a malformed
class row, a reader or plant that will not load, a base or a base worktree that will not resolve.
"""

from __future__ import annotations

import functools
import importlib.util
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib

HERE = pathlib.Path(__file__).resolve().parent
if __name__ == "__main__":
    sys.modules.setdefault("step_gate", sys.modules[__name__])
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import govkit as gk  # noqa: E402  the deployer beside this file, whose readers every class reuses

Refusal = gk.Refusal
CLASSES_FILE = "surface-classes.toml"
CLASS_KEYS = ("id", "reader", "plant", "witness", "summary")
CLASS_ID_RE = re.compile(r"[a-z][a-z0-9-]*")
SKILL_RE = re.compile(r"\.claude/skills/([^/]+)/SKILL\.md")
RED_RE = re.compile(r"^step-gate: RED (.+?) vanished with no ", re.M)
SPARSE_PATTERNS = "/*\n!/memory/\n"
# The declared usage texts the `verb` class reads: (cli, its file under the tool root, the span of
# that file that is the usage text or None for the whole file, the line naming one verb).
VERB_SOURCES = (
    ("govkit.py", ("govkit", "govkit.py"), r'^USAGE = """(.*?)"""', r"^  govkit\.py (\S+)"),
    ("unattended.sh", ("unattended", "unattended.sh"), None, r"^#   unattended[.]sh (\S+)"),
)
# The fixture's own cases beside each class row's plant: S4's and S5's registry shapes.
FIXTURE_CLASS = "sg-fixture"
FIXTURE_MARK = "sg-fixture.txt"
REGISTRY_PLANTS = ("empty-class", "no-plant", "own-record", "own-record-unnamed")
_MODULES: dict[pathlib.Path, object] = {}


def run_git_text(root, *args: str) -> subprocess.CompletedProcess:
    """`git -C <root> <args>`, text in UTF-8, never raising on a non-zero exit."""
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def derive_member_path(path, tr: str) -> str:
    """`path` spelled as a member name: under the tool root `tr`, with `{prefix}` in its place."""
    path = str(path)
    return "{prefix}/" + path[len(tr) + 1:] if tr and path.startswith(tr + "/") else path


def load_class_callable(root, spelled, at: str):
    """The function a class row's `<path>:<function>` names, loaded from `root`'s tree; a refusal
    naming `at` where the spelling is malformed or the module or function will not load."""
    path_s, _sep, fn = str(spelled).rpartition(":")
    if not path_s or not fn:
        raise Refusal(f"{at}: '{spelled}' is not `<path>:<function>`")
    path = (pathlib.Path(root) / gk.resolve_prefix_token(path_s, gk.derive_tool_root(root))).resolve()
    mod = _MODULES.get(path)
    if mod is None:
        if path == pathlib.Path(__file__).resolve():
            mod = sys.modules[__name__]
        else:
            try:
                spec = importlib.util.spec_from_file_location(f"step_gate_class_{len(_MODULES)}", path)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
            except Exception as e:  # any failure to import is "will not load", named
                raise Refusal(f"{at}: '{spelled}' will not load: {type(e).__name__}: {e}") from None
        _MODULES[path] = mod
    f = getattr(mod, fn, None)
    if not callable(f):
        raise Refusal(f"{at}: '{spelled}' names no function {fn}")
    return f


def read_surface_classes(root) -> list[dict]:
    """The class rows of `root`'s registry, validated, each reader, plant and witness loaded from
    `root`. Denies by default: an unknown key, a missing `id`, `reader` or `plant`, a malformed or
    duplicate id, an empty registry, and anything that will not load are refusals naming the row."""
    path = gk.resolve_tool_path(root, gk.GOVKIT_DIR.name, CLASSES_FILE)
    rel = path.relative_to(root).as_posix()
    rows = gk.load_toml(path).get("class", [])
    if not isinstance(rows, list) or not rows:
        raise Refusal(f"{rel}: no `[[class]]` row, so the gate would grade nothing")
    out, seen = [], set()
    for n, row in enumerate(rows, 1):
        at = f"{rel} [[class]] row {n}" + (f" (id {row.get('id')})" if isinstance(row, dict) else "")
        if not isinstance(row, dict):
            raise Refusal(f"{at}: not a table")
        for k in row:
            if k not in CLASS_KEYS:
                raise Refusal(f"{at} key {k}: not a class key ({', '.join(CLASS_KEYS)})")
        for k in ("id", "reader", "plant"):
            if not isinstance(row.get(k), str) or not row[k]:
                raise Refusal(f"{at} key {k}: required, and this row has none")
        cid = row["id"]
        if not CLASS_ID_RE.fullmatch(cid):
            raise Refusal(f"{at} key id: '{cid}' is not [a-z][a-z0-9-]*, a member's class half")
        if cid in seen:
            raise Refusal(f"{at} key id: '{cid}' is declared twice")
        seen.add(cid)
        out.append({"id": cid, "summary": str(row.get("summary", "")),
                    "reader": load_class_callable(root, row["reader"], f"{at} key reader"),
                    "plant": load_class_callable(root, row["plant"], f"{at} key plant"),
                    "witness": load_class_callable(root, row["witness"], f"{at} key witness")
                    if row.get("witness") else None})
    return out


def read_surface_population(root, classes: list[dict]) -> set[str]:
    """Every member over one tree, `<class>:<name>`: each class row's reader run over `root`."""
    root = pathlib.Path(root)
    return {f"{c['id']}:{name}" for c in classes for name in c["reader"](root)}


def write_sparse_checkout(tree, sha: str) -> None:
    """Check `tree` out at `sha` past `memory/`, the sparse pattern set for this one command so no
    config of the repository it belongs to moves."""
    tree = pathlib.Path(tree)
    out = pathlib.Path(run_git_text(tree, "rev-parse", "--git-path", "info/sparse-checkout").stdout.strip())
    sp = out if out.is_absolute() else tree / out
    sp.parent.mkdir(parents=True, exist_ok=True)
    sp.write_text(SPARSE_PATTERNS, encoding="utf-8", newline="\n")
    p = run_git_text(tree, "-c", "core.sparseCheckout=true", "-c", "core.sparseCheckoutCone=false",
                     "reset", "-q", "--hard", sha)
    if p.returncode != 0:
        raise Refusal(f"cannot check {tree.as_posix()} out at {sha[:8]}: {p.stderr.strip()}")


def rmtree_writable(path) -> None:
    """`path` removed, a read-only file (git's objects on Windows) made writable first."""
    def chmod_retry(func, p, _exc):
        os.chmod(p, 0o700)
        func(p)
    shutil.rmtree(path, onexc=chmod_retry)


def read_base_population(root, sha: str, classes: list[dict]) -> set[str]:
    """The population at the commit `sha`: the tip's readers over a detached sparse worktree there."""
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="sgb-"))
    tree = tmp / "b"
    try:
        p = run_git_text(root, "worktree", "add", "-q", "--detach", "--no-checkout", str(tree), sha)
        if p.returncode != 0:
            raise Refusal(f"the base worktree at {sha[:8]} will not add: {p.stderr.strip()}")
        write_sparse_checkout(tree, sha)
        return read_surface_population(tree, classes)
    finally:
        run_git_text(root, "worktree", "remove", "--force", str(tree))
        if tmp.exists():
            rmtree_writable(tmp)
        run_git_text(root, "worktree", "prune")


def read_witnessed_members(root, classes: list[dict]) -> set[str]:
    """Every member a row at the tip witnesses: each `surfaces` value of every `[[upgrade]]` and
    `[[retired]]` row, through TOOL-dSafePassage-1's reader, and each class's own-record names."""
    us = gk.upgrade_steps
    names = {s for r in us.read_steps(root, None, None) for s in r.surfaces}
    names |= {s for r in us.read_retired(root, None, None) for s in r.surfaces}
    for c in classes:
        if c["witness"]:
            names |= {f"{c['id']}:{n}" for n in c["witness"](pathlib.Path(root))}
    return names


def derive_vanished_members(base_pop: set[str], tip_pop: set[str]) -> list[str]:
    """The members present at the base and absent at the tip, sorted."""
    return sorted(base_pop - tip_pop)


def check_step_gate(root, base: str | None) -> int:
    """The leg: exit 1 naming each vanished member no row witnesses, 2 on a refusal, else 0."""
    root = pathlib.Path(root)
    sha, boundary, why = gk.resolve_landing_base(root, base)
    if not sha:
        print(f"step-gate: REFUSED · no base to compare against{why}")
        return 2
    how = "--base" if base is not None else "GATE_PUSH_BASE" if boundary else "merge-base with the default branch"
    print(f"step-gate: base {sha[:8]} ({how}) · tip the working tree")
    classes = read_surface_classes(root)
    tip = read_surface_population(root, classes)
    counts = {c["id"]: 0 for c in classes}
    for m in tip:
        counts[m.split(":", 1)[0]] += 1
    empty = [c for c, n in counts.items() if not n]
    if empty:
        for c in empty:
            print(f"step-gate: REFUSED · class {c} is empty at the tip, and a green over an empty class grades nothing")
        return 2
    vanished = derive_vanished_members(read_base_population(root, sha, classes), tip)
    witnessed = read_witnessed_members(root, classes)
    red = [m for m in vanished if m not in witnessed]
    print(f"step-gate: {len(classes)} classes · {len(tip)} members at the tip · {len(vanished)} vanished · "
          f"{len(vanished) - len(red)} witnessed")
    for m in red:
        print(f"step-gate: RED {m} vanished with no [[upgrade]] or [[retired]] row naming it in surfaces")
    return 1 if red else 0


# ---------------------------------------------------------------------------- the class readers
@functools.lru_cache(maxsize=None)
def read_shipped_survivors(root) -> tuple:
    """((entry, survivor row), ...) for every descriptor survivor with a source in a role an adopter
    receives, as `govkit.py shipped --epoch` reads them. ponytail: cached per tree for one process,
    which reads each tree once; a caller must not mutate the rows."""
    root = pathlib.Path(root)
    return tuple((eid, row) for eid, (d, _p) in sorted(gk.read_shipped_descriptors(root).items())
                 for row in gk.resolve_entry(root, d, gk.canonical_ctx(eid))["survivors"]
                 if row.get("src") and row["role"] in gk.EPOCH_ROLES)


def read_file_members(root) -> set[str]:
    """Each `files` row's path in gov's source-mode receipt; none where the tree carries no such receipt."""
    p = pathlib.Path(root) / ".governance" / "install.json"
    if not p.is_file():
        return set()
    try:
        rec = json.loads(p.read_text(encoding="utf-8"))
    except ValueError as e:
        raise Refusal(f".governance/install.json is not JSON: {e}") from None
    if not isinstance(rec, dict) or rec.get("mode") != "source":
        return set()
    tr = gk.derive_tool_root(root)
    return {derive_member_path(r["path"], tr) for r in rec.get("files") or []
            if isinstance(r, dict) and isinstance(r.get("path"), str) and r["path"]}


def read_installable_members(root) -> set[str]:
    """Each destination a shipped survivor resolves to under the canonical context."""
    tr = gk.derive_tool_root(root)
    return {derive_member_path(row["dest"], tr) for _e, row in read_shipped_survivors(pathlib.Path(root))}


def read_hook_members(root) -> set[str]:
    """Each tracked hook fragment's `name`, the population the deployer wires."""
    root = pathlib.Path(root)
    names = set()
    for rel in filter(None, run_git_text(root, "ls-files", "-z", "--", "*.fragment.json").stdout.split("\0")):
        if not (root / rel).is_file():
            continue
        try:
            d = json.loads((root / rel).read_text(encoding="utf-8"))
        except ValueError as e:
            raise Refusal(f"{rel}: not JSON: {e}") from None
        if isinstance(d, dict) and isinstance(d.get("name"), str) and d["name"]:
            names.add(d["name"])
    return names


def read_command_members(root) -> set[str]:
    """Each `<name>` of a survivor destination shaped `.claude/skills/<name>/SKILL.md`."""
    return {m[1] for _e, row in read_shipped_survivors(pathlib.Path(root)) if (m := SKILL_RE.fullmatch(row["dest"]))}


def read_agent_members(root) -> set[str]:
    """Each `<name>` of a tracked `<name>.agent.md` in the roles kit's agents, never a rendered copy."""
    root = pathlib.Path(root)
    rel = gk.resolve_tool_path(root, "roles", "agents").relative_to(root).as_posix()
    return {pathlib.PurePosixPath(p).name[:-len(".agent.md")]
            for p in run_git_text(root, "ls-files", "-z", "--", f"{rel}/*.agent.md").stdout.split("\0")
            if p and (root / p).is_file()}


def read_conf_members(root) -> set[str]:
    """Each `<conf file>#<KEY>` a descriptor's `[config]` declares required or defaulted."""
    out = set()
    for _eid, (d, _p) in gk.read_shipped_descriptors(pathlib.Path(root)).items():
        cfg = d.get("config") or {}
        f = str(cfg.get("file") or "").strip()
        if f:
            out |= {f"{f}#{k}" for k in (*(cfg.get("required_keys_gate") or []),
                                         *(cfg.get("required_keys_render") or []), *(cfg.get("defaults") or {}))}
    return out


def read_policy_members(root) -> set[str]:
    """Each `[[key]]` row's `name` in the policy schema catalogue under `root`, so each side reads its own."""
    p = gk.resolve_tool_path(root, "policy", "catalogue.toml")
    if not p.is_file():
        return set()
    return {k["name"] for k in gk.load_toml(p).get("key", [])
            if isinstance(k, dict) and isinstance(k.get("name"), str) and k["name"]}


def read_verb_members(root) -> set[str]:
    """Each `<cli>:<verb>` a declared usage source in `VERB_SOURCES` states."""
    out = set()
    for cli, parts, block, line in VERB_SOURCES:
        p = gk.resolve_tool_path(root, *parts)
        if not p.is_file():
            continue
        text = p.read_text(encoding="utf-8")
        if block:
            m = re.search(block, text, re.S | re.M)
            text = m[1] if m else ""
        out |= {f"{cli}:{v}" for v in re.findall(line, text, re.M)}
    return out


def read_entry_members(root) -> set[str]:
    """Each registry `[[entry]]` row's id."""
    return {e["id"] for e in gk.load_registry(root).get("entry", []) or []
            if isinstance(e, dict) and isinstance(e.get("id"), str) and e["id"]}


def read_fixture_members(root) -> set[str]:
    """The fixture class's members: `kept`, and `gone` only where the plant's mark is absent."""
    return {"kept"} | (set() if (pathlib.Path(root) / FIXTURE_MARK).is_file() else {"gone"})


def read_fixture_successors(root) -> set[str]:
    """The names the fixture class's own record, its mark, gives a successor; none where it is absent."""
    p = pathlib.Path(root) / FIXTURE_MARK
    return set(p.read_text(encoding="utf-8").split()) if p.is_file() else set()


# ----------------------------------------------------------------------------------- the plants
def write_plant_edit(clone, rel: str, edit) -> None:
    """`rel` in the clone rewritten by `edit` over its text, its bytes otherwise kept, and staged."""
    p = pathlib.Path(clone) / rel
    text = p.read_bytes().decode("utf-8")
    new = edit(text)
    if new == text:
        raise Refusal(f"the plant changed nothing in {rel}")
    p.write_bytes(new.encode("utf-8"))
    run_git_text(clone, "add", "--", rel)


def run_git_staged(clone, *args: str) -> None:
    """A staging git command in the clone (`mv`, `rm`), refused where git refuses it."""
    p = run_git_text(clone, *args)
    if p.returncode != 0:
        raise Refusal(f"git {' '.join(args)} refused in the fixture clone: {p.stderr.strip()}")


def write_file_plant(clone) -> str:
    """Removes the first `.md` files row from the clone's source receipt."""
    clone = pathlib.Path(clone)
    rel = ".governance/install.json"
    rec = json.loads((clone / rel).read_text(encoding="utf-8")) if (clone / rel).is_file() else {}
    rows = sorted((r["path"] for r in rec.get("files") or [] if isinstance(r, dict)
                   and str(r.get("path", "")).endswith(".md")) if rec.get("mode") == "source" else [])
    if not rows:
        raise Refusal("the file plant needs a source receipt with a `.md` files row, and the clone carries none")
    rec["files"] = [r for r in rec["files"] if not (isinstance(r, dict) and r.get("path") == rows[0])]
    write_plant_edit(clone, rel, lambda _t: json.dumps(rec, indent=2) + "\n")
    return "file:" + derive_member_path(rows[0], gk.derive_tool_root(clone))


def write_installable_plant(clone) -> str:
    """Renames one installed file: a kit README its `**` engine rule lands where it sits."""
    clone = pathlib.Path(clone)
    srcs = sorted(row["src"] for _e, row in read_shipped_survivors(clone)
                  if row["role"] == "engine" and row["src"] == row["dest"] and row["src"].endswith("/README.md"))
    if not srcs:
        raise Refusal("the installable plant found no kit README its engine rule lands in place")
    run_git_staged(clone, "mv", srcs[0], srcs[0][:-len(".md")] + "-moved.md")
    return "installable:" + derive_member_path(srcs[0], gk.derive_tool_root(clone))


def write_hook_plant(clone) -> str:
    """Renames one hook fragment's `name`."""
    clone = pathlib.Path(clone)
    rels = sorted(filter(None, run_git_text(clone, "ls-files", "-z", "--", "*.fragment.json").stdout.split("\0")))
    if not rels:
        raise Refusal("the hook plant found no tracked hook fragment")
    name = json.loads((clone / rels[0]).read_text(encoding="utf-8"))["name"]
    write_plant_edit(clone, rels[0], lambda t: re.sub(r'("name"\s*:\s*)' + re.escape(json.dumps(name)),
                                                      lambda m: m[1] + json.dumps(name + "-moved"), t, count=1))
    return f"hook:{name}"


def write_command_plant(clone) -> str:
    """Renames one Skill destination in the descriptor that declares it."""
    clone = pathlib.Path(clone)
    for _eid, (d, dpath) in sorted(gk.read_shipped_descriptors(clone).items()):
        for rule in d.get("files") or []:
            m = SKILL_RE.fullmatch(str(rule.get("to", "")))
            if m:
                to = json.dumps(m[0])
                write_plant_edit(clone, dpath, lambda t: t.replace(
                    to, json.dumps(f".claude/skills/{m[1]}-moved/SKILL.md"), 1))
                return f"command:{m[1]}"
    raise Refusal("the command plant found no descriptor rule landing a Skill")


def write_agent_plant(clone) -> str:
    """Renames one tracked agent file of the roles kit."""
    clone = pathlib.Path(clone)
    names = sorted(read_agent_members(clone))
    if not names:
        raise Refusal("the agent plant found no tracked agent file")
    rel = gk.resolve_tool_path(clone, "roles", "agents").relative_to(clone).as_posix()
    run_git_staged(clone, "mv", f"{rel}/{names[0]}.agent.md", f"{rel}/{names[0]}-moved.agent.md")
    return f"agent:{names[0]}"


def write_conf_plant(clone) -> str:
    """Drops one required conf key no other descriptor declares for that conf file."""
    clone = pathlib.Path(clone)
    descs = sorted(gk.read_shipped_descriptors(clone).items())
    seen: dict[str, int] = {}
    for _eid, (d, _p) in descs:
        cfg = d.get("config") or {}
        for k in (*(cfg.get("required_keys_gate") or []), *(cfg.get("required_keys_render") or []),
                  *(cfg.get("defaults") or {})):
            key = f"{str(cfg.get('file') or '').strip()}#{k}"
            seen[key] = seen.get(key, 0) + 1
    for _eid, (d, dpath) in descs:
        cfg = d.get("config") or {}
        f = str(cfg.get("file") or "").strip()
        for lk in ("required_keys_gate", "required_keys_render"):
            for k in cfg.get(lk) or []:
                if f and seen.get(f"{f}#{k}") == 1:
                    q = re.escape(json.dumps(k))

                    def drop(t, lk=lk, q=q):
                        m = re.search(rf"^{lk}\s*=\s*\[[^\]]*\]", t, re.M)
                        span = re.sub(rf"{q}\s*,\s*|,\s*{q}|{q}", "", m[0], count=1)
                        return t[:m.start()] + span + t[m.end():]
                    write_plant_edit(clone, dpath, drop)
                    return f"conf:{f}#{k}"
    raise Refusal("the conf plant found no required conf key one descriptor alone declares")


def write_policy_plant(clone) -> str:
    """Deletes the first `[[key]]` table of the clone's policy catalogue."""
    clone = pathlib.Path(clone)
    rel = gk.resolve_tool_path(clone, "policy", "catalogue.toml").relative_to(clone).as_posix()
    lines = (clone / rel).read_bytes().decode("utf-8").splitlines(keepends=True)
    starts = [i for i, ln in enumerate(lines) if ln.strip() == "[[key]]"]
    if not starts:
        raise Refusal(f"the policy plant found no [[key]] table in {rel}")
    i = starts[0]
    j = next((k for k in range(i + 1, len(lines))
              if lines[k].startswith("[[") or (lines[k].startswith("[") and not lines[k].startswith("[key."))), len(lines))
    name = tomllib.loads("".join(lines[i:j]))["key"][0]["name"]
    write_plant_edit(clone, rel, lambda _t: "".join(lines[:i] + lines[j:]))
    return f"policy:{name}"


def write_verb_plant(clone) -> str:
    """Renames the last verb of the first declared usage source that states it once."""
    clone = pathlib.Path(clone)
    cli, parts, block, line = VERB_SOURCES[0]
    p = gk.resolve_tool_path(clone, *parts)
    text = p.read_bytes().decode("utf-8")
    b = re.search(block, text, re.S | re.M)
    hits = list(re.finditer(line, b[1], re.M))
    once = [h for h in hits if sum(x[1] == h[1] for x in hits) == 1]
    if not once:
        raise Refusal(f"the verb plant found no verb {cli} states once")
    h = once[-1]
    at = b.start(1) + h.start(1)
    write_plant_edit(clone, p.relative_to(clone).as_posix(),
                     lambda t: t[:at] + h[1] + "-moved" + t[at + len(h[1]):])
    return f"verb:{cli}:{h[1]}"


def write_entry_plant(clone) -> str:
    """Deletes the last registry `[[entry]]` row whose descriptor is its own, with that descriptor."""
    clone = pathlib.Path(clone)
    entries = [e for e in gk.load_registry(clone).get("entry", []) if isinstance(e, dict)]
    used = [e.get("descriptor") for e in entries]
    pick = next((e for e in reversed(entries) if used.count(e.get("descriptor")) == 1), None)
    if pick is None:
        raise Refusal("the entry plant found no entry whose descriptor is its own")
    reg = gk.derive_registry_path(clone).relative_to(clone).as_posix()
    want = f"id = {json.dumps(pick['id'])}"

    def drop(t):
        lines = t.splitlines(keepends=True)
        i = next(k for k in range(1, len(lines)) if lines[k].strip() == want and lines[k - 1].strip() == "[[entry]]")
        j = next((k for k in range(i + 1, len(lines)) if not lines[k].strip() or lines[k].startswith("[")), len(lines))
        j += j < len(lines) and not lines[j].strip()
        return "".join(lines[:i - 1] + lines[j:])
    write_plant_edit(clone, reg, drop)
    run_git_staged(clone, "rm", "-q", "--", pick["descriptor"])
    return f"entry:{pick['id']}"


def write_content_plant(clone) -> str:
    """Appends one byte to an installed engine file: an edit that moves no member."""
    clone = pathlib.Path(clone)
    srcs = sorted(row["src"] for _e, row in read_shipped_survivors(clone)
                  if row["role"] == "engine" and row["src"].endswith(".md"))
    if not srcs:
        raise Refusal("the content plant found no installed engine file")
    write_plant_edit(clone, srcs[0], lambda t: t + "\n")
    return ""


def write_class_row_plant(clone, case: str) -> str:
    """One of the registry's own shapes, appended to the clone's class registry: a class whose
    reader returns nothing, a row with no plant, or a fixture class whose own record (its mark)
    names the member that vanishes, or names another."""
    clone = pathlib.Path(clone)
    me = f"{{prefix}}/{HERE.name}/{pathlib.Path(__file__).name}"
    reader = "read_fixture_successors" if case == "empty-class" else "read_fixture_members"
    row = [f'\n[[class]]\nid = "{FIXTURE_CLASS}"\nreader = "{me}:{reader}"\n',
           "" if case == "no-plant" else f'plant = "{me}:write_content_plant"\n',
           f'witness = "{me}:read_fixture_successors"\n' if case.startswith("own-record") else "",
           f'summary = "the step gate fixture\'s {case} class"\n']
    rel = gk.resolve_tool_path(clone, HERE.name, CLASSES_FILE).relative_to(clone).as_posix()
    write_plant_edit(clone, rel, lambda t: t + "".join(row))
    if case.startswith("own-record"):
        (clone / FIXTURE_MARK).write_text("gone\n" if case == "own-record" else "other\n", encoding="utf-8", newline="\n")
        run_git_text(clone, "add", "--", FIXTURE_MARK)
        return f"{FIXTURE_CLASS}:gone"
    return ""


def write_witness_row(clone, planted: str, names: list[str]) -> None:
    """One conforming witness row naming `names` in `surfaces`, staged: a `[[retired]]` row in the
    clone's registry for an `entry` member, an `[[upgrade]]` row in its `steps.toml` otherwise."""
    clone = pathlib.Path(clone)
    reg = gk.derive_registry_path(clone)
    surf = "[" + ", ".join(json.dumps(n) for n in names) + "]"
    if planted.startswith("entry:"):
        rel = reg.relative_to(clone).as_posix()
        row = f'\n[[retired]]\nid = {json.dumps(planted[len("entry:"):])}\nsuccessor = "none"\nsurfaces = {surf}\n'
    else:
        rel = (reg.parent / "steps.toml").relative_to(clone).as_posix()
        argv = json.dumps(["python", f"{{gov}}/{HERE.name}/{pathlib.Path(__file__).name}", "--list"])
        row = (f'\n[[upgrade]]\nid = "{HERE.name}/step-gate-fixture"\nup = {argv}\ndown = {argv}\n'
               f'witness = {argv}\nsurfaces = {surf}\nneeds-target = false\n')
    write_plant_edit(clone, rel, lambda t: t + row)


# ---------------------------------------------------------------------------------- the fixture
def write_fixture_commit(clone, hooks, msg: str) -> None:
    """Commits what the clone's index holds, under no hook and no signing."""
    p = run_git_text(clone, "-c", "user.name=step-gate", "-c", "user.email=step-gate@fixture.invalid",
                     "-c", "commit.gpgsign=false", "-c", f"core.hooksPath={hooks}",
                     "commit", "-q", "--no-verify", "--allow-empty", "-m", msg)
    if p.returncode != 0:
        raise Refusal(f"the fixture commit refused: {p.stderr.strip()}")


def run_gate_subprocess(clone, sha: str) -> tuple[int, str]:
    """The clone's own gate, its tip the clone, graded from `sha`: (exit, its output)."""
    gate = gk.resolve_tool_path(clone, HERE.name, pathlib.Path(__file__).name)
    p = subprocess.run([sys.executable, str(gate), "--base", sha], cwd=str(clone), capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    return p.returncode, p.stdout + p.stderr


def run_step_gate_fixture(root, case: str, with_row: bool) -> int:
    """S7: a scratch clone at HEAD, one plant committed on it, and the clone's gate over that range;
    `with_row` then commits one witness row naming every member the gate redded, and the planted
    one, and grades again. Exits as the last gate run exits."""
    root = pathlib.Path(root)
    sha = run_git_text(root, "rev-parse", "HEAD").stdout.strip()
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="sg-"))
    try:
        clone, hooks = tmp / "c", tmp / "h"
        hooks.mkdir()
        p = run_git_text(tmp, "clone", "-q", "--no-checkout", "--shared", str(root), str(clone))
        if p.returncode != 0:
            raise Refusal(f"the fixture clone refused: {p.stderr.strip()}")
        write_sparse_checkout(clone, sha)
        classes = {c["id"]: c for c in read_surface_classes(clone)}
        if case in classes:
            planted = classes[case]["plant"](clone)
        elif case == "content-edit":
            planted = write_content_plant(clone)
        elif case in REGISTRY_PLANTS:
            planted = write_class_row_plant(clone, case)
        else:
            raise Refusal(f"no fixture case '{case}': the cases are each class id "
                          f"({', '.join(classes)}), content-edit, {', '.join(REGISTRY_PLANTS)}")
        write_fixture_commit(clone, hooks, f"step-gate fixture: plant {case}")
        rc, out = run_gate_subprocess(clone, sha)
        line = f"step-gate: fixture {case} · planted {planted or 'no member'}"
        if with_row:
            names = sorted(set(RED_RE.findall(out)) | ({planted} - {""}))
            write_witness_row(clone, planted, names)
            write_fixture_commit(clone, hooks, f"step-gate fixture: witness row for {case}")
            rc, out = run_gate_subprocess(clone, sha)
            line += f" · witness row naming {len(names)} member(s)"
        print(line)
        sys.stdout.write(out)
        return rc
    finally:
        rmtree_writable(tmp)


def main(argv: list[str]) -> int:
    root = gk.repo_root()
    try:
        if argv == ["--list"]:
            for c in read_surface_classes(root):
                print(f"step-gate: {c['id']} · {len(c['reader'](root))} members · {c['summary']}")
            return 0
        if argv[:1] == ["--print-base"] and (len(argv) == 1 or (len(argv) == 3 and argv[1] == "--base")):
            sha, _boundary, why = gk.resolve_landing_base(root, argv[2] if len(argv) == 3 else None)
            if not sha:
                print(f"step-gate: REFUSED · no base to compare against{why}")
                return 2
            print(sha)
            return 0
        if argv[:2] == ["--fixture", "--plant"] and (len(argv) == 3 or (len(argv) == 4 and argv[3] == "--with-row")):
            return run_step_gate_fixture(root, argv[2], len(argv) == 4)
        if not argv or (len(argv) == 2 and argv[0] == "--base"):
            return check_step_gate(root, argv[1] if argv else None)
        sys.stderr.write("usage: python step_gate.py [--base <rev>] | --list | --print-base [--base <rev>] | "
                         "--fixture --plant <case> [--with-row]\n")
        return 2
    except Refusal as e:
        print(f"step-gate: REFUSED · {e}")
        return 2


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    raise SystemExit(main(sys.argv[1:]))
