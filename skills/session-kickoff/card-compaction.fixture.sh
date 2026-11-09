#!/usr/bin/env bash
# card-compaction.fixture.sh — does a session that moves from the primary tree into a worktree and
# compacts load the WORKTREE's orientation card file? (PLAY-dOrderedCharter-8 S1, AC1)
#
#   bash card-compaction.fixture.sh <scratch-dir>
#
# Builds, under <scratch-dir> (a SHORT path: a clone under a long one fails with "Filename too long" on
# Windows, and the directory must be absent or empty):
#   1. a repository whose CLAUDE.md holds the two import lines, `@AGENTS.md` then
#      `@.claude/orientation-card.md`, with two linked worktrees;
#   2. a card file, ignored through the clone's info/exclude, in the primary tree carrying `P-<rand>`
#      and in the first worktree carrying `W-<rand>`; the second worktree holds none;
#   3. session A, `claude -p` started in the primary tree, told to enter the worktree, then resumed with
#      `/compact`, then resumed again and asked which nonce its loaded card file carries;
#   4. session B, started in the second worktree, whose card file is absent, asked to print `ok`.
#
# Exit 0 when A's answer carries the `W-` nonce and not the `P-` one and B prints `ok`; 1 naming the
# limb that failed; 2 when `claude` is not on PATH, no scratch dir is named, or it is not empty. Each
# harness call is bounded by CARD_FIXTURE_BOUND seconds (default 300). WHAT THIS DOES NOT DO: launch
# anything but the `claude` CLI, or stop that CLI keeping its own session transcripts under the user's
# home, the one write outside <scratch-dir>. Costs two headless sessions in minutes and API tokens, so
# the main loop runs it, never a builder pass.
set -u
D=${1:-}
[ -n "$D" ] || { echo "card-compaction: name a scratch dir: bash card-compaction.fixture.sh <scratch-dir>"; exit 2; }
command -v claude >/dev/null 2>&1 || { echo "card-compaction: claude is not on PATH, so no session can be started"; exit 2; }
if [ -e "$D" ] && [ -n "$(ls -A "$D" 2>/dev/null)" ]; then
  echo "card-compaction: $D is not empty; name an absent or empty dir"; exit 2
fi
BOUND=${CARD_FIXTURE_BOUND:-300}
P="$D/p"; W="$D/w"; B="$D/b"
mkdir -p "$P" || { echo "card-compaction: cannot create $P"; exit 2; }
NP="P-$RANDOM$RANDOM"; NW="W-$RANDOM$RANDOM"
CARD_REL=.claude/orientation-card.md
write_card() {   # $1=tree $2=nonce: the card file in its level-1 envelope, as the card engine writes it
  mkdir -p "$1/.claude" && printf '[%s · Level 1 · the build'"'"'s card: where this session stands; level 0 outranks it]\nnonce — %s\n[/%s]\n' \
    "$CARD_REL" "$2" "$CARD_REL" > "$1/$CARD_REL"
}
{ git -C "$P" init -q -b main \
  && printf '# Fixture charter\n\nAnswer exactly what is asked.\n' > "$P/AGENTS.md" \
  && printf '@AGENTS.md\n@%s\n' "$CARD_REL" > "$P/CLAUDE.md" \
  && printf '/%s\n' "$CARD_REL" >> "$P/.git/info/exclude" \
  && git -C "$P" add AGENTS.md CLAUDE.md \
  && git -C "$P" -c user.name=f -c user.email=f@f -c commit.gpgsign=false commit -q -m fixture \
  && git -C "$P" worktree add -q "$W" -b w && git -C "$P" worktree add -q "$B" -b b \
  && write_card "$P" "$NP" && write_card "$W" "$NW"; } >/dev/null 2>&1 \
  || { echo "card-compaction: the fixture repository under $D could not be built"; exit 2; }

ask() {   # $1=tree, the rest claude's arguments: its stdout, bounded; never fails the script
  (cd "$1" && timeout -k 5 "$BOUND" claude "${@:2}" </dev/null 2>/dev/null) || true
}
re_sid='"session_id"[[:space:]]*:[[:space:]]*"([^"]*)"'
out=$(ask "$P" -p "Run \`cd $W\` with the Bash tool, then reply with the single word moved." \
  --allowedTools Bash --add-dir "$W" --output-format json)
[[ $out =~ $re_sid ]] || { echo "card-compaction: FAILED limb A1 — session A printed no session_id: ${out:0:200}"; exit 1; }
SID=${BASH_REMATCH[1]}
ask "$P" -p --resume "$SID" --add-dir "$W" "/compact" >/dev/null
answer=$(ask "$P" -p --resume "$SID" --add-dir "$W" \
  "Which nonce does the orientation card file loaded in your instructions carry? Reply with that nonce alone.")
case "$answer" in
  *"$NP"*) echo "card-compaction: FAILED limb A — session A names the primary's nonce $NP: ${answer:0:200}"; exit 1 ;;
  *"$NW"*) ;;
  *) echo "card-compaction: FAILED limb A — session A names neither $NW nor $NP: ${answer:0:200}"; exit 1 ;;
esac
okb=$(ask "$B" -p "Reply with the single word ok.")
case "$okb" in
  *ok*|*OK*|*Ok*) ;;
  *) echo "card-compaction: FAILED limb B — the session in a tree with no card file did not print ok: ${okb:0:200}"; exit 1 ;;
esac
echo "card-compaction: green — session A names the worktree's $NW after compaction, and session B started with no card file"
exit 0
