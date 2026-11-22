#!/usr/bin/env python3
"""kickoff_facts_to_overlay.py — the upgrade step `kickoff-manifest/facts-to-overlay` (TOOL-dPlacedRequest-9, S5).

    python <prefix>/govkit/steps/kickoff_facts_to_overlay.py up|down|witness <target>
    python <prefix>/govkit/steps/kickoff_facts_to_overlay.py --fixture [--plant <case>]

Its row is the kickoff-manifest descriptor's `[[upgrade]]`. The UP turns each top-level `- ` bullet of the
kickoff manifest's `## §B` section, the run before its first `###` sub-head, into one level-2 `repo.kickoff.`
unit of `.governance/instructions.toml`, which the orientation card prints under `## pockets`, and leaves §B
holding one bullet naming where the facts went; the DOWN restores both files byte-identical from the
before-image; the WITNESS exits 0 when §B carries that bullet and only bullets the up would refuse, and every
`repo.kickoff.` unit's text was a §B bullet.

WHERE. The manifest is the `[answers] manifest_path` of the target's `.governance/deploy.toml`, read here,
since an argv carries no answer, and held inside the target by the step reader's `check_contained`; one
leaving it is refused, exit 1, nothing written. The write command is the playbook kit's `instructions_edit.py`
where `resolve_kit_dir` finds it from the target; the facts bullet names its target-relative path. No
`deploy.toml`, no answer, no file at it, no `## §B` heading or no write command inside the target is
nothing to move: exit 0, nothing written and no before-image, and the witness exits 0 naming which.

THE ROWS. Bullet `n` of §B becomes `tag = "repo.kickoff.f<nn>"`, `<nn>` its two-digit position, `level = 2`,
`type = "constraint"`, `scope = ["reader.card"]`, `trigger = "always"`, `budget` `line` within the line
budget and `block` past it, `text` the bullet without its `- `, and `enforced-by` none. Each row is graded
alone, by `check_statement` and by the overlay reader over that row by itself; a bullet either refuses, or
one spanning more than one line, stays in §B as guide text, named on its own line by position and finding,
and the update goes on. The candidate of every passing row is graded whole; its refusal exits 1, nothing
written. The facts bullet is known by every byte up to its semicolon and never converted.

THE UP, in order: the before-image, the overlay where a row passed, and LAST the manifest, its top-level §B
bullets rewritten to the facts bullet and then the bullets that stayed, so the witness changes last. A
re-run over a killed up converges on the first image. It never writes the policy mirror.

THE FIXTURE builds a throwaway repository in the system temp directory per case: a manifest, a
`deploy.toml` answering `manifest_path`, a policy file and a stub playbook kit whose tracked
`instruction_units.py` forwards to gov's module and whose `instructions_edit.py` the resolver probes for.
The card cases run gov's kickoff engine there. Each case prints `ok` or `FAIL` lines; exit 0 when all hold.

Exit 0 done, 1 refused naming why (nothing written), 2 a usage error or the writer's duplicate-tag refusal.
"""

import base64
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

STEP_ID = "kickoff-manifest/facts-to-overlay"
SAY = "kickoff-facts"
DEPLOY = ".governance/deploy.toml"
OVERLAY = ".governance/instructions.toml"
SECTION = "## §B"
TAG_HEAD = "repo.kickoff.f"
READER = "reader.card"
ENFORCED = "none — a fact the kickoff manifest front-loads"
FACTS_LEAD = "The orientation facts are level-2 units the card prints under ## pockets;"
WRITE_HOME, WRITE_ANCHOR = "playbook", "instructions_edit.py"
GOV = pathlib.Path(__file__).resolve().parents[2]  # `{gov}`: the tool root this step ships in
HERE = pathlib.Path(__file__).resolve().parent


def load_steps():
    """The step reader beside this file's directory, imported by its path: the runner's `-I` drops
    this file's own directory from `sys.path`, and the before-image helpers live there."""
    path = HERE.parent / "upgrade_steps.py"
    mod = sys.modules.get("upgrade_steps")
    if mod is not None and getattr(mod, "__file__", None) and pathlib.Path(mod.__file__).resolve() == path:
        return mod
    spec = importlib.util.spec_from_file_location("upgrade_steps", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["upgrade_steps"] = mod
    spec.loader.exec_module(mod)
    return mod


STEPS = load_steps()
Refusal = STEPS.Refusal


def load_overlay():
    """Gov's playbook overlay module, found through the sibling-kit resolver the step reader carries:
    its reader, its writer and, through it, the unit grammar."""
    kit = STEPS.resolve_kit_dir(WRITE_HOME, "overlay.py", GOV)
    if str(kit) not in sys.path:
        sys.path.insert(0, str(kit))
    import overlay
    return overlay


def read_manifest_path(target: pathlib.Path) -> str | None:
    """The `[answers] manifest_path` of the target's descriptor, target-relative, or None where there is
    no descriptor or no answer; one leaving the target is a refusal."""
    deploy = target / DEPLOY
    if not deploy.is_file():
        return None
    try:
        doc = tomllib.loads(deploy.read_bytes().decode("utf-8").removeprefix("﻿"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as e:
        raise Refusal(f"{DEPLOY}: does not parse ({e})") from None
    answers = doc.get("answers")
    value = answers.get("manifest_path") if isinstance(answers, dict) else None
    if not isinstance(value, str) or not value.strip():
        return None
    return STEPS.check_contained(target, value).relative_to(target).as_posix()


def derive_write_command(target: pathlib.Path) -> str | None:
    """The target-relative path of the playbook kit's write command, or None where none resolves from the
    target or the one that does sits outside it."""
    try:
        kit = pathlib.Path(STEPS.resolve_kit_dir(WRITE_HOME, WRITE_ANCHOR, target)).absolute()
    except LookupError:
        return None
    try:
        return (kit / WRITE_ANCHOR).relative_to(target.absolute()).as_posix()
    except ValueError:
        return None


def derive_facts_bullet(write: str) -> str:
    """The one bullet §B keeps in front of the bullets that stayed (S6)."""
    return f"- {FACTS_LEAD} change one with {write}."


def parse_fact_bullets(text: str):
    """`(lines, bullets)` of §B, or None with no `## §B` heading: `lines` the text's lines with their
    endings, each bullet `(first, end, text)`, a top-level `- ` line and each following line indented two or
    more spaces, `lines[first:end]`, up to the next bullet, a blank line, the first `###` sub-head or next `## `
    heading; `text` is those lines joined by single spaces, each stripped, the `- ` dropped
    (TOOL-dPlacedRequest-34 S50), so a wrapped bullet's row carries the whole bullet."""
    lines = text.splitlines(keepends=True)
    head = next((i for i, ln in enumerate(lines) if ln.startswith(SECTION)), None)
    if head is None:
        return None
    bullets, i = [], head + 1
    while i < len(lines) and not lines[i].startswith(("###", "## ")):
        if lines[i].startswith("- "):
            end = i + 1
            while end < len(lines) and lines[end].startswith("  ") and lines[end].strip():
                end += 1
            text = " ".join(ln.strip() for ln in [lines[i][2:]] + lines[i + 1:end])
            bullets.append((i, end, text))
            i = end
        else:
            i += 1
    return lines, bullets


def check_fact_row(ov, target: pathlib.Path, row: dict) -> list[str]:
    """Every finding against one fact row graded alone: the statement grammar, then the overlay reader
    over that row by itself, which holds it to the schema and its budget."""
    reds = list(ov.iu.check_statement(row))
    try:
        ov.read_overlay(target, candidate=ov.derive_overlay_text("", [row]))
    except ov.OverlayRefused as e:
        reds += [ln for ln in str(e).splitlines() if ln.strip()]
    return reds


def derive_fact_plan(ov, target: pathlib.Path, bullets) -> tuple[list, list, list]:
    """`(rows, kept, refused)`: a row per bullet that passes, the bullets that stay (each refused one, in
    order), and `(position, finding)` per refusal. The facts bullet is neither moved nor kept."""
    line = ov.iu.BUDGET_BYTES["line"]
    rows, kept, refused = [], [], []
    for n, bullet in enumerate(bullets, 1):
        first, end, text = bullet
        if text.startswith(FACTS_LEAD):
            continue
        row = {"tag": f"{TAG_HEAD}{n:02d}", "level": 2, "type": "constraint", "scope": [READER],
               "trigger": "always", "budget": "line" if len(text.encode("utf-8")) <= line else "block",
               "text": text, "enforced-by": ENFORCED}
        reds = [f"it spans {end - first} lines, and a unit is one line"] if end - first > 1 else \
            check_fact_row(ov, target, row)
        if reds:
            kept.append(bullet)
            refused.append((n, " · ".join(reds)))
        else:
            rows.append(row)
    return rows, kept, refused


def render_manifest_facts(lines: list, bullets, kept, write: str) -> str:
    """The manifest with §B's top-level bullets rewritten: the facts bullet where the first stood, then
    the bullets that stayed, every other line kept."""
    first = bullets[0][0]
    eol = lines[first][len(lines[first].rstrip("\r\n")):] or "\n"
    drop = {i for b in bullets for i in range(b[0], b[1])}
    out = []
    for i, ln in enumerate(lines):
        if i == first:
            out.append(derive_facts_bullet(write) + eol)
            for b in kept:
                out += lines[b[0]:b[1]]
        if i not in drop:
            out.append(ln)
    return "".join(out)


def read_image_bullets(target: pathlib.Path, rel: str) -> set:
    """The bullet texts §B held before the up, read from its before-image; empty with no image."""
    image = STEPS.derive_image_path(target, STEP_ID)
    if not image.is_file():
        return set()
    before = json.loads(image.read_text(encoding="utf-8"))["paths"].get(rel, {}).get("before")
    parsed = parse_fact_bullets(base64.b64decode(before).decode("utf-8")) if before else None
    return {b[2] for b in parsed[1]} if parsed else set()


def read_where(target: pathlib.Path, verb: str):
    """`(rel, manifest path, write command)` where the step has something to move, else None, printing
    which of the four was absent."""
    rel = read_manifest_path(target)
    why = None
    if rel is None:
        why = f"no [answers] manifest_path in {DEPLOY}"
    elif not (target / rel).is_file():
        why = f"no file at the manifest_path answer {rel}"
    else:
        try:
            parsed = parse_fact_bullets((target / rel).read_bytes().decode("utf-8"))
        except UnicodeDecodeError as e:
            raise Refusal(f"{rel}: is not UTF-8 ({e})") from None
        if parsed is None:
            why = f"no {SECTION} heading in {rel}"
        elif not parsed[1]:
            why = f"no top-level bullet under {SECTION} in {rel}"
    write = derive_write_command(target) if why is None else None
    if why is None and write is None:
        why = f"no playbook kit's {WRITE_ANCHOR} resolves inside the target"
    if why is not None:
        print(f"{SAY}: {verb} · {why}, so there is nothing to move")
        return None
    return rel, target / rel, write


def cmd_up(target: pathlib.Path) -> int:
    where = read_where(target, "up")
    if where is None:
        return 0
    rel, mpath, write = where
    ov = load_overlay()
    current = mpath.read_bytes()

    def derive_after(before):
        data = before[rel] if before is not None else mpath.read_bytes()
        if before is not None:
            text = (before.get(OVERLAY) or b"").decode("utf-8")
        else:
            path = target / OVERLAY
            text = path.read_bytes().decode("utf-8") if path.is_file() else ""
        lines, bullets = parse_fact_bullets(data.decode("utf-8"))
        rows, kept, _refused = derive_fact_plan(ov, target, bullets)
        after = {}
        if rows:
            out = ov.derive_overlay_text(text, rows)
            try:
                ov.read_overlay(target, candidate=out)
            except ov.OverlayRefused as e:
                raise Refusal(f"the overlay reader refuses the converted rows:\n{e}") from None
            after[OVERLAY] = out.encode("utf-8")
        after[rel] = render_manifest_facts(lines, bullets, kept, write).encode("utf-8")
        return after

    lines, bullets = parse_fact_bullets(current.decode("utf-8"))
    rows, kept, refused = derive_fact_plan(ov, target, bullets)
    for n, finding in refused:
        print(f"{SAY}: up · bullet {n} stays in {SECTION} as guide text · {finding}")
    if not rows and render_manifest_facts(lines, bullets, kept, write).encode("utf-8") == current:
        print(f"{SAY}: up · {rel} holds no bullet to move, so there is nothing to move")
        return 0
    try:
        after = STEPS.write_before_image(target, STEP_ID, derive_after)
    except ov.OverlayRefused as e:
        sys.stderr.write(f"{SAY}: up refused · {e}\n")
        return e.code
    if OVERLAY in after:
        (target / OVERLAY).parent.mkdir(parents=True, exist_ok=True)
        (target / OVERLAY).write_bytes(after[OVERLAY])
    mpath.write_bytes(after[rel])  # LAST: the witness reads §B
    print(f"{SAY}: up · {len(rows)} fact(s) moved to {OVERLAY} as level-2 {TAG_HEAD[:-1]} units · "
          f"{len(refused)} stayed in {SECTION} as guide text · {rel} names {write}")
    return 0


def cmd_down(target: pathlib.Path) -> int:
    restored = STEPS.write_from_before_image(target, STEP_ID)
    print(f"{SAY}: down · restored {', '.join(restored) or 'nothing: no before-image, no up applied'}")
    return 0


def cmd_witness(target: pathlib.Path) -> int:
    where = read_where(target, "witness")
    if where is None:
        return 0
    rel, mpath, _write = where
    ov = load_overlay()
    _lines, bullets = parse_fact_bullets(mpath.read_bytes().decode("utf-8"))
    if not any(b[2].startswith(FACTS_LEAD) for b in bullets):
        print(f"{SAY}: witness · {SECTION} of {rel} carries no facts bullet: not applied")
        return 1
    rows, kept, _refused = derive_fact_plan(ov, target, bullets)
    if rows:
        print(f"{SAY}: witness · {len(rows)} bullet(s) of {SECTION} would move: not applied")
        return 1
    held = read_image_bullets(target, rel)
    path = target / OVERLAY
    units = ov.iu.parse_unit_rows(path.read_bytes().decode("utf-8"), OVERLAY)[0] if path.is_file() else []
    facts = [u for u in units if (u.tag or "").startswith(TAG_HEAD)]
    stray = [u.tag for u in facts if u.text not in held]
    if stray:
        print(f"{SAY}: witness · {', '.join(stray)} carry text no {SECTION} bullet held before the up: not applied")
        return 1
    print(f"{SAY}: witness · {SECTION} carries the facts bullet and {len(kept)} bullet(s) kept as guide text, "
          f"and each of {len(facts)} {TAG_HEAD[:-1]} unit(s) was a {SECTION} bullet: applied")
    return 0


# ------------------------------------------------------------------------------------------ the fixture

FX_MANIFEST = "kickoff/MANIFEST.md"
FX_BULLETS = ("A build of more than one pass runs on `docs/METHOD.md`.",
              "Every session start writes 1 orientation card.",
              "The remote is `origin`, default branch `main`.")
FX_REFUSED = "A bullet that carries no value at all."
FX_UNITS, FX_SIZE = 30, 150     # PINNED fixture literals: the cap plants' unit count and each text's bytes
FX_ROOM, FX_TINY = 2048, 40     # PINNED fixture literals: the cap plant's two rooms
GIT_LEAKS = ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR", "GIT_OBJECT_DIRECTORY")


def derive_kickoff_home() -> pathlib.Path:
    """The kickoff engine's directory in gov, from this step's own descriptor's `home`."""
    entry = HERE.parent / "entries" / f"{STEP_ID.split('/')[0]}.kit.toml"
    doc = tomllib.loads(entry.read_text(encoding="utf-8"))
    return GOV.parent / doc["home"] if doc.get("home_root_relative") else GOV / doc["home"]


def derive_fx_env() -> dict:
    """This process's environment less the variables that would point git at another repository, and
    with no global or system git config, so no runner's hooks path or template reaches the fixture."""
    env = {k: v for k, v in os.environ.items() if k not in GIT_LEAKS and k != "CARD_CAP_BYTES"}
    env.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1")
    return env


def run_fx_git(t: pathlib.Path, *args) -> str:
    env = derive_fx_env()
    return subprocess.run(["git", "-C", str(t), *args], capture_output=True, text=True, encoding="utf-8",
                          errors="replace", env=env, check=True).stdout


def write_fx_commit(t: pathlib.Path, msg: str) -> None:
    run_fx_git(t, "add", "-A")
    run_fx_git(t, "commit", "-q", "--no-verify", "--allow-empty", "-m", msg)


def build_fact_fixture(base: pathlib.Path, bullets=FX_BULLETS, *, manifest=None, answer=True, edit=True,
                       units=True) -> pathlib.Path:
    """One throwaway repository: the manifest, the descriptor answering where it is, a policy file, and
    the stub playbook kit, committed."""
    t = base / "t"
    t.mkdir(parents=True)
    run_fx_git(t, "init", "-q", "-b", "main")
    for key, value in (("user.email", "fx@fixture"), ("user.name", "fx"), ("commit.gpgsign", "false"),
                       ("core.autocrlf", "false")):
        run_fx_git(t, "config", key, value)
    text = manifest if manifest is not None else (
        "# fixture manifest\n\n## §B — Orientation\n\nOne line per bullet.\n\n"
        + "".join(f"- {b}\n" for b in bullets) + "\n### Pointer map\n\n- a guide row\n")
    (t / FX_MANIFEST).parent.mkdir(parents=True)
    (t / FX_MANIFEST).write_text(text, encoding="utf-8", newline="\n")
    (t / ".governance").mkdir()
    (t / DEPLOY).write_text("[answers]\nproject_name = \"fixture\"\n"
                            + (f"manifest_path = \"{FX_MANIFEST}\"\n" if answer else ""), encoding="utf-8",
                            newline="\n")
    policy = STEPS.resolve_kit_dir("policy", "policy.py", GOV) / "policy.py"
    scaffold = subprocess.run([sys.executable, str(policy), "scaffold"], capture_output=True).stdout
    (t / ".governance" / "policy.toml").write_bytes(scaffold.replace(b"\r\n", b"\n"))
    if units:
        kit = t / WRITE_HOME
        kit.mkdir()
        gov_iu = STEPS.resolve_kit_dir(WRITE_HOME, "instruction_units.py", GOV) / "instruction_units.py"
        (kit / "instruction_units.py").write_text(
            f"import runpy, sys\nsys.argv[0] = {str(gov_iu)!r}\nrunpy.run_path({str(gov_iu)!r}, run_name='__main__')\n",
            encoding="utf-8", newline="\n")
        if edit:
            (kit / WRITE_ANCHOR).write_text("# a stub: the step's resolver probes for it\n", encoding="utf-8",
                                            newline="\n")
    write_fx_commit(t, "release")
    return t


def derive_fx_rows(n: int, size: int, level: int = 2) -> list:
    """`n` committed-ready `reader.card` rows of `size`-byte texts, tags in order."""
    rows = []
    for i in range(1, n + 1):
        head = f"Fact {i:02d} holds `x{i}`: "
        rows.append({"tag": f"{TAG_HEAD}{i:02d}", "level": level, "type": "constraint", "scope": [READER],
                     "trigger": "always", "budget": "line", "text": head + "y" * (size - len(head)),
                     "enforced-by": ENFORCED})
    return rows


def write_fx_units(t: pathlib.Path, rows) -> None:
    load_overlay().write_overlay_units(t / OVERLAY, rows)


def run_fx_step(t: pathlib.Path, verb: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-I", str(pathlib.Path(__file__).resolve()), verb, str(t)],
                          capture_output=True, text=True, encoding="utf-8", errors="replace", env=derive_fx_env())


def run_fx_pockets(t: pathlib.Path, *args) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-I", str(t / WRITE_HOME / "instruction_units.py"), "pockets",
                           "--root", str(t), *args], capture_output=True, text=True, encoding="utf-8",
                          errors="replace", cwd=str(t), env=derive_fx_env())


def run_fx_card(t: pathlib.Path, verb: str, body: str | None = None, cap: int | None = None):
    env = derive_fx_env()
    if cap is not None:
        env["CARD_CAP_BYTES"] = str(cap)
    engine = derive_kickoff_home() / "manifest-check.sh"
    return subprocess.run([STEPS.resolve_bash(), str(engine), "--card", verb, "--session", "t1"],
                          input=(body or "").encode("utf-8"), capture_output=True, cwd=str(t), env=env,
                          timeout=300)


def read_fx_card(t: pathlib.Path) -> str:
    return (t / ".git" / "orientation" / "t1.md").read_bytes().decode("utf-8").replace("\r\n", "\n")


def read_fx_bullets(t: pathlib.Path) -> list:
    parsed = parse_fact_bullets((t / FX_MANIFEST).read_bytes().decode("utf-8"))
    return [b[2] for b in parsed[1]] if parsed else []


def read_fx_units(t: pathlib.Path) -> list:
    return list(load_overlay().read_overlay(t).units)


def check_fx_quiet(t: pathlib.Path) -> bool:
    return run_fx_git(t, "status", "--porcelain") == ""


def arm_up(base, add):
    t = build_fact_fixture(base)
    up = run_fx_step(t, "up")
    loose = run_fx_pockets(t, "--all")
    write_fx_commit(t, "up")
    units = read_fx_units(t)
    add("[AC1] up exits 0 and the overlay at HEAD holds f01 to f03 at level 2 under reader.card, each text its bullet",
        up.returncode == 0 and [(u.tag, u.level, tuple(u.scope), u.text) for u in units]
        == [(f"{TAG_HEAD}{i:02d}", 2, (READER,), b) for i, b in enumerate(FX_BULLETS, 1)], up.stdout + up.stderr)
    bullets = read_fx_bullets(t)
    add("[AC1] ...and §B holds the facts bullet alone, naming the write command where the target holds it",
        bullets == [derive_facts_bullet(f"{WRITE_HOME}/{WRITE_ANCHOR}")[2:]], repr(bullets))
    add("[AC3] pockets over the write left uncommitted prints the heading and none declared",
        loose.returncode == 0 and loose.stdout.splitlines() == ["## pockets", "- none declared"], loose.stdout)
    full = run_fx_pockets(t, "--all")
    add("[AC3] pockets --all after the commit prints the heading and the three bullets in tag order",
        full.returncode == 0 and full.stdout.splitlines() == ["## pockets", *(f"- {b}" for b in FX_BULLETS)],
        full.stdout + full.stderr)


def arm_pockets_level(base, add):
    t = build_fact_fixture(base)
    run_fx_step(t, "up")
    write_fx_commit(t, "up")
    row = dict(derive_fx_rows(1, 60, level=3)[0], tag=f"{TAG_HEAD}99")
    write_fx_units(t, [row])
    write_fx_commit(t, "a level-3 card unit")
    held = [u.tag for u in read_fx_units(t)]
    full = run_fx_pockets(t, "--all")
    add("[AC3] LIVENESS the overlay at HEAD holds the level-3 reader.card unit", f"{TAG_HEAD}99" in held, repr(held))
    add("[AC3] pockets --all prints the three level-2 units and not the level-3 one",
        full.stdout.splitlines() == ["## pockets", *(f"- {b}" for b in FX_BULLETS)], full.stdout + full.stderr)


def arm_pockets_cap(base, add):
    t = build_fact_fixture(base)
    rows = derive_fx_rows(FX_UNITS, FX_SIZE)
    write_fx_units(t, rows)
    write_fx_commit(t, "thirty units")
    p = run_fx_pockets(t, "--room", str(FX_ROOM))
    out = p.stdout.splitlines()
    shown = out[1:-1]
    m = re.fullmatch(r"- … \(\+(\d+)\) — instruction_units\.py pockets --all", out[-1] if out else "")
    add("[AC4] --room 2048 prints at most 2048 bytes", p.returncode == 0 and len(p.stdout.encode("utf-8")) <= FX_ROOM,
        f"{len(p.stdout.encode('utf-8'))} bytes")
    add("[AC4] ...each unit line its unit's text whole, in tag order",
        out[:1] == ["## pockets"] and shown == [f"- {r['text']}" for r in rows[:len(shown)]] and len(shown) > 0,
        p.stdout)
    add("[AC4] ...and the closing line counts the units left out: k plus the lines shown is 30",
        bool(m) and int(m[1]) + len(shown) == FX_UNITS, out[-1] if out else "")
    full = run_fx_pockets(t, "--all")
    add("[AC4] --all prints every unit's line", full.stdout.splitlines() == ["## pockets", *(f"- {r['text']}" for r in rows)],
        full.stdout[-300:])
    tiny = run_fx_pockets(t, "--room", str(FX_TINY))
    add("[AC4] --room 40 prints nothing and exits 0", tiny.returncode == 0 and tiny.stdout == "", tiny.stdout + tiny.stderr)


def read_fx_section(card: str) -> list:
    """The card's lines from its `## pockets` line through the line after the section, or []."""
    lines = card.splitlines()
    if "## pockets" not in lines:
        return []
    i = lines.index("## pockets")
    j = next((k for k in range(i + 1, len(lines)) if not lines[k].startswith("- ")), len(lines))
    return lines[i:j + 1]


def arm_card(base, add):
    t = build_fact_fixture(base)
    run_fx_step(t, "up")
    write_fx_commit(t, "up")
    p = run_fx_card(t, "--write")
    card = read_fx_card(t) if p.returncode == 0 else ""
    section = read_fx_section(card)
    lines = card.splitlines()
    add("[AC5] the card writes and holds ## pockets and its three lines immediately before recent —",
        p.returncode == 0 and section == ["## pockets", *(f"- {b}" for b in FX_BULLETS), "recent —"],
        p.stdout.decode("utf-8", "replace")[-400:] + repr(section))
    ready = next((i for i, ln in enumerate(lines) if ln.startswith("READY — ")), -1)
    add("[AC5] ...above the READY anchor", "## pockets" in lines and lines.index("## pockets") < ready, repr(ready))


def arm_card_no_playbook(base, add):
    t = build_fact_fixture(base, units=False)
    p = run_fx_card(t, "--write")
    card = read_fx_card(t) if p.returncode == 0 else ""
    add("[AC5] with no playbook kit the card still writes and holds one pockets — skipped: line above recent —",
        p.returncode == 0 and re.search(r"^pockets — skipped: .*\nrecent —$", card, re.M) is not None
        and "## pockets" not in card.splitlines(), p.stdout.decode("utf-8", "replace")[-400:])


def arm_refused(base, add):
    bullets = (FX_BULLETS[0], FX_REFUSED, FX_BULLETS[2])
    t = build_fact_fixture(base, bullets)
    before = (t / FX_MANIFEST).read_bytes()
    up = run_fx_step(t, "up")
    named = [ln for ln in up.stdout.splitlines() if " stays in " in ln]
    add("[AC6] up over a refused second bullet exits 0 printing one line naming position 2",
        up.returncode == 0 and len(named) == 1 and " · bullet 2 stays in " in named[0], up.stdout + up.stderr)
    write_fx_commit(t, "up")
    units = [u.tag for u in read_fx_units(t)]
    add("[AC6] ...the overlay at HEAD holds f01 and f03 alone", units == [f"{TAG_HEAD}01", f"{TAG_HEAD}03"], repr(units))
    got = read_fx_bullets(t)
    add("[AC6] ...§B holds the facts bullet, then the refused bullet",
        got == [derive_facts_bullet(f"{WRITE_HOME}/{WRITE_ANCHOR}")[2:], FX_REFUSED], repr(got))
    w = run_fx_step(t, "witness")
    add("[AC6] ...and the witness exits 0", w.returncode == 0, w.stdout + w.stderr)
    down = run_fx_step(t, "down")
    add("[AC6] down restores the manifest byte for byte, the refused bullet beside the moved ones",
        down.returncode == 0 and (t / FX_MANIFEST).read_bytes() == before, down.stdout + down.stderr)


def arm_template(base, add):
    text = (derive_kickoff_home() / "MANIFEST-TEMPLATE.md").read_bytes().decode("utf-8").replace("\r\n", "\n")
    t = build_fact_fixture(base, manifest=text)
    up = run_fx_step(t, "up")
    named = [ln for ln in up.stdout.splitlines() if " stays in " in ln]
    w = run_fx_step(t, "witness")
    add("[AC6] over the shipped template's §B, up exits 0, naming the placeholder bullets it keeps",
        up.returncode == 0 and len(named) > 0, up.stdout + up.stderr)
    add("[AC6] ...and the witness exits 0", w.returncode == 0, w.stdout + w.stderr)


def check_fx_nothing(base, add, label, **opts):
    t = build_fact_fixture(base, **opts)
    runs = [run_fx_step(t, verb) for verb in ("up", "down", "witness")]
    add(f"[AC6] {label}: up, down and witness each exit 0", all(p.returncode == 0 for p in runs),
        "".join(p.stdout + p.stderr for p in runs))
    add(f"[AC6] {label}: git status --porcelain prints nothing", check_fx_quiet(t), run_fx_git(t, "status", "--porcelain"))


def arm_no_answer(base, add):
    check_fx_nothing(base, add, "no manifest_path answer", answer=False)


def arm_no_kit(base, add):
    check_fx_nothing(base, add, "no instructions_edit.py", edit=False)


def arm_down(base, add):
    t = build_fact_fixture(base)
    manifest = (t / FX_MANIFEST).read_bytes()
    w0, up, w1 = run_fx_step(t, "witness"), run_fx_step(t, "up"), run_fx_step(t, "witness")
    image = STEPS.derive_image_path(t, STEP_ID)
    add("[AC7] LIVENESS the up moved the facts: an overlay and a before-image", up.returncode == 0
        and (t / OVERLAY).is_file() and image.is_file(), up.stdout + up.stderr)
    down, w2 = run_fx_step(t, "down"), run_fx_step(t, "witness")
    add("[AC7] after the down both files equal their before-image: the manifest byte for byte, no overlay",
        down.returncode == 0 and (t / FX_MANIFEST).read_bytes() == manifest and not (t / OVERLAY).exists()
        and not image.exists(), down.stdout + down.stderr)
    add("[AC7] the witness exits 1 before the up and after the down, 0 after the up",
        (w0.returncode, w1.returncode, w2.returncode) == (1, 0, 1), w0.stdout + w1.stdout + w2.stdout)
    add("[AC7] no verb wrote a policy mirror", not (t / ".governance" / "policy.json").exists())


def arm_card_cap(base, add):
    t = build_fact_fixture(base)
    write_fx_units(t, derive_fx_rows(FX_UNITS, FX_SIZE))
    write_fx_commit(t, "thirty units")
    p = run_fx_card(t, "--write")
    card = read_fx_card(t) if p.returncode == 0 else ""
    whole = len(read_fx_section(card)) == FX_UNITS + 2
    add("[AC9] LIVENESS the written card holds every unit line", p.returncode == 0 and whole, repr(read_fx_section(card)[-2:]))
    cap = len(card.encode("utf-8")) - 4 * (FX_SIZE + 3)   # DERIVED: four unit lines below the whole card
    body = f"## open\n- `{FX_MANIFEST}` — the fixture's manifest\n"
    a = run_fx_card(t, "--append", body=body, cap=cap)
    card = read_fx_card(t)
    lines = card.splitlines()
    above = lines[lines.index("recent —") - 1] if "recent —" in lines else ""
    m = re.fullmatch(r"- … \(\+(\d+)\) — instruction_units\.py pockets --all", above)
    add("[AC9] the append under a cap below the whole card exits 0 printing its appended — line",
        a.returncode == 0 and "appended — " in a.stdout.decode("utf-8", "replace"), a.stdout.decode("utf-8", "replace"))
    add("[AC9] ...the line above recent — counts at least 1 unit left out", bool(m) and int(m[1]) >= 1, above)
    add("[AC9] ...and the card holds at most the cap", len((t / ".git" / "orientation" / "t1.md").read_bytes()) <= cap,
        f"cap {cap}")


def check_fx_refused(add, label, t, want, needle):
    """One refusal arm: `up` exits `want` naming `needle` on its standard error, and writes nothing."""
    up = run_fx_step(t, "up")
    add(f"{label}: up exits {want} naming why, and writes nothing",
        up.returncode == want and needle in up.stderr and check_fx_quiet(t), up.stdout + up.stderr)


def arm_escape(base, add):
    t = build_fact_fixture(base)
    (t / DEPLOY).write_text("[answers]\nmanifest_path = \"../outside.md\"\n", encoding="utf-8", newline="\n")
    write_fx_commit(t, "an answer leaving the target")
    check_fx_refused(add, "[S5] a manifest_path leaving the target", t, 1, "no step may write it")


def arm_bad_deploy(base, add):
    t = build_fact_fixture(base)
    (t / DEPLOY).write_text("[answers\n", encoding="utf-8", newline="\n")
    write_fx_commit(t, "a descriptor that does not parse")
    check_fx_refused(add, "[S5] a deploy.toml that does not parse", t, 1, "does not parse")


def arm_not_utf8(base, add):
    t = build_fact_fixture(base)
    (t / FX_MANIFEST).write_bytes(b"## \xa7B\n\n- a \xff byte\n")
    write_fx_commit(t, "a manifest that is not UTF-8")
    check_fx_refused(add, "[S5] a manifest that is not UTF-8", t, 1, "is not UTF-8")


def arm_duplicate(base, add):
    t = build_fact_fixture(base)
    write_fx_units(t, derive_fx_rows(1, 60))
    write_fx_commit(t, "an overlay already holding f01")
    check_fx_refused(add, "[S5] an overlay already holding a fact's tag", t, 2, "already holds")


def arm_pockets_refused(base, add):
    t = build_fact_fixture(base)
    (t / OVERLAY).write_text('[[unit]]\ntag = "repo.barred"\nlevel = 1\ntype = "constraint"\nscope = ["reader.card"]\n'
                             'text = "Holds `x`."\nenforced-by = "none — a fixture"\n', encoding="utf-8", newline="\n")
    write_fx_commit(t, "an overlay the reader refuses")
    p = run_fx_pockets(t, "--all")
    add("[S3] a refused overlay read exits 1 with one line naming it",
        p.returncode == 1 and len(p.stdout.splitlines()) == 1 and p.stdout.startswith("pockets: refused · "),
        p.stdout + p.stderr)
    bad = run_fx_pockets(t, "--room", "x")
    add("[S3] a malformed argv exits 2", bad.returncode == 2, bad.stdout[:200] + bad.stderr)


PLANTS = {"up": arm_up, "pockets-level": arm_pockets_level, "pockets-cap": arm_pockets_cap, "card": arm_card,
          "card-no-playbook": arm_card_no_playbook, "refused": arm_refused, "template": arm_template,
          "no-answer": arm_no_answer, "no-kit": arm_no_kit, "down": arm_down, "card-cap": arm_card_cap,
          "escape": arm_escape, "bad-deploy": arm_bad_deploy, "not-utf8": arm_not_utf8, "duplicate": arm_duplicate,
          "pockets-refused": arm_pockets_refused}


def run_fixture(plant=None) -> tuple[list, int]:
    """Each named case, or every case, in its own throwaway repository; one line per check."""
    lines, bad = [], 0
    for name in [plant] if plant else list(PLANTS):
        base = pathlib.Path(tempfile.mkdtemp(prefix="kf-fx-"))

        def add(label, ok, detail=""):
            nonlocal bad
            lines.append(f"{'ok  ' if ok else 'FAIL'} {name}: {label}")
            if not ok:
                bad += 1
                lines.extend(f"    {ln}" for ln in str(detail).splitlines()[:12])
        try:
            PLANTS[name](base, add)
        except (subprocess.SubprocessError, OSError, ValueError, KeyError, Refusal) as e:
            add(f"the case ran to its end ({type(e).__name__}: {e})", False)
        finally:
            try:  # git writes its objects read-only, which Windows will not unlink until they are writable
                shutil.rmtree(base, onexc=lambda func, p, _e: (os.chmod(p, 0o700), func(p)))
            except OSError:
                pass  # ponytail: a handle still open on the scratch tree leaves it to the system temp's sweep
    lines.append(f"{SAY}: fixture · {len(lines)} line(s) · {bad} failed")
    return lines, 1 if bad else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["--fixture"] and (len(argv) == 1 or (len(argv) == 3 and argv[1] == "--plant")):
        plant = argv[2] if len(argv) == 3 else None
        if plant is not None and plant not in PLANTS:
            sys.stderr.write(f"{SAY}: no plant {plant!r}; the plants are {', '.join(PLANTS)}\n")
            return 2
        lines, rc = run_fixture(plant)
        print("\n".join(lines))
        return rc
    verbs = {"up": cmd_up, "down": cmd_down, "witness": cmd_witness}
    if len(argv) != 2 or argv[0] not in verbs:
        sys.stderr.write("usage: python kickoff_facts_to_overlay.py up|down|witness <target> | --fixture [--plant <case>]\n")
        return 2
    try:
        return verbs[argv[0]](pathlib.Path(argv[1]).resolve())
    except Refusal as e:
        sys.stderr.write(f"{SAY}: {argv[0]} refused · {e}\n")
        return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    raise SystemExit(main(sys.argv[1:]))
