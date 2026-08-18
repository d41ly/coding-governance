# Review — aWalkedCorpus, round 4 (the BUILT unit, TOOL-aWalkedCorpus-3)

**Serves:** diff-review TOOL-aWalkedCorpus-3

## Verdict: SHIP WITH FIXES — 0 blockers, 2 high

*Review shape: **raw 21, confirmed 17, refuted 4, unverified 0, precision 0.81.** Against the
worktree at HEAD `9d41abb`, declared base `3e5c6d43`. The 17 confirmed rows collapse to **11
distinct findings** after merging three duplicate clusters (three lenses filed the temp-dir leak,
two the `CheckRefused` escape, two the overlap dead-probe, two the `hits` header contradiction, two
the `sys.path` ordering). Every row in the table below was **re-executed here** before it entered
it; one was **elevated** on re-execution and one **narrowed**, both recorded under Report limits
rather than silently.*

*The tree was not mutated. Every degradation was constructed in `mktemp` scratch dirs over an
already-extracted corpus; no tracked file was edited. (`memory/builds/aWalkedCorpus/RUN.md` was
already dirty at session start and is not mine.)*

## The central claim holds

**"The two predicates can each red ALONE" — VERIFIED, by running the arms and by construction.**

```
ok  the FLOOR reds alone (per-id stays green) — floor RED at 0.7500, per-id ok
ok  PER-ID reds alone (the floor stays green and RISES) — per-id RED naming the id, floor ok at 0.9091
```

`python tools/memory-recall/test_recall_floor.py` → **16/16 arms green** on this tree, and the two
independence arms are not tautological: the per-id arm's floor does not merely stay green, it *rises*
to 0.9091, which is the honest signature of a retirement (the ceiling drops faster than the hits do).
The full bar is **65/65 legs** and `tools/gate-legs.json` registers both new legs as claimed.

The design's load-bearing choices also survive attack. Importing `bench.py`'s scorers rather than
extending it is correct given `bench.py` always returns 0 and is byte-pinned by `verbatim.json`. The
ceiling-normalised comparison genuinely reduces to `h/R`. The pin **0.81** is a real derivation, not a
cherry-pick: `(h-1)/(R-1) = 9/11 = 0.8182` at `h=10, R=12`, reproduced by `--audit-fixture` here.

**But the third guard — the anti-tautology overlap audit — is disarmable in silence.** That is F2,
and it is the finding I would fix before this lands, because it is `fixture-passes-by-finding-nothing`
inside the gate written to close that class.

---

## Findings

### F1 [HIGH] Every arm leaks a full corpus copy — 15 dirs / ~120 MB per bar run, forever

`tools/memory-recall/test_recall_floor.py:87`

`build_filtered()` does `dst = pathlib.Path(tempfile.mkdtemp(prefix="recallarm-"))` and returns it.
Nothing ever removes `dst`. `main()` (`:367-368`) rmtrees only `_BASE`. There are **15
`build_filtered()` call sites**, so one leg run orphans exactly 15 directories, each holding the
repo's whole extracted decision corpus (`records`/`chunks`/`spine`/`anchors`) at ~8 MB.

**Measured here, before/after a single run:** 240 → **255** surviving non-base `recallarm-*` dirs in
`%TEMP%`. The accumulation on this node is now **~2 GB**. Thirty stray `recallarm-base-*` dirs are
also present, so the `ignore_errors=True` base cleanup is not reliable either.

The asymmetry is what makes this an omission rather than a convention: `check-recall.py`'s own
`build_data_dir` scratch is removed in a `finally` (**0** surviving `check-recall-*` dirs), and this
same file's `recallfx-`/`recallconf-` dirs all rmtree. It also contradicts the unit's stated security
posture — "writes only inside `mkdtemp()`" is only safe if something removes it.

The `recall floor arms` leg is guarded on `tools/memory-recall/` and `memory/`, and `memory/` moves on
nearly every records-touching commit; `.githooks/pre-push` sets `GATE_FULL=1`, so every authoritative
push adds another ~120 MB on every node, unbounded.

- **Fix.** Track each dir in a module-level `_SCRATCH: list[pathlib.Path]`, append in
  `build_filtered()`, and `for d in _SCRATCH: shutil.rmtree(d, ignore_errors=True)` beside the
  `_BASE` cleanup at `:367-368`. Cheaper still: memoise `build_filtered` on its predicate — ten arms
  pass `drop=None` and could share one copy.
- **Left-shift gate.** Add an arm that snapshots `len(list(Path(tempfile.gettempdir()).glob('recallarm-*')))`
  at start and end of `main()` and fails on a nonzero delta. This is a general class worth a gate leg
  of its own: a repo-wide scan for `mkdtemp(` call sites with no `rmtree`/`finally`/`TemporaryDirectory`
  in the enclosing function, in the shape of `check-arms.py` (which today scans `.sh` only and
  therefore cannot see any of this).

### F2 [HIGH] The anti-tautology audit has no liveness assertion and reads 0.000 when it measures nothing

`tools/memory-recall/check-recall.py:203-211`

*Elevated from the two [medium] rows that filed it, on evidence found here — see Report limits.*

`measure_overlap` re-implements target resolution as `by_id[r["id"]]` (`:204-206`) instead of reusing
the `p["targets"]` that `measure_run` already computed through `bench.expected_by_target`. Any
question whose targets it cannot resolve gets `homes 0` and `overlap 0.000` — which the predicate
scores as a **PASS**, the most independent row in the table. That inverts AGENTS.md's own rule that "a
probe that cannot move prints DEAD PROBE instead of a reassuring 0".

Two reproductions:

**(a) Structural, whole-set.** `parse_pin` admits `chunks` (it is in `SETS`), but chunk-level docs
carry no `id` — `bench.expected_by_target`'s own docstring says so — hence `by_id` is empty and
**every** question reads 0.000. Under `RECALL_FLOOR="chunks:fts5:r@5>=0.05"`:

```
overlap: max 0.000 mean 0.000  (OVERLAP_MAX 0.60)
derivation: h=2 R=12  (h-1)/(R-1) = 0.0909  declared RECALL_FLOOR 0.05
EXIT=0
```

All twelve rows print `homes 0 / overlap 0.000`. The guard the design leans on hardest is vacuous for
a whole in-vocabulary set.

**Sharper than filed:** the earlier lenses saw the `hits` predicate red incidentally here and had to
work around it. It is **opt-in** — `check_audit` fires only `if row["declared_hit"] is not None`
(`:241`) — so a fixture that simply *omits* the `hits` column, which nothing requires, gets the
EXIT=0 above with the overlap guard fully disarmed. The backstop is not a backstop.

**(b) Per-question, on the shipped `records` pin.** Retiring one expected id makes that row read
`homes 0 / overlap 0.000` and drags the summary `mean` from 0.362 to 0.348 — a row that measured
nothing averaged in as a maximally-good row — while the audit stays EXIT=0. Per-id never runs to
contradict it, because audit mode returns early at `:297`.

The signature-level tell: `measure_overlap(run, pin)` **never reads `pin`** (`:194-219`). It is
records-only while being applied to whatever set the pin names.

- **Fix.** Build `target_terms` from the run's own resolution, which resolves chunks through the
  anchor map exactly as the scorer does:
  `for i in {d for hs in p["targets"].values() for d in hs}: target_terms |= set(bench.terms(run["docs"][i]["text"]))`.
  Then add the liveness failure: `homes == 0` → `question N resolves no target — overlap is NOT
  MEASURED`. Exclude un-measured rows from the max/mean summary. Either drop the unused `pin`
  parameter or use it to refuse the audit when the graded set's docs carry no `id`.
- **Left-shift gate.** Two arms: one driving `--audit-fixture` under a `chunks:` pin and asserting a
  NOT MEASURED red (not a 0.000 green), one retiring a single expected id and asserting the same.
  Generalise: this repo already has the `DEAD PROBE` convention in `drift-audit` and `lexicon` —
  a shared assertion helper (`assert_probe_live(population, name)`) used by every new measurement
  predicate would have caught this at authoring time.

### F3 [MEDIUM] `build_data_dir`'s refusal escapes `main()` uncaught — the bar's own path is the untested one

`tools/memory-recall/check-recall.py:284`

`data = scratch = build_data_dir(root)` sits in a `try` whose only clause is `finally:` (`:328`). The
`except CheckRefused` at `:287` wraps **only** `measure_run`, so the `CheckRefused` raised at `:153`
escapes. Reproduced with a `--repo` carrying a conf but no git repo:

```
EXIT=1   Traceback lines: 2   "REFUSED" lines: 0
```

— a two-level Python traceback (`CheckRefused: extract.py failed (1)` wrapping extract.py's
`CalledProcessError`) and exit **1**, not `check-recall: REFUSED -- ...` and exit **2**. Exit 1 is
this program's *"a predicate failed"* code, so on the bar a broken extraction is indistinguishable
from a genuine recall-floor regression — the opposite of what the module docstring's "THREE
PRECONDITIONS stop the run" contract promises, and what all four refusal arms assert.

Coverage is the sharp end: **every one of the 16 arms passes `--data-dir`**, while the `recall floor`
leg is `python3 tools/memory-recall/check-recall.py` with *no* `--data-dir`. The gate's own branch is
the one branch no arm drives, and `check-arms.py` scans `.sh` only, so the meta-gate cannot see it.

- **Fix.** Move the data-dir construction inside the existing handler, the same shape already used at
  `:276-278` and `:287-289`, returning 2. Add an arm forcing an extract failure that asserts exit 2
  **and** no `Traceback` in the output, matching `test_out_of_vocabulary_pin_reds`.
- **Left-shift gate.** An arm-coverage assertion: every documented precondition in the module
  docstring's table must have an arm that reaches it **through the leg's own argv**. More broadly,
  extend `check-arms.py` beyond `.sh` to `.py` engines — its "every `fail` branch armed by a positive
  assertion naming its own failure text" rule is exactly the rule that was needed here.

### F4 [MEDIUM] `read_fixture` validates the container, not the questions — a hand edit crashes three branches later

`tools/memory-recall/check-recall.py:108`

`read_fixture` (`:101-110`) checks only is-file / JSON-parseable / `queries` is a non-empty list.
Nothing validates a question object. Reproduced against `{"queries":[{"expected_ids":["TOOL-aStandingWrit-2"]}]}`:

```
KeyError: 'query'    EXIT=1
```

raised at `:180` inside `bench.rank_with(..., q["query"], ...)` — again exit 1, reading as a floor
regression rather than a precondition refusal. Non-string entries in `expected_ids` fail the same way
via `.strip()` at `:177`. Reachable by any hand edit of the committed fixture or via `--fixture`,
which is exactly the maintenance path the fixture exists to support.

- **Fix.** After the list check, refuse any element that is not a dict or carries no non-empty string
  `query`, naming the 1-based index:
  `raise CheckRefused(f"fixture question {i} carries no \`query\`: {path.as_posix()}")`. Same for
  non-string `expected_ids`. Add an arm asserting that message.
- **Left-shift gate.** Validate the fixture against a declared shape (a small stdlib schema check) in
  precondition 1, and arm it. The class — "a precondition validates the container and not the
  elements" — is worth a line in `memory/gotchas/`.

### F5 [LOW] The derivation guard fires in one direction; three records claim it fires in both

`tools/memory-recall/check-recall.py:251`

The guard is `if headroom == headroom and headroom < pin["value"]` — **loose-direction only**.
Deleting the two questions that declare `hits: false` moves R from 12 to 10, and `--audit-fixture`
prints `h=10 R=10  (h-1)/(R-1) = 1.0000  declared RECALL_FLOOR 0.81` and exits **0**. The pin is now
loose by 0.19 (it tolerates two further losses out of ten) with no complaint.

Three records overclaim: `.memory-tree.conf:137` ("reds if a fixture edit moved either"),
`tools/memory-recall/README.md:168-169`, and `memory/map/features/memory-recall.md:88-89` ("reds when
they disagree"). The code's own failure string — "the fixture moved h or R and the pin was not
re-derived" — is likewise broader than what it detects. The safety property (`pin <= headroom`) is
intact, which is why this is low; but a maintainer following the conf's own re-derivation instruction
reads that green as confirmation the pin is still the one-retirement worst case. The guarantee is in
fact enforced elsewhere — `test_recall_floor.py:284` asserts the literal `h=10 R=12` — so **the
records name the wrong instrument**.

- **Fix.** Either add the tight direction (fail when `headroom - pin` exceeds an intended margin,
  naming it a stale-loose pin), or narrow the three sentences to what the code does.
- **Left-shift gate.** `check-playbook-parity.sh` already machine-checks "a value the playbook STATES
  equals the source that OWNS it". Register the `RECALL_FLOOR` derivation as a declared pair so a
  records-vs-code divergence in this class reds on the bar rather than in a review.

### F6 [LOW] The kit's withholding rule binds `govkit apply` only; the documented copy-install ships all three

`tools/memory-recall/kit.toml:13`

The `project-owned` rule removes the three gov-only files from govkit's `apply` pool — its comment
says exactly that (`project-owned` is absent from `LANDABLE_ROLES`). But `WIRE-INTO-PROJECT.md:279`
(§3c step 1) is literally `cp -r <gov>/tools/memory-recall <project>/tools/memory-recall`, which
carries `check-recall.py`, `recall-fixture.json` and `test_recall_floor.py` straight into the adopter
tree — the outcome the rule's own comment says it prevents. The runbook's memory-recall
maintenance-class inventory at `:560-566` enumerates every *other* file in the kit by class and never
mentions these three, and no step in §3c or the §5 verification list tells an adopter to delete or
wire them.

Low because every downstream failure is loud (their `check-recall.py` refuses with `RECALL_FLOOR is
not declared`; the per-id predicate would red on gov ids) — but the withholding claim as written is
materially false for the one install path the shipped runbook documents.

- **Fix.** Add a `rm -f tools/memory-recall/{check-recall.py,recall-fixture.json,test_recall_floor.py}`
  step to §3c step 1 and name the three as gov-only in the §560 list — or narrow the kit.toml comment
  to say the withholding binds `govkit apply` only, citing the copy-install gap the charter tracks.
- **Left-shift gate.** Teach `check-install-prefix.sh`'s sibling class a new predicate: every file
  carrying a `project-owned` role in any `kit.toml` must be named in `WIRE-INTO-PROJECT.md`'s
  copy-install exclusion list. Two withholding mechanisms with one declaration is the actual fix.

### F7 [LOW] The `recall floor arms` guard omits `tools/govkit/`, which one arm imports and executes

`tools/gate-legs.json:436`

The leg declares `"guard": ["tools/memory-recall/", "memory/"]`, but `test_kit_payload_withholds`
(`test_recall_floor.py:338-358`) inserts `tools/govkit` on `sys.path`, imports `govkit`, and calls
`G.resolve_rule_pool(...)` — and it runs at import time via the `@check` decorator. A diff touching
only govkit (renaming `resolve_rule_pool`, changing `scan_claimed_paths`' destination-claim
semantics, adding the `exclude` key the arm's docstring says govkit lacks) skips the single arm
proving the three gov-only files stay out of the adopter payload.

The two govkit legs do not cover it: `govkit selftest` tests govkit, and `govkit selfcheck` would
stay green — a semantics change that made the rule stop withholding leaves those three files claimed
by the `**` rule, which selfcheck accepts. `.githooks/pre-push` sets `GATE_FULL=1`, so the merge
verdict stays right and only the early signal is lost — precisely the cost AGENTS.md says a
too-narrow guard buys.

- **Fix.** Add `"tools/govkit/"` to that leg's guard array. It classes as `kit-relative` under govkit
  selfcheck's 7c partition, so exactly one class matches and the selfcheck stays green.
- **Left-shift gate.** A run-gates canary predicate: for each leg, statically extract the paths its
  script imports or `sys.path.insert`s and assert each is covered by the leg's guard. This class
  ("the guard omits a dependency the leg executes") is mechanical and currently unwatched.

### F8 [LOW] The fixture's own header says `hits` is never read; a bar leg reds on editing it

`tools/memory-recall/recall-fixture.json:18`

The `_README` states `hits` is "documentation of the fixture's shape, not an input: nothing reads
it". `check-recall.py:218` reads it (`"declared_hit": q.get("hits")`) and `check_audit` reds at
`:241-244`; `test_recall_floor.py:317-334` exists solely to prove that red fires. So the file a
maintainer edits when the corpus moves tells them the column is free-form commentary, while an armed
leg reds on it — `memory/gotchas/two-answers-to-one-question.md`, with the two answers one commit
apart. The README (`:149`) and the map dossier describe it correctly; the fixture is the one wrong
surface. (Scope caveat: the read only happens under `--audit-fixture`, so the header is true of the
plain leg — but "nothing reads it" is false as written.)

- **Fix.** "`hits` is not an input to the SCORE — nothing in the grading path reads it — but
  `--audit-fixture` compares it against the measurement and reds on a disagreement, so it is
  documentation a gate keeps honest."
- **Left-shift gate.** Extend the hygiene engine's existing prose-vs-code parity family: any file
  asserting "nothing reads X" should have that phrase treated as a declared pair and grep-checked.

### F9 [LOW] `sys.path.insert` is written one line after the import it exists to enable

`tools/memory-recall/test_recall_floor.py:73`

`import query` is at `:71`; `sys.path.insert(0, str(KIT))` is at `:73`. The insert is a no-op where it
stands — the import resolves only because CPython seeds `sys.path[0]` with the script's directory,
the exact accident the insert was written not to depend on. Reproduced:
`python -P tools/memory-recall/test_recall_floor.py` fails **15 of 16** arms with
`ModuleNotFoundError: No module named 'query'` (only the kit-payload arm survives, doing its own
insert at `:347`). Contrast `check-recall.py:57`, which inserts before its sibling imports.

- **Fix.** Hoist the insert to module scope beside the `KIT`/`CHECK`/`FIXTURE` constants, above the
  deferred import.
- **Left-shift gate.** A lint arm asserting the leg passes under `PYTHONSAFEPATH=1`; running the two
  python legs with `-P` in the canary would catch the whole class cheaply.

### F10 [LOW] `gate-legs.json` was rewritten wholesale, and now carries three non-ASCII bytes read without an encoding

`tools/gate-legs.json:307`

`git diff main...HEAD -- tools/gate-legs.json` is **639 added / 617 removed** for a change that adds
exactly two legs (63 → 65, none removed). The new file round-trips byte-exactly as
`json.dumps(data, indent=1, ensure_ascii=False)`, so it was regenerated; no in-repo tool writes it.
Two costs:

1. **Merge.** Every line differs from main, so any concurrent branch touching the manifest conflicts
   on the whole file. `.gitattributes:8` gives this path only `text eol=lf` — `merge=rows` is scoped
   to `memory/DECISIONS.md` and `memory/backlog/*.md`, so the four-node fleet has no row-keyed driver
   for this JSON.
2. **Encoding.** Main's blob carried **zero** bytes above 0x7F (the fan-out leg escaped `≤`); the new
   one carries exactly **three** (`\xe2\x89\xa4` at offsets 4979-4981). `run-gates.sh:96` and
   `run-gates.test.sh:18,39,53` all `open(...)` with no `encoding=` — while every other reader
   (`govkit.py:445`, `drift_signals.py:116`, `map_lib.py:284`) passes `encoding="utf-8"`, making
   these four the outliers. Those bytes mojibake under cp1252/cp932 and **raise** under
   cp936/cp949/cp950, which `run-gates.sh:114` converts to `cannot parse tools/gate-legs.json` +
   exit 2 before a single leg runs. Masked on this node only by `PYTHONUTF8=1`.

Tempering: on a cp1252 node the mojibake is self-consistent across the manifest read, the
`\x1e`-joined stdout and the timing-cache round-trip, so no verdict flips; the DBCS hard-fail is
hypothetical for the current registry. Hence low — but the fix is free, in a repo whose
`.gitattributes` documents paying for this class twice.

- **Fix.** Restore the previous formatting and re-add only the two leg objects (regenerate with
  `indent=2, ensure_ascii=True`). Independently add `encoding="utf-8"` to the four call sites.
- **Left-shift gate.** A canary predicate: `tools/gate-legs.json` is pure ASCII **and** every reader
  of it passes an explicit encoding. Cheap, and it pins the class permanently.

### F11 [LOW] `measure_run` returns a dead `anchors` key that makes F2's real gap look covered

`tools/memory-recall/check-recall.py:188`

`anchors` is loaded at `:161`, used locally at `:176`, and packed into the returned dict at `:188`.
No consumer anywhere reads `run["anchors"]` — every other key (`docs`, `per`, `h`, `R`, `ceiling`,
`cell_value`, `unresolved`) has a reader. Cosmetic, but it sits in the one dict that is the seam
between measurement and reporting, and it signals to the next reader that a downstream predicate
resolves ids through the anchor map — which is **exactly** the resolution `measure_overlap` at `:211`
does *not* do. The dead key makes F2 look already handled.

- **Fix.** Delete `"anchors": anchors,` from the returned dict. (Or, better, fix F2 by making it
  true.)
- **Left-shift gate.** Nothing bespoke — a dead-key check over the small number of hand-built
  result dicts would be over-engineering. F2's arms are the real coverage here.

---

## What I attacked and could not break

- **The independence claim.** Both arms pass, and I re-derived the per-id arm's rising floor by hand.
- **The pin's derivation.** `h=10, R=12 → 9/11 = 0.8182 → 0.81` reproduced under `--audit-fixture`.
- **The import-don't-extend decision.** Correct: `bench.py` always returns 0, its flag set is closed
  and `verbatim.json` byte-pins it. Importing `load`/`build_index`/`rank_with`/`score`/
  `expected_by_target`/`terms` is the only way to reuse the scorer without breaking that pin.
- **The security model.** Verified: no network call, no execution of anything from the corpus, reads
  tracked files only, writes only under `mkdtemp()`. F1 is a *lifetime* defect inside that model, not
  a breach of it.
- **Preconditions 1-3 as designed.** All three stop the run and all three have arms. The gaps are at
  their edges (F3's uncovered branch, F4's unvalidated elements), not in their intent.

## Report limits

- **One elevation.** F2 was filed twice at [medium]. I raised it to [high] on evidence found in this
  pass: the `hits` predicate that both earlier lenses hit as an incidental backstop is **opt-in**
  (`if row["declared_hit"] is not None`), so a fixture that omits the column gets a fully silent
  EXIT=0 with the overlap guard reading 0.000 on all twelve. Neither original row established that.
- **One narrowing.** F5's original filing quoted the failing-case as a general "reds when they
  disagree" contract. The safety direction (`pin <= headroom`) *is* enforced; only the tight direction
  is missing. Severity stays low for that reason.
- **F1 severity is a merge, not an average.** Two lenses filed it [medium] and one [high]; I took the
  high, because the measured accumulation (~2 GB on one node) and the unbounded per-push growth are
  facts neither medium filing had.
- **Precision 0.81 (17/21).** The four refuted rows are not restated here; the confirmed set is what
  the skeptic stage survived.
- **Not assessed.** I did not re-audit the codebase-map dossier, the four claimed `baseline.toml`
  keys, the 13 rotated backlog rows, or the generated map artifacts beyond confirming the bar is
  green at 65/65 — the map coverage leg is itself the instrument for those.

## Suggested landing order

1. **F2** — it disarms the unit's own headline guard, silently. Fix before landing.
2. **F1** — mechanical, and it grows on every push until fixed.
3. **F3, F4** — both turn a refusal into an exit-1 that reads as a floor regression on the bar.
4. **F5-F11** — records/hygiene, safe to batch.
