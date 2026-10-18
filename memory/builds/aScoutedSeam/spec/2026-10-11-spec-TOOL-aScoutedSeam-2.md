# TOOL-aScoutedSeam-2 — a spec's §10 names every MUST seam its brief carries, or overrides it with a reason, and check 12 grades it

**Status:** SPECCED · rev-2 · 2026-10-18 · node a · Tier-2 · base d19938f3 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aScoutedSeam-1-1-failure-analysis.md](../build/2026-10-11-build-TOOL-aScoutedSeam-1-1-failure-analysis.md) | research | TOOL-aScoutedSeam-1 TOOL-aScoutedSeam-3 KICK-aScoutedSeam-1 DEPL-aScoutedSeam-1 |
| [2026-10-18-prompt-DEPL-aScoutedSeam-1-brief.md](../prompts/2026-10-18-prompt-DEPL-aScoutedSeam-1-brief.md) | research | DEPL-aScoutedSeam-1 KICK-aScoutedSeam-1 TOOL-aScoutedSeam-1 TOOL-aScoutedSeam-3 |

<!-- /gen:spec-records -->

## 1. Goal

Make a scout's MUST seam impossible to drop silently between orientation and the spec. Today check 12
grades §10 on shape, and "a citation naming the wrong seam satisfies it". The failure analysis
measured the cost: two NicoCares builds had the shared card generator surfaced and named in a
dossier, and both forked a second card. This unit joins the brief's MUST lines to the build's specs:
each one is cited by some spec's §10, or overridden there with a stated reason.

## 2. Scope (IN)

- **S1** — The join. A build qualifies when it holds a brief whose `## The brief` / `### Reuse`
  carries at least one line of `TOOL-aScoutedSeam-1`'s MUST grammar. Once any spec in a qualifying
  build is at `SPECCED` or later, each MUST line's path must be resolved by the build's non-terminal
  Tier-2 specs taken together. Resolved means it appears backticked in some spec's §10, or that spec's
  §10 carries `- reuse-override <path> — <reason>`. The join is by SET, as `BUILD-METHOD.md` M5 says
  the reuse obligation is met once for the set.
  - AC1 observes it.
- **S2** — An override line with an empty reason, or one naming a path no MUST line carries, is its
  own finding, named by the line.
  - AC2 observes it.
- **S3** — Triggered by the GRAMMAR, with no cutoff key. A brief whose `### Reuse` holds free prose,
  the shape every brief before the scout has, never qualifies, so no landed build reds.
  - AC3 observes it.
- **S4** — The §10 probe half of check 12 gains a third satisfier: a citation of the reuse scout's
  run, the phrase `reuse scout` beside the brief's path. A spec built on the scout's seams no longer
  needs a lookup citation it would only write to satisfy the gate. The terms half is unchanged.
  - AC4 observes it.
- **S5** — Liveness: every hygiene run prints one line naming how many builds the join graded and how
  many MUST lines it read, so a join over nothing reports zero instead of reading as clean.
  - AC5 observes it.
- **S6** — The prose that states the rule, each edited in its template and re-rendered:
  - the §10 rules in the spec template;
  - M5 of the build method;
  - item 12 of the hygiene catalogue.
  - AC4 observes it.

## 3. Non-goals (OUT)

- Grading that the cited seam is TRUE or that the build used it: the diff mode's job
  (`TOOL-aScoutedSeam-3`).
- Per-spec joins. Not every unit of a build serves every seam, so a spec-by-spec rule would force
  pasted citations.
- A new `.memory-tree.conf` cutoff key. The trigger is the grammar's presence (S3), so nothing
  retroactive needs fencing.
- Grading SHOULD lines. A SHOULD is overridable by definition and the brief already records it.

### Edges

- **consumes-from** `KICK-aScoutedSeam-1` — the brief's `### Reuse` lines in the scout's grammar;
  without them no build qualifies and the join grades nothing.
- **consumes-from** `TOOL-aScoutedSeam-1` — the MUST line grammar this join parses.
- **hands-off** external — aOrientedCast names this check in the `reuse` workflow row's `enforced-by`.

## 4. Design

### The join, step by step

1. Select the briefs: tracked files under a build's `prompts/` whose name ends `-brief.md` or
   `-brief-<n>.md`, the names aRoutedQuill's `BRIEF_SKELETON` prescribes.
2. Parse the `### Reuse` block under `## The brief`, up to the next `###` or `##`. Keep the lines
   matching `^- MUST [^:]+:(\S+) :: `; the captured path is the key.
3. If the build has no spec at `SPECCED` or later, report nothing for it.
4. Collect the §10 of every non-terminal Tier-2 spec in the build, found by heading TEXT, the way
   check 12 already finds its sections.
5. A key is resolved when it appears inside backticks in any collected §10, or when some §10 carries
   an override line naming it with a non-empty reason.
6. Print one finding per unresolved key, naming the brief, the path and the specs read.

### Placement

The join is a delegated Python module, `tools/memory-tree/reuse_join.py`, invoked from the check-12
block in both full and `--staged` mode and reporting as check 12. Checks 13 to 19 are delegated the
same way. The population is the qualifying builds only, so the staged leg stays cheap; the measured
lesson of check 23 is that a join over every build is not.

### Inventory

| identifier | cell |
|---|---|
| `reuse_join.py` | py.module |
| `parse_reuse_block`, `check_build_join`, `scan_briefs`, `main` | py.function |
| `MUST_LINE_RE`, `OVERRIDE_LINE_RE` | py.constant |

### Files touched (estimate)

- `tools/memory-tree/reuse_join.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/HYGIENE.template.md`
- `tools/memory-tree/SPEC-TEMPLATE.template.md`
- `tools/memory-tree/BUILD-METHOD.template.md`
- `tools/memory-tree/check-verdict-epoch.sh`
- `memory/HYGIENE.md`
- `memory/TEMPLATE-SPEC.md`
- `memory/guides/BUILD-METHOD.md`
- `memory/map/generated/symbols.json`

### Rollout

Live from landing, and it binds only a build whose brief carries the scout's MUST grammar, which no
landed build has. The first build to opt in is the first one graded.

### Alternatives rejected

- **An awk arm inside check 12's program.** The join spans files, a brief and a spec set, and the
  awk program reads one spec at a time.
- **Grading in `tools/check-spec-tokens.py`.** That checker is gov's root tool and does not ship, so
  adopters, where the measured reinventions happened, would not get the rule.
- **A hook at spec write.** A spec is written in several passes; the set is only complete at commit.

## 5. Production-readiness checklist

- security: N/A — reads tracked markdown only, no write path.
- perf / scale: the population is qualifying builds only, and the staged leg selects the staged
  builds.
- error / empty / loading states: a brief with an unparseable `### Reuse` is reported, not skipped,
  and a join over zero builds says so (S5).
- observability: the liveness line on every run.
- risks: an author pastes every MUST path into one §10 to pass the gate. The diff mode, not this
  join, sees whether the seam was used.
- testing: the hygiene suite gains fixture builds for each arm, and the module carries `--selftest`
  scratch trees for its own arms.
- migration: N/A — no landed brief qualifies.
- user docs: the hygiene catalogue item 12 and the spec template's §10 rules.

## 6. Acceptance criteria

- **AC1** — When a fixture build's brief carries two MUST lines and its one SPECCED spec's §10
  backticks only the first path, `reuse_join.py` reports the second path, the brief and the spec.
  Red when: the join reads the whole spec instead of its §10, so a mention in §4 passes.
- **AC2** — When the §10 carries `- reuse-override <path> — ` with an empty reason, `reuse_join.py`
  names the override line; with a reason the build passes.
  Red when: an empty reason resolves the key.
- **AC3** — When a fixture brief's `### Reuse` holds free prose, `reuse_join.py` grades zero builds
  and its liveness line says `0 build(s)`.
  Red when: prose that mentions a MUST word qualifies the build.
- **AC4** — When a §10 says `reuse scout` beside its brief's path and carries a terms line,
  `check-memory-hygiene.sh` reports no §10 finding for that spec.
  Red when: the probe half still demands a lookup citation.
- **AC5** — When the join grades one qualifying build, the hygiene run prints `reuse join: 1 build(s),
  2 MUST line(s)`.
  Red when: the line is printed only on a finding.

## 7. Gates

`memory hygiene` · `kit/dogfood doc parity` · `verdict epoch (kit version dates the engine)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `method carriers (every pointer declared)` · `recall floor` · `recall floor arms`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC2 AC3 AC4 AC5 · fixture builds with briefs and specs staged per arm · none

## 8. Open questions

- **F1 — Should an override need the owner's word, or is the spec author's reason enough?** The spec
  is approved by the owner before a build starts, so the reason is read at that approval.
  Recommendation: the author's reason, read at approval; no separate owner mark.
  RESOLVED (owner, 2026-10-18): the author's reason, read at approval, as recommended.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-18 · §8 · F1 closed as recommended. No S, AC or gate moved.

## 10. Reuse audit

The seam this unit extends is check 12 in `tools/memory-tree/check-memory-hygiene.sh`, with the
delegation shape of checks 13 to 19 and the brief naming from `BRIEF_SKELETON` in
`skills/session-kickoff/manifest-check.sh`. The heading-text section finder is check 12's own.
`tools/codebase-map/reuse_lookup.py "check that a spec section names every line a sibling record
lists, or carries an override with a reason"` ranked `check`, `records` and `check_line` by stem.
`check_line` validates run-log lines and does not fit, so no existing seam fits beyond check 12's own
section reader.

Recall terms used: section 10 reuse audit check 12 brief Reuse sub-head MUST seam override join spec set
