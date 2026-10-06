# drift-audit kit

`gov:kit drift-audit@1.23` — the marker a deployer greps; paired with `KIT_DRIFT_AUDIT_VERSION` in
`drift_report.py` and asserted equal by `<prefix>/check-kit-versions.sh`, which also holds each Tier-2
harness's own `meta.version` to the same number.

**Migrating 1.10 → 1.11 (additive, no caller edit).** One new signal,
`run_records_nonterminal_but_merged`, report-only, so `--check` cannot red on it. A repo with no run
record and no `.unattended.conf` reads it as NOT ASKED. A repo that does keep run records reads a
non-zero value against tolerance 0 until it seeds a pin at the value it measures, as the install steps
below say for every signal. No existing field or signal moves.

**Migrating 1.7 → 1.8 (additive, no caller edit).** Three changes, none of which moves an existing
field. `drift-audit-state.js` gains the aggregate `severityCorrections` return key and the matching
downgrade count on its RUN INTEGRITY line, both of which `drift-audit-code.js` has carried since
1.4 — the per-finding value already reached the synthesis writer, so this adds the number an
operator reads without opening the report. `drift_report.py`'s conf parser gains `map_lib`'s
`export ` prefix rule and its ends-at-whitespace rule, which it had claimed in its docstring and did
not implement: a conf spelling `export K=v` now yields key `K`, and `K=v  # note` now yields `v`
rather than `v  # note`. **That is the one observable behaviour change**, and it only reaches a repo
whose `.memory-tree.conf` uses either spelling; no tracked conf in this repo does. Finally
`shrink_only_lists_not_shrinking` stops counting a list that was seeded EMPTY and is still empty,
which could never shrink and made the signal unable to reach its own tolerance of 0. A list that
GREW is still an offender.

**Migrating 1.6 → 1.7 (breaking, one RETURN field).** `lensesRun` on the Tier-2 harnesses was an
ARRAY of lens slugs in `drift-audit-state.js` and is now an INTEGER, the count of lenses that
actually returned. A caller reading it as a list breaks, loudly, on a type error rather than quietly
on a wrong value; no caller in this tree reads it. `drift-audit-code.js` returned no lens information
at all and now returns the same integer. Everything else added is additive — `lensesDead`,
`skepticsDead`, `conflicts`, `duplicates`, `spurious` and `note` — so an adopter passing the same
`args` needs no edit. One behaviour change is observable: a run whose lenses ALL died, or whose
configured lens set is empty, now returns early with those counters instead of synthesizing a report
over an empty finding set. That path previously produced a confident report about nothing.

**Migrating 1.0 → 1.1 (breaking, `args` only).** The two Tier-2 harnesses no longer accept a
caller-supplied concurrency cap or verifier total; both are bare literals matching the review
protocol's ≤5. Delete those two keys from any `args` object you pass — they are ignored, not
honoured. Nothing else in the contract moved. The knobs never worked as documented on any adopter
whose `agent-cap.js` enforced the rule: the guard read the literal on the fallback's right-hand side
and the runtime used the caller's value, so the two disagreed silently. `agent-cap.js` 1.2 now
resolves the bound and denies that binder form, which is what makes the removal load-bearing rather
than cosmetic.

Measures whether a repo's own **records** still describe reality, and — at higher tiers — hunts dead,
unwired and duplicated code. Ported from adopter ic's audit that found a repo where 24 of 58 in-flight
ledger rows contradicted git and roughly half of all non-terminal spec headers said "not built" about
shipped work, with every hygiene check green throughout.

Nothing was lost in that repo. The records had simply stopped being readable, and it took a human's
hunch to notice. This kit is the machine that notices instead.

## The premise

A governance repo gates its **code** contracts hard and its **record** contracts not at all. A
memory-hygiene gate checks that a spec Status token is spelled legally; nothing checks whether it is
**true**. That gap is where drift lives, and it is invisible by construction.

The four dispositions, in cost order — most records need the first, which is free:

| | When | Example |
|---|---|---|
| **Delete** | git or a generated file can derive it | a ledger's landed-state prose |
| **Gate** | must stay written, an oracle exists | spec Status headers |
| **Pin** | countable, no clean oracle | the three pins below |
| **Declare** | genuinely non-derivable | "was the human security review done?" |

The fourth row is real. Keep it **small and loud**, not buried in prose.

## Install

```bash
mkdir -p <target-repo>/<prefix>
cp -r <governance>/<prefix>/drift-audit <target-repo>/<prefix>/drift-audit
cd <target-repo>
<prefix>/drift-audit/adopt-drift-audit.sh
```

Requires `.memory-tree.conf` (owned by the memory-tree kit). This kit reads `MEMORY_ROOT` from it and
**declares no conf of its own** — there is deliberately no `--memory-root` flag. A second way to state
the same value is the hand-kept-second-copy defect the kit exists to detect.

Then, in order:

1. Fill `<prefix>/drift-audit/drift_signals.py` — `PRODUCT_GLOBS` at minimum.
2. Run `python <prefix>/drift-audit/drift_report.py`.
3. **`RATCHET_LOOKBACK` is optional and shipped at 14** — how many lines above a ratcheted pin the
   gate looks for the `<old> -> <new>` justification that excuses a weakening move. Narrow it if
   your pins sit close together, so a justification for a DIFFERENT pin cannot be read as this
   one's; widen it if your repo writes long justifications above a pin. This tree has two pins
   three lines apart at the same value, which is the case that makes the first half real.
4. **Seed `PINS` at the values you just measured, not at zero.** A pin above the measured value hides
   a live regression on day one; a pin below it reds the bar on work nobody did. Where a gateable
   signal's rows each carry an `id`, seed `BASELINES` with the measured ids instead of a pin for it.
4. Wire `--check` into your gate manifest.

## Layout

| File | Owner | What |
|---|---|---|
| `drift_report.py` | kit | the engine: the signal implementations, `--json`, `--check`, `--delta`, `--escape-ratio` |
| `drift_signals.template.py` | kit | the project layer's starting point |
| `drift_signals.py` | **project** | `PRODUCT_GLOBS`, `SHRINK_ONLY`, `HANDKEPT`, `PINS`, `RATCHETS`, optional `BASELINES`, `CHARTER`, `TRACE_CUTOFF`, `TRACE_GLOBS`, `TRACE_WAIVER`, `RATCHET_LOOKBACK`, `REMOTE_CI_WORKFLOW`, `AUTO_MEMORY_DIR`, `DEAD_READINGS_LIMIT`, `DEAD_FILED` |
| `SKILL.template.md` | kit | rendered to `.claude/skills/drift-audit/SKILL.md` by the adopt script |
| `adopt-drift-audit.sh` | kit | adopt + the `--check` sync arm for the merge bar |
| `selftest.py` | kit | the kit's own falsifiability test |
| `<git-common-dir>/drift-history.tsv` | **node** | written by `--check`: one row per signal per run, never pushed |

Tier 2 needs the two workflow scripts from `<prefix>/workflows/drift-audit-{code,state}.js`.

## The signals

A report-only signal with no pin by design prints `report only, no pin` in the status column, never
`over pin 0`: it has nothing to be over, so the column states that rather than raising a red-looking
word nobody acts on. Its `--json` record carries `null` for both `tolerance` and `pin`. A project
that wants a threshold for one declares it in its `PINS`, and the column then compares against it.
Which signals are pinless is the status column's to say, not this paragraph's; a gateable signal
never is. A gateable signal whose rows each name their offender by `id` may take an id set in
`BASELINES` instead of a `PINS` count; its status then reads `ok (baseline <n>)` or `OVER BASELINE`.

| Signal | Asks | Gateable |
|---|---|---|
| `lexicon_marginal_offense_rate` | how many naming offenders came in per definition added since the commit that adopted the lexicon declaration? Both operands are derived by the lexicon's own extractor at both shas. | no |
| `ledger_rows_contradicting_git` | does an in-flight row claim "not merged" about a landed sha? | yes |
| `non_terminal_specs_cited_by_product_source` | does a SPECCED/INPROGRESS spec describe shipped work? | yes |
| `shrink_only_lists_not_shrinking` | has a list that promises to shrink risen above the lowest count its first-parent history reached (`regrown`), or held at least the rows it was seeded with (`never drained`)? A row whose history cannot be replayed is `unjudgeable`, never an offender. | no |
| `handkept_inventories_disagreeing_with_source` | does a hand-kept list still match what generates it? | yes |
| `dangling_pointers_in_own_ledger` | do this node's auto-memory notes (`AUTO_MEMORY_DIR`) name repo paths that `git ls-files` still carries? | no |
| `closed_specs_with_no_product_commit` | does a CLOSED spec have a commit that names it and changed the product? A spec whose status header carries the field `records-only` declares a records deliverable: it is set aside before the commit join and listed under `records_only` in `--json`, and a `trace-waiver.txt` row beside it reports stale. | yes |
| `lexicon_verbs_declared_but_unused` | does the verb table still describe the code it was derived from? | yes |
| `lexicon_ratified_older_than_language_surface` | was the table curated since the languages it grades last moved? | yes |
| `live_backlog_rows_per_shard` | is a shard’s live set approaching the floor rotation cannot clear? Under `BACKLOG_MODE="builds"`, how many asks derive live, read from the generator’s own live projection? | no |
| `readme_mechanism_drift` | does a build README still describe a mechanism its own spec set revised? Grades live builds only: a build whose every spec is CLOSED or WONTDO is a frozen record and is skipped, and `of` counts the READMEs of live builds. | no |
| `backlog_asks_contested` | does an ask carry both closing and declining evidence, or terminal evidence beside a live spec? Not asked under `shards`. | no |
| `backlog_evidence_sha` | does every `by <sha>` closing an ask resolve to a commit in this clone? Not asked under `shards`. | no |
| `backlog_asks_unlabelled` | how many live asks carry no severity row? Not asked under `shards`. | no |
| `open_asks_cited_by_product_source` | does a live ask name work that already shipped? Counts the asks of the generator's live projection whose id tracked `EVIDENCE_GLOBS` source cites, by signal 2's whole-word match in one `git grep`; the detail names each with its status and up to three citing paths. DEAD PROBE when the projection cannot be read or the globs resolve to no file; not asked under `shards`. Report-only until a sampled precision exists, because source legitimately cites an ask it has not fixed yet. | no |
| `backlog_stragglers` | does a ref still carry backlog row changes unaccounted against the default branch? | no |
| `asks_disposed_overrides` | how often did a run buy the `asks-disposed` Definition-of-Done item with an override? | no |
| `run_records_nonterminal_but_merged` | does a run record still read live after its work reached the default branch? | no |
| `aborted_work_landed` | does a live ABORTED record dated before `HANDOFF_CUTOFF` have work the content predicate reads landed, with no upheld `work-landed-at`? Cleared by the unattended kit's `--settle`; an archive is listed and not counted. | no |
| `discarded_work_landed` | did the work of an ABORTED record dated on or after `HANDOFF_CUTOFF`, when ABORTED means discard, land anyway? No verb clears it. Not asked while the key is blank. | no |
| `legs_retried_after_timeout` | how many legs did the merge bar retry, once and alone, after their own ceiling fired, over the run records every git dir of the clone still holds — the common dir and each linked worktree's — and which legs, how often each failed on its retry? A removed worktree takes its records with it. | no |
| `fleet_over_budget` | which builds hold more undeclared writes than the unattended kit's per-build `UNDECLARED_WRITE_BUDGET`, read from the `check 23 fleet` line of the newest bar run any git dir of the clone holds? A line reading `over unjudged` is DEAD PROBE, never 0. Not asked without `.unattended.conf`. | no |
| `remote_ci_red_streak` | how many consecutive completed runs of the declared remote CI workflow on the default branch failed, newest first? Read through `gh`; DEAD PROBE when `gh` cannot answer, not asked under `--check` or with no workflow declared. | no |
| `cutoff_keys_armed` | how many `_CUTOFF` keys carry a non-blank value across the tracked root-level `.<name>.conf` files? `of` counts every such assignment. | only where `PINS` declares it |
| `source_cited_ids_resolving_to_no_record` | does every id cited in tracked source resolve to a record, an anchor line under the memory root or a spec's own H1? | no |
| `dossiers_older_than_their_paths` | how many codebase-map feature dossiers are older than their paths — a commit touching a path the dossier claims is not an ancestor of the dossier's own last commit? Read from the map kit's own `map_diff.py --stale-dossiers --json`, so the attribution is spelled once; map-root paths are never a claim, and a merge commit carries no paths, so a change made only in a conflict resolution is not seen. The detail is the refresh worklist, most-behind first. Not asked where the map kit is absent or unadopted; DEAD PROBE on a shallow clone or when nothing touched a claimed path. | no |
| `live_builds_without_activity` | how many live builds are dormant? Counts the `dormant` cells of the `Activity` column the memory-tree generator renders into `LIVE.md` against its `LIVE_DORMANT_DAYS`, found by header name, and defines no dormancy rule of its own; `of` counts the `active` and `dormant` rows, any other cell is unjudgeable, and the detail names each dormant build with its `Last record`. Not asked where `LIVE.md` or its `Activity` column is absent. | no |

### Armed cutoff keys are a budget

Every armed `_CUTOFF` key makes a record's required shape depend on a filename date, so
`cutoff_keys_armed` is pinned: a change that arms a new key reds `--check` unless an old one stops
counting in the same change. A key stops counting in one of three ways. Its rule becomes
unconditional, and the key goes with its readers' date guards. Two keys merge into one. Or the key
is blanked or unassigned, which disarms its rule. The signal cannot tell the third from the first
two; the diff shows which one happened. With no `PINS` entry the signal reports and never gates,
because the shipped example confs arm a key. When no tracked root conf assigns any `_CUTOFF` key
the signal reads DEAD PROBE, never 0.

**Every signal carries a `live` field.** A signal whose population is empty prints `DEAD PROBE`
instead of a clean `0`. This is the kit's central rule and it is not decoration: the upstream repo's
convergence tool shipped a `collision_flags` signal structurally incapable of being non-zero, and
every reader took the 0 as "converged" for thirteen days. A metric that cannot move is worse than no
metric, because it is read as good news.

**A report-only probe dead for N readings is named for retirement.** "Ignore its value" is honest
once and is how a dead probe survives for months. The report reads `--check`'s history,
`<git-common-dir>/drift-history.tsv`, once per run and before it appends; a READING is the last group
of a run of consecutive groups at one sha, so a bar re-run at one commit ages nothing. A report-only
signal dead for at least `DEAD_READINGS_LIMIT` readings in a row (10 when undeclared) prints
`DEAD PROBE for <k> readings` and asks you to take it out of `SIGNALS`, or to file an ask and map the
signal to its id in `DEAD_FILED`, after which it prints `filed <id>`. The header carries one `# dead-for-N:`
line naming the readings it found, or that it found no history; a `DEAD_FILED` entry naming a signal
that is absent or live is named there too. It is REPORT-ONLY because the history is node-local and
never pushed: a verdict built on it would pass on a fresh clone and fail on an old one at one sha.
The `--json` record carries `dead_readings`, `null` when no history was read.

The kit holds itself to that rule — `selftest.py` exercises each gateable signal **twice**, once on a
fixture where it must be silent and once on a minimal violating fixture where it must fire. An arm
that can only pass the first is the dead probe the report refuses.

### Run records left non-terminal after their build merged

An unattended run's record can keep saying `LANDING` or `BUILDING` after its work is on the default
branch, so "did it land?" cannot be answered from the record. The signal reads every tracked
`RUN.md`, and every rotated `RUN.<phase>.<blob8>.md`, **at HEAD and never in the working tree**. It
counts a record whose phase is not terminal, whose witness is an ancestor of the base ref, and whose
witness is neither equal to nor behind the record's own `base:`. A `LANDING` record whose landing
commit, the newest commit at HEAD that changed it, is on the base ref reads **derived LANDED** and is
neither counted nor unjudgeable; the detail's summary line counts those. It reports and never gates, because
a sanctioned worktree landing raises the count through nobody's fault.

A witness at or behind its base is **unjudgeable**, not clean. The witness is HEAD at the last verb
that writes one, and `--close` writes none, so such a run may well have landed. The signal counts it
apart with its reason, and every other record whose facts it cannot place goes there too.

Each counted record gets one sub-class, read from its **last** parked row: `retired-unit`,
`surfaced-park`, `no-rows` or `other`. The first-match table that decides it is
`_derive_run_subclass` in `drift_report.py`, and it is not restated here. Its kinds and acts are the
unattended driver's own declared sets, spelled in the engine so the report runs in a tree without that
kit, and `selftest.py` holds each set to the driver's source wherever the driver is present. A refused
landing leaves no tracked row, so no sub-class can name one, and the detail says so on every run.

### The harness note is a DERIVED contract, not prose

Both `drift-audit-code.js` and `drift-audit-state.js` build their run `note` from
`deriveLiveness(counters)` and `renderLivenessNote(state, counters)`. **The sentence is a contract**
(`TOOL-dRetiredFork-6`, ratified F1): a consumer gate re-derives it and byte-compares, which is what
a hand-written string can never satisfy — and relaxing such a gate to a substring match makes it
satisfiable by prose, the first class the charter's §7 names.

Three states, three distinct sentences, and the split is the point:

| state | when | the sentence opens |
|---|---|---|
| `clean` | synthesis returned, no lens or skeptic died, nothing unverified | `CLEAN:` |
| `partial` | something died or something is unverified, but the run measured | `PARTIAL:` |
| `dead` | synthesis died, OR no lens ran at all | `DEAD PROBE:` |

The retired ternary had three branches and conflated the last two into the bare word `complete`, so
a run that measured NOTHING reported the same word as a clean one. Changing any of these sentences
is a version bump like any other.

## The reading history — `drift-history.tsv`

Every `--check` run, the mode the merge bar's leg executes, appends one GROUP of rows to
`drift-history.tsv` in the directory `git rev-parse --git-common-dir` names, so every worktree of a
clone writes one history. `--offenders`, `--json` (even beside `--check`) and the plain table never
write. The file is node-local: it lives in the git dir, so git never pushes it.

The first line is a header, `#utc`, `sha`, `base_ref`, `base_sha`, `signal`, `state`, `value`, `of`,
`key_hash`, tab-separated, and readers locate columns by it, never by position. A group shares `utc`
and the full HEAD `sha`; `state` is `live`, `dead`, `not-asked` or `declared-empty`; `key_hash` is 16
hex of the SHA-256 over the record's detail keys as `--offenders` spells them, so it moves when the
members change at an equal count and not when a line number moves, and is `-` for any state but
`live`. One group per bar, one row per entry of `SIGNALS`, and no rotation. A write that fails prints one
`history NOT written` line on stderr and never changes the exit status; a write that succeeds prints
one stdout line naming the row count and the path.

`--delta <base> <head>` is the history's one reader, and the unattended close prints its output as a
report-only block. It compares the last group read at BASE or an ancestor of it with the last group read
inside BASE..HEAD, printing one line per signal whose value, state or `key_hash` moved, and every case
that cannot produce a delta prints one `skipped` line at exit 0; only an argument that is not a commit
exits 2.

## The escape ratio — `--escape-ratio <YYYY-MM>`, on demand only

Every signal above reads a RECORD; this mode reads an OUTCOME. `drift_report.py --escape-ratio 2026-09`
takes the month's product fixes — non-merge commits whose subject's first word is `fix`, with an
optional scope, touching `PRODUCT_GLOBS` — and calls one ESCAPED when any line its diff takes out,
blamed in its parent, landed on the base before the fix did. A landing is the first-parent commit that
first made a commit reachable, and the month's landings are the first-parent commits dated in it, UTC.
Version and audit stamps are dropped before blame, and a fix left with no line is unclassified and
outside n. It prints n, escaped, the ratio with its 95% Wilson interval, the DIRECT share — fixes made
on the first-parent line itself, escaped by construction, so that share measures workflow rather than
defects — and `--json` lists every fix with its class so any figure can be re-derived by hand.

It costs one blame per fix and file, minutes on a Windows host, which is why it is a mode and never a
signal, refuses `--check`, `--offenders` and `--delta`, and is on no bar and no card. Two biases are
known: a fix not called `fix` is missed, and blame credits moved code to its mover. The caveat line it
always prints is the rule: a difference between two months of one repository is not evidence of an
effect, so it prints no comparison.

## What "landed" is measured against — the base ladder

Every ancestry answer, every `git show <base>:<path>` a ratchet reads and the trace walk are
measured against ONE ref, and the report prints it on its header line with the commit it resolved
to: `(base refs/remotes/origin/main @ 1a2b3c4d)`. It is resolved remote-first:

1. `--base-ref <ref>`, verbatim. The escape hatch for every rung below.
2. The default branch's NAME: `GOV_DEFAULT_BRANCH`, else the last component of
   `refs/remotes/origin/HEAD`, else a refusal (exit 2) naming both and `git remote set-head origin -a`.
3. `refs/remotes/origin/<name>`, whenever it resolves.
4. A clone with **no `origin` remote** compares against `refs/heads/<name>` and says so on stderr.
   There is no staler or fresher copy of the branch in such a clone, so local is the record.
5. A clone that **has `origin` but no tracking ref** for the branch refuses with exit 2 and names
   `git fetch origin <name>`. Falling back to local there is the defect this ladder removes.

The base used to be the bare branch name, which git resolves to the LOCAL branch, so the same commit
read differently on a node whose local `main` was stale: a pin raise already on origin read as a
weakened ratchet on that node alone. The report never fetches — it is a leg that must run offline,
and a fetch would move the ref it is grading — so a node wanting a fresher answer fetches first.
TOOL-dDerivedDocket-21. A CI checkout that fetches branches without
`refs/remotes/origin/HEAD` still needs `GOV_DEFAULT_BRANCH`, as before.

## Why pins rather than a perfect oracle

The spec-status oracle has one residual false-positive mode it cannot cheaply discriminate: an id
cited as a **forward** reference ("TODO: see FOO-1") reads identically to one citing shipped work. And
`INPROGRESS` is arguably true of a built-but-unmerged unit.

Chasing a perfect oracle is the expensive way to be wrong. A shrink-only pin drains the population
without needing one, and it is the idiom these repos already use for exactly this. Lower a pin as its
population drops; raising one needs the same justification as any other ratchet raise.

**A pin bounds a count, not the offenders it counts.** When one pinned offender drains and a new one
arrives in the same change, the value does not move and `--check` stays green over a regression. So
a gateable signal whose detail rows each carry an `id` takes an id set in `BASELINES` instead: a row
whose `id` the set does not list reds as `new`, a listed id no row carries reds as `stale` until its
line is deleted, and the set may never gain an id against the base, nor be first seeded above the
pin the base held. There is no escape for an addition: each such signal has a remedy that is not
one. Nor is moving a signal out of the set an escape: a signal leaving `BASELINES` for `PINS` is
pinned no higher than the size of the set the base held, or `--check` reds it as a weakened ratchet.
A signal named in both `PINS` and `BASELINES`, or a `BASELINES` key naming no gateable signal,
is refused with exit 2. Signals that never gate keep their pins, because a set would change nothing
`--check` does. The project layer is never evidence for signal 2, so listing an id does not cite it.

## Oracles are tightened against FIELD false positives, never speculatively

Both corrections in this kit's history came from a real misjudged row, and both are recorded at the
code:

- Keying the spec signal on the **slug** over-flagged 107 of 126 — one shipped unit made all 14
  siblings of its multi-spec build look stale. The **seq** is the discriminator.
- Including a `scripts/` tree let an **id catalog** (a recall alias file listing every id in the
  corpus) certify all 110 specs. Product source only; a record certified by an index of records is
  circular.
- The ledger signal flagged a row whose only sha was a **parity comparison baseline**
  ("byte-identical vs `X`"). The reference-sha exclusion now covers `vs|against|compared to|relative
  to` as well as `off|base`.
- This repo's own first `HANDKEPT` probe compared charter **bullets** (12) to **legs** (19) — numbers
  that should never be equal, so it was permanently red. Comparing leg **names** gives a predicate
  that can legitimately reach zero.

Widen an exclusion when a real row is misjudged. Never pre-emptively: every term costs detection power.

## Known portability trap

`selftest.py` compares the Python conf parser against a shell sourcing the same file. On Windows a
bare `bash` resolves to the **WSL** shim ahead of MSYS on PATH, and it cannot source a Windows temp
path the same way — so the comparison fails on an interpreter mismatch rather than on real parser
drift. The selftest therefore **resolves** a working POSIX shell by probing candidates, and if none
works it prints `SKIP` and tallies it. It never prints `ok` for an arm that did not run.

## Tiers

| Tier | Cost | Answers |
|---|---|---|
| 0 | seconds, 0 agents | Are the records still true? Which pins moved? |
| 1 | ~20 min, one bounded wave | Why did a signal move? Is an instrument blind? |
| 2 | hours, ~22 agents | Dead / unwired / duplicated code, and everything above |

In the founding audit, **Tier 0 alone produced the blocker, the vacuous-metric lead and the entire
work-state answer.** The 22 agents deepened those and added the code findings; they did not originate
the most consequential ones. Run Tier 0 first, always. The rendered Skill carries the eight harness
invariants for the agent tiers — read those before any Tier 1 or 2 run.
