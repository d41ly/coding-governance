# TOOL-dFramedEntrypoint-1 — the build README's authored half becomes a closed heading canon

**Status:** CLOSED · rev-6 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · order 2 · streams tooling · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-TOOL-dFramedEntrypoint-1-acceptance.md](../build/2026-08-24-build-TOOL-dFramedEntrypoint-1-acceptance.md) | journal | — |
| [2026-08-24-build-TOOL-dFramedEntrypoint-1-contradictions.md](../build/2026-08-24-build-TOOL-dFramedEntrypoint-1-contradictions.md) | research | — |
| [2026-08-24-build-TOOL-dFramedEntrypoint-1-corpus-census.md](../build/2026-08-24-build-TOOL-dFramedEntrypoint-1-corpus-census.md) | research | — |
| [2026-08-24-build-TOOL-dFramedEntrypoint-1-derivation.md](../build/2026-08-24-build-TOOL-dFramedEntrypoint-1-derivation.md) | research | — |
| [2026-08-24-build-TOOL-dFramedEntrypoint-1-enforcement.md](../build/2026-08-24-build-TOOL-dFramedEntrypoint-1-enforcement.md) | research | — |
| [2026-08-24-build-TOOL-dFramedEntrypoint-1-migration.md](../build/2026-08-24-build-TOOL-dFramedEntrypoint-1-migration.md) | research | — |
| [2026-08-24-build-TOOL-dFramedEntrypoint-1-owner-rulings.md](../build/2026-08-24-build-TOOL-dFramedEntrypoint-1-owner-rulings.md) | journal | — |
| [2026-08-24-review-TOOL-dFramedEntrypoint-1-claim-verification.md](../reviews/2026-08-24-review-TOOL-dFramedEntrypoint-1-claim-verification.md) | spec-audit | — |
| [2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round1.md](../reviews/2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round1.md) | spec-audit | TOOL-dFramedEntrypoint-2 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-7 TOOL-dFramedEntrypoint-8 |
| [2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round2.md](../reviews/2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round2.md) | spec-audit | TOOL-dFramedEntrypoint-2 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-7 TOOL-dFramedEntrypoint-8 |

<!-- /gen:spec-records -->

## 1. Goal

The shipped slot contract constrains only WHERE authored content sits in a build README, never WHAT
it is, so an entrypoint can carry any prose in any shape and pass. This unit gives the authored half a
CLOSED heading canon — five named slots in a fixed order — graded by the same verb and the same gate
leg that already grade position, and closes the total-exemption hole that lets a README with no
generated marker pair skip the check entirely.

## 2. Scope (IN)

- **S1** — `slot_violations` in `tools/memory-tree/gen_build_index.py` gains a THIRD trigger: the
  authored region between the title and the first generated marker must consist of exactly the
  canonical slot headings, in canonical order, with no heading outside the canon and no non-blank
  line between the title line and the first canonical heading.
- **S2** — the canon is a module-level tuple beside `GEN_REGIONS`, declaring for each slot its exact
  heading text, whether its body may be empty, and whether its body must be a bullet list.
- **S3** — the description slot is DECLARED to be the goal bound that the build method's rescope rule
  reads, rather than a sixth slot restating it. The method's pointer is updated to name the slot, so
  the two are one sentence in one place.
- **S3b** — the build method mandates two further authored README writes that the owner's fork-2
  ruling did not name: the per-unit CLASSIFICATION written before acting on it, and the review loop's
  runaway-ceiling PROMOTION notice. Both are routed explicitly to the build-level rules slot's body,
  and `tools/memory-tree/BUILD-METHOD.template.md` is edited to say so with
  `memory/guides/BUILD-METHOD.md` re-rendered from it. The canon closes the HEADING set and not slot
  bodies, so this costs no sixth slot — but leaving it unstated makes the method and the gate
  contradict each other the first time a run follows the method on a bound README.
- **S4** — the NO-MARKERS arm. `slot_violations` returns an empty list whenever it finds no registered
  region pair, so a README carrying no generated markers passes unconditionally. It must instead
  report that absence as a violation naming the file.
- **S5** — the canon applies only to files the registry of unit 3 declares. Until that unit lands, the
  predicate is written and exercised but wired to an empty declared population, and the leg says so on
  every run rather than reporting a clean count.
- **S6** — the blind-spot paragraph — what this contract does NOT check — is written into
  `gen_build_index.py`'s module docstring and `do_check_format`'s own docstring, and mirrored in the
  `build-readme-surface` dossier. NOT into `tools/gate-legs.json`: that manifest is a JSON array whose
  leg objects carry a CLOSED key set enforced by the run-gates canary, JSON carries no comments, and
  an added prose key reds the bar.
- **S7** — a `--survey` verb that runs the candidate predicate over EVERY tracked build README
  regardless of the declared population and prints hits AND near-misses without changing the exit
  code. It exists because this repo requires a new gate predicate to be run over the real tree before
  it is wired, and because `main()` silently ignores an unknown argument, so an acceptance criterion
  naming a flag that does not exist would pass by printing the ordinary clean line.
- **S8** — new `--selftest` arms covering every trigger, every refusal and the survey verb, including
  a fixture for the no-markers case that the live corpus cannot exercise.
- **S-READPATH** — S3 and S3b both grow `memory/guides/BUILD-METHOD.md`, which is one of six capped
  members of the read path check 16 grades, and the margin measures in the low tens of bytes. This
  unit therefore raises `READ_PATH_CEILING` in `.memory-tree.conf` in the SAME commit as the
  re-render, or trims a member by at least the added width, and records the pre- and post-edit margin
  from `corpus_ids.py --report`. Unit 8 raises the same ceiling for its own decision append and its
  raise is deliberately MINIMAL and sized against that one file, so it does not cover this growth —
  two units charge the same budget and each prices its own charge.
- **S-EPOCH** — this unit moves `tools/memory-tree/gen_build_index.py`, which is inside the
  verdict-epoch gate's scan set, so its landing carries a `KIT_MEMORY_TREE_VERSION` bump. The carrier
  set is DERIVED, never read off the epoch gate's remedy text: bump the constant and its inline marker
  in the engine, then every carrier `git grep -l 'gov:kit memory-tree@'` returns over tracked paths
  outside `memory/builds/` and `memory/archive/`, then re-render the live copies with
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. The remedy string names three paths and
  the parity harness three pairs; their union is five, and there are SEVEN carriers — the two it cannot
  reach are kit SOURCES rather than dogfood copies. Following the remedy exactly reds the unguarded
  `kit version markers` leg, which is `TOOL-dSettledRoster-4` in the backlog, recorded as having cost a
  full-bar cycle twice. The rule binds per PUSH RANGE, not per commit: units landing in one push need
  one correctly-placed bump, on the LAST engine-moving commit in that range. It is stated in every
  engine-moving unit rather than once, because a rule written in one spec is a rule the other seven do
  not carry.

## 3. Non-goals (OUT)

- No per-slot BYTE OR CHARACTER BUDGET. That is unit 2, separated because a shape check and a size
  check fail for different reasons and a reader must be able to tell which fired.
- No REGISTRY. That is unit 3. This unit ships only the reader for it.
- No CORPUS SURGERY. No existing build README is edited here. That is unit 7.
- No IMMUTABILITY CHECK on the description. Ruled out by the owner on measurement: 26 of the 61
  description blocks already carry more than one commit, so a history-based gate has no green starting
  state. Immutability becomes a DOCUMENTED check in the hygiene grammar.
- No change to the authored roster pair or to any reader of it. That is this build's park.
- No new gate LEG. The predicate rides the leg that already grades this file class.

## 4. Design

### Data model

The canon is a tuple of records beside `GEN_REGIONS`, each carrying the exact heading text, an
`empty_ok` flag and a `bullets` flag. Five slots, in this order:

| Slot | Body may be empty | Body shape |
|---|---|---|
| the immutable description, which IS the goal bound | no | prose |
| expected improvements | no | bullet list |
| detriments if not built | no | bullet list |
| build-level rules | yes | prose |
| parked decisions | yes | prose |

The goal bound is not a sixth entry. S3 folds it into the description, because two slots that must
agree are the two-answers-to-one-question class this tree already names.

**The authored `roster:units` pair keeps an explicit declared position**: where present, it sits
AFTER the last canonical slot and BEFORE the first generated marker, and the canon walk permits it
there rather than reporting it as content outside the canon. Its span belongs to no slot, so unit
2's last slot terminates its measured slice at that pair's opening marker rather than at the first
generated one. Without this the pair's table is billed to the parked-decisions slot, which is a
block this unit's own non-goals forbid touching. The pair's FUTURE is this build's park; its
POSITION is not, and leaving the position unstated makes an implementer guess.

### Inventory

The graded population is exactly the paths the unit-3 registry declares. This unit ships the reader as
a function returning an empty set when the registry file is absent, so the predicate is complete
before its population exists and unit 3 supplies only data.

### Migration

None, by construction: an empty declared population edits nothing and reds nothing. The leg prints the
declared count on every run, so an empty population is VISIBLE rather than silently green — which is
the failure mode a date-keyed cutoff would have shipped, because the population guard counts before
the date filter and a cutoff governing zero files reports clean.

### Alternatives rejected

**Per-slot marker pairs.** Refused in the record that shipped the position-bound contract, on the
ground that markers make every README carry two more lines to solve a problem position already solves.
That record's Alternatives-rejected section refuses TWO DIFFERENT things, and they must not be read as
two reasons for one refusal: bounding the PROSE by a marker pair, refused for the two-lines reason
above, and detecting the PLAN slot by heading text, refused because the unattended authorization
byte-compared a marker-delimited region and a heading is not a delimiter it could address. Only the
second has EXPIRED, when the frozen authorization scope moved to the generated unit-ID set. The first
still holds and is what this unit respects: the canon adds no marker pair and closes the heading set
INSIDE the position-bound block.

**Delegating the check to the hygiene shell gate.** That would put the new refusals where
`check-arms.py` can see them, which is the recorded reason hygiene check 21 keeps its refusals in
shell while delegating its parse to this same Python file. Rejected here for a different reason: this
file carries its own arm harness graded by its own selftest leg, so the branches ARE armable, and
splitting one file-class contract across two gates gives a reader two places to look. The deviation
from check 21's precedent is deliberate and recorded here rather than left to be rediscovered.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` for the canon tuple, the third trigger, the no-markers arm, the
registry reader and the selftest arms · `tools/memory-tree/HYGIENE.template.md` edited FIRST with
`memory/HYGIENE.md` re-rendered from it, because the parity harness renders the live copy from the
template and editing the pair together inverts that · `.memory-tree.conf` for the S-READPATH ceiling raise ·
`tools/memory-tree/BUILD-METHOD.template.md` edited FIRST for the S3 pointer and the S3b routing, with
`memory/guides/BUILD-METHOD.md` re-rendered from it · the `build-readme-surface` dossier, whose
`[paths]` globs already claim this module, so the new module-level functions need a dossier prose
refresh rather than a new claim. NOT `tools/gate-legs.json` — see S6.

## 5. Production-readiness checklist

- security — N/A. The predicate reads tracked markdown and writes nothing.
- perf / scale — the leg measures well under a second over the corpus; the canon walk is one more pass
  over an already-read string, so the cost is a rounding error on one of the cheapest legs on the bar.
- a11y — N/A. No user interface.
- i18n — N/A. The canon headings are repo-internal identifiers, not display strings.
- error / empty / loading states — the empty declared population is the state that matters, and S5
  makes it announce itself rather than pass silently.
- observability — the leg reports the declared count and the graded count separately, so a population
  that shrank to nothing is distinguishable from one that is clean.
- risks — the read-path budget is the near-certain one, not a hypothetical: this unit grows a capped
  member whose margin is in the low tens of bytes, and S-READPATH is the mitigation, in scope rather
  than noted. The other real hazard is a predicate that reds innocent files. Mitigated by running the
  candidate over the whole tree before wiring it and printing hits AND near-misses, which this repo
  requires of any new gate predicate.
- testing + left-shift gates — every trigger and refusal gets a selftest arm; the no-markers arm needs
  a fixture because no live file exercises it.
- migration / rollback — nothing to migrate. Rollback is deleting the canon tuple; the two position
  triggers are untouched and keep working.
- user docs — the canon and the documented immutability rule land in `memory/HYGIENE.md` via its
  template.

## 6. Acceptance criteria

- **AC1** — When a README in the declared population carries a heading outside the canon,
  `python tools/memory-tree/gen_build_index.py --check-format` exits 1 and names the file and the
  offending line.
- **AC2** — When a README in the declared population carries the canonical headings out of canonical
  order, `--check-format` exits 1 and names the first heading that broke the order.
- **AC3** — When a README carries no generated marker pair at all, `--check-format` exits 1 naming
  that file; the RED is observed first by staging the break, because this arm passes today.
- **AC4** — When a non-blank line sits between the title line and the first canonical heading,
  `--check-format` exits 1 naming that line.
- **AC5** — When the declared population is empty, `--check-format` exits 0 AND prints a line stating
  the population is empty, so a green run is never mistaken for coverage.
- **AC6** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, every new arm passes
  and the count of `arm ok` lines it prints has risen by the number of branches added. The harness
  prints no summary count line, so the observation is the line count, not a reported total.
- **AC7** — When `bash tools/run-gates/run-gates.sh` runs, the `build README slot contract` leg is
  green, and `do_check_format`'s docstring carries the paragraph naming what the contract does not
  check.
- **AC8** — When `python tools/memory-tree/gen_build_index.py --survey` runs over all tracked build
  READMEs, it exits 0 and lists hits AND near-misses including files outside the declared population,
  and that output is recorded in this build's acceptance ledger.
- **AC9** — When the build-level rules slot carries a method classification line and a promotion
  notice, `--check-format` exits 0, and `memory/guides/BUILD-METHOD.md` names that slot as their home.
- **AC10** — When `python tools/memory-tree/corpus_ids.py --report` runs before and after the
  `memory/guides/BUILD-METHOD.md` re-render, both margins are recorded, and
  `bash tools/memory-tree/check-memory-hygiene.sh` is green including check 16.

## 7. Gates

`build README slot contract` · `build-index selftest` · `memory hygiene` · the hygiene parity harness ·
`check-kit-versions.sh` (leg `kit version markers`, unguarded) · `check-verdict-epoch.sh` ·
`kit/dogfood doc parity`.

## 8. Open questions

- **F1 — does the description slot carry the goal bound, or is the bound its own slot?** S3 folds it
  in, on the ground that two slots that must agree are one fact in two places. The alternative keeps
  them separate so the method's rescope rule can point at a slot whose only job is to be that bound.
  RESOLVED (agent, 2026-08-24, delegated): fold, as specced — the owner's fork-2 ruling named the goal
  bound as an addition to the slot set, and folding it into the description satisfies that without
  creating a second authored sentence that can disagree with the first.
- **F2 — should `--write` scaffold the canonical headings into a new build README?** For: it makes the
  canon self-serving for every new build and removes the commonest way to fail it. Against: `--write`
  has never authored prose, and a scaffold shipping empty required bodies would red the shape check it
  was meant to satisfy. Recommendation: no scaffold in this unit; revisit if unit 7 measures authoring
  friction as the dominant cost. RESOLVED (agent, 2026-08-24, delegated): no scaffold. Veto 1 discards the
  alternative outright — a scaffold shipping empty required bodies fails AC1 and AC5, which this
  same spec writes.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, from the owner rulings of the same date and the adversarial
  verification of the five research claims.
- rev-2 · 2026-08-24 · folded spec-audit round 1. The blind-spot paragraph leaves
  `tools/gate-legs.json`, whose key set is closed and canary-enforced. The survey verb becomes a real
  S-item, because the flag AC8 named did not exist and an unknown argument is silently ignored, so the
  criterion would have passed by printing the ordinary clean line. The roster pair gains a declared
  position and a budget-slice exclusion. The two method-mandated writes gain a named home. The
  kit-version bump becomes an S-item here rather than only in unit 5.
- rev-3 · 2026-08-24 · folded the factual corrections from round 1's LOW tier. The alternatives
  paragraph no longer reads one record's two separate refusals as two reasons for one; only the
  plan-slot refusal expired. AC6 counts `arm ok` lines, because the harness prints no total. The
  dossier refresh is named as prose rather than as a new claim.
- rev-4 · 2026-08-24 · folded spec-audit round 2. The kit-version carrier set becomes a DERIVATION
  rather than a pointer at the epoch gate's remedy string, which resolves to five carriers where
  seven exist and reds an unguarded leg — the defect `TOOL-dSettledRoster-4` records as having cost
  a full-bar cycle twice, and which this fold reproduced by copying round 1's own fix text. The
  read-path charge for this unit's BUILD-METHOD.md growth becomes its own S-item: round 1 asked for
  both halves and the first fold priced only unit 8's, which rev-3 then narrowed so it cannot cover
  this one. The stale `tools/gate-legs.json` entry in Files touched is DELETED rather than negated.
- rev-5 · 2026-08-24 · every open fork in section 8 resolved under the standing mandate's delegated resolver authority, by M3's rule: the most feature-rich survivor after the three vetoes. No option was taken that needed a new dependency, install location or public surface. The one question this build refuses is not a spec fork and is parked on the run-state file instead.
- rev-6 · 2026-08-24 · BUILT and CLOSED. The canon, the registry reader, the no-markers arm and the survey verb all landed; 13 selftest arms added, 71 to 84, and the canon walk was disabled in place to watch five of them fail before restoring. Two things changed during the build: the method pointers were compacted after the first wording pushed BUILD-METHOD.md further over its own line budget, and the read-path figure in the conf was re-derived after that compaction rather than carried forward. Ledger: `build/2026-08-24-build-TOOL-dFramedEntrypoint-1-acceptance.md`.

## 10. Reuse audit

Memory-recall terms used for the regrounding read, recorded because the build method asks for them:
`build README slot contract generated region authored prose entrypoint roster units order verb tier
immutable description curation cap`.

`python tools/codebase-map/reuse_lookup.py "grade a markdown file against a closed heading sequence"`
ranks the `build-readme-surface` affordance seam and its `apply_region` entry among the candidates.
The seam this unit wires through is `slot_violations(text, path)`, published by that dossier as a
reuse affordance and already the sole caller-facing shape of the position contract. No new seam is
created: the third trigger is added inside the existing return contract of line-and-reason pairs, so
every present caller keeps working unchanged.
