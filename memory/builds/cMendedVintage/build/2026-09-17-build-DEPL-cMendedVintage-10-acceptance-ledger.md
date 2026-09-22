# cMendedVintage — the acceptance ledger for unit 10

**Serves:** journal DEPL-cMendedVintage-10

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar, no self-test suite and
no `*.test.sh` ran in this pass. Every observation below was taken by running the real engine against
a scratch fixture target at the shell, and the one criterion no fixture here can reach is recorded
OWED rather than claimed.*

## The one thing worth reading twice

**The spec named a doc correction that does not exist.** rev-2's `hands-off external` edge and its
section 5 user-docs line both said `WIRE-INTO-PROJECT.md` states that `update` never edits
`.gitattributes`. It does not. That file's four mentions of the path are all about an ADOPTING repo's
own EOL rules for the hygiene checker, and the three shipped carriers of the never-writes claim are
elsewhere: two comments in this engine, both rewritten here, and one line in the deploy Skill that is
about `apply` and was already false at BASE. rev-3 withdraws the edge rather than leaving a handoff
nobody could discharge.

**The subtraction was armed, not asserted, and the arming needed a second fixture rule.** With only
the target's own
`*.md text eol=lf`
rule, gov's own write is outside the renormalize population and removing the subtraction changes
nothing — the arm would have passed over a broken guard. Pinning
`.gitattributes`
itself in the fixture puts gov's write inside the population, and then the two sides separate: with
`_rn_ours` emptied the write run exits non-zero naming `.gitattributes`, with the subtraction in
place every arm is green. Both were observed before the arm was written.

**The stale-order unlink collided with the renormalize, and the fixture found it.** A target that
COMMITS its outbox left an index entry behind the unlinked order; `eol_population` reads git's
tracked set, so the reaped file came back as a pinned path missing from the worktree and refused the
very renormalize this unit adds. The unlink now unstages with `--ignore-unmatch` and the path joins
both subtraction sets. Measured on a fixture whose own attributes pin `*.md`, which is the shape any
target with a docs pin has.

**Two shipped selftest arms were flipped, by name.** The first is the arm labelled
`NEVER edits .gitattributes -- that destination is apply's`
and the second is the one labelled
`it writes an ORDER instead`.
Both carry the `[-2]` prefix, both were `DEPL-dCarriedReceipt-2`'s ratified design, and both now
assert the opposite. Rewritten rather than deleted, so the inversion reads as a decision in the diff
instead of as lost coverage.

**Evidences:** DEPL-cMendedVintage-10

- AC1 — `lf_pin_block` — on a scratch fixture installed with `push-main`, tampered INSIDE the marker
  pair and committed, `update --target <fixture> --write` exits 0, prints
  `wrote the lf-pin block [spliced]`
  and leaves the block byte-identical to what `lf_pin_block` renders from `lf_pins` over the same
  selection, compared through the engine's own `find_block` rather than against a second render. The
  target's own rules outside the block survived the splice.
- AC2 — `i/lf` — the fixture's index blob for a pinned path gov does not claim was forced to CRLF
  with `git hash-object -w` plus `git update-index --cacheinfo`, and `git ls-files --eol` reported
  `i/crlf` before the run. After `update --write` the same path reads `i/lf`, and the run printed
  `renormalize: re-staged`
  with its path count. The forcing is what makes this non-vacuous: without it every pinned path in
  the fixture was already LF and the arm would have graded nothing.
- AC3 — `--write` — a read-only run on the same moved-block fixture reports `pins-moved`, leaves
  `.gitattributes` byte-identical by `read_bytes()` comparison, and leaves the forced CRLF index blob
  at `i/crlf`. Both halves are asserted, because a write placed in the classification loop would
  break the first and a renormalize placed outside the write phase would break the second.
- AC4 — `.gitattributes` — OWED. Reaching it needs a kit whose `[check]` goes green-to-red across the
  run, and `push-main` declares `[check] none`, so the fixture this unit builds cannot produce the
  transition the rollback keys on. The `-14` roll fixture can, but its scratch kits declare no
  `[[lf_pin]]` and so synthesize no attributes row. Section 7 names two new arm groups and neither is
  this one, so the spec never promised an arm here. What IS in the tree is the mechanism: the
  snapshot entry is appended above the write and below nothing, the rollback loop reaches it for
  every rolled-back kit, and the row is restored whole. None of that was executed. Owed to a suite
  run with a fixture that pins and rolls back at once.
- AC5 — `git diff --cached` — with a pinned path the run did not write left dirty in the worktree,
  `update --write` reports
  `the pinned population is not clean relative to HEAD (notes.md)`
  and `git diff --cached --name-only` in the fixture does not list that path. The victim is
  deliberately NOT receipt-claimed: with a claimed path the earlier dirty precondition fires first
  and the arm grades that refusal instead, which is how the first draft of this probe passed for the
  wrong reason.
- AC6 — `update-pins.md` — a stale order was planted in the fixture's outbox and committed before the
  write run. Afterwards no `update-pins.md` exists there and the run printed
  `removed a stale .governance/outbox/update-pins.md`.
  The unlink is unconditional rather than keyed on this run having written one, which is the
  criterion's own `Red when` and is untestable any other way once the order stops being written.

One criterion is OWED: AC4. The other five were observed against the real engine.

## What did not run, and why

`tools/govkit/selftest.py` gained fifteen arms and one fixture rule and was NOT executed as a suite,
by this pass's own mandate. Every expression those arms use — `govkit_module()`, `marker_pair`,
`GA_BLOCK_ID`, `find_block`, the `git ls-files --eol` field split, the `hashlib` digest — was replayed
verbatim against the same fixture in a scratch runner and all returned the asserted values. What was
not replayed is the suite's own `run()` wrapper, which threads `--to GOV_PIN` into every `update`; the
arms above it in the same block already run under that pin and exit 0, so the fixture is clean at that
vintage, but this is stated rather than assumed.

`govkit selftest`, `govkit selfcheck`, `govkit refusal join` and `govkit acceptance matrix` are the
gates section 7 names and all four are owed to the bar this run closes with. Two checkers WERE run
directly, because both grade bytes this commit writes:
`bash tools/check-install-prefix.sh --check`
reports clean at 268 shipped files and 136 recorded files with none rising, and
`python tools/govkit/refusal_join.py`
enumerates 252 branches, one above its previous pin, which is this unit's single new refusal.
`python tools/check-spec-tokens.py` was run with this spec held at SPECCED rather than CLOSED, because
a CLOSED spec is terminal and goes ungraded: the graded set went 43 live specs and 962 tokens to 44
and 988, so rev-3's twenty-six tokens were actually examined.

## What the bug-class checklist changed

`python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` named sixteen classes and two landed on
this commit's own bytes.

`ledger-token-wrapped-across-a-line-joins-nothing` — hygiene check 23 failed on AC1, and the cause was
in the SPEC rather than in this ledger: AC1's invocation span was wrapped across two lines, which put
every later backtick on the wrong parity so `lf_pin_block` was read as a closing tick and became no
token at all. Reflowed; rev-3 logs it as editorial.

`git-rm-cached-refuses-a-diverged-index-blob` — the stale-order unstage was written without `-f`, and
`git rm --cached` refuses a path whose index blob differs from both HEAD and the worktree. A stale
order re-staged after its commit is exactly that path, and a silent refusal there leaves the index
entry standing and hands the renormalize a pinned path missing from the worktree — the failure the
unstage was added to prevent. `-f` added, with the reason on the call.

`fixture-passes-by-finding-nothing` was checked twice and changed the fixture both times: the CRLF
index blob is FORCED rather than hoped for, and the second attributes rule was added because without
it removing the subtraction changed no arm's verdict.

## The two findings this unit did not fix

**`apply` refuses its own renormalize on a target that pins `.gitattributes`.** Its `ours` set is the
`staged` list, which never carries that path, so `apply` writes the block, finds it dirty against
HEAD and refuses — measured, exit non-zero, on the fixture built to arm this unit's subtraction. Same
class as the defect S4 exists to prevent, one verb over. Not repaired here: this unit was scoped to
move a write between verbs, and `apply`'s set is `DEPL-dSettledRoster`-adjacent surface.

**`skills/deploy-governance/SKILL.md` says the `.gitattributes` block write has no implementation.**
That was already false at BASE — `apply` has written the block since before this build — and it is
now false twice over. Left standing because correcting a Skill is not in this unit's declared write
set, and re-dispatching to touch one sentence buys less than recording it here.
