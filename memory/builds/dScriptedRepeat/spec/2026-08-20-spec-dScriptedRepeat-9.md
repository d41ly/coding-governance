# TOOL-dScriptedRepeat-9 — the `proposal` park kind and the `--propose` verb

**Status:** SPECCED · rev-2 · 2026-08-20 · node d · Tier-1 · base d2a40aa8 · streams tooling · ratified 2026-08-20

## 1. Goal

Give a run a place to log an improvement it discovered while a playbook was working — the owner-facing
half of the mode's second verb — as a fifth `park()` KIND rather than a second register.

## 2. Scope (IN)

- **S1.** A fifth parked kind, `proposal`, written by a new `--propose <slug> --item <what> --reason
  <why>` verb that reuses `verb_park`'s guards wholesale.
- **S2.** One extra field the other kinds do not carry: the STEP the proposal amends, so a proposal is
  joined to the playbook step it came from rather than being free-floating advice. Its PLACEMENT is
  `... · item <i> · step <s> · reason <r>`, keeping `reason` LINE-FINAL, because every existing reader
  depends on that - `waivers_of` at `unattended.sh:654`, and check 17's trailing-strip at
  `check-unattended.sh:503`. Appending after `reason` makes the step part of every reader's greedy
  match. The ` · ` separator refusal, which screens the item only today because `reason` could not
  previously be mis-parsed, EXTENDS to the step.
- **S3.** The alternation in `verb_status`'s parked-kind regex at `unattended.sh:1566`, which today
  carries exactly four kinds.
- **S4.** The row in protocol §2, which today states four kinds.
- **S5.** NO DoD item, and no effect on the close. `parked-decisions-surfaced` surfaces every parked
  kind through one key, and a proposal must not block. That key is agent-ATTESTED, not derived:
  `DOD_CORE` spells it `parked-decisions-surfaced:agent` at `unattended.sh:93`, and `dod_met` grades it
  by grepping for a line the run itself writes via `--attest` at `:1879-1880`. Under protocol §9 a
  self-written line is exactly what does not constitute evidence, so fork 6's "surfaced at close" rests
  on an attestation. Stated plainly rather than dressed up as a derivation.
- **S5b.** TWO REUSE LIMITS, named because S1 calls the guards reused "wholesale" and two of them do
  not travel. `verb_park` REFUSES with no run-state file at `unattended.sh:1940`, so `--propose` is
  unattended-only and the attended path has no proposal channel - the same asymmetry unit 5 solved by
  giving its writer a second caller, and the same solution applies. And the STEP field is a row GRAMMAR
  change, so the parked-region parsers in the leg and in `verb_status` are in-scope readers.
- **S6.** The verb-set carriers. The research found the verb set spelled in FIVE places with three
  already stale — the header docstring, `fail 14`'s message and protocol §7 each name fewer verbs than
  the dispatch handles. Adding a verb without fixing that ships a sixth stale copy, so this unit
  derives the list or fixes all carriers in one commit.
- **S7.** Arms: a proposal is recorded and idempotent on re-issue; a proposal does not block `--close`;
  a proposal with no step is refused; `verb_status` lists it.

## 3. Non-goals (OUT)

- No separate register file. §4 gives the reasoning and records the residual tension with the fork's
  own wording.
- The verb does not EDIT the playbook. A run that rewrites the checklist it is judged by has no rules;
  the precedent run refused exactly this and parked it instead.
- No proposal triage, ranking or auto-application.

## 4. Design

### The fork's premise was wrong and its ruling survives

Fork 6 was ruled on the framing that a park blocks the close and a proposal must not. Measured: it does
not. `park()` already writes four kinds into one region; `parked-decisions-surfaced` is satisfied by a
single derived `parked-surfaced:` line that neither distinguishes kinds nor blocks per entry; and what
actually demands the two agent items is `--abort`'s hard-coded list and `--close`'s DoD loop, neither
of which looks at whether parks are outstanding. **The asymmetry the fork asked for already holds.**

So the ruling's INTENT — proposals are distinct from blockers and must read that way — is satisfied by
a KIND, which is already the discriminator the protocol uses, at roughly a tenth of the cost of a
register. What the SURFACING rests on is a separate question, and the answer is weaker than the
previous revision claimed: it is an attestation, per S5.

**The residual tension, recorded rather than smoothed over.** The fork's words were "distinct region",
and a fifth kind is the same region with a different first token. If the owner meant region literally,
this unit is wrong and the alternative costs a new file outside the run-state file — which lands
outside unit 8's exemption set and needs adding there. Flagged in §8.

### The 8 KB spill is a prerequisite, not a follow-up

`TOOL-aBoundedVerdict-6` is OPEN: the run-state file's authored region has an 8 KB cap, and it becomes
load-bearing the moment parking is cheap. A run emitting proposals across N pieces makes crossing it
likely, and crossing it mid-run reds the bar and blocks `--close` with nobody to interpret it. Only one
research lens priced this. It is named here so the build does not discover it at piece forty.

## 5. Production-readiness checklist

- security — a proposal is free text the run writes. `verb_park`'s existing guards are reused unchanged
  and they are the security-relevant part: the newline refusal, the separator refusal, and the
  bypass-flag refusal over BOTH the item and the reason. Each exists because of a recorded defect.
- perf / scale — one appended line per proposal, bounded by the 8 KB cap above.
- a11y — N/A. i18n — free text, unconstrained.
- error / empty / loading states — a proposal with no step, no item or no reason is three distinct
  refusals; re-issuing an identical proposal is an exact-line no-op, reusing the compare `verb_park`
  already had to fix once when a prefix match silently dropped distinct decisions.
- observability — `verb_status` lists proposals separately from decisions.
- risks — the spill. See §4.
- testing + left-shift gates — S7, plus an arm asserting a proposal does NOT block the close, which is
  the property the whole unit rests on.
- migration / rollback — additive; existing records parse unchanged.
- user docs — protocol §2's kind row and the Skill's verb table.

## 6. Acceptance criteria

- **AC1** — When `--propose` is called with a slug, item, step and reason, a `proposal` row is appended
  to the run-state file's parked region and staged.
- **AC2** — When the same proposal is re-issued verbatim, `--propose` no-ops and says so, verified against an
  EXACT line compare rather than a prefix match.
- **AC3** — When a run holds proposals and no parked decisions, `--close` does not block on them.
  Observed, because this is the fork's actual requirement.
- **AC4** — When `--propose` omits the step, the driver REFUSES.
- **AC5** — When `bash tools/unattended/unattended.sh --status <slug>` runs, proposals are listed and
  are visually distinct from decisions.
- **AC6** — When the verb set is grepped after this unit lands, every carrier names the same set,
  derived or fixed in one commit: the header docstring, `fail 14`, protocol §7, the dispatch, and the
  Skill. Three of these are stale TODAY, which is why this is an acceptance criterion.

## 7. Gates

`bash tools/unattended/check-unattended.sh` · `bash tools/unattended/unattended.test.sh` ·
`bash tools/unattended/check-unattended.test.sh` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

- **F1 — did "distinct region" mean a distinct FILE?** Recommendation: no — a kind satisfies the
  intent, costs a tenth as much, and keeps proposals inside the file the wrap-up already derives from.
  **Owner decision if the literal reading was meant**; otherwise this is settled by §4.
- **F2 — must `TOOL-aBoundedVerdict-6` close first?** Recommendation: yes, and it is small. Building
  proposals on a region that can overflow mid-run means discovering the cap at the worst moment. Filed
  as a prerequisite in the build plan rather than a follow-up.

## 9. Revision log

- rev-1 · 2026-08-20 · initial draft. Written after measuring `park()` and `dod_met` directly and
  finding the fork's premise false; the verb-carrier drift in S6 comes from the research.
- rev-2 · 2026-08-20 · folded the M4 spec audit. F18 pinned the STEP field's placement before `reason`
  and extended the separator refusal to it - `park()` is ONE format string and every reader depends on
  `reason` being line-final, so the field's position is a correctness property rather than a style
  choice. F19 corrected S5 and §4: `parked-decisions-surfaced` is agent-attested, not derived, and the
  two reuse limits are named in S5b instead of being implied away by the word wholesale.

## 10. Reuse audit

`verb_park` is the seam and it is reused in full rather than copied: the same three refusals, the same
newline and separator guards, the same exact-line idempotence, the same `stage_or_fail`. Every one of
those exists because of a recorded defect — a reason containing a newline forged a second row, an item
spelling the field separator made its own record unparseable, a prefix match dropped distinct
decisions, and screening only the reason left an item free to red the bar permanently. Reusing the
repaired verb rather than writing a sibling is the entire correctness argument for this unit being
Tier 1. `park()`'s KIND argument already exists and takes a fifth value with no change. Recall terms
used: park kind register proposal verb refusal newline separator idempotent status parked surfaced
attested close block spill cap authored region.
