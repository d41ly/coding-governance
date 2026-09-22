# The corpus census — the population, verdicts, token rows and resolver output the pass wrote against

**Serves:** journal TOOL-dGatedProse-5

Node `d`, written 2026-09-22 by the build pass of `TOOL-dGatedProse-5` on
`branch/spec-prose-gates-b41f7c`. This is S8's census record: the provenance for every clause the
pass writes, committed with the resolver's output inside it and BEFORE the first clause commit. It
lands under `memory/builds/`, so under `TOOL-dGatedProse-1`'s S5 it is a record and resolves nothing
by content. Every figure below was produced by the pass's own instruments, written fresh for the pass
and run from the session scratchpad, so they are untracked and every figure is stated with what it
counts. The spec author's probes are provenance for the spec's section 4 and were not used here.

## The base, and the reading of the rulings

BASE is `e61b1cea544a4e70080d80cc45d0abe04d290efe`, pinned with `git rev-parse HEAD` before any
edit. The population was derived twice at that base, once reading every blob out of the commit and
once over the clean working tree, and the two runs printed byte-identical output.

The trigger is `TOOL-dGatedProse-1`'s S2 and S3 as its rev-8 text states them at that base:

- every member of the closed verb list matched case-insensitively over a folded copy of the item
  with runs of spaces and tabs squeezed to one;
- the strict phrases as substrings, the four imperative stems and the five past-tense forms of the
  O5 ruling at a word boundary on both sides. The pass ran the boundary two ways, a letter boundary
  and a regex `\b` boundary, and both gave the same item set, so the choice moves nothing here;
- the five identifier shapes over each backticked token as written, after the `:<line>` strip, with
  the three exclusions, and NO `.md` exclusion on any shape: reading B of O6, which F7 settled;
- shape 6, a backticked bare word beside one of the six kind nouns, which fires on nothing.

The item is check 12's accumulator: a column-0 bullet under `## N. Scope (IN)` and every line to the
next column-0 bullet, `## ` or `### `, fenced lines excluded. Liveness is the engine's negative test,
a status header that is neither `CLOSED` nor `WONTDO`.

## The population, and the two-way difference against section 4

| population | size | derivation |
|---|---|---|
| tracked spec-shaped files | 719 | check 12's path regex over `git ls-tree` at BASE |
| at or after `SPEC_FORMAT_CUTOFF` 2026-07-15 | 717 | check 12's selection |
| LIVE within that selection | 38 | the engine's liveness test |
| triggered items, reading B | 37 across 19 specs | the trigger above |
| node `a` | 27 items across 14 specs | each status header's `node` field |
| node `b` | 3 items across 1 spec | the same |
| node `d` | 7 items across 4 specs | the same |

Entered since the census, in the pass's set and not in section 4's tables: none. Left since the
census, in the tables and not in the pass's set: none. The write set is the derived set, and it is
the census's 37 items label for label.

Reading A, the slash-only drop F7 set aside, gives 33 items across 17 specs. Its difference from
reading B is exactly the four `B only` rows of section 4: `aMendedLedger-6-u6` S1 and S5,
`aPacedTurnstile-14` S9 and `dPolishedVitrine-14` S2, and no item is in reading A alone. The text
unit 1 carries is reading B, so the four are in the write set (AC14).

Of the 49 verb-bearing live items, 12 do not trigger. Four carry backticked tokens with no identifier
shape, the named gap: `aBatchedLintel-1` S3, `aGradedDoorway-7` S4, `aMendedLedger-1` S7 and
`aMendedLedger-6-u6` S3. Eight carry no backticked token at all: `aMendedLedger-1` S6,
`aMendedLedger-8-u9` S3, `aTunedCompass-3` S5, `aTunedCompass-9` S3 and its plain `S5c` item,
`dGatedProse-3` S4 and S6, and `dGatedProse-4` S2. Both classes match section 3 and get no clause.

No spec carrying a write-set item is terminal at BASE: four are INPROGRESS, one BLOCKED, two
DEFERRED and twelve SPECCED, so none leaves the population by the liveness test and none is edited
as a frozen record (AC8). The trigger run over this unit's own spec fires on 0 items, and over unit
1's on 0 (AC9).

## Verdicts and token rows

Copied from section 4's token table and escaped table, with ONE row changed: `dScaffoldedMirror-9`
S5, corrected at source by the spec's rev-8 before any clause was written, and for the reason below.
No row moves for S1's difference, because the difference is empty. "prose" means the half names no
token and passes by vacuity.

| item | node | status | verdict | by name | by value |
|---|---|---|---|---|---|
| `aGradedDoorway-7` S2 | a | INPROGRESS | GENUINE | `tools/unattended/check-unattended.test.sh`, `tools/unattended/unattended.test.sh`, `tools/run-gates/run-gates.gov.test.sh` | `tools/unattended/check-unattended.test.sh`, `tools/unattended/unattended.test.sh` |
| `aMendedLedger-1` S1 | a | SPECCED | GENUINE | `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`, `WIRE-INTO-PROJECT.md` | `WIRE-INTO-PROJECT.md` |
| `aMendedLedger-1` S2 | a | SPECCED | GENUINE | `tools/drift-audit/drift_report.py`, `tools/drift-audit/drift_signals.py`, `WIRE-INTO-PROJECT.md` | `signal_ledger`, `tools/drift-audit/selftest.py` |
| `aMendedLedger-2-u1` S4 | a | SPECCED | GENUINE | prose | `tools/memory-tree/check-memory-hygiene.sh` |
| `aMendedLedger-2-u1` S5 | a | SPECCED | GENUINE | `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`, `WIRE-INTO-PROJECT.md` | `WIRE-INTO-PROJECT.md` |
| `aMendedLedger-2-u1` S6 | a | SPECCED | GENUINE | `tools/check-dead-paths.sh`, `tools/dead-path-waivers.txt`, `tools/memory-tree/check-memory-hygiene.sh` | `signal_ledger`, `tools/drift-audit/drift_report.py` |
| `aMendedLedger-3-u2` S2 | a | SPECCED | GENUINE | `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/check-memory-hygiene.test.sh` | `tools/drift-audit/drift_report.py`, `tools/drift-audit/drift_signals.py` |
| `aMendedLedger-3-u2` S3 | a | SPECCED | GENUINE | `tools/drift-audit/drift_signals.py`, `tools/drift-audit/drift_report.py`, `tools/drift-audit/selftest.py`, `DECLARED_EMPTY` | `tools/drift-audit/drift_report.py` |
| `aMendedLedger-3-u2` S6 | a | SPECCED | GENUINE | `tools/drift-audit/SKILL.template.md`, `.claude/skills/drift-audit/SKILL.md`, `tools/check-kit-versions.sh`, `memory/map/features/review-harnesses.md`, `memory/map/generated/inventories.json` | `tools/drift-audit/README.md` |
| `aMendedLedger-4-u3` S3 | a | SPECCED | GENUINE | `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/corpus_ids.py`, `tools/memory-tree/hygiene-parity.test.sh`, `memory/map/features/memory-tree-hygiene.md` | `tools/memory-tree/check-memory-hygiene.sh` |
| `aMendedLedger-4-u3` S4 | a | SPECCED | GENUINE | `tools/memory-tree/check-memory-hygiene.sh` | `tools/memory-tree/check-memory-hygiene.sh` |
| `aMendedLedger-4-u3` S7 | a | SPECCED | GENUINE | `WIRE-INTO-PROJECT.md`, `README.md`, `memory/HYGIENE.md`, `memory/map/features/annotation-style.md` | `tools/memory-tree/check-memory-hygiene.sh` |
| `aMendedLedger-5-u5` S5 | a | SPECCED | ESCAPE | prose | NO VALUE READERS, with its reason |
| `aMendedLedger-6-u6` S1 | a | SPECCED | GENUINE | `tools/drift-audit/drift_report.py`, `_TERMINAL_SHA` | `signal_ledger` |
| `aMendedLedger-6-u6` S11 | a | SPECCED | GENUINE | `skills/session-kickoff/SKILL.md`, `WIRE-INTO-PROJECT.md`, `memory/map/features/lexicon.md`, `memory/map/features/session-kickoff.md` | `WIRE-INTO-PROJECT.md` |
| `aMendedLedger-6-u6` S5 | a | SPECCED | GENUINE | `tools/drift-audit/drift_report.py`, `WIRE-INTO-PROJECT.md`, `tools/check-dead-paths.sh`, `tools/dead-path-waivers.txt` | `signal_ledger` |
| `aMendedLedger-6-u6` S6 | a | SPECCED | GENUINE | `tools/drift-audit/drift_report.py`, `tools/drift-audit/drift_signals.py` | `signal_ledger`, `tools/drift-audit/selftest.py` |
| `aMendedLedger-7-u8` S5 | a | SPECCED | GENUINE | prose | `tools/memory-tree/merge-rows.test.sh`, `tools/memory-tree/merge-rows.py` |
| `aMendedLedger-8-u9` S11 | a | SPECCED | GENUINE | `tools/memory-tree/merge-rows.py`, `tools/memory-tree/merge-rows.test.sh`, `memory/map/features/memory-tree-merge-driver.md`, `merge.conflictStyle` | `tools/memory-tree/merge-rows.test.sh` |
| `aMendedLedger-8-u9` S2 | a | SPECCED | GENUINE | `tools/check-wiring.sh`, `memory/map/features/memory-tree-merge-driver.md` | NO VALUE READERS, with its reason |
| `aPacedTurnstile-14` S9 | a | SPECCED | GENUINE | `unattended.md`, `build-readme-surface.md` | `tools/memory-tree/check-memory-hygiene.sh`, `.memory-tree.conf` |
| `aQuarriedLantern-1` S5 | a | INPROGRESS | GENUINE | `tools/memory-recall/query.py`, `tools/memory-recall/README.md`, `tools/memory-recall/SKILL.template.md` | `tools/memory-recall/query.py`, `build_cutoff` |
| `aQuarriedLantern-1` S6 | a | INPROGRESS | ESCAPE | prose | NO VALUE READERS, with its reason |
| `aTunedCompass-3` S2 | a | BLOCKED | GENUINE | `tools/memory-recall/check-recall.py` | `tools/memory-recall/check-recall.py`, `tools/memory-recall/test_recall_floor.py`, `test_out_of_vocabulary_pin_reds` |
| `aTunedCompass-9` S2b | a | SPECCED | ESCAPE | prose | NO VALUE READERS, with its reason |
| `aTunedCompass-9` S5c-i | a | SPECCED | GENUINE | `measure_run`, `check_audit`, `test_audit_green` | `tools/memory-recall/check-recall.py` |
| `aWalkedCorpus-2` S5 | a | DEFERRED | GENUINE | `measure_run` | `tools/memory-recall/check-recall.py`, `tools/memory-recall/test_recall_floor.py` |
| `bConvergentLodestar-1` S2 | b | SPECCED | ESCAPE | prose | NO VALUE READERS, with its reason |
| `bConvergentLodestar-1` S3 | b | SPECCED | ESCAPE | `reuse-discovery.js`, then READER NOT IN TREE with its reason | NO VALUE READERS, with its reason |
| `bConvergentLodestar-1` S4 | b | SPECCED | GENUINE | `memory/map/affordance-exempt.toml`, `tools/codebase-map/map_diff.py`, `tools/codebase-map/map_lib.py`, `tools/codebase-map/selftest.py`, `tools/memory-tree/check-memory-hygiene.sh` | `tools/codebase-map/test_codebase_map.py`, `affordance_offenders` |
| `dGatedProse-3` S8 | d | SPECCED | GENUINE | the clause that spec carries, verified and not rewritten | the clause that spec carries, verified and not rewritten |
| `dPolishedVitrine-1` S10 | d | INPROGRESS | ESCAPE | prose | NO VALUE READERS, with its reason |
| `dPolishedVitrine-1` S5 | d | INPROGRESS | GENUINE | `tools/check-install-prefix.sh` | `tools/check-install-prefix.sh` |
| `dPolishedVitrine-14` S2 | d | INPROGRESS | ESCAPE | prose | NO VALUE READERS, with its reason |
| `dScaffoldedMirror-9` S5 | d | DEFERRED | GENUINE | `tools/lexicon/lexicon.py`, `tools/lexicon/kit.toml`, `tools/lexicon/selftest.py`, `tools/drift-audit/selftest.py`, `tools/lexicon/README.md`, `tools/lexicon/LEXICON.md`, `tools/lexicon/adopt-lexicon.sh`, `tools/drift-audit/drift_report.py` | `tools/lexicon/lexicon.py` |
| `dScaffoldedMirror-9` S6 | d | DEFERRED | ESCAPE | prose | NO VALUE READERS, with its reason |
| `dScaffoldedMirror-9` S7 | d | DEFERRED | ESCAPE | prose | NO VALUE READERS, with its reason |


## The one row the pass corrected, and the code behind it

`dScaffoldedMirror-9` S5 deletes the `*_OFFENDER_PIN` keys from `.lexicon.conf`, `PIN_KEYS` from
`lexicon.py`, the `lexicon-pins` hole from `kit.toml`, and three `RATCHETS` rows from
`drift_signals.py`. Section 4 through rev-7 named `tools/drift-audit/drift_signals.py:270` and `:305`
as those rows. Read at BASE, the two lines are `lexicon_verbs_declared_but_unused` and
`lexicon_ratified_older_than_language_surface` in the `PINS` table, which the item does not name, and
the `RATCHETS` list at `tools/drift-audit/drift_signals.py:352` holds no `.lexicon.conf` row at all:
the three rows were proposed by `TOOL-dScaffoldedMirror-5`, whose status is WONTDO, so they were never
written. `git grep OFFENDER_PIN` outside the memory tree returns no line of that file. It reads
nothing the item withdraws, and the corrected row drops it.

The same grep, with `PIN_KEYS` and `lexicon-pins`, found the readers the row now carries:
`tools/lexicon/lexicon.py:120` maps the two live keys and `:3053`, `:3280` and `:3292` read and
compare them; `tools/lexicon/kit.toml:177` is the hole; `tools/lexicon/selftest.py:1320`-`:1327`
asserts every key of `PIN_KEYS` is scaffolded and the dead `LAYER_OFFENDER_PIN` is not;
`tools/drift-audit/selftest.py:784`, `:918` and `:1026` write `VERB_OFFENDER_PIN` and
`SUFFIX_OFFENDER_PIN` into fixture confs; and the keys are spelled in prose at
`tools/lexicon/README.md:516` and `:593`, `tools/lexicon/LEXICON.md:175`,
`tools/lexicon/adopt-lexicon.sh:454`, and `tools/drift-audit/drift_report.py:1193` and `:1331`. The
by-value reader is unchanged: `tools/lexicon/lexicon.py:3280` is `if len(unwaived) > pin`.

This is a false reader, not an escape over readers. The by-name half is graded by resolution, and
`tools/drift-audit/drift_signals.py` is a tracked path, so check 25 would have passed the false name
for good.

## Reader evidence, re-read at BASE

Every reader file section 4 cites is byte-identical between `bd44d3ff` and BASE: `git diff --stat`
over every tracked path outside the memory tree plus the five reader carriers returns nothing. So
section 4's line anchors hold at BASE, and the pass re-read each claim by grepping the reader for
what the item withdraws. 75 claims were checked; each hit below is file and line at BASE.

- `aGradedDoorway-7` S2: `SHARD_ARITY` at `tools/unattended/check-unattended.test.sh:29` and `:46`-`:48`
  and `:3474`-`:3475`, at `tools/unattended/unattended.test.sh:37`, `:54`-`:56` and `:6814`-`:6815`,
  and at `tools/run-gates/run-gates.gov.test.sh:395`-`:400`.
- `aMendedLedger-1` S1 and `aMendedLedger-2-u1` S5: `IN-FLIGHT.md` at
  `tools/memory-tree/check-memory-hygiene.sh:501`, `tools/memory-tree/check-memory-hygiene.test.sh:1873`
  and `WIRE-INTO-PROJECT.md:315` and `:321`.
- `aMendedLedger-3-u2` S2: `in-flight/` at `tools/memory-tree/check-memory-hygiene.sh:501` and the
  scaffolder loop at `tools/memory-tree/check-memory-hygiene.test.sh:1873`; by value,
  `tools/drift-audit/drift_report.py:2031` builds the ledger directory from `project` and
  `in-flight`, and `tools/drift-audit/drift_signals.py:139` declares the probe empty.
- `aMendedLedger-3-u2` S3: `DECLARED_EMPTY` at `tools/drift-audit/drift_signals.py:124` and `:132`,
  `tools/drift-audit/drift_report.py:2156` and `:2189`, and `tools/drift-audit/selftest.py:280`; the
  `PINS` fallback at `tools/drift-audit/drift_report.py:1364`.
- `aMendedLedger-3-u2` S6: `drift-audit-state` at `tools/drift-audit/SKILL.template.md:62`,
  `.claude/skills/drift-audit/SKILL.md:62`, `tools/check-kit-versions.sh:221`,
  `memory/map/features/review-harnesses.md:23` and `memory/map/generated/inventories.json:148`; the
  lens-count record at `tools/drift-audit/README.md:27`.
- `aMendedLedger-4-u3` S3: `index_set` at `tools/memory-tree/check-memory-hygiene.sh:662` and `:700`,
  `tools/memory-tree/corpus_ids.py:563` and `:1105`, and `memory/map/features/memory-tree-hygiene.md:101`;
  the check-7 row at `tools/memory-tree/hygiene-parity.test.sh:246`; `INDEX_SET` consumed at
  `tools/memory-tree/check-memory-hygiene.sh:785`.
- `aMendedLedger-4-u3` S4: `ex7` at `tools/memory-tree/check-memory-hygiene.sh:773`, `:774` and `:785`.
- `aMendedLedger-4-u3` S7: `adopt-memory-tree.sh` at `WIRE-INTO-PROJECT.md:181` and `:237`,
  `README.md:38`, `memory/HYGIENE.md:134` and `memory/map/features/annotation-style.md:56` and `:84`.
- `aMendedLedger-6-u6` S11: the `governance-template:` marker grep at
  `skills/session-kickoff/SKILL.md:85`, the re-pull instruction at `WIRE-INTO-PROJECT.md:1732`, and
  the marker's history at `memory/map/features/lexicon.md:152` and
  `memory/map/features/session-kickoff.md:97`.
- `aMendedLedger-7-u8` S5: `keys` at `tools/memory-tree/merge-rows.test.sh:332` and `:350`-`:351`,
  and `key()` at `tools/memory-tree/merge-rows.py:213`.
- `aMendedLedger-8-u9` S2: `split_regions` at `tools/check-wiring.sh:768` and
  `memory/map/features/memory-tree-merge-driver.md:196`.
- `aMendedLedger-8-u9` S11: `merge.conflictStyle` at `tools/memory-tree/merge-rows.py:79`, `:82` and
  `:493`, `conflictStyle` at `tools/memory-tree/merge-rows.test.sh:1206` and `:1210` and at
  `memory/map/features/memory-tree-merge-driver.md:116`, `:120` and `:166`; `zdiff3` at
  `tools/memory-tree/merge-rows.test.sh:1209`.
- `dPolishedVitrine-1` S5: `--write-ratchet` at `tools/check-install-prefix.sh:82`, `:348` and `:479`.
- `aTunedCompass-3` S2: `SETS` and `SUBS` at `tools/memory-recall/check-recall.py:73`-`:74` and
  `:140`-`:143`; `test_out_of_vocabulary_pin_reds` at `tools/memory-recall/test_recall_floor.py:295`.
- `aTunedCompass-9` S5c-i: `measure_run` at `tools/memory-recall/check-recall.py:180`, the set load
  at `:183`, `check_audit` at `:248`, and `test_audit_green` at
  `tools/memory-recall/test_recall_floor.py:309`.
- `aWalkedCorpus-2` S5: the ceiling at `tools/memory-recall/check-recall.py:213` and
  `test_per_id_reds_alone` at `tools/memory-recall/test_recall_floor.py:170`.
- `aQuarriedLantern-1` S5: `--tag` at `tools/memory-recall/README.md:53` and
  `tools/memory-recall/SKILL.template.md:85`, and throughout `tools/memory-recall/query.py`;
  `build_cutoff` at `tools/memory-recall/query.py:177`.
- `aMendedLedger-1` S2: `archive/ledger` at `WIRE-INTO-PROJECT.md:321`; `signal_ledger` at
  `tools/drift-audit/drift_report.py:381`.
- `aMendedLedger-2-u1` S4: check 2's link walk at `tools/memory-tree/check-memory-hygiene.sh:436`-`:478`.
- `aMendedLedger-2-u1` S6: `IN-FLIGHT.md` rows at `tools/dead-path-waivers.txt:47`-`:48`.
- `aMendedLedger-6-u6` S1: `_TERMINAL_SHA` at `tools/drift-audit/drift_report.py:378` and the
  `merged:` vocabulary at `:375` and `:393`.
- `aPacedTurnstile-14` S9: `DOSSIER_CAP_BYTES` at `.memory-tree.conf:441`, 20480, read at
  `tools/memory-tree/check-memory-hygiene.sh:733`; `memory/map/features/unattended.md` is 20460
  bytes at BASE, as at `bd44d3ff`.
- `bConvergentLodestar-1` S4: `load_affordance_exempt` at `tools/codebase-map/map_lib.py:1217`,
  `test_affordance_exemption_drop` at `tools/codebase-map/selftest.py:820`, `affordance-exempt` at
  `tools/memory-tree/check-memory-hygiene.sh:556`, and `affordance_offenders` at
  `tools/codebase-map/test_codebase_map.py:128`.

Four of the 75 greps missed on the needle the pass first wrote, and each was re-read at source. The
directory at `tools/drift-audit/drift_report.py:2031` is built from two path parts rather than
spelled whole, so the claim holds. The marker `skills/session-kickoff/SKILL.md:85` greps is spelled
`governance-template:`, so the claim holds. `tools/lexicon/kit.toml:177` names the hole by its id
`lexicon-pins`, so the claim holds. `tools/drift-audit/drift_signals.py` spells no offender pin, and
that is the corrected row above.

The escaped set was re-read on the same terms, each against the reason its clause carries.
`evict_dead_siblings` at `tools/memory-recall/query.py:418` evicts untracked caches only.
`tools/memory-tree/merge-rows.test.sh` was first added in `a08c2f3d`, so its item creates rather than
withdraws. `memory/map/generated/symbols.json` is the artifact `bConvergentLodestar-1` S2 creates.
`git grep` finds `reuse-discovery.js` in no tracked file outside the memory tree. `dPolishedVitrine-1`
S10's pins are written and deleted inside its own rollout steps. The one lexicon arm that reads a
conf's text, `tools/lexicon/selftest.py:1315`-`:1327`, reads a conf it scaffolds into a scratch repo
and never this repo's comments. `tools/lexicon/lexicon.py` carries neither `--freeze` nor `--drain`.
`git grep -i sampl` over `tools/memory-recall/` returns nothing. The retire-to-record step is at
`tools/unattended/SKILL.template.md:171` and the corroborating read at
`tools/unattended/check-brief-recorded.sh:58`-`:63`. Each of the nine escapes stands.

## The resolver's output

The pass's own implementation of `TOOL-dGatedProse-1`'s S5 as its rev-8 text states it: a
`:<line>` tail and a trailing `()` stripped; IDENTITY when the token equals a tracked path or the
part of one after a `/`, over the whole tracked set; CONTENT when a READER spells it, the readers
being every tracked file outside `memory/` plus `memory/guides/`, `memory/map/`, `memory/HYGIENE.md`,
`memory/TEMPLATE-SPEC.md` and `memory/README.md`, narrowed by ONE `git grep -l -F -f` and filtered by
that rule over the path list, never as a pathspec. The reader set is derived from `git ls-files`:
2465 tracked files, 371 readers, 330 outside the memory tree and 41 carriers.

The tokens resolved are every token of the rows above plus every backticked token the pass writes on
a by-name half, 61 distinct:

- IDENTITY, 50: every path token of the rows, all tracked, and the two bare dossier names
  `unattended.md` and `build-readme-surface.md`, which resolve as tails of
  `memory/map/features/unattended.md` and `memory/map/features/build-readme-surface.md`.
- CONTENT, 10, each spelled by code: `DECLARED_EMPTY` and `_TERMINAL_SHA` in
  `tools/drift-audit/drift_report.py`, `signal_ledger` there too, `affordance_offenders` in
  `tools/codebase-map/map_lib.py`, `build_cutoff` in `tools/memory-recall/query.py`, `check_audit`
  and `measure_run` in `tools/memory-recall/check-recall.py`, `test_audit_green` and
  `test_out_of_vocabulary_pin_reds` in `tools/memory-recall/test_recall_floor.py`, and
  `merge.conflictStyle` in `tools/memory-tree/merge-rows.py`.
- UNRESOLVED, 1: `reuse-discovery.js`, the one token section 4 expects unresolved, which proves the
  resolver can fail. It stands on `bConvergentLodestar-1` S3's by-name half under
  READER NOT IN TREE with its reason.

No token is a path in one of S5's record classes: the pass tests each token's identity hits and
refuses any whose every hit lies under the memory root outside the five carriers, and none does.

## Verifications the pass makes and does not edit

`dGatedProse-3` S8 already carries its clause. Its three markers appear once each and in order, its
four by-name tokens resolve by identity, and its by-value half carries eleven backticked tokens and
no escape. The pass leaves its bytes alone (S6, AC7).

The reciprocal edges hold at BASE (S9, AC11): units 1, 2 and 4 each carry a **consumes-from**
bullet naming this unit in their Edges sections, this spec carries the three mirroring **hands-off**
bullets, and unit 1's header carries `order 2`. No bullet is owed.

F1's derivation: `REV_SCOPE_CUTOFF` is 2026-09-08 in `.memory-tree.conf` at BASE. Of the nineteen
specs with a write-set item, three have a filename date on or after it: `dGatedProse-3`, which is
verified and not edited, and `dPolishedVitrine-1` and `dPolishedVitrine-14`, which the node-`d`
commit bumps by one rev each with a section 9 entry naming the item's scope label. The latest
filename date among the other sixteen is 2026-09-04, so no node-`a` or node-`b` header moves (AC17).
