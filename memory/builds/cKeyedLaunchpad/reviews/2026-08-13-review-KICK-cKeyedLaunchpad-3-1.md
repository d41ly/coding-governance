**Serves:** spec-audit KICK-cKeyedLaunchpad-3 KICK-cKeyedLaunchpad-6

## Verdict: BLOCKED

**Target:** the full seven-spec set under `memory/builds/cKeyedLaunchpad/spec/`, all rev-1, all
authored this run, at BASE `f006691` on `branch/session-kickoff-skill-review-0c76ec`. No code exists.
This is the M4 spec audit the build README names as the next action, and the hard floor
`BUILD-METHOD.md` M2 puts before any code.

**Scope.** Every `## 2` through `## 10` of all seven specs, plus the README's finding table, owner
decisions and dependency order, plus M2's four cross-spec axes (scope, interface, ordering,
acceptance). Owner decisions recorded in the README were treated as settled and were attacked only
where a spec contradicts one or mis-states its consequence. Style, tone and length were out.

**Method.** Four lenses, run independently over the whole set:

1. **Underspecification** — a map, built item by item, of every `§2` scope item to the `§6` criterion
   that would prove it done, and of every `§6` criterion to the observation (command, file content,
   gate verdict) that would decide it.
2. **Contradiction** — each spec against itself and against its siblings on M2's four axes.
3. **Unstated assumption** — what each `§4` design requires of code that exists at BASE, verified
   against source and, where the claim was about git behaviour, against a scratch repository.
4. **Prior art** — the recall probe the README prescribes, `memory/DECISIONS.md`, the backlog shards,
   `memory/gotchas/`, and `memory/builds/aRatchetForge/` (the spec that designed the ratchet three of
   these units extend).

Every candidate then went to a batched adversarial skeptic whose default was refutation and whose
verdict had to reproduce against the spec text, the tree, or a live command. Verifier fan-out stayed
inside `memory/guides/REVIEW-PROTOCOL.md`'s at-most-5-total and at-most-5-concurrent budget.

**Shape:** raw 36, confirmed 24, refuted 12, unverified 0. **Precision 0.67.** The 24 confirmed
carry duplicates across lenses — three findings were reached independently by two lenses each — and
dedupe to **18 distinct defects**.

**Severity split:** 1 blocker, 11 high, 6 medium, 0 low. By unit: spec-1 one, spec-2 four, spec-3
five, spec-4 two, spec-5 two, spec-6 three, spec-7 four (four of these are shared, counted in both
units they bind).

**Verdict rationale.** BLOCKED, on two findings. **B1** makes `KICK-cKeyedLaunchpad-3`'s C9
unbuildable as specced: the rename guard its `§4` designs cannot fire on the rename this build itself
performs, and the AC written to prove the guard works is unsatisfiable by that mechanism. **H10**
makes `KICK-cKeyedLaunchpad-6`'s AC1 and AC7 unsatisfiable together inside its own scope, by
measurement. Both need a design decision, not a wording fix. The remaining sixteen fold into spec
edits.

---

## Confirmed findings

### B1 (blocker) — C9's rename guard cannot fire on the rename this build performs

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-3.md` `§4` Design, the subsection "C9, and the three
things C5 does not have to worry about", item 1 — and `§6` AC9.

`§4` mandates a path-scoped walk and then classifies its output: "`R` is skipped, `A` is the
manifest's birth and terminates the walk as a body change." A path-scoped `git log --name-status --
<manifest>` does not report a `git mv` as `R`. Reproduced in a scratch repository (create, edit,
`git mv`, edit; git 2.55): `git log --name-status -- new.md` prints `A new.md` at the move commit,
identically with `-M`; `git rev-list --count HEAD -- new.md` is 2, i.e. pre-rename history is
unreachable; only `git log --follow --name-status -- new.md` prints `R100 old.md new.md` and reaches
it. The word `--follow` appears nowhere in the spec.

So the `R` branch is dead code, and `KICK-cKeyedLaunchpad-2`'s `git mv` — which `§4` itself names as
the reason the guard is "not hypothetical for this build" — is classified as a birth and reports the
manifest as freshly maintained. That is precisely the false-fresh outcome `§4`'s own "Alternatives
rejected" bullet refuses the empty-parent inference for; the chosen alternative reaches it by another
route. AC9 ("When the manifest was renamed since its last body change, C9 does NOT report it as
freshly maintained. This is the arm that fails without the `--name-status` guard") cannot be
satisfied by the mechanism `§4` describes: a fixture built as specced emits `A`, so the arm either
mis-asserts or gets hacked around.

**Fix.** Pick a mechanism that survives path scoping and state it:

- run the body walk as `git log --follow --name-status -- <manifest>` (legal here — the manifest is a
  single pathspec, which is `--follow`'s requirement; the watch-pathspec commit count is a separate,
  multi-path walk and needs no change), treat `R` as a skip that CONTINUES into pre-rename history,
  and re-state what `A` means once `--follow` is in play, or
- drop the rename inference entirely and anchor the walk to a recorded baseline the manifest itself
  carries.

Then rewrite AC9's fixture to perform a real `git mv` and assert the walk still reaches the
pre-rename body change — not merely that the check "does not report freshly maintained", which an
unrelated bug also satisfies. Whichever is chosen, `§4` must record the observed git behaviour, since
the whole design turns on it.

### H1 — C9's three-month branch has neither a design nor a criterion

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-3.md` `§2` S3 and `§4`; `§6` AC7-AC11.

S3 defines C9 with two disjunctive thresholds — ten or more non-merge watch-pathspec commits, **or**
three months, whichever comes first. The word "month" appears exactly once in the file, in S3. `§4`
designs only the commit walk (body compare with `last-audit` stripped, the rename guard, the
50-candidate cap, the shallow-clone skip) and never names a timestamp source: author date or
committer date, of which commit. `§5`'s error-state row and all five C9 criteria exercise the commit
branch only. The upstream authority does not fill the gap — `aRatchetForge`'s `§10.9` says only
"≥10 watch-pathspec commits or ≥3 months with zero body growth".

Half of a new hard-red check therefore ships with no design and no acceptance criterion, and it is
the half that fires on an idle repository — the case the commit branch structurally cannot reach.

**Fix.** In `§4`, name the timestamp (committer date of the last body-change commit, compared against
now) and the comparison. Add an AC that ages a fixture (`GIT_COMMITTER_DATE` in the scratch repo) and
asserts C9 reds on elapsed time with fewer than ten commits. If the branch is instead to be dropped,
that reverses owner decision 2 and belongs in `§8` with the owner's mark, not in silence.

### H2 — the staged/non-staged placement contract is unobserved

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-3.md` `§2` S4 and `§6`.

S4 is an explicit two-part placement contract: C7 and C8 run in BOTH legs; C9 sits inside the
existing non-staged branch and never runs in the staged leg. No criterion in `§6` invokes
`manifest-check.sh --staged` at all. The split is a real code path — `manifest-check.sh:155` is
`if [ "$STAGED" = 0 ]` and the header at line 13 enumerates the staged leg as "C1 C2 C4 C6 + C5s" —
and the existing self-test's staged scenarios assert C5s text only, so C7/C8 landing solely in the
non-staged branch, or C9 leaking into the staged one, changes no asserted output. `§4`'s entire
performance argument rests on this split: the pre-commit hook runs the staged leg unconditionally,
and C9 measures 2.4 s. The untested failure is a 2.4 s tax on every commit in every adopting repo,
discovered by feel.

**Fix.** Add two criteria: `--staged` reds an oversize or long-line staged manifest (C7/C8 present),
and `--staged` over a stalled manifest exits 0 with no C9 line (C9 absent). Assert the staged
header's check enumeration as a string, so the arm has something exact to compare.

### H3 — nothing states what clears a C9 red

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-3.md` `§4` (or `§5` observability) and `§8`.

`§4` compares bodies with `last-audit` stripped, so the audit re-stamp — the only maintenance action
Step 2b performs when the manifest is found accurate — cannot clear a C9 red. The sole exit is
cosmetic body churn. No section, criterion or risks row says so, and `§8` declares the forks
resolved. A stable, accurate manifest then reds the full leg roughly quarterly forever, with a
remedy nobody wrote — in a check whose own upstream calls false-red rate "the adoption killer".

Note the settled part: the semantics (zero body growth means stall) are the owner-adopted threshold
and are not re-litigated here. What is missing is the clearing rule.

**Fix.** State the remedy the failure message prints and the mechanism behind it — an explicit
stability affirmation line the check honours, a waiver registry entry, or a recorded baseline the
re-stamp advances. Then correct `§5`'s risks row, which today corrects the C7 consequence and is
silent on this one.

### H4 — spec-2 AC6 and AC1 cannot both hold

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-2.md` `§6` AC6.

AC6 requires `git grep -l '\.claude/SESSION-KICKOFF\.md'` to return nothing outside build records.
S3 keeps `.claude/SESSION-KICKOFF.md` as location 2, S2 builds the discovery loop AND the not-found
string "from the same array the verb prints", and AC1 requires `--locations` to print that exact
path. The array therefore spells the string inside `skills/session-kickoff/manifest-check.sh`, which
is not a build record — verified live at `manifest-check.sh:54`, and also carried by `AGENTS.md:54`,
`WIRE-INTO-PROJECT.md:330` and `tools/memory-tree/README.md:166`, all of which `§3` and `§5` keep.

A builder driving AC6 to green deletes location 2, dropping the only location every existing adopter
uses and contradicting `§3`'s explicit no-retrofit non-goal. A builder driving AC1 ships AC6
permanently red.

**Fix.** Scope AC6 to the surface it means. Exempt the engine and its self-test, which must spell
location 2 by S3: e.g. the grep excludes `skills/session-kickoff/*` and `memory/builds/*`, or AC6 is
inverted to "the string appears in exactly the array, its self-test, and the migration note, and
nowhere else". The unreachable-by-construction basename dodge is not a fix.

### H5 — the four `docs/`-spelled manifest sites are in scope and unobserved

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-2.md` `§6` (add a criterion); `§4` Files touched.

S7 puts the four extra `docs/`-spelled manifest sites in `WIRE-INTO-PROJECT.md` IN scope, and S4
requires `SKILL.md` Step 2 and `WIRE` `§4` to stop restating the list. Neither AC5 (grep scoped to
`skills/session-kickoff/manifest-check.sh`) nor AC6 (pattern `\.claude/SESSION-KICKOFF\.md`) reaches
a `docs/` spelling. The sites survive both and are live at `WIRE-INTO-PROJECT.md:336` (a `cp` step
into `docs/`), `:372`, `:498`, `:521`, plus `SKILL.md:224` — which `2026-08-13-spec-cKeyedLaunchpad-7.md`
`§3` assigns to this unit, not to itself.

Nothing else closes the gap: the README parks `AGENTS.md` as ungated, hygiene check 15's dead-path
population is `memory/` only, and the install-prefix gate's population covers `WIRE` for kit paths,
not manifest locations. F2 and F6 are the findings this unit exists to close, so a build green on all
twelve criteria can still ship a runbook telling adopters to install the manifest where the same
commit made the engine stop looking.

**Fix.** Add a criterion using the `docs/` spelling — `git grep -n 'docs/SESSION-KICKOFF\.md'`
returns nothing outside build records and the migration note — and name the five sites in `§4` so the
builder finds them. Add `SKILL.md:224` to this unit's Files touched, since spec-7 disclaims it.

**Raised in refutation, not itself a finding, and NOT run through the skeptic batch:** two skeptics
independently observed that no S-item repoints the SCAFFOLDING write target, which today writes
`docs/SESSION-KICKOFF.md`, while S4 strips `docs/` from the engine's Step 2 discovery list. If that
holds, an adopter's engine stops seeing an existing manifest and offers to scaffold a new one beside
it. Treat this as a check to run against `§2`, not as an audited defect.

### H6 — `READ_PATH_CEILING` is raised by spec-2 and lowered by nobody

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-6.md` `§2`, `§4` Files touched, `§6`; or
`2026-08-13-spec-cKeyedLaunchpad-2.md` `§3`.

spec-2 S11 raises the ceiling and its `§3` states: "`READ_PATH_CEILING` is not left raised. U6 lowers
it once the traps are evicted. This unit owns the raise and names the obligation; it does not own the
lowering." spec-6 never mentions the key — not in S1-S6, not in `§4`, not in the Files-touched row
for `.memory-tree.conf` (which reads "the raised arms floor" alone), not in any criterion or gate. A
grep for the key across the whole build folder matches spec-2 and nothing else.

The harm is mechanical: `tools/memory-tree/corpus_ids.py:413-421` only fails when the total EXCEEDS
the ceiling, so a ceiling left high is green forever and nothing surfaces the orphan. The conf's own
comment records the ceiling as a one-sided ratchet with every prior raise justified. The build would
ship a permanently slackened merge-bar ratchet while both specs read as if the raise were temporary.

**Fix.** Preferred: add the S-item to spec-6 ("lower `READ_PATH_CEILING` to the post-eviction
measured read-path total plus the stated margin, recording the measurement in the conf comment"), the
conf to its Files touched, and a criterion pinning the new value against a fresh measurement. If
spec-6 declines it, spec-2 `§3` must stop naming spec-6 and instead park the lowering as a backlog
row with a real id, because nothing on the bar will ever notice.

### H7 — `--for-paths` ships with no caller; both specs disclaim the call site

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-5.md` `§3`, or `2026-08-13-spec-cKeyedLaunchpad-7.md`
`§2`/`§6`.

spec-5 `§3` delegates its only consumer: "No `--for-paths` call site in the kickoff engine. That is
U7's edit to `SKILL.md`, sequenced after U2 settles the engine's structure." spec-7 mentions
`--for-paths`, `gotchas.py` and the checklist nowhere — not in S1-S6, not in `§4` or its Files-touched
table, not in AC1-AC12, not in `§7` — and its S3 closes the door: "Trim the prose that U2 through U6
make redundant, and nothing else." A grep across the build folder finds the verb only in the README
and spec-5.

Both M2 axes fail at once: work one spec puts OUT is not IN the sibling it names, and spec-5 hangs
its own stated goal ("make the recurring-bug-class checklist reachable at kickoff") on a unit
sequenced after it. The concrete cost is owner decision 3: evicted traps become records "reachable
through U5's `--for-paths` selector", and nothing at kickoff ever calls it. spec-6 then deletes eight
manifest bullets in favour of a path nothing in the build opens.

**Fix.** One spec must carry it. Cheapest is spec-5 keeping the one-line engine edit itself (it is a
Tier-1 unit with no dependencies and the verb is its own). Otherwise add an S-item plus a criterion
to spec-7 naming the invocation and the READY-card line it prints, and drop the "and nothing else"
clause in its S3.

### H8 — there is no inline-copy parity population for `region()` to join

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-4.md` `§2` S7, `§4` ("The marker discipline" and Files
touched), `§7`.

S7 says `region()` is "added to the inline-copy parity population" and `§7` names
"`tools/lib/resolve-python.test.sh`'s sibling inline-parity arm, extended by S7". That arm is not a
population mechanism. At `resolve-python.test.sh:82-90` the marker is hardcoded in both halves — the
`awk` extractor keys on `^# >>> resolve_python` and the discovery is
`git grep -l '^# >>> resolve_python' -- '*.sh'` minus the canonical path — and every hit is compared
against ONE canonical blob, `tools/lib/resolve-python.sh`. Nothing is parameterised by marker or
canonical source. A repo-wide `git grep '^# >>>' -- '*.sh'` returns resolve_python blocks and nothing
else, so `region()` at `tools/unattended/check-unattended.sh:167` carries no delimiters today and
must gain them — an edit to another kit's gate script. Neither that file nor the parity test appears
in `§4`'s Files touched. The unattended kit also already carries a second, textually divergent
`region()` at `tools/unattended/unattended.sh:103` with no parity gate pairing it.

`§7`'s "extended by S7" is partial acknowledgement, which is why this is a budgeting defect rather
than a contradiction: AC10's "that arm refuses an empty population" clause does block a vacuous pass.
But the unit whose whole rationale is not re-typing a hard-won predicate hides a new merge-bar
mechanism plus a cross-kit edit behind a phrase that reads as a list addition.

**Fix.** State the mechanism in `§4`: generalise the arm into a (marker, canonical source) table, or
add a second sibling arm keyed on a `region` marker with canonical `check-unattended.sh`. Add
`tools/unattended/check-unattended.sh` (it gains the delimiters) and `tools/lib/resolve-python.test.sh`
to Files touched. Decide the pre-existing divergent third copy: bring it into the population or waive
it in `§3` with a reason.

### H9 — spec-1's state table has no state for an adopting repo

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-1.md` `§4` "States and reports", `§2` S2, `§6`.

The four enumerated states assume the repo under inspection is this one, so a tracked
`skills/session-kickoff/{SKILL.md,MANIFEST-TEMPLATE.md,manifest-check.sh}` always exists to compare
against. `check-wiring.sh` is a copy-in kit — `WIRE-INTO-PROJECT.md:412` instructs copying it into
`<project>/tools/` — and it `cd`s into `$ROOT`, the repo under inspection, a hazard its own comment at
lines 73-76 already records for the resolver. An adopting repo has the machine-global junction so
`/session-kickoff` fires everywhere, and no tracked kit source. There is no state for "install
present, tracked side absent", and `§5` claims the enumeration is exhaustive.

Every other arm in that file resolves both install prefixes with `first_of` and SKIPS when the kit is
not adopted; the recall arm's own comment says a permanent false alarm "is the fastest way to train
every node to ignore the wiring verifier". As specced, the check reports UNWIRED with a Fix line the
operator has already followed, at every SessionStart, forever, in every adopting repo.

One supporting claim in the original finding does not survive and is dropped: `--check` is NOT a gate
leg. The `check-wiring self-test` leg runs `tools/check-wiring.test.sh`, and `WIRE` says in terms not
to put `--check` on the bar. The false alarm is a SessionStart-noise defect, not a red bar.

**Fix.** Add a fifth state — install present, tracked kit source absent in `$ROOT` → SKIP (not
adopted here) — matching the file's existing skip idiom. Make S2 say the comparison is conditional on
a tracked source existing. Add the arm, with an adopter-shaped fixture.

### H10 (blocker-adjacent) — spec-6's own cap reds bullets spec-6 keeps, and AC1 is out of reach

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-6.md` `§2` S5, `§4`, `§6` AC1/AC7/AC10.

Measured against the traps section at BASE: 27 bullets, 14,665 normalised bytes, 19 of them over 400
bytes. `§4`'s own arithmetic removes exactly ten (S1's eight duplicates, S2's one eviction, S3's
merge-driver bullet). Even under the most favourable possible selection — deleting the ten LARGEST
bullets, 7,837 B — 6,828 bytes survive, before S1's eight replacement pointer lines. AC1's "under
4,000 bytes" is therefore arithmetically unreachable without rewriting bullets no S-item authorizes.
Independently, `§4` names the new-record procedure bullet as "correct and stays" and it measures 492
bytes, over S5's own 400-byte cap; the 32-KiB-gate bullet is 1,198 B and the gate-leg bullet 595 B.
S6 authorizes one-lining the five orphan classes only, not the machine-local survivors.

So the unit's new check fails on the unit's own manifest: AC7 and AC10 cannot both hold, and the
builder discovers mid-unit that a rewrite of every surviving trap is required — work no scope item
grants.

**Fix.** Redo the arithmetic in `§4` against the measured section, then choose: add an S-item
authorising a rewrite of the surviving machine-local bullets to the cap (naming the three that exceed
it), widen the eviction set, or move AC1's target to a number the authorized edits reach. AC1 and AC7
must be simultaneously satisfiable before this unit is built.

### H11 — spec-6 AC2 names no observation, and it is the only criterion for the unit's largest edit

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-6.md` `§6` AC2, and `§4`.

AC2 reads: "`git grep -c` finds no surviving manifest bullet whose substance is carried by an
existing `memory/gotchas/` record; each deleted one leaves a pointer naming the record." It names a
command with no pattern, and the predicate — does this bullet's SUBSTANCE duplicate a record — is a
classification over 27 bullets against 13 records that the spec never enumerates. `§4` gives only the
counts ("eight are already carried by an existing record") plus one named example. The criterion
cannot be decided without redoing the classification the grounding did and did not record, and the
only other criterion touching S1 is AC1's byte count, which the WRONG eight satisfies equally well.

Contrast AC3, which states a runnable procedure for the wiki-link claim, and AC5-AC7, which each name
a command and an outcome.

**Fix.** Put the classification in `§4` as a table: each of the eight bullets (first few words) to
its `memory/gotchas/` record file. AC2 then becomes decidable — those eight bullets are gone, and the
traps section contains a pointer line naming each of the eight record filenames, checked by grep for
the filenames.

### M1 — C7's 25,600-byte cap is the one number in the build with no derivation

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-3.md` `§2` S1 and `§4`; cite the record in `§10`.

25,600 appears in S1, AC1, and an "Alternatives rejected" bullet that argues for the env override,
not for the number. No measurement, margin or rule is stated for it anywhere. The uneven discipline
is inside the same spec: `§4` derives C8's 400 by measurement ("This repo's longest line is 303
bytes... at 76% of the cap") and measures the manifest at 20,920 normalised bytes — the analogous
statement for C7 is simply absent. The sibling spec-7 `§4` ("The limit is measured, not chosen") and
its AC9 ("not a round number inherited from another file") apply the opposite rule in the same build,
and `memory/gotchas/pin-copied-from-another-corpus.md` states it verbatim: every pin, floor, ceiling
and cutoff is MEASURED at adoption, never inherited; the symptom is "either always green... or always
red". Here: 22% slack over gov's measured size, three times under the adopter manifest at 77,056 B —
and after spec-6's eviction, roughly 2.5x the file it guards, which spec-6 `§4` half-concedes.

**Fix.** Derive it, or state explicitly why a kit-wide ceiling shipped to arbitrary adopters cannot
be measured on one corpus and what rule set this number instead. Record the figure a future raise
would have to argue against, and say what C7's slack becomes after the eviction lands.

### M2 — spec-2's migration story mis-states the channel it relies on

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-2.md` `§5` Production-readiness, migration/rollback row.

"Adopters at `docs/` must move, which is what the manifest-format WARN channel exists to tell them"
is wrong twice. Discovery runs at `manifest-check.sh:54-58` and exits 2 there when no listed spelling
holds a file; the version WARN is at lines 69-74, strictly AFTER discovery, so a manifest at a
dropped spelling can never reach it. And the WARN fires only on a marker-version delta, which `§3`'s
last bullet says this unit does not create. The documented adopter invocations are pathless
(`WIRE-INTO-PROJECT.md:366` and `:368`), so they depend on discovery: those adopters' pre-commit and
CI legs hard-error on the kit re-pull with no upgrade signal ever emitted.

AC4 does require the not-found message to name the supported locations, so some remedy text gets
written — but the required migration row is empty for the population the unit breaks.

**Fix.** Correct the sentence to the real mechanism, and write the migration path: the exit-2 message
an adopter sees, the one-line move, and where in `WIRE` the upgrade note goes. Settle the engine-side
consequence too (see H5's adjacent note).

### M3 — three of the four verb-list copies are unobserved

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-5.md` `§6`.

S5 puts ALL FOUR copies of the verb list in scope and `§4` names them: the module docstring, `main`'s
fallback usage line, `render()`'s help block, and `tools/memory-tree/README.md:22` — all four
verified in source. Only `render()`'s copy is observed, via AC8's green bar including hygiene check
17's byte-compare of the help block into `INDEX.md`. AC4 does not close the gap: it specifies the
per-verb arity usage `--for-diff` prints one branch earlier, a different string. No gate reaches the
docstring or the kit README. `§4` itself names this as the two-answers-to-one-question class and says
it is on this change's own checklist — then leaves three of four ungated.

**Fix.** Add one criterion that binds the four: a single grep for the new verb returning a hit in
each of the four files, or (cheaper and self-maintaining) a `--selftest` arm asserting the docstring
line, the fallback usage line and the rendered help block agree.

### M4 — spec-4 and spec-7 both edit `SKILL.md` Step 3, with no hand-off

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-4.md` `§2` S4 and `§4`;
`2026-08-13-spec-cKeyedLaunchpad-7.md` `§2` S1 and `§6` AC1; the README's dependency table.

The seven-field enumeration lives at `MANIFEST-TEMPLATE.md:43-50` and its engine copy at
`SKILL.md:119-130`. Its seventh bullet is the Risk-tier bullet, running through line 130, and the
"nine canonical sections" clause spec-7 S1 and AC1 must correct sits INSIDE it. spec-4 S4 replaces
that enumeration with the verb and its AC9 hardens the replacement (grep for the seven field names in
`SKILL.md` returns zero), while spec-4 `§4` drops the tier from the sealed constant entirely, sending
only the tier ENUMERATION to the manifest's section B. Coordination is absent in both directions: the
README gives spec-4 an edge to spec-3 only and spec-7 edges to spec-2 and spec-6, and spec-7 `§3`
divides this file with spec-2 alone.

Sequenced last, spec-7 either re-adds prose spec-4 deleted or cannot satisfy AC1. And the generic
high-risk/design-pass heuristic at `SKILL.md:125-130` — engine behaviour for projects that define no
tiers, and what makes Step 3 produce a spec at all — is claimed by neither spec and has no home in
the manifest's tier-rule section.

**Fix.** Give the whole bullet one owner. spec-4 S4 should state that it deletes the Risk-tier bullet
and say where both the section-count figure and the no-tiers heuristic land. spec-7 S1/AC1 then
either re-point at the surviving site or drop, since spec-4 will have corrected it. Add the missing
edge to the README's Depends-on column.

### M5 — spec-7 names a gate that cannot decide two of its criteria

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-7.md` `§7`, and `§2`/`§4` if a carrier is added.

AC7 ("honours the positional limit") and AC8 ("the new leg fails when the engine exceeds its limit,
asserted with a fixture rather than by inspection") have no named carrier that can produce them.
`tools/check-template-size.sh` has no sibling test at BASE and defines no `fail()` helper, so the
harness meta-gate does not discover it either; `§4`'s Files touched adds no test file. `§7`'s
`tools/run-gates.test.sh` is the manifest canary: it parses `gate-legs.json`, checks name and argv
shape and that every guard names a tracked path. It never executes a leg, so it cannot observe a leg
failing.

This one is CONTESTED and is reported at its agreed core. One skeptic held that a persistent carrier
is required and is unbudgeted; another held that "asserted with a fixture" is this set's idiom for a
build-time scratch assertion, needing no new tracked file — and separately refuted the identical
claim raised by another lens. What both accept: `§7` names a gate that cannot decide AC7 or AC8.

**Fix.** Either add `tools/check-template-size.test.sh` to `§2` and Files touched — and with it the
govkit registry entry and map coverage the bar will demand — or restate AC7/AC8 as build-time
assertions and remove the gate claim from `§7`, so nothing on the bar is credited with proving them.

### M6 — the "curly apostrophe" the prose pass must preserve does not exist

**Edit:** `2026-08-13-spec-cKeyedLaunchpad-7.md` `§4` ("The three strings that are not prose") and
`§6` AC4.

Both say the asserted READY sentence must be preserved "byte for byte including its em-dash and curly
apostrophe". Verified with `od -c` on both sides — `skills/session-kickoff/SKILL.md:166` and the
`grep -qF` at `tools/unattended/check-unattended.sh:366` — the em-dash is U+2014 and the apostrophe
is straight ASCII 0x27. Only the em-dash is multibyte. This is the one paragraph telling the builder
which bytes are load-bearing, and it names the wrong byte: a pass that "restores" the curly form
breaks check 12 of `check-unattended.sh`, which, as `§4` itself warns, reports as an unattended-run
defect and points away from the edit that caused it.

**Fix.** Correct both to "em-dash preserved; the apostrophe is straight ASCII". AC6 (running
`check-unattended.sh`) backstops it before landing, so the cost is a corrected sentence, not a shipped
defect — but the sentence is currently a false statement about source.

---

## Refuted

Twelve candidates did not survive. Recorded so they are not re-raised.

| Spec / section | Claim | Why it was refuted |
|---|---|---|
| spec-6 `§6` AC8 | Undecidable — names no command | Names two concrete subjects (agent-cap version, drift pin) and `§4` gives both defect and target; a bounded read of two bullets against the constants their gates print decides it |
| spec-7 `§2` S3 / AC9 | The trim has no positive criterion, so it can be skipped | The dangerous direction IS bound (AC3-AC6 pin the three strings; AC6 runs the checker), and sibling criteria assert the redundancy removal. A small trim is a quality miss, not a wrong build |
| spec-1 `§2` S2 / AC2-AC3 | No criterion discriminates which of the three files are compared | S2 names the three files unambiguously and AC2-AC4 observe the comparison; the missing-file arm is mandated by S4 and its text quality by AC6. Test-strength nit over a few lines of loop |
| spec-7 `§6` AC9 | "within a stated margin" states no margin | Deliberate: the limit is measured AFTER the trim, so no number can exist at authoring time; `§4` requires the number to live beside the measurement, and `§3` plus AC9's own clause block the ported-pin outcome |
| spec-4 `§2` S8 | The v1.3 format bump has no criterion | `§7` names `check-kit-versions.sh` and AC12 requires a green full bar, which runs that leg; the version WARN already exists at BASE; the ordering edge to spec-3 is declared in the README |
| spec-4 S3 vs spec-6 S5 | Both units will claim check number C10 | Neither spec spells a number for its own check anywhere, so no interface disagreement exists; both rewrite the same two files, so M6's disjoint-write-set test already forbids parallel building. Ordinary build-time assignment |
| spec-4 `§7` | The named parity arm cannot see the copy, so AC10 passes vacuously | AC10 requires the arm to refuse an empty population, so an unextended arm fails on inspection. What survived is the budgeting half, folded into H8 |
| spec-3 `§6` AC13 | Demands a negative fixture with no harness to hold it | "asserted by a fixture, not by inspection" is this set's idiom for a build-time proof; the observation named (disagree the constant, run the script, expect non-zero) costs a scratch mutation |
| spec-6 S5 / `§5` | Adds an adopter-visible check with no format bump, breaking the migration story | The WARN is version-vs-constant, not per-check; spec-4 moves the constant in the same landing series, so no adopter can report current while missing the new rule. `§5` answers migration explicitly |
| spec-6 `§6` AC1 | Baseline stated as 14,821 where siblings say 14,665 | Both correct: on-disk CRLF vs LF-normalised, verified. No criterion, gate or arm reads the narrative figure, and the two converge once the file moves under the LF-pinned prefix |
| spec-7 `§6` AC8 (second lens) | No test carrier exists, so the AC gets dropped | Satisfiable with an ad-hoc fixture; a forecast about the builder, not a defect in the spec. The narrow surviving core is M5 |
| spec-2 `§2` S3 | Making the memory-tree path location 1 couples a standalone kit, against prior art | The prior decision was that the CHECK must not depend on the memory-tree gate; a hardcoded default string reads no conf and calls no memory-tree code. `§3` keeps `.claude/` as location 2 for exactly the repos that lack the tree |

## Unverified

None. Every candidate received a skeptic verdict; nothing is outstanding for lack of one. The one
loose thread in this record — the scaffolding write target, noted under H5 — was raised BY a skeptic
during refutation and was not itself put through the batch. It is flagged as a check for the author,
not as an audited finding.

---

## What to change, per spec

**`2026-08-13-spec-cKeyedLaunchpad-1.md`** (1)
- H9: add the fifth state (install present, tracked kit source absent → SKIP), make S2 conditional on
  a tracked source, add the arm with an adopter-shaped fixture.

**`2026-08-13-spec-cKeyedLaunchpad-2.md`** (4)
- H4: rescope AC6 so the engine's own array and self-test are exempt; it currently contradicts AC1.
- H5: add a `docs/`-spelled criterion; name the five surviving sites in `§4`; claim `SKILL.md:224`,
  which spec-7 disclaims. Check the scaffolding write target while you are in there.
- H6: either accept that spec-6 will not lower the ceiling and park it with an id, or confirm the
  S-item lands in spec-6.
- M2: rewrite the migration row to the real mechanism and write the actual migration path.

**`2026-08-13-spec-cKeyedLaunchpad-3.md`** (5, one blocking)
- B1: replace the rename mechanism (`--follow`, or a recorded baseline), state the observed git
  behaviour in `§4`, and rewrite AC9's fixture to perform a real move and assert the walk reaches
  through it. Nothing else in this unit should be built first.
- H1: design the three-month branch (which timestamp, compared to what) and add an aged-fixture
  criterion.
- H2: add the two `--staged` criteria that observe S4's placement contract.
- H3: state what clears a C9 red and correct `§5`'s risks row.
- M1: derive 25,600 or state the rule that set it; cite the ported-pin record in `§10`.

**`2026-08-13-spec-cKeyedLaunchpad-4.md`** (2)
- H8: state the parity MECHANISM, not the outcome; add the two missing files to Files touched; decide
  the pre-existing divergent copy.
- M4: take full ownership of the Risk-tier bullet and say where the section-count figure and the
  no-tiers heuristic land.

**`2026-08-13-spec-cKeyedLaunchpad-5.md`** (2)
- H7: keep the one-line engine call site here, or confirm spec-7 accepts it with an S-item and a
  criterion. Today no unit owns it.
- M3: add the criterion that binds all four verb-list copies.

**`2026-08-13-spec-cKeyedLaunchpad-6.md`** (3, one blocking)
- H10: redo the arithmetic; make AC1 and AC7 simultaneously reachable inside authorized scope. This
  unit is not buildable as written.
- H11: put the eight-bullet classification in `§4` and rewrite AC2 against it.
- H6: accept the ceiling lowering with an S-item, Files-touched row and criterion — or send it back.

**`2026-08-13-spec-cKeyedLaunchpad-7.md`** (4)
- H7: accept the `--for-paths` call site with an S-item and criterion, or spec-5 keeps it.
- M4: re-point or drop S1/AC1 once spec-4 owns the bullet.
- M5: name a carrier that can decide AC7/AC8, or restate them as build-time assertions and drop the
  gate claim.
- M6: the apostrophe is straight ASCII; correct `§4` and AC4.

**One cross-set pattern worth a convention.** Three confirmed findings (H6, H7, M4) are the same
failure: a `§3` non-goal hands an obligation to a named sibling that never accepts it, and no gate
detects the orphan. When these edits are made, the cheap invariant is that every `§3` bullet naming a
sibling unit must be matched by an S-item in that sibling — checkable by reading two sections, and it
would have caught all three at authoring time.
