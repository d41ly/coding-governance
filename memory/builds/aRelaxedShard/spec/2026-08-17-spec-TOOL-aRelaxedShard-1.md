# TOOL-aRelaxedShard-1 — the row class becomes declared byte bounds

**Status:** CLOSED · rev-8 · 2026-08-17 · node a · Tier-2 · base 52f9bbb0 · streams tooling · ratified 2026-08-17

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-17-review-TOOL-aRelaxedShard-1-round2.md](../reviews/2026-08-17-review-TOOL-aRelaxedShard-1-round2.md) | spec-audit | — |
| [2026-08-17-review-TOOL-aRelaxedShard-1.md](../reviews/2026-08-17-review-TOOL-aRelaxedShard-1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

Hygiene check 6 caps every row document at a hardcoded 20,480 bytes and 250 lines, and on this repo the
byte bound is spent: the tooling backlog shard has no terminal rows left for rotation to archive. Make
the byte bound declared per-repo — 61,440 for the row class here, with map dossiers carrying their own
declared bound — and retire the row class's line bound, so that a declared byte number is what bounds
each class. The retirement is a ratified owner decision to relax a curation discipline, not a claim that
the bound was inert; §4 prices what it costs and the dossier key is what keeps the price bounded.

## 2. Scope (IN)

- **S1** — A new `.memory-tree.conf` key, `ROW_DOC_CAP_BYTES`, declared **61,440** here. Its comment
  records the derivation and the movement, the way `READ_PATH_CEILING` records its four.
- **S1b** — A second key, `DOSSIER_CAP_BYTES`, declared **20,480** here, bounding the codebase-map
  dossier sub-population separately. Retiring the row line bound would otherwise leave a dossier bounded
  only at 61,440, which across the measured class is 820 to 1,200 lines, and check 6 is the only size gate
  a dossier has. Both keys follow S2's resolution rules and S3's shipped default.
- **S2** — BOTH keys resolved in `tools/memory-tree/check-memory-hygiene.sh` through the same three
  branches, in one helper rather than two copies. The engine pre-sets defaults and THEN sources the conf,
  so a blank line overrides a default with blank; each key therefore needs an explicit re-normalisation
  AFTER the source. Absent resolves to the shipped default. Blank resolves to the shipped default, not to
  "off". A non-numeric value refuses before the scan with `exit 2`, naming which key, matching the
  conf-validation precedent at `:101`.
- **S3** — The shipped default for BOTH keys stays **20,480**. An adopter who declares neither gets
  byte-for-byte today's byte verdicts, which keeps this unit out of
  `memory/gotchas/pin-copied-from-another-corpus.md`: this corpus's measured numbers are DECLARED here,
  never shipped as anyone else's defaults. The line bound is retired for everyone, which is the one part
  of this unit an adopter cannot opt out of, and the kit README says so.
- **S4** — The per-class cap block, now at `tools/memory-tree/check-memory-hygiene.sh:391-405`. **The
  reground changed this item substantially, in the unit's favour**: the tree already carries THREE classes
  and already carries the exact mechanism rev-5 was designing. `:396` initialises `cb = 20480; cl = 250`,
  `:397` gives guides `61440`/`750`, and `:401` gives a build README `cb = 25600; cl = 0` — where **`cl = 0`
  already means NO line cap**, the comparison at `:402` is already the guarded
  `b>cb || (cl>0 && l>cl)`, and `:403-404` already splits the message per class. So this unit FOLLOWS an
  established convention instead of inventing a sentinel, a guard and a message split.

  What it adds: a fourth class for dossiers taking `DOSSIER_CAP_BYTES` with `cl = 0`, and the row default
  at `:396` becoming `cb = <resolved ROW_DOC_CAP_BYTES>; cl = 0`. Branch order stays most-specific-last as
  the block already reads, because the guide, build-README and dossier selectors are disjoint.

  The dossier branch keys on the engine's existing `MAP_SUB`, the same variable check 7's `ex7` uses, and
  like `ex7` at `:419` it is written UNDER AN EMPTINESS GUARD. That is not ceremony: an unguarded
  `index(f, M "/" MAP_SUB) == 1` degenerates to `memory/` when `MAP_SUB` is empty and prefix-matches EVERY
  row document, silently capping the whole class at the dossier bound. The cited precedent guards for this
  reason and is not licence to skip one.

  The engine's own justification comment at `:384-390` states the refusal this unit reverses, in the words
  `memory/DECISIONS.md:41` ratified — and it is ALREADY stale, because it says "the two classes" while the
  code beneath it has three. It is rewritten here.
- **S5** — The finding message needs NO new work after the reground: `:403-404` already prints both
  figures when `cl>0` and `"%dB > %dB; no line cap for this class"` when it is 0. Setting the row and
  dossier classes to `cl = 0` gets the correct message for free. AC4 still grades the guide side, because
  the remaining slip is editing that shared branch rather than the class assignments.
- **S6** — `KIT_MEMORY_TREE_VERSION` bumped off `2.19`. The diff moves non-comment lines of the engine,
  so `check-verdict-epoch.sh` requires it and `hygiene-parity.test.sh` derives its floor from it.
- **S7** — A BYTE-axis arm for check 6's row class, plus a green control under the declared cap. This is
  the unit's coverage gain: every existing check-6 fixture is a line-axis construction, so the byte bound
  that fires in production has never been armed. The reground widened this: main's own build-README class
  at `cb = 25600; cl = 0` has NO check-6 arm either — `tRunOk/README.md` and `tRunBig/README.md` exist as
  front-matter stubs and nothing sizes one past 25,600 — so a class whose ONLY bound is bytes is entirely
  unarmed. This unit arms the row and dossier classes it touches and files the build-README gap as a
  backlog row rather than widening scope.
- **S8** — The retirement arm, pinned **above 750 lines** and under the declared byte cap. The reground
  changed which slip this guards: with `cl = 0` and the guarded comparison already in the tree, forgetting
  to zero the row initialiser leaves `250` in force, which is LOUD — every row document over 250 lines
  reds at once. What the above-750 pin still catches is the guide class's `750` leaking into the row class,
  which a 251-750 fixture cannot see. The 750 reason is stated in the arm so the number is not quietly
  lowered later.
- **S9** — `memory/builds/tRunBig/RUN.md` preserved as a row-class `chit 6` by growing it past the byte
  cap. It is 265 lines and about 3 KB, so lines are its only over-cap axis today; retiring the row line
  bound silences check 6 on it and vacates two other contracts that are asserted THROUGH it — the only
  proof `RUN.md` enters `index_set` at all, and the check-7 exemption precondition asserted on the same
  file check 6 named. Losing those is `fixture-passes-by-finding-nothing`.

  The fixture carries a THIRD contract the regrow must not break: it is also the per-class scoping
  control proving the guide widening did not leak into the row class. That control is line-axis and dies
  with the bound, so its byte-axis replacement needs a BAND, not just a floor — the fixture is grown past
  the ROW byte cap in a tree that declares that cap, and stays under the guide class's 61,440, so it
  still discriminates.
- **S9b** — A dossier arm pair: a fixture dossier over `DOSSIER_CAP_BYTES` is NAMED, and one BETWEEN
  `DOSSIER_CAP_BYTES` and `ROW_DOC_CAP_BYTES` is ALSO named — the second is the load-bearing one, because
  it is the only thing that distinguishes a dossier class from a row class under a larger bound.

  **The precondition is two conf files, not one, and stating only the first is how this arm goes
  vacuous.** The fixture tree needs a `.codebase-map.conf` so `MAP_SUB` resolves, AND its
  `.memory-tree.conf` must DECLARE THE TWO KEYS APART — `ROW_DOC_CAP_BYTES=61440` and
  `DOSSIER_CAP_BYTES=20480`. S3 keeps both SHIPPED defaults at 20,480, so a fixture declaring neither
  makes the two bounds one number, the between-bounds interval empty, and the arm satisfiable by an
  implementation carrying no dossier branch at all. Do NOT open the band by raising a shipped default;
  the band belongs in the fixture conf and nowhere else. That one conf also makes S9's band and AC5c
  constructible, so it is written once and cited from all three.
- **S10** — The guide arms untouched: `memory/guides/tfixture.md` past 750 lines stays NAMED and
  `memory/guides/twide.md` at 401 lines stays SILENT. Those two are the only proof the classes are still
  separate, and `twide.md` is a deliberate silent control that must not be rebuilt on the byte axis.
- **S11** — An arm asserting `tools/memory-tree/.memory-tree.conf.example` declares BOTH keys. Nothing
  else reads that file: `adopt-memory-tree.sh:40` only copies it and `tools/check-install-prefix.sh:17`
  excludes `*.conf.example`.
- **S12** — Both keys added to that example **with the shipped default's value**, in its policy-ceiling
  idiom rather than blank. Blank there means "check off" for every measured pin, while both policy
  ceilings ship with a value and say why. These keys are the same kind.
- **S13** — `FLOOR_ASSERTIONS` in the hygiene self-test raised to the new executed count, so the arms S7
  to S11 add cannot later go dark without a diff.
- **S14** — The prose carriers, enumerated by line, and the prescribed shape is THREE classes. Guides
  carry both bounds; codebase-map dossiers carry `DOSSIER_CAP_BYTES` and no line bound; every other row
  document carries `ROW_DOC_CAP_BYTES` and no line bound. The shipped template says "a declared byte
  bound" rather than spelling gov's 61,440 into an adopter's rule-set.

  Two of the carriers state the CLASS STRUCTURE rather than a figure, which is why a figure-shaped grep
  cannot reach them and they must be named. `memory/HYGIENE.md:127` opens rule 6 with "TWO classes" — and
  the reground proved that is ALREADY WRONG, before this unit touches anything, because main added the
  build-README class to the engine without moving the prose. Correcting it to name FOUR classes is
  therefore a repair as well as a description. `:312` gives ONE cap to all three map documents while under
  S4 `features/*.md` take the dossier bound and `map/README.md` and `FOUNDATION.md` take the row bound — so
  that sentence splits and the SPLIT remedy re-attaches to the dossier bound. The figure carriers are
  `memory/HYGIENE.md:66`, `:128` and `:132`. Every one has a mirror in
  `tools/memory-tree/HYGIENE.template.md`, which is what an adopter receives; the two agree modulo the
  `{{KIT_DIR}}` substitution the parity gate performs, and must keep agreeing.

  `.gitattributes:26` is a present-tense cap claim and is swept. `:30` is a DATED MEASUREMENT and stays
  exactly as it is — rewriting it would falsify the evidence the `eol=lf` pin rests on.
- **S15** — Rule 6's spill clause corrected in both HYGIENE carriers. It says check 6's cap is what
  `builds/*/RUN.md` spills against; the protocol budgets the authored region at 8 KB and spills against
  THAT, with check 6 as the backstop. Raising the byte cap and dropping the line bound widens the gap and
  makes the sentence more wrong.
- **S16** — THREE carriers of one mis-citation, not two: `memory/guides/BUILD-METHOD.md` line 8, its kit
  template, and `tools/memory-tree/README.md:138`. Each cites hygiene rule 6 for a budget rule 6 does not
  impose on a guide, and the third belongs here rather than in S14 because its defect is the citation and
  not the figure. The corrected line names the budget as self-imposed.
- **S17** — `TOOL-cSettledDocket-16` closed against this unit. It is this unit's problem statement,
  already filed and OPEN.
- **S18** — A `memory/map/features/` dossier for the hygiene engine, with `memory-tree` deleted from
  `memory/map/baseline.toml:53` in the same commit.
- **S19** — The kit marker in `tools/memory-tree/SPEC-TEMPLATE.template.md` and `memory/TEMPLATE-SPEC.md`
  moved with S6, and `memory/guides/SESSION-KICKOFF.md` re-stamped, because three files in its `watch:`
  list move.

## 3. Non-goals (OUT)

- **A per-class LINE bound.** The owner considered retiring the row line bound while giving dossiers and
  run-state files their own line value, and chose outright retirement instead. No class below `guides/`
  carries a line bound after this unit. The dossier key added by F3 is a BYTE bound, which is a different
  thing and is what the owner ratified.
- **A byte bound for the run-state sub-population.** F3 resolved to a dossier key only. Run-state files
  take the row-class value, because the protocol's own 8 KB authored budget is their real bound and check
  6 is only the backstop. If that reasoning ever fails, it is a new fork and not a silent third key.
- **The re-shape.** Sharding a backlog below `FAMILY`, or a spill tier like the run-state file's, is the
  second unit the owner sequenced after this one. Its id is minted when its spec is authored.
- **Byte normalisation before measuring.** `TOOL-aRootedPrefix-3` is open against checks 6 and 7 for
  measuring raw working-tree bytes, which makes the cap platform-dependent for an adopter without the
  `eol=lf` pin. It is a separate mechanism.
- **Check 10's blindness to shard rotations.** `TOOL-cTracedPromise-6` is open and untouched.
- **The guide class.** `TOOL-aWidenedGuide-1` set `61440` and `750` for guides and nothing here changes
  them. That the row byte cap now equals the guide byte cap is arithmetic, not a merge of the classes.
- **`READ_PATH_CEILING`, the 300-char entry budget, and rotation's carry-forward rule.** All three stay
  exactly as they are. The `20480` at `.memory-tree.conf:57` and `tools/memory-tree/corpus_ids.py:461`
  belongs to `READ_PATH_CEILING`'s headroom and is not this unit's number.

**What this unit deliberately gives up, stated as a non-goal so it cannot be read as an oversight.** The
row-class curation discipline `TOOL-aWidenedGuide-1` protected is being RELAXED, knowingly. That decision
ratified a class split and refused to triple the row allowance in the words the engine still carries at
`:376-378`. This unit triples it for the backlog shards and the decision log, and removes the line bound
from every class below `guides/`. The owner ratified that on 2026-08-17, asked a second time, with the
22-of-29 population measurement and the dossier loosening in front of them, and then answered F3 by
giving dossiers their own declared byte bound — which holds that loosening to 1.10x-1.60x instead of the
3.29x-4.80x a single row-class key would have given. §4 prices both, per member rather than as a mean.

## 4. Design

### Data model

Two conf keys, each holding a byte count: `ROW_DOC_CAP_BYTES` declared 61,440 here, and
`DOSSIER_CAP_BYTES` declared 20,480. Each resolves through three branches and one non-obvious step: the
engine pre-sets its defaults and then sources the conf at `:27`, so a blank conf line overrides a pre-set
default with blank. Every existing key in that block documents blank as skip, which is the opposite of
what these keys need, so the design re-normalises AFTER the source. A non-numeric value refuses with
`exit 2` before the scan, naming which key.

Neither key has a value that disables its bound, and the shipped default for both stays 20,480 so nothing
an adopter receives changes on the byte axis until they declare their own.

`DOSSIER_CAP_BYTES` at 20,480 is not the same as changing nothing for dossiers, and the loosening is
UNEVEN across the class rather than a single percentage. Their operative bound today is the LINE count at
each one's own density, which over the 12 measured dossiers lands between **12,805 and 18,671 bytes** —
half the class sits below 14.5 KB. A 20,480-byte bound with no line count therefore buys the DENSEST of
them (74.7 bytes per line) only 274 lines, about +10%, and the SPARSEST (51.2) a full 400 lines, about
+60%. In bytes that is 1.10x to 1.60x.

Under a single row-class key at 61,440 the same class would have run **3.29x to 4.80x**, or roughly 820
to 1,200 lines. That difference is what the key buys. Stating one mean figure for the class was rev-5's
error: the mean is attached to no member, and the member the price should be quoted against is the
sparsest, because that is where the bound is loosest.

### Inventory

Check 6's row class is `INDEX_SET` minus `memory/guides/`: **29 files** at base, against 4 guides. The
population is `tools/memory-tree/check-memory-hygiene.sh:337-359` and the only class override is
`index(f, gp) == 1` at `:385`.

| path | bytes | lines | share of 20,480 | share of 250 lines |
|---|---|---|---|---|
| `memory/backlog/TOOL.md` | 19,152 | 78 | 93.5% | 31.2% |
| `memory/map/features/memory-tree-merge-driver.md` | 14,713 | 197 | 71.8% | 78.8% |
| `memory/builds/cBriefedPilot/RUN.md` | 13,806 | 151 | 67.4% | 60.4% |
| `memory/DECISIONS.md` | 12,328 | 69 | 60.2% | 27.6% |
| `memory/map/features/unattended.md` | 11,751 | 171 | 57.4% | 68.4% |
| `memory/map/features/lexicon.md` | 11,403 | 190 | 55.7% | 76.0% |
| `memory/builds/aSealedCaravan/RUN.md` | 8,141 | 114 | 39.8% | 45.6% |

| sub-population | members | max bytes | max lines |
|---|---|---|---|
| `memory/map/features/*.md` dossiers | 12 | 14,713 | 197 |
| `memory/builds/*/RUN.md` | 5 | 13,806 | 151 |
| `memory/backlog/*.md` | 4 | 19,152 | 78 |
| the decision log | 1 | 12,328 | 69 |
| generated indices and ledgers | 3 | 3,240 | 40 |
| other row documents | 4 | 2,695 | 35 |

**Which bound binds first today: 22 of 29 are LINE-bound.** The break-even is 20,480/250 = 81.92 bytes
per line. All 12 dossiers sit below it, as do 4 of the 5 run-state files, both ledger shards,
`memory/README.md`, `memory/map/README.md`, `memory/map/FOUNDATION.md` and
`memory/builds/aPrunedCeremony/STATUS.md`. Only 7 are byte-bound: the four backlog shards, the decision
log, `memory/LIVE.md` and `memory/builds/cBriefedPilot/RUN.md`.

Three measurements decide the declared value:

- **Row length.** `wc -c` over the dash rows of `memory/backlog/TOOL.md` is 18,519 bytes across 73 rows,
  so 253.7 bytes per row. This is a BYTE count, which is what check 6 measures; a character count reads
  18,314, because the `·` separators are two bytes each.
- **Minting rate.** 156 of the 161 distinct `TOOL-` ids across the live shard and its three archives
  first appear inside the nine-day window: 17.3 ids per day.
- **Live-set growth.** Those nine days left 73 non-terminal rows standing: 8.1 rows per day, about
  2,057 bytes.

61,440 is 250 rows at the measured 253.7 bytes, which is 63,425, rounded down to 60 KiB. Runway from
today's 19,152 at 2,057 bytes per day is about 21 days.

### Why rotation cannot be the answer here

Rotation moves terminal rows only and carries forward everything else. `memory/backlog/TOOL.md` has 66
OPEN, 6 SPECCED, 1 DEFERRED and zero terminal rows, so a fourth rotation leaves the whole 19,152-byte
file where it is — the floor is 93.5% of the cap, because the 633-byte head with its two rotation
announcements stays too. It has rotated three times in four days, twice on one of them; the third
announcement lands in the tree the Rollout section reground targets, not at this base.
`TOOL-cSettledDocket-16` is OPEN in that shard and says the same thing.

`memory/builds/cSteadyMetronome/README.md` also recorded that rotation orphans ids against check 14,
which is why a rotation was once attempted and reverted. That claim looks stale and this spec does not
rely on it: `corpus_ids.py`'s one walk is `git ls-files` with no `archive/` exclusion, and three
rotations have since landed green. F4 turns the reading into a fixture.

### What retiring the row line bound costs

rev-1 argued the line bound "cannot fire". That was measured on one document and is false: it is the
bound that binds FIRST on 22 of 29 row documents. The retirement therefore removes a bound that is doing
work, and the price is concentrated in one sub-population.

**Dossiers — the sub-population F3 carved out.** A dossier's effective ceiling today is its line count at
its own density, and the class spans a wide range: 250 x 74.7 is 18,671 B for
`memory-tree-merge-driver.md` at the dense end, down to 250 x 51.2 = 12,805 B for `codebase-map.md` at the
sparse end, with `install-prefix.md` and `testsuite-counts.md` beside it near 12.9 KB. Under a single
row-class key at 61,440 the class would have run **3.29x to 4.80x** looser, roughly 820 to 1,200 lines.
`DOSSIER_CAP_BYTES` at 20,480 holds it to **1.10x at the densest (274 lines) and 1.60x at the sparsest
(400 lines)** instead. That matters because dossiers are row class by construction,
`tools/codebase-map/test_codebase_map.py` carries no size or line predicate of its own, and
`memory/HYGIENE.md:276-278` gives their remedy as a SPLIT rather than a rotation — so check 6 is the only
thing bounding a dossier at all, and its split trigger moves with whichever bound applies.

**Run-state files.** Four of five are line-bound today and become byte-bound at 61,440. Behaviour does
not change, because the protocol budgets the authored region at 8 KB and spills against that; check 6 is
the backstop whose purpose is never to be reached. But the fixture that PROVES `RUN.md` is in the
population is line-only, which is why S9 grows it rather than leaving it silent.

**The other line-bound members** — both ledgers, two READMEs, a STATUS file and `FOUNDATION.md`, six in
all — sit between 3.6% and 15.8% of the byte cap at base. The retirement gives them room they were not
asking for and costs nothing observable.

### The three consumers whose behaviour shifts

- **`builds/*/RUN.md`** — no trigger moves; the backstop loosens. The protocol names no byte figure, so
  it needs no edit. Rule 6's clause contradicting it does, and S15 is that edit.
- **Codebase-map dossiers** — priced above. With `DOSSIER_CAP_BYTES` the split trigger moves from an
  effective ~14.5 KB to a declared 20,480, not to 61,440. In a tree with no codebase map the branch is
  inert because `MAP_SUB` is empty, and the key is then declared-and-unreached rather than wrong.
- **The generated indices** — `memory/LIVE.md` and the ledger shards are rendered; a larger byte cap
  defers the month a ledger shard would rotate.

### Rollout

**This unit's own records cannot be written until its conf change lands, and that ordering is forced by
the defect.** The §4 figures above are measured at the ORIGINAL base `43eb6b10` and stay there — a base is
immutable and the measurements belong to it. The reground has since HAPPENED: this branch merged the local
default's 37 commits and the spec's base moved to `52f9bbb0`, which is what the header now carries. At
that tip `memory/backlog/TOOL.md` is **20,345 of 20,480 bytes — 99.34%, with 135 bytes left**, holding 80
rows of which none is terminal. At 253.7 bytes per row, 135 bytes is half a row: **the next backlog row
that tree receives reds check 6**, and rotation cannot make room.

So the landing order is: the conf change and its declared value first, then this build's decision rows
and backlog rows. Writing the records first is red, not merely untidy. This is the bind
`memory/builds/cSteadyMetronome/README.md` described on 2026-08-14 arriving a second time, and it is why
S17 closes `TOOL-cSettledDocket-16` in place rather than filing a fresh row beside it.

The reground onto the local default was the first build pass, and it earned itself. It found that main
had already built the `cl = 0` sentinel, the guarded comparison and the per-class message this unit was
designing (S4, S5), that main's own build-README class shipped with no byte-axis arm (S7), that rule 6's
prose already understates the class count (S14), and that `KIT_MEMORY_TREE_VERSION` had moved to `2.19`
(S6). Building on the original base would have produced a diff against a file that no longer exists: main
touched every one of this unit's targets, the engine by 108 lines.

### Files touched (estimate)

| path | change | forced by |
|---|---|---|
| `.memory-tree.conf` | both keys — 61,440 and 20,480 — with derivations and movement | S1 S1b |
| `tools/memory-tree/.memory-tree.conf.example` | both keys at the shipped default | S12 |
| `tools/memory-tree/check-memory-hygiene.sh` | two conf reads and re-normalisation · the three-class cap block · the message · kit version | S2 S4 S5 S6 |
| `tools/memory-tree/check-memory-hygiene.test.sh` | byte-axis arms · the above-750 retirement arm · tRunBig grown · the dossier arm pair · the example-conf arm · `FLOOR_ASSERTIONS` | S7 S8 S9 S9b S11 S13 |
| `memory/HYGIENE.md` | the four carriers · rule 6's spill clause | S14 S15 |
| `tools/memory-tree/HYGIENE.template.md` | the same, in lockstep | S14 S15 |
| `tools/memory-tree/README.md` | the figures | S14 |
| `.gitattributes` | the two present-tense cap claims at `:26` and `:30` | S14 |
| `memory/guides/BUILD-METHOD.md` · `tools/memory-tree/BUILD-METHOD.template.md` | the budget line and its mis-citation | S16 |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` · `memory/TEMPLATE-SPEC.md` | the kit marker, paired by `kit-dogfood-parity.test.sh:53` | S19 |
| `memory/guides/SESSION-KICKOFF.md` | the manifest re-stamp; three watched files move | S19 |
| `memory/map/features/` · `memory/map/baseline.toml` | the dossier, and the baseline line it claims | S18 |
| `memory/DECISIONS.md` · `memory/backlog/TOOL.md` | the decision rows, and closing `TOOL-cSettledDocket-16` | S17 |

### Alternatives rejected

- **Raise the constant and leave it hardcoded.** Ships this corpus's number to every adopter with no
  knob — `pin-copied-from-another-corpus`, which is also why S3 keeps the shipped default at 20,480.
- **Keep the row line bound and move only the byte bound.** rev-2's shape and the smaller diff. Rejected
  by the owner on 2026-08-17 in favour of outright retirement.
- **Retire the line bound but give dossiers and run-state files their own line value.** Also rejected by
  the owner in the same turn. F3 asks the narrower remaining question about a BYTE sub-bound.
- **One byte cap for the whole index set.** Dissolves the class split by arithmetic rather than by
  decision; re-plumbing the guide class is a larger diff than leaving it alone.
- **Do nothing and rotate harder.** Measured impossible: zero terminal rows remain.

## 5. Production-readiness checklist

- **security** — N/A. No new input, no write path, no surface.
- **perf / scale** — Neutral. The awk block already computes both counts per file; one comparison is
  dropped for the row class and no new pass over the corpus is added.
- **a11y** — N/A. A shell gate with no user interface.
- **i18n** — N/A, with one live caveat the engine carries: check 7 sets no `LC_ALL` because
  character-versus-byte counting is a property of the adopter's awk. This unit adds no locale-sensitive
  comparison, and rev-1's own row-length figure was wrong by exactly that confusion.
- **error / empty / loading states** — Three branches, all in S2: absent and blank resolve to the shipped
  default after an explicit post-source re-normalisation, and a non-numeric value refuses with `exit 2`.
- **observability** — The finding message is the whole interface. Per S5 it prints the cap it applied.
- **risks** — Four, and rev-1 named the wrong one as silent. First, a blank or zero byte cap is the
  LOUDEST failure available: measured on this repo's awk, `19152 > ""`, `19152 > 0` and an uninitialised
  right-hand side all evaluate true, so the whole class reds at once. Second, the genuinely silent
  direction is a bound that cannot fire — which is what this unit deliberately creates for the row line
  axis, and why S8 pins its arm above the guide's 750 rather than inside the band where a slip is
  invisible. Third, the shared `cb`/`cl` pair now carries THREE classes in S4: deleting the row `cl`
  assignment leaves the guide's 750 governing rows, and mis-ordering the branches leaves a dossier taking
  the row-class value. Both look like a successful retirement. Fourth, the dossier branch is inert when
  `MAP_SUB` is empty, which is correct in a tree with no codebase map and is `vacuous-selector-empty-population`
  in a fixture that forgot the conf — S9b requires one. Rollback is reverting one commit; nothing migrates.
- **testing + left-shift gates** — S7 to S11 and S13. The byte axis of check 6 gains its first arm in the
  kit's life; S9 keeps the one row-class arm that three other contracts hang on.
- **migration / rollback** — None required. An adopter who never declares the key keeps today's verdicts
  exactly, because S3 keeps the shipped default at the present value.
- **user docs** — The kit README and both HYGIENE carriers, per S14. No end-user surface.

No open scope item. F3 resolved to a second declared key on 2026-08-17 and is built by S1b and S4.

## 6. Acceptance criteria

- **AC1a** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over a scratch tree whose conf
  declares no `ROW_DOC_CAP_BYTES`, the row class is capped at the shipped default.
- **AC1b** — When that conf declares `ROW_DOC_CAP_BYTES=` blank, the row class is capped at the shipped
  default and not left unbounded, which is the branch the engine's pre-set-then-source idiom gets wrong.
- **AC1c** — When that conf declares a non-numeric value, `check-memory-hygiene.sh` refuses with
  `exit 2` before scanning, naming the key and the value.
- **AC2** — When a row document exceeds the declared byte cap, `check-memory-hygiene.sh` names it and the
  finding reports the measured bytes and the cap it applied, with no line figure for the row class.
- **AC3** — When a row document carries **more than 750 lines** and stays under the declared byte cap,
  `check-memory-hygiene.sh` is SILENT about it. Above 750 rather than above 250 deliberately: a fixture
  in the 251-750 band is equally silent if the implementation leaves the guide class's `cl` governing
  rows, so it cannot tell a retirement from that slip.
- **AC4** — When the guide fixtures run, `memory/guides/tfixture.md` past 750 lines is still NAMED, its
  finding still reports BOTH bounds, and `memory/guides/twide.md` at 401 lines is still SILENT — proving
  the classes are separate, that the silent control was not rebuilt on the byte axis, and that S5's
  per-class message did not drop the line figure from the one class that still enforces it.
- **AC5** — When the suite runs, `memory/builds/tRunBig/RUN.md` is still NAMED by check 6, now on the
  byte axis, so the `index_set` membership proof and the check-7 exemption precondition asserted on that
  same file both still hold.
- **AC5b** — In a fixture tree that carries a `.codebase-map.conf` AND declares the two keys apart
  (`ROW_DOC_CAP_BYTES=61440`, `DOSSIER_CAP_BYTES=20480`), three observations hold together: a dossier over
  20,480 is NAMED; a dossier sized BETWEEN the two bounds is ALSO named; and a ROW document sized in that
  same band is SILENT. The second and third are the pair that proves a dossier class exists rather than a
  row class under a larger bound — either alone is satisfied by an implementation with no dossier branch.
  With the keys undeclared the band is empty, so the declaration is part of the criterion, not setup.
- **AC5c** — In a fixture tree with NO codebase map that DECLARES `ROW_DOC_CAP_BYTES` above
  `DOSSIER_CAP_BYTES` and carries a row document sized between them, `check-memory-hygiene.sh` is SILENT
  about that document. This is the discriminating form: asserting mere silence proves nothing, because
  without a `.codebase-map.conf` no dossier-shaped path enters check 6's population at all and silence is
  guaranteed one layer above the branch under test. What this arm catches is the degenerate selector — an
  unguarded `index(f, M "/" MAP_SUB)` resolving to `memory/` and capping every row document at the dossier
  bound, which would red this document and does red under no other arm.
- **AC6** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, its new check-6 row arms
  fail on the BYTE axis and `FLOOR_ASSERTIONS` has been raised to the new executed count.
- **AC7** — When `bash tools/memory-tree/check-verdict-epoch.sh` runs over this diff it is green, and
  `KIT_MEMORY_TREE_VERSION` no longer reads `2.18`.
- **AC8** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs it is green, which is the gate
  that pairs `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` with
  their templates — so it is also what observes S16's corrected budget line in both carriers.
- **AC9** — Per carrier rather than once for the list: each S14 line named above no longer states its own
  retired figure, AND `memory/HYGIENE.md:127` with its mirror names THREE classes and both key names,
  which a figure-shaped grep cannot observe and which a two-class sentence would satisfy. `git grep -nE
  '20 ?KB|20,?480|250 lines'` is the figure half only. Expected survivors, each for a stated reason:
  `memory/DECISIONS.md:41` (the ratified `TOOL-aWidenedGuide-1` row, in an append-only log),
  `.memory-tree.conf:57` and `tools/memory-tree/corpus_ids.py:461` (`READ_PATH_CEILING`'s headroom, out
  of scope), the engine's own shipped default at 20,480 per S3, the guide class's own `750`,
  `.gitattributes:30` (a dated measurement that must NOT be rewritten), and the test fixtures. The
  criterion is scoped to a path list because a tree-wide zero-survivor sweep is unsatisfiable.
- **AC9b** — When the hygiene self-test runs, its example-conf arm asserts
  `tools/memory-tree/.memory-tree.conf.example` declares BOTH keys with the shipped default's value. No
  other leg reads that file, so without this criterion the one artifact an adopter actually receives can
  be forgotten silently.
- **AC10** — When `bash tools/check-testsuite-counts.sh` and `python tools/memory-tree/check-arms.py`
  run, both are green, with the hygiene gate's `ARMS_FLOORS` pair unchanged at `14:14` because no `fail`
  branch is added or removed.
- **AC11** — When `python tools/codebase-map/test_codebase_map.py` runs, the hygiene engine is claimed by
  a dossier under `memory/map/features/`, `memory-tree` is gone from `memory/map/baseline.toml`, and the
  generated artifacts byte-compare against a fresh render.
- **AC12** — When `bash skills/session-kickoff/manifest-check.sh` runs it exits 0, because three files in
  its `watch:` list moved and the manifest was re-stamped in the same change.
- **AC13** — When `GATE_FULL=1 bash tools/run-gates.sh` runs at the push boundary it is green,
  `memory/backlog/TOOL.md` sits under 61,440, and `TOOL-cSettledDocket-16` reads CLOSED against this unit.

## 7. Gates

The legs this unit must keep green, from `tools/gate-legs.json`: `memory/` hygiene · the hygiene
self-test · the harness meta-gate `check-arms.py` against the `ARMS_FLOORS` pair
`tools/memory-tree/check-memory-hygiene.sh:14:14` · verdict epoch and its self-test · kit version
markers · kit/dogfood doc parity · method carriers · testsuite counts · codebase-map coverage and
freshness · the kickoff-manifest ratchet, because `.memory-tree.conf`,
`tools/memory-tree/check-memory-hygiene.sh` and `memory/guides/BUILD-METHOD.md` are all in its `watch:`
list · drift-audit records. It adds no new leg.

One leg is RED at the spec's base for a reason outside this diff, and the build must not read it as its
own: `drift-audit records` reports `ORPHAN_ID_PIN moved 0 -> 5`, because the local default drained that
pin in `7f2b7b0` while this branch sits on `origin/main`, which still carries 5. It clears on the
reground the Rollout section schedules.

Bug classes the checklist selects: `fixture-passes-by-finding-nothing` (S8, S9, S9b, S10 and S11 exist
for it, and round 2 found it twice more inside those very arms) ·
`two-answers-to-one-question` · `vacuous-selector-empty-population` · `pin-copied-from-another-corpus`
(S3 exists for it) · `gate-green-by-accident-on-generated-bytes`.

## 8. Open questions

### F1 — the declared value · RESOLVED (owner, 2026-08-17): 61,440

Three candidates were priced from today's 19,152 bytes at 2,057 bytes per day: 61,440 for about 21 days,
derived as 250 rows at the measured 253.7 bytes; 39,632 for about 10 days, from the flat 20,480 headroom
`READ_PATH_CEILING` uses; and 184,500 for about 80 days, a quarter of measured net growth, listed to be
rejected because a 180 KB backlog shard is not scannable. The owner ratified 61,440.

### F5 — the row line bound · RESOLVED (owner, 2026-08-17): retire it outright

Asked twice. rev-1 recommended retirement on a premise the M4 audit falsified, so the fork was re-opened
with the measured population — 22 of 29 row documents line-bound first, all 12 dossiers among them, and a
3.3x-to-4.3x dossier loosening that `TOOL-aWidenedGuide-1` had refused. The owner was shown that
measurement and both alternatives, and chose outright retirement. Recorded here as a deliberate
relaxation of a ratified curation discipline, not as an inherited assumption.

### F3 — the dossier bound · RESOLVED (owner, 2026-08-17): its own conf key

F3 originally asked whether the row class needs a per-document-kind matrix, and rev-3 recommended no on
the grounds that a dossier's operative bound was the line count this unit would not touch. F5's answer
removed that ground: after retirement a dossier would be bounded only at 61,440 bytes, roughly 1,050 lines
at measured density, with check 6 the only size gate it has and a split as its declared remedy.

Three options were put to the owner — one key for the whole row class, one extra branch pinning dossiers
at the shipped 20,480 with no new key, or a second declared key. The owner chose the **second declared
key**, which is `DOSSIER_CAP_BYTES` in S1b. It costs one more number to measure and comment, and it buys
an adopter the ability to set a dossier bound different from the one gov measured — the same argument that
made the row cap a key rather than a constant.

### F2 — absent-and-blank semantics · RESOLVED (agent, 2026-08-18, standing recommendation, built and armed)

Absent and blank both resolve to the shipped default; no value disables the bound. Put to the owner in
the 2026-08-17 hand-back with F1 and F5 and not overruled, so S2 builds it. This is the policy-ceiling
idiom rather than the measured-pin idiom, and it needs the explicit re-normalisation S2 specifies.

### F4 — the stale rotation claim · RESOLVED (agent, 2026-08-18, built by TOOL-aRelaxedShard-4 S2)

Settled, and NOT in this unit — `TOOL-aRelaxedShard-4` S2 built it, because that unit could not evaluate
a spill tier without the answer. The recorded claim is FALSE as stated and true on a different axis.
Rotating between two TRACKED paths cannot orphan an id: check 14 is `cites` minus `defs`, a backlog row
defines and cites its own id on one line, and 83 ids in this corpus are defined only under `archive/` with
zero orphans. What DOES orphan them is corpus MEMBERSHIP — an archive present on disk but not staged —
which is the state `cSteadyMetronome` actually saw. Both directions are armed and red-proved in
`tools/memory-tree/check-memory-hygiene.test.sh`.

## 9. Revision log

- rev-1 · 2026-08-17 · initial draft. Authored this run, so unreviewed by definition.
- rev-2 · 2026-08-17 · folded the M4 spec audit at
  `reviews/2026-08-17-review-TOOL-aRelaxedShard-1.md` — verdict BLOCKED, 21 distinct defects. The
  blocker rescoped the unit: retiring the row line bound left for fork F5, because the bound binds first
  on 22 of 29 row documents and rev-1 had measured one. §4's Inventory gained the whole 29-member class
  with a lines axis. Corrected: row length 253.7 B by `wc -c` not 251 by character count, the rotation
  floor is the whole 19,152-byte file at 93.5%, minting 17.3 ids/day, F1's third candidate ~80 days. The
  shipped default was stated and pinned at 20,480, the blank and non-numeric branches gained scope items
  and criteria, the sweep became a runnable scoped `git grep` with expected survivors named, four
  gate-mandated files entered the files-touched table, and `TOOL-cSettledDocket-16` — already OPEN for
  this defect and missed by rev-1's recall probe — is closed by scope.
- rev-3 · 2026-08-17 · added §4 Rollout: the local default advanced 37 commits during the build and the
  shard is at 99.34% there with 135 bytes left, forcing the conf change to land before this build's own
  records.
- rev-4 · 2026-08-17 · folded the owner's F1 and F5 decisions. F5 was reaffirmed AFTER the correct
  measurement was put in front of the owner, so the line bound is retired outright and §3 now states the
  relaxation of `TOOL-aWidenedGuide-1`'s discipline as deliberate and ratified rather than as a premise.
  §4 gained "What retiring the row line bound costs", pricing the dossier shift (the figures were wrong at
  the class edges and rev-6 re-derives them). Three arms follow from the audit's folds: AC3 is pinned above 750 rather than 250 because
  the 251-750 band cannot distinguish retirement from the shared-`cl` slip, AC5 keeps `tRunBig` named on
  the byte axis so two contracts asserted through it survive, and AC4 protects the silent control. §5
  risks gained the shared-`cl` hazard and now names the cannot-fire direction as one the unit creates on
  purpose. F3 is RE-OPENED, because its rejection rested on the line bound staying.
- rev-5 · 2026-08-17 · folded the owner's F3 decision: dossiers get their own declared key,
  `DOSSIER_CAP_BYTES`, at 20,480. §4's cap block becomes THREE classes ordered most-specific first, keyed
  on the engine's existing `MAP_SUB`. That holds the dossier loosening well below what a single row-class key would
  have given, and §4 says so rather than claiming dossiers are unaffected. The figures rev-5 used were
  the class MEAN and rev-6 replaces them. Three arms added: AC5b names a dossier over its own bound
  AND one between the two bounds, which is the only observation distinguishing a dossier class from a row
  class under a larger bound; AC5c asserts the branch is inert with no map. §5 gained the mis-ordering
  hazard and the inert-branch vacuity. §3 gained two non-goals the answer creates: no line bound anywhere
  below `guides/`, and no third key for run-state files. §8 F3 is RESOLVED, so the header carries
  `ratified`.
- rev-6 · 2026-08-17 · folded M4 round 2 at
  `reviews/2026-08-17-review-TOOL-aRelaxedShard-1-round2.md` — verdict CLEAN WITH FIXES, 43 raw, 29 confirmed, 14
  refuted, precision 0.67, 3 of 3 lenses, 17 distinct defects and no blocker. Round 2 audited only what
  rev-4 and rev-5 changed, and found the same failure twice INSIDE the arms rev-5 added for it: AC5b's
  between-bounds dossier and AC5c's inert branch were both unfalsifiable, because S3 pins both SHIPPED
  defaults at 20,480 and no item asked the FIXTURE conf to declare them apart, so the band those arms sit
  in was empty. Both now require the fixture to declare `ROW_DOC_CAP_BYTES=61440` and
  `DOSSIER_CAP_BYTES=20480`, AC5b gained the third observation that makes the pair discriminate (a ROW
  document in the same band, SILENT), and AC5c was re-pinned onto the degenerate-selector case it can
  actually catch. S4 dropped its claim that `MAP_SUB` needs no emptiness guard — the `ex7` precedent it
  cited has one, and an unguarded selector resolves to `memory/` and caps the whole class.
  The dossier price was re-derived per member rather than as a class mean: effective ceilings run 12,805
  to 18,671 bytes, so 20,480 buys the densest +10% and the SPARSEST +60%, and a single row-class key would
  have run 3.29x to 4.80x. S14's prescribed wording was still rev-2's TWO-class sentence, which would have
  shipped an adopter a rule-set documenting two classes for a three-class gate; it now names the
  class-COUNT carriers a figure-grep cannot reach. Smaller: the third mis-citation carrier moved to S16,
  the engine's own justification comment entered S4, S9 gained the band its third contract needs, the
  message requirement became per-class, the sub-population table stopped reporting the decision log
  against a group that excludes it, and this log now ascends.
- rev-7 · 2026-08-17 · REGROUND onto the local default (M7), which was the first build pass, and folded
  what it found. Base moves to `52f9bbb0`; the §4 figures stay at `43eb6b10` where they were measured.
  main had already landed most of this unit's mechanism for a build-README class: `cl = 0` meaning no line
  cap, the guarded `b>cb || (cl>0 && l>cl)` comparison, and the per-class message split. S4 now EXTENDS
  three classes to four instead of inventing a sentinel; S5 needs no work at all; S8's hazard changed
  character, because forgetting to zero the row initialiser is now loud rather than silent. `S6` bumps off
  `2.19`, not `2.18`. Two fresh findings: main's build-README class at 25,600 has no byte-axis arm either,
  so S7 arms what it touches and files the rest as a row; and `memory/HYGIENE.md:127` already says "TWO
  classes" against an engine with three, so S14 is a repair and not only a description. Every line anchor
  the spec cites was re-derived — the cap block is `:391-405`, `ex7` is `:419`, the map additions are
  `:347-349`, rule 6 is `:127-136` and the dossier sentence is `:312`. Status moves to INPROGRESS.

- rev-8 · 2026-08-18 · F4 RESOLVED and the unit CLOSED. F4 was settled by `TOOL-aRelaxedShard-4` S2
  rather than here, and the answer inverted it: the recorded claim is false as stated — rotation between
  two tracked paths cannot orphan an id — and true on corpus MEMBERSHIP, an archive present but unstaged.
  Both arms are red-proved. F2 is marked resolved on the standing recommendation it was built and armed
  under, with the AGENT named as resolver rather than the owner, who did not itemise it.

## 10. Reuse audit

**The seam this unit extends** is the per-class cap block at
`tools/memory-tree/check-memory-hygiene.sh:379`, together with the conf-key convention of
`.memory-tree.conf` itself. rev-1 attributed that convention to the engine, which is wrong: the engine
mentions `READ_PATH_CEILING` only in a prose comment at `:375` and contains neither `UNIVERSAL_BUDGET`
nor `ROW_DUPLICATE_PIN`. The readers are `tools/memory-tree/corpus_ids.py:74`,
`tools/memory-tree/gotchas.py:84` and `tools/memory-tree/row_grammar.py:42`. The correction matters
because the engine's own keys are pre-set defaults followed by a source, so copying its idiom yields the
blank-disables-the-bound behaviour S2 forbids.

**`TOOL-aWidenedGuide-1` is REOPENED by this unit, not extended.** That decision split the cap by class
and explicitly refused to triple the row allowance. This unit triples it and retires the row line bound
as well. rev-1 and rev-2 framed the decision as a seam being extended; with F5 answered YES that framing
is false, and the record of the reopening is §3's closing paragraph plus the F5 mark above.

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
rotations landing green since it was written. F4 turns the reading into a fixture.
