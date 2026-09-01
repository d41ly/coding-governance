#!/usr/bin/env bash
# manifest-check.sh — kickoff-manifest ratchet gate (coding-governance session-kickoff kit).
# Verifies a project's SESSION-KICKOFF.md kickoff manifest against mechanical truth signals:
#   C1 no surviving {{PLACEHOLDER}}      C2 audit block present + parseable
#   C3 anchor sha real + ancestor        C4 verify-paths tracked
#   C5 no unaudited watch drift          C6 watch list alive
# Single source: CI, pre-commit, the manifest's gate fence, and the kickoff engine all invoke THIS
# script — never hand-copy the checks. Spec: the manifest-ratchet design record in coding-governance.
#
#   manifest-check.sh [<manifest-path>]   # full check (discovers the manifest when no path given;
#                                         # a relative path resolves from the repo root, then from
#                                         # the invoking directory)
#   manifest-check.sh --staged [<path>]   # pre-commit fast leg: C1 C2 C4 C6 C7 C8 + C5s.
#                                         # C9/C10/C11 are FULL-RUN only: they judge the working
#                                         # tree, not what this commit stages, and the hook that
#                                         # runs this leg fires on every commit.
#
# Exit 0 + no FAILED lines = clean (WARN:/NOTE: lines permitted). Exit 1 = a check failed.
# Exit 2 = environment error (not a git repo / no manifest found / path outside the repo).
set -u
KIT_MANIFEST_VERSION="1.3"   # gov:kit kickoff-manifest@1.3 — the registry id

# THE ONE LIST of places a kickoff manifest may live, in precedence order. Every consumer reads it
# from here — the discovery loop, the not-found message, and the `--locations` verb that the kickoff
# engine and WIRE-INTO-PROJECT.md invoke INSTEAD of restating the list. It used to be spelled in five
# files that did not agree with each other, and two of the four spellings named directories no live
# install has ever used.
#
# The skill's own base directory is a THIRD location the ENGINE honours and this script deliberately
# does not list: it sits outside every repository, and this script decides membership by git identity
# and refuses an out-of-repo path with exit 2 by design. It cannot check that one, so it does not
# claim to. A manifest found there is read but never audited, and the engine says so on the card.
MANIFEST_LOCATIONS="memory/guides/SESSION-KICKOFF.md .claude/SESSION-KICKOFF.md"

# THE CANONICAL TASK FIELD SET, and its ONE home. §A of a manifest used to restate what the kickoff
# engine's Step 3 already said, with the manifest outranking the engine on conflict — two binding
# spellings of one contract, which is the drift this kit exists to remove. Sealing the manifest's copy
# against a constant would have FROZEN that duplication; giving the field set one home removes it.
#
# It lives HERE because this script is the only kickoff-kit file that is present, byte-identical and
# overwritten wholesale in every adopting repo. MANIFEST-TEMPLATE.md cannot hold it: the template is a
# SEED that BECOMES the manifest, so an adopting tree has no reference copy left to compare against.
#
# NO PLACEHOLDER inside the region. A tier value is optional by the template's own customize note, and
# a region whose content is conditional cannot be byte-compared — it would be simultaneously required
# by check 10 and banned by check 1. The tier enumeration already has a home in §B's tier rule, so
# dropping it here is a deduplication that happens to be what makes the seal implementable.
read -r -d '' TASK_SKELETON <<'KICKOFF_TASK_SKELETON' || true
<!-- kickoff:task -->
> - **Title:** …
> - **Goal (1–2 sentences):** …
> - **IN scope:** …
> - **OUT / non-goals** (explicit cut-line): …
> - **Acceptance check** (the observation that proves THIS change — a test it adds, a gate it
>   moves, an observed behavior; *not* an unrelated green check): …
> - **Gates it must pass:** …
<!-- /kickoff:task -->
KICKOFF_TASK_SKELETON

# Both read-only verbs answer BEFORE the repo probe below, because the whole point of `--locations` is
# to be readable from OUTSIDE a repository — and the probe exits 2 there without ever reading argv.
# They print and exit 0, adding no `fail` branch, so the harness meta-gate's shrink-only floor for this
# script counts neither of them.
for _a in "$@"; do
  case "$_a" in
    --locations)     printf '%s\n' $MANIFEST_LOCATIONS; exit 0 ;;
    --task-skeleton) printf '%s\n' "$TASK_SKELETON"; exit 0 ;;
  esac
done

CALLER_PWD=$PWD
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "MANIFEST env ERROR — not a git repository"; exit 2; }
ROOT=$(cd "$ROOT" 2>/dev/null && pwd) || { echo "MANIFEST env ERROR — cannot enter repo root"; exit 2; }   # normalize to the shell's path flavor (git-bash: C:/ vs /c/)
cd "$ROOT" || exit 2

STAGED=0; MF=""
for a in "$@"; do
  case "$a" in
    --staged) STAGED=1 ;;
    *) MF="$a" ;;
  esac
done

# Resolve a path argument: repo-root-relative first, then caller-cwd-relative; never outside the
# repo. Membership is decided by git identity (file's toplevel == this ROOT, both normalized the
# same way), never by path-string comparison — under MSYS one directory has two spellings
# (/tmp/x vs /c/.../Temp/x) and realpath can't unify them (mount points aren't symlinks).
if [ -n "$MF" ]; then
  case "$MF" in
    /*|[A-Za-z]:*) abs="$MF" ;;
    *) if [ -f "$ROOT/$MF" ]; then abs="$ROOT/$MF"; else abs="$CALLER_PWD/$MF"; fi ;;
  esac
  [ -f "$abs" ] || { echo "MANIFEST env ERROR — '$MF' not found (tried the repo root, then $CALLER_PWD)"; exit 2; }
  dir=$(cd "$(dirname -- "$abs")" 2>/dev/null && pwd) || dir=""
  froot=""
  if [ -n "$dir" ]; then
    froot=$(git -C "$dir" rev-parse --show-toplevel 2>/dev/null) || froot=""
    [ -n "$froot" ] && { froot=$(cd "$froot" 2>/dev/null && pwd) || froot=""; }
  fi
  if [ -z "$froot" ] || [ "$froot" != "$ROOT" ]; then
    echo "MANIFEST env ERROR — '$MF' resolves outside this repository"; exit 2
  fi
  MF="$(git -C "$dir" rev-parse --show-prefix 2>/dev/null)$(basename -- "$abs")"
else
  for p in $MANIFEST_LOCATIONS; do
    [ -f "$p" ] && { MF="$p"; break; }
  done
fi
# The message is BUILT from the same array the loop walks, so it can never again describe a different
# list than the one that was searched.
[ -n "$MF" ] && [ -f "$MF" ] || {
  echo "MANIFEST env ERROR — no kickoff manifest at $(printf '%s, ' $MANIFEST_LOCATIONS | sed 's/, $//') (and no valid path argument). Move an existing manifest to the first of those, or run this script with --locations to see the list."
  exit 2
}

# Unmanaged manifest (no kickoff-manifest marker, e.g. a prototype) — not ratchet-managed.
# An UNREADABLE manifest is an env error, never a green.
grep -q 'kickoff-manifest:' "$MF"
case $? in
  0) ;;
  1) echo "NOTE: $MF carries no kickoff-manifest marker — not ratchet-managed; skipping all checks."; exit 0 ;;
  *) echo "MANIFEST env ERROR — cannot read $MF"; exit 2 ;;
esac

# Forward-drift signal: manifest format older than this kit copy (no sort -V — BSD/busybox safe).
ver_older() { awk -v a="$1" -v b="$2" 'BEGIN{na=split(a,x,".");nb=split(b,y,".");n=(na>nb?na:nb);for(i=1;i<=n;i++){d=(x[i]+0)-(y[i]+0);if(d<0){print "y";exit}if(d>0)exit}}'; }
mver=$(sed -n 's/.*kickoff-manifest: v\([0-9][0-9.]*\).*/\1/p' "$MF" | head -1); mver=${mver%.}
if [ -n "$mver" ] && [ "$(ver_older "$mver" "$KIT_MANIFEST_VERSION")" = "y" ]; then
  echo "WARN: manifest format v$mver < kit v$KIT_MANIFEST_VERSION — see the upgrade recipe in coding-governance/WIRE-INTO-PROJECT.md §4."
fi

status=0
fail() { echo "MANIFEST check $1 FAILED — $2"; status=1; }

# LIFTED VERBATIM from tools/unattended/check-unattended.sh, and gated as an inline copy by the
# parity table in tools/lib/resolve-python.test.sh. Do not re-type it:
# it carries two fixes that were each reproduced before they were written. A marker line IS the marker
# or it is malformed — the prefix test IDENTIFIES the line and equality JUDGES it, because the older
# form let a run append its own text to a marker line and still compare byte-equal. And the pair must
# be exactly one open, one close, CLOSE AFTER OPEN: a transposed pair satisfies a count-only check and
# once truncated a file. CR-normalised before comparing, because the prefix test tolerated a CRLF
# worktree by accident and an equality test does not.
# >>> kickoff_region
region()   { awk -v o="$2" -v c="$3" '
               { ln=$0; sub(/\r$/,"",ln) }
               index(ln,o)==1 { if (ln!=o) bad=1; no++; if (no==1) oat=NR; if (nc==0) inside=1; next }
               index(ln,c)==1 { if (ln!=c) bad=1; nc++; if (nc==1) cat=NR; inside=0; next }
               inside { print }
               END { if (bad || no!=1 || nc!=1 || cat<oat) exit 3 }' "$1"; }
# <<< kickoff_region

# The block's last-audit VALUE from a manifest body on stdin (block-scoped: body decoys don't count).
blockstamp() {
  awk '/<!-- manifest-audit/{f=1;next} f&&/-->/{exit} f' | tr -d '\r' \
    | sed -n 's/^[[:space:]]*last-audit:[[:space:]]*\(.*\)$/\1/p' | head -1 | sed 's/[[:space:]]*$//'
}

# C1 — no placeholder survives (placeholder SHAPE only: gate fences legitimately hold ${{ ... }},
# Go-template {{.Field}}, Helm {{ .Values }} — none of which match '{{' + uppercase).
c1=$(grep -nE '\{\{[A-Z]' "$MF" || true)
[ -n "$c1" ] && fail 1 "unfilled {{PLACEHOLDER}} survives in $MF (fill or delete each):
$(printf '%s\n' "$c1" | sed 's/^/  /')"

# C7 — SIZE. LF-NORMALISED bytes, because the manifest is not eol-pinned in every adopting tree and
# an unnormalised count answers differently per platform — the split that already cost this repo a
# blocked push on the memory-tree byte caps. `check-template-size.sh` is the in-repo precedent and
# measures the same way. The env override exists so the self-test can drive the limit without writing
# a 25 KiB fixture on every run; it is NOT an adopter escape hatch, and the message says so.
MAX_MANIFEST_BYTES=${MAX_MANIFEST_BYTES:-25600}
c7bytes=$(tr -d '\r' < "$MF" | wc -c | tr -d '[:space:]')
if [ "$c7bytes" -gt "$MAX_MANIFEST_BYTES" ]; then
  c7over=$((c7bytes - MAX_MANIFEST_BYTES))
  fail 7 "the manifest is over its size limit and must be trimmed, not have the limit raised: $c7bytes bytes, $c7over over the $MAX_MANIFEST_BYTES-byte limit in $MF"
fi

# C8 — LINE LENGTH, in BYTES. awk's length() counts bytes on this platform, and portable character
# counting across busybox, mawk and BSD awk does not exist — so the limit is bytes and the message
# says bytes rather than claiming characters it does not measure.
#
# Two regions are exempt. The audit block is machine-maintained data with no prose to wrap: its watch
# list is one line that grows as pathspecs are added. Fenced blocks hold commands that cannot be
# wrapped without breaking them. NOTHING else is exempt — a table row or a body bullet over the limit
# is prose someone wrote, which is exactly what this check is for.
c8=$(awk '
  { ln=$0; sub(/\r$/,"",ln) }
  index(ln,"<!-- manifest-audit")==1 { inblk=1; next }
  inblk && ln ~ /-->/ { inblk=0; next }
  inblk { next }
  ln ~ /^[[:space:]]*(```|~~~)/ { fence=!fence; next }
  fence { next }
  length(ln) > 400 { printf "  line %d: %d bytes\n", NR, length(ln) }
' "$MF")
[ -n "$c8" ] && fail 8 "a manifest line is over the 400-byte limit; wrap the prose or move the detail out:
$c8"

# C2 — exactly one manifest-audit block, four keys with non-empty, well-formed values.
RETROFIT="retrofit: (1) body deltas — rewrite the §B intro to 're-audited every kickoff; accretes', add the ratchet + dated-corrections (never delete the section) + traps-accrete text; (2) add the manifest-audit block: last-audit '<ISO datetime> @ <full sha>' (sha = HEAD on the default branch, else \$(git merge-base <remote>/<default> HEAD)), watch = gate-defining pathspecs, verify-paths = 2-3 anchors, last-body-change = the sha where the BODY was last revised; (2b) paste the sealed task region from --task-skeleton into §A; (3) copy manifest-check.sh in, add the .gitattributes LF rule + the gate-fence line, git add everything; (4) run this check to 0; (5) pull the manifest DoD + reconcile lines into the project's playbook; (6) bump the marker to v1.3 LAST. Full recipe: coding-governance/WIRE-INTO-PROJECT.md §4."
nblocks=$(grep -c '<!-- manifest-audit' "$MF" || true)
BLOCK_OK=1
if [ "$nblocks" -eq 0 ]; then
  fail 2 "no manifest-audit block in $MF — $RETROFIT"
  BLOCK_OK=0
elif [ "$nblocks" -gt 1 ]; then
  fail 2 "$nblocks manifest-audit blocks in $MF — exactly one is allowed; merge them."
  BLOCK_OK=0
fi

LA=""; WATCH_RAW=""; VP_RAW=""
if [ "$BLOCK_OK" = 1 ]; then
  BLOCK=$(awk '/<!-- manifest-audit/{f=1;next} f&&/-->/{exit} f' "$MF" | tr -d '\r')
  getval() { printf '%s\n' "$BLOCK" | sed -n "s/^[[:space:]]*$1:[[:space:]]*\(.*\)$/\1/p" | head -1 | sed 's/[[:space:]]*$//'; }
  LA=$(getval 'last-audit'); WATCH_RAW=$(getval 'watch'); VP_RAW=$(getval 'verify-paths')
  LBC=$(getval 'last-body-change')
  [ -n "$LA" ] || { fail 2 "manifest-audit block lacks a last-audit value — stamp '<ISO datetime> @ <full sha>' after verifying §B."; BLOCK_OK=0; }
  # The C9 baseline. It is RECORDED rather than derived, because deriving it means walking the
  # manifest's own path history, and a path-scoped `git log --name-status` reports a `git mv` as an
  # ADD, not a rename — so a relocated manifest read as freshly created and a stalled one reported
  # itself maintained. Reproduced at git 2.55 before this key existed.
  [ -n "$LBC" ] || { fail 2 "manifest-audit block lacks a last-body-change value — add the full sha of the commit where this manifest's BODY was last genuinely revised; it is what check 9 measures the stall against."; BLOCK_OK=0; }
  [ -n "$WATCH_RAW" ] || { fail 2 "manifest-audit block lacks a watch value — list the gate-defining pathspecs (a missing watch silently disables the drift check)."; BLOCK_OK=0; }
  [ -n "$VP_RAW" ] || { fail 2 "manifest-audit block lacks a verify-paths value — list the 2-3 anchor paths."; BLOCK_OK=0; }
fi

# ;-split, trimming, EMPTY ELEMENTS DROPPED (a stray ';' must never reach git as '' — fatal 128).
splitspecs() { printf '%s\n' "$1" | tr ';' '\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | grep -v '^$' || true; }

WATCH=(); VPATHS=(); LA_SHA=""
if [ "$BLOCK_OK" = 1 ]; then
  while IFS= read -r _s; do WATCH+=("$_s"); done < <(splitspecs "$WATCH_RAW")
  while IFS= read -r _s; do VPATHS+=("$_s"); done < <(splitspecs "$VP_RAW")
  [ "${#WATCH[@]}" -gt 0 ] || { fail 2 "watch: holds no usable pathspec after splitting — list the gate-defining pathspecs (a missing watch silently disables the drift check)."; BLOCK_OK=0; }
  [ "${#VPATHS[@]}" -gt 0 ] || { fail 2 "verify-paths: holds no usable path after splitting — list the 2-3 anchor paths."; BLOCK_OK=0; }
  if [ "$BLOCK_OK" = 1 ]; then
    if ! printf '%s' "$LA" | grep -qE '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]+)?([+-][0-9]{2}:?[0-9]{2}|Z)[[:space:]]*@[[:space:]]*[0-9a-fA-F]{40}$'; then
      fail 2 "last-audit value malformed ('$LA') — want '<ISO-8601 datetime with offset> @ <full 40-hex sha>'."
      BLOCK_OK=0
    else
      LA_SHA=$(printf '%s' "$LA" | sed -n 's/.*@[[:space:]]*\([0-9a-fA-F]\{40\}\)[[:space:]]*$/\1/p')
    fi
  fi
fi

if [ "$BLOCK_OK" = 1 ]; then
  # C6 — watch list is alive (a dead pathspec is a silent permanent false-green on the drift check).
  for w in "${WATCH[@]}"; do
    n=$(git ls-files -- "$w" 2>/dev/null | wc -l | tr -d '[:space:]')
    if [ "$n" -eq 0 ]; then
      fail 6 "watch pathspec '$w' matches no tracked file — update the watch list to the restructured paths."
    elif [ "$n" -gt 100 ]; then
      echo "WARN: watch pathspec '$w' matches $n tracked files — overly broad; narrow it to the gate-defining slice."
    fi
  done

  # C4 — every verify-path anchors TRACKED content (an untracked leftover must not green the local
  # leg while fresh-clone CI reds).
  for vp in "${VPATHS[@]}"; do
    vp="${vp%/}"
    if git ls-files --error-unmatch -- "$vp" >/dev/null 2>&1; then :
    elif git ls-files -- "$vp/" 2>/dev/null | grep -q .; then :
    else
      fail 4 "verify-path '$vp' is not tracked content — the tree restructured or the anchor is dead; fix the path (or the §B pointer it anchors)."
    fi
  done

  STAMP_SHA_RULE="sha = HEAD on the default branch, else \$(git merge-base <remote>/<default> HEAD)"
  if [ "$STAGED" = 0 ]; then
    SKIP_RANGE=0
    # C3 — anchor sha is real and ours.
    if ! git rev-parse -q --verify 'HEAD^{commit}' >/dev/null 2>&1; then
      fail 3 "HEAD has no commits on this branch — make the first commit, then re-verify §B and re-stamp last-audit at it."
      SKIP_RANGE=1
    elif ! git cat-file -e "$LA_SHA^{commit}" 2>/dev/null; then
      if [ "$(git rev-parse --is-shallow-repository 2>/dev/null)" = "true" ]; then
        echo "WARN: shallow clone and the last-audit sha is absent — skipping C3+C5; set 'fetch-depth: 0' on the CI checkout step so the drift check actually enforces."
        SKIP_RANGE=1
      else
        fail 3 "last-audit sha $LA_SHA is unknown to this repo — the stamp is foreign or predates a history rewrite; re-verify §B, then re-stamp last-audit '<ISO datetime> @ <sha>' with $STAMP_SHA_RULE."
        SKIP_RANGE=1
      fi
    elif ! git merge-base --is-ancestor "$LA_SHA" HEAD 2>/dev/null; then
      fail 3 "last-audit sha $LA_SHA is not an ancestor of HEAD — history was rewritten or the stamp was squash-merged; re-verify §B, then re-stamp last-audit '<ISO datetime> @ <sha>' with $STAMP_SHA_RULE."
      SKIP_RANGE=1
    fi

    # C5 — no unaudited drift (TOPOLOGICAL + STRUCTURAL): the newest watch-touching commit W must be
    # an ancestor of (or equal to) the newest commit S that actually CHANGED the audit block's
    # last-audit VALUE. Candidates come from a pathspec-FREE -G search (with the rename source in the
    # diff, git's rename detection collapses a pure `git mv` of the manifest, which a pathspec-scoped
    # search would mistake for a stamp); each candidate is then validated by comparing the block's
    # stamp value at the commit vs its parent, so body decoy lines and block reorders never count.
    # Residual (documented): a decoy edit in a commit predating the manifest's current path is
    # accepted unvalidated — narrow, and it fails toward green only when combined with a later rename.
    if [ "$SKIP_RANGE" = 0 ]; then
      W=$(git rev-list -1 "$LA_SHA..HEAD" -- "${WATCH[@]}" 2>/dev/null)
      if [ -n "$W" ]; then
        S=""
        while IFS= read -r cand; do
          [ -n "$cand" ] || continue
          cur=$(git show "$cand:$MF" 2>/dev/null | blockstamp)
          prev=$(git show "$cand^:$MF" 2>/dev/null | blockstamp)
          if [ -z "$cur" ] || [ -z "$prev" ] || [ "$cur" != "$prev" ]; then S="$cand"; break; fi
        done < <(git log --format=%H -G'^last-audit:' "$LA_SHA..HEAD" 2>/dev/null)
        if [ -z "$S" ] || ! git merge-base --is-ancestor "$W" "$S" 2>/dev/null; then
          files=$(git diff --name-only "$LA_SHA..HEAD" -- "${WATCH[@]}" 2>/dev/null | sed 's/^/  /')
          fail 5 "watched files changed since last-audit with no re-stamp at/after the change:
$files
  For each file, re-check the §B claims derived from it, update the manifest where stale, then
  re-stamp last-audit ($STAMP_SHA_RULE) — bundled with the watched change or as a follow-up in the
  same PR. After a merge that brought in watch-touching commits, the fresh post-merge audit +
  re-stamp is the close."
        fi
      fi
    fi

    # C10 and C11 live HERE, not beside C7/C8, and the reason is the adopter upgrade path.
    # WIRE-INTO-PROJECT.md installs the --staged leg as an UNCONDITIONAL pre-commit hook and
    # documents overwriting this checker wholesale on a kit update. Both checks judge the
    # WORKING-TREE manifest's structure rather than what a commit stages, so above the split they
    # would block EVERY commit in a repo whose manifest predates this format — with no migration
    # staged and no way to make progress. C9's own comment already drew this line; these two
    # simply had not been held to it.
    # C10 — THE SEALED TASK REGION. §A's field set is a contract, not guidance, and before this check it
    # was prose: deleting §A entirely left every check green.
    #
    # ABSENCE IS A FAILURE, NOT A SKIP. The prior art this borrows from skips silently when its source is
    # absent, and copying that here would make the seal dormant in exactly the population it exists for —
    # every manifest written before this format version has no region at all. Three distinct messages,
    # one per failure mode, so the remedy is never guessed.
    #
    # The comparison appends a SENTINEL. Command substitution strips trailing newlines, so without it a
    # trailing-blank-line difference inside the region is invisible — the weakness the prior art still
    # carries and `kit-dogfood-parity.test.sh` already defeats this way.
    c10n=$(grep -c '<!-- kickoff:task -->' "$MF" || true)
    if [ "$c10n" -eq 0 ]; then
      fail 10 "the manifest carries no sealed task region, so its §A field set is prose that any edit can silently change; paste the region printed by this script's --task-skeleton verb into §A of $MF"
    elif ! c10have=$(region "$MF" '<!-- kickoff:task -->' '<!-- /kickoff:task -->' 2>/dev/null); then
      fail 10 "the sealed task region's markers are malformed, so the region cannot be compared with the contract it copies; the pair must be exactly one open and one close, close after open, each alone on its line in $MF"
    else
      # The sentinel goes INSIDE each substitution. Appended after, both sides have already had their
      # trailing newlines stripped identically and it defends nothing — which is exactly what it did
      # until the closing review pointed at it, and a trailing blank line inside the region passed.
      c10have=$(region "$MF" '<!-- kickoff:task -->' '<!-- /kickoff:task -->' 2>/dev/null; printf X)
      c10want=$(printf '%s\n' "$TASK_SKELETON" | region /dev/stdin '<!-- kickoff:task -->' '<!-- /kickoff:task -->' 2>/dev/null; printf X)
      if [ "$c10have" != "$c10want" ]; then
        fail 10 "the sealed task region differs from the task contract this script carries, and that region is not hand-authorable; restore it from the --task-skeleton verb rather than editing it in $MF"
      fi
    fi

    # C11 — PER-BULLET CAP on the environment-traps section. Not a new rule: MANIFEST-TEMPLATE.md has
    # always instructed "keep each to one line; link out for detail". It was ignored until this repo's own
    # traps section reached 14,535 bytes across 27 bullets, 19 of them over the cap. C11 makes the kit's
    # own instruction mechanical, and reuses C8's 400 rather than minting a second number — C8 already
    # defines how long a line may be, and one line is what the template asked for.
    #
    # C7 is not a substitute. It bounds the FILE, so traps can re-accrete to the size limit by crowding
    # out every other section; C11 bounds the ENTRY, which is where accretion actually happens.
    c11=$(awk '
      { ln=$0; sub(/\r$/,"",ln) }
      /^###[[:space:]]+Environment traps/ { intraps=1; next }
      intraps && /^##[^#]/ { intraps=0 }
      intraps && /^###[[:space:]]/ { intraps=0 }
      !intraps { next }
      /^-[[:space:]]/ {
        if (n > 0 && len > 400) printf "  the bullet starting %s is %d bytes\n", head, len
        n++; len = length(ln) + 1; head = "\"" substr(ln, 3, 40) "…\""; next
      }
      { len += length(ln) + 1 }
      END { if (n > 0 && len > 400) printf "  the bullet starting %s is %d bytes\n", head, len }
    ' "$MF")
    [ -n "$c11" ] && fail 11 "an environment-traps bullet is over the 400-byte cap; the template asks for one line each with the detail linked out, and a record under the memory tree is where the detail belongs:
    $c11"

    # C9 — MAINTENANCE STALL. Never in the staged leg: the pre-commit hook runs that leg
    # unconditionally on every commit in an adopting repo, and this question is not one a single
    # commit changes.
    #
    # The baseline is READ, not walked. `aRatchetForge` §10.9 set the thresholds and deliberately left
    # them to an owner review because the delta lines it would have read live in commit messages and
    # READY cards, which squash merges do not preserve. A recorded sha survives a squash, survives a
    # rename, needs no candidate cap and cannot be defeated by a graft boundary on a shallow clone.
    #
    # MERGES ARE EXCLUDED. A merge commit carries no content of its own, so counting it alongside the
    # commits it brings in double-counts the same churn. The prior spec said only "watch-pathspec
    # commits" and that one unstated word decides the verdict: this repo measures 11 counting merges
    # and 6 without, against a threshold of 10.
    if [ -n "$LBC" ]; then
      if ! printf '%s' "$LBC" | grep -qE '^[0-9a-fA-F]{40}$'; then
        fail 9 "last-body-change is not a full 40-hex sha, so the stall check has no baseline to measure from: '$LBC'"
      elif ! git cat-file -e "$LBC^{commit}" 2>/dev/null; then
        if [ "$(git rev-parse --is-shallow-repository 2>/dev/null)" = "true" ]; then
          echo "WARN: shallow clone and the last-body-change sha is absent — skipping C9; set 'fetch-depth: 0' on the CI checkout step."
        else
          fail 9 "last-body-change names a commit unknown to this repository, so the stall baseline is foreign or predates a history rewrite: $LBC"
        fi
      elif ! git merge-base --is-ancestor "$LBC" HEAD 2>/dev/null; then
        fail 9 "last-body-change is not an ancestor of HEAD, so the stall baseline was squash-merged or rewritten and measures nothing: $LBC"
      else
        c9n=$(git rev-list --count --no-merges "$LBC..HEAD" -- "${WATCH[@]}" 2>/dev/null || echo 0)
        c9age=$(( ( $(git log -1 --format=%ct HEAD 2>/dev/null || echo 0) - $(git log -1 --format=%ct "$LBC" 2>/dev/null || echo 0) ) / 86400 ))
        if [ "$c9n" -ge 10 ]; then
          fail 9 "the manifest body has not changed across ten or more watched commits, so its front-loaded claims are drifting unverified; re-read §B and advance last-body-change to a current sha: $c9n non-merge commits since $LBC"
        elif [ "$c9age" -ge 90 ]; then
          fail 9 "the manifest body has not changed in three months or more, so its front-loaded claims are drifting unverified; re-read §B and advance last-body-change to a current sha: $c9age days since $LBC"
        fi
      fi
    fi
  else
    # C5s — staged leg (deliberately narrowed: a blocking pre-commit cannot see a future follow-up
    # commit, so the bundle form is the only green path here). STRUCTURAL: the staged blob's block
    # stamp must differ from HEAD's — co-staging an unrelated manifest edit, or a body decoy line,
    # does not count.
    sw=$(git diff --cached --name-only -- "${WATCH[@]}" 2>/dev/null)
    if [ -n "$sw" ]; then
      staged_stamp=$(git show ":$MF" 2>/dev/null | blockstamp)
      head_stamp=$(git show "HEAD:$MF" 2>/dev/null | blockstamp)
      if [ -z "$staged_stamp" ] || [ "$staged_stamp" = "$head_stamp" ]; then
        fail 5 "staged changes touch watched files:
$(printf '%s\n' "$sw" | sed 's/^/  /')
  but the staged manifest's audit block does not update last-audit. Re-verify the §B claims these
  files feed, update the manifest where stale, and bundle the re-stamp into THIS commit
  ($STAMP_SHA_RULE)."
      fi
    fi
  fi
fi

exit "$status"
