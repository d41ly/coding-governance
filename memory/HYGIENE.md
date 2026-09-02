<!-- gov:kit memory-tree@2.57 -->
# memory/ retention & hygiene

`memory/` is the project's AI-first memory: version-controlled, travelling to every node on clone.
It holds one append-only decision log, per-build folders, the gate's own waiver registries, and
long-lived guides.
The tree is FLAT: the discipline is a SIGNAL, not a directory. Which discipline a build served is
declared in each spec's status header as `streams <value>[+<value>]`, over the closed enum your
repo-root `.memory-tree.conf` declares as `DISCIPLINES`. A build spanning two disciplines is one
build, in one folder.
This file is the rule set; the single mechanical enforcement is `tools/memory-tree/check-memory-hygiene.sh`
(run by CI, the pre-commit hook, and the local gate runner). Prose rules with no wiring rot — the
script is the law, this doc explains it. (Replace `memory/` throughout with your `MEMORY_ROOT` if you renamed it.)

## Structure

```
memory/
├── README.md              root index (one-liners)
├── LIVE.md                GENERATED — builds with a non-terminal unit (tools/memory-tree/gen_build_index.py)
├── ledger/<YYYY-MM>.md    GENERATED — one row per build opened that month; freezes when the month passes
├── HYGIENE.md             this file
├── TEMPLATE-SPEC.md       the canonical spec/design-pass format (check 12; ships with the kit)
├── DECISIONS.md           append-only decision index, EVERY family, grouped for reading
├── backlog/<FAMILY>.md    mutable backlog, one shard per id family (status-vocabulary rows)
├── decisions/             decision detail (append-only area files)
├── guides/                long-lived reference guides
├── archive/               rotated indexes + legacy material a build can't claim
├── project/               the gate's own waiver registries (`*.txt`) and nothing else
└── builds/<slug>/
    ├── README.md                   (the build's entry point; mostly generated)
    ├── RUN.md                      run-state for an UNATTENDED run; only when one is/was live
    └── prompts/ · spec/ · build/ · reviews/   (<date>-<kind>[-<FAMILY>]-<slug>-<seq>.md)
```

`<FAMILY>` is a stream's id family from `.memory-tree.conf` (`architecture:ARCH …`). A build folder is
named for its SLUG alone — no date, no family. A recording filename MAY carry the family as an
optional qualifier, which is how one slug shared by two families survives in a single folder.
Ceremony is conditional: subfolders exist only when non-empty; a single-file build is one spec file
plus its backlog row — no README. Non-markdown artifacts (scripts, data) are legal only inside
`builds/*/build/`, `guides/`, and `archive/`.

## Rules

1. **Prompt placement (structural).** Prompt-kind files are sanctioned ONLY under `builds/*/prompts/`
   or `archive/`. A scratch planning-prompt committed elsewhere is a regression.
2. **No instance-specific / secret content** in core memory — scrub throwaway dev creds before mirroring a note.
3. **Archive-or-file on landing.** DECISIONS.md is the durable home. Delete cold scratch notes; file a
   feature's plan/review writeups into its `builds/` folder; a file's own "NOT merged" status prose rots.
4. **No broken relative links** outside the append-only log (`DECISIONS.md`, `decisions/`), `archive/`
   (dead pointers allowed by design), and migrated recording files listed in `legacy-files.txt`. The
   generated index files are NOT exempt: their rows link to build READMEs, and a link that stops
   resolving is exactly the drift they exist to prevent.
5. **A check never selects an empty population.** A path selector that matches nothing prints nothing,
   and nothing is what a passing check prints. Every selector over a population a real tree has
   asserts it is non-empty, so a mis-segmented path fails loudly instead of disarming its check.

## Index budgets, caps, rotation

- **Entry budget:** every entry in an index (`DECISIONS.md`, `backlog/<FAMILY>.md`,
  `LIVE.md`, `ledger/<month>.md`, root `README.md` lists) is ONE physical line, ≤
  `ENTRY_CAP_CHARS` (300 by default); a build `README.md` gets its own tier,
  `BUILD_README_ENTRY_CAP_CHARS` (350). Both are declared in `.memory-tree.conf`. Detail
  lives in the build folder or decision file the line points at. `guides/*.md` is exempt from the
  entry budget — a guide is prose, not index rows — and still carries the file caps below. That
  exemption is ONE expression with one base and one optional append for the codebase-map detail
  files; a second full spelling of it is how the `guides/` half went missing once.
- **File caps:** index and generated files are capped BY CLASS, and every cap is declared in
  `.memory-tree.conf` (`INDEX_CAP_*`, `GUIDE_CAP_*`, `BUILD_README_CAP_*`, `DOSSIER_CAP_*`). The shipped
  defaults are 20 KB / 250 lines for a row document, 60 KB / 750 lines for a guide, 25 KB with no line
  cap for a build README, and 20 KB with no line cap for a codebase-map dossier. `archive/` is wholly
  exempt. A LINE cap of 0 means no independent line cap for that class, which is how a project retires
  the line axis — this repo has, for row documents.
- **The live-row floor.** Because rotation carries forward every non-terminal row, a shard's floor is
  its live set: when nothing terminal is left, rotating is a no-op and the next row breaches the cap.
  So the number that actually bounds a shard is its LIVE ROW COUNT, and `drift-audit` reports that per
  shard on every run (`live_backlog_rows_per_shard`, report-only). `TOOL-aRelaxedShard-4`.
- **Rotation** (on cap breach): `git mv <INDEX>.md archive/<INDEX>.<YYYY-MM-DD>.md`; create a fresh index
  whose line 1 notes the rotation + the id range archived. BACKLOG rotation carries forward every
  non-CLOSED/non-WONTDO row. Rotated archives stay inside `memory/` so the all-time id collision grep still
  covers them. Rotation moves whole files — it never rewrites or renumbers a ratified record.

## Status vocabulary (backlogs)

Every backlog row leads with exactly one token of
`OPEN · SPECCED · INPROGRESS · BLOCKED · DEFERRED · CLOSED · WONTDO`, in its `·`/`|`/leading-dash slot
(a prose mention of one of these words elsewhere on the line does not count). New-entry dash form:
`- <id> · <STATUS> · <one-liner>[ → <pointer>]`.
Spec status headers (check 12) reuse the same seven tokens with spec-lifecycle meanings — see
`TEMPLATE-SPEC.md`.

## The grandfather ratchet

The plain lists in `memory/project/` — the whole of what that directory holds — read as exact-key
set membership rather than a `grep -qxF` per call, because that fork ran once per scanned file:
- **`legacy-files.txt`** — recording files kept under historical names (e.g. from a migration), permanently
  exempt from the recording-file naming check. Should not grow after the initial adoption.
- **`curation-debt.txt`** — index files pending slimming, exempt from the cap / entry-budget / status-vocabulary
  checks while listed. Every curation sweep deletes lines; empty = fully strict. CI fails if a listed path is gone.
- **`id-orphan-waiver.txt`** — ids cited but never defined, deliberately (check 14). Shrink-only
  against `ORPHAN_ID_PIN`, with a stale-entry guard: a waived id that now resolves reds.
- **`corpus-path-unresolved.txt`** — rooted repo-path citations that resolve to nothing (check 15),
  one TAB-separated row per `(citing-file, cited-path)`. Shrink-only against `DEAD_PATH_PIN`.
- **`unarmed-branches.txt`** — `fail` branches no assertion reaches (the harness meta-gate below).
  Shrink-only, and EMPTY is its working state rather than its retirement.
- `project/method-carriers.txt` — every file outside the memory tree that POINTS AT
  `guides/BUILD-METHOD.md`, one `<path> · <why>` row each, read by
  `check-method-carriers.sh`. Keyed on PATH alone, never `<path>:<line>`. It is per-repo and the kit
  ships none: an adopter's is scaffolded from their OWN measured population, because gov's rows would
  name paths their tree does not have.

MOST are scaffolded by `adopt-memory-tree.sh`, not all: a registry that arrives with the gate
that reads it is scaffolded by nothing. "Absent" and "present and empty" read identically
to every consumer, so a registry a gate names and nothing creates is invisible until the first row.

## The check catalog (all in `tools/memory-tree/check-memory-hygiene.sh`; this file is the prose home)

1. **prompt placement** — prompt-kind files only under `builds/*/prompts/` or `archive/`.
2. **link integrity** — every relative md link resolves (exempt: DECISIONS.md, `decisions/`, `archive/`,
   and `legacy-files.txt`-listed recordings). The generated index files are NOT exempt.
3. **structure lint** — the `memory/` root holds only the sanctioned set; `backlog/` holds only
   `<FAMILY>.md`; `builds/` holds only folders; `decisions/ guides/ archive/` contents are
   unconstrained; `project/` holds ONLY the waiver registries — no catch-all — and its selector
   carries rule 5's guard, so a mis-segmented `project/` path reds instead of admitting everything;
   `builds/` shape is check 4.
4. **build-folder naming** — `builds/*` is the SLUG alone, no date and no family prefix; inside a
   build folder only `README.md RUN.md prompts/ spec/ build/ reviews/` plus loose
   recording-named `.md`; non-md only in `build/`. `RUN.md` is the UNATTENDED run-state file: one
   generated region plus an authored one, present only while a run is or was live. It is capped by
   rule 6, exempt from rule 7 (the standing mandate is verbatim prose), and deliberately OUTSIDE
   rule 8 — a run phase is not a slot status, and no token in that vocabulary means "built and
   reviewed, not yet landed".
5. **recording-file naming** — files under the four subfolders, AT ANY DEPTH, match
   `<date>-<kind>[-<FAMILY>]-<slug>-<seq>[-<unit-tail>].md`. The kind comes from the SUBFOLDER, not
   from the file's immediate parent — `spec/units/x.md` is a spec. The family is the closed
   `FAMILIES` alternation and the optional unit tail is shared with check 12's selector, in one
   variable, because two hand-copied EREs for one grammar had already diverged (grandfather:
   `legacy-files.txt`).
6. **index size caps** — FOUR classes, because prose, rows, a generated surface and a map dossier
   fail for different reasons. Row
   documents ≤ `INDEX_CAP_BYTES` / `INDEX_CAP_LINES` (20 KB / 250 by default); `guides/*.md` ≤
   `GUIDE_CAP_BYTES` / `GUIDE_CAP_LINES` (60 KB / 750); a build `README.md` ≤
   `BUILD_README_CAP_BYTES` (25 KB) with `BUILD_README_CAP_LINES` at 0, which means NO independent
   line cap for that class; and a codebase-map dossier ≤ `DOSSIER_CAP_BYTES` (20 KB) with no line cap,
   reached only where a map is adopted and guarded on a non-empty prefix, because an unguarded selector
   would hand the dossier bound to the whole tree. A cap that is not a whole number, or a zero BYTE cap, is refused before
   any check runs: the gate exits 2 naming the key rather than reporting a tree it could not
   measure (grandfather:
   `curation-debt.txt` exempts either). A guide is MANDATORY reading the charter points a session at,
   and check 16 refuses a charter-cited file that nothing caps — but for a guide the LINE count is a
   proxy for the byte cap beside it. There is no longer a SUMMED read-path budget behind these:
   `READ_PATH_CEILING` was retired in 2.42, and these per-class caps ARE the bound a guide has.
   Entry-budget exempt (check 7's `ex7`) — a
   guide is prose, not index rows. `builds/*/RUN.md` is a ROW document on both counts: it is designed
   to GROW, so the cap is the bound the protocol spills against (oldest parked entries move to the
   build's own `build/` folder as a dated recording).

   **A row class may retire its line axis, and this repo has.** `TOOL-aRelaxedShard-1` declares
   `INDEX_CAP_LINES=0` after the owner ratified it, reversing what `TOOL-aWidenedGuide-1` refused. It
   was a decision, not a tidy-up: at check 7's 300-char entry budget a 250-line row document may hold
   75,000 B, so the byte figure decided every real case — but the line figure DID bind on 22 of the 29
   members, every dossier among them, which is why dossiers became their own class rather than
   inheriting the relaxed index cap.
7. **entry budget** — index entry lines ≤ `ENTRY_CAP_CHARS` (300 by default), a build `README.md`
   ≤ `BUILD_README_ENTRY_CAP_CHARS` (350) (grandfather: `curation-debt.txt`).
8. **status vocabulary** — `backlog/<FAMILY>.md` rows carry exactly one slot status token (grandfather: `curation-debt.txt`).
9. **build-index drift** — `tools/memory-tree/gen_build_index.py --check` must be clean. The index is
   DERIVED from each build's README front matter (`slug node opened streams roster ids [status]`, at
   column 0, opening at line 1) plus every `**Status:**` header under its `spec/`. A build with no
   README, an unpaired generated-region marker, or two answers to its own status is a NAMED error.
   Pin the generated files `eol=lf` in `.gitattributes` — the gate byte-compares them.
10. **rotation note** — every rotated `archive/<INDEX>.<date>.md` is referenced from lines 1–3 of its live index.
11. **old-tree tombstone** — if `.memory-tree.conf` sets `TOMBSTONE_ROOTS` (the tree you migrated FROM),
    the gate fails if that tree ever regains a tracked file. Blank = skipped (fresh-scaffold projects).
12. **spec format** — when `.memory-tree.conf` sets `SPEC_FORMAT_CUTOFF`, spec files dated ≥ it
    (any depth under `spec/`) carry the `**Status:**` header (token · rev · date · node · tier ·
    base sha); Tier-2 adds exactly the canonical `##` sections, non-empty bodies,
    header-rev-in-§9 parity — the §9 range CLOSES at the next `##`, so a bigger `rev-N` in §10 no
    longer satisfies the header — and a resolved §8 before CLOSED/WONTDO; both tiers reject skeleton
    placeholders and a bare WONTDO tail (`TEMPLATE-SPEC.md`). Older specs grandfathered by filename date.
    A `streams` segment is validated against the `DISCIPLINES` enum whenever present, on either tier,
    and is REQUIRED once the filename date reaches `STREAMS_CUTOFF`.
    Every acceptance bullet must name a witness in backticks once the filename date reaches
    `SPEC_WITNESS_CUTOFF`, on either tier. SHAPE only — that a bullet names something, never
    that the named thing exists.

13. **id-definition collision** — one id claimed by two different build folders. A decision-log row
    and its spec's H1 both anchor the same id BY DESIGN (the index points at the record), so
    "defined twice" is not the test; "claimed by two builds" is.
14. **orphan ids** — an id cited but never defined fails unless listed in
    `project/id-orphan-waiver.txt`, which carries a shrink-only pin (`ORPHAN_ID_PIN`) and a
    stale-entry guard: a waived id that now resolves is a stale row and reds.
15. **dead repo-path citations** — a rooted repo-path citation in the PRESENT-tense corpus that
    resolves to nothing must be registered in `project/corpus-path-unresolved.txt`. A DIRECTORY
    citation counts: it is exactly as broken when it does not resolve, and the flatten left four of
    them in the live ledger. `DEAD_PATH_EXCLUDE` names prefixes that are not repo CONTENT — a
    checkout location, say — because resolution never touches the filesystem and cannot tell meaning
    from existence. Four rules:
    (1) set equality between the registry and the measured set, keyed on `(citing-file, cited-path)`
    with an occurrence count and NEVER on a line number — a line number moves on unrelated edits and
    a gate whose steady state is red gets bypassed; (2) a shrink-only pin (`DEAD_PATH_PIN`);
    (3) no duplicate rows; (4) a `moved:<dest>` row needs `<dest>` to be a tracked FILE.
16. **read-path accounting** — the files `CHARTER` points a session at, under `MEMORY_ROOT`, derived
    from the charter's own text through three token arms. TWO rules, and NO byte budget: rule 3 is
    that every member is byte-capped by check 6 or listed in `READ_PATH_WAIVER`, because a charter
    citation nothing watches is a read budget nobody watches; rule 4 is that a cited file tracked but
    absent from the worktree is a finding, and it is the ONLY detector for that class — check 12's
    arm covers `builds/*/spec/*.md` alone and the index set drops absent files before check 6
    measures. The SUMMED budget `READ_PATH_CEILING` carried was retired in 2.42: check 6 already
    caps every member, so the sum was a second bound over an already-bounded population and it never
    once caused a trim. A conf still declaring `READ_PATH_CEILING` or `READ_PATH_HEADROOM` is
    ANNOUNCED and reds nothing.

Check 16 is STRUCTURAL: it runs whenever the conf is loadable, is behind no pin, and reaches neither
`walk()` nor the id grammar. It was behind a pin, and that was the defect — one blank line silenced a
citation check. Rules 3 and 4 REPORT without gating until the version named in `corpus_ids.py`'s
`READ_PATH_GATES_FROM`, so an adopter is not redded for a pre-existing condition on their first
upgraded bar; the grace announces itself on every run.

Checks 13-15 live in `tools/memory-tree/corpus_ids.py` and are DISABLED when their pins are blank.
Every pin is MEASURED against the adopting corpus (`corpus_ids.py --measure`), never inherited: a pin
copied from a larger tree is either vacuous or permanently red. The id grammar comes from the
memory-recall kit, so arming these checks requires that kit — with the pins blank it is never
imported, and with a pin set and the kit absent the failure is NAMED, not a traceback.

17. **catalogue index freshness** — `gotchas/INDEX.md` byte-matches a fresh render.
18. **a class declares its resolution** — every `kind: class` record names a gate or says in as many
    words that it has none. Silence is not acceptable: "no gate named" and "gate not yet written" are
    indistinguishable from outside, and the second one quietly never happens.
19. **the record can actually fire** — a class record derives at least one anchor or is marked
    `universal`, and a record whose anchors reach ONLY the append-only tree is reported as INERT:
    reachable on paper, dead in practice. The `universal` set is budgeted (`UNIVERSAL_BUDGET`)
    because every universal record is emitted on EVERY reviewer's checklist.

20. **one id, one row per document** — within a single row document (the decision index, a backlog
    shard, a rotated archive) an id appears at most once. The count of survivors is pinned
    shrink-only by `ROW_DUPLICATE_PIN`, and an UNDECLARED pin is a refusal, not a disabled check.
    Scope is PER FILE deliberately: corpus-wide would red every designed backlog-row-plus-decision-row
    pair. NAMED GAP — the live index and its rotated archive are two files, so a row that rotates out
    and is re-minted is not caught here; the all-time collision grep the index's own header
    prescribes covers that. Keyability is asserted alongside it, but only as the precondition that
    makes the uniqueness census meaningful: on its own it is a check the corpus cannot fail, over a
    property the merge driver already enforces where it can be violated.

21. **every record names the spec it is evidence about** — a build folder holds one spec per unit,
    and everything else in it (an adversarial review, a build ledger, a research report, a
    transcript) is a RECORD. Each carries one authored line in its head naming the spec ids it
    serves, so the binding is a fact rather than an inference from a filename ordinal. The rule, the
    grammar and the escape are below under "Record bindings". Delegated to `gen_build_index.py`,
    which already reads every record's bytes; the parse RAISES nothing, so an unannotated record can
    never refuse the render.

22. **review verdict vocabulary** — a review record whose filename date reaches
    `REVIEW_VERDICT_CUTOFF` carries exactly ONE `## Verdict:` line, and its token is a member of the
    closed set `CLEAN` / `CLEAN WITH FIXES` / `BLOCKED`. A trailing tally is not a member: the point is
    a token a machine can compare, and counts belong in the body. Deliberately NOT check 5, which is a
    recording FILENAME grammar, and NOT check 21, which asks which spec a record is evidence about — a
    verdict assertion under either number would make a structural check read as a semantic one to
    everybody who did not write it. Forward-only by the cutoff, because 45 of 111 tracked records
    carried no verdict at all when this landed and a landed review is not rewritten.
    **What it does NOT check:** whether the verdict is TRUE. It grades the token and never the
    judgement behind it, exactly as the acceptance-witness rule grades a backticked name and never the
    thing that name points at.

## Record bindings — how a record names its spec

Within the first 12 unfenced lines, optionally behind a comment marker so a non-markdown record can
carry it too:

```
**Serves:** <kind> <id> [<id> …]
**Serves:** none — <why this record serves no spec>
**Commissions:** <id> [<id> …]          (optional, for a record that PRODUCED specs)
```

- `<kind>` is closed: `spec-audit` (a pre-code pass over a spec) · `diff-review` (a pass over built
  code) · `journal` (evidence of what was built) · `research` (a report that precedes the specs).
  An open kind field stops being groupable the first time two authors spell one relation differently.
- `<id>` is family-qualified, so a record can name a spec in ANOTHER build — which real corpora need,
  because one closing review legitimately covers two builds. It may carry a trailing `@rev-N`, which
  is recorded and never validated, and a contiguous run may be written `N..M`, which EXPANDS at
  authoring time and therefore cannot rot when the build later gains a unit.
- Ids resolve against the set DEFINED BY A SPEC H1 — never against a build README's `ids:` roster,
  which is a reservation range that admits backlog and decision rows as if they were units.
- The `none` form's REASON is mandatory; a bare `none` is malformed. The kind is optional there and
  required otherwise, because an unbound record names no ids for a kind to describe. The count of
  `none` records is bounded shrink-only by `RECORD_UNBOUND_PIN`, measured against YOUR corpus.
- `gen_build_index.py --print-bindings` is the read-only report: it classifies every record, writes
  nothing, and always exits 0. It is both the migration checklist and the gate's own predicate, so a
  seed list and a gate that disagree is structurally impossible.

## Acceptance ledger — how a built unit evidences its criteria

Inside a record whose `**Serves:**` kind is `journal`, which is already defined as evidence of what
was built. One `**Evidences:**` line per unit, and one line per criterion beneath it:

```
**Evidences:** <id>
- AC1 — `<observation token>` — what was observed
- AC2 — amended rev-<n> — the change, and the section 9 line that logs it
```

- **TWO forms and no third.** OBSERVED carries a backticked token naming the command, file, flag or
  test that made the observation. AMENDED names the revision that changed the criterion. There is no
  "satisfied" without one of them, and no `N/A`: a third form is how a ledger becomes a checkbox
  exercise, and the resulting green is worth nothing.
- **The AMENDED form is the more important of the two.** Without it a run that legitimately found a
  criterion wrong has no legal way to record that, and would either write the observed form untruly
  or skip the ledger. With it, divergence has a home and becomes visible rather than trusted — which
  is the whole reason the ledger exists.
- A record MAY carry several `**Evidences:**` blocks, one per unit it evidences. The block ends at
  the next `**Evidences:**` line or at the next heading.
- The ledger is EVIDENCE and belongs in a record, never in the spec. A spec is the design and is
  written before the code; putting evidence in it would make every build rewrite its own acceptance
  criteria and fill the revision log with bumps that changed no design.
- The gate reads SHAPE and COVERAGE only. It asserts every criterion a closed spec numbers has a line
  in one of the two forms; it does NOT assert the token names anything real, that the observation was
  actually made, or that an amendment was justified. Its header says so.

## The harness meta-gate

Every `fail` BRANCH in every gate is either ARMED — a POSITIVE assertion in that gate's own sibling
test naming a literal slice of the branch's OWN failure text — or listed in
`project/unarmed-branches.txt`. The POPULATION IS DISCOVERED: a tracked `*.sh` that DEFINES `fail()`
and has `fail <n> "` call sites is a gate, and `<stem>.test.sh` beside it is its test; a missing
sibling test is a named failure. `*.test.sh` is excluded, because a fixture that QUOTES a fail line
would otherwise demand a `<stem>.test.test.sh` that will never exist.

The key is `(gate, check number, ordinal)`. The gate is in the key because the PIN's keys are global
and several gates number their checks from 1, so keys collide across gates; the gate name in the
key is what keeps them apart. The ordinal is in the key because one number can carry several branches and a
number-keyed pin lets the cheapest arm hide the valuable one.

A branch's signature ends at the first UNESCAPED closing quote of its message. Capturing to end of
line puts shell source into the signature for any branch written inline as `{ fail 2 "…"; ok=0; }`,
and no assertion can ever emit that — the row becomes permanently unarmable inside a shrink-only
pin.

Three things do NOT arm a branch: a bare `check N` mention, an ABSENCE assertion, and a COMMENT. All
three are "something in the file mentions it", which is not "something exercises it".

The pin is shrink-only and reds three ways: a pinned branch that is now armed, a pinned branch that
no longer exists, and a signature the message was reworded out from under. It is EXCLUDED from its
own scan — it holds each signature verbatim in order to name it.

BOTH directions are pinned, PER GATE — `ARMS_FLOORS="<gate>:<branches>:<armed> …"`. The branch floor
catches a deleted guard; the armed floor catches an assertion dropped by WIDENING the pin, which a
branch count alone cannot see because the count falls and the pin still holds. Per-gate rather than
aggregate: a total lets one gate's deletion be masked by another gate's addition, and goes slack by a
whole gate's branch count the day a third gate lands. A gate that raises a named error does not abort
the walk, so one bad gate cannot hide every other gate's findings.

`tools/memory-tree/check-arms.py --report` shows every branch, its line, its signature and its state.

The pin's working state is EMPTY, and it is not empty today — one branch is pinned. `--report`
prints the live count and this sentence deliberately does not, because a number written here rots
while the gate stays green; the sentence claimed the pin WAS empty for as long as it carried a row,
which is the same defect one level up. A row appears when a new branch lands that no fixture can
reach, and it carries the REASON in a comment above it: "not yet written" and "cannot be written
from here" look identical in a bare pin and only one of them is acceptable. Where an arm goes is a
property of the harness, not a preference: the hygiene gate's `fail` never aborts, so one scratch
tree trips many branches in one ~9 s invocation and the fixtures batch; the manifest gate's CALLERS
short-circuit — `BLOCK_OK` skips four whole checks after any check-2 branch fires, and check 3 is a
mutually-exclusive `if`/`elif` chain — so its branches need separate small repos and must not be
helpfully merged back together.

## The bug-class catalogue

One authored record per class under `gotchas/`, front matter `name` + `description` (+ optional
`kind` and `universal`) at COLUMN 0 — an indented key is dropped without a word by any simple parser,
so it is a named error here. ANCHORS ARE DERIVED, not declared: a record's anchors are the
backtick-quoted path-like tokens in its body, because an authored list is a second copy of what the
body already says. Derivation over-selects rather than under-selects, and a record naming no path is
REPORTED as unanchored rather than silently never firing.

Hand a reviewer the classes their diff can hit:

```bash
python tools/memory-tree/gotchas.py --for-diff <base>..<head>
```

Its stdout IS the checklist. A checklist nobody can finish is not a checklist.

## Codebase-map interop

If the codebase-map kit is adopted with its `MAP_ROOT` a DIRECT child of this tree (e.g.
`<MEMORY_ROOT>/map`), that subtree is sanctioned automatically (the scripts read
`.codebase-map.conf`): allowed entries are `README.md`, `FOUNDATION.md`, `baseline.toml`,
`affordance-exempt.toml` (the codebase-map kit renders it; a gate that did not sanction it reds a
freshly-adopted map),
`features/`, `generated/`; `README.md`,
`FOUNDATION.md` and `features/*.md` carry check 6's size caps but are entry-budget exempt (check 7) —
dossiers are detail files. The two split across CLASSES: `features/*.md` take `DOSSIER_CAP_*`, while
`README.md` and `FOUNDATION.md` take `INDEX_CAP_*` like any other row document. A `features/*.md` over
its cap is SPLIT into two dossiers (never rotated; the map gate requires `FOUNDATION.md` in place), and
that class is deliberately kept tighter than the index class because a split is the only remedy a
dossier has and check 6 is the only size gate it has. The map's
coverage/freshness enforcement is its own test file, not this script.
