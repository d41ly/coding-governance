# TOOL-aDrainedSluice-9 — V8: a dead DIRECTORY citation is a dead citation

**Status:** INPROGRESS · rev-3 · 2026-08-08 · node a · Tier-2 · base 76fcd09b · streams tooling

## 1. Goal

The flatten moved every build folder, and citations of the old paths remain. Check 15 was supposed to
catch the live ones and reported zero. Measured: there are four, all in
`memory/project/in-flight/a.md`, and check 15 cannot see them because they are DIRECTORY citations
and its harvest requires a file extension.

## 2. Scope (IN)

- **S1** — check 15's harvest accepts a rooted token with no extension when it is a plausible
  DIRECTORY citation: it contains a slash, its first segment is a real top-level directory, and it
  either ends in `/` or names no dotted basename. Resolution already handles directories — a cited
  path resolves if it is a tracked file OR a prefix of one — so only the harvest was narrow.
- **S2** — the measured census is recorded: 26 `(citing file, dead path)` pairs across 17 files, of
  which 4 sit in the present-tense corpus and 22 sit in frozen build records or the append-only log.
- **S3** — the four live ones are REPAIRED, not registered. The ledger is live navigation in the
  present-tense corpus; the registry exists for citations that cannot legally be edited.
- **S4** — the 22 frozen ones are left alone, and the reason is written where a reader will look:
  `builds/` and the append-only areas are records of a moment, and the present-tense scope is what
  makes that boundary mean something. Widening the scope to them would make the registry a permanent
  inventory of history rather than a shrink-only repair list.
- **S5** — `DEAD_PATH_PIN` is re-measured after the repair. If the repair takes it to zero it stays
  zero, and the ratchet is armed against the next unresolving citation.
- **S6** — the selftest gains a directory-citation arm in both directions: a cited directory that
  resolves is silent, one that does not is reported.
- **S7** — the harvest widening is checked against a false-positive population before it is trusted:
  every token it newly accepts across the whole corpus is listed, and anything that is not a repo
  path is a reason to narrow the rule, not to waive the finding. MEASURED BEFORE ANY EDIT: the
  widened harvest newly accepts SIX tokens in the present-tense corpus. One resolves and is silent.
  Five are dead — four are the pre-flatten build paths S3 repairs, and the fifth is
  `.claude/worktrees/<name>`, a CHECKOUT LOCATION rather than repo content.
- **S8** — that fifth token is the finding the census bought, and the reason it needs a declared
  exclusion is NOT node-dependence. The draft said the worktree path "exists on this machine and not
  on another"; that is factually wrong about the code. Check 15's resolution never touches the
  filesystem — it is membership in `git ls-files` plus a prefix scan over the same index — so
  `.claude/worktrees/<name>` classifies as DEAD identically on every node. The real reason is that a
  checkout LOCATION is not repo CONTENT, and no resolution rule can express that, because the
  question is about meaning rather than existence. So the exclusion is DECLARED:
  `.memory-tree.conf` gains `DEAD_PATH_EXCLUDE`, a space-separated prefix list defaulting to
  `.claude/worktrees/`, documented as "paths that are not repo CONTENT".
- **S8b** — the fixture gains a tracked `.claude/` path. The module's `_scratch()` tracks only
  `AGENTS.md`, `.memory-tree.conf` and `memory/**`, so `_roots()` yields `{memory/}` and a
  `.claude/worktrees/x` citation never becomes a candidate at all — both exclusion arms would pass
  without exercising the rule.

## 3. Non-goals (OUT)

- Registering the 22 frozen citations. S4 covers why.
- Rewriting any frozen record to repoint a citation. That is the rewrite-history move the whole
  registry mechanism exists to avoid.
- Accepting a bare token with no slash. `README.md` on its own is not a repo path claim, and the
  upstream measurement of a loose rule found 13 085 hits whose top entries were package specifiers
  and git refs.

## 4. Design

### Data model

```
today  : accept token if it endswith(KNOWN_EXT) or "." in basename(token)
after  : accept ALSO if "/" in token and first segment is a real top-level dir
         and (token ended with "/" or basename has no dot)
resolve: unchanged — tracked file, or prefix of a tracked path
```

The trailing slash is stripped before resolution, as it already is; the widening is purely about what
enters the candidate set.

### Inventory

| Concern | Change |
|---|---|
| `corpus_ids.py` harvest | directory citations enter the candidate set |
| `memory/project/in-flight/a.md` | four citations repointed at the flat paths |
| `DEAD_PATH_PIN` | re-measured after the repair |
| the selftest | a directory-citation arm, both directions |

### Migration

Four ledger rows are edited. The ledger is mutable by design and this is the edit it is for.

### Rollout

One commit: the harvest, the false-positive census, the four repairs, the re-measured pin, the arm.

### Files touched (estimate)

`tools/memory-tree/corpus_ids.py`, `memory/project/in-flight/a.md`, `.memory-tree.conf`.

### Alternatives rejected

- **Register the four instead of repairing them.** Rejected: a registry row says "this citation
  cannot be fixed". These can, in one edit, and a registry that holds fixable rows stops meaning
  anything.
- **Widen the present-tense scope to `builds/`.** Rejected by S4. It would turn a shrink-only repair
  list into a permanent census of history, which no one can drain.
- **Accept any backticked token containing a slash.** Rejected by §3 with the upstream number.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — the candidate set grows; resolution is a set lookup and a prefix scan already
  present.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — a corpus with no citations is unchanged; the registry may be
  empty and that is a clean pass with an armed ratchet.
- observability — every finding names the citing file, its line and the cited path.
- risks — FALSE POSITIVES. A widened harvest that admits non-paths makes the gate permanently red on
  correct prose, which is why S7 lists the newly accepted tokens before the rule is trusted.
- testing + left-shift gates — a directory-citation arm in both directions.
- migration / rollback — one commit.
- user docs — `HYGIENE.template.md` check 15's wording gains the directory clause.

## 6. Acceptance criteria

- **AC1** — When the present-tense corpus cites a directory that does not resolve, check 15 fails
  naming the citing file, its line and the cited path.
- **AC2** — When it cites a directory that DOES resolve — a prefix of a tracked path — check 15 is
  silent, AND the same fixture with the directory removed reds. The silent half alone passes on the
  un-widened code, because an unharvested token is also silent; only the pair can tell "widened" from
  "not widened".
- **AC3** — When the four ledger citations are repointed at the flat paths, check 15 is silent about
  them and the registry stays empty.
- **AC4** — When the newly accepted token set is listed across the whole corpus, every member is
  either a repo path or covered by `DEAD_PATH_EXCLUDE`; anything else narrows the rule.
- **AC4b** — When a citation falls under a `DEAD_PATH_EXCLUDE` prefix, it is not classified, and
  removing that prefix from the conf makes it classified again — so the exclusion is visible and
  reversible rather than compiled in.
- **AC5** — When a citation lives in `builds/` or an append-only area, it is not classified, and the
  measured count of such citations is recorded in the build journal.
- **AC6** — When `DEAD_PATH_PIN` is re-measured, the conf carries the new number and the reason.
- **AC7** — When `corpus_ids.py --selftest` runs, the directory arm has a red and a green side and
  the pass line prints last.

## 7. Gates

`bash tools/run-gates.sh`; the `memory hygiene` and `corpus-ids selftest` legs carry this unit.

## 8. Open questions

none — the two forks below are RESOLVED (owner-ratified 2026-08-08); kept for the record.

- **Fork A — repair or register the four live citations.** RESOLVED (owner, 2026-08-08): repair. See
  S3; a registry of fixable rows is a registry nobody drains.
- **Fork B — does the widened harvest need a grandfather list?** Options: register everything it
  newly finds, or repair first and pin at the residue. RESOLVED (owner, 2026-08-08): repair first.
  The measurement says the live residue is four rows and all four are one edit each; pinning them
  would be creating debt to avoid five minutes of work.

## 9. Revision log

- rev-1 · 2026-08-08 · initial draft, written after measuring the census.
- rev-3 · 2026-08-08 · folded review 2: N6 pairs AC2's green arm with a red one over the same
  fixture, because the green half passes on the un-widened code; N11 corrects S8's justification,
  which was factually wrong about the resolution rule; N12 adds a tracked `.claude/` path to the
  fixture, without which both exclusion arms are vacuous.
- rev-2 · 2026-08-08 · folded the false-positive census into S7 and added S8. The widened harvest
  admits `.claude/worktrees/<name>` — a checkout location, not repo content — and no resolution
  rule can classify it node-independently, so the exclusion is a declared conf prefix list rather
  than a special case in code.

## 10. Reuse audit

One condition inside `corpus_ids.py`'s existing harvest, and nothing else in the module moves: the
resolution rule, the registry format, the four rules and the pin are all untouched. The arm goes into
the module's existing selftest in its existing shape. The repair edits a ledger file that is already
mutable and already the kit's own navigation surface. No new file, no new key beyond re-measuring one
that exists.
