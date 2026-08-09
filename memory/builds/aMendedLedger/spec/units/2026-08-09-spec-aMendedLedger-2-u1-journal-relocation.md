# TOOL-aMendedLedger-2 — U1: the journal relocation pass, plus the three .md stub deletions

**Status:** SPECCED · rev-2 · 2026-08-09 · node a · Tier-2 · base 663ca427 · streams tooling

## 1. Goal

Relocate both session journals out of `memory/project/journal/` into build folders under the
master's relocate-not-delete rule, give `bThriftyBellows` the stub build folder its slug has no home
for, and delete the three `memory/project/*.md` stubs plus `memory/project/journal/.gitkeep` in the
SAME commit — because `memory/project/MEMORY.md:4` holds a live relative link into `journal/` and
hygiene check 2 is full-tree at the push boundary.

## 2. Scope (IN)

- **S1** `git mv memory/project/journal/2026-07-16-bThriftyBellows.md` to
  `memory/builds/bThriftyBellows/build/2026-07-16-build-bThriftyBellows-1.md`, creating the stub
  build folder.
- **S2** `git mv memory/project/journal/2026-07-15-aRuledParchment.md` to
  `memory/builds/aRuledParchment/build/2026-07-15-build-aRuledParchment-1.md`. That build folder
  already exists and holds `README.md` + `spec/` only; `build/` is new.
- **S3** Author `memory/builds/bThriftyBellows/README.md` with front matter carrying an authored
  `status: CLOSED`, and write NO spec under that folder.
- **S4** Fold `memory/project/MEMORY.md:4`'s digest into the relocated `bThriftyBellows` recording as
  plain prose, with the markdown link removed and not in a record-anchor shape.
- **S5** Delete `memory/project/MEMORY.md`, `memory/project/IN-FLIGHT.md`,
  `memory/project/README.md` and `memory/project/journal/.gitkeep`, in the commit that performs S1
  and S2.
- **S6** Create `memory/archive/ledger/README.md` carrying `memory/project/IN-FLIGHT.md:3`'s protocol
  prose, marked RETIRED, so nothing is lost between this unit and U2.
- **S7** Run `python tools/memory-tree/gen_build_index.py --write` inside this commit and stage every
  artifact it rewrites.

## 3. Non-goals (OUT)

- **`memory/project/in-flight/`** — the three shards and `in-flight/.gitkeep` are U2's, and they are
  what keeps the `drift-audit` ledger probe alive until U2+U4 land together.
- **Any edit to `tools/memory-tree/check-memory-hygiene.sh`.** Check 3 still admits `D:journal`,
  `F:MEMORY.md` and `F:IN-FLIGHT.md` after this unit; those arms go dormant, not red. Two edits to
  that file are U3's and neither may be taken here: tightening the `F:*.md` catch-all at `:229`
  (master §8 F1, `RESOLVED (build, 2026-08-09)`) and rebuilding the `ex7` expression at `:345-346`
  as base-plus-append (master §8 F6, `RESOLVED (build, 2026-08-09)` — the master's rev-2 Non-goal
  covering it is gone at rev-4, so the temptation to "just do it while here" is now live). Touching
  that file would owe the `KIT_MEMORY_TREE_VERSION` bump in three places plus a `--render`, and a
  kickoff-manifest re-stamp.
- **`adopt-memory-tree.sh`** — it still scaffolds `project/journal/`, `MEMORY.md`, `IN-FLIGHT.md` and
  `project/README.md` at `:38`, `:79-93`. Retiring that is U3, in lockstep with the gate.
- **Doc truth.** `memory/README.md:23` and `memory/HYGIENE.md:5, :28, :60-61, :74, :81` and `:93` name
  files this unit deletes — the same six `memory/HYGIENE.md` line sites the master's §4 Files touched
  lists at `…-1.md:195-196`, not the two rev-1 named. They are prose, not links, so no gate reds, and
  that holds tree-wide: the only markdown link into the doomed set anywhere under `memory/` is
  `memory/project/MEMORY.md:4` itself (`memory/README.md:23` links the `project/` DIRECTORY, and check
  2's awk at `:187` matches only targets containing `.md`). The master files all of it under U6.
- **`memory/DECISIONS.md`.** It is append-only. The dead journal pointer at `:19` and the false
  "lives in the bug-class catalogue" claim at `:45` are superseded by an appended row in U7 (master
  S8), never by an edit here. `memory/backlog/TOOL.md:5` repeats that claim and is U7's too.
- **Deleting either journal**, and **naming a relocated file with a `-journal` tail** — see §4
  Alternatives rejected.

## 4. Design

### Inventory

`git ls-files memory/project` at HEAD `dae75003` returns 15 tracked paths. U1 touches six: two
journals moved, three `.md` stubs deleted, `journal/.gitkeep` deleted. The five `*.txt` registries and
the four `in-flight/` paths are untouched, so `memory/project/` still holds nine tracked paths when
this commit lands.

| file | lines | what is durable in it |
|---|---|---|
| `memory/project/MEMORY.md` | 4 | line 4 only: the digest, which is also the link forcing atomicity |
| `memory/project/IN-FLIGHT.md` | 3 | line 3 only: write-own/read-all, the row shape, the status vocabulary, self-prune |
| `memory/project/README.md` | 5 | nothing — it describes `MEMORY.md`, `IN-FLIGHT.md`/`in-flight/` and `journal/`, and already omits the five registries |

Counts are `wc -l`, re-measured at HEAD: `3 411`, `4 318`, `5 241` bytes respectively.

### The atomicity rule, verified against source

`check-memory-hygiene.sh:163` builds check 2's population from `git ls-files "$M/"` filtered to
`.md`, minus `DECISIONS.md`, `decisions/` and `archive/`. It is narrowed to the staged set ONLY under
`--staged` (`:164`), and `.githooks/pre-push` runs the full bar, so at the push boundary check 2 is
full-tree. The awk at `:187` matches every inline-markdown link target containing `.md`, and `:200`
resolves it with `[ -f "$d/$t" ]`, where `d` is the citing file's own directory (`:199`). Code spans
are NOT excluded — only fenced blocks are (`:181-186`) — so a link-shaped string inside backticks is
scanned too, which is why this spec spells such targets out in prose rather than reproducing them.

`memory/project/MEMORY.md:4` is a bulleted index entry whose link target is
`journal/2026-07-16-bThriftyBellows.md`, resolving to
`memory/project/journal/2026-07-16-bThriftyBellows.md`. So a commit that moves that journal and keeps
`MEMORY.md` reds check 2, and a commit that deletes `MEMORY.md` first leaves the journal unowned.
Both halves land in one commit.

Nothing grandfathers the link out: `memory/project/legacy-files.txt:2-6` lists five `aRatchetForge` /
`aDeployScout` / `aLeanRework` recordings and no `memory/project/` path, and
`memory/project/curation-debt.txt` is empty but for its comment. Consequently the stale-line guards
at `check-memory-hygiene.sh:662-673`, which fail when a listed path disappears, stay silent through
all four deletions.

`index_set()` at `:303` echoes `$M/project/MEMORY.md` and `$M/project/IN-FLIGHT.md` unconditionally
at `:307`, but the whole set is filtered through `[ -f "$f" ]` at `:319`. Their deletion therefore
drops them out of checks 6 and 7 instead of redding them, which is exactly why U1 needs no gate edit
and stays off both couplings named in §7.

### Migration

| path | action | destination |
|---|---|---|
| `memory/project/journal/2026-07-16-bThriftyBellows.md` | `git mv` | `memory/builds/bThriftyBellows/build/2026-07-16-build-bThriftyBellows-1.md` |
| `memory/project/journal/2026-07-15-aRuledParchment.md` | `git mv` | `memory/builds/aRuledParchment/build/2026-07-15-build-aRuledParchment-1.md` |
| `memory/project/MEMORY.md` | delete, digest folded first | — |
| `memory/project/IN-FLIGHT.md` | delete, prose moved first | `memory/archive/ledger/README.md` |
| `memory/project/README.md` | delete | — |
| `memory/project/journal/.gitkeep` | delete with its directory | — |

**The stub `README.md` takes an authored `status: CLOSED` and NO spec.** The reason is mechanical, at
`tools/memory-tree/gen_build_index.py:185-199`:

- `collect()` builds each build's unit list from `spec/` only (`:229`), and the module docstring at
  `:15` states outright that `build/` and `reviews/` are never scanned. A relocated `build/`
  recording therefore contributes no `**Status:**` header, and `parsed` in `derive_status` is empty.
- With `parsed` empty and no `status` key, `:189-192` raises a named `Problem` telling you to declare
  it; with the key present, `:193` returns it verbatim. That is the sanctioned route for a build
  whose only recording carries no header.
- Authoring a spec instead flips the branch: `parsed` becomes non-empty and an authored `status:` is
  then a hard error at `:194-199` — "two answers to one question is exactly the drift this index
  removes". The two routes are mutually exclusive by construction, so "spec plus authored status" is
  not an option and "spec, no status" would derive the build's status from a spec that never existed.
- It would also fabricate provenance. The work shipped 2026-07-16 with no spec; `SPEC_FORMAT_CUTOFF`
  is `2026-07-15`, so a spec dated then would have to satisfy check 12 as a plan for work already
  landed.

The front matter, exactly:

```
---
slug: bThriftyBellows
node: b
opened: 2026-07-16
streams: tooling
roster: TOOL
ids: TOOL-bThriftyBellows-1/-2
status: CLOSED
---
```

`REQUIRED_KEYS` at `:56` is `slug node opened streams roster ids`; `status` is validated against
`STATUS_TOKENS` at `:149-150`; `streams` and `roster` against the `.memory-tree.conf` enums at
`:223-228` (`tooling` and `TOOL` are both members). The body follows the shape of
`memory/builds/aRuledParchment/README.md` — H1, a node/opened/streams line, the "records live under"
sentence — and MUST carry the
`<!-- gen:build-index -->` / `<!-- /gen:build-index -->` marker pair, which `apply_region` requires at
`:271-273`. Any relative link written into that body must resolve from
`memory/builds/bThriftyBellows/`; `builds/` is not exempt from check 2.

**The digest fold.** `memory/project/MEMORY.md:4` is a linked index entry. It folds into the relocated
`bThriftyBellows` recording as prose with the markdown link deleted — the link target is the file
itself, and a `.md` target is precisely what check 2's awk picks up. It must also not be written as
`- TOOL-bThriftyBellows-1 · …`, and the reason is RETRIEVAL, not a gate. That shape is a record
ANCHOR under two of the recall grammar's four regexes — `A_BOLD_LI` at
`tools/memory-recall/extract.py:88` (a dash bullet whose id is followed by `-`, `—`, `:` or `·`) and
`A_DASH` at `:92` (`·` or `|`) — so the recall index would carry the folded digest as a SECOND record
for an id whose durable home is the row at `memory/DECISIONS.md:19`, and a query for
`TOOL-bThriftyBellows-1` would return two half-records instead of one. Written as prose, the id
appears only as a citation and the single durable anchor stands.

The gate fact is adjacent and must be stated separately, because it does NOT carry that rule:
**check 13 is unaffected by the anchor shape either way.** It is not a duplicate-definition check —
`corpus_ids.py:340-342` fires only when one id is claimed by more than one BUILD FOLDER, and the
comment at `:337-339` says the exclusion is deliberate ("a decision-log row and its spec's H1 both
anchor the same id by design"). `walk()` records a build claim only when the citing path matches
`builds/<slug>/` (`:210`, `:218-219`), and `memory/DECISIONS.md` does not match, so a dash anchor
inside `memory/builds/bThriftyBellows/build/…` would be the FIRST build-folder claim for that id, not
a collision. The count is 0 before and 0 after. A builder who finds the stated reason false is
entitled to discard the rule, so the reason given is the one that holds.

The three facts that must survive verbatim in substance are the `2647s → 34s` figure, the
byte-identical golden-diff claim across three targets, and the banked negative "cache-and-grep is
SLOWER".

**Naming.** Both relocated files take the plain `<date>-build-<slug>-<seq>.md` form. Check 5 selects
them at `:284` and matches at `:294` — the `[[ $base =~ … ]]` test — against the closed grammar built
from `FAM_ALT` and `REC_TAIL` (`:109`); `:296` is the comment above the `fail 5` heredoc and asserts
nothing. A `-journal` tail would be legal under `REC_TAIL` and is not used, so the name matches every
other recording in the tree. Check 4's `rre` at `:255` does not govern these files: its awk registers
`F:` entries only for direct children of `builds/<slug>/`, and a file one level deeper registers as
`D:build`, which is in the `continue` allowlist inside `flush()` at `:265`.

### Generated artifacts

`gen_build_index.py --write` must run in this commit, after the moves and the new README are staged —
`collect()` reads `git ls-files` at `:210`, so an unstaged README makes the new build invisible and an
unstaged move leaves the old path in the index.

| artifact | effect |
|---|---|
| `memory/builds/bThriftyBellows/README.md` | region fills: `**Build status:** CLOSED · 0 unit(s) · node b · opened 2026-07-16 · streams tooling · ids TOOL-bThriftyBellows-1/-2`, then the "no spec carries a status header" sentence from `:258-260` |
| `memory/ledger/2026-07.md` | one added row. `render_shards` keys the month off `fm["opened"][:7]` (`:308`) and sorts by slug (`:320`), so the row lands after `bTamedTempest`. The file is LF-pinned by `.gitattributes` |
| `memory/LIVE.md` | UNCHANGED. `render_live` keeps only non-terminal builds (`:283`) and `TERMINAL` is `("CLOSED", "WONTDO")` at `:45` |
| `memory/builds/aRuledParchment/README.md` | UNCHANGED. Its unit table comes from `spec/` alone; U1 adds a `build/` recording |

Hygiene check 9 (`check-memory-hygiene.sh:420-427`) delegates to `--check`, which byte-compares every
artifact against a fresh render, so skipping `--write` reds the bar.

### Corpus effects, measured

`corpus_ids.py`'s present-tense corpus is
`^memory/(DECISIONS\.md|README\.md|HYGIENE\.md|TEMPLATE-SPEC\.md|LIVE\.md|backlog/|ledger/|project/|guides/)`
at `:198-201`, and anything outside it is skipped for dead-path classification at `:225`. Both
journals sit under `memory/project/` today and move OUT of that set, so `DEAD_PATH_PIN=0` can only
get safer, never worse.

Neither journal defines a record: `A_HEADING` requires two to six `#` (`extract.py:87`; `:86` is the
tail of the comment explaining why H1 is deliberately NOT an anchor) and `corpus_ids.py:194`'s
`h1_re` requires an id immediately after `# `, while both H1 lines open with a date, and `ARCH-` is
outside this repo's `FAMILIES`. The new README cites `TOOL-bThriftyBellows-1`,
which `memory/DECISIONS.md:19` anchors — `ID_RE` does not read the `/-2` tail as a second id, the same
shape `memory/builds/aRuledParchment/README.md:7` already carries. Measured at HEAD,
`python tools/memory-tree/corpus_ids.py --report` prints 51 defined, 56 cited, 5 orphan (the five
waived in `memory/project/id-orphan-waiver.txt`, matching `ORPHAN_ID_PIN=5`), 0 build collisions, 0
dead path cites. U1 moves none of those numbers.

### The archive README

`memory/archive/ledger/README.md` is created here, not in U2, so `IN-FLIGHT.md:3`'s protocol prose is
never absent from the tree. It carries the write-own/read-all rule, the row shape, the
`in-flight | merged:<sha>` vocabulary and the self-prune trigger, framed as RETIRED, and says the
shards land beside it in U2. Its gate surface is deliberately thin: `archive/` is excluded from check
2's population at `:163`, is inside `APPEND_ONLY_ERE` at `:47` so `corpus_ids` never classifies its
citations, is opaque to check 3 (the root entry is `D:archive`, allowed at `:212`), and is absent from
`index_set()` (`:303-320`) so it is under no byte or entry cap. Check 10 (`:429`) governs only
`archive/<INDEX>.<date>.md` rotation names and does not see this file.

**Unit boundary, stated because the master used to state it twice.** This file is created HERE on the
authority of the master's §4 Migration row for `IN-FLIGHT.md` (`…-1.md:138`), whose unit column reads
U1. The master's §4 Rollout row for U2+U4 (`…-1.md:174`) once claimed it too; at rev-4 that row reads
"its README is created in U1, per the Migration table — U2 must not re-create it", so the two agree.
U2 moves the three shards beside this README and neither re-creates nor clobbers it.

### Rollout

One commit, in this order:

1. Create `memory/builds/bThriftyBellows/build/`, `memory/builds/aRuledParchment/build/` and
   `memory/archive/ledger/` — `git mv` will not create a missing destination directory.
2. `git mv` both journals. Rename detection holds: `aRuledParchment` moves byte-identical, and
   `bThriftyBellows` gains one digest line against a file of roughly forty, far inside git's 50%
   similarity default.
3. Fold the digest. Author `memory/builds/bThriftyBellows/README.md` and
   `memory/archive/ledger/README.md`, both LF. `git add` them.
4. `git rm` the three `.md` stubs and `memory/project/journal/.gitkeep`.
5. `python tools/memory-tree/gen_build_index.py --write`; stage the two artifacts it rewrites.
6. `bash tools/run-gates.sh`; commit.

Steps 2 through 4 are one commit by the atomicity rule above; step 5 joins them because check 9
byte-compares the generated index against a fresh render inside the same run.

U1 stages none of the seven pathspecs on `.claude/SESSION-KICKOFF.md:6`
(`check-memory-hygiene.sh`, `check-template-size.sh`, `run-gates.sh`, `gate-legs.json`,
`manifest-check.sh`, `.memory-tree.conf`, `parallel-coding-governance.template.md`), so this commit
owes no `last-audit` re-stamp. It adds no gate leg, so `AGENTS.md` owes no bullet and
`handkept_inventories_disagreeing_with_source` (`tools/drift-audit/drift_signals.py:136`) stays at its
pin of 7.

### Files touched (estimate)

Moved: 2. New: `memory/builds/bThriftyBellows/README.md`, `memory/archive/ledger/README.md`.
Deleted: 4. Regenerated: `memory/builds/bThriftyBellows/README.md`'s marked region and
`memory/ledger/2026-07.md`. Asserted unchanged: `memory/LIVE.md`,
`memory/builds/aRuledParchment/README.md`. No file under `tools/` is touched.

### Alternatives rejected

- **Deleting either journal.** Both are sole carriers — the master's Migration table names the
  9-bullet optimization inventory, the golden-diff protocol and the banked negative for
  `bThriftyBellows`, and two sole-carried facts for `aRuledParchment`.
- **Splitting the deletions into a later commit.** Reds check 2 in one direction and orphans a live
  file in the other. This is the whole reason the three stub deletions sit in U1.
- **Authoring a stub spec for `bThriftyBellows`.** Forbidden in combination with `status:` at
  `gen_build_index.py:194-199`, and false provenance without it.
- **A `-journal` tail on the relocated names.** Legal under `REC_TAIL`; rejected so the names match
  every other recording in the tree.
- **Keeping `journal/.gitkeep` so the empty directory survives.** The directory has no remaining
  purpose, and U3 retires check 3's `D:journal` arm — leaving it would hand U3 an admitted empty
  directory to re-handle.
- **Re-homing the journals under `memory/archive/`.** `archive/` is where material a build cannot
  claim goes (`memory/HYGIENE.md:27` — the line sits inside the fenced tree diagram that opens at
  `:16` and closes at `:32`, so it is prose-by-picture and check 2 never scans it), and it is exempt
  from the link and cap checks. Both journals have a build that can claim them, and a build folder
  gives each an indexed owner.

## 5. Production-readiness checklist

- security — N/A. No auth, egress or sanitization surface; this unit moves two markdown files.
- perf / scale — N/A. Two moved files and one new build folder; no gate gains a walk.
- a11y — N/A. No user interface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — the one empty state is a build folder with zero header-carrying
  specs, which is the authored-`status:` route at `gen_build_index.py:185-193`; AC3 asserts it.
- observability — hygiene check 9 plus `gen_build_index.py --check` are the instrument, and both read
  `git ls-files`, so an unstaged step is visible rather than silent.
- risks — data-loss is the live risk and it is concentrated in one commit: `MEMORY.md:4` and
  `IN-FLIGHT.md:3` are each a sole carrier and are both deleted here. AC5 and AC6 assert each survived
  at its destination. Rollback is `git revert` of the single commit; there is no external state.
- testing + left-shift gates — no new gate leg; the full bar runs on the commit.
- migration / rollback — no adopter data moves and no kit file changes, so this unit has no adopter
  blast radius. Adopter-facing retirement is U3 and U6.
- user docs — none here. `memory/README.md:23` and the six `memory/HYGIENE.md` line sites in §3 are
  U6's.

## 6. Acceptance criteria

- **AC1** When `git ls-files memory/project` is run after this commit, it lists exactly nine paths —
  the five `*.txt` registries, `in-flight/.gitkeep` and `in-flight/{a,b,c}.md` — with no path under
  `journal/` and no `.md` file at `memory/project/` itself.
- **AC2** When
  `git log --follow -p --find-renames -- memory/builds/aRuledParchment/build/2026-07-15-build-aRuledParchment-1.md | grep -m1 'similarity index'`
  is run it prints `similarity index 100%`, over a diff naming
  `memory/project/journal/2026-07-15-aRuledParchment.md` as the source. The `-p` is the criterion, not
  decoration: `git log --follow` alone prints commit subjects, `similarity index` comes from the diff
  machinery and appears only under `-p`, `--summary` or `--raw`, and without it a builder cannot tell
  a 100% rename from a delete-plus-add — the one thing this AC exists to prove. The same pipeline over
  the `bThriftyBellows` destination prints a `similarity index` BELOW 100% (the fold adds a line;
  `git show -M --summary <commit>` names the same move as `rename … (NN%)`), and the diff's only added
  content is the folded digest. The master's AC2 (`…-1.md:273-275`) carries the corrected form.
- **AC3** When `python tools/memory-tree/gen_build_index.py --check` is run it exits 0,
  `memory/builds/bThriftyBellows/README.md` carries `status: CLOSED` in front matter, its generated
  region reads `0 unit(s)`, and `git ls-files memory/builds/bThriftyBellows/spec` returns nothing.
- **AC4** When `bash tools/memory-tree/check-memory-hygiene.sh` is run over the full tree it exits 0
  and check 2 reports no broken relative link — the assertion the atomicity rule exists for.
- **AC5** When `memory/builds/bThriftyBellows/build/2026-07-16-build-bThriftyBellows-1.md` is read, it
  carries the digest formerly at `memory/project/MEMORY.md:4` — the `2647s → 34s` figure, the
  byte-identical golden-diff claim, and the "cache-and-grep is SLOWER, don't retry" negative — as
  prose, with no markdown link and not in a record-anchor shape: no line of that file matches
  `A_BOLD_LI` or `A_DASH` on `TOOL-bThriftyBellows-1`.
- **AC6** When `memory/archive/ledger/README.md` is read, it carries `memory/project/IN-FLIGHT.md:3`'s
  write-own/read-all rule, its row shape, its `in-flight | merged:<sha>` vocabulary and its self-prune
  trigger, marked RETIRED, and names U2 as where the shards arrive.
- **AC7** When `git show --stat` is read for this commit, `memory/LIVE.md` and
  `memory/builds/aRuledParchment/README.md` are absent from it, and `memory/ledger/2026-07.md` shows
  exactly one added line.
- **AC8** When `python tools/memory-tree/corpus_ids.py --check` is run it exits 0, with orphan ids
  still 5 and dead path citations still 0.
- **AC9** When the commit's changed-path list is intersected with the seven pathspecs on
  `.claude/SESSION-KICKOFF.md:6`, the intersection is empty — so no `last-audit` re-stamp is owed and
  `bash skills/session-kickoff/manifest-check.sh --staged` passes without one.
- **AC10** When `bash tools/run-gates.sh` is run on this commit, all 38 legs are green.
- **AC11** When `git grep -l -F 'TOOL-aMendedLedger-' -- tools skills .claude parallel-coding-governance.*.md WIRE-INTO-PROJECT.md`
  is run after this commit it returns nothing, so
  `non_terminal_specs_cited_by_product_source` stays at its pin of 2 and
  `python tools/drift-audit/drift_report.py --check` exits 0. This unit writes no file under those
  globs at all, which is the cheapest way to hold the assertion; the AC exists so the H1 id this file
  now carries (`TOOL-aMendedLedger-2`) cannot leak into one as a provenance comment.

## 7. Gates

Existing legs that must stay green: `bash tools/run-gates.sh` in full, 38 legs at
`tools/gate-legs.json`. Load-bearing here — `memory hygiene (19 checks)`, and inside it checks 2, 3,
4, 5 and 9 plus the check-5 and check-6 stale-line guards; `build-index selftest`; `corpus-ids
selftest`; `codebase-map coverage + freshness`; `kickoff-manifest ratchet`. The manifest names the
recall legs `memory-recall kit selftest` and `memory-recall skill wiring` — rev-1 listed a
`memory-recall selftest` leg that does not exist. Neither is in fact load-bearing for U1: the kit
selftest reads its own fixtures rather than the live tree, and the wiring leg re-renders the Skill
from `.memory-tree.conf`, which this unit does not touch.

No new gate leg. The three couplings the master states in its §7 are discharged rather than
inherited:

1. **`KIT_MEMORY_TREE_VERSION`.** U1 makes no edit to `tools/memory-tree/check-memory-hygiene.sh`, so
   the three-place bump (`:13` plus the `HYGIENE.template.md` marker pair) and the `--render` are not
   owed, and `tools/memory-tree/check-verdict-epoch.sh` stays quiet. A builder tempted to widen check
   3 or to fix `ex7` while here must stop: both edits are U3's, and taking either in U1 pulls in the
   version bump, the parity render and a kickoff re-stamp.
2. **The kickoff manifest's seven watched pathspecs.** None is staged, so `manifest-check.sh
   --staged`'s C5s leg needs no `last-audit` re-stamp in this commit.
3. **A new gate leg would need an `AGENTS.md` bullet citing its argv path.** There is no new leg, so
   `handkept_inventories_disagreeing_with_source` stays at its pin of 7 and
   `python tools/drift-audit/drift_report.py --check` is unmoved.

Two obligations belong to the commit that LANDS THIS SPEC FILE, which is not the build commit above:

- The unit specs under `memory/builds/aMendedLedger/spec/units/` are new files under a build's
  `spec/`, and `collect()` selects that whole subtree (`gen_build_index.py:229`). Landing them moves
  the `<!-- gen:build-index -->` region of `memory/builds/aMendedLedger/README.md` — the `N unit(s)`
  count and the unit table `render_region` writes at `:248-257`. That commit must run
  `python tools/memory-tree/gen_build_index.py --write` and stage every artifact it rewrites, or
  hygiene check 9 reds on a file nobody edited.
- This file's H1 is `# TOOL-aMendedLedger-2 — U1: …`, per-file seq, id followed IMMEDIATELY by the
  em-dash. `H1_RE` (`gen_build_index.py:54`) requires exactly that, and `parse_spec` (`:169-174`)
  otherwise falls back to the basename with an empty title, so the rendered unit row would carry a
  filename instead of an id and title. Six sibling specs sharing one id would also reproduce the
  over-flagging shape `drift_report.py:228-231` records at 107/126 — the seq is the discriminator.
  `memory/builds/aMendedLedger/README.md:7` already reads `ids: TOOL-aMendedLedger-1..-6`, so the
  front matter and the H1s agree.

Run `python tools/memory-tree/gotchas.py --for-diff 663ca427..HEAD` before the review, not after.

## 8. Open questions

none — the master resolved all six of its forks at rev-4: F2 and F5 `RESOLVED (owner, 2026-08-09)`,
F1, F3, F4 and F6 `RESOLVED (build, 2026-08-09)`. Every one of them is scoped to U2+U4, U3 or U6, and
§3 names the two — F1's check-3 tightening and F6's `ex7` rewrite, both now IN and both U3's — that a
builder working in this unit could mistake for U1's business.

## 9. Revision log

- rev-1 · 2026-08-09 · initial draft. Written to the ratified master
  `memory/builds/aMendedLedger/spec/2026-08-09-spec-aMendedLedger-1.md` at its third revision, covering its §4
  Migration rows 1-5, the journal half of the `.gitkeep` row, and Rollout row U1. Every claim about
  existing code re-verified at HEAD `dae75003` rather than taken from the master: check 2's full-tree
  population and its `[ -f ]` resolution, `index_set()`'s existence filter, `derive_status`'s two
  mutually exclusive routes, `render_live`'s terminal filter, `render_shards`' month key, the
  present-tense corpus regex, the two grandfather registries' contents, and the manifest's seven
  pathspecs.
- rev-2 · 2026-08-09 · folded the cross-unit sub-spec review (no blocking defects against this file;
  nine non-blocking, plus the cross-file H1 item). The H1 is now `# TOOL-aMendedLedger-2 — U1: …`:
  rev-1's `# TOOL-aMendedLedger-1 U1 — …` did not match `H1_RE`, so `parse_spec` fell back to the
  filename with an empty title, and all six specs of this build shared one id. Header moved Tier-1 →
  **Tier-2**: Tier-1 makes check 12 `next` at `check-memory-hygiene.sh:549`, disarming the section
  canon, the empty-body rule, the header-rev-logged-in-§9 rule and the terminal-status-needs-a-
  resolved-§8 rule — four assertions this file already satisfied, so Tier-1 bought nothing and would
  have left the §8 assertion unrun when the status flips to CLOSED. Six citations corrected against
  the worktree: check 2's link awk `:191`→`:187`, check 5's name test `:296`→`:294`, `extract.py:86`→
  `:87` for `A_HEADING`, `corpus_ids.py:190`→`:194` for `h1_re`, `drift_signals.py:135`→`:136` for
  `handkept_inventories_disagreeing_with_source`, and `memory/HYGIENE.md:31`→`:27` for the archive
  line. The digest-fold rule kept its verdict and replaced its reason: rev-1 justified it with check
  13, which is a two-build-folders check (`corpus_ids.py:340-342`) and cannot fire on this at all —
  the reason that holds is that `A_BOLD_LI` (`extract.py:88`) and `A_DASH` (`:92`) would split
  retrieval for `TOOL-bThriftyBellows-1` across two records. AC2 was unfalsifiable: `git log --follow`
  without `-p` never prints `similarity index`, so it could not distinguish the rename it exists to
  prove; the master carries the same correction in its own AC2. §4's inventory cell for
  `memory/project/IN-FLIGHT.md` was 4 lines and is 3. §7 named a leg that does not exist
  (`memory-recall selftest` → `memory-recall kit selftest`, and it is not load-bearing here). §3's
  doc-truth non-goal now enumerates all six `memory/HYGIENE.md` sites the master hands to U6, not two,
  and records that the only markdown link into the doomed set tree-wide is `memory/project/MEMORY.md:4`.
  Two unit boundaries are now stated rather than left implicit: `memory/archive/ledger/README.md` is
  created HERE (master §4 Migration `…-1.md:138`; the master's current Rollout row `…-1.md:174` now
  agrees and tells U2 not to re-create it), and the commit that lands these spec files — not the build
  commit — owes the `gen_build_index.py --write` regeneration. Re-read against the master's **fourth
  revision**, where all six forks are resolved and the `check-memory-hygiene.sh:346` `ex7` rewrite has
  moved out of §3 Non-goals into U3; §3 and §8 here are re-stated to that fact. AC11 added so the new
  H1 id cannot leak into a `PRODUCT_GLOBS` file as a provenance comment. (The MASTER's revision
  numbers are spelled out in words throughout this section, deliberately: check 12 takes the largest
  `rev-N` token anywhere in §9 as the high-water the header must not exceed, so another spec's higher
  revision token written here would pre-satisfy the assertion for revisions this file has not had.)

## 10. Reuse audit

U1 adds no executable code, so there is no symbol for `tools/codebase-map/reuse_lookup.py` to match;
the master's §10 already recorded the build-level pass, and its finding ("no seam fits for the merge
itself") is about U5, not this unit. What U1 does instead is invoke four seams that already exist and
must not be re-implemented:

- `python tools/memory-tree/gen_build_index.py --write` renders the build README region, the month
  shard and `LIVE.md`. No index row is hand-written here, and check 9 byte-compares the result.
- `git mv` carries the rename, so `git log --follow` keeps both journals' history. A delete-plus-add
  would satisfy every gate and lose the provenance AC2 asserts.
- `memory/builds/aRuledParchment/` is reused rather than duplicated: only its missing `build/`
  subfolder is created, per the kit's conditional-ceremony rule.
- Check 5's single-sourced name grammar (`REC_TAIL` at `check-memory-hygiene.sh:109`) is satisfied by
  choosing conforming names, not dodged by appending either journal to
  `memory/project/legacy-files.txt` — that file is a shrink-only grandfather list, and growing it to
  cover a file this unit is free to rename is the wrong direction.
