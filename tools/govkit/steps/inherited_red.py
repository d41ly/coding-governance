#!/usr/bin/env python3
"""inherited_red.py — the upgrade step `govkit/inherited-red-to-verdict-blocks` (TOOL-dWitnessedBar-3, S8;
widened by TOOL-dWitnessedBar-44).

    python <prefix>/govkit/steps/inherited_red.py up|down|witness <target>

Its row is in `steps.toml` beside this directory. The retired gate key `INHERITED_RED` becomes the
policy key `verdict.blocks` in the target's `.governance/policy.toml`, so which red blocks a landing
reads the same on either side of the step. The kit before it read the key in TWO files: the pre-push
hook read `.githooks/gate-env.sh`, and the driver read the file `GATE_POLICY_FILE` names in
`.unattended.conf`, that same gate file where the key is blank or absent or there is no conf. The
step reads both, each only where present, and the second only where it is another file.

THE MAPPING is the pre-step readers' own `case` arms: `land` is `own-mixed-contended`, and `park`
and every other non-blank value, `Park` and `LAND` included, is `every-red`, as both readers read
it. A `GATE_POLICY_FILE` that is not a repo-relative path inside the tree, by the driver's own case
patterns, read `park`: it maps to `every-red`, and the step neither reads nor edits the file it
names. Where the two files map to different values the stricter, `every-red`, is written. A blank
value maps to nothing, so where every file read is blank the catalogue default `own-only` applies.

THE READER is the pre-step readers' own `read_policy_key` (TOOL-dWitnessedBar-55), and not
`conf_to_policy.py`'s sourced-conf grammar. Each line, split on LF with one trailing CR cut, is an
assignment only where it begins exactly `INHERITED_RED=`: an `export` line, an indented, commented or
`INHERITED_RED =` spaced one, and a first line opening with a BOM are not. The LAST assignment wins;
its value is cut at the first whitespace character followed by `#`, stripped of trailing spaces and
tabs and of leading spaces, a leading tab kept, and stripped of one surrounding pair of double or of
single quotes. A last assignment that cleans to empty is undeclared, whatever an earlier line set.
`GATE_POLICY_FILE` is read from `.unattended.conf` by the same rule, as the driver reads it.

THE UP, in order. No file read assigns `INHERITED_RED`: exit 0, nothing written, and the `undeclared`
line names the loosening: MIXED and CONTENDED reds the kit default `land` blocked now pass. Otherwise each file
is read by that rule; a file that is not UTF-8 exits 1 naming it, writing nothing. The
value is written into `[verdict] blocks` through `upgrade_steps.render_policy_text`, the one writer,
unless the policy file already sets `verdict.blocks`: the same value writes nothing more, and another
value is a conflict, printed as `conflict · verdict.blocks · policy <value> · gate <value>`, exit 1
writing nothing, since two keys deciding one landing must not be resolved by a step. Every
`INHERITED_RED` assignment by that rule is then taken out of each file that held one, every other
line kept byte for byte and the file kept, LAST, so the witness changes last. A re-run over a killed
up recomputes from the first before-image and converges. The DOWN restores every file
byte-identical. The WITNESS prints one line per file read, naming it, the value found and the value
written, and one `not an assignment <file>:<line>` line per line that spells the key and is no
assignment by that rule, which does not fail it; it exits 0 when no `INHERITED_RED` assignment is
left in either file, or neither is present, which is the step applied.

Exit 0 done, 1 refused naming the file or the conflict (nothing written), 2 a usage error.
"""

import base64
import importlib.util
import json
import pathlib
import re
import sys
import tomllib

STEP_ID = "govkit/inherited-red-to-verdict-blocks"
GATE = ".githooks/gate-env.sh"
KEY = "INHERITED_RED"
CONF, CONF_KEY = ".unattended.conf", "GATE_POLICY_FILE"
POLICY = ".governance/policy.toml"
TABLE, POLICY_KEY = "verdict", "blocks"
# The loosening v2's default makes, said where it happens (TOOL-dWitnessedBar-51 S16, §8 F2): an
# undeclared key read the kit default `land` before the step, and the catalogue default after it is
# `own-only`.
UNDECLARED = ("inherited-red: undeclared — the kit default land read MIXED and CONTENDED reds as blocking; "
              "own-only now passes them")
VALUES = {"park": "every-red", "land": "own-mixed-contended"}
OTHER = "every-red"  # the readers' `*` arm read any value outside `park land` as park
STRICTNESS = ("every-red", "own-mixed-contended")  # the stricter first


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


def check_policy_assignment(line: str, key: str) -> bool:
    """True where `line`, one trailing CR cut, begins exactly `<key>=`: the pre-step readers'
    `read_policy_key` case arm, so an `export`, indented, commented, spaced or BOM-led line is not."""
    return line.removesuffix("\r").startswith(f"{key}=")


def read_value(data: bytes, rel: str, key: str) -> str | None:
    """The value the last `key` assignment of `rel`'s bytes carries, cleaned as `read_policy_key`
    cleans it: cut at the first whitespace before a `#`, trailing spaces and tabs and leading spaces
    stripped, one pair of quotes removed. None where no line assigns it. Bytes that are not UTF-8
    refuse, naming `rel`."""
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as e:
        raise Refusal(f"{rel}: not UTF-8 ({e}), so its {key} cannot be read") from None
    found = None
    for ln in text.split("\n"):
        if check_policy_assignment(ln, key):
            found = ln.removesuffix("\r")[len(key) + 1:]
    if found is None:
        return None
    cut = re.search(r"[ \t\n\v\f\r]#", found)
    found = (found[:cut.start()] if cut else found).rstrip(" \t").lstrip(" ")
    return found[1:-1] if len(found) >= 2 and found[0] == found[-1] and found[0] in "\"'" else found


def render_gate_rest(data: bytes, key: str) -> bytes:
    """`data` with every `key` assignment by `check_policy_assignment` taken out, split on LF where
    `read_value` splits, each other line byte for byte. The file is kept where nothing remains."""
    parts = data.decode("utf-8").split("\n")
    lines = [p + "\n" for p in parts[:-1]] + ([parts[-1]] if parts[-1] else [])
    return "".join(ln for ln in lines if not check_policy_assignment(ln.removesuffix("\n"), key)).encode("utf-8")


def parse_gate(data: bytes, rel: str):
    """The `verdict.blocks` value the last `INHERITED_RED` line of `rel` maps to, None where it is
    blank or absent: `land` the milder, every other value the readers' `park`."""
    value = read_value(data, rel, KEY)
    return VALUES.get(value, OTHER) if value else None


def derive_stricter(values) -> str | None:
    """The value of `values` that blocks more, None where none is set."""
    return next((v for v in STRICTNESS if v in values), None)


def check_off_tree(path: str) -> bool:
    """True where `path` is not a repo-relative path inside the tree by the driver's own `case`
    patterns (`/*|[A-Za-z]:*|..|../*|*/..|*/../*`), which read `park` without reading the file."""
    return (path.startswith("/") or re.match(r"[A-Za-z]:", path) is not None or path == ".."
            or path.startswith("../") or path.endswith("/..") or "/../" in path)


def derive_reads(target: pathlib.Path) -> tuple[list[str], str | None]:
    """(the repo-relative files the step reads, the `GATE_POLICY_FILE` read as `park` unread or None).
    The gate file always; the file the conf's `GATE_POLICY_FILE` names beside it where that is
    another contained path. A blank or absent key, or no conf, names the gate file."""
    conf = target / CONF
    named = read_value(conf.read_bytes(), CONF, CONF_KEY) if conf.is_file() else None
    if not named:
        return [GATE], None
    if check_off_tree(named):
        return [GATE], named
    C2P.STEPS.check_contained(target, named)  # a link or a git-directory path refuses, read nothing
    rel = C2P.STEPS.derive_contained_rel(named)
    if rel == POLICY:
        raise Refusal(f"{CONF}: {CONF_KEY} names {POLICY}, the file this step writes, so it cannot "
                      f"also be read as a gate file")
    return ([GATE] if rel == GATE else [GATE, rel]), None


def read_file(target: pathlib.Path, rel: str) -> bytes | None:
    """`rel`'s bytes, None where it is absent or unreadable, as the driver read an absent file."""
    p = target / rel
    try:
        return p.read_bytes() if p.is_file() else None
    except OSError:
        return None


def read_image_before(target: pathlib.Path) -> dict:
    """The before bytes this step's before-image records per path, {} where there is none or it
    does not parse: the witness's value found once the up has taken the lines out."""
    try:
        image = C2P.STEPS.derive_image_path(target, STEP_ID)
        paths = json.loads(image.read_text(encoding="utf-8"))["paths"] if image.is_file() else {}
        return {p: None if v["before"] is None else base64.b64decode(v["before"]) for p, v in paths.items()}
    except (Refusal, OSError, ValueError, KeyError, TypeError, AttributeError):
        return {}


def read_held(before: bytes | None):
    """The `verdict.blocks` the policy file's bytes already set, None where none."""
    if before is None:
        return None
    node = tomllib.loads(before.decode("utf-8")).get(TABLE)
    return node.get(POLICY_KEY) if isinstance(node, dict) else None


def cmd_up(target: pathlib.Path) -> int:
    reads, off = derive_reads(target)
    held = [rel for rel in reads if (b := read_file(target, rel)) is not None
            and any(check_policy_assignment(ln, KEY) for ln in b.decode("utf-8", "replace").split("\n"))]
    if not held:
        print(f"inherited-red: up · no {KEY} in {' or '.join(reads)} at {target.as_posix()}, "
              f"so there is nothing to move")
        print(UNDECLARED)
        return 0
    pol = target / POLICY

    def derive_after(before):
        rels = held if before is None else [rel for rel in reads if rel in before]
        after, values = {}, [OTHER] if off else []
        for rel in rels:
            data = read_file(target, rel) if before is None else before[rel]
            values.append(parse_gate(data, rel))
            after[rel] = render_gate_rest(data, KEY)
        if before is not None and POLICY not in before:
            return after  # the first up wrote no policy key, so a re-run writes none either
        pol_bytes = (pol.read_bytes() if pol.is_file() else None) if before is None else before[POLICY]
        value, have = derive_stricter(values), read_held(pol_bytes)
        if value is not None and have is not None and have != value:
            raise Refusal(f"conflict · {TABLE}.{POLICY_KEY} · policy {have} · gate {value}: settle which "
                          f"one decides, then re-run the step")
        if value is not None and have is None:
            after[POLICY] = C2P.render_policy_bytes(pol_bytes, [(TABLE, POLICY_KEY, value)])
        return after

    after = C2P.STEPS.write_before_image(target, STEP_ID, derive_after)
    if after.get(POLICY) is not None:
        pol.parent.mkdir(parents=True, exist_ok=True)
        pol.write_bytes(after[POLICY])
    gates = [rel for rel in after if rel != POLICY]
    for rel in gates:
        (target / rel).write_bytes(after[rel])  # LAST: the witness reads the line's absence
    print(f"inherited-red: up · {', '.join(gates)} kept, its {KEY} taken out"
          + (f" · {CONF_KEY} {off} is outside the tree, read as park" if off else "")
          + (f" · {TABLE}.{POLICY_KEY} set in {POLICY}" if POLICY in after else f" · {POLICY} unchanged"))
    return 0


def cmd_down(target: pathlib.Path) -> int:
    restored = C2P.STEPS.write_from_before_image(target, STEP_ID)
    print(f"inherited-red: down · restored {', '.join(restored) or 'nothing: no before-image, no up applied'}")
    return 0


def cmd_witness(target: pathlib.Path) -> int:
    reads, off = derive_reads(target)
    image = read_image_before(target)
    rows, values, pending = [], [], False
    for rel in reads:
        data = read_file(target, rel)
        lines = [] if data is None else data.decode("utf-8", "replace").split("\n")
        now = any(check_policy_assignment(ln, KEY) for ln in lines)
        was = image.get(rel)
        stray = [f"not an assignment {rel}:{n}" for n, ln in enumerate(lines, 1)
                 if re.search(rf"(?<!\w){KEY}\s*=", ln) and not check_policy_assignment(ln, KEY)]
        if not now and not (was is not None and any(
                check_policy_assignment(ln, KEY) for ln in was.decode("utf-8", "replace").split("\n"))):
            rows.append(f"{rel} " + ("is absent or unreadable" if data is None else f"assigns no {KEY}")
                        + ": applied")
            rows.extend(stray)
            continue
        pending |= now
        try:
            raw = read_value(data if now else was, rel, KEY)
            mapped = parse_gate(data if now else was, rel)
            values.append(mapped)
            rows.append((rel, raw, mapped, now))
        except Refusal as e:
            rows.append(f"{e}: {'not applied' if now else 'applied'}")
        rows.extend(stray)
    if off and values:
        values.append(OTHER)
    written = derive_stricter(values) or f"nothing, {POLICY} unchanged"
    for row in rows:
        if isinstance(row, str):
            print(f"inherited-red: witness · {row}")
            continue
        rel, raw, mapped, now = row
        print(f"inherited-red: witness · {rel} " + ("assigns" if now else "assigned before the up")
              + f" {KEY}={raw!s} · read as {mapped or 'nothing'} · "
              + (f"the up writes {written}: not applied" if now else f"written {written}: applied"))
    if off:
        print(f"inherited-red: witness · {CONF_KEY} {off} is not a repo-relative path inside the tree, "
              f"read as park ({OTHER}), the file neither read nor edited")
    return 1 if pending else 0


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
