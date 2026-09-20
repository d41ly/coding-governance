**Serves:** spec-audit TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1

# Tier-2 spec audit — the aHoistedPass spec set

*Adversarial pre-code pass over all ten unit specs. Node `a`, 2026-09-05, ROUND 1. Findings below are
the set that survived a skeptic prompted to refute them; each carries the address, the fix, and the
gate that would have caught it before a human had to.*

**Reviewed subjects, pinned at blob:**

- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-1.md`@`c8da85eda0ebb7d0d1d1ca18e029c38cb83ec8db`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-2.md`@`c2efb7e14cc66b42e42573dc993cec7478c45b70`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-3.md`@`4f243260d1f750f4f31dc187325179b59197c70a`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-4.md`@`87e581c71d3e48859b92b27b93fca3a30a6e1089`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-5.md`@`d7fa4781d5477f4078057ee28b5c250bcd6c719a`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-6.md`@`d71a4ecadd1ecfc9ed73690cca14e5244a203c04`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-7.md`@`3774fdbecc5be4ed567fbd5e5ac58b5812c49571`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-8.md`@`54627d7fcebbc0cd06727741ef6fa5822ae7db87`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-9.md`@`040fc87664661dd879725cfe2eb3fcce3540ddad`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-DEPL-aHoistedPass-1.md`@`95b65cb76107c96fa3ee277d5247c76b0e8f1949`

All ten pins were re-hashed against the working tree at review time and match.

## Verdict: BLOCKED

One finding at BLOCKER severity and twelve at HIGH. The blocker is `TOOL-aHoistedPass-6`, whose
section 4 addresses `tools/workflows/unattended-build.js` throughout by `c4fcf5ad` line numbers that
no longer point at the code they name — a builder following section 4 literally deletes the AUDIT
stage and leaves BUILD standing, and its AC15 is an executable criterion that cannot pass however the
edit is made. That one is not a fix-while-building item: the spec has to be re-derived at BASE first.

The high band is dominated by two structural faults rather than twelve unrelated ones. Four units
(`DEPL-aHoistedPass-1`, `TOOL-aHoistedPass-2`, `TOOL-aHoistedPass-7`, `TOOL-aHoistedPass-9`) each
scope the same single `unattended` 1.17-to-1.18 bump, and two of them derive their owner-turn
classification from owning it — a classification that decides whether an unattended run may land the
unit at all. Separately, eight findings are one class: a scope item with no acceptance criterion, so
the work can be skipped with every leg green and no ledger line recording the skip.

## Run integrity

- Lenses: 4/4 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified; 0 spurious verdicts discarded; 0 duplicates removed.
- Unverified (no usable skeptic verdict): 0. There are no OUTSTANDING findings carried into this
  record.

Every lens and every skeptic batch returned. No zero reported below is a zero-by-absence: the finding
set is complete for the lenses run.

## Review shape

| Measure | Value |
|---|---|
| Raw findings | 50 |
| Confirmed | 24 |
| Refuted | 26 |
| Unverified | 0 |
| Precision (confirmed / (confirmed + refuted)) | 0.48 |
| Round | 1 |

Precision at 0.48 sits right on the charter's ~0.5 tighten-scope line (§8). The refutation rate is
consistent with a spec set that has already been swept twice — several rev-2 and rev-3 entries
pre-empted findings that lenses raised anyway.

Two pairs below are the same defect seen by two lenses, and the pipeline did not collapse them:
**id 3 and id 21** are both `TOOL-aHoistedPass-7`'s extraction-versus-consumption split, and **id 23
and id 35** are both `TOOL-aHoistedPass-1` section 4's stale `<the design record>` path. They are kept
as separate rows because each carries evidence the other does not, but they are 22 distinct defects,
not 24. Fixing either member of a pair closes both.

## Findings, severity-ranked

| # | Sev | Unit | Address | Defect |
|---|---|---|---|---|
| 31 | blocker | TOOL-aHoistedPass-6 | §2 S2, §4 | Every `unattended-build.js` line address is stale at BASE; S2's deletion spans now cover the AUDIT stage, and AC15 cannot pass |
| 22 | high | TOOL-aHoistedPass-4 | §6 AC8 vs AC9 | AC8 and AC9 cannot both pass; satisfying AC8 ships a half-bumped kit |
| 18 | high | TOOL-aHoistedPass-2 | §2 S11, §6 AC15 | Scopes two bumps §8 reassigned away, and AC15 asserts a `memory-tree` version that is already the BASE value |
| 19 | high | TOOL-aHoistedPass-7 | §2 S8, §4 | Scopes a bump spent five orders earlier, and derives OWNER-GATED status from owning it |
| 20 | high | TOOL-aHoistedPass-9 | §2 S7, §4, §6 AC11 | Same spent bump; owner-turn status derived from it, AC11 witnesses another unit's work |
| 2 | high | DEPL-aHoistedPass-1 | §6 AC10 vs §2 S8 | AC10 is true whether or not either bump it owns was performed |
| 21 | high | TOOL-aHoistedPass-7 | §2 S2/S3, §6 AC7 | AC7 grades an extraction §8 declares MOOT; names a symbol and file that will not carry it |
| 3 | high | TOOL-aHoistedPass-7 | §2 S2/S3 vs §8 F2 | Same split, other half: the landed helper is nested in `check-pass-order.sh` and is not callable |
| 17 | high | TOOL-aHoistedPass-1 | §3 non-goal 1 | TOOL-1 and TOOL-6 each disclaim the `unattended-build.js:34-37` correction and name the other as owner |
| 41 | high | TOOL-aHoistedPass-2 | §2 S6, §4 | Strikes a sentence ratified by `TOOL-dBriefedPass-3` with no superseding id; sibling narrows the same claim |
| 33 | high | TOOL-aHoistedPass-5 | §3, §4 Inventory | Nine `agent-cap.js` anchors stale after `TOOL-aWeldedTribunal-1`; S8 writes them into the shipped header |
| 4 | high | TOOL-aHoistedPass-2 | §2 S5 vs §6 | S5's first half — the false sentence at `UNATTENDED-PROTOCOL.md:635-637` — has no criterion |
| 1 | high | TOOL-aHoistedPass-3 | §8 F1 vs §2, §6 | The `memory-tree` 2.60→2.61 bump appears in no scope item and no criterion |
| 36 | medium | TOOL-aHoistedPass-8 | §4 Finding 2, AC3 | Stale `:118-124` span committed verbatim into a record whose product is reproducibility |
| 35 | medium | TOOL-aHoistedPass-1 | §4 Inventory | `<the design record>` bound to a path that does not exist; AC3 re-runs the derivation over it |
| 23 | medium | TOOL-aHoistedPass-1 | §4 Inventory | Same stale definitional path, second lens; residual-count row derives from it |
| 7 | medium | TOOL-aHoistedPass-5 | §2 S2 vs §6 | The eight-key args contract and its parse guard have no criterion |
| 5 | medium | TOOL-aHoistedPass-3 | §2 S9 vs §6 AC1 | Skipping the high-water row satisfies AC1; the leg then announces growth is unpriced, forever, at exit 0 |
| 9 | medium | TOOL-aHoistedPass-3 | §2 S2 vs §6 | Replacing the false "no gate enforces the pair" sentence has no criterion |
| 6 | medium | TOOL-aHoistedPass-6 | §6 AC2 vs §2 S3 | Absence-only grep: deleting the two surviving sites satisfies it as well as rewriting them |
| 24 | medium | DEPL-aHoistedPass-1 | §2 (missing S9) | Two backlog rows promised by §3 and §4 and booked in Files-touched have no scope item |
| 25 | medium | TOOL-aHoistedPass-6 | §2 (missing S13) | Same shape: `memory/backlog/TOOL.md` booked, no scope item, no criterion |
| 27 | medium | TOOL-aHoistedPass-1 | §7 second bullet | Gate rationale rests on "first to track the README", false at BASE; rev-2 fixed §8 only |
| 30 | low | TOOL-aHoistedPass-8 | §4 The population | Population paragraph contradicts AC7 on both the filename and the hit count |

## The three classes, and the gates that close them

Before the per-finding detail: 22 distinct defects fall into three classes, and three gates cover
nineteen of them. Building those three is a better use of the next hour than fixing twenty-two rows by
hand, because the rows come back on the next spec set and the gates do not.

**Class A — a scope item nothing grades.** Findings 1, 4, 5, 6, 7, 9, 24, 25 (and 2 as its
green-by-construction cousin). Nine of twenty-two. Each is an `S<n>` in section 2, or an obligation a
section-8 resolution assigns, that no `AC<n>` in section 6 observes. The acceptance ledger is keyed on
numbered criteria, so an obligation with no AC gets no ledger line — the work can be skipped with
every leg green and no record that it was skipped.

*Gate:* a memory-hygiene check that parses each spec's section 2 for `S<n>` tokens and its section 6
for `AC<n>` bodies, and reds on any `S<n>` no criterion mentions. Cheap, structural, and it fires on
this whole class at authoring time. It grades linkage, never adequacy — the header must say so, or a
structural check reads as a semantic one to everyone who did not write it (§7).

**Class B — a citation that outlived its base.** Findings 23, 30, 31, 33, 35, 36. Six of twenty-two,
including the blocker. Every one is a `path:line` or `path` address measured at `c4fcf5ad` and never
re-derived at BASE, in a spec whose whole value is that a reader can re-open what it cites.

*Gate:* a citation prober over `memory/builds/*/spec/*.md` — extract every `path:line`,
`path:a-b` and bare tracked-path citation, resolve it against the spec's declared `base`, and red when
the path does not exist there. Line-content matching is the stronger form and can follow; path
existence alone catches findings 23, 30 and 35 today. Pair it with an authoring rule the blocker
argues for directly: **cite by NAME, not by span** — a named target (`BUILD_SCHEMA`, `const unbuilt`,
`label: 'build:'`) survives the next shift and a line range does not.

**Class C — an amendment that left its other half standing.** Findings 3, 18, 19, 20, 21, 27, and 17
as its cross-spec form. Seven of twenty-two. A section-8 fork resolution or a section-9 rev entry
declares an item MOOT or reassigns it, and the section-2 scope item, the section-4 derivation and the
section-6 criterion that depended on it are all left as they were. `TOOL-aHoistedPass-4`'s rev-3 fixed
one instance of this class and introduced finding 22 doing it.

*Gate:* partly mechanical, partly a checklist entry. The mechanical half is the version-bump
collision: derive every `<kit> <a.b> -> <c.d>` claim across a build's spec set and red when two units
claim one move. That alone closes 18, 19, 20 and the ownership half of 2. The rest belongs in the §10
recurring-bug-class checklist as a named class with a named remedy — *when a rev entry moots an item,
grep the spec for every S, AC and Files-touched row naming it, in the same commit* — because "did the
amendment reach its other half" is a semantic question no parser answers.

## Detail

### 31 — blocker — TOOL-aHoistedPass-6 §2 S2 and §4 (Inventory, return block, install-prefix block, Files touched)

Section 4 addresses `tools/workflows/unattended-build.js` by `c4fcf5ad` line numbers throughout, and
every one except `:5`, `:9` and `:26-27` is wrong at BASE. The file grew from 531 to 835 lines, and
the spans S2 names for deletion now hold the AUDIT stage rather than the BUILD stage.

S2 says to delete `const built = await agent(` at `:485` through `:509` plus `BUILD_SCHEMA` at
`:210-219`. At BASE, `:485` is `const res = await agent(` — the audit-subjects agent — `:493` is its
options object, and `:210-219` is prompt prose and a comparator. The real BUILD agent is `:784`,
`BUILD_SCHEMA` is `:298`, `const unbuilt` is `:804`. A builder following section 4 literally deletes
the audit stage and leaves BUILD standing.

The rest of section 4 is off by the same drift. The four-site `--dispatch` table: `:56-57` is now
`:85`, `:462-463` is now `:675`, `:495-497` is now `:758`. `renderRoster` is `:226` not `:138`;
`allIds` is `:236` not `:148`; the `CONVERGING` return is `:646` not `:441-457`; the empty-`units`
refusal is `:184` not `:118-124`; `gotchas.py` is `:794` not `:499`; `DRIVER` is `:215` not `:127`.

The decisive one is AC15, which runs `sed -n '276,277p'` and asserts the nesting comment is there. At
BASE those two lines read `const SUBJECTS_SCHEMA = {` and `type: 'object',`; the nesting comment is at
`:467-468`. AC15 cannot pass however the edit is made, because S2's deletions all sit below `:467`.

rev-3's own sweep cited `:784` and `:84`, so the sweep knew the file had moved and left section 4
uncorrected. Section 10's reuse probe checks the corpus, never the citations. Unlike spec 7's rev-3,
spec 6's issued no blanket re-read instruction, so nothing supersedes section 4.

**Fix.** Re-derive every `unattended-build.js` address in section 4 at BASE, and restate S2 by NAME
rather than by span — the BUILD agent's `label: 'build:'`, `BUILD_SCHEMA`, `const unbuilt`. Replace
AC15's `sed -n '276,277p'` with a grep for the comment's own text. Re-check that the five
install-prefix occurrences are still five at their new sites before asserting the 5-to-6 rise.

**Left-shift.** Class B's citation prober, plus the cite-by-name rule. AC15 specifically argues for a
narrower gate worth having on its own: **an acceptance criterion may not name a bare line range.** An
AC is executable, so an AC anchored on `sed -n 'N,Mp'` is a criterion that rots between authoring and
landing, in the one place where rot is graded as failure.

### 22 — high — TOOL-aHoistedPass-4 §6 AC8 (against §4 Files-touched and AC9)

AC8 asserts that the only files changed under `tools/` are `tools/hooks/agent-cap.js` and
`tools/hooks/README.md`. Section 4's Files-touched table and AC9 both require
`tools/hooks/scratch-guard.js`'s `gov:kit agent-cap@` marker to move to 1.13 with the constant.

The two cannot both pass. `tools/hooks/scratch-guard.js:41` carries `gov:kit agent-cap@1.12`, and
`tools/check-kit-versions.sh:87` reds when any file carrying that marker disagrees with
`KIT_AGENT_CAP_VERSION`. S5 says so explicitly — "every tracked `gov:kit agent-cap@` carrier with
it... TWO files today". Satisfying AC8 leaves the second carrier at 1.12 and `check-kit-versions.sh`
exits non-zero, which is the failure mode AC9 itself names. Satisfying AC9 falsifies AC8. A run
verifying against AC8 ships a half-bumped kit. The rev-3 rewrite that fixed one instance of the
amendment class introduced this one.

**Fix.** Rewrite AC8 to name three files under `tools/` — `agent-cap.js`, `README.md`, and
`scratch-guard.js` (marker only) — matching section 4's table and AC9.

**Left-shift.** A criterion-consistency check: an AC asserting a closed file set must be reconciled
against the spec's own Files-touched table, and any path in the table absent from the set reds. This
is the cheapest gate in the report and it is purely structural.

### 18 — high — TOOL-aHoistedPass-2 §2 S11 and §6 AC15 (against §8's RESOLVED addendum)

S11 scopes both version bumps — `unattended` 1.17 to 1.18 and `memory-tree` 2.59 to 2.60 — and AC15
asserts all eight `unattended` carriers at 1.18 and all four `memory-tree` carriers at 2.60. Section
8's own RESOLVED addendum hands the `memory-tree` bump to `TOOL-aHoistedPass-3`, and
`DEPL-aHoistedPass-1`'s RESOLVED takes the `unattended` bump at order 2.

`TOOL-aHoistedPass-3`'s resolution then re-derived the `memory-tree` move as 2.60 to 2.61, because
`check-memory-hygiene.sh:20` already reads 2.60 at BASE. So AC15 asserts a version that is the BASE
value and that the order-2 unit will have moved past — the criterion is false at landing however
correctly this unit behaves. Section 4's Migration derivation and Files-touched table still book
eleven marker and render files this unit no longer owns.

**Fix.** Rewrite S11 to "assert `bash tools/check-kit-versions.sh` exit 0 against the versions
`DEPL-aHoistedPass-1` and `TOOL-aHoistedPass-3` set; move neither." Restate AC15 as an agreement
assertion with no literal version numbers. Cut the eight-carrier and five-render rows from section 4's
Files-touched table, keeping the `README.md` ungraded-marker observation as a note rather than an edit.

**Left-shift.** Class C's version-bump collision gate.

### 19 — high — TOOL-aHoistedPass-7 §2 S8 and §4 ("This unit is OWNER-GATED and the coupling is why")

S8 scopes "the kit version bump 1.17 -> 1.18" and section 4 derives the unit's OWNER-GATED status from
owning that bump, via `SKILL.template.md`'s marker. At `order 7` the move is spent:
`DEPL-aHoistedPass-1` takes it at order 2, and `TOOL-aHoistedPass-2` (S11) and `TOOL-aHoistedPass-9`
(S7) each still claim it too.

The Definition of Done therefore demands a move that no longer exists by the time this unit runs, so
the unit either re-bumps to a version nobody declared or reports a scope item it cannot perform. Worse:
the OWNER-GATED classification — the thing deciding whether an unattended run may land this unit
without an owner turn — rests on a coupling already spent, over an edit set (five template markers)
the unit would no longer touch. `TOOL-aHoistedPass-6` §3 applies the opposite reading to itself
("this unit lands inside that release"), which is the correction this spec never received.

**Fix.** Replace S8's bump with "assert `bash tools/check-kit-versions.sh` exit 0 at the version the
earlier order set, and add `check-brief-recorded.sh` as the fourth entry in
`check-kit-versions.sh:169`'s script list carrying that same version." Re-derive the OWNER-GATED line
in section 4 from whatever carrier this unit actually edits, rather than from the bump.

**Left-shift.** The version-bump collision gate, plus a narrower rule with teeth: **a spec's
OWNER-GATED or owner-turn classification must name the carrier it edits, and that carrier must appear
in its own Files-touched table.** A classification derived from an edit the unit does not make is the
one class of spec defect that changes whether an unattended run may land it at all.

### 20 — high — TOOL-aHoistedPass-9 §2 S7, §4 Rollout, §6 AC11

S7 is nothing but the `unattended` 1.17 to 1.18 bump across three engine constants and the marker in
all five tracked templates. Section 4's Rollout derives the unit's owner-turn status from it ("makes
this an owner turn transitively"), and AC11 asserts `KIT_UNATTENDED_VERSION=1.18`.

`DEPL-aHoistedPass-1`'s RESOLVED takes that single move at order 2. At `order 6` the whole scope item
is spent, the owner-turn derivation is hollow, and AC11 stays green only because someone else moved the
version — a criterion that no longer witnesses this unit's own work. Its rev-2 sweep resolved F1 and F2
only and never touched this collision.

**Fix.** Cut the bump from S7 and from section 4's Files-touched marker rows. Keep AC11 as a pure
agreement assertion. Re-derive the Rollout paragraph's owner-turn claim from the carriers this unit
actually edits — `check-unattended.sh` and its test file — or drop the claim.

**Left-shift.** Same two as finding 19.

### 2 — high — DEPL-aHoistedPass-1 §6 AC10 (against §2 S8)

AC10 asserts only that `check-kit-versions.sh` "exits 0 with `KIT_GOVKIT_VERSION` and every
`unattended` carrier agreeing". That is satisfied at 1.9/1.17 exactly as at 1.10/1.18. The spec's own
F1 says why: `check-kit-versions.sh` grades marker presence and marker/constant agreement, and "no
branch in it reads a diff".

Section 8's F1 resolution makes this the unit that performs the `unattended` 1.17 to 1.18 move for the
whole build, and `TOOL-aHoistedPass-2` stands down on the strength of it. S8 covers both bumps and no
other criterion in AC1-AC13 names a target number, so AC10 is green-by-construction for the work it
purports to cover: both units ship green with the kit still at 1.17 and govkit still at 1.9.

One qualifier on the impact, not the claim: `TOOL-aHoistedPass-2`'s AC15 does name 1.18 for the eight
`unattended` carriers, so that half could still be caught downstream. The `KIT_GOVKIT_VERSION` half is
named nowhere in the build.

**Fix.** Name the target values and a failing case, as the sibling specs do: kit-versions exits 0 with
`KIT_GOVKIT_VERSION` at its bumped value and all eight `unattended` carriers at 1.18, and exits
non-zero naming the carrier when one is staged back to 1.17.

**Left-shift.** A criterion-shape check: **an AC whose only observation is that a checker exits 0 must
also name a staged failing case.** This is §7's "a new gate is not landed until its failing case has
been observed", applied to acceptance criteria — and it is greppable, because an AC body with an
`exits 0` and no `exits non-zero` is a string match.

### 21 — high — TOOL-aHoistedPass-7 §2 S2/S3 and §6 AC7 (against §8's F2 RESOLVED)

S2 scopes moving the build-commit selection into `build_commit()` in
`tools/unattended/lib-unattended.sh`, S3 scopes repointing `check-pass-order.sh` at it, and AC7 asserts
the suite passes "after `build_commit` is extracted into `tools/unattended/lib-unattended.sh`" — while
section 8's F2 RESOLVED says the extraction already landed as `_find_build_commit` inside
`check-pass-order.sh` and that "this unit CONSUMES the landed helper rather than extracting it".

Measured at BASE `e828f778`: `_find_build_commit` is defined at `tools/unattended/check-pass-order.sh:337`
with call sites at `:378` and `:395`, and `tools/unattended/lib-unattended.sh` carries no such helper.
The extraction the spec scopes has not happened, yet §8 declares it MOOT. AC7's literal text names a
symbol and a file that the resolution says will not carry it, and no revision entry touched AC7. This
is the `amendment-leaves-its-other-half-standing` class `TOOL-aHoistedPass-4` rev-3 fixed for itself;
rev-3's "re-read against the shipped shape" instruction does not reconcile "consumes" with an AC that
grades "extracted".

**Fix.** Strike or strike-through S2 and S3 the way `TOOL-aHoistedPass-4` section 2 marks its landed
items. Rewrite AC7 to assert the sibling suite stays green with this leg CALLING the shipped
`_find_build_commit`. Remove `tools/unattended/lib-unattended.sh` from section 4's Files-touched list,
unless the consumption genuinely edits it.

**Left-shift.** Class C's checklist entry, plus Class A's coverage gate — with S2 and S3 struck, the
consumption path needs a criterion of its own or it inherits the same gap.

### 3 — high — TOOL-aHoistedPass-7 §2 S2/S3 (against §6 AC7 and §8 F2)

Same defect, second lens, and it adds the fact that makes the resolution unachievable rather than
merely inconsistent: the landed helper is defined **nested inside another block** at
`check-pass-order.sh:337` (the file's only other definition is `_report` at `:325`), so it is not
callable from the new sibling script at all. Section 8's stated route — consume the landed helper —
cannot be taken without the extraction section 8 says is not happening.

So sections 2 and 8 say opposite things, AC7's precondition will never occur, and no criterion in
AC1-AC11 observes the consumption path either. Whichever route the build takes, nothing grades it. The
"S2 and S3 are re-read against the shipped shape" clause names no outcome and settles nothing.

**Fix.** Rewrite S2 and S3 to what the unit now owes against the shipped shape and re-point AC7 at it.
Either the helper is lifted to `lib-unattended.sh` with the sibling suite green and its four liveness
counts byte-identical pre- and post-move, or the new leg's own selection is asserted to produce the
same build commit as `check-pass-order.sh` over the same fixture.

**Left-shift.** As finding 21. Worth adding to the §10 checklist as its own line: **a resolution that
says "consumes the landed X" must confirm X is reachable from the consumer** — nested-in-another-
function is the specific trap here, and it is invisible to a grep for the symbol name.

### 17 — high — TOOL-aHoistedPass-1 §3, non-goal 1

`TOOL-aHoistedPass-1` §3 lists `tools/workflows/unattended-build.js:34-37` among "The four live
carriers are not edited here" and routes it to "the design's U5". The design record's §7 table shows
U5 is "The parent and the driver", which is `TOOL-aHoistedPass-6`. `TOOL-aHoistedPass-6` §3 in turn
disclaims the same edit on the grounds that "`TOOL-aHoistedPass-1` at `order 1` owns that correction by
name". That sentence is false against TOOL-1's own text. The two specs disclaim to each other and no
unit scopes the edit.

The one carrier both specs agree is cheapest to fix therefore keeps quoting the superseded
`parallelism route: none` verdict after the whole build lands. Nothing on the bar grades a decision
row's truth — TOOL-1's own §4 says so — so the gap closes green, and the build's stated goal, the
record catching up with the verdicts that superseded it, is missed on the file both units had open.

**Fix.** Pick one owner in section 3. Either add the `unattended-build.js:34-37` correction to
`TOOL-aHoistedPass-6`'s section 2 — it already edits that file — and strike it from TOOL-1's S4 row; or
keep it out of both and make TOOL-1's S4 backlog row say explicitly that no unit of this build takes
it, so the residual is filed rather than assumed handled.

**Left-shift.** A cross-spec non-goal reconciler: collect every `path:line` a spec disclaims in its
section 3 together with the unit it routes to, and red when the named owner's section 2 does not scope
it. This is the same derivation as the version-bump collision gate, over a different field, and it
catches the mutual-disclaim shape that no single-spec check can see.

### 41 — high — TOOL-aHoistedPass-2 §2 S6 and §4 "The protocol corrections", correction two

S6 strikes `and the pass-order leg over the commit graph` from `UNATTENDED-PROTOCOL.md:642` as false.
`memory/DECISIONS.md:125` ratifies `TOOL-dBriefedPass-3` as exactly that claim: "pass ORDER is enforced
TWICE because one half is bypassable: `--dispatch` at the moment of the act, and a history leg over the
commit graph anchored on the build commit's FIRST PARENT". The protocol sentence is that record's own
sentence in its own section.

`check-pass-order.sh:12-16` says the leg exists precisely because `--dispatch` is bypassable and "Only
the commit graph remembers the ORDER" — so the exclusions the spec quotes at `:21-24` do not make the
clause false, they scope what it refuses. A grep for `dBriefedPass|supersed` over the spec returns
nothing, so no superseding id is cited, and AC8 forces the phrase to 0 in both halves.

Meanwhile sibling `TOOL-aHoistedPass-6` §4 handles the identical claim at `unattended-build.js:26-27`
by NARROWING it "to spec-before-code for CLOSED units" rather than deleting it. One build ships
strike-and-narrow on one fact: the protocol will say only `--dispatch` refuses while the harness header
says the history leg refuses spec-after-code. Whichever is read first is the one that misinforms.

**Fix.** Narrow rather than strike, matching `TOOL-aHoistedPass-6` S3's wording. Or, if the strike is
right, append a superseding row for `TOOL-dBriefedPass-3` in `TOOL-aHoistedPass-1`'s S1 commit and cite
it here.

**Left-shift.** A supersession check: **a spec that strikes text quoted in a ratified `DECISIONS.md`
row must cite a superseding id.** Mechanical enough to try — for each phrase an AC forces to 0, grep
`memory/DECISIONS.md` for it and red on a hit with no `supersed` citation in the same spec. Run the
candidate predicate over the tree first and print hits and near-misses (§7); this one will have
near-misses.

### 33 — high — TOOL-aHoistedPass-5 §3 and §4 Inventory

Section 3 asserts the fan-out hook is unchanged since `c4fcf5ad`. It is not:
`TOOL-aWeldedTribunal-1/2/3` plus four folds moved `tools/hooks/agent-cap.js` from 1610 to 1814 lines
between that base and BASE, widening the loop predicate. Every `agent-cap.js:<line>` in section 4's
nine-row inventory now points at unrelated code.

At BASE, `:403` (claimed: `guardAgentSpawn` claims a slot against `MAX_VERIFIERS`) is
`.filter(({ line }) => {`; `:1494-1499` (claimed: reached only on an `Agent` payload) is a
`path.dirname` walk; `:1509` (claimed: the `scriptPath` re-read) is `let names`; `:1519` (claimed: a
`name:` call reads nothing) is `fs.rmSync(...)`; `:1521` and `:1593` are a bare `}` and `)`; `:1541` is
the `MAX_VERIFIERS` slot loop; `:1562` is a TTL comparison. Only `:9` survives.

Section 4's whole value is the "what actually holds it" column, and every cell is anchored on a line
address. A reader cannot re-check any measured exit code, because the sites named do not exist. And the
exit codes were taken against the narrower pre-widening predicate, so the row asserting a plain loop
admits at exit 0 is now an unverified claim about a hook that has since learned two more loop spellings.
This lands in the product: S8 rewrites the shipped file's header "in the words section 4's inventory
settles on". Spec 5's rev-3 re-derived only "unattended-unit.js still does not exist" and issued no
re-read of the agent-cap citations.

**Fix.** Restate section 3 as "takes `agent-cap.js` as it stands at BASE, after
`TOOL-aWeldedTribunal-1`'s widening". Re-derive the nine anchors at BASE. Re-run the nine fixtures
against the shipped hook so the inventory's exit codes measure the predicate that will actually grade
the child.

**Left-shift.** Class B's citation prober. Add one rule beyond it: **a spec asserting a file is
unchanged since a base must name the command that proved it** — `git log --oneline <base>..BASE -- <path>`
is one line, and an empty result is the assertion. This finding is an unverified negative claim, which
is exactly the shape a liveness assertion exists to catch (§7).

### 4 — high — TOOL-aHoistedPass-2 §2 S5 (against §6 AC8-AC10, AC18)

S5's first half — rewriting `UNATTENDED-PROTOCOL.md:635-637`'s first two sentences, which the spec says
become false under the hoist — has no acceptance criterion. AC10 covers only S5's state-refusal list.

Walking AC1-AC18: AC8 grades correction two's strike; AC10 grades only the state-refusal sentence
(MISSING/THIN/no FORKED); AC9 grades byte identity of the two halves, which holds whether or not the
sentences were rewritten. Nothing observes correction one. The live carrier still reads at `:634-636`
"BUILD is unreachable except through both and on a TERMINAL --review verdict", and that sentence can
survive the landing untouched with every leg green — a false claim in a carrier the charter calls
binding, which is the exact defect this build exists to remove.

**Fix.** Add an AC in AC8's shape: grep the false clause (for example `unreachable except through
both`) returns 0 in both halves, and the replacement sentence names DISPOSAL as the third stage and
states that what the program holds is the roster hand-out rather than the build's reachability.

**Left-shift.** Class A's coverage gate.

### 1 — high — TOOL-aHoistedPass-3 §8 F1 RESOLVED (against §2 S1-S11 and §6 AC1-AC12)

The fork sweep assigns this unit the `memory-tree` 2.60 to 2.61 kit bump, and that work appears in no
section-2 scope item and in no section-6 criterion. §2 S1-S11 names no version bump, and §6 AC1-AC12
never invokes `check-kit-versions.sh`.

The bump is a payload obligation across the version constant, every tracked
`tools/memory-tree/*.template.md` marker, and its three renders. The spec's own §7 states that
`check-kit-versions.sh` grades only presence and agreement while `check-verdict-epoch.sh`'s scan set
excludes templates — so no leg has an opinion, and skipping the bump entirely leaves every leg green.
`TOOL-aHoistedPass-2` rev-2 then asserts kit-versions exit 0 without moving the version. Neither unit
notices the release shipped two different budget lines under one version. The sibling that would have
caught it does not: TOOL-2's AC15 names `memory-tree` carriers at 2.60, which is already the BASE
value, and its rev-2 §8 stands the unit down from moving it further. With no AC, there is no ledger
line either, so the skip leaves no record.

**Fix.** Add a scope item for the bump naming the derived carrier set, and an AC in the shape of
`TOOL-aHoistedPass-2`'s AC15 or `TOOL-aHoistedPass-9`'s AC11: kit-versions exits 0 with the constant
and every `memory-tree` marker reading 2.61, and exits non-zero with one carrier staged back to 2.60.

**Left-shift.** Class A's coverage gate, extended to obligations a section-8 resolution assigns — the
gate must read resolutions as scope, not only `S<n>` rows, or a fork sweep can create work no criterion
can reach.

### 36 — medium — TOOL-aHoistedPass-8 §4 (Finding 2, probe-table observation 3) and AC3

Finding 2 anchors the harness refusal at `unattended-build.js:118-124` with its message "at
`:120-122`". At BASE, `:118` is `return out`, `:120` is `function chunk(a, n) {`, and the
`unattended-build: args carries no` throw is at `:182-188` with its message at `:184-186`. The span was
correct at `c4fcf5ad`.

This unit's entire product is a record whose value is reproducibility, and AC9 forbids it from touching
any path under `tools/` — so the stale span is committed verbatim into the probe record as the thing a
later reader re-opens. AC3 asserts the throw is "the message at `:120-122`", which cannot be observed at
BASE. rev-3 re-derived `unattended.sh:469` and `UNATTENDED-PROTOCOL.md:637` and stopped, so the one
citation into the file that moved most is the one left unswept.

**Fix.** Drop the line span from Finding 2 and AC3 and assert on the message text the spec already
quotes (`unattended-build: args carries no`), which is what the shim actually exercised and which
cannot go stale. Record the BASE location once, in the probe record, marked as of BASE.

**Left-shift.** Class B's prober, and the cite-by-name rule from finding 31 — this finding is that rule
stated in its cheapest form, because the spec already quotes the message it should have asserted on.

### 35 — medium — TOOL-aHoistedPass-1 §4 Inventory (the `<the design record>` definition and the residual-bullet row)

Section 4 binds `<the design record>` to
`memory/builds/aHoistedPass/build/2026-09-04-build-aHoistedPass-1-design-pass.md`, a path that does not
exist. The record is `2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md`, which this spec's own
`gen:spec-records` table already names correctly at line 9.

The definition is the operand of a derivation the spec runs twice: the 28-residual count and its 21/7
split in the Inventory table, and AC3 at landing, which re-runs
`awk '/^## §10/…' <the design record> | grep -c '^- '` to prove every residual got a row with no gap and
no repeat. With the operand naming a missing file the awk emits nothing, `grep -c` prints 0, and AC3
compares a real backlog count against 0 — failing for a reason unrelated to the work, or passing
vacuously if the run silently substitutes the right path without recording that it did. S3's ordinal
`<k>` has no defined range until this is settled. `TOOL-aHoistedPass-8`'s rev-2 caught precisely this
class for itself; specs 1 and 5 were never swept for it.

**Fix.** Replace the path in section 4's Inventory paragraph with the one in the `gen:spec-records`
table, then re-derive the 28/21/7 split from that file at BASE before S3 files a single row.

**Left-shift.** Class B's prober catches this one on path existence alone, no line matching needed. A
second, better rule for this specific shape: **define a record token once, by pointing at the
`gen:spec-records` row, never by retyping the filename** — the generated table cannot go stale and a
hand-typed second copy can, which is the charter's derive-over-author rule applied to a spec.

### 23 — medium — TOOL-aHoistedPass-1 §4 Inventory (same definition, residual-count row)

The same stale `<the design record>` binding, reported by a second lens against the residual-count row
rather than the residual-bullet row. Recorded separately because its verification adds a fact worth
keeping: the path never existed in history — the record was added under its real name in `fa273fc7`.

Severity is capped at medium on evidence, not on charity. Running the `awk`/`grep` against the real
record returns exactly 28, and the spec's own `gen:spec-records` table names the correct path one line
away, so the figure is reproducible and a builder resolves it without help. The defect is a wrong
definitional path, not an unreproducible count.

**Fix.** As finding 35 — the two close together.

**Left-shift.** As finding 35.

### 7 — medium — TOOL-aHoistedPass-5 §2 S2 (against §6 AC1-AC13)

The args contract — eight keys refused by name with a reason, behind a `JSON.parse` guard for a string
payload — has no acceptance criterion. AC11 observes only the absence of `roster` and `reportPath` and
the schema's required keys.

S2 is one of the two things this file is, and section 4 gives each key its own justification for not
being defaulted — `repo` defaulting to cwd is named as how a sibling harness reviewed the wrong
repository. A child shipped with `repo` defaulted, or with the parse guard missing, passes every
criterion in section 6, and the failure then surfaces as a wrong-tree build rather than as a refusal at
the boundary.

**Fix.** Add an AC that invokes the landed script with each of the eight keys omitted in turn and
asserts a refusal naming that key, and one that hands `args` as a JSON string and asserts the parse path
is taken rather than every key reading `undefined`.

**Left-shift.** Class A's coverage gate. This one also argues for a rule the charter already holds
elsewhere (§9, sanitize at the write boundary): **an input contract is a trust boundary, and a trust
boundary gets a per-key refusal test, not a schema assertion.** Worth a §10 checklist line.

### 5 — medium — TOOL-aHoistedPass-3 §2 S9 (against §6 AC1)

Seeding the high-water row is a scope item with no criterion, and AC1's wording — "exits 0 and prints
one template-size OK line" — does not exclude the no-ratchet line the missing row produces at exit 0.

Section 4 declaration 6 states that without the row the leg prints
`TEMPLATE-SIZE no-ratchet ... growth is unpriced` on every bar at exit 0, confirmed at
`tools/check-template-size.sh:178`, and the OK line still prints after it. AC1 asks only for exit 0 and
one template-size OK line naming the bytes against 27648, which the no-row state satisfies exactly;
AC12's green bar tolerates it too. S9 is the one declaration of §4's six with no observation, and
skipping it leaves the new leg permanently announcing that the growth it was built to price is unpriced,
with nothing failing.

**Fix.** Add an AC asserting `tools/template-size-highwater.txt` carries a row keyed on
`memory/guides/BUILD-METHOD.md` after `--bump`, and that the leg's output on the landing tree contains
no line matching `no-ratchet`.

**Left-shift.** Class A's coverage gate. Also a candidate for a real bar leg, independent of this
build: **`check-template-size.sh` reds on any `no-ratchet` line rather than printing one at exit 0.** A
checker that announces its own blindness and then exits 0 is the reassuring-zero shape §7 names, and it
is one line to fix in the checker.

### 9 — medium — TOOL-aHoistedPass-3 §2 S2 (against §6 AC1-AC12)

Replacing the now-false sentence at `BUILD-METHOD.template.md:16-18` — "No gate enforces the pair ...
nobody has ruled" — has no acceptance criterion. AC10's dogfood-parity run compares template to render
for byte identity modulo substitution, which holds equally well over the unrevised sentence, and the new
pair term reads only the `**Budget:` line, not this paragraph.

Skipping S2 lands the leg while the document keeps telling every reader that nothing enforces its
budget — a false claim in the exact file whose false claim this unit was written to remove, and one that
would license the next author to exceed the pair silently.

**Fix.** Add an AC greping `No gate enforces the pair` to 0 in both the template and the render, and
asserting the replacement names the build-method size leg and states that the line axis stays ungated.

**Left-shift.** Class A's coverage gate.

### 6 — medium — TOOL-aHoistedPass-6 §6 AC2 (against §2 S3)

AC2 is an absence-only grep returning 0 over four phrases, so deleting the two surviving sites at
`:26-27` and `:56-57` satisfies it exactly as well as rewriting them does.

S3 exists because two of the four assertions do not leave with the BUILD agent, and section 4's table
marks `:26-27` and `:56-57` as NOT removed by S2, specifying positive replacements: `:26-27` restated
with the order clause marked conditional and the pass-order clause narrowed to spec-before-code, and
`:56-57` rewritten around DISPOSAL. None of that content is observed. AC15 covers S6's nesting comment
and AC16 covers meta; no criterion reads the replacement text. So the unit can pass its own acceptance
while the file's WHY block simply falls silent about what `--dispatch` refuses — the state the run then
has no carrier for.

**Fix.** Add a positive assertion beside AC2: the rewritten `:26-27` names the two spec-state refusals
and marks the order clause conditional on both units carrying an order verb, and `:56-57` names DISPOSAL
as the stage the one-agent-per-stage shape still applies to.

**Left-shift.** A criterion-shape check, the sibling of finding 2's: **a scope item specifying
replacement TEXT may not be graded solely by an absence assertion.** Greppable — an `S<n>` whose section
4 entry says "rewritten" or "restated", matched to an AC body containing only a `grep ... 0`, is a
string match. This is green-by-absence, which the charter names explicitly and which this build's own
siblings call out.

### 24 — medium — DEPL-aHoistedPass-1 §2 (no scope item for the backlog rows §3 and §4 both promise)

Section 3 defers the mis-spelled `require` key class with "Backlog row." Section 4 defers the stale
`BRANCH_PIN`/`FILE_PIN` re-baseline "as a backlog row rather than smuggled in here". Section 4's
Files-touched table books `memory/backlog/DEPL.md` for "the mis-spelled-key row and the stale-pin row",
and §7 lists memory hygiene as gating "this spec and the backlog rows". S1 through S8 contain no item
filing either row, and AC1-AC13 assert none.

Two deferrals the design leans on to justify narrowing scope therefore have no scope item and no
acceptance witness, so a run that lands S1-S8 green closes the unit with both residuals unrecorded — the
stale-pin one being the argument AC9 leans on to accept `BRANCH_PIN` at 217 against a live 244. The
build's own sibling (`TOOL-aHoistedPass-1` S3) shows the convention is an explicit scope item for
backlog filing, so this is an omission rather than an implied record.

**Fix.** Add an S9 filing both rows in `memory/backlog/DEPL.md` with their reasons, and an AC asserting
`git grep -c` finds each row, so the section 4 file-set and the scope agree.

**Left-shift.** A Files-touched reconciler: **every path in a spec's section 4 Files-touched table is
named by at least one section 2 scope item.** Purely structural, closes findings 24 and 25 together, and
it is the mirror of finding 22's gate — one reads the table against the ACs, the other against the scope.

### 25 — medium — TOOL-aHoistedPass-6 §2 (no scope item for the backlog rows §4 promises)

Section 4 books `memory/backlog/TOOL.md` in Files-touched for "rows for the residuals in §5", and
separately says of the ungraded `gov:kit unattended-build@1.0` marker "It is not moved here and a
backlog row records it." S1 through S12 file no backlog row and none of AC1-AC23 mentions one.

The unit's edit set therefore includes a file its scope never authorises, and the two residuals the
design explicitly refuses to fix in place have no durable home — so they vanish with the build folder,
which `TOOL-aHoistedPass-1` §4 identifies as exactly the failure mode residuals must avoid.

**Fix.** Add an S13 naming the backlog rows this unit files — the section 5 residuals and the ungraded
`unattended-build@` marker — and one AC asserting each row exists. Or remove `memory/backlog/TOOL.md`
from section 4's Files-touched table.

**Left-shift.** The Files-touched reconciler from finding 24.

### 27 — medium — TOOL-aHoistedPass-1 §7, second bullet (build README slot contract)

Section 7 says "this unit's commit is the first to track `memory/builds/aHoistedPass/README.md`, which
is the fork in §8". `git ls-tree` at BASE `e828f778` lists that README as tracked, and section 8's own
RESOLVED note records that the readme-contract row already exists at BASE. rev-2's F1-is-MOOT resolution
corrected §8 without touching §7 — the amendment class again.

Half of the reported finding is refuted and worth recording as such: section 4's rejected alternative
("The build folder is UNTRACKED at this base") is explicitly base-qualified to `c4fcf5ad`, where it was
true, and it prints the command a reader re-runs. That half stands. The consequence is also narrower
than first claimed: §7 states the leg is chunk `records`, subject `repo`, no guard, so the
`--check-format` obligation is unambiguous regardless of the stale rationale. What remains is a reader
who cannot tell whether the stated rationale still applies at the version being built.

**Fix.** Amend section 7's bullet to say the README is already tracked and contract-BOUND at BASE, so
the leg simply stays green. Add a rev note to the section 4 alternative marking its "UNTRACKED at this
base" clause as true only at `c4fcf5ad`.

**Left-shift.** Class C's checklist entry. The generalisable rule this finding supplies is narrower and
cheap: **a claim about tracked-ness or first-tracking carries the base it was measured at**, the same
way section 4's rejected alternative already does. The half that was written correctly is the model for
the half that was not.

### 30 — low — TOOL-aHoistedPass-8 §4 "The population"

Section 4 states the only `authorized-by: recipe` hit is
`memory/builds/aHoistedPass/build/2026-09-04-build-aHoistedPass-1-design-pass.md`, a name that has never
been tracked — the real record is `2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md`, added in
`fa273fc7`. Section 9's rev-2 entry states plainly that the pattern has TWO hits on the landing tree,
ZERO at `c4fcf5ad`, and that "the design record has since been renamed, so rev-1's path is stale as well
as mis-based" — then corrects AC7 alone and leaves the section 4 paragraph carrying the stale path and
the superseded one-hit count.

So the measurement paragraph and the revision log disagree about both the filename and the hit count,
and a later reader quoting section 4 contradicts AC7, the criterion that grades the same population.
Low severity because AC7 is correct and is what actually grades; the cost is a misleading paragraph, not
a wrong verdict.

**Fix.** Update section 4's population sentence to the tracked path and to the two-hit landing-tree
count AC7 asserts, keeping the `c4fcf5ad` zero-hit result labelled as the control.

**Left-shift.** Class C's checklist entry — a rev entry that corrects a measurement must sweep the
paragraph that reported it, not only the criterion that grades it.

## What this round did not cover

Stated so a later reader does not misread the finding count as coverage:

- **Adequacy, not just linkage.** Class A findings say a scope item has no criterion. Where a criterion
  does exist, this round did not systematically ask whether it is strong enough — findings 2 and 6
  caught two weak ones, but that was lens luck rather than a sweep.
- **Whether the specified work is the right work.** This is a pre-code audit of internal consistency,
  citation accuracy and acceptance coverage. It does not second-guess the design's verdicts.
- **`TOOL-aHoistedPass-6`'s section 4 beyond the addresses.** Finding 31 blocks that section on its line
  numbers; once re-derived at BASE, the section's substance needs a fresh pass, because a corrected
  address set may change what S2 actually deletes.
- **Round 2 is owed.** Thirteen findings at blocker or high touch scope items, acceptance criteria and
  owner-turn classifications, and several fixes are cross-spec. The re-spun set should be re-audited
  before code, not after.
