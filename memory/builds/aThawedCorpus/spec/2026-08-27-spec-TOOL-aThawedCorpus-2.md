# TOOL-aThawedCorpus-2 — the memory legs declare what they read, so the freeze that exists can reach them

**Status:** WONTDO · rev-2 · 2026-08-27 · node a · Tier-2 · base f1be0b49 · streams tooling · order 4 · retired, see §9 rev-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-review-TOOL-aThawedCorpus-5-spec-audit.md](../reviews/2026-08-27-review-TOOL-aThawedCorpus-5-spec-audit.md) | spec-audit | TOOL-aThawedCorpus-5 TOOL-aThawedCorpus-4 TOOL-aThawedCorpus-1 TOOL-aThawedCorpus-3 |

<!-- /gen:spec-records -->

## 1. Goal

`run-gates.sh` already carries the freeze the owner asked for: `input_key` keys a leg on
`git ls-files -s` over its declared guard pathspecs plus their dirty share, and `GATE_REUSE` skips a
leg whose key is unchanged and whose last verdict was green. The memory legs are excluded from it
because they declare no `guard`, so their key is the whole-tree fingerprint and moves on every commit
anywhere. Make each memory leg declare the input set it actually reads, and prove the declaration is
neither under- nor over-stated.

## 2. Scope (IN)

- **S1** — Derive, by reading the sources rather than by assumption, the true input set of every
  `tools/memory-tree/` gate leg, and record the derivation in this build's folder as a table of
  `<leg> → <path or pathspec> → <the line that reads it>`.
- **S2** — Declare a `guard` in `tools/gate-legs.json` for every leg whose derived input set is a
  proper subset of the tree, and declare NOTHING for a leg whose input set is the tree — an
  unguarded leg is the correct declaration for a whole-tree reader, not an omission.
- **S3** — A `guard-covers-its-reader` arm: for each declared pathspec, stage a byte change under it
  and assert the leg's `input_key` MOVES; and for at least one path the leg reads but the guard would
  exclude, assert the key does NOT move — the under-declaration case, observed RED before the
  pathspec is added and green after.
- **S4** — The arm PRINTS its population every run: how many legs were graded, how many pathspecs
  were exercised, and which legs are deliberately unguarded with the reason. A guard nobody can see
  the scope of is a skip nobody can audit.
- **S5** — Resolve F1 below with the post-collapse measurement, and record the answer with its
  numbers before any guard is declared.

## 3. Non-goals (OUT)

- **N1** — No new cache, digest helper, freeze file or skip state. The mechanism exists, it is
  content-addressed, it is fail-open and it is gated; a second one would be two answers to one
  question, which is a bug class this corpus carries a record for.
- **N2** — `GATE_REUSE` stays OPT-IN and `.githooks/pre-push` still never sets it. That boundary is a
  recorded decision — an advisory input may cause less work only on a run that is not authoritative —
  and this unit does not reopen it.
- **N3** — No change to what any check MEANS, and no check may become unreachable. A guard that drops
  a check is a coverage loss wearing a performance costume.
- **N4** — No new conf key. The declaration lives in `tools/gate-legs.json`, which is where a leg's
  other properties already live and which adopters already own.

## 4. Design

### Inventory

Read from source, not assumed. `check-memory-hygiene.sh` reads: `git ls-files "$M/"`;
`.memory-tree.conf`; `.codebase-map.conf` for the `MAP_SUB` carve-out; `$M/project/legacy-files.txt`
and `curation-debt.txt`; its own bytes; and its four sibling modules under `tools/memory-tree/`.

**And one thing more, which is the whole difficulty.** `corpus_ids.py`, behind checks 13-16, resolves
cited repository paths against the WHOLE `git ls-files` index and reads the `CHARTER` document. So a
tracked file deleted anywhere in the repo can legitimately red this leg. The delegating half is a
whole-tree reader; the shell half is not.

That is why S2 admits "declare nothing" as an outcome. A guard naming `memory/` alone would be
under-declared for checks 13-16, and the failure mode is silent: the leg would skip on a commit that
broke it. The measured cost of the delegating half is 47.4 s of a 1398 s run, so buying its scope back
is worth very little, and this spec does not assume the answer — F1 decides it against the
post-collapse baseline.

### Rollout

Declaration only, landed after the two collapse units so the remaining cost is the one being priced.
No default changes: an unset `GATE_REUSE` behaves exactly as today, and a guard only ever causes a
leg to be skipped on a run whose diff does not touch its declared inputs.

### Files touched (estimate)

`tools/gate-legs.json` — guard declarations. A new arm file under `tools/run-gates/` or
`tools/memory-tree/`, per F2. `memory/builds/aThawedCorpus/build/` — the derivation table.

### Alternatives rejected

- **A kit-local digest helper with its own skip state.** Rejected under N1. It was this build's first
  design and the reuse audit killed it: `input_key` already computes exactly that digest, from
  `git ls-files -s`, for the right reason, with the fail-open law this repo already runs under.
- **Guarding the leg on `memory/` and accepting the check 13-16 gap.** Rejected: the gap is silent,
  and §7 of the charter names silent-skip as its own defect class.
- **Splitting the checker into two legs at the shell/python boundary.** Not rejected — it is F1's
  second option, and it is not chosen before the collapse is measured.

## 5. Production-readiness checklist

- security — N/A. Declarations about which files a check reads; no new surface.
- perf / scale — the subject. §6 carries the observable.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an unresolvable fingerprint already yields a dash key, which the
  reuse unit treats as never-matching. This unit adds no new failure mode and inherits that one.
- observability — S4's printed population, on every run of the arm.
- risks — the ONLY real risk is an under-declared guard, whose failure mode is a silent skip. S3 is
  the control and it is a staged break, not an argument.
- testing + left-shift gates — the new arm is a gate leg. The `run-gates canary` already refuses a
  guard naming an untracked path, so that class is covered upstream and is not re-implemented.
- migration / rollback — a JSON declaration; revert is a one-line revert.
- user docs — `tools/memory-tree/README.md` gains a line naming which legs are guarded and why one
  is not. No user-facing surface beyond that.

## 6. Acceptance criteria

- **AC1** — When a byte is changed under each declared guard pathspec in turn, the leg's `input_key`
  differs from its unchanged value, once per pathspec, asserted by the new arm.
- **AC2** — When the arm is run with a pathspec deliberately removed from a leg's `guard` in
  `tools/gate-legs.json`, it REDS naming that leg — the under-declaration case observed red, then
  restored.
- **AC3** — When `bash tools/run-gates/run-gates.sh` is run twice with `GATE_REUSE=1` on an unchanged
  tree, the second run prints `GATE reuse` for every newly guarded memory leg.
- **AC4** — When a commit touches only `tools/govkit/`, a `GATE_REUSE=1` bar reuses the guarded
  memory legs, and a bar without `GATE_REUSE` skips them by guard — both observed in the run's own
  output, not inferred.
- **AC5** — When the arm runs, its stdout carries the number of legs graded, the number of
  pathspecs exercised, and each deliberately unguarded leg with its reason — the `memory hygiene`
  row among them.
- **AC6** — When `bash tools/run-gates/run-gates.sh` runs with the declarations in place, the set of
  checks that execute over an unchanged tree is unchanged from before this unit — no check became
  unreachable, asserted by diffing the checker's own output.

## 7. Gates

`memory hygiene` · `run-gates canary` · `run-gates evidence` · `govkit selfcheck` (a new leg must be
declared in the tooling registry). Adds one leg, the `guard-covers-its-reader` arm.

## 8. Open questions

- **F1 — after the two collapse units land, is the guardable half still worth guarding?**
  RESOLVED (agent, 2026-08-27, delegated): NO, and the unit is retired rather than re-scoped. The
  spec audit established that guard-skip is decided at `run-gates.sh:762`, BEFORE the reuse loop at
  `:855`, which opens `[ -f "$WORK/$i.rc" ] && continue` — so a guarded leg is skipped and never
  reused, and this unit's stated goal was a misdescription of what a guard buys.

- **F2 — where does the arm live?** RESOLVED (agent, 2026-08-27, delegated): nowhere. `input_key` is
  an internal shell function with no print mode and no external surface, so the arm this unit needs
  cannot be written without first changing `run-gates.sh`, which is another kit and another owner.

## 9. Revision log

- rev-1 · 2026-08-27 · initial draft, after the reuse audit found `input_key` and `GATE_REUSE`
  already implement the mechanism this unit was first specced to build.
- rev-2 · 2026-08-27 · RETIRED (WONTDO). Three findings from the M4 spec audit, each verified
  against `main` after regrounding: guard-skip preempts reuse so the goal was misdescribed;
  `input_key` has no readable surface for the arm; and `memory hygiene` is unguarded TODAY, which is
  exactly why `.githooks/pre-push` runs it on both its forced and its scoped branch — the
  compensating control `TOOL-aThawedCorpus-5` depends on. Guarding it would open the hole that unit
  relies on not existing. No successor: the freeze the owner asked for already exists and the memory
  leg is deliberately outside it.

## 10. Reuse audit

**The seam is `tools/run-gates/run-gates.sh`'s `input_key` and its reuse unit**, plus the `guard`
field of `tools/gate-legs.json`. Found by reading `run-gates.sh` while pricing a kit-local digest
helper; it computes the same content key this unit needed, from `git ls-files -s` plus the guard's
share of the porcelain, and `GATE_REUSE` consumes it under a fail-open law spelled out in its own
comment. `TOOL-aPacedTurnstile-6` is the unit that built it and its spec carries the acceptance
criteria this one's AC3 mirrors. `tools/run-gates/gate-fingerprint.sh` is the whole-tree sibling and
is deliberately NOT extended: a per-pathspec form already exists inside `input_key`.

`python tools/codebase-map/reuse_lookup.py "skip re-checking a memory build folder whose content has
not changed since it was last verified"` returned `build_cache` at `tools/memory-recall/query.py`,
which is the mtime-keyed cache this build's measurement record rules out as a model.

Recall terms used, because M7 re-runs the query: `cache freeze closed build corpus walk hygiene gate
fingerprint incremental stale mtime tree-hash rescan`. It surfaced `TOOL-aQuarriedLantern-1`'s review
finding F1 — the recall cache's freshness key omitted the conf, so every construct moved into
`.memory-tree.conf` was served stale. That is the exact defect S1's derivation exists to avoid here,
one mechanism over.
