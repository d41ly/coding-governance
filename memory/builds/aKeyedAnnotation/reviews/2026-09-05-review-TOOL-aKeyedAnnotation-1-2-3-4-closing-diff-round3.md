**Serves:** diff-review TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4

# aKeyedAnnotation — Tier-2 CLOSING DIFF review, round 3

Node `a` · streams `tooling` · 2026-09-05 · adversarial fan → skeptic refutation → synthesis, per `memory/guides/REVIEW-PROTOCOL.md`. Four Tier-2 units, all CLOSED. This round reads the round-2 FOLD and nothing before it: the base is round 2's tip, so the range is one commit.

**Reviewed range:** `d53129af2872eef1262af2b7334fddd67e2fde77...HEAD` · ROUND 3

The base resolves in this tree, HEAD is `504533fb40327898c66347f5d6ded88b832c97f7`, and `git log` over the range returns exactly one commit touching 12 files (+289/-26). Round 2's record had to note that its printed base did not resolve; this one does, and the note is here so the next reader knows the check was made rather than skipped.

## Verdict: BLOCKED

One blocker, and unlike round 2's it is not in product code at all — the build's own README breaches a slot ceiling, so an UNGUARDED merge-bar leg is red at HEAD. `python tools/memory-tree/gen_build_index.py --check-format` exits 1 on a clean tree and names one file: `memory/builds/aKeyedAnnotation/README.md`, slot `## Expected improvements`, 777 B against a declared 500 B ceiling. The leg carries no `guard` key in `tools/gate-legs.json`, so it runs on every bar including the full one this build owes at close. The merge cannot land until the slot fits. The prose that overflows it arrived in `b0e7dd43`, before this round's base — the fold did not write it, but the fold edited that file and reported gates green over it, and so did the fold before that.

The three highs are all the same shape the build was convened to close, arriving one round later. Two are annotations the tree refutes at the commit that writes them: the new `_ID_SHAPE` comment claims it picks up an adopter override through a module that deliberately imports no project layer, and the collapsed `EVIDENCE_GLOBS` comment claims one substring predicate covers every excluded spelling while a tracked file walks back into the population it just narrowed. The third is the absent left-shift: the fold gave the codebase-map repair a regression arm and gave neither drift-audit repair one, including the arm round 2 prescribed in writing for its own blocker. `tools/drift-audit/selftest.py` is not in the diff.

The two mediums are the fold's stale sibling carriers: a comment that still states the pre-fold comparison rule and cites as its proof the loop that now refutes it, and a status branch whose predicate moved to the pin while its wording and its silent fall-through did not.

Nothing here argues against the build. Every fix is between one line and a small test arm, no finding asks for a new grammar, signal, carrier or scope change, and every product-code repair the fold made is correct where it was made. As in round 2, the defects are in what the fold said about its repairs and in what it left ungated — plus one record that has been red on the bar for three rounds while three folds called the bar green.

## Review shape and run integrity

- Raw findings 18 · confirmed 16 · refuted 2 · unverified 0 · precision 0.89.
- Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates dropped by the pipeline. **The run is complete**: every lens and every skeptic batch came back, so a zero anywhere in this report is a measured zero and not an absence of coverage.
- Precision 0.89 is back near round 1's 0.91 and well up from round 2's 0.57. Read it as narrow-surface behaviour rather than as a quality signal: 18 raw findings over a 406-line fold, from a fan already primed by two rounds on the same code, means the lenses converged on the same short list rather than that they searched harder. The refutation rate falling while the DISTINCT defect count also falls is the convergence claim, and it is the count below that carries it.

**Convergence, and the duplicates the pipeline did not drop.** The pipeline reports 0 duplicates because it dedupes by identity, not by defect. The 16 confirmed findings describe **6 distinct defects**. Raw 1, 6, 11 and 16 are all the `_ID_SHAPE` comment. Raw 2, 7, 12 and 17 are all the `EVIDENCE_GLOBS` collapse. Raw 3, 9 and 13 are all the stale `tolerance` comment. Raw 14 and 18 are both the report-only status string. Raw 8 and 15 are both the missing drift-audit regression arm, from opposite ends — 8 from the blocker that has no arm, 15 from the selftest file that has no diff. Every raw id is named in the table's last column, so nothing is absorbed silently, and each merged row is stronger than any of its halves: raw 12 supplies the `git show` proof of the deleted exclusion, raw 17 supplies the two-out-one-in population measurement that explains why a net `-1` read as a clean narrowing, and raw 15 supplies the asymmetry against the codebase-map arm that raw 8 only implies.

Round over round the distinct-defect count runs 14 → 8 → 6, and blockers 2 → 1 → 1. The loop is converging on defect count. It is not converging on defect CLASS: the dominant class named at the top of every round — one carrier of a fact repaired, a sibling carrier left stating the old one, or an assertion the tree refutes — accounts for 4 of this round's 6, exactly as it accounted for 4 of round 2's 8. Three of those four are in comments the fold WROTE, not comments it inherited. The class is not being reduced by folding; it is being reproduced by folding, which is the argument for the gate suggestions below rather than for a round 4 of the same shape.

Every measurement in this report was re-run against HEAD in this worktree before it was written down. Where a finding claimed a number, the number below is the one the command printed here.

## Findings

| # | Sev | Where | Defect | Raw ids |
|---|-----|-------|--------|---------|
| B1 | blocker | `memory/builds/aKeyedAnnotation/README.md:22` | Slot `## Expected improvements` is 777 B against its 500 B ceiling; the unguarded `build README slot contract` leg is RED at HEAD | 10 |
| H1 | high | `tools/codebase-map/reuse_lookup.py:79` | The new `_ID_SHAPE` comment claims it picks up a project override; the module imports no project layer and cannot | 1, 6, 11, 16 |
| H2 | high | `tools/drift-audit/drift_signals.py:93` | The four-into-one exclusion collapse silently dropped `*.test-template.py`, re-admitting a test file to signal 2's evidence population, under a comment claiming total coverage | 2, 7, 12, 17 |
| H3 | high | `tools/drift-audit/selftest.py` (absent from the diff) | Both drift-audit fixes landed with no regression arm, including the one round 2 prescribed in writing for its own blocker | 8, 15 |
| M1 | medium | `tools/drift-audit/drift_report.py:1296` | The sibling comment still states the pre-fold comparison rule and cites the loop that now refutes it; the workaround it justifies is now dead | 3, 9, 13 |
| M2 | medium | `tools/drift-audit/drift_report.py:1831` | The report-only branch moved to the pin but kept its old wording and falls through to a bare `ok`, hiding a live pinned residue | 14, 18 |

---

### B1 — blocker — `memory/builds/aKeyedAnnotation/README.md:22`

**The build's own README fails an unguarded merge-bar leg, so the full bar this build runs at close will red and the merge cannot land.**

Reproduced on a clean tree (`git status --porcelain` empty) at HEAD:

```
python tools/memory-tree/gen_build_index.py --check-format   # RC=1
  build-index FORMAT — authored content outside the slot contract:
    memory/builds/aKeyedAnnotation/README.md — slot `## Expected improvements` is 777 B over its declared ceiling of 500 B
```

That is the only FORMAT block in the output; everything else the command prints is ADVISORY, and the two advisory rows belong to a different build. Measured directly, the slot body is 777 B stripped against a 500 B ceiling — 277 B over. The leg is real and unguarded: `tools/gate-legs.json` carries `{"name": "build README slot contract", "argv": ["python3", "tools/memory-tree/gen_build_index.py", "--check-format"], "chunk": "records", "subject": "repo", "ceiling": 300}` with no `guard` key, so it runs on every bar including diff-scoped ones.

The overflow is the first bullet, 492 B on its own, added by `b0e7dd43` — before this round's base. The fold did not cause it. What the fold did do is touch that file, and report green. So did the round-1 fold. A red unguarded leg surviving three rounds of "gates green" is the more interesting half of this finding.

**Fix.** Delete or compress the first bullet of `## Expected improvements` until the slot measures ≤500 B; dropping it outright leaves ~285 B. Its content — that two source citations shipped repaired where the design pass had measured one — already lives in the unit-1 acceptance record, which is where a build-level narrative of that length belongs. Then re-run `--check-format` and confirm RC=0. Do NOT raise the ceiling instead: that is a RATCHETS-governed weakening and owes an `<old> -> <new>` justification.

**Left-shift.** The gate already exists and already fires; what failed is that three folds reported green without running it. The left-shift is therefore not a new leg but a Definition-of-Done arm: the unattended driver's per-fold verify step must run the unguarded `subject = repo` legs of the chunk it touched, not only the diff-scoped ones. Concretely — a fold that edits any file under `memory/builds/` runs `gen_build_index.py --check-format` and refuses to report gates green on RC≠0. That is one line in the fold's own verify list and it converts this class from "found in round 3" to "found at fold time".

---

### H1 — high — `tools/codebase-map/reuse_lookup.py:79`

**The new comment asserts a mechanism the tree does not contain, in the build that shipped the rule against assertions with no observation behind them.**

The sentence is: *"Taking it from the module also picks up a project override where one is declared, where a copy silently would not."* It does not. The declared override channel is `map_extractors.DECISION_ID_RE`, advertised at `map_extractors.template.py:115` and named by `map_lib.py`'s own comment on the default ("override with a project grammar in map_extractors"). Every other consumer resolves it as `getattr(ext, "DECISION_ID_RE", m.DEFAULT_DECISION_ID_RE)` — `gen_map.py:39`, `map_diff.py:260`, `test_codebase_map.py:71`. `reuse_lookup.py` imports only `map_lib as m` and its own docstring, twelve lines above the comment, states it needs NO project `map_extractors.py`; `selftest.py` pins that premise with `assert not (tmp / "map_extractors.py").exists()`. So `_ID_SHAPE = m.DEFAULT_DECISION_ID_RE` binds the kit FALLBACK — precisely the value an override replaces — and nothing rebinds that constant anywhere in the tree.

The consequence is the asymmetry round 2 named and this comment claims to have closed. `_dossier_decisions` returns `tuple(t for t in toks if _ID_SHAPE.match(t))`: it DROPS what it does not match, where the validate path raises. An adopter that widens `DECISION_ID_RE` gets ids admitted by `gen_map` and silently absent from the `decisions:` clause of the reuse shortlist; an adopter that narrows it gets ids here that the rest of the kit rejects. In this repo the two are identical (`map_extractors.py:242` assigns the default), so nothing is observable today and nothing can red when that stops being true.

The de-duplication itself is correct and should stay — the retyped byte-identical copy was a real second reader of one rule with nothing comparing the pair.

**Fix.** Delete the override clause. Say what is true: this reader takes the kit DEFAULT grammar because the module carries no project layer, an adopter's `map_extractors.DECISION_ID_RE` is not seen here, and a project that widens it loses ids from the shortlist in silence. If the divergence is to be closed rather than documented, resolve `DECISION_ID_RE` from `map_extractors` where importable with `m.DEFAULT_DECISION_ID_RE` as the fallback — that keeps the no-project-layer premise the header asserts and the selftest pins. Do not leave the sentence claiming a resolution the module cannot perform.

**Left-shift.** This is the third annotation in this build refuted by the tree it sits in, and the class is gateable in one narrow form: an assertion about IMPORTS is checkable from the module's own import set. Add a codebase-map selftest arm asserting that `reuse_lookup.py` imports no project layer AND that no comment in it names `map_extractors` outside the docstring clause that declares the module does not need one. Broader and cheaper, and the one that would have caught all three: extend the annotation-style checker this build shipped with a lint for comment sentences making a capability claim (`picks up`, `also reads`, `covers every`, `resolves`) about a symbol the file does not import. Run it over the real tree first and print hits AND near-misses before wiring it, per §7.

---

### H2 — high — `tools/drift-audit/drift_signals.py:93`

**Collapsing four exclusions into `:(exclude)*fixture*` dropped one that was never a fixture spelling, re-admitting a test file to the evidence population — under a comment asserting the opposite.**

Measured at HEAD against the real `EVIDENCE_GLOBS` list:

```
git ls-files -- tools skills .claude memory/guides/SESSION-KICKOFF.md \
  coding-governance-agents.template.md WIRE-INTO-PROJECT.md \
  ':(exclude)*.test.sh' ':(exclude)*/selftest.py' ':(exclude)*/test_*.py' ':(exclude)*fixture*'
  → 176 files
  … with ':(exclude)*.test-template.py' restored → 175 files
  the delta → tools/pytest-parallel-guardrails/aiosqlite_worker_resilience.test-template.py
```

`git show 504533fb -- tools/drift-audit/drift_signals.py` deletes four literal excludes — `*/fixtures/*`, `*/fixture-*/*`, `*.fixture.md` and `*.test-template.py` — and adds one. Three were fixture spellings. The fourth was a TEST spelling, and `*fixture*` cannot match it; neither can the three test predicates above it, because that file is deliberately named off pytest's `test_*.py` glob (its own docstring says so). It was excluded before the fold and is inside the population after it. The net count moved by one because two fixture files left and this one came back, which is why a two-out-one-in regression read as a clean narrowing in a re-measurement.

The comment three lines up asserts the single predicate *"covers every spelling the tree uses now and every one it grows later"*, which a tracked file refutes at the commit that writes it, and describes what it deleted as *"four more literal spellings of 'a fixture'"*, which is wrong for one of the four. That mis-description is the mechanism by which the loss is invisible in the diff.

Runtime impact is latent and this finding says so: the template carries zero id-shaped tokens today, so `non_terminal_specs_cited_by_product_source` still reads 2 of 64 and AC5 of the unit-2 acceptance record holds. But that signal is `gateable: True` with pin 2, and the block's own header says a citation from a test file is *the house's own bookkeeping certifying the bookkeeping*. The first spec id written into a shipped test template would count as shipment evidence and could push a gateable signal over its pin — a false RED sourced from exactly the class this list exists to exclude. The exclusion existed so that "it happens to cite nothing" would not have to be true.

**Fix.** Keep `:(exclude)*fixture*` and restore a test-template predicate beside it — `":(exclude)*test-template*"` covers the spelling and any future sibling. Re-measure in the same commit and confirm the population returns to 175. Correct the comment: the collapse replaced three fixture spellings, and the predicate covers fixture spellings, not every excluded spelling.

**Left-shift.** This block has now been edited in three consecutive rounds with nothing able to red on a wrong edit. Add a drift-audit selftest arm that resolves `EVIDENCE_GLOBS` over a fixture tree containing one `fixture`-pathed file and one `.test-template.py` file and asserts BOTH are absent from the resolved population. Observe it RED by deleting either predicate before landing it. A population-size assertion over the real tree is the weaker sibling and would also have caught this — but it reds on every unrelated file addition, so prefer the two-file fixture arm.

---

### H3 — high — `tools/drift-audit/selftest.py` (absent from the diff)

**Round 2's blocker fix landed with no regression arm, and so did its sibling — while the codebase-map fix in the same fold got one.**

`git log --oneline -- tools/drift-audit/selftest.py` last touches that file at `d53129af`, the round-1 fold. It is absent from `504533fb`'s diffstat entirely. The fold's `--stat` shows `tools/codebase-map/selftest.py | 12 ++` and no drift-audit selftest line at all.

Neither prescription was implemented. Round 2's record, committed in this same diff, writes both: *"for every signal in `SIGNALS` where `gateable` is False and a `PINS` entry exists, a value equal to the pin renders `ok`, not `out of tolerance`. Stage the break … and confirm RED before landing"*, and an arm resolving `EVIDENCE_GLOBS` over a tree containing a `fixture` path. Grep confirms neither exists: `tools/drift-audit/selftest.py` contains zero occurrences of `out of tolerance` or `report only`, and its three `EVIDENCE_GLOBS` hits are all fixture-project declarations (`EVIDENCE_GLOBS = ['src', ':(exclude)*.test.sh']` and a `no-such-directory` swap), not assertions over the kit's real list. Its status-ladder arms parse printed rows only for `ledger_rows_contradicting_git`, asserting `empty by declaration`, `DEAD PROBE` and `OVER PIN` — all gateable branches above the changed line.

The two gate legs cannot see it either. `drift-audit records` runs `drift_report.py --check`, whose over-pin filter already compared against `pin` before the fold. `drift-audit selftest` has no arm on the branch. So reverting `drift_report.py:1831` from `s["pin"]` to `s["tolerance"]` restores round 2's blocker verbatim with every gate green.

The asymmetry is what makes this high rather than medium. The same fold DID left-shift the codebase-map repair, at `tools/codebase-map/selftest.py:1046`, and that arm is real — reverting `detail=feature` at `reuse_lookup.py:268` turns it RED, verified. The fold knew how; it did it for the sibling high and not for the blocker. §7's *"a new gate is not landed until its failing case has been observed"* and *"a gate you have only ever seen pass is an assertion about nothing"* both bind, and they bind hardest on the blocker.

**Fix.** Add both arms to `tools/drift-audit/selftest.py`, each observed RED against its pre-fix form before landing. One: in a fixture repo whose project layer declares a `PINS` entry for a non-gateable signal, run the human report and assert the row reads `ok` at `value == pin` and the over-pin wording at `value == pin + 1`; stage the break by reverting line 1831, confirm RED, unstage. Two: the `EVIDENCE_GLOBS` arm described under H2.

**Left-shift.** The arms above ARE the left-shift for the two product defects. The left-shift for the class — a fold implementing a prescribed arm for one finding and skipping it for another — is a fold-time check rather than a gate: when a review record's left-shift ledger names a file, the fold that closes those findings must touch that file or record in one line why it did not. Round 2's ledger named this file twice. Nothing read it.

---

### M1 — medium — `tools/drift-audit/drift_report.py:1296`

**The pin-comparison fix closed one carrier and left the sibling carrier stating the superseded rule, citing as its proof the loop that refutes it.**

The comment on `live_backlog_rows_per_shard` still reads: *"The threshold comes from the project layer, and for a NON-GATEABLE signal the status line compares against `tolerance` rather than `pin` (see the report loop), so it is read here."* The same fold rewrote that loop from `elif s["value"] > s["tolerance"]` to `elif s["value"] > s["pin"]`, and every signal now gets `s["pin"] = ctx.pins.get(s["signal"], s["tolerance"])` resolved at line 1810 before display. A reader following the pointer finds the opposite of what the comment says.

The workaround the comment justifies is now dead plumbing. `"tolerance": ctx.pins.get("live_backlog_rows_per_shard", 0)` at line 1300, and the identical unannotated construction for `readme_mechanism_drift` at line 1502, resolve the same value with or without the project-layer read, because `pin` already falls back to `tolerance` through the same `ctx.pins` lookup. `grep '\["tolerance"\]'` returns exactly one consumer in the tree: line 1810. So the next author of a report-only signal reads a rule that no longer exists and either copies a no-op or, reading it as the only way to get a pin into a status line, reproduces round 2's blocker.

Doc-only impact, and the comment was not touched by the fold that falsified it — which is the class this build's third round is still finding.

**Fix.** Rewrite lines 1296-1299 to state the current rule: the display loop resolves a pin for every signal and compares against it, gateable and report-only alike. Then either set `"tolerance": 0` at 1300 and 1502 like every other signal, or keep the `ctx.pins.get(...)` reads with one clause saying what they still buy (`--json` consumers are the only candidate).

**Left-shift.** Same annotation-lint hook as H1, second predicate: a comment containing a cross-reference of the form *see the report loop* / *see `<symbol>`* is an assertion about code elsewhere in the same file, and the cheap machine check is that the fold changing that referenced region must also touch, or explicitly re-affirm, every comment pointing at it. Implementable in the drift-audit kit as a line-range dependency: declare the report loop's range once, and red when a diff changes it without changing any comment whose text cites it. Run the predicate over the tree and print near-misses before wiring it.

---

### M2 — medium — `tools/drift-audit/drift_report.py:1831`

**The report-only branch moved its predicate to the pin and kept its old wording, so a pinned residue now falls through to a bare `ok` and an over-pin residue will announce a tolerance it did not cross.**

Observed at HEAD, one run, `GOV_DEFAULT_BRANCH=main python tools/drift-audit/drift_report.py`:

```
  non_terminal_specs_cited_by_product_source        2     64  ok (pin 2, drain it)
  live_backlog_rows_per_shard                     295      4  out of tolerance (report only)
  readme_mechanism_drift                           24     99  out of tolerance (report only)
  source_cited_ids_resolving_to_no_record           2    402  ok
```

The last row is unit 3's entire deliverable. It is report-only with a hardcoded `"tolerance": 0`, so `pin` resolves to the declared 2, `2 > 2` is False, and it falls through the new branch into the bare `else: status = "ok"` — rendering identically to a drained zero. The gateable sibling in the identical state, two rows up, prints `ok (pin 2, drain it)`. The pin is computed and compared and never shown on the one branch that suppresses the alarm.

For a report-only signal the status line IS the enforcement. The shipped Skill tells readers *"At the pin means 'still owed, drain it'"* and the `PINS` comment calls this population *a drain target from the first commit*; neither is reachable from the status column any more. Round 2 correctly called the false alarm a blocker. The fix traded it for a silent tolerance in the same carrier, which is the reassuring-zero family from the other direction — the family this build exists to close.

The other half is the wording. `git log -p` shows the predicate changed and the string `"out of tolerance (report only)"` left verbatim. At value 3 the row will say *out of tolerance* against a declared tolerance of 0 that was exceeded at 1, and will name neither the 0 nor the 2 it actually crossed. Harmless today only because no live report-only signal has `pin < tolerance`.

**Fix.** Give the report-only branch the two strings its gateable neighbours already use: `f"OVER PIN {s['pin']} — report only"` when over, and the `ok (pin N, drain it)` shape when at or under a non-zero pin. Amend the Skill template's pin paragraph so the rule is stated for report-only signals too — it currently frames the pin as a gateable-signal concept, which the fold made untrue.

**Left-shift.** The H3 status-ladder arm covers both sides if it asserts the full string rather than a substring: for a report-only signal with a pin above its tolerance, assert the row at `value == pin` contains the pin, and the row at `value == pin + 1` names the pin rather than the word `tolerance`. Observe both RED against the pre-fix branch. One fixture, four assertions, and this branch stops being the only one in the ladder nobody has watched fail.

## Left-shift ledger

Every confirmed defect above, and where its regression coverage goes. Nothing in this build is closed until this table is empty of `owed` rows.

| Row | Coverage | Where | State |
|-----|----------|-------|-------|
| B1 | fold verify list runs the unguarded `subject = repo` records legs before reporting green | unattended fold protocol | owed |
| H1 | selftest arm: `reuse_lookup` imports no project layer; comment lint for capability claims about unimported symbols | `tools/codebase-map/selftest.py` + annotation-style checker | owed |
| H2 | selftest arm resolving `EVIDENCE_GLOBS` over a fixture tree with a `fixture` path and a `.test-template.py`, both asserted absent | `tools/drift-audit/selftest.py` | owed |
| H3 | status-ladder arm over a report-only signal at `pin` and `pin + 1`, observed RED against the reverted branch | `tools/drift-audit/selftest.py` | owed, prescribed in round 2 and not implemented |
| M1 | comment-to-referenced-region dependency check, or fold-time re-affirmation of comments citing a changed region | annotation-style checker | owed |
| M2 | folded into H3's arm by asserting the full status string, not a substring | `tools/drift-audit/selftest.py` | owed |

## What this round did NOT find

Stated because a zero in a complete run is evidence, and this run is complete — 4/4 lenses and 5/5 skeptic batches returned, 0 DIED.

- No security finding. The diff opens no write path, no egress, no auth surface.
- No correctness defect in product code. Every product-code repair the fold made is correct at HEAD: `_ID_SHAPE` de-duplicates the retyped pattern, `_dossier_decisions` renders ids on the synthetic-candidate path, the pin comparison fixes round 2's blocker, and the fixture exclusions do exclude the two fixture files the comment claims. The defects are in the annotations, the coverage and one record.
- No verdict moves at HEAD from H2. Signal 2 reads 2 of 64 and AC5 of the unit-2 acceptance record holds; the re-admitted template carries no ids today. The finding is a coverage regression, and is filed as one.
- No new scope. No finding asks for a new grammar, signal, carrier, kit or unit. Every fix is a comment rewrite, a one-line predicate, a prose trim, or a test arm.
- The full merge bar has not run. Both kit self-tests and every diff-scoped gate are green at HEAD; the unguarded records leg is RED, which is B1, and the full bar owed at close has not been executed. No claim in this report rests on it having been.
