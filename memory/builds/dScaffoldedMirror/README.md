---
slug: dScaffoldedMirror
node: d
opened: 2026-08-24
streams: tooling
roster: TOOL
ids: TOOL-dScaffoldedMirror-1 TOOL-dScaffoldedMirror-2 TOOL-dScaffoldedMirror-3 TOOL-dScaffoldedMirror-4 TOOL-dScaffoldedMirror-5 TOOL-dScaffoldedMirror-6 TOOL-dScaffoldedMirror-7 TOOL-dScaffoldedMirror-8 TOOL-dScaffoldedMirror-9 TOOL-dScaffoldedMirror-10 TOOL-dScaffoldedMirror-11 TOOL-dScaffoldedMirror-12 TOOL-dScaffoldedMirror-13 TOOL-dScaffoldedMirror-14 TOOL-dScaffoldedMirror-15 TOOL-dScaffoldedMirror-16 TOOL-dScaffoldedMirror-17 TOOL-dScaffoldedMirror-18 TOOL-dScaffoldedMirror-19 TOOL-dScaffoldedMirror-20
---

# dScaffoldedMirror — the lexicon kit stops deriving its standard from the code it grades

Node `d` · opened 2026-08-24 · stream tooling.

Commissioned when the owner ran `adopt-lexicon.sh --scaffold` on a fresh repo and watched every
deliberately-bad name pass green. The demo is the whole diagnosis in one run: the scaffold derived a
25-verb table from the corpus, reported `VERB_OFFENDER_PIN=5`, and all five offenders were in the
vendored kit's own files. `do_thing`, `is_ready`, `get_record`, `fetch_remote`, `validate_order` and
`calculate_total` were legal, because the frequency count had promoted `do`, `is`, `get`, `fetch`,
`validate` and `calculate` into the vocabulary on the strength of those very names. Replacing the
seed with twelve curated rows moved the pin 5 → 22.

## The finding that reframes the build

**The kit is already half-working, and it is not the half anyone was watching.** Since
`.lexicon.conf` landed on 2026-08-16 this repo added **136 definitions and zero offenders** — their
leading tokens are exactly the declared table, and a whole new JavaScript hook was written end to end
in the vocabulary. Over the same window the gate refused nothing: three firings in its life, three
pin raises (412 → 415 → 417 → 463), and exactly one offender key ever leaving the set, by a
de-duplication rather than a rename.

So the DECLARATION constrains the generations and the ENFORCEMENT has a measured contribution of
zero. That ordering decides the phase order: supply before pressure, and honesty before both.

**The single root cause of the useless half WAS one property in two places** — past tense, and the
tense is the point: this paragraph is the diagnosis this build opened with, kept because the record
of what was wrong is worth more than a description of what is now right. It stood in the present
tense until the round-2 review reported it, along with a `scaffold_lexicon.py:105-107` pointer that
had come to name the replacement rather than the defect.

Every standard in the kit was derived from the corpus it graded, pointing the same direction the
corpus pointed. `--scaffold` ranked the corpus's own leading tokens and adopted the top rows as an
ALLOWLIST, so a repo that consistently did the wrong thing legalised it; the scaffold then wrote the
ceiling from that same corpus, two thirds of it as hardcoded `"0"` literals under a comment claiming
all three were MEASURED. When the corpus grew, the ceiling rose with it. No exogenous reference
existed anywhere in the design. `TOOL-dScaffoldedMirror-8` supplied one — `tools/lexicon/canon.py`,
whose clusters are frozen and whose element 0 is the representative unconditionally — and
`TOOL-dScaffoldedMirror-1` closed by deleting the ranking rather than by tuning it.

## The adopter probe, and why its numbers are not the research pass's numbers

The research pass estimated adopter scale by re-implementing the kit's predicates. That estimate was
run again on 2026-08-24 with the kit's OWN extractor against `C:/projects/incms/main`, read-only,
7.8 s, writing nothing to that repo (the probe script is folded into that record as an appendix). Two of the three headline
estimates held and one was wrong by eighty-fold:

| | research estimate | measured by the kit's extractor |
|---|---|---|
| P1 offenders | 6,482 | **6,566** (44.8% of 14,659 graded) |
| P2 offenders | 484 | **6** |
| extensions present | 44 | 44, of which **31 undeclared** |
| unparseable under `parser` | — | **0** |

Three results move the plan. Armed coverage on incms is **19.3%** — 1,190 of 6,168 tracked files —
because the kit has no pattern set for `.ts` (626 files) or `.tsx` (572), so the adopter's primary
language is invisible to it; that is a bigger hole than this repo's own dark `.sh` population and it
is filed as `TOOL-dScaffoldedMirror-13`. P2 is essentially clean on a real adopter at six offenders,
which retires the research pass's proposal to replace it with a nineteen-row blocklist. And **55.2%
of incms's definitions already lead with a verb from this repo's table**, with nobody there having
seen it — which is the strongest available evidence for a SHIPPED canon over a derived one, because
it says the useful vocabulary is largely universal and the 1,458 distinct off-table leading tokens
are what an absent convention looks like rather than a different one.

## The owner rulings this build is built on

Four forks were put to the owner on 2026-08-24 and all four resolved. They are recorded as
`TOOL-dScaffoldedMirror-16` through `-19` in `memory/DECISIONS.md`, because two of them SUPERSEDE
ratified records from `dClosedLexicon` and a supersession that lives only in a build README is a
supersession nobody will find.

Two further rulings were taken by the agent on a stated default with the owner declining to override:
the `t_`/`do_`/`cmd_` renames (`-14`), and forbidding freeze advancement in v1, which is carried in
`-9`'s spec rather than as its own decision because it is a property of that one mechanism.

## The plan, after the spec set was reviewed and cut

Thirteen units were specced, then reviewed as a set. They converge mechanically — all fourteen specs
pass every machine-checked mechanic — but the review's plan-level verdict was that **the plan did not
follow from its own diagnosis**, and the owner ruled on it the same day.

The diagnosis said *the gate is the half with the zero; do not respond to "it shipped worthless" by
building more gate.* The thirteen-unit plan then spent roughly 1,000 of its ~2,000 estimated lines on
gate machinery and scheduled `-10`, the one mechanism with a measured record, seventh. It also grew
the pin count 3 → 5 across Phases 0–3, two phases before `-9` deletes three, in a build whose thesis
is that the raisable ceiling is the defect.

**The ruling: six units build now, and `-9` becomes a SEVENTH item gated on evidence rather than the
terminus of a five-phase chain nobody can stop.**

| status | units | outcome |
|---|---|---|
| **CLOSED — built** | `-2` `-6` `-7` `-8` `-10` `-14` | All six. No new pin, no conf scalar, no receipt reader, no backfill, no freeze, no runbook — and `VERB_OFFENDER_PIN` never rose once, falling 463 → 384 by RENAMING. |
| **DEFERRED** | `-4` `-9` `-11` `-12` `-13` `-15` | Parked behind the two measurements this plan takes and never consults. Both now exist. |
| **WONTDO** | `-3` `-5` | Cut. Each spec's own section 9 carries the killing argument. |

`TOOL-dScaffoldedMirror-1`, the defect that opened this build, is CLOSED — retired by `-8` deleting
its subject rather than patching that write path a fourth time.

## What shipped, and the one number that decides what happens next

**The demo that opened this build passes.** The owner's original fixture, re-scaffolded after `-8`:
all six deliberately-bad names are offenders where all six passed green.

**The kit no longer derives its standard from the corpus it grades.** `canon.py` is frozen, shipped,
and an adopter cannot edit it; the corpus decides which CONCEPTS appear and never what they are
CALLED. The polarity arm is the proof — a corpus of `get_*` and `fetch_*` with no `load` anywhere
proposes `read` and `load`, the two spellings it does not use.

**And the enforcement half now has a standing measurement.** `build_lexicon_marginal_offense_rate`
read **4.3% in files written FRESH** in its window on its first run. `-7`'s docstring carries the
kill rule: at or below roughly 5% across two further readings, the pressure chain — `-4`, `-9`, and
`-11`'s cut fourth pin — should be ABANDONED rather than deferred. **That is reading one of two.**
A second reading is owed before anyone acts, and this build deliberately took none of the pressure
work while the question is open.

**The stop rule this build did not have.** After the six land: read `-7`'s first standing measurement,
and run `--probe` read-only against `C:/projects/incms/main`. Those are the two measurements the
original plan produced and then never made anything depend on. The pressure chain — `-4`, `-9`, and
`-11`'s cut fourth pin — is decided with them in hand, not before.

Every SPECCED unit owes a rev-2 scope pass before building; the cuts and corrections are recorded in
each one's section 9, and the full argument is in the review record under `build/`.

**What the review says this build still does not deliver**, stated here rather than discovered later.
Demand 1 arrives Python-only over reach ≥ 2, so 71.5% of variable bindings are refused by design, and
on the one adopter `.ts`/`.tsx` are dark. Demand 2 rides entirely on the deferred `-9`. Demand 3's
probe ships and **the adopter population is still zero when the build ends** — no unit in this set
installs the kit anywhere, and every unit raises the price of adopting it, in a build commissioned
because nobody adopts it. That last one is the largest unaddressed risk in the set and it has no
owner yet.

<!-- gen:build-index -->
**Build status:** DEFERRED · 14 unit(s) · node d · opened 2026-08-24 · streams tooling
ids TOOL-dScaffoldedMirror-1 TOOL-dScaffoldedMirror-2 TOOL-dScaffoldedMirror-3 TOOL-dScaffoldedMirror-4 TOOL-dScaffoldedMirror-5 TOOL-dScaffoldedMirror-6 TOOL-dScaffoldedMirror-7 TOOL-dScaffoldedMirror-8 TOOL-dScaffoldedMirror-9 TOOL-dScaffoldedMirror-10 TOOL-dScaffoldedMirror-11
ids TOOL-dScaffoldedMirror-12 TOOL-dScaffoldedMirror-13 TOOL-dScaffoldedMirror-14 TOOL-dScaffoldedMirror-15 TOOL-dScaffoldedMirror-16 TOOL-dScaffoldedMirror-17 TOOL-dScaffoldedMirror-18 TOOL-dScaffoldedMirror-19 TOOL-dScaffoldedMirror-20

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dScaffoldedMirror-10 — supply the vocabulary to the author](spec/2026-08-24-spec-dScaffoldedMirror-10.md) | — | 2 | CLOSED | rev-5 | 2026-08-25 |
| [TOOL-dScaffoldedMirror-11 — the scoped extractor, and the one predicate it makes possible](spec/2026-08-24-spec-dScaffoldedMirror-11.md) | — | 2 | DEFERRED | rev-1 | 2026-08-24 |
| [TOOL-dScaffoldedMirror-12 — the consistency instrument, measured before it is believed](spec/2026-08-24-spec-dScaffoldedMirror-12.md) | — | 1 | DEFERRED | rev-1 | 2026-08-24 |
| [TOOL-dScaffoldedMirror-13 — the .ts/.tsx darkness, decided rather than inherited](spec/2026-08-24-spec-dScaffoldedMirror-13.md) | — | 1 | DEFERRED | rev-1 | 2026-08-24 |
| [TOOL-dScaffoldedMirror-14 — the `t_` and `do_` renames, and `cmd` as a reserved row](spec/2026-08-24-spec-dScaffoldedMirror-14.md) | — | 1 | CLOSED | rev-2 | 2026-08-25 |
| [TOOL-dScaffoldedMirror-15 — wire the runbook-parity gate, and pay what wiring it costs](spec/2026-08-24-spec-dScaffoldedMirror-15.md) | — | 1 | DEFERRED | rev-1 | 2026-08-24 |
| [TOOL-dScaffoldedMirror-2 — honest reporting and per-predicate liveness](spec/2026-08-24-spec-dScaffoldedMirror-2.md) | — | 1 | CLOSED | rev-3 | 2026-08-25 |
| [TOOL-dScaffoldedMirror-3 — corpus scoping derived from the install receipt](spec/2026-08-24-spec-dScaffoldedMirror-3.md) | — | 1 | WONTDO | rev-1 | 2026-08-24 |
| [TOOL-dScaffoldedMirror-4 — waiver keying and the mandatory reason](spec/2026-08-24-spec-dScaffoldedMirror-4.md) | — | 1 | DEFERRED | rev-1 | 2026-08-24 |
| [TOOL-dScaffoldedMirror-5 — the three RATCHETS rows and the delete-then-re-add repair](spec/2026-08-24-spec-dScaffoldedMirror-5.md) | — | 1 | WONTDO | rev-1 | 2026-08-24 |
| [TOOL-dScaffoldedMirror-6 — the coverage floor and the LANGS mode ratchet](spec/2026-08-24-spec-dScaffoldedMirror-6.md) | — | 1 | CLOSED | rev-4 | 2026-08-25 |
| [TOOL-dScaffoldedMirror-7 — the marginal-offense-rate signal](spec/2026-08-24-spec-dScaffoldedMirror-7.md) | — | 1 | CLOSED | rev-4 | 2026-08-25 |
| [TOOL-dScaffoldedMirror-8 — the shipped frozen canon, and `--probe`](spec/2026-08-24-spec-dScaffoldedMirror-8.md) | — | 2 | CLOSED | rev-3 | 2026-08-25 |
| [TOOL-dScaffoldedMirror-9 — the grandfather set with a provenance assert, replacing all three pins](spec/2026-08-24-spec-dScaffoldedMirror-9.md) | — | 2 | DEFERRED | rev-1 | 2026-08-24 |
<!-- /gen:build-units -->

Records: 10 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->