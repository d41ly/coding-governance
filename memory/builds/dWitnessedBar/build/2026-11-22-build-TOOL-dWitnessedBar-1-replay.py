#!/usr/bin/env python3
"""The dWitnessedBar landing replay (owner: "Yes, replay it", 2026-11-22), after dPlacedRequest's recipe.

    python <this file> plan            # print each offender's parts; writes no object
    python <this file> write           # write the objects, print OLD NEW, write the maps to the scratchpad
    python <this file> remap <map>     # remap cited commit hashes in every tracked memory/ text file

The pre-push RANGE half of routed_commits reads no waiver, so every `Red-fix:` commit of `origin/main..HEAD` over
the inline lane's limits blocks the landing. `routed_commits.py --red-fix-limits <rev>` names the offenders; each
commit is rewritten in topo order with `git hash-object -t commit -w` over its raw object, its parents mapped and
the hashes its message cites remapped. A commit with no rewritten parent and no repair keeps its hash.

An offender splits, each part's tree its parent's plus the paths that part takes from the original:
  1. red-fix parts: the routed paths (ROUTED_PATHS `tools/` `skills/`) in chunks of at most 3 paths and 60 lines,
     the first part carrying the original message and every non-routed record path, each later chunk its own
     message with the same `Red-fix:` trailer;
  2. a unit part, for a routed path the parent lacks (L4): named for the unit its subject names, no trailer;
  3. a guarded part (L2, `.governance/`), then a spec part (L3, `memory/builds/*/spec/`), records commits.
The LAST part's tree is the original's, so a descendant's parent maps to it and every later tree is unchanged; a
citation maps to the first part. daa7d653's trailer named no leg and names `gate-leg conformance`.
"""
import json
import os
import re
import subprocess
import sys

S = "C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad"
COA = "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
ROUTED = ("tools/", "skills/")
MAX_PATHS, MAX_LINES = 3, 60


def git(*a, inp=None, env=None, ok=(0,)):
    e = dict(os.environ, **(env or {}))
    r = subprocess.run(["git", *a], input=inp, capture_output=True, env=e)
    if r.returncode not in ok:
        sys.exit(f"git {' '.join(a)} failed: {r.stderr.decode(errors='replace')}")
    return r.stdout


def full(s):
    return git("rev-parse", "--verify", s + "^{commit}").decode().strip()


TRAILER_FIX = full("daa7d653")
# 56569347 re-rendered the guarded policy mirror alone, under a trailer naming no leg: it becomes a records
# commit with no trailer, and its red-fix record is withdrawn.
STRIP = {full("56569347"): (
    "records(dWitnessedBar): TOOL-dWitnessedBar-4's pass legs, the policy mirror re-rendered over the summarised "
    "verdict.tree row\n\n"
    "Replayed as a records commit: the commit re-rendered the guarded policy mirror alone, which the inline\n"
    "lane's limit L2 admits in no `Red-fix:` commit, and its trailer named `regen (policy mirror)`, no leg.\n\n"
    "Pass: none\n" + COA + "\n")}
UNIT_FOR = {full("871d5817"): "TOOL-dWitnessedBar-51"}
UNIT_MSG = {full("871d5817"): (
    "fix(dWitnessedBar): TOOL-dWitnessedBar-51's rule correction stands at gov first: the adopter-rules step "
    "retired to a successor whose witness reads the rule's tag\n\n"
    "The owner ruled \"Yes, fix both\" on the parked decision landing-adopter-rules-witness, option (a).\n"
    "playbook/adopter-rules-to-overlay is retired to playbook/adopter-rules-to-overlay-2. Its up and\n"
    "down are the predecessor's frozen program; its witness, adopter_rules_witness.py, reads each\n"
    "converted rule by its text or by the tag the up derives for it, so unit 51's correction of rule\n"
    "06 reads applied. Split at the replay from the red fix {p1}, whose lane admits no new surface.\n")}
OVERRIDE_FIRST = {full("871d5817"): (
    "fix(dWitnessedBar): the floor step's program back at its landed bytes, on the owner's ruling, so "
    "step-rows-frozen holds\n\n"
    "The owner ruled \"Yes, fix both\" on the parked decision landing-python-floor-frozen, option (a).\n"
    "tools/govkit/steps/python_floor.py is back at the bytes the landed row lib/python-floor-3.15\n"
    "names. TOOL-dWitnessedBar-26's S7 holds through the import: resolve_shell_argv raises where no\n"
    "bash resolves, so the bare name is never spawned; the step prints the refusal as a traceback.\n\n"
    "Pass: none\nRed-fix: step-rows-frozen\n" + COA + "\n")}


def split_raw(raw):
    head, _, msg = raw.partition(b"\n\n")
    return head.split(b"\n"), msg


def write_commit(lines, msg: bytes) -> str:
    return git("hash-object", "-t", "commit", "-w", "--stdin", inp=b"\n".join(lines) + b"\n\n" + msg).decode().strip()


def set_tree(lines, tree):
    return [b"tree " + tree.encode() if ln.startswith(b"tree ") else ln for ln in lines]


def set_parents(lines, parents):
    out, done = [], False
    for ln in lines:
        if ln.startswith(b"parent "):
            if not done:
                out += [b"parent " + p.encode() for p in parents]
                done = True
            continue
        out.append(ln)
    if not done:
        sys.exit("a commit with no parent line in the range")
    return out


def tree_with(base_tree, src, paths, idx):
    env = {"GIT_INDEX_FILE": idx}
    git("read-tree", base_tree, env=env)
    for p in paths:
        ls = git("ls-tree", src, "--", p).decode().strip()
        if ls:
            mode, _t, rest = ls.split(" ", 2)
            git("update-index", "--add", "--cacheinfo", f"{mode},{rest.split(chr(9), 1)[0]},{p}", env=env)
        else:
            git("update-index", "--force-remove", "--", p, env=env)
    return git("write-tree", env=env).decode().strip()


HEX = re.compile(rb"(?<![0-9a-fA-F@])([0-9a-f]{7,40})(?![0-9a-fA-F])")


def make_index(cite):
    index = {}
    for o, n in cite.items():
        if o != n:
            index.setdefault(o[:7], []).append(o)
    return index


def remap_bytes(data, cite, index):
    n = [0]

    def sub(m):
        tok = m.group(1).decode()
        olds = [o for o in index.get(tok[:7], ()) if o.startswith(tok)]
        if len(olds) != 1:
            return m.group(0)
        n[0] += 1
        return cite[olds[0]][:len(tok)].encode()
    return HEX.sub(sub, data), n[0]


def offenders(revs):
    out = set()
    for c in revs:
        if c in STRIP:
            continue
        body = git("log", "-1", "--format=%B", c)
        if not re.search(rb"^Red-fix:", body, re.M):
            continue
        r = subprocess.run(["python3", "tools/memory-tree/routed_commits.py", "--red-fix-limits", c],
                           capture_output=True)
        if r.returncode == 1:
            out.add(c)
        elif r.returncode != 0:
            sys.exit(f"--red-fix-limits {c} exited {r.returncode}: {r.stdout.decode()[-300:]}")
    return out


def plan_parts(c, parent):
    """[(kind, paths)] in commit order; the last part takes every remaining path."""
    rows = git("diff-tree", "--no-commit-id", "--numstat", "-r", "--no-renames", parent, c).decode().splitlines()
    added = set(git("diff-tree", "--no-commit-id", "--name-only", "-r", "--no-renames", "--diff-filter=A",
                    parent, c).decode().split())
    routed, unit, guarded, spec, other = [], [], [], [], []
    for row in rows:
        a, d, p = row.split("\t", 2)
        lines = 10 ** 6 if a == "-" else int(a) + int(d)
        if re.match(r"memory/builds/[^/]+/spec/", p):
            spec.append(p)
        elif p.startswith(".governance/"):
            guarded.append(p)
        elif p.startswith(ROUTED) and (p in added or c in UNIT_FOR and p != "tools/govkit/steps/python_floor.py"):
            unit.append(p)
        elif p.startswith(ROUTED):
            routed.append((p, lines))
        else:
            other.append(p)
    if c in UNIT_FOR:   # the unit part takes the unit's non-routed paths too
        unit += [p for p in other if p.startswith("help/") or p.startswith("memory/map/")]
        other = [p for p in other if p not in unit]
    chunks, cur, cur_n = [], [], 0
    for p, n in routed:
        if cur and (len(cur) == MAX_PATHS or cur_n + n > MAX_LINES):
            chunks.append(cur)
            cur, cur_n = [], 0
        cur.append(p)
        cur_n += n
    if cur:
        chunks.append(cur)
    parts = [("redfix", (chunks[0] if chunks else []) + other)]
    parts += [("redfix-more", ch) for ch in chunks[1:]]
    if unit:
        parts.append(("unit", unit))
    if guarded:
        parts.append(("guarded", guarded))
    if spec:
        parts.append(("spec", spec))
    return parts


def part_msg(kind, c, msg, p1, paths, trailer):
    subj = git("log", "-1", "--format=%s", c).decode().strip()
    files = ", ".join(paths)
    if kind == "redfix-more":
        return (f"fix(dWitnessedBar): a further part of the red fix {p1}, split at the replay to the lane's limits\n\n"
                f"{subj}\nThis part carries {files}.\n\nPass: none\n{trailer}\n{COA}\n").encode()
    if kind == "unit":
        return (UNIT_MSG[c].format(p1=p1) + f"\nPass: none\n{COA}\n").encode()
    if kind == "guarded":
        return (f"records(dWitnessedBar): the policy mirror of the red fix {p1}, split from it at the replay\n\n"
                f"The lane's limit L2 admits no guarded policy file in a `Red-fix:` commit; this records commit\n"
                f"carries {files}.\n\nPass: none\n{COA}\n").encode()
    return (f"records(dWitnessedBar): the spec hunks of the red fix {p1}, split from it at the replay\n\n"
            f"The lane's limit L3 admits no spec path in a `Red-fix:` commit; this records commit carries\n"
            f"{files}.\n\nPass: none\n{COA}\n").encode()


def run(write):
    revs = git("rev-list", "--topo-order", "--reverse", "origin/main..HEAD").decode().split()
    off = offenders(revs)
    print("offenders", len(off))
    parent_map, cite, parts_of = {}, {}, {}
    idx = f"{S}/replay.index"
    for c in revs:
        raw = git("cat-file", "commit", c)
        lines, msg = split_raw(raw)
        parents = [ln[7:].decode() for ln in lines if ln.startswith(b"parent ")]
        newp = [parent_map.get(p, p) for p in parents]
        msg2, _n = remap_bytes(msg, cite, make_index(cite))
        if c in off:
            plan = plan_parts(c, parents[0])
            trailer = re.search(rb"^Red-fix: .*$", msg, re.M).group(0).decode()
            if not write:
                print(c[:9], [(k, len(p)) for k, p in plan])
                parent_map[c] = cite[c] = c
                continue
            prev, base, made = newp[0], git("rev-parse", parents[0] + "^{tree}").decode().strip(), []
            taken = []
            for i, (kind, paths) in enumerate(plan):
                taken += paths
                last = i == len(plan) - 1
                t = git("rev-parse", c + "^{tree}").decode().strip() if last else tree_with(base, c, taken, idx)
                if i == 0:
                    m = OVERRIDE_FIRST.get(c, None)
                    m = m.encode() if m else msg2
                else:
                    m = part_msg(kind, c, msg2, made[0][1][:9], paths, trailer)
                pl = set_parents(lines, [prev] + newp[1:] if i == 0 else [prev])
                new = write_commit(set_tree(pl, t), m)
                made.append((kind, new, paths))
                prev = new
            cite[c], parent_map[c] = made[0][1], made[-1][1]
            parts_of[c] = [(k, n, p) for k, n, p in made]
            continue
        if c == TRAILER_FIX:
            msg2 = msg2.replace(b"Red-fix: regen freshness (tools/gate-legs.json)", b"Red-fix: gate-leg conformance")
        if c in STRIP:
            msg2 = STRIP[c].encode()
        if newp == parents and msg2 == msg:
            parent_map[c] = cite[c] = c
            continue
        if not write:
            parent_map[c] = cite[c] = c
            continue
        new = write_commit(set_parents(lines, newp), msg2)
        parent_map[c] = cite[c] = new
    if not write:
        return
    head = git("rev-parse", "HEAD").decode().strip()
    new_head = parent_map[head]
    assert git("rev-parse", head + "^{tree}") == git("rev-parse", new_head + "^{tree}")
    json.dump({"cite": cite, "parent": parent_map, "parts": parts_of, "old_head": head, "new_head": new_head},
              open(f"{S}/replay-map.json", "w", encoding="utf-8"), indent=1)
    print("OLD", head, "NEW", new_head)
    print("rewritten", sum(1 for k, v in parent_map.items() if k != v), "of", len(revs))


def remap(map_path):
    m = json.load(open(map_path, encoding="utf-8"))
    cite = m["cite"]
    succ = next(n for k, n, _p in m["parts"].get(full("871d5817"), []) if k == "unit")
    index = make_index(cite)
    total = 0
    for f in git("ls-files", "-z", "--", "memory/").split(b"\0"):
        if not f:
            continue
        p = f.decode()
        try:
            data = open(p, "rb").read()
        except OSError:
            continue
        if b"\0" in data:
            continue
        orig = data
        if p.endswith("dWitnessedBar/BACKLOG.md"):
            data = data.replace("CLOSED · TOOL-dWitnessedBar-111 · by 871d58171".encode(),
                                ("CLOSED · TOOL-dWitnessedBar-111 · by " + succ[:9]).encode())
        new, n = remap_bytes(data, cite, index)
        if new != orig:
            open(p, "wb").write(new)
            total += n
            print(n, p)
    print("remapped", total)


if __name__ == "__main__":
    verb = sys.argv[1] if len(sys.argv) > 1 else ""
    if verb in ("plan", "write"):
        run(verb == "write")
    elif verb == "remap":
        remap(sys.argv[2])
    else:
        sys.exit(__doc__)
