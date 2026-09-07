# TOOL-aReapedSpinner-2 — the scope fence: attribution is a TREE property, computed once

**Status:** OPEN · rev-3 · 2026-09-08 · node a · Tier-2 · base e2b82a53 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-08-build-TOOL-aReapedSpinner-2-live-predicate-run.md](../build/2026-09-08-build-TOOL-aReapedSpinner-2-live-predicate-run.md) | research | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-3 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md) | spec-audit | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round2.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round2.md) | spec-audit | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7 |

<!-- /gen:spec-records -->

## 1. Goal

Decide which census rows this repo's agent work OWNS, so nothing downstream can name — let alone
kill — a process belonging to somebody else, including another agent session on the same machine.
This is the safety property the whole kit rests on.

## 2. Scope (IN)

- **S1** — `tools/process-monitor/scope.py`, exposing `derive_scope(census, conf, self_chain)`
  returning the in-scope SET of winpids plus, per member, the ROOT that admitted it. One call over
  the whole census; not a per-row predicate. Observed by AC1.
- **S2** — ATTRIBUTABLE ROOTS: a row is a root when a declared `PROCMON_ROOTS` prefix matches its
  resolved program path or one of its path-shaped argument TOKENS, per §4's tokenizer, and it is
  not in `self_chain`. Observed by AC1, AC2, AC8.
- **S3** — THE CLOSURE: the in-scope set is the roots plus their transitive descendants over the
  UNION of the census's two parent graphs. Nothing else is in scope. Observed by AC3, AC9.
- **S4** — the SELF fence: the calling process, every ancestor of it, and their descendants reached
  only through them are excluded, and a root is never taken from `self_chain`. Observed by AC4.
- **S5** — a blank or absent `PROCMON_ROOTS` REFUSES, and so does a root shorter than a declared
  minimum or equal to a filesystem root. Observed by AC5, AC6.
- **S6** — prefix matching is normalized, case-folded and separator-anchored, so `…/repo` does not
  admit `…/repo-other`. Observed by AC7.
- **S7** — `scope.py --explain <winpid>` prints whether one row is in scope and by which root and
  chain. Observed by AC10.
- **S8** — a row whose `command` is `None` cannot be a ROOT, but may still be a DESCENDANT of one.
  Unattributable rows that are in no closure are COUNTED and the count is printed. Observed by AC11.

## 3. Non-goals (OUT)

- **No per-row standalone verdict as the fence.** rev-2 graded each row alone, which refused every
  bare-argv leaf and every relative-argv leg shell — measured, a leg shell carries a relative script
  path and `.githooks/pre-push:292` invokes the runner relatively. That produced D9, then D17's
  vacuous repair, then D20. All three are one defect: attribution is a property of a TREE, and a
  process is ours because of where its ancestry starts, not because of what its own argv happens to
  spell.
- **No raw-string containment.** D11's finding stands and §4 keeps its answer.
- **No declared scratch or temp root.** rev-2 needed one so the gate runner's `mktemp -d` legs were
  admissible, which collided with the rule forbidding the temp root, and on this node they are the
  same directory (D16). Under S3 the leg is in scope because its ANCESTOR is, so no scratch root is
  declared and the collision does not exist.
- **No inference from the process name, no user or session filtering, no cwd probing.**
- **No re-checking inside the reaper.** Unit 4 checks MEMBERSHIP of this set. rev-2's per-member
  inheritance clause admitted every member unconditionally (D17); a set computed once cannot be
  vacuous in that way.

### Edges

- **consumes-from** `TOOL-aReapedSpinner-1` — `command`, `winpid`, and BOTH parent graphs. The
  closure is over their union, so a native descendant of an MSYS process is reachable.
- **consumes-from** `TOOL-aReapedSpinner-6` — `PROCMON_ROOTS`.
- **hands-off** `TOOL-aReapedSpinner-3` — the classifier grades only members of this set.
- **hands-off** `TOOL-aReapedSpinner-4` — the reaper kills only members of this set, and tests
  membership rather than re-deriving attribution.
- **hands-off** `TOOL-aReapedSpinner-7` — S7's explain mode is what the gate runner uses at profile
  time to confirm its own process is a root, before any leg is dispatched.

## 4. Design

### The tokenizer, which is what D11 and D19 are both about

A row's `command` is decomposed before any matching, never matched as one string:

1. **Word-split** the command line, honouring quotes.
2. **Strip every `NAME=value` token wherever it appears** — leading, or after `export`, `env`,
   `declare`, `set` — and INSIDE a `-c` / `-Command` body, which is itself word-split and processed
   by these same rules rather than treated as one token.
3. What remains: the resolved PROGRAM PATH (the first non-assignment token) and every PATH-SHAPED
   ARGUMENT (a token containing a separator).

A declared root must prefix-match the program path or one of those arguments.

**Why, measured.** Every Claude Bash-tool shell here carries
`bash.exe -c "source … && export TEMP='<tempdir>' TMP='…' && …"`. rev-2 defined an assignment as
"`NAME=value` before the first program token", which does not describe that shape at all: the
assignment sits after `bash.exe`, after `source`, behind `export`. Under rev-2's rule
`TEMP=<tempdir>` was an ARGUMENT containing separators, hence path-shaped, hence admitting — the
exact vector D11 was written to close, left open by its own repair (D19).

**And the honest limit.** Even with the strip, declaring a root under the shared temp directory
would admit sibling sessions through their GENUINE path-shaped arguments — measured, all nine live
rows carrying `export TEMP=` also name a real path under it. That is why no temp or scratch root is
declared at all (§3), and why unit 6 §4 keeps the prohibition. The tokenizer closes the assignment
vector; the non-declaration closes the rest.

### The closure, and why it is the whole fence

Roots are computed over the census. The in-scope set is their transitive descendant closure over
`win_ppid ∪ msys_ppid`. Consequences worth stating because each was a separate round-2 finding:

- A leg shell with a relative argv is in scope: its ancestor chain reaches a shell whose argv
  carries an absolute repo path (D20).
- A `sleep` with a bare argv is in scope: same reason (D9).
- A `mktemp -d` scratch is irrelevant to attribution (D16).
- A native `python.exe` leg is in scope and so are ITS children, because the closure runs over the
  union of both graphs (D22).
- A process whose ancestry is DEAD is NOT in scope. That is the limit this build recorded in its
  live-predicate run — `sleep 27200` at 7.5 h is real, live and unattributable — and it is not
  designed around. An adopter may declare more roots; the report names the count.

**A recycled or stale parent edge cannot smuggle a row in**, because a child's start time must not
precede its parent's: an edge whose child is OLDER than its claimed parent is dropped from the
closure and counted. That is the corroboration round 2 asked for, applied where it belongs — in the
graph, once, rather than per member inside the reaper.

### The self fence

`self_chain` is the calling process and its ancestors, walked over the same union graph. Those rows
are never roots. A row reachable ONLY through the self chain is excluded with them; a row also
reachable from a genuine root stays in scope, because it is genuinely ours.

### Files touched (estimate)

`tools/process-monitor/scope.py` new; arms and a frozen census fixture added under
`tools/process-monitor/`.

## 5. Production-readiness checklist

- security — this IS the security unit. D11, D16, D17, D19 and D20 were all its predicate shape.
- perf / scale — one tokenize per row plus one graph walk; linear in the table.
- error / empty / loading states — blank or over-broad roots REFUSE; an empty closure is reported as
  "0 in scope of N rows, M unattributable", never as a bare "nothing to report".
- observability — `--explain`, the admitting root per member, the unattributable count, and the
  dropped-edge count.
- risks — an over-broad declared root, and a root under the temp directory. Mitigated by the
  minimum-length refusal, the tokenizer, and unit 6 §4's prohibition with its own criterion.
- testing — a FROZEN census fixture captured from this node, and an arm asserting `derive_scope`
  admits a hand-checked winpid set over it and no others. A synthetic fixture did not catch D11 and
  would not catch D19.
- migration — none.
- user docs — the kit README's scope section, unit 6.

## 6. Acceptance criteria

- **AC1** — When `derive_scope` runs over the frozen fixture, the returned set equals a
  hand-enumerated expected set recorded in the test, and each member names the root that admitted
  it. Observed by `selftest.py`, arm `test_scope_over_the_frozen_corpus_is_exact`.
  Red when: the set differs in either direction. This is the corpus arm round 2 asked for: a
  carve-out whose precondition never occurs reds at authoring time rather than at adoption.
- **AC2** — When a row's program path is under a declared root, it is a ROOT and its verdict names
  that root. Observed by `selftest.py`, arm `test_declared_root_admits_and_names_it`.
  Red when: a member is admitted with no admitting root, which makes an over-broad root
  undiagnosable.
- **AC3** — When a fixture stages `bash(root argv) → bash -c(relative argv) → sleep(bare argv) →
  python.exe(native)`, all four are in scope and the last two are in scope ONLY by closure.
  Observed by `selftest.py`, arm `test_closure_reaches_bare_argv_and_native_descendants`.
  Red when: any is refused. rev-2 refused three of the four, which is D9, D20 and D22 together.
- **AC4** — When the calling process and its ancestors are graded, none is a root, and a row
  reachable only through them is not in scope; a row also reachable from a genuine root IS.
  Observed by `selftest.py`, arm `test_self_chain_is_never_a_root`.
  Red when: only the immediate parent is excluded, leaving the session's own shell killable; or the
  whole self-reachable subtree is excluded, which would exclude everything the session started.
- **AC5** — When `PROCMON_ROOTS` is blank, `derive_scope` raises and `scope.py` exits non-zero
  naming the key. Observed by `selftest.py`, arm `test_blank_roots_refuses`.
  Red when: a blank list yields an empty set and the kit reports a clean tree it never examined.
- **AC6** — When a root of `/`, a one-character root, or one below the declared minimum is
  declared, the conf read REFUSES. Observed by `selftest.py`, arm
  `test_root_that_claims_everything_refuses`.
  Red when: the check is advisory and the run continues.
- **AC7** — When the declared root is `/c/projects/gov`, a row naming `/c/projects/gov-scratch/x` is
  not a root and one naming `/c/projects/gov/x` is. Observed by `selftest.py`, arm
  `test_prefix_is_separator_anchored`.
  Red when: the match is a bare containment test, which admits the sibling.
- **AC8** — When a CONSTRUCTED row's only occurrence of a declared root is inside an
  `export NAME=<root>` within a `-c` body, that row is not a root. Observed by `selftest.py`, arm
  `test_assignment_inside_a_dash_c_body_does_not_admit`.
  Red when: the assignment is treated as a path-shaped argument (rev-2's rule) or the `-c` body is
  treated as one opaque token.
  `fixture:` CONSTRUCTED, and stated as such. rev-2 claimed this shape was "the real Bash-tool
  shape, taken from a captured snapshot"; checked, and in zero of the nine live rows carrying
  `export TEMP=` is the assignment the ONLY occurrence — every one also names a genuine path under
  that root (D19). The vector is real, the isolated instance is not, and the fixture says so.
- **AC9** — When a fixture stages a row whose parent edge names an in-scope process that started
  LATER than the child, that row is not in the closure and the dropped-edge count is non-zero.
  Observed by `selftest.py`, arm `test_recycled_parent_edge_is_dropped_and_counted`.
  Red when: any edge is trusted on the id alone, which lets a recycled pid attach an arbitrary
  process to an in-scope tree — the blast-radius question round 2 asked about inheritance.
- **AC10** — When `scope.py --explain <winpid>` is given a live winpid, it prints one line saying in
  scope or not, and the root and chain if so. Observed by `selftest.py`, arm
  `test_explain_answers_one_row`.
  Red when: it prints the whole table, which is the census's job and hides the answer.
- **AC11** — When a fixture row has `command = None`, it is never a root, IS admitted if it is a
  descendant of one, and is counted as unattributable when it is in no closure. Observed by
  `selftest.py`, arm `test_no_command_row_can_be_a_descendant_but_not_a_root`.
  Red when: such rows are silently dropped — measured, 115 of 314 rows here — or promoted to roots.

## 7. Gates

`line length` · `lexicon naming predicates` · `govkit selfcheck` · `dead-path carriers (deleted files still named)`

New arm: `tools/process-monitor/selftest.py` · stages the frozen corpus, blank and over-broad roots,
a sibling-prefix root, a four-deep mixed-namespace tree with bare and relative argv, a constructed
assignment-only row, a recycled parent edge, and a `None` command · floor moves with unit 1's arms,
one suite.

## 8. Open questions

- **F1 — may a row with no `command` be in scope?**
  RESOLVED (agent, 2026-09-08, delegated): NOT AS A ROOT, YES AS A DESCENDANT. It cannot attribute
  itself, so it cannot start a tree; but a child of a known-ours process is ours whatever it reports
  about itself, and refusing it outright would exclude a third of the table from a tree we already
  own. Vetoes clean.
- **F2 — should attribution be per-row or tree-closure?**
  RESOLVED (agent, 2026-09-08, delegated): TREE-CLOSURE. Per-row was measured to refuse every
  bare-argv leaf, every relative-argv leg shell and every native descendant, and its two attempted
  repairs produced a vacuous check (D17) and an unreachable delegation (D20). Closure resolves all
  three and removes the need to declare a scratch root, which removes D16. The cost is stated: the
  blast radius of a mis-declared root is now a whole subtree rather than one row — priced by the
  minimum-length refusal, the tokenizer, the start-time corroboration in §4, and AC1's exact
  corpus assertion. Vetoes clean: nothing new is depended on, and the kill surface narrows for
  every process whose ancestry is not ours.

## 9. Revision log

- rev-1 · 2026-09-08 · initial draft.
- rev-2 · 2026-09-08 · S2 · S6 · S7 · S8 · §4 · AC6-AC10 · folded round 1 (D3, D6, D9, D11).
- rev-3 · 2026-09-08 · §1 · S1 · S2 · S3 · S4 · S8 · §3 · §4 · every AC · §8 F2 · folded round 2.
  D9/D17/D20 collapse into one root cause and one fix: attribution becomes a TREE CLOSURE computed
  once (S1, S3), so a bare-argv leaf and a relative-argv leg shell are in scope by ancestry and the
  reaper tests membership instead of re-deriving anything. D16 dissolves — no scratch or temp root
  is declared at all. D19: the tokenizer now strips `NAME=value` wherever it appears including
  inside a `-c` body, and AC8 declares its fixture CONSTRUCTED because the shape rev-2 claimed to
  have captured does not occur in the corpus. D22: the closure runs over the union of both parent
  graphs. Round 2's corroboration ask lands as the start-time edge check in §4 and AC9.

## 10. Reuse audit

No existing seam fits. `python tools/codebase-map/reuse_lookup.py "kill a hung or idle background
process and report it to the session"` surfaced no path-containment helper, and its coverage line
reads `unscanned layers: .sh`, so that miss is weak evidence and was checked by hand:
`tools/govkit/govkit.py` holds containment logic for the deploy surface and
`tools/memory-tree/gen_build_index.py` holds path normalization, but both work over repo-relative
tracked paths from `git ls-files` — a closed, normalized population — while this unit tokenizes
arbitrary command strings carrying three spellings of one path plus shell assignments. Extending
either would widen a tracked-file helper to accept untrusted text.

What IS reused is a class rather than code: `memory/gotchas/containment-tested-one-way.md`, which
§4 and AC6/AC7 are written from, and which the bug-class checklist selected for these paths.

Recall terms used: `gate runner wall clock bound timeout kill children orphan process leg pool
watchdog GATE_WALL background subprocess reaper`
