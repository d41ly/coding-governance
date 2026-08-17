# TOOL-aRelaxedShard-1 — the row-document byte cap becomes a declared value

**Status:** OPEN · rev-2 · 2026-08-17 · node a · Tier-2 · base 43eb6b10 · streams tooling

## 1. Goal

Hygiene check 6 caps every row document at a hardcoded 20,480 bytes, and on this repo that bound is
spent: `memory/backlog/TOOL.md` is at 19,152 of 20,480 bytes with no terminal rows left for rotation to
archive. Make the byte bound a declared per-repo value so this tree can raise it against its own
measurement while every adopter keeps today's behaviour until they measure their own.

## 2. Scope (IN)

- **S1** — A new `.memory-tree.conf` key, `ROW_DOC_CAP_BYTES`, holding the byte cap check 6 applies to
  the row class. Its value here is MEASURED against this corpus and its comment records the movement,
  the way `READ_PATH_CEILING` records its four.
- **S2** — The key resolved in `tools/memory-tree/check-memory-hygiene.sh` with three branches, because
  the engine's own conf idiom produces the wrong answer for two of them. The engine pre-sets defaults
  and THEN sources the conf, so a blank line overrides a default with blank; this key therefore needs an
  explicit re-normalisation AFTER the source. Absent resolves to the shipped default. Blank resolves to
  the shipped default, not to "off" — check 6 is the rule the kit exists to enforce and
  `memory/project/curation-debt.txt` is already the deliberate per-file exemption. A non-numeric value
  refuses before the scan with `exit 2`, matching the conf-validation precedent at
  `tools/memory-tree/check-memory-hygiene.sh:101`.
- **S3** — The shipped default stays **20,480**. An adopter who never adds the key gets byte-for-byte
  today's verdicts, which is what keeps this unit out of
  `memory/gotchas/pin-copied-from-another-corpus.md`: this corpus's measured number is DECLARED here,
  never shipped as anyone else's default.
- **S4** — The byte comparison in the per-class cap block at
  `tools/memory-tree/check-memory-hygiene.sh:379` reads the resolved value for the row class. The guide
  class keeps its own `61440` and `750` untouched, and the row class keeps its `250`-line bound
  untouched — see §3.
- **S5** — `KIT_MEMORY_TREE_VERSION` bumped off `2.18`. The diff moves a non-comment line of the engine,
  so `check-verdict-epoch.sh` requires it and `hygiene-parity.test.sh` derives its floor from it.
- **S6** — A BYTE-axis arm for check 6's row class in
  `tools/memory-tree/check-memory-hygiene.test.sh`, plus a green control under the declared cap. This is
  the unit's real coverage gain: all three existing check-6 fixtures are line-axis constructions, so the
  byte bound that fires in production has never been armed. The arm is ADDED, never substituted — the
  three line-axis fixtures stay exactly as they are, for the reasons in §3.
- **S7** — An arm asserting `tools/memory-tree/.memory-tree.conf.example` declares the key. Nothing else
  reads that file: `adopt-memory-tree.sh:40` only copies it and `tools/check-install-prefix.sh:17`
  excludes `*.conf.example`, so without this arm S8 can be forgotten silently.
- **S8** — The key added to `tools/memory-tree/.memory-tree.conf.example` **with the shipped default's
  value**, in that file's policy-ceiling idiom rather than blank. Blank there means "check off" for every
  measured pin, while both policy ceilings — `UNIVERSAL_BUDGET` and `ROW_DUPLICATE_PIN` — ship with a
  value and say why. This key is the same kind.
- **S9** — `FLOOR_ASSERTIONS` in the hygiene self-test raised to the new executed count, so the arms S6
  and S7 add cannot later go dark without a diff.
- **S10** — The byte-figure prose carriers, enumerated by line rather than by count:
  `memory/HYGIENE.md:66`, `:128`, `:132` and `:276`, the four mirrors at the same lines in
  `tools/memory-tree/HYGIENE.template.md`, `tools/memory-tree/README.md`, and `.gitattributes:26` and
  `:30`. The `250`-line figures in those carriers stay, because the line bound stays.
- **S11** — Rule 6's spill clause corrected in both HYGIENE carriers (`memory/HYGIENE.md:133-136` and
  its lockstep twin). It says check 6's cap is what `builds/*/RUN.md` spills against;
  `memory/guides/UNATTENDED-PROTOCOL.md:130-132` budgets the authored region at 8 KB and spills against
  THAT, with check 6 as the backstop. Raising the byte cap widens the gap and makes the sentence more
  wrong. Same mis-attribution class as S12, one file over.
- **S12** — `memory/guides/BUILD-METHOD.md` line 8 and its kit template. Both cite hygiene rule 6 for a
  budget rule 6 does not impose on a guide, which gets 61,440 bytes and 750 lines. The corrected line
  names the budget as self-imposed. The discipline is real, because M7 re-reads that file whole; the
  citation is wrong.
- **S13** — `TOOL-cSettledDocket-16` closed against this unit. It is this unit's problem statement,
  already filed and OPEN, and landing without closing it leaves a stale duplicate in the very shard the
  unit exists to unblock.
- **S14** — A `memory/map/features/` dossier for the hygiene engine, and `memory-tree` deleted from
  `memory/map/baseline.toml:53` in the same commit, because the coverage gate reds on a baseline line
  whose key a dossier now claims.

## 3. Non-goals (OUT)

- **Retiring the row class's 250-line bound.** rev-1 scoped this and the M4 audit falsified its premise:
  the line bound is the OPERATIVE bound on 22 of the 29 row documents, including all 12 map dossiers,
  where check 6 is the only gate that bounds anything. It is now fork F5, re-opened with the correct
  measurement, and it is OUT until the owner answers.
- **The re-shape.** Sharding a backlog below `FAMILY`, or a spill tier like the run-state file's, is the
  second unit the owner sequenced after this one. Its id is minted when its spec is authored, so that
  this spec cites nothing check 14 would call an orphan.
- **Byte normalisation before measuring.** `TOOL-aRootedPrefix-3` is open against checks 6 and 7 for
  measuring raw working-tree bytes, which makes the cap platform-dependent for an adopter without the
  `eol=lf` pin. It is why a larger declared cap is worth more to an adopter than to this repo, and it is
  a separate mechanism.
- **Check 10's blindness to shard rotations.** `TOOL-cTracedPromise-6` is open and untouched.
- **A per-document-kind cap matrix.** One key for the row class. See F3.
- **The guide class.** `TOOL-aWidenedGuide-1` set `61440` and `750` and nothing here reopens it.
- **`READ_PATH_CEILING`, the 300-char entry budget, and rotation's carry-forward rule.** All three stay
  exactly as they are. The `20480` at `.memory-tree.conf:57` and `tools/memory-tree/corpus_ids.py:461`
  belongs to `READ_PATH_CEILING`'s headroom and is not this unit's number.

## 4. Design

### Data model

One conf key, `ROW_DOC_CAP_BYTES`, holding a byte count. Resolution has three branches and one
non-obvious step. The engine pre-sets its defaults and then sources the conf at
`tools/memory-tree/check-memory-hygiene.sh:27`, so a blank conf line overrides a pre-set default with
blank — every existing key in that block documents blank as skip, which is the opposite of what this key
needs. The design therefore re-normalises AFTER the source: an empty resolved value is reset to the
shipped default. A non-numeric value refuses with `exit 2` before the scan.

There is deliberately no value that disables the bound, and the shipped default stays 20,480 so that
nothing an adopter receives changes until they declare their own.

The guide class keeps its own hardcoded pair. If the value ratified in F1 is 61,440 the two byte numbers
coincide, and the engine comment must say they coincide rather than that they are one number —
`TOOL-aWidenedGuide-1` split the classes as a decision, and a later row-class movement re-separates them.

### Inventory

Check 6's row class is `INDEX_SET` minus `memory/guides/`: **29 files** at base, against 4 guides. The
population is `tools/memory-tree/check-memory-hygiene.sh:337-359` and the only class override is
`index(f, gp) == 1` at `:385`.

The seven largest row documents, and then the sub-populations rev-1 omitted:

| path | bytes | lines | rows | share of 20,480 | share of 250 lines |
|---|---|---|---|---|---|
| `memory/backlog/TOOL.md` | 19,152 | 78 | 73 | 93.5% | 31.2% |
| `memory/map/features/memory-tree-merge-driver.md` | 14,713 | 197 | — | 71.8% | 78.8% |
| `memory/builds/cBriefedPilot/RUN.md` | 13,806 | 151 | — | 67.4% | 60.4% |
| `memory/DECISIONS.md` | 12,328 | 69 | — | 60.2% | 27.6% |
| `memory/map/features/unattended.md` | 11,751 | 171 | — | 57.4% | 68.4% |
| `memory/map/features/lexicon.md` | 11,403 | 190 | — | 55.7% | 76.0% |
| `memory/builds/aSealedCaravan/RUN.md` | 8,141 | 114 | — | 39.8% | 45.6% |

| sub-population | members | max bytes | max lines |
|---|---|---|---|
| `memory/map/features/*.md` dossiers | 12 | 14,713 | 197 |
| `memory/builds/*/RUN.md` | 5 | 13,806 | 151 |
| `memory/backlog/*.md` | 4 | 19,152 | 78 |
| generated indices and ledgers | 3 | 12,328 | 69 |
| other row documents | 5 | 2,695 | 35 |

**Which bound binds first: 22 of 29 are LINE-bound.** The break-even is 20,480/250 = 81.92 bytes per
line. Every one of the 12 dossiers sits below it, as do 4 of the 5 run-state files, both ledger shards,
`memory/README.md`, `memory/map/README.md`, `memory/map/FOUNDATION.md` and
`memory/builds/aPrunedCeremony/STATUS.md`. Only 7 documents are byte-bound first, and they are the four
backlog shards, the decision log, `memory/LIVE.md` and `memory/builds/cBriefedPilot/RUN.md`.

Three measurements decide the value, each derived rather than estimated:

- **Row length.** `wc -c` over the dash rows of `memory/backlog/TOOL.md` is 18,519 bytes across 73 rows,
  so 253.7 bytes per row. This is a BYTE count, which is what check 6 measures; a character count reads
  18,314, and the `·` separators are two bytes each.
- **Minting rate.** 156 of the 161 distinct `TOOL-` ids across the live shard and its three archives
  first appear inside the nine-day window, which is 17.3 ids per day.
- **Live-set growth.** Those nine days left 73 non-terminal rows standing: 8.1 rows per day, about
  2,057 bytes.

Against those, the remaining 1,328 bytes of headroom is **0.65 days**. That figure, not the percentage,
is what makes this a defect rather than a tight budget.

### Why rotation cannot be the answer here

Rotation moves terminal rows only and carries forward everything else, so the live file's floor is what
survives it. `memory/backlog/TOOL.md` has 66 OPEN, 6 SPECCED, 1 DEFERRED and zero terminal rows, so a
fourth rotation leaves the whole 19,152-byte file exactly where it is — the floor is 93.5% of the cap,
not some smaller row-only figure, because the 633-byte head with its three rotation announcements stays
too. It has already rotated three times in four days, twice on one of them.

This was filed. `TOOL-cSettledDocket-16` is OPEN in that shard and states the same thing, and
`memory/builds/cSteadyMetronome/README.md` recorded it on 2026-08-14 including the detail that the unit
it needed could not be given a backlog row because there was no room to write one. S13 closes the row.

That build also recorded that rotation orphans ids against check 14, which is why a rotation was once
attempted and reverted. That claim looks stale and this spec does not rely on it: `corpus_ids.py`'s one
walk is `git ls-files` with no `archive/` exclusion, and three rotations have since landed green. F4
turns the reading into a fixture rather than acting on either.

### Why the line bound is NOT retired

rev-1 argued the 250-line bound "cannot fire" from the break-even arithmetic — true — and then tested it
against one document. Over the real population it is false 22 times out of 29. The nearest-to-cap row
document in the tree on either axis is `memory/map/features/memory-tree-merge-driver.md` at 197 of 250
lines (78.8%) against 14,713 of 20,480 bytes (71.8%): the line bound is the closer of the two, today, on
the axis rev-1 called unreachable.

It binds hardest exactly where nothing else does. Dossiers are row class by construction, their declared
remedy is a SPLIT rather than a rotation, and `tools/codebase-map/test_codebase_map.py` carries no size
predicate of its own — so check 6 is the only thing bounding a dossier at all. Retiring the line bound
and adopting F1's value would take a dossier from an effective ~14.5 KB ceiling at its measured density
to 61,440 bytes: a 3.3x to 4.3x loosening of precisely the class `TOOL-aWidenedGuide-1` refused to
triple, in the words the engine still carries at `:376-378`.

Narrowing to the byte bound also makes that loosening inert rather than merely unratified. A dossier at
~58 bytes per line reaches its 250-line bound around 14.5 KB, so raising the byte cap above that changes
nothing for the 22 line-bound documents. The unit's effect lands only on the 7 byte-bound ones, which
are the backlog shards and the decision log — the documents the owner asked about.

### The three consumers whose behaviour shifts, and by how much

- **`builds/*/RUN.md`** — unaffected in behaviour. The protocol budgets the authored region at 8 KB and
  spills against that; check 6 is the backstop whose purpose is never to be reached. Raising the byte cap
  loosens the backstop and moves no trigger. Four of the five run-state files are line-bound anyway. The
  protocol names no byte figure, so it needs no edit; rule 6's clause that contradicts it does, and S11
  is that edit.
- **Codebase-map dossiers** — effectively unaffected, per the paragraph above: all 12 are line-bound
  first and the line bound does not move. rev-1 claimed "No dossier is near the bound today"; the
  measured answer is 14,713 bytes and 197 of 250 lines, which is nearer than anything else in the class.
- **The generated indices** — `memory/LIVE.md` and the ledger shards are rendered, and a larger byte cap
  only defers the month a ledger shard would have to rotate.

### Files touched (estimate)

| path | change | forced by |
|---|---|---|
| `.memory-tree.conf` | the key, measured, with its movement comment | S1 |
| `tools/memory-tree/.memory-tree.conf.example` | the key with the shipped default's value | S8 |
| `tools/memory-tree/check-memory-hygiene.sh` | conf read and re-normalisation · the byte comparison · the finding message · kit version | S2 S4 S5 |
| `tools/memory-tree/check-memory-hygiene.test.sh` | the byte-axis arms · the example-conf arm · `FLOOR_ASSERTIONS` | S6 S7 S9 |
| `memory/HYGIENE.md` | the four byte carriers · rule 6's spill clause | S10 S11 |
| `tools/memory-tree/HYGIENE.template.md` | the same, in lockstep | S10 S11 |
| `tools/memory-tree/README.md` | the byte figure | S10 |
| `.gitattributes` | the two present-tense cap claims at `:26` and `:30` | S10 |
| `memory/guides/BUILD-METHOD.md` · `tools/memory-tree/BUILD-METHOD.template.md` | the budget line and its mis-citation | S12 |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` · `memory/TEMPLATE-SPEC.md` | the kit marker, paired by `kit-dogfood-parity.test.sh:53` | S5 |
| `memory/guides/SESSION-KICKOFF.md` | the manifest re-stamp; three watched files move | S1 S2 S12 |
| `memory/map/features/` · `memory/map/baseline.toml` | the dossier, and the baseline line it claims | S14 |
| `memory/DECISIONS.md` · `memory/backlog/TOOL.md` | the decision row, and closing `TOOL-cSettledDocket-16` | S13 |

### Alternatives rejected

- **Raise the constant and leave it hardcoded.** Cheapest diff, and it ships this corpus's measured
  number to every adopter with no knob. That is `pin-copied-from-another-corpus` by construction, which
  is also why S3 keeps the shipped default at 20,480 rather than at whatever F1 ratifies.
- **Retire the row line bound as well** — rev-1's shape, now F5. Rejected as a default by the
  measurement above: it removes the operative bound from 22 of 29 documents and triples the dossier
  allowance that a ratified decision refused to triple.
- **One byte cap for the whole index set.** Dissolves `TOOL-aWidenedGuide-1`'s class split by arithmetic
  rather than by decision, and re-plumbing the guide class is a larger diff than leaving it alone.
- **A per-document-kind matrix.** See F3. Nothing needs it today.
- **Do nothing and rotate harder.** Measured impossible: zero terminal rows remain.

## 5. Production-readiness checklist

- **security** — N/A. No new input, no write path, no surface; one gate threshold becomes declared.
- **perf / scale** — Neutral. The awk block already computes both counts per file and no new pass over
  the corpus is added.
- **a11y** — N/A. A shell gate with no user interface.
- **i18n** — N/A, with one live caveat the engine already carries: check 7 deliberately sets no `LC_ALL`
  because character-versus-byte counting is a property of the adopter's awk. This unit adds no
  locale-sensitive comparison, and rev-1's own row-length figure was wrong by exactly that confusion.
- **error / empty / loading states** — Three branches, all in S2: absent and blank both resolve to the
  shipped default after an explicit post-source re-normalisation, and a non-numeric value refuses with
  `exit 2` before the scan.
- **observability** — The finding message is the whole interface. It must print the cap it applied, so an
  operator can tell a default from a declaration without opening the conf.
- **risks** — Two directions, and rev-1 named the wrong one as silent. A blank or zero byte cap is the
  LOUDEST failure available: measured on this repo's awk, `19152 > ""`, `19152 > 0` and an uninitialised
  right-hand side all evaluate true, so the whole class reds at once and announces itself. The genuinely
  silent direction is an over-large declared value, which is why the value is a measured declaration with
  its movement recorded rather than a round number. Rollback is reverting one commit; nothing migrates.
- **testing + left-shift gates** — S6, S7 and S9 are the left-shift. The byte axis of check 6 gains its
  first arm in the kit's life, which is coverage this repo did not have before the unit.
- **migration / rollback** — None required. An adopter who never adds the key keeps today's verdicts
  exactly, because S3 keeps the shipped default at the present value.
- **user docs** — The kit README and both HYGIENE carriers, per S10. No end-user surface.

Two items for the owner scope menu: the declared value (F1), and whether the row line bound is retired
at all (F5, which rev-1 assumed and this rev does not).

## 6. Acceptance criteria

- **AC1a** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over a scratch tree whose conf
  declares no `ROW_DOC_CAP_BYTES`, the row class is capped at the shipped default.
- **AC1b** — When that conf declares `ROW_DOC_CAP_BYTES=` blank, the row class is capped at the shipped
  default and not left unbounded, which is the branch fork F2 is about and the one the engine's own
  pre-set-then-source idiom gets wrong.
- **AC1c** — When that conf declares a non-numeric value, `check-memory-hygiene.sh` refuses with
  `exit 2` before scanning, naming the key and the value.
- **AC2** — When a row document exceeds the declared byte cap, `check-memory-hygiene.sh` names it and the
  finding reports the measured bytes and the cap it applied, so a default is distinguishable from a
  declaration in the output alone.
- **AC3** — When a row document sits under the declared byte cap and over the old 20,480,
  `check-memory-hygiene.sh` is SILENT about it on the byte axis while still naming it if it passes 250
  lines, which is the observation that proves the byte bound moved and the line bound did not.
- **AC4** — When the guide fixtures run, `memory/guides/tfixture.md` past 750 lines is still NAMED and
  `memory/guides/twide.md` at 401 lines is still SILENT, proving the classes are still separate.
- **AC5** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, its new check-6 row arms
  fail on the BYTE axis, the three existing line-axis fixtures are unchanged, and `FLOOR_ASSERTIONS` in
  that file has been raised to the new executed count.
- **AC6** — When `bash tools/memory-tree/check-verdict-epoch.sh` runs over this diff it is green, and
  `KIT_MEMORY_TREE_VERSION` no longer reads `2.18`.
- **AC7** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs it is green, which is the gate
  that pairs `memory/HYGIENE.md` with its template, `memory/TEMPLATE-SPEC.md` with
  `tools/memory-tree/SPEC-TEMPLATE.template.md`, and `memory/guides/BUILD-METHOD.md` with its template —
  so it is also what observes S12's corrected budget line in both carriers.
- **AC8** — When `git grep -nE '20 ?KB|20,?480'` runs over the explicit S10 carrier list, no listed
  carrier still states the retired byte figure. Expected survivors elsewhere, each for a stated reason:
  `memory/DECISIONS.md:41` (the ratified `TOOL-aWidenedGuide-1` row, in an append-only log),
  `.memory-tree.conf:57` and `tools/memory-tree/corpus_ids.py:461` (`READ_PATH_CEILING`'s headroom, out
  of scope per §3), the engine's own shipped default (S3 keeps it at 20,480), and
  `tools/memory-tree/check-memory-hygiene.test.sh` fixtures. The criterion is scoped to a path list
  precisely because a tree-wide zero-survivor sweep is unsatisfiable.
- **AC9** — When `bash tools/check-testsuite-counts.sh` and `bash tools/memory-tree/check-arms.py` run,
  both are green, with the hygiene gate's `ARMS_FLOORS` pair unchanged at `14:14` because no `fail`
  branch is added or removed.
- **AC10** — When `python tools/codebase-map/test_codebase_map.py` runs, the hygiene engine is claimed by
  a dossier under `memory/map/features/`, `memory-tree` is gone from `memory/map/baseline.toml`, and the
  generated artifacts byte-compare against a fresh render.
- **AC11** — When `bash skills/session-kickoff/manifest-check.sh` runs it exits 0, because three files in
  its `watch:` list moved and `memory/guides/SESSION-KICKOFF.md` was re-stamped in the same change.
- **AC12** — When `GATE_FULL=1 bash tools/run-gates.sh` runs at the push boundary it is green,
  `memory/backlog/TOOL.md` sits under the declared cap, and `TOOL-cSettledDocket-16` reads CLOSED against
  this unit.

## 7. Gates

The legs this unit must keep green, from `tools/gate-legs.json`: `memory/` hygiene · the hygiene
self-test · the harness meta-gate `check-arms.py` against the `ARMS_FLOORS` pair
`tools/memory-tree/check-memory-hygiene.sh:14:14` · verdict epoch and its self-test · kit version
markers · kit/dogfood doc parity · method carriers · testsuite counts · codebase-map coverage and
freshness · the kickoff-manifest ratchet, because `.memory-tree.conf`,
`tools/memory-tree/check-memory-hygiene.sh` and `memory/guides/BUILD-METHOD.md` are all in its `watch:`
list · drift-audit records. It adds no new leg, so the four gates that trip on a new leg are not in play.

Bug classes the checklist selects for these paths, each answered in the M4 record and re-answerable at
the closing review: `fixture-passes-by-finding-nothing` · `two-answers-to-one-question` ·
`vacuous-selector-empty-population` · `pin-copied-from-another-corpus` ·
`gate-green-by-accident-on-generated-bytes`.

## 8. Open questions

### F1 — the declared value for THIS repo

S3 fixes the shipped default at 20,480, so this fork decides only what this tree declares. Runway is
measured from today's 19,152 bytes at 2,057 bytes per day, on one convention for all three rows.

| value | basis | runway |
|---|---|---|
| 61,440 | 250 rows at the measured 253.7 B/row is 63,425, rounded to 60 KiB | ~21 days |
| 39,632 | today's 19,152 plus the flat 20,480 headroom `READ_PATH_CEILING` uses | ~10 days |
| 184,500 | a quarter of measured net growth | ~80 days |

**Recommendation: 61,440.** It is the only candidate derived from something already in the rule rather
than from a headroom convention borrowed from another check. The third row is listed to be rejected
explicitly: a 180 KB backlog shard is not scannable, and the honest conclusion is that no byte cap
compatible with a readable file buys a quarter at this minting rate. That is what the re-shape unit is
for, and this fork must not be resolved by pretending otherwise.

### F2 — absent-and-blank semantics

The conf carries two idioms. The measured pins read "blank turns its check off"; the two policy ceilings
ship with a value and say why.

**Recommendation: absent and blank both resolve to the shipped default, and no value disables the
bound** — the policy-ceiling idiom, which this key matches. Note that the engine's pre-set-then-source
order means this needs the explicit re-normalisation S2 specifies; the naive spelling gives the opposite
behaviour, which is what makes this a design decision rather than a preference.

### F3 — one row-class key, or a per-document-kind matrix

Backlog shards, the decision log, map dossiers and run-state files share a cap and do not share a reason
for having one. Measured maxima against 20,480: backlog shard 93.5%, largest dossier 71.8%, largest
run-state file 67.4%, decision log 60.2%. None is under 20%, so rev-1's stated basis for rejecting the
matrix was simply false.

**Recommendation: still one key, on the grounds that survive.** The run-state file's real bound is the
protocol's 8 KB authored budget; a dossier's remedy is a split and, with F5 answered NO, its operative
bound is the line count this unit does not touch. So the byte cap is load-bearing for one sub-population
— the backlog shards and the decision log — and a matrix would be four knobs for one live case.

### F4 — confirm or park the stale rotation claim

`memory/builds/cSteadyMetronome/README.md` records that rotating a backlog orphans every id the moved
rows defined. Reading `corpus_ids.py` says otherwise and three landed rotations agree with the reading.

**Recommendation: confirm it by fixture in this unit.** It is two arms in a suite this unit is already
editing, and the re-shape unit's options depend on whether rotation is a live remedy or a dead one.

### F5 — the row line bound, re-opened

**This fork was answered once already, and the answer rested on a premise the M4 audit falsified.** The
owner chose to retire the row class's 250-line bound on rev-1's recommendation that it "cannot fire".
Measured over the real population it is the bound that binds FIRST on 22 of 29 row documents, all 12
dossiers among them, and check 6 is the only gate bounding a dossier at all. Retiring it with F1's value
would loosen the dossier allowance 3.3x to 4.3x — the exact loosening `TOOL-aWidenedGuide-1` refused.

**Recommendation: do not retire it.** §1's goal is met by the byte bound alone, the narrowing is a
strictly smaller diff, it keeps the three existing line-axis arms intact instead of rebuilding one of
them, and it leaves the byte raise inert for the 22 documents where the line bound already binds — which
is the same thing as saying the raise reaches only the documents the owner asked about.

If the owner still wants the line bound retired, the buildable shape is a SECOND declared bound rather
than a deletion: a per-class line value that keeps the dossier and run-state sub-populations bounded
while the backlog shards go byte-only. That is a materially larger unit, and it belongs with the
re-shape rather than here.

## 9. Revision log

- rev-1 · 2026-08-17 · initial draft. Authored this run, so unreviewed by definition.
- rev-2 · 2026-08-17 · folded the M4 spec audit recorded at
  `reviews/2026-08-17-review-TOOL-aRelaxedShard-1.md` — verdict BLOCKED, 55 raw, 38 confirmed, 17
  refuted, precision 0.69, 4 of 4 lenses, 21 distinct defects. The blocker rescoped the unit: retiring
  the row line bound left §3 for fork F5, because the bound binds first on 22 of 29 row documents and
  rev-1 had measured one. §4's Inventory now carries the whole 29-member class with a lines axis and the
  sub-population maxima, which is what hid the blocker. Corrected figures: row length 253.7 B by `wc -c`
  and not 251 by character count, the rotation floor is the whole 19,152-byte file at 93.5% and not
  89.4%, minting is 17.3 ids/day, and F1's third candidate runs 80 days on its neighbours' formula and
  not 90. Also: the shipped default is now stated and pinned at 20,480 (S3), the blank and non-numeric
  branches gained scope items and criteria, AC8's sweep became a runnable scoped `git grep` with its
  expected survivors named, AC7 moved onto the gate that actually pairs the carriers, four
  gate-mandated files entered the files-touched table, the carrier list is enumerated by line, rule 6's
  spill clause and `.gitattributes` entered the sweep, and `TOOL-cSettledDocket-16` — already OPEN for
  this exact defect and missed by rev-1's recall probe — is closed by S13.

## 10. Reuse audit

**The seam this unit extends** is the per-class cap block at
`tools/memory-tree/check-memory-hygiene.sh:379`, together with the conf-key convention of
`.memory-tree.conf` itself. rev-1 attributed that convention to the engine; it is wrong. The engine
mentions `READ_PATH_CEILING` only in a prose comment at `:375` and contains neither `UNIVERSAL_BUDGET`
nor `ROW_DUPLICATE_PIN`. The actual readers are `tools/memory-tree/corpus_ids.py:74`,
`tools/memory-tree/gotchas.py:84` and `tools/memory-tree/row_grammar.py:42`. The correction matters
because the engine's own six keys are pre-set defaults followed by a source, so copying its idiom yields
the blank-disables-the-bound behaviour §4 forbids — which is why S2 specifies a re-normalisation step.

`TOOL-aWidenedGuide-1` is the decision this unit sits inside. rev-1 framed it as a seam extended; with
F5 recommended NO it genuinely is extended rather than reopened, because the row class keeps the line
bound that decision left in place. If F5 is answered YES, §10 must be rewritten to name the decision as
reopened.

`python tools/codebase-map/reuse_lookup.py "index file size cap and rotation for backlog shards"`
returned no seam that fits. Its ranked candidates were name-stem coincidences — `build_index` in
`tools/memory-recall/bench.py`, `tracked_files` in `tools/lexicon/lexicon.py`, `backlog_keys` and
`append_backlog` in `tools/codebase-map/map_lib.py` — none of which touch a size bound.

`python tools/memory-recall/query.py` was run with the question "why is the backlog shard size cap 20 KB
and can it be raised for adopters" and these terms verbatim, so that M7 can re-run it: `backlog shard
index size cap rotation carry-forward entry budget hygiene check 6 row document curation sweep 20480
adopters`. The records that bind are `TOOL-aWidenedGuide-1`, `TOOL-cSettledDocket-16` (this unit's
problem statement, already filed and OPEN, returned at rank 13 and missed when rev-1 read the results),
`memory/builds/cSteadyMetronome/README.md`, `TOOL-aRootedPrefix-3` and `TOOL-cTracedPromise-6`.

**Two limits on that probe, recorded rather than implied.** It caps the result set at about 40 hits, so
its output is not evidence of absence — and six of today's forty slots are this build's own records,
which did not exist when rev-1 ran it, so re-running it does not reproduce rev-1's ranking.

**Where a hit and the source disagreed.** cSteadyMetronome's rotation-orphans-ids claim is contradicted
by `corpus_ids.py`, whose one walk enumerates `git ls-files` with no `archive/` exclusion, and by three
rotations landing green since it was written. The spec treats the record as stale and F4 turns the
reading into a fixture rather than acting on either.
