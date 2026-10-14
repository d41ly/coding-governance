# Research — the Maintain stage, and how the loop corrects itself: detectors without owners, a surface that only grows

**Serves:** research PLAY-dClosedLoop-1

Researched by the main loop in session `1799cb98`, 2026-10-14, in the shape the five stage
researchers were handed (their handoffs are under `prompts/`), because the direct-spawn budget is
five per owner turn. Every number below comes from a probe whose instrument is recorded in the last
section, beside its output.

## 1. Inventory

- **drift-audit** (`tools/drift-audit/drift_report.py`, Skill `/drift-audit`, harnesses
  `tools/workflows/drift-audit-code.js` and `drift-audit-state.js`): 27 signals over records versus
  the tree, each with a liveness assertion; Tier 0 runs in seconds with no agent. A detector.
- **process-monitor** (`tools/process-monitor/`, SessionStart and PostToolUse hooks, `reap.py`):
  names processes past their declared ceiling; reaping waits for someone to run `reap.py --sweep`.
- **branch-reconcile** (`tools/branch-reconcile/`, Skill `/cleanup`): verdicts for every worktree,
  branch and stash, and removal of only the landed ones, when an owner asks.
- **runlog** (`tools/runlog/`, Skill `/runlog`): answers what an unattended run did, read-only.
- **memory-recall** (`tools/memory-recall/`): the decision-corpus index and the `recall floor` leg.
- **codebase-map** (`tools/codebase-map/`, `memory/map/`): coverage and freshness legs, a shrink-only
  `baseline.toml`.
- **the bug-class catalogue** (`memory/gotchas/`, `tools/memory-tree/gotchas.py`): the sink of the
  charter's `[left-shift]` rule where no gate fits; 122 classes.
- **the backlog fold and views** (`tools/memory-tree/backlog.py`, `memory/backlog/`), and
  `memory/LIVE.md`'s dormancy and landed-unclosed labels.
- **shrink-only registries** (`memory/project/*.txt`, 20 files, 815 live rows) and their pins.
- **version hygiene**: kit version markers, the verdict epoch, the kit epoch, `govkit epoch`.
- **session-start wiring** (`tools/check-wiring.sh --session`) and the orientation card's `drift —`
  and `health —` cells (`skills/session-kickoff/manifest-check.sh --card --write`).
- **unattended health**: `tools/unattended/stall-recorder.js`, the keepalive and resume crons a run
  registers through `CronCreate` (`tools/unattended/README.md`, "The resume tick").
- **recipe mode** (`memory/map/features/playbook-mode.md`, status `building`): an unattended
  authorization mode for repeatable content, run from a PLAYBOOK document, graded by the `playbook
  validity gate` leg. The one existing seam for recurring, owner-free work.

## 2. Flow

- **Detection is session-triggered.** Every SessionStart prints the drift cell, the process census
  and the wiring check. Nothing else runs on a cadence: no scheduled task, routine or cron exists for
  maintenance; the only `CronCreate` use is an unattended run's own keepalive and resume tick.
- **Action is ask-triggered.** Reaping, cleanup, triage, closing dormant builds, retiring run
  records and refreshing dossiers each happen only when a session or the owner chooses to.
- **ENFORCED:** freshness of generated outputs (the bar refuses stale ones), shrink-only pins that
  have a pin, coverage of the map, the recall floor, kit version markers.
- **STATED or report-only:** most drift signals ("report only, no pin"); dormancy; the
  `[left-shift]` obligation itself; retiring anything.
- **Hand-offs:** in, from Test and Deploy, inherited reds and asks; out, to Plan, asks filed into
  build backlogs, which Plan has no owner to triage (see the Plan record).

## 3. The implicit contract today

- **Entry:** none. Maintenance starts when someone notices.
- **Exit:** none. No signal has to reach zero, and nothing records that a maintenance pass ran.
- **Artifacts:** the drift history (`<git-dir>/drift-history.tsv`, per node, untracked), asks, gotcha
  records, ceiling evidence.
- **Who:** whichever session trips over it; the owner by asking.
- **Review at this stage, and of the loop itself:** the loop adjusts itself only by ADDING. A
  confirmed finding becomes a gate or a gotcha (`[left-shift]`), so every review grows the governing
  surface. No mechanism measures what a gate, rule or gotcha is worth, and none retires one.

## 4. Gaps

**HIGH**
- **No cadence.** Absent: any scheduled maintenance job (grep for `CronCreate`, `schtasks`,
  `crontab`, `RemoteTrigger` under `tools/` finds only an unattended run's own keepalive).
- **Detectors without owners.** 15 of 27 drift signals are nonzero; most are "report only, no pin";
  2 are DEAD PROBES, one of them dead for 20 readings (`discarded_work_landed`), the other
  `remote_ci_red_streak`, which cannot move.
- **The default branch can be red with no one told.** The full memory-hygiene run on
  `origin/main` at `ebce889c` reds check 23 on acceptance-ledger lines of `aSparedSpawn` and
  `aOrientedCast` (instrument 4). Remote CI "blocks nothing", and the signal meant to watch its reds
  is the dead probe above.
- **The governing surface only grows.** Between 2026-08-01 and 2026-10-14: gate legs 17 → 140,
  bug classes 0 → 122, guides 0 → 301 KB, tracked files under `tools/` 42 → 377, shrink-only
  registries 2 → 20 (815 rows). Nothing retires a leg, a rule or a class, and nothing prices one
  against what it has caught.
- **Records dominate the work.** Of 2,827 non-merge commits on `origin/main` in the last 30 days,
  1,598 touched only `memory/` and 1,168 touched product paths. `records` is the commonest subject
  prefix (1,131).

**MED**
- **Dormant work never closes.** 21 of 25 live builds have no activity in 21 days; 89 run-state
  files are still live `RUN.md`, and 10 non-terminal run records belong to merged work (pin 2).
- **The map goes stale.** 28 of 31 dossiers are older than the paths they claim (pin 26).
- **Ratchets that should shrink do not.** 3 of 5 shrink-only lists are not shrinking.
- **Timeouts are retried and forgotten.** 3 legs were retried after a timeout (pin 0).
- **Reaping is manual.** The session-start census printed two idle processes 5.6 h past their
  ceiling, and only a hint to run `reap.py --sweep`.

**LOW**
- `lexicon_marginal_offense_rate` 584 of 4,948, report only.
- `dangling_pointers_in_own_ledger` 8 of 63, report only.

## 5. Candidates

**A. A maintenance recipe on a cadence.**
- *Mechanism:* a PLAYBOOK for a recurring maintenance run in `recipe` mode: the drift report, the
  reap dry-run, the cleanup dry-run, triage drafts for unlabelled asks, dormancy proposals; each
  finding filed as an ask into a standing maintenance build; registered on a schedule.
- *Seam:* recipe mode (`tools/unattended/check-playbook.sh`, `PLAYBOOK-TEMPLATE.template.md`), the
  unattended kit's `CronCreate` registration, `drift_report.py`, `reap.py --dry-run`,
  `branch_reconcile.py`.
- *Losing test:* the run needs a host that is up on the cadence and a mandate that permits it; a
  maintenance action that mutates must be safe with no owner turn.
- *Result:* partly open. The kit's crons are session-scoped, so a cadence needs a session that is
  alive or a cloud routine; the recipe mode is still `building`. The read-only half (reports and
  drafted asks) is safe; the mutating half (closing builds, reaping) stays owner-confirmed.

**B. Detectors that bind.**
- *Mechanism:* every drift signal carries a pin and a named owning stage; a signal over its pin, or
  dead, reds a leg instead of printing "report only".
- *Seam:* `drift_report.py`'s existing pins, the `drift-audit records` leg.
- *Losing test:* the predicate must move on the real tree without reding unboundedly.
- *Result:* survives. Today it would red on 4 signals over pin (`shrink_only_lists_not_shrinking`,
  `run_records_nonterminal_but_merged`, `legs_retried_after_timeout`,
  `dossiers_older_than_their_paths`) plus 2 dead probes, which is 6 bounded items.

**C. A value and retirement ledger for the governing surface.**
- *Mechanism:* each leg, rule and bug class records when it last caught a real defect (an OWN red,
  a cited finding) and what it costs (ceiling evidence); a periodic loop review retires, merges or
  demotes the ones that never catch anything.
- *Seam:* `GATE_ATTRIBUTE`, `<git-dir>/gate-ledger.tsv`, `tools/run-gates/ceiling-evidence.txt`,
  bug-class front matter.
- *Losing test:* the catch history must exist somewhere every node can read.
- *Result:* loses as built today. The gate ledger is per node and untracked, and ceiling evidence
  comes from node `a` alone (the Test record); a catch history has to be published first.

## 6. Pick

B now, A next, and C after the Test stage publishes its verdicts. B turns 6 silent signals into
owned reds with no new machinery; A gives Maintain the cadence it has never had, on the one seam
built for owner-free repeatable work; C is the only candidate that lets the loop shrink itself, and
it is blocked only on a shared verdict record that the Test stage's own pick (a remote verifier)
would produce.

## Instruments and their output

Instrument 1: `python tools/drift-audit/drift_report.py` at `035ff4b9` (base `origin/main` at
`ebce889c`), kit 1.29. Output, the signal table:

```text
  lexicon_marginal_offense_rate                        584   4948  report only, no pin
  ledger_rows_contradicting_git                          0      0  empty by declaration — nothing to measure here yet
  non_terminal_specs_cited_by_product_source             2     30  ok (baseline 2)
  shrink_only_lists_not_shrinking                        3      5  over pin 0 (report only)
  handkept_inventories_disagreeing_with_source           0     27  ok (pin 0)
  dangling_pointers_in_own_ledger                        8     63  report only, no pin
  closed_specs_with_no_product_commit                    1   1208  ok (baseline 1)
  lexicon_verbs_declared_but_unused                      0     23  ok (pin 0)
  lexicon_ratified_older_than_language_surface           0      1  ok (pin 0)
  live_backlog_rows_per_shard                          521    126  report only, no pin
  asks_disposed_overrides                                0     89  ok
  readme_mechanism_drift                                 4     20  ok (pin 4, drain it)
  backlog_asks_contested                                 0    859  ok
  backlog_evidence_sha                                   0     72  ok
  backlog_asks_unlabelled                              435    521  ok (pin 447, drain it)
  open_asks_cited_by_product_source                     54    521  report only, no pin
  cutoff_keys_armed                                     34     34  ok (pin 34, drain it)
  source_cited_ids_resolving_to_no_record                2   1249  ok (pin 2, drain it)
  backlog_stragglers                                     0     47  ok
  run_records_nonterminal_but_merged                    10     98  over pin 2 (report only)
  aborted_work_landed                                    0     13  ok
  discarded_work_landed                                  0     13  DEAD PROBE for 20 readings — take it out of SIGNALS, or file an ask and declare it in DEAD_FILED
  legs_retried_after_timeout                             3     39  over pin 0 (report only)
  fleet_over_budget                                      0      4  ok
  remote_ci_red_streak                                   0      0  DEAD PROBE — signal cannot move, ignore its value
  dossiers_older_than_their_paths                       28     31  over pin 26 (report only)
  live_builds_without_activity                          21     25  report only, no pin
```

Instrument 2: a read-only growth probe, run with the worktree root as its argument. Its source:

```python
"""Read-only growth probe for dClosedLoop's Maintain research: how fast gov's governing surface grows,
and whether anything drains it. Reads git history and the tree; writes nothing."""
import json, os, re, subprocess, sys
ROOT = sys.argv[1]
def git(*args):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True,
                          encoding="utf-8", errors="replace").stdout
def rev_at(date):
    return git("rev-list", "-1", f"--before={date}T23:59:59", "origin/main").strip()
def show(rev, path):
    return git("show", f"{rev}:{path}")
def count_legs(rev):
    txt = show(rev, "tools/gate-legs.json")
    if not txt:
        return None
    try:
        return len(json.loads(txt))
    except Exception:
        return len(re.findall(r'"name"\s*:', txt))
def count_tree(rev, prefix, suffix=""):
    out = git("ls-tree", "-r", "--name-only", rev, "--", prefix)
    return sum(1 for line in out.splitlines() if line.endswith(suffix))
def bytes_of(rev, paths):
    total = 0
    for p in paths:
        for line in git("ls-tree", "-r", "-l", rev, "--", p).splitlines():
            parts = line.split()
            if len(parts) >= 4 and parts[3].isdigit():
                total += int(parts[3])
    return total
def charter_rules(rev):
    return len(re.findall(r"^- \[[a-z-]+\]", show(rev, "coding-governance-agents.template.md"), flags=re.M))
for d in ["2026-07-15", "2026-08-01", "2026-08-15", "2026-09-01", "2026-09-15", "2026-10-01", "2026-10-14"]:
    r = rev_at(d)
    builds = len({p.split("/")[2] for p in git("ls-tree", "-r", "--name-only", r, "--", "memory/builds").splitlines()
                  if p.count("/") >= 3})
    print(d, r[:8], count_legs(r), builds, count_tree(r, "memory/gotchas", ".md"),
          bytes_of(r, ["memory/guides"]) // 1024, count_tree(r, "tools"),
          count_tree(r, "memory/project", ".txt"), charter_rules(r))
```

Its output (columns: date, rev, legs, builds, bug classes, guides KB, files under `tools/`,
registries, one-line charter rules; the rule count is 0 before the template's v4.0 tag syntax):

```text
2026-07-15  78b23be6     -       0        0         0          30           2             0
2026-08-01  9368d1e8    17       0        0         0          42           2             0
2026-08-15  c32161be    54      35       15        61         126           6             0
2026-09-01  05f6236c    87      86       38       138         216           9             0
2026-09-15  06257a22   107     117       71       151         271          13             0
2026-10-01  c1d75484   123     139       92       217         318          15             0
2026-10-14  ebce889c   140     172      122       301         377          20            45
```

Instrument 3: the commit mix over the last 30 days on `origin/main`, non-merge commits:

```bash
git log --since="30 days ago" --no-merges --name-only --format='@@%h' origin/main | awk '
/^@@/ { if (n) tally(); n=0; mem=1; prod=0; next }
NF { n++; if ($0 !~ /^memory\//) mem=0; if ($0 ~ /^(tools\/|skills\/|coding-governance-agents\.template\.md|WIRE-INTO-PROJECT\.md)/) prod=1 }
function tally() { if (mem) m++; else if (prod) p++; else o++ }
END { if (n) tally(); printf "memory-only %d · product %d · other %d\n", m, p, o }'
```

Output: `memory-only 1598 · product 1168 · other 61`. The subject-prefix count from the same range
put `records` first at 1,131, then `build` 322, `spec` 293, `fix` 215 and `tool` 168.

Instrument 4: the full memory-hygiene run on the default branch, in a detached worktree at
`ebce889c7d7104fe4811707d6f17b2a486bf0fd6` created for the probe and removed after it:

```bash
git worktree add --detach /c/Users/d41ly/AppData/Local/Temp/gm1 ebce889c7d7104fe4811707d6f17b2a486bf0fd6
cd /c/Users/d41ly/AppData/Local/Temp/gm1 && bash tools/memory-tree/check-memory-hygiene.sh | grep -E '^HYGIENE check [0-9]+ FAILED'
```

Output, exit 1: two `HYGIENE check 23 FAILED` lines, one for acceptance-ledger lines in neither
legal form and one for answers sharing no backticked token with their criterion, naming
`TOOL-aSparedSpawn-*` and `TOOL-aOrientedCast-22` rows. `LEDGER_LABEL_CUTOFF` and
`LEDGER_TOKEN_CUTOFF` are both 2026-09-08 in `.memory-tree.conf`.

Instrument 5: the wired hooks, read from `.claude/settings.json`: PreToolUse `agent-cap.js`,
`scratch-guard.js`, `gate-guard.js`; SessionStart the card writer and replayer, `check-wiring.sh
--session`, `procmon-hook.js`; PostToolUse `recall-opened.js`, `procmon-hook.js`; Stop
`stop-guard.js`, `format-guard.js`; StopFailure `stall-recorder.js`; SubagentStart `scratch-guard.js`.
None runs on a schedule.
