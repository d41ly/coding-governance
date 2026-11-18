"""conf_to_policy.py — the shared part of an upgrade step that moves one conf key into policy keys
(TOOL-dDeclaredLoop-21, S8).

Extracted at the kind's second instance from `fanout_cap.py`'s four helpers, generalised by conf file
and key; `fanout_cap.py` itself stays byte-identical, because it is the program of a landed step row
and the frozen-row check reds a byte it moves. A step program loads this file by its path, as it
loads `upgrade_steps.py`: the runner's `-I` drops the program's own directory from `sys.path`.

THE GRAMMAR, the one a conf the driver sources is read in. `<KEY>=<n>`, `<KEY>="<n>"` or `<KEY>='<n>'`,
a trailing ` # comment`, a BOM and a trailing CR tolerated, the last such line winning, and every other
line legal and ignored. A blank value reads as no value. A value that is not an integer of at least 1
is a refusal at its line.

The policy text is written through `upgrade_steps.render_policy_text`, the one writer, one key at a
time. Nothing here writes a file: the step program writes what these return.
"""

import importlib.util
import pathlib
import re
import subprocess
import sys


def load_steps():
    """The step reader beside this file's directory, imported by its path: the runner's `-I` drops
    a program's own directory from `sys.path`, and the before-image helpers live there."""
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


def build_line_re(key: str):
    """The pattern of one assignment line of `key`."""
    return re.compile(rf"^\s*{re.escape(key)}\s*=(.*)$")


def check_assigned(data: bytes, key: str) -> bool:
    """True where a line of the conf's bytes assigns `key`: the step's witness reads its absence."""
    line = build_line_re(key)
    return any(line.match(ln.removeprefix("﻿").rstrip("\r"))
               for ln in data.decode("utf-8", "replace").split("\n"))


def parse_conf(data: bytes, conf: str, key: str) -> int | None:
    """The value of `key` the conf's bytes carry, None where no line sets it or the last one is
    blank; a value that is not an integer of at least 1 is a refusal at its line."""
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as e:
        raise Refusal(f"{conf}: not UTF-8 ({e}), so its {key} cannot be read") from None
    line, found = build_line_re(key), None
    for n, ln in enumerate(text.removeprefix("﻿").split("\n"), 1):
        m = line.match(ln.rstrip("\r"))
        if m:
            found = (re.sub(r"\s+#.*$", "", m[1]).strip(), n)
    if found is None:
        return None
    raw, n = found
    value = raw[1:-1] if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'" else raw
    if value == "":
        return None
    if not re.fullmatch(r"[0-9]+", value) or int(value) < 1:
        raise Refusal(f"{conf}:{n}: {key} must be an integer of at least 1")
    return int(value)


def render_conf_rest(data: bytes, key: str) -> bytes:
    """The conf's bytes with every `key` line taken out, each other line byte for byte. The file
    is kept even where nothing else remains: a conf a driver requires is never removed."""
    line = build_line_re(key)
    lines = data.decode("utf-8").splitlines(keepends=True)
    return "".join(ln for ln in lines if not line.match(ln.removeprefix("﻿").rstrip("\r\n"))).encode("utf-8")


def check_committed(target: pathlib.Path, rel: str) -> bool:
    """True where the working-tree `rel` is its blob at HEAD, read through the target's own filters,
    or is absent in both."""
    head = subprocess.run(["git", "-C", str(target), "rev-parse", "--verify", "--quiet", f"HEAD:{rel}"],
                          capture_output=True, encoding="utf-8")
    if not (target / rel).is_file():
        return head.returncode != 0
    now = subprocess.run(["git", "-C", str(target), "hash-object", f"--path={rel}", "--", rel],
                         capture_output=True, encoding="utf-8")
    return head.returncode == 0 and now.returncode == 0 and head.stdout.strip() == now.stdout.strip()


def render_policy_bytes(before: bytes | None, settings) -> bytes:
    """The policy file's bytes with each `(table, key, value)` of `settings` set, in order, through
    the one writer."""
    text = None if before is None else before.decode("utf-8")
    for table, key, value in settings:
        text = STEPS.render_policy_text(text, table, key, value)
    return text.encode("utf-8")
