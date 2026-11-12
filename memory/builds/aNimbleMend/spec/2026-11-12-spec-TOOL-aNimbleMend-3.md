# TOOL-aNimbleMend-3 — the budget gate: the declared pass legs' cost rows sum inside the budget, red past the limit, with no leg over the cap, unmeasured, held or of an excluded class

**Status:** INPROGRESS · rev-1 · 2026-11-12 · node a · Tier-2 · base 97e0841d · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md) | research | TOOL-aNimbleMend-1 TOOL-aNimbleMend-2 TOOL-aNimbleMend-4 TOOL-aNimbleMend-5 TOOL-aNimbleMend-6 TOOL-aNimbleMend-7 TOOL-aNimbleMend-8 TOOL-aNimbleMend-9 TOOL-aNimbleMend-10 TOOL-aNimbleMend-11 TOOL-aNimbleMend-12 |
| [2026-11-12-prompt-TOOL-aNimbleMend-3-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-3-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-aNimbleMend-2's rule writes the `pass_leg` field, and nothing re-checks the list it leaves.
A field typed by hand, a cost row that rose after the last apply, or a fault in the rule can put a
pass over its ten minutes with no red anywhere. This unit adds the independent check: a second
reading of the same tracked files that reds a declared list the owner's limits refuse.

## 2. Scope (IN)

- **S1** — One constant in `tools/run-gates/pass_legs.py`, `PASS_LIMIT_SECONDS`, 690, beside
  `PASS_BUDGET_SECONDS` and `PASS_LEG_CAP_SECONDS`, which TOOL-aNimbleMend-2 mints there. Observed
  by AC1.
- **S2** — A function, `check_pass_budget`, and its verb, `pass_legs.py --budget`. It grades every
  manifest row carrying `pass_leg` against the five findings of §4, "The findings", and prints the
  lines of §4, "The output". Observed by AC2, AC3, AC4, AC5 and AC6.
- **S3** — A verb, `pass_legs.py --figures`, that prints the budget, the limit and the cap as one
  tab-separated line, so a shell reader holds no copy of them. Observed by AC1.
- **S4** — `derive-ceilings.py --check` runs `check_pass_budget` after its own arm, whether or not
  a ceiling failed, and exits with the higher of the two. The existing leg
  `leg ceilings clear their evidenced maximum` then carries the gate on every bar. Where
  `pass_legs.py` is not beside the script, it prints one line saying the budget was not graded and
  its own verdict stands. Observed by AC7 and AC8.
- **S5** — The section of `tools/run-gates/README.md` that TOOL-aNimbleMend-2 writes for
  `pass_legs.py` gains the two verbs, the limit, the five findings and the leg that carries them.
  Observed by AC9.

## 3. Non-goals (OUT)

- A new leg. The gate is an arm of a leg the bar already runs (§4, "Alternatives rejected").
- Reading `pass.fast-legs`. The field is tracked data whichever way the switch reads, and a list
  that is over its limit is wrong before anyone turns the switch back on.
- Choosing the cap. `PASS_LEG_CAP_SECONDS` and its value are F1 of TOOL-aNimbleMend-2.
- Grading whether the list is the rule's own output. That is `pass_legs.py --check`, the staged
  check of TOOL-aNimbleMend-2, and the `no-red` reason is its concern alone.
- Timing a run. A pass that takes longer than its budget is TOOL-aNimbleMend-5's finding.
- An adopter leg. The carrying leg is gov's own, an `[[exempt_leg]]`, because it reads gov's cost
  rows. An adopter runs `--budget` by hand once it holds cost rows of its own.
- Any change to a `ceiling`, to `tools/run-gates/ceiling-evidence.txt`, or to the bar runner.
- The help page, which is TOOL-aNimbleMend-11's, and the kit version, which the lander's `mint`
  moves.

### Edges

- **consumes-from** `TOOL-aNimbleMend-2` — `pass_legs.py`, the `pass_leg` field, the constants
  `PASS_BUDGET_SECONDS` and `PASS_LEG_CAP_SECONDS`, and the predicate `check_pass_eligible`.
  Without them there is no declared row to grade and no figure to grade it against.
- **hands-off** `TOOL-aNimbleMend-5` — the budget and the limit its adapter compares a run's wall
  time with, which it reads from the figures verb of S3 and types nowhere.

## 4. Design

### Evidence

Read at 97e0841d, and from TOOL-aNimbleMend-2 rev-1 for what that unit builds first.

- **The carrying leg reads tracked files only.** `tools/run-gates/derive-ceilings.py#cmd_check`
  reads the manifest through `tools/run-gates/derive-ceilings.py#read_legs`, which honours
  `GATE_LEGS`, and the cost rows through `tools/run-gates/derive-ceilings.py#read_evidence`. Its leg
  last ran in `0.5 s` (PINNED, the primary checkout's ledger, 2026-11-12).
- **That leg is gov's.** `tools/govkit/registry.toml` lists it as an `[[exempt_leg]]`, and
  `tools/run-gates/kit.toml` withholds the cost rows from installs. The script ships.
- **A leg's cost is its cost row.** TOOL-aNimbleMend-2 fills the budget from the maximum in the
  ceiling evidence and says this gate sums the same figure.
- **The predicate asks `no-red` before cost.** `check_pass_eligible` answers the first reason that
  fits, in the order `selftest`, `e2e`, `unattended-gate`, `no-red`, `unevidenced`, `over-cap`. A
  declared leg with no red row therefore never reaches the two cost reasons through it.
- **The runner holds more than the predicate excludes.** The runner holds a leg whose `subject` is
  `kit` or whose `chunk` is `selftests` (TOOL-aNimbleMend-5's §4, "Evidence"). The predicate has
  no reason for `subject`. One row at this base is held by subject alone, outside both excluded
  chunks, and has a cost row under every offered cap:
  `python resolver (behaviour + inline parity + idiom ban)`, at `48.8 s` (PINNED, the ceiling
  evidence, dated 2026-09-24). The bar run log names it in a red bar.
- **The suite of the carrying script copies two files.** `tools/run-gates/run-gates.evidence.test.sh`
  builds each fixture from `derive-ceilings.py` and `ceiling-margin.txt` alone, at three sites, so
  an unguarded import of a sibling module would break every existing arm.

### The findings

A declared leg is a manifest row carrying `pass_leg`. Each finding names the leg.

| # | Finding | Decided by |
|---|---|---|
| B1 | the leg is of an excluded class | `check_pass_eligible` answers `selftest`, `e2e` or `unattended-gate` |
| B2 | the runner would hold the leg | its `subject` is `kit` |
| B3 | the leg has no cost row | no row in the ceiling evidence |
| B4 | the leg is over the cap | its cost row is above `PASS_LEG_CAP_SECONDS`, or `check_pass_eligible` answers `over-cap` |
| B5 | the list is over the limit | the declared legs' cost rows sum above `PASS_LIMIT_SECONDS` |

B3 and B4 ask the cost row directly, because the predicate's order hides it behind `no-red`. The
second half of B4 keeps the predicate's last-seconds reading, which catches a cost row gone stale
low. B5 sums the legs that have a cost row; a leg without one is already B3. A sum above
`PASS_BUDGET_SECONDS` and at or under the limit is a warning line and no finding: the owner allows
that band, and it is where a cost row that rose after the last apply lands.

B2 is this gate's own clause. Declaring a held leg buys nothing, since the pass-leg runner prints a
finding and runs nothing for it. Once the predicate of TOOL-aNimbleMend-2 answers a reason for a
kit-subject row, B2 reads that reason and its own comparison goes.

### The output

```
PASS-BUDGET FAILED — <leg>: <the finding's sentence>
PASS-BUDGET FAILED — <n> declared leg(s) sum to <sum>s, over the <limit>s limit (budget <budget>s)
pass-budget: WARN — <n> declared leg(s) sum to <sum>s, over the <budget>s budget, inside the <limit>s limit
pass-budget: <n> leg(s) declared, <sum>s against a <budget>s budget and a <limit>s limit, cap <cap>s
pass-budget: 0 leg(s) declared
```

Failures go to stderr, as the ceiling arm's do. `--budget` exits 0 when clean, a warning included,
1 on any finding, and 2 when it cannot grade: a manifest that does not parse, a limit under the
budget, or a cap over the budget. A warning line is printed ahead of the summary, never in its
place. The last line of a clean run is always the summary or the zero line, so a run that graded
nothing says so.

`--figures` prints `<budget><TAB><limit><TAB><cap>` and nothing else, every field an integer and
none empty, so a tab-split `read` in a shell cannot shift a field.

### The call from the ceiling check (S4)

`cmd_check` imports `pass_legs` inside the function, after its ceiling arm has collected its
failures and before it returns. An `ImportError` prints
`pass-budget: not graded — pass_legs.py is not beside derive-ceilings.py` on stderr and changes no
exit. Otherwise it calls `check_pass_budget` with the manifest and the cost rows it has already
read, prints what the function returns, and exits 1 when either arm found something. The early
`UNMEASURED` return, for a tree with no cost rows at all, stays ahead of both arms.

### What it does not check

- A cost row is the worst reading on record, and a leg never re-measured can sit under its true
  cost. PINNED, 2026-11-12: `memory hygiene` holds a cost row of `86.8 s` and last ran in
  `632.7 s`. The last-seconds half of B4 covers a leg with a ledger reading, and
  TOOL-aNimbleMend-5's overrun finding covers the rest at run time.
- The sum is the legs run one after another. A pooled run takes less, and the runner's own start
  is in no cost row.
- A leg its guard skips still counts in full.
- A suite-shaped leg that is neither held nor in an excluded chunk is graded by the cap alone.
- Every cost row was read on node `a`. Another node's seconds are not in the sum.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| `PASS_LIMIT_SECONDS` | `pass_legs.py` | no `py.constant` cell is declared; the spelling of the two beside it |
| `check_pass_budget` | `pass_legs.py` | `py.function`; `lexicon.py --suggest` answered OK on 2026-11-12 |
| the verbs `--budget` and `--figures` | `pass_legs.py` | no cell grades a flag |
| the prefixes `pass-budget:` and `PASS-BUDGET FAILED` | stdout and stderr lines | no cell grades an output prefix |

### Migration

Additive. A manifest with no `pass_leg` field prints the zero line and moves no exit.

### Rollout

No switch. The arm reads the field, and a tree whose rule has selected nothing has nothing to grade.

### Files touched (estimate)

- `tools/run-gates/pass_legs.py`
- `tools/run-gates/derive-ceilings.py`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/README.md`

### Alternatives rejected

- **A leg of its own.** A new row owes a pin, an exempt row, a dossier name, a pending row and a
  cost row, the set `memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md` names, and that
  record prefers a check inside a leg that already reads the same files.
- **A finding inside `pass_legs.py --check`.** That check is a staged freshness check, so the bar's
  preflight refuses on it and names `--regen` as the cure. A re-apply does not cure a typed field's
  budget, and a refusal is no leg's red.
- **The figures in a tracked file of their own.** TOOL-aNimbleMend-2 already states the budget and
  the cap as constants of the module the rule lives in, so a file would be their second home.
- **The limit derived from the budget by a percentage.** The owner states both figures. A fixture
  that needs a small budget and a larger limit sets two constants and computes nothing.
- **An unguarded import in `derive-ceilings.py`.** It breaks the three fixture sites of the
  existing suite and any install that holds the script without its sibling.

## 5. Production-readiness checklist

- security — no write path and no input beyond tracked files and `GATE_LEGS`, which the ceiling
  check already reads. A leg name is printed and compared, never run.
- perf / scale — one pass over the manifest and two small files, inside a leg that already reads
  both.
- error / empty / loading states — no declared row prints the zero line; no cost rows at all is
  the ceiling check's `UNMEASURED`; a missing sibling module prints the not-graded line; figures
  that contradict each other refuse with exit 2.
- observability — a `pass-budget:` line on every run, one failure line per finding, one warning
  line in the tolerance band.
- risks — at this base the rule of TOOL-aNimbleMend-2 rev-1 can select the kit-subject row §4
  names, which B2 reds. That is a disagreement between the two specs, to settle in that unit's
  predicate before code. TOOL-aNimbleMend-5 rev-1 says this unit declares the budget; the budget
  constant is TOOL-aNimbleMend-2's, and this unit adds the limit and the verb that prints both.
- testing — AC1 to AC8 run in a scratch repository on planted manifests; the arm of §7 keeps them.
- migration — additive; see §4, "Migration".
- user docs — the kit README, S5. The help page is TOOL-aNimbleMend-11's.

## 6. Acceptance criteria

Fixture G is a scratch git repository under `%TEMP%` with a short name. It holds copies of
`pass_legs.py`, `derive-ceilings.py` and `ceiling-margin.txt` at their kit path, a hand-written
manifest beside the kit directory, and a hand-written cost file. Every leg has `chunk` `product`,
a ceiling of 1000 and a cost row unless its line says otherwise. The cap is whatever
`PASS_LEG_CAP_SECONDS` holds, `C` below. Each manifest is named by `GATE_LEGS`. `<kit>` is the
run-gates kit directory: `tools/run-gates` in this repository, and its copy in G.

| Manifest | Declared legs | Expected |
|---|---|---|
| `green` | six, each costing 100 | exit 0, the summary line with a sum of 600 |
| `none` | no row carries the field | exit 0, `pass-budget: 0 leg(s) declared` |
| `band` | seven, each costing 95 | exit 0, one `WARN` line naming 665, then the summary line |
| `over` | seven, each costing 100 | exit 1, B5 naming 700 |
| `cap` | one costing `C` plus 1 | exit 1, B4 naming the leg |
| `bare` | one with no cost row | exit 1, B3 naming the leg |
| `class` | four costing 1: `chunk` `selftests`, `chunk` `e2e`, an `argv` naming `check-unattended.sh`, `subject` `kit` | exit 1, three B1 lines and one B2 line |

- **AC1** — When `python <kit>/pass_legs.py --figures` runs in this repository, it prints
  one line of three tab-separated integers, the first 600 and the second 690.
  Red when: the limit is typed in a second place, or a field is empty.
  figure: 600 and 690 are PINNED, the owner's prompt of 2026-11-11; the third is DERIVED from the
  constant.
- **AC2** — When `python <kit>/pass_legs.py --budget` runs in G over `green` and over
  `none`, each exits 0, its last line is the line the table gives, and neither prints `WARN`.
  Red when: the band is entered with `>=`, which warns on a list at exactly the budget, or an
  empty list prints a summary over no leg.
- **AC3** — When the same command runs over `band`, it exits 0 and prints one line opening
  `pass-budget: WARN`.
  Red when: the tolerance band is a finding, or passes with no line.
- **AC4** — When the same command runs over `over`, it exits 1 and prints one line opening
  `PASS-BUDGET FAILED` that names 700 and the limit.
  Red when: the sum is compared with nothing, or with the budget alone.
- **AC5** — When the same command runs over `cap` and over `bare`, each exits 1 and names its leg,
  with no pass-leg evidence file in G.
  Red when: the cost is asked only through `check_pass_eligible`, which answers `no-red` first and
  hides both.
- **AC6** — When the same command runs over `class`, it exits 1 and prints four failure lines, one
  per leg, the kit-subject leg's saying the runner would hold it.
  Red when: a class is matched by a typed leg name, or the held clause is absent.
- **AC7** — When `python <kit>/derive-ceilings.py --check` runs in G with `GATE_LEGS` naming `over`,
  it exits 1 and its output holds the B5 line; over `green` it exits 0 and holds both the
  `ceiling-evidence:` summary and the `pass-budget:` summary.
  Red when: the ceiling check does not call the arm, so the bar never runs the gate.
- **AC8** — When the same check runs over `over` with `pass_legs.py` removed from G's kit copy, it
  exits 0 and prints a line opening `pass-budget: not graded`.
  Red when: the import is unguarded, which exits with a traceback and breaks the existing arms.
- **AC9** — When `grep -c 'PASS_LIMIT_SECONDS' tools/run-gates/README.md` runs it prints 1 or more,
  and `grep -c -- '--budget' tools/run-gates/README.md` prints 1 or more.
  Red when: the limit and the gate are recorded only in this spec.

## 7. Gates

`leg ceilings clear their evidenced maximum` · `run-gates evidence` · `python reads (a name never bound, an import outside its guard)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `docs` · `install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The first is the leg that carries the gate from this unit on: at the close it grades gov's own
declared list, and a red there is a finding about that list. `run-gates evidence` holds the new
arms and is in the held tier, so the close runs it only where it asks for that tier. No path of
§4's estimate trips a guard that is not broad, by the checker's `--legs-for` at 97e0841d. The
kit epoch leg expects the lander's `mint`.

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC2 AC3 AC4 AC5 AC6 AC7 AC8 · fixture G's manifests, staged with the limit comparison removed, then with the held clause removed · `FLOOR_ASSERTIONS`, raised by the arms added

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft.

## 10. Reuse audit

The seam is the ceiling check, `tools/run-gates/derive-ceilings.py#cmd_check`: a leg that already
reads the manifest and the cost rows from tracked files, already honours `GATE_LEGS` for a planted
manifest, and already has a suite that copies it into a scratch repository. The gate's own logic
sits in `pass_legs.py`, the module TOOL-aNimbleMend-2 builds first, beside the two constants and
the predicate it reuses. `python tools/codebase-map/reuse_lookup.py "a gate that sums the evidenced
seconds of a declared subset of gate legs against a wall-clock budget"` ranked name-stem neighbours,
`read_legs` in `tools/run-gates/derive-ceilings.py` the nearest, with `check_budgets` in
`tools/policy/budgets.py` and `check_gate_wall` in `tools/unattended/lib-unattended.sh`, which
grade the policy file's cap table and a bar's declared wall. For a sum over a declared subset of
legs, no existing seam fits, and the evidence is that the ceiling check compares each leg with its
own ceiling and adds nothing up. Recall returned `TOOL-aQuenchedHarness-2`, the ceiling check's own spec, and
`TOOL-dWitnessedBar-10`, a deferred design with no built seam. `gotchas.py --for-paths` over the
estimate selected `a-new-leg-trips-a-growing-set-of-meta-gates`, which decided S4,
`fixture-passes-by-finding-nothing`, which the `none` manifest and AC5's missing file answer, and
`empty-field-collapses-unless-it-is-last`, which is why `--figures` prints no empty field.

Where the records and the source disagreed: the prompt says the gate sums "evidenced ceilings", and
the tracked file holds evidenced maxima, which are readings; a `ceiling` is the hang bound beside
them. The gate sums the readings.

Recall terms used: `python tools/memory-recall/query.py "which gate legs are cheap enough to run
after every pass, and how is a leg's evidenced wall time budgeted" --terms "pass leg budget ceiling
evidence evidenced maximum derive-ceilings scoped --only --staged spec tokens --spec hygiene"`
