#!/usr/bin/env python3
"""chain-packet.py — the front door for a chain build's packet (TOOL-aBatchedPacket-1).

It runs the dClosedLoop packet instrument's own `main` with two of its reads answered in-process,
so `--check` and `--write` stop spawning one git process per spec revision. No instrument byte
moves, and every line printed on stdout is the instrument's own.

Usage (from the worktree root, as the instrument is run):
  python chain-packet.py --write <slug> | --check <slug> | --fixture [...]
      the instrument's own arguments, handed to its own `main` with the two reads installed
  python chain-packet.py --parity <slug>
      render the packet the instrument's way, then with the two reads installed, in one process,
      and compare path, bytes and any refusal; exit 0 identical, 1 different. It costs the
      instrument's walk once
  python chain-packet.py <anything else>
      the instrument as a child with the same arguments (`--repin` goes this way, unchanged)

The two reads:
  the coverage report  the instrument's child `carries.py --report <slug>` is answered by the
                       carries module's own `design`, `join` and `report` over each chain spec's
                       working-tree text with an empty revision list. `report` reads no revision.
                       If that render raises, the instrument's own child runs instead.
  the parent specs     each `git show <ref>:<path>` of `schedule.py#tree_state` is answered from
                       one `tree_lib.py#read_blobs_at` call per parent build. A path the batch
                       cannot answer is read by the instrument's own `git`. That reader runs its
                       git less the variables `tree_lib.GIT_ENV_LEAKS` names, and the instrument's
                       git runs under them. So with any of them set this read is not installed, the
                       instrument's own git reads the parent specs, and one stderr line says so:
                       `chain-packet: <NAME>[, <NAME>] set, so the parent specs are read by the
                       instrument's own git`. The coverage report read stays installed, and
                       `--parity` takes the same branch.

THE FALLBACK. The shortcuts are bound to content: `INSTRUMENT_BLOBS` holds the git blob id of each
instrument whose internals they rely on, compared with the file's bytes BEFORE anything is loaded.
With any role moved, with `tree_lib.py` not beside this script, or with no shortcut mode among the
arguments, the door prints one stderr line, `chain-packet: shortcuts off, ...`, naming every
reason, and runs the instrument as a child. A re-pinned or stubbed instrument is therefore graded
the slow way, never by a shortcut read against other bytes. The ids are constants with no
environment or flag form.

Exit: the instrument's own, or `--parity`'s 0 and 1; 2 when no packet instrument, or more than
one, sits under the instrument folder (one line on stdout, nothing run), and when `--parity` meets
a moved role.

What it does not check: a chain spec REVISION in history that is not UTF-8, on which the
instrument's child raises and the packet refuses, while the door reads no history and renders
(`--parity` reports that case as DIFFERENT); the instrument's Python child failing to start; a
spec path that is not valid Unicode; `read_blobs_at`'s decode, which no blob binds and only the
suite's equality arms and `--parity` see; a CR-only difference in an instrument file, since the
blob comparison folds CRLF; an object format other than SHA-1, where every role reads as moved;
the other modules the instrument loads, which run as they stand on both paths; speed; and whether
the instrument's own reading is right. A caller who runs the instrument directly gets the same
bytes, slowly.

Nor, on the git environment (TOOL-aBatchedPacket-2): a git variable outside `GIT_ENV_LEAKS`, a
graft file among them, under which the batch reader and the instrument's git still run under
different environments, since the door declines only on the twelve names the kit's reader strips;
whether a leak variable that is set is harmless, since the door declines on presence, so such a
run reads the parents the slow way; and the report read under a foreign git directory, which reads
working-tree files on both paths. The suite's arm CP8 compares the parent read's cached answers
with git's own, and its arm CP9 runs the door and the instrument under a foreign `GIT_DIR`. What
those arms and the suite's fixture leave unchecked, a parent spec that is not UTF-8 in CP8 and the
records the leg skips under changed mode among them, is stated in the suite's header.
"""
import hashlib
import importlib.util
import os
import subprocess
import sys
import types
from pathlib import Path

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
INSTRUMENT_DIR = "memory/builds/dClosedLoop/build"
# One git blob id per instrument, each with the reliance points read against that blob. A landing
# that moves an instrument reads its points again against the new bytes, then sets the constant.
INSTRUMENT_BLOBS = {
    # The module names `subprocess`, `carries` and `schedule`; `INSTRUMENTS[0]`, the carries
    # instrument's path; the report call's argument shape in `derive_sources`,
    # `[sys.executable, INSTRUMENTS[0], "--report", slug]`, of whose result it reads `returncode`,
    # `stderr` and `stdout.strip()`; `main`, `render_packet`, `Refusal`, `Unmeasured`; and the two
    # `lru_cache` readers `read_tree` and `read_asks`.
    "packet": "cab3bff165a1bb61a5854f58d350912e79a7b34b",
    # `design()` returning `(builds, nodes, retired)`; `join(builds, nodes, retired, specs, only)`,
    # whose second result is the carriers and whose one read of a revision list sits under
    # `if revs:` and feeds findings alone; `report(b, builds, nodes, specs, carriers)`;
    # `real_specs`'s sorted `*.md` glob of each build's `spec/` folder, read as UTF-8; and `main`'s
    # `--report` branch, which prints `report` and returns 0.
    "carries": "0b5fab9cc06d7b03c50ab94522092e2b9e266ce3",
    # `git(*args, check=True)` returning stdout decoded `text=True, encoding="utf-8"`; and the two
    # calls `tree_state` makes, `git("ls-tree", "-r", "--name-only", ref, <folder>)` once per
    # build and `git("show", f"{ref}:{p}")` once per listed path.
    "schedule": "5aa5421e265b02ba4478f8860ad9a4f5fea94500",
}
FAST_MODES = ("--write", "--check", "--fixture")


# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir


def derive_blob(path):
    """The git blob id of a file's bytes with CRLF folded, as `git hash-object` gives a text file."""
    data = Path(path).read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def resolve_instruments():
    """{role: [each working-tree file of that instrument's shape]}; no unit id is spelled here."""
    return {role: sorted(p.as_posix() for p in Path(INSTRUMENT_DIR).glob(f"*-build-*-{role}.py"))
            for role in INSTRUMENT_BLOBS}


def scan_moved(found):
    """One reason per role that is not the one file its shortcuts were read against."""
    out = []
    for role, want in INSTRUMENT_BLOBS.items():
        paths = found[role]
        if len(paths) != 1:
            out.append(f"{role}: {f'{len(paths)} files' if paths else 'no file'}")
        elif (got := derive_blob(paths[0])) != want:
            out.append(f"{role}: blob {got[:12]}, read against {want[:12]}")
    return out


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_instrument(path, argv):
    """The instrument as a child with the same arguments; it inherits stdout, so its lines are its own."""
    sys.stdout.flush()
    sys.stderr.flush()
    return subprocess.run([sys.executable, path, *argv]).returncode


def run_report(carries, slug):
    """`carries.py --report <slug>`'s stdout, from `real_specs`'s shape with no history."""
    builds, nodes, retired = carries.design()
    specs = {}
    for b in builds:
        for p in sorted(Path(f"memory/builds/{b}/spec").glob("*.md")):
            specs.setdefault(b, []).append((p.as_posix(), p.read_text(encoding="utf-8"), []))
    carriers = carries.join(builds, nodes, retired, specs, slug)[1]
    return carries.report(slug, builds, nodes, specs, carriers) + "\n"


def set_reads(packet, tree_lib):
    """Install the two reads: `packet.subprocess` and `schedule.git` rebound, no file changed."""
    carries, schedule = packet.carries, packet.schedule
    git = schedule.git
    cache = {}

    def run(args, *a, **k):
        if isinstance(args, list) and len(args) == 4 \
                and args[:3] == [sys.executable, packet.INSTRUMENTS[0], "--report"]:
            try:
                return subprocess.CompletedProcess(args, 0, stdout=run_report(carries, args[3]),
                                                   stderr="")
            except Exception as e:      # whatever it is, the refusal must be the instrument's
                print(f"chain-packet: the in-process report raised {type(e).__name__}, running "
                      "carries.py --report as the instrument does", file=sys.stderr)
        return subprocess.run(args, *a, **k)

    def read_git(*args, check=True):
        if len(args) == 5 and args[:3] == ("ls-tree", "-r", "--name-only"):
            out = git(*args, check=check)
            try:
                got = tree_lib.read_blobs_at(".", [(args[3], p) for p in out.split("\n") if p])
            except OSError:
                got = {}
            # read_blobs_at folds CRLF; text=True also folds a lone CR, so this does too.
            cache.update({f"{ref}:{p}": text.replace("\r", "\n")
                          for (ref, p), text in got.items() if text is not None})
            return out
        if len(args) == 2 and args[0] == "show" and args[1] in cache:
            return cache[args[1]]
        return git(*args, check=check)

    # The real module, attribute for attribute, with `run` answering the report call.
    packet.subprocess = types.SimpleNamespace(**{**vars(subprocess), "run": run})
    # read_blobs_at runs its git less GIT_ENV_LEAKS and the instrument's git runs under them, so
    # with one set the two could read different repositories: the instrument's own git stays.
    leaks = [name for name in tree_lib.GIT_ENV_LEAKS if name in os.environ]
    if leaks:
        print(f"chain-packet: {', '.join(leaks)} set, so the parent specs are read by the "
              "instrument's own git", file=sys.stderr)
        return
    schedule.git = read_git


def render_outcome(packet, slug):
    """("packet", path, text), or the instrument's refusal or nothing-to-check with its message."""
    try:
        return ("packet", *packet.render_packet(slug))
    except packet.Refusal as e:
        return ("refused", str(e))
    except packet.Unmeasured as e:
        return ("unmeasured", str(e))


def check_parity(packet, tree_lib, slug):
    """Render the instrument's way, then with the reads installed, and compare the two outcomes."""
    slow = render_outcome(packet, slug)
    packet.read_tree.cache_clear()      # so the second render re-reads everything through the
    packet.read_asks.cache_clear()      # stand-ins and nothing is compared with itself
    set_reads(packet, tree_lib)
    fast = render_outcome(packet, slug)

    def render_outcome_line(o):    # a refusal's message can carry a child's stderr, folded onto the one line
        return f"{o[0]} {len(o[2].encode('utf-8'))} bytes" if o[0] == "packet" \
            else f"{o[0]}: {' '.join(o[1].split())}"
    if slow != fast:
        print(f"chain-packet: parity {slug} · DIFFERENT · the instrument {render_outcome_line(slow)} · "
              f"the door {render_outcome_line(fast)}")
        return 1
    if slow[0] == "packet":
        print(f"chain-packet: parity {slug} · identical · {render_outcome_line(slow)[7:]} · {slow[1]}")
    else:
        print(f"chain-packet: parity {slug} · identical · both {render_outcome_line(slow)}")
    return 0


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    found = resolve_instruments()
    if len(found["packet"]) != 1:
        print(f"chain-packet: {len(found['packet'])} files match the packet instrument's shape under "
              f"{INSTRUMENT_DIR}/, and the door runs exactly one, so nothing was run")
        return 2
    parity = argv[:1] == ["--parity"]
    if parity and len(argv) != 2:
        print("chain-packet: --parity takes one slug and nothing else", file=sys.stderr)
        return 2
    reasons = scan_moved(found)
    tree_lib = kit = None
    try:
        kit = resolve_kit_dir("memory-tree", "tree_lib.py", HERE)
    except LookupError:
        reasons.append("tree_lib.py is not beside this script")
    if not parity and not any(a in FAST_MODES for a in argv):
        reasons.append("no shortcut mode in the arguments")
    if not reasons:     # nothing is loaded before the blobs have been compared
        try:
            tree_lib = load_module("tree_lib", kit / "tree_lib.py")
        except Exception:
            reasons.append("tree_lib.py is not beside this script")
    if reasons:
        print("chain-packet: shortcuts off, running the instrument as it stands — " + "; ".join(reasons),
              file=sys.stderr)
        return 2 if parity else run_instrument(found["packet"][0], argv)
    packet = load_module("packet", found["packet"][0])
    if parity:
        return check_parity(packet, tree_lib, argv[1])
    set_reads(packet, tree_lib)
    return packet.main(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
