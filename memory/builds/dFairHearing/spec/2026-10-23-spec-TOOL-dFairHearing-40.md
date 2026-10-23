# TOOL-dFairHearing-40 — the round-5 spec audit's 35 minors: one build-wide version reading on one base, an attempt checker that refuses what it cannot place, and criteria a correct build can pass

**Status:** DEFERRED · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 26 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-40-deviation-401.md](../build/2026-10-23-build-TOOL-dFairHearing-40-deviation-401.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-38-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-38-promoted-fix-brief.md) | research | TOOL-dFairHearing-38 TOOL-dFairHearing-39 |
| [2026-10-23-prompt-TOOL-dFairHearing-40-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-40-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

One batch unit closes every MEDIUM and LOW finding that the round-5 spec audit confirmed
(`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md`), 35
report ids over units 33 to 37. MEDIUM ids: 2 and 26 (item M1), 3, 20 and 27 (M2), 14, 21 and 35 (M3),
13 (M4), 4 (M5), 12 (M6), 15 and 38 (M7), 22 (M8), 18 (M9), 25 (M10), 28 (M11), 31 (M12) and 33 (M13).
LOW ids: 5 (L1), 6 (L2), 7 (L3), 8 (L4), 9 and 24 (L5), 10 (L6), 16 (L7), 17 (L8), 23 (L9), 29 (L10),
30 (L11), 34 (L12), 36 (L13), 37 (L14) and 39 (L15). Each id is its own §2 item. The minors land on
five units, so this unit repairs no one unit and sits above every order in the build, after units 38
and 39. That order is also what item M1 needs: this unit's commit is the build's last pass commit, the
one place a build-wide version reading sees every unit's edits. A criterion it supersedes is named by
the hands-off bullet in that unit's §3, and that unit's acceptance ledger records it superseded here
(`TOOL-dFairHearing-23` §8 F7's form).

## 2. Scope (IN)

Each item names its report id, its report item, the unit it lands on and the criterion that observes
it. Where a report item merges ids, the later id points at the first one's mechanism.

- **S1** — id 2 (M1, units 33 and 34, AC1). The build-wide half of unit 27 S15's rule is read at this
  unit's commit, after units 36 and 37 edit kit files at order 24 (unit 37 edits
  `tools/workflows/tier2-review.template.js`, review-harness's `version_from` carrier per
  `tools/workflows/kit.toml:8`). `constants.py` and `markers.py`, as S18, S19, S26 and S34 correct
  them, run over `<base>..HEAD` with `<base>` from S3. Unit 33 AC1 and unit 34 AC1 keep their reading
  at their own commit; the "a constant moved on the branch" half of each Red when clause is answered
  here. A unit ordered after this one inherits the re-run. Observed by AC1.
- **S2** — id 26 (M1). S1's mechanism. Observed by AC1.
- **S3** — id 3 (M2, units 33, 34 and 36). One base seam for the build-wide reading: S1's `<base>` is
  the sha unit 36's `base.py` prints, which takes `GATE_BASE` unchanged and otherwise calls
  `resolve_compare_base` (`tools/codebase-map/map_lib.py:1502`). Units 33 and 34 at order 23 read unit
  31's probe, and the two bases agree only with `GATE_BASE` unset and `HEAD` ahead of the remote tip,
  so each of their ledgers names whether `GATE_BASE` was set when its AC1 ran. Observed by AC1 and AC2.
- **S4** — id 20 (M2). S3's mechanism: the consumes-from edge of units 33 and 34 on unit 31 stays for
  their order-23 reading, and the build-wide reading consumes `base.py` here. Observed by AC2.
- **S5** — id 27 (M2, unit 36 §4, unit 31 AC1). Unit 31's script and its AC1 are left as they are:
  `base <sha> from origin/main` is unit 31's label and `base <sha> from merge-base of HEAD and
  origin/main` is `base.py`'s, each read only by its own criterion. Unit 36 §4's sentence "It prints the
  line unit 31's probe prints, so units 33 and 34 read its sha the same way" is superseded by S3's
  statement. Observed by AC2.
- **S6** — id 14 (M3, unit 35 S1, S2 and §4). The attempt checker gains a third outcome, `failed`: the
  harness call was made and returned no usable report. A `failed` attempt counts as a completed void
  attempt and takes one of the two eligible slots. Any line inside the attempts table, from its header
  row to the first line not opening with `|`, that opens like an attempt row (`| <1-4> | <arm> |`, the
  arm matched ignoring case) and does not match the full row grammar exits 1 naming its line number.
  Rows of the record's other tables are never read. Observed by AC3.
- **S7** — id 21 (M3). S6's mechanism: the staged `Completed` row is refused naming its line, never
  dropped. Observed by AC3.
- **S8** — id 35 (M3). S6's mechanism: a call that died or timed out is `failed`, so its label is never
  the runner's choice between `refused` and `completed`. Observed by AC3.
- **S9** — id 13 (M4, unit 35 S2, AC1). The void column is re-derived, never trusted. For each attempt
  row, `void.py` (§4) derives its void cause from evidence the record names: the report's parse, the
  dead agents its `Run integrity` block names, and for a cell citing an outside read, the transcript line
  it quotes. A cell that disagrees, a `refused` row whose clone holds a report, or a named report not on
  disk is red. Observed by AC4.
- **S10** — id 4 (M5, unit 35 AC3, unit 37 AC11). Unit 35 AC3 holds unless the checker exited 3, in
  which case the record states `no decision`, no pooled figure is computed and unit 35 AC4's empty diff
  holds. Unit 37 AC11 reads "each scored clone", the scored clones are distinct, and a `void after cap`
  pair is listed with its reason. Observed by AC5.
- **S11** — id 12 (M6, unit 36 AC3). Unit 36 AC3's suite input is
  `git show 3708a705:tools/hooks/agent-cap.test.sh` written to a scratch file and passed as every suite
  path, so its pinned 73 and 5 are read over the revision they were measured at. Observed by AC6.
- **S12** — id 15 (M7, unit 37 S8 and §4). The per-arm step (§4) refuses, exit 2 naming the variable,
  when `SCRATCH` or `ORCH` is empty, and builds the clone's parent from `TEMP`, else `TMPDIR`, refusing
  when both are empty, so no path is built from an unset variable. The README states that `TEMP` is the
  Windows name and `TMPDIR` the POSIX one. Observed by AC7.
- **S13** — id 38 (M7). The orchestrating commit is read as its own call, `git -C "$ORCH" rev-parse
  --verify HEAD`, with its status checked before the log line is written. Observed by AC7.
- **S14** — id 22 (M8, unit 37 S8, AC8). The run log line S8 claims is observed: after the per-arm
  block runs over a clean fixture clone up to the harness call, the log holds exactly one
  `orchestrating <40 hex> clone ` line whose sha equals `ORCH`'s `HEAD`. Observed by AC7.
- **S15** — id 18 (M9, unit 37 S9, AC9). Unit 37 AC9's absence probe reads both `.js` files through
  `renderLexedView` (`tools/hooks/agent-cap.js:720`), which blanks strings, cuts `//` comments, blanks
  template text and copies each `${…}` body with its brace depth saved in `interpDepths`. It replaces
  the two-pass reader unit 37 S9 describes. Observed by AC8.
- **S16** — id 25 (M10, unit 35 S3, S6). When unit 35's record states `ungated`, no prose carrier tells
  a caller to pass `gotchas.py --for-diff` stdout as the review harness's `checklist`, because spec 15
  S1 lets a caller's checklist win. The carriers are `memory/guides/MERGE-BAR.md`,
  `memory/guides/SESSION-KICKOFF.md`, `memory/HYGIENE.md` and its template
  `tools/memory-tree/HYGIENE.template.md`, the four unit 23 S45 rewords. Each says the harness acquires
  its own checklist on the diff kind; where one does not, this unit rewords it in unit 23 S45's form.
  When the record states `selected`, the range's selection is the decided checklist and nothing changes.
  Observed by AC9.
- **S17** — id 28 (M11, unit 37 S13, AC12). The cure of a disagreement between `resolveKitDir` in
  `tools/hooks/agent-cap.js` and `tools/lib/resolve_kit_dir.py` on rows 8 and 9 is this unit's, after
  units 36 and 37, so neither order-24 pass writes the hook. Unit 37 records the two rows' result, and
  the Red when clause of its AC12 is answered here. Where the port disagrees, this unit makes it test
  `.git` by existence and catch a `JSON.parse` failure, and owes the hook's legs. Observed by AC10.
- **S18** — id 31 (M12, unit 33 §4, S3, AC3). `constants.py` catches `RuntimeError`, the base of
  `govkit.Refusal` (`tools/govkit/govkit.py:115`), beside its other exceptions, so a registry that does
  not load exits 2 naming it. Observed by AC11.
- **S19** — id 33 (M13, unit 33 S2, §5). A `new` outcome is a refusal, exit 2, unless the entry's
  descriptor is absent at the base. The registry is read at both ends, and an entry present at the base
  and absent at the head is a refusal naming it. Unit 33 §5's line "a kit removed by the build refuses
  rather than passes" is then true. Observed by AC11 and AC12.
- **S20** — id 5 (L1, unit 37 AC17, AC5). Unit 37 AC17 counts `trap '` only on lines of the replay
  section's fenced bash blocks, the section sliced from its heading to the next `## ` and comments
  excluded. Unit 37 AC5 observes an absence in place of its count: no `ls-files --literal-pathspecs`
  spelling, string or argv form, remains in `replay_scorer.py`. Observed by AC13.
- **S21** — id 6 (L2, unit 35 §4). The checker exits 1 naming the line when a row's last cell is empty.
  Observed by AC3.
- **S22** — id 7 (L3, unit 36 AC6). Unit 36's ledger labels AC6 precondition evidence, as its S7 labels
  the other green-at-base criteria. Observed by AC14.
- **S23** — id 8 (L4, unit 37 AC15). Unit 37 AC15 first requires its grep to print the
  `function deriveAddressKey` line, and where the comment above it cites the instrument by line it holds
  `:1665-1666`. Observed by AC15.
- **S24** — id 9 (L5, unit 35 S5). Unit 35 S5's change to unit 30's record's `**Serves:**` line is
  observed. Observed by AC16.
- **S25** — id 24 (L5). S24's mechanism. Observed by AC16.
- **S26** — id 10 (L6, unit 33 S3, AC3). The two refusals unit 33 AC3 never stages are staged: a
  constant resolving at the base and not at the head, and zero constants compared. Observed by AC11.
- **S27** — id 16 (L7, unit 36 §4). S5's mechanism: the sentence is superseded by S3's statement of
  when the two bases agree. Observed by AC2.
- **S28** — id 17 (L8, unit 33 §4). Unit 33 §4's sentence naming `(none declared)` as a value the `(`
  test reads is corrected: the guard above it skips undeclared entries on the predicate
  `resolve_entry_version_at` (`tools/govkit/govkit.py:703-705`) uses, so only `(unresolvable)` reaches
  the test. NOT OBSERVED by a criterion: it corrects a sentence and changes no behaviour; unit 33's
  ledger records it superseded here.
- **S29** — id 23 (L9, unit 33 S2). The `absent` and `new` outcomes are asserted: the `7d98741e3` pair
  prints `absent branch-reconcile` and `absent roles`, and the pair that adds the branch-reconcile kit
  prints `new branch-reconcile 1.0`. Observed by AC12.
- **S30** — id 29 (L10, unit 37 S15). After unit 37 S15 changes `check_ungated`'s sentence end, the
  `ungated` class set unit 35's `## Scoring` records is re-derived with the corrected function over the
  class records at unit 30's commit and compared; this unit's ledger states `unchanged` or names each
  class that moved. Observed by AC17.
- **S31** — id 30 (L11, units 36 and 37 §4). The `--dispatch --writes` set of each order-24 pass counts
  its own acceptance ledger record, and unit 36's counts the ledgers of units 28, 29 and 31 it writes
  supersessions into. The README's generated build-index blocks are a shared render the main loop
  regenerates after the passes, written by neither. Observed by AC18.
- **S32** — id 34 (L12, unit 34 §3, §4). Unit 34 §3's attribution is corrected: a marker in an added or
  renamed file, and a marker present only at the head in a modified file, are graded by
  `govkit selfcheck`'s check 5c (`tools/govkit/govkit.py:2222`) within its basis of claimed paths and
  `marker_carriers`, never by `kit version markers`, whose script reads a fixed list of pairs. A file
  outside that basis is not graded by either, and the residual says so. NOT OBSERVED by a criterion: it
  corrects an attribution and changes no behaviour; unit 34's ledger records it superseded here.
- **S33** — id 36 (L13, unit 37 S6). Every `git -C ${repo}` interpolation in
  `tools/workflows/tier2-review.template.js`, the prompts and `diffCmd` (:1081) included, is quoted as
  `git -C "${repo}"`, and after unit 37 S6's fold a `repo` holding a double quote, a `$` or a backtick
  is refused naming the character. A path holding a space then stays one argument. Observed by AC19.
- **S34** — id 37 (L14, unit 37 S9). S15's mechanism: `renderLexedView` takes an interpolation only
  inside template text and balances its braces, so the nested and comment copies S9 left undefined are
  decided. Its residual: it does not blank block comments, so a `/* MAX_LENSES */` copy fails the probe
  closed. Observed by AC8.
- **S35** — id 39 (L15, unit 36 S12). `base.py`'s refusal of a tip answer names both causes that reach
  it: "HEAD is not ahead of <tip>, or shares no merge-base with it (shallow or unrelated history)".
  Observed by AC2.

## 3. Non-goals (OUT)

- No re-review, and no fold into the specs of units 33 to 37: each item makes the corrected statement
  true and reopens no severity.
- No re-run of a replay and no re-decision. When the corrected checker or the void re-derivation reads
  unit 30's record differently from unit 35's recorded output, AC3 or AC4 goes red and the main loop
  parks the decision; this unit never re-scores.
- No HIGH finding: ids 1 and 11 are `TOOL-dFairHearing-38` and `-39`.
- No new gate leg and no committed checker: `constants.py`, `markers.py`, `base.py`, `attempts.py` and
  `void.py` stay scratch probes, as units 33 to 36 resolved.
- No change to `gotchas.py`, its catalogue or its rendered index header: the header hands a reader the
  classes, and the harness's own acquisition is the workflows README's.
- No help page: `help/` covers neither the review harness, the scorer factory, the hooks nor a
  build-time check.

### Edges

- **consumes-from** `TOOL-dFairHearing-30` — the verdict record, each attempt's clone and report path, which S9, S24 and S30 read
- **consumes-from** `TOOL-dFairHearing-32` — `resolveKitDir`, the port S17 cures where it disagrees
- **consumes-from** `TOOL-dFairHearing-33` — `constants.py`, S2, S3, §4, AC1 and AC3, which S1, S3, S4, S18, S19, S26, S28 and S29 correct
- **consumes-from** `TOOL-dFairHearing-34` — `markers.py`, §3 and AC1, which S1, S3, S4 and S32 correct
- **consumes-from** `TOOL-dFairHearing-35` — the attempt rule, its checker, the `## Scoring` section and AC3, which S6 to S10, S16, S21, S24 and S30 correct or read
- **consumes-from** `TOOL-dFairHearing-36` — `base.py`, AC3 and AC6 and its §4, which S3, S5, S11, S22, S27, S31 and S35 read or correct
- **consumes-from** `TOOL-dFairHearing-37` — S6, S8, S9, S13, S15, the per-arm step and AC5, AC8, AC9, AC11, AC12, AC15 and AC17, which S10, S12 to S15, S17, S20, S23, S30, S31, S33 and S34 correct

## 4. Design

### Why one batch unit

M6 admits two halves only when neither writes a file the other reads as an acceptance input. S1 reads
every kit's version carrier, and S33 writes one of them, `tools/workflows/tier2-review.template.js`.
Any split that keeps S1 apart from S33 fails that clause, and S1 must run last. So the 35 minors are
one unit at the build's last order.

### The version probes, corrected (S1, S18, S19, S26, S29)

`constants.py` is unit 33 §4's script with three changes. The `except` tuple gains `RuntimeError`. The
`new` branch refuses unless the descriptor is absent at the base. And before the loop, the registry is
read at both ends:

```python
# inside the try, after read_descriptors
reg = pathlib.Path(govkit.derive_registry_path(root)).resolve().relative_to(root).as_posix()
def ids(ref):
    blob = govkit.blob_at(root, ref, reg)
    return {e.get("id") for e in tomllib.loads(blob.decode("utf-8")).get("entry", [])} if blob else set()
gone = sorted(ids(base) - ids(head))
# after the problems check
if gone:
    refuse(f"registry entries at {base} and not at {head}: {' '.join(gone)}")
# the new branch
elif old.startswith("("):
    if subprocess.run(["git", "-C", str(root), "cat-file", "-e", f"{base}:{dpath}"],
                      capture_output=True).returncode == 0:
        refuse(f"{eid}: its descriptor is at {base} and its constant does not resolve there: {old}")
    print(f"new {eid} {new}")
```

`import tomllib` joins the import line, and the loop names the descriptor path `dpath` where unit 33
wrote `_dpath`. A base holding no registry blob holds no entry, so every entry it lacks is new.
`markers.py` is unit 34 §4's script unchanged. Measured on 2026-10-23: the branch-reconcile kit's
descriptor and version file are both added by `0baf2e47a`, and its parent holds neither.

### The attempt checker, corrected (S6 to S8, S21)

```python
# attempts.py <record> — unit 15's replay: the scored attempt of each record and arm, by rule
import re, sys
ROW = re.compile(r"^\|\s*([1-4])\s*\|\s*(selected|ungated)\s*\|\s*(\d+)\s*\|\s*(\S+)\s*\|"
                 r"\s*(refused|completed|failed)\s*\|\s*(.*?)\s*\|\s*$")
OPENS = re.compile(r"^\|\s*[1-4]\s*\|\s*(selected|ungated)\s*\|", re.I)
HEADER = re.compile(r"^\|\s*record\s*\|\s*arm\s*\|", re.I)
rows, seen, inside = {}, set(), False
for no, line in enumerate(open(sys.argv[1], encoding="utf-8"), 1):
    if HEADER.match(line):
        inside = True
        continue
    if inside and not line.startswith("|"):
        inside = False
    if not inside or not OPENS.match(line):
        continue
    m = ROW.match(line)
    if not m:
        sys.exit(f"attempts: line {no} opens an attempt row and does not parse: {line.strip()}")
    r, a, n, clone, outcome, void = m.groups()
    if not void:
        sys.exit(f"attempts: line {no} has an empty last cell")
    if (r, a, int(n)) in seen:
        sys.exit(f"attempts: attempt {n} of record {r} {a} is listed twice")
    seen.add((r, a, int(n)))
    rows.setdefault((r, a), []).append((int(n), clone, outcome, void))
```

The rest is unit 35 §4's checker with one change: `done` holds the `completed` and `failed` attempts,
and `scored` is the first of `done[:2]` that is `completed` with void `-`. A `failed` attempt's last
cell names what came back instead of a report.

### The void re-derivation (S9)

`void.py <record>` reads the attempts table with the grammar above and, for each row, the report path
unit 30's record names beside that clone (unit 30 S5).

| Row | Must hold | Red when |
|---|---|---|
| `refused` | the clone holds no review report | a report is on disk |
| `completed`, void `-` | the report is on disk, parses under the reader `replay_scorer.py --experiment` uses for its `parsed` lines run over a one-candidate scratch manifest, and its `Run integrity` block names 0 dead finders and 0 dead skeptics | any of the three fails |
| `completed` or `failed`, void naming a cause | that cause re-derives from the same three reads; a cell citing an outside read quotes `<transcript file>:<line>` and the absolute path, and that line holds that path, outside the clone and the scratchpad | the cause does not re-derive, or the quoted line is absent |

It prints `agrees <record> <arm> <attempt>` for each row that holds, and exits 1 naming the first row
that does not. A report or a transcript the record names and that is no longer on disk is red, as not
re-derivable, so the evidence stays until this unit's pass. The residual: an outside read on an attempt whose cell
reads `-`, which the pass did not record, is not re-derived; spec 1 §4's probe at order 21 is its only
observation.

### The per-arm step, corrected (S12 to S14)

```bash
test -n "$SCRATCH" || { echo "SCRATCH is empty"; exit 2; }
test -n "$ORCH" || { echo "ORCH is empty"; exit 2; }
t="${TEMP:-$TMPDIR}"
test -n "$t" || { echo "no temp directory: TEMP and TMPDIR are both empty"; exit 2; }
if command -v cygpath >/dev/null 2>&1; then t=$(cygpath -m "$t"); fi
c="$t/f<r><a><n>"
test ! -e "$c" || { echo "stale: $c"; exit 2; }
# the recipe over "$c" at the record's range head, with its exact-commit check
s=$(git -C "$c" status --porcelain --untracked-files=all) || { echo "status failed: $c"; exit 2; }
test -z "$s" || { echo "dirty: $c"; exit 2; }
o=$(git -C "$ORCH" rev-parse --verify HEAD) || { echo "orchestrating head unreadable: $ORCH"; exit 2; }
echo "orchestrating $o clone $c" >> "$SCRATCH/run.log"
# the harness call, `repo` set to "$c"; a refused attempt takes the next <n> and a new clone
```

`ORCH` is the orchestrating repository's root. It replaces unit 37 §4's block in the README's replay
section.

### The absence probe's view (S15, S34)

The probe slices `checkLiteralOpen`, `resolveLiteralEnd` and `renderLexedView` out of
`tools/hooks/agent-cap.js`, each from its `function <name>(` line to the next line opening `function `
at column 0, and evaluates them together in a `vm` context; the file itself calls `main()` at load, so
it is never required. A `ReferenceError` names a further function to slice and exits 2, never a pass.
The probe joins the view's `code` lines and searches `\bMAX_LENSES\b`. The same view is applied to
`check-verifier-fanout.js`.

### The port's cure (S17)

Only where unit 37's rows 8 and 9 disagree: `resolveKitDir` tests the worktree root's `.git` by
existence, as `tools/lib/resolve_kit_dir.py:29` does with `(d / ".git").exists()`, and treats a receipt
whose `JSON.parse` throws as absent, as :33 catches `ValueError`.

### Files touched (estimate)

- `tools/workflows/README.md`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/hooks/agent-cap.js`
- `memory/guides/MERGE-BAR.md`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/HYGIENE.md`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/builds/dFairHearing/build/`

`tools/workflows/tier2-review.js` is the template's render. `tools/hooks/agent-cap.js` changes only
where AC10 finds the port disagreeing. The four prose carriers change only on an `ungated` record and
only where AC9 finds the instruction. Two arms of `tools/workflows/tier2-review.test.sh` assert the
unquoted `git -C /tmp/r` text (:766, :1659); their expected strings take the quoted form, the same
assertions. Under the build folder, only this unit's acceptance ledger is written.

### Alternatives rejected

- **Two batch units.** §4 "Why one batch unit".
- **Refuse a `repo` holding a space (S33).** Every caller whose checkout path holds one would fail;
  quoting keeps the path one argument.
- **State as a non-goal that a caller's checklist keeps the selection (S16).** It leaves the decision
  applying only to callers that pass none, where the carriers can say so for the cost of a grep.
- **Re-run units 33 and 34 at order 25.** Unit 33 and 34's own readings stay at their commits; one
  build-wide reading at the last order is the one that sees every unit.

## 5. Production-readiness checklist

- security — S33 quotes a path pasted into shell commands and refuses the three characters a
  double-quoted bash string cannot hold literally; no new write path.
- perf / scale — two `git show` reads per declared constant and per modified file; one parse per
  attempt report.
- error / empty / loading states — every probe refuses by name: an unplaceable or empty attempt row, an
  unset variable, an unreadable head, a registry entry dropped, a moved carrier.
- observability — the run log names the orchestrating commit beside each clone; each probe prints its
  population before its verdict.
- risks — a difference between the corrected checker and unit 35's recorded output stops the build
  rather than re-deciding; a deleted report reds S9 as not re-derivable.
- testing — scratch probes and fixtures per criterion; the §7 arms observed RED then GREEN at the close.
- migration — none for adopters beyond the harness's quoted `repo` and its refusal of three characters.
- user docs — `tools/workflows/README.md`, the replay section; there is no `help/` page (§3).

## 6. Acceptance criteria

`constants.py`, `markers.py`, `base.py`, `attempts.py` and `void.py` are the scripts of §4 and of units
33, 34 and 36 as §4 corrects them, written under the pass's scratch directory. A clone or fixture
repository goes under `%TEMP%/<short name>`.

- **AC1** — When `python base.py .` runs at this unit's commit with `GATE_BASE` unset and prints `base
  <sha>`, `python constants.py . <sha>` prints `constants <n>` and no `->` line and exits 0, and
  `python markers.py . <sha>` prints `files <m>` and no `->` line and exits 0.
  Red when: a version value moved in any commit of the build, units 36 and 37 included.
  figure: `<n>` and `<m>` are DERIVED, as unit 33 AC1 and unit 34 AC1 derive them.
- **AC2** — When `python base.py .` runs at this unit's commit with `GATE_BASE` unset, its sha equals
  `git merge-base HEAD origin/main`. In a fixture made by `git clone --depth 1` of a two-commit
  repository, it exits 2 printing `shares no merge-base`. `git grep -n GATE_BASE` over the acceptance
  ledgers of units 33 and 34 prints one line each, naming `unset` or the value.
  Red when: the build-wide reading takes a base other than `base.py`'s, a shallow clone's refusal names
  only the not-ahead cause, or a ledger leaves the order-23 base unstated.
  fixture: a two-commit repository under `%TEMP%/fsa` cloned to `%TEMP%/fsb`, made by the probe and
  removed after it.
- **AC3** — When `python attempts.py <unit 30's verdict record>` runs at this unit's commit, its
  `scored` and `void after cap` lines equal those unit 35's `## Scoring` section quotes. Over scratch
  tables it exits 1 naming the line for a row reading `Completed`, a row whose last cell is empty and a
  row reading `| 4 | Selected |`; a record 4 `selected` reading failed then completed prints `scored 4
  selected 2`, and failed, failed, completed prints `void after cap 4 selected` and exits 3. A row of a
  second table opening `| 1 |` outside the attempts table is not read.
  Red when: a row is dropped without a message, a `failed` attempt is scored or takes no slot, or the
  corrected checker scores an attempt unit 35's record did not.
  fixture: the tables under the pass's scratch directory, written by the probe.
- **AC4** — When `python void.py <unit 30's verdict record>` runs at this unit's commit, it prints one
  `agrees` line per attempt row and exits 0. Over a scratch copy whose attempt-1 void cell is changed to
  cite an outside read the transcript does not hold, it exits 1 naming that row, and over one whose
  completed attempt is relabelled `refused`, it exits 1 naming the report on disk.
  Red when: a void cell the evidence does not support decides which attempt is scored.
  fixture: the record copies under the pass's scratch directory; the reports and transcripts unit 30's
  record names, on disk.
- **AC5** — When `python attempts.py <unit 30's verdict record>` exits 3, unit 30's record states
  `no decision` beside each void pair with its reason and names no pooled figure, `git diff <unit 35's
  parent> <unit 35's commit> -- tools/memory-tree/gotchas.py` prints nothing, and the clones unit 37's
  ledger grades for AC11 are exactly those the `scored` lines name. When it exits 0, unit 35 AC3 and
  unit 37 AC11 are answered as written.
  Red when: a correct void-after-cap build is held to the four parsed records or the eight clones that
  unit 35 AC3 and unit 37 AC11 required.
- **AC6** — When the hook suite as it stood at base `3708a705`, read by `git show` at that revision as
  §2 S11 spells it, is written to a scratch file and given as every suite path, `census.py` prints 73 `gone` lines and `members.py` prints 5, under both
  `PYTHONUTF8=1` and `PYTHONUTF8=0`.
  Red when: the counts are read over the working suite, from which units 26, 28 and 29 moved the arms.
  figure: 73 and 5 are PINNED, measured at `3708a705` on 2026-10-23 (unit 36 §4).
- **AC7** — When the README's per-arm block runs in a scratch shell with `SCRATCH` empty, then `ORCH`
  empty, then `TEMP` and `TMPDIR` both empty, each exits 2 naming the variable before any clone path
  is used. With `ORCH` naming a directory that is no repository, it exits 2 printing `orchestrating head
  unreadable` before the harness call. Over a clean fixture clone with every variable set,
  `grep -c "^orchestrating [0-9a-f]\{40\} clone " run.log` prints 1 and that sha equals
  `git -C "$ORCH" rev-parse HEAD`.
  Red when: a path is built from an unset variable, or the log line is absent, empty or unanchored.
  fixture: one clone under `%TEMP%/fpa`, made by the probe and removed after it.
- **AC8** — When the S15 probe reads `tools/hooks/agent-cap.js` and `check-verifier-fanout.js`, neither
  holds a `MAX_LENSES` identifier. Scratch copies holding `` `x ${f({k: MAX_LENSES})}` ``,
  `` `${ {a:1}.a + MAX_LENSES }` `` and `` `${ `${MAX_LENSES}` }` `` each fail the probe, and copies
  holding `// see ${MAX_LENSES}` and `// MAX_LENSES was 6` each pass it.
  Red when: a nested interpolation passes as absent, or a line comment reds a correct build.
- **AC9** — When unit 35's record states `ungated`, `grep -n "acquires" memory/guides/MERGE-BAR.md`
  and the same over `memory/guides/SESSION-KICKOFF.md`, `memory/HYGIENE.md` and
  `tools/memory-tree/HYGIENE.template.md` each print the sentence saying the harness acquires its own
  checklist, and none of the four tells a caller to pass the command's stdout as `checklist`. When it
  states `selected`, `git diff <this unit's parent> HEAD -- memory/guides/MERGE-BAR.md` prints nothing.
  Red when: a carrier hands the range's selection to the harness after an `ungated` decision.
- **AC10** — When a scratch probe runs `tools/lib/resolve_kit_dir.py` and `resolveKitDir`, sliced from
  `tools/hooks/agent-cap.js` at this unit's commit, over unit 37's rows 8 and 9, the two print the same
  directory on each row. `git diff <this unit's parent> HEAD -- tools/hooks/agent-cap.js` prints
  nothing unless unit 37's ledger records a disagreement.
  Red when: the port walks past a worktree's `.git` file or denies on a malformed receipt.
- **AC11** — When `constants.py` runs over a scratch root holding `tools/govkit/govkit.py` and no
  registry, it exits 2 naming the registry, and over a root with no `tools/govkit`, it exits 2 naming
  the import. In a clone under `%TEMP%/fcd` that deletes `tools/roles/roles_lib.py` in one commit,
  `python constants.py <clone> HEAD~1 HEAD` exits 2 naming `roles`; with the clone's
  `tools/branch-reconcile/branch_reconcile.py` moved by `git mv` and its version line raised in one
  commit, it exits 2 naming `branch-reconcile`; and with that kit's registry entry removed in one
  commit, it exits 2 naming it. `python constants.py . <root> <root>`, where `<root>` is the commit
  `git rev-list --max-parents=0 HEAD` prints, exits 2 printing `no declared constant resolved at both
  ends`.
  Red when: any of the six exits 0 or 1, or prints a traceback.
  fixture: the clone under `%TEMP%/fcd`, and the scratch roots under `%TEMP%/fce` and `%TEMP%/fcf`,
  made by the probe and removed after it.
- **AC12** — When `python constants.py . 7d98741e3~1 7d98741e3` runs, it prints `absent branch-reconcile`
  and `absent roles` beside unit 33 AC2's two lines. `python constants.py . 0baf2e47a~1 0baf2e47a`
  prints `new branch-reconcile 1.0`.
  Red when: an `absent` or `new` outcome is refused, dropped or misprinted.
  figure: the lines are PINNED, measured on 2026-10-23 at `7d98741e3` and `0baf2e47a`.
- **AC13** — When `tools/workflows/README.md` is sliced from its replay section heading to the next
  `## ` and its fenced bash lines are read, `grep -c "^\s*trap '"` over them prints 1, and a copy whose
  prose holds the word `trap ` still prints 1. In the workflows kit, `grep -cE
  "ls-files.{0,8}--literal-pathspecs" replay_scorer.py` prints 0, and the valid-path control of unit
  37 AC5 holds.
  Red when: a comment or a second section doubles the count, or the argv form reads as a miss.
- **AC14** — When `git grep -n "^- AC6 — "` runs over unit 36's acceptance ledger, the line it prints
  holds `precondition`.
  Red when: a criterion green at base is recorded as observing S8 and S9.
- **AC15** — When `grep -n -B12 "function deriveAddressKey" tools/workflows/tier2-review.template.js`
  runs, it prints the `function deriveAddressKey` line, and the comment it prints holds no `:1664` and,
  where it cites the instrument by line, holds `:1665-1666`.
  Red when: the grep prints nothing, which passed unit 37 AC15 vacuously.
- **AC16** — When `grep -c "^\*\*Serves:\*\*.*TOOL-dFairHearing-35"` runs over unit 30's verdict record,
  it prints 1.
  Red when: the record does not bind to unit 35.
- **AC17** — When a scratch python probe imports `tools/memory-tree/gotchas.py` at this unit's commit and
  applies `check_ungated` to every class record at unit 30's commit, with that commit's tracked paths
  and leg names, the set of classes it admits equals the `ungated` class set unit 35's `## Scoring`
  section names, or this unit's ledger names each class that moved.
  Red when: the shipped function and the recorded set disagree with nothing recorded.
- **AC18** — When `grep -E "dispatch · item [0-9a-f]+ TOOL-dFairHearing-36 · reason "` runs over the
  build's run-state file, the row it prints names the build folder among its writes, and the row for
  `TOOL-dFairHearing-37` does too.
  Red when: a pass's recorded write set omits the ledger record it commits.
- **AC19** — When a scratch stub-agent run of `tools/workflows/tier2-review.js` is given `repo` as
  `C:/x y/z`, every captured prompt's `git -C` command names `"C:/x y/z"` in double quotes, and given a
  `repo` holding `$`, the call throws naming `$`. `grep -c 'git -C \${repo}'
  tools/workflows/tier2-review.template.js` prints 0.
  Red when: a path holding a space splits into two arguments, or an unquoted interpolation remains.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `hook destinations self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `kit/dogfood doc parity` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `workflow script syntax` · `kit version markers` · `govkit selfcheck` · `review-replay selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `harness arms (fail branches armed or pinned)` · `testsuite counts (every bar self-test prints one)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC19 · a stub run whose `repo` holds a space, and one holding `$`, staged against the harness at `TOOL-dFairHearing-37`'s commit, where the interpolation is bare · FLOOR_ASSERTIONS in that suite, raised by the arms added
New arm: tools/lib/resolve-python.test.sh · covers AC10 · unit 37's rows 8 and 9 over the port at this unit's commit, staged with the port testing `isDirectory()` for `.git` · none

## 8. Open questions

- **F1 — One batch unit or two (BUILD-METHOD M4, M6)?** Options: (a) one; (b) two, split by the units
  the minors land on. §4 shows S1 reads a file S33 writes, so no split clears M6 clause 2 while S1 runs
  last. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — Quote or refuse a `repo` holding a space (S33)?** Options: (a) quote every interpolation and
  refuse only `"`, `$` and a backtick; (b) refuse any whitespace or shell metacharacter. (b) fails every
  caller whose checkout path holds a space. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3; it
  satisfies AC19 as (b) does and breaks no caller. widens: none · relaxes: none
- **F3 — Edit the prose carriers or state a non-goal (S16)?** Options: (a) on an `ungated` record, each
  carrier says the harness acquires its own checklist, reworded in unit 23 S45's form where it does
  not; (b) a non-goal stating that a caller's checklist keeps the selection. (a) satisfies the finding's
  consequence and reuses unit 23 S45's wording. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3;
  the only governance carrier it can touch, `memory/HYGIENE.md`, is one unit 23 S45 already rewords
  in the same form. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting the 19 MEDIUM and 16 LOW findings of the round-5 spec
  audit of specs 33 to 37 as one batch.

## 10. Reuse audit

Every item extends a seam an earlier unit mints or the base tree carries: units 33, 34 and 36's scratch
probes corrected in place, govkit's readers (`read_descriptors`, `resolve_version_value_at`,
`derive_registry_path` and `blob_at` in `tools/govkit/govkit.py`), `resolve_compare_base`
(`tools/codebase-map/map_lib.py:1502`), unit 35's attempt checker, `renderLexedView`
(`tools/hooks/agent-cap.js:720`), the README replay section and unit 23 S45's carrier wording.
`python tools/codebase-map/reuse_lookup.py "refuse a table row a parser recognises but cannot parse"`
ranked the generic `rows`, `row` and `parse` stems and no row-refusing reader, so no existing seam fits
the attempt-table refusal; it stays in the scratch checker. The recall query returned the audit's M3 and
M13 items, unit 35's checker, unit 36's `base.py`, and `DEPL-aHoistedPass-10` and
`TOOL-aBoundedVerdict-29`, two marker sites outside a gate's population, which S32's residual names.

Recall terms used: `python tools/memory-recall/query.py "a build-wide version check run once before later units edit kit files, and an attempt checker that drops rows" --terms "constants markers base.py resolve_compare_base attempts void after cap renderLexedView per-arm TEMP SCRATCH quoting repo"`
