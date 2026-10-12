# **Serves:** journal TOOL-aSparedSpawn-12
"""Replay the held-tier selection rule AS BUILT over the last N first-parent commits of a branch.

    python <this file> <repo> <legs.tsv> [N] [branch]

The rule is the one `GATE_SELFTESTS=changed` applies in the run-gates kit: a held leg (subject kit or
chunk selftests) is selected when a path in its selection set moved. The set is the epoch-role rows
(`govkit.py shipped --epoch`) of every entry whose `shipped` rows carry one of the leg's suite files,
plus those suite files; a leg no entry owns selects by its guard plus its suite files, and an unguarded
one by any path. Suite files are the argv words carrying a slash and ending .sh, .py or .js. Each
commit is diffed against its first parent, as the research replay was. A leg's cost is its alone
seconds from the legs table: the retry seconds where a ceiling fired, else the pool seconds.

Prints one row per commit, then the share of held leg-seconds selected and the count of commits
selecting nothing. WHAT THIS DOES NOT CHECK: the record and lag halves of the rule (every commit here
is read as one step past a green record), and a branch bar, which diffs against its last record and
so sits between the per-commit mean and the merge-commit rows.
"""
import json
import os
import subprocess
import sys


def read_git(repo, *args):
    """The stdout of one git command in <repo>."""
    return subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True,
                          encoding="utf-8", errors="replace").stdout


def read_shipped(repo, *extra):
    """The rows of `govkit.py shipped` in <repo>, as (entry, role, src) tuples."""
    out = subprocess.run([sys.executable, os.path.join(repo, "tools", "govkit", "govkit.py"), "shipped", *extra],
                         capture_output=True, text=True, encoding="utf-8", cwd=repo).stdout
    return [tuple(r.split("\t")) for r in out.splitlines() if r.count("\t") == 2]


def derive_suites(argv):
    """The suite files a leg runs: its argv words carrying a slash and ending .sh, .py or .js."""
    words = [a.replace("{prefix}", "tools") for a in argv]
    return [w for w in words if "/" in w and not any(c.isspace() for c in w) and w.endswith((".sh", ".py", ".js"))]


def derive_selection(leg, owners, epoch):
    """(owner entries, selection pathspecs) for one held leg, as the runner derives them."""
    suites = derive_suites(leg["argv"])
    ents = set().union(*(owners.get(s, set()) for s in suites))
    if ents:
        return ents, set(suites).union(*(epoch.get(e, set()) for e in ents))
    guard = [g.replace("{prefix}", "tools") for g in leg.get("guard") or []]
    return set(), (set(suites) | set(guard)) if guard else {""}


def check_hit(files, specs):
    """True when any moved file falls under any pathspec, the way the runner matches one."""
    return any(g == "" or f == g.rstrip("/") or f.startswith(g.rstrip("/") + "/") for f in files for g in specs)


def main(argv):
    repo, legt = argv[1], argv[2]
    n = int(argv[3]) if len(argv) > 3 else 30
    branch = argv[4] if len(argv) > 4 else "main"
    owners, epoch = {}, {}
    for e, _role, src in read_shipped(repo):
        owners.setdefault(src, set()).add(e)
    for e, _role, src in read_shipped(repo, "--epoch"):
        epoch.setdefault(e, set()).add(src)
    cost = {}
    for line in open(legt, encoding="utf-8"):
        if line.startswith(("#", "secs")):
            continue
        p = line.rstrip("\n").split("\t")
        cost[p[1]] = min(float(p[0]), float(p[6])) if p[6] else float(p[0])
    legs = json.load(open(os.path.join(repo, "tools", "gate-legs.json"), encoding="utf-8"))
    held = [leg for leg in legs if leg.get("chunk") == "selftests" or leg.get("subject") == "kit"]
    info = [(leg["name"], *derive_selection(leg, owners, epoch), cost.get(leg["name"], 0.0)) for leg in held]
    tot = sum(x[3] for x in info)
    print("held legs %d, held leg-seconds %.0f; legs selecting by their guard: %s" % (
        len(info), tot, ", ".join(x[0] for x in info if not x[1]) or "none"))
    commits = read_git(repo, "log", "--first-parent", "-n", str(n), "--format=%H %s", branch).splitlines()
    # A leg no entry owns and no guard scopes selects on every commit, so the zero-run count is also
    # given with those legs set aside: that is the figure an owner or a guard for them would reach.
    every = {x[0] for x in info if x[2] == {""}}
    print("unowned and unguarded, so selected by every commit: %s" % (", ".join(sorted(every)) or "none"))
    total = zero = only_every = 0.0
    for c in commits:
        sha, subj = c.split(" ", 1)
        files = [f for f in read_git(repo, "diff", "--no-renames", "--name-only", sha + "^1", sha).splitlines() if f]
        ran = [x for x in info if check_hit(files, x[2])]
        secs = sum(x[3] for x in ran)
        total += secs
        zero += not ran
        only_every += not [x for x in ran if x[0] not in every]
        print("%s files %4d | %2d legs %6.0f s | %s" % (sha[:9], len(files), len(ran), secs, subj[:60]))
    k = len(commits) or 1
    print("selected: mean %.0f s per commit, %.1f%% of %.0f held leg-seconds; commits selecting nothing: %d of %d;"
          " selecting nothing beyond the every-commit legs: %d of %d"
          % (total / k, 100 * total / k / (tot or 1), tot, zero, len(commits), only_every, len(commits)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
