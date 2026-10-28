---
slug: dSafePassage
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-14 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-60 TOOL-dSafePassage-61 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71
spec-audit: 2026-10-21
parents: dGroundRules
may: PLAY-dClosedLoop-3
---

# dSafePassage — the Supersession build of the dClosedLoop chain

## The problem this build exists to solve

dSafePassage owns 13 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-deploy-15,
gap-deploy-16, gap-deploy-17, gap-deploy-24, gap-tool-10, gap-tool-22, gap-tool-12, gap-tool-23, gap-deploy-18,
gap-deploy-19, gap-deploy-20, gap-deploy-25, gap-found-35. Closing every one is this build's goal bound.

## Expected improvements

- Each of the 13 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 13 owned gaps above close.

## Detriments if this is not built

- Its 13 owned gaps stay open.
- Its 2 child builds wait on it: dOrderedCharter, dFairHearing.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dSafePassage` green before the first pass; a moved instrument blob is
  a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dSafePassage`, a record per member "recorded by nobody", the same with `--write` (commit it
  as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
  re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `TOOL-dSafePassage-1` | `cl-dClosedLoop-0018@ed08a364` | the upgrade-step kind: a kit descriptor's `[[upgrade]]` row (id |
| 2 | `TOOL-dSafePassage-2` | `cl-dClosedLoop-0019@6e0cd313` | `update` walking every step between a receipt's vintage and its target |
| 3 | `TOOL-dSafePassage-3` | `cl-dClosedLoop-0020@42c7d579` | the receipt's schema 4 gaining `steps` |
| 4 | `TOOL-dSafePassage-4` | `cl-dClosedLoop-0021@ad0db541` | down steps run in reverse |
| 5 | `TOOL-dSafePassage-5` | `cl-dClosedLoop-0022@4bc8eba9` | the release-0 fixture tree and the `upgrade-walk` leg: up |
| 6 | `TOOL-dSafePassage-6` | `cl-dClosedLoop-0023@6e1e2e99` | a forwarding shim for a moved command |
| 7 | `TOOL-dSafePassage-7` | `cl-dClosedLoop-0024@7817c7d0` | the step kind's isolation contract |
| 8 | `TOOL-dSafePassage-8` | `cl-dClosedLoop-0025@4e486ab9` | gov first for every step: each step run on gov's own tree in the lander's prepared merge before any adopter meets it |
| 9 | `TOOL-dSafePassage-9` | `cl-dClosedLoop-0026@97d3c99b` | withdrawn hook fragments unwired |
| 10 | `TOOL-dSafePassage-10` | `cl-dClosedLoop-0027@46290183` | the step gate: a leg that diffs the adopter-visible surface population between a landing's base and its tip |
| 11 | `TOOL-dSafePassage-11` | `cl-dClosedLoop-0028@032ca791` | the interpreter floor raised to Python 3.15 as the step kind's first step after the receipt's schema-4 step |
| 12 | `TOOL-dSafePassage-12` | `cl-dClosedLoop-0029@4aeb7648` | gov's own executors at the floor in the landing that raises it: every job of `.github/workflows/remote-ci.yml` that runs Python setting it up at the floor |
| 13 | `TOOL-dSafePassage-13` | `cl-dClosedLoop-0030@274077d4` | the docs leg |
| 14 | `TOOL-dSafePassage-15` | **Derived:** PLAY-dClosedLoop-2 | the walk persists no step row below schema 4, so a schema-3 receipt reaches the schema step |
| 15 | `TOOL-dSafePassage-16` | **Derived:** PLAY-dClosedLoop-2 | the step record's precondition, one predicate beside its one writer, and the schema-4 bootstrap it answers |
| 16 | `TOOL-dSafePassage-17` | **Derived:** PLAY-dClosedLoop-2 | a down is judged by its row's declared `reverted` rule, and a down with no before-image by its exit |
| 17 | `TOOL-dSafePassage-18` | **Derived:** PLAY-dClosedLoop-2 | the reverse walk writes no row once a down leaves the receipt below schema 4 |
| 18 | `TOOL-dSafePassage-19` | **Derived:** PLAY-dClosedLoop-2 | a rollback past the schema step stamps schema 3 with no `steps`, finishes its record, and converges after a kill |
| 19 | `TOOL-dSafePassage-20` | **Derived:** PLAY-dClosedLoop-2 | the reader's `unlanded` is recorded as `null` at the step record's one writer |
| 20 | `TOOL-dSafePassage-21` | **Derived:** PLAY-dClosedLoop-2 | the step gate's `file` class reads gov's planned destinations when no source receipt is on the tree |
| 21 | `TOOL-dSafePassage-22` | **Derived:** PLAY-dClosedLoop-2 | the lock reclaim reads its clock before the census, so a slow census errs toward live |
| 22 | `TOOL-dSafePassage-23` | **Derived:** PLAY-dClosedLoop-2 | the resolver keeps an override's own name, and prefers the direct executable only for the launcher names |
| 23 | `TOOL-dSafePassage-24` | **Derived:** PLAY-dClosedLoop-2 | a step is refused when the target's own git config declares an executor or a credential |
| 24 | `TOOL-dSafePassage-25` | **Derived:** PLAY-dClosedLoop-2 | a refused gov-first landing removes the untracked files its walk made |
| 25 | `TOOL-dSafePassage-26` | **Derived:** PLAY-dClosedLoop-2 | the round-1 spec audit's 54 minors: one base rule, one writer each, honest populations, declared exits, and the texts that name them |
| 26 | `TOOL-dSafePassage-27` | **Derived:** PLAY-dClosedLoop-2 | the prepared landing's one untracked snapshot, taken before the walk, serves the regeneration's refusal too |
| 27 | `TOOL-dSafePassage-28` | **Derived:** PLAY-dClosedLoop-2 | every refusal of the prepared landing after the walk leaves a clean tree, gated as a class |
| 28 | `TOOL-dSafePassage-29` | **Derived:** PLAY-dClosedLoop-2 | the step contract's refused keys are the class git's own config list derives, held to it by an arm |
| 29 | `TOOL-dSafePassage-30` | **Derived:** PLAY-dClosedLoop-2 | the step contract's config check reads every repository git can enter from the target, its submodules included |
| 30 | `TOOL-dSafePassage-31` | **Derived:** PLAY-dClosedLoop-2 | the write lock records its holder's pid namespace, and a holder from another namespace reads unknown |
| 31 | `TOOL-dSafePassage-32` | **Derived:** PLAY-dClosedLoop-2 | the reuse estimate compares like clocks: a POSIX census row is judged on the kernel's boot clock, never the wall clock |
| 32 | `TOOL-dSafePassage-33` | **Derived:** PLAY-dClosedLoop-2 | a missing before-image means "never ran" only for a row the forward walk applied by witness alone, recorded as such |
| 33 | `TOOL-dSafePassage-34` | **Derived:** PLAY-dClosedLoop-2 | the `ac-order` join ships under a dated cutoff, over a population measured at HEAD with every current hit disposed |
| 34 | `TOOL-dSafePassage-35` | **Derived:** PLAY-dClosedLoop-2 | the round-1 audit of units 15 to 26: its 39 minors, one filtered population, one plan source, pinned plants and the texts that cite them |
| 35 | `TOOL-dSafePassage-36` | **Derived:** PLAY-dClosedLoop-2 | the config check walks the target worktree's own git directory for submodules, so a linked worktree's submodules are graded |
| 36 | `TOOL-dSafePassage-37` | **Derived:** PLAY-dClosedLoop-2 | the refused-key predicate keeps every key named as a hook, and the step environment closes the `ext::` transport by one command-scope pair |
| 37 | `TOOL-dSafePassage-38` | **Derived:** PLAY-dClosedLoop-2 | a credential anywhere in a step target's config is refused by one predicate over keys and values, and no refusal line prints it |
| 38 | `TOOL-dSafePassage-39` | **Derived:** PLAY-dClosedLoop-2 | the step row's `via` mark survives every rewrite that keeps the row `applied`, so the reverse walk's own records cannot erase it |
| 39 | `TOOL-dSafePassage-40` | **Derived:** PLAY-dClosedLoop-2 | the forward walk marks a row `via: witness` only when nothing records that its up ever ran |
| 40 | `TOOL-dSafePassage-41` | **Derived:** PLAY-dClosedLoop-2 | the `ac-order` join lands in the pass that arms it, so no commit carries the join without its cutoff key |
| 41 | `TOOL-dSafePassage-42` | **Derived:** PLAY-dClosedLoop-2 | the spec audit of units 27 to 35: its 27 minors, per-row postconditions, discriminating criteria, one blanked population and the texts that cite them |
| 42 | `TOOL-dSafePassage-43` | **Derived:** PLAY-dClosedLoop-2 | the step row's one writer admits a stopped down's failure on an `applied` row, by one declared prefix set, and refuses every other |
| 43 | `TOOL-dSafePassage-44` | **Derived:** PLAY-dClosedLoop-2 | the credential predicate keeps an ssh-scheme URL's bare user, so an `ssh://git@host` remote is never refused, and holds itself to the repo's redaction negatives |
| 44 | `TOOL-dSafePassage-45` | **Derived:** PLAY-dClosedLoop-2 | the spec audit of units 36 to 42, the step contract's 21 minors: a derived pair count, a credential class over keys and values, a walk by git's own test, declared exits, and the readings that cite them |
| 45 | `TOOL-dSafePassage-46` | **Derived:** PLAY-dClosedLoop-2 | the spec audit of units 36 to 42, its three minors off the step module: the drift pin raised in the pass that arms its key, a lander arm that finds its sibling kit, and the `ac-order` key documented |
| 46 | `TOOL-dSafePassage-47` | **Derived:** PLAY-dClosedLoop-2 | the submodule walk lists a repository by git's own directory shape, and refuses one whose config git cannot read |
| 47 | `TOOL-dSafePassage-48` | **Derived:** PLAY-dClosedLoop-2 | the step contract refuses `sendemail.sendmailCmd` and every send-email executor key in its identity form |
| 48 | `TOOL-dSafePassage-49` | **Derived:** PLAY-dClosedLoop-2 | the spec audit of units 43 to 46, the step module's 20 minors: one step-row predicate, TOOL-4 after TOOL-43, a second walk refusal, identity forms held by the arm, declared exits, and the readings that cite them |
| 49 | `TOOL-dSafePassage-50` | **Derived:** PLAY-dClosedLoop-2 | the spec audit of units 43 to 46, its five minors on TOOL-46: the lander arm placed after the scan it reads, its locator cited by content, and one owner for the cutoff paragraph |
| 50 | `TOOL-dSafePassage-51` | **Derived:** PLAY-dClosedLoop-2 | the spec audit of units 47 to 50, the step module's 15 minors: the build order observed in commit order, the walk's checks in one sequence and no link followed, the guard's keys in the guard, one section probe, and the readings that cite them |
| 51 | `TOOL-dSafePassage-52` | **Derived:** PLAY-dClosedLoop-2 | the spec audit of units 47 to 50, its seven minors on TOOL-50: a misplaced arm that aborts the suite, one scan line, the arm's place read by content, the template repaired through its render, and the readings that cite them |
| 52 | `TOOL-dSafePassage-53` | **Derived:** PLAY-dClosedLoop-2 | the walk's listing handler: an absent directory is the empty population, and only an existing one that cannot be listed is refused |
| 53 | `TOOL-dSafePassage-54` | **Derived:** PLAY-dClosedLoop-2 | the walk's sound baseline: a plain submodule git built and gov's own tree, each walked to exit 0 with no refusal |
| 54 | `TOOL-dSafePassage-55` | **Derived:** PLAY-dClosedLoop-2 | the roster hand-out refuses on TOOL-49 AC2's whole order predicate, written once as one probe |
| 55 | `TOOL-dSafePassage-56` | **Derived:** PLAY-dClosedLoop-2 | the walk tests for a link on every path it enters, the root and each `modules/` it recurses into, before listing it |
| 56 | `TOOL-dSafePassage-57` | **Derived:** PLAY-dClosedLoop-2 | TOOL-52 AC1 reads the arm: its guard taken from the suite by content, evaluated after the scan and alone under `set -u` |
| 57 | `TOOL-dSafePassage-58` | **Derived:** PLAY-dClosedLoop-2 | the spec audit of units 51 and 52, its ten minors on TOOL-52: the arm probe staged, the placement anchored on the block's `fi`, the abort's real exit, and the render's four outputs |
| 58 | `TOOL-dSafePassage-59` | **Derived:** PLAY-dClosedLoop-2 | the spec audit of units 51 and 52, its 12 minors on TOOL-51: the link test's population and form, the `.gitmodules` link refusal, the sweep's own criteria, and the readings that cite them |
| 59 | `TOOL-dSafePassage-61` | **Derived:** TOOL-dSafePassage-1 | the size-limits step and gov's own migration, moved out of TOOL-dSafePassage-1 at its F8 stop and held until the guard admits a value-preserving write |
| 60 | `TOOL-dSafePassage-62` | **Derived:** TOOL-dSafePassage-5 | `update` writes the receipt its file pass moved before the first step, so a walk killed below schema 4 leaves rows a rollback can return |
| 61 | `TOOL-dSafePassage-63` | **Derived:** TOOL-dSafePassage-5 | `update` proves an edit to a rendered file from the sha256 its install recorded, when the row has no `oid` |
| 62 | `TOOL-dSafePassage-64` | **Derived:** TOOL-dSafePassage-5 | a `retired-edited` row takes back the role gov's descriptor gives its path once gov ships that path again |
| 63 | `TOOL-dSafePassage-65` | **Derived:** TOOL-dSafePassage-5 | `update` resolves a row's role from the descriptor at `--to`, not from the gov checkout's working tree |
| 64 | `TOOL-dSafePassage-66` | **Derived:** TOOL-dSafePassage-5 | `update` puts a held kit's writes back before the first upgrade step, so a walk killed inside a step leaves that kit at its pre-run bytes |
| 65 | `TOOL-dSafePassage-67` | **Derived:** TOOL-dSafePassage-26 | the fixture factory pins commit signing and hooks in every repository it builds, and refuses a git command that fails |
| 66 | `TOOL-dSafePassage-68` | **Derived:** TOOL-dSafePassage-26 | the upgrade-walk child's stand-ins take and pass on every parameter of the functions they rebind, held by an arm that reads the live signature |
| 67 | `TOOL-dSafePassage-69` | **Derived:** TOOL-dSafePassage-26 | the floor step's down grades a rollback to the pin under the floor the pin's code needs, and a refused down's reason reaches the step's tail |
| 68 | `TOOL-dSafePassage-70` | **Derived:** TOOL-dSafePassage-35 | a rollback killed after the schema step's down resumes: the reverse walk persists nothing on a receipt already below schema 4, and stops only at the down that lowers it |
| 69 | `TOOL-dSafePassage-71` | **Derived:** TOOL-dSafePassage-42 | govkit selftest's staged-break copies of upgrade_steps.py take the whole govkit directory through one helper, and an arm reds a copy that hand-picks its files |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** DEFERRED · 69 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-14
ids TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28
ids TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42
ids TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56
ids TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-60 TOOL-dSafePassage-61 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70
ids TOOL-dSafePassage-71

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dSafePassage-1 — the upgrade-step kind: the step row, succession rows, their one reader, and frozen landed rows](spec/2026-10-23-spec-TOOL-dSafePassage-1.md) | 1 | 2 | CLOSED | rev-11 | 2026-10-26 |
| [TOOL-dSafePassage-3 — the receipt's schema 4: the `steps` field, its one writer, and the step that ships it](spec/2026-10-23-spec-TOOL-dSafePassage-3.md) | 1 | 2 | CLOSED | rev-6 | 2026-10-26 |
| [TOOL-dSafePassage-16 — the step record's precondition, one predicate beside its one writer, and the schema-4 bootstrap it answers](spec/2026-10-23-spec-TOOL-dSafePassage-16.md) | 2 | 2 | CLOSED | rev-2 | 2026-10-26 |
| [TOOL-dSafePassage-2 — `update` walks the upgrade steps oldest first, and recovers what a killed run left](spec/2026-10-23-spec-TOOL-dSafePassage-2.md) | 2 | 2 | CLOSED | rev-5 | 2026-10-26 |
| [TOOL-dSafePassage-20 — the reader's `unlanded` is recorded as `null` at the step record's one writer](spec/2026-10-23-spec-TOOL-dSafePassage-20.md) | 2 | 2 | CLOSED | rev-2 | 2026-10-26 |
| [TOOL-dSafePassage-4 — down steps in reverse, and the recorded rollback that lifts the downgrade refusal](spec/2026-10-23-spec-TOOL-dSafePassage-4.md) | 2 | 2 | CLOSED | rev-5 | 2026-10-26 |
| [TOOL-dSafePassage-43 — the step row's one writer admits a stopped down's failure on an `applied` row, by one declared prefix set, and refuses every other](spec/2026-10-23-spec-TOOL-dSafePassage-43.md) | 2 | 2 | CLOSED | rev-2 | 2026-10-26 |
| [TOOL-dSafePassage-7 — the step kind's isolation contract, and the check of its needs-target field](spec/2026-10-23-spec-TOOL-dSafePassage-7.md) | 2 | 2 | CLOSED | rev-5 | 2026-10-26 |
| [TOOL-dSafePassage-11 — the interpreter floor at Python 3.15, declared once, refused below by the resolver, and raised as the second upgrade step](spec/2026-10-23-spec-TOOL-dSafePassage-11.md) | 3 | 2 | CLOSED | rev-4 | 2026-10-26 |
| [TOOL-dSafePassage-12 — gov's remote CI at the interpreter floor, read from its one declaration, with the floor's preflight as the bar's first step](spec/2026-10-23-spec-TOOL-dSafePassage-12.md) | 3 | 2 | CLOSED | rev-3 | 2026-10-26 |
| [TOOL-dSafePassage-15 — the walk persists no step row below schema 4, so a schema-3 receipt reaches the schema step](spec/2026-10-23-spec-TOOL-dSafePassage-15.md) | 3 | 2 | CLOSED | rev-2 | 2026-10-26 |
| [TOOL-dSafePassage-18 — the reverse walk writes no row once a down leaves the receipt below schema 4](spec/2026-10-23-spec-TOOL-dSafePassage-18.md) | 3 | 2 | CLOSED | rev-2 | 2026-10-26 |
| [TOOL-dSafePassage-19 — a rollback past the schema step stamps schema 3 with no `steps`, finishes its record, and converges after a kill](spec/2026-10-23-spec-TOOL-dSafePassage-19.md) | 3 | 2 | CLOSED | rev-4 | 2026-10-26 |
| [TOOL-dSafePassage-22 — the lock reclaim reads its clock before the census, so a slow census errs toward live](spec/2026-10-23-spec-TOOL-dSafePassage-22.md) | 3 | 2 | CLOSED | rev-2 | 2026-10-26 |
| [TOOL-dSafePassage-24 — a step is refused when the target's own git config declares an executor or a credential](spec/2026-10-23-spec-TOOL-dSafePassage-24.md) | 3 | 2 | CLOSED | rev-3 | 2026-10-26 |
| [TOOL-dSafePassage-8 — gov first for every step: the lander walks each new step on gov's own tree, recorded in gov's source-mode receipt](spec/2026-10-23-spec-TOOL-dSafePassage-8.md) | 3 | 2 | CLOSED | rev-5 | 2026-10-26 |
| [TOOL-dSafePassage-10 — the step gate: the adopter-visible surface population diffed between a landing's base and its tip](spec/2026-10-23-spec-TOOL-dSafePassage-10.md) | 4 | 2 | CLOSED | rev-4 | 2026-10-26 |
| [TOOL-dSafePassage-17 — a down is judged by its row's declared `reverted` rule, and a down with no before-image by its exit](spec/2026-10-23-spec-TOOL-dSafePassage-17.md) | 4 | 2 | CLOSED | rev-5 | 2026-10-27 |
| [TOOL-dSafePassage-23 — the resolver keeps an override's own name, and prefers the direct executable only for the launcher names](spec/2026-10-23-spec-TOOL-dSafePassage-23.md) | 4 | 2 | CLOSED | rev-2 | 2026-10-27 |
| [TOOL-dSafePassage-25 — a refused gov-first landing removes the untracked files its walk made](spec/2026-10-23-spec-TOOL-dSafePassage-25.md) | 4 | 2 | CLOSED | rev-2 | 2026-10-27 |
| [TOOL-dSafePassage-29 — the step contract's refused keys are the class git's own config list derives, held to it by an arm](spec/2026-10-23-spec-TOOL-dSafePassage-29.md) | 4 | 2 | CLOSED | rev-4 | 2026-10-27 |
| [TOOL-dSafePassage-30 — the step contract's config check reads every repository git can enter from the target, its submodules included](spec/2026-10-23-spec-TOOL-dSafePassage-30.md) | 4 | 2 | CLOSED | rev-3 | 2026-10-27 |
| [TOOL-dSafePassage-32 — the reuse estimate compares like clocks: a POSIX census row is judged on the kernel's boot clock, never the wall clock](spec/2026-10-23-spec-TOOL-dSafePassage-32.md) | 4 | 2 | CLOSED | rev-3 | 2026-10-27 |
| [TOOL-dSafePassage-6 — forwarding shims for a moved command, hook path or module import, held for their deprecation window](spec/2026-10-23-spec-TOOL-dSafePassage-6.md) | 4 | 2 | CLOSED | rev-6 | 2026-10-27 |
| [TOOL-dSafePassage-9 — withdrawn hook fragments unwired, and an edited file gov stopped shipping kept as `retired-edited` and ordered](spec/2026-10-23-spec-TOOL-dSafePassage-9.md) | 4 | 2 | CLOSED | rev-5 | 2026-10-27 |
| [TOOL-dSafePassage-13 — the docs leg: each user-facing member's declared usage fingerprinted against its help page, under help.enforce](spec/2026-10-23-spec-TOOL-dSafePassage-13.md) | 5 | 2 | CLOSED | rev-6 | 2026-10-27 |
| [TOOL-dSafePassage-21 — the step gate's `file` class reads gov's planned destinations when no source receipt is on the tree](spec/2026-10-23-spec-TOOL-dSafePassage-21.md) | 5 | 2 | CLOSED | rev-3 | 2026-10-27 |
| [TOOL-dSafePassage-27 — the prepared landing's one untracked snapshot, taken before the walk, serves the regeneration's refusal too](spec/2026-10-23-spec-TOOL-dSafePassage-27.md) | 5 | 2 | CLOSED | rev-2 | 2026-10-27 |
| [TOOL-dSafePassage-28 — every refusal of the prepared landing after the walk leaves a clean tree, gated as a class](spec/2026-10-23-spec-TOOL-dSafePassage-28.md) | 5 | 2 | CLOSED | rev-3 | 2026-10-27 |
| [TOOL-dSafePassage-33 — a missing before-image means "never ran" only for a row the forward walk applied by witness alone, recorded as such](spec/2026-10-23-spec-TOOL-dSafePassage-33.md) | 5 | 2 | CLOSED | rev-4 | 2026-10-27 |
| [TOOL-dSafePassage-36 — the config check walks the target worktree's own git directory for submodules, so a linked worktree's submodules are graded](spec/2026-10-23-spec-TOOL-dSafePassage-36.md) | 5 | 2 | CLOSED | rev-4 | 2026-10-27 |
| [TOOL-dSafePassage-37 — the refused-key predicate keeps every key named as a hook, and the step environment closes the `ext::` transport by one command-scope pair](spec/2026-10-23-spec-TOOL-dSafePassage-37.md) | 5 | 2 | CLOSED | rev-3 | 2026-10-27 |
| [TOOL-dSafePassage-5 — the release-0 fixture tree and the upgrade-walk leg: every declared step walked up, down and up again over today's install](spec/2026-10-23-spec-TOOL-dSafePassage-5.md) | 5 | 2 | CLOSED | rev-11 | 2026-10-27 |
| [TOOL-dSafePassage-62 — `update` writes the receipt its file pass moved before the first step, so a walk killed below schema 4 leaves rows a rollback can return](spec/2026-10-27-spec-TOOL-dSafePassage-62.md) | 5 | 2 | CLOSED | rev-1 | 2026-10-27 |
| [TOOL-dSafePassage-63 — `update` proves an edit to a rendered file from the sha256 its install recorded, when the row has no `oid`](spec/2026-10-27-spec-TOOL-dSafePassage-63.md) | 5 | 2 | CLOSED | rev-1 | 2026-10-27 |
| [TOOL-dSafePassage-64 — a `retired-edited` row takes back the role gov's descriptor gives its path once gov ships that path again](spec/2026-10-27-spec-TOOL-dSafePassage-64.md) | 5 | 2 | CLOSED | rev-1 | 2026-10-27 |
| [TOOL-dSafePassage-65 — `update` resolves a row's role from the descriptor at `--to`, not from the gov checkout's working tree](spec/2026-10-27-spec-TOOL-dSafePassage-65.md) | 5 | 2 | CLOSED | rev-1 | 2026-10-27 |
| [TOOL-dSafePassage-66 — `update` puts a held kit's writes back before the first upgrade step, so a walk killed inside a step leaves that kit at its pre-run bytes](spec/2026-10-27-spec-TOOL-dSafePassage-66.md) | 5 | 2 | CLOSED | rev-1 | 2026-10-27 |
| [TOOL-dSafePassage-26 — the round-1 spec audit's 54 minors: one base rule, one writer each, honest populations, declared exits, and the texts that name them](spec/2026-10-23-spec-TOOL-dSafePassage-26.md) | 6 | 2 | CLOSED | rev-11 | 2026-10-27 |
| [TOOL-dSafePassage-39 — the step row's `via` mark survives every rewrite that keeps the row `applied`, so the reverse walk's own records cannot erase it](spec/2026-10-23-spec-TOOL-dSafePassage-39.md) | 6 | 2 | CLOSED | rev-3 | 2026-10-27 |
| [TOOL-dSafePassage-40 — the forward walk marks a row `via: witness` only when nothing records that its up ever ran](spec/2026-10-23-spec-TOOL-dSafePassage-40.md) | 6 | 2 | CLOSED | rev-2 | 2026-10-27 |
| [TOOL-dSafePassage-67 — the fixture factory pins commit signing and hooks in every repository it builds, and refuses a git command that fails](spec/2026-10-27-spec-TOOL-dSafePassage-67.md) | 6 | 2 | CLOSED | rev-1 | 2026-10-27 |
| [TOOL-dSafePassage-31 — the write lock records its holder's pid namespace, and a holder from another namespace reads unknown](spec/2026-10-23-spec-TOOL-dSafePassage-31.md) | 7 | 2 | CLOSED | rev-3 | 2026-10-27 |
| [TOOL-dSafePassage-34 — the `ac-order` join ships under a dated cutoff, over a population measured at HEAD with every current hit disposed](spec/2026-10-23-spec-TOOL-dSafePassage-34.md) | 7 | 2 | CLOSED | rev-4 | 2026-10-28 |
| [TOOL-dSafePassage-68 — the upgrade-walk child's stand-ins take and pass on every parameter of the functions they rebind, held by an arm that reads the live signature](spec/2026-10-27-spec-TOOL-dSafePassage-68.md) | 7 | 2 | CLOSED | rev-1 | 2026-10-27 |
| [TOOL-dSafePassage-69 — the floor step's down grades a rollback to the pin under the floor the pin's code needs, and a refused down's reason reaches the step's tail](spec/2026-10-27-spec-TOOL-dSafePassage-69.md) | 7 | 2 | CLOSED | rev-2 | 2026-10-27 |
| [TOOL-dSafePassage-35 — the round-1 audit of units 15 to 26: its 39 minors, one filtered population, one plan source, pinned plants and the texts that cite them](spec/2026-10-23-spec-TOOL-dSafePassage-35.md) | 8 | 2 | CLOSED | rev-7 | 2026-10-28 |
| [TOOL-dSafePassage-41 — the `ac-order` join lands in the pass that arms it, so no commit carries the join without its cutoff key](spec/2026-10-23-spec-TOOL-dSafePassage-41.md) | 8 | 2 | CLOSED | rev-5 | 2026-10-28 |
| [TOOL-dSafePassage-70 — a rollback killed after the schema step's down resumes: the reverse walk persists nothing on a receipt already below schema 4, and stops only at the down that lowers it](spec/2026-10-28-spec-TOOL-dSafePassage-70.md) | 8 | 2 | CLOSED | rev-1 | 2026-10-28 |
| [TOOL-dSafePassage-38 — a credential anywhere in a step target's config is refused by one predicate over keys and values, and no refusal line prints it](spec/2026-10-23-spec-TOOL-dSafePassage-38.md) | 9 | 2 | CLOSED | rev-3 | 2026-10-28 |
| [TOOL-dSafePassage-42 — the spec audit of units 27 to 35: its 27 minors, per-row postconditions, discriminating criteria, one blanked population and the texts that cite them](spec/2026-10-23-spec-TOOL-dSafePassage-42.md) | 10 | 2 | CLOSED | rev-7 | 2026-10-28 |
| [TOOL-dSafePassage-44 — the credential predicate keeps an ssh-scheme URL's bare user, so an `ssh://git@host` remote is never refused, and holds itself to the repo's redaction negatives](spec/2026-10-23-spec-TOOL-dSafePassage-44.md) | 10 | 2 | CLOSED | rev-3 | 2026-10-28 |
| [TOOL-dSafePassage-71 — govkit selftest's staged-break copies of upgrade_steps.py take the whole govkit directory through one helper, and an arm reds a copy that hand-picks its files](spec/2026-10-28-spec-TOOL-dSafePassage-71.md) | 10 | 2 | CLOSED | rev-1 | 2026-10-28 |
| [TOOL-dSafePassage-45 — the spec audit of units 36 to 42, the step contract's 21 minors: a derived pair count, a credential class over keys and values, a walk by git's own test, declared exits, and the readings that cite them](spec/2026-10-23-spec-TOOL-dSafePassage-45.md) | 11 | 2 | CLOSED | rev-3 | 2026-10-28 |
| [TOOL-dSafePassage-46 — the spec audit of units 36 to 42, its three minors off the step module: the drift pin raised in the pass that arms its key, a lander arm that finds its sibling kit, and the `ac-order` key documented](spec/2026-10-23-spec-TOOL-dSafePassage-46.md) | 11 | 2 | CLOSED | rev-3 | 2026-10-28 |
| [TOOL-dSafePassage-47 — the submodule walk lists a repository by git's own directory shape, and refuses one whose config git cannot read](spec/2026-10-23-spec-TOOL-dSafePassage-47.md) | 12 | 2 | CLOSED | rev-3 | 2026-10-28 |
| [TOOL-dSafePassage-48 — the step contract refuses `sendemail.sendmailCmd` and every send-email executor key in its identity form](spec/2026-10-23-spec-TOOL-dSafePassage-48.md) | 12 | 2 | CLOSED | rev-3 | 2026-10-28 |
| [TOOL-dSafePassage-50 — the spec audit of units 43 to 46, its five minors on TOOL-46: the lander arm placed after the scan it reads, its locator cited by content, and one owner for the cutoff paragraph](spec/2026-10-23-spec-TOOL-dSafePassage-50.md) | 12 | 2 | CLOSED | rev-2 | 2026-10-28 |
| [TOOL-dSafePassage-49 — the spec audit of units 43 to 46, the step module's 20 minors: one step-row predicate, TOOL-4 after TOOL-43, a second walk refusal, identity forms held by the arm, declared exits, and the readings that cite them](spec/2026-10-23-spec-TOOL-dSafePassage-49.md) | 13 | 2 | CLOSED | rev-6 | 2026-10-28 |
| [TOOL-dSafePassage-52 — the spec audit of units 47 to 50, its seven minors on TOOL-50: a misplaced arm that aborts the suite, one scan line, the arm's place read by content, the template repaired through its render, and the readings that cite them](spec/2026-10-23-spec-TOOL-dSafePassage-52.md) | 13 | 2 | CLOSED | rev-3 | 2026-10-28 |
| [TOOL-dSafePassage-51 — the step module's 15 audit minors from units 47 to 50: build order in commit order, the walk's checks in one sequence, the guard's keys, one section probe](spec/2026-10-23-spec-TOOL-dSafePassage-51.md) | 14 | 2 | CLOSED | rev-4 | 2026-10-28 |
| [TOOL-dSafePassage-57 — TOOL-52 AC1 reads the arm: its guard taken from the suite by content, evaluated after the scan and alone under `set -u`](spec/2026-10-23-spec-TOOL-dSafePassage-57.md) | 14 | 2 | CLOSED | rev-2 | 2026-10-28 |
| [TOOL-dSafePassage-58 — the spec audit of units 51 and 52, its ten minors on TOOL-52: the arm probe staged, the placement anchored on the block's `fi`, the abort's real exit, and the render's four outputs](spec/2026-10-23-spec-TOOL-dSafePassage-58.md) | 14 | 2 | CLOSED | rev-1 | 2026-10-28 |
| [TOOL-dSafePassage-53 — the walk's listing handler: an absent directory is the empty population, and only an existing one that cannot be listed is refused](spec/2026-10-23-spec-TOOL-dSafePassage-53.md) | 15 | 2 | CLOSED | rev-2 | 2026-10-28 |
| [TOOL-dSafePassage-54 — the walk's sound baseline: a plain submodule git built and gov's own tree, each walked to exit 0 with no refusal](spec/2026-10-23-spec-TOOL-dSafePassage-54.md) | 15 | 2 | CLOSED | rev-2 | 2026-10-28 |
| [TOOL-dSafePassage-55 — the roster hand-out refuses on TOOL-49 AC2's whole order predicate, written once as one probe](spec/2026-10-23-spec-TOOL-dSafePassage-55.md) | 15 | 2 | WONTDO | rev-2 | 2026-10-28 |
| [TOOL-dSafePassage-56 — the walk tests for a link on every path it enters, the root and each `modules/` it recurses into, before listing it](spec/2026-10-23-spec-TOOL-dSafePassage-56.md) | 15 | 2 | DEFERRED | rev-3 | 2026-10-28 |
| [TOOL-dSafePassage-59 — the spec audit of units 51 and 52, its 12 minors on TOOL-51: the link test's population and form, the `.gitmodules` link refusal, the commit-order criterion's attribution and form, and the readings that cite them](spec/2026-10-23-spec-TOOL-dSafePassage-59.md) | 15 | 2 | DEFERRED | rev-3 | 2026-10-28 |
| [TOOL-dSafePassage-61 — the size-limits step and gov's own migration, held until the guard admits a value-preserving write](spec/2026-10-26-spec-TOOL-dSafePassage-61.md) | 16 | 2 | DEFERRED | rev-2 | 2026-10-26 |
<!-- /gen:build-units -->

Records: 359 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-61 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65
TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71.

Ids whose spec moved past its audited revision: TOOL-dSafePassage-1@rev-2 TOOL-dSafePassage-10@rev-1 TOOL-dSafePassage-11@rev-1 TOOL-dSafePassage-12@rev-1 TOOL-dSafePassage-13@rev-1 TOOL-dSafePassage-15@rev-1 TOOL-dSafePassage-16@rev-1 TOOL-dSafePassage-17@rev-1 TOOL-dSafePassage-18@rev-1
TOOL-dSafePassage-19@rev-1 TOOL-dSafePassage-2@rev-1 TOOL-dSafePassage-20@rev-1 TOOL-dSafePassage-21@rev-1 TOOL-dSafePassage-22@rev-1 TOOL-dSafePassage-23@rev-1 TOOL-dSafePassage-24@rev-1 TOOL-dSafePassage-25@rev-1 TOOL-dSafePassage-26@rev-1 TOOL-dSafePassage-27@rev-1 TOOL-dSafePassage-28@rev-1
TOOL-dSafePassage-29@rev-1 TOOL-dSafePassage-3@rev-1 TOOL-dSafePassage-30@rev-1 TOOL-dSafePassage-31@rev-1 TOOL-dSafePassage-32@rev-1 TOOL-dSafePassage-33@rev-1 TOOL-dSafePassage-34@rev-1 TOOL-dSafePassage-35@rev-1 TOOL-dSafePassage-36@rev-1 TOOL-dSafePassage-37@rev-1 TOOL-dSafePassage-38@rev-1
TOOL-dSafePassage-39@rev-1 TOOL-dSafePassage-4@rev-1 TOOL-dSafePassage-40@rev-1 TOOL-dSafePassage-41@rev-1 TOOL-dSafePassage-42@rev-1 TOOL-dSafePassage-43@rev-1 TOOL-dSafePassage-44@rev-1 TOOL-dSafePassage-45@rev-1 TOOL-dSafePassage-46@rev-1 TOOL-dSafePassage-47@rev-1 TOOL-dSafePassage-48@rev-1
TOOL-dSafePassage-49@rev-2 TOOL-dSafePassage-5@rev-1 TOOL-dSafePassage-50@rev-1 TOOL-dSafePassage-51@rev-1 TOOL-dSafePassage-52@rev-1 TOOL-dSafePassage-6@rev-1 TOOL-dSafePassage-7@rev-1 TOOL-dSafePassage-8@rev-1 TOOL-dSafePassage-9@rev-1.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dSafePassage's 13 clause(s) and 5 owned node(s), over 68 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 11
- carried in parts: 2 (cl-dClosedLoop-0018, cl-dClosedLoop-0022)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: `spec/2026-10-23-spec-TOOL-dSafePassage-15.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-16.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-17.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dSafePassage-18.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-19.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-20.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-21.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dSafePassage-22.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-23.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-24.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-25.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dSafePassage-26.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-27.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-28.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-29.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dSafePassage-30.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-31.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-32.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-33.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dSafePassage-34.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-35.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-36.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-37.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dSafePassage-38.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-39.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-40.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-41.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dSafePassage-42.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-43.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-44.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-45.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dSafePassage-46.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-47.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-48.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-49.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dSafePassage-50.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-51.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-52.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-53.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dSafePassage-54.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-56.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-57.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dSafePassage-58.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dSafePassage-59.md` (PLAY-dClosedLoop-2), `spec/2026-10-27-spec-TOOL-dSafePassage-63.md` (TOOL-dSafePassage-5), `spec/2026-10-27-spec-TOOL-dSafePassage-64.md` (TOOL-dSafePassage-5), `spec/2026-10-27-spec-TOOL-dSafePassage-65.md` (TOOL-dSafePassage-5),
  `spec/2026-10-27-spec-TOOL-dSafePassage-66.md` (TOOL-dSafePassage-5), `spec/2026-10-27-spec-TOOL-dSafePassage-67.md` (TOOL-dSafePassage-26), `spec/2026-10-27-spec-TOOL-dSafePassage-68.md` (TOOL-dSafePassage-26), `spec/2026-10-27-spec-TOOL-dSafePassage-69.md` (TOOL-dSafePassage-26),
  `spec/2026-10-28-spec-TOOL-dSafePassage-70.md` (TOOL-dSafePassage-35), `spec/2026-10-28-spec-TOOL-dSafePassage-71.md` (TOOL-dSafePassage-42)
- clauses the token arm cannot see: cl-dClosedLoop-0021
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dSafePassage-1`, `TOOL-dSafePassage-3` | no |
| 2 | `TOOL-dSafePassage-16`, `TOOL-dSafePassage-2`, `TOOL-dSafePassage-20`, `TOOL-dSafePassage-4`, `TOOL-dSafePassage-43`, `TOOL-dSafePassage-7` | no |
| 3 | `TOOL-dSafePassage-11`, `TOOL-dSafePassage-12`, `TOOL-dSafePassage-15`, `TOOL-dSafePassage-18`, `TOOL-dSafePassage-19`, `TOOL-dSafePassage-22`, `TOOL-dSafePassage-24`, `TOOL-dSafePassage-8` | no |
| 4 | `TOOL-dSafePassage-10`, `TOOL-dSafePassage-17`, `TOOL-dSafePassage-23`, `TOOL-dSafePassage-25`, `TOOL-dSafePassage-29`, `TOOL-dSafePassage-30`, `TOOL-dSafePassage-32`, `TOOL-dSafePassage-6`, `TOOL-dSafePassage-9` | no |
| 5 | `TOOL-dSafePassage-13`, `TOOL-dSafePassage-21`, `TOOL-dSafePassage-27`, `TOOL-dSafePassage-28`, `TOOL-dSafePassage-33`, `TOOL-dSafePassage-36`, `TOOL-dSafePassage-37`, `TOOL-dSafePassage-5`, `TOOL-dSafePassage-62`, `TOOL-dSafePassage-63`, `TOOL-dSafePassage-64`, `TOOL-dSafePassage-65`, `TOOL-dSafePassage-66` | no |
| 6 | `TOOL-dSafePassage-26`, `TOOL-dSafePassage-39`, `TOOL-dSafePassage-40`, `TOOL-dSafePassage-67` | no |
| 7 | `TOOL-dSafePassage-31`, `TOOL-dSafePassage-34`, `TOOL-dSafePassage-68`, `TOOL-dSafePassage-69` | no |
| 8 | `TOOL-dSafePassage-35`, `TOOL-dSafePassage-41`, `TOOL-dSafePassage-70` | no |
| 9 | `TOOL-dSafePassage-38` | no |
| 10 | `TOOL-dSafePassage-42`, `TOOL-dSafePassage-44`, `TOOL-dSafePassage-71` | no |
| 11 | `TOOL-dSafePassage-45`, `TOOL-dSafePassage-46` | yes |
| 12 | `TOOL-dSafePassage-47`, `TOOL-dSafePassage-48`, `TOOL-dSafePassage-50` | no |
| 13 | `TOOL-dSafePassage-49`, `TOOL-dSafePassage-52` | yes |
| 14 | `TOOL-dSafePassage-51`, `TOOL-dSafePassage-57`, `TOOL-dSafePassage-58` | no |
| 15 | `TOOL-dSafePassage-53`, `TOOL-dSafePassage-54`, `TOOL-dSafePassage-55`, `TOOL-dSafePassage-56`, `TOOL-dSafePassage-59` | unknown |
| 16 | `TOOL-dSafePassage-61` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dGroundRules](../dGroundRules/README.md)
- **Child builds:** [dFairHearing](../dFairHearing/README.md), [dOrderedCharter](../dOrderedCharter/README.md)
<!-- /gen:build-edges -->
