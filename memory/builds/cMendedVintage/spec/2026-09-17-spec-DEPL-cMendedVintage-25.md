# DEPL-cMendedVintage-25 — the renormalize cleanliness guard reads paths, not whitespace tokens

**Status:** CLOSED · rev-2 · 2026-09-17 · node c · Tier-2 · base 859daa67 · streams deployer · order 35

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-17-build-DEPL-cMendedVintage-25-acceptance-ledger.md](../build/2026-09-17-build-DEPL-cMendedVintage-25-acceptance-ledger.md) | journal | — |
| [2026-09-17-prompt-DEPL-cMendedVintage-25-2-build-brief.md](../prompts/2026-09-17-prompt-DEPL-cMendedVintage-25-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Both renormalize cleanliness guards ask `git diff --name-only HEAD` which pinned paths are dirty and
then split its answer on arbitrary whitespace. A dirty path whose name carries a space arrives as two
tokens and matches nothing in the pinned set; a dirty path carrying a non-ASCII byte arrives
C-quoted and matches nothing either. The guard passes, `git add --renormalize` runs over the whole
pinned population, and the operator's uncommitted content is folded into the index of a repository
gov does not own — which is verbatim what the refusal two lines above says it exists to prevent.
Ask git for NUL-delimited paths at both sites, and leave behind a check that reaches every other
place this engine word-splits git.

## 2. Scope (IN)

- **S1** Both renormalize guards invoke `git diff --name-only -z HEAD` and split the answer on NUL,
  dropping the empty tail. The sites are `_cmd_update`'s and `_cmd_apply`'s renormalize guards —
  BY SYMBOL, because the line numbers rev-1 carried had already moved when this was built. Observed by AC1
  and AC2.
- **S2** A permanent class arm in `tools/govkit/selftest.py` refuses any git invocation in
  `govkit.py` whose stdout reaches a record-splitting read — a bare `.split()` OR a `.split("\0")`
  — without `-z` in its argv. It takes the module
  path as a parameter so its own failing case can be staged against a scratch copy rather than
  against the shipped engine. Observed by AC3 and AC4.
  AMENDED rev-2: the specified predicate graded the BARE form alone, and after S1 both fixed sites
  NUL-split, so deleting `-z` from either left it green — measured by staging exactly that break.
  A NUL split over a newline-terminated answer yields ONE element and every membership test below
  it goes quietly false, which is this unit's own defect wearing the repaired code's clothes. The
  arm also EXCLUDES a git call whose argv carries a `*splice`, and prints how many it excluded: the
  first run over the real tree reddened `dirty_claimed_paths`'s `_names` closure, which is correct
  because all four of its callers pass `-z` through the splice.
- **S3** The three remaining bare-split git reads conform rather than being exempted: `:1296` reads
  gov's own `git ls-files` and is the same defect one repository over, and `:4564` and `:7874` take
  a fixed field out of `ls-tree` and `ls-files -s`. Measured in a scratch repo: `-z` changes the
  terminator and not the field order, so both field reads return the same mode and the same oid over
  a spaced path. Observed by AC4.
  AMENDED rev-2: a FOURTH site conforms, and the predicate does not reach it. `_cmd_apply`'s
  post-renormalize LF verification reads `git ls-files --eol` and takes its path by a TAB split,
  which a space never breaks — so it is outside S2's population and stayed outside it. The QUOTING
  half still reached it: measured, git prints `"caf\303\251.md"` and the set it is tested against
  holds the raw bytes, so a pinned non-ASCII path was silently dropped and that post-condition went
  vacuous for exactly the population the guard above protects. Found by reading the near-miss list
  S2's first real-tree run printed, which is the whole reason that list is printed.
- **S4** Fixture arms for both verbs, one with a pinned path named with a space and one with a
  non-ASCII name, each left dirty and each asserted to produce the refusal NAMING that path. Two
  spellings, because the two failures reach the guard by different routes — one splits, the other
  quotes. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- No extraction of a shared renormalize body, which is the review's more thorough proposed form.
  Section 4 states what was measured about the two bodies and why the cheaper fix is the one
  specified; the guarantee against their divergence moves to S2's arm, which is where it belongs.
- No repair of the asymmetry the review noticed in passing: `update` subtracts `deleted` from its
  absence test and `apply` does not. That difference is deliberate and documented at `:8567`, and a
  unit closing a parse defect is the wrong place to re-adjudicate an exemption.
- No change to either refusal's text, its population, or what the run does once it holds the right
  set of dirty paths. The guard's decision was always correct; only its input was wrong.
- No widening of S2's arm past `tools/govkit/govkit.py`. The same word-split in `selftest.py`,
  `matrix.py` or a sibling kit is invisible to it, and section 5's observability row says so in the
  arm's own header rather than leaving a reader to infer coverage it does not have.
- No rewrite of the two NUL readers this file already has. `eol_population` and the `_names` closure
  inside `dirty_claimed_paths` are correct today, and churning correct code during a blocker repair
  buys nothing and risks the next finding.

### Edges

- **consumes-from** `DEPL-cMendedVintage-10` — that unit added `update`'s renormalize, which is the
  second of the two sites. Without it this is a one-site fix in `apply` and the class arm has one
  hit to report rather than the pair that makes the arm worth having.
- **hands-off** external — an adopter whose tree holds a path with a space or a non-ASCII byte.
  Nothing else in this build reads either guard; the three sibling blocker units touch other
  functions in the same file and share no hunk with this one.

## 4. Design

**What was measured.** In a throwaway repo on node `c` under git 2.55.0.windows.1, a dirty `a b.txt`
and a dirty `café.txt` were committed and modified. `git diff --name-only HEAD` printed `a b.txt`
unquoted on its own line and `"caf\303\251.txt"` C-quoted; splitting that on whitespace yields `a`,
`b.txt` and the quoted token, none of which is a member of the raw set `eol_population` returns from
`git ls-files -z`. The same diff with `-z` printed both names raw and NUL-terminated. That settles
the question the review left open about `core.quotePath`: it is not a second hazard, it is the same
one, and `-z` alone disables the quoting. Adding `-c core.quotepath=false` alongside `-z`, as the
review's proposed patch does, is inert — it is specified OUT, because a knob that changes nothing is
a knob a later reader will believe is load-bearing.

**What is reasoned rather than measured.** Both the population read and the diff read pass
`text=True`, so both decode with the same codec whatever the locale is; a lossy codec would mangle
both sides identically and membership would still hold. On this node the codec is UTF-8 and both
sides round-tripped exactly, so the symmetry argument was not exercised and is recorded as
reasoning.

**Why the parse is fixed in place and no helper is extracted.** The review proposes one helper both
verbs call. The two bodies were read at HEAD and they agree on four lines and disagree on five
things: the precondition (`update` runs only when it wrote the pin block and carries no findings,
`apply` runs whenever there are pins), the set of paths exempted as gov's own writes
(`written_paths | _reaped` against `set(staged)`), the absence test's exemption (`update` subtracts
`deleted` and the reaped orders, `apply` subtracts nothing), the post-step (`apply` sets
`_renormalized` and re-reads the index with `ls-files --eol`, `update` does not), and the reporting
of the empty case. A helper expressing both needs more parameters than it has body, which is the
abstraction this repo's §12 spends a bullet refusing. The thing that actually stops the two copies
drifting further is a check that grades both, and that is S2.

**The class arm.** `tools/govkit/selftest.py` already holds `check_retired_flags`, a source-text
predicate over `govkit.py` with `ast` imported and a declared row table, and S2's arm is its sibling
rather than a new mechanism. It parses the module, finds every `subprocess` call whose first
argument is a list literal beginning `git`, records whether that argv carries `-z`, and then finds
every record-splitting read of the `stdout` of one — a bare `.split()` or a `.split("\0")`, inline
on the call or through the name the call was assigned to, resolved in the NEAREST ENCLOSING FUNCTION
scope. Amended per rev-2 S2; the one-spelling form is what could not fail. A hit is a red naming the line. The one exemption is declared as a row carrying its
reason, not written into the predicate: a `--format=` argv whose placeholders cannot produce a path,
which today is `derive_attribution`'s commit walk — named by SYMBOL, because three units landed
in this file while this one was specced and every line number the finding cites is wrong. The next such format supplies a row, exactly as the next
retired flag supplies a row rather than a regex.

AMENDED rev-2 — the helper set. Section 4 described the walker without naming its helpers, and two
of the obvious names lead with verbs `.lexicon.conf` does not declare. What shipped is ONE
`_extract_git_argv`, returning `None` for a non-git call, a sentinel for one whose argv it cannot
read, and the constant list otherwise; the split test is inline at the loop. "Is it git" and "can I
read its argv" are one question asked once, and two functions answering it would drift.

The arm asserts its own liveness before it asserts anything else, because a walker that resolves no
calls reports a clean pass over nothing and that is indistinguishable from coverage. It derives and
prints both figures — git invocations found, split sites found — and never reads a count anybody
typed. What it does not reach is stated in its own header: only this module, only an argv written as
a list literal at the call, and never whether the guard reading those paths is correct.

## 5. Production-readiness checklist

- security — this is the security row. The guard decides whether gov stages content it did not
  write into a repository it does not own, and today a path it cannot parse is a path it cannot
  refuse. Fixing the parse strictly narrows what `git add --renormalize` is allowed to reach.
- perf / scale — one flag and one different split character, over output already being read. The arm
  parses one module once per suite run.
- error / empty / loading states — a clean tree returns the empty string, so the NUL split yields one
  empty element and the existing filter drops it; measured. A target with no pinned `eol=lf` path
  still takes the existing nothing-to-re-stage branch, and a git invocation that fails is reported by
  the same path as before, unchanged.
- observability — the refusal already names up to four offending paths, and after this change the
  names it prints are the names on disk rather than fragments of them. The arm prints its derived
  population on every run, red or green.
- risks — the real one is arrival behaviour: an adopter with a spaced or non-ASCII dirty pinned path
  starts being refused where they were silently being staged. That is the guard working, and AC1 and
  AC2 are written to observe it rather than to route around it. The secondary risk is a false red
  from the arm over a git read that is safe by construction; S3 answers it by conforming the three
  such sites instead of teaching the predicate to forgive them.
- testing — AC1 and AC2 drive the real verbs against scratch fixtures, AC3 stages the arm's own
  break, AC4 grades the shipped module. The permanent homes are declared in section 7.
- migration — none. No receipt field, no descriptor key and no on-disk format moves.
- user docs — none owed. Neither `WIRE-INTO-PROJECT.md` nor any `help/` page documents the
  renormalize step's path parsing, and a refusal that now fires correctly needs no new sentence to
  explain it.

## 6. Acceptance criteria

- **AC1** — When a fixture target holds a pinned path named `a b.txt`, left dirty in the worktree,
  and
  `python tools/govkit/govkit.py update --target <fixture> --write`
  runs, the run REFUSES and the refusal names that path in full. Red when: the fixture's dirty path
  carries no space, in which case the whitespace parse finds it too and the arm passes identically
  at BASE while the defect is untouched.
  fixture: `update`'s guard is reached only on a run that wrote the pin block and collected no
  findings, so the fixture must be a target the `.gitattributes` write completes cleanly against.
- **AC2** — When a fixture target holds a pinned path whose name carries a non-ASCII byte, left dirty,
  and
  `python tools/govkit/govkit.py apply --target <fixture>`
  runs, the run REFUSES and names that path. Red when: the fixture creates the non-ASCII path but
  never dirties it, so `git diff` prints nothing, both parses agree on the empty set and the arm
  observes only that a clean tree is clean.
- **AC3** — When `check_git_split_parses` is driven over a scratch copy of the engine with `-z`
  deleted from one git invocation, it FAILS naming the line it was deleted from. Red when: the
  predicate matches on the literal `-z` anywhere in the call's source text rather than in its argv
  list, which a comment mentioning the flag would then satisfy.
  AMENDED rev-2: the break is staged at `_cmd_update`'s renormalize diff, whose comment block SPELLS
  `-z` and is left in place, so the red-when is exercised by the same run rather than reasoned about.
  As first written this criterion could not fail at all — see S2.
- **AC4** — When `check_git_split_parses` runs over the shipped `tools/govkit/govkit.py`, it reports
  zero hits and prints a derived, non-zero count of both git invocations and split sites. Red when:
  the walker resolves no calls at all — a renamed import or an argv built outside the call would do
  it — and the zero-hit result is vacuous rather than clean.
  figure: both counts are DERIVED by the arm at observation time; neither is pinned in this spec nor
  in the arm.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: `tools/govkit/selftest.py` · a scratch copy of the engine with one `-z` deleted stages the
class arm's failing case, and two fixtures with a spaced and a non-ASCII dirty pinned path stage the
behavioural ones, one per verb · no floor moves, and the `BRANCH_PIN` floor in
`tools/govkit/refusal_join.py` is untouched because this unit adds and removes no refusal branch.

## 8. Open questions

- **Q1 — exempt the two field-indexed reads, or conform them?** RESOLVED (agent, 2026-09-17, delegated):
  conform them. A per-site exemption list is a second population to keep true, and this repo already
  records that an exemption naming a site that has moved silently widens the surface it was written
  to narrow. Measured: `-z` on `ls-tree` and on `ls-files -s` changes the record terminator and not
  the field order, so `split()[0]` still yields the mode and `[1]` still yields the oid over a path
  with a space. Two characters each is cheaper than a row each.
- **Q2 — does the arm belong in `selfcheck` rather than in the selftest?** RESOLVED (agent, 2026-09-17,
  delegated): the selftest. `selfcheck` is the registry-and-surface ratchet and its leg is
  deliberately unguarded, so putting a `govkit.py` source lint there would run it on every bar to
  grade a file that had not moved. The selftest leg is guarded on `tools/govkit/`, which is exactly
  the condition under which this predicate can newly fail.

## 9. Revision log

- rev-2 · 2026-09-17 · node c · amended mid-build, after measuring. Four divergences, all in S2/S3
  and all recorded above: the predicate grades two split spellings rather than one, because the
  specified one could not fail at either site this unit fixes; a spliced argv is excluded and
  counted, because the specified one reddened a correct read on its first run over the real tree; a
  fourth git read conforms, found in that run's near-miss list rather than by the predicate; and the
  helper set is one `extract` rather than three functions, two of which led with undeclared verbs.
  Section 4's `core.quotePath` measurement was re-run independently on node c under git 2.55.0 and
  REPRODUCED: `-z` disables the quoting as well as the terminator, so `core.quotepath=false` beside
  it stays specified OUT.
  §8 moved too, in shape and not in substance: both forks were marked with a resolver the
  machine does not read, which the hygiene gate named the moment the header went terminal.

- rev-1 · 2026-09-17 · initial draft, authored mid-build after the closing review adjudicated finding
  H1 a HIGH found independently by four lenses. Every line the finding cites was re-opened at HEAD
  `4c4d42fe` before this was written, and the `core.quotePath` question the finding left open was
  measured rather than assumed.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "parse git plumbing output as NUL-delimited paths instead of word-splitting"`
returns no seam to extend: the ranked candidates are name-stem matches on `parse` and `path` across
unrelated kits, and the only `govkit.py` entries it surfaces — `git_pathspec`, `dirty_claimed_paths`,
`check_paths_never_lost` — are callers of git rather than readers of its output. NO EXISTING SEAM
FITS as a function to call. What the probe did surface is that the CORRECT spelling already lives in
this file twice: `eol_population` reads `git ls-files -z` and splits on NUL, and the `_names` closure
inside `dirty_claimed_paths` does the same for four different plumbing reads. Neither is reusable
from the renormalize sites — one answers a different question and the other closes over a pathspec —
but between them they establish that this repo spells the NUL read inline wherever it needs one, and
that a fourth spelling wrapped in a helper would be the outlier rather than the convergence.

The class arm reuses a real seam rather than inventing one: `check_retired_flags` in
`tools/govkit/selftest.py` is already a source-text predicate over `govkit.py`, already takes its
module path as a parameter so its failing case can be staged, already declares its population as
rows carrying provenance, and already opens with a liveness assertion and a paragraph naming what it
does not check. S2's arm is that shape with a different predicate, which is why this unit adds a
check and not a checker.

Recall terms used: govkit renormalize eol population pinned path dirty guard word-split NUL-delimited
git plumbing quotePath ls-files diff --name-only selftest class arm.
