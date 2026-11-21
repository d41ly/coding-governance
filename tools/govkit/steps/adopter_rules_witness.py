#!/usr/bin/env python3
"""adopter_rules_witness.py — the witness of `playbook/adopter-rules-to-overlay-2` (TOOL-dWitnessedBar-111).

    python <prefix>/govkit/steps/adopter_rules_witness.py witness <target>

The step succeeds `playbook/adopter-rules-to-overlay`, retired to it by the govkit registry's `[[retired]]`
row. Its up and its down are the predecessor's program, `adopter_rules_to_overlay.py`, unchanged: a landed
step's program is frozen, and only the witness was wrong. The predecessor's witness held every line its
before-image's `[charter] adopter_rules` key carried to a level-0 unit's TEXT, so an instruction edit of a
converted rule after the up read as the step never applied, and gov first refused every landing that
carried one (TOOL-dWitnessedBar-51 corrected rule 06's file name).

THE WITNESS exits 0 when the key is absent from `.governance/deploy.toml` and every line the before-image's
key held is either a level-0 unit's text or the tag the up derives for that line is a level-0 unit's tag:
the up names each rule `repo.rule-<NN>-<seg>` from the line's position and its text, so the tag is the
identity a later edit of the text keeps. The before-image is the predecessor's own, at its step id, since
the up writing it is the predecessor's program. It reads the predecessor's module by its path for every
name the up uses: the descriptor parser, the row derivation, the overlay reader and the tag index's fold.

WHAT IT DOES NOT CHECK: that an edited unit still means what the rule meant, and a rule whose unit was
re-tagged as well as re-worded, which reads not applied.

Exit 0 applied, 1 not applied or a refusal naming why, 2 a usage error.
"""

import base64
import importlib.util
import json
import pathlib
import sys

PREDECESSOR = "adopter_rules_to_overlay.py"


def load_predecessor():
    """The predecessor step's module, loaded by its path beside this file: the runner's `-I` drops this
    file's own directory from `sys.path`."""
    path = pathlib.Path(__file__).resolve().parent / PREDECESSOR
    spec = importlib.util.spec_from_file_location("adopter_rules_to_overlay", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def cmd_witness(pre, target: pathlib.Path) -> int:
    deploy = target / pre.DEPLOY
    if deploy.is_file() and pre.parse_rules(deploy.read_bytes()) is not None:
        print(f"adopter-rules: witness · {pre.DEPLOY} still holds [charter] {pre.KEY}: not applied")
        return 1
    image = pre.STEPS.derive_image_path(target, pre.STEP_ID)
    lines = []
    if image.is_file():
        before = json.loads(image.read_text(encoding="utf-8"))["paths"].get(pre.DEPLOY, {}).get("before")
        found = pre.parse_rules(base64.b64decode(before)) if before else None
        lines = found[0] if found else []
    if not lines:
        print(f"adopter-rules: witness · no [charter] {pre.KEY}, and its before-image held no rule: applied")
        return 0
    ov = pre.load_overlay()
    import tag_index
    rows = pre.derive_rule_rows(lines, tag_index.derive_heading_seg, ov.iu.ADOPTER_RULE)
    path = target / pre.OVERLAY
    units = []
    if path.is_file():
        units, _faults = ov.iu.parse_unit_rows(path.read_bytes().decode("utf-8"), pre.OVERLAY)
    texts = {u.text for u in units if u.level == 0}
    tags = {u.tag for u in units if u.level == 0}
    lost = [r["tag"] for r in rows if r["text"] not in texts and r["tag"] not in tags]
    if lost:
        print(f"adopter-rules: witness · {len(lost)} rule(s) the key held are no level-0 unit's text or "
              f"tag: {', '.join(lost)}: not applied")
        return 1
    edited = sum(1 for r in rows if r["text"] not in texts)
    print(f"adopter-rules: witness · no [charter] {pre.KEY}, and each of its {len(rows)} rule(s) is a unit, "
          f"{edited} of them edited since the up: applied")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[0] != "witness":
        sys.stderr.write("usage: python adopter_rules_witness.py witness <target>\n")
        return 2
    pre = load_predecessor()
    try:
        return cmd_witness(pre, pathlib.Path(argv[1]).resolve())
    except pre.Refusal as e:
        sys.stderr.write(f"adopter-rules: witness refused · {e}\n")
        return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    raise SystemExit(main(sys.argv[1:]))
