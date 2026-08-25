# PLAY-dClosedLexicon-1 — §0 gains a fallback rule, and the §14 externalization is refuted

**Status:** CLOSED · rev-3 · 2026-08-16 · node d · Tier-2 · base 587b95a4 · streams playbook

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-16-review-PLAY-dClosedLexicon-1-7.md](../reviews/2026-08-16-review-PLAY-dClosedLexicon-1-7.md) | diff-review | TOOL-dClosedLexicon-1 TOOL-dClosedLexicon-2 |

<!-- /gen:spec-records -->

## 1. Goal

Add the §0 fallback rule `TOOL-dClosedLexicon-1` F2 ratified, and record that §14 must NOT go behind
a §-stub — a conclusion this unit reached by measuring, and which refutes the recommendation
`PLAY-aCandidStub-2` currently carries as an OPEN row.

At rev-1 this unit was the byte-freeing predecessor the lexicon build was parked on. The ceiling is
being raised to 48 KiB in a parallel build, so the freeing half is moot and is dropped. What survives
is the line that was always the point, and the finding that would otherwise be lost with it.

BLOCKED, not DEFERRED, and the distinction is measured: the §0 line is 157 B against 86 B of headroom
at the present ceiling, so it does not fit until the raise lands. `TOOL-dClosedLexicon-1` is NOT
blocked — its playbook edits measure ~69 B and fit today at 32,751 of 32,768.

## 2. Scope (IN)

- **S1** — the §0 fallback rule, one line, naming how to decide a case no other section covers.
- **S2** — correct `PLAY-aCandidStub-2`. Its row recommends §14 as the strongest §-stub candidate,
  which §4 refutes. The row is mutable and node `a` owns it; the correction carries the measurement,
  not just a verdict, so a future session can check the reasoning rather than trust it.
- **S3** — the lockstep bump both shipped files take for any rule change, per §4 Migration.

## 3. Non-goals (OUT)

- The §14 split itself. Its only justification was byte pressure, and at 48 KiB there is none. §4
  keeps the measurement because the FINDING outlives the plan, but nothing is moved.
- Raising the ceiling, and the five places that spell 32 KiB (`AGENTS.md` three times, `README.md`,
  and the leg name in `tools/gate-legs.json`). The raise lands in a parallel build, and §3 says own
  streams rather than files — two units editing one gate's spellings is the overlap that rule exists
  to prevent. Named here so the parallel build's author sees the full population.
- Externalizing anything else. §16 and §8 were measured at rev-1 and are recorded in §4 for whoever
  next needs room, which at 48 KiB is nobody.

## 4. Design

### Why §14 must not go behind a §-stub

Every §-stub in the template carries an ACTIVITY trigger, and the trigger is what makes the
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

§14 is per-call token discipline. Its activity is every call in every session, so there is nothing to
trigger on. A stub reading "LOAD always" moves the bytes without saving them, because every session
still pays them. A stub nobody bothers to load makes always-on rules dark, which is worse than the
crowding it was meant to fix.

This is the reusable half of the finding: **§-stub externalization is available only to
activity-scoped sections**, and §14, §15 and §16 are the three that are not. The template has no
other section in that class, so the rule is complete as stated.

### The measurement that produced it

Taken at `587b95a4`. Retained because S2's correction has to carry evidence.

| Bullet | Bytes | Class |
|---|---|---|
| Strategy, spend tokens on new judgment | 338 | always-on |
| Don't re-fetch what's in context | 251 | always-on |
| Bound every command's output | 177 | always-on |
| Re-Read only when something else changed | 276 | situational |
| Don't poll background work | 185 | situational |
| Lint the files you changed | 231 | situational |
| Pin a review base to an immutable SHA | 197 | situational |
| A no-match `grep` exits non-zero | 178 | situational |
| **§14 total** | **1,900** | |

Three of eight bullets are violated with no activity in between, which is why a whole-section move was
never available. Section sizes for whoever next needs room: §16 is 4,773 B and §8 is 3,692 B, both
with real triggers and both heavily cross-referenced.

### The §0 line

Drafted and measured at 157 B:

```
- **When no rule below covers it**, decide by these: verify over assert, gate over remember, derive over author, delete over disable, one fact in one place.
```

Synthesized from what this playbook already enforces, not imported from the source charter. The five
pairs are §8's verify-don't-assert, §7's left-shift, §5's derived-not-authored, the YAGNI rule this
repo practises in its shrink-only pins, and §5's single-source rule. A fallback assembled from rules
already in force cannot contradict them, which an imported philosophy list could.

### Data model

None. One line added to one file, and one backlog row corrected.

### Migration

Any rule change moves both shipped files to the next version in lockstep. With the §14 split dropped,
this unit and `TOOL-dClosedLexicon-1` are the only playbook edits in flight, and whichever lands
first takes v2.8. Neither spec should name a number; the landing commit assigns it. That is the
correction rev-1 forced on the lexicon spec from the other direction, and it applies here too.

### Rollout

One commit. The line, the row correction and the lockstep bump land together.

### Files touched (estimate)

`parallel-coding-governance.template.md`, `parallel-coding-governance.domain-rules.md` for the marker
only, and `memory/backlog/PLAY.md`. No code.

### Alternatives rejected

- **Split §14 anyway, on readability grounds.** Without byte pressure the split buys a companion
  round-trip for five rules and costs a load step. Rejected: the §-stub is a budget instrument, not
  an organising one.
- **Close this unit WONTDO and fold the §0 line into `TOOL-dClosedLexicon-1` S13.** Tempting, and it
  would drop the build to two units. Rejected because the §14 finding needs a durable home with its
  measurement attached, and a spec is that home; a WONTDO tail pointer is not.
- **Correct `PLAY-aCandidStub-2` immediately rather than scoping it.** The row is 270 of its 300
  allowed characters, so the correction is a rewrite rather than an append, and rewriting another
  node's row is a shared-mutable-file edit that belongs in a landing, not a drive-by.

## 5. Production-readiness checklist

- security — N/A. One prose line and one record correction.
- perf / scale — N/A.
- a11y — N/A — no user interface.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — `tools/check-template-size.sh` reports the resulting size on every run.
- risks — the only one is landing before the ceiling raise, which the BLOCKED status exists to
  prevent. If the raise never lands, this unit does not land either, and nothing else in the build
  depends on it.
- testing + left-shift gates — `tools/check-template-size.sh`, plus the marker assertion from
  `TOOL-dClosedLexicon-1` S12 if that lands first.
- migration / rollback — one commit, reverts cleanly.
- user docs — none. `customize.md`'s conditional-section list is untouched, because §0 is universal
  core that an adopter never drops.

## 6. Acceptance criteria

- **AC1** — When §0 is read after landing, it carries the fallback line, and
  `bash tools/check-template-size.sh` is green at the raised ceiling.
- **AC2** — When `bash tools/check-template-size.sh` is run BEFORE the raise lands, it reds, which is
  the mechanical statement of this unit's BLOCKED status.
- **AC3** — When `grep -n 'governance-template: v' ` is run over both shipped files, both report the
  same version.
- **AC4** — When `PLAY-aCandidStub-2` is read after landing, its row no longer recommends §14, names
  the activity-trigger reason, and stays within the 300-character entry budget.
- **AC5** — When `bash tools/run-gates.sh` runs on the landing commit, it is green.

## 7. Gates

`tools/check-template-size.sh` and `tools/memory-tree/check-memory-hygiene.sh` (the row correction is
inside its entry-budget check). The full bar via `bash tools/run-gates.sh` at the push boundary. This
unit adds no gate.

## 8. Open questions

- **F1 — does the §0 line earn its bytes?** RESOLVED (owner, 2026-08-16): keep. It was ratified when
  157 B was scarce; at 48 KiB the byte objection is moot and the reason it was wanted is unchanged.
- **F2 — this unit may land a lockstep it cannot yet verify.** RESOLVED (agent, 2026-08-16,
  delegated): the recommendation was followed and the risk never materialised. `TOOL-dClosedLexicon-1`
  landed FIRST, so `tools/check-placeholders.sh` exists and rides the bar; AC3 is a GATE for this
  landing, not a read. The gate is also narrower than the fork assumed — its catalogue arithmetic was
  dropped as a duplicate of `check-playbook-parity.sh` — but the marker lockstep, which is the half
  AC3 needs, is exactly what survived and is checked by nothing else.

## 9. Revision log

- rev-3 · 2026-08-16 · BUILT and CLOSED. The blocker is gone: the 48 KiB ceiling landed with
  `aSiftedPlaybook` and arrived here in the dClosedLexicon merge, so the §0 line's 157 B now sits
  against ~11.8 KB of headroom rather than 86 B. S1 lands the fallback line at the end of §0, S2
  corrects `PLAY-aCandidStub-2` to WONTDO carrying the REFUTATION rather than a verdict — every
  §-stub needs an ACTIVITY trigger and §14's is every call, so a stub reading "LOAD always" moves
  bytes without saving any and makes always-on rules dark — and S3 takes both marker carriers to
  v2.10 in lockstep. AC2 is no longer observable and is recorded as such: it asserted the unit reds
  BEFORE the raise, and the raise has landed.

- rev-1 · 2026-08-16 · initial draft. Corrects the externalization plan on measurement: §14 splits
  rather than moving whole, and the saving is ~738 B rather than the ~1,480 B ratified.
- rev-2 · 2026-08-16 · reworked for the 48 KiB ceiling landing in a parallel build. The §14 split is
  dropped entirely — its only justification was byte pressure — and the finding that produced it is
  kept as S2's evidence. Status SPECCED to BLOCKED: the §0 line is 157 B against 86 B of headroom and
  does not fit until the raise lands. The unit stops being anyone's predecessor.

## 10. Reuse audit

No code seam. The §0 line reuses five rules already in the document rather than importing a
philosophy, which is the whole argument for its wording. S2 reuses the backlog row grammar the
memory-tree gate already enforces, including the 300-character entry budget that shapes the
correction into a rewrite.

The per-section byte census in §4 was a throwaway script at rev-1 and is now cited by a second
consumer, this spec's own S2 evidence. That is the point at which a tool is justified rather than
speculative, so `tools/check-template-size.sh --census` becomes worth a backlog row — but not scope
here, since at 48 KiB nobody is shopping for room.
