**Serves:** spec-audit TOOL-aBoundedVerdict-1..5 TOOL-aBoundedVerdict-11..19

## Verdict: BLOCKED

## 1. The review shape

raw 85, confirmed 81, refuted 4, unverified 0, lenses 5/5.

Lens key for the table below: `facts` = every factual claim about existing code, re-verified ·
`x-read/<AXIS>` = the four-axis cross-read · `accept` = underspecification and unobservable
acceptance · `assume` = unstated assumptions and unnamed dependencies · `prior-art` = prior art.

Ref key: `spec-N` = `memory/builds/aBoundedVerdict/spec/2026-08-16-spec-TOOL-aBoundedVerdict-N.md`
for N in 1..5 and `memory/builds/aBoundedVerdict/spec/2026-08-19-spec-TOOL-aBoundedVerdict-N.md`
for N in 11..19; `README` = `memory/builds/aBoundedVerdict/README.md`. Every other ref is spelled in
full.

## 2. CONFIRMED findings

| id | lens | sev | ref | what is wrong | the fix |
|----|------|-----|-----|---------------|---------|
| 1 | facts | blocker | spec-2:156 | Population stated as four run-state files with ONE codeless ABORTED; `git ls-files 'memory/builds/*/RUN.md'` returns seven, three ABORTED and codeless | Restate §4 and §3 over `memory/builds/aWalkedCorpus/RUN.md`, `memory/builds/cBriefedPilot/RUN.md`, `memory/builds/dClosedLexicon/RUN.md`; derive each code from its own parked text |
| 21 | x-read/ACCEPTANCE | blocker | spec-2:276 | AC4 promises the new leg check is green over the real tree on landing day; it reds on two records the spec never names | Restate AC4/AC4a over the measured set, or assert only over a build-time re-measure |
| 38 | accept | blocker | spec-2:101 | §3's non-goal caps the retrofit at "the one §4 enumerates", forbidding the retrofit AC4 needs | Move the cap with the count |
| 55 | assume | blocker | spec-2:238 | Files touched names only `memory/builds/dClosedLexicon/RUN.md` | Name all three ABORTED records |
| 2 | facts | blocker | spec-2:64 | Fact pin spelled "correct at eight, moving to nine"; `memory/guides/UNATTENDED-PROTOCOL.md:110` and `tools/unattended/PROTOCOL.template.md:110` both read eleven | Spell the pin's ROLE, not its value, or read 11→12 at build time |
| 19 | x-read/INTERFACE | blocker | spec-2:64 | Same pin wrong in four further carriers: spec-2:29 "ninth", spec-2:236 "seven-fact pin", README:130, README:166 | Delete every numeral; enumerate the five carriers by path |
| 56 | assume | blocker | spec-2:67 | S7 says the driver's resume comment carries FIVE; `tools/unattended/unattended.sh:1360` says seven | Correct that site to seven |
| 4 | facts | blocker | spec-5:15 | rev-6 claims S1/S2 restated to the shipped two-field verb; S1, S2:18, AC1:181, AC2:184 still spell three flags | Apply the restatement to `--item`/`--reason` |
| 37 | accept | blocker | spec-5:52 | The rev-6 reconciliation reaches the argument and none of the sites: §1:9, §4:110, inventory:128, §10:283 | Restate every site; add the kind divergence to S6a |
| 73 | prior-art | blocker | spec-5:59 | Four further three-field sites: S3:21, §3:99, §5:162, F1's premise | Rewrite all of them; AC2 must drive a missing `--item` and a missing `--reason` |
| 18 | x-read/SCOPE | blocker | spec-11:42 | `build-complete`'s term 1 (`tools/unattended/unattended.sh:1495`) and `roster_ids`/`missing_units` (:889-890) still read the AUTHORED roster pair; no unit re-points them | Add a scope item re-pointing them and an AC observing `--close` on a README carrying no authored pair |
| 39 | accept | blocker | spec-15:53 | Stage ratio is 3-of-5, not 4-of-5: `verb_phase` (`tools/unattended/unattended.sh:1023-1026`) is the second non-stager, so S4's source rule reds on the landing diff | Stage `verb_phase` in S1 or name it an exemption in S4 with the reason |
| 3 | facts | high | spec-2:299 | AC8's alternation stops at `ten`; run over the three roots it returns no line from either protocol carrier | Key on the noun, assert per carrier |
| 20 | x-read/ACCEPTANCE | high | spec-2:299 | The criterion is green today over a stale pin — the failure its own text says it was rewritten to prevent | Anchor on `facts and nothing else` and assert the extracted numerals are equal |
| 5 | facts | high | spec-15:53 | §1:7, S1:16, inventory:73/:78 and the reuse audit:195 all repeat the wrong 4-of-5 | Correct to 3-of-5 in all five places |
| 6 | facts | high | spec-12:32 | S6 as worded is satisfied by every arm: only `gates-green` and `build-complete` carry a literal `return 1`, and both set `DOD_OUT` | Reword to "may not RETURN NON-ZERO without having set `DOD_OUT`"; inventory:91 to "6 of 8 fail silently" |
| 40 | accept | high | spec-12:171 | AC6's "fails against the shipped driver" is therefore false; the `*)` arm at `tools/unattended/unattended.sh:1533` is a ninth arm outside the declared exemption | Phrase over the failing exit; exempt or message the `*)` arm |
| 7 | facts | high | spec-14:35 | `grep -ni serves tools/workflows/tier2-review.js` returns nothing — the harness writes no `**Serves:**` line, kind-less or otherwise | Restate S7 as "emit the line with its kind"; inventory:95 Today cell to "absent" |
| 41 | accept | high | spec-14:174 | A kind-only line is MALFORMED under `memory/HYGIENE.md:246`, and the filename branch still needs M8's rename, so AC5's "no hand edit" is unobservable | Write the ids too and name the file in check 5's grammar, or state which edit remains |
| 59 | assume | high | spec-14:35 | The harness does not write the record either: `tools/workflows/tier2-review.js:307` instructs the SYNTH AGENT to write it | Make S7 a synth-prompt change beside `tier2-review.js:315` |
| 22 | x-read/INTERFACE | high | spec-5:110 | §4 Data model and S1:16 specify a `park` kind; `tools/unattended/unattended.sh:1597` writes `decision` | Correct both to `decision` |
| 77 | prior-art | high | spec-5:15 | S6a enumerates two divergences and declares the rest reconciled; the kind token is an unreconciled third | Add it as S6a's third bullet |
| 23 | x-read/SCOPE | high | spec-5:9 | "`park()` exists with exactly two callers" — it has four (`tools/unattended/unattended.sh:1135`, `:1298`, `:1435`, `:1597`), one of them the verb §1 says does not exist | Rewrite §1's Goal to the reconciled scope; correct the inventory's Today column |
| 24 | x-read/SCOPE | high | spec-5:67 | S7's taxonomy never classifies the `waiver` kind, which is live and counted at `tools/unattended/unattended.sh:1344` | Name `waiver` and assign it a class with the reason |
| 79 | prior-art | high | spec-5:68 | S7a turns the hole into a driver constant, so the shipped set would drop waivers; `memory/guides/UNATTENDED-PROTOCOL.md:380-381` puts waivers in front of the owner | Put `waiver` in DECISION; fix S6a's "inflated by three kinds"; fixture one line of every kind |
| 25 | x-read/ACCEPTANCE | high | spec-2:82 | S10 changes `memory/HYGIENE.md` check 5's grammar; none of AC1-AC12 (spec-2:269-313) observes it | Add a red/green AC pair and declare `memory/HYGIENE.md` + `tools/memory-tree/HYGIENE.template.md` |
| 26 | x-read/SCOPE | high | README:226 | The `-3` row assigns `--attest` (spec-15:18) and the non-overridable sentence (spec-19:21) to a unit whose rev-6 log says "No scope item changes" (spec-3:274) | Rewrite the row to READY/unchanged |
| 27 | x-read/INTERFACE | high | README:142 | Three documents state three read-path budgets; measured is 91997 B against `.memory-tree.conf:113` `READ_PATH_CEILING="112987"` | Fix the README rule to 91997/112987 and the six-unit spender set; delete spec-3's figures |
| 28 | x-read/ORDERING | high | spec-5:65 | `-5` (position 5) and `-3` (position 9) both declare a dependency on `-15` at position 10, under README:100 "a dependency order, not a preference" | Move `-15` ahead of both; record the settlement in spec-15's F2 |
| 42 | accept | high | spec-12:221 | Five rev logs (-11, -12, -13, -14, -19) claim forks resolved that carry no RESOLVED mark; `memory/TEMPLATE-SPEC.md:155-158` requires the mark in place | Mark them, or correct the logs to "open with the recommendation standing" |
| 43 | accept | high | spec-11:186 | The §5 security bullet still mandates rev-1's withdrawn row-byte rule | Rewrite to the id-set invariant: refuse a REMOVED or RENAMED id, tolerate status/rev/date/title |
| 61 | assume | high | spec-11:186 | The same bullet directly contradicts S6 (:30-36) and AC7a (:229-232), which require a `SPECCED`→`CLOSED` move to return 0 | Same rewrite; the "edits an existing unit's id" half survives it |
| 44 | accept | high | spec-11:213 | AC2 pins 4 unit rows; the spec-linked set in `memory/builds/aBranchedMandate/README.md` is SIX, corroborated by `memory/builds/aBranchedMandate/RUN.md:12` | Change to 6 and 0, cross-checked against `units-at-landing` |
| 60 | assume | high | spec-14:25 | "none names a usable tip" is false — eleven tracked records name a `sha..sha` range | Keep S4, drop the clause; rest it on the harness's `HEAD` default at `tools/workflows/tier2-review.js:66` |
| 62 | assume | high | spec-11:180 | S6 rests the authority on the BASE blob without stating that `.unattended.conf:89` `ANCHOR_SCOPE="published"` puts that blob inside the run's reach | Carry the limit in §4 and §5, as `memory/guides/UNATTENDED-PROTOCOL.md:32-35` already does for the authored roster |
| 63 | assume | high | README:222 | Replaying `plan_state` (`tools/unattended/unattended.sh:857-878`) prints FORKED for all fourteen specs; the table says READY for three | Resolve the mechanism-only forks, or say the units are FORKED-by-design and what the verb prints |
| 74 | prior-art | high | spec-18:175 | F1 resolves "stays" against OPEN `memory/backlog/TOOL.md:71` (`TOOL-cSettledDocket-11`), whose remedy is the opposite, and never names it | Name the row; keep the exemption for the emptiness branch only |
| 75 | prior-art | high | memory/DECISIONS.md:63 | `-1` reverses a landed append-only row and cites it nowhere; the same gap at `:64` for the halt-code ordinal | Add the "Falsifies:" pointer to the rev-6 log and to `-2`, stating which clauses survive |
| 76 | prior-art | high | memory/backlog/TOOL.md:81 | `-13` closes the driver half of OPEN `TOOL-aBoundedVerdict-10` without citing it and leaves the `run-gates.sh` per-leg deadline unowned | Cite the row; scope or explicitly out-scope the second fix |
| 78 | prior-art | high | spec-11:31 | S6 keeps the opt-in-by-presence guard (`tools/unattended/unattended.sh:731`): a BASE with no units region makes BASE ⊆ HEAD vacuous | Make an absent or malformed BASE pair a NAMED refusal with a cutoff |
| 8 | facts | medium | spec-14:25 | 28 records name a range, not 25 | Restate with the command beside it |
| 9 | facts | medium | spec-11:213 | AC2's 4 is `memory/builds/aDeclaredCeiling/RUN.md`'s number | Change to 6 |
| 10 | facts | medium | spec-11:135 | "six ids each" — `memory/builds/aDeclaredCeiling/RUN.md:10` carries four | "six and four respectively"; AC10 names both |
| 11 | facts | medium | spec-3:139 | 72122/86476/14354 all stale; ceiling 86476 retired | Delete the figures, keep the re-measure instruction |
| 12 | facts | medium | spec-3:130 | `memory/guides/BUILD-METHOD.md` is 245 lines / 17460 B, not 236 / 16466 | Re-measure or point at the `wc` |
| 14 | facts | medium | spec-1:81 | "thirteen of forty-three build folders" — measured twelve of forty-nine at base 098bebd9 | Restate, or re-run the count in the landing commit |
| 29 | x-read/SCOPE | medium | spec-12:25 | S4 duplicates spec-16:28 with a different fourth failure mode; spec-12:46 already disclaims the item | Delete S4/AC4 from -12; refresh its §3 |
| 30 | x-read/SCOPE | medium | spec-19:31 | The roster bullet hand-off lands in spec-11:161 Files touched and in no scope item or AC | Add both; observe `grep -c 'Opt-in by presence'` returns zero in `tools/unattended/PROTOCOL.template.md:33` and `memory/guides/UNATTENDED-PROTOCOL.md:33` |
| 31 | x-read/ACCEPTANCE | medium | spec-11:213 | AC2 and the Migration paragraph carry transposed counts | 6/0 and "six and four" |
| 32 | x-read/SCOPE | medium | README:138 | The re-stamp rule claims five units carry `memory/guides/SESSION-KICKOFF.md`; four do, and `-1` is not one of them | Add it to every unit naming a watched path; drop the count |
| 33 | x-read/INTERFACE | medium | spec-13:95 | Inventory inverts both halves: 3 in the driver, 2 in the leg | Correct the row; AC5 to the testing bullet at spec-13:158 |
| 34 | x-read/SCOPE | medium | README:104 | The dependency paragraph reads positions against the withdrawn five-unit roster and names the withdrawn review cap (README:198) | Rewrite using ids; delete the cap sentence; "five specs" (README:182) is fourteen |
| 45 | accept | medium | spec-16:32 | S6 is a question, answerable now: `tools/unattended/check-unattended.sh` carries no DoD predicate | Replace with the measured statement plus an arm and an AC |
| 46 | accept | medium | spec-2:81 | S10's "Forward-only" names no mechanism; every other ratchet here is a dated conf key | Name the cutoff key or split S10 into its own unit |
| 47 | accept | medium | spec-1:315 | `grep -c 'RUNAWAY'` returns ≥1 on a CORRECT implementation, since the leg reads constants via `core_of` (`tools/unattended/check-unattended.sh:65`) | Mirror spec-2's AC6 complement form |
| 48 | accept | medium | spec-12:178 | AC9 is green before the unit is built: `tools/unattended/unattended.test.sh:1670` already prints against `FLOOR_ASSERTIONS=296` | Delete, or restate as the count rising |
| 49 | accept | medium | spec-3:139 | Both -3 budgets stale at its own declared base; AC5 grades against them | Re-measure; AC5 names the command |
| 50 | accept | medium | README:138 | The self-congratulating clause is false in both directions | Update to the fourteen-unit set |
| 51 | accept | medium | spec-5:65 | `-5` S6/AC6 rest on an interface that is neither built nor decided — spec-15's F2 is open | Reorder or resolve F2; state what writes the value in the fixture |
| 64 | assume | medium | spec-5:59 | Eight sites still spell three fields; rev-6's "S4a" (spec-5:273) is `-1`'s item, not this spec's | Restate; fix the cross-spec citation |
| 65 | assume | medium | spec-11:135 | Same asymmetric roster counts | "six and four", or drop the count since AC10 asserts byte-identity |
| 66 | assume | medium | spec-3:130 | The derived displacement claim (spec-3:135) is computed off 236 lines; at 245 it is 5 lines, not 14 | Recompute off the measured value |
| 67 | assume | medium | spec-18:20 | Deleting term 3 leaves `landed-via-lander` with no reachable failure mode — terms 1-2 are pre-refused by `tools/unattended/check-unattended.sh:54-56` | Keep the grep with a dated note, or retire the item; cite `memory/guides/UNATTENDED-PROTOCOL.md:219` |
| 68 | assume | medium | README:91 | The order violates `memory/guides/BUILD-METHOD.md:53` for `-3` and `-5` against `-15` | Reorder, or state that both land degraded |
| 69 | assume | medium | README:136 | Seven further units touch a watched path and omit the re-stamp; README:135's "Every unit" is false | Restate as "every unit that touches a watched path" |
| 70 | assume | medium | spec-13:22 | S3 states a blocking GUI prompt as fact; the source record calls it "a possibility, not a finding", node-`c`-specific | Restate the grounds; keep the fix; replace AC6's observable or say why none exists |
| 80 | prior-art | medium | spec-11:214 | AC2's stated pair carries no replay command, against README:175 | Correct to 6/0 with the command beside it |
| 81 | prior-art | medium | spec-14:36 | The wrong premise is inherited from `memory/backlog/TOOL.md:97` (`TOOL-aLoosenedCeiling-6`) | Amend the row when closing it |
| 82 | prior-art | medium | README:226 | Both mechanisms disclaimed at spec-3:281 | Move them to the `-15` and `-19` rows |
| 83 | prior-art | medium | spec-5:9 | Four callers at the spec's own declared base too, and `tools/unattended/unattended.sh:1551` states the pre-verb figure | Correct §1 and inventory:127 |
| 85 | prior-art | medium | memory/backlog/TOOL.md:45 | `-16` supersedes OPEN `TOOL-cBriefedPilot-8` and `-11`/`-12` move what OPEN `TOOL-cBriefedPilot-7` describes; neither is named | Name and close both; their specs are already CLOSED at `memory/builds/cBriefedPilot/README.md:344-345` |
| 15 | facts | low | spec-1:118 | Ten records over two days, not "10 in one day"; the replayed counts belong to rounds 3-7 | Restate and re-index |
| 16 | facts | low | spec-13:95 | `:211-212` is a comment, not a call site | Cite `:228` and `:230` only |
| 17 | facts | low | spec-11:298 | The `GEN_REGIONS` seam is `memory/map/features/build-readme-surface.md:80`, not `:87` | Change the citation |
| 35 | x-read/ACCEPTANCE | low | spec-14:25 | The count disagrees with its own evidence record (`memory/builds/aBoundedVerdict/build/2026-08-18-research-TOOL-aBoundedVerdict-1-close-path-audit.md:231`, "7 of 90") by 3.5x | State the measurement with its command, or keep only the zero |
| 36 | x-read/INTERFACE | low | spec-12:179 | `tools/testsuite-count-waivers.txt` does not exist; it is `memory/project/testsuite-count-waivers.txt` | Spell the real path, or name the leg |
| 53 | accept | low | spec-18:155 | AC6's bare `git diff` is empty after the commit whether or not the prohibition held | Name the range |
| 54 | accept | low | README:226 | Same misassignment as 26/82 | READY/unchanged |
| 71 | assume | low | README:182 | Four claims left behind by the growth to fourteen units | Re-take each with its command |
| 72 | assume | low | spec-12:178 | Same wrong waiver path; spec-12:113 writes `tools/unattended/check-arms` for an `ARMS_FLOORS` entry read by `tools/memory-tree/check-arms.py` | Fix both spellings |
| 84 | prior-art | low | spec-13:95 | The audit it derives from says two | Correct the leg's half only — the driver's "2" is right as a network-call count |

### Blockers

**B1 · ids 1, 21, 38, 55 — the migration population is measured wrong at the spec's own base.**
`spec-2:156` states four tracked run-state files with one codeless ABORTED record. Measured at the
declared base 098bebd9 and identically at HEAD, `git ls-files 'memory/builds/*/RUN.md'` returns
SEVEN: four LANDED and three ABORTED — `memory/builds/aWalkedCorpus/RUN.md`,
`memory/builds/cBriefedPilot/RUN.md`, `memory/builds/dClosedLexicon/RUN.md` — none carrying a halt
code, because the fact does not exist yet. The consequence is mechanical, not cosmetic: AC4
(`spec-2:276-280`) promises "the check is green over the real tree on the day it lands" and AC4a
migrates only `dClosedLexicon`, so the new leg check reds the merge bar on two records the spec never
names; `spec-2:101` then caps the retrofit at "the one §4 enumerates", forbidding the fix; and Files
touched (`spec-2:238`) names one file. This is the defect `README:161-164` records rev-4 catching
once, re-landed at one third of its size, and the set disagrees with itself — `spec-11:135` already
reads "The seven tracked run-state files." The hedges at `spec-2:173-174` and `spec-2:281` tell the
builder to re-measure and are worth keeping; they do not repair a stated count, an enumerated
population of one, or §3's cap.

**B2 · ids 2, 19, 56 — the authored-region fact pin is stale in four carriers at once.**
`memory/guides/UNATTENDED-PROTOCOL.md:110` and `tools/unattended/PROTOCOL.template.md:110` both read
"**Authored**, carrying exactly eleven facts and nothing else", with the enumeration beneath running
1..11. So the halt code is the TWELFTH fact. `spec-2:64` says the sentence is "currently correct at
eight, moving to nine"; `spec-2:29` calls the code "the region's NINTH fact"; `spec-2:236` calls it
"the seven-fact pin"; `README:130` says eighth and `README:166` says ninth. S7's second site is wrong
a different way: it says the driver's resume comment carries FIVE, and
`tools/unattended/unattended.sh:1360` says seven. Only the two map statements
(`memory/map/features/unattended.md:76` and `:119`) match S7's description. The spec's own hedge at
`spec-2:72-73` — read the value at build time — is the right instruction and does not reach S3, the
rev log or Files touched, which spend the ordinal as a fact. Do not spell a move count either: the
pin's history across those carriers is non-monotone and not cleanly derivable.

**B3 · ids 4, 37, 73 — `-5`'s rev-6 reconciliation is announced and never applied.**
`spec-5:52-60` states that S1 and S2 are restated to the shipped two-field verb. They are not. S1
(`spec-5:15`) still spells `--question --options --reason`; S2 (`:18`), S3 (`:21`), §3 (`:99`), §4's
Data model (`:110`), §5 (`:162`), the inventory row (`:128`), AC1 (`:181`) and AC2 (`:184`) all still
describe three fields. The shipped verb is two-field: `tools/unattended/unattended.sh:1556` takes
slug · item · reason, refuses on `--item`/`--reason` only, and routes an unknown `--question` to
`fail 14`. A builder implementing AC1/AC2 mints a second incompatible verb, and S2's "refused for a
missing field" is unbuildable for a field that does not exist. §1 (`:9`) compounds it — the verb
shipped under `TOOL-cSettledDocket-1`, so the premise that a run must hand-edit is false.

**B4 · id 18 — `build-complete`'s authored-roster dependency is claimed by no unit.**
The design record and `README` both put `-11` at the front because `build-complete` cannot pass until
it lands. But `build-complete`'s first term reads the AUTHORED `<!-- roster:units -->` pair
(`tools/unattended/unattended.sh:1495`), and `roster_ids`/`missing_units` read it too (`:889-890`).
`spec-11:18-21` re-points three call sites (`:913`, `:1078`, `:1339`) and names none of those.
`spec-11:43-45` declines to delete the authored pair, S5 renders only `gen:build-units`, and F3
(`spec-11:269-274`) is raised to the OWNER and unresolved. Measured: of 49 build folders only four
carry the authored pair, and `memory/builds/aBoundedVerdict/README.md` carries none — this build
could not close itself. `spec-11:121` nonetheless claims the item "passes when its units are
terminal". The unit clearly intends the removal (`spec-11:176-179` rejects leaving it "dependent on
an undocumented hand-edit"); what is missing is the scope item and an AC whose fixture is a README
with no authored pair (`spec-11:218-220` leaves that unspecified).

**B5 · ids 39, 5 — the stage-rule premise misdescribes the driver.**
`grep -n 'set_fact "$rel" phase' tools/unattended/unattended.sh` returns five writers (`:1023`,
`:1069`, `:1133`, `:1288`, `:1442`); `stage_or_fail` has four call sites (`:1080`, `:1136`, `:1303`,
`:1598`) and `:1598` is inside `verb_park`, which writes no phase. So three of five stage, and
`verb_phase` (`:1023-1026`) is the second omission, not `--close` alone. S4's source rule — every
phase write followed by `stage_or_fail` — therefore reds on `verb_phase` on the very diff that lands
it, and AC7's single red fixture (`spec-15:152-154`) is built on a one-violator assumption. The same
error repeats at `spec-15:7`, `:16`, `:73`, `:78` and `:195`. The row's other fraction is correct:
the bypass guard genuinely is 3-of-4 park callers, the override at `:1435` being the exception.

### Highs

**H1 · ids 3, 20 — AC8's completeness grep cannot match the value it exists to police.**
I ran the exact pattern at `spec-2:299`. Its spelled-number alternation stops at `ten` and the live
pin is `eleven`, so neither protocol carrier appears in the output; of the five statements AC8 claims
to cover it returns three, and most of its lines over the three roots are unrelated "N of them"
prose, so "returns only statements naming the current count" is false as well. This is the failure
`spec-2:300-303` says the criterion was rewritten to prevent, one spelled numeral later. Anchor on
`facts and nothing else` and assert the extracted numerals are equal, per carrier.

**H2 · ids 6, 40 — `-12`'s S6 meta-gate is vacuous against the shipped driver.**
`dod_met` spans `tools/unattended/unattended.sh:1449-1544`. A literal `return 1` appears in exactly
two arms — `gates-green` (`:1464`, `:1466`) and `build-complete` (`:1497`) — and those are the two
arms that already set `DOD_OUT`. Six arms fail silently by falling off the end of the case arm, so
S6 as worded (`spec-12:32`) is satisfied by every arm today and AC6's "fails against the shipped
driver" (`spec-12:171-173`) is false — the fixture-passes-by-finding-nothing class `spec-12:190`
warns about. The `*)` arm (`:1533`) is a ninth arm outside the two-item exemption, and even under the
exit-level rewrite `gates-green`'s `DOD_OUT=""` means the rule must require a NON-EMPTY message.
S1-S5 also leave `records-current`, `landed-via-lander` and `authorization-reachable` without a
message, so the "0 plus 2 exemptions" target is unreachable in this unit's scope.

**H3 · ids 7, 41, 59 — the review harness writes no binding line at all.**
`grep -ni serves tools/workflows/tier2-review.js` returns nothing. The synth prompt
(`tools/workflows/tier2-review.js:290-317`) asks for a severity-ranked report, the review-shape line,
a range line at `:315` and a JSON return — no binding line, kinded or otherwise. So S7 (`spec-14:35`)
is wrong in both halves: nothing is written with a missing kind token, and the harness does not write
the record at all — `:307` instructs the synth AGENT to write it. The work is a synth-prompt change,
and AC5 (`spec-14:174`) must observe the agent's output. AC5 is unreachable as scoped for a second
reason: a kind token with no id is MALFORMED under `memory/HYGIENE.md:246` and
`tools/memory-tree/gen_build_index.py:377-384`, and check 21's fourth branch
(`tools/memory-tree/check-memory-hygiene.sh:605-624`) also requires the FILENAME to project an id,
which `memory/guides/BUILD-METHOD.md` M8 still assigns to a hand rename.

**H4 · ids 22, 77, 23, 24, 79 — the park verb's kind, callers and taxonomy.**
`tools/unattended/unattended.sh:1597` writes kind `decision`; `spec-5:16` and `spec-5:110` specify a
`park` kind that nothing reads — `--status`'s counter at `:1344` greps `(decision|abort|override|waiver)`.
S6a enumerates two divergences and declares the rest reconciled, so this is an unreconciled third.
`park()` has four callers (`:1135`, `:1298`, `:1435`, `:1597`), not the two `spec-5:9` claims or the
three its inventory row implies; the driver's own comment at `:1551` states the pre-verb figure. And
S7's two-class taxonomy (`spec-5:67-73`) never classifies `waiver`, which is live, counted, and put
in front of the owner by `memory/guides/UNATTENDED-PROTOCOL.md:380-381`. Because S7a makes the
DECISION set a driver constant the leg reads, an implementer building from the enumeration ships a
set short one member and regresses a stated behaviour. Under S7's own test the shipped counter is
inflated by ONE kind, not the three S6a claims — the spec uses "decision" for both the literal token
and the class, and the two senses must be separated before either the constant or the counter can be
built.

**H5 · id 25 — `-2`'s S10 is specced, unobserved and undeclared.**
S10 (`spec-2:82`) makes a verdict token the first line of a review record and changes
`memory/HYGIENE.md` check 5's grammar. Read in full, AC1-AC12 (`spec-2:269-313`) cover the halt code,
the fact pin, the kickoff size, kit versions, arms and run-gates; none mentions a verdict token, a
first line, or check 5. `memory/HYGIENE.md` appears once in the whole spec, inside S10 itself, and is
absent from Files touched (`spec-2:228-244`); `tools/memory-tree/check-memory-hygiene.sh` is listed
at `spec-2:322` for a different reason. `-1`'s AC3 observes only that the legal set is byte-identical
to the one `-2` defines. So the larger half of this unit has no observable and no declared write set.

**H6 · id 26 — `README`'s classification table widens the wrong unit.**
`README:226` gives `-3` an `--attest` verb and the non-overridable-item sentence. `--attest` is
`spec-15:18` with its own Files touched, ACs and forks; the sentence is `spec-19:21`; and `-3` routes
both away at `spec-3:280-281` while its rev-6 log (`spec-3:274`) states "No scope item changes". The
table is the artifact a builder reads to decide what each unit must contain, so this is the one
document in the set that would put two units on one mechanism. Findings 82 and 54 are the same defect
seen from the prior-art and acceptance lenses.

**H7 · id 27 — three read-path budgets, one of them right.**
`python tools/memory-tree/corpus_ids.py --report` returns "read path : 6 files, 91997 B" against
`.memory-tree.conf:113` `READ_PATH_CEILING="112987"`, with `memory/guides/UNATTENDED-PROTOCOL.md` at
27582 B and `memory/guides/BUILD-METHOD.md` at 17460 B. `spec-1:231-235` matches exactly.
`README:142-146` says 70262 against 86476 with the protocol at 18214 B; `spec-3:139-140` says 72122
against 86476. 86476 is a retired ceiling, so a builder trusting either document believes in 14-16 KB
of headroom against a number that no longer exists. The README's own rule says the spender set is
stated "HERE and nowhere else" while omitting `-11` and `-14`, which `spec-1:234-235` names.

**H8 · ids 28, 51, 68 — two units depend on a unit sequenced after them.**
`README:100` declares "a dependency order, not a preference" and places `-5` at 5, `-3` at 9 and
`-15` at 10. `spec-5:65-66` names `-15`'s `--attest --value` as the writer S6 needs; `spec-3:280-282`
says its halt path "is reachable only by a hand-edit today" for the same reason. `-15` declares no
dependency of its own, so moving it is free. Both dependencies are soft — the keys are hand-editable
— so the cost is a hand-edit rather than a block, and `spec-15:171-174` agrees with `-5` about the
direction; what fails is the order, and the fact that the order paragraph never mentions `-15`.

**H9 · id 42 — five revision logs claim fork resolutions their §8 does not carry.**
In `-11`, `-12`, `-13`, `-14` and `-19` only F1 carries a `RESOLVED (agent, 2026-08-19, delegated):`
mark; F2 in all five, and F3 in `-12`, carry a bolded Recommendation and nothing else, while their
rev logs (e.g. `spec-12:221`) say otherwise. `memory/TEMPLATE-SPEC.md:155-158` requires the mark in
place, and `tools/memory-tree/check-memory-hygiene.sh:815-844` grades a terminal spec's §8 by
counting items against those matching RESOLVED — a landing-time block, not a red today. `-15`, `-16`,
`-17` and `-18` state the same situation honestly, which is what makes this an omission rather than a
house convention.

**H10 · ids 43, 61 — `-11`'s security bullet instructs the rule rev-2 deleted.**
`spec-11:186-188` still mandates refusing a CHANGED row, including a status change. Rev-2 replaced
that with an id-SET subset test: `spec-11:30-36` compares "the id set and **not the row bytes**",
`spec-11:98-113` says a byte-level test "would therefore refuse **every run that built anything**",
and AC7a (`spec-11:229-232`) requires a `SPECCED`→`CLOSED` move plus a rev bump to return 0. The
bullet is the line a builder reads when arming the security-relevant half, and it is the live path: a
promoted unit under `-1`'s S8 is authored SPECCED and closed CLOSED inside one run. The bullet's
"edits an existing unit's id" clause survives the rewrite — a renamed id removes a BASE id.

**H11 · id 44 — AC2 pins a count the corpus does not have.**
Replaying the shipped `unit_rows` selector over `memory/builds/aBranchedMandate/README.md` reproduces
13 and 7 exactly. Restricting to rows whose link target is under `spec/` — which is what
`gen:build-units` will hold — gives SIX rows, all CLOSED, corroborated by
`memory/builds/aBranchedMandate/RUN.md:12` and by that README's own generated status line. An arm
written to `spec-11:213-214`'s 4 fails against a correct implementation. The 4 is
`memory/builds/aDeclaredCeiling/RUN.md`'s number, which is also what makes `spec-11:135-137`'s "six
ids each" wrong for the second frozen fact.

**H12 · id 60 — `-14`'s range measurement is false in its load-bearing half.**
`grep -lE '[0-9a-f]{7,40}\.\.\.?[0-9a-f]{7,40}' memory/builds/*/reviews/*.md` returns ELEVEN records
naming a `sha..sha` range, so `spec-14:25`'s "none names a usable tip" is refuted, and it is the
stated reason a later round learns nothing. What is true and still motivates S4: the harness default
at `tools/workflows/tier2-review.js:66` writes the literal `HEAD`, so a harness-written record pins a
moving ref. The count is separately unreliable — the spec says 25, the audit it derives from says 7
(`memory/builds/aBoundedVerdict/build/2026-08-18-research-TOOL-aBoundedVerdict-1-close-path-audit.md:231`),
and my measures give 11 sha-tipped and 28 carrying a `..HEAD` token.

**H13 · id 62 — S6's authority assumption does not hold under this repo's declared anchor.**
`spec-11:180-182` rejects freezing the scope in the run-state file because that file is inside the
subject's reach, and keeps the BASE blob as the authority — without stating that the BASE blob has
the same property here. `.unattended.conf:89` declares `ANCHOR_SCOPE="published"`, and its own
comment says roster integrity stops being enforceable on the branch anchor;
`memory/guides/UNATTENDED-PROTOCOL.md:32-35` says the same for the authored roster. As written S6
reads as closing the self-certification hole on this repo when it closes it only on the
default-branch anchor.

**H14 · id 63 — the planning verb and the classification table give two answers.**
Extracting the awk from `plan_state` (`tools/unattended/unattended.sh:857-878`) and replaying it over
all fourteen specs prints FORKED for every one, because `memory/guides/BUILD-METHOD.md:36` defines
FORKED as an unresolved §8 item and twelve specs leave at least one. `README:222-227` says READY for
`-2`, `-3` and `-4`. FORKED is not a stall — `memory/guides/BUILD-METHOD.md:43` routes it to M3 — so
the defect is the disagreement, not a deadlock: resolve the mechanism-only forks, or say in the table
that these units are FORKED-by-design and what the verb prints.

**H15 · id 74 — a fork resolved against an OPEN row about the same check.**
`memory/backlog/TOOL.md:71` (`TOOL-cSettledDocket-11`) is OPEN and names this exemption exactly, with
the opposite remedy: scope it to emptiness alone. `tools/unattended/check-unattended.sh:322` clears
`rd` for any terminal phase, and the guard at `:323` gates both the malformed-marker `fail 8` at
`:325` and the emptiness one at `:327`. `spec-18:175` resolves "stays" weighing only the emptiness
half, which leaves the malformed-marker half exempt forever; no spec in the set cites the row. This
build's own `spec-11:22-24` argues the identical class.

**H16 · id 75 — a landed append-only decision row is reversed and never named.**
`memory/DECISIONS.md:63` carries `-1`'s two-round FILE CONSTANT and is present at the declared base;
`README:198-208` withdraws that design outright, and no spec under the build folder cites the row.
The convention exists in the same file at `memory/DECISIONS.md:19-20` ("Reverses aWidenedGuide-1
knowingly", plus a "Falsifies:" list). The sibling gap is `memory/DECISIONS.md:64`, which fixes the
halt code as the region's EIGHTH fact — a figure that itself needs re-measuring against the
eleven-fact pin before any close-out row is written.

**H17 · id 76 — half a backlog row silently closed, half left unowned.**
`memory/backlog/TOOL.md:81` (`TOOL-aBoundedVerdict-10`) is OPEN, is this build's own reserved id,
names `-13`'s mechanism verbatim, and names TWO fixes: the driver bound and a per-leg deadline in
`run-gates.sh`. `-13` delivers the first and cites only `TOOL-aBranchedMandate-3` (`spec-13:47`); no
spec in the set carries the second, and `README:191-193` enumerates seven other rows but not this
one. The row's traced 240s hang wedging the bar at 46/65 is also stronger evidence than the
blackhole-IP reproduction `-13`'s §4 rests on.

**H18 · id 78 — the opt-in-by-presence hole survives S6.**
`tools/unattended/unattended.sh:731` guards the comparison on the marker's presence at BASE, under a
comment saying a build without the markers is authorized on existence alone. S6 keeps the BASE-blob
shape and says nothing about a BASE carrying no `gen:build-units` pair — which is every BASE before
S5's migration render, every adopter tree, and any run pinned earlier. An empty BASE set makes
BASE ⊆ HEAD vacuously true, while `spec-11:124` promises the opt-in goes away. AC7 covers append and
delete, AC7a covers a re-render; none covers absence, and `spec-11:110-113`'s declared non-catch is a
different limit.

## 3. The four-axis cross-read

### Scope

Agreed: every unit carries a §3 non-goals section, and in most cases work handed away is handed to a
named sibling that owns it — `spec-19:31` routes the roster bullet to `-11`, `spec-3:281` routes
`--attest` to `-15`, `spec-12:46` routes the closing-review join to `-16`.

Did not agree, and this is where the set leaks: one mechanism the build names as its headline is
owned by nobody (18 — `build-complete`'s authored-roster terms); one is owned twice with two
different failure-mode sets (29 — `spec-12:25` against `spec-16:28`); one hand-off lands in a
Files-touched list and in no scope item or AC (30 — `spec-11:161`); `README:226` assigns `-3` two
mechanisms its own spec disclaims (26, 82, 54); the manifest re-stamp obligation is asserted for five
units and carried by four while seven further units take a watched path (32, 50, 69); `README:104`
and `README:182` still describe the withdrawn five-unit build (34, 71); and half of
`TOOL-aBoundedVerdict-10` has no owner (76). `-5`'s Goal (23, `spec-5:9`) states a premise the
shipped driver falsifies, so its scope statement describes work already done.

### Interface

Agreed: the halt-code conf keys (`HALT_CODES_EXTRA`, `HALT_FLOOR`) are spelled identically in `-2`
and read the same way by `-1`; the `--attest` verb name is spelled the same in `spec-15:18`,
`spec-5:65` and `spec-3:281`; and `core_of` (`tools/unattended/check-unattended.sh:65`) is the agreed
seam for the leg to read driver constants, used consistently by `-1` and `-2`.

Did not agree: the authored-region fact count is spelled four ways across `-2` and the README against
a live value of eleven (19); the park verb's kind is `park` in the spec and `decision` in the driver
(22, 77) and its taxonomy omits a live kind (24, 79); the shared read-path budget has three values in
three documents (27); the leg's `ls-remote` population is inverted (33, 16, 84); a waiver registry
path is spelled where no file exists (36, 72); and the harness's binding line is described as
existing-but-kindless when it does not exist (7, 59, 81).

### Ordering

Agreed: `-11` is first, and the units that read the region it moves — `-12`'s `build-complete`
messages, `-16`'s closing-review predicate — follow it. `README:235` declares `-12` and `-13`
independent and nothing in either spec contradicts that.

Did not agree: `-5` at position 5 and `-3` at position 9 both declare a dependency on `-15` at
position 10 (28, 51, 68), against `README:100` and `memory/guides/BUILD-METHOD.md:53`. `-15` depends
on nothing in the set, so the reorder is free. Separately, the order paragraph itself reads its
positions against the withdrawn five-unit roster (34, `README:104-107`), so unit numbers 1, 2 and 3
in that prose name the wrong specs while 4 and 5 still coincide — the shape most likely to be
misread.

### Acceptance

Agreed: most ACs name a command and an observable rather than a judgement; `spec-11:229-232`'s
AC7/AC7a pair arms both directions of the id-set rule; and `spec-2`'s AC6 states its predicate in the
complement form a prefix grep cannot fake, which is the model the rest of the set should follow.

Did not agree: an AC promises a green bar over a population measured wrong (21); one is blind to the
value it polices (20, 3); one is green before the unit is built (48); one names a file that does not
exist (36, 72); one asserts a count a correct implementation will not produce (31, 44, 80); one
cannot express its claim through the command it names (47); one observes nothing once the commit
lands (53); one is unreachable from its own scope item (41); a scope item is a question with no
criterion (45); and the whole of `-2`'s S10 has no criterion at all (25, 46). The sharpest signal the
cross-read produced is that scope and acceptance fail together: 18, 25 and 45 are each a mechanism
whose absence from the AC set is what let the scope gap survive rev-6.

## 4. REFUTED

- **13** (`spec-1:106`, BLOCKED counted 38 not 36) — already fixed: the file is at rev-7, `spec-1:108`
  reads 36, and `spec-1:400-405` records the correction naming the two absorbed section headings.
- **52** (`spec-13:188`, AC5 cites a missing scope item and AC8's fixture is unbuildable) — the
  referent is §5's testing bullet at `spec-13:167-169`, which names exactly that arm; and AC8 needs
  no HTTP server, since a delaying local transport is hermetic and buildable.
- **57** (`spec-1:152`, the per-subject runaway ceiling cannot bound the promotion chain) — the spec
  states the limit itself at `spec-1:141-154` ("not proven by construction") with F4 raised to the
  OWNER, and under S5 a fold-scoped closing round's subject is the build slug, so the ceiling does
  bound it.
- **58** (`spec-1:134`, the dClosedLexicon replay is a cross-subject filename join with two countless
  rounds) — re-measured: "1, 1, 2, 1, 2" reproduces exactly on records 3-7, only one round lacks a
  count, and a retrospective measurement in a design section is not the mechanism `spec-1:88-90`
  refuses.

## 5. UNVERIFIED — OUTSTANDING

None. Every raw finding reached a confirmed or refuted disposition this round, and coverage was
clean: 0 dead lenses of 5, 0 dead skeptic batches of 5, 0 contradictory, 0 spurious. That is a
property of this round's batches only — an empty outstanding set is not a claim that the unexamined
surface in §6 is sound.

## 6. What this audit did NOT cover

- **The implementation.** Nothing in this build is built. Every claim about behaviour is a claim
  about the shipped `tools/unattended/unattended.sh`, `tools/unattended/check-unattended.sh` and
  `tools/workflows/tier2-review.js` as they stand at HEAD, read against the specs; no specced change
  was executed, so no AC was run as an AC.
- **The gate.** `bash tools/run-gates/run-gates.sh` was not run, nor any single leg. Where a finding says a
  unit "reds the bar", that is derived from the leg's source, not observed from a run.
- **Ids `TOOL-aBoundedVerdict-6` through `-10`.** These are not specs in this set. `-10` is an OPEN
  backlog row (`memory/backlog/TOOL.md:81`) and was read only as prior art for `-13`.
- **The design record and the research records** under `memory/builds/aBoundedVerdict/build/` were
  read only where a spec cites them; they were not audited as records in their own right, so a defect
  living only there is unreported except where it propagated into a spec.
- **Prose correctness below the structural level.** Findings key on measurable claims — counts,
  paths, line refs, call sites, populations. A fluent paraphrase that is subtly wrong about intent
  passes this audit, exactly as `tools/check-playbook-parity.sh`'s own header says of itself.
- **Kit/dogfood byte parity** for the protocol and template pairs, `memory/HYGIENE.md` against
  `tools/memory-tree/HYGIENE.template.md`, and the rendered Skills. Findings 19 and 25 touch those
  carriers; neither was checked for render parity.
- **`memory/backlog/*.md` completeness.** Rows were read where a finding named one; the backlog was
  not swept for further rows this set supersedes, so 74, 76, 81 and 85 are a floor, not a total.
- **Node scope.** Everything was measured on node `c`'s worktree at this HEAD. Finding 70's
  credential observations are node-specific by construction and were not reproduced here.
