# TOOL-dDeclaredLoop-58 — the LF-only criterion reads a counted, non-empty CLI output before it looks for a CR

**Status:** INPROGRESS · rev-2 · 2026-11-14 · node d · Tier-2 · base 0d9bdeb4 · streams tooling · order 5 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-58-deviation-581.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-58-deviation-581.md) | deviation | — |
| [2026-11-14-build-TOOL-dDeclaredLoop-58-deviation-582.md](../build/2026-11-14-build-TOOL-dDeclaredLoop-58-deviation-582.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-11-14-prompt-TOOL-dDeclaredLoop-58-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-58-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-dDeclaredLoop-58-build-brief.md](../prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-58-build-brief.md) | journal | — |
| [2026-11-14-prompt-TOOL-dDeclaredLoop-58-reground-brief.md](../prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-58-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
confirmed finding **id 51 at HIGH**, its item **H5**, alone in that item: the only observation of the
LF-only trailer CLI looked for a CR in an output nobody counted, so an empty output passed it.
`TOOL-dDeclaredLoop-38` closed at rev-3 reading `tokens HEAD`, a range that prints, and its arm in
`tools/memory-tree/routed_commits.py#run_selftest` asserts only that the captured bytes hold no CR; the
arm's own comment hands the count to this unit. This unit adds the count: one predicate that matches
the CLI's lines to the commits git lists before it looks for a CR, and the arm reads through it. It
repairs `TOOL-dDeclaredLoop-38`.

## 2. Scope (IN)

- **S2** — `check_lf_lines(out, shas)`, a module-level function of `tools/memory-tree/routed_commits.py`
  beside `check_trailer_parses`. It takes the bytes of a `tokens` run and the shas git lists for the
  same revisions, and returns a list of findings, empty when clean. First it asks that each non-empty
  line open with the next sha of `shas` followed by a space, with no line missing or extra; only when
  that holds does it look for a `b"\r"`. An empty `shas` is itself a finding, so the predicate never
  passes on nothing. Observed by AC1, AC2, AC3.
- **S3** — The `TOOL-dDeclaredLoop-38` arm in `tools/memory-tree/routed_commits.py#run_selftest` reads
  the fixture's `git rev-list HEAD` through the module's `run_git`, passes it and the captured stdout
  bytes to `check_lf_lines`, and prints each finding on a failure. Its label names both units' AC1
  and says, off win32, that the CR half is not live there while the count half is. Observed by AC4.

## 3. Non-goals (OUT)

- The criterion's range, rev-1's S1. `TOOL-dDeclaredLoop-38` rev-3 took it under its §8 F2, so its AC1
  and its arm read `tokens HEAD` at HEAD. The built code satisfies it, and it leaves this scope.
- A rewrite of `TOOL-dDeclaredLoop-38` AC1: that spec is CLOSED and frozen, and this unit re-observes
  its criterion through the predicate.
- The producer fix and the wrapper's CR strip: `TOOL-dDeclaredLoop-38`'s and
  `TOOL-dDeclaredLoop-23`'s, landed.
- A template rule that every absence criterion asserts a counted output first, the finding's
  left-shift: a governance carrier no clause of this build names. S2 and S3 are this criterion's
  instance, and the class is recorded at the close.
- Making the CR half live on a node whose default newline is LF: nothing can write a CR there.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-38` — the LF-only `commit_trailers.py` CLI and its declared `routed_commits.py` arm, whose criterion this unit re-observes

## 4. Design

### Evidence

Every probe below ran on node `d` at `0d9bdeb4` on 2026-11-14, git 2.54.0.windows.1, Python 3.15.2.
Each figure is PINNED to that run.

- In the repository `commit_trailers.build_fixture` plants, the memory-tree copy's
  `tokens HEAD` exits 0 and writes 3 sha-led lines and 0 CRs (PINNED, that run),
  its shas in the order `git rev-list HEAD` prints them.
- `tokens HEAD~3..HEAD` there exits 0 and writes 0 bytes (PINNED, that run).
  `tools/memory-tree/commit_trailers.py#main` catches the `OSError` of a range `read_commits` cannot
  read and returns 0.
- A scratch copy of `tools/memory-tree/commit_trailers.py` without its `reconfigure` line, run with
  `tokens HEAD` there, writes 3 sha-led lines and 3 CRs (PINNED, that run).
  It notes `unregistered-key check skipped: no edges.toml` on stderr only, the floor
  `TOOL-dDeclaredLoop-40` built.
- The arm at HEAD passes on the empty output: it asserts `b"\r" not in out38` and nothing else.
- `tools/memory-tree/routed_commits.py#run_git` returns a call's stdout as bytes, under `build_git_env`
  less `GIT_ENV_LEAKS`, with the repository named by `-C`.

### The predicate

```python
def check_lf_lines(out: bytes, shas: list) -> list:
    # [] when clean; else one finding: no expected commit, the lines against shas, or a CR
    if not shas:                                   -> "no commit to compare against"
    lines = non-empty parts of out.split(b"\n")
    if [line[:40] decoded] != shas or a line's byte 41 is not b" ":
                                                   -> the count and the shas read, against git's
    return ["a CR reached the output"] if b"\r" in out else []
```

The line match runs first, so an empty or short output is named as such and never reaches the CR
read. Splitting on `b"\n"` alone keeps a CR at each line's end, so CRLF output passes the match and is
then named by the CR read. The expected shas are DERIVED from `git rev-list HEAD` at each run, so a
fixture that gains a commit moves the expectation with it (§8 F2).

### The arm

The existing block in `run_selftest` keeps its fixture, its spawn and its environment. It gains one
`run_git(fix38, "rev-list", "HEAD")` read, decoded as ASCII and split, and calls
`check_lf_lines(out38, shas)` in place of its bare CR test. Its comment that it counts no lines goes,
since it now does.

### The probe the criteria share

```bash
K="$PWD/tools/memory-tree"; S=$(mktemp -d)
R=$(python -c "import sys; sys.path.insert(0, sys.argv[1]); import commit_trailers as c; print(c.build_fixture(sys.argv[2]))" "$K" "$S")
(cd "$R" && python "$K/commit_trailers.py" tokens HEAD) > "$S/a"
python -c "import pathlib, sys; sys.path.insert(0, sys.argv[1]); import routed_commits as r
shas = r.run_git(sys.argv[3], 'rev-list', 'HEAD').decode('ascii').split()
print(r.check_lf_lines(pathlib.Path(sys.argv[2]).read_bytes(), shas))" "$K" "$S/a" "$R"
```

AC2 and AC3 swap only the line that writes `$S/a`.

### Files touched (estimate)

- `tools/memory-tree/routed_commits.py`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **The count PINNED at three.** It holds today and goes red the day the fixture grows, while the shas
  `git rev-list HEAD` prints follow the fixture and also catch a line that names the wrong commit.
- **The count and the CR read inline in the arm.** Nothing outside the suite could call them, so every
  criterion would need the whole selftest run over a staged scratch kit (§8 F3).
- **`HEAD~2..HEAD`.** It prints two of three commits and keeps a range whose length the fixture fixes
  by hand; `tokens HEAD` follows the fixture.
- **Asserting a non-zero exit is red.** The CLI prints nothing and exits 0 on a range it cannot read,
  as the evidence shows; the line match is the observation that cannot pass on nothing.

## 5. Production-readiness checklist

- security — no new surface: the predicate reads bytes it is handed, and the arm's spawn is unchanged.
- perf / scale — one more git spawn in the selftest, over a fixture of a few commits.
- error / empty / loading states — an empty output and an empty `shas` are each a finding of their own.
- observability — the arm prints the finding, which names the line match or the CR, and the bytes read.
- risks — the predicate and the CLI can disagree only on order, and both walk `HEAD` the same way.
  Every surface the change could move is accounted for below.
- testing — AC1 to AC4 as probes; the arm under §7, observed RED and GREEN at the close.
- migration — none.
- user docs — none: no page under `help/` names this selftest arm.

### Write set and what keeps each neighbour green

| Surface | What the change does to it |
|---|---|
| `memory/map/generated/symbols.json` | gains `check_lf_lines`; `python tools/codebase-map/gen_map.py --write` regenerates it, as `TOOL-dDeclaredLoop-37` did for `check_trailer_parses` |
| `tools/govkit/usage.toml` row `script:{prefix}/memory-tree/routed_commits.py` | unchanged: no flag is added |
| `tools/govkit/registry.toml`, `tools/playbook/namespaces.toml`, `tools/playbook/edges.toml` | unchanged: no file, kit, tag or trailer key is minted |
| subject pins | unchanged: no gate leg is added |
| `DELEGATES` in `tools/memory-tree/check-verdict-epoch.sh` | already lists `routed_commits.py`; the version bump it asks is minted by the lander, per that file's header |
| the watch list of `memory/guides/SESSION-KICKOFF.md` | does not name `routed_commits.py`, so no re-stamp is owed |
| the install-prefix ban | the arm names the CLI as `KIT / "commit_trailers.py"` and spells no kit path |
| the `TOOL-dDeclaredLoop-37` AC3 live arm, `check_trailer_parses` over the tool root | the new code spells no trailer parse |
| the `TOOL-dTrueNorth-31` AC6 probe in `tools/check-spec-tokens.test.sh` | counts `, env=env)` in the module's source as exactly one; the new code adds none |
| `memory/project/positional-refs.txt` | cites lines of this file in landed records; `TOOL-dDeclaredLoop-37` added a function here with no edit to it |
| the arms of `TOOL-dDeclaredLoop-39` and `TOOL-dDeclaredLoop-40` | read the same `commit_trailers` import and their own fixtures, untouched |
| `policy fixtures`, whose `PASS_LANE_FILES` in `tools/policy/check_policy.py` runs this file as the pass lane's grader | the grading path and `main` are untouched; the change sits in a new function and in `run_selftest` |
| `recall floor` and `recall floor arms`, whose guard covers `memory/` | tripped by the regenerated symbol map alone; UNVERIFIED that either reads it, so both sit on the §7 leg line and run at the close |

## 6. Acceptance criteria

- **AC1** — When the probe of §4 runs on win32 over the planted fixture, with `tokens HEAD` writing
  `$S/a`, `check_lf_lines` prints `[]`.
  Red when: the predicate counts the trailing LF as a line or reads a different order than git's
  walk, so a clean output is a finding.
  fixture: the repository `commit_trailers.build_fixture` plants; the tree holds none.
  figure: DERIVED, the expected shas are `git rev-list HEAD` over the fixture at observation time.
- **AC2** — When the same probe writes `$S/a` with `tokens HEAD~3..HEAD`, which writes nothing,
  `check_lf_lines` prints one finding naming the line count, and no finding names a CR.
  Red when: the predicate only looks for a CR, so the empty output prints `[]`, as the arm passes it at HEAD.
- **AC3** — When the probe writes `$S/a` from a scratch copy of `tools/memory-tree/commit_trailers.py`
  without its `sys.stdout.reconfigure(newline="\n")` line, run with `tokens HEAD` on win32,
  `check_lf_lines` prints exactly one finding, naming the CR.
  Red when: the predicate splits on line endings that eat the CR, or never reads bytes, so CRLF passes.
  permission: a win32 node; on a node whose default newline is LF the copy writes no CR, and the
  criterion is not observable there.
- **AC4** — When `grep -n "check_lf_lines(" tools/memory-tree/routed_commits.py` runs, it shows the
  definition and one call inside `run_selftest` passing `out38`, and `grep -c 'b"\\r" not in out38'`
  over the same file prints `0`.
  Red when: the arm keeps its bare CR test and the predicate has no caller in the suite.

## 7. Gates

`routed-commits selftest` · `policy fixtures` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC1 AC2 AC3 · the TOOL-dDeclaredLoop-38 arm through the predicate, staged for one run each by the range HEAD~3..HEAD in its spawn and, on win32, by deleting the reconfigure call from the memory-tree copy, each restored · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — What does the line match compare against?** Options: (a) a count PINNED at three, rev-1's
  figure, matching `TOOL-dDeclaredLoop-23`'s fixture as it stands; (b) the shas `git rev-list HEAD`
  prints over the fixture at each run, DERIVED, so the expectation moves with the fixture and a line
  naming the wrong commit is caught too. (b) costs one git spawn. Recommendation: (b), the charter's
  `[derive]`. The body is written on (b).
  RESOLVED (agent, 2026-11-14, delegated): (b), rung 3: a count derived from the fixture cannot go stale beside it.
  widens: none · relaxes: none
- **F3 — Where does the check live?** Options: (a) a module-level `check_lf_lines` the arm calls and a
  probe can import, which mints one symbol and so regenerates `memory/map/generated/symbols.json`;
  (b) inline in the arm, minting nothing, with every criterion observed by running the whole
  `--selftest` over a staged scratch copy of the kit. Recommendation: (a): its criteria are direct
  probes of the unit's own code, and `TOOL-dDeclaredLoop-37`'s `check_trailer_parses` set the shape in
  this file. The body is written on (a).
  RESOLVED (agent, 2026-11-14, delegated): (a), rung 3: a criterion observes the predicate directly, never through a suite.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's id 51 (HIGH, item H5).
- rev-2 · 2026-11-14 · §1 · S1 · S2 · S3 · §3 · §4 · §5 · AC1 AC2 AC3 AC4 · §7 · §8 F2 F3 · §10 ·
  re-grounded on `0d9bdeb4` by the brief `prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-58-reground-brief.md`.
  Satisfied by landed code and out of scope: S1, the range, which `TOOL-dDeclaredLoop-38` rev-3 took
  under its F2. Moved by reading HEAD: the empty range exits 0 and prints nothing rather than exit 128;
  the fixture comes from `build_fixture`, since `--fixture` deletes its own; the count becomes a
  predicate the arm calls, matched to `git rev-list HEAD` (F2, F3); AC4 observes the arm's wiring; the
  write set gains the symbol map, and §5 accounts for every neighbour.

## 10. Reuse audit

The seam is the `TOOL-dDeclaredLoop-38` arm in `tools/memory-tree/routed_commits.py#run_selftest`, its
fixture from `TOOL-dDeclaredLoop-23`'s `build_fixture`, and the module's own `run_git` for the sha
list; the predicate sits beside `check_trailer_parses`, the shape `TOOL-dDeclaredLoop-37` set in this
file. `python tools/codebase-map/reuse_lookup.py "count sha-led output lines against git rev-list
before asserting no carriage return in CLI bytes"` ranked `git`, `read_bytes`, `run_git`,
`check_line` of `tools/runlog/runlog_lib.py` and `read_git_output`; `run_git` is reused, and none of
the others matches a CLI's lines to a commit list, so no existing seam fits the predicate itself.

Recall terms used: commit_trailers tokens HEAD rev-list sha-led lines CRLF empty output count absence routed_commits run_selftest build_fixture
