# TOOL-aHonedRuleset-5 — the last-audit stamp rule gets exactly one home

**Status:** SPECCED · rev-2 · 2026-09-04 · node a · Tier-2 · base 102e98f0 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aHonedRuleset-1-spec-audit.md](../reviews/2026-09-04-review-TOOL-aHonedRuleset-1-spec-audit.md) | spec-audit | TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-6 |

<!-- /gen:spec-records -->

## 1. Goal

One rule — how to compute the sha for a kickoff manifest's `last-audit` stamp — is written out in
seven places across five files, in two spellings that already disagree. Reduce it to one prose home
and one machine home, point the rest at them, and gate the pair so the disagreement cannot come back.

## 2. Scope (IN)

- **S1** — `skills/session-kickoff/MANIFEST-TEMPLATE.md:29-31` becomes the single PROSE home. Its
  text is unchanged. Every other prose carrier points at it or at the manifest instantiated from it.
- **S2** — `skills/session-kickoff/MANIFEST-TEMPLATE.md:121-124` loses the parenthetical restating
  the rule. The sentence already says "per the stamp rule"; the pointer stays and the restatement
  goes. Its unborn-branch clause is unique content and survives verbatim.
- **S3** — `skills/session-kickoff/SKILL.md:118-119` loses the inline rule. Step 2b's repair
  instruction becomes "sha per the manifest's own stamp rule", which resolves in whatever tree the
  engine is standing in and names no path.
- **S4** — `WIRE-INTO-PROJECT.md:437-439` loses the parenthetical. The step already opens with "per
  the template's Customize notes", so the pointer is already written and only the restatement is cut.
- **S5** — `skills/session-kickoff/manifest-check.sh:265` becomes the single MACHINE home. Its
  `STAMP_SHA_RULE` constant is repaired to carry the no-remote fallback it currently omits, and moves
  above line 197 so `RETROFIT` can interpolate it.
- **S6** — `skills/session-kickoff/manifest-check.sh:197` stops re-typing the rule inside `RETROFIT`
  and interpolates `$STAMP_SHA_RULE` instead.
- **S7** — two rows join `PAIRS` in `tools/check-playbook-parity.sh`, comparing the template's prose
  against the checker's constant, one row per git command in the rule. The gate's header gains a line
  saying its pair list is no longer playbook-only and one saying what these two rows do not cover.
  Both lines carry a pinned anchor so AC6 can observe them: the widening line contains the literal
  `no longer playbook-only`, and the scope-limit line contains the literal `compare two git
  merge-base invocations`. Neither string occurs in that file today, measured at 0 apiece.
- **S8** — `memory/guides/SESSION-KICKOFF.md` gets its `last-audit` re-stamp in the same commit,
  because `skills/session-kickoff/SKILL.md` and `skills/session-kickoff/manifest-check.sh` are both
  watched pathspecs on line 6 of that file.

## 3. Non-goals (OUT)

- **Not fixing the rule.** `KICK-cSettledDocket-1` is OPEN and records that the rule cannot satisfy
  the checker's own check 5 on a feature branch, because the merge-base predates every watched file
  the branch changed. That is a defect in what the rule SAYS. This unit only fixes where it is
  written. Single-homing is what makes that later fix a one-line edit instead of a five-file sweep,
  which is the argument for doing this one first.
- **Not touching `memory/guides/SESSION-KICKOFF.md:22`.** That line is this repo's own instantiated
  copy of S1, with `<remote>/<default>` resolved to `origin/main` as instantiation requires. It is an
  instance of the home, not a duplicate of it. Its own omission of the no-remote fallback is correct
  here — this repo has a remote — and adjudicating adopter manifests is not this unit's business.
- **No `--stamp-rule` verb on the checker.** `--locations` and `--task-skeleton` exist because a
  consumer needed to read a value at runtime. Nothing needs to read this one at runtime, and the
  parity rows extract from the file with `sed` exactly as the five existing rows do.
- **No seal.** Check 10 byte-compares the manifest's task region against `TASK_SKELETON`. The
  equivalent here is impossible and the checker's own header at lines 40-42 says why. See §4.
- **No cut to `memory/builds/aRatchetForge/spec/manifest-ratchet-spec.md:81`.** A landed spec is a
  frozen record and is cited, never edited.
- **Nothing in the charter.** `AGENTS.md:140` and `coding-governance-agents.template.md:68` state the
  MERGE-CONFLICT rule for the stamp line, which is a different rule that happens to mention the same
  two shas. They are not carriers of this one and are out of scope.

## 4. Design

### Inventory

Every carrier, located with `grep -n "merge-base <remote>/<default> HEAD\|merge-base <local-default>
HEAD\|merge-base origin/main HEAD"` over the five files at base `102e98f0`. Byte figures are
LF-normalised and were measured by reading the file in binary and slicing the span, because
`WIRE-INTO-PROJECT.md` and `MANIFEST-TEMPLATE.md` sit CRLF in this Windows working tree while their
committed blobs are LF.

| # | Carrier | Spelling | Bytes | Disposition |
|---|---|---|---|---|
| 1 | `skills/session-kickoff/MANIFEST-TEMPLATE.md:29-31` | full | 234 | the PROSE home, unchanged |
| 2 | `skills/session-kickoff/MANIFEST-TEMPLATE.md:121-124` | full | 135 | cut to the pointer already there |
| 3 | `skills/session-kickoff/SKILL.md:118-119` | full | 180 | cut to a pointer, 83 B replacement |
| 4 | `WIRE-INTO-PROJECT.md:437-439` | full | 135 | cut to a pointer, 29 B replacement |
| 5 | `skills/session-kickoff/manifest-check.sh:265` | SHORT | 100 | the MACHINE home, repaired to 151 B |
| 6 | `skills/session-kickoff/manifest-check.sh:197` | SHORT | 83 | interpolates the constant, 17 B |
| 7 | `memory/guides/SESSION-KICKOFF.md:22` | concretised | 104 | out of scope, see §3 |

**The census undercounted, and its line numbers have moved.** It found four copies in three files.
There are seven in five, and three of the four it named are off by one to two lines. Carriers 5 and 6
are the ones it missed, and they are the interesting ones: the checker already half-owns this rule in
a variable literally named `STAMP_SHA_RULE`, and its spelling omits the no-remote fallback that all
four doc copies carry. The drift the census predicted has already happened, in the file that grades
the contract.

**The census also over-estimated the recovery.** Its cut 4 read "Est. 250-400 B in the kickoff
engine". Measured, the whole duplicated clause in `SKILL.md` is 180 B gross and the pointer costs
83 B, so the net is **97 B**. My measurement wins and the unit's case shifts accordingly: this is a
drift fix that happens to recover bytes, not a byte recovery.

**And the byte half of the case is smaller still once the build's own order is honoured.** At base
`102e98f0`, `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` reports
`18225 / 18432 bytes (207 under, 98.9%)`, against which 97 B would be a 47% rise in free space. But
`TOOL-aHonedRuleset-3` is `order 1`, edits the same `skills/session-kickoff/SKILL.md`, and its own
AC binds it to leave the file at least 1200 B under 18432 — its estimate is a 1237 B recovery,
landing near 16988. So by the time this unit runs the free space is near 1444 B rather than 207, and
97 B is roughly a 7% rise, not 47%. Nothing in this unit's scope changes; the argument for it is the
drift, and the bytes are a rounding error a predecessor already banked.

### Why the floor is two homes rather than one

Three candidate single homes were tested against the tree, not assumed.

**The checker alone cannot be it.** `WIRE-INTO-PROJECT.md` §4 step 2 fills `{{AUDIT_SHA}}`, and step
4 is what copies `manifest-check.sh` into the target. At the one moment the rule is first needed the
checker is not yet in the adopter's tree, so a home reachable only by running it is unreachable
exactly when it matters. A verb would not help; the script is absent.

**The template alone cannot be it either.** A failure message must be self-contained. When check 2
reds because the audit block is missing, or check 3 reds because the stamp is foreign, the manifest
is the thing that is wrong — telling the reader to consult it is worthless. That is why
`STAMP_SHA_RULE` is interpolated into four failure messages today, and why it stays.

**A seal is not available.** Check 10 byte-compares the manifest's `kickoff:task` region against
`TASK_SKELETON`, and the checker's header at lines 40-42 states why that constant lives in the script
and not the template: "the template is a SEED that BECOMES the manifest, so an adopting tree has no
reference copy left to compare against." The same is true here, and worse — instantiation SUBSTITUTES
`<remote>/<default>`, so an adopter's correct manifest is guaranteed not to match the constant
byte-for-byte. Carrier 7 is the live proof.

So the answer is one prose home and one machine home, in the same directory, with a gate holding them
equal in the gov repo where every future edit is made. The adopter's instantiated copy is downstream
of the prose home and the checker's failure message is the backstop when that copy is broken.

**Which of the two `MANIFEST-TEMPLATE.md` copies survives is carrier 1, decisively.** Carrier 2 sits
inside the "Customize before use" block that `WIRE-INTO-PROJECT.md` step 3 orders deleted at
scaffolding, so it does not exist in any adopting tree. Carrier 1 sits in the ratchet section, which
survives instantiation and is the copy every re-stamp reads. Carrier 1 also carries two facts carrier
2 lacks: why a branch sha is refused, and that the datetime always advances. Carrier 2's one unique
fact is the unborn-branch clause, which is scaffolding-time advice, is kept verbatim, and is backed
at runtime by check 3's own message.

### The parity rows

`tools/check-playbook-parity.sh` S2 already holds five rows of the shape
`<label>~<stated-file>~<stated-extraction>~<owning-file>~<owning-extraction>`, with the anti-vacuity
arm that reds when either extraction matches nothing. Two rows join it, one per git command:

| label | stated side | owning side |
|---|---|---|
| `stamp rule remote form` | `MANIFEST-TEMPLATE.md` line 29 | `manifest-check.sh` `STAMP_SHA_RULE` |
| `stamp rule no-remote fallback` | `MANIFEST-TEMPLATE.md` line 30 | `manifest-check.sh` `STAMP_SHA_RULE` |

Each extraction captures one backticked or `$(…)`-wrapped `git merge-base …` invocation and the loop
already strips whitespace, so neither side's line wrapping matters and `head -1` is not a problem.
Splitting into two rows rather than comparing the whole sentence is what keeps every extraction
single-line, and it is also what makes the failure message name WHICH clause drifted.

**What these two rows do not check**, stated because a structural check reads as a semantic one to
everyone who did not write it: they compare two `git merge-base` invocations. They do not grade the
surrounding prose, they do not grade an adopter's instantiated manifest, and they cannot — see the
seal argument above. That sentence goes in the gate's header beside its existing "WHAT IT DOES NOT
DO" paragraph.

### Files touched (estimate)

| File | Change |
|---|---|
| `skills/session-kickoff/MANIFEST-TEMPLATE.md` | S2 — delete the parenthetical at 121-124 |
| `skills/session-kickoff/SKILL.md` | S3 — the Step 2b pointer |
| `WIRE-INTO-PROJECT.md` | S4 — the step 2 pointer |
| `skills/session-kickoff/manifest-check.sh` | S5, S6 — hoist and repair the constant, interpolate it |
| `tools/check-playbook-parity.sh` | S7 — two `PAIRS` rows and two header lines |
| `memory/guides/SESSION-KICKOFF.md` | S8 — re-verify §B, re-stamp `last-audit` |
| `memory/map/features/session-kickoff.md` | dossier prose refreshed on touch; no claim key moves |

No new file, no new gate leg, no inventory key. `tools/gate-legs.json` is not edited, which is why
`memory/map/generated/inventories.json` does not move either.

### Couplings checked and clear

- `skills/session-kickoff/manifest-check.test.sh:617` seeds a fixture from the real template, but it
  compares only the `kickoff:task` region. The ratchet block is not in that comparison.
- `tools/govkit/fixtures/incms-2cff5855.receipt.json` records a `gov_oid` for the template that
  currently equals the live blob. `govkit.py:2924` compares it against gov's blob AT THE RECEIPT'S
  RECORDED COMMIT, not at HEAD, so editing the template does not red it.
- `tools/check-wiring.sh:778` cksum-compares the junction-installed engine against the tracked one
  and will report `UNWIRED` while this branch is unmerged. It is not a gate leg — only the per-kit
  adopters and its own selftest are — so it blocks nothing. Named so the next session does not
  re-derive it.
- `tools/line-length-limits.txt` declares no row for any file here and the gate's default is 450
  characters. Every line touched is under 100.

### Alternatives rejected

- **A new gate leg for the pair.** A separate script plus a `tools/gate-legs.json` row, to hold two
  data rows, when a gate with exactly this mechanism, an anti-vacuity arm and a completion sentinel
  already runs on every bar. Rejected as one more moving part.
- **Adding the arms to `manifest-check.test.sh`.** That leg is `chunk: selftests, subject: kit`, so
  it is held on the ordinary bar and needs `GATE_SELFTESTS=1`. A session editing the template would
  not run it, which is the green-by-absence class.
- **A conditional check inside `manifest-check.sh`.** It would be dark in every adopting tree, where
  the template does not exist, and would owe an announced skip on every adopter run. The checker is
  adopter-facing and should not carry gov-only logic.
- **Cutting `WIRE-INTO-PROJECT.md`'s copy for the bytes.** The file is 69030 B with no ceiling
  anywhere, so the 105 B is worth nothing. It is cut because it is a fourth prose spelling with no
  gate on it, and because the step already points at the template two clauses earlier.

## 5. Production-readiness checklist

- security — N/A. No write path, no input boundary, no new execution.
- perf / scale — N/A. Two `sed` extractions inside a gate whose declared ceiling is 560 s.
- a11y — N/A. No interface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — the parity rows inherit S2's anti-vacuity arm, so an extraction
  that matches nothing reds by name rather than passing by finding nothing.
- observability — the failure names the label and prints both sides, per the existing `PAIRFAIL`
  format.
- risks — the one real risk is a pointer whose target an adopter has deleted. Carrier 1 sits in a
  section `WIRE-INTO-PROJECT.md` never tells anyone to delete, and the checker's failure messages are
  the backstop when the manifest itself is broken.
- testing + left-shift gates — the two `PAIRS` rows ARE the left shift. Their failing case is staged
  and observed before the unit lands, per AC4.
- migration / rollback — none. Prose edits and one shell constant, revertable as one commit.
- user docs — `WIRE-INTO-PROJECT.md` is the adopter runbook and is edited by S4. No `help/` page.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'merge-base <remote>/<default> HEAD' skills/session-kickoff/SKILL.md
  skills/session-kickoff/MANIFEST-TEMPLATE.md WIRE-INTO-PROJECT.md` runs, the only hit is
  `MANIFEST-TEMPLATE.md:29`.
- **AC2** — `wc -c skills/session-kickoff/SKILL.md` is taken immediately BEFORE this unit's first
  edit and again after the commit; the second figure is at least 90 bytes smaller than the first.
  Stated as a DELTA and not as an absolute against 18432, because `TOOL-aHonedRuleset-3` is `order 1`
  and edits the same file: an absolute threshold is satisfied by that unit alone and never observes
  this unit's 97 B. Separately, `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md`
  emits no `TEMPLATE-SIZE WARN` line — which holds under EITHER branch of §8 F1, since the file is
  already below 18215 once unit 3 lands, and a row bumped down records the post-unit measurement
  rather than a figure the file exceeds.
- **AC3** — When `grep -c 'STAMP_SHA_RULE=' skills/session-kickoff/manifest-check.sh` runs it returns
  `1`, and `grep -n 'STAMP_SHA_RULE' skills/session-kickoff/manifest-check.sh` shows the assignment
  above the `RETROFIT=` line with `RETROFIT` interpolating it.
- **AC4** — When the `git merge-base <local-default> HEAD` clause in
  `skills/session-kickoff/MANIFEST-TEMPLATE.md:30` is staged with one word changed, `bash
  tools/check-playbook-parity.sh` exits 1 and its output names `stamp rule no-remote fallback`; the
  break is then unstaged. The remote-form row gets the same treatment against line 29.
- **AC5** — When `bash tools/check-playbook-parity.sh` runs on the unmodified tree, it exits 0 and
  prints the `pairs in agreement` line.
- **AC6** — When `grep -c 'no longer playbook-only' tools/check-playbook-parity.sh` runs it returns
  `1`, and `grep -c 'compare two git merge-base invocations' tools/check-playbook-parity.sh` returns
  `1`. Both return 0 at base `102e98f0`, measured, so this observes S7's two header lines — which
  AC4 and AC5 do not reach, since those grade the two `PAIRS` rows only.
- **AC7** — When `bash skills/session-kickoff/manifest-check.test.sh` runs it exits 0, so the
  constant's repair and hoist broke no fixture and the shipped-seed arm still passes.
- **AC8** — When `bash skills/session-kickoff/manifest-check.sh` runs after the commit, it exits 0,
  proving the `last-audit` re-stamp owed by the two watched pathspecs landed with the change.
- **AC9** — When `bash tools/run-gates/run-gates.sh` runs at the push boundary it is green, with the
  `playbook parity`, `kickoff-manifest ratchet` and `kickoff engine size <=18KiB` legs all reported.

## 7. Gates

- `playbook parity` — `bash tools/check-playbook-parity.sh`. The leg this unit extends. `subject:
  repo`, unguarded, so it runs on every bar.
- `kickoff engine size <=18KiB` — `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md`.
- `kickoff-manifest ratchet` — `bash skills/session-kickoff/manifest-check.sh`. Owed because two
  watched pathspecs are edited.
- `manifest-check self-test` — `bash skills/session-kickoff/manifest-check.test.sh`. Guarded on
  `skills/session-kickoff/`, `chunk: selftests`, so it needs `GATE_SELFTESTS=1` and this unit's DoD
  owes that run because it edits the kit.
- `playbook parity selftest` — `bash tools/check-playbook-parity.test.sh`. Same guard shape; the new
  rows use the already-covered check 7 arm, and AC4 supplies the row-level failing case.
- `line length`, `memory hygiene` and the rest of the bar — no new leg is added.

## 8. Open questions

- **F1 — does the high-water record move down?** `tools/template-size-highwater.txt:3` holds
  `skills/session-kickoff/SKILL.md 18215`, and at base `102e98f0` the gate WARNs
  `18215 -> 18225 (+10)`. **That WARN is not this unit's to clear.** `TOOL-aHonedRuleset-3` is
  `order 1` on the same file and lands it near 16988, below the mark, so the WARN is already gone
  before S3 runs; S3 then takes it near 16891. The question this fork settles is therefore not "does
  the WARN clear" but "does the recorded mark follow the file down", and it is asked HERE because
  unit 5 is the LAST unit in this build to touch that file — a `--bump` taken at order 1 records a
  figure order 2 immediately supersedes. `--bump` writes the current measurement unconditionally, so
  it can lower as well as raise.
  **Recommendation: bump it down in the same commit, to the post-S3 measurement.** The ratchet exists
  to price growth against the last deliberate measurement, and leaving 18215 standing quietly hands
  back roughly 1324 B of headroom this build just bought — most of it unit 3's, which is the reason
  to record it rather than let it evaporate. It is a merge-bar knob either way, so the owner rules.
  UNRESOLVED, unsigned.
- **F2 — do the two rows belong in `check-playbook-parity.sh`?** Its header says "the playbook's
  claims about THIS repo" and S2 is described as "a value the playbook STATES". A row whose stated
  side is `MANIFEST-TEMPLATE.md` widens that subject, and the leg is named `playbook parity`.
  **Recommendation: take the rows and widen the header, do not rename the leg.** The mechanism is
  general, the cost is two data rows against a whole new script, and a leg rename touches
  `tools/gate-legs.json` and the timing cache keyed by leg name for no reader benefit. If the owner
  prefers the narrow reading, the fallback is a `stamp-rule parity` leg of its own, which is the
  rejected alternative in §4 and costs a file.
- **F3 — should this unit also fix what the rule SAYS?** `KICK-cSettledDocket-1` is OPEN and records
  that stamping the merge-base fails the checker's own check 5 on a feature branch, at a cost of
  three attempts. The rule is about to have one home, so fixing it here would be cheap.
  **Recommendation: no.** One mechanism per unit, and a byte-parity gate landed in the same commit as
  a semantic change to the text it grades cannot be shown to have caught anything. Land this, then
  file the fix against the single home.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Carrier census re-run against source at base `102e98f0`; found
  seven carriers rather than the four the prose census reported, corrected three of its four line
  numbers, and measured the `SKILL.md` recovery at 97 B net against its 250-400 B estimate.
- rev-2 · 2026-09-04 · folded the spec audit
  ([2026-09-04-review-TOOL-aHonedRuleset-1-spec-audit.md](../reviews/2026-09-04-review-TOOL-aHonedRuleset-1-spec-audit.md)),
  four findings addressed to this unit. **A2** — AC2 was an absolute against 18432 that
  `TOOL-aHonedRuleset-3` satisfies alone at `order 1`; it is now a ≥90 B delta against a `wc -c`
  taken immediately before this unit, and its no-WARN clause is restated to hold under either branch
  of §8 F1. **P6** — §4's headroom case and F1's arithmetic were both computed at base and ignored
  that unit 3 lands first: the free space this unit inherits is near 1444 B, not 207, so 97 B is a 7%
  rise rather than 47%, and F1's `18128` became `16891` with unit 3 named as the mover. **P7** — S7's
  two header lines had no criterion; they now carry pinned anchors and new AC6 greps both, which
  renumbered the old AC6-AC8 to AC7-AC9. **P3** — §7's `memory-tree hygiene` corrected to the leg
  `tools/gate-legs.json:1021` actually declares, `memory hygiene`.
  Re-measured at source rather than taken from the report: `SKILL.md` 18225 B, the high-water row
  18215, unit 3's recovery estimate 1237 B against its own ≥1200 B floor, and both AC6 anchor strings
  at 0 occurrences in `tools/check-playbook-parity.sh`. Every §8 fork stays UNRESOLVED and unsigned.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "one rule stated in several documents with the source that
owns it"` ranked `kit-dogfood-parity.PAIRS [build-method]` and `check-playbook-parity.sh [playbook]`
among its affordance-seam hits. That is the seam this unit extends: `tools/check-playbook-parity.sh`
S2 holds a declared `PAIRS` list of exactly this shape, with an anti-vacuity arm and a completion
sentinel already built, and its in-script comment records that the list is in-script rather than a
data file because it "reuses the seam kit-dogfood-parity.PAIRS already establishes". Two rows join it
and no new mechanism is built. The probe also surfaced
`manifest-check.sh [session-kickoff]` as a seam, which is the second half of the answer: that script
already owns `MANIFEST_LOCATIONS` and `TASK_SKELETON` as single homes for values that used to be
spelled across several files, and `STAMP_SHA_RULE` is the third instance of the same pattern in the
same file.

Recall terms used: `python tools/memory-recall/query.py "why does the last-audit stamp sha rule live
where it does, and what decided the kickoff kit's single-home pattern" --terms "last-audit stamp rule
merge-base manifest-check MANIFEST-TEMPLATE single source kickoff engine restatement drift playbook
parity PAIRS"`. Thirty-six hits; the two that changed this design are `KICK-cSettledDocket-1` in
`memory/backlog/KICK.md:4`, which put the rule's own correctness out of scope in §3, and
`memory/guides/SESSION-KICKOFF.md:16`, which is how the seventh carrier was found.
