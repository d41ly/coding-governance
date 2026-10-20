# Instruments: the execution research's probes and the main loop's verification

**Serves:** research PLAY-dClosedLoop-1

Every probe script the five execution researchers left in their scratch folders, verbatim, so each table in their
returns can be re-run from the build folder (`execution.md` `[research]`). Then the main loop's two checks of claims
the returns leave open. The ids missing:PLAY-dTrueNorth-1, missing:TOOL-dTrueNorth-1 name units no build has minted yet, so each is written `missing:<id>` and the build index does not take it for a unit; restore them to re-run a script.

## [d214]

Dispatch 214, the unattended driver: sizes.py prints each chain build's clause count, selfmod.py the clauses that name the driver's own files, clause.py one clause's text.

### `d214/clause.py` (404 bytes)

```python
import re, sys
V = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
chain = open(V, encoding="utf-8").read().split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
want = set(sys.argv[1:])
for cl in re.split(r"; ", chain):
    ids = re.findall(r"cl-dClosedLoop-(\d{4})", cl)
    if ids and ids[-1] in want:
        print(ids[-1], ":", cl[-700:].replace("\n"," "), "\n")
```

### `d214/selfmod.py` (849 bytes)

```python
import re
V = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
chain = open(V, encoding="utf-8").read().split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
pat = re.compile(r"unattended|run claim|RUN\.md|--preflight|push-main|lander|unattended-build|unattended-unit|BUILD-METHOD|build method|run-state|stop-guard|resume tick|resume-tick", re.I)
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| [^|]+ \| (.+) \| [^|]+ \|$", ln)
    if not m: continue
    hits = []
    for cl in m.group(2).split("; "):
        ids = re.findall(r"cl-dClosedLoop-\d{4}", cl)
        ws = sorted(set(w.lower() for w in pat.findall(cl)))
        if ws: hits.append((ids[-1] if ids else "?", ws))
    if hits: print(m.group(1), len(hits), [h[0] for h in hits][:12], sorted({w for h in hits for w in h[1]}))
```

### `d214/sizes.py` (685 bytes)

```python
import re
V = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
text = open(V, encoding="utf-8").read()
chain = text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
tot_u = tot_c = 0
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| ([^|]+) \| ([^|]+) \| (.+) \| ([^|]+) \|$", ln)
    if m:
        u = len([x for x in m.group(4).split("; ") if x.strip()])
        c = len(set(re.findall(r"cl-dClosedLoop-\d{4}", m.group(4))))
        tot_u += u; tot_c += c
        print(f"{m.group(1):20s} stage={m.group(2).strip():14s} units={u:3d} clause-ids={c:3d} bytes={len(m.group(4))}")
print("total units", tot_u, "clause ids", tot_c)
```

## [d215]

Dispatch 215, coordination: width.py and static.py measure the chain's width and the static partition against the dynamic pick; paths.py lists the paths two unordered builds both name. The claim race (`cas/`: a bare remote and two clones) and the merge-driver probe (`fx/`: two branches each opening a build) were built by git commands the return describes, not by a script.

### `d215/paths.py` (1057 bytes)

```python
import re,sys,itertools
text=open(sys.argv[1],encoding="utf-8").read()
chain=text.split("\n## [chain]",1)[1].split("\n## ",1)[0]
names=re.findall(r"^\| (d[A-Z]\w+) \|",chain,flags=re.M)
rows={};par={}
for ln in chain.split("\n"):
    m=re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| ([^|]+) \| (.+) \| [^|]+ \|$",ln)
    if m:
        toks=set(t for t in re.findall(r"`([^`]+)`",m.group(3)) if re.fullmatch(r"[A-Za-z0-9._/-]+",t) and ("/" in t or re.search(r"\.(sh|py|md|toml|json|js|txt|conf)$",t)))
        rows[m.group(1)]=toks; par[m.group(1)]=[p.strip() for p in m.group(2).split(",") if p.strip() in names]
anc={}
def A(b):
    if b not in anc:
        s=set()
        for p in par[b]: s|={p}|A(p)
        anc[b]=s
    return anc[b]
n=0
for a,b in itertools.combinations(rows,2):
    if a in A(b) or b in A(a): continue   # ordered: not concurrent
    sh=rows[a]&rows[b]
    if sh: n+=1; print(a,b,sorted(sh)[:6])
print("concurrent-capable pairs sharing a named path:",n, "of", sum(1 for a,b in itertools.combinations(rows,2) if not(a in A(b) or b in A(a))))
```

### `d215/static.py` (1513 bytes)

```python
import re,sys,heapq
text=open(sys.argv[1],encoding="utf-8").read()
chain=text.split("\n## [chain]",1)[1].split("\n## ",1)[0]
names=re.findall(r"^\| (d[A-Z]\w+) \|",chain,flags=re.M)
U,P={},{}
for ln in chain.split("\n"):
    m=re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| ([^|]+) \| (.+) \| [^|]+ \|$",ln)
    if m: U[m.group(1)]=len([u for u in m.group(3).split("; ") if u.strip()]); P[m.group(1)]=[p.strip() for p in m.group(2).split(",") if p.strip() in names]
memo={}
def tail(b):
    if b not in memo: memo[b]=U[b]+max([tail(c) for c in U if b in P[c]],default=0)
    return memo[b]
def run(speed,assign=None):
    # event sim: each node runs one build at a time; dynamic picks longest-tail ready build; static picks only its own
    t=0.0;done={};free=set(range(len(speed)));running=[];started=set();who={}
    while len(done)<len(U):
        for n in sorted(free,key=lambda n:-speed[n]):
            ready=[b for b in U if b not in started and all(p in done for p in P[b]) and (assign is None or assign[b]==n)]
            if ready:
                b=max(ready,key=tail);started.add(b);who[b]=n;free.discard(n);heapq.heappush(running,(t+U[b]/speed[n],b,n))
        if not running: return float('inf'),who
        t,b,n=heapq.heappop(running);done[b]=t;free.add(n)
    return t,who
eq,who=run([1,1,1])
print("dynamic, 3 equal nodes:",round(eq,1))
for sp in ([1,1,0.5],[0.5,1,1],[1,0.5,1]):
    d,_=run(sp); s,_=run(sp,who)
    print("speeds",sp,"dynamic",round(d,1),"static(partition from equal run)",round(s,1))
```

### `d215/width.py` (1866 bytes)

```python
import re,sys,heapq
V=sys.argv[1]
text=open(V,encoding="utf-8").read()
chain=text.split("\n## [chain]",1)[1].split("\n## ",1)[0]
names=re.findall(r"^\| (d[A-Z]\w+) \|",chain,flags=re.M)
units,parents={},{}
for ln in chain.split("\n"):
    m=re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| ([^|]+) \| (.+) \| [^|]+ \|$",ln)
    if m:
        units[m.group(1)]=len([u for u in m.group(3).split("; ") if u.strip()])
        parents[m.group(1)]=[p.strip() for p in m.group(2).split(",") if p.strip() in names]
tot=sum(units.values()); print("total units",tot,"builds",len(units))
# list schedule with k nodes, one build per node, build takes units time (spec+build), longest-remaining-path priority
def tail(b,memo={}):
    if b not in memo:
        ch=[c for c in units if b in parents[c]]
        memo[b]=units[b]+max([tail(c) for c in ch],default=0)
    return memo[b]
for k in (1,2,3,4):
    t=0;done=set();running=[];free=k;started=set();log=[];maxw=0
    while len(done)<len(units):
        ready=[b for b in units if b not in started and all(p in done for p in parents[b])]
        ready.sort(key=lambda b:-tail(b))
        while free and ready:
            b=ready.pop(0);started.add(b);heapq.heappush(running,(t+units[b],b));free-=1
        maxw=max(maxw,len(running))
        t,b=heapq.heappop(running);done.add(b);free+=1
        while running and running[0][0]==t:
            _,b2=heapq.heappop(running);done.add(b2);free+=1
    print(f"k={k} makespan={t} units  peak concurrent={maxw}")
# width over time with unlimited nodes
ef={};
def fin(b):
    if b not in ef: ef[b]=max([fin(p) for p in parents[b]],default=0)+units[b]
    return ef[b]
for b in units: fin(b)
pts=sorted(set([ef[b]-units[b] for b in units]))
for s in pts:
    live=[b for b in units if ef[b]-units[b]<=s<ef[b]]
    print(s,len(live),",".join(live))
for b in units: print(b,units[b],parents[b])
```

## [d216]

Dispatch 216, oriented handoffs: packet_probe.py and packet_probe2.py derive a build packet's fields for every chain build, sched_probe.py the 3-node availability, foreign_carry.py plants a spec carrying another build's clause.

### `d216/foreign_carry.py` (1045 bytes)

```python
import sys, importlib.util
sys.dont_write_bytecode = True
B = "memory/builds/dClosedLoop/build/"
s = importlib.util.spec_from_file_location("carries", B + "2026-10-19-build-PLAY-dClosedLoop-1-carries.py")
C = importlib.util.module_from_spec(s); s.loader.exec_module(C)
builds, nodes, retired = C.design()
h31 = builds["dOrderedCharter"]["cl-dClosedLoop-0031"][1]
h01 = builds["dTrueNorth"]["cl-dClosedLoop-0001"][1]
spec = "# missing:TOOL-dTrueNorth-1 — x\n**Carries:** cl-dClosedLoop-0001@%s whole\n**Carries:** cl-dClosedLoop-0031@%s whole\n" % (h01, h31)
specs = {"dTrueNorth": [("memory/builds/dTrueNorth/spec/x.md", spec, None)]}
f, carriers, measured, _ = C.join(builds, nodes, retired, specs, None, False)
print("findings on a dTrueNorth spec carrying dOrderedCharter's cl-0031:", f)
print("dOrderedCharter now counts cl-0031 carried:", ("clause", "cl-dClosedLoop-0031") in carriers)
print("hashes:", "0001@" + h01, "0031@" + h31)
for cid, (t, h, toks) in builds["dTrueNorth"].items(): print(cid, h, len(t.encode()), "B,", len(toks), "tokens")
```

### `d216/packet_probe.py` (4602 bytes)

```python
"""Read-only probe: can a per-chain-build handoff packet be DERIVED from the tree? Run from the worktree root."""
import sys, re, json, subprocess, importlib.util, hashlib
sys.dont_write_bytecode = True
B = "memory/builds/dClosedLoop/build/"
V2 = B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
GAPS = B + "2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md"
BASE = "59ff8f2ac04a967751eae00de6856afbea66c033"
spec = importlib.util.spec_from_file_location("carries", B + "2026-10-19-build-PLAY-dClosedLoop-1-carries.py")
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)

def git(*a): return subprocess.run(["git", *a], capture_output=True, text=True, encoding="utf-8").stdout

def chain(text):
    body = text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
    rows = {}
    for ln in body.split("\n"):
        m = re.match(r"^\| (d[A-Z]\w+) \| ([^|]+) \| ([^|]+) \| (.+) \| ([^|]+) \|$", ln)
        if not m: continue
        cl = {}
        for c in C.split_clauses(m.group(4)):
            i = C.CID.search(c)
            if i: cl[i.group(1)] = (C.CID.sub("", c).strip(), C.clause_hash(c))
        rows[m.group(1)] = dict(stage=m.group(2).strip(), parents=[p.strip() for p in m.group(3).split(",")],
                               clauses=cl, gaps_raw=m.group(5).strip())
    return rows

base_txt = git("show", f"{BASE}:{V2}")
head_txt = open(V2, encoding="utf-8").read()
cb, ch = chain(base_txt), chain(head_txt)
names = set(cb)
gap_keys = set(re.findall(r"^\| (gap-[a-z]+-\d+) \|", open(GAPS, encoding="utf-8").read(), re.M))

def expand(raw):
    out, bad = [], []
    for part in [p.strip() for p in raw.split(",")]:
        m = re.fullmatch(r"(gap-[a-z]+-)(\d+) to (gap-[a-z]+-)(\d+)", part)
        if m and m.group(1) == m.group(3):
            w = len(m.group(2)); out += [f"{m.group(1)}{n:0{w}d}" for n in range(int(m.group(2)), int(m.group(4)) + 1)]
        elif re.fullmatch(r"gap-[a-z]+-\d+", part): out.append(part)
        else: bad.append(part)
    return out, bad

def ancestors(b):
    seen, st = set(), [p for p in cb[b]["parents"] if p in names]
    while st:
        p = st.pop()
        if p not in seen: seen.add(p); st += [q for q in cb[p]["parents"] if q in names]
    return seen

children = {b: sorted(c for c in cb if b in cb[c]["parents"]) for b in cb}
outside = head_txt.split("\n## [chain]", 1)[0] + "\n## " + head_txt.split("\n## [chain]", 1)[1].split("\n## ", 1)[1]
tot = {"clauses": 0, "moved_hash": 0, "gaps": 0, "gaps_missing": 0, "gaps_bad": 0, "fwd": 0, "fwd_standin": 0}
owners = {}
report = {}
for b in cb:
    cl = cb[b]["clauses"]; anc = ancestors(b)
    moved = [i for i in cl if ch[b]["clauses"].get(i, (None, None))[1] != cl[i][1]]
    gaps, bad = expand(cb[b]["gaps_raw"]); missing = [g for g in gaps if g not in gap_keys]
    for g in gaps: owners.setdefault(g, []).append(b)
    refs_anc, fwd, fwd_si = {}, {}, {}
    for i, (t, h) in cl.items():
        for o in sorted(names - {b}):
            if re.search(r"\b" + o + r"\b", t):
                if o in anc: refs_anc.setdefault(o, []).append(i)
                else:
                    fwd.setdefault(o, []).append(i)
                    if re.search(r"stand(s|ing)?[- ]in|until " + o + r"|before " + o + r"|" + o + r"'s [\w-]+ (lands|land)", t): fwd_si.setdefault(o, []).append(i)
    nbytes = sum(len(t.encode()) for t, _ in cl.values())
    outside_mentions = len(re.findall(r"\b" + b + r"\b", outside))
    report[b] = dict(stage=cb[b]["stage"], parents=cb[b]["parents"], ancestors=len(anc), children=children[b], clauses=len(cl),
                     clause_bytes=nbytes, hash_moved_since_base=moved, gaps=len(gaps), gaps_missing=missing, gaps_unparsed=bad,
                     refs_to_ancestors={k: len(v) for k, v in refs_anc.items()},
                     refs_to_non_ancestors={k: len(v) for k, v in fwd.items()},
                     standin_like={k: len(v) for k, v in fwd_si.items()}, mentions_outside_chain=outside_mentions)
    tot["clauses"] += len(cl); tot["moved_hash"] += len(moved); tot["gaps"] += len(gaps); tot["gaps_missing"] += len(missing)
    tot["gaps_bad"] += len(bad); tot["fwd"] += sum(len(v) for v in fwd.values()); tot["fwd_standin"] += sum(len(v) for v in fwd_si.values())
dup = {g: o for g, o in owners.items() if len(o) > 1}
unowned = sorted(gap_keys - set(owners))
print(json.dumps(tot)); print("gap keys in register", len(gap_keys), "owned", len(owners), "owned twice", len(dup), "unowned", len(unowned), unowned[:8])
print("baseline==HEAD for v2 chain:", cb == ch)
for b, r in report.items():
    print(b, json.dumps(r))
```

### `d216/packet_probe2.py` (1813 bytes)

```python
import sys, re, runpy, json
sys.dont_write_bytecode = True
sys.argv = ["x"]
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    g = runpy.run_path(sys.argv0 if False else r"C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/exec/d216/packet_probe.py")
cb, names, head = g["cb"], g["names"], g["head_txt"]
anc = g["ancestors"]
# policy keys by owner
pol = head.split("\n## [policies]", 1)[1].split("\n## ", 1)[0]
own = {}
for ln in pol.split("\n"):
    cells = [c.strip() for c in ln.strip().strip("|").split("|")]
    if len(cells) >= 5 and cells[0].startswith("`") and cells[-1] in names:
        own.setdefault(cells[-1], []).append(cells[0].strip("`"))
print("policy keys with a chain-build owner:", sum(len(v) for v in own.values()), {b: len(v) for b, v in own.items()})
print("dTrueNorth owns:", own.get("dTrueNorth"))
# unclassified forward refs
unc = []
for b in cb:
    A = anc(b)
    for i, (t, h) in cb[b]["clauses"].items():
        for o in sorted(names - {b} - A):
            if re.search(r"\b" + o + r"\b", t) and not re.search(r"stand(s|ing)?[- ]in|until " + o + r"|before " + o + r"|" + o + r"'s [\w-]+ (lands|land)", t):
                k = t.find(o); unc.append((b, i, o, t[max(0, k-90):k+60].replace("\n", " ")))
print("forward mentions not matching the stand-in pattern:", len(unc))
for u in unc[:8]: print("  ", u[0], u[1], u[2], "…" + u[3] + "…")
# owed / planned sections mention
for sec in ("[owed]", "[planned]", "[open]", "[enforcement]"):
    s = head.split("\n## " + sec, 1)[1].split("\n## ", 1)[0]
    print(sec, {b: len(re.findall(r"\b" + b + r"\b", s)) for b in ("dTrueNorth", "dGroundRules", "dOrderedCharter", "dTotalRecall")})
```

### `d216/sched_probe.py` (1536 bytes)

```python
import sys, runpy, io, contextlib, heapq
sys.dont_write_bytecode = True
with contextlib.redirect_stdout(io.StringIO()):
    g = runpy.run_path(r"C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/exec/d216/packet_probe.py")
cb, names = g["cb"], g["names"]
dur = {b: len(cb[b]["clauses"]) for b in cb}
par = {b: [p for p in cb[b]["parents"] if p in names] for b in cb}
# longest remaining path priority
memo = {}
def tail(b):
    if b not in memo: memo[b] = dur[b] + max([tail(c) for c in cb if b in par[c]] or [0])
    return memo[b]
done, running, t, free, log = set(), [], 0, 3, []
started = set(); busy = 0; widths = []
while len(done) < len(cb):
    ready = sorted([b for b in cb if b not in started and all(p in done for p in par[b])], key=lambda b: -tail(b))
    widths.append((t, len(ready) + len(running)))
    while free and ready:
        b = ready.pop(0); started.add(b); heapq.heappush(running, (t + dur[b], b)); free -= 1; log.append((t, b))
    ft, b = heapq.heappop(running); t = ft; done.add(b); free += 1
    while running and running[0][0] == t:
        _, b2 = heapq.heappop(running); done.add(b2); free += 1
print("build-level, 3 nodes, unit = clause: makespan", t, "of serial", sum(dur.values()))
print("concurrently available builds at each event (t, n):", widths)
idle_first = sum(1 for (tt, n) in widths if n < 3)
print("events with fewer than 3 builds available:", idle_first, "of", len(widths))
```

## [d217]

Dispatch 217, per-node distribution: schedule.py parses v2 `[chain]` and prints earliest start, finish and slack; heft.py is the list scheduler; stale.py policy J and the staleness measure; planj.py the recommended table (`python3 planj.py <dir> <worktree> 0.33 0.25 any full J`); noise.py the static-versus-re-dispatch draws; surfaces.py maps clauses to the surfaces nodes run on; compare.py and plan.py the earlier sweeps.

### `d217/compare.py` (1002 bytes)

```python
import sys, importlib.util
here = sys.argv[1]; root = sys.argv[2]
sys.argv = [here + "/schedule.py", root]
spec = importlib.util.spec_from_file_location("sch", here + "/schedule.py"); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
U = S.U
print("serial on one reference node:", sum(U.values()))
for bs in (0.25, 0.5):
  for s in (0.2, 0.33, 0.5):
    sp = {"a": 1.0, "d": 1.0, "b": bs}
    row = []
    for pol in "ABC":
        for aff in ("same", "any"):
            mk, *_ = S.simulate(s, pol, sp, aff); row.append(f"{pol}/{aff}={mk:.0f}")
    # lower bounds
    T = S.tasks(s, "B"); bl = S.bottom(T); cp = max(bl.values())
    lb = max(cp, sum(U.values()) / sum(sp.values()))
    # two-node (a,d only), policy B any
    mk2, *_ = S.simulate(s, "B", {"a": 1.0, "d": 1.0}, "any")
    mkA2, *_ = S.simulate(s, "A", {"a": 1.0, "d": 1.0}, "same")
    print(f"b={bs} s={s}: " + "  ".join(row) + f"  | bound(B)={lb:.0f} (cp {cp:.0f}) | a+d only: A/same={mkA2:.0f} B/any={mk2:.0f}")
```

### `d217/heft.py` (2659 bytes)

```python
"""Speed-aware list scheduling (earliest FINISH, HEFT-like) over schedule.py's task graph.
roles: which phases each node may run, e.g. {"a":{"spec","build"},"d":{"spec","build"},"b":{"spec"}}."""
import sys, importlib.util
here = sys.argv[1]; root = sys.argv[2]
sys.argv = [here + "/schedule.py", root]
spec = importlib.util.spec_from_file_location("sch", here + "/schedule.py"); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)

def heft(s, pol, speeds, roles, affinity="any"):
    T = S.tasks(s, pol); bl = S.bottom(T)
    fin, where, start = {}, {}, {}
    free = {n: 0.0 for n in speeds}
    rem = set(T)
    while rem:
        ready = [t for t in rem if all(q in fin for q in T[t][1])]
        best = None
        for t in ready:
            rt = max([fin[q] for q in T[t][1]], default=0.0)
            for n in speeds:
                if t[0] not in roles[n]: continue
                if affinity == "same" and t[0] == "build" and where.get(("spec", t[1]), n) != n: continue
                st = max(rt, free[n]); ft = st + T[t][0] / speeds[n]
                key = (st, -bl[t], ft, n)   # start soonest, most critical first, then fastest node
                if best is None or key < best[0]: best = (key, t, n, st, ft)
        # refine: for the chosen task, take the node with the earliest finish
        _, t, _, _, _ = best
        rt = max([fin[q] for q in T[t][1]], default=0.0)
        opts = []
        for n in speeds:
            if t[0] not in roles[n]: continue
            if affinity == "same" and t[0] == "build" and where.get(("spec", t[1]), n) != n: continue
            st = max(rt, free[n]); opts.append((st + T[t][0] / speeds[n], st, n))
        ft, st, n = min(opts)
        fin[t], start[t], where[t] = ft, st, n; free[n] = ft; rem.discard(t)
    return max(fin.values()), start, fin, where, T

if __name__ == "__main__":
    full = {"spec", "build"}
    for bs in (0.25, 0.5):
        for s in (0.2, 0.33, 0.5):
            sp = {"a": 1.0, "d": 1.0, "b": bs}
            out = []
            for name, roles, pol in (
                ("A3", {"a": full, "d": full, "b": full}, "A"),
                ("B3", {"a": full, "d": full, "b": full}, "B"),
                ("C3", {"a": full, "d": full, "b": full}, "C"),
                ("Bb-spec", {"a": full, "d": full, "b": {"spec"}}, "B"),
                ("Cb-spec", {"a": full, "d": full, "b": {"spec"}}, "C"),
                ("Aad", {"a": full, "d": full}, "A"),
            ):
                spd = {n: sp[n] for n in roles}
                mk, *_ = heft(s, pol, spd, roles); out.append(f"{name}={mk:.0f}")
            print(f"b={bs} s={s}: " + "  ".join(out))
```

### `d217/noise.py` (2020 bytes)

```python
"""B's staleness, and static-table vs re-dispatch under duration noise (each phase x U(0.6,1.6), 300 draws, seed 7)."""
import sys, io, contextlib, random, importlib.util
here, root = sys.argv[1], sys.argv[2]
sys.argv = [here + "/stale.py", here, root]
spec = importlib.util.spec_from_file_location("stale", here + "/stale.py"); M = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(M)
H, S = M.H, M.S; full = {"spec", "build"}
sp = {"a": 1.0, "d": 1.0, "b": 0.25}; roles = {"a": full, "d": full, "b": full}
for pol in "BCJ":
    mk, start, fin, where, T = H.heft(0.33, pol, sp, roles)
    st = [sum(1 for o in M.SURF if o != b and fin[("spec", b)] <= fin[("build", o)] <= start[("build", b)]) for b in S.order]
    print(f"{pol}: makespan {mk:.0f} staleness {sum(st)} max {max(st)}")
mk0, start0, fin0, where0, T0 = H.heft(0.33, "J", sp, roles)
seq = {n: sorted([t for t in T0 if where0[t] == n], key=lambda t: start0[t]) for n in sp}
rng = random.Random(7); stat, dyn = [], []
orig = S.tasks
for _ in range(300):
    f = {t: rng.uniform(0.6, 1.6) for t in T0}
    Tn = {t: (T0[t][0] * f[t], T0[t][1]) for t in T0}
    # static: same node, same per-node order
    fin, free, done = {}, {n: 0.0 for n in sp}, set(); ptr = {n: 0 for n in sp}
    while len(fin) < len(Tn):
        moved = False
        for n in sp:
            if ptr[n] < len(seq[n]):
                t = seq[n][ptr[n]]
                if all(q in fin for q in Tn[t][1]):
                    s0 = max([fin[q] for q in Tn[t][1]] + [free[n]]); fin[t] = s0 + Tn[t][0] / sp[n]; free[n] = fin[t]; ptr[n] += 1; moved = True
        if not moved: raise SystemExit("static deadlock")
    stat.append(max(fin.values()))
    S.tasks = lambda s, pol, Tn=Tn: Tn
    dyn.append(H.heft(0.33, "J", sp, roles)[0]); S.tasks = orig
q = lambda xs, p: sorted(xs)[int(p * (len(xs) - 1))]
print(f"static table: median {q(stat,.5):.0f} p90 {q(stat,.9):.0f} | re-dispatch: median {q(dyn,.5):.0f} p90 {q(dyn,.9):.0f}")
```

### `d217/plan.py` (2336 bytes)

```python
"""The recommended schedule: policy C (spec after dTrueNorth lands and every parent's spec set closes; build after
every parent lands), speed-aware list scheduling, node b spec-only. Prints the per-phase table, the per-node load,
utilisation, sync points and the first wave. Usage: python plan.py <scratch dir> <worktree> [s] [b-speed] [same|any]"""
import sys, importlib.util
here, root = sys.argv[1], sys.argv[2]
s = float(sys.argv[3]) if len(sys.argv) > 3 else 0.33
bs = float(sys.argv[4]) if len(sys.argv) > 4 else 0.25
aff = sys.argv[5] if len(sys.argv) > 5 else "any"
argv0 = sys.argv; sys.argv = [here + "/heft.py", here, root]
spec = importlib.util.spec_from_file_location("heft", here + "/heft.py"); H = importlib.util.module_from_spec(spec); spec.loader.exec_module(H)
S = H.S
full = {"spec", "build"}
sp = {"a": 1.0, "d": 1.0, "b": bs}
roles = {"a": full, "d": full, "b": {"spec"}}
mk, start, fin, where, T = H.heft(s, "C", sp, roles, aff)
es, ef, ls, lf, cp, kids = S.unbounded()
print(f"s={s} b={bs} affinity={aff}: makespan {mk:.0f} (serial 509, whole-build critical path {cp})")
print("| Build | Parents | Units | Slack | Spec node | Spec start-end | Build node | Build start-end |")
print("|---|---|---|---|---|---|---|---|")
for b in sorted(S.order, key=lambda b: (start[("build", b)], b)):
    a_, b_ = ("spec", b), ("build", b)
    print(f"| {b} | {', '.join(S.P[b]) or 'dClosedLoop'} | {S.U[b]} | {ls[b]-es[b]} | {where[a_]} | {start[a_]:.0f}-{fin[a_]:.0f} | {where[b_]} | {start[b_]:.0f}-{fin[b_]:.0f} |")
for n in sp:
    busy = sum(fin[t] - start[t] for t in T if where[t] == n)
    print(f"node {n}: busy {busy:.0f} of {mk:.0f} ({100*busy/mk:.0f}%), phases {sum(1 for t in T if where[t]==n)}")
print("first wave (start 0 or at dTrueNorth's landing):")
tn = fin[("build", "dTrueNorth")]
for t in sorted(T, key=lambda t: start[t]):
    if start[t] <= tn + 1e-9: print(f"  {t[0]} {t[1]} on {where[t]} {start[t]:.0f}-{fin[t]:.0f}")
print(f"dTrueNorth lands at {tn:.0f}")
print("sync points: at each landing, the phases in flight on any node")
for b in sorted(S.order, key=lambda b: fin[("build", b)]):
    L = fin[("build", b)]
    infl = [f"{k[0]}:{k[1]}@{where[k]}" for k in T if start[k] < L - 1e-9 < fin[k] - 2e-9 and k != ("build", b)]
    print(f"  {L:6.0f} {b} lands; in flight: {', '.join(infl) or 'none'}")
```

### `d217/planj.py` (2530 bytes)

```python
"""The recommended schedule: policy C (spec after dTrueNorth lands and every parent's spec set closes; build after
every parent lands), speed-aware list scheduling, node b spec-only. Prints the per-phase table, the per-node load,
utilisation, sync points and the first wave. Usage: python plan.py <scratch dir> <worktree> [s] [b-speed] [same|any]"""
import sys, importlib.util
here, root = sys.argv[1], sys.argv[2]
s = float(sys.argv[3]) if len(sys.argv) > 3 else 0.33
bs = float(sys.argv[4]) if len(sys.argv) > 4 else 0.25
aff = sys.argv[5] if len(sys.argv) > 5 else "any"
argv0 = list(sys.argv); sys.argv = [here + "/stale.py", here, root]
spec = importlib.util.spec_from_file_location("stale", here + "/stale.py"); H0 = importlib.util.module_from_spec(spec); import io, contextlib
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(H0)
H = H0.H
S = H.S
full = {"spec", "build"}
sp = {"a": 1.0, "d": 1.0, "b": bs}
roles = {"a": full, "d": full, "b": full if (sys.argv[6] if len(sys.argv) > 6 else "full") == "full" else {"spec"}}
mk, start, fin, where, T = H.heft(s, (argv0[7] if len(argv0) > 7 else "J"), sp, roles, aff)
es, ef, ls, lf, cp, kids = S.unbounded()
print(f"s={s} b={bs} affinity={aff}: makespan {mk:.0f} (serial 509, whole-build critical path {cp})")
print("| Build | Parents | Units | Slack | Spec node | Spec start-end | Build node | Build start-end |")
print("|---|---|---|---|---|---|---|---|")
for b in sorted(S.order, key=lambda b: (start[("build", b)], b)):
    a_, b_ = ("spec", b), ("build", b)
    print(f"| {b} | {', '.join(S.P[b]) or 'dClosedLoop'} | {S.U[b]} | {ls[b]-es[b]} | {where[a_]} | {start[a_]:.0f}-{fin[a_]:.0f} | {where[b_]} | {start[b_]:.0f}-{fin[b_]:.0f} |")
for n in sp:
    busy = sum(fin[t] - start[t] for t in T if where[t] == n)
    print(f"node {n}: busy {busy:.0f} of {mk:.0f} ({100*busy/mk:.0f}%), phases {sum(1 for t in T if where[t]==n)}")
print("first wave (start 0 or at dTrueNorth's landing):")
tn = fin[("build", "dTrueNorth")]
for t in sorted(T, key=lambda t: start[t]):
    if start[t] <= tn + 1e-9: print(f"  {t[0]} {t[1]} on {where[t]} {start[t]:.0f}-{fin[t]:.0f}")
print(f"dTrueNorth lands at {tn:.0f}")
print("sync points: at each landing, the phases in flight on any node")
for b in sorted(S.order, key=lambda b: fin[("build", b)]):
    L = fin[("build", b)]
    infl = [f"{k[0]}:{k[1]}@{where[k]}" for k in T if start[k] < L - 1e-9 < fin[k] - 2e-9 and k != ("build", b)]
    print(f"  {L:6.0f} {b} lands; in flight: {', '.join(infl) or 'none'}")
```

### `d217/schedule.py` (5028 bytes)

```python
"""Per-node schedule for the dClosedLoop chain, derived from v2 [chain] (read-only).
Usage: python schedule.py <worktree root> [--s 0.33] [--b 0.5] [--table]
A build's units = its planned-units cell split on "; " (as critical-path.py counts), checked against its cl- ids.
Each build = a spec phase (s*U) and a build phase ((1-s)*U), in reference-node units.
Policies (precedence for spec(X), X != dTrueNorth):
  A  whole: spec(X) after every parent's build lands (spec and build back to back)
  B  ahead: spec(X) after dTrueNorth lands, never waiting on parents
  C  confirmed: spec(X) after every parent's spec closes (the parent's design exit)
build(X) always after spec(X) and every parent's build (landed). One phase at a time per node.
Node speeds: a=1, d=1, b=--b. Affinity: same = build on the node that specced it; any = free.
"""
import re, sys, itertools, heapq
root = sys.argv[1]
args = dict(zip(sys.argv[2::2], sys.argv[3::2])) if len(sys.argv) > 2 else {}
V = root + "/memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
text = open(V, encoding="utf-8").read()
chain = text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
names = re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)
U, P, STAGE, IDS = {}, {}, {}, {}
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| ([^|]+) \| ([^|]+) \| (.+) \| [^|]+ \|$", ln)
    if m:
        b = m.group(1); STAGE[b] = m.group(2).strip()
        U[b] = len([u for u in m.group(4).split("; ") if u.strip()])
        IDS[b] = re.findall(r"`(cl-dClosedLoop-\d{4})`", m.group(4))
        P[b] = [p.strip() for p in m.group(3).split(",") if p.strip() in names]
assert len(U) == 22 and sum(U.values()) == 509, (len(U), sum(U.values()))
assert all(U[b] == len(IDS[b]) for b in U)
ROOT = "dTrueNorth"
order = []  # topological
seen = set()
def topo(b):
    if b in seen: return
    for p in P[b]: topo(p)
    seen.add(b); order.append(b)
for b in names: topo(b)

def unbounded():
    es, ef = {}, {}
    for b in order:
        es[b] = max([ef[p] for p in P[b]], default=0); ef[b] = es[b] + U[b]
    mk = max(ef.values()); lf, ls = {}, {}
    kids = {b: [c for c in names if b in P[c]] for b in names}
    for b in reversed(order):
        lf[b] = min([ls[c] for c in kids[b]], default=mk); ls[b] = lf[b] - U[b]
    return es, ef, ls, lf, mk, kids

def tasks(s, pol):
    """task -> (work, preds)"""
    T = {}
    for b in order:
        sp, bd = ("spec", b), ("build", b)
        if b == ROOT: spre = []
        elif pol == "A": spre = [("build", p) for p in P[b]] + [("build", ROOT)]
        elif pol == "B": spre = [("build", ROOT)]
        else: spre = [("spec", p) for p in P[b]] + [("build", ROOT)]
        T[sp] = (s * U[b], sorted(set(spre)))
        T[bd] = (U[b] - s * U[b], [sp] + [("build", p) for p in P[b]])
    return T

def bottom(T):
    succ = {t: [] for t in T}
    for t, (w, pre) in T.items():
        for q in pre: succ[q].append(t)
    bl = {}
    def f(t):
        if t not in bl: bl[t] = T[t][0] + max([f(c) for c in succ[t]], default=0)
        return bl[t]
    for t in T: f(t)
    return bl

def simulate(s, pol, speeds, affinity="same", pin=None):
    """List scheduling: when a node frees, it takes the ready task of largest bottom level it may run.
    pin: build -> node (static assignment of both phases)."""
    T = tasks(s, pol); bl = bottom(T)
    done, start, fin, where = {}, {}, {}, {}
    free = {n: 0.0 for n in speeds}
    t_now = 0.0; remaining = set(T)
    while remaining:
        ready = [t for t in remaining if all(q in fin for q in T[t][1])]
        # earliest each ready task could start = max pred finish
        best = None
        for n in sorted(free, key=lambda n: (free[n], n)):
            for t in sorted(ready, key=lambda t: -bl[t]):
                kind, b = t
                if pin and pin[b] != n: continue
                if affinity == "same" and kind == "build" and where.get(("spec", b), n) != n: continue
                rt = max([fin[q] for q in T[t][1]], default=0.0)
                st = max(rt, free[n]); ft = st + T[t][0] / speeds[n]
                key = (st, -bl[t], ft)
                if best is None or key < best[0]: best = (key, t, n, st, ft)
        if best is None:
            raise SystemExit("deadlock")
        _, t, n, st, ft = best
        start[t], fin[t], where[t] = st, ft, n
        free[n] = ft; remaining.discard(t)
    return max(fin.values()), start, fin, where

if __name__ == "__main__":
    es, ef, ls, lf, mk, kids = unbounded()
    print(f"builds {len(U)}, units {sum(U.values())}, critical path {mk}")
    crit = [b for b in order if es[b] == ls[b]]
    print("critical:", " > ".join(crit))
    print("| Build | Stage | Parents | Units | ES | EF | LS | Slack | Children |")
    print("|---|---|---|---|---|---|---|---|---|")
    for b in sorted(order, key=lambda b: (es[b], b)):
        print(f"| {b} | {STAGE[b]} | {', '.join(P[b]) or 'dClosedLoop'} | {U[b]} | {es[b]} | {ef[b]} | {ls[b]} | {ls[b]-es[b]} | {len(kids[b])} |")
```

### `d217/stale.py` (2435 bytes)

```python
"""Makespan vs staleness. Adds policy J (just in time): spec(X) after dTrueNorth lands, every parent's spec closes,
and every grandparent lands, so a spec is written while only its parents are in flight. Staleness of X = landings
between spec(X)'s end and build(X)'s start of builds whose clauses change a surface the chain's own executors use
(driver, lander, charter, spec format, method, roles, bar), counted from surfaces.py's patterns."""
import sys, re, importlib.util
here, root = sys.argv[1], sys.argv[2]
sys.argv = [here + "/heft.py", here, root]
spec = importlib.util.spec_from_file_location("heft", here + "/heft.py"); H = importlib.util.module_from_spec(spec); spec.loader.exec_module(H)
S = H.S
orig = S.tasks
def tasks(s, pol):
    if pol != "J": return orig(s, pol)
    T = orig(s, "C")
    for b in S.order:
        if b == S.ROOT: continue
        w, pre = T[("spec", b)]
        gp = {g for p in S.P[b] for g in S.P[p]}
        T[("spec", b)] = (w, sorted(set(pre) | {("build", g) for g in gp}))
    return T
S.tasks = tasks
V = root + "/memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
chain = open(V, encoding="utf-8").read().split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
RX = r"unattended|run claims?|--plan|--status|push-main|lander\b|landing record|pre-push|charter|\*\*Carries:\*\*|specs? frozen|derived READY|spec tokens|build method|per-pass checklist|handoff\.py|work order|merge bar|run-gates|verdict"
SURF = set()
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| [^|]+ \| (.+) \| [^|]+ \|$", ln)
    if m and re.search(RX, m.group(2)): SURF.add(m.group(1))
full = {"spec", "build"}
for bs in (0.25, 0.5):
  for s in (0.2, 0.33, 0.5):
    out = []
    for pol in "ACJ":
      for bro in ("b-full", "b-spec"):
        sp = {"a": 1.0, "d": 1.0, "b": bs}
        roles = {"a": full, "d": full, "b": full if bro == "b-full" else {"spec"}}
        mk, start, fin, where, T = H.heft(s, pol, sp, roles)
        lands = {b: fin[("build", b)] for b in S.order}
        st = [sum(1 for o in SURF if o != b and fin[("spec", b)] <= lands[o] <= start[("build", b)]) for b in S.order]
        bu = sum(fin[t]-start[t] for t in T if where[t] == "b")
        out.append(f"{pol}/{bro}: mk {mk:.0f} stale {sum(st)} max {max(st)} b% {100*bu/mk:.0f}")
    print(f"b={bs} s={s}: " + " | ".join(out))
print("surface-changing builds:", len(SURF), sorted(SURF))
```

### `d217/surfaces.py` (1504 bytes)

```python
"""Which chain builds' clauses touch a surface the executing nodes run on. Read-only over v2 [chain]."""
import re, sys
root = sys.argv[1]
V = root + "/memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
chain = open(V, encoding="utf-8").read().split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
SURF = {
 "driver":   r"unattended|run claims?|--plan|--status|`next`|resume tick",
 "lander":   r"push-main|lander\b|landing record|pre-push",
 "charter":  r"charter|AGENTS\.md",
 "specfmt":  r"\*\*Carries:\*\*|TEMPLATE-SPEC|spec template|specs? frozen|derived READY|spec tokens",
 "method":   r"build method|BUILD-METHOD|per-pass checklist",
 "roles":    r"handoff\.py|\.claude/agents|work order|role agents?|the roster",
 "install":  r"upgrade step|`update`|govkit|adopt|install",
 "bar":      r"merge bar|gate-legs|run-gates|the bar\b|verdict",
 "policy":   r"policy\.toml|\.unattended\.conf|\.agent-cap\.conf",
 "hooks":    r"\bhooks?\b|PreToolUse|SessionStart",
}
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| [^|]+ \| (.+) \| [^|]+ \|$", ln)
    if not m: continue
    b, cell = m.group(1), m.group(2)
    clauses = [c for c in cell.split("; ") if c.strip()]
    hits = []
    for k, rx in SURF.items():
        ids = [re.search(r"`cl-dClosedLoop-(\d{4})`\s*$", c).group(1) for c in clauses if re.search(rx, c)]
        if ids: hits.append(f"{k}:{len(ids)}({','.join(ids[:4])}{'..' if len(ids)>4 else ''})")
    print(b, " ".join(hits))
```

## [d218]

Dispatch 218, specs held to the design: mkspecs.py writes a clean dTrueNorth spec set into a `--shared` clone, plant.py plants each wrong carry and undeclared departure, run.sh runs both joins and prints their exits.

### `d218/mkspecs.py` (1534 bytes)

```python
# Writes two dTrueNorth specs into the CURRENT directory's tree (the scratch clone), carrying cl-0001..0006.
import importlib.util, sys
from pathlib import Path
B = "memory/builds/dClosedLoop/build/"
s = importlib.util.spec_from_file_location("carries", B + "2026-10-19-build-PLAY-dClosedLoop-1-carries.py")
c = importlib.util.module_from_spec(s); s.loader.exec_module(c)
builds, nodes, retired = c.design()
tn = builds["dTrueNorth"]
def spec(n, ids, extra=""):
    lines = [f"# PLAY-dTrueNorth-{n} — probe unit {n}", "",
             f"**Status:** OPEN · rev-1 · 2026-10-21 · node d · Tier-2 · base 4592ab00 · streams playbook", ""]
    for i in ids:
        lines += [f"**Carries:** {i}@{tn[i][1]} whole"]
    lines += (["**Carries:** node:record-kind.deviation"] if n == 2 else []) + ["", "## 5. Acceptance criteria", ""]
    for i in ids:
        lines += [f"- AC for {i}: " + tn[i][0].replace("AMENDED", "amended-ledger")]
    return "\n".join(lines) + "\n" + extra
d = Path("memory/builds/dTrueNorth/spec"); d.mkdir(parents=True, exist_ok=True)
(d / "2026-10-21-spec-missing:PLAY-dTrueNorth-1.md").write_text(spec(1, ["cl-dClosedLoop-0001", "cl-dClosedLoop-0002", "cl-dClosedLoop-0003"]), encoding="utf-8", newline="\n")
(d / "2026-10-21-spec-missing:PLAY-dTrueNorth-2.md").write_text(spec(2, ["cl-dClosedLoop-0004", "cl-dClosedLoop-0005", "cl-dClosedLoop-0006"]), encoding="utf-8", newline="\n")
if "--hash" in sys.argv:
    for b in ("dTrueNorth", "dGroundRules"):
        for i in sorted(builds[b])[:2]: print(b, i, builds[b][i][1])
```

### `d218/plant.py` (2387 bytes)

```python
# Edits the scratch clone (cwd) for one plant step. Usage: plant.py <step>
import re, sys
from pathlib import Path
S1 = Path("memory/builds/dTrueNorth/spec/2026-10-21-spec-missing:PLAY-dTrueNorth-1.md")
S2 = Path("memory/builds/dTrueNorth/spec/2026-10-21-spec-missing:PLAY-dTrueNorth-2.md")
V2 = Path("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
R = lambda p: p.read_text(encoding="utf-8")
W = lambda p, t: p.write_text(t, encoding="utf-8", newline="\n")
step = sys.argv[1]
if step == "stale":
    W(S1, R(S1).replace("cl-dClosedLoop-0002@6acd9ea9", "cl-dClosedLoop-0002@6acd9ea8"))
elif step == "crossbuild":
    t = R(S2).replace("**Carries:** node:record-kind.deviation", "**Carries:** node:record-kind.deviation\n**Carries:** cl-dClosedLoop-0007@b0458b78 whole")
    W(S2, t)
elif step == "semantic":
    t = R(S2) + "- AC-X: a loosening deviation is approved by its author alone; the owner is never asked.\n"
    W(S2, t)
elif step == "part":
    W(S1, re.sub(r"(cl-dClosedLoop-0003@[0-9a-f]{8}) whole", r"\1 part 1/2", R(S1)))
elif step == "drop":
    W(S1, "\n".join(l for l in R(S1).split("\n") if not l.startswith("**Carries:** cl-dClosedLoop-0003")))
elif step == "typo":
    W(S1, R(S1).replace("probe unit 1", "probe unit one"))
elif step == "acrevise":
    W(S1, R(S1).replace("- AC for cl-dClosedLoop-0001:", "- AC for cl-dClosedLoop-0001 (narrowed, the malformed-line red case dropped):"))
elif step == "status":
    W(S1, R(S1).replace("**Status:** OPEN", "**Status:** INPROGRESS"))
elif step == "code":
    p = Path("tools/probe-x.txt"); W(p, "built\n")
elif step == "v2edit":
    t = R(V2); i = t.index("`cl-dClosedLoop-0002`"); W(V2, t[:i] + "and a quiet edit " + t[i:])
elif step.startswith("record:"):
    _, rev, risk, approver = step.split(":")
    d = Path("memory/builds/dTrueNorth/build"); d.mkdir(parents=True, exist_ok=True)
    W(d / "2026-10-21-build-missing:PLAY-dTrueNorth-1-deviation-1.md", "\n".join([
        "# missing:PLAY-dTrueNorth-1 deviation 1", "",
        f"- **Departs from:** missing:PLAY-dTrueNorth-1@rev-{rev} [acceptance]",
        "- **Hand-off:** spec-revised", "- **Before:** the malformed-line red case", "- **After:** dropped",
        "- **Cause:** builder discovery", "- **Reason:** probe", "- **Evidence:** probe",
        f"- **Risk:** {risk}", f"- **Approver:** {approver}", "- **Follow-through:** gap gap-design-13", ""]))
```

### `d218/run.sh` (518 bytes)

```bash
# Usage: run.sh <label> ; runs both joins in the scratch clone and prints exits and findings.
B=memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1
export PYTHONDONTWRITEBYTECODE=1
c=$(python -B $B-carries.py --build dTrueNorth); ce=$?
cx=$(python -B $B-carries.py --build dTrueNorth --exit); cxe=$?
d=$(python -B $B-deviations.py); de=$?
echo "## $1: carries=$ce carries--exit=$cxe deviations=$de"
printf '%s\n%s\n%s\n' "$c" "$cx" "$d" | grep -E "^  " | grep -v "not read yet" | sort -u | cut -c1-200
```

## [verified]

The main loop's checks, 2026-10-20, of two claims the returns leave open.

**1. Today's merge bar is blind to a stale design pin (dispatch 218 asked for it).** A `--shared` clone of this
worktree at `bf163426c`, in the main loop's scratch folder `exec/v218/`. One planted spec, staged, so the tracked-file
readers see it: `memory/builds/dTrueNorth/spec/2026-10-20-spec-missing:PLAY-dTrueNorth-1-probe.md`, status OPEN, carrying
`cl-dClosedLoop-0001@00000000 whole`, a pin no clause text hashes to.

- Arm 1, the control: the spec also cites `AGENTS.md:99999` in an acceptance bullet and names a gate that is no leg.
  `python -X utf8 tools/check-spec-tokens.py` exits 1 and names the planted file twice:
  `[leg] hygiene — not a name in tools/gate-legs.json` and `[cite] AGENTS.md:99999 — file has 177 lines`. So the
  leg reads the planted spec.
- Arm 2, the stale pin alone: the control lines removed, the file restaged. `check-spec-tokens.py` exits 0 and names
  the planted file in none of its lines. Over the same tree, the bootstrap instrument
  `2026-10-19-build-PLAY-dClosedLoop-1-carries.py --build dTrueNorth` exits 1:
  `pins cl-dClosedLoop-0001@00000000, and the clause's text now hashes 83b6b117 (a stale pin)`, with four token
  findings beside it.

So the merge bar as it stands passes a spec whose pin no longer matches its clause, and only the bootstrap
instrument, which nothing runs, reds it.

**2. A README the owner landed on main lets a `slug` run take `spec-audit:` and `may:` (dispatch 214's candidate A).**
Read, not run. `resolve_base` sets the anchor kind to `default-branch` whenever the README resolves at the merge-base
of the advertised default-branch tip and HEAD, before the local anchor is tried (`tools/unattended/unattended.sh`
line 2655, inside `resolve_base` at line 2647). Fail 89 refuses `spec-audit:` only when the mode is not `slug` (the test at line 4108, the fail at 4113) or the
anchor is `local` (line 4122, the fail at 4125), and fail 78 refuses `may:` on the same two conditions (lines 4160
and 4166, the fails at 4161 and 4167). A run
started from a fresh worktree off `origin/main`, on a build whose README `origin/main` holds, therefore reads both. No
run has done it yet (dispatch 214), so the first chain run is the test.
