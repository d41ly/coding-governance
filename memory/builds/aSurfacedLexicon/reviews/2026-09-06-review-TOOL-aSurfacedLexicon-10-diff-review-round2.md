**Serves:** diff-review TOOL-aSurfacedLexicon-10

# Closing diff review — the widening holds its canon, and cannot land

Tier-2 closing diff review, round 2 · 2026-09-06 · node `a` · build `aSurfacedLexicon` · streams
tooling. Round 1 is the spec audit at
`2026-09-06-review-TOOL-aSurfacedLexicon-10-spec-audit.md` (CLEAN WITH FIXES); this round grades the
code that shipped against it.

Reviewed range: **67232c4f...3f6715e8** — sixteen files, +900/-75, the whole of
`TOOL-aSurfacedLexicon-10` in one commit.

## Verdict: BLOCKED

One blocker, one high, five mediums, three lows. The blocker is not a design defect: a version
constant moved and its four markers did not, and the leg that pairs them is unguarded on the merge
bar. It is a one-commit fix. Everything below it is real but none of it breaches the canon boundary
the unit was built to defend.

## The question the unit was built to answer, answered

**No path was found by which an off-canon token reaches the proposal list.** Four lenses returned,
none died, and each was primed on that specific hazard, so this zero is evidence rather than the
absence of a report. The closure at `tools/lexicon/scaffold_lexicon.py:143` —
`live = {forms[v] for v in counts if v in forms}` — is the whole boundary and it is intact: a token
with no cluster fails the `in forms` test and cannot enter `live` by any route, the extraction to
`derive_candidates()` gives it one home with two callers as the spec required, and both callers grade
it. The corpus votes on WHICH concepts are live and never on what any of them is called.

What the review found instead sits one ring out. Three of the ten defects are the mode LYING ABOUT
ITS OWN MEASUREMENT — a reassuring zero, a tail drawn from the wrong population, an arm that grades
nothing — and two more are records that re-create the exact defect they were written to close.

## Findings

| # | Sev | Site | Defect |
|---|-----|------|--------|
| F1 | BLOCKER | `tools/lexicon/lexicon.py:78` | Kit constant bumped to 1.2, all four `gov:kit` markers left at 1.1; `govkit selfcheck` is RED and unguarded |
| F2 | HIGH | `tools/lexicon/lexicon.py:2446` | Empty proposal on an unmeasured corpus prints "not a run that failed to measure" |
| F3 | MEDIUM | `tools/lexicon/scaffold_lexicon.py:145` | `declared` subtracted in raw-token space against `live` in representative space |
| F4 | MEDIUM | `tools/lexicon/adopt-lexicon.sh:267` | `--stamp` dirty-tree guard passes when `.lexicon.conf` is itself untracked |
| F5 | MEDIUM | `tools/lexicon/lexicon.py:2456` | Unruled tail reads all offenders where `--check` reads unwaived |
| F6 | MEDIUM | `tools/lexicon/selftest.py:3682` | AC2 is green with or without the mechanism its comment says it proves |
| F7 | MEDIUM | `spec/2026-09-04-spec-aSurfacedLexicon-10.md:498` | The stale-citation fix republishes five line numbers measured at the base |
| F8 | LOW | `tools/lexicon/lexicon.py:2565` | Dispatch comment asserts an exit-1 invariant `run_expand` breaks 140 lines up |
| F9 | LOW | `tools/lexicon/adopt-lexicon.sh:276` | The NO COMMIT refusal is the one new guard whose red has never been observed |
| F10 | LOW | `spec/2026-09-04-spec-aSurfacedLexicon-10.md:191` | §5 still claims one existing code path changed; two `--check` reads also moved |

Ten rows carry the thirteen confirmed findings: F2 was independently reported three times (ids 4, 6,
12) and F8 twice (ids 5, 15). The lens ledger's raw ids are named in each section so the merge is
traceable.

---

### F1 — BLOCKER · `tools/lexicon/lexicon.py:78` · the unit cannot land *(id 3)*

`KIT_LEXICON_VERSION` went 1.1 -> 1.2 while every tracked marker stayed behind.
`python tools/govkit/govkit.py selfcheck` exits 1 at 3f6715e8 with exactly four problems, all of them
this pair:

- `tools/lexicon/lexicon.py:2` — `gov:kit lexicon@1.1`
- `tools/lexicon/canon.py:2` — `gov:kit lexicon@1.1`
- `tools/lexicon/README.md:1` — `gov:kit lexicon@1.1`
- `tools/lexicon/LEXICON.md:1` — `gov:kit lexicon@1.1`

Those are the only failures reported, so the base at 67232c4f was green and this diff caused the red.
The `govkit selfcheck` row in `tools/gate-legs.json` carries **no `guard` key** (subject `repo`, chunk
`declarations`), so it runs on every bar including the push-boundary one.

Why branch-local checking missed it: `tools/check-kit-versions.sh:239` is a presence check on the
constant only (`need "KIT_LEXICON_VERSION" tools/lexicon/lexicon.py …`). It does not pair the lexicon
markers the way it pairs pytest-parallel-guardrails' four kept artifacts. Two checkers, one question,
and the weaker one is the one a session reaches for.

`.claude/skills/lexicon/SKILL.md` is already correct — it is rendered from the constant. So an
adopting tree would carry four files advertising 1.1 for a kit whose own Skill says 1.2.

**Fix.** Bump the marker on all four carriers in the same commit as the constant, then require
`python tools/govkit/govkit.py selfcheck` exit 0.

**Left-shift.** Add the lexicon carriers to `tools/check-kit-versions.sh` as a paired assertion, in
the shape it already uses for pytest-parallel-guardrails — so the cheap branch-local checker reds on
this class instead of leaving it to the push boundary. The gate that would have caught this exists;
it just does not cover this kit.

---

### F2 — HIGH · `tools/lexicon/lexicon.py:2446` · a reassuring zero *(ids 4, 6, 12)*

The empty-candidate branch prints, verbatim:

> All 0 cluster(s) with a live site in this corpus already carry a row … That is the NORMAL result on
> an adopted repo and not a run that failed to measure.

`live` is empty for two opposite reasons: every live cluster is declared, or nothing was measured at
all. The branch asserts the first and explicitly denies the second, over a population it never
checked. Reproduced three ways:

- A fixture whose `LANGS` are all `dark` (`py::dark conf::dark`, one `def frobnicate_v` present) —
  the headline prints with `All 0 cluster(s)`, a tail of `0 leading token(s) across 0 definition(s)`,
  no `NOTE`, exit 0. `measure_pass`'s DEAD PROBE arm `continue`s on `dark`, so nothing fires.
- The same with an armed-but-empty extension (`py:python-ast:parser`, no `.py` files).
- Worst: a genuine dead extractor (`txt:shell-tokens:probe` over a `.txt` with no definitions), where
  `--check` is RED with DEAD PROBE. `--expand` still leads with the healthy sentence, then closes
  with "The proposal above came off the same walk and is unaffected by them" — false precisely when
  the problem is a dead extractor, because an extractor that found nothing cannot vote a cluster
  live. The empty proposal IS the symptom.

This is not a hazard the kit is unaware of. `--check` on the same trees prints `graded=0`,
`coverage — armed 0 of 9` and `INERT DECLARATION`; `run_expand` returns before `check_pass` and
inherits none of it. The sibling branch twenty lines up (`SCAFFOLDER ABSENT`, line 2407) already draws
exactly this distinction — "Nothing was measured; this is not an empty proposal". The function knows
the shape and does not apply it here.

Reachability is structural, not exotic: the module's own docstring says shell ships recall-dark by
law, so a shell/conf-only adopter lands here by construction, reads a complete vocabulary, and can
then spend the one-shot `--stamp` on it.

**Fix.** `derive_candidates` already returns `counts`. Branch on it in `run_expand` before the
candidates branch: when `not derived["counts"]`, print a DEAD-PROBE-shaped report naming the armed
extension population and saying no extractor produced a definition, so an unmeasured tree is
distinguishable from a satisfied one. Keep the NORMAL wording only for `live` non-empty with
`candidates` empty.

**Left-shift.** AC6 is the only arm asserting a non-zero cluster count and it runs
`cwd=KIT.parent.parent` — this repo, which can never be empty. Add a fixture arm over an all-`dark`
declaration asserting the NOTHING MEASURED line, so the class is graded against a corpus that CAN be
empty rather than one that cannot.

---

### F3 — MEDIUM · `tools/lexicon/scaffold_lexicon.py:145` · a proposal its own reader refuses *(id 7)*

`live` holds cluster representatives (`forms[v]`, line 143); `declared` is the raw `VERBS` key set
(`declared = set(declared)`, line 145). `candidates: sorted(live - declared)` therefore subtracts
across two different spaces, so a table declaring a canon ALTERNATIVE never subtracts its cluster.

Reproduced: a fixture declaring `fetch` in `VERBS` over a corpus containing `fetch_w`. `--expand`
exits 0 and proposes

```
load      read a store into memory — NOT `fetch`
```

Pasting that row exactly as the EXPAND header instructs makes the declaration RED — `--check` refuses
with "VERBS declares as BANNED a token that is itself a row: fetch". The mode hands the operator a row
its own reader rejects, and if they ran `--expand --stamp` the one supported widening has already been
spent on it.

The precondition is a legal green state: the `fetch`-declaring conf produced no problems, and
`check_declaration` has no arm refusing a `VERBS` row that names a canon alternative. Any hand-edited
table can reach it, which is exactly the population `--expand` exists to serve.

Note what this is NOT: no off-canon token enters. `load` is a legitimate representative. The defect is
that the cluster was already declared under another spelling.

**Fix.** Fold the declared table through the form index before subtracting —
`declared = {forms.get(v, v) for v in declared}`.

**Left-shift.** A fixture arm declaring a canon alternative and asserting its representative is NOT
proposed. Same fixture shape as the existing candidate arms, one different `VERBS` row.

---

### F4 — MEDIUM · `tools/lexicon/adopt-lexicon.sh:267` · a stamp naming a tree with no declaration *(id 1)*

The `--stamp` guard is the two-sided tracked diff `git diff --quiet || git diff --cached --quiet`.
That is tracked-only by design, and the design note above it is correct about why: a kit fixture
copies the directory in untracked, so a porcelain-based refusal could never be exercised. But the
exemption swallows `.lexicon.conf` itself as collateral.

Reproduced in a fixture with `src/a.py` committed and `.lexicon.conf` left untracked (`?? .lexicon.conf`):
`bash tools/lexicon/adopt-lexicon.sh --expand --stamp` exits 0 and writes
`expanded="2026-09-06 2a85e99e…"` into the untracked conf. Both properties the code states in its own
words fail at once:

- The sha does not name the tree the proposal was measured against — that tree contains no
  `.lexicon.conf` at all.
- The ALREADY EXPANDED message's claim that "what the stamp buys is a visible edit in a tracked file"
  is false when the file is untracked.

This is the natural first-adoption path: `--scaffold` writes the conf, the operator curates it, then
expands. Nothing forces a commit in between.

**Fix.** One arm before `git rev-parse HEAD`, leaving the existing exemption intact:

```sh
git ls-files --error-unmatch -- "$CONF" >/dev/null 2>&1 || {
  echo "lexicon-adopt: UNTRACKED DECLARATION — refusing to stamp. …"; exit 1; }
```

Every existing arm stays green: all fixtures already stage `.lexicon.conf`.

**Left-shift.** The reason the selftest cannot see this is that both `run_case` and the shell-surface
block run `git add -- src/a.py .lexicon.conf`, so the conf is tracked in every fixture. Add the same
shell fixture with the conf left out of `git add`, asserting the named refusal — the failing case for
the new arm, which is also the failing case the existing guard never had.

---

### F5 — MEDIUM · `tools/lexicon/lexicon.py:2456` · two surfaces, one corpus, different answers *(id 8)*

The unruled tail loops `measured["offenders"]["verb"]`. The `--check` split at lexicon.py:1905 and the
PINS census both read `measured["unwaived"][kind]`; the waiver split happens at line 1589. So the tail
includes waived offenders and `--check` does not.

Reproduced with one waiver row (`frobnicate_v`), same tree:

- `--check`: `P1 verb graded=2 offenders=0 (debt=0 + unruled=0) waived=1`, exit 0
- `--expand`: `NOT PROPOSALS — 1 leading token(s) across 1 definition(s)`, listing `frobnicate`

That directly contradicts the comment above the loop, which calls this "the number `--check` prints on
every bar" and identifies a second predicate as the only divergence risk. The divergence arrived
without one.

An adopter with verb waivers is handed already-accounted-for exceptions as a work list of unresolved
house idioms. `tools/lexicon/lexicon-verb-waivers.txt` has zero non-comment rows, so this repo's own
corpus cannot observe it, and AC4's fixture is waiver-free.

**Fix.** Read `measured["unwaived"]["verb"]` so the tail is the population the bar actually ratchets —
or keep all offenders and say so on the line and in the comment. Either is defensible; the current
state is a comment asserting one and code doing the other.

**Left-shift.** A fixture arm with a waiver row that pins which population the tail means. This repo's
empty waiver registry is the reason no existing arm can distinguish them, and that emptiness is not
guaranteed to last.

---

### F6 — MEDIUM · `tools/lexicon/selftest.py:3682` · an arm that cannot fail *(id 2)*

The AC2 arm carries a header naming it the proof of the CRLF inversion — "THE INVERSION, which is the
failure this whole read shape exists to prevent" — and asserts the verdict rather than the exit code,
which the comment offers as what makes it strong.

It is green with or without `read_conf_scalar`'s `tr -d '\r'`, on both platforms. Four combinations,
four passes. For the `expanded` key the refusal fires on a NON-empty value, and a CR residue makes a
value more non-empty, never less: on a GNU node the value reads `2026-09-06 <sha>"\r` — still
non-empty, still ALREADY EXPANDED, still non-zero; on this git-bash node MSYS grep drops the CR before
sed and `with_tr` and `no_tr` return byte-identical values, which the function's own comment already
concedes.

The direction the residue actually inverts for this key is the opposite one: a CRLF conf carrying
`expanded=""` yields the residue `"\r`, non-empty, read as "already expanded" — permanently refusing
the one supported widening to an adopter who cleared the stamp on a CRLF checkout. No arm covers it.

Bounding the impact rather than refuting it: the same mechanism IS genuinely armed for `ratified` at
selftest.py:744 (empty-value direction, same function), so deleting the `tr` would still red the suite
on a GNU node. What is confirmed is the §7 class — an arm carrying a header claiming a strength it
does not have.

**Fix.** Add the direction the residue inverts: a CRLF conf with an empty `expanded=""`, asserting
`--expand` PROCEEDS rather than refusing. Keep the existing arm if useful, but stop labelling it the
inversion proof.

**Left-shift.** MSYS grep strips the CR before sed on node `a`, so half of this is unexercisable here.
Announce it as a named skip beside the arm saying which half goes unexercised on git-bash — a prose
comment in the header reads as coverage, which is how this arm got its label in the first place.

---

### F7 — MEDIUM · `spec/2026-09-04-spec-aSurfacedLexicon-10.md:498` · the fix re-creates the defect *(id 13)*

The rev-5 entry closing the prior round's stale-citation finding publishes six re-measured line
numbers and asserts they were "re-measured against the tree the build actually runs on". Five were
measured at the pre-build tree 67232c4f and are stale at 3f6715e8 — the same commit that ships them:

| Cited | Actual at 3f6715e8 | Drift |
|-------|--------------------|-------|
| `scaffold_lexicon.py:184` (the closure) | `:143` | 41 |
| `scaffold_lexicon.py:112` (flag arity) | `:174` | 62 |
| `scaffold_lexicon.py:217` (`CANON` comment) | `:272` | 55 |
| `adopt-lexicon.sh:373-377` (overwrite refusal) | `:465-469` | 93 |
| `adopt-lexicon.sh:225` (`ratified` read) | `:326` | 101 |
| `.lexicon.conf:113` | `:113` | holds |

The shift is exactly the build's own insertions above them — `derive_candidates` at
scaffold_lexicon.py:101 and `read_conf_scalar` at adopt-lexicon.sh:182. The same figures are
republished as the "Actual" column of the correction table in
`reviews/2026-09-06-review-TOOL-aSurfacedLexicon-10-spec-audit.md:53-59`, so a reader following either
correction lands on unrelated code. Stale halves also survive at spec lines 24, 89, 191, 319, 349,
358, 379, 402, 471, 473 and 522.

**Fix.** Strike the numbers from the rev-5 entry and the review table; cite the expressions the
criteria already cite (`live = {forms[v] for v in counts if v in forms}`,
`if len(argv) != 2 or argv[1].startswith("-")`, `# PROPOSED from the SHIPPED CANON`,
`already exists — refusing to overwrite`, `read_conf_scalar ratified`). Keep the pre-build sha beside
any number that must stay.

**Left-shift.** This is the second round in a row to find it, which is the argument for a gate rather
than a third correction. A records check that flags `<tracked-path>:<digits>` citations inside a build
folder whose commit also touches that path would catch the whole class — the citation and the code
move in one commit or the citation is wrong. Failing that, the documented check is: a spec correcting
line numbers cites expressions, never digits.

---

### F8 — LOW · `tools/lexicon/lexicon.py:2565` · a false invariant at the dispatch site *(ids 5, 15)*

The comment says `--expand` "must not be able to reach a pin, a waiver or an exit code of 1 by any
path, however the file is refactored", and draws a parallel to `run_suggest`. The parallel is false:
`run_suggest` returns only 0 and 2, while `run_expand` returns 1 at line 2426 from
`except (ConfError, ValueError) as e: print(f"lexicon: {e}"); return 1`. Verified by execution — a
fixture with a malformed conf (`BOGUS_HEADER:`) exits 1 through `--expand`.

No functional break: `adopt-lexicon.sh` collapses every non-zero to 1 before stamping. And the
contract is recorded correctly elsewhere — `run_expand`'s own docstring says the accurate, milder
thing, "exits 0 on any tree it can read". So this is two answers to one question with the wrong copy
at the dispatch site, in a file where the comments are a substantial part of the product.

**Fix.** Narrow the comment to what holds: it cannot reach a pin or a waiver, and its only non-zero
exits are the declaration refusal (1) and the absent scaffolder (2). Or return 2 from the `ConfError`
arm and make the sentence true as written.

**Left-shift.** None proposed. A gate over comment semantics costs more than the class is worth; the
docstring is already the correct copy, and the cheap discipline is that an exit-code claim lives with
the function, not at the dispatcher.

---

### F9 — LOW · `tools/lexicon/adopt-lexicon.sh:276` · a gate whose red was never seen *(id 16)*

`grep -n "NO COMMIT" tools/lexicon/selftest.py` returns nothing. Every sibling refusal this unit added
does have an arm: SCAFFOLDER ABSENT at selftest.py:3597, DIRTY TREE at :3644, ALREADY EXPANDED at
:3672 and :3683.

Reachable, reproduced in a scratch repo: `git init -b main` plus an untracked `.lexicon.conf` gives
`git diff --quiet` exit 0, `git diff --cached --quiet` exit 0, and `git rev-parse HEAD` exit 128 — so
`sha` is empty and the refusal fires. The spec knew about the unborn state (lines 277-278) but treats
it purely as a fixture obstacle to be removed by committing, never as a case to exercise, which is
exactly why the arm does not exist.

The guard itself is correct. §7: a new gate is not landed until its failing case has been observed.

**Fix and left-shift are the same edit.** One arm beside the AC7 block: `git init` a fixture, write
the conf and corpus without committing or staging, run `--expand --stamp`, assert non-zero and
`NO COMMIT` in the output. If the branch is judged unreachable in practice, delete it and let
`rev-parse` fail loudly instead.

---

### F10 — LOW · `spec/2026-09-04-spec-aSurfacedLexicon-10.md:191` · a scope claim that outlived its scope *(id 14)*

§5 Rollout reads: "The mode allowlist edit at `tools/lexicon/adopt-lexicon.sh:184` is the only change
to an existing code path." False on both halves. The allowlist is now at :202, and two reads inside
the pre-existing `--check` path moved onto a new shared helper: `ratified` from an inline
`tr|grep|head|sed` pipeline at :225 to `read_conf_scalar ratified` at :326, and `canon_unfrozen`
likewise at :347, both calling `read_conf_scalar` added at :182.

Behaviour is byte-identical — the sed program expands to the same three substitutions — so nothing
breaks. But `read_conf_scalar` appears nowhere in the build folder: not the spec, not the acceptance
ledger, not the review. The refactor is recorded only in the commit message while the CLOSED spec's
scope claim stands unamended, and that claim is what a future revert or bisect would be bounded by.

**Fix.** Amend §5 to name the allowlist edit plus the two `--check` reads collapsing onto
`read_conf_scalar`, and drop the line number in favour of the `case "$MODE" in` expression.

**Left-shift.** Folds into F7's check: a build folder that never names a function the diff added is
the same staleness class as a citation whose line moved.

---

## Review shape and run integrity

Raw 16 · confirmed 13 · refuted 3 · unverified 0 · precision 0.81.

The thirteen confirmed collapse to ten distinct defects (F2 = ids 4/6/12, F8 = ids 5/15). Severities
in the table above are this report's adjudication, not the lens ledger's: id 4 was raised medium and
is folded into F2 at high, and no other severity moved.

**Run integrity — all clean, nothing degraded.**

- Lenses: 4/4 returned, 0 DIED.
- Skeptic batches: 4/4 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified.
- 0 spurious verdicts discarded.
- 0 duplicates removed by the harness. (The F2 and F8 overlaps are three and two independent lens
  reports of one site; they are merged here in adjudication, not discarded upstream.)

Because every lens and every skeptic batch returned, the negative result at the top of this record —
no path by which an off-canon token reaches the proposal list — is supported by the run rather than
being an artifact of coverage that never happened. That statement would not be available had a lens
died.

## What blocks, what does not

F1 blocks and only F1: `govkit selfcheck` is an unguarded `declarations` leg, it is RED at
3f6715e8, and the push boundary runs it. Four marker edits clear it.

F2 is the one worth building before the next adopter installs the kit, because it is the only defect
that ships a false liveness claim into a tree nobody here will run. F3 and F5 are correctness defects
whose blast radius is bounded by loud failure — a proposal that reds `--check`, a tail that overstates
work — and both are one-line fixes with one fixture arm each. F4, F6 and F9 are the guard-and-arm
trio: a guard with a hole, an arm that grades nothing, and a guard with no arm. F7, F8 and F10 are
records.

Nothing found touches the closure. The unit's thesis survived the review.
