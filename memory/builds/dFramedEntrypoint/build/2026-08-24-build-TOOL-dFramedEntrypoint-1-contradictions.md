**Serves:** research TOOL-dFramedEntrypoint-1

*Research lens for the `dFramedEntrypoint` design pass — the adversarial hunt against the owner proposal. Produced 2026-08-24, node d, against base 9ddcc5c9. Findings in this record were subsequently adversarially verified; where the verification corrected a claim, the verification record wins.*

# The refutation lens — where the build-README proposal contradicts the record, and where the record is wrong

Every claim below carries an id, a `file:line`, or a command whose output is quoted. Ranked
BLOCKING / MATERIAL / MINOR, with DISSOLVED refutations at the end.

All paths are repo-root-relative to
`C:/projects/coding-governance/.claude/worktrees/build-readme-governance-18d6ea`.

---

## BLOCKING

### B1 — "DERIVED first" structurally destroys the only signal that can see a planned-but-unspecced unit

The proposal's roster table is "unit, ORDER #, tier, status, rev, last change" — every column
derived from spec status headers. A roster derived from specs **cannot, by construction, contain a
unit that has no spec.** That is not a nuance; it is the exact question the corpus already pays a
region to answer.

`tools/unattended/unattended.sh:1487-1493`:

```
roster_ids() { # slug -> ids the AUTHORED plan names, which may include unspecced units
```

and the comment that governs it, `unattended.sh:1483-1486`:

> The two questions are SPLIT rather than merged. Authorization, the presence term and terminality
> read the GENERATED region, which is what makes them satisfiable without a hand-edit. The
> planned-but-unspecced question keeps the authored pair.

`missing_units()` at `unattended.sh:1511-1515` is `roster_ids` minus `spec_ids`, and it feeds
`build-complete`'s term 3 at `unattended.sh:2717-2721` — "the authored plan names a unit that no
tracked spec carries, so the build is incomplete by its own roster". That is a Definition-of-Done
item with **no override**, and its only input is the AUTHORED roster.

`memory/builds/aRuledFrontispiece/README.md:96-99` states the same thing from the other side and
names the constraint that makes it hard:

> A row gains its id when its spec lands. **A planned unit may not be named by id here before then**
> … hygiene check 14 reds any id cited but never defined, this table cited nine of them, and the
> orphan waiver registry is shrink-only.

So the authored roster's whole job is to name work that does not exist yet, and the id gate forbids
naming it by id. A derived table replaces a forward-looking plan with a rear-view mirror.

**Measured**: `grep -l "roster:units" $(git ls-files "memory/builds/*/README.md") | wc -l` → **12 of
61**. On the other 49, `missing_units` returns empty and `build-complete`'s term 3 passes
vacuously — the repo's own `memory/gotchas/vacuous-selector-empty-population.md` class, live today.

**What this means for the design.** The proposal must state explicitly whether the roster table is
(a) derived-only, in which case `roster_ids`, `missing_units` and `build-complete` term 3 must be
retired in the same change and the owner must accept that "you planned 13 units and specced 9" is
no longer machine-observable; or (b) a UNION — derived rows for specced units plus authored rows for
planned ones — which is a hybrid the "DERIVED/COMPUTED first" phrasing does not currently permit.
Silence here ships a broken DoD item, not a tidier README.

### B2 — the wrap-up's "open / parked" row loses its only source

`memory/guides/BUILD-METHOD.md:176-178` (M6):

> **Parking, at any point.** Write the *question*, the *options you saw*, and the *reason you
> refused* into the build's authored record. A bare "parked" is indistinguishable from "forgotten",
> and M9 is where the owner gets the turn you did not take.

`BUILD-METHOD.md:254` (M9's derivation table):

> | open / parked | every `surfaced`-class parked entry in the authored record (M6) with question,
> options and reason … |

`BUILD-METHOD.md:200-202` (M7 regrounding, read order, step 2):

> The build's authored record whole (under a mandate `memory/builds/<slug>/RUN.md` …) — mandate,
> phase, witness, parked entries.

Under an unattended mandate the run-state file carries parks. **An attended build has no `RUN.md`,
so the build README IS the authored record.** The proposed slot list — technical header, title,
immutable description, improvements, detriments, one paragraph of rules, roster, edges — has **no
slot for a park**, and M9 says a wrap-up row with no source on disk "is not 'unknown' — it is work
that did not happen".

Live carriers: `memory/builds/aRuledFrontispiece/README.md:214-262` ("Parked — four RESOLVED by the
owner, one still open", P1-P7 with question/options/reason each), and
`memory/builds/aBranchedMandate/README.md:114-156` ("UNPARKED 2026-08-17 …", "PARKED — unit 4 …").

Also `BUILD-METHOD.md:133`: when the BLOCKED review loop hits its runaway ceiling, "the run promotes
and lands anyway and says so in its output AND the build README." That is a mandated README write
with no slot in the proposal either.

**Decision the owner owes**: either a `PARKED` slot survives in the template (and it is authored, and
it is append-only, which makes it exactly the kind of prose the proposal is trying to ban), or M6,
M7 and M9 are amended in the same change to route parks somewhere else. Amending three method
sections is a bigger blast radius than the README redesign itself.

### B3 — kickoff fork rulings bind the SET, not one spec, and moving them into specs has a measured failure

The proposal: "'OWNER DECISIONS' … belong strictly in the individual specs, if anywhere at all."

`memory/builds/aRuledFrontispiece/README.md:23-26`:

> ## What the owner decided at kickoff
>
> Eight forks were put and answered before any spec was written. They are recorded here because five
> of them reverse or constrain a rule stated elsewhere in this repo, **and a spec that re-litigates
> one has misread this table rather than found a new option.**

Fork 1 in that table does not bind one spec — `README.md:39-43` records that it also resolves an
open fork belonging to **another build** (`cBriefedPilot` spec-7 §8, `Resolver: owner` unresolved).
A ruling with cross-build reach cannot live in one spec of one build.

And the corpus has already run the experiment. `memory/builds/dScriptedRepeat/README.md:37-44` and
`:46-53` moved the seven kickoff forks and the four rounds of owner rulings out to `build/` records
under byte-cap pressure. The result, recorded in the file itself:

> the trim that wrote this paragraph pointed at a "kickoff record" that did not exist, which is
> round 4's MEDIUM 9 …
> Both records spell their fork numbers in prose, so a grep for `fork 5` resolves — the table rows
> are verbatim and number their first column bare, which is exactly how **four citations went
> dangling** at the first move of this kind (round 4, MEDIUM 9). **There is no gate for this; it is
> a documented check.**

So relocating rulings out of the README is a move this repo has performed once and measured four
broken cross-references from, with no gate to catch a fifth. And `dScriptedRepeat/README.md:70-73`
still cites "Fork 6" and "Fork 5" by bare number from the README body — those citations resolve only
because the relocated record spells them.

**This does not refute the owner's instinct**; it prices it. A ruling relocation needs a citation
grammar and a check, or it repeats a measured defect. That work is not in the proposal.

### B4 — the corpus surgery this proposal implies has no derivable ORDER to put in the roster

The proposal's roster column is "ORDER #". The machinery exists and its population is **zero**.

```
$ grep -l "gen:build-order" $(git ls-files "memory/builds/*/README.md") | wc -l
61
$ grep -l "No spec under this build declares an" $(git ls-files "memory/builds/*/README.md") | wc -l
61
```

Every one of the 61 build READMEs carries a `gen:build-order` region and every one of them is empty.
Zero specs in the corpus carry the `order <n>` verb. Same for edges:

```
$ grep -l "This build declares no parent and no build declares it as one" … | wc -l
61
```

Zero READMEs declare `parents:`. The proposal's "build parents/children" slot is a region that
shipped and nobody fed.

Two records explain why, and both are unclosed:

- `memory/map/features/build-readme-surface.md:108-109`: "The `order` verb is PERMITTED and not
  required, so the build-order region is empty for every build that has not adopted it. Requiring it
  needs a dated cutoff, **which the owner deferred to a follow-up.**" (fork 5,
  `aRuledFrontispiece/README.md:35`: "permitted in this build, required in a follow-up commit").
- `memory/builds/aRuledFrontispiece/reviews/2026-08-17-review-TOOL-aRuledFrontispiece-1-3.md:35`, a
  HIGH that was never folded: `memory/TEMPLATE-SPEC.md:50` says "The tail holds POINTERS only — a
  review workflow id, `ratified <date>` — never prose", and the `order` verb occupies that slot. The
  review's own grep for the verb across `AGENTS.md`, `HYGIENE.md`, `TEMPLATE-SPEC.md`,
  `memory/README.md`, `memory/guides/` and both kit templates "returns nothing". I re-ran it today
  over the same six carriers plus `SPEC-TEMPLATE.template.md`: **still zero.** The verb the ORDER
  column would derive from is undocumented, unadopted, and formally forbidden by the spec template's
  own tail rule.

Meanwhile `memory/backlog/TOOL.md:117` (`TOOL-aBoundedVerdict-7`, OPEN) says the owner's instinct is
already recorded as a want:

> nothing records inter-unit dependencies; a build README's authored order carries them in prose …
> A front-matter dependency field would make it derivable — its own unit

**So**: the ORDER column is not a new idea, it is an adoption mandate for a region that shipped in
aRuledFrontispiece and has zero users. Shipping the column without (a) a dated cutoff making the verb
required, (b) the TEMPLATE-SPEC tail-grammar amendment, and (c) a corpus backfill across 61 builds,
produces a column that renders empty everywhere — the exact "green by absence" shape the charter §7
bans. And an ORDER integer alone loses the "Why here" column that
`memory/builds/dUnstalledConvoy/README.md:196-209` and
`memory/builds/dScriptedRepeat/README.md:99-111` (a PREDECESSOR list, not an integer) both carry —
neither is derivable from an integer, and the second is a strictly richer encoding the `order` verb
cannot express at all.

---

## MATERIAL

### M1 — the marker-bounding refusal does NOT block a closed heading canon, and the dossier misstates it

Two sources, and they do not say the same thing.

The **dossier**, `memory/map/features/build-readme-surface.md:29-32`:

> **The slot sequence is positional, not delimited.** … Bounding the prose with markers instead was
> considered and **refused by the owner**: it would have let authored content sit anywhere and made
> the contract a labelling convention rather than a shape.

The **primary record**, `memory/builds/aRuledFrontispiece/spec/2026-08-16-spec-TOOL-aRuledFrontispiece-1.md:156-162`
(§4 "Alternatives rejected"):

> Bounding the prose by a marker pair of its own was rejected: it makes every README carry two more
> lines to solve a problem that position already solves, and an author who puts prose in the wrong
> place is not helped by being asked to wrap it.
>
> Detecting the plan slot by heading text rather than by a marker was rejected because
> `check_authorization` in the unattended kit byte-compares a marker-delimited region across a base
> commit, and a heading is not a delimiter it can address.

Three findings:

1. **The dossier's attribution is unsupported.** The spec records these as the spec author's
   rejections, in §4, not as an owner ruling. `aRuledFrontispiece/README.md:23-40` lists the eight
   forks the owner actually answered and marker-bounding is not among them; the parks P1-P5 at
   `:236-262` are not it either. The dossier line entered at commit `12b9ee45`
   (`TOOL-aRuledFrontispiece-6`, the leg unit) and its phrase "labelling convention rather than a
   shape" appears **nowhere else in the tree** — verified by
   `grep -rn "labelling convention"`, one hit, the dossier itself. That is this repo's own
   `two-answers-to-one-question` class, sitting in the dossier that governs the surface under
   redesign.
2. **The second refusal has EXPIRED.** `TOOL-aBoundedVerdict-11` moved the frozen authorization
   scope off any byte comparison. `tools/unattended/unattended.sh:1226-1229`:
   "the frozen scope is the GENERATED units region's unit-ID SET, compared BASE -> HEAD and required
   to be a SUBSET … This REPLACES the authored roster pair's byte comparison, which S8 retires by
   deleting this reader". So "a heading is not a delimiter `check_authorization` can address" is no
   longer true of anything: `check_authorization` addresses only front matter and the GENERATED
   units region. The one recorded reason that actually blocked heading-based structure is gone.
3. **Answering the owner's question both ways, cleanly.**
   - *If the new contract is a closed, ORDERED heading set enforced positionally* (headings in a
     fixed sequence, each required or explicitly `N/A — <why>`): **this satisfies the old ruling
     rather than re-opening it.** The dossier's stated objection — "a labelling convention rather
     than a shape" — is an argument *for* the closed set: a total order over a closed heading
     vocabulary IS a shape, and it is the exact shape hygiene **check 12** already enforces on every
     Tier-2 spec (`tools/memory-tree/check-memory-hygiene.sh:722`: "the canonical nine `##` sections
     (exact, in order) · no empty section bodies (write 'N/A — <why>')", date-gated by
     `SPEC10_CUTOFF` at `:35` so no landed file goes retroactively red). The proposal's own words —
     "strictly constrained to a template (similar to the SPEC template)" — name the shipped
     precedent.
   - *If the new contract is a marker pair per authored slot* (`<!-- slot:improvements -->` etc.):
     **this DOES re-open the ruling**, and the spec's objection still bites — every README carries
     2N more lines, and the corpus-surgery cost lands on 61 files. Nothing has changed that
     dissolves it.

   The owner can therefore have the tight contract without overturning anything, **provided** the
   enforcement is heading-canon-plus-order, not markers.

### M2 — the immutable description vs M8's mandated re-read: real tension, and the reconciliation holds empirically

`memory/guides/BUILD-METHOD.md:237` (M8):

> **Re-read the build README against the code before closing** — every owner ruling and every
> sentence naming a shipped mechanism. `readme_mechanism_drift` reports only the pairs that spell it
> identically; the fold owns the rest.

`memory/backlog/TOOL.md:12` (`TOOL-dScriptedRepeat-14`, CLOSED) and
`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-14.md:5-10`:

> this build's README said `--counts` takes the recorded FACTS while spec 6 rev-8, written in the
> same fold, said it takes a pinned BASE sha and re-parses the blob. Two answers to one question
> about the guard on the one Definition-of-Done item that takes no override — **and the README is
> the file a session opens first.**

The tension is exact: M8 mandates *correcting* README sentences at close; the proposal mandates a
description "added once, never re-authored". Both cannot govern the same sentence.

**The reconciliation the prompt hypothesised is CORRECT, and it is measurable.** The drift signal
scans only lines above the first generated marker (`tools/drift-audit/drift_report.py:957`:
`cut = next(i for i,ln in enumerate(lines) if ln.startswith(_GEN_MARK))`) and only backticked
mechanism tokens (`:963-980`). I ran it:

```
$ python tools/drift-audit/drift_report.py --json   →  readme_mechanism_drift
value 19  of 61  tolerance 19  live True
```

All 19 rows, mapped to their sections by heading line number:

| row | section it sits in |
|---|---|
| `aBoundedVerdict/README.md:91,103` | "Units — the authored roster" |
| `aBoundedVerdict/README.md:128` | **"Cross-unit rules"** |
| `aBoundedVerdict/README.md:281,283,290` | "The 2026-08-19 re-decomposition" / "Classification" / "What the audit changed about the dependency order" |
| `aBoundedVerdict/README.md:325,353` | "Why it stopped" / "Recommendations" |
| `aBranchedMandate/README.md:31` | opening block, a *mechanism-analysis* paragraph (C1/C2/C3 table follow-up) |
| `aBranchedMandate/README.md:97` | **"Build-level rules"** |
| `aRuledFrontispiece/README.md:81` | "Units — the authored roster (M2)" |
| `aTetheredRecord/README.md:84` | "Units — the authored roster (M2)" |
| `cBriefedPilot/README.md:161` | "The waiver, end to end" |
| `cFinalBerth/README.md:71,74,102` | "Owner decision menu" / "Review record" |
| `dScriptedRepeat/README.md:114` | "The unit set" |
| `dScriptedRepeat/README.md:125` | "What the spec audits changed" |
| `dScriptedRepeat/README.md:139` | "What is deliberately NOT in this build" |

**Zero of 19 land in a build's problem statement.** `aBranchedMandate/README.md:14-16` — "The
commissioning report was one sentence: unattended build tooling will not execute unless the build and
its specs are landed…" — carries no backticked mechanism and never drifted; the drifting line is
`:31`, three paragraphs later, where the file starts explaining `--preflight`.

**Two consequences the design must take:**

- The immutable description is safe **iff** it is a PROBLEM STATEMENT and names no mechanism of this
  build. A mechanism does not exist at kickoff, so a description that names one is already narrating
  the future. The phrasing rule is mechanical and checkable: **no backticked token matching the
  drift signal's `_MECH_RE` may appear in the immutable slot** — the same predicate, run as a
  refusal instead of a report.
- **The one authored slot the owner KEEPS mutable — "BUILD-LEVEL RULES" — is a proven drift
  carrier.** 2 of the 19 rows are in exactly that slot (`aBoundedVerdict:128` "Cross-unit rules",
  `aBranchedMandate:97` "Build-level rules"). Compressing it from bullets to "ONE paragraph" does not
  make it drift-free; it makes it denser. It must either carry M8's re-read obligation explicitly or
  be frozen at kickoff like the description.

### M3 — "one paragraph of BUILD-LEVEL RULES (may be empty)" is a downgrade with named casualties

Measured: 7 of 61 build READMEs carry a `## Build-level rules` heading. Read the two richest.

`memory/builds/aRuledFrontispiece/README.md:181-206`, six bullets, of which one is load-bearing and
irreplaceable:

> **Two legs are RED for a declared window, and that is accepted rather than hidden.** The
> verdict-epoch leg reds from position 1 until the kit version bump at position 7, and the
> kickoff-manifest ratchet reds until its re-stamp at position 8 … **The window is declared here
> with its discharge point so a red leg inside it is expected and a red leg outside it is a defect.**
> No other leg may be red at any tip.

That is the build's *merge-bar exception register*. It cannot go in one spec — it is a statement
about which of ELEVEN units may be red, and a resuming session that cannot find it reads a red leg as
a defect and stops. It is also the thing `BUILD-METHOD.md:174` ("A pass whose gate is red is not
followed by another") is overridden by. Under a one-paragraph cap this is the first thing squeezed.

`memory/builds/dUnstalledConvoy/README.md:160-181`, six bullets, one of which is a **disjointness
declaration**:

> **`.memory-tree.conf` is a BUILD-WIDE shared write, and it makes seven units mutually
> non-disjoint.** … They may NEVER be dispatched as a concurrent pair …

`BUILD-METHOD.md:179-186` (M6 parallelism) *requires* concurrent dispatch where disjointness is
proven and requires both write-path lists be written down before dispatch. A build-wide non-disjoint
declaration is the negation, stated once for the whole build. It is not one spec's fact.

**Verdict**: the slot should survive as a bulleted list with no arbitrary count, and it should be
named for what it is — build-scoped constraints that no single spec owns. "May be empty" is right;
"one paragraph" is a cap that will evict a red-leg window before it evicts prose.

### M4 — the char-cap instinct is right and this repo has measured it backfiring twice

The owner asked "(character guard?)" twice. The pattern in this repo is consistent and it is not the
one the question expects.

- `tools/memory-tree/check-memory-hygiene.sh:54`:
  `ENTRY_CAP_CHARS=300 ; BUILD_README_ENTRY_CAP_CHARS=350`. Check 7 grades **every line** of a build
  README against 350 chars, authored and generated alike.
- **Backfire 1**, `memory/project/curation-debt.txt:10-14`: three GENERATED unit-table rows in
  `aRuledFrontispiece/README.md` blew the per-line tier because the row carries the full spec title
  AND the path. Remedy taken: a curation-debt row, which silences checks **6, 7 and 8 on the whole
  file** to buy three rows.
- **Backfire 2**, `curation-debt.txt:40-51` + `memory/backlog/TOOL.md:20`
  (`TOOL-dUnstalledConvoy-13`, OPEN): a GENERATED record-bindings row measured **438 chars against
  the 350 tier**, "BY CONSTRUCTION: the row carries the record filename, its path and every id the
  record serves, and the binding grammar expands a contiguous range at authoring time so the ids
  cannot be abbreviated." The longest *authored* line in the same file is 319. The remedy again
  silenced checks 6 and 7 on the whole file.
- **The contrast**, `tools/check-template-size.sh:183`: the template gate WARNs past a recorded
  high-water and re-records on `--bump`. Advisory, ratcheted, never a hard stop that forces a
  blanket exemption.

**Pattern**: in this repo a hard char cap over a population that includes GENERATED rows has fired
twice, both times against a generated row, and both times the only available remedy was an exemption
**wider than the failure** — silencing three checks on an entire file to buy one row.

**Judgement on a per-slot char cap.** A per-slot cap over AUTHORED prose only is a different and
better instrument than check 7, because it excludes the population that broke check 7 twice.
Failure modes to price:
1. **Wrapping is not shrinking.** A cap on lines invites `\n`; a cap on the slot's total characters
   is what the owner actually wants. Say which.
2. **A hard cap with no ratchet forces the curation-debt shape.** A build legitimately at the cap
   has one exit today, and that exit disables unrelated checks. Adopt the `check-template-size.sh`
   high-water shape — WARN + `--bump` — or ship a slot-scoped waiver, never a file-scoped one.
3. **A cap on a slot that may be empty is unarmable one way.** Charter §7 demands a gate's failing
   case be observed; a cap on "may be empty" slots needs both an over-cap fixture and an empty one.
4. **Do not cap the ROSTER.** It is generated and it is exactly what broke twice.

### M5 — the "links are pointless" claim: the coverage joins survive, but the record links are already duplicated

Three separate questions were folded into the owner's one sentence; they have different answers.

**(a) Do the coverage joins survive the table's removal? YES — they are computed, not parsed.**
`tools/memory-tree/gen_build_index.py:666-678` builds `named`, `audited`, `gap` and `agap` from
`build["records"]` — the same data `read_bindings()` produces — and renders two sentences. Nothing
re-reads the rendered table. Deleting the `| Record | Kind | Serves |` table leaves both joins
intact.

**(b) Do the joins have a reader? YES, demonstrably.**
`memory/builds/aRelaxedShard/reviews/2026-08-18-review-TOOL-aRelaxedShard-4.md:541` uses one as
evidence in a confirmed LOW finding: "`-4` has none either; the README's generated region says so
('Ids no record names: TOOL-aRelaxedShard-4')". And `BUILD-METHOD.md:129` makes the underlying join
a method obligation: the `**Serves:**` line "is what makes 'every spec with no review record naming
it' answerable from the tree instead of from memory" — which is M4's selection rule for which specs
still need an audit.

There is no gate leg depending on them (`tools/gate-legs.json` has one build-README leg, "build
README slot contract", argv `gen_build_index.py --check-format`, `chunk: records`, `subject: repo`,
**no guard**), and no DoD item reads them: `build-complete` reads only the nested
`gen:build-units` region (`unattended.sh:2691-2721`). So they are advisory — but they are the
cheapest coverage signal in the corpus and they answer a method question.

**(c) Is the record listing duplicated? YES, twice over.** Measured across all 61 READMEs:

```
records-table rows: 221      gen:build-docs record links: 488
```

`gen:build-docs` lists **every** tracked record including every spec; the units table lists every
spec; the records table lists every record. So each spec appears twice and each record appears twice,
both times generated. `dScriptedRepeat/README.md` is 272 lines and carries 29 records-table rows plus
43 docs-region links; `dUnstalledConvoy` carries 24 + 48.

**Verdict.** The owner's instinct is correct about the *volume* and half-correct about the *value*.
The cheapest replacement, and it is genuinely cheap: **delete the `| Record | Kind | Serves |` table,
keep the two coverage-join sentences, and fold `Serves` into the `gen:build-docs` bullet as a
suffix.** That removes 221 table rows and one whole duplicate listing, keeps every link, keeps both
joins, and incidentally drains `TOOL-dUnstalledConvoy-13` — the 438-char row disappears with the
table that carries it.

### M6 — the leg named "build README slot contract" does not check anything the owner is complaining about

This is the crux of why the owner sees a "contract" and finds prose anyway.

`tools/memory-tree/gen_build_index.py:978-1005`, `slot_violations()` has **two triggers, both about
content AFTER the generated markers**:

- Trigger 1 — "authored content after the first generated marker"
- Trigger 2 — "authored content between the plan pair and the generated region"

Nothing constrains the authored region above the first marker: not its size, not its heading count,
not its heading names, not its content. The corpus is clean by this measure:

```
$ python tools/memory-tree/gen_build_index.py --check-format
build-index: slot contract clean (61 build README(s))   rc=0
```

…while carrying, in that same "clean" corpus, `aBoundedVerdict/README.md` at 417 authored lines with
15 headings including "The unattended run, 2026-08-19 — what it built and what it cost" and
"Recommendations, in the order that unblocks the most".

Charter §7: "A gate's OWN header states what it does NOT check. A structural check reads as a
semantic one to everybody who did not write it, and the resulting false confidence is worse than the
gap." `do_check_format`'s docstring (`:1137-1143`) states only *why it is unreachable from other
verbs*; it never says what it does not check. The module docstring's usage block (`:4-6`) does not
list `--check-format` at all.

**This is a MATERIAL finding independent of the redesign**: the leg's name promises a template and
delivers a boundary check, and that mis-promise is exactly what let the authored half grow unwatched.
Fix the header even if the redesign is refused.

### M7 — aRuledFrontispiece's central claim about itself is false as measured, which is the owner's case

`memory/builds/aRuledFrontispiece/README.md:20`:

> This build inverts that ratio. The README keeps exactly one bounded block of authored prose and one
> immutable authored plan; everything else is rendered from the sources that already own it.

Measured over the corpus today (61 READMEs, lines above the first `<!-- gen:` marker vs at-and-below):

```
total lines 8554   authored 5647 (66%)   generated 2907 (34%)
```

The ratio was not inverted. It is 2:1 authored. Top authored counts: `aBoundedVerdict` 417 of 509,
`cBriefedPilot` 316 of 408, `aRuledFrontispiece` itself 293 of 355.

The mechanism the claim rests on — "ONE authored prose block" — is satisfied by any amount of prose,
because M6 shows the predicate only checks that it sits before the markers. So the sentence is true
about *position* and false about *ratio*, and the file that says it is the third-largest offender.
The owner is not describing a lapse in discipline; he is describing a contract that was never written
to bind what he thought it bound.

### M8 — the dossier claims a retired region that is still read

`memory/map/features/build-readme-surface.md:55-62`:

> **The `roster:units` pair is authored, this generator never writes into it, and it is being
> RETIRED.** … `TOOL-aBoundedVerdict-11` … retires the authored pair by removing its readers …
> **A region nothing reads is inert.**

`tools/unattended/unattended.sh:1487-1493` (`roster_ids`) reads it; `:1511-1515` (`missing_units`)
calls that; `:2717` (`build-complete` term 3) calls that. Three live readers, in the DoD path.
`unattended.sh:1483-1486` says so explicitly — "The planned-but-unspecced question keeps the authored
pair."

The dossier is stale against the shipped code, in the dossier that owns this surface. Any design pass
that trusts it will conclude the authored roster is free to delete — which is B1.

---

## MINOR

### N1 — `tier` is one line from derivable

`HDR_RE` at `gen_build_index.py:101-104` already captures `Tier-(?P<tier>[12])`, but `parse_spec`
(`:275-285`) never puts it in the unit record. The proposal's `tier` column costs one dict key and one
table cell. This one is free.

### N2 — "dates" plural has no second source

Front matter carries `opened` only (`REQUIRED_KEYS` at `gen_build_index.py:111`). A `closed` date is
derivable as the max `last change` over terminal units, or from `derive_status`. Say which, or the
slot is authored and rots.

### N3 — the technical header must not lose the unattended keys

`parse_front_matter` requires `slug node opened streams roster ids`; `parents` is optional; and the
unattended kit additionally reads `authorized-by:`, plus a playbook path and piece count in recipe
mode (`unattended.sh:540-550`, checks 13/19 at `:923-990`). The proposal's list ("slug, node, dates,
streams, roster, ids") omits all of those. If "technical-details header" means the existing YAML
front matter, this is a non-issue; if it means a rendered header block replacing it, every parser in
two kits breaks. **State which.**

### N4 — "roster" is a three-way collision in this repo's own vocabulary

The word already means three different things:
1. front-matter `roster:` = the id **FAMILY** set, validated against `FAMILIES`
   (`gen_build_index.py:574-576`); `dUnstalledConvoy` declares `roster: TOOL+PLAY`.
2. `build["roster"]` in code and the `ids` line = the derived id **reservation** set.
3. "the authored roster" in READMEs and `BUILD-METHOD.md` M2 = the **units table**.

`aRuledFrontispiece/README.md:73` states the collision head-on: "This table is the roster; the `ids:`
key above is not." Whatever the template calls its slots, it must not reuse this word for two of
them.

---

## DISSOLVED (4)

### D1 — "the owner asks for 'roster' twice"

**Dissolved.** He asks for two different populations, and the code says so in two places.

`gen_build_index.py:615-618`:

> `unit(s)` and `ids` answer DIFFERENT questions and are deliberately not reconciled: a unit is a
> spec carrying a status header, a roster member is an id that exists in the record. **aUnmannedHelm
> is 7 and 10 because three of its ids never got a spec.** Rendering them as one number would
> re-create, inverted, the defect this derivation removes.

`gen_build_index.py:311-315` (`spec_ids` docstring):

> Deliberately NOT the build README `ids:` roster. That roster is a reservation RANGE generated from
> citations anywhere, and it admits backlog and decision rows as if they were units — **measured on
> this corpus, two thirds of its ids had no spec at all.**

So the header `ids` line is the id reservation (a superset, two-thirds of it non-units) and the table
is the unit set. Both must exist. `TOOL-aMouldedFolio-2` S4 ratified rendering the FULL roster in the
README and only its COUNT in `LIVE.md` and the ledger, and the wrap at 300 chars
(`gen_build_index.py:686-698`) is deliberately one tier below the 350 cap because `length()` in the
entry-budget awk is locale-dependent. Do not "tidy" the `ids` line into a count — that reverses a
recorded decision and reintroduces the aUnmannedHelm 7-vs-10 confusion.

The residual is naming, not substance: see N4.

### D2 — "DERIVED/COMPUTED first contradicts the charter's derive-over-author rule"

**Dissolved — it IS the rule, verbatim.** `TOOL-aMouldedFolio-1`, restated in
`memory/builds/aRuledFrontispiece/spec/2026-08-16-spec-TOOL-aRuledFrontispiece-3.md:87-102`:

> Its operative rule … is that where content is derivable it must be GENERATED, because that
> converts a truth question into a **freshness question the gates can answer**. …
> The parent set is NOT derivable … So the choice here is **authored-or-absent, not
> authored-or-derived**, and the trade the refusal rejected — keep the authored value AND bolt a
> validator onto it — has no derived alternative it is losing to.

So an authored non-derivable slot does not violate the rule. The proposal is aligned with the
ratified decision, not against it. **But see D3 for what the rule's REASON costs slots 4 and 5.**

### D3 — "improvements and detriments are the least derivable content imaginable, so they rot"

**Partly dissolved, and the surviving half has a measured 88% failure rate — read this one.**

They cannot rot as *predictions*, because a dated prediction is a claim about the past. They rot the
moment anyone edits them, because an edited prediction becomes a claim about the present. That is the
whole distinction, and the repo has measured what happens when a kickoff prediction is left in place
and never revisited.

`tools/memory-tree/gen_build_index.py:585-587`:

> Which record folders this build actually HAS. **Authored as prose in 17 READMEs and wrong in 15 of
> them**: the sentence is written when a build opens, predicting the folders it will grow, and
> nothing revisits it. Seven claim a `build/` that was never created.

That sentence had every property the proposal wants for slots 4 and 5: short, authored once at
kickoff, never re-authored. **88% wrong.** The repo's response was to derive it (`kinds` at
`gen_build_index.py:588-590`) and to build `strip_records_sentence` (`:788+`) to delete the authored
copies — sentence-scoped and fence-aware, because the first cut corrupted a README that quoted the
boilerplate.

`memory/gotchas/two-answers-to-one-question.md` names the general form and its fix: "Where the
correction is prose rather than a value, **replace the copy with a pointer**: the copy that does not
exist cannot be half-fixed."

**The phrasing rule that keeps slots 4 and 5 un-rottable** — three constraints, all mechanically
checkable:
1. **Past tense, dated, at kickoff.** "On 2026-08-24 this build expected to …" A reader can then
   grade the prediction rather than trust it.
2. **No backticked mechanism token.** Run the drift signal's `_MECH_RE`
   (`tools/drift-audit/drift_report.py`) as a REFUSAL over these slots. That is the empirical
   boundary M2 established: 19 of 19 drift rows carry one, and the drift-free problem statements
   carry none.
3. **Immutable, like the description.** An edited improvement list is a status claim, and status is
   derived in this tree or it is nothing. If the expectation turns out wrong, that belongs in the M9
   wrap-up and in the spec, never as a silent rewrite of the kickoff slot.

Without all three, slot 4 is the `Records live under …` sentence with a new name, and that sentence
was wrong in 15 of 17 carriers.

### D4 — "the record links in build/ and reviews/ are load-bearing for a gate"

**Dissolved.** No gate leg and no DoD item reads them. `tools/gate-legs.json` carries exactly one
build-README leg ("build README slot contract", `--check-format`, unguarded, `subject: repo`); check
2 of `check-memory-hygiene.sh` resolves generated links but does not require the table; unattended
check 21 (`check-unattended.sh:1658-1687`) requires exactly one well-formed `gen:build-units` pair
and says nothing about records; `build-complete` reads only that units region. The table is
advisory. See M5 for what to do with it.

---

## What the proposal has missed entirely

1. **The corpus surgery is not scoped.** aRuledFrontispiece's `TOOL-aRuledFrontispiece-11` needed a
   dedicated unit and a per-file record to relocate authored prose in a *double-digit* number of
   READMEs (`aRuledFrontispiece/README.md:188-196`: "conforming the corpus means MOVING authored
   sections … which no `--check` output can review and which belongs to other nodes' build records").
   This proposal moves prose in **61** files across four nodes' records. The owner should expect
   that unit to exist and to be reviewed as a diff, not as `--check` output.
2. **The empty regions are pure noise in the entry point.** 61 of 61 READMEs carry an empty
   `gen:build-order` and an empty `gen:build-edges` — roughly 6 lines each, ~370 lines of "this build
   declares nothing" in a corpus of 8554. If the order verb is not being made mandatory in this same
   change, the honest move is to render nothing rather than a sentence saying nothing.
3. **No gate can enforce "irrelevant prose".** A heading canon bounds WHERE prose sits and WHAT it is
   called; it cannot bound whether the prose under a legal heading is relevant. Charter §7's rule
   applies to the new gate on day one: state in its header that it checks the heading set and the
   slot order, and does **not** check content. Otherwise the next owner reads a green
   "build README template" leg and assumes the problem is solved — which is precisely what happened
   with the leg in M6.
4. **A new gate needs its failing case observed before it lands** (charter §7, and
   `dUnstalledConvoy/README.md:170-174` makes it a build-level rule with a scope item and a criterion
   that greps for it). Every slot's refusal — missing, out of order, duplicated, over-cap, empty
   where required — needs a staged red.
