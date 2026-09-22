**Serves:** diff-review TOOL-dPromptedSeam-1 TOOL-dPromptedSeam-2 TOOL-dPromptedSeam-3

## Verdict: BLOCKED

# Diff review round 2 — `4e0ed2bcbb8ec9e0a5e1b3e5d7b6c0f1e2a3b4c5...HEAD`

Reviewed range: `4e0ed2bcbb8ec9e0a5e1b3e5d7b6c0f1e2a3b4c5...HEAD`, HEAD at `5e839ddc`, node `d`,
2026-08-25. **ROUND 2** — the first pass over the code that round 1's fold produced. Round 1's own
record sits beside this one and its eight confirmed findings are not re-litigated; what is judged
here is the fold that answered them.

**Range sha correction, recorded rather than silently fixed.** The 40-character base I was handed,
`4e0ed2bcbb8ec9e0a5e1b3e5d7b6c0f1e2a3b4c5`, does not resolve in this repo. Its 8-character prefix
does: the real commit is `4e0ed2bc19822151d18b086bb419312d1f405a9b`, which is round 1's HEAD, and
that is the commit every reproduction below was run against. Two commits are in range —
`c6268374` (the fold) and `5e839ddc` (the round-1 record). Anyone re-running this review should pin
`4e0ed2bc19822151d18b086bb419312d1f405a9b`, not the string in the heading.

**Review shape:** raw 17 · confirmed 16 · refuted 1 · unverified 0 · precision 0.94.

The sixteen confirmed findings fold into **six distinct defects**. The collapse is severe and it is
itself the round's loudest signal: four independent lenses landed on the same `KeyError`, four on the
same undefined name, and four on the same un-swept comment. When four lenses converge on one line
without coordination, that line is not a matter of taste.

**Two blockers, and both are in code the fold added to satisfy round 1.** The first is a crash
regression on `--brief`'s primary use — asking about a file you have not committed yet, which is the
lexicon Skill's entire trigger. The second is a new gate whose only failure path is an undefined
name, so the drift diagnostic it exists to print is unreachable and a stopword drift aborts sixteen
later checks. Round 1 closed on the observation that "the mechanism landed correct and the prose
around it did not keep up". Round 2 inverts it: the prose is now nearly right, and the mechanism the
fold added to enforce it is broken in two places. A fold that repairs a false claim by shipping a
gate that cannot fire has moved the falsehood, not removed it.

The other four are round-1 remnants — one guard that does not name the kit it watches, one comment
swept in two of its three carriers, one half of a two-part rule left ungated, and one user-facing doc
quoting a string that no longer exists.

---

## Findings

### BLOCKER — B1 · `tools/lexicon/lexicon.py:1017` — `--brief` on any untracked file dies with `KeyError`

*(raised independently as findings 1, 6, 11 and 15)*

The L4 fix replaced a pure computation over `obj` with a bare subscript into a dict built from a
different population:

```python
dead = read_object_state(next(iter(sorted(spellings_of[obj])))) == "dead"
```

`spellings_of` is populated **only** inside the `tracked_files(root)` loop — that is `git ls-files`.
`here` is derived from the TARGET file's own definitions, and `run_brief` never requires the target to
be tracked; it checks only `p.is_file()`. Any object present in the target and in no tracked file is a
guaranteed miss.

**Reproduced on this tree.** An untracked two-function file defining `build_zzqqxxwidget` and
`render_zzqqxxwidget` gives:

```
File "tools/lexicon/lexicon.py", line 1017, in run_brief
  dead = read_object_state(next(iter(sorted(spellings_of[obj])))) == "dead"
KeyError: 'zzqqxxwidget'
```

exit 1. At base `4e0ed2bc` the same invocation printed
`zzqqxxwidget: no other definition names this object` and exited 0, so this is a regression the fold
introduced, not a pre-existing gap.

Three aggravators, each verified:

- The line **directly above** already writes `live.get(obj) or {}`, and the print at :1024 has a
  dedicated `no other definition names this object` branch for exactly this state. The crash sits one
  line under a branch written to handle it.
- `dead` is computed unconditionally, *before* the `len(seen) > 1` test that would otherwise have made
  the empty case harmless. The tolerant guard exists and is bypassed.
- Exit 1 is the code this function's own comment twenty lines up reserves for verdicts ("Exit 2,
  keeping 1 reserved for verdicts"). A traceback is now indistinguishable from a verdict, which
  defeats the NAMED refusal this same diff added fifteen lines above for unparseable targets.

A second, narrower route reaches the same line: any corpus file whose `extract()` raises `OSError`
(git `core.quotepath` escaping a non-ASCII path) is skipped by the loop's
`except (SyntaxError, OSError): continue`, so its objects are absent from `spellings_of` too.

This breaks the tool on the case it exists for. The lexicon Skill's trigger is "about to name a new
function" — a file that is not committed yet — in this repo and in every adopter that copy-installs
the kit.

**Fix.** Seed `spellings_of` from the target's own names *before* the corpus loop, which removes the
`KeyError` and makes L4's comment ("every name sharing this object yields it") true rather than
assumed:

```python
for n in names:
    _o = read_object(n)
    if _o:
        spellings_of.setdefault(_o, set()).add(n)
```

Minimal alternative if the seeding is unwanted: `_sp = spellings_of.get(obj)`, then
`dead = read_object_state(min(_sp)) == "dead" if _sp else not any(read_token_is_live(t) for t in subtokens(obj))`.

**Left-shift.** Add a `run_case` arm whose `--brief` target is deliberately left OUT of the fixture's
`git add`. All 173 existing lexicon arms are green through this crash because `run_case`
(`tools/lexicon/selftest.py:100`) stages every fixture file, so the untracked-target population is
structurally unreachable by the current suite — the green-by-absence class §7 names. Beyond the
instance, the checklist entry is **an index built from one population, keyed by another**: any dict
filled from `git ls-files` and read with keys derived from an arbitrary path argument is a `KeyError`
waiting for its first untracked caller.

---

### BLOCKER — B2 · `tools/codebase-map/selftest.py:1129` — the new parity gate's failure path calls an undefined name

*(raised independently as findings 2, 7, 12 and 16)*

The stopword-parity arm the fold added to answer round 1's M1 reds like this:

```python
fail("lexicon.DEAD_TOKENS has drifted from map_lib._STOPWORDS — ... "
     f"only in lexicon: {only_lex or 'none'}; only in map_lib: {only_map or 'none'}")
```

`fail` is defined nowhere. Confirmed statically — there is no `def fail` in the module, no star import
(the file imports `os`, `sys`, `Path`, `map_lib as m`, `reuse_lookup as rl`), the name appears exactly
once in the file, and it is not a builtin. Confirmed at runtime: after importing the module,
`hasattr(selftest, 'fail')` is `False`.

Staging the drift — dropping a word from either set — raises `NameError: name 'fail' is not defined`.
`check()` at `selftest.py:52-59` catches `AssertionError` only, and every other red path in this file
raises `AssertionError` (lines 533, 555, 628, 661, 908). So the `NameError` escapes `check()`, escapes
`main()`, and kills the process.

Two consequences, both worse than the drift the arm watches for:

- The `only in lexicon: … only in map_lib: …` diagnostic, which is the arm's **entire reason to
  exist**, is unreachable code. The gate can red, but it can never say which word moved or which kit
  moved it.
- The arm is registered 8th of 24 in `main()`. Sixteen later arms never execute — coverage
  directions, dossier contract, attribution, render determinism, glob brackets, `symbols.json`
  fail-closed, both extractor fail-closed arms, conf grammar, affordance, seed-affordances, both
  reuse-lookup arms, collisions, `new_clones` — and no `PASS` / `N FAILURE(S)` summary prints. One
  stopword drift blinds sixteen unrelated checks.

The run still exits non-zero, so this is not a false green. But `c6268374`'s commit message and
spec-3's rev-4 log both record that the arm "was watched to red on a removed word" and "reds naming
the drifted words". What a removed word actually produces is an undefined-name traceback naming
neither kit, with sixteen checks silently unrun. That is §7's own rule — **"a new gate is not landed
until its failing case has been observed"** — broken by the commit that adds the gate, on the arm
added to satisfy the previous round.

**Fix.** Replace `fail(` with `raise AssertionError(`, the shape `check()` actually catches and the
convention every other red path in the file uses, keeping the message text verbatim. Then re-stage the
break and confirm the run prints
`FAIL js definition probe ⊇ the lexicon's own set: lexicon.DEAD_TOKENS has drifted … only in map_lib: ['the']`
**and still reaches the summary line**.

**Left-shift.** Two gates, and the second is the general one:

1. An `ast` pass over each kit's `selftest.py` asserting that every `Name` loaded at module scope
   resolves to a module-level binding, an import, or a builtin. That is a handful of lines, it catches
   every future undefined name in a failure path, and it needs no execution.
2. The checklist entry: **a gate's failure path is unexecuted code until it has been executed.** A
   green arm exercises only its success branch; the branch that matters runs zero times in every
   passing run, forever. Staging the break is the only way to see it, and "the process exited
   non-zero" is not evidence that the intended message printed.

---

### HIGH — H1 · `tools/gate-legs.json:500` — the parity arm lives in a leg the diff that breaks it cannot run

*(raised as finding 3)*

The new arm sits in the `codebase-map kit selftest` leg, which carries `subject: kit` and
`guard: ["tools/codebase-map/", "tools/lib/"]`. `tools/lexicon/` is not in that guard. Verified end to
end:

- `tools/run-gates/run-gates.sh:741` marks every `subject: kit` leg `ondemand` when `GATE_SELFTESTS`
  is unset. That test runs BEFORE the guard check and is **not** bypassed by `GATE_FULL` — `changed()`
  at :151 short-circuits on `GATE_FULL`, but the subject test never consults it, and the comment at
  :736 says the omission is deliberate.
- `.githooks/pre-push` only ever `export GATE_FULL=1` (line 224); it merely READS `GATE_SELFTESTS`
  from the caller's environment at line 215 and never sets it. **The authoritative push-boundary bar
  does not run this arm.**
- With `GATE_SELFTESTS=1` but no `GATE_FULL`, the guard's `changed tools/codebase-map/ tools/lib/`
  skips the leg for a lexicon-only diff — which is precisely the diff that introduces the drift, since
  the drift is introduced by editing `DEAD_TOKENS` in `tools/lexicon/lexicon.py`.
- No other leg carries the parity. The `lexicon selftest` leg (`subject: kit`, guard `tools/lexicon/`)
  asserts only the count `21` and five members, which is the arm round 1 already raised as M2.

Coverage is not zero, and that nuance is worth stating plainly: the arm does run under
`GATE_FULL=1 GATE_SELFTESTS=1`, the documented complete bar. But `tools/lexicon/lexicon.py:861` now
asserts flatly that **"THE EQUALITY IS GATED"**, and spec-3's Q1 closes on that basis. That is the same
shape as the false claim this round was written to remove, merely inverted: round 1 found a comment
claiming coverage was impossible; round 2 finds a comment claiming coverage the wiring does not
deliver at the boundary where it matters.

**Fix.** Add `tools/lexicon/` to the `codebase-map kit selftest` guard so a lexicon-side edit triggers
the leg, and move the parity assertion into a `subject: repo` leg — the unguarded
`codebase-map coverage + freshness` leg is the obvious home — so the push-boundary bar executes it. If
it must stay a kit self-test, soften `lexicon.py:861` to name the invocation that runs it
(`GATE_FULL=1 GATE_SELFTESTS=1`) instead of claiming unqualified coverage.

**Left-shift.** A canary leg asserting that **every constant a guard exists to watch is inside that
guard's paths**: for each leg whose selftest imports a module from kit X, assert kit X's directory
appears in that leg's guard list. The general checklist entry is **a guard that does not name the file
whose edit introduces the defect is decoration** — the guard scopes the run, and if it omits the
population that can break the check, the check is unreachable exactly when it is needed.

---

### MEDIUM — M1 · `tools/lexicon/selftest.py:1004` — the "a parity gate cannot exist" falsehood survives in its third carrier

*(raised independently as findings 4, 10, 13 and 17)*

Lines 1004-1006 still read, verbatim:

> THE SET EQUALS map_lib's, and nothing but this arm says so. The layer ban forbids importing
> map_lib, so a parity gate cannot exist; the spec's Q1 records that and this asserts the count and
> two members rather than pretending the equality is watched.

All three clauses are now false:

- "nothing but this arm says so" — `tools/codebase-map/selftest.py:1126` says so.
- "a parity gate cannot exist" — the fold's own commit message calls that false and explains the ban
  is directional and file-scoped; the map selftest already imports both modules.
- "the spec's Q1 records that" — spec-3 went to rev-4 in the same commit and Q1 now reads
  "RE-RESOLVED by the closing review, which found the reason given here was false."

The fold corrected the identical sentence at `lexicon.py:861` and re-resolved spec-3's Q1, but
`git show c6268374 -- tools/lexicon/selftest.py` shows the ONLY change to this file was the unrelated
L1 label fix on line 1040 (`STOPWORD` -> `DEAD tail`). Round 1's fix text named this exact site —
"Update `tools/lexicon/selftest.py:1005` and spec-3 §8 Q1 to match" — so this is an explicitly
instructed edit that did not land, not a duplicate of an already-closed item.

Why it matters beyond tidiness: this is the file a maintainer opens FIRST when asking whether the
restated stopword set is watched. They read "cannot exist", stop, and never find the arm — or find it
later and delete it as redundant. The fold's own argument is that this same sentence is what closed Q1
as RESOLVED and foreclosed the repair; leaving one copy standing re-arms exactly that trap. The kit
now answers one question two ways in two files, which is the `two-answers-to-one-question` class
`gotchas.py --for-diff` selects for this very diff.

**A fourth stale carrier exists and no lens named it:** spec-3 line 184 still reads "Q1 records that
nothing can gate the restatement", contradicting the corrected Q1 forty lines above it at line 138.
Sweep both.

**Aggravator, same site.** The arm two lines below is `len(lex.DEAD_TOKENS) == 21` under the label "as
map_lib declares", and the predicate never touches `map_lib` — round 1's M2, unfixed. Now that a real
parity arm exists, a legitimate synchronized 22nd stopword leaves the parity arm green while this one
reds under a label naming an authority it does not read.

**Fix.** Rewrite 1004-1006 to point at the real gate rather than deny it: the equality is asserted in
`tools/codebase-map/selftest.py`, which may import both because the LAYERS ban is directional and
file-scoped; these two local arms remain as the lexicon-side floor for adopters who took the lexicon
without the map — which is a real reason for them to exist, unlike the current one. Rename the count
arm to what it measures ("the restated stopword set is 21 words"), dropping the "as map_lib declares"
claim. Fix spec-3:184 in the same commit.

**Left-shift.** A grep gate over the tree for the phrase family "cannot exist" / "no gate can" /
"nothing can gate" in comments and specs, requiring each hit to carry a decision id, so a foreclosing
claim is at minimum traceable to a ratified record. The checklist entry is **a claim that something
cannot be checked is the one claim that must be re-verified on every touch** — it is the only class of
comment whose falsehood removes work rather than adding it, so it decays silently and nobody
investigates.

---

### MEDIUM — M2 · `tools/lexicon/lexicon.py:874` — half of a two-rule predicate is gated; the other half is not

*(raised as findings 5 and 9)*

`read_token_is_live` is explicitly two independent rules — `len(tok) >= MIN_LIVE_TOKEN and tok not in
DEAD_TOKENS` — and `MIN_LIVE_TOKEN`'s own comment calls the separation load-bearing (`boundedK` yields
object `k`, which no stopword list holds and which dies on length alone). `map_lib.stems()` spells the
same half as a bare literal at `map_lib.py:627`: `if t not in _STOPWORDS and len(t) >= 2`.

The new arm compares `DEAD_TOKENS` to `_STOPWORDS` and nothing else. A repo-wide grep for the second
rule returns exactly three sites and no comparison between any of them: `lexicon.py:874`,
`lexicon.py:899`, `map_lib.py:627`. Moving either number leaves the arm green while the two kits
classify every 2-character token differently — the identical silent-divergence class the arm was
written for, with one of its two carriers unwatched.

This is a partial fold, not a reviewer's invention: round 1's M1 fix text asks for `DEAD_TOKENS` vs
`_STOPWORDS` as sets **AND** `MIN_LIVE_TOKEN` vs `map_lib`'s `len(t) >= 2`. Only the set half shipped,
and the rev-4 log records M1/M2 as folded.

Impact is genuinely bounded — divergence needs a future edit on either side, and the only consumer is
`--brief`'s advisory dead-tail marker — which is why this is medium and not high.

**Fix.** Lift `map_lib`'s literal into a named module constant (`_MIN_STEM_LEN = 2`) used by
`stems()`, then extend the arm to assert `lx.MIN_LIVE_TOKEN == m._MIN_STEM_LEN` alongside the set
equality, so neither number can move alone. If naming the map-side literal is unwanted, a behavioural
probe works: assert `lx.read_token_is_live` and `m.stems` agree over a fixed set
(`{"k", "of", "index", "a"}`).

**Left-shift.** Extend the same arm rather than adding a leg — one gate that reds on either half. The
checklist entry is **a restatement is gated in whole or not at all**: a parity check covering some of a
copied rule creates the confidence of coverage across all of it, and the ungated half is now *less*
likely to be found by hand than before the check existed.

---

### LOW — L1 · `tools/lexicon/LEXICON.md:49` — the user-facing doc quotes a label that no longer exists

*(raised as finding 14)*

The doc reads "names sharing only a stopword tail — `pin_of`, `cache_of`, `token_of` — are marked a
shared **STOPWORD** tail". The emitted string is now
`(shared DEAD tail — a stopword or a one-character token, not a shared concept)` at
`lexicon.py:1022`, changed by L1 in this fold, and the selftest assertion at `selftest.py:1040` was
updated in the same commit. Grepping `shared STOPWORD tail|shared DEAD tail` across `tools/` and
`.claude/skills/` returns exactly two hits: the old label in the doc and the new one in the code.

Two things are wrong. The literal string a reader would grep for appears in no output. And the stated
reason is the stopword half only — the same under-description L1 corrected in the code, since the
branch also fires for length-dead objects like `boundedK`, whose object `k` is in no stopword list.

Nothing gates it: grep for `LEXICON.md` across `tools/`, `skills/`, `.claude/skills/` and
`tools/gate-legs.json` hits only its own header. The rendered `.claude/skills/lexicon/SKILL.md`
carries neither label and is unaffected. This is §6's "a value stated in prose beside the source that
OWNS it rots" class, at its cheapest.

**Fix.** "Names whose object is entirely dead tokens — a stopword like `of`, or a token shorter than
two characters like the `k` in `boundedK` — are marked a shared DEAD tail rather than a shared
concept."

**Left-shift.** A golden-output arm: run `--brief` on a fixture and byte-compare against a block the
doc itself embeds, so the doc becomes a rendered artifact rather than a hand-kept copy. Cheaper
interim: a gate asserting every all-caps output label quoted in `LEXICON.md` appears verbatim in
`lexicon.py`. The checklist entry: **an ungated doc quoting a program's output is a second source of
truth for that string**, and it is always the copy that rots.

---

## Refuted

One finding of seventeen was refuted by the skeptic pass and is recorded here so it is not re-raised
by a later round. Precision 0.94 is unusually high for a round-2 pass and reflects a small, dense diff
in which most lenses converged on the same handful of lines.

## What was NOT reviewed

- **The merge bar.** No leg was run for this record. The three finding sites were reproduced directly:
  invoking `tools/lexicon/lexicon.py --brief` on an untracked probe, importing
  `tools/codebase-map/selftest.py` and testing `hasattr(module, 'fail')`, and reading
  `tools/gate-legs.json`, `tools/run-gates/run-gates.sh` and `.githooks/pre-push`. Nothing here is
  evidence about any other leg's state, including whether round 1's B1 (`symbols.json`) stayed green.
- **`TOOL-dPromptedSeam-1` and `-2`.** Both remain WONTDO. They are bound by this record because their
  spec files moved in range; their retirement text was not re-audited. The two `spec-audit` records
  hold that judgement.
- **The rendered Skill's byte-compare.** `.claude/skills/lexicon/SKILL.md` was grepped for the two
  labels and carries neither. Whether the kit's render-and-compare gate is green on this diff was not
  checked — run the bar.
- **Round 1's findings as a set.** Whether each was correctly folded was assessed only where a round-2
  finding touches it. M1 and M2 are round-1 remnants; round 1's L4 and L1 produced B1 and L1 here.

## Landing bar

1. **B1 and B2 first, and nothing lands until both are green.** B1 is a crash on the tool's headline
   path; B2 is a gate that has never done the thing it was landed to do. Both fixes are small.
2. **Watch B2's failing case with your own eyes.** Stage a stopword drift, confirm the run prints the
   `only in lexicon` / `only in map_lib` diagnostic naming the moved word, and confirm it then reaches
   the `N FAILURE(S)` summary with the sixteen later arms having run. A non-zero exit is not the check.
3. **B1's selftest arm is part of B1**, not a follow-up. A `--brief` target the fixture deliberately
   does not `git add` — 173 green arms could not see this class and will not see the next one either.
4. **H1, M1 and M2 travel together as one commit**: the guard gains `tools/lexicon/`, the parity moves
   to a `subject: repo` leg or the `lexicon.py:861` comment is qualified, the arm gains the
   `MIN_LIVE_TOKEN` half, and the "cannot exist" sentence is swept from both remaining carriers
   (`tools/lexicon/selftest.py:1004` and spec-3 line 184).
5. **L1 is one sentence** in `tools/lexicon/LEXICON.md`.
6. Re-run `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` before the push.
   `GATE_FULL` alone says nothing about the kit self-tests, and this round's whole subject is a kit
   self-test.
