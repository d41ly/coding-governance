# The lexicon kit — is it salvageable, and what has to change

**Serves:** research TOOL-dScaffoldedMirror-2

Synthesis of four ground reports, four designs and three adversarial refutations, run 2026-08-24 on
`C:/projects/coding-governance/.claude/worktrees/unattended-ascanned-throttle-18a592`. Every figure
below was measured by one of those passes on this worktree or on `C:/projects/incms/main`; nothing
here is estimated. Paths are repo-root-relative.

---

## 1. VERDICT

**Salvageable, and it is already half-working — but not the half anyone was looking at.** Since
`.lexicon.conf` landed on 2026-08-16 this repo has added **136 definitions and zero offenders**;
their leading tokens are exactly the declared table (`test` 25, `build` 19, `derive` 15, `read` 13,
`resolve` 12, `check` 11, …), and a whole new JavaScript hook was written end-to-end in the
vocabulary. In the same window the gate refused nothing: it has fired three times in its life and all
three resolved as a pin raise (412 → 415 → 417 → 463), with **exactly one** offender key ever leaving
the set, and that one by a de-duplication rather than a rename. So the *declaration* is constraining
the random generations at 136-for-136 and the *enforcement* has a measured contribution of zero. The
single root cause of the useless half is that **every standard in this kit is derived from the corpus
it grades, pointing the same direction the corpus points**: `--scaffold` ranks the corpus's own
leading tokens and adopts the top 25 as an *allowlist*, so a repo that consistently does the wrong
thing legalises it (measured: all 5 demo offenders were in the vendored kit, 4 of 25 "verbs" were not
verbs, and every deliberately-bad name passed green); `scaffold_lexicon.py:105-107` then writes the
ceiling from that same corpus, two thirds of it as hardcoded `"0"` literals under a comment claiming
all three are MEASURED; and when the corpus grows the ceiling is raised. There is no exogenous
reference anywhere in the design. Fix that one property in two places — ship the candidate vocabulary
instead of deriving it, and replace the raisable integer with a named set frozen at a past commit —
and the kit becomes what the owner asked for. Do **not** respond to "it shipped worthless" by
building more gate: the gate is the half with the zero.

---

## 2. THE DIAGNOSIS, ranked

### A. Genuine design defects — the standard is derived from the subject

**A1. The scaffold's polarity is inverted, and this is the whole demo failure.** A frequency-ranked
*allowlist* derived from the graded population legalises whatever the corpus does most. Run the same
frequency count into a *blocklist* and the same tokens become the debt list — same derivation,
opposite polarity, opposite outcome. This is the one defect that makes a fresh adoption worthless on
arrival, and it is upstream of the "4 non-verbs" and "17 of 22 offenders hidden" results.

**A2. The pin is a raisable integer with no baseline and one operator.** `lexicon.py:537` is
`if len(unwaived) > pin`. No direction guard, no ratchet, no shrink-only enforcement in code —
"SHRINK-ONLY" appears in all three waiver headers and in `kit.toml:91` and **no code reads it**.
`.lexicon.conf` carries ~70 lines of hand-written archaeology for four raises, every one a raise. The
conf's own comment on the last one: *"32 of the 45 are the govkit deployer … That is NOT what a raise
is meant to absorb"* — the file knows, and nothing acts on it.

**A3. The gate grades conformance to a table, not consistency of the corpus, and 77% of its findings
are unactionable.** Grouping every definition by its object (the subtokens after the leading one):
**354 of 459 offender keys conflict with nothing in this corpus** — they are not inconsistent with
anything, they merely fail a table. Meanwhile **60 definitions sit in a genuine spelling conflict and
P1 calls them green** (`load_conf` ×8 vs `read_conf`, both in the table with different declared
meanings; `region` spelled `build_`/`render_`/`parse_`/`apply_`/`insert_`, all five green). The
instrument the owner asked for is consistency; the shipped instrument correlates with it at 23%.

**A4. The corpus is `git ls-files` with no exclusion, so the kit grades and seeds itself.**
`lexicon.py:125-129`. Ten of this repo's 463 offenders are the kit's own files, and `tracked`, `ext`,
`python`, `probe`, `glob` — the exact non-verbs that bled into the demo's proposed vocabulary — are
their leading tokens. A real adopter vendors a dozen kits into `tools/` and it gets worse. **A derived
proposal computed over a corpus that includes the deriver is untrustworthy on arrival**, which makes
this a prerequisite for every other derivation, not a phase of its own.

**A5. Vacuity is unreported at every level.** `lexicon.py:455` folds `len(funcs) + len(types_)` into
one `populations[ext]`, so `.js` reports a healthy 89 while P2 grades **zero** JavaScript classes and
the DEAD PROBE arm cannot see it. The green line —
`lexicon OK — 896 tracked file(s); coverage: …` — prints **no offender count and no population at
all**, so a reader of the bar cannot distinguish this repo from one with zero findings.
`--measure` prints UNDECLARED EXTENSIONS, DEAD PROBE, UNSELECTIVE LAYERS RULE and STALE WAIVERS as
`# NOTE:` comments and **returns 0 unconditionally**. A whole-repo `.ts` corpus carrying a banned
suffix, a non-verb function and a forbidden import exits 0 with `lexicon OK` — reproduced.

**A6. Darkness is a free, unbudgeted drain.** 82 tracked `.sh` files against 44 `.py` and 10 `.js` —
shell is this repo's largest source population by file count, holds ~518 function definitions, and is
`dark` by one token in one string. Only 54 of the 126 files that actually carry a definition (42.9%)
are covered by an armed mode. No design in the brief budgets this, and declaring coverage
per-(extension, predicate) would multiply the surface sevenfold.

### B. Under-delivery — the mechanism was specified and not built

**B1. `TOOL-dScaffoldedMirror-1`: found three times, fixed zero.** Review 3 M3 (2026-08-16), review 4
L3, and the owner's demo all found `scaffold_lexicon.py:106-107` writing `SUFFIX_OFFENDER_PIN="0"` and
`LAYER_OFFENDER_PIN="0"` as string literals under a MEASURED comment. The remedy verb (`--measure`)
shipped; the write path never moved.

**B2. The negative definitions are prose in a column nothing parses.** `LEXICON.md` and the charter
both demand them; **11 of 22 rows carry a `NOT <verb>` clause and 11 do not** (`resolve extract
measure derive seed run arm add print main test`). No reader parses the gloss. The gate's message is
therefore the contentless *"not in the declared VERBS table"* rather than *"fetch is banned; load is
the verb for this"*.

**B3. The three `.lexicon.conf` pins are absent from `RATCHETS`.** `drift_signals.py:265` holds eight
rows and none is `.lexicon.conf` — confirmed by grep today. The conf already hand-writes
`RAISED 412 -> 415` in exactly the format `ratchet_findings` parses. The convention is being followed
and nothing is reading it. Three lines.

**B4. `tools/govkit/check_runbook_parity.py` is dead code hiding 18 undocumented deployables,
`lexicon` among them.** Zero callers, not in `tools/gate-legs.json`; run today it exits 1 with
*"registry entry 'lexicon' has no anchored runbook section"*. A hand-wiring adopter is never told the
kit exists. This is upstream of demand (3).

**B5. Waivers accept an empty reason and are keyed repo-wide.** `load_waivers` (`lexicon.py:195-208`)
does `s.split(None, 1)` and never validates the second field; `Offender.text` for P1 is the bare
identifier, so waiving `enc` waives it in every file forever. 46 of 395 distinct names span multiple
files, covering 114 of 463 occurrences (24.6%).

### C. Working as designed, and never enough

**C1. The verb table works as a *declaration*.** 136/136 compliance in eight days, and the mechanism
is context delivery, not refusal. It is currently delivered by a session happening to read
`.lexicon.conf` — no machine holds it in front of the author, and nothing measures whether it keeps
working.

**C2. P2 and P3 are honest and inert.** P2 grades 37 python classes and 0 js classes; none of the 37
was ever a plausible offender. P3's single declared rule `tools/lexicon/* -> tools/codebase-map/*` has
**0 live candidate edges** because the 3 real edges between those directories run the other way —
which is what a rule being *obeyed* looks like, not a broken one. Both pins of 0 are true over
populations that could not produce a finding.

**C3. The classic-LLM-token result is a gov-only artifact.** `get fetch create save handle process
manage calculate` are at **0 occurrences each** here — and were already at zero at `7b01979a`
(2026-07-20), a month before the conf existed. On `incms/main` the same tokens are `get`=136,
`list`=121, `validate`=94, `create`=89, `require`=69, `make`=67. The absence of a species was measured
in the one enclosure it was never released into.

**C4. Cost is not a constraint and should stop being discussed as one.** Lexicon's three legs are
13.0 s of a 2,587 s leg-sum (0.503%); the full check is 0.44 s warm; the longest leg on the bar is
297 s. Adding the scoped visitor and the provenance assert takes the check leg to ~0.81 s on gov and
~8-10 s cold on a 6,165-file adopter. Nothing here dies on compute. Things die on blast radius,
landing-day reds, and un-adoption.

### D. The population that decides everything: adopters = 0

`C:/projects/incms/main` is a **full gov adopter** — 6,165 tracked files, `.governance/`,
`.codebase-map.conf`, `.memory-tree.conf`, `.unattended.conf`, `.githooks/` — and carries **no
`.lexicon.conf`**. `C:/projects/swydee` is hand-wired, 133 files, no lexicon, no `.governance/` at
all. The kit's live adoption count is one: the repo that wrote it. Every noise floor and "gateable at
pin 0" claim in the design set was fitted to a 44-file Python corpus. On incms the same predicates
give: P1 **6,482**; the four new coverage predicates **3,133** union; the negative-definitions
predicate **446** (against 2 here — 223x). The brief's own bar is *"a predicate that reds 2000
identifiers on a real adopter is not adopted, it is deleted."*

---

## 3. RECOMMENDATIONS, ranked

Marks: **SHIP** = land now, small, unblocked. **BUILD** = a real unit, spec it. **RESEARCH** = a
measurement or decision comes first. **REJECTED** = §6.

---

### R1 — Honest reporting and per-predicate liveness · **SHIP**

**What.** Split `populations` per *predicate*, not per extension. Every predicate prints
`graded=<n> offenders=<n> waived=<n>` on green as well as red. An armed extension whose predicate
population is 0 prints `DEAD PREDICATE — graded 0` and reds. `--measure` stops returning 0 over
UNDECLARED EXTENSIONS / DEAD PROBE / UNSELECTIVE LAYERS RULE / STALE WAIVERS.

**Why it beats the alternatives.** Nothing was refuted here; this was the only unanimous survivor
across all three skeptics, and it is the cheapest correct thing in the whole brief. It is also a
precondition for honesty about everything else: three designs route through `--measure`, and any new
`[[hole]]` discharged by "run the checker" inherits a checker that measures nothing.

**Mechanism.** `lexicon.py:455` becomes two dicts (`funcs_per_ext`, `types_per_ext`) plus a
per-predicate roll-up; the verdict loop at `:516-548` emits the counts; `measure_mode` returns 1 when
`problems` is non-empty.

**Cost.** Zero compute. ~60 lines.

**Failing case, already in the tree, unstaged.** `.js` has 89 function definitions and **0** class
definitions; P2 grades an empty set behind `populations["js"] = 89` and prints nothing. Today this is
`lexicon OK`.

**Arm.** Run against the current tree: `DEAD PREDICATE — P2 graded 0 of an armed extension (.js)`,
exit 1. Then declare the js `types` category dark, confirm the refusal names it rather than passing.

---

### R2 — Corpus scoping, derived from the receipt, never authored · **SHIP**

**What.** Exclude vendored kit files from the graded corpus. Default rule needs no declaration: a file
carrying a `# gov:kit <id>@<ver>` marker, or living under a directory holding a `kit.toml`. Every run
prints `corpus — graded N of M tracked file(s) · excluded K by <rule>`. An exclusion rule matching
**zero** tracked files REDS (the unselective-rule law, already built for `LAYERS`). The excluded
fraction is capped and exceeding it REDS.

**Why it beats the refuted alternative.** A free-form `CORPUS_GLOBS` key was proposed once and refuted
on the grounds that the whole tracked tree is a stricter contract. That refutation is right about an
*unconstrained* key, and it is answered on its own terms by the three controls above: a shrink is
never invisible, an inert rule reds, and the total is bounded. The counter-evidence is now measured
rather than asserted — an unscoped corpus makes the *derived proposal* wrong, which is a different
defect from making the *gate* loose. Where there is no `.governance/` receipt (swydee), the honest
answer is a named refusal, not a glob list.

**Cost.** ~0.02 s. ~80 lines.

**Failing case.** Stage a `CORPUS_EXCLUDE` rule naming a path that no longer exists → RED. Today no
such key exists and vendored files are graded silently.

**Arm.** Run the scaffold over a fixture repo with a vendored kit; assert the vendored kit's leading
tokens (`tracked`, `ext`, `probe`, `glob`) appear in **neither** the proposal nor the offender count.

---

### R3 — Waiver hardening · **SHIP**

**What.** Re-key all three registries from bare `text` to `path::name`. Require a non-empty reason.
Add the waiver-row count to `drift-audit`'s `PINS` as a `gateable: False` watermark and to `RATCHETS`.

**Why now, before anything else that concentrates pressure.** Under R8 the waiver becomes the *only*
remaining dodge, and all the pressure that used to leak through the pin lands on a file whose rows are
currently unreasoned and repo-wide. This is not re-introducing the refuted `<path>:<line>` keying
(`TOOL-aLoosenedCeiling-5`) — that failed because an edit *above* a waived line unpinned it.
`path::name` carries no line number and survives every edit to the file. Say so in the record; a
reviewer will otherwise flag it as overturning a settled decision.

**Cost.** ~0.01 s. ~40 lines plus a one-time key migration (all three registries are comment-only
headers today, so the migration is empty).

**Failing case.** A waiver row with no reason must RED. Today `s.split(None, 1)` accepts it silently.

---

### R4 — Ratchet the three pins, and close the delete-then-re-add hole · **SHIP, and it dies at R8**

**What.** Three rows into `RATCHETS` at `drift_signals.py:265`:
`{"file": ".lexicon.conf", "key": "VERB_OFFENDER_PIN", "weakens": "up"}` and the two siblings. Then
fix `ratchet_findings` (`drift_report.py:198-221`), whose guard is
`if now is None or was is None or now == was: continue` — **a key that vanishes passes silently and a
key that reappears passes silently**, so delete-in-commit-1 / re-add-at-900-in-commit-2 is a
two-commit, zero-finding bypass.

**Why.** Highest value-per-line in the brief: the conf already writes the marker by hand in exactly
the format the reader parses. **Label it a documentation ratchet and do not report it as answering
demand (2)** — the 417 → 463 move came with three paragraphs of prose and would have sailed through.
It converts a free move into a five-minute move; against an LLM author five minutes of prose is a
subroutine, not a deterrent.

**Interaction.** If R8 lands, these three rows go permanently inert and nothing says so — a ratchet row
naming a dead key is the stale-exemption class one level up. R8 deletes them in the same commit, and
adds an assert that every `RATCHETS` row names a key present in its file.

**Failing case.** Raise a pin with no `<old> -> <new>` marker within 14 lines → RED. Delete and re-add
across two commits → RED (today: silent, both arms).

---

### R5 — Coverage floor and a `LANGS` mode ratchet · **SHIP**

**What.** Print, every run, the graded fraction of tracked files that carry at least one definition
(gov today: **54 of 126, 42.9%**, with 72 dark `.sh` holding ~518 definitions). Declare a floor and red
below it. Add `LANGS` to a mode ratchet where `parser > probe > dark` per extension, so flipping `py`
to `dark` is a weakening move that needs an in-place justification.

**Why.** This is the largest unclosed hole the refutations found and no design owned it. Every
fail-closed story in the brief covers the *undeclared* (extension, predicate) pair; **none covers the
declared-dark one**, and declared-dark is the cheap move — one string edit empties the graded
population and reds nothing. Without this, R8's asserts, the ledger and every new predicate are
defeated by an edit nobody reviews.

**Cost.** Zero compute. `RATCHETS` is scalars-only today, so the per-extension mode ratchet is a new
shape (~120 lines) — the coverage-fraction print is ~15 lines and can ship first.

**Failing case.** Flip `py` from `parser` to `dark` → RED with the graded fraction collapsing from
42.9% to 7.9%. Today: `lexicon OK`, exit 0.

---

### R6 — The marginal-offense-rate signal · **SHIP**

**What.** A new `drift-audit` signal: offenders added per definition added between a recorded base and
HEAD, derived at both shas by the kit's own extractor. Both operands derived, nothing authored,
nothing raisable. `gateable: False` initially — it is a trend and one bad landing should not red the
bar — with an explicit `live` assertion so a broken derivation prints DEAD PROBE.

**Why this is not optional.** It is the **only** instrument anywhere in this brief that measures the
owner's actual demand: *are new generations constrained?* The 136/136 result that reframes everything
is a one-off measurement by one agent on one afternoon over eight days of one repo, with a named
confound (sessions that had just built the kit). Making it standing converts an anecdote into a
falsifiable claim, and it is the evidence that answers the owner-ratified retirement condition F4
(*retire P1 if it goes unused across two adopters*) with data instead of argument.

**Cost.** ~0.4 s per invocation (derive-at-sha measured at 0.369 s on gov, 3.218 s on incms),
sha-cacheable because a commit's tree is immutable. Not on the merge bar.

**Failing case.** Set the base to a sha not in the object store → DEAD PROBE, never a reassuring 0.

---

### R7 — The shipped frozen canon, and `--probe` · **BUILD**

**What.** A kit-owned frozen `tools/lexicon/canon.py`: ~19 concept clusters, each a set of English
surface forms with a **default representative that is always the first element**. `role = "engine"`, so
an upgrade overwrites it and an adopter cannot edit it. `--probe` is a read-only report: per cluster,
which forms are live, how many sites each has, what convergence would cost. It writes nothing and
exits 0. `--probe --write` writes the curated table and the debt ledger.

**The one correction the skeptics forced, and it is the whole design.** D3 proposed a dominance table:
D ≥ 0.80 → adopt *the corpus's leader*. That is the demo defect one indirection down — a repo whose
sessions all wrote `get_*` has D ≈ 1.0 and `get` is adopted silently, and D3's own falsifiable day-1
claim (`get`=1, `fetch`=1, `load`=0 → propose `load`) is **false** under its own table, because `load`
has zero sites and cannot be the leader. **Corrected rule: the canon's first element is the proposal
unconditionally, at every dominance. The corpus is admitted as evidence for exactly one thing — which
spellings become debt rows.** Corpus votes to *exclude*, never to *select*. That deletes three of the
four verdict rows, which is the honest shape, because the surviving rows were the mirror.

**Why it beats the alternatives.** No token outside `CANON` can enter `VERBS` at any frequency, at any
threshold. `t`, `do`, `git`, `kit`, `signal`, `bounded`, `repo`, `tracked`, `ext`, `python`, `probe`,
`glob` are in no cluster and are therefore **unnominatable**. This one property kills the measured demo
defect by construction. And adopting a form *creates debt for its synonyms* — a row is written together
with its negative definitions, and every corpus site using a losing form becomes a ledger row in the
same write. That is net-negative on legality, the exact inverse of a mirror.

**Cost.** ~19 dict rows plus a report renderer. One full corpus pass: 0.44 s gov, ~4.7 s incms. Run on
demand, never on the bar.

**Failing case.** Feed `--probe --write` a corpus of 500 `frobnicate_*` definitions and assert
`frobnicate` does **not** enter `VERBS`. Freeze the demo as a regression fixture.

**Second arm, which is the one that catches the polarity regression.** A corpus with `get`=1,
`fetch`=1, `load`=0 must propose **`load`**. Under the refuted dominance table it proposes `get` or
`fetch`.

**Related, and free: promote the negative definitions from prose to structured data.** A `VERBS` row
becomes `<verb> <gloss> — NOT <other>[, NOT <other>]`; the conf reader parses the list; the checker
asserts every row carries ≥1 negative and that no declared negative is itself in the table. Backfilling
the 11 missing negatives is a curation pass a machine cannot do. Its own failing case exists today: 11
of 22 rows carry none. This turns the gate's message into the fix — *"fetch is banned; load is the verb
for this"* — which is free convergence pressure and does not add a predicate.

---

### R8 — The grandfather set with a provenance assert, replacing all three pins · **BUILD**

**What.** `.lexicon.conf: FREEZE_SHA="<40 hex>"` pinned once at adoption, plus a shrink-only named set
keyed `path::name`, plus five asserts:

| | assert | what it forces |
|---|---|---|
| A | every current offender ∈ grandfathered ∪ waived | a new offender REDS; no absorbing move exists |
| B | every grandfathered key is still an offender | draining forces deleting the line, same commit |
| **C** | **every grandfathered key is derivable as an offender at `FREEZE_SHA`** | **the file cannot be topped up** |
| D | grandfathered ∩ waived = ∅ | no double cover hiding a drain |
| E | `FREEZE_SHA` resolves, its tree reads, both populations > 0 | a shallow clone prints DEAD PROBE, never green |

**Why it beats every refuted alternative.** A bare shrink-only file is a pin with 459 digits — that is
`codebase-map`'s own recorded verdict on itself (`memory/map/baseline.toml`: *"Nothing enforces the
rule today — that is why the option was available at all"*). Per-directory pins are N raise paths
instead of one, and a new directory mints its own. A justification-comment ratchet is satisfied by
prose. Diff-scoped enforcement is base-dependent and this repo has three incompatible bases at the push
boundary (`BASE` computed at `run-gates.sh:128-139` and never exported; `GATE_BASE=$rec_sha` up to 10
commits stale; `GOV_DEFAULT_BRANCH` with a recorded fail-open). **Assert C is the only mechanism in the
entire brief that makes an absorbing edit *impossible* rather than expensive**, because no edit to the
present tree can change what a past commit contains. It is also reviewer R4's own proposed repair to
the pin-direction guard — *"guard on the offender IDENTITIES, not the count"* — which was cut at rev-3
on defects in a *different* spelling while R4's sound one sat unbuilt in the same record. Restoring it
is building a design a reviewer already validated.

**Five rulings the skeptics left open, decided here:**

1. **Which conf does the freeze-time derivation read? Today's.** So admitting a verb retroactively
   un-offends historical keys, assert B reds every one, and they must be deleted in that commit. That
   is the pressure; reading the conf at the freeze sha would let grandfathered rows outlive their
   justification forever.
2. **Freeze advancement: forbidden in v1.** The set only shrinks. This deletes the subset rule, which
   was the one place D2's design smuggled a base back in after spending a section refuting bases.
3. **Remote reachability: dropped, and say why.** The unattended protocol requires a remote-observed
   BASE because a run merges and pushes with no owner turn. A naming leg that reds on every offline
   run and in every shallow CI clone is worse than the attack it prevents, and the attack — a run
   minting the commit that grandfathers its own offender — is a one-line diff on a tracked file. Do
   not borrow the protocol's language for a control that will not carry it.
4. **Location: the kit directory with `role = "seed"`, not `memory/lexicon/`.** Measured staged break:
   `memory/lexicon/` reds `HYGIENE check 3 FAILED — unexpected entries (structure)`, exit 1, and the
   remediation is a `.memory-tree.conf` edit — an optional kit forcing a declaration change in a
   required one, which is the coupling direction lexicon's own `LAYERS` rule exists to forbid.
5. **Multiplicity: rename the three, do not carry them.** `bench.py::enc`, `selftest.py::scratch_gov`,
   `gen_build_index.py::_rec` are one key covering two or three occurrences each. Renaming three keeps
   the design free of integers entirely.

**Cost.** 0.44 s → ~0.81 s cold on gov, ~8-10 s cold on incms, sha-cacheable to ~0.45 s warm. ~600
lines including selftest arms. Backfill: 459 rows here, **6,299 on incms**.

**Prerequisite that will otherwise bite on day one.** A staged 8-method `ast.NodeVisitor` in
`tools/lexicon/` **reds this gate today** (471 over pin 463), and **26 of 26** proposed identifiers are
off-table including all 17 `visit_*` names, which CPython's dispatch mandates and which cannot be
renamed. Under R8 those cannot be grandfathered (post-freeze) and cannot be renamed, so the design's
first act would be 16-18 waivers in the design whose thesis is that the waiver is the last escape hatch.
**A kit-owned structural exemption class (`^visit_[A-Z]`, `generic_visit`) lands first.**

**Failing case, one per assert, each staged and confirmed RED then unstaged.** A: add
`def frobnicate_thing()`. B: rename a grandfathered function without deleting its row. **C: hand-add a
row for a function added after the freeze → RED, "not an offender at FREEZE_SHA".** D: waive a
grandfathered key. E: point `FREEZE_SHA` at an absent sha → DEAD PROBE. C's failing case has never been
observable before, because there has never been an assertion a pin edit could violate.

---

### R9 — Supply the vocabulary to the author: `--brief`, `--suggest`, the rendered skill, a net-negative charter pointer · **BUILD**

**What.** Three surfaces and one deletion.

- **`--suggest <name>`** — one deterministic line, no parse, **0.042-0.047 s** measured: `OK`, or
  `use load_record — the declaration says "load", NOT "fetch"/"get"/"retrieve"`.
- **`--brief <path>`, reframed.** D4's prototype prints the declared table plus a frequency histogram
  of the directory's off-table leading tokens; that is 378 bytes and 0.18 s on gov and **dies at
  adopter scale** — `services/api/tests` in incms has **750 distinct off-table leading tokens** and a
  7,996-byte full list, so the top-9 line D4 prices at 92 bytes shows **1.2%** of the live vocabulary.
  The truncation that bounds the cost voids the signal. **Replace the histogram with per-OBJECT
  conflict**: for the objects this file already names, which leading tokens are live. That is bounded
  by construction (keyed on what the author is about to name, not on the directory), and it surfaces
  the only drift class actually measured here — `do_` in memory-tree vs `cmd_` in govkit; `t_` and
  `test_` twenty-nine and five times **in one file**, while `test` is in the table and `t` is not.
- **A rendered `skills/lexicon/` Skill** on the `memory-recall` pattern: `SKILL.template.md` +
  `role = "rendered"` + an adopter `--check` that re-renders and byte-diffs + a gate leg with **no
  guard**. This is the only mechanism in the brief that lets the full 1,787-byte table travel *and*
  stay bound to its source — a `.lexicon.conf` edit nobody re-rendered REDS. The charter can only
  point; the skill points and gates the pair.
- **The charter block points and shrinks.** Measured: `AGENTS.md` is 64,394 of 64,512 — **118 bytes** —
  and already emitting `TEMPLATE-SIZE WARN`; the template is 48,827 of 49,152 — 325 bytes; the `VERBS`
  block is 1,787 bytes and the bare list is 125. A staged 193-byte bullet reds the gate by 87 bytes.
  Embedding is 15x over budget and the replacement bullet must be **net-negative** or landing day reds.

**Why this is ranked above the gate work in value even though it is ranked below it here in build
order.** It is the mechanism with the only measured record — 136 definitions, zero offenders — and its
failure mode is *absence*, not randomness. An LLM that has the vocabulary in context does not generate
randomly; this repo demonstrated it 136 times. The fix for absence is supply. The gate is the backstop
and should be sized like one.

**The guards that keep `--brief` from becoming the mirror it looks like.** The §12 ban is on the
*gate's* vocabulary — the thing that decides pass/fail. The brief decides nothing. Make that structural,
not stated: exit code 0 only, no pin output, no path from the brief's histogram into
`scaffold_lexicon.py`, and a header saying *this prints what the corpus does, never what it should do*.
**And it must declare its coverage mode** — handed a `.sh` path (82 files, 60% of this repo's
definition-carrying files), an empty "established here" section reads as *"nothing is established,
invent freely"* and is byte-indistinguishable from *"this language is not extracted"*. Print
`COVERAGE: dark — nothing extracted for .sh` and refuse.

**Cost.** `--suggest` 0.045 s. `--brief` 0.18 s gov / ~1.6 s incms. Skill `--check` leg 0.8 s.

**Failing case.** The skill's `--check` byte-compare: edit `.lexicon.conf` without re-rendering → RED.

**Unmeasured, and flagged rather than assumed.** Skill trigger rate for a "before you name something"
description is unknown and there is no in-repo precedent — `memory-recall`'s description is
question-shaped, which is a much stronger trigger signal. And nothing measures whether an agent handed
the brief actually uses it; the same PostToolUse-observer instrument that `recall-opened.js` exists to
provide would answer it, and should ship *with* the brief rather than after it.

---

### R10 — The scoped extractor and P6 (short-name-in-wide-scope) · **BUILD, after the exemption class**

**What.** Replace `_python_defs`'s `ast.walk` (`lexicon.py:140-169`, four node types, scope-blind by
construction) with an `ast.NodeVisitor` emitting `(name, line, kind, scope, span, public)`. Widen
`extract()`'s 3-tuple to a record list; three call sites unpack it, and the third
(`drift_report.py:715`) is index-based and survives. Then one predicate: `len(name.strip("_")) >= 3`
unless the name is in a **kit-owned** 14-name allowlist (`i j k n x y z id db fn ok rc ts fd`) or the
enclosing scope is ≤ 10 lines.

**Why only this one predicate out of the four proposed.** The span condition is the entire design and it
is measured: the same rule fires **51 times above the cut line and 1,033 below it**. Twentyfold. It is
the only one of the four whose adopter number stays in three figures (gov 55, incms 481). And the knobs
are **kit constants, not conf keys** — D1 published its own threshold menu (87 / 120 / 65 / 51), and an
offender count selected from a menu is a pin wearing a threshold's clothes.

**The cut line, which is the reusable result.** Gate reach ≥ 2 (module-level names, type names, class
attributes, parameters — 2,349 of 8,249 bindings). Never gate `comp_target` (764 occurrences over
**65** distinct names), `except_alias` (88 over **3**), `with_alias` (62 over 7), `for_target` (870
over 189), locals (4,000, of which 865 are `len < 3`). A predicate over an already-converged population
is a check that cannot fail.

**Cost.** +0.091 s gov, +0.938 s incms — inside a parse that already happens.

**Failing case, and both arms are required.** Stage a 40-line function with a parameter `d` → RED.
Stage the same parameter in a 4-line function → GREEN. Without the second arm P6 is a plain length rule
that would have shown 1,033 offenders and the span condition is decorative.

**Blocked on.** The `^visit_[A-Z]` / `generic_visit` structural exemption class, which must itself carry
the unselective-rule refusal (a shape matching zero definitions REDS) and a printed exemption total.

---

### R11 — The consistency instrument · **RESEARCH**

**What.** Group every definition by its **object** (subtokens after the leading one) and measure whether
the members agree on the leading token. No vocabulary. Nothing to ratify, freeze, or re-derive. Measured
today: `824 defs · 589 carry an object · 418 distinct objects · 47 objects spelled with more than one
leading token, covering 167 definitions · CONSISTENCY = 0.716`.

**Why it is the most interesting idea in the brief and why it is not a recommendation yet.** It is the
only instrument that measures what the owner actually asked for, it cannot mirror (no vocabulary, so
§12 does not apply), it is a ratchet by construction (both operands derived from the tree, so unlike a
pin it cannot be raised by editing a number), and it fires exactly where two sessions disagreed. It
finds 60 genuine conflicts P1 calls **green** (`load_conf` vs `read_conf`; `region` spelled five ways,
all legal) and it declines to fire on the **354 of 459 offender keys that conflict with nothing**.

If it survives, the architecture inverts: **consistency is the gate, the table is the arbiter, the
declaration is the product.** The verb table stops being an allowlist 56% of the corpus fails and
becomes a tie-breaker for the ~47 live conflicts — which is the only structure under which "closed" is
a property you can hold rather than a convention you hope for.

**Four disqualifying gaps, which is why this is RESEARCH.** It is silent on the **first instance** — a
group of one scores perfectly, at exactly the moment an LLM most needs an answer. A repo where every
function is `get_*` scores **1.000**, so it is orthogonal to quality. It has no opinion and can never
say `load` not `fetch`. And the `tokens[1:]` keying produces junk: `of` collects `ext_of`, `owners_of`,
`parent_of`, `cache_of`; `root` collects `repo_root` and `map_root`, which are different roots — by
inspection roughly **half** of the 47 groups are artifacts.

**What research means concretely.** Build a real concept key, hand-measure precision on ≥40 groups on
gov **and** on incms, and only then decide whether the table demotes to arbiter. Do not ship a metric
whose precision is 50%.

---

## 4. THE THREE OWNER DEMANDS

### Demand 1 — "coverage beyond function names, explicitly including VARIABLES"

**Achievable MODIFIED, and much smaller than asked.** Four measurements settle the shape:

- Verbs do not transfer. Leading token is a declared verb for **1.7%** of module constants, **1.0%** of
  parameters, **0.0%** of class attributes, **0.4%** of locals. Pointing P1 at variables is a 98-100%
  offense rate — a syntax error with a delay.
- A noun table is the mirror in pure form. **469 distinct leading tokens** govern the 1,640 gated
  variable bindings; a 300-row table still leaves 169 offenders; zero requires all 469, at which point
  the table *is* the corpus. There is no knee. Verbs are a closed word class; nouns are an open one.
- The variable analogue of every curation-free instrument collapses. Grouping `name = call(...)` by
  callee: 124 producers used ≥3 times, **99 of them (80%) bound to more than one name**. `sorted()` is
  bound to `orphans`, `names`, `missing`, `slugs`, `roots` — all correct, because a variable names the
  value's *role* and roles are legitimately many.
- **71.5%** of bindings (5,900 of 8,249) have reach ≤ one function body. A name a single reader carries
  ten lines costs nothing to get wrong.

**What ships:** the scoped extractor so scope and span exist at all (R10), the short-name-in-wide-scope
predicate (R10, gov 55 / incms 481), and the synonym-group debt **reported by `--probe`, never gated**
(R7). **What is refused:** a verb or noun table over variables; casing as a kit predicate (it is
`ruff --select N` / `eslint camelcase`, and on incms's `.tsx` the rule reds **1,072 PascalCase React
components** — the exception list *is* a vocabulary, the mirror one layer down); synonym groups as a
gate (2,016 sites on incms is a rewrite, not a baseline).

The owner's instinct is right and the target is wrong. 77% of what the kit already grades is noise it
cannot act on; adding four more predicates over 2,349 more bindings without fixing that ratio produces
four more absorbing pins, which is exactly how we got here.

### Demand 2 — "real constraining pressure, not a ceiling that absorbs"

**Achievable AS STATED**, via R8's assert C. The integer disappears; the grandfather set's every member
must be provably derivable as an offender at a frozen sha, and no edit to the present tree can change
what a past commit contains. The cost ordering inverts: today it is *raise the pin (1 min) → waive (2
min) → add a verb (5 min) → rename (10 min)*, i.e. the cheapest path buys nothing. After R8 it is
*rename → add a verb → waive*, and **raise does not exist**.

Two honest caveats the owner should hear. First, on **this** repo the pressure buys almost nothing —
new code is already at 0% marginal offense; the ledger's real customer is an adopter with 6,299 rows of
legacy debt. Second, the pressure **concentrates on waivers**, which is why R3 is a hard prerequisite
and not tidying.

### Demand 3 — "on-demand probe in EXISTING adopter repos that emits guards forcing rework"

**Achievable MODIFIED, and the population is currently ZERO.** Neither `incms/main` (a full gov adopter,
6,165 files, `.governance/` present) nor `swydee` carries `.lexicon.conf`. `check_runbook_parity.py`
reports **18 registry entries with no runbook section, `lexicon` among them**, and has zero callers —
so a hand-wiring adopter is never told the kit exists. **Wiring that parity gate is upstream of
promising any of this**, and it is not the lexicon's work.

The **probe** half is buildable exactly as asked and is R7: `--probe`, read-only, no arguments, no
state, safe to run against any repo at any time. The **"emit guards forcing rework"** half must be
delivered as the ledger + the outbox `[[hole]]` + the shrink-only asserts (R8) and **refused in the
touch-rule form**. D3's touch rule ("you may not edit a file and leave its naming debt behind") priced
itself at a median of 4 renames — that is rows per **file**. A landing touches many files: measured
rows per **commit** is **median 42 on gov (max 77) and 41 on incms (max 281)**, and it would stop 15% of
gov's landings and 38% of incms's. It is also not on the merge bar (it runs at pre-commit, which
`--no-verify` bypasses), so it is advisory pressure sold as a forcing function.

---

## 5. PHASED ROADMAP

### Phase 0 — Honesty. R1, R2, R3, R4, R5, R6. All SHIP.

Nothing about the vocabulary changes and the pin still exists. What changes is that the kit stops
lying about what it measured.

**Exit criteria.** The green line prints `graded/offenders/waived` per predicate. An armed predicate
with a zero population prints `DEAD PREDICATE` and reds — failing case staged and observed against
`.js` today. `--measure` no longer exits 0 over UNDECLARED EXTENSIONS / DEAD PROBE / STALE WAIVERS.
Corpus scoping prints `graded N of M · excluded K` and reds on a zero-matching rule. Every waiver row
carries a reason and a `path::name` key. Three `RATCHETS` rows land **and** the delete-then-re-add hole
at `drift_report.py:198-221` is closed, both arms observed. The coverage fraction is printed and floored.
The marginal-rate signal is reporting with a liveness assertion.

**Unblocks.** Every derivation (scoping), every pressure design (waivers), and the ability to tell
whether any of the rest worked (the signal). Ship Phase 0 even if the owner rejects everything below.

### Phase 1 — Supply. R9.

**Exit criteria.** The rendered skill's `--check` byte-compare leg is on the bar with no guard, and a
conf edit without a re-render REDS. `--brief` declares its coverage mode and refuses on a dark
extension. `--suggest` returns in under 100 ms. The charter's §12 block is **net-negative** in bytes and
the `charter size` leg is green. The uptake observer ships with the brief, not after it.

**Unblocks.** The one mechanism with a measured record gets a machine holding it identical to source
instead of relying on a session happening to open the conf.

### Phase 2 — The canon and the probe. R7.

**Exit criteria.** The demo regression fixture passes: 500 `frobnicate_*` definitions through
`--probe --write` and `frobnicate` does not enter `VERBS`. The polarity arm passes: `get`=1, `fetch`=1,
`load`=0 proposes `load`. `--scaffold`'s frequency allowlist is **deleted**, which retires
`TOOL-dScaffoldedMirror-1` by removing its subject rather than patching the write path a fourth time.
The 11 missing negative definitions are backfilled and the structured-`NOT` assert is armed.

**Gate on Phase 3.** Run `--probe` read-only against `C:/projects/incms/main` and read the report. Its
day-one ledger there is 6,482 rows, and that number decides whether R8 is adoptable at all.

### Phase 3 — Extraction. The structural exemption class, then R10.

**Exit criteria.** `^visit_[A-Z]` / `generic_visit` exemption landed, kit-owned and closed, with its
zero-match refusal observed and its exemption total printed. The scoped visitor lands **without redding
the gate** — the staged break that reds today at 471 over 463 re-runs green. P6's two arms observed
(40-line scope RED, 4-line scope GREEN).

### Phase 4 — Pressure. R8.

**Exit criteria.** Five asserts, each staged and confirmed RED then unstaged, with assert C's arm — a
hand-added row for a post-freeze function — documented as the first assertion in this kit's history
that a ceiling edit could violate. All three `*_OFFENDER_PIN` keys deleted from `.lexicon.conf`,
`PIN_KEYS`, the `lexicon-pins` hole text, and the three `RATCHETS` rows from Phase 0, **in one commit**,
plus an assert that a `RATCHETS` row names a live key. ~70 lines of pin archaeology deleted. The
artifact sits in the kit dir with `role = "seed"` and `bash tools/memory-tree/check-memory-hygiene.sh`
is green. The three multiplicity keys renamed.

### Phase 5 — R11, if the owner wants it.

**Exit criteria.** A concept key better than `tokens[1:]`; hand-measured precision on ≥40 groups on gov
**and** incms; a written decision on whether the verb table demotes from allowlist to arbiter.

---

## 6. WHAT NOT TO BUILD

**A PreToolUse deny hook on P1.** 57.8% of 2,987 real agent-written definitions denied (79.1% within
gov), ~82.6% of those denials wrong, ~1.3M output tokens of forced re-emission, ~582 s of serial
latency — and it would refuse `boundedParallel`, a name §8 of the charter **mandates** and
`agent-cap.js` **enforces**, a live P1 offender at `tools/workflows/tier2-review.js:15`. This repo
already rejected a hook at 59.3% wrong (`scratch-guard.js`'s first spelling, measured over 23,966 Bash
calls). Settled twice.

**The mirror ratio M, red at M = 1.0.** Measured **M = 22/22 = 1.000 on the current hand-curated
table** — the metric declares the one table we know a human curated to be a mirror. It is also cleared
by *adding unused verbs*, i.e. the cheapest way to pass is the escape-hatch abuse it exists to detect.
And it deadlocks against `signal_lexicon_verbs_unused` (gateable, tolerance 0), which pushes M → 1.0;
the satisfiable window is "between one and three aspirational verbs", which is not a property.

**Adopter-authored `SHAPES` with a percentage ceiling.** One row, `^_`, exempts **102 of 463 offenders
(22.0%)** at only 12.4% of the graded population — four-fold headroom under a 50% ceiling, forever.
Three rows absorb 39% of the debt. Strictly worse than the integer: a pin absorbs a fixed count and
must be visibly raised again; a regex pre-absorbs every future `_helper` silently. And `^t_` would
legalise the exact drift the census identified. Structural exemptions must be **kit-shipped and
closed**, as in R10.

**The touch rule.** Median **42** renames per commit on gov, **41** on incms — not the 4 claimed, which
was rows per file. Not on the merge bar. Deferral reasons priced above renames on a human's cost model,
while the stated author is an LLM for which 16 one-line reasons is an order of magnitude cheaper than
16 renames with call-site verification.

**The dominance verdict table (CONVENTION / CONTESTED adopting the corpus's leader).** The corpus still
selects the legal form, which is the demo defect one indirection down, and it contradicts its own
falsifiable day-1 claim. Replaced by R7's unconditional-canon rule.

**P7 noun synonym groups as a gate.** It bans only spellings *already present*, so it is structurally
blind to the next name — and it is sold as the predicate that most directly attacks random generations,
which is precisely the case it cannot see. 2,016 sites on incms. Demoted to `--probe` output and merged
into the canon, which supplies the unseen spellings.

**P4 casing as a kit predicate.** It is `ruff --select N` (N801/N802/N803/N806) and `eslint camelcase`,
both installed one-liners with better test coverage than a stdlib re-implementation will ever have. And
"zero vocabulary" holds only until it meets a framework: incms's `.tsx` has **1,072 PascalCase function
bindings** (React components) and `.ts` has 1,281 SCREAMING_SNAKE consts at nested scope. The compensating
documented check is a README line telling adopters to wire their language's own linter.

**P5 as a fourth predicate alongside `BANNED_SUFFIXES`.** D1's 19-row blocklist contains **all eight**
current `BANNED_SUFFIXES`, lowercased — one fact, two carriers, two pins, two waiver registries, and a
site waivable in one while counted in the other. If it is built at all it **replaces** P2 and
`BANNED_SUFFIXES` leaves the grammar in the same commit; and the list must be re-derived per adopter
(gov 6, incms 484), because a blocklist curated against 44 files is the "pin copied from a larger tree"
defect inverted.

**The `extern` coverage mode.** It adds an arbitrary adopter-declared subprocess per language per run
inside a merge-bar check, plus a schema, a validator, a conformance fixture and a `MISCONFIGURED` state
— a new trust boundary and four failure modes, for a language nobody has asked for, in a kit with zero
adopters. Its conformance fixture is a known-answer test the adopter's own argv can special-case.

**Arming `sh` under P1.** 518 shell definitions, **433 (83.6%) off-table** — a 94% increase on a 463
population, from a language the kit declares dark by a written law.

**Replacing `scan_unselective_rules` with a live-candidate-edge count.** A "live candidate edge" as
proposed *is a violation*; zero of them is what a rule being **obeyed** looks like. The predicate cannot
distinguish unfireable from satisfied, and it would red this repo for keeping the rule that
`subtokens.py` was ported rather than imported to honour. If liveness is wanted, assert it on the FROM
side: does the FROM layer issue at least one import the resolver resolves to a tracked file? Measured:
38 issued, 7 resolve — armed today, and dark under the pre-fix resolver.

**Pay-as-you-go drain (K added ⇒ K drained).** Diff-scoped, therefore base-dependent, therefore killed
by the same argument that kills diff-scope at the merge bar. Stacked on top of a 42-rename median it is
a tax on a tax.

**Self-declared per-1000-file wall-clock ceilings that red on breach.** Wall readings vary 3x on node
`d` because its AV taxes every exec; a wall-clock RED inside a stdlib checker is a flaky gate on the
machine that would run it most, and a flaky gate gets bypassed. The real gap is that
`tools/gate-legs.json`'s leg schema is `{argv, chunk, guard, impure, name, subject}` with no ceiling
field — that is a change to run-gates' manifest contract and it is somebody else's unit. Sanity check on
the proposed numbers anyway: incms would get an 18.5 s ceiling against a measured 8-10 s run, i.e. a
check that cannot fail.

**`memory/lexicon/` as the artifact location.** Reds `HYGIENE check 3`, exit 1, measured.

**Embedding the verb table in the charter.** 118 bytes of headroom against 1,787; a 193-byte bullet reds
the gate by 87. Not a preference — arithmetic.

**A calendar drain schedule.** It becomes the pin one level up; moving a deadline is one edit.
`PLAY-dClosedLexicon-1` has sat BLOCKED on a ceiling raise since 2026-08-16, which is the receipt.

**A kit-owned JS/TS lexer — not now, and here is the condition.** Cost is fine (a stdlib prototype hit
21.9 MB/s, 0.439 s over incms's 1,236 TS/TSX/JS files). The objection is order: it arms P4 over 1,072
React components and P7 over a TypeScript corpus nobody measured, and it has **no independent oracle** —
the conformance fixture is written by the lexer's author and round-trips through the lexer's own
reading, which is the P3 tautology this kit already recorded. Revisit only after P4 and P7 have
adopter-scale answers, and only with fixtures extracted from real adopter files rather than authored.

---

## 7. OPEN QUESTIONS FOR THE OWNER

**Q1 — F4 is standing and it would delete the thing you are asking to strengthen.** *"Retire P1 if it
goes unused across two adopters"* is owner-ratified (2026-08-16) and a later session is entitled to
close P1 on that evidence without reopening the argument. P1 is adopted in exactly one repo and used in
none. Supersede it explicitly, or execute it — the answer decides whether Phases 2-4 happen at all.

**Q2 — F-A5 says the kit must be OPT-IN *because* its benefit is unmeasurable, and §3 makes "any claim
that this kit catches defects" a non-goal.** Both are owner-ratified and both are the recorded reason
the kit ships without pressure. R8 makes it binding once adopted; R6 makes the benefit measurable for
the first time. This needs an explicit written supersession, not an assumption.

**Q3 — does gov itself take the pressure, or only adopters?** Gov's new code is already at 0% marginal
offense; the ledger's customer is a repo with 6,299 legacy rows. If gov never adopts R8, the design
ships untested on its own repo, which contradicts the dogfood law this charter opens with.

**Q4 — `t_` (52) and `do_`/`cmd_` (27): two decisions worth 79 of 459 keys, 17% of the backfill.** All
52 `t_` are self-test functions and `test` is already a table row; all 27 are CLI subcommand
entrypoints split by kit (`do_` in memory-tree, `cmd_` in govkit) with no reserved verb. Rename them, or
reserve a verb, or carry them as debt? Deciding **before** the backfill is the difference between 380
rows and 459.

**Q5 — the noun-led population is ~288 of 463 (62%) and nobody has ruled on it.** Is a noun-led
definition legal in this repo at all, and if so only for `@property`, `@cached_property`, or a
zero-argument accessor? All three are detectable in `ast`. This is the single largest lever on the
debt and no design decided it; the 73.9% "not verb-led by nature" figure is one reader's hand
classification of 46 items with a 61-87% CI.

**Q6 — may `--probe` be run read-only against `C:/projects/incms/main`?** Every adopter figure in this
report is a faithful re-implementation of the kit's predicates against that corpus, **not the kit's own
binary**. The 44-extension `LANGS` requirement and the 6,482 ledger size are derived, not observed. A
read-only probe run there before Phase 4 would replace the largest remaining estimate in the plan.

**Q7 — freeze advancement.** I recommend forbidding it entirely in v1: the set only shrinks, and the
subset rule that would allow a forward re-freeze is the one place a base sneaks back into a
deliberately base-free design. If you want the escape hatch, say so, and it comes with a base and its
failure modes.

---

## Appendix — the adopter probe, verbatim

Run read-only against a target repo, writing nothing to it:

```bash
python <this-script> tools/lexicon <target-repo> .lexicon.conf
```

```python
"""Read-only probe of a target repo using the lexicon kit's OWN extractor and this repo's table.
Writes nothing to the target. Reports what the kit would say if adopted there."""
import subprocess, sys, collections
from pathlib import Path

KIT = Path(sys.argv[1])          # gov's tools/lexicon
TARGET = Path(sys.argv[2])       # the repo to probe
CONF = Path(sys.argv[3])         # gov's .lexicon.conf (the declared table)
sys.path.insert(0, str(KIT))
import lexicon as L
from lexicon_conf import load_conf, langs
from subtokens import leading_verb

conf = load_conf(CONF)
verbs = set(conf.get("VERBS", {}) or {})
banned = (conf.get("BANNED_SUFFIXES") or "").split()
declared = {e: (p, m) for e, p, m in langs(conf)}

files = [ln for ln in subprocess.run(
    ["git", "ls-files"], cwd=TARGET, capture_output=True, text=True).stdout.splitlines() if ln.strip()]

by_ext = collections.Counter(L.ext_of(f) for f in files)
print(f"TARGET {TARGET}   tracked files: {len(files)}")
print(f"TABLE  {len(verbs)} verbs, {len(banned)} banned suffixes, from {CONF.name}")
print()
print("=== 1. LANGS declaration burden: every extension present must be declared ===")
undeclared = [(e, n) for e, n in by_ext.most_common() if e not in declared]
print(f"extensions present: {len(by_ext)}   already declared by gov's conf: {len(by_ext) - len(undeclared)}"
      f"   UNDECLARED (each a named refusal): {len(undeclared)}")
for e, n in undeclared[:25]:
    print(f"    .{e or '<none>'}  {n} file(s)")
if len(undeclared) > 25:
    print(f"    ... and {len(undeclared) - 25} more")
print()

# What the kit can actually extract: py=parser, js=probe. Everything else has no extractor at all.
ARMED = {"py": ("parser", ""), "js": ("probe", "js-regex")}
p1 = []
p2 = []
defs_total = 0
files_with_defs = 0
parse_fail = 0
lead = collections.Counter()
for f in files:
    e = L.ext_of(f)
    if e not in ARMED:
        continue
    mode, pset = ARMED[e]
    try:
        got = L.extract(TARGET / f, mode, pset)
    except SyntaxError:
        parse_fail += 1
        continue
    except Exception:
        parse_fail += 1
        continue
    if not got:
        continue
    funcs, types_, _ = got
    if funcs or types_:
        files_with_defs += 1
    defs_total += len(funcs)
    for name, line in funcs:
        v = leading_verb(name)
        lead[v] += 1
        if v and v not in verbs:
            p1.append((f, line, name, v))
    for name, line in types_:
        for suf in banned:
            if name.endswith(suf):
                p2.append((f, line, name, suf))
                break

print("=== 2. What the kit's armed extractors reach here ===")
py_n, js_n = by_ext.get("py", 0), by_ext.get("js", 0)
print(f"armed: .py {py_n} file(s) parser + .js {js_n} file(s) probe = {py_n + js_n} of {len(files)} tracked"
      f"  ({100.0 * (py_n + js_n) / len(files):.1f}%)")
print(f"unparseable under the parser declaration (would RAISE, not skip): {parse_fail}")
print(f"function/method definitions graded: {defs_total} across {files_with_defs} file(s)")
print()
print("=== 3. P1 offenders against gov's 22-verb table ===")
print(f"P1 OFFENDERS: {len(p1)}   distinct names: {len({n for _, _, n, _ in p1})}"
      f"   offense rate: {100.0 * len(p1) / defs_total:.1f}%" if defs_total else "no definitions")
off_lead = collections.Counter(v for _, _, _, v in p1)
print(f"distinct off-table leading tokens: {len(off_lead)}")
print("top 25 off-table leading tokens:")
for v, n in off_lead.most_common(25):
    print(f"    {v:<18} {n}")
print()
print("=== 4. P2 offenders (banned type suffixes) ===")
print(f"P2 OFFENDERS: {len(p2)}")
for f, line, name, suf in p2[:15]:
    print(f"    {f}:{line}: {name}  (ends '{suf}')")
if len(p2) > 15:
    print(f"    ... and {len(p2) - 15} more")
print()
print("=== 5. In-table leading tokens actually used here (the overlap) ===")
in_table = [(v, n) for v, n in lead.most_common() if v in verbs]
print(f"{sum(n for _, n in in_table)} of {defs_total} definitions already lead with a declared verb"
      f"  ({100.0 * sum(n for _, n in in_table) / defs_total:.1f}%)" if defs_total else "")
for v, n in in_table[:15]:
    print(f"    {v:<18} {n}")
```
