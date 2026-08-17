# TOOL-aRelaxedShard-1 — the row class becomes one declared byte bound

**Status:** OPEN · rev-4 · 2026-08-17 · node a · Tier-2 · base 43eb6b10 · streams tooling

## 1. Goal

Hygiene check 6 caps every row document at a hardcoded 20,480 bytes and 250 lines, and on this repo the
byte bound is spent: the tooling backlog shard has no terminal rows left for rotation to archive. Make
the byte bound a declared per-repo value, set here to 61,440, and retire the row class's line bound so
that one declared number bounds the class. The retirement is a ratified owner decision to relax a
curation discipline, not a claim that the bound was inert — §4 prices what it costs.

## 2. Scope (IN)

- **S1** — A new `.memory-tree.conf` key, `ROW_DOC_CAP_BYTES`, declared **61,440** here. Its comment
  records the derivation and the movement, the way `READ_PATH_CEILING` records its four.
- **S2** — The key resolved in `tools/memory-tree/check-memory-hygiene.sh` with three branches. The
  engine pre-sets defaults and THEN sources the conf, so a blank line overrides a default with blank;
  this key therefore needs an explicit re-normalisation AFTER the source. Absent resolves to the shipped
  default. Blank resolves to the shipped default, not to "off". A non-numeric value refuses before the
  scan with `exit 2`, matching the conf-validation precedent at `:101`.
- **S3** — The shipped default stays **20,480**. An adopter who never declares the key gets byte-for-byte
  today's verdicts, which keeps this unit out of `memory/gotchas/pin-copied-from-another-corpus.md`: this
  corpus's measured number is DECLARED here, never shipped as anyone else's default.
- **S4** — The per-class cap block at `tools/memory-tree/check-memory-hygiene.sh:379`: the row class is
  bounded by the resolved byte value and by NO line count; the guide class keeps its own `61440` and
  `750`. The retirement must not leave the guide's `750` in play on the shared `cl` variable — deleting
  the row branch's assignment does exactly that, and so does a `cl > 0 && l > cl` guard whose `cl`
  defaults to the guide value. The two classes share the code path and must not share the bound.
- **S5** — The finding message reports bytes alone for a row document. A line figure the gate no longer
  enforces reads as a second bound, and the message must also print the cap it applied so a default is
  distinguishable from a declaration in the output alone.
- **S6** — `KIT_MEMORY_TREE_VERSION` bumped off `2.18`. The diff moves non-comment lines of the engine,
  so `check-verdict-epoch.sh` requires it and `hygiene-parity.test.sh` derives its floor from it.
- **S7** — A BYTE-axis arm for check 6's row class, plus a green control under the declared cap. This is
  the unit's coverage gain: all three existing check-6 fixtures are line-axis constructions, so the byte
  bound that fires in production has never been armed.
- **S8** — The retirement arm, pinned **above 750 lines** and under the declared byte cap. A fixture in
  the 251-750 band is silent under the intended retirement AND under the likeliest implementation slip
  in S4, so it cannot discriminate between them. The 750 reason is stated in the arm so the number is
  not quietly lowered later.
- **S9** — `memory/builds/tRunBig/RUN.md` preserved as a row-class `chit 6` by growing it past the byte
  cap. It is 265 lines and about 3 KB, so lines are its only over-cap axis today; retiring the row line
  bound silences check 6 on it and vacates two other contracts that are asserted THROUGH it — the only
  proof `RUN.md` enters `index_set` at all, and the check-7 exemption precondition asserted on the same
  file check 6 named. Losing those is `fixture-passes-by-finding-nothing`.
- **S10** — The guide arms untouched: `memory/guides/tfixture.md` past 750 lines stays NAMED and
  `memory/guides/twide.md` at 401 lines stays SILENT. Those two are the only proof the classes are still
  separate, and `twide.md` is a deliberate silent control that must not be rebuilt on the byte axis.
- **S11** — An arm asserting `tools/memory-tree/.memory-tree.conf.example` declares the key. Nothing else
  reads that file: `adopt-memory-tree.sh:40` only copies it and `tools/check-install-prefix.sh:17`
  excludes `*.conf.example`.
- **S12** — The key added to that example **with the shipped default's value**, in its policy-ceiling
  idiom rather than blank. Blank there means "check off" for every measured pin, while both policy
  ceilings ship with a value and say why. This key is the same kind.
- **S13** — `FLOOR_ASSERTIONS` in the hygiene self-test raised to the new executed count, so the arms S7
  to S11 add cannot later go dark without a diff.
- **S14** — The prose carriers, enumerated by line. Both figures move for the row class, so the sweep
  covers `memory/HYGIENE.md:66`, `:128`, `:132` and `:276`, the four mirrors at the same lines in
  `tools/memory-tree/HYGIENE.template.md`, `tools/memory-tree/README.md`, and `.gitattributes:26` and
  `:30`. Each must state the new shape: rows carry a declared byte bound and no line bound; guides carry
  both.
- **S15** — Rule 6's spill clause corrected in both HYGIENE carriers. It says check 6's cap is what
  `builds/*/RUN.md` spills against; the protocol budgets the authored region at 8 KB and spills against
  THAT, with check 6 as the backstop. Raising the byte cap and dropping the line bound widens the gap and
  makes the sentence more wrong.
- **S16** — `memory/guides/BUILD-METHOD.md` line 8 and its kit template. Both cite hygiene rule 6 for a
  budget rule 6 does not impose on a guide. The corrected line names the budget as self-imposed.
- **S17** — `TOOL-cSettledDocket-16` closed against this unit. It is this unit's problem statement,
  already filed and OPEN.
- **S18** — A `memory/map/features/` dossier for the hygiene engine, with `memory-tree` deleted from
  `memory/map/baseline.toml:53` in the same commit.
- **S19** — The kit marker in `tools/memory-tree/SPEC-TEMPLATE.template.md` and `memory/TEMPLATE-SPEC.md`
  moved with S6, and `memory/guides/SESSION-KICKOFF.md` re-stamped, because three files in its `watch:`
  list move.

## 3. Non-goals (OUT)

- **A per-class LINE bound.** The owner considered retiring the row line bound while giving dossiers and
  run-state files their own line value, and chose outright retirement instead. The row class carries no
  line bound after this unit.
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
`:376-378`. This unit triples it and removes the line bound as well. The owner ratified that on
2026-08-17, asked a second time, with the 22-of-29 population measurement and the 3.3x-to-4.3x dossier
figure in front of them. §4 prices it; §8 F3 carries the one question the decision opens.

## 4. Design

### Data model

One conf key, `ROW_DOC_CAP_BYTES`, holding a byte count, declared 61,440 here. Resolution has three
branches and one non-obvious step: the engine pre-sets its defaults and then sources the conf at `:27`,
so a blank conf line overrides a pre-set default with blank. Every existing key in that block documents
blank as skip, which is the opposite of what this key needs, so the design re-normalises AFTER the
source. A non-numeric value refuses with `exit 2` before the scan.

There is no value that disables the bound, and the shipped default stays 20,480 so nothing an adopter
receives changes until they declare their own.

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
| generated indices and ledgers | 3 | 12,328 | 69 |
| other row documents | 5 | 2,695 | 35 |

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
file where it is — the floor is 93.5% of the cap, because the 633-byte head with its three rotation
announcements stays too. It has rotated three times in four days, twice on one of them.
`TOOL-cSettledDocket-16` is OPEN in that shard and says the same thing.

`memory/builds/cSteadyMetronome/README.md` also recorded that rotation orphans ids against check 14,
which is why a rotation was once attempted and reverted. That claim looks stale and this spec does not
rely on it: `corpus_ids.py`'s one walk is `git ls-files` with no `archive/` exclusion, and three
rotations have since landed green. F4 turns the reading into a fixture.

### What retiring the row line bound costs

rev-1 argued the line bound "cannot fire". That was measured on one document and is false: it is the
bound that binds FIRST on 22 of 29 row documents. The retirement therefore removes a bound that is doing
work, and the price is concentrated in one sub-population.

**Dossiers.** A dossier's effective ceiling today is its line count at its own density: 250 x 74.7 is
about 18.7 KB for `memory-tree-merge-driver.md`, about 15.0 KB for `lexicon.md` at 60.0 bytes per line,
about 14.4 KB for `agent-cap.md` at 57.7. After this unit each is bounded at 61,440 bytes alone — a
**3.3x to 4.3x loosening**. At about 58 bytes per line a dossier reaches roughly 1,050 lines with nothing
firing. Dossiers are row class by construction, `tools/codebase-map/test_codebase_map.py` carries no size
or line predicate of its own, and `memory/HYGIENE.md:276-278` gives their remedy as a SPLIT rather than a
rotation — so check 6 is the only thing bounding a dossier at all, and its split trigger moves with the
cap. This is the cost the owner ratified, and it is the subject of F3.

**Run-state files.** Four of five are line-bound today and become byte-bound at 61,440. Behaviour does
not change, because the protocol budgets the authored region at 8 KB and spills against that; check 6 is
the backstop whose purpose is never to be reached. But the fixture that PROVES `RUN.md` is in the
population is line-only, which is why S9 grows it rather than leaving it silent.

**The other line-bound members** — both ledgers, three READMEs, a STATUS file, `FOUNDATION.md` — sit
between 3.6% and 16.4% of the byte cap. The retirement gives them room they were not asking for and
costs nothing observable.

### The three consumers whose behaviour shifts

- **`builds/*/RUN.md`** — no trigger moves; the backstop loosens. The protocol names no byte figure, so
  it needs no edit. Rule 6's clause contradicting it does, and S15 is that edit.
- **Codebase-map dossiers** — the largest shift, priced above. The split trigger moves from an effective
  ~14.5 KB to 61,440 bytes.
- **The generated indices** — `memory/LIVE.md` and the ledger shards are rendered; a larger byte cap
  defers the month a ledger shard would rotate.

### Rollout

**This unit's own records cannot be written until its conf change lands, and that ordering is forced by
the defect.** The figures above are measured at the spec's immutable base. The local default branch has
since advanced 37 commits past `origin/main`, and at that tip `memory/backlog/TOOL.md` is **20,345 of
20,480 bytes — 99.34%, with 135 bytes left**, holding 80 rows of which none is terminal, with no fourth
rotation having occurred. At 253.7 bytes per row, 135 bytes is half a row: **the next backlog row that
tree receives reds check 6**, and rotation cannot make room.

So the landing order is: the conf change and its declared value first, then this build's decision rows
and backlog rows. Writing the records first is red, not merely untidy. This is the bind
`memory/builds/cSteadyMetronome/README.md` described on 2026-08-14 arriving a second time, and it is why
S17 closes `TOOL-cSettledDocket-16` in place rather than filing a fresh row beside it.

The reground onto the local default is the first build pass. It does not move the spec's base or its
figures — a base is immutable and the measurements belong to it — and it shortens the runway by about
half a day.

### Files touched (estimate)

| path | change | forced by |
|---|---|---|
| `.memory-tree.conf` | the key at 61,440, with its derivation and movement | S1 |
| `tools/memory-tree/.memory-tree.conf.example` | the key at the shipped default | S12 |
| `tools/memory-tree/check-memory-hygiene.sh` | conf read and re-normalisation · the cap block · the message · kit version | S2 S4 S5 S6 |
| `tools/memory-tree/check-memory-hygiene.test.sh` | byte-axis arms · the above-750 retirement arm · tRunBig grown · the example-conf arm · `FLOOR_ASSERTIONS` | S7 S8 S9 S11 S13 |
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
- **risks** — Three, and rev-1 named the wrong one as silent. First, a blank or zero byte cap is the
  LOUDEST failure available: measured on this repo's awk, `19152 > ""`, `19152 > 0` and an uninitialised
  right-hand side all evaluate true, so the whole class reds at once. Second, the genuinely silent
  direction is a bound that cannot fire — which is what this unit deliberately creates for the row line
  axis, and why S8 pins its arm above the guide's 750 rather than inside the band where a slip is
  invisible. Third, the shared `cl` variable in S4: deleting the row assignment leaves the guide's 750
  governing rows, which looks like a successful retirement and is a silent 3x line raise instead.
  Rollback is reverting one commit; nothing migrates.
- **testing + left-shift gates** — S7 to S11 and S13. The byte axis of check 6 gains its first arm in the
  kit's life; S9 keeps the one row-class arm that three other contracts hang on.
- **migration / rollback** — None required. An adopter who never declares the key keeps today's verdicts
  exactly, because S3 keeps the shipped default at the present value.
- **user docs** — The kit README and both HYGIENE carriers, per S14. No end-user surface.

One item for the owner scope menu: F3, the dossier byte sub-bound, which the F5 decision opened.

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
- **AC4** — When the guide fixtures run, `memory/guides/tfixture.md` past 750 lines is still NAMED and
  `memory/guides/twide.md` at 401 lines is still SILENT, proving the classes are still separate and that
  the silent control was not rebuilt.
- **AC5** — When the suite runs, `memory/builds/tRunBig/RUN.md` is still NAMED by check 6, now on the
  byte axis, so the `index_set` membership proof and the check-7 exemption precondition asserted on that
  same file both still hold.
- **AC6** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, its new check-6 row arms
  fail on the BYTE axis and `FLOOR_ASSERTIONS` has been raised to the new executed count.
- **AC7** — When `bash tools/memory-tree/check-verdict-epoch.sh` runs over this diff it is green, and
  `KIT_MEMORY_TREE_VERSION` no longer reads `2.18`.
- **AC8** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs it is green, which is the gate
  that pairs `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` with
  their templates — so it is also what observes S16's corrected budget line in both carriers.
- **AC9** — When `git grep -nE '20 ?KB|20,?480|250 lines'` runs over the explicit S14 carrier list, no
  listed carrier still states a retired figure. Expected survivors elsewhere, each for a stated reason:
  `memory/DECISIONS.md:41` (the ratified `TOOL-aWidenedGuide-1` row, in an append-only log),
  `.memory-tree.conf:57` and `tools/memory-tree/corpus_ids.py:461` (`READ_PATH_CEILING`'s headroom, out
  of scope), the engine's own shipped default at 20,480 per S3, the guide class's own `750`, and the test
  fixtures. The criterion is scoped to a path list because a tree-wide zero-survivor sweep is
  unsatisfiable.
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

Bug classes the checklist selects: `fixture-passes-by-finding-nothing` (S8, S9, S10 exist for it) ·
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

### F3 — RE-OPENED by F5's answer: does the dossier sub-population need its own byte bound?

F3 previously asked whether the row class needs a per-document-kind matrix, and rev-3 recommended no on
the grounds that a dossier's operative bound was the line count this unit would not touch. **F5's answer
removes that ground.** After retirement a dossier is bounded only at 61,440 bytes, which at its measured
density is roughly 1,050 lines; check 6 is the only size gate a dossier has, and its declared remedy is a
split.

Options: one key for the whole row class, accepting ~1,050-line dossiers until the map's convergence
discipline is felt; or one extra branch giving the dossier sub-population its own byte bound at roughly
its present effective ceiling, so the backlog shards get their 61,440 and dossiers keep the pressure to
split.

**Recommendation: the dossier sub-bound.** It is one branch and one conf key, it keeps the relaxation
aimed at the population that asked for it, and it is the cheapest thing that stops the retirement
reaching a class the owner's goal never mentioned. This is the only item that changes what gets built, so
it is not resolved here.

### F2 — absent-and-blank semantics · recommendation not overruled

Absent and blank both resolve to the shipped default; no value disables the bound. Put to the owner in
the 2026-08-17 hand-back with F1 and F5 and not overruled, so S2 builds it. This is the policy-ceiling
idiom rather than the measured-pin idiom, and it needs the explicit re-normalisation S2 specifies.

### F4 — the stale rotation claim · recommendation not overruled

Confirm by fixture in this unit that rotating a backlog does not orphan the ids the moved rows defined.
Put to the owner in the same hand-back and not overruled. Two arms in a suite this unit already edits,
and the re-shape unit's options depend on the answer.

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
  §4 gained "What retiring the row line bound costs", pricing the dossier shift at 3.3x-4.3x and about
  1,050 lines. Three arms follow from the audit's folds: AC3 is pinned above 750 rather than 250 because
  the 251-750 band cannot distinguish retirement from the shared-`cl` slip, AC5 keeps `tRunBig` named on
  the byte axis so two contracts asserted through it survive, and AC4 protects the silent control. §5
  risks gained the shared-`cl` hazard and now names the cannot-fire direction as one the unit creates on
  purpose. F3 is RE-OPENED, because its rejection rested on the line bound staying.

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
