# TOOL-dBriefedPass-2 — the unit BRIEF, a tracked record of what a building agent was handed

**Status:** SPECCED · rev-1 · 2026-09-01 · node d · Tier-2 · base 269dacae · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-prompt-TOOL-dBriefedPass-1.md](../prompts/2026-09-01-prompt-TOOL-dBriefedPass-1.md) | research | TOOL-dBriefedPass-1 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5 |

<!-- /gen:spec-records -->

## 1. Goal

Make "what instructions did this agent start building with" answerable from the tree. A build pass
records the BRIEF it was handed as a tracked file joined to its unit's spec, written by a driver verb
so it cannot be composed after the fact or left out.

## 2. Scope (IN)

- **S1** — a new verb `--brief <slug> --unit <id> --path <file>` in
  `tools/unattended/unattended.sh`. It reads the brief the caller has WRITTEN and records its content
  hash, the unit id and the run label into the run-state file's parked region as a new `brief` kind.
- **S2** — the brief itself is a tracked record under `memory/builds/<slug>/prompts/`, which is where
  this memory tree already sanctions prompt-kind files. It carries the standard
  `**Serves:** journal <unit-id>` binding line, so hygiene check 21 joins it to the spec.
- **S3** — the recorded hash is over the brief FILE's bytes. Editing a brief after recording makes
  the record STALE and readable as stale, the same join `--record-piece` uses for a piece.
- **S4** — the `brief` kind is `history` class, not `surfaced`: it carries no question and no options,
  so it must not inflate the count of decisions `parked-decisions-surfaced` covers. It is added to
  the driver's `PARK_KINDS` and NOT to `PARK_KINDS_OWED`.
- **S5** — `--status` counts briefs apart from questions, as it already does for proposals.
- **S6** — the verb REFUSES a unit id that the build README's generated units region does not carry,
  and REFUSES a `--path` that is untracked. A brief naming a unit that does not exist records nothing
  about a build, and an untracked brief is not a record.
- **S7** — arms in `tools/unattended/unattended.test.sh` for each refusal and for the passing case.

## 3. Non-goals (OUT)

- The verb does not WRITE the brief's prose. Composing the brief is the orchestrator's judgement, and
  a driver that generated it would be recording its own output rather than the agent's instructions.
- No Definition-of-Done item is added here. Whether a build pass OWES a brief is
  `TOOL-dBriefedPass-3`'s refusal, and putting it in two places would be two answers to one question.
- The brief is not compared to the spec. Nothing here grades whether the instructions were GOOD or
  faithful; it records what they were.
- `memory/HYGIENE.md`'s record-binding grammar is not extended. `journal` is already the kind for
  "evidence of what was built" and a brief is exactly that.

## 4. Design

### Data model

One parked line per brief, in the run-state file's authored region:

```
- brief · <unit-id> · <sha256-12> · <repo-relative path>
```

The hash is truncated to 12 hex, the same width the piece records use, and the path is
repo-relative and forward-slashed. The line leads with the KIND and not with the id, because
protocol section 2's anchor ban refuses a dash row leading with an id — that would make this build a
claimant of every unit a brief names.

### Inventory

The existing park kinds and which class each is, read from the driver's `PARK_KINDS_OWED` and its
complement, to place the new one:

| kind | class | writer |
|---|---|---|
| `decision` | surfaced | `--park` |
| `abort` | surfaced | `--abort` |
| `override` | surfaced | `--close --override` |
| `waiver` | surfaced | `--preflight --waive` |
| `proposal` | history | `--propose` |
| `rescope` | split by act | `--rescope` |
| `dispatch` | history | `--dispatch` |
| `review` | history | `--review` |
| `brief` | history | `--brief` (this unit) |

### Alternatives rejected

- **Store the brief inline in the run-state file.** Rejected: that region is budgeted at 8 KB with a
  spill rule, and a brief is prose measured in kilobytes. It would evict parked decisions, which is
  the one thing the spill rule already refuses to do to waivers.
- **Put the brief in the spec itself, as a section.** Rejected: the spec canon is closed at ten
  sections and a spec is the unit's DESIGN, not the transcript of one attempt at it. A unit rebuilt
  twice has two briefs and one spec.
- **Derive the brief from the spec at read time.** Rejected: then it is not a record of what the
  agent was handed, it is a re-derivation, and the defect being fixed is precisely that no such
  record exists.

### Files touched (estimate)

`tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`.

## 5. Production-readiness checklist

- **Security · data · write surface** — the verb writes one line to a file the run already owns and
  reads a tracked file. No new external surface.
- **Performance** — one hash of one file per build pass.
- **Error states** — S6's two refusals, each naming what it refused and why.
- **Observability** — `--status` reports the brief count.
- **Testing** — S7.
- **Migration · rollback** — additive. A run-state file with no `brief` lines is legal and is every
  record written before this lands.

## 6. Acceptance criteria

- **AC1** — `--brief` on a tracked brief file naming a rostered unit writes exactly one `brief` line
  and exits 0; a second identical call is a no-op, matching `--park`'s exact-line idempotence.
- **AC2** — `--brief` naming a unit absent from the generated units region is REFUSED, and the
  message names the id and the region it was not found in. Observed RED before the guard exists.
- **AC3** — `--brief --path` naming an untracked file is REFUSED and says so.
- **AC4** — `parked-decisions-surfaced` with a `--value` count is UNAFFECTED by any number of brief
  lines. This is the arm that proves the `history` classification: write three briefs, attest the
  surfaced count, and `--close` must not refuse.
- **AC5** — `--status` prints the brief count separately from the decision count.
- **AC6** — in `tools/unattended/unattended.test.sh`, a brief recorded and then EDITED reports as stale, and the arm asserts the stale message
  rather than merely a non-zero exit.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · `unattended driver selftest` · `unattended kit gate` ·
`memory hygiene`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-01 · authored under the dBriefedPass mandate.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "record what an agent was handed before it built a unit"`
found no seam for a brief record; the seam this unit EXTENDS was located by reading source and is
named by path: the `--record-piece` writer in `tools/unattended/unattended.sh`, which already
hash-joins a tracked file to a record and already carries the newline, separator, bypass and
exact-line-idempotence refusals this verb needs. `--propose` is the seam for the second half — it is
the existing `history`-kind park writer and shows how a kind stays out of `PARK_KINDS_OWED`. Both are
extended rather than copied.

Recall terms used: unattended mandate pass ordering workflow harness spec before code regrounding
compaction driver orchestration agent-cap fan-out build-method handoff prompt.
