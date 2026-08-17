# TOOL-aRelaxedShard-1 — the row-document cap becomes one declared byte bound

**Status:** OPEN · rev-1 · 2026-08-17 · node a · Tier-2 · base 43eb6b10 · streams tooling

## 1. Goal

Hygiene check 6 caps every row document at a hardcoded 20,480 bytes and 250 lines, and on this repo
the byte half is spent: `memory/backlog/TOOL.md` holds 19,152 bytes of live rows with nothing left for
rotation to archive. Make the byte bound a declared per-repo value and retire the line bound for the
row class, so the number that binds is the one the prose names and an adopter can measure their own.

## 2. Scope (IN)

- **S1** — A new `.memory-tree.conf` key, `ROW_DOC_CAP_BYTES`, holding the byte cap check 6 applies to
  row documents. Its value here is MEASURED against this corpus and its comment records the movement,
  the way `READ_PATH_CEILING` records its four.
- **S2** — The key read in `tools/memory-tree/check-memory-hygiene.sh` beside the other conf keys, with
  an absent or blank value resolving to the kit's shipped default. A cap is never disabled by omission.
- **S3** — The per-class cap block at `tools/memory-tree/check-memory-hygiene.sh:379`: the row class
  loses its line bound and keeps only the byte bound; the guide class keeps both. The finding message
  reports the byte figures alone for a row document, because a line figure it no longer enforces reads
  as a second bound.
- **S4** — `KIT_MEMORY_TREE_VERSION` bumped off `2.18`. The diff moves a non-comment line of the
  engine, so `check-verdict-epoch.sh` requires it and `hygiene-parity.test.sh` derives its floor from it.
- **S5** — The row-class arms in `tools/memory-tree/check-memory-hygiene.test.sh` rebuilt on the BYTE
  axis. Today all three check-6 fixtures trip on line count, so the byte bound that fires in production
  has never been armed, and retiring the line bound would leave the row class with no arm at all.
- **S6** — A green arm for the retirement itself: a row document over 250 lines and under the byte cap
  must be SILENT. Without it the change is indistinguishable from raising the line cap.
- **S7** — The key added to `tools/memory-tree/.memory-tree.conf.example`, blank, with its
  absent-and-blank semantics stated where an adopter reads it. `adopt-memory-tree.sh` copies that file
  when a target has no conf, so a key missing from it is a key no adopter ever sees.
- **S8** — The prose carriers of the retired numbers, swept in one pass: `memory/HYGIENE.md` rule 6 and
  its two later restatements, the same three in `tools/memory-tree/HYGIENE.template.md`, and
  `tools/memory-tree/README.md`.
- **S9** — `memory/guides/BUILD-METHOD.md` line 8 and its kit template. Both are carriers of the
  retired figures AND mis-attribute them: they cite hygiene rule 6 for a budget rule 6 does not impose
  on a guide, which gets 61,440 bytes and 750 lines. The corrected line names the budget as
  self-imposed, because M7 re-reads that file whole and the discipline is real even though the citation
  is wrong.
- **S10** — A `memory/map/features/` dossier for the hygiene engine. It is undossiered today —
  `memory-tree` sits unclaimed at `memory/map/baseline.toml:53` — and this is a Tier-2 unit changing its
  contract, which is the map's convergence rule.

## 3. Non-goals (OUT)

- **The re-shape.** Sharding a backlog below `FAMILY`, or giving backlogs a spill tier like `RUN.md`'s,
  is the second unit the owner sequenced after this one. Its id is minted when its spec is authored, so
  that this spec cites nothing check 14 would call an orphan.
- **Byte normalisation before measuring.** `TOOL-aRootedPrefix-3` is open against checks 6 and 7 for
  measuring raw working-tree bytes, which makes the cap platform-dependent for an adopter without the
  `eol=lf` pin. It is adjacent and it is the reason a larger cap is worth more to an adopter than to
  this repo, but it is a separate mechanism and stays in its own row.
- **Check 10's blindness to shard rotations.** `TOOL-cTracedPromise-6` is open and untouched.
- **A per-class cap matrix.** One key for the whole row class, not one per document kind. See §8.
- **Raising the guide cap.** `TOOL-aWidenedGuide-1` set it and nothing here reopens it.
- **Relaxing `READ_PATH_CEILING`, the 300-char entry budget, or rotation's carry-forward rule.** All
  three stay exactly as they are; only the row byte cap and the row line cap move.

## 4. Design

### Data model

One conf key, `ROW_DOC_CAP_BYTES`, whose value is a byte count. Resolution order is the kit's usual
one: the conf value when non-blank, else the engine's shipped default. There is deliberately no value
that disables the bound. A gate an adopter can silently switch off by blanking a line is a gate that
reports green for a tree nobody is checking, and `memory/project/curation-debt.txt` already exists as
the per-file escape hatch for a document that genuinely needs one.

The guide class keeps its own hardcoded 61,440 bytes and 750 lines. If the value ratified in §8 is also
61,440 the two byte numbers coincide, and the engine comment must say that they coincide rather than
that they are the same number — `TOOL-aWidenedGuide-1` split the classes as a decision, and a later
row-class movement re-separates them.

### Inventory

Every row document in this tree, measured at the spec's base sha:

| path | bytes | rows | share of 20,480 |
|---|---|---|---|
| `memory/backlog/TOOL.md` | 19,152 | 73 | 93.5% |
| `memory/DECISIONS.md` | 12,328 | — | 60.2% |
| `memory/ledger/2026-08.md` | 3,240 | — | 15.8% |
| `memory/LIVE.md` | 2,054 | — | 10.0% |
| `memory/backlog/PLAY.md` | 1,741 | 9 | 8.5% |
| `memory/backlog/DEPL.md` | 1,734 | 11 | 8.5% |
| `memory/backlog/KICK.md` | 373 | 4 | 1.8% |

Three further measurements decide the value, and each is derived rather than estimated:

- **Row length.** 18,314 bytes across 73 rows in `memory/backlog/TOOL.md` is 251 bytes per row.
- **Minting rate.** 161 distinct `TOOL-` ids across the live shard and its three archives, first
  appearing over nine active days, is 17.9 ids per day. The last four of those days average 20.3.
- **Live-set growth.** The same nine days left 73 non-terminal rows standing, which is 8.1 live rows
  per day, or about 2,034 bytes per day.

Against those, the present 1,328 bytes of headroom is **0.65 days**. That figure, not the percentage,
is what makes this a defect rather than a tight budget.

### Why rotation cannot be the answer here

Rotation carries forward every non-`CLOSED` and non-`WONTDO` row, so the live file's floor is its live
row set. `memory/backlog/TOOL.md` holds 73 such rows and zero terminal ones: its floor IS its current
18,314 bytes, 89.4% of the cap, and a fourth rotation would move nothing. It has already rotated three
times in four days, twice on one of them. `memory/builds/cSteadyMetronome/README.md` recorded the
conclusion on 2026-08-14 and predicted today's state, including that the unit it needed could not get a
backlog row because there was no room to write one.

That build also recorded that rotation orphans ids against check 14, which is why a rotation was once
attempted and reverted. That claim looks stale and this spec does not rely on it: `corpus_ids.py`'s one
walk is `git ls-files` with no `archive/` exclusion, and three rotations have since landed green. It is
listed in §5 as a claim to confirm with a fixture rather than by reading, because it is load-bearing for
whether rotation remains a remedy at all.

### Why the line bound goes rather than moving

The two halves of the rule have never been consistent. At the 300-char entry budget a 250-line row
document may hold 75,000 bytes, so the byte bound decides every real case and the line bound can only
fire on rows averaging under 82 bytes. Measured mean row length here is 251. The line bound is not
strict, it is unreachable, and a bound that cannot fire is a number in six prose carriers with nothing
behind it.

Keeping bytes as the single row bound is also the correct choice on the merits. What check 6 exists to
bound is the cost of reading the file, and a shard of long rows costs more to read than a shard of short
ones. A byte cap prices that; a line cap does not.

The value in §8 is derived from the line bound's own evident intent: 250 scannable rows at the measured
251 bytes each is 62,750 bytes. It is not a relaxation so much as a correction of a byte figure that
was set as though rows were a third of their real length.

### The three consumers whose behaviour shifts, and by how much

- **`builds/*/RUN.md`** — unaffected in behaviour. `memory/guides/UNATTENDED-PROTOCOL.md` budgets the
  authored region at 8 KB and spills against THAT, not against check 6; the protocol calls check 6 the
  backstop whose whole purpose is never to be reached. Raising the row cap loosens the backstop and
  moves no trigger. The protocol names no byte figure, so it needs no edit — the pointer discipline held.
- **Codebase-map dossiers** — `memory/HYGIENE.md` gives them check 6's caps with SPLIT rather than
  rotation as the remedy. A larger cap means a dossier splits later. No dossier is near the bound today.
- **The generated indices** — `memory/LIVE.md` and `memory/ledger/<month>.md` are rendered, and a
  larger cap only defers the month a ledger shard would have to rotate.

### Files touched (estimate)

| path | change |
|---|---|
| `.memory-tree.conf` | the key, measured, with its movement comment |
| `tools/memory-tree/.memory-tree.conf.example` | the key, blank, with absent-and-blank semantics |
| `tools/memory-tree/check-memory-hygiene.sh` | conf read · the cap block · the finding message · kit version |
| `tools/memory-tree/check-memory-hygiene.test.sh` | byte-axis row arms · the over-250-lines green arm · assertion count |
| `memory/HYGIENE.md` | rule 6 and its two restatements |
| `tools/memory-tree/HYGIENE.template.md` | the same three, in lockstep |
| `memory/guides/BUILD-METHOD.md` | the budget line, and its mis-citation |
| `tools/memory-tree/BUILD-METHOD.template.md` | the same line |
| `tools/memory-tree/README.md` | the 250-line claim about the build method |
| `memory/map/features/` | a dossier for the hygiene engine, plus a re-render |
| `memory/DECISIONS.md` · `memory/backlog/TOOL.md` | the decision row and the follow-up rows |

### Alternatives rejected

- **Raise the constant and leave it hardcoded.** Cheapest diff, and it ships this repo's newly measured
  number to every adopter with still no knob. That is `memory/gotchas/pin-copied-from-another-corpus.md`
  by construction, and the kit has a record of the class precisely because it keeps recurring.
- **One byte cap for the whole index set, rows and guides together.** Tempting because the ratified
  value may equal the guide cap, but it dissolves `TOOL-aWidenedGuide-1`'s class split by arithmetic
  rather than by decision, and re-plumbing the guide class is a larger diff than leaving it alone.
- **A per-document-kind cap matrix.** Backlogs, decision logs, dossiers and run-state files all have
  distinct reasons for being bounded, so a matrix is arguable. Nothing needs it today, three of the four
  sit under 20% of the present cap, and the matrix is a config surface added for a case nobody has.
- **Do nothing and rotate harder.** Measured impossible: zero terminal rows remain.

## 5. Production-readiness checklist

- **security** — N/A. No new input, no write path, no surface; one gate threshold moves.
- **perf / scale** — Neutral. The awk block already computes both counts per file; one comparison is
  dropped for the row class and no new pass over the corpus is added.
- **a11y** — N/A. A shell gate with no user interface.
- **i18n** — N/A, with one live caveat already in the engine: check 7 deliberately sets no `LC_ALL`
  because character-versus-byte counting is a property of the adopter's awk. This unit adds no
  locale-sensitive comparison, and must not add one to check 6.
- **error / empty / loading states** — The absent and blank key both resolve to the shipped default,
  and a non-numeric value must fail loudly rather than coerce to zero through awk's `+0`.
- **observability** — The finding message is the whole interface. It must print the declared cap it
  applied, so an operator can tell a default from a declaration without opening the conf.
- **risks** — One rollback hazard and one silent-failure hazard. A wrong `cl` sentinel makes every row
  document red or every row document silent, and awk coerces a blank to `0`, which is the silent
  direction. Rollback is reverting one commit; nothing migrates and no data moves.
- **testing + left-shift gates** — S5 and S6 are the left-shift. The byte axis of check 6 gains its
  first arm in the kit's life, which is a coverage gain beyond this change.
- **migration / rollback** — None required. An adopter who never adds the key keeps working at the
  shipped default; a raise is a conf edit with no tree change.
- **user docs** — The kit README and both HYGIENE carriers, per S8. No end-user surface.

Two items for the owner scope menu: the ratified cap value, and whether the stale rotation-orphans-ids
claim is confirmed by fixture in this unit or parked to the re-shape unit that depends on it.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over a scratch tree whose conf
  declares no `ROW_DOC_CAP_BYTES`, the row class is capped at the engine's shipped default; an absent
  key neither widens the bound nor disables it.
- **AC2** — When a row document in that scratch tree exceeds the declared byte cap,
  `check-memory-hygiene.sh` names it and the finding reports the byte figures and the cap it applied,
  with no line figure for the row class.
- **AC3** — When a row document carries more than 250 lines and stays under the byte cap,
  `check-memory-hygiene.sh` is SILENT about it, which is the observation that separates retiring the row
  line bound from raising it.
- **AC4** — When the guide fixture `memory/guides/tfixture.md` passes 750 lines, check 6 still names it,
  proving the retirement did not reach the guide class.
- **AC5** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, its check-6 row arms fail
  on the BYTE axis, and the suite's printed assertion count has moved to match the arms added rather
  than staying at the floor `tools/check-testsuite-counts.sh` reads.
- **AC6** — When `bash tools/memory-tree/check-verdict-epoch.sh` runs over this diff it is green, and
  `KIT_MEMORY_TREE_VERSION` no longer reads `2.18`.
- **AC7** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, `memory/HYGIENE.md` and
  `tools/memory-tree/HYGIENE.template.md` agree on the rewritten rule 6, and no carrier of the retired
  figures survives `grep -rnE '20 ?KB|20480|250 lines' -- ':!memory/archive' ':!memory/builds'`.
- **AC8** — When `bash tools/memory-tree/check-method-carriers.sh` runs after S9, it is green with
  `memory/guides/BUILD-METHOD.md` and its template stating the same corrected budget line.
- **AC9** — When `python tools/codebase-map/test_codebase_map.py` runs, the hygiene engine is claimed by
  a dossier under `memory/map/features/` and the generated artifacts byte-compare against a fresh render.
- **AC10** — When `GATE_FULL=1 bash tools/run-gates.sh` runs at the push boundary it is green, and
  `memory/backlog/TOOL.md` sits under the ratified cap with the runway that value buys stated in bytes
  per day in the `.memory-tree.conf` comment.

## 7. Gates

The legs this unit must keep green, from `tools/gate-legs.json`: `memory/` hygiene · the hygiene
self-test · the harness meta-gate `check-arms.py` against the `ARMS_FLOORS` pair
`tools/memory-tree/check-memory-hygiene.sh:14:14` · verdict epoch and its self-test · kit version
markers · kit/dogfood doc parity · method carriers · testsuite counts · codebase-map coverage and
freshness · the kickoff-manifest ratchet, because both `.memory-tree.conf` and the hygiene engine are in
its `watch:` list · drift-audit records. It adds no new leg, so the four gates that trip on a new leg
are not in play.

Bug classes the checklist selects for these paths, each to be answered in the review:
`fixture-passes-by-finding-nothing` · `two-answers-to-one-question` · `vacuous-selector-empty-population`
· `pin-copied-from-another-corpus` · `gate-green-by-accident-on-generated-bytes`.

## 8. Open questions

### F1 — the ratified cap value

Three candidates, each with a stated basis rather than a preference.

| value | basis | runway at 2,034 B/day |
|---|---|---|
| 61,440 | 250 rows at the measured 251 B/row, rounded to 60 KiB — the line bound's own evident intent | ~21 days |
| 39,632 | today's 19,152 plus the flat 20,480 headroom `READ_PATH_CEILING` uses | ~10 days |
| 184,500 | a quarter of measured net growth | ~90 days |

**Recommendation: 61,440.** It is the only one derived from something already in the rule rather than
from a headroom convention borrowed from a different check, and it reframes the change as correcting a
byte figure set as though rows were a third of their real length. The third candidate is listed to be
rejected explicitly: a 180 KB backlog shard is not scannable, and the honest conclusion is that no byte
cap compatible with a readable file buys a quarter at this minting rate. That is what the re-shape unit
is for, and this fork must not be resolved by pretending otherwise.

### F2 — absent-and-blank semantics for the key

The conf carries two idioms. The `corpus_ids.py` pins read "blank turns its check off";
`RECALL_CACHE_BUDGET_MB` reads "absent is the measured default, blank is uncapped".

**Recommendation: neither — absent and blank both resolve to the shipped default, and no value
disables the bound.** Check 6 is the rule the kit exists to enforce, an off switch reachable by
deleting a value is one an adopter reaches by accident, and `curation-debt.txt` is already the
deliberate per-file exemption. This is the one place the spec argues against the local convention, so
it is the fork most worth overruling if the owner reads the consistency cost as higher.

### F3 — one row-class key, or a per-document-kind matrix

Backlog shards, the decision log, map dossiers and run-state files share a cap and do not share a
reason for having one.

**Recommendation: one key for the row class.** Three of the four sit under 20% of the present cap, the
run-state file's real bound is the protocol's own 8 KB authored budget, and a dossier's remedy is a
split rather than a rotation. A matrix is a config surface for a case nobody has. Revisit only if the
re-shape unit needs per-kind bounds, at which point it will say so.

### F4 — confirm or park the stale rotation claim

`memory/builds/cSteadyMetronome/README.md` records that rotating a backlog orphans every id the moved
rows defined. Reading `corpus_ids.py` says otherwise and three landed rotations agree with the reading.

**Recommendation: confirm it by fixture in this unit.** It is two arms in a suite this unit is already
editing, and the re-shape unit's options depend on whether rotation is a live remedy or a dead one. A
claim this load-bearing should not be retired by a reading of the source alone.

## 9. Revision log

- rev-1 · 2026-08-17 · initial draft. Authored this run, so unreviewed by definition; the M4 spec audit
  is the next pass. Grounded on the base sha in the status header, with every figure in §4 measured at
  that base rather than quoted from prose.

## 10. Reuse audit

**The seam this unit extends** is the per-class cap block already in the engine at
`tools/memory-tree/check-memory-hygiene.sh:379`, together with the conf-key convention the same file
uses for `READ_PATH_CEILING`, `UNIVERSAL_BUDGET` and `ROW_DUPLICATE_PIN`. Nothing new is introduced:
`TOOL-aWidenedGuide-1` built the class split and this unit changes one class's bounds inside it.

`python tools/codebase-map/reuse_lookup.py "index file size cap and rotation for backlog shards"`
returned no seam that fits. Its ranked candidates were name-stem coincidences — `build_index` in
`tools/memory-recall/bench.py`, `tracked_files` in `tools/lexicon/lexicon.py`, `backlog_keys` and
`append_backlog` in `tools/codebase-map/map_lib.py` — none of which touch a size bound. Recorded as an
answer, not a failure to retry.

`python tools/memory-recall/query.py` was run with the question "why is the backlog shard size cap 20 KB
and can it be raised for adopters" and these terms verbatim, so that M7 can re-run it: `backlog shard
index size cap rotation carry-forward entry budget hygiene check 6 row document curation sweep 20480
adopters`. It returned 39 hits over 316 records. The four that bind are `TOOL-aWidenedGuide-1` (the
class split, and the recorded refusal to relax the row class), `memory/builds/cSteadyMetronome/README.md`
(the exhausted-rotation finding), `TOOL-aRootedPrefix-3` (raw-byte measurement, the adopter half) and
`TOOL-cTracedPromise-6` (check 10's blindness to shard rotations).

**Where a hit and the source disagreed.** cSteadyMetronome's rotation-orphans-ids claim is contradicted
by `corpus_ids.py`, whose one walk enumerates `git ls-files` with no `archive/` exclusion, and by three
rotations landing green since it was written. The spec treats the record as stale and F4 turns the
reading into a fixture rather than acting on either.
