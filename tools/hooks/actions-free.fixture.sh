#!/usr/bin/env bash
# actions-free.fixture.sh — the actions.free arm (KICK-dKeptSession-8 S8) over one planted case.
#
#   bash actions-free.fixture.sh --plant <case>
#
# Builds a scratch repository under the host temp directory holding the build tFix with one routed
# Tier-2 INPROGRESS unit and a .memory-tree.conf whose ROUTED_PATHS holds the Edit's target; a card file
# at .claude/orientation-card.md whose card-owner line names the payload's session, whose route names
# tFix and whose ## pointers the case writes; copies of scratch-guard.js and agent-cap.js at the path
# this file's own directory has under its checkout; and two stubs where agent-cap.js's resolveKitDir
# probes beside that directory, their directories derived from it, never spelled: the policy kit's
# reader, answering actions.free with the planted value (or, for `refusal`, throwing a PolicyRefusal),
# runtime.agents-in-flight with 2 and refusing any other key; and the kickoff checker, answering
# --card --path with a session card holding a real READY line, a tree line naming the scratch
# repository and the same route, so the orientation check admits the commit and the write gate the
# Edit before the arm runs. The scratch's .claude/settings.json sets both variables rule 7 reads to 2,
# and GOV_SETTINGS_JSON and CLAUDE_PROJECT_DIR are unset for every call, so rule 7 admits before rule 9.
#
# Each call pipes one payload to one hook copy and prints one line:
#   <case> · <value> · <call> · exit <code> · <stderr, its lines joined by ' ¶ ', or (empty stderr)>
# and `anything-none` prints one more, `<case> · <value> · log · <n> line(s) · <the log's lines>`.
# The cases:
#   probes-none  read-only-probes, item none: git status, echo x > f, git commit -m x, git push, an Edit
#   probes-item  an instance key: the four acts of probes-none under each of the three values
#   reads-none   item-reads-only, item none: git status and the two boundary commands
#   anything-none recorded-anything, item none: echo x > f and git status, then the log
#   spawn-none   read-only-probes, item none: an Agent payload to agent-cap.js
#   spawn-item   the same with an instance key
#   no-pointers  a card file with no ## pointers: echo x > f
#   no-route     ## pointers and no route: echo x > f
#   other-owner  ## pointers, card-owner naming another session: echo x > f
#   throw        a directory at the card file's path: echo x > f
#   no-helper    no policy reader beside the hooks: echo x > f
#   refusal      the policy reader throws a PolicyRefusal: echo x > f
# Exit 0 once every call of the case ran; 2 on a usage error or a scratch repository that could not
# be built. It judges nothing: the hooks kit's suites read its lines. WHAT IT DOES NOT DO: run any
# payload's command, or read the real policy or kickoff kits.
set -u
[ "${1:-}" = --plant ] && [ -n "${2:-}" ] || { echo "actions-free.fixture: usage: bash actions-free.fixture.sh --plant <case>"; exit 2; }
PLANT=$2
case $PLANT in
  probes-none|probes-item|reads-none|anything-none|spawn-none|spawn-item|no-pointers|no-route|other-owner|throw|no-helper|refusal) ;;
  *) echo "actions-free.fixture: no case $PLANT"; exit 2 ;;
esac
HERE=.; [[ $0 == */* ]] && HERE=${0%/*}
HERE="$(cd "$HERE" && pwd)"
KIT_REL=$(git -C "$HERE" rev-parse --show-prefix 2>/dev/null) || { echo "actions-free.fixture: $HERE is in no git checkout"; exit 2; }
KIT_REL=${KIT_REL%/}
case $KIT_REL in */*) PARENT=${KIT_REL%/*}/ ;; *) PARENT="" ;; esac
TMP=$(mktemp -d) || { echo "actions-free.fixture: no scratch directory"; exit 2; }
trap 'rm -rf "$TMP"' EXIT
R="$TMP/r"
HOOKS="$R${KIT_REL:+/$KIT_REL}"
POLICY_DIR="$R/${PARENT}policy"
SID=tFixSession-1
SPEC=memory/builds/tFix/spec/2026-01-01-spec-TOOL-tFix-1.md
KEY=item.build.base@TOOL-tFix-1#aaaa0001

{ mkdir -p "$R/src" "$R/.claude" "$R/memory/builds/tFix/spec" "$HOOKS" "$POLICY_DIR" "$R/${PARENT}session-kickoff" \
  && git -C "$R" init -q \
  && printf 'a\n' > "$R/src/a.js" \
  && git -C "$R" add src/a.js \
  && git -C "$R" -c user.name=f -c user.email=f@f -c commit.gpgsign=false commit -q -m seed \
  && cp "$HERE/scratch-guard.js" "$HERE/agent-cap.js" "$HOOKS/"; } >/dev/null 2>&1 \
  || { echo "actions-free.fixture: the scratch repository under $TMP could not be built"; exit 2; }
AT=$(git -C "$R" rev-parse --short=8 HEAD | tr -d '\r')
TOP=$(cd "$R" && { pwd -W 2>/dev/null || pwd; })
printf 'MEMORY_ROOT="memory"\nROUTED_PATHS="src/"\n' > "$R/.memory-tree.conf"
printf '# TOOL-tFix-1 — the fixture unit\n\n**Status:** INPROGRESS · Tier-2\n' > "$R/$SPEC"
printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"2","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"2"}}\n' > "$R/.claude/settings.json"
mkdir -p "$R/.git/orientation"
printf 'tree — %s\n## route\n- build: tFix\n- unit: TOOL-tFix-1 · spec %s\nREADY — tFix\n' "$TOP" "$SPEC" > "$R/.git/orientation/$SID.md"
printf '%s\n' '[ "${1:-} ${2:-} ${3:-}" = "--card --path --session" ] || exit 2' \
  'd=$(git rev-parse --path-format=absolute --git-common-dir) || exit 1' \
  'echo "$d/orientation/$4.md"' > "$R/${PARENT}session-kickoff/manifest-check.sh"
if [ "$PLANT" != no-helper ]; then
  printf '%s\n' "'use strict'" \
    '// The fixture'"'"'s policy reader: actions.free from value.txt beside it, the agent limit 2, nothing else.' \
    'const fs = require('"'"'fs'"'"')' \
    'const path = require('"'"'path'"'"')' \
    'class PolicyRefusal extends Error {}' \
    'function readPolicy(key) {' \
    '  if (key === '"'"'actions.free'"'"') {' \
    '    const v = fs.readFileSync(path.join(__dirname, '"'"'value.txt'"'"'), '"'"'utf8'"'"').trim()' \
    '    if (v === '"'"'refusal'"'"') throw new PolicyRefusal('"'"'policy refused: the fixture plants a refusal of actions.free'"'"')' \
    '    return { value: v }' \
    '  }' \
    '  if (key === '"'"'runtime.agents-in-flight'"'"') return { value: 2 }' \
    '  throw new Error('"'"'the fixture policy reader answers no key '"'"' + key)' \
    '}' \
    'module.exports = { readPolicy, PolicyRefusal }' > "$POLICY_DIR/policy-mirror.js"
fi

# write_fixture_card <owner> <pointer value, or - for no ## pointers> [noroute]
write_fixture_card() {
  { printf '[.claude/orientation-card.md · Level 1 · a fixture direction]\ncard-owner — %s · fixture\n' "$1"
    [ "${3:-}" = noroute ] || printf '## route\n- build: tFix\n- unit: TOOL-tFix-1 · spec %s\n' "$SPEC"
    [ "$2" = - ] || printf '## pointers\nitem — %s · at %s\n' "$2" "$AT"
    printf 'READY — tFix\n[/.claude/orientation-card.md]\n'; } > "$R/.claude/orientation-card.md"
}
# write_fixture_value <value>: what the policy reader answers for actions.free
write_fixture_value() { [ -d "$POLICY_DIR" ] && printf '%s\n' "$1" > "$POLICY_DIR/value.txt"; return 0; }

# run_fixture_call <value shown> <call label> <hook file> <tool> <command, or the Edit's target>
run_fixture_call() {
  local payload code err
  payload=$(node -e '
    const [tool, arg, sid, cwd] = process.argv.slice(1)
    const d = { hook_event_name: "PreToolUse", tool_name: tool, session_id: sid, cwd }
    if (tool === "Edit") d.tool_input = { file_path: arg, old_string: "a", new_string: "b" }
    else if (tool === "Agent") d.tool_input = { subagent_type: "general-purpose", description: "a fixture spawn", prompt: arg }
    else d.tool_input = { command: arg }
    process.stdout.write(JSON.stringify(d))' "$4" "$5" "$SID" "$TOP")
  err=$(printf '%s' "$payload" | (cd "$R" && env -u CLAUDE_PROJECT_DIR -u GOV_SETTINGS_JSON node "$HOOKS/$3" 2>&1 >/dev/null)); code=$?
  err=$(printf '%s' "$err" | tr -d '\r' | awk 'NF { printf "%s%s", (n++ ? " ¶ " : ""), $0 }')
  printf '%s · %s · %s · exit %s · %s\n' "$PLANT" "$1" "$2" "$code" "${err:-(empty stderr)}"
}
# run_fixture_acts <value>: the four acts AC1 refuses at item none
run_fixture_acts() {
  run_fixture_call "$1" 'echo x > f' scratch-guard.js Bash 'echo x > f'
  run_fixture_call "$1" 'git commit -m x' scratch-guard.js Bash 'git commit -m x'
  run_fixture_call "$1" 'git push' scratch-guard.js Bash 'git push'
  run_fixture_call "$1" 'Edit src/a.js' scratch-guard.js Edit "$TOP/src/a.js"
}

case $PLANT in
  probes-none)
    write_fixture_card "$SID" none; write_fixture_value read-only-probes
    run_fixture_call read-only-probes 'git status' scratch-guard.js Bash 'git status'
    run_fixture_acts read-only-probes ;;
  probes-item)
    write_fixture_card "$SID" "$KEY"
    for v in read-only-probes item-reads-only recorded-anything; do write_fixture_value "$v"; run_fixture_acts "$v"; done ;;
  reads-none)
    write_fixture_card "$SID" none; write_fixture_value item-reads-only
    run_fixture_call item-reads-only 'git status' scratch-guard.js Bash 'git status'
    run_fixture_call item-reads-only 'position.py --boundary' scratch-guard.js Bash 'python position.py tFix --boundary none'
    run_fixture_call item-reads-only 'manifest-check.sh --card --boundary' scratch-guard.js Bash "bash manifest-check.sh --card --boundary --build tFix --session $SID" ;;
  anything-none)
    write_fixture_card "$SID" none; write_fixture_value recorded-anything
    run_fixture_call recorded-anything 'echo x > f' scratch-guard.js Bash 'echo x > f'
    run_fixture_call recorded-anything 'git status' scratch-guard.js Bash 'git status'
    log="$R/.git/gov-free-actions.log"
    n=0; [ -f "$log" ] && n=$(grep -c . "$log")
    printf '%s · recorded-anything · log · %s line(s) · %s\n' "$PLANT" "$n" "$( [ -f "$log" ] && tr -d '\r' < "$log" | awk 'NF { printf "%s%s", (n++ ? " ¶ " : ""), $0 }' )" ;;
  spawn-none|spawn-item)
    if [ "$PLANT" = spawn-none ]; then write_fixture_card "$SID" none; else write_fixture_card "$SID" "$KEY"; fi
    write_fixture_value read-only-probes
    run_fixture_call read-only-probes 'Agent' agent-cap.js Agent 'a fixture prompt' ;;
  no-pointers)
    write_fixture_card "$SID" -; write_fixture_value read-only-probes
    run_fixture_call read-only-probes 'echo x > f' scratch-guard.js Bash 'echo x > f' ;;
  no-route)
    write_fixture_card "$SID" none noroute; write_fixture_value read-only-probes
    run_fixture_call read-only-probes 'echo x > f' scratch-guard.js Bash 'echo x > f' ;;
  other-owner)
    write_fixture_card tFixOther-2 none; write_fixture_value read-only-probes
    run_fixture_call read-only-probes 'echo x > f' scratch-guard.js Bash 'echo x > f' ;;
  throw)
    mkdir -p "$R/.claude/orientation-card.md"; write_fixture_value read-only-probes
    run_fixture_call read-only-probes 'echo x > f' scratch-guard.js Bash 'echo x > f' ;;
  no-helper)
    write_fixture_card "$SID" none
    run_fixture_call '(no policy reader)' 'echo x > f' scratch-guard.js Bash 'echo x > f' ;;
  refusal)
    write_fixture_card "$SID" none; write_fixture_value refusal
    run_fixture_call '(a PolicyRefusal)' 'echo x > f' scratch-guard.js Bash 'echo x > f' ;;
esac
exit 0
