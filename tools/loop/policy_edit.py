#!/usr/bin/env python3
"""policy_edit.py — the policy file's one write path for an agent and its TTY command for the owner (TOOL-dDeclaredLoop-2).

    python policy_edit.py set <key> <value> --build <slug> --unit <id>
    python policy_edit.py raise <cap> <new> --build <slug> --unit <id> --argument <text>
    python policy_edit.py propose <key> <value>

Run from inside the repository; it works at its top level. A value is read as TOML reads it, so `4` is
an integer and `off` a string.

`set` checks the value against its catalogue row with the policy kit's `check_value`, a `floor` member
against the map row and the four members, and `policy-file.proof` through the guard's
`check_expansion_value` first. It writes when the proof holds: standard error an interactive terminal,
then the typed confirmation `yes` on standard input; or the branch a live run's branch, as the minimal
guard's `check_run_mandate` reads it at HEAD, while `policy-file.guard`, as landed, is
`agents-with-reason` or `agents-within-mandate`, which asks no confirmation (TOOL-dBoundRoles-95).
Otherwise, a live run's branch under `owner-only` included, it prints the proposal and exits 1, writing
nothing. The terminal proof stops forgetting, not evasion: a pty wrapper
giving an agent a terminal passes it, the threat the owner accepted (SA-1).

`raise` is the agent's door for one measured-file cap and needs no proof, only the four conditions the
paragraph "WHEN A RUN MAY RAISE A ROW" of the template-size limits file states, checked in order and
each refusal named: the cap is a leaf under `budgets`, neither `enforce` nor `pinned`, set in the policy
file at HEAD, its name a file tracked at HEAD, and `<new>` an integer above its value there; condition 1,
the working tree's file, measured CR-stripped in bytes, exceeds the old value; condition 2, the comment
block directly above the cap carries no `reserved: owner` line; condition 3, it writes
`# RAISED <old> -> <new>, <date>, <unit>, measured <n> bytes, <argument>` directly above the cap;
condition 4, the change record names the cap's row tag, and it prints the decision row the caller adds
to `memory/DECISIONS.md` in the same commit, without which the minimal guard refuses the commit.

A write goes through the guarded write: the policy file, then its change record through the memory-tree
kit's `write_change`, `Unit` the leaf's row tag, `Action` `edit` or `add`, `Before` and `After` that tag
at the file's blob id before and after, `Mark` `semantic`, `Proof` `tty-cli`, `none — run mandate
<run-state path>` or `none — budgets raise`; a record refused puts the file back. Both are staged, and it
prints `Proof: <proof>` and the `Gov-Policy:` trailer line the commit must carry, one per changed leaf.

`propose` writes nothing: it prints the row diff and the `set` command that would apply it.

Exit 0 written or proposed, 1 a write with no proof or no confirmation, 2 a refused key, value, condition
or record, nothing written.

WHAT THIS DOES NOT CHECK: a stated rule in a comment block other than an explicit `reserved: owner`
line, which the change record's argument answers; that the argument is true; the layered proof
`signed` names, which no component implements and the expansion rule reads.
"""
import argparse
import datetime
import difflib
import hashlib
import importlib.util
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import tomllib

sys.dont_write_bytecode = True
KIT =pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from floor import FLOOR_INVARIANTS, read_policy_modules  # noqa: E402
from loop_lib import LoopError, read_memory_tree  # noqa: E402

SAY = "policy-edit"
CONFIRM = "yes"
RESERVED = re.compile(r"^\s*#.*\breserved:\s*owner\b")
CAP_VALUE = re.compile(r"^(\s*[^=#]+=\s*)(\d+)(.*)$")


class Refused(Exception):
    """A verb that stops: `code` its exit and `lines` what it prints."""

    def __init__(self, code, *lines):
        super().__init__(lines[0] if lines else "")
        self.code, self.lines = code, list(lines)


# The guarded write (S5), carried inline because gov's lib dir ships to no install.
# >>> guarded_write_py -- canonical copy: guarded_write.py in the gov lib dir (byte-identical; gated)
#: The route a not-proven refusal ends with (TOOL-dDeclaredLoop-67 S18).
TERMINAL_ROUTE = ("a mintty or other pipe-backed terminal is no console, so run the command under `winpty` "
                  "or in a console window")


def check_terminal_proof():
    """The owner's proof `tty-cli` where standard error is an interactive terminal, else None: the one
    stream dOrderedCharter-15 S5 tests, and the one an agent's shell lacks. A pty wrapper giving an agent
    a terminal passes it, the threat the owner accepted (SA-1). On win32 `isatty` is true for `NUL`, a
    character device, so there the stream's handle must also answer `GetConsoleMode`, which only a
    console does (TOOL-dDeclaredLoop-56 S20); elsewhere `isatty` alone."""
    if not sys.stderr.isatty():
        return None
    if sys.platform == "win32":
        import ctypes
        import msvcrt
        mode = ctypes.c_uint32()
        handle = ctypes.c_void_p(msvcrt.get_osfhandle(sys.stderr.fileno()))
        if not ctypes.windll.kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            return None
    return "tty-cli"


def write_guarded(path, new_text, record):
    """`new_text` written to `path` as UTF-8, or called with the path where it is a callable writing the
    path itself, then `record()`, the caller's record writer, called and its record's path returned.
    Where either step raises, the path's prior bytes are put back, the path removed where it did not
    exist, and the error raised again: no write lands without its record.
    Each write, the restore included, goes to a sibling temp `<name>.<random>.tmp` made by `mkstemp`
    and is `os.replace`d over the path, so the path holds its prior bytes or the new ones, never a
    part of either; a callable is handed that temp, already holding the prior bytes. No fsync."""
    path = pathlib.Path(path)
    held = path.read_bytes() if path.is_file() else None

    def write_target(fill):
        fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=path.name + ".", suffix=".tmp")
        try:
            with os.fdopen(fd, "wb") as fh:
                fh.write(fill if isinstance(fill, bytes) else held or b"")
            if callable(fill):
                fill(pathlib.Path(tmp))
            os.replace(tmp, path)
        except BaseException:
            pathlib.Path(tmp).unlink(missing_ok=True)
            raise

    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        write_target(new_text if callable(new_text) else new_text.encode("utf-8"))
        return record()
    except BaseException:
        if held is None:
            path.unlink(missing_ok=True)
        elif path.is_file() and path.read_bytes() != held:
            write_target(held)
        raise
# <<< guarded_write_py


def read_loop_guard():
    """This kit's guard.py, loaded by file path as `loop_guard`, so it never takes the name `guard` the policy
    kit's minimal guard is imported under."""
    if "loop_guard" not in sys.modules:
        spec = importlib.util.spec_from_file_location("loop_guard", KIT / "guard.py")
        mod = importlib.util.module_from_spec(spec)
        sys.modules["loop_guard"] = mod
        spec.loader.exec_module(mod)
    return sys.modules["loop_guard"]


def run_git(top, *args):
    """`git <args>` in `top` -> its stdout, text; Refused exit 2 naming git's refusal."""
    p = subprocess.run(["git", *args], cwd=top, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if p.returncode:
        raise Refused(2, "%s: refused · git %s exited %d: %s · nothing written" % (
            SAY, " ".join(args), p.returncode, p.stderr.strip()))
    return p.stdout


def parse_cli_value(text):
    """A command-line value as TOML reads it, so `4` is an integer and `true` a boolean; other text a string."""
    try:
        return tomllib.loads("v = " + text)["v"]
    except tomllib.TOMLDecodeError:
        return text


def derive_blob_pin(tag, data):
    """`<tag>@<hash8>`, git's blob id of `data` cut to eight hex, or `none` where the file was absent."""
    if data is None:
        return "none"
    return "%s@%s" % (tag, hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()[:8])


def check_one_change(policy, mguard, text, new, path, value):
    """Refused unless `new` parses to `text` with exactly the leaf `path` changed, to `value`."""
    try:
        old_doc, new_doc = (tomllib.loads(t.removeprefix("﻿")) for t in (text, new))
    except tomllib.TOMLDecodeError as e:
        raise Refused(2, "%s: refused · the edited file would not parse: %s · edit it by hand from a terminal" % (SAY, e))
    changed = mguard.derive_leaf_changes(old_doc, new_doc)
    if set(changed) != {path} or repr(changed[path][1]) != repr(value):
        raise Refused(2, "%s: refused · this file's shape keeps %s from being set by one line: the edit changes %s · "
                         "edit it by hand from a terminal" % (SAY, policy.render_dotted(path),
                                                              ", ".join(policy.render_dotted(k) for k in changed) or "nothing"))


def derive_set_text(policy, mguard, text, path, value):
    """The policy file's text with the leaf `path` set to `value`: the line assigning it rewritten, else a line
    added under its table's header, else the table added at the end."""
    eol = "\r\n" if "\r\n" in text else "\n"
    lines = text.splitlines(keepends=True)
    line = "%s = %s" % (policy.render_dotted(path[-1:]), policy.render_toml_value(value))
    n = policy.derive_key_line(text, path) if text else 0
    if n:
        old = lines[n - 1]
        lines[n - 1] = old[:len(old) - len(old.lstrip())] + line + (old[len(old.rstrip("\r\n")):] or eol)
    else:
        def check_header(ln):
            hit = policy.TABLE_HEADER.fullmatch(ln.rstrip("\r\n"))
            try:
                return bool(hit) and not ln.lstrip().startswith("[[") and policy.parse_key(hit[1]) == path[:-1]
            except policy.Refusal:
                return False
        at = 0 if not path[:-1] else next((i + 1 for i, ln in enumerate(lines) if check_header(ln)), None)
        if at is not None:
            lines.insert(at, line + eol)
        else:
            if lines and not lines[-1].endswith("\n"):
                lines[-1] += eol
            lines += ([eol] if lines else []) + ["[%s]%s" % (policy.render_dotted(path[:-1]), eol), line + eol]
    new = "".join(lines)
    check_one_change(policy, mguard, text, new, path, value)
    return new


def derive_set_plan(top, key, raw):
    """What `set` and `propose` would write: the modules, the leaf path, the value checked, the policy file's
    path, its bytes and text, the leaf's old value, the new text and the row tag."""
    policy, mguard = read_policy_modules()
    guard = read_loop_guard()
    value = parse_cli_value(raw)
    try:
        path = policy.parse_key(key)
        rows = policy.load_catalogue(policy.KIT)
        try:
            why = policy.check_value(policy.read_catalogue_row(path, rows), value)
        except policy.Refusal:
            row = policy.read_catalogue_row(path[:-1], rows)   # a map row's member, `floor.<member>` among them
            if (row.get("allowed") or {}).get("type") != "map":
                raise
            why = policy.check_value(row, {path[-1]: value})
            if path[:-1] == policy.parse_key("floor") and path[-1] not in FLOOR_INVARIANTS:
                why = "%s is no member of the floor: %s" % (path[-1], " ".join(FLOOR_INVARIANTS))
    except policy.Refusal as e:
        raise Refused(2, "%s: refused · %s · nothing written" % (SAY, e))
    if why:
        raise Refused(2, "%s: refused · %s = %s · %s · nothing written" % (SAY, key, policy.render_json(value), why))
    if key == "policy-file.proof":
        try:
            value = guard.check_expansion_value(key, value, guard.read_core_points(), str(top))
        except LoopError as e:
            raise Refused(2, "%s: refused · %s · nothing written" % (SAY, e))
    tag = guard.derive_row_tag(policy, path)
    if tag is None:
        raise Refused(2, "%s: refused · no catalogue row names %s, so no change record can · nothing written" % (SAY, key))
    rel = policy.POLICY_REL
    data = (top / rel).read_bytes() if (top / rel).is_file() else None
    try:
        text = "" if data is None else data.decode("utf-8")
        old = policy.parse_policy(text).get(path) if text.strip() else None
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as e:
        raise Refused(2, "%s: refused · %s does not read: %s · nothing written" % (SAY, rel, e))
    new = None if repr(old) == repr(value) else derive_set_text(policy, mguard, text, path, value)
    return {"policy": policy, "mguard": mguard, "guard": guard, "path": path, "value": value, "rel": rel,
            "data": data, "text": text, "old": old, "new": new, "tag": tag}


def render_proposal(plan, apply):
    """The row diff and the command that applies it."""
    diff = difflib.unified_diff(plan["text"].splitlines(), plan["new"].splitlines(), plan["rel"], plan["rel"],
                                lineterm="", n=1)
    return ["%s: proposal · %s" % (SAY, plan["policy"].render_dotted(plan["path"])), *diff,
            "%s: apply with: %s" % (SAY, apply)]


def write_policy_change(top, args, plan, new_text, action, proof):
    """The policy file and its change record through the guarded write, both staged -> the lines to print."""
    read_memory_tree("build_records.py")
    import build_records
    tag, after = plan["tag"], new_text.encode("utf-8")
    try:
        record = write_guarded(top / plan["rel"], new_text, lambda: build_records.write_change(
            str(top), args.build, args.unit, tag, action, "semantic", derive_blob_pin(tag, plan["data"]),
            derive_blob_pin(tag, after), proof))
    except (ValueError, OSError) as e:
        raise Refused(2, "%s: refused · %s · nothing written" % (SAY, e))
    run_git(top, "add", "--", plan["rel"], record)
    return ["%s: wrote %s" % (SAY, plan["rel"]), "%s: wrote %s" % (SAY, record), "Proof: %s" % proof]


def derive_kit_command(top, verb, *words):
    """The command line naming this file by its path in `top`, never a typed prefix."""
    prefix = run_git(KIT, "rev-parse", "--show-prefix").strip()
    return " ".join(["python", prefix + pathlib.Path(__file__).name, verb, *words])


def run_set(top, args):
    plan = derive_set_plan(top, args.key, args.value)
    shown = plan["policy"].render_dotted(plan["path"])
    if plan["new"] is None:
        return ["%s: %s already reads %s · nothing written" % (SAY, shown, plan["policy"].render_json(plan["value"]))], 0
    proposal = render_proposal(plan, derive_kit_command(top, "set", args.key, args.value, "--build", args.build,
                                                        "--unit", args.unit))
    # S7: the proof the landed revision asks; `signed` and `both` select the layered proof no component
    # implements, read as policy-file.on-missing-expansion says, so the one proof left is `tty-cli`.
    policy, guard = plan["policy"], plan["guard"]
    try:
        asked = guard.check_expansion_value("policy-file.proof", policy.resolve("policy-file.proof").value,
                                            guard.read_core_points(), str(top))
    except (policy.Refusal, LoopError) as e:
        return ["%s: refused · %s · nothing written" % (SAY, e)], 2
    proof = check_terminal_proof() if asked == "tty-cli" else None
    if proof:
        print("\n".join(proposal))
        sys.stderr.write("%s: type %s to write %s: " % (SAY, CONFIRM, plan["rel"]))
        sys.stderr.flush()
        if sys.stdin.readline().strip() != CONFIRM:
            return ["%s: not confirmed · nothing written" % SAY], 1
    else:
        admission, whys = plan["mguard"].check_run_mandate([plan["rel"]])
        if admission is None:
            return proposal + ["%s: not proven · standard error is no terminal and %s · nothing written · %s" % (
                SAY, "; ".join(whys), TERMINAL_ROUTE)], 1
        proof = "none — run mandate %s" % admission.split(", phase ")[0]
    lines = write_policy_change(top, args, plan, plan["new"], "add" if plan["old"] is None else "edit", proof)
    trailer = plan["guard"].render_policy_trailer(plan["policy"], plan["path"], plan["old"], plan["value"])
    return lines + ["%s: the commit carries this trailer line:" % SAY, "Gov-Policy: %s" % trailer], 0


def run_raise(top, args):
    policy, mguard = read_policy_modules()
    guard = read_loop_guard()
    rel, path, cap = policy.POLICY_REL, ("budgets", args.cap), args.cap
    shown = policy.render_dotted(path)

    def build_refusal(why):
        return Refused(2, "%s: refused · %s · %s · nothing written" % (SAY, shown, why))
    if path in mguard.NOT_CAPS:
        raise build_refusal("budgets.enforce and budgets.pinned are no caps")
    oid = mguard.read_blob_id("HEAD", rel)
    head = b"" if oid is None else mguard.run_git("cat-file", "blob", oid)
    text = head.decode("utf-8", "replace")
    data = (top / rel).read_bytes() if (top / rel).is_file() else None
    if data != (None if oid is None else head):
        raise build_refusal("the policy file differs from HEAD; a raise is written over its HEAD text alone")
    old = policy.parse_policy(text).get(path) if text.strip() else None
    if old is None:
        raise build_refusal("not set in the policy file at HEAD: a cap whose value sits in its legacy home is the owner's "
                     "to move into the file")
    if mguard.read_blob_id("HEAD", cap) is None:
        raise build_refusal("%s is no file tracked at HEAD, so no measured-file cap" % cap)
    if not re.fullmatch(r"\d+", args.new) or isinstance(old, bool) or not isinstance(old, int) or int(args.new) <= old:
        raise build_refusal("%s is not an integer above the cap's value at HEAD, %s" % (args.new, old))
    new = int(args.new)
    measured = len((top / cap).read_bytes().replace(b"\r", b""))
    if measured <= old:
        raise build_refusal("condition 1 · %s measures %d bytes, CR-stripped, not above its cap %d" % (cap, measured, old))
    if "\n" in args.argument or "\r" in args.argument or not args.argument.strip():
        raise build_refusal("--argument is one non-empty line")
    lines = text.splitlines(keepends=True)
    n = policy.derive_key_line(text, path)
    hit = CAP_VALUE.match(lines[n - 1].rstrip("\r\n")) if n else None
    if not hit:
        raise build_refusal("no one line assigns the cap, so the RAISED shape cannot be written")
    above = n - 2
    while above >= 0 and lines[above].lstrip().startswith("#"):
        if RESERVED.match(lines[above]):
            raise build_refusal("condition 2 · the comment block above the cap reads reserved: owner")
        above -= 1
    eol = lines[n - 1][len(lines[n - 1].rstrip("\r\n")):] or "\n"
    comment = "# RAISED %d -> %d, %s, %s, measured %d bytes, %s" % (old, new, datetime.date.today().isoformat(),
                                                                    args.unit, measured, args.argument)
    lines[n - 1:n] = [comment + eol, hit[1] + str(new) + hit[3] + eol]
    new_text = "".join(lines)
    check_one_change(policy, mguard, text, new_text, path, new)
    plan = {"rel": rel, "data": data, "tag": guard.derive_row_tag(policy, path)}
    if plan["tag"] is None:
        raise build_refusal("no catalogue row names the cap, so no change record can")
    out = write_policy_change(top, args, plan, new_text, "edit", "none — budgets raise")
    row = "- %s · %s cap %d -> %d: %s" % (args.unit, cap, old, new, args.argument)
    return out + ["%s: the commit carries this trailer line:" % SAY,
                  "Gov-Policy: %s" % guard.render_policy_trailer(policy, path, old, new),
                  "%s: add this row to %s in the same commit, or the minimal guard refuses it:" % (SAY, mguard.DECISIONS),
                  row], 0


def run_propose(top, args):
    plan = derive_set_plan(top, args.key, args.value)
    if plan["new"] is None:
        return ["%s: %s already reads %s · nothing to propose" % (
            SAY, plan["policy"].render_dotted(plan["path"]), plan["policy"].render_json(plan["value"]))], 0
    return render_proposal(plan, derive_kit_command(top, "set", args.key, args.value, "--build", "<slug>",
                                                    "--unit", "<id>")), 0


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="policy_edit.py", description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="verb", required=True)
    for verb in ("set", "propose"):
        sp = sub.add_parser(verb, help="%s one policy key" % ("write" if verb == "set" else "print the diff for"))
        sp.add_argument("key")
        sp.add_argument("value")
        if verb == "set":
            sp.add_argument("--build", required=True)
            sp.add_argument("--unit", required=True)
    rp = sub.add_parser("raise", help="raise one measured-file cap, the agent's door")
    rp.add_argument("cap")
    rp.add_argument("new")
    rp.add_argument("--build", required=True)
    rp.add_argument("--unit", required=True)
    rp.add_argument("--argument", required=True)
    args = ap.parse_args(argv)
    try:
        top = pathlib.Path(run_git(".", "rev-parse", "--show-toplevel").strip())
        os.chdir(top)   # the minimal guard's readers work from the top level
        lines, rc = {"set": run_set, "raise": run_raise, "propose": run_propose}[args.verb](top, args)
    except Refused as e:
        lines, rc = e.lines, e.code
    except LookupError as e:
        lines, rc = ["%s: unarmed · %s · nothing written" % (SAY, e)], 2
    for line in lines:
        print(line)
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
