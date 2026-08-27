## Verdict: CLEAN WITH FIXES

**Serves:** spec-audit TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-5 TOOL-aBoundedCeiling-6

The fold is good. Round 1's blocker is genuinely dead, all seven of its HIGH/BLOCKER findings are closed or closed-with-residue, and every LOW was picked up including both README nits. Nothing here makes a spec unbuildable, so this is not BLOCKED. What survives is one cross-unit consequence round 1 could not see because it audited the units singly, one scope item the fold added without a mechanism to implement it, and a tail of stale-text defects concentrated in exactly the sentences the fold edited around.

Two findings are worth an owner's attention before build: **R2-1** (specs 1 and 5 together red an adopter's bar) and **R2-2** (spec-5's new S7 has no provenance channel). Both are spec edits, neither is large.

---

## What round 1 asked for, and what the fold delivered

### `TOOL-aBoundedCeiling-1`

- **BLOCKER — S8/AC7, the deletion causes what AC7 prevents.** **CLOSED.** S8 and AC7 are gone, the AC list ends at AC6, and `:52-58` N6 states the refutation with the mechanism (`run_one`'s empty-budget treatment) rather than just deleting the scope item. F3 at `:228-231` re-resolves in the same direction and says rev-1 was "wrong in the dangerous direction". This is the right shape for a folded blocker: the correction is recorded, not quietly applied.
- **HIGH — §4/F1, the derivation launders two live breaches.** **CLOSED, one residue.** `:87-102` excludes any leg carrying a declared `BUDGET_*` from the 3× formula and prices the `unattended kit gate` case explicitly. The fold did not take round 1's suggested fix (ship the `BUDGET_*` value as the manifest ceiling); it argued a different answer — a 1600 s hang bound in the manifest and the 120 s cost bound left where it is — and the argument holds, because those two numbers answer different questions. The silent-raise charge is answered. Residue is R2-7: `playbook validity gate` is excluded from the formula and given no replacement number.
- **MEDIUM — §10, two governing records uncited.** **CLOSED** at `:266-271`, both ids cited with an honest note about why the recall probe missed them. The "state which candidate this unit takes" half is answered *wrong* — see R2-6.
- **MEDIUM — §5 vs §7 acceptance homes.** **CLOSED** at `:176-178`, routed correctly and with the reason (`run-gates.test.sh` IS the canary leg).
- **MEDIUM — AC6's reuse-cache clause false for 48 of 85 legs.** **CLOSED** at `:201-206`, narrowed to what is true and carrying the 48-of-85 number as a stated design consequence.
- **LOW — Inventory's misplaced "and ceilings exist".** **CLOSED** at `:152`.

### `TOOL-aBoundedCeiling-5`

- **HIGH — the parity check names two programs and the wrong manifest.** **CLOSED, thoroughly.** S5 at `:32-36` names `govkit.py` check 7h and explains why the distinction is material; the Inventory rows at `:98-99` split the arm from where its failing case is staged; AC3 at `:134-135` names `govkit selfcheck`; §7 at `:148` adds that leg; F2 at `:157-161` is re-resolved with "the premise, not the preference, is what changed". That last sentence is the difference between folding an audit and obeying one.
- **HIGH — the copied seam crashes on its below-floor path.** **CLOSED** via S6 (`:37-41`) plus AC5 (`:136-138`), which is a real failing-case-first criterion. Residue: the *"and say so"* half — see R2-5.
- **HIGH — the version bump routed to a file with no version.** **CLOSED.** Inventory `:96-97` names `run-gates.sh:19` and the README marker, N2 at `:50-54` is amended to permit exactly that one line, and §7 at `:149` adds `kit version markers`.
- **MEDIUM — no durable lever for a slow-node adopter.** **PARTIALLY.** The lever exists (S7, `:42-44`) but has no mechanism (R2-2), and neither text correction round 1 asked for was made (R2-4).
- **LOW — `TOOL-aPacedTurnstile-12` uncited.** **CLOSED** at `:193-200`, with a stated reason `guard` stays out and the row left open.

### `TOOL-aBoundedCeiling-6`

- **MEDIUM — the prescribed edit set reds this unit's own gate twice.** **CLOSED for the two files named**, at `:118` and `:120`, and the `check-unattended.sh` row was replaced by the explanatory note at `:127-131`. That note is now slightly overclaiming — see R2-3, which is the same class one file over.
- **MEDIUM — the sibling unbounded seam left unnamed.** **CLOSED, and the lazy way.** S2 at `:27-35` is one helper at both seams, N1 at `:45-48` records the widening, AC5 at `:171-174` exercises the second site, §10 at `:228-232` names it. Residue: the key's own definition did not widen with it (R2-3b).
- **LOW — the observation record's `Serves:` line.** **CLOSED**; all three specs' `gen:spec-records` regions now carry `-6`.

### Build README

Both LOWs closed: `:36-39` now points at spec-1 §4 instead of restating a number, and `:102` reads `BUDGET_*`. One sentence the fold walked past — R2-8.

---

## Surviving findings

**R2-1 · HIGH · specs 1 + 5 together · the first `govkit apply` after unit 5 reds an adopter's bar**

Spec-1 S6 (`:36-37`) and AC3 (`:193-195`) make the declaration check presence-scoped: once a manifest carries one `ceiling`, every row must carry one. Spec-5 AC1 (`:129-130`) has the emitter write `ceiling` onto kit-owned legs while N1 (`:48-49`) leaves the project's own legs without one. An adopter's manifest is a merge, not a rewrite — `govkit.py:4231` reads their existing rows, `:4319`/`:4321` replace-or-append only kit rows, `:4337` writes the whole list back. Target-authored rows survive with no ceiling beside kit rows that now have one, and the runner refuses. The mixed manifest is not hypothetical: `govkit.py:4290` exists specifically to protect a leg "the target wrote". Spec-1 `:140-141` asserts the opposite — that once unit 5 lands "the scoping stops mattering on its own".

*Smallest fix:* scope S6 to rows the manifest can be held responsible for (a row a kit receipt claims), and replace spec-1 `:140-141` with one sentence saying what a mixed manifest does. The `subject` precedent did not hit this because `subject` has no presence-requirement check; the ceiling adds one, and that is the novel half.

**R2-2 · HIGH · spec-5 · S7 and AC6 are provenance predicates with no provenance channel**

S7 (`:42-44`) says the emitter never overwrites "a leg's ceiling that the target itself declared"; AC6 (`:139-140`) says "a `ceiling` a kit did not write". The emitter's only record of what it wrote is the receipt's emitted row at `govkit.py:4328-4331`, which carries name, kit, argv, guard, subject, guard_dropped, history_depth — and no ceiling. Spec-5's Inventory (`:91-99`) has no row for it. Every implementation the spec permits fails an arm: preserve-any-existing withholds forever after the first apply and fires the withheld-report on every leg on every apply; preserve-when-different-from-descriptor withholds exactly the kit updates; preserve-only-unclaimed-rows makes S7 vacuous, since N1 already says the kit writes nothing to project legs. The code states the rule three lines above the site it would go in — `govkit.py:4322-4327`, *"a field that reaches the target's manifest but not the receipt is a field no drift check can ever see move. TOOL-dUnstalledConvoy-26"* — which is the same class S6 is repairing six lines up.

*Smallest fix:* one Inventory row for `govkit.py:4328-4331` (the receipt's emitted row carries `ceiling`), a decision in that same row on whether `RECEIPT_SCHEMA` at `govkit.py:45` moves, and S7 restated as its predicate rather than its intent — withhold only when the target's ceiling differs from what the receipt recorded. Then amend AC6 to observe both arms.

**R2-3 · MEDIUM · spec-6 · the Skill render pair is the third file pair, and it is not in the Inventory or §7**

§5's user-docs bullet (`:156-157`) promises "the rendered Skill's close section gains one sentence". That section is `tools/unattended/SKILL.template.md:552`. `adopt-unattended.sh --check` (`:231-247`) renders the template against `.unattended.conf` into a temp file and `diff`s it against the tracked `.claude/skills/unattended/SKILL.md`, exiting 1 on drift. That is the `unattended skill wiring` leg — `tools/gate-legs.json:652-660`, subject `repo`, no guard, so it runs on every bar. Neither file is in the Inventory (`:115-125`) and §7 (`:178-181`) names neither the leg nor the suite. Editing the template without re-rendering, or re-rendering without the edit, reds a leg on every bar. The Inventory note at `:127-131` compounds it: "the three files it reads are the ones edited above" is true of `check-unattended.sh` and false of this leg, which reads a fourth.

*Smallest fix:* two Inventory rows — `tools/unattended/SKILL.template.md` (the sentence) and `.claude/skills/unattended/SKILL.md` (RE-RENDER in the same commit via `bash tools/unattended/adopt-unattended.sh`) — and `unattended skill wiring` added to §7.

**R2-4 · MEDIUM · spec-6 · the key is defined for one command and applied to two**

S2 widened to two seams (`:27-35`, verified at `unattended.sh:988` and `:2695`) and the key's definition did not follow. S1 at `:26` still reads "the wall-clock bound on `$GATE_CMD`", N3 at `:51-53` repeats it, §1 (`:17-20`) and the title describe only the close's gate run, and §4's default derivation at `:103-107` prices gov's bar alone. AC5 at `:171-174` then says `$WIRING_CHECK` "sleeps past the bound" — singular, against one conf key. This is not internal prose: Inventory `:117` routes the definition into `.unattended.conf`'s comment and `:119` into the protocol's declared-key table, so the narrow wording ships to every adopter, and a builder has to invent whether the wiring seam takes `GATE_BOUND` or a second number.

*Smallest fix:* restate S1 as the bound on any project-declared command this driver runs, naming both `$GATE_CMD` and `$WIRING_CHECK`; widen N3 and §1 to match; add one sentence to §4 saying the same hour covers the preflight check.

**R2-5 · MEDIUM · spec-5 · §4's rejected alternative, §5's observability sentence, and §10's self-correction do not agree with S7**

Three small text defects the fold left in one area:

- `:107-109` still rejects *"Let adopters hand-write ceilings"* on the ground that a downstream-authored ceiling drifts on the first kit update — which is now an argument against the accepted S7. N1 at `:48-49` is byte-identical to rev-1 and still says nothing about which lever a slow-node adopter reaches for. Both are exactly what round 1 asked to be corrected.
- The floor's withhold report is committed to in §10 (`:205`, "this unit writes the second") and appears in no §2 item and no Inventory row. S6 is the `KeyError`; S7's report is the project-override withhold, a different one. §5 `:116-117` still says the decision is "reported the way `check_target_reads_subject`'s is", which is silent (`govkit.py:4306-4307` sets the key and prints nothing).
- `:202` attributes "already exists" to §4; grep says the phrase occurs once in the whole spec, at `:179`, in §10 itself.

*Smallest fix:* rewrite `:107-109` as the accepted alternative rather than the rejected one; add the withhold line to S3 in one clause and extend AC2 to observe it (or delete §5's promise); change "§4 says" to "the paragraph above".

**R2-6 · MEDIUM · spec-1 · "takes candidate (2)" is a claim the unit refuses to honour**

`:96-97` says "This unit takes candidate (2), re-declare the ceiling with the reason beside it", and `:269` repeats it in §10. `TOOL-aCollapsedScan-4`'s candidate (2) is the `BUDGET_kit_gate=120` re-declaration in `run-unattended-gates.sh`. N6 at `:52-53` forbids touching that file at all, and `:100-101` confirms the declaration stays at 120 with the row closing "only when someone rules on the cost half". Round 1's MEDIUM offered the honest answer ("If neither, ...") and the fold answered with a candidate name instead. The harm is narrow but real: §10 invites a future session to close an OPEN row that stays open.

*Smallest fix:* "This unit takes NEITHER candidate" in both places — the paragraph's actual argument (a hang bound and a cost bound are two questions) survives intact and is stronger without the claim.

**R2-7 · LOW · spec-1 · one excluded leg has no ceiling number anywhere**

`:87` excludes the three `BUDGET_*` legs from the formula and `:99-100` supplies a number for one of them. `playbook validity gate` is `BUDGET_playbook_validity_gate=120` against 161.780 s measured, and is a real manifest row — so it is excluded from the derivation rule and given no replacement, while S1 at `:26` demands a ceiling on every row. (`unattended skill wiring` is unaffected: 5.512 s against the 60 s floor yields 60 either way.)

*Smallest fix:* one clause in §4 naming the number — 486, or 120 with the reason beside it.

**R2-8 · LOW · README · the overview describes the dropped build**

`:49-50` — "The remaining two units are about paying for that bar once per landing instead of twice, and about a forced run keeping the guards that scope it" — names `-2` and `-3`, both recorded DROPPED at `:91` and `:94`, while the Units table six lines below at `:56-58` lists 1, 5 and 6.

*Smallest fix:* name the live pair — carrying the field to adopters through the deployer, and bounding whatever gate command an unattended close runs.

**R2-9 · LOW · specs 5 and 6 · the fold's own new ACs have no test home**

spec-5 `:121` still reads "AC1 through AC4, in `tools/govkit/selftest.py`" while AC5 (`:136`) and AC6 (`:139`) are new; the same sentence misroutes AC4, which is a whole-bar `GATE_SELFTESTS=1` run asserting the `govkit selftest` leg is green and cannot live inside the suite that leg runs. §6 also lists its criteria AC1, AC2, AC3, AC5, AC6, AC4. spec-6 `:152` reads "AC1 through AC4" while AC5 sits at `:171-174` — the criterion that exists precisely because the second call site would otherwise be "asserted only by inspection" is the one with no declared home. The fold rewrote this exact sentence in spec-1 (`:176-178`) and did not carry the edit to the other two.

*Smallest fix:* spec-5 §5 — "AC1, AC2, AC3, AC5 and AC6 in `tools/govkit/selftest.py`; AC4 is a whole-bar run and belongs to no suite"; move the AC4 bullet below AC6. spec-6 §5 — "AC1 through AC5", and add the preflight refusal to the observability bullet.

---

## What the fold got right

- **The blocker was killed at the root, not patched.** N6 does not just drop S8; it records the mechanism that refutes it and states the general rule (a leg may hold a ceiling in the manifest and a `BUDGET_*` beside its suite). F3's resolution was rewritten to say rev-1 was wrong in the dangerous direction. That is the difference between folding an audit and complying with one.
- **Two findings were answered by disagreeing with the auditor, correctly.** The `BUDGET_kit_gate` fix ships 1600 s as a hang bound rather than round 1's suggested 120 s, with the two-numbers-two-questions argument written out. F2 in spec-5 was re-resolved on the ground that the *premise* was false, not the preference. Both are better answers than the ones offered.
- **Spec-6's S2 got smaller by fixing the class.** Round 1 offered "one helper at both seams" as the lazy option and the fold took it, with AC5 to exercise the site that would otherwise have been inspected only — which is the exact failure mode the target line's own comment records.
- **The AC6 narrowing is exemplary.** Rather than deleting the false clause, `:201-206` states what is true, states what is *not* claimed, and carries the 48-of-85 consequence as a design fact. A later reader cannot re-derive the wrong benefit from it.
- **Line citations remain sound.** As in round 1, no cited line number in `run-gates.sh`, `run-unattended-gates.sh`, `unattended.sh`, `govkit.py`, `check-unattended.sh` or `gate-legs.json` was found off by more than one. Every defect above is a wrong conclusion or a stale sentence, never a bad citation.
- **The three standing constraints hold.** No spec returns a `*.test.sh` leg to `tools/gate-legs.json`; `PROF_TIMEOUT` stays 0 on every row (spec-1 N1, with the turnstile evidence at `:104-113`); the three dropped units remain recorded in the README.
- The merge bar was not run and no `*.test.sh` suite was executed. Every verdict above is from reading source, `tools/gate-legs.json`, the live `gate-ledger.tsv` and `memory/backlog/TOOL.md`.

---

## Unjudged — no skeptic reached these

- **`s1-candidate-2-claimed-and-refused`** — no skeptic was assigned to it, but it is the same defect as F3, which *was* judged and confirmed at MEDIUM. I verified it independently against source: `memory/backlog/TOOL.md:226` spells candidate (2) as the `BUDGET_kit_gate` re-declaration, spec-1 `:52-53` forbids touching that file, `:100-101` confirms the declaration stays at 120. It is reported above as R2-6, and it contributes one detail F3 lacked — §10 at `:269` repeats the claim, so the fix is two edits, not one. Nothing in it is unverified.