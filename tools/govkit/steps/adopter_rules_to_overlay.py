#!/usr/bin/env python3
"""adopter_rules_to_overlay.py — the upgrade step `playbook/adopter-rules-to-overlay` (PLAY-dOrderedCharter-31, S4).

    python <prefix>/govkit/steps/adopter_rules_to_overlay.py up|down|witness <target>

Its row is the playbook descriptor's `[[upgrade]]`. The UP turns each `- ` line of `[charter] adopter_rules`
in `.governance/deploy.toml` into one level-0 `repo.` unit of `.governance/instructions.toml` and takes the
key out of the descriptor; the DOWN restores both files byte-identical from the before-image; the WITNESS
exits 0 when the key is absent and every line the before-image's key held is a unit's text.

THE ROWS. Line `n` of the key becomes `tag = "repo.rule-<NN>-<seg>"`, `level = 0`, `type = "directive"`,
`scope = ["reader.every"]` and `text`, the line with its leading `- ` cut. `<NN>` is `n` zero-padded to two
digits, or to the key's line count's digit count past 99 lines; `<seg>` is the text folded by the tag index's
`derive_heading_seg`, cut at 40 bytes, its trailing `-` trimmed, and an empty fold takes `repo.rule-<NN>`.
So the tags' byte order is the rules' order, the order the overlay writer's level-then-tag placement keeps,
and the project block, which renders the key's lines and then the every-reader level-0 units in overlay
order, renders the same lines in the same order on either side of the step.

THE UP, in order. No `[charter]` table or no `adopter_rules` key: exit 0, nothing written. It refuses, exit 1
and nothing written: a key line that is not a `- ` line; an overlay level-0 unit whose tag sorts below the
last converted tag, which the block rendered after the key's lines and the writer would place among them;
and a row the overlay reader refuses, a line over the one-line budget among them. A tag the overlay already
holds is the writer's own refusal, exit 2. The rows are placed by `derive_overlay_text`, the function
`write_overlay_units` writes through, so a re-run over a killed up recomputes the before-image's after-state
and converges. The key leaves `deploy.toml` by a line edit that keeps every other byte, written LAST, so the
witness changes last.

Exit 0 done, 1 refused naming why (nothing written), 2 a usage error or the writer's duplicate-tag refusal.
"""

import base64
import importlib.util
import json
import pathlib
import re
import sys
import tomllib

STEP_ID = "playbook/adopter-rules-to-overlay"
DEPLOY = ".governance/deploy.toml"
OVERLAY = ".governance/instructions.toml"
KEY = "adopter_rules"
SEG_MAX = 40
GOV = pathlib.Path(__file__).resolve().parents[2]  # `{gov}`: the tool root this step ships in
HEADER_RE = re.compile(r"^\s*\[")


def load_steps():
    """The step reader beside this file's directory, imported by its path: the runner's `-I` drops
    this file's own directory from `sys.path`, and the before-image helpers live there."""
    path = pathlib.Path(__file__).resolve().parents[1] / "upgrade_steps.py"
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
    """The playbook kit's overlay module, found through the sibling-kit resolver the step reader carries:
    its reader, its writer and, through it, the unit grammar and the tag index's fold."""
    kit = STEPS.resolve_kit_dir("playbook", "overlay.py", GOV)
    if str(kit) not in sys.path:
        sys.path.insert(0, str(kit))
    import overlay
    return overlay


def parse_rules(deploy: bytes):
    """(the `adopter_rules` lines, the key as the table spells it), or None where the descriptor has no
    `[charter]` table or no such key; a line that is not a `- ` line is a refusal naming it."""
    try:
        doc = tomllib.loads(deploy.decode("utf-8").removeprefix("\ufeff"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as e:
        raise Refusal(f"{DEPLOY}: does not parse ({e})") from None
    table = doc.get("charter")
    if not isinstance(table, dict):
        return None
    spelled = next((k for k in table if k.lower() == KEY), None)
    if spelled is None:
        return None
    value = table[spelled]
    if not isinstance(value, str):
        raise Refusal(f"{DEPLOY}: [charter] {spelled} is not a string")
    lines = value.rstrip("\n").split("\n") if value.strip() else []
    for n, ln in enumerate(lines, 1):
        if not ln.startswith("- "):
            raise Refusal(f"{DEPLOY}: [charter] {spelled} line {n} ({ln!r}) is not a `- ` line, and the "
                          f"project block renders a unit only as `- <text>`, so converting it would change the block")
    return lines, spelled


def derive_rule_tag(n: int, width: int, text: str, fold) -> str:
    """Rule `n`'s tag: `repo.rule-<NN>-<seg>`, `<NN>` `n` padded to `width`, `<seg>` the fold cut at 40 bytes."""
    seg = fold(text)[:SEG_MAX].rstrip("-")
    return f"repo.rule-{n:0{width}d}" + (f"-{seg}" if seg else "")


def derive_rule_rows(lines: list[str], fold) -> list[dict]:
    """One overlay row per rule line, in the rules' order."""
    width = max(2, len(str(len(lines))))
    return [{"tag": derive_rule_tag(n, width, ln[2:], fold), "level": 0, "type": "directive",
             "scope": ["reader.every"], "text": ln[2:]} for n, ln in enumerate(lines, 1)]


def render_deploy_rest(deploy: bytes, spelled: str) -> bytes:
    """`deploy.toml`'s bytes with the `[charter]` key's lines taken out and every other byte kept; a cut
    that leaves anything else changed is a refusal."""
    text = deploy.decode("utf-8")
    lines = text.splitlines(keepends=True)
    key_re = re.compile(rf"^\s*{re.escape(spelled)}\s*=\s*(.*)$", re.S)
    table, start = None, None
    for i, ln in enumerate(lines):
        if HEADER_RE.match(ln):
            table = ln.strip()
        elif table == "[charter]" and key_re.match(ln.rstrip("\r\n")):
            start = i
            break
    if start is None:
        raise Refusal(f"{DEPLOY}: [charter] {spelled} is not a line this step can cut")
    rest = key_re.match(lines[start].rstrip("\r\n"))[1]
    end = start
    for quote in ('"""', "'''"):
        if rest.startswith(quote):
            if rest.count(quote) < 2:
                end = next((j for j in range(start + 1, len(lines)) if quote in lines[j]), None)
                if end is None:
                    raise Refusal(f"{DEPLOY}: [charter] {spelled}'s value never closes")
            break
    out = "".join(lines[:start] + lines[end + 1:])
    want = tomllib.loads(text.removeprefix("\ufeff"))
    del want["charter"][spelled]
    if tomllib.loads(out.removeprefix("\ufeff")) != want:
        raise Refusal(f"{DEPLOY}: cutting [charter] {spelled}'s lines would change another key, so it is left")
    return out.encode("utf-8")


def check_overlay_order(units, rows) -> None:
    """A refusal where the overlay holds a level-0 unit whose tag sorts below the last converted tag: the
    block rendered it after the key's lines, and the writer would place it among or ahead of them."""
    last = rows[-1]["tag"]
    below = sorted(u.tag for u in units if u.level == 0 and u.tag and u.tag < last)
    if below:
        raise Refusal(f"{OVERLAY}: level-0 unit(s) {', '.join(below)} sort below {last}, so the converted rules "
                      f"would render after them and the block's order would change")


def cmd_up(target: pathlib.Path) -> int:
    deploy = target / DEPLOY
    found = parse_rules(deploy.read_bytes()) if deploy.is_file() else None
    if found is None:
        print(f"adopter-rules: up · no [charter] {KEY} in {DEPLOY}, so there is nothing to move")
        return 0
    ov = load_overlay()
    import tag_index

    def derive_after(before):
        data = before[DEPLOY] if before is not None else deploy.read_bytes()
        if before is not None:
            text = (before.get(OVERLAY) or b"").decode("utf-8")
        else:
            path = target / OVERLAY
            text = path.read_bytes().decode("utf-8") if path.is_file() else ""
        lines, spelled = parse_rules(data)
        after = {DEPLOY: render_deploy_rest(data, spelled)}
        if not lines:
            return after
        rows = derive_rule_rows(lines, tag_index.derive_heading_seg)
        units, faults = ov.iu.parse_unit_rows(text, OVERLAY)
        if faults:
            raise Refusal(f"{OVERLAY}: " + "; ".join(faults))
        check_overlay_order(units, rows)
        out = ov.derive_overlay_text(text, rows)
        try:
            ov.read_overlay(target, candidate=out)
        except ov.OverlayRefused as e:
            raise Refusal(f"the overlay reader refuses the converted rows:\n{e}") from None
        after[OVERLAY] = out.encode("utf-8")
        return after

    try:
        after = STEPS.write_before_image(target, STEP_ID, derive_after)
    except ov.OverlayRefused as e:
        sys.stderr.write(f"adopter-rules: up refused · {e}\n")
        return e.code
    if OVERLAY in after:
        (target / OVERLAY).parent.mkdir(parents=True, exist_ok=True)
        (target / OVERLAY).write_bytes(after[OVERLAY])
    deploy.write_bytes(after[DEPLOY])  # LAST: the witness reads the key's absence
    n = len(found[0])
    print(f"adopter-rules: up · {n} rule(s) moved to {OVERLAY} as level-0 repo.rule- units · "
          f"[charter] {found[1]} taken out of {DEPLOY}")
    return 0


def cmd_down(target: pathlib.Path) -> int:
    restored = STEPS.write_from_before_image(target, STEP_ID)
    print(f"adopter-rules: down · restored {', '.join(restored) or 'nothing: no before-image, no up applied'}")
    return 0


def cmd_witness(target: pathlib.Path) -> int:
    deploy = target / DEPLOY
    if deploy.is_file() and parse_rules(deploy.read_bytes()) is not None:
        print(f"adopter-rules: witness · {DEPLOY} still holds [charter] {KEY}: not applied")
        return 1
    image = STEPS.derive_image_path(target, STEP_ID)
    held = []
    if image.is_file():
        before = json.loads(image.read_text(encoding="utf-8"))["paths"].get(DEPLOY, {}).get("before")
        found = parse_rules(base64.b64decode(before)) if before else None
        held = [ln[2:] for ln in found[0]] if found else []
    path = target / OVERLAY
    texts = set()
    if path.is_file():
        units, _faults = load_overlay().iu.parse_unit_rows(path.read_bytes().decode("utf-8"), OVERLAY)
        texts = {u.text for u in units if u.level == 0}
    lost = [t for t in held if t not in texts]
    if lost:
        print(f"adopter-rules: witness · {len(lost)} rule(s) the key held are no level-0 unit's text: not applied")
        return 1
    print(f"adopter-rules: witness · no [charter] {KEY}, and each of its {len(held)} rule(s) is a unit: applied")
    return 0


def main(argv: list[str]) -> int:
    verbs = {"up": cmd_up, "down": cmd_down, "witness": cmd_witness}
    if len(argv) != 2 or argv[0] not in verbs:
        sys.stderr.write("usage: python adopter_rules_to_overlay.py up|down|witness <target>\n")
        return 2
    try:
        return verbs[argv[0]](pathlib.Path(argv[1]).resolve())
    except Refusal as e:
        sys.stderr.write(f"adopter-rules: {argv[0]} refused · {e}\n")
        return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    raise SystemExit(main(sys.argv[1:]))
