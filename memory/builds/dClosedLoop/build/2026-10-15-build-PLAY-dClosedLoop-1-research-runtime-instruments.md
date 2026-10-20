# Research: the runtime layer's probe scripts

**Serves:** research PLAY-dClosedLoop-1

The four runtime researchers wrote their probes in the session's shared scratchpad and cited them
from their returns. This record keeps them beside the returns, as fenced text, because the lexicon
gate grades every tracked Python file. Every probe reads; none was run again for this record.

**One probe was lost to the shared scratchpad.** Dispatches 30 and 31 each wrote a `tx.py`. The
surviving file is dispatch 30's: it counts driver calls. Dispatch 31's version, which counted
spawns by path, was overwritten, and its output survives only in its return. Concurrent agents
writing scratch files under one name is the isolation gap the runtime design closes with a
scratch directory per agent.

## Dispatch 30: the executor and `next`

Its return is `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-executor.md`.

### `tx.py`

```python
import json,sys,re,glob,os,collections
root=os.path.expanduser('~/.claude/projects')
files=[f for f in glob.glob(root+'/C--projects-coding-governance*/*.jsonl')]
rows=[]
for f in files:
    txt=open(f,encoding='utf-8',errors='replace').read()
    if 'unattended.sh --preflight' not in txt: continue
    tools=collections.Counter(); verbs=collections.Counter(); scripts=collections.Counter()
    compacts=0; errs=0; ts=[]; slug=set(); cron_wakes=0; users=0; ask=0
    for line in txt.splitlines():
        try: o=json.loads(line)
        except: continue
        if o.get('isSidechain'): continue
        t=o.get('timestamp');
        if t: ts.append(t)
        if o.get('type')=='system' and o.get('subtype')=='compact_boundary': compacts+=1
        if o.get('isCompactSummary'): pass
        m=o.get('message') or {}
        c=m.get('content')
        if o.get('type')=='user':
            if isinstance(c,str):
                users+=1
                if 'unattended.sh --resume' in c or 'scheduled' in c.lower(): cron_wakes+=1
            elif isinstance(c,list):
                for b in c:
                    if b.get('type')=='tool_result' and b.get('is_error'): errs+=1
                    if b.get('type')=='text':
                        users+=1
                        if 'unattended.sh --resume' in b.get('text',''): cron_wakes+=1
        if o.get('type')=='assistant' and isinstance(c,list):
            for b in c:
                if b.get('type')!='tool_use': continue
                n=b.get('name'); tools[n]+=1; inp=b.get('input',{})
                if n=='Bash':
                    cmd=inp.get('command','')
                    for v in re.findall(r'unattended\.sh\s+(--[a-z-]+)',cmd): verbs[v]+=1
                    for s in re.findall(r'unattended\.sh\s+--preflight\s+(\S+)',cmd): slug.add(s.strip('"\''))
                if n=='Workflow':
                    sp=inp.get('scriptPath') or inp.get('name') or '?'; scripts[os.path.basename(str(sp))]+=1
                if n=='AskUserQuestion': ask+=1
    tot=sum(tools.values())
    rows.append((min(ts) if ts else '',os.path.basename(f)[:8],','.join(sorted(slug))[:22],tot,tools.get('Bash',0),tools.get('Read',0),tools.get('Edit',0)+tools.get('Write',0),tools.get('Agent',0)+tools.get('Task',0),sum(scripts.values()),verbs.get('--dispatch',0),sum(verbs.values()),compacts,errs,cron_wakes,ask,dict(scripts)))
rows.sort()
print('start sess slug tot bash read edit agent wf disp drvcalls compacts errs cronwakes ask scripts')
for r in rows: print(r[0][:16],*r[1:])
```

### `cmp.py`

```python
import json,glob,os,collections
root=os.path.expanduser('~/.claude/projects')
first=collections.Counter(); n=0; preT=[]
for f in glob.glob(root+'/C--projects-coding-governance*/*.jsonl'):
    txt=open(f,encoding='utf-8',errors='replace').read()
    if 'unattended.sh --preflight' not in txt: continue
    after=None
    for line in txt.splitlines():
        try:o=json.loads(line)
        except:continue
        if o.get('isSidechain'):continue
        if o.get('type')=='system' and o.get('subtype')=='compact_boundary':
            n+=1; after=[]; preT.append(o.get('compactMetadata',{}).get('preTokens'))
            continue
        if after is not None and o.get('type')=='assistant':
            for b in (o.get('message',{}).get('content') or []):
                if isinstance(b,dict) and b.get('type')=='tool_use':
                    i=b.get('input',{}); s=i.get('command') or i.get('file_path') or i.get('scriptPath') or ''
                    after.append(b['name']+': '+str(s)[:90].replace('\n',' '))
            if len(after)>=3:
                print(os.path.basename(f)[:8],' | '.join(after[:3])); after=None
print('compactions',n,'preTokens',sorted(x for x in preT if x))
```

### `cmp2.py`

```python
import json,glob,os,collections
root=os.path.expanduser('~/.claude/projects')
first=collections.Counter(); n=0; preT=[]
for f in glob.glob(root+'/C--projects-coding-governance*/*.jsonl'):
    txt=open(f,encoding='utf-8',errors='replace').read()
    if 'unattended.sh --preflight' not in txt: continue
    after=None
    for line in txt.splitlines():
        try:o=json.loads(line)
        except:continue
        if o.get('isSidechain'):continue
        if o.get('type')=='system' and o.get('subtype')=='compact_boundary':
            n+=1; after=[]; preT.append(o.get('compactMetadata',{}).get('preTokens'))
            continue
        if after is not None and o.get('type')=='assistant':
            for b in (o.get('message',{}).get('content') or []):
                if isinstance(b,dict) and b.get('type')=='tool_use':
                    i=b.get('input',{}); s=i.get('command') or i.get('file_path') or i.get('scriptPath') or ''
                    after.append(b['name']+': '+str(s)[:90].replace('\n',' '))
            if len(after)>=10:
                import re; hits=[a for a in after if re.search(r'unattended.sh --(status|resume|plan)',a)]; print(os.path.basename(f)[:8], 'driver-reorient-in-first-10:', len(hits)>0); after=None
print('compactions',n,'preTokens',sorted(x for x in preT if x))
```

## Dispatch 31: the spawn harness

Its return is `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-spawn.md`.

### `wf.py`

```python
import json,glob,os,time,collections,sys
cut=time.time()-60*86400
root=os.path.expanduser('~/.claude/projects')
js=[p for p in glob.glob(root+'/C--projects-coding-governance*/*/workflows/*.json') if os.path.getmtime(p)>=cut]
st=collections.Counter(); names=collections.Counter(); ag=collections.Counter(); errs=[]; fans=collections.Counter()
partial=[]
for p in js:
    try: d=json.load(open(p,encoding='utf-8'))
    except Exception as e: st['unreadable']+=1; continue
    st[d.get('status')]+=1; names[(d.get('workflowName'),d.get('status'))]+=1
    agents=[w for w in d.get('workflowProgress') or [] if w.get('type')=='workflow_agent']
    s=collections.Counter(a.get('state') for a in agents)
    for k,v in s.items(): ag[k]+=v
    if s.get('error'):
        e=[a for a in agents if a.get('state')=='error']
        errs.append((d.get('runId'),d.get('workflowName'),d.get('status'),len(agents),len(e),(e[0].get('error') or e[0].get('errorMessage') or str({k:v for k,v in e[0].items() if k not in('label',)})[:200]) ))
        if len(e)==len(agents): fans['all agents error']+=1
        else: fans['some agents error']+=1
print('journals',len(js)); print('status',dict(st)); print('agent states',dict(ag)); print('fan error shape',dict(fans))
for n,c in names.most_common(30): print(c,n)
print('--- runs with errored agents')
for e in errs: print(e)
```

### `wf2.py`

```python
import json,glob,os,time,collections,re
cut=time.time()-60*86400
root=os.path.expanduser('~/.claude/projects')
js=[p for p in glob.glob(root+'/C--projects-coding-governance*/*/workflows/*.json') if os.path.getmtime(p)>=cut]
cls=collections.Counter()
def c(m):
    m=m or ''
    for k,r in [('session/weekly limit',r'hit your (session|weekly) limit'),('overloaded/5xx/conn',r'Overloaded|500|Connection lost|ENOTFOUND'),('schema retry cap',r'StructuredOutput retry')]:
        if re.search(r,m): return k
    return 'other:'+m[:80]
for p in js:
    d=json.load(open(p,encoding='utf-8'))
    ag=[w for w in d.get('workflowProgress') or [] if w.get('type')=='workflow_agent']
    for a in ag:
        if a.get('state')=='error': cls[c(a.get('error'))]+=1
    e=[a for a in ag if a.get('state')=='error']
    if e and len(e)==len(ag) and d.get('status')=='completed':
        print('ALL-ERR completed', d['runId'], d.get('workflowName'), 'result=', json.dumps(d.get('result'))[:160])
    if d.get('status')!='completed':
        print(d.get('status'), d['runId'], d.get('workflowName'), len(ag), 'err', len(e), '|', json.dumps(d.get('result'))[:120], '|', (d.get('logs') or [''])[-1][:140])
print(dict(cls))
```

### `wf3.py`

```python
import json,glob,os,time,re
cut=time.time()-60*86400
root=os.path.expanduser('~/.claude/projects')
for p in sorted(glob.glob(root+'/C--projects-coding-governance*/*/workflows/*.json')):
    if os.path.getmtime(p)<cut: continue
    d=json.load(open(p,encoding='utf-8'))
    ag=[w for w in d.get('workflowProgress') or [] if w.get('type')=='workflow_agent']
    e=[a for a in ag if a.get('state')=='error' and re.search('limit',a.get('error') or '')]
    if not e: continue
    sess=os.path.basename(os.path.dirname(os.path.dirname(p)))
    tx=os.path.join(os.path.dirname(os.path.dirname(p))+'.jsonl')
    ver='?'
    try:
        for l in open(tx,encoding='utf-8',errors='replace'):
            m=re.search(r'"version":"([0-9.]+)"',l)
            if m: ver=m.group(1)
    except: pass
    print(d['timestamp'][:10], d['runId'], d.get('workflowName'), f"{len(e)}/{len(ag)}", 'cli', ver)
```

## Dispatch 32: hooks, isolation and supervision

Its return is `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-hooks.md`.

### `hookagg.py`

```python
import json,os,sys,time,glob,statistics,collections,re
root=os.path.expanduser('~/.claude/projects'); cut=time.time()-60*86400
agg=collections.defaultdict(list); codes=collections.defaultdict(collections.Counter); types=collections.Counter()
nfiles=0
for d in glob.glob(root+'/*coding-governance*'):
  for dp,_,fs in os.walk(d):
    for f in fs:
      if not f.endswith('.jsonl'): continue
      p=os.path.join(dp,f)
      if os.path.getmtime(p)<cut: continue
      nfiles+=1
      with open(p,encoding='utf-8',errors='replace') as h:
        for line in h:
          if '"hookEvent"' not in line: continue
          try: a=json.loads(line).get('attachment') or {}
          except Exception: continue
          t=a.get('type',''); 
          if not t.startswith('hook'): continue
          types[t]+=1
          cmd=a.get('command')
          if not cmd: continue
          m=re.search(r'([\w.-]+\.(?:js|sh|py))',cmd); s=m.group(1) if m else cmd[:40]
          if '--card --write' in cmd: s+=' --write'
          if '--card --replay' in cmd: s+=' --replay'
          k=(a.get('hookEvent'),s); 
          if a.get('durationMs') is not None: agg[k].append(a['durationMs'])
          codes[k][(t,a.get('exitCode'))]+=1
print('files',nfiles); print(types.most_common())
def pct(v,q): v=sorted(v); return v[min(len(v)-1,int(q*len(v)))]
for k in sorted(codes,key=lambda k:-sum(codes[k].values())):
  v=agg[k]; n=sum(codes[k].values())
  print(f"{k[0]:<13}{k[1]:<30}n={n:<7}", (f"p50={pct(v,.5)} p95={pct(v,.95)} max={max(v)}" if v else ''), dict(codes[k]))
```

### `hookerr.py`

```python
import json,os,time,glob
root=os.path.expanduser('~/.claude/projects'); cut=time.time()-60*86400
for d in glob.glob(root+'/*coding-governance*'):
  for dp,_,fs in os.walk(d):
    for f in fs:
      p=os.path.join(dp,f)
      if not f.endswith('.jsonl') or os.path.getmtime(p)<cut: continue
      for line in open(p,encoding='utf-8',errors='replace'):
        if 'hook_non_blocking_error' not in line and 'hook_blocking_error' not in line: continue
        try: o=json.loads(line); a=o.get('attachment') or {}
        except Exception: continue
        if a.get('type') not in ('hook_non_blocking_error','hook_blocking_error'): continue
        txt=(a.get('stderr') or json.dumps(a.get('blockingError') or a.get('content') or ''))[:150].replace('\n',' ')
        print(o.get('timestamp','')[:16],a['type'][5:9],a.get('hookName'),a.get('exitCode'),(a.get('command') or '')[-28:],'|',txt)
```

### `procmon.py`

```python
import json,os,time,glob,re,collections
root=os.path.expanduser('~/.claude/projects'); cut=time.time()-60*86400
rows=collections.defaultdict(set); reports=0; broken=collections.Counter(); reapcmd=collections.Counter(); killed=collections.Counter()
for d in glob.glob(root+'/*coding-governance*'):
  for dp,_,fs in os.walk(d):
    for f in fs:
      p=os.path.join(dp,f)
      if not f.endswith('.jsonl') or os.path.getmtime(p)<cut: continue
      for line in open(p,encoding='utf-8',errors='replace'):
        if 'process-monitor' in line and 'procmon-hook' in line and '"attachment"' in line:
          try: a=json.loads(line)['attachment']
          except Exception: continue
          c=a.get('stdout') or ''
          if not c.strip(): continue
          reports+=1
          hit=False
          for m in re.finditer(r'^\s*(ORPHAN|SPIN|IDLE|UNKNOWN)\s+winpid\s+(\d+)\s+age\s+([\d.]+h)',c,re.M):
            rows[m.group(1)].add(m.group(2)); hit=True
          if not hit: broken[c.strip().splitlines()[0][:90]]+=1
        if 'reap.py' in line and '"tool_use"' in line:
          try: o=json.loads(line)
          except Exception: continue
          for b in (o.get('message') or {}).get('content') or []:
            if isinstance(b,dict) and b.get('type')=='tool_use':
              cmd=str((b.get('input') or {}).get('command',''))
              if 'reap.py' in cmd:
                k='dry-run' if '--dry-run' in cmd else ('sweep' if '--sweep' in cmd else 'other')
                reapcmd[k]+=1; m2=re.search(r"reap.py(s+--?[a-z-]+)*",cmd); reapcmd["form:"+(m2.group(0) if m2 else "?")]+=1
print('reports',reports); print({k:len(v) for k,v in rows.items()}); print(reapcmd)
for k,v in broken.most_common(6): print(v,k)
```

### `reapforms.py`

```python
import json,os,time,glob,re,collections
root=os.path.expanduser('~/.claude/projects'); cut=time.time()-60*86400; c=collections.Counter()
for d in glob.glob(root+'/*coding-governance*'):
  for dp,_,fs in os.walk(d):
    for f in fs:
      p=os.path.join(dp,f)
      if not f.endswith('.jsonl') or os.path.getmtime(p)<cut: continue
      for line in open(p,encoding='utf-8',errors='replace'):
        if 'reap.py' not in line or '"tool_use"' not in line: continue
        try: o=json.loads(line)
        except Exception: continue
        for b in (o.get('message') or {}).get('content') or []:
          if isinstance(b,dict) and b.get('type')=='tool_use':
            cmd=str((b.get('input') or {}).get('command',''))
            for m in re.finditer(r'reap\.py((?:\s+--?[\w-]+(?:[ =]\d+)?)*)',cmd): c[m.group(1).strip() or '(bare)']+=1
for k,v in c.most_common(15): print(v,k)
```

## Dispatch 33: sessions, context, scheduling, harnesses and nodes

Its return is `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-sessions.md`.

### `scan.py`

```python
import json,glob,os,collections,statistics as S,sys
root=os.path.expanduser('~/.claude/projects')
dirs=[d for d in glob.glob(root+'/C--projects-coding-governance*')]
def tot(u): return (u.get('input_tokens',0)+u.get('cache_creation_input_tokens',0)+u.get('cache_read_input_tokens',0))
hooks=collections.Counter(); card_by_src=collections.Counter(); compacts=[]; sub_compacts=[]
first_after={'startup':[], 'resume':[], 'compact':[], 'clear':[]}
sess_turns=[]; sess_compacted=0; nsess=0; precompact=0; resume_cc=[]
for d in dirs:
  for f in glob.glob(d+'/*.jsonl')+glob.glob(d+'/*/subagents/*.jsonl'):
    sub='subagents' in f
    pending=None; turns=0; nc=0; ts=[]
    for l in open(f,encoding='utf-8',errors='replace'):
      try:x=json.loads(l)
      except:continue
      a=x.get('attachment') or {}
      if x.get('timestamp'): ts.append(x['timestamp'])
      hn=a.get('hookName','')
      if hn.startswith('PreCompact') or a.get('hookEvent')=='PreCompact': precompact+=1
      if hn.startswith('SessionStart:') and a.get('type')=='hook_success' and not sub:
        src=hn.split(':')[1]; hooks[src]+=1
        if 'orientation —' in (a.get('content') or ''): card_by_src[src]+=1
        pending=src
      if x.get('type')=='system' and x.get('subtype')=='compact_boundary':
        m=x.get('compactMetadata',{}); (sub_compacts if sub else compacts).append((m.get('trigger'),m.get('preTokens'),m.get('postTokens'),m.get('durationMs'))); nc+=1
        pending='compact'
      if x.get('type')=='assistant':
        u=(x.get('message') or {}).get('usage') or {}
        if u and not x.get('isApiErrorMessage'):
          turns+=1
          if pending in first_after and not sub:
            first_after[pending].append(tot(u))
            if pending=='resume': resume_cc.append((u.get('cache_creation_input_tokens',0),u.get('cache_read_input_tokens',0)))
          pending=None
    if not sub:
      nsess+=1; sess_turns.append((turns,nc))
      if nc: sess_compacted+=1
print('dirs',len(dirs),'main sessions',nsess)
print('SessionStart hook_success by source',dict(hooks))
print('…of which carried a card',dict(card_by_src))
print('PreCompact hook entries',precompact)
def st(v): return 'n=%d median=%s mean=%s min=%s max=%s'%(len(v),int(S.median(v)) if v else '-',int(S.mean(v)) if v else '-',min(v) if v else '-',max(v) if v else '-')
for k,v in first_after.items(): print('first-turn input after',k,st(v))
print('resume first turn (cache_creation, cache_read) sample',resume_cc[:12])
print('main compactions',len(compacts),collections.Counter(c[0] for c in compacts))
print(' preTokens',st([c[1] for c in compacts if c[1]]))
print(' postTokens',st([c[2] for c in compacts if c[2]]))
print(' durationMs',st([c[3] for c in compacts if c[3]]))
print('subagent compactions',len(sub_compacts),sub_compacts[:5])
print('sessions compacted',sess_compacted,'of',nsess)
for lo,hi in [(0,200),(200,1000),(1000,3000),(3000,10**9)]:
  g=[c for t,c in sess_turns if lo<=t<hi]; print(' turns %d-%s: sessions %d compacted %d total compactions %d'%(lo,hi,len(g),sum(1 for c in g if c),sum(g)))
```

### `scan2.py`

```python
import json,glob,os,collections
root=os.path.expanduser('~/.claude/projects')
ev={}
for d in glob.glob(root+'/C--projects-coding-governance*'):
  for f in glob.glob(d+'/*.jsonl'):
    for l in open(f,encoding='utf-8',errors='replace'):
      try:x=json.loads(l)
      except:continue
      a=x.get('attachment') or {}
      hn=a.get('hookName','')
      if a.get('hookEvent')=='SessionStart' and hn.startswith('SessionStart:'):
        k=(f,a.get('toolUseID'),hn)
        e=ev.setdefault(k,{'card':False,'ts':x.get('timestamp',''),'types':set(),'ver':x.get('version')})
        e['types'].add(a.get('type'))
        c=a.get('content') or ''
        if isinstance(c,list): c=' '.join(map(str,c))
        if 'orientation —' in c: e['card']=True
c=collections.Counter(); 
for (f,t,hn),e in ev.items():
  src=hn.split(':')[1]; after=e['ts']>='2026-09-15'
  c[(src,'since-09-15' if after else 'before',e['card'])]+=1
for k in sorted(c): print(k,c[k])
miss=[(e['ts'],os.path.basename(f)[:8],hn,e['ver'],sorted(e['types'])) for (f,t,hn),e in ev.items() if hn.endswith('resume') and not e['card'] and e['ts']>='2026-09-15']
for m in sorted(miss)[-12:]: print(m)
```

### `scan3.py`

```python
import json,glob,os,statistics as S
root=os.path.expanduser('~/.claude/projects')
fresh=[];gaps=[];hrs=[]
for d in glob.glob(root+'/C--projects-coding-governance*'):
  for f in glob.glob(d+'/*.jsonl'):
    pend=None;turn=0;last=None;t0=None;t1=None
    for l in open(f,encoding='utf-8',errors='replace'):
      try:x=json.loads(l)
      except:continue
      a=x.get('attachment') or {}
      if (a.get('hookName') or '')=='SessionStart:startup': pend='s'
      if x.get('subtype')=='compact_boundary':
        if last is not None: gaps.append(turn-last)
        last=turn
      if x.get('type')=='assistant':
        u=(x.get('message') or {}).get('usage') or {}
        if u:
          turn+=1
          if pend=='s': fresh.append((u.get('cache_creation_input_tokens',0),u.get('cache_read_input_tokens',0),u.get('input_tokens',0))); pend=None
print('fresh first turn median cache_creation',int(S.median(c for c,_,_ in fresh)),'cache_read',int(S.median(r for _,r,_ in fresh)))
print('assistant turns between consecutive compactions: n=%d median=%d min=%d max=%d'%(len(gaps),S.median(gaps),min(gaps),max(gaps)))
```

### `scan4.py`

```python
import json,glob,os,statistics as S
root=os.path.expanduser('~/.claude/projects'); v=[]; turns=[]
for f in glob.glob(root+'/C--projects-coding-governance*/*/subagents/*.jsonl'):
  n=0;first=None
  for l in open(f,encoding='utf-8',errors='replace'):
    try:x=json.loads(l)
    except:continue
    u=(x.get('message') or {}).get('usage') if x.get('type')=='assistant' else None
    if u:
      n+=1
      if first is None: first=u.get('input_tokens',0)+u.get('cache_creation_input_tokens',0)+u.get('cache_read_input_tokens',0)
  if first: v.append(first); turns.append(n)
print('subagent transcripts',len(v),'first-turn input median',int(S.median(v)),'p90',sorted(v)[int(len(v)*.9)],'turns median',int(S.median(turns)),'max',max(turns))
```
