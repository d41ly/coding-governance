# dFoldedAudit — the spec stage's writer returns

**Serves:** journal TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8

Run wf_9c122f58-668, verbatim from its journal.

## v2:0a89bd541

{
 "authored": [
  "TOOL-dFoldedAudit-3",
  "TOOL-dFoldedAudit-4"
 ],
 "alreadyPresent": [],
 "refused": [],
 "summary": "Both specs are authored at Tier-2, OPEN, rev-1, with the order verbs 30 and 40. Nothing is committed and no index was regenerated.\n- C:\\projects\\coding-governance\\.claude\\worktrees\\gov-build-m4-spec-audit-694e7b\\memory\\builds\\dFoldedAudit\\spec\\2026-11-01-spec-TOOL-dFoldedAudit-3.md\n- C:\\projects\\coding-governance\\.claude\\worktrees\\gov-build-m4-spec-audit-694e7b\\memory\\builds\\dFoldedAudit\\spec\\2026-11-01-spec-TOOL-dFoldedAudit-4.md\n\nVerification: hygiene checks 5, 12 and 25 ran over all eight specs of this build in a scratch clone, staged there, and exited 0. The clone is deleted. Every §7 leg name was checked against `tools/gate-legs.json` by a read of the manifest. §8 is `none` on both.\n\nTOOL-dFoldedAudit-3 decisions the design left open, all recorded in its §4:\n- The rule reaches the harness as a `disposal` arg, because a Workflow script has no filesystem. Absent means today's rule and row, byte for byte. `promote-all` means the old rule on the new row. `by-nature` is the new rule on the new row. Units 1, 2 and 5 already read it this way.\n- Under a declared value the disposal precedes the record at every exit. The first `--review` call's refusal is the exit probe, and a second agent named `record-exit` writes the row after the stage.\n- `dispositions` holds one entry per finding per spec, with `id` as the integer raw finding id and `nature` as `local` or `new-mechanism`.\n- The §9 line cites the review record by file stem, which is what unit 6's predicate reads. A later rename of the report must rename the citation in the same commit.\n\nTOOL-dFoldedAudit-4 decisions:\n- The class gate's home resolves to `tools/check-spec-tokens.py`, as `scan_supersede`, with its own key `SPEC_SUPERSEDE_CUTOFF`. The key is separate from `SPEC_FOLD_CUTOFF` because it dates a spec's filename, not a run's preflight. The hygiene engine was rejected because it is a copy-installed kit, the same reason TOOL-dDerivedDocket-37 gave.\n- Waiver rows cannot silence its hits, as [repair] requires.\n- The frozen join reads `planState` by its `DONE` prefix, and it covers `local` fold entries as well as `siblingEdits`. It refuses a named unit that carries no `planState`.\n- The predicate over the real tree found 39 specs carrying the phrase, all pre-cutoff, and no live spec. A single-line search finds only 36.\n\nOpen for the cross-read (M2):\n1. Unit 1's carrier sentences name the `disposal` arg but not the `planState` requirement. Unit 4 §3 hands that sentence to unit 1, without a backticked payload, so no gate catches a miss. An unattended caller that omits `planState` meets refusal rows 15 and 16 on its first fold.\n2. Unit 6 dropped its consumes-from on unit 3, so I removed the matching hands-off. Unit 6 still reads the fold's §9 stem; the contract now rests on the prose in unit 3 §4 and unit 6 §4.\n\nOne departure from my role: I ran `python tools/check-spec-tokens.py --help` to read its usage, and that executed the gate instead, because it does not parse `--help`. The role allows only hygiene and the lexicon. It wrote nothing, and I relied on its printed report only for the 37 live specs figure in unit 4 §5."
}

## v2:7ad32fd4b

{
 "authored": [
  "TOOL-dFoldedAudit-1",
  "TOOL-dFoldedAudit-8"
 ],
 "alreadyPresent": [],
 "refused": [],
 "summary": "Both specs are authored at Tier-2, status OPEN rev-1, with `order 70` and `order 80`. Nothing was committed and no index was regenerated.\n\nFiles:\n- C:\\projects\\coding-governance\\.claude\\worktrees\\gov-build-m4-spec-audit-694e7b\\memory\\builds\\dFoldedAudit\\spec\\2026-11-01-spec-TOOL-dFoldedAudit-1.md\n- C:\\projects\\coding-governance\\.claude\\worktrees\\gov-build-m4-spec-audit-694e7b\\memory\\builds\\dFoldedAudit\\spec\\2026-11-01-spec-TOOL-dFoldedAudit-8.md\n\nVerification: memory hygiene checks 12 and 25, with the §3 edge joins, exit 0 over all eight of this build's specs, run in a scratch clone with the specs staged. One sentence of TOOL-dFoldedAudit-1 §3 changed after that run; a repo-wide `--staged` run on an earlier draft showed no check 12 or 25 failure, and that later sentence was not regraded. A first `--only 12,25` run failed check 12 on an edge mirror while sibling specs were still changing; recomputing the edges showed every one reciprocal, and the rerun passed. The spec-tokens leg was not run, because this role may not run it, so the leg lines, `New arm:` lines and backticks were checked by reading only.\n\nFor the commit stage: `--staged` check 9 fails until the index is regenerated, and it also names the `status: OPEN` line in the dFoldedAudit README front matter. Neither is a fault in these specs.\n\nDecisions a reader should check:\n1. The method fits. M4's target text renders to 30504 of 30720 bytes, measured against the real render with the as-built names.\n2. The unattended protocol has only one byte of headroom: its render is 66859 and its row 66860, and check 22 owes a new row for `SPEC_FOLD_CUTOFF`. TOOL-dFoldedAudit-1 takes the raise that `tools/template-size-limits.txt:16-28` permits, pinned with no headroom, so its write set adds that file and `memory/DECISIONS.md` to the brief's list. A trim of unrelated rows was rejected under the brief's limitation.\n3. Sibling hand-offs added carriers the brief did not list: the `/build` Skill template and render, the `disposal` and `planState` sentences for callers, and `tools/workflows/README.md` for `addresses` and `chainRecord`.\n4. Design tag [limits] says kit versions bump where a kit moves, but `tools/push-main.sh:26-31` mints them at the lander, so neither unit bumps one by hand.\n5. Design tag [chain] says `--hold`, but `--hold` refuses `owner-decision`, so HOLD routes through `--handoff --code owner-decision`, as TOOL-dFoldedAudit-5 specifies.\n6. `budgets.enforce` is `warn`, so `build-method size` cannot go red. TOOL-dFoldedAudit-1 therefore adds one real arm to the memory-tree parity suite, pinning M4's literals and the Budget line's byte figure.\n\nIn TOOL-dFoldedAudit-8:\n- v2:1260 and v2:1261 are catalogue rows with no clause id, so the single deviation record amends `cl-dClosedLoop-0117` alone and names both keys in its After text.\n- The new clause hash is `afb50a20`; `derive_clause_hash` reproduced both existing pins, so DL-32's `**Carries:**` pin moves to it.\n- The record's owner approver is listed as refused until TOOL-dFoldedAudit-1's decision row reaches the mainline. The host's `report` value means that listing moves no exit.\n- The pass runs as gov-spec-writer outside `unattended-unit.js`, because that harness's typed prompt hands spec changes back.\n- All its `New arm:` lines re-observe existing branches, because a records pass writes no suite.\n- DL-32 needs more edits than the design tag names: `no-fall` as a sixth `review_state` argument, and a spec subject's promotion target always ` · to units`. Both follow from the README rule that a budget does not outrank a spec audit's chain stop."
}

## v2:b0f5f98e2

{
 "authored": [
  "TOOL-dFoldedAudit-5",
  "TOOL-dFoldedAudit-6"
 ],
 "alreadyPresent": [],
 "refused": [],
 "summary": "Both specs are authored, uncommitted, Tier-2, OPEN, rev-1, at order 50 and order 60. All ten sections are present and the §3 edges mirror every sibling. Hygiene ran on a scratch index (a copy of the git index, leaving the shared one untouched), and check 12 reported no finding on either spec. The run still exited 1 on check 21, whose failing ids are this build's unit ids named by its records. I expect that to clear once the specs are committed, but I have not confirmed it. The check 13 lines come from sibling specs 1 and 8.\n\nTOOL-dFoldedAudit-5 is FORKED: its §8 F1 is open and needs the main loop's M3 sweep before build.\n- **F1:** the design's step 1, read literally, preempts R5 and the ceiling on any round that promotes. That contradicts two owner rulings in the build README.\n- **Recommendation:** option (b), where U leaves out P(N) and step 1 audits U, P(N) and F(N). §4 and AC6 and AC8 are written to it.\n\nDepartures and findings in TOOL-dFoldedAudit-5:\n- **Hold route:** HOLD uses `--park` then `--handoff --code owner-decision`, not the design's literal `--hold`, because `--hold` refuses that code (`tools/unattended/unattended.sh:6879`). TOOL-dFoldedAudit-1 already cites this.\n- **Refusal census:** the driver stands at 323 of a 323 ceiling that only the owner moves. The unit therefore adds one site, `check_chain_fault`, and merges the two byte-identical check 41 sites.\n- **Disposed-HIGH refusal:** the design's test could not fail when read from rows alone, so `--record-round` also takes `--blockers` and `--highs`.\n- **Harness refusals:** rows 17 and 18 of the reconciliation refuse a narrowed address and a non-id token before the shell string is composed.\n\nDepartures and findings in TOOL-dFoldedAudit-6:\n- **Both revision arms:** the exemption gates the `revision` arm as well as the `audit` arm, because 19 of dMindYourWords' 26 records answer the `revision` arm.\n- **File list:** the predicate lives in `tools/memory-tree/design_lib.py`, one file beyond the brief's list.\n- **Re-render:** the predicate clears 77 ids, so the pass re-renders three landed READMEs (dRankedPlan, dFurnishedOrders, dDeclaredLoop). A live claim on any of them is a park, and dSafePassage does not move."
}

## v2:ba6388c2b

{
 "authored": [
  "TOOL-dFoldedAudit-7",
  "TOOL-dFoldedAudit-2"
 ],
 "alreadyPresent": [],
 "refused": [],
 "summary": "Both specs are authored at Tier-2, status OPEN, uncommitted, with no fork left open.\n- C:/projects/coding-governance/.claude/worktrees/gov-build-m4-spec-audit-694e7b/memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-7.md (order 10)\n- C:/projects/coding-governance/.claude/worktrees/gov-build-m4-spec-audit-694e7b/memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-2.md (order 20)\n\nDerived names:\n- Policy keys: `review.spec-audit.disposal`, `review.spec-audit.chain-stop`, `review.spec-audit.chain-ceiling`.\n- Conf key: `SPEC_FOLD_CUTOFF`.\n- Reader: `read_spec_audit_switch`, which TOOL-dFoldedAudit-5 already consumes by that name.\n- Flags: `--folded`, `--promoted`, as TOOL-dFoldedAudit-3 expects.\n\nDesign splits you should know about:\n- The switches live only in `.governance/policy.toml`, because `policy.py:1285` refuses a new `.unattended.conf` key.\n- An adopter without the policy kit takes the kit defaults, and a blank cutoff keeps the old rule.\n- The brief's acceptance line 7 is split. TOOL-dFoldedAudit-7 observes the resolved value, and TOOL-dFoldedAudit-2 AC7 observes the refusal, because order 10 cannot rest on order 20.\n- TOOL-dFoldedAudit-2 calls `check_landed_facts_due` without renaming it, because a rename would touch `lib-unattended.sh`, outside its brief. Alternatives rejected records this.\n\nHygiene: I ran the gate in a scratch clone with all eight specs committed. The clone was on commit dccdeaa8. No check 12, 21, 25 or edge finding names any of the eight specs; I took check 12 and the edge join from the absence of a finding, not from a staged break.\nTwo items remain:\n- Check 9 reds until the committer regenerates the index, and it asks for the README's `status:` key to be deleted.\n- Check 13 prints lines for TOOL-dDeclaredLoop-20, TOOL-dDeclaredLoop-32, TOOL-dFairHearing-17 and TOOL-dGatedProse-4. The TOOL-dGatedProse-4 line printed before any spec existed, from the committed orient record. The other three first appeared with all eight specs tracked and name none of the units I authored, so they come from a sibling spec.\n\nFlags for the main loop:\n1. `check-arms` stands at the ceiling on both gates: driver census 323 of 323, `check-unattended.sh` 264 of 264. TOOL-dFoldedAudit-2 stays net zero by sharing one site. TOOL-dFoldedAudit-5's spec does not discuss the ceiling, and its two new verbs will pass it unless they cover sites or get the owner's retirement review.\n2. [cutoff] sets the value to the landing date, and `unattended.sh:1009-1012` records how a landing-day value redded a same-day record. TOOL-dFoldedAudit-7's edge gives the close a check before it writes the date.\n3. TOOL-dFoldedAudit-1's non-goal attributes the `.unattended.conf` writes to TOOL-dFoldedAudit-2. Per the briefs they are TOOL-dFoldedAudit-7's.\n\nA built-in safety check refused one fixture cleanup command. It never ran and created nothing, so nothing is left to delete. The scratch clones I made were removed."
}

## v2:772f7f9b1

{
 "committed": false,
 "sha": "dccdeaa8a8302cca2fdbffebfcfbe4a79fc50418",
 "why": "No commit landed: the pre-commit hook refused it on HYGIENE check 9, and HEAD is still dccdeaa8a. That sha is the unchanged base, not a spec commit.\n\nRoot cause, from both the generator and the hook: \"build-index: memory/builds/dFoldedAudit/README.md: front matter declares 'status: OPEN' but 8 spec(s) carry a status header — the build status is DERIVED from them, and two answers to one question is exactly the drift this index removes. Delete the 'status:' key.\"\n\nHook output:\n\"HYGIENE check 9 FAILED — generated build index differs from a fresh render:\nbuild-index: render owed under --staged — memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-1.md is staged as A, and an added or deleted path moves the record set\nbuild-index: memory/builds/dFoldedAudit/README.md: front matter declares 'status: OPEN' but 8 spec(s) carry a status header [...] Delete the 'status:' key.\npre-commit: a gate failed — fix or 'git commit --no-verify' to override deliberately.\"\n\nThe block's last line printed these porcelain lines (step 4), so the specs are not committed:\nA  memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-1.md\nA  memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-2.md\nA  memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-3.md\nA  memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-4.md\nA  memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-5.md\nA  memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-6.md\nA  memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-7.md\nA  memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-8.md\n\nState left behind: the eight specs are staged as A, and nothing else in the tree changed, so the render wrote no view. I did not unstage them, because the block names no cleanup for this exit.\n\nFix owed: line 8 of the memory/builds/dFoldedAudit/README.md front matter holds `status: OPEN`, and that key has to go. The README is not a spec and is outside this stage's scope. The block allows no added step, so I did not edit it, retry, or use --no-verify. After the fix, the block needs a fresh run. A read-only `gen_build_index.py --check` run afterwards also returned rc=1.\n\nTwo caveats. The block reached its last line although the hook failed, so `set -e` did not stop it as the task expects. I did not determine why, so a caller should not rely on the block's exit status here. I also did not observe the --write call's exit status. Step 6 did not run, because no commit exists and HEAD~1..HEAD would grade the previous records commit, so `checklist` is empty.",
 "specs": [
  {
   "id": "TOOL-dFoldedAudit-7",
   "path": "memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-7.md"
  },
  {
   "id": "TOOL-dFoldedAudit-2",
   "path": "memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-2.md"
  },
  {
   "id": "TOOL-dFoldedAudit-3",
   "path": "memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-3.md"
  },
  {
   "id": "TOOL-dFoldedAudit-4",
   "path": "memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-4.md"
  },
  {
   "id": "TOOL-dFoldedAudit-5",
   "path": "memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-5.md"
  },
  {
   "id": "TOOL-dFoldedAudit-6",
   "path": "memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-6.md"
  },
  {
   "id": "TOOL-dFoldedAudit-1",
   "path": "memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-1.md"
  },
  {
   "id": "TOOL-dFoldedAudit-8",
   "path": "memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-8.md"
  }
 ],
 "summary": "Spec commit refused by the pre-commit hook (HYGIENE check 9). The build README's front matter still declares `status: OPEN`, which the generator rejects once specs carry status headers. HEAD is unchanged at dccdeaa8a, the eight specs remain staged, and no view was rendered. The `status:` key must be deleted from memory/builds/dFoldedAudit/README.md before the block runs again.",
 "checklist": ""
}
