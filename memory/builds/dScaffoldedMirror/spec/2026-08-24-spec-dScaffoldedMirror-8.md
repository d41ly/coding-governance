# TOOL-dScaffoldedMirror-8 — the shipped frozen canon, and `--probe`

**Status:** INPROGRESS · rev-2 · 2026-08-25 · node d · Tier-2 · base 9ddcc5c9 · streams tooling

## 1. Goal

`--scaffold` ranks the graded corpus's own leading tokens and adopts the top 25 as an allowlist, so
a repo that consistently does the wrong thing legalises it — measured on the owner's demo: all five
reported offenders were in the vendored kit, four of the 25 proposed "verbs" were not verbs, and
every deliberately-bad name passed green. Replace that derivation with a kit-owned frozen canon of
concept clusters whose first element is the proposal unconditionally, so no token outside the canon
can enter a `VERBS` table at any frequency and at any threshold. The corpus stops selecting the
standard and is admitted as evidence for exactly one thing: which spellings become debt rows.

## 2. Scope (IN)

- **S1** — a new `tools/lexicon/canon.py`: frozen concept clusters, each an ordered tuple of
  English surface forms plus a gloss, with `role = "engine"` in `kit.toml` so an upgrade overwrites
  it and an adopter cannot edit it. The rev-1 proposal is 20 clusters, published in §4.
- **S2** — the selection rule, which is the whole unit. Which clusters enter a proposed table is
  decided by the corpus (a cluster with at least one live site enters). Which form REPRESENTS a
  cluster is decided by the canon, always element 0, never by any count. The two questions have two
  different answers and conflating them is the defect.
- **S3** — `--probe`: read-only, no arguments, no state, exits 0 unconditionally, and legal
  against any repo at any time including one with no `.lexicon.conf`. It reports per cluster which
  forms are live, how many sites each has, and what convergence would cost.
- **S4** — `--probe --write`: writes the proposed `VERBS` block into the conf and the debt ledger
  to `tools/lexicon/lexicon-debt.tsv`. It REFUSES on a conf whose `ratified` stamp is non-empty,
  naming the refusal — it is an adoption-time verb, not a maintenance verb, and gov's own conf
  carries about 70 lines of pin archaeology a rewrite would silently destroy.
- **S5** — delete the frequency allowlist from `scaffold_lexicon.py`: the `collections.Counter`
  loop, `SEED_VERBS`, the `verb_offenders` arithmetic and the three pin lines it heads. The
  scaffold's `VERBS` block becomes the canon's proposal for that corpus.
- **S6** — the structured NOT-clause grammar. A `VERBS` row becomes a verb, a gloss, and one or
  more `` NOT `<token>` `` clauses that `lexicon_conf.py` parses into a set. Two asserts inside the
  existing check: every row carries at least one negative, and no declared negative is itself a row
  in the table.
- **S7** — backfill the 11 rows carrying no negative today (`add arm derive extract main measure
  print resolve run seed test`), with the clauses published in §4. S6 and S7 land in ONE commit.
- **S8** — carry `TOOL-dScaffoldedMirror-1`'s second finding in the same edit: seed `conf::dark`
  unconditionally, because the scaffold runs before the conf it writes is tracked and the adopter's
  first `git add .lexicon.conf` otherwise reds with UNDECLARED EXTENSIONS. Retiring half a defect
  row under a "retired" claim is the two-answers-to-one-question class.

## 3. Non-goals (OUT)

- **No dominance table, at any threshold.** Refuted in §4 and quoted there. This is not a knob
  left at a conservative default; the mechanism does not exist.
- **No assert that a declared verb must be a canon representative.** It would red this repo on
  landing day over `seed` and `arm`, two rows a human curated for cause, and the remedy would be
  deleting them or growing the canon on an adopter's demand — which is §12's "if the reflex on a
  refusal is to add a verb, the table has become a synonym list".
- **No new predicate and no gate reads the debt ledger.** The ledger is an output for a human
  doing a rename pass. Nothing reds on it being stale or absent, and it is regenerable in 0.44 s on
  gov.
- **`--scaffold` itself survives.** S5 deletes its frequency ranking, not the verb.
- **No `.ts`/`.tsx` extractor**, so `--probe` on `incms/main` reads 19.3% of that tree. `-13`.
- **No pin change and no waiver change.** `-4` owns waiver keying, `-9` owns the pins.
- **No P7 noun synonym gate.** The research pass demoted it into `--probe` output and it stays
  there.

## 4. Design

### The rule, in two lines

```
which CLUSTERS enter a proposed table   the corpus decides   (>= 1 live site in the cluster)
which FORM represents a cluster         the canon decides    (element 0, at every dominance level)
```

A cluster is live when ANY of its forms is live, including when its representative has zero sites.
That is the mechanism behind the polarity arm: `get`=1, `fetch`=1, `load`=0 makes the `load` cluster
live with two sites and proposes `load`, which has none.

### Data model

`canon.py` holds one frozen tuple per cluster and nothing else — no counts, no thresholds, no
adopter-readable knob:

```python
CANON = (
    Cluster("build", "create a new value and return it", ("create", "make", "construct", ...)),
    ...
)
```

`lexicon_conf.py`'s `_parse_block` return type for `VERBS` moves from `{verb: gloss}` to `{verb:
(gloss, frozenset(negatives))}`. Both current consumers survive that: `lexicon.py` uses the table
only for `if verb not in verbs`, which is a key test, and `--print-verbs` prints sorted keys.
`map_extractors.py` does not read it yet.

### Inventory — the rev-1 canon, 20 clusters

Element 0 is the representative. Every other form is unnominatable by the first-element rule.

| # | representative | other forms in the cluster |
|---|---|---|
| 1 | `build` | create, make, construct, generate, new |
| 2 | `load` | fetch, retrieve, hydrate, pull |
| 3 | `read` | get, list, access, obtain, consume |
| 4 | `write` | save, store, persist, put, flush |
| 5 | `parse` | decode, deserialize, unmarshal, convert |
| 6 | `render` | format, serialize, encode, stringify, marshal |
| 7 | `resolve` | lookup, locate, dereference |
| 8 | `check` | validate, verify, ensure, require, assert, is, has |
| 9 | `scan` | search, walk, traverse, iterate, crawl, find |
| 10 | `extract` | pluck, strip, harvest, mine |
| 11 | `measure` | count, tally, size |
| 12 | `derive` | compute, calculate, infer, deduce |
| 13 | `init` | setup, configure, prepare, install, bootstrap |
| 14 | `run` | execute, invoke, perform, dispatch, call, do, process, handle |
| 15 | `add` | append, insert, push, register, attach |
| 16 | `remove` | delete, drop, destroy, purge, detach, unregister |
| 17 | `set` | update, assign, apply, modify, mutate, patch |
| 18 | `print` | echo, emit, output, log, dump, report |
| 19 | `main` | entrypoint, start, boot, cli |
| 20 | `test` | spec, should, it, t, case |

The count is 20 rather than the research pass's "about 19" for one stated reason: `main` and `test`
are both structurally mandatory in a Python corpus and neither folds into the other. A scaffold that
proposed no `test` row would make every `test_*` function a P1 offender on an adopter's first run.

**Three measurements say this list is not one agent's taste.** Every one of the 11 negative
definitions a human wrote here on 2026-08-16 is exactly a non-first element of the cluster
containing its verb — `build` NOT create, `load` NOT fetch, `read` NOT get, `write` NOT save,
`parse` NOT convert, `render` NOT format, `check` NOT validate, `scan` NOT search, `init` NOT setup,
`remove` NOT delete, `set` NOT update. The canon reproduces a curated table it never saw. Second:
55.2% of the 14,659 definitions measured on `incms/main` already lead with a verb from this repo's
22-row table, in a repo that has never carried a `.lexicon.conf`, and all six of that corpus's
commonest off-table leaders land in a cluster (get and list to `read`, validate and require to
`check`, create and make to `build`). Third: of the ten non-verbs the 2026-08-16 curation deleted
from the derived seed, EIGHT (`t git kit signal bounded all repo no`) are in no cluster and are
unnominatable by absence, and the other two (`do`, `is`) are non-first elements of `run` and `check`
and are unnominatable by the first-element rule. Two closing mechanisms, no gap between them.

**Gov's ratified table exceeds the canon by exactly two rows, `seed` and `arm`, and that is legal.**
The canon bounds what a machine may PROPOSE. It does not bound what a human may ratify, and a row
outside the canon carries a hand-written negative rather than a canon-derived one.

### The structured NOT-clause grammar

A negative is a backticked token following the literal `NOT`, anywhere in the gloss:

```
  load      read a store into memory — NOT `fetch`, which implies a network call
```

The backtick requirement is not decoration. Measured against today's table: the pattern ``
NOT\s+`([A-Za-z]+)` `` matches exactly 11 rows, and a bare `\bNOT\b` word match also matches exactly
11 — so there is no un-backticked `NOT` anywhere in the corpus this grammar must govern, and it
parses all 11 existing rows with zero rewrites and zero false positives. The prose after the comma
is kept, because "which implies a network call" is the half a reader needs.

The two asserts run inside the existing `lexicon naming predicates` leg, against the conf rather
than the corpus. The second one (no negative is itself a declared verb) is satisfied today — the 11
declared negatives are `convert create delete fetch format get save search setup update validate`
and none is a row — and it earns its place forward: it is what stops a later unit admitting a verb
that some other row already banned. `-14` reserves `cmd`, which collides with nothing here.

### The 11 backfilled negatives

Nine are the non-first element of the verb's own canon cluster. `seed` and `arm` sit outside the
canon and take a hand-written negative, which is the general adopter case for a repo-specific row.

| verb | negative | the boundary it draws |
|---|---|---|
| `resolve` | `lookup` | a lookup returns a row; resolve returns the thing, RUNNING the candidate |
| `extract` | `pluck` | pluck names the taking; extract names the declared shape taken |
| `measure` | `count` | count is the arithmetic; measure counts a population and decides nothing |
| `derive` | `compute` | compute says a value was produced, not that it never has to be authored |
| `seed` | `install` | install claims the tool owns the result after; a seed is never overwritten |
| `run` | `execute` | the same word twice; one spelling, and this repo already runs processes |
| `arm` | `enable` | enable reads as a feature flag; arm makes a dormant CHECK live |
| `add` | `append` | append claims a position at the end; add claims only membership |
| `print` | `log` | log implies a level, a sink and a filter; print writes to stdout for a human |
| `main` | `start` | start names a lifecycle event; main is a module's one CLI entry point |
| `test` | `assert` | assert is one statement inside a test; test is what a harness collects |

### `--probe` and `--probe --write`

`--probe` takes no arguments, holds no state, writes nothing and returns 0 on every path including a
tree with no conf, no git history and no declared language. That is the property that makes it safe
to run against a stranger's repository, and it is the reason the debt count is REPORTED rather than
gated: a probe that can red is a probe nobody runs on someone else's tree.

Output is one block per cluster: the live forms with their site counts, the representative, and the
convergence cost as a site total. Off-table leading tokens in NO cluster are reported separately as
`unclustered`, because those are renames a human has to invent and the tool cannot propose one. On
`incms/main` that population is the large one — 1,458 distinct off-table leading tokens — and
calling it what it is beats a top-9 histogram that shows 1.2% of the live vocabulary.

`--probe --write` writes two artifacts. The `VERBS` block goes into `.lexicon.conf`, still marked
PROPOSED with `ratified=""`, so the existing `lexicon-ratified` hole still refuses an uncurated
table at the merge bar. The ledger goes to `tools/lexicon/lexicon-debt.tsv` with `role = "seed"`,
one row per site: `path::name`, the losing form, the canonical form, and a kind of `synonym` or
`unclustered`. Its header records the sha it was derived at.

### How this retires TOOL-dScaffoldedMirror-1

`-1` is `scaffold_lexicon.py:105-107` writing `SUFFIX_OFFENDER_PIN="0"` and `LAYER_OFFENDER_PIN="0"`
as string literals under a comment claiming all three are MEASURED against the corpus. It has been
found three times and fixed zero times, and the proposed fix each time was to patch that write path.
S5 deletes the write path instead. The scaffold stops emitting any pin VALUE: the three keys are
written empty, and `lexicon.py` already treats an empty pin as 0, so the adopter's first gate run
reds with the exact count to paste. That is the `lexicon-pins` hole discharged by the mechanism its
own `kit.toml` already names — "the probe is the gate itself: an unmeasured pin set fails it" — and
the false MEASURED claim has no text left to sit in. S8 carries `-1`'s second finding so the row
retires whole. `-9` later deletes the three keys entirely; this unit only stops lying about them.

### The two arms

**(a) Polarity, absolute.** A fixture repo of 500 `frobnicate_*` definitions in one tracked file.
Run `--probe --write`, parse the written conf through `load_conf`, and assert `frobnicate` is not a
row. Two further asserts stop it passing vacuously: the written `VERBS` block must be NON-EMPTY (a
`--write` that wrote nothing would otherwise score a pass), and `frobnicate` must appear in the debt
ledger as `unclustered` with 500 sites — which proves the tool SAW the 500 and declined to promote
them, rather than having failed to read the file at all.

**(b) Polarity under dominance, which is the arm that catches a regression.** A fixture with exactly
one `get_*` definition, one `fetch_*` definition, and zero `load_*` definitions. Four asserts:

1. `load` IS a row in the written table, though it has zero sites in the corpus. 2. `get` and
`fetch` are NOT rows, though they are the corpus's only leading tokens. 3. Both appear in the ledger
as `synonym` rows targeting `load`, at one site each — this is what proves the losing forms were
observed and beaten, not merely absent from the reader's view. 4. A cluster with zero live sites in
this fixture — `render` — is NOT a row. This is the assert that separates the correct design from
"print the whole canon", which would satisfy 1 and 2.

Under the refuted dominance table, assert 1 fails: `load` has zero sites and cannot be a leader, so
the proposal is `get` or `fetch`. Both fixtures are frozen as regression fixtures in
`tools/lexicon/selftest.py`, alongside the owner's original demo corpus.

### Files touched (estimate)

`tools/lexicon/canon.py` (new, ~140 lines, 20 rows and a gloss each). `tools/lexicon/lexicon.py`
(~190 lines: the probe verb, the cluster roll-up, the two conf asserts).
`tools/lexicon/lexicon_conf.py` (~35 lines: the negatives parse and the changed `VERBS` value type).
`tools/lexicon/scaffold_lexicon.py` (~60 lines DELETED, ~25 added). `tools/lexicon/selftest.py` (the
two arms plus a frozen-canon sentinel). `tools/lexicon/kit.toml` (the ledger's `seed` row).
`.lexicon.conf` (11 rows gain a NOT clause). `tools/lexicon/LEXICON.md` and `README.md`.

### Alternatives rejected

- **The dominance table — D3's proposal, and the one this design exists to refuse.** Adopt the
  corpus's leader when dominance reaches 0.80. Quoting the research pass: *"That is the demo defect
  one indirection down — a repo whose sessions all wrote `get_*` has dominance near 1.0 and `get` is
  adopted silently, and D3's own falsifiable day-1 claim (`get`=1, `fetch`=1, `load`=0 → propose
  `load`) is false under its own table, because `load` has zero sites and cannot be the leader."* A
  threshold does not fix it, because there is no threshold at which a mirror stops being a mirror;
  it only moves the corpus size at which the repo starts legalising itself. The rule is
  unconditional or it is the old design with a parameter.
- **Ship the canon as adopter-editable data (`role = "seed"`).** It is then a hand-kept table in
  every adopter, which is the shape the corpus derivation was replaced for. `engine` is the point.
- **Make the canon a conf key.** Same defect, one file closer.
- **Assert a declared verb must be a canon representative.** §3. It reds gov on day one and turns
  curation into menu selection.
- **Have `--probe` red on a debt count over some bound.** A probe that can refuse will not be run
  against an adopter's tree, which is the entire demand it was built for.

## 5. Production-readiness checklist

For Tier-2, the unresolved items below ARE the owner scope menu; §8 carries the forks.

- **security** — `--probe --write` is the one write path this unit adds. It refuses on a non-empty
  `ratified` stamp (S4), so it cannot silently overwrite a curated table, and it writes only inside
  the repo it was invoked in. `--probe` without `--write` opens no file for writing at all, which is
  what makes it safe to point at a repository the operator does not own.
- **perf / scale** — one full corpus pass: 0.44 s on gov, about 4.7 s on `incms/main`. Run on
  demand, never on the merge bar. The two conf asserts (S6) are O(rows) against a 22-row table and
  cost nothing measurable on the bar leg they join.
- **a11y** — N/A. A CLI checker with no rendered surface.
- **i18n** — N/A for the tool. The canon is English surface forms by construction and says so; an
  adopter whose identifiers are not English gets `unclustered` rows and a hand curation, which is
  the honest output rather than a wrong proposal.
- **error / empty / loading states** — the empty corpus is the case that matters: `--probe` on a
  tree with no extractable definitions must print that it found none and still exit 0, and `--probe
  --write` on that tree must write NO `VERBS` rows rather than the whole canon. Arm (b) assert 4 is
  the same property at cluster granularity.
- **observability** — every proposal line names the cluster it came from and the site count that
  made the cluster live, so a reader can see WHY a row was proposed without re-running anything.
- **risks** — the landing-day red is S6: arming the at-least-one-negative assert reds `lexicon
  naming predicates` immediately, because 11 of 22 rows carry none today. S7's backfill must be in
  the SAME commit. Second risk: `lexicon_conf.py`'s changed `VERBS` value type is a contract change
  to the one reader three consumers share; both current consumers are key-only and survive, and
  `map_extractors.py` does not read it yet. Rollback is deleting the kit's three legs, which is the
  standing opt-in property.
- **testing + left-shift gates** — the two arms above plus the frozen-canon sentinel, all inside
  the existing `lexicon selftest` leg. The class is the derived-standard defect the whole build
  names; its gotcha is `memory/gotchas/pin-copied-from-another-corpus.md`'s neighbour, and if no
  class file covers "a standard derived from its own subject", this unit writes one.
- **migration / rollback** — `.lexicon.conf` gains 11 NOT clauses and loses nothing. No persisted
  artifact changes shape. The debt ledger is new and no gate reads it, so deleting it is a no-op.
- **user docs** — `tools/lexicon/LEXICON.md` gains the canon's rule in two lines and the `--probe`
  verb; `README.md` gains the ledger's meaning and the statement that nothing reads it.

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py --probe --write` runs over a fixture of 500
  `frobnicate_*` definitions, `frobnicate` is absent from the written `VERBS` block, that block is
  non-empty, and `tools/lexicon/lexicon-debt.tsv` carries `frobnicate` as `unclustered` with 500
  sites.
- **AC2** — When the same command runs over a fixture with one `get_*`, one `fetch_*` and zero
  `load_*` definitions, the written table contains `load` and contains neither `get` nor `fetch`.
- **AC3** — When that fixture's ledger is read, `get` and `fetch` each appear as a `synonym` row
  targeting `load` at one site, and `render` is absent from the written table — the two asserts that
  stop AC2 passing over a tool that printed the whole `canon.py`.
- **AC4** — When `python tools/lexicon/lexicon.py --probe` runs against a tree with no
  `.lexicon.conf`, no declared language and no definitions, it exits 0, writes no file, and says it
  found nothing.
- **AC5** — When `python tools/lexicon/lexicon.py --probe --write` runs against a conf whose
  `ratified` value is non-empty, it refuses, names the stamp, changes no file, and exits non-zero.
- **AC6** — When a `VERBS` row carrying no `` NOT `<token>` `` clause is staged into
  `.lexicon.conf`, `python tools/lexicon/lexicon.py` reds and names that row. Staged, observed RED,
  unstaged.
- **AC7** — When a `VERBS` row declares a negative that is itself a row in the table, the same
  check reds and names both rows. Staged, observed RED, unstaged.
- **AC8** — When `python tools/lexicon/lexicon.py` runs on this repo after S7's backfill, it is
  green and all 22 rows parse at least one negative — asserted by a selftest arm counting them, not
  by reading the file.
- **AC9** — When `bash tools/lexicon/adopt-lexicon.sh --scaffold` runs on a fresh repo carrying
  only `class OrderManager` and `def do_thing()`, the written conf proposes no `do` row, writes
  `conf::dark` in `LANGS`, and writes the three `*_OFFENDER_PIN` keys EMPTY rather than as `"0"`.
- **AC10** — When `python tools/lexicon/selftest.py` runs, it covers AC1 through AC3 and AC9, and
  a fixture that stops carrying its 500 definitions fails the suite rather than passing silently.

## 7. Gates

Keeps green: `lexicon naming predicates`, `lexicon selftest`, `lexicon wiring`, `memory hygiene`,
and the kit version markers (`KIT_LEXICON_VERSION` and the `gov:kit lexicon@` markers move
together). Adds NO new gate leg. S6's two asserts are new refusals inside `lexicon naming
predicates`, and the canon sentinel is a new arm inside `lexicon selftest` — the leg count is not
the coverage, and a new leg here would only advertise that a conf assert needed its own process.

## 8. Open questions

- **F1 — are the 20 clusters published in this spec, or derived at build time?** RECOMMENDATION:
  published, and this spec's §4 table is the reviewed rev-1 list. The canon is the one artifact in
  the kit that must NOT be derived from any corpus, so a list authored at build time by the same
  agent that writes the code has no review boundary at all — it would be exogenous only in the sense
  that nobody checked it. Publishing puts it in front of a reader before it freezes. The cost is a
  second copy: `canon.py` is the source from the moment it lands, and §4's table is a rev-1 record
  that §9 dates, not a maintained mirror — a later cluster edit bumps `canon.py` and logs a rev
  here, it does not re-render the table. RESOLVED (agent, 2026-08-24, delegated): published in §4,
  with `canon.py` canonical from landing.
- **F2 — does `-8` retire `TOOL-dScaffoldedMirror-1` wholly or only its first finding?** The row
  carries two: the hardcoded pin literals under a MEASURED comment, and the scaffold running before
  its own conf is tracked so `conf` cannot reach `LANGS`. S5 removes the first one's subject; the
  second survives untouched unless carried. RECOMMENDATION: carry it, as S8. It is one line in a
  file this unit is already rewriting, and a row marked retired with a live defect in it is worse
  than an open row. RESOLVED (agent, 2026-08-24, delegated): retire it whole, via S8.
- **F3 — NEW DEPENDENCY EDGE, not in the build's stated set: `-8` wants `-3`.** `--probe` derives
  which clusters are live from the corpus, and `lexicon.py:125-129` is `git ls-files` with no
  exclusion, so a vendored kit's own files vote. Under the OLD design that edge was hard: the corpus
  selected the vocabulary, so pollution chose the standard. Under this design it is soft and
  bounded, and the difference is the design working — a polluted corpus can only make an extra
  cluster enter (curated away in the same pass) or add ledger rows in files nobody owns (noise). It
  cannot change which form represents a cluster, because no count is consulted for that.
  RECOMMENDATION: state the edge, do not block on it; `-3` is Phase 0 and lands first anyway. `-3`'s
  spec does not yet carry the reciprocal "unblocks `-8`" line and that line is owed to it. RESOLVED
  (agent, 2026-08-24, delegated): soft edge, recorded here, reciprocal owed in `-3`.
- **F4 — is 20 the right count when the research pass said about 19?** RECOMMENDATION: 20, with
  the reason in §4 — `main` and `test` are both structurally mandatory and neither folds into the
  other, and dropping `test` would make every `test_*` function an offender on an adopter's first
  run. The number is not a target and the spec does not defend it as one. RESOLVED (agent,
  2026-08-24, delegated): 20 clusters at rev-1.
- **F5 — should the debt ledger be tracked in git, or written and left untracked?** Genuinely
  open, and it is an owner call because it is a policy about adopter repos rather than a mechanism.
  Tracking it makes drain visible in a diff; leaving it untracked keeps a derived population out of
  the tree, which is §7's own rule. RECOMMENDATION: ship it as `role = "seed"` so an adopter who
  wants drain-in-git gets it and one who does not deletes the file with no consequence, since no
  gate reads it either way. RESOLVED (agent, 2026-08-24, delegated): `seed`, unread by any gate.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, grounded on recommendation R7 of the `dScaffoldedMirror`
  research pass (`build/2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md`)
  and on the read-only probe of `incms/main` taken the same day with the kit's own extractor. Two
  additions the research pass left implicit rather than decided, neither an overturn: the debt
  ledger is computed against the RATIFIED table rather than the canon alone, so a form an adopter
  declares in its own right is a sibling and not debt; and cluster LIVENESS is measured over the
  whole cluster rather than over its representative, which is what lets a zero-site `load` be
  proposed at all. The cluster count is 20 rather than the pass's "about 19", per F4.
- rev-1 status 2026-08-24 · KEPT and SPLIT at the S5/S6 seam by the owner ruling. S6/S7 (the structured NOT-clause grammar and the eleven backfilled negatives) land FIRST, in Phase 0, because `-10`'s message depends on them. `--probe --write`, the debt ledger and its seed artifact are CUT: no gate reads them and no adopter exists to run them.

- rev-2 · 2026-08-25 · S6 and S7 BUILT and landed FIRST, ahead of S1-S5 and S8, which is the split
  the spec-set review recommended: `TOOL-dScaffoldedMirror-10`'s `--suggest` message consumes this
  grammar and cannot be built without it. The eleven backfills are the clauses §4 published, and the
  measurement §4 rests on held: the backticked pattern matched exactly the rows a bare word-match
  did, so all 23 rows parse with zero rewrites and zero false positives.
  ONE INTEGRATION COST, recorded because it is the assert working rather than a defect: adding a
  DECLARATION-shaped check means every fixture conf must satisfy it, and the suite's own `BASE_CONF`
  had an `add` row with no negative — 15 arms redded at once until it was given one. A check whose
  subject is the conf reaches every fixture that writes a conf.
  `build_negatives` is so named because `negatives` leads with a token outside the table; the pin
  stayed at 384, which is the fifth unit running where a new definition took a declared verb rather
  than a raise.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py canon cluster proposal scaffold vocabulary probe` returns
no seam this unit can wire through, and that is the real answer rather than a shrug. The ranked hits
are `hook_probe` (`tools/govkit/govkit.py`, fan-in 0), `t_scaffold_converges`
(`tools/memory-recall/selftest.py`, fan-in 0) and `test_js_probe_against_the_lexicon`
(`tools/codebase-map/selftest.py`, fan-in 0) — three name-stem matches on the words `prob` and
`scaffold`, none of them a mechanism for proposing a vocabulary. The only affordance seams offered
are prose matches in the `unattended`, `govkit`, `install-prefix` and `playbook` dossiers, reached
through the word "vocabulary" in unrelated sentences. The lookup's own closing note applies and is
worth repeating: the bash layer has no symbol extractor, so `adopt-lexicon.sh` would not appear
above whatever it contained.

There is no existing frozen-vocabulary artifact anywhere in this repo. The nearest structural
relative is `codebase-map`'s `memory/map/baseline.toml`, a shrink-only registry — and it is a shape
to learn from rather than a seam to wire through, because `.lexicon.conf`'s `LAYERS` rule forbids
`tools/lexicon/*` importing `tools/codebase-map/*` precisely so the kit ships self-contained. The
reuse that DOES apply is internal and is a split rather than a new helper: `scaffold_lexicon.py`
already calls `lex.tracked_files`, `lex.ext_of`, `lex.extract` and `lex.leading_verb`, and `--probe`
is the same four calls with the counter loop replaced by a cluster roll-up. Nothing new is
introduced on the extraction side, which is the intended answer — the defect was the polarity of one
derivation, not a missing mechanism.
