#!/usr/bin/env bash
# card-store.fixture.sh — the build card over a scratch repository (TOOL-dPlacedRequest-2 S12): its
# publish at READY, its three stores, its follow at a stage move, its snapshot record, its lookup on
# another clone and the replay's resume lines, each case one observation of the kickoff engine beside
# this file.
#
#   bash card-store.fixture.sh --plant <case>    # one case: exit 0 when its observation holds, 1 when not
#   bash card-store.fixture.sh --list            # the cases, one per line
#
# Each case builds, in the system temp directory, a bare remote and a repository pushed to it, holding
# the build `tFix` (one spec, one brief), the memory-tree, loop and unattended kits copied from the tree
# this file sits in at the paths the engine's own resolver finds them, a `.unattended.conf` with
# RUN_CLAIMS on, so the driver writes the card's ref (TOOL-dPlacedRequest-33), a stub policy kit answering the case's
# planted values from a file outside the repository, a stub playbook kit whose `pockets` verb
# prints one fact, and the copied loop kit's `position.py` replaced by a stub answering from a second
# planted file, CARD_STUB_POSITION, so no case runs the real engine (KICK-dKeptSession-13 S9): `<slug>
# --boundary <pointer>` the planted `key`, `answer` and `forked` units, and `<slug> --json` the planted
# `json` and `rc`, each after the planted `delay`; and its `budget.py` replaced by a stub answering `state
# --build <slug>` with the planted `budget` from that same file, `open 0/4` where none is planted, so no case
# runs the real module either (KICK-dKeptSession-26 S4). The engine writes the session card `t1`, appends a READY body with a `## route`
# naming `tFix`, and the case runs its verbs and prints one `card-store: <case> · <what> · held|MISSED`
# line per observation. The scratch tree is removed at exit. The card-import fixture's verdict
# (KICK-dKeptSession-12) is planted in its file, or recorded by `--card --fixture-run` over a stub
# fixture named by CARD_FIXTURE; those cases and every `context-` case export one `AI_AGENT`, or unset
# it where the case says so, and the cases that record one or replay a recorded pass put a stub `claude`
# first on PATH, whose version the verdict records (KICK-dKeptSession-37) and its reader compares
# (KICK-dKeptSession-38), so no outcome reads the version of the session or the node running the suite.
# Exit 2 is a usage error, or a fixture that could not be built.
# WHAT THIS DOES NOT CHECK: a remote other than a local bare one; a lost compare-and-swap, which needs
# two writers between one read and its push; the engine's other cells, which their own arms cover; the
# real card-compaction.fixture.sh, which starts harness sessions and is never run here.
set -u
case "$0" in */*) HERE=${0%/*} ;; *) HERE=. ;; esac
HERE=$(CDPATH= cd -- "$HERE" && pwd) || exit 2
CHECK="$HERE/manifest-check.sh"
PLANTS="render publish publish-off publish-unwritten publish-late publish-hung store-remote store-local store-folder store-empty follow-rerender follow-per-step
follow-fixed snapshot-terminal snapshot-every lookup lookup-offline lookup-upstream lookup-hung replay context-idle context-always-resume
context-always-fresh context-fixture-red context-transcript-absent partial-continue partial-restart
partial-ask terminal-route close-follow-twice follow-offline-publish follow-offline-publish-online
follow-foreign-after-cached follow-foreign-after-offline fixture-stale fixture-run fixture-run-cli worktree-named replay-order
fixture-cli-path-differs fixture-cli-unknown pointers-render pointers-boundary pointers-at-transitions pointers-cap pointers-replay
budget-open budget-spent budget-unfrozen budget-omitted budget-no-kit"
REF=refs/gov/builds/tFix/card
SPEC=memory/builds/tFix/spec/2026-01-01-spec-TOOL-tFix-1.md
BRIEF=memory/builds/tFix/prompts/2026-01-01-prompt-TOOL-tFix-1-brief.md

case "${1:-}" in
  --list) printf '%s\n' $PLANTS; exit 0 ;;
  --plant) PLANT=${2:-} ;;
  *) echo "usage: card-store.fixture.sh --plant <case> | --list"; exit 2 ;;
esac
case " ${PLANTS//$'\n'/ } " in *" $PLANT "*) ;; *) echo "card-store: no case '$PLANT'; --list names them"; exit 2 ;; esac

# The engine's own resolvers, read out of it, so no kit's path is spelled here.
eval "$(sed -n '/^# >>> resolve_python /,/^# <<< resolve_python$/p' "$CHECK")"
eval "$(awk '/^resolve_kit_dir\(\) \{$/,/^}$/' "$CHECK")"
eval "$(awk '/^resolve_kit_file\(\) \{$/,/^}$/' "$CHECK")"
GOVROOT=$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || { echo "card-store: $HERE is in no repository"; exit 2; }
PY=$(resolve_python 2>/dev/null) || { echo "card-store: no Python resolves on this node"; exit 2; }

S=$(mktemp -d "${TMPDIR:-/tmp}/cardstore.XXXXXX") || { echo "card-store: no scratch directory under ${TMPDIR:-/tmp}"; exit 2; }
trap 'rm -rf "$S"' EXIT
# Hermetic: no global or system git config reaches a case, so a node's hooks path, line-ending
# conversion or signing cannot move what it observes; the repository's own config is set below.
: > "$S/gitconfig"; export GIT_CONFIG_GLOBAL="$S/gitconfig" GIT_CONFIG_NOSYSTEM=1
R="$S/repo"; O="$S/origin.git"; OUT="$S/out"
# The fixture repository's one remote, named apart from any real one: kit code names no remote by literal
# (check-remote-literals.sh), and the driver reads a repository of one remote through the ladder's only-remote rung.
FX_REMOTE=upstream
export CARD_STUB_POLICY="$S/policy.txt" CARD_STUB_POSITION="$S/position.txt"
MISSED=0
# Two item keys in the engine's instance shape, `<item tag>@<pass>#<inputs>`.
K1=item.build.base@TOOL-tFix-1#aaaa0001; K2=item.build.base@TOOL-tFix-1#aaaa0002

# print_card_held <what> <0 held | else missed>
print_card_held() {
  if [ "$2" = 0 ]; then printf 'card-store: %s · %s · held\n' "$PLANT" "$1"
  else printf 'card-store: %s · %s · MISSED\n' "$PLANT" "$1"; sed 's/^/    /' "$OUT"; MISSED=1; fi
}
# set_card_policy <key> <value, a set comma-joined, empty for the empty set>
set_card_policy() {
  local t; t=$(mktemp "$CARD_STUB_POLICY.XXXXXXXX") || exit 2
  grep -v "^$1=" "$CARD_STUB_POLICY" > "$t" 2>/dev/null; mv -f "$t" "$CARD_STUB_POLICY"
  printf '%s=%s\n' "$1" "$2" >> "$CARD_STUB_POLICY"
}
# set_card_position <key|answer|forked|json|rc|delay> <value> — the stub position engine's planted answer.
set_card_position() {
  local t; t=$(mktemp "$CARD_STUB_POSITION.XXXXXXXX") || exit 2
  grep -v "^$1=" "$CARD_STUB_POSITION" > "$t" 2>/dev/null; mv -f "$t" "$CARD_STUB_POSITION"
  printf '%s=%s\n' "$1" "$2" >> "$CARD_STUB_POSITION"
}
# run_card_engine <tree> <engine args…> — stdin closed, stdout and stderr to $OUT; the engine's exit.
run_card_engine() {
  local t=$1; shift
  (cd "$t" && bash "$CHECK" "$@" </dev/null) > "$OUT" 2>&1
}
# read_ref_card <git dir or tree> — the card a card ref's tip carries, every message line after the
# fifth, less the blank line `%B` closes with.
read_ref_card() {
  git -C "$1" log -1 --format=%B "$REF" -- 2>/dev/null | tr -d '\r' \
    | awk 'NR > 5 { l[++n] = $0 } END { while (n > 0 && l[n] == "") n--; for (i = 1; i <= n; i++) print l[i] }'
}
# measure_card_records <tree> — the build's card records.
measure_card_records() { ls "$1/memory/builds/tFix/build/" 2>/dev/null | grep -c -- '-card-[0-9]*\.md$'; }
# set_card_verdict <verdict> <blob8> <cli> — the card-import fixture's recorded verdict, planted in the
# writer's grammar where the engine's reader finds it.
set_card_verdict() {
  local at; printf -v at '%(%Y-%m-%dT%H:%M:%S%z)T' -1
  mkdir -p "$R/.git/orientation" \
    && printf 'card-fixture — %s · fixture %s · cli %s · %s\n' "$1" "$2" "$3" "$at" > "$R/.git/orientation/card-fixture.verdict"
}
# write_claude_stub <script body> — a stub `claude` at $S/clibin, that dir first on PATH, whose version
# the fixture's verdict records (KICK-dKeptSession-37 S2). The PATH entry is the POSIX spelling: a
# drive-letter one's colon splits PATH, and the node's own `claude` answers instead of the stub.
write_claude_stub() {
  local d="$S/clibin"
  { mkdir -p "$d" && printf '#!/usr/bin/env bash\n%s\n' "$1" > "$d/claude" && chmod +x "$d/claude"; } \
    || { echo "card-store: no stub claude could be written under $d"; exit 2; }
  command -v cygpath >/dev/null 2>&1 && d=$(cygpath -u "$d")
  case ":$PATH:" in *":$d:"*) ;; *) export PATH="$d:$PATH" ;; esac
}

# The scratch repository: its build, the copied kits and the two stubs, committed and pushed.
write_card_fixture() {
  local f rel
  git init -q --bare "$O" && git init -q "$R" || return 1
  git -C "$R" config user.email fixture@test && git -C "$R" config user.name fixture \
    && git -C "$R" config commit.gpgsign false && git -C "$R" config core.autocrlf false \
    && mkdir -p "$S/hooks" && git -C "$R" config core.hooksPath "$S/hooks" || return 1
  for f in "memory-tree corpus_ids.py" "loop loop_transition.py" "unattended unattended.sh"; do
    f=$(ROOT="$GOVROOT" MC_DIR="$HERE" resolve_kit_file $f); [ -n "$f" ] || return 1
    rel=${f#"$GOVROOT"/}; rel=${rel%/*}
    mkdir -p "$R/$rel" && cp -R "$GOVROOT/$rel/." "$R/$rel/" || return 1
  done
  # The stub position engine over the copied one: nothing a plant runs imports a name from it.
  f=$(ROOT="$GOVROOT" MC_DIR="$HERE" resolve_kit_file loop position.py); [ -n "$f" ] || return 1
  f="$R/${f#"$GOVROOT"/}"; [ -f "$f" ] || return 1
  printf '%s\n' 'import os, sys, time' \
    'sys.stdout.reconfigure(encoding="utf-8")' \
    'vals = dict(l.rstrip("\n").partition("=")[::2] for l in open(os.environ["CARD_STUB_POSITION"], encoding="utf-8") if "=" in l)' \
    'time.sleep(float(vals.get("delay") or 0))' \
    'if len(sys.argv) == 4 and sys.argv[2] == "--boundary":' \
    '    p, key, answer = sys.argv[3], vals.get("key") or "none", vals.get("answer") or "act"' \
    '    if answer in ("stale-remote", "invalid-input"):' \
    '        print("boundary — none crossed · item %s · %s" % (p, answer))' \
    '    elif key == p:' \
    '        print("boundary — none crossed · item %s" % p)' \
    '    else:' \
    '        print("boundary — %s → %s" % (p, key))' \
    '    print("forked — %s" % (" · ".join(u for u in (vals.get("forked") or "").split(",") if u) or "none"))' \
    '    sys.exit(2 if answer == "invalid-input" else 0)' \
    'if len(sys.argv) == 3 and sys.argv[2] == "--json":' \
    '    print(vals.get("json") or "{}")' \
    '    sys.exit(int(vals.get("rc") or 0))' \
    'sys.exit("stub position: <slug> --boundary <pointer> or <slug> --json, and was asked %s" % sys.argv[1:])' > "$f"
  # The stub rework budget over the copied one (KICK-dKeptSession-26 S4): no card path imports a name from it.
  f=$(ROOT="$GOVROOT" MC_DIR="$HERE" resolve_kit_file loop budget.py); [ -n "$f" ] || return 1
  f="$R/${f#"$GOVROOT"/}"; [ -f "$f" ] || return 1
  printf '%s\n' 'import os, sys' \
    'sys.stdout.reconfigure(encoding="utf-8")' \
    'vals = dict(l.rstrip("\n").partition("=")[::2] for l in open(os.environ["CARD_STUB_POSITION"], encoding="utf-8") if "=" in l)' \
    'if sys.argv[1:3] == ["state", "--build"] and len(sys.argv) == 4:' \
    '    print(vals.get("budget") or "open 0/4")' \
    '    sys.exit(0)' \
    'sys.exit("stub budget: state --build <slug>, and was asked %s" % sys.argv[1:])' > "$f"
  : > "$CARD_STUB_POSITION"
  f=$(ROOT="$GOVROOT" MC_DIR="$HERE" resolve_kit_file policy policy.py); [ -n "$f" ] || return 1
  rel=${f#"$GOVROOT"/}; mkdir -p "$R/${rel%/*}"
  printf '%s\n' 'import os, sys' \
    'vals = dict(l.rstrip("\n").partition("=")[::2] for l in open(os.environ["CARD_STUB_POLICY"], encoding="utf-8") if "=" in l)' \
    'if len(sys.argv) != 3 or sys.argv[1] != "get" or sys.argv[2] not in vals:' \
    '    sys.exit("stub policy: get <a planted key>, and was asked %s" % sys.argv[1:])' \
    'if vals[sys.argv[2]] == "":' \
    '    sys.exit("policy: refused · %s is the empty set, and its row says empty = never" % sys.argv[2])' \
    'print("\n".join(vals[sys.argv[2]].split(",")))' > "$R/$rel"
  f=$(ROOT="$GOVROOT" MC_DIR="$HERE" resolve_kit_file playbook instruction_units.py); [ -n "$f" ] || return 1
  rel=${f#"$GOVROOT"/}; mkdir -p "$R/${rel%/*}"
  printf '%s\n' 'import sys' 'if sys.argv[1:2] == ["pockets"]:' '    print("## pockets\n- the fixture fact")' > "$R/$rel"
  printf '%s\n' 'MEMORY_ROOT=memory' 'FAMILIES="tooling:TOOL"' 'DISCIPLINES="tooling"' > "$R/.memory-tree.conf"
  printf 'RUN_CLAIMS="on"\n' > "$R/.unattended.conf"
  printf '__pycache__/\n' > "$R/.gitignore"
  mkdir -p "$R/memory/builds/tFix/spec" "$R/memory/builds/tFix/prompts" "$R/memory/builds/tFix/build"
  printf '# TOOL-tFix-1 — the fixture unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01 · node a · Tier-1\n' > "$R/$SPEC"
  printf '**Serves:** research TOOL-tFix-1\n\n# Brief — tFix: the fixture build\n' > "$R/$BRIEF"
  : > "$CARD_STUB_POLICY"
  set_card_policy card.store remote-ref,build-folder,local-clone
  set_card_policy card.follows re-render-at-transition
  set_card_policy card.snapshot terminal-only
  set_card_policy card.pointers every-item
  set_card_policy resume.context fresh-when-idle
  set_card_policy resume.partial continue-item
  git -C "$R" add -A && ! git -C "$R" diff --cached --quiet && git -C "$R" commit -q -m "fixture: the build tFix" \
    && git -C "$R" branch -M main && git -C "$R" remote add "$FX_REMOTE" "$O" \
    && git -C "$R" push -q "$FX_REMOTE" main 2>/dev/null || return 1
  run_card_engine "$R" --card --write --session t1
}

# write_card_body <file> <ready 0|1> — the kickoff body: its task, the route naming tFix and its READY line.
write_card_body() {
  {
    if [ "$2" = 1 ]; then printf '## task\n'; bash "$CHECK" --task-skeleton | sed 's/…/the fixture'"'"'s value/'; fi
    printf '## route\n- build: tFix\n- unit: TOOL-tFix-1 · spec %s\n- brief: %s\n' "$SPEC" "$BRIEF"
    [ "$2" = 0 ] || printf 'READY — tFix · node a · main · base %s · Tier-1 · gates none\n' "$(git -C "$R" rev-parse --short=12 HEAD)"
  } > "$1"
}
# write_card_records — AC1's build: two journal records a day apart, one spec-audit record and a second
# spec, TOOL-tFix-2, the unit the stub engine grades FORKED, committed; and the memory root's LIVE.md, which
# the session card's `live —` cell names absent, so `--card --check` finds that path tracked.
write_card_records() {
  printf '# LIVE\n' > "$R/memory/LIVE.md"
  printf '**Serves:** journal TOOL-tFix-1\n\n# the older journal\n' > "$R/memory/builds/tFix/build/2026-01-01-build-TOOL-tFix-1-agent-ledger.md"
  printf '**Serves:** journal TOOL-tFix-1\n\n# the newer journal\n' > "$R/memory/builds/tFix/build/2026-01-02-build-TOOL-tFix-1-agent-ledger.md"
  mkdir -p "$R/memory/builds/tFix/reviews"
  printf '## Verdict: CLEAN\n\n**Serves:** spec-audit TOOL-tFix-1@rev-1\n' > "$R/memory/builds/tFix/reviews/2026-01-01-review-TOOL-tFix-1-spec-audit.md"
  printf '# TOOL-tFix-2 — the forked unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01 · node a · Tier-1\n' > "$R/memory/builds/tFix/spec/2026-01-01-spec-TOOL-tFix-2.md"
  git -C "$R" add -A memory && ! git -C "$R" diff --cached --quiet && git -C "$R" commit -q -m "fixture: tFix's records and its forked unit"
}
# read_card_section <card file> — its `## pointers` section, the heading to the line before the next `## ` or READY line.
read_card_section() {
  tr -d '\r' < "$1" | awk '/^## pointers$/ { p = 1; print; next } p && (/^## / || /^(- )?READY — /) { p = 0 } p'
}
# read_card_budget <card file> — the line of its `## pointers` section directly after the `item —` line.
read_card_budget() {
  read_card_section "$1" | awk 'i { print; exit } /^item — / { i = 1 }'
}
# The append at READY, which publishes the build card.
run_card_append() {
  write_card_body "$S/body" 1
  (cd "$R" && bash "$CHECK" --card --append --session t1 < "$S/body") > "$OUT" 2>&1
}

write_card_fixture || { echo "card-store: the fixture could not be built under $S"; sed 's/^/    /' "$OUT" 2>/dev/null; exit 2; }
# The installed card-import fixture's blob, as the engine hashes it from the tree it runs in, and that
# tree's toplevel as git spells it, the bytes of the `tree —` cell.
FX_BLOB=$(git -C "$R" hash-object -- "$HERE/card-compaction.fixture.sh" 2>/dev/null)
RT=$(unset GIT_DIR GIT_WORK_TREE; git -C "$R" rev-parse --show-toplevel)

case "$PLANT" in
  render)
    run_card_append; read_ref_card "$O" > "$S/card"
    print_card_held "AC1 the first line names the build at step unrecorded" "$(head -n 1 "$S/card" | grep -q '^card — tFix · step unrecorded · '; echo $?)"
    print_card_held "AC1 the card carries ## pockets and ## route" "$(grep -qx '## pockets' "$S/card" && grep -qx '## route' "$S/card"; echo $?)"
    print_card_held "AC1 its READY line is last" "$(tail -n 1 "$S/card" | grep -q '^READY — tFix'; echo $?)" ;;
  publish)
    run_card_append; c1=$(git -C "$O" rev-parse --verify -q "$REF")
    print_card_held "AC2 the bare remote holds $REF" "$([ -n "$c1" ]; echo $?)"
    print_card_held "AC2 the cache's first line names that commit" "$(head -n 1 "$R/.git/orientation/tFix.md" | grep -qx "# card-ref $c1"; echo $?)"
    run_card_engine "$R" --card --publish --build tFix --session t1; c2=$(git -C "$O" rev-parse --verify -q "$REF")
    print_card_held "AC2 a second publish's commit has the first as its parent" "$([ -n "$c2" ] && [ "$c2" != "$c1" ] && [ "$(git -C "$O" rev-parse "$c2^")" = "$c1" ]; echo $?)" ;;
  publish-off)
    # TOOL-dPlacedRequest-33 AC1, AC2: the switch is the driver's, so the conf alone moves it.
    set_card_policy card.snapshot every-transition
    printf 'RUN_CLAIMS="off"\n' > "$R/.unattended.conf"
    run_card_append
    print_card_held "AC1 RUN_CLAIMS off: the append names the remote-ref store unwritten" "$(grep -qx 'card — remote-ref not written: RUN_CLAIMS is off' "$OUT"; echo $?)"
    print_card_held "AC1 the clone cache and the build-folder snapshot are written" "$(grep -qx '# card-ref local' "$R/.git/orientation/tFix.md" && [ "$(measure_card_records "$R")" = 1 ]; echo $?)"
    print_card_held "AC1 the bare remote holds no refs/gov/builds ref" "$([ -z "$(git -C "$O" for-each-ref refs/gov/builds)" ]; echo $?)"
    printf 'RUN_CLAIMS="on"\n' > "$R/.unattended.conf"
    run_card_append; c1=$(git -C "$O" rev-parse --verify -q "$REF")
    print_card_held "AC2 RUN_CLAIMS on: the bare remote holds $REF" "$([ -n "$c1" ]; echo $?)"
    print_card_held "AC2 gov-feed.log holds its line" "$(tr -d '\r' < "$R/.git/gov-feed.log" 2>/dev/null | awk -F'\t' -v r="$REF" -v c="$c1" '$2 == r && $5 == c { f = 1 } END { exit !f }'; echo $?)"
    print_card_held "AC2 the cache ref names the same commit" "$([ "$(git -C "$R" rev-parse --verify -q "refs/gov/remote/${REF#refs/gov/}")" = "$c1" ]; echo $?)" ;;
  publish-unwritten)
    # TOOL-dPlacedRequest-33 S2's other unwritten answers: no conf, no driver, and a driver refusal relayed.
    mv "$R/.unattended.conf" "$S/conf.kept"
    run_card_append
    print_card_held "S2 no .unattended.conf: the remote-ref store is named unwritten" "$(grep -qx 'card — remote-ref not written: no .unattended.conf in this tree' "$OUT"; echo $?)"
    mv "$S/conf.kept" "$R/.unattended.conf"
    f=$(ROOT="$R" MC_DIR="$HERE" resolve_kit_file unattended unattended.sh); [ -n "$f" ] || { echo "card-store: no driver resolves in $R"; exit 2; }
    mv "$f" "$S/driver.kept"
    run_card_append
    print_card_held "S2 no driver: the remote-ref store is named unwritten" "$(grep -qx 'card — remote-ref not written: no unattended driver resolves in this tree' "$OUT"; echo $?)"
    mv "$S/driver.kept" "$f"
    git -C "$R" remote add second "$O"
    run_card_append
    print_card_held "S2 the driver's refusal is relayed: two remotes, check 24" "$(grep -qx 'card — remote-ref not written: the clone does not declare exactly one remote, check 24' "$OUT"; echo $?)"
    print_card_held "S2 none of the three wrote a ref, and the cache reads local" "$([ -z "$(git -C "$O" for-each-ref refs/gov/builds)" ] && grep -qx '# card-ref local' "$R/.git/orientation/tFix.md"; echo $?)" ;;
  publish-late)
    # TOOL-dPlacedRequest-43 AC17: a stub driver whose lookup answers `none` and whose write lands the
    # card ref on the bare remote, then sleeps past CARD_PUBLISH_BOUND=2; the append names the store
    # `unknown`, since the write landed, never `not written`. Staged against the `not written` kill line.
    f=$(ROOT="$R" MC_DIR="$HERE" resolve_kit_file unattended unattended.sh); [ -n "$f" ] || { echo "card-store: no driver resolves in $R"; exit 2; }
    printf '%s\n' 'case "${1:-} ${2:-}" in' \
      '  "--card-ref lookup") echo "card-ref — none"; exit 0 ;;' \
      '  "--card-ref write") c=$(git commit-tree "$(git mktree </dev/null)" -m "gov-card tFix") && git push -q '"$FX_REMOTE"' "$c:'"$REF"'" 2>/dev/null; exec sleep 60 ;;' \
      'esac' 'echo "claims: off"' > "$f"
    CARD_PUBLISH_BOUND=2 run_card_append
    print_card_held "AC17 a killed publish whose write landed names the store unknown" "$(grep -qx 'card — remote-ref unknown: no answer within 2s' "$OUT"; echo $?)"
    print_card_held "AC17 ...never not written" "$(! grep -q '^card — remote-ref not written' "$OUT"; echo $?)"
    print_card_held "AC17 the bare remote holds the ref the write landed" "$(git -C "$O" rev-parse --verify -q "$REF" >/dev/null; echo $?)" ;;
  publish-hung)
    # TOOL-dPlacedRequest-33 AC3: a driver that never answers `--card-ref`, its `--claims` answering off.
    # The clock is the append's excess over a control append whose stub driver answers at once, so the
    # engine's own render time, seconds on a slow node, is not charged to the bound.
    f=$(ROOT="$R" MC_DIR="$HERE" resolve_kit_file unattended unattended.sh); [ -n "$f" ] || { echo "card-store: no driver resolves in $R"; exit 2; }
    printf '%s\n' 'case "${1:-}" in --card-ref) echo "card-ref — off"; exit 0 ;; esac' 'echo "claims: off"' > "$f"
    t0=$EPOCHSECONDS; CARD_FETCH_BOUND=4 run_card_append; t1=$EPOCHSECONDS
    printf '%s\n' 'case "${1:-}" in --card-ref) exec sleep 60 ;; esac' 'echo "claims: off"' > "$f"
    t2=$EPOCHSECONDS; CARD_FETCH_BOUND=4 run_card_append; t3=$EPOCHSECONDS
    print_card_held "AC3 the append names no answer within the bound" "$(grep -qx 'card — remote-ref not written: no answer within 4s' "$OUT"; echo $?)"
    print_card_held "AC3 the append took $((t3 - t2 - t1 + t0))s over the control, within the bound plus 3s" "$([ $((t3 - t2 - t1 + t0)) -le 7 ]; echo $?)"
    print_card_held "AC3 the session card is written" "$(grep -q '^READY — tFix' "$R/.git/orientation/t1.md"; echo $?)" ;;
  store-remote|store-local|store-folder|store-empty)
    case "$PLANT" in
      store-remote) set_card_policy card.store remote-ref ;; store-local) set_card_policy card.store local-clone ;;
      store-folder) set_card_policy card.store build-folder ;; store-empty) set_card_policy card.store "" ;;
    esac
    set_card_policy card.snapshot every-transition
    run_card_append
    ref=$(git -C "$O" rev-parse --verify -q "$REF" >/dev/null; echo $?); cache=$([ -f "$R/.git/orientation/tFix.md" ]; echo $?)
    folder=$([ "$(measure_card_records "$R")" -gt 0 ]; echo $?)
    case "$PLANT" in
      store-remote) want="0 1 1" ;; store-local) want="1 0 1" ;; store-folder) want="1 1 0" ;; store-empty) want="1 1 1" ;;
    esac
    print_card_held "AC3 written: remote-ref $([ "$ref" = 0 ] && echo yes || echo no) · local-clone $([ "$cache" = 0 ] && echo yes || echo no) · build-folder $([ "$folder" = 0 ] && echo yes || echo no)" "$([ "$ref $cache $folder" = "$want" ]; echo $?)"
    if [ "$PLANT" = store-empty ]; then
      print_card_held "AC3 the empty set is refused, named" "$(grep -q '^card — skipped: card.store refused' "$OUT"; echo $?)"
      print_card_held "AC3 the session card alone is written" "$(grep -q '^READY — tFix' "$R/.git/orientation/t1.md"; echo $?)"
    fi ;;
  follow-rerender|follow-per-step|follow-fixed)
    case "$PLANT" in
      follow-per-step) set_card_policy card.follows card-per-step ;; follow-fixed) set_card_policy card.follows fixed-at-start ;;
    esac
    run_card_append; c1=$(git -C "$O" rev-parse --verify -q "$REF")
    run_card_engine "$R" --card --follow --build tFix --to designing; read_ref_card "$O" > "$S/card"
    case "$PLANT" in
      follow-rerender) print_card_held "AC4 re-render-at-transition: step designing, the tail kept" "$(head -n 1 "$S/card" | grep -q '^card — tFix · step designing ·' && grep -qx '## route' "$S/card"; echo $?)" ;;
      follow-per-step) print_card_held "AC4 card-per-step: step designing, READY — none yet, no route" "$(head -n 1 "$S/card" | grep -q '^card — tFix · step designing ·' && grep -qx 'READY — none yet' "$S/card" && ! grep -qx '## route' "$S/card"; echo $?)" ;;
      follow-fixed) print_card_held "AC4 fixed-at-start: the ref is unchanged" "$([ "$(git -C "$O" rev-parse --verify -q "$REF")" = "$c1" ] && grep -q 'fixed-at-start: nothing written' "$OUT"; echo $?)" ;;
    esac
    run_card_engine "$R" --card --follow --build tFix --to landed --terminal
    print_card_held "AC4 a terminal follow publishes step landed, marked terminal" "$(read_ref_card "$O" | head -n 1 | grep -q '^card — tFix · step landed ·' && git -C "$O" log -1 --format=%B "$REF" | sed -n 3p | grep -qx 'step: landed · terminal'; echo $?)" ;;
  snapshot-terminal|snapshot-every)
    run_card_append
    [ "$PLANT" = snapshot-terminal ] || set_card_policy card.snapshot every-transition
    run_card_engine "$R" --card --follow --build tFix --to designing
    run_card_engine "$R" --card --follow --build tFix --to landed --terminal
    n=$(measure_card_records "$R"); want=1; [ "$PLANT" = snapshot-terminal ] || want=2
    print_card_held "AC5 the build folder holds $n card record(s), $want owed" "$([ "$n" = "$want" ]; echo $?)"
    br=$(ROOT="$R" MC_DIR="$HERE" resolve_kit_file memory-tree build_records.py); bad=0
    for f in "$R"/memory/builds/tFix/build/*-card-*.md; do
      [ -f "$f" ] || continue
      (cd "$R" && "$PY" "$br" read "memory/builds/tFix/build/${f##*/}") > "$OUT" 2>&1 || bad=1
    done
    print_card_held "AC5 build_records.py read grades each record clean" "$bad"
    print_card_held "AC5 each record is committed alone" "$(git -C "$R" log -1 --format=%s | grep -q '^card snapshot(tFix): landed$' && [ -z "$(git -C "$R" status --porcelain -- memory)" ]; echo $?)"
    if [ "$PLANT" = snapshot-terminal ]; then
      gi=$(ROOT="$R" MC_DIR="$HERE" resolve_kit_file memory-tree gen_build_index.py)
      (cd "$R" && "$PY" "$gi" --print-bindings) > "$OUT" 2>&1
      rec=$(cd "$R" && ls memory/builds/tFix/build/*-card-1.md 2>/dev/null)
      print_card_held "AC12 --print-bindings prints an S row for $rec of kind card and the anchor TOOL-tFix-1, and no A row" \
        "$(tr -d '\r' < "$OUT" | grep -q "^S	$rec	card	.*TOOL-tFix-1" && ! tr -d '\r' < "$OUT" | grep -q "^A	$rec"; echo $?)"
    fi ;;
  lookup|lookup-offline)
    run_card_append; c1=$(git -C "$O" rev-parse --verify -q "$REF")
    # The lookup is the driver's (TOOL-dPlacedRequest-34 S12), so the clone checks out main, its kits and
    # its `.unattended.conf` with it: the bare remote's HEAD names no branch the fixture pushed.
    git clone -q -b main "$O" "$S/clone2" 2>/dev/null && git -C "$S/clone2" config core.hooksPath "$S/hooks"
    mkdir -p "$S/clone2/.git/orientation" && printf '# card-ref 0000000000000000000000000000000000000000\ncard — tFix · step stale · published - · by t0\n' > "$S/clone2/.git/orientation/tFix.md"
    run_card_engine "$S/clone2" --card --lookup --build tFix --session t2
    print_card_held "AC6 a stale cache is not trusted: re-derived" "$(grep -q '^card — tFix · re-derived · ref ' "$OUT"; echo $?)"
    print_card_held "AC6 t2.md holds the session's header and the build card's tail" "$(head -n 1 "$S/clone2/.git/orientation/t2.md" | grep -q '^orientation — t2 ' && grep -qx '## route' "$S/clone2/.git/orientation/t2.md"; echo $?)"
    print_card_held "AC6 the cache is rewritten to the ref" "$(head -n 1 "$S/clone2/.git/orientation/tFix.md" | grep -qx "# card-ref $c1"; echo $?)"
    if [ "$PLANT" = lookup-offline ]; then
      mv "$O" "$O.gone"
      CARD_FETCH_BOUND=10 run_card_engine "$S/clone2" --card --lookup --build tFix --session t2
      print_card_held "AC6 the remote unreachable: evidence, read the cache" "$(grep -q '^card — tFix · evidence · ref  · read the cache' "$OUT"; echo $?)"
    fi ;;
  lookup-upstream)
    # TOOL-dPlacedRequest-34 AC9: the lookup fetches from the remote the driver resolves, never `origin`.
    run_card_append; c1=$(git -C "$O" rev-parse --verify -q "$REF")
    git clone -q -b main "$O" "$S/clone2" 2>/dev/null && git -C "$S/clone2" config core.hooksPath "$S/hooks" \
      && git -C "$S/clone2" remote rename origin upstream
    run_card_engine "$S/clone2" --card --lookup --build tFix --session t2
    print_card_held "AC9 a clone whose one remote is upstream reads the card: re-derived at ${c1:0:8}" "$(grep -q "^card — tFix · re-derived · ref ${c1:0:8} " "$OUT"; echo $?)" ;;
  lookup-hung)
    # TOOL-dPlacedRequest-34 AC11: a driver that never answers the lookup; the clock is the excess over a
    # control lookup whose stub answers at once, as publish-hung measures, and the cache answers.
    run_card_append
    f=$(ROOT="$R" MC_DIR="$HERE" resolve_kit_file unattended unattended.sh); [ -n "$f" ] || { echo "card-store: no driver resolves in $R"; exit 2; }
    printf '%s\n' 'case "${1:-}" in --card-ref) echo "card-ref — none"; exit 0 ;; esac' 'echo "claims: off"' > "$f"
    t0=$EPOCHSECONDS; CARD_FETCH_BOUND=4 run_card_engine "$R" --card --lookup --build tFix --session t2; t1=$EPOCHSECONDS
    printf '%s\n' 'case "${1:-}" in --card-ref) exec sleep 60 ;; esac' 'echo "claims: off"' > "$f"
    t2=$EPOCHSECONDS; CARD_FETCH_BOUND=4 run_card_engine "$R" --card --lookup --build tFix --session t2; t3=$EPOCHSECONDS
    print_card_held "AC11 a silent driver reads the next store: evidence" "$(grep -q '^card — tFix · evidence · ' "$OUT"; echo $?)"
    print_card_held "AC11 the lookup took $((t3 - t2 - t1 + t0))s over the control, within the bound plus 3s" "$([ $((t3 - t2 - t1 + t0)) -le 7 ]; echo $?)" ;;
  replay)
    # TOOL-dPlacedRequest-34 AC12: the replay's lookup is the driver's, which writes no FETCH_HEAD.
    run_card_append
    : > "$R/.git/FETCH_HEAD"; touch -d '2001-01-01 00:00:00' "$R/.git/FETCH_HEAD"; m0=$(stat -c %Y "$R/.git/FETCH_HEAD")
    printf -v payload '{"session_id":"t1","cwd":"%s"}' "$R"
    (cd "$R" && printf '%s' "$payload" | bash "$CHECK" --card --replay) > "$OUT" 2>&1
    print_card_held "AC12 the replay re-keyed the routed build's card" "$(grep -q '^card — tFix · ' "$OUT"; echo $?)"
    print_card_held "AC12 FETCH_HEAD's mtime is unchanged" "$([ "$(stat -c %Y "$R/.git/FETCH_HEAD")" = "$m0" ]; echo $?)" ;;
  fixture-run)
    # KICK-dKeptSession-12 AC4: the verb over a stub fixture exiting 0, 1 and 2, each into its own
    # scratch dir; every file under the scratch tree but those dirs and the case's output is listed
    # before and after, so a write outside <dir> other than the verdict is seen. The verdict records PATH's
    # `claude` (KICK-dKeptSession-37 S2), so a stub answering 9.9.2 stands first on PATH.
    export AI_AGENT=claude-code_9-9-2_agent
    write_claude_stub 'echo "9.9.2 (Claude Code)"'
    v="$R/.git/orientation/card-fixture.verdict"; mkdir -p "$S/snap"
    printf 'exit 0\n' > "$S/stub0.sh"
    printf '%s\n' 'echo "card-compaction: FAILED limb B — the stub names its limb"' 'exit 1' > "$S/stub1.sh"
    printf 'exit 2\n' > "$S/stub2.sh"
    find "$S" -path "$S/snap" -prune -o -path "$S/fx*" -prune -o -path "$OUT" -prune -o -type f -printf '%p %s %T@\n' | sort > "$S/snap/before"
    for x in 0 1 2; do
      CARD_FIXTURE="$S/stub$x.sh" run_card_engine "$R" --card --fixture-run "$S/fx$x"; rc=$?
      case "$x" in 0) want='pass' ;; 1) want='red B' ;; 2) want='absent' ;; esac
      b8=$(git -C "$R" hash-object -- "$S/stub$x.sh" | cut -c1-8)
      print_card_held "AC4 a stub exiting $x records $want, and the verb prints that line and exits 0" \
        "$([ "$rc" = 0 ] && grep -qx "card-fixture — $want · fixture $b8 · cli 9\.9\.2 · [0-9T:+-]*" "$v" && [ "$(tr -d '\r' < "$OUT")" = "$(tr -d '\r' < "$v")" ]; echo $?)"
    done
    find "$S" -path "$S/snap" -prune -o -path "$S/fx*" -prune -o -path "$OUT" -prune -o -type f -printf '%p %s %T@\n' | sort > "$S/snap/after"
    moved=$(diff "$S/snap/before" "$S/snap/after" | sed -n 's/^[<>] \(.*\) [0-9]* [0-9.]*$/\1/p' | sort -u)
    print_card_held "AC4 nothing outside the scratch dirs was written but the verdict (moved: ${moved:-none})" "$([ "$moved" = "$v" ]; echo $?)"
    rm -f "$v"
    CARD_FIXTURE="$S/stub9.sh" run_card_engine "$R" --card --fixture-run "$S/fx9"; rc=$?
    print_card_held "AC4 with CARD_FIXTURE naming no file the verb exits 2 and writes no verdict" "$([ "$rc" = 2 ] && [ ! -e "$v" ]; echo $?)" ;;
  fixture-run-cli)
    # KICK-dKeptSession-37 AC2, AC3: the verdict records the version of the `claude` first on PATH, the
    # binary the fixture launches, never the one AI_AGENT names; a stub printing no version records
    # `unknown`, and a card written beside it keeps the `cli —` cell's skipped: reason.
    export AI_AGENT=claude-code_9-9-2_agent
    v="$R/.git/orientation/card-fixture.verdict"
    printf 'exit 0\n' > "$S/stub0.sh"
    write_claude_stub 'echo "9.9.1 (Claude Code)"'
    CARD_FIXTURE="$S/stub0.sh" run_card_engine "$R" --card --fixture-run "$S/fx0"; rc=$?
    print_card_held "AC2 the verdict records PATH's claude 9.9.1, not AI_AGENT's 9.9.2" \
      "$([ "$rc" = 0 ] && grep -q '^card-fixture — pass · fixture [0-9a-f]\{8\} · cli 9\.9\.1 · ' "$v"; echo $?)"
    write_claude_stub 'exit 1'
    CARD_FIXTURE="$S/stub0.sh" run_card_engine "$R" --card --fixture-run "$S/fx1"; rc=$?
    print_card_held "AC3 a PATH claude printing nothing records cli unknown" \
      "$([ "$rc" = 0 ] && grep -q '^card-fixture — pass · fixture [0-9a-f]\{8\} · cli unknown · ' "$v"; echo $?)"
    run_card_engine "$R" --card --write --session t1
    print_card_held "AC3 the card's cli — cell keeps its reason" \
      "$(grep -m1 '^cli — ' "$R/.git/orientation/t1.md" | tr -d '\r' | grep -qx 'cli — skipped: claude --version printed no version'; echo $?)" ;;
  context-*|partial-*|terminal-route|fixture-stale|fixture-cli-*|worktree-named|replay-order)
    case "$PLANT" in context-*|fixture-stale|fixture-cli-path-differs|worktree-named|replay-order) export AI_AGENT=claude-code_9-9-2_agent ;; fixture-cli-unknown) unset AI_AGENT ;; esac
    # The verdict's reader compares a recorded pass with PATH's `claude` too (KICK-dKeptSession-38 S1),
    # so every case replaying one past its blob test answers from a stub, never the node's own binary.
    case "$PLANT" in context-always-resume|fixture-stale|fixture-cli-*) write_claude_stub 'echo "9.9.2 (Claude Code)"' ;; esac
    if [ "$PLANT" = worktree-named ]; then
      # The build card published from a linked worktree, so its `tree —` cell names that tree, and the
      # replay below runs in the primary.
      git -C "$R" worktree add -q "$S/wt" -b wt 2>/dev/null || { echo "card-store: no worktree could be added under $S"; exit 2; }
      WT=$(unset GIT_DIR GIT_WORK_TREE; git -C "$S/wt" rev-parse --show-toplevel)
      write_card_body "$S/body" 1
      (cd "$S/wt" && bash "$CHECK" --card --append --session t1 < "$S/body") > "$OUT" 2>&1
    else
      run_card_append
    fi
    case "$PLANT" in
      context-always-resume|context-fixture-red|fixture-stale|fixture-cli-*) set_card_policy resume.context always-resume ;;
      context-always-fresh) set_card_policy resume.context always-fresh ;;
      partial-restart) set_card_policy resume.partial restart-item ;; partial-ask) set_card_policy resume.partial ask-owner ;;
    esac
    tx="$S/transcript.jsonl"; : > "$tx"; touch -d "@$(( EPOCHSECONDS - 1800 ))" "$tx"
    printf -v payload '{"session_id":"t1","transcript_path":"%s","cwd":"%s"}' "$tx" "$R"
    case "$PLANT" in
      context-always-resume) set_card_verdict pass "${FX_BLOB:0:8}" 9.9.2 ;;
      context-fixture-red)
        printf '@.claude/orientation-card.md\n' > "$R/CLAUDE.md"
        set_card_verdict 'red A' "${FX_BLOB:0:8}" 9.9.2 ;;
      fixture-stale) set_card_verdict pass 00000000 9.9.2 ;;
      fixture-cli-path-differs) set_card_verdict pass "${FX_BLOB:0:8}" 9.9.2; write_claude_stub 'echo "9.9.1 (Claude Code)"' ;;
      fixture-cli-unknown) set_card_verdict pass "${FX_BLOB:0:8}" unknown ;;
      context-transcript-absent) printf -v payload '{"session_id":"t1","cwd":"%s"}' "$R" ;;
      partial-*) : > "$R/one.txt"; : > "$R/two.txt" ;;
    esac
    if [ "$PLANT" = terminal-route ]; then
      run_card_engine "$R" --card --follow --build tFix --to landed --terminal
      cp "$R/.git/orientation/t1.md" "$S/before"
      write_card_body "$S/route" 0
      (cd "$R" && bash "$CHECK" --card --append --session t1 < "$S/route") > "$OUT" 2>&1; rc=$?
      print_card_held "AC9 a route to a terminal build exits 1 printing route R7 REFUSED" "$([ "$rc" = 1 ] && grep -q 'route R7 REFUSED' "$OUT"; echo $?)"
      print_card_held "AC9 the card is unchanged" "$(cmp -s "$S/before" "$R/.git/orientation/t1.md"; echo $?)"
    fi
    (cd "$R" && printf '%s' "$payload" | bash "$CHECK" --card --replay) > "$OUT" 2>&1
    case "$PLANT" in
      context-idle) print_card_held "AC7 fresh-when-idle, idle 1800s: fresh, in the publisher's tree" "$([[ $(grep '^resume — ' "$OUT" | tr -d '\r') == "resume — fresh recommended: idle 1"*"s past 300s · in $RT (resume.context: fresh-when-idle)" ]]; echo $?)" ;;
      context-always-resume) print_card_held "AC2 always-resume, a pass recorded for this fixture and cli: resume, no override" "$(grep -qx 'resume — resume recommended (resume.context: always-resume)' "$OUT"; echo $?)" ;;
      context-always-fresh) print_card_held "AC7 always-fresh: fresh, in the publisher's tree" "$(grep -qxF "resume — fresh recommended · in $RT (resume.context: always-fresh)" "$OUT"; echo $?)" ;;
      context-fixture-red)
        want='(resume.context: always-resume read as fresh-when-idle · card-import fixture red: red A)'
        print_card_held "AC1 always-resume, a red verdict recorded and the import line present: fresh, the override named" "$(grep -F "$want" "$OUT" | grep -q '^resume — fresh recommended: idle '; echo $?)" ;;
      fixture-stale)
        print_card_held "AC3 a pass recorded for another fixture blob overrides" "$(grep '^resume — fresh recommended: idle ' "$OUT" | grep -qF "card-import fixture red: recorded for fixture 00000000, now ${FX_BLOB:0:8})"; echo $?)"
        set_card_verdict pass "${FX_BLOB:0:8}" 1.0.0
        (cd "$R" && printf '%s' "$payload" | bash "$CHECK" --card --replay) > "$OUT" 2>&1
        print_card_held "AC3 a pass recorded under another cli overrides, named against PATH's" "$(grep '^resume — fresh recommended: idle ' "$OUT" | grep -qF "card-import fixture red: recorded under cli 1.0.0, PATH now 9.9.2)"; echo $?)" ;;
      fixture-cli-path-differs)
        # KICK-dKeptSession-38 AC1, AC2: a pass recorded at 9.9.2 replayed under each side differing in
        # turn, then under all three equal.
        print_card_held "AC1 the session's 9.9.2 equal, PATH's 9.9.1 not: fresh, the PATH reason named" "$(grep '^resume — fresh recommended: idle ' "$OUT" | grep -qF "card-import fixture red: recorded under cli 9.9.2, PATH now 9.9.1)"; echo $?)"
        write_claude_stub 'echo "9.9.2 (Claude Code)"'; export AI_AGENT=claude-code_9-9-3_agent
        (cd "$R" && printf '%s' "$payload" | bash "$CHECK" --card --replay) > "$OUT" 2>&1
        print_card_held "AC2 PATH's 9.9.2 equal, the session's 9.9.3 not: fresh, the session reason named" "$(grep '^resume — fresh recommended: idle ' "$OUT" | grep -qF "card-import fixture red: fixture ran cli 9.9.2, this session runs 9.9.3)"; echo $?)"
        export AI_AGENT=claude-code_9-9-2_agent
        (cd "$R" && printf '%s' "$payload" | bash "$CHECK" --card --replay) > "$OUT" 2>&1
        print_card_held "AC2 all three 9.9.2: resume, no override" "$(grep -qx 'resume — resume recommended (resume.context: always-resume)' "$OUT"; echo $?)" ;;
      fixture-cli-unknown)
        # KICK-dKeptSession-38 AC3 and S2's other two sides: an unknown version is red, never an equality.
        print_card_held "AC3 a recorded cli unknown, AI_AGENT unset: fresh, unknown named for the record" "$(grep '^resume — fresh recommended: idle ' "$OUT" | grep -qF "card-import fixture red: cli version unknown · recorded)"; echo $?)"
        set_card_verdict pass "${FX_BLOB:0:8}" 9.9.2; write_claude_stub 'exit 1'; export AI_AGENT=claude-code_9-9-2_agent
        (cd "$R" && printf '%s' "$payload" | bash "$CHECK" --card --replay) > "$OUT" 2>&1
        print_card_held "S2 a PATH claude printing no version: fresh, unknown named for PATH" "$(grep '^resume — fresh recommended: idle ' "$OUT" | grep -qF "card-import fixture red: cli version unknown · PATH)"; echo $?)"
        write_claude_stub 'echo "9.9.2 (Claude Code)"'; unset AI_AGENT
        (cd "$R" && printf '%s' "$payload" | bash "$CHECK" --card --replay) > "$OUT" 2>&1
        print_card_held "S2 AI_AGENT naming no version: fresh, unknown named for the session" "$(grep '^resume — fresh recommended: idle ' "$OUT" | grep -qF "card-import fixture red: cli version unknown · session)"; echo $?)" ;;
      worktree-named)
        print_card_held "AC5 a fresh recommendation names the worktree the stored tree cell names" "$([[ $(grep '^resume — ' "$OUT" | tr -d '\r') == "resume — fresh recommended: idle 1"*"s past 300s · in $WT (resume.context: fresh-when-idle)" ]] && [ "$WT" != "$RT" ]; echo $?)"
        git -C "$R" worktree remove --force "$S/wt" 2>/dev/null
        (cd "$R" && printf '%s' "$payload" | bash "$CHECK" --card --replay) > "$OUT" 2>&1
        print_card_held "AC5 that tree no longer listed: a new worktree of tFix" "$(grep '^resume — fresh recommended: idle ' "$OUT" | grep -qF ' · in a new worktree of tFix (resume.context: fresh-when-idle)'; echo $?)" ;;
      replay-order)
        at=$(tr -d '\r' < "$OUT" | awk '/^READY — tFix/ && !r { r = NR } /^card — tFix · / && !c { c = NR } /^route — / && !o { o = NR }
          /^resume — / && !e { e = NR } /^partial — / && !p { p = NR } /^now — / && !n { n = NR } END { print r + 0, c + 0, o + 0, e + 0, p + 0, n + 0 }')
        read -r l1 l2 l3 l4 l5 l6 <<<"$at"
        print_card_held "AC6 READY, card, route, resume, partial and now at lines $at, increasing" "$([ "$l1" -gt 0 ] && [ "$l1" -lt "$l2" ] && [ "$l2" -lt "$l3" ] && [ "$l3" -lt "$l4" ] && [ "$l4" -lt "$l5" ] && [ "$l5" -lt "$l6" ]; echo $?)" ;;
      context-transcript-absent)
        print_card_held "AC7 no transcript_path: fresh, transcript absent, in the publisher's tree" "$(grep -qxF "resume — fresh recommended: transcript absent · in $RT (resume.context: fresh-when-idle)" "$OUT"; echo $?)"
        printf -v payload '{"session_id":"t1","transcript_path":"%s","cwd":"%s"}' "$S/deleted.jsonl" "$R"
        (cd "$R" && printf '%s' "$payload" | bash "$CHECK" --card --replay) > "$OUT" 2>&1
        print_card_held "AC7 a transcript_path naming a deleted file: the same" "$(grep -qxF "resume — fresh recommended: transcript absent · in $RT (resume.context: fresh-when-idle)" "$OUT"; echo $?)" ;;
      partial-*)
        v=${PLANT#partial-}; case "$v" in continue) v=continue-item ;; restart) v=restart-item ;; ask) v=ask-owner ;; esac
        print_card_held "AC8 the partial line counts 2 paths and names $v" "$(grep -q "^partial — 2 uncommitted path(s) · resume.partial: $v · " "$OUT"; echo $?)"
        [ "$v" != restart-item ] || print_card_held "AC8 the kickoff's RESUME.md states the restart act (TOOL-dPlacedRequest-34 S36)" "$(grep -q 'partial/<slug>/<sid8>' "$HERE/RESUME.md"; echo $?)" ;;
      terminal-route) print_card_held "AC9 a replay over the card routed there re-checks R7" "$(grep -qx 'route — re-checked · R7' "$OUT"; echo $?)" ;;
    esac ;;
  close-follow-twice)
    run_card_append
    run_card_engine "$R" --card --follow --build tFix --to withdrawn --terminal
    run_card_engine "$R" --card --follow --build tFix --to withdrawn --terminal
    print_card_held "AC13 the second follow keeps the snapshot, named" "$(grep -qx 'card — snapshot kept: withdrawn already recorded' "$OUT"; echo $?)"
    rec=$(ls "$R"/memory/builds/tFix/build/*-card-*.md 2>/dev/null)
    print_card_held "AC13 one card record, its Step withdrawn" "$([ "$(measure_card_records "$R")" = 1 ] && grep -qx -- '- \*\*Step:\*\* withdrawn' "$rec"; echo $?)" ;;
  follow-offline-publish|follow-offline-publish-online|follow-foreign-after-cached|follow-foreign-after-offline)
    # TOOL-dPlacedRequest-99 S4: a follow's stored tail is the FRESHER card of the selected stores. The
    # two offline plants publish online, look the card up, then publish again from a later base with the
    # remote gone, so the cache alone holds the newer card under `# card-ref local`; the follow, offline
    # or with the remote answering again, carries that card's tail and says `tail from cache` (S6). The
    # two foreign plants plant a second writer's publish on the ref, stamped later than the cache, after
    # this node cached its own published sha or after an offline local write; the follow carries the
    # foreign tail, and the lookup that `resolve_build_card` runs after it re-keys the same card. Staged
    # against the ref-first order, each offline plant misses with the older tail; against a rule taking
    # the cache whenever its `# card-ref` is `local` or differs from the ref, each foreign plant misses.
    run_card_append; c1=$(git -C "$O" rev-parse --verify -q "$REF"); cache="$R/.git/orientation/tFix.md"
    old=$(read_ref_card "$O" | tail -n 1)
    case "$PLANT" in
      follow-offline-publish|follow-offline-publish-online)
        run_card_engine "$R" --card --lookup --build tFix --session t1 ;;
      follow-foreign-after-cached)
        print_card_held "S4 the publish cached its own sha" "$(head -n 1 "$cache" | tr -d '\r' | grep -qx "# card-ref $c1"; echo $?)" ;;
    esac
    if [ "$PLANT" != follow-foreign-after-cached ]; then
      sleep 1; git -C "$R" commit -q --allow-empty -m "fixture: a later base"
      mv "$O" "$O.gone"; CARD_FETCH_BOUND=10 run_card_append
      want=$(tail -n 1 "$cache" | tr -d '\r')
      print_card_held "S4 the offline publish wrote the cache alone, # card-ref local, a READY line other than the ref's" \
        "$(head -n 1 "$cache" | tr -d '\r' | grep -qx '# card-ref local' && [ -n "$want" ] && [ "$want" != "$old" ]; echo $?)"
      [ "$PLANT" = follow-offline-publish ] || mv "$O.gone" "$O"
    fi
    case "$PLANT" in
      follow-foreign-*)
        sleep 1; printf -v at '%(%Y-%m-%dT%H:%M:%S%z)T' -1
        git -C "$O" log -1 --format=%B "$REF" -- | tr -d '\r' \
          | sed -e '4s/^session: .*/session: tF/' -e "6s/ · published [^ ]* · by .*/ · published $at · by tF/" \
                -e '/^READY — tFix/s/ · base [0-9a-f]* · / · base f0f0f0f0f0f0 · /' > "$S/foreign.msg"
        f1=$(git -C "$O" -c user.name=foreign -c user.email=foreign@test commit-tree "$REF^{tree}" -p "$REF" -F "$S/foreign.msg") \
          && git -C "$O" update-ref "$REF" "$f1" "$c1"
        print_card_held "S4 a second writer's publish stands on the ref, stamped $at" "$([ "$(git -C "$O" rev-parse --verify -q "$REF")" = "$f1" ]; echo $?)"
        want=$(grep '^READY — tFix' "$S/foreign.msg") ;;
    esac
    CARD_FETCH_BOUND=10 run_card_engine "$R" --card --follow --build tFix --to designing; cp "$OUT" "$S/follow.out"
    [ -d "$O" ] || mv "$O.gone" "$O"
    if [ "$PLANT" = follow-offline-publish ]; then
      tail -n +2 "$cache" | tr -d '\r' > "$S/card"
      print_card_held "S6 the follow's local-clone line says tail from cache" "$(grep -q '^card — tFix · step designing · local-clone .* · tail from cache$' "$S/follow.out"; echo $?)"
    else
      read_ref_card "$O" > "$S/card"
    fi
    print_card_held "S4 the follow's card is at step designing and carries the newer publish's tail" \
      "$(head -n 1 "$S/card" | grep -q '^card — tFix · step designing ·' && [ "$(tail -n 1 "$S/card")" = "$want" ]; echo $?)"
    case "$PLANT" in
      follow-foreign-*)
        run_card_engine "$R" --card --lookup --build tFix --session t1
        sed -n '/^## route$/,$p' "$S/card" > "$S/card.tail"; tr -d '\r' < "$R/.git/orientation/t1.md" | sed -n '/^## route$/,$p' > "$S/t1.tail"
        print_card_held "S4 resolve_build_card, run after the follow, re-keys that same card" \
          "$(grep -q '^card — tFix · ' "$OUT" && [ -s "$S/card.tail" ] && cmp -s "$S/card.tail" "$S/t1.tail"; echo $?)" ;;
    esac ;;
  pointers-render)
    # KICK-dKeptSession-13 AC1, AC11: `--card --pointers` over two journal records, one spec-audit record
    # and a FORKED unit, the stub answering K1. Staged against an older record of a kind winning, the
    # resolved spec listed, or the section after the READY line, a row reds; AC11's second row is the
    # failing case, a section missing a POINTER_LINES line passing the check.
    write_card_records; set_card_position key "$K1"; set_card_position forked TOOL-tFix-2
    run_card_append
    run_card_engine "$R" --card --pointers --build tFix --session t1
    read_ref_card "$O" > "$S/card"; read_card_section "$S/card" > "$S/sec"; h8=$(git -C "$R" rev-parse --short=8 HEAD)
    print_card_held "AC1 records — names the newer journal and the review, never the older journal" \
      "$(grep -q '^records — .*journal memory/builds/tFix/build/2026-01-02-build-TOOL-tFix-1-agent-ledger\.md' "$S/sec" \
        && grep -q '^records — .*spec-audit memory/builds/tFix/reviews/2026-01-01-review-TOOL-tFix-1-spec-audit\.md' "$S/sec" \
        && ! grep -q '2026-01-01-build-TOOL-tFix-1-agent-ledger' "$S/sec"; echo $?)"
    print_card_held "AC1 forks — names the FORKED spec's §8 alone" "$(grep -qx 'forks — memory/builds/tFix/spec/2026-01-01-spec-TOOL-tFix-2\.md §8' "$S/sec"; echo $?)"
    print_card_held "AC1 item — names the stub's key at HEAD $h8" "$(grep -qxF "item — $K1 · at $h8" "$S/sec"; echo $?)"
    print_card_held "AC1 the section sits above the READY line, which is still last" \
      "$(tr -d '\r' < "$S/card" | awk '/^## pointers$/ { p = NR } /^READY — / { r = NR } END { exit !(p && r > p && r == NR) }'; echo $?)"
    run_card_engine "$R" --card --check --session t1; rc=$?
    print_card_held "AC11 --card --check passes the session card as written" "$([ "$rc" = 0 ] && read_card_section "$R/.git/orientation/t1.md" | grep -q '^forks — '; echo $?)"
    grep -v '^forks — ' "$R/.git/orientation/t1.md" > "$S/t1.cut" && cp "$S/t1.cut" "$R/.git/orientation/t1.md"
    run_card_engine "$R" --card --check --session t1; rc=$?
    print_card_held "AC11 with its forks — line cut the check exits 1 naming forks —" "$([ "$rc" = 1 ] && grep -q "no 'forks —' line" "$OUT"; echo $?)" ;;
  pointers-boundary)
    # KICK-dKeptSession-13 AC2: the session card brought to K1, then the stub at K2. Staged against a
    # crossing that leaves the ref's `item —` unchanged, the first row reds; against a run with no
    # crossing that publishes, the second.
    run_card_append; set_card_position key "$K1"
    run_card_engine "$R" --card --boundary --build tFix --session t1
    print_card_held "AC2 a card with no section crosses none → K1" "$(grep -qxF "boundary — none → $K1" "$OUT"; echo $?)"
    set_card_position key "$K2"
    run_card_engine "$R" --card --boundary --build tFix --session t1
    print_card_held "AC2 K1 → K2 prints the crossing and the ref's card reads item — K2" \
      "$(grep -qxF "boundary — $K1 → $K2" "$OUT" && read_ref_card "$O" | grep -q "^item — $K2 · at "; echo $?)"
    c1=$(git -C "$O" rev-parse --verify -q "$REF"); git -C "$R" commit -q --allow-empty -m "fixture: another commit"; h8=$(git -C "$R" rev-parse --short=8 HEAD)
    run_card_engine "$R" --card --boundary --build tFix --session t1
    print_card_held "AC2 the stub still at K2 after a commit: nothing published, the session card's at reads $h8" \
      "$(grep -qxF "boundary — none crossed · item $K2" "$OUT" && [ "$(git -C "$O" rev-parse --verify -q "$REF")" = "$c1" ] \
        && read_card_section "$R/.git/orientation/t1.md" | grep -qxF "item — $K2 · at $h8"; echo $?)"
    run_card_engine "$R" --card --boundary --build tFix --session t1 --out "$S/boundary.out"
    print_card_held "AC2 with --out the stdout is empty and the file holds the lines" "$([ ! -s "$OUT" ] && grep -qxF "boundary — none crossed · item $K2" "$S/boundary.out"; echo $?)"
    run_card_engine "$R" --card --boundary --build tFix --session t1 --out "$S/nowhere/boundary.out"; rc=$?
    print_card_held "AC2 an --out whose directory does not exist is refused, exit 2" "$([ "$rc" = 2 ] && [ ! -e "$S/nowhere" ]; echo $?)" ;;
  pointers-at-transitions)
    # KICK-dKeptSession-13 AC3: under at-transitions a crossing publishes nothing and the follow re-renders.
    set_card_policy card.pointers at-transitions
    run_card_append; c1=$(git -C "$O" rev-parse --verify -q "$REF"); set_card_position key "$K1"
    run_card_engine "$R" --card --boundary --build tFix --session t1
    print_card_held "AC3 the crossing leaves the ref unchanged and rewrites the session card's item — line" \
      "$(grep -qxF "boundary — none → $K1" "$OUT" && [ "$(git -C "$O" rev-parse --verify -q "$REF")" = "$c1" ] \
        && read_card_section "$R/.git/orientation/t1.md" | grep -q "^item — $K1 · at "; echo $?)"
    run_card_engine "$R" --card --follow --build tFix --to designing
    print_card_held "AC3 the follow re-renders the section with the stub's key" \
      "$(read_ref_card "$O" | head -n 1 | grep -q '^card — tFix · step designing ·' && read_ref_card "$O" | grep -q "^item — $K1 · at "; echo $?)" ;;
  pointers-cap)
    # KICK-dKeptSession-13 AC6: a cap the card fits under without its section and not with it, the
    # `## pockets` section's room taken out, since the render drops it before it refuses the card.
    set_card_position key "$K1"; run_card_append; c1=$(git -C "$O" rev-parse --verify -q "$REF")
    read_ref_card "$O" > "$S/card"
    b=$(wc -c < "$S/card"); sb=$(read_card_section "$S/card" | wc -c)
    pb=$(tr -d '\r' < "$S/card" | awk '/^## pockets$/ { p = 1 } /^recent —/ { p = 0 } p' | wc -c)
    CARD_CAP_BYTES=$((b - pb - sb / 2)) run_card_engine "$R" --card --pointers --build tFix --session t1
    print_card_held "AC6 under CARD_CAP_BYTES=$((b - pb - sb / 2)) the publish names the pointers not written" "$(grep -q '^card — pointers not written: [0-9]* bytes over the cap$' "$OUT"; echo $?)"
    print_card_held "AC6 the ref is unchanged" "$([ "$(git -C "$O" rev-parse --verify -q "$REF")" = "$c1" ]; echo $?)" ;;
  pointers-replay)
    # KICK-dKeptSession-13 AC7: a compacted session's replay in a second clone, after a publish carrying
    # K1, prints the section the lookup re-keyed from the build card.
    set_card_position key "$K1"; run_card_append
    git clone -q -b main "$O" "$S/clone2" 2>/dev/null && git -C "$S/clone2" config core.hooksPath "$S/hooks"
    run_card_engine "$S/clone2" --card --lookup --build tFix --session t2
    C2=$(unset GIT_DIR GIT_WORK_TREE; git -C "$S/clone2" rev-parse --show-toplevel)
    printf -v payload '{"session_id":"t2","cwd":"%s"}' "$C2"
    (cd "$S/clone2" && printf '%s' "$payload" | bash "$CHECK" --card --replay) > "$OUT" 2>&1
    print_card_held "AC7 the replay prints the ## pointers section the lookup re-keyed" \
      "$(read_card_section "$OUT" | grep -q "^item — $K1 · at " && read_card_section "$OUT" | grep -q '^records — '; echo $?)" ;;
  budget-open)
    # KICK-dKeptSession-26 AC1, AC4: the stub loop kit answering open 3/10 at the append, then two
    # `--card --boundary` runs, the stub moved to K2 and open 4/10 between them, so the second crosses and
    # publishes under every-item. Staged against a line placed outside the section or after another line,
    # the first row reds; against a boundary re-rendering the section with the earlier figure, the second.
    set_card_position key "$K1"; set_card_position budget "open 3/10"; run_card_append
    read_ref_card "$O" > "$S/card"
    print_card_held "AC1 the published card's line directly after item — reads budget — open 3/10" \
      "$([ "$(read_card_budget "$S/card")" = 'budget — open 3/10' ]; echo $?)"
    run_card_engine "$R" --card --boundary --build tFix --session t1
    set_card_position key "$K2"; set_card_position budget "open 4/10"
    run_card_engine "$R" --card --boundary --build tFix --session t1
    read_ref_card "$O" > "$S/card"
    print_card_held "AC4 the second boundary crosses to K2 and the ref's card reads budget — open 4/10 after item — K2" \
      "$(grep -qxF "boundary — $K1 → $K2" "$OUT" && read_card_section "$S/card" | grep -q "^item — $K2 · at " \
        && [ "$(read_card_budget "$S/card")" = 'budget — open 4/10' ]; echo $?)" ;;
  budget-spent|budget-unfrozen)
    # KICK-dKeptSession-26 AC1: the other two answers, printed as the stub prints them.
    case "$PLANT" in budget-spent) want='budget — spent' ;; *) want='budget — unfrozen 1/4' ;; esac
    set_card_position key "$K1"; set_card_position budget "${want#budget — }"; run_card_append
    read_ref_card "$O" > "$S/card"
    print_card_held "AC1 the published card's line directly after item — reads $want" \
      "$([ "$(read_card_budget "$S/card")" = "$want" ]; echo $?)" ;;
  budget-omitted)
    # KICK-dKeptSession-26 AC2: the session card as written passes `--card --check`; with its `budget —`
    # line cut, the failing case, the check exits 1 naming `budget —`.
    write_card_records; set_card_position key "$K1"; run_card_append
    run_card_engine "$R" --card --pointers --build tFix --session t1
    run_card_engine "$R" --card --check --session t1; rc=$?
    print_card_held "AC2 --card --check passes the session card as written, its line after item — reading budget — open 0/4" \
      "$([ "$rc" = 0 ] && [ "$(read_card_budget "$R/.git/orientation/t1.md")" = 'budget — open 0/4' ]; echo $?)"
    grep -v '^budget — ' "$R/.git/orientation/t1.md" > "$S/t1.cut" && cp "$S/t1.cut" "$R/.git/orientation/t1.md"
    run_card_engine "$R" --card --check --session t1; rc=$?
    print_card_held "AC2 with its budget — line cut the check exits 1 naming budget —" "$([ "$rc" = 1 ] && grep -q "no 'budget —' line" "$OUT"; echo $?)" ;;
  budget-no-kit)
    # KICK-dKeptSession-26 AC3: the copied loop kit's budget.py taken out of the repository, so
    # `resolve_kit_file` answers nothing; the line is a skip, and a skip is a line the check passes.
    f=$(ROOT="$R" MC_DIR="$HERE" resolve_kit_file loop budget.py); [ -n "$f" ] || { echo "card-store: no budget.py resolves in $R"; exit 2; }
    git -C "$R" rm -q -- "${f#"$R"/}" && git -C "$R" commit -q -m "fixture: no budget.py" || { echo "card-store: $f could not be taken out"; exit 2; }
    print_card_held "AC3 no budget.py resolves in the repository" "$([ -z "$(ROOT="$R" MC_DIR="$HERE" resolve_kit_file loop budget.py)" ]; echo $?)"
    write_card_records; set_card_position key "$K1"; run_card_append
    run_card_engine "$R" --card --pointers --build tFix --session t1
    read_ref_card "$O" > "$S/card"
    print_card_held "AC3 the published card's line directly after item — reads budget — skipped: no loop kit" \
      "$([ "$(read_card_budget "$S/card")" = 'budget — skipped: no loop kit' ]; echo $?)"
    run_card_engine "$R" --card --check --session t1; rc=$?
    print_card_held "AC3 --card --check passes the session card carrying the skip" \
      "$([ "$rc" = 0 ] && read_card_section "$R/.git/orientation/t1.md" | grep -qx 'budget — skipped: no loop kit'; echo $?)" ;;
esac
exit "$MISSED"
