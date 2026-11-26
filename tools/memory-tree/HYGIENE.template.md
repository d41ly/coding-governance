<!-- gov:kit memory-tree@2.182 -->
[{{MEMORY_ROOT}}/HYGIENE.md · Level 3 · Read before writing any record, index or id under the memory root; yields to levels 0 to 2]
# {{MEMORY_ROOT}}/ retention & hygiene

`{{MEMORY_ROOT}}/` is the project's AI-first memory: version-controlled, travelling to every node on clone.
It holds one append-only decision log, per-build folders, the gate's own waiver registries, and
long-lived guides.
The tree is FLAT: the discipline is a SIGNAL, not a directory. Which discipline a build served is
declared in each spec's status header as `streams <value>[+<value>]`, over the closed enum your
repo-root `.memory-tree.conf` declares as `DISCIPLINES`. A build spanning two disciplines is one
build, in one folder.
This file is the rule set; the single mechanical enforcement is `{{KIT_DIR}}/check-memory-hygiene.sh`
(run by CI, the pre-commit hook, and the local gate runner). Prose rules with no wiring rot — the
script is the law, this doc explains it.

## Structure

```
{{MEMORY_ROOT}}/
├── README.md              root index (one-liners)
├── LIVE.md                GENERATED — builds with a non-terminal unit ({{KIT_DIR}}/gen_build_index.py)
├── ledger/<YYYY-MM>.md    GENERATED — one row per build opened that month; freezes when the month passes
├── HYGIENE.md             this file
├── TEMPLATE-SPEC.md       the canonical spec/design-pass format (check 12; ships with the kit)
├── DECISIONS.md           append-only decision index, EVERY family, grouped for reading
├── backlog/<FAMILY>.md    `shards`: mutable backlog, one shard per family; `builds`: the GENERATED view
├── decisions/             decision detail (append-only area files)
├── guides/                long-lived reference guides
├── archive/               rotated indexes + legacy material a build can't claim
├── project/               the gate's own waiver registries (`*.txt`) and nothing else
└── builds/<slug>/
    ├── README.md                   (the build's entry point; mostly generated)
    ├── RUN.md                      run-state for an UNATTENDED run; only when one is/was live
    ├── BACKLOG.md                  this build's own asks and dispositions; `builds` layout only
    └── prompts/ · spec/ · build/ · reviews/   (<date>-<kind>[-<FAMILY>]-<slug>-<seq>.md)
```

`<FAMILY>` is a stream's id family from `.memory-tree.conf` (`architecture:ARCH …`). A build folder is
named for its SLUG alone — no date, no family. A recording filename MAY carry the family as an
optional qualifier, which is how one slug shared by two families survives in a single folder.
Ceremony is conditional: subfolders exist only when non-empty; a single-file build is one spec file
plus its backlog row — no README. With `BACKLOG_MODE` set to `builds` the smallest build is smaller still: a
folder holding nothing but `BACKLOG.md`, which is a FILING HOME for asks nobody has specced yet. Non-markdown artifacts (scripts, data) are legal only inside
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
  `BUILD_README_ENTRY_CAP_CHARS` (350). Both are declared in `.memory-tree.conf`, and so is the
  unit they count in; this tree's `ENTRY_CAP_UNIT` is: {{ENTRY_CAP_UNIT}}. Detail
  lives in the build folder or decision file the line points at. `guides/*.md` is exempt from the
  entry budget — a guide is prose, not index rows — and still carries the file caps below. That
  exemption is ONE expression with one base and one optional append for the codebase-map detail
  files; a second full spelling of it is how the `guides/` half went missing once.
- **File caps:** index and generated files are capped BY CLASS, and every cap is declared in
  `.memory-tree.conf` (`INDEX_CAP_*`, `GUIDE_CAP_*`, `BUILD_README_CAP_*`, `DOSSIER_CAP_*`). The shipped
  defaults are 20 KB / 250 lines for a row document, 96 KB / 1200 lines for a guide, 25 KB with no line
  cap for a build README, and 20 KB with no line cap for a codebase-map dossier. `archive/` is wholly
  exempt. A LINE cap of 0 means no independent line cap for that class, which is how a project retires
  the line axis. This tree's row-document line cap, `INDEX_CAP_LINES`, is: {{INDEX_CAP_LINES}}.
- **Rotation mode is DECLARED, never assumed.** `.memory-tree.conf` sets `ROTATION_MODE` to one of
  `cut | snapshot`, and a repo that declares neither has not decided rather than defaulted. **`cut`** —
  move only the TERMINAL rows out to `archive/<INDEX>.<date>.md`, leaving every non-terminal row in the
  live index, so an id sits in exactly ONE file and its status has exactly one owner. **`snapshot`** —
  `git mv <INDEX>.md archive/<INDEX>.<date>.md` whole, then open a fresh index carrying the
  non-terminal rows forward, so a live id sits in two files and the archived copy is a dated
  PHOTOGRAPH of the index, never a second answer about that id's status.
- **The two do not blend, and blending them is the defect this key exists to prevent.** A whole-file
  move PLUS a carry-forward writes every live row into a frozen file, and each of those rows then
  drifts, one status edit at a time, into contradicting the shard it was cut from. That is not
  hypothetical: it is how one archive in this kit's own dogfood repo came to hold 66 non-terminal rows
  under a header promising terminal ones only, with 49 of its ids also live in the shard and 7 of
  those disagreeing about status.
- **Either mode:** the fresh or surviving index notes the rotation in its PREAMBLE, naming the archive
  file (check 10, which greps for that basename and reads nothing else) and what moved; rotated archives stay inside `{{MEMORY_ROOT}}/` so the all-time id-collision
  grep still reaches them; and rotation never rewrites or renumbers a ratified record.
- **The live-row floor.** Non-terminal rows survive the rotation under either mode, so a shard's floor
  is its LIVE ROW COUNT: when nothing terminal is left, rotating is a no-op and the next row breaches
  the cap. `drift-audit` reports that per shard on every run (`live_backlog_rows_per_shard`,
  report-only). `TOOL-aRelaxedShard-4`. Under `cut` that floor is reached sooner, because a cut
  rotation sheds less.
- **NOT CHECKED, and it matters:** nothing in this engine asserts that a tree HONOURS its declared
  mode. `ROTATION_MODE` is validated against the closed set and then read by no check. A green bar is
  therefore not evidence that an archive holds what the mode says it should.

## Status vocabulary (backlogs)

Every backlog row leads with exactly one token of
`OPEN · SPECCED · INPROGRESS · BLOCKED · DEFERRED · CLOSED · WONTDO`, in its `·`/`|`/leading-dash slot
(a prose mention of one of these words elsewhere on the line does not count). New-entry dash form:
`- <id> · <STATUS> · <one-liner>[ → <pointer>]`.
Spec status headers (check 12) reuse the same seven tokens with spec-lifecycle meanings — see
`TEMPLATE-SPEC.md`.

## Backlog layout (`BACKLOG_MODE`)

`.memory-tree.conf` sets `BACKLOG_MODE` to `shards` or `builds`; blank reads `shards`, which is what
a conf predating the key describes, and an unrecognised value ABORTS the gate at exit 2 rather than
falling back — a migration that half-happened is worse than one that refused. Unlike `ROTATION_MODE`
there is no UNDECLARED third state, because every check below has to grade some layout.

- **`shards`** — an ask is a row in `backlog/<FAMILY>.md`, which is an AUTHORED document: it carries
  the status vocabulary above, the index caps, the entry budget and the rotation rules.
- **`builds`** — an ask is a row in `builds/<slug>/BACKLOG.md`, filed once, and `backlog/<FAMILY>.md`
  becomes a GENERATED view of the live asks of that family. A view is re-rendered, never reconciled,
  and its status is FOLDED from disposition rows and spec header verbs rather than typed.
- Which checks move, and how, is in each check's own entry in the catalog below: 4, 6, 7, 8, 10, 13,
  15, 20 and 24. Under `shards` every one of them behaves exactly as it did before the key existed.
- Check 26 is not in that list because it has no `shards` behaviour to preserve: it arrived with
  the key, it grades merges across the switch itself, and on a shards-mode tree it announces that it
  is dormant rather than reporting a clean zero.
- `ASK_CUTOFF` is read only under `builds`. It is the zero-padded date that separates asks MIGRATED
  from a shard — whose ids are already anchored in another build's records — from asks filed after
  the switch-over. Check 13 below is its one consumer.

## The grandfather ratchet

The plain lists in `{{MEMORY_ROOT}}/project/` — the whole of what that directory holds — read as exact-key
set membership rather than a `grep -qxF` per call, because that fork ran once per scanned file. Most are
ledger populations (TOOL-dWitnessedBar-16): a header line rendered from the list's `[[ledger]]` table,
then one TAB row per key, its count, its sha and its disposition, read through the ledger factory and
never parsed by hand; a row's reason is the conversion record's or its widen record's, never the row's.
- **`legacy-files.txt`** — recording files kept under historical names (e.g. from a migration), permanently
  exempt from the recording-file naming check, from check 4's build-folder shape (a listed folder
  name or a listed build-root file) and from check 21's missing-Serves branch. Should not grow after
  the initial adoption.
- **`curation-debt.txt`** — index files pending slimming, exempt from the cap / entry-budget / status-vocabulary
  checks while listed. Every curation sweep deletes lines; empty = fully strict. CI fails if a listed path is gone,
  and — since `TOOL-cGradedDebt-1` — if a listed path would PASS all three unwaived, because a row
  that hides nothing has stopped shrinking. The same run prints which of the three each row earns,
  so a waiver wider than its fault is visible without being failed. Held under `--staged`.
- **`id-orphan-waiver.txt`** — ids cited in the present tense but never defined, deliberately
  (check 14), the `id-orphan-waiver` ledger keyed by id, with a stale-entry guard: a waived id that
  now resolves, or that no present-tense file cites, reds. PRESENT, even empty, it arms checks 13
  and 14; absent, they are off, and `--scaffold` does not write it.
- **`corpus-path-unresolved.txt`** — rooted repo-path citations that resolve to nothing (check 15),
  the `corpus-path-unresolved` ledger keyed by `(citing-file, cited-path)`, its count the
  occurrences. PRESENT, even empty, it arms checks 13 and 15; absent, they are off, and
  `--scaffold` does not write it.
- **`row-duplicates.txt`**, **`unbound-records.txt`** — the keyed populations of checks 20 and 21,
  one row per tolerated duplicate `(shard, id)` and per graded unbound record. Shrink-only; an
  offender with no row reds, and so does a row no offender matches.
- **`dossier-decisions-empty.txt`** — the feature dossiers declaring no decisions, one row per
  feature, graded by `ratchet (both ways)`. **`date-cutoffs.txt`** — every `*_CUTOFF` date of the
  root confs in the working tree, ignored ones excluded, as an eight-digit ceiling, a blank one `99991231`, so a date moved later reds.
- **`unarmed-branches.txt`** — `fail` branches no assertion reaches (the harness meta-gate below).
  Shrink-only, and EMPTY is its working state rather than its retirement.
- **`substitution-fed-loops.txt`** — the sites `gate-lint`'s shell scan grades, shipped by that kit
  as an EMPTY seed the repo then owns. Rows are this tree's own; gov's would name paths you do not
  have.
- **`pass-order-waiver.txt`** — the unattended kit's pass-order checker reads it at this default
  path, so check 3 admits it by name wherever that kit is adopted. A registry a PROJECT adds goes in
  `PROJECT_REGISTRY_EXTRA` instead.
- **`positional-refs.txt`** — the playbook kit's positional check reads its list at this default
  path and reds it absent, and that kit's write mode writes it empty, so the project-registry
  whitelist admits it by name wherever that kit is adopted. Its rows are this tree's own.
- `project/method-carriers.txt` — every file outside the memory tree that POINTS AT
  `guides/BUILD-METHOD.md`, one ledger row keyed by `path` each, read by
  `check-method-carriers.sh`. Keyed on PATH alone, never `<path>:<line>`. It is per-repo and the kit
  ships none: an adopter's is scaffolded from their OWN measured population, because gov's rows would
  name paths their tree does not have.

MOST are scaffolded by `adopt-memory-tree.sh`, not all: a registry that arrives with the gate
that reads it is scaffolded by nothing. "Absent" and "present and empty" read identically
to every consumer, so a registry a gate names and nothing creates is invisible until the first row.

## Ids — how a session mints them

Carried from the charter's v3.5 node section when v4.0 cut it to one `[ids]` practice
(PLAY-aDistilledCharter-3). Checks 5, 13 and 14 below grade what these rules produce.

- Every new tracked id is `FAMILY-<slug>-<seq>`, owned by the session that mints it, so nothing it
  numbers can be contested.
- The slug is the node's tag from the charter's node registry plus fresh words, minted ONCE per
  session; the tag's letter makes two nodes' slugs disjoint. Its shape is the slug grammar's, the policy
  keys `builds.slug-words`, `builds.slug-style` and `builds.slug-date` as `derive_slug_grammar` in the
  memory-tree kit's `id_grammar.py` derives them, and a new build's README records it as `slug-grammar:`.
- `<seq>` is a plain 1-up per session and family, unpadded: a label, never a rank. The next one is the
  numeric maximum of YOUR ids in that family plus one, carried in session state, because an
  uncommitted id is invisible to grep.
- Before using a slug, grep the whole memory tree for `[A-Z]+-<slug>-[0-9]` at all times, archives
  included, and scan the live rows of the work-state index; re-roll on any hit.
- Within a build, no reserve-above-a-marker, no shared counter and no renumber-on-merge: the slug,
  claimed once at `refs/gov/claims/<slug>`, is the guarantee. A filer outside a build, one filing an
  ask in another build's family, mints the id through `gov-claim.sh ask`, under that family's counter
  ref `refs/gov/claims/asks/<FAMILY>-<slug>`.
- A session is one continuous effort under one slug, across work-units and families; a resumed or
  summarized session keeps its slug.
- A fan-out child never mints: its orchestrator does, or the child takes a slug of its own.
- The residual tie-break: the later to merge re-mints its slug for every UNMERGED id, and an id
  already merged wins.
- Legacy id eras are frozen: cite them verbatim, never renumber, never mint in their format.
- Shorthand with the slug elided is for session prose only, never where ids are the permanent record,
  because it is shape-identical to a frozen legacy id.

## The check catalog (all in `{{KIT_DIR}}/check-memory-hygiene.sh`; this file is the prose home)

1. **prompt placement** — prompt-kind files only under `builds/*/prompts/` or `archive/`.
2. **link integrity** — every relative md link resolves (exempt: DECISIONS.md, `decisions/`, `archive/`,
   and `legacy-files.txt`-listed recordings). The generated index files are NOT exempt.
3. **structure lint** — the `{{MEMORY_ROOT}}/` root holds only the sanctioned set; `backlog/` holds only
   `<FAMILY>.md`; `builds/` holds only folders; `decisions/ guides/ archive/` contents are
   unconstrained; `project/` holds ONLY the waiver registries — no catch-all — and its selector
   carries rule 5's guard, so a mis-segmented `project/` path reds instead of admitting everything;
   `builds/` shape is check 4.
4. **build-folder naming** — `builds/*` is the SLUG alone, no date and no family prefix; inside a
   build folder only `README.md RUN.md prompts/ spec/ build/ reviews/` plus loose
   recording-named `.md`; non-md only in `build/`. `RUN.md` is the UNATTENDED run-state file: one
   generated region plus an authored one, present only while a run is or was live. It is in NO size
   check — see rule 6 — and deliberately OUTSIDE rule 8, because a run phase is not a slot status
   and no token in that vocabulary means "built and reviewed, not yet landed". The RETIRED form
   `RUN.<PHASE>.<8 hex>.md` is admitted here by grammar and IS capped by rule 6. With
   `BACKLOG_MODE` set to `builds` a `BACKLOG.md` is admitted at a build root too, including in a folder that
   holds nothing else; under `shards` it is a stray file and is named.
5. **recording-file naming** — files under the four subfolders, AT ANY DEPTH, match
   `<date>-<kind>[-<FAMILY>]-<slug>-<seq>[-<unit-tail>].md`. The kind comes from the SUBFOLDER, not
   from the file's immediate parent — `spec/units/x.md` is a spec. The family is the closed
   `FAMILIES` alternation and the optional unit tail is shared with check 12's selector, in one
   variable, because two hand-copied EREs for one grammar had already diverged (grandfather:
   `legacy-files.txt`).
6. **index size caps** — FOUR classes, because prose, rows, a generated surface and a map dossier
   fail for different reasons. Row
   documents ≤ `INDEX_CAP_BYTES` / `INDEX_CAP_LINES` (20 KB / 250 by default); `guides/*.md` ≤
   `GUIDE_CAP_BYTES` / `GUIDE_CAP_LINES` (96 KB / 1200); a build `README.md` ≤
   `BUILD_README_CAP_BYTES` (25 KB) with `BUILD_README_CAP_LINES` at 0, which means NO independent
   line cap for that class; and a codebase-map dossier ≤ `DOSSIER_CAP_BYTES` (20 KB) with no line cap,
   reached only where a map is adopted and guarded on a non-empty prefix, because an unguarded selector
   would hand the dossier bound to the whole tree. A build README is priced by its authored bytes:
   its `wc -c` figure less every line from a `<!-- gen:build-index -->`, `<!-- gen:build-coverage -->`,
   `<!-- gen:build-order -->` or `<!-- gen:build-edges -->` marker through its matching close, and less
   the front matter's `ids:` line, so the generated half never bills the cap at any roster size; a
   README whose pairs do not balance is priced whole. This check does NOT verify that a region's bytes
   really are generated — check 9 does, by re-rendering the four regions and byte-comparing them
   (TOOL-aMendedFleet-84, the coverage pair TOOL-dTrueNorth-3). A cap that is not a whole number, or a zero BYTE cap, is refused before
   any check runs: the gate exits 2 naming the key rather than reporting a tree it could not
   measure (grandfather:
   `curation-debt.txt` exempts either). A guide is MANDATORY reading the charter points a session at,
   and check 16 refuses a charter-cited file that nothing caps — but for a guide the LINE count is a
   proxy for the byte cap beside it. There is no longer a SUMMED read-path budget behind these:
   `READ_PATH_CEILING` was retired in 2.42, and these per-class caps ARE the bound a guide has.
   Entry-budget exempt (check 7's `ex7`) — a
   guide is prose, not index rows. A LIVE `builds/*/RUN.md` is exempt from this rule BY CLASS: it is
   append-only by construction, the driver writes a row per verb and removes none, so no compliant
   state exists and the remedy this rule names is unreachable while the record is still being read.
   The class is the RESERVED NAME, which rule 4 lets only the run-state file hold, and retirement is
   a rename — so the frozen `RUN.<PHASE>.<8 hex>.md` stays capped and keeps the `ex7` exemption.

   **A row class may retire its line axis** by declaring its line cap as 0; this tree's
   `INDEX_CAP_LINES` is: {{INDEX_CAP_LINES}}. Retiring it is a decision, not a tidy-up, so record it in
   the decision log: at check 7's 300-char entry budget a 250-line row document may hold 75,000 B, so
   the byte figure decides most cases — but a line figure that DOES bind on some members is a real
   bound, which is why a codebase-map dossier is its own class rather than inheriting a relaxed index
   cap.

   **With `BACKLOG_MODE` set to `builds` the population swaps one member for another.** Each
   `builds/*/BACKLOG.md` joins the row class, and the family VIEWS leave it: a view is generated, so
   a cap on it would be a hard ceiling on how many live asks a family may hold, which owner ruling
   D3 refused. A `BACKLOG.md` over cap fails on its OWN branch, whose remedy is to move detail into
   a `build/` recording and NEVER to rotate — an ask is filed exactly once, in its own build's
   folder, and a rotation would move it where the view cannot link to it.
7. **entry budget** — index entry lines ≤ `ENTRY_CAP_CHARS` (300 by default), a build `README.md`
   ≤ `BUILD_README_ENTRY_CAP_CHARS` (350) (grandfather: `curation-debt.txt`). With
   `BACKLOG_MODE` set to `builds` the population is check 6's set PLUS the family views, MINUS the
   exemptions — the views are graded, because their rows are short by construction and this budget
   is what keeps them so, and `builds/*/BACKLOG.md` is EXEMPT, because the ask is the record and its
   text is free prose on one line.
8. **status vocabulary** — only where `BACKLOG_MODE` reads `shards`. `backlog/<FAMILY>.md` rows carry exactly
   one slot status token (grandfather: `curation-debt.txt`).
   Under `builds` this check is RETIRED and says so on every run, in place of the line below: an ask
   carries no status token at all there, its status being folded from records that check 9 grades by
   re-rendering. Its empty-population guard is retired with it, because that guard's precondition
   counts the very files the check no longer reads.
   It REPORTS the number of rows it graded, because its population guard counts shard FILES: a waiver
   over most of the rows otherwise reads as a green check over a population nobody sees.
9. **build-index drift** — `{{KIT_DIR}}/gen_build_index.py --check` must be clean. The index is
   DERIVED from each build's README front matter (`slug opened ids [status]`, at column 0, opening at
   line 1) plus every `**Status:**` header under its `spec/`. The key set is the generator's
   `FRONT_MATTER_KEYS`, each key's role, type and requiredness declared once: a key it does not name
   and a value its type refuses are NAMED errors. `node`, `roster` and `streams` are DERIVED and not
   typed (`--print-front-matter <slug>` prints them); a README the `build-readme-typed-derived`
   population lists may still type them, read and never refused, the derivation winning in every
   render (`TOOL-dTotalRecall-4`). A build with no
   README, an unpaired generated-region marker, or two answers to its own status is a NAMED error.
   Pin the generated files `eol=lf` in `.gitattributes` — the gate byte-compares them. While any
   file under `archive/` is untracked, `--check` and `--write` both REFUSE and name it: the index
   reads `git ls-files`, so a half-staged rotation's moved rows look deleted. Stage the archive
   first (`TOOL-dHomedResolver-2`).
   `--check` reports only what `--write` cures: the as-built view DESIGN_VIEW names is one more
   artifact, its byte drift listed under the same `--write` remedy, and its other findings, which
   `--write` cannot cure, are check 30's (`TOOL-dTrueNorth-16`).
   A build README carries five generated regions, in this order: `<!-- gen:build-index -->`,
   `<!-- gen:build-coverage -->`, `<!-- gen:build-order -->`, `<!-- gen:build-edges -->` and
   `<!-- gen:build-routes -->`, the last routing a reader to each record by purpose.
   `--write` creates a missing pair and `--check` never demands one, save the coverage pair: it renders
   the design clauses' coverage from the carries join `SPEC_CARRIES_CUTOFF` arms, every field with an
   explicit none, so `--write` creates it only in a chain build's README, one the design view's Build
   column names, and `--check` names a chain README without it and any other README holding one. With
   the key blank no README gains it, and one that holds it renders a single line saying so
   (`TOOL-dTrueNorth-3`).
10. **rotation note** — every rotated `archive/<STEM>.<date><suffix?>.md` is referenced from its live index, which is resolved at the stem's DECLARED HOME —
    `DECISIONS.md` at the memory root, `backlog/<FAMILY>.md` for a family — and never by searching
    for a file of that name, so a build file that shares a stem's name is not consulted
    (`TOOL-dHomedResolver-1`). A home that is not tracked is a NAMED finding, never a skip. The reference is read from everything above the index's first row, and never fewer
    than its first three lines. It grades ANNOUNCEMENT, never the archive's CONTENTS.
    With `BACKLOG_MODE` set to `builds` an archive whose stem is a FAMILY is left to check 9's archive
    guard and COUNTED in one line, because the live file at that stem is a generated view that could
    never reference it — a finding here would have no remedy but to hand-edit the next render away.
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
    Every numbered acceptance bullet must also name the BREAK that would turn it red, in a clause
    marked `Red when:`, once the filename date reaches `SPEC_FAILURE_MODE_CUTOFF`, on either tier.
    The per-bullet walk is shared with the witness arm above and each reads only its own key.
    A LIVE spec must have the `base` sha in its status header RESOLVE to a real commit once the
    filename date reaches `BASE_RESOLVE_CUTOFF`, on either tier. TERMINAL specs are excluded, so a
    spec that goes SPECCED to CLOSED in one commit is never graded at all — a known bypass, named
    here rather than implied away. Skipped with a stderr line in a shallow clone, where every
    commit outside the fetch depth answers `missing`.
    A Tier-2 spec must carry a `### Edges` block in §3 once the filename date reaches
    `SPEC_EDGES_CUTOFF`: one bullet per edge, `**consumes-from**` or `**hands-off**` plus a
    backticked sibling id or the bare word `external`, or the single word `none`. The SHAPE arm
    runs under `--staged`; there the reciprocity, order and payload JOINS read each staged spec's
    whole build from the worktree and report an edge either of whose ends is staged.
    Every §2 scope item must name the acceptance criterion that observes it, or carry `NOT OBSERVED`
    and a reason, once the filename date reaches `SCOPE_JOIN_CUTOFF`, on either tier — and only for a
    spec carrying BOTH headings, matched by heading TEXT rather than by ordinal. SHAPE only.
    Every revision-log entry numbered rev-2 or higher must name what it MOVED — a `§<n>`,
    `section <n>`, `S<n>` or `AC<n>` token — once the filename date reaches `REV_SCOPE_CUTOFF`, on
    either tier. Graded per ENTRY with continuation lines folded in, because this corpus wraps the
    revision log and puts the detail in the wrap; rev-1 is exempt, and the engine announces a zero
    population rather than passing silently while the cutoff sits ahead of the corpus.
    §8 is graded PER F-ITEM once the filename date reaches `FORK_ITEM_CUTOFF`, which supersedes the
    section-wide reading there: at a terminal status, on either tier, each F-item's span carries its
    own mark, quoted marks not counting; a Tier-2 §8 of any other shape reds at ANY status and under
    `--staged`. The grammar is `TEMPLATE-SPEC.md`'s, and a zero population is announced likewise.
    A Tier-1 spec takes the micro-spec profile once the filename date reaches `SPEC_TIER1_CUTOFF`:
    every `##` heading is a canonical title, the eight required titles are present, the titles run
    in canonical order, and no section body is empty. Sections are found by heading TEXT, so the
    numbering is free; Production-readiness checklist and Reuse audit are optional. One file, no
    join, so it runs under `--staged`; SHAPE only, and a zero population is announced likewise.

13. **id-definition collision** — one id claimed by two different build folders. A decision-log row
    and its spec's H1 both anchor the same id BY DESIGN (the index points at the record), so
    "defined twice" is not the test; "claimed by two builds" is.
    With `BACKLOG_MODE` set to `builds` an ask row in a `BACKLOG.md` filed BEFORE `ASK_CUTOFF` is not its
    folder's claim: those ids were migrated and their records already live elsewhere. An ask filed on
    or after the cutoff DOES claim, so a new foreign anchor is still a collision. The row still
    DEFINES the id, so nothing this silences becomes an orphan under check 14. A cutoff that is blank
    or not zero-padded disarms the comparison rather than being compared raw, and one line names the
    verdict — comparing a blank cutoff as the empty string would read every migrated ask as filed
    after it and red them all at once.
14. **orphan ids** — an id cited in the PRESENT-tense corpus but never defined fails unless listed
    in `project/id-orphan-waiver.txt`. The population is check 15's, decided by one test for both:
    a record of a moment or an append-only file is not a claim about now. The waiver is not a
    citation. It is keyed by id, shrink-only by `ratchet (never gains)`, with a stale-entry guard: a
    waived id that now resolves, or that no present-tense file cites, is a stale row and reds.
    The waiver ARMS this check by being present, even empty, and check 13 with it.
    An id with no record is cited as `missing:` written immediately before the id: it is no orphan,
    joins no build's roster, and `--report` counts it on its own line. That form naming an id the
    corpus DEFINES reds in a present-tense file, as marked missing but defined, naming both files.
15. **dead repo-path citations** — a rooted repo-path citation in the PRESENT-tense corpus that
    resolves to nothing must be registered in `project/corpus-path-unresolved.txt`. A DIRECTORY
    citation counts: it is exactly as broken when it does not resolve, and the flatten left four of
    them in the live ledger. `DEAD_PATH_EXCLUDE` names prefixes that are not repo CONTENT — a
    checkout location, say — because resolution never touches the filesystem and cannot tell meaning
    from existence. The registry ARMS this check by being present, even empty, and check 13 with it.
    It is a ledger, read through the ledger factory: set equality between the registry and the
    measured set, keyed on `(citing-file, cited-path)` with an occurrence count and NEVER on a line
    number — a line number moves on unrelated edits and a gate whose steady state is red gets
    bypassed; a duplicate row is the factory's refusal; its shrink is `ratchet (never gains)`'s.
    With `BACKLOG_MODE` set to `builds` the PRESENT-tense corpus swaps `backlog/` for
    `builds/<slug>/BACKLOG.md`: the ask keeps its path grading and the view's derived text does not.
    The member is replaced rather than dropped, because dropping it alone would take every graded
    ask path token out of this check and report green.
    The build READMEs `LIVE.md` links are an ADVISORY population: their dead citations, a trailing
    `:<line>` locator cut first, print as one NON-GATING `HYGIENE advisory check 15:` note and are
    never registered, because a build README is a record of its moment.
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

Checks 13-15 live in `{{KIT_DIR}}/corpus_ids.py` and are DISABLED while both waiver homes,
`project/id-orphan-waiver.txt` and `project/corpus-path-unresolved.txt`, are absent; a home present,
even empty, arms its checks. Every row is MEASURED against the adopting corpus (`corpus_ids.py
--measure`), never inherited: a row copied from another tree is either vacuous or permanently red. The
id grammar comes from this kit's own `id_grammar.py`, so arming these checks requires that file — with
both homes absent it is never imported, and with a home present and the file absent the failure is
NAMED, not a traceback.

17. **catalogue index freshness** — `gotchas/INDEX.md` byte-matches a fresh render.
18. **a class declares its resolution** — every `kind: class` record names a gate or says in as many
    words that it has none. Silence is not acceptable: "no gate named" and "gate not yet written" are
    indistinguishable from outside, and the second one quietly never happens. Every `kind: invariant`
    record names a `decision:` this corpus DEFINES, carries all five sections non-empty, and opens its
    `## Guarded by` with `no machine gate` or with backticked tokens alone, each a tracked path or a
    leg name in the manifest `LEG_MANIFEST` names. A blank key, or an absent id-grammar kit, turns its
    arm into a `NOT resolved` line printed at exit 0 — announced, never a red and never silent.
19. **the record can actually fire** — a class record derives at least one anchor or is marked
    `universal`, and a record whose anchors reach ONLY the append-only tree is reported as INERT:
    reachable on paper, dead in practice. The `universal` set is budgeted (`UNIVERSAL_BUDGET`)
    because every universal record is emitted on EVERY reviewer's checklist. An invariant is graded
    the same way with no universal escape: unanchored or marked `universal` is a finding.
    A class anchor that selects no tracked path is reported by one NON-GATING
    `HYGIENE advisory check 19:` line naming the counts, never the exit status; `gotchas.py --report`
    lists each one.

20. **one id, one row per document** — within a single row document (the decision index, a backlog
    shard, and the rotated archive of either) an id appears at most once. An archive is recognised by
    the name of the document it ROTATED — `DECISIONS` or a declared FAMILY, plus a date and an
    optional same-day disambiguator — and NOT by being any `.md` under `archive/`, which would sweep
    in frozen snapshots where a quoted example row would red a file nobody may edit. Until
    `TOOL-cSpliceWarden-3` the archive half admitted only `DECISIONS.`-prefixed names, so a rotated
    BACKLOG shard was outside this check entirely; three were, and one of them carried two duplicated
    ids past a green bar for a month. The survivors are KEYED, one row per `(shard, id)` in
    `project/row-duplicates.txt`: a duplicate with no row reds, and so does a row no duplicate
    matches, so a repaired duplicate and a new one never net to zero. An ABSENT home is the empty
    population — the strictest value, never a refusal and never off, because a default that can only
    TIGHTEN needs no ceremony. Each backlog shard's live and unranked rows are counted too, as the
    `live-rows` and `severity-unlabelled` populations, registered UNSEEDED: no default over an
    inherited population is honest, so every green run prints one NOT MEASURED line per shard, which
    the gate shows rather than swallows.
    Scope is PER FILE deliberately: corpus-wide would red every designed backlog-row-plus-decision-row
    pair. NAMED GAP — the live index and its rotated archive are two files, so a row that rotates out
    and is re-minted is not caught here; the all-time collision grep the index's own header
    prescribes covers that. Keyability is asserted alongside it, but only as the precondition that
    makes the uniqueness census meaningful: on its own it is a check the corpus cannot fail, over a
    property the merge driver already enforces where it can be violated.
    With `BACKLOG_MODE` set to `builds` the row documents are the decision index and ITS archives alone: a
    family view's rows are link-wrapped renderings of asks filed elsewhere, so reading one as a row
    document would report a mis-segmented grammar against text no author wrote, and ask uniqueness
    is the fold's corpus-wide verdict rather than a per-file one.

24. **the declared rotation mode is HONOURED** — with `ROTATION_MODE` set to `cut` a rotated archive of a
    status-bearing shard holds TERMINAL rows only, and no id sits in both an archive and the live
    index it was cut from. Those two together are what `cut` means: one id, one file. Delegated to
    `row_grammar.py`, which owns the row grammar — a second spelling of it in shell passed a
    bold-wrapped id silently, and the decision index carries fifteen such rows. NOT GRADED, and
    announced on every run rather than passed over: `snapshot`, whose assertion inverts to "an
    archived row is never edited after the rotation" and whose baseline commit is not resolvable
    here; an UNDECLARED mode; a DECISIONS archive's terminal half, since a decision row carries no
    lifecycle token; and the CONTENT of any archive, ever. A `cut` tree with no rotated archive says
    it graded nothing rather than reporting clean.
    With `BACKLOG_MODE` set to `builds` it follows check 20's population out: a family archive is check 9's
    archive guard's, and this check grades the decision-log archive alone.

21. **every record names the spec it is evidence about** — a build folder holds one spec per unit,
    and everything else in it (an adversarial review, a build ledger, a research report, a
    transcript) is a RECORD. Each carries one authored line in its head naming the spec ids it
    serves, so the binding is a fact rather than an inference from a filename ordinal. The rule, the
    grammar and the escape are below under "Record bindings". Delegated to `gen_build_index.py`,
    which already reads every record's bytes; the parse RAISES nothing, so an unannotated record can
    never refuse the render. A record `legacy-files.txt` lists is not graded for a missing Serves
    line. `RECORD_UNDATED_ARTIFACTS` set to `exempt` drops an undated non-markdown file (a JSON result, an
    HTML report) from that branch and prints how many it dropped on every run; blank or `grade`
    grades them. From `SPEC_AUDIT_PIN_CUTOFF` its audit-pin branch fails each `spec-audit` record,
    dated on or after the key or undated, that leaves an id without an `@rev-N` pin or pins it
    above its spec's header revision, refuses a parse printing no `Q` row, and names on every run
    how many records it graded, or that the arm is off.

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

25. **a retirement answers for its readers** — a §2 scope item of a LIVE spec that retires a named
    thing carries a `**Readers:**` clause, then the literal `by name:`, then the literal `by value:`,
    on the item's opening line or any line beneath it. LIVE is a status header that is not `CLOSED`
    or `WONTDO`, and the check has no cutoff key of its own. Its population is check 12's selection,
    so a blank `SPEC_FORMAT_CUTOFF` disarms this check whatever else is true, and the engine says so
    at exit 0 rather than going quiet.
    **The trigger.** A verb from the closed list in the arm is matched ignoring case, over the item
    with its whitespace squeezed, and reaches the past tense beside the present and the imperative;
    it must sit beside a backticked token of an identifier shape, which is an underscore, a slash, a
    dotted word tail, a lowercase letter then an uppercase one, or two dashes then a letter. A
    markdown path counts as an identifier with or without a slash, because `.md` is a dotted tail
    like any other. A family-slug-seq id, a token of dashes and digits and a token carrying a space
    never count, and a `:<line>` tail is stripped before any shape is tried. A bare backticked word
    counts only beside one of the six declared kind nouns, which are ONE literal in the arm, beside
    the verb list, and are not restated here.
    **Which half is graded how.** The `by value:` half is graded by presence: a backticked token, or
    `NO VALUE READERS` followed by a reason. The `by name:` half is graded by resolution: every
    backticked name it lists must resolve, or the half carries `READER NOT IN TREE` followed by a
    reason, and every name that escape covers is printed, so the skip announces itself. Neither half
    is graded for completeness. The control is `TOOL-dLoggedFlight-22` at rev-3, whose inventory
    missed three readers while every name it did list resolves, so it passes this check. Both
    escapes are taken on trust: the check cannot tell a true escape from a false one, and once
    written a false one passes for good. A clause is graded wherever it appears, not only where the
    trigger fired.
    **What a name resolves against.** A name resolves where a reader spells it as a whole word, and
    never where a record merely quotes it. A reader is every tracked file outside the memory root, plus `guides/`,
    `map/`, `HYGIENE.md`, `TEMPLATE-SPEC.md` and `README.md` inside it. Every other file under the
    root is a record, such as a build record, the archive, the decision log, a backlog, a gotcha note
    or a waiver registry, which quotes a name and so resolves nothing by content. A name also resolves when it is a tracked path, or the part of
    one after a `/`, anywhere in the tree. A `:<line>` tail and a trailing `()` are stripped before
    either test. A whole word means that at each end of the name that is a letter, digit or
    underscore, the character beside it in the reader is none of those, and a name carrying a
    hyphen counts the hyphen among them. So a name spelled only inside a longer identifier
    resolves nothing, a hyphenated name inside a longer hyphenated one included.
    **Not reached, and named rather than implied away:** a retirement whose backticked tokens hold no
    identifier shape, and a retirement carrying no backticked token at all. The author of either is
    never asked, and the remedy is to name the withdrawn thing in backticks.

26. **a TRANSITION MERGE loses no row** — a merge that joins a lineage still editing AUTHORED
    backlog shards to a lineage already rendering them from build folders can drop a row change with
    nothing watching: the shards side edits a file the builds side no longer authors, so a clean
    three-way merge takes a side and neither outcome is a conflict. Every such merge in the history
    HEAD carries is classified BY LINEAGE and never by a parent's tip — a straggler that pulled the
    new conf early has a builds-mode tip and shards-mode content — and each row it changed owes
    exactly ONE `RELOCATED` provenance row naming the id and the change commit. Delegated to
    `transition_audit.py`, which owns the walk, and keyed through this kit's `id_grammar.py` anchor
    grammar, so no second row grammar is spelled here. LIVE ONLY WHEN `BACKLOG_MODE` IS `builds`: on a
    shards-mode tree it prints that it is DORMANT and why, because a silent zero there reads exactly
    like a clean audit. Three DEAD PROBE refusals guard it — a shallow repository, a history whose
    shards-mode commits yield no mode boundary, and a walk that finds no builds-mode commit at all
    while the shell's own conf read says `builds`, which is two readers of one key disagreeing.
    Every line it prints, refusals included, begins `memory-hygiene: check 26 `, so one grep reaches
    all of them.
    NOT GRADED, and said out loud: a rebase, a squash or a cherry-pick that discards rows leaves no
    merge behind and is invisible here; a text change on a continuation line of a wrapped legacy row
    is not a version change to an anchor-keyed reader; and the truth of a `RELOCATED` row's `why` is
    nobody's assertion. The watched paths are `backlog/` and the FAMILY-named rotated archives ALONE,
    never the whole of `archive/`: rotating the decision log is routine, and a directory-wide
    selector would report every id anchored in a rotated log as a lost row. Known transitions are
    pinned in `project/transition-audit.txt`, which is APPEND-ONLY because a transition in history is
    permanent; an unpinned one is COUNTED on the liveness line and never refused, since a merge
    cannot list its own sha. A tree that wants the same refusal at the moment a merge is CONCLUDED
    wires the module as a `commit-msg` hook, which is the one hook a clean `git merge` and a
    conflicted one both reach.

27. **a new record that RESTATES an older one names it** — every decision row and every gotcha whose
    identity is absent at the mainline merge-base is ranked against the records present there, with
    the index builder of this kit's `id_grammar.py` over each record's summary (a row's text after its id,
    a gotcha's `description`). A top hit that reaches `NEAR_MATCH_GATE`'s floor in Jaccard similarity
    AND shares a term of four or more characters is a NEAR MATCH, and the new record must name the
    hit, name a successor `id_grammar.py`'s superseded-by map holds for it, or carry `supersedes`,
    `coexists-with` or `disputes`. It obliges a relation and never judges one. A hit that is a row of
    the new row's own session slug is counted and not graded. Delegated to `row_grammar.py`, which
    owns the row grammar; full runs only, because it reads a commit range. `red:<floor>` fails the
    leg, `warn:<floor>` prints `WARN` lines and passes, BLANK is NOT ARMED and says so on every run,
    and the kit ships it blank: a floor measured on another corpus is not a floor for yours, so
    measure your own with `row_grammar.py --measure-relations <floor>` before arming it. An armed
    run with no mainline base, or with no `id_grammar.py` beside `row_grammar.py`, is a named refusal. Every
    armed run prints one summary line with its counts, red or green.
    NOT GRADED, and said out loud: a near match below the TOP hit; a paraphrase under the floor; a
    bare relation token that names no record; a row edited in place, since the added set is decided
    by identity alone; and two records added in the same range.

28. **one TEXT is held by one record** — every decision row and every gotcha gets one normalized
    content key: a row's text after its id, a gotcha's body after its front matter, with links
    reduced to their text, ISO dates and `*`, `_` and backtick dropped, case and whitespace runs
    folded, and a leading separator run stripped. A key held by two or more distinct identities
    REDS when at least one holder is absent at the mainline merge-base, one finding per key naming
    every holder. It is check 27's exact half. A key whose every holder had landed at the base is
    counted and not reported, because nobody may edit or remove a landed append-only record; with
    no mainline base every key is graded and the summary says so. Delegated to `row_grammar.py
    --check-content`; full runs only. Every run prints one summary line, red or green. The remedy
    is to reword or drop the record that has not landed.
    NOT GRADED, and said out loud: a paraphrase, which is check 27's; an id held twice, which is
    20's and 24's, so a `snapshot` carry-forward is one identity; any record kind but those two;
    front matter; and a duplicate whose every holder had landed at the base.

29. **a chain build's spec is not INPROGRESS while its coverage is red** — with `SPEC_CARRIES_CUTOFF`
    set, a spec of a chain build at `INPROGRESS`, which is past that build's Design exit, fails while
    the carries join finds anything for the build at that exit: an uncarried clause, an owned node no
    spec names, a stale pin, or any other arm. Each refused spec is named with every finding's arm and
    reference. Delegated to `{{KIT_DIR}}/gen_build_index.py --check-coverage`, which reads the one
    value the `build-coverage` region renders (check 9), and a coverage it cannot read fails as well.
    With the key blank it prints one line and passes. Under `--staged` the check passes `--staged`
    through, and the verb's trigger is the render's: it runs when a staged path is a build-index input,
    a staged view row and a staged spec alike, or the carries checker beside the kit, and otherwise
    prints its held line (`TOOL-dTrueNorth-16`). A full run, `--staged` off and no `--only`, reads
    this verdict from check 9's generator process, which runs the verb ahead of its own render, and
    prints it as the standalone verb prints it (`TOOL-dTrueNorth-27`).
    NOT GRADED: a spec at any other status, since `OPEN`, `SPECCED` and `BLOCKED` precede the exit and
    a terminal or `DEFERRED` spec is not building; and a build the design view does not name.
30. **the as-built view's verdicts** — with all four `DESIGN_*` keys set, the deviation records and
    the design record the as-built view renders from must agree: a record departing from a clause
    with no `amends` or `supersedes` row, two amends of one clause no `**Supersedes:**` orders, a
    `**Supersedes:**` naming a record outside its clause's set, an `**After:**` holding a `|`, a
    pinned hash the clause does not carry at the baseline, a `Baseline:` line moved off the pin, a
    view that does not answer `merge: ours` to `git check-attr merge`, so no `.gitattributes` line
    guards it (`TOOL-dTrueNorth-26`), or a view answering `ours` only through an
    untracked info/attributes line, tracked state alone answering otherwise, a macro either side
    defines included (`TOOL-dTrueNorth-32`), each fail, named. Check 30 reads the merge attribute as
    tracked state answers it: no system or global attributes file, no attribute source tree
    (`attr.tree`, `GIT_ATTR_SOURCE`) and no untracked info/attributes line answers it, while the
    work tree's `.gitattributes` files do, an untracked one included. The records read are the TRACKED ones, so a
    draft never staged moves no verdict. These are the findings `--write` cannot cure, so they are not check 9's, whose
    message and remedy read only the view's byte drift. Delegated to
    `{{KIT_DIR}}/gen_build_index.py --check-asbuilt`, which renders through the host `--write` writes the
    view with, and a view it cannot render, a partial key set, an unreadable pin or a `DESIGN_VIEW`
    not named `<date>-build-<unit id>-as-built.md`, the record name its head's two names are read
    from, fails as well.
    With every `DESIGN_*` key blank it prints one line and passes. Under `--staged` its trigger is the
    render's, as check 29's is: it runs when any staged path is a build-index input, the kit's own
    code included, or is `DESIGN_RECORD` or `DESIGN_VIEW` outside that set, and otherwise prints its
    held line (`TOOL-dTrueNorth-16`, `TOOL-dTrueNorth-20`). A full run reads this verdict from check
    9's generator process as check 29 reads its own, printed as the standalone verb prints it
    (`TOOL-dTrueNorth-27`).
31. **a red fix has its record** — an inline red fix has no spec, so its one account is the `red-fix`
    record written after it. Every commit reachable from HEAD that carries a `Red-fix:` trailer owes,
    per trailer value, one record whose `Commit` is that commit's sha and whose `Leg` is that value.
    Failing, each named: J1 a fix commit below HEAD with no record, J2 a record whose `Commit` is no
    such commit, J3 a record whose `Leg` is no trailer value of its commit, J4 a record whose `Files`
    differs from the commit's own paths, J5 two records answering one commit and leg, J6 a malformed
    record. A fix AT HEAD with no record is printed as owed and passes, because the record names the
    commit by sha and so is always the next commit. Under `--staged` the check grades HEAD alone: a
    HEAD carrying the trailer with no record in the index fails, so the commit after a fix is its
    record's, and a HEAD with no trailer prints a held line. Delegated to `build_records.py join
    red-fix`, whose summary line, the commits and records it read, is printed on every green run; a
    join that cannot read git or the tracked records fails as well (`TOOL-aNimbleMend-9`).
    A path-less trailer commit, an empty commit or any merge, whose paths the join's log pass reads
    empty, owes no record: it is outside the fix count and raises no J1 at any depth, a record naming
    it is J2, and the join prints a `path-less` line per trailer value and counts such commits last on
    its summary line, so a path-less HEAD passes under `--staged` too (`TOOL-aClearedLedger-9`).
    NOT GRADED: that the record is the fix's direct child on a full run, a clone with no pre-commit
    hook having no promptness check at all; that `Rerun` or `Red line` is true; that the leg was red;
    whether a merge's resolution changed a file, or whether a path-less commit should carry the trailer.

## Record bindings — how a record names its spec

Within the first 12 unfenced lines, optionally behind a comment marker so a non-markdown record can
carry it too:

```
**Serves:** <kind> <id> [<id> …]
**Serves:** spec-audit <id>@rev-<N> [<id>@rev-<N> …]   (a spec audit, from SPEC_AUDIT_PIN_CUTOFF)
**Serves:** none — <why this record serves no spec>
**Commissions:** <id> [<id> …]          (optional, for a record that PRODUCED specs)
```

- `<kind>` is closed: `spec-audit` (a pre-code pass over a spec) · `diff-review` (a pass over built
  code) · `log` (evidence of what was built; `journal`, its name until TOOL-dTotalRecall-18, is a
  read-only alias still bound and graded as `log`, and no writer emits it) · `research` (a report
  that precedes the specs) ·
  `deviation` (a departure from the design or from a spec, in the grammar under "Deviation records") ·
  `exception` (a principle excused for one part, minted by `PLAY-dOrderedCharter-7`'s record factory) ·
  `override` (minted by `PLAY-dOrderedCharter-2`) · `change` (minted by `PLAY-dOrderedCharter-15`) ·
  `red-fix` (the record of an inline red fix, in the grammar under "Red-fix records") ·
  `disposition` (the owner's disposition of one loop item, in the grammar under "Disposition records") ·
  `acceptance` (a unit's acceptance commands re-run at a commit, in the grammar under "Acceptance
  records") · `transition` (one build stage move, in the grammar under "Transition records") ·
  `recommendation` (a stage exit's review recommendation, in the grammar under "Recommendation
  records") · `widen` (a population's growth admitted with its reason, written by the ratchet pack's
  `ratchet.py widen` door) · `leg-tail` (a failing leg's output tail kept by its hash, written by the
  run-gates kit's `keep_tails.py`) · `flake` (one `test.flakes` run's per-leg verdicts, written by the run-gates kit's
  `verdict_flow.py flakes`) · `gate-health` (one gate-health measurement, the reliability bar derived from
  the flake records, written by the drift kit's `drift_report.py --gate-health --write`) · `card` (a build's orientation card at one
  step, its snapshot, fields `Build`, `Step` and `Ref` and the card's text in one `~~~~` fenced block)
  · `probe-trigger` (a probe opened at an item boundary, fields `Cause`, `Asker`, `Subject`, `At` and
  `Key`) · `probe` (the probe it opened: its pinned head, its `## Method` entries, its run lines and
  its `Verdict` beside `Judged`, written by the loop kit's `probe.py`) · `stream-plan` (a build's
  units grouped into ordered streams, no field and one TOML fence of `[[stream]]` tables, written by
  dIndexedDesign's planner) · `shape-run` (one review exit's `review-shape` line as typed fields,
  written by `gov_record.py new shape-run`, TOOL-dTotalRecall-11) · `mailbox-message` (one
  mailbox message a build's transition disposed, fields `Id`, `From`, `To`, `Kind`, `Subject`,
  `Answers`, `State`, `Reply` and `Ref` and its body in one `~~~~` fenced block, written by the loop
  kit's transition writer). The typed kinds, `TYPED_RECORD_KINDS` in `{{KIT_DIR}}/tree_lib.py`, are
  those after `research`: each record is named `<date>-build-<unit id>-<kind>-<n>.md` in a build's
  `build/` folder, and the kind and that name are joined both ways. An open kind field stops being
  groupable the first time two authors spell one relation differently.
- `<id>` is family-qualified, so a record can name a spec in ANOTHER build — which real corpora need,
  because one closing review legitimately covers two builds. On a `spec-audit` record dated on or
  after `SPEC_AUDIT_PIN_CUTOFF`, or carrying no date, each id is written `<id>@rev-<N>`, N the
  `rev-N` of that spec's status header at the blob the audit read and never above its current
  header: the pin is what makes a revision past it read as unaudited, so a range, which carries no
  pin, is unpinned there. On any other record a trailing `@rev-N` is recorded and never validated.
  A contiguous run may be written `N..M`, which EXPANDS at authoring time and therefore cannot rot
  when the build later gains a unit.
- Ids resolve against the set DEFINED BY A SPEC H1 — never against a build README's `ids:` roster,
  which is a reservation range that admits backlog and decision rows as if they were units.
- The `none` form's REASON is mandatory; a bare `none` is malformed. The kind is optional there and
  required otherwise, because an unbound record names no ids for a kind to describe. The GRADED
  `none` records — those `RECORD_SERVES_CUTOFF` and `legacy-files.txt` leave — are KEYED, one row
  per record in `project/unbound-records.txt`, seeded against YOUR corpus. Check 21 prints their
  count beside `N` on every run; a graded record with no row reds, and so does a row no graded
  record matches.
- `gen_build_index.py --print-bindings` is the read-only report: it classifies every record and
  writes nothing. It exits 0, or 2 on a `SPEC_AUDIT_PIN_CUTOFF` that is neither blank nor an ISO
  date, or on a git read the audit pin needs and cannot make. Beside its A, U, S, B and N rows it
  prints a `P` row per graded id owing a pin, and one `Q` row in four fields, the graded count, the
  cutoff or `off`, and the exempt count or `-`, `Q<TAB><graded><TAB><cutoff><TAB><exempt>`
  (`TOOL-dTrueNorth-14`). It is both the migration checklist and the gate's own predicate, so a
  seed list and a gate that disagree is structurally impossible.
- The check REFUSES when that report exits non-zero or prints no `N` row. The report is the only
  thing check 21 reads, so a report that did not run would otherwise look exactly like a clean
  corpus. An adopter whose generator is a fork must carry the mode, or this check names that first.
- A record written after the causes seed also carries `**Caused-by:** <target>` within those first
  unfenced lines (`tree_lib.py`'s `BIND_HEAD_LINES`), directly under its Serves line: `<target>` is a
  family id the corpus defines or a record key, bare, never pinned `@rev-N` and never an `N..M` run.
  `gov_record.py new <kind> --caused-by <target>` is the door that writes it. `record_causes.py --check`
  reds a new record that names none (`TOOL-dTotalRecall-19`), and its writer census reds a code file
  that spells a Serves line and no cause (`TOOL-dTotalRecall-36`). A non-Markdown record writes its cause
  line behind the comment prefix its Serves line uses, `# **Caused-by:** <target>` under a
  `# **Serves:**` line, and a cause or made-by line whose prefix differs from its Serves line's is
  refused (`TOOL-dTotalRecall-51`).

**Deviation records.** A departure from the frozen design, or from a spec once its code has started,
is a `deviation` record named `<date>-build-<unit id>-deviation-<n>.md` in the departing build's
`build/` folder, `<n>` unique within its build; check 21 joins that kind to that name both ways, each
mismatch an `A` row. Its fields are `- **<Key>:** <value>` bullets, one line each: Departs from
(`<clause id>@<hash8>`, `<unit>@rev-N` or a build slug, an optional ` [<section>]` tail), Hand-off
(`design-to-spec` · `design-revised` · `spec-revised` · `spec-to-code` · `code-to-record`), Before,
After, Cause (`design defect` · `owner ruling` · `builder discovery` · `review finding` · `external`),
Reason, Evidence, Risk (`editorial` · `additive` · `stricter` · `loosening` · `breaking`), Approver
(opening `author`, `spec writer` or `owner`, then where the approval is recorded), Follow-through
(`amends <clause id>@<hash8>` · `supersedes <clause id>@<hash8> by <clause id>` · `new unit <id>` ·
`gap <key>` · `ask <id>` · `usage <key>`) and Caused-by (one id), with Bound, Tier, Surface and
Supersedes optional. Supersedes holds one record id, the stem `<date>-build-<unit id>-deviation-<n>`
of another record, and orders two amends of one clause: the newer names the older there. The
as-built view's row for a clause whose records' After texts all agree is cited by the later file by
path; where they differ, the head supplies it, the one record no other names in Supersedes, whatever
its path. A set left with two or more such records, or none, is an `unordered amends of <clause>`
finding naming every one, and a Supersedes naming a record outside its clause's set a finding naming
both; either renders the clause from the baseline, and neither path order nor a commit date decides.
`deviation_join.py` computes the departures from history and joins each to its record. An
approver is graded under one of two values: `author-recorded`, the default, passes a role the grammar
names, and an owner only citing a decision row held on the mainline the remote ladder resolves that
names the departed clause or the new unit; `by-risk` also refuses a role below the risk class, `editorial` needing an `author`,
`additive` and `stricter` a `spec writer`, and `loosening`, `breaking` or a cause of `owner ruling` the
`owner`. An approval carried for the owner's walk has a decline route: an owner decline is filed as an
ask naming the record, and its follow-up is a new record naming the declined one in Supersedes, the
as-built view re-rendered in that commit, so no landed record keeps citing a withdrawn approval
(`TOOL-dTrueNorth-20`).

**Red-fix records.** An inline red fix, a commit carrying a `Red-fix: <leg name>` trailer, is recorded
after the fix by a `red-fix` record named `<date>-build-<unit id>-red-fix-<n>.md` in a build's `build/`
folder, under the unit whose pass the red followed, or a unit of the build that last changed the fixed
file. Its fields are `- **<Key>:** <value>` bullets, one line each and all required: Leg (the leg's
name as the trailer spells it), Red line (the line of the failure the fix clears), Files (the commit's
paths, sorted, joined by a comma and a space), Commit (the fix commit's full 40-hex sha), Rerun (the
command that showed the leg green, and its result) and Caused-by (one id). Write it through the door,
`build_records.py new red-fix --build <slug> --unit <id> --leg <leg name> --red-line <line> --commit
<rev> --rerun <command and result>`, which derives Files and Commit from the commit and refuses a
commit carrying no trailer naming that leg. Check 31 joins every such commit to its record. A path-less
commit carrying the trailer, an empty commit or any merge, owes no red-fix record: its `Files` would be
the change it accounts for and it holds none, so the door refuses it saying so and check 31 asks none.

**Disposition records.** The owner's answer to a held loop item is a `disposition` record named
`<date>-build-<unit id>-disposition-<n>.md` in a build's `build/` folder, under the unit the item
belongs to, or the build's first unit for an item no unit owns. Its fields are `- **<Key>:** <value>`
bullets, one line each: Item (the disposed item's tag, opening `item.`), Disposition (one word, a
member of that item's closed outcome set), Channel (`mailbox` · `terminal` · `prompt`, where the owner
answered) and Caused-by (one id), with Reason optional. Write it through the door, `build_records.py
new disposition --build <slug> --unit <id> --item <tag> --disposition <word> --channel <channel>
[--reason <text>]`, which refuses a value outside those shapes. The door does not read the item's
outcome set: that join is the loop kit's `check_disposition_record`, run by whoever reads the record.

**Acceptance records.** A unit's acceptance commands re-run at one commit are an `acceptance` record
named `<date>-build-<unit id>-acceptance-<n>.md` in a build's `build/` folder. Its fields are
`- **<Key>:** <value>` bullets, one line each and all required: Sha (the full 40-hex commit the re-run
read), Writer (`executor` · `stand-in`) and Caused-by (the unit). After one blank line come its run
lines, one per command, `run · <exit> · <hash> · <command>`: the exit an integer or `timeout`, the
hash the first twelve hex digits of the SHA-256 of the command's combined output after the run-gates kit's `write_normaliser` program strips its roots and durations. A record with no
run line, or with a line opening `run ·` outside that grammar, is malformed. It has no door: the
lines are computed, never typed, by the loop kit's `loop_witness.py acceptance` until an executor
writes it, and a hand-typed record reads malformed wherever it lacks them.

**Transition records.** A build's stage move is a `transition` record named
`<date>-build-<anchor id>-transition-<n>.md` in the build's `build/` folder, the anchor the lowest unit
id a spec H1 under the build defines, `<n>` following the move order. Its fields are
`- **<Key>:** <value>` bullets, one line each: Build, From and To (one state word each), Item (the exit
item's tag) and Sha (eight to forty hex digits, the witness commit), all required, then any extension
field the move carries, its name capitalised (`Stand-in`). It has no door: the loop kit's
`loop_transition.py record` writes it from the move, beside the move's `Gov-Transition` trailer, and
its `check` holds the record to that trailer field by field. A move made before the build's first spec
writes no record; the next move after it back-fills one per earlier trailer.

**Recommendation records.** A stage exit's review recommendation is a `recommendation` record named
`<date>-build-<anchor id>-recommendation-<n>.md` in the build's `build/` folder, the anchor the lowest unit
id of the build README's generated units region, `<n>` following the order written, so a stage scored
twice keeps both. Its fields are `- **<Key>:** <value>` bullets, one line each: Stage, Source and Role (one
word each), Score (`review` · `no-review` · `unarmed` · `none`), Binds (`yes` · `no`), Reason and
Caused-by, all required, and exactly one of Signals and Answers. A SCORE record carries Signals, the
signals that held or `none`, and Role `command`; a REASON record carries Answers, the stem of the score
record it answers, and the answering role. Write it through the door, `build_records.py new
recommendation --build <slug> --unit <id> --stage <stage> --score <score> --source <source> --binds
yes|no --reason <text> --role <role> [--signals <text>] [--answers <stem>]`, which refuses a value outside
those shapes and an Answers naming no recommendation record of the build. The unattended driver's
`--recommend` calls it; the newest score record of a stage and the reason answering it are the pair
that decides.

## Record kinds — the registry's view

Every record kind is declared once, as a `[[record-kind]]` row of `{{KIT_DIR}}/record-kinds.toml`; the
table below is GENERATED from it by `python {{KIT_DIR}}/record_kinds.py --write`, and the `record-kinds`
leg reds it when it differs by one byte. A kind joins through `record_kinds.py new`, never by an edit here.
The `Purpose` cell is the row's declared purpose, `—` while it is pending on an owner ask or a ledger.

<!-- gen:record-kinds -->

57 kinds · 28 purposes pending

| Kind | Tag | Home | Writer | Read by | Written by | Check | Purpose |
|---|---|---|---|---|---|---|---|
| `spec` | `record.spec` | `memory/builds/*/spec/*.md` | `gov_record.py new spec` | `gov-builder`, `gov-diff-reviewer`, `gov-skeptic`, `gov-spec-reviewer`, `gov-spec-writer`, `gov-synthesizer`, `gov-tester` | `gov-spec-writer` | `memory hygiene` | its writer is `design.unit-spec`; the spec redesigned as a structured, tagged contract |
| `build-readme` | `record.build-readme` | `memory/builds/*/README.md` | `gov_record.py new build-readme` | — | — | `memory hygiene` | the build README's declared front-matter schema, with unknown keys refused; writer item not named |
| `spec-audit` | `record.spec-audit` | `memory/builds/*/reviews/*.md` | `tier2-review.js` | — | `gov-synthesizer` | `memory hygiene` | — |
| `diff-review` | `record.diff-review` | `memory/builds/*/reviews/*.md` | `tier2-review.js` | — | `gov-synthesizer` | `memory hygiene` | — |
| `log` | `record.log` | `memory/builds/*/prompts/*.md` | `gov_record.py new log` | `gov-builder`, `gov-orienter`, `gov-researcher`, `gov-session`, `gov-spec-reviewer`, `gov-spec-writer` | — | `memory hygiene` | the journal grammar moved into the core; writer item not named |
| `research` | `record.research` | `memory/builds/*/build/*.md` | `gov_record.py new research` | — | — | `memory hygiene` | — |
| `run-record` | `record.run-record` | `memory/builds/*/build/*-runlog-*.md` | `runlog.py record --write` | — | — | `runlog record schema` | observability's journal reader writes it when the journal shows a run closed, as `observability.run-record` says |
| `backlog-row` | `record.backlog-row` | `memory/backlog/*.md` | `hand` | — | — | `memory hygiene` | the ask register's row store; the memory contract declares it; writer item not named |
| `design-record` | `record.design-record` | `memory/builds/*/build/*-architecture-v*.md` | `gov_record.py new design-record` | — | — | `memory hygiene` | a core memory kind with no writer item; the memory contract declares it |
| `dossier` | `record.dossier` | `memory/map/features/*.md` | `hand` | — | — | `codebase-map gate coverage` | dossiers anchored to symbol keys; its writer, where the map is installed, is `build.unit-pass`, the claiming dossier's |
| `deviation` | `record.deviation` | `memory/builds/*/build/*-build-*-deviation-*.md` | `gov_record.py new deviation` | — | — | `memory hygiene` | the record kept in its departing build's `build/` folder, read by the deviation join, the as-built view |
| `exception` | `record.exception` | `memory/builds/*/build/*-build-*-exception-*.md` | `build_records.py new exception` | — | — | `memory hygiene` | the exception register, kept in the building build's `build/` folder as a deviation record is; writer item not named |
| `override` | `record.override` | `memory/builds/*/build/*-build-*-override-*.md` | `build_records.py new override` | — | — | `memory hygiene` | `charter.override` and its record, under the precedence and override rule, the record kept in the building build's |
| `change` | `record.change` | `memory/builds/*/build/*-build-*-change-*.md` | `build_records.py new change` | — | — | `memory hygiene` | — |
| `red-fix` | `record.red-fix` | `memory/builds/*/build/*-build-*-red-fix-*.md` | `build_records.py new red-fix` | — | — | `memory hygiene` | — |
| `disposition` | `record.disposition` | `memory/builds/*/build/*-build-*-disposition-*.md` | `build_records.py new disposition` | — | `item.entry.place-owner`, `item.build.ratify` | `memory hygiene` | the owner's disposition record, written by whichever channel carried it: the mailbox, a terminal command or a prompt. |
| `acceptance` | `record.acceptance` | `memory/builds/*/build/*-build-*-acceptance-*.md` | `loop_witness.py acceptance` | — | `item.build.acceptance` | `memory hygiene` | its writer is `build.acceptance`; dDeclaredLoop builds the witnesses computed rather than typed, the acceptance re-run |
| `transition` | `record.transition` | `memory/builds/*/build/*-build-*-transition-*.md` | `loop_transition.py record` | — | `item.plan.exit`, `item.design.exit`, `item.build.exit`, `item.test.exit`, `item.deploy.close` | `memory hygiene` | the transition record three ways; every step's exit item writes it: `plan.exit`, `design.exit`, `build.exit` |
| `recommendation` | `record.recommendation` | `memory/builds/*/build/*-build-*-recommendation-*.md` | `build_records.py new recommendation` | — | `item.plan.recommend`, `item.design.recommend`, `item.build.recommend`, `item.test.recommend`, `item.deploy.recommend` | `memory hygiene` | every `*.recommend` item writes it; the stage-exit recommendation is one mechanism, dDeclaredLoop's (AF-1) |
| `widen` | `record.widen` | `memory/builds/*/build/*-build-*-widen-*.md` | `ratchet.py widen` | — | — | `memory hygiene` | — |
| `leg-tail` | `record.leg-tail` | `memory/builds/*/build/*-build-*-leg-tail-*.md` | `keep_tails.py` | — | — | `memory hygiene` | — |
| `flake` | `record.flake` | `memory/builds/*/build/*-build-*-flake-*.md` | `verdict_flow.py flakes` | — | `item.test.flakes` | `memory hygiene` | its writer is `test.flakes`; flake quarantine |
| `gate-health` | `record.gate-health` | `memory/builds/*/build/*-build-*-gate-health-*.md` | `drift_report.py --gate-health --write` | — | — | `memory hygiene` | — |
| `card` | `record.card` | `memory/builds/*/build/*-build-*-card-*.md` | `manifest-check.sh --card --follow` | — | — | `memory hygiene` | the build's orientation card at level 1, its stores and snapshot; its writer is `entry.orient`, which composes it |
| `probe-trigger` | `record.probe-trigger` | `memory/builds/*/build/*-build-*-probe-trigger-*.md` | `probe.py trigger` | — | `item.probe.trigger` | `memory hygiene` | its writer is `probe.trigger`: why the probe opened, keyed by the boundary or the raising return, or by content for a |
| `probe` | `record.probe` | `memory/builds/*/build/*-build-*-probe-*.md` | `probe.py pin` | — | `item.probe.pin`, `item.probe.run`, `item.probe.judge`, `item.probe.return` | `memory hygiene` | its writer is `probe.return`: one record per probe, its kind a verification, a reproduction or an experiment, an |
| `mailbox-message` | `record.mailbox-message` | `memory/builds/*/build/*-build-*-mailbox-message-*.md` | `loop_transition.py record` | — | — | `memory hygiene` | one mailbox message a build's transition disposed, its fields and its body in one fenced block |
| `view` | `record.view` | `memory/LIVE.md`, `memory/ledger/*.md`, `memory/map/generated/*` | `gen_build_index.py --write` | — | — | `memory hygiene` | a generated view: LIVE.md, the ledger, the ask views; re-rendered, never merged (the away pass); writer item not named |
| `registry` | `record.registry` | `memory/project/*.txt`, `memory/project/*.toml` | `hand` | — | — | `ratchet (never gains)` | a gate's row registry under `memory/project/`, written by its gate's pin emitter (the away pass); writer item not named |
| `archive` | `record.archive` | `memory/archive/**` | `hand` | — | — | `memory hygiene` | a rotated record under `memory/archive/`, written by rotation (the away pass); writer item not named |
| `instrument` | `record.instrument` | `memory/builds/*/build/*.py`, `memory/builds/*/build/*.sh`, `memory/builds/*/build/*.js`, `memory/builds/*/build/*.json`, `memory/builds/*/build/*.tsv`, `memory/builds/*/build/*.txt`, `memory/builds/*/build/*.svg`, `memory/builds/*/build/*.html`, `memory/builds/*/build/*.log`, `memory/builds/*/build/*.out` | `hand` | — | — | `memory hygiene` | a script, table or drawing kept beside the record it serves (the away pass); writer item not named: the session that |
| `witness` | `record.witness` | `refs/gov/**` | `gov-ref.sh` | — | — | `record-kinds` | a declared pocket outside the tree, such as a transcript, a Codex rollout, the auto-memory, the live inbox or a |
| `claim` | `record.claim` | `refs/gov/claims/**` | `gov-claim.sh` | — | — | `build-index selftest` | the claim ref on the remote and the ask-family counter ref (`gap-mem-13`); `entry.claim` writes the claim |
| `orientation-cards` | `record.orientation-cards` | `<git-common-dir>/orientation/*` | `manifest-check.sh --card` | `gov-builder`, `gov-reuse-scout`, `gov-session`, `gov-spec-writer` | — | `record-kinds` | — |
| `unattended-sidecars` | `record.unattended-sidecars` | `<git-common-dir>/unattended/*`, `<git-common-dir>/unattended-landed` | `unattended.sh` | — | — | `record-kinds` | — |
| `runlog-journal` | `record.runlog-journal` | `<git-common-dir>/runlog/*`, `<git-common-dir>/runlog-stamp-*` | `runlog.py` | — | — | `record-kinds` | — |
| `drift-history` | `record.drift-history` | `<git-common-dir>/drift-history.tsv` | `drift_report.py` | — | — | `record-kinds` | — |
| `gate-ledger` | `record.gate-ledger` | `<git-common-dir>/gate-*`, `<git-common-dir>/pre-push-*`, `<git-common-dir>/selftest-baseline` | `run-gates.sh` | — | — | `record-kinds` | — |
| `history-verdicts` | `record.history-verdicts` | `<git-common-dir>/history-verdicts/*` | `history_store.py` | — | — | `record-kinds` | — |
| `health-logs` | `record.health-logs` | `<git-common-dir>/health.log`, `<git-common-dir>/procmon-stamp` | `health-log.sh` | — | — | `record-kinds` | — |
| `hook-state` | `record.hook-state` | `<git-common-dir>/agent-cap/*` | `agent-cap.js` | — | — | `record-kinds` | — |
| `reuse-lookups` | `record.reuse-lookups` | `<git-common-dir>/codebase-map/*` | `reuse_lookup.py` | — | — | `record-kinds` | — |
| `recall-cache` | `record.recall-cache` | `<git-common-dir>/recall/*` | `query.py` | — | — | `record-kinds` | — |
| `review-lenses` | `record.review-lenses` | `<git-common-dir>/review-lenses/*` | `tier2-review.js` | — | — | `record-kinds` | — |
| `transition-cache` | `record.transition-cache` | `<git-common-dir>/transition-audit-cache` | `transition_audit.py` | — | — | `record-kinds` | — |
| `recovery-manifests` | `record.recovery-manifests` | `<git-common-dir>/recovery-manifests/*` | `branch_reconcile.py` | — | — | `record-kinds` | — |
| `gov-index` | `record.gov-index` | `<git-common-dir>/gov/*` | `tag_index.py` | — | — | `record-kinds` | — |
| `gov-feed` | `record.gov-feed` | `<git-common-dir>/gov-feed.*`, `<git-common-dir>/gov-last-fetch` | `gov-feed.sh` | — | — | `record-kinds` | — |
| `handoff-calls` | `record.handoff-calls` | `<git-common-dir>/handoff-calls/*` | `handoff.py` | — | — | `record-kinds` | — |
| `index-render-stamp` | `record.index-render-stamp` | `<git-common-dir>/gen-build-index-render-stamp` | `gen_build_index.py` | — | — | `record-kinds` | — |
| `git-client-state` | `record.git-client-state` | `<git-common-dir>/sourcetreeconfig.json` | `hand` | — | — | `record-kinds` | — |
| `stream-plan` | `record.stream-plan` | `memory/builds/*/build/*-stream-plan-*.md` | `hand` | — | — | `record-kinds` | a build's units grouped into ordered streams, written by dIndexedDesign's planner, read by dWellOiledMachine's pick |
| `ask` | `record.ask` | `memory/builds/*/BACKLOG.md` | `gov_record.py new ask` | — | — | `memory hygiene` | the ask kind's acceptance at filing; its writers are the items that file asks, each filing stating its acceptance |
| `shape-run` | `record.shape-run` | `memory/builds/*/build/*-build-*-shape-run-*.md` | `gov_record.py new shape-run` | — | — | `shape-run records (each record equals its review line)` | one review exit's review-shape line as typed fields, compared back to that line by shape_run.py |
| `code` | `record.code` | `<git-common-dir>/gov/index-s*.db` | `generator:{prefix}/playbook/code_record.py` | — | — | `code record` | what a tree's code defines, calls, invokes and registers, derived per blob and cached by tree hash |
| `request-records` | `record.request-records` | `<git-common-dir>/requests/*` | `request.py` | — | — | `record-kinds` | — |
| `session-registry` | `record.session-registry` | `<git-common-dir>/procmon/*` | `tether.py` | — | — | `record-kinds` | — |

<!-- /gen:record-kinds -->

## Acceptance ledger — how a built unit evidences its criteria

Inside a record whose `**Serves:**` kind is `log`, which is already defined as evidence of what
was built, or its read-only alias `journal`, graded alike. Two further arms once the SPEC's filename
date reaches `LEDGER_LABEL_CUTOFF` and
`LEDGER_TOKEN_CUTOFF`: an answer whose criterion label the spec does not number is a finding, and an
answer must share a backticked token with the criterion it answers, case-folded and either way round.
Both are branches of the same check, so a blank `ACCEPTANCE_LEDGER_CUTOFF` disarms them too. One `**Evidences:**` line per unit, and one line per criterion beneath it:

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
- Under `--staged` it grades the closed units a staged spec or a staged log record names,
  against the records of their own build folders. A record in another build that evidences one of
  them is read only by the full run.

**The seen-red line** (TOOL-dWitnessedBar-7) records a gate seen red, one line per arm the main loop
observed red on its staged break and green once restored, under the `**Evidences:**` block of the
unit that adds or changes the gate:

```
- seen-red — `<leg name>` — red `<sha>` — green `<sha>` — <the staged break>
```

The leg is its manifest `name`, each SHA 8 to 40 lowercase hex, the break one line of prose; `red` is
the commit the break was staged over, `green` the one the arm read green at once restored. It is no
answer to a criterion and no third form: it closes the answer above it, so check 23 joins none of its
tokens to that answer's. `seen_red.py --build <slug>` reads it back, one line per gate the build adds
or changes, and refuses a line opening `- seen-red` in any other shape.

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
the walk, so one bad gate cannot hide every other gate's findings. A BLANK `ARMS_FLOORS` is refused while any gate
is discovered, since both floor arms would iterate nothing; `check-arms.py --emit-floors` prints the
measured line to declare.

`{{KIT_DIR}}/check-arms.py --report` shows every branch, its line, its signature and its state.

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

The review harness acquires the classes a diff can hit on its own: on the diff kind, `tier2-review.js`
given no `checklist` runs the command below and hands its stdout to the lenses. A reader who wants the
checklist runs it by hand:

```bash
python {{KIT_DIR}}/gotchas.py --for-diff <base>..<head>
```

Its stdout IS the checklist. A checklist nobody can finish is not a checklist.

A record is a `kind: class` (the default), a `note`, a `superseded` class, or a `kind: invariant`: a
ruling a reviewer keeps mistaking for a bug. An invariant carries a `decision:` key naming the ruling
and five sections, `## Looks wrong`, `## Actually`, `## Do`, `## Do not` and `## Guarded by`; its
anchors select it exactly as a class's do. The checklist ends with the by-design block, printed on
every non-empty selection, `0` included:

```text
# by design — 1 invariant(s) this selection touches
- <name> — <looks wrong> → <actually> (<decision id>)
```

The review harness cuts that block out of `checklist` and hands it to every lens and skeptic as
intended behaviour, so a reviewer refutes a finding the ruling covers instead of re-reporting it.

The block is read at the subject's BASE, so a change cannot write its own exemption: `--for-diff`
reads it at the commit its range diffs from, and `--for-paths --base <rev>` at that revision. An
invariant the subject adds, edits or takes out prints as a checklist item instead, and a header line
names the base and how many there were:

```text
- [ ] NEW/CHANGED invariant <name> — verify the ruling before treating it as by design
```

`--for-paths` with no base reads the working tree, and its header line says so.

## Codebase-map interop

If the codebase-map kit is adopted with its `MAP_ROOT` a DIRECT child of this tree (e.g.
`<MEMORY_ROOT>/map`), that subtree is sanctioned automatically (the scripts read
`.codebase-map.conf`): allowed entries are `README.md`, `FOUNDATION.md`, `baseline.txt`,
`affordance-exempt.txt` (the codebase-map kit renders it; a gate that did not sanction it reds a
freshly-adopted map),
`features/`, `generated/`; `README.md`,
`FOUNDATION.md` and `features/*.md` carry check 6's size caps but are entry-budget exempt (check 7) —
dossiers are detail files. The two split across CLASSES: `features/*.md` take `DOSSIER_CAP_*`, while
`README.md` and `FOUNDATION.md` take `INDEX_CAP_*` like any other row document. A `features/*.md` over
its cap is SPLIT into two dossiers (never rotated; the map gate requires `FOUNDATION.md` in place), and
that class is deliberately kept tighter than the index class because a split is the only remedy a
dossier has and check 6 is the only size gate it has. The map's
coverage/freshness enforcement is its own test file, not this script.
[/{{MEMORY_ROOT}}/HYGIENE.md]
