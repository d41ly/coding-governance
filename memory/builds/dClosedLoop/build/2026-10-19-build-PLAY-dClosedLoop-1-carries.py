# **Serves:** research PLAY-dClosedLoop-1
"""The carries join and its coverage report: every chain build's specs held to the design clauses they carry, the
bootstrap half of the owner's FQ-2 (final-questions `[coverage]` and `[bootstrap]`, dTrueNorth's clauses
`cl-dClosedLoop-0001` to `cl-dClosedLoop-0003`). Until dTrueNorth builds the product join into the `spec tokens` leg,
this instrument checks the chain builds' specs, dTrueNorth's own first.

A spec under `memory/builds/<chain build>/spec/` declares what it carries, one line each:
  **Carries:** cl-dClosedLoop-NNNN@<hash8> whole      the clause, whole, pinned to its text's hash
  **Carries:** cl-dClosedLoop-NNNN@<hash8> part k/n   one of n specs carrying it in parts
  **Carries:** node:<namespace>.<key>                 an owned node the spec builds
  **Derived:** <decision id>                          a spec no clause asks for, and the decision behind it
  **Moved:** cl-dClosedLoop-NNNN to <build> by <decision id>; likewise **Retired:** and **Deferred:**, ... by <decision id>
A clause's hash is the first eight hex digits of the SHA-256 of its text, the id cut off and its whitespace folded.

The join's arms, each a finding (final-questions `[coverage]`):
  per spec   a ghost id; an unbound spec, carrying nothing and derived from nothing; a stale pin; two specs carrying
             one clause whole, or pinning it to two hashes; a revision that stops carrying a clause and records no
             move, retirement or deferral (read against the spec's previous commit);
  per build  a clause or an owned node no spec carries (with --exit, as at a Design exit); a token of a clause, a
             backticked name, missing from every spec that carries it;
  a run that measured no spec is never green: it exits 2.

Usage (from the worktree root):
  python carries.py [--build <slug>] [--exit]   the join over the chain builds' specs as they stand
  python carries.py --report <slug>             the coverage report for one build, as its README renders it
  python carries.py --fixture [--plant <case>] [--build <slug>]
      the join over a spec set built in memory, carrying every clause and node of the build (default dTrueNorth), and
      damaged one way: ghost, unbound, stale, ambiguous, dropped, uncarried, node, token, unmeasured
Exit 0 green, 1 on any finding, 2 when no spec was measured.

What it does not read: whether a spec's text means what its clause means, which the semantic lens reads at the Design
exit (`design.coverage.semantic`); a clause with no backticked name, which the token arm cannot see and the report
lists; and specs outside the chain builds.
"""
import hashlib
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

B = "memory/builds/dClosedLoop/build/"
V2 = B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
CID = re.compile(r"`(cl-d[A-Z]\w+-\d{4})`\s*$")
DECISION = r"[A-Z]+-d[A-Z]\w+-\d+"
CARRY = re.compile(r"^\*\*Carries:\*\* (?:(cl-d[A-Z]\w+-\d{4})@([0-9a-f]{8}) (whole|part (\d+)/(\d+))|node:([a-z-]+)\.(\S+))\s*$",
                   re.M)
DERIVED = re.compile(r"^\*\*Derived:\*\* (" + DECISION + r")\s*$", re.M)
RELEASED = re.compile(r"^\*\*(Moved|Retired|Deferred):\*\* (cl-d[A-Z]\w+-\d{4})(?: to (d[A-Z]\w+))? by (" + DECISION
                      + r")\s*$", re.M)
OWNED = ("item", "policy-key", "point", "record-kind", "tag-namespace", "system")
PLANTS = ("ghost", "unbound", "stale", "ambiguous", "dropped", "uncarried", "node", "token", "unmeasured")


def split_clauses(cell):
    """A chain row's clauses, split on '; ' outside backticks, parentheses and double quotes (the clause scan's rule)."""
    out, cur, depth, tick, quote, i = [], [], 0, False, False, 0
    while i < len(cell):
        ch = cell[i]
        if ch == "`" and not quote:
            tick = not tick
        elif ch == '"' and not tick:
            quote = not quote
        elif not tick and ch == "(":
            depth += 1
        elif not tick and ch == ")":
            depth = max(0, depth - 1)
        if cell.startswith("; ", i) and not (depth or tick or quote):
            out.append("".join(cur))
            cur, i = [], i + 2
            continue
        cur.append(ch)
        i += 1
    out.append("".join(cur))
    return [c.strip() for c in out if c.strip()]


def clause_hash(text):
    body = re.sub(r"\s+", " ", CID.sub("", text)).strip()
    return hashlib.sha256(body.encode("utf-8")).hexdigest()[:8]


def design():
    """Each chain build's clauses, {id: (text, hash8, tokens)}, its owned nodes, and the retired ids."""
    v2 = Path(V2).read_text(encoding="utf-8")
    chain = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
    builds = {}
    for ln in chain.split("\n"):
        m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| [^|]+ \| (.+) \| [^|]+ \|$", ln)
        if not m:
            continue
        cl = {}
        for c in split_clauses(m.group(2)):
            i = CID.search(c)
            if i:
                body = CID.sub("", c).strip()
                cl[i.group(1)] = (body, clause_hash(c), sorted(set(re.findall(r"`([^`\s][^`]*)`", body))))
        builds[m.group(1)] = cl
    cid = v2.split("\n## [clause-ids]", 1)[1].split("\n## ", 1)[0] if "\n## [clause-ids]" in v2 else ""
    retired = set(re.findall(r"`(cl-d[A-Z]\w+-\d{4})`", cid.split("Retired:", 1)[1])) if "Retired:" in cid else set()
    spec = importlib.util.spec_from_file_location("projectmap", B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py")
    mp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mp)
    _, ns = mp.derive()
    nodes = {b: set() for b in builds}
    for name in OWNED:
        for n in ns.get(name, []):
            for k, vs in n["rels"]:
                if k == "owner":
                    for o in vs:
                        if o in nodes:
                            nodes[o].add(f"{name}.{n['key']}")
    return builds, nodes, retired


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8").stdout


def real_specs(builds):
    """{build: [(path, text, previous text or None)]} from each chain build's spec folder."""
    out = {}
    for b in builds:
        for p in sorted(Path(f"memory/builds/{b}/spec").glob("*.md")):
            shas = git("log", "--format=%H", "-2", "--", p.as_posix()).split()
            prev = git("show", f"{shas[1]}:{p.as_posix()}") if len(shas) > 1 else None
            out.setdefault(b, []).append((p.as_posix(), p.read_text(encoding="utf-8"), prev))
    return out


def fixture(builds, nodes, build, plant):
    """A spec set carrying every clause and node of the build, the third clause in two parts, damaged one way."""
    ids = sorted(builds[build])
    lines = [[], []]
    for n, i in enumerate(ids):
        body, h, _ = builds[build][i]
        if n == 2:
            lines[0].append((f"**Carries:** {i}@{h} part 1/2", body))
            lines[1].append((f"**Carries:** {i}@{h} part 2/2", body))
        else:
            lines[n % 2].append((f"**Carries:** {i}@{h} whole", body))
    for k, node in enumerate(sorted(nodes[build])):
        lines[k % 2].append((f"**Carries:** node:{node}", ""))
    texts = ["\n".join(f"{c}\n\n{b}\n" for c, b in ls) for ls in lines]
    specs = [(f"fixture/{build}/spec/unit-{n + 1}.md", t, t) for n, t in enumerate(texts)]
    if plant == "ghost":
        specs[0] = (specs[0][0], specs[0][1] + "\n**Carries:** cl-dClosedLoop-9999@00000000 whole\n", specs[0][2])
    elif plant == "unbound":
        specs.append((f"fixture/{build}/spec/unit-3.md", "A spec that carries nothing.\n", None))
    elif plant == "stale":
        specs[0] = (specs[0][0], re.sub(r"@[0-9a-f]{8}", "@deadbeef", specs[0][1], count=1), specs[0][2])
    elif plant == "ambiguous":
        first = CARRY.search(specs[0][1]).group(0)
        specs[1] = (specs[1][0], specs[1][1] + "\n" + first + "\n", specs[1][2])
    elif plant == "dropped":
        first = CARRY.search(specs[0][1]).group(0)
        specs[0] = (specs[0][0], specs[0][1].replace(first, "", 1), specs[0][2])
        moved = CARRY.search(specs[1][1]).group(0)
        specs[1] = (specs[1][0], specs[1][1] + "\n" + moved.replace("part 2/2", "whole") + "\n", specs[1][2])
    elif plant == "uncarried":
        first = CARRY.search(specs[0][1]).group(0)
        specs[0] = (specs[0][0], specs[0][1].replace(first, ""), specs[0][1].replace(first, ""))
    elif plant == "node":
        both = [s for s in specs if "node:" in s[1]]
        if not both:
            sys.exit(f"carries: {build} owns no node, so the node plant has nothing to drop; pass --build <slug>")
        s = both[0]
        line = re.search(r"^\*\*Carries:\*\* node:\S+\s*$", s[1], flags=re.M).group(0)
        specs[specs.index(s)] = (s[0], s[1].replace(line, ""), s[2].replace(line, ""))
    elif plant == "token":
        # A clause's name dropped from the prose of every spec, the Carries lines left whole.
        tok = next(t for i in ids for t in builds[build][i][2] if not any(t in c for c, _ in lines[0] + lines[1]))

        def strip(text):
            return "\n".join(ln if ln.startswith("**Carries:**") else ln.replace(f"`{tok}`", "").replace(tok, "")
                             for ln in text.split("\n"))
        specs = [(p, strip(t), prev) for p, t, prev in specs]
    elif plant == "unmeasured":
        specs = []
    return {build: specs} if specs else {}


def join(builds, nodes, retired, specs, only=None, exit_mode=False):
    findings, carriers, notes = [], {}, {}
    all_ids = {i: b for b, cl in builds.items() for i in cl}
    for b, items in specs.items():
        for path, text, prev in items:
            carried = CARRY.findall(text)
            if not carried and not DERIVED.search(text):
                findings.append(f"{path}: carries nothing and is derived from nothing (unbound)")
            for cid, h, kind, k, n, nsn, key in carried:
                if nsn:
                    carriers.setdefault(("node", f"{nsn}.{key}"), []).append((path, "whole", None))
                    continue
                if cid in retired:
                    findings.append(f"{path}: carries {cid}, a retired id")
                    continue
                if cid not in all_ids:
                    findings.append(f"{path}: carries {cid}, which no clause carries (a ghost id)")
                    continue
                cur = builds[all_ids[cid]][cid][1]
                if h != cur:
                    findings.append(f"{path}: pins {cid}@{h}, and the clause's text now hashes {cur} (a stale pin)")
                carriers.setdefault(("clause", cid), []).append((path, kind, h))
            if prev:
                before = {c[0] for c in CARRY.findall(prev) if c[0]}
                now = {c[0] for c in carried if c[0]}
                released = {m[1] for m in RELEASED.findall(text)}
                for cid in sorted(before - now - released):
                    findings.append(f"{path}: stopped carrying {cid} since its last revision, with no move, retirement "
                                    f"or deferral recorded")
    for (kind, ref), cs in sorted(carriers.items()):
        whole = [c for c in cs if c[1] == "whole"]
        pins = {c[2] for c in cs}
        if kind == "clause" and (len(whole) > 1 or len(pins) > 1):
            findings.append(f"{ref}: carried whole by {len(whole)} specs" + (f", pinned to {len(pins)} hashes" if len(pins) > 1
                            else "") + f" ({', '.join(c[0] for c in cs)})")
        if kind == "clause" and not whole:
            parts = sorted(c[1] for c in cs)
            n = int(parts[0].split("/")[1]) if parts else 0
            if sorted(int(p.split()[1].split("/")[0]) for p in parts) != list(range(1, n + 1)):
                findings.append(f"{ref}: carried in parts {parts}, not 1 to {n}")
    measured = {b for b, items in specs.items() if items}
    for b in sorted(measured if only is None else measured & {only}):
        texts = {p: t for p, t, _ in specs[b]}
        for cid, (body, h, tokens) in builds[b].items():
            cs = carriers.get(("clause", cid))
            released = any(cid == m[1] for t in texts.values() for m in RELEASED.findall(t))
            if not cs:
                if exit_mode and not released:
                    findings.append(f"{b}: {cid} is carried by no spec (uncarried)")
                continue
            joined = " ".join(texts[c[0]] for c in cs if c[0] in texts)
            for tok in tokens:
                if tok not in joined:
                    findings.append(f"{b}: {cid}'s token `{tok}` appears in none of its carriers")
        for node in sorted(nodes[b]):
            if exit_mode and ("node", node) not in carriers:
                findings.append(f"{b}: owned node {node} is named by no spec")
        notes[b] = sum(1 for cid in builds[b] if not builds[b][cid][2])
    return findings, carriers, measured, notes


def report(b, builds, nodes, specs, carriers):
    cl = builds[b]
    whole = [i for i in cl if any(c[1] == "whole" for c in carriers.get(("clause", i), []))]
    split = [i for i in cl if carriers.get(("clause", i)) and i not in whole]
    released = [(m[0], m[1], m[3]) for _, t, _ in specs.get(b, []) for m in RELEASED.findall(t)]
    uncarried = [i for i in cl if not carriers.get(("clause", i)) and i not in {r[1] for r in released}]
    stale = [i for i in cl if any(c[2] and c[2] != cl[i][1] for c in carriers.get(("clause", i), []))]
    ambiguous = [i for i in cl if len([c for c in carriers.get(("clause", i), []) if c[1] == "whole"]) > 1]
    unnamed = sorted(n for n in nodes[b] if ("node", n) not in carriers)
    derived = [(p, m) for p, t, _ in specs.get(b, []) for m in DERIVED.findall(t)]
    blind = [i for i in cl if not cl[i][2]]
    none = lambda xs: ", ".join(xs) if xs else "none"   # noqa: E731
    return "\n".join([
        f"Coverage of {b}'s {len(cl)} clauses and {len(nodes[b])} owned nodes, over {len(specs.get(b, []))} specs:",
        f"- carried whole: {len(whole)}; carried in parts: {len(split)} ({none(split)})",
        f"- moved, retired or deferred: {none([f'{r[1]} {r[0].lower()} by {r[2]}' for r in released])}",
        f"- uncarried: {none(uncarried)}; stale: {none(stale)}; ambiguous: {none(ambiguous)}",
        f"- owned nodes no spec names: {none(unnamed)}",
        f"- specs derived from no clause: {none([f'{p} ({m})' for p, m in derived])}",
        f"- clauses the token arm cannot see: {none(blind)}"])


def main(argv):
    def opt(flag):
        return argv[argv.index(flag) + 1] if flag in argv else None

    builds, nodes, retired = design()
    plant = opt("--plant")
    if plant and plant not in PLANTS:
        sys.exit(f"carries: no plant {plant}")
    build = opt("--build") or ("dTrueNorth" if "--fixture" in argv else None)
    if build and build not in builds:
        sys.exit(f"carries: {build} is no chain build")
    if "--fixture" in argv:
        specs = fixture(builds, nodes, build, plant)
        exit_mode = True
    else:
        specs = real_specs(builds)
        exit_mode = "--exit" in argv
    if opt("--report"):
        b = opt("--report")
        _, carriers, _, _ = join(builds, nodes, retired, specs, b)
        print(report(b, builds, nodes, specs, carriers))
        return 0
    findings, carriers, measured, _ = join(builds, nodes, retired, specs, build, exit_mode)
    print(f"carries: chain builds {len(builds)}, clauses {sum(len(c) for c in builds.values())}, retired {len(retired)}, "
          f"specs measured {sum(len(v) for v in specs.values())} in {len(measured)} builds · findings {len(findings)}"
          + (f" · fixture {build}" if "--fixture" in argv else "") + (f" · plant {plant}" if plant else ""))
    for f in findings:
        print(f"  {f}")
    if not measured:
        print("carries: no spec measured, so the join reads nothing and is never green")
        return 2
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
