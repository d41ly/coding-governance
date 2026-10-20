# Research: the memory layer's probe scripts

**Serves:** research PLAY-dClosedLoop-1

The five memory researchers wrote their probes outside the repository, in scratch directories, and
cited them from their returns. This record keeps them beside the returns. They are kept as fenced
text, not as `.py` files, because the lexicon gate grades every tracked Python file.

Every probe reads. None was run again for this record.

## Dispatch 22: builds

Its return is `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-builds.md`.

### `kinds.py`

```python
import os,re,statistics,sys
root=sys.argv[1]
kinds={}
for b in os.listdir(root):
  for dp,dn,fn in os.walk(os.path.join(root,b)):
    rel=os.path.relpath(dp,os.path.join(root,b)).replace(os.sep,'/')
    for f in fn:
      sz=os.path.getsize(os.path.join(dp,f))
      if rel=='.':
        k=f
        if re.match(r'RUN\.(LANDED|ABORTED)\.',f): k='RUN.<state>.<sha>.md'
      else:
        k=rel+'/*'+os.path.splitext(f)[1]
      kinds.setdefault(k,[]).append((b,sz))
def p(xs,q):
  xs=sorted(xs); i=min(len(xs)-1,int(round(q*(len(xs)-1)))); return xs[i]
for k,v in sorted(kinds.items(),key=lambda x:-len(x[1])):
  s=[x[1] for x in v]; bs=len(set(x[0] for x in v))
  print(f"{k:28} files={len(v):5} builds={bs:4} med={int(statistics.median(s)):7} p90={p(s,.9):7} total={sum(s)}")
```

### `fm.py`

```python
import os,re,collections,glob,sys
root='memory/builds'
keys=collections.Counter(); regions=collections.Counter(); heads=collections.Counter(); parents=[]
nfm=0
for b in sorted(os.listdir(root)):
  p=os.path.join(root,b,'README.md')
  if not os.path.exists(p): continue
  L=open(p,encoding='utf-8').read().split('\n')
  if L[0].strip()=='---':
    nfm+=1
    for l in L[1:]:
      if l.strip()=='---': break
      if ':' in l: k,_,v=l.partition(':'); keys[k.strip()]+=1
      if l.startswith('parents:'): parents.append((b,v.strip()))
  t='\n'.join(L)
  for r in re.findall(r'<!-- gen:([a-z-]+) -->',t): regions[r]+=1
  for h in re.findall(r'^## (.+)$',t,re.M): heads[h.strip()]+=1
print('READMEs with fm',nfm); print('keys',dict(keys)); print('regions',dict(regions))
print('top headings',heads.most_common(14))
print('parents decl',len(parents),parents[:40])
```

### `rel.py`

```python
import os,re,collections
root='memory/builds'
c=collections.Counter(); b=collections.defaultdict(set)
pats={'serves':r'^\**Serves:\**','commissions':r'^\**Commissions:\**','edges_hdr':r'^### Edges','consumes-from':r'\*\*consumes-from\*\*','hands-off':r'\*\*hands-off\*\*',
 'order_verb':r'^\*\*Status:\*\*.*· order \d','closes_verb':r'^\*\*Status:\*\*.*· closes ','advances_verb':r'^\*\*Status:\*\*.*· advances ',
 'supersedes_word':r'(?i)\bsupersed','amends_word':r'(?i)\bamend','patch_word':r'(?i)\bpatch(es)? (of|to) ','rev_gt1_hdr':r'^\*\*Status:\*\* \S+ · rev-([2-9]|\d\d)'}
for bd in os.listdir(root):
  for dp,dn,fn in os.walk(os.path.join(root,bd)):
    for f in fn:
      if not f.endswith('.md'): continue
      sub=os.path.relpath(dp,os.path.join(root,bd)).split(os.sep)[0]
      t=open(os.path.join(dp,f),encoding='utf-8',errors='replace').read()
      for k,p in pats.items():
        n=len(re.findall(p,t,re.M))
        if n: c[(k,sub)]+=1; b[k].add(bd)
for k in pats: print(f"{k:16} builds={len(b[k]):4} files="+str({s:n for (kk,s),n in c.items() if kk==k}))
```

### `reads.py`

```python
import os,re,json,glob,collections,sys
home=os.path.expanduser('~')
files=glob.glob(os.path.join(home,'.claude','projects','C--projects-coding-governance*','**','*.jsonl'),recursive=True)
BR=re.compile(r'memory/+builds/+([A-Za-z0-9]+)(?:/+(.*))?$')
pending={}
rows=[]  # (session_kind, slug, rel, bytes, partial)
nsess=collections.Counter()
for f in files:
  kind='subagent' if 'subagents' in f else 'session'
  nsess[kind]+=1
  pend={}
  try:
    fh=open(f,encoding='utf-8',errors='replace')
  except: continue
  for line in fh:
    if 'memory' not in line or 'builds' not in line: continue
    try: o=json.loads(line)
    except: continue
    msg=o.get('message') or {}
    c=msg.get('content')
    if not isinstance(c,list): continue
    for it in c:
      if not isinstance(it,dict): continue
      if it.get('type')=='tool_use' and it.get('name')=='Read':
        p=(it.get('input') or {}).get('file_path','')
        m=BR.search(p.replace(chr(92),'/'))
        if m and m.group(2):
          pend[it.get('id')]=(m.group(1),m.group(2).replace(chr(92),'/'),bool((it.get('input') or {}).get('offset') or (it.get('input') or {}).get('limit')))
      elif it.get('type')=='tool_result' and it.get('tool_use_id') in pend:
        s,r,part=pend.pop(it['tool_use_id'])
        cc=it.get('content'); 
        if isinstance(cc,list): cc=''.join(x.get('text','') for x in cc if isinstance(x,dict))
        rows.append((kind,s,r,len((cc or '').encode('utf-8')),part))
def cls(r):
  if r=='README.md': return 'README'
  if r in('BACKLOG.md','RUN.md'): return r
  if r.startswith('RUN.'): return 'RUN.<state>'
  return r.split('/')[0]+'/'
print('jsonl files',dict(nsess),'build-folder Reads',len(rows))
for kind in ('session','subagent','all'):
  R=[x for x in rows if kind=='all' or x[0]==kind]
  if not R: continue
  agg=collections.defaultdict(lambda:[0,0])
  for x in R: a=agg[cls(x[2])]; a[0]+=1; a[1]+=x[3]
  tot=sum(a[0] for a in agg.values()); totb=sum(a[1] for a in agg.values())
  print(f'-- {kind}: reads={tot} bytes={totb}')
  for k,a in sorted(agg.items(),key=lambda x:-x[1][0]): print(f'   {k:12} n={a[0]:6} ({100*a[0]/tot:5.1f}%) bytes={a[1]:11} ({100*a[1]/totb:5.1f}%)')
cnt=collections.Counter((x[1],x[2]) for x in rows if x[2]!='README.md')
print('top non-README files:')
for (s,r),n in cnt.most_common(12): print(f'   {n:4} {s}/{r}')
# per (transcript) did reader go past README?
```

### `route.py`

```python
import os,re,json,glob,collections
home=os.path.expanduser('~')
files=glob.glob(os.path.join(home,'.claude','projects','C--projects-coding-governance*','**','*.jsonl'),recursive=True)
BR=re.compile(r'memory/+builds/+([A-Za-z0-9]+)/+(.+)$')
pairs=collections.Counter(); bashreads=0
for f in files:
  seq=[]
  for line in open(f,encoding='utf-8',errors='replace'):
    if 'builds' not in line: continue
    try:o=json.loads(line)
    except:continue
    c=(o.get('message') or {}).get('content')
    if not isinstance(c,list):continue
    for it in c:
      if isinstance(it,dict) and it.get('type')=='tool_use':
        inp=it.get('input') or {}
        if it.get('name')=='Read':
          m=BR.search(inp.get('file_path','').replace(chr(92),'/'))
          if m: seq.append((m.group(1),m.group(2)))
        elif it.get('name')=='Bash' and re.search(r'\b(cat|sed -n|head|tail)\b[^|;]*memory/builds/',inp.get('command','')): bashreads+=1
  per=collections.defaultdict(list)
  for s,r in seq: per[s].append(r)
  for s,rs in per.items():
    other=[r for r in rs if r!='README.md']
    if not other: pairs['README only']+=1
    elif 'README.md' not in rs: pairs['other files, README never read']+=1
    elif rs[0]=='README.md': pairs['README first, then other']+=1
    else: pairs['other first, README later']+=1
print('(transcript,build) pairs:',dict(pairs),'total',sum(pairs.values()))
print('Bash cat/sed/head/tail calls naming a build path (not counted above):',bashreads)
```

### `bashr.py`

```python
import os,re,json,glob,collections
home=os.path.expanduser('~')
files=glob.glob(os.path.join(home,'.claude','projects','C--projects-coding-governance*','**','*.jsonl'),recursive=True)
P=re.compile(r'memory/builds/([A-Za-z0-9*]+)/([A-Za-z0-9_.*/-]+)')
c=collections.Counter()
for f in files:
  for line in open(f,encoding='utf-8',errors='replace'):
    if 'memory/builds/' not in line: continue
    try:o=json.loads(line)
    except:continue
    cc=(o.get('message') or {}).get('content')
    if not isinstance(cc,list):continue
    for it in cc:
      if isinstance(it,dict) and it.get('type')=='tool_use' and it.get('name')=='Bash':
        cmd=(it.get('input') or {}).get('command','')
        if not re.search(r'\b(cat|sed -n|head|tail)\b',cmd): continue
        for s,r in P.findall(cmd):
          k='README' if r=='README.md' else r.split('/')[0]+('/' if '/' in r else '')
          c[k]+=1
print(c.most_common(10))
```

### `derive.py`

```python
import os,sys,re
sys.path.insert(0,'tools/memory-tree'); sys.dont_write_bytecode=True
import gen_build_index as g
fam2d={'PLAY':'playbook','KICK':'kickoff','TOOL':'tooling','DEPL':'deployer'}
n=nodeok=rosterok=streamsok=0; bad=[]
for b in sorted(os.listdir('memory/builds')):
  p=f'memory/builds/{b}/README.md'
  if not os.path.exists(p): continue
  fm=g.parse_front_matter(p,b); n+=1
  nodeok+= fm['node']==b[0]
  ids=fm['ids'].split(); fams=sorted({i.split('-')[0] for i in ids})
  r=set(fm['roster'].replace('+',' ').split()); s=set(fm['streams'].replace('+',' ').split())
  if ids:
    rosterok+= r==set(fams); streamsok+= s=={fam2d.get(f,f) for f in fams}
print(f'READMEs={n} node==slug[0]: {nodeok}  roster==families(ids): {rosterok}  streams==disciplines(ids): {streamsok}')
open(os.path.join(sys.argv[1],'typo.md'),'w').write('---\nslug: zTypo\nnode: z\nopened: 2026-10-15\nstreams: tooling\nroster: TOOL\nids:\nparent: aGhostBuild\n---\n')
fm=g.parse_front_matter(os.path.join(sys.argv[1],'typo.md'),'zTypo'); print('typo key accepted silently:', 'parent' in fm, '| parents parsed:', fm.get('parents'))
```

### `blast.py`

```python
import re
slugs=['dClosedLoop','dLoop','dClosedLoopTwo','d20261015ClosedLoop','dClosedLoop20261015','d2026-10-15ClosedLoop']
R={
 'backlog.py:129 SLUG_RE':(r'^(?=.*[A-Z])[A-Za-z0-9]+$','s'),
 'roles_lib.py:75 SLUG_RE':(r'^[A-Za-z]+$','s'),
 'hygiene.sh:818 check4 default':(r'^[A-Za-z][A-Za-z0-9-]*$','s'),
 'tier2-review.js:296 reviewSlug':(r'^[A-Za-z]+$','s'),
 'handoff.py:104 UNIT_RE':(r'^[A-Z]+-([A-Za-z]+)-[0-9]+$','i'),
 'hygiene.sh:885 check5 record':(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}-spec-((PLAY|TOOL)-)?[A-Za-z0-9]+-[0-9]+\.md$','f'),
 'gen_build_index.py:603 Serves id':(r'^(PLAY|TOOL)-(?P<slug>[A-Za-z0-9]+)-(?P<seq>\d+)$','i'),
 'memory-recall extract.py:160 ERA':(r'^(PLAY|TOOL)-[abcd][A-Za-z]{2,}-\d+[a-z]*$','i'),
 'check-pass-order.sh:227':(r'^[A-Z]+-[A-Za-z]+-[0-9]+$','i'),
 'push-main.sh:583':(r'^[A-Z][A-Z]+-([A-Za-z]+)-[0-9]+:','c'),
 'lib-unattended.sh:1467':(r'^[A-Z]+-[A-Za-z0-9]+-[0-9]+$','i'),
}
print('reader'.ljust(36),' '.join(s[:12].ljust(12) for s in slugs))
for k,(p,mode) in R.items():
  row=[]
  for s in slugs:
    x={'s':s,'i':f'PLAY-{s}-1','f':f'2026-10-15-spec-PLAY-{s}-1.md','c':f'PLAY-{s}-1: msg'}[mode]
    row.append(('ok' if re.search(p,x) else 'REJECT').ljust(12))
  print(k.ljust(36),' '.join(row))
```

### `derived.py`

```python
import os,re,collections
root='memory/builds'; slugs=set(os.listdir(root))
ID=re.compile(r'\b(?:PLAY|KICK|TOOL|DEPL)-([A-Za-z0-9]+)-\d+')
cites=collections.defaultdict(collections.Counter)
for b in slugs:
  for dp,dn,fn in os.walk(os.path.join(root,b)):
    for f in fn:
      if not f.endswith('.md'): continue
      for s in ID.findall(open(os.path.join(dp,f),encoding='utf-8',errors='replace').read()):
        if s!=b and s in slugs: cites[b][s]+=1
declared=[('aHoistedPass','dBriefedPass'),('aHoistedPass','dRatifiedSeam'),('aJoinedCanon','aWeighedCanon'),('aPooledSweep','aQuenchedHarness'),('aProbedUnit','aRatifiedRulings'),('aQuenchedHarness','aBoundedCeiling'),('aRatifiedRulings','aLeakedHandle'),('aSparedSpawn','aMeteredSweep'),('aStagedLane','dBriefedPass'),('aTunedCompass','aWeighedCompass'),('aWokenSentinel','aPrimedKeepalive'),('aWokenSentinel','aProbedUnit'),('dHonouredPark','dFramedEntrypoint')]
rec=sum(1 for c,p in declared if cites[c][p]>0)
ranks=[sorted(cites[c].values(),reverse=True).index(cites[c][p])+1 if cites[c][p] else None for c,p in declared]
edges=sum(len(v) for v in cites.values())
print(f'declared edges recovered by any citation: {rec}/{len(declared)}; rank of parent among child cites: {ranks}')
print(f'derived cross-build citation edges: {edges} over {sum(1 for v in cites.values() if v)} citing builds; mean out-degree {edges/max(1,sum(1 for v in cites.values() if v)):.1f}')
```

## Dispatch 23: the ask register and the decision index

Its return is `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-asks-decisions.md`.

### `map.txt`

```text
10:5 11:4 12:1 16:2 17:3 18:5 22:3 23:5 24:6 25:2 26:5 27:5 28:5 29:6 30:6 31:6 33:4 34:3 35:5 36:5 37:6 38:5 39:4 40:4
41:1 42:2 43:6 44:2 45:5 46:3 47:3 48:6 49:5 50:6 51:6 52:6 53:6 54:6 55:6 56:6 58:2 59:6 60:3 61:6 62:2 64:5 65:6 66:6 67:6 69:6
70:5 71:6 72:3 73:5 74:5 75:5 76:5 78:5 79:6 81:3 83:5 84:4 85:4 86:4 87:5 88:5 89:6 90:6 91:1 92:5 93:5 94:5 95:4 97:5 98:2 99:6
101:5 103:1 104:5 105:2 106:6 107:6 108:4 109:4 110:1 111:4 112:4 113:4 114:4 115:4 116:5 117:2 118:3 119:1 120:5 121:4 122:1 123:5 124:2 125:5 126:5 127:4 128:4 129:4 130:4 131:4 132:1 133:4 134:4 135:4 136:1 137:4 138:5
143:6 144:5 145:5 146:5 147:3 148:1 149:6 150:4 151:6 152:5 153:5 154:5 155:4 156:6 157:6 158:6 159:4 160:4 161:4 162:4 163:4 164:4 165:5 166:6 167:2 168:6 169:6
170:5 171:6 172:1 173:6 174:6 175:4 176:4 177:4 178:1 179:5 180:6 181:6 182:4 183:3 184:5 185:5 186:6 187:6 188:3 189:6 190:6 191:6 192:6 193:5 194:5 195:5 196:6 197:5 198:5 199:6
200:5 201:5 202:5 203:5 204:6 205:5 206:5 207:6 208:6 209:1 210:3 211:3 212:3 213:5 214:5 215:1 216:4 217:3 218:5 219:4 220:4 221:4 222:4 223:4 224:4 225:2 226:4 227:4 228:4 229:1
```

### `tally.py`

```python
import re,sys,collections
m=dict(tuple(map(int,t.split(':'))) for t in open(sys.argv[1]).read().split())
rows={i+1:l for i,l in enumerate(open(sys.argv[2],encoding='utf-8')) if l.startswith('- ')}
print('rows',len(rows),'mapped',len(m),'unmapped',sorted(set(rows)-set(m)),'extra',sorted(set(m)-set(rows)))
idre=re.compile(r'\b((?:PLAY|KICK|TOOL|DEPL)-[A-Za-z0-9]+-\d+)')
by=collections.defaultdict(list)
for ln,c in sorted(m.items()): by[c].append(idre.search(rows[ln]).group(1))
names={1:'waiver/exception',2:'major product',3:'feature/convention to reuse',4:'owner ruling on fork',5:'process/tooling rule',6:'minor/finding'}
for c in sorted(by): print(c,names[c],len(by[c]),by[c][:2])
# field measurements
date=re.compile(r'20\d\d-\d\d-\d\d'); slug=re.compile(r'builds/[A-Za-z]+'); code=re.compile(r'`[^`]*(?:/|\.(?:py|sh|js|md|json|toml))[^`]*`|tools/|\.py\b|\.sh\b|\.js\b')
reuse=re.compile(r'\b(reuse|use this|must use|instead of (re)?building|integrat)',re.I)
own=re.compile(r'\bowner\b|OWNER RULING',re.I)
sup=re.compile(r'supersed|reverse|narrow|amend',re.I)
for nm,rx in [('date',date),('builds/ slug path',slug),('code ref',code),('reuse instruction',reuse),('owner',own),('supersedes/reverses/narrows/amends',sup)]:
  print(nm,sum(1 for l in rows.values() if rx.search(l)))
ids=[idre.search(l).group(1) for l in rows.values()]
print('dup ids',[k for k,v in collections.Counter(ids).items() if v>1])
print('bytes/row median',sorted(len(l.encode()) for l in rows.values())[len(rows)//2])
```

## Dispatch 24: the codebase map and the reuse tools

Its return is `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-map-reuse.md`.

### `count.py`

```python
import ast, json, re, subprocess, sys, collections
root = sys.argv[1]
files = subprocess.run(["git","-C",root,"ls-files"],capture_output=True,text=True).stdout.split("\n")
prod = [f for f in files if f and not f.startswith("memory/")]
c = collections.Counter()
for f in prod:
    if not f.endswith(".py"): continue
    t = ast.parse(open(f"{root}/{f}",encoding="utf-8").read())
    top = set(id(n) for n in t.body)
    for n in ast.walk(t):
        if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
            k = "class" if isinstance(n,ast.ClassDef) else "func"
            scope = "top" if id(n) in top else "nested/method"
            priv = "priv" if n.name.startswith("_") else "pub"
            c[(k,scope,priv)] += 1
    for n in ast.walk(t):
        if isinstance(n,ast.Call): c["py-call-sites"] += 1
for k,v in sorted(c.items(), key=str): print("py",k,v)
# shell: function defs by regex (name() { or function name)
rx = re.compile(r"^\s*(?:function\s+)?([A-Za-z_][\w:-]*)\s*\(\s*\)\s*\{?|^\s*function\s+([A-Za-z_][\w:-]*)\s*\{", re.M)
sc=collections.Counter()
for f in prod:
    if f.endswith(".sh") or (f.startswith(".githooks/") and "." not in f.split("/")[-1]):
        for m in rx.finditer(open(f"{root}/{f}",encoding="utf-8").read()):
            n=m.group(1) or m.group(2); sc["priv" if n.startswith("_") else "pub"]+=1
print("sh(regex, incl heredoc bodies)",dict(sc))
jc=collections.Counter()
jrx=[re.compile(r"^\s*(?:export\s+)?(?:async\s+)?function\s*\*?\s*([A-Za-z_$][\w$]*)",re.M),
     re.compile(r"^\s*(?:export\s+)?class\s+([A-Za-z_$][\w$]*)",re.M),
     re.compile(r"^\s*(?:export\s+)?(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?(?:function\b|\([^)]*\)\s*=>|[A-Za-z_$][\w$]*\s*=>)",re.M)]
for f in prod:
    if f.endswith(".js"):
        s=open(f"{root}/{f}",encoding="utf-8").read()
        for r in jrx: jc[f.split("/")[1] if f.count("/")>1 else f]+=len(r.findall(s))
print("js defs (any indent) by kit",dict(jc), "total",sum(jc.values()))
sym=json.load(open(f"{root}/memory/map/generated/symbols.json",encoding="utf-8"))["symbols"]
sk=collections.Counter((s["file"].rsplit(".",1)[-1] if "." in s["file"].split("/")[-1] else "noext", s["kind"]) for s in sym)
print("symbols.json rows",len(sym),dict(sk))
print("symbols.json keys", set(k for s in sym for k in s))
```

### `graph.py`

```python
import ast, sys, subprocess, collections, time, re
root = sys.argv[1]; sys.path.insert(0, root + "/tools/lexicon")
sys.dont_write_bytecode = True
from lexicon import parse_shell_defs, scan_shell_tokens, scan_ts_tokens, parse_ts_defs
t0 = time.time()
files = [f for f in subprocess.run(["git","-C",root,"ls-files"],capture_output=True,text=True).stdout.split("\n")
         if f and not f.startswith("memory/")]
defs = collections.defaultdict(set)   # name -> {file}
pycalls = []; shcalls = []; jscalls = []
mods = collections.defaultdict(set)
for f in files:
    if f.endswith(".py"): mods[f.rsplit("/",1)[-1][:-3]].add(f)
# --- python
for f in files:
    if not f.endswith(".py"): continue
    tree = ast.parse(open(f"{root}/{f}",encoding="utf-8").read())
    for n in ast.walk(tree):
        if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)): defs[n.name].add(f)
    for n in ast.walk(tree):
        if isinstance(n, ast.Call):
            fn = n.func
            name = fn.id if isinstance(fn, ast.Name) else (fn.attr if isinstance(fn, ast.Attribute) else None)
            recv = fn.value.id if isinstance(fn, ast.Attribute) and isinstance(fn.value, ast.Name) else None
            if name: pycalls.append((f, name, recv))
# --- shell
shfiles = [f for f in files if f.endswith(".sh") or (f.startswith(".githooks/") and "." not in f.rsplit("/",1)[-1])]
shfail = 0
for f in shfiles:
    src = open(f"{root}/{f}",encoding="utf-8").read()
    try:
        fns = parse_shell_defs(src)[0]; toks = scan_shell_tokens(src)
    except SyntaxError: shfail += 1; continue
    for name,_ in fns: defs[name].add(f)
    for kind, text, line in toks:
        if kind == "word": shcalls.append((f, text))
# --- js
jsfail = 0
for f in files:
    if not f.endswith(".js"): continue
    src = open(f"{root}/{f}",encoding="utf-8").read()
    try:
        fns = parse_ts_defs(src)[0]; calls=set(); toks = scan_ts_tokens(src, calls=calls)
    except Exception as e: jsfail += 1; continue
    for d in fns: defs[d[0] if isinstance(d,(tuple,list)) else d].add(f)
    for i in calls:
        if i>0 and toks[i-1][0]=="word": jscalls.append((f, toks[i-1][1]))
t1 = time.time()
def grade(calls, lang):
    c = collections.Counter(); edges=set()
    for row in calls:
        f, name = row[0], row[1]
        d = defs.get(name)
        if not d: c["to-no-repo-def"] += 1; continue
        if f in d: c["same-file"] += 1; edges.add((f,name,f)); continue
        if len(d) == 1: c["unique-cross-file"] += 1; edges.add((f,name,next(iter(d))))
        else: c["ambiguous(>1 definer)"] += 1
    print(lang, "call-sites", len(calls), dict(c), "edges", len(edges))
    return c
grade(pycalls, "py"); grade(jscalls, "js")
shwords = [(f,w) for f,w in shcalls if w in defs and any(x.endswith(('.sh',)) or '.githooks/' in x for x in defs[w])]
grade(shwords, "sh(word==defined fn)")
homo = sum(1 for n,s in defs.items() if len(s)>1)
print("distinct def names", len(defs), "names with >1 definer", homo, "shfail", shfail, "jsfail", jsfail)
# cross-language: script invocations
inv = collections.Counter()
rx = re.compile(r"(?:bash|sh|python3?|py|node|\$PY|\"\$PY\")\s+[\"']?[\w./${}-]*?([\w-]+\.(?:sh|py|js))")
for f in files:
    if f.endswith((".sh",".py",".js",".json",".yml")) or f.startswith(".githooks/"):
        for m in rx.finditer(open(f"{root}/{f}",encoding="utf-8",errors="replace").read()): inv[f.rsplit('.',1)[-1] if '.' in f.rsplit('/',1)[-1] else 'hook'] += 1
print("script-invocation sites (interp + path) by caller ext", dict(inv))
print("parse s %.1f total s %.1f" % (t1-t0, time.time()-t0))
```

### `pyimp.py`

```python
import ast, sys, subprocess, collections, time
root=sys.argv[1]; t0=time.time()
files=[f for f in subprocess.run(["git","-C",root,"ls-files","*.py"],capture_output=True,text=True).stdout.split() if not f.startswith("memory/")]
stem=collections.defaultdict(set)
for f in files: stem[f.rsplit("/",1)[-1][:-3]].add(f)
topdefs=collections.defaultdict(set)
trees={}
for f in files:
    t=ast.parse(open(f"{root}/{f}",encoding="utf-8").read()); trees[f]=t
    for n in t.body:
        if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)): topdefs[f].add(n.name)
c=collections.Counter(); edges=set(); callers=collections.Counter()
for f,t in trees.items():
    d=f.rsplit("/",1)[0]
    alias={}; frm={}
    for n in ast.walk(t):
        if isinstance(n,ast.Import):
            for a in n.names: alias[a.asname or a.name]=a.name
        elif isinstance(n,ast.ImportFrom) and n.module:
            for a in n.names: frm[a.asname or a.name]=(n.module,a.name)
    def mod_file(mod):
        cands=stem.get(mod.split(".")[-1],set())
        same=[x for x in cands if x.rsplit("/",1)[0]==d]   # sys.path.insert(kit dir) convention
        return same[0] if len(same)==1 else (next(iter(cands)) if len(cands)==1 else ("AMBIG" if cands else None))
    for n in ast.walk(t):
        if not isinstance(n,ast.Call): continue
        fn=n.func
        if isinstance(fn,ast.Name):
            if fn.id in topdefs[f]: c["local"]+=1; edges.add((f,fn.id,f)); continue
            if fn.id in frm:
                tf=mod_file(frm[fn.id][0])
                if tf=="AMBIG": c["from-import ambiguous"]+=1
                elif tf: c["from-import resolved"]+=1; edges.add((f,frm[fn.id][1],tf)); callers[(tf,frm[fn.id][1])]+=1
                else: c["external"]+=1
                continue
            c["builtin/other"]+=1
        elif isinstance(fn,ast.Attribute) and isinstance(fn.value,ast.Name) and fn.value.id in alias:
            tf=mod_file(alias[fn.value.id])
            if tf=="AMBIG": c["mod.attr ambiguous"]+=1
            elif tf: c["mod.attr resolved"]+=1; edges.add((f,fn.attr,tf)); callers[(tf,fn.attr)]+=1
            else: c["external"]+=1
        else: c["method/dynamic (unresolved)"]+=1
print(dict(c)); print("resolved edges",len(edges),"cross-file edges",sum(1 for e in edges if e[0]!=e[2]))
print("top callee by cross-file call sites",callers.most_common(5))
print("seconds %.1f"%(time.time()-t0))
```

## Dispatch 25: code annotations, the gotchas and the lexicon

Its return is `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-annotations.md`.

### `census.py`

```python
import ast, io, os, re, subprocess, sys, tokenize, collections, json
root = sys.argv[1]; os.chdir(root)
files = subprocess.run(["git","ls-files","tools","skills",".githooks"],capture_output=True,text=True).stdout.split()
LANG = {".py":"py",".sh":"sh",".js":"js",".toml":"toml",".conf":"conf",".txt":"txt"}
def lang(f):
    if f.startswith(".githooks/") and "." not in os.path.basename(f): return "sh"
    return LANG.get(os.path.splitext(f)[1])
FAM = r"[A-Z]{2,5}"
ID = re.compile(r"\b"+FAM+r"-(?:\d{3}|[a-z]\d{2,3}|[a-z][A-Za-z]{2,}-\d+[a-z]*)\b")
TAGNS = re.compile(r"\b(?:level|layer|step|item|role|policy|practice|principle|kind|record|kit):[a-z][\w-]*")
CHTAG = re.compile(r"\[(?:reuse|verify|class|memory|land|scope|probe|spec|review|test|ids|records)\]")
MEMPTR = re.compile(r"\bmemory/[\w./<>-]+")
FILEPTR = re.compile(r"(?<![\w])(?:[\w.-]+/)*[\w.-]+\.(?:md|py|sh|js|json|toml|conf|txt)\b")
SECT = re.compile(r"§\s?[A-Z]?\d|\b[A-Z]\d{1,2}\b(?= of| in)|\bU\d+\b")
DIR = re.compile(r"\b(?:MUST|NEVER|MUST NOT|SHALL)\b")
GOV = re.compile(r"\bgov:[a-z]")
def comments(f, lg):
    try: src = open(f,encoding="utf-8").read()
    except Exception: return []
    out=[]
    if lg=="py":
        try:
            for t in tokenize.generate_tokens(io.StringIO(src).readline):
                if t.type==tokenize.COMMENT and not (t.start[0]==1 and t.string.startswith("#!")):
                    out.append((t.start[0],t.string,"#"))
        except Exception: pass
        try:
            tree=ast.parse(src)
            for n in ast.walk(tree):
                if isinstance(n,(ast.Module,ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) and n.body and isinstance(n.body[0],ast.Expr) and isinstance(getattr(n.body[0],'value',None),ast.Constant) and isinstance(n.body[0].value.value,str):
                    e=n.body[0]; lines=src.splitlines()[e.lineno-1:e.end_lineno]
                    for i,l in enumerate(lines): out.append((e.lineno+i,l,"doc"))
        except Exception: pass
    elif lg=="js":
        inb=False
        for i,l in enumerate(src.splitlines(),1):
            s=l.strip()
            if inb:
                out.append((i,l,"/*"));
                if "*/" in s: inb=False
                continue
            if s.startswith("//"): out.append((i,l,"//"))
            elif s.startswith("/*"):
                out.append((i,l,"/*")); inb = "*/" not in s
            elif " // " in l: out.append((i,l[l.index(" // "):],"//t"))
    else:
        for i,l in enumerate(src.splitlines(),1):
            s=l.strip()
            if s.startswith("#") and not (i==1 and s.startswith("#!")): out.append((i,l,"#"))
            elif lg=="sh" and re.search(r"\s#\s",l) and not re.search(r"['\"].*#.*['\"]",l): out.append((i,l[l.index('#'):] if '#' in l else l,"#t"))
    return out
per=collections.Counter(); code=collections.Counter(); filesn=collections.Counter()
cat=collections.Counter(); catlang=collections.defaultdict(collections.Counter); ex={}
ids=collections.Counter(); idsites=collections.defaultdict(list)
blocks=[]  # (file, startline, text)
for f in files:
    lg=lang(f)
    if not lg: continue
    filesn[lg]+=1
    try: n=sum(1 for _ in open(f,encoding="utf-8"))
    except Exception: continue
    code[lg]+=n
    cs=sorted(comments(f,lg)); per[lg]+=len(cs)
    prev=None; cur=None
    for ln,txt,k in cs:
        hits={"tag-ns":TAGNS.search(txt),"tag-charter":CHTAG.search(txt),"id":ID.search(txt),"ptr-memory":MEMPTR.search(txt),"ptr-file":FILEPTR.search(txt),"directive":DIR.search(txt),"gov-marker":GOV.search(txt)}
        for c,m in hits.items():
            if m:
                cat[c]+=1; catlang[c][lg]+=1
                ex.setdefault(c,(f,ln,txt.strip()[:110]))
        for m in ID.finditer(txt): ids[m.group(0)]+=1; idsites[m.group(0)].append(f"{f}:{ln}")
        if prev is not None and ln==prev+1: cur[2].append(txt)
        else:
            cur=[f,ln,[txt]]; blocks.append(cur)
        prev=ln
print("LANG files lines commentlines pct")
for lg in sorted(per,key=lambda k:-per[k]): print(lg,filesn[lg],code[lg],per[lg],f"{100*per[lg]/max(code[lg],1):.1f}%")
T=sum(per.values()); print("TOTAL",sum(filesn.values()),sum(code.values()),T)
print("\nCATEGORY lines pct-of-comment-lines bylang")
for c in ["tag-ns","tag-charter","id","ptr-memory","ptr-file","directive","gov-marker"]:
    print(c,cat[c],f"{100*cat[c]/T:.2f}%",dict(catlang[c]))
print("\nEXAMPLES"); [print(c,"|",f"{f}:{ln}","|",t) for c,(f,ln,t) in ex.items()]
print("\nblocks",len(blocks))
idb=[b for b in blocks if ID.search(" ".join(b[2]))]
print("blocks with id",len(idb))
bare=[]
for f,ln,tx in idb:
    words=re.findall(r"[A-Za-z]{2,}"," ".join(ID.sub("",t) for t in tx).replace("#","").replace("//",""))
    if len(words)<4: bare.append((f,ln," ".join(t.strip() for t in tx)[:100]))
print("id blocks failing A5 (<4 words without id)",len(bare)); [print("  ",b) for b in bare[:12]]
print("distinct ids",len(ids),"citations",sum(ids.values()))
json.dump({"ids":ids,"sites":idsites},open(sys.argv[2],"w"))
```

### `dangle.py`

```python
import json,re,subprocess,sys,collections
d=json.load(open(sys.argv[1]))
ids=d["ids"]
ID = re.compile(r"\b[A-Z]{2,5}-(?:\d{3}|[a-z]\d{2,3}|[a-z][A-Za-z]{2,}-\d+[a-z]*)\b")
mem=set()
out=subprocess.run(["git","grep","-ohE",r"\b[A-Z]{2,5}-([0-9]{3}|[a-z][0-9]{2,3}|[a-z][A-Za-z]{2,}-[0-9]+[a-z]*)\b","--","memory"],capture_output=True,text=True).stdout
mem=set(out.split())
# slug-level: build folder exists?
builds=set(l.split("/")[2] for l in subprocess.run(["git","ls-files","memory/builds"],capture_output=True,text=True).stdout.split() if l.count("/")>=3)
dang=[i for i in ids if i not in mem]
fams=collections.Counter(i.split("-")[0] for i in ids)
print("families cited",dict(fams))
print("ids cited",len(ids),"absent from memory/ entirely",len(dang),"citations",sum(ids[i] for i in dang))
nob=[i for i in ids if len(i.split("-"))==3 and i.split("-")[1] not in builds]
print("session-era ids",sum(1 for i in ids if len(i.split('-'))==3),"whose slug has no memory/builds/<slug>/",len(nob))
for i in sorted(dang,key=lambda k:-ids[k])[:10]: print("  ",i,ids[i],d["sites"][i][0])
```

### `tx.py`

```python
import json,os,re,sys,collections,glob,pathlib
ROOT=pathlib.Path(sys.argv[1]); PROJ=pathlib.Path(os.path.expanduser("~/.claude/projects"))
SINCE="2026-08-16"
ID=re.compile(r"\b[A-Z]{2,5}-(?:\d{3}|[a-z]\d{2,3}|[a-z][A-Za-z]{2,}-\d+[a-z]*)\b")
MEM=re.compile(r"memory/[\w./-]+\.md")
REL=re.compile(r"((?:tools|skills|\.githooks)/[\w./-]+)$")
cache={}
def lines(rel):
    if rel not in cache:
        p=ROOT/rel
        try: cache[rel]=p.read_text(encoding="utf-8",errors="replace").splitlines()
        except Exception: cache[rel]=None
    return cache[rel]
def is_comment(l):
    s=l.strip(); return s.startswith("#") or s.startswith("//") or s.startswith("*") or s.startswith('"""')
C=collections.Counter(); sess_g=set(); sess_l=set()
gcmd=collections.Counter(); lcmd=collections.Counter()
use=collections.Counter(); samples=[]
files=[f for f in PROJ.glob("*coding-governance*/**/*.jsonl") if os.path.getmtime(f)>=1786838400]
for f in files:
    calls=[]
    try:
        fh=open(f,encoding="utf-8",errors="replace")
    except Exception: continue
    for raw in fh:
        if '"tool_use"' not in raw: continue
        try: e=json.loads(raw)
        except Exception: continue
        ts=e.get("timestamp","")
        if ts and ts<SINCE: continue
        msg=e.get("message") or {}
        cont=msg.get("content") if isinstance(msg,dict) else None
        if not isinstance(cont,list): continue
        for b in cont:
            if isinstance(b,dict) and b.get("type")=="tool_use":
                calls.append((b.get("name"),b.get("input") or {}))
    fh.close()
    for i,(n,inp) in enumerate(calls):
        s=json.dumps(inp)
        if n=="Bash":
            cmd=inp.get("command","")
            if "gotchas.py" in cmd:
                m=re.search(r"gotchas\.py\S*\s+(--[a-z-]+)",cmd); gcmd[m.group(1) if m else "?"]+=1; sess_g.add(str(f))
            if "lexicon.py" in cmd:
                m=re.search(r"lexicon\.py\S*\s+(--[a-z-]+)",cmd); lcmd[m.group(1) if m else "(none)"]+=1; sess_l.add(str(f))
        elif "gotchas" in s and n in("Workflow","Task","Agent"): C["gotchas-in-"+n]+=1
        if n=="Read":
            fp=inp.get("file_path","").replace("\\","/")
            m=REL.search(fp)
            if not m: continue
            rel=m.group(1); L=lines(rel)
            if L is None: continue
            off=int(inp.get("offset") or 1); lim=int(inp.get("limit") or 2000)
            reg=L[max(off-1,0):off-1+lim]
            ids=set(); mems=set()
            for l in reg:
                if is_comment(l):
                    ids.update(ID.findall(l)); mems.update(MEM.findall(l))
            C["code-reads"]+=1
            if inp.get("offset") or inp.get("limit"): C["code-reads-sliced"]+=1
            nxt=calls[i+1:i+11]
            anymem=any("memory/" in json.dumps(x[1]) for x in nxt)
            if anymem: C["code-read->any-memory-within10"]+=1
            if not (ids or mems): continue
            C["code-reads-region-has-id-or-ptr"]+=1
            slugs={x.split("-")[1] for x in ids if x.count("-")==2}
            hit=None
            for k,(n2,i2) in enumerate(nxt):
                t=json.dumps(i2)
                if n2 in("Read","Grep","Glob","Bash") and ("memory/" in t or n2=="Grep"):
                    if any(x in t for x in ids) or any(x in t for x in mems) or any(("builds/"+sl) in t for sl in slugs):
                        hit=(k,n2,t[:140]); break
            if hit:
                C["...followed-by-ref-record-within10"]+=1
                if len(samples)<6: samples.append((f.name,rel,off,hit))
            # sliced reads only
            if inp.get("offset") or inp.get("limit"):
                C["sliced-region-has-id-or-ptr"]+=1
                if hit: C["sliced...followed"]+=1
print("files",len(files)); print(dict(C))
print("gotchas.py bash invocations",dict(gcmd),"sessions",len(sess_g))
print("lexicon.py bash invocations",dict(lcmd),"sessions",len(sess_l))
for s in samples: print("  ",s)
```

### `tx2.py`

```python
import json,os,re,sys,collections,glob,pathlib
ROOT=pathlib.Path(sys.argv[1]); PROJ=pathlib.Path(os.path.expanduser("~/.claude/projects"))
SINCE="2026-08-16"
ID=re.compile(r"\b[A-Z]{2,5}-(?:\d{3}|[a-z]\d{2,3}|[a-z][A-Za-z]{2,}-\d+[a-z]*)\b")
MEM=re.compile(r"memory/[\w./-]+\.md")
REL=re.compile(r"((?:tools|skills|\.githooks)/[\w./-]+)$")
cache={}
def lines(rel):
    if rel not in cache:
        p=ROOT/rel
        try: cache[rel]=p.read_text(encoding="utf-8",errors="replace").splitlines()
        except Exception: cache[rel]=None
    return cache[rel]
def is_comment(l):
    s=l.strip(); return s.startswith("#") or s.startswith("//") or s.startswith("*") or s.startswith('"""')
C=collections.Counter(); sess_g=set(); sess_l=set()
gcmd=collections.Counter(); lcmd=collections.Counter()
use=collections.Counter(); samples=[]
files=[f for f in PROJ.glob("*coding-governance*/**/*.jsonl") if os.path.getmtime(f)>=1786838400]
for f in files:
    calls=[]
    try:
        fh=open(f,encoding="utf-8",errors="replace")
    except Exception: continue
    for raw in fh:
        if '"tool_use"' not in raw: continue
        try: e=json.loads(raw)
        except Exception: continue
        ts=e.get("timestamp","")
        if ts and ts<SINCE: continue
        msg=e.get("message") or {}
        cont=msg.get("content") if isinstance(msg,dict) else None
        if not isinstance(cont,list): continue
        for b in cont:
            if isinstance(b,dict) and b.get("type")=="tool_use":
                calls.append((b.get("name"),b.get("input") or {}))
    fh.close()
    prev_region=None
    for i,(n,inp) in enumerate(calls):
        s=json.dumps(inp)
        if n=="Bash":
            cmd=inp.get("command","")
            if "gotchas.py" in cmd:
                m=re.search(r"gotchas\.py\S*\s+(--[a-z-]+)",cmd); gcmd[m.group(1) if m else "?"]+=1; sess_g.add(str(f))
            if "lexicon.py" in cmd:
                m=re.search(r"lexicon\.py\S*\s+(--[a-z-]+)",cmd); lcmd[m.group(1) if m else "(none)"]+=1; sess_l.add(str(f))
        elif "gotchas" in s and n in("Workflow","Task","Agent"): C["gotchas-in-"+n]+=1
        if n=="Read":
            fp=inp.get("file_path","").replace("\\","/")
            m=REL.search(fp)
            if not m: continue
            rel=m.group(1); L=lines(rel)
            if L is None: continue
            off=int(inp.get("offset") or 1); lim=int(inp.get("limit") or 2000)
            reg=L[max(off-1,0):off-1+lim]
            ids=set(); mems=set()
            for l in reg:
                if is_comment(l):
                    ids.update(ID.findall(l)); mems.update(MEM.findall(l))
            C["code-reads"]+=1
            if inp.get("offset") or inp.get("limit"): C["code-reads-sliced"]+=1
            nxt=calls[i+1:i+11]
            anymem=any("memory/" in json.dumps(x[1]) for x in nxt)
            if anymem: C["code-read->any-memory-within10"]+=1
            if not (ids or mems): continue
            C["code-reads-region-has-id-or-ptr"]+=1
            slugs={x.split("-")[1] for x in ids if x.count("-")==2}
            hit=None
            for k,(n2,i2) in enumerate(nxt):
                t=json.dumps(i2)
                if n2 in("Read","Grep","Glob","Bash") and ("memory/" in t or n2=="Grep"):
                    if any(x in t for x in ids) or any(x in t for x in mems) or any(("builds/"+sl) in t for sl in slugs):
                        hit=(k,n2,t[:140]); break
            ctrl=None
            if prev_region:
                cids,cmems=prev_region
                cs={x.split("-")[1] for x in cids if x.count("-")==2}
                for k,(n2,i2) in enumerate(nxt):
                    t=json.dumps(i2)
                    if n2 in("Read","Grep","Glob","Bash") and ("memory/" in t or n2=="Grep"):
                        if any(x in t for x in cids-ids) or any(x in t for x in cmems-mems) or any(("builds/"+sl) in t for sl in cs-slugs):
                            ctrl=1;break
                C["control-other-file-region"]+=1
                if ctrl: C["control-followed"]+=1
            prev_region=(ids,mems)
            exact=None
            for k,(n2,i2) in enumerate(nxt[:3]):
                t=json.dumps(i2)
                if any(x in t for x in ids) or any(x in t for x in mems): exact=1;break
            if exact: C["exact-id-or-path-within3"]+=1
            if hit:
                C["...followed-by-ref-record-within10"]+=1
                if len(samples)<6: samples.append((f.name,rel,off,hit))
            # sliced reads only
            if inp.get("offset") or inp.get("limit"):
                C["sliced-region-has-id-or-ptr"]+=1
                if hit: C["sliced...followed"]+=1
print("files",len(files)); print(dict(C))
print("gotchas.py bash invocations",dict(gcmd),"sessions",len(sess_g))
print("lexicon.py bash invocations",dict(lcmd),"sessions",len(sess_l))
for s in samples: print("  ",s)
```

## Dispatch 26: the tooling map

Its return is `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-tooling.md`.

### `usage.py`

```python
import json,glob,os,re,sys,collections
root=os.path.expanduser('~/.claude/projects')
cut='2026-08-16'
kits="agent-instructions branch-reconcile codebase-map drift-audit gate-lint govkit hooks lexicon lib memory-recall memory-tree playbook process-monitor pytest-parallel-guardrails roles run-gates runlog unattended workflows".split()
checks=[os.path.basename(p) for p in glob.glob(sys.argv[1]+'/tools/check-*')]+['push-main.sh','settings-merge.py']
skills="build cleanup drift-audit lexicon memory-recall runlog unattended deploy-governance session-kickoff".split()
cmd=collections.Counter(); sk=collections.Counter(); slash=collections.Counter(); files=0; uses=0
for d in glob.glob(root+'/C--projects-coding-governance*'):
  for f in glob.glob(d+'/**/*.jsonl',recursive=True):
    files+=1
    for line in open(f,encoding='utf-8',errors='replace'):
      try: e=json.loads(line)
      except: continue
      if e.get('timestamp','')<cut: continue
      m=e.get('message') or {}
      c=m.get('content')
      if e.get('type')=='user' and isinstance(c,str):
        for s in skills:
          if f'<command-name>/{s}</command-name>' in c: slash[s]+=1
      if not isinstance(c,list): continue
      for b in c:
        if not isinstance(b,dict) or b.get('type')!='tool_use': continue
        n=b.get('name'); i=b.get('input') or {}
        if n=='Skill':
          sk[str(i.get('skill') or i.get('command'))]+=1
        if n in('Bash','PowerShell'):
          s=i.get('command','') or ''
          uses+=1
          for k in kits:
            if re.search(r'tools/'+re.escape(k)+r'/', s): cmd['kit:'+k]+=1
          for k in checks:
            if re.search(r'tools/'+re.escape(k)+r'\b', s): cmd[k]+=1
          if 'run-gates.sh' in s: cmd['run-gates.sh']+=1
print('files',files,'shell calls',uses)
for k,v in sorted(cmd.items()): print(k,v)
print('SKILL tool',dict(sk)); print('slash',dict(slash))
```

### `exec.py`

```python
import json,glob,os,re,sys,collections
root=os.path.expanduser('~/.claude/projects'); cut='2026-08-16'
names="agent-instructions branch-reconcile codebase-map drift-audit gate-lint govkit hooks lexicon lib memory-recall memory-tree playbook process-monitor pytest-parallel-guardrails roles run-gates runlog unattended workflows".split()
checks=[os.path.basename(p) for p in glob.glob(sys.argv[1]+'/tools/check-*') if not p.endswith('.txt') and not p.endswith('.json')]+['push-main.sh','push-main.test.sh','settings-merge.py']
RUN=r'(?:^|[;&|(]\s*|\s)(?:bash|sh|python3?|py(?:\s+-3)?|node|\$\w+|"\$\w+")\s+(?:-\S+\s+)*"?[^\s"]*'
pk={k:re.compile(RUN+r'tools/'+re.escape(k)+r'/([\w.-]+)') for k in names}
pc={k:re.compile(RUN+r'tools/'+re.escape(k)+r'(?![\w.-])') for k in checks}
kc=collections.Counter(); ent=collections.Counter(); cc=collections.Counter(); rg=0; sessions=set()
for d in glob.glob(root+'/C--projects-coding-governance*'):
  for f in glob.glob(d+'/**/*.jsonl',recursive=True):
    for line in open(f,encoding='utf-8',errors='replace'):
      try: e=json.loads(line)
      except: continue
      if e.get('timestamp','')<cut: continue
      c=(e.get('message') or {}).get('content')
      if not isinstance(c,list): continue
      for b in c:
        if isinstance(b,dict) and b.get('type')=='tool_use' and b.get('name') in('Bash','PowerShell'):
          s=(b.get('input') or {}).get('command','') or ''
          for k,p in pk.items():
            hits=p.findall(s)
            if hits: kc[k]+=1
            for h in set(hits): ent[k+'/'+h]+=1
          for k,p in pc.items():
            if p.search(s): cc[k]+=1
print('KITS'); [print(' ',k,kc[k]) for k in names]
print('CHECKS'); [print(' ',k,cc[k]) for k in checks]
print('TOP ENTRYPOINTS'); [print(' ',k,v) for k,v in ent.most_common(70)]
```
