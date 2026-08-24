---
slug: dScaffoldedMirror
node: d
opened: 2026-08-24
streams: tooling
roster: TOOL
ids: TOOL-dScaffoldedMirror-1 TOOL-dScaffoldedMirror-2 TOOL-dScaffoldedMirror-3 TOOL-dScaffoldedMirror-4 TOOL-dScaffoldedMirror-5 TOOL-dScaffoldedMirror-6 TOOL-dScaffoldedMirror-7 TOOL-dScaffoldedMirror-8 TOOL-dScaffoldedMirror-9 TOOL-dScaffoldedMirror-10 TOOL-dScaffoldedMirror-11 TOOL-dScaffoldedMirror-12 TOOL-dScaffoldedMirror-13 TOOL-dScaffoldedMirror-14 TOOL-dScaffoldedMirror-15 TOOL-dScaffoldedMirror-16 TOOL-dScaffoldedMirror-17 TOOL-dScaffoldedMirror-18 TOOL-dScaffoldedMirror-19
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

**The single root cause of the useless half is one property in two places.** Every standard in the
kit is derived from the corpus it grades, pointing the same direction the corpus points.
`--scaffold` ranks the corpus's own leading tokens and adopts the top rows as an ALLOWLIST, so a repo
that consistently does the wrong thing legalises it; `scaffold_lexicon.py:105-107` then writes the
ceiling from that same corpus, two thirds of it as hardcoded `"0"` literals under a comment claiming
all three are MEASURED. When the corpus grows, the ceiling is raised. No exogenous reference exists
anywhere in the design.

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

## Phases

`build/2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md` carries the full diagnosis, the eleven ranked
recommendations, what was killed in review and why, and the exit criteria per phase. It is the
contract for the unit set below and is not restated here.

- **Phase 0 — honesty.** `-2` through `-7`. The kit stops lying about what it measured. Nothing about
  the vocabulary changes and the pin still exists. Ship this even if every later phase is refused.
- **Phase 1 — supply.** `-10`. The mechanism with the only measured record gets a machine holding it
  in front of the author instead of relying on a session happening to open the conf.
- **Phase 2 — the canon and the probe.** `-8`. Deletes `--scaffold`'s frequency allowlist, which
  retires `-1` by removing its subject rather than patching that write path a fourth time.
- **Phase 3 — extraction.** `-11`, blocked on a kit-owned structural exemption class.
- **Phase 4 — pressure.** `-9`. Replaces all three pins with a grandfather set whose every member
  must be derivable as an offender at a frozen sha.
- **Phase 5 — research.** `-12`, only if the owner wants it.

Off-phase: `-13` (the `.ts`/`.tsx` darkness), `-14` (the renames), `-15` (wiring the runbook-parity
gate that currently tells no adopter this kit exists).

<!-- gen:build-index -->
**Build status:** SPECCED · 1 unit(s) · node d · opened 2026-08-24 · streams tooling
ids TOOL-dScaffoldedMirror-1 TOOL-dScaffoldedMirror-2 TOOL-dScaffoldedMirror-3 TOOL-dScaffoldedMirror-4 TOOL-dScaffoldedMirror-5 TOOL-dScaffoldedMirror-6 TOOL-dScaffoldedMirror-7 TOOL-dScaffoldedMirror-8 TOOL-dScaffoldedMirror-9 TOOL-dScaffoldedMirror-10 TOOL-dScaffoldedMirror-11
ids TOOL-dScaffoldedMirror-12 TOOL-dScaffoldedMirror-13 TOOL-dScaffoldedMirror-14 TOOL-dScaffoldedMirror-15 TOOL-dScaffoldedMirror-16 TOOL-dScaffoldedMirror-17 TOOL-dScaffoldedMirror-18 TOOL-dScaffoldedMirror-19

<!-- gen:build-units -->
| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-dScaffoldedMirror-2 — honest reporting and per-predicate liveness](spec/2026-08-24-spec-dScaffoldedMirror-2.md) | SPECCED | rev-1 | 2026-08-24 |
<!-- /gen:build-units -->

Records live under `spec/` and `build/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md](build/2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md) | research | TOOL-dScaffoldedMirror-2 |

Ids no `spec-audit` record has ever named: TOOL-dScaffoldedMirror-2.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-24-spec-dScaffoldedMirror-2.md](spec/2026-08-24-spec-dScaffoldedMirror-2.md)
- **`build/`**
  - [2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md](build/2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md)
<!-- /gen:build-docs -->
