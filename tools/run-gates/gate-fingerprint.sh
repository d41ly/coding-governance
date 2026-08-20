#!/usr/bin/env bash
# gate-fingerprint.sh — one digest over "what tree is this, exactly", in two forms.
#
#     gate-fingerprint.sh            # the WORKING-TREE form
#     gate-fingerprint.sh <rev>      # the AT-A-REV form
#
# TWO FORMS, ONE IMPLEMENTATION, and that is the whole point of the file existing. The run record
# stamps the working-tree form; `.githooks/pre-push` calls the at-a-rev form to ask whether a
# recorded green still describes the commit it names. Two independent implementations of one digest
# disagree silently and then force the full bar forever — safe, permanently expensive, and the kind
# of failure nobody investigates because it looks like caution.
#
# THE BINDING PROPERTY: on a CLEAN tree the two forms produce the SAME value. Both hash three
# components in the same order and the same arity; the rev form supplies the last two EMPTY rather
# than omitting them, and on a clean tree the working-tree form's last two are empty as well. The
# record is only ever written from a clean tree, so every recorded digest is one the rev form
# reproduces at the sha it names.
#
# WHAT THIS DOES NOT CHECK. It says nothing about whether the tree is CORRECT, only whether it is the
# same tree. It is deliberately OVER-sensitive: a whitespace-only edit, a touched-then-reverted file
# that git still reports, and an untracked scratch file all change the answer. Over-sensitive costs a
# needless full run; under-sensitive certifies a tree nobody tested, so the asymmetry is chosen.
#
# EMPTY ON ANY FAILURE, never a partial digest. A caller that cannot get a fingerprint must see
# nothing and decide for itself; a half-computed digest is a confident wrong answer, and every
# consumer of this file treats empty as "force the expensive path".
set -u

rev="${1:-}"

# `git hash-object --stdin` rather than a sha utility: git is already a hard dependency here, and
# `sha1sum`/`shasum`/`certutil` are three different tools with three availabilities across the
# platforms this kit ships to. It also gives the digest the same shape as every other id in a git
# repo, which is what a reader of the record expects.
digest() { git hash-object --stdin 2>/dev/null; }

if [ -n "$rev" ]; then
  # THE AT-A-REV FORM. The tree object at <rev>, and the other two components EMPTY.
  #
  # `$rev^{tree}` and not `$rev` — peeling to the tree is what makes two commits with identical
  # content hash identically, which is the property predicate 0 needs when a landing is retried and
  # produces a different commit over the same tree.
  tree=$(git rev-parse --verify -q "$rev^{tree}" 2>/dev/null) || exit 0
  [ -n "$tree" ] || exit 0
  porcelain=""
  blobs=""
else
  # THE WORKING-TREE FORM. All three components, and the two that can be empty are empty exactly
  # when the tree is clean.
  tree=$(git rev-parse --verify -q 'HEAD^{tree}' 2>/dev/null) || exit 0
  [ -n "$tree" ] || exit 0

  # SORTED, because git's porcelain order is not guaranteed stable across versions and a digest that
  # moves with the git build is a digest that forces full for no reason. LC_ALL=C so the sort is over
  # bytes rather than over whatever collation the operator's locale supplies — the same reason every
  # other ordered comparison in this kit pins it.
  porcelain=$(LC_ALL=C git status --porcelain 2>/dev/null | LC_ALL=C sort) || exit 0

  # The blob hash of every dirty-or-untracked file THAT STILL EXISTS. The status lines above already
  # name what changed; these say what it changed TO, which is what makes an edit-and-revert-and-edit
  # cycle distinguishable rather than merely detectable.
  #
  # `-z` and a NUL-delimited read: a path with a space, a quote or a newline in it is legal on every
  # platform this runs on, and porcelain's non-`-z` form QUOTES such a path, so a naive read would
  # hash a filename that does not exist. Deleted paths are skipped rather than failing the digest —
  # their absence is already recorded in the porcelain component.
  blobs=$(
    LC_ALL=C git status --porcelain -z 2>/dev/null \
      | while IFS= read -r -d '' entry; do
          p=${entry:3}
          [ -n "$p" ] || continue
          [ -f "$p" ] || continue
          h=$(git hash-object -- "$p" 2>/dev/null) || continue
          printf '%s %s\n' "$h" "$p"
        done | LC_ALL=C sort
  ) || exit 0
fi

# THREE COMPONENTS, ALWAYS, each on its own line-delimited section. The arity is fixed so the two
# forms hash structurally identical input; a form that omitted a component would produce a different
# digest for the same tree, which is the mismatch this file exists to make impossible.
printf '%s\n---\n%s\n---\n%s\n' "$tree" "$porcelain" "$blobs" | digest
