**Serves:** diff-review TOOL-aShelvedLeg-1 TOOL-aShelvedLeg-2

# Closing diff review, round 1: aShelvedLeg unit 2, the closing review's minors on the held kit gate

2026-11-11 · Tier-2 · on `branch/clever-babbage-44839c` · adversarial fan through `tier2-review.js`: 5 finder lenses (gov-diff-reviewer), 4 skeptic batches (gov-skeptic), then this synthesis (gov-synthesizer). The subject is the cumulative diff landing on main.

**Reviewed range:** `13b83e12a86e1e7802e12f261233b9a421daf5d1...2f004093efd06de4612d8c5e103bb18559deed43`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

Nothing blocks the landing. There are two items: one MEDIUM and one LOW. Both are prose defects with no effect on behaviour. The MEDIUM one matters more than its effect suggests, because a CLOSED spec now certifies a rewording scope that the unit did not meet. Fold both fixes before the close.

## Review shape

Intensity full, raw 4, confirmed 4, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| verification | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 2 items, 1 MEDIUM and 1 LOW. By raw confirmed finding: 4 findings, 1 MEDIUM (id 3) and 3 LOW (ids 1, 2, 4). Blockers 0, highs 0. Every finding keeps its binding grade.

### Run integrity

- Lenses: 5/5 returned, 0 DIED. Skeptic batches: 4/4 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified. 0 orphaned duplicate refutations demoted to unverified. 0 duplicate refutations counted as merged confirmations. 0 spurious verdicts discarded. 0 duplicates.
- Fixes on confirmed findings: 2 judged SOUND, 0 judged UNSOUND, 2 judged INSTANCE-ONLY, 0 with no fix proposed, 0 NOT JUDGED. An INSTANCE-ONLY fix cures the cited instance and leaves its class standing. An unjudged fix would be the finder's proposal and nothing more.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, so none is bound at the finder's grade. 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: neither `specs` nor `context` was supplied. The lenses had only the range's commit messages.
- Checklist: 67 items, acquired by the harness from `--for-diff 13b83e12a86e..HEAD`. Each went to exactly one lens: security 14, correctness 14, seams 13, verification 13, intent 13.
- By design: 1 invariant from the checklist's by-design block.
- Refuted findings shown: 0. Same-address pairs shown: 0. No twins to flag.
- Dispositions: unclassed refuse. 67 class slugs were handed in, and 149 leg names were read from `tools/gate-legs.json`.
- Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Every count above is zero where it should be, so this run is complete.

## Items

### 1. MEDIUM: S1 is recorded as met, but the kit still says the held leg's checks run on every bar (ids 2, 3)

Ids 2 and 3 describe one defect from two lenses. Id 2 (verification, LOW) reports that the probe cannot see the population. Id 3 (intent, MEDIUM) reports that the closed unit certifies a scope it did not meet. Each keeps its binding grade, and the item takes the higher one.

- **What:** the spec `memory/builds/aShelvedLeg/spec/2026-11-10-spec-TOOL-aShelvedLeg-2.md` is marked CLOSED. Its S1 (line 22) says every sentence in the unattended kit's scripts that claims `check-unattended.sh` runs on every bar is reworded. Its §4 site table leaves out `tools/unattended/lib-unattended.sh`. Its probes (line 243) cannot reach that file: AC1 greps only `check-unattended.sh` and `check-unattended.test.sh`, and AC2 matches three fixed phrases in `run-unattended-gates.sh` and `unattended.sh`. `tools/unattended/lib-unattended.sh:2389` still says `read_spec_audit_ids` "exists because check 2 runs on every bar". Check 2 belongs to `check-unattended.sh`: its `fail 2` sites are at :830, :839, :860, :1253 and :1290-1307, and it calls `read_spec_audit_ids` at :1206. The skeptic on id 3 found a second instance of the class in a file this diff edits. `tools/unattended/unattended.sh:2997` bases an owner-accepted cost on "leg check 9 asserts the same facts independently on the bar", and check 9 also belongs to `check-unattended.sh` (`fail 9` at :2600, :2624, :2626).
- **Consequence:** since TOOL-aShelvedLeg-1, `kit.toml:255-264` has held that leg off every merge and push bar. So both sentences are false. The second one also leaves an accepted cost resting on a check that no automatic bar runs. AC1 and AC2 both pass, so the unit closed with S1 recorded as observed. A later reader may reason about cost or coverage on the belief that checks 2 and 9 run on every bar. Behaviour does not change.
- **Fix, id 3 (judged INSTANCE-ONLY by the skeptic; the class-level fix follows):** reword both sentences that attribute a `check-unattended.sh` check to a bar: `lib-unattended.sh:2389` (check 2) and `unattended.sh:2997` (check 9, whose accepted-cost bound no longer holds while the leg is held). Make the probe a grep over `tools/unattended/*.sh` that matches a numbered check of the held leg, or `check-unattended.sh` itself, named next to bar wording. For example: `grep -nE '(check-unattended|(leg )?check [0-9]+)[^.]*\b(on the|every) bar' tools/unattended/*.sh`. Pin its expected output. Do not widen the bare AC1 pattern. The finder's proposal cures only the cited instance: reword `:2389` in the same way as `check-unattended.sh:318`, and widen AC1's grep to `tools/unattended/*.sh`.
- **Fix, id 2 (judged SOUND by the skeptic):** reword `lib-unattended.sh:2389` to say where the leg runs now, for example "because check 2 walks every build whenever the leg runs". Widen AC1's grep to `tools/unattended/*.sh`, and list each kept sentence that names another leg as an expected exception (`check-playbook.sh`, `check-pass-order.sh` and the rest, including `lib-unattended.sh:1052`). These two fixes disagree on AC1. The class-level probe from id 3 is narrower, and it is pinned. It covers id 2's population without needing an exception list for the bare pattern. Use it, and reword `unattended.sh:2997` as well.
- **Left-shift gate:** put the pinned class-level grep into the spec's acceptance criteria. Also put it in a leg that runs on the bar, not in the held `unattended kit gate`, which no automatic bar runs. Add a checklist note to the `criterion-asserts-what-its-own-command-cannot-show` class: a criterion that claims "every X in <scope>" must read the whole scope with a glob, never a list of named files.

### 2. LOW: the changed-mode wording states a narrower selection rule than the runner has (ids 1, 4)

Ids 1 and 4 cite the same added sentences, and both say the prose leaves out the runner's other selection arms. They are one defect. Id 4's ref, `tools/unattended/kit.toml:444`, is wrong. The skeptic placed the sentence at `kit.toml:263-265`.

- **What:** this diff adds the sentence at `tools/unattended/README.md:424-426` and `tools/unattended/kit.toml:263-265`. It says `GATE_SELFTESTS=changed` "selects it by this kit's shipped sources only", so a records-only change "leaves it held". The new gotcha `memory/gotchas/changed-mode-selection-ignores-doc-reads.md` says the same thing in its frontmatter description (line 3, "alone") and in its "Where it bit" sentence. The runner's selection comment at `tools/run-gates/run-gates.sh:3071-3080` lists more cases where a held leg still runs:
  - its last-run record is missing, unreadable or not an ancestor of HEAD;
  - the record was earned under another manifest row;
  - the record is more than `GATE_SELFTESTS_MAX_LAG` first-parent commits behind HEAD (default 10, set at :3095);
  - the suite file changed.
- **Consequence:** the error is in the documentation only. A reader is told that changed mode never runs the kit gate after records-only drift, but the lag bound runs it once ten commits have passed. The advice the sentence gives, to run with the variable at 1 or through `--checks`, is still correct. The gotcha's "reads green" stays: it describes the overall run, and a held leg prints `GATE held` without failing the bar.
- **Fix, id 1 (judged INSTANCE-ONLY by the skeptic; the class-level fix follows):** use narrowed wording everywhere the diff makes the absolute claim. Suggested wording: "does not by itself select it; it stays held unless its last-run record is missing, unreadable or not an ancestor of HEAD, or lags more than GATE_SELFTESTS_MAX_LAG commits". The places are `README.md:424-425`, `kit.toml:263-265`, and the gotcha's frontmatter description and its sentence "A records-only change leaves it held under changed mode". The gotcha's "reads green" can stay. The finder's proposal cures only the cited instance: narrow the sentence in README and kit.toml, and change "reads green" to "holds it".
- **Fix, id 4 (judged SOUND by the skeptic):** write "selects it by this kit's shipped sources (and the runner's lag bound), never by the records its doc_reads names". Alternatively, drop "only" and keep the "never by doc_reads" clause, which is the point S3 needs to make. Apply it at the same three sites as id 1.
- **Left-shift gate:** no gate fits a paraphrase of a rule, so this goes into the project's bug-class checklist as `restated-rule-drops-its-other-arms`. When prose restates when a runner selects or skips something, quote or point to the runner's own comment (`run-gates.sh:3071-3080`) instead of narrowing it with "only" or "alone".

review-shape kind=diff-review round=1 intensity=full at=synth raw=4 confirmed=4 refuted=0 merged=0 unverified=0 blocker=0 high=0 medium=1 low=3 agents=10 out-tokens=34088
review-round round=1 limit=- prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/unattended/README.md:424 | low | low | confirmed | I checked this against the code. README.md:424-425 and kit.toml:263-265, both added by this diff, say a records-only change 'leaves it held' as if that always happens. The selection comment at run-gates.sh:3071-3077 says otherwise. Under GATE_SELFTESTS=changed a held leg still runs if it has no last-run record, an unreadable one, a non-ancestor or foreign-row one, or one more than GATE_SELFTESTS_MAX_LAG (default 10, set at line 3095) first-parent commits behind HEAD. So after a records-only change the kit gate can still run, and the sentence overstates the skip. This is wording only and behaviour is unchanged, so it grades low. The 'reads green' half of the finding is weaker. The gotcha says the overall run reads green, and that is accurate: line 4166 prints 'GATE held' for the leg, and a held leg does not fail the bar. It is not a claim about the leg's own line. | instance | - | new:restated-rule-drops-its-other-arms |
| 2 | verification | memory/builds/aShelvedLeg/spec/2026-11-10-spec-TOOL-aShelvedLeg-2.md:243 | low | low | confirmed | I checked this against the code. tools/unattended/lib-unattended.sh:2389 still says read_spec_audit_ids exists 'because check 2 runs on every bar'. Its check-2 caller is check-unattended.sh:1206. kit.toml:255-264 marks that leg as 'HELD BY OWNER RULING, 2026-11-10 ... no merge or push bar runs it', so the sentence is false. The sentence was already in the base file at the same line, but S1 was added by this diff. S1 (spec line 22) covers 'every sentence in the unattended kit's scripts', and lib-unattended.sh is one of those scripts. AC1 greps only check-unattended.sh and check-unattended.test.sh, and AC2 only run-unattended-gates.sh and unattended.sh, so neither one reaches this file. Running AC1's regex on lib-unattended.sh finds line 2389. It also finds line 1052, which describes a different leg and is correctly kept. So the diff records S1 as observed while one sentence in its population is still unchanged. The only effect is a misleading comment, so the grade is low. | sound | - | class:criterion-asserts-what-its-own-command-cannot-show |
| 3 | intent | tools/unattended/lib-unattended.sh:2389 | medium | medium | confirmed | I checked this against the code. The comment at tools/unattended/lib-unattended.sh:2389 says 'It exists because check 2 runs on every bar'. Check 2 belongs to check-unattended.sh: its `fail 2` sites are at :830, :839, :860, :1253 and :1290-1307, and it calls read_spec_audit_ids at :1206. TOOL-aShelvedLeg-1 held that leg off every automatic bar, so the sentence is false. The line is unchanged since base, but the diff is where this becomes a defect. The diff adds the spec memory/builds/aShelvedLeg/spec/2026-11-10-spec-TOOL-aShelvedLeg-2.md, marked CLOSED. Its S1 says 'Every sentence in the unattended kit's scripts' that says the leg runs on every bar 'is reworded'. Its §4 table of sentence sites leaves out lib-unattended.sh. AC1's grep reads only check-unattended.sh and its .test.sh, and AC2's grep reads only fixed phrases, so neither can see this line. The closed unit therefore certifies a scope it did not meet. That is the intent-lens defect the finder describes, and the stale wording is now attested by a closed spec. The effect is contained to a comment that misleads, with no behaviour change, so medium. The same class has a second instance in a file this diff edits. tools/unattended/unattended.sh:2997 rests an owner-accepted cost on 'leg check 9 asserts the same facts independently on the bar', and check 9 is check-unattended.sh's (`fail 9` at :2600, :2624 and :2626). That leg no longer runs on any automatic bar, so the bound that sentence relies on is now false too. | instance | amendment-leaves-its-other-half-standing | class:amendment-leaves-its-other-half-standing |
| 4 | intent | tools/unattended/kit.toml:444 | low | low | confirmed | The line numbers are off, but the claim holds. The sentence the diff added is at tools/unattended/kit.toml:263-265, not :444, and at tools/unattended/README.md:424-426. Both say GATE_SELFTESTS=changed 'selects it by this kit's shipped sources only'. The gotcha changed-mode-selection-ignores-doc-reads.md:3 says 'alone'. The runner's own header comment in tools/run-gates/run-gates.sh (around 3071-3080) lists more ways a held leg gets selected: a missing, unreadable or non-ancestor last-run record; a record earned under another manifest row; a record more than GATE_SELFTESTS_MAX_LAG first-parent commits behind HEAD; and a change to the suite file, which is in the selection set. So 'only' is narrower than what was built. The effect is on documentation alone. The practical advice (run at 1 or through --checks) is still right. | sound | - | new:restated-rule-drops-its-other-arms |
