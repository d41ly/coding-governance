**Serves:** diff-review TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 TOOL-dTracedLattice-6 TOOL-dTracedLattice-7

# dTracedLattice — Tier-2 CLOSING DIFF review, round 1

*Node `d`, 2026-09-06. An adversarial pass over the whole landed diff of the seven-unit set: a primed
finder fan, a skeptic stage prompted to REFUTE each finding, one synthesis. Every claim any surviving
finding makes about the tree was re-checked against source in this worktree before it was written
down here, and where a claim was verified by RUNNING something the command and its output are quoted
inside the finding. The build's own recurring classes were run over the diff as the checklist
(`python tools/memory-tree/gotchas.py --for-diff 6ec402bd..HEAD`); the two that have already bitten
this build twice each — `fold-text-is-unreviewed-surface` and `one-value-field-records-a-mixed-outcome`
— got a dedicated pass and both returned a finding (F6 and F7 for the first, F3 and F6 for the second).*

**Range reviewed: `6ec402bd3eb7f9cb5ce6257b0f60348ae3e593fc...HEAD`** (HEAD = `32d8d880`, branch
`branch/unattended-dtracedlattice-2f8f2b`, 54 files, +4643/-198).

**Round: 1.**

## Verdict: BLOCKED

One BLOCKER: a shipped kit entrypoint, `gen_map.py --seed-affordances`, raises `AttributeError` on
every invocation because unit 1's field rename missed it, and `WIRE-INTO-PROJECT.md` prescribes that
exact command to adopters. Twelve findings in total (1 blocker, 1 high, 4 medium, 6 low). Nothing
here reverses a unit's design decision; every one of the twelve is a one-file, small-diff repair.

## Review shape

Raw 23 · confirmed 19 · refuted 4 · unverified 0 · precision 0.83.

The 19 confirmed findings carried four sets of co-reported duplicates (three lenses each reached
`gen_map.py:198`, the dark-layer roots scoping, the `rank_harness` denominator, and the dead
`files` accumulator). Adjudication merges those into **12 distinct defects**, F1–F12 below; each
names the raw ids it absorbs. That merge is mine, at synthesis, and is separate from the pipeline's
own duplicate count in the integrity line.

## Run integrity

- Lenses: **4/4 returned, 0 DIED.**
- Skeptic batches: **5/5 returned, 0 DIED.**
- 0 contradictory verdicts demoted to unverified · 0 spurious verdicts discarded · 0 duplicates
  removed by the pipeline.
- 0 findings left UNVERIFIED. Nothing in this report is outstanding for lack of a skeptic verdict.

The run is COMPLETE: no lens died, so the zero counts above are measurements rather than gaps, and
"no finding in area X" means the area was looked at.

## Findings

| # | Sev | Where | One line | Raw ids |
|---|---|---|---|---|
| F1 | **BLOCKER** | `tools/codebase-map/gen_map.py:198` | `--seed-affordances` reads the deleted `Candidate.file` and crashes on every run | 1, 10, 16 |
| F2 | **HIGH** | `tools/codebase-map/map_lib.py:844` | present-layer derivation is scoped to the symbol corpus's top-level dirs, so an unread layer elsewhere is reported as covered | 2, 9, 17 |
| F3 | MEDIUM | `tools/codebase-map/reuse_lookup.py:498` | with no scan, every declared dark layer is reported STALE and the user is told to delete a correct declaration | 6 |
| F4 | MEDIUM | `tools/memory-recall/README.md:24` | `bench.py` is now forked, but four carriers still call it verbatim upstream — the documented re-pull would revert unit 7 | 3 |
| F5 | MEDIUM | `tools/codebase-map/rank_harness.py:150` | the constant control divides by all scenarios while the measured rate divides by live ones | 8, 13, 20 |
| F6 | MEDIUM | `tools/codebase-map/check_gate_coverage.py:63` | "GATE_FILE unset" and "GATE_FILE names nothing" are one return value and one exit 0 | 12 |
| F7 | MEDIUM | `tools/codebase-map/map_diff.py:20` | the shipped `--help` still names the destination unit 3 moved away from | 18 |
| F8 | LOW | `tools/codebase-map/map_diff.py:261` | on the fail-open path the legacy note names the file the run just wrote to, and says to delete it | 11 |
| F9 | LOW | `tools/codebase-map/reuse_lookup.py:567` | a branch production cannot reach, graded by a fixture in a shape production never emits | 15 |
| F10 | LOW | `tools/codebase-map/replay-phrases.py:179` | the `files` accumulator is dead and cost the loop its early exit | 14, 21 |
| F11 | LOW | `tools/memory-recall/bench.py:192` | the comment's "both halves are needed" is false; the explicit sort key alone is sufficient | 22 |
| F12 | LOW | `memory/map/features/codebase-map.md:66` | the dossier calls the rescued copy byte-identical; the module header says it is not | 23 |

---

### F1 — BLOCKER · `tools/codebase-map/gen_map.py:198` · `--seed-affordances` is 100% dead

Unit 1 (S1) renamed `Candidate.file` to `files: tuple[str, ...]` (`tools/codebase-map/reuse_lookup.py:80`,
with the rename's rationale in the comment at `:76-79`). Every sibling consumer was updated —
`reuse_lookup._line` prints `", ".join(c.files)` at `:585`, `replay-phrases.py:182` iterates
`r.candidate.files` — and this one was missed. It is the `amendment-leaves-its-other-half-standing`
class, in the one consumer no arm executes.

Reproduced in this worktree at `32d8d880`:

```
$ python tools/codebase-map/gen_map.py --seed-affordances --top 3
# seed-affordances: top 3 undeclared seams (fan-in >= 3)
Traceback (most recent call last):
  ...
  File "tools/codebase-map/gen_map.py", line 198, in _seed_affordances
    f"- {cand.name}  [fan-in {fanin} | {cand.kind} | {cand.file}]  "
AttributeError: 'Candidate' object has no attribute 'file'. Did you mean: 'files'?
```

This is ENGINE, not project-owned, so it lands broken in every adopter on the next kit upgrade —
and `WIRE-INTO-PROJECT.md:346` prescribes exactly this command as the up-front step to converge an
adopter's active surface (`tools/codebase-map/README.md:35` and the usage block at `gen_map.py:10`
advertise it too).

Nothing catches it. `tools/codebase-map/selftest.py:857 test_seed_affordances` drives
`rl.seed_affordances(corpus, ref, ...)` directly and its own docstring concedes "the CLI is thin glue
over this" — so the printer at `:198` is executed by no arm. Confirmed by running the suite at HEAD:
`codebase-map selftest: 52 executed, 0 skipped (0 of 5 guarded)` → `PASS`, over a dead entrypoint.

**Fix.** One line: `f"- {cand.name}  [fan-in {fanin} | {cand.kind} | {', '.join(cand.files)}]  "`,
matching `reuse_lookup._line`.

**Left-shift gate.** Gate the CLASS, not this line: add a selftest arm that, inside the existing
fixture repo, invokes EVERY mode `gen_map.py` advertises (`--scaffold --write --check --seed-baseline
--seed-affordance-baseline --seed-affordances`) through `gen_map.main([...])` under
`contextlib.redirect_stdout`, and asserts each exits 0. That is one arm covering six entrypoints and
it fails on the next data-model rename too, which a fix to `test_seed_affordances` alone would not.

### F2 — HIGH · `tools/codebase-map/map_lib.py:844` · the dark-layer derivation cannot see outside the symbol corpus's roots

Unit 5 replaced an authored `RECALL_DARK_LAYERS` with a derivation, so that a present layer with no
extractor REFUSES before a shortlist renders. The derivation's population is too small.
`build_reference_index` sets `roots = sorted({f.split("/", 1)[0] for f in files if f})` from the
SYMBOL file list (`map_lib.py:826`), and the `present[suffix]` tally at `:843-844` sits INSIDE
`for top in roots`. A language layer living in any other top-level directory is therefore never
counted as present, and everything downstream reads that as "not there".

Reproduced against the real module in a scratch tree (symbols list `["src/text.py"]`, an unextracted
`web/text.ts` on disk, `RECALL_DARK_LAYERS=".ts"`):

```
roots ['src'] present {'.py': 1} covered ['.py']
verdict {'uncovered': [], 'undeclared': [], 'stale': ['.ts'], 'legacy': (), 'counts': {'.py': 1}}
refusal: ''
scan line: # scan coverage: 1 files scanned | 0 parse skips | unscanned layers: none — every present layer has an extractor
derive_dark: []
```

Three consequences, all wrong, all in the mechanism this unit added to stop exactly this:
`render_layer_refusal` returns `""` so the refusal at `reuse_lookup.py:781-784` never fires; the
`recall partial:` paragraph (`reuse_lookup.py:469-476`) is suppressed because `_derive_dark`
(`:552`) returns `[]`; and `_scan_line` (`:570`) prints the affirmative `unscanned layers: none —
every present layer has an extractor` over a layer nothing read. On top of that, the correct
declaration is reported STALE, so `main` (`:785-788`) tells the operator to DELETE the one thing
that was protecting them — a regression against the pre-unit behaviour, where the declaration alone
drove the notice.

On this repo it is masked, not absent. Probed at HEAD: `roots == ['tools']`,
`present_counts == {'.js': 8, '.py': 53, '.sh': 85}`, while `git ls-files '*.sh' | grep -v '^tools/'`
returns 9 tracked shell files (under `.githooks/`, `memory/builds/`, `skills/session-kickoff/`) the
walk never sees. It happens not to change the verdict here only because `.sh` also lives under
`tools/`. An adopter whose symbols come from `src/` and whose shell lives in `scripts/` gets the
false coverage claim on the first run. The declared-limitation note above `DEFINITION_CARRYING_EXTS`
(`map_lib.py:673-676`) names only the missing-`_LEX_PROFILES` case, so this gap is undocumented too.

**Fix.** Count `present` over the tracked file list (or a walk from `root` under the same
`skip_dirs`) instead of over `roots`, keeping the `exts` filter for the token scan itself — the
counting walk is cheap and has no reason to inherit the symbol corpus's shape. If widening is
deliberately out of scope, then `_scan_line` must stop making a repo-wide claim: it already holds
`scan['roots']`, so print `none under tools/ — layers outside the symbol corpus roots are not
examined`, add the restriction to the `WHAT IT CANNOT SEE` note, and suppress the `stale` note for
extensions outside those roots.

**Left-shift gate.** `selftest.py:2260-2272` only asserts declared ⊆ present, which cannot see this
direction. Add the opposite arm on a fixture repo shaped like the repro above — symbols under
`src/`, an undeclared unextracted layer under `web/` — asserting `render_layer_refusal` is non-empty.
That arm reds today and is the smallest thing that fails if the population ever narrows again.

### F3 — MEDIUM · `tools/codebase-map/reuse_lookup.py:498` · no scan makes every declaration "stale"

`main` leaves `scan = {}` whenever `corpus.symbol_files` is empty (`:773-775`) — the normal state for
an adopter that has not taken the SYMBOL tier, and the state the kit's own opt-out path produces
(`INVENTORY-DERIVATION.md:97-100` tells such an adopter to record the uncovered layer in
`RECALL_DARK_LAYERS`). `derive_layer_verdict` then reads `present = set(scan.get("present_extensions", ()))`
at `:498` — an empty set — and computes `stale = declared_exts - present` at `:510`, so everything
declared falls out as stale. Verified:

```
# scan coverage: not run (no symbol file list to scan)
dark: ['.sh']
stale: ['.sh'] -> main prints the DELETE-IT note on stderr
```

So one run says both things at once: stdout carries `recall partial: layers .sh have no symbol
extractor … check that layer by hand`, and stderr carries `RECALL_DARK_LAYERS declares .sh dark and
no file with that extension is in the corpus. The declaration is stale — delete it`. Two answers to
one question, which is the shape this unit exists to remove, and the harmful one is the actionable
one: delete the declaration, adopt the symbol tier later, and the now-undeclared layer makes
`reuse_lookup` REFUSE at `:783`.

`_derive_dark` has the exact guard `derive_layer_verdict` lacks — `if present is None: return
list(shortlist.recall_dark)` at `:549-551`. The two functions disagree because only one of them
distinguishes "no layer" from "no walk".

**Fix.** Give `derive_layer_verdict` the same guard: when `scan.get("present_extensions") is None`
the walk never ran, so return `stale`/`undeclared` empty. The `legacy` migration check can still
fire — it reads only the declaration.

**Left-shift gate.** Every arm below `SCAN_FIXTURE` (`selftest.py:2197`) drives it; none passes the
no-scan input. Add `assert derive_layer_verdict({}, (".sh",))["stale"] == []`, mirroring the
`_derive_dark` fallback arm that already exists.

### F4 — MEDIUM · `tools/memory-recall/README.md:24` · a forked file is still recorded as verbatim

Commit `32d8d880` gave `tools/memory-recall/bench.py` a real local delta — `df.update(sorted(set(...)))`
at `:195` and the explicit `(-count, term)` key at `:196` — and re-pinned `verbatim.json` in the same
commit. Four carriers still classify the file as unmodified upstream:

- `tools/memory-recall/README.md:24` — the file table row: `bench.py … **Verbatim** upstream`, beside
  `recall-opened.js` marked `**Forked**`.
- `tools/memory-recall/README.md:32` — `digests of the two verbatim files`.
- `tools/memory-recall/README.md:206-211` — Maintenance: `bench.py`, `union.py` … "re-pulled
  **wholesale** from upstream on any fix and never merged".
- `memory/map/features/memory-recall.md:47` — "**`bench.py` and `union.py` are byte-pinned**".

And the ratchet's own arm, `tools/memory-recall/selftest.py:1323`, is titled "byte-identical to the
upstream copies they were taken from", with a docstring reading "An edit here means somebody forked
them without saying so" — now false of the very file it pins. `bench.py` also carries no fork header,
unlike the three files `README.md:212-214` says each carry one.

Following the documented rule reverts unit 7, and the rule's own re-pin step makes the regression
green: the `rm3` `RECALL_FLOOR` verdict starts moving on an unchanged tree again with a passing
verbatim arm. The ratchet built to detect an undeclared fork was silenced by the fork it should have
flagged.

**Fix.** Move `bench.py` to the Forked category in all four carriers and name the delta once:
"`run_rm3` term selection made hash-seed-independent (`TOOL-dTracedLattice-7`); a re-pull is a merge,
not a wholesale replace". Add the fork header to `bench.py` that the other forked files carry, and
retitle the selftest arm so its claim matches what the pin now means (a pin against the recorded
digest, not against upstream).

**Left-shift gate.** Make the classification machine-checked rather than remembered: in
`selftest.py`, derive the Verbatim/Forked sets from the README table and assert that every file in
the Verbatim set carries no fork header AND every file in `verbatim.json` is classified by exactly
one of the two lists. A file that grows a header, or a row that says Verbatim over a file the digest
was re-pinned for, then reds instead of drifting.

### F5 — MEDIUM · `tools/codebase-map/rank_harness.py:150` · the control and the measurement use different denominators

`measure_recall` divides by `len(scored)` — live scenarios only (`:105`) — and `run_shuffle_control`
does the same (`:124`). `run_constant_control` is handed the raw `rows` at `:176` and returns
`hits / len(rows)` at `:150`. `render_report` prints the two on one line and derives the verdict
`beats it` / `DOES NOT beat it` from `real > c` (`:177-180`), i.e. from two populations.

This contradicts the module's own stated law at `:19-22`: dead probes "are reported separately and
excluded from the rates". The error direction favours the tool — dead probes inflate only the
control's denominator, deflating the control and making the measured ranking likelier to "beat" it.
The numerator is affected too: `git log --name-only` lists DELETED paths, so a scenario whose
`expected_file` no longer exists (counted into `dead` at `:86-89`, excluded from `scored`) can still
match the churn top-K and score a control hit while being unscorable on the measured side.

Latent today — `scen-adversarial.json` reports `dead probes 0` — but this file is tracked precisely
so later readers can re-run it after the tree has moved, which is exactly when probes go dead, and
its numbers are what decide whether a ranking change lands.

**Fix.** Score the control over the live set: build `live_ids = {s["id"] for s in scored}` in
`render_report`, filter `rows` by it before the call, and keep `hits / len(live_rows)`. Refuse with
`nan` when that set is empty, as the report path already does elsewhere.

**Left-shift gate.** A selftest arm over a two-scenario fixture where one target is absent from the
fixture tree, asserting that the constant control and `measure_recall` report over the same
denominator (equivalently: that a dead probe changes neither rate's divisor).

### F6 — MEDIUM · `tools/codebase-map/check_gate_coverage.py:63` · one return value for a benign state and a broken configuration

`resolve_gate_path` returns `None` both when `GATE_FILE` is empty and when it names a file that does
not exist (`:59-63`), and `main` prints one skip line for both and returns 0 (`:83-88`). The message
itself admits the conflation — "GATE_FILE is unset in .codebase-map.conf or names no existing file" —
and still exits 0. That is `one-value-field-records-a-mixed-outcome`, in the program whose docstrings
condemn precisely this ("a check's silence reads as coverage", `:20`).

The population it matters for is the one the check exists for. `kit.toml:100-106` declares
`[[hole]] frozen-gate-vs-moving-engine` with `discharge = ["python", "{kit}/check_gate_coverage.py"]`,
and `tools/gate-legs.json:573-584` carries it as the `codebase-map gate coverage` leg (subject
`repo`, guard `tools/codebase-map/`, on the bar). An adopter renames or relocates the gate into their
own test dir — which the adoption instruction invites — forgets the conf key, and from then on the
declared hole's only compensating control prints `gate-coverage: skipped` and exits 0 forever while
the engine keeps adding artifacts nothing compares.

The file's own liveness precedent sets the standard it violates: an empty engine-side match REFUSES
with exit 2 at `:77-81`. A `GATE_FILE` naming nothing is the same "probe cannot move" shape.

**Fix.** Split the states in `resolve_gate_path` — return `None` only for an empty value, and the
non-existent `Path` when one is set — then in `main` keep exit 0 for unset, and exit 2 for set-but-
missing: "GATE_FILE names `<path>`, which does not exist — the gate this check grades is not
installed where the conf says."

**Left-shift gate.** Add a fixture row to the existing `_run_gate_coverage` harness with
`GATE_FILE=tests/moved_gate.py` and no such file, asserting a non-zero exit and that the message
names the missing path. One row, and it is the arm that would have caught this.

### F7 — MEDIUM · `tools/codebase-map/map_diff.py:20` · the shipped `--help` still names the old destination

Unit 3 moved the reinvention backlog to `<git-common-dir>/codebase-map/reinvention-backlog.md`
(`derive_backlog_path`, `:142-172`), leaving the `<MAP_ROOT>/` spelling reachable only on the
git-unavailable fail-open branches at `:167` and `:169`. The module docstring at `:20` still reads
"routed as a review WARN to `<MAP_ROOT>/reinvention-backlog.md`", and `main` passes `__doc__` as the
`ArgumentParser` description (`:286`) — so that IS the shipped `--help` text.
`WIRE-INTO-PROJECT.md:344` carries the same stale spelling, inside the §3c block this very diff
edited two lines earlier. `tools/codebase-map/README.md:39` was updated, with a whole new paragraph
explaining the move.

An operator looking for the appended rows is sent to a path that will not have them — in the unit
that exists because nobody could find those rows. `fold-text-is-unreviewed-surface`: the prose 140
lines above the changed function was not read when the function changed.

**Fix.** Update `map_diff.py:20` to `<git-common-dir>/codebase-map/reinvention-backlog.md` (noting
the map-root fail-open), and make the same edit at `WIRE-INTO-PROJECT.md:344`.

**Left-shift gate.** A one-line grep leg (or an assertion in the existing kit selftest): the literal
`MAP_ROOT>/reinvention-backlog.md` must appear in NO tracked file except `derive_backlog_path`'s own
fail-open branch. It reds today, it is two lines of Python, and it covers the class — any future
carrier that restates the destination.

### F8 — LOW · `tools/codebase-map/map_diff.py:261` · the legacy note can name the file the run just wrote

`derive_backlog_path` fails open to `m.map_root(root) / "reinvention-backlog.md"` (`:167`, `:169`)
when `git rev-parse --git-common-dir` cannot answer, and `_converge` builds
`legacy = map_dir / "reinvention-backlog.md"` with `map_dir = m.map_root(root)` (`:192`, `:241`) —
byte-identical paths on that branch. The run appends rows there (`:232-239`), then
`render_legacy_note` is called unconditionally at `:261`, sees `legacy.is_file()`, and prints
"`memory/map/reinvention-backlog.md` is a LEGACY location and is NO LONGER WRITTEN … Fold or delete
it by hand; new rows go to `<the same file>`". A reader who follows that deletes the live record the
unit exists to preserve.

Reachability is real but narrow, which is why this is filed LOW rather than with the mediums:
root resolution is pure path math (`map_lib.py:83-119`, explicitly not `git rev-parse`),
`_changed_files` and `_symbols_at_ref` both fail SOFT on git failure, and `_read_symbols` falls back
to the committed artifact — so a non-git checkout (export, copied adopter tree, git off PATH) runs
the whole `--converge` and takes the fail-open branch. But that is an unusual place to run it.

**Fix.** One condition, best placed inside the function so it covers future callers:
`if not legacy.is_file() or legacy == current: return ""`.

**Left-shift gate.** `test_legacy_backlog_is_named_and_never_deleted` (`selftest.py:2096`) hands the
function two distinct paths. Add a row passing the SAME path twice and asserting `""`.

### F9 — LOW · `tools/codebase-map/reuse_lookup.py:567` · a dead branch, graded by a synthetic fixture

`build_reference_index` writes `files_scanned`, `parse_skips`, `extensions`, `present_extensions`,
`present_counts` and `roots` in one block (`map_lib.py:857-863`), and it is the only production
filler of a scan dict (`reuse_lookup.py:774`, `rank_harness.py:81`); every other production path
passes `{}`, which `_scan_line` catches at `:559`. So once `:559` has passed, the
`present_extensions is None` test at `:567` can never be true: the declaration-fallback string at
`:568` is unreachable, and `uncovered` (`:566`) is computed and unused on that branch.

The only caller that reaches it is `test_scan_coverage_line_cannot_go_quiet` (`selftest.py:1908-1922`),
whose fixture `{"files_scanned": 41, "parse_skips": 2, "extensions": [".py"], "roots": ["tools"]}`
omits `present_extensions` — a shape production never emits — and then asserts
`"unscanned layers: sh, ps1"`, the pre-migration language-name spelling `derive_layer_verdict` and
`render_layer_refusal` now REFUSE. An arm named "cannot go quiet" is grading the fallback instead of
the line production renders: `staged-break-substitutes-a-synthetic-value`, one level up.

(The sibling fallback in `_derive_dark` at `:549-551` IS reachable, through render's unguarded call
on an empty corpus — that one is not this finding.)

**Fix.** Delete `:567-568` and let the line read
`dark = ", ".join(uncovered) if uncovered else "none — every present layer has an extractor"`
unconditionally; give the selftest fixture `present_extensions`/`present_counts` so it grades the
rendered line. Note this interacts with F2: whichever wording F2 lands, the fixture asserts it.

**Left-shift gate.** Rather than a new gate, make the existing one honest: build the arm's scan dict
by CALLING `m.build_reference_index` over the fixture tree instead of hand-writing it. A fixture
assembled by the producer cannot drift into a shape the producer never emits.

### F10 — LOW · `tools/codebase-map/replay-phrases.py:179` · dead accumulator, and the loop lost its early exit

`files` is declared at `:179`, appended at `:184-186`, and read nowhere: `rank` comes from
`enumerate(sl.ranked, 1)` at `:181-183`, and the returned dict (`:187-195`) carries
`phrase/truth/n_ranked/rank/hit/hit5/hit10` and no such key. The other `files` hits in the module
(`r.candidate.files` at `:182`, `corpus_files` at `:233`) are unrelated expressions.

With the accumulator still there the loop also walks the entire shortlist after `rank` is fixed,
doing an `f not in files` linear membership test per candidate per graded phrase — in the one
instrument that enforces its own wall-clock ceiling, and whose numbers the AC5/AC10 ledger entries
quote. Not a correctness bug; it is leftover plumbing from the ranking basis the unit replaced.

**Fix.** Delete `:179` and `:184-186`, and short-circuit:
`rank = next((i for i, r in enumerate(sl.ranked, 1) if any(check_path_match(f, t) for f in r.candidate.files for t in truth)), None)`.

**Left-shift gate.** None proposed, deliberately. This is a deletion, and standing up an unused-local
linter for one dead list in a measurement script costs more than it saves — say so in the fix commit
rather than adding a leg.

### F11 — LOW · `tools/memory-recall/bench.py:192` · the comment states a false rationale for half the fix

The comment at `:186-192` says the two halves of the determinism fix are both required and "either
alone leaves the other free". Traced the whole consumer chain: `df` is a `Counter` read only at
`:196` via `sorted(df.items(), key=lambda kv: (-kv[1], kv[0]))`. Counter keys are unique, so that key
is a TOTAL order and insertion order cannot reach `ranked`, `extra`, or the final query; counts are
order-independent too, since each doc contributes a deduped set of a fixed 400-term slice. The
`sorted()` inside `df.update` at `:195` is therefore redundant while the explicit key stands.

It is a comment, but it is a comment in a file `verbatim.json` pins and that F4's records say is
re-pulled wholesale — so the next person merging an upstream fix preserves the wrong half on the
strength of it.

**Fix.** Restate it: the deterministic total order is `(-count, term)`; the `sorted()` in `update` is
belt-and-braces against a future reader reintroducing `most_common`. Or drop the `sorted()` and keep
one stated mechanism.

**Left-shift gate.** The gate already exists and is correct —
`tools/memory-recall/test_recall_floor.py:484-509` runs the probe under several `PYTHONHASHSEED`
values and compares rankings. Nothing to add; only the comment is wrong.

### F12 — LOW · `memory/map/features/codebase-map.md:66` · the dossier calls the rescued copy byte-identical

The dossier says "a byte-identical copy still lives in the lexicon kit and a selftest arm compares
the two on every run". It is not byte-identical: `tools/codebase-map/map_imports.py:33` spells the
helper `derive_ext` where `tools/lexicon/lexicon.py:203` spells it `ext_of`, with the rename live at
four call sites. The module's own header states the exception explicitly (`map_imports.py:22-28`) and
says a provenance claim nobody can check is worth nothing. The second half of the sentence is loose
too: `test_map_imports_matches_the_kit_it_was_rescued_from` compares the module index and a candidate
set — behaviour, never bytes.

Two records answering one question differently, with the dossier as the copy a reader reaches first
(it is where the map's coverage gate points them).

**Fix.** Amend to "a copy identical except for one forced rename (`ext_of` → `derive_ext`, per the
naming gate), compared BEHAVIOURALLY by a selftest arm on every run" — or point at the module header
instead of restating it, which is the lazier and more durable option.

**Left-shift gate.** None as a new leg. The durable repair is the pointer: a dossier sentence that
cites the header cannot disagree with it, which is cheaper than any gate comparing prose to prose.

---

## What was checked and found clean

These are measurements, not silence — all four lenses returned, so a zero here means the area was
read.

- **Unit 2's twins.** `tools/codebase-map/test_codebase_map.py` and `test_codebase_map.template.py`
  are identical modulo the module-name token (verified by diffing the two with the name normalised;
  empty diff). The `amendment-leaves-its-other-half-standing` risk the build flagged for this unit
  did not materialise — both carry every edit.
- **Unit 6's copy-then-delete.** Nothing under `tools/lexicon/` is touched by this diff, and
  `map_imports.py` imports no sibling kit (asserted by its own arm at `selftest.py:1810`). The one
  deviation from byte-identity is declared in the module header; only the dossier's restatement of it
  is wrong (F12).
- **Unit 4's wiring.** The `codebase-map gate coverage` leg is declared in all three carriers —
  `tools/codebase-map/kit.toml:108-112`, `tools/gate-legs.json:573-584`,
  `tools/govkit/subject-pins.tsv:26` — with the `[[hole]]` discharge naming the same program. The
  wiring is complete; the defect is in the program's exit contract (F6).
- **The kit suite at HEAD.** `python tools/codebase-map/selftest.py` → `52 executed, 0 skipped
  (0 of 5 guarded)`, `PASS`. Quoted here as evidence for F1 and F9 rather than as reassurance: it is
  green over a dead entrypoint and over a fixture in a shape production never emits.

## Scope and limits of this review

- Findings are anchored to this worktree at `32d8d880`. Every `file:line` was re-opened in the tree
  before being written down; the four that were reproduced by RUNNING code carry their output above.
- Not covered: the acceptance ledgers' arithmetic was read for consistency with the specs but the
  measurement runs behind them (`meas-*.md`, `scen-adversarial.json` scoring) were not re-executed —
  F5 is a defect in the instrument, not a claim that any recorded figure is wrong.
- Not covered: the memory-tree, hygiene and manifest legs of the bar. This is a diff review, not a
  gate run.
