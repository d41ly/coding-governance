# TOOL-dTotalRecall-97 — the C5 classifier's input is extracted from unit 80's ledger by a stated rule, and every read line it cannot place is counted

**Status:** DEFERRED · rev-2 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 38 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-97-deviation-971.md](../build/2026-10-26-build-TOOL-dTotalRecall-97-deviation-971.md) | deviation | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-97-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-97-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-97-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-97-reground-spec-writer.md) | log | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 89 to 92
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md`)
confirmed finding **id 30 at HIGH**, its item **H3**, which it shares with id 12 (HIGH, taken by
`TOOL-dTotalRecall-96`). The report files it under the class `parser-drops-rows-it-cannot-place`.

`TOOL-dTotalRecall-91` §4 "The classifier" keeps only lines that begin with `<label> ` and are an
`rc=` line or a failure line, and drops every other line without a word. The report ran it verbatim: a
read whose check-5 line is indented printed `C5 passed`, because the indented line was dropped. A read
recorded as a bullet, inside backticks or inline in a sentence is dropped the same way. Unit 91 rev-3
keeps that classifier and leaves the wrapped lines to this unit.

One premise of the finding has moved. Unit 80 rev-4 fixes its ledger's format: its S1 holds both reads
verbatim in one fenced block and spells a read line nowhere else. Nothing yet checks that the ledger
keeps that form, and this unit's count is that check.

This unit states the extraction and counts what it cannot place. §4's `c5_input` lifts a label's read
lines out of a ledger whatever bullet, quote, backtick or indent wraps them, keeps each distinct
placed line once, and counts every other line that names the label's status or a failure as
unplaced. `TOOL-dTotalRecall-96` classifies only its output and reads any unplaced line as
not-evaluated. It repairs `TOOL-dTotalRecall-91`, at order 38, one above that unit's 37.

## 2. Scope (IN)

- **S1** — The extraction. §4's `c5_input` takes a ledger file and a label and prints the label's
  placed lines, each once, then `<label> unplaced <n>`. A placed line names one read of the label and
  is, once leading whitespace, `-`, `*`, `>` and backticks and trailing whitespace and backticks are
  stripped, exactly `<label> rc=<n>` or `<label> MANIFEST check <n> FAILED...`, the two shapes
  `TOOL-dTotalRecall-77`'s `read_checker` prints. Observed by AC1.
- **S2** — The count. Every other line that begins with `<label> ` once stripped, or names
  `<label> rc=<n>` or `<label> MANIFEST check <n>` anywhere, adds one to `unplaced`. A line holding two
  reads is one of them, whatever it begins with. A mid-line `<label> rc=` with no digit is prose,
  not a read: unit 80's AC1 spells it so. Observed by AC1.
- **S3** — Unit 80's ledger, extracted. `c5_input` runs over unit 80's acceptance ledger, the one file
  §4 "The answer" lists, for `p69` and `p69^` at this pass's base. This unit's ledger records both
  outputs verbatim in one fenced block, beside the path read. `TOOL-dTotalRecall-96` makes the run
  again and classifies it. Observed by AC2.

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
# run from the repository root
. tools/lib/resolve-python.sh; PY=$(resolve_python) || exit 2
c5_input() {  # ledger file · label -> the label's distinct placed lines, then "<label> unplaced <n>"
  "$PY" - "$@" <<'PROBE'
import re, sys
path, label = sys.argv[1], sys.argv[2]
lab = re.escape(label)
read = re.compile(r'(?<!\w)' + lab + r' (?:rc=\d|MANIFEST check \d)')
shape = re.compile(lab + r' (?:rc=\d+|MANIFEST check \d+ FAILED.*)')
placed, unplaced = [], 0
for raw in open(path, encoding='utf-8'):
    line = re.sub(r'[\s`]+$', '', re.sub(r'^[\s>*`-]+', '', raw))
    reads = len(read.findall(raw))
    if reads == 1 and shape.fullmatch(line):
        if line not in placed:
            placed.append(line)
    elif reads or line.startswith(label + ' '):
        unplaced += 1
for line in placed:
    print(line)
print(label, 'unplaced', unplaced)
PROBE
}
```

A line quoted twice, once in a fenced block and once in a bullet, is one read and is kept once. Two
different status lines under one label both survive, and `TOOL-dTotalRecall-96` reads them as
contradictory. A label matches only with its following space, so `p69` never reads a `p69^` line. A
failure line's detail runs to the end of its line, so a second read on that line would vanish inside
it; counting the reads per line is what stops that.

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
- `w MANIFEST check 9 FAILED — stall` and `w MANIFEST check 5 FAILED — stale`
- AC3: the read was "x rc=1"
- AC1 — `read_sweep_line` — exactly one line starting `p69 rc=`
p69^ rc=1
LEDGER
```

PINNED, measured 2026-11-24 at `b59778f81` on node a with these exact lines: `c5_input` printed, for
`y`, both of its lines and `y unplaced 0`; for `p69`, `p69 rc=0` once and `p69 unplaced 0`; for `p69^`,
`p69^ rc=1` and `p69^ unplaced 0`; for `v`, `k`, `w` and `x`, only `v unplaced 1`, `k unplaced 1`,
`w unplaced 1` and `x unplaced 1`; for `u`, `u rc=0` and `u unplaced 1`; and for `none`,
`none unplaced 0`. Rev-1's function, run over the same file, placed the whole `w` line as one check-9
failure and printed `w unplaced 0`, printed `x unplaced 0`, and printed `p69 unplaced 1`. Unit 96 rev-1's
classifier printed `y C5 failed` over the `y` output, and unit 91 rev-3's printed `y C5 passed` over the
raw lines.

### The answer

```bash
# run from the repository root, with c5_input sourced
LEDGER80=$(git grep -l "Evidences:\*\* TOOL-dTotalRecall-80" -- memory/builds/dTotalRecall/build)
for L in p69 'p69^'; do c5_input "$LEDGER80" "$L"; done
```

Unit 91 §4 spells the same listing. It names one file, as it does for unit 69's ledger (DERIVED
2026-11-24, the same command with that id). An empty or two-file listing opens no file: `c5_input`
exits 1, prints no `unplaced` line, and the pass stops on it.

The `p69` line is the one unit 80's `read_sweep_line` lifts. Over the tree at `b59778f81` that function,
keyed on `f7011dd6f`'s full sha, printed `p69 rc=0` alone, from the sweep recorded in
`memory/builds/dTotalRecall/prompts/2026-11-24-prompt-TOOL-dTotalRecall-76-build-brief.md` (DERIVED
2026-11-24, that call). Over a scratch ledger of unit 80 rev-4's shape, its fence holding that line, a
`parent` line and a `p69^ rc=0` line, and its AC1 line naming `p69 rc=`, both labels printed their status
and `unplaced 0` (DERIVED 2026-11-24, `c5_input`).

### Why order 38

Unit 91 classifies at order 37. `TOOL-dTotalRecall-96` shares order 38 and consumes this unit, so
`--dispatch` refuses it while this unit is neither CLOSED nor WONTDO
(`tools/unattended/unattended.sh#verb_dispatch`, reading
`tools/unattended/lib-unattended.sh#read_consumes_from`).

### Inventory

Minted: the function `c5_input`, spec text only. No record is written. Naming cell: none, no product
symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger)

### Alternatives rejected

- **Read only the lines of a fenced block in unit 80's ledger.** The report's first option. Unit 80
  rev-4 does hold its reads in one fence, but a reader of the fence alone would miss a read line
  written outside it, and a ledger that broke the form would yield no line and no count.
- **Drop unplaced lines, as unit 91 does.** That is the defect: a dropped failure line reads as a
  clean read.

## 5. Production-readiness checklist

- security — no surface.
- perf / scale — one pass over one ledger per label.
- error / empty / loading states — a ledger with no line for the label prints `<label> unplaced 0`
  alone, which the classifier reads as no status; any unplaced line is counted and never dropped; a
  ledger that cannot be opened or is not UTF-8 exits 1 with no `unplaced` line.
- observability — the extracted lines are recorded verbatim beside the unplaced count.
- risks — prose that spells a whole read, or a wrapped line that begins `p69 `, is counted unplaced,
  which errs toward not-evaluated and never toward green. A read whose own bytes were changed in
  transcription, such as a backtick between the label and `rc=`, is neither placed nor counted; unit 80
  S1's verbatim block is what rules it out.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `c5_input "$SCRATCH/ledger97.md" <label>` runs for `y`, `p69`, `p69^`, `v`, `k`, `u`,
  `w`, `x` and `none`, it prints the lines §4 pins, among them both `y` lines with `y unplaced 0`,
  `v unplaced 1`, `u unplaced 1`, `w unplaced 1` and `p69 unplaced 0`.
  Red when: an indented failure line is dropped, an inline, quoted or trailing read line is not counted,
  a second read on a line is swallowed, a quoted duplicate is kept twice, or prose naming `p69 rc=` with
  no digit is counted.
  fixture: the ledger is made in the run's scratch by the pass; the tree holds none.
  figure: the outputs are PINNED in §4, measured 2026-11-24.
- **AC2** — When `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-97" -- memory/builds/dTotalRecall/build`
  runs after the pass, the ledger it names has an AC2 line naming unit 80's acceptance ledger by path,
  and one fenced block holding the verbatim output of `c5_input` for `p69` and for `p69^` over it, each
  ending in its `unplaced` line. Run again over that path, `c5_input` prints the same lines.
  Red when: either output is paraphrased, differs from the second run, or lacks its `unplaced` line.
  fixture: unit 80's ledger, which the §3 edge puts before this unit's dispatch; the tree holds none
  at `b59778f81`.

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
- rev-2 · 2026-11-24 · §1 · S1 · S2 · S3 · §4 · §5 · AC1 · AC2 · §10 · re-grounded at `b59778f81` per
  `2026-11-24-prompt-TOOL-dTotalRecall-97-reground-brief`, over unit 80 rev-4's fenced ledger, unit 77
  rev-4 and unit 91 rev-3: a line holding two reads and a read in double quotes are counted, prose naming
  `p69 rc=` with no digit is not, as unit 80's AC1 spells it; the launcher and the answer's command are
  spelled; the fixture gains labels `p69^`, `w` and `x` and is re-measured; AC2 reads the untracked
  ledger; citations are by symbol. No scope item or criterion is cut.

## 10. Reuse audit

The seams, re-read at `b59778f81`, are `TOOL-dTotalRecall-77` rev-4's `read_checker`, whose two printed
line shapes are the only placed lines, unit 80 rev-4's fenced block, and `TOOL-dTotalRecall-91`'s
classifier, which this extraction feeds through `TOOL-dTotalRecall-96`. Unit 80's `read_sweep_line`
lifts a sweep's lines by unit number and sha and counts nothing, so it is the writer of this input and
not its reader. `python tools/codebase-map/reuse_lookup.py "run a checker at each historical commit in a scratch worktree"`,
re-run 2026-11-24, ranked `add_scratch_worktree` among its SEAM candidates and nothing that lifts
recorded read lines out of a ledger. Asked to lift a label's status and failure lines and count the
rest, it ranked name-stem neighbours of `record`, `count` and `line`; its `read_ledger`
(`tools/lib/legacy_ledger.py#read_ledger`) reads keyed legacy rows, not an acceptance ledger. The recall
query below, re-run 2026-11-24, found this audit's record, specs 77, 80, 91 and 96 and no extractor.
The class is `memory/gotchas/parser-drops-rows-it-cannot-place.md`, whose rule, refuse what cannot be
placed, is S2. `tools/memory-tree/id_grammar.py#read_kept_reason` and the build-folder walks of
`tools/memory-tree/record_causes.py#check_cause_writers` and
`tools/memory-tree/record_kinds.py#check_alias_compares` are no seam here: this unit reads no marker
and no registry. No existing seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how are a checker's recorded read lines lifted out of a ledger so no line is dropped" --terms "read_checker p69 ledger extraction unplaced line indented bullet backtick c5_of manifest-check rc failure"`
