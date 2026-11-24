**Serves:** research TOOL-dQuietDisk-36

# Spec task — dQuietDisk: the closing review's round-1 fold, H1 and H2

You write specs only, in `memory/builds/dQuietDisk/spec/`. Do not commit. Read the spec brief first,
`memory/builds/dQuietDisk/prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md`, and the round-1 closing review
`memory/builds/dQuietDisk/reviews/2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md`, its H1 and H2
whole. Write one new spec, `2026-11-22-spec-TOOL-dQuietDisk-36.md`, Tier-2, order 8, base the `HEAD` you read at.

## Why this unit exists

The closing diff review of `b3f5a2bc3..879413160` confirmed no blocker and two HIGHs. The review loop's closing
target is `highs` (`python tools/loop/review_bounds.py show` prints `closing-target=highs`), so the round does not
converge until both are fixed. This unit is that round's fold; round 2 reviews it. The MEDIUMs and LOWs are not this
unit's: they are promoted at the loop's exit.

## What the unit fixes

1. **H1, the class fix the skeptic asked for.** The bash face of the template cache, `tools/lib/template-cache.sh`
   (`resolve_template`, `build_template_clone`, `derive_template_key`), and its inline copy in
   `tools/lib/lib-selftest.sh`, run git and the fixture builder with the caller's environment as it is. Run every git
   call AND the builder subshell with the git environment names the Python face drops
   (`tools/lib/template_cache.py`, its `GIT_ENV_LEAKS`) unset, so the two faces answer alike. Keep the inline copy
   byte-equal to the canonical block, as the parity row requires. Name the arm that exports `GIT_DIR` at a scratch
   repository, runs a builder that commits its own tree, and sees that repository's `HEAD` unmoved; its failing case
   restores one unscrubbed call.
2. **H2.** `tools/run-gates/run-gates.turnstile.test.sh`'s foreign-repository fixture plants an owner whose absolute
   common dir names no directory, which TOOL-dQuietDisk-9's orphan rule now sweeps, so the arm proving a live other
   repository is spared goes red. Point that fixture's common dir at a directory that exists, keep the health-line
   arm's count right, and add the orphan arm: a dead owner whose absolute common dir is missing is swept, and one
   whose common dir is relative is kept.

## Constraints

- Read every cited line at `HEAD` and cite by symbol or blob. The review cites older blobs.
- Both suites are owed to the main loop: name `New arm:` lines in section 7 so the close observes them RED and GREEN.
- State the files, generated outputs included. Shell-line rows grow only through
  `python tools/memory-tree/ratchet.py widen shell-role`, which the main loop runs after the pass; say so.
- Check every git command and shell idiom against the real tool. This build has ruled on these false facts:
  `git rev-parse --short` takes a single revision; a local `git clone --shared` spawns two processes; an MSYS shell
  rewrites a `!/path` argument; `git hash-object --stdin-paths` and an alternates line refuse an MSYS `/c/...` path; a
  plain `x=$(...)` assignment makes the shell-hygiene scanner follow a heredoc loop over `$x`.
- Each kit whose shipped bytes move moves its version at the mint, never by hand.

## Before you return

- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk TOOL-dQuietDisk-36`.
- Run `check-memory-hygiene.sh --only 12 --spec <path>` and `python tools/check-spec-tokens.py --spec <path>`.
- Run `python tools/playbook/writing_practice.py check pinned-facts` and fix any red in your spec.
- Mark every figure you add PINNED, DERIVED or with an id on its own line.

Return: the spec path and rev, its files touched, its arms, and any fork.
