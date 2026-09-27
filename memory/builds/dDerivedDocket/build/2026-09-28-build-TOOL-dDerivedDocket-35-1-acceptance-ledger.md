**Serves:** journal TOOL-dDerivedDocket-35

# TOOL-dDerivedDocket-35 — acceptance ledger

The unit is two commits, and this ledger is the second: Rollout step 6's FIRST commit, made at the
end of the pass while the scratch clone still stands. `79485291` is the arming commit. It sets gov's
`ASKS_CMD` to `python tools/memory-tree/gen_build_index.py --asks`, writes S9's sixteen KEEP rows in
this build's `BACKLOG.md`, refreshes the mandate dossier's gap entry and re-stamps the kickoff
manifest. The scratch clone was cloned from that commit. This commit carries the three in-pass REDs,
the spec's rev-10 and its CLOSED header.

NO MERGE BAR, NO GATE LEG AND NO SUITE FILE RAN IN THIS PASS. The direct checks were the driver
(`unattended.sh --preflight`, `--close`) and the leg's own checker (`check-unattended.sh`), both run
INSIDE the scratch clone over its fixtures, the declared producer run by hand in call shape 2, and
`gen_build_index.py --asks --all --json` over this tree. Five criteria have NO line below, because
their `permission:` lines defer them. AC1, AC7 and AC9 are leg verdicts over the real tree, owed to
the one post-build bar. AC5 and AC6 need the linked-worktree topology that
`straggler-guard.test.sh --topology` builds, which gate-guard denies in a pass, so they are staged
at VERIFYING (§8 F7). Their direct in-pass reads are recorded in prose below.

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
- AC8 — `python tools/memory-tree/gen_build_index.py --asks --all --json` — at `79485291` every ask
  homed in this build's `BACKLOG.md` derives OPEN with a KEEP row there. That is `<triage-id>`,
  TOOL-dDerivedDocket-66, with unit 34's KEEP, and the sixteen section 11 declines, 38 to 47 and 55
  to 60, with S9's. `git diff HEAD^ HEAD` at `79485291` over the file adds sixteen KEEP rows and
  removes none. Each names an ask whose text records the decline, and the journal lists all seventeen
  with status and deciding row.
- AC10 — `core.hooksPath` — was unset in the clone when `4c6bd140`, carrying both scratch READMEs,
  reached the scratch remote's `main`. It was set by `check-wiring.sh --fix` only afterwards. The
  in-pass procedure used no `--no-verify` and no `GOV_GATE_CMD`, and pushed nothing after the hooks
  path was set, so no landing met `push-main-active`. S7's two documented uses are VERIFYING's.
