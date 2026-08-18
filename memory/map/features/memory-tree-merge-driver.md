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
lexicon-verbs = []
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

**TWO PLANES, split by the ROW SHAPE and never by the anchor grammar.** One stateless predicate —
`^\s*[-*]\s`, applied to each line in isolation, no parser state — classifies every line as ROW or
STRUCTURE. Structure goes to `git merge-file` positionally; only the row set is key-merged here. The
partition is the shape because the grammar has never keyed every row-shaped line, and handing git
the lines it cannot key would hand it exactly the population git is measured to DUPLICATE at rc 0 —
the one corruption class git commits. Everything else git was measured CORRECT on: a heading, a
placeholder, a repeated lead-in note, a sub-heading opened in two sections.

**The two planes recombine through a SKELETON, which is what makes the recombination ordered rather
than guessed.** Each of `%O %A %B` is projected to a line list of the same length in which every row
becomes one token line — its id when the grammar keys it, a digest of its text when it does
not — and every structure line passes through byte for byte. `git merge-file` merges the three
skeletons, and the merged skeleton is walked and its tokens substituted. Keying a token on the ID
rather than the text is what keeps a row EDIT invisible to the structure plane; otherwise every row
edit is a structural change and git starts arbitrating record text, which is where duplication comes
from. The digest drops the terminator and trailing whitespace, which stops line form
smuggling a duplicate — a final copy with no newline and an interior copy with one hash the same —
and KEEPS leading whitespace, because indentation is nesting and nesting is content. Collapsing
`- x` and `  - x` onto one key made rule 4 substitute one side's body for the other's and destroy a
line no side had touched.

**A conflict region that is entirely tokens on both sides resolves by CONCATENATION; any disputed
structure line is always a conflict.** Both sides of a diff hunk sit between the same context lines,
so when every disputed line is a row, section membership is not in dispute — only order among
siblings, which is not semantic, because ids are labels and not ranks. Dedup happens ACROSS the two
sides and never within one: the within-side form is set union wearing a rule's clothes, and it
deletes a legitimately repeated note out of an append-only record at rc 0. The converse rule is the
one the whole design rests on — structure is precisely the class git is right about and this driver
was wrong about three times running.

**The row plane is `key -> LIST`, never `key -> line`.** A markdown file may legitimately carry the
same row-shaped line twice, and collapsing those made such a file FAIL ITS OWN IDENTITY MERGE — a
permanent whole-file conflict no author action clears.

**The properties are POSTCONDITIONS on the WRITTEN BYTES, not inferences from the keying.** Bytes and
not the in-memory emit list: a terminator defect is invisible in a list where two glued records are
still two elements. Five checks run on every verdict, over the merged lines with conflict REGIONS
excised — no row-shaped line written more often than any one input carried it; no leading ID written
more often (the line half compares exact text, and two nodes minting one id with different prose are
two different lines AND two different `raw:` keys, so this half is the only net for that shape); no
row filed under a `#` heading no input filed it under; per-key CONSERVATION, which is explicitly not
uniqueness; and structure identity against the merged skeleton, markers excluded on BOTH sides.
Scoping them to clean verdicts was wrong — an author resolves the marked hunks and reads everything
outside them as settled, so a duplicate emitted beside an unrelated conflict is invisible at rc 1
exactly as it is at rc 0.

**The bar is `git merge-file`, mechanically, in every fixture.** Being quietly worse than the merge
this driver replaces is the standard it is held to, and it is now arithmetic rather than judgement:
every case runs a live control on the identical three blobs, losing a line git keeps or writing a row
more often than git does fails the suite by name, and conflicting where git resolves correctly is
counted by name against a shrink-only constant (2 today: a row one side MOVED and the other
DELETED, in both directions, and nothing else). Every case runs a control — two of twenty-eight
groups did before kit 2.2 — but the ARITHMETIC comparison can only bind where the control EXITS 0,
which is 16 of 40 cases and is floored so a fixture edit cannot quietly drop one. Saying it that
precisely matters: a suite that reads stronger than it is, is how this driver shipped rc-0
corruption twice.

**Failure is closed.** A merge driver that raises exits non-zero WITHOUT writing `%A`, and git then
leaves the path unmerged holding OURS-only content with no markers — the incoming rows are simply
absent and nothing says so. That is silent, unrecoverable loss and strictly worse than the crash that
caused it, so every exception becomes a whole-file conflict instead. This is also why the grammar
import is DEFERRED into the first anchor call: at module scope an unreadable `extract.py` kills the
process before `main()` can write anything.

**Newlines are never translated, at SEVEN sites.** This repo's nodes run `core.autocrlf=true` and the
governed indexes are CRLF in the worktree while their index blobs are LF, and git hands a merge
driver WORKING-TREE-format temp files. So the read is `newline=""`, the three `git merge-file` temps
are `newline=""`, its stdout is captured as BYTES and decoded by hand (upstream passes `text=True`
here, which is universal-newline mode and undoes the line above), and the result goes out through
`write_bytes`. Stating only the write half makes every identity `cmp` red and makes a real merge
rewrite the whole file's line endings. Three more arrive with the skeleton: a token carries the
terminator of the row it replaces; every marker line the DRIVER synthesizes carries the file's
dominant terminator; and a row substituted for a token carries the TOKEN's terminator, never the one
it carried in its source blob. The last is not a refinement — measured, an unterminated final row
relocated by the merge kept its empty terminator and FUSED TWO RECORDS ONTO ONE LINE at rc 0 with no
markers and a clean audit line, where the control refuses at rc 1 with both intact.

**The conflict style is PINNED at the single `git merge-file` call site.** `git merge-file` honours
the invoking repo's `merge.conflictStyle` and git runs a merge driver from the top of the worktree,
so a node-local `diff3`/`zdiff3` reaches this process and adds a third `||||||| base` section. The
reconciliation rules are defined over an ours side and a theirs side; under three sections a
token-only region stops being token-only, the concatenation rule evaporates, and the same driver
returns different verdicts per node on identical blobs. `-c merge.conflictStyle=merge` overrides a
configured value (measured, git 2.54). The cost, stated: the driver's own conflict output carries no
base section even where the adopter asked for one.

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
`resolve_python` is source-and-call and git never goes through `tools/run-gates/run-gates.sh`, so the runner's
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
- **An ORDINARY conflict is now a scoped hunk; a POSTCONDITION refusal is still whole-file.** The
  scoped half is new and structural: a disputed structure line is re-emitted as git's own region, in
  place, so a heading rename conflict is one marker pair around one heading rather than a 186-line
  sandwich over a ~90-line index. A postcondition refusal still goes through `main()`'s fail-closed
  handler and writes `%A` and `%B` in full. Correct and loud, and heavier than it needs to be: the
  exception could carry the offending keys and the handler could mark only their neighbourhood.
  Refusals are rare by construction — every fixture that triggers one is a shape git itself either
  duplicates or conflicts on — so this is ergonomics, not safety.
- **The adopter's `merge.conflictStyle` is overridden, not honoured.** Pinning the style at the call
  site is what keeps the region shape node-independent, and the price is that an adopter who chose
  `diff3` does not get a base section in the conflicts this driver writes. The alternative — define
  the rules over three sections and discard the base — keeps their config meaningful and costs a
  marker grammar on the merge path, which is the class of state all three defect rounds lived in.
  Recorded as a trade rather than an oversight.
- **Fenced code blocks are not parsed**, deliberately. A `- ` bullet inside a fence is a ROW and is
  tokenized. The cost is bounded and conservative — two identical bullet-shaped lines inside two
  fences can trip the duplicate cap and produce a refusal — and measured at zero reachability here:
  `memory/DECISIONS.md` and all four backlog shards carry no fenced blocks. A fence-tracking state
  machine on the merge path of an append-only record buys a rare case and pays in exactly the state
  the two-plane design exists to delete.
- **A file that already carries a COMMITTED, unresolved conflict block refuses where git resolves.**
  Git's own markers are now labelled with the token sentinel so the reconciliation cannot mistake an
  input's block for one it produced — before that, rule 3 concatenated the block, erased all three
  marker lines and silently accepted both disputed wordings at rc 0. What remains is that `settled()`
  still excises the input's block by its marker TEXT, so conservation sees rows it cannot account
  for and refuses. Loud and lossless, on a file the hygiene gate reds anyway.
- **The delete/modify branch's scoped conflict block is unplaceable for the plain shape.** A row edit
  is invisible to the skeleton by design (that is what lets a heading rename survive a row edit), so
  when the other side deletes the row there is no token left to place the block at, and the run ends
  in a whole-file refusal instead of the scoped hunk `resolve_rows` promises. No content is lost;
  git returns a scoped conflict here, so it is an ergonomics gap of the same family as the one above.
- **No `regenerate` driver, and there will not be one.** `ort` checks the merge result out only AFTER
  the per-path merges run, so a generator invoked from inside a driver renders from the pre-merge tree
  and commits a stale artifact. `memory/LIVE.md` and `memory/ledger/<month>.md` stay regenerated by
  `gen_build_index.py` after the merge, not during it.

## Reuse affordance

seam: merge-rows.skeleton — reuse for any three-way merge where SOME lines must be merged by key and the rest positionally: project each input to a token list, let `git merge-file` merge that, key-merge the tokens separately, recombine. Extend via a second line-class predicate, never by re-deriving placement. (This replaces the retired `merge-rows.split_regions` seam, which offered the three-region prose-then-rows model — withdrawn with kit 2.2 because that model is what the two planes replace.)
seam: pyrun.sh — reuse whenever a tool OUTSIDE `tools/run-gates/run-gates.sh` must run a python script (a git driver, a hook, an editor integration); extend by calling it, never by naming a launcher.
