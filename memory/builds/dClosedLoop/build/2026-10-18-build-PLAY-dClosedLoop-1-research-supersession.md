# Research: the rebuilt kits superseding today's, seamlessly

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 111's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-14-researcher.md`, and its use is in `build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md`.

---

## 1. Verdict

I recommend **release-chained upgrade steps**. Each chain build that changes something an adopter can see ships two things in the same landing: the successor, and a declared upgrade step that can run in both directions. `govkit update` then walks those steps in order, keyed by gov commit (later by release tag). This extends today's row engine, and gov runs each step on itself first (P8).

Today's engine can't do this. A receipt that names a retired kit refuses the whole update (probe below). A downgrade is refused, so nothing can be rolled back across versions. Moved conf keys are only reported. An edited file of a retired part stays where it is, silently.

The other four candidates each lose a test: an epoch, shims alone, a translation layer alone, and a re-install. Shims and translation survive only as bounded windows, each controlled by a policy key.

## 2. Today's update path

What `_cmd_update` does (tools/govkit/govkit.py:8777-12094), in order, for an adopter on an older receipt:

| # | Step | Code | Effect |
|---|---|---|---|
| 1 | Refuse if the target is gov's own checkout | :8794-8795 | **gov can never update itself** |
| 2 | Read the receipt; refuse if there is none | :8797-8799 | — |
| 3 | Warn if the measurer's own clone is behind | :8805-8824 | warning only |
| 4 | Refuse if the receipt's `gov_commit` is unresolvable | :8832-8844 | — |
| 5 | Write preconditions: no operation in progress, index resolved, claimed paths clean, lock | :7164-7175 | a dirty claimed path refuses with "Commit or stash" (:7103-7106) |
| 6 | Refuse a downgrade; refuse an unpublished `--to` | :7178-7198, :7200-7215 | **"A DOWNGRADE IS NOT AN UPDATE"** |
| 7 | **Refuse a claimed kit that is no longer a registry entry** | :8855-8861 | a retired or absorbed kit stops the whole run |
| 8 | Install default-gained entries | :8863-8868 | additive |
| 9 | Migrate the receipt schema (<3 back-fills `gov_oid`) | :8950-8961 | the only data migration today |
| 10 | Check integrity, containment and untracked shadows | :8963-9107 | refusals |
| 11 | Build a rename map with `git diff -M50%`, unscoped | :8416-8452, :8413 | a moved file gets `renamed`, `git mv` plus a three-way merge |
| 12 | Classify each row: (ours, theirs) grid | :8042-8052, :8455-8578 | see the surface table |
| 13 | Snapshot and baseline, before any write | :9919-10016 | per row |
| 14 | Write loop: raw write for `stale`/`missing`, three-way for `diverged`, conflict orders | :10117-10488, :8060-8078 | stages into the index and **never commits** |
| 15 | Re-render and regenerate (target-side argvs) | :10825 | — |
| 16 | Wire new hook fragments | :11062-11127 | wires only; nothing is unwired except on rollback (:11304) |
| 17 | Verify each touched kit; roll back on a green-to-red transition | :11128-11660 | rollback is **within one run, per kit**; writes an `update-rollback-<kit>.md` order (:11556) |
| 18 | Re-stamp the receipt; emit gate legs | :11836 | `gov_source` is a local path (:8020) |

What each surface gets:

| Surface | Today | Code |
|---|---|---|
| Retired or renamed **kit** | whole-run refusal; `check` reds | :8857; probe A |
| Renamed **file** (≥50% similar) | moved, local edit three-way merged | :8536-8568 |
| File gov stopped shipping, adopter **unedited** | `withdrawn`: an outbox order; deleted only with `--write-withdrawals` | :10364-10400 |
| File gov stopped shipping, adopter **edited** | `("differs","absent")` gives `patched`, not a touching verdict, so **no action and no order** | :8048, :8078 |
| Adopter-owned row (`project-owned`) | skipped | :8104 |
| Kit **conf** whose keys moved | `seed` rows never written; prints `CONF GAP` | :8103, :10939-10943 |
| **Hooks** of a withdrawn file | the file stays, so the hook stays wired and keeps running | :11062-11127 |
| **Records** in an older shape | untouched; old shapes are exempted by 21 date cutoffs | `.memory-tree.conf` |
| Half-applied run | the lock is left behind and the operator must `rm` it by hand (:7138-7141); the staged index then refuses the next run (:7103) | — |

**Probe A** checks a receipt that claims a kit the registry no longer has. I made a throwaway target under `.../d111/t-retired`:
```
$ python tools/govkit/govkit.py check --target "$P/t-retired"
govkit: the receipt claims kit 'unattended-retired-probe', which is not a registry entry
govkit: 1 problem(s)        exit=1
```

**Probe B** plans gov's own selection (`.governance/deploy.toml`) into a fresh target:
```
$ python tools/govkit/govkit.py plan --target "$P/t-fresh"
govkit: the target descriptor's 'answers.stream_ownership' is '...', which carries '—' ... Refusing   exit=2
```
Gov's own deploy file is refused, so gov can't be planned as an adopter (P8). With the answers sanitized:
```
govkit plan — 228 write(s), 109 order(s), 18 side-effect(s), 2 covered, 3 blocked ... NOTHING was written.
rows by destination: tools/ 283 · root 33 · .governance/ 20 · memory/ 11 · .claude/ 7 · .githooks/ 4
rows from absorbed kits: unattended 70 + agent-instructions 4 = 74 of 358
```

**What an adopter's tree carries.** I measured this from the descriptors, gov's own tree and the fixture:
- Descriptor rules over 29 entries: 45 engine, 31 project-owned, 24 rendered, 10 seed, 3 merged, 1 generated.
- 9 kits declare `[config]` over 5 conf files. Gov's own confs hold 141 keys (memory-tree 61, unattended 63, codebase-map 7, process-monitor 6, lexicon 4), plus 6 in `gate-env.sh`.
- Gov has 13 wired hook commands; 3 of them point into `tools/unattended/`. It also has 7 rendered Skills, 9 agents and 11 guides, 4 of them `UNATTENDED-*`.
- The receipt fixture `tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json` (adopter `ic`) has 52 rows, and **19 belong to `unattended`**. Of those 19, 14 hold bytes that differ from gov's blob. Since its vintage, 44 of its 47 engine rows moved on gov's side, over 4,896 gov commits.
- Gov's history since that vintage, under `tools/ skills/ .githooks/`, shows 0 renames and 2 deletions. The rename and withdrawal arms have barely been exercised in real use.

## 3. The mapping

These are the fates table's 131 rows, re-counted. They match the record (fates.md:69-70).

| Fate | Rows | Of which unattended | Commands/Skills | Hooks | Conf/policy | Records/templates |
|---|---|---|---|---|---|---|
| STAYS | 24 | 0 | 8 | 6 | 1 | 3 |
| RESHAPED (changes shape) | 70 | 11 | 26 | 15 | 2 | 26 |
| MERGED (moves) | 23 | 2 | 13 | 0 | 2 | 3 |
| RETIRED | 14 | 9 | 3 | 3 | 1 | 4 |

The surface columns come from a keyword classifier over each row's function, job and destination cells. They are indicative only; a row can count under several surfaces or none.

At kit level, 2 of 19 kits are absorbed (agent-instructions, unattended) and 2 are new (the loop kit and the runtime's own kit). Govkit and lib gain descriptors. On top of the rows, dConvergedCharter folds every unconverted conf key (up to 141 in gov) into `.governance/policy.toml`. 107 of the 131 rows (82%) change shape, move or retire. Today's engine handles a move only when git pairs the rename at ≥50% similarity, and an absorbed kit's files mostly don't pair.

## 4. Candidates

The seam is govkit `update`: its row grid, rename map, transition-keyed rollback and outbox orders. Precedents in gov:
- `migrate_backlog.py`, a planner with `--dry-run`, `--write` and `--stragglers` (tools/memory-tree/migrate_backlog.py:1-20);
- the receipt's own schema migration (:8950);
- `transition_audit.read_modes`, which reads the old or new shape per commit (tools/memory-tree/transition_audit.py:418-435);
- v2 using shims ad hoc, in two places: `map_lib` "re-exports the moved names for one release" (dOrderedCharter), and `/unattended` as a client of `run` (dWellOiledMachine).

| | **E. Release-chained upgrade steps** (recommended) | A. Epoch | B. Side-by-side shims | C. Core translation layer | D. Re-install |
|---|---|---|---|---|---|
| Mechanism | Each chain build declares `[[upgrade]]` steps in its kit descriptor (id, introducing commit, up and down argv run from gov's checkout, witness, surfaces, `needs-target`). The registry gains `[[retired]]` rows (old id → successor or none). `update` walks every step whose introducing commit lies between the receipt's vintage and `--to`, oldest first. | Adopters stay on the last pre-chain commit; one release at dConvergedCharter runs one big migration program | The successor lands next to its predecessor; the old path becomes a forwarder that warns, until a retirement release | The new core reads old confs, records and receipts until an upgrade step rewrites them | Remove the old install, `apply` the new one, re-adopt |
| Order in one run | preconditions → receipt schema → registry succession → file rows (successor-aware) → data steps in declared order → re-render → wire and unwire hooks → per-kit verify plus step witnesses → stamp `steps` | the same, once, over the whole gap | ordinary update rows | none: reads are lazy | uninstall → apply |
| Idempotence | step keyed by id in the receipt and skipped when its witness holds (P24) | one giant step: all or nothing | file rows only | n/a | n/a |
| Reversibility | each step's down runs in reverse; rollback is one revert of the adopter's update commit, plus down steps for anything outside the tree (`install.guards: managed`, refs) | revert of one huge commit; per-kit rollback can't apply because the kits are coupled | the old surface is still there | trivial | none |
| Adopter's edits | engine edits: three-way merge, as today. An edit to a retired part: an order plus a `forked` row (new). Conf values carried by the step, never reset to defaults. Project-owned rows never touched (:8104) | a three-way merge across 20 builds; retired parts silently `patched` | an edited predecessor becomes `diverged` against the shim, and the edit's logic is lost | kept, unread | lost or forked |
| Half-applied | per-kit rollback (exists) plus reverse down steps; a stale lock reclaimed by checking whether its pid is alive (new) | whole run | as today | n/a | — |
| **Losing test** | A release-0 fixture tree (today's kits, with planted edits: an engine edit, an old-key conf, a project-owned row, a wired hook, an old-shape record, an edited retired file) walked up, down, then up again. It loses if down isn't byte-identical (tree and receipt), or if any planted edit is neither carried nor ordered. | Under v2's own defaults, `kits.cadence: weekly` (v2:944) and `currency.max-behind: 2` (v2:937), an adopter held for a 20-build chain goes over budget after 2 releases | Find one surface a shim can't forward | An adopter-invoked command whose file the update withdrew | Adopter edits survive |
| **Result** | **Not runnable today: the step kind doesn't exist.** The seam fails two of its preconditions, measured: a retired entry refuses (probe A, :8857) and a down is refused (:7178). Those become the build's first units. | **LOSES** by the design's own defaults. The fixture shows the size of the jump: 44/47 engine rows moved; 14 of 19 absorbed-kit rows differ adopter-side and would read `patched`, silent (:8048) | **LOSES**: old-shape records and conf files can't be forwarded; 9 RETIRED unattended rows have no successor to forward to (`--attest`, stop-guard, `RESUME_SCHEDULE_*`); and a shim with no enforcer is a bypass P16 refuses | **LOSES**: nothing to translate for a withdrawn script; permanent dual readers break P10's "one reader" | **LOSES**: `apply` refuses a tree carrying kits its receipt doesn't claim (:7257-7263); in the fixture, 29/47 engine rows differ from gov's blob |
| Kept as | the mechanism | — | a **bounded window** for commands and hook paths only, `install.deprecation-window` | a **bounded window** between a release landing and its step running (dGroundRules' legacy-homes list already is this) | — |

**Gov itself (P8) under E.** The lander runs each step that a landing introduces on gov's own tree in the prepared merge, the way `mint` already runs there (USAGE :13228-13231). Gov is therefore the first tree every step migrates. Gov's source-mode receipt (DI-1) records the steps, and probe B's refusal has to be fixed so that gov's `deploy.toml` plans.

## 5. Seamless, verified

"Seamless" means four things. No adopter takes a manual step. No adopter edit is lost silently. Every surface an adopter can see either works or warns until its window closes. And any update can be undone by one action.

| Instrument | What it proves | Owner |
|---|---|---|
| `upgrade-walk` leg over a **release-0 fixture tree**: the planted cases above, generated by `apply` at a pinned commit into a scratch clone | up, then down byte-identical, then up again; every planted edit carried or ordered; `check` green after | step-kind build |
| The same walk run with each step skipped once | each step's witness is load-bearing, and the walk reds without it | step-kind build |
| Conformance arm: every RESHAPED, MERGED or RETIRED fates row that touches an adopter-visible surface names a step, a `[[retired]]` row or "internal" | no migration missing | joined into the fates check (fates.md `[check]`) |
| Registry arm: every removed entry has a `[[retired]]` row | probe A can't recur | step-kind build |
| Receipt schema 4 gains `steps[]` (id, introducing commit, up-witness SHA), `superseded[]` (old kit → successor), `deprecations[]` (surface, retire-at), `prior_commit` | rollback target and currency inputs | dShippedRelease |
| `kits.currency` gains readings: steps pending, attended steps owed, shim calls journaled | the watch sees a stuck migration, not only being behind | dShippedRelease |
| Fleet register row per adopter (by key) | release, behind, steps pending, shim calls, open conflict orders | dShippedRelease |

What the owner sees:
- each release's notes carry a "superseded" section generated from the steps and the fates table;
- the fleet view shows one line per adopter;
- an owner item opens only for an attended step, a conflict order, or a shim still in use after its window. Otherwise nothing.

## 6. Chain, gaps and forks

**Units by build:**

| Build | Unit |
|---|---|
| **New `dHandedOver`** (parent dGroundRules, before dOrderedCharter); see fork F2 | the `[[upgrade]]` step kind and its factory; `[[retired]]` succession rows read by `update` and `check`; the commit-keyed step walk; reverse down steps and a rollback mode that lifts :7178 for a recorded rollback only; stale-lock reclaim; unwiring of withdrawn hook fragments; edited retired files becoming orders plus `forked` rows; the release-0 fixture and the `upgrade-walk` leg; the lander running new steps on gov; probe B's refusal fixed |
| dOrderedCharter | the first steps: agent-instructions' wiring moves to the one renderer; the `map_lib` re-export becomes a declared deprecation |
| dGroundRules | its legacy-homes list declared as the translation window's population |
| dWellOiledMachine | steps re-pointing the unattended hooks into dispatcher packs; `/unattended` shim with a declared retire-at |
| dShippedRelease | receipt schema 4's new fields; currency and fleet readings; `kits.offer` running steps that are not `needs-target`; the backlog migration (NP-22) declared as a step, its first instance |
| dConvergedCharter | the conf fold and the unattended retirement shipped as steps; shims removed at window close; exit check: every registered adopter at the converged commit with 0 pending steps, or an owner item for that adopter |

**Gaps to register** (the next free ids):

| Id | Sev | What | Evidence |
|---|---|---|---|
| gap-deploy-15 | HIGH | A retired or absorbed entry refuses the whole update, and `check` reds | govkit.py:8855-8861, :5421-5423; probe A |
| gap-deploy-16 | HIGH | No upgrade-step kind: moved conf keys are only reported; old record shapes are carried by 21 cutoffs; the backlog migration stands alone | :8103, :10939-10943; `.memory-tree.conf` |
| gap-deploy-17 | MED | No rollback across versions; rollback exists only inside one run, per kit | :7178-7198, :11128 |
| gap-deploy-18 | MED | An edited file gov retired reads `patched` with no order; a withdrawn hook stays wired | :8048, :8078, :11304 |
| gap-deploy-19 | MED | Recovering a half-applied update is manual (`rm` the lock, clear staged paths) | :7138-7141, :7103-7106 |
| gap-deploy-20 | MED | Gov can't run `update` on itself, and its `deploy.toml` is refused by `plan` | :8794-8795; probe B |
| gap-tool-10 | LOW | No release-0 adopter tree fixture: the only fixture is a receipt, and the rename arm is graded only by authored fixtures | `tools/govkit/fixtures/`; 0 renames since that fixture's vintage |

**Where a record and the code disagree:**
- v2's dShippedRelease row calls the backlog migration "an update's upgrade step", but `update` has no step mechanism; `migrate_backlog.py` runs on its own.
- v2's dOrderedCharter re-exports `map_lib` "for one release", but no release has ever been cut (gap-deploy-11), so "one release" isn't defined yet.

**Forks for the owner:**

| Fork | Options | Recommendation |
|---|---|---|
| F1: the mechanism | E release-chained steps · A epoch · B shims · C translation | **E**. A loses by v2's own currency defaults; B and C lose on surfaces they can't reach. |
| F2: where the step kind is built | new `dHandedOver` ahead of dOrderedCharter · folded into dGroundRules · left in dShippedRelease with adopters frozen until it lands | **new build**. dOrderedCharter is the first build that changes adopter surfaces (v2 says its template is "re-copied into adopters through govkit's update"). Keying steps by gov commit means no release is needed first. |
| F3 policy `install.deprecation-window` | 0, 1, 2, 4 releases | **2**, equal to `currency.max-behind`'s default, so an adopter inside its currency budget never meets a removed surface |
| F4 policy `install.on-shim-call` | warn, journal, refuse | **warn** (prints, and journals for the fleet view) |
| F5 policy `install.retired-edits` | order, keep, delete | **order**: the file is kept, its row marked `forked`, and an outbox order written. `keep` is today's silent `patched`; `delete` loses edits. |
| F6 policy `install.steps` | offer, attended | **offer**: gov-authored steps run inside `kits.offer`'s no-target-code mode; a `needs-target` step always falls back to attended (NP-22) |
| F7: gov under P8 | the lander runs each new step on gov, recorded in the source-mode receipt · gov's own diff is its migration | **lander runs it**. Otherwise the path adopters take is never exercised in gov. |

Probe directory, with throwaway targets only: `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/away/d111/`

Files read:
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/govkit/govkit.py`
- `.../tools/govkit/registry.toml`
- `.../tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json`
- `.../tools/memory-tree/migrate_backlog.py`
- `.../tools/memory-tree/transition_audit.py`
- `.../memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md`
- `.../memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
- `.../memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`
