**Serves:** diff-review TOOL-aSurfacedLexicon-10

# Closing diff review, round 3 — the fixes, and the half of the blocker that did not land

Tier-2 closing diff review of THE FOLD'S OWN DIFF, round 3 · 2026-09-06 · node `a` · build
`aSurfacedLexicon` · streams tooling. Round 1 is the spec audit
(`2026-09-06-review-TOOL-aSurfacedLexicon-10-spec-audit.md`, CLEAN WITH FIXES); round 2 is the
closing diff review (`2026-09-06-review-TOOL-aSurfacedLexicon-10-diff-review-round2.md`, BLOCKED,
ten defects). This round grades **the commit that fixed those ten**, not the ten.

Reviewed range: **3f6715e8...86ea916f** — fifteen files, +677/-45, one commit.

## Verdict: BLOCKED

One blocker, one high, four mediums, two lows. The blocker is round 2's own F2 surviving its fix:
the new refusal gates on the wrong population, so the reassuring zero it was written to close is
still reachable and still exits 0. Round 2 wrote the correct prescription in words and half of it
was implemented. Nothing else here is a behaviour defect that a merge would ship wrong: the
remaining seven are a can't-fail arm, two false diagnostics printed by the new refusal, one count
that disagrees with its sibling surface, and three record or comment claims the code does not
support.

## Review shape

Raw 19 · confirmed 13 · refuted 6 · unverified 0 · precision 0.68. Four lenses (correctness,
gate-integrity, record-fidelity, integration-seams), five skeptic batches.

**Run integrity — all zero, so this run is complete.** Lenses 4/4 returned, 0 DIED. Skeptic batches
5/5 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded,
0 duplicates. No lens died, so a zero finding in an area a lens covered is evidence of absence rather
than a gap in the sweep.

The thirteen confirmed findings describe **eight distinct defects**: three skeptics independently
confirmed the F6 skip (H1), three the NOTHING MEASURED message (M1, one of them also carrying the
B1 sibling arm), and two the `armed extension(s)` line (M2). Merged below with the raw ids named,
because the raw count is the pipeline's and the defect count is the one a fixer works from.

| # | Sev | Site | Defect | Raw |
|---|-----|------|--------|-----|
| B1 | BLOCKER | `tools/lexicon/lexicon.py:2454` | The F2 fix gates on `graded_defs`, not on `live` — the reassuring zero still fires, still exits 0 | 5, 14b |
| H1 | HIGH | `tools/lexicon/selftest.py:3744` | The F6 skip is `check(<label>, True)`: invisible, unconditional, and unfailable — and the two real F6 arms above it cannot fail on any registered node | 3, 7, 10 |
| M1 | MEDIUM | `tools/lexicon/lexicon.py:2453` | The refusal's predicate reads VERBS; its message speaks for the whole extraction, so `--check` contradicts it on the same tree | 2, 9, 14a |
| M2 | MEDIUM | `tools/lexicon/lexicon.py:2460` | `armed extension(s)` prints every DECLARED extension, `dark` ones included — false in exactly the state the refusal exists for | 6, 11 |
| M3 | MEDIUM | `…/spec/2026-09-04-spec-aSurfacedLexicon-10.md:192` | Rollout enumerates three changes to existing paths and misses `OPTIONAL_SIBLINGS`, the only one that is not behaviour-preserving | 15 |
| M4 | MEDIUM | `…/spec/2026-09-04-spec-aSurfacedLexicon-10.md:167` | Rev-5 claims every line citation was struck; four live `146` citations remain, one an imperative | 16 |
| L1 | LOW | `tools/lexicon/lexicon.py:2489` | The tail's per-token counts now disagree with the site census `--list` prints for the same token | 12 |
| L2 | LOW | `tools/lexicon/adopt-lexicon.sh:293` | The NO SHA comment credits the wrong guard for its own unreachability, and prints that reason to the operator | 13 |

---

## B1 — BLOCKER · `tools/lexicon/lexicon.py:2454`

**The new refusal gates on the wrong population, so the branch it was written to close is still
reachable and still exits 0.**

`graded_defs = sum(n for key, n in measured["graded"].items() if key[1] == "verb")` counts
definitions EXTRACTED. `live` is built in `derive_candidates` at `tools/lexicon/scaffold_lexicon.py:143`
from leading tokens present in the form index. Those are different populations: a walk can extract
many definitions and put nothing in `live`, because no leading token is in any cluster. The guard
cannot see that state, so control reaches the `else` at `:2481` and prints

> `EXPAND — nothing to propose. All 0 cluster(s) with a live site in this corpus already carry a row
> … That is the NORMAL result on an adopted repo and not a run that failed to measure.`

with exit 0. A vacuously-true universal over an empty set, closing with an explicit denial of the
failure mode that is actually occurring. Reproduced in a throwaway fixture (`py:python-ast:parser`,
corpus `def frobnicate_v` + `def demand_u`): `graded_defs` is 2, the refusal is skipped, the sentence
above is what prints.

The exit code is the harm. `tools/lexicon/adopt-lexicon.sh:249` is
`"$PY" "$KIT_DIR/lexicon.py" --expand || exit 1`, so a 0 lets `--stamp` proceed and spend the **one
supported widening** on a corpus in which no cluster is live — a stamp that the ALREADY EXPANDED
refusal at `:240` then makes permanent. Round 2's own F2 prescription said, verbatim, *keep the
NORMAL wording only for live non-empty with candidates empty*
(`…-diff-review-round2.md:122`). That half was not implemented.

The suite cannot see it: AC6 (`selftest.py:3788`) asserts `All [1-9][0-9]* cluster\(s\)` against
THIS repo, which can never reach zero, and no fixture arm covers an adopter corpus with a non-empty
walk and an empty `live`.

**Fix.** Split three ways rather than two. `not graded_defs` keeps the NOTHING MEASURED refusal.
`graded_defs and not live` gets its own refusal returning 2, naming its own cause — the walk read N
definitions and none led with a token any cluster holds, so the empty proposal is still the symptom.
Only `live` non-empty with `candidates` empty keeps the NORMAL wording.

**Left-shift gate.** A fixture arm over exactly that corpus (definitions extracted, every leading
token off-canon) asserting the exit is non-zero AND that `NORMAL result` is absent from the output.
It fails today, which is the point — stage it, observe the red, then fix.

---

## H1 — HIGH · `tools/lexicon/selftest.py:3744`

**The F6 skip announcement is `check(<label>, True)`, which prints nothing, cannot fail, is emitted
unconditionally, and raises the arm count by one.**

`check()` at `selftest.py:221` increments `PASSES` on a true condition and appends the label to
`FAILURES` otherwise. `PASSES` is read only by the two closing prints, and neither emits labels. So
a passing arm's label reaches no output on a green run OR a red one. This arm's condition is the
literal `True`. It is a comment wearing a check's clothes.

Three things follow, and each breaks a rule this repo states by hand:

- **The skip does not announce itself.** The build record claims the unexercisable half is
  "announced as a skip rather than left in a comment"; the mechanism does not support that. The file
  already has the working idiom twenty-three hundred lines up at `selftest.py:2021` — a bare
  `print("lexicon selftest SKIP — AC5's conf-comment arms … Four arms unexercised.")`, which does
  reach the reader and did appear in this run's output.
- **It is unconditional.** The three sibling `check(…, True)` skips at `:2535`, `:2551` and `:3419`
  all sit inside branches that fire only when the skip genuinely applies. This one sits directly in
  the `with build_tempdir()` block opened at `:3660` with no platform test anywhere, so on a
  GNU-coreutils node — where its own comment says the arm above DOES bind — it still asserts the arm
  went unexercised.
- **The two real F6 arms it accompanies have never been observed failing, anywhere the leg runs.**
  I verified the platform premise: on this node `grep -E '^expanded=' <crlf file> | sed …` yields an
  empty value with and without the `tr -d '\r'`. All four rows of the node registry are Windows. So
  the `tr` — the whole mechanism F6 exists to grade — is unexercised on every node that runs the
  suite, while three green arms report otherwise. A new gate is not landed until its failing case has
  been observed.

**Fix.** Probe the property instead of asserting it: write a CRLF file, run `grep -E '^expanded='`
over it through `subprocess`, and branch on whether the CR survives. If it does not, `print()` a real
`lexicon selftest SKIP — F6's CR-residue half: MSYS grep drops the CR before sed, so one arm went
UNEXERCISED`. If it does, assert the CR-hardened read so the arm actually binds. The same treatment
is owed to the pre-existing `check("AC8: SKIPPED …", True)` at `:2535`/`:2551` and
`check("AGREE: SKIPPED …", True)` at `:3419`.

**Left-shift gate.** A meta-arm over the suite's own source: `check(` whose second argument is the
literal `True` is a skip claim, and a skip claim must be a `print`, not a `check`. One regex over
`selftest.py`, run as an arm of the suite itself, reds on the class rather than on these four
instances.

---

## M1 — MEDIUM · `tools/lexicon/lexicon.py:2453`

**The refusal's predicate reads the VERB population alone; its message asserts three things about
the whole extraction, all false on a corpus that extracted only type definitions.**

`graded` is keyed `(ext, "verb")` / `(ext, "suffix")` at `:1476-1477`, and the guard sums only the
verb half. Reproduced in a scratch repo (kit installed outside the tree, `py:python-ast:parser`, two
files holding only `class Alpha: x = 1` / `class Beta: y = 2`): `--expand` exits 2 printing *No armed
extractor produced a definition over this corpus*, the three named causes (all dark / armed extension
has no files / extractor refused them), `definition(s) extracted: 0 over 3 tracked file(s)`, and
`--check names the cause on this same tree`. On that identical tree `--check` exits 0 with
`P2 suffix graded=2`, `coverage — armed 2 of 2 definition-carrying file(s) (100.0%)` and `lexicon OK`.

The extension was armed, it had files, and the extractor refused nothing — it extracted two type
definitions. The refusal itself is correct (a verb table cannot be widened from zero function
definitions); the diagnosis printed with it is wrong, and its own pointer sends the operator to a
green page that disproves it. Reachable outside a contrived corpus: a probe pattern set whose
`functions` regex misses the local style while `types` matches lands in exactly this state.

**Fix.** Keep the verb-only predicate and make the words match it — "no FUNCTION definition" — and
derive the evidence line from both halves rather than typing a zero: print
`graded: verb=0 · suffix=<sum over key[1]=="suffix">` over `len(measured['files'])`. Drop or condition
the `--check` pointer; it holds for the all-dark case and not for this one.

**Left-shift gate.** A fixture arm on a class-only corpus asserting the refusal fires AND that the
evidence line reports the non-zero suffix count. No count of a derived population may be typed into
the message; the `0` at `:2461` is one.

---

## M2 — MEDIUM · `tools/lexicon/lexicon.py:2460`

**`armed extension(s)` prints `sorted(declared)`, and `declared` is the whole `{ext: (pset, mode)}`
map from `langs(conf)` — so it lists `dark` extensions under the word "armed".**

Running the kit's own F2 fixture conf (`LANGS="py::dark conf::dark"`) through `--expand` prints
`armed extension(s): conf py` while nothing is armed at all. The sentence directly above it offers
*every language may be declared `dark`* as the first candidate cause, and the evidence line
immediately under appears to rule that cause out. This is the one diagnostic block whose entire
purpose is to stop a misleading zero.

The engine already derives the right set at `:1933`:
`armed_exts = {e for e, (ps, m) in declared.items() if m == "parser" or (m == "probe" and ps in measured["sets"])}`.
This is a wrong expression, not a missing capability. The three F2 arms at `selftest.py:3598-3601`
assert only `NOTHING MEASURED`, `SYMPTOM`, and the absence of `NORMAL result` — none reads this line.

**Fix.** Carry the mode, which the tuple this loop already holds:
`' '.join(f"{e}={m}" for e, (_p, m) in sorted(declared.items()))`. Or filter to `m != "dark"`, keep
the "armed" label, and emit `(none armed)` when the filter empties.

**Left-shift gate.** Extend the F2 arm to assert the evidence line: with all-dark LANGS it must not
list `py` under an "armed" label. That arm fails today.

---

## M3 — MEDIUM · `memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-10.md:192`

**The corrected Rollout section enumerates three further changes to existing paths and closes "Every
one is behaviour-preserving" — missing the fourth, which is the only one that is not.**

`git log -S OPTIONAL_SIBLINGS -- tools/lexicon/lexicon.py` returns exactly one commit, `3f6715e8`,
the unit's own. It adds the constant at `lexicon.py:931` and changes `:966` to
`siblings = {p.stem for p in mods} | set(OPTIONAL_SIBLINGS)` inside `check_self_containment` — an
existing function whose result is read at `:1407` and printed on every `--check`, i.e. the leg that
binds at the merge. It is not behaviour-preserving: before the change the predicate would flag the
engine's `import scaffold_lexicon` in a kit copy installed without the scaffolder; after it, it never
can. That is a permanent widening of a refusal, and the code's own comment at `:926` flags the hazard
it opens. `grep -n 'OPTIONAL_SIBLINGS\|self_contain'` over the spec returns nothing.

Round 2's F10 was "the section claims a completeness it does not have". The corrected section still
claims it, one item short, and the missing item is the one a reader most needed.

**Fix.** Name `OPTIONAL_SIBLINGS` as the fourth change and replace the blanket sentence with the
split: three are behaviour-preserving refactors, the fourth widens the self-containment refusal by a
named allowance, armed at runtime by the two arms `lexicon.py:927-929` cites.

**Left-shift gate.** A record check comparing each spec's Rollout enumeration against the unit
commit's touched-symbol set is over-built for one document. The cheap version: the fold's Definition
of Done grows one line — *every change to an existing path named in Rollout, derived from the diff,
not from memory* — and the acceptance ledger records the derivation command.

---

## M4 — MEDIUM · `memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-10.md:167`

**F7's fix struck the `146` citation in the audit table and the rev-5 log entry, and left four live
ones standing in the body — one of them an imperative.**

The rev-5 entry at `:504-505` now claims *Every line citation in this spec is STALE by construction …
the numbers are STRUCK AND NOT REPLACED, and the expressions are cited instead.* The document does
not support that. `:167-168` reads "the closure is at line 146 … **Cite 146.**"; `:90` cites
`scaffold_lexicon.py:146` as a live design fact; `:205` says "reusing line 146's expression"; `:340`,
`:410` and `:531` all anchor on 146, with `:531` naming it "by path".

`live = {forms[v] for v in counts if v in forms}` is at `scaffold_lexicon.py:143` today. Lines
144-149 are the F3 comment block **this same fold commit added**, so `146` now reads "representatives
crosses two spaces: a table carrying fetch never subtracts load". A reader obeying the spec's own
instruction cites a comment about the fix instead of the mechanism.

Two paragraphs (`:36`, `:266`) handle the identical expression correctly — "cite the EXPRESSION and
not a line". That inconsistency is the finding: two conventions in one document, one of them
blanket-asserting the other does not exist.

**Fix.** Strike the number in all four live places the way the audit table now does, citing the
expression. Where the historical narrative needs the old number, mark it as a frozen quotation of
what the research record said, not as a live instruction.

**Left-shift gate.** A records-hygiene arm: a `<tracked path>:<digits>` citation in a build record
must resolve to a line whose content matches the quoted expression, or be marked frozen. Cheap as a
grep over spec bodies for `\.py:[0-9]+` with an allowlist for frozen quotations; it catches the whole
class rather than these four instances.

---

## L1 — LOW · `tools/lexicon/lexicon.py:2489`

**Moving the tail to `measured["unwaived"]["verb"]` aligned its per-token counts with the offender
scalar and broke them against the site census the engine attaches to every unruled offender at
`:1538`, which is still computed over ALL offenders.**

Two numbers for one question, printed by one tool. Reproduced with three `demand_*` definitions and
`demand_one` waived: `--list` prints "3 definition(s) corpus-wide lead with it" on each surviving
offender, while `--expand`'s tail row for the same token on the same tree reads `demand 2
definition(s)`. The tail's header describes its population as definitions that "lead with a word no
cluster holds and no row names", with no waiver qualifier and no waived count — unlike `--check`,
which prints `waived=N` on its own line. An operator sizing a rename off the tail undercounts by
exactly the waived sites, which are still definitions leading with that token.

Invisible in this repo: the verb waiver registry has zero rows, and the new F5 arm checks presence
and absence, never the count.

**Fix.** Pick one population and say so. Either take each row's count from the `sites` census the
engine already computed (one number, labelled corpus-wide on both surfaces), or keep the unwaived
counts and add the waived total to the tail header the way `check_pass`'s count line does.

**Left-shift gate.** Extend the F5 fixture arm from presence to COUNT: with one of three sites
waived, assert the number the tail prints and the number `--list` prints for that token are the same
number.

---

## L2 — LOW · `tools/lexicon/adopt-lexicon.sh:293`

**The unreachability holds; the reason the comment and the echoed message give for it is false.**

Measured in a scratch repo (`git init` + `git add .lexicon.conf`, no commit):
`git ls-files --error-unmatch -- .lexicon.conf` exits 0, `git rev-parse HEAD` exits 128,
`git diff --cached --quiet` exits 1. So on an unborn branch with a staged declaration the
untracked-declaration refusal at `:281` does **not** fire — an index entry is tracked — and the DIRTY
TREE refusal at `:267` does. The comment at `:288-296` credits `:281`, the one guard that cannot
reach this state, and the same false sentence is printed to the operator at `:301`.

In a repo whose §7 grades "a gate satisfied by its own comment prose", this is the class it polices:
relaxing or moving the deliberately-weaker dirty predicate — its own header calls it the weaker of
the two definitions this repo carries — makes the branch reachable while the prose swears it cannot
be.

**Fix.** Attribute it correctly in both places. A staged-but-uncommitted index is a dirty tree by the
two-sided diff, so the unborn-branch state is refused at `:267`. Drop "has no tracked declaration
either" from the comment and from the echoed message.

**Left-shift gate.** None worth building for one comment. The generalisable form — a refusal that
documents itself as unreachable must name the guard that subsumes it, and that guard must be tested
— belongs in the build method as a review question, not as a script.

---

## House rules

- **A kit file names nothing outside itself by literal.** Clean. The new `check-kit-versions.sh` hunk
  binds `LXD="tools/lexicon"` once and derives all five paths from it, which is the rule's own shape;
  `install-prefix-carried.txt` moved with it. The engine's new block names no sibling.
- **No count of a derived population in prose.** **Breached, at `lexicon.py:2461`** —
  `definition(s) extracted: 0` is a literal zero standing in for a derived figure, and M1 is what it
  costs. Everything else in the new block derives.
- **A new gate is not landed until its failing case has been observed.** **Breached for all three F6
  arms** (H1): the mechanism they grade is unexercisable on every registered node, and the third
  cannot fail anywhere. The new `check-kit-versions.sh` pairing and the F2/F3/F4/F5 arms are fine —
  each was reproduced red here in the course of this review.
- **A skip must announce itself and say which arm went unexercised.** **Breached** (H1). The intent
  is in the source and reaches no reader.
- **A guard that shares state with the thing it guards is not a guard.** Clean, with one note: B1's
  guard does not share state with what it guards — it reads a DIFFERENT population from the one it is
  meant to protect, which is the adjacent failure and the worse of the two, because the guard looks
  present.

## Did the ten fixes break the twelve landed units?

No breakage found, and the two changes with real blast radius were traced.

- `declared = {forms.get(v, v) for v in declared}` (`scaffold_lexicon.py:150`) is safe on a key in no
  cluster — `.get` falls through to the identity, so an off-canon declared row subtracts nothing, as
  before. `--scaffold`, the other caller, passes an empty `declared`, so its behaviour is byte-identical.
- `measured["unwaived"]["verb"]` is a real key populated at `lexicon.py:1749` and already read by
  three other call sites (`:1785`, `:1906`, `:2029`), so the tail joined an established contract
  rather than inventing one. Its only consequence is L1.
- `OPTIONAL_SIBLINGS` widens `check_self_containment` permanently and is read by `--check`,
  `--scaffold` and `--measure`. It cannot red a green tree; it can only fail to red one. That is M3's
  subject, and the risk the code's own comment at `:926` already names.

## Landing bar

B1 is the blocker: fix the predicate split and land the fixture arm that fails today. H1 should ride
the same commit — it is a one-line swap to an idiom this file already contains, and leaving it
re-ships the class round 2 blocked on. M1 and M2 are two edits inside the same `print` block as B1,
so all four are one visit to `run_expand`. M3, M4 and L2 are record and comment corrections. L1 is
optional and invisible in this repo.
