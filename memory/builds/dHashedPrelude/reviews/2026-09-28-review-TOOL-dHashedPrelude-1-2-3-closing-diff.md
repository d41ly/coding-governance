**Serves:** diff-review TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-2 TOOL-dHashedPrelude-3

# dHashedPrelude — the closing diff review

*Tier-2 adversarial review · 2026-09-28 · node d · ROUND 1 · subject: the build's whole landing diff.*

Reviewed range: `3cf05f29a8803664845ce243e60bdc0d1d3eee71...211d184dfc5397ceb800eb554d8d9e47f51ca6c5`

## Verdict: BLOCKED

The product fix is real and correct: unit 1 moves the baseline above the arms, and the live-log row
can now fail. What blocks the landing is unit 2. Its ordering arm is the regression gate for exactly
that fix, and it does not gate it — a source with the original defect restored verbatim passes the
arm with a byte-identical verdict string. The build's own Definition of Done requires the confirmed
defect to be left-shifted into a gate; the gate that was built does not hold, so the DoD is not met.
Everything else here is records, and none of it is load-bearing on the product.

## Review shape

| | raw | confirmed | refuted | unverified | precision |
|---|---|---|---|---|---|
| findings | 19 | 13 | 6 | 0 | 0.68 |

Adjudicated tally, stated both ways because the table and the returned ids must agree:

| severity | items | raw confirmed findings |
|---|---|---|
| BLOCKER | 1 | 5 |
| HIGH | 0 | 0 |
| MEDIUM | 1 | 4 |
| LOW | 2 | 4 |
| **total** | **4** | **13** |

Five raw findings (1, 6, 12, 13, 16) are four lenses and two skeptic batches arriving at one defect
in one arm from different directions, so they are adjudicated as a single BLOCKER item rather than
five. Four more (4, 9, 14, 18) are one wrong integer in one backlog row, and three (5, 15, 19) are
one dead symbol in one ledger line. Merging them does not lower any of them; each item takes the
highest severity any of its constituent findings carried, and finding 1's `high` is escalated on the
reasoning given under item 1.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.

Every count is zero, so the finding set is complete as far as the configured lenses reach, and this
run is not described as partial. Note the ordinary limit that still applies: four lenses are a
coverage choice, not a proof of absence, and the zeros above say the machinery worked, not that
nothing else exists.

---

# Item 1 — BLOCKER — the ordering arm is a text search, so it greens on seven ways of disabling the guard it exists to protect

*Covers findings 1, 6, 12, 13, 16.* `tools/memory-recall/selftest.py:2729-2733`

**What is wrong.** `test_the_live_log_baseline_is_taken_before_any_arm_runs` certifies, in its own
`@check` label, that "main() appends its row unconditionally". It establishes that with three
clauses over `body = src[mn:]`, which is raw file text from `\ndef main() -> int:` to EOF —
comments, docstrings and all:

```python
assert "_LIVE_LOG_BEFORE" in body, "main() does not read the module-scope baseline"
assert "_checks.append(_build_live_log_row(" in body, "main() does not append the guard's row"
for dead in ("if live is not None", "if _LIVE_LOG is not None"):
    assert dead not in body, ...
```

Two `in` tests and a two-element denylist. None of the three can see structure, so none of them can
see the properties the arm's name claims.

**Reproduction.** I lifted the arm's predicate verbatim and drove it over the shipped file plus
seven mutations. The control passes, as it must. So do all seven realistic ways of disabling the
guard; only outright deletion of the line reds, and it reds on clause one rather than clause two,
because deletion happens to remove main()'s only textual mention of `_LIVE_LOG_BEFORE`.

| mutation of `selftest.py:2856` | arm verdict |
|---|---|
| control, shipped file | `PASS — baseline 17175 < first arm 18403, 73 arm(s), main() at 150706` |
| commented out, the call text quoted in the comment | **PASS**, byte-identical detail |
| `if _LIVE_LOG:` guarding the append | **PASS**, byte-identical detail |
| append wrapped in `try:` / `except Exception: pass` | **PASS**, byte-identical detail |
| `_ll = _LIVE_LOG` then `if _ll:` | **PASS**, byte-identical detail |
| the append duplicated | **PASS**, byte-identical detail |
| `global _LIVE_LOG_BEFORE` + re-derive as main()'s first statements | **PASS**, byte-identical detail |
| the line deleted outright | RED — `main() does not read the module-scope baseline` |

The detail string is identical across every passing row. A reader comparing two runs cannot tell the
shipped file from a mutated one by the arm's own output.

**Why this blocks.** The sixth row is the one that matters. `global _LIVE_LOG_BEFORE` followed by a
re-derive inside `main()` restores precisely the defect this build exists to close: the baseline
taken after every arm has already run at decoration time, so the guard brackets post-arm state
against post-arm state and the row can never fail. That is the original bug, reintroduced, with the
gate written to prevent it reporting `ok`.

The first row is the second-worst. Commenting a line out preserves its text by definition, and
main() already carries a comment block that is prose about these exact names — so the most common
way anyone disables a flaky row is the one form the arm structurally cannot see.

Nothing else catches any of it. `assert len(order) == len(_checks)` at 2838 runs *before* the five
appends, so it is unaffected. `SELFTEST_ARMS = 73` pins decorated arms only. The sibling arm drives
`_build_live_log_row` directly and never inspects main()'s call site. The summary would fall from 78
to 77 with nothing pinning it, and unit 3 deliberately removed the last typed count that might have
noticed. Outside `selftest.py` and this build's records, `_build_live_log_row` has no other
reference.

Two records assert coverage this arm does not provide, which is what makes it a landing blocker
rather than a backlog row. Spec-1 AC6 asserts the row is appended by "a single unconditional
`_checks.append(_build_live_log_row(...))`" and says "Unit 2's ordering arm is what keeps this true
afterwards"; the arm checks neither singleness nor conditionality beyond two spellings. Round-2
finding D prescribed a two-part fix — no conditional guarding the append, **and** the call at the
same indentation as the sibling appends — and only the first half landed, as an instance ban rather
than a class check. The indentation clause is absent from the shipped arm. That is
`fold-text-is-unreviewed-surface` behaving exactly as the gotcha describes.

The assertion message compounds it by promising an outcome its predicate cannot detect: "emits the
row twice and both copies are green". Neither banned spelling would produce that. There is no local
`live` in main() at HEAD, so `if live is not None` would raise `NameError` rather than duplicate a
row.

This is the repo's own named class, from AGENTS.md §7's porting note — "a gate satisfied by its own
comment prose" — landing inside the one arm the build exists to make fallible. §7 also states "Gate
the CLASS, not the instance" and "A new gate is not landed until its failing case has been
observed." The ledger's AC2 does record an observed red, but the synthetic that produced it dropped
the constant's name entirely; one comment line flips that same probe green.

**Fix.** Assert over code, not text. Replace the three clauses with an `ast` walk over the same
`src` — `ast` is stdlib and one new import. Find the module-level `main` FunctionDef; scan its
**direct** body statements (not `ast.walk`, so anything nested under `if`/`try`/`for` is invisible
and therefore reds) for an `Expr` whose value is a `Call` to `_checks.append` whose first argument is
a `Call` to `_build_live_log_row`; assert exactly one such statement; assert its `Name` arguments are
`["_LIVE_LOG", "_LIVE_LOG_BEFORE"]`; and assert no `ast.Global` naming `_LIVE_LOG_BEFORE` and no
`Store` context on that name anywhere in the function. That retires the `for dead in (...)` denylist
entirely.

**Left-shift gate — validated, not proposed.** §7 requires a candidate predicate be run over the
real tree before it is wired, so I ran it. The predicate above passes the shipped file and reds all
eight mutations, including one the current arm was never tested against (`before =
_derive_live_log_digest(_LIVE_LOG)` passed as a local shadow):

| mutation | candidate predicate |
|---|---|
| control, shipped file | PASS |
| commented out | RED — `0 unconditional _build_live_log_row append(s) in main(), expected 1` |
| `if _LIVE_LOG:` | RED — same |
| `try:`/`except` | RED — same |
| renamed-local conditional | RED — same |
| duplicated append | RED — `2 unconditional ... expected 1` |
| baseline re-taken via `global` | RED — `main() declares global _LIVE_LOG_BEFORE` |
| deleted | RED — `0 ... expected 1` |
| local shadow passed in | RED — `the row is built from ['_LIVE_LOG', 'before'], not the module-scope pair` |

Re-cite spec-1 AC6 and unit-2 AC8 against the new clauses once they land, and re-run the staged-red
discipline against the comment-out mutation specifically, since that is the one the observed red
never reached.

---

# Item 2 — MEDIUM — the backlog row edited to close the drifted-number class types a number that was already wrong when it was written

*Covers findings 4, 9, 14, 18.* `memory/backlog/TOOL.md:20`

`TOOL-aProbedToolkit-14` now reads: "said the selftest is `18 checks`; it was 38 at the time and 76
by 2026-09-28."

At the tip this row lands with, the figure is 78. Derived, not asserted: `grep -c '^@check('
tools/memory-recall/selftest.py` returns 73, `SELFTEST_ARMS = 73` at line 111, and `main()` makes
exactly five `_checks.append` calls after the arity assert — lines 2840, 2848, 2856, 2867, 2878 —
none inside a conditional. The summary prints `len(_checks)`, so 73 + 5 = 78.

76 is the BASE `3cf05f29` value, 71 arms plus the same five rows. The row was rewritten in
`2e2087a3`, which lands after `e4db4519` raised the arm count, so the number was stale at the
keystroke. The contradiction is internal to this one diff and needs no outside source: the
acceptance ledger states "The suite summary reads 78/78, which is 73 arms plus five appended
run-property rows", spec-2 qualifies it correctly as "76 at BASE and 78 after this unit", and the
commit message of `2e2087a3` itself says "It was 38 when that was written and 76 before this build;
it is 78 now." The row dropped the "before this build" qualifier the commit message kept and pinned
the stale figure to the date the build landed 78.

Medium rather than low on three grounds. The row lives in a backlog shard that stays live long after
this build closes, so unlike the two ledger items below it does not go quiet. It contradicts the
build's own acceptance record, so a later session reconciling the README pointer against this row
gets two answers to one question. And AGENTS.md §7 is unconditional — "NO count of a derived
population is written in prose" — in the same edit that credits this build with answering that
row's memory-recall half.

**Fix.** Drop the figure rather than correct it, which is the remedy the row itself prescribes and
the one unit 3 applied to the README cell: "it was 38 at the time and the run's own summary line has
owned the number since `TOOL-dHashedPrelude-3`." If a figure must stay, bind it to where it was
measured — "76 at BASE `3cf05f29`" — the way the neighbouring parked decision already does.

**Left-shift gate.** A memory-tree hygiene check that reds on a bare integer adjacent to a
`tools/<kit>/` pointer in a backlog row is the general form, but it will false-positive on legitimate
historical figures. The narrower and safer version: extend the existing hygiene walk so a row citing
a kit path may carry a figure only when the same sentence carries a BASE sha or a dated qualifier.
Failing that, this joins §10 as a documented manual check — "a number typed into a records edit is
re-derived against the tree that edit lands with, not the tree it was drafted against."

---

# Item 3 — LOW — the acceptance ledger's AC8 evidence cites a function symbol that exists nowhere in the tree

*Covers findings 5, 15, 19.* `memory/builds/dHashedPrelude/build/2026-09-28-build-TOOL-dHashedPrelude-1-1-acceptance-ledger.md:64`

AC8's evidence attests to the docstrings of two arms, one of which is named
`test_the_live_log_row_is_total_over_its_four_states`. A tree-wide grep for that string returns
exactly one hit: the ledger line itself. The shipped arm is
`test_the_build_live_log_row_is_total_over_its_four_states` at `tools/memory-recall/selftest.py:2739`,
spelled correctly three times in spec-2 and carried that way in
`memory/map/generated/symbols.json`, so the ledger is the copy that is wrong and it disagrees with
the generated map.

The cause is visible in history. `848ac8e3` renamed the helpers to lead with a declared lexicon verb
(`_live_log_row` became `_build_live_log_row`, and the arm with it), and the ledger commit `211d184d`
lands after that rename while still carrying the pre-rename spelling. Stale text, not a typo that
predates the name.

Low severity, but the ledger is specifically the artifact a later session re-verifies the build
from, and AC8's whole subject is two named functions — so half of that criterion cannot be re-run by
the name the record gives it. The sibling symbol in the same sentence resolves, which is what makes
the dead one easy to miss. Nothing catches it: the hygiene dead-path walk in `corpus_ids.py` resolves
cited paths, not function names.

**Fix.** Correct the spelling in place to `test_the_build_live_log_row_is_total_over_its_four_states`.
This is a transcription error in evidence, not a ratified decision, so it is fixed rather than
superseded.

**Left-shift gate.** Extend the hygiene dead-path walk to resolve backticked identifiers that match
a function-name shape (`^(test|_)?[a-z][a-z0-9_]{8,}$`) against `memory/map/generated/symbols.json`,
reporting an unresolvable one as a dead citation exactly as it already does for paths. The map is
generated and already in the merge bar, so the oracle is free. Run it over the tree before wiring —
it will surface existing prose that names symbols outside the map, and the exemption list wants
sizing before the leg turns red.

---

# Item 4 — LOW — the build README's parked decision states two integers that are both pre-unit-2

*Covers finding 10.* `memory/builds/dHashedPrelude/README.md:62`

The parked "summary line counts rows, not arms" decision reads, in the present tense, that the suite
prints `len(_checks)`, "which is 76 against 71 declared arms". At this build's tip both integers are
wrong: 78 rows against 73 declared arms.

The deferral's mechanism still holds — the summary counts `_checks` rows while the declared count
lives only in the pin row's detail, and that is as true at 78 vs 73 as at 76 vs 71 — so only the
evidence is stale. That is why this stays low.

I tried to refute it as ordinary historical narration of a decision parked at BASE. The file itself
defeats that reading: the parked decision two bullets above explicitly names `epoch --base 3cf05f29`
when it means a BASE figure, so this file distinguishes the two cases and this bullet does not. It
also contradicts the rule quoted four headings above it in the same README, "No count of a derived
population is written in prose" — the rule unit 3 exists to enforce on the kit README.

**Fix.** Write "78 rows against 73 declared arms at this build's tip", or state the relationship with
no figures at all: the summary counts `_checks` rows, the declared arm count lives only in the pin
row's detail.

**Left-shift gate.** Same leg as item 2, and the same caveat — the honest version of this check
scopes to records written by the build that is landing, comparing any integer adjacent to a claim
about a suite against the tree at HEAD. Where that cannot be made precise enough to avoid
false-positives, both items 2 and 4 fold into one §10 checklist entry rather than a gate, and the
exemption is documented as §7 requires.

---

## Hunted, nothing confirmed

Stated so a later reader knows which ground was walked and found clean, rather than reading silence
as coverage.

**`_build_live_log_row`'s totality (hunt area 2).** Four states are claimed and four are driven by
the sibling arm. There is a fifth path the arm does not reach: `_derive_live_log_digest` calls
`live.read_bytes()` after an `exists()` check, so a path that exists but is unreadable — a
permission error, a directory at that name, a TOCTOU unlink between the two calls — raises out of
`_build_live_log_row`, and `main()` calls it unguarded at 2856. The result is a traceback instead of
a row. I did not raise this as a finding: the old code had the same exposure in the same place, the
helper's docstring is honest about claiming only the two states it handles, and no lens or skeptic
confirmed it. It is worth a `try/except` returning a FAIL row the next time this file is opened,
which would also make the helper total in fact rather than by enumeration.

**The unconditional append and the arity assert (hunt area 3).** Confirmed sound. `assert len(order)
== len(_checks)` at 2838 runs before all five appends, so making the live-log row unconditional
cannot move declared-versus-ran. The row count moves 76 to 78 across this build, which is what the
records other than the two flagged above state.

**Import-time cost and side effects (hunt area 4).** `_LIVE_LOG = _resolve_live_log()` runs a `git
rev-parse` subprocess at import. `_resolve_live_log` wraps it in `except Exception` returning `None`,
so it cannot crash an importer, and `_derive_live_log_digest` returns the absent-sentinel rather than
raising on a missing repo or file. `git_common_dir` passes no `timeout`, so a hung git could hang an
import where the old code hung a `main()` — but that is a change of when, not of whether, and the
nested-selftest arm merely doubles an existing cost. Nothing writes. No finding.

**The gotcha record (hunt area 5).** `memory/gotchas/anchor-literal-resolves-above-its-target.md` and
its INDEX row describe the anchor-offset class accurately, and the class it names is real. It is
worth noting that the gotcha filed alongside this build documents the anchor-resolution defect while
item 1 shows the *absence*-assertion half of the same arm is the weaker one — the sibling gotcha
`absence-assertion-over-whole-file-text` is the one item 1 actually instantiates.

---

## State

- `BUILD — dHashedPrelude · Tier-2 · 3/3 closing-review · left TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-2 TOOL-dHashedPrelude-3`
- `SPEC — [TOOL-dHashedPrelude-1](../spec/2026-09-28-spec-TOOL-dHashedPrelude-1.md) · review TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-2 TOOL-dHashedPrelude-3 · open TOOL-dHashedPrelude-2`
