#!/usr/bin/env python3
"""leg_factory.py — the leg manifest, rendered from each leg's ONE declaration (TOOL-dWitnessedBar-11).

    python <this kit>/leg_factory.py --write      # render <tool root>/gate-legs.json from the declarations
    python <this kit>/leg_factory.py --check      # exit 1 naming each leg the file holds differently
    python <this kit>/leg_factory.py --conform    # --check, then every field arm over every declaration
    python <this kit>/leg_factory.py --list       # one line per declaration and the file declaring it
    python <this kit>/leg_factory.py new <name> --kit <id> --argv <json> --subject <kit|repo>
                                      --purpose <text> --enforces <tag> [--enforces <tag>]
                                      [--tests <tag>] [--guard <json>] [--stage <step>]
                                      [--chunk <name>] [--ceiling <seconds>]
    python <this kit>/leg_factory.py new <name> --exempt <why> --argv <json> ...   # a registry row
    python <this kit>/leg_factory.py --selftest   # each arm's failing case, in a scratch tree

ONE DECLARATION PER LEG. A leg an adopter receives is a `[[gate_leg]]` row of its kit's descriptor;
any other leg is an `[[exempt_leg]]` row of the deployer's registry, carrying its whole row beside its
`why`. A descriptor row is what an adopter receives, through the deployer's emitter and its floors;
where gov's own run differs, gov's value sits under the row's `[gate_leg.gov]` sub-table, key by key,
which the emitter never reads. The manifest is generated: hand-editing it ends, and a red names the
declaration to edit.

THE RENDER, per declaration, in order of its declaring file's path and then its row order, the
registry's rows last:
  1. the row's keys that are members of `LEG_KEYS`, the canary's one key set;
  2. each key of `[gate_leg.gov]` overlaid; an empty list there removes the key from gov's row;
  3. `{kit}` resolved to `{prefix}/<home>` (`{prefix}` where the home is the tool root) and
     `{memory_root}` to this tree's memory root; `{prefix}` stays, and any other token is a refusal;
  4. JSON, two-space indent, `name` first and the other keys in KEY_ORDER, UTF-8, one trailing LF;
  5. `pass_leg`, which `pass_legs.py` derives: its rule and its render, never re-stated here.
After the declarations, each runner adapter's rows (TOOL-dWitnessedBar-9 S4): a descriptor's
`[[test_runner]]` row, its `detect` run in the tree, one row per level it names, under the rule and
the `tests.product` value `product_tests.py` beside this file owns; a name a declaration holds is a
finding, never a second row.
The file written is the manifest beside the tool root, never one `$GATE_LEGS` names.

WHERE GOVKIT IS ABSENT, as in every adopter (TOOL-dWitnessedBar-45): the module still loads, since it
imports govkit only inside the verbs that render. `--write`, `--check`, `--list` and `new` exit 2 with
the lookup's line naming the places looked. `--conform` reads the tree's descriptors through
`regen.py`'s reader and grades every field arm over their `[[gate_leg]]` rows, and prints `fresh` and
`enforces` as not graded here: the render and the registries both arms read are gov's.

EXIT 0 clean · 1 a finding (`--check`, `--conform`, a failed selftest) · 2 a refusal: a declaration
that does not parse, a token left unresolved, an empty population, or a sibling kit not found.

WHAT IT DOES NOT CHECK. Whether a leg's `enforces` names the rule the leg actually enforces: the
tags are read against their cites by a person. Whether gov's `[gate_leg.gov]` value is RIGHT: the
sub-table states the difference where a reviewer reads it, and nothing compares it with a run.
"""
import argparse
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib

HERE = pathlib.Path(os.path.abspath(__file__)).parent
# NO GOVKIT AT LOAD (TOOL-dWitnessedBar-45 S2): the module imports the standard library and this kit's
# shipped siblings alone, so it loads in an adopter's tree; govkit is loaded inside the gov verbs.
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import regen  # noqa: E402 - this kit's own descriptor reader and token resolver, standard library only
SAY = "leg-factory"
# `purpose := at most 60 characters` (TOOL-dWitnessedBar-19 S2, §8 F3), CHARACTERS and never bytes.
# Moved whole from govkit (TOOL-dWitnessedBar-11 §8 F8): read by the `purpose` arm and by `new`.
PURPOSE_MAX_CHARS = 60
# Sibling kits' directory names, spelled once so no literal kit path ships (the install-prefix ban).
GOVKIT_HOME = "govkit"  # the deployer kit's directory name, as the policy kit's DEPLOYER_HOME spells it
PLAYBOOK_HOME = "playbook"
RUN_GATES_HOME = "run-gates"
# The manifest's own key order, the one its rows were written in, `name` first.
KEY_ORDER = ("name", "pass_leg", "tag", "tests", "purpose", "argv", "scope_of", "reads", "signature",
             "guard", "impure", "chunk", "subject", "ceiling", "doc_reads", "pack", "level", "enforces", "stage")
SUBJECTS = ("kit", "repo")
# The read classes the runner's reader admits (run-gates.sh, its `reads` reader).
READ_CLASSES = ("history", "base", "clock", "remote")
TOKEN_RX = re.compile(r"\{([a-z_]+)\}")
TAG_MAX_BYTES = 64


class Refusal(Exception):
    """Exit 2, nothing written."""


# The sibling-kit resolver, INLINED byte-identically from the canonical copy named on its marker
# line and gated by the resolve-python self-test.
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


def load_govkit():
    """The deployer module, whose registry and descriptor readers and token resolver the render uses."""
    try:
        gk = resolve_kit_dir("govkit", "govkit.py", HERE)
    except LookupError as e:
        raise Refusal(str(e)) from None
    if str(gk) not in sys.path:
        sys.path.insert(0, str(gk))
    import govkit  # noqa: PLC0415
    return govkit


def load_pass_legs():
    """This kit's own `pass_legs` module: the pass-leg rule and its render (§8 F7)."""
    import pass_legs  # noqa: PLC0415
    return pass_legs


def derive_repo_root():
    """The tree this kit sits in, by walking for `.git` rather than asking git (a hook's GIT_DIR)."""
    root = next((d for d in (HERE, *HERE.parents) if (d / ".git").exists()), None)
    if root is None:
        raise Refusal(f"no repository holds {HERE.as_posix()}, so there is no tree to render")
    return root


def read_layout(root, G):
    """(tool root relative to `root`, memory root) of the tree at `root`."""
    tool_rel = G.derive_tool_root(root)
    mem = "memory"
    conf = pathlib.Path(root, ".memory-tree.conf")
    if conf.is_file():
        for raw in conf.read_text(encoding="utf-8").splitlines():
            m = re.match(r'^\s*(?:export\s+)?MEMORY_ROOT=["\']?([^"\'\s]+)', raw)
            if m:
                mem = m.group(1)
    return tool_rel, mem


def read_leg_keys(root, tool_rel):
    """`LEG_KEYS`, the one leg-row key set, from the canary beside this kit (TOOL-dWitnessedBar-12 S4)."""
    canary = pathlib.Path(root, tool_rel, HERE.name, "run-gates.test.sh")
    if not canary.is_file():
        raise Refusal(f"{canary.as_posix()} is absent, so no key set bounds a declaration")
    for ln in canary.read_text(encoding="utf-8").splitlines():
        m = re.match(r'^LEG_KEYS="([^"]*)"', ln)
        if m:
            return set(m.group(1).split())
    raise Refusal(f"{canary.as_posix()} holds no LEG_KEYS line, so no key set bounds a declaration")


def derive_kit_spelling(desc, tool_rel):
    """What `{kit}` resolves to in gov's row: `{prefix}/<home>`, `{prefix}` where the home is the tool
    root, and a root-relative home as it is spelled."""
    home = str(desc.get("home") or ".").strip("/")
    if desc.get("home_root_relative"):
        return home
    if home in ("", ".", tool_rel):
        return "{prefix}"
    if tool_rel and home.startswith(tool_rel + "/"):
        return "{prefix}/" + home[len(tool_rel) + 1:]
    return "{prefix}/" + home


def read_declarations(root, G):
    """Every declaration, in render order: [{name, file, kind, eid, base, gov, why, kit}]."""
    reg = G.load_registry(root)
    rep = G.Report()
    descs = G.read_descriptors(root, reg, rep)
    if rep.problems:
        raise Refusal("; ".join(rep.problems))
    tool_rel = G.derive_tool_root(root)
    out, seen = [], set()
    for eid, (d, dpath) in sorted(descs.items(), key=lambda kv: (kv[1][1], kv[0])):
        if dpath in seen:
            continue
        seen.add(dpath)
        for leg in d.get("gate_leg", []) or []:
            gov = leg.get("gov") if isinstance(leg.get("gov"), dict) else {}
            out.append({"name": leg.get("name"), "file": dpath, "kind": "claimed", "eid": eid,
                        "base": {k: v for k, v in leg.items() if k != "gov"}, "gov": gov, "why": None,
                        "kit": derive_kit_spelling(d, tool_rel)})
    reg_rel = pathlib.Path(G.derive_registry_path(root)).relative_to(root).as_posix()
    for x in reg.get("exempt_leg", []) or []:
        out.append({"name": x.get("name"), "file": reg_rel, "kind": "exempt", "eid": None,
                    "base": {k: v for k, v in x.items() if k != "why"}, "gov": {},
                    "why": x.get("why"), "kit": "{prefix}"})
    if not out:
        raise Refusal("no declaration found: an empty population is refused, never rendered as []")
    return out


def read_adopter_declarations(root, tool_rel):
    """(every `[[gate_leg]]` row of this tree's descriptors as a declaration, [(arm, leg, message)]) in a
    tree with no govkit (TOOL-dWitnessedBar-45 S3): read through `regen.read_descriptors`, each argv
    resolved through `regen.resolve_argv`. The registry's `[[exempt_leg]]` rows and the flat entries'
    descriptors under the playbook kit are not read, since that reader reads `*/kit.toml` alone."""
    mem = regen.read_conf_value(pathlib.Path(root, ".memory-tree.conf"), "MEMORY_ROOT") or "memory"
    mapr = regen.read_conf_value(pathlib.Path(root, ".codebase-map.conf"), "MAP_ROOT")
    out, found = [], []
    for kit_rel, d in regen.read_descriptors(pathlib.Path(root), tool_rel):
        dpath = f"{kit_rel}/kit.toml"
        ctx = {"kit": kit_rel, "prefix": tool_rel or ".", "memory_root": mem,
               "map_root": "memory/map" if mapr is None else mapr}
        for leg in d.get("gate_leg", []) or []:
            nm = leg.get("name")
            if "pass_leg" in leg:
                found.append(("derived", nm, f"{dpath} declares `pass_leg` on leg {nm!r}: the field is "
                                             f"derived by pass_legs.py at the render, never declared"))
            try:
                regen.resolve_argv(leg.get("argv"), ctx, f"{dpath} leg {nm!r}")
            except regen.Refusal as e:
                found.append(("token", nm, str(e)))
            gov = leg.get("gov") if isinstance(leg.get("gov"), dict) else {}
            out.append({"name": nm, "file": dpath, "kind": "claimed", "eid": d.get("id"),
                        "base": {k: v for k, v in leg.items() if k != "gov"}, "gov": gov, "why": None,
                        "kit": kit_rel})
    if not out:
        raise Refusal("no [[gate_leg]] row found: an empty population is refused, never graded as green")
    return out, found


def resolve_row_tokens(value, ctx, left):
    """`value` with `{kit}` and `{memory_root}` resolved; every other token but `{prefix}` into `left`."""
    if isinstance(value, str):
        for k, v in ctx.items():
            value = value.replace("{" + k + "}", v)
        left.extend(t for t in TOKEN_RX.findall(value) if t != "prefix")
        return value
    if isinstance(value, list):
        return [resolve_row_tokens(x, ctx, left) for x in value]
    if isinstance(value, dict):
        return {k: resolve_row_tokens(x, ctx, left) for k, x in value.items()}
    return value


def render_rows(root, G, decls=None):
    """(gov's manifest rows without `pass_leg`, [(arm, leg, message)]) from the declarations."""
    decls = read_declarations(root, G) if decls is None else decls
    tool_rel, mem = read_layout(root, G)
    keys = read_leg_keys(root, tool_rel)
    rows, found = [], []
    for dc in decls:
        nm = dc["name"]
        if "pass_leg" in dc["base"] or "pass_leg" in dc["gov"]:
            found.append(("derived", nm, f"{dc['file']} declares `pass_leg` on leg {nm!r}: the field is "
                                         f"derived by pass_legs.py at the render, never declared"))
        row = {k: v for k, v in dc["base"].items() if k in keys and k != "pass_leg"}
        for k, v in dc["gov"].items():
            if k not in keys or k == "pass_leg":
                if k != "pass_leg":
                    found.append(("token", nm, f"{dc['file']} leg {nm!r}: its [gate_leg.gov] key {k!r} is "
                                               f"no member of LEG_KEYS, so it reaches no manifest row"))
                continue
            if v == []:
                row.pop(k, None)
            else:
                row[k] = v
        left = []
        row = resolve_row_tokens(row, {"kit": dc["kit"], "memory_root": mem}, left)
        for t in sorted(set(left)):
            found.append(("token", nm, f"{dc['file']} leg {nm!r}: gov's row still carries {{{t}}} after "
                                       f"rendering — spell gov's own value under [gate_leg.gov]"))
        rows.append(row)
    taken = {r.get("name") for r in rows}
    for a in derive_runner_rows(root, G, tool_rel):
        if a["name"] in taken:
            found.append(("one declaration", a["name"], f"leg {a['name']!r} is declared and is also a runner "
                                                        f"adapter's row: one leg, one declaration"))
            continue
        rows.append(a)
    rank = {k: i for i, k in enumerate(KEY_ORDER)}
    return [{k: r[k] for k in sorted(r, key=lambda k: (rank.get(k, len(rank)), k))} for r in rows], found


def derive_runner_rows(root, G, tool_rel):
    """The runner adapters' rows of this tree's manifest (TOOL-dWitnessedBar-9 S4), from
    `product_tests.derive_product_rows`: every `[[test_runner]]` row of the descriptors, its `detect`
    run first, and `tests.product` read only where one names a level, so a tree no runner detects
    spends no policy read. `{kit}` is spelled as gov's own rows spell it."""
    import product_tests  # noqa: PLC0415 - the contract, read only by the render
    reg = G.load_registry(root)
    rep = G.Report()
    descs = G.read_descriptors(root, reg, rep)
    if rep.problems:
        raise Refusal("; ".join(rep.problems))
    runners, seen = [], set()
    for _eid, (d, dpath) in sorted(descs.items(), key=lambda kv: (kv[1][1], kv[0])):
        if dpath in seen:
            continue
        seen.add(dpath)
        for r in d.get("test_runner") or []:
            r = product_tests.check_runner(dict(r), dpath)
            runners.append(dict(r, kit=derive_kit_spelling(d, tool_rel), kit_dir=pathlib.Path(root, dpath).parent,
                                file=dpath))
    if not runners:
        return []
    detected = product_tests.read_detected(root, runners)
    if not any(detected.values()):
        return []
    value, _where = product_tests.read_product_value(root)
    return product_tests.derive_product_rows(root, value, runners, [], detected)


def render_manifest(rows):
    """The manifest's text: the rows as JSON, then `pass_leg` from pass_legs.py's own rule and render."""
    pl = load_pass_legs()
    text = json.dumps(rows, indent=2, ensure_ascii=False) + "\n"
    evidence = pl.read_pass_evidence()
    ranked = pl.derive_pass_legs(rows, evidence[1] if evidence else {}, pl.read_ceilings())
    try:
        return pl.render_pass_field(text, [r["name"] for r in ranked if r["verdict"] == "selected"])
    except pl.Refusal as e:
        raise Refusal(str(e)) from None


def read_manifest(path):
    """(text with LF line ends, parsed rows), or (None, None) where the file is absent."""
    p = pathlib.Path(path)
    if not p.is_file():
        return None, None
    text = p.read_bytes().decode("utf-8").replace("\r\n", "\n")
    try:
        return text, json.loads(text)
    except ValueError:
        return text, None


def derive_drift(cur_text, cur_rows, new_text):
    """One line per leg the file holds differently from the render: added, dropped or changed, and how."""
    if cur_text == new_text:
        return []
    if cur_rows is None:
        return ["the manifest is absent or does not parse as JSON"]
    new_rows = json.loads(new_text)
    have = {r.get("name"): r for r in cur_rows if isinstance(r, dict)}
    want = {r["name"]: r for r in new_rows}
    out = [f"leg {n!r} added: a declaration renders it and the manifest lacks it" for n in want if n not in have]
    out += [f"leg {n!r} dropped: the manifest holds it and no declaration renders it" for n in have
            if n not in want]
    for n in want:
        if n in have and have[n] != want[n]:
            ks = sorted(k for k in set(have[n]) | set(want[n]) if have[n].get(k) != want[n].get(k))
            out.append(f"leg {n!r} changed: {', '.join(ks)} differ from the render")
    if not out:
        out.append("the rows agree and the bytes do not: the order or the formatting was edited by hand")
    return out


def read_enforce_population(root, tool_rel):
    """(every tag a leg may enforce, the legs the pending list excuses) from the playbook kit, or None."""
    try:
        pk = resolve_kit_dir("playbook", "kinds.toml", pathlib.Path(root, tool_rel or ".", HERE.name))
    except LookupError:
        return None
    if pathlib.Path(root).resolve() not in pk.resolve().parents:
        return None
    tags = set()
    for name, table in (("principles.toml", "principle"), ("practices.toml", "practice")):
        p = pk / name
        if not p.is_file():
            continue
        try:
            data = tomllib.loads(p.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as e:
            raise Refusal(f"{p.as_posix()} does not parse: {e}") from None
        for row in data.get(table) or []:
            t = row.get("tag") if isinstance(row, dict) else None
            if isinstance(t, str):
                tags.add(t)
                tags.update(f"{t}.{r}" for r in row.get("rules") or [] if isinstance(r, str))
    pending = set()
    pp = pk / "core-pending.txt"
    if pp.is_file():
        for ln in pp.read_text(encoding="utf-8").splitlines():
            cells = ln.split("\t")
            if len(cells) == 3 and cells[0] == "leg":
                pending.add(cells[1])
    return tags, pending


def derive_held(row):
    """Whether the runner holds this manifest row by the row alone: subject `kit` or chunk `selftests`,
    the `kit` source of run-gates.sh's `derive_hold_source`."""
    return row.get("subject") == "kit" or row.get("chunk") == "selftests"


def measure_held(rows):
    """(held, unguarded): the rows the `kit` source holds, and those of them with no guard."""
    held = [r for r in rows if derive_held(r)]
    return len(held), sum(1 for r in held if not r.get("guard"))


def check_declarations(decls, rows):
    """[(arm, leg, message)] for every field arm of §4 "The gate" but `fresh`, `token` and `enforces`."""
    found = []
    by_name = {}
    for dc in decls:
        nm = dc["name"]
        if not isinstance(nm, str) or not nm:
            found.append(("name", str(nm), f"{dc['file']} declares a leg with no name"))
            continue
        if nm in by_name:
            found.append(("one declaration", nm, f"leg {nm!r} is declared in {by_name[nm]} and again in "
                                                 f"{dc['file']}: one leg, one declaration"))
        by_name.setdefault(nm, dc["file"])
        if dc["kind"] == "exempt" and not str(dc["why"] or "").strip():
            found.append(("exempt reason", nm, f"[[exempt_leg]] {nm!r} carries an empty why: an exemption "
                                               f"without a reason is an omission wearing a label"))
        if re.search(r"\([^)]*\d[^)]*\)", nm):
            found.append(("name", nm, f"leg {nm!r} carries a digit-bearing parenthetical: a count in a "
                                      f"leg name goes stale where nobody is reading"))
        for side, src in (("its row", dc["base"]), ("[gate_leg.gov]", dc["gov"])):
            if side == "its row" or "subject" in src:
                sub = src.get("subject")
                if sub not in SUBJECTS:
                    found.append(("subject", nm, f"leg {nm!r} declares subject {sub!r} in {side} of "
                                                 f"{dc['file']}: absent or outside kit|repo"))
            if "ceiling" in src:
                ce = src["ceiling"]
                if isinstance(ce, bool) or not isinstance(ce, int) or ce <= 0:
                    found.append(("ceiling", nm, f"leg {nm!r} declares ceiling {ce!r} in {side}: a "
                                                 f"ceiling is a positive integer, a bool included"))
            if "reads" in src:
                rd = src["reads"]
                bad = sorted(set(rd) - set(READ_CLASSES)) if isinstance(rd, dict) else [repr(rd)]
                if bad:
                    found.append(("reads", nm, f"leg {nm!r} declares the read class(es) {', '.join(bad)} "
                                               f"in {side}, outside {'|'.join(READ_CLASSES)}"))
    # THE `held guard` ARM (TOOL-dWitnessedBar-5 S8): a leg the runner holds by its row, the `kit` source
    # of `derive_hold_source`, runs under `GATE_SELFTESTS=1` whole where it has no guard. That choice is
    # declared: a non-empty `guard` on the row the runner reads, or a descriptor-only `unguarded_why`
    # naming why it runs whole, never both. `unguarded_why` is no member of LEG_KEYS, so it never
    # reaches a rendered row or an adopter. The row graded is the one this tree's runner reads: gov's
    # render here, the declaration's own row in an adopter (`run_conform_adopter`). A declaration whose
    # guard is split, set on its row and cleared by `[gate_leg.gov]` or the reverse, runs unguarded in
    # one of the two forms, so its reason is true there: "both" is a guard in EVERY form beside a reason.
    by_row = {r.get("name"): r for r in rows}
    for dc in decls:
        nm, row = dc["name"], by_row.get(dc["name"])
        if not isinstance(nm, str) or row is None or not derive_held(row):
            continue
        why = dc["base"].get("unguarded_why")
        own_guard = dc["base"].get("guard")
        gov_guard = dc["gov"]["guard"] if "guard" in dc["gov"] else own_guard
        if own_guard and gov_guard and "unguarded_why" in dc["base"]:
            found.append(("held guard", nm, f"held leg {nm!r} in {dc['file']} carries a guard in every form "
                                            f"and an unguarded_why: it is guarded, so the reason is false"))
        elif not row.get("guard") and not (isinstance(why, str) and why.strip()):
            found.append(("held guard", nm, f"held leg {nm!r} in {dc['file']} carries neither a guard nor a "
                                            f"non-empty unguarded_why: declare the guard that skips it when "
                                            f"nothing it reads moved, or why it runs whole under GATE_SELFTESTS"))
    # THE `purpose presence` ARM (TOOL-dWitnessedBar-51 S8): every leg says what it is for, so a row with
    # no `purpose` reds by name; no pending population excuses one, since every row carries the key.
    purposes = {}
    for row in rows:
        nm = row["name"]
        if "purpose" not in row:
            found.append(("purpose presence", nm, f"leg {nm!r} carries no purpose: every leg declares one "
                                                  f"line saying what it is for"))
            continue
        pu = row["purpose"]
        if not isinstance(pu, str):
            found.append(("purpose", nm, f"leg {nm!r} carries purpose {pu!r}, which is not a string"))
            continue
        if not pu or len(pu) > PURPOSE_MAX_CHARS or "\n" in pu or "\r" in pu or pu != pu.strip():
            found.append(("purpose", nm, f"leg {nm!r} carries purpose {pu!r} ({len(pu)} characters): one "
                                         f"line of 1 to {PURPOSE_MAX_CHARS} characters with no edge space"))
        purposes.setdefault(pu, []).append(nm)
    for pu, nms in sorted(purposes.items()):
        if len(nms) > 1:
            found.append(("purpose", nms[0], f"legs {', '.join(repr(x) for x in nms)} share the purpose "
                                             f"{pu!r}: two legs, one purpose, says what a feature is for"))
    return found


def check_enforces(root, tool_rel, rows):
    """[(arm, leg, message)] for the `enforces` arm, gov's: graded against the playbook kit's registries
    and its pending list; nothing where no playbook kit sits in the tree."""
    found = []
    pop = read_enforce_population(root, tool_rel)
    if pop is not None:
        tags, pending = pop
        for row in rows:
            nm, enf = row["name"], row.get("enforces")
            if not enf and nm not in pending:
                found.append(("enforces", nm, f"leg {nm!r} enforces nothing and no `leg` row of "
                                              f"core-pending.txt excuses it"))
            for t in enf or []:
                if t not in tags:
                    found.append(("enforces", nm, f"leg {nm!r} enforces {t!r}, which no principle row, "
                                                  f"practice row or practice rule holds"))
    return found


def render_toml_value(v):
    """`v` spelled as a TOML value: strings JSON-escaped, which TOML's basic strings read alike."""
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, str):
        return json.dumps(v, ensure_ascii=False)
    if isinstance(v, list):
        one = "[" + ", ".join(render_toml_value(x) for x in v) + "]"
        if len(one) <= 100:
            return one
        return "[\n" + "".join(f"  {render_toml_value(x)},\n" for x in v) + "]"
    if isinstance(v, dict):
        return "{ " + ", ".join(f"{k if re.fullmatch(r'[A-Za-z0-9_-]+', k) else json.dumps(k)} = "
                                f"{render_toml_value(x)}" for k, x in v.items()) + " }"
    raise Refusal(f"{v!r} has no TOML spelling here")


def derive_leg_tag(owner, name, root, tool_rel):
    """`leg.<owner>.<name>` by TOOL-dWitnessedBar-12's rule: `-kit` after an owner that is a namespace
    word, the name folded to lower-case hyphenated segments, cut at its last hyphen within 64 bytes."""
    ns = pathlib.Path(root, tool_rel or ".", PLAYBOOK_HOME, "namespaces.toml")
    words = set()
    if ns.is_file():
        words = {r.get("ns") for r in tomllib.loads(ns.read_text(encoding="utf-8")).get("namespace") or []}
    own = f"{owner}-kit" if owner in words else owner
    tag = f"leg.{own}.{re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')}"
    if len(tag.encode("utf-8")) > TAG_MAX_BYTES:
        tag = tag.encode("utf-8")[:TAG_MAX_BYTES].decode("utf-8", "ignore")
        tag = tag[:tag.rfind("-")] if tag.rfind("-") > len(f"leg.{own}.") else tag
    return tag


def write_declaration(path, header, row, gov):
    """Append one declaration to the TOML file at `path`: `header`, its keys, then its gov sub-table."""
    p = pathlib.Path(path)
    text = p.read_bytes().decode("utf-8").replace("\r\n", "\n")
    block = f"\n{header}\n" + "".join(f"{k} = {render_toml_value(v)}\n" for k, v in row.items())
    if gov:
        block += "\n[gate_leg.gov]\n" + "".join(f"{k} = {render_toml_value(v)}\n" for k, v in gov.items())
    p.write_bytes((text.rstrip("\n") + "\n" + block).encode("utf-8"))


# ---------------------------------------------------------------------------------------------- verbs
def run_write(root):
    G = load_govkit()
    rows, found = render_rows(root, G)
    refused = [m for a, _n, m in found if a in ("token", "derived")]
    if refused:
        return 2, [f"{SAY}: refused · {m}" for m in refused]
    tool_rel, _mem = read_layout(root, G)
    path = pathlib.Path(root, tool_rel, "gate-legs.json")
    new = render_manifest(rows)
    cur, _r = read_manifest(path)
    if cur != new:
        path.write_bytes(new.encode("utf-8"))
        return 0, [f"{SAY}: wrote {len(rows)} legs to {pathlib.Path(tool_rel, 'gate-legs.json').as_posix()}"]
    return 0, [f"{SAY}: {len(rows)} legs, the manifest already fresh"]


def run_check(root):
    G = load_govkit()
    rows, found = render_rows(root, G)
    refused = [m for a, _n, m in found if a in ("token", "derived")]
    if refused:
        return 2, [f"{SAY}: refused · {m}" for m in refused]
    tool_rel, _mem = read_layout(root, G)
    cur_text, cur_rows = read_manifest(pathlib.Path(root, tool_rel, "gate-legs.json"))
    drift = derive_drift(cur_text, cur_rows, render_manifest(rows))
    if drift:
        return 1, [f"{SAY}: fresh · {d}" for d in drift] + [
            f"{SAY}: the manifest is generated — edit the declaration, then `leg_factory.py --write`"]
    return 0, [f"{SAY}: fresh · {len(rows)} legs, the manifest is what --write renders"]


def run_conform_adopter(root):
    """`--conform` in a tree with no govkit (TOOL-dWitnessedBar-45 S3, §8 F4): every field arm over the
    `[[gate_leg]]` rows of this tree's descriptors; `fresh` and `enforces` are gov's and named ungraded."""
    tool_rel = pathlib.Path(os.path.relpath(HERE.parent, root)).as_posix()
    tool_rel = "" if tool_rel == "." else tool_rel
    decls, found = read_adopter_declarations(root, tool_rel)
    rows = [dict(dc["base"], name=dc["name"]) for dc in decls]
    found += check_declarations(decls, rows)
    held, unguarded = measure_held(rows)
    lines = [f"{SAY}: {arm} · {m}" for arm, _n, m in found]
    lines += [f"{SAY}: fresh: not graded here — no govkit", f"{SAY}: enforces: not graded here — no govkit",
              f"legs: {len(decls)} declared · {len(decls)} claimed · the registry's exempt rows are not "
              f"read here — no govkit · {held} held · {unguarded} unguarded"]
    rc = 1 if found else 0
    lines.append(f"{SAY}: conform · {'red' if rc else 'green'}")
    return rc, lines


def run_conform(root):
    try:
        resolve_kit_dir(GOVKIT_HOME, "govkit.py", HERE)
    except LookupError:
        return run_conform_adopter(root)
    G = load_govkit()
    decls = read_declarations(root, G)
    rows, found = render_rows(root, G, decls)
    tool_rel, _mem = read_layout(root, G)
    cur_text, cur_rows = read_manifest(pathlib.Path(root, tool_rel, "gate-legs.json"))
    lines = [f"{SAY}: fresh · {d}" for d in derive_drift(cur_text, cur_rows, render_manifest(rows))]
    found += check_declarations(decls, rows) + check_enforces(root, tool_rel, rows)
    lines += [f"{SAY}: {arm} · {m}" for arm, _n, m in found]
    pop = read_enforce_population(root, tool_rel)
    pend = len(pop[1]) if pop else 0
    if pop is None:
        lines.append(f"{SAY}: enforces · unarmed: no playbook kit in this tree, so no tag is graded")
    claimed = sum(1 for d in decls if d["kind"] == "claimed")
    held, unguarded = measure_held(rows)
    lines.append(f"legs: {len(decls)} declared · {claimed} claimed · {len(decls) - claimed} exempt · "
                 f"{pend} enforces-pending · {held} held · {unguarded} unguarded")
    rc = 1 if len(lines) > 1 + (pop is None) else 0
    lines.append(f"{SAY}: conform · {'red' if rc else 'green'}")
    return rc, lines


def run_list(root):
    G = load_govkit()
    return 0, [f"{d['name']}\t{d['file']}" for d in read_declarations(root, G)]


def run_new(root, a):
    G = load_govkit()
    decls = read_declarations(root, G)
    tool_rel, _mem = read_layout(root, G)
    bad = []
    nm = a.name
    if not nm or re.search(r"\([^)]*\d[^)]*\)", nm):
        bad.append(f"name {nm!r} is empty or carries a digit-bearing parenthetical")
    if any(d["name"] == nm for d in decls):
        bad.append(f"leg {nm!r} is declared already")
    if (a.kit is None) == (a.exempt is None):
        bad.append("name exactly one of --kit <id> and --exempt <why>")
    if a.exempt is not None and not a.exempt.strip():
        bad.append("--exempt carries an empty why")
    if a.subject not in SUBJECTS:
        bad.append(f"--subject {a.subject!r} is outside kit|repo")
    pu = a.purpose
    if pu is None:
        bad.append("--purpose is required: a leg says what it is for")
    elif not pu or len(pu) > PURPOSE_MAX_CHARS or "\n" in pu or "\r" in pu or pu != pu.strip():
        bad.append(f"--purpose {pu!r} is not one line of 1 to {PURPOSE_MAX_CHARS} characters")
    elif any(d["base"].get("purpose") == pu or d["gov"].get("purpose") == pu for d in decls):
        bad.append(f"--purpose {pu!r} is another leg's purpose already")
    pop = read_enforce_population(root, tool_rel)
    if not a.enforces:
        bad.append("--enforces is required: a new leg has no pending row to excuse it")
    elif pop is not None:
        bad += [f"--enforces {t!r} names no principle row, practice row or practice rule"
                for t in a.enforces if t not in pop[0]]
    lists = {}
    for flag, val in (("argv", a.argv), ("guard", a.guard)):
        if val is None:
            continue
        try:
            lists[flag] = json.loads(val)
        except ValueError:
            lists[flag] = None
        if not (isinstance(lists[flag], list) and all(isinstance(x, str) and x for x in lists[flag])
                and (lists[flag] or flag == "guard")):
            bad.append(f"--{flag} {val!r} is not a JSON list of non-empty strings")
    if a.argv is None:
        bad.append("--argv is required")
    if a.ceiling is not None and a.ceiling <= 0:
        bad.append(f"--ceiling {a.ceiling} is not a positive integer")
    path = None
    if a.kit is not None:
        reg = G.load_registry(root)
        ent = next((e for e in reg.get("entry", []) if e.get("id") == a.kit), None)
        if ent is None:
            bad.append(f"--kit {a.kit!r} is no entry of the registry")
        else:
            path = pathlib.Path(root, ent["descriptor"])
    left = [t for s in (lists.get("argv") or []) + (lists.get("guard") or [])
            for t in TOKEN_RX.findall(s) if t not in ("prefix", "kit", "memory_root")]
    if left:
        bad.append(f"--argv or --guard carries {{{left[0]}}}, a token gov's own row cannot resolve")
    if bad:
        return 2, [f"{SAY}: refused · {b}" for b in bad] + [f"{SAY}: refused · nothing written"]
    row = {"name": nm, "tag": derive_leg_tag("gov" if a.exempt is not None else a.kit, nm, root, tool_rel)}
    if a.exempt is not None:
        row["why"] = a.exempt
    if a.tests:
        row["tests"] = a.tests
    row.update({"purpose": pu, "argv": lists["argv"]})
    if a.guard is not None:
        row["guard"] = lists["guard"]
    own = {k: v for k, v in (("chunk", a.chunk), ("ceiling", a.ceiling)) if v is not None}
    if a.exempt is not None:
        row.update(own)
        own = {}
    row.update({"subject": a.subject, "enforces": a.enforces})
    if a.stage:
        row["stage"] = a.stage
    if a.exempt is not None:
        path = G.derive_registry_path(root)
        write_declaration(path, "[[exempt_leg]]", row, {})
    else:
        write_declaration(path, "[[gate_leg]]", row, own)
    rc, lines = run_write(root)
    where = pathlib.Path(path).resolve().relative_to(pathlib.Path(root).resolve()).as_posix()
    return rc, [f"{SAY}: new · declared {nm!r} as {row['tag']} in {where}"] + lines


# ------------------------------------------------------------------------------------------- selftest
FIXTURE = {
    ".memory-tree.conf": 'MEMORY_ROOT="mem"\n',
    f"kits/{GOVKIT_HOME}/registry.toml": (
        'version = 1\n\n[[entry]]\nid = "alpha"\ndescriptor = "{prefix}/alpha/kit.toml"\n\n'
        '[[entry]]\nid = "beta"\ndescriptor = "{prefix}/beta/kit.toml"\n\n'
        '[[exempt_leg]]\nname = "gov only leg"\nwhy = "a fixture row gov alone runs"\ntag = "leg.gov.gov-only-leg"\n'
        'purpose = "a gov-only fixture leg"\nargv = ["bash", "{prefix}/gov-only.sh"]\nchunk = "product"\n'
        'subject = "repo"\nceiling = 60\nenforces = ["principle.p1"]\nstage = ["step.test"]\n\n'
        '[[exempt_leg]]\nname = "pending leg"\nwhy = "a fixture row the pending list excuses"\n'
        'tag = "leg.gov.pending-leg"\npurpose = "a fixture leg still pending"\n'
        'argv = ["bash", "{prefix}/pending.sh"]\nchunk = "product"\nsubject = "repo"\nceiling = 60\n'),
    "kits/alpha/kit.toml": (
        'id = "alpha"\nhome = "alpha"\n\n[[gate_leg]]\nname = "alpha check"\ntag = "leg.alpha.alpha-check"\n'
        'tests = ["feature.alpha"]\nsubject = "repo"\npurpose = "checks the alpha fixture"\n'
        'argv = ["python3", "{kit}/check.py", "{memory_root}/rows.txt"]\nguard = ["{kit}/"]\n'
        'doc_reads = ["{memory_root}/doc.md"]\nstage = ["step.test"]\nenforces = ["practice.verify"]\n'
        'ceiling = 30\n\n[gate_leg.gov]\nargv = ["python3", "{kit}/check.py", "{memory_root}/rows.txt", "--gov"]\n'
        'chunk = "product"\nceiling = 90\nguard = []\n'),
    "kits/beta/kit.toml": (
        'id = "beta"\nhome = "beta"\n\n[[gate_leg]]\nname = "beta selftest"\ntag = "leg.beta.beta-selftest"\n'
        'subject = "kit"\npurpose = "arms the beta fixture red and green"\nargv = ["bash", "{kit}/beta.test.sh"]\n'
        'unguarded_why = "a fixture suite with no path to guard"\n'
        'reads = { history = "it reads the log" }\nenforces = ["practice.gate"]\n\n'
        '[gate_leg.gov]\nchunk = "selftests"\nceiling = 120\n'),
    f"kits/{RUN_GATES_HOME}/run-gates.test.sh": f'LEG_KEYS="{" ".join(KEY_ORDER)}"\n',
    f"kits/{PLAYBOOK_HOME}/kinds.toml": "",
    f"kits/{PLAYBOOK_HOME}/namespaces.toml": '[[namespace]]\nns = "leg"\n',
    f"kits/{PLAYBOOK_HOME}/principles.toml": '[[principle]]\ntag = "principle.p1"\nid = "P1"\nline = "One."\n',
    f"kits/{PLAYBOOK_HOME}/practices.toml": ('[[practice]]\ntag = "practice.verify"\nline = "Verify."\n\n'
                                     '[[practice]]\ntag = "practice.gate"\nline = "A gate."\nrules = ["red"]\n'),
    f"kits/{PLAYBOOK_HOME}/core-pending.txt": "# fixture\nleg\tpending leg\tdFx\n",
}


def write_fixture(top):
    """FIXTURE at `top`: two descriptors, a registry and the playbook rows the `enforces` arm reads."""
    for rel, text in FIXTURE.items():
        p = pathlib.Path(top, rel)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(text.encode("utf-8"))


def write_planted(top, rel, old, new):
    """Replace `old`, which must occur once, by `new` in the fixture file `rel`."""
    p = pathlib.Path(top, rel)
    text = p.read_bytes().decode("utf-8")
    if text.count(old) != 1:
        raise AssertionError(f"the plant's anchor {old!r} occurs {text.count(old)} times in {rel}")
    p.write_bytes(text.replace(old, new, 1).encode("utf-8"))


def write_manifest_edit(top, fn):
    """Rewrite the fixture's manifest rows through `fn`, by hand, as a hand-edit would."""
    p = pathlib.Path(top, "kits", "gate-legs.json")
    p.write_bytes((json.dumps(fn(json.loads(p.read_bytes().decode("utf-8"))), indent=2) + "\n").encode("utf-8"))


def check_precommit_trigger(scratch):
    """TOOL-dWitnessedBar-108 S2, §4 "The trigger parity arm": the pre-commit hook's staged list against
    the runner's own `changed` line, for guard `a/` in a scratch repository holding `a/x`, `a/y` and
    `b/z`. Four staged cases, each from a clean reset: a `git rm a/x`, a `git mv a/y b/y`, an edit of
    `a/x` and an edit of `b/z`. The work tree always equals the index, so the runner's work-tree
    compare and the hook's index compare read the same change. -> (cases failed, cases run), one
    `arm ok` or `arm FAIL` line printed per case naming both answers. An absent `changed()` line, or no
    bash, is an `arm FAIL` for every case naming why, never a skip. WHAT IT DOES NOT CHECK: an unstaged
    edit, which the runner counts and the hook never sees by design, and a guard spelled with
    `{prefix}`, which `derive_trigger` resolves before the compare."""
    import precommit  # noqa: PLC0415 - the hook's own lister, this kit's sibling, loaded by this arm alone
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_") and k != "GATE_FULL"}

    def run_git(*args):
        return subprocess.run(["git", "-C", str(scratch), *args], capture_output=True, env=env,
                              stdin=subprocess.DEVNULL, timeout=60)

    def write_edit(rel):
        pathlib.Path(scratch, rel).write_bytes(b"edited\n")
        run_git("add", "--", rel)

    cases = (("remove: a staged git rm a/x", lambda: run_git("rm", "-q", "--", "a/x")),
             ("rename: a staged git mv a/y b/y", lambda: run_git("mv", "a/y", "b/y")),
             ("edit inside: a/x edited and staged", lambda: write_edit("a/x")),
             ("edit outside: b/z edited and staged", lambda: write_edit("b/z")))
    runner = HERE / "run-gates.sh"
    try:
        line = next((ln for ln in runner.read_bytes().decode("utf-8").splitlines()
                     if ln.startswith("changed()")), "")
    except OSError as e:
        line, why = "", f"{runner.as_posix()} could not be read: {e}"
    else:
        why = "" if line else f"{runner.as_posix()} holds no line opening changed()"
    bash, refusal = precommit.resolve_bash_launcher()
    if not why and not bash:
        why = f"no bash runs the runner's changed line: {refusal}"
    if not why:
        scratch.mkdir(parents=True, exist_ok=True)
        for rel in ("a/x", "a/y", "b/z"):
            pathlib.Path(scratch, rel).parent.mkdir(parents=True, exist_ok=True)
            pathlib.Path(scratch, rel).write_bytes(rel.encode("ascii") + b"\n")
        steps = (("init", "-q", "--template="), ("add", "-A"),
                 ("-c", "user.name=fixture", "-c", "user.email=fixture@example.invalid", "-c", "commit.gpgsign=false",
                  "commit", "-q", "--no-verify", "-m", "fixture"))
        for step in steps:
            p = subprocess.run(["git", "-C", str(scratch), *step], capture_output=True, env=env,
                               stdin=subprocess.DEVNULL, timeout=60)
            if p.returncode:
                why = f"the scratch repository's git {step[0]} exited {p.returncode}"
                break

    def read_runner_verdict(guard):
        """True where the runner's `changed` line, BASE at HEAD, calls `guard` changed; None where it
        answered neither way."""
        base = run_git("rev-parse", "HEAD").stdout.decode("ascii", "replace").strip()
        p = subprocess.run([bash, "-c", f"BASE={base}\n{line}\nchanged \"$1\"", "trigger", guard],
                           cwd=str(scratch), capture_output=True, env=env, stdin=subprocess.DEVNULL, timeout=60)
        return {0: True, 1: False}.get(p.returncode)

    failed = 0
    for case, stage in cases:
        if why:
            failed += 1
            print(f"arm FAIL  trigger parity, {case} — {why}")
            continue
        run_git("reset", "-q", "--hard")
        run_git("clean", "-fdq")
        stage()
        runner_says = read_runner_verdict("a/")
        # `read_staged` inherits the caller's environment, as the hook needs; a GIT_DIR git exports
        # to a pre-push hook in a linked worktree would point it away from the scratch repository.
        aside = {k: os.environ.pop(k) for k in [k for k in os.environ if k.startswith("GIT_")]}
        try:
            staged = precommit.read_staged(scratch)
        finally:
            os.environ.update(aside)
        hook_says = any(precommit.check_guard_trips(p, "a/") for p in staged)
        ok = runner_says is not None and runner_says == hook_says
        failed += not ok
        print(f"arm {'ok  ' if ok else 'FAIL'}  trigger parity, {case} — the runner's changed says "
              f"{runner_says}, the hook's staged list says {hook_says}")
    return failed, len(cases)


def run_selftest():
    """Each arm of §4 "The gate", and each plant §4 "The plants" moves out of govkit's selftest."""
    al, be, reg = "kits/alpha/kit.toml", "kits/beta/kit.toml", f"kits/{GOVKIT_HOME}/registry.toml"
    pu_a = 'purpose = "checks the alpha fixture"'
    cases = [
        # (case, plant, verb, rc, needles that one output line holds, needles no line holds)
        ("control: the fixture conforms", None, run_conform, 0, ("legs: 4 declared · 2 claimed · 2 exempt · 1 "
                                                                 "enforces-pending · 1 held · 1 unguarded",),
         ("fresh ·",)),
        # TOOL-dWitnessedBar-5 AC7: the held leg `beta selftest` declares its reason; each plant moves it.
        ("held guard: neither a guard nor a reason", lambda t: write_planted(
            t, be, 'unguarded_why = "a fixture suite with no path to guard"\n', ""), run_conform, 1,
         ("held guard ·", "'beta selftest'", "neither a guard nor"), ()),
        ("held guard: an empty reason", lambda t: write_planted(
            t, be, '"a fixture suite with no path to guard"', '""'), run_conform, 1,
         ("held guard ·", "'beta selftest'", "neither a guard nor"), ()),
        ("held guard: a guard and a reason", lambda t: write_planted(
            t, be, 'argv = ["bash", "{kit}/beta.test.sh"]\n', 'argv = ["bash", "{kit}/beta.test.sh"]\nguard = ["{kit}/"]\n'),
         run_conform, 1, ("held guard ·", "'beta selftest'", "a guard in every form and an unguarded_why"), ()),
        ("held guard, control: a guard alone is silent", lambda t: write_planted(
            t, be, 'unguarded_why = "a fixture suite with no path to guard"\n', 'guard = ["{kit}/"]\n'),
         run_conform, 0, ("1 held · 0 unguarded",), ("held guard ·",)),
        ("control: --check is green on the fresh render", None, run_check, 0, ("fresh · 4 legs",), ()),
        ("AC1 fresh: a manifest row hand-edited", lambda t: write_manifest_edit(
            t, lambda rs: [dict(r, ceiling=91) if r["name"] == "alpha check" else r for r in rs]),
         run_check, 1, ("'alpha check' changed: ceiling",), ()),
        ("AC1 fresh: a declaration added and no --write", lambda t: write_planted(
            t, be, 'ceiling = 120\n', 'ceiling = 120\n\n[[gate_leg]]\nname = "gamma leg"\nsubject = "repo"\n'
            'purpose = "a gamma leg"\nargv = ["bash", "g.sh"]\nenforces = ["practice.verify"]\n'),
         run_check, 1, ("'gamma leg' added",), ()),
        ("fresh, run 1 b: a declared ceiling moved", lambda t: write_planted(t, al, "ceiling = 90", "ceiling = 91"),
         run_check, 1, ("'alpha check' changed: ceiling",), ()),
        ("fresh, run d: a stage changed", lambda t: write_planted(t, al, 'stage = ["step.test"]',
                                                                  'stage = ["step.disagree"]'),
         run_check, 1, ("'alpha check' changed: stage",), ()),
        ("fresh, run e: a stage dropped", lambda t: write_planted(t, al, 'stage = ["step.test"]\n', ""),
         run_check, 1, ("'alpha check' changed: stage",), ()),
        ("fresh, run f: a tag", lambda t: write_planted(t, al, '"leg.alpha.alpha-check"', '"leg.alpha.drifted"'),
         run_check, 1, ("'alpha check' changed: tag",), ()),
        ("fresh, run g: tests and enforces", lambda t: write_planted(
            t, al, 'tests = ["feature.alpha"]\n', 'tests = ["feature.drifted"]\nenforces = ["principle.p1"]\n'),
         run_check, 1, ("'alpha check' changed: enforces, tests",), ()),
        ("fresh, run i2: a drifted purpose", lambda t: write_planted(t, al, pu_a, 'purpose = "drifted"'),
         run_check, 1, ("'alpha check' changed: purpose",), ()),
        ("fresh, D3: doc_reads", lambda t: write_planted(t, al, '["{memory_root}/doc.md"]', '["mem/other.md"]'),
         run_check, 1, ("'alpha check' changed: doc_reads",), ()),
        ("fresh, D3 control: a {memory_root} value rendering equal is silent", lambda t: write_planted(
            t, al, '["{memory_root}/doc.md"]', '["mem/doc.md"]'), run_check, 0, ("fresh · 4 legs",), ()),
        ("fresh, L1: a subject changed", lambda t: write_planted(t, be, 'subject = "kit"', 'subject = "repo"'),
         run_check, 1, ("'beta selftest' changed: subject",), ()),
        ("fresh, the typo leg: one added and one dropped", lambda t: write_planted(
            t, be, 'name = "beta selftest"', 'name = "beta selftset"'), run_check, 1,
         ("'beta selftset' added",), ()),
        ("fresh, the typo leg: ...and its old name dropped", lambda t: write_planted(
            t, be, 'name = "beta selftest"', 'name = "beta selftset"'), run_check, 1,
         ("'beta selftest' dropped",), ()),
        ("subject: maybe", lambda t: write_planted(t, al, 'subject = "repo"', 'subject = "maybe"'),
         run_conform, 1, ("subject ·", "'alpha check'", "'maybe'"), ()),
        ("subject, L1: absent", lambda t: write_planted(t, al, 'subject = "repo"\n', ""),
         run_conform, 1, ("subject ·", "'alpha check'", "None"), ()),
        ("subject, L1: Kit", lambda t: write_planted(t, be, 'subject = "kit"', 'subject = "Kit"'),
         run_conform, 1, ("subject ·", "'beta selftest'", "'Kit'"), ()),
        ("one declaration: a name in a descriptor and the registry", lambda t: write_planted(
            t, reg, 'name = "gov only leg"', 'name = "alpha check"'), run_conform, 1,
         ("one declaration ·", "'alpha check'", reg), ()),
        ("exempt reason: an empty why", lambda t: write_planted(
            t, reg, 'why = "a fixture row gov alone runs"', 'why = "  "'), run_conform, 1,
         ("exempt reason ·", "'gov only leg'"), ()),
        ("ceiling, run 2: a ceiling of true", lambda t: write_planted(t, al, "ceiling = 30", "ceiling = true"),
         run_conform, 1, ("ceiling ·", "'alpha check'", "True"), ()),
        ("reads: a class outside the four", lambda t: write_planted(t, be, "history =", "weather ="),
         run_conform, 1, ("reads ·", "'beta selftest'", "weather"), ()),
        ("name: a digit-bearing parenthetical", lambda t: write_planted(
            t, be, 'name = "beta selftest"', 'name = "beta selftest (3 arms)"'), run_conform, 1,
         ("name ·", "'beta selftest (3 arms)'", "digit-bearing"), ()),
        ("purpose, run h1: 61 characters", lambda t: write_planted(t, al, pu_a, f'purpose = "{"x" * 61}"'),
         run_conform, 1, ("purpose ·", "'alpha check'", "61 characters"), ()),
        ("purpose, run h2: two legs sharing one", lambda t: write_planted(
            t, be, 'purpose = "arms the beta fixture red and green"', pu_a), run_conform, 1,
         ("purpose ·", "'alpha check'", "'beta selftest'", "share the purpose"), ()),
        ("purpose presence: a declaration with no purpose", lambda t: write_planted(t, al, pu_a + "\n", ""),
         run_conform, 1, ("purpose presence ·", "'alpha check'", "carries no purpose"), ()),
        ("purpose, run i1: 60 characters, one multibyte, is silent", lambda t: write_planted(
            t, al, pu_a, f'purpose = "{"é" + "x" * 59}"'), run_conform, 0, ("conform · green",),
         ("purpose ·",)),
        ("token: a {gate_file} with no gov override", lambda t: write_planted(
            t, be, '"{kit}/beta.test.sh"]', '"{kit}/beta.test.sh", "{gate_file}"]'), run_conform, 1,
         ("token ·", "'beta selftest'", "{gate_file}"), ()),
        ("derived: a declaration carrying pass_leg", lambda t: write_planted(
            t, be, "ceiling = 120\n", "ceiling = 120\npass_leg = true\n"), run_conform, 1,
         ("derived ·", "'beta selftest'"), ()),
        ("enforces: empty on a leg no pending row excuses", lambda t: write_planted(
            t, al, 'enforces = ["practice.verify"]\n', ""), run_conform, 1,
         ("enforces ·", "'alpha check'", "core-pending.txt"), ()),
        ("enforces: a tag no row holds", lambda t: write_planted(
            t, be, '["practice.gate"]', '["practice.unheard"]'), run_conform, 1,
         ("enforces ·", "'beta selftest'", "practice.unheard"), ()),
        ("enforces: a practice rule is a tag a leg may hold", lambda t: write_planted(
            t, be, '["practice.gate"]', '["practice.gate.red"]'), run_check, 1, ("'beta selftest' changed: "
                                                                                 "enforces",), ()),
    ]
    failed = 0
    scratch = pathlib.Path(tempfile.mkdtemp(prefix="legf-"))
    try:
        for case, plant, verb, want_rc, want, never in cases:
            shutil.rmtree(scratch / "t", ignore_errors=True)
            top = scratch / "t"
            write_fixture(top)
            rc0, out0 = run_write(top)
            if rc0 != 0:
                failed += 1
                print(f"arm FAIL  {case} — the fixture's --write exited {rc0}: {out0}")
                continue
            if plant is not None:
                plant(top)
            try:
                rc, lines = verb(top)
            except Refusal as e:
                rc, lines = 2, [f"{SAY}: refused · {e}"]
            hit = any(all(w in ln for w in want) for ln in lines)
            leak = any(n in ln for ln in lines for n in never)
            if rc == want_rc and hit and not leak:
                print(f"arm ok    {case}")
                continue
            failed += 1
            print(f"arm FAIL  {case} — wanted rc={want_rc} and a line holding {want!r}, got rc={rc}")
            print("".join(f"      {ln}\n" for ln in lines), end="")
        # AC5: `new` writes a declaration the gate takes, and refuses one it would not, writing nothing.
        shutil.rmtree(scratch / "t", ignore_errors=True)
        top = scratch / "t"
        write_fixture(top)
        run_write(top)
        before = pathlib.Path(top, al).read_bytes()
        ns = argparse.Namespace(name="demo leg", kit="alpha", exempt=None, argv='["python3", "demo.py"]',
                                subject="repo", purpose=None, enforces=["practice.verify"], guard=None,
                                chunk=None, ceiling=None, tests=None, stage=None)
        rc, lines = run_new(top, ns)
        ok = rc == 2 and pathlib.Path(top, al).read_bytes() == before and any("--purpose" in ln for ln in lines)
        print(f"arm {'ok  ' if ok else 'FAIL'}  AC5 new: no --purpose refuses and writes nothing")
        failed += not ok
        ns.purpose = "a demo leg"
        rc, lines = run_new(top, ns)
        crc, clines = run_conform(top)
        text = pathlib.Path(top, al).read_bytes().decode("utf-8")
        ok = (rc == 0 and crc == 0 and 'tag = "leg.alpha.demo-leg"' in text
              and any(r["name"] == "demo leg" for r in json.loads(
                  pathlib.Path(top, "kits", "gate-legs.json").read_bytes().decode("utf-8"))))
        print(f"arm {'ok  ' if ok else 'FAIL'}  AC5 new: the declaration renders and conforms")
        if not ok:
            print("".join(f"      {ln}\n" for ln in lines + clines), end="")
        failed += not ok
        # Over gov: the live tree conforms, its legs: note printed.
        rc, lines = run_conform(derive_repo_root())
        ok = rc == 0 and any(ln.startswith("legs: ") for ln in lines)
        print(f"arm {'ok  ' if ok else 'FAIL'}  over gov: --conform exits 0 on the live tree, its legs: note printed")
        if not ok:
            print("".join(f"      {ln}\n" for ln in lines[-12:]), end="")
        failed += not ok
        # TOOL-dWitnessedBar-108 S2: the hook's staged list against the runner's own `changed` line.
        trig_failed, trig_ran = check_precommit_trigger(scratch / "trigger")
        failed += trig_failed
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
    total = len(cases) + 3 + trig_ran
    if failed:
        print(f"FAIL — {failed} of {total} leg-factory fixtures failed")
        return 1
    print(f"PASS — the leg-factory fixtures, {total} cases")
    return 0


def main(argv=None):
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    argv = sys.argv[1:] if argv is None else argv
    if argv[:1] == ["new"]:
        ap = argparse.ArgumentParser(prog="leg_factory.py new", description="declare one conforming leg")
        ap.add_argument("name")
        ap.add_argument("--kit", help="the registry entry id whose descriptor receives a [[gate_leg]] row")
        ap.add_argument("--exempt", help="the why of an [[exempt_leg]] row of the registry instead")
        ap.add_argument("--argv", help="the argv, a JSON list")
        ap.add_argument("--subject", help="kit or repo")
        ap.add_argument("--purpose", help=f"one line of at most {PURPOSE_MAX_CHARS} characters")
        ap.add_argument("--enforces", action="append", help="a principle or practice tag; repeatable")
        ap.add_argument("--tests", action="append", help="a feature tag the leg tests; repeatable")
        ap.add_argument("--guard", help="the guard, a JSON list")
        ap.add_argument("--stage", action="append", help="a step tag the leg serves; repeatable")
        ap.add_argument("--chunk", help="gov's chunk for the leg")
        ap.add_argument("--ceiling", type=int, help="gov's ceiling for the leg, in seconds")
        a = ap.parse_args(argv[1:])
        verb = lambda root: run_new(root, a)  # noqa: E731
    else:
        ap = argparse.ArgumentParser(prog="leg_factory.py", description=__doc__.split("\n")[0])
        g = ap.add_mutually_exclusive_group(required=True)
        for flag, fn in (("--write", run_write), ("--check", run_check), ("--conform", run_conform),
                         ("--list", run_list), ("--selftest", None)):
            g.add_argument(flag, action="store_const", dest="verb", const=fn or "selftest")
        a = ap.parse_args(argv)
        if a.verb == "selftest":
            return run_selftest()
        verb = a.verb
    try:
        rc, lines = verb(derive_repo_root())
    except (Refusal, LookupError) as e:
        rc, lines = 2, [f"{SAY}: refused · {e}"]
    except Exception as e:  # noqa: BLE001 - govkit's own Refusal is a refusal here too
        if type(e).__name__ != "Refusal":
            raise
        rc, lines = 2, [f"{SAY}: refused · {e}"]
    for ln in lines:
        print(ln)
    return rc


if __name__ == "__main__":
    sys.exit(main())
