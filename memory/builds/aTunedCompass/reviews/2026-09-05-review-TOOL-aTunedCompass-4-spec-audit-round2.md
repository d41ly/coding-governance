**Serves:** spec-audit TOOL-aTunedCompass-4 TOOL-aTunedCompass-6 TOOL-aTunedCompass-9

# aTunedCompass — spec audit, round 2: reviewing the fold, not the specs it repaired

*Node `a`, 2026-09-05. A Tier-2 adversarial pass over the three units that carried a round-1
BLOCKER, read as DESIGNS and not as code. The other eight units of the set converged in round 1 and
are out of scope here. Every round-1 finding against these three was folded before this pass, so the
prose under review is fresh text nobody has read — the class this repo names at
`memory/gotchas/fold-text-is-unreviewed-surface.md`, and the reason the round exists. A primed
finder fan, a skeptic stage prompted to REFUTE every finding, one synthesis. Every claim any finding
made about existing code was re-checked at source during synthesis; the claims that moved on that
re-check are named inside the findings that carried them.*

**Round: 2.** Subjects, pinned at the blobs they were read at:

- `memory/builds/aTunedCompass/spec/2026-09-04-spec-TOOL-aTunedCompass-4.md@43318b38e84577b29007008b9960ca46b82b6e4c`
- `memory/builds/aTunedCompass/spec/2026-09-04-spec-TOOL-aTunedCompass-6.md@95f97b7a441756cd7df504332404c38d1810ea13`
- `memory/builds/aTunedCompass/spec/2026-09-04-spec-TOOL-aTunedCompass-9.md@78f32754ed788d4c8d66433001dfbe7cf16be1ef`

## Verdict: BLOCKED

Two blockers, seven highs, seven mediums: sixteen distinct defects, and fifteen of them are IN the
fold. Round 1 closed with three blockers on these three units. Two of the three original blockers
are genuinely retired; what replaced them are two new ones the fold itself created, one of which is
redding the merge bar at HEAD right now.

The set's failure mode has changed shape between rounds and is worth naming. Round 1's dominant
defect was a resolution that never reached the scope list. Round 2's is narrower and meaner: the
fold rewrote a section and left the OTHER half of the same claim standing — an id that now resolves
to the wrong criterion, a field the same commit refuted, a rollback line describing a scope the
same fold enlarged. Seven of the sixteen are that shape. It is not a new class; it is
`memory/gotchas/amendment-leaves-its-other-half-standing.md`, and the two orphans already caught by
hand in unit 4 after the fold were not the only two.

Unit 6 additionally leaves the bar RED. `python tools/check-spec-tokens.py` exits 1 at HEAD naming
this spec twice, on an unguarded `subject=repo` leg, over a waiver registry declared SHRINK-ONLY.
That is not a design opinion; it is reproducible in one command and blocks the push boundary today.

### Review shape

Raw 45, confirmed 21, refuted 24, unverified 0, precision 0.47.

The 21 confirmed findings resolve to **16 distinct defects**: five defects were reported by two
lenses at different addresses, and the severity adjudicated below is mine, not the reporting lens's.
Each merged entry names its source ids. The 0.47 precision is identical to round 1's, on a surface
one quarter the size — the refuted half was again dominated by findings reading spec prose as a
promise `memory/TEMPLATE-SPEC.md` does not make.

### Run integrity

- Lenses 4/4 returned, 0 DIED.
- Skeptic batches 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- 0 outstanding unverified findings.

Every count is zero, so no lens gap qualifies the finding set and a zero here is evidence. The
"0 duplicates" figure is the harness's — it counts verdict-level duplicates discarded before
synthesis. The five merges below are a synthesis judgement on top of that, not a contradiction of
it.

### Severity ledger

| # | Sev | Unit | Address | The defect | Source ids |
|---|---|---|---|---|---|
| B1 | blocker | 9 | §6 AC7, §2 S5c | the audit AC7 demands cannot report a number for this fixture, and widening it reds an existing arm | 26 |
| B2 | blocker | 6 | §6 AC9 + AC10 | two untracked backticked paths red the `spec tokens` leg at HEAD, unwaivably | 36, 28 |
| H1 | high | 4 | §8 F1 RESOLVED | the binding resolution still names `results` after the fold moved the measurement to `shown_paths` | 41, 31 |
| H2 | high | 4 | §6 AC5, §4 "What settles it" | the criterion stays unsatisfiable after its named unblocker lands, and §4 names the wrong fixture | 14 |
| H3 | high | 9 | §8 F1 + F2 | both resolutions cite pre-renumber AC ids and now resolve cleanly to the WRONG criteria | 15 |
| H4 | high | 4 | §4 "The parent key, verified at source" | the parent rollup is a per-path cap for 99.3% of the served chunk arm, and only the 0.7% branch is tested | 27 |
| H5 | high | 6 | §2 S7, §6 AC10 | the withholding covers `govkit apply` only, and codebase-map's documented install is `cp -r` | 37 |
| H6 | high | 4 | §4 Files touched, §5, §7 | the version bump is load-bearing for AC9 and none of its paired carriers is named | 40 |
| H7 | high | 9 | §4, §5, §7 | no Files-touched at all, a false rollback line, and a version-marker leg nothing in the unit feeds | 1 |
| M1 | medium | 9 | §5 | three restored readiness lines carry stale AC ids, and one frames AC3's requirement as the hazard | 17 |
| M2 | medium | 9 | §4 S2b vs §6 AC2/AC3 | the records-side filter cannot reject anything in the population AC3 mandates | 19 |
| M3 | medium | 6 | §6 AC2 | two literals measured at BASE, observed on a tree this unit's own new file enlarges | 22, 29 |
| M4 | medium | 6 | §6 AC10 | `bash tools/govkit/govkit.sh selfcheck` has never existed at any revision, and the hedge unpins it | 20, 32 |
| M5 | medium | 6 | §6 AC9, §2 S8 | the ceiling's enforcing runner is created by no scope item and observed by no criterion | 42 |
| M6 | medium | 6 | §7, §4 Files touched | the leg grading the descriptor S7 edits is absent, and the regenerated map artifacts are uncounted | 43 |
| M7 | medium | 9 | §7, §2 S5c | three grading legs missing from the list, and "iterate every fixture" silently rewrites three arms | 34, 44 |

---

## Blockers

### B1 — unit 9: AC7 asks for an overlap number the audit cannot produce for this fixture

*`spec/2026-09-04-spec-TOOL-aTunedCompass-9.md`, §6 AC7, with §2 S5c. Source id 26.*

AC7 requires `--audit-fixture` to report every question of the new set under `OVERLAP_MAX`. The
audit resolves targets in the PINNED set only: `measure_run` does `docs = bench.load(data,
pin["set"])` (`tools/memory-recall/check-recall.py:179`) and `.memory-tree.conf:286` pins
`RECALL_FLOOR="records:fts5:r@5>=0.81"`. S1 builds a set no question of which can resolve a
`records` target by construction. So `measure_overlap` returns `None` for every row, and
`check_audit` turns each one into a failure: "resolves no target in 'records' -- overlap is NOT
MEASURED, which is a DEAD PROBE rather than a passing 0.000" (`:260-261`).

AC7 is therefore unsatisfiable in the strongest sense — not "hard to hit", but incapable of printing
a number at all. The anti-tautology bound S5b says is "inherited outright" is inherited as a
guaranteed red.

The downstream half is worse than the criterion. Once S5c makes the audit iterate every fixture,
`tools/memory-recall/test_recall_floor.py:301` — `test_audit_green`, which asserts
`returncode == 0` on the committed set — goes red the day the new fixture lands, taking the
`recall floor arms` leg with it. `TOOL-aTunedCompass-3` is due to pin the merge bar on this same
population.

**Fix.** Extend S5c: the audit grades each fixture against the set its targets live in — a
per-fixture declared set, or the `chunks` set when the fixture uses `expected_paths` — rather than
against the pin's set. Then restate AC7 as "reports a measured overlap below `OVERLAP_MAX` for
every question, with no NOT MEASURED row", and add an arm pinning the DEAD PROBE branch so the
widened audit cannot pass by finding nothing.

**Left-shift gate.** Bind the set to the fixture rather than to the pin, and make the binding
checkable: every committed fixture declares the set its targets resolve in, and `--audit-fixture`
reds on a fixture whose declared set resolves no target for any question. That converts today's
"the pin happens to match the fixture" coincidence into an assertion, and it gates the CLASS —
every fixture this build is about to add, not this one.

### B2 — unit 6: the fold put two untracked paths in §6 and the bar is red on both right now

*`spec/2026-09-04-spec-TOOL-aTunedCompass-6.md`, §6 AC9 and AC10, with §7. Source ids 36, 28.*

Reproduced at HEAD:

```
spec-tokens: …-6.md [path] `tools/codebase-map/replay-phrases.py` — not tracked by git ls-files
spec-tokens: …-6.md [path] `tools/govkit/govkit.sh` — not tracked by git ls-files
spec-tokens: 3 unwaived hit(s), 0 stale waiver(s)
exit=1
```

The leg `spec tokens (a spec's own names resolve)` joins every path-shaped backticked token inside a
live spec's `## 6. Acceptance criteria` bullets against `git ls-files`
(`tools/check-spec-tokens.py:20`, `:173`). It carries NO guard and is `subject=repo`, so it runs on
every bar, and `memory/project/spec-token-waivers.txt` declares itself SHRINK-ONLY, so neither hit
can legally be waived. `git log --all` confirms both tokens arrived with the fold commit `5bc5b3f9`,
and that `tools/govkit/govkit.sh` has never been tracked at any revision — govkit's entrypoint is
`python tools/govkit/govkit.py selfcheck` per `tools/gate-legs.json`.

`TOOL-dRetiredFork-20` built this gate for exactly "a section 6 criterion whose witness path is not
tracked". It is doing its job; the fold walked into it. Section 7 then lists `codebase-map kit
selftest`, `codebase-map coverage + freshness`, `codebase-map adopter e2e`, `kit version markers`
and `lexicon naming predicates`, and never names the leg its own criteria red.

**Fix.** AC10: replace `bash tools/govkit/govkit.sh selfcheck` with the tracked invocation
`python tools/govkit/govkit.py selfcheck` and drop the "(or the kit's declared equivalent)" hedge —
`tools/gate-legs.json` already answers it. AC9: stop naming the new harness as a backticked path in
§6, since it is untracked until the unit lands; phrase it as "the harness S6 names is tracked by
`git ls-files`" and leave the literal path in S6 and §4, where the gate does not join. Add
`spec tokens (a spec's own names resolve)` to §7, and re-run `python tools/check-spec-tokens.py`
before ratifying.

**Left-shift gate.** The path half is already gated and was simply not run before ratification, so
the left-shift is timing, not code: run `check-spec-tokens.py` as a ratification step in the spec
DoR, or add it to the pre-commit fast leg scoped to the specs in the commit, so a fold cannot land a
red token and discover it at the push boundary. The genuinely new gate is the command half: grade a
backticked COMMAND token the way path tokens are graded, by joining its argv against the leg
manifest, so `bash …/govkit.sh` versus `python …/govkit.py` reds instead of reading fine.

---

## Highs

### H1 — unit 4: the binding resolution still names the field the same fold refuted

*`spec/…-4.md`, §8 the F1 RESOLVED block. Source ids 41, 31.*

The F1 resolution paragraph (`:253`) still reads "the de-duplication is measured from the live query
log's own `results` field". The same fold moved the measurement to `shown_paths` in §4 (`:93`), S8
(`:52-57`), AC1 (`:194-196`) and AC3 (`:201-203`), and the rev-3 log records why: "F1's resolution
named `results`, which is capped at five: two populations, neither answering the question".

Verified at source: `results` is truncated at `RESULT_CAP = 5` (`tools/memory-recall/query.py:136`,
emitted `:1241`) while `shown_paths` is the full ordered served list (`:1251`). The document now
names two different fields for one measurement — the exact two-populations defect round 1's H4 was
folded to close — and it names the wrong one in the block this repo's spec convention treats as the
owner's binding instruction. A note about the error in the revision log does not amend the block.

**Fix.** Rewrite the one clause in the F1 RESOLVED block to name `shown_paths` and the total
duplicate-path rate, with a bracketed rev-3 note recording that the resolution's original wording
said `results` and that S8 corrected the field. Leave the rest of the owner's decision verbatim.

**Left-shift gate.** A fold that refutes a named identifier must not leave it standing in the same
document: when a revision-log entry names a backticked identifier as superseded, grep the rest of
the spec for that identifier and red on a surviving occurrence outside the log. Cheap, mechanical,
and it retires this round's dominant class rather than this instance of it.

### H2 — unit 4: AC5 stays unsatisfiable after the unit it waits on lands

*`spec/…-4.md`, §6 AC5 and §4 "What settles it". Source id 14.*

AC5 runs `union.py <data-dir> tools/memory-recall/recall-fixture.json` "at a `--k` where
`records:fts5` alone scores below 1.000", while the criterion's own folded tail states that no `--k`
on the committed fixture leaves headroom. Unit 9's non-goals keep that fixture untouched and its F2
resolution puts the discriminating set in a SECOND file. So the deferral resolves to a run that
cannot produce the comparison even after its named unblocker ships.

§4 compounds it: "What settles it" describes the settling run as one over "the terms-carrying
fixture", which is unit 2's artifact per its AC4, not unit 9's.

**Fix.** Point AC5's `union.py` invocation at the discriminating fixture unit 9 produces, once unit
9 names it, and change §4 "What settles it" to say the run is over unit 9's set at a `k` with
headroom rather than over unit 2's terms-carrying fixture.

**Left-shift gate.** A criterion deferred to another unit must name the producing unit AND the
artifact, and the artifact must appear in that unit's Files-touched. That join is checkable from the
spec set alone and would also have caught round 1's H6 and this round's H2 at authoring time.

### H3 — unit 9: both resolutions cite the pre-renumber criteria, and now resolve to the wrong ones

*`spec/…-9.md`, §8, the F1 and F2 RESOLVED paragraphs. Source id 15.*

F1 credits "AC4's per-question `qid` traceability" and F2 rests on "AC5 makes safe: the existing
floor must still exit 0". Verified against the pre-fold text at `9df968f4`: criterion 4 WAS qid
traceability and criterion 5 WAS the existing-floor exit. The fold inserted a new AC2
(`extract_records`) and AC3 (ceilings), pushing traceability to AC5 and the floor to AC6, and left
both citations untouched.

This is worse than a dangling id. Both citations now resolve CLEANLY to different criteria, so
check 23 passes on them and the record of what the owner decided is quietly wrong. rev-3's own M1
note says §6 was relabelled precisely because "this spec's own resolutions cite AC1, AC4 and AC5" —
the renumber happened, the re-pointing did not.

**Fix.** Re-point the two citations to AC5 (qid traceability) and AC6 (the existing floor still
exits 0), and re-read every AC id in §5 and §8 against the new numbering in the same pass (see M1,
which is the rest of that sweep).

**Left-shift gate.** A commit that changes the numbering of a spec's §6 — count or order — must
touch every line in that file citing `AC<n>`, or red. It is a diff-shaped ratchet, needs no
semantics, and catches H3 and M1 together.

### H4 — unit 4: the "parent rollup" is a per-path cap for 99.3% of the served corpus

*`spec/…-4.md`, §4 "The parent key, verified at source" and "What the fallback costs". Source id 27.*

§4's design rests on chunk documents carrying `rec`. `extract_chunks` sets `rec` only when a heading
line ITSELF defines a record id, and `A_HEADING` requires `#{2,6}` — an H1 does not anchor, and a
bold-list or table anchor is never inspected. Re-measured independently over the tracked memory
corpus: 129 of 20 029 chunks (0.64%) carry `rec`, in 8 of 1324 files; the finding's 334 of 46 619
(0.7%) at the served 600-char width is the same fact at a different width.

So `hit["id"] or hit["path"]` is `hit["path"]` for the overwhelming majority of the chunk arm, and
what ships for this corpus is a per-path cap of 1 on that arm — not a best-chunk-per-parent rollup.
§4 presents the path key as the exception. S7's arm exercises only the rare branch, a synthetic
fixture "where one anchored record holds several matching chunks", certifying the mechanism the
served corpus takes roughly one time in 150.

One correction from synthesis: §3 rejects a per-path cap inside `rrf()` because it thins the RECORDS
arm too, which a chunk-arm-only collapse does not — so this is adjacent to the rejected shape, not
literally it. The measurement and the untested dominant branch stand.

**Fix.** State the measured share in §4, re-frame the path key as the operating mode rather than the
fallback, re-argue §3's rejection in that light, and add a second S7 arm over an UNANCHORED
synthetic file so the branch the corpus actually takes is the one observed.

**Left-shift gate.** Derive the share rather than authoring it: add an `extract`-side report printing
the anchored-chunk percentage over the tracked corpus, cite that command in §4 instead of a typed
figure, and require one test arm per branch the §4 argument names. A number typed beside the corpus
it describes is wrong on the next commit and nobody notices.

### H5 — unit 6: the withholding S7 was folded in for does not cover the install path adopters use

*`spec/…-6.md`, §2 S7, with §6 AC10 and §4 Files touched. Source id 37.*

S7 marks the harness `project-owned` in `tools/codebase-map/kit.toml`, which withholds it from
`govkit apply` and from nothing else. The precedent it copies says so in its own words:
`tools/memory-recall/kit.toml:13-15` — "NOTE THE SCOPE: this withholds them from `govkit apply`
only. The copy-install path WIRE-INTO-PROJECT.md documents is a plain `cp -r` of the kit dir and
does not read this file" — which is why that kit ALSO pays for an explicit `rm -f` step in
`WIRE-INTO-PROJECT.md` §3c step 1.

Codebase-map's §3b step 1 is `cp -r <gov-repo>/tools/codebase-map <project>/tools/codebase-map` with
no removal step, and the runbook tells adopters to refresh engine files "by overwriting from
<gov-repo> wholesale" (`WIRE-INTO-PROJECT.md:906`). So a harness that parses THIS repo's build
records still ships to every adopter, which is the outcome S7 exists to prevent. AC10 observes only
the apply, so nothing in the unit's acceptance can see the leak. Sibling unit 9's S5d covers both
carriers for the same mechanism in the same fold, which is the internal inconsistency.

**Fix.** Extend S7 to both carriers as unit 9 S5d does: the `kit.toml` role AND a removal step in
`WIRE-INTO-PROJECT.md` §3b step 1, plus the adopter inventory line at `WIRE-INTO-PROJECT.md:854`.
Add `WIRE-INTO-PROJECT.md` to Files touched, and give AC10 a second observation over the runbook
step rather than over `apply` alone.

**Left-shift gate.** `govkit selfcheck` asserts a descriptor's carve-outs today; extend it to assert
the OTHER carrier: every path a descriptor marks `project-owned` has a matching removal step in that
kit's `WIRE-INTO-PROJECT.md` copy-install section. Two carriers, one gate — the same shape as the
kit-version pair, which is already gated this way.

### H6 — unit 4: the version bump is load-bearing for AC9 and names none of its paired carriers

*`spec/…-4.md`, §4 Files touched, with §5 user docs and §7. Source id 40.*

`tools/check-kit-versions.sh:199-205` greps `KIT_MEMORY_RECALL_VERSION` out of `recall_conf.py` and
reds unless `gov:kit memory-recall@<v>` matches at `tools/memory-recall/README.md:3` (currently
`1.6`). Unit 4's Files touched offers only "in every carrier the govkit stamp check names" — no
check exists under that name; the pairing lives in `check-kit-versions.sh`, whose leg is
`kit version markers`, and nothing under `tools/govkit/` carries a stamp check. §5 then says the
user docs are unchanged, and §7 omits `kit version markers` while both siblings name it.

This repo has already paid for this on this exact pair. The aWalkedCorpus round-1 review's F9
(`memory/builds/aWalkedCorpus/reviews/2026-08-16-review-TOOL-aWalkedCorpus-1-1.md:65`) raised the
identical defect, with the identical remedy, as a high.

**Fix.** Add `tools/memory-recall/README.md` (the `gov:kit memory-recall@` marker) and
`tools/memory-recall/recall_conf.py` as explicit Files-touched rows, replace the "govkit stamp
check" pointer with `tools/check-kit-versions.sh`, add `kit version markers` to §7, and correct §5's
user-docs line to say the kit README marker moves with the bump.

**Left-shift gate.** Join the spec to the descriptor: a Files-touched path whose kit role is
`engine` obliges that kit's version constant AND its README marker to appear in the same
Files-touched list. The pairing is already machine-known to `check-kit-versions.sh`; this applies it
one stage earlier, at the spec, where the omission is cheap to fix.

### H7 — unit 9: no Files-touched, a false rollback line, and a version leg nothing feeds

*`spec/…-9.md`, §4 (no `### Files touched (estimate)` sub-head) and §5, against §7. Source id 1.*

Two independently verified points. §5 says "Rollback is deleting one file and one `kit.toml` rule",
which is false for the unit's own scope: S5c edits `tools/memory-recall/check-recall.py`, AC8
requires an arm in `tools/memory-recall/selftest.py`, and S5d edits `WIRE-INTO-PROJECT.md`. Only the
fixture and its `_README` are one file — `_README` is a key inside the fixture JSON, verified
against `tools/memory-recall/recall-fixture.json`.

And §7 names `kit version markers` as a leg that binds while no scope item, criterion or file list
produces the `KIT_MEMORY_RECALL_VERSION` move that S5c's edit obliges. Every sibling editing this
kit carries it explicitly — spec-2 S11, spec-4 §4 Migration, spec-5 S7 — and spec-2 S11 even
enumerates the units that carry it for this kit, with unit 9 absent from the list. The version bump
lands as a red bar at build time rather than as a planned edit, and this repo's own gotcha records
that one bump owes five carriers.

The weak half, stated for honesty: `memory/TEMPLATE-SPEC.md:182` calls `Files touched (estimate)` a
canonical sub-head to use "as needed", not a required one. The missing sub-head is a symptom; the
false rollback line and the unfed leg are the defect.

**Fix.** Add `### Files touched (estimate)` to §4 listing the real set (the new fixture,
`check-recall.py`, `selftest.py`, `kit.toml`, `WIRE-INTO-PROJECT.md`) plus the kit-version carriers,
add a criterion in the shape of unit 6's AC7 (`bash tools/check-kit-versions.sh` green with
`KIT_MEMORY_RECALL_VERSION` moved), and rewrite §5's rollback line to name the real revert set.

**Left-shift gate.** The §7 join described at M7 covers the unfed leg from the other direction: a leg
in §7 whose guard matches no Files-touched path is as much a defect as a Files-touched path whose
guard leg is missing. Grade both directions, the way `govkit selfcheck` grades its population.

---

## Mediums

### M1 — unit 9: the restored §5 carries three stale AC ids and one inverted hazard

*`spec/…-9.md`, §5 observability, migration/rollback and error/empty lines. Source id 17.*

rev-3's M7 says §5 was restored wholesale in this fold, so this is fresh text carrying pre-renumber
ids. The observability line's "AC4 makes every question traceable to the `qid`" is now AC5; the
migration line's "the committed fixture is untouched, which AC5 observes" is now AC6; and the
error/empty line's "AC2 reads that number" is now AC3, since AC2 runs `extract_records`.

The error/empty line has a second problem beyond numbering: it frames a sub-1.00 ceiling as the
failure state, while AC3 mandates a `records` ceiling of exactly 0.00. The hazard and the
requirement are now the same number, in the section a production-readiness reader trusts.

**Fix.** Re-point the three ids to AC5, AC6 and AC3, and rewrite the error/empty line to say the
state that matters is a CHUNKS ceiling below 1.00, since a 0.00 `records` ceiling is the property
AC3 requires.

**Left-shift gate.** Retired by H3's renumber ratchet — the same commit-shaped check catches every
`AC<n>` in the file, not only the ones in §8.

### M2 — unit 9: S2b's records-side filter cannot reject anything in the population AC3 mandates

*`spec/…-9.md`, §4 the S2b paragraph, against §6 AC2 and AC3. Source id 19.*

§4 justifies S2b's records-side filter by saying structural unsatisfiability "does not by itself
guarantee `records:fts5` scores below 1.000, since recall is measured per question over whatever
targets that question declares". Verified at source, that sentence is false for the population AC2
and AC3 mandate: `expected_by_target` records a target only `if hits`, so a question restricted to
S1 files yields an empty target set, and `score()` with empty `targets` sets `want = set()`, making
`r@k` exactly `0.0`. Under AC3 records scores 0.000 for every question, so S2b's "records:fts5 alone
fails" arm can never reject a candidate.

The charitable reading fails too. S2b's predicate is "records fails to RETRIEVE at `k`" while
`ceiling` counts RESOLVABILITY, so a question carrying an extra records-resolvable id can miss at
`k`, pass S2b, and still red AC3 — the arm does not secure AC3 in the non-compliant population
either. AC2 only requires a question to name AN `expected_paths` target in an unanchored file, which
still admits the mixed-target question AC3 reds on. One overstatement corrected: the S2b pass is not
wholly a no-op, its chunks arm still filters.

**Fix.** State in S1 and AC2 that EVERY declared target of a question must sit in an unanchored
file, drop the records-side half of S2b's filter and keep "`chunks:fts5` retrieves it", and replace
§4's justification with the `if hits` / empty-target-set mechanism, which is the real guarantee.

**Left-shift gate.** Fold this into B1's per-fixture audit: report per question, per set, whether
the target resolves at all, and red on a question whose targets resolve in the set the fixture is
supposed to discriminate against. A property argued in §4 prose is a property nobody can re-check;
the same claim as an audit row is.

### M3 — unit 6: AC2 pins two literals measured on a tree without this unit's own new file

*`spec/…-6.md`, §6 AC2. Source ids 22, 29.*

AC2 pins twelve names summing to fan-in 8 against twelve summing to 271, non-intersecting, measured
at base `c4fcf5ad`. Measured here at HEAD, both halves reproduce: the current neighbours sum to 8,
and the reordered top twelve are `main` 37, `read_text` 29, `key` 28, `run` 28, `resolve` 26,
`search` 23, `check` 19, `write` 19, `load_conf` 18, `write_text` 18, `repo_root` 13, `why` 13 = 271.

The coupling is at source. `map_lib.build_reference_index` (`:791`) walks the FILESYSTEM under the
top-level dirs of `symbols.json` filtered to their extension set, and `fan_in` (`:823`) counts
distinct referencing files minus the def file — so a new tracked `.py` under `tools/` is scanned.
S6/S7 commit exactly that: `tools/codebase-map/replay-phrases.py`, a harness that will reference
`main`, `run` and `read_text` among others. Injecting it as a referencing file for eight of the
twelve moves the sum 271 → 279; `main` alone moves it to 272. AC2 then fails at DoD for a reason
unrelated to the reorder, and the tempting exit is to retype the constant, which destroys the
measurement AC2 exists to hold.

**Fix.** Say the two numbers were measured at base `c4fcf5ad` with `replay-phrases.py` absent, and
restate the after-observation as the relation — the retained twelve are the twelve highest-fan-in
names in the pool and the two sets do not intersect — or require both halves to be run at one tree
state with the harness present.

**Left-shift gate.** A criterion pinning a derived numeric literal carries the sha it was measured
at, and the checker that reproduces it runs at that sha. This is the charter's "no count of a
derived population is written in prose" applied to acceptance criteria, where it currently is not.

### M4 — unit 6: AC10 names a command that has never existed

*`spec/…-6.md`, §6 AC10. Source ids 20, 32.*

`tools/govkit/govkit.sh` exists nowhere in the tree and `git log --all` returns nothing for it, so it
has never been tracked at any revision. The entrypoint is `tools/govkit/govkit.py` and the leg is
`govkit selfcheck` = `python tools/govkit/govkit.py selfcheck` per `tools/gate-legs.json`. The
criterion's hedge, "(or the kit's declared equivalent)", does not repair that — it invites a builder
to substitute whatever runs, so a wrong entrypoint passes the witness-token check on shape.

This is also the second of B2's two unwaivable `spec tokens` hits, and is fixed by the same edit.

**Fix.** Name `python tools/govkit/govkit.py selfcheck` and the apply command explicitly, and drop
the "declared equivalent" hedge — the leg manifest already answers what the equivalent is.

**Left-shift gate.** B2's command-token join: grade a backticked command in §6 against the leg
manifest's argv, so a criterion naming a runner the repo does not have reds instead of reading fine.

### M5 — unit 6: the ceiling AC9 adds can ship with its enforcement dead

*`spec/…-6.md`, §6 AC9, with §2 S8. Source id 42.*

AC9's observable half is `git ls-files` plus a PRINTED ceiling, and then it asserts "the runner that
owns it reds on a breach". No scope item creates that runner, no Files-touched row names it, and no
criterion observes the red. There is no runner in the kit to own it: `tools/codebase-map/` holds no
on-demand gate runner, and the precedent S8 cites works the other way round —
`tools/unattended/run-unattended-gates.sh` declares `BUDGET_*` per suite and reds on breach, so a
suite does not police its own budget there.

This is round 1's B3 shape one level down: the obligation the fold added is satisfiable by printing
a number, so the enforcing half can ship dead and nobody would know. The same spec requires AC1's
arm to be observed RED before it is written; AC9 asks for no such observation of its own.

**Fix.** State in S8 which component enforces — the script self-times and exits non-zero, or a named
runner does — add it to Files touched if it is new, and make AC9 observe the RED: with the ceiling
temporarily set below the measured wall clock the script exits non-zero, restored before landing.

**Left-shift gate.** A spec that introduces a ceiling, budget or threshold constant must carry a
criterion whose observation is a non-zero exit. Greppable from §6 alone, and it makes the charter's
"a new gate is not landed until its failing case has been observed" checkable at spec time rather
than remembered at build time.

### M6 — unit 6: the leg that grades the descriptor S7 edits is missing, and so are the regen artifacts

*`spec/…-6.md`, §7 with §4 Files touched. Source id 43.*

`govkit selfcheck` is a real, unguarded leg (`tools/gate-legs.json`, argv
`python tools/govkit/govkit.py selfcheck`) and it is the bar-side witness for AC10's property:
`govkit.py:1431-1434` fails an entry that "carves out '<src>' as project-owned and writes it
anyway". Unit 6 edits exactly that descriptor and invokes selfcheck by hand in AC10, yet §7 omits
it — while unit 4, which touches no descriptor, names it.

Separately, `WIRE-INTO-PROJECT.md:914` states that any move of `KIT_CODEBASE_MAP_VERSION` "owes one
`python <kit>/gen_map.py --write` in the same landing: the version rides `inventories.json`,
`MAP.md` and `symbols.json` as `codebase-map@<v>`, and the freshness gate byte-compares them". All
three carry `codebase-map@1.4` today. AC7 forces that bump, and the fold's "Six source files, plus
one record" tally names none of the three regenerated artifacts.

**Fix.** Add `govkit selfcheck` to §7, and add the `gen_map.py --write` regeneration of
`<MAP_ROOT>/generated/` to Files touched — or drop the typed "Six source files" count, which this
repo's own rule says not to write beside the list that owns it.

**Left-shift gate.** Same join as M7: derive §7's leg list from the Files-touched paths and the
manifest's guards, in both directions. A typed six is the smaller half of the same defect.

### M7 — unit 9: three grading legs missing, and S5c silently rewrites three existing arms

*`spec/…-9.md`, §7 with §2 S5c. Source ids 34, 44.*

§7 asserts `recall floor`, `memory hygiene` and `kit version markers` are "the legs that bind", and
that is wrong for this unit's own scope in three ways.

`recall floor arms` is the leg that runs `tools/memory-recall/test_recall_floor.py`, which S5c's
rewrite of `--audit-fixture` reaches directly — the suite drives that flag in five arms, three of
them passing an explicit `--fixture` (`:330`, `:350`, `:408`). "Iterate every fixture" written
without preserving the override at `:303` silently changes what those three assert.
`memory-recall kit selftest` owns AC8's arm, and §7 describes that leg's `GATE_SELFTESTS` behaviour
without ever naming it. `govkit selfcheck` grades S5d's carve-out and is the only bar-side witness
for AC9, and is absent entirely. A scoped run cannot be assembled from the list as written.

One sub-claim did NOT hold and is dropped: S5c's premise is accurate — the constant is what
`--audit-fixture` defaults to, and the bar's `recall floor` invocation passes no `--fixture`.

**Fix.** Name `recall floor arms`, `memory-recall kit selftest` and `govkit selfcheck` in §7, and
state in S5c that `--fixture` remains a single-fixture override while the no-argument form iterates
the kit's fixtures, so the existing arms keep their meaning. The Files-touched half is H7's.

**Left-shift gate.** Derive §7 rather than authoring it: join the spec's Files-touched paths against
each leg's `guard` in `tools/gate-legs.json` and red on a guarded leg the paths hit that §7 omits,
and on a §7 leg no path feeds. That single check retires H7, M6 and M7, and it is the same
"derive over author" the charter applies to every other list in this repo.

---

## What round 3 should carry

Three gates retire eleven of the sixteen defects, and none of them is exotic.

The renumber ratchet — a commit that changes §6's numbering must touch every `AC<n>` citation in the
file — retires H3 and M1, and would have caught round 1's M1 at authoring time.

The §7 join — derive the leg list from Files-touched against the manifest's guards, in both
directions — retires H6, H7, M6 and M7, and is the same defect round 1 raised twice under different
numbers.

The refuted-identifier grep — an identifier a revision log names as superseded must not survive
elsewhere in the same spec — retires H1, and is the mechanical form of the gotcha this repo already
writes down twice.

The residual risk this audit did NOT cover, unchanged from round 1: these are designs. Nothing here
says the three units build the right thing, only that each currently asks a builder to do two
contradictory things or to observe something that cannot fail. The parent measurement was taken as
given and not re-derived. The eight units that converged in round 1 were not re-read, so nothing
here says the fold left them intact — if the fold touched a shared claim in one of them, this pass
would not have seen it.
