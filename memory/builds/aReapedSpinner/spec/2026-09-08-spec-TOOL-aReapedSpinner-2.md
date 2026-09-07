# TOOL-aReapedSpinner-2 — the scope fence: attribution is positive, declared, and never the caller

**Status:** OPEN · rev-1 · 2026-09-08 · node a · Tier-2 · base e2b82a53 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-08-build-TOOL-aReapedSpinner-2-live-predicate-run.md](../build/2026-09-08-build-TOOL-aReapedSpinner-2-live-predicate-run.md) | research | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-3 |

<!-- /gen:spec-records -->

## 1. Goal

Decide which census rows this repo's agent work OWNS, so that nothing downstream can name — let
alone kill — a process that belongs to somebody else. This is the safety property the whole kit
rests on, and it is a separate unit because it must be gated separately.

## 2. Scope (IN)

- **S1** — `tools/process-monitor/scope.py`, exposing `check_in_scope(row, conf, self_chain)`
  returning a verdict plus the REASON it was admitted. Observed by AC1.
- **S2** — POSITIVE attribution only: a row is in scope when its `command` contains one of the
  declared `PROCMON_ROOTS` prefixes. Nothing is in scope by default and there is no exclusion list.
  Observed by AC1 and AC2.
- **S3** — the SELF fence: the calling process, every ancestor of it, and the census backend's own
  children are excluded whatever else matches. Observed by AC3.
- **S4** — a blank or absent `PROCMON_ROOTS` REFUSES rather than matching nothing. Observed by AC4.
- **S5** — prefix matching is anchored and separator-aware, so a declared root `…/repo` does not
  admit `…/repo-other`. Observed by AC5.
- **S6** — `scope.py --explain <pid>` prints why one row was admitted or refused, so a surprising
  verdict is diagnosable without reading source. Observed by AC6.

## 3. Non-goals (OUT)

- **No classification and no killing.** This unit answers "is this ours", nothing else.
- **No inference from the process name.** A row is not in scope because it is called `bash` or
  `python`; only a declared root admits it. Naming-based attribution is how a monitor reaps an
  unrelated editor.
- **No user or session filtering.** The observed failures include processes whose launching session
  was long dead, so a same-session predicate would miss exactly the population that matters.
- **No cwd probing.** A dead-parent orphan's cwd is unreliable and reading `/proc/<pid>/cwd` has no
  Windows equivalent. The command string is what both backends give.

### Edges

- **consumes-from** `TOOL-aReapedSpinner-1` — the `command` and `pid` fields. Without the census
  there is no population to fence.
- **consumes-from** `TOOL-aReapedSpinner-6` — `PROCMON_ROOTS`, declared in `.process-monitor.conf`.
- **hands-off** `TOOL-aReapedSpinner-3` — the classifier grades ONLY rows this unit admitted.
- **hands-off** `TOOL-aReapedSpinner-4` — the reaper kills ONLY rows this unit admitted, and
  re-checks rather than trusting a list handed to it.
- **hands-off** `TOOL-aReapedSpinner-7` — the gate runner's scratch roots must be DECLARED here, or
  the reaper refuses every leg pid and the runner falls back.

## 4. Design

### The containment test, both ways

The selected bug class `containment-tested-one-way` is the failure mode here, verbatim: *a guard
asking only "is this path under the protected one" refuses the narrow declarations and admits the
one that claims everything.* Two consequences this unit must satisfy:

1. A root of `/` or an empty string must NOT admit the whole table. Handled by S4's refusal on
   blank plus a minimum-length check on each declared root.
2. Matching is on a normalized, separator-terminated prefix. `/c/projects/coding-governance` admits
   `/c/projects/coding-governance/x` and refuses `/c/projects/coding-governance-scratch`.

Paths are normalized to forward slashes and case-folded before comparison, because the same tree is
spelled `C:/projects/...`, `C:\projects\...` and `/c/projects/...` by three different producers in
one command string on this node.

### The self fence

`check_in_scope` takes `self_chain` — the set of pids from the calling process up to the root of its
own ancestry, walked over the census's own `ppid` edges. The measurement that makes this
non-negotiable: the disposable test tree's descendants shared the Bash-tool shell's pgid, and that
shell is an ancestor of anything the monitor runs from a session. A fence that omitted it would let
a sweep kill the session running the sweep.

**The self chain is computed from the census, not from `os.getppid()` alone**, because the reaper
must exclude the whole chain and not just the immediate parent.

### Files touched (estimate)

`tools/process-monitor/scope.py` new; one `[[files]]` claim already covers it via unit 6's `**`.

## 5. Production-readiness checklist

- security — this IS the security unit. It is the only thing standing between a kill loop and an
  unrelated process, and every other unit is written to trust it.
- perf / scale — a string containment test per row over a few hundred rows; immeasurable.
- error / empty / loading states — blank roots REFUSE (S4); zero admitted rows is a legitimate
  answer and is reported as "0 of N in scope", never as a bare "nothing to report".
- observability — `--explain` (S6) plus the admission reason carried on every verdict.
- risks — an over-broad declared root. Mitigated by the minimum-length check and by `--explain`,
  not by hoping the adopter is careful.
- testing — a table-driven arm over adversarial roots: blank, `/`, a single character, a root that
  is a prefix of a sibling directory, mixed separators, mixed case.
- migration — none.
- user docs — the kit README's scope section, unit 6.

## 6. Acceptance criteria

- **AC1** — When a row whose command contains a declared root is graded, it is admitted and its
  verdict names the root that admitted it. Observed by `selftest.py`, arm
  `test_declared_root_admits_and_names_it`.
  Red when: a row is admitted with no reason, which makes an over-broad root undiagnosable.
- **AC2** — When a row whose command matches NO declared root is graded, it is refused. Observed by
  `selftest.py`, arm `test_undeclared_row_is_refused`.
  Red when: the predicate falls through to admit-by-default on any input shape.
- **AC3** — When the calling process and each of its ancestors are graded — every one of which sits
  under a declared root and would otherwise be admitted — all are refused. Observed by
  `selftest.py`, arm `test_self_chain_is_never_in_scope`.
  Red when: only the immediate parent is excluded, which leaves the session's own shell killable.
- **AC4** — When `PROCMON_ROOTS` is blank, `check_in_scope` raises and `scope.py --explain` exits
  non-zero naming the key. Observed by `selftest.py`, arm `test_blank_roots_refuses`.
  Red when: a blank list matches nothing and the kit reports a clean tree it never examined.
- **AC5** — When the declared root is `/c/projects/gov`, a row whose command names
  `/c/projects/gov-scratch/x` is REFUSED and one naming `/c/projects/gov/x` is admitted. Observed
  by `selftest.py`, arm `test_prefix_is_separator_anchored`.
  Red when: the match is a bare `in` test, which admits the sibling — the
  `containment-tested-one-way` class, selected for these paths.
- **AC6** — When a root of `/` or of a single character is declared, the conf read REFUSES rather
  than admitting the whole table. Observed by `selftest.py`, arm `test_root_that_claims_everything`.
  Red when: the minimum-length check is written as advisory and the run continues.
- **AC7** — When `scope.py --explain <pid>` is given a live pid, it prints one line saying admitted
  or refused and why. Observed by `selftest.py`, arm `test_explain_answers_one_pid`.
  Red when: `--explain` prints the whole table, which is the census's job and hides the answer.

## 7. Gates

`line length` · `lexicon naming predicates` · `govkit selfcheck` · `dead-path carriers (deleted files still named)`

New arm: `tools/process-monitor/selftest.py` · stages blank roots, a one-character root, a
sibling-prefix root, mixed separators, and the caller's own ancestry · floor moves with unit 1's
arms, one suite.

## 8. Open questions

- **F1 — should a row with no `command` string be admitted or refused?**
  RESOLVED (agent, 2026-09-08, delegated): REFUSED, and counted. A row the backend could not
  describe cannot be attributed, and admitting it would put an unidentifiable process in front of
  the reaper. The count is reported so an adopter whose backend returns many such rows learns that
  rather than seeing a quietly smaller population — a silent drop here is the same
  green-by-absence class the build rules forbid.

## 9. Revision log

- rev-1 · 2026-09-08 · initial draft.

## 10. Reuse audit

No existing seam fits. The probe
`python tools/codebase-map/reuse_lookup.py "kill a hung or idle background process and report it to
the session"` surfaced no path-containment helper anywhere in the corpus. Checked by hand against
the nearest candidates: `tools/govkit/govkit.py` has containment logic for the deploy surface and
`tools/memory-tree/gen_build_index.py` has path normalization, but both work over repo-relative
tracked paths from `git ls-files` — a closed, normalized population — while this unit grades
arbitrary command strings carrying three spellings of one path. Extending either would widen a
tracked-file helper to accept untrusted text, which is the wrong direction. The `containment-tested-one-way`
gotcha class IS reused: it is what §4 and AC5 are written from.

Recall terms used: `gate runner wall clock bound timeout kill children orphan process leg pool
watchdog GATE_WALL background subprocess reaper`
