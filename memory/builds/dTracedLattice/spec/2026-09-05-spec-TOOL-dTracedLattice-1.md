# TOOL-dTracedLattice-1 — fan-in stops counting homonyms and stops discarding real dotted references

**Status:** SPECCED · rev-3 · 2026-09-05 · node d · Tier-2 · base c4fcf5ad · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md) | research | TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 |
| [2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round1.md) | spec-audit | TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 |
| [2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round2.md) | spec-audit | TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 |

<!-- /gen:spec-records -->

## 1. Goal

Raise the precision of `map_lib.fan_in` so that `reuse_lookup`'s ranked output is worth the mandate
that makes reading it compulsory. Measured against AST-resolved import edges, the shipped heuristic
scores 14.5% precision overall and 7.2% in the fan-in band that `reuse_lookup` prints first.

## 2. Scope (IN)

- **S1** Subtract same-name definers in `fan_in`: the referencing-file set loses every file that also
  DEFINES the symbol, not only the one definition file passed as `def_file`. The caller already holds
  `symbols.json` and can supply the definer set.
- **S2** Add a receiver-binding pass so a dotted occurrence counts when its receiver binds to a repo
  module. `import map_lib as m` followed by `m.fan_in(...)` is a real reference and the current index
  cannot distinguish it from `Path(p).read_text()`.
- **S3** Report the index's own coverage on every call: how many attribute sites were bound, how many
  were left unresolved, and which language layers were not scanned at all.
- **S4** Re-declare the wall-clock ceiling for every entrypoint whose cost moves, with the reading
  that justifies it.
- **S5** Amend `TOOL-aScouredKit-16` in place with the measurement that rejects its second proposal,
  so the row is not later built as written. This unit is the ONLY one that edits that row, and it
  therefore carries `TOOL-dTracedLattice-3` S3's three corrections as well: the reinvention backlog
  is NOT tracked, the fiction is NOT permanent, and it does NOT ship to adopters. All three clauses
  are live at `memory/backlog/TOOL.md:294`, and `git ls-files | grep reinvention` returns nothing,
  so two of them are checkably false today. Rev-2 declared the sole-editor rule and did not widen
  this item to receive what the other unit stopped doing, which left the corrections owned by nobody.
- **S6** Land the scoring instrument as tracked files under `tools/codebase-map/`: the AST
  ground-truth resolver and the variant harness that AC1 and AC2 are scored by, plus the ground-truth
  corpus as a FIXTURE rather than as a remembered number. Both exist today only in a scratchpad this
  build's README already records as unreproducible, so without this item the unit's headline criteria
  can be satisfied only by assertion.
- **S7** Update `tools/codebase-map/map_diff.py`, which calls `fan_in` at line 204 and computes the
  dead-export figure at 207. It is in this unit's write set, not unit 3's, because the signature S1
  changes is the one that line passes.
- **S8** Re-derive `SEAM_FANIN_THRESHOLD` against the new metric, or record with the measurement that
  `3` still means what it meant. Definer subtraction rescales the seam population for all three
  consumers, and a tuned adopter value does not travel with this fix.

## 3. Non-goals (OUT)

- No committed relation artifact. That question is answered in this build's README on `AGENTS.md` §12
  grounds, and reversing it is not this unit's business.
- No change to `symbols.json`, its schema, or the freshness gate — `TOOL-dTracedLattice-2` owns the
  gate.
- No type inference. A receiver that cannot be bound by import analysis alone stays unresolved and is
  REPORTED as unresolved.
- No re-basing of `dead_exports`; that population changes as a consequence and its repair is a
  follow-up, named in §8.

## 4. Design

### Data model

`build_reference_index` gains a per-file record of whether each occurrence was bare or attribute-form,
and for attribute form, the receiver name. A second pass resolves receiver names to repo modules using
the import statements already parseable with `ast`. `fan_in` then takes a definer set rather than a
single `def_file`.

`fan_in` has FOUR PRODUCTION call sites across THREE files: `map_diff.py:204`, `map_lib.py:1240`,
and `reuse_lookup.py:264` and `:274`. `selftest.py` holds five more, at `:898` through `:901` and
`:936`. Each production site must supply the definer set.

`map_lib.py:1240` is the hard case and rev-2's enumeration omitted it while the sentence beside it
called `detect_collisions` "the hard case" — naming a problem and not locating it. That call sits
INSIDE `detect_collisions`, which sees only the union of base and new rows and never the head symbol
table, so it cannot build a head definer set itself. It is therefore given one by its caller; keeping
the old signature there behind a compatibility path is rejected, because a silent fallback to the old
behaviour at one call site is exactly how a precision fix half-lands — which is what rev-2's own
omission would have caused.

### Alternatives rejected

`TOOL-aScouredKit-16` proposes discarding dotted occurrences outright. **Measured, that is harmful:**
scored against 329 AST-verified edges over 127 rows, the bare-only variant scores 4.9% precision and
25.2% recall against the shipped 14.5% and 100%, and combined with S1 it scores 11.2% and 8.1%. It
discards 198 of 211 verified edges because this repo's dominant idiom is aliased-module dotted calls.
S1 alone scores 33.8% precision at 82.9% recall and 0.46 mean absolute error against the shipped 1.38.
S1 plus S2 is the design; S1 alone is the fallback if S2 does not pay for its cost.

### Rollout

S1 first and alone, because it is the measured floor and needs no new pass. S2 behind the same
entrypoint, landing dark in the sense that it can be disabled to recover S1-only behaviour.

## 5. Production-readiness checklist

- security — N/A, no new input surface; the scan reads tracked source it already reads.
- perf / scale — the receiver-binding pass measured a median 1.761 s against `build_reference_index`'s
  0.595 s, taking the on-demand path to roughly 2.4 s. S4 owns the re-declaration.
- a11y — N/A, a CLI.
- i18n — N/A.
- error / empty / loading states — an unparseable file is skipped fail-open, as today, because this
  feeds a ranking and not a gate. The skip is counted and reported by S3.
- observability — S3 is the observability item.
- risks — the fan-in-0 population grows, so `dead_exports` inflates; §8 carries the disposition.
- testing + left-shift gates — arms in `tools/codebase-map/selftest.py`, each observed RED first.
- migration / rollback — no committed artifact moves, so rollback is reverting the functions.
- user docs — `tools/codebase-map/README.md` and `reuse-lookup.agent.md` state what the ranking means.

## 6. Acceptance criteria

- **AC1** — When the harness S6 lands is run over the fixture corpus S6 pins, `fan_in` with S1 scores
  at least `33.8%` precision at no less than `82.9%` recall, against the shipped `14.5%` / `100%`.
  Both the harness and the corpus are tracked paths named in S6, so the criterion is scorable by
  something in the tree.
- **AC2** — When mean absolute error is scored by that same tracked harness, S1 reports at most `0.46`
  against the shipped `1.38`.
- **AC3** — When `python tools/codebase-map/reuse_lookup.py` is run on any query, its output names the
  count of bound and unresolved attribute sites and every unscanned layer, so a reader can tell a
  thin answer from a confident one.
- **AC4** — When a symbol defined in more than one file is ranked, its fan-in counts only files that
  do not themselves define it; `load_conf`, defined in nine files, drops from `18` to its
  definer-subtracted value.
- **AC5** — When the dot-prefix-only variant is requested, `tools/codebase-map/selftest.py` fails,
  because an arm pins the measurement that rejects it.
- **AC6** — When `memory/backlog/TOOL.md` is read, `TOOL-aScouredKit-16` carries the amendment naming
  the rejected half and the measurement that rejected it, AND no longer claims the reinvention
  backlog is tracked, that the fiction is permanent, or that it ships to adopters — the three
  corrections `TOOL-dTracedLattice-3` S3 supplies and this unit applies.
- **AC9** — When S8 lands, the seam threshold is either re-derived with the reading that justifies the
  new value, or `.codebase-map.conf`'s `SEAM_FANIN_THRESHOLD` comment records the measurement showing
  `3` still means what it meant. AC7's fixture pin is a regression guard at a FIXED threshold and
  cannot grade this, so without AC9 the whole of S8 could be skipped with AC7 green.
- **AC7** — When `seed_affordances` is run on the fixture corpus at threshold `3` before and after S1,
  the seam population is pinned at both readings, so any later change to `fan_in` that moves the seam
  set reds rather than drifting.
- **AC8** — When `python tools/codebase-map/map_diff.py --converge` runs after S7, its dead-export
  figure reports the new population beside the old, so the movement is attributable.

## 7. Gates

`codebase-map kit selftest` · `codebase-map coverage + freshness` · `memory hygiene` ·
`harness arms (fail branches armed or pinned)`. No new leg: the arms join the kit's existing selftest.

Both `codebase-map kit selftest` and `codebase-map coverage + freshness` are kit-subject legs and are HELD on a plain bar; a builder verifying this unit needs `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`. The runner names every held leg, so they are announced rather than silent.

## 8. Open questions

- **Q1 — the `dead_exports` disposition.** S1 grows the fan-in-0 population from 451 to 532, and the
  hint is already weak: it is a bare scalar with no list, and its 451 rows are dominated by 120
  selftest definitions, 13 name-dispatched `cmd_*` handlers and a block of module-private dataclasses
  that read dead only because `fan_in` subtracts the definition file. **The follow-up already exists:**
  `TOOL-aScouredKit-17` owns the dead-export disposition and says it should land with `-16`, the row
  S5 amends. Its `412` was measured at `093730e4` and reads `451` at `c4fcf5ad`, so its next reader is
  not comparing two trees. RESOLVED (agent, 2026-09-05): the disposition belongs to
  `TOOL-aScouredKit-17`; this unit reports the movement per AC8 and declines the co-landing, because
  narrowing the population is a second mechanism and M2 forbids two mechanisms in one spec.
- **Q2 — whether S2 pays for its cost.** FACT-QUESTION · the probe is the precision harness of AC1 run
  with and without S2, and the observation that decides it is whether S2's precision exceeds S1's by
  more than the ratio its wall clock grows. LIVENESS: the harness already distinguishes four variants
  at four different scores, so it can return a negative. RESOLVED (agent, 2026-09-05, delegated): the
  probe runs before S2 lands and S1 ships regardless.

## 9. Revision log

- rev-1 · 2026-09-05 · initial draft, from the dTracedLattice design pass and its skeptic round.
- rev-3 · 2026-09-05 · folded the round-2 spec audit: B1 (S5 and AC6 widened to RECEIVE the three
  corrections unit 3 S3 hands over — rev-2 declared the sole-editor rule and left them owned by
  nobody), B2 (§4's call-site list was false in both directions and omitted `map_lib.py:1240`, the
  very call it called the hard case), H1 (AC9 grades S8, which AC7 could not), M1 (§7 discloses that
  the kit legs are held).
- rev-2 · 2026-09-05 · folded the round-1 spec audit: B2 (S6 lands the scoring instrument AC1 and AC2
  are scored by), H1 (§4 names `fan_in`'s four call sites and the `detect_collisions` case), H6 (§8 Q1
  cites `TOOL-aScouredKit-17`), H7 (S8 re-derives `SEAM_FANIN_THRESHOLD`, AC7 pins the seam
  population), and B1's reassignment of `map_diff.py` into this unit's write set as S7 with AC8.

## 10. Reuse audit

The seam this unit extends is `map_lib.fan_in` together with `map_lib.build_reference_index`, cited
from `python tools/codebase-map/reuse_lookup.py "derive relations between symbols and expose them to
the orientation tools"`, which returns `render_symbols_json` (`tools/codebase-map/map_lib.py`,
fan-in 4, SEAM) at rank two and no seam for the reference index itself — a result this unit's own
subject explains, since the ranking that produced it is the thing being repaired. `resolve_import` in
`tools/lexicon/lexicon.py` already performs AST import resolution and is the prior art for S2, but it
is SPECCED for deletion by `TOOL-aSurfacedLexicon-2` at order 1, so it is prior art rather than a seam
to wire through.

Recall terms used: codebase-map relations fan-in reference index symbols dossier reuse_lookup
memory-recall corpus retrieval seam affordance converge
