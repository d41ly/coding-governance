# Pre-code review, round 4 — part 1 of 2, the engine and safety units, DEPL-dCarriedReceipt-1..8

**Serves:** spec-audit DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8

**Reviewed:** all 15 specs plus the build README, in ONE pass, against the round-3 fold at
`2f9d7a4f`. **Base:** `f39cf548`, worktree clean. Source read at `9ddcc5c9`; `tools/govkit/govkit.py`
and `tools/govkit/refusal_join.py` are byte-identical between the two, so every line citation holds
at either sha.
**Harness:** four primed finder lenses over the folded set (contradiction, underspecification,
unstated assumption, fold regression), then batched default-refute skeptics over every finding, then
one synthesis. Ten agents, all returned. Thirty-six confirmed entries arrived; deduplicated they are
the 21 defects across both parts of this record, and eleven were refuted and are named so round 5
does not re-file them.
**Why this record is in two parts:** the Serves id list renders into one build-README table row and
15 ids blow its entry cap. That is DEPL-dCarriedReceipt-16, and round 1 split on the same boundary.

This record carries the findings against units 1-8. Units 9-15 are part 2,
`2026-08-25-review-DEPL-dCarriedReceipt-9-round4.md`, which also carries the convergence answer
and every blocker. Three findings in part 2 land edits inside this half as well: H1 rewords
`-7` S9's closing sentence, M6 replaces a clause in `-7` S9, and M1 adds a sentence to `-7` S4.

## Verdict: BLOCKED

No blocker lands in this half. The verdict is the BUILD's, carried on both parts so neither reads
as clean on its own; the three blockers are in part 2, against `-13` and `-14`.

## High

**H6 — `-6` AC6 names a command `load_deploy` refuses on, against a target this build does not fix.**
AC6: "`govkit.py plan --target <inCMS>` names exactly ONE surviving leg, `kickoff engine size
<=18KiB`, and not the fifteen that this run's own writes would satisfy". `cmd_plan` (`:1429`) calls
`load_deploy(target)` at `:1433`, before any predicate runs, and `load_deploy` (`:553-561`) raises
`Refusal` when `<target>/.governance/deploy.toml` is absent. `-6`'s own §4 says inCMS has none:
"inCMS's column is measured against a descriptor reconstructed from `.governance/kits.json`, because
inCMS has no `.governance/deploy.toml` at `9ddcc5c9`; reproducing it needs that reconstruction to
carry inCMS's `[kit.*]` layout overrides, without which the reading runs high." So the criterion is
unobservable as written — the command refuses before printing a leg — and no scope item in `-6`
creates the reconstruction. §3's land-alone bullet names only the `-1` ordering. `-4` handles the
identical prerequisite honestly, both in §3 ("`load_deploy` (`:553`) refuses without one;
the adopter-side unit writes it. That is a target-side prerequisite") and in AC3, which names the
descriptor it runs against; `-6` is the copy that does not.

**Edit:** rewrite AC6's opening in `-4`'s existing words — "`govkit.py plan --target <inCMS>`, run
against an inCMS checkout carrying the `.governance/deploy.toml` the adopter-side unit writes — its
14 kits at `prefix = \"scripts\"` with its `[kit.*]` layout overrides, the same descriptor `-4` AC3
names — names exactly ONE surviving leg..." — and add the target-side prerequisite to §3's
land-alone bullet in the sentence `-4` §3 already uses. A hermetic fixture reproducing that tree is
the alternative and is strictly more work; `-4` AC2's live-NicoCares reading establishes that a
hand-placed descriptor in a local checkout is by design for coverage units, which are read-only.

## Medium

**M4 — `-7` S1's unqualified quantifier contradicts the fold's own S9 text.**
S1: "every receipt row gov writes carries `gov_oid` and `oid`, both git blob oids." S9, as folded:
"Every row `apply` writes through the `unlanded` channel at `:2440` also carries neither field."
Both describe rows `apply` writes, `:2440-2441` is a receipt row, and they are opposites. Taken
literally, S1 stamps `gov_oid` onto rows that carry no `commit`, which is precisely S9's own "a row
carrying exactly ONE of the two is its own REFUSAL" arm — the outcome `-12` §4 names as the thing to
avoid ("scope it by nothing and it refuses on all 41 of inCMS's unattributable rows and no adopter
ever updates"). Three signals inside `-7` contradict the loose sentence, so a builder is unlikely to
implement it, but this spec elsewhere calls out "the contract's own unscoped-quantifier mistake" by
name, and this is the same shape.

**Edit:** amend `-7` S1 to "every receipt row gov writes for a LANDED file — the `writes` channel at
`:2443-2460` — carries `gov_oid` and `oid`. A row written through the `unlanded` channel at `:2440`
carries neither, as it carries no `commit` today, and this unit does not add them: there are no gov
bytes at that destination to hash."

## Low

**L2 — `-2`'s arm count is 2 in §4 and 3 in §5 and §7.** §4's Files touched reads
"`tools/govkit/selftest.py` (2 arms)" while §5 reads "three arms in `selftest.py`" and §7 "Adds three
arms to `tools/govkit/selftest.py`". Two of three say three, and the two-arm figure is the one a
builder budgets from. `-10` rev-3 folded this exact self-contradiction one spec over. **Edit:** in
`-2` §4 change "(2 arms)" to "(3 arms)" and note the correction in a rev-3 §9 entry.

**L4 — the `BRANCH_PIN` repair landed in one of four specs, and two of them cite the wrong line.**
The fold's message claims "a malformed backtick from round 3's BRANCH_PIN substitution repaired",
singular, against a class of four. `-9` §7 was genuinely repaired. `-5` §7 line 170, `-6` §7 line 214
and `-10` §7 line 226 were only rewrapped and still render an English sentence as an inline code
identifier: "`BRANCH_PIN (a shrink-only FLOOR, so it is re-derived at landing rather than pinned to a
literal here)`", each followed by a second "shrink-only" in the same sentence. `-5` and `-6` also
cite `tools/govkit/refusal_join.py:40`; the constant is at `:41` and `:39-40` is the comment above
it. The sentence carries a real landing obligation — re-derive the floor and move it in the same
commit with both values named — so it is load-bearing and currently unreadable in three places.
**Edit:** apply `-9`'s repaired shape verbatim in all three, identifier inside the backticks and
property in prose beside it — "`BRANCH_PIN` in `tools/govkit/refusal_join.py:41` is a shrink-only
FLOOR, so it is re-derived at landing rather than pinned to a literal here, and it is moved in the
SAME commit with both values named beside it, per that file's own convention" — dropping the
duplicated "is shrink-only" clause that follows.

**L5 — the README's landing order invites `-4` forward to a step where its own AC3 cannot go green.**
Step 6 reads "`-4` is independently useful from step 1 onward and may be pulled forward". The same
README's units table gives `-4` `deps` = 1, and `-1` lands in step 2. `-4` §3 states the dependency
as an order — "it lands after `-1`, because AC3 asserts the post-`-1` reading of `54` while the
pre-`-1` tree prints `55`" — and AC3 makes that an alarm, not a preference: "A reading of `55` after
`-1` means `-1` regressed, which is the assertion this AC is for." A builder who takes the invitation
reads 55 and spends a debugging cycle on a regression in a unit that has not landed. The README
supplies its own tie-break in the same section ("Each unit's §3 land-alone line is the authority"),
so two of its three signals are already right. **Edit:** change step 6 to "`-4` is independently
useful once step 2 is beneath it — it needs `-1`, whose reading AC3 asserts — and may be pulled
forward to step 3; it is the only unit that runs against a real adopter today."

**L6 — `-4` AC2's rewrap pushed the `--kits` list to column 0.** The fold's line-length pass changed
AC2's continuation from a two-space indent to column 0, so the line now begins
"check-install-prefix,gate-lint,kickoff-manifest,..." flush left inside a bullet whose other
continuations are indented two spaces and inside a multi-line inline code span. It survives as a lazy
paragraph continuation, so nothing renders wrong today; it is the only de-indented continuation in
the corpus and one blank line away from detaching from the criterion. **Edit:** re-indent the line by
two spaces, and if the width then breaks the limit, split the `--kits` value across two indented
lines rather than de-indenting one.

---

## What remains unverified

Nothing was executed. Every finding above is a spec read plus a source read at `9ddcc5c9`; no fixture
was built, no arm run, no verb invoked. Specifically:

- B3's wedge is mechanism-verified end to end in source, including the persistence seam at `:3115`,
  but no rename was landed, red and rolled back to observe the refusal on the following run.
- B2's `cmd_check` breakage is read, not reproduced: `row["block_id"]` at `:1570` is unguarded and
  `marker_pair(None, ...)` refuses at `:1706`, but no adopted receipt with a merged rule was built.
- H2's chosen answer — that `sha256` holds the TARGET's bytes at receipt-write time — is inferred
  from `cmd_apply` (`:2459`), `-8`'s ratified bullet and `cmd_check`'s integrity loop. It is a
  decision the owner should ratify in `-13` §8, not a fact I measured.
- The inCMS populations were not re-measured. M2 is arithmetic internal to `-9`; M3's 13 pairs and 26
  needles were not re-derived over either candidate population, and I cannot say which one they
  reproduce over.
- L1's "fourteen" is not derivable from `-13` as written, because S9 counts arms per branch rather
  than per criterion. The fixer must re-derive it against the enumerated branches.
- The adopter-side specs under the other repo's slug were not read this round, so cross-repo
  consistency of the descriptor prerequisite H6 and `-4` §3 both depend on is unchecked here.
- The fold's line-length pass was spot-checked at the sites findings pointed to, not diffed
  exhaustively across all 15 specs; L6 is the only rewrap regression I looked for and found.
