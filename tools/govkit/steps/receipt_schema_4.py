#!/usr/bin/env python3
"""receipt_schema_4.py — the upgrade step `govkit/receipt-schema-4` (TOOL-dSafePassage-3, S6).

    python <prefix>/govkit/steps/receipt_schema_4.py up|down|witness <target>

Its row is the first of `steps.toml`. It moves `<target>/.governance/install.json` between schema 3
and schema 4, whose one new field is `steps`, the per-step record.

THE UP exits 0 at schema 4 or above with `steps` a list, writing nothing; exits 1 naming the schema,
writing nothing, below schema 3, because `update`'s preamble lifts such a receipt to 3 and back-fills
its `gov_oid` first; and otherwise sets `schema` to 4 in place and appends an empty `steps` as the
last key. THE DOWN exits 0 at schema 3 or below without the field; exits 1, writing nothing, while
`steps` holds an `applied` row for any other step, since taking the field out would delete that
step's record; exits 1 on a field below schema 3; and otherwise sets `schema` to 3 and takes the
field out. A schema-4 receipt without the field, or a schema-3 one with it, is normalised to schema
3 without it. THE WITNESS exits 0 at schema 4 or above with `steps` a list, else 1.

Every write is `json.dumps(receipt, indent=2) + "\\n"`, govkit's own serialization, through a sibling
temporary file renamed over the receipt — govkit's `write_atomic`, repeated because a step runs
isolated and cannot import govkit — so a kill leaves one receipt or the other, never half of one, and
the down's bytes equal the up's input for every receipt `apply`, `adopt` or `update` wrote.

Exit 0 done, 1 refused naming the receipt (nothing written), 2 a usage error.
"""

import json
import os
import pathlib
import sys

STEP_ID = "govkit/receipt-schema-4"
RECEIPT = ".governance/install.json"


def cmd_up(receipt: dict):
    """(exit code, message, the receipt to write or None)."""
    s = receipt.get("schema", 1)
    if not isinstance(s, int) or isinstance(s, bool):
        return 1, f"schema {s!r} is not a number, so it is not this step's to move", None
    if s >= 4 and isinstance(receipt.get("steps"), list):
        return 0, f"schema {s} with `steps`: already applied, nothing written", None
    if s < 3:
        return 1, (f"schema {s} is below 3; `govkit.py update` lifts it to 3 and back-fills its "
                   f"`gov_oid` first, and this step starts from there"), None
    receipt.pop("steps", None)
    receipt["schema"] = 4
    receipt["steps"] = []
    return 0, f"schema {s} -> 4, `steps` empty", receipt


def cmd_down(receipt: dict):
    """(exit code, message, the receipt to write or None)."""
    s = receipt.get("schema", 1)
    if not isinstance(s, int) or isinstance(s, bool):
        return 1, f"schema {s!r} is not a number, so it is not this step's to move", None
    if s <= 3 and "steps" not in receipt:
        return 0, f"schema {s} without `steps`: nothing to take out", None
    if s < 3:
        return 1, f"schema {s} carries `steps`, a field no writer gives a receipt below 3", None
    steps = receipt.get("steps")
    held = sorted({r.get("id") for r in steps if isinstance(r, dict) and r.get("state") == "applied"
                   and r.get("id") != STEP_ID} if isinstance(steps, list) else set(), key=str)
    if held:
        return 1, (f"`steps` holds applied row(s) for {', '.join(map(str, held))}; run their downs "
                   f"first, since taking the field out would delete their record"), None
    receipt.pop("steps", None)
    receipt["schema"] = 3
    return 0, f"schema {s} -> 3, `steps` taken out", receipt


def cmd_witness(receipt: dict):
    """(exit code, message, None): applied at schema 4 or above with `steps` a list."""
    s = receipt.get("schema", 1)
    ok = isinstance(s, int) and not isinstance(s, bool) and s >= 4 and isinstance(receipt.get("steps"), list)
    return (0 if ok else 1), f"schema {s!r}: " + ("applied" if ok else "not applied"), None


def main(argv: list[str]) -> int:
    verbs = {"up": cmd_up, "down": cmd_down, "witness": cmd_witness}
    if len(argv) != 2 or argv[0] not in verbs:
        sys.stderr.write("usage: python receipt_schema_4.py up|down|witness <target>\n")
        return 2
    path = pathlib.Path(argv[1]).resolve() / RECEIPT
    try:
        receipt = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        sys.stderr.write(f"receipt-schema-4: {argv[0]} refused · {path.as_posix()} is unreadable: {e}\n")
        return 1
    if not isinstance(receipt, dict):
        sys.stderr.write(f"receipt-schema-4: {argv[0]} refused · {path.as_posix()} is not an object\n")
        return 1
    code, msg, out = verbs[argv[0]](receipt)
    if out is not None:
        tmp = path.with_name(path.name + ".govkit-new")
        tmp.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8", newline="\n")
        os.replace(tmp, path)
    (sys.stdout if code == 0 else sys.stderr).write(
        f"receipt-schema-4: {argv[0]} " + ("" if code == 0 else "refused ") + f"· {path.as_posix()} · {msg}\n")
    return code


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    raise SystemExit(main(sys.argv[1:]))
