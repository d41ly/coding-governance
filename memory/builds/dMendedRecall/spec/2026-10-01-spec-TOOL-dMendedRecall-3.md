# TOOL-dMendedRecall-3 — the verb contract's `--status` entry names every field the line prints, the pinned-asks and holder-worktree verdicts among them

**Status:** SPECCED · rev-1 · 2026-10-01 · node d · Tier-2 · base 1f915870 · streams tooling · order 1 · closes TOOL-dAlignedCarrier-7 · ratified 2026-10-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-prompt-TOOL-dMendedRecall-1-build-brief.md](../prompts/2026-10-01-prompt-TOOL-dMendedRecall-1-build-brief.md) | journal | TOOL-dMendedRecall-1 TOOL-dMendedRecall-2 |
| [2026-10-01-prompt-TOOL-dMendedRecall-1-spec-brief.md](../prompts/2026-10-01-prompt-TOOL-dMendedRecall-1-spec-brief.md) | journal | TOOL-dMendedRecall-1 TOOL-dMendedRecall-2 |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-dAlignedCarrier-4 added two fields to `--status`'s one line, the pinned-asks verdict and the
holder-worktree verdict, and the `--status` entry of the verb contract does not name them. Unlike
the optional fields the entry does name, these two print on a PASS, so the entry's rule that the
optional fields print only when there is something to report is no longer the line's rule either.
This unit makes the entry describe the line `verb_status` actually prints, field by field and in
order, and re-copies the render.

## 2. Scope (IN)

- **S1** — The `--status` entry of `tools/unattended/VERBS.template.md` names the pinned-asks field
  in both its spellings, and says it prints on every record that pins `asks`, a pass included,
  because `--resume` runs check 73 above every row of its matrix. Observed by AC1, AC2.
- **S2** — The entry names the holder-worktree field in its three spellings, and says it prints when
  the record carries `lease-utc`, its phase is not terminal and it is not a LANDING the landed log
  observed, which are the records on which `--resume` reaches check 58, a pass included. Observed
  by AC1, AC2.
- **S3** — The entry accounts for the whole line in the order it prints, per §4's field table: the
  fields every line carries, then each optional field with the condition that prints it, the two
  verdicts before the keepalive field, which stays last. The sentence that every optional field
  prints only when there is something to report is reworded so it holds for every field it covers,
  and the closing promise that the line stays ONE line is kept. Observed by AC3, AC4.
- **S4** — The render, `memory/guides/UNATTENDED-VERBS.md`, is re-copied in the same pass by
  `bash tools/unattended/adopt-unattended.sh` and is byte-identical to the template. Observed by
  AC5.
- **S5** — The `unattended kit gate` leg reads green, the second half of the ask's accept clause.
  Observed by AC6.

## 3. Non-goals (OUT)

- `verb_status` itself. The driver's line is the subject being described; no field, spelling or
  order of it changes here.
- Any other verb's entry, and any other carrier: the protocol, the stop contract and the Skill
  stay as they are. The accept clause names this carrier and its render only.
- A gate joining the fields `verb_status` appends to the fields this entry names. It would close
  the class this ask is an instance of, and it is a separate mechanism with its own unit.
- The unattended kit version. The orchestrator moves it once, at VERIFYING.

### Edges

- **hands-off** external — a check that every field `verb_status` appends is named in the verb
  contract's `--status` entry, so the next field cannot outgrow the entry unseen.
- **consumes-from** external — the close's bar, which is where AC6 reads the kit gate this pass
  may not run.

## 4. Design

### Evidence

Read at `1f915870` on 2026-10-01, PINNED to that date.

- The entry (`tools/unattended/VERBS.template.md:87-92`) names the phase, the first non-terminal
  unit and the parked counts, then the resume tick's attempts, `orphans <n>` and the keepalive
  field, under the rule that those print only when there is something to report.
- `verb_status` (`tools/unattended/unattended.sh:5564`) prints one `printf` line. Its optional
  fields are appended to two strings: the halt-code and spec-audit facts ride before `next`, and
  every other optional field rides after it. The two verdicts sit at `:5680-5694`, before the
  keepalive block, whose comment calls it the LAST suffix.
- The live line of this build's own run, read with `bash tools/unattended/unattended.sh --status
  dMendedRecall` on 2026-10-01: `phase SPECCING · witness <sha> · next (no non-terminal unit) ·
  noted 3 · asks as pinned · worktree holds the run · keepalive <id> present in the harness listing
  at <utc>`. Both verdicts print, on a pass, which is exactly what the entry's rule says no
  optional field does.
- The template and the render are byte-identical at BASE (`cmp` exits 0). The adopter copies the
  template rather than rendering it, and the kit gate's check 10 byte-compares the pair.
- The carrier has no byte cap of its own: no size leg names it.

### Fields

The order is the printed order. "Always" fields carry no condition.

| Field | Spelling | Prints when |
|---|---|---|
| phase | `phase <phase>`; a derived LANDED reads `LANDED (derived: <sha8> on <ref> at <tip8>)`, and a LANDING the derivation explains reads `LANDING (not on the remote: <reason>)` | always |
| witness | `witness <sha>`, or `witness NONE` | always |
| halt code | `halt-code <code>` | the record carries `halt-code` |
| spec audit | `spec-audit <date>` | the record pins `spec-audit` |
| next | `next <unit>`, or `next (no non-terminal unit)` | always |
| parked | `parked <n>` | owed parked rows exist |
| noted | `noted <n>` | rows the owner is told of but owes no answer to exist |
| briefs | `STALE briefs <n>` and `briefs gone <n>` | a unit's latest recorded brief no longer hashes the same, or its file is gone |
| resume tick | `resume-tick <n> attempt(s), last <stamp>` | the tick's sidecar for this slug holds a line |
| orphans | `orphans <n>` | the process ledger names an orphan; nothing is killed |
| asks | `asks as pinned`, or `asks moved at HEAD, check 73 refuses a resume: pinned [<pin>] at HEAD [<now>]` | the record pins `asks` |
| worktree | `worktree holds the run`, `worktree not the run's, check 58 refuses a resume here: <where>`, or `worktree unanswerable, the record names no run branch` | the record carries `lease-utc`, its phase is not terminal, and it is not a LANDING the landed log observed |
| keepalive | `keepalive <id> present\|absent in the harness listing at <utc>` | the record names a keepalive id and the stop-guard's sidecar holds a line, whatever its phase |

The entry is prose, as every entry of the carrier is; the table is the content it must carry, not
a table to paste. Every field is joined to the line by ` · `, and the entry says so once.

### Rollout

`bash tools/unattended/adopt-unattended.sh`, run in the same pass after the template edit, re-copies
`memory/guides/UNATTENDED-VERBS.md` and re-renders the Skill and the other copied carriers. A
re-render that changes any file but the verb pair is a finding the pass names in its ledger.

### Files touched (estimate)

`tools/unattended/VERBS.template.md` · `memory/guides/UNATTENDED-VERBS.md`

### Alternatives rejected

- **Name only the two new fields.** It satisfies the accept clause and leaves the entry wrong about
  six fields it already omits, and wrong about its own rule, since the two new fields print on a
  pass. §8 F1.
- **Paste the field table into the carrier.** The carrier's entries are prose bullets, and a table
  inside one bullet would be the only one in the file.

## 5. Production-readiness checklist

- security — N/A: a documentation carrier and its byte copy; no code path changes.
- perf / scale — N/A: no runtime change.
- error / empty / loading states — N/A: the entry describes the line's optional fields, which is
  the line's own empty-state behaviour.
- observability — the entry is how a reader learns what the status line reports; it now reports
  all of it.
- risks — a reader of the old entry learned that every optional field means trouble; the reworded
  rule says the two verdicts print on a pass. A spelling copied wrongly would teach a field the
  verb never prints, which AC3 grades against the driver.
- testing — the greps and the live reading of AC1 to AC5; the kit gate at the close.
- migration — none.
- user docs — this unit IS the user doc for the line.

## 6. Acceptance criteria

- **AC1** — When `grep -c -F 'asks as pinned' tools/unattended/VERBS.template.md` runs, and the same
  count is taken for `asks moved at HEAD`, `worktree holds the run`, `worktree not the run`, and
  `worktree unanswerable`, each prints at least 1, where BASE prints 0 for every one of them.
  Red when: either verdict, or any one of its spellings, is unnamed.
- **AC2** — When `awk '/^- .--status. /,/^- .--audit. /' tools/unattended/VERBS.template.md` cuts
  the entry, the cut carries `check 73`, `check 58` and `lease-utc`, and carries the word `pass` in
  the sentence that says when the two verdicts print.
  Red when: a verdict is named without the condition that prints it.
- **AC3** — When the build pass greps `tools/unattended/unattended.sh` with `grep -c -F` for every
  literal fragment of every spelling the entry now names, a fragment being the text between two
  placeholders, such as `(no non-terminal unit)`, `attempt(s), last`, `in the harness listing at`
  and `check 73 refuses a resume: pinned [`, every count is at least 1. The pass lists each
  fragment and its count in its ledger.
  Red when: the entry names a field, or a spelling, that the driver does not print.
- **AC4** — When `bash tools/unattended/unattended.sh --status dMendedRecall` runs in the run's own
  worktree during the build, every field head its one line carries is named in AC2's cut, and in
  the same relative order, `asks as pinned` before `worktree holds the run` and both before
  `keepalive`.
  Red when: the live line carries a field the entry omits, or the entry orders them otherwise.
  fixture: this build's own run-state file, which pins `asks` and carries `lease-utc` today.
- **AC5** — When `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` runs it
  exits 0, and `git diff --stat` after the re-render names no other changed file under
  `memory/guides/` or `.claude/skills/unattended/`.
  Red when: the render differs from the template, or the re-render moved a carrier this unit did
  not edit.
- **AC6** — When the close's bar runs, the `unattended kit gate` and `unattended skill wiring` legs
  read green, as their rows in the bar's summary and their persisted `unattended_kit_gate.log` and
  `unattended_skill_wiring.log` show.
  Red when: either leg is red, check 10's byte compare of the verb pair above all.
  permission: units run no gate leg, by the owner's rule; this criterion is observed at the close,
  not in the pass.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `dead-path carriers (deleted files still named)` · `recall floor` · `recall floor arms`

No arm is added or moved; the carrier's checks are the kit gate's existing check 10 and check 26.

## 8. Open questions

- **F1 — Does the entry name only the two new fields, or the whole line?** (a) The two fields the
  ask names, appended beside the three optional fields the entry already lists. (b) Every field
  the line prints, in order, with the condition for each. (a) meets the accept clause and leaves
  six fields unnamed, and the entry's rule about optional fields false for the two it adds; the
  next field outgrows it the same way. (b) meets the accept clause, and leaves the entry true of
  the line as it prints at BASE. Neither trips a veto: the carrier is named by the accept clause, so
  M3's veto 2 does not reach it, and no criterion or non-goal excludes either. Recommendation (b).
  RESOLVED (agent, 2026-10-01, delegated): (b), the more feature-rich survivor with the fewer
  follow-ups, M3's rule.

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft, from the ask's accept clause, the build's spec brief,
  `verb_status` read at BASE, and this run's own live status line.

## 10. Reuse audit

The probe, run on 2026-10-01:

```
python tools/codebase-map/reuse_lookup.py "the verb contract entry that enumerates the fields of the status line"
```

It ranked `leading_verb`, `parse_line` and `render_status_row` as name-stem neighbours, none of
them about this carrier, and reported `.sh` as an unscanned layer. No existing seam fits a prose
entry in a copied carrier; what is reused is the copy step the kit already has,
`tools/unattended/adopt-unattended.sh`, and the spellings themselves, which are read from
`verb_status` rather than written fresh. The recall probe returned the ask, TOOL-dAlignedCarrier-4's
spec, whose §4 "Fields" lists the two verdicts' spellings and conditions, and its acceptance
ledger; the conditions above agree with that spec and with the driver at BASE.

Recall terms used: VERBS.template.md UNATTENDED-VERBS --status one line fields keepalive orphans resume-tick asks-as-pinned holder-worktree check-73 check-58 verb_status

The question passed with them: "what does the verb contract say --status prints, and which fields
did the holder worktree and pinned asks add".
