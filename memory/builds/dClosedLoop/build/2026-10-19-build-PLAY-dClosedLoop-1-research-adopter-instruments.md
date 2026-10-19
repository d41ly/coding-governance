# Research instruments: adopter instructions, four passes

**Serves:** research PLAY-dClosedLoop-1

Each pass's shell commands, written files, web queries and pages read, taken in order from its transcript, so nothing is retyped. The passes shared the session scratch directory, so a file there may hold another pass's content; these are what each pass sent. Reads of the tree (Read, Grep, Glob) are left out, as the retrofit pass's instruments left them out. The returns are `build/2026-10-19-build-PLAY-dClosedLoop-1-research-adopter-today.md`, `-research-adopter-design.md`, `-research-adopter-prior-art.md` and `-research-adopter-history.md`.

## [adopter-today] Dispatch 118: today's product, measured on a scratch install

1. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && ls tools/ && cat tools/govkit/registry.toml && ls tools/*/kit.toml && wc -l tools/govkit/govkit.py
````

2. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -v '^#' tools/govkit/registry.toml | grep -v '^$' | head -150; ls tools/*/kit.toml skills/*/kit.toml 2>/dev/null; wc -l tools/govkit/*.py
````

3. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && cat tools/govkit/entries/playbook.kit.toml; echo ======; cat tools/playbook/kit.toml
````

4. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -n "ROLES\b\|^ROLE\|\"seed\"\|\"patched\"\|\"forked\"\|\"withdrawn\"\|project-owned\|\"rendered\"" tools/govkit/govkit.py | head -80
````

5. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && source tools/lib/resolve-python.sh 2>/dev/null; echo "PY=$PY ${PYTHON:-}"; cat tools/lib/resolve-python.sh | head -40
````

6. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && . tools/lib/resolve-python.sh; PY=$(resolve_python); echo $PY; $PY --version; $PY tools/govkit/govkit.py --help 2>&1 | head -60
````

7. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; mkdir -p "$S/t1" && cd "$S/t1" && git init -q -b main && git commit -q --allow-empty -m init && cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && python3 tools/govkit/govkit.py plan --target "$S/t1" --all 2>&1 | head -80
````

8. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && python3 tools/govkit/govkit.py intake --target "$S/t1" --all 2>&1 | tail -60; cat "$S/t1/.governance/deploy.toml" 2>/dev/null | head -120
````

9. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && ls -la .governance/ && cat .governance/deploy.toml
````

10. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && python3 tools/govkit/govkit.py intake --target "$S/t1" --all --answer gate_file=.github/workflows/ci.yml --answer manifest_path=memory/guides/SESSION-KICKOFF.md --answer playbook_path=coding-governance-agents.template.md --answer user_skills="$S/userskills" 2>&1 | tail -30; cat "$S/t1/.governance/deploy.toml"
````

11. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && python3 tools/govkit/govkit.py plan --target "$S/t1" --all > "$S/plan-all.txt" 2>&1; echo exit=$?; wc -l "$S/plan-all.txt"; head -50 "$S/plan-all.txt"
````

12. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; sed -n '50,411p' "$S/plan-all.txt" | grep -v "\[engine       \] tools/.*\.\(py\|sh\|js\|json\)  " 
````

13. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && for f in tools/*/kit.toml tools/govkit/entries/*.kit.toml; do python3 - "$f" <<'EOF'
import sys,tomllib
p=sys.argv[1]; d=tomllib.load(open(p,'rb'))
regs=d.get('regenerate',[])
rows=[(r.get('role','engine'),r.get('to'),r.get('include')) for r in d.get('files',[]) if r.get('role') in ('rendered','generated','merged','forked')]
ad=d.get('adopt',{}).get('argv')
print(f"{d.get('id')}: adopt={ad}")
for r in regs: print("   regenerate writes", r.get('writes'), r.get('argv'))
for r in rows: print("   row", r)
EOF
done
````

14. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -rln "\.claude/rules" tools/ skills/ --include=*.sh --include=*.py --include=*.toml | head; echo ===; grep -n "claude/agents\|roles.json\|house" tools/roles/kit.toml | head -30; echo; cat tools/agent-instructions/kit.toml | grep -v '^#' | grep -v '^$' | head -60
````

15. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -rn "\.claude/rules" tools/ skills/ WIRE-INTO-PROJECT.md coding-governance-agents.template.md | grep -v "^tools/.*test" | head -20; ls .claude/rules/
````

16. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && wc -l tools/playbook/*.sh tools/playbook/*.py && grep -n "gov:playbook\|region\|outside\|wrapper\|--force\|refus" tools/playbook/adopt-playbook.sh | head -80
````

17. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -n "def \|BEGIN\|END_MARK\|<!-- gov\|region" tools/playbook/render_playbook.py | head -120
````

18. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -n "gov:playbook" AGENTS.md; wc -l AGENTS.md; head -5 AGENTS.md; cat CLAUDE.md; ls -la | grep -i "gemini\|cursor\|copilot\|windsurf\|\.github"; ls .claude/; ls .claude/agents .claude/skills
````

19. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && wc -l tools/agent-instructions/adopt-agent-instructions.sh && sed -n 1,200p tools/agent-instructions/adopt-agent-instructions.sh
````

20. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && ls tools/roles/ tools/roles/house; wc -l tools/roles/*.sh tools/roles/*.py; sed -n 1,80p tools/roles/README.md
````

21. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && ls tools/memory-tree/; grep -n "render\|region\|house\|overlay\|local" tools/memory-tree/adopt-memory-tree.sh | head -60
````

22. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && sed -n 380,520p tools/memory-tree/adopt-memory-tree.sh
````

23. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -n "GOVKIT_RERENDER\|def _cmd_update\|def cmd_update\|regenerate" tools/govkit/govkit.py | sed -n 1,200p | awk -F: '$1>9000' | head -80
````

24. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && git log --format='%h %ad %s' --date=short -n 8 -- tools/roles/agents tools/memory-tree/HYGIENE.template.md coding-governance-agents.template.md tools/unattended/PROTOCOL.template.md tools/lexicon/SKILL.template.md tools/review-harness/REVIEW-PROTOCOL.template.md | cut -c1-140; git log --oneline | wc -l
````

25. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && B=$(git rev-parse b61ec1c49~1); echo $B; git diff --stat $B HEAD -- coding-governance-agents.template.md 'tools/*/SKILL.template.md' 'tools/*/*.template.md' tools/roles/agents tools/roles/house tools/hooks/*.js skills/session-kickoff/MANIFEST-TEMPLATE.md | tail -30; git show -s --format='%ad %s' --date=short $B | cut -c1-120
````

26. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S" && git clone -q --no-hardlinks "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" gov 2>&1 | tail -3; cd gov && git checkout -q 9df98d1eb && git log -1 --oneline | cut -c1-100; git -C "$S/gov" rev-parse HEAD; git -C "$S/gov" branch -a | head
````

27. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S" && rm -rf t1 && git init -q --bare origin-b.git && git init -q -b main tB && cd tB && git config user.email x@x && git config user.name x && mkdir -p .github/workflows && printf 'name: ci\non: push\njobs:\n  a:\n    runs-on: ubuntu-latest\n    steps:\n      - run: true\n' > .github/workflows/ci.yml && printf '# demo\n' > README.md && git add -A && git commit -q -m init && git remote add origin "$S/origin-b.git" && git push -q origin main 2>&1; git remote set-head origin main; cd "$S/gov" && python3 tools/govkit/govkit.py intake --target "$S/tB" --all --answer gate_file=.github/workflows/ci.yml --answer manifest_path=memory/guides/SESSION-KICKOFF.md --answer playbook_path=coding-governance-agents.template.md --answer user_skills="$S/userskills" 2>&1 | tail -3
````

28. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cat > "$S/add_answers.py" <<'EOF'
import sys,pathlib
p=pathlib.Path(sys.argv[1])/'.governance'/'deploy.toml'
t=p.read_text()
keys=["project_name","stream_ownership","doc_routing_table","product_preamble","repo_layout_map","command_catalog","product_context_home","gate_commands","commit_trailer","worktree_script","kind_factory_map","shared_primitives_location","toolchain_notes"]
add="".join(f'{k} = "demo {k}"\n' for k in keys)
t=t.replace("[answers]\n","[answers]\n"+add,1)
t+='\n[charter]\nadopter_rules = """\n- ADOPTER-RULE-ONE: every migration ships with a rollback.\n"""\n'
p.write_text(t)
EOF
python3 "$S/add_answers.py" "$S/tB" && cat "$S/tB/.governance/deploy.toml" | sed -n 1,40p
````

29. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/gov" && time python3 tools/govkit/govkit.py apply --target "$S/tB" --all > "$S/apply-B.txt" 2>&1; echo exit=$?; tail -40 "$S/apply-B.txt"
````

30. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; grep -n -i "configure\|adopter\|AGENT-INSTR\|roles\|process-monitor\|unattended" "$S/apply-B.txt" | grep -v "^.*pin '" | head -60; ls "$S/tB" "$S/tB/.claude" "$S/tB/.claude/agents" 2>&1; git -C "$S/tB" status --short | head -30
````

31. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/tB" && ls -a; bash tools/memory-tree/adopt-memory-tree.sh --scaffold 2>&1 | tail -8; echo ---; bash tools/roles/adopt-roles.sh --scaffold 2>&1 | tail -8
````

32. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/tB" && find memory -type f; grep -v '^#' .memory-tree.conf | grep -v '^$' | head -30
````

33. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/tB" && cp memory/guides/SESSION-KICKOFF.md "$S/kick.bak" && rm -rf memory && bash tools/memory-tree/adopt-memory-tree.sh --scaffold 2>&1 | tail -5; cp "$S/kick.bak" memory/guides/SESSION-KICKOFF.md; find memory -maxdepth 2 | head -20
````

34. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/tB" && bash tools/playbook/adopt-playbook.sh --target . 2>&1 | tail -3; grep -n "ADOPTER-RULE\|^## \|^### " AGENTS.md | head -30; bash tools/roles/adopt-roles.sh --scaffold 2>&1 | tail -5
````

35. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/gov" && grep -n "names no section" tools/roles/*.py | head; grep -n "def .*section\|§3\|Generated" tools/roles/render_agents.py | head -20
````

36. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/gov" && sed -n 95,180p tools/roles/render_agents.py; grep -n "charter" tools/roles/agents/gov-builder.agent.md | head
````

37. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && B=b61ec1c49; git diff --stat $B HEAD -- coding-governance-agents.template.md 'tools/*/SKILL.template.md' 'tools/*/*.template.md' tools/roles/agents tools/roles/house tools/hooks/*.js skills/session-kickoff/MANIFEST-TEMPLATE.md tools/playbook tools/roles/*.py | tail -30
````

38. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S" && rm -rf tB origin-b.git userskills && git -C gov checkout -q b61ec1c49 && git init -q --bare origin-b.git && git init -q -b main tB && cd tB && git config user.email x@x && git config user.name x && git config core.autocrlf false && mkdir -p .github/workflows && printf 'name: ci\non: push\njobs:\n  a:\n    runs-on: ubuntu-latest\n    steps:\n      - run: true\n' > .github/workflows/ci.yml && printf '# demo\n' > README.md && git add -A && git commit -q -m init && git remote add origin "$S/origin-b.git" && git push -q origin main && git remote set-head origin main; cd "$S/gov" && python3 tools/govkit/govkit.py intake --target "$S/tB" --all --answer gate_file=.github/workflows/ci.yml --answer manifest_path=memory/guides/SESSION-KICKOFF.md --answer playbook_path=coding-governance-agents.template.md --answer user_skills="$S/userskills" 2>&1 | tail -1 && python3 "$S/add_answers.py" "$S/tB" && python3 tools/govkit/govkit.py apply --target "$S/tB" --all > "$S/apply-B.txt" 2>&1; echo exit=$?; grep "CONFIGURE" "$S/apply-B.txt"
````

39. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/tB" && cp memory/guides/SESSION-KICKOFF.md "$S/kick.bak" && rm -rf memory && bash tools/memory-tree/adopt-memory-tree.sh --scaffold >/dev/null 2>&1; echo mt=$?; cp "$S/kick.bak" memory/guides/SESSION-KICKOFF.md; bash tools/agent-instructions/adopt-agent-instructions.sh 2>&1 | tail -5; echo ai=$?; bash tools/unattended/adopt-unattended.sh 2>&1 | tail -5; ls tools/review-harness/ | head -30
````

40. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/tB" && cp tools/unattended/.unattended.conf.example .unattended.conf && bash tools/unattended/adopt-unattended.sh 2>&1 | tail -4; git add -A >/dev/null 2>&1; bash tools/review-harness/check-protocol-parity.test.sh --render --tracked-only 2>&1 | tail -4; ls memory/guides .claude/skills .claude/agents
````

41. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/tB" && bash tools/review-harness/check-protocol-parity.test.sh --render 2>&1 | tail -3; git add -A 2>/dev/null; git commit -q -m "install gov at b61ec1c49" --no-verify && git log --oneline | head -3; ls memory/guides; cd "$S/gov" && python3 tools/govkit/govkit.py check --target "$S/tB" > "$S/check-B0.txt" 2>&1; echo check=$?; tail -15 "$S/check-B0.txt"
````

42. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/tB" && ls memory; find . -name "*.js" -path "*hook*" -o -name "agent-cap.js" | grep -v .git; ls tools/hooks 2>/dev/null | head; cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -rli "work.order" tools/*/kit.toml tools/*/*.template.md skills/session-kickoff/*.md 2>/dev/null | head
````

43. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -rli "work.order\|workorder" --include=*.md --include=*.toml --include=*.py --include=*.js tools skills | head; ls skills/session-kickoff/
````

44. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/tB" && cat > "$S/edit.py" <<'EOF'
import pathlib,sys
root=pathlib.Path(sys.argv[1])
def app(p,tag):
    f=root/p; t=f.read_text(encoding='utf-8'); f.write_text(t.rstrip('\n')+f'\n\n- {tag}: an adopter-added line.\n',encoding='utf-8',newline='\n')
# inside region
a=root/'AGENTS.md'; t=a.read_text(encoding='utf-8')
t=t.replace('## 2. This repository\n','## 2. This repository\n\n- CUSTOM-AGENTS-IN: edited inside the region.\n',1)
t=t.rstrip('\n')+'\n\n## Local notes\n\n- CUSTOM-AGENTS-OUT: authored below the region.\n'
a.write_text(t,encoding='utf-8',newline='\n')
# template section 1
tp=root/'coding-governance-agents.template.md'; t=tp.read_text(encoding='utf-8')
i=t.index('## 1.'); j=t.index('\n- ',i)
t=t[:j]+'\n- CUSTOM-TEMPLATE: an adopter practice added in the seeded template.'+t[j:]
tp.write_text(t,encoding='utf-8',newline='\n')
for p,tag in [('CLAUDE.md','CUSTOM-CLAUDE'),('.github/copilot-instructions.md','CUSTOM-COPILOT'),
  ('.claude/skills/lexicon/SKILL.md','CUSTOM-SKILL-LEX'),('.claude/skills/build/SKILL.md','CUSTOM-SKILL-BUILD'),
  ('.claude/skills/unattended/SKILL.md','CUSTOM-SKILL-UNATT'),('.claude/agents/gov-builder.md','CUSTOM-AGENT'),
  ('tools/roles/house/gov-builder.md','CUSTOM-HOUSE'),('tools/roles/agents/gov-researcher.agent.md','CUSTOM-ROLEBASE'),
  ('memory/HYGIENE.md','CUSTOM-HYGIENE'),('memory/TEMPLATE-SPEC.md','CUSTOM-SPECTPL'),('memory/guides/BUILD-METHOD.md','CUSTOM-METHOD'),
  ('memory/guides/UNATTENDED-PROTOCOL.md','CUSTOM-UPROTO'),('memory/guides/REVIEW-PROTOCOL.md','CUSTOM-RPROTO'),
  ('memory/guides/SESSION-KICKOFF.md','CUSTOM-MANIFEST'),('memory/guides/PLAYBOOK-TEMPLATE.md','CUSTOM-PLAYTPL'),
  ('tools/memory-tree/HYGIENE.template.md','CUSTOM-HYG-TPL'),('tools/unattended/SKILL.template.md','CUSTOM-UNATT-TPL')]:
    app(p,tag)
h=root/'tools/hooks/agent-cap.js'; t=h.read_text(encoding='utf-8'); h.write_text(t+'\n// CUSTOM-HOOK: adopter edit to refusal text file\n',encoding='utf-8',newline='\n')
r=root/'.claude/rules'; r.mkdir(parents=True,exist_ok=True); (r/'custom.md').write_text('- CUSTOM-RULE: an adopter path rule.\n',encoding='utf-8',newline='\n')
EOF
python3 "$S/edit.py" "$S/tB" && git add -A && git commit -q --no-verify -m "adopter customizations" && git show --stat HEAD | tail -25
````

45. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cp -r "$S/tB" "$S/tB-pre"; cd "$S/gov" && git checkout -q a0b1a06c4 && git log -1 --oneline | cut -c1-60 && python3 tools/govkit/govkit.py update --target "$S/tB" > "$S/update-ro.txt" 2>&1; echo exit=$?; wc -l "$S/update-ro.txt"; grep -n -i "custom\|rendered\|forked\|patched\|diverged\|AGENTS\|CLAUDE\|copilot\|SKILL\|agents/\|house\|HYGIENE\|PROTOCOL\|METHOD\|SESSION-KICKOFF\|template.md\|agent-cap.js\|rules" "$S/update-ro.txt" | head -120
````

46. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; sed -n 26,41p "$S/update-ro.txt"; sed -n 292,338p "$S/update-ro.txt"
````

47. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/gov" && python3 tools/govkit/govkit.py update --target "$S/tB" --write > "$S/update-w.txt" 2>&1; echo exit=$?; wc -l "$S/update-w.txt"; grep -n -i "diverged\|three-way\|conflict\|re-render\|regenerate\|rolled back\|REFUSED\|rollback\|reverted\|still differs\|problem" "$S/update-w.txt" | head -60
````

48. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; sed -n 306,420p "$S/update-w.txt" | grep -v "^  \(current\|stale\)" | cut -c1-400
````

49. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/tB" && for t in CUSTOM-AGENTS-IN CUSTOM-AGENTS-OUT CUSTOM-TEMPLATE CUSTOM-CLAUDE CUSTOM-COPILOT CUSTOM-SKILL-LEX CUSTOM-SKILL-BUILD CUSTOM-SKILL-UNATT CUSTOM-AGENT CUSTOM-HOUSE CUSTOM-ROLEBASE CUSTOM-HYGIENE CUSTOM-SPECTPL CUSTOM-METHOD CUSTOM-UPROTO CUSTOM-RPROTO CUSTOM-MANIFEST CUSTOM-PLAYTPL CUSTOM-HYG-TPL CUSTOM-UNATT-TPL CUSTOM-HOOK CUSTOM-RULE ADOPTER-RULE-ONE; do hits=$(git grep -l "$t" -- . 2>/dev/null; grep -rl "$t" --exclude-dir=.git . 2>/dev/null | sed 's|^\./||'); printf '%-20s %s\n' "$t" "$(echo "$hits" | sort -u | tr '\n' ' ')"; done
````

50. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/tB" && grep -rl "CUSTOM-AGENT:" --exclude-dir=.git .; echo ---; git status --short | grep -v "^ M tools/\|^M  tools/\|^A  tools" | head -40; echo ---; git diff HEAD --stat -- AGENTS.md .claude memory .github CLAUDE.md coding-governance-agents.template.md | tail -25; grep -n "AGENTS.md\|CLAUDE.md\|\.claude/agents" "$S/update-w.txt" | head
````

51. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/tB" && git diff HEAD -- AGENTS.md memory/guides/REVIEW-PROTOCOL.md; grep -n "governance-template" AGENTS.md coding-governance-agents.template.md; bash tools/agent-instructions/adopt-agent-instructions.sh --check; echo ai-check=$?; bash tools/playbook/adopt-playbook.sh --target . --check 2>&1 | tail -3; echo pb-check=$?
````

52. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/tB" && git diff HEAD -- AGENTS.md memory/guides/REVIEW-PROTOCOL.md; grep -n "governance-template" AGENTS.md coding-governance-agents.template.md; cmp -s AGENTS.md .github/copilot-instructions.md && echo copilot=identical || echo copilot=differs-from-AGENTS.md
````

53. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S" && rm -rf tA origin-a.git && git init -q --bare origin-a.git && git init -q -b main tA && cd tA && git config user.email x@x && git config user.name x && git config core.autocrlf false && mkdir -p .github/workflows .claude/rules .claude/agents && printf 'name: ci\non: push\njobs:\n  a:\n    runs-on: ubuntu-latest\n    steps:\n      - run: true\n' > .github/workflows/ci.yml && printf '# Project agents guide\n\n- PRE-AGENTS: always run make lint before commit.\n' > AGENTS.md && printf '# Claude notes\n\n- PRE-CLAUDE: use pnpm, never npm.\n' > CLAUDE.md && printf -- '- PRE-RULE: api/ handlers validate input.\n' > .claude/rules/api.md && printf -- '- PRE-COPILOT: prefer functional components.\n' > .github/copilot-instructions.md && printf -- '- PRE-GEMINI: be terse.\n' > GEMINI.md && printf -- '---\nname: my-agent\ndescription: x\n---\nPRE-OWNAGENT body\n' > .claude/agents/my-agent.md && printf '{\n  "permissions": {"allow": ["Bash(make:*)"]}\n}\n' > .claude/settings.json && git add -A && git commit -q -m init && git remote add origin "$S/origin-a.git" && git push -q origin main && git remote set-head origin main; cd "$S/gov" && git log -1 --format=%h && python3 tools/govkit/govkit.py intake --target "$S/tA" --all --answer gate_file=.github/workflows/ci.yml --answer manifest_path=memory/guides/SESSION-KICKOFF.md --answer playbook_path=coding-governance-agents.template.md --answer user_skills="$S/userskillsA" 2>&1 | tail -1 && python3 "$S/add_answers.py" "$S/tA" && python3 tools/govkit/govkit.py plan --target "$S/tA" --all 2>&1 | grep -i "AGENTS\|CLAUDE\|settings\|rules\|copilot\|GEMINI\|agents/" ; python3 tools/govkit/govkit.py apply --target "$S/tA" --all > "$S/apply-A.txt" 2>&1; echo exit=$?; grep -n "CONFIGURE\|AGENTS\|CLAUDE\|settings\|copilot\|GEMINI\|agents" "$S/apply-A.txt" | head -40
````

54. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/tA" && head -5 AGENTS.md; grep -n "gov:playbook\|PRE-AGENTS\|^## " AGENTS.md | head; echo ---; cat CLAUDE.md GEMINI.md .github/copilot-instructions.md .claude/rules/api.md; ls .claude/agents .gemini 2>&1; cat .claude/settings.json | head -30; bash tools/agent-instructions/adopt-agent-instructions.sh 2>&1 | tail
````

55. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; rm -rf "$S/tA2" && cp -r "$S/tA" "$S/tA2" && cd "$S/tA2" && printf '@AGENTS.md\n' >> CLAUDE.md && bash tools/agent-instructions/adopt-agent-instructions.sh --aliases claude 2>&1 | tail -2; cat CLAUDE.md; echo ---; bash tools/agent-instructions/adopt-agent-instructions.sh --force 2>&1 | tail -4; cat CLAUDE.md GEMINI.md 2>&1 | head; head -3 .github/copilot-instructions.md
````

56. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && wc -c tools/roles/house/*.md | tail -12; head -5 .claude/rules/product.md; ls -a | grep "^\.\w*conf\|^\.lexicon"; grep -v "^#" .lexicon.conf | grep -v "^$" | head -15; cat tools/roles/house/policy.toml | grep -v "^#" | grep -v "^$" | head -20
````

57. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -n "{{[A-Z_]*}}" tools/*/SKILL.template.md tools/unattended/*.template.md tools/review-harness/REVIEW-PROTOCOL.template.md tools/memory-tree/*.template.md -o | awk -F: '{print $1": "$3}' | sort -u | awk -F': ' '{a[$1]=a[$1]" "$2} END{for(k in a) print k":"a[k]}'
````

58. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && git diff b61ec1c49 HEAD -- tools/roles/agents/gov-builder.agent.md | head -30
````

59. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; rm -rf "$S/tC" && cp -r "$S/tB-pre" "$S/tC" && cd "$S/tC" && sed -i 's/^description: Builds exactly one unit from its spec, verifies it with the spec.s direct check, and commits it\./description: CUSTOM-CONFLICT builds per our house style./' tools/roles/agents/gov-builder.agent.md && head -3 tools/roles/agents/gov-builder.agent.md && git commit -qam conflict --no-verify && cd "$S/gov" && python3 tools/govkit/govkit.py update --target "$S/tC" --write > "$S/update-C.txt" 2>&1; echo exit=$?; grep -n -i "gov-builder.agent\|conflict\|outbox" "$S/update-C.txt" | cut -c1-300 | head; ls "$S/tC/.governance/outbox/"; head -5 "$S/tC/tools/roles/agents/gov-builder.agent.md"
````

60. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -n "\[\[own\]\]" tools/govkit/govkit.py | head -20; grep -n "\[\[own\]\]\|adopter-owned" WIRE-INTO-PROJECT.md tools/govkit/README.md 2>/dev/null | head
````

61. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && sed -n 1195,1240p WIRE-INTO-PROJECT.md; sed -n 1493,1555p tools/govkit/govkit.py
````

62. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; for case in "memory/HYGIENE.md|memory-tree:HYGIENE.template.md" ".claude/skills/build/SKILL.md|roles:SKILL.template.md" "tools/roles/agents/gov-builder.agent.md|roles:agents/gov-builder.agent.md"; do rm -rf "$S/tD"; cp -r "$S/tB-pre" "$S/tD"; p=${case%%|*}; i=${case#*|}; printf '\n[[own]]\npath = "%s"\nimplements = "%s"\nwhy = "our own instruction text"\n' "$p" "$i" >> "$S/tD/.governance/deploy.toml"; echo "== $p"; (cd "$S/gov" && python3 tools/govkit/govkit.py adopt --target "$S/tD" --re-adopt 2>&1 | grep -i "own\]\]\|adopter-owned\|refus" | head -3 | cut -c1-300); done
````

63. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory" && ls builds | grep -i "RepatriatedFork\|HalvedInstall\|DistilledCharter\|RetiredFork\|OrientedCast\|CarriedReceipt"; sed -n 1,60p builds/aRepatriatedFork/README.md 2>/dev/null | cut -c1-260
````

64. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds" && sed -n 198,206p dPolishedVitrine/reviews/2026-09-13-review-TOOL-dPolishedVitrine-1-diff-review-round2.md | cut -c1-400; echo ----; sed -n 314,322p dPolishedVitrine/reviews/2026-09-13-review-TOOL-dPolishedVitrine-1-diff-review-round2.md | cut -c1-400; echo ----; sed -n 333,340p aRatchetForge/spec/manifest-ratchet-spec.md | cut -c1-300; echo ----; sed -n 118,126p aRepatriatedFork/spec/2026-09-23-spec-TOOL-aRepatriatedFork-10.md | cut -c1-300; echo ----; sed -n 216,226p aRepatriatedFork/spec/2026-09-23-spec-TOOL-aRepatriatedFork-5.md | cut -c1-300
````

65. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -n "carve-out" WIRE-INTO-PROJECT.md | head -20; sed -n 1160,1198p WIRE-INTO-PROJECT.md
````

66. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && sed -n 1139,1158p WIRE-INTO-PROJECT.md; grep -rn "carve-out" tools/govkit/govkit.py | head -5
````

67. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory" && grep -rln "house overlay\|House rules\|adopter_rules" --include=*.md . | grep -v dClosedLoop | head -15; grep -rn "adopter_rules" builds/aDistilledCharter/README.md | head -5
````

68. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds" && grep -n -i "wrapper\|authored\|outside the region\|section 2" aDistilledCharter/spec/2026-10-09-spec-PLAY-aDistilledCharter-4.md | head -12 | cut -c1-260; grep -n -i "overlay" aOrientedCast/spec/2026-10-11-spec-TOOL-aOrientedCast-1.md | head -8 | cut -c1-260
````

69. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds" && sed -n 14,30p aDistilledCharter/spec/2026-10-09-spec-PLAY-aDistilledCharter-4.md
````

70. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -n -i "def arm.*\(render\|patched\|diverged\|seed\|own\)\|edited.*render\|render.*edited\|hand-edit\|operator.s edit\|adopter.s edit" tools/govkit/selftest.py | head -30
````

71. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && sed -n 14070,14082p tools/govkit/selftest.py; grep -n -i "rendered.*(patched|edit)|edit.*rendered" -E tools/govkit/selftest.py | head
````

72. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; grep -E '^\s+(write|SIDE|ORDER|COVER|BLOCK)' "$S/plan-all.txt" | grep -v '\[attributes\|\[hole\|\[project-owned\|\[generated' | grep -E '\.md |\.agent\.md|hooks/.*\.js|policy\.toml|\.claude/' | grep -v -E 'README\.md|fixture|INVENTORY' | awk '{print $2, $3, $4, $6}' | sort -k4 ; echo; cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -h -A3 "^\[\[attributes\]\]\|^\[\[regenerate\]\]" tools/*/kit.toml | grep -E "pattern|writes" | sort -u
````

73. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -v "^#" tools/govkit/entries/kickoff-manifest.kit.toml | grep -v "^$" | head -30; sed -n 118,145p tools/roles/kit.toml
````

74. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -n "^#\|Section B\|section B" skills/session-kickoff/MANIFEST-TEMPLATE.md | head -15; grep -n -A6 'id = "manifest-section-b"' tools/govkit/entries/kickoff-manifest.kit.toml | head -10
````

75. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; rm -rf "$S/tE" && cp -r "$S/tB-pre" "$S/tE" && cd "$S/tE" && printf '\n<!-- carve-out house-1 -->\n- CUSTOM-TAGGED: a tagged adopter edit per the runbook carve-out contract.\n' >> memory/guides/BUILD-METHOD.md && printf 'house-1  memory/guides/BUILD-METHOD.md  our review cadence\n' > memory/project/carve-outs.txt && git add -A && git commit -qm tagged --no-verify && cd "$S/gov" && python3 tools/govkit/govkit.py update --target "$S/tE" --write > "$S/update-E.txt" 2>&1; echo exit=$?; grep -n "BUILD-METHOD\|carve" "$S/update-E.txt" | cut -c1-200; grep -c "CUSTOM-TAGGED\|carve-out house-1" "$S/tE/memory/guides/BUILD-METHOD.md"; cd "$S/tE" && git diff HEAD -- memory/guides/BUILD-METHOD.md | tail -8
````

76. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S/tE" && cp .governance/deploy.toml "$S/dep.bak" && sed -i 's/^\[charter\]$/[charter]\nreuse = "- [reuse] OUR reuse rule replaces gov wording."/' .governance/deploy.toml && grep -n -A2 "^\[charter\]" .governance/deploy.toml && python3 tools/playbook/render_playbook.py --target . 2>&1 | tail -2; cp "$S/dep.bak" .governance/deploy.toml
````

77. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" && grep -n "def render_role" -A28 tools/roles/roles_lib.py | grep -v '^\s*$' | head -34; grep -n "omitClaudeMd" tools/roles/render_agents.py
````

78. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; grep -o 'tools/[^ ]*\.fragment\.json' "$S/plan-all.txt" | sort -u; ls "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/.governance"
````

79. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; ls -la "$S"; ls -la "$S/userskills" "$S/userskillsA" 2>&1 | head
````

80. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; for d in userskills userskillsA; do [ -e "$S/$d" ] && { echo "$d:"; cmd //c dir "$(cygpath -w "$S/$d")" 2>/dev/null | grep -i "junction\|symlink\|DIR"; }; done; echo done
````

81. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; cd "$S" && rm -rf gov tA tA2 tB tB-pre tC tD tE origin-a.git origin-b.git userskills userskillsA plan-all.txt apply-A.txt apply-B.txt update-ro.txt update-w.txt update-C.txt update-E.txt check-B0.txt add_answers.py edit.py kick.bak dep.bak; ls -d gov tA tB tE 2>&1 | head -3; git -C "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297" status --short
````

## [adopter-design] Dispatch 119: the converged design

1. Bash

````text
ls memory/builds/dClosedLoop/build/ && wc -l memory/builds/dClosedLoop/build/*.md | tail -40
````

2. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && wc -l 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md 2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md 2026-10-14-build-PLAY-dClosedLoop-1-foundations.md 2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md 2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md 2026-10-18-build-PLAY-dClosedLoop-1-walk.md 2026-10-16-build-PLAY-dClosedLoop-1-systems.md; grep -n '^#' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | head -80
````

3. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n '1387,1427p' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md; sed -n '1428,1456p' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | grep -E 'dOrderedCharter|dSafePassage|dShippedRelease|dConvergedCharter|dLinkedLibrary' | fold -w 4000
````

4. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -o -i -E '[^.|]{0,300}(project block|overlay)[^.|]{0,300}' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | sort -u
````

5. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -l -i -E 'project block|overlay' *.md | while read f; do echo "== $f $(grep -c -i -E 'project block|overlay' $f)"; done
````

6. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n '^#' 2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md
````

7. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i -E 'CV1|project block|overlay|repo-declared|house' 2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md 2026-10-18-build-PLAY-dClosedLoop-1-walk.md 2026-10-14-build-PLAY-dClosedLoop-1-foundations.md | cut -c1-400
````

8. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n '760,845p' 2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md; echo ======; sed -n '40,200p' 2026-10-14-build-PLAY-dClosedLoop-1-foundations.md
````

9. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i -E 'adopter|K2|amendment|its own|declare its own|C3|closed set' 2026-10-14-build-PLAY-dClosedLoop-1-foundations.md | cut -c1-500
````

10. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n '^#' 2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md; grep -n -i -E 'adopt\.(census|practices|decisions|reconstruct)|instruction|AGENTS|CLAUDE\.md|charter|overlay|project block|practice' 2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md | cut -c1-300 | head -100
````

11. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n '143,186p;310,377p;445,540p' 2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md
````

12. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n '^#' 2026-10-16-build-PLAY-dClosedLoop-1-systems.md; grep -n -E 'IW-[0-9]' 2026-10-16-build-PLAY-dClosedLoop-1-systems.md | cut -c1-250 | head -40
````

13. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n '130,142p;345,396p' 2026-10-16-build-PLAY-dClosedLoop-1-systems.md
````

14. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n '224,290p' 2026-10-16-build-PLAY-dClosedLoop-1-systems.md; sed -n '548,600p' 2026-10-16-build-PLAY-dClosedLoop-1-systems.md
````

15. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n '^#' 2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md; grep -n -E 'amends|supersedes|promoted-from|overlay|adopter|instruction' 2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md | cut -c1-300
````

16. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n '40,54p;63,64p;124,195p;250,300p' 2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md
````

17. Bash

````text
ls .governance/ 2>&1; git ls-files | grep -i -E 'deploy\.toml|instructions\.toml|overlay|house/' | head -30; grep -n -i -E 'SA-12' memory/builds/dClosedLoop/build/*.md | cut -c1-400 | head -20
````

18. Bash

````text
wc -l .governance/deploy.toml && grep -n -E '^\[|^[a-zA-Z_]+ *=' .governance/deploy.toml | head -60
````

19. Bash

````text
sed -n '55,70p' .governance/deploy.toml; grep -rn -E 'adopter_rules|ADOPTER_RULES' --include=*.py --include=*.sh --include=*.md tools coding-governance-agents.template.md | head -20
````

20. Bash

````text
grep -n -i 'house' tools/roles/kit.toml tools/roles/README.md 2>/dev/null | head -20; ls tools/roles
````

21. Bash

````text
sed -n '25,45p' tools/roles/kit.toml; sed -n '10,30p;260,275p' tools/roles/README.md
````

22. Bash

````text
wc -c tools/roles/house/*; head -15 tools/roles/house/gov-builder.md
````

23. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && awk 'NR>=1424 && NR<=1456' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | grep -E '^\| d(OrderedCharter|ConvergedCharter) ' | fold -w 200 -s
````

24. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -o -i -E ".{0,200}(gov-only|gov's own rules|gov's overlay|govern only gov|adopter rules|project-specific).{0,200}" *.md | grep -v instruments | cut -c1-500
````

25. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n '10,24p' 2026-10-14-build-PLAY-dClosedLoop-1-design-rounds.md; grep -n -i -E 'overlay|project block|separate block' 2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md 2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md 2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md | cut -c1-600
````

26. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i -E 'house|overlay' 2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md | cut -c1-600
````

27. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && awk 'NR>=1424 && NR<=1456' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | grep -E '^\| dSafePassage ' | fold -w 200 -s
````

28. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && awk 'NR>=1424 && NR<=1456' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | grep -E '^\| d(ShippedRelease|KeptSession|LinkedLibrary|GroundRules) ' | grep -o -i -E '[^;]{0,250}(offer|receipt|overlay|seed|repo-declared|preset|promot|reuse entr|instruction|local edit|edited)[^;]{0,250}' | cut -c1-600
````

29. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n '50,70p;188,210p' 2026-10-18-build-PLAY-dClosedLoop-1-walk.md; grep -n -i -E 'seed|local edit|adopter.{0,20}edit|edited|carried or ordered|three-way|verdict grid|fork' 2026-10-18-build-PLAY-dClosedLoop-1-research-supersession.md 2026-10-18-build-PLAY-dClosedLoop-1-research-compatibility.md | cut -c1-400 | head -30
````

30. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n '1457,1580p' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | grep -n -i -E 'instruction|overlay|adopter|unit|practice|preset' | cut -c1-400 | head -30; grep -n -E '`install\.(retired-edits|steps|on-shim-call)`' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | cut -c1-500
````

31. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i -E 'translate|import,|AGENTS\.md|CLAUDE\.md|instruction file' 2026-10-17-build-PLAY-dClosedLoop-1-research-retrofit-a.md 2026-10-17-build-PLAY-dClosedLoop-1-research-retrofit-b.md | cut -c1-500 | head -20
````

32. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n '160,175p' 2026-10-17-build-PLAY-dClosedLoop-1-research-retrofit-a.md; sed -n '185,200p' 2026-10-17-build-PLAY-dClosedLoop-1-research-retrofit-b.md
````

33. Bash

````text
grep -n -i -E 'existing (AGENTS|charter)|already has an? (AGENTS|charter)|pre-existing|adopter_rules' tools/playbook/README.md tools/playbook/adopt-playbook.sh WIRE-INTO-PROJECT.md 2>/dev/null | cut -c1-300 | head -15
````

34. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i -E 'overlay|project block' 2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md 2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md 2026-10-16-build-PLAY-dClosedLoop-1-research-instruction-writing-a.md 2026-10-16-build-PLAY-dClosedLoop-1-research-instruction-writing-b.md 2026-10-16-build-PLAY-dClosedLoop-1-research-distribution-a.md | cut -c1-500
````

35. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n '104,135p' 2026-10-16-build-PLAY-dClosedLoop-1-research-instruction-writing-a.md; echo =====; sed -n '112,150p' 2026-10-16-build-PLAY-dClosedLoop-1-research-instruction-writing-b.md
````

36. Bash

````text
f=$(git ls-files | grep 'merge-rows.py$' | head -1); echo $f; sed -n '1,40p' $f
````

37. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -o -i -E ".{0,250}(repo-declared|declare its own|its own practices|instruction packs?|own named presets).{0,250}" *.md | grep -v instruments | cut -c1-520
````

38. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && for f in 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md; do grep -c -i -E 'regroup|gov-only|govern only gov|gov.s overlay' $f; grep -n -o -i -E '.{0,120}foundation set.{0,200}' $f; done; grep -n -i -E 'gap-found-19' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | cut -c1-80; git -C /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 log --oneline -S"gov's overlay split out" -- memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | tail -3
````

39. Bash

````text
git log --oneline -S"overlay split out" -- memory/builds/dClosedLoop/build/ | tail -5; git log --oneline -S"rules that govern only gov" -- memory/builds/dClosedLoop/build/ | tail -5
````

40. Bash

````text
git log --oneline -S"overlay" -- memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | tail -5; git log --oneline --diff-filter=A -- memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md; git show $(git log --format=%h --diff-filter=A -- memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md):memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | grep -n -i 'dConvergedCharter |' | cut -c1-400
````

41. Bash

````text
git log --format=%h -S"every adopter's overlay, gov's included" -- memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | while read c; do git log -1 --format='%h %s' $c; done
````

42. Bash

````text
git show aa0d778b1 -- memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | grep -E '^[-+]\| dConvergedCharter' | cut -c1-500
````

43. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i -E "overlay|project block|adopter's own (rules|instruction|units)|instructions\.toml|instruction manifest" 2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md 2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md 2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md 2026-10-18-build-PLAY-dClosedLoop-1-shape-reviews-compared.md 2026-10-18-build-PLAY-dClosedLoop-1-answers-reviews-compared.md 2026-10-18-build-PLAY-dClosedLoop-1-fates.md 2026-10-18-build-PLAY-dClosedLoop-1-recut.md 2026-10-16-build-PLAY-dClosedLoop-1-state.md | cut -c1-400
````

44. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i -E 'deploy\.toml|house|adopter_rules|charter template|playbook' 2026-10-18-build-PLAY-dClosedLoop-1-fates.md 2026-10-18-build-PLAY-dClosedLoop-1-walk.md | grep -i -E 'fate|MERGED|KEPT|RESHAPED|RETIRED|·' | cut -c1-300 | head -20
````

45. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -E '^\| (unique|owned|retired|resolves)' 2026-10-16-build-PLAY-dClosedLoop-1-systems.md; grep -n -E 'Mint, rename, retire|one fact in one unit|merged by row key' 2026-10-16-build-PLAY-dClosedLoop-1-systems.md; grep -n -E '^\| `pinned-at`|^\| `amends`|^\| `supersedes`|^\| one owner|^\| retire, never' 2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md; grep -n -E 'retired-edits` moves' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | cut -c1-60; grep -n 'and the registry.s entries, each later class' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | cut -c1-20
````

46. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -E '^  \| (unique|owned|retired|resolves)' 2026-10-16-build-PLAY-dClosedLoop-1-systems.md | cut -c1-120; grep -n 'An unregistered type reds' 2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md
````

## [adopter-prior-art] Dispatch 120: prior art outside gov

1. WebFetch

````text
https://code.claude.com/docs/en/memory
How does CLAUDE.md hierarchy work: which locations, precedence/order of loading, @imports syntax and depth limits, .claude/rules path-scoped rules, CLAUDE.local.md. Does a more specific file override or are all concatenated? Quote relevant sentences.
````

2. WebFetch

````text
https://agents.md/
What does it say about nested AGENTS.md precedence, closest file wins, conflicts with user prompts? Quote exactly.
````

3. WebFetch

````text
https://developer.mozilla.org/en-US/docs/Web/CSS/@layer
How does layer order determine precedence; unlayered styles vs layered; !important reversal. Quote key sentences.
````

4. WebFetch

````text
https://eslint.org/docs/latest/use/configure/configuration-files
How do flat config arrays merge: later objects override earlier ones? How to extend shared configs and override a rule's severity? Quote key sentences on cascading/merging.
````

5. WebFetch

````text
https://git-scm.com/docs/git-config
Configuration file levels (system, global, local, worktree) and precedence: which wins, last value wins? Multi-valued keys and how to reset/clear a multi-valued variable in a later file (empty value). Quote key sentences.
````

6. WebFetch

````text
https://docs.cursor.com/context/rules
Rule types (Always, Auto Attached, Agent Requested, Manual), .cursor/rules locations, nested rules, precedence between team/user/project rules, AGENTS.md support. Quote key sentences.
````

7. WebFetch

````text
https://kubectl.docs.kubernetes.io/references/kustomize/kustomization/patches/
How do patches work: strategic merge vs JSON6902, target selection by kind/name/labels, what happens if target is not found? Quote key sentences.
````

8. WebFetch

````text
https://helm.sh/docs/chart_template_guide/values_files/
Precedence of values: chart values.yaml, parent chart, -f files, --set. How to delete a default key (null). Quote key sentences.
````

9. WebFetch

````text
https://jinja.palletsprojects.com/en/stable/templates/#template-inheritance
How template inheritance works: extends, block overrides, super(), what happens if child defines a block not in parent. Quote key sentences.
````

10. WebFetch

````text
https://cursor.com/docs/context/rules
Rule types (Always Apply, Apply Intelligently, Apply to Specific Files, Manually), .cursor/rules locations, nested rules, precedence between team/user/project rules and AGENTS.md. Quote key sentences especially on precedence and conflicts.
````

11. WebFetch

````text
https://docusaurus.io/docs/swizzling
Wrap vs eject; safe vs unsafe components; what happens to ejected components on Docusaurus upgrade; recommendations. Quote key sentences.
````

12. WebFetch

````text
https://developer.wordpress.org/themes/advanced-topics/child-themes/
How child themes override parent templates (file of same name), functions.php loading order, how updates to parent theme are preserved. Quote key sentences.
````

13. WebFetch

````text
https://guides.rubyonrails.org/engines.html
How does an application override an engine's views (same path in app/views takes precedence)? Quote key sentences about overriding views and models (decorators / class_eval).
````

14. WebFetch

````text
https://copier.readthedocs.io/en/stable/updating/
How does copier update work: answers file, regenerating old version, diff, three-way merge, conflict modes (inline markers vs .rej), skip_if_exists, migrations. Quote key sentences.
````

15. WebFetch

````text
https://cruft.github.io/cruft/
How cruft update works (.cruft.json commit hash, diff between template versions applied as patch, three-way, .rej files, skip list), cruft check for CI. Quote key sentences.
````

16. WebFetch

````text
https://manpages.debian.org/bookworm/ucf/ucf.1.en.html
How ucf handles a configuration file the user modified when new version ships: md5sum cache, prompt options (install new, keep, show diff, 3-way merge), --three-way, side files (.ucf-dist, .ucf-old, .ucf-new), non-interactive behavior with debconf frontend noninteractive / UCF_FORCE_CONFFOLD. Quote key sentences.
````

17. WebFetch

````text
https://git-scm.com/docs/git-merge-file
What does git merge-file do, arguments current base other, conflict markers, exit status, --ours/--theirs/--union. Quote key sentences.
````

18. WebFetch

````text
https://www.debian.org/doc/debian-policy/ap-pkg-conffiles.html
How dpkg handles conffiles on upgrade when user modified and package changed: prompt, .dpkg-dist, .dpkg-old, --force-confold/confnew/confdef; removed conffile; obsolete conffiles. Quote key sentences.
````

19. WebFetch

````text
https://github.com/ds300/patch-package
How patch-package works: patches dir, postinstall reapply, what happens when package version changes or a patch fails to apply (warning vs error, --error-on-fail, CI behavior). Quote key sentences.
````

20. WebFetch

````text
https://man7.org/linux/man-pages/man1/dpkg.1.html
Quote what dpkg says about confold, confnew, confdef, confmiss, confask, and the .dpkg-dist and .dpkg-old files.
````

21. WebFetch

````text
https://docs.fedoraproject.org/en-US/packaging-guidelines/#_configuration_files
Quote what it says about %config vs %config(noreplace), .rpmnew and .rpmsave behavior.
````

22. WebFetch

````text
https://developers.openai.com/codex/guides/agents-md
How Codex discovers AGENTS.md: global ~/.codex, AGENTS.override.md, root to cwd concatenation order, later overrides earlier, project_doc_max_bytes size limit (default 32 KiB) and what happens when exceeded. Quote key sentences.
````

23. WebFetch

````text
https://www.man7.org/linux/man-pages/man1/quilt.1.html
Quote what quilt says about the series file, push/pop, refresh, push failing when a patch does not apply (-f force, .rej), and fuzz.
````

24. WebFetch

````text
https://learn.chatgpt.com/docs/agent-configuration/agents-md
How Codex discovers AGENTS.md: global ~/.codex, AGENTS.override.md, root to cwd concatenation order, later overrides earlier, project_doc_max_bytes size limit (default value) and what happens when exceeded. Quote key sentences.
````

25. WebFetch

````text
https://rpm-software-management.github.io/rpm/manual/spec.html
Quote what it says about %config and %config(noreplace), .rpmnew, .rpmsave behaviors.
````

26. WebFetch

````text
https://kubectl.docs.kubernetes.io/references/kustomize/kustomization/patchesstrategicmerge/
Quote what it says about $patch: delete / replace directives, and any statement about errors when a patch target resource is missing.
````

27. WebFetch

````text
https://rpm-software-management.github.io/rpm/man/rpm-spec.5
Quote what it says about %config and %config(noreplace), .rpmnew, .rpmsave behaviors.
````

28. WebFetch

````text
https://developer.wordpress.org/plugins/hooks/filters/
Quote how add_filter works, priority ordering, and remove_filter. What happens if the hook name no longer exists (filter never runs)?
````

29. WebFetch

````text
https://create-react-app.dev/docs/available-scripts/#npm-run-eject
Quote what npm run eject does and that it is one-way; what you lose regarding updates.
````

30. WebFetch

````text
https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html
Quote what it says about drop-in directories (foo.service.d/*.conf), override precedence of /etc over /usr/lib, masking with /dev/null symlink, and resetting list settings with an empty assignment.
````

31. WebFetch

````text
https://www.freedesktop.org/software/systemd/man/latest/systemd-delta.html
Quote what systemd-delta does and its categories (masked, equivalent, redirected, overridden, extended, unchanged).
````

32. WebFetch

````text
https://nixos.org/manual/nixos/stable/#sec-option-definitions-setting-priorities
Quote what it says about mkDefault, mkForce, mkOverride priorities, and what happens when two definitions of a non-mergeable option conflict at the same priority (error). Also mkBefore/mkAfter ordering.
````

33. WebFetch

````text
https://manpages.debian.org/bookworm/dpkg/dpkg-maintscript-helper.1.en.html
Quote what rm_conffile and mv_conffile do, how they treat a user-modified conffile (renamed to .dpkg-bak / kept), and the prior-version argument.
````

34. WebSearch

````text
kustomize strategic merge patch "failed to find unique target for patch" error
````

35. WebFetch

````text
https://jinja.palletsprojects.com/en/stable/templates/#template-inheritance
Anything about required blocks ({% block x required %}), what is rendered of a child template outside blocks, or blocks defined in a child that the parent lacks.
````

36. WebFetch

````text
https://jinja.palletsprojects.com/en/stable/templates/#required-blocks
Quote the "Required Blocks" section exactly, and anything about content in a child template outside of blocks.
````

37. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/probe"; rm -rf "$S"; mkdir -p "$S"; cd "$S"
# Probe A: three-way merge, upstream rewords a line the adopter amended
printf '%s\n' "# Rules" "- [verify] Verify before claiming done." "- [reuse] Reuse before building." > base.md
printf '%s\n' "# Rules" "- [verify] Verify before claiming done, and attach the gate log." "- [reuse] Reuse before building." > adopter.md
printf '%s\n' "# Rules" "- [verify] Verify before claiming done: a check that exercises THIS change." "- [reuse] Reuse before building." > upstream.md
cp adopter.md merged.md; git merge-file -L adopter -L base -L upstream merged.md base.md upstream.md; echo "A exit=$?"; cat merged.md
echo ----
# Probe A2: upstream splits the line into two units; adopter amended the original
printf '%s\n' "# Rules" "- [verify] Verify before claiming done." "- [verify-scope] The check must exercise THIS change." "- [reuse] Reuse before building." > upstream2.md
cp adopter.md merged2.md; git merge-file -L adopter -L base -L upstream merged2.md base.md upstream2.md; echo "A2 exit=$?"; cat merged2.md
echo ----
# Probe B: patch queue with fuzz; upstream inserts a new section with the same context lines
printf '%s\n' "## Build" "Run the gates." "Never push red." "" "## Deploy" "Tag the release." > b0.md
printf '%s\n' "## Build" "Run the gates." "Never push red." "Adopter: also run lint." "" "## Deploy" "Tag the release." > b1.md
diff -u b0.md b1.md > adopter.patch
printf '%s\n' "## Review" "Run the gates." "Never push red." "" "## Build" "Run the gates locally." "Never push red." "" "## Deploy" "Tag the release." > b2.md
patch --dry-run -o - b2.md < adopter.patch; echo "B exit=$?"
which patch
````

38. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/probe"; cd "$S"
PY=$(bash C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/lib/resolve-python.sh 2>/dev/null); echo "py=$PY"
cat > c2.py <<'EOF'
import hashlib,json,sys
h=lambda s: hashlib.sha256(s.encode()).hexdigest()[:12]
def check(upstream, amendments, steps):
    # steps: list of (op, old, new) retargets shipped by upstream release
    errs=[]
    for a in amendments:
        tgt=a["target"]
        for op,old,new in steps:
            if tgt==old and op=="rename": tgt=new
            if tgt==old and op=="split": errs.append(f"{a['tag']}: target {old} split into {new}; retarget required"); tgt=None
        if tgt is None: continue
        if tgt not in upstream: errs.append(f"{a['tag']}: dangling amends -> {tgt}"); continue
        if h(upstream[tgt])!=a["base"]: errs.append(f"{a['tag']}: base drift on {tgt} (pinned {a['base']}, now {h(upstream[tgt])})")
    return errs
v1={"core.verify":"Verify before claiming done.","core.reuse":"Reuse before building."}
am=[{"tag":"local.verify-log","target":"core.verify","base":h(v1["core.verify"]),"text":"Attach the gate log."}]
cases={
 "S0 unchanged": (v1,[]),
 "S1 reword": ({**v1,"core.verify":"Verify before claiming done: a check that exercises THIS change."},[]),
 "S1b typo-only": ({**v1,"core.verify":"Verify before claiming done. "},[]),
 "S2 rename w/ step": ({"core.verify-done":v1["core.verify"],"core.reuse":v1["core.reuse"]},[("rename","core.verify","core.verify-done")]),
 "S2b rename no step": ({"core.verify-done":v1["core.verify"],"core.reuse":v1["core.reuse"]},[]),
 "S3 split": ({"core.verify":"Verify before claiming done.","core.verify-scope":"The check must exercise THIS change.","core.reuse":v1["core.reuse"]},[("split","core.verify","core.verify,core.verify-scope")]),
 "S4 contradicting new unit": ({**v1,"core.no-logs":"Never attach gate logs to the record."},[]),
}
for k,(up,st) in cases.items(): print(k,"->",check(up,am,st) or "PASS (green)")
EOF
"$PY" -I c2.py
````

39. Bash

````text
sed -n '1,40p' C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/lib/resolve-python.sh | grep -nE '^(#|[a-z_]+\(\))' | head; for c in python3 python py; do $c -c 'print(1)' 2>/dev/null && echo "ok $c"; done
````

40. Bash

````text
cd "C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/probe" && python3 -I c2.py
````

41. WebFetch

````text
https://www.rfc-editor.org/rfc/rfc6902#section-4.6
Quote section 4.6 "test" operation and section 5 on error handling (what happens to the whole patch if an operation fails).
````

## [adopter-history] Dispatch 121: the owner's hypothesis against gov's history

1. Bash

````text
git log --reverse --format='%h %ad' --date=short | head -1; git log --format='%h %ad' --date=short | head -1; git rev-list --count HEAD; ls; ls tools; ls tools/roles; git ls-files | grep -E '\.template\.md$|guides/|HYGIENE|TEMPLATE-SPEC|SKILL' | head -100
````

2. Bash

````text
git ls-files tools | grep -E '\.template\.md$|\.md$' ; echo ---; ls tools/roles/agents tools/roles/house; git ls-files tools/roles; echo ---; git ls-files | grep -iE 'MERGE-BAR|SESSION-KICKOFF'; 
````

3. Bash

````text
cat tools/memory-tree/kit.toml | head -60; echo ----; grep -rn "MERGE-BAR\|SESSION-KICKOFF" --include=*.toml --include=*.sh --include=*.json tools skills | head -20
````

4. Bash

````text
wc -l coding-governance-agents.template.md tools/*/*.template.md tools/roles/agents/* tools/roles/house/*.md skills/*/SKILL.md; grep -n '^#\|^- \*\*\[\|^- \[' coding-governance-agents.template.md | head -80
````

5. Bash

````text
cat tools/roles/agents/gov-researcher.agent.md; echo ====; grep -c '^#' tools/*/*.template.md skills/*/SKILL.md; sed -n 89,201p coding-governance-agents.template.md
````

6. Bash

````text
for f in coding-governance-agents.template.md tools/memory-tree/ANNOTATION-STYLE.template.md tools/memory-tree/BUILD-METHOD.template.md tools/memory-tree/HYGIENE.template.md tools/memory-tree/SPEC-TEMPLATE.template.md tools/unattended/ASKS.template.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/PROTOCOL.template.md tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/workflows/REVIEW-PROTOCOL.template.md tools/branch-reconcile/SKILL.template.md tools/drift-audit/SKILL.template.md tools/lexicon/SKILL.template.md tools/memory-recall/SKILL.template.md tools/roles/SKILL.template.md tools/runlog/SKILL.template.md tools/unattended/SKILL.template.md skills/deploy-governance/SKILL.md skills/session-kickoff/SKILL.md tools/roles/agents/gov-builder.agent.md; do n=$(git log --follow --format=%h -- $f | wc -l); first=$(git log --follow --reverse --format='%ad' --date=short -- $f | head -1); names=$(git log --follow --name-only --format= -- $f | sort -u | tr '\n' ' '); echo "$n $first $f :: $names"; done
````

7. Bash

````text
git log --all --format= --name-only --diff-filter=AD | grep -iE 'template\.md$|agent\.md$|SKILL\.md$|governance.*\.md$' | sort | uniq -c | sort -rn | head -60
````

8. Bash

````text
git log --format='%h %ad %s' --date=short --name-status --diff-filter=ADR -- 'parallel-coding-governance*' 'memory/archive/*governance*' 'coding-governance-agents*' | head -60
````

9. Bash

````text
P="parallel-coding-governance.template.md coding-governance-agents.template.md parallel-coding-governance.domain-rules.md parallel-coding-governance.customize.md :(glob)tools/**/*.template.md :(glob)memory-tree/*.template.md :(glob)tools/roles/agents/*.md :(glob)tools/roles/house/*.md :(glob)skills/*/SKILL.md"; git log --no-merges --format=%h -- $P | wc -l; git log --first-parent --format=%h -- $P | wc -l; git log --merges --format=%h | wc -l; git log --first-parent --format=%h | wc -l; bash tools/lib/resolve-python.sh 2>/dev/null; cat tools/lib/resolve-python.sh | head -30
````

10. Bash

````text
. tools/lib/resolve-python.sh && PY=$(resolve_python) && echo $PY && $PY --version; S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; mkdir -p "$S/anchors" && ls "$S"
````

11. Bash

````text
git show 5b00666a2^:parallel-coding-governance.customize.md | head -40; echo ====; git show 5b00666a2 --stat | head -20; git log -1 --format=%B 5b00666a2 | head -30
````

12. Bash

````text
grep -n '^#' tools/memory-tree/BUILD-METHOD.template.md tools/memory-tree/HYGIENE.template.md tools/unattended/STOPS.template.md | head -60; grep -nE '^\s*[-*] \[[a-z0-9-]+\]|^\*\*[A-Z]?[0-9]+' tools/*/*.template.md | head; head -12 tools/lexicon/SKILL.template.md; grep -n '^- \*\*M[0-9]\|^\*\*M[0-9]\|^M[0-9]' tools/memory-tree/BUILD-METHOD.template.md | head
````

13. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors"; cat > "$S/seg.py" <<'EOF'
"""Segment a gov instruction source into units by today's anchors.

Precedence, per line:
  1. a charter rule tag   `- [tag] ...`            -> anchor  "[tag]"   (the bullet and its continuation lines)
  2. a markdown heading   `#.. text` (not in fence) -> anchor  "H<n> text" (everything up to the next anchor)
  3. a front-matter field `key: value` in a leading `---` block (role fields; Skill name/description)
                                                    -> anchor  "field:key"
Text before any anchor goes to anchor "(preamble)". A unit whose body is empty after whitespace
collapse is structural only and is dropped. Duplicate anchors in one file get a "#2", "#3" suffix.
"""
import re, sys

TAG = re.compile(r'^\s*- \[([a-z0-9][a-z0-9-]*)\]\s')
HEAD = re.compile(r'^(#{1,6})\s+(.*?)\s*#*\s*$')
FIELD = re.compile(r'^([A-Za-z_][A-Za-z0-9_-]*):(\s|$)')
FENCE = re.compile(r'^\s*(```|~~~)')

def group_of(path):
    if path in ('parallel-coding-governance.template.md', 'coding-governance-agents.template.md',
                'parallel-coding-governance.domain-rules.md', 'parallel-coding-governance.customize.md'):
        return 'charter'
    if 'fixture' in path:
        return None
    if re.match(r'^(tools/)?memory-tree/(HYGIENE|SPEC-TEMPLATE)\.template\.md$', path):
        return 'hygiene+spec'
    if re.match(r'^tools/roles/(agents|house)/[^/]+\.md$', path) or path.endswith('.agent.template.md'):
        return 'roles'
    if re.match(r'^tools/.*SKILL\.template\.md$', path) or re.match(r'^skills/[^/]+/SKILL\.md$', path):
        return 'skills'
    if re.match(r'^(tools/.*|memory-tree/[^/]+)\.template\.md$', path):
        return 'guides'
    return None

def segment(text):
    lines = text.replace('\r\n', '\n').split('\n')
    units = []          # [anchor, kind, [lines]]
    i = 0
    if lines and lines[0].strip() == '---':          # front matter: role fields
        j = 1
        while j < len(lines) and lines[j].strip() != '---':
            m = FIELD.match(lines[j])
            if m:
                units.append(['field:' + m.group(1), 'field', [lines[j][m.end(1)+1:]]])
            elif units:
                units[-1][2].append(lines[j])
            j += 1
        i = j + 1
    cur = ['(preamble)', 'preamble', []]
    units.append(cur)
    in_fence = False
    in_tag = False
    for ln in lines[i:]:
        if FENCE.match(ln):
            in_fence = not in_fence
        if not in_fence:
            h = HEAD.match(ln)
            t = TAG.match(ln)
            if h:
                cur = ['H%d %s' % (len(h.group(1)), h.group(2)), 'heading', []]
                units.append(cur); in_tag = False; continue
            if t:
                cur = ['[%s]' % t.group(1), 'tag', [ln[t.end():]]]
                units.append(cur); in_tag = True; continue
            if in_tag and (ln.strip() == '' or re.match(r'^\s*([-*]|\d+\.)\s', ln) or ln.startswith('<!--')):
                # a tag unit ends at a blank line, the next bullet or a marker; the rest returns
                # to the heading it sits under
                parent = next(u for u in reversed(units) if u[1] in ('heading', 'preamble'))
                cur = parent; in_tag = False
        cur[2].append(ln)
    out, seen = [], {}
    for a, k, ls in units:
        body = '\n'.join(ls).strip('\n')
        if not ' '.join(body.split()):
            continue
        seen[a] = seen.get(a, 0) + 1
        out.append((a if seen[a] == 1 else '%s#%d' % (a, seen[a]), k, body))
    return out

if __name__ == '__main__':
    for p in sys.argv[1:]:
        us = segment(open(p, encoding='utf-8', errors='replace').read())
        kinds = {}
        for a, k, b in us:
            kinds[k] = kinds.get(k, 0) + 1
        print('%-55s units=%3d %s' % (p, len(us), ' '.join('%s=%d' % kv for kv in sorted(kinds.items()))))
EOF
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python3 - <<EOF
import subprocess,sys
sys.path.insert(0, r"$S")
from seg import group_of, segment
files=subprocess.run(['git','ls-files'],capture_output=True,text=True).stdout.split()
tot={}
for f in files:
    g=group_of(f)
    if not g: continue
    us=segment(open(f,encoding='utf-8').read())
    kinds={}
    for a,k,b in us: kinds[k]=kinds.get(k,0)+1
    t=tot.setdefault(g,[0,0,{}]); t[0]+=1; t[1]+=len(us)
    for k,v in kinds.items(): t[2][k]=t[2].get(k,0)+v
    print('%-12s %-52s %3d %s'%(g,f,len(us),kinds))
print()
for g,(nf,nu,k) in tot.items(): print('%-12s files=%2d units=%4d %s'%(g,nf,nu,k))
print('TOTAL files=%d units=%d'%(sum(v[0] for v in tot.values()),sum(v[1] for v in tot.values())))
EOF
````

14. Bash

````text
S="$(cygpath -m /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors)"; cat > "$S/count.py" <<'EOF'
import subprocess, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seg import group_of, segment
files = subprocess.run(['git', 'ls-files'], capture_output=True, text=True).stdout.split()
tot = {}
for f in files:
    g = group_of(f)
    if not g: continue
    us = segment(open(f, encoding='utf-8').read())
    kinds = {}
    for a, k, b in us: kinds[k] = kinds.get(k, 0) + 1
    t = tot.setdefault(g, [0, 0, {}]); t[0] += 1; t[1] += len(us)
    for k, v in kinds.items(): t[2][k] = t[2].get(k, 0) + v
    print('%-12s %-50s %3d %s' % (g, f, len(us), kinds))
print()
for g, (nf, nu, k) in tot.items(): print('%-12s files=%2d units=%4d %s' % (g, nf, nu, k))
print('TOTAL files=%d units=%d' % (sum(v[0] for v in tot.values()), sum(v[1] for v in tot.values())))
EOF
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python3 "$S/count.py"
````

15. Bash

````text
S="$(cygpath -m /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors)"; cat > "$S/walk.py" <<'EOF'
"""Walk every commit that touched a source, classify what happened to each unit.

usage: walk.py <mode> <out.json>     mode = commits (every non-merge commit, diff vs parent)
                                          | landings (first-parent chain, diff vs first parent)
Matcher, per commit, over the files the commit changed (old side = parent, new side = commit):
  M1 identity: same file lineage (git -M rename resolved) + same anchor      -> kept / text edit
  M2 rename/move: leftover old x leftover new, word-level SequenceMatcher ratio >= 0.6,
     greedy best-first                                                      -> anchor rename / move
  M3 merge: leftover old unit whose 4-word shingles are >= 50% inside ONE new unit
  M3 split: leftover old unit spread over >= 2 new units (each >= 15%, sum >= 50%),
            or a leftover NEW unit >= 50% drawn from an old unit that M1/M2 kept (split-off)
  M4 leftover old -> retired;  leftover new -> added
"""
import json, os, re, subprocess, sys
from difflib import SequenceMatcher
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seg import group_of, segment

def git(*a):
    return subprocess.run(['git'] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout

_blob = {}
def units_of(rev, path):
    k = (rev, path)
    if k not in _blob:
        txt = subprocess.run(['git', 'show', '%s:%s' % (rev, path)], capture_output=True).stdout.decode('utf-8', 'replace')
        _blob[k] = segment(txt)
    return _blob[k]

def norm(b): return ' '.join(b.split())
def words(b): return norm(b).lower().split()
def shingles(b):
    w = words(b)
    return set(tuple(w[i:i+4]) for i in range(max(1, len(w) - 3))) if len(w) >= 4 else set((x,) for x in w)
def ratio(a, b):
    return SequenceMatcher(None, words(a), words(b), autojunk=False).ratio()
def contain(x, y):
    sx = shingles(x)
    return len(sx & shingles(y)) / len(sx) if sx else 0.0
def placeholders_only(a, b):
    f = lambda s: re.sub(r'\{\{[A-Z0-9_]+\}\}', '{{P}}', norm(s))
    return f(a) == f(b)

def changes(parent, rev):
    """name-status with renames, over the WHOLE tree, filtered to the source predicate on either side."""
    out = git('diff-tree', '-r', '-M', '--no-commit-id', '--name-status', parent, rev)
    rows = []
    for ln in out.splitlines():
        p = ln.split('\t')
        st = p[0][0]
        if st == 'R':
            old, new = p[1], p[2]
        elif st == 'A':
            old, new = None, p[1]
        elif st == 'D':
            old, new = p[1], None
        else:
            old = new = p[1]
        og = group_of(old) if old else None
        ng = group_of(new) if new else None
        if og or ng:
            rows.append((st, old if og else None, new if ng else None))
    return rows

def classify(parent, rev):
    rows = changes(parent, rev)
    old, new = [], []      # (file, lineage, ordinal, anchor, kind, body)
    file_renames = 0
    for st, o, n in rows:
        lin = n or o
        if o and n and o != n:
            file_renames += 1
        if o:
            for i, (a, k, b) in enumerate(units_of(parent, o)): old.append((o, lin, i, a, k, b))
        if n:
            for i, (a, k, b) in enumerate(units_of(rev, n)): new.append((n, lin, i, a, k, b))
    ev = []
    mo, mn = {}, {}
    byk = {(u[1], u[3]): j for j, u in enumerate(new)}
    for i, u in enumerate(old):                                   # M1
        j = byk.get((u[1], u[3]))
        if j is not None and j not in mn:
            mo[i] = j; mn[j] = i
    lo = [i for i in range(len(old)) if i not in mo]
    ln_ = [j for j in range(len(new)) if j not in mn]
    cand = []
    for i in lo:                                                   # M2
        for j in ln_:
            r = ratio(old[i][5], new[j][5])
            if r >= 0.6: cand.append((r, i, j))
    for r, i, j in sorted(cand, reverse=True):
        if i in mo or j in mn: continue
        mo[i] = j; mn[j] = i
    for i, j in mo.items():
        o, n = old[i], new[j]
        e = {'old': [o[0], o[3]], 'new': [n[0], n[3]], 'kind': o[4], 'group': group_of(o[0]),
             'ordinal_moved': o[2] != n[2]}
        e['edit'] = norm(o[5]) != norm(n[5])
        e['reflow_only'] = (o[5] != n[5]) and not e['edit']
        e['placeholder_only'] = e['edit'] and placeholders_only(o[5], n[5])
        e['sim'] = round(ratio(o[5], n[5]), 3) if e['edit'] else 1.0
        e['rename'] = o[3] != n[3]
        e['move'] = o[1] != n[1]
        e['file_rename'] = (o[0] != n[0]) and (o[1] == n[1])
        e['type'] = 'kept'
        ev.append(e)
    used_split_src = set()
    lo = [i for i in range(len(old)) if i not in mo]
    for i in lo:                                                   # M3 merge / split
        o = old[i]
        cs = sorted(((contain(o[5], new[j][5]), j) for j in range(len(new))), reverse=True)
        e = {'old': [o[0], o[3]], 'new': None, 'kind': o[4], 'group': group_of(o[0]), 'edit': True}
        if cs and cs[0][0] >= 0.5:
            e['type'] = 'merge'; e['new'] = [new[cs[0][1]][0], new[cs[0][1]][3]]
            e['move'] = new[cs[0][1]][1] != o[1]
        elif sum(c for c, j in cs if c >= 0.15) >= 0.5 and len([c for c, j in cs if c >= 0.15]) >= 2:
            e['type'] = 'split'; e['move'] = any(new[j][1] != o[1] for c, j in cs if c >= 0.15)
            used_split_src.add(i)
        else:
            e['type'] = 'retire'; e['move'] = False
        ev.append(e)
    ln_ = [j for j in range(len(new)) if j not in mn]
    split_off = {}
    for j in ln_:
        n = new[j]
        cs = sorted(((contain(n[5], old[i][5]), i) for i in range(len(old))), reverse=True)
        if cs and cs[0][0] >= 0.5 and cs[0][1] in mo:
            split_off.setdefault(cs[0][1], []).append(j)
        else:
            ev.append({'old': None, 'new': [n[0], n[3]], 'kind': n[4], 'group': group_of(n[0]), 'type': 'add'})
    for i, js in split_off.items():
        for e in ev:
            if e['type'] == 'kept' and e['old'] == [old[i][0], old[i][3]]:
                e['type'] = 'split_off'; e['split_into'] = [[new[j][0], new[j][3]] for j in js]
        for j in js:
            ev.append({'old': None, 'new': [new[j][0], new[j][3]], 'kind': new[j][4], 'group': group_of(new[j][0]),
                       'type': 'add_from_split'})
    return ev, file_renames

def snapshot_count(rev):
    """units per group in the whole source set at rev (the adopter's base)."""
    out = git('ls-tree', '-r', '--name-only', rev)
    c = {}
    keys = []
    for p in out.splitlines():
        g = group_of(p)
        if not g: continue
        for a, k, b in units_of(rev, p):
            c[g] = c.get(g, 0) + 1; keys.append([p, a])
    return c, keys

if __name__ == '__main__':
    mode, outp = sys.argv[1], sys.argv[2]
    paths = ['parallel-coding-governance.template.md', 'coding-governance-agents.template.md',
             'parallel-coding-governance.domain-rules.md', 'parallel-coding-governance.customize.md',
             ':(glob)tools/**/*.template.md', ':(glob)memory-tree/*.template.md',
             ':(glob)tools/roles/agents/*.md', ':(glob)tools/roles/house/*.md', ':(glob)skills/*/SKILL.md']
    if mode == 'commits':
        revs = git('log', '--no-merges', '--reverse', '--format=%H %P %ad', '--date=short', '--', *paths).splitlines()
    else:
        revs = git('log', '--first-parent', '--reverse', '--format=%H %P %ad', '--date=short', '--', *paths).splitlines()
    res = []
    for ln in revs:
        p = ln.split()
        rev, parent, date = p[0], p[1] if len(p) > 2 else None, p[-1]
        if parent is None or len(p) < 3: continue
        ev, fr = classify(parent, rev)
        if not ev: continue
        cnt, keys = snapshot_count(parent)
        res.append({'rev': rev[:9], 'date': date, 'file_renames': fr, 'events': ev, 'base_units': cnt, 'base_keys': keys})
        _blob.clear()
    json.dump(res, open(outp, 'w'), indent=0)
    print(mode, 'updates with a unit-level change:', len(res))
EOF
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && time python3 "$S/walk.py" landings "$S/landings.json"
````

16. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && cat > walk.py <<'PYEOF'
"""Walk every commit that touched a source, classify what happened to each unit.

usage: walk.py <mode> <out.json>     mode = commits (every non-merge commit, diff vs parent)
                                          | landings (first-parent chain, diff vs first parent)
Matcher, per commit, over the files the commit changed (old side = parent, new side = commit):
  M1 identity: same file lineage (git -M rename resolved) + same anchor      -> kept / text edit
  M2 rename/move: leftover old x leftover new, word-level SequenceMatcher ratio >= 0.6,
     greedy best-first                                                      -> anchor rename / move
  M3 merge: leftover old unit whose 4-word shingles are >= 50% inside ONE new unit
  M3 split: leftover old unit spread over >= 2 new units (each >= 15%, sum >= 50%),
            or a leftover NEW unit >= 50% drawn from an old unit that M1/M2 kept (split-off)
  M4 leftover old -> retired;  leftover new -> added
"""
import json, os, re, subprocess, sys
from difflib import SequenceMatcher
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seg import group_of, segment

def git(*a):
    return subprocess.run(['git'] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout

_blob = {}
def units_of(rev, path):
    k = (rev, path)
    if k not in _blob:
        txt = subprocess.run(['git', 'show', '%s:%s' % (rev, path)], capture_output=True).stdout.decode('utf-8', 'replace')
        _blob[k] = segment(txt)
    return _blob[k]

def norm(b): return ' '.join(b.split())
def words(b): return norm(b).lower().split()
def shingles(b):
    w = words(b)
    return set(tuple(w[i:i+4]) for i in range(max(1, len(w) - 3))) if len(w) >= 4 else set((x,) for x in w)
def ratio(a, b):
    return SequenceMatcher(None, words(a), words(b), autojunk=False).ratio()
def contain(x, y):
    sx = shingles(x)
    return len(sx & shingles(y)) / len(sx) if sx else 0.0
def placeholders_only(a, b):
    f = lambda s: re.sub(r'\{\{[A-Z0-9_]+\}\}', '{{P}}', norm(s))
    return f(a) == f(b)

def changes(parent, rev):
    out = git('diff-tree', '-r', '-M', '--no-commit-id', '--name-status', parent, rev)
    rows = []
    for ln in out.splitlines():
        p = ln.split('\t')
        st = p[0][0]
        if st in 'RC':
            old, new = p[1], p[2]
        elif st == 'A':
            old, new = None, p[1]
        elif st == 'D':
            old, new = p[1], None
        else:
            old = new = p[1]
        og = group_of(old) if old else None
        ng = group_of(new) if new else None
        if og or ng:
            rows.append((st, old if og else None, new if ng else None))
    return rows

def classify(parent, rev):
    rows = changes(parent, rev)
    old, new = [], []
    file_renames = 0
    for st, o, n in rows:
        lin = n or o
        if o and n and o != n:
            file_renames += 1
        if o:
            for i, (a, k, b) in enumerate(units_of(parent, o)): old.append((o, lin, i, a, k, b))
        if n:
            for i, (a, k, b) in enumerate(units_of(rev, n)): new.append((n, lin, i, a, k, b))
    ev = []
    mo, mn = {}, {}
    byk = {(u[1], u[3]): j for j, u in enumerate(new)}
    for i, u in enumerate(old):
        j = byk.get((u[1], u[3]))
        if j is not None and j not in mn:
            mo[i] = j; mn[j] = i
    lo = [i for i in range(len(old)) if i not in mo]
    ln_ = [j for j in range(len(new)) if j not in mn]
    cand = []
    for i in lo:
        for j in ln_:
            r = ratio(old[i][5], new[j][5])
            if r >= 0.6: cand.append((r, i, j))
    for r, i, j in sorted(cand, reverse=True):
        if i in mo or j in mn: continue
        mo[i] = j; mn[j] = i
    for i, j in mo.items():
        o, n = old[i], new[j]
        e = {'old': [o[0], o[3]], 'new': [n[0], n[3]], 'kind': o[4], 'group': group_of(o[0]),
             'ordinal_moved': o[2] != n[2], 'old_ord': o[2], 'new_ord': n[2]}
        e['edit'] = norm(o[5]) != norm(n[5])
        e['reflow_only'] = (o[5] != n[5]) and not e['edit']
        e['placeholder_only'] = e['edit'] and placeholders_only(o[5], n[5])
        e['sim'] = round(ratio(o[5], n[5]), 3) if e['edit'] else 1.0
        e['rename'] = o[3] != n[3]
        e['move'] = o[1] != n[1]
        e['file_rename'] = (o[0] != n[0]) and (o[1] == n[1])
        e['type'] = 'kept'
        ev.append(e)
    lo = [i for i in range(len(old)) if i not in mo]
    for i in lo:
        o = old[i]
        cs = sorted(((contain(o[5], new[j][5]), j) for j in range(len(new))), reverse=True)
        e = {'old': [o[0], o[3]], 'new': None, 'kind': o[4], 'group': group_of(o[0]), 'edit': True}
        big = [(c, j) for c, j in cs if c >= 0.15]
        if cs and cs[0][0] >= 0.5:
            e['type'] = 'merge'; e['new'] = [new[cs[0][1]][0], new[cs[0][1]][3]]
            e['move'] = new[cs[0][1]][1] != o[1]
        elif len(big) >= 2 and sum(c for c, j in big) >= 0.5:
            e['type'] = 'split'; e['move'] = any(new[j][1] != o[1] for c, j in big)
        else:
            e['type'] = 'retire'; e['move'] = False
        ev.append(e)
    ln_ = [j for j in range(len(new)) if j not in mn]
    split_off = {}
    for j in ln_:
        n = new[j]
        cs = sorted(((contain(n[5], old[i][5]), i) for i in range(len(old))), reverse=True)
        if cs and cs[0][0] >= 0.5 and cs[0][1] in mo:
            split_off.setdefault(cs[0][1], []).append(j)
        else:
            ev.append({'old': None, 'new': [n[0], n[3]], 'kind': n[4], 'group': group_of(n[0]), 'type': 'add'})
    for i, js in split_off.items():
        for e in ev:
            if e['type'] == 'kept' and e['old'] == [old[i][0], old[i][3]]:
                e['type'] = 'split_off'; e['split_into'] = [[new[j][0], new[j][3]] for j in js]
        for j in js:
            ev.append({'old': None, 'new': [new[j][0], new[j][3]], 'kind': new[j][4], 'group': group_of(new[j][0]),
                       'type': 'add_from_split'})
    return ev, file_renames

def snapshot(rev):
    out = git('ls-tree', '-r', '--name-only', rev)
    keys = []
    for p in out.splitlines():
        g = group_of(p)
        if not g: continue
        for a, k, b in units_of(rev, p):
            keys.append([p, a, g])
    return keys

if __name__ == '__main__':
    mode, outp = sys.argv[1], sys.argv[2]
    paths = ['parallel-coding-governance.template.md', 'coding-governance-agents.template.md',
             'parallel-coding-governance.domain-rules.md', 'parallel-coding-governance.customize.md',
             ':(glob)tools/**/*.template.md', ':(glob)memory-tree/*.template.md',
             ':(glob)tools/roles/agents/*.md', ':(glob)tools/roles/house/*.md', ':(glob)skills/*/SKILL.md']
    flag = '--no-merges' if mode == 'commits' else '--first-parent'
    revs = git('log', flag, '--reverse', '--format=%H %P', '--', *paths).splitlines()
    res = []
    for ln in revs:
        p = ln.split()
        if len(p) < 2: continue
        rev, parent = p[0], p[1]
        date = git('log', '-1', '--format=%ad', '--date=short', rev).strip()
        ev, fr = classify(parent, rev)
        if not ev: continue
        res.append({'rev': rev[:9], 'parent': parent[:9], 'date': date, 'file_renames': fr, 'events': ev,
                    'base_keys': snapshot(parent)})
        _blob.clear()
    json.dump(res, open(outp, 'w'))
    print(mode, 'commits listed:', len(revs), 'updates with a unit-level change:', len(res))
PYEOF
echo ok
````

17. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && cat > t.txt <<'PYEOF'
a 'x' {{P}} \{\{
    f = lambda s: re.sub(r'\{\{[A-Z0-9_]+\}\}', '{{P}}', norm(s))
PYEOF
cat t.txt
````

18. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && cat > walk.py <<'PYEOF'
"""Walk every commit that touched a source, classify what happened to each unit.

usage: walk.py MODE OUT.json     MODE = commits (every non-merge commit, diff vs parent)
                                      | landings (first-parent chain, diff vs first parent)
Matcher, per commit, over the files the commit changed (old side = parent, new side = commit):
  M1 identity: same file lineage (git -M rename resolved) + same anchor      -> kept / text edit
  M2 rename/move: leftover old x leftover new, word-level SequenceMatcher ratio >= 0.6,
     greedy best-first                                                      -> anchor rename / move
  M3 merge: leftover old unit whose 4-word shingles are >= 50% inside ONE new unit
  M3 split: leftover old unit spread over >= 2 new units (each >= 15%, sum >= 50%),
            or a leftover NEW unit >= 50% drawn from an old unit that M1/M2 kept (split-off)
  M4 leftover old -> retired;  leftover new -> added
"""
import json, os, re, subprocess, sys
from difflib import SequenceMatcher
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seg import group_of, segment

def git(*a):
    return subprocess.run(['git'] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout

_blob = {}
def units_of(rev, path):
    k = (rev, path)
    if k not in _blob:
        txt = subprocess.run(['git', 'show', rev + ':' + path], capture_output=True).stdout.decode('utf-8', 'replace')
        _blob[k] = segment(txt)
    return _blob[k]

def norm(b): return ' '.join(b.split())
def words(b): return norm(b).lower().split()
def shingles(b):
    w = words(b)
    return set(tuple(w[i:i+4]) for i in range(max(1, len(w) - 3))) if len(w) >= 4 else set((x,) for x in w)
def ratio(a, b):
    return SequenceMatcher(None, words(a), words(b), autojunk=False).ratio()
def contain(x, y):
    sx = shingles(x)
    return len(sx & shingles(y)) / len(sx) if sx else 0.0
PH = re.compile(r'\{\{[A-Z0-9_]+\}\}')
def placeholders_only(a, b):
    return PH.sub('P', norm(a)) == PH.sub('P', norm(b))
PYEOF
wc -l walk.py
````

19. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && cat >> walk.py <<'PYEOF'

def changes(parent, rev):
    out = git('diff-tree', '-r', '-M', '--no-commit-id', '--name-status', parent, rev)
    rows = []
    for ln in out.splitlines():
        p = ln.split('\t')
        st = p[0][0]
        if st in 'RC':
            old, new = p[1], p[2]
        elif st == 'A':
            old, new = None, p[1]
        elif st == 'D':
            old, new = p[1], None
        else:
            old = new = p[1]
        og = group_of(old) if old else None
        ng = group_of(new) if new else None
        if og or ng:
            rows.append((st, old if og else None, new if ng else None))
    return rows
PYEOF
wc -l walk.py
````

20. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && cat >> walk.py <<'PYEOF'

def classify(parent, rev):
    rows = changes(parent, rev)
    old, new = [], []
    file_renames = 0
    for st, o, n in rows:
        lin = n or o
        if o and n and o != n:
            file_renames += 1
        if o:
            for i, (a, k, b) in enumerate(units_of(parent, o)): old.append((o, lin, i, a, k, b))
        if n:
            for i, (a, k, b) in enumerate(units_of(rev, n)): new.append((n, lin, i, a, k, b))
    ev = []
    mo, mn = {}, {}
    byk = {(u[1], u[3]): j for j, u in enumerate(new)}
    for i, u in enumerate(old):
        j = byk.get((u[1], u[3]))
        if j is not None and j not in mn:
            mo[i] = j; mn[j] = i
    lo = [i for i in range(len(old)) if i not in mo]
    ln_ = [j for j in range(len(new)) if j not in mn]
    cand = []
    for i in lo:
        for j in ln_:
            r = ratio(old[i][5], new[j][5])
            if r >= 0.6: cand.append((r, i, j))
    for r, i, j in sorted(cand, reverse=True):
        if i in mo or j in mn: continue
        mo[i] = j; mn[j] = i
    for i, j in mo.items():
        o, n = old[i], new[j]
        e = dict(old=[o[0], o[3]], new=[n[0], n[3]], kind=o[4], group=group_of(o[0]),
                 ordinal_moved=(o[2] != n[2]), old_ord=o[2], new_ord=n[2])
        e['edit'] = norm(o[5]) != norm(n[5])
        e['reflow_only'] = (o[5] != n[5]) and not e['edit']
        e['placeholder_only'] = e['edit'] and placeholders_only(o[5], n[5])
        e['sim'] = round(ratio(o[5], n[5]), 3) if e['edit'] else 1.0
        e['rename'] = o[3] != n[3]
        e['move'] = o[1] != n[1]
        e['file_rename'] = (o[0] != n[0]) and (o[1] == n[1])
        e['type'] = 'kept'
        ev.append(e)
    lo = [i for i in range(len(old)) if i not in mo]
    for i in lo:
        o = old[i]
        cs = sorted(((contain(o[5], new[j][5]), j) for j in range(len(new))), reverse=True)
        e = dict(old=[o[0], o[3]], new=None, kind=o[4], group=group_of(o[0]), edit=True, old_ord=o[2])
        big = [(c, j) for c, j in cs if c >= 0.15]
        if cs and cs[0][0] >= 0.5:
            e['type'] = 'merge'; e['new'] = [new[cs[0][1]][0], new[cs[0][1]][3]]
            e['move'] = new[cs[0][1]][1] != o[1]
        elif len(big) >= 2 and sum(c for c, j in big) >= 0.5:
            e['type'] = 'split'; e['move'] = any(new[j][1] != o[1] for c, j in big)
        else:
            e['type'] = 'retire'; e['move'] = False
        ev.append(e)
    ln_ = [j for j in range(len(new)) if j not in mn]
    split_off = {}
    for j in ln_:
        n = new[j]
        cs = sorted(((contain(n[5], old[i][5]), i) for i in range(len(old))), reverse=True)
        if cs and cs[0][0] >= 0.5 and cs[0][1] in mo:
            split_off.setdefault(cs[0][1], []).append(j)
        else:
            ev.append(dict(old=None, new=[n[0], n[3]], kind=n[4], group=group_of(n[0]), type='add'))
    for i, js in split_off.items():
        for e in ev:
            if e['type'] == 'kept' and e['old'] == [old[i][0], old[i][3]]:
                e['type'] = 'split_off'; e['split_into'] = [[new[j][0], new[j][3]] for j in js]
        for j in js:
            ev.append(dict(old=None, new=[new[j][0], new[j][3]], kind=new[j][4], group=group_of(new[j][0]),
                           type='add_from_split'))
    return ev, file_renames
PYEOF
wc -l walk.py
````

21. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && cat >> walk.py <<'PYEOF'

def snapshot(rev):
    out = git('ls-tree', '-r', '--name-only', rev)
    keys = []
    for p in out.splitlines():
        g = group_of(p)
        if not g: continue
        for i, (a, k, b) in enumerate(units_of(rev, p)):
            keys.append([p, a, g, i])
    return keys

PATHS = ['parallel-coding-governance.template.md', 'coding-governance-agents.template.md',
         'parallel-coding-governance.domain-rules.md', 'parallel-coding-governance.customize.md',
         ':(glob)tools/**/*.template.md', ':(glob)memory-tree/*.template.md',
         ':(glob)tools/roles/agents/*.md', ':(glob)tools/roles/house/*.md', ':(glob)skills/*/SKILL.md']

def main():
    mode, outp = sys.argv[1], sys.argv[2]
    flag = '--no-merges' if mode == 'commits' else '--first-parent'
    revs = git('log', flag, '--reverse', '--format=%H %P %ad', '--date=short', '--', *PATHS).splitlines()
    res = []
    for ln in revs:
        p = ln.split()
        if len(p) < 3: continue
        rev, parent, date = p[0], p[1], p[-1]
        ev, fr = classify(parent, rev)
        if not ev: continue
        res.append(dict(rev=rev[:9], parent=parent[:9], date=date, file_renames=fr, events=ev,
                        base_keys=snapshot(parent)))
        _blob.clear()
    json.dump(res, open(outp, 'w'))
    print(mode, 'listed', len(revs), 'with unit-level change', len(res))

if __name__ == '__main__':
    main()
PYEOF
wc -l walk.py; cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && time python3 "$(cygpath -m /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors)/walk.py" landings "$(cygpath -m /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors)/landings.json"
````

22. Bash

````text
S="$(cygpath -m /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors)"; time python3 "$S/walk.py" commits "$S/commits.json"
````

23. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && cat > table.py <<'PYEOF'
"""History table: per group and total, what happened to units. usage: table.py X.json"""
import json, sys
from collections import Counter, defaultdict
data = json.load(open(sys.argv[1]))
G = ['charter', 'guides', 'hygiene+spec', 'roles', 'skills']
c = defaultdict(Counter)
for u in data:
    for e in u['events']:
        g = e['group']; t = e['type']
        rows = []
        if t in ('kept', 'split_off'):
            if e['edit']: rows.append('text_edit')
            if e.get('reflow_only'): rows.append('(reflow_only)')
            if e.get('placeholder_only'): rows.append('(placeholder_only)')
            if e['rename'] and not e['move']: rows.append('anchor_rename')
            if e['rename'] and not e['move'] and not e['edit']: rows.append('(rename_body_identical)')
            if e['move']: rows.append('move')
            if e['file_rename'] : rows.append('(in_file_rename)')
            if t == 'split_off': rows.append('split')
        elif t == 'split': rows.append('split'); rows += (['move'] if e['move'] else [])
        elif t == 'merge': rows.append('merge'); rows += (['move'] if e['move'] else [])
        elif t == 'retire': rows.append('retire')
        elif t == 'add': rows.append('(added)')
        elif t == 'add_from_split': rows.append('(added_from_split)')
        for r in rows: c[g][r] += 1; c['TOTAL'][r] += 1
cols = ['text_edit', 'anchor_rename', 'split', 'merge', 'move', 'retire', '(added)', '(added_from_split)',
        '(rename_body_identical)', '(reflow_only)', '(placeholder_only)', '(in_file_rename)']
print('%-13s' % 'group' + ''.join('%11s' % x.strip('()')[:10] for x in cols))
for g in G + ['TOTAL']:
    print('%-13s' % g + ''.join('%11d' % c[g][x] for x in cols))
print('updates:', len(data), ' first', data[0]['date'], ' last', data[-1]['date'],
      ' file renames in set:', sum(u['file_renames'] for u in data))
PYEOF
for m in commits landings; do echo "== $m"; python3 table.py $m.json; done
````

24. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && python3 - <<'PYEOF'
import json, subprocess
from collections import Counter
d = json.load(open('commits.json'))
rows = []
for u in d:
    c = Counter()
    for e in u['events']:
        t = e['type']
        if t == 'kept' and (e['rename'] or e['move']): c['ren/move'] += 1
        elif t in ('split', 'merge', 'retire', 'split_off'): c[t] += 1
    n = sum(c.values())
    if n: rows.append((n, u['rev'], u['date'], dict(c)))
rows.sort(reverse=True)
print('commits with any orphaning event:', len(rows), 'of', len(d))
for n, r, dt, c in rows[:15]:
    s = subprocess.run(['git', '-C', 'C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297', 'log', '-1', '--format=%s', r], capture_output=True, text=True).stdout.strip()[:90]
    print(n, r, dt, c, s)
PYEOF
````

25. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && python3 - <<'PYEOF'
import json
d = json.load(open('commits.json'))
for u in d:
    if u['rev'] in ('9ae1d023e', 'b61ec1c49', '817ce1890', 'c52df6ada', '7f79393d7', '5b00666a2'):
        print('==', u['rev'])
        for e in u['events']:
            if e['type'] in ('retire', 'merge', 'split', 'split_off'):
                print('  ', e['type'], e['old'], '->', e.get('new') or e.get('split_into'))
        print('   added:', [e['new'][1][:40] for e in u['events'] if e['type'] == 'add'][:30])
PYEOF
````

26. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && cat > model.py <<'PYEOF'
"""Adopter model. usage: model.py X.json
An adopter amended k units of the base (the parent of each update). Per update:
  conflict = an amended unit's text changed while its anchor held (kept/split_off with an edit)
  orphan   = an amended unit's anchor is gone: anchor rename, move, split, merge, retire
             (orphan+fr also counts an in-set file rename, which a per-file key does not follow)
uniform: exact hypergeometric.  weighted: P(pick) ~ lineage text-edit count over the whole history
(0.05 floor), sampled without replacement by Efraimidis-Spirakis keys, 4000 draws per update."""
import json, sys, random, math
from collections import defaultdict
data = json.load(open(sys.argv[1]))
random.seed(7)
par = {}
def find(x):
    while par.get(x, x) != x:
        par[x] = par.get(par[x], par[x]); x = par[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb: par[ra] = rb
edits = defaultdict(int)
per_update = []
for u in data:
    conf, orph, orph_fr = set(), set(), set()
    for e in u['events']:
        if not e['old']: continue
        ok = tuple(e['old'])
        t = e['type']
        if t in ('kept', 'split_off'):
            union(ok, tuple(e['new']))
            if e['edit']:
                conf.add(ok)
            if e['rename'] or e['move'] or t == 'split_off' and False:
                orph.add(ok)
            if e['rename'] or e['move'] or e['file_rename']:
                orph_fr.add(ok)
        else:
            orph.add(ok); orph_fr.add(ok)
            if t == 'merge': union(ok, tuple(e['new']))
    per_update.append((u, conf, orph, orph_fr))
for u, conf, orph, orph_fr in per_update:
    for k in conf: edits[find(k)] += 1
def p_uniform(N, m, k):
    if m == 0: return 0.0
    if N - m < k: return 1.0
    return 1 - math.exp(math.lgamma(N-m+1) - math.lgamma(N-m-k+1) - math.lgamma(N+1) + math.lgamma(N-k+1))
def p_weighted(keys, hit, k, R=4000):
    w = [max(edits[find(x)], 0.05) for x in keys]
    hits = [x in hit for x in keys]
    if not any(hits): return 0.0
    n = 0
    lw = [math.log(x) for x in w]
    for _ in range(R):
        top = sorted(range(len(keys)), key=lambda i: math.log(random.random()) / w[i], reverse=True)[:k]
        n += any(hits[i] for i in top)
    return n / R
for k in (5, 20):
    acc = defaultdict(float); cnt = 0
    for u, conf, orph, orph_fr in per_update:
        keys = [tuple(x[:2]) for x in u['base_keys']]
        N = len(keys)
        conf_b = conf & set(keys); orph_b = orph & set(keys); fr_b = orph_fr & set(keys)
        acc['uni_conf'] += p_uniform(N, len(conf_b), k)
        acc['uni_orph'] += p_uniform(N, len(orph_b), k)
        acc['uni_orph_fr'] += p_uniform(N, len(fr_b), k)
        acc['w_conf'] += p_weighted(keys, conf_b, k)
        acc['w_orph'] += p_weighted(keys, orph_b, k)
        acc['w_orph_fr'] += p_weighted(keys, fr_b, k)
        acc['N'] += N; cnt += 1
    print('k=%-2d  updates=%d mean base units=%.0f' % (k, cnt, acc['N'] / cnt))
    print('   uniform : P(conflict)=%.3f  P(orphan)=%.4f  P(orphan, file renames counted)=%.4f' % (acc['uni_conf']/cnt, acc['uni_orph']/cnt, acc['uni_orph_fr']/cnt))
    print('   weighted: P(conflict)=%.3f  P(orphan)=%.4f  P(orphan, file renames counted)=%.4f' % (acc['w_conf']/cnt, acc['w_orph']/cnt, acc['w_orph_fr']/cnt))
hot = sorted(((v, k) for k, v in edits.items()), reverse=True)[:8]
print('hottest lineages (text edits):', [(v, k[0].split('/')[-1], k[1][:30]) for v, k in hot])
zero = sum(1 for u in [per_update[-1][0]] for x in u['base_keys'] if edits[find(tuple(x[:2]))] == 0)
print('units in the last base never text-edited:', zero, 'of', len(per_update[-1][0]['base_keys']))
PYEOF
python3 model.py landings.json
````

27. Bash

````text
sed -n 1,14p tools/memory-tree/HYGIENE.template.md | cut -c1-200; echo; sed -n 1,6p tools/unattended/PROTOCOL.template.md | cut -c1-200
````

28. Bash

````text
grep -hn '^<!-- gov:' coding-governance-agents.template.md tools/*/*.template.md tools/roles/agents/*.md skills/*/SKILL.md | cut -c1-120 | sort | uniq -c | sort -rn | head; git log -p -3 --format=%h -- coding-governance-agents.template.md | grep '^[-+]' | grep -i 'v4\.\|version' | head
````

29. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && python3 - <<'PYEOF'
s = open('seg.py').read()
s = s.replace("FENCE = re.compile(r'^\\s*(```|~~~)')",
 "FENCE = re.compile(r'^\\s*(```|~~~)')\nSTAMP = re.compile(r'^\\s*<!-- (gov:kit |governance-template)')   # machine version stamps: not instructions")
s = s.replace("    for ln in lines[i:]:\n        if FENCE.match(ln):",
 "    for ln in lines[i:]:\n        if STAMP.match(ln):\n            continue\n        if FENCE.match(ln):")
open('seg.py', 'w').write(s)
PYEOF
grep -n 'STAMP' seg.py; cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python3 "$(cygpath -m /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors)/count.py" | tail -7
````

30. Bash

````text
S="$(cygpath -m /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors)"; python3 "$S/walk.py" landings "$S/landings.json" && python3 "$S/walk.py" commits "$S/commits.json" && cd "$S" && for m in commits landings; do echo "== $m"; python3 table.py $m.json; done
````

31. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && echo "== landings"; python3 model.py landings.json; echo "== commits"; python3 model.py commits.json
````

32. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && cat > retire_probe.py <<'PYEOF'
"""For each retire event: does its content survive in the commit's new side? (max word ratio to any
new unit; sum of shingle containment over new units). usage: retire_probe.py X.json"""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from walk import units_of, ratio, contain, changes
data = json.load(open(sys.argv[1]))
full = {u['rev']: u for u in data}
import subprocess
buckets = {'survives (containment sum >= 0.3)': 0, 'partly (0.1-0.3)': 0, 'gone (< 0.1)': 0}
rows = []
for u in data:
    rets = [e for e in u['events'] if e['type'] == 'retire']
    if not rets: continue
    revfull = subprocess.run(['git', 'rev-parse', u['rev']], capture_output=True, text=True).stdout.strip()
    parfull = subprocess.run(['git', 'rev-parse', u['parent']], capture_output=True, text=True).stdout.strip()
    newu = []
    for st, o, n in changes(parfull, revfull):
        if n: newu += [b for a, k, b in units_of(revfull, n)]
    for e in rets:
        ob = [b for a, k, b in units_of(parfull, e['old'][0]) if a == e['old'][1]][0]
        cs = sum(contain(ob, nb) for nb in newu)
        br = max([ratio(ob, nb) for nb in newu] or [0])
        b = 'survives (containment sum >= 0.3)' if cs >= 0.3 else 'partly (0.1-0.3)' if cs >= 0.1 else 'gone (< 0.1)'
        buckets[b] += 1
        rows.append((u['rev'], e['old'][0].split('/')[-1], e['old'][1][:45], round(cs, 2), round(br, 2)))
print(buckets)
for r in rows: print(r)
PYEOF
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python3 "$(cygpath -m /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors)/retire_probe.py" "$(cygpath -m /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors)/commits.json"
````

33. Bash

````text
git show b61ec1c49 -- tools/roles/agents/gov-builder.agent.md | grep '^[-+]' | head -12 | cut -c1-200; git log -1 --format=%ad --date=short 9ae1d023e; git log --format='%h %ad' --date=short 9ae1d023e..HEAD -- coding-governance-agents.template.md | wc -l
````

34. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && cat > schemes.py <<'PYEOF'
"""Losing tests for the four anchoring schemes, from the walk's events. usage: schemes.py X.json"""
import json, sys, statistics as st
data = json.load(open(sys.argv[1]))
A = dict(edits=0, edits_held=0, repurposed=0, rename_body_survived=0, rename_body_identical=0,
         reflow_only=0, placeholder_only=0, orphan_total=0, small_edit=0, kept_units_touched=0,
         pos_shift=0, pos_wrong_live=0, tag_events=0, tag_edits=0, tag_orphans=0)
changed_frac = []
renames = []
for u in data:
    for e in u['events']:
        if not e['old']: continue
        t = e['type']
        if e['kind'] == 'tag':
            A['tag_events'] += 1
        if t in ('kept', 'split_off'):
            A['kept_units_touched'] += 1
            if e['edit']:
                A['edits'] += 1
                changed_frac.append(1 - e['sim'])
                if e['sim'] >= 0.9: A['small_edit'] += 1
                if e['kind'] == 'tag': A['tag_edits'] += 1
            if e['edit'] and not e['rename'] and not e['move']:
                A['edits_held'] += 1
                if e['sim'] < 0.3: A['repurposed'] += 1
            if e.get('reflow_only'): A['reflow_only'] += 1
            if e.get('placeholder_only'): A['placeholder_only'] += 1
            if e['rename'] or e['move']:
                A['rename_body_survived'] += 1
                if not e['edit']: A['rename_body_identical'] += 1
                renames.append((u['rev'], e['old'][1][:50], e['new'][1][:50], e['sim']))
                if e['kind'] == 'tag': A['tag_orphans'] += 1
            if e['ordinal_moved'] or e['old'][0] != e['new'][0]:
                A['pos_shift'] += 1
        else:
            A['orphan_total'] += 1
            if e['kind'] == 'tag': A['tag_orphans'] += 1
for k, v in A.items(): print('%-22s %d' % (k, v))
print('orphans incl. renames/moves:', A['orphan_total'] + A['rename_body_survived'])
print('edit size, fraction of unit words changed: median %.3f  p75 %.3f  share of edits changing <10%%: %.2f'
      % (st.median(changed_frac), st.quantiles(changed_frac, n=4)[2], A['small_edit'] / A['edits']))
print('position: kept units whose (file, ordinal) changed: %d of %d kept-in-touched-file (%.3f)'
      % (A['pos_shift'], A['kept_units_touched'], A['pos_shift'] / A['kept_units_touched']))
print('anchor renames/moves (body >= 0.6 similar):')
for r in renames: print('  ', r)
PYEOF
python3 schemes.py landings.json; echo; python3 schemes.py commits.json | head -22
````

35. Bash

````text
git log --format='%h %ad %s' --date=short 9ae1d023e^..HEAD -- coding-governance-agents.template.md | cut -c1-110; echo; git log -p --format='@@@ %h' 9ae1d023e..HEAD -- coding-governance-agents.template.md | grep -E '^@@@|^[-+]- \[[a-z0-9-]+\]' | sed -E 's/^([-+]- \[[a-z0-9-]+\]).*/\1/' | uniq | head -60
````

36. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && cat > simtest.py <<'PYEOF'
"""Content-similarity anchoring, two losing tests.
T1 (history): for every unit gov text-edited while its anchor held (ground truth = anchor identity, M1),
   re-find it by best word-ratio among the new units of the files the update touched.
   wrong = best match is another unit; lost = best ratio < 0.6 (the matcher's own threshold).
T2 (static, HEAD): near-duplicates -- units whose best ratio to ANOTHER unit is >= 0.8, globally and
   within the same file. usage: simtest.py X.json"""
import json, sys, os, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from walk import units_of, ratio, changes, _blob
from seg import group_of, segment
data = json.load(open(sys.argv[1]))
def full(r): return subprocess.run(['git', 'rev-parse', r], capture_output=True, text=True).stdout.strip()
n = wrong = lost = 0
wrong_rows = []
for u in data:
    held = [e for e in u['events'] if e['type'] in ('kept', 'split_off') and e['edit'] and not e['rename'] and not e['move']]
    if not held: continue
    rv, pr = full(u['rev']), full(u['parent'])
    newu = []
    for st, o, nn in changes(pr, rv):
        if nn: newu += [(nn, a, b) for a, k, b in units_of(rv, nn)]
    for e in held:
        ob = [b for a, k, b in units_of(pr, e['old'][0]) if a == e['old'][1]][0]
        best = max(newu, key=lambda x: ratio(ob, x[2]))
        br = ratio(ob, best[2])
        n += 1
        if [best[0], best[1]] != e['new']:
            wrong += 1; wrong_rows.append((u['rev'], e['old'][1][:40], '->', best[1][:40], round(br, 2), e['sim']))
        elif br < 0.6:
            lost += 1
    _blob.clear()
print('T1 edited-with-anchor-held units: %d  wrong re-find: %d  lost (<0.6): %d' % (n, wrong, lost))
for r in wrong_rows[:12]: print('   ', r)
files = [p for p in subprocess.run(['git', 'ls-files'], capture_output=True, text=True).stdout.split() if group_of(p)]
U = []
for p in files:
    U += [(p, a, b) for a, k, b in segment(open(p, encoding='utf-8').read())]
glob = same = 0
ex = []
for i, x in enumerate(U):
    bg = bs = 0
    for j, y in enumerate(U):
        if i == j: continue
        if abs(len(x[2]) - len(y[2])) > 0.5 * max(len(x[2]), len(y[2])): continue
        r = ratio(x[2], y[2])
        bg = max(bg, r)
        if y[0] == x[0]: bs = max(bs, r)
    glob += bg >= 0.8; same += bs >= 0.8
    if bg >= 0.8 and len(ex) < 6: ex.append((x[0].split('/')[-1], x[1], x[2][:40]))
print('T2 HEAD units: %d  near-duplicate of another unit (>=0.8): globally %d, within its own file %d' % (len(U), glob, same))
for r in ex: print('   ', r)
PYEOF
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && time python3 "$(cygpath -m /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors)/simtest.py" "$(cygpath -m /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors)/landings.json"
````

37. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && cat > windows.py <<'PYEOF'
"""Write window slices of a walk: since a date, and weekly pulls (ISO week; events concatenated,
base = the week's first base). usage: windows.py X.json"""
import json, sys, datetime
d = json.load(open(sys.argv[1]))
stem = sys.argv[1][:-5]
json.dump([u for u in d if u['date'] >= '2026-09-19'], open(stem + '-last30.json', 'w'))
json.dump([u for u in d if u['date'] >= '2026-10-09'], open(stem + '-tagera.json', 'w'))
wk = {}
for u in d:
    y, w, _ = datetime.date.fromisoformat(u['date']).isocalendar()
    k = (y, w)
    if k not in wk:
        wk[k] = dict(rev=u['rev'], parent=u['parent'], date=u['date'], file_renames=0, events=[], base_keys=u['base_keys'])
    wk[k]['events'] += u['events']; wk[k]['file_renames'] += u['file_renames']
json.dump(list(wk.values()), open(stem + '-weekly.json', 'w'))
print('weeks', len(wk))
PYEOF
python3 windows.py landings.json && for w in last30 tagera weekly; do echo "== landings-$w"; python3 model.py landings-$w.json | grep -v hottest; done
````

38. Bash

````text
python3 - <<EOF
import sys, subprocess, statistics as st
sys.path.insert(0, r"$(cygpath -m /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors)")
from seg import group_of, segment
U=[]
for p in subprocess.run(['git','ls-files'],capture_output=True,text=True).stdout.split():
    g=group_of(p)
    if g: U+=[(len(b.split()),g,p.split('/')[-1],a[:40]) for a,k,b in segment(open(p,encoding='utf-8').read())]
w=[u[0] for u in U]
print('units',len(U),'words median',st.median(w),'p90',sorted(w)[int(.9*len(w))],'max',max(w))
for u in sorted(U,reverse=True)[:6]: print(u)
for g in ['charter','guides','hygiene+spec','roles','skills']:
    x=[u[0] for u in U if u[1]==g]; print(g,'median',st.median(x),'max',max(x))
EOF
````

39. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && cat > sizes.py <<'PYEOF'
import sys, os, subprocess, statistics as st
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seg import group_of, segment
U = []
for p in subprocess.run(['git', 'ls-files'], capture_output=True, text=True).stdout.split():
    g = group_of(p)
    if g: U += [(len(b.split()), g, p.split('/')[-1], a[:40]) for a, k, b in segment(open(p, encoding='utf-8').read())]
w = [u[0] for u in U]
print('units', len(U), 'words median', st.median(w), 'p90', sorted(w)[int(.9 * len(w))], 'max', max(w))
for u in sorted(U, reverse=True)[:5]: print('  ', u)
for g in ['charter', 'guides', 'hygiene+spec', 'roles', 'skills']:
    x = [u[0] for u in U if u[1] == g]; print('  ', g, 'median', st.median(x), 'max', max(x))
PYEOF
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python3 "$(cygpath -m /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors)/sizes.py"
````

40. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/anchors && cat > bykind.py <<'PYEOF'
import json, sys
from collections import Counter
d = json.load(open(sys.argv[1])); occ = Counter(); ed = Counter(); orp = Counter()
for u in d:
    for e in u['events']:
        if not e['old']: continue
        k = e['kind']; occ[k] += 1
        if e['type'] in ('kept', 'split_off'):
            ed[k] += e['edit']; orp[k] += bool(e['rename'] or e['move'])
        else: orp[k] += 1
for k in occ: print('%-9s unit-in-touched-file %5d  edited %4d (%.3f)  orphaned %3d (%.4f)' % (k, occ[k], ed[k], ed[k]/occ[k], orp[k], orp[k]/occ[k]))
PYEOF
python3 bykind.py landings.json
````

41. Bash

````text
grep -n "house" tools/roles/render_agents.py | head -15; grep -n "ADOPTER_RULES" -r tools/playbook/*.py | head -5
````

42. Bash

````text
cd /c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad && rm -rf anchors && ls -d anchors 2>&1; cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && git status --short
````
