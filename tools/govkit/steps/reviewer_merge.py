#!/usr/bin/env python3
"""reviewer_merge.py — the upgrade step `roles/reviewers-to-gov-reviewer` (TOOL-dBoundRoles-18).

    python <gov tool root>/govkit/steps/reviewer_merge.py up|down|witness <target> <prefix>

Its row is the roles kit descriptor's `[[upgrade]]`. TOOL-dBoundRoles-1 merged gov's two reviewer roles,
`gov-spec-reviewer` and `gov-diff-reviewer`, into `gov-reviewer`; this step gives an adopter the same merge
on `govkit update`. `<prefix>` is the target's install prefix, the roles kit found under it by
`resolve_kit_dir`, so a kit homed under another name is found through the receipt.

THE CARRIERS. The roles kit's house file `house/policy.toml`: each level table, `[effort]` and every
`[effort.profiles.<name>]`, with its `roles` and `stages.<workflow>` tables, and `[gates]`. The policy file
`.governance/policy.toml`: `roles.effort.<role>`, `roles.effort.<workflow>.<stage>`, and every other key whose
catalogue name holds a `<role>` segment, read through the policy kit's `read_catalogue_row` by its `scan_keys`.
The overlay `.governance/instructions.toml`: every string value equal to `role.gov-spec-reviewer` or
`role.gov-diff-reviewer`. And each old stem's house text file, `house/<stem>.md`.

THE UP. No old stem in any carrier, no old type under `.claude/agents`, no old role file in the kit and an
index naming neither: exit 0, nothing written. Otherwise it reads every carrier and computes every write
first; a conflict refuses, exit 1, nothing written, the before-image included:
- effort (S4): per level table, the level each finder stage the merge moves takes is recorded, the old
  stems' role entries go, `gov-reviewer` takes the higher of the two by `EFFORT_LEVELS` where both held an
  entry and it holds none, and a stage entry keeps the recorded level wherever the stage would move. The
  stages are the rows of the target's workflow table whose role is an old stem, or `gov-reviewer` under the
  finder key that stem ran, as TOOL-dBoundRoles-1 §4 "The merge" records (`OLD_STAGES`);
- every other `<role>` key and each `[gates]` row (S5) moves where both stems hold one parsed value or
  neither holds one; any other pair refuses naming both stems, the key and the remedy;
- the overlay (S6) is a value edit, `write_overlay_values`; a row whose `edges` names an old tag refuses
  naming the row, since its pin is over the old row;
- a non-empty old house text is appended to `house/gov-reviewer.md` under one line naming its stem, the
  spec reviewer first, and both old house texts and both old role files in the kit are removed;
- a carrier the up writes that differs from its blob at HEAD refuses.
The agent types and the index are what the target's own `render_agents.py` renders over the merged kit:
`derive_render_after` runs that render over a scratch copy of the kit beside it and keeps what it would
write. Then the before-image (`write_before_image`) covers every path, the carriers are written and the old
role files removed, and `render_agents.py --write` runs in the target: it unlinks the two old types as stale
owned types and writes `gov-reviewer.md`, then the index last. An old type the index does not list is no
type the render owns, so the step removes it before the render. The render's result is held to the image.

THE DOWN restores every path from the before-image (`write_from_before_image`): a path edited since the up
refuses the whole down, exit 1, naming it, and nothing is restored.

THE WITNESS exits 0 when no carrier, agent type, kit role file or index entry spells an old stem and, where
the target installs the roles kit and holds an index, the index lists `gov-reviewer`. It runs no target code.

Exit 0 done, 1 refused naming why, 2 a usage error.
"""

import importlib.util
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tomllib

STEP_ID = "roles/reviewers-to-gov-reviewer"
SAY = "reviewer-merge"
MERGED = "gov-reviewer"
OLD = ("gov-spec-reviewer", "gov-diff-reviewer")  # the spec reviewer first, as S6 carries its text
# The finder stage each old stem ran, TOOL-dBoundRoles-1 §4 "The merge": the workflow table an update
# ships maps both keys to MERGED, so the slot a stage held before the merge is read from here.
OLD_STAGES = {"specFinder": OLD[0], "diffFinder": OLD[1]}
TAG = "role."
OLD_TAGS = tuple(TAG + s for s in OLD)
ROLES_HOME = "roles"
POLICY_HOME = "policy"
POLICY = ".governance/policy.toml"
OVERLAY = ".governance/instructions.toml"
AGENTS = ".claude/agents"
INDEX = ".claude/roles.json"
ROLE_SEGMENT = "<role>"
EFFORT_FAMILY = ["roles", "effort", ROLE_SEGMENT]  # S4's family; S5 re-keys every other <role> family
BOM = chr(0xFEFF)
# The render the scratch copy runs: the target's own `render_agents.run_mode`, its one writer swapped
# for a keeper, so what it would write is read and nothing is written.
CAPTURE = r'''import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")
kit, tool_root, target, out = (pathlib.Path(a) for a in sys.argv[1:5])
sys.path.insert(0, str(kit))
import render_agents
held = {"rendered": {}, "stale": []}
def keep_rendered(target_root, rendered, stale):
    held.update(rendered=dict(rendered), stale=list(stale))
    return [], []
render_agents.write_rendered = keep_rendered
held["rc"] = render_agents.run_mode("write", kit, tool_root, target)
out.write_text(json.dumps(held), encoding="utf-8")
'''


def load_conf_to_policy():
    """The shared step helpers beside this file, imported by their path: the runner's `-I` drops
    this file's own directory from `sys.path`."""
    path = pathlib.Path(__file__).resolve().parent / "conf_to_policy.py"
    mod = sys.modules.get("conf_to_policy")
    if mod is not None and getattr(mod, "__file__", None) and pathlib.Path(mod.__file__).resolve() == path:
        return mod
    spec = importlib.util.spec_from_file_location("conf_to_policy", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["conf_to_policy"] = mod
    spec.loader.exec_module(mod)
    return mod


C2P = load_conf_to_policy()
STEPS = C2P.STEPS
Refusal = C2P.Refusal


# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the canonical
# copy named on its marker line and gated by the resolve-python self-test: the roles and policy kits
# are found through it, never through a typed kit path.
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir


def load_target_module(path: pathlib.Path, name: str):
    """The module at `path`, a file of the target's own kits, imported by its path under `name` with no
    bytecode written into the target; one that does not import is a refusal naming it."""
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except (ImportError, SyntaxError, OSError) as e:
        raise Refusal(f"{path.as_posix()}: does not import ({e}), so the step cannot read the target's kit") from None
    return mod


def read_roles_kit(target: pathlib.Path, prefix: str) -> pathlib.Path | None:
    """The roles kit's directory in `target` under the install prefix `prefix`, None where none is."""
    try:
        kit = resolve_kit_dir(ROLES_HOME, "roles_lib.py", target / prefix)
    except LookupError:
        return None
    return kit if target in kit.parents else None


def read_bytes(target: pathlib.Path, rel: str) -> bytes | None:
    """The working-tree bytes of `rel`, None where it is no file."""
    p = target / rel
    return p.read_bytes() if p.is_file() else None


def read_toml(data: bytes | None, rel: str) -> dict | None:
    """`data`, the bytes of `rel`, parsed; None where there are none, a refusal naming `rel` where they
    do not parse, so an unreadable carrier is never read as clean."""
    if data is None:
        return None
    try:
        return tomllib.loads(data.decode("utf-8").removeprefix(BOM))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as e:
        raise Refusal(f"{rel}: does not read as UTF-8 TOML ({e}), so whether it spells a retired "
                      f"reviewer is unknown; fix it, then re-run the step") from None


def read_index_roles(target: pathlib.Path) -> list[str] | None:
    """The role names the index lists, None where there is no index."""
    data = read_bytes(target, INDEX)
    if data is None:
        return None
    try:
        roles = json.loads(data.decode("utf-8")).get("roles")
    except (UnicodeDecodeError, ValueError, AttributeError) as e:
        raise Refusal(f"{INDEX}: does not read as the role index ({e}); re-render it, then re-run the step") from None
    return list(roles) if isinstance(roles, dict) else []


def derive_key_spellings(doc, at: tuple = ()) -> list[str]:
    """The dotted path of every key of the parsed `doc` that is an old stem, at any depth."""
    out = []
    items = doc.items() if isinstance(doc, dict) else enumerate(doc) if isinstance(doc, list) else ()
    for k, v in items:
        path = at + (str(k),)
        if k in OLD:
            out.append(".".join(path))
        out += derive_key_spellings(v, path)
    return out


def derive_value_spellings(doc, at: tuple = ()) -> list[str]:
    """The dotted path of every string value of the parsed `doc` equal to an old tag, at any depth."""
    if isinstance(doc, str):
        return [".".join(at)] if doc in OLD_TAGS else []
    items = doc.items() if isinstance(doc, dict) else enumerate(doc) if isinstance(doc, list) else ()
    return [hit for k, v in items for hit in derive_value_spellings(v, at + (str(k),))]


def read_old_edges(doc: dict) -> list[str]:
    """One refusal line per overlay row whose `edges` names an old tag (§8 F6): an edge is
    `<relation>=<tag>[@<hash8>]`, its pin over the old row's canonical form, so it is re-pinned by its
    owner and never re-keyed here."""
    out = []
    for kind, rows in doc.items():
        if not isinstance(rows, list):
            continue
        for n, row in enumerate(rows, 1):
            if not isinstance(row, dict):
                continue
            edges = row.get("edges")
            for edge in [edges] if isinstance(edges, str) else edges if isinstance(edges, list) else []:
                named = edge.split("=", 1)[1].split("@", 1)[0].strip() if isinstance(edge, str) and "=" in edge else ""
                if named in OLD_TAGS:
                    out.append(f"{OVERLAY} [[{kind}]] row {n} ({row.get('tag', 'no tag')}): its edge '{edge}' "
                               f"names {named}, which the merge retires, and its pin is over that row; remedy: "
                               f"re-pin the edge on {TAG}{MERGED} against that row's canonical form, commit, "
                               f"and re-run the step")
    return out


def read_old_spellings(target: pathlib.Path, kit: pathlib.Path | None) -> list[str]:
    """Every place `target` still spells an old stem, each named by its path and key: the house file's
    keys, each old house text and kit role file, the policy file's key segments, the overlay's values
    and edges, each old agent type and the index's roles. [] is the merge applied."""
    out = []
    if kit is not None:
        kit_rel = kit.relative_to(target).as_posix()
        house = f"{kit_rel}/house/policy.toml"
        out += [f"{house} {k}" for k in derive_key_spellings(read_toml(read_bytes(target, house), house) or {})]
        for stem in OLD:
            out += [rel for rel in (f"{kit_rel}/house/{stem}.md", f"{kit_rel}/agents/{stem}.agent.md")
                    if (target / rel).is_file()]
    out += [f"{POLICY} {k}" for k in derive_key_spellings(read_toml(read_bytes(target, POLICY), POLICY) or {})]
    overlay = read_toml(read_bytes(target, OVERLAY), OVERLAY) or {}
    out += [f"{OVERLAY} {k}" for k in derive_value_spellings(overlay)] + read_old_edges(overlay)
    out += [f"{AGENTS}/{stem}.md" for stem in OLD if (target / AGENTS / f"{stem}.md").is_file()]
    out += [f"{INDEX} roles.{stem}" for stem in OLD if stem in (read_index_roles(target) or [])]
    return out


def derive_merged_stages(rl, kit: pathlib.Path) -> list[tuple[str, str, str]]:
    """`(workflow, stage key, old stem)` for every stage of the target's workflow table the merge moves:
    a row whose role is an old stem, or `gov-reviewer` under the finder key an old stem ran."""
    try:
        workflows = rl.load_workflows(kit)
        out = []
        for w in workflows:
            for key, slot in rl.derive_stage_map(w).items():
                old = slot if slot in OLD else OLD_STAGES.get(key) if slot == MERGED else None
                if old:
                    out.append((w.get("name"), key, old))
    except rl.RolesError as e:
        raise Refusal(f"{kit.as_posix()}/workflows.toml: {e}") from None
    return out


def derive_stage_levels(table: dict, stages, slot_of) -> dict:
    """`{(workflow, stage key): level}` one level table gives each of `stages`, as
    `resolve_stage_efforts` reads that table: its `stages.<workflow>` entry, else the `roles` entry of
    the slot `slot_of(old stem)` names, else its `default`, None where it holds none of them."""
    out = {}
    for wf, key, old in stages:
        staged = (table["stages"].get(wf) or {}).get(key)
        out[(wf, key)] = staged if staged is not None else table["roles"].get(slot_of(old), table["default"])
    return out


def derive_effort_writes(table: dict, stages, levels, roles_at: str, stage_at, where: str) -> list:
    """The edits `[(table, key, value or None to unset)]` that merge one level table (S4, §8 F2): its
    `roles`, `stages` and `default` in `table`, `roles_at` the dotted table its role entries sit in and
    `stage_at(workflow)` a workflow's stage table. Every stage of `stages` keeps the level this table gave
    it: the old role entries go, `gov-reviewer` takes the higher of the two by `levels` where both held one
    and it holds none, and a stage entry is written wherever the stage would move. A table holding neither
    old entry is no edit."""
    roles = table["roles"]
    olds = {s: roles[s] for s in OLD if s in roles}
    if not olds:
        return []
    for s, lv in olds.items():
        if lv not in levels:
            raise Refusal(f"{where} {roles_at}.{s}: '{lv}' is not a level; the levels are {', '.join(levels)}")
    before = derive_stage_levels(table, stages, lambda old: old)
    edits = [(roles_at, s, None) for s in olds]
    merged = {k: v for k, v in roles.items() if k not in OLD}
    if MERGED not in roles and len(olds) == len(OLD):
        merged[MERGED] = max(olds.values(), key=levels.index)
        edits.append((roles_at, MERGED, merged[MERGED]))
    after = derive_stage_levels(dict(table, roles=merged), stages, lambda old: MERGED)
    for (wf, key), lv in before.items():
        if after[(wf, key)] == lv:
            continue
        if lv is None:
            raise Refusal(f"{where} {roles_at}.{MERGED}: already set, so the stage {wf}.{key}, which took no "
                          f"level from this table, would take it; remedy: set {stage_at(wf)}.{key} by hand, "
                          f"commit, and re-run the step")
        edits.append((stage_at(wf), key, lv))
    return edits


def check_key_conflicts(where: str, key: str, held: dict, merged) -> list[str]:
    """[] where the two old stems hold one parsed value of `key`, or neither holds one, and `gov-reviewer`
    holds none or that value; else one line naming both stems, the key and the remedy (S5, §8 F3): one
    value would widen one reviewer's grant or narrow the other's."""
    a, b = (held.get(s) for s in OLD)

    def test_same(x, y) -> bool:
        return type(x) is type(y) and x == y

    def show(v) -> str:
        return "nothing" if v is None else json.dumps(v)

    if test_same(a, b) and (a is None or merged is None or test_same(a, merged)):
        return []
    if test_same(a, b):
        return [f"{where} {key}: {OLD[0]} and {OLD[1]} hold {show(a)} and {MERGED} already holds {show(merged)}; "
                f"remedy: give the three one value or remove {MERGED}'s in {where}, commit, and re-run the step"]
    return [f"{where} {key}: {OLD[0]} holds {show(a)} and {OLD[1]} holds {show(b)}, so {MERGED} would widen one "
            f"reviewer's stages or narrow the other's; remedy: give both stems one value, or remove both, in "
            f"{where}, commit, and re-run the step"]


def derive_family_writes(doc: dict, policy, catalogue) -> tuple[list, list[str]]:
    """`(edits, conflicts)` over the policy file's keys whose catalogue name holds a `<role>` segment, but
    `roles.effort.<role>`, which S4 merges: per key, both stems' values move to `gov-reviewer` where
    `check_key_conflicts` finds none."""
    groups: dict[tuple, tuple] = {}
    for segs, row, value in policy.scan_keys(doc, catalogue):
        pat = str((row or {}).get("name", "")).split(".")
        if ROLE_SEGMENT not in pat:
            continue
        i = pat.index(ROLE_SEGMENT)
        if pat[:i + 1] == EFFORT_FAMILY or segs[i] not in (*OLD, MERGED):
            continue
        shown = ".".join(list(segs[:i]) + [ROLE_SEGMENT] + list(segs[i + 1:]))
        groups.setdefault(segs[:i] + segs[i + 1:], (shown, i, {}))[2][segs[i]] = value
    edits, conflicts = [], []
    for rest, (shown, i, held) in groups.items():
        present = [s for s in OLD if s in held]
        if not present:
            continue
        lines = check_key_conflicts(POLICY, shown, held, held.get(MERGED))
        if lines:
            conflicts += lines
            continue
        for s in present + ([] if MERGED in held else [MERGED]):
            segs = rest[:i] + (s,) + rest[i:]
            edits.append((".".join(segs[:-1]), segs[-1], None if s in OLD else held[OLD[0]]))
    return edits, conflicts


def render_edits(text: str | None, edits) -> str:
    """`text` with each `(table, key, value)` of `edits` applied through the one writer,
    `render_policy_text`, a None value its unset mode: every set first, in order, so a table the
    merged key joins is never emptied and re-appended, then every unset."""
    for table, key, value in sorted(edits, key=lambda e: e[2] is None):
        text = STEPS.render_policy_text(text, table, key, value, unset=value is None)
    return text or ""


def write_overlay_values(text: str) -> str:
    """The overlay `text` with every quoted one-line string value exactly equal to an old tag spelled
    `role.gov-reviewer` in its own quotes, every comment, key and other byte kept (S6). It refuses its own
    output unless tomllib reads the two documents equal once the old tags among the values are mapped,
    so a key or a multi-line string spelling an old tag stops the up."""
    out, i, n = [], 0, len(text)
    while i < n:
        c = text[i]
        if c == "#":
            j = text.find("\n", i)
            j = n if j < 0 else j
        elif text.startswith('"""', i) or text.startswith("'''", i):
            q = text[i:i + 3]
            j = i + 3
            while j < n and not text.startswith(q, j):
                j += 2 if q == '"""' and text[j] == "\\" else 1
            j = min(n, j + 3)
        elif c in "\"'":
            j = i + 1
            while j < n and text[j] != c and text[j] != "\n":
                j += 2 if c == '"' and text[j] == "\\" else 1
            j = min(n, j + 1)
            try:
                value = tomllib.loads("v = " + text[i:j])["v"]
            except tomllib.TOMLDecodeError:
                value = None
            if value in OLD_TAGS:
                out.append(c + TAG + MERGED + c)
                i = j
                continue
        else:
            j = i + 1
        out.append(text[i:j])
        i = j
    got = "".join(out)

    def map_values(v):
        if isinstance(v, dict):
            return {k: map_values(x) for k, x in v.items()}
        if isinstance(v, list):
            return [map_values(x) for x in v]
        return TAG + MERGED if v in OLD_TAGS else v

    try:
        same = map_values(tomllib.loads(text.removeprefix(BOM))) == tomllib.loads(got.removeprefix(BOM))
    except tomllib.TOMLDecodeError:
        same = False
    if not same:
        raise Refusal(f"{OVERLAY}: re-spelling its old tags changes more than its values: a key or a "
                      f"multi-line string spells {OLD_TAGS[0]} or {OLD_TAGS[1]}; remedy: re-spell it "
                      f"{TAG}{MERGED} by hand, commit, and re-run the step")
    return got


def derive_house_text(merged: str, stem: str, body: str) -> str:
    """`merged`, the house text of `gov-reviewer`, with `body`, the old stem's, appended under one line
    naming that stem (S6)."""
    lead = merged.rstrip("\n") + ("\n\n" if merged.strip() else "")
    return f"{lead}From the {stem} house overlay, carried by {STEP_ID}:\n\n{body}\n"


def build_render_env() -> dict:
    """The environment a render runs under: the caller's, less every `GIT_` name, so git answers for
    the target alone."""
    return {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}


def derive_render_after(target: pathlib.Path, kit: pathlib.Path, kit_rel: str, after: dict) -> dict:
    """`{path: bytes, or None for removed}` the target's own `render_agents.py --write` writes over the
    kit as `after` leaves it: the kit copied beside itself under the tool root, `after`'s kit paths
    applied to the copy, and `CAPTURE` run there, which keeps what the render would write and writes
    nothing. A type whose bytes, carriage returns aside, are already on disk is left out, as the render
    leaves it. The copy is removed whatever happens."""
    scratch = kit.parent / f".{kit.name}-{STEP_ID.split('/', 1)[1]}"
    shutil.rmtree(scratch, ignore_errors=True)
    try:
        shutil.copytree(kit, scratch, ignore=shutil.ignore_patterns("__pycache__"))
        for rel, data in after.items():
            if rel.startswith(kit_rel + "/"):
                dest = scratch / rel[len(kit_rel) + 1:]
                if data is None:
                    dest.unlink(missing_ok=True)
                else:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(data)
        held = scratch / "rendered.json"
        p = subprocess.run([sys.executable, "-I", "-c", CAPTURE, str(scratch), str(kit.parent), str(target), str(held)],
                           cwd=str(target), env=build_render_env(), stdin=subprocess.DEVNULL, capture_output=True,
                           text=True, encoding="utf-8", errors="replace")
        got = json.loads(held.read_text(encoding="utf-8")) if p.returncode == 0 and held.is_file() else None
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
    if got is None or got.get("rc") != 0:
        tail = " / ".join((p.stderr or p.stdout).strip().splitlines()[-3:]) or f"exit {p.returncode}"
        raise Refusal(f"{kit_rel}/render_agents.py refuses the merged kit, so nothing was written: {tail}")
    out = {}
    for rel, text in got["rendered"].items():
        data = text.encode("utf-8")
        now = read_bytes(target, rel)
        if now is None or now.replace(b"\r", b"") != data:
            out[rel] = data
    out.update(dict.fromkeys(got["stale"]))
    return out


def cmd_up(target: pathlib.Path, prefix: str) -> int:
    kit = read_roles_kit(target, prefix)
    spelled = read_old_spellings(target, kit)
    if not spelled:
        print(f"{SAY}: up · nothing spells {OLD[0]} or {OLD[1]}, so there is nothing to merge")
        return 0
    if kit is None:
        raise Refusal(f"{spelled[0]}: spells a retired reviewer, and no roles kit under '{prefix}' holds the "
                      f"workflow table the effort rule reads; remedy: remove the spelling by hand, commit, "
                      f"and re-run the step")
    kit_rel = kit.relative_to(target).as_posix()
    rl = load_target_module(kit / "roles_lib.py", "reviewer_merge_roles_lib")
    stages = derive_merged_stages(rl, kit)
    levels = list(rl.EFFORT_LEVELS)
    house_rel = f"{kit_rel}/house/policy.toml"
    texts = {stem: f"{kit_rel}/house/{stem}.md" for stem in (*OLD, MERGED)}
    role_files = [f"{kit_rel}/agents/{stem}.agent.md" for stem in OLD]

    def derive_after(before):
        def read(rel):
            return before[rel] if before is not None and rel in before else read_bytes(target, rel)

        after, conflicts = {}, []
        data = read(house_rel)
        doc = read_toml(data, house_rel)
        if doc is not None:
            effort = doc.get("effort") if isinstance(doc.get("effort"), dict) else {}
            profiles = effort.get("profiles") if isinstance(effort.get("profiles"), dict) else {}
            edits = []
            for at, t in [("effort", effort)] + [(f"effort.profiles.{n}", p) for n, p in profiles.items()]:
                if isinstance(t, dict):
                    view = {"roles": t.get("roles") or {}, "stages": t.get("stages") or {}, "default": t.get("default")}
                    edits += derive_effort_writes(view, stages, levels, f"{at}.roles",
                                                  lambda wf, at=at: f"{at}.stages.{wf}", house_rel)
            gates = doc.get("gates") if isinstance(doc.get("gates"), dict) else {}
            if any(s in gates for s in OLD):
                lines = check_key_conflicts(house_rel, "[gates]", gates, gates.get(MERGED))
                conflicts += lines
                if not lines:
                    edits += [("gates", s, None) for s in OLD if s in gates]
                    edits += [] if MERGED in gates else [("gates", MERGED, gates[OLD[0]])]
            if edits:
                after[house_rel] = render_edits(data.decode("utf-8"), edits).encode("utf-8")
        data = read(POLICY)
        doc = read_toml(data, POLICY)
        if doc is not None and derive_key_spellings(doc):
            try:
                policy_kit = resolve_kit_dir(POLICY_HOME, "policy.py", target / prefix)
            except LookupError:
                raise Refusal(f"{POLICY}: spells a retired reviewer, and no policy kit under '{prefix}' reads "
                              f"the catalogue its keys are matched against; remedy: re-key it by hand") from None
            policy = load_target_module(policy_kit / "policy.py", "reviewer_merge_policy")
            pe = (doc.get("roles") or {}).get("effort") if isinstance(doc.get("roles"), dict) else None
            pe = pe if isinstance(pe, dict) else {}
            view = {"roles": {k: v for k, v in pe.items() if not isinstance(v, dict) and k != "default"},
                    "stages": {k: v for k, v in pe.items() if isinstance(v, dict)}, "default": pe.get("default")}
            edits = derive_effort_writes(view, stages, levels, "roles.effort", lambda wf: f"roles.effort.{wf}", POLICY)
            family, lines = derive_family_writes(doc, policy, policy.load_catalogue(policy_kit))
            conflicts += lines
            if edits + family and not lines:
                after[POLICY] = render_edits(data.decode("utf-8"), edits + family).encode("utf-8")
        data = read(OVERLAY)
        doc = read_toml(data, OVERLAY)
        if doc is not None:
            conflicts += read_old_edges(doc)
            if derive_value_spellings(doc) and not conflicts:
                after[OVERLAY] = write_overlay_values(data.decode("utf-8")).encode("utf-8")
        if conflicts:
            raise Refusal("\n".join(conflicts))
        merged = (read(texts[MERGED]) or b"").decode("utf-8")
        carried = merged
        for stem in OLD:
            body = read(texts[stem])
            if body is None:
                continue
            after[texts[stem]] = None
            body = body.decode("utf-8").replace("\r\n", "\n").strip("\n")
            if body.strip():
                carried = derive_house_text(carried, stem, body)
        if carried != merged:
            after[texts[MERGED]] = carried.encode("utf-8")
        after.update({rel: None for rel in role_files if read(rel) is not None})
        if before is None:
            for rel in sorted(r for r in after if r not in role_files):
                if not C2P.check_committed(target, rel):
                    raise Refusal(f"{rel}: differs from its blob at HEAD; remedy: commit it, then re-run the step")
        after.update(derive_render_after(target, kit, kit_rel, after))
        # an old type the index does not list is no type the render owns, so the step removes it
        after.update({rel: None for rel in old_types if read(rel) is not None})
        return after

    old_types = [f"{AGENTS}/{stem}.md" for stem in OLD]
    unowned = {f"{AGENTS}/{stem}.md" for stem in OLD if stem not in (read_index_roles(target) or [])}
    after = STEPS.write_before_image(target, STEP_ID, derive_after)
    rendered = {rel for rel in after if rel == INDEX or rel.startswith(AGENTS + "/")}
    for rel, data in sorted(after.items()):
        if rel in rendered and rel not in unowned:
            continue
        if data is None:
            (target / rel).unlink(missing_ok=True)
        else:
            (target / rel).parent.mkdir(parents=True, exist_ok=True)
            (target / rel).write_bytes(data)
    for rel in (house_rel, POLICY, OVERLAY, *texts.values(), *role_files):
        done = ("removed" if after[rel] is None else "carries the old house text" if rel == texts[MERGED]
                else "re-keyed") if rel in after else None
        print(f"{SAY}: up · {rel} " + (done or ("spells no retired reviewer, so it is skipped"
                                               if (target / rel).is_file() else "is absent, so it is skipped")))
    p = subprocess.run([sys.executable, "-I", str(kit / "render_agents.py"), "--write"], cwd=str(target),
                       env=build_render_env(), stdin=subprocess.DEVNULL, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if p.returncode != 0:
        tail = " / ".join((p.stderr or p.stdout).strip().splitlines()[-3:])
        raise Refusal(f"{kit_rel}/render_agents.py --write exited {p.returncode} after the carriers were written: "
                      f"{tail}; remedy: run the step's down, which restores them")
    moved = {ln.split(" ", 2)[2] for ln in p.stdout.splitlines()
             if ln.startswith(("render_agents: wrote ", "render_agents: unlinked "))}
    off = sorted(rel for rel in rendered | moved if rel not in after or (
        (read_bytes(target, rel) or b"").replace(b"\r", b"") != after[rel] if after[rel] is not None
        else (target / rel).exists()))
    if off:
        raise Refusal(f"{', '.join(off)}: the render wrote other bytes than the before-image records; remedy: "
                      f"run render_agents.py --check, and the step's down, which names each path it cannot restore")
    print(f"{SAY}: up · {kit_rel}/render_agents.py --write · "
          + ", ".join(f"{rel} {'unlinked' if after[rel] is None else 'written'}" for rel in sorted(rendered)))
    return 0


def cmd_down(target: pathlib.Path, prefix: str) -> int:
    restored = STEPS.write_from_before_image(target, STEP_ID)
    print(f"{SAY}: down · restored {', '.join(restored) or 'nothing: no before-image, no up applied'}")
    return 0


def cmd_witness(target: pathlib.Path, prefix: str) -> int:
    kit = read_roles_kit(target, prefix)
    spelled = read_old_spellings(target, kit)
    listed = read_index_roles(target)
    if not spelled and kit is not None and listed is not None and MERGED not in listed:
        spelled = [f"{INDEX} lists no {MERGED}"]
    if spelled:
        print(f"{SAY}: witness · {spelled[0]}: still the reviewers before the merge, so not applied")
        return 1
    print(f"{SAY}: witness · nothing spells {OLD[0]} or {OLD[1]}: applied")
    return 0


def main(argv: list[str]) -> int:
    verbs = {"up": cmd_up, "down": cmd_down, "witness": cmd_witness}
    if len(argv) != 3 or argv[0] not in verbs:
        sys.stderr.write("usage: python reviewer_merge.py up|down|witness <target> <prefix>\n")
        return 2
    prefix = argv[2]
    if prefix not in ("", ".") and STEPS.derive_contained_rel(prefix) is None:
        sys.stderr.write(f"{SAY}: '{prefix}' is not an install prefix inside the target\n")
        return 2
    try:
        return verbs[argv[0]](pathlib.Path(argv[1]).resolve(), prefix)
    except Refusal as e:
        sys.stderr.write(f"{SAY}: {argv[0]} refused · {e}\n")
        return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    raise SystemExit(main(sys.argv[1:]))
