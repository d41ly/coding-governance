# TOOL-aMendedFleet-21 — a cutoff budget: armed `*_CUTOFF` keys are a pinned drift signal, so a new one must displace an old one

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 21

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Every dated cutoff key makes the required shape of a spec, a ledger or a run record depend on a
filename date, and nothing prices adding one: the report counted 22 in `.memory-tree.conf`, added in
under three months, and this tree's `.unattended.conf` arms seven more. Several of those keys also
carry a re-derivation owed at every reconcile, written in the conf beside them. This unit makes the
count of armed cutoff keys a gateable drift-audit signal with a pin, so a change that arms a new key
reds `drift-audit records` unless an old key stops being armed in the same change, and raising the
pin instead needs its reason written beside it.

## 2. Scope (IN)

- **S1** — A new signal, `cutoff_keys_armed`, in `tools/drift-audit/drift_report.py`. Its population
  is every assignment whose key ends `_CUTOFF` in a TRACKED root-level conf, a file whose path
  matches `^\.[^/]+\.conf$`. Its value counts the assignments whose value is non-blank, its `of`
  counts every assignment, and its detail lists each armed pair as file, key and value. Observed by
  AC1.
- **S2** — The signal reads each conf with the same line parser `load_conf` applies to the
  memory-tree conf. The loop body of `load_conf` becomes `parse_conf_text`, and `load_conf` calls
  it, so the kit keeps one conf grammar. Observed by AC1.
- **S3** — The probe's liveness assertion: a population with no `_CUTOFF` assignment in any root
  conf reports the signal DEAD, never 0, because the memory-tree kit's own example conf ships its
  cutoff keys and a reading of none means the probe read nothing. Observed by AC6.
- **S4** — The signal is gateable only where the project declares a pin for it in `PINS`. With no
  entry it reports with `gateable` false and a detail note saying no budget is declared, so an
  adopter is not red on its first `--check`. Observed by AC4.
- **S5** — This repo's `tools/drift-audit/drift_signals.py` pins the signal at the value it measures
  when the unit lands, and adds a `RATCHETS` row for that key weakening upward. A change that arms a
  new key then reds `drift-audit records` unless another key is unarmed in the same change,
  and a pin raised instead needs the `<was> -> <now>` line `ratchet_findings` already demands.
  Observed by AC2 and AC3.
- **S6** — The adopter template `tools/drift-audit/drift_signals.template.py` carries the key in its
  `PINS` block and its `RATCHETS` block as commented lines, with the instruction to seed the pin from
  the first report. Observed by AC5.
- **S7** — The kit README's signal table gains the row, and one paragraph names the three ways a key
  stops counting: its rule becomes unconditional and the key goes with its readers' date guards; two
  keys merge into one; or the key is blanked or unassigned, which disarms its rule. The paragraph
  says the signal cannot tell the third from the first two. Observed by AC5.
- **S8** — `memory/map/generated/symbols.json` is regenerated for the new definitions. NOT OBSERVED
  by a criterion here: `python tools/codebase-map/gen_map.py --check` at the close is its check, and
  §7 names the legs that read it.

## 3. Non-goals (OUT)

- Making any existing cutoff unconditional or merging two of them. Nine of the memory-tree conf's
  keys share one date, which makes a merge the obvious first candidate, but each is its own
  checker change with its own staged break; it is filed as an ask at this build's close.
- Counting `_CUTOFF` names that tool source spells and no conf assigns. Several are optional keys an
  adopter may set, and comments name retired ones; counting spellings would let a comment edit move
  the budget (§8 F1).
- Grading whether a key's date is past every spec it reaches. That is the cutoff-relation check
  `tools/check-spec-tokens.py` already runs for the keys it reads.
- Any rule about the order of units in this build. A later unit here that arms a new key meets this
  budget like any other change; unit 25's spec already declines a dated cutoff for that reason, and
  unit 26's citation form arms none.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564`; no file below moved between it and `6a88fbf7`.

- `.memory-tree.conf` assigns 22 `_CUTOFF` keys and `.unattended.conf` seven, every one non-blank;
  `.codebase-map.conf`, `.lexicon.conf` and `.process-monitor.conf` assign none. PINNED, counted
  2026-10-04 at `6a88fbf7`; S1's signal derives the figure from then on.
- The shipped examples arm one key between them: `tools/memory-tree/.memory-tree.conf.example`
  assigns 22 and arms one, and `tools/unattended/.unattended.conf.example` assigns seven and arms
  none. So an adopter graded at tolerance 0 would red on day one, which is S4's reason.
- `PINS` and `RATCHETS` in `tools/drift-audit/drift_signals.py` are the kit's budget with a reasoned
  raise: `--check` reds a gateable signal over its pin, and `ratchet_findings` reds an upward move of
  a declared scalar with no `<was> -> <now>` line within the lookback above it.
- `load_conf` in `drift_report.py` parses one named file; its docstring records two spellings its
  copy once dropped and the selftest arm that compares it with bash sourcing.
- `build_backlog_asks_unlabelled` is the shape a pinned count signal returns, and `SIGNALS` is the
  list `--check` walks.

### Data model

One report row:

```
{"signal": "cutoff_keys_armed", "value": <armed pairs>, "of": <every _CUTOFF assignment>,
 "tolerance": <PINS entry, else 0>, "gateable": <a PINS entry exists>, "live": <of > 0>,
 "detail": [{"file": ".memory-tree.conf", "key": "<KEY>", "value": "<value>"}, ...]}
```

Without a `PINS` entry the detail opens with `{"note": "no budget declared: add a PINS entry"}`.

### Inventory

- `build_cutoff_keys_armed` and `parse_conf_text` in `drift_report.py`; the builder joins `SIGNALS`.
- The `PINS` key and the `RATCHETS` row in `drift_signals.py`, and their commented twins in the
  template.

The lexicon leg grades each definition; a refused name takes its `--suggest` answer at build time
and this list is amended with a rev bump.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/drift_signals.py`
- `tools/drift-audit/drift_signals.template.py`
- `tools/drift-audit/README.md`
- `tools/drift-audit/selftest.py`
- `memory/map/generated/symbols.json`

### Rollout

The pin is seeded at the measured value in the commit that adds the signal, so the bar is green on
landing. The drift-audit kit version moves once, at this build's close, after the last pass that
touches the kit.

### Alternatives rejected

- **A new hygiene check over `.memory-tree.conf`.** It sees one kit's keys and misses the seven the
  unattended kit arms, and it adds a check number where the drift kit already owns a budget.
- **A gate comparing the key set against the base ref.** It needs a base on every run and cannot
  tell a key renamed from a key added. The pin answers the same question from the tree alone.
- **A report-only watermark.** The report asks that a new key MUST displace an old one; a watermark
  that never reds only makes the raise visible.

## 5. Production-readiness checklist

- security — N/A: reads tracked conf files the kit already reads one of; writes nothing.
- perf / scale — a handful of small files read once per run; no measurable cost on a 46 s leg.
- error / empty / loading states — no assignment at all is DEAD (S3); no pin is report-only with a
  note (S4); an unreadable conf is skipped and named in the detail.
- observability — the detail lists every armed key with its file and value, so the reader sees what
  to merge or make unconditional.
- risks — the budget can be met by blanking a key, which disarms its rule; the README says so, the
  diff shows it, and S7's paragraph names it as the route the signal cannot see.
- testing — direct runs on the live tree and in a scratch clone, plus one selftest arm.
- migration — none; the pin starts at the measured value.
- user docs — the kit README's signal table and the paragraph of S7.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py --json` runs on the live tree, the
  `cutoff_keys_armed` row reports `live` true, `gateable` true, `tolerance` equal to its `PINS`
  entry, and a `value` equal to the count printed by
  `git ls-files | grep -E '^\.[^/]+\.conf$' | xargs cat | grep -cE '^[[:space:]]*(export[[:space:]]+)?[A-Z0-9_]*_CUTOFF="[^"]+"'`.
  Red when: the value differs from that count, or the row is not gateable.
  cost: one report run, about 46 s on node a.
  figure: both counts DERIVED at observation time.
- **AC2** — When, in a `git clone --local` of the unit's branch under `%TEMP%`, one new armed
  `_CUTOFF` assignment is appended to `.memory-tree.conf` as the staged break,
  `python tools/drift-audit/drift_report.py --check` names `cutoff_keys_armed` as over its pin; and
  when one existing assignment is then blanked in the same file, the next run does not name it.
  Red when: the first run does not name the signal, or the second still does.
  cost: two report runs in the clone.
- **AC3** — When, in that clone, the `PINS` entry in `tools/drift-audit/drift_signals.py` is raised
  by one with no comment, `drift_report.py --check` prints the `RATCHETS` finding naming the key as
  weakened with no justification; with a comment line spelling the old and new values joined by
  `->` above it, the finding is absent.
  Red when: the unjustified raise passes.
- **AC4** — When, in that clone, the `PINS` entry is deleted, `drift_report.py --json` reports the
  row with `gateable` false and the no-budget note, and `--check` does not name it.
  Red when: the unpinned signal reds `--check` or reports `gateable` true.
- **AC5** — When `grep -n "cutoff_keys_armed" tools/drift-audit/README.md tools/drift-audit/drift_signals.template.py`
  runs, the README's signal table carries the row, its paragraph names the three routes, and the
  template carries the commented `PINS` and `RATCHETS` lines.
  Red when: either file lacks the key.
- **AC6** — When, in that clone, every `_CUTOFF` assignment line is deleted from every root conf,
  `drift_report.py --json` reports the row with `live` false, and `--check` names it as a dead
  gateable probe.
  Red when: the row reports `value` 0 with `live` true.

## 7. Gates

`drift-audit records` · `drift-audit selftest` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · a fixture with two root confs carrying armed, blank, exported and commented cutoff lines, staged red by dropping the builder from SIGNALS · none

## 8. Open questions

- **F1 — Which assignments are the population?**
  Options: the memory-tree conf only; every tracked root-level conf; those plus every `_CUTOFF` name
  tool source spells. The first misses the seven the unattended kit arms. The third counts comments
  and optional keys nobody set, so a comment edit would move the budget, which is a signal satisfied
  by matching nothing.
  RESOLVED (agent, 2026-10-04, delegated): every tracked root-level conf.
- **F2 — Does a blank assignment count?**
  Options: every assignment; only armed ones. Counting every assignment starts each adopter at the
  example conf's 29 blank and armed lines and makes blanking cost nothing it should. A blank key
  shapes no spec, and the report's harm is a spec's shape depending on its date.
  RESOLVED (agent, 2026-10-04, delegated): only armed assignments count; `of` keeps the total.
- **F3 — Is the signal gateable for an adopter that declares no pin?**
  Options: gateable at the kit's default tolerance of 0; gateable only where a pin is declared. The
  first reds every adopter on its first `--check`, since the shipped example arms a key, and a
  guessed shipped pin is what the template's `PINS` block forbids.
  RESOLVED (agent, 2026-10-04, delegated): gateable only where a pin is declared.
- **F4 — Where does the budget live?**
  Options: a drift signal with a pin; a new hygiene check; a gate diffing the key set against the
  base ref. §4's alternatives give the reasons; the pin and `RATCHETS` already are a budget whose
  raise needs a reason.
  RESOLVED (agent, 2026-10-04, delegated): a drift-audit signal with a pin and a `RATCHETS` row.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from `PINS`, `RATCHETS`, `ratchet_findings` and `load_conf` at
  base, and a count of every cutoff assignment in the tracked root confs and the shipped examples.
- rev-2 · 2026-10-04 · §3 · S8 · §4 · §7 · M2 cross-read: §3 named unit 25's ceiling and unit 26's
  citation form as later units arming a key, but unit 25's spec declines a dated cutoff because of
  this budget and unit 26 arms none; and the new definitions owe `symbols.json`, which units 57, 59
  and 90 regenerate and this spec omitted.

## 10. Reuse audit

The seams extended are the drift-audit kit's pin and ratchet machinery: `PINS` and `RATCHETS` in
`tools/drift-audit/drift_signals.py`, `ratchet_findings` and the `--check` over-tolerance walk in
`tools/drift-audit/drift_report.py`, and its `load_conf`, whose loop S2 lifts into one parser.
`python tools/codebase-map/reuse_lookup.py "count declared conf keys against a shrink-only pin"`
named `load_conf` at fan-in 16, among its copies the one in `drift_report.py`, and no function that
counts conf keys of a kind, so no counting seam fits and the pin machinery is extended instead.
Recall named `TOOL-aDeclaredBound-2`, which moved `SPEC10_CUTOFF` into the conf beside its
siblings, and `TOOL-aRuledFrontispiece-10`, whose alternatives record the owner declining a
filename-date cutoff once because it leaves a corpus permanently two-shaped. Where the report and
the tree disagree: the report counted 22 dated cutoffs, which is the memory-tree conf alone; the
tree arms 29 across two confs, PINNED as counted 2026-10-04 at `6a88fbf7` by AC1's command.

Recall terms used: `python tools/memory-recall/query.py "was a budget or cap on the number of dated cutoff keys ever proposed or rejected" --terms "cutoff budget SPEC_FORMAT_CUTOFF dated cutoffs retire ratchet pin drift signal RATCHETS record_overhead_ratio kit version"`
