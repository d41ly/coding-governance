# TOOL-dGroundRules-63 — the closing review's minors: unit 46's population re-measured with units 44 and 45, a packet join for each live chain run, and the owner-cap record's count named by range, one scope item each

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 20 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-63-deviation-51.md](../build/2026-10-23-build-TOOL-dGroundRules-63-deviation-51.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-53-closing-promotions-brief.md) | research | TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-61-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-61-task.md) | research | TOOL-dGroundRules-61 TOOL-dGroundRules-62 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of the spec run
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`)
confirmed two MEDIUM items and one LOW item beside its four HIGHs. BUILD-METHOD M4 batches them into
one unit, and this is that unit: M1 (ids 6, 15 and 21), the left-shift gate of M2 (id 22; the
packet's re-render itself is the main loop's close step), and L1 (ids 7, 11, 18 and 23). A finding
the review merged with another into one item still takes its own scope item here, named by its own
id, and each item's left-shift is a scope item of its own. They write `tools/check-spec-tokens.py`,
one record of this build and two bug-class records, so they share no write set with units 61 and 62.
The unit repairs `TOOL-dGroundRules-46`, which sits at order 14, and its criteria need units 34, 40,
44 and 45 terminal, so it builds at order 20, after every unit the closing review's promotions
repair.

| Finding id | Severity | Review item | Lands on | Scope item | Criterion |
|---|---|---|---|---|---|
| 6 | MEDIUM | M1 | unit 46, Rollout and AC3's fixture | S1 | AC1 |
| 15 | MEDIUM | M1 | unit 46, Goal and Evidence | S2 | AC2 |
| 21 | MEDIUM | M1 | unit 46, the cutoff-key non-goal | S3 | AC3 |
| 22 | MEDIUM | M2, its left-shift gate | `tools/check-spec-tokens.py` | S4 | AC4, AC5, AC6, AC7 |
| 7 | LOW | L1 | the owner-cap record | S5 | AC8 |
| 11 | LOW | L1 | the owner-cap record | S6 | AC9 |
| 18 | LOW | L1 | the owner-cap record | S7 | AC10 |
| 23 | LOW | L1 | the owner-cap record | S8 | AC11 |
| 6, 15, 21 | MEDIUM | M1, its left-shift | a bug-class record | S9 | AC12 |
| 7, 11, 18, 23 | LOW | L1, its left-shift | a bug-class record | S10 | AC13 |

Each item's fix is the one the review's skeptic judged sound. Where the review offered options, §8
records the pick.

## 2. Scope (IN)

- **S1** — Finding 6. `TOOL-dGroundRules-46`'s Rollout and AC3 fixture say its join meets no live
  hit because only units 34 and 40 carry the bare form. Its own predicate also hits units 44 and 45,
  which sit at its order and were written in the same commit. This unit observes 46's AC3 at its
  own close, where units 34, 40, 44 and 45 are terminal by their orders: the spec-tokens checker's
  `--list` over the built tree prints no `[source]` hit. Observed by AC1.
- **S2** — Finding 15. The Goal's "hits exactly the two" and §4 Evidence, measured at `0ced625e1`
  before units 44 and 45 existed, are re-measured at `7810198ad`, the commit that carries units 44 to
  52: the predicate finds nine source commands in acceptance sections and four bare ones, units 34
  (`:509`), 40 (`:129`), 44 (`:129`) and 45 (`:124`) (§4 Evidence, PINNED). Observed by AC2.
- **S3** — Finding 21. 46's non-goal of a cutoff key holds only while every unit carrying a hit is
  terminal when the join is graded. This unit asserts it: at its commit the status headers of units
  34, 40, 44 and 45 read `CLOSED` or `WONTDO`. Observed by AC3.
- **S4** — Finding 22, the left-shift gate of M2. `tools/check-spec-tokens.py` gains a join,
  `packet`, over every chain build whose run is live in the tree: a build holding a file matching
  `memory/builds/*/prompts/*-prompt-PLAY-dClosedLoop-1-packet.md` whose `RUN.md` exists and whose
  last `phase:` line is not `LANDED`, `ABORTED` or `LANDING`. For each one the join runs the packet
  instrument's `--check <slug>` from the root, and any exit but 0 is a hit naming the build, the exit
  and the instrument's summary line, its first line of output. Every run prints
  `spec-tokens: packet join · <n> live chain run(s) · <m> packet(s) checked`, and with the
  instrument absent from the tree the join prints that it is off and grades nothing. The module
  docstring names the join and what it does not see (§4). Observed by AC4, AC5, AC6, AC7.
- **S5** — Finding 7. The owner-cap record's application line, which counts "the forty-one the
  audit promoted" against its own round list summing to forty, names the units by id range and
  spells no count (§4, the record's line). Observed by AC8.
- **S6** — Finding 11. Every id the record's ranges name is an id of the build README's roster, so
  the record, the README index and `RUN.md` agree. Observed by AC9.
- **S7** — Finding 18. The deferral line carries no spelled-out count from which a reconciliation
  would expect fifty-two units. Observed by AC10.
- **S8** — Finding 23. The eleven units the README opened with are named as the range
  `TOOL-dGroundRules-1` to `TOOL-dGroundRules-11`. Observed by AC11.
- **S9** — M1's left-shift. `memory/gotchas/observation-before-the-last-fold-of-the-same-commit.md`
  gains the population form, with this instance in "Where it bit": a gate unit's §4 population claim,
  measured before the same disposal commit wrote siblings at its order, is re-measured at the spec's
  own commit, and a disposal re-runs each new gate unit's predicate over its own output before it
  commits. Observed by AC12.
- **S10** — L1's left-shift. `memory/gotchas/two-answers-to-one-question.md` gains the count form: an
  authority record that states a population names it by id range, never by a spelled-out count,
  because a count beside a derived roster is a second answer nobody re-derives. Observed by AC13.
- **S11** — The generated indexes. `python tools/memory-tree/gotchas.py --write` regenerates
  `memory/gotchas/INDEX.md`, and `python tools/codebase-map/gen_map.py --write` regenerates
  `memory/map/generated/` for the join's new function. Observed by AC12, AC14.

## 3. Non-goals (OUT)

- Re-rendering any packet, this build's included: the M2 fix proper is the main loop's close step,
  and another build's packet is this build's non-goal.
- The join over every open chain build's packet (§8 F1).
- Editing `TOOL-dGroundRules-46`'s text. Its defects are closed here, in the criteria they govern,
  and its §3 names this unit.
- Running a spec literal from a gate: `TOOL-dGroundRules-46` §3 keeps it out, and the packet join
  runs one instrument the tree pins, never spec text.

### Edges

- **consumes-from** `TOOL-dGroundRules-46` — its bare-source join, whose Goal, Evidence, Rollout and AC3 fixture S1 to S3 re-measure and observe, and its count-line convention, which S4's join follows

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23.

- The predicate of `TOOL-dGroundRules-46` §4, run over the acceptance section of every spec under
  `memory/builds/*/spec/` at `7810198ad` by the `REMEASURE` literal of §6, found 1445 spec files,
  nine source commands and four bare operands, `34:509`, `40:129`, `44:129` and `45:124`, each
  `lib-unattended.sh`; at `0ced625e1` it found two, `34:509` and `40:125` (PINNED).
- `packet.py --check` was run for each of the 22 chain builds holding a packet at `7810198ad`. Every
  one was byte-red at the as-built view's line, and dGroundRules' also carried 40 roster findings for
  `TOOL-dGroundRules-65` to `TOOL-dGroundRules-52` (PINNED). One check of dGroundRules took 20
  seconds on node d.
- `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py:100` declares
  `TERMINAL = ("LANDED", "ABORTED")`, and `:541-556` reads a chain build's last `phase:` line; a
  LANDING record is terminal only when `read_landed_derivation` (`:510-538`) asks the remote.
- The execution plan's "Keeping a packet current"
  (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:989-1006`)
  has each build's own runs re-render its packet, and forbids a run to write another build's.
- At `7810198ad` the RUN.md of dGroundRules reads phase `REVIEWING` and dTrueNorth's reads
  `LANDING`; no other chain build has one.
- The leg `spec tokens (a spec's own names resolve)` carries no guard in `tools/gate-legs.json`, so it
  runs on every bar; `tools/unattended/unattended.test.sh:6561` records that govkit's registry
  exempts `check-spec-tokens.py` from every adopter.
- The owner-cap record's line 10 lists rounds promoting 9, 4, 7, 2, 9 and 9 units, and its line 16
  says "the forty-one the audit promoted".

### The packet join

```text
PACKET_INSTRUMENT = memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py
LIVE_EXCLUDED     = ("LANDED", "ABORTED", "LANDING")

(after the spec walk):
    if PACKET_INSTRUMENT is not tracked: print "packet join · off · no packet instrument"; grade nothing
    for each slug with a packet under memory/builds/<slug>/prompts/ and a memory/builds/<slug>/RUN.md:
        phase = the last "phase: <word>" line of that RUN.md
        if phase is absent or in LIVE_EXCLUDED: continue
        live += 1; rc, out = run [sys.executable, PACKET_INSTRUMENT, "--check", slug] from the root
        checked += 1
        if rc != 0: hits.append((packet path, "packet", slug, f"packet.py --check exited {rc}: {summary}"))
    print the S4 count line
```

A LANDING record is left out, rather than derived as the instrument derives it, because that
derivation asks the remote, and a join on an unguarded leg must not read the network on every bar; a
run's packet is graded while the run is live, at its `--prepare` included, before its LANDING record
is written. A hit is waivable by the waiver registry like every other join's, and this unit adds no
row.

The docstring states what the join does not see: a LANDING record's packet, a run whose `RUN.md`
this tree does not hold, and anything the instrument itself does not check, which its own
docstring lists.

### The record's line, after S5 to S8

```text
- Every unit of the roster, TOOL-dGroundRules-1 to TOOL-dGroundRules-11 as the README opened with
  them, TOOL-dGroundRules-65 to TOOL-dGroundRules-52 as the audit promoted them, and each unit the
  closing review promotes, is deferred against TOOL-dGroundRules-12 and carried forward to the build
  run, which builds them (README rule 1).
```

Each range sits whole on one line, as AC8 and AC11 grep it. The owner's quoted prompt and the
record's other lines are unchanged.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `scan_live_packets` | py.function, lexicon `--suggest` OK on 2026-10-23 | `tools/check-spec-tokens.py` |
| `packet join` | a report line | `tools/check-spec-tokens.py` |

### Files touched (estimate)

- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-1-owner-audit-cap.md`
- `memory/gotchas/observation-before-the-last-fold-of-the-same-commit.md`
- `memory/gotchas/two-answers-to-one-question.md`
- `memory/gotchas/INDEX.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **A new leg running the instrument over every chain build.** §8 F1.
- **Folding the M1 restatement into `TOOL-dGroundRules-46`'s text.** Nothing is folded at this exit
  (BUILD-METHOD M4); the criterion moves here and 46's §3 names the move.

## 5. Production-readiness checklist

- security — the join runs one tracked instrument with a fixed argv and reads nothing it runs; it
  writes nothing.
- perf / scale — about 20 seconds per live chain run on the `spec tokens` leg, measured on node d,
  and usually one run is live; if the leg's ceiling trips, `tools/run-gates/derive-ceilings.py`
  re-derives it.
- error / empty / loading states — the count line names zero live runs; an absent instrument prints
  the join off; an instrument exit of 2, nothing to check, is a hit, since every member holds a
  packet.
- observability — each hit names the build, the exit and the instrument's summary line, which says
  which arm went red.
- risks — a live run whose packet is red reds the bar until its own run re-renders it, which is the
  intent; a red pin arm is a stop the hit names, never re-rendered away.
- testing — AC1 to AC14 and the `New arm:` line under §7.
- migration — the gotcha index and the codebase map regenerated.
- user docs — N/A: a gov-only checker whose docstring is its reference, and one record of this build.

## 6. Acceptance criteria

Every command runs from the repository root unless it says otherwise. The literals the criteria run
are spelled whole here, once. `REMEASURE`, `STATUS_PROBE`, `DEFER_WORDS` and `ROSTER_JOIN` read only
tracked files and were run verbatim from the root on 2026-10-23 at `7810198ad`; the rest need the
built join:

```text
LIST         = python tools/check-spec-tokens.py --list
REMEASURE    = python - 7810198ad <<'EOF'
import re, subprocess, sys
rev = sys.argv[1]
cmd = re.compile(r"""(?:^|[;&|('"]|\s)(?:\.|source)\s+([^\s;&|'"()]+\.sh)\b""", re.M)
ls = subprocess.run(["git", "ls-tree", "-r", "--name-only", rev, "--", "memory/builds/"],
                    capture_output=True, text=True).stdout.split()
for f in (f for f in ls if "/spec/" in f and f.endswith(".md")):
    t = subprocess.run(["git", "show", f"{rev}:{f}"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace").stdout
    m = re.search(r"^## 6\. Acceptance criteria\n(.*?)(?=^## 7\.)", t, re.S | re.M)
    for h in (cmd.finditer(m.group(1)) if m else ()):
        if "/" not in h.group(1):
            print(f"{f.rsplit('-', 1)[1][:-3]}:{t[:m.start(1) + h.start(1)].count(chr(10)) + 1} {h.group(1)}")
EOF
STATUS_PROBE = grep -m1 -h "^\*\*Status:\*\*" memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-34.md memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-40.md memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-44.md memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-45.md
SCRATCH      = a git clone of this repository under %TEMP%/gr63, checked out at the commit under test
PACKET       = memory/builds/dGroundRules/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md
RUN_LIVE     = in SCRATCH, the line "phase: BUILDING" appended to memory/builds/dGroundRules/RUN.md, committed
RUN_DONE     = in SCRATCH, the line "phase: LANDED" appended to the same file, committed
STALE        = in SCRATCH, the line "stale" appended to PACKET, committed
RECORD       = memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-1-owner-audit-cap.md
DEFER_WORDS  = python -c "import re; t=open('memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-1-owner-audit-cap.md',encoding='utf-8').read(); b=re.search(r'^- Every unit of the roster.*?(?=^- |\Z)',t,re.M|re.S).group(0); print(len(re.findall(r'(?i)\b(eleven|forty|fifty)',b)))"
ROSTER_JOIN  = python -c "import re; r=open('memory/builds/dGroundRules/README.md',encoding='utf-8').read(); ids=set(re.search(r'^ids: (.*)$',r,re.M).group(1).split()); t=open('memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-1-owner-audit-cap.md',encoding='utf-8').read(); print(*[f'TOOL-dGroundRules-{n}' for a,b in re.findall(r'TOOL-dGroundRules-(\d+) to TOOL-dGroundRules-(\d+)',t) for n in range(int(a),int(b)+1) if f'TOOL-dGroundRules-{n}' not in ids])"
```

- **AC1** — When `LIST` runs on the built tree at this unit's commit, it prints no `[source]` hit.
  Red when: a live spec still carries a criterion that sources a shell file by bare name, and
  `TOOL-dGroundRules-46` AC3 stays red on a correct build of 46.
- **AC2** — When `REMEASURE` runs, it prints exactly four lines: `34:509`, `40:129`, `44:129` and
  `45:124`, each naming `lib-unattended.sh`.
  Red when: the measurement leaves out a sibling the same disposal commit wrote.
  figure: the four are PINNED at `7810198ad`.
- **AC3** — When `STATUS_PROBE` runs at this unit's commit, each of its four lines reads `CLOSED` or
  `WONTDO` after `**Status:**`.
  Red when: one of the four is live, and 46's join reds a spec of this build that its non-goal said
  would be terminal.
- **AC4** — When `RUN_LIVE` and `STALE` run, and `LIST` runs in `SCRATCH`, it prints a `[packet]` hit
  naming `dGroundRules` and `byte compare red`.
  Red when: a live run's red packet is graded by no join, which is how the spec run landed with its
  entry check red (review id 22).
- **AC5** — When `RUN_LIVE` runs alone and `LIST` runs in `SCRATCH`, it prints no `[packet]` hit, and
  the `packet join ·` count line names at least one live chain run.
  Red when: a packet green at its own render is read as red.
  figure: the counts are DERIVED at observation time.
- **AC6** — When `RUN_DONE` and `STALE` run, and `LIST` runs in `SCRATCH`, it prints no `[packet]`
  hit naming `dGroundRules`.
  Red when: a landed build's packet, which its own runs no longer keep, reds the bar.
- **AC7** — When `LIST` runs on the built tree at this unit's commit, it prints the `packet join ·`
  count line and no `[packet]` hit.
  Red when: the build run reaches this unit with its own packet red.
- **AC8** — When `grep -c "forty-one" memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-1-owner-audit-cap.md`
  runs it prints `0`, and `grep -c "TOOL-dGroundRules-65 to TOOL-dGroundRules-52"` over `RECORD`
  prints `1`.
  Red when: the record still counts the promoted units against its own round list.
- **AC9** — When `ROSTER_JOIN` runs, it prints an empty line.
  Red when: a range the record names holds an id the README's roster does not.
- **AC10** — When `DEFER_WORDS` runs, it prints `0`.
  Red when: the deferral bullet still spells a count a reconciliation would read; over the record
  as it stands at `7810198ad` it prints `2`.
- **AC11** — When `grep -c "TOOL-dGroundRules-1 to TOOL-dGroundRules-11"` runs over `RECORD`, it
  prints `1`.
  Red when: the opened units are still named by a count.
- **AC12** — When `grep -c "TOOL-dGroundRules-46" memory/gotchas/observation-before-the-last-fold-of-the-same-commit.md`
  runs it prints `1` or more, and `python tools/memory-tree/gotchas.py --check` exits 0.
  Red when: the class gains no population form, or the generated index is stale.
- **AC13** — When `grep -c "id range" memory/gotchas/two-answers-to-one-question.md` runs it prints
  `1` or more.
  Red when: the count form is not recorded where the next authority record's author is handed it.
- **AC14** — When `python tools/codebase-map/gen_map.py --check` runs at this unit's commit it exits 0.
  Red when: the map does not carry the join's new function.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `memory-hygiene self-test` · `build-index selftest` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `gotchas selftest` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/check-spec-tokens.test.sh · covers AC4 AC6 · a scratch repository holding a stub at the packet instrument's path that exits 1 printing a finding, and one chain build's packet and RUN.md, its last phase BUILDING and then LANDED · that suite's assertion count, raised by the arm

## 8. Open questions

- **F1 — Which packets does the left-shift gate grade, and where does it live?** (a) The review's
  wording: a new leg running the instrument's `--check` for every open chain build, guarded on the
  as-built view, a README roster or a packet. (b) A join in `tools/check-spec-tokens.py` over each
  chain build whose run is live in the tree, which grades a run's own packet, the one that run may
  write. (c) The same population as (b) in a new guarded leg with its own suite. (d) A checklist
  entry only. (a) lands red: every one of the 22 packets is byte-red at `7810198ad` (§4 Evidence),
  each build's own runs re-render its packet, and re-rendering another build's packet is this build's
  non-goal, so the leg fails at its own commit (veto 1). (d) leaves a class a gate can see to prose,
  where M8 asks for the gate. (b) and (c) grade the same population and meet the same criteria;
  tie-break, reuse of a seam M5 found: (b), which reuses the checker's walk, its count-line
  convention, its waiver registry, its suite and its leg. Recommendation (b). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (b). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting the closing diff review's M1 (ids 6, 15, 21), M2's
  left-shift gate (id 22) and L1 (ids 7, 11, 18, 23) in one batch, from the skeptic's sound fixes,
  with unit 46's predicate re-run at `7810198ad` and every chain packet checked on 2026-10-23.
- rev-2 · 2026-10-23 · §4 §6 · TOOL-dGroundRules-13 renamed TOOL-dGroundRules-65 by the owner's ruling, the id a landed dSafePassage ask holds; nothing else moved.

## 10. Reuse audit

The seams extended are `tools/check-spec-tokens.py`, whose spec walk, count lines and waiver
registry every join shares and which `TOOL-dGroundRules-46` already extends with the bare-source
join this unit re-measures; the packet instrument's own `--check`, run as its CLI states rather than
re-derived; and two bug-class records, widened rather than new. `python
tools/codebase-map/reuse_lookup.py "check the packet of each chain build whose run is live"` ranked
name-stem matches only (`run`, `check`, `live`, `build`), none of which reads a packet, so no
existing code seam fits the population scan itself. The recall probe returned the open asks
`PLAY-dClosedLoop-24` and `PLAY-dClosedLoop-26` and the decision `PLAY-dClosedLoop-27`. The first
records that a view re-render reds every other chain packet, which §4 measured again. The other two
record that a LANDING record reads as terminal only through the remote, which is why S4 leaves
LANDING out rather than derive it.

Recall terms used: `python tools/memory-recall/query.py "how is a chain build packet kept green
before the build run's first pass" --terms "packet.py check byte compare as-built view re-render pin
arm roster Obligations stale packet first pass"`
