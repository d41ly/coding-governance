**Serves:** diff-review TOOL-aTunedCompass-1 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11

# aTunedCompass — closing diff review, round 2: reviewing the fold, not the diff it repaired

*Node `a`, 2026-09-05. A Tier-2 adversarial pass over ONE commit — `0afeb5f3`, the fold that
answered round 1 — and not over the range round 1 already read. 19 files, 625 insertions, 75
deletions. The scope is deliberate: re-reading `22d75b31...HEAD` would spend the pass on fixes
already verified and skip the only text in the build nobody has read, which is the fold itself. This
repo names that class at `memory/gotchas/fold-text-is-unreviewed-surface.md`. Four primed finder
lenses, a skeptic stage prompted to REFUTE every finding, one synthesis. The bug-class checklist
`gotchas.py --for-diff` selected for this range was the lens brief; `amendment-leaves-its-other-half-standing`,
`fixture-passes-by-finding-nothing`, `two-answers-to-one-question` and
`assertion-between-two-derived-values` account for ten of the eleven defects below. Every claim was
re-checked at source during synthesis, and every re-check that moved a claim — a corrected sha, a
swapped exemplar, two measurements taken over different populations — is named inside the finding
that carried it. Two of the fold's repairs changed real logic — F2's `derive_source_paths`
and F7's `ensure_cache` freshness predicate — and both were read for correctness rather than for
difference.*

**Range:** `b8b8768a...HEAD` (round 1's recorded tip to the fold), reviewed at `0afeb5f3`.

## Verdict: BLOCKED

One blocker, and it is the cheapest kind: the fold wrote 2070 B of prose into a gated slot and left
an unguarded merge-bar leg exiting 1 at HEAD. `python tools/memory-tree/gen_build_index.py --check-format`
reds today, in one command, on `chunk: records, subject: repo` with no guard — so every bar runs it,
including a records-only push. Nothing else here is a wrong answer in shipped behaviour.

The round's real story is the HIGH beneath it. Round 1's F2 was a BLOCKER; the fold fixed it
correctly and shipped it behind a regression arm that cannot fail. I deleted the entire F2
production fix from `derive_source_paths` and ran the suite: `29 executed, 0 skipped`, PASS, exit 0.
The fixture holds zero dossiers, so the branch the fix added is never entered. The build spent a
blocker on a defect and left nothing standing between it and its return.

The failure mode of this fold is the one round 2 of the spec audit found in the same commit:
**the amendment corrected one half of its claim and left the other half standing.** Six of eleven
defects are that shape — a backlog row closed for four siblings and not the fifth, a metric renamed
in the tool and not in its eight carriers, a measurement pinned to a sha on one bullet and not on
its twin twelve lines above, a dead symbol corrected in one bullet of a four-line block while the
bullet that carries the dead name was left alone. None of these is subtle once you look for the
pair; the fix each time is smaller than the sentence describing it.

**Review shape.** Raw 22 · confirmed 20 · refuted 2 · unverified 0 · precision 0.91.

**Run integrity.** Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. The run is COMPLETE:
every count above is zero, so an absence below is evidence of absence within the lens brief rather
than of a lens that never reported.

**Synthesis note on the finding count.** The pipeline discarded no duplicates, but the 20 confirmed
findings are 11 distinct defects — five were reported independently by more than one lens, and the
vacuous selftest arm was found by four. They are merged below with every contributing raw id named,
so nothing is lost and no defect is counted twice in the severity tally. The merges: F2 = raw 1 + 6
+ 11 + 18 · F3 = raw 4 + 7 + 12 + 19 · F4 = raw 3 + 13 · F6 = raw 15 + 21 · F11 = raw 16 + 22.

**Severity moves made at synthesis, named rather than buried.** F2's contributing raws split 3 high
/ 1 medium; I adjudicated HIGH after reproducing the staged break myself. F6's raws split 1 medium /
1 low; I took MEDIUM, because the broader raw is the correct one — the surviving carriers include
two acceptance criteria of CLOSED units. F10 stays LOW as reported.

---

## Findings

| # | Sev | Site | Defect | Raw ids |
|---|-----|------|--------|---------|
| F1 | **BLOCKER** | `memory/builds/aTunedCompass/README.md:66` | The fold overran a gated slot; an unguarded merge-bar leg exits 1 at HEAD | 17 |
| F2 | HIGH | `tools/codebase-map/selftest.py:992` | The `(a2)` arm written as F2's regression gate passes with the entire F2 fix deleted | 1, 6, 11, 18 |
| F3 | MEDIUM | `tools/codebase-map/reuse_lookup.py:433` | The fix made two derivations agree by hand-copying, under a docstring asserting there is one | 4, 7, 12, 19 |
| F4 | MEDIUM | `memory/backlog/TOOL.md:354` | Four falsified rows closed, a fifth left OPEN citing code this build deleted | 3, 13 |
| F5 | MEDIUM | `tools/codebase-map/reuse_lookup.py:57` | `SOURCE_PATHS_CAP`'s measured justification was measured against the derivation this fold replaced | 2 |
| F6 | MEDIUM | `tools/codebase-map/replay-phrases.py:214` | `median` → `upper-median` renamed in the tool, in none of its eight carriers | 15, 21 |
| F7 | MEDIUM | `tools/codebase-map/replay-phrases.py:129` | The ground-truth harvester counts paths the spec author declared MISSES as hits | 9 |
| F8 | MEDIUM | `memory/map/features/codebase-map.md:81` | F11's sha pin landed on one bullet; its twin twelve lines up still does not reproduce | 5 |
| F9 | MEDIUM | `memory/map/features/memory-recall.md:62` | The dead `fuse()` survives in the bullet above the one the fold corrected | 20 |
| F10 | LOW | `memory/map/features/codebase-map.md:108` | The illustrative `n_sources` figure was measured against the derivation this fold replaced | 14 |
| F11 | LOW | `tools/codebase-map/replay-phrases.py:195` | The new `unreachable` count re-types `measure_phrase`'s match predicate | 16, 22 |

---

### F1 — BLOCKER — the fold left the merge bar red

`memory/builds/aTunedCompass/README.md:66`

Reproduced at HEAD, without a pipe:

```
$ python tools/memory-tree/gen_build_index.py --check-format ; echo EXIT=$?
build-index FORMAT — authored content outside the slot contract:
    memory/builds/aTunedCompass/README.md — slot `## Build-level rules` is 4503 B over its declared ceiling of 1800 B
EXIT=1
```

It is the only FORMAT line in the whole run — `grep -c FORMAT` is 1. Every other build in the tree
reports ADVISORY only, which does not affect exit status. The leg is real and it is unguarded:

```json
{"name": "build README slot contract", "argv": ["python3", "tools/memory-tree/gen_build_index.py", "--check-format"],
 "chunk": "records", "subject": "repo", "ceiling": 300}
```

No `guard` key, so it runs on every bar, including the records-only commit that closes this build.

The growth curve, measured across the three revisions rather than asserted: the slot body is 1727 B
at the build base `22d75b31` (under ceiling), 2435 B at round 1's tip `b8b8768a` (already over), and
4505 B at HEAD. This fold contributed ~2070 B — more than the entire ceiling of excess in one
commit. Round 1 did not catch it because the slot was over by 635 B then and the leg was not run
against that tip; it is over by 2705 B now.

The failure is easy to miss for the reason this repo already wrote down: `$?` read after piping the
checker into `tail` reports `tail`'s status, not the checker's. That is
`memory/gotchas/never-read-a-suite-result-through-tail.md`, and it is very likely how the fold
convinced itself the bar was green.

**Fix.** Move the three new bullets out of the slot. Two of the three are already recorded verbatim
as decision entries at `memory/builds/aTunedCompass/RUN.md:56-59`, so the slot needs a one-line
pointer to them and not a second copy — one fact in one place, which is the rule the bullets
themselves are about. The spec-audit-rounds bullet belongs in the round-2 spec-audit record. Then
re-run `--check-format` with no pipe and confirm exit 0 before the closing commit lands. If the
prose genuinely has to live in the README, raise the declared ceiling with a recorded reason;
shipping the leg red is not an option and silently raising the ceiling to fit is not a fix.

**Left-shift gate.** The gate exists and works — what failed is that the run never saw its verdict.
Add the `--check-format` call to the unattended kit's pre-landing leg set so a run that will merge
with no owner turn cannot land over a red records leg, and make the invocation redirect to a file
rather than pipe, so the exit status the run reads is the checker's.

---

### F2 — HIGH — the regression gate for round 1's blocker cannot fail

`tools/codebase-map/selftest.py:992` · raw 1, 6, 11, 18 (four lenses, independently)

I staged the break at synthesis rather than trusting the lenses. Deleting the whole dossier branch
from `derive_source_paths` — that is, reverting the entire F2 production fix:

```python
        if ("affordance-seam" in c.sources or "shared-seams" in c.sources) and c.detail:
            where = "FOUNDATION.md" if c.detail == "foundation" else f"features/{c.detail}.md"
            add(f"{root_name}/{where}")
```

and running `python tools/codebase-map/selftest.py` gives `29 executed, 0 skipped (0 of 2 guarded)`,
PASS, exit 0. The `(c2)` end-to-end arm does not catch it either. Restored cleanly; the tree is
unmodified.

The cause is the fixture, not the assertion. `test_lookup_row_carries_sources` builds
`generated/symbols.json` plus an EMPTY `memory/map/features/` directory, so no candidate ever
carries `affordance-seam` or `shared-seams`. The run's own header prints it:

```
# corpus: 2 symbols | 0 inventory keys | 0 affordance seams | 0 dossiers
```

Both sides of the containment assertion therefore collapse to `{'src/text.py'}` whatever the
function does with dossiers. The arm's own comment says *"The reverse direction is the whole gate."*
It is not a gate at all on this fixture.

This is `fixture-passes-by-finding-nothing`, and §7's rule is explicit: a new gate is not landed
until its failing case has been observed. It plainly was not. The severity is HIGH rather than
BLOCKER because the shipped behaviour is correct — `derive_source_paths` does emit dossier paths, and
a live query confirms the two walks agree today — but this arm is also the only thing standing
between F3's two hand-copied derivations and a silent return of the original defect.

There is a second, quieter half. The `labelled` parse at `:997-1001` collects only `symbol def: ` and
`dossier: ` lines and silently discards every `inventory ...` line — which is precisely the one line
class where the two functions still genuinely diverge (F3). So even given a real corpus, the reverse
assertion is blind exactly where the remaining gap is.

**Fix.** Give the fixture a dossier so the branch actually runs: write `memory/map/features/text.md`
with a `## Reuse affordance` seam line naming `slugify` (or a `## Shared seams` block carrying the
`slug` stem), so `_sources` emits a `dossier: memory/map/features/text.md` line and `paths` carries
the same path. Then re-run the staged break above and confirm `labelled <= set(paths)` goes RED
before unstaging. While there, either parse `inventory ` lines into `labelled` too, or assert
explicitly that inventory lines are the ONLY sanctioned asymmetry, so a divergence of any other
class still reds.

**Left-shift gate.** The fixture header already prints `0 affordance seams | 0 dossiers` and nobody
read it. Make the arm read it: assert the fixture's own preconditions before asserting the
behaviour — `assert any("dossier: " in line for line in shown), "fixture carries no dossier; this arm proves nothing"`.
A fixture that stops producing the class under test then reds instead of passing, which is the
generalisable form of this defect and would have caught it at authoring time.

---

### F3 — MEDIUM — "ONE derivation, read twice" is now two derivations

`tools/codebase-map/reuse_lookup.py:433` (docstring) · `:441-462` and `:471-492` (the pair) ·
`memory/map/features/codebase-map.md:110` · raw 4, 7, 12, 19

Verified byte-level at source. `derive_source_paths` and `_sources` are two independent walks of
`shortlist.ranked`, and the fold copied three fragments verbatim from the second into the first:

- the repo-relative map-root resolution with its `ValueError` fallback (`:444-447` ≡ `:474-477`),
- the seam predicate `("affordance-seam" in c.sources or "shared-seams" in c.sources) and c.detail`,
- the dossier path `"FOUNDATION.md" if c.detail == "foundation" else f"features/{c.detail}.md"` (`:462` ≡ `:491`).

Neither function reads the other. The docstring at `:433` asserts *"ONE derivation, read twice:
`_sources` LABELS these"*, and the dossier at `codebase-map.md:110-111` describes the same data flow
(*"`derive_source_paths()` produces the set; `_sources()` labels it"*). Both describe a flow the code
does not have. The unit-8 ledger's AC3 — *"One derivation feeds both, so this holds by construction
rather than by luck"* — is the sharpest instance: the equality now holds by hand-copied bytes, which
is the definition of luck.

The docstring carries a second false sentence. It defends dropping inventory keys with *"An inventory
key with no file contributes nothing here, exactly as it contributes no openable path there"* — and
`_sources:494` prints exactly such a path: ``inventory `gate-legs` (see memory/map/generated/MAP.md)``.
Measured live: `reuse_lookup.py "resolve the python launcher"` renders 34 lines under
`## sources to open` while the log row records `n_sources: 32`, the two missing entries being the
inventory lines. The dropped set is spec-compliant — spec 8 says a file-less inventory key
contributes nothing — so the defect is the false justification, not the behaviour.

This is `two-answers-to-one-question`, re-created one level up by the fix for it, and per F2 nothing
can observe a future divergence.

**Fix.** Make it literally one walk. A private generator over `shortlist.ranked` yielding
`(label, path_or_None)`, with `_sources` rendering labels and `derive_source_paths` projecting the
non-`None` paths. Three duplicated fragments delete, and the docstring's claim becomes true by
construction rather than by assertion. Then correct the two prose carriers: the docstring's inventory
sentence and `codebase-map.md:110`.

**Left-shift gate.** With one walk there is nothing to gate. If the pair stays split, the gate is
F2's fixed arm plus one line making the sanctioned asymmetry explicit — the set of labelled paths
minus the logged paths must be exactly the inventory lines, never merely non-empty.

---

### F4 — MEDIUM — the fifth falsified backlog row is still OPEN

`memory/backlog/TOOL.md:354` · raw 3, 13

The row is live at HEAD, still `· OPEN ·`, and its quoted code no longer exists:

> TOOL-aWeighedCompass-12 · OPEN · THE REUSE PROBE TRUNCATES ITS NEIGHBOUR POOL ALPHABETICALLY,
> BEFORE RANKING. `tools/codebase-map/reuse_lookup.py` (`:243`) is
> `for name, reason in sorted(neighbours.items())[:NEIGHBOUR_CAP]`

`grep -rn 'sorted(neighbours.items())\[:' tools/` returns one hit, and it is the past-tense prose in
`selftest.py:1050` describing what the shipped code *used to* do. At HEAD `reuse_lookup.py:283-288`
ranks the whole pool, sorts it with `_derive_shortlist_key`, and only then slices `[:NEIGHBOUR_CAP]`,
with a dedicated arm `test_neighbour_cap_ranks_before_truncating`.

`git show HEAD -- memory/backlog/TOOL.md` proves the shape: the fold rewrote rows 5, 6, 10 and 17 in
this very hunk — rows 10 and 17 now read `CLOSED · … Closed by TOOL-aTunedCompass-8` and
`… Closed by TOOL-aTunedCompass-4` — and left row 12 untouched four lines below them. Round 1 named
four rows; the fold closed exactly those four. The instance, not the class. `grep -rn aWeighedCompass-12`
finds only this row and two roster lines, so the closure is recorded nowhere, and a future kickoff
reads a live row telling it to build a fix that shipped in this build.

One correction to the raw findings, which does not move the verdict: the closing commit is `36af6f9f`
("TOOL-aTunedCompass-6: the reuse probe ranks its neighbour pool before it truncates it"), not
`6aad7751`, which is unit 10's directory-scoping commit. Both raws named the wrong sha; one also
attributed it to unit 10 rather than unit 6.

**Fix.** Rewrite the row in place in the shape its four siblings now carry:
`TOOL-aWeighedCompass-12 · CLOSED · … The pool is ranked and then capped. Closed by TOOL-aTunedCompass-6 at `36af6f9f` → tools/codebase-map/reuse_lookup.py`.
Then re-scan the rest of the hunk for the same class rather than the rows a review happened to name.

**Left-shift gate.** A backlog row citing a file and a literal is checkable: extract the backticked
code fragment from each `OPEN` row that names a tracked path, and red when the fragment is absent
from that file. It would have caught this row and the four the fold did close, at the cost of one
scanner over `memory/backlog/*.md`.

---

### F5 — MEDIUM — the cap's measured justification no longer describes what it caps

`tools/codebase-map/reuse_lookup.py:57`

The comment reads *"the parent build measured a mean of ~17 file-backed sources per probe against
~71 ranked entries, so this is comfortably above the mean and below the 188-candidate outlier"*.
That was measured against the derivation this fold just changed. `derive_source_paths` now also emits
a dossier path per affordance-seam or shared-seams candidate, so the population `SOURCE_PATHS_CAP = 40`
bounds grew.

Two lenses measured it over different populations and I report both rather than picking one:

| Population | New derivation | Old (file-only) derivation |
|---|---|---|
| 179 recorded probe phrases | mean 34.11, median 35, max 50; **51 of 179 (28.5%) exceed the cap** | mean 18.97, max 32; **0 truncate** |
| 8 everyday phrases | mean 25.25, max 43 | — |

Both agree on the single phrase they share: `read the gate leg manifest` returns 43 sources under
the new derivation and 24 under the old. So a cap whose stated basis is "comfortably above the mean"
now truncates in routine use, at roughly double the mean it was sized against.

The impact is bounded and the finding says so: `n_sources` records the pre-cap count, so a truncated
row is visible AS truncated and nothing is silently lost. The defect is a derived count written in
prose beside the source that owns it, gone stale on the commit that changed the derivation — §7's
"NO count of a derived population is written in prose", broken by the comment explaining a constant.

**Fix.** Re-measure and restate. Either raise the cap above the observed max with the new figure
recorded, or keep 40 and replace the "comfortably above the mean" claim with the plain statement
that everyday probes now truncate and `n_sources` is how you see it.

**Left-shift gate.** Do not gate the prose — delete the need for it. Have the cap's rationale live as
a one-line derivation in `replay-phrases.py`'s summary (`sources per probe: mean/max over the graded
set`), printed on every replay run, and have the comment point at it. A number that is re-derived on
demand cannot be stale.

---

### F6 — MEDIUM — the metric was renamed in the tool and in none of its carriers

`tools/codebase-map/replay-phrases.py:214` · raw 15, 21

The fold acted on round 1's F8 by renaming the JSON key `median_rank_of_first_correct` →
`upper_median_rank_of_first_correct` (`:214`) and the printed label to `upper-median rank of first
correct` (`:228`). It touched nothing downstream. Every carrier still says "median rank":

- `memory/builds/aTunedCompass/spec/2026-09-04-spec-TOOL-aTunedCompass-6.md:151` and its **AC4** at `:229`
- `memory/builds/aTunedCompass/spec/2026-09-04-spec-TOOL-aTunedCompass-10.md:132` — also an **AC4**
- `memory/builds/aTunedCompass/build/2026-09-05-build-TOOL-aTunedCompass-6-acceptance-ledger.md:16` and `:39`
- `memory/builds/aTunedCompass/build/2026-09-05-build-TOOL-aTunedCompass-10-acceptance-ledger.md:22` — `| median rank of first correct | 2 | 2 |`
- `memory/map/features/codebase-map.md:83` and `:95`

Two of those are acceptance criteria of CLOSED units, and they require the harness to report a
statistic the committed harness no longer emits — anyone re-verifying AC4 by running the tool finds
no field by that name. The `:95` instance is the sharpest: the fold edited that very sentence in this
commit, adding the `6aad7751` pin, and left "the median rank are unchanged" standing inside the line
it was rewriting. Round 1's F8 text had already enumerated the dossier and both ledgers as the
figure's carriers, so the list was in front of the fold.

The surviving word is exactly the imprecision F8 was raised to remove: the upper of two middle values
is not the median.

**Fix.** Sweep the carriers to "upper-median rank of the first correct path". The two ACs belong to
CLOSED units, so give those a superseding line naming this finding rather than a silent edit to a
ratified record; the dossier lines and the ledger table row are plain edits.

**Left-shift gate.** The tool owns the name, so derive it: have `replay-phrases.py --help` and the
dossier both read the key from the summary dict, or — cheaper — add the bare word `median` (not
preceded by `upper-`) to the spec-token check's banned list for this build's records, which reds any
carrier that reintroduces it.

---

### F7 — MEDIUM — the harness grades declared misses as hits

`tools/codebase-map/replay-phrases.py:129` (`_parse_section10_paths`) · raw 9

Round 1's F6 had two halves: an undeclared denominator, and a ground-truth harvester with no notion
of negation. The fold declared the denominator — the `unreachable` block at `:186-198`, which is good
work — and left the harvester exactly as it was. `_parse_section10_paths` still harvests every
backticked path-shaped token in §10, including the ones the spec author wrote down as MISSES.

The skeptic stage refuted the finding's own example and then confirmed the class with two stronger
ones, so the finding stands on better evidence than it was filed with:

- `aWeldedTribunal-6`'s §10 says the probe *"did NOT name the seam"* and names the wrong candidates
  it returned instead. The replay scores that phrase `hit=true` at **rank 2**, matched on
  `tools/memory-tree/row_grammar.py` via the very candidate the author called wrong.
- `aWeldedTribunal-7`'s §10 says the probe *"did NOT name the seam"* and names `resolve` in
  `recall_conf.py`. The replay scores it `hit=true` at **rank 1**, on that file.

(The finding's own `aTunedCompass-8` example is defensible as a legitimate file-level hit — that §10
does name `reuse_lookup.py` as the seam the unit extends, and the instrument grades at file
granularity by declared design. The class is real regardless; only the exemplar moved.)

So the instrument counts self-declared misses as hits. That inflates `hit_rate` and contaminates the
new `phrases_truth_unreachable` count in the same direction — a miss-path that happens to be in the
corpus makes an otherwise-unreachable phrase look reachable. Those are the two figures the dossier
and two acceptance ledgers quote as the measured worth of the unit-6 and unit-10 ranker changes.

**Fix.** Teach the harvester negation, cheaply: drop paths that appear in a sentence containing an
explicit negative (`did NOT name`, `was never returned`, `only because`), or — better, because it
does not guess — restrict harvesting to the sentence or bullet that names the chosen seam, marked by
a convention the specs already nearly follow. Re-run and report the corrected hit rate beside the
pinned `6aad7751` figures rather than replacing them silently.

**Left-shift gate.** One arm over the tracked spec corpus: for each §10 that contains a negation
marker, assert the harvested truth set excludes the paths in the negated clause. It is a probe over
real data, so it will also print the near-misses — which per §7 is the point of running a candidate
predicate over the tree before wiring it.

---

### F8 — MEDIUM — F11's sha pin landed on one bullet and not on its twin

`memory/map/features/codebase-map.md:81-84`

Round 1's F11 said a cost figure did not reproduce at HEAD and pinned no sha. The fold fixed the
bullet at `:92`, which now reads *"Replayed at `6aad7751` over 140 phrases"* — verified to reproduce
at that sha. The identically-shaped bullet twelve lines above was not touched:

> **What the reorder is worth, measured rather than assumed.** Replayed over 140 recorded probe
> phrases … hit rate 0.579 → 0.600, while hit@5, hit@10 and the median rank of the first correct
> answer are all UNCHANGED at 0.371, 0.400 and 2.

Run at HEAD, `replay-phrases.py` reports hit rate 0.593, hit@5 **0.379**, hit@10 **0.414**,
upper-median 2. Neither 0.371 nor 0.400 nor 0.600 reproduces, and there is no revision named at which
a reader could check them. That is verbatim the round-1 finding, one bullet up, in the same file, in
the same commit that fixed the other one.

**Fix.** Pin it the same way — add the sha the 0.579 → 0.600 replay was run at (the intermediate
rank-then-cap commit, `36af6f9f`) — or re-run both bullets against one named sha and restate.

**Left-shift gate.** A dossier bullet claiming a replayed figure without a `` `sha` `` is
machine-detectable: red any line in `memory/map/features/` matching `Replayed` that carries no
backticked 7-or-40-hex token. Cheap, exact, and it generalises to every "measured at" claim in the
map tree.

---

### F9 — MEDIUM — the dead symbol survives one bullet above the one that was corrected

`memory/map/features/memory-recall.md:62`

`grep -rn 'def fuse' tools/memory-recall/` returns nothing; the function is `run_fusion` at
`query.py:761`. The dossier still reads:

> `fuse()` reads the chunk arm `k * ROLLUP_DEPTH` deep and keeps the best hit per parent before fusion

while the very next bullet, at `:68`, was corrected by this fold to *"There is ONE fusion call site,
`run_fusion`."* One bullet of a four-line block was fixed; the one carrying the dead name was not.
It is also the one a session greps when it opens the served chunk arm — a backticked symbol that
resolves to nothing.

Round 1's F9 named a second carrier the fold did not touch at all:
`memory/builds/aTunedCompass/build/2026-09-05-build-TOOL-aTunedCompass-4-acceptance-ledger.md:58`,
still *"holds ONE fused call site, `fuse()`"*.

**Fix.** `:62` becomes `run_fusion` — a plain edit to a live map record. The closed unit's ledger gets
a one-line superseding note naming this finding rather than an edit to a ratified record, the same
shape the run used for the aClosedDocket ledger.

**Left-shift gate.** The map tree already has the right instrument and it was not pointed here:
extend the dead-paths leg to backticked `name()` tokens in `memory/map/features/*.md`, resolved
against the symbol index the map already builds. A dossier naming a symbol that does not exist is the
same defect class as a dossier naming a file that does not exist, and one of the two is already gated.

---

### F10 — LOW — the illustrative source count was measured against the old derivation

`memory/map/features/codebase-map.md:108`

> **`n_shown` was NOT redefined.** It still counts RANKED CANDIDATES … measured on one live row,
> 39 ranked against 10 sources.

The log settles it. Two rows carry the query "unit 8 verification probe for the map log fields": the
`2026-09-05T11:44:07Z` row is `n_shown 39 / n_sources 10` — the pre-fix derivation the dossier quotes
— and the `2026-09-05T13:57:51Z` row, after the F2 fix, is `n_shown 39 / n_sources 17` on the
identical query. The fold changed what `n_sources` counts and left the number illustrating it
standing, unpinned, in the same file and the same commit where it pinned the sibling figure at `:92`.

Low because the bullet's *point* — that `n_shown` and `n_sources` are different numbers — survives
intact; only the illustration is stale.

**Fix.** Restate as `39 ranked against 17 sources`, or pin the old pair to the revision it was
measured at.

**Left-shift gate.** Covered by F8's suggested check if it is written to cover "measured on one live
row" as well as "Replayed": any dossier figure asserting a measurement carries the revision it was
measured at, or reds.

---

### F11 — LOW — the new `unreachable` count re-types the match predicate

`tools/codebase-map/replay-phrases.py:195-198` · raw 16, 22

`measure_phrase` at `:145` matches a truth path with
`f == t or f.endswith("/" + t) or t.endswith("/" + f)`. The `unreachable` sum the fold added at
`:196-197` spells the byte-identical relation again over `x` and `corpus_files`. Two hand-kept copies
of one rule, with nothing tying them together and no shared helper anywhere in the kit.

They agree today — 49 of 140 counted unreachable, and none of those also scores a hit — so this is a
latent divergence, not a live wrong answer. It matters because `phrases_truth_unreachable` is
documented at `:190-194` as the explanation of `hit_rate`'s denominator, and it stops explaining that
denominator the moment either copy is loosened. It is also the same class the fold's own F7 repair
removed from `query.py:633-652` on the identical argument, reintroduced in the file next door in the
same commit.

Correctly LOW: the file is on no merge-bar leg by owner ruling (2026-08-23, stated in its own header
and registered `project-owned` in `kit.toml`), so a divergence corrupts a hand-read diagnostic rather
than a gate verdict.

**Fix.** Three lines: `def _matches(f: str, truth: list[str]) -> bool`, called from both sites.

**Left-shift gate.** With one predicate there is nothing to gate. If both copies stay, the invariant
is one assertion in the harness itself — `assert not any(r["hit"] and _truth_unreachable(r) for r in rows)`
— which reds the moment the two spellings disagree, and costs nothing on a run that is already
walking the rows.

---

## What is NOT in this report

Stated so a zero is not read as coverage it does not have. Every lens and skeptic returned, so
absences below are absences within the brief rather than of a lens that never reported.

- **No security finding.** The fold touches no write path, no egress, no authorization surface.
- **No data-loss path.** F5's truncation is bounded and visible; F3's inventory omission is
  spec-compliant.
- **The F7 `ensure_cache` rewrite is correct on the thing that matters, and I read it at synthesis
  rather than inferring it from the absence of a finding.** `fresh` is unchanged: the generator
  yields exactly the old `and`-chain's nine clauses, `fresh = cause is None` is equivalent to the
  conjunction, and the `if man is not None` guard keeps every manifest-dependent clause unreachable
  when there is no manifest. The claimed performance repair is real — the old cause ladder ran BEFORE
  the early return and reached `corpus_digest` on the warm path, so a cache hit walked the corpus
  twice; the generator is lazy and `corpus_digest` is its last clause, so it is now computed once.
  One behavioural delta is NOT named in the comment and is worth recording even though it is not a
  finding: the reported cause changes precedence in two overlapping-failure cases — `--force` with no
  manifest now reports `forced` where it reported `no manifest`, and a missing database alongside a
  stale corpus digest now reports `a missing database` where it reported `corpus digest`. Both new
  answers are the more actionable one, and nothing consumes the string: `REBUILD_CAUSE` is read at
  exactly one site, `query.py:1285`, to print a status line, and no test asserts any cause value.
- **Nothing was reviewed outside `b8b8768a...HEAD`.** Round 1's range is not re-read here by design,
  so this report asserts nothing about the round-1 fixes except where the fix text itself falls inside
  the fold and a finding above names it. Two round-1 findings are touched by nothing here and their
  status is therefore UNASSERTED rather than verified: F3 (the `--help`, docstring and agent-instruction
  copies of the pre-unit-10 neighbour predicate) and F10 (the `grade` → `measure_phrase` rename
  reaching the `--help` prose). Round 3 should confirm both rather than inherit this silence as a pass.

## Landing bar for round 3

F1 must be fixed and `--check-format` must exit 0, read without a pipe. F2 must be fixed and its
failing case OBSERVED — the staged break in this report is the test of the fix. F4 is one line and
closes a row that will otherwise send a future session to rebuild shipped work. The rest can land as
fixes in the same commit, but F3 and F6 are the two that will otherwise be found again in round 3,
because both are amendments with a half still standing and this fold is the second consecutive one to
produce that shape.
