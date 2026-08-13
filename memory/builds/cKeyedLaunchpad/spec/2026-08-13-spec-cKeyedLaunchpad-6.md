# KICK-cKeyedLaunchpad-6 — evicting the traps that pay, and restoring the cap the kit already shipped

**Status:** OPEN · rev-1 · 2026-08-13 · node c · Tier-2 · base f006691f · streams kickoff+tooling

## 1. Goal

Shrink the traps section from 70% of the manifest to a bounded remainder, by deleting what a
`memory/gotchas/` record already says, correcting what is wrong, and enforcing the one-line rule the
kit's own template has always stated and this repo's manifest has never obeyed.

## 2. Scope (IN)

- S1. Delete the eight bullets already carried by an existing record, each replaced by a one-line
  pointer naming that record.
- S2. Evict exactly ONE trap to a new record, at `memory/gotchas/inputs-inside-the-subjects-reach.md`.
- S3. Delete the merge-driver bullet outright. It is wrong, not stale.
- S4. Correct two stale figures in surviving bullets: an agent-cap kit version and a drift-signal pin.
- S5. A new check caps every traps bullet at 400 bytes, the same number C8 uses for a line.
- S6. The five orphan bug classes that are not yet worth a record stay as one-line bullets under S5's
  cap, with the reasons recorded here.

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

### The eviction arithmetic, which is why "evict them all" is the wrong plan

Of 27 bullets: **eight** are already carried by an existing record, **seven** are bug classes with no
record, and **twelve** are machine- or repo-local facts that must stay.

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
| `.memory-tree.conf` | the raised arms floor |

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

- AC1. The manifest's traps section is under 4,000 bytes, down from 14,821.
- AC2. `git grep -c` finds no surviving manifest bullet whose substance is carried by an existing
  `memory/gotchas/` record; each deleted one leaves a pointer naming the record.
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
