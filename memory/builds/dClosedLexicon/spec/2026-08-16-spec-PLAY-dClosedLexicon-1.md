# PLAY-dClosedLexicon-1 — §14 splits, not externalizes, and §0 gains a fallback rule

**Status:** SPECCED · rev-1 · 2026-08-16 · node d · Tier-2 · base 587b95a4 · streams playbook

## 1. Goal

`PLAY-aCandidStub-2` records that the template is effectively full and names §14 as the strongest
externalization candidate. `TOOL-dClosedLexicon-1` F1 ratified it as that unit's predecessor, and F2
ratified the §0 constitution line into this one. This unit does both, and it corrects the
externalization plan on measurement: §14 cannot go behind a §-stub whole, because it is the only
candidate section that is not activity-scoped.

## 2. Scope (IN)

- **S1** — §14 SPLITS. Its three always-on bullets stay inline; its five situational bullets move
  behind a §-stub, per §4 The split rule.
- **S2** — a §14 section in `parallel-coding-governance.domain-rules.md` holding the five moved
  bullets verbatim, with no rule reworded on the way across.
- **S3** — a fallback rule in §0 naming how to decide a case the playbook does not cover, per §4
  The §0 line.
- **S4** — the lockstep edits: the version marker to v2.8 in both shipped files, the header changelog
  gaining a v2.8 entry and dropping v2.6, the "nine domain checklists (§1, §4, §7–§13)" sentence
  becoming ten and §7–§14, and `customize.md`'s conditional-section list gaining its §14 row.
- **S5** — the byte ledger is an ACCEPTANCE artifact, not a note: the landing commit message carries
  the measured before and after, and `tools/check-template-size.sh` is green on the result.

## 3. Non-goals (OUT)

- Anything in `tools/lexicon/`. This unit is the predecessor `TOOL-dClosedLexicon-1` is parked on and
  ships no kit code.
- Externalizing §16 or §8, both measured and rejected in §4 Alternatives rejected. Their numbers are
  recorded there so the next budget pass argues from measurements rather than from impressions.
- Rewording any moved rule. A move that edits is a move nobody can diff, and the §-body diff is how
  `customize.md` tells adopters to re-pull.
- Raising the 32 KiB ceiling. `AGENTS.md` says trim or externalize, never raise, and this unit exists
  because that rule was taken seriously.

## 4. Design

### The finding that changed the plan

Every §-stub in the template today carries an ACTIVITY trigger, and the trigger is what makes the
externalization safe — the rules are absent from the session that does not need them and present in
the session that does.

| Stub | Trigger |
|---|---|
| §4 | standing up local stacks, or verifying via a harness |
| §7 | adding or changing a gate |
| §8 | writing a Workflow script |
| §9 | a unit adds or touches a write path, auth, sanitization, or egress |
| §11 | cross-OS or toolchain work |
| §12 | adding a 2nd instance of a kind, or building shared structure |
| §13 | any UI work |

§14 is per-call token discipline. It has no activity to trigger on, because its activity is every
call in every session. A stub reading "LOAD always" saves nothing — the bytes move but every session
still pays them — and a stub nobody bothers to load makes always-on rules dark. That is a worse
outcome than the crowding it was meant to fix, and it is the failure mode this repo names elsewhere
as a check that cannot fire.

The section is not homogeneous, though, which is what makes the split available.

### The split rule

A bullet stays inline if a session violates it WITHOUT undertaking any particular activity. A bullet
moves if reaching it requires doing a nameable thing.

| Bullet | Bytes | Disposition | Why |
|---|---|---|---|
| Strategy, spend tokens on new judgment | 338 | STAYS | the section's thesis; every other bullet is an instance of it |
| Don't re-fetch what's in context | 251 | STAYS | violated by an ordinary second Read, with no activity in between |
| Bound every command's output | 177 | STAYS | violated by any unbounded command |
| Re-Read only when something else changed | 276 | MOVES | reachable only while editing files |
| Don't poll background work | 185 | MOVES | reachable only with background work running |
| Lint the files you changed | 231 | MOVES | reachable only while linting |
| Pin a review base to an immutable SHA | 197 | MOVES | reachable only during a review or diff |
| A no-match `grep` exits non-zero | 178 | MOVES | reachable only while writing a check |

The stub trigger is therefore real: LOAD when editing across several passes, running background work,
linting, pinning a review base, or writing a shell check.

### The byte ledger

Every figure MEASURED at `587b95a4`, none estimated.

| Item | Bytes |
|---|---|
| Template today | 32,682 |
| Ceiling | 32,768 |
| Headroom today | 86 |
| §14 whole | 1,900 |
| §14 bullets that move | 1,067 |
| §14 stub bullet, at the §9/§12 average | ~330 |
| "nine" to "ten" in the header sentence | −1 |
| v2.8 entry added, v2.6 entry dropped | ~0 |
| §0 fallback line | 157 |
| **Net saving this unit** | **~738** |
| **Headroom after this unit** | **~667** |

`TOOL-dClosedLexicon-1` then spends roughly 69 B, leaving about 598 B — which is the first real slack
the template has had since v2.3, and the number the next playbook rule gets to argue against.

The originally ratified figure was ~1,480 B, from externalizing §14 whole. Half of that saving was
never available without darkening always-on rules. The owner ratified F1 on the larger number, and
this spec is where that correction is recorded rather than absorbed.

### The §0 line

Drafted and measured at 157 B against the 120 B assumed at ratification:

```
- **When no rule below covers it**, decide by these: verify over assert, gate over remember, derive over author, delete over disable, one fact in one place.
```

It is synthesized from what this playbook already enforces, not imported from the source charter. The
five pairs are §8's verify-don't-assert, §7's left-shift, §5's derived-not-authored, the YAGNI rule
this repo practises in its shrink-only pins, and §5's single-source rule. A fallback assembled from
rules already in force cannot contradict them, which an imported philosophy list could.

### Data model

None. This unit moves prose between two files and adds one line to a third.

### Migration

The two shipped files move in lockstep to v2.8, and `customize.md` moves with them.

This changes the version `TOOL-dClosedLexicon-1` lands at. That spec's §4 Migration names v2.8 for
its own edits; once this unit lands, the lexicon unit is v2.9. Amend it at its next rev rather than
now, because a version written into a parked spec rots exactly the way this repo has already recorded
twice, and the amendment belongs to the rev that unparks it.

### Rollout

One commit. The move, the §0 line, and the lockstep bump are one atomic edit — a landing that carries
the move without the marker bump ships a companion and a template that disagree, which is the failure
the marker exists to make visible.

### Files touched (estimate)

`parallel-coding-governance.template.md`, `parallel-coding-governance.domain-rules.md`,
`parallel-coding-governance.customize.md`. No code.

### Alternatives rejected

- **Externalize §14 whole, as ratified.** Rejected on the finding above. Recorded rather than
  silently narrowed, because the owner ratified the larger saving.
- **Externalize §16 instead.** MEASURED at 4,773 B, by far the largest section, and it has a genuine
  activity trigger in composing a work report. Rejected on coupling: §0, §1, §5 and §15 all cite §16,
  and its micro-formats are consumed every turn, so the trigger would fire every turn. Worth
  revisiting only if a future unit needs more than this one frees.
- **Externalize §8's Tier-2 mechanics.** MEASURED at 3,692 B with a real trigger in running a Tier-2
  review. Rejected for now because §8 carries the ≤5 concurrency rule, which §0 also states and which
  is enforced by a hook — splitting a rule that already has two homes needs its own pass.
- **Raise the ceiling.** Forbidden by `AGENTS.md` in as many words.

## 5. Production-readiness checklist

- security — N/A. Prose movement between shipped documents.
- perf / scale — N/A.
- a11y — N/A — no user interface.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — the byte ledger in the commit message is the observation; `check-template-size.sh`
  reports the resulting size on every subsequent run.
- risks — the real one is a moved rule going dark despite the split. The stub trigger names five
  concrete activities rather than a category, which is the mitigation, and the three always-on
  bullets never leave.
- testing + left-shift gates — `tools/check-template-size.sh` and, once
  `TOOL-dClosedLexicon-1` S12 lands, the marker-agreement assertion. Until then the lockstep is
  checked by reading, which is why S4 names all three files explicitly.
- migration / rollback — one commit, reverts cleanly; adopters re-pull per §-body diff as usual.
- user docs — `customize.md`'s conditional-section list is the adopter-facing change, in S4.

## 6. Acceptance criteria

- **AC1** — When the split lands, `bash tools/check-template-size.sh` is green and reports a size at
  least 700 bytes below the pre-landing 32,682.
- **AC2** — When `grep -c '^- ' ` is run over template §14, it reports four bullets: the three
  always-on ones and the stub.
- **AC3** — When the five moved bullets are diffed against their companion §14 copies, they are
  byte-identical, so `git diff` shows a move rather than a rewrite.
- **AC4** — When `grep -n 'governance-template: v2.8'` is run over both shipped files, both match.
- **AC5** — When the template header sentence is read, it names ten domain checklists over `§7–§14`,
  and `grep -c 'nine domain checklists'` reports 0.
- **AC6** — When §0 is read, it carries the fallback line, and `tools/check-template-size.sh` is still
  green with it present.
- **AC7** — When `parallel-coding-governance.customize.md` is read, its conditional-section list
  carries a §14 row naming what an adopter dropping it loses.
- **AC8** — When `bash tools/run-gates.sh` runs on the landing commit, it is green.

## 7. Gates

`tools/check-template-size.sh` is the leg this unit exists to satisfy. The rest of the bar must stay
green: `tools/memory-tree/check-memory-hygiene.sh`, `python tools/govkit/govkit.py selfcheck` (the
shipped playbook files are inside its declared surface), and `bash tools/run-gates.sh` entire.

This unit adds no gate. The marker-agreement check it would benefit from is `TOOL-dClosedLexicon-1`
S12, which lands after it — noted in §8 F2.

## 8. Open questions

- **F1 — does the §0 line earn 157 B when it is advice rather than a rule?** Nothing enforces it and
  nothing can. The counter-argument is that §0 is already the section of load-bearing summaries and a
  reader who hits an uncovered case currently has no stated method at all.
  RECOMMENDATION: keep it. It was ratified on a 120 B estimate and measures 157 B, and the 37 B
  difference does not change the decision against ~667 B of freed headroom.
- **F2 — this unit lands the lockstep it cannot yet verify.** `check-placeholders.sh`, which asserts
  the three markers agree, is `TOOL-dClosedLexicon-1` S12 and therefore lands after. AC4 is a read,
  not a gate, for exactly one landing. RECOMMENDATION: accept, and let S12's first run over an
  already-bumped pair be its own live control — a gate whose first run has a known-good subject is
  cheaper to trust than one whose first subject is the change that introduced it.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft. Corrects the externalization plan on measurement: §14 splits
  rather than moving whole, and the saving is ~738 B rather than the ~1,480 B ratified.

## 10. Reuse audit

The reuse here is a PATTERN rather than a seam, and it already ran six times in this document's own
history: §4, §9, §10, §11, §12 and §13 are each a rule set behind a triggered stub, and their stub
bodies are the shape S1 copies. `python tools/codebase-map/reuse_lookup.py template section stub`
surfaces no code seam because none exists — nothing in `tools/` reads section structure, and
`check-template-size.sh` weighs the file without parsing it.

The measurement method is the reusable part and it is not currently a tool: the per-section byte
census in §4 was a throwaway script. A future budget pass would repeat it. Whether that becomes
`tools/check-template-size.sh --census` is a follow-up worth a row, not scope here — a second
consumer justifies the tool, and this is the first.
