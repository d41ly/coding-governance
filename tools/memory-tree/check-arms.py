#!/usr/bin/env python3
"""check-arms.py — the harness meta-gate: every `fail` BRANCH is armed, or explicitly pinned.

    python tools/memory-tree/check-arms.py --check      # the gate
    python tools/memory-tree/check-arms.py --report     # what is armed, what is pinned
    python tools/memory-tree/check-arms.py --selftest

WHY A BRANCH AND NOT A CHECK NUMBER. This kit's gate has 14 `fail` call sites behind 12 numbers:
checks 5 and 6 each fail for two different reasons. A pin keyed on the NUMBER lets the cheapest arm
empty a number while its second, more valuable branch stays unwritten AND invisible. Upstream counted
41 branches behind 25 numbers and hit exactly that. So the key is the CALL SITE — `(number, ordinal)`
— never the label prose, which gets reworded, and never the number, which is not unique.

WHAT COUNTS AS AN ARM. A POSITIVE assertion naming the branch's OWN failure text. A bare `check N`
mention satisfies a substring test, and so does an ABSENCE assertion (`miss 'check 7'`) — both would
let a branch count as armed while nothing exercises it. So the signature is a literal slice of the
branch's own message, and a line that is a negative assertion does not arm anything.

PINNED IN BOTH DIRECTIONS. A derived count catches a DELETED guard. It does not catch an assertion
dropped by WIDENING the exemption list — the branch count falls, the pin still holds, and the gate is
quieter than it was. So there are two floors: `ARMS_BRANCH_FLOOR` (how many `fail` branches exist)
and `ARMS_ARMED_FLOOR` (how many are armed). Both are measured, both are one-sided upward.

THE PIN IS EXCLUDED FROM ITS OWN SCAN. The pin file holds each pinned signature verbatim in order to
name it, so a scan that included the pin would find every signature there and report every branch as
armed. Upstream shipped this meta-check vacuous for exactly that reason.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PIN = "project/unarmed-branches.txt"

# `fail <n> "<message …>` — the message opens on the same line and may run on. The signature is the
# first line of it, with every shell interpolation dropped: `$SPEC_FORMAT_CUTOFF` is a value, not
# text a test can assert on.
# ANYWHERE on the line, not just at its start. Check 9's call sits inside an `if ! drift=$(…); then`
# and a start-anchored pattern missed it entirely — a branch invisible to this meta-check is exactly
# what the meta-check exists to prevent, and it would have been invisible SILENTLY.
FAIL_RE = re.compile(r'\bfail (\d+) "(.*)$')
INTERP_RE = re.compile(r'\$\{?[A-Za-z_][A-Za-z0-9_]*\}?')
# A NEGATIVE assertion. `miss` is this kit's absence helper; the `&&` form is the inline one.
NEGATIVE_RE = re.compile(r"^\s*(miss\b|.*grep -qF .* <<<.*\s&&\s)")


class Problem(Exception):
    """A named, user-facing failure. Never a traceback."""


def run(*argv, cwd=None):
    return subprocess.run(argv, cwd=cwd, capture_output=True, text=True, check=True).stdout


def read(p):
    with open(p, "rb") as fh:
        return fh.read().decode("utf-8", "replace").replace("\r\n", "\n")


def load_conf(root):
    conf = {"MEMORY_ROOT": "memory", "ARMS_BRANCH_FLOOR": "", "ARMS_ARMED_FLOOR": ""}
    p = os.path.join(root, ".memory-tree.conf")
    if os.path.isfile(p):
        for line in read(p).split("\n"):
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            conf[k.strip()] = v.strip().strip('"').strip("'")
    return conf


def signature(message: str) -> str:
    """A literal slice of the branch's own message that a test can assert on.

    Interpolations are dropped rather than guessed at, and the longest surviving literal run is the
    signature — short runs like ':' or ' — ' appear in every message and would arm every branch.
    """
    parts = [p.strip() for p in INTERP_RE.split(message)]
    parts = [p.rstrip(':" ').strip() for p in parts]
    best = max(parts, key=len) if parts else ""
    return best


def branches(gate_path: str) -> list:
    """Every `fail` call site, keyed on (number, ordinal-within-that-number)."""
    seen = {}
    out = []
    for lineno, line in enumerate(read(gate_path).split("\n"), 1):
        if line.lstrip().startswith("#") or "fail() {" in line:
            continue                      # a comment about a branch, and the helper's definition
        m = FAIL_RE.search(line)
        if not m:
            continue
        num = int(m.group(1))
        seen[num] = seen.get(num, 0) + 1
        sig = signature(m.group(2))
        if len(sig) < 12:
            raise Problem(f"{gate_path}:{lineno}: check {num} branch {seen[num]} has no literal run "
                          f"long enough to assert on ({sig!r}) — reword the message or the arm cannot "
                          f"name it")
        out.append({"num": num, "ord": seen[num], "line": lineno, "sig": sig})
    return out


def armed_signatures(test_path: str) -> set:
    """Lines of the test file that could carry a POSITIVE assertion.

    A COMMENT is not an arm. The test file's prose explains what each arm covers and naturally
    quotes the messages, so a comment-blind scan would let a branch read as armed on the strength of
    a sentence describing it — the same shape as the bare-`check N` mention and the absence
    assertion this function already refuses. All three are "something in the file mentions it",
    which is not "something exercises it".
    """
    out = set()
    for line in read(test_path).split("\n"):
        if line.lstrip().startswith("#"):
            continue
        if NEGATIVE_RE.match(line):
            continue
        out.add(line)
    return out


def parse_pin(root: str, m: str) -> list:
    p = os.path.join(root, m, PIN)
    rows = []
    if not os.path.isfile(p):
        return rows
    for i, line in enumerate(read(p).split("\n"), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) != 3:
            raise Problem(f"{m}/{PIN}:{i}: expected 3 tab-separated fields "
                          f"(check<TAB>ordinal<TAB>signature), got {len(parts)}")
        rows.append((parts[0].strip(), parts[1].strip(), parts[2].strip(), i))
    return rows


def classify(root: str, conf: dict, gate: str, test: str) -> dict:
    m = conf["MEMORY_ROOT"]
    brs = branches(gate)
    lines = armed_signatures(test)
    for b in brs:
        b["armed"] = any(b["sig"] in l for l in lines)
    pinned = parse_pin(root, m)
    return {"branches": brs, "pinned": pinned, "m": m}


def do_check(root: str, conf: dict, gate: str, test: str) -> int:
    st = classify(root, conf, gate, test)
    brs, pinned, m = st["branches"], st["pinned"], st["m"]
    bad = []
    pin_keys = {(r[0], r[1]): r for r in pinned}
    for b in brs:
        key = (str(b["num"]), str(b["ord"]))
        if b["armed"]:
            if key in pin_keys:
                bad.append(f"check-arms: {m}/{PIN}:{pin_keys[key][3]} pins check {b['num']} branch "
                           f"{b['ord']}, which IS armed now — delete the row (the pin is shrink-only)")
            continue
        if key not in pin_keys:
            bad.append(f"check-arms: {os.path.basename(gate)}:{b['line']} check {b['num']} branch "
                       f"{b['ord']} has no POSITIVE assertion naming its own failure text "
                       f"({b['sig']!r}) and is not pinned in {m}/{PIN}")
        elif pin_keys[key][2] != b["sig"]:
            bad.append(f"check-arms: {m}/{PIN}:{pin_keys[key][3]} pins check {b['num']} branch "
                       f"{b['ord']} with a stale signature — the message was reworded")
    live = {(str(b["num"]), str(b["ord"])) for b in brs}
    for r in pinned:
        if (r[0], r[1]) not in live:
            bad.append(f"check-arms: {m}/{PIN}:{r[3]} pins check {r[0]} branch {r[1]}, which no longer "
                       f"exists — the guard was deleted or renumbered")
    # BOTH FLOORS. A deleted guard shrinks the branch count; an assertion dropped by widening the
    # exemption list shrinks the armed count while the branch count and the pin both hold.
    n_br, n_armed = len(brs), sum(1 for b in brs if b["armed"])
    for key, got, label in (("ARMS_BRANCH_FLOOR", n_br, "fail branch(es)"),
                            ("ARMS_ARMED_FLOOR", n_armed, "armed branch(es)")):
        floor = conf.get(key, "")
        if floor and got < int(floor):
            bad.append(f"check-arms: {got} {label} against a floor of {floor} ({key}) — a guard or an "
                       f"assertion was removed; lower the floor in a commit that says why")
    for line in bad:
        print("HYGIENE " + line)
    return 1 if bad else 0


def do_report(root: str, conf: dict, gate: str, test: str) -> int:
    st = classify(root, conf, gate, test)
    brs = st["branches"]
    print(f"fail branches : {len(brs)}   (ARMS_BRANCH_FLOOR={conf.get('ARMS_BRANCH_FLOOR') or 'unset'})")
    print(f"armed         : {sum(1 for b in brs if b['armed'])}   (ARMS_ARMED_FLOOR={conf.get('ARMS_ARMED_FLOOR') or 'unset'})")
    print(f"pinned rows   : {len(st['pinned'])}")
    for b in brs:
        print(f"    check {b['num']:>2} branch {b['ord']}  line {b['line']:>4}  "
              f"{'ARMED ' if b['armed'] else '      '} {b['sig'][:78]}")
    return 0


def do_emit_pin(root: str, conf: dict, gate: str, test: str) -> int:
    """Print the pin file for the CURRENT unarmed set — the measurement, not a guess."""
    st = classify(root, conf, gate, test)
    print("# unarmed-branches.txt — `fail` branches with no positive assertion naming their own")
    print("# failure text. SHRINK-ONLY: a row leaves when its branch gains an arm, and check-arms")
    print("# reds if a pinned branch is armed, if a pinned branch disappears, or if a message is")
    print("# reworded out from under its signature. Fields: check<TAB>ordinal<TAB>signature.")
    for b in st["branches"]:
        if not b["armed"]:
            print(f"{b['num']}\t{b['ord']}\t{b['sig']}")
    return 0


# ----------------------------------------------------------------------------------------- selftest
def do_selftest() -> int:
    fails = []

    def arm(label, want, fn):
        import contextlib
        import io

        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                rc = fn()
            got = buf.getvalue() + f"[rc={rc}]"
        except Problem as exc:
            got = str(exc)
        except Exception as exc:  # noqa: BLE001
            got = f"UNEXPECTED {type(exc).__name__}: {exc}"
        ok = (want in got) if want else ("[rc=0]" in got)
        print(("arm ok    " if ok else "arm FAIL  ") + label + ("" if ok else f" — expected {want!r}, got: {got.strip()}"))
        if not ok:
            fails.append(label)

    GATE = (
        'fail() { echo "HYGIENE check $1 FAILED — $2"; status=1; }\n'
        '[ -n "$a" ] && fail 1 "alpha branch message here:\n"\n'
        '[ -n "$b" ] && fail 1 "beta branch message here:\n"\n'
        '[ -n "$c" ] && fail 2 "gamma branch message here:\n"\n'
    )
    with tempfile.TemporaryDirectory() as base:
        os.makedirs(os.path.join(base, "memory", "project"))
        g = os.path.join(base, "gate.sh")
        t = os.path.join(base, "gate.test.sh")
        with open(g, "wb") as fh:
            fh.write(GATE.encode())
        conf = {"MEMORY_ROOT": "memory", "ARMS_BRANCH_FLOOR": "3", "ARMS_ARMED_FLOOR": "1"}

        # TWO branches behind ONE number — the whole reason the key is (number, ordinal).
        arm("branches are keyed on the call site, not the check number", "[rc=0]",
            lambda: 0 if [(b["num"], b["ord"]) for b in branches(g)] == [(1, 1), (1, 2), (2, 1)] else 1)

        # an unarmed, unpinned branch reds
        with open(t, "wb") as fh:
            fh.write(b"hit 'alpha branch message here'\n")
        arm("an unarmed branch with no pin reds", "branch 2 has no POSITIVE assertion",
            lambda: do_check(base, conf, g, t))

        # a bare `check N` mention does NOT arm
        with open(t, "wb") as fh:
            fh.write(b"hit 'alpha branch message here'\nhit 'HYGIENE check 1 FAILED'\nhit 'check 2'\n")
        arm("a bare check-number mention does not arm a branch", "check 2 branch 1 has no POSITIVE",
            lambda: do_check(base, conf, g, t))

        # a COMMENT naming the message does NOT arm — the test file's own prose quotes these.
        with open(t, "wb") as fh:
            fh.write(b"hit 'alpha branch message here'\n"
                     b"# this arm would cover: gamma branch message here\n")
        arm("a comment naming the message does not arm a branch", "check 2 branch 1 has no POSITIVE",
            lambda: do_check(base, conf, g, t))

        # an ABSENCE assertion does not arm
        with open(t, "wb") as fh:
            fh.write(b"hit 'alpha branch message here'\nmiss 'beta branch message here'\n"
                     b"hit 'gamma branch message here'\n")
        arm("an absence assertion does not arm a branch", "check 1 branch 2 has no POSITIVE",
            lambda: do_check(base, conf, g, t))

        # pinned -> passes; and the pin is EXCLUDED from its own scan
        pin = os.path.join(base, "memory", "project", "unarmed-branches.txt")
        with open(pin, "wb") as fh:
            fh.write(b"1\t2\tbeta branch message here\n")
        arm("a pinned unarmed branch passes", None, lambda: do_check(base, conf, g, t))
        # THE PIN IS EXCLUDED FROM ITS OWN SCAN. The pin now holds `beta branch message here`
        # verbatim, because that is how it names the branch it exempts. If the arm scan reached the
        # pin, that branch would read as ARMED — every pinned branch would, and the meta-check would
        # ship vacuous, which is exactly what upstream did. The scan reads the TEST file and nothing
        # else, so a signature present only in the pin arms nothing.
        arm("a signature present only in the PIN arms nothing", "[rc=0]",
            lambda: 0 if not [b for b in classify(base, conf, g, t)["branches"]
                              if (b["num"], b["ord"]) == (1, 2) and b["armed"]] else 1)

        # a pinned branch that becomes armed reds (shrink-only)
        with open(t, "wb") as fh:
            fh.write(b"hit 'alpha branch message here'\nhit 'beta branch message here'\n"
                     b"hit 'gamma branch message here'\n")
        arm("a pin that is now armed reds", "which IS armed now", lambda: do_check(base, conf, g, t))

        # a pinned branch that no longer exists reds
        with open(pin, "wb") as fh:
            fh.write(b"9\t1\tvanished branch message\n")
        arm("a pin for a deleted branch reds", "which no longer exists",
            lambda: do_check(base, conf, g, t))

        # BOTH floors
        os.remove(pin)
        conf2 = dict(conf, ARMS_BRANCH_FLOOR="4")
        arm("the branch floor catches a deleted guard", "3 fail branch(es) against a floor of 4",
            lambda: do_check(base, conf2, g, t))
        with open(t, "wb") as fh:
            fh.write(b"hit 'alpha branch message here'\n")
        with open(pin, "wb") as fh:
            fh.write(b"1\t2\tbeta branch message here\n2\t1\tgamma branch message here\n")
        conf3 = dict(conf, ARMS_ARMED_FLOOR="3")
        arm("the armed floor catches an assertion dropped by widening the pin",
            "1 armed branch(es) against a floor of 3", lambda: do_check(base, conf3, g, t))

        # a message with no assertable literal run is a named error, not a silent skip
        with open(g, "wb") as fh:
            fh.write(b'[ -n "$a" ] && fail 1 "$X:\n"\n')
        arm("a message with no literal run is named", "no literal run long enough",
            lambda: do_check(base, conf, g, t))

    if fails:
        print(f"FAIL — {len(fails)} arm(s) failed")
        return 1
    print("PASS — check-arms: all arms held")
    return 0


def main(argv):
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode == "--selftest":
        return do_selftest()
    try:
        root = run("git", "rev-parse", "--show-toplevel").strip()
    except Exception:  # noqa: BLE001
        print("check-arms: not a git repo")
        return 2
    conf = load_conf(root)
    gate = os.path.join(HERE, "check-memory-hygiene.sh")
    test = os.path.join(HERE, "check-memory-hygiene.test.sh")
    try:
        if mode == "--check":
            return do_check(root, conf, gate, test)
        if mode == "--report":
            return do_report(root, conf, gate, test)
        if mode == "--emit-pin":
            return do_emit_pin(root, conf, gate, test)
        print("usage: check-arms.py [--check|--report|--emit-pin|--selftest]")
        return 2
    except Problem as exc:
        print(f"HYGIENE {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
