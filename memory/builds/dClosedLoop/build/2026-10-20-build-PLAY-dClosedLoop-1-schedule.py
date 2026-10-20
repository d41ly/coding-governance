# **Serves:** research PLAY-dClosedLoop-1
"""The chain's schedule across nodes a, b and d: which node takes which build's spec run and build run, and when,
re-derived from the tree at every landing (the execution plan's `[schedule]`). The owner's answers bind it
(`build/…-execution.md` `[answers]`, `[answers-2]` and `[answers-3]`).

Usage (from the worktree root; `git fetch` does not fill the claim cache, `--claims` does):
  . tools/lib/resolve-python.sh && PY=$(resolve_python)
  git fetch; bash tools/unattended/unattended.sh --claims; "$PY" <this file> [--ref <rev>] [--s 0.33] [--b 0.25]
--ref is the commit whose tree is read, HEAD by default; a node re-running it at a landing passes `origin/main`.

INPUTS, all read at --ref except the claim cache:
  - v2's `[chain]` (`build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`), parsed here: each build's stage,
    parents and clauses. A build's units are its clauses, counted twice, by their `cl-` ids and by the "; " split
    `critical-path.py` uses; both must give 22 builds and 509 clauses, or the script stops.
  - each chain build's tracked specs under `memory/builds/<slug>/spec/`: its `**Status:**` token and its
    `**Carries:**`, `**Moved:**`, `**Retired:**` and `**Deferred:**` lines. A build's spec phase is DONE when its specs
    carry or release every clause of its row and none is OPEN or SPECCED; its build phase is DONE when, besides,
    every spec in its folder is CLOSED or WONTDO, an EXTRA unit's spec included.
  - the run claims `unattended.sh --claims` last cached under `refs/gov/remote/runs/<slug>` (no fetch is made here),
    `tools/playbook/fleet.toml` to turn a claim's `node:` user into a fleet tag, and `RESUME_STALE_BOUND` from
    `.unattended.conf`. A `held` claim, or a `live` one whose `beat-utc` is within the bound, pins that build's next
    phase to the claim's node from time 0. A `live` claim past the bound is reported stale and left unpinned, for a
    take-over. A claim on a node outside the three keeps its run off every node's table (held off-fleet), and a
    claim on a SPEC_ONLY node pins only a spec run.
  - two facts no file above holds, declared here from the owner's answers: dTrueNorth runs as ONE whole run and
    carries one unit more than its v2 row, the carry-forward condition for any unit a spec run adds, from a review or
    a discovery (WHOLE, EXTRA: `[answers-2]` item 5, widened by `[answers-3]` item 1); and node b takes spec runs
    only (SPEC_ONLY: `[answers-2]` item 4).

THE MODEL. Each build is two runs: a spec run of s*U units and a build run of (1-s)*U, U its clause count plus any
EXTRA, in units of a full-pace node's work; a WHOLE build is one run of U, which starts at once. Policy J (the schedule
return's): a spec run starts once dTrueNorth has landed, every parent's spec run has closed (a WHOLE parent's run has
landed) and every grandparent has landed; a build run starts once its own spec run has closed and every parent has
landed. Nodes a and d work at pace 1, node b at --b; each node holds one run at a time. The dispatch rule, at every
moment a node is free:
  - a free full-pace node (a before d) takes the ready run with the most downstream work, its bottom level;
  - node b takes the ready SPEC run with the MOST slack among those whose slack covers b's slowdown, (1/b - 1) times
    the run's work, never a run with no slack and never a build run; slack is each run's float in the same graph with
    unlimited nodes at pace 1, so b's slice is smaller and off the critical path (`[answers]` 4, `[answers-2]` 4).

WHAT IT DOES NOT MODEL: wall time, since no unit's wall time is recorded (gap-rt-26) and a unit here is a share of
work, not hours; the spec share s, which history cannot measure; usage limits, holds and resumes; review rounds, the
closing review and the landing bar's wall (up to `GATE_WALL`); the owner's delay in starting each run; the opening,
phase 0 and each node's preparation; how far an in-flight run has got (it is charged its whole phase from time 0);
rework a landing forces on a build in flight; and two runs at once on one node.

Prints the schedule table, each node's load, the first wave, the runs the owner starts in order, each landing with
the runs in flight then, and node b's pace swept from 0.25 to 0.5 beside a and d alone. Exit 0, or 1 when v2's
`[chain]` does not hold 22 builds and 509 clauses or a claim names a node the fleet does not. Every claim it does
not pin is printed with the reason.
"""
import argparse
import datetime
import re
import subprocess
import sys

V2 = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
FLEET = "tools/playbook/fleet.toml"
ROOT = "dTrueNorth"
WHOLE = {"dTrueNorth"}                         # one run, spec and build together (`[answers-2]` item 5)
EXTRA = {"dTrueNorth": 1}                      # its unit beyond v2: the carry-forward condition for any unit a spec
#                                                run adds, from a review or a discovery (`[answers-2]` item 5, widened by
#                                                `[answers-3]` item 1, ER:320)
SPEC_ONLY = {"b"}                              # node b takes spec runs only (`[answers-2]` item 4)
NODES = ("a", "d", "b")                       # the owner's three nodes, full-pace ones first
CID = re.compile(r"`(cl-d[A-Z]\w+-\d{4})`")
ROW = re.compile(r"^\| (d[A-Z]\w+) \| ([^|]+) \| ([^|]+) \| (.+) \| [^|]+ \|$")
STATUS = re.compile(r"^\*\*Status:\*\* ([A-Z]+)", re.M)
CARRY = re.compile(r"^\*\*(?:Carries|Moved|Retired|Deferred):\*\* (cl-d[A-Z]\w+-\d{4})", re.M)
# A landing changes what the nodes load when its clauses change a surface the runs themselves stand on. The schedule
# return's patterns (`surfaces.py`), a hint for the plan's [sync-points], never a verdict.
SURFACES = {
    "driver": r"unattended|run claims?|--plan|--status|`next`|resume tick",
    "lander": r"push-main|lander\b|landing record|pre-push",
    "charter": r"charter|AGENTS\.md",
    "spec-format": r"\*\*Carries:\*\*|TEMPLATE-SPEC|spec template|specs? frozen|derived READY|spec tokens",
    "method": r"build method|BUILD-METHOD|per-pass checklist",
    "roles": r"handoff\.py|\.claude/agents|work order|role agents?|the roster",
    "bar": r"merge bar|gate-legs|run-gates|the bar\b|verdict",
    "hooks": r"\bhooks?\b|PreToolUse|SessionStart",
}


def git(*args, check=True):
    done = subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8")
    if check and done.returncode:
        sys.exit(f"schedule: git {' '.join(args)} failed: {done.stderr.strip()[:200]}")
    return done.stdout


def chain(ref):
    v2 = git("show", f"{ref}:{V2}")
    rows = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
    names = re.findall(r"^\| (d[A-Z]\w+) \|", rows, flags=re.M)
    stage, parents, ids, split = {}, {}, {}, {}
    for ln in rows.split("\n"):
        m = ROW.match(ln)
        if m:
            b = m.group(1)
            stage[b] = m.group(2).strip()
            parents[b] = [p.strip() for p in m.group(3).split(",") if p.strip() in names]
            ids[b] = CID.findall(m.group(4))
            split[b] = len([u for u in m.group(4).split("; ") if u.strip()])
    n_ids = sum(len(v) for v in ids.values())
    if len(ids) != 22 or n_ids != 509 or sum(split.values()) != 509 or any(len(ids[b]) != split[b] for b in ids):
        print(f"schedule: v2's [chain] at {ref} holds {len(ids)} builds and {n_ids} clause ids "
              f"({sum(split.values())} by the '; ' split), not 22 and 509; the schedule is derived from nothing")
        sys.exit(1)
    return names, stage, parents, ids, rows


def tree_state(ref, ids):
    """build -> (spec done, build done), from the build's tracked specs at ref."""
    state = {}
    for b, cl in ids.items():
        paths = [p for p in git("ls-tree", "-r", "--name-only", ref, f"memory/builds/{b}/spec/").split("\n")
                 if p.endswith(".md")]
        statuses, carried = [], set()
        for p in paths:
            text = git("show", f"{ref}:{p}")
            s = STATUS.search(text)
            statuses.append(s.group(1) if s else "NONE")
            carried |= set(CARRY.findall(text))
        spec_done = bool(paths) and set(cl) <= carried and not any(s in ("OPEN", "SPECCED", "NONE") for s in statuses)
        state[b] = (spec_done, spec_done and all(s in ("CLOSED", "WONTDO") for s in statuses))
    return state


def claims(ref, names):
    """build -> (node tag, status) for a held claim or a live one within the stale bound; the others, reported."""
    fleet = git("show", f"{ref}:{FLEET}")
    tag = dict((u, t) for t, u in re.findall(r'^tag = "(\w)"\s*\nuser = "([^"]+)"', fleet, flags=re.M))
    bound = re.search(r'^RESUME_STALE_BOUND="(\d+)"', git("show", f"{ref}:.unattended.conf"), flags=re.M)
    if not bound:
        sys.exit("schedule: .unattended.conf declares no RESUME_STALE_BOUND, so a live claim's age cannot be read")
    now = datetime.datetime.now(datetime.timezone.utc)
    held, other = {}, []
    for ln in git("for-each-ref", "--format=%(refname)", "refs/gov/remote/runs/").split():
        slug = ln.rsplit("/", 1)[1]
        if slug not in names:
            continue
        msg = dict(re.findall(r"^(\w[\w-]*): (.*)$", git("log", "-1", "--format=%B", ln), flags=re.M))
        if msg.get("status") not in ("live", "held"):
            other.append(f"{slug} {msg.get('status', '?')}")
            continue
        if msg.get("node") not in tag:
            print(f"schedule: the claim on {slug} names node user '{msg.get('node')}', which {FLEET} does not")
            sys.exit(1)
        n = tag[msg["node"]]
        if msg["status"] == "live":
            try:
                beat = datetime.datetime.strptime(msg.get("beat-utc", ""), "%Y-%m-%dT%H:%M:%SZ").replace(
                    tzinfo=datetime.timezone.utc)
            except ValueError:
                beat = None            # an unreadable beat refuses a second driver (STOPS 7), so it stays pinned
            if beat is not None and (now - beat).total_seconds() > int(bound.group(1)):
                other.append(f"{slug} stale on {n}: take over per [coordination]")
                continue
        held[slug] = (n, msg["status"])
    return held, other


def graph(names, parents, ids, state, s):
    """run -> (work, predecessors) over the runs not yet done, policy J; a done run is no predecessor."""
    done = {("spec", b) for b in names if state[b][0]} | {("build", b) for b in names if state[b][1]}
    T = {}
    for b in names:
        U = len(ids[b]) + EXTRA.get(b, 0)
        if b == ROOT:
            pre = []
        else:
            grand = {g for p in parents[b] for g in parents[p]}
            pre = [("build", ROOT)] + [("build" if p in WHOLE else "spec", p) for p in parents[b]] \
                + [("build", g) for g in grand]
        if b in WHOLE:                      # one run: the build key carries the whole of it
            T[("build", b)] = (U, pre)
            continue
        T[("spec", b)] = (s * U, pre)
        T[("build", b)] = (U - s * U, [("spec", b)] + [("build", p) for p in parents[b]])
    return {t: (w, sorted({p for p in pre if p not in done})) for t, (w, pre) in T.items() if t not in done}


def float_of(T):
    """Each run's bottom level and its slack, with unlimited nodes at pace 1."""
    succ = {t: [] for t in T}
    for t, (_, pre) in T.items():
        for p in pre:
            succ[p].append(t)
    es, order, seen = {}, [], set()

    def visit(t):
        if t in seen:
            return
        seen.add(t)
        for p in T[t][1]:
            visit(p)
        order.append(t)
    for t in sorted(T):
        visit(t)
    for t in order:
        es[t] = max((es[p] + T[p][0] for p in T[t][1]), default=0.0)
    span = max((es[t] + T[t][0] for t in T), default=0.0)
    lf, bl = {}, {}
    for t in reversed(order):
        lf[t] = min((lf[c] - T[c][0] for c in succ[t]), default=span)
        bl[t] = T[t][0] + max((bl[c] for c in succ[t]), default=0.0)
    return bl, {t: lf[t] - T[t][0] - es[t] for t in T}, span


def simulate(T, speed, pinned):
    """The dispatch rule run forward. Returns start, finish and node per run."""
    bl, slack, _ = float_of(T)
    start, fin, where = {}, {}, {}
    free = {n: 0.0 for n in speed}
    for t, n in pinned.items():
        start[t], fin[t], where[t] = 0.0, T[t][0] / speed[n], n
        free[n] = fin[t]
    left = set(T) - set(pinned)
    now = 0.0
    while left:
        ready = sorted(t for t in left if all(p in fin and fin[p] <= now + 1e-9 for p in T[t][1]))
        for n in [n for n in NODES if n in speed and free[n] <= now + 1e-9]:
            if speed[n] >= 1:
                cand = sorted(ready, key=lambda t: (-bl[t], t))
            else:
                cand = sorted((t for t in ready if (n not in SPEC_ONLY or t[0] == "spec") and slack[t] > 1e-9
                               and slack[t] >= T[t][0] * (1 / speed[n] - 1) - 1e-9), key=lambda t: (-slack[t], t))
            if cand:
                t = cand[0]
                start[t], fin[t], where[t] = now, now + T[t][0] / speed[n], n
                free[n] = fin[t]
                ready.remove(t)
                left.discard(t)
        later = [x for x in list(free.values()) + list(fin.values()) if x > now + 1e-9]
        if left and not later:
            sys.exit("schedule: no node may take any ready run; the dispatch rule deadlocked")
        now = min(later) if later else now
    return start, fin, where


def surfaces(rows):
    out = {}
    for ln in rows.split("\n"):
        m = ROW.match(ln)
        if m:
            cl = [c for c in m.group(4).split("; ") if c.strip()]
            hit = []
            for k, rx in SURFACES.items():
                n = [CID.search(c).group(1)[-4:] for c in cl if re.search(rx, c) and CID.search(c)]
                if n:
                    hit.append(f"{k} {','.join(n[:3])}{'..' if len(n) > 3 else ''}")
            out[m.group(1)] = "; ".join(hit) or "none"
    return out


def run(names, parents, ids, state, held, s, pace, with_b=True):
    T = graph(names, parents, ids, state, s)
    speed = {"a": 1.0, "d": 1.0}
    if with_b:
        speed["b"] = pace
    pinned, notes = {}, []
    for b, (n, _) in held.items():
        t = ("build", b) if state[b][0] or b in WHOLE else ("spec", b)
        if t not in T:
            continue
        if n not in speed:                  # an off-fleet holder: its run stays off every node's table
            speed[n] = 1.0
            pinned[t] = n
            notes.append(f"{b} held off-fleet on {n}")
        elif n in SPEC_ONLY and t[0] != "spec":
            notes.append(f"{b} claimed on {n}, which takes spec runs only: its {t[0]} run is left unpinned")
        else:
            pinned[t] = n
    start, fin, where = simulate(T, speed, pinned)
    return T, start, fin, where, {k: v for k, v in speed.items() if k in NODES}, notes


def kind(t):
    return "whole" if t[1] in WHOLE else t[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="HEAD")
    ap.add_argument("--s", type=float, default=0.33)
    ap.add_argument("--b", type=float, default=0.25)
    a = ap.parse_args()
    names, stage, parents, ids, rows = chain(a.ref)
    state = tree_state(a.ref, ids)
    held, other = claims(a.ref, names)
    T, start, fin, where, speed, notes = run(names, parents, ids, state, held, a.s, a.b)
    bl, slack, span = float_of(T)
    mk = max(fin.values(), default=0.0)
    whole = {}

    def ef(x):                          # the whole-build critical path, as critical-path.py measures it, with EXTRA
        if x not in whole:
            whole[x] = len(ids[x]) + EXTRA.get(x, 0) + max((ef(p) for p in parents[x]), default=0)
        return whole[x]
    for b in names:
        ef(b)
    print(f"read at {a.ref}: 22 builds, 509 clauses; s={a.s}, node b at pace {a.b}; "
          f"specs done {sum(st[0] for st in state.values())}, builds landed {sum(st[1] for st in state.values())}")
    print("claims cached on chain builds: " + (", ".join(f"{b} {st} on {n}" for b, (n, st) in sorted(held.items()))
                                                or "none live or held") + ("; other: " + ", ".join(other) if other else "")
          + ("; " + "; ".join(notes) if notes else ""))
    print(f"makespan {mk:.0f} units; with unlimited nodes {span:.0f}; whole builds after their parents land "
          f"{max(whole.values())}; serial on one node {sum(len(v) for v in ids.values()) + sum(EXTRA.values())} "
          f"(v2's 509 and {sum(EXTRA.values())} unit beyond it)")
    print()
    print("| Build | Stage | Parents | Units | Spec run: node, start-end, slack | Build run: node, start-end, slack |")
    print("|---|---|---|---|---|---|")

    def cell(t):
        if t[0] == "spec" and t[1] in WHOLE:
            return "one whole run, in the next column"
        return "done" if t not in T else f"{where[t]} {start[t]:.0f}-{fin[t]:.0f}, slack {slack[t]:.0f}"
    for b in sorted(names, key=lambda b: (start.get(("build", b), -1), b)):
        print(f"| {b} | {stage[b]} | {', '.join(parents[b]) or 'dClosedLoop'} | {len(ids[b]) + EXTRA.get(b, 0)} | "
              f"{cell(('spec', b))} | {cell(('build', b))} |")
    print()
    for n in speed:
        mine = [t for t in T if where[t] == n]
        busy = sum(fin[t] - start[t] for t in mine)
        print(f"node {n}: busy {busy:.0f} of {mk:.0f} ({100 * busy / mk if mk else 0:.0f}%), "
              f"work {sum(T[t][0] for t in mine):.0f} of {sum(w for w, _ in T.values()):.0f} units, {len(mine)} runs: "
              + ", ".join(f"{sum(1 for t in mine if kind(t) == k)} {k}" for k in ("spec", "build", "whole")))
    print()
    print("first wave, each node's first run:")
    for n in speed:
        mine = sorted((t for t in T if where[t] == n), key=lambda t: start[t])
        print(f"  {n}: " + (f"{kind(mine[0])} {mine[0][1]} at {start[mine[0]]:.0f}" if mine else "no run"))
    print()
    order = sorted(T, key=lambda t: (start[t], t))
    print(f"runs the owner starts, {len(order)}, at {len({round(start[t]) for t in order})} distinct times, "
          f"in order (time, node, run):")
    line = []
    for t in order:
        line.append(f"{start[t]:.0f} {where[t]} {kind(t)} {t[1]}")
    for i in range(0, len(line), 4):
        print("  " + " · ".join(line[i:i + 4]))
    print()
    surf = surfaces(rows)
    print("landings of build and whole runs, with the runs in flight then and the surfaces the landing's clauses touch:")
    for t in sorted((t for t in T if t[0] == "build"), key=lambda t: fin[t]):
        L = fin[t]
        flight = [f"{kind(k)} {k[1]} on {where[k]}" for k in sorted(T, key=lambda k: start[k])
                  if start[k] < L - 1e-9 < fin[k] - 1e-9]
        print(f"  {L:4.0f} {t[1]} lands; in flight: {', '.join(flight) or 'none'}; surfaces: {surf[t[1]]}")
    print()
    print("node b's pace swept (makespan; busy share of a, d, b; b's runs):")
    for pace in (0.25, 0.3, 0.35, 0.4, 0.45, 0.5):
        T2, s2, f2, w2, sp2, _ = run(names, parents, ids, state, held, a.s, pace)
        m2 = max(f2.values(), default=0.0)
        share = {n: sum(f2[t] - s2[t] for t in T2 if w2[t] == n) / m2 * 100 if m2 else 0 for n in sp2}
        bs = sorted((t for t in T2 if w2[t] == "b"), key=lambda t: s2[t])
        print(f"  b {pace:.2f}: {m2:.0f}; a {share['a']:.0f}% d {share['d']:.0f}% b {share['b']:.0f}%; "
              + (", ".join(f"{kind(t)} {t[1]} {s2[t]:.0f}-{f2[t]:.0f}" for t in bs) or "none"))
    T3, s3, f3, w3, sp3, _ = run(names, parents, ids, state, held, a.s, a.b, with_b=False)
    print(f"  a and d alone: {max(f3.values(), default=0.0):.0f}")


if __name__ == "__main__":
    main()
