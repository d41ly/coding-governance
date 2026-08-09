# memory-tree merge driver — the row-keyed three-way merge for the authored indexes

```toml
feature = "memory-tree-merge-driver"
title = "Row-keyed merge driver for memory/DECISIONS.md and memory/backlog/*.md"
status = "shipped"
streams = ["tooling"]
decisions = []

[claims]
gate-legs = ["row-keyed merge driver replay"]
kits = []
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
[paths]
globs = [
  "tools/memory-tree/merge-rows.py",
  "tools/memory-tree/merge-rows.test.sh",
  "tools/lib/pyrun.sh",
]
```

## Constraints & why

Two indexes in this tree are AUTHORED and appended to by every node — `memory/DECISIONS.md` and the
four `memory/backlog/<FAMILY>.md` shards — so two nodes landing work in the same window collide on
the same file. `merge=union` is the one-line answer and is rejected on measurement, not preference:
union never loses an id, but upstream measured it introducing a duplicate in 147 of 151 historical
`DECISIONS.md` conflicts, and these files hold zero duplicate ids. A design that measured only LOSS
concluded union was safe.

**Only the row block is key-merged.** A file is three regions — preamble, the first-to-last anchored
line inclusive, trailer — and the region rule WINS at the block boundary. `memory/DECISIONS.md` opens
with a title, two blockquote routing lines and the `## PLAY — playbook` heading before its first
anchored row at `:8`; all of that is preamble and takes an ordinary `git merge-file` three-way merge.
Without the split, an unconditional "a line the grammar cannot key conflicts" rule conflicts on every
single merge and the auto-resolve is unreachable. Inside the block the opposite rule applies: an
unkeyed line attaches to the FOLLOWING anchor, because `## KICK — kickoff`, `## TOOL — tooling` and
the `*(none yet)*` placeholder sit interleaved BETWEEN anchored rows. A driver that collected them in
a side list and re-emitted them at the end would move every section heading to the bottom of the file
while exiting 0.

**The properties are POSTCONDITIONS on the written file, not inferences from the keying.** The
keying speaks only for the lines the grammar keys — measured at 35 of this corpus's 73 rows, because
the ratified `…-9b` correction form falls outside the shared session era's trailing `\b`. So three
checks run on every verdict, over the merged lines with conflict REGIONS excised: no ROW-SHAPED line
written more often than any one input carried it, no leading ID written more often (the line half
compares exact text and two nodes minting one id with different prose are two different lines), and
no row filed under a `#` heading no input filed it under. Scoping them to clean verdicts was wrong —
an author resolves the marked hunks and reads everything outside them as settled, so a duplicate
emitted beside an unrelated conflict is invisible at rc 1 exactly as it is at rc 0. Each of the three
was written against a REPRODUCTION, and each reproduction's control is `git merge-file`: being
quietly worse than the merge this driver replaces is the standard it is held to, and a conflict is an
acceptable answer for an append-only record while silently wrong content never is.

**Failure is closed.** A merge driver that raises exits non-zero WITHOUT writing `%A`, and git then
leaves the path unmerged holding OURS-only content with no markers — the incoming rows are simply
absent and nothing says so. That is silent, unrecoverable loss and strictly worse than the crash that
caused it, so every exception becomes a whole-file conflict instead. This is also why the grammar
import is DEFERRED into the first anchor call: at module scope an unreadable `extract.py` kills the
process before `main()` can write anything.

**Newlines are never translated, at four sites.** This repo's nodes run `core.autocrlf=true` and the
governed indexes are CRLF in the worktree while their index blobs are LF, and git hands a merge
driver WORKING-TREE-format temp files. So the read is `newline=""`, the three `git merge-file` temps
are `newline=""`, its stdout is captured as BYTES and decoded by hand (upstream passes `text=True`
here, which is universal-newline mode and undoes the line above), and the result goes out through
`write_bytes`. Stating only the write half makes every identity `cmp` red and makes a real merge
rewrite the whole file's line endings.

**The wiring is two facts, and only one of them is committed.** `.gitattributes` declares
`merge=rows`; `merge.rows.driver` is per-node git config. A node that never ran
`bash tools/check-wiring.sh --fix` falls back to git's built-in line merge with a warning — the
pre-change behaviour, which is why the attribute and the config can land in one commit without a flag
day, and why `check_merge_rows` exists to turn "declared" into "wired" per node.

## Shared seams

The anchor grammar is IMPORTED from `tools/memory-recall/extract.py` — `grammar_for(root)` for the id
alternation and the four anchor regexes, `anchor_at(line, g)` for the "which id does this line
DEFINE" predicate — and never vendored. A second copy of a regex is this repo's catalogued drift
class, and a stale-but-single grammar beats two that disagree. Because `grammar_for` re-resolves
`.memory-tree.conf` at an explicit root, an adopting repo with different `FAMILIES` keys on its own
ids with no change here.

`tools/lib/pyrun.sh` is a shim over `tools/lib/resolve-python.sh`, not a second resolver: it sources
the canonical block rather than inlining it, so it is deliberately absent from the inline-copy parity
population (which is derived by `git grep -l '^# >>> resolve_python'`). It exists because
`resolve_python` is source-and-call and git never goes through `tools/run-gates.sh`, so the runner's
`$PYBIN` substitution cannot reach a merge driver.

`tools/check-wiring.sh`'s `first_of` supplies the two-layout path resolution both the driver and its
wiring arm need (`tools/memory-recall/` here, `memory-recall/` in a copy-installed adopter).

## Gaps

- **Not packaged for adopters.** `adopt-memory-tree.sh` is untouched. A copy-installed memory-tree kit
  lands at `<root>/memory-tree/` and cannot reach `tools/lib/pyrun.sh` at all, so shipping the driver
  to adopters is a kit-layout change with its own blast radius. The driver already RESOLVES both
  layouts, so the follow-up is a packaging question rather than a rewrite.
- **The grammar is read from the PRE-merge worktree.** The driver is a pure function of `%O %A %B`
  plus the worktree's grammar, so a merge that itself changes `FAMILIES` keys its index merge on the
  old grammar. Bounded rather than hidden: no row is invented or duplicated, and at worst a row whose
  anchor only the NEW grammar recognises is treated as unkeyed content.
- **Conflict markers are written with LF terminators** even into a CRLF file. Harmless — a marker line
  is deleted during resolution — but it is a real asymmetry with the four newline sites above.
- **A postcondition refusal is a WHOLE-FILE conflict, not a scoped hunk.** The three checks run after
  the merge is assembled, so a refusal goes through `main()`'s fail-closed handler, which writes
  `%A` and `%B` in full between markers. Correct and loud, and heavier than it needs to be on a
  ~90-line append-only index: the exception could carry the offending ids and the handler could mark
  only their neighbourhood. Refusals are rare by construction (every fixture that triggers one is a
  shape git itself either duplicates or conflicts on), so this is ergonomics, not safety.
- **Two DIFFERENT empty sections opened one per side still conflict where git resolves.** Each side's
  lead-in for its new row is a different, overlapping slice of the same base furniture, so the
  adjacency dedup cannot suppress either and one heading is emitted twice; the trailing row's lead-in
  three-way then conflicts. Measured: driver rc 1 with both rows correctly filed and a redundant
  heading block, `git merge-file` rc 0 and clean. Fails CLOSED and no content is lost, so it is
  noise rather than damage — but it is a shape where the driver is still worse than the merge it
  replaces, and closing it means merging lead-ins as text against the base rather than picking one.
- **A `%B` cross-section MOVE of a shared row is discarded at rc 0.** `order` is seeded from `%A` and
  shared keys are never repositioned, so if only theirs moved a row between sections, ours' position
  wins silently. The placement postcondition does not catch it: it asks whether the merged section
  matches an input that carries the row, and ours' does. LOW today — the backlog shards carry no
  `## ` sections and `DECISIONS.md` is append-only in practice — but it is the one placement shape
  the driver still decides by preference rather than by evidence.
- **No `regenerate` driver, and there will not be one.** `ort` checks the merge result out only AFTER
  the per-path merges run, so a generator invoked from inside a driver renders from the pre-merge tree
  and commits a stale artifact. `memory/LIVE.md` and `memory/ledger/<month>.md` stay regenerated by
  `gen_build_index.py` after the merge, not during it.

## Reuse affordance

seam: merge-rows.split_regions — reuse for any three-way merge of a file that is prose-then-rows; extend via a second region predicate rather than a second copy of the block arithmetic.
seam: pyrun.sh — reuse whenever a tool OUTSIDE `tools/run-gates.sh` must run a python script (a git driver, a hook, an editor integration); extend by calling it, never by naming a launcher.
