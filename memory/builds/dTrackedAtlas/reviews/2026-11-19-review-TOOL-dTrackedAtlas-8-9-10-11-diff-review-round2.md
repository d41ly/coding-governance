**Serves:** diff-review TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-9 TOOL-dTrackedAtlas-10 TOOL-dTrackedAtlas-11

# dTrackedAtlas — Tier-2 diff review of the round-1 fold (TOOL-dTrackedAtlas-8..11), round 2

*2026-11-19. Subjects: the fold of round 1
(`memory/builds/dTrackedAtlas/reviews/2026-11-19-review-TOOL-dTrackedAtlas-1-2-3-4-diff-review-round1.md`),
whose findings became four units. Unit 8 (H1) puts no tree text into shell source in `scan_forks`. Unit 9 (H2)
measures landings on the default branch's first-parent line through `--default-ref`. Unit 10 (H3) widens the
page stamp's digest to cover the landings and the default ref. Unit 11 (M1, L1, L2) adds one reader for the
Atlas's valued options, clears ledger 1's stale line, and records the main loop's browser-pane observations in
ledgers 2 and 3. Build-folder instruments only; nothing under `tools/` changed. Five finder lenses ran, then
skeptic batches prompted to refute each finding, then this synthesis. Roles: finders gov-diff-reviewer, skeptic
batches gov-skeptic, synthesis gov-synthesizer. Intent came from 5 spec documents supplied as `specs`, beside
the range's commit messages. By design: the caller's byDesign.*

**Range reviewed: `5f2d3da6f8f440daee34140142b7bbdb56e19e3a...62fcd9a10d8bb6082bd87ed24993c0baecab04d0`**

**Round: 2.**

## Verdict: CLEAN WITH FIXES

No finding is a BLOCKER or a HIGH. Two MEDIUM items and three LOW items stand.

M1 (findings 1 and 5): `build_stamp` writes a `default_ref` that `read_stamp` refuses, so such a page can never
read current.

M2 (finding 2): the Atlas tells the operator to pass `--default-ref`, an option it silently ignores.

L1 (findings 4 and 7): the reds recorded for unit 2's AC12 and unit 3's AC8 name their page ambiguously, and
ledger 3's red is not the one spec 11 names.

L2 (finding 6): the pane observations were recorded in a new section, not as the precedent-form line spec 11
asks for beneath each "Owed to the close" line.

L3 (finding 3): a `--ref` guard in `check_page` is dead since unit 11's reader.

How the fold stands against round 1, as far as the confirmed findings speak to it. No confirmed finding says
that round 1's H1, H2 or H3 still stands. The default-ref input that unit 9 added and unit 10 stamped is the
surface of M1 and M2. Round 1's M1 is discharged in substance; L1 and L2 here are defects in how that
discharge was recorded. Round 1's L1 is folded; L3 here is the guard the fold left behind. No confirmed finding
touches round 1's L2.

No reviewer ran a gate. Every statement about behaviour comes from source or from the finders' and skeptics'
read-only probes.

## Review shape

Intensity full, raw 7, confirmed 7, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 5 items (0 blocker, 0 high, 2 medium, 3 low).
Adjudicated tally by raw confirmed finding: 7 (0 blocker, 0 high, 2 medium, 5 low).
Two synthesis merges account for the difference.
Findings 1 and 5 are one defect, the writer and reader of the stamp's `default_ref` holding two rules (M1).
Findings 4 and 7 are one defect, the pane reds recorded against a page other than the one named (L1).
Every finding keeps its binding grade. No grade was changed in synthesis.
Findings 4 and 6 were graded medium by their finders and low by their skeptics. The skeptics' grades bind.
No refuted finding was shown, so no twin is flagged.
The security lens returned and reported nothing. Its zero is evidence only within its checklist of 6 items.

## Run integrity

- Lenses: 5/5 returned, 0 died. Skeptic batches: 4/4 returned, 0 died.
- 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified,
  0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 6 judged sound, 0 judged UNSOUND, 1 judged INSTANCE-ONLY (finding 5), curing
  the cited instance and leaving its class standing, 0 none proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 2 re-graded by the skeptic (findings 4 and 6,
  medium to low).
- Unverified findings: 0 answered uncertain by a skeptic, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Checklist: 26 items, acquired by the harness from `--for-diff 5f2d3da6f..HEAD`, each assigned to exactly one
  of 5 lenses: security 6, correctness 5, seams 5, verification 5, intent 5.
- Refuted findings shown to synthesis: 0. Same-address pairs shown: 0.
- Dispositions: unclassed refuse; 26 class slugs handed; 198 leg names read from `tools/gate-legs.json`.

The run is complete: every count above that must be zero is zero.

## MEDIUM

### M1 — The stamp's writer accepts a `default_ref` its reader refuses (findings 1 and 5, medium)

**Where:** the reader's rule at
`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@09b2b8f6:900`; the writer's
refusals in `build_stamp` at `@09b2b8f6:862` (lines 860-864). The name comes from `resolve_default_ref` in
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py` (lines 246-265).

**What is wrong:** The rule for a stamp's `default_ref` exists in two copies that disagree. `build_stamp` only
requires a `str`. `read_stamp` requires `[A-Za-z0-9._][A-Za-z0-9._/-]*`, which has no `+` or `@`.
`resolve_default_ref` builds `refs/remotes/<remote>/<branch>`, the branch taken from `GOV_DEFAULT_BRANCH` or the
remote's HEAD, and it checks no characters. git accepts such names: `git check-ref-format
refs/remotes/origin/release+2` and `git check-ref-format refs/remotes/origin/feat@x` both exit 0. The write-side
refusals (no string `default_ref`, no 40-hex `default_commit`) have never been seen red: ledger 10's AC1-AC7
never pass `build_stamp` a state lacking either field, and AC5 tests the read side only. The base had no
`default_ref` field, so this diff introduced the disagreement.

**Consequence:** On a repository whose default branch is named, for example, `release+2`, `--out` writes a page
and exits 0. Every later `--check --page` prints `atlas: unstamped ... the stamp's default_ref field fails its
rule` and exits 1. Regenerating writes the same stamp again, so the page can never read current, and the reason
points away from the cause. The tool never certifies a page it should not; it refuses a valid one, and only for
unusual branch or remote names.

**Fix (finding 1's fix judged SOUND; finding 5's fix judged INSTANCE-ONLY, so the skeptic's class-level fix is
the fix):** Make one table of stamp field rules, `read_stamp`'s `rules` dict, the single source. Have
`build_stamp` check the whole stamp it is about to return against every rule in that table and raise
`StampError` naming the field, not just `default_ref`. Alternatively, widen the `default_ref` rule in that one
table to git's ref-format rules, for example by validating with `git check-ref-format`. Add probes that each
fail on the write side: a state without `default_commit`, a `default_ref` containing `+`, and a state whose
builds give empty landings. Live probe: in a scratch clone with `refs/remotes/origin/release+2` present, set
`GOV_DEFAULT_BRANCH=release+2`, run `--claims none --out p.html`, then `--check --page p.html`. Today it prints
`unstamped` with exit 1. After the fix it refuses at `--out`, or prints `current` with exit 0. The finder's
proposal for finding 5, one shared `default_ref` constant used by writer and reader, cures the cited instance
alone and leaves the other fields' two copies standing.

**Left-shift:** class `two-answers-to-one-question`. Gate: a self-test arm that, for every field in the stamp
rules table, builds a stamp whose field violates the rule and asserts `build_stamp` raises; and a round-trip
arm asserting that every stamp `build_stamp` returns passes `read_stamp`.

### M2 — The Atlas advises `--default-ref`, which it silently drops (finding 2, medium)

**Where:** `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@09b2b8f6:835`
(`read_landings`), `derive_actual`'s `sys.exit` at `@09b2b8f6:767`, and `main`/`read_options` at
`@09b2b8f6:971` (lines 971-1001). The message comes from `resolve_default_ref` in
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py` (lines 254, 256, 263).

**What is wrong:** `resolve_default_ref` raises `StateError` messages ending `pass --default-ref <rev>`. The
Atlas passes them on unchanged in two places: `derive_actual`'s `sys.exit(f"atlas: chain state: {e}")`, and
`check_page` through `read_landings`, `StampError` and `print_refusal`. The Atlas has no such option.
`VALUED_OPTIONS` is `('--page','--ref','--claims','--plant','--out')`, `derive_actual` calls
`build_state.derive` with no default ref, and `read_options` and `main` ignore any other argument without a word.
A read-only probe, `main(['--check','--page','nope.html','--default-ref','origin/main'])`, gave `read_options`
`({'--page': 'nope.html'}, None)` and ran on with the flag ignored. Both the refusal text and the
`read_landings` path are new in this diff (units 9 and 10).

**Consequence:** Whenever `refs/remotes/<remote>/<branch>` is missing (a clone with no remote, after a prune, or
in the AC6 fixture), both `atlas --out` and `--check --page` tell the operator to pass `--default-ref`. If the
operator does, the flag is dropped and the same refusal returns. No wrong result is certified; the remedy
printed is one the tool cannot accept.

**Fix (judged SOUND by the skeptic):** In `read_landings`, and in `derive_actual`'s `StateError` catch, rewrite
the trailing `pass --default-ref <rev>` into Atlas terms, such as "fetch the default branch, or run the
derivation with --default-ref". Alternatively, have `main` refuse any argument starting with `--` that is not in
`VALUED_OPTIONS` or `--check`, so an unknown flag is never silently dropped. Probe: run the Atlas with
`--default-ref` and confirm it exits 2 naming the flag.

**Left-shift:** new class `refusal-names-a-remedy-its-tool-cannot-take`. Gate: a self-test arm that runs the
Atlas with an unknown `--` option and asserts exit 2 naming it; and an arm that triggers each relayed
`StateError` through the Atlas and asserts every option the message names is one the Atlas accepts.

## LOW

### L1 — The pane reds name their page ambiguously, and ledger 3's is not the red spec 11 names (findings 4 and 7, low)

**Where:** `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-2-ledger.md@0cfc9d76:90` and
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-3-ledger.md@e522ed0e:85`, against spec 11
§4's table (`memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-11.md`, line 144) and ledger
3's own owed line at `@e522ed0e:75` (lines 75-76).

**What is wrong:** At its line `90`, the unit 2 ledger records the red on "the page the generator wrote at `9e21ac760`, the page home's
copy"; ledger 3:85 on "the page home's copy, written at `9e21ac760`". Those are different bytes at the
observation commit. The page blob is `ebf09934` at `9e21ac760`, `2f8839b8` at `d0743a938`, and `1df9858e` at
both `c8c089b07` and `0faa80088`; commits `5651f783b` (unit 2) and `cffbd91e0` (unit 3) rewrote the committed
copy in between. The `9e21ac760` blob has 0 matches for the green strings, the `c8c089b07` blob 5. Separately,
spec 11's table and ledger 3's owed line name ledger 3's red as "the page of the generator at `d0743a938`".
Ledger 3 used `9e21ac760`, an ancestor whose page lacks unit 2 as well as unit 3 (`git diff --stat 9e21ac760
d0743a938`: atlas.py 102 lines, atlas.html 115 lines), and records no deviation.

**Consequence:** Whoever re-runs either red as written, by opening the page home's copy, opens a template that
already holds unit 2's and unit 3's renderer, not the before-change page. These two observations are the only
evidence for units 2 and 3 reading CLOSED. Ledger 3's red does not isolate unit 3's stamp as the cause, and the
record departs from the criterion it says it discharges. The red's conclusion still holds: both ledgers name the
commit, so `git show 9e21ac760:<page>` recovers the bytes, and the green element is absent at both `9e21ac760`
and `d0743a938`. The defect is in the record, not a wrong result.

**Fix (both findings' fixes judged SOUND by their skeptics):** Restate each red with exact bytes: name the blob
opened (for example `git show 9e21ac760:<page> > <scratch>/red.html`, blob `ebf09934`) and stop calling it the
page home's copy. For ledger 3, repeat the red on a page written by the generator at `d0743a938`, as spec 11's
table and the owed line name it: confirm its `#derived` line has no `generated from` field and that
`--check --page` on it prints `atlas: unstamped` with exit 1, then cite `d0743a938` and the blob sha. If the
named red is not re-observed, record the deviation from it. Probe: serve the scratch copy of each named blob,
confirm it lacks the green element, and record the blob sha in the ledger line.

**Left-shift:** finding 4 takes new class `red-named-by-a-path-whose-bytes-moved`; finding 7 takes class
`staged-break-substitutes-a-synthetic-value`. Gate: a memory-hygiene check that reds a ledger "Red:" line naming
a committed path without a blob sha, and a spec-tokens style check that reds a ledger red whose commit differs
from the one its spec's acceptance table names unless the line carries a recorded deviation.

### L2 — The pane observations are not in the precedent form spec 11 asks for (finding 6, low)

**Where:** `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-2-ledger.md@0cfc9d76:78` and
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-3-ledger.md@e522ed0e:75` (lines 75-76);
spec 11 §4 "The pane observations at the close" (lines 146-149).

**What is wrong:** Spec 11 §4 says each ledger gains one line directly beneath its "Owed to the close" line, in
the precedent's form `Owed to the close, and since observed by the main loop in the browser pane: ...`
(aClearedLedger-3-1 line 7). Commit `0faa80088` left both owed lines unchanged, still owing AC12 and AC8, and
added a separate `## Observed at the close` section. A grep for `since observed by the main loop` matches
neither ledger.

**Consequence:** Each ledger holds an unqualified owed line for an item that is now observed. The observation sits
immediately beneath under a heading naming the criterion, and no tool, skill or guide greps for the precedent
form, so this is a record-form deviation from the spec with no behavioural effect, not round 1's M1 state.

**Fix (judged SOUND by the skeptic):** In ledgers 2 and 3, put the precedent-form line directly beneath, or in
place of, the owed line: `Owed to the close, and since observed by the main loop in the browser pane: AC12 ...`
(`AC8 ...` in ledger 3), pointing to the green and red already recorded. Probe: `grep -n 'since observed by the
main loop in the browser pane'` over both ledgers prints one line each; today it prints none.

**Left-shift:** class `amendment-leaves-its-other-half-standing`. Gate: a memory-hygiene check that reds a
ledger whose bare "Owed to the close" line names a criterion that a later section of the same ledger records as
observed, unless the owed line carries the precedent's "since observed" form.

### L3 — A `--ref` guard in `check_page` is dead since unit 11's reader (finding 3, low)

**Where:** `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@09b2b8f6:926`, against
`read_options` at `@09b2b8f6:984` (lines 976-990) and `check_page`'s only caller, `main` at `@09b2b8f6:1001`.

**What is wrong:** `check_page` still holds `if ref.startswith("-"): return print_refusal(f"--ref takes a
revision, not {ref}")`. `read_options` already refuses any `--ref` value starting with `-` as `--ref takes a
value`, and `main` refuses on that before it calls `check_page`. The rule now sits in two places with two texts.
At base `5f2d3da6f`, `main` computed the ref from position, so the guard could fire; unit 11's reader made it
dead.

**Consequence:** No behavioural effect. It misleads the next change, which could edit or rely on the dead
message: ledger 11:36 cites the "takes a revision" text, observed only from a scratch mutant of `read_options`.

**Fix (judged SOUND by the skeptic):** Remove the guard at line 926, or keep it and record in `check_page`'s
docstring that it is a library-caller backstop. Probe: grep for callers of `check_page` and confirm `main` is
the only one.

**Left-shift:** class `guard-above-a-fold-makes-its-fallback-dead`. Gate: a self-test arm that, for each refusal
text the Atlas defines, asserts some argv through `main` produces it, so a refusal no entry point can reach reds.

review-shape kind=diff-review round=2 intensity=full at=synth raw=7 confirmed=7 refuted=0 merged=0 unverified=0 blocker=0 high=0 medium=2 low=5 agents=10 out-tokens=65843 trigger=- shape=- efforts=- role-sha=-
review-round round=2 limit=- prior=4 count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | correctness | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@09b2b8f6:900 | medium | medium | confirmed | Confirmed by reading the code. build_stamp (atlas.py about line 861) checks only that default_ref is a str. read_stamp (about line 900) requires `[A-Za-z0-9._][A-Za-z0-9._/-]*`, which has no '+' or '@'. resolve_default_ref (memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py@eea3f911:246-264) builds the name refs/remotes/<remote>/<branch>. The branch comes from GOV_DEFAULT_BRANCH or from the observed remote HEAD (tools/lib/resolve_remote.py), and nothing checks its characters. I ran `git check-ref-format refs/remotes/origin/release+2`: it exits 0. So a page stamped on such a repo fails its own read_stamp, and every `--check --page` reports 'unstamped' with exit 1, forever. The base had no default_ref field (grep of 5f2d3da6f's atlas.py finds none), so this diff introduced it. Severity is medium: the effect is contained. The tool never certifies a page it should not, it only refuses a valid one, and only for unusual branch or remote names. | sound | - | class:two-answers-to-one-question |
| 2 | seams | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@09b2b8f6:835 | medium | medium | confirmed | Confirmed by reading the code. resolve_default_ref raises StateError messages that end 'pass --default-ref <rev>' (memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py@eea3f911:254, 256, 263). The Atlas passes them on unchanged in two places: derive_actual's `sys.exit(f"atlas: chain state: {e}")`, and check_page through read_landings -> StampError -> print_refusal. The Atlas cannot act on that advice. derive_actual calls build_state.derive(ref, root, claims, detail) with no default_ref. VALUED_OPTIONS is ('--page','--ref','--claims','--plant','--out'), and read_options and main ignore any other argument without a word, so '--default-ref x' is dropped and the same refusal returns. Both the refusal text and the read_landings path are new in this diff (unit 9 and unit 10). Severity is medium: the advice is wrong and the operator cannot follow it, but no wrong result is certified. | sound | - | new:refusal-names-a-remedy-its-tool-cannot-take |
| 3 | seams | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@09b2b8f6:926 | low | low | confirmed | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@09b2b8f6:926 still holds `if ref.startswith("-"): return print_refusal(f"--ref takes a revision, not {ref}")`. check_page has one caller, main at :1001, which passes values.get("--ref"). read_options (:976-990) has already returned `--ref takes a value` for any value that starts with '-', and main refuses on that reason before it calls check_page. So the guard cannot fire through main. The diff introduced this. At base 5f2d3da6f, main computed has_ref only from position, so `--ref --x` reached check_page and the guard fired. The rule now lives in two places with two different texts. Ledger 11:36 records the 'takes a revision, not --ref' text, but only from a scratch mutant of read_options. It has no effect on behaviour, so the grade is low. | sound | amendment-leaves-its-other-half-standing | class:guard-above-a-fold-makes-its-fallback-dead |
| 4 | verification | memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-2-ledger.md:90 | medium | low | confirmed | I re-ran the probe. The page blob is ebf09934 at 9e21ac760, 2f8839b8 at d0743a938, and 1df9858e at both c8c089b07 and 0faa80088. Commits 5651f783b and cffbd91e0 rewrote the committed copy between those points. The 9e21ac760 blob has 0 matches for the green strings, the c8c089b07 blob has 5. Ledger 2:90 says 'the page the generator wrote at 9e21ac760, the page home's copy', and ledger 3:85 says 'the page home's copy, written at 9e21ac760'. At the observation commit, the page home's copy is the post-change template, so the wording is misleading. Spec 11's table names ledger 3's red as 'the page of the generator at d0743a938'. That blob already has unit 2 ('Where each build stands' 3 times, 5651f783b is its ancestor) and no 'generated from'. Ledger 3 used 9e21ac760 instead and records no deviation. I grade it low, not medium. Both ledgers name the commit, so the bytes can be recovered with `git show 9e21ac760:<page>`. The green element ('generated from', or the Chain table and panel) is absent at both 9e21ac760 and d0743a938, so the red's conclusion holds either way. The defect is the record's wording and an unrecorded deviation from the spec, not a wrong result. | sound | - | new:red-named-by-a-path-whose-bytes-moved |
| 5 | verification | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@09b2b8f6:862 | low | low | confirmed | The diff added this code. At the base, read_stamp had no default_ref rule. build_stamp (memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@09b2b8f6:860-864) only requires default_ref to be a str, while read_stamp (line 900) requires `[A-Za-z0-9._][A-Za-z0-9._/-]*`. resolve_default_ref (memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py@eea3f911:246-265) returns either the --default-ref as passed or `refs/remotes/<remote>/<branch>`, and it only refuses names that start with '-' or that do not resolve. So a name git accepts but the reader's rule rejects (for example one with `+` or `@`) gets stamped, and main writes the page with exit 0. The next --check then reports it unstamped. Ledger 10's AC1-AC7 never call build_stamp with a state missing default_ref or default_commit; AC5 tests only the read side. So neither write-side refusal has been seen red. The effect is contained to unusual branch names, so low. | instance | - | class:two-answers-to-one-question |
| 6 | intent | memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-2-ledger.md:78 | medium | low | confirmed | Spec 11 §4 (lines 146-149) asks for one line directly beneath each 'Owed to the close' line, in the precedent form `Owed to the close, and since observed by the main loop in the browser pane: ...`. Commit 0faa80088 did something else. It left ledger 2 line 78 and ledger 3 lines 75-76 unchanged and added a separate '## Observed at the close — AC12/AC8 in the browser pane' section with the green and red observations. A grep for 'since observed by the main loop' matches neither ledger, so the spec deviation is real. The impact is overstated, though. The observation sits immediately beneath the owed line under a heading that names the criterion, and no tool, skill or guide greps for that form (I checked tools/, skills/, memory/guides). So this is not the round-1 M1 state of an owed item with no record. What remains is a record-form deviation from the spec with no behavioural effect: low. | sound | - | class:amendment-leaves-its-other-half-standing |
| 7 | intent | memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-3-ledger.md:85 | low | low | confirmed | Line 85 of ledger 3 was added in this range (0faa80088, +10 lines). It records the red on 'the page home's copy, written at 9e21ac760'. Spec 11's table at line 144 and ledger 3's own owed line (lines 75-76) both name 'the page of the generator at d0743a938'. `git merge-base --is-ancestor 9e21ac760 d0743a938` holds, and `git diff --stat` between the two shows atlas.py changed by 102 lines and atlas.html by 115 lines, so the page used lacks unit 2 as well as unit 3. The record therefore departs from the criterion it claims to discharge. As the finder says, the effect is contained: unit 2 adds no stamp, so the conclusion (no 'generated from' field, 'unstamped' with exit 1) would very likely be the same on the d0743a938 page. This is a record that does not match its spec, with no wrong behaviour shipped, so it is low. | sound | staged-break-substitutes-a-synthetic-value | class:staged-break-substitutes-a-synthetic-value |
