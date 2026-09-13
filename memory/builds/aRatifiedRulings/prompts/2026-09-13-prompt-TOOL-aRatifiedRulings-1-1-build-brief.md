# Build brief — TOOL-aRatifiedRulings-1

**Serves:** journal TOOL-aRatifiedRulings-1

The pass this brief was handed to builds unit 1 of `aRatifiedRulings` at rev-3. The spec is
`memory/builds/aRatifiedRulings/spec/2026-09-13-spec-TOOL-aRatifiedRulings-1.md` and it is
authoritative; the ruling it implements is `TOOL-aLeakedHandle-6` in `memory/DECISIONS.md`.

## What the pass builds

Two halves, one unit. M4 of `tools/memory-tree/BUILD-METHOD.template.md` — the SOURCE; the file
under `memory/guides/` is its render and the kit/dogfood parity leg byte-compares them — gains the
paragraph making CONVERGED terminal for its subject with a later blocker taking the exit's own fold
or promote disposition, plus the qualifier on the rev-moved clause. Check 37 branch 10 in
`tools/unattended/unattended.sh` keeps its predicate and its refusal message names that route.

## What two audit rounds settled

- **The kit version bump is NOT this unit's.** Unit 2's §8 F1 assigns the unattended bump to the
  closing pass, once, after every unit that edits the unattended kit has landed. Do not bump
  `KIT_UNATTENDED_VERSION`. The memory-tree kit is a different question: editing its template is a
  watched-kit change, and the spec's S5 and AC7 state what that owes. Read them.
- **The byte budget is measured, not guessed.** M1 caps the render at 27648 B / 350 lines. The spec
  measured 26439 B / 336 lines at base and a scratch render of 26743 B / 340 after both edits. If your
  render lands over, the spec says what is traded out; raising M1's own budget is outside the mandate.
- **AC7's same-commit join is on the M4 BYTES**, via `git log -G` for the version-line change and a
  `git show <sha> -- <template> | grep -c` for the M4 phrases. The file-level join could not fail
  (`a3b4ca1e` proves it) and is not what you build. The two-commit split is the named break.
- **The passes of this build are SEQUENTIAL.** Check 49 condition 1 refuses a second open pass that
  shares any path, and every pass declares the README, LIVE.md and the ledger shard.

## The rules this pass is bound by

- The failing case of every changed arm is OBSERVED RED first, and each arm asserts a positive
  artifact that it ran. `unattended.test.sh` cannot be run unsharded (`TOOL-aTracedSpawn-1`); the spec
  names the shard.
- `memory/guides/SESSION-KICKOFF.md` is in the write set because `unattended.sh` is a watched file:
  re-verify §B and re-stamp `last-audit`, or the kickoff-manifest ratchet reds the commit.
- Commit with the unit id in the subject; then `python tools/memory-tree/gotchas.py --for-diff
  HEAD~1..HEAD` and act on it. Flip the spec status header in the same commit as the code.
- If you need a wider write set — the memory-tree version carriers, say — re-declare with
  `--dispatch` BEFORE the commit. Narrowing after the fact is refused.

## What the pass must not do

- No `KIT_UNATTENDED_VERSION` change. No sibling unit's files: `check-unattended.sh` is unit 2's.
- Never `git stash` on this worktree; the stack is shared with other sessions.
