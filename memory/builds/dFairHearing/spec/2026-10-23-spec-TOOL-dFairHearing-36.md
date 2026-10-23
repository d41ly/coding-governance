# TOOL-dFairHearing-36 — the round-4 spec audit's 13 minors on units 28, 29 and 31: probes that read every node's bytes alike, misses seen red, and the bar's own base

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 24 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-36-deviation-361.md](../build/2026-10-23-build-TOOL-dFairHearing-36-deviation-361.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-33-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-33-promoted-fix-brief.md) | research | TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-37 |
| [2026-10-23-prompt-TOOL-dFairHearing-36-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-36-1-spec-writer.md) | journal | — |
| [2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md) | spec-audit | TOOL-dFairHearing-35 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-37 |

<!-- /gen:spec-records -->

## 1. Goal

One of two batch units closes the MEDIUM and LOW findings that the round-4 spec audit confirmed
(`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md`) and
that land on units 28, 29 and 31. That is 13 report ids. MEDIUM ids: 3 (item M3), 11 (M7), 19 (M10),
27 (M14), 28 (M15) and 29 (M16). LOW ids: 7 (L2), 9 (L4), 15 (L5), 18 (L7), 21 (L5), 24 (L8) and 30
(L10). Each id is its own §2 item. The other 19 minors land on units 30 and 32 and are
`TOOL-dFairHearing-37`'s; the two write sets are disjoint by BUILD-METHOD M6, so the halves build
concurrently (§4). This unit builds after every unit it repairs. It makes each corrected statement
true on what those units built, and it observes what each criterion claimed. A criterion it
supersedes is named by the hands-off bullet in that unit's §3, and that unit's acceptance ledger
records it superseded here (`TOOL-dFairHearing-23` §8 F7's form).

## 2. Scope (IN)

Each item names its report id, its report item, the unit it lands on and the criterion that observes
it. Where a report item merges ids, the later id points at the first one's mechanism.

- **S1** — id 3 (M3, units 28 and 29). The move of the five escaped-quote arms is unit 28's alone,
  by its S3. Unit 29's S2 move sentence and its AC2 are answered here: at this unit's commit each of
  the five member labels occurs exactly once in `tools/workflows/spec-audit-optin.test.sh` (the
  pack's suite) and not at all in `tools/hooks/agent-cap.test.sh` (the hook's suite). A duplicate
  that the parallel passes left is cut here, with the surviving arm's label, payload and verdict
  unchanged. Observed by AC1.
- **S2** — id 11 (M7, unit 28, AC3). Unit 28 AC3's second half is restated so its copy reaches the
  population assertion: a copy of `census.py` that keeps the self-check and expects a population of
  60 and 14 prints `population 59 14` and exits naming `the population is not 59 and 14`. The figures
  66 and 54 are `grep -E`'s reading of the folded text, as unit 28 §4 Evidence states, and no copy of
  the script reproduces them, because Python refuses the folded pattern. Observed by AC2.
- **S3** — id 27 (M14, unit 28). `census.py` decodes `git show` as UTF-8, `encoding="utf-8"` beside
  `text=True`, the codec it reads the suites with, and writes its output as UTF-8 through
  `sys.stdout.reconfigure(encoding="utf-8")`. Without the second half, a label holding `→` raises
  `UnicodeEncodeError` on a cp1251 console once the first half lands. The result no longer depends on
  `PYTHONUTF8`. Observed by AC3.
- **S4** — id 28 (M15, unit 29). `members.py` takes S3's two changes. Observed by AC3.
- **S5** — id 29 (M16, unit 28). The placement half of `census.py` is seen red over three scratch
  copies: the hook's suite with the :1063 arm restored prints its `gone` line, the pack's suite with
  the :874 arm cut prints its `home` line, and `tools/workflows/check-review-join.test.sh` (the join
  suite) with the arm labelled `rule5: the Map ban fires` cut prints its `home` line. Each exits 1.
  Unit 26's AC3, the inline `grep -oE` census unit 28 S1 refuses, is answered by this. Observed by
  AC4.
- **S6** — id 30 (L10, unit 29). `label()` in `members.py` returns an empty label when a line holds no
  quote or its quote never closes, so the existing test names that line `not a member` instead of
  raising. Observed by AC5.
- **S7** — id 7 (L2, units 28 and 29). Unit 28's AC1 and AC3 and unit 29's AC1 read only
  `git show 3708a705:` through their own scripts and are green before any build, so their ledgers
  record them as precondition evidence. Acceptance of the move rests on unit 28's AC2 and this unit's
  AC1 and AC4, which a correct build can fail. NOT OBSERVED by a criterion here: it is the labelling
  of three ledger lines; AC1 and AC4 are the observations that can go red in their place.
- **S8** — id 15 (L5, unit 28 §10). The extractor the round-3 audit refuted as a census seam is
  `tools/lib/extract-arms.sh`. It requires a `PASS (N assertions)` total that the hook's suite does not
  print, so the refutation stands with the path corrected. Observed by AC6.
- **S9** — id 21 (L5, unit 29 §10). S8's defect in spec 29; S8 closes it. Observed by AC6.
- **S10** — id 24 (L8, units 28 and 29 §7). The suite receiving the moved arms is run by the leg
  `TOOL-dFairHearing-16` adds, `spec-audit opt-in pack self-test`. This unit's §7 names it in a prose
  sentence, because a leg line naming a leg absent at base is refused. Observed by AC7.
- **S11** — id 19 (M10, unit 31 S1, unit 32 S28). The version check's base takes `GATE_BASE`
  unchanged when it is set, verified by `git rev-parse --verify`, as `tools/run-gates/run-gates.sh:396-399`
  does. Unit 31 S1's and unit 32 S28's claim that the check uses the bar's base is then true. This
  supersedes the merge-base of `HEAD` with `GATE_BASE` in unit 31 §4. Observed by AC8.
- **S12** — id 9 (L4, unit 31). With no `GATE_BASE`, the base is `resolve_compare_base`'s answer
  (`tools/codebase-map/map_lib.py:1502`): the remote ladder's observed branch, or `main` when it names
  none, as `run-gates.sh` reads it (:376, :401), and its merge-base with `HEAD` where that is a proper
  ancestor. Where that function answers the remote tip, the probe exits 2 naming that the branch has
  nothing of its own to diff. Unit 31's S1 and its script then give one answer. Observed by AC8.
- **S13** — id 18 (L7, unit 31 §10). The probe calls `resolve_compare_base` instead of a third hand
  copy of the bar's rule, and the refusal of the tip fallback is its one recorded departure. Observed
  by AC8.

## 3. Non-goals (OUT)

- No re-review, and no fold into the specs of units 28, 29 and 31: each item makes the corrected
  statement true and reopens no severity.
- No HIGH finding: ids 22, 31 and 32 are `TOOL-dFairHearing-33`, `-34` and `-35`.
- No minor on units 30 and 32: those 19 are `TOOL-dFairHearing-37`'s.
- No new gate leg and no committed checker: the census, the member check and the base probe stay
  scratch probes, as units 26, 28, 29 and 31 resolved.
- No change to what a moved arm asserts, as unit 26 §3 states.
- No help page: `help/` covers no suite and no build-time check.

### Edges

- **consumes-from** `TOOL-dFairHearing-28` — `census.py`, its population and the move of the five escaped-quote arms, which S1 to S3, S5, S7 and S8 correct
- **consumes-from** `TOOL-dFairHearing-29` — `members.py` and the five member labels, which S1, S4, S6, S7 and S9 correct
- **consumes-from** `TOOL-dFairHearing-31` — the version check's base, which S11 to S13 correct
- **consumes-from** `TOOL-dFairHearing-16` — the leg `spec-audit opt-in pack self-test`, which S10 names and AC7 reads
- **hands-off** `TOOL-dFairHearing-40` — the round-5 spec audit's minors on this spec, ids 3, 7, 12, 16, 27, 30 and 39: `base.py`'s sha as the build-wide base, §4's sentence on units 33 and 34 superseded, AC3's suite read from `git show 3708a705:`, AC6 labelled precondition evidence in this unit's ledger, the pass's write set counting its ledger records, and the tip refusal naming both causes (its S3, S5, S11, S22, S27, S31 and S35)


## 4. Design

### Why two batch units, and where the line falls

The 32 minors land on five units. Those on units 28, 29 and 31 write at most
`tools/workflows/spec-audit-optin.test.sh` and `tools/hooks/agent-cap.test.sh`, and read those two,
`tools/workflows/check-review-join.test.sh`, `tools/gate-legs.json` and
`tools/codebase-map/map_lib.py`. Those on units 30 and 32 (`TOOL-dFairHearing-37`) write the workflows
README, `replay_scorer.py`, the harness template and render, `tier2-review.test.sh`, `gotchas.py`,
`tools/lib/resolve-python.test.sh`, `memory/map/generated/symbols.json` and two records, and read
neither suite this unit writes. Neither half writes a file the other reads (M6 clause 2). This unit
defines no function and cuts none, so the generated `symbols.json` and its generator stay the other
half's alone (clause 3). M6 then requires the two to run concurrently.

### The member check, corrected (S1, S4, S6)

```python
# members.py <base-ref> [<hook suite> <pack suite>]
import subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")
LINES = (874, 959, 985, 988, 1063)
base = subprocess.run(["git", "show", f"{sys.argv[1]}:tools/hooks/agent-cap.test.sh"],
                      capture_output=True, text=True, encoding="utf-8", check=True).stdout.splitlines()
def label(line):
    if '"' not in line:
        return ""
    i = j = line.index('"') + 1
    while j < len(line) and line[j] != '"':
        j += 2 if line[j] == chr(92) else 1
    return line[i:j] if j < len(line) else ""
members = [label(base[n - 1]) for n in LINES]
for n, m in zip(LINES, members):
    print(f"member :{n} {m}")
bad = [f"not a member :{n}" for n, m in zip(LINES, members)
       if not m.startswith("rule0") or chr(92) + '"' not in m]
if len(sys.argv) == 4:
    hook, pack = (open(p, encoding="utf-8").read() for p in sys.argv[2:4])
    bad += [f"home {m}" for m in members if m not in pack]
    bad += [f"twice {m}" for m in members if pack.count(m) > 1]
    bad += [f"gone {m}" for m in members if m in hook]
print("\n".join(bad))
sys.exit(1 if bad else 0)
```

`census.py` is unit 28 §4's script with S3's two changes: `sys.stdout.reconfigure(encoding="utf-8")`
after its import line, and `encoding="utf-8"` in its `subprocess.run` call. The pass writes both files
with its file-writing tool under its scratch directory.

Measured on 2026-10-23 at `3708a705`, with the hook's suite given as every suite path. Unit 28's
script printed 73 `gone` lines with `PYTHONUTF8=1` and 13 with `PYTHONUTF8=0`; with the `encoding`
half alone it raised `UnicodeEncodeError` on `→` under `PYTHONUTF8=0`; with both halves it printed
73 under both settings. The member check above printed 5 `gone` lines under both settings, and with
864, a comment line holding no quote, in place of 874, it printed `not a member :864` and exited 1.

### The base (S11 to S13)

```python
# base.py <repo root> [<codebase-map kit dir>] — the version check's base: the merge bar's own rule
import os, pathlib, subprocess, sys
root = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, sys.argv[2] if len(sys.argv) > 2 else str(root / "tools" / "codebase-map"))
from map_lib import resolve_compare_base
def refuse(why):
    print(f"version-lines: no base, nothing diffed: {why}", file=sys.stderr)
    sys.exit(2)
if os.environ.get("GATE_BASE"):
    p = subprocess.run(["git", "-C", str(root), "rev-parse", "--verify", "-q", os.environ["GATE_BASE"]],
                       capture_output=True, text=True)
    if p.returncode or not p.stdout.strip():
        refuse(f"GATE_BASE does not resolve: {os.environ['GATE_BASE']}")
    base, how = p.stdout.strip(), "GATE_BASE"
else:
    base, how = resolve_compare_base(root)
    if base is None:
        refuse(how)
    if how.endswith(" tip"):
        refuse(f"HEAD is not ahead of {how[:-4]}, so the branch has nothing of its own to diff")
print(f"base {base} from {how}")
```

It prints the line unit 31's probe prints, so units 33 and 34 read its sha the same way. Measured on
2026-10-23: in this worktree it printed `base 3708a705… from merge-base of HEAD and origin/main`. In a
fixture clone whose `HEAD` equals its `origin/main` it exited 2. With `GATE_BASE=origin/side`, a
commit that is not an ancestor of `HEAD`, it printed that commit's sha, not the merge-base.

### Files touched (estimate)

- `tools/workflows/spec-audit-optin.test.sh`
- `tools/hooks/agent-cap.test.sh`

Each changes only where AC1 finds a member twice in the pack's suite or still in the hook's.

### Alternatives rejected

- **One batch unit for all 32 minors.** M6 requires disjoint passes to run concurrently, and §4 shows
  these two write sets are disjoint.
- **Keep unit 31's merge-base of `GATE_BASE` and reword S1 to state the departure.** The bar's base
  then has a second spelling in the build, and a later change trusting unit 32 S28 inherits the gap.
- **Reconfigure stdout only.** The `git show` text would still decode by the locale, and 60 labels
  would match no suite.

## 5. Production-readiness checklist

- security — N/A: read-only scratch probes and test suites; no new input or write path.
- perf / scale — one `git show` and up to three file reads per probe.
- error / empty / loading states — a short population exits before any suite is read; a member line
  with no quote is named, never a traceback; a base that cannot be derived exits 2 with its reason.
- observability — each probe prints its population, its member lines or its base before any failure.
- risks — a deliberate rewording of a label reads as missing; unit 26 §3 keeps labels byte for byte.
- testing — AC1 to AC8 as probes and fixtures; the pack suite's arms observed RED then GREEN at the
  close.
- migration — none.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

`census.py`, `members.py` and `base.py` are the scripts of §4, written under the pass's scratch
directory. A clone or fixture repository goes under `%TEMP%/<short name>`.

- **AC1** — When `python members.py 3708a705` runs at this unit's commit with the hook's suite and the
  pack's suite as its two paths (S1 names the files), it prints five `member` lines and no `home`, `twice`, `gone` or `not a
  member` line, and exits 0. Over a scratch copy of the pack's suite with the :874 arm pasted a second
  time, it prints a `twice` line naming that label and exits 1.
  Red when: a member sits twice in the pack's suite, stays in the hook's, or reaches neither.
- **AC2** — When a scratch copy of `census.py` that expects `(60, 14)` runs as `python <copy>
  3708a705`, it prints `population 59 14` and exits 1 naming `the population is not 59 and 14`.
  Red when: it exits 0, which means the population assertion cannot fire.
- **AC3** — When `census.py` and `members.py` each run with the hook's suite given as every suite path,
  once with `PYTHONUTF8=1` and once with `PYTHONUTF8=0`, each run prints the same count of `gone`
  lines under both settings, 73 for the census and 5 for the members, and no `Traceback`.
  Red when: the count differs between the two settings, or either run raises.
  figure: 73 and 5 are PINNED, measured at `3708a705` on 2026-10-23.
- **AC4** — When `census.py 3708a705` runs over three sets of scratch copies at this unit's commit,
  the hook's suite with the :1063 arm restored, the pack's suite with the :874 arm cut and
  the join suite (S5 names the file) with the `rule5: the Map ban fires` arm cut, it prints
  respectively a `gone` line, a `home` line and a `home` line naming that label, and exits 1 each time.
  Red when: any of the three exits 0, which means the placement half passes a planted miss.
- **AC5** — When a scratch copy of `members.py` with 864 in place of 874 runs, it prints `not a member
  :864` and exits 1, and prints no `Traceback`.
  Red when: a quote-less line raises `ValueError` instead of being named.
- **AC6** — When `git ls-files "*extract-arms.sh"` runs, it prints `tools/lib/extract-arms.sh` alone,
  no path under the workflows kit, and `grep -c "PASS (N assertions)" tools/lib/extract-arms.sh`
  prints a number above 0.
  Red when: the extractor sits at the path specs 28 and 29 cite, or no longer requires the total.
- **AC7** — When `grep -n -A6 '"spec-audit opt-in pack self-test"' tools/gate-legs.json` runs at this
  unit's commit, it prints that leg with an argv naming the pack's suite (S1 names the file).
  Red when: no leg runs the suite that receives the moved arms.
- **AC8** — When `python base.py .` runs at this unit's commit with `GATE_BASE` unset, it prints `base
  <sha> from merge-base of HEAD and origin/main`, where `<sha>` equals `git merge-base HEAD origin/main`.
  In a fixture clone whose `HEAD` equals its `origin/main`, it exits 2 before any `base` line. With
  `GATE_BASE` naming a fixture commit that is not an ancestor of `HEAD`, it prints that commit's sha.
  `grep -c "merge-base" base.py` prints 0.
  Red when: an explicit `GATE_BASE` is merge-based, the tip fallback is diffed, or the probe carries
  its own copy of the bar's rule.
  fixture: a one-commit source repository under `%TEMP%/fga` with a diverging branch `side`, cloned
  to `%TEMP%/fgb`, both made by the probe and removed after it.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `tier2-review self-test` · `unattended-build self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The leg `spec-audit opt-in pack self-test` runs the pack's suite once `TOOL-dFairHearing-16` adds it
to `tools/gate-legs.json`.

New arm: tools/workflows/spec-audit-optin.test.sh · covers AC1 · a member arm pasted twice, which this unit's cut leaves once, staged against the pack's suite at this unit's parent · none
New arm: tools/workflows/check-review-join.test.sh · covers none · the `rule5: the Map ban fires` arm AC4's join-suite case reads, staged with the Map ban cut from the ref-keyed join check unit 16's S3 builds · none

This unit writes no arm in the join suite. Its line re-observes the arm that unit 26 moved there,
because AC4's join-suite case reds only if that arm is present at this unit's commit. The hook's
suite takes no `New arm:` line: it only loses an arm, as unit 26 §7 states.

## 8. Open questions

- **F1 — One batch unit or two (BUILD-METHOD M4, M6)?** Options: (a) one; (b) two, split by the units
  the minors land on, 28, 29 and 31 here and 30 and 32 in `TOOL-dFairHearing-37`. §4 shows the two
  write sets disjoint by M6's three clauses, and M6 requires disjoint passes to run concurrently.
  RESOLVED (agent, 2026-10-23, delegated): (b), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting the 6 MEDIUM and 7 LOW findings of the round-4 spec
  audit of specs 28 to 32 that land on units 28, 29 and 31, as one of two batches.
- rev-2 · 2026-10-23 · §3 · the round-5 spec audit's disposal: a hands-off edge to TOOL-dFairHearing-40 (seven minors).

## 10. Reuse audit

Every item extends a seam an earlier unit mints or the base tree carries. The base probe calls
`resolve_compare_base` (`tools/codebase-map/map_lib.py:1502`), the bar's rule in Python, which
`python tools/codebase-map/reuse_lookup.py "resolve the merge base with the remote default branch or
refuse"` lists as a SEAM with fan-in 3, the row unit 31's reuse audit did not name. The census and
member scripts are units 28 and 29's, corrected in place. The recall query returned the audit's
M14 item, spec 29, and `TOOL-cFinalBerth-2`, a merge-base-equals-`HEAD` refusal that fired on every
published `HEAD`. S12's refusal of the tip fallback is weighed against it: it fires only where `HEAD`
is not ahead of the default branch, which a unit pass on a run branch never is, and a landed `HEAD`
has no version change of its own for this check to grade.

Recall terms used: `python tools/memory-recall/query.py "census and member probes that read git output by the locale codec, and a version base that merge-bases an explicit base" --terms "census members PYTHONUTF8 encoding utf-8 escaped quote label GATE_BASE resolve_compare_base merge-base planted miss"`
