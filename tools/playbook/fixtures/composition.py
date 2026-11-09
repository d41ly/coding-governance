#!/usr/bin/env python3
"""composition.py — the plants of PLAY-dOrderedCharter-34's composition: one scratch tree, one render each.

    python composition.py --plant <case> [--enforce warn|refuse]

Each plant builds a throwaway repository on `main` holding a gov kit `alpha` with its units, the repository's
overlay, the charter template where the render reads it first, the renderer kit's directory in the tree, and
the deploy answers, commits it, renders the charter through `render_playbook.main` (or `render` where the plant
names its own `gov_root`), and checks what the criterion names. The cases: `project-block` (AC1), `marked-part`
and `unplaced` (AC2), `level-6` (AC3), `over-budget` (AC4, `--enforce` the `budgets.enforce` it commits),
`over-codex` (AC5), `alias-copy` (AC6), `seeded-template` and `installed-template` (AC7), and `delta` (AC8),
whose rows are `row_kind.py`'s fixture kind.

Exit 0 every expectation held · 1 one failed · 2 usage or a plant that could not be built.
"""
from __future__ import annotations

import argparse
import pathlib
import shutil
import sys
import tempfile

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
import instruction_units as iu  # noqa: E402
import overlay as ov  # noqa: E402
import render_playbook as rp  # noqa: E402

SAY = "composition"
KIT = iu.derive_tool_rel("alpha")
SLOT = "# fixture — agent charter\n\n{filler}\n<!-- units: reader.every -->\n"
BLOCK = "# fixture — agent charter\n\n## This repository's own rules\n\n<!-- one-line -->\n{{ADOPTER_RULES}}\n<!-- /one-line -->\n"
GOV4 = (("unit.four-a", 4, "MUST hold four a."), ("unit.four-b", 4, "MUST hold four b."))
REPO4 = (("repo.four", 4, "MUST mind the local four."),)
LEVEL0 = (("repo.zeta", 0, "MUST mind the zeta rule."), ("repo.alpha", 0, "MUST mind the alpha rule."))
KEYED = 'kits = ["lexicon"]\n\n[charter]\nadopter_rules = """\n- The key\'s first rule.\n- The key\'s second rule.\n"""\n'
DEPLOY = 'kits = ["lexicon"]\n'
#: The planted totals: AC5's PINNED 33210, and a figure between the charter's 20480 cap and Codex's limit.
OVER_CODEX, OVER_BUDGET = 33210, 21311


def build_tree(c, gov=(), overlay=(), template=SLOT.format(filler=""), deploy=DEPLOY, files=None):
    """Commit one tree: gov's kit `alpha` holding `gov`'s units, the overlay holding `overlay`'s where any, the
    template at the renderer kit's directory, the deploy answers and `files` beside them."""
    rows = "".join(ov.render_fx_row(t, lvl, text) for t, lvl, text in gov)
    plan = {f"{KIT}/kit.toml": 'id = "alpha"\n', f"{KIT}/instructions.toml": rows or "\n",
            iu.derive_template_rel(): template, ".governance/deploy.toml": deploy, **(files or {})}
    if overlay:
        plan[iu.OVERLAY] = "".join(ov.render_fx_row(t, lvl, text) for t, lvl, text in overlay)
    for rel, text in plan.items():
        c.write_file(rel, text)
    iu.run_commit(c.top, "the fixture")


def read_block(top) -> list:
    """The lines between the charter's one-line markers."""
    text = (top / rp.CANON).read_text(encoding="utf-8")
    return text.split(rp.ONE_LINE_OPEN + "\n", 1)[1].split("\n" + rp.ONE_LINE_CLOSE, 1)[0].splitlines()


def arm_project_block(c, _a):
    build_tree(c, overlay=LEVEL0, template=BLOCK, deploy=KEYED)
    rc, said = iu.run_render(c.top)
    got = read_block(c.top) if rc == 0 else []
    c.check("the key's lines, then the level-0 units' in overlay order, all inside the block",
            got == ["- The key's first rule.", "- The key's second rule.", "- MUST mind the zeta rule.",
                    "- MUST mind the alpha rule."], f"rc {rc} · {got} · {said}")
    build_tree(c, overlay=LEVEL0, template=BLOCK)
    rc, said = iu.run_render(c.top)
    got = read_block(c.top) if rc == 0 else []
    c.check("with the key unanswered, the units alone and no default bullet",
            got == ["- MUST mind the zeta rule.", "- MUST mind the alpha rule."], f"rc {rc} · {got} · {said}")


def arm_marked_part(c, _a):
    build_tree(c, GOV4, REPO4)
    rc, said = iu.run_render(c.top)
    first = (c.top / rp.CANON).read_bytes() if rc == 0 else b""
    want = (f"MUST hold four a.\nMUST hold four b.\n{rp.REPO_OPEN}\nMUST mind the local four.\n{rp.REPO_CLOSE}\n"
            .encode("utf-8"))
    c.check("gov's units, then the repository's once between the marked pair",
            want in first and first.count(b"MUST mind the local four.") == 1, f"rc {rc} · {first!r} · {said}")
    rc, said = iu.run_render(c.top)
    again = (c.top / rp.CANON).read_bytes() if rc == 0 else b""
    c.check("a second render leaves the document byte-identical, no second pair", again == first
            and again.count(rp.REPO_OPEN.encode("utf-8")) == 1, f"rc {rc} · {again!r}")


def arm_unplaced(c, _a):
    build_tree(c, GOV4, REPO4, template="# fixture — agent charter\n\nno unit slot here\n")
    rc, said = iu.run_render(c.top)
    notes = [ln for ln in said.splitlines() if "unplaced" in ln]
    c.check("one unplaced note naming the unit, exit 0", rc == 0 and len(notes) == 1 and "repo.four" in notes[0]
            and "level 4" in notes[0], f"rc {rc} · {said}")


def arm_level_6(c, _a):
    build_tree(c, GOV4, (("repo.task", 6, "MUST write the task."),))
    rc, said = iu.run_render(c.top)
    c.check("a repository unit at level 6 refuses, naming it and its level",
            rc == 1 and "repo.task" in said and "level 6" in said, f"rc {rc} · {said}")


def build_sized(c, total, enforce):
    """A tree whose charter composes to exactly `total` bytes: gov's template padded, five gov units of 200
    bytes a line and repository units of 191, near 14290 bytes over Codex's limit and 2391 under it, each
    unit inside its 200-byte text budget, and `budgets.enforce` committed."""
    gov = tuple((f"unit.wide-{n}", 4, "G" * 199) for n in range(5))
    repo = tuple((f"repo.wide-{n}", 4, "R" * 190) for n in range((14290 if total > 32768 else 2391) // 191))
    policy = {".governance/policy.toml": f'[budgets]\nenforce = "{enforce}"\n"AGENTS.md" = 20480\n'}
    build_tree(c, gov, repo, files=policy)
    body = rp.render(pathlib.Path(rp.__file__).resolve().parent, c.top, c.top)[0]
    pad = total - len(rp.build_region(None, body).encode("utf-8"))
    build_tree(c, gov, repo, template=SLOT.format(filler="P" * pad), files=policy)


def arm_over_budget(c, a):
    build_sized(c, OVER_BUDGET, a.enforce)
    rc, said = iu.run_render(c.top)
    over = [ln for ln in said.splitlines() if " BUDGET " in ln]
    if a.enforce == "refuse":
        c.check("under refuse: exit 1 and no file written", rc == 1 and not (c.top / rp.CANON).exists(),
                f"rc {rc} · {said}")
        return
    line = over[0] if len(over) == 1 else ""
    c.out.append(f"{SAY}:   {line.strip()}")
    sizes = [int(p.rsplit(" ", 1)[1]) for p in line.partition("largest: ")[2].split(" · ") if p]
    c.check("under warn: exit 0, one budget line naming the cap's key and the origins, largest first",
            rc == 0 and line.strip().startswith("budget") and 'budgets."AGENTS.md"' in line
            and f"{OVER_BUDGET} bytes" in line and len(sizes) == 3 and sizes == sorted(sizes, reverse=True)
            and "repository" in line and "gov:alpha" in line, f"rc {rc} · {said}")


def arm_over_codex(c, a):
    build_sized(c, OVER_CODEX, a.enforce)
    rc, said = iu.run_render(c.top)
    refused = [ln for ln in said.splitlines() if "REFUSED" in ln]
    c.out += [f"{SAY}:   {ln.strip()}" for ln in refused]
    c.check("over Codex's limit under warn: exit 1, one REFUSED line naming CODEX_MAX and the origins, no file",
            rc == 1 and len(refused) == 1 and "CODEX_MAX" in refused[0] and f"{OVER_CODEX} bytes" in refused[0]
            and "largest: gov:playbook" in refused[0] and "repository 14" in refused[0]
            and not (c.top / rp.CANON).exists(), f"rc {rc} · {said}")


def arm_alias_copy(c, _a):
    build_tree(c, GOV4)
    rc, said = iu.run_render(c.top)
    c.write_file("GEMINI.md", (c.top / rp.CANON).read_text(encoding="utf-8"))
    iu.run_git(c.top, "add", "--", rp.CANON, iu.LOCK)
    iu.run_commit(c.top, "the render and its copy")
    build_tree(c, (("unit.four-a", 4, "MUST hold four a, now changed."), GOV4[1]))
    rc, said = iu.run_render(c.top, "--check")
    c.check("--check reds the copy left with last render's bytes, naming it", rc == 1 and "GEMINI.md" in said,
            f"rc {rc} · {said}")
    rc, said = iu.run_render(c.top)
    canon = (c.top / rp.CANON).read_bytes()
    c.check("the render re-writes the copy as the composition in the same run",
            rc == 0 and (c.top / "GEMINI.md").read_bytes() == canon and b"now changed" in canon, f"rc {rc} · {said}")
    rc, said = iu.run_render(c.top, "--check")
    c.check("--check is green once the copy is the composition", rc == 0, f"rc {rc} · {said}")


def arm_seeded_template(c, _a):
    tpl = "# fixture — agent charter\n\n- MUST land from the kit's copy.\n"
    seed = {"SEED.md": "# an edited seed\n\n- MUST NOT land from the seed.\n"}
    build_tree(c, template=tpl, deploy=DEPLOY + '\n[answers]\nplaybook_path = "SEED.md"\n', files=seed)
    rc, said = iu.run_render(c.top)
    answered = (c.top / rp.CANON).read_bytes() if rc == 0 else b""
    retired = [ln for ln in said.splitlines() if ln.strip().startswith("retired") and "playbook_path" in ln]
    build_tree(c, template=tpl, files=seed)
    rc2, said2 = iu.run_render(c.top)
    plain = (c.top / rp.CANON).read_bytes() if rc2 == 0 else b"-"
    c.check("the composition is byte-identical with and without the answer, no byte of the seed in it",
            answered == plain and b"MUST NOT land" not in answered, f"{said} {said2}")
    c.check("one retired note names playbook_path", len(retired) == 1, said)


def arm_installed_template(c, _a):
    build_tree(c, template="# fixture — agent charter\n\n- MUST land from the installed copy.\n")
    empty = c.top.parent / f"{c.top.name}-gov"
    empty.mkdir()
    engine = pathlib.Path(rp.__file__).resolve().parent
    try:
        body = rp.render(engine, empty, c.top)[0]
        c.check("an install renders from the kit's copy, gov_root holding nothing",
                "MUST land from the installed copy." in body, body)
        (c.top / iu.derive_template_rel()).unlink()
        try:
            rp.render(engine, empty, c.top)
            said = "no refusal"
        except rp.Refusal as exc:
            said = str(exc)
        c.check("with the copy removed the render refuses, exit 1, naming both paths",
                iu.derive_template_rel() in said and f"{empty.as_posix()}/{rp.TEMPLATE_NAME}" in said, said)
    finally:
        shutil.rmtree(empty, ignore_errors=True)


def arm_delta(c, _a):
    import row_kind as rk
    delta, zeta = rk.STATE_GOV[3], rk.STATE_GOV[5]
    narrow = '{ grants = ["read"] }'
    over = "\n".join([rk.render_patch("fixture.adopter.alpha-tuned", rk.GOV[0], remove='{ needs = ["fixture.beta"] }'),
                      rk.render_patch("fixture.adopter.gamma-own", rk.GOV[2], "supersedes", grants=["write"],
                                      needs=[], ceiling="low"),
                      rk.render_patch("fixture.adopter.delta-tuned", delta, remove=narrow),
                      rk.render_patch("fixture.adopter.zeta-tuned", zeta, remove=narrow)])
    rk.build_tree(c.top, gov=rk.STATE_GOV, overlay=over, exclude="fixture.beta")
    new = {**delta, "grants": ["read", "write"]}
    rk.build_next(c.top, rk.STATE_GOV[:3] + [new, rk.STATE_GOV[4]],
                  [(delta["tag"], "edit", delta, [new], None), (zeta["tag"], "remove", zeta, [], "none", "editorial")])
    try:
        lines = rp.render_delta_report(c.top)
    except rp.Refusal as exc:
        lines = [f"refused: {exc}"]
    c.out += [f"{SAY}:   {ln}" for ln in lines]
    words = [ln.split()[0] for ln in lines]
    c.check("one state line per S22 state and one widening line",
            all(words.count(s) == 1 for s in rp.DELTA_STATES) and words.count(rp.WIDENING) == 1, " | ".join(lines))
    c.check("each line in update's verdict widths", bool(lines) and all(
        ln[:20] == f"  {ln.split()[0]:<18}" and ln[20:22] == " [" and ln[35] == "]" for ln in lines), " | ".join(lines))


PLANTS = {"project-block": arm_project_block, "marked-part": arm_marked_part, "unplaced": arm_unplaced,
          "level-6": arm_level_6, "over-budget": arm_over_budget, "over-codex": arm_over_codex,
          "alias-copy": arm_alias_copy, "seeded-template": arm_seeded_template,
          "installed-template": arm_installed_template, "delta": arm_delta}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="composition.py")
    ap.add_argument("--plant", required=True, choices=list(PLANTS))
    ap.add_argument("--enforce", default="warn", choices=("warn", "refuse"))
    a = ap.parse_args(argv)
    iu.load_memory_tree_path()
    from deviation_join import set_env_aside
    from tree_lib import GIT_ENV_LEAKS
    out = [f"{SAY}: plant {a.plant} · enforce {a.enforce}"]
    top = pathlib.Path(tempfile.mkdtemp(prefix="compose-"))
    try:
        with set_env_aside(GIT_ENV_LEAKS):
            iu.run_git(top, "init", "-q", "-b", "main")
            iu.run_git(top, "config", "core.autocrlf", "false")
            case = iu.Case(top, out)
            try:
                PLANTS[a.plant](case, a)
            except (ValueError, OSError, RuntimeError, rp.Refusal) as exc:   # a plant that raises was not built
                out.append(f"{SAY}: plant {a.plant} could not be built: {type(exc).__name__}: {exc}")
                case.failed, rc = case.failed or 1, 2
            else:
                rc = 1 if case.failed else 0
    finally:
        shutil.rmtree(top, ignore_errors=True)
    out.append(f"{SAY}: {'FAILED' if rc else 'green'} · exit {rc}")
    sys.stdout.buffer.write("".join(f"{ln}\n" for ln in out).encode("utf-8"))
    return rc


if __name__ == "__main__":
    sys.exit(main())
