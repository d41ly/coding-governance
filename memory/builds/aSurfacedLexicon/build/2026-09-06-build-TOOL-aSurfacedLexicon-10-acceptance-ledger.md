**Serves:** journal TOOL-aSurfacedLexicon-10

# Build pass, step 6 — `--expand`, the widening the frozen clusters bound

Node `a` · 2026-09-06 · build `aSurfacedLexicon` · streams tooling. ONE unit, built twelve units
after the rest of this build landed, on an owner ruling that resolved the fork the run had parked.

**The headline is the shape of the resolution, not the feature.** F1 asked where the candidate
computation lives, and both LISTED options fell to the veto ladder: one broke the unit's only
observed-RED criterion, the other reversed a write guard whose header records a real adopter
committing a file literally named `--help` through a 62-leg bar. The park said so and stopped, because
a veto is not a licence to take the vetoed option. The owner took the third route the park had
MEASURED and could not itself ratify — an importable `derive_candidates` beside the closure, reached
from the engine's dispatcher — and both vetoes are satisfied rather than waived: the closure keeps ONE
home, so the staged break at that expression still reds the arm; and the flag-arity guard is untouched,
because the module is imported and its `argv` never sees a flag.

**Evidences:** TOOL-aSurfacedLexicon-10
- AC1 — `bash tools/lexicon/adopt-lexicon.sh --expand` against a conf carrying a non-empty `expanded=` — REFUSES, names the stamp it read, exits non-zero. The fixture reaches that state by RUNNING `--stamp` rather than by hand-writing the line, so the arm also proves the writer and the guard agree about the value.
- AC2 — the same fixture conf rewritten byte-wise to CRLF — the refusal STILL fires, and the arm asserts the ALREADY EXPANDED VERDICT rather than the exit code alone, because a non-zero for another reason satisfies the weaker form.
- AC3 — `--expand` against a fixture declaring only `build` and `read` — the proposal set is NON-EMPTY, every entry is a representative of the shipped clusters, a declared row is not re-proposed, and each row carries its negative. One proposal is reached through an ALTERNATIVE spelling (`fetch_w` proposes `load`, never `fetch`), which is what proves the closure resolved a form to its representative instead of echoing the corpus's own word.
- AC4 — the unruled tail on that same fixture — non-empty, DISJOINT from the proposal list, carrying the fixture's own off-canon tokens, under a header that says in words that these are not proposals and never will be.
- AC5 — `live = {forms.get(v, v) for v in counts}` staged into `tools/lexicon/scaffold_lexicon.py` — the subset assertion BREAKS and the proposal list names the off-canon token itself. The rev-3 replacement break is the one used: deleting the cluster filter instead raises `KeyError`, so the arm would red BY EXCEPTION and certify nothing about the predicate.
- AC6 — `python tools/lexicon/lexicon.py --expand` over THIS repo — exits 0, proposes nothing, and SAYS SO, naming a non-zero live-cluster count. Asserted as a message and not as silence, because an empty proposal is the normal state of an adopted tree and a run that printed nothing would pass an assertion on silence.
- AC7 — `--expand --stamp` on a committed fixture — writes `expanded="<date> <sha>"` as EXACTLY ONE line, the conf keeps LF bytes, and a second `--expand` hits AC1's refusal. The dirty half is armed too: a tracked working-tree change REFUSES, while `git status --porcelain` is asserted NON-EMPTY at the moment the stamp succeeds — which is the whole reason the predicate is the tracked two-sided diff and not porcelain.
- AC8 — `python tools/lexicon/lexicon.py` — the sibling unit's narrowed guard against an emitted block header is still green, and the LOOSE arm rationing that substring to one line in the scaffold is green too. The second is the one this pass nearly tripped: the register this kit writes in would have spent the ration in a docstring.

## What the revert matrix found, and the mechanism it forced

**One mechanism was ungated when first written, and the suite said so on its first run.** Reaching the
closure by import makes the engine depend on a file the kit deliberately supports an adopter NOT
having — the scaffold guard's absent-file branch REPORTS for exactly that reason. The self-containment
refusal caught it: with the scaffolder dropped, `--check` redded on a dependency that adopter cannot
satisfy, which is the red-nobody-can-fix that branch exists to avoid.

The fix is a named tuple of ONE optional sibling, and its own comment states what it does not buy: it
says nothing about HOW the import is written, so a module-level import would pass it and then break
the engine at import time for the same adopter. The property that actually holds is armed at RUNTIME
on both modes — `--check` green with the file deleted, `--expand` REPORTING rather than raising — and
the allowance itself is staged: emptying the tuple reds that adopter's gate.

**Three more mechanisms were closed the same way**, each because a guard or a landed arm objected
rather than because a review noticed:

- The import must be function-local. A top-level one raises `AttributeError` out of the sibling,
  because it reads an engine constant in its own module body above the engine's definition of it —
  so the engine would stop importing at all and every leg touching the kit would red.
- `--expand` refuses a trailing argument. Every other mode drops `argv[2]` silently, so `--stamp` —
  the exact word an operator reaches for, because the wrapper takes it — would have run a full
  expansion, written nothing, and reported success.
- The stamp is written IN PLACE, never appended. The conf reader takes the LAST occurrence of a
  repeated scalar while the shell guard reads the FIRST, so an appended second stamp would leave the
  two readers disagreeing and the once-only refusal silently off. A freshly scaffolded conf also ends
  without a trailing newline, which is the other way an append corrupts the line above it.

## What the closing review found, and the shape it shared

Round 2 is `reviews/2026-09-06-review-TOOL-aSurfacedLexicon-10-diff-review-round2.md`: **BLOCKED**,
raw 16, confirmed 13, refuted 3, collapsing to ten distinct defects. Four lenses returned and none
died, so its central zero — no path by which an off-canon token reaches the proposal list — is
evidence rather than an unread population. The closure held; everything found sits one ring out.

**The blocker was mine and it was not in the spec at all.** I bumped `KIT_LEXICON_VERSION` to 1.2 and
left all four `gov:kit lexicon@1.1` markers behind. `govkit selfcheck` carries no guard, so it runs on
every bar and the unit could not have landed. The branch-local checker that should have caught it
PRESENCE-checks the constant and pairs no lexicon marker — two checkers, one question, and the weaker
one is the one a session reaches for. Both are fixed: four markers bumped, and
`tools/check-kit-versions.sh` now pairs them in the shape it already used for another kit. Its RED was
observed by reverting one marker.

**Three findings were the mode lying about its own measurement**, which is this repo's own named
class and the reason the review earns its cost:

- An empty `live` has two OPPOSITE causes and the branch asserted the harmless one over a population
  it never checked — printing "not a run that failed to measure" on a tree where nothing was measured,
  including one where `--check` is RED with `DEAD PROBE`. It now REFUSES with 2, naming the empty
  extraction as the symptom, and the non-zero is what stops the wrapper spending the one-shot stamp.
- `live` holds representatives while `declared` held raw table keys, so a conf declaring a canon
  ALTERNATIVE never subtracted its cluster — the mode proposed a row its own reader then refuses,
  from a legal green state any hand-edited table can reach.
- The tail read every offender where `--check` reads the unwaived ones, under a comment claiming
  parity with `--check`. An adopter with a verb waiver got their accounted-for exception handed back
  as an unresolved idiom.

**Two more were guards with nothing behind them.** The stamp's tracked-only dirty test swallowed
`.lexicon.conf` itself, so an untracked declaration could be stamped with a sha naming a tree that
does not contain it — the natural first-adoption path. And the AC2 arm's header called it the proof of
the CRLF inversion; it is green with or without the mechanism, because for a NON-empty value a CR
residue makes it more non-empty, never less. The direction that actually inverts is an EMPTY
`expanded=""`, which now has its own arm, with the half that is unexercisable on a git-bash node
announced as a skip rather than left in a comment.

**And the citation fix re-created the defect it was closing.** The rev-5 entry replaced the spec's
stale line numbers with re-measured ones — measured at the PRE-BUILD tree, and stale in the commit
that shipped them, moved by this unit's own insertions. Struck and not replaced; the criteria cite
expressions.

Every one of the ten is folded. Five new fixture arms grade the classes that had none.

## Two things this pass did NOT build, and why

**S4's tail is not computed by the new function.** The engine's measurement pass already classifies
that exact population as `unruled`, on every bar, and prints its count; a second predicate in the
scaffolder would be two answers to one question with the copy nobody grades. The verb reads the
engine's classification, so the tail's definition count IS the number `--check` reports — 897 over 493
distinct tokens on this tree, both derived by the run rather than written here.

**S7 names no pin.** It used to order the output to name three scalars at three line numbers, one of
which no longer exists, while asserting that a block which does exist could not. Every clause was
wrong in a different direction, in a criterion whose subject is that a value written beside its source
rots. The output points at `--measure` instead.
