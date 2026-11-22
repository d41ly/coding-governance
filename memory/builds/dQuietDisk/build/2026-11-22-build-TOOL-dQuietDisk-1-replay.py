#!/usr/bin/env python3
"""The dQuietDisk replay onto dWitnessedBar's landed history (owner: "rebase or re-merge onto its landing").

    python <this file> plan            # print the commits it rewrites and each offender's parts; writes no object
    python <this file> write           # write the objects, print OLD NEW, write the map to the scratchpad
    python <this file> remap <map>     # remap cited commit hashes in the tracked memory/ text files this build owns

dWitnessedBar was replayed before it landed: main carries fb6f1a74c, whose tree is byte-identical to the land tip
ed833f684 this branch merged at e4699ee75, while ed833f684 itself is on no branch main holds. A plain merge of main
would carry the pre-replay copies of dWitnessedBar's commits onto main.

The replay, after dWitnessedBar's own program (memory/builds/dWitnessedBar/build/
2026-11-22-build-TOOL-dWitnessedBar-1-replay.py), rewrites this build's own commits in topo order with
`git hash-object -t commit -w` over each raw object:
  - the merge's second parent ed833f684 becomes fb6f1a74c, so every tree is unchanged;
  - every parent is mapped, and each message's hash citations are remapped, through this build's map and through
    dWitnessedBar's replay map;
  - a `Red-fix:` commit over the inline lane's limits (`routed_commits.py --red-fix-limits`) splits in two: the
    red-fix part (every non-spec path, the original message) and a records part (the spec hunks, L3). The last
    part's tree is the original's.
"""
import json
import os
import re
import subprocess
import sys

S = "C:/Users/d41ly/AppData/Local/Temp/claude/b3f6db677b077b04/0840beea-0651-4dc3-9fe7-f227915b6b42/scratchpad"
DWB_MAP = "C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/replay-map.json"
COA = "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
BUILD_ROOTS = ("memory/builds/dQuietDisk/", "memory/project/readme-contract.txt", "memory/project/unpinned-facts.txt")


def git(*a, inp=None, env=None, ok=(0,)):
    e = dict(os.environ, **(env or {}))
    r = subprocess.run(["git", *a], input=inp, capture_output=True, env=e)
    if r.returncode not in ok:
        sys.exit(f"git {' '.join(a)} failed: {r.stderr.decode(errors='replace')}")
    return r.stdout


def full(s):
    return git("rev-parse", "--verify", s + "^{commit}").decode().strip()


OLD_TIP, NEW_TIP = full("ed833f684"), full("fb6f1a74c")
LOW = full("c2a407b03")


def split_raw(raw):
    head, _, msg = raw.partition(b"\n\n")
    return head.split(b"\n"), msg


def write_commit(lines, msg):
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
        if not re.search(rb"^Red-fix:", git("log", "-1", "--format=%B", c), re.M):
            continue
        r = subprocess.run([sys.executable, "tools/memory-tree/routed_commits.py", "--red-fix-limits", c],
                           capture_output=True)
        if r.returncode == 1:
            out.add(c)
        elif r.returncode != 0:
            sys.exit(f"--red-fix-limits {c} exited {r.returncode}: {r.stdout.decode()[-300:]}")
    return out


def plan_parts(c, parent):
    names = git("diff-tree", "--no-commit-id", "--name-only", "-r", "--no-renames", parent, c).decode().split()
    spec = [p for p in names if re.match(r"memory/builds/[^/]+/spec/", p)]
    rest = [p for p in names if p not in spec]
    if not spec or any(p.startswith(".governance/") for p in rest):
        sys.exit(f"{c[:9]}: an offender this program does not split (spec {len(spec)}, paths {rest})")
    return [("redfix", rest), ("spec", spec)]


def spec_msg(p1, paths):
    return (f"records(dQuietDisk): the spec hunks of the red fix {p1}, split from it at the replay\n\n"
            f"The lane's limit L3 admits no spec path in a `Red-fix:` commit; this records commit carries\n"
            f"{', '.join(paths)}.\n\nPass: none\n{COA}\n").encode()


def base_cite():
    dwb = json.load(open(DWB_MAP, encoding="utf-8"))["cite"]
    return {o: n for o, n in dwb.items() if o != n}


def run(write):
    revs = git("rev-list", "--topo-order", "--reverse", "HEAD", "^" + LOW, "^" + OLD_TIP).decode().split()
    off = offenders(revs)
    print("range", len(revs), "offenders", len(off), [c[:9] for c in sorted(off)])
    parent_map = {OLD_TIP: NEW_TIP}
    cite = base_cite()
    own, parts_of = {}, {}
    idx = f"{S}/qd-replay.index"
    for c in revs:
        lines, msg = split_raw(git("cat-file", "commit", c))
        parents = [ln[7:].decode() for ln in lines if ln.startswith(b"parent ")]
        newp = [parent_map.get(p, p) for p in parents]
        msg2, _n = remap_bytes(msg, cite, make_index(cite))
        if c in off:
            plan = plan_parts(c, parents[0])
            if not write:
                print("split", c[:9], [(k, len(p)) for k, p in plan])
                parent_map[c] = c
                continue
            base = git("rev-parse", parents[0] + "^{tree}").decode().strip()
            first_tree = tree_with(base, c, plan[0][1], idx)
            p1 = write_commit(set_tree(set_parents(lines, newp), first_tree), msg2)
            p2 = write_commit(set_tree(set_parents(lines, [p1]), git("rev-parse", c + "^{tree}").decode().strip()),
                              spec_msg(p1[:9], plan[1][1]))
            cite[c], parent_map[c], own[c] = p1, p2, p1
            parts_of[c] = [("redfix", p1, plan[0][1]), ("spec", p2, plan[1][1])]
            continue
        if newp == parents and msg2 == msg:
            parent_map[c] = c
            continue
        if not write:
            print("rewrite", c[:9], "parents" if newp != parents else "", "msg" if msg2 != msg else "")
            parent_map[c] = c
            continue
        new = write_commit(set_parents(lines, newp), msg2)
        parent_map[c] = cite[c] = own[c] = new
    if not write:
        return
    head = full("HEAD")
    new_head = parent_map[head]
    assert git("rev-parse", head + "^{tree}") == git("rev-parse", new_head + "^{tree}"), "HEAD tree moved"
    json.dump({"own": own, "parent": parent_map, "parts": parts_of, "old_head": head, "new_head": new_head},
              open(f"{S}/qd-replay-map.json", "w", encoding="utf-8"), indent=1)
    print("OLD", head, "NEW", new_head)
    print("rewritten", len(own), "of", len(revs))


def remap(map_path):
    m = json.load(open(map_path, encoding="utf-8"))
    cite = dict(base_cite(), **m["own"])
    index = make_index(cite)
    total = 0
    for f in git("ls-files", "-z", "--", *BUILD_ROOTS).split(b"\0"):
        if not f:
            continue
        p = f.decode()
        data = open(p, "rb").read()
        if b"\0" in data:
            continue
        new, n = remap_bytes(data, cite, index)
        if new != data:
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
