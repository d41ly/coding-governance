# TOOL-aReapedSpinner-2 — the scope fence: attribution is positive, path-shaped, and never the caller

**Status:** OPEN · rev-2 · 2026-09-08 · node a · Tier-2 · base e2b82a53 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-08-build-TOOL-aReapedSpinner-2-live-predicate-run.md](../build/2026-09-08-build-TOOL-aReapedSpinner-2-live-predicate-run.md) | research | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-3 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md) | spec-audit | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7 |

<!-- /gen:spec-records -->

## 1. Goal

Decide which census rows this repo's agent work OWNS, so that nothing downstream can name — let
alone kill — a process belonging to somebody else, INCLUDING another agent session on the same
machine. This is the safety property the whole kit rests on.

## 2. Scope (IN)

- **S1** — `tools/process-monitor/scope.py`, exposing `check_in_scope(row, conf, self_chain)`
  returning a verdict plus the REASON it was admitted. Observed by AC1.
- **S2** — POSITIVE attribution only: a row is in scope when a declared `PROCMON_ROOTS` prefix
  matches its resolved PROGRAM PATH or one of its PATH-SHAPED ARGUMENTS. Nothing is in scope by
  default; there is no exclusion list. Observed by AC1, AC2, AC8.
- **S3** — the SELF fence: the calling process, every ancestor of it, and the census backend's own
  children are excluded whatever else matches. Observed by AC3.
- **S4** — a blank or absent `PROCMON_ROOTS` REFUSES rather than matching nothing, and so does a
  root shorter than a declared minimum or equal to a filesystem root. Observed by AC4, AC6.
- **S5** — prefix matching is anchored and separator-aware, so a declared root `…/repo` does not
  admit `…/repo-other`. Observed by AC5.
- **S6** — `scope.py --explain <pid>` prints why ONE row was admitted or refused. Observed by AC7.
- **S7** — `scope.py --check-path <path>` grades a PATH rather than a pid, so a caller can ask
  "would rows under this directory be admitted" BEFORE any process exists. Observed by AC9.
- **S8** — a row whose `command` is `None` is REFUSED and COUNTED, and the count is printed.
  Observed by AC10.

## 3. Non-goals (OUT)

- **No classification and no killing.** This unit answers "is this ours", nothing else.
- **No inference from the process name.** A row is not in scope because it is called `bash` or
  `python`; only a declared root admits it.
- **No RAW-STRING containment.** Matching the whole command line as one string is what rev-1 did,
  and it is the defect D11 records: every Claude Bash-tool shell carries an `export TEMP=`
  assignment naming the user's temp directory, so a root naming that directory admits every agent
  session in every repository on the machine.
- **No user or session filtering.** The observed failures include processes whose launching session
  was long dead, so a same-session predicate would miss the population that matters.
- **No cwd probing.** A dead-parent orphan's cwd is unreliable and there is no cheap Windows
  equivalent.
- **No descendant inheritance HERE.** A walked descendant inheriting its ancestor's scope is unit
  4's rule, because inheritance is only meaningful inside a walked set. This unit grades one row
  standalone and says so, so unit 4 cannot mistake a standalone refusal for a tree-wide one.

### Edges

- **consumes-from** `TOOL-aReapedSpinner-1` — `command` and `pid`. S2 depends on `command` being
  CIM's `CommandLine`, not `ps -W`'s executable column.
- **consumes-from** `TOOL-aReapedSpinner-6` — `PROCMON_ROOTS`.
- **hands-off** `TOOL-aReapedSpinner-3` — the classifier grades ONLY rows this unit admitted.
- **hands-off** `TOOL-aReapedSpinner-4` — the reaper kills ONLY rows this unit admitted, re-checks
  rather than trusting a handed list, and owns the descendant-inheritance rule §3 excludes here.
- **hands-off** `TOOL-aReapedSpinner-7` — S7's path mode is what lets the gate runner grade its own
  scratch directory at profile time, which is the only way its fallback can be announced before a
  kill rather than during one.

## 4. Design

### What is matched, and what is NOT

**The row is decomposed before matching, never matched as one string.** From `command`:

1. the resolved PROGRAM PATH — argv[0], normalized;
2. every PATH-SHAPED ARGUMENT — a token containing a separator, after stripping surrounding quotes.

A declared root must prefix-match one of those. It is NOT matched against the raw command line.

**Why, measured (D11).** Every Claude Bash-tool shell on this machine carries an `export TEMP=`
assignment naming the user's temp directory inside its argv, and `mktemp -d` resolves under that
same root. Unit 7 needs the runner's scratch directories admissible. Under raw-string containment,
declaring the temp root therefore admits every agent session on the box — in every repository —
because the substring appears in an ENVIRONMENT ASSIGNMENT, not in a program path. S3's self fence
excludes only the caller's own ancestry, so a sibling session's shell stays in scope and killable,
and one such shell in the live table already carries `ppid 1`, which grades ORPHAN under the
resolved default `reap-orphans` mode. The safety property of the kit, inverted, by following unit
7's own requirement.

An environment assignment is `NAME=value` before the first program token. Its value is not a
path-shaped argument for this purpose even when it looks like one.

### The containment test, both ways

The selected class `containment-tested-one-way` is the failure mode: *a guard asking only "is this
path under the protected one" refuses the narrow declarations and admits the one that claims
everything.* Both directions are handled:

1. A root of `/`, of a single character, or shorter than a declared minimum REFUSES (S4).
2. Matching is on a normalized, separator-terminated prefix, so `/c/projects/gov` admits
   `/c/projects/gov/x` and refuses `/c/projects/gov-scratch`.

Paths are normalized to forward slashes and case-folded first: the same tree is spelled
`C:/projects/…`, `C:\projects\…` and `/c/projects/…` by three different producers in one command
string on this node.

### The self fence

`check_in_scope` takes `self_chain` — the pids from the calling process up to the root of its own
ancestry, walked over the census's `ppid` edges. Not `os.getppid()` alone: the reaper must exclude
the whole chain. The measurement that makes it non-negotiable is that a test tree's descendants
shared the Bash-tool shell's pgid, and that shell is an ancestor of anything a session runs.

### Files touched (estimate)

`tools/process-monitor/scope.py` new; arms added to `tools/process-monitor/selftest.py`.

## 5. Production-readiness checklist

- security — this IS the security unit, and D11 is the proof that its predicate shape is the whole
  guarantee rather than a detail of it.
- perf / scale — tokenization plus a prefix test per row over a few hundred rows.
- error / empty / loading states — blank or over-broad roots REFUSE (S4); zero admitted rows is a
  legitimate answer reported as "0 of N in scope", never as a bare "nothing to report"; an
  unattributable row is refused and counted (S8).
- observability — `--explain` (S6), `--check-path` (S7), the admission reason on every verdict, and
  the unattributable count.
- risks — an over-broad declared root, and specifically the temp root. Mitigated by the minimum
  length check, by program-path matching, and by unit 6 §4 stating the rule in the conf itself.
- testing — a table-driven arm over adversarial roots AND a fixture captured from this machine's
  real `ps -ef`, env assignments and all. A synthetic fixture would not have caught D11.
- migration — none.
- user docs — the kit README's scope section, unit 6.

## 6. Acceptance criteria

- **AC1** — When a row whose PROGRAM PATH is under a declared root is graded, it is admitted and
  its verdict names the root that admitted it. Observed by `selftest.py`, arm
  `test_declared_root_admits_and_names_it`.
  Red when: a row is admitted with no reason, which makes an over-broad root undiagnosable.
- **AC2** — When a row matches NO declared root in either its program path or its path-shaped
  arguments, it is refused. Observed by `selftest.py`, arm `test_undeclared_row_is_refused`.
  Red when: the predicate falls through to admit-by-default on any input shape.
- **AC3** — When the calling process and each of its ancestors are graded — every one of which sits
  under a declared root and would otherwise be admitted — all are refused. Observed by
  `selftest.py`, arm `test_self_chain_is_never_in_scope`.
  Red when: only the immediate parent is excluded, leaving the session's own shell killable.
- **AC4** — When `PROCMON_ROOTS` is blank, `check_in_scope` raises and `scope.py` exits non-zero
  naming the key. Observed by `selftest.py`, arm `test_blank_roots_refuses`.
  Red when: a blank list matches nothing and the kit reports a clean tree it never examined.
- **AC5** — When the declared root is `/c/projects/gov`, a row naming `/c/projects/gov-scratch/x` is
  REFUSED and one naming `/c/projects/gov/x` is admitted. Observed by `selftest.py`, arm
  `test_prefix_is_separator_anchored`.
  Red when: the match is a bare containment test, which admits the sibling.
- **AC6** — When a root of `/`, a one-character root, or a root below the declared minimum length
  is declared, the conf read REFUSES. Observed by `selftest.py`, arm
  `test_root_that_claims_everything_refuses`.
  Red when: the minimum-length check is advisory and the run continues.
- **AC7** — When `scope.py --explain <pid>` is given a live pid, it prints one line saying admitted
  or refused and why. Observed by `selftest.py`, arm `test_explain_answers_one_pid`.
  Red when: `--explain` prints the whole table, which is the census's job and hides the answer.
- **AC8** — When a row's ONLY occurrence of a declared root is inside an environment assignment —
  the real Bash-tool shape, taken from a captured `ps -ef` snapshot of this machine — the row is
  REFUSED. Observed by `selftest.py`, arm
  `test_root_inside_an_env_assignment_does_not_admit`.
  Red when: matching is against the raw command string, which admits every agent session on the
  machine once the temp root is declared (D11). This is the criterion that makes the resolved
  `reap-orphans` default defensible; unit 6 §8 F1 is conditional on it.
  `fixture:` a REAL snapshot from this node. A synthetic command line would not carry the
  `export TEMP=` shape that produced the defect.
- **AC9** — When `scope.py --check-path <path>` is given a directory under a declared root it
  answers admitted, and given one outside every declared root it answers refused, in both cases
  without any process existing at that path. Observed by `selftest.py`, arm
  `test_check_path_grades_a_path_with_no_process`.
  Red when: the path mode requires a live pid, which would make unit 7's profile-time probe
  impossible and force its refusal to surface mid-kill (D6).
- **AC10** — When a row carries `command = None`, it is refused and the printed summary names the
  unattributable count as non-zero. Observed by `selftest.py`, arm
  `test_unattributable_row_is_refused_and_counted`.
  Red when: such rows are silently dropped. Measured: 115 of 314 CIM rows on this node carry no
  command line, so this is a third of the table, not an edge case.

## 7. Gates

`line length` · `lexicon naming predicates` · `govkit selfcheck` · `dead-path carriers (deleted files still named)`

New arm: `tools/process-monitor/selftest.py` · stages blank roots, a one-character root, a
sibling-prefix root, mixed separators, the caller's own ancestry, a REAL captured `ps -ef` snapshot
carrying `export TEMP=` assignments, a path with no process, and a `None` command · floor moves
with unit 1's arms, one suite.

## 8. Open questions

- **F1 — should a row with no `command` string be admitted or refused?**
  RESOLVED (agent, 2026-09-08, delegated): REFUSED, and counted. A row the backend could not
  describe cannot be attributed, and admitting it would put an unidentifiable process in front of
  the reaper. The count is reported because a silent drop of a third of the table is the
  green-by-absence class. Vetoes clean.
- **F2 — should an environment assignment ever admit a row?**
  RESOLVED (agent, 2026-09-08, delegated): NEVER. An assignment describes where a process's
  temporary files may go, not what it is or which tree it belongs to. Admitting on one is what
  turns a declared root into a licence over every session on the machine (D11). The cost is
  accepted and stated: a process whose ONLY connection to the tree is an env var is invisible to
  this kit. Vetoes clean — nothing widens, and the alternative widens a kill surface.

## 9. Revision log

- rev-1 · 2026-09-08 · initial draft.
- rev-2 · 2026-09-08 · §1 · S2 · S6 · S7 · S8 · §3 · §4 · AC6 · AC7 · AC8 · AC9 · AC10 · §7 ·
  §8 F2 · folded spec-audit round 1. D11: matching moves from the raw command string to the program
  path and path-shaped arguments, with AC8 staged from a real snapshot, and §3 gains the
  raw-string non-goal. D3: the scope-to-acceptance join was off by one from S6 — S6 now points at
  AC7, and the root-claims-everything refusal AC6 grades is owned by S4. D6: S7 adds the path-mode
  entry point unit 7's profile-time probe needs. D9: §3 states that descendant inheritance is unit
  4's rule, so a standalone refusal is not mistaken for a tree-wide one.

## 10. Reuse audit

No existing seam fits, and the near candidates were opened rather than assumed.
`python tools/codebase-map/reuse_lookup.py "kill a hung or idle background process and report it to
the session"` surfaced no path-containment helper. Checked by hand: `tools/govkit/govkit.py` holds
containment logic for the deploy surface and `tools/memory-tree/gen_build_index.py` holds path
normalization, but both work over repo-relative tracked paths from `git ls-files` — a closed,
normalized population — while this unit grades arbitrary command strings carrying three spellings
of one path plus environment assignments. Extending either would widen a tracked-file helper to
accept untrusted text, which is the wrong direction.

What IS reused is a CLASS rather than code: `memory/gotchas/containment-tested-one-way.md`, which
§4 and AC5/AC6 are written from, and which the bug-class checklist selected for these paths.

Recall terms used: `gate runner wall clock bound timeout kill children orphan process leg pool
watchdog GATE_WALL background subprocess reaper`
