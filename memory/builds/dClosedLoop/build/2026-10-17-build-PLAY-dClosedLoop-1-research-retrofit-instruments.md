# Research instruments: retrofitting gov's practices, runs A and B

**Serves:** research PLAY-dClosedLoop-1

Each run's files and shell commands, taken in order from its transcript, so nothing is retyped. Both
runs shared the session scratch directory, so a file there may hold the other run's content; these
are what each run sent. The returns are `build/2026-10-17-build-PLAY-dClosedLoop-1-research-retrofit-a.md`
and `-b.md`.

## [run-a] Run A, dispatch 83

1. Bash

````text
ls memory/builds/dClosedLoop/build/ && wc -c memory/builds/dClosedLoop/build/*.md | tail -20 && ls memory/map/ && ls tools/
````

2. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && for f in *systems.md *layer-expansions.md *layer-memory.md *layer-library.md *flow-steps.md; do echo "== $f"; grep -n '^#' $f | head -60; done
````

3. Bash

````text
wc -l memory/builds/aDeployScout/spec/governance-deployer-research.md WIRE-INTO-PROJECT.md && grep -n '^#' memory/builds/aDeployScout/spec/governance-deployer-research.md | head -50 && grep -n -i 'retrofit\|existing\|brownfield\|legacy\|baseline' memory/builds/aDeployScout/spec/governance-deployer-research.md | head -40
````

4. Bash

````text
grep -n '^#' WIRE-INTO-PROJECT.md | head -80; grep -n -i 'retrofit\|existing code\|brownfield\|legacy\|baseline\|pre-existing\|already has' WIRE-INTO-PROJECT.md | head -60
````

5. Bash

````text
sed -n 225,313p WIRE-INTO-PROJECT.md; echo ----; sed -n 396,430p WIRE-INTO-PROJECT.md; echo ---; sed -n 515,572p WIRE-INTO-PROJECT.md
````

6. Bash

````text
head -40 memory/map/baseline.toml; wc -l memory/map/baseline.toml; git log --follow --format='%h %ad %s' --date=short -- memory/map/baseline.toml | wc -l; git log --follow --format='%h %ad %s' --date=short -- memory/map/baseline.toml | tail -5; git log --follow --format='%h %ad %s' --date=short -- memory/map/baseline.toml | head -5
````

7. Bash

````text
cat > /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/bl.sh <<'EOF'
for c in $(git log --reverse --follow --format='%h' -- memory/map/baseline.toml); do
  d=$(git show -s --format=%ad --date=short $c)
  n=$(git show $c:memory/map/baseline.toml 2>/dev/null | grep -cE '^\s+"')
  s=$(git show -s --format=%s $c | cut -c1-80)
  echo "$c $d keys=$n $s"
done
EOF
bash /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/bl.sh
````

8. Bash

````text
grep -cE '^\s+"' memory/map/baseline.toml; grep -n '= \[' memory/map/baseline.toml; for c in 9eff763dc 5f28bd0f1 a4caea91c 9d41abb16 22f3e12c1 3b5f9b116 c09646577 49d2dc60e 83269a93e; do echo "== $c"; git show $c -- memory/map/baseline.toml | grep -E '^-\s+"' | tr '\n' ' '; echo; git show --stat --format= $c | tail -1; done
````

9. Bash

````text
ls memory/map/features | wc -l; ls memory/map/generated; cat memory/map/affordance-exempt.toml | grep -cE '^\s*"|^[a-z]'; head -20 memory/map/affordance-exempt.toml; git log --reverse --format='%h %ad' --date=short -- memory/map/affordance-exempt.toml | head -2; for c in $(git log --reverse --format='%h' -- memory/map/affordance-exempt.toml); do echo "$c $(git show -s --format=%ad --date=short $c) $(git show $c:memory/map/affordance-exempt.toml | grep -cE '^\s+\"')"; done
````

10. Bash

````text
python -c "
import json;d=json.load(open('memory/map/generated/inventories.json'));
print(type(d), list(d)[:5] if isinstance(d,dict) else len(d))
tot=0
for k,v in (d.items() if isinstance(d,dict) else []):
  n=len(v) if hasattr(v,'__len__') else v; tot+= n if isinstance(n,int) else 0; print(k,n)
print('total',tot)" ; git show f9cf666c8 --stat --format= | grep -c 'features/'; git show f9cf666c8:memory/map/generated/inventories.json 2>/dev/null | python -c "import json,sys;d=json.load(sys.stdin);print('at adoption', sum(len(v) for v in d.values()))"
````

11. Bash

````text
python -c "
import json;d=json.load(open('memory/map/generated/inventories.json'))['inventories'];
print({k:len(v) for k,v in d.items()}, sum(len(v) for v in d.values()))"; git show f9cf666c8:memory/map/generated/inventories.json | python -c "
import json,sys;d=json.load(sys.stdin)['inventories'];print({k:len(v) for k,v in d.items()}, sum(len(v) for v in d.values()))"; git show f9cf666c8 --stat --format= | grep features/ 
````

12. Bash

````text
sed -n 34,66p memory/map/baseline.toml; for k in agent-instructions drift-audit lib pytest-parallel-guardrails workflows; do echo "$k last=$(git log -1 --format=%ad --date=short -- tools/$k) commits90=$(git log --since=2026-07-19 --format=%h -- tools/$k | wc -l)"; done
````

13. Bash

````text
ls tools/codebase-map/; grep -n 'baseline' tools/codebase-map/test_codebase_map.py | head -40
````

14. Bash

````text
sed -n 136,200p tools/codebase-map/test_codebase_map.py; grep -n 'drop-affordance-exempt\|def drop_\|affordance_exempt' tools/codebase-map/map_diff.py | head; grep -rn 'drop-affordance-exempt' --include=*.sh --include=*.py --include=*.js --include=*.json tools .claude .github | grep -v '^tools/codebase-map/map_diff.py' | head
````

15. Bash

````text
grep -oE '\b[A-Z][A-Z0-9_]*_CUTOFF\b' -r tools .memory-tree.conf 2>/dev/null | awk -F: '{print $NF}' | sort -u | tr '\n' ' '; echo; echo; grep -oE '\b[A-Z][A-Z0-9_]*_PIN\b' -r tools .memory-tree.conf 2>/dev/null | awk -F: '{print $NF}' | sort -u | wc -l; ls .memory-tree.conf 2>/dev/null; grep -cE '_CUTOFF=' .memory-tree.conf; grep -cE '_PIN=' .memory-tree.conf; grep -E '_CUTOFF=' .memory-tree.conf
````

16. Bash

````text
for f in tools/*waivers*.txt tools/template-size-highwater.txt tools/line-length-limits.txt memory/project/*.txt memory/map/affordance-exempt.toml; do echo "$f $(grep -cvE '^\s*(#|$)' $f) firstcommit=$(git log --reverse --format=%ad --date=short -- $f | head -1)"; done; grep -E '_PIN=' .memory-tree.conf
````

17. Bash

````text
for f in memory/project/spawn-idiom-sites.txt memory/project/unarmed-branches.txt memory/project/substitution-fed-loops.txt memory/project/encoding-posture-sites.txt tools/dead-path-waivers.txt memory/project/testsuite-count-waivers.txt memory/project/spec-token-waivers.txt tools/template-size-highwater.txt; do first=$(git log --reverse --format=%h -- $f | head -1); n0=$(git show $first:$f | grep -cvE '^\s*(#|$)'); nmax=0; for c in $(git log --format=%h -- $f); do x=$(git show $c:$f 2>/dev/null | grep -cvE '^\s*(#|$)'); [ $x -gt $nmax ] && nmax=$x; done; echo "$f first=$n0 max=$nmax now=$(grep -cvE '^\s*(#|$)' $f) commits=$(git log --format=%h -- $f | wc -l)"; head -5 $f | cut -c1-150; done 2>&1 | head -80
````

18. Bash

````text
for f in memory/project/spawn-idiom-sites.txt memory/project/substitution-fed-loops.txt memory/project/unarmed-branches.txt; do echo "== $f"; for c in $(git log --reverse --format=%h -- $f); do echo "$c $(git show -s --format=%ad --date=short $c) $(git show $c:$f | grep -cvE '^\s*(#|$)') $(git show -s --format=%s $c | cut -c1-90)"; done | head -34; done
````

19. Bash

````text
grep -rlnE 'touched (file|block|path)|files? (the|this) (branch|range) touch|diff --name-only' tools --include=*.py --include=*.sh | grep -v test | head -30
````

20. Bash

````text
python -c "
import json;d=json.load(open('tools/gate-legs.json'));
print(type(d), list(d)[:10] if isinstance(d,dict) else '')
legs=d['legs'] if isinstance(d,dict) and 'legs' in d else d
print(len(legs)); print(json.dumps(legs[0],indent=1)[:800])
import collections; c=collections.Counter(tuple(sorted(l.keys())) for l in legs); print(c.most_common(5))
print('with watch', sum(1 for l in legs if l.get('watch') or l.get('guard') or l.get('paths')))
"
````

21. Bash

````text
python -c "
import json,collections;legs=json.load(open('tools/gate-legs.json'))
g=[l for l in legs if 'guard' in l]; print(len(g)); print(json.dumps(g[0]['guard'])[:300]); print(collections.Counter(l['subject'] for l in legs))
"; grep -n 'guard' tools/run-gates/run-gates.sh | head -20
````

22. Bash

````text
git log --reverse --format=%ad --date=short | head -1; git rev-list --count HEAD; git ls-files | grep -vE '^memory/' | grep -E '\.(py|sh|js|mjs|cjs|ts)$' > /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/code.txt; wc -l < /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/code.txt; git ls-files | grep -vE '^memory/' | grep -E '\.(py|sh|js|mjs|cjs|ts)$' | cut -d/ -f1 | sort | uniq -c
````

23. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; git log --since=2026-09-17 --name-only --format= | sort -u > $S/t30; git log --since=2026-07-19 --name-only --format= | sort -u > $S/t90; git log --name-only --format= | sort | uniq -c | awk '{print $2"\t"$1}' > $S/tall; sort $S/code.txt > $S/code.s; echo "30d $(comm -12 $S/code.s $S/t30 | wc -l)"; echo "90d $(comm -12 $S/code.s $S/t90 | wc -l)"; awk -F'\t' 'NR==FNR{c[$1]=$2;next}{print $0"\t"c[$0]}' $S/tall $S/code.s > $S/codecount; awk -F'\t' '$2==1' $S/codecount | wc -l; awk -F'\t' '{print $2}' $S/codecount | sort -n | awk '{a[NR]=$1}END{print "median commits/file",a[int(NR/2)], "p90", a[int(NR*0.9)], "max", a[NR]}'
````

24. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; now=$(date -d 2026-10-17 +%s); : > $S/ages; while read f; do git blame --line-porcelain -- "$f" 2>/dev/null | awk -v n=$now '/^author-time /{print int((n-$2)/86400)}' >> $S/ages; done < $S/code.s; wc -l < $S/ages; awk '{t++; if($1<=7)a++; if($1<=30)b++; if($1<=90)c++} END{printf "lines=%d <=7d %.1f%% <=30d %.1f%% <=90d %.1f%% >90d %.1f%%\n",t,100*a/t,100*b/t,100*c/t,100*(t-c)/t}' $S/ages
````

25. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; git log --since=2026-09-17 --name-only --format= | grep -Fxf $S/code.s | sort | uniq -c | sort -rn > $S/c30; awk '{s+=$1; a[NR]=$1} END{n=NR; k=int(n*0.2); for(i=1;i<=k;i++) t+=a[i]; printf "files=%d events=%d top20%%(%d files) share=%.1f%%\n", n, s, k, 100*t/s}' $S/c30; head -8 $S/c30
````

26. Bash

````text
ls /c/Users/d41ly/.claude/projects/ | grep -i coding-gov | head; for d in $(ls -d /c/Users/d41ly/.claude/projects/*coding-governance* | head -40); do echo "$d $(find $d -name '*.jsonl' -newermt 2026-09-17 | wc -l)"; done | sort -k2 -n | tail -5
````

27. Bash

````text
find /c/Users/d41ly/.claude/projects/ -path '*coding-governance*' -name '*.jsonl' -newermt 2026-09-17 | grep -v scratchpad | wc -l; find /c/Users/d41ly/.claude/projects/ -path '*coding-governance*' -name '*.jsonl' -newermt 2026-09-17 | grep -v scratchpad | xargs du -cm | tail -1
````

28. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && git log --format='@%ad' --date=short --name-only > $S/hist.txt && cat > $S/reads.py <<'EOF'
import json,sys,os,re,glob,datetime,collections
S=sys.argv[1]
code=set(l.strip() for l in open(S+'/code.s'))
hist=collections.defaultdict(list); d=None
for l in open(S+'/hist.txt',encoding='utf-8'):
    l=l.strip()
    if l.startswith('@'): d=datetime.date.fromisoformat(l[1:]); continue
    if l in code: hist[l].append(d)
top=set()
for l in open(S+'/c30'):
    pass
c30=[l.split() for l in open(S+'/c30')]; top=set(p for _,p in c30[:46])
pat=re.compile(r'(?:coding-governance(?:/\.claude/worktrees/[^/]+)?/)?((?:tools|skills|\.githooks)/[\w./-]+\.(?:py|sh|js|mjs|cjs|ts))')
files=[f for f in glob.glob(os.path.expanduser('~/.claude/projects/*coding-governance*/**/*.jsonl'),recursive=True) if 'scratchpad' not in f and os.path.getmtime(f)>datetime.datetime(2026,9,17).timestamp()]
n=collections.Counter(); kinds=collections.Counter()
for f in files:
  for line in open(f,encoding='utf-8',errors='ignore'):
    if '"tool_use"' not in line: continue
    try: o=json.loads(line)
    except: continue
    ts=o.get('timestamp','')[:10]
    if not ts: continue
    t=datetime.date.fromisoformat(ts)
    for c in (o.get('message') or {}).get('content') or []:
      if not isinstance(c,dict) or c.get('type')!='tool_use': continue
      nm=c.get('name'); inp=c.get('input') or {}
      paths=[]
      if nm=='Read': paths=[inp.get('file_path','').replace('\\','/')]; k='Read'
      elif nm=='Bash':
        cmd=inp.get('command','')
        if not re.search(r'\b(cat|sed|head|tail|grep|rg|awk|less)\b',cmd): continue
        paths=[m.group(0) for m in re.finditer(r'[\w./\\:-]+',cmd)]; k='Bash'
      elif nm=='Grep': paths=[(inp.get('path') or '').replace('\\','/')]; k='Grep'
      else: continue
      seen=set()
      for p in paths:
        m=pat.search(p.replace('\\','/'))
        if not m: continue
        rel=m.group(1)
        if rel not in code or rel in seen: continue
        seen.add(rel)
        n['reads']+=1; kinds[k]+=1
        ds=[x for x in hist[rel] if x<=t]
        if any((t-x).days<=30 for x in ds): n['r30']+=1
        if any((t-x).days<=7 for x in ds): n['r7']+=1
        if rel in top: n['top']+=1
        n['files:'+rel]+=0
print(len(files),'transcripts', dict((k,v) for k,v in n.items() if not k.startswith('files:')), dict(kinds))
print('share<=30d %.1f%%  <=7d %.1f%%  top20%%churn %.1f%%' % (100*n['r30']/n['reads'],100*n['r7']/n['reads'],100*n['top']/n['reads']))
EOF
python $S/reads.py $S
````

29. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; cd $S && sed -i "s/replace('\\\\','\/')/replace(chr(92),'\/')/g; s/replace('\\\\\\\\','\/')/replace(chr(92),'\/')/g" reads.py; grep -n "replace(" reads.py | head; grep -n "\[\\\\w" reads.py
````

30. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; python $S/reads.py $S
````

31. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; for since in 2026-10-10 2026-09-30 2026-09-20; do echo "$since $(git log --since=$since --name-only --format= | sort -u | grep -Fxf $S/code.s | wc -l)/236"; done
````

32. Bash

````text
N=$(git rev-list --count HEAD); echo "commits $N"; echo "subject names an id: $(git log --format=%s | grep -cE '\b(TOOL|PLAY|KICK|DEPL)-[A-Za-z]+-[0-9]+')"; echo "subject has build slug in parens: $(git log --format=%s | grep -cE '^[a-z]+\([a-zA-Z]+')"; echo "conventional prefix: $(git log --format=%s | grep -cE '^(feat|fix|build|records|tools?|records|map|gotcha|merge|test|docs|chore|fold|review)(\(|:)')"; echo "merges $(git rev-list --merges --count HEAD)"; echo "body has Co-Authored-By: $(git log --format=%B | grep -c 'Co-Authored-By')"; git log --format=%B | grep -oE '^[A-Z][A-Za-z-]+: ' | sort | uniq -c | sort -rn | head -8; ls CODEOWNERS .github/CODEOWNERS docs/CODEOWNERS 2>&1 | head -3; ls -a | grep -iE 'editorconfig|shellcheck|ruff|flake|pylint|eslint|prettier|pyproject|setup.cfg|tox'
````

33. Bash

````text
git log --format=%B | grep -m3 '^Decided: '; git log --format=%B | grep '^Decided: ' | awk '{print length($0)}' | sort -n | awk '{a[NR]=$1}END{print "Decided median len",a[int(NR/2)]}'; git log --format='%h' --grep='^Decided: ' | head -1 | xargs git show -s --format=%ad --date=short; git log --format='%ad' --date=short --grep='^Decided: ' | tail -1; grep -cE '^\| ' memory/DECISIONS.md; grep -n 'Decided' tools/memory-tree/*.sh tools/memory-tree/*.py .githooks/* 2>/dev/null | head -5
````

34. Bash

````text
wc -lc memory/DECISIONS.md; sed -n 1,12p memory/DECISIONS.md | cut -c1-200; grep -cE '^- \*\*|^### |^- ' memory/DECISIONS.md; grep -cE '^- 20[0-9]{2}-' memory/DECISIONS.md; ls memory/; grep -rlE '^## (Status|Decision|Context|Consequences)' --include=*.md . | grep -v node_modules | wc -l
````

35. Bash

````text
grep -rlE '^## (Status|Decision|Context|Consequences)' --include=*.md . | sed 's#/[^/]*$##' | sort | uniq -c | sort -rn | head -6; echo; echo "py defs: $(git grep -hcE '^\s*def ' -- 'tools/*.py' 'skills/*.py' | paste -sd+ | bc)"; python - <<'EOF'
import ast,subprocess
fs=subprocess.run(['git','ls-files','tools/*.py','skills/*.py','.githooks/*.py'],capture_output=True,text=True).stdout.split()
d=ds=0;mods=mds=0
for f in fs:
    try: t=ast.parse(open(f,encoding='utf-8').read())
    except Exception: continue
    mods+=1; mds+= bool(ast.get_docstring(t))
    for n in ast.walk(t):
        if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
            d+=1; ds+= bool(ast.get_docstring(n))
print(f"py files {mods}, module docstrings {mds} ({100*mds/mods:.0f}%), defs {d}, with docstring {ds} ({100*ds/d:.0f}%)")
EOF
````

36. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; echo "gov:note lines: $(git grep -c 'gov:note' -- tools skills .githooks | wc -l)  gov:feature: $(git grep -nE '^\s*(#|//)\s*gov:feature' -- tools skills .githooks | wc -l)"; echo "comment lines citing an id: $(git grep -hE '^\s*(#|//).*\b(TOOL|PLAY|KICK|DEPL)-[A-Za-z]+-[0-9]+' -- 'tools/*' 'skills/*' '.githooks/*' | wc -l)"; echo "comment lines citing memory/ path: $(git grep -hE '^\s*(#|//).*memory/(gotchas|builds|DECISIONS)' -- 'tools/*' 'skills/*' '.githooks/*' | wc -l)"; tests=$(grep -cE '(\.test\.sh|selftest\.py|test_.*\.py|\.test\.js)$' $S/code.s); echo "test files $tests of 236"; nontest=$(grep -vE '(\.test\.sh|selftest\.py|test_.*\.py|\.test\.js)$' $S/code.s); paired=0; total=0; for f in $nontest; do total=$((total+1)); b=${f%.*}; e=${f##*.}; if [ -f "$b.test.$e" ] || [ -f "$(dirname $f)/test_$(basename $f)" ]; then paired=$((paired+1)); fi; done; echo "non-test $total, with a sibling test by name $paired"
````

37. Bash

````text
ls tools/drift-audit/ tools/lexicon/; grep -rn 'marginal' tools/drift-audit/*.py tools/lexicon/*.py | grep -v test | head -12
````

38. Bash

````text
sed -n 1,40p tools/drift-audit/drift_report.py | cut -c1-160; grep -nE 'write_text|open\(.*"w"|--write|--json|add_argument' tools/drift-audit/drift_report.py | head -20
````

39. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; git status --porcelain | wc -l; time (python tools/drift-audit/drift_report.py --json > $S/drift.json 2>$S/drift.err); git status --porcelain | wc -l; python -c "
import json;d=json.load(open(r'$S/drift.json'))
sig=d['signals'] if isinstance(d,dict) else d
print(len(sig))
for s in sig:
  n=s.get('signal'); 
  if any(k in n for k in ('lexicon','source_cited','shrink','handkept','legacy','baseline','stale')):
    print(n, 'value',s.get('value'),'of',s.get('of'),'tol',s.get('tolerance'),'gateable',s.get('gateable'),'live',s.get('live'))
"
````

40. Bash

````text
S='C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad'; ls -la "$S/drift.json"; python -c "
import json;d=json.load(open(r'$S/drift.json'))
sig=d['signals'] if isinstance(d,dict) else d
print(len(sig), type(d), list(d)[:5] if isinstance(d,dict) else '')
for s in sig:
  n=s.get('signal'); 
  if any(k in n for k in ('lexicon','source_cited','shrink','handkept','legacy','baseline','stale','unclaim')):
    print(n, 'value',s.get('value'),'of',s.get('of'),'tol',s.get('tolerance'),'gateable',s.get('gateable'),'live',s.get('live'))
"
````

41. Bash

````text
S='C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad'; python -c "
import json;d=json.load(open(r'$S/drift.json'))
for s in d:
  if s['signal'] in ('lexicon_marginal_offense_rate','shrink_only_lists_not_shrinking','source_cited_ids_resolving_to_no_record'):
    print(s['signal'], json.dumps(s.get('detail'))[:900]); print()
print([ (s['signal'],s.get('gateable')) for s in d])
"; grep -n 'SHRINK_ONLY\|shrink_only' tools/drift-audit/drift_signals.py | head
````

42. Bash

````text
git ls-files | grep -E '^(AGENTS\.md|CLAUDE\.md|coding-governance-agents\.template\.md|\.claude/(rules|agents|skills)/.*\.md|memory/guides/.*\.md|memory/(HYGIENE|TEMPLATE-SPEC)\.md|skills/.*\.md|tools/[^/]+/[^/]*(agent|SKILL)[^/]*\.md)$' > /tmp/x 2>/dev/null; S='C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad'; git ls-files | grep -E '^(AGENTS\.md|CLAUDE\.md|coding-governance-agents\.template\.md|\.claude/(rules|agents|skills)/.*\.md|memory/guides/.*\.md|memory/(HYGIENE|TEMPLATE-SPEC)\.md|skills/.*\.md|tools/[^/]+/[^/]*(agent|SKILL)[^/]*\.md)$' > "$S/instr.txt"; wc -l < "$S/instr.txt"; cat "$S/instr.txt" | xargs cat | wc -c; cut -d/ -f1-2 "$S/instr.txt" | sort | uniq -c; c30=0; while read f; do [ -n "$(git log -1 --since=2026-09-17 --format=%h -- "$f")" ] && c30=$((c30+1)); done < "$S/instr.txt"; echo "changed in 30d: $c30"; grep -c 'generated\|GENERATED\|do not edit' $(head -50 "$S/instr.txt") 2>/dev/null | awk -F: '$2>0' | wc -l
````

43. Bash

````text
S='C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad'; git ls-files | grep -E '^(AGENTS\.md|CLAUDE\.md|coding-governance-agents\.template\.md|\.claude/(rules|agents|skills)/.*\.md|memory/guides/.*\.md|memory/(HYGIENE|TEMPLATE-SPEC)\.md|skills/.*\.md|tools/[^/]+/[^/]*(agent|SKILL)[^/]*\.md)$' > "$S/instr.txt"; wc -l < "$S/instr.txt"; cat "$S/instr.txt" | xargs cat | wc -c; cut -d/ -f1-2 "$S/instr.txt" | sort | uniq -c; c30=0; while read f; do [ -n "$(git log -1 --since=2026-09-17 --format=%h -- "$f")" ] && c30=$((c30+1)); done < "$S/instr.txt"; echo "changed in 30d: $c30"
````

44. Bash

````text
for f in tools/*waivers*.txt tools/template-size-highwater.txt tools/line-length-limits.txt memory/project/*.txt memory/map/baseline.toml memory/map/affordance-exempt.toml; do b=$(basename $f); r=$(git grep -l -F "$b" -- 'tools/*.py' 'tools/*.sh' 'tools/*.js' ':!*test*' ':!*selftest*' | head -3 | tr '\n' ' '); echo "$b <- $r"; done
````

45. Bash

````text
grep -hiE 'a row is|row is `|one `<|row shape|^# *`<' tools/*waivers*.txt memory/project/*.txt | cut -c1-120 | head -30; grep -n 'touch' memory/project/encoding-posture-sites.txt memory/project/substitution-fed-loops.txt memory/project/spawn-idiom-sites.txt | head
````

46. Bash

````text
git grep -l -E 'encoding-posture-sites|spawn-idiom-sites|location-probe-waivers|fork-ceilings' -- tools .githooks | head; git grep -n -E 'def .*(registry|sites|waiver).*\(' -- 'tools/*.py' | grep -viE 'test' | head -20
````

47. Bash

````text
sed -n 160,250p tools/gate-lint/encoding_posture.py; sed -n 380,400p tools/gate-lint/sh_hygiene.py; sed -n 440,475p tools/gate-lint/sh_hygiene.py
````

48. Bash

````text
S='C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad'; git log --since=2026-09-17 --no-merges --format='@%h' --name-only > "$S/c30names.txt"; python - "$S" <<'EOF'
import sys,collections,statistics
S=sys.argv[1]
reg=collections.Counter(); files_by=collections.defaultdict(set)
for f in ['memory/project/encoding-posture-sites.txt','memory/project/substitution-fed-loops.txt','memory/project/spawn-idiom-sites.txt','memory/project/location-probe-waivers.txt']:
    for row in open(f,encoding='utf-8'):
        if not row.strip() or row.startswith('#'): continue
        p=row.rstrip('\n').split('\t')
        if len(p)>=3 and p[2].strip().isdigit():
            reg[p[0]]+=int(p[2]); files_by[f].add(p[0])
print('legacy sites',sum(reg.values()),'in files',len(reg))
commits=[];cur=None
for l in open(S+'/c30names.txt',encoding='utf-8'):
    l=l.strip()
    if l.startswith('@'): cur=[]; commits.append(cur)
    elif l: cur.append(l)
code=[c for c in commits if any(x.startswith(('tools/','skills/','.githooks/')) for x in c)]
burd=[sum(reg.get(x,0) for x in c) for c in code]
hit=[b for b in burd if b>0]
print('commits30 non-merge',len(commits),'touching code',len(code),'carrying legacy sites',len(hit))
print('sites per code commit: median',statistics.median(burd),'mean %.1f'%statistics.mean(burd),'p90',sorted(burd)[int(.9*len(burd))],'max',max(burd))
touched=set(x for c in code for x in c)
print('legacy files touched in 30d',len(set(reg)&touched),'of',len(reg),'sites in them',sum(v for k,v in reg.items() if k in touched))
EOF
````

49. Bash

````text
S='C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad'; git log --since=2026-09-17 --no-merges --format='@%h' --numstat > "$S/c30num.txt"; python - "$S" <<'EOF'
import sys,collections,statistics,subprocess
S=sys.argv[1]
reg=collections.Counter()
for f in ['memory/project/encoding-posture-sites.txt','memory/project/substitution-fed-loops.txt','memory/project/spawn-idiom-sites.txt','memory/project/location-probe-waivers.txt']:
    for row in open(f,encoding='utf-8'):
        if not row.strip() or row.startswith('#'): continue
        p=row.rstrip('\n').split('\t')
        if len(p)>=3 and p[2].strip().isdigit(): reg[p[0]]+=int(p[2])
lines={}
for p in reg:
    try: lines[p]=sum(1 for _ in open(p,encoding='utf-8',errors='ignore'))
    except FileNotFoundError: pass
dens={p:reg[p]/max(lines.get(p,1),1) for p in reg}
commits=[];cur=None
for l in open(S+'/c30num.txt',encoding='utf-8'):
    l=l.rstrip('\n')
    if l.startswith('@'): cur={}; commits.append(cur)
    elif l.strip():
        a,d,p=l.split('\t',2)
        if a.isdigit(): cur[p]=int(d)  # removed/modified lines approximate touched old lines
code=[c for c in commits if any(x.startswith(('tools/','skills/','.githooks/')) for x in c)]
burd=[sum(dens.get(p,0)*n for p,n in c.items()) for c in code]
print('hunk-scoped legacy sites per code commit: median %.2f mean %.2f p90 %.2f'%(statistics.median(burd),statistics.mean(burd),sorted(burd)[int(.9*len(burd))]))
print('overall density sites/line %.4f'%(sum(reg.values())/sum(lines.values())))
EOF
````

50. Bash

````text
ls tools/lib; grep -n 'def compute_coverage\|def derive_baseline_additions\|def resolve_compare_base\|def affordance_offenders' tools/codebase-map/map_lib.py; grep -n 'SHRINK_ONLY' -A 14 tools/drift-audit/drift_signals.py | sed -n 1,30p | cut -c1-140
````

51. Bash

````text
git grep -n -iE 'seed(s|ed)? (the )?(shrink-only|baseline|registry|pin)|--seed-|measure.*pin|CUTOFF=.*date' -- 'tools/*/adopt-*.sh' | cut -c1-170 | head -20; git grep -c -E '^def |^    def ' -- tools/govkit/census.py; sed -n 1,30p tools/govkit/census.py | cut -c1-160
````

52. Bash

````text
grep -n 'def build_cutoff_keys_armed' -A 25 tools/drift-audit/drift_report.py | cut -c1-150 | head -30; S='C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad'; python -c "
import json;d=json.load(open(r'$S/drift.json'))
for s in d:
  if s['signal'] in ('cutoff_keys_armed','dossiers_older_than_their_paths'): print(s['signal'],s['value'],s['of'],json.dumps(s.get('detail'))[:400])"
````

53. Bash

````text
echo "fix-subject commits: $(git log --no-merges --format=%s | grep -ciE '^fix')"; ls memory/gotchas | wc -l; echo "gotchas citing from: $(grep -l '^from:\|^\*\*From' memory/gotchas/*.md 2>/dev/null | wc -l)"; echo "gotchas naming a commit sha: $(grep -lE '\b[0-9a-f]{9,40}\b' memory/gotchas/*.md | wc -l)"; ls memory/builds | wc -l; find memory/builds -path '*spec/units/*.md' | wc -l
````

54. Bash

````text
S='C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad'; python - "$S" <<'EOF'
import sys,statistics,collections
S=sys.argv[1]
commits=[];cur=None
for l in open(S+'/c30names.txt',encoding='utf-8'):
    l=l.strip()
    if l.startswith('@'): cur=[]; commits.append(cur)
    elif l: cur.append(l)
code=[[x for x in c if x.startswith(('tools/','skills/','.githooks/'))] for c in commits]
code=[c for c in code if c]
n=[len(c) for c in code]
print('code files per code commit median',statistics.median(n),'p90',sorted(n)[int(.9*len(n))])
rows=collections.Counter(); byt=collections.Counter()
import glob
for f in glob.glob('memory/project/*.txt')+glob.glob('tools/*waivers*.txt'):
    for r in open(f,encoding='utf-8'):
        if r.strip() and not r.startswith('#'):
            p=r.split('\t')[0].strip(); rows[p]+=1; byt[p]+=len(r.encode())
b=[sum(byt.get(x,0) for x in c) for c in code]
print('registry rows bytes per commit write set: median',statistics.median(b),'p90',sorted(b)[int(.9*len(b))],'max',max(b))
EOF
````

55. Bash

````text
S='C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad'; time (while read f; do git blame --porcelain -- "$f" >/dev/null 2>&1; done < "$S/code.s"); echo "renames in history: $(git log --no-merges -M --diff-filter=R --name-status --format= | grep -c '^R')"; echo "commits renaming code: $(git log --no-merges -M --diff-filter=R --format=%h -- tools skills .githooks | wc -l)"; f=$(head -1 "$S/c30"); echo $f
````

56. Bash

````text
grep -n '^def \|^    return' tools/gate-lint/encoding_posture.py | head -30; git log --reverse --format='%h %ad' --date=short -- memory/project/encoding-posture-sites.txt | head -1
````

57. Bash

````text
sed -n 130,155p tools/gate-lint/encoding_posture.py; grep -n 'encoding posture' -A6 tools/gate-legs.json | head -12
````

58. Bash

````text
python - <<'EOF'
import sys,pathlib,subprocess,datetime
sys.path.insert(0,'tools/gate-lint')
import encoding_posture as ep
root=pathlib.Path('.')
hits,n=ep.scan_tree(root,['.','tools'])
hits=sorted(set(hits))
arm=datetime.datetime(2026,9,23).timestamp()
reg,_=ep.read_registry(pathlib.Path('memory/project/encoding-posture-sites.txt'))
old=new=0; newfiles=set()
for rel,line,col,a,w in hits:
    out=subprocess.run(['git','blame','--porcelain','-L',f'{line},{line}','--',rel],capture_output=True,text=True,encoding='utf-8').stdout
    t=int([l for l in out.splitlines() if l.startswith('author-time ')][0].split()[1])
    if t>=arm: new+=1; newfiles.add(rel)
    else: old+=1
print('scanned',n,'hits',len(hits),'registry sites',sum(reg.values()),'hit lines blamed before arming',old,'after arming',new,'files',sorted(newfiles)[:6])
EOF
````

59. Bash

````text
grep -n 'fetch-depth\|checkout' .github/workflows/remote-ci.yml | head
````

60. Bash

````text
git grep -n -iE 'gained (a )?(row|key)|rows? (it|the base) did not|grew against|never (rise|grow)s? against' -- 'tools/*.py' 'tools/*.sh' ':!*test*' ':!*selftest*' | cut -c1-160 | head
````

61. Bash

````text
grep -n -iE 'shrink|rise|base' tools/check-spec-tokens.py | head -12; grep -n -iE 'shrink-only|regrow|seed' tools/memory-tree/check-arms.py | head -8
````

62. Bash

````text
git grep -n 'drop-affordance-exempt\|drop_affordance' -- . ':!memory/builds' | grep -v 'tools/codebase-map/map_diff.py' | cut -c1-140; sed -n 550,554p WIRE-INTO-PROJECT.md | cut -c1-140; S='C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad'; python - "$S" <<'EOF'
import sys,collections
S=sys.argv[1]
reg=collections.Counter()
for f in ['memory/project/encoding-posture-sites.txt','memory/project/substitution-fed-loops.txt','memory/project/spawn-idiom-sites.txt','memory/project/location-probe-waivers.txt']:
    for row in open(f,encoding='utf-8'):
        if row.strip() and not row.startswith('#'):
            p=row.rstrip('\n').split('\t')
            if len(p)>=3 and p[2].strip().isdigit(): reg[p[0]]+=int(p[2])
lines={p:max(1,sum(1 for _ in open(p,encoding='utf-8',errors='ignore'))) for p in reg if __import__('os').path.exists(p)}
cur=None;b=[]
for l in open(S+'/c30num.txt',encoding='utf-8'):
    l=l.rstrip('\n')
    if l.startswith('@'):
        cur=[0.0,False]; b.append(cur)
    elif l.strip():
        a,d,p=l.split('\t',2)
        if p.startswith(('tools/','skills/','.githooks/')): cur[1]=True
        if d.isdigit() and p in lines: cur[0]+=reg[p]/lines[p]*int(d)
v=sorted(x for x,c in b if c); print('max %.1f  p99 %.1f  share>20 %.4f'%(v[-1],v[int(.99*len(v))],sum(1 for x in v if x>20)/len(v)))
EOF
````

## [run-b] Run B, dispatch 84

1. Bash

````text
ls memory/builds/dClosedLoop/build/ | grep -E "architecture-v2|layer-|flow-|systems" ; wc -c memory/builds/dClosedLoop/build/*systems* memory/builds/dClosedLoop/build/*layer-expansions* memory/builds/dClosedLoop/build/*layer-memory* memory/builds/dClosedLoop/build/*layer-library* memory/builds/dClosedLoop/build/*flow-steps*
````

2. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && for f in *systems.md *layer-expansions.md *layer-memory.md *layer-library.md *flow-steps.md; do echo "== $f"; grep -nE '^#+ |^\[[a-z-]+\]|\{#|<a id|\[[a-z0-9-]+\]$' $f | head -80; done
````

3. Bash

````text
wc -l memory/builds/aDeployScout/spec/governance-deployer-research.md WIRE-INTO-PROJECT.md; grep -niE 'retrofit|existing (repo|code|project)|brownfield|legacy|baseline' memory/builds/aDeployScout/spec/governance-deployer-research.md | head -40; echo ===; grep -niE 'retrofit|existing (repo|code|project)|brownfield|legacy|baseline|already has' WIRE-INTO-PROJECT.md | head -40
````

4. Bash

````text
sed -n 15,40p memory/builds/aDeployScout/spec/governance-deployer-research.md; echo ====; sed -n 265,290p WIRE-INTO-PROJECT.md; echo ===; sed -n 340,350p WIRE-INTO-PROJECT.md; echo ===; sed -n 400,420p WIRE-INTO-PROJECT.md; echo; sed -n 535,550p WIRE-INTO-PROJECT.md; echo ===; sed -n 2100,2120p WIRE-INTO-PROJECT.md
````

5. Bash

````text
wc -lc memory/map/baseline.toml; head -30 memory/map/baseline.toml; echo; git log --follow --format='%h %ad %s' --date=short -- memory/map/baseline.toml | wc -l; git log --follow --format='%h %ad %s' --date=short -- memory/map/baseline.toml | tail -5
````

6. Bash

````text
cat > "$TMPDIR/bl.py" 2>/dev/null || true; S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; mkdir -p $S; for c in $(git log --follow --format='%h' -- memory/map/baseline.toml); do d=$(git log -1 --format=%ad --date=short $c); p=$(git log -1 --format=%s $c | cut -c1-70); n=$(git show $c:memory/map/baseline.toml 2>/dev/null | grep -cE '^\s+"'); echo "$d $c keys=$n $p"; done
````

7. Bash

````text
for c in $(git log --follow --format='%h' -- memory/map/baseline.toml); do d=$(git log -1 --format=%ad --date=short $c); p=$(git log -1 --format=%s $c | cut -c1-75); n=$(git show $c:memory/map/baseline.toml 2>/dev/null | grep -cE '^\s+"'); echo "$d $c keys=$n $p"; done
````

8. Bash

````text
for c in 9eff763dc 5f28bd0f1 a4caea91c b0f5247a9 9d41abb16 22f3e12c1 3b5f9b116 c09646577 49d2dc60e 54c8d081f 83269a93e; do echo "== $c removed: $(git show $c -- memory/map/baseline.toml | grep -cE '^-\s+"') added: $(git show $c -- memory/map/baseline.toml | grep -cE '^\+\s+"') dossier-files: $(git show --name-only --format= $c | grep -c 'memory/map/features/')"; done; ls memory/map; python -c "import json;d=json.load(open('memory/map/generated/inventories.json'));print({k:len(v) for k,v in d.items() if isinstance(v,(list,dict))})" 2>&1 | head -5
````

9. Bash

````text
python -c "
import json;d=json.load(open('memory/map/generated/inventories.json'))['inventories']
t=0
for k,v in d.items():
  n=len(v) if isinstance(v,(list,dict)) else v; t+=n if isinstance(n,int) else 0; print(k, n if isinstance(n,int) else type(v))
print('total',t)"; grep -E '^[a-z-]+ = \[' memory/map/baseline.toml; ls memory/map/features | wc -l; wc -l memory/map/affordance-exempt.toml; git log --format='%h %ad' --date=short -- memory/map/affordance-exempt.toml | tail -1; git log --format=%h -- memory/map/affordance-exempt.toml | while read c; do echo "$c $(git show $c:memory/map/affordance-exempt.toml | grep -cE '^\s*\"|^[a-z]')"; done
````

10. Bash

````text
git show f9cf666c8:memory/map/generated/inventories.json | python -c "import json,sys;d=json.load(sys.stdin)['inventories'];print({k:len(v) for k,v in d.items()}, sum(len(v) for v in d.values()))"; git show f9cf666c8 --stat --format='%s' | tail -3; git show f9cf666c8:memory/map/baseline.toml | grep -E '^[a-z-]+ = \[' ; git show f9cf666c8:memory/map/baseline.toml | sed -n '/^\[/,$p' | head -0; git show 83269a93e:memory/map/baseline.toml | python - <<'E'
import sys,re
E
python - <<'E'
import re
s=open('memory/map/baseline.toml').read()
for m in re.finditer(r'^([a-z-]+) = \[(.*?)\]',s,re.S|re.M): print(m.group(1), len(re.findall(r'"',m.group(2)))//2)
E
````

11. Bash

````text
python - <<'E'
import re,subprocess
def keys(s): return set(re.findall(r'^\s+"([^"]+)"',s,re.M))
a=keys(subprocess.run(['git','show','f9cf666c8:memory/map/baseline.toml'],capture_output=True,text=True,encoding='utf-8').stdout)
b=keys(open('memory/map/baseline.toml',encoding='utf-8').read())
print(len(a),len(b),'still from seed',len(a&b),'new in baseline',len(b-a))
print(sorted(b)[:40])
E
````

12. Bash

````text
for k in agent-instructions drift-audit lib pytest-parallel-guardrails workflows; do echo "$k commits-since-seed: $(git log --since=2026-08-09 --format=%h -- tools/$k | wc -l)"; done; for k in absence-assertion-over-whole-file-text concurrency-is-not-a-budget fixture-passes-by-finding-nothing vacuous-selector-empty-population; do echo "$k: $(git log --since=2026-08-09 --format=%h -- memory/gotchas/$k.md | wc -l)"; done
````

13. Bash

````text
grep -nE 'add_argument|write_text|open\(.*"w' tools/drift-audit/drift_report.py | head -30
````

14. Bash

````text
PY=$(bash -c 'source tools/lib/resolve-python.sh >/dev/null 2>&1; echo ${PY:-python}'); time python tools/drift-audit/drift_report.py --json > /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/drift.json 2>/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/drift.err; echo rc=$?; git status --porcelain | head
````

15. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad && python - <<'E'
import json
d=json.load(open('drift.json',encoding='utf-8'))
sig=d.get('signals',d) if isinstance(d,dict) else d
if isinstance(sig,dict): sig=list(sig.values())
for s in sig:
    if not isinstance(s,dict): continue
    print(f"{s.get('signal'):55} v={s.get('value')} of={s.get('of')} tol={s.get('tolerance')} gate={s.get('gateable')} live={s.get('live')}")
E
````

16. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad && python - <<'E'
import json
d=json.load(open('drift.json',encoding='utf-8'))
sig=d.get('signals',d)
if isinstance(sig,dict): sig=list(sig.values())
for s in sig:
  if s.get('signal') in ('lexicon_marginal_offense_rate','shrink_only_lists_not_shrinking'):
    det=s.get('detail')
    print(s['signal'], json.dumps(det if not isinstance(det,list) else det[:6],ensure_ascii=False)[:1800]); print()
E
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && grep -nE 'PIN|RATIFIED' .lexicon.conf | head; git log --diff-filter=A --format='%h %ad' --date=short -- .lexicon.conf
````

17. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad && python - <<'E'
import json
d=json.load(open('drift.json',encoding='utf-8'))
for s in d:
  if s.get('signal') in ('lexicon_marginal_offense_rate','shrink_only_lists_not_shrinking'):
    det=s.get('detail')
    print(s['signal'], json.dumps(det[:5] if isinstance(det,list) else det,ensure_ascii=False)[:1500]); print()
E
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && for c in $(git log --format=%h -S'VERB_OFFENDER_PIN=' -- .lexicon.conf); do echo "$(git log -1 --format='%ad' --date=short $c) $c $(git show $c:.lexicon.conf | grep -E '^VERB_OFFENDER_PIN')"; done
````

18. Bash

````text
git log --format=%h -G'^VERB_OFFENDER_PIN=' -- .lexicon.conf | while read c; do echo "$(git log -1 --format='%ad' --date=short $c) $c $(git show $c:.lexicon.conf | grep -E '^VERB_OFFENDER_PIN')"; done | head -20; git log --format=%h -G'^VERB_OFFENDER_PIN=' -- .lexicon.conf | wc -l
````

19. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -nE 'legacy list|hand-written|shrink-only list|handwritten' 2026-10-16-build-PLAY-dClosedLoop-1-systems.md | head; sed -n 130,142p 2026-10-16-build-PLAY-dClosedLoop-1-systems.md
````

20. Bash

````text
for g in "memory/guides/*.md" "memory/TEMPLATE-SPEC.md memory/HYGIENE.md" ".claude/rules/*.md" ".claude/agents/*.md" ".claude/skills/*/SKILL.md" "AGENTS.md CLAUDE.md"; do n=$(ls $g 2>/dev/null | wc -l); b=$(cat $g 2>/dev/null | wc -c); echo "$g files=$n bytes=$b"; done; ls .claude/
````

21. Bash

````text
for f in AGENTS.md CLAUDE.md .claude/rules/*.md .claude/agents/*.md .claude/skills/*/SKILL.md memory/guides/*.md memory/TEMPLATE-SPEC.md memory/HYGIENE.md; do if head -c 3000 "$f" | grep -qiE 'generated|rendered by|do not edit|gov:render|BEGIN gov'; then r=R; else r=H; fi; echo "$r $(wc -c <"$f") $f"; done | sort | awk '{s[$1]+=$2; n[$1]++; print} END{for(k in s) print "TOTAL",k,n[k],s[k]}'
````

22. Bash

````text
git ls-files | grep -E '\.(py|sh|js|mjs|cjs|ts|ps1)$' > /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/code.txt; wc -l < /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/code.txt; git log -1 --format=%ad --date=short; git log --reverse --format=%ad --date=short | head -1; for d in 30 90 365; do git log --since="$d days ago" --name-only --format= | sort -u > /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/ch$d.txt; echo "$d days: $(grep -cxFf /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/ch$d.txt /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/code.txt)"; done
````

23. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; git log --since="7 days ago" --name-only --format= | sort -u > $S/ch7.txt; echo "7 days: $(grep -cxFf $S/ch7.txt $S/code.txt)"; git log --format=%H --name-only --since=2026-06-01 > $S/log.txt; python - "$S" <<'E'
import sys,collections,subprocess
S=sys.argv[1]
code=set(open(S+'/code.txt').read().split())
cnt=collections.Counter()
for line in open(S+'/log.txt',encoding='utf-8',errors='replace'):
    l=line.strip()
    if l in code: cnt[l]+=1
once=[f for f in code if cnt[f]<=1]
print('code files',len(code),'touched once (landed, never changed):',len(once))
vals=sorted((cnt[f] for f in code),reverse=True); tot=sum(vals)
for p in (0.1,0.2,0.5):
    k=int(len(vals)*p); print(f'top {int(p*100)}% files hold {sum(vals[:k])/tot:.1%} of file-touches')
import statistics; print('median touches',statistics.median(vals),'total',tot)
E
````

24. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; git log --format='C %ad' --date=short --name-only --diff-filter=AM > $S/dated.txt; python - "$S" <<'E'
import sys,collections,datetime as dt
S=sys.argv[1]; code=set(open(S+'/code.txt').read().split())
first={};last={};d=None
for line in open(S+'/dated.txt',encoding='utf-8',errors='replace'):
    l=line.strip()
    if l.startswith('C '): d=dt.date.fromisoformat(l[2:]); continue
    if l in code:
        first[l]=min(first.get(l,d),d); last[l]=max(last.get(l,d),d)
today=dt.date(2026,10,17)
for age in (30,60,90):
    old=[f for f in code if f in first and (today-first[f]).days>age]
    stale=[f for f in old if (today-last[f]).days>30]
    print(f'files landed >{age}d ago: {len(old)}; unchanged in last 30d: {len(stale)} ({len(stale)/max(1,len(old)):.0%})')
E
````

25. Bash

````text
ls /c/Users/d41ly/.claude/projects/ | grep -i coding-governance | head; ls /c/Users/d41ly/.claude/projects/C--projects-coding-governance 2>/dev/null | wc -l
````

26. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; cat > $S/reads.py <<'E'
import sys,os,json,re,glob,datetime as dt,collections,bisect
S=sys.argv[1]; root='/c/Users/d41ly/.claude/projects'
code=set(open(S+'/code.txt').read().split())
# per-file change dates (code files)
dates=collections.defaultdict(list); d=None
for line in open(S+'/dated.txt',encoding='utf-8',errors='replace'):
    l=line.strip()
    if l.startswith('C '): d=dt.date.fromisoformat(l[2:]); continue
    if l in code: dates[l].append(d)
for k in dates: dates[k].sort()
cut=dt.datetime(2026,9,17).timestamp()
files=[f for p in glob.glob(root+'/C--projects-coding-governance*') for f in glob.glob(p+'/**/*.jsonl',recursive=True) if os.path.getmtime(f)>cut]
rx=re.compile(r'(?:^|[\s"\'=/])((?:tools|skills|\.claude|\.github)/[\w./-]+\.(?:py|sh|js|mjs|cjs|ts|ps1))')
def norm(p):
    p=p.replace('\\','/')
    m=re.search(r'((?:tools|skills|\.claude|\.github)/[\w./-]+)$',p)
    return m.group(1) if m else None
stats=collections.Counter(); bucket=collections.Counter(); filecount=collections.Counter()
for f in files:
  for line in open(f,encoding='utf-8',errors='replace'):
    if '"tool_use"' not in line: continue
    try: o=json.loads(line)
    except: continue
    ts=o.get('timestamp');
    if not ts: continue
    t=dt.date.fromisoformat(ts[:10])
    for c in (o.get('message') or {}).get('content') or []:
      if not isinstance(c,dict) or c.get('type')!='tool_use': continue
      paths=[]
      if c['name']=='Read': 
          p=norm(c['input'].get('file_path','')); paths=[p] if p else []; kind='Read'
      elif c['name']=='Bash' and re.match(r'\s*(?:cd [^;&]*(?:&&|;)\s*)?(sed|cat|head|tail|grep|rg)\b',c['input'].get('command','')):
          paths=list(set(rx.findall(c['input']['command']))); kind='Bash'
      elif c['name']=='Grep':
          p=norm(c['input'].get('path','') or ''); paths=[p] if p else []; kind='Grep'
      else: continue
      for p in paths:
        if p not in code: continue
        stats[kind]+=1; filecount[p]+=1
        ds=dates.get(p,[])
        i=bisect.bisect_right(ds,t)
        prior=ds[:i]
        age=(t-prior[-1]).days if prior else 9999
        for w in (7,30,90):
            if age<=w: bucket[w]+=1
        bucket['all']+=1
print('transcripts',len(files),'code reads by tool',dict(stats))
for w in (7,30,90): print(f'reads on a file changed within {w}d before the read: {bucket[w]}/{bucket["all"]} = {bucket[w]/bucket["all"]:.1%}')
v=sorted(filecount.values(),reverse=True); tot=sum(v)
print('distinct code files read',len(v),'of',len(code))
for p in (0.1,0.2): k=int(len(code)*p); print(f'top {int(p*100)}% of code files ({k}) take {sum(v[:k])/tot:.1%} of reads')
E
python $S/reads.py $S
````

27. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; sed -i "s/p=p.replace('.','\/')/p=p.replace(chr(92),'\/')/" $S/reads.py; sed -n 15p $S/reads.py; grep -n "root=" $S/reads.py; python $S/reads.py $S
````

28. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; sed -i "s#root='/c/Users/d41ly/.claude/projects'#root='C:/Users/d41ly/.claude/projects'#" $S/reads.py; python $S/reads.py $S
````

29. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; cat >> $S/reads.py <<'E'
touch=collections.Counter()
for line in open(S+'/log.txt',encoding='utf-8',errors='replace'):
    l=line.strip()
    if l in code: touch[l]+=1
top=set(f for f,_ in touch.most_common(int(len(code)*0.2)))
print('reads landing on the top-20% most-touched files:', f"{sum(n for f,n in filecount.items() if f in top)/tot:.1%}")
unread=[f for f in code if f not in filecount]; print('code files never read in 30d of transcripts:',len(unread))
E
python $S/reads.py $S 2>&1 | tail -2
````

30. Bash

````text
echo "commits: $(git rev-list --count HEAD)"; echo "with Decided: trailer: $(git log --format=%B | grep -cE '^Decided:')"; echo "commits carrying a unit id in subject: $(git log --format=%s | grep -cE '(TOOL|PLAY|KICK|DEPL)-[a-zA-Z]+-[0-9]+')"; echo "conventional-type subject: $(git log --format=%s | grep -cE '^[a-z]+(\([^)]*\))?!?: ')"; echo "Co-Authored-By trailers: $(git log --format=%B | grep -c '^Co-Authored-By:')"; ls -a | grep -iE 'codeowners|editorconfig|ruff|flake8|pylintrc|eslint|shellcheck|pyproject|setup.cfg|prettier'; ls .github; ls .github/* | head; git ls-files | grep -iE 'CODEOWNERS|\.shellcheckrc|ruff.toml|\.eslintrc|pyproject.toml|setup.cfg|\.editorconfig' 
````

31. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; echo "test files: $(grep -cE '(selftest|test)[^/]*\.(py|sh|js)$|/tests?/' $S/code.txt)"; echo "DECISIONS rows: $(grep -cE '^\| *D?[0-9]|^- \*\*D|^\| [0-9]{4}-' memory/DECISIONS.md)"; head -c 1500 memory/DECISIONS.md | tail -c 900; echo; grep -rlE '^#+ *(Decision|Status|Consequences|Context)\b' memory --include=*.md | grep -v builds/ | head; echo "build records with a Decision heading: $(grep -rlE '^#+ .*\b(Decision|Decisions)\b' memory/builds --include=*.md | wc -l)"; echo "gotcha class records: $(ls memory/gotchas/*.md | wc -l)"; echo "gov:note lines: $(git grep -c 'gov:note' -- tools skills | wc -l) gov:feature: $(git grep -nE 'gov:feature [a-z]' -- tools skills ':!*.md' | wc -l)"
````

32. Bash

````text
echo "DECISIONS bullet rows: $(grep -cE '^- ' memory/DECISIONS.md) bytes $(wc -c < memory/DECISIONS.md)"; echo "rows citing an id: $(grep -cE '^- .*(TOOL|PLAY|KICK|DEPL)-[a-zA-Z]+-[0-9]+' memory/DECISIONS.md)"; echo "rows marked owner: $(grep -cE '^- .*\(owner' memory/DECISIONS.md)"; git log --format=%B | grep -E '^Decided:' | head -3; git log --format=%B | grep -E '^Decided:' | awk '{print length}' | sort -n | awk '{a[NR]=$1} END{print "Decided median len",a[int(NR/2)]}'
````

33. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; python - "$S" <<'E'
import sys,ast,re
S=sys.argv[1]; code=open(S+'/code.txt').read().split()
py=[f for f in code if f.endswith('.py')]; sh=[f for f in code if f.endswith('.sh')]; js=[f for f in code if f.endswith(('.js','.mjs','.cjs'))]
doc=0; defs=0; ddoc=0
for f in py:
    try: t=ast.parse(open(f,encoding='utf-8').read())
    except Exception: continue
    if ast.get_docstring(t): doc+=1
    for n in ast.walk(t):
        if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
            defs+=1; ddoc+= bool(ast.get_docstring(n))
def head(f,mark):
    L=open(f,encoding='utf-8',errors='replace').read().splitlines()[:15]
    return sum(1 for l in L if l.strip().startswith(mark))>=3
print(f'py {len(py)} with module docstring {doc} ({doc/len(py):.0%}); defs {defs} with docstring {ddoc} ({ddoc/defs:.0%})')
print(f'sh {len(sh)} with >=3 header comment lines {sum(head(f,"#") for f in sh)}')
print(f'js {len(js)} with >=3 header comment lines {sum(head(f,("//","*","/*")) for f in js)}')
E
````

34. Bash

````text
python -c "
import json;d=json.load(open('tools/gate-legs.json'))
legs=d['legs'] if isinstance(d,dict) and 'legs' in d else d
print(len(legs)); print(list(legs[0].keys()) if isinstance(legs,list) else list(d.keys())[:10])
for l in legs: print(l.get('name') or l.get('label'))
" | head -160
````

35. Bash

````text
python -c "
import json;d=json.load(open('tools/gate-legs.json'))
legs=d['legs'] if isinstance(d,dict) else d
want=['line length','shell hygiene (a loop fed by a command substitution)','shell hygiene (a fork spent on builtin work)','spawn budget (forks per hot entrypoint)','encoding posture (text IO names its encoding)','python resolver (behaviour + inline parity + idiom ban)','harness arms (fail branches armed or pinned)','codebase-map coverage + freshness','lexicon naming predicates','memory hygiene','dead-path carriers (deleted files still named)','remote literals (kit code names no remote)','marker contracts','drift-audit records','install-prefix (shipped surface)','routed commits name a specced unit','spec tokens (a spec\'s own names resolve)']
for l in legs:
  if l['name'] in want: print(l['name'],'::',' '.join(l['argv'])[:200])
"
````

36. Bash

````text
for f in memory/project/*; do n=$(grep -cvE '^\s*(#|$)' "$f"); echo "$n rows  $(wc -c <"$f")B  $f :: $(grep -m1 -E '^#' "$f" | cut -c1-110)"; done
````

37. Bash

````text
for f in encoding-posture-sites substitution-fed-loops spawn-idiom-sites unarmed-branches; do p=memory/project/$f.txt; first=$(git log --diff-filter=A --format=%h -- $p | tail -1); echo "== $f seed $(git log -1 --format=%ad --date=short $first) rows $(git show $first:$p | grep -cvE '^\s*(#|$)') -> now $(grep -cvE '^\s*(#|$)' $p), commits $(git log --format=%h -- $p | wc -l)"; grep -vE '^\s*(#|$)' $p | head -2; done; sed -n 1,25p memory/project/encoding-posture-sites.txt
````

38. Bash

````text
grep -rnliE 'touched|diff --name-only|merge-base|--cached' tools/gate-lint/ tools/check-line-length.sh tools/memory-tree/check-arms.py tools/codebase-map/test_codebase_map.py tools/lexicon/lexicon.py 2>/dev/null; echo ---; grep -nE 'touched|merge-base|diff' tools/check-line-length.sh | head; echo ---; grep -nE 'def .*touch|touched' tools/gate-lint/*.py | head
````

39. Bash

````text
grep -nE 'touched|merge-base|diff' tools/codebase-map/test_codebase_map.py | head -8; echo ---; grep -nE 'touched|merge-base|added|base' tools/lexicon/lexicon.py | head -15; echo ---; sed -n 1,40p tools/check-line-length.sh | grep -E '^#' | head -25
````

40. Bash

````text
ls tools/run-gates/; grep -nE 'attribute' tools/run-gates/run-gates.sh | head -20; grep -n 'offenders' tools/gate-legs.json | head; python -c "
import json;d=json.load(open('tools/gate-legs.json'));legs=d['legs'] if isinstance(d,dict) else d
print('legs with an offenders/signature key:',[l['name'] for l in legs if any(k not in ('name','argv','reads','chunk','subject','ceiling') for k in l)][:20])
print(sorted(set(k for l in legs for k in l)))"
````

41. Bash

````text
sed -n 4300,4345p tools/run-gates/run-gates.sh; python -c "
import json;d=json.load(open('tools/gate-legs.json'));legs=d['legs'] if isinstance(d,dict) else d
s=[l for l in legs if 'signature' in l]; g=[l for l in legs if 'guard' in l]
print('legs with signature:',len(s),'of',len(legs)); print([ (l['name'],l['signature']) for l in s][:6]); print('guarded legs',len(g), g[0].get('guard') if g else '')"
````

42. Bash

````text
grep -nE '^# .*(LEG GUARD|guard)' tools/run-gates/run-gates.sh | head -12
````

43. Bash

````text
git grep -hoE '^[A-Z0-9_]+_CUTOFF="[^"]*"' -- '.*.conf' | head -40 | awk -F= '{print $1"="$2}' | column -c 200 | head -20; git grep -cE '^[A-Z0-9_]+_CUTOFF="[^"]+"' -- '*.conf' '.*.conf'
````

44. Bash

````text
for f in tools/check-dead-paths.sh tools/check-remote-literals.sh tools/check-install-prefix.sh tools/check-line-length.sh tools/gate-lint/fork-count.sh tools/memory-tree/check-arms.py tools/check-spec-tokens.py; do echo "$f: $(grep -ciE 'waiver|baseline|pin|predate|exempt|shrink' $f) legacy-words; $(grep -m1 -iE 'waiver|baseline|PIN=|predate|shrink-only' $f | cut -c1-120)"; done
````

45. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; git log --since=2026-08-09 --format='U %h %s' --name-only > $S/units.txt; python - "$S" <<'E'
import sys,re,collections,subprocess
S=sys.argv[1]
seed=subprocess.run(['git','show','f9cf666c8:memory/map/baseline.toml'],capture_output=True,text=True,encoding='utf-8').stdout
keys=re.findall(r'^\s+"([^"]+)"',seed,re.M)
# map key -> path prefix (kits, gotchas, hooks); others unmapped
def path(k):
    import os
    if k.endswith('.md'): return 'memory/gotchas/'+k
    if os.path.isdir('tools/'+k): return 'tools/'+k+'/'
    if k in('pre-commit','pre-push'): return '.githooks/'+k
    return None
mp={k:path(k) for k in keys}; mapped={k:p for k,p in mp.items() if p}
print('seed keys',len(keys),'mapped to a path',len(mapped))
units=collections.defaultdict(set); cur=None
for l in open(S+'/units.txt',encoding='utf-8',errors='replace'):
    l=l.rstrip('\n')
    if l.startswith('U '):
        m=re.search(r'((?:TOOL|PLAY|KICK|DEPL)-[A-Za-z]+-\d+)',l); cur=m.group(1) if m else None; continue
    if cur and l:
        for k,p in mapped.items():
            if l==p or l.startswith(p): units[cur].add(k)
allunits=set()
for l in open(S+'/units.txt',encoding='utf-8',errors='replace'):
    m=re.search(r'^U .*?((?:TOOL|PLAY|KICK|DEPL)-[A-Za-z]+-\d+)',l)
    if m: allunits.add(m.group(1))
hit=[len(v) for v in units.values()]
hit.sort()
print('units since seed',len(allunits),'units touching >=1 baselined key',len(hit))
print('keys per touching unit: median',hit[len(hit)//2],'p90',hit[int(len(hit)*.9)],'max',hit[-1])
first=collections.Counter()
seen=set()
# how many keys would be drained if each first-touch drained it
touched=set().union(*units.values())
print('mapped keys touched by some unit:',len(touched),'of',len(mapped))
E
````

46. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; git log --reverse --since=2026-08-09 --format='U %h %ad %s' --date=short --name-only > $S/unitsr.txt; python - "$S" <<'E'
import sys,re,collections,subprocess,os
S=sys.argv[1]
seed=subprocess.run(['git','show','f9cf666c8:memory/map/baseline.toml'],capture_output=True,text=True,encoding='utf-8').stdout
keys=re.findall(r'^\s+"([^"]+)"',seed,re.M)
def path(k):
    if k.endswith('.md'): return 'memory/gotchas/'+k
    if os.path.isdir('tools/'+k): return 'tools/'+k+'/'
    if k in('pre-commit','pre-push'): return '.githooks/'+k
mapped={k:path(k) for k in keys if path(k)}
drained={}; cur=None; d=None
for l in open(S+'/unitsr.txt',encoding='utf-8',errors='replace'):
    l=l.rstrip('\n')
    if l.startswith('U '):
        parts=l.split(' ',3); d=parts[2]; m=re.search(r'((?:TOOL|PLAY|KICK|DEPL)-[A-Za-z]+-\d+)',l); cur=m.group(1) if m else None; continue
    if cur and l:
        for k,p in mapped.items():
            if k not in drained and (l==p or l.startswith(p)): drained[k]=(d,cur)
per=collections.Counter(u for _,u in drained.values())
print('first-touch drains',len(drained),'units carrying a drain',len(per),'max per unit',max(per.values()))
ds=sorted(v[0] for v in drained.values()); print('first drain',ds[0],'last',ds[-1],'median date',ds[len(ds)//2])
E
````

47. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; git log --since="30 days ago" --format='U %h' --name-only > $S/c30.txt; python - "$S" <<'E'
import sys,collections
S=sys.argv[1]
lists={'spawn-idiom-sites':2,'encoding-posture-sites':2,'substitution-fed-loops':2}
sites=collections.Counter()
for n,ci in lists.items():
    for l in open(f'memory/project/{n}.txt',encoding='utf-8'):
        if not l.strip() or l.lstrip().startswith('#'): continue
        p=l.split('\t')
        try: sites[p[0]]+=int(p[ci])
        except: sites[p[0]]+=1
commits=[];cur=None
for l in open(S+'/c30.txt',encoding='utf-8',errors='replace'):
    l=l.strip()
    if l.startswith('U '): cur=set(); commits.append(cur); continue
    if l: cur.add(l)
owed=[sum(sites[f] for f in c if f in sites) for c in commits]
hit=sorted(o for o in owed if o)
print('files carrying baselined code offenses',len(sites),'sites',sum(sites.values()))
print('commits in 30d',len(commits),'touching such a file',len(hit))
print('file-scoped drain owed per touching commit: median',hit[len(hit)//2],'p90',hit[int(len(hit)*.9)],'max',hit[-1])
E
````

48. Bash

````text
S=/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad; cat $(cat $S/code.txt) | wc -c; cat >> $S/reads.py <<'E'
import os
ub=sum(os.path.getsize(f) for f in unread); ab=sum(os.path.getsize(f) for f in code)
print(f'bytes of code never read in 30d: {ub} of {ab} = {ub/ab:.1%}')
E
python $S/reads.py $S | tail -1; grep -c . memory/map/features/*.md | awk -F: '{s+=$2} END{print "dossier lines",s}'; cat memory/map/features/*.md | wc -c
````

49. Bash

````text
git show b0f5247a9 -- memory/map/baseline.toml | grep -E '^[-+]\s+"|^[-+]#' ; git show 1640f6808 -- memory/map/baseline.toml | grep -E '^[-+]\s+"'; git show 54c8d081f --stat --format=%s | head -5
````

50. Bash

````text
grep -n 'no waiver registry' tools/check-install-prefix.sh; grep -n 'WAIVERS are a tracked' tools/check-dead-paths.sh; grep -n "green on a fresh seed" WIRE-INTO-PROJECT.md; grep -n 'One mechanical pass' WIRE-INTO-PROJECT.md; grep -n 'seed-affordance-baseline' WIRE-INTO-PROJECT.md | head -2; grep -n 'def ratchet_findings' tools/drift-audit/drift_report.py; grep -n 'def build_shrink_only\|shrink_only_lists_not_shrinking' tools/drift-audit/drift_report.py | head -2; grep -n 'unattended retrofit' memory/builds/aDeployScout/spec/governance-deployer-research.md; grep -nE 'adopter|EXISTING' memory/builds/aDeployScout/spec/governance-deployer-research.md | sed -n 1,3p
````
