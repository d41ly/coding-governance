**Serves:** journal TOOL-dDerivedDocket-35

# TOOL-dDerivedDocket-35 — acceptance ledger

The unit is two commits, and this ledger is the second: Rollout step 6's FIRST commit, made at the
end of the pass while the scratch clone still stands. `79485291` is the arming commit. It sets gov's
`ASKS_CMD` to `python tools/memory-tree/gen_build_index.py --asks`, writes S9's sixteen KEEP rows in
this build's `BACKLOG.md`, refreshes the mandate dossier's gap entry and re-stamps the kickoff
manifest. The scratch clone was cloned from that commit. This commit carries the three in-pass REDs,
the spec's rev-10 and its CLOSED header. Rollout step 6's SECOND commit, made at VERIFYING, adds
the two deferred REDs, AC5's and AC6's lines, and the clone's removal. That is the section
"The two deferred REDs, staged at VERIFYING" below.

NO MERGE BAR, NO GATE LEG AND NO SUITE FILE RAN IN THIS PASS. The direct checks were the driver
(`unattended.sh --preflight`, `--close`) and the leg's own checker (`check-unattended.sh`), both run
INSIDE the scratch clone over its fixtures, the declared producer run by hand in call shape 2, and
`gen_build_index.py --asks --all --json` over this tree. At the first commit five criteria had NO
line below, because their `permission:` lines defer them. AC1, AC7 and AC9 are leg verdicts over the
real tree, owed to the one post-build bar, and still have none. AC5 and AC6 need the linked-worktree
topology that `straggler-guard.test.sh --topology` builds, which gate-guard denies in a pass, so
they were staged at VERIFYING (§8 F7) and their lines came with the second commit. The direct
in-pass reads behind AC1, AC7 and AC9 are recorded in prose below.

## The scratch clone, left standing for VERIFYING

- **Where.** The clone is `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-build-readme-governance-18d6ea/2588f719-5358-4984-93bc-1f908a71e0ab/scratchpad/build-scratch/c`.
  Its `origin` is the bare repository `o.git` beside it, seeded by fetching this branch's tip,
  `79485291`, as its `main`, which the bare repository's `HEAD` names. `merge.rows.driver` is copied
  from this node (`bash tools/memory-tree/merge-rows.sh %O %A %B %P`), since a clone copies no local
  config.
- **The one fixture commit, `4c6bd140`, on the scratch `main`.** `.memory-tree.conf` adds the
  `example` discipline and the `example:EXMP` family, the pair the generator's `EXAMPLE_ROW` names.
  `.unattended.conf` sets `GATE_CMD="false"`. The commit also carries the two scratch builds and
  their BOUND contract rows, and the views `gen_build_index.py --write` rendered for them. The first
  build, `dUnfiledMandate`, is a README only, whose `asks:` names EXMP-dUnfiledMandate-1, which no
  `BACKLOG.md` files. The second, `dStagedMandate`, is a README plus its own `BACKLOG.md`, which files
  EXMP-dStagedMandate-1 with a `seen … matching …` locator and an `accept` clause, so it grades
  READY `yes`. Both READMEs were rendered by the kit's own `render_new_build_readme`, called directly:
  the `--new-build` command refuses a slug whose folder already files an ask, which the self-filing
  build is by the spec's design (rev-10).
- **Order (AC10).** `4c6bd140` was pushed to `origin main` while `git config --get core.hooksPath`
  printed nothing, and `git ls-remote --symref origin HEAD` then read `ref: refs/heads/main` at
  `4c6bd140`. Only after that, `bash tools/check-wiring.sh --check` printed
  `UNWIRED  hooks     — core.hooksPath unset; .githooks gates (incl. branch guard) dormant.` and
  wrote nothing, and `bash tools/check-wiring.sh --fix` printed
  `FIXED    hooks     — set core.hooksPath -> .githooks`. Every later scratch commit met the hooks.
- **State handed to VERIFYING.** The two linked worktrees the in-pass runs used, and their branches,
  were removed after the REDs below, so the clone is its primary tree on `main` at `4c6bd140` with
  `core.hooksPath` `.githooks`. S6's topology and S7's merge start from there.

## The three in-pass REDs, verbatim

Each ran in a LINKED worktree of the clone on a run branch cut from the scratch `main`, because the
clone is a primary tree and its branch guard refuses a commit off its default branch there. The
environment named a fixture session (`CLAUDE_CODE_SESSION_ID=fixture-scratch`, `CLAUDE_PID=999999999`)
so no record carries this session's lease.

**S3, the ask driver.** `unattended.sh --preflight dUnfiledMandate --keepalive-id KA-scratch` passed
authorization and refused at P5, writing nothing:

```
UNATTENDED check 72 FAILED — a mandated ask is not filed in the tree this run is anchored to, so the run would be choosing among records it could have written itself: EXMP-dUnfiledMandate-1 has no row in memory/builds/dUnfiledMandate/BACKLOG.md at 4c6bd14086fadbee3a00b1b837970c2c535c6e48
unattended: --preflight refused; the run-state file is unchanged
```

P5 runs before READY, so the READY witness did not run for this mandate.

**S4, `asks-disposed`.** The second build's preflight succeeded and ran READY at `m-base`:

```
unattended: preflight — mandate pinned at m-base 4c6bd14086fadbee3a00b1b837970c2c535c6e48 · asks EXMP-dStagedMandate-1 · ready EXMP-dStagedMandate-1=yes
unattended: preflight OK — base 4c6bd14086fadbee3a00b1b837970c2c535c6e48 · anchor refs/heads/main at 4c6bd14086fadbee3a00b1b837970c2c535c6e48 · keepalive KA-scratch · region copied from memory/builds/dStagedMandate/README.md
```

`--close dStagedMandate` refused twice before it evaluated any item, and each refusal is a step a
real run takes. Check 62 refused the staged, uncommitted record, so the record was committed as
`bc89e2bf` through the hooks. Check 63 then asked for a prepared merge, so
`push-main.sh --prepare --slug dStagedMandate` made `adc6f286`, whose first parent is the advertised
tip `4c6bd140`. That merge was local, and nothing was pushed. The third `--close` evaluated every
item, and among its unmet items:

```
UNATTENDED check 13 FAILED — a machine-checked DoD item is unmet, so --close blocks: asks-disposed
    a mandated ask ended in none of the states this item admits - it is not derived terminal, and this build's own file holds no BLOCKED, DEFERRED or KEEP row for it: EXMP-dStagedMandate-1 reads OPEN
```

The other unmet items were `gates-green`, which is `GATE_CMD="false"` and ran no bar, then
`build-complete`, `closing-review-recorded`, `keepalive-reaped`, `parked-decisions-surfaced` and
`reuse-probed`, each a fixture that was never going to finish. The item did not read T0, so the
clone's conf was the armed one, and it passed T2, so the witness agreed with the scope. Shape 2 run
by hand in the same worktree, with `--ready EXMP-dStagedMandate-1 --target dStagedMandate --at HEAD`
appended to the declared value, printed one `ask` row and `examined 1`.

**S5, the folder-wide anchor ban.** The baseline leg run in that worktree, before the break and with
`GOV_UNATTENDED_REPORT=1`, reported `check 37 found no foreign anchor under memory/builds/dStagedMandate`
and one run-state record pinning an `asks:` fact. The break was a staged typed table,
`memory/builds/dStagedMandate/reviews/2026-09-28-review-EXMP-dStagedMandate-1-resolution.md`, whose
one body row's first cell is the BACKTICKED id TOOL-dDerivedDocket-38. That id is a real ask, filed
in this build's folder. The same leg run then printed:

```
UNATTENDED check 37 FAILED — a mandated run's own build folder ANCHORS a record id belonging to another build, so this folder is a second claimant for an id it does not own and the two builds' records can no longer be told apart: memory/builds/dStagedMandate/reviews/2026-09-28-review-EXMP-dStagedMandate-1-resolution.md:7:TOOL-dDerivedDocket-38 (1 in all) under memory/builds/dStagedMandate
```

The table was then unstaged and deleted.

## The two deferred REDs, staged at VERIFYING

This is Rollout step 6's second commit, and the orchestrator makes it at VERIFYING, after the last
unit closed (§8 F7). The clone read as the pass handed it over: `git status --short` printed nothing,
`main` stood at `4c6bd140`, `git worktree list` held the primary tree alone, and
`git config --get core.hooksPath` printed `.githooks`. Every command ran under the in-pass fixture
session environment, plus `PYTHONDONTWRITEBYTECODE=1`, which the straggler suite also sets.

**The topology.** `git branch straggler abac6d59` cut the pre-switch branch. Then
`bash .githooks/straggler-guard.test.sh --topology <clone> straggler`, run in the clone, exited 0 and
printed one path, the linked worktree `c-wt-straggler` beside the clone. The helper checks out an
existing branch, so this pair stands in for the `git worktree add <dir> -b <branch> abac6d59` that
S6 spells. `git worktree list` then read the primary tree at `4c6bd140 [main]` and the linked one at
`abac6d59 [straggler]`, and `core.hooksPath` still read `.githooks`, the relative value the pass's
`check-wiring.sh --fix` wrote. Every edit below rewords the same row of `memory/backlog/TOOL.md`,
the row of TOOL-aHonedRuleset-7, which is OPEN at `abac6d59` and whose id this tree defines in
`memory/builds/aHonedRuleset/BACKLOG.md`.

**S6, the relative arm, ran first.** That order makes the edit the absolute arm refuses the same
edit S7 commits with `--no-verify`, so the change commit the audit names is S7's. AC5 orders neither
arm. With `core.hooksPath` read from the clone's shared config alone, a plain `git commit` of the
staged reword in the linked worktree exited 0. The worktree's own pre-switch `pre-commit` ran, and
no line refused or printed the recipe:

```
memory-hygiene: project key PROJECT_REGISTRY_EXTRA='pass-order-waiver.txt substitution-fed-loops.txt' (gov's default is blank)
memory-hygiene: project key ROTATION_MODE='cut' (gov's default is blank)
memory-hygiene: the §3 edge JOINS are held under --staged — the selection is the staged set, so one end of a correctly declared pair would report the other as missing. The shape arm still ran; the push-boundary run is where the joins bind.
memory-hygiene: the curation-debt stale-ENTRY guard and its per-row report are HELD under --staged — the selection is the staged set, so a listed file nobody staged would record nothing and read as stale
memory-hygiene: check 23 HELD under --staged — a corpus-wide join over every closed Tier-2 unit; the push-boundary run is where they bind
[straggler 46dfdc2e] scratch straggler: a shard row edit under the relative hooks path
 1 file changed, 1 insertion(+), 1 deletion(-)
```

`bash tools/check-wiring.sh --session` in the primary scratch tree then exited 0, and the last of
its ten lines was:

```
note     straggler — refs/heads/straggler (hooks own-tree) still edit the authored backlog shards and owe a relocation before they merge; a marked branch runs its own pre-flip hook files, so only this note, the drift signal and the merge bar reach it. Detail: python3 tools/memory-tree/migrate_backlog.py --stragglers
```

**S6, the absolute arm.** This is a FIXTURE SETTING and proves nothing about gov's own wiring:
`git config extensions.worktreeConfig true` in the clone, then
`git config --worktree core.hooksPath <clone>/.githooks` in the linked worktree.
`git config --show-origin --get-all core.hooksPath` there then read the shared `.githooks` and the
absolute value from that worktree's `config.worktree`. A second reword of the same row was staged,
and a plain `git commit` exited 1:

```
pre-commit: REFUSING — this branch predates the per-build backlog and this commit stages an
  authored backlog shard or a family-named backlog archive. Merged later, that edit can drop
  a row with nothing able to say which one. Relocate it instead:
  This branch predates the per-build backlog. Its edits to memory/backlog/<F>.md must be relocated, not merged.
    git merge <default>       # MERGE, never rebase or squash: those leave no merge to audit
    python tools/memory-tree/migrate_backlog.py --relocate --as <your-slug>
    git add memory/ && git commit
  Already landed without this? Any node:  python tools/memory-tree/migrate_backlog.py --repair <merge-sha>
  A branch nobody will revisit? From the default branch:  python tools/memory-tree/migrate_backlog.py --ingest <ref>
  Deliberate override, as always: git commit --no-verify
memory-hygiene: project key PROJECT_REGISTRY_EXTRA='pass-order-waiver.txt substitution-fed-loops.txt' (gov's default is blank)
memory-hygiene: project key ROTATION_MODE='cut' (gov's default is blank)
memory-hygiene: the §3 edge JOINS are held under --staged — the selection is the staged set, so one end of a correctly declared pair would report the other as missing. The shape arm still ran; the push-boundary run is where the joins bind.
memory-hygiene: the curation-debt stale-ENTRY guard and its per-row report are HELD under --staged — the selection is the staged set, so a listed file nobody staged would record nothing and read as stale
memory-hygiene: check 23 HELD under --staged — a corpus-wide join over every closed Tier-2 unit; the push-boundary run is where they bind
pre-commit: a gate failed — fix or 'git commit --no-verify' to override deliberately.
```

**S7, the transition audit.** The refused edit was committed in the linked worktree with
`git commit --no-verify`, the first of S7's two bypasses, as `f150d8fb`. In the primary scratch tree
`git merge --no-ff straggler` then exited 1, stopped by the row driver:

```
merge-rows: REFUSED — %A is a GENERATED family view and %B is an AUTHORED backlog shard, so one branch predates the per-build backlog; those rows are RELOCATED, never line-merged
This branch predates the per-build backlog. Its edits to memory/backlog/<F>.md must be relocated, not merged.
  git merge <default>       # MERGE, never rebase or squash: those leave no merge to audit
  python tools/memory-tree/migrate_backlog.py --relocate --as <your-slug>
  git add memory/ && git commit
Already landed without this? Any node:  python tools/memory-tree/migrate_backlog.py --repair <merge-sha>
A branch nobody will revisit? From the default branch:  python tools/memory-tree/migrate_backlog.py --ingest <ref>
Auto-merging memory/backlog/TOOL.md
CONFLICT (content): Merge conflict in memory/backlog/TOOL.md
Automatic merge failed; fix conflicts and then commit the result.
```

The resolution took the default branch's view, `git checkout --ours memory/backlog/TOOL.md` and then
`git add`, which left the index equal to `HEAD`. A plain `git commit --no-edit` exited 1 with one
line:

```
memory-hygiene: check 26 refuses this merge — TOOL-aHonedRuleset-7 (changed), changed by f150d8fb77472e03bf7841c0ae72ac98ab31fd49, crosses a mode boundary with no RELOCATED row in the index. Write the row and conclude the merge, or `--repair` it afterwards.
```

That line comes from `transition_audit.py --staged`, which `.githooks/commit-msg` calls and
`pre-commit` does not. A direct replay of both hooks over the same pending merge confirmed it:
`bash .githooks/commit-msg .git/MERGE_MSG` exited 1 printing the same line, and
`bash .githooks/pre-commit` exited 0. Then `git commit --no-verify --no-edit`, S7's second bypass,
concluded the merge as `2ee66b9c`. Its parents are `4c6bd140` and `f150d8fb`, so it is a real merge
and not a squash. `bash tools/memory-tree/check-memory-hygiene.sh` in the primary scratch tree then
exited 1 after 44 s, and its check 26 printed:

```
memory-hygiene: check 26 transitions examined 1 · merges walked 391 · pinned 0 · unpinned 1 · cache hits 0
memory-hygiene: check 26 UNACCOUNTED — merge 2ee66b9c09543792ab055530ce668fa79b33856e carries a lost row: TOOL-aHonedRuleset-7 (changed), changed by f150d8fb77472e03bf7841c0ae72ac98ab31fd49. Remedy: repair it forward with `--repair 2ee66b9c09543792ab055530ce668fa79b33856e`, which writes the RELOCATED row this check reads.
```

**That exit 1 is not check 26's alone.** The same run reported findings that belong to the scratch
content, not to the break:

- Check 14 named 23 `EXMP` ids as cited and never defined. The clone's conf declares that family,
  and this corpus already cites ids in it.
- Check 23 failed on closed units the clone's content at `79485291` evidences in no journal.
- Check 17 reported the gotchas index stale, and check 16 reported one ungated finding.
- It printed `line 2534: files8: unbound variable` three times, once per curation-debt row it found
  earning a waived check. `files8` is assigned only on check 8's shards-mode branch, so under
  `BACKLOG_MODE="builds"` the report's check-8 applicability test reads an unset name under
  `set -u`. It moved no verdict here, and this unit touched neither that line nor the report. The
  same script run over this worktree while this section was written printed the same three lines,
  so this one is not scratch content.

The audit's own module isolates the RED. `python tools/memory-tree/transition_audit.py --at 4c6bd140`
exited 0 with `transitions examined 0`, and the same module at the merge exited 1 with the
`UNACCOUNTED` line above.

**Bypasses, and the clone's removal.** This procedure used `--no-verify` exactly twice, both of them
S7's. It set no `GOV_GATE_CMD` and pushed nothing. Afterwards, `chmod -R u+w` over the clone, the
linked worktree beside it and `o.git` cleared their read-only object files, 73 of them, and
`rm -rf` removed all three. `test -e` then read each one absent. The rest of the `build-scratch`
directory holds other units' files and was left in place. AC7's `memory hygiene` reading binds only
on a run that includes the commit carrying this section; a bar started before that commit reads the
first commit's ledger (Rollout step 6).

## A red that is not this unit's, and that the owed bar will meet

Both leg runs in the clone also failed check 15, independent of the break:

```
UNATTENDED check 15 FAILED — a first-commit DATE is read with --diff-filter=A and no --follow in this kit's own shell, so a rotation re-dates an archived record to the commit that added its name and a cutoff grades a record it was written to grandfather:
  …/tools/unattended/check-unattended.test.sh:5243
```

The dating self-scan globs every `*.sh` beside the leg, and its own suite is one of them. Line 5243
is the suite's fixture for that very arm, a `printf` whose text carries the banned spelling. The same
awk predicate run over this tree's `tools/unattended/*.sh` at `79485291` returns that one line. So
the `unattended kit gate` leg that AC1 defers to will red on it at the post-build bar. Both the arm
and the line came in with `743e01e5` (TOOL-dDerivedDocket-22), and this unit touched neither.

## In-pass reads behind the deferred criteria

- **AC1.** `.unattended.conf` at `79485291` carries
  `ASKS_CMD="python tools/memory-tree/gen_build_index.py --asks"`, and the `ASKS_CMD` row is present
  in the protocol's key table (`memory/guides/UNATTENDED-PROTOCOL.md`). The value, run in call shape
  2 over this build's seventeen homed asks at `79485291`, printed seventeen `ask` rows and `examined 17`.
  `PROBE_ALLOW` in `.memory-tree.conf` is still blank.
- **AC9.** The pre-commit hook's staged manifest leg accepted `79485291`, whose `last-audit` reads
  `2026-09-28T02:21:57+03:00 @ 869209edc6f8056706989e05e45558607b0eb709` against the parent's
  `02:02:14`. The sha is the merge-base with `origin/main`, unchanged. The commit carries the delta
  line.
- **AC7.** Before this commit was made, `git status --porcelain` listed only this ledger, the spec
  and the build README's generated units region, all declared writes. The clone stays for
  VERIFYING (S8).

## This build's own asks (S9, AC8)

`gen_build_index.py --asks --all --json` at `79485291` homes seventeen asks in
`memory/builds/dDerivedDocket/BACKLOG.md`, and every one derives `OPEN`, because a KEEP keeps an ask
live. Sixteen record their decline under the unattended protocol's section 11 in their own text,
and S9 wrote one KEEP for each. The seventeenth is the triage ask, TOOL-dDerivedDocket-66, whose
KEEP unit 34 wrote. `git diff 79485291^ 79485291` over the file is sixteen additions and no deletion,
each a KEEP row. Each ask with its status and deciding row, as `status · deciding row`:

1. TOOL-dDerivedDocket-38 — OPEN · the S9 KEEP, citing section 11
2. TOOL-dDerivedDocket-39 — OPEN · the S9 KEEP, citing section 11
3. TOOL-dDerivedDocket-40 — OPEN · the S9 KEEP, citing section 11
4. TOOL-dDerivedDocket-41 — OPEN · the S9 KEEP, citing section 11
5. TOOL-dDerivedDocket-42 — OPEN · the S9 KEEP, citing section 11
6. TOOL-dDerivedDocket-43 — OPEN · the S9 KEEP, citing section 11
7. TOOL-dDerivedDocket-44 — OPEN · the S9 KEEP, citing section 11
8. TOOL-dDerivedDocket-45 — OPEN · the S9 KEEP, citing section 11
9. TOOL-dDerivedDocket-46 — OPEN · the S9 KEEP, citing section 11
10. TOOL-dDerivedDocket-47 — OPEN · the S9 KEEP, citing section 11
11. TOOL-dDerivedDocket-55 — OPEN · the S9 KEEP, citing section 11
12. TOOL-dDerivedDocket-56 — OPEN · the S9 KEEP, citing section 11
13. TOOL-dDerivedDocket-57 — OPEN · the S9 KEEP, citing section 11
14. TOOL-dDerivedDocket-58 — OPEN · the S9 KEEP, citing section 11
15. TOOL-dDerivedDocket-59 — OPEN · the S9 KEEP, citing section 11
16. TOOL-dDerivedDocket-60 — OPEN · the S9 KEEP, citing section 11
17. TOOL-dDerivedDocket-66 — OPEN · unit 34's KEEP, awaiting the owner's triage of five legacy holds

**Evidences:** TOOL-dDerivedDocket-35
- AC2 — amended rev-10 — `unattended.sh --preflight` on the landed `dUnfiledMandate` README refused
  at check 72, P5's statement, naming EXMP-dUnfiledMandate-1, after authorization passed. It was no
  parse refusal and no DEAD PROBE. The criterion asked for the label `P5` by name, which the driver
  never prints, so rev-10 reads the term off the check number and statement (section 9, rev-10). READY
  did not run there, because P5 precedes it; on the second build it pinned one grade for one id.
- AC3 — amended rev-10 — `unattended.sh --close` on the scratch mandated run listed `asks-disposed`
  among its unmet items, naming EXMP-dStagedMandate-1 in T3's mandated-ask statement, `reads OPEN`,
  and neither T0 nor a DEAD PROBE. Call shape 2 returned one row and `examined 1` for the one scoped
  id. The criterion asked for the label `T3`, which the driver never prints (section 9, rev-10). The
  scratch `GATE_CMD` was `false`, so no bar ran.
- AC4 — `bash tools/unattended/check-unattended.sh` — in the scratch clone, with the typed table
  staged, failed check 37 naming the anchor ban and TOOL-dDerivedDocket-38 at line 7 of the table.
  The baseline run before the break reported no foreign anchor under the same folder, and the first
  cell was backticked, not link-wrapped.
- AC5 — `git commit` — ran in the scratch clone's linked worktree on `straggler`, cut from `abac6d59`,
  built by `straggler-guard.test.sh --topology`, with the primary scratch tree on `main` and a reword
  of TOOL-aHonedRuleset-7's row in `memory/backlog/TOOL.md` staged. Under the absolute
  `config.worktree` override naming the primary tree's `.githooks`, a fixture setting, it exited 1
  printing `REFUSING` and the recipe's `migrate_backlog.py --relocate --as <your-slug>` line. Under
  the relative `.githooks` the pass's `check-wiring.sh --fix` wrote, it landed as `46dfdc2e` with no
  recipe, and `bash tools/check-wiring.sh --session` in the primary scratch tree then printed one
  `note` line naming `refs/heads/straggler` with `hooks own-tree`. The relative arm ran first.
- AC6 — `git merge --no-ff` — of `straggler` into the scratch `main`, in the primary scratch tree,
  stopped on the row driver's shard-into-view refusal in `memory/backlog/TOOL.md`. Resolved to
  `main`'s view, a plain `git commit` exited 1 on `.githooks/commit-msg`: replayed directly, that
  hook exited 1 printing check 26's refusal of TOOL-aHonedRuleset-7, changed by `f150d8fb`, while
  `pre-commit` exited 0. Concluded with `--no-verify` as the two-parent merge `2ee66b9c`,
  `bash tools/memory-tree/check-memory-hygiene.sh` there exited 1, and check 26 printed
  `UNACCOUNTED` naming merge `2ee66b9c`, TOOL-aHonedRuleset-7 and change commit `f150d8fb`. Other
  scratch-content findings shared that exit, and `transition_audit.py` alone read 0 at `4c6bd140`
  and 1 at the merge.
- AC8 — `python tools/memory-tree/gen_build_index.py --asks --all --json` — at `79485291` every ask
  homed in this build's `BACKLOG.md` derives OPEN with a KEEP row there. That is `<triage-id>`,
  TOOL-dDerivedDocket-66, with unit 34's KEEP, and the sixteen section 11 declines, 38 to 47 and 55
  to 60, with S9's. `git diff HEAD^ HEAD` at `79485291` over the file adds sixteen KEEP rows and
  removes none. Each names an ask whose text records the decline, and the journal lists all seventeen
  with status and deciding row.
- AC10 — `core.hooksPath` — was unset in the clone when `4c6bd140`, carrying both scratch READMEs,
  reached the scratch remote's `main`. It was set by `check-wiring.sh --fix` only afterwards. The
  in-pass procedure used no `--no-verify` and no `GOV_GATE_CMD`, and pushed nothing after the hooks
  path was set, so no landing met `push-main-active`. S7's two documented uses are VERIFYING's, and
  the VERIFYING procedure used exactly those two, set no `GOV_GATE_CMD` and pushed nothing.
