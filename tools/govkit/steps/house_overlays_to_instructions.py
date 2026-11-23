#!/usr/bin/env python3
"""house_overlays_to_instructions.py — the upgrade step `roles/house-overlays-to-instructions` (TOOL-dBoundRoles-19).

    python <gov tool root>/govkit/steps/house_overlays_to_instructions.py up|down|witness <target> <prefix>

Its row is the roles kit descriptor's `[[upgrade]]`. A repository's own rules for a role lived in a seeded
house text file of the roles kit, `house/<slot>.md`, appended to the role under `## House rules`; they now
live in the repository's one instruction overlay, `.governance/instructions.toml`, as level-5 units
selecting the role, which the role render places between the marked pair. `<prefix>` is the target's
install prefix, the roles kit found under it by `resolve_kit_dir`, so a kit homed under another name is
found through the receipt. `house/policy.toml` is no house text file and stays.

THE ROWS. A non-empty `house/<slot>.md` becomes one row: `tag = "repo.house.<slot>"`, `level` the ladder's
`role` level, `type = "adopter-rule"`, `scope = ["role.<slot>"]`, `budget = "block"` and `text`, the file's
body with CRLF folded, a leading byte-order mark and its edge newlines cut, `{{MEMORY_ROOT}}` kept. The
playbook kit's unit grammar admits an `adopter-rule` at that level under that budget alone
(`instruction_units.ADOPTER_RULE_LEVELS`), and holds its text to that budget's bytes.

THE UP. No roles kit under `<prefix>`, or one holding no house text file: exit 0, nothing written. It
refuses, exit 1 and nothing written, the before-image included: a body that is not UTF-8, a body over the
budget's bytes, each naming the file, and rows the instruction-unit grammar or the overlay reader refuses.
A tag the overlay already holds at the `role` level with a byte-equal text is skipped and its file still
removed, so a re-run over an up killed between the two converges (TOOL-dBoundRoles-43 S38, §8 F12); a held
tag carrying other text is the writer's own refusal, exit 2, naming it, both files left byte-identical. The
rows are placed by `derive_overlay_text`, the function `write_overlay_units` writes through, so a re-run
over a killed up recomputes the before-image's after-state and converges. An empty file is removed and
writes no unit. The overlay is written first and the house files removed LAST, so the witness changes last.

THE DOWN restores every path from the before-image (`write_from_before_image`): each house file and the
overlay byte-identical, the overlay removed where the up created it; a path edited since the up refuses
the whole down, exit 1, naming it, and nothing is restored.

THE WITNESS exits 0 when the roles kit holds no house text file and, for each house text file the
before-image recorded as holding text, the overlay holds a level-5 unit tagged `repo.house.<slot>`,
whatever its text now says: an adopter's later edit of the unit is the overlay's to grade. 1 otherwise.
It reads the working tree and runs no target code.

WHAT IT DOES NOT CHECK: that a held unit still says what its house file said, or still selects its role;
a unit re-tagged since the up reads not applied.

Exit 0 done, 1 refused or not applied, naming why, 2 a usage error or the writer's duplicate-tag refusal.
"""

import base64
import importlib.util
import json
import pathlib
import sys

STEP_ID = "roles/house-overlays-to-instructions"
SAY = "house-overlays"
OVERLAY = ".governance/instructions.toml"
ROLES_HOME = "roles"
HOUSE_DIR = "house"
TAG_HEAD = "repo.house."
SCOPE_HEAD = "role."
LEVEL_NAME = "role"
BUDGET = "block"
BOM = chr(0xFEFF)
GOV = pathlib.Path(__file__).resolve().parents[2]  # `{gov}`: the tool root this step ships in


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
    its reader, its writer and, through it, the unit grammar."""
    kit = STEPS.resolve_kit_dir("playbook", "overlay.py", GOV)
    if str(kit) not in sys.path:
        sys.path.insert(0, str(kit))
    import overlay
    return overlay


def read_roles_kit(target: pathlib.Path, prefix: str) -> pathlib.Path | None:
    """The roles kit's directory in `target` under the install prefix `prefix`, None where none is."""
    try:
        kit = STEPS.resolve_kit_dir(ROLES_HOME, "roles_lib.py", target / prefix)
    except LookupError:
        return None
    return kit if target in kit.parents else None


def read_house_files(target: pathlib.Path, kit: pathlib.Path | None) -> list[str]:
    """The target-relative path of each house text file, `house/*.md`, of the roles kit at `kit`, sorted;
    [] where there is no kit."""
    if kit is None:
        return []
    return sorted(p.relative_to(target).as_posix() for p in (kit / HOUSE_DIR).glob("*.md") if p.is_file())


def derive_house_rows(bodies: dict, iu) -> list[dict]:
    """One overlay row per non-empty body of `bodies`, `{target-relative path: bytes}`, in path order, `iu`
    the playbook kit's unit grammar; a body that is not UTF-8, one over the budget's bytes and a row the
    grammar's `check_statement` reds are one refusal naming each file."""
    level, limit = iu.LEVELS.index(LEVEL_NAME), iu.BUDGET_BYTES[BUDGET]
    rows, refused = [], []
    for rel, data in sorted(bodies.items()):
        try:
            text = data.decode("utf-8").removeprefix(BOM).replace("\r\n", "\n").strip("\n")
        except UnicodeDecodeError:
            refused.append(f"{rel}: is not UTF-8 text, so no unit can carry it; remedy: re-save it as UTF-8, "
                           f"commit, and re-run the step")
            continue
        if not text.strip():
            continue
        size = len(text.encode("utf-8"))
        if size > limit:
            refused.append(f"{rel}: its body is {size} bytes, over the {limit} bytes a `{BUDGET}` unit holds; "
                           f"remedy: shorten it, commit, and re-run the step")
            continue
        slot = pathlib.PurePosixPath(rel).stem
        row = {"tag": TAG_HEAD + slot, "level": level, "type": iu.ADOPTER_RULE, "scope": [SCOPE_HEAD + slot],
               "budget": BUDGET, "text": text}
        refused += [f"{rel}: {red}" for red in iu.check_statement(row)]
        rows.append(row)
    if refused:
        raise Refusal("\n".join(refused))
    return rows


def remove_held_rows(rows: list[dict], overlay: str, iu) -> list[dict]:
    """`rows` less each whose tag the overlay text `overlay` already holds at the ladder's `role` level with a
    byte-equal text (TOOL-dBoundRoles-43 S38, §8 F12): a unit a killed up already wrote, whose house file the
    up still removes, so a re-run converges on its own partial state. A row whose held tag carries other
    text, or sits at another level, is kept, so the writer's duplicate-tag refusal names the tag, exit 2,
    nothing written."""
    if not overlay.strip():
        return rows
    held = {u.tag: u.text for u in iu.parse_unit_rows(overlay, OVERLAY)[0]
            if u.level == iu.LEVELS.index(LEVEL_NAME)}
    return [r for r in rows if held.get(r["tag"]) != r["text"]]


def cmd_up(target: pathlib.Path, prefix: str) -> int:
    kit = read_roles_kit(target, prefix)
    rels = read_house_files(target, kit)
    if not rels:
        print(f"{SAY}: up · no house text file in a roles kit under '{prefix or '.'}', so there is nothing to move")
        return 0
    ov = load_overlay()
    written = set()   # the tags the after-state writes, for the closing line

    def derive_after(before):
        def read(rel):
            if before is not None:
                return before.get(rel)
            p = target / rel
            return p.read_bytes() if p.is_file() else None

        house = [rel for rel in (sorted(before) if before is not None else rels) if rel != OVERLAY]
        rows = derive_house_rows({rel: read(rel) or b"" for rel in house}, ov.iu)
        rows = remove_held_rows(rows, (read(OVERLAY) or b"").decode("utf-8"), ov.iu)
        written.update(r["tag"] for r in rows)
        after = dict.fromkeys(house)
        if rows:
            out = ov.derive_overlay_text((read(OVERLAY) or b"").decode("utf-8"), rows)
            try:
                ov.read_overlay(target, candidate=out)
            except ov.OverlayRefused as e:
                raise Refusal(f"the overlay reader refuses the house rows of {', '.join(house)}:\n{e}") from None
            after[OVERLAY] = out.encode("utf-8")
        return after

    try:
        after = STEPS.write_before_image(target, STEP_ID, derive_after)
    except ov.OverlayRefused as e:
        sys.stderr.write(f"{SAY}: up refused · {e}\n")
        return e.code
    if after.get(OVERLAY) is not None:
        (target / OVERLAY).parent.mkdir(parents=True, exist_ok=True)
        (target / OVERLAY).write_bytes(after[OVERLAY])
    moved = sorted(rel for rel in after if rel != OVERLAY)
    for rel in moved:  # LAST: the witness reads the house files' absence
        (target / rel).unlink(missing_ok=True)
    tags = sorted(written)
    print(f"{SAY}: up · {len(moved)} house text file(s) removed; {len(tags)} written to {OVERLAY} as level-"
          f"{ov.iu.LEVELS.index(LEVEL_NAME)} unit(s){': ' + ', '.join(tags) if tags else ''}")
    return 0


def cmd_down(target: pathlib.Path, prefix: str) -> int:
    restored = STEPS.write_from_before_image(target, STEP_ID)
    print(f"{SAY}: down · restored {', '.join(restored) or 'nothing: no before-image, no up applied'}")
    return 0


def cmd_witness(target: pathlib.Path, prefix: str) -> int:
    left = read_house_files(target, read_roles_kit(target, prefix))
    if left:
        print(f"{SAY}: witness · {left[0]} is still a house text file: not applied")
        return 1
    image = STEPS.derive_image_path(target, STEP_ID)
    want = []
    if image.is_file():
        paths = json.loads(image.read_text(encoding="utf-8"))["paths"]
        want = sorted(TAG_HEAD + pathlib.PurePosixPath(rel).stem for rel, v in paths.items()
                      if rel != OVERLAY and v.get("before")
                      and base64.b64decode(v["before"]).decode("utf-8", "replace").removeprefix(BOM).strip())
    if not want:
        print(f"{SAY}: witness · no house text file, and none moved held a rule: applied")
        return 0
    iu = load_overlay().iu
    path = target / OVERLAY
    units = iu.parse_unit_rows(path.read_bytes().decode("utf-8"), OVERLAY)[0] if path.is_file() else []
    tags = {u.tag for u in units if u.level == iu.LEVELS.index(LEVEL_NAME)}
    lost = [tag for tag in want if tag not in tags]
    if lost:
        print(f"{SAY}: witness · {len(lost)} moved house text(s) hold no level-"
              f"{iu.LEVELS.index(LEVEL_NAME)} unit by their tag: {', '.join(lost)}: not applied")
        return 1
    print(f"{SAY}: witness · no house text file, and each of the {len(want)} moved holds its unit's tag: applied")
    return 0


def main(argv: list[str]) -> int:
    verbs = {"up": cmd_up, "down": cmd_down, "witness": cmd_witness}
    if len(argv) != 3 or argv[0] not in verbs:
        sys.stderr.write("usage: python house_overlays_to_instructions.py up|down|witness <target> <prefix>\n")
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
