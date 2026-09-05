**Serves:** diff-review TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4

# aKeyedAnnotation — Tier-2 CLOSING DIFF review, round 1

Node `a` · streams `tooling` · 2026-09-05 · adversarial fan → skeptic refutation → synthesis, per `memory/guides/REVIEW-PROTOCOL.md`. Four Tier-2 units, all CLOSED before this review ran. The bug-class checklist for this exact range selected fifteen classes and they were the priority lenses.

**Reviewed range:** `87dbc7dff8258de626a1a8af58c1f1bd9dcb6e4d...HEAD` · ROUND 1

## Verdict: BLOCKED

Two blockers, and both are the same class: **an acceptance criterion certified true that the tree at HEAD refutes.** B1 — spec 4's AC1 says a candidate sourced from a dossier with a non-empty `decisions` list prints those ids, and the dossier this build itself created cannot print the id this build itself minted. B2 — the unit-3 pin comment and the unit-3 acceptance ledger both say `400 distinct ids`, and the command they name prints `402`, at the commit that wrote the comment and again at HEAD. Neither is expensive: B2 is two digits in two files, B1 is one field passed into one constructor. Both are cheap enough that landing without them would be a choice, not a trade.

The reason they block rather than trail as fixes is the build's own subject. This range wrote the rule that a comment may not assert what nobody observed and may not carry a live derived count, and then shipped three annotations that do exactly that (B2, H2, L1). A closing review that waved that through would be certifying the ledger rather than the tree, which is the thing the range exists to stop.

Nothing here argues against the build's shape. The four units repair a layer this repo already had; no finding asks for a new grammar, a new signal, a new carrier or a scope change, and the two spec-audit rounds that preceded the code did their job — none of the fifteen defects the round-2 record left standing came back as a code defect.

## Review shape and run integrity

- Raw findings 22 · confirmed 20 · refuted 2 · unverified 0 · precision 0.91.
- Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates dropped by the pipeline. **The run is complete**: every lens and every skeptic batch came back, so a zero anywhere in this report is a measured zero and not an absence of coverage.
- Precision 0.91 is far above the ~0.5 floor §8 names and above round 2's 0.62 on 40% less raw volume. Read it the way §8 says to read a high number: the surface was well primed and the lenses spent their budget on this diff rather than on re-deriving the specs — not as licence to fan wider next time.

**Convergence.** The 20 confirmed findings describe **14 distinct defects**. The pipeline dropped no duplicates because it dedupes by identity; this synthesis merged six rows into three primaries by defect, and every row is named in the `Raw ids` column so nothing is silently absorbed. Four lenses independently found H2 — the `_local_anchors` docstring — from four directions, and two found each of B2, M3 and M6. Convergence is a severity signal here, not extra findings, and the table counts defects.

**Which of the fifteen selected classes actually landed.** `second-implementation-is-not-a-second-opinion` (H2, M1), `two-readers-of-one-config-one-re-derived` (H4, M6), `fixture-passes-by-finding-nothing` (M2, M3), `staged-break-substitutes-a-synthetic-value` (M1), `spec-names-code-its-base-lacks` (H3), and the A3/A4 annotation classes this build minted (B2, H2, L1). Four selected classes produced nothing: `id-matched-as-a-substring`, `containment-tested-one-way`, `fixture-inherits-ambient-machine-state`, `two-guards-one-question-two-answers`. Since the run is complete, those four are measured absences — the slug-by-dash-split in unit 2 and the containment predicates were looked at and are correct.

## Findings

| # | Severity | Unit | Address | Defect | Raw ids |
|---|---|---|---|---|---|
| B1 | blocker | `-4` | `tools/codebase-map/reuse_lookup.py:250` | The synthetic dossier candidate is built with empty `decisions`, so a dossier surfaced as itself never prints its ids — spec 4 AC1 refuted at HEAD | 12 |
| B2 | blocker | `-3` | `tools/drift-audit/drift_signals.py:284` | The pin comment says 400 distinct cited ids; the signal printed 402 at the commit that wrote it, and the unit-3 acceptance ledger repeats the wrong figure as AC1 | 20, 4 |
| H1 | high | `-4` | `tools/codebase-map/reuse_lookup.py:171` | `merge()` resolves `detail` and `decisions` under separate last-write rules, so one dossier's ids print under another dossier's label | 11 |
| H2 | high | `-2` | `tools/drift-audit/drift_report.py:499` | `_local_anchors`' docstring asserts a byte-compare against the extractor that exists nowhere — and would red today if written | 2, 7, 13, 18 |
| H3 | high | `-2` | `memory/builds/aKeyedAnnotation/spec/2026-09-05-spec-TOOL-aKeyedAnnotation-2.md:156` | Two left-shifts the spec says "this unit owns" did not land, are in no AC, and reached no backlog row — unit CLOSED | 8 |
| H4 | high | `-2` | `tools/drift-audit/drift_report.py:536` | `_families_of` is a second reader of `FAMILIES` that diverges from `recall_conf` both ways, and its unvalidated token compiles outside main()'s handler, so a conf typo exits 1 and reads as drift | 3 |
| M1 | medium | `-2` | `tools/drift-audit/selftest.py:1824` | The only guard on the copied id grammar compares the copy against a function that falls back to the copy — tautological under any import failure | 1 |
| M2 | medium | `-2` | `tools/drift-audit/drift_report.py:845` | `checked += 1` precedes the new `slug is None` guard, so a pre-slug-era id inflates `of` while being unjudged, and `live` stays True on a fully unjudged corpus | 6 |
| M3 | medium | `-2` | `tools/drift-audit/drift_signals.py:84` | `EVIDENCE_GLOBS` excludes three test-file shapes and leaves every fixture DIRECTORY inside the evidence population the comment says it narrowed | 14, 21 |
| M4 | medium | `-4` | `tools/codebase-map/gen_map.py:76` | S4/AC5's honesty comment landed in `_FOUNDATION_SKELETON`, the one file `load_map_tree` excludes from `tree.dossiers` — so the check can never see it | 15 |
| M5 | medium | `-1` | `memory/gotchas/hookspath-resolves-into-another-checkout.md:64` | The paragraph trim removed the record's only `.unattended.conf` anchor, so the class no longer routes to diffs touching that file | 19 |
| M6 | medium | `-4` | `tools/codebase-map/reuse_lookup.py:73` | `_DECISIONS_RE` plus a comma split mis-parse a legal multi-line TOML array: a comment is emitted as an id and the id on the next line is swallowed | 5, 9 |
| L1 | low | `-4` | `tools/codebase-map/reuse_lookup.py:81` | The docstring states "the 17 dossiers that declare none"; the tree has 16, which is what the pin in `.codebase-map.conf` records | 16 |
| L2 | low | `-4` | `tools/codebase-map/reuse-lookup.agent.md:22` | The agent-facing doc still says a candidate is exactly one line; `_line()` now emits a second `decisions:` line for five dossiers | 22 |

---

## B1 — blocker — the dossier that owns this build's id cannot print it

`tools/codebase-map/reuse_lookup.py:250`, `assemble_shortlist`.

The fallback candidate for a dossier with no affordance seams is built as `Candidate(name, ('shared-seams',), detail=feature)` and takes the default empty `decisions`, so `_line` emits no clause. Reproduced at HEAD:

```
$ python tools/codebase-map/reuse_lookup.py "run the gates bar concurrently"
- annotation-style (## Shared seams)  [annotation-style]  (shared-seams prose ...)
```

`memory/map/features/annotation-style.md:8` declares `decisions = ["TOOL-aKeyedAnnotation-1"]` — the one id this build minted, on the dossier this build created, invisible on the path that surfaces it. Spec 4 AC1 says a candidate sourced from a dossier with a non-empty `decisions` list prints those ids; the tree refutes it, and the unit is CLOSED against that AC.

Reachability is independent of H1: `foundation` has zero affordance seams today, and any dossier that legitimately writes `none — <why feature-specific>` in its Reuse affordance section takes the same branch. Fixing H1 does not close this.

**Fix.** Keep `decisions_by_feature: dict[str, tuple]` on `Corpus`, filled in the dossier loop that already reads the text, and have `_line` print `corpus.decisions_by_feature.get(c.detail, ())`. One field instead of two, and it closes H1 in the same edit. If the Candidate field is kept instead, pass `decisions=decisions` into the `pool.setdefault(name, Candidate(...))` call.

**Left-shift gate.** A selftest arm that loops every dossier declaring a non-empty `decisions` and asserts the ids appear in the output when that dossier is surfaced — the class, not the seam-path instance. Stage the break by emptying the pass-through and confirm RED before landing it.

## B2 — blocker — a measured count that was never true, in two carriers

`tools/drift-audit/drift_signals.py:284`, and `memory/builds/aKeyedAnnotation/build/2026-09-05-build-TOOL-aKeyedAnnotation-3-acceptance.md:9` as AC1.

The comment reads "MEASURED on this corpus at the unit that added the signal: 400 distinct ids cited from 255 tracked non-memory source files, against 108 slugs anchored by a record." Measured at HEAD on a clean tree, `python tools/drift-audit/drift_report.py --json` returns `value: 2, of: 402, known_slugs: 108, scanned_source_files: 255`. A detached worktree at `c6c21d41`, the commit that introduced both the signal and the comment, also prints `402`. The 255 and the 108 are right; `400` is the one figure that was false of the tree it shipped on. The base was 399, unit 2's fixture id took it to 400, and unit 3's own two fixture ids took it to 402 in the same commit as the comment.

This is A4 of the guide unit 1 wrote, violated in the range that wrote it: a present-tense count of a live derived population with no sha and no node/date freezing it, sitting beside the source that owns it. It is also the `criterion-asserts-what-its-own-command-cannot-show` class this build filed, since AC1 certifies a number the command it names does not print.

**Fix.** Drop the digits and point at the signal's own `of` / `known_slugs` / `scanned_source_files`, the way the sibling repair at `drift_signals.py:397` already does for signal 2. If the figures are wanted frozen, name the sha they were measured at, per A4's FROZEN disposition. Correct AC1 in the unit-3 ledger in the same commit — two carriers, one fix.

**Left-shift gate.** A grep leg over `tools/**/*.py` for a `MEASURED` comment carrying a bare multi-digit literal with no adjacent sha or `(node, date)` stamp. That is the machine form of A4, it is one predicate, and per §7 run it over the real tree first and print near-misses — this build alone gives it two live hits (B2 and L1).

## H1 — high — one dossier's decision ids under another dossier's label

`tools/codebase-map/reuse_lookup.py:171`, `merge()`.

`detail or prev.detail` and `decisions or prev.decisions` are resolved independently, so a candidate name declared by several dossiers keeps the last non-empty value of each, from potentially different dossiers. Reproduced at HEAD: `parse_affordance` yields the degenerate seam name `the` for four dossiers, and

```
$ python tools/codebase-map/reuse_lookup.py "shrink-only registry convention stale row reds tracked path oracle"
- the  [spec-tokens]  (shared-seams prose (spec-tokens): ...)
    decisions: TOOL-aRelaxedShard-1 TOOL-aWidenedGuide-1
```

Both ids are declared only by `memory/map/features/memory-tree-hygiene.md`; `spec-tokens.md` declares `decisions = []`. An orienting agent is handed two ids that govern a different feature and both resolve — the "a guessed id resolves and is worse than an empty list" failure the unit's own §3 non-goals name. The degenerate `the` is what surfaced it, not what causes it: any two dossiers legitimately declaring the same seam name collide identically.

**Fix.** The `decisions_by_feature` change under B1 removes the second merge rule entirely.

**Left-shift gate.** A selftest arm with two fixture dossiers declaring the same seam name, one with decisions and one without, asserting that the printed ids belong to the dossier named in the label. Stage the break by restoring the independent `or` and confirm RED.

## H2 — high — a docstring asserting a guard nobody wrote

`tools/drift-audit/drift_report.py:499`, `_local_anchors`.

The docstring says the four anchor patterns are "byte-compared against the extractor's own anchors by this kit's self-test whenever that kit is present." No such comparison exists: `grep -c '_local_anchors\|_grammar_anchors' tools/drift-audit/selftest.py` returns 0, and the only grammar arm, `test_local_grammar_matches_the_extractor` at `selftest.py:1804`, compares `_local_ident` against `_grammar_ident` and nothing else.

The claimed compare would also red today. Anchors 1 and 3 differ byte-wise — the local copy spells the classes as raw-string escapes where `extract.py:115,119` writes the literal characters. They compile to the same sets, so this is an unguarded copy rather than a live divergence. What makes it high rather than medium is where the copy sits: these four patterns are the DEFINITION set for the new `source_cited_ids_resolving_to_no_record` signal, they are the half every copy-installed adopter without memory-recall actually runs, and the kit's own fixtures never install a recall kit — so the self-test path and the production path are disjoint with nothing joining them. Four lenses found this independently.

**Fix.** Either add the arm the docstring claims — beside the existing one, compare the anchor tuples, spelling the local classes with the literal characters so `.pattern` compares equal — or delete the sentence and record the copy as unguarded, the way the ledger already handles the unreachable import branch.

**Left-shift gate.** The arm itself is the gate. Broader and cheap: a leg that greps shipped docstrings for "compared by this kit's self-test" and requires the named symbol to appear in that kit's `selftest.py`. That predicate is the mechanical form of A3's "an assertion with no observation behind it", and this build supplies its first hit.

## H3 — high — two committed left-shifts that never landed

`memory/builds/aKeyedAnnotation/spec/2026-09-05-spec-TOOL-aKeyedAnnotation-2.md:156`, §5.

§5 names "two left-shifts the round-1 audit named and this unit owns": a class-level self-test arm that empties EVERY glob declaration and asserts its liveness flag flips, and a ban-grep so no module outside the recall extractor imports its module-level grammar constants. Neither exists. `selftest.py` empties only `EVIDENCE_GLOBS` (lines 1773/1782); there is no loop over signals whose declaration is a glob set, so `PRODUCT_GLOBS` and `TRACE_GLOBS` have no dead-declaration arm. No ban-grep exists anywhere in `tools/` — `gate-legs.json`'s only two ban legs are the python-resolver idiom and the review-join. Neither item appears in AC1–AC10, so the acceptance ledger closed green without them, and `memory/backlog/TOOL.md`'s aKeyedAnnotation rows 5–11 are all on unrelated subjects. Spec 2 reads `Status: CLOSED · rev-7`.

§7's left-shift rule is unsatisfied for both, and the class the ban-grep was written for is exactly the defect round 1 found — a consumer binding the grammar to the kit's own root.

**Fix.** Land the two items, or amend §5 to record them as deferred and open a `TOOL-aKeyedAnnotation-<n>` backlog row for each naming the class and the intended mechanism. A deferral is a decision; a silent drop is not.

**Left-shift gate.** A memory-tree hygiene arm asserting that every §5 item a CLOSED spec claims the unit "owns" resolves to either an AC in that unit's ledger or a backlog id. That is the check that would have caught this at close rather than at closing review.

## H4 — high — a second reader of FAMILIES, and a conf typo that reports itself as drift

`tools/drift-audit/drift_report.py:536`, `_families_of`; crash site at `drift_report.py:1790`.

Two divergences from `recall_conf.resolve`, neither visible to the new byte-compare because gov's own conf exercises neither.

- For `FAMILIES="PLAY KICK TOOL DEPL"` — no disciplines, a plausible adopter spelling — `_families_of` returns `()` (it `continue`s on any pair lacking `:`), so the fallback ident widens to `(?:[A-Z]{2,6})-...`, while `recall_conf`'s `rpartition(':')[2]` returns the exact four. Same conf, two grammars.
- `recall_conf` filters tokens with `^[A-Z][A-Z0-9]*$`; `_families_of` validates nothing. A token carrying a regex metacharacter makes `recall_conf.resolve` raise `ConfError`, `_grammar_ident`'s `except Exception` falls back to the unvalidated local copy, and the compile raises `PatternError`. `ctx = Ctx(root, conf, proj, base_ref)` sits BELOW the `except DriftError` that closes ~30 lines above, so the report dies with a raw traceback and rc=1 — and rc=1 is precisely `--check`'s "a gateable signal is over its pin". The comment at `drift_report.py:1749-1758` states verbatim that this shape was closed for `RATCHET_LOOKBACK` ("a config error reported itself as drift"); `FAMILIES` reopens it one attribute over.

**Fix.** In `_families_of`, take `pair.rpartition(":")[2]` and keep only tokens matching `^[A-Z][A-Z0-9]*$` — byte-for-byte `recall_conf`'s rule. Move the `Ctx(...)` construction inside main()'s existing `try/except DriftError` so a bad declaration exits 2 with a named refusal.

**Left-shift gate.** Two selftest arms: one feeding a discipline-free `FAMILIES` and asserting both readers return the same tuple, one feeding a metacharacter token and asserting rc=2 with a named refusal rather than rc=1 with a traceback. The second is the regression gate for the RATCHET_LOOKBACK class as a class, which is what §7 asks for.

## M1 — medium — the grammar guard can compare the copy to itself

`tools/drift-audit/selftest.py:1824`.

The arm asserts `mod._local_ident(families) == mod._grammar_ident(root, families)`, and `_grammar_ident` (`drift_report.py:475-495`) returns `_local_ident(families)` from its `except Exception` arm. With `import extract` forced to raise, the assertion evaluates True and the arm goes green: the guard shares its variable with the thing it guards, §7's named shape. The arm's only precondition is `extractor.exists()`, a file-existence check, not an importability one — so a syntax error, a new required key in `recall_conf.resolve`, or a raise inside `grammar_for` silently converts the sole check keeping `_local_ident` honest into a tautology, while the stale alternation goes on classifying the corpus for two signals that answer with a confident zero when the grammar matches nothing.

**Fix.** In the test, import `tools/memory-recall/extract.py` by path (the test already builds that path) and compare `mod._local_ident(families)` against `extract.grammar_for(root).ID`. Let an import failure fail the arm. The fallback's exception arm is correct product behaviour and should not change.

**Left-shift gate.** The fix is the gate; the missing half is the observation. Stage the break — patch `builtins.__import__` to raise for `extract` — confirm the arm REDS, unstage. §7: a gate you have only ever seen pass is an assertion about nothing.

## M2 — medium — a judged denominator counting the unjudged

`tools/drift-audit/drift_report.py:845`, `signal_closed_specs_untraceable`.

The two earlier unjudged paths `continue` before `checked += 1`; the new `slug is None` guard sits after it, so a no-slug-era id lands in both `of` and `unjudgeable` — the only such path in the function. The grammar swap widened `own_id_re` from the session-only form to the three-era alternation, so an H1 in the flat era (a family, a dash, three digits) and one in the node-scoped era (a family, a dash, a node letter and two or three digits) now match where they previously fell into the `if not own` branch (verified: `_own_id_re` matches both, `_slug_of` returns None for both). In an adopter tree on the flat or node-scoped era every terminal spec lands here, and since `live` keys on `checked > 0` the signal reports `live: True`, `of: <full population>`, `value: 0` having judged nothing. That is the reassuring-zero-wearing-a-live-flag class unit 2's own second liveness half closed for signal 2, one signal over. Gov's corpus is all session-era, so it reads 395/36 correctly and no leg sees it.

**Fix.** Move `checked += 1` below the slug guard, or gate liveness on a separate count of actually-judged specs the way `signal_spec_status` now gates on `evidence_files`.

**Left-shift gate.** A fixture spec with a flat-era H1 id, asserting `of` does not move while `unjudgeable` does.

## M3 — medium — the fixture narrowing that misses every fixture directory

`tools/drift-audit/drift_signals.py:84`.

The block comment at line 67 gives the rationale: a fixture id is evidence of a test, not of a shipment. The three exclusions cover only executable test-file shapes (`*.test.sh`, `*/selftest.py`, `*/test_*.py`). Running the declaration returns 186 files, and the survivors include `tools/govkit/fixtures/make_incms_receipt.py` (whose line 1 cites `DEPL-dCarriedReceipt-9`), `tools/govkit/fixtures/incms-2cff5855.receipt.json`, `tools/memory-recall/recall-fixture.json` (12 real TOOL ids), `tools/unattended/fixture-records/*.md`, `tools/unattended/fixture-pieces/*/piece.md`, `tools/unattended/playbook.fixture*.md` and `tools/pytest-parallel-guardrails/aiosqlite_worker_resilience.test-template.py`.

Signal 2 is gateable at tolerance 0 with pin 2, and it stays at 2 today only because `DEPL-dCarriedReceipt-9` happens to be CLOSED. The repo's own authoring convention is that a file's header names its unit id, so any fixture written by an in-flight unit flags its own still-open spec. The failure mode is a spurious red on the house's own bookkeeping, not a missed defect — bounded, but it is the hole the declaration was written to close. The arm that proves the narrowing writes only `src/thing.test.sh`, so a staged break in any missed shape flips nothing.

**Fix.** Add `:(exclude)*/fixtures/*`, `:(exclude)*/fixture-*/*`, `:(exclude)*.fixture.md`, `:(exclude)*.test-template.py`, then re-measure `of` and `evidence_files` and record the reading in the same commit that changes the list.

**Left-shift gate.** Extend the ARM 2 fixture to place a citation under a newly excluded shape (`src/fixtures/thing.py`) so the arm grades the class rather than the one filename it was written against. §7: gate the class, not the instance.

## M4 — medium — a repair landed on the one population the check cannot see

`tools/codebase-map/gen_map.py:76`, `_FOUNDATION_SKELETON`.

S4/AC5's honesty comment on the `decisions` key landed only in the FOUNDATION skeleton, written solely to `FOUNDATION.md` by the `--scaffold` branch. `load_map_tree` (`map_lib.py:1015-1027`) builds `dossiers` from `features/*.md` only and parses FOUNDATION separately, and `test_dossier_decisions_are_declining` counts `tree.dossiers` — so the one annotated key in the tree can never move the pin. `gen_map.py` has no `features/<feature>.md` scaffolder at all; the real creation path is the sibling-copy instruction at `test_codebase_map.py:10`, and 16 of the live dossiers carry a bare `decisions = []`.

One correction to how this was reported: AC5 as literally written is satisfied, and the shrink-only pin still reds on a new empty dossier, so the growth ratchet is intact. What is inert is S4's honesty nudge — F2's resolution ("the scaffold emits the key with a comment and the check counts it like any other empty") is false in both halves.

**Fix.** Put the annotated line where a new dossier actually comes from: the sibling-copy guidance in `test_codebase_map.py:10` and `test_codebase_map.template.py:10`, and `memory/map/README.md`'s dossier-format bullet. Keep or drop the FOUNDATION comment, but stop counting it as the mechanism.

**Left-shift gate.** None proportionate — this is prose placement, not a predicate. Documented check instead: when a dossier-shaped repair is specified, the acceptance criterion must name the population the check reads, not the file the edit touched. Record it against F2 in the unit-4 ledger.

## M5 — medium — a trimmed paragraph silently narrowed a bug class's routing

`memory/gotchas/hookspath-resolves-into-another-checkout.md:64`.

Anchors are derived from backticked path tokens in the record body (`gotchas.py:179`, `selectable()` at :184), and they are the routing key for `--for-diff` / `--for-paths`, which AGENTS.md makes the bug-class checklist for every review. Measured both sides: at base `87dbc7df` the anchors were `['.githooks/', '.githooks/pre-push', '.unattended.conf', 'check-wiring.sh', 'gate-env.sh', 'tools/check-wiring.sh']`; at HEAD they are the same set minus `.unattended.conf`. `python tools/memory-tree/gotchas.py --for-paths .unattended.conf` selected this record at base and does not at HEAD. The INDEX row went 6 → 4 sites with nothing in the commit explaining it — a coverage change as the side effect of a dedup, not a decision. The record still turns on `.unattended.conf` making `--check` an unattended run's precondition, so that is the file whose diffs most need it.

**Fix.** Put a backticked `.unattended.conf` back into the surviving prose and regenerate `memory/gotchas/INDEX.md`.

**Left-shift gate.** A hygiene arm that warns when a record's derived anchor set SHRINKS in a diff without the commit naming the record — the generated INDEX makes the loss invisible today, which is why nobody saw it.

## M6 — medium — the second reader of `decisions` fabricates one id and swallows another

`tools/codebase-map/reuse_lookup.py:73`, `_DECISIONS_RE`.

The pattern `^decisions\s*=\s*\[([^\]]*)\]` with `re.M` spans newlines, and the comma split strips no TOML comment. For the legal input

```toml
decisions = [
  "<FAMILY>-<slug>-1",  # the measured one
  "<FAMILY>-<slug>-2",
]
```

(ids elided to id-shaped placeholders on purpose — a fabricated id in a tracked record becomes an orphan, which is a bug class this build itself filed.) The helper returns `('<FAMILY>-<slug>-1', '# the measured one\n  "<FAMILY>-<slug>-2')`: one real id dropped, and a comment fragment carrying an embedded newline reaching the `decisions:` line and breaking its shape. `map_lib.py:913/930` reads the same field through a real `tomllib` parse and even validates each element against `decision_id_re`, so the codebase-map gate stays green while the second reader is wrong — `two-readers-of-one-config-one-re-derived`, on this diff's own checklist. Latent: I compared both readers across all 21 dossiers and found zero divergence, since every live array is single-line. It is one keystroke away — multi-line arrays are already the norm for `claims`, and `gen_map.py`'s new template line now models a comment on the `decisions` line itself.

The docstring's justification ("a front-matter read rather than a parse, so this module keeps needing no project layer") buys nothing here: `reuse_lookup.py:50` already does `import map_lib as m`.

**Fix.** `re.sub(r"#[^\n]*", "", body)` before the split, and drop any token that does not look like an id, so the regex reader can never emit a non-id.

**Left-shift gate.** Add the commented multi-line array to the selftest fixture at `selftest.py:974` and assert both readers agree — that arm grades the divergence rather than the spelling.

## L1 — low — a live count in a docstring, wrong at HEAD

`tools/codebase-map/reuse_lookup.py:81`.

"the 17 dossiers that declare none". Measured: 21 dossiers, 16 declaring `decisions = []`, none omitting the key — which is exactly what `.codebase-map.conf:44` records as `DOSSIER_DECISIONS_EMPTY_PIN=16`, with a comment recording the 17 → 16 transition. Two carriers of one derived count shipped in the same commit with different values, and this is the copy nothing grades. A3's ban on a present-tense count of a live derived population, in the build that wrote A3.

**Fix.** Drop the digits: "...would be noise on the dossiers that declare none, which `DOSSIER_DECISIONS_EMPTY_PIN` in `.codebase-map.conf` counts." The reasoning survives; the number moves to the file that owns it.

**Left-shift gate.** The same B2 grep leg, widened from `MEASURED` blocks to any docstring digit adjacent to a word like `dossiers`/`files`/`ids`. Run it over the tree and print near-misses before wiring it.

## L2 — low — the agent doc no longer describes the output

`tools/codebase-map/reuse-lookup.agent.md:22`.

The doc still says `each line is name [kind | file | fan-in N | SEAM] (why it is listed)`, and never mentions the field. `reuse_lookup.py:384-385` now appends `"\n    decisions: " + " ".join(c.decisions)`, and five dossiers declare non-empty decisions, so the shape change is live — confirmed by running the tool, which printed two `decisions:` continuation lines. The doc's last touch is `63e26430`; `78958d59` added the emission without updating the only instruction its only reader has.

**Fix.** Add the continuation line to the `candidates (ranked)` bullet, naming what `decisions:` carries and that it is absent when the owning dossier declares none.

**Left-shift gate.** None proportionate; the line is self-describing and nothing breaks. Documented check instead: a unit that changes `_line`'s output shape updates `reuse-lookup.agent.md` in the same commit, recorded as a DoD item on the codebase-map dossier rather than as a leg.

## What this build got right

Worth stating, because the finding list is long and the shape of it is not "the build is bad".

- Every new arm was observed RED by staging a break, and the review found no arm that had only ever been seen pass. `staged-break-substitutes-a-synthetic-value` was a priority lens and produced one finding (M1), which is about a guard's variable, not about an unobserved break.
- The two spec-audit rounds paid for themselves. Fifteen defects were folded before a line of code was written, and none of them recurred as a code defect — the code findings here are all new surface.
- The units that repaired existing annotations repaired them correctly: the two dangling source citations, the trimmed duplicate bug-class record, and the pin-comment repair at `drift_signals.py:397` are all sound. B2 is the sibling pin that did not get the same treatment.
- The recurring class across this range is narrow and nameable: **the build about honest annotations shipped three dishonest ones** (B2's count, H2's asserted guard, L1's count), and two more defects are a repair landed one population away from the check that reads it (M4, M5). Both classes are already this repo's own records. That convergence is the argument for the two grep legs proposed under B2 and H2: the rule exists, the corpus supplies its first hits, and nothing mechanical reads it yet.

## Gate suggestion summary

| Finding | Left-shift | Cheapest form |
|---|---|---|
| B1, H1 | gate | Selftest arm over every dossier declaring decisions, asserting the ids print under the right label |
| B2, L1 | gate | Grep leg: a bare multi-digit literal in a shipped comment with no sha or `(node, date)` beside it |
| H2 | gate | The anchor-tuple comparison the docstring already claims; optionally a leg asserting a claimed self-test symbol exists |
| H3 | gate | Hygiene arm: a CLOSED spec's §5 "this unit owns" items resolve to an AC or a backlog id |
| H4 | gate | Two arms — discipline-free `FAMILIES` agreeing across readers, metacharacter `FAMILIES` exiting 2 not 1 |
| M1 | gate | Import the extractor in the test; stage the import failure and confirm RED |
| M2 | gate | Flat-era fixture id: `of` must not move, `unjudgeable` must |
| M3 | gate | ARM 2 fixture citation under a fixture DIRECTORY, not only `*.test.sh` |
| M6 | gate | Commented multi-line array in the selftest fixture, both readers compared |
| M5 | gate | Warn on a derived anchor set shrinking without the commit naming the record |
| M4, L2 | documented check | Named in the sections above; §7 exemption — an exemption is not coverage, so both are written down |
