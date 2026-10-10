# TOOL-aFrugalTurnstile-12 — the close's bar runs with the bar knobs scrubbed, so its green certifies the whole bar

**Status:** OPEN · rev-1 · 2026-10-10 · node a · Tier-2 · base bef97330 · streams tooling · order 6

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The unattended close's `gates-green` arms inherit `GATE_LEGS`, `GATE_REUSE` and `GATE_DOCS_BASE` from the driver's environment, and `write_bar_green` then records the rc-0 result as a trusted `gate-bar-green`, so a subset run can certify the whole bar for that tree. The hook and `post-merge.sh` already scrub these knobs for their own bars; the driver must too. Promoted from the closing review's item H1 (finding ids 1 and 6), 2026-10-10-review-TOOL-aFrugalTurnstile-1-11-diff-review-round1.md, at the CONVERGED exit (build method M4: every confirmed finding is promoted).

## 2. Scope (IN)

- **S1 — the scrub.** Every bar call in the `gates-green` arm of `tools/unattended/unattended.sh` (the in-place `full`, `scoped` and fallback calls, and the primary call) runs under `env -u GATE_LEGS -u GATE_REUSE -u GATE_DOCS_BASE -u GATE_SPAWN_CMD -u GATE_SPAWN_FLOOR -u GATE_VERDICT_FAULT` beside the existing `-u GATE_WALL`: the hook's `BAR_SCRUBBED_KNOBS` plus the docs knob. When any of them was set in the driver's environment, the arm prints one line naming them, `unattended: gates-green — not honoured from the environment by this bar: <names>`. Observed by AC1, AC2.
- **S2 — the parity arm.** One arm in `tools/unattended/unattended.test.sh` extracts the hook's `BAR_SCRUBBED_KNOBS` value and asserts every name in it appears in the driver's scrub, so a knob added to the hook reds the driver's copy. Observed by AC3.

## 3. Non-goals (OUT)

- Any finding of the review this unit does not name; each has its own promoted unit.
- A kit-version bump: one bump per touched kit happens after the last unit.

### Edges

none

## 4. Design

The fix is the review's, judged SOUND by its skeptic (or the skeptic's corrected fix where it judged the finder's unsound); see the report's item H1 for the defect, the reachable path and the left-shift gate.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`

## 5. Production-readiness checklist

- security — the change narrows what a green record may certify; nothing new is trusted.
- perf / scale — no new spawn on the common path beyond what each criterion names.
- error / empty / loading states — every refused input prints one line and takes the safe (larger) path.
- observability — the new refusal or decline line is named in §2.
- testing — the arm in §7, run at VERIFYING; the pass observes each criterion in a scratch fixture.
- migration — none; records written before this unit read as they did.
- risks — the fix can only force more work where it is wrong, never less; a mis-scoped predicate costs a saving, not a verdict.
- user docs — the touched script's header sentence.

## 6. Acceptance criteria

Each criterion is observed in a scratch fixture first against the file at the previous commit, then against the edit.

- **AC1** — When the driver's environment exports `GATE_LEGS` naming a one-leg manifest and the close runs a green bar under a declared stub that writes its own environment to a file, that file shows `GATE_LEGS` unset and the output carries `not honoured from the environment by this bar`. Red when: the stub sees `GATE_LEGS`, the behaviour at the previous commit.
- **AC2** — When `GATE_REUSE=1` and `GATE_DOCS_BASE` are exported instead, the stub sees neither. Red when: it sees either.
- **AC3** — When the parity arm's extraction runs over the hook and the driver, every `BAR_SCRUBBED_KNOBS` name is present in the driver's scrub; when a staged copy of the driver drops `GATE_REUSE`, the arm's check names `GATE_REUSE`. Red when: the dropped name passes.

## 7. Gates

`unattended kit gate` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · a stub bar writing its environment, and the hook/driver scrub extraction · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-10 · §1-§7: promoted from the closing review round 1, item H1.

## 10. Reuse audit

The seams are this build's own, named in §2 by file and function; `reuse_lookup.py` cannot see `.sh` (memory note "reuse_lookup cannot see shell seams"), so they were read from source at 61e5103c8. No existing seam does what §2 adds.

Recall terms used: pre-push full green stamp scoped boundary candidate post-merge red decide lineage ledger scrub
