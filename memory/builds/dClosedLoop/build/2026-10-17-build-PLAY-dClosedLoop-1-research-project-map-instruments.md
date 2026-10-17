# Research instruments: the level-0 project map, runs A and B

**Serves:** research PLAY-dClosedLoop-1

Each run's files and shell commands, taken in order from its transcript, so nothing is retyped. Both
runs shared the session scratch directory, and run A reports that run B overwrote two of its scripts
mid-run, so a file there may hold the other run's content; these are what each run sent. The returns
are `build/2026-10-17-build-PLAY-dClosedLoop-1-research-project-map-a.md` and `-b.md`.

## [run-a] Run A, dispatch 87

1. Bash

````text
ls memory/builds/dClosedLoop/build/ | head -80 && wc -c memory/builds/dClosedLoop/build/*project-map* memory/builds/dClosedLoop/build/*atlas*
````

2. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && for f in *layer-memory.md *systems*.md *orientation.md *layer-roles.md *architecture-v2.md; do echo "== $f $(wc -c <$f)"; grep -n '^## \[\|^### \[' $f | head -60; done; ls | grep -i system
````

3. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n 'P27' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | head; sed -n 1074,1100p 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md
````

4. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n 538,545p 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md; echo ====; awk 'NR>=1076 && NR<=1100' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | cut -c1-400; echo; grep -n 'dTotalRecall |' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | cut -c1-60
````

5. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -o '.\{120\}\(project map\|project-map\|level-0 map\|whole view\).\{120\}' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md 2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md | head; echo ===; grep -n 'gap-mem-[0-9]* \|gap-orient-[0-9]* ' 2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md | cut -c1-260
````

6. Bash

````text
ls tools/codebase-map/ tools/memory-tree/ | head -80; wc -c tools/codebase-map/*.py tools/memory-tree/gen_build_index.py memory/map/generated/* memory/LIVE.md; ls tools | wc -l; ls tools
````

7. Bash

````text
sed -n 1,80p tools/codebase-map/gen_map.py; head -c 2500 memory/map/generated/MAP.md; echo; echo ====; head -c 1500 memory/map/generated/CARDS.md
````

8. Bash

````text
python -c "
import json;d=json.load(open('memory/map/generated/inventories.json',encoding='utf-8'));print(type(d), list(d)[:20] if isinstance(d,dict) else len(d))
for k,v in (d.items() if isinstance(d,dict) else []):
  print(k, type(v).__name__, (len(v) if hasattr(v,'__len__') else v), str(v)[:200])
"; ls tools/*/kit.toml | wc -l; grep -n 'def inventory_ids\|^def \|INVENTOR' tools/codebase-map/map_extractors.py | head -40
````

9. Bash

````text
sed -n 82,110p tools/codebase-map/map_extractors.py; sed -n 405,460p tools/codebase-map/map_extractors.py; python -c "
import json;d=json.load(open('memory/map/generated/inventories.json',encoding='utf-8'))['inventories'];print(d['kits'])"; ls -d tools/*/ | wc -l; for d in tools/*/; do [ -f $d/kit.toml ] || echo "nokit $d"; done
````

10. Bash

````text
for f in tools/*/kit.toml; do echo "$f: $(grep -m1 -E '^(description|summary|purpose|title) *=' $f | cut -c1-140)"; done; echo; head -30 tools/roles/kit.toml
````

11. Bash

````text
ls tools/govkit; grep -rn -i 'summary\|description\|purpose' tools/govkit/*.toml 2>/dev/null | head; for d in tools/*/; do f=$d/README.md; [ -f $f ] && echo "$d: $(grep -m1 -v '^\s*$\|^#\|^<!--' $f | cut -c1-110)" || echo "$d: NO README"; done
````

12. Bash

````text
head -40 tools/govkit/registry.toml; ls tools/govkit/entries | head; grep -c '^\[\[' tools/govkit/registry.toml
````

13. Bash

````text
sed -n 1,60p tools/memory-tree/gen_build_index.py; grep -n 'add_argument\|--check\|--write' tools/memory-tree/gen_build_index.py | head -30; head -12 memory/LIVE.md
````

14. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory && ls builds | wc -l; sed -n 1,30p builds/aOrientedCast/README.md | cut -c1-200; grep -n 'description' ../tools/memory-tree/gen_build_index.py | head -15
````

15. Bash

````text
python -c "
import json;d=json.load(open('tools/gate-legs.json',encoding='utf-8'));print(type(d).__name__, list(d)[:5] if isinstance(d,dict) else '')
legs=d['legs'] if isinstance(d,dict) and 'legs' in d else d
print(len(legs)); print(json.dumps(legs[0])[:500]); print(sorted({k for l in legs for k in l}))
"; ls memory/gotchas | head -5; ls memory/gotchas | wc -l; head -8 memory/gotchas/$(ls memory/gotchas | grep -v README | head -1); ls tools/roles/ | head -40
````

16. Bash

````text
head -12 memory/gotchas/a-grep-for-a-word-is-a-presence-probe.md | cut -c1-200; ls tools/roles/agents; head -6 tools/roles/agents/$(ls tools/roles/agents | head -1) | cut -c1-250; python -c "
import json;d=json.load(open('.claude/settings.json',encoding='utf-8'));h=d.get('hooks',{})
for ev,arr in h.items():
  for m in arr:
    for x in m.get('hooks',[]): print(ev, m.get('matcher',''), x.get('command','')[:100])
"; ls .githooks skills .claude/skills 2>&1 | head -30
````

17. Bash

````text
wc -c memory/DECISIONS.md; grep -c '^| ' memory/DECISIONS.md; grep -m3 '^| [A-Z]' memory/DECISIONS.md | cut -c1-250; git ls-files memory/builds | sed -E 's#.*/[0-9]{4}-[0-9]{2}-[0-9]{2}-([a-z]+)-.*#\1#;t;d' | sort | uniq -c | sort -rn | head -20; ls memory
````

18. Bash

````text
sed -n 1,30p memory/DECISIONS.md | cut -c1-220; grep -c '^- ' memory/DECISIONS.md; grep -cE '^(- |### |## )' memory/DECISIONS.md
````

19. Bash

````text
ls memory/map memory/map/features | head -50; ls memory/guides memory/backlog memory/project; sed -n 1,25p memory/map/features/agent-cap.md
````

20. Bash

````text
mkdir -p "/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad" && cat > "/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/census.py" <<'EOF'
"""Census of every node class a level-0 map must hold: count, bytes at one line per node
(`- <ns>.<name> — <purpose cut at 100>`), and the share of nodes with a declared purpose today."""
import collections, glob, json, os, re, subprocess, sys, tomllib
B = "memory/builds/dClosedLoop/build/"
rd = lambda p: open(p, encoding="utf-8").read()
V = rd(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
G = rd(B + "2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md")
R = rd(B + "2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md")
RT = rd(B + "2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md")
def section(t, tag):
    m = re.search(r"^##+ \[" + re.escape(tag) + r"\].*?(?=^##+ \[|\Z)", t, re.M | re.S); return m.group(0) if m else ""
def cut(s, n=100):
    s = re.sub(r"\s+", " ", s or "").strip(); return s if len(s) <= n else s[:n-1] + "…"
rows = collections.OrderedDict()
def add(cls, name, purpose, src):
    rows.setdefault(cls, {"n": [], "src": src})
    line = f"- {cls}.{name}" + (f" — {cut(purpose)}" if purpose else "")
    rows[cls]["n"].append((line, bool(purpose)))
for m in re.finditer(r"^\| `([a-z]+)` \| (core|expansion) \| (.+?) \|$", section(V, "layers"), re.M): add("layer", m[1], m[3], "v2 [layers] table")
for m in re.finditer(r"^- \*\*(P\d+) ([^*]+?)\*\*", V, re.M): add("principle", m[1], m[2], "v2 [principles] bold title")
for ln in section(V, "chain").splitlines():
    if ln.startswith("| d"):
        c = [x.strip() for x in ln.strip("|").split(" | ")]; add("chain", c[0], c[1], "v2 [chain] Stage cell only (units cell is 1-4 KB)")
for m in re.finditer(r"^\| (`[a-z]+\.[a-z0-9.-]+`) \| [^|]*\| [^|]*\| ([^|]*)\|", section(V, "policies"), re.M): add("policy", m[1].strip("`"), m[2], "v2 [policies] why column")
for m in re.finditer(r"^\| (gap-[a-z]+-\d+) \| [^|]+\| [A-Z]+ \| ([^|]+)\|", G, re.M): add("gap", m[1], m[2], "register row text (first sentence)")
for rp in sorted(glob.glob("memory/builds/*/README.md")):
    t = rd(rp); h = re.search(r"^# \S+ — (.+)$", t, re.M); add("build", rp.split("/")[2], h[1] if h else "", "README H1 after the slug")
for p in sorted(glob.glob("memory/map/features/*.md")):
    t = rd(p); m = re.search(r'^title = "(.*)"', t, re.M); add("feature", os.path.basename(p)[:-3], m[1] if m else "", "dossier toml title")
for d in sorted(x for x in os.listdir("tools") if os.path.isdir("tools/" + x) and x != "__pycache__"): add("kit", d, "", "none: kit.toml has no purpose field")
for e in sorted(glob.glob("tools/govkit/entries/*.kit.toml")): add("kit-entry", os.path.basename(e)[:-9], "", "none: govkit entry has no purpose field")
for l in json.load(open("tools/gate-legs.json", encoding="utf-8")): add("leg", l["name"], "", "none: gate-legs.json has name, argv, reads; the name is free text")
s = json.load(open(".claude/settings.json", encoding="utf-8"))
for ev, arr in s["hooks"].items():
    for m in arr:
        for x in m["hooks"]: add("hook", ev + ":" + re.sub(r'.*/', '', x["command"].split('"')[-2] if '"' in x["command"] else x["command"]), "", "none: settings.json carries no description")
for g in ("commit-msg", "pre-commit", "pre-push", "pre-rebase"): add("githook", g, "", "none")
for p in sorted(glob.glob(".claude/skills/*/SKILL.md") + glob.glob("skills/*/SKILL.md")):
    m = re.search(r"^description: (.*)$", rd(p), re.M); add("skill", p.split("/")[-2], m[1] if m else "", "SKILL.md front-matter description")
for p in sorted(glob.glob("tools/roles/agents/*.agent.md")):
    m = re.search(r"^description: (.*)$", rd(p), re.M); add("role", os.path.basename(p)[:-9], m[1] if m else "", "agent front-matter description")
for p in sorted(glob.glob("memory/gotchas/*.md")):
    if os.path.basename(p) in ("README.md", "INDEX.md"): continue
    m = re.search(r"^description: (.*)$", rd(p), re.M); add("class", os.path.basename(p)[:-3], m[1] if m else "", "gotcha front-matter description")
for m in re.finditer(r"^- (?:\*\*)?([A-Z]+-[A-Za-z]+-\d+)(?:\*\*)? (?:·|—) (?:\*\*)?(.+)$", rd("memory/DECISIONS.md"), re.M): add("decision", m[1], m[2], "DECISIONS.md row (no major/minor field)")
for p in sorted(glob.glob("memory/guides/*.md")):
    t = rd(p); h = re.search(r"^# (.+)$", t, re.M); add("guide", os.path.basename(p)[:-3], h[1] if h else "", "guide H1")
items = sorted(set(re.findall(r"`((?:entry|plan|design|build|test|deploy|review|life|adopt)\.[a-z-]+)`", section(R, "matrix"))))
for i in items: add("item", i, "", "flow-steps item row (designed, not built)")
for m in re.finditer(r"^\| ([a-z]+(?: [a-z]+)*) \| (core|distribution, integrations|observability) \| (.+?) \|$", section(R, "roster"), re.M): add("role-designed", m[1].replace(" ", "-"), m[3], "layer-roles [roster] (designed)")
for m in re.finditer(r"^\| ([a-z]+ [a-z]+|[a-z]+) \| ([^|]+) \| ([^|]+) \|$", section(RT, "extend"), re.M):
    if m[1] not in ("Extension point",): add("point", m[1].replace(" ", "-"), m[2], "layer-runtime [extend] (designed)")
own = re.findall(r"`([a-z]+)`", section(rd(B + "2026-10-16-build-PLAY-dClosedLoop-1-systems.md"), "design-tags").split("**Owners.**")[1].split("**Keys.**")[0])
for n in sorted(set(own)): add("namespace", n, "", "systems [design-tags] Owners (designed)")
for p in sorted(glob.glob(B + "*.md")): add("record", os.path.basename(p)[len("2026-10-14-build-PLAY-dClosedLoop-1-"):-3], "", "this build's design records")
tot = 0; totn = 0
print(f"{'class':14}{'n':>5}{'bytes':>8}{'purpose%':>9}  purpose source")
for c, d in rows.items():
    b = sum(len(l.encode()) + 1 for l, _ in d["n"]); n = len(d["n"]); p = sum(h for _, h in d["n"])
    tot += b; totn += n; print(f"{c:14}{n:5}{b:8}{100*p//max(n,1):8}%  {d['src']}")
print(f"{'all':14}{totn:5}{tot:8}")
if "--print" in sys.argv:
    for c in sys.argv[2:]: print("\n".join(l for l, _ in rows[c]["n"]))
EOF
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python "/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/census.py"
````

21. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; sed -i 's/^import collections, glob/import collections, glob as _g/; s/^B = /class glob:\n    glob = staticmethod(lambda p: [x.replace(chr(92), "\/") for x in _g.glob(p)])\nB = /' $S/census.py && cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python $S/census.py
````

22. Bash

````text
ls -d ~/.claude/projects/C--projects-coding-governance* | head; for d in ~/.claude/projects/C--projects-coding-governance*; do find "$d" -path '*subagents*' -name '*.jsonl' 2>/dev/null; done | wc -l; for d in ~/.claude/projects/C--projects-coding-governance*; do find "$d" -path '*subagents*' -name '*.jsonl' 2>/dev/null; done | head -3
````

23. Bash

````text
f=$(for d in ~/.claude/projects/C--projects-coding-governance*; do find "$d" -path '*subagents*' -name '*.jsonl' 2>/dev/null; done | head -1); ls $(dirname $f) | head; head -c 1500 $f; echo; python -c "
import json,sys
for i,l in enumerate(open(sys.argv[1],encoding='utf-8')):
  d=json.loads(l); print(i, d.get('type'), list(d)[:15]);
  if i>4: break" $f
````

24. Bash

````text
cd ~/.claude/projects && cat $(ls -d C--projects-coding-governance*/ | head -1)*/subagents/workflows/*/*.meta.json 2>/dev/null | head -c 600; echo; for d in C--projects-coding-governance*; do find "$d" -path '*subagents*' -name '*.meta.json'; done | xargs cat 2>/dev/null | python -c "
import sys,json,re,collections
c=collections.Counter()
for m in re.finditer(r'\"agentType\":\s*\"([^\"]+)\"', sys.stdin.read()): c[m[1]]+=1
print(c.most_common(30))"
````

25. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cat > $S/orient.py <<'EOF'
"""Per subagent role: calls, bytes returned and distinct files read before the first act, and the share
of calls that ask whether something exists. Act = first Write/Edit/MultiEdit/NotebookEdit (writer roles),
else the whole run (read-only roles). Existence probe = Glob; Grep in files_with_matches/count mode; a
shell command whose first verb is ls/find/test or that runs `git ls-files`, `grep -l`, `grep -c`, `rg -l`."""
import glob, json, os, re, statistics as st, collections, sys
home = os.path.expanduser("~/.claude/projects")
files = [f for d in glob.glob(home + "/C--projects-coding-governance*") for f in glob.glob(d + "/**/subagents/**/*.jsonl", recursive=True)]
WR = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
EXIST = re.compile(r"(^|[;&|]\s*|\bcd [^;&]*&&\s*)(ls|find|test)\b|git ls-files|grep -[a-zA-Z]*[lc]\b|rg -[a-zA-Z]*l\b|\[ -[ef] ")
def role_of(f, first):
    m = re.search(r"gov:handoff role=([\w-]+)", first)
    if m: return m[1]
    try: return json.load(open(f[:-6] + ".meta.json", encoding="utf-8")).get("agentType", "?")
    except Exception: return "?"
agg = collections.defaultdict(list)
for f in files:
    try: L = [json.loads(l) for l in open(f, encoding="utf-8")]
    except Exception: continue
    first = next((json.dumps(x["message"]["content"]) if not isinstance(x["message"]["content"], str) else x["message"]["content"] for x in L if x.get("type") == "user"), "")
    r = role_of(f, first)
    res = {}
    for x in L:
        if x.get("type") == "user" and isinstance(x["message"]["content"], list):
            for c in x["message"]["content"]:
                if c.get("type") == "tool_result":
                    v = c.get("content"); res[c["tool_use_id"]] = len(json.dumps(v) if not isinstance(v, str) else v)
    calls = reads = byts = exist = 0; fs = set(); acted = False
    for x in L:
        if x.get("type") != "assistant": continue
        for c in x["message"].get("content", []):
            if c.get("type") != "tool_use": continue
            n, i = c["name"], c.get("input", {})
            if n in WR: acted = True; break
            calls += 1; byts += res.get(c["id"], 0)
            if n == "Read": reads += 1; fs.add(i.get("file_path", "").replace("\\", "/").lower())
            if n == "Glob" or (n == "Grep" and i.get("output_mode", "files_with_matches") in ("files_with_matches", "count")) or (n in ("Bash", "PowerShell") and EXIST.search(i.get("command", ""))): exist += 1
        if acted: break
    agg[r].append((calls, reads, len(fs), byts, exist, acted, len(first)))
med = lambda v: st.median(v) if v else 0
print(f"{'role':22}{'n':>5}{'calls':>7}{'reads':>6}{'files':>6}{'KB ret':>8}{'brief KB':>9}{'exist':>6}{'exist%':>7}{'acted':>6}")
for r, v in sorted(agg.items(), key=lambda kv: -len(kv[1])):
    if len(v) < 5: continue
    tc = sum(x[0] for x in v); te = sum(x[4] for x in v)
    print(f"{r:22}{len(v):5}{med([x[0] for x in v]):7}{med([x[1] for x in v]):6}{med([x[2] for x in v]):6}{med([x[3] for x in v])/1000:8.1f}{med([x[6] for x in v])/1000:9.1f}{med([x[4] for x in v]):6}{100*te/max(tc,1):6.1f}%{sum(x[5] for x in v):6}")
EOF
python $S/orient.py
````

26. Bash

````text
cd ~/.claude/projects && for d in C--projects-coding-governance*; do find "$d" -path '*subagents*' -name '*.jsonl'; done > /tmp/sa_list.txt 2>/dev/null || true; python - <<'EOF'
import json,re,collections,os
home=os.path.expanduser("~/.claude/projects")
c=collections.Counter()
for f in open('/tmp/sa_list.txt',encoding='utf-8').read().split('\n'):
    if not f: continue
    try: m=json.load(open(os.path.join(home,f[:-6]+'.meta.json'),encoding='utf-8'))
    except Exception: continue
    if m.get('agentType')!='workflow-subagent': continue
    l=json.loads(open(os.path.join(home,f),encoding='utf-8').readline())
    t=l['message']['content']; t=t if isinstance(t,str) else json.dumps(t)
    c[re.sub(r'\s+',' ',t[:70])]+=1
for k,v in c.most_common(25): print(v,k)
EOF
````

27. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cat > $S/wfgroups.py <<'EOF'
import json,re,collections,os,glob
home=os.path.expanduser("~/.claude/projects")
c=collections.Counter()
for f in [f for d in glob.glob(home+"/C--projects-coding-governance*") for f in glob.glob(d+"/**/subagents/**/*.jsonl",recursive=True)]:
    try: m=json.load(open(f[:-6]+'.meta.json',encoding='utf-8'))
    except Exception: continue
    if m.get('agentType')!='workflow-subagent': continue
    l=json.loads(open(f,encoding='utf-8').readline())
    t=l['message']['content']; t=t if isinstance(t,str) else json.dumps(t)
    k=re.search(r'(reuse scout|orient\w*|coherence|lens[: ]+\w+|You are (?:an? )?[\w -]{3,30})',t[:3000],re.I)
    c[k[0].lower()[:40] if k else re.sub(r'\s+',' ',t[:50])]+=1
for k,v in c.most_common(30): print(v,k)
EOF
python $S/wfgroups.py
````

28. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; python - "$S" <<'EOF'
import sys,re
S=sys.argv[1]; t=open(S+"/orient.py",encoding="utf-8").read()
t=t.replace('''    m = re.search(r"gov:handoff role=([\\w-]+)", first)
    if m: return m[1]''','''    m = re.search(r"gov:handoff role=([\\w-]+)", first)
    if m: return m[1]
    h = first[:3000].lower()
    for k, v in (("seams reviewer", "lens:seams"), ("prior-art reviewer", "lens:prior-art"), ("contradiction reviewer", "lens:contradiction"), ("reuse scout", "gov-reuse-scout"), ("orientation", "orient-stage")):
        if k in h: return v''')
t=t.replace('''            if n == "Read": reads += 1; fs.add(i.get("file_path", "").replace("\\\\", "/").lower())''','''            if n == "Read": reads += 1; fs.add(i.get("file_path", "").replace("\\\\", "/").lower())
            if n in ("Bash", "PowerShell") and re.search(r"\\b(cat|sed -n|head|tail|Get-Content)\\b", i.get("command", "")):
                reads += 1; fs.update(p.lower() for p in re.findall(r"[\\w./-]+\\.(?:md|py|sh|js|json|toml)\\b", i.get("command", "")))''')
open(S+"/orient2.py","w",encoding="utf-8").write(t)
EOF
python $S/orient2.py
````

29. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; python - "$S" <<'EOF'
import sys
S=sys.argv[1]; t=open(S+"/orient2.py",encoding="utf-8").read()
t=t.replace('            calls += 1; byts += res.get(c["id"], 0)','            calls += 1; byts += res.get(c["id"], 0)\n            fs.update(p.lower().split("/")[-1] for p in re.findall(r"[\\w./-]+\\.(?:md|py|sh|js|json|toml|txt)\\b", json.dumps(i)))')
open(S+"/orient3.py","w",encoding="utf-8").write(t)
EOF
python $S/orient3.py 2>&1 | grep -v SyntaxWarn
````

30. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; grep -n 'calls += 1\|fs.update\|fs.add\|len(fs)' $S/orient3.py
````

31. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cat > $S/dbg.py <<'EOF'
import json,glob,os,collections
home=os.path.expanduser("~/.claude/projects")
for f in [f for d in glob.glob(home+"/C--projects-coding-governance*") for f in glob.glob(d+"/**/subagents/**/*.jsonl",recursive=True)]:
    l=open(f,encoding='utf-8').readline()
    if 'seams reviewer' not in l: continue
    c=collections.Counter()
    for x in map(json.loads,open(f,encoding='utf-8')):
        if x.get('type')=='assistant':
            for k in x['message'].get('content',[]):
                if k.get('type')=='tool_use': c[k['name']]+=1; last=k
    print(f[-40:],c.most_common(), json.dumps(last.get('input'))[:300]); break
EOF
python $S/dbg.py
````

32. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; sed -n 25,36p $S/orient3.py
````

33. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; sed -n 36,50p $S/orient3.py
````

34. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cat >> $S/dbg.py <<'EOF'
import re
for f in [f for d in glob.glob(home+"/C--projects-coding-governance*") for f in glob.glob(d+"/**/subagents/**/*.jsonl",recursive=True)]:
    l=open(f,encoding='utf-8').readline()
    if 'seams reviewer' not in l: continue
    for x in map(json.loads,open(f,encoding='utf-8')):
        if x.get('type')=='assistant':
            for k in x['message'].get('content',[]):
                if k.get('type')=='tool_use': print(k['name'], json.dumps(k['input'])[:160])
    break
EOF
python $S/dbg.py | head -12
````

35. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; sed 's/^med = lambda/import sys; print(agg["lens:seams"][:5]); sys.exit()\nmed = lambda/' $S/orient3.py > $S/orient4.py; python $S/orient4.py
````

36. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; python -c "
import re,json
print(re.findall(r'[\w./-]+\.(?:md|py|sh)', json.dumps({'command':'cd x && cat -n tools/a/b.sh'})))
src=open(r'$S/orient3.py',encoding='utf-8').read().split('\n')[37]; print(repr(src[:140]))"
````

37. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S" && python -c "
t=open('orient3.py',encoding='utf-8').read(); print(t.count('\x08')); open('orient5.py','w',encoding='utf-8').write(t.replace('\x08','\\\\b'))" && grep -c '\\b' orient5.py && python orient5.py
````

38. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cat > $S/orient6.py <<'EOF'
"""Per role: tool calls, read calls (Read, or a shell cat/sed/head/tail/Get-Content/git show), distinct
file names named in any call, bytes returned, and existence probes, before the first Write/Edit."""
import glob, json, os, re, statistics as st, collections
home = os.path.expanduser("~/.claude/projects")
files = [f for d in glob.glob(home + "/C--projects-coding-governance*") for f in glob.glob(d + "/**/subagents/**/*.jsonl", recursive=True)]
WR = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
PATH = re.compile(r"[A-Za-z0-9_./-]+\.(?:md|py|sh|js|json|toml|txt)\b")
SHREAD = re.compile(r"\b(cat|sed -n|head|tail|Get-Content|git show)\b")
EXIST = re.compile(r"(^|[;&|]\s*)(ls|find|test)\b|git ls-files|grep -[a-zA-Z]*[lc]\b|rg -[a-zA-Z]*l\b|\[ -[ef] |Test-Path")
LENS = (("seams reviewer", "lens:seams"), ("prior-art reviewer", "lens:prior-art"), ("contradiction reviewer", "lens:contradiction"), ("reuse scout", "gov-reuse-scout"), ("orientation", "orient-stage"))
agg = collections.defaultdict(list)
for f in files:
    try: L = [json.loads(l) for l in open(f, encoding="utf-8")]
    except Exception: continue
    u = next((x for x in L if x.get("type") == "user"), None)
    if not u: continue
    first = u["message"]["content"]; first = first if isinstance(first, str) else json.dumps(first)
    m = re.search(r"gov:handoff role=([\w-]+)", first)
    if m: r = m[1]
    else:
        try: r = json.load(open(f[:-6] + ".meta.json", encoding="utf-8")).get("agentType", "?")
        except Exception: r = "?"
        if r in ("workflow-subagent", "general-purpose", "?"):
            r = next((v for k, v in LENS if k in first[:3000].lower()), r)
    res = {}
    for x in L:
        if x.get("type") == "user" and isinstance(x["message"]["content"], list):
            for c in x["message"]["content"]:
                if isinstance(c, dict) and c.get("type") == "tool_result":
                    v = c.get("content"); res[c["tool_use_id"]] = len(v if isinstance(v, str) else json.dumps(v))
    calls = reads = byts = exist = 0; fs = set(); acted = False
    for x in L:
        if acted: break
        if x.get("type") != "assistant": continue
        for c in x["message"].get("content", []):
            if not isinstance(c, dict) or c.get("type") != "tool_use": continue
            n, i = c["name"], c.get("input", {}) or {}
            if n in WR: acted = True; break
            calls += 1; byts += res.get(c["id"], 0); s = json.dumps(i)
            fs.update(p.rsplit("/", 1)[-1].lower() for p in PATH.findall(s))
            cmd = i.get("command", "") if isinstance(i, dict) else ""
            if n == "Read" or (n in ("Bash", "PowerShell") and SHREAD.search(cmd)): reads += 1
            if n == "Glob" or (n == "Grep" and i.get("output_mode", "files_with_matches") != "content") or (n in ("Bash", "PowerShell") and EXIST.search(cmd)): exist += 1
    agg[r].append((calls, reads, len(fs), byts, exist, acted, len(first)))
med = lambda v: st.median(v) if v else 0
print(f"{'role':20}{'n':>5}{'calls':>7}{'reads':>6}{'files':>6}{'KBret':>7}{'briefKB':>8}{'exist':>6}{'exist%':>7}")
for r, v in sorted(agg.items(), key=lambda kv: -len(kv[1])):
    if len(v) < 10: continue
    tc = sum(x[0] for x in v); te = sum(x[4] for x in v)
    print(f"{r:20}{len(v):5}{med([x[0] for x in v]):7}{med([x[1] for x in v]):6}{med([x[2] for x in v]):6}{med([x[3] for x in v])/1000:7.1f}{med([x[6] for x in v])/1000:8.1f}{med([x[4] for x in v]):6}{100*te/max(tc,1):6.1f}%")
EOF
python $S/orient6.py
````

39. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/reviews && ls -la | awk '{print $5, $9}'
````

40. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/reviews && for f in *fold-round3-a.md *library-followup-a.md *debt-folds.md *systems-retrofit.md *library.md; do echo "== $f"; grep -cE '^(###|\*\*|- \*\*|\| )[HML][0-9]+' $f; grep -nE '^#{2,4} ' $f | head -12; done
````

41. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/reviews && python - <<'EOF'
import re
for f in ["2026-10-16-review-PLAY-dClosedLoop-1-library.md","2026-10-17-review-PLAY-dClosedLoop-1-debt-folds.md"]:
    t=open(f,encoding='utf-8').read().split("## Appendix")[0]
    items=re.findall(r"^### ([HML]\d+)[.—\s]+(.+?)\n(.*?)(?=^### |^## |\Z)",t,re.M|re.S)
    print("=====",f,len(items))
    for i,h,b in items:
        print(f"{i}: {h}\n   {re.sub(r'\s+',' ',b)[:420]}")
EOF
````

42. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/reviews && python - <<'EOF'
import re
f="2026-10-17-review-PLAY-dClosedLoop-1-systems-retrofit.md"
t=open(f,encoding='utf-8').read().split("## Appendix")[0]
items=re.findall(r"^### ([HML]\d+)[.—\s]+(.+?)\n(.*?)(?=^### |^## |\Z)",t,re.M|re.S)
print(len(items))
for i,h,b in items:
    w=re.search(r"\*\*What[^*]*:\*\*(.*?)(?=- \*\*|\Z)",b,re.S)
    print(f"{i}: {h}\n   {re.sub(r'\s+',' ',(w[1] if w else b))[:300]}")
EOF
````

43. Bash

````text
ls -a | grep conf; for f in .*.conf; do echo "$f $(grep -cE '^[A-Z_]+=' $f)"; done; grep -cE '^[A-Z_]+_PIN=' .*.conf | paste -sd' '; grep -hcE '^[A-Z_]+_CUTOFF=' .*.conf | paste -sd' '; ls memory/project tools/*waiver*.txt | wc -l; git grep -ohE 'gov:[a-z][a-z-]+' -- tools skills .claude .githooks | sort | uniq -c | sort -rn | wc -l; grep -cE '^# *check [0-9]+|^### Check [0-9]+|^## [0-9]+\.' memory/HYGIENE.md; grep -oE 'check [0-9]+' tools/memory-tree/check-memory-hygiene.sh | sort -u | wc -l; ls -d */ | wc -l
````

44. Bash

````text
for p in 'memory/builds/*/README.md' 'memory/map/features/*.md' 'tools/*/kit.toml' 'memory/gotchas/*.md'; do echo "== $p"; git log --diff-filter=A --format='%ad' --date=format:%Y-%m --name-only -- "$p" | awk '/^20[0-9][0-9]-/{m=$0;next} NF{c[m]++} END{for(k in c) print k, c[k]}' | sort; done; git log --reverse --format=%ad --date=short | head -1
````

45. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n 1,40p 2026-10-16-build-PLAY-dClosedLoop-1-atlas.py; grep -n '^def \|argv\|open(.*"w"\|write_text\|write(' 2026-10-16-build-PLAY-dClosedLoop-1-atlas.py | head -40
````

46. Bash

````text
git status --porcelain | head -3; for c in "python tools/codebase-map/gen_map.py --check" "python tools/memory-tree/gen_build_index.py --check" "python memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py --check" "python $(cygpath -w /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/census.py)"; do s=$(date +%s.%N); out=$($c 2>&1); rc=$?; e=$(date +%s.%N); printf '%-60s rc=%s %.2fs  %s\n' "${c:0:60}" $rc $(echo "$e - $s" | bc) "$(echo "$out" | tail -1 | cut -c1-90)"; done; git status --porcelain | head -3
````

47. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; for c in "tools/codebase-map/gen_map.py --check" "tools/memory-tree/gen_build_index.py --check" "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py --check" "$S/census.py"; do /usr/bin/time -f "%e s %M KB-rss" python $c > $S/out.txt 2>$S/err.txt; echo "$c :: $(tail -1 $S/err.txt) :: $(tail -1 $S/out.txt | cut -c1-120)"; done; git status --porcelain | wc -l
````

48. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; for c in "tools/codebase-map/gen_map.py --check" "tools/memory-tree/gen_build_index.py --check" "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py --check" "$S/census.py"; do a=$(date +%s%N); python $c > $S/out.txt 2>&1; rc=$?; b=$(date +%s%N); echo "$(basename ${c%% *}) rc=$rc $(( (b-a)/1000000 )) ms :: $(tail -1 $S/out.txt | cut -c1-140)"; done; git status --porcelain | wc -l
````

49. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; ls -la $S; tail -5 $S/census.py
````

50. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; head -5 $S/census.py; ls -la $S/census.py $S/orient*.py
````

51. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; cat > $S/pm2_census.py <<'EOF'
"""Run-B census for the level-0 map: per node class, its count, bytes at one line per node
(`- <ns>.<name> — <purpose cut at N>`), the share with a declared purpose, and three candidate shapes:
A flat (every node, purpose 100), B tiered (bounded classes one line per node, purpose 60; unbounded
classes one count line), C roll call (every node's name, comma-joined per class, no purpose)."""
import collections, glob as _g, json, os, re, sys
G = lambda p: sorted(x.replace("\\", "/") for x in _g.glob(p))
B = "memory/builds/dClosedLoop/build/"
rd = lambda p: open(p, encoding="utf-8").read()
V = rd(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
GR = rd(B + "2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md")
R = rd(B + "2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md")
def sec(t, tag):
    m = re.search(r"^##+ \[" + re.escape(tag) + r"\].*?(?=^##+ \[|\Z)", t, re.M | re.S); return m.group(0) if m else ""
cls = collections.OrderedDict()
def add(c, name, purpose, bounded):
    cls.setdefault(c, {"rows": [], "bounded": bounded}); cls[c]["rows"].append((name, re.sub(r"\s+", " ", purpose or "").strip()))
for m in re.finditer(r"^\| `([a-z]+)` \| (core|expansion) \| (.+?) \|$", sec(V, "layers"), re.M): add("layer", m[1], m[3], True)
for m in re.finditer(r"^- \*\*(P\d+) ([^*]+?)\*\*", V, re.M): add("principle", m[1], m[2], True)
for ln in sec(V, "chain").splitlines():
    if ln.startswith("| d"): c = [x.strip() for x in ln.strip("|").split(" | ")]; add("chain", c[0], c[1] + " · after " + c[2], True)
live = set(re.findall(r"^\| \[?`?([a-z][A-Za-z]+)", rd("memory/LIVE.md"), re.M))
for rp in G("memory/builds/*/README.md"):
    s = rp.split("/")[2]; h = re.search(r"^# \S+ — (.+)$", rd(rp), re.M)
    add("build-live" if s in live else "build-closed", s, h[1] if h else "", s in live)
for p in G("memory/map/features/*.md"):
    m = re.search(r'^title = "(.*)"', rd(p), re.M); add("feature", os.path.basename(p)[:-3], m[1] if m else "", True)
for d in sorted(x for x in os.listdir("tools") if os.path.isdir("tools/" + x) and x != "__pycache__"): add("kit", d, "", True)
for p in G("tools/roles/agents/*.agent.md"):
    m = re.search(r"^description: (.*)$", rd(p), re.M); add("role", os.path.basename(p)[:-9], m[1] if m else "", True)
for p in G(".claude/skills/*/SKILL.md") + G("skills/*/SKILL.md"):
    m = re.search(r"^description: (.*)$", rd(p), re.M); add("skill", p.split("/")[-2], m[1] if m else "", True)
for p in G("memory/guides/*.md"):
    m = re.search(r"^# (.+)$", rd(p), re.M); add("guide", os.path.basename(p)[:-3], m[1] if m else "", True)
s = json.load(open(".claude/settings.json", encoding="utf-8"))
for ev, arr in s["hooks"].items():
    for m in arr:
        for x in m["hooks"]: add("hook", ev + ":" + re.findall(r"[\w.-]+\.(?:js|sh)", x["command"])[-1], "", True)
for g in ("commit-msg", "pre-commit", "pre-push", "pre-rebase"): add("hook", "git:" + g, "", True)
ns = collections.Counter(re.findall(r"^\| `([a-z]+)\.", sec(V, "policies"), re.M))
for n, k in ns.items(): add("policy-ns", n, f"{k} keys", True)
areas = collections.Counter(re.findall(r"^\| gap-([a-z]+)-\d+ ", GR, re.M))
for a, k in areas.items(): add("gap-area", a, f"{k} gaps", True)
# unbounded classes
for l in json.load(open("tools/gate-legs.json", encoding="utf-8")): add("leg", l["name"], "", False)
for p in G("memory/gotchas/*.md"):
    if os.path.basename(p) in ("README.md", "INDEX.md"): continue
    m = re.search(r"^description: (.*)$", rd(p), re.M); add("class", os.path.basename(p)[:-3], m[1] if m else "", False)
for m in re.finditer(r"^- (?:\*\*)?([A-Z]+-[A-Za-z]+-\d+)(?:\*\*)? (?:·|—) (?:\*\*)?(.+)$", rd("memory/DECISIONS.md"), re.M): add("decision", m[1], m[2], False)
for m in re.finditer(r"^\| `([a-z]+\.[a-z0-9.-]+)` \|", sec(V, "policies"), re.M): add("policy", m[1], "", False)
for m in re.finditer(r"^\| (gap-[a-z]+-\d+) \| [^|]+\| [A-Z]+ \| ([^|]+)\|", GR, re.M): add("gap", m[1], m[2], False)
for i in sorted(set(re.findall(r"`((?:entry|plan|design|build|test|deploy|review|life|adopt)\.[a-z-]+)`", sec(R, "matrix")))): add("item", i, "", False)
for f in G(".*.conf"):
    for k in re.findall(r"^([A-Z][A-Z0-9_]+)=", rd(f), re.M): add("conf-key", os.path.basename(f) + ":" + k, "", False)
for p in G("memory/project/*.txt") + G("tools/*waiver*.txt"): add("population", os.path.basename(p), "", False)
for p in G(B + "*.md"): add("record", os.path.basename(p)[len("2026-10-14-build-PLAY-dClosedLoop-1-"):-3], "", False)
def ln(c, n, p, w): return f"- {c}.{n}" + (f" — {p if len(p) <= w else p[:w-1] + '…'}" if p and w else "")
by = lambda lines: sum(len(x.encode()) + 1 for x in lines)
A = Bt = C = 0
print(f"{'class':13}{'n':>5}{'bound':>6}{'purp%':>6}{'A flat':>8}{'B tier':>8}{'C roll':>8}")
for c, d in cls.items():
    rows = d["rows"]; n = len(rows); pc = 100 * sum(1 for _, p in rows if p) // n
    a = by(ln(c, x, p, 100) for x, p in rows)
    b = by(ln(c, x, p, 60) for x, p in rows) if d["bounded"] else by([f"- {c}.* — {n} nodes · gov tag show {c}"])
    r = len((f"{c} ({n}): " + ", ".join(x for x, _ in rows) + "\n").encode())
    A += a; Bt += b; C += r
    print(f"{c:13}{n:5}{str(d['bounded'])[0]:>6}{pc:5}%{a:8}{b:8}{r:8}")
print(f"{'all':13}{sum(len(d['rows']) for d in cls.values()):5}{'':12}{A:8}{Bt:8}{C:8}")
EOF
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python $S/pm2_census.py
````

52. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && sed -e 's/^A = Bt = C = 0/import sys\nfor W in (0, 30, 40, 60, 80):\n    print(W, sum(by(ln(c, x, p, W) for x, p in d["rows"]) if d["bounded"] else by([f"- {c}.* — {len(d[\x27rows\x27])} nodes · gov tag show {c}"]) for c, d in cls.items()))\nsys.exit()\nA = Bt = C = 0/' $S/pm2_census.py > $S/pm2_width.py && python $S/pm2_width.py; python - <<'EOF'
import re
t=open("memory/DECISIONS.md",encoding="utf-8").read()
print("bold (major-looking) decision rows:", len(re.findall(r"^- \*\*[A-Z]+-", t, re.M)))
EOF
````

53. Bash

````text
grep -n -A30 '^\[selection\]' tools/govkit/registry.toml | grep -E 'default|"' | head -20; grep -n 'id = "codebase-map"' -A8 tools/codebase-map/kit.toml | head; grep -n 'optional\|opt-in' tools/codebase-map/kit.toml | head -5; ls help 2>/dev/null | head -3
````

54. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; cat > $S/pm2_hits.py <<'EOF'
"""Losing test for each map shape: of the systems audit's 23 'part not in view' items (rows A and C of
the project-map record's [sort], minus the content-only M35), does the render NAME the node whose absence
from view caused the defect? Tokens are the node names the review's own Where/What cites."""
import re, subprocess, sys, glob as _g, os
exec(open(sys.argv[1], encoding="utf-8").read().split("def ln(")[0])          # reuse pm2_census's classes
# classes the probe and census lack: hygiene checks, gov: markers, top-level directories
for n in sorted(set(re.findall(r"\bcheck (\d+)\b", rd("tools/memory-tree/check-memory-hygiene.sh")))): add("check", "hygiene-" + n, "", False)
for w in sorted(set(subprocess.run(["git", "grep", "-ohE", "gov:[a-z][a-z-]+", "--", "tools", "skills", ".claude", ".githooks"], capture_output=True, text=True).stdout.split())): add("marker", w, "", False)
for d in sorted(x for x in os.listdir(".") if os.path.isdir(x) and not x.startswith(".")): add("dir", d, "", True)
TOK = {"H1": "refusal-retirements.txt", "H3": "kit.codebase-map", "H4": "check.hygiene-3", "M14": "derive_low_waters",
       "M15": "Bash|PowerShell", "M16": "VERB_OFFENDER_PIN", "M18": "workflows.toml", "M19": "compute_coverage",
       "M20": "_CUTOFF", "M21": "_drop_affordance_exempt", "M24": "check.hygiene-3", "M25": "voluntary",
       "M26": "leg.", "M27": "parity", "M28": "memory-tree-merge-driver", "M33": "gov:kit", "L6": "review-shape",
       "L8": "kit.lib — ", "L10": "dir.help", "M2": "dShippedRelease — Deploy · after dWitnessedBar", "M3": "adopt.census — owner",
       "M10": "namespace.doc — owner"}
def render(mode):
    out = []
    for c, d in cls.items():
        rows = d["rows"]
        if mode == "C" or (mode == "B+" and not d["bounded"]): out.append(f"{c} ({len(rows)}): " + ", ".join(f"{c}.{x}" for x, _ in rows))
        elif d["bounded"]: out += [f"- {c}.{x}" + (f" — {p[:59]}" if p else "") for x, p in rows]
        else: out.append(f"- {c}.* — {len(rows)} nodes · gov tag show {c}")
    return "\n".join(out)
for mode in ("B", "B+", "C"):
    t = render(mode); hit = [k for k, v in TOK.items() if v in t]
    print(f"{mode:3} {len(t.encode()):6} B  hits {len(hit):2}/{len(TOK)}: {' '.join(hit)}")
EOF
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python $S/pm2_hits.py $S/pm2_census.py | tail -3
````

55. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; cat > $S/pm2_probes.py <<'EOF'
"""Share of structural roles' existence probes whose target names a node of map B (bounded classes) or of
map C (every node). A probe's target = the path-ish or word tokens of a Glob pattern, a Grep pattern in
list/count mode, or an ls/find/test/git ls-files/grep -l command."""
import glob, json, os, re, sys, collections
names = collections.defaultdict(set)
exec(open(sys.argv[1], encoding="utf-8").read().split("def ln(")[0])
for c, d in cls.items():
    for x, _ in d["rows"]:
        for k in {x.lower(), re.sub(r"\.(md|txt|py|sh|js|toml|json)$", "", x.lower())}: names["B" if d["bounded"] else "U"].add(k)
home = os.path.expanduser("~/.claude/projects")
STRUCT = ("gov-researcher", "gov-spec-writer", "gov-spec-reviewer", "lens:seams", "lens:prior-art", "lens:contradiction", "orient-stage", "Plan", "gov-reuse-scout", "gov-orienter")
EXIST = re.compile(r"(^|[;&|]\s*)(ls|find|test)\b|git ls-files|grep -[a-zA-Z]*[lc]\b|rg -[a-zA-Z]*l\b|\[ -[ef] |Test-Path")
LENS = (("seams reviewer", "lens:seams"), ("prior-art reviewer", "lens:prior-art"), ("contradiction reviewer", "lens:contradiction"), ("reuse scout", "gov-reuse-scout"), ("orientation", "orient-stage"))
tot = hb = hc = 0
for f in [f for d in glob.glob(home + "/C--projects-coding-governance*") for f in glob.glob(d + "/**/subagents/**/*.jsonl", recursive=True)]:
    try: L = [json.loads(l) for l in open(f, encoding="utf-8")]
    except Exception: continue
    u = next((x for x in L if x.get("type") == "user"), None)
    if not u: continue
    first = u["message"]["content"]; first = first if isinstance(first, str) else json.dumps(first)
    m = re.search(r"gov:handoff role=([\w-]+)", first)
    r = m[1] if m else None
    if not r:
        try: r = json.load(open(f[:-6] + ".meta.json", encoding="utf-8")).get("agentType", "?")
        except Exception: r = "?"
        if r in ("workflow-subagent", "general-purpose", "?"): r = next((v for k, v in LENS if k in first[:3000].lower()), r)
    if r not in STRUCT: continue
    for x in L:
        if x.get("type") != "assistant": continue
        for c in x["message"].get("content", []):
            if not isinstance(c, dict) or c.get("type") != "tool_use": continue
            n, i = c["name"], c.get("input") or {}
            if n == "Glob": q = i.get("pattern", "")
            elif n == "Grep" and i.get("output_mode", "files_with_matches") != "content": q = i.get("pattern", "") + " " + i.get("path", "")
            elif n in ("Bash", "PowerShell") and EXIST.search(i.get("command", "")): q = i.get("command", "")
            else: continue
            toks = {t.lower() for t in re.split(r"[\s/\\'\"*|(){}\[\],;:=]+", q) if len(t) > 2}
            toks |= {re.sub(r"\.(md|txt|py|sh|js|toml|json)$", "", t) for t in toks}
            tot += 1; b = bool(toks & names["B"]); hb += b; hc += b or bool(toks & names["U"])
print(f"existence probes by structural roles: {tot}; naming a node of map B: {hb} ({100*hb/tot:.1f}%); of map C: {hc} ({100*hc/tot:.1f}%)")
EOF
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python $S/pm2_probes.py $S/pm2_census.py | tail -1
````

56. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; python - "$S" <<'EOF'
import sys
S=sys.argv[1]; t=open(S+"/pm2_probes.py",encoding="utf-8").read()
old='toks = {t.lower() for t in re.split(r"[\\s/\\\\\'\\"*|(){}\\[\\],;:=]+", q) if len(t) > 2}'
assert old in t, "pattern"
t=t.replace(old,'toks = {w.replace("\\\\", "/").rstrip("/").split("/")[-1].strip("\'\\"*").lower() for w in re.split(r"\\s+", q)} - {""}; toks = {x for x in toks if len(x) > 2}')
open(S+"/pm2_probes2.py","w",encoding="utf-8").write(t)
EOF
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python $S/pm2_probes2.py $S/pm2_census.py | tail -1
````

57. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; sed 's/tot += 1; b = bool(toks \& names\["B"\]); hb += b/tot += 1; b = bool(toks \& names["B"]); hb += b\n            if b and tot % 97 == 0: print("HIT", sorted(toks \& names["B"]), "<-", q[:110].replace("\\n"," "))/' $S/pm2_probes2.py > $S/pm2_probes3.py; cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python $S/pm2_probes3.py $S/pm2_census.py 2>/dev/null | grep HIT | head -14
````

58. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; python - "$S" <<'EOF'
import sys
S=sys.argv[1]; t=open(S+"/pm2_probes2.py",encoding="utf-8").read()
old='tot += 1; b = bool(toks & names["B"]); hb += b;'
assert old in t
t=t.replace(old,'tot += 1; b = bool(toks & names["B"]); hb += b\n            if b and tot % 97 == 0: print("HIT", sorted(toks & names["B"]), "<-", q[:110].replace(chr(10), " "))\n           ;')
open(S+"/pm2_probes3.py","w",encoding="utf-8").write(t)
EOF
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python $S/pm2_probes3.py $S/pm2_census.py 2>&1 | grep -v Warn | head -16
````

59. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; python - "$S" <<'EOF'
import sys
S=sys.argv[1]; t=open(S+"/pm2_probes2.py",encoding="utf-8").read()
old='tot += 1; b = bool(toks & names["B"]); hb += b; hc += b or bool(toks & names["U"])'
assert old in t
t=t.replace(old,old+'\n            if b and tot % 97 == 0: print("HIT", sorted(toks & names["B"]), "<-", q[:110].replace(chr(10), " "))')
open(S+"/pm2_probes3.py","w",encoding="utf-8").write(t)
EOF
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python $S/pm2_probes3.py $S/pm2_census.py 2>&1 | grep HIT | head -14
````

60. Bash

````text
git grep -l 'CARDS\.md\|generated/MAP\.md' -- . ':!memory/builds' | head -20; echo ===; git grep -n 'CARDS\.md\|generated/MAP\.md' -- AGENTS.md CLAUDE.md coding-governance-agents.template.md skills .claude memory/guides | head
````

61. Bash

````text
cd ~/.claude/projects && for d in C--projects-coding-governance*; do find "$d" -name '*.jsonl'; done 2>/dev/null | xargs grep -l 'generated/CARDS.md\|generated/MAP.md' 2>/dev/null | wc -l; for d in C--projects-coding-governance*; do find "$d" -name '*.jsonl'; done 2>/dev/null | wc -l
````

62. Bash

````text
cd ~/.claude/projects && for d in C--projects-coding-governance*; do find "$d" -name '*.jsonl'; done 2>/dev/null | xargs grep -ohE '"file_path":"[^"]*generated[/\\]+(CARDS|MAP)\.md"|(cat|sed -n [^ ]+|head[^|]*) [^ ]*generated/(CARDS|MAP)\.md' 2>/dev/null | sed -E 's/.*(CARDS|MAP)\.md.*/\1/' | sort | uniq -c
````

63. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; python - "$S" <<'EOF'
import sys
S=sys.argv[1]; t=open(S+"/pm2_hits.py",encoding="utf-8").read()
t=t.replace('(mode == "B+" and not d["bounded"])','(mode == "B+" and not d["bounded"]) or (mode == "Barch" and c in ("leg", "check", "conf-key", "population", "marker"))')
t=t.replace('for mode in ("B", "B+", "C"):','for mode in ("B", "Barch", "B+", "C"):')
open(S+"/pm2_hits2.py","w",encoding="utf-8").write(t)
EOF
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python $S/pm2_hits2.py $S/pm2_census.py | tail -4
````

64. Bash

````text
grep -n '^Inventories' memory/map/generated/MAP.md; grep -n 'at most 1024' memory/map/generated/CARDS.md | head -2; grep -n '"hooks"' .claude/settings.json; grep -n 'TASK_FIELDS' tools/roles/handoff.py | head -3; grep -n 'def compute_coverage' tools/codebase-map/map_lib.py; grep -n 'opt-in\|OPT-IN\|An opt-in' tools/codebase-map/README.md | head -2; grep -n 'def derive\|--check' memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py | head -3
````

## [run-b] Run B, dispatch 88

1. Bash

````text
ls memory/builds/dClosedLoop/build/ | head -80 && wc -c memory/builds/dClosedLoop/build/*project-map* memory/builds/dClosedLoop/build/*layer-memory* memory/builds/dClosedLoop/build/*systems* memory/builds/dClosedLoop/build/*orientation.md memory/builds/dClosedLoop/build/*layer-roles* memory/builds/dClosedLoop/build/*architecture-v2*
````

2. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n "^## \|^### " 2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md | head -80; echo ---; grep -n "^## \|^### " 2026-10-16-build-PLAY-dClosedLoop-1-systems.md | head -80
````

3. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n "^## \|^### " 2026-10-14-build-PLAY-dClosedLoop-1-orientation.md; echo ---; grep -n "^## \|^### " 2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md; echo ---; grep -n "^## \|^### \|P27" 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | head -80
````

4. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i "work order" 2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md | head -40
````

5. Bash

````text
ls tools/codebase-map/ tools/codebase-map/* | head -60; wc -c tools/codebase-map/*.py tools/memory-tree/gen_build_index.py memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py memory/map/generated/* memory/LIVE.md 2>/dev/null; ls memory/map memory/map/*
````

6. Bash

````text
head -60 memory/map/generated/MAP.md; echo ...; grep -n "^## " memory/map/generated/MAP.md; echo; head -30 memory/map/generated/CARDS.md
````

7. Bash

````text
sed -n 1,40p tools/memory-tree/gen_build_index.py; grep -n "add_argument\|def main" tools/memory-tree/gen_build_index.py | head -30; head -20 memory/LIVE.md
````

8. Bash

````text
ls tools/*/kit.toml | wc -l; ls tools/; python -c "import json;d=json.load(open('tools/gate-legs.json'));print(type(d), list(d)[:5] if isinstance(d,dict) else d[0])" 2>&1 | head; ls memory/builds | wc -l; ls memory/; ls memory/gotchas | wc -l; ls tools/roles/agents | head -30
````

9. Bash

````text
ls tools/*/kit.toml; head -25 tools/codebase-map/kit.toml; grep -h "^description\|^summary\|^purpose" tools/*/kit.toml | head; sed -n 154,180p memory/map/generated/MAP.md
````

10. Bash

````text
python - <<'EOF'
import json,collections
d=json.load(open('tools/gate-legs.json',encoding='utf-8'))
print(len(d)); c=collections.Counter(k for x in d for k in x); print(c)
EOF
ls tools/govkit tools/lib | head; python -c "
import json;s=json.load(open('.claude/settings.json',encoding='utf-8'));h=s.get('hooks',{});print({k:sum(len(e.get('hooks',[])) for e in v) for k,v in h.items()})"; ls .githooks 2>/dev/null || git config core.hooksPath
````

11. Bash

````text
head -5 memory/DECISIONS.md; grep -c "^| " memory/DECISIONS.md; echo; ls memory/gotchas | head -3; head -8 memory/gotchas/$(ls memory/gotchas | sed -n 5p); echo; sed -n 1,30p memory/builds/aOrientedCast/README.md
````

12. Bash

````text
sed -n 1,15p memory/DECISIONS.md | cut -c1-400; awk 'NR>5' memory/DECISIONS.md | grep -c "^- \*\*\|^### \|^## "
````

13. Bash

````text
B=memory/builds/dClosedLoop/build; grep -m3 "^| gap-" $B/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md | cut -c1-300; grep -c "^| gap-" $B/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md; sed -n 299,330p $B/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md | cut -c1-250; grep -n "^| \`" $B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | sed -n '1,3p' | cut -c1-300
````

14. Bash

````text
B=memory/builds/dClosedLoop/build; sed -n 330,390p $B/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md | cut -c1-220
````

15. Bash

````text
sed -n 1,60p memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py; grep -n "argv\|write\|open(" memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py | head -30
````

16. Bash

````text
PY=$(bash -c 'source tools/lib/resolve-python.sh 2>/dev/null; echo ${PYTHON:-python}'); echo PY=$PY; git status --porcelain | wc -l; for c in "tools/codebase-map/gen_map.py --check" "tools/memory-tree/gen_build_index.py --check" "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py --check"; do s=$(date +%s.%N); python $c > /tmp/o.txt 2>&1; rc=$?; e=$(date +%s.%N); echo "$c rc=$rc $(echo "$e - $s" | bc) s $(wc -c </tmp/o.txt)B"; tail -2 /tmp/o.txt; done; git status --porcelain | wc -l
````

17. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; mkdir -p "$S"; git status --porcelain | wc -l; for c in "tools/codebase-map/gen_map.py --check" "tools/memory-tree/gen_build_index.py --check" "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py --check"; do s=$(date +%s%N); python $c > "$S/o.txt" 2>&1; rc=$?; e=$(date +%s%N); echo "$c rc=$rc $(( (e - s)/1000000 )) ms out=$(wc -c <"$S/o.txt")B"; tail -2 "$S/o.txt"; done; git status --porcelain | wc -l
````

18. Bash

````text
sed -n 204,240p memory/map/generated/MAP.md; sed -n 383,420p memory/map/generated/MAP.md; ls .claude/skills 2>/dev/null; ls tools/roles/
````

19. Bash

````text
B=memory/builds/dClosedLoop/build; grep -m3 "^| \`[a-z]*\.[a-z-]*\` |" $B/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md | cut -c1-250; grep -o "^| \`[a-z]*\.[a-z0-9-]*\` |" $B/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md | sort -u | wc -l; grep -n "\[extend\]" $B/*layer-*.md | head; head -6 tools/roles/agents/gov-builder.agent.md | cut -c1-200; head -5 .claude/skills/build/SKILL.md | cut -c1-200
````

20. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cat > "$S/census.py" <<'EOF'
"""Node census for a level-0 map: per class, count, bytes at one line per node, and purpose source."""
import json, re, glob, os, collections, sys
B = "memory/builds/dClosedLoop/build/"
rd = lambda p: open(p, encoding="utf-8").read()
V = rd(B+"2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
G = rd(B+"2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md")
FS = rd(B+"2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md")
LIVE = rd("memory/LIVE.md")
def section(t, tag):
    m = re.search(r"^##+ \[" + re.escape(tag) + r"\].*?(?=^## \[|\Z)", t, flags=re.M | re.S); return m.group(0) if m else ""
def cut(s, n=90):
    s = re.sub(r"\s+", " ", s or "").strip(); return s if len(s) <= n else s[:n-1] + "…"
def fm(p):
    t = rd(p); m = re.match(r"---\n(.*?)\n---", t, re.S); d = {}
    if m:
        for l in m.group(1).splitlines():
            if ":" in l: k, v = l.split(":", 1); d[k.strip()] = v.strip()
    return d, t
L = collections.OrderedDict(); SRC = {}
def add(cls, tag, purpose, extra="", src=None):
    L.setdefault(cls, []).append(f"- {tag} — {cut(purpose)}" + (f" · {extra}" if extra else "") if purpose else f"- {tag}" + (f" · {extra}" if extra else ""))
    if src: SRC[cls] = src
for m in re.finditer(r"^\| `([a-z]+)` \| (core|expansion) \| (.+?) \|$", section(V, "layers"), re.M):
    add("layer", "layer."+m.group(1), m.group(3), m.group(2), "declared: v2 [layers] definition column")
for m in re.finditer(r"^- \*\*(P\d+) ([^*]+?)\*\*", V, re.M):
    add("principle", "principle."+m.group(1).lower(), m.group(2), "", "declared: v2 [principles] bold title")
for ln in section(V, "chain").splitlines():
    if ln.startswith("| d"):
        c = [x.strip() for x in ln.strip().strip("|").split(" | ")]
        add("chain build", "build."+c[0], c[1], f"after {c[2]} · gaps {len(re.findall(r'gap-[a-z]+-\d+', c[-1]))}", "partial: v2 [chain] stage word only")
live = {}
for ln in LIVE.splitlines():
    m = re.match(r"\| \[(\w+)\]", ln)
    if m: live[m.group(1)] = ln.split("|")[2].strip()
h1yes = 0
for rp in sorted(glob.glob("memory/builds/*/README.md")):
    slug = rp.split("/")[2]; d, t = fm(rp)
    h = re.search(r"^# \S+ — (.+)$", t, re.M); h1yes += bool(h)
    cls = "build (live)" if slug in live else "build (closed)"
    ids = len(d.get("ids", "").split())
    add(cls, "build."+slug, h.group(1) if h else "", f"{live.get(slug,'closed')} · node {d.get('node','?')} · ids {ids}", "authored H1 after the slug in README (no declared field)")
for p in sorted(glob.glob("memory/map/features/*.md")):
    t = rd(p); m = re.search(r'^title = "(.+)"', t, re.M)
    add("feature", "feature."+os.path.basename(p)[:-3], m.group(1) if m else "", "", "declared: dossier toml `title`")
kits = sorted(set(os.path.dirname(p).split(os.sep)[-1].split("/")[-1] for p in glob.glob("tools/*/kit.toml")) | {"govkit", "lib"})
for k in kits:
    r = f"tools/{k}/README.md"; h = re.search(r"^# (.+)$", rd(r), re.M) if os.path.exists(r) else None
    add("kit", "kit."+k, h.group(1) if h else "", "", "none declared: kit.toml has no purpose; README H1 as proxy")
legs = json.load(open("tools/gate-legs.json", encoding="utf-8"))
for x in legs: add("gate leg", "leg", x["name"], "", "name only: gate-legs.json has no purpose field")
S = json.load(open(".claude/settings.json", encoding="utf-8"))
for ev, es in S.get("hooks", {}).items():
    for e in es:
        for h in e.get("hooks", []):
            add("harness hook", f"hook.{ev}", "", h.get("command","")[-60:], "none declared")
for g in [p for p in glob.glob(".githooks/*") if "." not in os.path.basename(p)]:
    add("git hook", "hook.git."+os.path.basename(g), "", "", "none declared")
for p in sorted(glob.glob(".claude/skills/*/SKILL.md")):
    d, _ = fm(p); add("skill", "skill."+p.split("/")[2], d.get("description",""), "", "declared: SKILL.md `description`")
for p in sorted(glob.glob("tools/roles/agents/*.agent.md")):
    d, _ = fm(p); add("role (today)", "role."+d.get("name",""), d.get("description",""), "", "declared: agent.md `description`")
for p in sorted(glob.glob("tools/workflows/*.js")) + sorted(glob.glob("tools/unattended/*.js")):
    add("workflow script", "workflow."+os.path.basename(p), "", "", "none declared (file header comment only)")
for p in sorted(glob.glob("memory/gotchas/*.md")):
    if p.endswith("INDEX.md"): continue
    d, _ = fm(p); add("bug class", "class."+os.path.basename(p)[:-3], d.get("description",""), "", "declared: gotcha `description`")
for p in sorted(glob.glob("memory/guides/*.md")):
    h = re.search(r"^# (.+)$", rd(p), re.M); add("guide", "doc."+os.path.basename(p), h.group(1) if h else "", "", "H1 only")
dec = [l for l in rd("memory/DECISIONS.md").splitlines() if re.match(r"- \**[A-Z]+-\w+-\d+", l)]
for l in dec:
    m = re.match(r"- \**([A-Z]+-\w+-\d+)\**\s*[·—]\s*(.*)", l); add("decision row", "dec."+(m.group(1) if m else "?"), m.group(2) if m else l, "", "declared: the row's text (unclassed; major not routed)")
ns = collections.Counter(re.findall(r"^\| `([a-z]+)\.", section(V, "policies"), re.M))
for n, k in ns.items(): add("policy namespace", "policy."+n, "", f"{k} keys", "none per namespace; per key a why column")
area = collections.Counter(re.findall(r"^\| gap-([a-z]+)-\d+ ", G, re.M))
for a, k in area.items(): add("gap area", "gap."+a, "", f"{k} gaps", "none per area; per gap a row text")
for m in re.finditer(r"^\| `([a-z]+\.[a-z0-9-]+)` \| ([^|]+) \| [^|]* \| ([^|]+) \|", FS, re.M):
    add("item", "item."+m.group(1), m.group(3), cut(m.group(2), 20), "declared: flow-steps `does` column")
for p in sorted(glob.glob(B+"*.md")):
    t = rd(p); h = re.search(r"^# (.+)$", t, re.M)
    add("design record", "rec."+re.sub(r".*-1-", "", os.path.basename(p))[:-3], h.group(1) if h else "", "", "H1 only")
tot = 0; nodes = 0
print(f"{'class':18} {'nodes':>5} {'bytes':>7} {'B/node':>6}  purpose source")
for c, ls in L.items():
    b = sum(len(x.encode()) + 1 for x in ls); tot += b; nodes += len(ls)
    print(f"{c:18} {len(ls):5} {b:7} {b//len(ls):6}  {SRC.get(c,'')}")
print(f"{'all':18} {nodes:5} {tot:7}")
print("build READMEs with an H1 purpose:", h1yes, "of", len(glob.glob('memory/builds/*/README.md')))
if "--print" in sys.argv:
    for c, ls in L.items(): print("\n## "+c); print("\n".join(ls[:4]))
EOF
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python "$S/census.py" --print
````

21. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && sed -i 's/glob\.glob(/GG(/g; s/^import json, re, glob, os, collections, sys$/import json, re, glob, os, collections, sys\nGG = lambda p: [x.replace("\\\\", "\/") for x in glob.glob(p)]/' "$S/census.py" && sed -n 2,4p "$S/census.py" && python "$S/census.py" --print
````

22. Bash

````text
ls -d ~/.claude/projects/C--projects-coding-governance* | head; for d in ~/.claude/projects/C--projects-coding-governance*; do echo "$d $(find "$d" -name '*.jsonl' -path '*subagents*' | wc -l) $(find "$d" -name '*.jsonl' | wc -l)"; done 2>/dev/null | awk '{print $2, $3}' | paste -sd' ' ; find ~/.claude/projects/C--projects-coding-governance* -name '*.jsonl' -path '*subagents*' | head -3
````

23. Bash

````text
f=$(find ~/.claude/projects/C--projects-coding-governance* -name '*.jsonl' -path '*subagents*' | head -1); ls "$(dirname "$f")" | head; head -c 1500 "$f"; echo; python -c "
import json,sys
for i,l in enumerate(open(sys.argv[1],encoding='utf-8')):
    o=json.loads(l); print(i,o.get('type'),list(o)[:12]) 
    if i>4: break" "$f"
````

24. Bash

````text
cd ~/.claude/projects && cat "$(find C--projects-coding-governance* -name '*.meta.json' -path '*subagents*' | head -1)"; echo; find C--projects-coding-governance* -name '*.meta.json' -path '*subagents*' | xargs cat 2>/dev/null | python -c "
import sys,json,re,collections
c=collections.Counter()
for m in re.finditer(r'\"agentType\"\s*:\s*\"([^\"]+)\"', sys.stdin.read()): c[m.group(1)]+=1
print(c.most_common(30))"
````

25. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cat > "$S/tx.py" <<'EOF'
"""Orientation reads per role from subagent transcripts: bytes of tool results, read calls, distinct files,
and existence searches, before the first act (first Write/Edit for writers; the whole run for read-only roles)."""
import json, glob, os, re, sys, collections, statistics as st
root = os.path.expanduser("~/.claude/projects")
files = [p for p in glob.glob(root + "/C--projects-coding-governance*/**/subagents/**/*.jsonl", recursive=True)]
def role_of(meta, first):
    t = meta.get("agentType", "")
    if t != "workflow-subagent" and t != "general-purpose":
        m = re.search(r"role=(gov-[a-z-]+)", first); return m.group(1) if m else t
    m = re.search(r"role=(gov-[a-z-]+)", first)
    if m: return m.group(1)
    low = first[:3000].lower()
    for lens in ("coherence", "reuse", "grounding", "failure-envelope", "blast-radius", "alternatives"):
        if re.search(r"\b" + lens + r"\b[^.\n]{0,40}\blens\b|\blens\b[^.\n]{0,40}\b" + lens, low): return "lens:" + lens
    if "skeptic" in low[:400]: return "wf:skeptic"
    return t
WRITE = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
EXIST = re.compile(r"(^|[;&|]\s*)(ls|find|test -[ef]|\[ -[ef]|git ls-files|git grep -l|grep -[a-zA-Z]*[lc]|rg -[a-zA-Z]*[lc]|rg --files)\b")
rows = collections.defaultdict(list)
for p in files:
    mp = p[:-6] + ".meta.json"
    meta = json.load(open(mp, encoding="utf-8")) if os.path.exists(mp) else {}
    first = None; calls = {}; res_bytes = 0; reads = 0; exist = 0; searches = 0; dfiles = set(); acted = False; total_calls = 0
    try:
        for line in open(p, encoding="utf-8"):
            o = json.loads(line); msg = o.get("message") or {}
            c = msg.get("content")
            if first is None and o.get("type") == "user":
                first = c if isinstance(c, str) else json.dumps(c)[:5000]
            if not isinstance(c, list) or acted: continue
            for b in c:
                if b.get("type") == "tool_use":
                    n = b["name"]; i = b.get("input", {}); total_calls += 1
                    if n in WRITE: acted = True; break
                    calls[b["id"]] = n
                    if n == "Read": reads += 1; dfiles.add(i.get("file_path", "").lower().replace("\\", "/"))
                    elif n == "Glob": exist += 1; searches += 1
                    elif n == "Grep":
                        searches += 1
                        if i.get("output_mode", "files_with_matches") in ("files_with_matches", "count"): exist += 1
                    elif n in ("Bash", "PowerShell"):
                        cmd = i.get("command", "")
                        if re.search(r"\b(cat|sed -n|head|tail|Get-Content)\b", cmd): reads += 1
                        if re.search(r"\b(grep|rg|find|ls|Select-String)\b", cmd): searches += 1
                        if EXIST.search(cmd): exist += 1
                elif b.get("type") == "tool_result" and b.get("tool_use_id") in calls:
                    cc = b.get("content"); s = cc if isinstance(cc, str) else json.dumps(cc)
                    res_bytes += len(s.encode("utf-8"))
    except Exception as e:
        continue
    if first is None: continue
    r = role_of(meta, first or "")
    rows[r].append((res_bytes, reads, len(dfiles), searches, exist, total_calls, acted, len((first or "").encode())))
print(f"{'role':22} {'n':>5} {'medKB':>6} {'p90KB':>6} {'reads':>5} {'files':>5} {'srch':>4} {'exist':>5} {'calls':>5} {'exist%':>6} {'acted':>5} {'promptKB':>8}")
for r, v in sorted(rows.items(), key=lambda kv: -len(kv[1])):
    if len(v) < 5: continue
    med = lambda k: st.median(x[k] for x in v)
    b = sorted(x[0] for x in v); p90 = b[int(.9 * (len(b) - 1))]
    ec = sum(x[4] for x in v); tc = sum(x[5] for x in v) or 1
    print(f"{r:22} {len(v):5} {med(0)/1000:6.1f} {p90/1000:6.1f} {med(1):5.0f} {med(2):5.0f} {med(3):4.0f} {med(4):5.0f} {med(5):5.0f} {100*ec/tc:6.1f} {sum(x[6] for x in v):5} {med(7)/1000:8.1f}")
EOF
python "$S/tx.py"
````

26. Bash

````text
cd ~/.claude/projects && python - <<'EOF'
import glob,json,re,collections,os
fs=glob.glob(os.path.expanduser("~/.claude/projects")+"/C--projects-coding-governance*/**/subagents/workflows/**/*.jsonl",recursive=True)
c=collections.Counter()
for p in fs:
    l=open(p,encoding="utf-8").readline()
    try: o=json.loads(l)
    except: continue
    m=o.get("message",{}).get("content"); s=m if isinstance(m,str) else json.dumps(m)
    h=re.search(r"(?i)(?:lens|LENS)[:\s]+\**`?([A-Za-z-]+)",s[:4000])
    first=s[:80].replace("\n"," ")
    c[(h.group(1).lower() if h else "-")]+=1
print(c.most_common(40))
EOF
````

27. Bash

````text
grep -n -i "coherence\|reuse" tools/workflows/tier2-review.js | head -20; grep -n -o "lens[A-Za-z]*: *['\"][a-z-]*" tools/workflows/tier2-review.js | head -20
````

28. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S" && python - <<'EOF'
import re
s=open("tx.py",encoding="utf-8").read()
s=s.replace('''    low = first[:3000].lower()''','''    if re.search(r"Coherence: ", first): return "lens:coherence"
    if re.search(r"Reuse: (functionality|is )", first) or re.search(r"(?i)\\breuse lens\\b", first[:1500]): return "lens:reuse"
    low = first[:3000].lower()''')
s=s.replace('''first = c if isinstance(c, str) else json.dumps(c)[:5000]''','''first = c if isinstance(c, str) else json.dumps(c)[:20000]''')
s=s.replace('''                        if re.search(r"\\b(cat|sed -n|head|tail|Get-Content)\\b", cmd): reads += 1''','''                        if re.search(r"\\b(cat|sed -n|head|tail|Get-Content)\\b", cmd):
                            reads += 1
                            for f in re.findall(r"[\\w./:-]+\\.(?:md|py|js|json|toml|sh|txt)\\b", cmd): dfiles.add(f.lower().split("/")[-1])''')
open("tx.py","w",encoding="utf-8").write(s)
EOF
python "$S/tx.py"
````

29. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; grep -n "lens:coherence\|dfiles.add(f" "$S/tx.py"; cd ~/.claude/projects; grep -l "Coherence: does\|COHERENCE" -r --include='*.jsonl' C--projects-coding-governance*/ 2>/dev/null | grep subagents | wc -l; f=$(grep -l "Coherence: does" -r --include='*.jsonl' C--projects-coding-governance*/ | grep subagents | head -1); echo $f; head -1 "$f" | cut -c1-1200
````

30. Bash

````text
cd ~/.claude/projects && python - <<'EOF'
import glob,json,re,collections,os
fs=glob.glob(os.path.expanduser("~/.claude/projects")+"/C--projects-coding-governance*/**/subagents/workflows/**/*.jsonl",recursive=True)
c=collections.Counter(); ex={}
for p in fs:
    try: o=json.loads(open(p,encoding="utf-8").readline())
    except: continue
    m=o.get("message",{}).get("content"); s=m if isinstance(m,str) else json.dumps(m)
    for k in re.findall(r"(?m)^(?:LENS|Lens|YOUR LENS|Your lens)[^\n]{0,60}", s[:20000]):
        key=re.sub(r"[^a-z -]","",k.lower())[:40]; c[key]+=1; ex.setdefault(key,p)
print(len(fs)); print(c.most_common(40))
EOF
````

31. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S" && python - <<'EOF'
s=open("tx.py",encoding="utf-8").read()
old='''    if re.search(r"Coherence: ", first): return "lens:coherence"'''
new='''    if re.search(r"Coherence: ", first) or re.search(r"(?im)^(?:your )?lens\\W*(contradiction|underspecification|cross-unit|coherence)", first): return "lens:coherence"
    if re.search(r"(?im)^(?:your )?lens\\W*(prior[ -]?art|priorart|reuse)", first): return "lens:reuse"'''
assert old in s; s=s.replace(old,new); open("tx.py","w",encoding="utf-8").write(s)
EOF
python "$S/tx.py" 2>&1 | grep -v Warning
````

32. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S" && python - <<'EOF'
s=open("tx.py",encoding="utf-8").read()
old='''                        cmd = i.get("command", "")'''
new='''                        cmd = i.get("command", "")
                        for f in re.findall(r"[A-Za-z0-9_./-]+[.](?:md|py|js|json|toml|sh|txt)(?![A-Za-z])", cmd): dfiles.add(f.lower().split("/")[-1])'''
assert old in s; s=s.replace(old,new)
s=s.replace('''dfiles.add(i.get("file_path", "").lower().replace("\\\\", "/"))''','''dfiles.add(i.get("file_path", "").lower().replace("\\\\", "/").split("/")[-1])''')
open("tx.py","w",encoding="utf-8").write(s)
EOF
grep -n "dfiles.add" "$S/tx.py"; python "$S/tx.py" 2>&1 | grep -v Warning
````

33. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/reviews && ls -la | awk '{print $5, $9}' | tail -40
````

34. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/reviews && for f in 2026-10-17-review-PLAY-dClosedLoop-1-systems-retrofit.md 2026-10-16-review-PLAY-dClosedLoop-1-library.md 2026-10-17-review-PLAY-dClosedLoop-1-debt-folds.md; do echo "== $f"; grep -n "^#" $f | head -30; done
````

35. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/reviews && awk '/^## Appendix/{exit} /^### /{print; n=1; next} n && /^- \*\*(What|Consequence)/{print substr($0,1,600)}' 2026-10-17-review-PLAY-dClosedLoop-1-systems-retrofit.md
````

36. Bash

````text
git log --diff-filter=A --format='D %ad' --date=format:%Y-%m --name-only -- 'memory/builds/*/README.md' 'memory/map/features/*.md' 'tools/*/kit.toml' 'memory/gotchas/*.md' 'memory/guides/*.md' 'tools/roles/agents/*.agent.md' | python -c "
import sys,re,collections
c=collections.defaultdict(collections.Counter); d=None
for l in sys.stdin:
    l=l.strip()
    if l.startswith('D '): d=l[2:]; continue
    if not l: continue
    k='build' if l.endswith('README.md') and 'builds/' in l else 'feature' if 'features/' in l else 'kit' if l.endswith('kit.toml') else 'class' if 'gotchas/' in l else 'guide' if 'guides/' in l else 'role'
    c[d][k]+=1
cum=collections.Counter()
for m in sorted(c):
    cum.update(c[m]); print(m, dict(c[m]), 'cum', dict(cum))
"; git log --reverse --format=%ad --date=short | head -1
````

37. Bash

````text
grep -h "^opened:" memory/builds/*/README.md | cut -c9-15 | sort | uniq -c; for d in 2026-08-01 2026-08-15 2026-09-01 2026-09-15 2026-10-01 2026-10-17; do c=$(git rev-list -1 --before=$d HEAD); n=$(git show $c:tools/gate-legs.json 2>/dev/null | python -c "import json,sys;print(len(json.load(sys.stdin)))" 2>/dev/null); dr=$(git show $c:memory/DECISIONS.md 2>/dev/null | grep -cE "^- \**[A-Z]+-"); echo "$d legs=$n decisions=$dr"; done
````

38. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cat > "$S/tiers.py" <<'EOF'
"""Size a two-tier map: tier 0 holds every structural node one line each and folds each large population
into group lines; tier 1 is one namespace's full list. Reuses census.py's lines. Prints bytes per part."""
import runpy, sys, io, re, collections, json, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    g = runpy.run_path(sys.argv[1], run_name="census")
L = g["L"]; cut = g["cut"]
def short(lines, n):  # re-cut each line's purpose to n chars, drop the "- " and " — " decorations
    out = []
    for x in lines:
        m = re.match(r"- (\S+)(?: — (.*?))?(?: · (.*))?$", x)
        tag, p, ex = m.group(1), m.group(2) or "", m.group(3) or ""
        out.append(" ".join(s for s in (tag, cut(p, n) if n else "", ex) if s))
    return out
B = lambda ls: sum(len(x.encode()) + 1 for x in ls)
for n in (0, 40, 60, 90):
    flat = sum(B(short(v, n)) for v in L.values())
    print(f"flat, all {sum(len(v) for v in L.values())} nodes, purpose<={n}: {flat} B")
STRUCT = ["layer", "principle", "chain build", "build (live)", "feature", "kit", "skill", "role (today)", "guide"]
FOLD = {"build (closed)": lambda t: t.split(" · ")[-2] if " · " in t else "?",  # by node
        "gate leg": None, "harness hook": None, "git hook": None, "workflow script": None, "bug class": None,
        "decision row": lambda t: re.match(r"dec\.([A-Z]+)", t).group(1) if re.match(r"dec\.([A-Z]+)", t) else "?",
        "policy namespace": None, "gap area": None, "design record": None}
legs = json.load(open("tools/gate-legs.json", encoding="utf-8"))
for n in (40, 60):
    t0 = []
    for c in STRUCT: t0 += short(L[c], n)
    # items: one line per step with its item names only
    steps = collections.defaultdict(list)
    for x in L["item"]:
        tag = x.split()[1][5:]; steps[tag.split(".")[0]].append(tag.split(".", 1)[1])
    t0 += [f"step.{s} items {len(v)}: " + " ".join(v) for s, v in steps.items()]
    t0.append("policy " + " ".join(f"{x.split()[1][7:]}:{x.split()[-2]}" for x in L["policy namespace"]))
    t0.append("gap " + " ".join(f"{x.split()[1][4:]}:{x.split()[-2]}" for x in L["gap area"]))
    ch = collections.Counter(l["chunk"] for l in legs)
    t0.append(f"leg {len(legs)} by chunk: " + " ".join(f"{k}:{v}" for k, v in ch.items()))
    t0.append(f"hook harness {len(L['harness hook'])} git {len(L['git hook'])} · workflow {len(L['workflow script'])}")
    t0.append(f"class {len(L['bug class'])} → gov map class")
    fam = collections.Counter(re.match(r"- dec\.([A-Z]+)", x).group(1) for x in L["decision row"])
    t0.append("decision " + " ".join(f"{k}:{v}" for k, v in fam.items()) + " (major: not yet routed)")
    nodes = collections.Counter(x.split(" · node ")[1].split(" ")[0] for x in L["build (closed)"])
    t0.append(f"build closed {len(L['build (closed)'])} by node: " + " ".join(f"{k}:{v}" for k, v in nodes.items()))
    t0.append(f"rec dClosedLoop {len(L['design record'])} records")
    t0.append("record-kind (designed, ~37) · tag-ns 25 · point 10 — not yet derivable")
    print(f"tier 0, purpose<={n}: {len(t0)} lines {B(t0)} B; structural lines {sum(len(L[c]) for c in STRUCT)}")
    if n == 60 and "--print" in sys.argv: print("\n".join(t0))
for c in ("gate leg", "bug class", "build (closed)", "decision row", "item", "design record"):
    print(f"tier 1 slice {c}: {len(L[c])} lines {B(short(L[c], 60))} B")
EOF
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python "$S/tiers.py" "$S/census.py"
````

39. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; sed -i 's/fam = collections.Counter(re.match(r"- dec\\.(\[A-Z\]+)", x).group(1) for x in L\["decision row"\])/fam = collections.Counter((re.match(r"- dec\\.([A-Z]+)", x) or re.match("(.)", "?")).group(1) for x in L["decision row"])/' "$S/tiers.py"; grep -n "fam =" "$S/tiers.py"; cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python "$S/tiers.py" "$S/census.py" --print
````

40. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S" && python - <<'EOF'
s=open("tiers.py",encoding="utf-8").read()
s=s.replace('fam = collections.Counter(re.match(r"- dec\\.([A-Z]+)", x).group(1) for x in L["decision row"])',
 'fam = collections.Counter(re.findall(r"dec\\.([A-Z]+)", x)[0] if re.findall(r"dec\\.([A-Z]+)", x) else "?" for x in L["decision row"])')
open("tiers.py","w",encoding="utf-8").write(s)
EOF
grep -n "fam =" "$S/tiers.py"; cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python "$S/tiers.py" "$S/census.py" --print
````

41. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; sed -i 's/^for n in (40, 60):/for n in (0, 30, 40, 60):/' "$S/tiers.py"; cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python "$S/tiers.py" "$S/census.py" | grep "tier 0"
````

42. Bash

````text
grep -n -c "gate-legs\|kit.toml\|gotchas\|map/features\|LIVE.md" memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py; grep -rn "MAP.md\|CARDS.md" --include=*.md --include=*.js --include=*.sh --include=*.py --include=*.json skills .claude tools/hooks tools/roles AGENTS.md CLAUDE.md coding-governance-agents.template.md 2>/dev/null | grep -v "^tools/codebase-map" | head; ls gov 2>/dev/null; grep -rln "def.*tag_show\|gov tag" tools | head
````

43. Bash

````text
grep -n "def render_cards_md\|CARD_BYTES\|1024\|def render_map_md\|def compute_coverage\|def owners_of" tools/codebase-map/map_lib.py | head; grep -n "TASK_FIELDS\s*=" -A14 tools/roles/handoff.py | head -24; grep -n "def render_live\|LIVE.md" tools/memory-tree/gen_build_index.py | head -5; grep -n "routing\|def render_readme_region" tools/memory-tree/gen_build_index.py | head -5
````

44. Bash

````text
cd /c/projects/coding-governance && ls -la .git/orientation 2>/dev/null | head -5; ls .git/orientation 2>/dev/null | wc -l; find .git/orientation -name '*.md' -size +0 2>/dev/null | xargs wc -c 2>/dev/null | sort -n | awk '{a[NR]=$1} END{print "n="NR-1, "median="a[int(NR/2)], "max="a[NR-1]}'; wc -c .claude/worktrees/gov-architecture-plan-e34297/tools/roles/agents/gov-orienter.agent.md; grep -n "read\|README" .claude/worktrees/gov-architecture-plan-e34297/tools/roles/agents/gov-orienter.agent.md | head -8
````

45. Bash

````text
grep -n "^| gap-" memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md | grep -i "map\|whole\|glance\|overview\|orient\|view\|load\|over-read\|read list\|exists" | cut -c1-260 | head -30
````

46. Bash

````text
grep -n "^| gap-mem-\|^| gap-design-0[2-9]\|^| gap-maint-0[1-5]" memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md | cut -c1-230
````

47. Bash

````text
ls tools/workflows/ | head -30; sed -n 1,20p tools/workflows/review_replay.py 2>/dev/null
````

48. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cat > "$S/per_call.py" <<'EOF'
"""Median bytes per tool result by call kind (Read, search, other) for the PM-1 roles' transcripts."""
import json, glob, os, re, statistics as st, collections
root = os.path.expanduser("~/.claude/projects")
ROLE = re.compile(r"role=(gov-spec-writer|gov-spec-reviewer|gov-reuse-scout|gov-orienter)|(?im)^(?:your )?lens\W*(contradiction|underspecification|cross-unit|coherence|prior[ -]?art|priorart|reuse)")
sizes = collections.defaultdict(list)
for p in glob.glob(root + "/C--projects-coding-governance*/**/subagents/**/*.jsonl", recursive=True):
    lines = open(p, encoding="utf-8").readlines()
    if not lines: continue
    c0 = json.loads(lines[0]).get("message", {}).get("content"); s0 = c0 if isinstance(c0, str) else json.dumps(c0)
    if not ROLE.search(s0[:20000]): continue
    kind = {}
    for l in lines:
        c = (json.loads(l).get("message") or {}).get("content")
        if not isinstance(c, list): continue
        for b in c:
            if b.get("type") == "tool_use":
                n = b["name"]; cmd = b.get("input", {}).get("command", "")
                kind[b["id"]] = "read" if n == "Read" or re.search(r"\b(cat|sed -n|head|tail)\b", cmd) else "search" if n in ("Grep", "Glob") or re.search(r"\b(grep|rg|find|ls)\b", cmd) else "other"
            elif b.get("type") == "tool_result" and b.get("tool_use_id") in kind:
                cc = b.get("content"); sizes[kind[b["tool_use_id"]]].append(len((cc if isinstance(cc, str) else json.dumps(cc)).encode()))
for k, v in sizes.items(): print(k, "calls", len(v), "median B", int(st.median(v)), "mean B", int(st.mean(v)))
EOF
python "$S/per_call.py"
````

49. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; sed -i 's/ROLE = re.compile(r"role=/ROLE = re.compile(r"(?im)role=/; s/|(?im)^(?:your )?lens/|^(?:your )?lens/' "$S/per_call.py"; python "$S/per_call.py"
````
