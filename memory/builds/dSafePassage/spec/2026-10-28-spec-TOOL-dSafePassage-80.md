# TOOL-dSafePassage-80 — five leg ceilings clear their evidence by the declared margin, and upgrade-walk is budgeted

**Status:** DEFERRED · rev-4 · 2026-10-28 · node d · Tier-2 · base 83817478 · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-prompt-TOOL-dSafePassage-80-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-80-1-spec-writer.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-80-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-80-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

At the close, two declaration legs went red. The first is
`python tools/run-gates/derive-ceilings.py --check`. Against the evidence rows the close wrote, it
names five legs whose `ceiling` in `tools/gate-legs.json` is short of its evidenced maximum plus the
headroom `tools/run-gates/ceiling-margin.txt` declares. Three are legs this build added:
`step-gate`, `docs` and `upgrade-walk`. Two are older legs that timed out twice in the close's
discovery bar: `routed commits name a specced unit` and `spec tokens (a spec's own names resolve)`.
The second red leg is `every held leg is budgeted, every budget row resolves`. It names
`upgrade-walk`, a held leg with no row in `tools/run-gates/selftest-budgets.txt`.

This unit sets the five integers to the least value the first check passes, by the rounding the
manifest already uses. It adds the budget row by that file's own rule, and commits the three
evidence rows the ceilings rest on, so neither leg names any of these legs.

## 2. Scope (IN)

- **S1** — `step-gate`'s `ceiling` (`tools/gate-legs.json:1460`) goes from 60 to 130, clearing its
  evidence row of 4.4 s (`tools/run-gates/ceiling-evidence.txt:136`), §4 "The values". Observed by
  AC1, AC2 and AC3.
- **S2** — `docs`'s `ceiling` (`tools/gate-legs.json:1471`) goes from 60 to 130, clearing its
  evidence row of 2.7 s (`tools/run-gates/ceiling-evidence.txt:49`). Observed by AC1, AC2 and AC3.
- **S3** — `upgrade-walk`'s `ceiling` (`tools/gate-legs.json:1483`) goes from 7200 to 14360,
  clearing its evidence row of 7177.0 s (`tools/run-gates/ceiling-evidence.txt:146`, S4). Observed
  by AC1, AC2 and AC3.
- **S4** — The pass commits `tools/run-gates/ceiling-evidence.txt` exactly as the close's writes
  left it in the working tree, §4 "The evidence rows". That is three rows: `upgrade-walk` and
  `routed commits name a specced unit` added, and `spec tokens (a spec's own names resolve)` raised.
  Each was written by `derive-ceilings.py --write --observed` under `GOV_NODE=a`, and each is kept
  as written, node `a` included. No other line of the file moves. Observed by AC1 and AC5.
- **S5** — `tools/run-gates/selftest-budgets.txt` gains an `upgrade-walk` row of 10770 s, by the
  file's own rule against the 7177 s reading, with an empty argv column so the command is taken from
  `tools/gate-legs.json`, §4 "The budget row". Observed by AC4.
- **S6** — `routed commits name a specced unit`'s `ceiling` (`tools/gate-legs.json:1104`) goes from
  300 to 510, clearing its evidence row of 253.0 s (`tools/run-gates/ceiling-evidence.txt:115`, S4).
  Observed by AC1, AC2 and AC3.
- **S7** — `spec tokens (a spec's own names resolve)`'s `ceiling` (`tools/gate-legs.json:1749`) goes
  from 390 to 740, clearing its evidence row of 366.0 s (`tools/run-gates/ceiling-evidence.txt:134`,
  S4). Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- Any other leg's `ceiling`, any other field of these five rows, and any other row of
  `tools/run-gates/selftest-budgets.txt`.
- A hand edit of `tools/run-gates/ceiling-evidence.txt`, or any `--write` run over it in this pass.
  The evidence is written by `derive-ceilings.py --write` alone, and its header forbids a hand edit
  (`tools/run-gates/ceiling-evidence.txt:3-5`). S4 commits bytes the close's writes produced.
- Any change to `tools/run-gates/ceiling-margin.txt`, to `upgrade-walk`'s own cost, or to why
  `routed commits name a specced unit` and `spec tokens (a spec's own names resolve)` take as long as
  they do.
- The three rows' node column, which reads `a`. The readings were taken on node `a`, and the check
  reads the seconds and not the node (`tools/run-gates/derive-ceilings.py:683`).
- A budget row for the two older legs. Both carry `"subject": "repo"` and chunk `declarations`
  (`tools/gate-legs.json:1101-1102`, `:1747-1748`), so neither is held and neither owes a row
  (`tools/run-gates/run-selftests.sh:945-962`).
- A help page. No page under `help/` states any of the five ceilings or a budget for them
  (`git grep` over `help/` for `7200`, `7177`, and for `ceiling` beside these legs' names finds none
  at `83817478f`). No adopter receives any of the values, §4 "Migration".

### Finding for the owner: a two-hour leg under the charter's cost rule

This is a finding. S5 gives the leg the cost verdict it lacked, and nothing here changes what the
leg costs.

The charter's cost rule is `[cost]`: every suite declares a wall-clock ceiling and reds on a breach,
because a check nobody can afford to run is never run (`AGENTS.md:28`). This repository splits that
rule in two. The `ceiling` S3 raises is a hang bound and not a cost verdict
(`tools/run-gates/ceiling-margin.txt:14`). The cost verdict of a held leg is its row in
`tools/run-gates/selftest-budgets.txt` (`:11-14`), which S5 adds.

- **Who pays it.** `upgrade-walk` carries `"subject": "kit"`, so the runner holds it on a default bar
  and runs it only when `GATE_SELFTESTS` asks (`tools/run-gates/run-gates.sh:3249-3250`). Remote CI
  sets no `GATE_SELFTESTS` (`.github/workflows/remote-ci.yml`), and the pre-push hook demands a
  self-test run only when the pusher sets it (`.githooks/pre-push:1653`). A default bar is not
  slowed.
- **What it costs where it runs.** On a bar that runs the held legs, 7177 s is about two hours, and
  the bar can finish no sooner than its longest leg. The next-longest evidenced leg is
  `govkit selftest` at 3358.7 s (`ceiling-evidence.txt`), and the whole-run wall of 21600 s was
  sized against a longest leg of 3837 s and about 4000 s end to end
  (`tools/run-gates/gate-profiles.txt:104-106`). This leg roughly doubles the wall-clock floor of
  every such bar. The reading was taken under load from a closing review and three suite researchers
  (its row's source text), so a quiet run may be shorter. Nothing in the tree measures that today.
- **What a hang costs.** At 14360 s the leg is killed at four hours. Its serial retry runs alone
  after the pool drains and inside the run's wall (`tools/run-gates/README.md:50-56`), and
  14360 + 14360 exceeds the 21600 s wall, so the wall rather than the retry decides that bar's
  verdict. The unattended driver sizes its backstop from `ceiling_max`
  (`tools/run-gates/README.md:603-606`), which stays 16040 s (`unattended kit gate`), so that
  backstop does not move.
- **What the budget says.** At 10770 s, the leg is the largest single budget in the file. A breach
  is read by re-running on a quiet box first (`tools/run-gates/selftest-budgets.txt:20-25`), which
  for this leg is another two hours.

The owner's remaining options on the cost itself, as this writer reads them: accept a two-hour
self-test; cut the walk's own cost, its cases or their spawns; or split it so a bar pays the
expensive cases only when their inputs move. This unit takes none of them.

### Edges

- **consumes-from** external — three rows of `tools/run-gates/ceiling-evidence.txt`, written at the
  close by `derive-ceilings.py --write --observed` under `GOV_NODE=a` and present only in the
  working tree at writing time: `upgrade-walk` at 7177.0 s, `routed commits name a specced unit` at
  253.0 s, and `spec tokens (a spec's own names resolve)` raised from 195.0 s to 366.0 s
  (`git show HEAD:tools/run-gates/ceiling-evidence.txt` holds none of the three values). S4 commits
  them and does not produce them. If the working tree no longer holds them, the pass stops and
  reports rather than re-deriving them, because a fresh `--write` also re-reads the run record and
  can raise other rows.
- **hands-off** external — the cost finding above: a cheaper or split leg, for the owner.

Read and closed, so named here rather than joined: TOOL-dSafePassage-5 added `upgrade-walk`,
TOOL-dSafePassage-10 added `step-gate`, and TOOL-dSafePassage-13 added `docs`, each with the
ceiling this unit raises. TOOL-dGroundRules-87 set the `spec tokens` ceiling of 390 that S7 raises.
The edge join counts CLOSED specs, and a CLOSED spec cannot take the matching line.

## 4. Design

### The rule

`cmd_check` reads two tracked files and the margin (`tools/run-gates/derive-ceilings.py:643-648`).
For each leg it computes `need = max(floor, frac * max)` (`:663`) and fails the leg when
`ceiling < max + need` (`:683`). It also fails a leg whose `ceiling` is not an integer (`:660-661`).
The margin file declares a floor of 120 s and a fraction of 1.0
(`tools/run-gates/ceiling-margin.txt:26`), read by `read_margin`
(`tools/run-gates/derive-ceilings.py:145-174`). The REACHED branch (`:679`) grades runner rows
alone, and all five rows here are out-of-band, so each falls to the headroom branch.

The pass condition is `ceiling >= max + max(120, max)`. Under 120 s of evidence the floor governs,
and the ceiling must be at least `max + 120`. At 120 s or more the fraction governs, and the ceiling
must be at least twice the maximum.

### The rounding

Every `ceiling` in `tools/gate-legs.json` is a multiple of 10: 148 rows and none other, read at
`83817478f`. TOOL-dGroundRules-87 sized the `spec tokens` ceiling the same way, as the least multiple
of 10 at or above the required value. Each value below is that least multiple, `10 × ⌈required / 10⌉`,
so it carries no headroom beyond the margin file's own.

### The values

| Leg | Evidence row | Required: max + max(120, 1.0 × max) | Ceiling now | New ceiling | Clears by |
|---|---|---|---|---|---|
| `step-gate` | 4.4 s, `tools/run-gates/ceiling-evidence.txt:136` | 4.4 + 120 = 124.4 s | 60 | 130 | 5.6 s |
| `docs` | 2.7 s, `tools/run-gates/ceiling-evidence.txt:49` | 2.7 + 120 = 122.7 s | 60 | 130 | 7.3 s |
| `upgrade-walk` | 7177.0 s, `tools/run-gates/ceiling-evidence.txt:146` | 7177.0 + 7177.0 = 14354.0 s | 7200 | 14360 | 6.0 s |
| `routed commits name a specced unit` | 253.0 s, `tools/run-gates/ceiling-evidence.txt:115` | 253.0 + 253.0 = 506.0 s | 300 | 510 | 4.0 s |
| `spec tokens (a spec's own names resolve)` | 366.0 s, `tools/run-gates/ceiling-evidence.txt:134` | 366.0 + 366.0 = 732.0 s | 390 | 740 | 8.0 s |

The evidence figures are PINNED as written in the evidence file at writing time. Each value stays a
JSON integer, because the check fails a non-integer ceiling.

The two older legs' readings were each taken alone on a frozen clone of `83817478f`, and each leg
timed out at its current ceiling twice in the discovery bar's pool (their rows' source text). The
margin's fraction doubles a reading taken alone. Whether that clears a pooled run is a question
only the close's bar answers. A pooled run that still crosses the new ceiling gets the runner's
serial retry, alone, as before.

### The edit

Five lines of `tools/gate-legs.json` change, each the `"ceiling":` line of one of the five rows,
and nothing else in the file moves:

```
:1104   "ceiling": 300    ->   "ceiling": 510      (routed commits name a specced unit)
:1460   "ceiling": 60     ->   "ceiling": 130      (step-gate)
:1471   "ceiling": 60     ->   "ceiling": 130      (docs)
:1483   "ceiling": 7200   ->   "ceiling": 14360    (upgrade-walk)
:1749   "ceiling": 390    ->   "ceiling": 740      (spec tokens (a spec's own names resolve))
```

### The evidence rows

At writing time `git diff -U0 -- tools/run-gates/ceiling-evidence.txt` shows three hunks and no
header change:

| Hunk | Row | Change |
|---|---|---|
| `:115` | `routed commits name a specced unit` | one line added: 253.0 s, 1 reading, node `a`, 2026-10-28 |
| `:134` | `spec tokens (a spec's own names resolve)` | one line replaced: 195.0 s of 2026-10-26 becomes 366.0 s, 1 reading, node `a`, 2026-10-28 |
| `:146` | `upgrade-walk` | one line added: 7177.0 s, 1 reading, node `a`, 2026-10-28 |

Each row's sixth field is its `--how` text: the command, the tree it ran over, rc 0, and the
conditions. The `spec tokens` replacement is the file's monotone raise, a higher reading taking the
row (`tools/run-gates/ceiling-evidence.txt:7-11`). The pass stages that file as it stands and
runs no `derive-ceilings.py --write`.

### The budget row

The file's rule is the worst observed reading times 1.5, floored at 60 s
(`tools/run-gates/selftest-budgets.txt:20`). Its rows round the product up to a multiple of 10:
44 of the 48 rows whose reading reads `worst of <n> readings <s>s, x1.5` equal
`max(60, 10 × ⌈1.5 × s / 10⌉)`, read at `83817478f`. For `upgrade-walk`, 1.5 × 7177 = 10765.5, so the row is 10770.

The row's columns are `<name>`, `<budget seconds>`, `<argv>`, `<the reading>` (`:49`). The argv
column is empty, as `govkit selftest`'s is (`:66`), so `read_population` takes the command from the
manifest (`tools/run-gates/run-selftests.sh:704-709`) and the manifest stays the one place it is
written. The row sits after `unattended runlog-writer selftest` and before `verdict-epoch self-test`:

```
upgrade-walk<TAB>10770<TAB><TAB>one reading 7177s on node a 2026-10-28, the whole leg timed by date over the worktree at 83817478f, rc 0, under load from a closing review and three suite researchers, the upgrade-walk row of ceiling-evidence.txt, x1.5
```

The forward direction of `run-selftests.sh --check` names every leg with `subject` `kit` or chunk
`selftests` that has no row (`tools/run-gates/run-selftests.sh:945-962`). At `83817478f` it
names `upgrade-walk` alone, as the main loop confirmed by a run.

### The probes

Each runs from the repository root, from a file written to the scratchpad. Each parses the tracked
files itself and imports neither checker, so neither shares state with the check it re-derives.

The ceiling probe, for AC1. Its last line applies the check's predicate to every leg in the two
files:

```python
import json, math, pathlib
legs = {l["name"]: l.get("ceiling") for l in json.loads(pathlib.Path("tools/gate-legs.json").read_text(encoding="utf-8"))}
def rows(p, width):
    for ln in pathlib.Path(p).read_text(encoding="utf-8").splitlines():
        f = ln.split("\t")
        if ln.strip() and not ln.startswith("#") and len(f) >= width:
            yield f
floor, frac = next((int(f[0]), float(f[1])) for f in rows("tools/run-gates/ceiling-margin.txt", 2) if f[0].isdigit())
ev = {f[0]: float(f[1]) for f in rows("tools/run-gates/ceiling-evidence.txt", 5)}
for n in ("step-gate", "docs", "upgrade-walk", "routed commits name a specced unit", "spec tokens (a spec's own names resolve)"):
    c, m = legs[n], ev.get(n)
    if m is None:
        print(n, c, "unbacked")
        continue
    need = m + max(floor, frac * m)
    ok = isinstance(c, int) and c >= need
    print(n, c, f"{m:.1f}", f"{need:.1f}", f"{c - need:.1f}", "ok" if ok else "SHORT",
          "least" if c == 10 * math.ceil(need / 10) else "not-least")
print("ALL-SHORT", [k for k, v in legs.items() if k in ev and (not isinstance(v, int) or v < ev[k] + max(floor, frac * ev[k]))])
```

The budget probe, for AC4. It applies the forward predicate to the two files and prints the row's
budget beside the value the file's rule gives:

```python
import json, math, pathlib
text = pathlib.Path("tools/run-gates/selftest-budgets.txt").read_text(encoding="utf-8")
rows = {f[0]: f for f in (ln.split("\t") for ln in text.splitlines() if ln.strip() and not ln.lstrip().startswith("#"))}
held = [l["name"] for l in json.loads(pathlib.Path("tools/gate-legs.json").read_text(encoding="utf-8"))
        if l.get("subject") == "kit" or l.get("chunk") == "selftests"]
ev = {f[0]: float(f[1]) for f in (ln.split("\t") for ln in pathlib.Path("tools/run-gates/ceiling-evidence.txt").read_text(encoding="utf-8").splitlines())
      if len(f) >= 5 and not f[0].startswith("#")}
print("unbudgeted", [n for n in held if n not in rows])
r = rows.get("upgrade-walk")
want = max(60, 10 * math.ceil(ev["upgrade-walk"] * 1.5 / 10))
print("upgrade-walk", r[1] if r else None, want, "argv-empty" if r and len(r) > 2 and not r[2] else "argv-set")
```

### Measured at writing time

At `83817478f`, with the close's three evidence rows in the working tree, the ceiling probe printed:

```
step-gate 60 4.4 124.4 -64.4 SHORT not-least
docs 60 2.7 122.7 -62.7 SHORT not-least
upgrade-walk 7200 7177.0 14354.0 -7154.0 SHORT not-least
routed commits name a specced unit 300 253.0 506.0 -206.0 SHORT not-least
spec tokens (a spec's own names resolve) 390 366.0 732.0 -342.0 SHORT not-least
ALL-SHORT ['routed commits name a specced unit', 'step-gate', 'docs', 'upgrade-walk', "spec tokens (a spec's own names resolve)"]
```

With the five values of §4 "The values" substituted in memory, it printed `ok least` on all five
lines, with slacks of 5.6, 7.3, 6.0, 4.0 and 8.0, and `ALL-SHORT []`. With 500 and 730 substituted
for the two older legs instead, both printed `SHORT`, so the probe can fail.

The budget probe printed `unbudgeted ['upgrade-walk']` and `upgrade-walk None 10770 argv-set`. With
§4's row appended in memory it printed `unbudgeted []` and `upgrade-walk 10770 10770 argv-empty`;
with a 7200 budget appended instead, its second line read `upgrade-walk 7200 10770 argv-empty`.

### Inventory

None minted. No leg, key, file or arm label is added. S5 adds a row to an existing declaration.

### Migration

None, and no adopter receives any of these values:

- `step-gate`, `docs` and `upgrade-walk` are registry exemptions that never travel into a target
  (`tools/govkit/registry.toml:710-720`), and so is `spec tokens (a spec's own names resolve)`
  (`:399-403`).
- `routed commits name a specced unit` ships with the memory-tree kit, but its descriptor declares
  no `ceiling` (`tools/memory-tree/kit.toml:333-339`). The deployer carries a ceiling into a target
  only where the descriptor declares one, with no fallback to gov's manifest
  (`tools/govkit/govkit.py:4221-4228`). Its descriptor-to-manifest parity check compares only a
  declared one (`:2637-2649`).
- `selftest-budgets.txt` and `ceiling-evidence.txt` are withheld from adopters as `project-owned`
  (`tools/govkit/registry.toml:680`, `:684`).

### Rollout

Live at landing, at order 16. TOOL-dSafePassage-61 also writes `tools/gate-legs.json` at order 16
and is held on TOOL-dGroundRules-13; its rows and these five lines are disjoint. A future runner
reading of a killed leg is admitted only inside `[ceiling, ceiling + 35]`
(`tools/run-gates/derive-ceilings.py:286`, `CEILING_WINDOW_S` at `:108`), so from the new values
for these legs, as for any raised ceiling.

### Files touched (estimate)

- `tools/gate-legs.json`
- `tools/run-gates/ceiling-evidence.txt`
- `tools/run-gates/selftest-budgets.txt`

### Alternatives rejected

- **A rounder ceiling, such as 180 for the two small legs or 14400 for `upgrade-walk`.** Every second
  above the least passing multiple of 10 is headroom on top of the declared headroom, a second
  margin typed into the manifest beside the one `ceiling-margin.txt` declares, and nothing records
  why it is there.
- **The least integer ceilings, 125, 123, 14354, 506 and 732.** They pass the check, but they depart
  from the multiple-of-10 shape every one of the manifest's 148 ceilings has, and from the
  TOOL-dGroundRules-87 precedent.
- **Sizing the two older legs from their pooled timeouts.** A killed run records only that the work
  reached the ceiling, a lower bound and not a duration
  (`tools/run-gates/derive-ceilings.py:219-225`), so the alone readings are the only durations on
  record.
- **A budget at the ceiling, 14360.** The budget file says the two figures are deliberately
  different (`tools/run-gates/selftest-budgets.txt:11-14`), and its own rule gives 10770.
- **The budget row's argv written out.** It would be a second copy of the manifest's command for the
  same leg, which the empty column exists to avoid (`tools/run-gates/run-selftests.sh:643-644`).
- **Re-measuring `upgrade-walk` on a quiet host first.** The evidence file is monotone
  (`tools/run-gates/ceiling-evidence.txt:7-11`), so a quieter reading cannot lower the row without
  `--reset`, and both checks grade the row as it stands. Whether a quiet run is cheaper is part of
  the owner's cost finding in §3.

## 5. Production-readiness checklist

- security: N/A — five integers and two declaration rows in gov-side files; no write path, input or
  surface.
- perf / scale: a healthy leg's run time does not move. A hung leg runs longer before its ceiling
  fires: `upgrade-walk` four hours, the two small legs about two minutes, and on every default bar
  `routed commits name a specced unit` 510 s and `spec tokens (a spec's own names resolve)` 740 s.
  §3 states the cost finding.
- error / empty / loading states: N/A — neither check's messages change.
- observability: `--check` keeps naming all five legs on its out-of-band line, since their rows are
  operator readings (`tools/run-gates/derive-ceilings.py:706-710`); a self-test sweep now grades
  `upgrade-walk` against a budget.
- risks: the two older legs are sized from readings taken alone, and timed out in the pool at their
  old ceilings, so a pooled run may still need the serial retry; a hung `upgrade-walk` on a self-test
  bar is cut by the 21600 s wall before its serial retry can finish; `upgrade-walk`'s reading was
  taken under load.
- testing: AC1's and AC4's probes, each staged red by today's files; AC2 observes the ceiling check
  itself, and §7 names the budget leg.
- migration: none.
- user docs: N/A — no page under `help/` states these ceilings or budgets, and no adopter receives
  them.

## 6. Acceptance criteria

- **AC1** — When §4's ceiling probe runs as `python <scratch>/ceiling_probe.py` from the repository
  root, it prints `step-gate 130 4.4 124.4 5.6 ok least`, `docs 130 2.7 122.7 7.3 ok least`,
  `upgrade-walk 14360 7177.0 14354.0 6.0 ok least`,
  `routed commits name a specced unit 510 253.0 506.0 4.0 ok least`,
  `spec tokens (a spec's own names resolve) 740 366.0 732.0 8.0 ok least` and `ALL-SHORT []`.
  Red when: a ceiling stays at its old value, so its line reads `SHORT not-least`, as all five did
  at `83817478f`; or an evidence row is not committed, so a clean checkout prints `unbacked` for
  `upgrade-walk` or `routed commits name a specced unit`, or 195.0 for `spec tokens`.
  figure: DERIVED at observation from the three tracked files; the printed numbers are PINNED to the
  evidence rows as of 2026-10-28, and a later `--write` that raises a row moves them.
- **AC2** — When `python tools/run-gates/derive-ceilings.py --check` runs, it exits 0, no
  `CEILING-EVIDENCE FAILED` line names any of the five legs, and its out-of-band line names all
  five.
  Red when: any of the five ceilings is under its required value, so the check prints that leg's
  `does not clear its evidenced maximum` line and exits 1.
  permission: a role agent may not run this checker (scratch-guard row G1); the main loop observes
  it.
- **AC3** — When, with the pass staged, `git diff --cached -U0 -- tools/gate-legs.json` runs, it
  shows five hunks, each one `-` and one `+` `"ceiling":` line, at the five legs' rows.
  Red when: another leg's ceiling or another field moves, so a sixth hunk or a non-`ceiling` line
  appears.
- **AC4** — When §4's budget probe runs as `python <scratch>/budget_probe.py` from the repository
  root, it prints `unbudgeted []` and `upgrade-walk 10770 10770 argv-empty`.
  Red when: the row is absent, so the first line reads `unbudgeted ['upgrade-walk']`, as at
  `83817478f`; or its budget departs from the file's rule, so the two numbers differ.
  figure: the 10770 is DERIVED from the committed evidence row at observation.
- **AC5** — When, with the pass staged, `git diff --cached -U0 -- tools/run-gates/ceiling-evidence.txt`
  runs, it shows the three hunks of §4 "The evidence rows". Two add one line each, beginning
  `routed commits name a specced unit` with `253.0` and `upgrade-walk` with `7177.0`. One replaces
  the `spec tokens (a spec's own names resolve)` row's `195.0` with `366.0`. Each added line carries
  node `a`, and no other line is removed.
  Red when: the pass ran a fresh `--write`, so another row moved; or a row was retyped with another
  node or value.

## 7. Gates

`leg ceilings clear their evidenced maximum` · `every held leg is budgeted, every budget row resolves` · `routed commits name a specced unit` · `spec tokens (a spec's own names resolve)` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `memory hygiene`

No `New arm:` line: this unit adds or moves no suite arm. Each of the first two legs' own failing
case is its arm. `leg ceilings clear their evidenced maximum` runs `derive-ceilings.py --check` on
every bar, and at `83817478f`, with the close's three evidence rows, it names all five legs.
`every held leg is budgeted, every budget row resolves` names `upgrade-walk` at `83817478f`, which
the main loop observed by a run. Those are the REDs the close recorded. The main loop observes both
legs GREEN at the close, and the two older legs complete under their new ceilings on the close's
bar. The budget leg's checker is not an acceptance token, because the spec-token join refuses its
script at command position as a suite invocation (`tools/check-spec-tokens.py:400-404`); AC4 is its
direct probe. The four legs after the two older ones are the ones whose `guard` names
`{prefix}/gate-legs.json`. The broad `{prefix}/` and `{prefix}/run-gates/` guards, the only ones
that reach the two `run-gates` files, are outside the join.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-80-1-spec-writer.md`,
  grounded at `83817478f` with the close's `upgrade-walk` evidence row in the working tree. The
  rounding is read from the manifest's own values and the TOOL-dGroundRules-87 precedent, not
  chosen. The cost finding in §3 was derived by reading `run-selftests.sh`'s forward check and
  applying its predicate to the two files; no gate was run.
- rev-2 · 2026-10-28 · §1 · S4 · S5 · §3 · §4 · §5 · AC1 · AC4 · AC5 · §7 · §10 · the
  coordinator's hand-off during this dispatch, under M10. It confirmed by a run that
  `run-selftests.sh --check` at the head names `upgrade-walk`, this build's own red. It directed
  this unit to adopt the budget row (S5, AC4) rather than file it as an ask, and to carry the
  close's uncommitted evidence row as a declared write (S4, AC5), so AC1 reads a committed row. The
  row stays as written, node `a` included. §3's finding keeps only the cost options; §7 gains the
  budget leg and says why its checker is not an acceptance token.
- rev-3 · 2026-10-28 · §1 · S1 · S3 · S4 · S6 · S7 · §3 · §4 · §5 · AC1 · AC2 · AC3 · AC5 · §7 ·
  the coordinator's second hand-off during this dispatch. Two legs that timed out twice in the
  discovery bar's pool, `routed commits name a specced unit` and
  `spec tokens (a spec's own names resolve)`, join the unit (S6, S7). Each was read alone on a
  frozen clone of `83817478f` and written by `--write --observed` under `GOV_NODE=a`, so S4 and AC5
  now carry three evidence rows. The margin rule and multiple-of-10 rounding give 510 and 740, the
  values the coordinator expected. AC1 and AC3 widen to five legs. The evidence row line numbers of
  S1 and S3 moved with the added rows. §4 "Migration" adds why neither new value reaches an
  adopter, and §7 names both legs.
- rev-4 · 2026-10-28 · §3 · §4 · §5 · AC2 · §7 · §10 · the coordinator's third hand-off during this
  dispatch. The spec-token checker resolved the bare citation of the run-gates README to the
  repository root's 119-line file. It now reads `tools/run-gates/README.md:603-606`, and every other bare
  `file:line` citation is spelled with its full path, so none resolves against the root.

## 10. Reuse audit

No code is written, so the seams are the existing ones, extended by value only. The first is the
`ceiling` field of `tools/gate-legs.json`, graded by `cmd_check` in
`tools/run-gates/derive-ceilings.py:643-719` against `tools/run-gates/ceiling-evidence.txt` and
`tools/run-gates/ceiling-margin.txt`. The second is the budget declaration
`tools/run-gates/selftest-budgets.txt`, read by `read_population` in
`tools/run-gates/run-selftests.sh:648-716`, whose empty-argv form takes the command from the
manifest. The ceiling sizing follows TOOL-dGroundRules-87's rule
(`memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-87.md:114-122`), and the budget
follows the file's own calibration line.
`python tools/codebase-map/reuse_lookup.py "raise a gate leg ceiling in the leg manifest so it clears its evidenced maximum by the declared margin"`
ranked name-token seams (`legs`, `leg`, `manifest`) and `load_manifest` in
`tools/run-gates/held_halves.py`; none sizes a ceiling or a budget, so no further seam fits. The
recall probe ranked TOOL-cMendedVintage-17, the ruling that a ceiling may be raised from a reading
taken outside the runner (`memory/DECISIONS.md:205`), TOOL-dGroundRules-87, whose rounding this unit
takes, and a TOOL-dDerivedDocket-6 review line separating the margin's headroom from the budget
file's x1.5. `python tools/memory-tree/gotchas.py --for-paths tools/gate-legs.json` selected only
universal classes, and `gen_build_index.py --asks --path tools/gate-legs.json` listed no open ask on
these legs.

Recall terms used: `python tools/memory-recall/query.py "how is a leg ceiling raised after its evidence row reds the ceiling check" --terms "ceiling evidence margin headroom derive-ceilings observed gate-legs raise leg killed budget"`
