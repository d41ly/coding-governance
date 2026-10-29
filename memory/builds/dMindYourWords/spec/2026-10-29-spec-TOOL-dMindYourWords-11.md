# TOOL-dMindYourWords-11 — the vocabulary changed only with the write path's record, which takes over from `ratified`

**Status:** OPEN · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 5 · advances TOOL-dMindYourWords-18

**Carries:** cl-dClosedLoop-0272@51d03a52 whole
**Carries:** node:record-kind.lexicon-declaration

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-build-TOOL-dMindYourWords-11-deviation-111.md](../build/2026-10-29-build-TOOL-dMindYourWords-11-deviation-111.md) | deviation | — |
| [2026-10-29-build-TOOL-dMindYourWords-11-reuse-scout-c.md](../build/2026-10-29-build-TOOL-dMindYourWords-11-reuse-scout-c.md) | research | TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-16 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-12 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-1 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-12 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-6 TOOL-dMindYourWords-8 TOOL-dMindYourWords-10 TOOL-dMindYourWords-9 TOOL-dMindYourWords-16 TOOL-dMindYourWords-13 TOOL-dMindYourWords-17 |

<!-- /gen:spec-records -->

## 1. Goal

Today anyone edits `.lexicon.conf` and nothing asks why: pins and un-armed cells change by plain edit,
and `ratified` is a stamp that certifies nothing about a VERBS edit, because its one signal compares it
with `LANGS=` alone (`tools/drift-audit/drift_report.py:1343`; gap-lex-06). This unit makes every
vocabulary change carry the instruction write path's `change` record in its own commit, refused at
commit without one; lets that record take over from `ratified`, with every reader of the stamp by value
moved to it; widens the staleness signal to VERBS and the armed LANGS; adds the re-baseline that sets
the debt pin once a vocabulary change reclassifies debt; re-justifies the `init` row; and registers the
repository's lexicon declaration as a record kind whose writer is that path.

## 2. Scope (IN)

Build-run precondition: PLAY-dOrderedCharter-15 S7 (the `change` record kind) and PLAY-dOrderedCharter-7
S7 (the factory `tools/memory-tree/build_records.py`, whose `new change` verb is the stand-in door while
`instructions_edit.py` refuses writes), and TOOL-dTotalRecall-1 S1 and S9 (`record-kinds.toml`,
`record_kinds.py new`), each DEFERRED at base and built by an ancestor build before this build run.

- **S1** — The reader (I11). `read_vocabulary_record(root, tags=None, rev=None)` in
  `tools/lexicon/lexicon_conf.py` returns `(date, path)` for the latest vocabulary record, or `None`. A
  vocabulary record is a tracked file named `<date>-build-<unit id>-change-<n>.md` whose `**Serves:**`
  line reads `change <unit id>` and whose `**Unit:**` field is a tag of `RECORD_TAGS` (§4), restricted to
  `tags` when given. With `rev` a commit, only the records that commit adds count; with `rev` `index`,
  only the records the index adds over HEAD. Latest is the largest filename date, ties broken by path.
  The CLI mode `--print-record [<tag>] <root>`, beside `--print-verbs` and `--print-rows`
  (`lexicon_conf.py:501-521`), prints `<date>` TAB `<path>`, or nothing, and exits 0. Observed by AC1,
  AC2.
- **S2** — The record's pins. `derive_vocabulary_hash(root, tag, conf)` returns the first eight hex
  digits of the SHA-1 of the rows that tag covers (§4 "The tags"), and `--print-hash <tag> <root>`
  prints `<tag>@<hash8>`, the value a writer puts in the record's `Before` and `After`. A dark-only
  LANGS entry is outside every hash. Observed by AC3.
- **S3** — The commit check. `python lexicon.py --check-record` compares HEAD with the index: for each
  tag of `RECORD_TAGS` whose rows differ, except a debt pin that falls, it requires a vocabulary record
  of that tag the index adds (S1 with `rev` `index`), and exits 1 naming each tag without one and the
  `Before` and `After` S2 prints; it exits 0 when every changed tag has its record and 2 when a
  declaration does not parse. A debt pin raised means, under unit 1's ledger (I4), a row the ledger
  `memory/project/lexicon-debt.txt` gains, and that row's disposition must be `widened:<record>`
  naming a record the index adds. Observed by AC4.
- **S4** — The hook block. `.githooks/pre-commit` gains one block, `lexicon vocabulary record, staged
  leg`, beside the memory-tree hygiene staged leg: it runs only when `.lexicon.conf`, a lexicon waiver
  registry or the debt ledger is staged, resolves the kit with `resolve_kit_gate lexicon lexicon.py`,
  and runs `with_hook_index "$py" "$g" --check-record || rc=1`, announcing a skip with `print_kit_miss`
  when no kit resolves. Observed by AC5.
- **S5** — The stamp's readers by value move to the record, and the key `ratified` retires.
  **Readers:** by name: `ratified`, spelled in `.lexicon.conf` (line 370), `drift_report.py` (line
  1215, its `conf.get` read), `adopt-lexicon.sh` (lines 15, 430, 566 and 587), the writer
  `scaffold_lexicon.py` (lines 12, 53 and 319), the prose carriers `tools/lexicon/README.md` (line 669)
  and `LEXICON.md` (lines 75 to 78), the comment in `lexicon_conf.py` (line 164), and the fixtures
  `tools/lexicon/selftest.py` and `tools/drift-audit/selftest.py` (lines 1074 to 1095) · by value:
  `signal_lexicon_ratified_stale`, which compares the stamp's date with the LANGS commit
  (`drift_report.py` lines 1334 to 1338), the empty-stamp refusal in `adopt-lexicon.sh` (line 431), and
  the hole `lexicon-ratified` (`tools/lexicon/kit.toml` lines 177 to 183) that discharges through it.
  Each by-value reader reads S1 instead, `.lexicon.conf` loses the key and its comment block (lines 330
  to 370) in the commit that adds gov's first vocabulary record (S10), and the scaffold writes no stamp.
  `lexicon.py` and `lexicon_conf.py` never read the key by value at base (scout C disagreement 2): the
  only text there is the comment at `lexicon_conf.py:164`, rewritten. Observed by AC6, AC7, AC11.
- **S6** — The signal widened (I16). `signal_lexicon_ratified_stale` keeps its function name and its
  place in `SIGNALS` (`drift_report.py:3524`), and its signal name becomes
  `lexicon_record_older_than_language_surface`, so the old name retires. **Readers:** by name:
  `lexicon_ratified_older_than_language_surface`, spelled in `drift_report.py` (line 1326), its pin in
  `drift_signals.py` (line 309), its row in `tools/drift-audit/README.md` (line 131) and the fixture
  reads in `tools/drift-audit/selftest.py` (lines 1026, 1074, 1080 and 1090) · by value: the pin's
  comparison in `drift_report.py --check` and the `drift-audit records` leg that gates on it. It
  compares the latest vocabulary record of tag `unit.lexicon.verbs` or `unit.lexicon.cells` with the
  newest commit on `.lexicon.conf` whose VERBS rows or armed LANGS entries differ from its first
  parent's (§4 "The surface"), and fires when that commit's date is after the record's. Observed by AC6.
- **S7** — `adopt-lexicon.sh --check` and the hole. The empty-stamp arm becomes: when `--print-record
  <root>` prints nothing, refuse, naming the write path and the stand-in command that writes a first
  record. The hole `lexicon-ratified` takes the id `lexicon-recorded`, its `why` stating the record,
  its discharge command unchanged, so the old id retires. **Readers:** by name: `lexicon-ratified`,
  spelled in `tools/lexicon/kit.toml` (line 178) and the comment in `govkit.py` (line 11324) · by value:
  NO VALUE READERS — govkit runs a hole's `discharge` command and reads its exit, never its id.
  Observed by AC7.
- **S8** — The re-baseline. `python lexicon.py --rebaseline <record>` reads a vocabulary record from the
  working tree, grades the corpus under the working-tree `.lexicon.conf`, writes the debt pin unit 1
  holds so it equals the debt population, every key the population gains carrying
  `widened:<record>`, and prints `re-baseline <tag>: debt <old> -> <new>`. The debt population is the
  offenders whose `Offender.grade` is `debt` (I1), keyed as `render_offender_keys` keys them
  (`lexicon.py:3482`). A record that does not resolve, or whose tag is outside `RECORD_TAGS`, exits 2.
  The admission is this unit's too: in unit 1's pin verdict `check_debt_pin` (TOOL-dMindYourWords-1
  S4), a `gained` or `raised` row whose disposition is `widened:<record>` greens under `lexicon.pin`
  `shrink-only` when `<record>` is a tracked vocabulary record (S1's predicate on that one path), and
  stays red when it names anything else. Observed by AC8.
- **S9** — The `init` row. It stays as vocabulary, re-justified by a comment above it in `.lexicon.conf`
  naming its measured users and that the data-model pack (TOOL-dMindYourWords-7) forces `__init__`
  (§8 F2); `memory/map/features/lexicon.md:36` keeps its claim, so no dossier moves. Observed by AC9.
- **S10** — The node `record-kind.lexicon-declaration`. One `[[record-kind]]` row in
  `tools/memory-tree/record-kinds.toml`, written by `python record_kinds.py new lexicon-declaration
  --tag record.lexicon-declaration --writer hand --check "lexicon wiring"`, with `home` `.lexicon.conf`,
  `schema` form `rows` and `readers` the lexicon engine and `adopt-lexicon.sh --check`; the writer is
  `hand` because the declaration is edited by hand and admitted by S3, until TOOL-dTotalRecall-2 registers
  a door. `python record_kinds.py --write` re-renders the kinds region of
  `tools/memory-tree/HYGIENE.template.md`, which `adopt-memory-tree.sh --render` carries into
  `memory/HYGIENE.md` (TOOL-dTotalRecall-1 S6). Gov's own first record,
  `memory/builds/dMindYourWords/build/<date>-build-TOOL-dMindYourWords-11-change-1.md`, tag `unit.lexicon.verbs`, `Action: add`, `Before: none`, written through the stand-in door, lands in
  the same commit as S5's edit to `.lexicon.conf`. Observed by AC10.
- **S11** — The docs: the lexicon README's adoption section and `LEXICON.md`'s curation paragraph name the
  record, the check and the re-baseline. NOT OBSERVED by a criterion: the `lexicon wiring` leg renders the
  Skill from the conf and grades it, and prose has no other grader.

## 3. Non-goals (OUT)

- The write path, its proof and its guard: PLAY-dOrderedCharter-15 and dDeclaredLoop. This unit writes
  no change record of its own beyond gov's migration record, and never writes one from lexicon code.
- The pin's classes, its values and its ledger: TOOL-dMindYourWords-1. S8 writes the pin through the
  shape unit 1 holds and decides nothing about `lexicon.pin`.
- Suppressions' provenance: TOOL-dMindYourWords-5 reads S1 per commit. The contract table's:
  TOOL-dMindYourWords-3.
- Moving the signal into the lexicon's leg pack and out of drift-audit: TOOL-dMindYourWords-16, which
  reads S1. This unit edits the signal where it stands.
- The `lexicon-pins` hole and the two-sided pin wording: TOOL-dMindYourWords-14 (d) and
  TOOL-dMindYourWords-1.
- Catching a commit made with `--no-verify`: the refusal journal `git:pre-commit/<gate>`
  (TOOL-dWellOiledMachine-49 S3) records a bypass when it lands, and S6 and unit 1's shrink-only ledger
  see its effect at the bar.
- Ask TOOL-dUnstalledConvoy-35, the dark-only LANGS change: S6's armed-entries surface answers its
  question, and this unit changes no row of that build's backlog.

### Edges

- **consumes-from** `TOOL-dMindYourWords-1` — `Offender.grade`, whose `debt` value is the population S8
  sets the pin to, and the debt ledger of I4 S3 and S8 read and write; without it S8 counts every
  offender
- **hands-off** `TOOL-dMindYourWords-3` — `read_vocabulary_record`, which the contract table's check
  reads for tag `unit.lexicon.contracts`, and `RECORD_TAGS`, which that unit extends with `CONTRACTS:`
- **hands-off** `TOOL-dMindYourWords-5` — `read_vocabulary_record` with `rev` a commit, the provenance a
  suppression row's commit must carry, tag `unit.lexicon.suppressions`
- **hands-off** `TOOL-dMindYourWords-10` — `--rebaseline`, which brings the existing splits into the
  pin once, under a record of tag `unit.lexicon.nouns`, and `RECORD_TAGS`, whose `NOUNS:` and
  `FAMILIES:` rows put both blocks under `--check-record`
- **hands-off** `TOOL-dMindYourWords-13` — `read_vocabulary_record`, which names the re-baseline record
  that unit's landing seed of tag rows cites
- **hands-off** `TOOL-dMindYourWords-16` — `read_vocabulary_record`, which the moved signal reads, and the
  signal name `lexicon_record_older_than_language_surface`
- **consumes-from** external — PLAY-dOrderedCharter-15 S7 and PLAY-dOrderedCharter-7 S7 (the `change`
  kind and its stand-in door) and TOOL-dTotalRecall-1 S1 and S9 (the record-kind registry), DEFERRED at
  base and built by ancestor builds before this build run
- **hands-off** `TOOL-dMindYourWords-23` — `--rebaseline`, which that unit makes carry the tag rows it does not measure (review id 43)
- **hands-off** `TOOL-dMindYourWords-26` — S8's `shrink-only` admission, which that unit narrows to a vocabulary record the branch adds (review id 44)
- **hands-off** `TOOL-dMindYourWords-28` — `read_vocabulary_record` with `rev` a commit, whose added set that unit defines for a parentless commit (review id 49)
- **consumes-from** `TOOL-dMindYourWords-27` — the ledger home `.lexicon-debt.txt`, the debt ledger S3's `--check-record` reads and S4's hook block runs for, in place of `memory/project/lexicon-debt.txt` (review id 45)
- **hands-off** `TOOL-dMindYourWords-29` — `read_vocabulary_record`, `--check-record`, the hook block and the stamp's other readers, which the minors batch repairs (review ids 16, 26, 34, 35, 52)

## 4. Design

### The tags

`RECORD_TAGS` in `lexicon_conf.py` maps each declaration key to the tag a record of its change carries.
The tag set is I11's, closed: `verbs`, `nouns`, `families`, `packs`, `contracts`, `suppressions`,
`pins`, `cells`, each `unit.lexicon.<part>`.

| Key | Tag | What the hash covers |
|---|---|---|
| `VERBS:`, `CANON:` | `unit.lexicon.verbs` | each row as `--print-rows` prints it |
| `NOUNS:` | `unit.lexicon.nouns` | the same |
| `FAMILIES:` | `unit.lexicon.families` | the same |
| `PACKS:` | `unit.lexicon.packs` | the same |
| `CELLS:`, `PATTERNS:`, `OUT_OF_SCOPE:`, `LANGS=` | `unit.lexicon.cells` | rows, and LANGS' armed entries only |
| the debt pin | `unit.lexicon.pins` | the pin's value or the ledger's rows |
| the waiver registries | `unit.lexicon.suppressions` | their rows |
| `CONTRACTS:`, the entry TOOL-dMindYourWords-3 adds | `unit.lexicon.contracts` | its rows |

A key no conf declares yet (`NOUNS:`, `FAMILIES:`, `PACKS:`, `OUT_OF_SCOPE:`, each I8's) has no rows,
so it never differs until its unit adds the block. A dark LANGS entry is outside the hash: `dark` refuses
to extract, so it adds no definition to what the vocabulary governs (ask TOOL-dUnstalledConvoy-35's
reading). Turning an armed entry dark un-arms it and moves the hash.

### The check

```
--check-record:
  head, index = parse(HEAD:.lexicon.conf), parse(:.lexicon.conf)   # one load_conf each, via a temp copy
  changed = {tag for key, tag in RECORD_TAGS if rows(head, key) != rows(index, key)}
  changed -= {"unit.lexicon.pins"} if the pin fell
  for tag in changed:
      if read_vocabulary_record(root, (tag,), rev="index") is None: refuse(tag, before, after)
  for row the debt ledger gains: its disposition names a record the index adds, else refuse
```

A missing `.lexicon.conf` at HEAD is the adoption commit: every tag is changed, and the first record
admits it. The waiver registries and the ledger are compared as row sets the same way.

### The surface

The signal reads `git log --first-parent --format=%H %cs -- .lexicon.conf` once and every listed
blob with one `git cat-file --batch`, the shape `read_defs_at_sha` reads (`lexicon.py:4113`), and walks
newest first to the first commit whose VERBS rows or armed LANGS entries differ from the next older
blob's. Each blob is read by `read_vocabulary_surface(raw)` in `lexicon_conf.py`, built on the loader's
own `_BLOCK_RE`, `_parse_rows`, `_SCALAR_RE` and `langs`, which skips a block it does not know rather
than refusing it, so a blob from before a block retired still answers. A blob that does not parse is
counted `unjudgeable` and skipped.

### Inventory

Minted: `read_vocabulary_record`, `derive_vocabulary_hash`, `read_vocabulary_surface` and `RECORD_TAGS`
in `tools/lexicon/lexicon_conf.py`; the modes `--print-record` and `--print-hash` there; the modes
`--check-record` and `--rebaseline` of `tools/lexicon/lexicon.py`; the hole id `lexicon-recorded`; the
signal name `lexicon_record_older_than_language_surface`; the record kind `lexicon-declaration`. Naming
cells: the three functions answer `OK` under `lexicon.py --suggest <name> --as py.function` at base;
`RECORD_TAGS` sits in cell `py.constant`, which the conf does not declare at base.

### Migration

Gov's tree: S10's record lands in the same commit as the stamp's removal, so S7 never reds here. An
adopter: the upgrade brings the new `--check`, which reds until the adopter writes one vocabulary record,
naming the command (§8 F4); its leftover `ratified=` line is an unread scalar `load_conf` still parses.

### Rollout

Live when built. The hook block runs only when a vocabulary file is staged, so an ordinary commit
spawns nothing new.

### Files touched (estimate)

- `tools/lexicon/lexicon_conf.py`
- `tools/lexicon/lexicon.py`
- `tools/lexicon/adopt-lexicon.sh`
- `tools/lexicon/scaffold_lexicon.py`
- `tools/lexicon/kit.toml`
- `tools/lexicon/selftest.py`
- `tools/lexicon/README.md`
- `tools/lexicon/LEXICON.md`
- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/drift_signals.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `tools/govkit/govkit.py`, the comment at `:11324`
- `tools/memory-tree/record-kinds.toml`
- `tools/memory-tree/HYGIENE.template.md`, the kinds region `record_kinds.py --write` renders
- `memory/HYGIENE.md`, the render of the template above, regenerated by `adopt-memory-tree.sh --render`
  and never the edit; it trips `kit/dogfood doc parity`, as the template does
- `.githooks/pre-commit`
- `.lexicon.conf`
- `memory/builds/dMindYourWords/build/`, gov's first vocabulary record

### Alternatives rejected

- **The vocabulary as overlay rows** of a registered kind in `.governance/instructions.toml`, written by
  `instructions_edit.py`. Rejected by the clause itself: it compares "VERBS and LANGS edits" with the
  record, so the declaration keeps its blocks, and I8 adds four more to `.lexicon.conf`.
- **A lexicon-own editing command** writing the conf and the record. A second write path, which the
  clause's "only through the instruction write path" refuses.
- **The signal over `git log -G`**, as today. Rejected by test: a VERBS row and a CELLS row are both an
  indented `<key>  <rest>` line, so no `-G` pattern tells them apart, and the fixture's in-place-widening
  arm (`tools/drift-audit/selftest.py:1065-1082`) is the reason `-S` was already refused.
- **A record date read from the commit** that added it. The filename date is what the stamp's date was,
  an authored date the fixture can plant, and one fewer git call per record.

## 5. Production-readiness checklist

- security — the check refuses by default: a changed tag with no record refuses, a declaration that does
  not parse exits 2, and the hook refuses rather than passes on a refusal.
- perf / scale — the hook runs only on a staged vocabulary file: two `git show` reads, one `git diff
  --cached`, two parses. The signal is two git calls and one parse per conf blob, stopped at the first
  differing pair.
- error / empty / loading states — no record anywhere: `--print-record` prints nothing, the signal is
  not asked, `--check` refuses with the remedy; an unparseable historical blob is `unjudgeable`.
- observability — each refusal names the tag, the `Before` and `After` S2 prints and the command that
  writes the record; the re-baseline prints its delta.
- risks — every future LANGS arming, VERBS edit and pin raise costs a record, the price the clause sets;
  the adopter's first `--check` after upgrade reds until its first record (§8 F4).
- testing — the arms of §7, each on a planted case in a fixture repository.
- migration — S10's record for gov; the refusal's remedy for an adopter.
- user docs — the lexicon README and `LEXICON.md`, S11.

## 6. Acceptance criteria

- **AC1** — When `python lexicon_conf.py --print-record <root>` runs in a fixture repository holding
  `2026-10-01-build-TOOL-tX-1-change-1.md` with `**Unit:** unit.lexicon.verbs`,
  `2026-10-05-build-TOOL-tX-2-change-1.md` with `unit.lexicon.cells` and
  `2026-10-09-build-TOOL-tX-3-change-1.md` with `unit.memory.x`, it prints the 2026-10-05 record; with
  tag `unit.lexicon.verbs` it prints the 2026-10-01 record; in a repository with none it prints nothing
  and exits 0.
  Red when: the `unit.memory.x` record is read as vocabulary, or an untagged call ignores the tag set.
  fixture: the selftest builds the repository.
- **AC2** — When `read_vocabulary_record(root, rev=<sha>)` runs on the commit that added the 2026-10-05
  record, it returns that record, and on a commit adding none it returns `None`; with `rev` `index` and
  a staged record it returns the staged one.
  Red when: a record an older commit added is returned for a later commit.
- **AC3** — When `python lexicon_conf.py --print-hash unit.lexicon.cells <root>` runs before and after
  appending `zz::dark` to LANGS, it prints the same hash; after turning `py:python-ast:parser` into
  `py::dark` it prints another.
  Red when: a dark-only addition moves the hash, or un-arming does not.
- **AC4** — When `python lexicon.py --check-record` runs in a scratch clone of a fixture repository
  with a raise of the debt pin staged, it exits 1 naming `unit.lexicon.pins`; with a vocabulary
  record of that tag staged beside it, it exits 0; a staged removal of a `CELLS:` row with no record
  exits 1 naming `unit.lexicon.cells`; a staged pin fall and a staged `zz::dark` each exit 0.
  Red when: the staged pin raise exits 0, which is the clause's probe.
  fixture: the selftest builds the clone under the system temp directory.
- **AC5** — When `git commit` runs in that clone with `core.hooksPath` set to its `.githooks`, the pin
  raise without a record is refused with the `--check-record` line, and the same commit with its record
  lands.
  Red when: the hook block admits the raise.
  fixture: as AC4, the clone carrying `.githooks/pre-commit` and the kit.
- **AC6** — When `drift_report.py` runs over the drift-audit fixture that commits a vocabulary record
  dated 1999-01-01 and then arms `js:js-regex:probe` in LANGS, `lexicon_record_older_than_language_surface` reads value 1; the same
  with a VERBS row added instead reads 1; with only `zz::dark` added it reads 0; with a record dated
  2999-01-01 it reads 0.
  Red when: the planted LANGS change newer than the record reads 0, or the VERBS change is invisible.
  fixture: a scratch repository the probe builds, holding a `.lexicon.conf` with its LANGS and VERBS
  rows and one vocabulary record; §7's second `New arm:` carries the same fixture into the drift-audit
  suite, rewriting the one at its lines 1074 to 1095 today.
- **AC7** — When `bash adopt-lexicon.sh --check` runs over a fixture repository with no vocabulary
  record, it exits 1 naming the write path and the stand-in command; with one record that arm passes;
  `git grep -n 'get("ratified")' -- tools/` prints nothing and `grep -c lexicon-recorded
  tools/lexicon/kit.toml` prints 1.
  Red when: a repository with no record passes the check, or a by-value reader of the stamp remains.
- **AC8** — When a fixture repository whose `.lexicon.conf` declares `init` and whose corpus holds
  `init_repo` and `init_tree` removes the `init` row, adds a record of tag `unit.lexicon.verbs` and runs
  `python lexicon.py --rebaseline <record>`, it prints `re-baseline unit.lexicon.verbs: debt 0 -> 2`,
  both new ledger keys carry `widened:` naming that record, `--check-record` over the staged result
  exits 0 and the pin verdict greens under `shrink-only`; without the record staged `--check-record`
  exits 1, and a `widened:` naming a path that is no vocabulary record reds the verdict.
  Red when: the delta is carried by no record, or the pin moves with no record named.
  fixture: the selftest builds the repository; the ledger shape is unit 1's.
- **AC9** — When `grep -n -B3 '^  init ' .lexicon.conf` runs, it prints the `init` row with the comment
  naming its measured users and the data-model pack, and `grep -n '"init"'
  memory/map/features/lexicon.md` still prints the claim.
  Red when: the row stands with no justification, or the claim moved without the row.
  figure: the users count is PINNED at 12 at `ba8b3c8c4` (§8 F2), re-derived by that F-item's probe.
- **AC10** — When `grep -n 'name = "lexicon-declaration"'` runs over `record-kinds.toml`, it prints the
  row, and `python record_kinds.py --check` grades it clean; `--print-record <repo root>` at
  this unit's commit prints gov's record.
  Red when: the kind has no row, or gov's tree carries no vocabulary record after the stamp leaves.
- **AC11** — When `bash adopt-lexicon.sh --scaffold` seeds a fixture repository, the written `.lexicon.conf`
  carries no `ratified` line and `adopt-lexicon.sh --check` there refuses on the missing record.
  Red when: the scaffold still writes the stamp.

## 7. Gates

`lexicon selftest` · `lexicon wiring` · `lexicon naming predicates` · `codebase-map kit selftest` · `drift-audit selftest` · `drift-audit records` · `straggler-guard arms` · `govkit acceptance matrix` · `govkit selftest` · `govkit refusal join` · `policy fixtures` · `kit/dogfood doc parity` · `memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC7 AC8 AC11 · the fixture repositories and the scratch clone, each failing case staged by a planted pin raise, a planted un-armed cell and a planted re-baseline with no record · none

New arm: tools/drift-audit/selftest.py · covers AC6 · the fixture's planted LANGS and VERBS changes newer than the record, staged by comparing LANGS alone · none

## 8. Open questions

- **F1 — How does a vocabulary change reach `.lexicon.conf`, when `instructions_edit.py` writes only
  manifest rows and refuses every write until dDeclaredLoop's guard lands?** Options: (a) the vocabulary
  as overlay rows of a registered kind, the conf rendered from them; (b) the conf kept, edited by hand,
  each change admitted only with the write path's `change` record in its own commit, written by the
  command once it admits writes and through the factory's `new change` stand-in door until then; (c) a
  lexicon command writing the conf and the record. (a) contradicts the clause's "VERBS and LANGS edits"
  and I8's blocks; (c) is a second write path. RESOLVED (agent, 2026-10-29, delegated): (b), rung 1: the
  clause compares edits of the declaration with the record, and the lexicon review's `[vocabulary]` reads
  "a check refuses a commit that raises a pin or un-arms a cell with no instruction-path record".
  widens: none · relaxes: none
- **FACT-QUESTION · F2 — Is `init` vocabulary, or only a clearance for `__init__`?** Probe: a walk of
  `scan_corpus` over the graded corpus counting definitions whose `leading_verb` is `init` and whose name
  is not `__init__`; the row stays when the count is above 0, else it goes with the dossier claim. The
  probe can read 0: a corpus whose only `init` definitions are `__init__` reads 0. Observed at
  `ba8b3c8c4`: 12, among them `init_bounded` (`tools/unattended/unattended.sh:266`) and `init_repo`
  (`tools/memory-tree/migrate_backlog.py:2731`), beside 14 `__init__`. RESOLVED (agent, 2026-10-29,
  delegated): the row stays, re-justified, rung 2. widens: none · relaxes: none
- **F3 — Which changes need a record?** Options: (a) a pin raise and an un-armed cell only, the lexicon
  review's sentence; (b) every change to a vocabulary key except a pin fall and a dark-only LANGS
  addition; (c) every change to the file. (c) charges a record for a comment; (a) leaves a VERBS edit
  free, which is gap-lex-06's "`ratified` certifies nothing about verb edits". RESOLVED (agent,
  2026-10-29, delegated): (b), rung 3, the most feature-rich survivor: the clause reads "the vocabulary
  changed only through the instruction write path". widens: none · relaxes: none
- **F4 — An adopter's conf carries a `ratified` stamp and no record: what does `--check` do?** Options:
  (a) read the stamp as a legacy record; (b) an upgrade step writing a record into the adopter's tree;
  (c) refuse, naming the command that writes the first record. (a) keeps a reader of the stamp, against
  the clause (veto 1); (b) writes a record into an adopter's memory tree from `govkit update`, a write
  surface no unit priced, and the `change` kind's home is a build folder an upgrade does not have
  (veto 3). RESOLVED (agent, 2026-10-29, delegated): (c), rung 3, the one survivor. widens: none ·
  relaxes: none
- **F5 — Where does the re-baseline's delta live?** Options: (a) in the ledger keys it adds, each
  `widened:<record>`, with the delta printed; (b) a `Delta` field on the `change` kind, an ask to
  dOrderedCharter; (c) the record's prose, which nothing grades. RESOLVED (agent, 2026-10-29,
  delegated): (a), rung 3: it reuses TOOL-dWitnessedBar-13's `widened:<record>` disposition, so the
  ledger's own shrink-only compare reads the record, and it asks no parent change. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from the packet's Items 11, the lexicon review `[vocabulary]`
  :390-419 and `[drift]` :384-388, debt-fold rows `ratified-readers`, `pin-rebaseline`, `pins-plain-edit`
  and `init-row-inventory`, PLAY-dOrderedCharter-15 S2 to S7, scout C's row and disagreements 1 to 3
  and 6, and the spec brief's I11 and I16. The clause's named hole and readers differ from source:
  deviation record `2026-10-29-build-TOOL-dMindYourWords-11-deviation-111.md`.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (TOOL-dMindYourWords-23, TOOL-dMindYourWords-26, TOOL-dMindYourWords-28, TOOL-dMindYourWords-27, TOOL-dMindYourWords-29); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are `lexicon_conf.py`'s CLI `_main` (`:501`), whose `--print-verbs` and
`--print-rows` modes `adopt-lexicon.sh` already shells out to (`:423`, `:449`); the canon stamp arm
`adopt-lexicon.sh:439-465`, the recorded-door precedent S7 follows; `signal_lexicon_ratified_stale`
(`drift_report.py:1318`); the hook's staged-leg pattern (`.githooks/pre-commit:226-232`); the batched
blob read of `read_defs_at_sha` (`lexicon.py:4113`); `render_offender_keys` (`lexicon.py:3482`); and the
`widened:<record>` disposition of TOOL-dWitnessedBar-13 §4. `python tools/codebase-map/reuse_lookup.py
"find the latest change record for a vocabulary and compare its date with a declaration edit"` ranked
`records`, `read_records` (`tools/memory-tree/deviation_join.py`) and `read_first_commit_date`; each reads
another kit's records and a copy-installed kit may not import one (`check_self_containment`,
`lexicon.py:2359`), so no existing reader fits the record and S1 is new, the one reader. Where record and
source disagree: the clause names the `lexicon-pins` hole and reads in `lexicon.py` and `lexicon_conf.py`;
source shows the hole is `lexicon-ratified` and no by-value read in either module (scout C, disagreements
1 and 2, re-verified with `git grep -nw ratified` at `ba8b3c8c4`), recorded as deviation 111. Scout C's
line numbers hold at `ba8b3c8c4`. The recall probe also surfaced TOOL-dUnstalledConvoy-35, which §3 names.

Recall terms used: `python tools/memory-recall/query.py "how does a lexicon vocabulary change get recorded and replace the ratified stamp" --terms "ratified stamp change record instructions.edit write path vocabulary lexicon_conf drift signal LANGS VERBS re-baseline"`
