**Serves:** diff-review KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105

# Tier-2 closing diff review — aMendedFleet, ROUND 1

Produced by the `tools/workflows/tier2-review.js` harness on 2026-10-06: five finder lenses, five
skeptic batches, one synthesis pass. Subject: the cumulative diff landing on main.

**Reviewed range:** `7af5f564641d231f8b78f6b183dde1b6bf53111d...e83b29b66b7b4474afe9c8e5f46434f8b8253cbf`
(307 commits). **ROUND: 1.**

## Verdict: CLEAN WITH FIXES

No blocker survived verification. One HIGH finding does: the new BASELINES shrink-only guard in
drift-audit can be escaped by moving a baselined signal to PINS (finding 1). It defeats a ratchet
that claims to have no escape, so it should be fixed before this range lands rather than filed. The
ten MEDIUM and six LOW findings are contained, and each can land as a follow-up fix.

## Review shape

- Intensity full. Raw 21, confirmed 17, refuted 4, unverified 0 (0 uncertain). Precision 0.81.
- Adjudicated tally by RAW confirmed finding: blocker 0, high 1, medium 10, low 6.
- Adjudicated tally by ITEM in the table below: blocker 0, high 1, medium 7, low 4 (12 items).
  Items merge findings of one binding grade only. The ids each item covers are listed with it.
- Intent input: 104 spec documents supplied as `specs`, beside the range's commit messages.
- Checklist: 89 items, each assigned to exactly one of five lenses. Security 18, correctness 18,
  seams 18, verification 18, intent 17.

## Run integrity

- Lenses: 5/5 returned, 0 died. Skeptic batches: 5/5 returned, 0 died.
- 0 contradictory verdicts demoted to unverified. 0 spurious verdicts discarded. 0 duplicates.
- Fixes on confirmed findings: 14 judged sound, 3 judged UNSOUND (findings 1, 4 and 19), 0 with
  none proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 4 RE-GRADED by the skeptic (findings
  15, 19, 20 and 21). The skeptic's grade is the binding one in each case.
- Unverified findings: 0 answered uncertain, 0 with no usable verdict.
- Lens notes were supplied for all five lenses: security, correctness, seams, verification, intent.

Every counter above that could mark the run incomplete is zero, so this run is complete. The empty
blocker set is therefore evidence from a full fan, not an artifact of a dead lens.

## Findings, severity-ranked

### HIGH

**H1 — finding 1 (security) — [tools/drift-audit/drift_report.py:432](../../../../tools/drift-audit/drift_report.py)**

The BASELINES shrink-only guard only iterates the signals that the head's own BASELINES still lists
(`build_baseline_findings`, lines 400-443), and it returns `[]` at line 402 when the head dict is
empty. A branch can delete `BASELINES["closed_specs_with_no_product_commit"]` and add
`PINS[...] = 50`. Nothing compares that signal against the base. The both-declared refusal only
fires when a signal is in both places. RATCHETS no longer has a row for either key, and
`ratchet_findings` skips a key the base does not hold. So `drift-audit records --check` passes and
new offenders up to the pin stay green, which contradicts the "no escape" comments in
drift_report.py and drift_signals.py. It takes a deliberate governance-layer edit, but that is
exactly the edit an agent makes to clear a red `new` offender.

- **Fix (the finder's proposal was judged UNSOUND; this is the skeptic's corrected fix):** pass the
  head PINS into `build_baseline_findings` and drop the `if not baselines: return []` early exit. For
  each signal in `old_sets` that the head BASELINES does not list, report WEAKENS only when the head
  PINS declares that signal with a count above `len(old_sets[sig])`. Add a selftest arm that moves a
  baselined signal to PINS at a larger count and expects red.
- **Left-shift gate:** that selftest arm is the class gate for the move. Also add an arm that empties
  BASELINES entirely while the base held entries, and expects red. Stage both breaks against the
  current code and observe RED before landing the fix.

### MEDIUM

**M1 — findings 9, 10 and 19 (seams, seams, intent) — the `Plan` judge default broke the resume contract that every deferral message still promises**

Unit 93 made `Plan` the default `workerType`, and a Plan judge writes no lens or verify file. The
harness logs once that results are not durable, but every other reader still promises a cheap
resume:

- [tools/workflows/tier2-review.js:1467](../../../../tools/workflows/tier2-review.js) and line 1516:
  the synthesis-died log and note say the confirmed findings are on disk and a re-run "dispatches
  only the synthesis", with `pending: ['synth']`.
- The same file at lines 888, 1181 and 1209: the partial-fan notes say a re-run will "dispatch
  only" the dead labels. [tools/workflows/tier2-review.template.js:182](../../../../tools/workflows/tier2-review.template.js)
  carries the same default and the same strings.
- [tools/unattended/VERBS.template.md:603](../../../../tools/unattended/VERBS.template.md) lines
  603-604, rendered to `memory/guides/UNATTENDED-VERBS.md:604`, says every returned agent's result
  is on disk and to re-run once.
- `tools/workflows/unattended-build.js` (and its template) calls tier2-review with no `workerType`
  for the spec audit, so it gets the non-durable default. Its deferred-platform comment (886-890)
  and its `next` text (template line 916) still say the remedy is cheap. `unattended.sh:6646`,
  STOPS step 8 and `memory/map/features/review-harnesses.md:66` say the same.

Under the default, a re-run after any deferral dispatches every finder and skeptic again at full
cost. A run sized to "retry once" is likely to hit the same session or usage limit and go to a hold.
No wrong result ships and no data is lost, which is why this is medium. Finding 19 was graded high
by its finder and re-graded medium by the skeptic, and the medium grade binds.

- **Fix for findings 9 and 10 (judged SOUND):** when `workerType` names a type, make each deferred
  `note` and the synthesis-died log say nothing was written and a re-run dispatches every judge. Set
  `pending` to every judge label plus `synth`, or add `durable:false` to every return. Keep the
  current wording only on the `workerType: 'none'` path, and mirror the change into
  tier2-review.template.js. For the unattended callers, either pass `workerType: 'none'` from
  unattended-build.js's tier2-review call and from the documented unattended review call so those
  runs stay resumable, or rewrite VERBS.template.md:603-604 (and re-render UNATTENDED-VERBS.md), the
  unattended-build.js comment and the review-harnesses card to say a default-type re-run repeats every
  judge.
- **Fix for finding 19 (the finder's proposal was judged UNSOUND; this is the skeptic's corrected
  fix):** make the deferred-platform and synthesis-died notes in tier2-review.template.js depend on
  `workerType`, so that under a named type they say a re-run dispatches every finder and skeptic
  again, and never "dispatch only <pending>". Pass `workerType: 'none'` from unattended-build's
  spec-audit call, so its `next` relaunch text, unattended.sh's relaunch line and STOPS step 8 stay
  true. If Plan is kept there instead, reword those texts to say the re-run is a full re-dispatch.
  Add a tier2-review.test.sh arm that asserts the deferred note's wording under the default
  `workerType` and under `'none'`.
- **Left-shift gate:** the tier2-review.test.sh arm above, asserting the deferral note text under both
  worker types. Add a check that greps every "re-run … only"/"on disk" claim in the unattended
  templates against the effective `workerType` at that call site. This is the
  amendment-leaves-its-other-half-standing class, so add a §10 checklist line too: "a change to a
  durability default re-reads every resume promise".

**M2 — finding 6 (correctness) — [tools/unattended/unattended.sh:7318](../../../../tools/unattended/unattended.sh)**

With `LIVE_LANDED_UNCLOSED=1`, which this repo arms, the LIVE.md render reads tracked product source
through drift-audit's `git grep` over the working tree, plus drift_report.py and drift_signals.py.
The dirty-input inventories in `write_ask_views` (lines 7318-7333) and `write_run_record` (lines
11224-11227) only look under the memory root, `.memory-tree.conf` and the generator's own directory.
Under `LANDER_MODE=primary`, `--close` does not refuse a dirty tree. So an unstaged edit under
`tools/`, `skills/` or `.claude/` that adds or drops a citation of a non-terminal id changes LIVE.md's
Landed-unclosed count, and the helper stages a view the index does not support. The pre-commit
freshness check renders from the same worktree, so it agrees with the stale view. The damage is one
count that the next clean render corrects.

- **Fix (judged SOUND):** when the conf sets `LIVE_LANDED_UNCLOSED=1`, add drift's `EVIDENCE_GLOBS`
  (or every unstaged tracked path) and the resolved drift-audit kit directory to the dirty-input test
  in both helpers. Better still, have gen_build_index.py expose its input pathspecs so the two
  helpers and the generator share one inventory.
- **Left-shift gate:** a unattended.test.sh arm that arms `LIVE_LANDED_UNCLOSED=1`, leaves an unstaged
  citation edit under `tools/`, runs the helper, and expects a refusal. A single generator-owned
  pathspec list makes the next new input impossible to miss.

**M3 — finding 5 (correctness) — [tools/memory-tree/check-verdict-epoch.sh:187](../../../../tools/memory-tree/check-verdict-epoch.sh)**

The epoch legs now take `GATE_PUSH_BASE` as their base. On a push that creates the default branch,
`.githooks/pre-push:1450` exports it as all zeros, and neither consumer treats that as "no base".
check-verdict-epoch.sh fails `git cat-file -e 0000…^{commit}` and exits 2, and `govkit.py epoch`
(lines 12370-12371) prints "FAILED · no base to compare against" and exits 1. An adopter's first push
to a fresh remote is refused. Before this diff both legs fell back to the merge-base. The hook already
guards the all-zero case for `GATE_ATTRIBUTE` (line 1380) and for the merge-loss block (line 733).
`--no-verify` escapes it, so the effect is contained.

- **Fix (judged SOUND):** treat an all-zero `GATE_PUSH_BASE` as unset in both consumers. In the
  shell, `case "${GATE_PUSH_BASE:-}" in ''|*[!0]*) ;; *) GATE_PUSH_BASE= ;; esac` before line 187.
  In govkit, `if base is None and os.environ.get("GATE_PUSH_BASE", "").strip("0"):`. Alternatively,
  export `GATE_PUSH_BASE` only when `${main_remote//0/}` is non-empty.
- **Left-shift gate:** an arm with `ARM_GPB=0000000000000000000000000000000000000000` in
  check-verdict-epoch.test.sh and in the govkit selftest, expecting the merge-base fallback. Fixing
  this at the hook export, so that every reader inherits it, gates the class rather than two
  instances.

**M4 — finding 7 (correctness) — [tools/memory-tree/check-verdict-epoch.sh:271](../../../../tools/memory-tree/check-verdict-epoch.sh)**

TOOL-aMendedFleet-65 now mints the kit version inside the prepared merge (push-main.sh,
`commit-tree` with parents R and oldb, lines 638-652). This bump search moved to
`--diff-merges=first-parent` so it can see such a merge. The other reader was not amended:
`tools/memory-tree/hygiene-parity.test.sh:67` still runs `git log -S"KIT_MEMORY_TREE_VERSION=$KITV"`
with no diff-merges option. Pickaxe does not diff merges by default, so after any `--prepare` landing
that mints memory-tree, `FLOOR` comes back empty. The harness then exits 2 with the misleading
"shallow clone or squashed import" reason. It is a manual tool that refuses loudly rather than giving
a wrong answer.

- **Fix (judged SOUND):** add `--diff-merges=first-parent` to the `git log -S` at
  hygiene-parity.test.sh:67, matching check-verdict-epoch.sh:271. Then grep for every other
  `log -S`/`-G` reader of a kit version constant and amend it the same way.
- **Left-shift gate:** a lint over tracked scripts that refuses `git log` with `-S` or `-G` on a
  `KIT_*_VERSION` pattern unless it also passes `--diff-merges`. Running that predicate over the tree
  is also how to find the remaining readers.

**M5 — finding 3 (security) — [tools/unattended/unattended.sh:2336](../../../../tools/unattended/unattended.sh)**

`check_cross_run_overlap` lists this run's own paths with
`git diff --name-only "$anc...HEAD"` and no `--no-renames`. A file this run renamed is listed only
under its new path. If another unmerged ref edits the old path, the join finds no shared path, and
the probe prints "no shared path" at `--preflight` and in the kickoff card's `overlaps —` cell. That
is a false clean result for exactly the conflict a rename causes. Every other diff read in this unit,
including the `theirs` read at about line 2367, passes `--no-renames`. The probe is advisory and
always returns 0, which contains the effect.

- **Fix (judged SOUND):** add `--no-renames` to that diff, so a rename lists both its source and its
  destination.
- **Left-shift gate:** an `--overlaps` arm where this run renames `a.sh` to `b.sh` and a second ref
  edits `a.sh`, expecting `a.sh` to be reported. A class check is to grep every
  `diff --name-only` in the unattended kit that feeds a path join and require `--no-renames`.

**M6 — findings 12 and 15 (verification) — assertion floors not raised for the arms this diff added**

- [tools/unattended/unattended.test.sh:12763](../../../../tools/unattended/unattended.test.sh)
  (finding 12): the floors (`FLOOR_ASSERTIONS=1902`, `FLOOR_SHARD_1=234`, `FLOOR_SHARD_2=1680`) were
  raised only for the -60 and KICK-2 blocks. Six other added blocks moved no floor. In region one
  these are -61 (line 1308, about 20 assertions) and -63 (line 1595, 11). In region two they are -66
  (9349, 2), -83 (9369, 2), -49 S8 (9783, 2, behind a SKIP branch) and -9 (11719, 16). About 50
  executed assertions sit above every floor.
- [tools/workflows/tier2-review.test.sh:1298](../../../../tools/workflows/tier2-review.test.sh)
  (finding 15): `FLOOR_ASSERTIONS` rose 180 to 183 for -17 and -18 only. The workerType block (lines
  296-324) executes 12 `ck()` calls with no floor raise. The finder graded this low and the skeptic
  re-graded it medium, and medium binds: the uncounted arms guard the same `workerType` behaviour
  behind M1.

Either block can be deleted or stranded behind an early exit and the suite still passes its floor in
every mode, which is the exact class the floor exists to catch. No wrong result ships, so the effect
is contained to the guard.

- **Fix for finding 12 (judged SOUND):** count each block's hit/miss/same/n++ lines. Raise
  `FLOOR_SHARD_1` by the region-one blocks (-61, -63), `FLOOR_SHARD_2` by the region-two blocks (-66,
  -83, -9, plus -49 S8 net of its SKIP), and `FLOOR_ASSERTIONS` by their sum. Add one RAISED comment
  line per unit, as the -60 block has.
- **Fix for finding 15 (judged SOUND):** raise `FLOOR_ASSERTIONS` to 195, with a RAISED line naming
  the 12 workerType assertions.
- **Left-shift gate:** a merge-bar check that diffs each suite against the base, counts added
  assertion-call lines, and reds when the suite's floor constant moved by less than that count without
  a recorded reason. That gates the class across every suite, including the LOW floor items in L2.

**M7 — finding 21 (intent) — [memory/builds/aMendedFleet/spec/2026-10-04-spec-KICK-aMendedFleet-1.md:3](../spec/2026-10-04-spec-KICK-aMendedFleet-1.md)**

KICK-1, KICK-2 and KICK-4 are graded Tier-1. The tier rule at
`memory/guides/SESSION-KICKOFF.md:203-205` assigns Tier 2 to a new or changed kit contract and to a
cross-kit change. KICK-2 is the clearest case. Commit 481eb9f39 adds an `--overlaps` flag to
unattended.sh with a new usage line, a new branch and a new README contract paragraph, and adds the
`overlaps —` card cell to manifest-check.sh in the same commit. KICK-1's card cell parses the
drift-audit kit's `drift-history.tsv` header contract. Because the hygiene gate skips Tier-1 headers,
the section canon and the CLOSED Tier-2 acceptance-ledger join never run on these specs. The build
README lists all three under "Ids no record names", so their AC observations exist only in commit
prose. The finder graded this low and the skeptic re-graded it medium, and medium binds: shipped
behaviour is unchanged, but a governance join is skipped for real kit-contract changes.

- **Fix (judged SOUND):** re-grade KICK-1, KICK-2 and KICK-4 as Tier-2 with a rev bump, and add the
  acceptance-ledger record each Tier-2 unit owes, carrying the observations already in their commit
  messages. Alternatively, record in each spec why the card cell falls outside the tier rule's
  kit-contract and cross-kit clauses.
- **Left-shift gate:** a hygiene check that reds a Tier-1 spec whose unit's commits touch files under
  two different kit directories, or add a usage line to a kit's CLI, unless the spec carries a
  recorded tier waiver.

### LOW

**L1 — finding 4 (security) — [tools/push-main.sh:544](../../../../tools/push-main.sh)**

`check_merge_losses` and `run_minter` locate the kit relative to `$self_dir`'s repository
(`resolve_kit_dir`, lines 521-522), but run `$top/$dir/<file>`, where `$top` is the cwd's toplevel
(line 99). When the lander comes from one checkout and runs against a tree without the kit at the same
relative path, python exits 2 for the missing file. check_merge_losses reads that as a DEAD PROBE and
continues, and run_minter reports "the version minter REFUSED", so the landing is blocked for the
wrong reason. The pre-push hook gets this right and grades the range again.

- **Fix (the finder's proposal was judged UNSOUND; this is the skeptic's corrected fix):** before
  running, test `[ -f "$top/$dir/lexicon.py" ]` (and `[ -f "$top/$dir/govkit.py" ]` in run_minter).
  When the file is missing, print the existing "no lexicon kit / no govkit deployer beside this
  lander" skip line and return 0, so python's exit 2 for a missing file is never graded.
- **Left-shift gate:** a push-main.test.sh arm that runs the lander from a checkout with the kit
  against a tree without it, and expects the skip line rather than DEAD PROBE or REFUSED.

**L2 — findings 14, 16 and 17 (verification) — floor comments and floors that miscount**

- [tools/unattended/unattended.test.sh:12761](../../../../tools/unattended/unattended.test.sh)
  (finding 14): the floor comment says the KICK-2 `--overlaps` block has 10 assertions, but the
  block at line 783 executes 9. `FLOOR_SHARD_1` (234) and `FLOOR_ASSERTIONS` (1902) each pin one
  assertion that does not exist. Today this is masked by the unpinned -61 and -63 arms.
- [tools/runlog/selftest.py:321](../../../../tools/runlog/selftest.py) (finding 16):
  `ASSERTION_FLOOR` rose 1543 to 1554 for -58 only. `test_extract_ready` (-70, line 1977) adds 4
  checks plus 3 decoy checks with no floor raise.
- [skills/session-kickoff/manifest-check.test.sh:1377](../../../../skills/session-kickoff/manifest-check.test.sh)
  (finding 17): `FLOOR_ASSERTIONS` 180 to 207 counts the overlaps cell (+8) and the cli cell (+19).
  The KICK-1 drift-cell block adds 5 `run_card` and 4 `check_eq` assertions that no floor line counts.

These are graded low because they miscount a guard, or leave one arm block outside it, with no
effect on behaviour today.

- **Fix for finding 14 (judged SOUND):** correct the comment to 9 and lower each raise by one
  (`FLOOR_SHARD_1` 233, `FLOOR_ASSERTIONS` 1901), or fold the correction into M6's recount.
- **Fix for finding 16 (judged SOUND):** raise `ASSERTION_FLOOR` to 1561, with a RAISED line counting
  `test_extract_ready`'s 4 checks plus its 3 decoy checks.
- **Fix for finding 17 (judged SOUND):** add "+9: the drift cell's arms (KICK-aMendedFleet-1)" and
  set `FLOOR_ASSERTIONS=216`.
- **Left-shift gate:** the floor-delta check proposed under M6 covers all three.

**L3 — finding 18 (verification) — [tools/check-install-prefix.sh:271](../../../../tools/check-install-prefix.sh)**

TOOL-aMendedFleet-38 deleted the only fixture line (`gd.resolve() / "qdemo" / "log.jsonl"`) and the
only census site that exercised NONKIT's `\bgd\b` alternative and `derive_operand`'s call-collapse,
and lowered the floor 40 to 39. The checker keeps both, so the `gd` homonym exemption is now a
predicate that matches nothing. A later edit can widen or break it and no arm reds.

- **Fix (judged SOUND):** either drop `\bgd\b` from NONKIT, since no site spells it any more, or keep
  a synthetic `gd.resolve() / "qdemo" / ...` line in the AC5 homonym fixture so the exemption and the
  collapse stay exercised.
- **Left-shift gate:** a liveness arm that asserts every NONKIT alternative matches at least one
  fixture line, so an exemption that stops being exercised reds instead of going quiet.

**L4 — finding 20 (intent) — [memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-75.md:148](../spec/2026-10-04-spec-TOOL-aMendedFleet-75.md)**

AC1 says a plain `python tools/check-spec-tokens.py` run prints one `HIT` line of kind `[covers]`.
The checker prints the `HIT` prefix only under `--list` (around check-spec-tokens.py:1275). A plain
run prints `spec-tokens: <spec> [covers] ...` with no `HIT` token, and the suite arm
(check-spec-tokens.test.sh:1252) asserts that plain form. Anyone re-running AC1 literally sees no HIT
line. The finder graded this medium and the skeptic re-graded it low, and low binds: it is a wording
defect in a CLOSED spec record and changes no behaviour.

- **Fix (judged SOUND):** add a rev bump to the spec that rewords AC1 to the plain-run form (a line
  carrying `[covers]` and `covers <- <fixture> AC9`, none naming AC1), or adds `--list` to AC1's
  command.
- **Left-shift gate:** none cheap. Add a §10 checklist line: "an AC quoting a checker's output names
  the flags that produce it".

## Refuted findings

Four findings were refuted by a skeptic and are dropped. Their reasons are in the appendix:
finding 2 (lexicon exit-2 DEAD PROBE is the specified behaviour), finding 8 (the bash re-validation
arm is defensive validation at a trust seam), finding 11 (no pre-BASELINES history row ever ships on
main), and finding 13 (the AC4/AC6 coverage gap is a scope the spec chose deliberately).

review-shape kind=diff-review round=1 intensity=full at=synth raw=21 confirmed=17 refuted=4 unverified=0 blocker=0 high=1 medium=10 low=6 agents=11 out-tokens=244623
## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/drift-audit/drift_report.py:432 | high | high | confirmed | build_baseline_findings (new in this diff, drift_report.py:400-443) only iterates `baselines.items()` from the head layer, and returns [] at line 402 when the head dict is empty. A signal that the base baselined but the head drops is never compared with the base. The both-declared refusal (3741) only fires when the signal is in both places. The diff deleted the RATCHETS row for non_terminal_specs_cited_by_product_source, and ratchet_findings skips a key the base does not hold (`was is None`). So deleting BASELINES['closed_specs_with_no_product_commit'] and adding PINS[...] = 50 passes `--check` with no finding. The pin becomes 50, and new offenders up to that count stay green. This contradicts the 'no escape' claim in the comments of both drift_report.py and drift_signals.py. It needs a deliberate edit to the governance layer, but that is exactly the edit an agent would make to clear a red `new` offender. | unsound | C66 |
| 2 | security | tools/lexicon/lexicon.py:4205 | medium | - | refuted | This is the behaviour the intent document asks for. The TOOL-aMendedFleet-3 spec defines exit 2 as a DEAD PROBE for 'no `.lexicon.conf`, no armed language' (line 45). It says 'Exit 2 prints `DEAD PROBE` and allows' (line 52), and in its consumes-from section: 'without them the check announces a skip or a DEAD PROBE and allows, and the push proceeds' (lines 83-84). The pre-push hook itself is also read from the pushed working tree and documents `--no-verify` as the override. So a tree-supplied conf that can disarm the check fits the documented trust model. It is not a defect this diff introduced. | unsound | C66 |
| 3 | security | tools/unattended/unattended.sh:2336 | medium | medium | confirmed | check_cross_run_overlap is new in this diff (it is absent at base). At unattended.sh:2336 it runs `GIT -c core.quotepath=off diff --name-only "$anc...HEAD"` with no --no-renames. The GIT wrapper (lib-unattended.sh:56) only adds replace/graft pins and does not set diff.renames=false, so git's default rename detection applies, and a renamed file is listed only under its destination path. The `theirs` read (~2367) and the slug-less ourspecs read both pass --no-renames. So when this run renames a.sh to b.sh and another ref edits a.sh, the join finds no shared path and the probe reports a clean result. The effect is contained because the probe is advisory and always returns 0. | sound | C41 |
| 4 | security | tools/push-main.sh:544 | low | low | confirmed | check_merge_losses and run_minter are new. resolve_kit_dir walks up from `$self_dir` to find its git root and prints the kit path relative to that root (push-main.sh:521-522), but both callers then run `$top/$dir/...`, and `$top` is the cwd's toplevel (line 99). When the lander comes from a different checkout than the tree it is run in, and that tree lacks the kit at the same relative path, python exits 2. check_merge_losses reads that as a DEAD PROBE and continues, and run_minter reports 'the version minter REFUSED'. The pre-push hook gets this right (`$_ml_tree/$_ml_dir`). The path is narrow, and pre-push grades the range again, so the effect is contained. | unsound | - |
| 5 | correctness | tools/memory-tree/check-verdict-epoch.sh:187 | medium | medium | confirmed | At base, pre-push already exported GATE_PUSH_BASE="$main_remote" (base line 1396), but neither consumer read it. This diff makes check-verdict-epoch.sh:187 and govkit.py:12370 take it as the base. On a push that creates the default branch, main_remote is all zeros. The bar still runs, because only an empty or all-zero main_local exits early (lines 959-960), and read_policy_at handles the zeros. check-verdict-epoch.sh then fails `git cat-file -e 000...^{commit}` and exits 2. govkit's rev-parse fails, which gives FAILED, exit 1. check-verdict-epoch is a gate_leg in the memory-tree kit.toml, so an adopter's first push to a new remote is refused. Before this diff it fell back to the merge-base. The hook already guards all-zero for GATE_ATTRIBUTE and for the merge-loss block. The result is a false refusal with a --no-verify escape, so it is contained. | sound | - |
| 6 | correctness | tools/unattended/unattended.sh:7318 | medium | medium | confirmed | This diff introduced LIVE_LANDED_UNCLOSED. The key is absent from the base .memory-tree.conf and from the base gen_build_index.py, and this repo's conf sets it to "1" (line 865). With it set, render_live writes a per-build Landed-unclosed count into LIVE.md (gen_build_index.py:1613-1627) using read_landed_unclosed, which calls drift_report.signal_spec_status. That function runs `git grep -l -w -F <id> -- EVIDENCE_GLOBS` (drift_report.py:725). With no --cached or tree argument, git grep reads tracked files from the working tree. The dirty-input inventories in write_ask_views (unattended.sh:7318-7333) and write_run_record (11224-11227) look only at changes under $M, .memory-tree.conf and the generator's own directory. So an unstaged product-source edit that adds or drops a citation of a non-terminal id goes unnoticed: the render picks it up and the helper stages a LIVE.md the index does not support. The pre-commit freshness check renders from the same worktree, so it agrees with the stale view. The damage is limited to one count in a view that the next clean render corrects, so medium. | sound | - |
| 7 | correctness | tools/memory-tree/check-verdict-epoch.sh:271 | medium | medium | confirmed | push-main.sh, changed in this diff, now mints kit versions inside the prepared merge with `git commit-tree ... -p "$R" -p "$oldb"` (lines 638-652). govkit's mint covers every epoch registry entry, and memory-tree is the engine check-verdict-epoch.sh dates. check-verdict-epoch.sh moved to `--diff-merges=first-parent` for this reason. hygiene-parity.test.sh:67 is unchanged and still runs `git log -S"KIT_MEMORY_TREE_VERSION=$KITV"` with no diff-merges option. By default git log does not diff merges, so pickaxe never matches the minting merge. When a value is introduced only by such a merge, FLOOR comes back empty and the harness exits 2 with the misleading 'shallow clone or squashed import' text. The harness is a manual tool that refuses loudly rather than giving a wrong answer, so medium. | sound | amendment-leaves-its-other-half-standing |
| 8 | correctness | tools/unattended/unattended.sh:7644 | low | - | refuted | The bash arm is not strictly unreachable. The Python guard only checks `isinstance(rid, int)`, which accepts a negative int and a bool (`isinstance(True, int)` is True). Either one prints as '-5' or 'True', which fails bash's `^[0-9]+$` and reaches the arm. Apart from that, re-validating a subprocess row at the bash boundary before it reaches `git merge-base` and an ask record is defensive validation at a trust seam, not a defect. Behaviour is unaffected either way. | unsound | C2 |
| 9 | seams | tools/workflows/tier2-review.js:1467 | medium | medium | confirmed | The base tier2-review.js has no workerType. Line 182 of the diff now defaults it to 'Plan', and the run's own log line 187 says lens and batch results are not durable and a resume re-dispatches them. Spec TOOL-aMendedFleet-93 also says a default-type review resumes nothing unless it passed 'none'. Several strings were not updated to match. The deferred notes at lines 888, 1181 and 1209 still say a re-run will 'dispatch only' the dead labels. The synth-death log (1467) and note (1516) still say the confirmed findings are 'in ${keyDir}' / 'on disk' and that the re-run 'dispatches only the synthesis', with `pending: ['synth']`. Under the default these claims are false, so a caller sizes its single retry wrongly. The effect is misleading guidance and extra cost, not wrong results, so medium. | sound | C18 |
| 10 | seams | tools/unattended/VERBS.template.md:603 | medium | medium | confirmed | unattended-build.js:839-852 calls tier2-review.js with no workerType, so it now gets the non-durable Plan default. Its deferred-platform comment (886-890) still says 'Every result that did come back is on disk under the callee's review key, so the remedy is cheap'. VERBS.template.md:603-604 still says 'every returned agent's result is on disk. Re-run the harness ONCE'. review-harnesses.md:66 still says every lens and skeptic batch writes its result under the key. Unit 93's S4 updated only the README and REVIEW-PROTOCOL. The retry-once-then-hold policy therefore rests on a cheap resume that no longer happens. A retry repeats the whole fan and is likely to hit the same limit, which pushes the run into a hold. That is costly but contained, so medium. | sound | - |
| 11 | seams | tools/drift-audit/drift_report.py:3258 | low | - | refuted | None of this code exists at base 7af5f564: there is no build_history_rows, HISTORY_FILE, render_drift_delta or BASELINES there. Units 48, 49 and 56 all land on main together in this diff, so main never wrote a history row with the pre-BASELINES hashing. The only pre-56 rows are the ones this branch's own intermediate commits wrote into a node-local history. A --delta can only pair such a row with a post-56 one when a run pins one of those intermediate branch shas as its BASE, which is not a path main ships. Even then the result is one extra '(members changed)' tail on a report-only delta. Under unit 56's own semantics, keying only new and stale rows is intended: a baselined row cannot swap in without becoming 'new', and dropping one makes it 'stale', so the hash still tracks membership against the baseline. | unsound | - |
| 12 | verification | tools/unattended/unattended.test.sh:12763 | medium | medium | confirmed | The diff adds 72 hit/miss/same/n++ lines to unattended.test.sh and removes none. The floors rose by only 25 (+15 for -60, +10 for -2). Region one runs from line 627 to 2036. It holds the -61 block (about 19-20 assertions, lines 1323-1349) and the -63 block (a loop over present/absent that executes 7+4=11), and neither moved FLOOR_SHARD_1. Region two holds -66 (2), -83 (2), -9 (16) and -49 S8 (2, behind a SKIP branch), and none moved FLOOR_SHARD_2 or FLOOR_ASSERTIONS. The file's own convention is to raise 'by exactly the arm', and its comments say the floor exists to catch a stranded BLOCK. With about 50 uncounted assertions, a stranded -61 or -9 block no longer reds in any mode. This weakens the guard rather than shipping a wrong result, so it is contained. | sound | - |
| 13 | verification | tools/push-main.sh:797 | medium | - | refuted | The spec for TOOL-aMendedFleet-65 scopes the automated arms on purpose. S9 says the new push-main.test.sh, selftest.py and check-verdict-epoch.test.sh arms stage only the moves of AC1, AC7 and AC9, and the 'New arm:' lines in section 7 declare only those. AC4 and AC6 are one-time observations by design. push-main.test.sh case 24 delivers the declared arm. The finding shows no wrong behaviour in the attended mint at push-main.sh:797-813 or in --prepare's refusal path at 644-649. Reading the code, the refusal path does reset to the branch tip and check the branch out, and the attended path does abort before the push. A coverage gap that the spec deliberately chose is not a defect this diff introduced. | sound | - |
| 14 | verification | tools/unattended/unattended.test.sh:12761 | low | low | confirmed | The KICK-aMendedFleet-2 block at unattended.test.sh lines 783-813 executes same, hit, hit, then hit, then miss, hit, then same, hit, miss. That is 9 assertions. The floor comments at lines 12761 and 12886 say 10, and both FLOOR_SHARD_1 and FLOOR_ASSERTIONS were raised by 10. The floors carry headroom, and region one now has about 30 unpinned arms from -61 and -63, so nothing reds today. The effect is a wrong count in the floor comment and one assertion of phantom pin. | sound | - |
| 15 | verification | tools/workflows/tier2-review.test.sh:1298 | low | medium | confirmed | The workerType block at tier2-review.test.sh lines 296-324 is new in this diff. It executes 12 ck() calls on the green path: 1 unconditional, 1 inside the absent-run checkNoThrow, 7 inside the Plan-run checkNoThrow, and 3 from the refusal loop. Each passing call increments the pass count the floor reads. FLOOR_ASSERTIONS rose 180 -> 183 only for -17 and -18, although line 1257 says 'raise it whenever arms are added'. So deleting the workerType block, or stranding it behind a die(), leaves the executed count at or above 183. The suite's own instruction is violated, but the effect is limited to the guard. | sound | - |
| 16 | verification | tools/runlog/selftest.py:321 | low | low | confirmed | Commit 7650e6e44 (TOOL-aMendedFleet-70) adds test_extract_ready at selftest.py:1977 with 4 check() calls. main() discovers every test_* global and runs 3 decoy checks after each one, so the arm adds 7 assertions. The commit leaves ASSERTION_FLOOR alone. The last floor move is cec007a68's RAISED 1543 -> 1554, which counts only the by-leg arm's 8 + 3. The floor is a `total < ASSERTION_FLOOR` minimum, so deleting the READY arm, or renaming it so it no longer starts with test_, takes the total back to exactly 1554 and nothing reds. The effect is a gap in a guard, with no wrong output today. | sound | - |
| 17 | verification | skills/session-kickoff/manifest-check.test.sh:1377 | low | low | confirmed | Each run_card and check_eq adds 1 to pass. The KICK-aMendedFleet-1 drift block has 5 run_card calls (t76a, the replay, t76b, t76c, t76d) and 4 check_eq calls, so 9 passes. The floor comment counts only overlaps (+8, which matches its 4 run_card and 4 check_eq) and cli (+19, which matches its 9 cli_card and 10 check_eq). 180 + 27 = 207, so the drift cell's 9 assertions are not under the floor, and they could be deleted or stranded without the floor going red. | sound | - |
| 18 | verification | tools/check-install-prefix.sh:271 | low | low | confirmed | TOOL-aMendedFleet-38 (9da643210 and 84783178f) removed the `gd.resolve() / "qdemo" / "log.jsonl"` line from the AC5 homonym fixture and the gd.resolve() census site, and lowered FLOOR_ASSERTIONS from 40 to 39. check-install-prefix.sh:271 still keeps `\bgd\b` in NONKIT. derive_operand's call-collapse is now reached only by a balanced call in front of a join. None of the remaining fixture lines has that shape. The tree's only `gd /` joins are in derive-ceilings.py, and they join 'gate-run', which is not a kit name. So neither branch is exercised any more. The commit's Decided line covers dropping the arm, but not keeping the predicate. The new install-prefix.md paragraph says a census shape that no longer occurs guards a spelling nobody writes, which is the state this exemption is now in. The effect is contained: an untested exemption. | sound | C64 |
| 19 | intent | tools/workflows/tier2-review.template.js:182 | high | medium | confirmed | At head, workerType defaults to 'Plan'. Under a type, judges are told to write no file, so no find-*.json or verify-*.json files exist, and a re-run reuses nothing. The harness logs this once at the start. Spec 93's risks paragraph accepts that loss of resume and puts the warning only in the protocol paragraph. But the deferred notes still say 're-run with identical args to dispatch only <pending>' (lines 888, 1181 and 1209), as do the synthesis-died messages. unattended-build.template.js passes no workerType on its spec-audit call (grep finds none), and its `next` text at line 916 says the re-run reuses every lens and skeptic batch. unattended.sh:6646 makes the same promise. On a deferral, the run's own instructions are therefore false: the re-run dispatches every judge again at full cost, which makes the second deferral, and so the hold, more likely. This is real and introduced by the diff, but the consequence is misleading text plus extra cost and holds on the deferral path. It produces no wrong result and loses no data, so it is medium, not high. | unsound | - |
| 20 | intent | memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-75.md:148 | medium | low | confirmed | check-spec-tokens.py prints the `HIT   [kind]` prefix only inside `if listing:` (around line 1275). A plain run prints hits as `spec-tokens: {f} [{kind}] `{tok}` — {why}`, with no HIT token. The suite arm (check-spec-tokens.test.sh:1252) asserts this plain form. The spec was new in this range, and its AC1 asks for a run without --list to show 'one `HIT` line of kind `[covers]`', which that run never prints. It is a wording defect in a CLOSED spec record and changes no behaviour. | sound | - |
| 21 | intent | memory/builds/aMendedFleet/spec/2026-10-04-spec-KICK-aMendedFleet-1.md:3 | low | medium | confirmed | The tier rule at memory/guides/SESSION-KICKOFF.md:203-205 is in the base too (the diff only touches 2 lines elsewhere in that file). It assigns Tier 2 to 'a new/changed kit's contract; a cross-kit change'. KICK-aMendedFleet-2 (commit 481eb9f39) is the clearest case. It adds a new `--overlaps` flag to tools/unattended/unattended.sh: a new usage line, an empty-slug branch in check_cross_run_overlap, and a new contract paragraph in tools/unattended/README.md. In the same commit it adds the `overlaps —` cell to skills/session-kickoff/manifest-check.sh. That is a new kit-contract surface and a two-kit change. The corpus grades the same thing Tier-2 elsewhere (aWokenSentinel-2: 'a new verb is a change to the kit's contract'). Yet KICK-2's header reads Tier-1. KICK-1 is less clear-cut: it touches only the session-kickoff kit, and precedent sometimes grades output-only changes Tier-1 (TOOL-aScouredKit-8). Still, its new card cell depends on the drift-audit kit's drift-history.tsv header contract (consumes-from TOOL-48, which is itself Tier-2). The consequence is real. In check-memory-hygiene.sh, `hdr ~ /Tier-1/ next` puts these specs below the Tier-1 cut, so the section canon and the CLOSED Tier-2 acceptance-ledger join never run on them. The build has a ledger for its Tier-2 units, and the README's 'Ids no record names' lists KICK-1, KICK-2 and KICK-4. The AC observations exist only in commit-message prose. The effect stays in the records and governance gates; shipped behaviour is unchanged. So medium rather than blocker or high. | sound | - |
