# TOOL-aFoldedQuarry-5 — U3: one id grammar, one walk, every consumer

**Status:** CLOSED · rev-3 · 2026-08-08 · node a · Tier-2 · base 42c3f4dc · streams tooling · ratified 2026-08-08

## 1. Goal

Give the kit a single classifier for the corpus's ids and repo-path citations, so every number a gate
quotes is DERIVED from one walk rather than written into a document. A classifier that lives in prose
is a classifier nobody can check.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/corpus_ids.py` builds, in ONE walk over the tracked corpus:
  `definitions(id -> defining paths)`, `citations(id -> mentioning paths)`, and
  `dead_paths((citing-file, cited-path) -> count, first line)` for rooted repo-path citations that
  resolve to nothing.
- **S2** — it declares NO id grammar and NO anchor pattern. `tools/memory-recall/extract.py` already
  owns `ID`, `ID_RE` and the four anchor shapes, all derived from `.memory-tree.conf`; this module
  imports them. A second grammar is the cross-language catalogue-drift class. That import is a
  DECLARED cross-kit dependency, and its two states are kept apart: with every pin blank the module
  is never imported and checks 13-16 are simply off, while a pin SET with the grammar module absent
  is a NAMED error — you armed a check whose grammar is not installed. Never a traceback, and never
  the silent pass a bare `try: import` would produce.
- **S3** — it declares NO append-only set and NO index set either. Both already exist inside
  `check-memory-hygiene.sh`, so the shell gains two PRINT modes (`--print-append-only-ere` and
  `--print-index-set`) that emit them and exit, and this module asks the shell. The dependency runs
  one way only, so there is no recursion: the print modes return before check 1.
- **S4** — check 13, id-definition uniqueness: an id defined by two different anchors is a
  collision, named with both paths.
- **S5** — check 14, orphan ids: an id CITED but never DEFINED fails unless its exact id is listed
  in `<MEMORY_ROOT>/project/id-orphan-waiver.txt`. The waiver carries a shrink-only PIN and a
  stale-entry guard — a waived id that now resolves is a stale row and reds.
- **S6** — check 15, dead repo-path citations, with the registry
  `<MEMORY_ROOT>/project/corpus-path-unresolved.txt` and FOUR rules:
  1. SET EQUALITY between the registry and the measured dead set, keyed on
     `(citing-file, cited-path)` with an occurrence COUNT — never on a line number. A line number
     moves whenever anything above the citation is edited, so a line-keyed registry reds on edits
     that have nothing to do with it, and a gate whose steady state is red gets bypassed. The line
     is still REPORTED for whoever repairs the row; it is not part of the identity. Repointing a
     citation while its row survives reds, and so does a new dead citation with no row.
  2. A shrink-only PIN: the registry may never hold more rows than `DEAD_PATH_PIN`.
  3. No duplicate rows for one `(citing-file, cited-path)` key.
  4. A row that declares a repair destination needs that destination to be a tracked FILE — not a
     directory, not absent.
- **S7** — check 16, read-path accounting: the set of files the charter points a session at is
  DERIVED from the charter's own text through three independent token arms, never enumerated. The
  charter is `.memory-tree.conf`'s `CHARTER` key, default `AGENTS.md` — a hardcoded filename makes
  this check silently empty in most adopting repos, and silently empty is the failure mode that
  looks like a pass; a configured charter that does not exist is a named error. Its total size must
  stay under `READ_PATH_CEILING`, which is the MEASURED total plus a stated headroom, both recorded
  in the journal (one-sided: shrinking never reds). Every member must either be under a byte cap
  already (the shell's own index set, asked for, not transcribed) or be listed in
  `READ_PATH_WAIVER` — a charter citation that nothing watches is the rule-3 case. A member that is
  tracked but absent from the worktree is SKIPPED with a note: check 12 already reports that state
  directly, and a second symptom of one cause is noise.
- **S8** — every PIN and CEILING is MEASURED against THIS repo's corpus by
  `adopt-memory-tree.sh --measure`, written into `.memory-tree.conf`, and never inherited. Blank
  means the check is disabled, matching the kit's existing disabled-when-blank contract. The
  MEASUREMENT ITSELF is a deliverable of this unit, not a by-product: if a check's whole population
  turns out to be waived — plausible for check 14, since this corpus's decision log carries ids that
  have no build folder by construction — the journal says so and the pin stays blank, rather than
  shipping a check with no signal.
- **S9** — `--report` prints the derived numbers; `--check <name>` is the gate; `--selftest` runs
  fixtures. Checks 13–16 ride `check-memory-hygiene.sh` so the merge bar has one hygiene leg.

## 3. Non-goals (OUT)

- inCMS's measured numbers. Every pin here is this corpus's own measurement; a pin copied from a
  larger tree is either vacuous or permanently red.
- `landing_map` and the commit-provenance half of the upstream module. Nothing in this kit consumes
  it, and a walk nobody reads is a walk that rots.
- Repairing anything. This unit MEASURES and REGISTERS; a repair is a separate, deliberate edit.
- A loose "backticked token with a slash" path class. Upstream measured that finding 13 085 dead
  citations whose top hits were package specifiers and git refs. Only paths rooted at a real
  top-level directory are classified.

## 4. Design

### Data model

```
definitions : id  -> [path, …]        an anchor, or an H1 inside spec/ or reviews/
citations   : id  -> [path, …]        any ID_RE match
dead_paths  : (file, cited) -> (count, first-line)   rooted, present-tense, resolves to nothing
read_set    : [path]                  derived from the charter's own text, three arms
```

The PRESENT-tense corpus is where a citation is a claim about NOW: the root indexes, the backlog
shards, the generated index, and `project/`. `builds/` is a record of a moment — a spec proposing to
write a file is a plan, not a broken pointer — and the append-only areas cannot legally be repaired,
so neither is classified.

### Inventory

| Constant | Home | Why there |
|---|---|---|
| `ID`, `ID_RE`, anchor shapes | `tools/memory-recall/extract.py` | already conf-derived; imported |
| append-only ERE | `check-memory-hygiene.sh` | check 2 already owns it; printed on demand |
| index set (the byte-capped files) | `check-memory-hygiene.sh` | check 6 already owns it; printed on demand |
| `DEAD_PATH_PIN`, `ORPHAN_ID_PIN`, `READ_PATH_CEILING` | `.memory-tree.conf` | measured per corpus |

### Migration

The two registry files are created empty by `adopt-memory-tree.sh` and populated by
`--measure`. This repo's first measurement is taken as part of this unit, and the resulting counts
are what the pins are set to.

### Rollout

One commit: the module, the two shell print modes, the four checks, the two registries, the measured
pins, and the self-test.

### Files touched (estimate)

One new module, the hygiene gate, the scaffolder, `.memory-tree.conf`, two new registry files, the
gate-leg manifest, and the two kit documents.

### Alternatives rejected

- **Transcribe the index set into Python.** Rejected: upstream did exactly this and had to guard the
  transcription in both directions with a parity arm, because a shell-side change the Python side
  still excludes leaves a file under no cap at all. Asking the shell removes the class.
- **Define the id grammar here.** Rejected by S2 — it is the catalogue-drift class, and upstream
  re-typed one alternation with its branches reordered and would never have noticed.

## 5. Production-readiness checklist

- security — N/A. Reads tracked text; the only subprocess calls are `git` and the sibling gate.
- perf / scale — one walk, one read per tracked file. The shell is asked twice per run, not per file.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — an empty corpus, an empty registry and a blank pin are all clean
  passes. A missing sibling script is a named error, not a traceback.
- observability — every failure names the id or the `(file, line, path)` and the rule number.
- risks — the registries are authored data that the gate compares against a measurement; a wrong
  measurement makes them permanently red. That is why S8 measures rather than inherits.
- testing + left-shift gates — `--selftest` fixtures for each rule, red and green.
- migration / rollback — one commit; the registries are new files.
- user docs — `HYGIENE.template.md` gains checks 13–16.

## 6. Acceptance criteria

- **AC1** — When two anchors define one id, check 13 fails naming the id and both paths.
- **AC2** — When an id is cited and never defined, check 14 fails; when that id is in the waiver, it
  passes; when a waived id later resolves, check 14 fails naming the stale waiver row.
- **AC3** — When a present-tense citation names a path that does not exist, check 15 rule 1 fails
  unless the registry holds that exact row; and when the source is repaired while the row remains,
  rule 1 fails naming the stale row.
- **AC4** — When the registry holds more rows than `DEAD_PATH_PIN`, rule 2 fails with both numbers.
- **AC5** — When a registry row declares a destination that is a directory or is untracked, rule 4
  fails naming it.
- **AC6** — When a file the charter points at is under no byte cap and not waived, check 16 fails
  naming it; when the read set exceeds `READ_PATH_CEILING`, check 16 fails with both numbers;
  shrinking below never fails.
- **AC7** — When `.memory-tree.conf` leaves a pin blank, its check is silently skipped, matching
  `SPEC_FORMAT_CUTOFF`.
- **AC8** — When `python tools/memory-tree/corpus_ids.py --selftest` runs, every rule above has a red
  and a green arm and the pass line prints last.

## 7. Gates

`bash tools/run-gates.sh` in full. Checks 13–16 ride `check-memory-hygiene.sh`; a new leg runs
`corpus_ids.py --selftest`.

## 8. Open questions

none — the two forks below are RESOLVED (owner-ratified 2026-08-08); kept for the record.

- **Fork A — where the append-only and index sets live.** Options: a second definition in Python, or
  print modes on the shell. RESOLVED (owner, 2026-08-08): print modes. A transcription needs a parity
  guard in both directions and still leaves the failure mode where the shell adds a path the Python
  side excludes; asking removes the class rather than guarding it.
- **Fork B — what the pins are set to.** Options: inherit upstream's, or measure. RESOLVED
  (owner, 2026-08-08): measure, and record the measurement in the build journal so the next raise or
  lower is an argument against a number rather than a guess.

## 9. Revision log

- rev-1 · 2026-08-08 · initial draft.
- rev-2 · 2026-08-08 · folded review 4: H1 re-keys the dead-path registry off line numbers, which
  would have made the gate red on unrelated edits; H2 declares the cross-kit grammar dependency and
  splits its two states; H3 adds the `CHARTER` conf key; H4 makes the measurement a deliverable and
  allows a blank pin as the honest outcome; H5 pins the ceiling's headroom to a recorded number;
  H6 skips a tracked-but-absent read-path member.
- rev-3 · 2026-08-08 · folded three findings that only MEASUREMENT produced, all recorded in the
  build journal: check 13 tests "claimed by two BUILD FOLDERS", not "defined twice" (a decision-log
  row and its spec's H1 anchor the same id by design, and the first reading would have redded ten
  ids on day one); check 16's read path is scoped to `MEMORY_ROOT`, because the charter also names
  every gate script it runs and folding those in made the population 32 files of which 30 needed
  waiving; and the corpus measurement itself — 29 defined, 33 cited, 4 orphans, 0 collisions,
  0 dead paths, a 3670 B read path — is what the pins are set from.

## 10. Reuse audit

This unit is mostly a wiring exercise, and that is the point. The id grammar and the four anchor
shapes come from `tools/memory-recall/extract.py`, which already derives them from
`.memory-tree.conf`; nothing is re-typed. The append-only set and the byte-capped index set come from
`check-memory-hygiene.sh`, which already owns both — the two new print modes are the seam rather than
a copy. The checks ride the existing `fail` protocol and the existing disabled-when-blank conf
contract. The gate leg registers in `tools/gate-legs.json`. The only genuinely new artifacts are the
two registry files and their rules, and both are modelled on the kit's existing grandfather lists
(`legacy-files.txt`, `curation-debt.txt`) down to the stale-entry guard those already carry.
