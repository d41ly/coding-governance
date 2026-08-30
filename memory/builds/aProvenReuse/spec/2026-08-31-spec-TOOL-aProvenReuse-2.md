# TOOL-aProvenReuse-2 — a `reuse-probed` DoD item joins the run to the recall query log

**Status:** OPEN · rev-1 · 2026-08-31 · node a · Tier-2 · base 3bfc5e87 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aProvenReuse-1.md](../prompts/2026-08-31-prompt-TOOL-aProvenReuse-1.md) | research | TOOL-aProvenReuse-1 |

<!-- /gen:spec-records -->

## 1. Goal

Give the `reuse-first` directive a LIVENESS half. `TOOL-aProvenReuse-1` makes a spec RECORD a reuse
audit; nothing there can tell a recorded audit from a typed one. This unit makes `--close` observe
that a recall probe actually ran in this run's tree, using the query log
`tools/memory-recall/query.py` already writes, and makes a waived `reuse-first` announce itself
instead of passing in silence.

## 2. Scope (IN)

- **S1** — `reuse-probed:machine` joins `DOD_CORE` in `tools/unattended/unattended.sh`.
- **S2** — a `reuse-probed)` arm in `dod_met` with exactly four outcomes, each with its own message:
  - **waived** — `reuse-first` appears in `recorded_waivers "$rel"`. MET, and `DOD_OUT` names the
    waiver and its recorded reason. This is the arm that ends the silent waiver.
  - **no log** — the log file does not exist. UNMET, and the message says the log is ABSENT rather
    than that zero probes ran. Those are different facts and an operator who confuses them looks for
    the wrong repair.
  - **zero** — the log exists and holds no `query` row for this tree. UNMET, message names the
    remedy: run the probe, or override.
  - **met** — one or more. MET, and `DOD_OUT` reports the count and the newest row's timestamp, so
    the wrap-up carries a number rather than a verdict.
- **S3** — the log is located as `$(git rev-parse --git-common-dir)/recall/queries.jsonl`, which is
  where `query.py`'s own `log_path()` puts it and where `recall-opened.js` reads it. The location is
  DERIVED by the same rule both existing readers use, never spelled as a path literal.
- **S4** — a row belongs to this run when its `worktree` value names this run's tree. Comparison is
  on the path with backslashes folded to forward slashes, because the logged value is written by
  Python on Windows and carries `\` while the shell's own root carries `/`.
- **S5** — `CORE_FLOOR` moves `12:10` to `12:11` in `.unattended.conf` and in
  `tools/unattended/.unattended.conf.example`.
- **S6** — the kit's SKILL and PROTOCOL templates lose the sentence asserting that waiving
  `reuse-first` is silent and that nothing machine-checks a reuse section, because after this build
  both halves of it are false, and both renders are refreshed. The kit version moves; the carriers
  are whatever `bash tools/check-kit-versions.sh` names.
- **S7** — self-test arms in `tools/unattended/unattended.test.sh` for all four S2 outcomes.

## 3. Non-goals (OUT)

- **N1** — a merge-bar leg. The log lives in the git common dir and is neither tracked nor pushed,
  so `tools/unattended/check-unattended.sh` could only ever report DEAD PROBE on it in a fresh
  clone. A check that cannot run where the bar runs does not belong on the bar.
- **N2** — joining the logged terms to the terms a spec records. The log carries `terms` and a spec
  now carries them too, so the join is buildable, but it needs an overlap threshold and this build
  has no measurement to set one from. A threshold copied from nowhere is the
  `pin-copied-from-another-corpus` class.
- **N3** — a time window. The prompt path runs its probes BEFORE the build folder exists, so a
  window anchored on the pinned BASE would systematically miss the orientation probes this whole
  build is about. §4 states the cost of using the tree instead.
- **N4** — observing `tools/codebase-map/reuse_lookup.py`. It writes no log. See the build README's
  third build-level rule.
- **N5** — making the item unoverridable. `authorization-reachable` and `pieces-complete` are the
  two items with no override and both are about authorization; this one is about diligence, and a
  run resumed on a node whose log does not carry the probe has a legitimate reason to override.

## 4. Design

### Inventory

| Path | Change |
|---|---|
| `tools/unattended/unattended.sh` | S1 `DOD_CORE`; S2–S4 the `dod_met` arm |
| `.unattended.conf`, `tools/unattended/.unattended.conf.example` | S5 `CORE_FLOOR` |
| `tools/unattended/SKILL.template.md`, `PROTOCOL.template.md` | S6 the retired sentence, the new item |
| `.claude/skills/unattended/SKILL.md`, `memory/guides/UNATTENDED-PROTOCOL.md` | S6 renders |
| `tools/unattended/unattended.test.sh` | S7 |

### What this item claims, and what it does not

Stated here rather than left to a reader, because §7 of the charter requires a check to declare its
own blind spots. The item observes that **a recall probe ran in this worktree**. It does not observe
that the probe was run FOR this build, that its question was relevant, or that its answer was read.
A worktree reused across two builds carries the earlier build's rows and would satisfy the later
one. That limit is accepted because the alternative — a time window — has a worse failure, N3's, and
because the item's job is to make zero distinguishable from unmeasured, which it does.

### Alternatives rejected

- **A `DOD_EXTRA` declaration instead of a core item.** Rejected on inspection of source: `dod_met`
  routes every item it does not know to a `*)` arm that greps the run-state file for an
  attestation. A project-declared item is therefore attestation-only by construction, and an
  attestation is precisely what this unit exists to replace.
- **Enforcement at `--preflight`.** Rejected: on the slug path the probes legitimately run after
  preflight, so the check would refuse every correct run.
- **A new verb, `--record-probe`.** Rejected: it would ask the agent to attest what a log already
  records, which is the weaker of two available evidences and one more thing to forget.
- **Reading the log through `query.py`.** Rejected: the driver is POSIX shell with no Python
  dependency in this path, and the read is one `grep` over a line-oriented file. Adding a Python
  hop to parse JSON the shell can substring-match would make the driver depend on the memory-recall
  kit being installed, which no adopter is required to do.

### Migration

None. A run whose log carries no rows meets the `zero` outcome and can override with a reason, which
is the documented path for every other unmet item.

### Rollout

One commit with `TOOL-aProvenReuse-1`'s, or immediately after it. The item is inert for any run that
has run a probe, which every conforming run has.

## 5. Production-readiness checklist

- **Security** — the driver reads one more file inside the git common dir, a directory it already
  writes to. No new input from outside the repo, no new write.
- **Performance** — one `grep -c` over a file whose growth is one line per query. Bounded by nothing
  today; the read is a single pass and the file is tens of KB after 169 records.
- **Error states** — the four S2 outcomes are exhaustive over "file absent / no match / match", plus
  the waiver short-circuit which precedes all three.
- **Observability** — `DOD_OUT` carries a distinct sentence per outcome, and `--close` already
  prints it. The count reaches the wrap-up through the same channel every other item uses.
- **Testing** — S7.
- **Migration/rollback** — revert; `CORE_FLOOR` returns to `12:10`.

## 6. Acceptance criteria

- **AC1** — with `reuse-first` recorded as waived, `--close` reports `reuse-probed` MET and the
  message names the handle and its recorded reason. Observed against a fixture run-state file
  carrying a waiver row.
- **AC2** — with no log file present, `--close` reports `reuse-probed` UNMET and the message
  contains the word `absent`, distinct from AC3's message.
- **AC3** — with a log present holding no row for this tree, `--close` reports UNMET and names the
  remedy.
- **AC4** — with a log holding at least one `query` row for this tree, `--close` reports MET and the
  message carries the row count.
- **AC5** — `bash tools/unattended/unattended.sh --close <slug> --override reuse-probed --reason "…"`
  records the override as a parked entry, proving N5. The negative control: `--override
  authorization-reachable` is still refused, so this unit did not widen the no-override set.
- **AC6** — `bash tools/unattended/check-unattended.sh` exits 0 with `CORE_FLOOR` at `12:11`, and
  reds with it left at `12:10`. The second half is the liveness assertion for the first.
- **AC7** — `bash tools/unattended/unattended.test.sh` passes with S7's arms present.
- **AC8** — `bash tools/check-kit-versions.sh` exits 0, and no tracked file still asserts that
  waiving `reuse-first` is silent. Checked by grep over the tree, because the claim appears in two
  templates and two renders and a fold that misses one leaves a document contradicting the code.

## 7. Gates

`bash tools/run-gates/run-gates.sh` for the bar, which carries `unattended kit gate` and
`unattended skill wiring` unguarded. `bash tools/unattended/run-unattended-gates.sh` for the kit
self-tests, which the owner's 2026-08-23 ruling took off the bar and which this unit's AC7 owes
because this IS kit work. `bash tools/check-kit-versions.sh` for AC8.
What no gate here checks: that the log this item reads is the log the agent's probe wrote. The two
are joined by a path both readers derive the same way, and a divergence would show as AC2's
`absent` outcome rather than as a wrong verdict.

## 8. Open questions

- **Q1 — should a missing log be UNMET or a MET-with-notice?** **RESOLVED (agent, 2026-08-31,
  delegated):** UNMET. A missing log is exactly the state where the item cannot answer its question,
  and the charter's rule is that a probe which cannot move says so rather than reporting a
  reassuring zero. Reporting MET would be a green verdict earned by the check being broken.
- **Q2 — is the worktree match the right join, given §4's stated limit?** **RESOLVED (agent,
  2026-08-31, delegated):** yes, by M3's rule. The two surviving options were a worktree match and a
  BASE-anchored time window; the window fails an acceptance criterion this build's own goal states,
  because it cannot see the prompt path's orientation probes. Fewest follow-ups left open decides it,
  and the limit is written into §4 rather than left for a reader to discover.

## 9. Revision log

- rev-1 · 2026-08-31 · authored by the aProvenReuse run.

## 10. Reuse audit

Three seams, all extended in place, none created. `tools/memory-recall/query.py`'s `log_path()`
already writes `<git-common-dir>/recall/queries.jsonl` with a `type: "query"` row carrying `terms`,
`query`, `at` and `worktree`; `tools/memory-recall/recall-opened.js` already reads that file and
already derives the common git dir the way S3 does; and `dod_met` in
`tools/unattended/unattended.sh` already dispatches per item with a demonstrated skip-announcing
idiom at its `pieces-complete|set-checks-recorded` arm, which S2's waived outcome copies rather than
reinvents.

`python tools/codebase-map/reuse_lookup.py "checking that a spec records a reuse audit before code
is written"` returned the `.unattended.conf` affordance seam and `check_audit` in
`tools/memory-recall/check-recall.py`. The latter was inspected and REJECTED: it grades a retrieval
FIXTURE against a pinned precision floor and holds no reader of the query log at all.

Recall terms used: `reuse-first reuse audit spec section 10 seam recall probe terms directive waiver
silent unchecked machine-checked prose`. The same query as this build's other unit, per M5's rule
that the obligation is satisfied once for the SET.

Where a hit was STALE: the recall probe did not surface any reader of the query log, and
`recall-opened.js` was found by grep over `.claude/settings.json` after the SessionStart hook
reported the wiring. That is recorded because it is the probe-failure taxonomy in action — the log
reader exists and the corpus has no decision record naming it, so recall could not have found it.
