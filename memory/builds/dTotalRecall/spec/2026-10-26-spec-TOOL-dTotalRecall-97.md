# TOOL-dTotalRecall-97 — the C5 classifier's input is extracted from unit 80's ledger by a stated rule, and every read line it cannot place is counted

**Status:** DEFERRED · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 38 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 89 to 92
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md`)
confirmed finding **id 30 at HIGH**, its item **H3**, which it shares with id 12 (HIGH, taken by
`TOOL-dTotalRecall-96`). The report files it under the class `parser-drops-rows-it-cannot-place`.

`TOOL-dTotalRecall-91` §4 "The classifier" keeps only lines that begin with `<label> ` and are an
`rc=` line or a failure line, and drops every other line without a word. Its §2 S3 runs it over "the
`p69` and `p69^` lines unit 80's acceptance ledger recorded" and states no rule for lifting them out
of that ledger, and `TOOL-dTotalRecall-80` fixes no ledger format. The report ran the classifier
verbatim: a read whose check-5 line is indented printed `C5 passed`, because the indented line was
dropped. A read recorded as a bullet, inside backticks or inline in a sentence is dropped the same
way.

This unit states the extraction and counts what it cannot place. §4's `c5_input` lifts a label's read
lines out of a ledger whatever bullet, quote, backtick or indent wraps them, keeps each distinct
placed line once, and counts every other line that names the label's status or a failure as
unplaced. `TOOL-dTotalRecall-96` classifies only its output and reads any unplaced line as
not-evaluated. It repairs `TOOL-dTotalRecall-91`, at order 38, one above that unit's 37.

## 2. Scope (IN)

- **S1** — The extraction. §4's `c5_input` takes a ledger file and a label and prints the label's
  placed lines, each once, then `<label> unplaced <n>`. A placed line is, once leading whitespace,
  `-`, `*`, `>` and backticks and trailing whitespace and backticks are stripped, exactly
  `<label> rc=<n>` or `<label> MANIFEST check <n> FAILED...`, the two shapes
  `TOOL-dTotalRecall-77`'s `read_checker` prints. Observed by AC1.
- **S2** — The count. A stripped line that begins with `<label> ` and is not placed, or a line naming
  `<label> rc=` or `<label> MANIFEST check` after its start, adds one to `unplaced`. Observed by AC1.
- **S3** — Unit 80's ledger, extracted. `c5_input` runs over unit 80's acceptance ledger for `p69` and
  `p69^` at this pass's base, and this unit's ledger records both outputs verbatim in a fenced block,
  the input `TOOL-dTotalRecall-96` classifies. Observed by AC2.

## 3. Non-goals (OUT)

- The classifier's rows, including a status that disagrees with the failure lines (item H3, id 12):
  `TOOL-dTotalRecall-96`, which also answers unit 69's AC1 and writes any record.
- A parse failure on a real read being turned into an unresolved answer and a record of unit 69
  (item M3, id 6): the batch `TOOL-dTotalRecall-100`.
- Running the checker again. The reads are unit 80's, recorded by the main loop, and no role agent may
  run that leg (`.claude/roles.json`).
- Editing spec 80's or spec 91's text, each frozen once its unit builds.
- The checklist entry the report suggests as the left-shift gate: the close's left-shift step
  (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dTotalRecall-80` — its acceptance ledger, which holds the `p69` and `p69^` reads this unit extracts
- **consumes-from** `TOOL-dTotalRecall-77` — `read_checker`'s two line shapes, `<label> rc=<n>` and the labelled failure line, which define a placed line
- **hands-off** `TOOL-dTotalRecall-96` — `c5_input` and the extracted reads in this unit's ledger, the only input that unit's classifier reads
- **hands-off** `TOOL-dTotalRecall-100` — `c5_input`, through which that batch re-reads unit 91's parse of unit 80's ledger for id 6

## 4. Design

### The extraction

```bash
# run from the repository root; PY is the launcher tools/lib/resolve-python.sh resolves
c5_input() {  # ledger file · label -> the label's distinct placed lines, then "<label> unplaced <n>"
  "$PY" - "$@" <<'PROBE'
import re, sys
path, label = sys.argv[1], sys.argv[2]
lab = re.escape(label)
placed, unplaced = [], 0
for raw in open(path, encoding='utf-8'):
    line = re.sub(r'[\s`]+$', '', re.sub(r'^[\s>*`-]+', '', raw))
    if re.fullmatch(lab + r' (?:rc=\d+|MANIFEST check \d+ FAILED.*)', line):
        if line not in placed:
            placed.append(line)
    elif line.startswith(label + ' ') or re.search(r'(?:^|[\s`(])' + lab + r' (?:rc=|MANIFEST check )', raw):
        unplaced += 1
for line in placed:
    print(line)
print(label, 'unplaced', unplaced)
PROBE
}
```

A line quoted twice, once in a fenced block and once in a bullet, is one read and is kept once. Two
different status lines under one label both survive, and `TOOL-dTotalRecall-96` reads them as
contradictory. A label matches only with its following space, so `p69` never reads a `p69^` line.

### The fixture

```bash
cat > "$SCRATCH/ledger97.md" <<'LEDGER'
# a fixture ledger
y rc=1
  y MANIFEST check 5 FAILED — watched files changed since last-audit
p69 rc=0
- `p69 rc=0`
- AC2: read `v rc=1` and `v MANIFEST check 5 FAILED`
k rc=1 trailing
u rc=0
u NOTE: memory/guides/SESSION-KICKOFF.md carries no kickoff-manifest marker
LEDGER
```

PINNED, measured 2026-10-26 at `32febccb6` with these exact lines: `c5_input` printed, for `y`, both
of its lines and `y unplaced 0`; for `p69`, `p69 rc=0` once and `p69 unplaced 0`; for `v`, only
`v unplaced 1`; for `k`, only `k unplaced 1`; for `u`, `u rc=0` and `u unplaced 1`; and for `none`,
`none unplaced 0`. The classifier of `TOOL-dTotalRecall-96` over the `y` output printed `y C5 failed`,
where unit 91's classifier over the raw lines printed `passed`.

### Why order 38

Unit 91 classifies at order 37. `TOOL-dTotalRecall-96` shares order 38 and consumes this unit, so the
dispatch verb holds it until this unit is CLOSED (`tools/unattended/unattended.sh:13691-13698`).

### Inventory

Minted: the function `c5_input`, spec text only. No record is written. Naming cell: none, no product
symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger)

### Alternatives rejected

- **Read only the lines of a fenced block in unit 80's ledger.** The report's first option. Spec 80
  fixes no format, so a ledger that records the reads as bullets would yield no line and an answer of
  "no status"; stripping the wrapping reads every form and still counts what it cannot place.
- **Drop unplaced lines, as unit 91 does.** That is the defect: a dropped failure line reads as a
  clean read.

## 5. Production-readiness checklist

- security — no surface.
- perf / scale — one pass over one ledger per label.
- error / empty / loading states — a ledger with no line for the label prints `<label> unplaced 0`
  alone, which the classifier reads as no status; any unplaced line is counted and never dropped.
- observability — the extracted lines are recorded verbatim beside the unplaced count.
- risks — a prose sentence naming `p69 rc=` is counted unplaced, which errs toward not-evaluated and
  never toward green.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `c5_input "$SCRATCH/ledger97.md" <label>` runs for `y`, `p69`, `v`, `k`, `u` and
  `none`, it prints the lines §4 pins, among them both `y` lines with `y unplaced 0`, `v unplaced 1`
  and `u unplaced 1`.
  Red when: an indented failure line is dropped, an inline or trailing read line is not counted, or a
  quoted duplicate is kept twice.
  fixture: the ledger is made in the run's scratch by the pass; the tree holds none.
  figure: the outputs are PINNED in §4, measured 2026-10-26.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-97" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC2 line names unit 80's acceptance ledger by path and holds the verbatim
  output of `c5_input` for `p69` and for `p69^` over it, each ending in its `unplaced` line.
  Red when: either output is paraphrased or its `unplaced` line is missing.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is `c5_input` over a scratch ledger and over unit 80's ledger.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 89 to 92, id 30
  (HIGH, item H3, shared with id 12).

## 10. Reuse audit

The seam is `TOOL-dTotalRecall-77`'s `read_checker`, whose two printed line shapes are the only
placed lines, and the classifier of `TOOL-dTotalRecall-91`, which this extraction feeds through
`TOOL-dTotalRecall-96`. `python tools/codebase-map/reuse_lookup.py "run a checker at each historical commit in a scratch worktree"`
ranked `add_scratch_worktree` among its SEAM candidates and nothing that lifts recorded read lines
out of a ledger. The recall query below found this audit's item H3, spec 91's classifier, spec 80's
ledger criteria and the class `parser-drops-rows-it-cannot-place`. No existing seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how are a checker's recorded read lines lifted out of a ledger so no line is dropped" --terms "read_checker p69 ledger extraction unplaced line indented bullet backtick c5_of manifest-check rc failure"`
