# TOOL-dScaffoldedMirror-12 — the consistency instrument, measured before it is believed

**Status:** DEFERRED · rev-1 · 2026-08-24 · node d · Tier-1 · base 9ddcc5c9 · streams tooling · re-file behind the visitor rewrite, out of this build

## 1. Goal

Decide with a measured precision figure, rather than with an argument, whether the consistency
instrument is worth building. It is the only idea in this build that measures the thing the owner
actually asked for — whether two sessions naming the same thing agree — and it is the only one whose
day-one precision is unknown and looks bad by inspection. This unit produces a number and a written
decision. It ships no gate, no leg, and no code on the check path.

## 2. Scope (IN)

- **S1** — reproduce the research pass's figures with the kit's own splitter, so the thing being
  graded is the shipped instrument and not a re-implementation: `824` definitions, `589` carrying an
  object, `418` distinct objects, `47` objects spelled with more than one leading token covering
  `167` definitions, `CONSISTENCY = 0.716`.
- **S2** — build and measure three candidate concept keys against `tokens[1:]`, defined in §4.
- **S3** — run every key over BOTH corpora: this worktree, and `C:/projects/incms/main` read-only,
  writing nothing to that repo.
- **S4** — hand-classify at least 40 groups per repo per surviving key as GENUINE CONFLICT or
  ARTIFACT, and report precision per key per repo with the full classified sample, not the ratio.
- **S5** — a written verdict on each of the four disqualifying gaps, saying which are closable and
  which are properties of the definition.
- **S6** — the written decision on whether the verb table demotes from allowlist to arbiter, or the
  written refusal, with the precision figure that decided it.
- **S7** — the deliverable is one build record under `memory/builds/dScaffoldedMirror/build/` with
  the probe script folded in as an appendix. That is the shape the adopter probe already used in the
  research record, and it keeps a throwaway measurement out of `tools/`.

## 3. Non-goals (OUT)

- **No gate, no leg, no conf key, no new verb on `lexicon.py`.** RESEARCH here means the deliverable
  is a number and a decision. A unit that lands a signal has pre-empted the decision it was asked to
  inform.
- **No change to P1's verdict.** The 60 conflicts P1 currently calls green stay green. This unit
  measures them; it does not act on them.
- **It does not demote the verb table.** It supplies the evidence; the architecture inversion is the
  owner's call and is stated as such in §8.
- **No shipped concept key.** `subtokens()` and `leading_verb()` (`tools/lexicon/subtokens.py`) are
  READ and not edited. A concept key that lands in the kit before its precision is known is the
  thing this unit exists to prevent.
- **Not blocked on `-8`, and it does not wait for the canon.** It also does not build one: the
  arbiter is `-8`'s mechanism and is cited here, never restated.

## 4. Design

### The instrument, stated exactly

Group every graded definition by its OBJECT — the subtokens after the leading one. A group is
CONSISTENT when every member leads with the same token. `CONSISTENCY` is one minus the share of
object-carrying definitions sitting in a group that is not: `1 − 167/589 = 0.716` on this worktree.
Both operands derive from the tree at read time, so unlike a pin there is no number an editor can
raise. There is no vocabulary anywhere in it, which is why the §12 mirror ban does not reach it.

### What it finds, and what it declines to find

It fires on 60 definitions that P1 calls GREEN: `load_conf` eight times against `read_conf`, both
declared verbs carrying different declared meanings, and the object `region` spelled `build_`,
`render_`, `parse_`, `apply_` and `insert_`, all five legal. It declines to fire on 354 of the 459
offender keys, which conflict with nothing in this corpus — they fail a table without being
inconsistent with anything. Measured with the shipped checker on this worktree, 2026-08-24:
`python tools/lexicon/lexicon.py --list` reports 463 verb occurrences over 459 distinct `path::name`
keys over 395 distinct bare names.

### The four disqualifying gaps, and which are actually research

- **Silent on the first instance** — a group of one scores 1.000, at exactly the moment an author
  most needs an answer. NOT CLOSABLE: closing it requires a vocabulary, and having none is the
  instrument's whole claim.
- **A repo where every function is `get_`-prefixed scores 1.000.** NOT CLOSABLE: orthogonality to
  quality is a property of the definition, not a defect in the implementation.
- **It has no opinion and can never say `load` not `fetch`.** NOT CLOSABLE here: that arbiter is
  `-8`'s canon, and this unit cites it rather than building one.
- **The `tokens[1:]` keying produces junk.** CLOSABLE, and **this one is the research** — the other
  three are stated so nobody spends the budget on them.

Three of the four are properties and one is a bug. Saying so is the design: this unit is not trying
to close the first three, it is deciding whether the fourth is closable well enough that the
instrument is worth having ALONGSIDE the table rather than instead of it.

### Why the keying is junk, which points at the key that is not

`of` collects `ext_of`, `owners_of`, `parent_of` and `cache_of`; `root` collects `repo_root` and
`map_root`, which are different roots. Every one of those six is NOUN-LED — `ext`, `owners`,
`parent`, `cache`, `repo`, `map` are not verbs — so grouping them by "the tokens after the leading
one" asks which verb they chose when they chose none. The corpus is ~288 of 463 noun-led, 62% of the
debt, so the largest single source of artifacts is a population `TOOL-dScaffoldedMirror-19` has now
ruled on. Three candidate keys follow, and the second is the one that hypothesis predicts:

- **K1** — the remaining tokens as an order-insensitive set, minus a closed connective list
  (`of for to in by at`). `ext_of` becomes `{ext}` and `owners_of` becomes `{owners}`, which
  separates the four.
- **K2** — K1, restricted to definitions the `-19` structural classifier calls verb-led. `-19` owns
  that classifier and it is cited, not designed here.
- **K3** — K1 plus a required minimum of one content token, so a name whose entire object is a
  connective is UNGRADEABLE rather than grouped. That is the treatment `leading_verb` already gives
  an identifier with no word characters (`subtokens.py:31-38`), applied one level out.

### The precision protocol, pre-registered

Precision is genuine conflicts over genuine plus artifacts, hand-classified. Gov has 47 multi-token
groups under `tokens[1:]`, so gov is a CENSUS and not a sample; incms is a seeded random 40 drawn by
a stated rule with the seed recorded. The bar is pre-registered before any group is read: ≥0.80
proceeds to a build recommendation, 0.50–0.79 buys one more key iteration and nothing else, and
below 0.50 is a written refusal. Pre-registration is not ceremony here — the agent choosing the key
is the agent grading the sample, and that is the single largest threat to this measurement.

### Alternatives rejected

- **Ship it now as a `gateable: False` drift signal and measure precision afterwards.** Roughly half
  the groups are artifacts by inspection. A standing signal reporting a number nobody can act on is
  the reassuring-zero class inverted, and it would be read as coverage.
- **Measure on gov only.** Gov's 824 definitions come from a 44-file Python corpus. Every noise
  floor in this kit's history fitted to that corpus has been wrong at adopter scale; incms grades
  14,659.
- **Replace P1 first and measure after.** That is the architecture inversion, and it is the outcome
  this unit exists to earn or refuse rather than assume.

### Files touched (estimate)

One probe script, folded into the record as an appendix. One build record under
`memory/builds/dScaffoldedMirror/build/`. Nothing under `tools/`, which §7 asserts rather than
promises.

## 5. Production-readiness checklist

- **security** — N/A. Read-only on both corpora, and the incms run writes nothing to that repo; the
  read-only adopter probe of 2026-08-24 is the precedent and its property is asserted in AC4.
- **perf / scale** — one corpus pass per key per repo. The equivalent shipped pass measures 0.44 s
  on gov and ~4.7 s on incms. Nothing runs on any bar, so this is a wall-clock note and not a budget.
- **a11y** — N/A. A measurement written into a record.
- **i18n** — N/A.
- **error / empty / loading states** — the empty state IS gap 1: a group of one. It is REPORTED as
  ungraded rather than scored as perfect, in every key, or the headline number flatters itself.
- **observability** — the record is the observability. Every figure carries its repo, its date and
  the key it was computed under, because the whole failure mode of this unit is a number without a
  key beside it.
- **risks** — confirmation bias, and it is the only real one: the same agent designs the key and
  grades the sample. Mitigated by pre-registering the bar and by publishing the classified sample
  rather than the ratio, so a reviewer can re-grade it.
- **testing + left-shift gates** — none, deliberately. Nothing lands on the check path, so there is
  nothing to regress. If the decision is BUILD, the arms belong to that unit and are priced there.
- **migration / rollback** — N/A. Nothing is migrated. The record stands whatever it concludes; a
  refusal is a result, not a failure to land.
- **user docs** — N/A until a build decision exists. A research record is not user-facing.

## 6. Acceptance criteria

- **AC1** — When the probe runs on this worktree under the `tokens[1:]` key, it reproduces
  `CONSISTENCY = 0.716` over `589` object-carrying definitions, using `tools/lexicon/subtokens.py`
  rather than a re-implementation. A different figure means the two passes graded different
  populations and the discrepancy is resolved before anything else is measured.
- **AC2** — When the probe runs under `K1`, `K2` and `K3`, the record carries one row per key per
  repo giving group count, multi-token group count and `CONSISTENCY`, so a reader can see which key
  produced which number.
- **AC3** — When the sample is classified, the record carries precision per key per repo over at
  least `40` groups each, with the full per-group GENUINE/ARTIFACT classification, not the ratio
  alone.
- **AC4** — When the incms pass finishes, `git -C C:/projects/incms/main status --porcelain` prints
  nothing, proving the run wrote nothing to a repo this build does not own.
- **AC5** — When the record is read, each of the four §4 gaps carries a written verdict, and only
  the `tokens[1:]` keying gap is answered with a measurement; the three recorded as properties are
  recorded as properties rather than quietly re-litigated.
- **AC6** — When the record is read, it carries the demotion decision against the `0.80`
  pre-registered bar, with the precision figure that decided it stated on the same line.
- **AC7** — When the unit lands, `git diff --stat` names no path under `tools/`, and
  `python tools/lexicon/lexicon.py` prints the same verdict line and exit code as at base
  `9ddcc5c9`.

## 7. Gates

Keeps green: `lexicon naming predicates`, `lexicon selftest`, `lexicon wiring`, `memory hygiene`.
The first three stay green TRIVIALLY, because nothing under `tools/lexicon/` changes — and that is
the point rather than an excuse: AC7 asserts the triviality instead of assuming it, since a research
unit that quietly touched the checker would owe arms it has not written. Adds no leg.

**What this unit does NOT check.** It adds no coverage of any kind. A green bar after it means a
record landed, and nothing about naming in this repo is enforced one line more tightly than before.

## 8. Open questions

- **F1 — where is the precision bar, and is it set before or after the sample is read?**
  RECOMMENDATION: 0.80, pre-registered in this spec before any group is classified, with the three
  outcomes in §4 written down in advance. The research pass's own instruction is *do not ship a
  metric whose precision is 50%*, which sets a floor but not a bar; 0.80 is the level at which one
  in five findings is noise, which is the ratio this kit already found unacceptable when it measured
  P1's 77% unactionable rate. RESOLVED (agent, 2026-08-24, delegated): 0.80, pre-registered, with
  the 0.50–0.79 band buying exactly one more key iteration.
- **F2 — does the owner want this measured at all, and if so before or after `-8`?** This is Phase 5
  and the research pass filed it as *only if the owner wants it*. It is a genuine owner fork and it
  is left UNRESOLVED, deliberately: nothing in the build is blocked on it, and resolving it by
  delegation would spend owner attention this unit has not earned. RECOMMENDATION: after `-8`. Two
  of the four gaps name an arbiter the canon supplies, so a decision taken before the canon exists
  is a decision taken against a strictly weaker alternative.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, grounded on the `dScaffoldedMirror` research pass
  (`build/2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md`, recommendation
  R11 and Phase 5) and on the read-only probe of `incms/main` taken the same day.
- rev-1 status 2026-08-24 · DEFERRED. Its own section 4 rules three of four gaps NOT CLOSABLE and its pre-registered bar is 0.80 against a measured 0.716, so the predicted outcome is a written refusal. It is cheap and its numbers are re-baselined by the visitor rewrite anyway, so it waits rather than dying.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py consistency object grouping leading token measurement`
returns `leading_verb` (`tools/lexicon/subtokens.py`, fan-in 3, SEAM) as its top candidate, and that
IS the seam this unit wires through. `subtokens()` in the same file supplies the full token list the
object key is built from, and using it rather than a fresh splitter is what makes AC1 a
reproduction rather than a second opinion — the research pass's 0.716 was computed over the same
split. The lookup's other hits do not fit: `resolve_tokens` (`tools/govkit/govkit.py`, fan-in 1)
resolves deployer template tokens and shares only the word, and `all_inventories`
(`tools/codebase-map/map_extractors.py`, fan-in 4, SEAM) enumerates map inventories rather than
identifiers. No new helper is introduced anywhere, because nothing is introduced anywhere: the
deliverable is a record.
