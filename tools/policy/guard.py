"""guard.py - the minimal guard over the policy file and its three neighbours (TOOL-dGroundRules-6).

    python <this kit>/guard.py --staged   # run from the repository's top level

The verdict over the staged change of an agent's commit. It refuses a change to any path
`guarded-paths.txt` lists at HEAD, and admits one agent shape: a single measured-file cap under
`budgets` raised, nothing else among those paths changed, a comment line carrying
`RAISED <old> -> <new>` added directly above the cap, and a `memory/DECISIONS.md` row added in the
same commit. A merge concluded with a parent's blob writes nothing new and is admitted. The mirror
`.governance/policy.json` leaves the judged set when its staged bytes are its render at HEAD and the
render's inputs are staged as HEAD holds them (TOOL-dGroundRules-19), so a catalogue or policy change
is one commit and its regenerated mirror the next. Exit 0 admitted, 1 refused naming every failed
condition, 2 when git cannot say what is staged.

It enforces the defaults of `policy-file.guard` and `policy-file.proof`, owner-only and the TTY proof,
WITHOUT READING EITHER KEY: it imports no policy reader. The owner's proof is the pre-commit hook's,
a committer at a terminal, checked before this runs; this file judges the commit that lacks it.

IT STOPS FORGETTING, NOT EVASION. These pass it: `git commit --no-verify`; a pty wrapper giving an
agent's commit a terminal, the threat the owner accepted; a list line removed in one commit and the
file changed in the next; a commit made on another clone; a cherry-pick or a rebase, which fire no
pre-commit; and this file deleted from the working tree, since the hook resolves the kit there. The
push-time bar does not re-judge authorship.
"""
import difflib
import json
import re
import subprocess
import sys
import tomllib
from pathlib import Path

sys.dont_write_bytecode = True

LIST = "guarded-paths.txt"
POLICY = ".governance/policy.toml"
MIRROR = ".governance/policy.json"
DECISIONS = "memory/DECISIONS.md"
NOT_CAPS = (("budgets", "enforce"), ("budgets", "pinned"))
REMEDY = ("policy-guard: an agent may raise one measured-file cap in this shape; any other change to "
          "these files is the owner's, committed from a terminal.")
MIRROR_REMEDY = (f" The landing renders {MIRROR} and commits it with no hook firing; drop it from this "
                 f"commit: git restore --staged --worktree {MIRROR}")


def run_git(*args, missing=False):
    """`git <args>` from the working directory -> its stdout bytes, or None where `missing` and git
    exits 1, as `rev-parse --verify --quiet` does for an object that is not there. Any other failure
    exits 2: the guard cannot judge what it cannot read, and the hook refuses on it."""
    try:
        p = subprocess.run(["git", *args], capture_output=True)
    except OSError as exc:
        print(f"policy-guard: cannot judge · git did not run: {exc}", file=sys.stderr)
        sys.exit(2)
    if p.returncode == 0:
        return p.stdout
    if missing and p.returncode == 1:
        return None
    err = p.stderr.decode("utf-8", errors="replace").strip()
    print(f"policy-guard: cannot judge · git {' '.join(args)} exited {p.returncode}: {err}", file=sys.stderr)
    sys.exit(2)


def read_blob_id(rev, path):
    """The blob id of `path` at `rev`, `""` naming the index -> its id, or None where it is absent."""
    oid = run_git("rev-parse", "--verify", "--quiet", f"{rev}:{path}", missing=True)
    return None if oid is None else oid.decode("ascii").strip()


def read_guarded_paths():
    """The list at HEAD -> its paths, CR stripped, `#` comments and blank lines dropped. With no HEAD,
    or no list there, nothing is guarded yet: []."""
    if run_git("rev-parse", "--verify", "--quiet", "HEAD^{commit}", missing=True) is None:
        return []
    kit = run_git("-C", str(Path(__file__).absolute().parent), "rev-parse", "--show-prefix")
    oid = read_blob_id("HEAD", kit.decode("utf-8").strip() + LIST)
    if oid is None:
        return []
    text = run_git("cat-file", "blob", oid).decode("utf-8", errors="replace").replace("\r", "")
    return [ln.strip() for ln in text.split("\n") if ln.strip() and not ln.strip().startswith("#")]


def read_touched_paths(guarded):
    """The staged change against HEAD, renames split into a deletion and an addition -> {path: its
    status letter} for each guarded path it touches."""
    fields = run_git("diff", "--cached", "--name-status", "--no-renames", "-z").decode("utf-8").split("\0")
    return {path: status for status, path in zip(fields[0::2], fields[1::2]) if path in guarded}


def check_parent_sides(touched):
    """`touched` less each path whose staged blob is its blob at HEAD or at MERGE_HEAD, when a merge
    is being concluded: a merge taking a side writes nothing new. A path both sides lack stays out."""
    if run_git("rev-parse", "--verify", "--quiet", "MERGE_HEAD", missing=True) is None:
        return touched
    return {p: s for p, s in touched.items()
            if read_blob_id("", p) not in (read_blob_id("HEAD", p), read_blob_id("MERGE_HEAD", p))}


def check_mirror_render():
    """The mirror shape (TOOL-dGroundRules-19) -> None where the staged mirror leaves the touched set,
    else why it stays. It leaves when every input the staged mirror records is staged as HEAD holds
    it, each absent on both sides counting as equal: the policy file, this kit's catalogue and each
    key of its `legacy_blobs`, read from the mirror's own record so an input the render adds needs no
    edit here (TOOL-dGroundRules-25 S19, S21); and when its staged bytes are the stdout of
    `policy.py mirror --print`, the render at HEAD, run under this interpreter and compared as bytes:
    a subprocess, so the guard imports no reader. A render that refuses keeps the mirror in the set,
    naming its line."""
    kit = Path(__file__).absolute().parent
    catalogue = run_git("-C", str(kit), "rev-parse", "--show-prefix").decode("utf-8").strip() + "catalogue.toml"
    staged = read_blob_id("", MIRROR)
    blob = None if staged is None else run_git("cat-file", "blob", staged)
    try:
        legacy = json.loads(blob.decode("utf-8")).get("legacy_blobs") if blob is not None else {}
    except (ValueError, AttributeError):
        legacy = None
    if not isinstance(legacy, dict) or not all(isinstance(k, str) for k in legacy):
        return "records no legacy_blobs object, so its inputs cannot be read; regenerate it"
    for p in (POLICY, catalogue, *sorted(legacy)):
        if read_blob_id("", p) != read_blob_id("HEAD", p):
            return f"the mirror renders HEAD and its input {p} is staged changed: commit {p} first, then regenerate"
    p = subprocess.run([sys.executable, str(kit / "policy.py"), "mirror", "--print"], capture_output=True)
    if p.returncode != 0:
        err = p.stderr.decode("utf-8", errors="replace").strip() or f"exit {p.returncode}"
        return f"its render at HEAD refused: {err}"
    if blob is None or blob != p.stdout:
        return "differs from its render at HEAD"
    return None


def derive_leaf_changes(old, new):
    """Two parsed TOML tables -> {leaf key tuple: (old value, new value)} for each leaf that differs,
    None standing for absent, since TOML has no null. A table is walked; any other value, an array
    included, is a leaf, compared by its repr so 1, 1.0 and true differ."""
    def derive_leaves(table, path=()):
        for k, v in table.items():
            yield from derive_leaves(v, path + (k,)) if isinstance(v, dict) else [(path + (k,), v)]
    a, b = dict(derive_leaves(old)), dict(derive_leaves(new))
    return {k: (a.get(k), b.get(k)) for k in a.keys() | b.keys() if repr(a.get(k)) != repr(b.get(k))}


def check_raise_shape(old_bytes, new_bytes):
    """The admitted shape over the policy file at HEAD and staged -> (each failed condition, the one
    changed leaf as (key, old, new), or None where not exactly one leaf changed on both sides)."""
    try:
        # One leading U+FEFF off each side, as policy.py's derive_bomless_text strips it for every reader.
        old_text, new_text = (b.decode("utf-8").removeprefix("﻿") for b in (old_bytes, new_bytes))
        changes = derive_leaf_changes(tomllib.loads(old_text), tomllib.loads(new_text))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError):
        return ["the policy file does not parse"], None
    if len(changes) != 1:
        return [f"{len(changes)} keys changed; one cap raised is the one agent shape"], None
    (key, (old, new)), = changes.items()
    name = ".".join(s if re.fullmatch(r"[A-Za-z0-9_-]+", s) else json.dumps(s) for s in key)
    if old is None or new is None:
        return [f"a key was {'added' if old is None else 'removed'}: {name}"], None
    why = []
    if key[0] != "budgets" or len(key) < 2 or key[:2] in NOT_CAPS:
        why.append(f"only a cap under budgets.* may be raised, not {name}")
    elif key[-1] not in run_git("ls-tree", "-r", "-z", "--name-only", "HEAD").decode("utf-8").split("\0"):
        why.append(f"{name} is not a measured-file cap: a class row or no file tracked at HEAD")
    counts = all(isinstance(v, int) and not isinstance(v, bool) for v in (old, new))
    if not counts:
        why.append(f"{name} is not a count: {old!r} -> {new!r}")
    elif new < old:
        why.append(f"{name} is a lowering: {old} -> {new}")
    # The text: one old line, and on the new side zero or more comment lines then one other line.
    old_lines, new_lines = old_text.replace("\r", "").split("\n"), new_text.replace("\r", "").split("\n")
    ops = [o for o in difflib.SequenceMatcher(None, old_lines, new_lines, autojunk=False).get_opcodes()
           if o[0] != "equal"]
    added = [new_lines[j] for o in ops for j in range(o[3], o[4])]
    one_block = all(x[2] == y[1] and x[4] == y[3] for x, y in zip(ops, ops[1:]))
    if not (ops and one_block and ops[-1][2] - ops[0][1] == 1 and added
            and all(ln.lstrip().startswith("#") for ln in added[:-1]) and not added[-1].lstrip().startswith("#")):
        why.append("another line of the policy file changed; only the cap's line and comment lines above it may")
    if counts and not any(re.search(rf"RAISED\s+{old}\s*->\s*{new}\b", ln)
                          for ln in added if ln.lstrip().startswith("#")):
        why.append(f"no RAISED {old} -> {new} argument above the cap")
    return why, (name, old, new)


def check_decisions_row():
    """True when the staged change adds at least one `- ` row to memory/DECISIONS.md and removes no line."""
    out = run_git("diff", "--cached", "--no-color", "--no-ext-diff", "-U0", "--", DECISIONS)
    rows, removed, hunk = 0, 0, False
    for ln in out.decode("utf-8", errors="replace").replace("\r", "").split("\n"):
        hunk = hunk or ln.startswith("@@")
        if hunk and ln.startswith("+"):
            rows += ln.startswith("+- ")
        elif hunk and ln.startswith("-"):
            removed += 1
    return rows > 0 and not removed


def main(argv):
    if argv != ["--staged"]:
        print("usage: python guard.py --staged", file=sys.stderr)
        return 2
    guarded = read_guarded_paths()
    touched = check_parent_sides(read_touched_paths(guarded)) if guarded else {}
    mirror_why = check_mirror_render() if MIRROR in touched else None
    if MIRROR in touched and mirror_why is None:
        del touched[MIRROR]
        print(f"policy-guard: admitted · {MIRROR} · equals its render at HEAD")
    if not touched:
        return 0
    refused = [(p, mirror_why if p == MIRROR else f"an agent's commit may change {POLICY} alone among the guarded paths")
               for p in sorted(touched) if p != POLICY]
    cap = None
    if touched.get(POLICY, "M") != "M":
        refused.append((POLICY, f"{'added' if touched[POLICY] == 'A' else 'deleted or retyped'}, not a cap raised"))
    elif POLICY in touched:
        why, cap = check_raise_shape(run_git("cat-file", "blob", read_blob_id("HEAD", POLICY)),
                                     run_git("cat-file", "blob", read_blob_id("", POLICY)))
        refused += [(POLICY, w) for w in why]
        if not check_decisions_row():
            refused.append((POLICY, f"no {DECISIONS} row in this commit, every row HEAD holds kept"))
    if not refused:
        print(f"policy-guard: admitted · {cap[0]} {cap[1]} -> {cap[2]} · its change record attached")
        return 0
    for path, why in refused:
        print(f"policy-guard: refused · {path} · {why}")
    print(REMEDY + (MIRROR_REMEDY if MIRROR in touched else ""))
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
