## Verdict: BLOCKED

*Review shape: raw 55, confirmed 38, refuted 17, unverified 0, precision 0.69, lenses 4/4, verify
batches 5. M4 spec audit over `spec/2026-08-17-spec-TOOL-aRelaxedShard-1.md`, read against this
worktree at the spec's declared base `43eb6b10`. Every number below was re-measured against source
rather than read back out of the spec.*

One blocker, seven highs. The 38 confirmed findings collapse to 21 distinct defects, because four
lenses read the same spec: the line-bound premise arrived three times (underspecification,
contradiction, prior-art), the truncated Inventory table four times, AC7's sweep command four times,
the `18,314` row-byte figure three times, and F1's third-candidate runway four times. Each merged
entry carries the strongest measurement any instance produced.

The blocker is not a gap — it is a measurement generalised from one document. §4's case for retiring
the row line bound is derived correctly and then tested against `memory/backlog/TOOL.md` alone; on
the other 28 members of the class it is false, and it is false hardest for the sub-population §4's
Inventory table omits. Six further findings are downstream of that same omission, which is why the
fold has to start at the Inventory rather than at S3.

The dominant secondary shape is the one this repo keeps finding: an acceptance criterion that names a
gate which cannot make the observation the criterion asserts. AC5, AC7 and AC8 are all that shape.

## Blocker

### B1 — §4 "Why the line bound goes rather than moving": the retired bound is the OPERATIVE one for 22 of 29 row documents

*Converged from three lenses: underspecification, contradiction, prior-art.*

§4 concludes "The line bound is not strict, it is unreachable" and that "the byte bound decides every
real case", and S3 retires it for the whole row class on that basis. The spec derives its own
break-even correctly — 20480/250 = 81.92 B/line, its "under 82 bytes" — and then tests it against one
document.

Measured over check 6's actual row-class population at base `43eb6b10`
(`bash tools/memory-tree/check-memory-hygiene.sh --print-index-set` returns 33 files; the only class
override is `index(f, gp)==1` with `gp="$M/guides/"` at `tools/memory-tree/check-memory-hygiene.sh:385`,
and exactly 4 files sit under `memory/guides/`, so 29 are row class), **22 of 29 sit below 81.92
B/line and are line-bound first**: all 12 `memory/map/features/*.md` dossiers (51-74 B/L), 4 of 5
`memory/builds/*/RUN.md` (45-77 B/L), both ledger shards (81.0 and 70 B/L), `memory/README.md` (69.3),
`memory/map/README.md` (68.9), `memory/map/FOUNDATION.md` (24.4), and
`memory/builds/aPrunedCeremony/STATUS.md` (79.3). The 251 B/row mean the argument generalises from is
`memory/backlog/TOOL.md`'s row set alone.

The nearest-to-cap row document in the tree on either axis is
`memory/map/features/memory-tree-merge-driver.md`: 14,713 B / 197 L, i.e. **197 of 250 lines (78.8%)
against 14,713 of 20,480 bytes (71.8%)**. The line bound is closer, today, on the axis §4 calls
unreachable. `lexicon.md` is at 190/250, `unattended.md` at 171/250.

The supporting 75,000-byte arithmetic also rests on the 300-char entry budget, which check 7's `ex7`
exemption (`tools/memory-tree/check-memory-hygiene.sh:400-401`) removes for exactly the `RUN.md`,
dossier and `FOUNDATION.md` members whose density makes the line bound bind. Dossiers are row class by
construction (`:341-353`) and their declared remedy is a SPLIT (`memory/HYGIENE.md:276-278`);
`tools/codebase-map/test_codebase_map.py` carries no size or line predicate of its own, so check 6 is
the only thing that bounds a dossier at all. With S3 plus F1's recommended 61,440 a dossier at its
measured ~58 B/line reaches roughly 1,050 lines with nothing firing.

**Fold.** §4 "Why the line bound goes rather than moving" must be rewritten against the measured
population, not against TOOL.md, and §2 S3 rescoped to what that measurement supports. Three
buildable shapes, in order of smallest diff: (a) keep the row line bound and move only the byte bound
— the goal in §1 is satisfied without touching the line axis at all; (b) retire the line bound and
declare it too (`ROW_DOC_CAP_LINES`), so the class keeps two bounds an adopter can measure; (c) retire
it only for the sub-population whose density makes it dead, which means a per-kind split and therefore
reopens F3. Whichever is chosen, §4 must state the 22-of-29 measurement and the
`memory-tree-merge-driver.md` 197/250 case, because the current text asserts the opposite. If (a) is
taken, S5/S6, AC3 and the S8/S9 prose sweep shrink correspondingly and F1 becomes the whole unit.

## High

### H1 — §6 AC7: the sweep command does not run as written, and its zero-survivor predicate is unsatisfiable

*Converged from four lenses: underspecification, contradiction, assumption, prior-art.*

`grep -rnE '20 ?KB|20480|250 lines' -- ':!memory/archive' ':!memory/builds'` is git-pathspec syntax
handed to plain grep. Run verbatim in this tree it prints `grep: :!memory/archive: No such file or
directory` twice, exits 2, and searches nothing — with the errors on stderr and **stdout empty**, so a
builder grading "no output" scores AC7 satisfied having scanned zero files. That is
`vacuous-selector-empty-population`, which §7 names as a class this review must answer.

Repaired to `git grep`, the predicate still cannot pass inside the scope §2/§3 declares. Survivors
after S8+S9: `memory/DECISIONS.md:41`, the ratified `TOOL-aWidenedGuide-1` row ("rows keep 20 KB /
250") in a log the engine holds append-only (`APPEND_ONLY_ERE`,
`tools/memory-tree/check-memory-hygiene.sh:48`) and `memory/HYGIENE.md:70` says is never rewritten;
`.memory-tree.conf:57` and `tools/memory-tree/corpus_ids.py:461` (`headroom = 20480`), both
`READ_PATH_CEILING` carriers §3 declares stay exactly as they are; `.gitattributes:26` and `:30`; and
`tools/memory-tree/check-memory-hygiene.test.sh:363`. The pattern is separately under-inclusive: it
misses the comma spelling at `memory/map/features/build-method.md:73` ("16,680 of 20,480 B").

**Fold.** §6 AC7: split the criterion in two. Keep the `kit-dogfood-parity.test.sh` clause as AC7.
Replace the sweep clause with a runnable, bounded one — `git grep -nE '20 ?KB|20,?480|250 lines'`
scoped to an explicit path list equal to the S8/S9 carrier set, asserting that each named carrier no
longer states the retired figure — and state in the criterion that `memory/DECISIONS.md`,
`.gitattributes`, `.memory-tree.conf:57` and `corpus_ids.py:461` are expected survivors with the
reason for each. An AC whose command cannot execute is worse than no AC.

### H2 — §4 Inventory: "Every row document in this tree" lists 7 of 29, and the consumer note that follows is false on both axes

*Converged from four lenses: underspecification, contradiction, assumption, prior-art.*

The table is headed "Every row document in this tree, measured at the spec's base sha" and lists
`memory/backlog/TOOL.md`, `memory/DECISIONS.md`, `memory/ledger/2026-08.md`, `memory/LIVE.md` and the
three other backlog shards. All seven figures reproduce exactly at base (19,152 / 12,328 / 3,240 /
2,054 / 1,741 / 1,734 / 373). The completeness claim does not: the class holds 29 files (population
per `tools/memory-tree/check-memory-hygiene.sh:337-359`). Omitted are 12 `memory/map/features/*.md`
dossiers, 5 `memory/builds/*/RUN.md`, `memory/builds/aPrunedCeremony/STATUS.md`, `memory/README.md`,
`memory/map/README.md`, `memory/map/FOUNDATION.md` and `memory/ledger/2026-07.md`.

Two omitted files are FULLER than the table's second-place entry:
`memory/map/features/memory-tree-merge-driver.md` at 14,713 B (71.8%) and
`memory/builds/cBriefedPilot/RUN.md` at 13,806 B (67.4%), against the 60.2% listed for
`memory/DECISIONS.md`. So §4's consumer note "No dossier is near the bound today" is wrong on the byte
axis at 71.8% and wrong again on the line axis at 197/250. The omission is precisely what lets §4
conclude the byte bound decides every real case, and every figure in §4 and §8 derives from this
table.

**Fold.** §4 Inventory: either enumerate all 29 rows, or re-head the table "the seven largest row
documents" and add a per-kind summary line for the dossier, `RUN.md` and generated-index
sub-populations carrying max bytes AND max lines each. Delete "No dossier is near the bound today" and
replace it with the measured 14,713 B / 197 L. The bytes-only shape of the table is what hid B1;
adding a lines column and a share-of-250 column is the cheapest way to keep it from hiding it again.

### H3 — §2 S6 / §6 AC3: the discrimination arm is set at a threshold that cannot discriminate

The engine sets both caps on a shared pair — `cb = 20480; cl = 250; if (index(f, gp) == 1) { cb =
61440; cl = 750 }` (`tools/memory-tree/check-memory-hygiene.sh:384-385`). S6 specifies its arm as "a
row document over 250 lines and under the byte cap must be SILENT" and justifies it with "Without it
the change is indistinguishable from raising the line cap". At 251-750 lines that fixture is silent
under the intended retirement AND under the likeliest implementation slip: deleting the row branch's
`cl` leaves the guide class's 750 in play on the shared variable, and a guard written `cl>0 && l>cl`
with `cl` defaulted to 750 does the same. The arm is itself indistinguishable from raising the row
line cap to 750. AC2's no-line-figure clause grades the message, not the bound; AC4 grades only the
guide class.

**Fold.** §2 S6 and §6 AC3: pin the fixture above the guide class's `cl` — over 750 lines and under
the byte cap — or additionally assert that the row finding message carries no line bound at all.
State the 750 reason in S6 so the number is not silently lowered later.

### H4 — §4 consumers / §8 F1: the unit multiplies the dossier budget by 3.3-4.3x, which is what `TOOL-aWidenedGuide-1` recorded as refused, and §4 tells the owner the opposite

A dossier's effective ceiling today is the LINE cap at its own density: 250 x 74.7 = ~18.7 KB for
`memory-tree-merge-driver.md`, ~15.0 KB for `lexicon.md` (60.0 B/L), ~14.4 KB for `agent-cap.md`
(57.7 B/L). Retire the line bound, adopt F1's 61,440, and every one of those becomes 61,440 — a
3.3-4.3x loosening of exactly the class the recorded decision refused to triple. The engine's own
comment at `tools/memory-tree/check-memory-hygiene.sh:376-378` states the ground verbatim ("tripling
the allowance for a backlog shard or a map dossier would loosen a curation discipline nobody asked to
loosen") and `memory/DECISIONS.md:41` ratifies it. §3 declares no non-goal covering this, and §10
frames `aWidenedGuide-1` as the seam extended rather than a refusal reopened. (The `RUN.md` half of
this is weaker and is not counted here: §4 does disclose that the backstop loosens and argues only
that no spill trigger moves, which is fair.)

**Fold.** §4 "The three consumers": price the dossier shift in the numbers above and say plainly that
it triples-plus. Then either §3 gains an explicit statement that the row-class curation discipline
`aWidenedGuide-1` protected is being deliberately relaxed with the measurement behind it, or §8 gains
a fifth fork asking the owner to ratify the dossier loosening separately from the backlog one. §10
must name the decision as reopened, not extended.

### H5 — §8 F3: "Three of the four sit under 20% of the present cap" is false for all four

F3's stated basis for rejecting a per-kind matrix, restated in §3 and §4 Alternatives. Measured
against 20,480: backlog shard 19,152 B = 93.5%, decision log 12,328 B = 60.2%, largest dossier
`memory/map/features/memory-tree-merge-driver.md` 14,713 B = 71.8%, largest run-state file
`memory/builds/cBriefedPilot/RUN.md` 13,806 B = 67.4%. Zero of four are under 20%; even on medians
only backlog shards (8.5%) clear it. The recommendation may well still hold — this attacks the stated
factual basis, not the conclusion.

**Fold.** §8 F3: replace the sentence with the four measured maxima and re-argue the rejection on the
grounds that actually survive — the run-state file's real bound is the protocol's 8 KB authored
budget, and a dossier's remedy is a split. If B1's fold takes shape (c), F3 is no longer rejectable
and must be re-opened rather than re-worded.

### H6 — §2 S2 / §6 AC1: the kit's shipped default byte cap is never stated, and one candidate answer reds AC7

S2 makes the key resolve to "the kit's shipped default" and AC1 tests against it; §4 Data model, §5
and F2 all lean on it. No section names its value, and §8's four forks do not cover it. If it stays
20480 the literal survives at `tools/memory-tree/check-memory-hygiene.sh:384` and AC7's sweep hits the
engine itself. If it becomes F1's ratified value, every adopter inherits this corpus's measured number
with no measurement of their own — `pin-copied-from-another-corpus`, the class §7 selects for and the
exact objection §4's first rejected alternative raises. The build cannot start without an answer.

**Fold.** §2 S2: state the shipped default's value and its basis in one clause. If it is the ratified
value, add it to §8 F1 as part of that fork's decision, because the two are then the same number
chosen for two different populations. Whatever it is, §6 AC7's expected-survivor list (per H1) must
account for it.

### H7 — §5 error states: the non-numeric requirement is owned by no scope item, observed by no criterion, and "loudly" has no channel; S2's BLANK half is unarmed too

§5 requires that "a non-numeric value must fail loudly rather than coerce to zero through awk's `+0`".
S2 covers only "an absent or blank value resolving to the kit's shipped default", and AC1-AC10 contain
no observation of the non-numeric branch. "Loudly" is undefined against three live precedents in the
same engine: `exit 2` with a bare message (`tools/memory-tree/check-memory-hygiene.sh:101`), a
`fail <n>` line that sets `status=1` (`:63`), or a pop_guard-style refusal. Separately, AC1's witness
is "a scratch tree whose conf declares no `ROW_DOC_CAP_BYTES`" — absent only — so the BLANK branch,
which is the entire subject of fork F2, ships with no acceptance criterion in a spec whose deliverable
is that key's semantics.

**Fold.** §2 S2: add the non-numeric branch to the scope item and name its channel (refuse before the
scan with `exit 2`, matching the conf-validation precedent at `:101`, is the smallest). §6 AC1: split
into AC1a absent and AC1b blank, both resolving to the default, plus AC1c a non-numeric value
producing the named refusal.

## Medium

### M1 — §4 Files touched: three files that named gates make mandatory are absent

*Converged from two lenses: underspecification, contradiction.*

S4 bumps `KIT_MEMORY_TREE_VERSION` off 2.18. `tools/check-kit-versions.sh` derives its marker
population from `git ls-files 'tools/memory-tree/*.template.md'` and requires `gov:kit
memory-tree@<constant>` in every member; the tracked set is `BUILD-METHOD.template.md`,
`HYGIENE.template.md` and `SPEC-TEMPLATE.template.md`, all three at `@2.18` on line 1.
`tools/memory-tree/kit-dogfood-parity.test.sh:53` then pairs `memory/TEMPLATE-SPEC.md` (also `@2.18`) with the third.
Neither `tools/memory-tree/SPEC-TEMPLATE.template.md` nor `memory/TEMPLATE-SPEC.md` appears in the
table or any S-item, while §7 commits both legs green. Third: `memory/guides/SESSION-KICKOFF.md` —
`skills/session-kickoff/manifest-check.sh` C5 reds on a watched change with no `last-audit` re-stamp,
and `.memory-tree.conf`, `tools/memory-tree/check-memory-hygiene.sh` and
`memory/guides/BUILD-METHOD.md` are all in that file's `watch:` list (line 6). Fourth:
`memory/map/baseline.toml:53` still lists `memory-tree` under `kits`, and
`tools/codebase-map/test_codebase_map.py` reds with "LAZY BASELINE (now claimed — delete its baseline
line)" once S10's dossier claims the key; AC9 requires that leg green. S10 cites the baseline line, so
that one is a table omission rather than a scope gap.

**Fold.** §4 Files touched: add `tools/memory-tree/SPEC-TEMPLATE.template.md`,
`memory/TEMPLATE-SPEC.md`, `memory/guides/SESSION-KICKOFF.md` and `memory/map/baseline.toml` with the
leg that forces each. "(estimate)" does not soften a set three named legs make deterministic.

### M2 — §2 S8: the prose-carrier enumeration is short, and `.gitattributes` is in no scope item while AC7 hits it

*Converged from two lenses: assumption, prior-art.*

`git grep -nE '20 ?KB|20480|250 lines' -- memory/HYGIENE.md` returns `:66`, `:128`, `:132`, `:276`.
The check-catalog rule 6 body spans `:127-136`, so `:132` is inside rule 6 and `:276` is the only site
LATER than it. S8's "rule 6 and its two later restatements" therefore cannot reach
`memory/HYGIENE.md:66` — "**File caps:** index + generated files ≤ 20 KB AND ≤ 250 lines" — the
earliest and most adopter-visible carrier, and the one that already fails to mention the class split
`aWidenedGuide-1` created. `tools/memory-tree/HYGIENE.template.md` mirrors all four at the same line
numbers, so "the same three" is short there too. And `.gitattributes:26` ("check 6 caps index files at
20 KB", present tense, inside the block that justifies the `eol=lf` pin for checks 6 and 7) plus `:30`
is a carrier in neither S8, S9 nor the files-touched table — while AC7's sweep hits it. §2 and AC7
disagree about the population.

**Fold.** §2 S8: enumerate the carriers by line rather than by count — `memory/HYGIENE.md:66`, `:128`,
`:132`, `:276` and the four mirrors in `tools/memory-tree/HYGIENE.template.md` — and add
`.gitattributes:26,30` to the sweep and to §4's table. (`memory/map/features/build-method.md:73` was
checked and is NOT a carrier to sweep: its figures describe the guide's self-imposed budget and stay
true.)

### M3 — §2 S8 against §4's own finding: `memory/HYGIENE.md` rule 6's spill clause carries no number, so the sweep leaves the mis-citation S9 exists to correct

`memory/HYGIENE.md:133-136` and its lockstep twin `tools/memory-tree/HYGIENE.template.md:133-136`
read "`builds/*/RUN.md` is a ROW document on both counts: it is designed to GROW, so the cap is the
bound the protocol spills against", and the engine repeats it at
`tools/memory-tree/check-memory-hygiene.sh:347-353` ("before the cap is reached").
`memory/guides/UNATTENDED-PROTOCOL.md:130-132` in fact budgets the authored region at 8 KB and spills
against that — which §4's own consumers bullet states correctly. S8 scopes rule 6 as a carrier of the
retired NUMBERS, and this clause carries none, so it survives; raising the row byte cap widens the gap
between the spill trigger and the cap and makes the sentence more wrong. It is the same
mis-attribution class S9 corrects one file over.

**Fold.** §2 S8: add the clause explicitly — rule 6's spill sentence in both HYGIENE carriers is
corrected to name the protocol's 8 KB authored budget as the spill trigger and check 6 as the
backstop, matching the wording §4 already uses.

### M4 — §2 S5: the fixture account is wrong, and the one row-class check-6 arm is load-bearing for two other contracts

*Converged from two lenses: underspecification, contradiction.*

S5 (and the README's "What this build found on the way in") says "Today all three check-6 fixtures
trip on line count". `tools/memory-tree/check-memory-hygiene.test.sh:372-373` builds
`memory/guides/twide.md` at 401 lines expressly as the SILENT control, asserted by
`cnot 6 'memory/guides/twide.md'` at `:574`; the comment above it says that fixture is what makes the
guide widening observable at all. A builder acting on "all three trip" could rebuild it on the byte
axis and destroy the `aWidenedGuide-1` arm. The load-bearing conclusion — the byte axis is unarmed —
is correct: all three fixtures are line-axis constructions.

Second half: `chit 6 'memory/builds/tRunBig/RUN.md'` (`:597`) is documented at `:591-598` as the only
proof `RUN.md` entered `index_set` at all AND as the scoping control proving the guide widening did
not leak into the row class, and the check-7 exemption arm at `:602-604` is explicitly asserted "on
the SAME file check 6 just named, so membership is already established". The fixture (`:427-429`) is
265 lines and ~3 KB, so LINES are its only over-cap axis: retiring the row line bound silences check 6
on it and vacates both contracts, making the `:602-604` arm pass for a file that never joined the
population. That is `fixture-passes-by-finding-nothing`, which §7 requires answered.

**Fold.** §2 S5: correct the fixture claim to "two of the three check-6 fixtures trip on line count;
`memory/guides/twide.md` is the deliberate silent control and must stay one", and state that the
byte-axis rebuild must keep a row-class `chit 6` on `memory/builds/tRunBig/RUN.md` (i.e. grow that
fixture past the byte cap) so the `index_set` membership proof and the check-7 exemption precondition
at `:602-604` survive. Same correction in the README's findings section.

### M5 — §6 AC5: the printed count is derived, so the clause is satisfied by a no-op, and the artifact that must move is named by no criterion

`n` increments inside the assertion helpers (`tools/memory-tree/check-memory-hygiene.test.sh:436-500`
plus ~50 inline sites), so the printed count moves automatically the moment an arm is added — nobody
edits it, and it cannot "stay at the floor". The shrink-only pin is `FLOOR_ASSERTIONS=136` at `:989`,
compared as `[ "$n" -ge "$FLOOR_ASSERTIONS" ]`, so adding arms without raising it stays green.
`tools/check-testsuite-counts.sh:48-60` holds no number for this suite — it asserts only that the file
prints the agreed shape, pins a non-zero floor, and compares the two. So the floor, which is what
keeps the new byte-axis arms from silently going dark later, is required by nothing. (AC5's first
clause, that the row arms fail on the BYTE axis, is a genuine observation and stands.)

**Fold.** §6 AC5: replace "has moved to match the arms added rather than staying at the floor" with
"and `FLOOR_ASSERTIONS` in that file has been raised to the new executed count", which is the
shrink-only artifact an arm deletion would have to fight.

### M6 — §6 AC8: the named gate cannot make the observation, and is green whether or not S9 landed

`tools/memory-tree/check-method-carriers.sh` builds its population from `git ls-files` with
case-exclusions at `:52-56` that skip `"$M"/*` — all of `memory/`, hence
`memory/guides/BUILD-METHOD.md` — and `"$KITREL"/BUILD-METHOD.template.md`. Its own header says the
test is structural: is this file declared, and does its mention look like a pointer. It never compares
the two carriers' budget line. The gate that pairs them is
`tools/memory-tree/kit-dogfood-parity.test.sh:53`, whose `PAIRS` includes
`$M/guides/BUILD-METHOD.md:$KITREL/BUILD-METHOD.template.md` — which AC7 cites for a different
purpose.

**Fold.** §6 AC8: keep `check-method-carriers.sh` green as a separate clause if wanted, but move the
"both state the same corrected budget line" observation onto
`bash tools/memory-tree/kit-dogfood-parity.test.sh`, which is the gate that actually pairs them.

### M7 — §10 / §4 Data model: the cited in-file conf-key precedent does not exist, and the engine's real idiom is the inverse of the one §4 wants

§10 names "the conf-key convention the same file uses for `READ_PATH_CEILING`, `UNIVERSAL_BUDGET` and
`ROW_DUPLICATE_PIN`", where the only file named is the engine. `git grep` shows
`tools/memory-tree/check-memory-hygiene.sh` mentions `READ_PATH_CEILING` only in a prose comment at
`:375` and contains neither of the other two; the readers are `tools/memory-tree/corpus_ids.py:74`,
`tools/memory-tree/gotchas.py:84` and `tools/memory-tree/row_grammar.py:42`. It matters because the
engine's own six keys (`:16-26`) are pre-set defaults followed by `. "$ROOT/.memory-tree.conf"` at
`:27`, so a blank conf line OVERRIDES the default with blank, and every one of those keys documents
blank as skip / never-required. An implementor copying the cited precedent gets exactly the
blank-disables-the-bound behaviour §4 forbids, and §4's "the kit's usual one" is in fact a new idiom
for this file needing an explicit post-source re-normalisation §4 never specifies.

**Fold.** §10: name the actual readers (`corpus_ids.py`, `gotchas.py`, `row_grammar.py`) or say
`.memory-tree.conf` rather than "the same file". §4 Data model: specify the re-normalisation
explicitly — after sourcing the conf, an empty `ROW_DOC_CAP_BYTES` is reset to the shipped default —
because the engine's own convention does the opposite.

### M8 — §2 S7: the one deliverable an adopter receives has no gate and no criterion, and shipping it blank contradicts that file's own idiom

No leg reads `tools/memory-tree/.memory-tree.conf.example`'s key set:
`tools/memory-tree/adopt-memory-tree.sh:40` only `cp`s it, and `tools/check-install-prefix.sh:17`
explicitly excludes `*.conf.example`. No AC1-AC10 bullet mentions the example conf, so if S7 is
forgotten nothing reds and — in S7's own words — "a key missing from it is a key no adopter ever
sees". Separately, blank in that file means "check off" for every measured pin (`ORPHAN_ID_PIN`,
`DEAD_PATH_PIN`, `READ_PATH_CEILING`, the three cutoffs), while both POLICY ceilings ship WITH a value
and say why: `UNIVERSAL_BUDGET="3"` ("Unlike the pins above this is a POLICY CEILING you choose ... so
it ships with a value rather than blank") and `ROW_DUPLICATE_PIN="0"` ("A POLICY refusal, not a
measured-blank pin: ship it with a value"). `ROW_DOC_CAP_BYTES` is the same kind of key.

**Fold.** §2 S7: ship the key WITH the shipped default's value and a comment in the policy-ceiling
idiom, not blank. §6: add a criterion that observes the example conf carries the key — the cheapest is
an arm in `check-memory-hygiene.test.sh` asserting the shipped example declares it, since nothing else
reads that file.

### M9 — §5 risks: the named silent direction is inverted

§5 says "awk coerces a blank to `0`, which is the silent direction". The comparison is
`b[f]+0>cb || l[f]+0>cl` (`tools/memory-tree/check-memory-hygiene.sh:386`). Measured on this repo's
awk (GNU Awk 5.4.0): `19152 > ""` -> 1, `19152 > <uninit>` -> 1, `19152 > 0` -> 1, and the same via
`-v cb=` and `-v cb=0`. A blanked cap therefore names all 29 row documents at once, which is the
LOUDEST possible failure. The genuinely silent direction is the one §5 does not name: an over-large
declared value, or a line sentinel set so high it can never fire — which is the exact shape this unit
is retiring.

**Fold.** §5 risks: separate the two variables. State that a blank or zero CAP reds the whole class
(loud, self-announcing) and that the silent direction is an over-large declared value or a sentinel
that cannot fire, then say which of those the design accepts and why. If B1's fold keeps a line bound,
the sentinel sentence goes away with it.

### M10 — §4 Inventory / "Why rotation cannot be the answer here": the row-byte figure does not reproduce, and the rotation floor is understated

*Converged from three lenses: contradiction, assumption, prior-art.*

`git show 43eb6b10:memory/backlog/TOOL.md | grep -E '^- ' | wc -c` is **18,519 B** over 73 rows, not
the stated 18,314. No reading yields 18,314: without newlines the rows are 18,446, without the `- `
prefixes 18,300; 18,314 is the CHARACTER count including newlines, for a check that measures `wc -c`.
So mean row length is 253.7 B not 251, and the derived figures move: growth ~2,057 B/day not 2,034,
and F1's basis 250 x 253.7 = 63,425 (still rounding to the recommended 60 KiB, so the recommendation
survives). The whole-file 19,152 does reproduce.

Second, sharper half: the live shard's post-rotation floor is the WHOLE 19,152-byte file — 93.5% of
cap — not 18,314 / 89.4%. Rotation moves terminal rows only (`memory/HYGIENE.md:67-68`) and leaves the
633-byte head, whose lines 4-5 are two ~275 B per-rotation announcements. With zero terminal rows
(verified: 66 OPEN, 6 SPECCED, 1 DEFERRED, 0 CLOSED, 0 WONTDO) a fourth rotation leaves the file at
19,152 B. §4 gives 93.5% for that same file in its own table two paragraphs earlier, so the section
contradicts itself; `memory/builds/aRelaxedShard/README.md:33` repeats the understated 89.4%.

**Fold.** §4 Inventory "Row length": 18,519 B across 73 rows = 253.7 B/row, and say `wc -c` bytes not
characters. §4 "Why rotation cannot be the answer here": the floor is the whole file, 19,152 B, 93.5%
of cap. §8 F1 row 1: restate the basis as 250 x 253.7 = 63,425, rounded to 61,440. README line 33: the
same 93.5%.

### M11 — §4 Inventory: the "rows" column answers two different questions

Measured at base: `memory/backlog/PLAY.md` is 9 lines but 6 dash rows (table says 9), `DEPL.md` 11
lines / 6 rows (says 11), `KICK.md` 4 lines / 1 row (says 4), while `TOOL.md` is 78 lines / 73 rows
and the table correctly says 73. So three of four cells are physical line counts and the fourth is the
true row count, in the column the cap value is reasoned from. Read as rows the table understates mean
row length badly — PLAY is 1,741/6 = 290 B/row, not 193. `two-answers-to-one-question`, which §7
selects for.

**Fold.** §4 Inventory: make the column `lines` and add a separate `rows` column (or drop the rows
figures for the three small shards and keep the derivation in the Row length bullet, which is where
F1 actually reads it from).

### M12 — §2 / §4 / §10: the OPEN backlog row already filed for this exact defect is cited nowhere

`memory/backlog/TOOL.md:72` reads "`TOOL-cSettledDocket-16` · OPEN · the TOOL index is at its
20480-byte cap with 81 rows and NOTHING terminal left to rotate, so new rows are now paid for by
shortening old ones" — this unit's problem statement, already filed, and returned at rank 13 by the
recall probe §10 records (re-run: still rank 13 of 40). Neither the spec nor
`memory/builds/aRelaxedShard/README.md` mentions it (`grep -n cSettledDocket` over both exits 1), and
§4's files-touched row for `memory/backlog/TOOL.md` says only "the decision row and the follow-up
rows". Landing as specced leaves a stale OPEN duplicate in the very shard the unit exists to unblock;
this repo's convention closes such a row against the id that resolves it (see "closed by
TOOL-aDrainedSluice-3" in `memory/archive/TOOL.2026-08-14.md`).

**Fold.** §2: add a scope clause closing `TOOL-cSettledDocket-16` against `TOOL-aRelaxedShard-1`, or
§10 records why it stays open (e.g. the re-shape unit owns it). §10 should list it among the records
that bind, since the probe returned it.

## Low

### L1 — §8 F1: the third candidate's runway is computed on a different formula from its neighbours

*Converged from four lenses.* Rows 1 and 2 price runway from today's 19,152: (61440-19152)/2034 = 20.8
-> "~21 days" and (39632-19152)/2034 = 10.1 -> "~10 days", both as printed. Row 3 prints "~90 days",
which is 184500/2034 = 90.7, i.e. growth from ZERO; on the other rows' formula it is
(184500-19152)/2034 = 81.3 days. The stated basis does not produce the value either: a quarter at
2,034 B/day is 91.25 x 2034 = 185,602, and 90 days is 183,060. `memory/builds/aRelaxedShard/README.md`
repeats "the 90-day one". The row exists to be rejected on readability, so the conclusion is
untouched.

**Fold.** §8 F1: "~81 days" for the third row, or one column header stating that runway is measured
from today's 19,152 and a corrected value. Same figure in the README's F1 bullet.

## Refuted

Seventeen of the 55 raw findings were refuted on measurement (precision 0.69). The instructive one:
four separate passes filed the §5 risk-direction defect, and three of the four were refuted because
they attacked the byte CAP while §5's sentence is about a `cl` line sentinel whose form S3 has not
fixed — under a guarded `cl>0 &&` shape a blank `cl` really does disarm silently. What survived
(M9) is the narrower claim that a blank BYTE cap is loud, measured on this repo's awk. Two others
worth naming: the recall probe in §10 is not re-runnable as evidence of absence, because
`tools/memory-recall/query.py` caps the result set at about 40 hits and six of today's forty slots are
this build's own records, which did not exist when §10 was written; and the "rotation orphans ids"
window correction failed against source — exactly five of the 161 ids predate the window, not sixteen,
giving 17.3 ids/day against the spec's 17.9.

## Unverified

None. Every raw finding received a skeptic verdict.

## What the fold must not do

The fold to B1 is where the risk sits. Keeping or declaring a row line bound must not touch the guide
class: `tools/memory-tree/check-memory-hygiene.sh:385` sets `cb = 61440; cl = 750` for
`memory/guides/`, `TOOL-aWidenedGuide-1` ratified that split as a decision, and §3 declares raising
the guide cap out of scope. `memory/guides/twide.md` at 401 lines must stay SILENT (`:574`) and
`memory/guides/tfixture.md` past 750 must stay NAMED (`:569`) — those two arms are the only thing that
proves the classes are still separate, and M4 exists because S5 as written would rebuild one of them.

Nothing in the fold may reach `READ_PATH_CEILING`, the 300-char entry budget, or rotation's
carry-forward rule; the `20480` at `.memory-tree.conf:57` and `tools/memory-tree/corpus_ids.py:461` is
a different check's constant and must survive the sweep, which is why H1's fold names it as an
expected survivor. `memory/DECISIONS.md:41` is append-only and must not be rewritten to satisfy any
criterion. Byte normalisation stays with `TOOL-aRootedPrefix-3`, check 10's shard blindness with
`TOOL-cTracedPromise-6`, and the re-shape stays the second unit — none of them is a way out of B1.

Finally, the corrections in M10 and M11 move figures §9 asserts were measured at base `43eb6b10`. Any
re-measurement must be taken at that base and the base restated if it moves, or the Inventory becomes
a mix of two trees — which is the shape that produced B1 in the first place.
