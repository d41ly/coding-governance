# cMendedVintage — the acceptance ledger for unit 5

**Serves:** journal DEPL-cMendedVintage-5

*Node `c`. BACK-FILLED 2026-09-17 by a later pass, NOT by the pass that built the unit — the
filename carries the date of the unit's own commits, `65baa6ee` and the comment-prose follow-up
`7034a135`, both 2026-09-16. Two kinds of line follow and they are not the same evidence. Where a
criterion is answered by a command or a file that could be replayed or read from here, it was,
against this worktree, and the result is given. Where it is answered by what the building pass
measured, the commit that recorded it is cited AS the commit's record and named as such. No merge
bar, no `*.test.sh` and no self-test runner ran in this pass, so not one of the legs this unit's
section 7 names was executed here.*

## The one thing worth reading twice

**This unit's headline criterion was never observed as written, and the spec says so itself.** AC1
asks for an `update --write` run against a scratch target with the flag exported, printing one
`ran` line per kit. Rev-2 note (c) records that the pass ran each declared argv directly instead,
because standing up a scratch target for the three kits costs a memory-tree seed-and-stop plus a
lexicon ratification; the commit says the same thing in one line, `Not run: update --write end to
end against a scratch target`. What was observed is the three entrypoints, not the loop that calls
them, and the loop is what the unit exists to feed.

**The text two of these criteria grade has been rewritten since, by two later units.**
`DEPL-cMendedVintage-16` narrowed the lexicon `[[outcome]]` probe AC2 is about, and
`DEPL-cMendedVintage-7` reworded the comment sentences AC3 is about when it flipped the flag's
default. The three `[[regenerate]]` argv themselves are untouched. Each line below says which text
it is speaking about, because a ledger read against the wrong bytes is a ledger about nothing.

**Evidences:** DEPL-cMendedVintage-5

- AC1 — `bash tools/lexicon/adopt-lexicon.sh --render` — and its two siblings,
  `bash tools/drift-audit/adopt-drift-audit.sh` and
  `bash tools/memory-recall/adopt-memory-recall.sh --scaffold`. Commit `65baa6ee` records all three
  run directly in this tree, each exiting 0 and each rewriting its own `rendered` row. That is the
  observation, and it is per-argv. The half the criterion actually asks for — an update against a
  scratch target with `GOVKIT_RERENDER=1` exported, printing one `ran` line per kit — is recorded by
  that same commit as NOT run, and spec rev-2 note (c) hands it to `DEPL-cMendedVintage-7`. It is
  owed. One of the three renders is legible in the diff and the other two cannot be: `65baa6ee`
  moves `.claude/skills/lexicon/SKILL.md` from `gov:kit lexicon@1.4` to `@1.5`, while the
  drift-audit and memory-recall Skills carry no `gov:kit` line at all — grepped at this tip, neither
  file contains that string — so their renders reproduce their own bytes and would leave no trace
  either way.
- AC2 — `no-project-layer` — commit `65baa6ee` records the observation and the two controls that
  make it a measurement rather than an assertion: a staged target with `.lexicon.conf` removed put
  the lexicon argv's real exit 1 through `classify_outcome` and `outcome_accepted` and it was
  ACCEPTED; with `ok` removed the same exit was refused; with the conf present it did not match the
  block at all. THAT WAS S4'S BLOCK, whose probe was `must_not_exist = ".lexicon.conf"` and nothing
  else, and it is not the block in the tree today. Read at this tip, the same `[[outcome]]` now
  probes `{ must_exist = ".claude/skills/lexicon/SKILL.md", must_not_exist = ".lexicon.conf" }`:
  `DEPL-cMendedVintage-16` added the discriminator because an acceptance declared by an absence
  alone is satisfied by every run that died before writing. The `code`, the `means` and the
  `ok = true` this criterion names are unchanged by that narrowing, so what AC2 asked is still true
  of the tree — of a strictly narrower state than the one that was measured.
- AC3 — `git grep -n "GOVKIT_RERENDER" -- tools/lexicon/kit.toml tools/drift-audit/kit.toml tools/memory-recall/kit.toml`
  — replayed at this tip from the repo root. Exit 0, one hit per descriptor and three in all, each
  on the opening line of that kit's `[[regenerate]]` comment. That is where the flag IS named; it is
  not evidence that no other sentence in those files claims an `update` re-renders without naming
  it, which is the direction S5's Red-when is about and which only arm 7l walks. The sentences are
  not the ones
  this unit wrote: `7034a135` rewrote all three the same day, after the checklist caught each of
  them stating a derived count beside the rules that own it, and `DEPL-cMendedVintage-7` rewrote the
  opening clause again when the default flipped, so what the grep reads today declares the re-render
  as the default and names `GOVKIT_RERENDER=0` as the decline. The criterion's other half — the
  selfcheck exiting 0 with its re-render-claims note counting these three kits, which `65baa6ee`
  records as a population of five — is the commit's record and not this pass's: that leg was not
  re-run here.
- AC4 — `bash tools/check-kit-versions.sh` — commit `65baa6ee` records it green. The leg was not
  re-run here, so the constants were read at both ends instead, with `git show` at the build's base
  `859daa67` and a grep at this tip: `KIT_LEXICON_VERSION` 1.4 to 1.5, `KIT_DRIFT_AUDIT_VERSION`
  1.10 to 1.11, `KIT_MEMORY_RECALL_VERSION` 1.8 to 1.9. All three still read the higher value at
  this tip, so nothing since has moved them again, and the well-formedness half of the criterion is
  the leg's and is the commit's word.

## What this ledger does NOT claim

That the merge bar is green, or that any leg of it ran, in either pass. The section 7 names are all
unobserved for this unit: `govkit selfcheck`, `kit version markers`, `lexicon wiring`,
`drift-audit wiring`, `memory-recall skill wiring` and `kit placeholders`. Two of them are cited
above as commit records, which is what the building pass saw, not what this pass verified.

That `update`'s re-render loop has ever executed these three blocks. Nothing in this tree evidences
it. The argv were exercised as programs; the declaration that makes an update reach them was read,
never run, and AC1 is owed on exactly that gap.

That the lexicon `[[outcome]]` block this unit shipped was sound. It was not, deliberately and with
the defect written into its own comment: the build brief told the pass to ship S4 as specified and
not to narrow it, and `DEPL-cMendedVintage-16` was moved to run immediately after for that reason.
AC2 above grades the narrowed block because that is what the tree holds; the block this unit landed
accepted a failed first scaffold as an unconfigured posture, and `classify_outcome` is not scoped
per step, so that hole was open on `apply`'s CONFIGURE too for as long as it stood.

That an adopter received any of this. gov keeps no `.governance/` receipt of its own, so no live
install was touched or measured from here, and the spec's own rollout section says the first
behavioural run belongs to a later unit.
