# TOOL-dScaffoldedMirror-9 — the grandfather set with a provenance assert, replacing all three pins

**Status:** DEFERRED · rev-1 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · streams tooling · gated on TOOL-dScaffoldedMirror-7's first reading + a read-only --probe of incms

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-TOOL-dScaffoldedMirror-2-spec-set-review.md](../build/2026-08-24-build-TOOL-dScaffoldedMirror-2-spec-set-review.md) | spec-audit | TOOL-dScaffoldedMirror-2 TOOL-dScaffoldedMirror-3 TOOL-dScaffoldedMirror-4 TOOL-dScaffoldedMirror-5 TOOL-dScaffoldedMirror-6 TOOL-dScaffoldedMirror-7 TOOL-dScaffoldedMirror-8 TOOL-dScaffoldedMirror-10 TOOL-dScaffoldedMirror-11 TOOL-dScaffoldedMirror-12 TOOL-dScaffoldedMirror-13 TOOL-dScaffoldedMirror-14 TOOL-dScaffoldedMirror-15 |

<!-- /gen:spec-records -->

## 1. Goal

`lexicon.py:537` is `if len(unwaived) > pin`, with no direction guard and no baseline, and the
mechanism has fired three times in its life for three raises: 412, 415, 417, 463. Replace all three
`*_OFFENDER_PIN` integers with a shrink-only set of offender IDENTITIES keyed `path::name`, pinned
to a `FREEZE_SHA` at which every member must be DERIVABLE as an offender. No edit to the present
tree can change what a past commit contains, which makes topping the file up impossible rather than
expensive — the only mechanism in the whole build with that property, and the first assertion in
this kit's history that a ceiling edit could violate.

## 2. Scope (IN)

- **S1** — `.lexicon.conf` gains `FREEZE_SHA="<40 hex>"`, pinned once at adoption and never
  advanced.
- **S2** — the grandfather set at `tools/lexicon/lexicon-grandfathered.txt`, `role = "seed"` in
  `kit.toml`, one `path::name` key per line and no reason field. It only shrinks.
- **S3** — the five asserts, A through E, exactly as §4 states them.
- **S4** — the freeze-time derivation: one `git cat-file --batch` over the distinct PATHS in the
  set, graded by the SAME extractor and TODAY's declaration, with a sha-keyed cache under the git
  dir.
- **S5** — one commit deletes all three `*_OFFENDER_PIN` keys from `.lexicon.conf`, `PIN_KEYS` from
  `lexicon.py`, the `lexicon-pins` hole from `kit.toml`, and `-5`'s three `RATCHETS` rows from
  `drift_signals.py`, and adds the assert that a `RATCHETS` row names a live key.
- **S6** — the same commit deletes about 70 lines of pin archaeology from `.lexicon.conf`.
- **S7** — a `--freeze` verb that writes the set once, refusing on an empty `ratified` stamp, and a
  `--drain` verb that deletes every grandfathered key which is no longer an offender. `--drain` can
  only delete, so it cannot absorb.
- **S8** — the three multiplicity keys are RENAMED rather than carried:
  `tools/memory-recall/bench.py::enc` (3 occurrences), `tools/memory-tree/gen_build_index.py::_rec`
  (2) and `tools/govkit/selftest.py::scratch_gov` (2). Verified today: 463 occurrences over 459
  distinct keys, and those three keys account for exactly the 4-occurrence excess.
- **S9** — the 459-row backfill on this repo, per `TOOL-dScaffoldedMirror-18`.

## 3. Non-goals (OUT)

- **No freeze advancement, in v1.** The set only shrinks. Advancement needs a subset rule, and the
  subset rule is the one place a base sneaks back into a design that spent a section refuting bases.
- **No remote reachability requirement.** The unattended protocol observes its BASE from the remote
  because a run merges and pushes with no owner turn; a NAMING leg that reds on every offline run
  and in every shallow CI clone is worse than the attack it prevents, and that attack — a run
  minting the commit that grandfathers its own offenders — is a one-line diff on a tracked file a
  reviewer reads.
- **Not under the memory root.** A `memory/lexicon/` location reds `HYGIENE check 3 FAILED —
  unexpected entries (structure)`, exit 1, measured, and its remediation is a `.memory-tree.conf`
  edit: an optional kit forcing a declaration change in a required one, which is the coupling
  direction this kit's own `LAYERS` rule exists to forbid.
- **No integers anywhere in the design.** That is what S8's three renames buy: no count, no
  multiplicity field, no per-key occurrence number.
- **No diff-scoped enforcement.** Base-dependent, and this repo has three incompatible bases at the
  push boundary.
- **No predicate change and no extractor change.** `-11` owns the scoped visitor and P6; this unit
  grades exactly the population `-11` leaves it.
- **No waiver redesign.** `-4` owns `path::name` keying and the mandatory reason. This unit consumes
  that key space and does not define it.
- **`-11` lands first, and this is not a preference.** A staged 8-method `ast.NodeVisitor` in
  `tools/lexicon/` reds the gate TODAY at 471 over pin 463, and 26 of 26 proposed identifiers are
  off-table including all 17 `visit_*` names, which CPython's dispatch mandates and which cannot be
  renamed. Under this unit they cannot be grandfathered either, because they are post-freeze. The
  design's own first act would then be 16 to 18 waivers, in the design whose thesis is that the
  waiver is the last escape hatch.

## 4. Design

### Data model

```
.lexicon.conf                            FREEZE_SHA="<40 hex>"        pinned once, never advanced
tools/lexicon/lexicon-grandfathered.txt  <path>::<name>               one per line, shrink-only
tools/lexicon/lexicon-verb-waivers.txt   <path>::<name>  <reason>     owned by -4
```

One key space, two files, two different meanings. A grandfathered key says "this predates the
freeze"; a waived key says "this is a deliberate exception and here is why". The grandfather file
carries no reason field on purpose: its reason is identical on every row and a uniform justification
is not one.

### The five asserts

| | assert | what it forces |
|---|---|---|
| A | every current offender is grandfathered or waived | a new offender REDS; no absorbing move |
| B | every grandfathered key is still an offender | draining forces deleting the row, same commit |
| C | every grandfathered key is an offender at `FREEZE_SHA` | the file cannot be topped up |
| D | grandfathered intersect waived is empty | no double cover hiding a drain |
| E | the sha resolves, its tree reads, both sets non-empty | a shallow clone prints DEAD PROBE |

Assert C is the load-bearing one and the others are hygiene around it. A, B and D all read the
PRESENT tree, which is the tree the author is editing; each of them can be satisfied by an edit. C
reads a past commit, and no edit to the present tree can change what a past commit contains. Topping
the file up therefore requires ALSO moving `FREEZE_SHA`, which is a one-line diff on a tracked file
whose entire purpose a reader knows.

C is also the repair a reviewer of this kit already proposed and this kit already cut.
`memory/builds/dClosedLexicon/reviews/2026-08-16-review-TOOL-dClosedLexicon-1-1.md:36` reads "FIX:
guard on the offender IDENTITIES, not the count", and the pin-direction guard was cut at unit 1's
rev-3 on defects in a DIFFERENT spelling while that sound proposal sat unbuilt in the same record.
Restoring it is building a design a reviewer already validated, not inventing one.

### Assert C, implemented

The derivation is deliberately small, and every step of it is measured below.

1. `git cat-file -e <FREEZE_SHA>^{commit}` — resolves, or assert E fires and the run prints DEAD
   PROBE rather than a green line. Ported inline from `tools/drift-audit/drift_report.py`'s
   `Git.is_commit` rather than imported, exactly as `subtokens.py` was ported from `codebase-map`
   and for the same stated reason: the kit ships self-contained.
2. Collect the distinct PATHS in the grandfather set, not the keys. On this repo today that is 45
   paths for 459 keys, so the derivation's unit of work is 45, not 459.
3. ONE `git cat-file --batch` process, fed `<FREEZE_SHA>:<path>` on stdin, all blobs read from one
   stream. This is not an optimisation, and §5 gives the number.
4. Grade each blob with the SAME extractor the live check uses. `extract()` currently takes a `Path`
   and calls `read_text`; it splits into `extract_text(src, mode, pset)` with `extract()` a two-line
   wrapper. The freeze pass reads blobs and never touches the worktree.
5. Build `offenders_at_freeze` as `path::name` keys, then assert `grandfathered` is a subset of it.
   Each violator is reported as `<key>: not an offender at FREEZE_SHA`.

**Which declaration the freeze-time derivation reads: TODAY's.** So admitting a verb retroactively
un-offends historical keys, assert B reds every one of them, and they must be deleted in that same
commit. That IS the pressure. Reading the conf as it stood at the freeze sha would let a
grandfathered row outlive the justification that put it there, forever.

**The cache.** The result of steps 2 through 5 depends only on `FREEZE_SHA` and today's declaration,
both immutable within a run. It is cached at `<git-dir>/lexicon-freeze-cache.json`, keyed by a
digest of `FREEZE_SHA` plus the conf's `VERBS`, `LANGS` and corpus-scoping bytes, so any declaration
edit invalidates it. It is never tracked, following `<git-dir>/gate-ledger.tsv`, and a missing or
corrupt cache costs wall clock and never a verdict — the same law the run-gates timing cache runs
under. It does not make the assert forgeable in any way editing `lexicon.py` would not already: a
check running under the run's own uid is a review surface, and
`memory/guides/UNATTENDED-PROTOCOL.md` §9 says exactly what that buys.

### The three renames

`bench.py::enc`, `gen_build_index.py::_rec` and `selftest.py::scratch_gov` are one key covering
three, two and two occurrences. Carrying them would need a multiplicity field, which is an integer,
which is a pin with a smaller domain. Renaming three keeps the design free of integers entirely, and
the arithmetic confirms the population is otherwise clean: 463 occurrences minus the 4-occurrence
excess across those three keys is exactly 459 distinct keys.

### Migration

One commit, and it must be one commit or the bar is red on `main` between them:

- write `FREEZE_SHA` and the 459-row set
- delete `VERB_OFFENDER_PIN`, `SUFFIX_OFFENDER_PIN`, `LAYER_OFFENDER_PIN` from `.lexicon.conf`
- delete `PIN_KEYS` and the pin comparison from `lexicon.py`
- delete the `lexicon-pins` hole from `kit.toml`
- delete `-5`'s three `RATCHETS` rows from `drift_signals.py`, and add the assert that a `RATCHETS`
  row names a live key — the assert is what stops the next such row outliving its subject silently
- delete about 70 lines of pin archaeology from `.lexicon.conf`
- rename the three multiplicity keys (S8)

`-5` is DELETED by this unit and `-5`'s spec must say so on its side; the reciprocal is owed there.

### Rollout

Zero adopters carry a `.lexicon.conf` other than this repo, so there is no fleet to migrate.
`--freeze` refuses on an empty `ratified` stamp: freezing against a table nobody has curated yet
would grandfather a set derived from a table that is about to change, and assert B would then red
every row the curation un-offends. So the adoption order is scaffold, curate, ratify, freeze.

### Merging the set

The file only shrinks, so a merge reconciles by taking the UNION of both sides' deletions, which is
the intersection of the two row sets. That is a documented manual rule rather than a merge driver
until a second node actually drains concurrently, and a wrong reconcile is safe in one direction and
loud in the other: a row wrongly kept reds on assert B, and a row wrongly dropped reds on assert A.
Neither outcome is a silent absorption, which is the property that makes the manual rule adequate.

### Files touched (estimate)

`tools/lexicon/lexicon.py` (~300 lines: the five asserts, the freeze derivation, the cache, the
`--freeze` and `--drain` verbs; the pin comparison and `PIN_KEYS` deleted).
`tools/lexicon/lexicon-grandfathered.txt` (new, 459 rows here). `tools/lexicon/selftest.py` (~200
lines, five staged-break arms plus the cache arm). `tools/lexicon/kit.toml` (the seed row; the
`lexicon-pins` hole deleted). `.lexicon.conf` (`FREEZE_SHA` added, three pins and ~70 lines of
archaeology deleted). `tools/drift-audit/drift_signals.py` (three rows deleted, one assert added).
Three source files for the renames. About 600 lines net including the selftest arms.

### Alternatives rejected

- **A bare shrink-only file with no provenance assert.** That is a pin with 459 digits. This repo
  has the receipt in its own tree: `memory/map/baseline.toml` carries a shrink-only claim and
  records "Nothing enforces the rule today — that is why the option was available at all", beside a
  documented in-place rename that the rule forbids.
- **Per-directory pins.** N raise paths instead of one, and a new directory mints its own.
- **A justification-comment ratchet.** Satisfied by prose. The 417 to 463 move came with three
  paragraphs of it and would have sailed through.
- **Diff-scoped enforcement.** §3, and the three incompatible bases.
- **Carrying multiplicity as a count.** An integer, which is the thing being deleted.
- **Requiring `FREEZE_SHA` to be reachable from the remote.** §3. The control that would actually
  bind lives on the remote, not in a stdlib checker run by the same session it is guarding.

## 5. Production-readiness checklist

For Tier-2, the unresolved item in §8 IS the owner scope menu.

- **security** — the honest statement, because the alternative is a claim this cannot carry. Assert
  C makes an absorbing EDIT impossible; it does not make an absorbing COMMIT impossible, because a
  run with shell access can move `FREEZE_SHA` in the same diff. What it converts is the failure
  mode: an absorption stops being a plausible-looking pin raise and becomes a visible edit to the
  one value in the file whose purpose is provenance. `memory/guides/UNATTENDED-PROTOCOL.md` §9
  states what a check running under the run's own uid can and cannot buy, and remote reachability
  was dropped deliberately rather than forgotten.
- **perf / scale** — measured on this worktree, node `d`, 2026-08-24. The 459 keys span 45 distinct
  paths, 37 `.py` and 8 `.js`. One `git cat-file --batch` reads all 45 blobs in **0.047 s**;
  `ast.parse` plus a walk over the 37 Python blobs (656 function definitions) costs **0.406 s**;
  total added **0.454 s**, taking the cold check from 0.44 s to about 0.89 s against the research
  pass's 0.81 s estimate. Warm, on a cache hit, it returns to about 0.45 s. The batch is
  load-bearing: 45 SEPARATE `git cat-file blob` execs cost **0.982 s**, 21.8 ms each, which is 21x
  the batched read and matches this node's recorded per-exec antivirus tax of about 0.022 s.
  Per-path exec would make the git read cost more than twice the parse. On `incms/main` the row
  count is 6,566 and the distinct-path count is UNMEASURED; the research pass's 8 to 10 s cold
  estimate stands and is not re-derived here.
- **a11y** — N/A. A CLI checker with no rendered surface.
- **i18n** — N/A. Keys are repo paths and identifiers.
- **error / empty / loading states** — assert E is exactly this row. An absent sha, a shallow clone
  and a blobless partial clone (`--filter=blob:none`, where `cat-file --batch` either fetches on
  demand or fails) all resolve to DEAD PROBE naming the condition, never to a green line. The
  non-empty requirement on both populations is what stops an empty grandfather file and an empty
  offender set reading as a satisfied gate.
- **observability** — every run prints the three sizes: grandfathered, waived, and current
  offenders. A drain shows up as a falling first number with no other change, which is the only
  signal in this kit's history that could ever have shown one.
- **risks** — three, in order. First, assert B makes a rename RED until its grandfather row is
  deleted in the same commit, and the measured median is 42 renames per commit on this repo;
  `--drain` (S7) is the answer and it must ship with the asserts, not after them. Second, if `-11`
  has not landed, the scoped visitor reds this gate on arrival and the escape is 16 to 18 waivers —
  the §3 note. Third, the one-commit deletion in §4 is genuinely atomic: a commit that deletes the
  pins without the set, or the set without the pins, leaves `main` red.
- **testing + left-shift gates** — one AC per assert, each STAGED, confirmed RED, then unstaged,
  plus an arm proving a stale cache cannot turn a red green. Assert C's failing case has never been
  observable in this kit before, because there has never been an assertion a ceiling edit could
  violate — a pin raise was always legal, so there was nothing to stage.
- **migration / rollback** — §4's Migration. Rollback is a revert of one commit, which restores
  three integers and deletes 459 rows. Zero adopters other than this repo, so no fleet migration
  exists.
- **user docs** — `tools/lexicon/LEXICON.md` gains the freeze mechanism, the drain procedure and the
  statement that the set never grows; `README.md` gains the adoption order (scaffold, curate,
  ratify, freeze) and the merge rule.

## 6. Acceptance criteria

- **AC1** — When `def frobnicate_thing()` is staged into a tracked Python file, `python
  tools/lexicon/lexicon.py` reds naming that key as an offender in neither the grandfathered nor the
  waived set (assert A). Staged, observed RED, unstaged.
- **AC2** — When a grandfathered function is renamed to a table-legal name without deleting its row
  from `tools/lexicon/lexicon-grandfathered.txt`, the check reds naming that row as no longer an
  offender (assert B). Staged, observed RED, unstaged.
- **AC3** — When a row is hand-added to `tools/lexicon/lexicon-grandfathered.txt` for a function
  that did not exist at `FREEZE_SHA`, the check reds with `not an offender at FREEZE_SHA` (assert
  C). Staged, observed RED, unstaged. This is the arm with no precedent in this kit.
- **AC4** — When a key present in `tools/lexicon/lexicon-grandfathered.txt` is also added to
  `tools/lexicon/lexicon-verb-waivers.txt`, the check reds naming the key and both files (assert D).
  Staged, observed RED, unstaged.
- **AC5** — When `FREEZE_SHA` is pointed at a sha absent from the repository, the check prints `DEAD
  PROBE` naming `FREEZE_SHA` and exits non-zero rather than reporting zero findings (assert E).
  Observed against a synthetic 40-hex value and against a `git clone --depth 1` fixture.
- **AC6** — When `python tools/lexicon/lexicon.py --drain` runs after a rename, it deletes exactly
  the rows that are no longer offenders, adds none, and the following `python
  tools/lexicon/lexicon.py` is green.
- **AC7** — When `python tools/lexicon/lexicon.py --freeze` runs against a conf whose `ratified`
  value is empty, it refuses, names the stamp, writes no file, and exits non-zero.
- **AC8** — When `<git-dir>/lexicon-freeze-cache.json` is hand-edited to claim a post-freeze key was
  an offender at the freeze, AC3's staged break still reds — the cache is keyed by the declaration
  digest and a mismatch discards it rather than trusting it.
- **AC9** — When the landing commit is inspected, `grep -rn "OFFENDER_PIN" .lexicon.conf
  tools/lexicon/ tools/drift-audit/` returns nothing, and `python tools/drift-audit/drift_report.py`
  is green with no `RATCHETS` row naming a deleted key.
- **AC10** — When `python tools/lexicon/lexicon.py` runs cold on this repo after landing, the added
  cost against the pre-change run is under 0.6 s, measured from `<git-dir>/gate-ledger.tsv` rather
  than asserted; a run over 1.5 s cold is a finding, not a pass.

## 7. Gates

Keeps green: `lexicon naming predicates`, `lexicon selftest`, `lexicon wiring`, `memory hygiene`,
`drift-audit records`, `drift-audit selftest`, and the kit version markers. Adds NO new gate leg.
The five asserts are new refusals inside `lexicon naming predicates`, and the
`RATCHETS`-row-names-a-live-key assert is a new refusal inside the drift-audit legs that already
read that table — the leg count is not the coverage, and a sixth leg here would only advertise that
an assert needed its own process.

## 8. Open questions

- **F1 — which sha does this repo freeze at?** UNRESOLVED, and it is an owner input by construction
  rather than an agent decision left pending. The whole value of `FREEZE_SHA` is provenance, and
  provenance is a claim about trust that the run writing the file cannot make about itself: a run
  minting the commit that grandfathers its own offenders is precisely the shape ruling 3 declined to
  defend against remotely. RECOMMENDATION: the merge-base of this build's branch with `origin/main`
  at the moment the owner approves this spec — a sha that predates every commit this build writes
  and that the owner can name. The build cannot proceed past S1 without an answer.
- **F2 — where does the set live and what parser reads it?** RECOMMENDATION:
  `tools/lexicon/lexicon-grandfathered.txt`, `role = "seed"` beside the three waiver registries, in
  the same line grammar so `load_waivers` generalises to a shared `load_keyset(path, reason=False)`
  rather than a second parser. One file grammar for four registries, and the reason field is the
  only difference. RESOLVED (agent, 2026-08-24, delegated): the kit directory, `role = "seed"`,
  shared reader.
- **F3 — NEW DEPENDENCY EDGE, not in the build's stated set: `-3` reaches assert C.** Corpus scoping
  changes which files are graded, and assert C grades a past tree. RECOMMENDATION: apply TODAY's
  scoping at the freeze sha, for the same reason ruling 1 reads today's declaration. The consequence
  is worth stating rather than discovering: excluding a path today makes its grandfathered rows
  underivable, assert C reds them, and they must be deleted in the scoping commit — which is
  correct, because a key in an ungraded file is not an offender. `-3`'s spec does not carry the
  reciprocal and it is owed there. RESOLVED (agent, 2026-08-24, delegated): today's scoping,
  deletions in the scoping commit.
- **F4 — does `--scaffold` write the grandfather set for a new adopter?** RECOMMENDATION: no, and
  `--freeze` is a separate verb refusing on an empty `ratified` stamp. Freezing against a PROPOSED
  table would grandfather a set derived from a table about to be rewritten, and assert B would then
  red every row the curation un-offends — turning an adopter's first curation pass into a 6,566-row
  deletion. RESOLVED (agent, 2026-08-24, delegated): a separate `--freeze`, post-ratify.
- **F5 — does `-14` land before the freeze?** It renames 79 of the 459 keys (`t_` to `test_`, `do_`
  and `cmd_` to a reserved `cmd` row), which is 17% of the backfill. RECOMMENDATION: land `-14`
  first and freeze at 380 rows. A key renamed AFTER the freeze must be deleted from the set under
  assert B anyway, so the work is identical; doing it first means 79 rows are never written. This is
  a sequencing preference, not a blocker, and reversing it costs nothing but 79 lines. RESOLVED
  (agent, 2026-08-24, delegated): `-14` first where the schedule allows, freeze either way.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, grounded on recommendation R8 of the `dScaffoldedMirror`
  research pass (`build/2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md`)
  and on the read-only probe of `incms/main` taken the same day with the kit's own extractor.
  Carries R8's five rulings unchanged. Three figures are measured HERE rather than carried: 459
  distinct keys over 45 distinct paths, the 0.454 s freeze derivation, and the 21x cost of per-path
  `git cat-file` execs against one `--batch`. Adds `--drain` and `--freeze` as named verbs, which R8
  implied and did not name, and the merge rule for a shrink-only tracked file, which it did not
  raise.
- rev-1 status 2026-08-24 · DEFERRED to a SEVENTH item by the owner ruling, gated on evidence rather than scheduled. Five defects stop it landing as written and none is costed: the seed ships gov's 459 rows to every adopter and deletes the hole that explained the red, it deletes three pin keys where `-11` makes four, shrink-only has no assert, AC8 asserts a cache property the digest cannot deliver, and the multiplicity answer is three renames on gov and 113 on the one real adopter. The deterrent is also priced unevenly: `-5` refuses to claim pressure for a move it prices at five minutes of prose, and this spec claims it for a one-line diff. The difference is VISIBILITY, not cost, and nobody in the set prices visibility. Build it after `-7` has reported once.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py grandfather freeze sha ratchet baseline pin` returns two
near-relatives and no seam this unit can wire through.

The structural relative is `codebase-map`'s baseline: `parse_baseline` and `render_baseline`
(`tools/codebase-map/map_lib.py`) over `memory/map/baseline.toml`, a shrink-only registry with a
ratchet that reds on an unclaimed new key — assert A's shape, one kit over. It is a shape to learn
from and a recorded failure to avoid, not a seam: `.lexicon.conf`'s `LAYERS` rule forbids
`tools/lexicon/*` importing `tools/codebase-map/*` precisely so this kit ships self-contained, and
that baseline's own header records "Nothing enforces the rule today — that is why the option was
available at all", which is the exact defect assert C exists to remove.

The provenance relative is `tools/drift-audit/drift_report.py`'s `Git` class, whose `is_commit` is
`git cat-file -e <sha>^{commit}` and whose `ratchet_findings` (fan-in 1) already parses this repo's
`RAISED N -> M` convention. Same self-contained argument, so the two-line `is_commit` idiom is
PORTED inline rather than imported — the precedent is written into `.lexicon.conf`'s own `LAYERS`
comment, where `subtokens.py` is named as a port made to honour that rule.

The reuse that DOES apply is internal and is two splits rather than any new mechanism: `extract()`
splits into `extract_text(src, mode, pset)` so the freeze pass can grade a blob instead of a file,
and `load_waivers` generalises into `load_keyset(path, reason=False)` so four registries share one
grammar. No new helper is introduced on either side.
