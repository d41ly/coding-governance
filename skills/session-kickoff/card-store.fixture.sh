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
# planted values from a file outside the repository, and a stub playbook kit whose `pockets` verb
# prints one fact. The engine writes the session card `t1`, appends a READY body with a `## route`
# naming `tFix`, and the case runs its verbs and prints one `card-store: <case> · <what> · held|MISSED`
# line per observation. The scratch tree is removed at exit.
# Exit 2 is a usage error, or a fixture that could not be built.
# WHAT THIS DOES NOT CHECK: a remote other than a local bare one; a lost compare-and-swap, which needs
# two writers between one read and its push; the engine's other cells, which their own arms cover.
set -u
case "$0" in */*) HERE=${0%/*} ;; *) HERE=. ;; esac
HERE=$(CDPATH= cd -- "$HERE" && pwd) || exit 2
CHECK="$HERE/manifest-check.sh"
PLANTS="render publish publish-off publish-unwritten publish-hung store-remote store-local store-folder store-empty follow-rerender follow-per-step
follow-fixed snapshot-terminal snapshot-every lookup lookup-offline lookup-upstream lookup-hung replay context-idle context-always-resume
context-always-fresh context-fixture-red context-transcript-absent partial-continue partial-restart
partial-ask terminal-route close-follow-twice"
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
export CARD_STUB_POLICY="$S/policy.txt"
MISSED=0

# print_card_held <what> <0 held | else missed>
print_card_held() {
  if [ "$2" = 0 ]; then printf 'card-store: %s · %s · held\n' "$PLANT" "$1"
  else printf 'card-store: %s · %s · MISSED\n' "$PLANT" "$1"; sed 's/^/    /' "$OUT"; MISSED=1; fi
}
# set_card_policy <key> <value, a set comma-joined, empty for the empty set>
set_card_policy() {
  grep -v "^$1=" "$CARD_STUB_POLICY" > "$CARD_STUB_POLICY.x" 2>/dev/null; mv -f "$CARD_STUB_POLICY.x" "$CARD_STUB_POLICY"
  printf '%s=%s\n' "$1" "$2" >> "$CARD_STUB_POLICY"
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
  set_card_policy resume.context fresh-when-idle
  set_card_policy resume.partial continue-item
  git -C "$R" add -A && git -C "$R" commit -q -m "fixture: the build tFix" && git -C "$R" branch -M main \
    && git -C "$R" remote add origin "$O" && git -C "$R" push -q origin main 2>/dev/null || return 1
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
# The append at READY, which publishes the build card.
run_card_append() {
  write_card_body "$S/body" 1
  (cd "$R" && bash "$CHECK" --card --append --session t1 < "$S/body") > "$OUT" 2>&1
}

write_card_fixture || { echo "card-store: the fixture could not be built under $S"; sed 's/^/    /' "$OUT" 2>/dev/null; exit 2; }

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
  context-*|partial-*|terminal-route)
    run_card_append
    case "$PLANT" in
      context-always-resume|context-fixture-red) set_card_policy resume.context always-resume ;;
      context-always-fresh) set_card_policy resume.context always-fresh ;;
      partial-restart) set_card_policy resume.partial restart-item ;; partial-ask) set_card_policy resume.partial ask-owner ;;
    esac
    tx="$S/transcript.jsonl"; : > "$tx"; touch -d "@$(( EPOCHSECONDS - 1800 ))" "$tx"
    printf -v payload '{"session_id":"t1","transcript_path":"%s","cwd":"%s"}' "$tx" "$R"
    read_card_fixture_verdict() { printf 'pass\n'; }
    export -f read_card_fixture_verdict
    case "$PLANT" in
      context-fixture-red)
        printf '@.claude/orientation-card.md\n' > "$R/CLAUDE.md"
        read_card_fixture_verdict() { printf 'red: no recorded run\n'; }
        export -f read_card_fixture_verdict ;;
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
      context-idle) print_card_held "AC7 fresh-when-idle, idle 1800s: fresh" "$(grep -q '^resume — fresh recommended: idle 1[0-9]*s past 300s (resume.context: fresh-when-idle)$' "$OUT"; echo $?)" ;;
      context-always-resume) print_card_held "AC7 always-resume, the verdict pass: resume" "$(grep -qx 'resume — resume recommended (resume.context: always-resume)' "$OUT"; echo $?)" ;;
      context-always-fresh) print_card_held "AC7 always-fresh: fresh" "$(grep -qx 'resume — fresh recommended (resume.context: always-fresh)' "$OUT"; echo $?)" ;;
      context-fixture-red)
        want='(resume.context: always-resume read as fresh-when-idle · card-import fixture red: no recorded run)'
        print_card_held "AC7 always-resume, the verdict red and the import line present: fresh, the override named" "$(grep -F "$want" "$OUT" | grep -q '^resume — fresh recommended: idle '; echo $?)"
        unset -f read_card_fixture_verdict
        (cd "$R" && printf '%s' "$payload" | bash "$CHECK" --card --replay) > "$OUT" 2>&1
        print_card_held "AC7 ...and with no reader exported, the same" "$(grep -qF "$want" "$OUT" && grep -q '^resume — fresh recommended' "$OUT"; echo $?)" ;;
      context-transcript-absent)
        print_card_held "AC7 no transcript_path: fresh, transcript absent" "$(grep -qx 'resume — fresh recommended: transcript absent (resume.context: fresh-when-idle)' "$OUT"; echo $?)"
        printf -v payload '{"session_id":"t1","transcript_path":"%s","cwd":"%s"}' "$S/deleted.jsonl" "$R"
        (cd "$R" && printf '%s' "$payload" | bash "$CHECK" --card --replay) > "$OUT" 2>&1
        print_card_held "AC7 a transcript_path naming a deleted file: the same" "$(grep -qx 'resume — fresh recommended: transcript absent (resume.context: fresh-when-idle)' "$OUT"; echo $?)" ;;
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
esac
exit "$MISSED"
