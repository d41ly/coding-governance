# TOOL-aFrugalTurnstile-4 — lineage reuse: after a red, the boundary's full bar re-runs only failed and moved legs, and may stamp

**Status:** CLOSED · rev-2 · 2026-10-10 · node a · Tier-2 · base bef97330 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md](../build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-build-TOOL-aFrugalTurnstile-4-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aFrugalTurnstile-4-1-acceptance-ledger.md) | journal | — |
| [2026-10-10-build-TOOL-aFrugalTurnstile-1-2-measurement.md](../build/2026-10-10-build-TOOL-aFrugalTurnstile-1-2-measurement.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-11 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |

<!-- /gen:spec-records -->

## 1. Goal

After a red full bar at the push boundary, the next full bar re-runs only the legs that failed and
the legs whose input key moved, reuses the rest from the earlier run's own ledger rows, and may
still stamp `gate-full-green`. This implements design D5 (prompt item B): today a one-line fix after
a red costs a whole bar again, because `.githooks/pre-push` never sets `GATE_REUSE` and a reusing
run cannot stamp.

## 2. Scope (IN)

- **S1** — The ledger row grows four trailing fields after `ended-at`, in this order: `run` (the
  run id), `full` (`1` when the run had `GATE_FULL` set and `TREE_CLEAN=yes`, else empty),
  `manifest_blob` (the blob of `LEGS_FILE` this run read) and `head` (the sha graded). A retried
  row and a red row carry the same four fields. Observed by AC1.
- **S2** — `GATE_REUSE=lineage` is a new value of the existing knob. Under it a leg is reused only
  when every term the block checks today holds AND the row's `full` is `1`, its `manifest_blob`
  equals this run's, and its `head` is an ancestor of HEAD. Any other non-empty value keeps
  today's meaning. Observed by AC2, AC3, AC4, AC5, AC6 and AC7.
- **S3** — The full-green stamp's "reused nothing" precondition becomes "every reuse was
  lineage-qualified", counted by a new counter beside `reuses`. The stamp always records
  `reused <n>`. `GATE_REUSE=1` still forbids the stamp. The inherited-green stamp keeps its
  `reuses = 0` precondition unchanged. Observed by AC2, AC6 and AC7.
- **S4** — The runner reads `GATE_REUSE` once into a variable, records it as a header key `reuse`,
  and unsets it before any leg starts, the way it already treats `GATE_RUN_ID`. A leg's nested
  runner never inherits a reuse mode. Observed by AC8.
- **S5** — The reuse block reads `gate-ledger.tsv` in ONE pass with bash `read`, in place of one
  `grep` spawn per leg, for both reuse modes. Observed by AC10.
- **S6** — Lineage terms are checked cheapest first, and `input_key` is computed only for a leg
  whose row passed them. Ancestry is asked once per distinct `head` value and memoized in a
  string. A row whose run's header (`<git-dir>/gate-run/<run>/header`, read with bash `read`)
  names a `base` different from this run's `BASE` is refused before its key is computed, because
  `input_key` hashes `BASE` and so cannot match. A missing header, or a `run` value outside
  `[A-Za-z0-9TZ-]`, falls back to computing the key. Observed by AC10.
- **S7** — `.githooks/pre-push` keeps scrubbing an inherited `GATE_REUSE` through
  `BAR_SCRUBBED_KNOBS`, and on a FULL decision with `bar_record=runner` exports
  `GATE_REUSE=lineage` itself. The FULL decision line then ends with the clause
  ` — reuse: lineage`. No other bar class gets the export or the clause. Observed by AC11, AC12
  and AC13.
- **S8** — The text. The README's "Reuse, and the baseline a guard diffs against" section is
  rewritten for both modes, not appended to. The runner's ledger comment states the nine-field
  row. The reuse block and the README carry the not-checked sentence in §4. Observed by AC14.
- **S9** — The existing suite arms this changes are re-staged: the evidence suite's AC6
  five-field assertion becomes nine fields, and `.githooks/pre-push.test.sh` H49's `GATE_REUSE`
  arm is re-staged so its earning run is not lineage-qualifying (§4). Observed by AC1 and AC13.

## 3. Non-goals (OUT)

- Changing what `GATE_REUSE=1` does, or making reuse the default anywhere outside the boundary's
  own FULL decision.
- Sharing a ledger across worktrees. The ledger is per git dir, so a run worktree's close bar
  feeds lineage only to a push made from that same worktree; the primary tree's push reads its
  own ledger. Cross-tree cover of the close bar is design D4, not this unit.
- Letting the inherited-green stamp rest on reused legs. A lineage run that reuses anything writes
  no inherited green, which costs a later saving and never a verdict, because the landing under
  `INHERITED_RED=land` reads the run record, not that stamp.
- Re-keying `input_key` (adding a field, or taking `BASE` out of it). Its `BASE` term is what bounds a lineage
  chain to one remote base; see §4.
- Exporting the mode to a bar that is not this kit's runner. A wrapper bar such as inCMS's
  `scripts/gate.sh` gets lineage only if its own tracked script passes the mode to the runner it
  calls; nothing in the hook reaches it.
- The post-merge script (TOOL-aFrugalTurnstile-6) is not written here; the handoff below is what it
  must do about this knob.

### Edges

- **hands-off** `TOOL-aFrugalTurnstile-6` — its post-merge full bar must run with `GATE_REUSE`
  unset in the bar's environment, so every leg re-executes there; this unit's not-checked sentence
  names that bar as the run that catches a verdict lineage carried forward.
- **hands-off** external — an adopter whose bar wraps the runner (inCMS `scripts/gov-bar.sh`) decides
  in its own tracked script whether to pass `GATE_REUSE=lineage` to the nested runner.

## 4. Design

**The decision implemented.** Design D5, as written. D5's sentence says "three fields" and then
names four (`run`, `full`, `manifest_blob`, `head`); the brief says four. The named list governs,
so the row is nine fields.

**Why the four terms are enough to call the stamp a full green.** A lineage-reused verdict was
produced by a run that set `GATE_FULL` on a clean tree (`full 1`), read the same manifest blob,
graded an ancestor of HEAD, and computed the same `input_key` — which hashes the leg's argv, the
run's `BASE` and the leg's guard composition (`git ls-files -s` over its guard paths plus their
porcelain lines), or the whole-tree fingerprint for an unguarded leg. The `BASE` term matters: under
a FULL decision the hook exports no `GATE_BASE`, so the runner's `BASE` is the merge-base with the
remote tip, which a refused push does not move. A red push and its fix push therefore share a
`BASE`, and a landing by any node between them moves it and voids every key. That bounds a reuse
chain to one remote base, which is the "same base lineage" of the prompt.

**Supersedes a recorded boundary rule, on the owner's instruction.** `TOOL-aPacedTurnstile-6` §4
ruled that an advisory input may cause less work only on an opt-in, non-authoritative run, which is
why the boundary never reused. Prompt item B and design D5 reverse that for one case: the
boundary's own FULL decision for a runner bar. The ledger is in the git dir, the same trust domain
as `gate-full-green`, so a hostile ledger row grants nothing a hostile stamp does not already grant.

**Not-checked sentence**, added to the reuse block's comment and to the README section, verbatim:

> WHAT LINEAGE REUSE DOES NOT CHECK: that a reused leg's guard names every input the leg reads, or
> that its verdict depends on the tree alone. A reused verdict is only as good as its input key, so
> a too-narrow guard or an undeclared `impure` leg is carried forward until its key moves, the
> remote base moves, or a run without `GATE_REUSE` re-executes it — the post-merge full bar is that
> run.

**Ceiling on the saving.** An unguarded leg is keyed on the whole-tree fingerprint, so any fix
re-runs every unguarded leg. PINNED at base `bef97330` from `tools/gate-legs.json`: 61 of 128 legs
carry no guard and 3 are `impure`. The saving is the guarded legs a fix does not touch, at most 64
of 128. It re-derives with
`python -c "import json; d=json.load(open('tools/gate-legs.json')); print(len(d), sum(1 for r in d if not r.get('guard')))"`.

### Data model

Ledger row, tab-separated, one per leg, at `<git-dir>/gate-ledger.tsv`:

```
name  seconds  status  key  ended-at  run  full  manifest_blob  head
```

Rows a run did not measure (guard-skipped, held, reused) are carried forward unchanged by the
existing awk merge, so a reused leg keeps the `run` and `head` of the run that executed it. A
five-field row (written before this unit) has an empty `full` and is never lineage-reusable; it is
still reusable under `GATE_REUSE=1` as today.

Header key `reuse`, value `lineage`, `1`-or-other as given, or empty. It sits outside the
run-envelope block, beside `queued`, for the reason the comments there give.

Stamp key `reused`, the count of reused legs, always written (`0` when none). No reader of
`gate-full-green` in `.githooks/pre-push` reads it; it is evidence.

### Inventory

No function is minted in the runner or the hook: the lineage branch is inline in the existing reuse
block. The suite arms of §7 mint eight helpers (rev-2), each leading with a declared verb, and
`memory/map/generated/symbols.json` is regenerated for them: `build_lin_repo`, `write_lin_fix`,
`read_lin_header`, `read_lin_stamp` and `check_lin_control` in the evidence suite; `run_lin_push`,
`read_lin_token` and `read_lin_reused` in `.githooks/pre-push.test.sh`. No new `GATE_`/`GOV_` knob is
minted: `lineage` is a value of `GATE_REUSE`, the runner reads it once as `${GATE_REUSE:-}` exactly
as before, and the `unset GATE_REUSE` spells no `$`, so H49's knob-class arm keeps its count. New
shell variables in the runner: `REUSE_MODE`, `lineage_reuses`, `MANIFEST_BLOB` (hoisted from the
header so the header, the rows and the stamp read one value), `HEAD_SHA`, the ledger block's
`lfull`, and the reuse block's temporaries `_lrow` and `_rbase` (associative arrays, unset after the
block), `_anc_yes` and `_anc_no` (the ancestry memo strings) and the `_`-prefixed row fields. The
hook gains `_reuse_clause`.

### Insertion points (read at base `bef97330`)

| Site | Line | Change |
|---|---|---|
| runner header block | `tools/run-gates/run-gates.sh` 2224-2275 | `manifest_blob` reads `MANIFEST_BLOB`; add `reuse` beside `queued` |
| reuse block | 2280-2304 | one-pass ledger read; the `lineage` branch with S6's order; `lineage_reuses` counted |
| reuse verdict print | 2596-2599 | unchanged bytes: `GATE reuse <leg>  (proven green, inputs unchanged)` |
| ledger write | 3636-3685 | comment names nine fields; `printf` gains `run full manifest_blob head` |
| stamp preconditions | 3805-3883 | `[ "$reuses" = 0 ]` becomes `[ "$reuses" = "$lineage_reuses" ]` for `gate-full-green` only; `reused` written |
| inherited-green stamp | 3926-3931 | untouched |
| hook scrub | `.githooks/pre-push` 1421 | untouched, `GATE_REUSE` stays scrubbed |
| hook FULL branch | 1460-1463 | after `export GATE_FULL=1`: `[ "$bar_record" = runner ] && export GATE_REUSE=lineage`, and the line's ` — reuse: lineage` clause |

`GATE_REUSE` is unset right after it is read, beside `unset GATE_RUN_ID` (~1937).

### The H49 arm, re-staged

H49's `GATE_REUSE` arm earns a green ledger row with a direct full run whose leg reads
`H49_LEG_RC=0`, then pushes with `H49_LEG_RC=1`. Under this unit the hook's own `lineage` export
would reuse that row, because the leg's verdict depends on the environment, which no key sees. That
is the not-checked class above, staged on purpose. The arm keeps testing what it names — an
inherited `GATE_REUSE` is not honoured — by earning its row WITHOUT the full flag, so the row's
`full` is empty: `GATE_REUSE=1` semantics would reuse it, lineage refuses it, and the red leg runs.

### Readers of the ledger, checked at base

| Reader | Reads | Nine fields |
|---|---|---|
| runner dispatch parser (`run-gates.sh` ~2001) | `split("\t")`, `len(p) >= 2`, field 2 | tolerated |
| `tools/run-gates/profile_bar.py` `read_timings` | `len(parts) >= 2`, field 2 | tolerated |
| `tools/run-gates/derive-ceilings.py` | reads `gate-run`, not the ledger (its docstring, line 14) | not a reader |
| the reuse block's own `read -r _n _sec _st _key _end` | `_end` absorbed the tail | rewritten by S5 |
| `run-gates.evidence.test.sh` 414, 419; `run-gates.test.sh` 885, 1309, 1529, 1573, 2868, 2915 | fields 1-4 by number | tolerated |
| `run-gates.evidence.test.sh` 699 | `NF != 5` | re-staged by S9 |

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/README.md`
- `tools/run-gates/run-gates.evidence.test.sh`
- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`

### Alternatives rejected

- **A dedicated resume file naming the failed legs.** Rejected for the reason `TOOL-aPacedTurnstile-6`
  gave: a second mechanism for what the key already decides, with its own staleness rule.
- **Bounding the chain to the immediately previous run only.** Considered: a leg reused twice in a
  row would then re-run. Not taken: the `BASE` term already bounds a chain to one remote base, and a
  run-count bound would need D5 changed. Recorded here so a reviewer weighing it starts from the
  measurement above.
- **Exporting lineage from the unattended close.** Not this unit: design D11 gives the close
  `GATE_FULL=1`, and the close is graded by its own decision.

## 5. Production-readiness checklist

- security — The ledger becomes an input to an authoritative run. It lives in the git dir beside
  `gate-full-green`, which a writer there can already forge outright, so the trust domain is not
  widened. A `run` value is shape-checked before it names a header path, so a row cannot steer a
  read outside `gate-run/`.
- perf / scale — The new work is one ledger read in bash, one `git merge-base --is-ancestor` per
  distinct row `head`, and `input_key` only for rows passing the cheap terms and the base filter.
  S5 also saves one `grep` spawn per leg that the opt-in mode paid. Measured at VERIFYING, not here.
- error / empty / loading states — An absent, empty or corrupt ledger reuses nothing; a five-field
  row is not lineage-qualified; an unreadable header computes the key; every failure is "did more
  work".
- observability — Reused legs print the existing `GATE reuse` line; the verdict line keeps its
  `(N reused)` note; the header records `reuse`, the stamp `reused`, and the hook's FULL line names
  the mode.
- risks — The not-checked sentence in §4. A leg whose verdict depends on the environment and is not
  declared `impure` is reused at the boundary; H49 stages exactly that.
- testing — Scratch fixtures driving a copy of the runner and of the hook, base copy first; suite
  arms added under §7 run at VERIFYING.
- migration — Additive. Old five-field rows read as not lineage-qualifying; readers select by field
  number and tolerate the tail.
- user docs — The README reuse section, rewritten (S8).

## 6. Acceptance criteria

Every fixture criterion runs twice: first against the base runner and hook (`git show
bef97330:<path>` copied into the fixture), where the `Red when` behaviour is observed, then against
the edited files. Fixtures live under the session scratch; a fixture clone that hits the path limit
goes under a short `%TEMP%` name. The three-leg fixture is `ru_repo`'s shape from the evidence suite
plus one unguarded leg: leg `pa` guarded on `ga/`, leg `pb` guarded on `gb/` and red until fixed,
leg `pu` unguarded, a seed commit, and `refs/remotes/origin/main` at the seed.

- **AC1** — When a fixture bar runs with the full-bar flag on a clean tree, every
  `gate-ledger.tsv` row has nine tab-separated fields, field 6 equals the header's `run_id`,
  field 7 is `1`, field 8 equals the header's `manifest_blob`, and field 9 equals
  `git rev-parse HEAD`; run again with an untracked file present, field 7 is empty. Checked with
  `awk -F'\t' 'NF != 9'` printing nothing.
  Red when: the base runner writes five-field rows.
- **AC2** — When the fixture's first full run has `pb` red, `gb/` is fixed in a new commit, and a
  second full run sets `GATE_REUSE=lineage`, the output prints `GATE reuse pa`, `GATE ok    pb` and
  `GATE ok    pu`, and `gate-full-green` exists carrying `reused` `1`.
  Red when: the base runner reuses `pa` but writes no stamp.
- **AC3** — When the first run is NOT full (no full-bar flag, over a commit touching `ga/` and `gb/`
  so every leg executes) and the second sets `GATE_REUSE=lineage`, no `GATE reuse` line prints;
  in the same state under `GATE_REUSE=1`, `GATE reuse pa` prints (the control proving the key
  matched).
  Red when: the base runner reuses `pa` from a row with an empty `full`.
- **AC4** — When the manifest gains a fourth leg between the runs, a `GATE_REUSE=lineage` run
  prints no `GATE reuse` line, and the `GATE_REUSE=1` control prints `GATE reuse pa`.
  Red when: a row earned on another manifest blob is reused.
- **AC5** — When the tree is reset to a sibling of the first run's head (same `ga/` bytes, `gb/`
  fixed), a `GATE_REUSE=lineage` run prints no `GATE reuse` line, and the `GATE_REUSE=1` control
  prints `GATE reuse pa`.
  Red when: a row whose `head` is not an ancestor of HEAD is reused.
- **AC6** — When lineage-qualifying rows exist and the run sets `GATE_REUSE=1`, `GATE reuse pa`
  prints and `gate-full-green` (deleted before the run) is absent afterwards.
  Red when: the opt-in mode stamps.
- **AC7** — When `pa` is declared `impure` and a full green run is followed by a
  `GATE_REUSE=lineage` run on the unchanged tree, `GATE ok    pa` prints, `GATE reuse pb` and
  `GATE reuse pu` print, and `gate-full-green` carries `reused` `2`.
  Red when: an impure leg is reused, or the run cannot stamp.
- **AC8** — When a fixture leg writes `${GATE_REUSE-unset}` to a file and the run sets
  `GATE_REUSE=lineage`, the file reads `unset` and the run's `header` carries `reuse` `lineage`.
  Red when: the base runner leaks the mode into every leg.
- **AC9** — When a nine-field ledger gives `pb` the largest seconds, the next run's header
  `dispatch` key lists `pb`'s index first, and
  `python -c "import sys; sys.path.insert(0, 'tools/run-gates'); import profile_bar; print(profile_bar.read_timings(sys.argv[1]))" <ledger>`
  prints all three durations.
  Red when: either reader rejects or misreads a nine-field row.
- **AC10** — With a PATH shim logging every `git` and `grep` argv, a `GATE_REUSE=lineage` run logs
  no `grep` whose arguments name `gate-ledger.tsv`; and after `refs/remotes/origin/main` is moved
  between the runs, the lineage run logs no more `hash-object --stdin` calls than a run with
  `GATE_REUSE` unset, while the unmoved-base control logs more.
  Red when: the base runner greps the ledger once per leg, or keys are computed for rows of another
  base.
  cost: two extra fixture runs.
- **AC11** — When a scratch clone with the hook and a runner copy pushes a tip whose `pb` is red
  (refused, token `gate-red`), then fixes `gb/` and pushes again, the second push's FULL line ends
  `— reuse: lineage`, its output carries `GATE reuse pa`, the push lands, and `gate-full-green`
  carries `reused` `1`.
  Red when: the base hook's second push runs all three legs.
- **AC12** — When the same push runs with the declared STUB bar (`GOV_GATE_CMD_TEST`), its FULL line
  carries no `reuse: lineage`; when `GOV_GATE_CMD` names a tracked non-runner script that writes
  `${GATE_REUSE-unset}`, that file reads `unset`; and when the runner bar is pushed with
  `GATE_REUSE=1` inherited, the `not honoured from the environment by this bar` line still names
  `GATE_REUSE` and the FULL line still ends `— reuse: lineage`.
  Red when: any bar other than the runner receives the mode, or the inherited value survives.
- **AC13** — When the H49 shape earns its green row with a direct run WITHOUT the full-bar flag and
  the push sets `GATE_REUSE=1` with the leg red, the push is refused with token `gate-red`.
  Red when: lineage accepts a row with an empty `full`.
- **AC14** — When `grep -n "WHAT LINEAGE REUSE DOES NOT CHECK" tools/run-gates/README.md` runs it
  prints one line, and the same grep over the runner prints one line;
  `grep -n "never sets it" tools/run-gates/README.md` prints nothing.
  Red when: the README still says the boundary never reuses, or the sentence is missing.

## 7. Gates

`run-gates canary` · `run-gates evidence` · `pre-push self-test` · `pre-push run-log line` · `profile-bar selftest` · `run-gates wiring` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · the reuse scratch extended with an unguarded leg, a red `gb/` leg and its fix commit; AC6's five-field line moved to nine · none
New arm: .githooks/pre-push.test.sh · covers AC11 AC12 AC13 · H49's `GATE_REUSE` arm re-staged on a row with an empty `full`, plus a lineage push after a red · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-10 · build pass. §4 Inventory: "no function is minted" held for the runner and
  the hook only; the §7 arms mint eight suite helpers, now named there with the symbols.json regen
  they owe, and the runner's temporaries are listed beside its four named variables. No criterion
  changed.

## 10. Reuse audit

The seam is the existing opt-in reuse block and `input_key` in `tools/run-gates/run-gates.sh`
(2196-2304), extended in place with a `lineage` branch; the ledger write (3636-3685) and the stamp
block (3862-3913) are extended, not paralleled. Found by reading those files: two
`tools/codebase-map/reuse_lookup.py` probes ("reuse a leg verdict proven green by an earlier full run
when its input key is unchanged" and "input key for a gate leg ledger row") ranked only name-stem
neighbours (`key`, `legs`, `rows`) and named neither block, so no existing seam outside the runner
fits. The recall query returned the design record, the brief and `TOOL-aPacedTurnstile-6`, whose
boundary rule this unit supersedes (§4).

Recall terms used: `python tools/memory-recall/query.py "how does the runner reuse a proven green leg and why can a reusing run not stamp the full green" --terms "GATE_REUSE reuse ledger input_key gate-full-green stamp impure full-green precondition pre-push boundary authoritative"`
