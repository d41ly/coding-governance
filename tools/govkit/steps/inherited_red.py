#!/usr/bin/env python3
"""inherited_red.py — the upgrade step `govkit/inherited-red-to-verdict-blocks` (TOOL-dWitnessedBar-3, S8).

    python <prefix>/govkit/steps/inherited_red.py up|down|witness <target>

Its row is in `steps.toml` beside this directory. The retired gate key `INHERITED_RED=park|land` in
the target's `.githooks/gate-env.sh` becomes the policy key `verdict.blocks` in its
`.governance/policy.toml`, so which red blocks a landing reads the same on either side of the step:
`park` is `every-red` and `land` is `own-mixed-contended`. The DOWN restores both files
byte-identical; the WITNESS exits 0 when no `INHERITED_RED` assignment is left in the gate file, or
there is no gate file, which is the step applied.

THE UP, in order. No gate file, or no `INHERITED_RED` line in it: exit 0, nothing written. Otherwise
the gate file is read in `conf_to_policy.py`'s line grammar, the last assignment winning, a trailing
` # comment` and one pair of quotes stripped; its value is parsed here, since that file's
`parse_conf` reads integers only. A value outside `park land` exits 1 WRITING NOTHING. A blank value
writes no policy key, so the catalogue default `own-only` applies. A mapped value is written into
`[verdict] blocks` through `upgrade_steps.render_policy_text`, the one writer, unless the policy file
already sets `verdict.blocks`: the same value writes nothing more, and another value is a conflict,
printed as `conflict · verdict.blocks · policy <value> · gate <value>`, exit 1 writing nothing, since
two keys deciding one landing must not be resolved by a step. Every `INHERITED_RED` line is then taken
out of the gate file, which is kept, LAST, so the witness changes last. A re-run over a killed up
recomputes from the first before-image and converges.

Exit 0 done, 1 refused naming the file or the conflict (nothing written), 2 a usage error.
"""

import importlib.util
import pathlib
import re
import sys
import tomllib

STEP_ID = "govkit/inherited-red-to-verdict-blocks"
GATE = ".githooks/gate-env.sh"
KEY = "INHERITED_RED"
POLICY = ".governance/policy.toml"
TABLE, POLICY_KEY = "verdict", "blocks"
VALUES = {"park": "every-red", "land": "own-mixed-contended"}


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
Refusal = C2P.Refusal


def parse_gate(data: bytes):
    """The `verdict.blocks` value the gate file's last `INHERITED_RED` line maps to, None where it is blank."""
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as e:
        raise Refusal(f"{GATE}: not UTF-8 ({e}), so its {KEY} cannot be read") from None
    line, found = C2P.build_line_re(KEY), None
    for n, ln in enumerate(text.removeprefix("﻿").split("\n"), 1):
        m = line.match(ln.rstrip("\r"))
        if m:
            found = (re.sub(r"\s+#.*$", "", m[1]).strip(), n)
    raw, n = found
    value = raw[1:-1] if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'" else raw
    if value == "":
        return None
    if value not in VALUES:
        raise Refusal(f"{GATE}:{n}: {KEY} must be park or land, and reads '{value}'")
    return VALUES[value]


def read_held(before: bytes | None):
    """The `verdict.blocks` the policy file's bytes already set, None where none."""
    if before is None:
        return None
    node = tomllib.loads(before.decode("utf-8")).get(TABLE)
    return node.get(POLICY_KEY) if isinstance(node, dict) else None


def cmd_up(target: pathlib.Path) -> int:
    gate = target / GATE
    if not gate.is_file() or not C2P.check_assigned(gate.read_bytes(), KEY):
        print(f"inherited-red: up · no {KEY} in {GATE} at {target.as_posix()}, so there is nothing to move")
        return 0
    pol = target / POLICY

    def derive_after(before):
        gate_bytes = gate.read_bytes() if before is None else before[GATE]
        pol_bytes = (pol.read_bytes() if pol.is_file() else None) if before is None else before.get(POLICY)
        value = parse_gate(gate_bytes)
        after = {GATE: C2P.render_conf_rest(gate_bytes, KEY)}
        if before is not None and POLICY not in before:
            return after  # the first up wrote no policy key, so a re-run writes none either
        held = read_held(pol_bytes)
        if value is not None and held is not None and held != value:
            raise Refusal(f"conflict · {TABLE}.{POLICY_KEY} · policy {held} · gate {value}: settle which "
                          f"one decides, then re-run the step")
        if value is not None and held is None:
            after[POLICY] = C2P.render_policy_bytes(pol_bytes, [(TABLE, POLICY_KEY, value)])
        return after

    after = C2P.STEPS.write_before_image(target, STEP_ID, derive_after)
    if after.get(POLICY) is not None:
        pol.parent.mkdir(parents=True, exist_ok=True)
        pol.write_bytes(after[POLICY])
    gate.write_bytes(after[GATE])  # LAST: the witness reads the line's absence
    print(f"inherited-red: up · {GATE} kept, its {KEY} taken out"
          + (f" · {TABLE}.{POLICY_KEY} set in {POLICY}" if POLICY in after else
             f" · {POLICY} unchanged"))
    return 0


def cmd_down(target: pathlib.Path) -> int:
    restored = C2P.STEPS.write_from_before_image(target, STEP_ID)
    print(f"inherited-red: down · restored {', '.join(restored) or 'nothing: no before-image, no up applied'}")
    return 0


def cmd_witness(target: pathlib.Path) -> int:
    gate = target / GATE
    held = gate.is_file() and C2P.check_assigned(gate.read_bytes(), KEY)
    print(f"inherited-red: witness · {GATE} " + (f"assigns {KEY}: not applied" if held else
                                                f"assigns no {KEY}, or is absent: applied"))
    return 1 if held else 0


def main(argv: list[str]) -> int:
    verbs = {"up": cmd_up, "down": cmd_down, "witness": cmd_witness}
    if len(argv) != 2 or argv[0] not in verbs:
        sys.stderr.write("usage: python inherited_red.py up|down|witness <target>\n")
        return 2
    try:
        return verbs[argv[0]](pathlib.Path(argv[1]).resolve())
    except Refusal as e:
        sys.stderr.write(f"inherited-red: {argv[0]} refused · {e}\n")
        return 1
    except tomllib.TOMLDecodeError as e:
        sys.stderr.write(f"inherited-red: {argv[0]} refused · {POLICY} does not parse: {e}\n")
        return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    raise SystemExit(main(sys.argv[1:]))
