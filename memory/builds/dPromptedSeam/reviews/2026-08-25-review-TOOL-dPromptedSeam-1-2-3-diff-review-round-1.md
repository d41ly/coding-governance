**Serves:** diff-review TOOL-dPromptedSeam-1 TOOL-dPromptedSeam-2 TOOL-dPromptedSeam-3

## Verdict: BLOCKED

# Diff review round 1 — `ee6554c3821bad569d7de47d5556f62700ea7dd2...HEAD`

Reviewed range: `ee6554c3821bad569d7de47d5556f62700ea7dd2...HEAD`, HEAD at `4e0ed2bc`, node `d`,
2026-08-25. **ROUND 1** — this is the first pass over BUILT code in this build; the two records
beside it are `spec-audit` passes over the specs and are not re-litigated here.

**Review shape:** raw 12 · confirmed 8 · refuted 4 · unverified 0 · precision 0.67.

The eight confirmed findings fold into seven distinct defects — findings 2 and 12 are the same
one-word label defect raised independently by two lenses, which is itself a signal about which ones
are real.

One blocker. It is not a design defect: the diff adds two functions and never regenerated the
codebase-map artifact that claims them, so an unguarded merge-bar leg reds and the push is blocked.
It is a one-command fix.

The rest is documentation and duplication in new code. Every one of them is a false or unfounded
statement printed by, or written beside, the exact code that this build exists to stop printing false
statements with. That concentration is the real signal of the round: the mechanism landed correct and
the prose around it did not keep up.

---

## Findings

### BLOCKER — B1 · `tools/lexicon/lexicon.py:872` — the merge bar reds: `symbols.json` was never regenerated

*(raised as finding 9)*

`read_object_state` and `read_token_is_live` are new functions and neither appears in
`memory/map/generated/symbols.json`.

Reproduced against both ends of the range. `python tools/codebase-map/test_codebase_map.py` exits 0 at
BASE `ee6554c3`; at HEAD `4e0ed2bc` it exits 1 with `FAIL test_generated_artifacts_are_fresh` and
`STALE symbols.json`. `grep -c` over the artifact returns 0 for both names. Running
`python tools/codebase-map/gen_map.py --write` produces a 10-line, one-file diff consisting of exactly
those two `tools/lexicon/lexicon.py` entries and nothing else, so this diff is the sole cause —
`inventories.json` and `MAP.md` rewrite byte-identically.

The leg is not guarded. In `tools/gate-legs.json` the row `codebase-map coverage + freshness` carries
`subject: repo` and no `guard` key, and `run-gates.sh` holds back only `subject: kit` legs. It runs on
every bar, including the one `.githooks/pre-push` runs. The push blocks.

`AGENTS.md` DoD requires generated artifacts regenerated in the same commit, and §7 names
generated-artifact freshness as a merge-bar leg.

**Fix.** Run `python tools/codebase-map/gen_map.py --write`, commit
`memory/map/generated/symbols.json`, then re-run `python tools/codebase-map/test_codebase_map.py` and
confirm all five checks report `ok` before landing.

**Left-shift.** The gate already exists and already caught this — the gap is that it was not run
before the commit that broke it. The left-shift is the pre-commit fast leg, not a new gate: add the
freshness check to `.githooks/pre-commit` for commits touching a mapped source file, so the cost is
paid at authoring time rather than at the push boundary where a full bar has a 26-minute floor. If
that is too expensive per-commit, the cheaper form is a variant scoped to the staged paths that
regenerates only their symbol entries.

---

### MEDIUM — M1 · `tools/lexicon/lexicon.py:860` — the reason given for leaving `DEAD_TOKENS` ungated is false, and it closed off the fix

*(raised as finding 3)*

The `DEAD_TOKENS` docstring says the set must EQUAL `map_lib._STOPWORDS`, that NOTHING GATES THAT
EQUALITY, and gives the reason: "the same layer ban that forces the copy forbids the import a parity
check would need". The premise is false and the tree disproves it two ways.

`.lexicon.conf:148` declares exactly one LAYERS rule, `tools/lexicon/* -> tools/codebase-map/*`, and
`check_layer_violation` (`tools/lexicon/lexicon.py:437-445`) only fires when the IMPORTING file matches
the left glob. A check living outside `tools/lexicon/` may import both modules freely. That is not
hypothetical: `tools/codebase-map/selftest.py:1091` already `sys.path`-inserts `tools/lexicon` and
imports it for exactly this class of cross-kit drift check, with a loud skip when the sibling is
missing. Separately, a text-level comparison of the two frozenset literals needs no import at all, and
the layer scan reads imports only, so it cannot see one.

The claim is load-bearing rather than cosmetic. Spec-3's Q1
(`memory/builds/dPromptedSeam/spec/2026-08-25-spec-dPromptedSeam-3.md:136-141`) is closed RESOLVED on
it, and `tools/lexicon/selftest.py:1005` repeats it verbatim as the reason a gate cannot exist. The
docstring both leaves the pair ungated and forecloses the repair.

One caveat on the evidence. `tools/lexicon/subtokens.py:6-12` asserts that a gov-internal parity leg
protects that sibling copy. No such leg exists either — `grep` for `subtokens` across `tools/` finds no
comparison against `map_lib`. That claim is textual and unbacked; it supports this finding's point
about the available pattern without itself being an existing mechanism.

**Fix.** Either add the parity arm — in `tools/codebase-map/selftest.py` or as a gov-internal leg,
comparing `lexicon.DEAD_TOKENS` against `map_lib._STOPWORDS` as sets and `lexicon.MIN_LIVE_TOKEN`
against `map_lib`'s `len(t) >= 2` rule — and delete the "NOTHING GATES THAT EQUALITY" sentence. Or, if
the owner still wants no gate, replace the reason with the true one (the shipped kit must not depend on
`codebase-map` being present in an adopter's tree) instead of citing an import ban that does not reach
a third-party checker. Update `tools/lexicon/selftest.py:1005` and spec-3 §8 Q1 to match.

**Left-shift.** The parity arm IS the gate, and it belongs on the bar as a leg. Beyond the instance:
this is the "two answers to one question" class the diff's own comment at `lexicon.py:953` invokes by
name. The gateable form is a check over every constant in `tools/` whose docstring claims it RESTATES a
value owned elsewhere — the marker is the word "restated" plus a named source path — asserting that
some arm somewhere actually reads the named source. A restatement that names its authority and is
never compared to it is the shape.

---

### MEDIUM — M2 · `tools/lexicon/selftest.py:1007` — the arm labelled "as `map_lib` declares" never reads `map_lib`

*(raised as finding 10)*

`check("the restated stopword set is 21 words, as map_lib declares", len(lex.DEAD_TOKENS) == 21, …)`
compares lexicon's own constant against a hand-typed 21. It never touches
`tools/codebase-map/map_lib.py`. The label claims a parity check that does not happen.

Staged break, verified: adding a 22nd word (`per`) to `_STOPWORDS` at
`tools/codebase-map/map_lib.py:583` leaves `python tools/lexicon/selftest.py` green at 173 arms.
Baseline confirmed as `lexicon selftest OK — 173 arm(s)`, and `grep` for `_STOPWORDS` finds only its
definition and its one use, so nothing else in the repo asserts the pair either. The follow-on arm at
:1010 checks five named members, so a typo or substitution in any of the other sixteen words keeps the
count at 21 and passes both arms.

The two kits then classify the same word differently and `--brief` labels a live shared object a
stopword tail, or the reverse — precisely the outcome the `DEAD_TOKENS` comment says must not happen
silently. The justification for that silence is M1's false claim.

**Fix.** Parse `tools/codebase-map/map_lib.py` with `ast` — no import, so no layer-rule surface at all
— pull the `_STOPWORDS` frozenset literal, and assert set EQUALITY against `lex.DEAD_TOKENS`, printing
the symmetric difference on failure. When the file is absent (an adopter who took `lexicon` without
`codebase-map`), emit a named `SKIPPED — map_lib.py not present, parity unmeasured` line rather than
passing silently. Then correct `tools/lexicon/lexicon.py:857`, which currently asserts no gate is
possible.

**Left-shift.** Same gate as M1 — one arm closes both. The generalizable rule, and the one worth adding
to the recurring-class checklist: **an arm whose LABEL names an external authority must read that
authority.** A predicate that touches only local state while its label cites a remote source is
mechanically detectable — flag any `check(` whose description string names a path or module the
predicate expression does not mention. Run it over `tools/**/selftest.py` before wiring; the finder
pass suggests it will hit more than one.

---

### LOW — L1 · `tools/lexicon/lexicon.py:1004` — the withheld-marker label hardcodes STOPWORD, but a token also dies by LENGTH

*(raised as findings 2 and 12, independently, by two lenses)*

`read_token_is_live` (`tools/lexicon/lexicon.py:891-894`) is
`len(tok) >= MIN_LIVE_TOKEN and tok not in DEAD_TOKENS` — two independent rules. `dead` at :1002 is
true when EITHER kills every token. The only label the branch can print names membership:
`(shared STOPWORD tail, not a shared concept)`.

The module insists elsewhere that the separation matters. The `MIN_LIVE_TOKEN` docstring at
`lexicon.py:866-869` calls it "load-bearing", and `tools/lexicon/selftest.py:983-992` gives the two
rules their own arms because `boundedK` dies by length and `k` is in no stopword list. Twenty-four
lines later the user-facing row collapses them into one word.

Reproduced end to end, not merely reasoned about. In a throwaway git repo with a real `.lexicon.conf`,
the kit copied in, and `core/a.py` defining `read_v2`/`build_v2` and `buildK`/`loadK`,
`--brief core/a.py` prints:

```
  k: build x1, load x1  (shared STOPWORD tail, not a shared concept)
  v_2: build x1, read x1  (shared STOPWORD tail, not a shared concept)
```

Neither `k`, `v` nor `2` is in `DEAD_TOKENS`. The verdict is right; the reason named is wrong, and a
reader sent to look up `k` in the stopword set will not find it.

The length arm is live in THIS corpus, not only in adopters'. `boundedK` at
`tools/hooks/agent-cap.js:125` and `.claude/hooks/agent-cap.js:125` both yield object `k`, and
`read_object_state("boundedK")` returns `dead`. It escapes the label today only because both
definitions lead with `bounded`, so `len(seen) == 1` and the branch is not reached. A second spelling
(`capK`, `limitK`) is all it takes. In an adopter corpus using versioned or single-letter-suffixed
names, reachability is ordinary.

`tools/lexicon/LEXICON.md:46-49` ships the same wording to adopters.

Severity is low because the printed VERDICT stays correct and only the stated reason is wrong. It is
still a false explanation in the row whose entire purpose is preventing a false reading, and it is one
word wide.

**Fix.** Branch on which rule fired. `toks = subtokens(obj)`; if `all(t in DEAD_TOKENS for t in toks)`
keep the STOPWORD wording, else if `dead` emit a rule-accurate phrase — `(shared one-character tail,
not a shared concept)` for the length case, or a rule-neutral `(shared tail carries no comparable
token, not a shared concept)`. Match the sentence in `tools/lexicon/LEXICON.md:46-49`.

**Left-shift.** Add a selftest arm over a length-dead SHARED object — two differently-spelled `*K`
definitions, e.g. `build_k`/`load_k` in the existing `_BRIEF` fixture — asserting the emitted label
does NOT contain `STOPWORD`. The current fixture exercises only the membership branch, so this branch
ships with zero coverage. That arm is the gate; it is also the missing half of the fixture, which is
the more useful framing. The class, for the checklist: **a fixture that exercises one arm of a two-rule
predicate certifies coverage it does not have** — the same could-not-fail shape §7 already names, one
level down.

---

### LOW — L2 · `tools/lexicon/lexicon.py:1000` — the measured denominator does not reproduce: 11 of 30, not 11 of 31

*(raised as finding 4)*

Re-derived independently at BASE `ee6554c3`. I replayed the pre-fix `run_brief` logic from
`git show ee6554c3:tools/lexicon/lexicon.py` — target `here` filtered on `read_object(n)` truthiness
(base :916), corpus `live` histogram over every declared non-dark tracked file (base :922-936), one
target per tracked `.py` file. Result: **30** targets emit any multi-spelling row, **11** of them emit
at least one false row.

The numerator and every named data point reproduce exactly — `map_lib.py` two (`of`, `in`),
`govkit.py` two (`at`, `for`), `lexicon.py` one (`of`), 11 files total. So the method matches and only
the denominator disagrees. The all-extension variant (py+js) gives 34/13, and replaying over HEAD gives
30 as well, so no plausible population yields 31.

The derived percentage inherits it:
`memory/builds/dPromptedSeam/spec/2026-08-25-spec-dPromptedSeam-3.md:73-75` states "11 of those 31
(35%)"; the true figure is 11/30 = 37%.

Minor, but this comment block is the only record of the before-state and nothing derives it. A future
reader re-deriving the figure cannot tell whether the population moved or the number was mistyped. This
is exactly the class §7 names — a count written in prose beside the population that owns it.

**Fix.** Re-run the measurement against a named sha and correct both carriers,
`tools/lexicon/lexicon.py:999-1000` and the spec at :73-75. Or drop the denominator and the percentage
and keep only the 11 files, which reproduce.

**Left-shift.** Not gateable as stated — it is a historical measurement of a code path that no longer
exists, so no live re-derivation can check it. The honest left-shift is a convention, and it belongs in
the recurring-class checklist: **a measured figure recorded in prose carries the sha it was measured at
and the one-line command that reproduces it.** With `(measured at ee6554c3, <command>)` beside it, a
future reader re-runs instead of guessing, and the number stops being unfalsifiable. A cheap partial
gate is available if wanted: flag any comment or spec line matching `\d+ of (?:the |those )?\d+` that
carries no sha within two lines.

---

### LOW — L3 · `tools/lexicon/lexicon.py:960` — the comment explaining the change describes a filter that did not do what it says

*(raised as finding 7)*

The comment says the old `if read_object(n)` truthiness filter dropped BOTH single-token definitions
and all-stopword objects, and that the reader was told about neither. Half of that is false.
`read_object("pin_of")` returns `"of"`, which is truthy, so the old filter KEPT all-stopword objects.
It dropped only single-token names — `read_object("main")` returns `""`. Executed against HEAD to
confirm: `read_object_state("pin_of")` is `dead`, not `none`.

The build's own records refute the comment in the same words. `RUN.md` says the dead-token objects are
truthy and reported today; the round-2 spec audit says the dead group is not merely present but the
loudest row; spec-3 S3 claims only that every single-token definition vanishes.

This comment is the only in-code explanation of what the diff changed, and it is wrong in the direction
that misroutes a future reader. Someone reading it concludes dead-object rows were previously
invisible, will not connect the dead-object handling to the separate marker change 40 lines below at
:1002, and may "restore" rows that were never missing or mis-scope a follow-up fix. The same wrong
claim is duplicated at `tools/lexicon/selftest.py:997-999`.

**Fix.** Reword `lexicon.py:958-960` to say the old filter dropped only single-token definitions (state
`none`), and that dead objects were always printed — wrongly labelled, which is what the marker branch
at :1002 fixes. Correct the duplicate at `selftest.py:997-999`.

**Left-shift.** No gate fits this one and saying so is the honest answer: a comment's account of prior
behaviour is not machine-checkable against a code path that has been deleted. It goes on the checklist
as a documented manual check, and it is a narrow one worth running because it recurs: **when a diff's
comment describes what the OLD code did, re-run the old code before believing it.**
`git show <base>:<file>` and one call is the whole check, and it would have caught this in under a
minute. Both of this round's documentation-of-the-past defects — this and L2 — are instances.

---

### LOW — L4 · `tools/lexicon/lexicon.py:1002` — `read_object_state` computes a verdict no production caller reads, and the rule is re-derived inline

*(raised as finding 8)*

`read_object_state` returns three states. Its only production call site collapses them to two.
`states[` appears at exactly two places, `tools/lexicon/lexicon.py:962` (`!= "none"`) and `:963`
(`== "none"`), which is byte-for-byte equivalent to the old `bool(read_object(n))`. The `dead` value
the new helper computes for every definition is dead plumbing in production, exercised only by selftest
arms.

The live/dead rule then has two expressions: `read_object_state`, keyed on the identifier, and the
inline `dead = not any(read_token_is_live(t) for t in subtokens(obj))` at :1002, keyed on the object.
The object-keyed loop at :995 explains the re-derivation but does not force it — a dead-object set
built from `states` was available.

They agree today because both reduce to `subtokens(read_object(name))`. A change to either does not
move the other. Folding `dead` into `none` to suppress those rows, for instance, silently leaves the
marker branch untouched. And the selftest arm asserting the three states are distinct guards a property
no production path reads.

Not a behavioural bug today. It is the same "two modes answering one question differently" class the
comment four lines above at :953 invokes by name, in the diff that invokes it.

**Fix.** Give the object-side verdict one carrier. Add `read_object_is_dead(obj)` — or key `states` by
object — and have both `read_object_state` and the row loop at :1002 call it, so the marker and the
state classification cannot diverge. This also subsumes half of L1's fix, since the branch would then
have one place to derive its reason from.

**Left-shift.** The structural gate is cheap and general: assert that `read_token_is_live` has exactly
one caller outside `read_object_state` — zero, after the fix — so a third inline re-derivation reds. An
`ast` walk over `tools/lexicon/lexicon.py` counting call sites is a few lines and it fails loudly on
the next copy. Beyond the instance, the checklist entry is **a helper whose richest return value is
read only by tests is not yet wired**: a value computed for every element of a production population
and consumed only by a selftest is a fixture, not a feature, and it will drift away from the inline
copy that actually decides.

---

## What was NOT reviewed

- **The spec and record changes for `TOOL-dPromptedSeam-1` and `-2`.** Both units are WONTDO in this
  diff and their spec edits are retirement text, not built code. They are bound by this record because
  their files moved in the range; they were not re-audited. The two `spec-audit` records beside this
  one hold that judgement.
- **The rendered Skill.** `tools/lexicon/LEXICON.md` was read only for the one sentence L1 names.
  Whether the kit's render-and-byte-compare gate is green on this diff was not checked here — run the
  bar.
- **The full merge bar.** Only the leg B1 reds was run, plus `tools/lexicon/selftest.py`
  (`OK — 173 arm(s)`) and `tools/codebase-map/test_codebase_map.py` (exit 1). No other leg was
  exercised, so nothing in this record is evidence about the other legs' state.

## Landing bar

1. Fix B1 — regenerate and commit `symbols.json`. Nothing lands until that leg is green.
2. M1 and M2 travel together: one parity arm plus the two corrected comments and spec-3 Q1.
3. L1 through L4 are one commit's worth of work in one file and its selftest.
4. Re-run `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` before the push — a DoD
   needs the kit self-tests, and `GATE_FULL` alone says nothing about them.
