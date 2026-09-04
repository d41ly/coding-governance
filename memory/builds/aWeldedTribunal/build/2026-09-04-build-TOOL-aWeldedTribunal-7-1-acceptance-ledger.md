# TOOL-aWeldedTribunal-7 — acceptance ledger

**Serves:** build TOOL-aWeldedTribunal-7

## What changed

`check_hook_blobs` in `tools/check-wiring.sh`, walking `GOV_WIRING_HOOKS` — `pre-commit pre-push` —
and called from check H once the resolved dir is known. Plus the two stale prose claims: the
`.githooks/pre-push` header, and `AGENTS.md`'s merge-bar paragraph. Plus both halves of
`memory/gotchas/hookspath-resolves-into-another-checkout.md`. Eight arms in the self-test.

## Each criterion, answered

- **AC1** — a planted `pre-push` divergence prints
  `note hooks — pre-push DIVERGES: the hook that will run is <blob> from <path>`, then the supplying
  checkout's branch and the tracked blob.
- **AC2** — with that divergence present, `bash tools/check-wiring.sh --check` exits **0**. This is
  the criterion the round-2 blocker was about: rev-1 would have used an `UNWIRED` line, and `unwired`
  is what `:809` turns into the exit code, so it would have shipped the vetoed option under the
  accepted one's name and refused every unattended run through `.unattended.conf`'s `WIRING_CHECK`.
- **AC3** — a planted `pre-commit` divergence reports too, and two divergences still exit 0.
- **AC4** — with the blobs equal, no divergence line prints and the existing `ok hooks` line stands.
  In this worktree today that is the live state, so the change is a no-op here.
- **AC5** — in a scratch repo tracking a `pre-commit` and no `pre-push`, the output reads
  `skip hooks — .githooks/pre-push is not tracked here` and `--check` exits 0. An adopter that owns
  its own pre-commit acquires no permanent unclearable finding.
- **AC6** — a resolved hook that cannot be read prints `pre-push: UNKNOWN, could not read both sides`
  with both values, never `ok`.
- **AC7** — `.githooks/pre-push`'s header no longer claims tracked equals active by construction; it
  names the repo-global-and-absolute condition and the measurement behind it.
- **AC8** — `grep` for `is not written`, `opened as a backlog item` and `is possible and is not` over
  the gotcha record returns **0**. The criterion is the WHOLE FILE: rev-2 scoped it to one heading
  and the same false assertion stood under another.
- **AC9** — `bash tools/check-wiring.test.sh`: **92 passed, 0 failed**, exit 0.

## The branch field, and why `unknown` is correct rather than broken

The supplying checkout's branch is read with `git -C "$(dirname "$dir")" rev-parse --abbrev-ref HEAD`
and is best-effort: a hooks dir whose parent is not a work tree yields `unknown`, which the line
prints rather than aborting the arm. In the planted fixtures the parent is a bare temp dir, so
`unknown` is exactly what a correct probe says there.

`git ls-tree HEAD -- <path>` is used instead of `git rev-parse HEAD:<path>` because a POSIX-emulation
shell on Windows can mangle the `<rev>:.dotpath` spelling and report ABSENT for a present file. Both
spellings were tested on this node and both answered correctly here; `ls-tree` is kept because the
trap is recorded and the safer spelling costs nothing.

## What this does NOT do, and the gate header says so

It REPORTS a divergence; it does not PREVENT one. A push made after the report still runs the other
checkout's hook. Closing that window needs a refusal inside the hook itself, which changes what the
push boundary REFUSES — a wider decision than this row opened, and a filed follow-up. The gotcha
record therefore KEEPS its landing-boundary documented check rather than losing it to this unit.
