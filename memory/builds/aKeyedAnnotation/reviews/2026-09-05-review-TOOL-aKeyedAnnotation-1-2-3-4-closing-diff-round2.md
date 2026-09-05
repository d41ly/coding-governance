**Serves:** diff-review TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4

# aKeyedAnnotation — Tier-2 CLOSING DIFF review, round 2

Node `a` · streams `tooling` · 2026-09-05 · adversarial fan → skeptic refutation → synthesis, per `memory/guides/REVIEW-PROTOCOL.md`. Four Tier-2 units, all CLOSED. This round reads the FIX, not the diff again: the base is round 1's tip, so the range is the fold commit alone.

**Reviewed range:** `b0e7dd4340bd8ef0b0c30ffcbcfaa1a2b4e2b8a1...HEAD` · ROUND 2

That sha does not resolve in this tree and the review was run against the one that does: the round-1 tip is `b0e7dd433f8e40289cf65b4ba7765c690bfd402e` and HEAD is `d53129af2872eef1262af2b7334fddd67e2fde77`, a one-commit range. The prefix `b0e7dd43` is common to both, so this is the orchestrator's sha carrier and not a different base — but a record in this build does not get to print an unresolvable sha silently, which is the whole subject of unit 1.

## Verdict: BLOCKED

One blocker, and it is the fold shipping a defect the round-1 diff did not have. `signal_source_cited_ids_with_no_record` — the entire deliverable of unit 3 — returns a hardcoded `"tolerance": 0`, and the display loop compares a report-only signal's value against `tolerance` rather than the resolved `pin`. So at HEAD the command prints `source_cited_ids_resolving_to_no_record 2 402 out of tolerance (report only)` while `PINS` declares that key's floor as exactly 2. The signal cannot print a calm status at its own declared floor, ever. The same file names this failure in prose two signals earlier — "Absent, it is 0 and every non-empty shard reads 'out of tolerance' — which trains a reader to skip the line" — and fixes it there and in `readme_mechanism_drift` by reading `ctx.pins`. The one signal this build wrote is the one that did not get the treatment.

It blocks rather than trails because a report-only signal's only product IS its status line. A signal that reads alarmed at its pin on day one is a line readers learn to skip, which is the same reassuring-zero family the build exists to close, arriving from the other direction. The fix is one line and there is a class version of it that is also one line.

The two highs are the round-1 repairs that did not finish. H1 is round 1's own blocker left with a regression arm that structurally cannot fail for it — the product code is correct at HEAD, verified by hand, and reverting the fix leaves the assertion green. H2 is the `_local_anchors` docstring: round 1 found a false assertion there, and the fold replaced it with a false explanation, measurably false, in the same sentence that cites the annotation guide's MUST NOT. Round 1 warned that six of its predecessors' fifteen defects were folds repairing one half of a statement and leaving the other standing. This fold did it twice more.

Nothing here argues against the build. No finding asks for a new grammar, signal, carrier or scope change, every fix is between one line and three, and the fold's product-code repairs are correct where they were made. The defects are in what the fold said about them and in what it left ungated.

## Review shape and run integrity

- Raw findings 21 · confirmed 12 · refuted 9 · unverified 0 · precision 0.57.
- Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates dropped by the pipeline. **The run is complete**: every lens and every skeptic batch came back, so a zero anywhere in this report is a measured zero and not an absence of coverage.
- Precision 0.57 is just above the ~0.5 floor §8 names and well down from round 1's 0.91. Read it the way §8 says: the surface is a single fold commit that four lenses had already been primed on, so the marginal lens spent its budget re-proposing things round 1 settled. Nine refutations on 21 raw is the cost of pointing a full fan at 406 lines. Next round on a surface this narrow takes fewer lenses, not more skeptics.

**Convergence, and the duplicates the pipeline did not drop.** The pipeline reports 0 duplicates because it dedupes by identity, not by defect. The 12 confirmed findings describe **8 distinct defects**: four pairs are the same defect found twice from different directions. Raw 3 and 6 are both `_ID_SHAPE`; 4 and 12 are both the ungated `decisions:` arm; 5 and 16 are both the `_local_anchors` docstring; 11 and 18 are both the `EVIDENCE_GLOBS` fixture escape. Every raw id is named in the table's last column, so nothing is silently absorbed, and the merged rows are strictly stronger than either half — raw 6 supplies the adopter-override path that raw 3 missed, and raw 12 supplies the `git show d53129af^` proof that raw 4 only asserted.

Every measurement in this report was re-run against HEAD in this worktree before it was written down. Where a finding claimed a number, the number is the one the command printed here.

## Findings

| # | Severity | Unit | Address | Defect | Raw ids |
|---|---|---|---|---|---|
| B1 | blocker | `-3` | `tools/drift-audit/drift_report.py:1669` | The signal hardcodes `"tolerance": 0` and the report-only display branch compares against `tolerance`, not the resolved `pin` — so unit 3's signal prints "out of tolerance" at its pinned value on every run | 7 |
| H1 | high | `-4` | `tools/codebase-map/selftest.py:1023` | Round 1's blocker and its high were fixed in product code and left ungated: the only `decisions:` assertion rides the one path the blocker never touched, so reverting the fix leaves the arm green | 4, 12 |
| H2 | high | `-2` | `tools/drift-audit/drift_report.py:500` | The repaired `_local_anchors` docstring withdrew a false assertion and replaced it with a false explanation — it blames the multiline flag, and the flags are equal because `_grammar_anchors` already normalises them | 5, 16 |
| M1 | medium | `-4` | `tools/codebase-map/reuse_lookup.py:73` | `_ID_SHAPE` is a hand-retyped byte-copy of `map_lib.DEFAULT_DECISION_ID_RE` in a module that already imports `map_lib`, with nothing comparing the pair and the copy dropping ids silently | 3, 6 |
| M2 | medium | `-2` | `tools/drift-audit/drift_signals.py:87` | The comment says the edit repairs "the gate-the-instance-not-the-class shape" and the edit adds four more instances; two fixtures survive, one carrying 12 real ids inside the evidence population | 11, 18 |
| L1 | low | `-2` | `tools/drift-audit/drift_report.py:551` | The `_families_of` comment says a discipline-free `FAMILIES` entry is dropped by both readers; both admit it, and the fold changed the behaviour in the opposite direction in the same hunk | 8 |
| L2 | low | `-4` | `tools/codebase-map/reuse_lookup.py:69` | "MULTI-LINE and COMMENTED arrays are legal TOML and this corpus has both" — the corpus has neither, in the build that shipped the rule banning unobserved assertions | 20 |
| L3 | low | `-2` | `memory/builds/aKeyedAnnotation/build/2026-09-05-build-TOOL-aKeyedAnnotation-2-acceptance.md:25` | AC5 attributes the movement of BOTH population figures to the glob narrowing; the judgeable population is counted before any glob is read and cannot move for that reason | 21 |

---

## B1 — blocker — unit 3's signal cannot print a calm status at its own pin

**`tools/drift-audit/drift_report.py:1669`** (the signal), with the reachable class fix at **`tools/drift-audit/drift_report.py:1826`** (the display branch).

`signal_source_cited_ids_with_no_record` returns `"tolerance": 0, "gateable": False`. The display loop resolves a pin for every signal at line 1805 (`s["pin"] = ctx.pins.get(s["signal"], s["tolerance"])`), then consults it only on the gateable branches at 1822 and 1825. Line 1826 is the report-only branch and it reads `s["value"] > s["tolerance"]`. The pin never reaches the status of a report-only signal.

Reproduced at HEAD in this worktree:

```
source_cited_ids_resolving_to_no_record                2    402  out of tolerance (report only)
```

`PINS` declares `2` for that key. The signal is at its floor and says it is over its bar.

This is not a novel class in this file, which is what makes it a blocker rather than a medium. `live_backlog_rows_per_shard` sets `"tolerance": ctx.pins.get(...)` at line 1295, and the comment above it names this exact reader-training failure. `readme_mechanism_drift` does the same at line 1497. Unit 3's own signal, written after both, kept the literal.

**Fix.** Two shapes, and the second is the root cause:

- Local: in the signal's return, `"tolerance": ctx.pins.get(name, 0)`, matching 1295 and 1497.
- Class, one line at 1826: `elif s["value"] > s["pin"]:`. Because `pin` already falls back to `tolerance` when no pin exists, this is identical for every signal without one and correct for every signal with one. I measured the blast radius: across all 13 signals at HEAD, exactly one has `pin != tolerance` on a report-only signal, and it is this one. Nothing else moves.

Take the class fix. The local fix leaves the next report-only signal that grows a pin to rediscover this.

**Left-shift gate.** An arm in `tools/drift-audit/selftest.py` asserting the invariant rather than the instance: for every signal in `SIGNALS` where `gateable` is False and a `PINS` entry exists, a value equal to the pin renders `ok`, not `out of tolerance`. Stage the break by reverting 1826 to `tolerance` and confirm RED before landing — §7's rule, and the one that would have caught this at the commit that wrote it.

---

## H1 — high — the blocker's fix is standing behind a gate that cannot fail for it

**`tools/codebase-map/selftest.py:1023`**

Round 1's B1 (the synthetic `<feature> (## Shared seams)` candidate never printing its own ids) and H1 (two dossiers declaring one seam, ids printing under the wrong label) were both repaired in `reuse_lookup.py`. Neither got an arm. The fold did not touch `tools/codebase-map/selftest.py` at all.

The one assertion on the clause is line 1023, `assert "decisions: ARCH-aSeeded-1 ARCH-aSeeded-2" in out`, and it is satisfied by the `slugify` candidate. `text.md` declares seam `slugify`, so `load_corpus` merges it with `detail='text'` and the ids resolve under that label — the affordance-seam path, which worked before the fold. `assemble_shortlist` (`reuse_lookup.py:252-261`) builds the synthetic candidate only when a feature has no affordance seams, which in this fixture is `glue.md` alone, and `glue.md` (`selftest.py:987-990`) has no toml fence at all, so it declares no `decisions`. The assertion at 1035 on `glue (## Shared seams)` checks the name and nothing else.

I confirmed against `git show d53129af^:tools/codebase-map/reuse_lookup.py`: the pre-fold source passes `decisions=decisions` into the per-`Candidate` field. Restoring that leaves line 1023 green while re-opening round 1's blocker verbatim. H1 is unguarded the same way — no two fixture dossiers declare the same seam name, so the last-write collision has no arm either.

The behaviour is correct at HEAD; I checked by hand. This is uncovered, not broken. But §7 states it exactly: gate the CLASS, not the instance. Fixing both paths and exercising one certifies coverage that does not exist, and it is a Definition-of-Done item on a blocker.

**Fix.** Two lines of fixture front matter and one assert, plus a third dossier:

- Give `glue.md` a toml fence with `decisions = ["ARCH-aGlue-9"]` and assert `"decisions: ARCH-aGlue-9" in out3` beside the existing name check.
- Add a third dossier declaring seam `slugify` with different ids, and assert the printed ids match the dossier named in the label.

**Left-shift gate.** Those two asserts ARE the gate. Stage each break in turn — restore the per-`Candidate` field for B1, restore the independent `or` for H1 — and confirm RED for each before landing. A gate whose failing case has not been observed is an assertion about nothing.

---

## H2 — high — the false assertion was withdrawn and a false explanation put in its place

**`tools/drift-audit/drift_report.py:500`**

The repaired docstring says the anchor patterns are not byte-compared "because the extractor builds them without the multiline flag this module needs and the two `.pattern` strings are therefore not equal". Measured at HEAD by building both tuples in this worktree:

```
flags   [(40, 40), (40, 40), (40, 40), (40, 40)]
pat_eq  [True, False, True, False]
```

Three things are wrong at once. The flags are equal — `_grammar_anchors` re-compiles the extractor's anchors as `re.compile(a.pattern, a.flags | re.M)` at line 519, which is the module's own proof that the flag is not an obstacle. Flags cannot reach `.pattern` in any case. And half the patterns ARE byte-equal already; anchors 1 and 3 differ only because the local copy spells the joiner classes as `[-—:·]` and `[·|]` where `extract.py` writes the literal `[-—:·]` and `[·|]`.

So the sentence steers the next reader at `re.M` instead of at an escape-spelling difference that a one-line change closes. It makes a comparable pair read as structurally uncomparable, in the docstring that cites the annotation guide's MUST NOT against an assertion with no observation behind it. This is the half of the module every adopter without the recall kit actually runs.

**Fix.** Either state the measured reason — the two spellings differ only in how the delimiter characters are escaped in source — or close the gap: spell the local classes with the literal characters and add the anchor-tuple compare beside the ident one in `test_local_grammar_matches_the_extractor`. The kit already compares `_local_ident(families)` against `grammar_for(root).ID` as plain strings at `selftest.py:1837`; an anchor arm is the same shape and two lines.

**Left-shift gate.** Close it rather than annotate it: extend `test_local_grammar_matches_the_extractor` to compare all four `.pattern` strings, which turns the docstring's excuse into a passing arm and deletes the sentence entirely. If the escapes are kept, the compensating check is a documented one and belongs in the kit descriptor, because an exemption is not coverage.

---

## M1 — medium — one grammar, two spellings, nothing comparing them

**`tools/codebase-map/reuse_lookup.py:73`**

`_ID_SHAPE = re.compile(r"^[A-Z][A-Z0-9]{1,11}-[A-Za-z0-9][A-Za-z0-9-]*$")` is character-for-character `map_lib.py:69`'s `DEFAULT_DECISION_ID_RE`, in a module that does `import map_lib as m` at line 50 and already reads `m.SEAM_FANIN_THRESHOLD_DEFAULT` at class-body level. Verified byte-identical; grep shows `_ID_SHAPE` declared and used only here, with nothing comparing the pair.

The asymmetry is the impact. `map_lib.parse_dossier` raises `MapError` on an id missing the pattern — fail loud, the authority. `_dossier_decisions` filters against the copy and drops non-matching tokens SILENTLY, with no liveness assertion. Two live divergence paths: widen the authority for a new id era and every dossier still parses green while the reuse audit quietly stops printing those ids; or let an adopter override `DECISION_ID_RE` in `map_extractors.py`, the mechanism `map_extractors.template.py:113` advertises — the validate path honours it, the render path does not, so a dossier that validates green renders with its `decisions:` line truncated or absent.

This is the reassuring-zero class, and it is the defect unit 2 of this build fixed in `drift_report.py` under the heading "ONE GRAMMAR, AND IT IS THE RECALL EXTRACTOR'S", reintroduced one kit over.

The portability header is not a defence: `DEFAULT_DECISION_ID_RE` lives in `map_lib`, which is kit code, not the project-side `map_extractors` layer this module refuses.

**Fix.** `_ID_SHAPE = m.DEFAULT_DECISION_ID_RE`. One line, deletes the copy, module stays project-layer-free.

**Left-shift gate.** After the one-liner there is nothing left to drift, which is the point — the copy is the whole defect and deleting it makes the class structurally impossible. If the copy is kept for any reason, it needs a `.pattern` byte-compare arm in `tools/codebase-map/selftest.py` and that arm must be observed RED against a deliberately widened `DEFAULT_DECISION_ID_RE`.

---

## M2 — medium — four more instances, offered as a class fix

**`tools/drift-audit/drift_signals.py:87`**

The comment added by the fold says the three prior exclusions "name three spellings of 'a test file' and left every fixture tree inside the population this list exists to narrow, which is the gate-the-instance-not-the-class shape". It then adds four more literal path patterns.

Measured at HEAD. Resolving the declaration through `git ls-files` with all seven exclusions returns exactly 177 files, matching the signal's own `evidence_files: 177`, and two fixtures survive:

- `tools/memory-recall/recall-fixture.json` — a graded question set keyed on record ids by its own `_README`, carrying 12 distinct `TOOL-*` id citations.
- `tools/unattended/playbook.fixture.template.md` — whose rendered sibling `playbook.fixture.md` IS excluded; the pattern misses the `.template.md` variant of the same file.

Signal 2 is `gateable: True` at tolerance 0 with pin 2, and its citation scan is a plain `git grep -l -w -F <id> -- <evidence_globs>`. So a non-terminal spec whose id appears in the recall fixture's `expected_ids` reads as demonstrably shipped: the house's bookkeeping certifying the bookkeeping, which is the exact hole the exclusion list exists to close.

Latent today, and I say so plainly: all 12 fixture ids belong to CLOSED specs, and the two live suspects are certified by genuine product source, so no verdict moves at HEAD. That is the same latency round 1's M3 was confirmed under. The list's stated policy is to narrow before it costs something.

**Fix.** Replace `:(exclude)*/fixtures/*`, `:(exclude)*/fixture-*/*` and `:(exclude)*.fixture.md` with the single `:(exclude)*fixture*`. Measured here: the population goes 177 → 175, removing exactly those two files and adding nothing. Re-measure and note the reading in the same commit, as the comment already promises.

**Left-shift gate.** A `tools/drift-audit/selftest.py` arm that resolves `EVIDENCE_GLOBS` in a fixture tree containing a file with `fixture` in its path and asserts it is absent from the population. Run the candidate predicate over the real tree printing hits AND near-misses before wiring it, per §7 — that is how the two survivors were found, and it is cheap.

---

## L1 — low — a validation rule stated beside code that does not have it

**`tools/drift-audit/drift_report.py:551`**

The comment says a discipline-free `FAMILIES` entry and a token carrying a regex metacharacter "are both dropped rather than one being silently admitted here and rejected there". Measured on both implementations:

```
_families_of({'FAMILIES': 'PLAY KICK'})       -> ('PLAY', 'KICK')
_families_of({'FAMILIES': 'a:PL*AY b:KICK'})  -> ('KICK',)
```

`recall_conf.py:257`'s comprehension agrees on both. Only the metacharacter token is dropped; a bare family is admitted by both readers.

The parity fix itself is correct — the two readers do agree, which is what the change bought. The claim beside it is not. And it is backwards as a description of the change: `git show d53129af` shows the fold replaced `if ":" not in pair: continue` with `rpartition(":")[2]` plus a shape check in the same hunk that added this comment, so bare families went from dropped to admitted while the new prose says they are refused.

**Fix.** Restate what was measured: a token whose part after the last colon is not family-shaped is dropped by both readers; a token with no discipline half is accepted by both, and that agreement is what the change buys.

**Left-shift gate.** None warranted — this is a prose defect on correct code. It joins the A3 documented check below with the other three.

---

## L2 — low — "this corpus has both", and it has neither

**`tools/codebase-map/reuse_lookup.py:69`**

The comment asserts "MULTI-LINE and COMMENTED arrays are legal TOML and this corpus has both", and states the mis-parse in the past tense.

Measured at HEAD, both halves. Across all 21 dossiers plus `FOUNDATION.md`, every `decisions` array is single-line and none contains a `#`. Widening the scan: no tracked TOML file in the repo has any array body containing `#`, under any reading of "this corpus". Multi-line arrays exist, but only for other keys. The one commented `decisions` line was `gen_map.py:76`'s scaffold, whose `#` sat outside the closing bracket and so never entered `_DECISIONS_RE`'s capture — and `d53129af` deleted it in the same commit that wrote this comment.

The hardening is right and the past-tense mis-parse description is backed by round 1's constructed input. The false clause is the observational one, and it is the A3 violation this build exists to stop, shipped for the fourth time inside the same range.

**Fix.** "Multi-line and commented arrays are legal TOML and no live dossier uses either yet, so the body is stripped and shape-checked before the split rather than after the first one appears."

**Left-shift gate.** Ungateable as stated — no checker reads English for observational claims. It joins the documented check below.

---

## L3 — low — a repaired number with a false cause attached

**`memory/builds/aKeyedAnnotation/build/2026-09-05-build-TOOL-aKeyedAnnotation-2-acceptance.md:25`**

AC5's replacement sentence says the two population figures "moved once during this build, when the closing review found the narrowing named three test-file spellings and left every fixture DIRECTORY inside the population". The judgeable population cannot move for that reason, and `drift_report.py:611` says so in the module the ledger describes: `checked` counts non-terminal keyed specs and is computed before any glob is read. Only `evidence_files` (186 → 177) moved with the narrowing.

Measured per commit: the judgeable population was 66 at the ledger commit and already 64 at `d53129af`. It fell because three of this build's own specs reached a terminal status, at `acfc7f73` and `9dd9629e` and at spec 2's own closure — not at the fold that narrowed the globs. False causally and false temporally.

**Fix.** Split the clause: the evidence-file count moved with the narrowing, the judgeable population moved as this build's specs closed.

**Left-shift gate.** Ungateable — it is a causal claim in a records file. Documented check below.

---

## Left-shift ledger

| Finding | Left-shift | Where |
|---|---|---|
| B1 | Invariant arm: every report-only signal with a `PINS` entry renders `ok` at its pin. Observe RED by reverting the display branch | `tools/drift-audit/selftest.py` |
| H1 | Fixture arms for both round-1 defects: a synthetic-candidate dossier that declares ids, and two dossiers declaring one seam. Observe RED by restoring each pre-fold form | `tools/codebase-map/selftest.py` |
| H2 | Extend the existing ident byte-compare to the four anchor `.pattern` strings, after normalising the escape spellings | `tools/drift-audit/selftest.py:1837` |
| M1 | Structural: deleting the copy makes the class impossible. No gate needed once the one-liner lands | `tools/codebase-map/reuse_lookup.py:73` |
| M2 | Arm asserting a `fixture`-named path is absent from the resolved evidence population; run the predicate over the real tree first | `tools/drift-audit/selftest.py` |
| L1, L2, L3 | DOCUMENTED CHECK, not a gate: no checker reads prose for unobserved assertions or false causes. The A3/A4 classes stay a Tier-2 checklist item — read every annotation the diff touches and ask what observation stands behind it | §10 checklist |

Four of the eight defects are ungateable prose or are already gated by their own deletion. That ratio is itself the finding: this build shipped a rule about annotation honesty and the only enforcement it has is a human reading the diff, which is exactly how three of the four got through the fold.

## What the fold got right

Round 1's fourteen fixes: twelve are correct as landed and are not re-reported here. The product-code repairs in `reuse_lookup.py` (the seam-merge carrier, the multi-line array parse, the synthetic candidate's ids), in `drift_report.py` (the `checked` guard ordering) and in `gen_map.py` (the misplaced honesty comment) all hold under direct test. The two that did not finish are H1 and H2 above, and in both cases the code half landed and the gate or the sentence did not.

The nine refuted findings are not listed individually; none survived a skeptic and none was a near-miss worth carrying forward. Precision 0.57 on a 406-line surface is the signal that this round was one lens too wide, which is a note for the next closing review rather than a defect in this one.
