# Research instruments: flow and roles adoption, three passes

**Serves:** research PLAY-dClosedLoop-1

Each pass's shell commands, written files, web queries and pages read, taken in order from its transcript, so nothing is retyped. The passes shared the session scratch directory, so a file there may hold another pass's content; these are what each pass sent. Reads of the tree (Read, Grep, Glob) are left out, as the retrofit pass's instruments left them out. The returns are `build/2026-10-19-build-PLAY-dClosedLoop-1-research-flow-today.md`, `-research-flow-design.md` and `-research-flow-prior-art.md`.

## [flow-today] Dispatch 123: today's product, measured on a scratch install

1. Bash

````text
ls tools/ && ls tools/*/kit.toml && wc -l tools/govkit/govkit.py memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-research-adopter-today.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-adopter-instructions.md
````

2. Bash

````text
for k in roles workflows unattended run-gates playbook gate-lint hooks agent-instructions; do echo "=== $k"; cat tools/$k/kit.toml; done
````

3. Bash

````text
wc -l tools/*/kit.toml && grep -v '^\s*#' tools/roles/kit.toml | grep -v '^\s*$'
````

4. Bash

````text
for k in workflows unattended run-gates; do echo "=== $k"; grep -v '^\s*#' tools/$k/kit.toml | grep -v '^\s*$'; done; ls tools/workflows tools/roles tools/roles/house tools/roles/agents tools/unattended tools/run-gates
````

5. Bash

````text
grep -n "add_parser\|sub.add_parser\|subparsers" tools/govkit/govkit.py | head -40; grep -n "gate-legs.json\|gate_legs\b\|project_legs\|adopter_legs\|\[\[gate_leg\]\]\|own_legs\|extra_legs" tools/govkit/govkit.py | head -60
````

6. Bash

````text
bash tools/lib/resolve-python.sh 2>/dev/null; echo; grep -n "def main\|argparse\|\"plan\"\|\"update\"\|\"apply\"\|\"intake\"" tools/govkit/govkit.py | head -30; git log --oneline -1; git log --oneline | wc -l
````

7. Bash

````text
cat /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/lib/resolve-python.sh | head -40; which python python3 py 2>&1
````

8. Bash

````text
python3 tools/govkit/govkit.py --help 2>&1 | head -80
````

9. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; mkdir -p "$S" && cd "$S" && rm -rf fx && mkdir fx && cd fx && git clone -q /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 gov 2>&1 | tail -2; git -C gov log --oneline -1; mkdir t1 && cd t1 && git init -q && git config user.email t@t && git config user.name t && echo "# t1" > README.md && git add . && git commit -qm init && echo ok
````

10. Bash

````text
git config --global core.autocrlf; S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && python3 $S/gov/tools/govkit/govkit.py intake --target . --all 2>&1 | tail -40
````

11. Bash

````text
grep -rn "gate_file\|manifest_path\|playbook_path\|user_skills" tools/*/kit.toml skills/session-kickoff/kit.toml 2>/dev/null | head -20; ls skills/session-kickoff; cat .governance/deploy.toml | head -60
````

12. Bash

````text
grep -n -B3 -A8 "gate_file\|^\[\[ask\]\]\|asked" tools/codebase-map/kit.toml | head -50; grep -rn "playbook_path" tools/playbook/kit.toml tools/govkit/*.toml 2>/dev/null | head
````

13. Bash

````text
ls tools/govkit/; grep -n "gate_file\|playbook_path\|user_skills\|manifest_path" tools/govkit/registry.toml 2>/dev/null | head -20
````

14. Bash

````text
ls tools/govkit/entries; grep -rn "gate_file\|playbook_path\|user_skills\|manifest_path" tools/govkit/entries tools/govkit/registry.toml | head -20
````

15. Bash

````text
sed -n 1,100p tools/codebase-map/kit.toml | grep -v "^#" | grep -v '^\s*$' | head -50
````

16. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; mkdir -p $S/userskills; cd $S/t1 && git config core.autocrlf false && python3 $S/gov/tools/govkit/govkit.py intake --target . --all --answer gate_file=tests/test_codebase_map.py --answer manifest_path=memory/guides/SESSION-KICKOFF.md --answer playbook_path=coding-governance-agents.template.md --answer "user_skills=$S/userskills" 2>&1 | tail -30; ls -a; ls .governance; 
````

17. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && python3 $S/gov/tools/govkit/govkit.py plan --target . --all > $S/plan.txt 2>&1; echo "exit $?"; wc -l $S/plan.txt; tail -15 $S/plan.txt; head -40 $S/plan.txt
````

18. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; grep -E "<- (roles|review-harness|unattended|run-gates|agent-cap|kickoff-manifest|playbook|playbook-render|settings-merge)$" $S/plan.txt | grep -v -E "\[(attributes|project-owned)" | grep -v -E "README|\.test\.|fixture|selftest"
````

19. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; grep -n -E "gate-legs|BUILD-METHOD|\.conf|roles\.json|agents|gate_runner|legs|settings" $S/plan.txt | grep -v "roles/agents/" | head -40
````

20. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && git add -A && git commit -qm intake && timeout 900 python3 $S/gov/tools/govkit/govkit.py apply --target . --all > $S/apply1.txt 2>&1; echo "exit $?"; grep -v "^  write\|^  ORDER\|^  SIDE" $S/apply1.txt | tail -60
````

21. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && git status --short | head -20; ls .claude .claude/agents 2>&1 | head; ls memory/guides; ls .governance; grep -n "adopter exited\|adopt  \|CONFIGURE\|roles" $S/apply1.txt | grep -v "^.*write " | head -30
````

22. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; grep -n -i -E "memory-tree|render-playbook|REFUSED|roles|governing|seed" $S/apply1.txt | grep -v -E "^\S+\s+(write|ORDER|SIDE)|  write|SKIPPED|pin '" | head -30; ls -a $S/t1
````

23. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && cat .memory-tree.conf | grep -v "^#" | grep -v '^$'; grep -A3 "^\[adopt\]" tools/memory-tree/kit.toml; grep -A3 "^\[adopt\]" tools/playbook/kit.toml
````

24. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && bash tools/memory-tree/adopt-memory-tree.sh --scaffold 2>&1 | tail -8; echo "mt exit ${PIPESTATUS[0]}"; bash tools/playbook/adopt-playbook.sh --target . 2>&1 | tail -8; echo "pb exit ${PIPESTATUS[0]}"
````

25. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && cp memory/guides/SESSION-KICKOFF.md $S/sk.md && rm -rf memory && bash tools/memory-tree/adopt-memory-tree.sh --scaffold 2>&1 | tail -4; echo "mt exit ${PIPESTATUS[0]}"; cp $S/sk.md memory/guides/SESSION-KICKOFF.md; sed -n '/^\[answers\]/,$p' .governance/deploy.toml
````

26. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && python3 - <<'EOF'
p='.governance/deploy.toml'
s=open(p,encoding='utf-8').read()
s=s.replace('[answers]\n','[answers]\nci_file = "none yet"\nproject_name = "t1"\n',1)
s=s.replace('[gate_runner]','[charter]\nadopter_rules = """\nADOPTER-RULE-ONE: every change names its ticket.\n"""\n\n[gate_runner]',1)
open(p,'w',encoding='utf-8',newline='\n').write(s)
EOF
for i in 1 2 3 4 5 6; do out=$(bash tools/playbook/adopt-playbook.sh --target . 2>&1); rc=$?; echo "$out" | tail -3; echo "pb exit $rc"; [ $rc = 0 ] && break; key=$(echo "$out" | grep -oE "probe \`[a-z_]+\`|answer '?[a-z_]+'?" | head -1); echo "KEY: $key"; break; done
````

27. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && sed -n 15,30p .governance/deploy.toml
````

28. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && python3 - <<'EOF'
p='.governance/deploy.toml'
s=open(p,encoding='utf-8').read()
s=s.replace('# [charter]\nadopter_rules','[charter]\nadopter_rules',1)
s=s.replace('"""\n\n[gate_runner] — emitted','"""\n\n# [gate_runner] — emitted',1)
open(p,'w',encoding='utf-8',newline='\n').write(s)
EOF
python3 -c "import tomllib;d=tomllib.load(open('.governance/deploy.toml','rb'));print(list(d))"; bash tools/playbook/adopt-playbook.sh --target . 2>&1 | tail -4
````

29. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && for i in $(seq 1 20); do out=$(bash tools/playbook/adopt-playbook.sh --target . 2>&1); rc=$?; if [ $rc = 0 ]; then echo "$out" | tail -3; echo OK; break; fi; k=$(echo "$out" | grep -oE "REFUSED — [A-Z_]+ is (an ASKED|derived)" | awk '{print $3}'); [ -z "$k" ] && { echo "$out" | tail -4; break; }; lk=$(echo $k | tr A-Z a-z); echo "add $lk"; python3 - "$lk" <<'EOF'
import sys
p='.governance/deploy.toml'; k=sys.argv[1]
s=open(p,encoding='utf-8').read()
s=s.replace('[answers]\n',f'[answers]\n{k} = "fixture value for {k}"\n',1)
open(p,'w',encoding='utf-8',newline='\n').write(s)
EOF
done
````

30. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && sed -i 's/^ADOPTER-RULE-ONE/- ADOPTER-RULE-ONE/' .governance/deploy.toml && bash tools/playbook/adopt-playbook.sh --target . 2>&1 | tail -3; echo "rc ${PIPESTATUS[0]}"; ls; bash tools/agent-instructions/adopt-agent-instructions.sh 2>&1 | tail -3; grep -A2 "^\[adopt\]" tools/agent-instructions/kit.toml
````

31. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && git add -A >/dev/null 2>&1; bash tools/roles/adopt-roles.sh --scaffold 2>&1 | tail -6; echo "roles rc ${PIPESTATUS[0]}"; ls .claude/agents .claude 2>&1
````

32. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && grep -v '^\s*#' tools/unattended/.unattended.conf.example | grep -v '^\s*$'; echo ----; grep -v '^\s*#' /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/.unattended.conf | grep -v '^\s*$'
````

33. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && sed -e 's#{{TOOL_ROOT}}#tools/#g' -e 's#<your-schedule-create-tool>#CronCreate#' -e 's#<your-schedule-delete-tool>#CronDelete#' -e 's#<e.g. every 10 minutes (cron 3-59/10 \* \* \* \*)>#every 10 minutes#' -e 's#<your-durable-schedule-create-tool>#create_scheduled_task#' -e 's#<your-durable-schedule-delete-tool>#delete_scheduled_task#' tools/unattended/.unattended.conf.example > .unattended.conf; grep -n "<" .unattended.conf | grep -v "^\S*#" | head; bash tools/unattended/adopt-unattended.sh 2>&1 | tail -5; echo "un rc ${PIPESTATUS[0]}"; bash tools/review-harness/check-protocol-parity.test.sh --render 2>&1 | tail -5; echo "rh rc ${PIPESTATUS[0]}"
````

34. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && git add -A && git commit -qm "install" --no-verify && python3 $S/gov/tools/govkit/govkit.py update --target . > $S/up0.txt 2>&1; echo "rc $?"; grep -v "unchanged\|^  ok\b" $S/up0.txt | tail -40; wc -l $S/up0.txt
````

35. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && python3 -c "
import json;l=json.load(open('tools/gate-legs.json'));print(len(l));print(sorted(set(k for r in l for k in r)))
r=json.load(open('.governance/install.json'));print(list(r));print(len(r['gate_runner']['emitted']))"; grep -n "patched\|re-rendered\|role-moved\|generated" $S/up0.txt | head -40
````

36. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles && wc -l *.py *.toml house/policy.toml; cat house/policy.toml; grep -n "house\|policy\|glob\|agents_dir\|AGENTS_DIR\|workflows.toml\|\.agent\.md" roles_lib.py | head -60
````

37. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles && cat workflows.toml; sed -n 1,80p check_roles.py
````

38. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles && grep -n -i "ceiling\|WORKFLOW_NAMES\|TEN\b\|\"orient\"\|DRIVERS\|WRITE_FOLDERS\s*=\|gov-" check_roles.py roles_lib.py | head -40
````

39. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/workflows && wc -l *.js *.template.js; grep -n "args\.\|lens\|LENS\|FANOUT_CAP\|effort\|roles\b\|agentType\|subagent_type" tier2-review.template.js | head -60
````

40. Bash

````text
grep -n "const LENSES\|LIGHT_LENSES =\|SPEC_LENSES\|DIFF_LENSES\|key: '" tools/workflows/tier2-review.template.js | head -30; grep -rn "lensNotes\|checklist" tools/roles/handoff.py tools/workflows/REVIEW-PROTOCOL.template.md tools/roles/SKILL.template.md tools/unattended/*.template.md 2>/dev/null | head -20
````

41. Bash

````text
sed -n 755,775p tools/unattended/VERBS.template.md; grep -rn "bug-class\|bug_class\|checklist" tools/memory-tree/kit.toml | head; ls tools/memory-tree | head -80
````

42. Bash

````text
sed -n 1,40p tools/memory-tree/gotchas.py | head -50; grep -n "checklist\|lensNotes" tools/workflows/unattended-build.template.js | head -12
````

43. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/unattended && grep -n "PHASES_EXTRA\|DOD_EXTRA\|DIRECTIVES_EXTRA\|HALT_CODES_EXTRA\|HOLD_CODES_EXTRA\|LANDING_NODES\|REVIEW_ROUNDS\|SPEC_AUDIT_DEFAULT" .unattended.conf.example | head -30
````

44. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/unattended && sed -n 100,120p .unattended.conf.example; sed -n 240,300p .unattended.conf.example; sed -n 340,400p .unattended.conf.example; sed -n 430,455p .unattended.conf.example
````

45. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/unattended && grep -n "PHASES_EXTRA\|DOD_EXTRA\|PHASES_CORE\|DOD_CORE" unattended.sh lib-unattended.sh check-unattended.sh adopt-unattended.sh | head -25
````

46. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/unattended && sed -n 838,870p unattended.sh; grep -n "phases)\|\$(phases)\|dod)\b\|\$(dod)" unattended.sh | head -15
````

47. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/unattended && sed -n 10755,10800p unattended.sh; sed -n 5995,6012p unattended.sh
````

48. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/unattended && n=$(grep -n "^dod_met()" unattended.sh | cut -d: -f1); echo $n; awk -v s=$n 'NR>=s && NR<=s+600' unattended.sh | grep -n "^\s*\*)\|agent)\|case \"\$item\"\|case \"\$ck\"" | head -20
````

49. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/unattended && sed -n 10957,10966p unattended.sh; awk 'NR>10963 && NR<12000 && /^    \*\)|^    \*\) /{print NR": "$0}' unattended.sh | head; grep -n "an EXTRA item\|extra DoD\|DOD_EXTRA item\|project item" unattended.sh | head
````

50. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/unattended && awk 'NR>10963 && NR<12600' unattended.sh | grep -n "^    \*)" | head; awk 'NR>10963 && NR<12600 && /^  esac/{print NR; exit}' unattended.sh
````

51. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/unattended && awk 'NR>10963 && NR<12600 && /^    \*/{print NR": "$0}' unattended.sh | head
````

52. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/unattended && sed -n 12225,12240p unattended.sh
````

53. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/run-gates && grep -o "GATE_[A-Z_]*" run-gates.sh | sort | uniq -c | sort -rn | head -40; grep -v "^#" gate-profiles.txt | head -20
````

54. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/run-gates && grep -n "windows-only-legs\|WINDOWS_ONLY\|held-legs\|HELD_LEGS\|skip a leg\|GATE_SKIP\|exempt" run-gates.sh | head -15; head -30 windows-only-legs.txt
````

55. Bash

````text
grep -rln -i "autonomy\|attended\b\|ATTENDANCE\|attendance" tools --include=*.sh --include=*.py --include=*.toml --include=*.js --include=*.conf* | head -20; grep -n "{{[A-Z_]*}}" tools/memory-tree/BUILD-METHOD.template.md | grep -o "{{[A-Z_]*}}" | sort | uniq -c
````

56. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cp -r $S/t1 $S/t2; cd $S/t1 && grep -n "trigger = \"before a new behaviour\|^gov-builder\|modest" tools/roles/workflows.toml tools/roles/house/policy.toml tools/run-gates/gate-profiles.txt; grep -n "key: 'intent'" -A6 tools/review-harness/tier2-review.template.js; python3 -c "
import json;l=json.load(open('tools/gate-legs.json'));[print(json.dumps(r)) for r in l if r['name'] in ('roles catalogue','roles render wiring','review-join ban (no ref-keyed join)')]"
````

57. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && python3 tools/roles/check_roles.py 2>&1 | tail -4; echo "rc ${PIPESTATUS[0]}"; bash tools/roles/adopt-roles.sh --check 2>&1 | tail -3; echo "rc ${PIPESTATUS[0]}"
````

58. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && \
sed -i 's/when kickoff asks for a scout"/when kickoff asks for a scout ADOPTER-WF-TRIGGER"/' tools/roles/workflows.toml && \
sed -i '12s/gov-builder = "xhigh"/gov-builder = "low"            # ADOPTER-POLICY/' tools/roles/house/policy.toml && \
echo "- ADOPTER-HOUSE-SPECWRITER: cite the ticket id in every spec." > tools/roles/house/gov-spec-writer.md && \
sed -i '127s/width=4/width=3/' tools/run-gates/gate-profiles.txt && \
python3 - <<'EOF'
import re
p='tools/review-harness/tier2-review.template.js'
s=open(p,encoding='utf-8').read()
s=s.replace("""scope beyond what was asked.',
  },
]""","""scope beyond what was asked.',
  },
  {
    key: 'acme-privacy',
    brief: 'ADOPTER-LENS: does the diff log personal data?',
  },
]""",1)
open(p,'w',encoding='utf-8',newline='\n').write(s)
import json
p='tools/gate-legs.json'
l=json.load(open(p,encoding='utf-8'))
for r in l:
    if r['name']=='roles catalogue': r['argv']=r['argv']+['--root','.']
    if r['name']=='roles render wiring': r['ceiling']=999
l=[r for r in l if r['name']!='review-join ban (no ref-keyed join)']
l.append({"name":"acme own leg","argv":["bash","-c","echo ADOPTER-LEG"],"subject":"repo"})
open(p,'w',encoding='utf-8',newline='\n').write(json.dumps(l,indent=2,ensure_ascii=False)+"\n")
EOF
echo "// ADOPTER-RENDERED-HARNESS" >> tools/review-harness/tier2-review.js && \
sed -i 's/^PHASES_EXTRA=""/PHASES_EXTRA="ACMEQA"/; s/^DOD_EXTRA=""/DOD_EXTRA="acme-signoff:agent"/' .unattended.conf && \
python3 - <<'EOF'
import json
p='.claude/roles.json'; d=json.load(open(p,encoding='utf-8')); print(type(d), list(d)[:5] if isinstance(d,dict) else len(d))
EOF
git diff --stat
````

59. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && cat tools/roles/agents/gov-researcher.agent.md | head -20; python3 -c "
import json;d=json.load(open('.claude/roles.json'));print(json.dumps(d['gates']));print(json.dumps(d['harnesses'])[:600]);print(list(d['roles'])[:3], json.dumps(d['roles']['gov-builder'])[:400])"
````

60. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && sed -e 's/^name: gov-researcher/name: acme-auditor/' -e 's/^description: .*/description: ADOPTER-ROLE audits privacy./' tools/roles/agents/gov-researcher.agent.md > tools/roles/agents/acme-auditor.agent.md && echo "- ADOPTER-HOUSE-ACME: name the data class." > tools/roles/house/acme-auditor.md && bash tools/roles/adopt-roles.sh --scaffold 2>&1 | tail -8; echo "rc ${PIPESTATUS[0]}"
````

61. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && head -12 .claude/agents/acme-auditor.md; grep -n "ADOPTER\|House rules" .claude/agents/*.md; grep -n "^effort" .claude/agents/gov-builder.md; python3 -c "
import json;d=json.load(open('.claude/roles.json'));print(json.dumps(d['roles'].get('acme-auditor')))"; grep -n "render wiring\|--check" tools/roles/adopt-roles.sh | head
````

62. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && git add -A && git commit -qm "adopter customizations" --no-verify && git log --oneline | head -3; cd $S/gov && git config user.email g@g && git config user.name g && git config core.autocrlf false && grep -n 'trigger = "any time a design must choose' tools/roles/workflows.toml && grep -n "Resume', detail" tools/workflows/tier2-review.template.js && sed -n 120,126p tools/run-gates/gate-profiles.txt | cat -A | cut -c1-80 && grep -n "^gov-builder = \"xhigh\"\|^default" tools/roles/house/policy.toml
````

63. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/gov && \
sed -i '87s/seam decides"/seam decides GOV-V2-RESEARCH"/' tools/roles/workflows.toml && \
sed -i "9s/carries the key is reused'/carries the key is reused GOV-V2-RESUME'/" tools/workflows/tier2-review.template.js && \
sed -i '12s/gov-builder = "xhigh"/gov-builder = "max"/; 6s/every role and stage this file does not name/every role and stage this file does not name (GOV-V2-SEED)/' tools/roles/house/policy.toml && \
sed -i 's/^capable\t8\t24000\twidth=8,/capable\t8\t24000\twidth=7,/' tools/run-gates/gate-profiles.txt && \
sed -i '88s/"gov-session": 2048,/"gov-session": 2304,/' tools/roles/check_roles.py && \
python3 - <<'EOF'
p='tools/roles/kit.toml'
s=open(p,encoding='utf-8').read()
s=s.replace('name = "roles catalogue"\nsubject = "repo"\nargv = ["python", "{kit}/check_roles.py"]\nguard = []\nceiling = 120','name = "roles catalogue"\nsubject = "repo"\nargv = ["python", "{kit}/check_roles.py"]\nguard = []\nceiling = 130',1)
s=s.replace('argv = ["bash", "{kit}/adopt-roles.sh", "--check"]\nguard = []\nceiling = 300','argv = ["bash", "{kit}/adopt-roles.sh", "--check"]\nguard = []\nceiling = 310',1)
s=s+'\n[[gate_leg]]\nname = "roles v2 new leg"\nsubject = "repo"\nargv = ["python", "{kit}/check_roles.py"]\nguard = []\n'
open(p,'w',encoding='utf-8',newline='\n').write(s)
EOF
git diff --stat && git commit -qam "synthetic gov v2" && git log --oneline -1
````

64. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && python3 $S/gov/tools/govkit/govkit.py update --target . > $S/up1.txt 2>&1; echo "rc $?"; grep -v -E "^\s+(current|project-owned:skipped)\s" $S/up1.txt | grep -v "^  [a-z-]\+ \+level\|none declared" | head -80
````

65. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && timeout 1200 python3 $S/gov/tools/govkit/govkit.py update --target . --write > $S/up1w.txt 2>&1; echo "rc $?"; grep -v -E "^\s+(current|project-owned:skipped|re-rendered)\s|carry map|the [0-9]+ row\(s\) under|level ·|none declared|mode-carry" $S/up1w.txt | head -90
````

66. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && for pat in "ADOPTER-WF-TRIGGER:tools/roles/workflows.toml" "GOV-V2-RESEARCH:tools/roles/workflows.toml" "ADOPTER-POLICY:tools/roles/house/policy.toml" "GOV-V2-SEED:tools/roles/house/policy.toml" "ADOPTER-LENS:tools/review-harness/tier2-review.template.js" "GOV-V2-RESUME:tools/review-harness/tier2-review.template.js" "ADOPTER-LENS:tools/review-harness/tier2-review.js" "GOV-V2-RESUME:tools/review-harness/tier2-review.js" "ADOPTER-RENDERED-HARNESS:tools/review-harness/tier2-review.js" "width=3:tools/run-gates/gate-profiles.txt" "width=7:tools/run-gates/gate-profiles.txt" "ACMEQA:.unattended.conf" "acme-signoff:.unattended.conf" "ADOPTER-HOUSE-SPECWRITER:.claude/agents/gov-spec-writer.md" "ADOPTER-ROLE:.claude/agents/acme-auditor.md" "ADOPTER-ROLE:tools/roles/agents/acme-auditor.agent.md" "2304:tools/roles/check_roles.py" "ADOPTER-LEG:tools/gate-legs.json" "roles v2 new leg:tools/gate-legs.json" "review-join ban:tools/gate-legs.json" "--root:tools/gate-legs.json"; do p=${pat%%:*}; f=${pat#*:}; printf '%-28s %-50s %s\n' "$p" "$f" "$(grep -c -- "$p" "$f" 2>&1)"; done; grep -n "^effort" .claude/agents/gov-builder.md; git status --short | head -20
````

67. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && git add -A && git commit -qm "partial v2" --no-verify && python3 - <<'EOF'
import json
p='tools/gate-legs.json'
l=json.load(open(p,encoding='utf-8'))
for r in l:
    if r['name']=='roles catalogue': r['argv']=r['argv'][:2]
open(p,'w',encoding='utf-8',newline='\n').write(json.dumps(l,indent=2,ensure_ascii=False)+"\n")
EOF
git commit -qam "revert argv edit" --no-verify; timeout 1200 python3 $S/gov/tools/govkit/govkit.py update --target . --write > $S/up2w.txt 2>&1; echo "rc $?"; grep -E "gate leg|gate legs|leg '|^govkit: |claimed|wrote [0-9]" $S/up2w.txt | head -20; for p in "ADOPTER-LEG" "roles v2 new leg" "review-join ban" ; do printf '%-20s %s\n' "$p" "$(grep -c -- "$p" tools/gate-legs.json)"; done; python3 -c "
import json;l=json.load(open('tools/gate-legs.json'));print([ (r['name'],r.get('ceiling')) for r in l if r['name'].startswith('roles') or 'acme' in r['name']]); print([r['name'] for r in l][-4:])"
````

68. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t2 && sed -i '88s/"gov-session": 2048,/"gov-session": 2048, "acme-auditor": 3072,/' tools/roles/check_roles.py && sed -i '87s/seam decides"/seam decides, or ACME-CONFLICT"/' tools/roles/workflows.toml && sed -n 88p tools/roles/check_roles.py && git commit -qam "adopter registers role" --no-verify && timeout 1200 python3 $S/gov/tools/govkit/govkit.py update --target . --write > $S/up3w.txt 2>&1; echo "rc $?"; grep -i -E "conflict|held back|rolled back|HELD|roles/check_roles|roles/workflows|order" $S/up3w.txt | head -20; grep -c "ACME-CONFLICT" tools/roles/workflows.toml; grep -c "acme-auditor" tools/roles/check_roles.py; grep -c "2304" tools/roles/check_roles.py; grep -c "width=7" tools/run-gates/gate-profiles.txt; ls .governance/outbox | head -30
````

69. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t2 && grep -E "gate legs:" $S/up3w.txt; python3 -c "
import json;l=json.load(open('tools/gate-legs.json'));print([(r['name'],r.get('ceiling')) for r in l if r['name'].startswith('roles')])"; head -30 .governance/outbox/update-rollback-roles.md
````

70. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/hooks && grep -n "harnesses" agent-cap.js scratch-guard.js | head -20; grep -n "harnesses" ../roles/render_agents.py | head
````

71. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles && grep -n "def resolve_harness_path" -A28 roles_lib.py; S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; python3 -c "
import json;print(json.load(open('$S/t1/.claude/roles.json'))['harnesses'])"; ls $S/t1/tools/workflows 2>&1 | head -2; python3 -c "
import json;r=json.load(open('$S/t1/.governance/install.json'));print([ (f['source'],f['path']) for f in r['files'] if f['source'].endswith(('tier2-review.js','unattended-unit.js','unattended-build.js'))])"
````

72. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && python3 -c "
import json;print(json.load(open('.claude/roles.json'))['harnesses'])
r=json.load(open('.governance/install.json'));print([ (f.get('source'),f.get('path')) for f in r['files'] if str(f.get('path','')).endswith(('tier2-review.js','unattended-unit.js','unattended-build.js'))])"
````

73. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/gov && echo "GOV-V3-README" >> tools/roles/README.md && git commit -qam "synthetic gov v3" && git log --oneline -1; cd $S/t1 && git add -A && git commit -qm "v2 legs" --no-verify; python3 - <<'EOF'
import json
p='.claude/roles.json'; d=json.load(open(p,encoding='utf-8'))
d['roles']['gov-researcher']['gates']=['acme own leg']
d['harnesses'].append('tools/review-harness/acme-review.js')
open(p,'w',encoding='utf-8',newline='\n').write(json.dumps(d,indent=2)+"\n")
EOF
git commit -qam "edit roles.json" --no-verify; timeout 1200 python3 $S/gov/tools/govkit/govkit.py update --target . --write > $S/up4w.txt 2>&1; echo "rc $?"; grep -E "roles|generated" $S/up4w.txt | grep -v "carry map\|row(s) under\|level ·\|doc_reads" | head; grep -c "acme own leg\|acme-review" .claude/roles.json; git status --short | head
````

74. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && grep -n "ran roles\|roles.json\|generated:\|verify roles" $S/up4w.txt | head; git diff .claude/roles.json | head -20; python3 -c "import json;print(json.load(open('.claude/roles.json'))['roles'].get('acme-auditor'))"
````

75. Bash

````text
grep -n "^## \|^### " skills/session-kickoff/MANIFEST-TEMPLATE.md | head -30; ls .githooks; head -30 .githooks/gate-env.sh 2>/dev/null
````

76. Bash

````text
grep -n "gate-env" .githooks/pre-push | head -5; sed -n 30,60p .githooks/gate-env.sh | grep -v "^#" ; grep -n "GATE_POLICY_FILE" tools/unattended/.unattended.conf.example | head -3
````

77. Bash

````text
grep -v "^\s*#" .githooks/gate-env.sh | grep -v "^\s*$"; grep -n "\. \"\?\$.*gate-env\|source.*gate-env\|gate-env.sh\"" .githooks/pre-push | head
````

78. Bash

````text
python3 - <<'EOF'
import json,tomllib,glob
legs=json.load(open('tools/gate-legs.json',encoding='utf-8'))
names=[l['name'] for l in legs]
desc=set(); exempt=set()
for f in glob.glob('tools/*/kit.toml')+glob.glob('tools/govkit/entries/*.toml'):
    d=tomllib.load(open(f,'rb'))
    for g in d.get('gate_leg',[]): desc.add(g['name'])
    for g in d.get('exempt_leg',[]): exempt.add(g.get('name'))
reg=tomllib.load(open('tools/govkit/registry.toml','rb'))
for g in reg.get('exempt_leg',[]): exempt.add(g.get('name'))
print('manifest legs',len(names),'descriptor legs',len(desc),'exempt rows',len(exempt))
gov_only=[n for n in names if n not in desc]
print('in manifest, from no descriptor:',len(gov_only))
for n in gov_only: print('  ',n, '(exempt_leg)' if n in exempt else '')
EOF
````

79. Bash

````text
grep -n "exempt_leg" -B2 -A6 tools/govkit/registry.toml | head -30; grep -n "exempt_leg" tools/govkit/govkit.py | head -10
````

80. Bash

````text
ls -a | grep "^\.\w" ; cat .agent-cap.conf 2>/dev/null | grep -v "^#"; ls memory/project/; wc -c tools/roles/house/*.md | tail -1; git log --oneline -3 -- tools/roles/house/policy.toml tools/roles/workflows.toml | cat
````

81. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory && grep -rlI -E "DIRECTIVES_EXTRA|PHASES_EXTRA|DOD_EXTRA|HALT_CODES_EXTRA|HOLD_CODES_EXTRA" . | head -20; echo ---; grep -rnI -i -E "adopter'?s? own (gate )?leg|their own leg|own legs|a leg the target wrote|target's own leg" . | head -20
````

82. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory && grep -rnI -E "DIRECTIVES_EXTRA" backlog/TOOL.md | head -5; echo ---; grep -rlI "DEPL-aRepatriatedFork-17\b" builds | head -3; grep -rnI -E "S8|claimed" builds/aRepatriatedFork/spec/*DEPL-aRepatriatedFork-17*.md | head -8
````

83. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory && grep -rlI "DEPL-cMendedVintage-22\b" builds | head -3; f=$(ls builds/cMendedVintage/spec/*-22.md 2>/dev/null | head -1); echo $f; [ -n "$f" ] && grep -n -i "measured\|adopter\|nc\b\|inCMS\|hand-edit" $f | head -12; f2=$(ls builds/aBenchedProbe/spec/*DEPL-aBenchedProbe-2.md 2>/dev/null|head -1); echo $f2; [ -n "$f2" ] && grep -n -i "keep\|adopter.*ceiling\|own bound\|inCMS\|nc\b" $f2 | head -10
````

84. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory && grep -rnI -E "(nc|inCMS|NicoCares|adopter)[^.]{0,80}(policy\.toml|workflows\.toml|house overlay|house/)" . | head -8; echo ---; grep -rnI -E "hand-widened|TOOL-dThriftyLanding-12" builds/dThriftyLanding/spec/*-12.md 2>/dev/null | head -4; echo ---; grep -rnI -E "(inCMS|nc|NicoCares)('s)? (own |forked |custom )?(tier2|harness|review harness|lens)" . | head -8
````

85. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/aRepatriatedFork && sed -n 1,25p spec/2026-09-23-spec-TOOL-aRepatriatedFork-5.md | cut -c1-400; grep -n -i "lens\|harness\|leg\|workflow\|phase\|DoD\|directive" README.md | head -25
````

86. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/aRepatriatedFork && sed -n 74,135p README.md | cut -c1-170; grep -n "^## 1" -A8 spec/2026-09-23-spec-TOOL-aRepatriatedFork-4.md | cut -c1-300
````

87. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && W=$(pwd -W); grep -n "agent-cap" .claude/settings.json | head -3; for sp in tools/review-harness/tier2-review.js tools/review-harness/unattended-unit.js; do printf '{"hook_event_name":"PreToolUse","tool_name":"Workflow","cwd":"%s","tool_input":{"scriptPath":"%s","args":{"repo":"%s","roles":{"diffFinder":"gov-diff-reviewer"}}}}' "$W" "$sp" "$W" | CLAUDE_PROJECT_DIR="$W" node tools/hooks/agent-cap.js > $S/hk.out 2>&1; echo "$sp rc=$?"; head -c 400 $S/hk.out; echo; done
````

88. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools && grep -n "def cmd_harness_args\|harness-args\|stage-efforts\|lensNotes\|checklist" roles/handoff.py | head -12; grep -n "lensNotes\|checklist" roles/SKILL.template.md workflows/REVIEW-PROTOCOL.template.md memory-tree/BUILD-METHOD.template.md | head -8
````

89. Bash

````text
grep -n "GOTCHAS\|gotchas/\|\"gotchas\"" tools/memory-tree/gotchas.py | head -5; ls memory | head -30; ls memory/gotchas 2>/dev/null | head -3; ls memory/gotchas | wc -l
````

90. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && ls memory memory/gotchas 2>&1 | head; python3 -c "
import json;r=json.load(open('.governance/install.json'));print([f['path'] for f in r['files'] if 'gotchas' in f['path'] or f['path'].startswith('memory/project')])"
````

91. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && git add -A && git commit -qm "v3" --no-verify; grep -c "stop-guard" .claude/settings.json; cat $S/gov/tools/unattended/stop-guard.fragment.json | head -20
````

92. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; cd $S/t1 && python3 - <<'EOF'
import json
p='.claude/settings.json'; d=json.load(open(p,encoding='utf-8'))
ev=d['hooks'].get('Stop',[])
d['hooks']['Stop']=[e for e in ev if 'stop-guard' not in json.dumps(e)]
if not d['hooks']['Stop']: del d['hooks']['Stop']
d['hooks'].setdefault('PreToolUse',[]).append({"matcher":"Bash","hooks":[{"type":"command","command":"echo ADOPTER-HOOK"}]})
open(p,'w',encoding='utf-8',newline='\n').write(json.dumps(d,indent=2)+"\n")
EOF
grep -c "stop-guard" .claude/settings.json; git commit -qam "adopter drops stop-guard, adds own hook" --no-verify; cd $S/gov && python3 - <<'EOF'
p='tools/unattended/stop-guard.fragment.json'
s=open(p,encoding='utf-8').read().replace('"matcher": "*",','"matcher": "*", "_v4": "GOV-V4",')
open(p,'w',encoding='utf-8',newline='\n').write(s)
EOF
git commit -qam "synthetic gov v4" && cd $S/t1 && timeout 1200 python3 $S/gov/tools/govkit/govkit.py update --target . --write > $S/up5w.txt 2>&1; echo "rc $?"; grep -i -E "settings|stop-guard|wired|fragment|merge" $S/up5w.txt | grep -v "carry map\|row(s) under\|current " | head -12; grep -c "stop-guard" .claude/settings.json; grep -c "ADOPTER-HOOK" .claude/settings.json
````

93. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fx"; grep -c "review-join ban" $S/up2w.txt; grep -n "acme" $S/up2w.txt $S/up1w.txt $S/up4w.txt | head; grep -n "acme-auditor\|agents/acme" $S/up*.txt | head -3
````

94. Bash

````text
python3 - <<'EOF'
import tomllib,glob
FLOW=('roles','review-harness','unattended','run-gates','memory-tree','kickoff-manifest','agent-cap','push-main','settings-merge','playbook-render')
for f in sorted(glob.glob('tools/*/kit.toml')+glob.glob('tools/govkit/entries/*.toml')):
    d=tomllib.load(open(f,'rb'))
    if d.get('id') not in FLOW: continue
    out=[]
    for r in d.get('files',[]):
        if r.get('role') in ('rendered','seed'):
            inc=r['include']; inc=inc if isinstance(inc,list) else [inc]
            out.append(f"{r['role']}:{','.join(inc)}->{r.get('to','(in place)')}")
    for g in d.get('generated',[]): out.append(f"generated:{g['path']}")
    if 'config' in d: out.append(f"config:{d['config']['file']} (owner {d['config'].get('owner')})")
    if 'gate_runner_seed' in d: out.append(f"runner:{d['gate_runner_seed']['file']}")
    out.append(f"gate_legs:{len(d.get('gate_leg',[]))}")
    print(d['id'], '|', ' ; '.join(out))
EOF
ls tools/unattended/*.fragment.json tools/hooks/*.fragment.json
````

95. Bash

````text
python3 - <<'EOF'
import tomllib,glob
FLOW=('roles','review-harness','unattended','run-gates','memory-tree','kickoff-manifest','agent-cap','push-main','settings-merge','playbook-render')
for f in sorted(glob.glob('tools/*/kit.toml')+glob.glob('tools/govkit/entries/*.toml')):
    d=tomllib.load(open(f,'rb'))
    if d.get('id') not in FLOW: continue
    out=[]
    for r in d.get('files',[]):
        if r.get('role') in ('rendered','seed'):
            inc=r.get('include') or r.get('path') or r.get('source') or '?'; inc=inc if isinstance(inc,list) else [inc]
            out.append(f"{r['role']}:{','.join(inc)}->{r.get('to','(in place)')}")
    for g in d.get('generated',[]): out.append(f"generated:{g['path']}")
    if 'config' in d: out.append(f"config:{d['config']['file']}")
    if 'gate_runner_seed' in d: out.append(f"runner:{d['gate_runner_seed']['file']}")
    out.append(f"gate_legs:{len(d.get('gate_leg',[]))}")
    print(d['id'], '|', ' ; '.join(out))
EOF
````

96. Bash

````text
S="/c/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; rm -rf "$S/fx" "$S/sk.md"; ls "$S"; cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && git status --short
````

97. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools && grep -n -i "kept the target's ceiling\|claimed   leg\|differs from what the receipt recorded\|a leg the target wrote\|PHASES_EXTRA=\"[A-Z]\|DOD_EXTRA=\"[a-z]" govkit/selftest.py unattended/*.test.sh roles/*.test.sh 2>/dev/null | head -12
````

98. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools && grep -n -i "own leg\|target.*own.*leg\|adopter.*leg.*surviv\|foreign leg\|non-gov leg" govkit/selftest.py | head -8; grep -n -E "EXTRA=\"[A-Za-z]" unattended/*.test.sh | head -6; grep -n "acme\|adopter role\|house role\|extra role\|own role" roles/render_agents.py roles/adopt-roles.test.sh | head -5
````

## [flow-design] Dispatch 124: the converged design

1. Bash

````text
ls memory/builds/dClosedLoop/build/ && wc -l memory/builds/dClosedLoop/build/*.md | tail -40
````

2. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && wc -l 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md 2026-10-14-build-PLAY-dClosedLoop-1-flow.md 2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md 2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md 2026-10-14-build-PLAY-dClosedLoop-1-roles.md 2026-10-16-build-PLAY-dClosedLoop-1-systems.md 2026-10-15-build-PLAY-dClosedLoop-1-review-system.md 2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md 2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md 2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md 2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md 2026-10-19-build-PLAY-dClosedLoop-1-research-adopter-design.md; grep -n '^#' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | head -100
````

3. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && awk 'NR>=1439 && NR<=1597 {print NR": "substr($0,1,160)}' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md
````

4. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n '1447p' 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | sed 's/; /;\n/g'
````

5. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && for n in 1450 1449 1456; do sed -n "${n}p" 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | sed 's/; /;\n/g'; echo ======; done
````

6. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && for n in 1443 1444 1445; do sed -n "${n}p" 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | sed 's/; /;\n/g'; echo ======; done
````

7. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && for n in 1446 1448 1451 1455 1458 1460 1461 1462 1463; do sed -n "${n}p" 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | sed 's/; /;\n/g' | grep -n -i -E '^\| d|adopter|repo-declared|repository|register|playbook|lens|shape|pack|custom|own steps|own item|extension point|factory|point'; echo ======; done
````

8. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n '^#' 2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md 2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md 2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md 2026-10-16-build-PLAY-dClosedLoop-1-systems.md 2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md 2026-10-15-build-PLAY-dClosedLoop-1-review-system.md 2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md 2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md 2026-10-14-build-PLAY-dClosedLoop-1-roles.md
````

9. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i -E "repo-declared|repository's own (step|item|role|leg|pack|lens|preset|playbook|shape|breakpoint|check|key|practice|kind|document|record)|adopter's own (step|item|role|leg|pack|lens|preset|playbook|shape|check|key|practice|kind|test|CI)|custom (step|item|role|leg|pack|lens|preset|shape)|its own (steps|items|roles|legs|lenses)|own roles|own legs|own steps|own items" *.md | grep -v -E 'research-adopter|adopter-instructions' | cut -c1-300
````

10. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n '18,40p' 2026-10-14-build-PLAY-dClosedLoop-1-design-rounds.md
````

11. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i -E "repository registers|adopter registers|registers its own|register its own|its own layer|adopter.{0,20}layer|layer register" *.md | grep -v instruments | cut -c1-350
````

12. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i -E "kind|adopter|repository" 2026-10-14-build-PLAY-dClosedLoop-1-foundations.md | cut -c1-300 | head -80
````

13. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -E '^\*\*R-|R-I|structured source|structured definition|overlay' 2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md | cut -c1-250
````

14. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -o -i -E ".{120}loop definition.{160}" 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md 2026-10-15-*.md 2026-10-16-*.md 2026-10-17-build-PLAY-dClosedLoop-1-ownership.md 2026-10-17-build-PLAY-dClosedLoop-1-project-map.md 2026-10-18-build-PLAY-dClosedLoop-1-walk.md 2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md 2026-10-18-build-PLAY-dClosedLoop-1-fates.md | grep -v instruments | head -30
````

15. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i "loop definition\|loop kit's definition\|tools/loop" *.md | grep -v instruments | cut -c1-260 | head -40
````

16. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i -E "product-test contract|tests\.product|runner adapter|adopter's (CI|legs|own legs|tests)|leg pack point|leg-pack point|legs manifest" 2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md 2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md 2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md 2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md 2026-10-14-build-PLAY-dClosedLoop-1-flow.md 2026-10-15-build-PLAY-dClosedLoop-1-layer-library.md 2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md 2>/dev/null | cut -c1-330
````

17. Bash

````text
ls tools/ && grep -rn -i -E "adopter.{0,30}leg|extra.?legs|project.?legs|legs\.local|local legs" tools/run-gates/*.sh tools/run-gates/*.py tools/run-gates/README.md 2>/dev/null | head -20
````

18. Bash

````text
sed -n 3075,3090p tools/run-gates/run-gates.sh; grep -n -i -E "GATE_LEGS|legs_file|gate-legs.json" tools/run-gates/run-gates.sh | head -15; grep -n -i -E "gate-legs|legs" tools/run-gates/kit.toml | head
````

19. Bash

````text
sed -n 155,215p tools/run-gates/kit.toml; sed -n 1,40p tools/run-gates/kit.toml
````

20. Bash

````text
ls tools/govkit/ && grep -n "dedupe_key" tools/govkit/*.py | head -20
````

21. Bash

````text
grep -n -i -E "def .*(gate_leg|emit_leg|merge_leg|manifest_rows|promot)" tools/govkit/govkit.py | head -20
````

22. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles && ls; ls house agents 2>/dev/null; sed -n 1,80p house/policy.toml
````

23. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles && grep -n -i -E "adopter|seed|project-owned|house" kit.toml | head -30; grep -n -i -E "own role|adopter.{0,40}role|add a role|new role" README.md workflows.toml | head
````

24. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i -E "adopter|its own|repo-|repository's" 2026-10-14-build-PLAY-dClosedLoop-1-flow.md 2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md | cut -c1-260 | head -40
````

25. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n 695,715p 2026-10-14-build-PLAY-dClosedLoop-1-flow.md
````

26. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i "playbook" 2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md | cut -c1-300 | head -30
````

27. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i -E "overlay|tools/loop|workflows.toml|gate-legs|policy.toml|house" 2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md | cut -c1-330
````

28. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n 40,80p 2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md | cut -c1-420
````

29. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n 80,130p 2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md | cut -c1-360 | grep -n -i -E "loop|leg|shape|workflow|transition|lens|preset|playbook|kit"
````

30. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools && grep -n -i -E "lens" hooks/agent-cap.js | head -25; grep -n -E "LENSES|lenses *=" workflows/tier2-review.js | head
````

31. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i -E "(adopter|repository).{0,40}(role|item|step|transition|shape|workflow|lens)s?\b" 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md 2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md 2026-10-14-build-PLAY-dClosedLoop-1-roles.md 2026-10-16-build-PLAY-dClosedLoop-1-systems.md 2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md 2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md 2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md 2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md 2026-10-18-build-PLAY-dClosedLoop-1-fates.md 2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md | cut -c1-280 | head -40
````

32. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i -E "gate-legs|workflows.toml|house|tier2-review|agent-cap|kit.toml|adopt-" 2026-10-18-build-PLAY-dClosedLoop-1-fates.md | cut -c1-330
````

33. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n 215,232p 2026-10-18-build-PLAY-dClosedLoop-1-fates.md
````

34. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles/house && wc -l *.md; cat gov-builder.md | head -30; cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && git log --oneline -3 -- tools/roles/house/ | cat
````

35. Bash

````text
python -c "
import json,glob,re
try:
  import tomllib
except: tomllib=None
legs=json.load(open('tools/gate-legs.json',encoding='utf-8'))
names={l['name'] for l in legs}
subj={}
for l in legs: subj[l.get('subject','repo')]=subj.get(l.get('subject','repo'),0)+1
shipped=set()
for f in glob.glob('tools/*/kit.toml'):
  d=tomllib.load(open(f,'rb'))
  for g in d.get('gate_leg',[]): shipped.add(g['name'])
print('manifest legs',len(names),'by subject',subj)
print('declared in kit.toml gate_leg',len(shipped),'of which in manifest',len(shipped&names))
print('manifest legs no kit declares',len(names-shipped))
" 2>&1 | head; 
````

36. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n "RS-2" 2026-10-16-build-PLAY-dClosedLoop-1-systems.md | cut -c1-400 | head; cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 && python -c "
import json;L=json.load(open('tools/gate-legs.json',encoding='utf-8'))
print([l['name'] for l in L if l['name'] in ('memory hygiene','lexicon naming predicates')])"; grep -n "memory hygiene\|lexicon naming predicates" tools/*/kit.toml | head -4
````

37. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i -E "adopter.{0,60}(item|step|role|leg|pack|lens|shape|transition|breakpoint)|(item|step|role|leg|pack|lens|shape|transition|breakpoint).{0,30}(an adopter|the adopter|a repository)" 2026-10-18-build-PLAY-dClosedLoop-1-shape-reviews-compared.md 2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md 2026-10-18-build-PLAY-dClosedLoop-1-walk.md 2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md 2026-10-18-build-PLAY-dClosedLoop-1-recut.md 2026-10-17-build-PLAY-dClosedLoop-1-ownership.md 2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md | cut -c1-300 | head -30
````

38. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n 571,580p 2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md; grep -n -i "custom pack" 2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md | cut -c1-300
````

39. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && sed -n 580,586p 2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md
````

40. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -o -E "\| \`[a-z.<>-]*(effort|gates|model)[a-z.<>-]*\` \|" 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md; grep -n -i -E "\[gates\]|effort\.roles|roles\.effort|roles\.gates" 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md 2026-10-18-build-PLAY-dClosedLoop-1-fates.md 2026-10-16-build-PLAY-dClosedLoop-1-systems.md | cut -c1-200
````

41. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n -i "overlay" 2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md 2026-10-16-build-PLAY-dClosedLoop-1-research-distribution-a.md 2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md | cut -c1-300
````

42. Bash

````text
cd /c/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build && grep -n '^##' 2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md 2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md 2026-10-18-build-PLAY-dClosedLoop-1-fates.md 2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md | head -60
````

## [flow-prior-art] Dispatch 125: prior art outside gov

1. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build" && ls && grep -n -i -E "amends|supersedes|stale|fixed set|witness|shape|layer contract|pack|preset" 2026-10-19-build-PLAY-dClosedLoop-1-adopter-instructions.md | head -60
````

2. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build" && wc -l 2026-10-19-build-PLAY-dClosedLoop-1-research-adopter-prior-art.md && sed -n 1,200p 2026-10-19-build-PLAY-dClosedLoop-1-research-adopter-prior-art.md | cut -c1-400
````

3. WebFetch

````text
https://docs.gitlab.com/ci/yaml/yaml_optimization/
Quote exactly: how `extends` merges (deep merge rules, arrays replaced or merged?), how `!reference` works, nesting limits, and what happens when the referenced/extended key does not exist. Also how included config and local config merge (local overrides?).
````

4. WebFetch

````text
https://docs.gitlab.com/ci/yaml/includes/
Quote exactly: how included files merge with the local .gitlab-ci.yml (which wins, deep merge, arrays), how to override included config, pinning include:project with ref, include:component versions, and any statement about what happens when an included job is changed upstream or removed. Also `needs` referencing missing jobs if mentioned.
````

5. WebFetch

````text
https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows
Quote exactly: how a caller calls a reusable workflow (uses: owner/repo/.github/workflows/x.yml@ref), pinning by SHA/tag, inputs/secrets, whether the caller can add steps to or override jobs inside the called workflow, nesting limits, and outputs. Anything about what happens when the called workflow changes.
````

6. WebFetch

````text
https://learn.microsoft.com/en-us/azure/devops/pipelines/security/templates
Quote exactly: how `extends` templates work, stepList parameters, how a template can inject steps before/after user steps, restrict what user steps can do (e.g. forbid script tasks), and the "required template" approval check — what happens when a pipeline doesn't extend the required template.
````

7. WebFetch

````text
https://docs.gitlab.com/ci/yaml/
Quote exactly what the docs say about `needs:optional` and what happens when a job in `needs` does not exist in the pipeline (error message?). Also `inherit`, and `include:component` / `spec:inputs` version pinning if present. Also `stages` ordering when includes define stages.
````

8. WebFetch

````text
https://pre-commit.com/
Quote exactly: repos with rev pinning; `repo: local` hooks; `repo: meta`; how a user overrides a hook's args/files/stages etc in their config (which keys can be overridden); what `pre-commit autoupdate` does (and --freeze); what happens if a hook id in the user config no longer exists in the upstream repo at the new rev; `fail_fast`; ordering of hooks; skipping via SKIP env.
````

9. WebFetch

````text
https://docs.renovatebot.com/config-presets/
Quote exactly: how `extends` presets resolve, order/precedence of presets vs user config, how to override a preset value, `ignorePresets`, versioning presets (github>owner/repo#tag), what happens if a preset is missing / renamed (error?), and how arrays (e.g. packageRules) merge.
````

10. WebFetch

````text
https://danger.systems/js/usage/extending-danger
Quote how Danger is extended with plugins and shared rules (Peril / shared dangerfiles / danger.import or plugins), how a user adds a rule, and anything about versioning or overriding shared rules.
````

11. WebFetch

````text
https://docs.gitlab.com/ci/yaml/
Quote exactly what the docs say about `needs:optional` and what happens when a job in `needs` does not exist in the pipeline. Also `inherit:default`.
````

12. WebFetch

````text
https://docs.renovatebot.com/key-concepts/presets/
Quote exactly: precedence of presets vs. repo config, order of multiple presets in extends, how arrays like packageRules merge (appended or replaced), how to override a preset value, and versioning of presets.
````

13. WebFetch

````text
https://docs.temporal.io/develop/typescript/versioning
Quote exactly: how patching (patched / deprecatePatch) works, worker versioning / build ids, what happens on non-determinism when workflow code changes under a running workflow (NonDeterminismError), and how a running execution keeps its old path.
````

14. WebFetch

````text
https://code.claude.com/docs/en/sub-agents
Quote exactly: subagent file locations and precedence when names collide (project vs user vs plugin vs CLI flag), frontmatter fields (name, description, tools, disallowedTools, model, etc.), what happens when tools are omitted (inherit all), how plugins ship subagents, and anything about overriding a plugin's subagent or about a subagent name not found.
````

15. WebFetch

````text
https://docs.renovatebot.com/config-overview/
Quote exactly what this page says about configuration precedence (global, inherited, repository, presets), how presets in extends are resolved relative to the repo's own settings, and how arrays/objects merge (e.g. packageRules concatenated vs replaced).
````

16. WebFetch

````text
https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html
Quote exactly: lifecycle phases, how plugin goals bind to phases (packaging defaults and <executions><phase>), order of multiple goals bound to the same phase (POM order / inherited first?), how to disable an inherited execution (phase none), and pluginManagement/inheritance from a parent POM.
````

17. WebFetch

````text
https://docs.gradle.org/current/userguide/controlling_task_execution.html
Quote exactly: dependsOn, mustRunAfter, shouldRunAfter, finalizedBy semantics; what happens if dependsOn names a task that doesn't exist; how to disable a task (enabled=false / onlyIf) and whether its dependencies still run; how to hook into lifecycle tasks like check/build.
````

18. WebFetch

````text
https://pre-commit.com/#pre-commit-autoupdate
Does the page say anything about hook ordering (hooks run in the order listed?), about what happens when a configured hook id is not found in the repository at its rev (error message), or about `minimum_pre_commit_version`? Quote exactly.
````

19. WebFetch

````text
https://raw.githubusercontent.com/pre-commit/pre-commit/main/pre_commit/repository.py
Quote the exact code and error message raised when a hook id configured by the user is not present in the repository's manifest at the pinned rev. Also show how user config keys override manifest keys (the merge of hook dicts).
````

20. WebFetch

````text
https://maven.apache.org/guides/mini/guide-configuring-plugins.html
Quote exactly what is said about execution ids during inheritance (merge vs additional execution), combine.children / combine.self (append, override, merge), and any mention of binding an inherited execution to phase none or skipping it. Also pluginManagement.
````

21. WebFetch

````text
https://support.atlassian.com/jira-cloud-administration/docs/manage-workflow-schemes/
Quote exactly: how a workflow scheme is shared across projects, what happens when an admin edits a workflow used by many projects (draft/publish, status migration of existing issues), how a project gets its own copy (copy/customize), and whether a project-level edit affects other projects sharing the scheme.
````

22. WebFetch

````text
https://backstage.io/docs/features/software-templates/writing-custom-actions
Quote exactly: how a user registers a custom scaffolder action, how template steps reference actions by id, what happens if a step references an action id that is not registered, and whether built-in actions can be overridden by registering one with the same id.
````

23. WebSearch

````text
Jira cloud shared workflow scheme edit workflow affects all projects "shared" copy workflow project
````

24. WebFetch

````text
https://docs.crewai.com/en/concepts/agents
Quote exactly: how agents are defined in YAML (agents.yaml) and code, how @CrewBase maps yaml keys to methods, what happens if a yaml key is missing or a method references a missing key, how tasks reference agents, and fields like tools, llm, allow_delegation.
````

25. WebFetch

````text
https://docs.langchain.com/oss/python/langgraph/use-subgraphs
Quote exactly: how a subgraph is added as a node, state schema sharing vs transformation, what happens when parent and subgraph state keys differ, and anything about compile-time validation of edges to unknown nodes.
````

26. WebFetch

````text
https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html
Quote exactly: team presets (RoundRobinGroupChat, SelectorGroupChat, Swarm), how a user adds their own agent to a team, how speaker selection knows agents (descriptions, handoffs), and any component config / declarative serialization (dump_component/load_component) and versioning.
````

27. WebFetch

````text
https://confluence.atlassian.com/adminjiracloud/configuring-workflow-schemes-776636598.html
Quote exactly what the page says about shared workflow schemes affecting all projects, default schemes needing copying, draft workflow schemes, publishing and issue status migration (mapping statuses when a status is removed).
````

28. WebFetch

````text
https://docs.getdbt.com/reference/resource-configs/enabled
Quote exactly: how a project disables a model from an installed package (+enabled: false in dbt_project.yml under the package name), and what happens when another model ref()s a disabled model (error message).
````

29. WebFetch

````text
https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch
Quote exactly: how dispatch search_order lets a root project override a package's macro, the config syntax (dispatch: macro_namespace, search_order), and what precedence applies.
````

30. WebFetch

````text
https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/selector-group-chat.html
Quote exactly how SelectorGroupChat chooses the next speaker (uses agent name and description in the selector prompt), selector_func / candidate_func, and what happens if the selector returns an invalid agent name.
````

31. WebFetch

````text
https://support.atlassian.com/jira-cloud-administration/docs/configure-workflow-schemes/
Quote exactly what the page says about shared workflow schemes affecting all projects, default schemes needing copying, draft workflow schemes, publishing and issue status migration (mapping statuses when a status is removed).
````

32. WebFetch

````text
https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/plugins.html
Quote exactly: what Airflow plugins can add (operators? macros, listeners, timetables, views), the note about operators no longer via plugins, and listeners/hooks into DAG/task lifecycle. Anything about cluster policies (task_policy, dag_policy) that mutate or reject tasks.
````

33. WebFetch

````text
https://docs.github.com/en/actions/tutorials/create-actions/create-a-composite-action
Quote: how a composite action is used as a step (uses: owner/repo@ref), how it bundles steps, and whether a caller can modify its inner steps.
````

34. WebFetch

````text
https://docs.temporal.io/worker-versioning
Quote exactly: Pinned vs Auto-Upgrade versioning behaviors, what happens to running workflows when a new deployment version is current, and how drain/sunset works.
````

35. Bash

````text
PY=$(bash tools/lib/resolve-python.sh 2>/dev/null); echo "py=$PY"; $PY --version; $PY -c "import importlib.util as u;[print(m, bool(u.find_spec(m))) for m in ['pre_commit','langgraph','crewai','autogen_agentchat','yaml','networkx']]"; for t in pre-commit mvn gradle git; do command -v $t; done
````

36. WebFetch

````text
https://raw.githubusercontent.com/backstage/backstage/master/plugins/scaffolder-backend/src/scaffolder/actions/TemplateActionRegistry.ts
Quote exactly the error thrown on registering an action id that already exists and on getting an action id that isn't registered.
````

37. WebFetch

````text
https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/cluster-policies.html
Quote exactly: what dag_policy and task_policy do, that they can mutate tasks or raise AirflowClusterPolicyViolation to reject, and when they run.
````

38. Bash

````text
sed -n 1,80p tools/lib/resolve-python.sh | head -40; for c in python3 python py; do command -v $c && $c --version; done
````

39. Bash

````text
python3 -c "import importlib.util as u;[print(m, bool(u.find_spec(m))) for m in ['pre_commit','langgraph','crewai','autogen_agentchat','yaml']]"; python3 -m pip --version; command -v pre-commit mvn gradle java node npm
````

40. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad"; mkdir -p "$S/flowprobe" && cd "$S/flowprobe" && python3 -m venv venv && ./venv/Scripts/python -m pip install -q pre-commit langgraph 2>&1 | tail -3; ./venv/Scripts/python -c "import pre_commit, langgraph; from importlib.metadata import version as v; print(v('pre-commit'), v('langgraph'))"
````

41. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/flowprobe"; cd "$S" && rm -rf up consumer && mkdir up consumer && cd up && git init -q && git config user.email p@p && git config user.name p
printf '#!/usr/bin/env bash\necho "HOOK $(basename $0) ARGS: $*" | head -c 200; echo\n' > a.sh; cp a.sh b.sh
cat > .pre-commit-hooks.yaml <<'EOF'
- id: a
  name: a
  entry: a.sh
  language: unsupported_script
  args: [--upstream-v1]
  pass_filenames: false
  always_run: true
  verbose: true
- id: b
  name: b
  entry: b.sh
  language: unsupported_script
  pass_filenames: false
  always_run: true
  verbose: true
EOF
git add -A && git commit -qm v1 && git tag v1
cd ../consumer && git init -q && git config user.email p@p && git config user.name p && echo x > f.txt
cat > .pre-commit-config.yaml <<EOF
repos:
- repo: $S/up
  rev: v1
  hooks:
  - id: a
    args: [--mine]
  - id: b
- repo: local
  hooks:
  - id: l
    name: l-local
    entry: bash -c 'echo LOCAL'
    language: system
    pass_filenames: false
    always_run: true
    verbose: true
EOF
git add -A && git commit -qm c
export PRE_COMMIT_HOME="$S/pchome"; ../venv/Scripts/pre-commit run --all-files; echo "exit=$?"
````

42. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/flowprobe"; export PRE_COMMIT_HOME="$S/pchome"; cd "$S/up" && sed -i 's/--upstream-v1/--upstream-v2-required-flag/; s/^- id: b$/- id: b2/; s/^  name: b$/  name: b2/' .pre-commit-hooks.yaml && cat >> .pre-commit-hooks.yaml <<'EOF'
- id: new-upstream
  name: new-upstream
  entry: a.sh
  language: unsupported_script
  pass_filenames: false
  always_run: true
EOF
git commit -qam v2 && git tag v2
cd ../consumer && echo "--- autoupdate:"; ../venv/Scripts/pre-commit autoupdate 2>&1 | tail -3; echo "exit=$?"; grep rev: .pre-commit-config.yaml
echo "--- force rev v2:"; sed -i 's/rev: v1/rev: v2/' .pre-commit-config.yaml; ../venv/Scripts/pre-commit run --all-files 2>&1 | tail -4; echo "exit=${PIPESTATUS[0]}"
echo "--- after user drops b, keeps a override:"; python3 - <<'P'
p='.pre-commit-config.yaml';s=open(p).read().replace("  - id: b\n","");open(p,'w').write(s)
P
../venv/Scripts/pre-commit run --all-files 2>&1 | grep -E "HOOK|LOCAL|new-upstream|Passed|Failed"; echo "exit=${PIPESTATUS[0]}"
````

43. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/flowprobe"; export PRE_COMMIT_HOME="$S/pchome"; cd "$S/consumer" && git checkout -q -- .pre-commit-config.yaml && ../venv/Scripts/pre-commit autoupdate >/dev/null 2>&1; echo "autoupdate exit=$?"; grep rev: .pre-commit-config.yaml
````

44. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/flowprobe"; mkdir -p "$S/lgscripts" && cat > "$S/lgscripts/lg.py" <<'P'
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
class S(TypedDict, total=False):
    log: list
def n(name):
    return lambda s: {"log": (s.get("log") or []) + [name]}
def upstream(review_name="review"):
    g = StateGraph(S)
    g.add_node("plan", n("plan")); g.add_node(review_name, n(review_name))
    g.add_edge(START, "plan"); g.add_edge("plan", review_name); g.add_edge(review_name, END)
    return g
def trial(label, f):
    try:
        r = f(); print(label, "->", r)
    except Exception as e:
        print(label, "-> RAISED", type(e).__name__, str(e)[:160])
def add_mine(g, after="review"):
    g.add_node("mine", n("mine")); g.add_edge(after, "mine"); g.add_edge("mine", END); return g
trial("T0 extend v1", lambda: add_mine(upstream()).compile().invoke({}))
trial("T1 upstream renames review->check", lambda: add_mine(upstream("check")).compile().invoke({}))
trial("T2 add node with upstream's name", lambda: upstream().add_node("review", n("x")))
trial("T3 remove_edge api exists?", lambda: hasattr(StateGraph, "remove_edge") or [a for a in dir(StateGraph) if "remove" in a.lower() or "edge" in a.lower()])
def dangling():
    g = upstream(); g.add_node("orphan", n("orphan")); return g.compile().invoke({})
trial("T4 node with no edges", dangling)
def deadend():
    g = upstream(); g.add_node("mine", n("mine")); g.add_edge("review", "mine"); return g.compile().invoke({})
trial("T5 node with no outgoing edge", deadend)
P
"$S/venv/Scripts/python" -I "$S/lgscripts/lg.py"
````

45. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build" && grep -n -i -E "requires|witness|transition table|position engine|layer contract|register|shape|tag" 2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md | head -50; echo ----; grep -n -i -E "layer contract|register|shape|unknown|refus" 2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md | head -40
````

46. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build" && sed -n 160,200p 2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md; sed -n 310,345p 2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md; grep -n -E "^\*\*P(24|28|38)\b|P28|registered shape|shapes? (single|per-unit)" 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md | head -20
````

47. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build" && sed -n 773,790p 2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md; sed -n 200,215p 2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md; grep -n -i -E "shape.*(single|per-unit|panel|twin|experiment)|registered shape|unknown role|role.*register" 2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md | head -15
````

48. Bash

````text
cd "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build" && sed -n 455,475p 2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md; grep -n -i -E "workflow shape|shapes" 2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md | head -10
````

49. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/flowprobe"; cat > "$S/lgscripts/govmodel.py" <<'P'
"""Throwaway model of gov's declared flow + roles, composed with an adopter overlay by each candidate mechanism.
Each candidate returns (status, note). status: LOUD (composition refuses/orders), SILENT-WRONG, OK, IMPOSSIBLE."""
import copy, hashlib, json
H=lambda d: hashlib.sha256(json.dumps(d,sort_keys=True).encode()).hexdigest()[:8]
def gov_v1():
    it={
     "item.build.implement":dict(actor="role.builder",inputs={},outputs={"diff":"patch"},requires=[],witness="commit-sha",routes={"done":"item.test.run-legs"}),
     "item.test.run-legs":dict(actor="command",inputs={"diff":"patch"},outputs={"verdict":"verdict"},requires=["item.build.implement"],witness="leg-log",routes={"green":"item.deploy.release"},args=["--packs=core"]),
     "item.deploy.release":dict(actor="command",inputs={"verdict":"verdict"},outputs={},requires=["item.test.run-legs"],witness="tag",routes={}),
    }
    roles={"role.builder":dict(shapes=["single","per-unit"]),"role.reviewer":dict(shapes=["single","panel"])}
    shapes={"single":{},"per-unit":{},"panel":{}}
    fixed={"item.test.run-legs"}  # gov's fixed set: cannot be disabled
    return dict(items=it,roles=roles,shapes=shapes,fixed=fixed)
V1=gov_v1()
def overlay(v1=V1,**kw):
    o=dict(add_items={"item.repo.license-scan":dict(actor="command",inputs={"diff":"patch"},outputs={},requires=["item.build.implement"],witness="scan-log",routes={})},
           amend={"item.test.run-legs":dict(base=H(v1["items"]["item.test.run-legs"]),set={"args":["--packs=core,repo"]})},
           disable=[],add_roles={},spawn=[])
    o.update(kw); return o
# ---------- composition mechanisms ----------
def check_graph(items,typed=True):
    errs=[]
    for t,d in items.items():
        for r in d["requires"]:
            if r not in items: errs.append(f"{t} requires unknown {r}")
            elif typed:
                for k,ty in d["inputs"].items():
                    prov=[items[x]["outputs"].get(k) for x in d["requires"] if x in items]
                    if ty not in prov: errs.append(f"{t} input {k}:{ty} not provided (got {prov})")
    return errs
def C1_override(gov,o):  # keyed deep-merge, user key wins (GitLab include/extends, pre-commit dict.update, Renovate, Maven exec id)
    items=copy.deepcopy(gov["items"]); items.update(copy.deepcopy(o["add_items"]))
    for t,a in o["amend"].items(): items.setdefault(t,{"requires":[],"inputs":{},"outputs":{}}).update(a["set"])
    for t in o["disable"]: items[t]["enabled"]=False
    live={t:d for t,d in items.items() if d.get("enabled",True)}
    errs=[e for e in check_graph(items,typed=False) if "unknown" in e]   # GitLab-style: needs on a missing job fails
    missing=[t for t,d in live.items() if any(r in items and not items[r].get("enabled",True) for r in d["requires"])]
    return ("LOUD",errs) if errs else (("SILENT-WRONG","dependent runs without "+str(missing)) if missing else ("OK",items))
def C2_slots(gov,o):     # fixed skeleton with typed slots (Azure extends stepList, reusable workflow inputs, Maven phases)
    if o["amend"] or o["disable"]: return ("IMPOSSIBLE","no way to change a shipped item")
    return ("OK",None)
def C3_graph(gov,o):     # named-dependency graph with compose-time validation (Gradle, GitLab needs, LangGraph)
    items=copy.deepcopy(gov["items"]); items.update(copy.deepcopy(o["add_items"]))
    for t in o["disable"]: items.pop(t,None)
    for t,a in o["amend"].items():
        if t in items: items[t].update(a["set"])
    errs=check_graph(items,typed=True)
    return ("LOUD",errs) if errs else ("OK",items)
def C4_pinned_overlay(gov,o):  # overlay + amends pinned to decl hash + typed graph check + fixed set + item schema + shape contract
    errs=[]
    items=copy.deepcopy(gov["items"])
    for t,d in o["add_items"].items():
        if not d.get("witness"): errs.append(f"{t}: no witness (schema)")
        items[t]=copy.deepcopy(d)
    for t,a in o["amend"].items():
        if t not in items: errs.append(f"amend {t}: target gone (orphan edge)")
        elif H(gov["items"][t])!=a["base"]: errs.append(f"amend {t}: stale pin {a['base']}->{H(gov['items'][t])}")
        else: items[t].update(a["set"])
    for t in o["disable"]:
        if t in gov["fixed"]: errs.append(f"disable {t}: in gov's fixed set")
        else:
            deps=[x for x,d in items.items() if t in d["requires"]]
            if deps: errs.append(f"disable {t}: required by {deps}")
            items.pop(t,None)
    errs+=check_graph(items,typed=True)
    roles=dict(gov["roles"]); roles.update(o["add_roles"])
    for role,shape in o["spawn"]:
        if role not in roles: errs.append(f"spawn {role}: unregistered")
        elif shape not in roles[role]["shapes"]: errs.append(f"spawn {role} in {shape}: role does not declare shape")
    return ("LOUD",errs) if errs else ("OK",items)
def C5_fork(gov,o):      # copy-and-own (Jira copied scheme, eject): adopter composes against the v1 copy forever
    return ("SILENT-WRONG" if gov is not V1 else "OK","adopter runs its v1 copy; gov's change never arrives")
def C6_registry(gov,o):  # roles: lookup by id at dispatch (Backstage registry, Claude Code subagents)
    roles=dict(gov["roles"]); roles.update(o["add_roles"])
    for role,shape in o["spawn"]:
        if role not in roles: return ("LOUD-AT-RUN",f"NotFound {role} at dispatch")
    return ("OK","shape never consulted")
# ---------- scenarios ----------
def v2(mut):
    g=copy.deepcopy(V1); mut(g); return g
S={}
S["A1 gov changes amended item"]=(v2(lambda g:g["items"]["item.test.run-legs"].update(args=["--packs=core","--require-sbom"])), overlay())
def ren(g):
    d=g["items"].pop("item.build.implement"); g["items"]["item.build.write"]=d
    g["items"]["item.test.run-legs"]["requires"]=["item.build.write"]
S["A2 gov renames item adopter depends on"]=(v2(ren), overlay())
def add_before_type(g):
    g["items"]["item.build.vendor-prep"]=dict(actor="command",inputs={},outputs={"diff":"patch-set"},requires=[],witness="x",routes={})
    g["items"]["item.build.implement"]["outputs"]={"diff":"patch-set"}
    g["items"]["item.test.run-legs"]["inputs"]={"diff":"patch-set"}
S["A3a gov adds earlier item, input TYPE changes"]=(v2(add_before_type), overlay())
def add_before_meaning(g):  # same key, same type, new meaning (diff now excludes vendored files); decl of implement unchanged
    g["items"]["item.build.vendor-prep"]=dict(actor="command",inputs={},outputs={},requires=[],witness="x",routes={},note="strips vendored paths from diff")
S["A3b gov adds earlier item, input MEANING changes"]=(v2(add_before_meaning), overlay())
S["A4 adopter disables required gov item"]=(V1, overlay(amend={},disable=["item.test.run-legs"]))
S["A4b adopter disables non-fixed required item"]=(V1, overlay(amend={},disable=["item.build.implement"]))
S["A5 adopter item has no witness"]=(V1, overlay(amend={},add_items={"item.repo.x":dict(actor="command",inputs={},outputs={},requires=[],witness=None,routes={})}))
S["A6 adopter role spawned by unknown shape"]=(V1, overlay(amend={},add_roles={"role.repo.auditor":dict(shapes=["single"])},spawn=[("role.repo.auditor","panel")]))
S["A6b role never registered"]=(V1, overlay(amend={},spawn=[("role.repo.ghost","panel")]))
C=dict(C1=C1_override,C2=C2_slots,C3=C3_graph,C4=C4_pinned_overlay,C5=C5_fork,C6=C6_registry)
for name,(g,o) in S.items():
    print("==",name)
    for cn,f in C.items():
        st,n=f(g,o); n=n if isinstance(n,(str,list)) else ""
        print(f"   {cn}: {st:13s} {str(n)[:150]}")
# A1 detail for C1: is gov's new flag present?
g,o=S["A1 gov changes amended item"]; st,items=C1_override(g,o); print("C1 A1 args after compose:",items["item.test.run-legs"]["args"])
P
python3 -I "$S/lgscripts/govmodel.py"
````

50. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/flowprobe"; ls "$S/lgscripts"; wc -l "$S/lgscripts/govmodel.py" 2>/dev/null
````

51. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/flowprobe"; cat > "$S/lgscripts/govmodel.py" <<'EOF_PY'
"""Throwaway model of the declared gov flow and roles, composed with an adopter overlay by each candidate mechanism.
status: LOUD (composition refuses or orders), SILENT-WRONG, OK, IMPOSSIBLE."""
import copy, hashlib, json
H=lambda d: hashlib.sha256(json.dumps(d,sort_keys=True).encode()).hexdigest()[:8]
def gov_v1():
    it={
     "item.build.implement":dict(actor="role.builder",inputs={},outputs={"diff":"patch"},requires=[],witness="commit-sha",routes={"done":"item.test.run-legs"}),
     "item.test.run-legs":dict(actor="command",inputs={"diff":"patch"},outputs={"verdict":"verdict"},requires=["item.build.implement"],witness="leg-log",routes={"green":"item.deploy.release"},args=["--packs=core"]),
     "item.deploy.release":dict(actor="command",inputs={"verdict":"verdict"},outputs={},requires=["item.test.run-legs"],witness="tag",routes={}),
    }
    roles={"role.builder":dict(shapes=["single","per-unit"]),"role.reviewer":dict(shapes=["single","panel"])}
    return dict(items=it,roles=roles,fixed={"item.test.run-legs"})
V1=gov_v1()
def overlay(**kw):
    o=dict(add_items={"item.repo.license-scan":dict(actor="command",inputs={"diff":"patch"},outputs={},requires=["item.build.implement"],witness="scan-log",routes={})},
           amend={"item.test.run-legs":dict(base=H(V1["items"]["item.test.run-legs"]),set={"args":["--packs=core,repo"]})},
           disable=[],add_roles={},spawn=[])
    o.update(kw); return o
def check_graph(items,typed=True):
    errs=[]
    for t,d in items.items():
        for r in d["requires"]:
            if r not in items: errs.append(t+" requires unknown "+r)
        if typed and d["requires"]:
            for k,ty in d["inputs"].items():
                prov=[items[x]["outputs"].get(k) for x in d["requires"] if x in items]
                if prov and ty not in prov: errs.append(t+" input "+k+":"+ty+" not provided, got "+str(prov))
    return errs
def C1_override(gov,o):
    items=copy.deepcopy(gov["items"]); items.update(copy.deepcopy(o["add_items"]))
    for t,a in o["amend"].items(): items.setdefault(t,{"requires":[],"inputs":{},"outputs":{}}).update(a["set"])
    for t in o["disable"]: items[t]["enabled"]=False
    live={t:d for t,d in items.items() if d.get("enabled",True)}
    errs=[e for e in check_graph(items,typed=False)]
    missing=[t for t,d in live.items() if any(r in items and not items[r].get("enabled",True) for r in d["requires"])]
    if errs: return ("LOUD",errs)
    if missing: return ("SILENT-WRONG","dependents run without their input: "+str(missing))
    return ("OK",items)
def C2_slots(gov,o):
    if o["amend"] or o["disable"]: return ("IMPOSSIBLE","no way to change a shipped item")
    return ("OK",None)
def C3_graph(gov,o):
    items=copy.deepcopy(gov["items"]); items.update(copy.deepcopy(o["add_items"]))
    for t in o["disable"]: items.pop(t,None)
    for t,a in o["amend"].items():
        if t in items: items[t].update(a["set"])
    errs=check_graph(items,typed=True)
    return ("LOUD",errs) if errs else ("OK",items)
def C4_pinned_overlay(gov,o):
    errs=[]; items=copy.deepcopy(gov["items"])
    for t,d in o["add_items"].items():
        if not d.get("witness"): errs.append(t+": no witness (item schema)")
        items[t]=copy.deepcopy(d)
    for t,a in o["amend"].items():
        if t not in items: errs.append("amend "+t+": target gone (orphan edge)")
        elif H(gov["items"][t])!=a["base"]: errs.append("amend "+t+": stale pin "+a["base"]+"->"+H(gov["items"][t]))
        else: items[t].update(a["set"])
    for t in o["disable"]:
        if t in gov["fixed"]: errs.append("disable "+t+": in the fixed set")
        else:
            deps=[x for x,d in items.items() if t in d["requires"]]
            if deps: errs.append("disable "+t+": required by "+str(deps))
            items.pop(t,None)
    errs+=check_graph(items,typed=True)
    roles=dict(gov["roles"]); roles.update(o["add_roles"])
    for role,shape in o["spawn"]:
        if role not in roles: errs.append("spawn "+role+": unregistered")
        elif shape not in roles[role]["shapes"]: errs.append("spawn "+role+" in "+shape+": role does not declare that shape")
    return ("LOUD",errs) if errs else ("OK",items)
def C5_fork(gov,o):
    return ("SILENT-WRONG" if gov is not V1 else "OK","adopter runs its v1 copy; the upstream change never arrives")
def C6_registry(gov,o):
    roles=dict(gov["roles"]); roles.update(o["add_roles"])
    for role,shape in o["spawn"]:
        if role not in roles: return ("LOUD-AT-RUN","NotFound "+role+" at dispatch")
        return ("OK-UNCHECKED","shape "+shape+" never consulted")
    return ("OK","")
def v2(mut):
    g=copy.deepcopy(V1); mut(g); return g
S={}
S["A1 gov changes amended item"]=(v2(lambda g:g["items"]["item.test.run-legs"].update(args=["--packs=core","--require-sbom"])), overlay())
def ren(g):
    d=g["items"].pop("item.build.implement"); g["items"]["item.build.write"]=d
    g["items"]["item.test.run-legs"]["requires"]=["item.build.write"]
S["A2 gov renames item adopter depends on"]=(v2(ren), overlay(amend={}))
def ren_amended(g):
    d=g["items"].pop("item.test.run-legs"); g["items"]["item.test.legs"]=d
    g["items"]["item.deploy.release"]["requires"]=["item.test.legs"]
S["A2b gov renames item adopter amended"]=(v2(ren_amended), overlay())
def add_before_type(g):
    g["items"]["item.build.vendor-prep"]=dict(actor="command",inputs={},outputs={"diff":"patch-set"},requires=[],witness="x",routes={})
    g["items"]["item.build.implement"]["outputs"]={"diff":"patch-set"}
    g["items"]["item.test.run-legs"]["inputs"]={"diff":"patch-set"}
S["A3a gov adds earlier item, input TYPE changes"]=(v2(add_before_type), overlay(amend={}))
def add_before_meaning(g):
    g["items"]["item.build.vendor-prep"]=dict(actor="command",inputs={},outputs={},requires=[],witness="x",routes={},note="strips vendored paths before implement emits diff")
S["A3b gov adds earlier item, input MEANING changes"]=(v2(add_before_meaning), overlay(amend={}))
S["A4 adopter disables fixed-set item"]=(V1, overlay(amend={},disable=["item.test.run-legs"]))
S["A4b adopter disables a required non-fixed item"]=(V1, overlay(amend={},add_items={},disable=["item.build.implement"]))
S["A5 adopter item has no witness"]=(V1, overlay(amend={},add_items={"item.repo.x":dict(actor="command",inputs={},outputs={},requires=[],witness=None,routes={})}))
S["A6 adopter role in a shape it does not declare"]=(V1, overlay(amend={},add_roles={"role.repo.auditor":dict(shapes=["single"])},spawn=[("role.repo.auditor","panel")]))
S["A6b role never registered"]=(V1, overlay(amend={},spawn=[("role.repo.ghost","panel")]))
C=dict(C1=C1_override,C2=C2_slots,C3=C3_graph,C4=C4_pinned_overlay,C5=C5_fork,C6=C6_registry)
for name,(g,o) in S.items():
    print("==",name)
    for cn,f in C.items():
        st,n=f(g,o); n=n if isinstance(n,(str,list)) else ""
        print("   %s: %-13s %s"%(cn,st,str(n)[:140]))
g,o=S["A1 gov changes amended item"]; st,items=C1_override(g,o); print("C1 on A1, composed args:",items["item.test.run-legs"]["args"])
g,o=S["A2b gov renames item adopter amended"]; st,items=C1_override(g,o); print("C1 on A2b, stub item created:",items.get("item.test.run-legs"))
EOF_PY
python3 -I "$S/lgscripts/govmodel.py"
````

52. Bash

````text
S="C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/flowprobe"; cat > "$S/lgscripts/pinprobe.py" <<'EOF_PY'
import copy, hashlib, json
H=lambda d: hashlib.sha256(json.dumps(d,sort_keys=True).encode()).hexdigest()[:8]
v1=dict(actor="command",witness="leg-log",args=["--packs=core"],routes={"green":"release"})
amend={"field":"args","set":["--packs=core,repo"]}
whole=H(v1); field=H(v1["args"])
cases={"unrelated field (witness) changes":dict(v1,witness="leg-log+sha"),
       "amended field changes":dict(v1,args=["--packs=core","--require-sbom"]),
       "route added":dict(v1,routes={"green":"release","flaky":"rerun"})}
for k,v2 in cases.items():
    print("%-36s whole-decl pin: %-5s field pin: %s"%(k,"RED" if H(v2)!=whole else "green","RED" if H(v2["args"])!=field else "green"))
EOF_PY
python3 -I "$S/lgscripts/pinprobe.py"
````
