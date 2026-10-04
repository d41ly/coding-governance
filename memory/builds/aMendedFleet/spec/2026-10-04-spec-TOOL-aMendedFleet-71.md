# TOOL-aMendedFleet-71 — one sweep gives every present-tense count in a code comment one of ANNOTATION-STYLE A4's three dispositions

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 71

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`memory/guides/ANNOTATION-STYLE.md` A3 says a code comment MUST NOT carry a present-tense count of
a live derived population, and A4 gives a number in a comment three safe dispositions: frozen by
its conditions, gated by a pin, or pointed at its owner. The tree still carries counts in none of
the three, such as the driver's "Five tracked specs produce the first row today" and "zero of 277
tracked specs disagree today", each wrong on the commit that changes the population and read by
nobody who would notice. The style guide records that a gate for this was designed and refused on
measurement, and the owner's ANNOTATION-STYLE ruling stands, so this unit is the one sweep the
report asks for: an instrument that lists the candidates, a recorded disposition for each, and the
comment edits that apply it.

## 2. Scope (IN)

- **S1** — THE INSTRUMENT. A census script in this build's `build/` folder, in the shape and with the
  test-path split of `aKeyedAnnotation`'s citation census, binding `**Serves:** journal
  TOOL-aMendedFleet-71`. It reads every tracked `*.sh`, `*.py`, `*.js` and extensionless hook under
  `tools/`, `skills/` and `.githooks/`, fixtures excluded. It folds consecutive line comments, and
  Python docstrings read through `ast`, into paragraphs, splits sentences after `.` or `;`, and
  reports a sentence as a CANDIDATE when it carries a COUNT and a PRESENT-TENSE marker and is not
  FROZEN:
  - a COUNT is a digit run not preceded by a word character, `-`, `.`, `#`, `§`, `/`, `$` or `{`,
    or one of the words zero to twenty, `none`, `every` or `no` before a noun;
  - a PRESENT-TENSE marker is `today`, `currently`, `now`, `at present`, `right now`, `live` or
    `tracked`;
  - FROZEN is a sentence carrying a date, a hex run of 7 to 40 characters, `node <tag>`, `PINNED`,
    `at review` or `at base`; `measured` alone does not freeze, since "measured today" is the defect.
  It prints every candidate as `<path>:<line>: <sentence>`, then every frozen near-miss, then the
  population sizes: files read, paragraphs read, candidates, near-misses, each split product and
  test. `--selftest` runs the predicate over literal strings, one candidate and one frozen
  near-miss per marker. Observed by AC1 and AC2.
- **S2** — THE DISPOSITIONS. A journal record beside the script lists every candidate the script
  prints at the pass's STARTING COMMIT, the tip the unit pass begins from, recorded with
  `git rev-parse HEAD` before its first edit. That is not base `7af5f564`: units ordered before this
  one edit files in the estimate below, unit 61 among them in `unattended.sh`, `lib-unattended.sh`
  and `adopt-unattended.sh`, and their new comments are part of the population the sweep owes. One row each: path and line, the sentence,
  and one of `FROZEN`, `POINTED`, `REWRITTEN` or `NOT-A-COUNT`, with the reason on every
  `NOT-A-COUNT` row. It opens with the starting commit's sha and the script's population line, so
  a short list is distinguishable from a dead walk. Observed by AC3.
- **S3** — THE EDITS. Each row not marked `NOT-A-COUNT` is applied to its comment:
  - `FROZEN` adds the sha and date of the commit that wrote the figure, read with `git log -L` on
    the line, and turns "today" into "when this was written";
  - `POINTED` names the file or command that derives the figure and leaves out the digits;
  - `REWRITTEN` keeps the reasoning and states it without the number.
  An edit to a `*.template.*` file is made there and reaches its render through the kit's own
  render step, never by hand. No edit changes a line outside a comment or a docstring. Observed by
  AC4, AC5 and AC6.
- **S4** — The two sentences the report names, in `tools/unattended/unattended.sh` near lines 4017
  and 4021 at base, are among the applied rows; the pass finds them by text, since unit 61 edits
  that file first and moves its line numbers. Observed by AC4.

## 3. Non-goals (OUT)

- A gate, a drift signal or a pin over comment counts. A1 records that one was designed and refused
  on measurement and the report's comment-share gate conflicts with the A1-A2 ruling; the census
  script is a research instrument, run by hand.
- Prose outside code: kit READMEs, guides, records and dossiers. Dossier prose is unit 44's; the
  charter's derived-count rule already binds the rest.
- Counts in string literals, refusal messages and test assertions. They are behaviour, and a
  changed message is a different unit.
- Comment rewrites beyond the candidate sentence. A paragraph around a candidate is left as it is.
- The kit version bumps every touched kit owes, owed once at the close after the build's last move.

### Edges

- **hands-off** external — the kit version bumps for every kit whose shipped bytes the sweep moves,
  owed once at the close.

## 4. Design

### Evidence

Read at base `7af5f564`, re-verified 2026-10-04 at `efc4b0c9`, whose `tools/`, `skills/` and
`.githooks/` bytes equal base.

- The report's two examples moved by two lines: "Five tracked specs produce the first row today and
  ZERO produce the second" opens at `tools/unattended/unattended.sh` line 4017, and "zero of 277
  tracked specs" wraps from line 4021 to "disagree today" on line 4022. A line-wise grep misses the
  second, which is why S1 folds paragraphs.
- A trial line-wise predicate, digits or number words with a present-tense marker within 50
  characters and no date, sha or `measured`, matched 195 comment lines in 70 tracked files
  on 2026-10-04, PINNED. A read of its `today` subset found the true shape in about fifteen of
  them, among them `unattended.sh` line 8023 ("Two of 307 tracked CLOSED specs grade THIN today"),
  `check-unattended.sh` line 2399 ("every record in this tree today"), `govkit/matrix.py` line 196
  ("none does today") and `row_grammar.py` line 1526 ("empty on every real row today"). The rest
  were behaviour words such as "today's path". The census decides the set; this estimate does not.
- The quantified claims, `every`, `none` and `zero`, are the same defect as a digit: a present-tense
  statement about a population that moves.
- `memory/builds/aKeyedAnnotation/build/2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py`
  is a census of code comments with a product-versus-test split and a liveness rule of printing
  every population with its size. S1 copies that shape; its predicate is about ids, not counts.

### Inventory

- The census script's functions `read_comment_blocks`, `derive_candidates`, `check_frozen` and
  `main`, each leading with a verb this tree already uses; the lexicon leg grades a `.py` in a
  build folder like any other.

### Files touched (estimate)

The census decides the set; these are the files the trial read found a probable true hit in. A
file the census adds outside this list is added here, with its owed legs in §7, by a rev bump
before it is edited.

- `tools/unattended/unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/adopt-unattended.sh`
- `tools/govkit/govkit.py`
- `tools/govkit/matrix.py`
- `tools/memory-tree/row_grammar.py`
- `tools/memory-tree/merge-rows.py`
- `tools/memory-recall/test_recall_floor.py`
- `tools/drift-audit/drift_report.py`
- `tools/lib/resolve-python.test.sh`
- `tools/run-gates/run-gates.runlog.test.sh`

### Rollout

Comment-only. A touched file that the kickoff manifest's `watch:` line names owes that manifest's
re-stamp in the same commit, per the Definition of Done; none in the estimate is watched.

### Alternatives rejected

- **A gate.** Refused on measurement in the build that wrote the style guide, and the owner's ruling
  stands; a sweep with a recorded instrument is what remains.
- **Line-wise grep as the instrument.** It misses every count that wraps, the report's own second
  example among them.
- **Freezing every candidate.** A count whose owner is a file, a manifest row or a command is better
  pointed than dated: a dated figure is honest and still useless to the next reader.

## 5. Production-readiness checklist

- security — N/A — comment text only.
- perf / scale — the instrument reads the code population once, in seconds.
- error / empty / loading states — the instrument prints its population sizes, so a walk that read
  nothing is not a clean result.
- observability — the dispositions record is the observable result.
- risks — a gate that reads comment prose would red; AC6 looks for any reader of each edited
  sentence before the edit lands.
- testing — AC1 to AC6 directly; no suite arm, since the instrument is a research record.
- migration — N/A — no stored state.
- user docs — N/A — no behaviour changes.

## 6. Acceptance criteria

- **AC1** — When the census script runs with `--selftest`, it reports each literal candidate as a
  candidate and each literal frozen sentence as a near-miss, and exits 0.
  Red when: a frozen sentence is reported as a candidate, or a candidate is missed.
- **AC2** — When the census script runs in a `git clone --local` checked out at the pass's starting
  commit S2 records, under a short `%TEMP%` path, its candidates include both sentences of
  `tools/unattended/unattended.sh` S4 names, the wrapped one included, and its population line names
  more than zero files of each kind.
  Red when: the walk reads nothing, or the wrapped count is missed.
  figure: every count is DERIVED at observation time.
  fixture: both sentences are present at base; a sibling unit that rewrites either before this pass
  leaves that half unobservable, and the dispositions record says so.
- **AC3** — When the dispositions record is read, every candidate the AC2 run printed has exactly one
  row, joined on path and line, and every `NOT-A-COUNT` row carries a reason.
  Red when: a candidate has no disposition.
- **AC4** — When the census script runs at the tip, every candidate it prints carries a
  `NOT-A-COUNT` row in the dispositions record, joined on path and sentence text since the edits
  move line numbers, and neither S4 sentence is among them.
  Red when: an applied disposition left its count in place.
- **AC5** — When `git diff <starting-commit> -- <every file the sweep touched>`, with the sha S2
  records, is filtered with `grep` to changed lines that are not blank and not a comment or
  docstring line, it prints nothing; and for every `*.template.*` pair touched, the `diff` of
  template and render prints at the tip what it printed at that starting commit.
  Red when: the sweep moved behaviour, or a render was edited by hand.
- **AC6** — When, for each edited sentence, `git grep -F` of a distinctive six-word fragment of its
  base wording runs over the tree at base, the only hit is the edited file itself, and that check
  is recorded in the sentence's row.
  Red when: a gate or a test reads the comment text the sweep changed.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `row-keyed merge driver replay` · `row-grammar selftest` · `memory-recall kit selftest` · `recall floor` · `recall floor arms` · `drift-audit selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `run-gates run-log line` · `lexicon naming predicates` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

The held self-test legs above are owed by the guards the estimate trips and run once, at the close.

## 8. Open questions

- **F1 — Do test files belong to the sweep?**
  Options: product source only; product and test source. A3 binds every comment, and a stale count in
  a suite misleads the reader who edits it next; the cost is held suites at the close, which run there
  regardless.
  RESOLVED (agent, 2026-10-04, delegated): both, split in the census output, per S1.
- **F2 — How is a FROZEN figure dated?**
  Options: the date the sweep runs; the commit that wrote the figure. The first claims a measurement
  nobody made.
  RESOLVED (agent, 2026-10-04, delegated): the writing commit, read with `git log -L`, per S3.
- **F3 — Is a quantifier a count?**
  Options: digits and number words only; those plus `every`, `none` and `no` before a noun. A
  present-tense "none does today" goes stale the same way a digit does.
  RESOLVED (agent, 2026-10-04, delegated): quantifiers count, per S1.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the style guide, a trial predicate over the tracked code
  population at base, and a read of its `today` subset.
- rev-2 · 2026-10-04 · S2 · S4 · AC2 · AC5 · M2 cross-read: the census, its dispositions and the
  behaviour diff were anchored at base `7af5f564`, but unit 61 and other units ordered first edit
  files in this sweep, so a base diff reds on their code and a tip census finds their new comments
  with no row; all three now anchor at the pass's starting commit, which S2 records.

## 10. Reuse audit

The seam reused is the shape of
`memory/builds/aKeyedAnnotation/build/2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py`:
a build-folder census over tracked code comments, with its test-path split and its liveness rule.
Its predicate is about ids, so S1 writes its own. `python tools/codebase-map/reuse_lookup.py "find
present-tense counts of a moving population written in code comments"` returned name-stem neighbours,
`population` in the govkit refusal join and `derive_count` in runlog's record among them, none a
comment reader; it reports `unscanned layers: .sh`, so the shell half was a direct grep, the trial
predicate in §4. Unit 44's `measure_typed_counts` reads dossier prose against inventory nouns and
does not fit code comments, whose nouns are open. Recall returned `ANNOTATION-STYLE.md` A4 and the
`aKeyedAnnotation` design pass, which own the rule and its three dispositions, and three review
findings of this exact defect, `aMeteredTurnstile`'s "FOUR gate legs" comment above five rows among
them, which is why S3 prefers POINTED. Where the report and the tree disagree: the report's line
4023 is now 4021 to 4022, and its example wraps.

Recall terms used: `python tools/memory-recall/query.py "which rule bans a present-tense count in a
code comment and was a gate for it refused" --terms "ANNOTATION-STYLE A4 present-tense count comment
FROZEN GATED POINTED derived population prose number comment-share gate"`
