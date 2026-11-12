# TOOL-aNimbleMend-2 — the pass-leg declaration: a `pass_leg` field on a leg's row, written by a derivation over the bar run log and the ceiling evidence

**Status:** CLOSED · rev-2 · 2026-11-12 · node a · Tier-2 · base 97e0841d · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md) | research | TOOL-aNimbleMend-1 TOOL-aNimbleMend-3 TOOL-aNimbleMend-4 TOOL-aNimbleMend-5 TOOL-aNimbleMend-6 TOOL-aNimbleMend-7 TOOL-aNimbleMend-8 TOOL-aNimbleMend-9 TOOL-aNimbleMend-10 TOOL-aNimbleMend-11 TOOL-aNimbleMend-12 |
| [2026-11-12-prompt-TOOL-aNimbleMend-2-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-2-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The legs a unit pass runs are declared once, as a field on each leg's own row of the leg manifest,
and no hand writes that field: one derivation ranks every leg by recorded reds per evidenced second
and fills a 600 s budget. The rule is recorded where the derivation lives, its inputs are tracked,
and the declaration is re-applied at every landing, so the list cannot drift from its evidence.

## 2. Scope (IN)

- **S1** — `tools/run-gates/pass_legs.py`, holding the rule as `derive_pass_legs`, the exclusion
  predicate `check_pass_eligible`, and the constants `PASS_BUDGET_SECONDS` and
  `PASS_LEG_CAP_SECONDS`. Observed by AC1, AC2 and AC3.
- **S2** — Its `--write` verb, which distils this node's bar run log and gate ledgers into the
  tracked `tools/run-gates/pass-leg-evidence.txt` and then applies. Observed by AC1, AC6 and AC7.
- **S3** — Its `--apply` and `--check` verbs over tracked files alone: `--apply` writes
  `"pass_leg": true` onto each selected row of the manifest and leaves no other row carrying it,
  and `--check` reds a manifest that differs from that. Observed by AC4, AC5 and AC9.
- **S4** — Its `--report` verb, one line per leg with reds, cost, score and verdict. Observed by
  AC2 and AC3.
- **S5** — One staged `[[regenerate]]` row in `tools/run-gates/kit.toml` naming `--apply` and
  `--check`, and one `project-owned` rule withholding the evidence file from installs. Observed by
  AC10.
- **S6** — `pass_leg` added to both pinned key sets of the manifest canary in
  `tools/run-gates/run-gates.test.sh`. Observed by AC8.
- **S7** — Gov's first evidence file and the fields it derives in `tools/gate-legs.json`, written
  by `--write` on node `a` and committed. Observed by AC11.
- **S8** — A section of `tools/run-gates/README.md` stating the field, the rule, the four verbs and
  the evidence file, and a row for `pass_legs.py` in its pieces table. Observed by AC12.

## 3. Non-goals (OUT)

- The budget gate. That a declared list sums to 600 s at most, reds past 690 s, holds no leg over
  the cap and no excluded class is `TOOL-aNimbleMend-3`'s gate. This unit's rule produces such a
  list, and that unit refuses one that is not.
- Any new leg. The scoped forms of memory hygiene and the spec-token check, and pinned facts and
  positional as legs, are `TOOL-aNimbleMend-4`'s. A leg with no bar history has no recorded red, so
  this rule never selects it: how such a leg enters the evidence is that unit's to state.
- Running a declared leg, and reading `pass.fast-legs`. The declaration is data, and the runner
  that asks the switch is `TOOL-aNimbleMend-5`'s.
- Any change to `tools/run-gates/ceiling-evidence.txt`, to a `ceiling`, or to
  `tools/run-gates/derive-ceilings.py`. A new evidence row there can red a ceiling beside it.
- Carrying the field through the deployer. `tools/govkit/govkit.py` rebuilds a row it owns from
  its descriptor, so an update drops the field from that row and the staged row of S5 re-applies it.
- A `[[gate_leg]]` descriptor key. Gov's reds are gov's, and seeding an adopter's manifest with
  them is the class `memory/gotchas/pin-copied-from-another-corpus.md` names.
- A kit version bump. The lander's `mint` moves every version once, after the last unit.

### Edges

- **hands-off** `TOOL-aNimbleMend-3` — its gate reads the pass-leg field, the budget and cap constants and the exclusion predicate from this unit's module, and owns the 690 s tolerance
- **hands-off** `TOOL-aNimbleMend-4` — its new legs carry no bar history, so it states how each enters the pass-leg evidence before this rule can select it
- **hands-off** `TOOL-aNimbleMend-5` — the adapter takes its list from the rows carrying the pass-leg field, and never from a list of its own
- **hands-off** `TOOL-aNimbleMend-11` — the pass-leg help page names the field, the rule and the write verb
- **hands-off** `TOOL-aNimbleMend-12` — observes a declared list in a scratch adopter, which holds no evidence until that adopter runs the write verb
- **consumes-from** external — a bar run log on the node that runs the write verb; a node that has run no bar derives nothing, and says so

## 4. Design

### Where the inputs are, and what the prompt calls them

The owner's prompt says "the gate ledger". Three stores hold what it means, and only one of them
holds red history.

| Store | Holds | Tracked | Read here for |
|---|---|---|---|
| `<git-common-dir>/runlog/gates.log` | one line per bar, its failing legs as `fail.1` to `fail.20` | no | the red count |
| `<git-dir>/gate-ledger.tsv` | one row per leg: the last seconds and status, no history | no | the last seconds |
| `tools/run-gates/ceiling-evidence.txt` | the evidenced maximum seconds per leg | yes | the cost |

`tools/run-gates/run-gates.sh#write_runlog_verdict` writes the first, and
`tools/run-gates/README.md`, "The run record", states the other two. The module docstring of
`tools/run-gates/derive-ceilings.py` records why the ledger carries no history. The first two are
node-local, so `--write` distils them into a tracked file and every other verb reads tracked files
only, which is the shape `derive-ceilings.py` already has.

### The evidence file

`tools/run-gates/pass-leg-evidence.txt`, generated by `--write`, never hand-edited, LF, tab-separated:

```
# window	<bars read>	<first bar's started>	<last bar's started>	<node>	<date>
<leg>	<reds>	<last seconds, or ->
```

- **reds** — the number of `p=gates`, `ev=once` lines whose `fail.<n>` fields name the leg. A leg
  named twice on one line counts once. A line's `fail_more` count names no leg and adds nothing.
- **last seconds** — field 2 of the leg's ledger row. Ledger rows are read from `<git-dir>` and
  from `<git-common-dir>`, and the row with the later `ended-at`, field 5, wins. A linked worktree
  has run no bar of its own, and the common directory's ledger is the primary checkout's.
- One row per manifest leg with at least one red. A failing name the manifest no longer carries is
  dropped, and the summary line counts those.
- The node is `GOV_NODE`, refused when unset, as `--observed` refuses it in `derive-ceilings.py`.
- A write replaces every row. The file is one node's window and is not monotone.

A run log that is absent, or holds no bar line, is a DEAD PROBE: `--write` exits 1 naming the path
and leaves the evidence file and the manifest as they were.

### The rule

`derive_pass_legs(legs, reds, ceilings)` returns each leg's verdict. It reads the manifest rows,
the evidence file and the ceiling evidence, and nothing else.

1. **Cost.** A leg's cost is its maximum in `ceiling-evidence.txt`. That is the figure
   `TOOL-aNimbleMend-3` sums, so the budget this rule fills is the budget that gate reads.
2. **Excluded.** `check_pass_eligible` gives the first reason that fits, in this order:

   | Reason | The leg |
   |---|---|
   | `selftest` | has `chunk` `selftests` |
   | `e2e` | has `chunk` `e2e` |
   | `unattended-gate` | has an `argv` word ending `check-unattended.sh` |
   | `no-red` | has no row in the evidence file |
   | `unevidenced` | has no row in the ceiling evidence, so its cost is unknown |
   | `over-cap` | has a cost, or a last seconds, above `PASS_LEG_CAP_SECONDS` |

3. **Score.** `reds / max(cost, 1.0)`. The one-second floor keeps a sub-second leg from outranking
   every other by division.
4. **Order.** Score descending, then cost ascending, then name.
5. **Fill.** Walk the order with a running sum of cost. A leg is `selected` when the sum with its
   cost stays at or under `PASS_BUDGET_SECONDS`, which is 600. Otherwise it is `over-budget`, and
   the walk goes on, so a cheaper leg further down still enters.

The unattended kit gate is found by its script and not by its leg name, so a renamed row stays
excluded. The last-seconds half of `over-cap` exists because ceiling evidence can be stale low:
PINNED, measured 2026-11-12 on node `a`, the ceiling evidence holds `memory hygiene` at 86.8 s from
2026-09-24 while the primary checkout's ledger holds its last run at 632.7 s.

The rule counts every recorded red, an inherited one included. The run log does not say whose a
red was, and the owner's starting table counts the inherited policy-check reds too.

**What the rule yields at this base.** PINNED, measured 2026-11-12 on node `a` by a read-only
probe of the three stores, with the cap at 120: 202 bars, 117 of them red, 78 legs with a red, 124
of 171 legs with a ceiling-evidence row. Excluded: 29 `selftest`, 1 `unattended-gate`, 15
`unevidenced`, 7 `over-cap`. Selected: 26 legs summing 412.8 s. The seven over the cap are
`memory hygiene`, `brief-recorded`, `pass-order history`, `spec tokens (a spec's own names resolve)`,
`govkit acceptance matrix`, `routed commits name a specced unit` and `tags (the resolver's checks)`.
The fifteen `unevidenced` legs, `policy check` and `instruction edits (manifest checks)` among them,
enter when a routine `derive-ceilings.py --write` gives them a row. S7's commit is whatever
`--write` derives on the day, and these figures are not its acceptance.

### The field, and the two tracked verbs

`"pass_leg": true` on a row declares it. An undeclared row carries no such key, as an unguarded row
carries no `guard`.

`--apply` edits the manifest as text, because the file is hand-formatted and a JSON re-dump would
rewrite every row. For each row it removes a `pass_leg` line if one is there, and for a selected
row it inserts the line `    "pass_leg": true,` directly after the row's `"name"` line, which opens
every row. Before writing, it parses the new text and refuses, exit 2 and nothing written, unless
the parse equals the old parse with only `pass_leg` keys differing. It writes LF bytes, and only
when they differ.

`--check` exits 0 when the manifest's bytes equal what `--apply` would write, printing
`pass-legs: <n> declared, <sum>s of 600s`. It exits 1 naming each leg that carries a field the rule
does not give it, and each selected leg that lacks one. With no evidence file the rule selects
nothing, so `--apply` writes nothing, `--check` is green over a manifest with no field and prints
`pass-legs: not derived, no evidence file`, and a field typed by hand is still a finding.

The manifest is found as `derive-ceilings.py#read_legs` finds it: `GATE_LEGS`, else the kit
directory's sibling. An evidence row naming a leg the manifest no longer carries is reported on
stderr and fails nothing.

### The staged row

```toml
[[regenerate]]
argv = ["python", "{kit}/pass_legs.py", "--apply"]
check = ["python", "{kit}/pass_legs.py", "--check"]
stage = 2
writes = ["the pass_leg field of the leg manifest"]
```

`tools/run-gates/regen.py#build_items` makes a staged `[[regenerate]]` row an item, so the lander
re-applies the field over each merged tree and every bar's preflight proves it fresh before it
queues. A ceiling-evidence refresh that moves the selection is therefore cured by the landing, or
by one `--regen`, and is never a leg's red. A `[[generated]]` row is not used: the unattended kit
enrols every `[[generated]]` path as a generated index (`tools/unattended/lib-unattended.sh#resolve_generated_indexes`),
and the manifest is an authored file that later units add legs to.

Stage 2, because the field reads no other generated output and the codebase map at stage 3 reads
the tree after it. UNVERIFIED: that govkit's own run of a `[[regenerate]]` argv resolves a leading
`python` token as `regen.py` does. If it does not, the row's argv becomes the kit's shell entry.

The evidence file is gov's own, as the ceiling evidence is, so `tools/run-gates/kit.toml` withholds
it with a `project-owned` rule beside the one for `ceiling-evidence.txt`. The tool ships.

### The canary

`tools/run-gates/run-gates.test.sh` pins the manifest's key set in two `KNOWN` literals, and a row
carrying any other key reds the `run-gates canary` leg. Both gain `"pass_leg"`. A search of the
tool tree for `KNOWN` and `unknown key` finds no other reader that refuses a manifest key.

### Inventory

| Minted | Cell | Graded by |
|---|---|---|
| `derive_pass_legs`, `check_pass_eligible`, `read_red_counts`, `read_last_seconds`, `render_pass_field` | `py.function` | `lexicon.py --suggest` answered OK for each on 2026-11-12 |
| `PASS_BUDGET_SECONDS`, `PASS_LEG_CAP_SECONDS` | no `py.constant` cell is declared | the upper-snake spelling of `RUNNER_SOURCE` beside them |
| `pass_legs.py` | no `py.file` cell is declared | the snake spelling of `measure_legs.py` and `owed_rows.py`, so a sibling module imports it |
| `pass-leg-evidence.txt` | no file cell is declared | the spelling of `ceiling-evidence.txt` |
| `pass_leg` | a manifest key | the canary's `KNOWN` set, and the snake spelling of `doc_reads` |

### Files touched (estimate)

`tools/run-gates/pass_legs.py`
`tools/run-gates/pass-leg-evidence.txt`
`tools/gate-legs.json`
`tools/run-gates/kit.toml`
`tools/run-gates/run-gates.test.sh`
`tools/run-gates/README.md`

### Alternatives rejected

- **Verbs added to `derive-ceilings.py`.** Its name and its 48 KB are about ceilings, its file name
  cannot be imported, and `TOOL-aNimbleMend-3` and `TOOL-aNimbleMend-5` import the predicate.
- **Reds read from the ledger, as the prompt words it.** The ledger keeps one row per leg and no
  history, so a red count from it is 0 or 1.
- **Reds read from `<git-dir>/gate-run/`.** It retains a handful of runs per worktree. The run log
  holds 202 bars across every worktree of the clone.
- **Seconds taken from the ledger alone.** The budget gate sums the ceiling evidence, and two cost
  figures for one leg is two facts.
- **Fresh ceiling-evidence rows written here for the unevidenced legs.** `policy check` declares a
  120 s ceiling, and any new row for it reds `derive-ceilings.py --check`, which asks 120 s of
  headroom above the reading.
- **The field written by hand and only checked.** The owner's rule is derive, never type.
- **A separate tracked list of pass legs.** The owner rules one declaration, in the manifest.
- **A JSON re-dump of the manifest.** It rewrites every row's bytes and loses the inline `reads`
  objects' layout.

## 5. Production-readiness checklist

- **security** — No write path beyond two tracked files in the tool tree. The run log is read as
  data: a leg name from it is used only as a key compared with manifest names, and never reaches a
  command line.
- **perf / scale** — One pass over a run log of a few hundred lines and two small files. `--check`
  spawns nothing and joins the bar's preflight, which already runs every staged check.
- **error / empty / loading states** — No run log is a DEAD PROBE. No evidence file is the
  not-derived state, green and said. An unset `GOV_NODE` refuses. A manifest that does not parse,
  or an edit that would change more than the field, refuses with nothing written.
- **observability** — `--report` prints every leg's reds, cost, score and verdict, and the window
  line. `--check` prints the declared count and sum.
- **risks** — The selection moves whenever the ceiling evidence moves, and the staged row is what
  keeps that from being a red. Stale-low ceiling evidence can admit a slow leg whose ledger row is
  also absent, and `TOOL-aNimbleMend-5` prints an overrun when one does. A deployer update drops the
  field from the rows it owns until the staged row runs. The run log names at most twenty failing
  legs per bar, so a bar with more undercounts the rest.
- **testing** — Two scratch repositories and direct runs of the four verbs. One moved arm, in §7.
- **migration** — Additive. A manifest with no field is legal, and an adopter with no evidence
  file derives nothing and is told so.
- **user docs** — The kit README section is S8. The help page is `TOOL-aNimbleMend-11`'s.

## 6. Acceptance criteria

`<kit>` is `tools/run-gates`, here and in each fixture. Fixture F is a scratch git repository under
`%TEMP%` with a short name. It holds a copy of this unit's module at `<kit>/pass_legs.py`, a
hand-written and committed `tools/gate-legs.json` and `tools/run-gates/ceiling-evidence.txt`, and,
under its git directory, a hand-written `runlog/gates.log` and `gate-ledger.tsv`. Its eight legs, with the cap at 120:

| Leg | `chunk` | Ceiling evidence | Reds | Ledger seconds | Expected |
|---|---|---|---|---|---|
| `a-cheap` | `product` | 2.0 | 4 | 2.0 | `selected` |
| `b-mid` | `declarations` | 100.0 | 5 | 90.0 | `selected` |
| `c-stale` | `declarations` | 90.0 | 6 | 300.0 | `over-cap` |
| `d-self` | `selftests` | 1.0 | 9 | 1.0 | `selftest` |
| `e-unatt` | `declarations`, its `argv` naming `check-unattended.sh` | 3.0 | 9 | 3.0 | `unattended-gate` |
| `f-nomeas` | `product` | none | 7 | 5.0 | `unevidenced` |
| `g-e2e` | `e2e` | 5.0 | 3 | 5.0 | `e2e` |
| `h-quiet` | `product` | 1.0 | 0 | 1.0 | `no-red` |

Fixture B is the same shape with seven `product` legs, `p1` to `p7`, each with ceiling evidence
100.0 and reds 7 down to 1.

- **AC1** — When `GOV_NODE=f python <kit>/pass_legs.py --write` runs in F, the evidence
  file holds one row per leg but `h-quiet`, with the reds above, and
  `grep -c '"pass_leg": true' tools/gate-legs.json` prints 2.
  Red when: reds are read from the ledger, which gives every leg 0 or 1 and changes the rows.
- **AC2** — When `python <kit>/pass_legs.py --report` runs in F after AC1, each leg's line
  carries the verdict in the table above.
  Red when: the last-seconds half of `over-cap` is absent, which reads `c-stale` as `selected`, or
  the unattended gate is matched by leg name, which reads `e-unatt` as `selected`.
- **AC3** — When `--write` and then `--report` run in B, `p1` to `p6` read `selected`, `p7` reads
  `over-budget`, and `--check` prints `pass-legs: 6 declared, 600.0s of 600s`.
  Red when: the fill compares with `<` and not `<=`, which leaves `p6` out, or the walk stops at the
  first leg that does not fit.
- **AC4** — When `python <kit>/pass_legs.py --check` runs in F after AC1 it exits 0. With
  `"pass_leg": true` typed onto `h-quiet`'s row it exits 1 naming `h-quiet`, and with the line
  deleted from `a-cheap`'s row it exits 1 naming `a-cheap`.
  Red when: the check compares only one direction.
- **AC5** — When `python <kit>/pass_legs.py --apply` runs in F over a manifest with no
  field, committed, `git diff --numstat -- tools/gate-legs.json` reports 2 lines added and 0
  deleted, and a second `--apply` leaves `git diff` unchanged.
  Red when: the manifest is re-dumped as JSON, which deletes lines, or a second run inserts a second
  line.
- **AC6** — When `--write` runs in F with the run log removed from its git directory, it exits 1, its output
  carries `DEAD PROBE`, and `git status --porcelain` shows the evidence file and the manifest
  unmoved.
  Red when: an absent run log is read as zero reds, which empties the evidence and strips the field.
- **AC7** — When `python <kit>/pass_legs.py --write` runs in F with `GOV_NODE` unset, it
  exits 2 naming `GOV_NODE` and writes nothing.
  Red when: the node defaults to `a`.
- **AC8** — When `grep -c '"doc_reads", "pack", "enforces", "pass_leg"' tools/run-gates/run-gates.test.sh`
  runs it prints 2.
  Red when: one `KNOWN` literal is widened and the other is not, which prints 1.
- **AC9** — When F holds no `<kit>/pass-leg-evidence.txt` and no field,
  `python <kit>/pass_legs.py --check` exits 0 printing `not derived, no evidence file`, and
  `--apply` leaves `git status --porcelain` empty. With a field typed onto any row, `--check`
  exits 1 naming that leg.
  Red when: a missing evidence file refuses, which reds every adopter's preflight on arrival.
- **AC10** — When `python tools/run-gates/regen.py --list` runs in this repository, one item names
  `pass_legs.py --apply` at stage 2, and `grep -c 'pass-leg-evidence.txt' tools/run-gates/kit.toml`
  prints 1 or more.
  Red when: the row carries no `stage`, which the list names as a skipped row and no item.
- **AC11** — When `python <kit>/pass_legs.py --check` runs in this repository after S7's
  commit, it exits 0, its sum is at or under 600, and `--report` shows no `selected` leg whose
  `chunk` is `selftests` or `e2e` and none naming `check-unattended.sh`.
  Red when: the manifest's fields were typed from the prompt's table and not written by `--write`.
  figure: the declared count and sum are DERIVED at observation. §4's 26 legs and 412.8 s are
  PINNED to 2026-11-12 and are not asserted.
  fixture: needs node `a`'s run log, which a linked worktree of the primary clone reaches through
  the common directory. The tree holds it today.
- **AC12** — When `grep -c 'pass_legs.py' tools/run-gates/README.md` runs it prints 2 or more, and
  `grep -c 'PASS_BUDGET_SECONDS' tools/run-gates/README.md` prints 1 or more.
  Red when: the rule is recorded only in this spec.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `leg ceilings clear their evidenced maximum` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.test.sh · covers AC8 · a control manifest whose row carries `pass_leg` must pass and one carrying the near-miss `pass_legs` must red, staged with `pass_leg` taken back out of the `KNOWN` literal · none

The `leg ceilings clear their evidenced maximum` leg is named because this unit must not move it:
no ceiling and no ceiling-evidence row changes here.

## 8. Open questions

- **F1 — What is the per-leg cap, `PASS_LEG_CAP_SECONDS`?** The owner asks for a stated cap and
  states no value. At this base the choice barely moves the list: PINNED, measured 2026-11-12, a
  cap of 60 selects 25 legs at 377.3 s, and 120 or 200 both select 26 at 412.8 s.
  - **60** — a tenth of the budget. It drops `install-prefix (shipped surface)`, 27 reds at 58.2 s
    evidenced and above 60 s in the ledger.
  - **120** — a fifth of the budget, and the floor `tools/run-gates/ceiling-margin.txt` already
    uses for headroom. No single leg can take more than a fifth of a pass.
  - **200** — a third of the budget. It admits nothing more today, and lets three legs fill a pass.
  Recommendation: 120.
  RESOLVED (agent, 2026-11-12, delegated): 120. A fifth of the budget, the floor the ceiling margin already uses, and it selects the same legs as 200 at this base.

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft.
- rev-2 · 2026-11-12 · every §8 fork resolved in place under the run's mandate (M3).

## 10. Reuse audit

The seam is the shape of `tools/run-gates/derive-ceilings.py`: a verb that distils node-local run
records into a tracked evidence file, and a check that reads tracked files only. This unit reads
that file's own output, `ceiling-evidence.txt`, as its cost, finds the manifest as its `read_legs`
does, and takes its `GOV_NODE` and DEAD PROBE refusals. The second seam is the staged
`[[regenerate]]` row that `tools/run-gates/regen.py#build_items` reads, which gives the field its
landing-time write and its preflight check with no new leg. `reuse_lookup.py` returned name-stem
neighbours only, `derive_kit_rel` in `tools/run-gates/measure_legs.py` the nearest, and no function
that derives a manifest field: for the derivation itself, no existing seam fits, and the evidence
is that `derive-ceilings.py`, the nearest writer, writes its evidence file alone and only compares
the manifest. Recall returned `TOOL-aScouredKit-27` for the canary's pinned key set,
`DEPL-aBenchedProbe-2` for how `ceiling` travels to an adopter, and `TOOL-dWitnessedBar-10`, a
deferred design for a new row field with no built seam.

Where the records and the source disagreed: the prompt and the build README say the list is
derived "from the gate ledger", and the ledger holds one row per leg with no history. The red count
is read from the bar run log, and the ledger gives the last seconds alone.

Reuse probe used: `python tools/codebase-map/reuse_lookup.py "derive a per-leg field in the gate leg manifest from the gate ledger and ceiling evidence"`.
Recall terms used: `python tools/memory-recall/query.py "how is a per-leg manifest field derived from recorded reds and evidenced seconds" --terms "gate-legs.json leg manifest key set canary ceiling evidence derive-ceilings run log gates.log ledger red"`.
