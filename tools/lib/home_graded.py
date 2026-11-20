"""home_graded — the tracked paths of an adopter tree that gov grades at home (TOOL-dHomeGraded-1 S1).

The canonical copy. `<prefix>/lib/` is gov-internal and ships nothing, so every consumer carries the
block below INLINE, byte-identical, and `<prefix>/lib/resolve-python.test.sh`'s parity table reds a copy
that drifts.

A kit file gov installed unchanged is gov's bytes: gov's bar grades them against gov's registries and
gov's decisions. An adopter scan that grades them again grades gov's code against the adopter's own,
usually empty, declarations, so every re-adoption reds on sites nobody in that tree wrote. The
receipt names those files exactly: an `engine` row whose `oid` (the blob written) equals its
`gov_oid` (the blob gov shipped). One `git hash-object --stdin-paths` call, which runs the tree's own
clean filters as `git add` would, tells which of them still hold those bytes. A file the adopter
edited hashes to something else and stays in the population.

WHAT IT DOES NOT ANSWER: whether gov's bar is green. A file is gov's to grade, not proven clean.
Every failure (no receipt, an unreadable one, a failed hash) answers the empty set, which grades the
whole tree as before: the safe direction.
"""

# >>> home_graded_py — canonical copy: home_graded.py in gov's lib dir (byte-identical; gated)
def derive_home_graded(root):
    """The set of tracked paths under `root` that a `.governance/install.json` `engine` row installed
    at gov's own bytes (`oid` == `gov_oid`) and that still hash to them. Empty when there is no
    receipt, it does not read, or the hash fails: the caller then grades every path, as before."""
    import json
    import pathlib
    import subprocess
    root = pathlib.Path(root)
    try:
        rows = json.loads((root / ".governance" / "install.json").read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        return set()
    want = {}
    for row in rows:
        if not isinstance(row, dict) or row.get("role") != "engine":
            continue
        path, oid = row.get("path"), row.get("oid")
        if isinstance(path, str) and isinstance(oid, str) and oid and oid == row.get("gov_oid") \
                and ".." not in path.split("/") and (root / path).is_file():
            want[path] = oid
    if not want:
        return set()
    paths = sorted(want)
    try:
        out = subprocess.run(["git", "hash-object", "--stdin-paths"], cwd=str(root),
                             input="".join(p + "\n" for p in paths), capture_output=True,
                             text=True, encoding="utf-8")
    except OSError:
        return set()
    got = out.stdout.split()
    if out.returncode != 0 or len(got) != len(paths):
        return set()
    return {p for p, oid in zip(paths, got) if oid == want[p]}
# <<< home_graded_py
