# TOOL-aMendedFleet-50 — a monthly escape-ratio report, outside the seconds tier

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 50

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Nothing in this repo reads an OUTCOME: whether the governance makes the shipped code better. The
review measured one with a scratch script: of the product fixes landed in August and September, the
share that repaired code which had already reached the default branch, 116 of 297 (0.39), flat
between the two months. That script was never committed. This unit adds it to the drift-audit kit
as an on-demand mode, `drift_report.py --escape-ratio <month>`, which classifies each product fix of
one month by first-parent landing and blame, drops version and stamp lines, and prints n, the
escaped count and ratio with a 95% Wilson interval, and the DIRECT share. It is never part of the
seconds-tier report, never on the bar and never on the orientation card, and it prints no
comparison between months, because one repository's before and after is not evidence of an effect.

## 2. Scope (IN)

- **S1** — `drift_report.py --escape-ratio <month>`, the month written as four-digit year, hyphen,
  two-digit month. It computes no drift signal, so the seconds tier is not paid and not changed, and
  it refuses to combine with `--check`, `--offenders` or `TOOL-aMendedFleet-49`'s `--delta`, the
  other mode added to the same parser. `--json` prints the same result as one
  object with a per-fix list. A malformed month is refused with exit 2. Observed by AC1 and AC5.
- **S2** — LANDINGS, from ONE `git rev-list --parents` of the base ref that `resolve_base_ref`
  resolves. Walking the first-parent chain oldest first, every commit newly reachable from a
  first-parent commit is assigned that commit as its landing, so the landings partition history and
  a commit's landing index orders when it reached the base. The month's landings are the
  first-parent commits whose committer date falls in that month, in UTC. Observed by AC2.
- **S3** — PRODUCT FIXES: the non-merge commits landed by the month's landings whose subject's first
  word is `fix`, optionally followed by a parenthesised scope, and whose diff touches a path under
  the project layer's `PRODUCT_GLOBS`. A fix's PARENT-SIDE lines are the lines its diff takes out,
  as they read in its parent. The month's fixes and their parent-side lines come from ONE
  `git log --no-merges --no-renames -U0 -p` over the month's landing range, restricted to those
  globs. Observed by AC2.
- **S4** — STAMP FILTER: a parent-side line matching the engine's declared stamp patterns is
  filtered out before blame. The patterns are a `gov:kit <name>@` marker, a `KIT_..._VERSION =`
  assignment, a `version = "` line, and a `last-audit:` or `last-body-change:` stamp. A fix with no
  parent-side line left is UNCLASSIFIED, with the reason `addition-only` or `stamp-only`, and is
  outside n. Observed by AC3.
- **S5** — CLASSIFICATION: each remaining parent-side line is blamed in the fix's parent, one
  `git blame --porcelain` per fix and file with every range as its own `-L`. A fix is ESCAPED when
  any blamed commit's landing index is lower than the fix's own; otherwise CONTAINED. A boundary
  commit counts as an earlier landing. Observed by AC2.
- **S6** — DIRECT: a fix whose landing is the fix itself, a commit made directly on the first-parent
  line. Every such fix that blames anything is escaped by construction, so the DIRECT share of n is
  printed beside the ratio to say how much of it measures workflow rather than defects. Observed by
  AC1 and AC2.
- **S7** — OUTPUT: one line each for n, escaped and ratio with the Wilson 95% interval, the DIRECT
  share, the unclassified counts by reason, and the base ref and sha it walked; then one fixed
  caveat line saying a difference between two months of one repository is not evidence of an
  effect. The interval is computed with `math` alone. Observed by AC1 and AC4.
- **S8** — The kit README gains a short section: what the mode measures, its cost, and the caveat.
  The Skill is not touched; the Skill's tiers stay as they are. Observed by AC5.
- **S9** — The kit selftest gains one arm over a fixture history with a merge-landed contained fix,
  a merge-landed escaped fix, a direct fix, a stamp-only fix and a non-product fix. NOT OBSERVED by a
  criterion here: the suite runs once at the close, and the arm is declared under `New arm:` in §7.
- **S10** — `memory/map/generated/symbols.json` is regenerated for the new definitions. NOT OBSERVED
  by a criterion here: `python tools/codebase-map/gen_map.py --check` at the close is its check, and
  §7 names the legs that read it.

## 3. Non-goals (OUT)

- A comparison mode between months, a trend, a significance test or any printed claim of change.
  The report's own caveat forbids the claim, so the tool does not make one.
- An orientation-card line or a drift signal reading the ratio. The report ruled both out: at about
  150 fixes a month the interval is about plus or minus 0.08, too wide to steer a session.
- The median escape age the review also quoted. It is a second figure with its own definition, and
  the brief names n, the interval and the DIRECT share only.
- Validating the ratio on an adopter that lands by direct commit. The review said it is validated
  on this repository only, and S6 makes that visible rather than fixing it.
- A project-layer override of the stamp patterns. One adopter's stamp shape is not known yet.
- Scheduling a monthly run. "Monthly" is a reading cadence for the owner; nothing here installs a
  scheduled task.
- Bumping the drift-audit kit version here; it is owed once at the build's close.

### Edges

- **consumes-from** external — `PRODUCT_GLOBS` in the project layer, and the base ref
  `resolve_base_ref` already resolves. Without the globs every fix is unclassified, as the
  `drift-product-globs` hole already says for the seconds tier.
- **hands-off** external — the kit version bump owed at the build's close.

## 4. Design

### Data model

The `--json` object: `month`, `base_ref`, `base_sha`, `n`, `escaped`, `ratio`, `interval` as a
two-element list, `direct`, `unclassified` as a reason-to-count map, and `fixes`, a list of
`{sha, landing, direct, class, blamed_landings}` where `class` is `escaped`, `contained` or the
unclassified reason.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `--escape-ratio` | CLI flag of `drift_report.py` | CLI subcommand flag |
| `build_landing_index` | function | Python function, verb `build` |
| `read_month_fixes` | function | Python function, verb `read` |
| `check_stamp_line` | function | Python function, verb `check` |
| `measure_escape_ratio` | function | Python function, verb `measure` |
| `derive_wilson_interval` | function | Python function, verb `derive` |
| `render_escape_ratio` | function | Python function, verb `render` |
| `ESCAPE_STAMP_PATTERNS` | engine constant | Python constant |

### Cost

Two whole-history git calls and one `git log -p` over the month's range, then one blame per fix and
product file. At about 150 fixes a month and two files each, that is about 300 blame spawns: under a
minute on a host where a spawn costs 70 ms, about four minutes where one costs 751 ms. That is why
it is a mode and never a signal.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- A separate script in the kit. It would re-import the engine's project-layer loader and base-ref
  resolver anyway, and the map inventories no kit script, so a file buys nothing a flag does not.
- Importing `build_graph` from `tools/memory-tree/transition_audit.py` for the walk. The drift kit is
  copy-installed and reaches sibling kits only for declared engines; the one-call parent walk is
  already spelled inside `build_nonterminal_merged_runs`, and S2 spells it the same way.
- Classifying by commit dates rather than landings. A branch commit authored before an earlier merge
  but landed after it would read as already on the base, which is the error "classify by landing"
  exists to remove.

## 5. Production-readiness checklist

- security — N/A — reads local history only; the month is parsed by a fixed pattern before use.
- perf / scale — §4 Cost; on demand only, and refused beside `--check`, so the bar never pays it.
- error / empty / loading states — a month with no landing prints n 0, no ratio and no interval,
  and says the month is empty rather than printing 0.0; a malformed month exits 2.
- observability — `--json` lists every fix with its class, so a figure can be re-derived by hand.
- risks — subject-prefix fix detection misses a fix not called one, and blame attributes moved code
  to its mover; both bias the ratio and are stated in the README section.
- testing — AC1 to AC5 observe the live tree and pure functions directly; the selftest arm is S9's.
- migration — N/A — a new mode.
- user docs — S8's README section.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py --escape-ratio 2026-09` runs on node a,
  it prints n, escaped, the ratio with an interval, the DIRECT share and the caveat line, and
  `python tools/drift-audit/drift_report.py --escape-ratio 2026-09 --json` reports an `n` equal to
  the number of its `fixes` entries whose `class` is `escaped` or `contained`.
  Red when: n counts an unclassified fix, or the caveat line is absent.
  cost: minutes, per §4.
  figure: DERIVED at observation time; the review measured 116 of 297 over two months, UNVERIFIED
  here because its script was not committed.
- **AC2** — When one `escaped` and one `contained` entry of AC1's `--json` are re-derived by hand,
  each `blamed_landings` commit satisfies `git merge-base --is-ancestor` against the fix's landing,
  the escaped one names a landing that is an ancestor of the fix's landing's first parent, and the
  contained one names only the fix's own landing; and every entry with `direct` true is its own
  `landing`.
  Red when: a contained fix blames an earlier landing, or a direct fix names a merge as its landing.
- **AC3** — When `python -c` imports `drift_report` from `tools/drift-audit` and calls
  `check_stamp_line` on a `gov:kit drift-audit@1.22` marker line, a `KIT_DRIFT_AUDIT_VERSION = "1.22"`
  line, a `version = "1.0"` line, a `last-audit:` line and an ordinary assignment, the first four
  return true and the last returns false.
  Red when: a stamp line survives the filter, or an ordinary line is dropped.
- **AC4** — When `python -c` calls `derive_wilson_interval` with 116 and 297, it returns bounds
  that round to 0.3368 and 0.4471; with 0 and 5 they round to 0.0 and 0.4345; with 0 and 0 it
  returns no interval.
  Red when: the interval is a normal approximation, which goes below 0 at k 0, or a zero n divides.
- **AC5** — When `python tools/drift-audit/drift_report.py --escape-ratio 2026-9` and
  `python tools/drift-audit/drift_report.py --escape-ratio 2026-09 --check` run, each exits 2 with a
  message naming the problem, and `grep -c -- "--escape-ratio" tools/drift-audit/README.md` reports at
  least 1.
  Red when: a malformed month runs, the mode runs inside the bar's mode, or it ships undocumented.

## 7. Gates

`drift-audit records` · `drift-audit selftest` · `drift-audit wiring` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: `tools/drift-audit/selftest.py` · a fixture history with a contained, an escaped, a direct, a stamp-only and a non-product fix, landed by merges and by direct commit · `CHECK_FLOOR` moves by the checks the arm adds

## 8. Open questions

- **F1** — What is a product fix?
  RESOLVED (agent, 2026-10-04, delegated): a non-merge commit whose subject's first word is `fix`,
  with an optional scope, that touches `PRODUCT_GLOBS`, per S3. It is the convention this repo's
  subjects follow, 425 non-merge `fix` subjects in August and September on `origin/main`, and the
  globs are the seconds tier's own definition of product.
- **F2** — What does DIRECT mean?
  RESOLVED (agent, 2026-10-04, delegated): the share of n landed by a direct first-parent commit,
  per S6. The review tied the figure's validity to landing by merge, and this is the share for which
  that does not hold.
- **F3** — Escaped on any blamed line, or on most?
  RESOLVED (agent, 2026-10-04, delegated): any, per S5. A fix repairing one line that had reached
  the base repaired escaped code, however much branch-local code it also touched.
- **F4** — Which interval?
  RESOLVED (agent, 2026-10-04, delegated): Wilson. It stays inside 0 and 1 at small n and at a
  ratio of 0, which a normal approximation does not, and it needs nothing outside `math`.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft.
- rev-2 · 2026-10-04 · S1 · S10 · §4 · §7 · M2 cross-read: S1's refusals named `--check` and
  `--offenders` but not `--delta`, which `TOOL-aMendedFleet-49` adds to the same parser first, so
  the pair's combination was defined by neither; and the new definitions owe `symbols.json`, which
  units 57, 59 and 90 regenerate for theirs and this spec omitted.

## 10. Reuse audit

No existing seam fits the measurement itself. `python tools/codebase-map/reuse_lookup.py "classify
fix commits by blame and first-parent landing to measure escapes"` returned name-stem neighbours,
`classify` in the govkit census and `measure_commitment` in the runlog record, none of which reads
landings or blame. `git grep -n -i "wilson" -- tools` finds nothing, and `git grep -n -- "--first-parent"`
over the Python tools finds only diff-merge options. The pieces it extends are in
`tools/drift-audit/drift_report.py`: `load_project_layer` for `PRODUCT_GLOBS`, `resolve_base_ref`,
the `Git` wrapper, the one-call parent walk inside `build_nonterminal_merged_runs`, and
`_build_blame_dates`, the kit's existing porcelain-blame parser, whose sha-header handling S5 reuses.
`build_graph` in `tools/memory-tree/transition_audit.py` is the same walk in a sibling kit and is
rejected in §4. Where the report and the tree disagree: the 116 of 297 figure could not be
re-derived without building this unit, so §6 marks it UNVERIFIED.

Recall terms used: `python tools/memory-recall/query.py "is there an escape ratio or outcome measure
of fixes reaching main" --terms "escape ratio fix commits blame first-parent landing outcome reading
monthly interval SZZ product fixes"`
