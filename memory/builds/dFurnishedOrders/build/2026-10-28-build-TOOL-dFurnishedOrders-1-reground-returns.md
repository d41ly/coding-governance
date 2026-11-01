**Serves:** research TOOL-dFurnishedOrders-1

# dFurnishedOrders — the re-ground writers' returns, verbatim

The `gov-spec-writer` returns for the brief
[`2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-reground`](../prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-reground.md),
each copied from its agent transcript; only the headings are the main loop's. Group B's writer was resumed once, for the fo11 mirror line Group C's revision of fo29 left stale.

## Group A, catalogue defaults

Specs 2, 5, 8, 16 and 18.

I revised all five Group A specs: 2, 5, 8, 16 and 18. I re-read both sides of each row before editing, and each row held, so none is refused. No fork was added, re-resolved or re-opened, and no spec hits the 49152-byte cap.

Each spec now reads its key with `read_policy_setting(..., with_default=True)`, as br21 S1 (br21:41-50) and br43 S21 (br43:105-110) require. A None now means only that no policy kit was found.

##### TOOL-dFurnishedOrders-2 (row 6)
- **Rev:** rev-3, 2026-10-28, still DEFERRED.
- **Moved:** §2 S5, plus a §9 line.
- **Change:** `prompts.batch` is read with `with_default=True`. The roles-kit copy of `per-batch` is gone. A None means only the absent policy kit, which gives F3's `per-task` and its note. F3 still holds, so it is unchanged.
- **Bytes:** 20156.

##### TOOL-dFurnishedOrders-5 (row 19)
- **Rev:** rev-3, 2026-10-28.
- **Moved:** §2 S3, the error-states line in §5, plus a §9 line.
- **Change:** both keys are read with `with_default=True`. `keyed` and `cold` stay only as the fallback when no policy kit is found, beside br21 S1's note, and AC9 holds that fallback to the catalogue.
- **Bytes:** 25486.

##### TOOL-dFurnishedOrders-8 (row 35)
- **Rev:** rev-3, 2026-10-28.
- **Moved:** §2 S4, the error-states line in §5, plus a §9 line.
- **Change:** `instructions.slices` is read with `with_default=True`, and the typed `handed` default is gone.
- **One reading of the brief:** when no policy kit is found, the spec still renders `handed`, as that case's fallback with its note. I took "the typed `handed` goes" to mean the default copy goes, not this fallback. Row 35's `Change:` says "with its own fallback and note", and AC9 (fo8:287-288) already renders `handed` with the policy kit removed. Removing it would change what the unit builds, which the re-ground does not force. If you meant the fallback to go too, AC9 has to change, and that is a fork.
- **Bytes:** 29247.

##### TOOL-dFurnishedOrders-16 (row 63)
- **Rev:** rev-4, 2026-10-28.
- **Moved:** §2 S1, §6 AC1, plus a §9 line.
- **Change:** `attendance` is read with `with_default=True`, so an unset key gets the catalogue's `unattended` (`tools/policy/catalogue.toml:60-63`). A None (no policy kit) now takes S1's existing `unread: <why>` path, which answers attended.
- **AC1 change:** AC1 gains a "policy kit removed" case and its "Red when" line, so the moved branch has an observation. This edit goes beyond the row's `Change:`; please confirm it.
- **Bytes:** 29074.

##### TOOL-dFurnishedOrders-18 (row 77)
- **Rev:** rev-3, 2026-10-28.
- **Moved:** §2 S5 and §2 S2, plus a §9 line.
- **Change:** `annotations.delivery` is read with `with_default=True`. The literal `work-order` stays only for the no-policy-kit None.
- **Edit outside the row:** S2 (fo18:47-48) spelled `read_policy_setting("instructions.slices", root)` "as TOOL-dFurnishedOrders-8 S4 reads it". My fo8 revision made that false, so I aligned it to the `with_default=True` form. The record has no row for it; it is the same mismatch as row 35, inside my group.
- **Bytes:** 23018.

##### Acceptance checks
- Every byte count is under 49152, every **Status:** line carries the new rev, and every §9 has its new 2026-10-28 line.
- Grepping for each quoted sentence (fo2:65-67, fo5:46-48, fo8:51-52, fo16:36, fo18:70-71) prints nothing.
- `read_policy_setting(` without `with_default` appears nowhere in the five specs.
- **Hygiene gate:** I ran it over an index copy with only these five specs staged. It exits 1 on check 9 alone, the build-index render (`gen_build_index.py --write` is owed for `memory/LIVE.md` and the dFurnishedOrders README). That render is the main loop's to do.
  - It reports two stale dLinkedLibrary files. That spec has unstaged changes in the worktree from before this task, and I did not edit it.
  - It notes that check 25 did not grade `owner-question` at fo16 S3, because no reader for it exists in the tree. That is a "did not grade" note, not a finding, and I did not touch S3.
- I deleted the index copy and its folder, and the real index has nothing staged.

##### For the main loop and other groups
- **fo29 S16 (Group C):** the returns record (line 84) says fo29 S16, "per-batch on a None from any cause", must be reconciled with fo2's revised S5 in the same pass.
- **Parent specs:** none looks wrong. br21 S1 and br43 S21/AC21 bore out all five rows.

Files:
- C:/projects/coding-governance/.claude/worktrees/beautiful-lalande-23ce8b/memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-2.md
- C:/projects/coding-governance/.claude/worktrees/beautiful-lalande-23ce8b/memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-5.md
- C:/projects/coding-governance/.claude/worktrees/beautiful-lalande-23ce8b/memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-8.md
- C:/projects/coding-governance/.claude/worktrees/beautiful-lalande-23ce8b/memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-16.md
- C:/projects/coding-governance/.claude/worktrees/beautiful-lalande-23ce8b/memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-18.md

## Group B, policy reads and the loop render

Specs 7, 11, 12, 17 and 20.

I revised all five Group B specs (7, 11, 12, 17, 20). I refused no record row: I re-read both sides of each one, and the parent text bears every one out. Each spec is now `DEFERRED · rev-3 · 2026-10-28` with a new §9 line naming the sections it moved and its cross-check rows, and each is under 49152 bytes. For every row, `grep -n -F` for the quoted sentence prints nothing, except the corrected sentence in fo20. The memory hygiene gate ran over an index copy holding only my five specs and named none of them; I deleted the copy and the `fo-wB/` scratch folder afterwards, and staged nothing into the real index. I did not run the naming lexicon, because these revisions add no new identifier.

| Spec | Rows | Rev | Bytes | Sections moved |
|---|---|---|---|---|
| 17 | 68, 71, 72, 73 | rev-3 | 21136 | §2 S1, S2, S4 · §3 Non-goals, Edges · §5 perf · §6 AC1, AC2 · §7 New arm · §9 · §10 |
| 12 | 50, 51 | rev-3 | 19797 | §2 S6 · §6 AC2 · §8 F1 · §9 · §10 |
| 11 | 46, 47 | rev-3 | 25316 | §2 S7 · §3 Edges · §4 The legacy states · §5 perf · §6 AC3, AC4 · §8 F5 (new) · §9 · §10 |
| 7 | 32, 33 | rev-3 | 30124 | §2 S4, S6 · §3 Edges · §8 F9 (new) · §9 |
| 20 | 86, 88 | rev-3 | 24797 | §2 S1, S5 · §9 |

**Forks**
- **fo11 F5, new, open for the owner, recommendation (a).** The roles kit has no way to list the ledger's registrations without loading another kit's module. The ask the build run would file is on TOOL-dWitnessedBar-13: the memory-tree copy of `legacy_ledger.py` gets S10's command-line verbs plus a new `registrations --json`. The other options were a declared `requires_if` row naming `memory-tree`, or the roles kit reading the ledger tables itself (rejected as a second reader). Under (a), AC3's three ledger cases pass only once the verb lands.
- **fo7 F9, new, open for the owner, recommendation (a).** `backlog.py`'s only verb is `--selftest` (`tools/memory-tree/backlog.py:2306-2312`), so nothing exposes its row renderers to another kit. The ask is that `backlog.py` gains `render --json`, filed on whichever build owns that file at the pass (dTotalRecall today). The other options were a declared `requires_if` row, or TOOL-dTotalRecall-7's `gov_record.py new ask` (rejected: it writes the backlog file itself and renders no `SEV` or `KEEP` row). AC5 and AC6 wait on the verb.
- **fo12 F1, a probe fact-question.** I re-pinned the probe to `grep -c -F` on the Layer cell of TOOL-dBoundRoles-1's roster rows and re-ran it at `1a61f21a2`: 12 rows read `layer.roles` and 1 reads `layer.runtime`, so the answer is unchanged. Its 2026-10-26 resolved mark stays.
- No other fork was re-resolved or re-opened.

**Choices a reviewer should check**
- **Policy fallback with no policy kit (fo7, fo11, fo12, fo17).** Each key is now read through `read_policy_setting(..., with_default=True)`. The typed default is used only when no policy kit is found, with that read's note. I took this from the brief's rule and fo29 S9's current "a None reading the catalogue default", so I did not open a fork. The values kept are `repair-and-record`, `1024`/`handed`, `structural-roles`/`item-declared` and `every-role`/`16k`.
- **fo17 non-goal.** Besides the Edges bullet, I reworded the non-goal that called the `neighbourhood` reader TOOL-dTotalRecall-8's. It now names ask TOOL-dTotalRecall-103, since the same false claim stood there.
- **fo20 S1.** The namespace reader is now `read_gov_namespace <policy> <ns>…`, one fetch for all namespaces, each cached at `refs/gov/remote/<name>`. I added "`refs/gov/runs` alone where that section has not landed at the pass". Without that clause, F4's "stops the unit if a cited section is absent" would block fo20 on TOOL-dPlacedRequest-1 S4.

**Left for the main loop**
- Hygiene check 9 is a render owed by `gen_build_index.py --write`: `memory/LIVE.md`, `memory/builds/dFurnishedOrders/README.md` and `memory/builds/dLinkedLibrary/README.md` are stale.
- fo11's Edges bullet that mirrors fo29 still says "its ledger load, which unit 29 … S6 … settle(s)". It mirrors fo29 S6, which Group C is revising, so I left it for that writer to re-sync.

**Parent specs that look wrong (not edited)**
- TOOL-dWitnessedBar-13 S10 puts its command-line verbs on the canonical file only, and S8's memory-tree copy is a module copy. The spec never says whether an adopter's copy can be run as a command at all, which a cross-kit reader would need.
- TOOL-dTotalRecall-8 §3 (line 117) still gives the `code` slot and `memory.code-budget` to dBoundRoles, and its line 136 Edges bullet says "dBoundRoles' `code` slot reads it". Ask TOOL-dTotalRecall-102 is still open on this.

Files:
- C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\memory\builds\dFurnishedOrders\spec\2026-10-26-spec-TOOL-dFurnishedOrders-7.md
- C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\memory\builds\dFurnishedOrders\spec\2026-10-26-spec-TOOL-dFurnishedOrders-11.md
- C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\memory\builds\dFurnishedOrders\spec\2026-10-26-spec-TOOL-dFurnishedOrders-12.md
- C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\memory\builds\dFurnishedOrders\spec\2026-10-26-spec-TOOL-dFurnishedOrders-17.md
- C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\memory\builds\dFurnishedOrders\spec\2026-10-26-spec-TOOL-dFurnishedOrders-20.md

## Group B, the follow-up fo11 re-sync

Specs 11.

I changed one word in fo11's §3 Edges mirror bullet (line 97): "load" is now "read". Nothing else in the file changed.

First I re-read fo29 rev-4. Its S6 (fo29:81-89) says unit 11's ledger "is read by `legacy_ledger.py registrations --json` (unit 11 §8 F5)", and its own consumes-from bullet for unit 11 (fo29:199) calls it "ledger read".

**Before:**
```
- **hands-off** `TOOL-dFurnishedOrders-29` — the legacy slot's seed, its two key reads and its ledger load, which unit 29 S10, S9, S6, S8 and S24 settle (ids 30, 16, 29, 27, 26, 57)
```

**After:**
```
- **hands-off** `TOOL-dFurnishedOrders-29` — the legacy slot's seed, its two key reads and its ledger read, which unit 29 S10, S9, S6, S8 and S24 settle (ids 30, 16, 29, 27, 26, 57)
```

- **Byte count:** 25316, the same as before, because "load" and "read" are both four bytes. That is under the 49152 cap.
- **Status:** still `DEFERRED · rev-3 · 2026-10-28`, with no new §9 line.
- **Check:** `grep -c 'ledger load'` over the spec now prints 0.

The rest of my earlier return stands. The note I left about this bullet for Group C's writer is now closed.

File: C:\projects\coding-governance\.claude\worktrees\beautiful-lalande-23ce8b\memory\builds\dFurnishedOrders\spec\2026-10-26-spec-TOOL-dFurnishedOrders-11.md

## Group C, the roles kit's cross-kit loads and the `answered-calls` leg

Specs 3, 6, 10, 14, 29, 37 and 42.

I revised all seven Group C specs. Each is DEFERRED, dated 2026-10-28, under the 49,152-byte cap, and has one new §9 line naming the cross-check record and its rows. No row was refused: every record row was borne out by the parent's text. I edited nothing outside these seven files, and the real index is untouched. The scratch copy is deleted and `fo-wC/` is empty.

**Acceptance checks**
- **Quoted sentences:** a grep for each record row's quoted sentence prints nothing in its spec.
- **Hygiene gate:** `check-memory-hygiene.sh --staged`, over an index copy with only these seven specs staged, exits 1 on check 9 alone. That is the build-index render owed by `gen_build_index.py --write` (it lists fo10 as an index input, plus stale `memory/LIVE.md` and the dFurnishedOrders and dLinkedLibrary READMEs). That render belongs to the main loop.

| Spec | Rev | Bytes | Rows | Forks |
|---|---|---|---|---|
| fo3 | rev-3 | 20,908 | 11, 12 | F3 re-resolved |
| fo6 | rev-3 | 31,057 | 26, 27 | none touched |
| fo10 | rev-3 | 26,507 | 43 | F3 re-resolved |
| fo14 | rev-3 | 27,997 | 55 | F8 new, open |
| fo29 | rev-4 | 36,534 | 98, 99, 104, 105, 107 | F6 new, open |
| fo37 | rev-4 | 43,343 | 113, 114 | none touched |
| fo42 | rev-3 | 28,271 | 120 | F2 re-resolved |

**Per spec**
- **fo3** — Sections moved: S2, S4, §3 Edges, §4 (The value, Inventory, Alternatives rejected), §5, §8 F3, §10.
  - S2 reads `notices.record` by running `policy.py get notices.record --json` as a subprocess.
  - S4 mints a runlog verb, `runlog.py notices --transcript <path> --json`, which `handoff.py` runs by subprocess. Precedent: fo16 S2 mints `runlog.py turns` in this same build, so no ask is needed.
  - F3 is re-resolved to the recognizer staying in runlog, reached through that verb. Mark: RESOLVED (agent, 2026-10-28, delegated), rung 1, PLAY-dOrderedCharter-7 §4.
- **fo6** — Sections moved: S5, S9, §3 Edges, §4 (The decision, Inventory, Files touched), §5, new AC11, §10.
  - S5 spawns `node <policy kit>/policy-mirror.js get roles.answered-calls --repo <repo>` under the spec's existing 5-second bound, located by KICK-dKeptSession-8's `resolvePolicyHelper`. A failed spawn is a hook failure.
  - S9 declares the leg once with `leg_factory.py new --exempt` and renders the manifest with `--write`. Its `enforces` is `["principle.p29"]`: v2:1851's P29 row names cl-dClosedLoop-0197, which fo6 carries.
  - AC11 checks `leg_factory.py --check` and `--list`.
- **fo10** — Sections moved: S2, S4, S7, §3 Edges, §4 (Inventory, Files touched), AC3, AC8, §8 F3, §10.
  - S2 mints a second runlog verb, `runlog.py orientation --transcript <path> --json`.
  - S7 reads the matrix through `loop_items.py matrix --json`.
  - S4 is restated to match fo3's new S4.
  - F3 is re-resolved to option (b), the verb. Mark: RESOLVED (agent, 2026-10-28, delegated), rung 1, PLAY-dOrderedCharter-7 §4.
- **fo14** — Sections moved: S6, §3 Edges, §5, new §8 F8, §10.
  - S6 reads open asks from `gen_build_index.py --asks --json`, but its rows carry no `data` clause today (`gen_build_index.py:3346-3375`).
  - F8 is open for the owner, recommending (a). The ask: "`gen_build_index.py --asks --json` rows gain `data`".
- **fo29** — Sections moved: S6, S9, S11, S16, S19, §3 Edges, §4 (Inventory, Files touched), AC5, AC7, AC8, AC12, AC14, §7, new §8 F6, §10.
  - S6 no longer mints `load_kit_module`. It points to the fo3 and fo10 runlog verbs and to fo11's `legacy_ledger.py registrations --json` (fo11 F5).
  - S9 uses `with_default=True` and restates the end state as no `get` or policy import outside `read_policy_setting`. AC7 takes br43 AC21's predicate.
  - AC8's stub answers `declaration --item`, logs its verb, and counts only `seed` lines.
  - S19's guard sits on fo6's declaration and is rendered.
  - S16 and AC12 now follow fo2's rev-3 S5, as you asked: with no policy kit the read gives `per-task` plus the note, and an unset key gives `per-batch`.
  - F6 is open for the owner, recommending (a). The ask: "PLAY-dOrderedCharter-19: `gov_tag.py` gains `namespaces --json`".
- **fo37** — Sections moved: S2, S24, §3 Edges, §4 Files touched, AC2, AC13, §7.
  - S2's check also flags `spec_from_file_location`, `load_kit_module` and `import_module`, and lets a line pass only where a `requires_if` row admits it. I ran the predicate over the real tree: it prints nothing. `budgets` is left out of the list on purpose, because `roles_lib.py:150` keeps that import until fo42 removes it at order 25.
  - S24's guard sits on the declaration and is rendered.
- **fo42** — Sections moved: S7, §3 Edges, §4 (Inventory, Alternatives rejected), §5, AC4, §8 F2, §10.
  - The verb already exists: S7 runs `budgets.py resolve --explain <request>` (`tools/policy/budgets.py:4`, `:360-399`) through fo39's `run_bounded`. The `import budgets` and the `sys.path` insert are removed.
  - F2 is re-resolved to option (c), the verb. Mark: RESOLVED (agent, 2026-10-28, delegated), rung 1, TOOL-dBoundRoles-43 S21.

**For the main loop**
- **fo11 needs a re-sync.** Its line 97 mirror bullet still says "its ledger load"; fo29's side now says "ledger read".
- **Leg line:** fo29's §7 line gains `govkit selftest`, `govkit refusal join` and `govkit acceptance matrix`, which `tools/govkit/registry.toml` trips.
- **No `leg_factory.py` yet:** it is not in the tree. fo6 S9, fo29 S19 and fo37 S24 each say the pass records a hand edit if it is still unbuilt then.

**Parent specs that look wrong**
- **br43 contradicts ks8.** TOOL-dBoundRoles-43 S19 and AC19 (br43:101-104, :422-425) accept a "`readPolicy` import" line in `scratch-guard.js` and spawn-guard. KICK-dKeptSession-8 S5 (ks8:62-66) says a hook never `require`s the policy kit's module.
- **ks8 keeps an in-process require.** The same S5 leaves `agent-cap.js:469`'s `require` of `policy-mirror.js` in place, an in-process load of a sibling kit that TOOL-dGroundRules-1 §4 forbids.

Files revised (all under `C:/projects/coding-governance/.claude/worktrees/beautiful-lalande-23ce8b/memory/builds/dFurnishedOrders/spec/`):
- `2026-10-26-spec-TOOL-dFurnishedOrders-3.md`
- `2026-10-26-spec-TOOL-dFurnishedOrders-6.md`
- `2026-10-26-spec-TOOL-dFurnishedOrders-10.md`
- `2026-10-26-spec-TOOL-dFurnishedOrders-14.md`
- `2026-10-26-spec-TOOL-dFurnishedOrders-29.md`
- `2026-10-26-spec-TOOL-dFurnishedOrders-37.md`
- `2026-10-27-spec-TOOL-dFurnishedOrders-42.md`

## Group D, the `govkit selftest` leg and the tester template

Specs 15, 46, 48, 50 and 58.

All five Group D specs are revised. Every row was borne out by the parent text, so none is refused. The new fork F7 in spec 46 stays open for the owner, and no resolved fork needed re-resolving. I edited only these five spec files. Nothing is staged in the real index and nothing is committed.

| Spec | Rev now | Rows | Bytes |
|---|---|---|---|
| TOOL-dFurnishedOrders-15 | rev-3 | 60 | 23025 |
| TOOL-dFurnishedOrders-46 | rev-4 | 122, 123 | 35537 |
| TOOL-dFurnishedOrders-48 | rev-5 | 124 | 37471 |
| TOOL-dFurnishedOrders-50 | rev-3 | 126 | 23243 |
| TOOL-dFurnishedOrders-58 | rev-4 | 127 | 32278 |

Each Status line is dated 2026-10-28, still DEFERRED, and each spec has one new §9 line naming the sections moved, the cross-check record and its rows. Byte counts are of the working-tree files (CRLF), all under 49152.

**Spec 15** (row 60, checked against br2:324-338)
- **Sections moved:** §2 S3, §3 Edges, §4 "The role", "Rendered return" and Inventory, §6 AC5.
- **Change:** the template is now `outcome:code-miss|spec-wrong|answered|designed|judged, evidence:text, answer:text?, method:text?, losing:text?`, and the body returns `answered` for `test.reason`.
- **AC5:** it also checks that the rendered template line names `answered`, `designed` and `judged`.
- **Forks:** none added or re-resolved.

**Spec 46** (rows 122, 123)
- **Sections moved:** §2 S1, S5 and S8, §3 Edges, §4 Files touched and Alternatives rejected, §6 AC5 and AC8, §7 (the leg line and the roles arm), §8 F7.
- **S8:** the guard rows go on the `[[exempt_leg]]` row at `tools/govkit/registry.toml:439` and are rendered with `leg_factory.py --write`. Where the factory is not built, a hand edit stands in and the ledger records it. AC8 adds a `--check` clause for when the factory is built.
- **S5:** the check now runs through a lexicon verb by subprocess. I confirmed `lexicon.py` has no mode that takes a kit directory (`tools/lexicon/lexicon.py:4358-4360`).
- **F7, open for the owner, recommendation (a):** ask the lexicon kit for a `--self-containment <kit-dir>` mode. The other options were (b) a `requires_if` row, rejected because it would declare an edge that only a withheld file holds, and (c) keeping unit 42's copy of the walk, which brings back the copy finding (id 15).
- **AC5:** it now runs that verb. Until the verb lands, AC5 stays owed.
- **Side effect:** adding the registry to Files touched trips `govkit refusal join`'s `{prefix}/govkit/` guard, so §7 gains that leg.

**Spec 48** (row 124)
- **Sections moved:** §2 S3, S14, S17 and S18, §3 Edges, §4 "Why two units" (clause 1 and the write set) and Files touched, §6 AC6.
- **Change:** S14 declares the guard once, on the registry row, rendered by `--write`, with the hand-edit fallback recorded. S17 and S18 add their rows to that declaration. S16's arm still reads the rendered manifest. AC6 adds a `--check` clause.
- **Forks:** none.

**Spec 50** (row 126)
- **Sections moved:** §2 S1, §3 Edges, §4 Rollout and Files touched, §6 AC1.
- **Change:** the narrowing edits the registry row and renders it. The re-stamp still follows, because the rendered manifest is a watched path.
- **Forks:** none.

**Spec 58** (row 127)
- **Sections moved:** §2 S17 and S25, §3 Edges, §4 Rollout and Files touched, §6 AC19.
- **Change:** S17's row goes on the declaration and is rendered. S25 says the declaration, the render and the waiver rows land in one commit. AC19's `git log -S` over `tools/gate-legs.json` still holds, and it gains a check that the same commit touches the registry.
- **Forks:** none.

**Checks**
- **Brief greps:** the grep for each sentence the rows quote now prints nothing.
- **Hygiene gate:** `check-memory-hygiene.sh --staged` ran over an index copy with only these five specs staged. Its one failure is check 9: a render owed for `memory/LIVE.md`, `memory/builds/dFurnishedOrders/README.md` and `memory/builds/dLinkedLibrary/README.md`, which only `gen_build_index.py --write` cures. That is the main loop's. I deleted the index copy.
- **Not run:** the naming lexicon, because these revisions mint no new identifier. The new `--self-containment` flag is an ask, not minted here, and the `spec tokens` leg, which I'm not allowed to run, may flag it as unresolved.

**Parent specs that look wrong or unfinished** (not edited)
- TOOL-dWitnessedBar-11 S1 says each `[[exempt_leg]]` row carries the leg's whole row. Today the `govkit selftest` row holds only `name` and `why`, and `tools/run-gates/leg_factory.py` doesn't exist at `1a61f21a2`. Until wb11's Migration lands, every pass in this group will hand-edit the manifest.
- The `govkit selftest` manifest row has no `enforces` key, so PLAY-dOrderedCharter-7 S3 reds it unless it has a pending row. That is wb11 S6's to give it, not this group's.
- No open build visibly owns `tools/lexicon/`, so F7's ask has no named recipient yet. It reads "the build that owns `tools/lexicon/` at the pass".

The helper and edit scripts are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-beautiful-lalande-23ce8b/a46c346a-6f74-4403-a01d-0c3480a8d930/scratchpad/fo-wD/`.

Files:
- C:/projects/coding-governance/.claude/worktrees/beautiful-lalande-23ce8b/memory/builds/dFurnishedOrders/spec/2026-10-26-spec-TOOL-dFurnishedOrders-15.md
- C:/projects/coding-governance/.claude/worktrees/beautiful-lalande-23ce8b/memory/builds/dFurnishedOrders/spec/2026-10-27-spec-TOOL-dFurnishedOrders-46.md
- C:/projects/coding-governance/.claude/worktrees/beautiful-lalande-23ce8b/memory/builds/dFurnishedOrders/spec/2026-10-27-spec-TOOL-dFurnishedOrders-48.md
- C:/projects/coding-governance/.claude/worktrees/beautiful-lalande-23ce8b/memory/builds/dFurnishedOrders/spec/2026-10-27-spec-TOOL-dFurnishedOrders-50.md
- C:/projects/coding-governance/.claude/worktrees/beautiful-lalande-23ce8b/memory/builds/dFurnishedOrders/spec/2026-10-27-spec-TOOL-dFurnishedOrders-58.md
