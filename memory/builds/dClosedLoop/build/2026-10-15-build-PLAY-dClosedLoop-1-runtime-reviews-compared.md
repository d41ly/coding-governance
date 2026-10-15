# Research: the runtime design's two Tier-2 rounds, compared

**Serves:** research PLAY-dClosedLoop-1

The owner asked for two medium-effort Tier-2 rounds on the runtime layer's design, "and compare results
to spot any gaps". This record compares them defect by defect, says what one round alone would have
missed, and points each defect at where the fold put it in
`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`.

## [runs] The two rounds

- **Subject:** the runtime record at blob `767187aa4073f6e64cb2b2ef6b798f0a538347fd` (commit `6cfd21619`).
- **Harness:** `tools/workflows/tier2-review.js`, with five lenses (`gov-spec-reviewer`), five skeptic
  batches (`gov-skeptic`) and synthesis (`gov-synthesizer`), every role at medium effort, as the owner
  asked.
- **Run A** was `wf_6508cb22-7d6`, and its report is
  `reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md`.
- **Run B** was `wf_3c895b43-8da`, and its report is
  `reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-b.md`.
- **How the args differed:** only in the context's run label ("this is run A" or "run B") and in the
  report path. Run B's args follow, verbatim. Run A's differ only in those two strings.
- **The admission:** agent-cap's rule 0 refused run A at first, so the owner ruled on a one-off
  opt-in. The session log's `Events` section records it.
- **The ledger:** the roles kit derived both runs' agent and returned lines. They are held in the
  session log, and `[instrument]` sums their output from there.

```json
{
  "kind": "spec-audit",
  "repo": "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297",
  "subjects": [{"path": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md", "blob": "767187aa4073f6e64cb2b2ef6b798f0a538347fd"}],
  "scratch": "<the session scratchpad>/review-runtime-b",
  "reviewDir": "memory/builds/dClosedLoop/reviews",
  "round": 1,
  "intensity": "full",
  "roles": {"specFinder": "gov-spec-reviewer", "skeptic": "gov-skeptic", "synthesis": "gov-synthesizer"},
  "efforts": {"specFinder": "medium", "skeptic": "medium", "synthesis": "medium"},
  "specs": [
    "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
    "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md",
    "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md",
    "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-executor.md",
    "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-spawn.md",
    "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-hooks.md",
    "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-sessions.md"
  ],
  "context": "The subject is the runtime layer's design record for build dClosedLoop, a design-only build that re-architects gov onto one loop. The owner handed this layer's framing and architecture to the main loop, and asked for two independent medium-effort Tier-2 rounds on it, whose results are compared to spot gaps; this is run B. Audit the record as an architecture spec, against six questions: (1) internal consistency: do its components, invariants, policies, build units, fixtures and gaps agree with each other; (2) consistency with the sibling records in specs: v2's principles and chain, the flow's step definitions, the roles layer; (3) feasibility against the measured platform facts in the four runtime research returns in specs: a mechanism the platform cannot support, or a claim the returns do not bear out; (4) missing mechanisms: anything Runtime must do for the other layers that the design omits; (5) claims that are unenforced or untestable as written; (6) extension points that could not in fact be filled without changing Runtime's code. Address each finding by the record's section tag, such as [decide], [supervise], [act], [spawn], [enforce], [isolate], [sessions], [schedule], [harness], [extend], [invariants], [contract], [policies], [build], [tests] or [gaps-proposed]. Write the report to memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-b.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** spec-audit PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else.",
  "byDesign": "- The build is design-only: no product code and no unit specs; each chain build writes its own specs later, so unit-level implementation detail is absent by design.\n- The fixtures in [tests] are owed by the chain build and were not run here.\n- The defaults in [policies] were set by the main loop under the owner's explicit delegation of this layer.\n- The [questions] are held on purpose until the review rounds are folded.\n- Leases, the mailbox and the position function belong to dDeclaredLoop (its coordination feature and loop kit); Runtime executes them.\n- Records outside memory/builds/dClosedLoop/ are not under review, and the research returns are evidence, not subjects.",
  "checklist": "<the output of gotchas.py over the subject: 11 classes, 5 by anchor and 6 universal>"
}
```

## [method] How the rounds were compared

Each finding names a defect, and several findings can name one. The map in `[map]` places every
finding of both rounds, confirmed or refuted, on the defect it names. The placement is the main
loop's judgment, so the map is shown whole. A finding that names two defects is placed on both.

The instrument in `[instrument]` reads the two reports' appendix tables, the map, and the returned
lines in the session log, and derives every number below. It refuses when:
- a report holds a finding id that the map does not place;
- the map names an id that a report lacks;
- a run has no returned lines.

It was seen red on two planted copies before it was trusted, and that output is kept with it.

A defect counts as **found** by a round when at least one of that round's findings on it was
confirmed. Its grade in a round is the highest grade any confirmed finding on it got, using the
skeptic's grade where one was given.

## [numbers] What the instrument derived

The instrument's output, verbatim. A defect's grade is 3 for high and 2 for medium.

```text
== runs
A: raw 60, confirmed 56, refuted 4, precision 0.93, high findings 6, agents 12, out 212.2k (sum of returned lines)
B: raw 61, confirmed 57, refuted 4, precision 0.93, high findings 9, agents 12, out 218.0k (sum of returned lines)
== defects
map rows 61, confirmed defects 59, refuted-only 2
both 32, A only 14, B only 13
A alone covers 46 of 59 (78%)
B alone covers 45 of 59 (76%)
overlap (Jaccard) 0.54
Chapman estimate of the population: 64.5, so about 6 found by neither
A only: driver-cwd, binding-events, compaction-checks, cli-floor-decision, permission-mode, parallel-cleared, core-sweep, journal-owner, next-readers, gap-keys, command-idempotence, reap-predicate, deferral-fixtures, cadence-period
B only: invariant-coverage, cycle-spawns, instance-witness, structured-output, headless-workflow, compact-target, user-guards, stopfailure-packs, deferral-seam, owner-rulings, git-witness-readers, return-write-path, limit-hold
== severity (a defect takes its highest confirmed grade per round)
high defects 8: relaunch-replay, merge-back, chain-overlap, fixture-2-population, catalogue-duplicates, fencing, cycle-spawns, structured-output
  relaunch-replay: A 3 B 3
  merge-back: A 3 B 2
  chain-overlap: A 3 B 3
  fixture-2-population: A 3 B 3
  catalogue-duplicates: A 2 B 3
  fencing: A 3 B 3
  cycle-spawns: A 0 B 3
  structured-output: A 0 B 3
shared defects graded alike 28 of 32
== lenses behind the defects one round alone found
A: reuse 5, failure-envelope 4, grounding 2, coherence 2, blast-radius 2
B: failure-envelope 5, grounding 4, coherence 3, blast-radius 3, reuse 3
== refuted findings and their twins
A14 (journal-owner): confirmed twin A35
A45 (prose-ceilings): confirmed twin none
A46 (slug-shape): confirmed twin none
A59 (resume-tick-consumers): confirmed twin A38, B43
B14 (calls-per-act): confirmed twin A21, B23
B38 (hook-fragments): confirmed twin A36, A41, B33
B47 (next-readers): confirmed twin A39
B61 (resume-tick-consumers): confirmed twin A38, B43
```

## [gaps] What one round alone would have missed

- **One round finds about three quarters of what two find.**
  - Run A alone covers 46 of the 59 defects, and run B alone covers 45.
  - The two overlap at 0.54.
  - Chapman's capture-recapture estimate puts the population near 64.5, so about 6 defects remain that
    neither round found.
  - That estimate assumes every defect was equally findable by each round. Easy defects are found by
    both, which inflates the overlap, so read the 6 as a floor.
- **Two of the eight high defects were found by one round only.**
  - Both rounds found `relaunch-replay`, `chain-overlap`, `fixture-2-population` and `fencing` at high.
  - Run A alone would have missed `structured-output`. SubagentStop's `last_assistant_message` carries no
    return for a schema-forced agent, so the durability mechanism would have persisted empty returns on
    its main path.
  - Run A alone would also have missed `cycle-spawns`: act binding would have refused the roles cycle's
    own prompt-writer and scout spawns.
  - Run B found all eight, but graded `merge-back` medium. Run A graded `catalogue-duplicates` medium.
  - The 32 shared defects were graded alike 28 times.
- **The rounds read different evidence.** The lenses behind each round's unique defects are tallied
  above, and they fall into three patterns:
  - run A's reuse lens read the decision history: TOOL-aMendedFleet-61 and -116,
    TOOL-dUnstalledConvoy-7, branch-reconcile and runlog;
  - run B's coherence lens read the sibling layers: the roles cycle's spawns and the flow's loops;
  - run B's grounding lens measured the platform channel, counting 2,588 `StructuredOutput` endings.

  Both rounds had the same briefs and the same inputs. What differed was which files each finder chose
  to open.
- **One defect drew opposite readings: `hookspath`.**
  - Run A read today's absolute path as the decided position, and run B read it as the defect.
  - Neither cited WIRE-INTO-PROJECT's documented position: an out-of-tree copy under the git common dir.
    The fold adopts that.
- **A refutation speaks for one finding, not for its defect.** Eight findings were refuted:
  - two as duplicates (B14, B38);
  - four as unit-level detail, by design (A45, A59, B47, B61);
  - two on a false premise (A14, A46).

  Six of the eight have a confirmed twin. Three of the by-design refutations (A59, B47, B61) sit beside
  confirmed findings on the same defect (A38, A39, B43), so the by-design line was applied unevenly.
  With run B as the only round, `next-readers` would have been dropped.
- **What the second round cost and bought.**
  - Run A's twelve agents returned 212.2k output tokens, and run B's returned 218.0k.
  - Whichever round ran second would have added 28 to 31% more defects, and two highs were among them.
  - For the owed Layer 3 revisit of the roles layer's mechanical shape, this is a second data point
    beside aScoutedSeam's: there, one xhigh agent matched two medium scouts and a judge. Both say
    shape decides yield, so a review's shape should be declared per item.

## [map] Every finding, placed on its defect

| defect | what | A | B | folded in |
|---|---|---|---|---|
| `relaunch-replay` | a fresh relaunch cannot replay a Workflow run, so completed agents would be paid for twice | 1, 15 | 1, 16, 50 | `[spawn]` returns handed back; `[supervise]` relaunch |
| `driver-schema` | one `--json-schema` per launch cannot serve a driver that lives a whole build | 2 | 53 | `[act]`: one act session per act |
| `driver-cwd` | a launch fixes its working directory, so a build-lifetime driver cannot enter each unit's worktree | 20 | — | `[act]`; `[supervise]` launch in the act's workspace |
| `calls-per-act` | "hundreds of acts below 1,000 turns" was never measured, and compaction is token-triggered | 21 | 14, 23 | retired with the build-lifetime driver |
| `merge-back` | nothing carries a unit worktree's commits onto the build branch, and the siblings' shared-worktree queue is left standing | 3 | 2 | `[isolate]` integration before release |
| `chain-overlap` | dWellOiledMachine repeats units and gaps that v2 gives other builds, and drops `supersede` | 4, 32, 44 | 9, 31, 48 | `[build]` chain edits; RT-3 |
| `return-check-owner` | the subagent-stop return check and act binding each have two owners | 33 | 32 | `[spawn]`; `[enforce]`; `[build]` |
| `executor-map` | "the executor" is never mapped, and the actor kinds differ from the roles layer's | 5 | 10 | `[terms]` |
| `renewal-keys` | two keys and a prose rule answer how a driver is renewed | 6, 37 | 3 | `[policies]`: both retired, `runtime.relaunch` kept |
| `fixture-2-population` | the act-binding fixture replays `driver.log`, which holds no Workflow call or script | 7, 17, 52 | 4, 17, 40 | `[tests]` `binding` |
| `hidden-spawns` | act binding claims to refuse `agent()` and nested `workflow()` spawns that no hook sees | 8, 16 | 4, 20 | `[act]`: bound at the call, declarations reconciled |
| `inflight-count` | the in-flight count has no feed, no queue and no release when an agent dies | 8, 16, 54 | 12, 54 | `[supervise]` agents in flight |
| `unfailing-fixtures` | the SubagentStop fixture and the start-cost fixture cannot fail | 9 | 6 | `[tests]` `returns`, `start-cost` |
| `fail-closed-policy` | the fail-closed invariant is unconditional while allowed policy values fail open | 10, 60 | 11 | `[invariants]` `fail-closed` |
| `binding-events` | SessionStart and SubagentStart cannot block, and neither has a witness | 10, 23 | — | `[enforce]` witnesses; `[act]` session binding |
| `extension-enums` | extension points are selected by closed enumerations | 11 | 13 | `[extend]`; `[policies]` |
| `compaction-checks` | the owed CX-3 compaction checks have no disposition | 12 | — | `[sessions]` |
| `invariant-8-fixture` | the no-skipped-permissions invariant has no fixture | 13 | 7 | `[tests]` `no-skip` |
| `invariant-coverage` | three more invariants and the primary-tree rule have no fixture | — | 7 | `[invariants]`; `[tests]` `coverage` |
| `cli-binary` | which `claude` the supervisor launches is unresolved, and this node's PATH CLI is below the floor | 18 | 18 | `[supervise]` launch |
| `cli-floor-decision` | an authored CLI floor re-opens what TOOL-aMendedFleet-61's review rejected | 29 | — | `[enforce]`: no floor, after RT-2 |
| `supervisor-host` | nothing starts the supervisor or keeps it alive | 19 | 22 | `[supervise]` host |
| `codex-events` | Codex's hook events do not match "one for one" | 22 | 13, 21 | `[harness]` capability tables |
| `dispatcher-latency` | the dispatcher's 57 ms goal was never timed | 24 | 27 | `[enforce]`; `[tests]` `latency` |
| `fanout-carrier` | `runtime.fanout` is a second, raisable carrier of agent-cap's cap | 25, 40, 60 | 29, 41 | `[supervise]`; `[policies]`: retired |
| `reap-key` | `runtime.reap` re-declares `PROCMON_REAP_MODE` with other values | 26 | 30, 42 | `[supervise]`; `[policies]`: retired |
| `resume-tick-seed` | `resume-tick.sh` already is the supervisor's seed | 27 | 28 | `[supervise]` |
| `hookspath` | the hooks-path change: A reads the absolute path as the decided position, B as the defect | 28 | 26 | `[enforce]`: WIRE-INTO-PROJECT's trusted copy |
| `hookspath-readers` | the readers of `core.hooksPath` are not named | 42 | 45 | `[enforce]` |
| `permission-mode` | the launch allowlist ignores the owner's ruling for auto mode, TOOL-aMendedFleet-116 | 30 | — | `[supervise]` launch |
| `parallel-cleared` | parallel units are treated as unproven, and the condition that cleared them is dropped | 31 | — | `[current]`; `[supervise]` shared records |
| `core-sweep` | the core sweep rebuilds branch-reconcile, which is an expansion | 34 | — | `[isolate]` sweep |
| `journal-owner` | the journal and the run record are claimed without runlog | 14, 35 | — | `[contract]`; `[build]` |
| `hook-fragments` | the hook packs ignore the kits' fragments and settings-merge | 36, 41 | 33, 38 | `[enforce]` |
| `resume-tick-consumers` | retiring the resume launch names none of its consumers | 38, 59 | 43, 61 | `[build]` retired, with consumers |
| `next-readers` | `next` replaces `--plan` and `--status` without naming their readers | 39 | 47 | `[build]`: Runtime's client-surface unit, after RT-3 |
| `catalogue-duplicates` | the `runtime.*` keys duplicate v2's catalogue and carry no presets | 43 | 2, 37 | `[policies]` |
| `gap-keys` | the new gaps have no key prefix | 47 | — | `[gaps-proposed]` |
| `relaunch-cap` | relaunch has no attempt cap | 48 | 52 | `[supervise]` relaunch |
| `hold-bound` | the SubagentStop hold has no bound, and no rule for a malformed return | 55 | 52 | `[spawn]` |
| `command-idempotence` | a take-over can re-run a command whose effect landed without its witness | 49 | — | `[supervise]` |
| `fencing` | a take-over does not fence the dead supervisor's sessions | 50 | 51 | `[supervise]` fencing |
| `reap-predicate` | the sweep has no ownership predicate, and none for clean and merged | 51 | — | `[isolate]` sweep |
| `deferral-fixtures` | the limit and fail-closed fixtures never reach the deferral factory or a partial fan | 53 | — | `[tests]` `limits`, `fail-closed` |
| `cadence-period` | cadence items have no per-period witness | 56 | — | `[schedule]` |
| `next-answers` | `next` has no answer for an empty frontier or for bad inputs | 57 | 57 | `[decide]` |
| `bash-improvisation` | act binding misses shell scripts, and sessions bound to no build | 58 | 58 | `[act]` |
| `cycle-spawns` | act binding would refuse the roles cycle's own prompt-writer and scout spawns | — | 5 | `[act]` |
| `instance-witness` | "a witnessed item never runs again" contradicts the flow's loops | — | 8 | `[decide]`; `[invariants]` `once-per-instance` |
| `structured-output` | SubagentStop's `last_assistant_message` carries no schema-forced return | — | 15, 49 | `[spawn]` |
| `headless-workflow` | nothing has run a role-typed Workflow agent inside `claude -p` | — | 19 | `[tests]` `spike`; `[supervise]` foreground |
| `compact-target` | the compaction keep-list rests on an unverified import and an unrouted write | — | 24, 46 | `[sessions]` |
| `user-guards` | the fail-closed fixture expects user-level guards outside the dispatcher to be refused | — | 25, 55 | `[enforce]`; `[tests]` `fail-closed` |
| `stopfailure-packs` | StopFailure is missing, and ten live hooks have no owner pack | — | 34, 39 | `[enforce]` |
| `deferral-seam` | the deferral factory and write-less roles ignore the shapes and writers that exist | — | 35, 44 | `[spawn]` |
| `owner-rulings` | the guard escape and the fail-closed invariant re-decide K1 and K4 | — | 36 | `[enforce]` |
| `git-witness-readers` | the commit-side git-hook witnesses have no reader | — | 56 | `[enforce]` |
| `return-write-path` | SubagentStop's writes bypass `record`, with no bound | — | 59 | `[spawn]` |
| `limit-hold` | the limit hold leaves the reset time, the lease and long holds unstated | — | 60 | `[supervise]` limits |
| `prose-ceilings` | the unattended kit's prose carriers sit at their size ceilings | 45 | — | refuted as unit-level; kept as a scoping fact in `[build]` |
| `slug-shape` | the build's slug has three words | 46 | — | refuted: the slug fits HYGIENE's adjective-noun rule |

## [neither] What neither round raised, found while folding

These are the main loop's own additions. No skeptic has tried to refute them.

- **An act has no wall-clock ceiling.** The record bounds an act only by `--max-turns`, so a hung act
  holds its build until someone notices. The fold adds `runtime.act-ceiling`, enforced through
  process-monitor's declared ceilings (the charter's `[cost]`).
- **A fresh worktree can start dirty.** On a node whose `autocrlf` differs from what the files were
  committed with, every unpinned path smudges, and a dirty tree blocks `--preflight`. Per-unit
  workspaces multiply fresh worktrees. The fold has the allocator set each workspace's line endings
  from the node registry.
- **Kit conf keys beside the policy file.** Runtime reads `FANOUT_CAP`, `PROCMON_REAP_MODE`,
  `RESUME_ATTEMPTS` and `RESUME_TURNS` from kit confs. v2 says every key lives in
  `.governance/policy.toml`, but never says whether the kit confs fold into it. That question belongs
  to v2's `[owed]`.
- **A second spawn backend.** Most of the reviewed spawn defects come from hosting a Workflow inside a
  headless session: `hidden-spawns`, `structured-output`, `relaunch-replay`, `headless-workflow` and
  `cycle-spawns`. A backend that launches one lean `claude -p` per agent has none of them, and pays a
  session start per agent instead. The fold registers it as a second backend, and the spike measures
  both before the build picks one.

## [instrument] The comparison script

Run from the session scratchpad. It is kept here as fenced text, since the lexicon gate grades every tracked Python file.

```python
"""Compare two Tier-2 rounds on one subject, defect by defect.

Inputs, all tracked: the two review reports (their appendix tables), the comparison record
(its [map] table, one row per defect naming each round's finding ids), and the session log
(the agent ledger's returned lines for the two runs).

Refuses, exit 1: a finding id the map does not place, a map id the report lacks, a run with no
returned lines. Prints every number the comparison record states.

Usage: python compare_rounds.py <report-a> <report-b> <compare-record> <session-log> <run-a> <run-b>
"""
import re
import sys

SEV = {"low": 1, "medium": 2, "high": 3, "blocker": 4}


def appendix(path):
    text = open(path, encoding="utf-8", newline="").read()
    tail = text.split("## Appendix", 1)[1]
    rows = {}
    for line in tail.splitlines():
        if not re.match(r"^\| \d+ \|", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        fid, lens, _ref, sev, skep, verdict = cells[:6]
        if verdict not in ("confirmed", "refuted", "unverified", "uncertain"):
            sys.exit(f"{path}: id {fid}: unparseable verdict {verdict!r}")
        rows[int(fid)] = {"lens": lens, "sev": (skep or sev), "verdict": verdict}
    if not rows:
        sys.exit(f"{path}: no appendix rows")
    return rows


def ids(cell):
    cell = cell.strip()
    return [] if cell in ("—", "-", "") else [int(x) for x in re.split(r"[,\s]+", cell) if x]


def defect_map(path):
    text = open(path, encoding="utf-8", newline="").read()
    block = text.split("## [map]", 1)[1].split("\n## ", 1)[0]
    out = []
    for line in block.splitlines():
        if not line.startswith("| `"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        out.append({"tag": cells[0].strip("`"), "A": ids(cells[2]), "B": ids(cells[3]), "disp": cells[4]})
    if not out:
        sys.exit(f"{path}: no [map] rows")
    return out


def returned_out(path, run):
    text = open(path, encoding="utf-8", newline="").read()
    outs = [float(m.group(1)) * (1000 if m.group(2) else 1) for m in re.finditer(
        r"^- returned — .*? · ([0-9.]+)(k?) out · run " + re.escape(run) + r"/", text, re.M)]
    if not outs:
        sys.exit(f"{path}: no returned lines for run {run}")
    return len(outs), sum(outs) / 1000


def main():
    rep = {"A": appendix(sys.argv[1]), "B": appendix(sys.argv[2])}
    dmap = defect_map(sys.argv[3])
    runs = {"A": returned_out(sys.argv[4], sys.argv[5]), "B": returned_out(sys.argv[4], sys.argv[6])}

    placed = {"A": set(), "B": set()}
    for d in dmap:
        for r in "AB":
            for i in d[r]:
                if i not in rep[r]:
                    sys.exit(f"map row {d['tag']}: {r}{i} is not in report {r}")
                placed[r].add(i)
    for r in "AB":
        missing = sorted(set(rep[r]) - placed[r])
        if missing:
            sys.exit(f"report {r}: ids the map does not place: {missing}")

    def state(d, r):
        vs = [rep[r][i]["verdict"] for i in d[r]]
        if "confirmed" in vs:
            return "confirmed"
        return "raised-refuted" if vs else "absent"

    def sev(d, r):
        s = [SEV[rep[r][i]["sev"]] for i in d[r] if rep[r][i]["verdict"] == "confirmed"]
        return max(s) if s else 0

    real = [d for d in dmap if "confirmed" in (state(d, "A"), state(d, "B"))]
    both = [d for d in real if state(d, "A") == state(d, "B") == "confirmed"]
    only = {r: [d for d in real if state(d, r) == "confirmed" and state(d, "AB"[r == "A"]) != "confirmed"] for r in "AB"}
    n = {r: len(both) + len(only[r]) for r in "AB"}

    print("== runs")
    for r in "AB":
        conf = sum(1 for v in rep[r].values() if v["verdict"] == "confirmed")
        highs = sum(1 for v in rep[r].values() if v["verdict"] == "confirmed" and SEV[v["sev"]] >= 3)
        agents, out = runs[r]
        print(f"{r}: raw {len(rep[r])}, confirmed {conf}, refuted {len(rep[r]) - conf}, "
              f"precision {conf / len(rep[r]):.2f}, high findings {highs}, "
              f"agents {agents}, out {out:.1f}k (sum of returned lines)")
    print("== defects")
    print(f"map rows {len(dmap)}, confirmed defects {len(real)}, refuted-only {len(dmap) - len(real)}")
    print(f"both {len(both)}, A only {len(only['A'])}, B only {len(only['B'])}")
    for r in "AB":
        print(f"{r} alone covers {n[r]} of {len(real)} ({n[r] / len(real):.0%})")
    print(f"overlap (Jaccard) {len(both) / len(real):.2f}")
    chap = (n["A"] + 1) * (n["B"] + 1) / (len(both) + 1) - 1
    print(f"Chapman estimate of the population: {chap:.1f}, so about {chap - len(real):.0f} found by neither")
    for r in "AB":
        print(f"{r} only: {', '.join(d['tag'] for d in only[r])}")
    print("== severity (a defect takes its highest confirmed grade per round)")
    hi = [d for d in real if max(sev(d, 'A'), sev(d, 'B')) >= 3]
    print(f"high defects {len(hi)}: {', '.join(d['tag'] for d in hi)}")
    for d in hi:
        print(f"  {d['tag']}: A {sev(d, 'A')} B {sev(d, 'B')}")
    agree = sum(1 for d in both if sev(d, "A") == sev(d, "B"))
    print(f"shared defects graded alike {agree} of {len(both)}")
    print("== lenses behind the defects one round alone found")
    for r in "AB":
        tally = {}
        for d in only[r]:
            for lens in sorted({rep[r][i]["lens"] for i in d[r] if rep[r][i]["verdict"] == "confirmed"}):
                tally[lens] = tally.get(lens, 0) + 1
        print(f"{r}: " + ", ".join(f"{k} {v}" for k, v in sorted(tally.items(), key=lambda kv: -kv[1])))
    print("== refuted findings and their twins")
    for r in "AB":
        for i, v in sorted(rep[r].items()):
            if v["verdict"] == "confirmed":
                continue
            d = next(d for d in dmap if i in d[r])
            twin = [f"{q}{j}" for q in "AB" for j in d[q] if rep[q][j]["verdict"] == "confirmed"]
            print(f"{r}{i} ({d['tag']}): confirmed twin {', '.join(twin) if twin else 'none'}")


if __name__ == "__main__":
    main()
```

Seen green, then red on three planted inputs before it was trusted:

```text
the record as written            rc 0, the output in [numbers]
relaunch-replay's A cell cut to 1  report A: ids the map does not place: [15]   rc 1
driver-schema's A cell given 99   map row driver-schema: A99 is not in report A   rc 1
run B named wf_nosuchrun          ...: no returned lines for run wf_nosuchrun   rc 1
```
