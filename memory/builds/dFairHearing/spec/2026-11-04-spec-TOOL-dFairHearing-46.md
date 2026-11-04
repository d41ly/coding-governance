# TOOL-dFairHearing-46 — the bar's own reds in the replay scorer, and its stated-count reader

**Status:** CLOSED · rev-2 · 2026-11-04 · node d · Tier-1 · base f4120c83 · streams tooling · order 29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md) | journal | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-39 TOOL-dFairHearing-40 TOOL-dFairHearing-43 TOOL-dFairHearing-44 TOOL-dFairHearing-45 TOOL-dFairHearing-47 |
| [2026-11-04-build-TOOL-dFairHearing-46-1-acceptance-ledger.md](../build/2026-11-04-build-TOOL-dFairHearing-46-1-acceptance-ledger.md) | journal | — |
| [2026-11-04-build-TOOL-dFairHearing-46-1-builder-return.md](../build/2026-11-04-build-TOOL-dFairHearing-46-1-builder-return.md) | journal | — |
| [2026-11-04-build-TOOL-dFairHearing-46-deviation-461.md](../build/2026-11-04-build-TOOL-dFairHearing-46-deviation-461.md) | deviation | — |
| [2026-11-04-prompt-TOOL-dFairHearing-46-1-spec-writer.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-46-1-spec-writer.md) | journal | — |
| [2026-11-04-prompt-TOOL-dFairHearing-46-build-brief.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-46-build-brief.md) | research | — |
| [2026-11-04-prompt-TOOL-dFairHearing-46-spec-brief.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-46-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The close ran the bar's lint legs on this branch and on a frozen clone of BASE `8bec4cefd`. Four reds
that pass at BASE sit in `tools/workflows/replay_scorer.py`, so they are this build's own, and this
unit repairs them. It also repairs `extract_stated_count`, which read a synthesis's prose as the
stated count and voided replay attempt `f2s1`, and it renames the lexicon's one new offender in this
file, which no other unit may write.

## 2. Scope (IN)

Every item lands in `tools/workflows/replay_scorer.py`. Line numbers are read at `f4120c83`.

- **S1** — The encoding posture leg. The four text-mode `subprocess.run` calls at :848, :861, :1285
  and :1417-1418 each gain `encoding="utf-8", errors="replace"`, written on the line that holds
  `text=True`. Observed by AC1.
- **S2** — The drift-audit records leg. `PROOF_DIR` and `HELD_OUT_FILE` (:1257, :1279) spell no spec
  id. The proof finds each of its three records by name ending under the build's folder, through a
  nested `derive_proof_path`. Observed by AC2.
- **S3** — The govkit selfcheck leg. `check_case`'s docstring (:651) cites `adopter ic` and the grader
  blob in place of the brand. Observed by AC3.
- **S4** — The install-prefix leg. The `pairing-walk` arm (:1380, :1382) derives its planted path from
  `KIT_DIR`, so it spells no kit path. Observed by AC4.
- **S5** — The stated-count reader. `extract_stated_count` (:270-273) reads the harness's
  `review-shape` line first, and today's `STATED` read only when a report carries no such line. A new
  selftest arm, `stated-shape`, holds the class, and `ARMS_DECLARED` moves 25 to 26. Observed by AC5.
- **S6** — The lexicon's ninth new verb offender. The function `names`, nested in `scan_pairing_sites`
  (:1214), takes the name `extract_names`, and its four calls (:1232, :1242, two on :1246) move with
  it. It stays nested. Observed by AC6.

## 3. Non-goals (OUT)

- No gate for S1 to S4 or S6: each leg already grades its own item.
- No catalogue record. The arm fits the class, so `memory/gotchas/INDEX.md` is not declared here.
- No re-scoring of `f2s1`. Its void is true of the scorer blob the run read, `36043efc`, and unit 30's
  record and unit 35's scoring are frozen. See "What this leaves as it is".
- No change to the harness's writer, `tools/workflows/review_replay.py` or `tools/workflows/README.md`.
  The README's liveness paragraph (:1012-1016) names a stated count and no way of reading one, so it
  stays true.
- Not the 165 records that `parse_record_findings` refuses with `liveness` under both readers. They
  are the legacy table's own, and this unit moves none of them.
- Not the other reds in these legs: `tools/workflows/README.md`'s citation, the kit spellings outside
  this file and the lexicon's other offenders are unit 45's. No pin moves here.
- No help page: no page under `help/` mentions the replay scorer (read at `f4120c83`).

### Edges

- **hands-off** `TOOL-dFairHearing-45` — this unit lands the replay scorer's two install-prefix lines, its drift citation and the `extract_names` rename, and leaves that unit the rest of those legs: its own offenders and the lexicon count's return to the pin

## 4. Design

### Tier

Tier-1. Five items are mechanical. S5 adds one reader of a line the harness already writes, with no
new write path and no change to the record's grammar.

### Encoding (S1)

The keyword is what the leg asks for. `errors="replace"` is the file's own posture on git's text
(:144, :1209), and it keeps a byte that does not decode from raising past `read_git`'s refusal. A
replaced byte in a path fails the `listed != [rel]` compare and refuses by name.

### The proof's records (S2)

The drift signal greps each non-terminal spec's own id as a whole word across product source
(`tools/drift-audit/drift_report.py:740`). Every `TOOL-aScoutedSeam-*` spec is SPECCED, and these two
constants spell one only because a record's file name carries it. The proof reads a build's records,
so the slug and each name's ending are all it needs.

```python
PROOF_DIR = "memory/builds/aScoutedSeam/build"
HELD_OUT_FILE = "-1-13-held-out-cases.json"  # the record's name ending under PROOF_DIR
```

Nested in `run_selftest`, beside `check_refused`:

```python
    def derive_proof_path(ending):
        """The one record under `PROOF_DIR` whose name ends `ending`, repo-relative; refused unless exactly one does."""
        found = sorted(pathlib.Path(top, PROOF_DIR).glob("*" + ending))
        if len(found) != 1:
            raise Refusal(f"proof: {len(found)} record(s) under {PROOF_DIR} end {ending}, not one")
        return found[0].relative_to(top).as_posix()
```

The three read sites become `derive_proof_path("-1-3-cases.json")`,
`derive_proof_path("-1-5-results.json")` and `derive_proof_path(HELD_OUT_FILE)`: :1339 in
`check_scouted_proof`, and :1546-1547 in `check_union_arm`. Each caller already returns `no_tree`
when `top` is None, and a refusal reaches the runner as a `FAIL`, so a moved record is a red and
never a skip. Measured at `f4120c83`: each ending matches one file, and the working tree's path of the
cases and of the results reads at both `PROOF_COMMIT` and `UNION_PROOF_COMMIT`.

### The adopter citation (S3)

```python
    wrong one: `resolveEntryImage` and `imageField` share a file in adopter ic (grader blob a0389611).
```

The leg's message asks for the record id and the adopter's short name. The record the sentence came
from is the grader, whose file name spells `TOOL-aScoutedSeam-1`, and citing that id would re-open
S2's red. So the citation is the blob, the id this file already cites the grader by (:36, :620).
`tools/govkit/adopters.toml` gives `ic` as the short name.

### The planted path (S4)

```python
            factory = f"{KIT_DIR.name}/planted.py"
            copy = derive_git_tree(pathlib.Path(tmp, "copy"), {factory: PLANTED, f"{MEMORY_ROOT}/b/planted.py": PLANTED})
            named = scan_pairing_sites(copy)
            if named != [f"{factory}:2"]:
```

The arm still plants one module under a factory directory and one under `memory/`. Read against
`tools/check-install-prefix.sh`, the spelling matches none of its rules, because the character before
the `/` is a brace closing a name and not a kit.

### The stated count (S5)

The `f2s1` report (blob `decf0ad2`, in its clone) reads, in order:

```text
By raw confirmed finding the tally is the same: 3 confirmed, 0 blocker, 0 high, 1 medium, 2 low.
Review shape: intensity full, raw 3, confirmed 3, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.
review-shape kind=diff-review round=1 intensity=full at=synth raw=3 confirmed=3 refuted=0 merged=0 ...
```

`STATED` takes the first `confirmed` followed by a number, so a count written before its noun hands
it the next noun's count. The third line is `renderShapeLine`'s
(`tools/workflows/tier2-review.template.js:80-85`), and the synthesis copies it verbatim above the
appendix heading (:2854). It is the one count the harness computes rather than an agent phrases.

```python
#: The count as the harness states it: the `review-shape` line the synthesis copies above the appendix.
SHAPE_STATED = re.compile(r"^\W*review-shape\b.*?\bconfirmed=(\d+)", re.IGNORECASE | re.MULTILINE)
```

```python
def extract_stated_count(text):
    """The `review-shape` line's count, else the first number after the word `confirmed`, from before any appendix."""
    head = text.split(APPENDIX_HEADING, 1)[0]
    m = SHAPE_STATED.search(head) or STATED.search(head)
    return int(m.group(1)) if m else None
```

Each candidate was run over every tracked `memory/builds/*/reviews/*.md` plus the `f2s1` report, 751
files, 279 of them with an appendix whose confirmed rows give the true count. The figures are PINNED,
measured at `f4120c83`.

| Reader | Right of 279 | `parse_record_findings` against today |
|---|---|---|
| today's `STATED` | 275 | the baseline |
| the first line naming `raw` or `shape` | 275 | not run: `f2s1`'s prose line itself says "raw" |
| `review-shape` line or `Review shape:` sentence, then `STATED` | 279 | corrects 4, and refuses a record that parses today |
| `review-shape` line alone, then `STATED` | 279 | corrects 4, regresses none, 747 unchanged |

The last row is this design. The four it corrects are `f2s1` and three committed records, each of
which writes its number before its noun. `TOOL-dLoggedFlight-1`'s round-1 closing review is the one
the sentence form regresses. Over the nine replay reports, eight parse as they did and `f2s1` now
reads its 3 rows.

The fallback is live. No report-shaped fixture in `tools/workflows/review_replay.py` carries the line,
and unit 43's AC2 hands `parse_appendix_rows` a bare `confirmed <n>` line, so the arm's controls hold
that form to its answer and unit 43 owes nothing here.

The arm, appended to the `arms` list as `("stated-shape", check_stated_shape_arm)`:

```python
    def check_stated_shape_arm():
        """TOOL-dFairHearing-46 AC5: the count is the `review-shape` line's, so prose reading `3 confirmed, 0 blocker`
        above it reads 3 and never 0; a line disagreeing with the rows still refuses; with no line, `STATED` still reads."""
        prose = "By raw confirmed finding the tally is the same: 3 confirmed, 0 blocker, 0 high, 1 medium, 2 low.\n\n"
        line = "review-shape kind=diff-review round=1 intensity=full at=synth raw=3 confirmed={n} refuted=0\n\n"
        table = (APPENDIX_HEADING + "\n\n| id | lens | ref | verdict |\n|---|---|---|---|\n"
                 + "".join(f"| {i} | l | a.py:{i} | confirmed |\n" for i in (1, 2, 3)))
        rows, err = parse_appendix_rows(prose + line.format(n=3) + table)
        if err or len(rows) != 3:
            return f"a report whose prose leads read {err or rows!r}"
        _, err = parse_appendix_rows(prose + line.format(n=2) + table)
        if not (err or "").endswith("stated confirmed count of 2"):
            return f"a shape line disagreeing with its rows read {err!r}"
        want = [("confirmed 2\n", 2), ("Review shape: raw 1, confirmed 1, refuted 0.\n", 1), ("no count here\n", None)]
        return next((f"{t!r} read {extract_stated_count(t)!r}, not {w!r}" for t, w in want if extract_stated_count(t) != w), None)
```

Measured in a scratch probe at `f4120c83`: today's reader fails it with the `liveness ... of 0` message,
the reader above passes it, and that reader without its `STATED` branch fails on `confirmed 2`.
`ARMS_DECLARED` (:121) moves to 26, and its comment gains "Raised 25 -> 26 by TOOL-dFairHearing-46 S5:
stated-shape."

**What the arm does not check.** It reads no JavaScript, so nothing compares `SHAPE_STATED` to
`renderShapeLine`. A renamed `confirmed=` field leaves the writer's own pin to catch it
(`tools/workflows/tier2-review.test.sh:2022`), and the reader falls back to `STATED` with no notice. A
report that omits the line also falls back, and its prose can still misread. In both cases the
liveness compare refuses unless the misread number happens to equal the row count.

### The local name (S6)

The lexicon's `P1 verb` arm names `names` at :1214, the only line of this file it lists. `--suggest`
calls that name a scoping question among the declared verbs and answers `OK` for `extract_names`
(`--as py.function`, read at `f4120c83`). `extract` is the verb of this file's closest sibling,
`extract_code_tokens`, and the function pulls the `ast.Name` ids out of a node.

The rename is local: no name outside `scan_pairing_sites` calls it, and nothing else in the file spells
`extract_names`. It takes the offender count from 1220 to 1219 (PINNED at `f4120c83`), and unit 45's
AC6 brings the count back to the pin of 1211.

### What this leaves as it is

`f2s1` stays void in unit 30's record, because the cell is true of the scorer that run read. Unit 35's
rule scored `f2s2` from that record, and both are frozen. Unit 40's `void.py` read that cell through
`parse_candidates`, and it was never committed, so nothing in the tree re-derives it. Run again after
this unit, the same read would call `f2s1` parsed.

### Generated files

This write set pairs no generated file with its generator. `replay_scorer.py` generates nothing,
`gotchas.py` and `memory/gotchas/INDEX.md` are not declared, and no `[[regenerate]]` row of
`tools/workflows/kit.toml` reads this file. `memory/map/generated/symbols.json` holds public
module-level functions and classes, with no constants, no nested functions and no line numbers, so
`derive_proof_path`, the arm, `SHAPE_STATED` and `extract_names` add no row, and `names` has none to
give up. That is why the helper is nested beside `check_refused` and not set beside `read_proof_tree`,
and why the rename stays nested. No kit version moves on the branch: the lander
mints it (`tools/govkit/govkit.py:13845-13846`).

### Rollout

The new comments cite this unit's id, which the drift signal counts as product-source evidence until
the header reads CLOSED. The bar runs after that flip, as it does for every unit of this build.

Units 43 and 44 share order 29. Unit 43 writes no path of this unit's product set. Unit 44's three
status renders below are also this unit's, so the two passes run one after the other, as unit 44's
Rollout says of itself and unit 43.

### The header's ask clause

The header carries neither `closes` nor `advances`, for the reason unit 43's Design section gives under
this same heading.

### Files touched (estimate)

- `tools/workflows/replay_scorer.py`
- `memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-46-1-acceptance-ledger.md`
- `memory/builds/dFairHearing/spec/2026-11-04-spec-TOOL-dFairHearing-46.md`
- `memory/builds/dFairHearing/README.md`
- `memory/LIVE.md`
- `memory/backlog/TOOL.md`

The last three are the renders the status flip forces, as unit 44 declares them. The departure record
`2026-11-04-build-TOOL-dFairHearing-46-deviation-461` is written beside this spec and is not the
builder's.

### Alternatives rejected

- **Build the id at run time, as `"TOOL-" + slug + "-1"`.** It hides the same citation from the grep,
  which is the exemption the leg's shrink-only set exists to refuse.
- **Name the cases and results by blob id, as `GRADER_BLOB` does.** That is four constants across two
  commits, and the held-out read still needs a working-tree path, so it would need the helper as well.
- **Unit 45 renames `names`, or drains another offender to balance the count.** Its F1 weighs both: the
  first breaks the disjoint write sets, and the second leaves a new name standing behind an unrelated
  rename.
- **Flip `TOOL-aScoutedSeam-1`'s status.** It is another build's spec and outside this write set.
- **A module-level `derive_proof_path`.** It adds a `symbols.json` row, which puts a generated file in
  a write set that needs none.
- **Skip a `confirmed` that follows a number.** It reads `3 confirmed, 0 blocker` right and leaves the
  three committed records with no count, 276 of 279, because their prose has no other `confirmed <n>`.

## 5. Acceptance criteria

- **AC1** — When `grep -n "text=True" tools/workflows/replay_scorer.py | grep -vc "encoding="` runs, it
  prints 0.
  Red when: a text-mode `subprocess.run` names no encoding, as four do at `f4120c83`, where it prints 4.
- **AC2** — When `git grep -c -w -F "TOOL-aScoutedSeam-1" -- tools/workflows/replay_scorer.py` runs, it
  prints nothing, and `python tools/workflows/replay_scorer.py --selftest` prints `ok scouted-proof` and
  `ok experiment-union`, neither as a `SKIP` line.
  Red when: the file spells the id, as it does at `f4120c83` on two lines, or an ending resolves to no
  record, so the arm prints `FAIL`.
  fixture: the three records under `memory/builds/aScoutedSeam/build`, which the tree holds today.
- **AC3** — When `grep -icE "incms|nicocares|swydee" tools/workflows/replay_scorer.py` runs, it prints 0,
  and `grep -n "adopter ic" tools/workflows/replay_scorer.py` prints one line holding `a0389611`.
  Red when: the file names an adopter by brand, as it does once at `f4120c83`, where the first prints 1.
- **AC4** — When `grep -c "tools/workflows/" tools/workflows/replay_scorer.py` runs, it prints 0, and
  `python tools/workflows/replay_scorer.py --selftest` prints `ok pairing-walk`.
  Red when: the arm spells a kit path, as two lines do at `f4120c83`, where it prints 2, or its planted
  file lands where `scan_pairing_sites` skips it, so the arm prints `FAIL`.
- **AC5** — When `python tools/workflows/replay_scorer.py --instance review-replay --known memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-64-spec-audit.md --candidate memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-64-spec-audit.md`
  runs, it exits 0 and prints `replay: recall 26/26 = 1.00`, and
  `python tools/workflows/replay_scorer.py --selftest` prints `ok stated-shape` and
  `replay_scorer selftest: 26/26 arms`.
  Red when: prose ahead of the shape line sets the count. At `f4120c83` this record exits 2 naming
  `liveness`, 26 rows against a stated 0, because its prose reads `26 confirmed, 0 refuted`.
  figure: 26 is PINNED, the confirmed rows of a frozen record. The arm count is `ARMS_DECLARED`.
- **AC6** — When `python tools/lexicon/lexicon.py --list | grep -c "replay_scorer.py"` runs, it prints 0,
  `grep -c "\bnames(" tools/workflows/replay_scorer.py` prints 0, and
  `python tools/lexicon/lexicon.py --suggest extract_names --as py.function` prints a line opening `OK`.
  `python tools/workflows/replay_scorer.py --selftest` prints `ok conformance` and `ok pairing-walk`,
  the arms that run the renamed function.
  Red when: the name stands, as it does at `f4120c83`, where the first prints 1 and the second 4, or a
  call keeps the old name, so `scan_pairing_sites` raises and those arms print `FAIL`.

## 6. Gates

`review-replay selftest` · `encoding posture (text IO names its encoding)` · `drift-audit records` · `govkit selfcheck` · `install-prefix (shipped surface)` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `testsuite counts (every bar self-test prints one)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/replay_scorer.py (its runner, in the `review-replay selftest` leg) · covers AC5 · the `stated-shape` arm, staged against `f4120c83`, where a report whose prose reads `3 confirmed, 0 blocker` above its `review-shape` line is refused with `liveness` naming a stated 0 · `ARMS_DECLARED` 25 to 26

AC1 to AC4 and AC6 take no arm, because their legs are the gate and each already reds. The edit to the
`pairing-walk` arm keeps its assertion, so it is no new arm. `drift-audit records` and
`install-prefix (shipped surface)` and `lexicon naming predicates` stay red after this unit until unit
45 lands its share.

The four verdicts of S1 to S4 are derived from each leg's source and the file's text, not from leg output.
This spec's author may run none of these legs, so the main loop reads their first real output at the
close.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-04 · S1 to S5 · AC1 to AC5 · initial draft: the four lint reds this build owns in the
  scorer, and the stated-count reader, from brief `2026-11-04-prompt-TOOL-dFairHearing-46-spec-brief`.
- rev-2 · 2026-11-04 · S6 · AC6 · the lexicon's ninth new verb offender, `names`, renamed
  `extract_names` and kept nested, taken from unit 45's fork F1 at the coordinator's request, with the
  Goal, Tier, Generated files, Alternatives rejected and Gates text that moves with it.
- rev-2 · 2026-11-04 · S6 · the Non-goals section gains the `hands-off` edge to
  `TOOL-dFairHearing-45`, mirroring the `consumes-from` that unit declares on this one.

## 9. Reuse audit

Each item extends a seam the file already carries: `extract_stated_count` and `STATED` for S5, the
nested helpers of `run_selftest` beside `check_refused` for S2, and the `arms` list with
`ARMS_DECLARED` for the new arm. S6 renames in place and extends nothing. `python tools/codebase-map/reuse_lookup.py "read a stated count from a
report's machine shape line"` ranked generic name stems only, and so did `"find a committed record file
by its name suffix under a build folder"`, so no existing seam fits either reader beyond those. The
recall query returned this unit's brief and `TOOL-dTieredTribunal-16`, the ask behind the harness
computing the counters a record states, which is why the machine line is the one to trust.
`gotchas.py --for-paths` named `guard-above-a-fold-makes-its-fallback-dead` and
`fixture-passes-by-finding-nothing`, and the arm's controls answer both.

Recall terms used: `python tools/memory-recall/query.py "a stated confirmed count read off the prose of a review report instead of its shape line" --terms "stated count confirmed review-shape liveness appendix parse_candidates extract_stated_count synthesis prose void attempt"`
