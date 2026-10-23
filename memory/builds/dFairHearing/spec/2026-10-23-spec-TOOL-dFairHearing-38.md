# TOOL-dFairHearing-38 — a `selected` verdict observed by the parser `gotchas.py` has, so a correct build passes and a shipped flag reds

**Status:** DEFERRED · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 25 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-38-deviation-381.md](../build/2026-10-23-build-TOOL-dFairHearing-38-deviation-381.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-38-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-38-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-38-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-38-promoted-fix-brief.md) | research | TOOL-dFairHearing-39 TOOL-dFairHearing-40 |

<!-- /gen:spec-records -->

## 1. Goal

The round-5 spec audit's finding id 1 (item H1, HIGH, shared with id 11,
`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md`) is
closed. `TOOL-dFairHearing-37` S4 and AC4 expect `gotchas.py --for-diff <range> --all-ungated` to exit 2
with argparse's `unrecognized arguments` when unit 35's record states `selected`. `gotchas.py` has no
argparse: `main`'s `--for-diff` branch (`tools/memory-tree/gotchas.py:1335-1339`) returns
`cmd_for_diff(root, conf, argv[2])` and never reads `argv[3:]`, so the call exits 0 and AC4 cannot pass
on a correct build. This unit replaces that half of AC4 with an observation the parser can satisfy and
a shipped flag cannot: the byte-identical comparison unit 32 AC8 already states, given a staged break,
and a read of the one branch where a flag would be dispatched. Id 11 is the same defect seen from the
grounding lens; its unit, `TOOL-dFairHearing-39`, carries the class into the bug-class catalogue.

## 2. Scope (IN)

- **S1** — Supersession. Unit 37 S4's sentence that the call exits 2 with `unrecognized arguments`, its
  claim that S4 "also answers unit 32 S13 and AC8", and the `selected` half of unit 37 AC4 are answered
  by this unit's S2 and S3 and AC1 and AC2. The `ungated` half of unit 37 AC4 stands, answered by unit
  35's AC4. Unit 37's acceptance ledger records the `selected` half superseded here
  (`TOOL-dFairHearing-23` §8 F7's form). NOT OBSERVED by a criterion of this unit: it is a ledger entry
  in unit 37's record, read there.
- **S2** — The behaviour half, one observation and not a second copy. When unit 35's record states
  `selected`, unit 32 AC8's comparison is the observation: over its fixture catalogue, which holds an
  ungated class outside the range's selection, `gotchas.py --for-diff <range> --all-ungated` prints
  output byte-identical to `gotchas.py --for-diff <range>`, and both exit 0. This unit re-runs that
  comparison at its own commit, then once over a staged copy of `gotchas.py` whose `--for-diff` branch
  appends every ungated class when `argv[3:]` holds `--all-ungated`. The staged copy must differ, which
  is the liveness unit 32 AC8 does not show. Observed by AC1.
- **S3** — The dispatch half. A flag `gotchas.py` honours is read in `main`'s `--for-diff` branch,
  because `cmd_for_diff` takes only the range. When unit 35's record states `selected`, that branch,
  sliced from its `if mode == "--for-diff":` line to the next `if mode ==` line, holds no `all-ungated`
  token. The slice reads code only: the module docstring and `cmd_for_diff`'s docstring, which may state
  unit 23 S21's contract, sit outside it. Observed by AC2.

## 3. Non-goals (OUT)

- No change to `gotchas.py`'s parser. A refusal of unknown arguments would turn unit 32 AC8's
  comparison red on a `selected` build, and no spec in this build asks for one.
- No catalogue record. Carrying the class into `memory/gotchas/` is id 11's mechanism,
  `TOOL-dFairHearing-39`; the two units share no file.
- No change to the `ungated` branch, which stays unit 35's S3 and AC4.
- No MEDIUM or LOW finding of the same audit: those 35 are `TOOL-dFairHearing-40`'s.
- No help page: `help/` covers neither the review harness nor the bug-class tool.

### Edges

- **consumes-from** `TOOL-dFairHearing-37` — S4 and AC4's `selected` half, which S1 supersedes; without them there is no criterion to repair
- **consumes-from** `TOOL-dFairHearing-35` — the record's `selected` or `ungated` decision, which decides whether AC1 and AC2 apply
- **consumes-from** `TOOL-dFairHearing-32` — AC8's comparison and its fixture catalogue, which S2 re-runs rather than restating

## 4. Design

### Why the comparison and not a refusal

Two observations fit a parser that ignores trailing arguments. A refusal would need a parser change,
which breaks unit 32 AC8 and which the report itself lists only as the alternative. The comparison
holds on the parser as it is, and it discriminates: a build that shipped the flag prints the outside
class under `--all-ungated` and not without it. The branch read covers the case the comparison cannot,
a flag dispatched but printing nothing new.

### The staged copy (S2)

The probe copies `tools/memory-tree/gotchas.py` to the pass's scratch directory and inserts, as the
first line of the `--for-diff` branch body, a print of every class `check_ungated` admits when
`"--all-ungated" in argv[3:]`. It runs that copy over unit 32 AC8's fixture with the flag. The probe
writes the copy with its file-writing tool and never edits the tracked file.

### The branch read (S3)

```python
# branch.py <gotchas.py> — the --for-diff dispatch branch of main, sliced and searched
import sys
lines = open(sys.argv[1], encoding="utf-8").read().splitlines()
start = next(i for i, l in enumerate(lines) if l.strip() == 'if mode == "--for-diff":')
end = next(i for i in range(start + 1, len(lines)) if lines[i].strip().startswith("if mode =="))
body = lines[start:end]
print(f"branch {start + 1}-{end} lines {len(body)}")
hits = [l for l in body if "all-ungated" in l]
print(f"all-ungated {len(hits)}")
sys.exit(1 if hits else 0)
```

A missing anchor raises `StopIteration`, so the probe never passes on a branch it did not find. At
`3708a705` the branch spans lines 1335 to 1339.

### Files touched (estimate)

None. Both observations are scratch probes; the result is a line in this unit's acceptance ledger and
the supersession entry in unit 37's.

### Alternatives rejected

- **Make `gotchas.py --for-diff` refuse unknown arguments with exit 2.** It reds unit 32 AC8 on a correct
  `selected` build and adds a parser change no spec asks for.
- **Keep the whole-file `grep -c -- "--all-ungated"`.** A docstring stating unit 23 S21's contract reds
  it, which is why unit 32 S13 retired it.

## 5. Production-readiness checklist

- security — N/A: read-only scratch probes over a tracked file and a fixture; no write path.
- perf / scale — two `gotchas.py` runs over one fixture and one file read.
- error / empty / loading states — a branch anchor that is not found raises, so an empty slice is never
  a pass.
- observability — the probe prints the branch's line span and count before its verdict.
- risks — a future parser that moves flag dispatch out of `main` makes S3 read the wrong place; AC2
  prints the span so a reader sees which lines it graded.
- testing — AC1 and AC2, each with a staged break.
- migration — none.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

`branch.py` is the script of §4, written under the pass's scratch directory. Unit 32 AC8's fixture is
the scratch catalogue repository under `%TEMP%/fgc`.

- **AC1** — When unit 35's record states `selected`, `python tools/memory-tree/gotchas.py --for-diff
  <range> --all-ungated` and the same command without the flag, run over the `%TEMP%/fgc` fixture at
  this unit's commit, both exit 0 and print byte-identical output. Over the staged copy of S2 the two
  outputs differ. When the record states `ungated`, unit 35's AC4 answers this criterion.
  Red when: a `selected` build prints the outside class under the flag, or the staged copy prints the
  same output, which means the fixture holds no ungated class outside the selection.
  fixture: the catalogue repository under `%TEMP%/fgc`, made by the probe as unit 32 AC8 states and
  removed after it.
- **AC2** — When unit 35's record states `selected`, `python branch.py tools/memory-tree/gotchas.py`
  prints the branch span and `all-ungated 0`, and exits 0. Over a scratch copy whose branch holds
  `if "--all-ungated" in argv[3:]:` it prints `all-ungated 1` and exits 1.
  Red when: a flag is dispatched in the `--for-diff` branch on a `selected` verdict.

## 7. Gates

`gotchas selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No new arm: both observations are scratch probes, observed directly by §6.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 1 (item H1, HIGH, shared with id 11) of the
  round-5 spec audit of specs 33 to 37.

## 10. Reuse audit

The seam reused is unit 32 AC8's comparison and its fixture, which the round-3 audit's corrected fix
(`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md`,
ids 4 and 9) already chose for this verdict; this unit adds the staged break and the branch read
rather than a third copy. `python tools/codebase-map/reuse_lookup.py "observe that a command line flag
did not ship by comparing output with and without it"` ranked `note`, `check_line` and
`read_git_output` by name-token fan-in and no flag-absence probe, so no existing seam fits the branch
read; it is a scratch script of one slice. The recall query returned the audit's H1 item, unit 37 S4,
the round-3 audit's corrected fix and `TOOL-aMendedFleet-38`'s ledger, where `map_diff.py` does use
argparse and so does print `unrecognized arguments`, the parser this criterion borrowed from.

Recall terms used: `python tools/memory-recall/query.py "a criterion expects an argparse error from a tool that parses its arguments by hand" --terms "argparse unrecognized arguments gotchas for-diff all-ungated selected verdict flag shipped criterion cannot pass"`
