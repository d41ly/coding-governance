# TOOL-aMendedFleet-56 — gateable stable-key drift signals are bounded by a shrink-only set of offender ids instead of a count

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 56 · advances TOOL-aNumeralWarden-3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-56-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-56-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`drift_report.py --check` reds a gateable signal when `value > pin`, so a pin bounds a COUNT and not
the offenders it counts: when one pinned offender drains and a new one arrives in the same range, the
value is unchanged and the gate stays green over a regression. Two gateable signals carry a pin
above 0 today, `non_terminal_specs_cited_by_product_source` at 2 and
`closed_specs_with_no_product_commit` at 1, and every row of both names its offender by spec id.
This unit replaces those two pins with a declared, shrink-only set of offender ids per signal: a new
id reds, a listed id that no longer offends reds until its line is deleted, and a set that gains a
member against the base reds, so the bound is on identities and the raise-or-drain ambiguity
`TOOL-aNumeralWarden-3` records cannot occur for these signals.

## 2. Scope (IN)

- **S1** — THE DECLARATION. The project layer gains `BASELINES`, a dict from signal name to a list
  of offender ids, read with `getattr` and an empty default so an older adopter's layer keeps
  importing. This repo's `tools/drift-audit/drift_signals.py` seeds it for
  `non_terminal_specs_cited_by_product_source` and `closed_specs_with_no_product_commit` with exactly
  the ids those records list at the BASE that still offend at the build commit; an offender that
  arrived on this branch after the base is not seeded, because seeding it is the top-up S6 refuses
  and S6's seed rule would red it against the base pin anyway. It reds as `new` instead, naming its
  id. The two `PINS` entries and the one `RATCHETS`
  row naming the first are deleted in the same commit. The measured-residual comments beside the old
  pins move above the new entries. `tools/drift-audit/drift_signals.template.py` declares an empty
  `BASELINES` with a comment saying when to use it. Observed by AC1, AC6.
  **Readers:** by name: `tools/drift-audit/drift_signals.py` spells both keys in `PINS` and the first
  in `RATCHETS`; `tools/drift-audit/drift_report.py` reads `ctx.pins` by signal name in `main`.
  by value: `main` compares each record's `value` against the pin it reads, and `ratchet_findings`
  compares the `RATCHETS` row's scalar at base and HEAD; S3 replaces the first comparison for a
  baselined signal, and the second has no scalar left to read.
- **S2** — IDENTITY. A detail row's identity is its `id` field when that is a string, and otherwise
  the unlocated key `extract_unlocated` builds for the row, the module-level helper
  `TOOL-aMendedFleet-48` hoists out of `render_drift_offenders`, so a row with no id is never
  silently matched and the unlocating step keeps one spelling. A new helper `derive_row_identity` in
  `tools/drift-audit/drift_report.py` is the one spelling of that rule. Observed by AC2.
- **S3** — THE VERDICT. For a signal named in `BASELINES`, `main` sets three fields on its record:
  `baseline`, the declared list's size, which also becomes its `pin` for display; `new`, the sorted
  identities of its rows that the list does not carry; and `stale`, the sorted listed ids no row
  carries. The record joins the over-population `--check` reds on when it is `live` and `new` or
  `stale` is non-empty, whatever its `value`. The human table prints `ok (baseline <n>)` or
  `OVER BASELINE — gateable`, and `--check` prints each new and stale id on stderr with its remedy.
  Observed by AC1, AC2, AC3.
- **S4** — ONE BOUND PER SIGNAL. A signal named in both `PINS` and `BASELINES`, or a `BASELINES` key
  naming no gateable record, is refused before any table line, JSON or offender key is printed:
  exit 2 and one line naming the signal and the declarations, on the stderr channel `main` already
  uses for a bad project-layer value. The first conflict is caught before the signals run, the
  second once their records exist and before `TOOL-aMendedFleet-48`'s `--check` history write, so a
  refused run appends no reading. Observed by AC5.
- **S5** — OFFENDER KEYS. `--offenders` emits, for a baselined signal, the existing key shape for each
  NEW row and a `{"stale": "<id>"}` key for each stale id, and never a key for a row the list
  carries, so the merge bar's red attribution compares only what moved. Observed by AC2, AC3.
- **S6** — THE SHRINK-ONLY GUARD. A new `build_baseline_findings` beside `build_lang_mode_findings`
  reads the project layer at `git.base_ref` with `git show`, parses it with `ast`, and evaluates the
  module-level `BASELINES` and `PINS` assignments with `ast.literal_eval`. For each signal in the
  working `BASELINES`: where the base lists the signal, each id the base did not carry is a finding;
  where the base does not, a seed larger than the base's `PINS` value for that signal, 0 when absent,
  is a finding. A project layer absent at the base is no comparison, as in `ratchet_findings`. The
  findings join the `ratchets` population, so `--check` and `--offenders` red on them through the
  path every other ratchet takes. Observed by AC4.
- **S7** — DOCS. The drift-audit README's disposition table and its pins section say when a gateable
  signal takes an id set rather than a count, its layout table lists `BASELINES` among the
  project-layer names, and its install steps say to seed `BASELINES` with the measured ids where a
  gateable signal's rows carry one. Observed by AC6.
- **S8** — Self-test arms in `tools/drift-audit/selftest.py`, over the fixture repository the signal
  2 arms already build: an equal-count swap reds; a drained listed id reds as stale; a baseline that
  gains an id against a committed base reds as a ratchet; a seed above the base pin reds; a signal
  in both declarations exits 2. NOT OBSERVED by a criterion here: the suite runs once at the close,
  and the arms are declared under `New arm:` in §7.
- **S9** — `memory/map/generated/symbols.json` is regenerated for the new definitions. NOT OBSERVED
  by a criterion here: `python tools/codebase-map/gen_map.py --check` at the close is its check, and
  §7 names the legs that read it.
- **S10** — THE LAYER IS NOT EVIDENCE. Signal 2 greps `EVIDENCE_GLOBS` for each id, and the project
  layer sits inside them in this repo, so a `BASELINES` list spelling an id would itself cite it: the
  listed id could never drain, and S3's stale half could never fire. The old `PINS` comment recorded
  the same self-citation and answered it by not spelling the ids. `Ctx` derives the layer's
  repo-relative path once, as `layer_path`, and `signal_spec_status` excludes it from its citation
  grep, so a declaration about the signal is never evidence for it. Observed by AC3.

## 3. Non-goals (OUT)

- Report-only signals. `source_cited_ids_resolving_to_no_record` also names its rows by id, but it
  never gates, so a set would change nothing `--check` does; its `RATCHETS` row holds its pin.
- Gateable signals with a pin of 0. An empty set and a pin of 0 bound the same thing, so the
  declaration stays the shorter one; unit 47 lowers `lexicon_verbs_declared_but_unused` to 0.
- A freeze-sha provenance assert, the precedent's assert C. §8 F1 records why.
- An escape that lets a set gain an id. §8 F3 records why.
- The lexicon's own offender pins, which `TOOL-dScaffoldedMirror-9` owns.
- The drift-audit kit version bump, owed once at the close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-48` — `extract_unlocated`, the hoisted unlocating step S2
  falls back to, and the `--check` history write S4 refuses ahead of.
- **hands-off** external — identity sets for report-only signals, should one ever become gateable.
- **hands-off** external — the drift-audit kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at worktree HEAD `725b1449`, whose `tools/` bytes equal base `7af5f564`'s.

- `python tools/drift-audit/drift_report.py --json` lists six gateable signals. Two carry a pin above
  0: `non_terminal_specs_cited_by_product_source` at value 2 of 82, rows `TOOL-aBatchedLintel-1` and
  `TOOL-dNarrowedAnchor-1`, and `closed_specs_with_no_product_commit` at 1 of 767, row
  `TOOL-aMooredAnchor-1`. `lexicon_verbs_declared_but_unused` reads 0 against a pin of 3. PINNED,
  measured 2026-10-04.
- A row of the first signal carries `cited_in`, up to three citing paths, so its full JSON key moves
  when a citation moves while its offender does not. That is why S2 prefers `id`.
- `TOOL-aBatchedLintel-1` is cited from product source only by `tools/memory-tree/check-memory-hygiene.sh`;
  its other citations are test files `EVIDENCE_GLOBS` excludes. AC2 and AC3 drain it there.
- `ratchet_findings` and `build_lang_mode_findings` both read their declaration at `git.base_ref`
  with `git show`, and the second is the kit's existing set-shaped guard placed beside `RATCHETS`
  rather than inside it.

### Data model

```
BASELINES: dict[str, list[str]] = {
    "non_terminal_specs_cited_by_product_source": [<the ids its record lists>],
    "closed_specs_with_no_product_commit": [<the ids its record lists>],
}
```

A baselined record gains `baseline` (an integer), `new` and `stale` (sorted lists of identities).

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `BASELINES` | project-layer attribute | none; attributes are not graded |
| `derive_row_identity` | function: a detail row in, an identity string out | `py.function`, verb `derive` |
| `build_baseline_findings` | function: git, the layer's path and the working `BASELINES` in, findings out | `py.function`, verb `build` |

Both function names were answered OK by `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.

### Migration

The commit that seeds `BASELINES` is the migration. Its base still carries the two pins, so S6's
seed rule compares each seed's size against them: a seed of the measured ids passes, and a seed that
smuggles one more id reds against the old pin.

### Rollout

An adopter whose layer declares no `BASELINES` keeps today's behaviour byte for byte. Units 47, 51
and 52 edit `PINS` and are ordered before this unit; dispatch is sequential.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/drift_signals.py`
- `tools/drift-audit/drift_signals.template.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **A provenance assert at a freeze sha**, assert C of `TOOL-dScaffoldedMirror-9`'s research. Tested
  by reading the two signals' sources: `signal_spec_status` globs `ctx.root` and runs `git grep`
  without a revision, and `signal_closed_specs_untraceable` globs the same spec files and reads its
  waiver registry from `ctx.root`, so neither can be evaluated at a past sha without a checkout of
  it. §8 F1.
- **A separate TOML file in `baseline.toml`'s shape.** A new kit file owes a descriptor role and a
  second parser, while the project layer already holds `PINS`, the thing this replaces, and
  `ast.literal_eval` reads it at the base with the standard library.
- **The full offender key as identity, as the source synthesis proposes.** It changes when a
  citation moves, so the same offender would read as new and its old key as stale.
- **Counting `new` and `stale` into `value`.** `value` is what the history rows unit 48 writes and
  the card reads; it keeps meaning "offenders now".

## 5. Production-readiness checklist

- security — N/A: reads the project layer at the base with `ast.literal_eval`, which evaluates
  literals only and executes nothing.
- perf / scale — one `git show` per run under `--check` or `--offenders`; set operations over a few ids.
- error / empty / loading states — a layer absent at the base is no comparison; a base layer that
  does not parse is a finding naming the parse error, never a pass; a dead baselined signal is
  reported dead exactly as today.
- observability — stderr names each new and stale id with its remedy; the table prints the baseline
  size.
- risks — closing a listed spec reds `drift-audit records` until its id is deleted from the set; the
  message names the line. A `--no-verify` push can land an addition no later run sees; §8 F1.
- testing — AC1 to AC6 here; the arms in S8.
- migration — §4 Migration; the seed commit is checked against the pins it deletes.
- user docs — S7.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py --json` runs on this repo, the
  `non_terminal_specs_cited_by_product_source` and `closed_specs_with_no_product_commit` records each
  carry a `baseline` equal to the size of its `BASELINES` list, an empty `stale` list, and a `new`
  list holding only offenders that arrived after the base measurement, and
  `python tools/drift-audit/drift_report.py --offenders` prints no line naming a listed id.
  Red when: a record lacks the fields, or a listed offender is still reported as an offender.
  figure: DERIVED at observation time; baselines 2 and 1 at writing, and on the build commit the
  first record's `new` holds the two ids earlier units of this build brought in (S1).
- **AC2** — When every occurrence of `TOOL-aBatchedLintel-1` is deleted from
  `tools/memory-tree/check-memory-hygiene.sh` and a comment naming one SPECCED spec id the record
  does not list is appended to `tools/drift-audit/drift_report.py`, both in the working tree, and
  `python tools/drift-audit/drift_report.py --check` runs, the first record's `value` is the value
  AC1 read, the run exits 1, and `--offenders` prints, among its lines for that signal, one naming
  the new id and one naming `TOOL-aBatchedLintel-1` as stale; reverting both edits restores AC1.
  Red when: a drain and a new offender at an equal count pass, which is the defect this unit closes.
  fixture: `TOOL-aBatchedLintel-1` is listed and cited from that file today.
- **AC3** — When only the deletion of AC2 is made and `python tools/drift-audit/drift_report.py --check`
  runs, it exits 1 and stderr names `TOOL-aBatchedLintel-1` as stale; when its id is also deleted
  from `BASELINES` in `tools/drift-audit/drift_signals.py`, `--offenders` prints no line naming
  it, though the layer now spells it in that run's other edits: S10 keeps the layer out of the
  evidence.
  Red when: a listed id that no longer offends passes, leaving a latent waiver for its return.
- **AC4** — When an id is appended to the `non_terminal_specs_cited_by_product_source` list of
  `BASELINES` in `tools/drift-audit/drift_signals.py` in the working tree and
  `python tools/drift-audit/drift_report.py --check` runs, it exits 1 and stderr carries a
  `RATCHET WEAKENED` line naming `BASELINES` and that signal, and `--offenders` prints a `ratchet`
  line; reverting restores AC1.
  Red when: the set grows against its base with no red. This is the staged break for S6.
  fixture: before this unit lands the base carries the pin, so the seed rule fires; after, the
  gained-id rule does. Both name the signal.
- **AC5** — When the `closed_specs_with_no_product_commit` entry is restored to `PINS` in
  `tools/drift-audit/drift_signals.py` in the working tree, and separately when
  `source_cited_ids_resolving_to_no_record` is added to `BASELINES`, each run of
  `python tools/drift-audit/drift_report.py` exits 2 with one line naming the signal and the
  conflicting declarations, and prints no table line.
  Red when: a signal carries two bounds, or a report-only one carries an id set, and the report runs.
- **AC6** — When `grep -c "BASELINES" tools/drift-audit/README.md tools/drift-audit/drift_signals.template.py`
  runs each file reports at least 1, and
  `grep -c "closed_specs_with_no_product_commit\": 1" tools/drift-audit/drift_signals.py` reports 0.
  Red when: a carrier omits the declaration, or the old pin survives beside the set.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `drift-audit wiring` · `encoding posture (text IO names its encoding)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/drift-audit/selftest.py` · a fixture with a baselined signal: an equal-count swap, a drained listed id, a set gaining an id against a committed base, a seed above the base pin, a signal in both declarations · `CHECK_FLOOR` moves by the checks the arm adds

## 8. Open questions

- **F1** — What stops the set from being topped up: a comparison against the base, or a provenance
  assert that every listed id was an offender at a frozen sha?
  The freeze assert is stronger: no edit to the present tree can change a past commit. It needs each
  signal evaluated against a historical tree, and both signals read the working tree, so the report
  would have to materialise a checkout it does not write today, which widens its write surface past
  what this tier priced. The base comparison is what every other shrink-only number in this kit uses,
  with the remote-first base `resolve_base_ref` resolves. Its residual, said plainly: an addition
  landed by a `--no-verify` push is invisible afterwards, because the base then carries it; every
  `RATCHETS` row in this kit has the same residual today.
  RESOLVED (agent, 2026-10-04, delegated): the base comparison, per S6; the freeze option is vetoed
  under M3's third veto.
- **F2** — Does a listed id that no longer offends red, or only report?
  Reporting leaves the id in the set, where it waives that offender's return without a red. The
  charter's §5 ratchet fails on a claim naming a dead key, and the precedent's assert B does the same.
  RESOLVED (agent, 2026-10-04, delegated): it reds, per S3, with the remedy named.
- **F3** — Is there an escape for a deliberate addition?
  Each signal already has a remedy that is not an addition: a status change for the first, the trace
  waiver for the second. Unit 40 ruled the same for the map's baseline.
  RESOLVED (agent, 2026-10-04, delegated): no escape.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#52] and the
  `TOOL-dScaffoldedMirror-9` precedent, with the gateable pins measured at base.
- rev-2 · 2026-10-04 · S2 · S4 · S9 · §3 · §4 · §7 · §10 · M2 cross-read: S2 fell back to the unlocating
  step nested in `render_drift_offenders`, which `TOOL-aMendedFleet-48` S4 hoists to
  `extract_unlocated` so the key keeps one spelling, and S4 did not say whether a refused run reaches
  that unit's history write; both now name it, with a consumes-from edge. The new definitions owe
  `symbols.json`, which units 57, 59 and 90 regenerate for theirs and this spec omitted.
- rev-3 · 2026-10-05 · S1 · S10 · AC1 · AC2 · AC3 · §4 Inventory · build pass: re-measured at the
  build commit, signal 2 read 4 against its pin of 2, the two extras brought in by earlier units of
  this build (a forward citation of unit 65 and the spec high-water registry unit 25 wrote), so S1
  now seeds only what the base measured and AC1 to AC3 name ids rather than equate counts. Spelling
  the ids in the layer made the layer cite them and no listed id could ever go stale, the
  self-citation the old pin comment recorded; S10 excludes the layer from signal 2's evidence.
  `build_baseline_findings` takes the working `BASELINES` from the imported layer rather than
  re-parsing the working file, so the two sides of `main` read one value.

## 10. Reuse audit

The seams extended are all in `tools/drift-audit/drift_report.py` and its project layer:
`build_lang_mode_findings`, the kit's set-shaped guard read at `git.base_ref` beside `RATCHETS`,
which S6 copies in shape; `ratchet_findings`' rule that a file absent at the base is no comparison;
`render_drift_offenders`' unlocated row key, hoisted by unit 48 as `extract_unlocated`, which S2
falls back to; and the `PINS` declaration this
replaces. `python tools/codebase-map/reuse_lookup.py "compare a shrink-only set of offender
identities against the base ref"` returned `affordance_offenders` in the map kit and
`resolve_pattern_sets` in the lexicon kit, each another kit's and neither a set-at-base guard, and
prose seams naming `check-testsuite-counts.sh` and `registry.toml`; no existing seam fits better
than the drift kit's own pair above. The scan names `.sh` as unscanned; no shell file is involved.
Recall returned `TOOL-dScaffoldedMirror-9` and its research record: its asserts A and B are S3, its
assert C is rejected in §8 F1, its assert D has no waiver list here to intersect, and its assert E is
the signal's own `live`. It also returned `TOOL-aSiftedPlaybook-1`, where the map's shrink-only
baseline was reversed in place because nothing enforced it, which is why S6 exists. Where the report
and the tree disagree: the synthesis proposes `render_drift_offenders`' keys as identities, and §4
shows why the `id` field is preferred.

Recall terms used: `python tools/memory-recall/query.py "why are drift pins counts rather than
offender identities and what replaces them" --terms "PINS RATCHETS identity baseline offender keys
render_drift_offenders shrink-only pin raise drain grandfather set FREEZE_SHA baseline.toml"`
