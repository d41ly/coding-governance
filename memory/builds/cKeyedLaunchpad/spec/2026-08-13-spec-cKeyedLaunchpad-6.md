# KICK-cKeyedLaunchpad-6 — evicting the traps that pay, and restoring the cap the kit already shipped

**Status:** OPEN · rev-3 · 2026-08-13 · node c · Tier-2 · base f006691f · streams kickoff+tooling

## 1. Goal

Shrink the traps section from 70% of the manifest to a bounded remainder, by deleting what a
`memory/gotchas/` record already says, correcting what is wrong, and enforcing the one-line rule the
kit's own template has always stated and this repo's manifest has never obeyed.

## 2. Scope (IN)

- S1. Delete the SIX bullets wholly carried by an existing record, each replaced by a one-line pointer
  naming that record. §4's table names all six.
- S2. Evict exactly ONE trap to a new record, at `memory/gotchas/inputs-inside-the-subjects-reach.md`,
  leaving a pointer in its place.
- S3. Delete the merge-driver bullet outright, with NO pointer. It is wrong, not duplicated.
- S4. **Rewrite the agent-cap bullet, which SPLITS.** Its concurrency half is carried by a record and
  goes, cited inline; its wiring half is repo-local and stays, with the stale kit version corrected.
- S5. Correct the stale drift-signal pin in the gate-leg bullet.
- S6. A new check, **C11**, caps every traps bullet at 400 bytes, the same number C8 uses for a line.
  U4 takes C10; §4 records why the number is not this unit's to choose.
- S7. **Rewrite EVERY surviving bullet that exceeds the cap.** Measured: fourteen do. This is the
  owner's decision 5 as written — "U6 rewrites the surviving over-cap trap bullets" — not a subset.
- S8. Lower `READ_PATH_CEILING` in `.memory-tree.conf` to the post-eviction measured read-path total
  plus the stated margin, recording the measurement in the conf comment. U2 raises it for the move;
  this unit is what makes the raise temporary.

## 3. Non-goals (OUT)

- **Not all seven orphan classes are evicted.** §4 gives the arithmetic. Five stay because each needs
  authored anchors and its own dossier claim, and the universal budget is full.
- **No `universal: true` record.** The budget is 3 of 3 and raising it is a separate decision in a
  commit that says why.
- **No new dossier.** S2's record is claimed by an existing one.
- **No citation of this build's own spec ids from the manifest.** The manifest is product source for a
  drift signal pinned at 2 with zero tolerance, and naming a non-terminal spec there reds the bar.
  It already did once. Every reference stays paraphrased.
- U7 owns the engine's prose. This unit touches only the manifest and the catalogue.

## 4. Design

### The measured section — every figure below is measured, none is estimated

Measured at BASE, LF-normalised, counting each bullet as its `- ` line plus its continuation lines:
**27 bullets, 14,535 bytes, 19 over 400 bytes, largest 1,199.**

Two revisions of this section were wrong before this one, both by reasoning about the numbers instead
of taking them. rev-1 set a 4,000-byte target that deletion could not reach. rev-2 authorised
rewriting "the three named survivors" and asserted the rest were already under the cap — measurably
false, and the M4 fix-verify pass blocked on it a second time. The table below is the measurement.

| Disposition | Bullets | Bytes |
|---|---|---|
| Deleted, wholly carried by a record (S1) | 6 | 2,835 |
| Evicted to a new record (S2) | 1 | 471 |
| Deleted as wrong, no pointer (S3) | 1 | 603 |
| **Removed, total** | **8** | **3,909** |
| **Survivors** | **19** | **10,626** |
| …of which exceed the 400-byte cap | 14 | — |

So S7 authorises rewriting **fourteen** bullets, not three. That is what the owner's decision 5
already said in general terms, and what rev-2 narrowed without measuring.

### Why AC1's target is derived rather than chosen

Both earlier revisions picked a byte target and then failed to reach it. This one does not pick: if
every survivor obeys C11 (AC6), the section's size is BOUNDED by construction —

> 19 survivors × 400-byte cap + 7 pointer lines × ~90 bytes + ~200 bytes of section prose ≈ **8,430**

AC1 asserts that ceiling and nothing tighter, so AC1 and AC6 cannot disagree: satisfying the cap
satisfies the size. The realistic outcome is far smaller — a rewritten trap runs nearer 250 bytes than
400, putting the section around 5,600 — but a spec that promises the realistic number is a spec that
blocks on the pessimistic one.

### The classification, named

rev-1 gave only counts, which made the unit's largest edit undecidable. rev-2's table then merged
three different dispositions into one list and double-counted the eviction. They are separated here.

**Deleted outright, wholly carried by an existing record** — each leaves a one-line pointer naming its
record, which is what AC2 greps for:

| Trap bullet, opening words | Carried by |
|---|---|
| a byte-comparing gate needs both halves | `gate-green-by-accident-on-generated-bytes.md` |
| a new gate PREDICATE is run over the real tree first | `absence-assertion-over-whole-file-text.md` |
| a `git worktree` checkout can land CRLF on an eol=lf path | `gate-green-by-accident-on-generated-bytes.md` |
| `subprocess.run` resolves the SYSTEM32 WSL launcher | `subprocess-resolves-a-different-shell.md` |
| generating source through a shell heredoc | `heredoc-escape-reaches-the-regex.md` |
| a core-subset-of-effective assertion is VACUOUS | `assertion-between-two-derived-values.md` |

**Evicted to a new record (S2), leaving a pointer:** the "ask what SUPPLIES each of a check's inputs"
bullet, to `inputs-inside-the-subjects-reach.md`. It is NOT one of the six above — it is one of the
seven orphan classes, and rev-2 listing it as a seventh duplicate is what made the table contradict
its own arithmetic.

**Rewritten because it SPLITS (S4):** the agent-cap bullet. Its concurrency half is carried by
`concurrency-is-not-a-budget.md` and goes, cited inline. Its wiring half — which matcher, which four
rules, where the binding protocol lives — is repo-local, is carried by no record, and STAYS with its
stale kit version corrected. rev-2 sent the whole bullet to deletion while S4 simultaneously required
its version corrected, which no builder could satisfy both ways; the version string exists nowhere
else in the section.

**Deleted with no pointer (S3):** the merge-driver bullet, because it is wrong rather than duplicated.

The eight duplicates are pure deletion — the record already exists, so the bullet is a second copy
whose only future is to disagree with it. One of them, the heredoc-escape trap, is duplicated by a
record that explicitly says its remedy is "recorded in the kickoff manifest's environment traps",
which is the duplication describing itself.

The seven orphans are not equal. Six would each cost an authored anchor, a dossier claim and an index
render, and two of them derive ZERO anchors as currently written — a check-19 refusal, because an
unanchored non-class record can never appear on a checklist and `universal: true` is unavailable at a
full budget. Anchoring them is authorial work, not a move.

**One orphan pays for itself.** The trap about asking what SUPPLIES a check's inputs is already
referenced by `second-implementation-is-not-a-second-opinion.md` through a wiki-link,
`[[inputs-inside-the-subjects-reach]]`, that resolves to no record. Nothing gates wiki-links, so that
dangling pointer has been shipping. Evicting this trap under that exact filename repairs a shipped
defect for free; evicting it under any other name leaves the link dangling. That is the one eviction
this unit performs.

### Why a bullet that is merely wrong is more urgent than a bullet that is long

The merge-driver trap says `tools/memory-tree/merge-rows.sh` does not exist and gives a remedy setting
`merge.rows.driver` to the `pyrun.sh` form. That file exists now and is the kit's own launcher.
`check-wiring.sh` builds the `merge-rows.sh` form as its expected value and deliberately DECLINES to
overwrite a set value, so an operator who follows the trap configures a value the check reports as
`UNWIRED` and `--fix` will not repair. The trap manufactures the problem it claims to solve.

Two further figures are stale in bullets that otherwise survive: an agent-cap version that has moved
on, and a drift pin quoted as seven of forty at zero tolerance that now reads zero of fifty-three.
The second is stale in the direction that matters — the conclusion it draws is now stronger, since
there is no slack at all.

### The cap is the kit's own rule, not a new number

`MANIFEST-TEMPLATE.md` already instructs: keep each trap to one line, and link out for detail. This
repo's manifest ignored it until the section reached 14,821 bytes, with a largest bullet of 1,209.
S5 makes that instruction mechanical rather than inventing a ceiling — and it reuses C8's 400 bytes
rather than minting a second number, on the reasoning that C8 already defines how long a line may be
and "one line" is what the template asked for.

C7's total-size cap is not a substitute. It bounds the file, so traps could re-accrete to 25 KiB by
crowding out every other section. S5 bounds the entry, which is where accretion actually happens.

### What a new record costs, and the order that makes it visible

The manifest's own procedure bullet for this is correct and stays: a new record needs the index
re-render for check 17 AND a dossier claim for coverage, and the coverage inventory reads TRACKED
files — so measuring before `git add` reports ok over a file the gate cannot see, and the gap surfaces
on the full bar instead. Stage first, then measure. This unit follows the instruction it is preserving.

Two selection semantics shape the record's text. Anchors are DERIVED from backticked path-like tokens
in the body, never declared, so the citations ARE the selector. And anchor matching includes tree-wide
basename equality, so a record citing a short filename selects that basename wherever it lives —
which is why adding seven records at once is the fastest way to turn the reviewer checklist into the
noise the module's own docstring warns about. One record, well anchored, is the conservative move.

### Files touched (estimate)

| File | Change |
|---|---|
| the manifest (at U2's path) | eight deletions with pointers, one deletion, two corrections, and the re-stamp |
| `memory/gotchas/inputs-inside-the-subjects-reach.md` | new record |
| `memory/gotchas/INDEX.md` | re-rendered |
| `memory/map/features/unattended.md` | the new gotcha key claim |
| `memory/map/generated/` | regenerated |
| `skills/session-kickoff/manifest-check.sh` and its test | S5's check and arms |
| `.memory-tree.conf` | the raised arms floor, and S8's lowered `READ_PATH_CEILING` |

### Alternatives rejected

- **Evicting all seven orphans.** Six cost authored anchors plus dossier claims for no repaired
  defect, and two cannot land at all as written.
- **A bullet-COUNT cap.** Bounds the wrong axis: thirty terse bullets are fine and three essays are
  not.
- **Leaving the merge-driver bullet with a correction.** Its remedy is the whole bullet; corrected, it
  says what `check-wiring.sh` already reports.
- **Raising `UNIVERSAL_BUDGET` to let an unanchored trap land.** Trades a hard analysis for a wider
  checklist, and the budget exists to stop exactly that.

## 5. Production-readiness checklist

- security — N/A; documentation and one read-only check.
- perf / scale — one awk pass over one section.
- a11y — N/A. i18n — the cap counts bytes, consistent with C8.
- error / empty / loading states — a manifest with no traps section passes S5 vacuously, which is
  correct: the cap bounds entries, it does not require them.
- observability — the failure names the offending bullet's first words and its measured size.
- risks — the new record's basename anchors widen what the checklist selects for unrelated diffs; one
  record is the bounded version of that cost.
- testing + left-shift gates — S5's arms, plus the record's own check-17/18/19 conformance.
- migration / rollback — adopters inherit S5 on re-pull; the template already stated the rule, so no
  adopter is being held to a rule they were not given.
- user docs — the template's one-line instruction is unchanged; it simply becomes enforced.

## 6. Acceptance criteria

- AC1. The manifest's traps section is under 8,430 LF-normalised bytes, down from 14,535. That
  ceiling is DERIVED in §4 from AC6's cap and the survivor count, so AC1 cannot contradict AC6.
- AC2. None of the six bullets named in §4's deletion table survives, and the traps section contains a
  pointer line naming each of those six record filenames — checked by grepping for the six filenames,
  not by judging substance. The evicted bullet's pointer names a seventh filename.
- AC3. `memory/gotchas/inputs-inside-the-subjects-reach.md` exists, and
  `grep -o '\[\[[a-z-]*\]\]' memory/gotchas/*.md` resolves every link to a real record.
- AC4. `python tools/memory-tree/gotchas.py --check` passes checks 17, 18 and 19 for the new record,
  including its derived anchors being non-empty and not inert.
- AC5. The merge-driver bullet is gone, and `bash tools/check-wiring.sh --check` still reports the
  merge driver as wired on a correctly configured node.
- AC6. When a traps bullet exceeds 400 bytes, the check fails naming that bullet and exits 1.
- AC7. When every bullet is at or under 400 bytes, the check passes.
- AC8. No surviving bullet quotes a figure this repo can print — the agent-cap version and the drift
  pin are corrected, and neither is restated where the gate that owns it can be run instead.
- AC9. `python tools/codebase-map/test_codebase_map.py` passes with the new gotcha key claimed, and
  the generated artifacts byte-compare after a `git add`.
- AC10. `GATE_FULL=1 bash tools/run-gates.sh` is green.
- AC11. All FOURTEEN over-cap survivors measure at or under 400 bytes after the rewrite, and each
  still states the fact it stated before — asserted by reading them, not by the byte count alone.
- AC13. The agent-cap bullet survives, its wiring half intact and its kit version corrected, and its
  concurrency half is gone with the record cited inline. This is the arm that fails if the bullet is
  deleted wholesale.
- AC12. `READ_PATH_CEILING` in `.memory-tree.conf` equals a freshly measured post-eviction read-path
  total plus the stated margin, and `python tools/memory-tree/corpus_ids.py --report` confirms the
  measurement the conf comment records.

## 7. Gates

- `bash skills/session-kickoff/manifest-check.sh` and its self-test — S5's check.
- `python tools/memory-tree/gotchas.py --check` and `--write` — checks 17 through 19.
- `python tools/codebase-map/test_codebase_map.py` — the coverage claim and the freshness render.
- `python tools/memory-tree/check-arms.py` · `GATE_FULL=1 bash tools/run-gates.sh`.

## 8. Open questions

none.

- Whether to evict or cap. RESOLVED (owner, 2026-08-13): evict the bug classes, cap the machine-local
  remainder. §4 narrows "the bug classes" to the one that repairs a dangling link, on the measured
  cost of the other six, and records the six so the decision can be revisited with the arithmetic in
  front of it rather than re-derived.

## 9. Revision log

- rev-1 · 2026-08-13 · initial draft, grounded by workflow `wf_0aaecb50-a51`.
- rev-3 · 2026-08-13 · folded the M4 fix-verify pass, which BLOCKED on this unit a second time. The
  rev-2 arithmetic was still wrong: it reused the audit's upper bound as if it described the
  authorised set, claimed the survivors were "already under the cap or one-lined", and narrowed the
  owner's general rewrite authorisation to three bullets. Measured properly this revision — 27
  bullets, 14,535 B, 19 over cap; 8 removed for 3,909 B; **19 survivors of which 14 exceed the cap**.
  S7 now authorises all fourteen, which is the owner's decision 5 as written. AC1's ceiling is DERIVED
  from the cap and the survivor count rather than chosen, so it cannot contradict AC6. Three further
  defects the pass found in the rev-2 table: the agent-cap bullet SPLITS and its wiring half must
  survive (S4, AC13) where rev-2 sent it to deletion while also requiring its version corrected; the
  eviction was double-counted as a seventh duplicate, contradicting the 8/7/12 split; and the check
  number C10 collided with U4, so this unit takes C11.
- rev-2 · 2026-08-13 · folded the M4 spec audit, review record 1. H10 (blocking): AC1 and AC7 were
  arithmetically unsatisfiable together — 19 of 27 bullets exceed the cap, the authorised deletions
  leave 6,828 bytes against a 4,000-byte target, and three bullets §4 keeps already exceed the cap
  this unit introduces. Added S7 authorising the rewrite of the three named survivors, restated the
  measured baseline, and moved AC1 to a target the authorised edits reach. H11: AC2 named a grep with
  no pattern for a semantic predicate, and was the only criterion for the unit's largest edit — the
  eight-bullet classification is now a table in §4 and AC2 greps for the eight record filenames.
  H6: accepted S8, the `READ_PATH_CEILING` lowering U2's §3 assigned here and rev-1 never took, with
  a Files-touched row and AC12.

## 10. Reuse audit

The catalogue and its gates are reused wholesale — no new mechanism. `gotchas.py` already owns record
parsing, anchor derivation, the index render and checks 17 through 19; this unit adds one conforming
record and deletes prose. S5's check reuses C8's awk region-tracking and its byte limit rather than
introducing a second length rule.

The record's home was DERIVED, not chosen: an existing record's dangling wiki-link already names the
file, so the eviction target was determined by a defect in the corpus rather than by preference. That
is the strongest form of the reuse question — the seam named itself.

`reuse_lookup.py "bound how long an entry in a document may be"` returns `check-memory-hygiene.sh`'s
index-entry cap, which is the same shape at a different scale: it caps an ENTRY inside a file the
whole-file cap also covers, exactly as S5 caps a bullet inside a file C7 covers. That precedent is the
argument for S5 existing alongside C7 rather than being folded into it.

Recall terms used: `kickoff manifest ratchet last-audit watch verify-paths SESSION-KICKOFF discovery
order traps accretion size gate prose`.
