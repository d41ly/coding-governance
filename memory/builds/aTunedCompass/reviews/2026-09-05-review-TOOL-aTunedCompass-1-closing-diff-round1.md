**Serves:** diff-review TOOL-aTunedCompass-1 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11

# aTunedCompass — closing diff review: the seams between eight units one run built alone

*Node `a`, 2026-09-05. A Tier-2 adversarial pass over the cumulative diff of one unattended run —
61 files, ~3762 insertions, seven units built and closed plus one committed with its spec still
open. Four primed finder lenses, a skeptic stage prompted to REFUTE each finding, one synthesis.
The bug-class checklist `gotchas.py --for-diff` selected for this exact range was the lens brief:
25 classes, of which `two-answers-to-one-question`, `assertion-between-two-derived-values`,
`amendment-leaves-its-other-half-standing` and `containment-tested-one-way` account for most of what
follows. Hunting was weighted at the seams BETWEEN units, which per-unit verification structurally
cannot see: units 6, 8 and 10 all edit `reuse_lookup.py`; units 4 and 5 both edit the memory-recall
kit; unit 11 edits the driver this run is executed by. Every claim was re-checked at source during
synthesis, and the re-checks that moved a number are named inside the finding that carried it.*

**Range:** `22d75b31296a3a4fe28cf53a85c51076b8e6d798...HEAD`

## Verdict: BLOCKED

Two blockers, both cheap and both self-inflicted. Neither is a wrong answer in shipped behaviour;
both are records that assert something the code does not do, in a build whose own unit 1 exists to
close exactly that class. The rest lands with fixes. Nothing in the diff is a security finding, a
data-loss path, or a broken gate.

**Review shape.** Raw 22 · confirmed 20 · refuted 2 · unverified 0 · precision 0.91.

**Run integrity.** Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates discarded by the
pipeline. The run is COMPLETE: every count above is zero, so an absence below is evidence of
absence within the lens brief rather than of a lens that never reported.

**Synthesis note on the finding count.** The pipeline discarded no duplicates, but the 20 confirmed
findings are 11 distinct defects — five of them were reported independently by more than one lens.
They are merged below with every contributing raw id named, so nothing is lost and no defect is
counted twice in the severity tally. The merges: F1 = raw 1 + 18 · F2 = raw 4 + 12 + 19 · F5 = raw 8
+ 11 · F7 = raw 3 + 7 + 13 · F9 = raw 14 + 15 + 21 · F10 = raw 16 + 22.

---

## Findings

| # | Sev | Site | Defect | Raw ids |
|---|-----|------|--------|---------|
| F1 | **BLOCKER** | `memory/backlog/TOOL.md:347,348,352,359` | Four backlog rows this diff falsified are still OPEN | 1, 18 |
| F2 | **BLOCKER** | `tools/codebase-map/reuse_lookup.py:430` | `shown_paths` records only symbol files, against its own spec, while docstring and dossier assert "ONE derivation" | 4, 12, 19 |
| F3 | HIGH | `tools/codebase-map/reuse_lookup.py:9` | `--help`, the function docstring and the agent instruction all state the pre-unit-10 neighbour predicate | 6 |
| F4 | MEDIUM | `tools/codebase-map/selftest.py:989` | Unit 8's only arm asserts the values it passed in; the real call site is unexercised and its argument defaults to `None` | 20 |
| F5 | MEDIUM | `tools/memory-recall/query.py:744` | `run_rollup`'s docstring misquotes `bench.parent_of`; the `rec` → `meta.id` fold it depends on is named nowhere and tested nowhere | 8, 11 |
| F6 | MEDIUM | `tools/codebase-map/replay-phrases.py:197` | 49 of 140 graded phrases cannot register a hit and are in the denominator, undeclared | 5 |
| F7 | MEDIUM | `tools/memory-recall/query.py:633` | The rebuild-cause chain is a second spelling of `fresh` AND runs before the early return, re-walking the corpus on every cache hit | 3, 7, 13 |
| F8 | LOW | `tools/codebase-map/replay-phrases.py:191` | Reports the upper of two middle values under the name `median` | 9 |
| F9 | LOW | `memory/map/features/codebase-map.md:74,91` · `memory-recall.md:62` | Three map-dossier symbols that do not exist | 14, 15, 21 |
| F10 | LOW | `tools/codebase-map/replay-phrases.py:2,23,162` | The `grade` → `measure_phrase` rename was applied to prose, so `--help` prints a botched sed | 16, 22 |
| F11 | LOW | `memory/map/features/codebase-map.md:94` | The cost figure for unit 10 does not reproduce at HEAD and pins no sha | 17 |

---

### F1 — BLOCKER — four backlog rows this diff falsified are still recorded OPEN

`memory/backlog/TOOL.md:347` · `:348` · `:352` · `:359`
*Raw ids 1 and 18. Class: `amendment-leaves-its-other-half-standing`.*

Four rows in the shard that §6 names as a tooling session's reading order were falsified by commits
in this range, and all four still read OPEN at HEAD.

- `:352` `TOOL-aWeighedCompass-10` states `lookups.jsonl` rows are `{type, at, query, worktree, n_shown}` and asks for `shown_paths`. Commit `231c99d1` shipped it — `reuse_lookup.py:548-549` writes `shown_paths` and `n_sources`.
- `:347` `TOOL-aWeighedCompass-5` states `DURABLE` requires `memory/<dir>/DECISIONS.md` and `spine` is empty. Commit `771d209d` widened the pattern; `extract.py:145-149` makes the directory segment optional and `DURABLE.search` now matches 9 of 1351 tracked `memory/` paths.
- `:359` `TOOL-aWeighedCompass-17` states "`roll` IS THE BEST CHUNK SUBSTRATE AND `query.py` DOES NOT USE IT". Commit `f8c1c4fc` landed `run_rollup` at `query.py:737` and applies it at `:780`. The headline is now flatly untrue.
- `:348` `TOOL-aWeighedCompass-6` prescribes "a per-path cap in the fusion" as the cheap shape and quotes 54.5%. That shape shipped, and unit 4's own acceptance ledger measures the duplicate rate at 0.369. Stale rather than false — an amend, not necessarily a close.

`grep -rn 'aWeighedCompass-5\|aWeighedCompass-6\|aWeighedCompass-10\|aWeighedCompass-17'` over
`memory/builds/aTunedCompass/` returns nothing, and no commit body in the range mentions them, so
nothing anywhere joins the fix to the row. Only unit 1 (`6f6b0504`) touched the shard; units 4, 5
and 8 touched no record at all.

This is not a declared deferral. The build has the opposite convention in the same diff: spec 1's
S4/AC7 closes `TOOL-aWeighedCompass-2` inside the unit that fixed it, and specs 6, 9 and 10 each
state explicitly which parent rows stay open and why. Nothing in `BUILD-METHOD.md` or
`UNATTENDED-PROTOCOL.md` defers row closure to landing, and §1's DoD requires the backlog updated
before the push. The row unit 1 closed is titled "STALE ROW HANDED A FALSE FACT TO A KICKOFF"; this
run re-creates that defect four times in the file it edited to fix it.

**Blocker because** the next kickoff reads four fixed defects as live and can re-plan work already
done, and because a closing review that lets a DoD violation through is the mechanism by which the
DoD stops binding. The fix is one commit.

**Fix.** Flip all four the way unit 1 flipped `TOOL-aProvenReuse-4`, each naming the unit that closed
it — `Closed by TOOL-aTunedCompass-8` (`:352`), `-5` (`:347`), `-4` (`:359`). For `:348` either close
it naming `-4`, or rewrite it keeping only the surviving half and stating the post-rollup figure
(0.369, not 0.545) rather than leaving the original claim standing.

**Left-shift gate.** A closing-review leg that, for every unit id closed in a build, greps the
build's records for the parent backlog ids that unit's spec names in its "what this closes" section,
and reds when a named parent row is still OPEN with no closure note anywhere in the build folder.
The spec files already name their parents, so the population is declared rather than inferred, and
the check is a grep over two sets. Cheap, and it fires on exactly this shape.

---

### F2 — BLOCKER — `shown_paths` records only symbol files, contradicting its own spec, its docstring and the dossier

`tools/codebase-map/reuse_lookup.py:430` (also `:449`, `:578`) ·
`memory/map/features/codebase-map.md:110`
*Raw ids 4, 12 and 19. Classes: `two-answers-to-one-question`, `containment-tested-one-way`,
`assertion-between-two-derived-values`.*

`derive_source_paths` (`:430`) collects `r.candidate.file` and nothing else. `_sources` (`:449`) is a
second, independent walk of the same `shortlist.ranked` that additionally emits
`dossier: <root>/features/<detail>.md` for affordance-seam and shared-seams candidates and
``inventory `<key>` `` for file-less inventory candidates. `_sources` never calls
`derive_source_paths`; the two dedupe on different keys (normalised path vs. the whole rendered
line) and normalise differently (`derive_source_paths` folds `\` to `/`, `_sources` does not).

Three things assert they are one derivation. The docstring at `:433`: "ONE derivation, read twice:
`_sources` LABELS these". `memory/map/features/codebase-map.md:110`, same words. Unit 8's acceptance
ledger: "One derivation feeds both, so this holds by construction." All three are false.

The consequence is not stylistic. Spec 8 §4 defines the population as "a symbol candidate contributes
its definition file, a dossier candidate contributes its dossier", and says dossier paths are KEPT.
Only the first half shipped, so the field diverges from its own spec. Measured live on this tree:

- "reuse affordance seam dossier prose" — 14 source lines shown (5 symbol, 9 dossier), `n_sources=5`.
- "unattended landing mandate protocol" — 15 shown (2 symbol, 9 dossier, 4 inventory), `n_sources=2`.
- "append a telemetry row to a jsonl log" — 19 entries rendered, 13 logged; 6 of 19 dropped, 32%.

In a repo that has not adopted the symbol tier (`has_symbols=False`) every candidate is file-less, so
every row logs `shown_paths: []` and `n_sources: 0` forever — and the dossier tells a reader that a
zero means the probe pointed at nothing. Unit 6's own `replay-phrases.py` `_PATH` regex admits `.md`,
so dossier paths are in the ground truth this instrument is graded against; the log systematically
under-credits map records against the one harness that grades them.

AC3 tests containment ONE WAY ("every entry appears there"), which by construction cannot see a
missing entry — the class the checklist selected as `containment-tested-one-way`, tripped in the unit
that the class was selected for.

**Blocker because** rows written wrong now are not recoverable retroactively: the whole justification
for the field is that a later analysis joins logged paths against what a session opened, and every
row this run and its successors write until the fix under-records by roughly a third. It also
carries a closed unit's acceptance claim that is false — "verify over assert" broken in the ledger
that asserts it.

**Fix.** Make it genuinely one derivation: have `_sources` build its `symbol def:` lines from
`derive_source_paths(shortlist)`, and extend `derive_source_paths` to walk the same dossier and
inventory branches (`<root>/features/<detail>.md` or `FOUNDATION.md`; inventory-with-no-file
contributes nothing). If the field is deliberately symbol-only — it is not, per spec §4 — then
rename it and correct spec §4, the docstring, the ledger and the dossier together.

**Left-shift gate.** A self-test arm asserting containment in BOTH directions: every path
`derive_source_paths` returns appears in `_sources`' output, AND every `symbol def:`/`dossier:` line
in `_sources` has its path in `derive_source_paths`. A one-way subset assertion is what let this
land; the reverse assertion is the whole gate.

---

### F3 — HIGH — `--help`, the function docstring and the agent instruction all state the predicate unit 10 removed

`tools/codebase-map/reuse_lookup.py:9-10` · `:203` · `tools/codebase-map/reuse-lookup.agent.md:24`
*Raw id 6. Class: `amendment-leaves-its-other-half-standing`.*

Unit 10 narrowed the same-kind neighbour arm to the seed's own directory. The code at `:265` now
requires `cand.kind in seed_kinds AND _derive_dir(cand.file) in seed_dirs`. Three statements of the
old predicate were left standing:

- `:9-10`, the module docstring — "a capped set of structural neighbours (same kind or same file as a seed)". `main` at `:559` passes `__doc__` into `argparse.ArgumentParser(description=...)`, so `reuse_lookup.py --help` prints a predicate the code no longer implements.
- `:203`, `assemble_shortlist`'s docstring — "symbols with the same kind OR the same file as a symbol seed, capped".
- `reuse-lookup.agent.md:24` — "neighbours live in the same file or are the same kind as a seed". This file is the tool's entire interface for an agent.

The kit's own selftest at `:1117-1125` proves the divergence: it asserts `far_helper` — same kind,
different directory — is NOT admitted.

An agent reading either prose statement believes a same-kind candidate in another kit directory would
have surfaced, and records `no seam fits` from a shortlist that structurally could not contain it.
Unit 10's own comment at `:262` names this failure: "A predicate that changes while its printed
reason does not is a gate lying quietly." The per-candidate reason string was updated; the three
other spellings were not.

**Fix.** All three to "same file as a seed, or the same kind within the seed's own directory".

**Left-shift gate.** Weaker than a real gate but honest and cheap: a self-test arm that asserts the
`--help` text and `reuse-lookup.agent.md` both contain the word `directory` within the neighbour
sentence, so a narrowing that does not reach the prose reds. The general form — prose stating a
predicate its code owns — is the `two-answers-to-one-question` class and is only truly closed by
having one statement; the honest alternative is to delete the predicate from both prose sites and
point at the function.

---

### F4 — MEDIUM — unit 8's only automated arm asserts the values the test itself passed in

`tools/codebase-map/selftest.py:989` (arm `b` of `test_lookup_row_carries_sources`)
*Raw id 20. Class: `assertion-between-two-derived-values`, `fixture-passes-by-finding-nothing`.*

Arm (b) calls `rl.write_lookup(m.repo_root(), "q", len(sl.ranked), paths)` and then asserts
`row["n_shown"] == len(sl.ranked)`, `row["n_sources"] == len(paths)` and
`row["shown_paths"] == paths[:CAP]` — three assertions between a value and the same value, which can
only fail if `json` is broken.

The wiring the unit is actually about —
`write_lookup(m.repo_root(), query, len(shortlist.ranked), derive_source_paths(shortlist))` at
`reuse_lookup.py:578` — is never run by the suite. Every call in the file is a direct
`rl.write_lookup(...)`; the only `rl.main()` call, at `:215`, is
`test_clis_refuse_an_unadopted_root`, which asserts exit 2 on a path that returns before the write.
A grep for `lookups.jsonl` across `tools/` confirms nothing runs the CLI end to end and inspects a
row. Spec AC1 is written as a property of running the CLI and is met only by hand observation.

Because `paths: list[str] | None = None` and `paths = paths or []` at `:534`, dropping or
mis-ordering that fourth argument writes `shown_paths: []` / `n_sources: 0` on every row — which the
spec explicitly declares a LEGAL state for an empty shortlist, so the corpus would fill with rows
indistinguishable from probes that pointed at nothing, with every arm green.

*In fairness to the arm as a whole:* (a) genuinely tests dedup, forward-slashing and membership of
`derive_source_paths`, and (c) genuinely exercises the cap. The load-bearing gap is the wiring.

**Fix.** Drive `rl.main(["normalise a display name into a url slug"])` inside the scratch repo and
read the row it writes, asserting `n_sources == len(rl.derive_source_paths(sl))` and
`n_shown != n_sources` on a fixture where they differ. Make `paths` a required positional parameter
so a dropped argument is a `TypeError` rather than an empty list.

**Left-shift gate.** The required-parameter change IS the gate — it converts a silent empty list into
a crash at the one call site. Pair it with the end-to-end arm above.

---

### F5 — MEDIUM — `run_rollup`'s docstring misquotes `bench.parent_of`, and the fold it silently depends on is named nowhere and tested nowhere

`tools/memory-recall/query.py:744` (key at `:756`) · `tools/memory-recall/bench.py:132` ·
`tools/memory-recall/query.py:344` · `tools/codebase-map/selftest.py` — no arm
*Raw ids 8 and 11. Class: `two-answers-to-one-question`, `staged-break-substitutes-a-synthetic-value`.*

The docstring says the parent key "is spelled the way `bench.parent_of` spells it:
`hit["id"] or hit["path"]`". `bench.parent_of` (`bench.py:130-132`) is
`r.get("rec") or r.get("id") or r["path"]` — three levels, `rec` first, and the opposite folding
precedence. `rec` is the key the docstring's whole 99.4% argument is about.

The served rollup is correct today only because a third file coalesces the keys: `_write_set`
(`query.py:341-344`) stores `meta.id` as `d.get("id") or d.get("rec") or ""`, and `extract_chunks`
(`extract.py:582-585`) sets `path`, `line`, `crumb`, `text` and optionally `rec` but never `id`. So a
chunk's `rec` arrives in `search()`'s `id` slot through that fold. That step is load-bearing and is
named in neither docstring.

Coverage is worse than the claim. `selftest.py:426 test_chunk_arm_rolls_up` states that "BOTH
branches of the parent key are covered" and feeds synthetic dicts carrying a literal `id`; grepping
the whole selftest for `rec` / `meta` / `_write_set` finds no arm exercising the real path. If
`_write_set`'s coalescing order changes or drops `rec`, the anchored branch degrades to a per-path
cap for the 129 chunk documents it exists to serve, every arm stays green, and the docstring still
says the key matches bench.

Behaviour is correct today. The documented invariant and its coverage claim are both false.

**Fix.** Spell the key as `hit.get("rec") or hit.get("id") or hit["path"]` so it is literally
`bench.parent_of` over a dict, correct the docstring to name `_write_set`'s coalescing as the reason
`rec` reaches the `id` slot, and add one arm that builds a real chunk index over a corpus with an
`##` heading-defined record id and asserts the rollup collapses on it.

**Left-shift gate.** The end-to-end arm above is the gate; the synthetic-dict arm is exactly the
`staged-break-substitutes-a-synthetic-value` shape and should be kept only as a companion, with its
"BOTH branches covered" comment corrected to say which branch it actually reaches.

---

### F6 — MEDIUM — 35% of the hit-rate denominator cannot register a hit, and the harness does not say so

`tools/codebase-map/replay-phrases.py:197`
*Raw id 5. Class: `fixture-passes-by-finding-nothing`, `inputs-inside-the-subjects-reach`.*

Reproduced with the harness's own parsers: 140 graded phrases, 39 ungraded, 47 distinct candidate
files in the corpus. 49 of the 140 have ground-truth sets where NO truth path can ever match a
candidate file under `measure_phrase`'s own rule
(`f == t or f.endswith('/'+t) or t.endswith('/'+f)`). Truth entries break down 165 `.py`, 82 `.sh`,
62 `.md`, 22 `.js`, 9 `.json`, 4 `.toml`; the `.sh` half is unhittable because the symbol index has
no shell extractor (the known `TOOL-aWeighedCompass-8` blind spot), and `.md`/`.json`/`.toml` truths
are unreachable by construction.

`hit_rate` at `:197` divides by `len(rows)`, which includes all 49. The summary reports only
`phrases_without_ground_truth` — the empty-§10 class — so nothing in the harness, its docstring,
`memory/map/features/codebase-map.md` or either acceptance ledger states that 35% of the denominator
cannot move.

The numbers are load-bearing. 0.579 → 0.600 (unit 6) and 0.600 → 0.586 (unit 10) are 3 and 2 phrases
respectively, quoted in the dossier and in both ledgers as the measured worth of two ranker changes,
and the file declares itself the instrument for judging future ones. The deltas survive the dilution
directionally, which is why this is a disclosure and instrument defect rather than a wrong
conclusion — but by this repo's own rules (a skip must announce itself; a gate's header states what
it does not check) the class has to be reported.

A second, smaller defect in the same file: `_parse_section10_paths` harvests every backticked path in
§10 including ones the author records as MISSES — unit 8's own §10 backticks
`tools/codebase-map/reuse_lookup.py` while stating the probe did not name it.

**Fix.** After `corpus` loads, partition `graded` on whether any truth entry can match a
`corpus.candidates[*].file` under `measure_phrase`'s own suffix rule; grade the reachable set and
report the unreachable count as a third summary field beside `phrases_without_ground_truth`. Restrict
`_parse_section10_paths` to the sentence naming the chosen seam, or require an explicit marker.

**Left-shift gate.** The harness itself: emit `phrases_unreachable` in the summary and have the
harness refuse (non-zero, or a loud banner) when it exceeds a declared fraction. An instrument that
prints a rate has to print what the rate cannot see.

---

### F7 — MEDIUM — the rebuild-cause chain is a second spelling of `fresh`, and it runs before the early return

`tools/memory-recall/query.py:633-652`
*Raw ids 3, 7 and 13. Class: `two-answers-to-one-question`.*

Two defects in one new block, introduced by this diff (`git diff 22d75b31 -- tools/memory-recall/query.py`
shows the whole chain is new).

**(a) Two spellings.** `fresh` (`:616-627`) orders its clauses force → version → chunk_max → digest →
alias_digest → conf_digest. The cause chain (`:633`) orders them manifest → force → version →
chunk_max → conf_digest → alias_digest → digest, and falls through to the literal
`"a missing database"`. The clause sets are identical today, so no wrong cause is printed now. A
clause added to `fresh` and not to the chain will report every instance of it as "a missing
database" — in the block whose stated purpose is to let an acceptance criterion name the reason
rather than assert that a rebuild happened.

**(b) It runs on the hot path.** The chain sits between the `fresh` computation and
`if fresh: return dirp, man, False` at `:652`. `fresh` being true means every clause was evaluated,
which forces the chain all the way through `man.get("digest") != corpus_digest(repo, files + declared)`
at `:645` — a second full stat sweep of the corpus, plus a second `alias_digest()` and `CONF.digest()`,
none of them memoised. The resulting `cause` is discarded: `REBUILD_CAUSE.append(cause)` is below the
return, and `REBUILD_CAUSE` is read only under `rebuilt` at `:1288`.

Measured on this tree: 1330 corpus files + 3 declared, `corpus_digest` at 22-33 ms per call depending
on cache warmth. Every cached query pays it twice, on the exact path the cache exists to make fast.
Two lenses measured 21.7 ms and 23 ms warm; a third quoted 45 ms cold. The spread is warmth, not
disagreement — the doubling is the finding, not the decimal.

**Fix.** Compute the cause once and derive `fresh` from it: an ordered list of `(clause, name)` pairs,
first failing name is the cause, `fresh = cause is None`. That evaluates `corpus_digest` once, cannot
drift in order, and makes a new clause impossible to add to one side only. If the one-derivation
shape is more surgery than wanted, the minimum is moving `if fresh: return` above the chain — that
fixes (b) and leaves (a) standing.

**Left-shift gate.** An arm that counts `corpus_digest` calls on a warm `ensure_cache` and asserts
exactly one. It fails today, which by §7 is the point: a gate whose failing case has been observed.

---

### F8 — LOW — the harness reports the upper of two middle values under the name `median`

`tools/codebase-map/replay-phrases.py:190-191`
*Raw id 9.*

`ranks = sorted(...)` then `median = ranks[len(ranks) // 2]` returns the upper of the two middle
values on an even-length list — for `[1,2,2,3,3,3]` it reports 3 where the median is 2.5. It is
printed and keyed as `median_rank_of_first_correct`, and that figure is quoted as unchanged at 2 in
`memory/map/features/codebase-map.md:83` and both acceptance ledgers (unit 6 `:39`, unit 10 `:22`) —
the declared instrument for judging ranker changes. With ~81 hits of 140 the parity is not fixed run
to run, so the reported value can step by a full rank when the true median moves by half of one.

**Fix.** `import statistics` and `statistics.median(ranks) if ranks else None`, or rename the field to
`p50_rank_of_first_correct` and state the tie rule. `statistics` is stdlib and already imported at
`tools/memory-recall/query.py:73`.

**Left-shift gate.** None worth building for a one-line stdlib swap — this is the fix, not a class.

---

### F9 — LOW — three map-dossier symbols that do not exist

`memory/map/features/codebase-map.md:74` and `:91` · `memory/map/features/memory-recall.md:62`
*Raw ids 14, 15 and 21. Class: `amendment-leaves-its-other-half-standing`.*

- `codebase-map.md:74` — "`_shortlist_key` is read twice". The symbol is `_derive_shortlist_key` (`reuse_lookup.py:326`, read at `:287` and `:290`); `_shortlist_key` exists nowhere in the kit. It is a substring of the real name, so a grep does land on it.
- `codebase-map.md:91` — "The axis is `os.path.dirname`". No `os.path.dirname` exists in the kit; the axis is `_derive_dir` (`:315`), a `replace("\\","/")` + `rsplit("/",1)` helper that also differs from `dirname` on a bare filename (returns `""`). Arguably conceptual shorthand, but it is backticked as a symbol.
- `memory-recall.md:62` — "`fuse()` reads the chunk arm `k * ROLLUP_DEPTH` deep". `grep -n 'def fuse' tools/memory-recall/query.py` returns nothing; the function is `run_fusion` (`:764`), with `rrf()` (`:719`) doing the arithmetic. This one genuinely resolves to nothing, and the bullet directly below it — "There is ONE fusion call site" — is anchored on that dead name. `memory/builds/aTunedCompass/build/2026-09-05-build-TOOL-aTunedCompass-4-acceptance-ledger.md:58` carries the same dead `fuse()`.

Unit 8's own ledger (AC9) records that the verb table refused `fuse` and `grade` and that thirteen
names were renamed; the renames landed in code only. These are the orientation records a session
greps before touching the area, and the map's ratchet covers inventory KEYS rather than prose symbol
names, so the class is structurally ungated.

**Fix.** `_shortlist_key` → `_derive_shortlist_key`; `os.path.dirname` → `_derive_dir` (or state the
axis as "the defining file's directory" with no function name); `fuse()` → `run_fusion`. The ledger
line is evidence — give it a one-line superseding note rather than an edit, matching how unit 11
annotated the `aClosedDocket` ledger.

**Left-shift gate.** A dossier leg that extracts every backticked token in `memory/map/features/*.md`
matching an identifier shape (`[A-Za-z_][A-Za-z0-9_]*` with a `_` or a trailing `()`) and asserts it
appears as a definition in the kit the dossier covers. Run the predicate over the tree first and
print hits AND near-misses, per §7 — the false-positive rate on prose words is the whole question,
and if it is too high the honest form is a warn-only report rather than a red.

---

### F10 — LOW — the `grade` → `measure_phrase` rename landed inside the tool's own help text

`tools/codebase-map/replay-phrases.py:2` · `:23` · `:162`
*Raw ids 16 and 22.*

`argparse` is built with `description=__doc__, formatter_class=RawDescriptionHelpFormatter` (`:160`),
so `python tools/codebase-map/replay-phrases.py --help` literally prints "Replay the reuse probe over
this repo's own recorded phrases, and measure_phrase it.", the usage line
"`{cli}            # measure_phrase every phrase, print the summary`", and the `--limit` help
"measure_phrase only the first N phrases". All three are prose positions where the word was "grade",
so the lexicon rename was applied by text substitution rather than to identifiers — worth knowing
before the next sweep. This is the first commit of a tool whose whole job is to be run by hand when
somebody changes the ranker, and its help text is the only documentation it has.

**Fix.** `:2` → "and grade it"; `:23` → "# grade every phrase, print the summary"; `:162` → "grade
only the first N phrases". The function name `measure_phrase` stays — the lexicon requires it.

**Left-shift gate.** For the lexicon kit's rename path rather than for this file: a rename sweep that
edits docstring or help-string bytes should report the prose hits separately for a human to confirm,
instead of applying them silently.

---

### F11 — LOW — the cost figure for unit 10 does not reproduce at HEAD and pins no sha

`memory/map/features/codebase-map.md:94`
*Raw id 17.*

The dossier records "hit rate falls 0.600 → 0.586" over 140 phrases as the price of the directory
narrowing. Running the committed instrument on the committed tree now:
`python tools/codebase-map/replay-phrases.py --json` returns `hit_rate 0.593` at
`phrases_graded 140`. Units 8 and 4 landed after unit 10 and added symbols to
`memory/map/generated/symbols.json` (+87 lines in this same diff), which is the corpus the ranker
scores, so the figure was stale by construction the moment the later units committed.

The identical phrase count is exactly what makes it look reproducible. The sibling fan-in bullet ten
lines above pins its base (`Measured at base c4fcf5ad`, `:79`); this one does not, and it is the
number that prices the trade-off the unit landed.

**Fix.** Re-run at HEAD and restate with the sha attached, the way `:79` already does. The harness is
committed, so pinning costs one line.

**Left-shift gate.** A memory-tree hygiene rule rather than a new script: a measured figure in a map
dossier carries the sha it was measured at, and the existing dossier-freshness leg can grep for a
bare decimal in a "measured" sentence with no `` `[0-9a-f]{8}` `` on the same bullet.

---

## What was looked for and not found

Every count here is from a complete run — 4/4 lenses and 5/5 skeptic batches returned, 0 died — so
these are absences within the lens brief rather than gaps left by a dead lens.

- **Unit 11 editing the driver this run is executed by.** The `MAP_CLI` declaration across six carriers and the reader in `unattended.sh`'s reuse-probed item drew lens attention as the highest-risk seam in the diff (a run modifying its own driver mid-run). No finding survived: the declaration is additive, the reader is inside an item that already existed, and the driver's own suite covers the item's shape. Noted rather than claimed clean — unit 11's spec is NOT closed, and its driver suite had not finished when this review was commissioned, so the suite's verdict is outstanding and is not evidence this review can substitute for.
- **Units 4 and 5 both moving the memory-recall kit version.** Checked for a lost bump or a double bump; the version moved once and the manifest's `conf_digest` clause forces the one rebuild per node that the F7 comment describes.
- **Units 6, 8 and 10 all editing `reuse_lookup.py`.** F2, F3 and F4 are all products of this seam. No conflicting edit to a shared function body was found; the collisions are all between code and the prose describing it.
- **Security.** No new write path, no egress surface, no auth or sanitisation change in the diff. §9 has no purchase here.
- **`status-set-in-a-subshell`, `bounded-through-a-pipe-is-unbounded`, `heredoc-escape-reaches-the-regex`, `hookspath-resolves-into-another-checkout`.** Four checklist classes with live shell surface in the diff (`unattended.sh` +63/-…, `unattended.test.sh` +57). Applied, nothing found.

## Disposition

F1 and F2 are the landing bar. Both are single-commit fixes, and both are the same underlying
failure in different materials: a record asserting what the code does instead of deriving it. F3 is
one line in three files and should ride the same commit. F4 through F7 are worth folding before the
build closes, since each leaves a false claim in a closed unit's ledger or docstring. F8 through F11
can ride a follow-up row if the run is out of budget, but F9 and F10 are one-line edits and the
budget argument for deferring them is weaker than the cost of making the row.
