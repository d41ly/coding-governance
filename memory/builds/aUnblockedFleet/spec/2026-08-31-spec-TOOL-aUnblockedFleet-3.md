# TOOL-aUnblockedFleet-3 — the protocol and the Skill state the rule the code now runs

**Status:** CLOSED · rev-3 · 2026-08-31 · node a · Tier-1 · base 117de044 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aUnblockedFleet-1-acceptance-ledger.md](../build/2026-08-31-build-TOOL-aUnblockedFleet-1-acceptance-ledger.md) | journal | TOOL-aUnblockedFleet-1 TOOL-aUnblockedFleet-2 TOOL-aUnblockedFleet-4 TOOL-aUnblockedFleet-5 |
| [2026-08-31-review-TOOL-aUnblockedFleet-1-diff-closing.md](../reviews/2026-08-31-review-TOOL-aUnblockedFleet-1-diff-closing.md) | diff-review | TOOL-aUnblockedFleet-1 TOOL-aUnblockedFleet-2 TOOL-aUnblockedFleet-4 TOOL-aUnblockedFleet-5 TOOL-aUnblockedFleet-6 |
| [2026-08-31-review-TOOL-aUnblockedFleet-1-specs-round1.md](../reviews/2026-08-31-review-TOOL-aUnblockedFleet-1-specs-round1.md) | spec-audit | TOOL-aUnblockedFleet-1 TOOL-aUnblockedFleet-2 TOOL-aUnblockedFleet-4 TOOL-aUnblockedFleet-5 |
| [2026-08-31-review-TOOL-aUnblockedFleet-6-specs-round2.md](../reviews/2026-08-31-review-TOOL-aUnblockedFleet-6-specs-round2.md) | spec-audit | TOOL-aUnblockedFleet-1 TOOL-aUnblockedFleet-2 TOOL-aUnblockedFleet-4 TOOL-aUnblockedFleet-5 TOOL-aUnblockedFleet-6 |

<!-- /gen:spec-records -->

## 1. Goal

Two carriers state the at-most-one-live-run rule as binding. Units 1 and 2 remove it from the code.
A contract that outlives its enforcement is worse than either — it tells the next agent to expect a
refusal that no longer exists, and `TOOL-dClosedLexicon-11`'s review already recorded one agent
building to exactly that kind of phantom.

## 2. Scope (IN)

- **S1** — `tools/unattended/PROTOCOL.template.md` §3: the paragraph beginning "**At most one
  run-state file in the tree may be in a non-terminal phase.**" is replaced by the rule that
  actually binds — concurrent runs are permitted and announced, a build folder holds one live
  record, and an archived record must be terminal (leg check 4, which is what still enforces it).
- **S2** — the replacement states WHY the old rule went, in one sentence naming the measurement, so
  the next reader does not re-derive it or re-add the refusal.
- **S3** — `tools/unattended/SKILL.template.md`: the `--preflight` refusal list drops "and when a
  second run is already live". Every other refusal in that sentence stays.
- **S4** — BOTH renders are regenerated in the same commit as their templates, and the rendered
  copies are `memory/guides/UNATTENDED-PROTOCOL.md` and `.claude/skills/unattended/SKILL.md`. Leg
  check 10 byte-compares the shipped protocol against the installed one, so a template edited without
  a re-render reds — which is the gate that makes this unit's failure mode loud rather than silent.
- **S5** — the kit version bump covers EVERY carrier of the marker, and the carrier set is DERIVED
  rather than typed here. `tools/check-kit-versions.sh:159-172` asserts the marker on every tracked
  `tools/unattended/*.template.md` with no exemption, and `git ls-files` returns **three**, not the
  two rev-1 named: `PLAYBOOK-TEMPLATE.template.md` is the third, and neither it nor its render
  `memory/guides/PLAYBOOK-TEMPLATE.md` appeared in any unit of this build. Missing it reds BOTH legs
  this unit calls binding — `check-kit-versions.sh` on the unbumped marker, and
  `adopt-unattended.sh --check` on the un-rendered artifact — with no unit owning the fix and nobody
  present to read it.
- **S6** — a run does not enumerate the carriers by hand. Before bumping, it derives the set:

  ```bash
  git ls-files 'tools/unattended/*.template.md'
  grep -rln 'gov:kit unattended@' tools/unattended/ .claude/skills/unattended/ memory/guides/
  ```

  and bumps what those print. A spec that types a derived population is the "count in prose beside
  the source that owns it" class the charter's §7 forbids, and rev-1 broke it and got the count wrong
  in the same sentence. AC5 asserts the derived set resolves to exactly one version.
- **S7** — three SURVIVING in-code and in-Skill carriers of the removed contract, none of which
  rev-1's greps could see. `SKILL.template.md:706` states "every later run still counts yours as live
  and the bar reds on the second one", which unit 2 falsifies, and it sits in a file this unit edits
  while AC2 greps only line 175's string. `unattended.sh:1109-1110` states the deleted rule verbatim
  as a stranded comment about a hundred lines above `check_single_live()`, outside AC1's two paths.
  `unattended.sh:2027` justifies `refuse_if_terminal` by naming check 7 as a live counter. All three
  are corrected here; a fourth, `check-unattended.sh:716-720`, belongs to unit 2's S7 because it is
  inside the file that unit rewrites.

## 3. Non-goals (OUT)

- The repository's own `AGENTS.md` / charter template. Neither states this rule; both point at
  `memory/guides/UNATTENDED-PROTOCOL.md` rather than restating it, which is the design working.
  Verified by grep at writing time.
- Any other section of the protocol. §3's neighbouring paragraphs about terminal phases, `--phase`,
  and `LANDING` being close-only are correct and untouched.
- Rewriting the protocol's Definition-of-Done table, the phase vocabulary, or the anchor sections.

## 4. Design

The change is text in two templates plus their renders. The mechanism that makes it safe is already
built: leg check 10 fails when the shipped template and the installed render disagree, and leg check
16 asserts the installed protocol still spells the archive filename grammar. Both run on the bar.

The one judgement is what the replacement paragraph SAYS. It must not read as "the rule was
relaxed", because the rule was not relaxed — it was found to have no referent. The replacement
states three facts that are all still true and all still enforced somewhere: concurrent runs are
permitted, every verb is slug-addressed so no reader ever has to resolve "the run", and a build
folder holds at most one live record because there is one `RUN.md` and check 4 refuses a
non-terminal archived one.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/PROTOCOL.template.md` | §3's singularity paragraph replaced, and it gains one sentence naming the close-time turnstile contention as a KNOWN residual with its backlog row — owned by this unit's S1, not by the retired `TOOL-aUnblockedFleet-6` |
| `tools/unattended/SKILL.template.md` | the `--preflight` refusal clause at `:175` dropped; the false consequence at `:706` corrected (S7) |
| `tools/unattended/PLAYBOOK-TEMPLATE.template.md` | marker bump only — the third carrier rev-1 missed (S5) |
| `memory/guides/UNATTENDED-PROTOCOL.md` · `.claude/skills/unattended/SKILL.md` · `memory/guides/PLAYBOOK-TEMPLATE.md` | the three renders, regenerated by `bash tools/unattended/adopt-unattended.sh` |
| `tools/unattended/unattended.sh` | the paired `KIT_UNATTENDED_VERSION` bump, plus the two stranded carriers at `:1109-1110` and `:2027` (S7) |
| `tools/unattended/check-unattended.sh` | the paired `KIT_UNATTENDED_VERSION` bump |

## 5. Production-readiness checklist

- security — N/A, documentation of a non-security control.
- perf / scale — N/A.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — N/A, static documents.
- observability — leg checks 10 and 16 are the observability; an unrendered template reds.
- risks — `two-answers-to-one-question`, which is the class this unit exists to avoid: the code
  saying one thing and the contract another. Mitigated by landing this unit in the same commit range
  as units 1 and 2 and by check 10.
- testing + left-shift gates — no new arm. Check 10's parity gate already covers the failure mode and
  a second arm asserting prose content would be a second answer to one question.
- migration / rollback — revert.
- user docs — this unit IS the user docs.

## 6. Acceptance criteria

- **AC1** — When `grep -n "At most one run-state file" tools/unattended/PROTOCOL.template.md
  memory/guides/UNATTENDED-PROTOCOL.md` runs, it returns nothing.
- **AC2** — When `grep -n "a second run is already live" tools/unattended/SKILL.template.md
  .claude/skills/unattended/SKILL.md` runs, it returns nothing.
- **AC3** — When `bash tools/unattended/check-unattended.sh` runs, check 10 is silent, proving the
  shipped template and the installed render agree after the edit.
- **AC4** — When `bash tools/check-kit-versions.sh` runs it is green, `bash
  tools/unattended/adopt-unattended.sh --check` exits 0 over all three installed artifacts, and
  `bash tools/check-wiring.sh --check` reports the installed Skill matches tracked.
- **AC5** — When `grep -rho 'gov:kit unattended@[0-9.]*' tools/unattended/ .claude/skills/unattended/
  memory/guides/ | sort -u` runs, it prints exactly ONE line. This is S6's derived-set criterion and
  it is what makes a missed carrier fail here rather than at the bar.
- **AC6** — When `grep -rn "the bar reds on the second one\|At most one run-state file may be
  non-terminal\|returns the run to check_single_live" tools/unattended/ .claude/skills/unattended/
  memory/guides/` runs, it returns nothing. This is S7's criterion, and it is deliberately a
  CONTENT grep across the whole kit rather than a line-numbered one: rev-1's ACs greped two known
  strings at two known lines and were structurally incapable of finding the three carriers the audit
  found.

## 7. Gates

`bash tools/run-gates/run-gates.sh`, with `unattended kit gate`, `unattended skill wiring`, the
kit-version pairing leg and `drift-audit records` binding. **The landing order is unit 1 §7's** and
binds this unit for the same reason.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-08-31 · authored under the aUnblockedFleet mandate.
- rev-3 · 2026-08-31 · spec-audit round 2 fold. The protocol's turnstile sentence was cited to
  `TOOL-aUnblockedFleet-6 S6` and owned by no scope item here; that unit is now RETIRED, so the
  sentence is folded into S1 explicitly and reworded from "a bound this build sets" to "a residual
  this build documents", which is what is actually true. Order 5 -> 4.
- rev-2 · 2026-08-31 · spec-audit round 1 fold. S5 rewritten: the marker has THREE template carriers
  and rev-1 named two, so `PLAYBOOK-TEMPLATE.template.md` and its render would have redded both legs
  this unit calls binding, unowned (B2). S6 added so the set is derived rather than typed. S7 added:
  three surviving carriers of the removed rule that rev-1's line-anchored ACs could not see (H1, H2,
  H3). AC5 and AC6 replace greps that could only find what was already known. §7 gained
  `drift-audit records` (B3). Order moved 3 -> 5, behind unit 6.

## 10. Reuse audit

No seam to find — the unit edits two prose templates and re-runs an existing renderer
(`tools/unattended/adopt-unattended.sh`). The render path, the parity gate and the version pairing
are all existing machinery this unit uses rather than extends.

Recall terms are unit 1's; the record that binds this unit specifically is
`TOOL-dClosedLexicon-11`'s review finding, which recorded an agent building to a refusal that did not
exist. That is the failure mode S1 and S3 prevent in the opposite direction.

**Verified at writing time**: both carriers hold the sentences S1 and S3 name, and neither `AGENTS.md`
nor `coding-governance-agents.template.md` restates the rule — both point at the protocol instead.
