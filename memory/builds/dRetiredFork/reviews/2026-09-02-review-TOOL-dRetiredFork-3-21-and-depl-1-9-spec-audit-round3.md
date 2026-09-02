**Serves:** spec-audit DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21

# Spec audit round 3 — a narrow fold-integrity audit of `8b307f06`

*Node d, 2026-09-02, round 3, on `branch/kit-update-complexity-af0fb0`. This is NOT a fresh review of the set. Round 2 returned BLOCKED with 30 defects, 21 of them created by round 1's fold; its five blockers were promoted to their own units at `5998eb03` and its remaining 25 findings, plus every fork's stated Recommendation, were folded at `8b307f06`. One question was asked: did that fold hold, and did it break anything. The three prior failure shapes were hunted first — instance-not-class, prepend-instead-of-substitute, and one-side-of-a-move — then the fork ratification was read recommendation-against-recommendation, the five promoted units were audited as specs, and every file:line the fold newly asserted was re-derived against source. Review shape: **raw 66, confirmed 41, refuted 25, unverified 0, precision 0.62**, consolidated below into 29 distinct defects; the lenses reached the same fold seams independently, so a defect is listed once with every address it occupies.*

**Reviewed subjects, each pinned at the blob it was read at:** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-1.md@ff5f06a4723f` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-2.md@075c3d5fb74d` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-3.md@f71796e8f8b2` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-6.md@a922617ac92d` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-7.md@8117a46d9e01` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-8.md@df829e7f90f1` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-9.md@7168e68437ca` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-3.md@d9c6adbec166` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-5.md@8453f768ebc0` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-8.md@e93ec20347cb` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-9.md@42694bde1cd4` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-11.md@0b6374c548fb` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-12.md@52ae2ed16428` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-13.md@dd56b27e4e8f` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-14.md@6a50325f6ed1` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-15.md@55fdb646e4e5` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-16.md@7693d3d1814e` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-17.md@a4b0e9fbe443` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-19.md@077d69d27590` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-20.md@a3e8689e3180` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-21.md@dcbd7c3c583e`. **ROUND 3.**

## Verdict: BLOCKED

Three blockers stand after adjudication. The fold held better than round 1's did — the prepend shape is gone entirely, because every edit this round was a substitution, and that is a real structural win worth naming before the bad news. What replaced it is worse in one specific way: **the blanket fork ratification settled recommendations nobody had read against each other,** and one of those ratified picks now contradicts a sibling spec's ratified criterion, in text the same commit wrote. That is blocker 3 and it is the highest-value finding in this round, exactly where the audit was pointed.

The two other blockers live inside the five units promoted at `5998eb03` — units created to fix a defect class and never reviewed. `DEPL-dRetiredFork-8`, promoted because round 2's blocker 1 was a criterion a correct implementation fails, carries a criterion a correct implementation fails. `TOOL-dRetiredFork-21` specifies a `{prefix}` token in two fragment bodies that the engine reading those files performs no substitution on, so either branch of the literal reading breaks the unit. Promotion moved the defects into new documents and the new documents were not graded.

On the three priors, measured rather than asserted:

**Shape 1, instance-not-class, SURVIVED in four places.** `TOOL-dRetiredFork-13` §1 and S1 still say "32 shipped test and selftest files" while AC0, added by this same fold, records that the ratchet holds 33 rows summing to 259 — the spec contradicts itself, and I counted `tools/install-prefix-carried.txt` to settle it at exactly 33 rows, 259 occurrences. `DEPL-dRetiredFork-8` S3 names four "nine" sites in `DEPL-dRetiredFork-6` where the file holds six. `TOOL-dRetiredFork-14` §6 still runs AC7 before AC6, the byte-identical sibling of the label defect the fold fixed in `DEPL-dRetiredFork-3`. And the three new checkers land tracked files under `tools/govkit/registry.toml`'s quantified surface with no unit declaring them, which is the class `TOOL-dRetiredFork-3` S6 fixed one round earlier at its own instance. The fold scripts asserted the refuted string was gone from the whole file; the assertion is doing less than it claims, because in each of these cases the refuted claim is a paraphrase rather than a literal, and a string equality test cannot see it.

**Shape 2, prepend-instead-of-substitute, is GONE — with one residue.** No truncated sentence, no dangling em dash, no double claim from a patch-in-place anywhere in the set. The single survivor is a missed anchor and reports as one: `DEPL-dRetiredFork-3` §3 line 57 is the old closing line of the `generated` non-goal whose lines 53-56 were rewritten, and it still reads "running the target's own tooling is the adopter's", which is what S2 and AC2 were folded to deny.

**Shape 3, one-side-of-a-move, SURVIVED once, loudly.** Of the three moves I was asked to check both sides of, two reconciled cleanly: `TOOL-dRetiredFork-8` S6 and `TOOL-dRetiredFork-13` §3 agree about the check-wiring sweep, and `TOOL-dRetiredFork-14` F0 and `TOOL-dRetiredFork-21` F1 ask the same question without contradicting each other. The third did not. `DEPL-dRetiredFork-7` S6 was rewritten to RECORD the misfiled registry row and hand the reclassification to inCMS, with §3 forbidding the edit and AC7 asserting against it — while the build README still reads "Reclassifying that registry row is `DEPL-dRetiredFork-7`". DEPL-7's own rev-3 log names the unreconciled side in writing and does not fix it.

Two honest notes on the numbers. Precision fell from 0.84 to 0.62, which is the expected direction for a narrow re-audit of already-folded text: the seams are fewer and the lenses spend more of their budget on speculation. And **every mechanical check handed to this round came back clean and I found counter-evidence to one of them.** The "specs with unresolved forks 0" sweep passes because it greps each file for a RESOLVED token; `DEPL-dRetiredFork-2` satisfies it on F2's inline agent-level mark while F1 carries only a Recommendation and no resolution at all, under a header advertising `ratified 2026-09-02`. I cross-tabbed all 30 specs for the three-way join of §8-presence, blanket mark and header pointer: DEPL-2 is the unique spec with a fork section and no blanket mark, and `TOOL-dRetiredFork-5` is the unique spec carrying the pointer with no §8 behind it. Both are anomalies of the ratification sweep itself, not of the specs it stamped.

## Severity table

| # | Severity | Subject | Address | Defect |
|---|---|---|---|---|
| 1 | blocker | DEPL-8 | §6 AC1 | `grep -c` cannot express "outside the generated records region"; the command returns 2 after a correct S1 and never `0` |
| 2 | blocker | TOOL-21 | §4 Inventory, §2 S1 | The "after" column writes `{prefix}` into fragment bodies; `settings-merge.py` substitutes nothing and refuses to wire a path that does not resolve |
| 3 | blocker | DEPL-9 / DEPL-3 | DEPL-9 §8 F1 (ratified) vs DEPL-3 §6 AC10 | Two ratified answers to one question, written in one commit: inCMS is escaped by `--allow-ungraded` and is deferred out of the done-condition |
| 4 | high | README / DEPL-7 | README Parked decisions line 79 vs DEPL-7 §2 S6, §3, §6 AC7 | One side of a move reconciled; the README promises a reclassification the spec forbids |
| 5 | high | DEPL-2 | §8 F1 and the status header tail | The only fork-carrying spec with no blanket mark, and its header claims `ratified` anyway; counter-evidence to the clean sweep |
| 6 | high | DEPL-1, TOOL-16 | §8 F1 in each, against the blanket mark below | The mark settles "by its own stated Recommendation" two forks that state none — both declared `FACT-QUESTION`, both undecided until a probe runs |
| 7 | high | DEPL-3 | §6 AC10 vs §3 | "and §3 says so" is a false internal citation; §3's three non-goals never mention inCMS, its receipt, or any deferral |
| 8 | high | DEPL-3 | §3 line 57 vs §2 S2, §6 AC2 | The missed anchor: the refuted closing line of the `generated` non-goal survives the rewrite above it |
| 9 | high | TOOL-13 | §1 line 19, §2 S1 line 25, vs §6 AC0 line 53 | The spec asserts 32 files in the two places a builder works from and 33 in the criterion that measures it |
| 10 | high | TOOL-13 / TOOL-17 | TOOL-13 §3 third non-goal vs §2 S1 | The narrowing changed the wording, not the ownership; 41 carried-prefix occurrences in six checkers reach TOOL-17's ban undrained |
| 11 | high | DEPL-8 | §2 S3 vs §6 AC2 | S3 lists four "nine" sites; DEPL-6 holds six, and AC2 greps the whole file |
| 12 | high | TOOL-19, TOOL-20, TOOL-21 | §2 (no registry item) vs §7 | Three new tracked checkers land unclaimed under govkit's quantified surface, so a named gate reds on landing |
| 13 | high | TOOL-19 | §4 Data model, §2 S3 | The join assumes every placeholder-declaring kit ships an adopter; `tools/workflows` declares one and has `argv = []` |
| 14 | high | DEPL-3 | §2 S1, §4 Data model | The mechanism re-runs `[adopt].argv`, which cannot reach the one rendered row whose entry has no adopter |
| 15 | high | TOOL-3 | §4 Migration, §5, §6 AC4 | A missing-registry REFUSAL in `collect()` reds every `cmd_selftest` fixture tree, which no S-item teaches to write the registry |
| 16 | high | TOOL-20 | §4 Data model, §6 AC3 | The `path:line` join has no defined verdict for an unresolvable path — half the corpus, measured |
| 17 | medium | DEPL-9 | §6 AC4 | A non-recursive grep against a directory: prints "Is a directory", exits 2, reads no file |
| 18 | medium | TOOL-12 | §2 S1 | The fold's corrected count is wrong by one: eight tokens are substituted, not seven |
| 19 | medium | TOOL-12 | §2 S1, §4 Migration | The row is retagged `rendered` with no `to`; every other rendered row in the corpus writes outside its kit home |
| 20 | medium | DEPL-8 | §2 S4 | Re-rendering the roster sentence to "eight" contradicts the generated build-order table, which shows nine order-1 units |
| 21 | medium | TOOL-19 | §6 AC1 | `grep -c` is asked to report where its hits are and what they say |
| 22 | medium | TOOL-5 | §2 S3 | The one runtime-behaviour change in the unit is conditional and observed by nothing |
| 23 | medium | DEPL-8 | §2 S2, S3 second clause | Two additions to DEPL-6 that every criterion permits to be omitted |
| 24 | medium | DEPL-9 | §2 S4 | The unit's entire left-shift — a README Build-level rule — has no criterion |
| 25 | low | TOOL-5 | status header tail | `ratified 2026-09-02` on a Tier-1 spec that has no §8 and never had one; the unique outlier of the sweep |
| 26 | low | TOOL-14 | §6 label sequence | AC7 sits between AC5 and AC6 — the sibling of the DEPL-3 defect the fold fixed |
| 27 | low | DEPL-1 | §2 label sequence | S3b sits between S4 and S5, away from the item it extends |
| 28 | low | DEPL-1 | §2 S6 | "the 25-unit set" in live scope prose; the roster has held 30 since `5998eb03` |
| 29 | low | TOOL-20 | §2 S1 second clause | The unit whose subject is unverified fold bookkeeping leaves its own bookkeeping correction unobserved |

---

## Blockers

### 1 — `DEPL-dRetiredFork-8` AC1 is a criterion a correct implementation fails

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-8.md` §6 AC1 (lines 46-47).

**The defect.** AC1 pins `grep -c 'TOOL-dRetiredFork-4' memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-6.md` and requires it to return `0` "outside the generated records region". Two things are wrong and they compound.

Measured: that command returns **3** today. Line 106 is the authored prose S1 strikes. Lines 9 and 10 are the two "Also serves" rows inside DEPL-6's `gen:spec-records` region, which are re-rendered from the round-1 and round-2 review records' own Serves lines. So after a correct implementation of S1 the pinned command returns **2, forever.**

And `grep -c` emits a bare integer per file. It cannot express the qualifier AC1 attaches to it — there is no way for that command to exclude a region, and no way to read its output as anything but a whole-file count. The criterion therefore cannot be discharged by the observation it names, in either direction.

**This is round 2's blocker 1 shape reproduced inside the unit promoted to fix it.** `DEPL-dRetiredFork-8` exists because `DEPL-dRetiredFork-6` AC2 was a criterion a correct verb reds. The promotion carried the defect into the new document rather than leaving it behind. Worse than round 2's version: the surviving hits sit in a GENERATED region whose contents move as new records serve this build, so the criterion is not even stably wrong — its true value changes without anyone editing the file.

**Fix.** Rewrite AC1 to a command that can express the exclusion and state the expectation against authored text, not against the file. For example `sed '/<!-- gen:spec-records -->/,/<!-- \/gen:spec-records -->/d' <file> | grep -c 'TOOL-dRetiredFork-4'` returning `0`, or a `grep -n` whose expected result is stated as "no hit outside lines 9-10". Say explicitly that the generated rows are out of the criterion's reach and why.

**Left-shift gate.** The mechanical arm worth wiring, and it generalises past this build: when a §6 criterion pins a shell command AND states a qualifier the command's own output shape cannot carry, red it. The cheap approximation that catches this exact class today is narrower and still worth having — red any acceptance criterion pinning `grep -c` together with a locational or contextual qualifier (`outside`, `only in`, `never in`, `in both`), because a bare count answers none of those. That single predicate catches this blocker, finding 17 and finding 21 in one pass.

### 2 — `TOOL-dRetiredFork-21` specifies a token the engine that reads those files never substitutes

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-21.md` §4 Inventory (the "after" column, rows 1 and 2), against §2 S1.

**The defect.** The Inventory table's "after" column writes `{prefix}/hooks/scratch-guard.js` into `tools/hooks/scratch-guard.fragment.json:6` and `{prefix}/memory-recall/recall-opened.js` into `tools/memory-recall/recall-opened.fragment.json:6`. Every mechanic in that path was re-derived at HEAD and none of it performs a substitution.

`tools/settings-merge.py:83` — `load_fragment` returns `{k: frag[k] for k in _FRAGMENT_KEYS}`, the raw JSON values. `:86-88` — `_command()` interpolates the value verbatim into `node "${CLAUDE_PROJECT_DIR}/{hook_path}"`. `:286` — `hook_path = a.hook_path or frag["hook_path"]`, with no transformation anywhere between the read and the write. `:291` — the script **refuses to wire** when `Path(hook_path).exists()` is false, printing that wiring a missing script "makes every matching tool call run `node` against nothing".

`{prefix}` is a govkit DESTINATION token. It is resolved in `to = ` fields when placing files; it is never applied to file CONTENT, and `tools/hooks/kit.toml:53-56` ships `scratch-guard.fragment.json` as `role = "engine"`, which is copied byte-for-byte.

**Either reading of the Inventory breaks the unit.** Written literally, `{prefix}` never resolves, `Path("{prefix}/hooks/scratch-guard.js").exists()` is false, and settings-merge refuses to wire both hooks — the silent unwiring `TOOL-dRetiredFork-14` §5 calls this build's highest risk, caused by the unit written to prevent it. Written resolved to gov's own prefix, an `engine` file carrying the literal `tools/` ships to every adopter, and it lands in the population `tools/check-install-prefix.sh` already scans at `:54` via its `*.fragment.json` glob — so the unit that drains carried prefixes adds two.

**Fix.** §4 must state who resolves the prefix inside a fragment BODY, which is a thing nothing does today. Either move the fragment to `role = "rendered"` with a declared placeholder and name the substituter, or scope fragment-side token resolution into `settings-merge.py` as its own S-item with its own criterion. Then add two criteria: `python tools/settings-merge.py --fragment tools/hooks/scratch-guard.fragment.json` still wires successfully after the repath, and the fragment's row in `tools/install-prefix-carried.txt` does not rise.

**Left-shift gate.** Extend the check `TOOL-dRetiredFork-19` is already building rather than adding a second one: for every file a descriptor ships with `role = "engine"`, red on any `{…}`-shaped destination token found in its CONTENT, since an engine file is copied verbatim and such a token can only survive into the adopter's tree unresolved. That arm is cheap, has an obvious failing case to stage, and would have refused this spec's Inventory before it was written.

### 3 — the blanket ratification settled two contradictory picks, in one commit

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-9.md` §8 F1 and its ratified Recommendation, against `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-3.md` §6 AC10 (lines 123-129). Both stamped by the same blanket mark, both written by `8b307f06`.

**The defect.** This is the question the round was pointed at, and it fails.

`DEPL-dRetiredFork-9` F1 asks whether the done-condition requires `unattributed` to reach zero or is observed with `--allow-ungraded`. Its Recommendation, now ratified: **"zero at NicoCares, `--allow-ungraded` at inCMS until its receipt is repaired, both stated in AC10."** S1 reinforces it — write the decision into DEPL-3 AC10 in its own text — and S5 requires wholesale rewrites.

`DEPL-dRetiredFork-3` AC10, rewritten by the same commit for round 2's finding 6, reads: **"inCMS's half of the done-condition is DEFERRED"**, because "no unit in this roster repairs that receipt, so a criterion gated on the repair would be permanently neither green nor red — worse than a missing one, because it looks covered."

These are two different resolutions of one problem. `--allow-ungraded` keeps inCMS inside the done-condition behind an escape; deferral removes inCMS from the done-condition entirely. The blanket mark ratified the first while the fold text implemented the second, four files apart, in one commit, and nobody read them against each other — which is precisely the risk a blanket ratification carries and precisely why this check was commissioned.

The ordering makes it worse rather than academic. `DEPL-dRetiredFork-9` is order 0 and `DEPL-dRetiredFork-3` is order 7. The order-0 builder is instructed by S1 and AC1 to write the ratified inCMS clause into a criterion belonging to a spec they do not own, reversing a rev-4 fold. Following the ratified pick reinstates the permanently-neither-green-nor-red criterion round 2 blocked on — and the reinstated clause is repair-gated with no owning unit, which is the exact shape round 2's own proposed left-shift gate was written to red. Following DEPL-3 leaves DEPL-9's AC1 and AC2 unsatisfiable. Whichever builder runs first silently decides what the build's headline verdict means.

BUILD-METHOD's M2 forbids a disagreement surviving in two documents past the first code pass. This one was created in the fold and ratified in the same breath.

**Fix.** Reconcile in exactly one document, and say in both which one moved. Either re-open AC10's inCMS half naming `--allow-ungraded` explicitly and delete the "neither green nor red" deferral sentence, or amend DEPL-9 F1's pick to "zero at NicoCares; inCMS deferred per `DEPL-dRetiredFork-3` AC10". The second reverses a ratified pick, so by the blanket mark's own closing clause it must be minted as a new fork with a new id rather than edited in place.

**Left-shift gate.** The gate this build needs and does not have: a blanket ratification is not landable until every Recommendation under it has been read against every sibling spec's ratified picks and against the README's Build-level rules and Parked decisions. Mechanically, the tractable half is a join — extract each `**F<n>` bullet's Recommendation text, extract every acceptance criterion it names by label, and red when two specs' ratified recommendations name the same criterion label in the same sibling spec. The full check is a documented manual one and belongs in BUILD-METHOD beside the existing done-condition rule: **a fork whose Recommendation instructs an edit to another spec's numbered criterion is read against that criterion's current text before ratification, not after.**

---

## High

### 4 — the README still promises a reclassification `DEPL-dRetiredFork-7` is forbidden to perform

**Address.** `memory/builds/dRetiredFork/README.md` Parked decisions, third bullet (line 79), against `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-7.md` §2 S6 (lines 48-50), §3, and §6 AC7.

**The defect.** Verified on both sides. The README reads "Reclassifying that registry row is `DEPL-dRetiredFork-7`; rewriting either program is not in scope." DEPL-7 S6 now reads "RECORD inCMS's `gen_build_index.py` row as contract-adopted in the census output, and … hand the reclassification to that adopter as a named recommendation. rev-1 said 'Reclassify', which §3 forbids and AC7 asserts against." §3 forbids editing either adopter's tree; AC7 states that neither register is edited by this unit.

This is prior shape 3, and it is the only one of the three checked moves that failed. What makes it a high rather than a low is that **DEPL-7's own rev-3 log names the unreconciled side and leaves it standing**: it records that "the unit could pass its DoD with the row untouched while the README believed it reclassified" — the fold diagnosed both halves, repaired one, and wrote the other down as a known survivor. The build can now close with the README's parked decision undischarged and no document able to say which is right.

**Fix.** Rewrite the parked bullet wholesale, per S5's own no-prepend rule: `DEPL-dRetiredFork-7` RECORDS the row's class in its census output and hands inCMS a named recommendation (AC4b); the reclassification itself is inCMS's edit in inCMS's own `kits.json` and is not this build's. Add that README edit as an S-item of DEPL-7 so the two sides land in one commit rather than depending on a second reader noticing.

**Left-shift gate.** A join the build README already supports: extract every `<ID>` mentioned in the README's Parked decisions and Build-level rules together with the verb attached to it, and red when that verb appears in the named spec's §3 non-goals. Cheaper and more general as a documented check in BUILD-METHOD: **when a fold changes what a unit DOES, the README's claims about that unit are part of the same edit** — which is the rule this fold broke while writing the sentence that describes it.

### 5 — `DEPL-dRetiredFork-2` advertises a ratification it does not carry

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-2.md` §8 F1 and the status header tail.

**The defect.** I cross-tabbed all 30 specs on §8-presence, blanket-mark presence and header pointer. DEPL-2 is the **unique** file with a fork section, a `ratified 2026-09-02` header pointer, and no blanket `RESOLVED (owner, 2026-09-02)` mark. F1 — which `evidence` value a newly landed row carries — has a bare `Recommendation: vintage-match` and no resolution of any kind. F2 carries a separate inline `RESOLVED (agent, 2026-09-02, delegated)`.

**This is counter-evidence to the "specs with unresolved forks 0" sweep I was handed as clean.** The sweep is satisfied by F2's token. `memory/TEMPLATE-SPEC.md:118-123` requires the mark IN PLACE per fork with the header pointer added beside it, and the hygiene gate grades §8 as one whitespace-squeezed string — so a conforming mark anywhere in the section makes the whole section read resolved, and F1 is machine-invisible. The fold commit's message asserts "Zero unresolved forks remain"; the first half of that claim is false here.

It matters beyond bookkeeping. S4 explicitly defers the new row's `evidence` value to §8 — "The choice is a fork in §8" — and no criterion AC1-AC7 observes that value at all. So a scope item depends on an unratified fork, on a contract question (whether the closed `EVIDENCE_STATES` set, joined to the engine by its own arm, gains a member), while the header tells every reader the forks are settled.

**Fix.** Add the same blanket mark the other fork-carrying specs got, or mark F1 individually as `RESOLVED (owner, 2026-09-02): vintage-match`. Then add a criterion observing that a newly landed row carries the chosen value and that `EVIDENCE_STATES`' engine arm still passes — the fork can be settled and the scope item still unobserved, and both are needed.

**Left-shift gate.** Replace the token-presence sweep with a join: parse each `**F<n>` bullet in §8 and require a resolution mark reachable from THAT bullet — inline, or a blanket mark whose text is the section's last non-blank line — rather than grepping the file for one RESOLVED string. Red a `ratified` header pointer on a spec where any `F<n>` fails that join. This is the sweep that would have caught both this finding and finding 25 in the same pass, and its failing case is trivially stageable.

### 6 — the blanket mark settles two forks that state no Recommendation

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-1.md` §8 F1, and the byte-identical case at `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-16.md` §8 F1, each against the blanket mark below it.

**The defect.** The mark asserts: "every fork above is settled by its own stated Recommendation … No fork is resolved against its recommendation and none by silence."

DEPL-1 F1 reads "UNRESOLVED, and it is the unit's central fact. This is a `FACT-QUESTION` decided by S4's read-only run" and states no Recommendation. TOOL-16 F1 reads "UNRESOLVED until run; the unit's shape depends on the answer" and states no Recommendation. The mark's universal quantifier is literally false of both, and it settles them by exactly the silence it disclaims.

A measurement is not ratifiable. `memory/guides/BUILD-METHOD.md:93-95` says a FACT-QUESTION is decided by its stated PROBE — take the winner only when it falls out of the observation — so an owner ratification of a recommendation that does not exist resolves nothing. But TEMPLATE-SPEC grades §8 as one squeezed string, so the conforming mark makes both sections read resolved to the hygiene gate and to the planning verb, and both headers now carry `ratified 2026-09-02`. Nothing will flag either again.

The cost is specific in both files. DEPL-1 F1's own text says a ZERO answer collapses that unit's value onto `DEPL-dRetiredFork-7` and that the owner should see it before the unit is built — the mark removes the FORKED classification that would have surfaced it. TOOL-16's §5 risks row says that if the probe inverts, "this unit's premise is false and the unit becomes a defect report instead"; a ratification over that question tells the next session the shape is decided, which is the one thing S3 exists to prevent.

**Fix.** Carve fact-questions out of the mark's wording in both files — "every fork above CARRYING A RECOMMENDATION is settled by it; items stating none remain open until their named probe runs" — or give each bullet an inline `FACT-QUESTION · OPEN until <probe> runs; the blanket mark below does not reach this item`. Drop `ratified` from both headers until the probes run, or state in the header that the pointer covers the recommendation-bearing forks only.

**Left-shift gate.** Same join as finding 5, with one added arm: a fork bullet carrying the literal `FACT-QUESTION` is not satisfiable by a blanket mark at all, only by a recorded probe result in §9. That arm is the machine form of BUILD-METHOD's own rule and it has a clean failing case — stage a blanket mark over a FACT-QUESTION and watch it red.

### 7 — `DEPL-dRetiredFork-3` AC10 cites a section that says nothing of the kind

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-3.md` §6 AC10 (lines 127-129) against §3 (lines 53-57).

**The defect.** AC10 asserts "**inCMS's half of the done-condition is DEFERRED, and §3 says so**". §3 was read in full. It carries exactly three non-goals: running an adopter for a deliberately INERT kit, the `merged` role, and writing a `generated` file's BYTES. None of them mentions inCMS, its receipt, or any deferral.

Round 2's prescribed fix for its finding 6 was two-part — strike the inCMS sentence from AC10 **and** state in §3 that inCMS's half is deferred. The fold did the first half and then cited the section it never edited. That is a new false internal citation created by this fold, in the single criterion the set labels THE BUILD'S DONE-CONDITION, and it is the same class round 2 caught twice in round 1's fold.

The consequence is not cosmetic. §3 is the section a builder reads to learn what is out of scope, and it is authoritative. The deferral currently has one carrier while claiming two, so a later session can re-scope inCMS back in without contradicting any written non-goal — which is how AC10's inCMS half became ungradeable in the first place. It also interacts with blocker 3: if the deferral survives that reconciliation, this is the sentence that has to carry it.

**Fix.** Add the fourth non-goal to §3 in its own sentence — repairing inCMS's receipt is out of scope for this roster, because no unit in it performs that repair and a criterion gated on the repair could never discharge — and leave AC10's pointer pointing at real text. Or drop "and §3 says so" and let AC10 carry the deferral and its reason alone. The first is better; the reason belongs where the cut-line is defined.

**Left-shift gate.** A spec lint with an easy failing case: extract every intra-document section reference (`§<n>`, `AC<n>`, `S<n>`) from a criterion and red when the named section contains none of the criterion's distinguishing terms. Applied here, AC10 names §3 while §3 contains neither "inCMS" nor "defer", and the arm fires. Cheap, and it generalises to every "as §N says" claim in the corpus.

### 8 — the missed anchor: `DEPL-dRetiredFork-3` §3 line 57

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-3.md` §3 line 57, against §2 S2 and §6 AC2.

**The defect.** The rev-4 fold of round 2's finding 12 rewrote lines 53-56 of the `generated` non-goal, establishing that the bullet "disclaims AUTHORSHIP and not INVOCATION" and that a `[[regenerate]]` argv declared by a gov descriptor IS run by this verb. It left the bullet's old closing line standing. Line 57 still reads:

> The report NAMES which generators are owed; running the target's own tooling is the adopter's.

That is the exact claim lines 53-56 were written to refute, and it is what S2 ("are performed rather than described in a runbook") and AC2 ("the run performs it") contradict outright — S2's own examples of what `update` now performs are the target's `gen_map.py --write` and `gen_build_index.py --write`.

This is the single survivor of prior shape 2, and it reports as the brief specified: a missed anchor, not a prepend. Every edit this round substituted; this one substituted three lines of a four-line bullet. I have adjudicated it down from the blocker severity it arrived with, because lines 53-56 pre-empt the misreading for anyone who reads the bullet in order. It stays high because the sentence is false as written and sits in the section that defines the cut-line, and because a reader who stops at the last line of a non-goal — which is a normal way to read a non-goal — implements report-only regeneration, the status quo this unit exists to end.

**Fix.** Delete line 57. The disclaimer the bullet needs is already above it. If a report-only case genuinely survives for generators that no `[[regenerate]]` block declares, say so in one rewritten sentence naming that case, rather than as an unqualified restatement of the refuted claim.

**Left-shift gate.** The class is "a fold rewrote a paragraph and left one sentence of it". The mechanical form worth having: when a fold commit edits a bullet, red the commit if any line of that bullet is untouched AND contains a phrase the commit message names as refuted. Where that is too deep, the documented check is the one this build keeps re-learning and should now write into BUILD-METHOD — **a substitution is over the whole bullet, not the sentences that matched the finding's quote.**

### 9 — `TOOL-dRetiredFork-13` states 32 where its own criterion states 33

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-13.md` §1 (line 19) and §2 S1 (line 25), against §6 AC0 (line 53).

**The defect.** §1 says "the other 32 shipped test and selftest files, which carry 259 of the ratchet's 656 recorded occurrences". S1 says "across the 32 remaining shipped test and selftest files". AC0, added by this fold, says "the ratchet holds 33 test rows summing to 259, and rev-1 said 32 carrying 259, which cannot both be right."

I counted `tools/install-prefix-carried.txt` directly: **33 rows whose path matches test or selftest, summing to exactly 259 occurrences.** AC0 is right and the two sections a builder implements from are wrong.

Round 2's finding 15 stated the mechanism precisely — S1 iterates the file count, so a builder enumerating 32 leaves one suite unswept. The fold answered by adding a criterion at a new address instead of substituting the refuted string where the work is specified. That is prior shape 1, and it is the identical argument `TOOL-dRetiredFork-19` was promoted to make about §4 versus §2 in a different spec. AC0 forcing a re-derivation mitigates the practical risk; it does not remove a refuted figure from the goal statement, and the miss stays invisible until TOOL-17's ban reds at order 9.

**Fix.** Rewrite §1 and S1 wholesale to 33 files and 259 occurrences, naming the `.githooks/pre-push.test.sh` ownership question there rather than only in AC0. Keep AC0 as the re-derivation check, not as the sole carrier of the true figure.

**Left-shift gate.** The charter's own no-derived-counts-in-prose rule, made mechanical for specs: red a bare cardinal in §1 or §2 that describes a population a tracked registry owns, when the registry's live count differs. `tools/install-prefix-carried.txt` is machine-readable and the join is a one-liner. The stronger and more general arm: red any spec where §6 contains a criterion asserting that a figure stated elsewhere in the same spec is wrong — a document that grades itself as incorrect should not be landable.

### 10 — the check-wiring narrowing changed the wording, not the ownership

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-13.md` §3 third non-goal, against §2 S1, and forward against `TOOL-dRetiredFork-17` §4.

**The defect.** This is one side of a move that reconciled and one that did not, in the same finding. The rev-3 fold narrowed §3's disclaimer from the whole non-test checker class to "`tools/check-wiring.sh` SPECIFICALLY, and no wider class", and `TOOL-dRetiredFork-8` S6 correctly owns that file — that half is clean, and I verified it as instructed. But S1's population is still "the 32 remaining shipped test and selftest files", so the six non-test checkers the narrowing stopped disclaiming are now claimed by nobody.

Measured from the ratchet: `check-agent-cap-restatement.sh` 2, `check-install-prefix.sh` 6, `check-kit-versions.sh` 30, `check-line-length.sh` 1, `check-microformats.sh` 1, `settings-merge.py` 1 — **exactly the 41 occurrences round 2 named.** I grepped the whole spec set: no unit scopes them. TOOL-8 S6/AC6 owns `check-wiring.sh`, TOOL-11 owns pre-push, and nothing owns these six.

A builder also cannot tell whether they are in scope: §3 now excludes only one named file, which by implication puts the others IN, while S1's population excludes them. The contradiction is internal to TOOL-13.

The forward cost is the part that bites. `TOOL-dRetiredFork-17` §4 states its population is "whatever survives units 10 through 13", and its F2 is ratified as seeding the exception list from ZERO. So the order-9 ban meets 41 undrained occurrences and lands permanently red, or is unblocked by exceptions written under deadline pressure — which §4 names as the state it must not land in.

**Fix.** Pick an owner and say so by id. Either widen S1's population to name those six files and re-derive the count the way AC0 already does, or add a scope item in `TOOL-dRetiredFork-17` that dispositions them before the ban. Then say in §3 which unit owns them — a disclaimer with no matching owner is what round 2 flagged and what the narrowing preserved.

**Left-shift gate.** A coverage join over the build's own scope statements: union every path or path-population named in any spec's §2, subtract it from `tools/install-prefix-carried.txt`, and red when a unit's §3 disclaims a path that the union does not cover. That gate makes an orphaned population impossible to create by narrowing a non-goal, which is exactly how this one was created.

### 11 — `DEPL-dRetiredFork-8` S3 names four sites where the file holds six

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-8.md` §2 S3, against §6 AC2.

**The defect.** S3 orders "nine" to become "eight" at `DEPL-dRetiredFork-6` §1, §4 Rollout (both sites) and §5. Counted in that file, "nine" appears at lines 16 (§1), 67 and 68 (§4 Rollout), **75 (§4 Alternatives rejected — "it did not happen for any of the nine")**, 92 (§5), and **139 (§9 rev-1 — "the nine hand-found absorptions")**. Both survivors describe the absorption count. AC2 grades the whole file.

So a builder who executes S3 exactly fails AC2 — the instance-not-class miss inside the scope statement of the unit promoted to correct that class. The secondary point that satisfying AC2 requires editing a landed revision-log entry is weaker than it looks, since `TOOL-dRetiredFork-20` S1 itself proposes editing a rev-log line, but it does mean scope and criterion currently grade different populations and neither says which is right.

**Fix.** Rewrite S3 to name §4 Alternatives rejected as a fifth site, and rewrite AC2 to state its population explicitly — either excluding §9 because the revision log records what rev-1 said and is not corrected, or including it and saying so. Scope and criterion must grade the same lines.

**Left-shift gate.** When a §2 item enumerates addresses for a string substitution and a §6 criterion greps for that string file-wide, red unless the criterion's population is stated. The general form is a documented check: **an enumerating scope item and a scanning criterion are a mismatch by construction** — either the scope scans or the criterion enumerates.

### 12 — the three new checkers land unclaimed under govkit's quantified surface

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-19.md` §2 (no registry item) against §7, and identically in `TOOL-dRetiredFork-20` and `TOOL-dRetiredFork-21`.

**The defect.** Verified against the engine rather than the prose. `surface_paths` in `tools/govkit/govkit.py:132-155` expands `tools/*` to depth-1, so a new `tools/check-*.sh` plus its `.test.sh` are unclaimed surface paths the moment they are tracked. `tools/govkit/entries/check-placeholders.kit.toml` says this about itself in its own header — "Both of this gate's files are therefore unclaimed surface paths the moment they are tracked, and each unclaimed one is its own selfcheck failure". Independently, `govkit.py:1601-1602` fails any `tools/gate-legs.json` leg "claimed by no descriptor and carried by no `[[exempt_leg]]`", and TOOL-19 S6 adds exactly such a leg.

All three units name `govkit selfcheck` in §7. None carries a §2 item or a §6 criterion declaring its new files in `tools/govkit/registry.toml` or in a kit descriptor. So a gate each spec names as its own reds on landing, for a reason the spec never anticipates.

`TOOL-dRetiredFork-3` rev-2 fixed this exact class at its own instance for check 3's whitelist, and its H7 record settles the principle explicitly — "this is a required scope item and not an inference". The fold created three new units under the same surface and carried none of it across.

**Fix.** Add to each of the three units a scope item declaring its new files in `tools/govkit/registry.toml` — an entry `[[files]]` rule, or an `[[exempt]]` row with a non-empty reason — in the same commit that lands the checker, plus a criterion that `python tools/govkit/govkit.py selfcheck` exits 0 afterwards. TOOL-19 additionally needs its new gate leg claimed by a descriptor or carried by an `[[exempt_leg]]`.

**Left-shift gate.** This one is already half-built and should be finished: a spec lint that extracts every path a §2 item says the unit CREATES, resolves it against `surface_paths`, and reds when the spec contains no registry or descriptor declaration for it. The failing case is stageable in one line — add a `tools/check-foo.sh` to a spec's scope and watch it red — and it closes the class for every future unit that ships a checker, which is the form `TOOL-dRetiredFork-3` H7 asked for and did not get.

### 13 — `TOOL-dRetiredFork-19`'s join has no left-hand side for one of its six kits

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-19.md` §4 Data model and §2 S3.

**The defect.** The join is "declared ⊆ substituted by that kit's own adopter script". Measured: six kits declare `placeholders` — drift-audit, lexicon, memory-recall, memory-tree, unattended, workflows. `tools/workflows/kit.toml:18` declares `placeholders = ["TOOL_ROOT"]` on a `role = "rendered"` row, and its `[adopt]` block at `:20-23` is `argv = []` with `why_no_adopter = "the harness is copied and its protocol rendered; the render is performed by the parity gate's own --render mode rather than by a separate adopter"` — free prose, not a machine pointer. The render is performed by `check-protocol-parity.test.sh --render`.

So for one of the six declaring kits there is no right-hand side to join against. The gate either REDS `workflows` for a declaration that is correct, blocking every contributor on day one, or silently skips the kit — the could-not-fail shape §5's error-states row exists to prevent but does not cover, since that row enumerates only "a kit declaring NO placeholders" and "an EMPTY population". §4 Migration names gov's own tree as the first subject, so the undefined case fires immediately and the builder invents the verdict.

**Fix.** §4 Data model must say how the substituter is located — the `[adopt] argv` field, not a filename convention — and what the gate does for an entry declaring `placeholders` with no adopter: REFUSE and name the entry, or resolve the declared renderer instead. Add a criterion for that third state, and name `workflows` in S5's pre-wiring run as the known instance so the builder meets it before the gate is armed.

**Left-shift gate.** The unit's own §5 error-states row is the gate; it just needs the third state in it. The general rule, which this build has now hit twice: **every state enumerated in a §5 error-states row is a criterion in §6, and a state discovered during the pre-wiring run is added to both.** A checker whose §5 enumerates two states and whose real domain has three is a checker that cannot fail on the third.

### 14 — `DEPL-dRetiredFork-3`'s mechanism cannot reach one of the rendered rows it must re-render

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-3.md` §2 S1 and §4 Data model.

**The defect.** Same underlying fact as finding 13, biting a different unit at a different address, which is why both are listed. S1 re-runs "the `[adopt].argv` of every entry whose landed set invalidated a rendered destination" — assuming every entry with a rendered row has an adopter. `tools/workflows/kit.toml` is the single entry with a `role = "rendered"` row and `[adopt] argv = []`.

In NicoCares' own receipt, `review-harness memory/guides/REVIEW-PROTOCOL.md` is a rendered row. So one of the two binding protocols §1 counts among that adopter's eight stale rendered destinations is unreachable by this unit's mechanism: it stays a vintage stale after the unit lands, and that adopter's byte-compare CI job keeps redding — the exact defect the unit exists to close. AC10 requires the run to "re-render every rendered row"; AC1 requires it to "name the adopter it ran", which for this entry does not exist. §3's three non-goals cover inert kits, the `merged` role and `generated` bytes, and none covers an entry with no adopter, so the gap surfaces as a passing criterion over an entry the run never touched.

**Fix.** §4 must say what `update` does for a rendered row whose entry declares no adopter — invoke a declared renderer argv as a second `[[regenerate]]`-shaped field, or REFUSE and name the entry in the report — and S6 gains an arm for it. Add a criterion observing `REVIEW-PROTOCOL.md` specifically, since it is the measured instance rather than a hypothetical.

**Left-shift gate.** A descriptor-level invariant, checkable today and independent of both specs: red any `kit.toml` carrying a `role = "rendered"` row whose `[adopt] argv` is empty and whose renderer is not named in a machine-readable field. That turns `why_no_adopter`'s free prose into a pointer and makes the entire class — findings 13 and 14 together — impossible to declare rather than merely documented.

### 15 — `TOOL-dRetiredFork-3`'s refusal reds the selftest fixtures

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-3.md` §4 Migration, §5 error/empty states, and §6 AC4.

**The defect.** AC4 requires `gen_build_index.py --check` to REFUSE when `memory/project/stale-header-waiver.txt` is absent, and S3 puts the consult in `collect()`. Verified: `plan()` calls `collect()` at `gen_build_index.py:1511`, and `cmd_selftest` builds its fixture trees under `tempfile.TemporaryDirectory()` at `:1852` via `_fixture()`, which writes `.memory-tree.conf`, `memory/builds/…` and `memory/ledger/…` and **never creates `memory/project/`**. A grep of the whole program for `memory/project` returns nothing.

So every selftest arm gets the refusal instead of its expected string, and the `build-index selftest` leg — named in §7 — reds on landing. No S-item teaches the fixtures to write the registry. §4 calls the mechanism "inert on the day it lands"; a missing-file refusal is the opposite of inert, and AC1's "before the change the same tree exited 0" and AC5's "differs by EXACTLY the `0 tolerated` line" both assume the selftest still passes.

§10 cites `legacy-files.txt` read into `LEGACY_SET` as the precedent. That model does the opposite of what this unit builds: `check-memory-hygiene.sh:127` reads it with `2>/dev/null || true` — tolerant of absence. The cited precedent argues against the design it is cited to support.

**Fix.** Add an S-item covering the selftest fixture builder, and state in §4 which callers of `collect()` are in the refusal's scope — the real tree, not every fixture. Correct §10 to say the copied `LEGACY_SET` shape TOLERATES an absent registry and that this unit deliberately diverges and why, or drop the refusal for the fixture path.

**Left-shift gate.** Narrow and mechanical: when a spec adds a REFUSAL to a function, resolve that function's callers and red when any caller is a test-fixture builder with no scope item teaching it the new precondition. The broader documented check, which this build has now paid for twice: **a new precondition on a shared collector is a change to every fixture that calls it, and the fixture list is part of the scope.**

### 16 — `TOOL-dRetiredFork-20`'s citation join is undefined over half its population

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-20.md` §4 Data model (third join) and §6 AC3.

**The defect.** The third join resolves "a `path:line` citation anywhere in the spec against that file's line count" and never says what happens when the cited path does not resolve. I measured it independently over the tracked corpus: **453 specs, 1721 backticked `path:line` citations, 854 naming a path `git ls-files` does not track — 50%.** They are bare basenames: `unattended.test.sh:188`, `check-verdict-epoch.sh:52`, `merge-rows.py:272`.

Undefined behaviour on half the population, on a lint whose own §5 risk row admits "a false red blocks every records commit repo-wide". If an unresolvable path reds, S6's pre-wiring drain is 854 dispositions and the lint cannot land; §4 Migration's "ships EMPTY … the S6 run decides its first rows" is incompatible with a drain that size. If it passes, the arm is a could-not-fail check over half the corpus — the class AGENTS.md §7 names and this unit invokes by name.

F2's shape predicate ("a slash AND an extension, or an exact match against a tracked path") would silently exclude every one of them, but §4 lists path shape and `path:line` shape as separate alternatives and never says F2 governs this join. AC3 grades only the beyond-EOF case.

**Fix.** §4 must state the disposition for an unresolvable citation path explicitly, and say whether F2's shape predicate scopes this join or only the §6-criterion one. Add a criterion for the unresolvable-path case, and record the measured figure in S6 so the drain is sized before the lint is wired rather than discovered by the builder.

**Left-shift gate.** This is the unit's own gate, so the left-shift is a rule about building it: **run the candidate predicate over the real tree and print hits AND near-misses before wiring it** — AGENTS.md §7 already says so, and S6 is where that happens. The addition worth making binding is that the run's output goes into the spec as a measured figure, because a drain nobody sized is a lint nobody lands.

---

## Medium

### 17 — `DEPL-dRetiredFork-9` AC4 names a command that reads no file

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-9.md` §6 AC4.

I ran it verbatim: `grep -n 'allow-ungraded\|re-adopt' memory/builds/dRetiredFork/spec/` prints "Is a directory" and exits 2, having read nothing. It can never "return a hit in both criteria", and a flat grep reports per file rather than per criterion. The criterion enforcing this unit's entire point — that the two criteria agree in writing — cannot be discharged, inside the unit promoted precisely because two criteria could not both be satisfied. §3 explicitly declines the argv-flag lint that would have caught this.

The flaw survives adding `-r`: `DEPL-dRetiredFork-1` S6 already names both `adopt --re-adopt --write` and `--allow-ungraded` independently of AC6, and DEPL-9's own spec names both, so a recursive grep hits those files whether or not the criteria carry the agreed sentence.

**Fix.** Extract each criterion's block by label — `awk` range extraction piped to `grep -c` — and require the two per-criterion counts to be equal and non-zero. Pin the two spec paths explicitly rather than the directory.

**Left-shift gate.** The `grep -c` predicate from blocker 1 catches the qualifier half. The other half is its own cheap arm: red any acceptance criterion pinning a `grep` whose final argument is a directory path with no `-r`, which is a pure syntax check with an obvious failing case.

### 18 — `TOOL-dRetiredFork-12` replaced a wrong count with another wrong count

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-12.md` §2 S1, and §9 rev-3.

Verified against source at both `b0108f13` and HEAD: `adopt-unattended.sh` substitutes **eight** tokens — `KIT_DIR`, `MEMORY_ROOT`, `LANDER` at `:222-224`, three `KEEPALIVE_*` and `ANCHOR_SCOPE` at `:225-228`, and `AUTH_PARAM` at `:233`, placed last with a fail-closed comment explaining the ordering. S1 enumerates the first seven and stops, presenting the list as exhaustive with the script as its subject; §9 rev-3 states flatly that it "substitutes seven tokens, not one". `tools/unattended/kit.toml:17` already declares `AUTH_PARAM` in the same `placeholders` list this unit edits.

The round-2 fold advertised this figure as a corrected citation and got it wrong again, in the sentence carrying the unit's whole measurement, and `TOOL-dRetiredFork-19` §1 then copied the same seven. The `TOOL_ROOT` conclusion survives; the substituted set does not.

**Fix.** Stop restating the list. Point at `tools/unattended/kit.toml:17`, which owns it — the derive-over-author rule the fold keeps breaking on counts. If a figure is wanted, it is eight, and `{{AUTH_PARAM}}` at `:233` is the eighth.

**Left-shift gate.** Same registry join as finding 9, pointed at descriptors: red a spec sentence enumerating a token set when the owning `kit.toml` declares a different one. The data is already machine-readable in both directions.

### 19 — `TOOL-dRetiredFork-12` retags a row `rendered` with no destination

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-12.md` §2 S1 and §4 Migration.

S1 retags `tools/unattended/playbook.fixture.md` to `role = "rendered"` without naming a `to`, and §4 Migration assumes the row keeps its path. Verified: all eleven `role = "rendered"` rows across the six declaring `kit.toml` files carry an explicit `to` **outside** their kit home — `.claude/skills/…` or `{memory_root}/…`. None renders in place. With no `to`, `destinations_for()` at `govkit.py:202` defaults the destination to `{kit}/<relpath>`, the source's own path, and `resolve_entry()` admits only LANDABLE_ROLES into `writes`, so the `include = "**"` engine rule keeps writing that same path while the rendered rule sits in `unlanded` — not the clean role change §4's receipt-identity argument assumes. In gov's own tree the adopter would render over its tracked source.

`check-playbook.sh` reads the fixture from the kit dir, so if the render lands elsewhere the checker is unrepointed and AC2 fails; if it lands in place, the receipt identity is one §4 does not describe. §10 cites the memory-tree rendered rules as precedent and every one of them writes outside the kit.

**Fix.** S1 states the `to` destination explicitly, and §4 says whether an in-home render destination is legal for govkit's receipt model. If it is not, add the S-item repointing `check-playbook.sh` at the rendered artifact and a criterion observing it at both prefixes.

**Left-shift gate.** A descriptor invariant with a clean failing case: red a `role = "rendered"` row whose resolved destination equals its source path, since a renderer overwriting its own template is a receipt the model cannot express.

### 20 — `DEPL-dRetiredFork-8` S4 would put authored prose at odds with a generated table

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-8.md` §2 S4.

S4 orders the README's roster sentence at line 122 — "Order 1 is nine independent absorptions" — to be re-rendered to eight. But that sentence counts the order-1 GROUP, and the generated `build-order` region three screens below shows step 1 holding nine units, `TOOL-dRetiredFork-1` through `-9`, TOOL-4 among them. TOOL-4 stops being an absorption; it does not leave order 1.

Executing S4 literally replaces one wrong number with a different wrong number, and puts authored prose in contradiction with the generated artifact — which is the side that cannot go stale. The asymmetry proves the point: S3 requires DEPL-6 §4 Rollout to say ONCE why the ninth order-1 unit is excluded, and S4 carries no equivalent clause for the README.

**Fix.** Rewrite the sentence rather than swapping the digit — "Order 1 is nine units, eight of them absorptions; `TOOL-dRetiredFork-4` reconciles a claim rather than absorbing a fix" — or drop the count entirely and let the generated table carry it, per the no-derived-counts-in-prose rule.

**Left-shift gate.** Red an authored cardinal in a build README that describes a population a `gen:` region on the same page enumerates. The generated region is the source; prose beside it stating a different number is the exact rule AGENTS.md §7 names, and here the two are in one file.

### 21 — `TOOL-dRetiredFork-19` AC1 asks `grep -c` where its hits are

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-19.md` §6 AC1, second half.

AC1 requires `grep -c 'TOOL_ROOT' <the TOOL-12 spec>` to return "hits only in prose explaining why it is absent, never in a declaration". `grep -c` emits a bare integer per file and can express neither location nor context. The criterion cannot be discharged by the command it pins, so it will be discharged by eye — the hand-verification of spec tokens that this unit and `TOOL-dRetiredFork-20` exist to end. Compare `DEPL-dRetiredFork-8` AC3's explicit "rather than by eye".

**Fix.** One byte-class: `grep -n`, plus the expected shape stated — every hit falls in the prose sentence explaining the token's absence, and none in §4's Data model or §10's seam claim.

**Left-shift gate.** Covered by blocker 1's predicate. Listed separately because it is a third instance of one class in one fold round, which is itself the signal: `grep -c` with a qualifier is now this build's most-repeated criterion defect and should be gated rather than re-found.

### 22 — `TOOL-dRetiredFork-5` S3 can be skipped with nothing to observe

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-5.md` §2 S3, against §6.

S3 absorbs inCMS's `encoding="utf-8"` fix on the corpus-recall `subprocess.run`, and it is conditionally scoped — "if gov HEAD still lacks it". Verified at HEAD: `tools/codebase-map/selftest.py:1188-1191` still calls `subprocess.run([...], capture_output=True, text=True, check=True)` with no `encoding=`, so the work is live and the row is not stale.

AC1 grades skip reporting, AC2 the vacuity RED, AC3 the unchanged executed count, AC4 the version bump plus `gen_map.py --check`. None observes the absorption. The one change in this unit that alters runtime behaviour can be dropped silently and the unit still passes its DoD — the unowned-work shape this build has now folded five times, inside a unit whose subject is a skip that looks like a pass.

**Fix.** Add a criterion: after the change, the corpus-recall `subprocess.run` in `tools/codebase-map/selftest.py` declares `encoding="utf-8"`, observed by grep. If the row is instead found stale, S3's disposition is recorded in the acceptance ledger with the measurement that decided it.

**Left-shift gate.** The build's own most-repeated class deserves the mechanical form it has earned: a spec lint joining every `S<n>` label in §2 to at least one §6 criterion that names it or its subject, redding on an unjoined item. A conditional scope item additionally requires its criterion to cover the skip branch. This build has folded the class at TOOL-3 M2, DEPL-3 M3 and B6, DEPL-7 finding 9 and TOOL-17 finding 10 — five hand-folds is the point at which a gate is cheaper than the sixth.

### 23 — `DEPL-dRetiredFork-8` S2 and S3 carry two additions nothing observes

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-8.md` §2 S2 and S3's second clause, against §6.

S2 requires `DEPL-dRetiredFork-6` AC2 to gain a clause reporting the inCMS `KIT_AGENT_CAP_DELTA` D1 row as stale or ALREADY ABSORBED. S3's second clause requires DEPL-6 §4 Rollout to say ONCE why the ninth order-1 unit is excluded. AC1 observes only that `TOOL-dRetiredFork-4` is gone, AC2 only that no "nine" describes the absorption count, AC3 that five ids are roster rows, AC4 hygiene.

Both additions can be omitted with a full green, leaving DEPL-6 AC2 silent about the very row a correct `contribute` emits — which is the defect this unit was promoted to remove.

**Fix.** Add a criterion requiring DEPL-6 AC2 to name the D1 row with its F2 disposition and the gov commit that took it, and a second requiring exactly one sentence in DEPL-6 §4 Rollout naming the excluded unit and the reason.

**Left-shift gate.** The S↔AC join from finding 22, which covers this instance and the next.

### 24 — `DEPL-dRetiredFork-9`'s entire left-shift is unobserved

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-9.md` §2 S4, against §6.

S4 records in the build README's Build-level rules that a done-condition criterion is read against every other spec's §2 before the set closes. §6 runs AC1-AC5 and none of them touches it — AC1, AC2 and AC4 grade the two criteria, AC3 is conditional on the zero decision, AC5 is hygiene. §5's "testing + left-shift gates" row names S4 as this unit's ONLY left-shift, so the row designates a check no criterion observes.

With nothing observing it, the rule ships unwritten while AC1-AC5 go green, and the class recurs on the next build with nothing recorded. That is a poor outcome for the one unit whose job is to stop this build's headline defect from happening again.

**Fix.** Add a criterion: the README's Build-level rules carries the sentence, verified by grep, and the build README slot contract still exits 0 after the addition.

**Left-shift gate.** The S↔AC join, plus one arm specific to this shape: when a §5 left-shift row names an `S<n>`, that item must be joined to a criterion, because an unobserved left-shift is the one omission that guarantees the class returns.

---

## Low

### 25 — `TOOL-dRetiredFork-5` carries a ratification pointer with no §8 behind it

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-5.md` status header tail.

Cross-tabbed across all 30 specs: eleven have no §8, and TOOL-5 is the only one of them carrying `ratified 2026-09-02`. It is Tier-1 with sections 1, 2, 3, 6, 7 and 9 — correct under the light profile — and has never had an Open questions section. TEMPLATE-SPEC ties that header field to an in-place §8 resolution mark, so here it points at nothing, and any later "which specs did the owner ratify" audit reads it as real. The fold commit says it stamped the nineteen specs whose forks it folded; twenty carry the stamp.

One correction to the rationale this arrived with: the predicted lint RED does not follow, because `TOOL-dRetiredFork-20` S3 builds three joins — gate names, path-shaped tokens, `path:line` citations — and no `ratified`↔§8 join. The anomaly is real and unique regardless.

**Fix.** Strike `· ratified 2026-09-02` from the header tail. No other edit.

**Left-shift gate.** The per-fork join from finding 5, with its converse arm: red a `ratified` pointer on a spec with no §8.

### 26 — `TOOL-dRetiredFork-14` §6 labels do not ascend

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-14.md` §6, AC7 between AC5 and AC6 (lines 112-116).

Verified: §6 runs AC1, AC2, AC3, AC4, AC5, AC7, AC6. Round 2's finding 28 raised this shape against `DEPL-dRetiredFork-3` AC8; DEPL-3's rev-4 log records the fix and its labels now ascend. The byte-identical sibling was not swept — prior shape 1, at its cheapest. The misplaced label is AC6, the version-marker criterion that catches a half-done bump, so it reads as an afterthought to anyone scanning for the end of the list.

**Fix.** Renumber so the labels ascend, and sweep the set for the shape rather than fixing this one.

**Left-shift gate.** Trivial and worth having beside the existing duplicate-label check the hygiene gate already runs: assert `S<n>` and `AC<n>` labels appear in ascending order within their section. The duplicate check exists; the ordering arm is the same parse.

### 27 — `DEPL-dRetiredFork-1` §2 labels do not ascend

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-1.md` §2 (lines 27-45).

Verified: S1, S2, S3, S4, S3b, S5, S6 — the rev-3 fold appended S3b after S4 instead of beside S3. The set's own convention contradicts it: `DEPL-dRetiredFork-2` places both its S3b and its S5b immediately after their parents. S3b is the needle-grading refusal §5 calls the build's highest-severity write path, so it is the item worst served by sitting out of sequence between two unrelated ones.

**Fix.** Move S3b to immediately after S3, in the same edit as finding 26.

**Left-shift gate.** Same ordering arm, with the suffixed-label rule stated: `S3b` sorts immediately after `S3`.

### 28 — `DEPL-dRetiredFork-1` S6 states a roster count that has moved

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-1.md` §2 S6 (line 46).

S6 reads "Nothing in the 25-unit set drives that population down", in live scope prose rather than a frozen revision-log line. The generated build-index in the build README reports 30 units, and `TOOL-dRetiredFork-20` S6, written in the same fold round, correctly says "This build's own set is 30 specs". A derived count authored in prose that has since moved — and it sits inside the sentence `DEPL-dRetiredFork-9` §1 leans on as its evidence, so the next reader cannot tell whether the claim was re-measured against the promoted units or predates them.

**Fix.** Rewrite the clause without the count — "no unit in this roster drives that population down" — so it cannot go stale when the roster next moves.

**Left-shift gate.** Red a spec sentence stating a cardinal for "the set" or "the roster" when the build's generated index reports a different unit count. One join, one file, no ambiguity.

### 29 — `TOOL-dRetiredFork-20` leaves its own bookkeeping correction unobserved

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-20.md` §2 S1, second clause, against §6 AC7.

S1 has two clauses — correct `TOOL-dRetiredFork-14` AC3's observation, and correct its rev-2 log line, which says B4 touched AC5 and overstates the fold. AC7 names only the first. The asymmetry is visible in the criterion's own text.

The unit whose entire subject is that a fold's bookkeeping went unverified leaves its own bookkeeping correction ungraded. TOOL-14 rev-2 keeps claiming a fold that covered both criteria when it covered one, and that is the record the next round reads as evidence.

**Fix.** Extend AC7 to require TOOL-14's rev-2 line to name AC5 only, verified by grep for the corrected sentence.

**Left-shift gate.** The S↔AC join from finding 22, which catches all four of this round's unobserved-clause findings — 22, 23, 24 and this one — in one predicate.

---

## What the mechanical sweeps said, and the one that was wrong

Reported in full, because a green row must never be misread as an unrun one.

| Check | Result | Note |
|---|---|---|
| non-declared gate-leg names | 0 | Confirmed clean; no counter-evidence found. |
| duplicate leg names | 0 | Confirmed clean. |
| duplicate AC/S labels | 0 | Clean — but see findings 26 and 27: labels are unique and out of ORDER, which this check does not measure. |
| header-rev vs §9-last-rev mismatches | 0 | Confirmed clean. |
| specs with unresolved forks | 0 | **COUNTER-EVIDENCE.** `DEPL-dRetiredFork-2` F1 is unresolved; the sweep is satisfied by F2's separate mark. Findings 5 and 6. |
| RESOLVED without a `ratified` pointer | 0 | Clean in that direction. The CONVERSE is dirty: `TOOL-dRetiredFork-5` carries the pointer with no §8. Finding 25. |
| `check-memory-hygiene.sh`, slot contract, build-index freshness | exit 0 | Re-confirmed; no counter-evidence. |

Both dirty rows are failures of the same join. The sweeps test for the PRESENCE of a token in a file; what the ratification needed was a join from each fork bullet to a mark that reaches it, and from each header pointer back to a section that exists. Finding 5's proposed gate is that join, and it closes both rows plus finding 6's fact-question carve-out.

## Re-derived claims about existing code

Every citation the fold newly asserted was checked against source. Round 2 found two false ones introduced by round 1's fold; this round found **one**, and it is finding 18.

| Claim | Verdict |
|---|---|
| `settings-merge.py:49` defines `HOOK_MARKER` | TRUE — `HOOK_MARKER = "agent-cap.js"` at exactly `:49`. |
| `adopt-unattended.sh` substitutes seven tokens at `:222-228` | **FALSE.** `:222-228` carries seven, and `{{AUTH_PARAM}}` at `:233` is an eighth the same function substitutes. Finding 18. |
| `scratch-guard.test.sh:183-190` hard-fails on absence | TRUE — `:183-185` is the FAIL-on-missing branch, `:186-190` the diff and drift arms. |
| `agent-cap.test.sh:810-817` | TRUE — the same parity block at exactly those lines. |
| `tools/hooks/kit.toml:43-46` covers scratch-guard | TRUE — the `[[files]]` rule for `scratch-guard.js` with both destinations. |
| `install-prefix-carried.txt` holds 33 test rows summing to 259 | TRUE — counted: 33 rows, sum 259. Which is what makes finding 9 a defect. |
| `memory/project` holds nine registries | TRUE — nine `.txt` files, no others. |

Three further claims were re-derived because findings depended on them: `tools/workflows/kit.toml:18` declares `placeholders = ["TOOL_ROOT"]` with `[adopt] argv = []` (findings 13 and 14, TRUE); `settings-merge.py:83/86-88/286/291` perform no token substitution and refuse a non-existent path (blocker 2, TRUE); and the `path:line` corpus measurement, which I reproduced independently at 453 specs, 1721 citations, 854 unresolvable (finding 16 — the count differs from the one in the finding by the citation regex used, and the conclusion is unaffected at either figure).

## Round shape and what it says about stopping

Precision fell from round 2's 0.84 to 0.62, on a raw set of 66 producing 41 confirmed and 25 refuted, consolidating to 29 distinct defects. The direction is right for a narrow re-audit and the absolute number is still above the ~0.5 floor where the charter says to tighten scope before adding lenses.

The distribution is the interesting part. Round 2's headline was that 21 of 30 defects were CREATED by the fold. This round, the fold created far fewer — the prepend shape is gone entirely and only one missed anchor survives. What it created instead is concentrated in two places: the blanket ratification, which settled recommendations against each other without reading them (blocker 3, findings 5 and 6), and the five promoted units, which were written as fixes and never graded as specs (blockers 1 and 2, findings 12, 13, 16, 20, 23, 24, 29 — nine of twenty-nine defects in five of thirty specs).

That is a usable signal for whether to run a round 4. The recurring-defect knee has been reached on the fold mechanics: substitution works, and the remaining instance-not-class misses are all paraphrase survivors that a string-equality assertion structurally cannot catch, so another round of the same method finds the same kind of thing. It has NOT been reached on the promoted units, which have been reviewed exactly once — this once. The S↔AC join (finding 22) and the per-fork resolution join (finding 5) between them would have caught eleven of the twenty-nine defects below blocker level; building those two gates is a better use of the next pass than a fourth reading.
