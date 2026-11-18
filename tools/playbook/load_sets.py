"""load_sets — each reader's load set, the missing-unit refusal, the render-time budgets and the injected
load points (PLAY-dOrderedCharter-11), and every role's `code` slot (PLAY-dOrderedCharter-27).

    python load_sets.py derive --reader <tag> [--item <tag>] [--feature <tag>]... [--units <manifest>]
                               [--code-budget <n>k] [--root <dir>]
    python load_sets.py check [--reader <tag>]... [--item <tag>] [--units <manifest>] [--checks refuse|warn|record]
                              [--load-point <name>[=<bytes>]]... [--budgets-enforce refuse|warn] [--reach]
                              [--root <dir>]
    python load_sets.py injected [--card <path>] [--cap <name>=<bytes>]... [--root <dir>]
    python load_sets.py --fixture --plant <case> [<check flags>]

THE LOAD SET (S1), `derive_load_set`: from the instruction-unit rows, read through `instruction_units`, the
units whose `scope` holds `reader.every`; for a `role.<name>` reader the units scoped to a practice tag the
role's `rules:` value cites, read off the roles kit's agent file, and the units scoped `role.<name>` once the
namespace registry holds a `role` row whose `role` is `selects`; the item's units once an `item` row selects;
and the units scoped to a `feature.*` tag the caller names once a `feature` row selects. A part whose
namespace no row registers as a selector selects nothing and is reported `unarmed — <ns>.*`, never empty and
green. The registry is the target's own, under its tool root, else the one beside this module. The set keeps
the unit registry's order.

THE REACH UNITS (PLAY-dOrderedCharter-21), `derive_reach_units`: a `role.<name>` reader's step is the reach
word the loop definition gives the workflow its `workflow:` value names, read through the loop kit's
`read_workflow_reach` (TOOL-dDeclaredLoop-1): the loop row's `reach`, else the last segment of its `step`,
else `none`; for a step other than `none`, one unit per active
practice (`charter.practices` at the root) whose catalogue row has a reach at that step, tag
`practice.<name>.<step>`, text the reach, derived at render and never written as a row. `derive` lists them
after the registry's units; `check --reach` prints one `load-set — reach ·` line per unit for each reader.
A step or an active set that does not read leaves the part `unarmed`, naming why.

THE CODE SLOT (PLAY-dOrderedCharter-27), `read_code_slot`: every `role.<name>` reader's set lists a `code`
slot, filled or not, priced by the policy key `memory.code-budget` read through `read_policy_value` at the
root, `<n>k` at 1,000 bytes a `k`. `--code-budget` stands in for the key. A value of another shape, or a
refused read, refuses the derivation naming the key. A filled slot is the `code` load point, measured under
the cap census row `code-slot`, a family whose value is this key's.

THE REFUSAL (S2), `check_required`: every unit whose `required-by` names the reader or its item and which the
set lacks. Its mode is the policy key `instructions.checks`, read through `policy_value.read_policy_value`:
`refuse` (the default) leaves the render undone and exits 1 naming each unit; `warn` prints a
`Missing required unit: <tag> · <reader>` line for the reader's text; `record` prints a `**Load gaps:**` line
for the prompt record alone. No value skips the check, and `budgets.enforce` is never read here. A refused
read runs the check as `refuse` and prints the reader's line once. `--checks` stands in for the key.

THE BUDGETS (S3), `check_budget`: a load point's bytes, CR stripped, against its cap. A path's cap is the cap
census row named by that path, read with tomllib from the policy kit's census; a `role.<name>` block's is the
`role-body` family, its value the roles kit's BODY_CEILINGS read from its source and never copied. One run of
the budgets script's `resolve` verb answers each cap's value and mode; over its cap a load point warns or
refuses as that mode says, `--budgets-enforce` standing in for the switch where the switch set the mode. A
file a harness reads whole carries the harness's limit as a second cap, today `AGENTS.md` under Codex's
CODEX_MAX, read through the budgets script's `home` verb on the `codex-instructions` row; over it the set is
refused whatever the mode. A load point with no census row prints `no cap declared`; an exit 2 of the
budgets script refuses, printing its line; with no policy kit the budget part prints `unarmed`.

THE INJECTED LOAD POINTS (S5), `measure_injected`: the agent list (each `description:` of
`.claude/agents/*.md`), the Skill list (each `description:` of the tracked Skills `kind.skill`'s population
in `kinds.toml` names, `*skills/*/SKILL.md`, listed by the core's `read_skill_paths`) and the session-start
card, one line each with its bytes and its cap or `no cap declared`, and an `injected — breach` line for each
over its cap. Every description is read by the core's `read_front_matter`, the one reader the Skill gate
reads too (PLAY-dOrderedCharter-49 S34), so the verb runs from this kit's directory, `core.py` beside it, and
no longer from a lone copy of this file. No cap census row names an injected load point, so a cap is one
`--cap` hands in, else none is declared. The kickoff card writer runs this verb and appends the breach lines.

Exit 0 green, 1 refused, 2 a usage error.
"""
from __future__ import annotations

import argparse
import ast
import functools
import os
import pathlib
import re
import subprocess
import sys
import tomllib

sys.dont_write_bytecode = True

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
if str(KIT_DIR) not in sys.path:
    sys.path.insert(0, str(KIT_DIR))

SAY = "load-set"
EVERY = "reader.every"
CHECK_MODES = ("refuse", "warn", "record")
ROLE_CAP = "role-body"
#: The code slot: its load point, its census cap, and the policy key that prices it (PLAY-dOrderedCharter-27).
CODE_SLOT, CODE_CAP, CODE_KEY = "code", "code-slot", "memory.code-budget"
CODE_BUDGET_RE = re.compile(r"([1-9][0-9]*)k")
#: The files a harness reads whole, each with its limit's census row: Codex reads `AGENTS.md`, the fork record's F3.
HARNESS_READS = {"AGENTS.md": ("codex-instructions", "Codex")}
MISSING = "Missing required unit:"
GAPS = "**Load gaps:**"
#: `check --reach`'s line per reach unit, `<REACH> role.<name> · practice.<name>.<step> · <reach>`, which the
#: roles kit's handoff reads off the subprocess its load-set check already runs (PLAY-dOrderedCharter-21 S3).
REACH = "load-set — reach ·"
INJECTED = "injected"
#: S5's injected load points: the name a cap is asked under, the label printed, and what is measured: the
#: agent list's glob, the Skill list's `kind.skill` population, read tracked (PLAY-dOrderedCharter-49 S34).
INJECTED_POINTS = (("agent-list", "agent list", (".claude/agents/*.md",)),
                   ("skill-list", "Skill list", "kind.skill"),
                   ("card", "card", ()))
GIT_TIMEOUT_S = 30


def run_git_bytes(root, *args) -> bytes | None:
    """git's stdout in `root`, or None on a non-zero exit; the caller's GIT_ variables kept out."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    try:
        p = subprocess.run(["git", "-C", str(root), *args], capture_output=True, env=env, timeout=GIT_TIMEOUT_S,
                           stdin=subprocess.DEVNULL)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return p.stdout if p.returncode == 0 else None


# ---- S1: the load set --------------------------------------------------------------------------------------

def read_namespace_rows(root=None) -> list[dict]:
    """The target's namespace registry rows, at this kit's path under its tool root, else this kit's own;
    `tag_index.read_namespaces` raises TagError on one that does not read."""
    import instruction_units as iu
    import tag_index
    own = pathlib.Path(root) / iu.derive_kit_rel("namespaces.toml") if root is not None else None
    return tag_index.read_namespaces(own if own is not None and own.is_file() else KIT_DIR / "namespaces.toml")


def check_selector_armed(rows, ns) -> bool:
    """True when the registry holds a `ns` row whose `role` is `selects`."""
    return any(r.get("ns") == ns and r.get("role") == "selects" for r in rows)


def read_role_field(name, key) -> tuple[tuple | None, str]:
    """`((roles kit dir, value), why)`: the `key:` value of the roles kit's agent file for role `name`, ''
    when the file has no such line; None with the reason when no roles kit or no such role is found."""
    from policy_value import resolve_kit_dir
    try:
        kit = resolve_kit_dir("roles", "check_roles.py", KIT_DIR)
    except LookupError as exc:
        return None, f"no roles kit: {exc}"
    path = kit / "agents" / f"{name}.agent.md"
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None, f"no role {name} in the roles kit"
    m = re.search(rf"(?m)^{re.escape(key)}:[ \t]*(.*)$", text.split("\n---", 1)[0])
    return (kit, (m.group(1) if m else "").strip()), ""


def read_role_rules(name) -> tuple[list | None, str]:
    """`(practice tags, why)`: the `rules:` value of the roles kit's agent file for role `name`, each entry
    `practice.<tag>` with any `?` cut; None with the reason when no roles kit or no such role is found."""
    got, why = read_role_field(name, "rules")
    if got is None:
        return None, why
    tags = [t.strip().rstrip("?") for t in got[1].split(",") if t.strip()]
    return [f"practice.{t}" for t in tags], ""


def read_role_step(name) -> tuple[str | None, str]:
    """`(step, why)`: the reach word the loop definition gives the workflow that role `name`'s `workflow:`
    value names (PLAY-dOrderedCharter-21 S1, moved by TOOL-dDeclaredLoop-1), read through the loop kit's
    `read_workflow_reach`; None with the reason when no roles kit, role, loop kit or loop row is found, or
    the definition does not read."""
    got, why = read_role_field(name, "workflow")
    if got is None:
        return None, why
    workflow = got[1]
    from render_playbook import load_loop_kit
    try:
        loop_lib, kit = load_loop_kit(KIT_DIR)
        reach = loop_lib.read_workflow_reach(kit)
    except LookupError as exc:
        return None, f"no loop kit: {exc}"
    except ValueError as exc:     # the reader's LoopError
        return None, f"the loop definition does not read: {exc}"
    if workflow not in reach:
        return None, f"role {name}'s workflow {workflow!r} has no row in the loop definition"
    return reach[workflow], ""


@functools.lru_cache(maxsize=None)
def read_active_rows(root) -> tuple[list, tuple]:
    """`(active practice rows, notes)` at `root`, this kit's catalogue: one policy read per root per run."""
    import instruction_units as iu
    notes = []
    rows = iu.read_active_practices(iu.read_practice_catalogue(KIT_DIR / "practices.toml"), root, notes)
    return rows, tuple(notes)


def derive_reach_units(name, root) -> tuple[list, str]:
    """`([(tag, reach)], report line)`: PLAY-dOrderedCharter-21 S2, one unit per active practice at `root`
    whose catalogue row has a reach at role `name`'s step, tag `practice.<name>.<step>`, in catalogue order.
    Derived from the catalogue at render and never written as a row; a step of `none` derives none, and a
    step or an active set that does not read leaves the part `unarmed`, naming why."""
    import instruction_units as iu
    step, why = read_role_step(name)
    if step is None:
        return [], f"reach — unarmed — {why}"
    if step == "none":
        return [], "reach — step none · 0 unit(s)"
    try:
        rows, notes = read_active_rows(str(root))
    except iu.UnitRowError as exc:
        return [], f"reach — unarmed — {exc}"
    units = [(f"{r['tag']}.{step}", r["reach"][step]) for r in rows if step in r["reach"]]
    return units, f"reach — step {step} · {len(units)} unit(s)" + "".join(f" · {n}" for n in notes)


class SlotRefused(ValueError):
    """The code slot's budget did not read: a value outside `<n>k`, or the policy reader's refusal."""


@functools.lru_cache(maxsize=None)
def read_code_slot(root, stand_in=None) -> dict:
    """The `code` slot's entry, `{"slot", "budget", "source"}`: `memory.code-budget` at `root`, or `stand_in`
    in its place, in bytes at 1,000 a `k`; the source names where the value came from. SlotRefused names the
    key on a value of another shape and on a refused read, never deriving a default."""
    if stand_in is None:
        from policy_value import PolicyRefused, read_policy_value
        try:
            lines, explain = read_policy_value("memory.code-budget", root)
        except PolicyRefused as exc:
            raise SlotRefused(f"{CODE_KEY} did not read · {exc.line}") from None
        value = lines[0].strip() if lines else ""
        how = (explain.split(" · ") + ["", ""])[1] or "policy"
        source = f"{CODE_KEY} {how} {value}"
    else:
        value, source = stand_in, f"--code-budget {stand_in}"
    m = CODE_BUDGET_RE.fullmatch(value)
    if not m:
        raise SlotRefused(f"{CODE_KEY} is {value!r}, not <n>k")
    return {"slot": CODE_SLOT, "budget": int(m[1]) * 1000, "source": source}


def derive_load_set(units, reader, item=None, features=(), namespaces=None, root=None,
                    code_budget=None) -> tuple[list, list]:
    """`(tags, report)`: the tags of the units `reader` loads, in the registry's order, and one report line per
    part. `namespaces` is the registry's rows, this kit's own when None. A `role.<name>` reader's set ends with
    its reach units, `derive_reach_units` at `root`, and its report lists its `code` slot with the budget
    `read_code_slot` reads there, `code_budget` standing in; a `root` of None leaves both unread, as `check`
    does, which prints no set. SlotRefused when the budget refuses."""
    rows = read_namespace_rows() if namespaces is None else namespaces
    picked, report = set(), []

    def add_part(part, wanted):
        hit = [u.tag for u in units if u.tag and wanted & set(u.scope)]
        picked.update(hit)
        report.append(f"{part} — {len(hit)} unit(s)")

    def add_unarmed(part, ns):
        report.append(f"{part} — unarmed — {ns}.*: no {ns} namespace is registered")

    add_part("every", {EVERY})
    ns, _dot, name = reader.partition(".")
    if ns == "role":
        tags, why = read_role_rules(name)
        if tags is None:
            report.append(f"practice — unarmed — {why}")
        else:
            add_part("practice", set(tags))
            report[-1] += f", by the {len(tags)} practice tag(s) its rules cite"
    if reader != EVERY:
        if check_selector_armed(rows, ns):
            add_part(ns, {reader})
        else:
            add_unarmed(ns, ns)
    if item is None:
        report.append("item — unarmed — item.*: no item namespace is registered"
                      if not check_selector_armed(rows, "item") else "item — none named")
    elif check_selector_armed(rows, item.partition(".")[0]):
        add_part("item", {item})
    else:
        add_unarmed("item", item.partition(".")[0])
    if features:
        if check_selector_armed(rows, "feature"):
            add_part("feature", set(features))
        else:
            add_unarmed("feature", "feature")
    reach = []
    if ns == "role" and root is not None:
        reach, line = derive_reach_units(name, root)
        report.append(line)
        slot = read_code_slot(str(root), code_budget)
        report.append(f"{slot['slot']} — slot · budget {slot['budget']} · {slot['source']}")
    return [u.tag for u in units if u.tag in picked] + [tag for tag, _text in reach], report


# ---- S2: the missing-unit refusal --------------------------------------------------------------------------

def check_required(load_set, units, reader, item, mode) -> tuple[bool, list]:
    """`(refused, lines)`: each unit whose `required-by` names `reader` or `item` and which `load_set` lacks,
    printed as `mode` says; `refused` only under `refuse` with a unit missing."""
    named = {reader, item} - {None}
    missing = [u.tag for u in units if u.tag and named & set(u.required_by) and u.tag not in load_set]
    if not missing:
        return False, []
    if mode == "warn":
        return False, [f"{MISSING} {t} · {reader}" for t in missing]
    if mode == "record":
        return False, [f"{GAPS} {reader} · {', '.join(missing)}"]
    return True, [f"{SAY} — refused · {reader} · missing {', '.join(missing)} · instructions.checks={mode}"]


def read_checks_mode(root) -> tuple[str, list]:
    """`(mode, notes)`: `instructions.checks` at `root`; a refused read is `refuse`, its line printed once."""
    from policy_value import PolicyRefused, read_policy_value
    try:
        value = read_policy_value("instructions.checks", root)[0]
    except PolicyRefused as exc:
        return "refuse", [f"{SAY} — instructions.checks read as refuse · {exc.line}"]
    mode = value[0].strip() if value else "refuse"
    return (mode if mode in CHECK_MODES else "refuse"), []


# ---- S3: the budgets ---------------------------------------------------------------------------------------

def read_body_ceiling(role) -> int | None:
    """BODY_CEILINGS[role] as the roles kit's checker assigns it, read from its source; None with no kit."""
    from policy_value import resolve_kit_dir
    try:
        path = resolve_kit_dir("roles", "check_roles.py", KIT_DIR) / "check_roles.py"
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except (LookupError, OSError, SyntaxError):
        return None
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == "BODY_CEILINGS" for t in node.targets):
            return ast.literal_eval(node.value).get(role)
    return None


def run_budgets(kit, cwd, *args) -> tuple[int, str, str]:
    """`(rc, stdout, stderr)` of the policy kit's budgets script; the script and its verb stay separate."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    script = str(kit / "budgets.py")
    try:
        p = subprocess.run([sys.executable, script, *args], cwd=str(cwd), capture_output=True, text=True,
                           encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL, env=env, timeout=60)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return 2, "", f"the budgets script did not run: {exc}"
    return p.returncode, p.stdout, p.stderr


def read_cap_answers(root, points) -> tuple[dict, list, bool]:
    """`(caps, lines, refused)`: for each load point name, its answers `[(cap, value, mode, rule, harness)]`,
    an absent name holding no census row. One run of the `resolve` verb, plus one of `home` where a harness
    reads a load point whole. No policy kit is one `unarmed` line; an exit 2 is a refusal printing its line."""
    from policy_value import resolve_kit_dir
    try:
        kit = resolve_kit_dir("policy", "budgets.py", KIT_DIR)
        census = {r.get("name"): r for r in tomllib.loads((kit / "caps.toml").read_text(encoding="utf-8")).get("cap", [])}
    except (LookupError, OSError, tomllib.TOMLDecodeError) as exc:
        return {}, [f"{SAY} — budgets unarmed · no policy kit found: {exc}"], False
    asked = {p: (ROLE_CAP if p.startswith("role.") else CODE_CAP if p == CODE_SLOT else p) for p in points}
    asked = {p: c for p, c in asked.items() if c in census}
    caps: dict = {}
    if asked:
        rc, out, err = run_budgets(kit, root, "resolve", "--explain", *sorted(set(asked.values())))
        if rc == 2:
            return {}, [f"{SAY} — refused · {(err.strip().splitlines() or ['the budgets script exited 2'])[-1]}"], True
        rules = dict(ln[len("budgets: "):].split(" · ")[:2] for ln in err.splitlines()
                     if ln.startswith("budgets: ") and ln.count(" · ") >= 2)
        rows = {f[0]: f for f in (ln.split("\t") for ln in out.splitlines()) if len(f) == 4}
        for p, cap in asked.items():
            if cap in rows:
                try:
                    value = (read_body_ceiling(p[5:]) if cap == ROLE_CAP
                             else read_code_slot(str(root))["budget"] if cap == CODE_CAP
                             else None if rows[cap][1] == "-" else int(rows[cap][1]))
                except SlotRefused as exc:
                    return {}, [f"{SAY} — refused · {exc}"], True
                caps.setdefault(p, []).append((cap, value, rows[cap][2], rules.get(cap, ""), False))
    for p in points:
        if p in HARNESS_READS:
            cap, who = HARNESS_READS[p]
            top = (run_git_bytes(kit, "rev-parse", "--show-toplevel") or b"").decode("utf-8", "replace").strip()
            rc, out, err = run_budgets(kit, top or kit, "home", cap)
            if rc != 0:
                return {}, [f"{SAY} — refused · {(err.strip().splitlines() or ['the budgets script exited 2'])[-1]}"], True
            _cap, home, value = (out.strip().split("\t") + ["", "", ""])[:3]
            if value.isdigit():
                caps.setdefault(p, []).append((home.rpartition(":")[2], int(value), "refuse",
                                               f"{who}'s limit for a file it reads whole", True))
    return caps, [], False


def check_budget(load_point, size, mode=None, answers=None) -> tuple[bool, list]:
    """`(refused, lines)` for `size` bytes of `load_point` against `answers`, `read_cap_answers`' list for it.
    `mode` stands in for the switch where `budgets.enforce` set a cap's mode; a harness limit refuses always."""
    if not answers:
        return False, [f"{SAY} — {load_point} · {size} bytes · no cap declared"]
    refused, lines = False, []
    for cap, value, cmode, rule, harness in answers:
        swap = bool(mode) and not harness and rule.startswith("budgets.enforce")
        use, why = (mode, f"--budgets-enforce {mode}") if swap else (cmode, rule)
        if not value:
            lines.append(f"{SAY} — {load_point} · {size} bytes · {cap} unchecked")
        elif size <= value:
            lines.append(f"{SAY} — {load_point} · {size} bytes of {value} ({cap})")
        else:
            word = "REFUSE" if use == "refuse" else "WARN"
            refused |= use == "refuse"
            lines.append(f"{SAY} — BUDGET {word} · {load_point} · {size} bytes over {cap} {value} · {why}")
    return refused, lines


def measure_blob(root, path) -> int | None:
    """The bytes of `path` in `root`'s HEAD, CR stripped; None where HEAD holds no such file."""
    blob = run_git_bytes(root, "show", f"HEAD:{path}")
    return None if blob is None else len(blob.replace(b"\r", b""))


def run_budget_check(root, points, mode=None) -> tuple[bool, list]:
    """`(refused, lines)` over `points`, `[(name, bytes)]`: ONE cap read for all, then `check_budget` each."""
    caps, lines, refused = read_cap_answers(root, [p for p, _s in points])
    if refused or lines:
        return refused, lines
    for point, size in points:
        r, got = check_budget(point, size, mode, caps.get(point))
        refused |= r
        lines += got
    return refused, lines


# ---- S5: the injected load points --------------------------------------------------------------------------

def measure_injected(root, card=None, caps=None) -> list:
    """S5's lines: each injected load point with its bytes and its cap, then a breach line for each over it."""
    root, caps, lines, breaches = pathlib.Path(root), dict(caps or {}), [], []
    if card is None:
        common = (run_git_bytes(root, "rev-parse", "--path-format=absolute", "--git-common-dir") or b"").decode().strip()
        cards = sorted(pathlib.Path(common, "orientation").glob("*.md"), key=lambda p: p.stat().st_mtime) if common else []
        card = cards[-1] if cards else None
    import core   # the one front-matter reader and the tracked Skill list, beside this file
    for name, label, globs in INJECTED_POINTS:
        if globs:
            if globs == "kind.skill":
                row = core.read_kind_row(KIT_DIR, "", "skill") or {}
                files = [root / p for p in core.read_skill_paths(root, row.get("population", "")) or ()]
            else:
                files = sorted({p for g in globs for p in root.glob(g) if p.is_file()})
            size = sum(len(((core.read_front_matter(p.read_text(encoding="utf-8", errors="replace")) or {})
                            .get("description") or "").encode("utf-8")) for p in files if p.is_file())
            what = f"{len(files)} description(s)"
        else:
            path = pathlib.Path(card) if card else None
            size = len(path.read_bytes().replace(b"\r", b"")) if path and path.is_file() else 0
            what = path.as_posix() if path and path.is_file() else "no card written"
        cap = caps.get(name)
        lines.append(f"{INJECTED} — {label} · {what} · {size} bytes · " + (f"cap {cap}" if cap else "no cap declared"))
        if cap and size > cap:
            breaches.append(f"{INJECTED} — breach · {label} · {size} bytes over {cap}")
    return lines + breaches


# ---- the CLI and the plants --------------------------------------------------------------------------------

def read_units_arg(root, units_path):
    """The unit rows: the manifest `units_path` names, else every kit manifest `root` tracks."""
    import instruction_units as iu
    if units_path:
        path = pathlib.Path(units_path)
        units, faults = iu.parse_unit_rows(path.read_text(encoding="utf-8"), path.as_posix())
        if faults:
            raise iu.UnitRowError("\n".join(str(f) for f in faults))
        return units
    return iu.read_units(root)


def run_check(a) -> int:
    """`check`: S2 for each `--reader`, then S3 for each `--load-point`; exit 1 on any refusal."""
    import tag_index
    root, refused, out = pathlib.Path(a.root), False, []
    if a.reader:
        try:
            units, rows = read_units_arg(root, a.units), read_namespace_rows(root)
        except (OSError, ValueError, tag_index.TagError) as exc:
            print(f"{SAY} — refused · the unit registry does not read: {exc}")
            return 1
        mode, notes = (a.checks, []) if a.checks else read_checks_mode(root)
        out += notes
        for reader in a.reader:
            tags, _report = derive_load_set(units, reader, a.item, (), rows)
            r, lines = check_required(tags, units, reader, a.item, mode)
            refused |= r
            out += lines
            if a.reach and reader.startswith("role."):
                reach, line = derive_reach_units(reader[len("role."):], root)
                out += [f"{REACH} {reader} · {tag} · {text}" for tag, text in reach]
                out += [f"{SAY} — {reader} · {line}"] if " — unarmed — " in line else []
    points = []
    for spec in a.load_point:
        name, eq, size = spec.partition("=")
        n = int(size) if eq and size.isdigit() else measure_blob(root, name)
        if n is None:
            out.append(f"{SAY} — refused · {name} · no such file in HEAD and no size handed in")
            refused = True
            continue
        points.append((name, n))
    if points:
        r, lines = run_budget_check(root, points, a.budgets_enforce)
        refused |= r
        out += lines
    if out:
        print("\n".join(out))
    return 1 if refused else 0


def run_derive(a) -> int:
    """`derive`: the reader's set, its required count, and each part's report line."""
    import tag_index
    root = pathlib.Path(a.root)
    try:
        units, rows = read_units_arg(root, a.units), read_namespace_rows(root)
    except (OSError, ValueError, tag_index.TagError) as exc:
        print(f"{SAY} — refused · the unit registry does not read: {exc}")
        return 1
    try:
        tags, report = derive_load_set(units, a.reader, a.item, tuple(a.feature), rows, root, a.code_budget)
    except SlotRefused as exc:
        print(f"{SAY} — refused · {a.reader} · {exc}")
        return 1
    named = {a.reader, a.item} - {None}
    required = sum(1 for u in units if named & set(u.required_by))
    print(f"{SAY} — {a.reader} · {len(tags)} unit(s) of {len(units)} · {required} required")
    for t in tags:
        print(f"  {t}")
    for line in report:
        print(line)
    return 0


#: The plants of the unit's New arm line: each a fixture registry and the verb it runs.
PLANT_UNITS = {
    "required-away": ('[[unit]]\ntag = "unit.every"\nscope = ["reader.every"]\n\n'
                      '[[unit]]\ntag = "unit.needed"\nscope = ["role.gov-skeptic"]\nrequired-by = ["role.gov-builder"]\n'),
    "role": ('[[unit]]\ntag = "unit.every"\nscope = ["reader.every"]\n\n[[unit]]\ntag = "unit.builder"\n'
             'scope = ["role.gov-builder"]\n\n[[unit]]\ntag = "unit.skeptic"\nscope = ["role.gov-skeptic"]\n'),
    "feature": '[[unit]]\ntag = "unit.roles"\nscope = ["feature.roles"]\n',
}
PLANTS = {"required-away": ("required-away", "role"), "role-unregistered": ("role", None),
          "role-registered": ("role", "role"), "feature-unregistered": ("feature", None),
          "feature-registered": ("feature", "feature"), "charter-over": (None, None),
          "role-block-over": (None, None), "code-every-role": ("role", None), "code-refused": ("role", None),
          "code-refused-check": (None, None),
          "code-over": (None, None), "code-at": (None, None)}
#: The `code-refused` plant's one committed policy file: a `memory.code-budget` its catalogue row refuses.
PLANT_POLICY = (".governance/policy.toml", '[memory]\ncode-budget = "big"\n')
PLANT_CHARTER_BYTES, PLANT_CHARTER_CAP = 40000, 50000


def build_plant_tree(top, plant) -> tuple[pathlib.Path, pathlib.Path]:
    """`(root, manifest)`: a repository on `main` holding the plant's unit manifest, the shipped namespace
    registry with the plant's row, and what the plant's verb reads, every path derived from this kit's own."""
    import instruction_units as iu
    from gov_tag import derive_fixture_row
    root = pathlib.Path(top) / "t"
    units, ns = PLANTS[plant]
    files = {iu.derive_kit_rel("namespaces.toml"): (KIT_DIR / "namespaces.toml").read_text(encoding="utf-8")
             + (derive_fixture_row(ns, "fixture_tags:extract_declared", "selects") if ns else ""),
             ".memory-tree.conf": 'MEMORY_ROOT=memory\nCHARTER="AGENTS.md"\n',
             "AGENTS.md": "x" * (PLANT_CHARTER_BYTES - 1 if plant == "charter-over" else 10) + "\n",
             "memory/builds/bx/README.md": "# bx\n"}
    if units:
        files[iu.derive_tool_rel("kitx", iu.MANIFEST)] = PLANT_UNITS[units]
    if plant == "charter-over":
        files[iu.derive_tool_rel("template-size-limits.txt")] = f"AGENTS.md\t{PLANT_CHARTER_CAP}\n"
    if plant.startswith("code-refused"):
        files[PLANT_POLICY[0]] = PLANT_POLICY[1]
    for rel, text in files.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8", newline="\n")
    for args in (("init", "-q", "-b", "main"), ("add", "-A"),
                 ("-c", "user.name=fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "plant")):
        if run_git_bytes(root, *args) is None:
            raise OSError(f"git {args[0]} failed in the plant tree")
    return root, root / iu.derive_tool_rel("kitx", iu.MANIFEST)


def run_code_every_role(root, manifest) -> int:
    """The `code-every-role` plant: each role of the roles kit derived at `root`, its code line printed; 1 when
    a role's set lacks the slot or no role is found."""
    import instruction_units as iu
    from policy_value import resolve_kit_dir
    agents = sorted((resolve_kit_dir("roles", "check_roles.py", KIT_DIR) / "agents").glob("*.agent.md"))
    units = iu.parse_unit_rows(manifest.read_text(encoding="utf-8"), manifest.as_posix())[0]
    rows, lacking = read_namespace_rows(root), []
    for agent in agents:
        reader = "role." + agent.name[:-len(".agent.md")]
        _tags, report = derive_load_set(units, reader, None, (), rows, root)
        got = [ln for ln in report if ln.startswith(f"{CODE_SLOT} — slot · ")]
        print(f"{reader} · {got[0] if got else 'NO code slot'}")
        lacking += [] if got else [reader]
    if lacking or not agents:
        print(f"{SAY} — code slot missing on {', '.join(lacking) or 'every role: no role found'}")
        return 1
    print(f"{SAY} — code slot listed for every role, {len(agents)} of {len(agents)}")
    return 0


def run_plant(plant, extra) -> int:
    """One plant: its tree in a scratch directory, the verb the plant names over it, its exit returned."""
    import shutil
    import stat
    import tempfile
    for k in [k for k in os.environ if k.startswith("GIT_")]:
        del os.environ[k]
    top = tempfile.mkdtemp(prefix="loadsets-")
    try:
        root, manifest = build_plant_tree(top, plant)
        base = ["--root", str(root)]
        if plant in ("role-unregistered", "role-registered", "code-refused"):
            return main(["derive", "--reader", "role.gov-builder", "--units", str(manifest), *base, *extra])
        if plant == "code-every-role":
            return run_code_every_role(root, manifest)
        if plant in ("code-over", "code-at"):
            budget = read_code_slot(str(root))["budget"]
            size = budget + 1 if plant == "code-over" else budget
            return main(["check", "--load-point", f"{CODE_SLOT}={size}", *base, *extra])
        if plant == "code-refused-check":
            return main(["check", "--load-point", f"{CODE_SLOT}=1", *base, *extra])
        if plant.startswith("feature"):
            import instruction_units as iu
            units = iu.parse_unit_rows(manifest.read_text(encoding="utf-8"), manifest.as_posix())[0]
            tags, report = derive_load_set(units, EVERY, None, ("feature.roles",), read_namespace_rows(root))
            print(f"{SAY} — feature.roles · selected: {', '.join(tags) or 'none'}")
            print("\n".join(report))
            return 0
        if plant == "charter-over":
            return main(["check", "--load-point", "AGENTS.md", *base, *extra])
        if plant == "role-block-over":
            ceiling = read_body_ceiling("gov-builder")
            if ceiling is None:
                print(f"{SAY} — plant role-block-over: no BODY_CEILINGS row for gov-builder")
                return 2
            return main(["check", "--load-point", f"role.gov-builder={ceiling + 10}", *base, *extra])
        rc = main(["check", "--reader", "role.gov-builder", "--units", str(manifest), *base, *extra])
        if rc == 1:
            from policy_value import resolve_kit_dir
            handoff = resolve_kit_dir("roles", "handoff.py", KIT_DIR) / "handoff.py"
            p = subprocess.run([sys.executable, str(handoff), "render", "--role", "gov-builder", "--build", "bx",
                                "--unit", "PLAY-bx-1", "--input", "spec=AGENTS.md"], cwd=str(root),
                               capture_output=True, text=True, encoding="utf-8", errors="replace",
                               stdin=subprocess.DEVNULL, timeout=120)
            prompts = list((root / "memory" / "builds" / "bx" / "prompts").glob("*.md"))
            said = (p.stderr.strip().splitlines() or ["(nothing)"])[0]
            print(f"handoff: exit {p.returncode} · {said}")
            print("handoff: WROTE a prompt file" if prompts else "handoff: no prompt file written")
            if prompts or p.returncode == 0:
                return 3
        return rc
    finally:
        def remove_readonly(fn, path, _exc):
            os.chmod(path, stat.S_IWRITE)
            fn(path)
        shutil.rmtree(top, onerror=remove_readonly)


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    if argv[:1] == ["--fixture"]:
        if argv[1:2] != ["--plant"] or len(argv) < 3 or argv[2] not in PLANTS:
            print(f"usage: load_sets.py --fixture --plant {{{','.join(PLANTS)}}} [<flags>]", file=sys.stderr)
            return 2
        return run_plant(argv[2], argv[3:])
    ap = argparse.ArgumentParser(prog="load_sets.py", description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="verb", required=True)
    for verb in ("derive", "check", "injected"):
        p = sub.add_parser(verb)
        p.add_argument("--root", default=".")
    d, c, i = sub.choices["derive"], sub.choices["check"], sub.choices["injected"]
    d.add_argument("--reader", required=True)
    for p in (d, c):
        p.add_argument("--item")
        p.add_argument("--units")
    d.add_argument("--feature", action="append", default=[])
    d.add_argument("--code-budget")
    c.add_argument("--reader", action="append", default=[])
    c.add_argument("--checks", choices=CHECK_MODES)
    c.add_argument("--load-point", action="append", default=[])
    c.add_argument("--budgets-enforce", choices=("refuse", "warn"))
    c.add_argument("--reach", action="store_true")
    i.add_argument("--card")
    i.add_argument("--cap", action="append", default=[])
    a = ap.parse_args(argv)
    if a.verb == "injected":
        caps = {}
        for spec in a.cap:
            name, _eq, n = spec.partition("=")
            if not n.isdigit():
                ap.error(f"--cap {spec}: give <name>=<bytes>")
            caps[name] = int(n)
        print("\n".join(measure_injected(a.root, a.card, caps)))
        return 0
    return run_derive(a) if a.verb == "derive" else run_check(a)


if __name__ == "__main__":
    sys.exit(main())
