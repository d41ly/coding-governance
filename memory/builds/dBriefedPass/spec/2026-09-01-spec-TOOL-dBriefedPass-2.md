# TOOL-dBriefedPass-2 — the unit BRIEF, a tracked record of what a building agent was handed

**Status:** SPECCED · rev-3 · 2026-09-01 · node d · Tier-2 · base 269dacae · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-prompt-TOOL-dBriefedPass-1.md](../prompts/2026-09-01-prompt-TOOL-dBriefedPass-1.md) | research | TOOL-dBriefedPass-1 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5 |
| [2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round1.md](../reviews/2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round1.md) | spec-audit | TOOL-dBriefedPass-1 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5 |
| [2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round2.md](../reviews/2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round2.md) | spec-audit | TOOL-dBriefedPass-1 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5 |

<!-- /gen:spec-records -->

## 1. Goal

Make "what instructions did this agent start building with" answerable from the tree. A build pass
records the BRIEF it was handed as a tracked file joined to its unit's spec, written by a driver verb
so it cannot be composed after the fact or left out.

## 2. Scope (IN)

- **S1** — a new verb `--brief <slug> --unit <id> --path <file>` in
  `tools/unattended/unattended.sh`. It reads the brief the caller has WRITTEN and records its content
  hash and path into the run-state file's parked region as a new `brief` kind, THROUGH `park()` and
  in `park()`'s own grammar. The parked region is the store and the piece records are not: a brief is
  run-scoped evidence, and a piece record exists because a piece outlives its run.
- **S2** — the brief itself is a tracked record under `memory/builds/<slug>/prompts/`, which is where
  this memory tree already sanctions prompt-kind files. It carries the standard
  `**Serves:** journal <unit-id>` binding line, so hygiene check 21 joins it to the spec.
- **S3** — the recorded hash is over the brief FILE's bytes, and `--status` RECOMPUTES it on every
  read and prints `STALE` beside any row whose file no longer hashes to what was recorded. Naming the
  reader is the whole of this item: nothing else in this kit recomputes a hash held in a parked row,
  so without `--status` doing it the recorded hash would be decoration and the record's advertised
  property would be untrue on landing day.
- **S4** — the `brief` kind is `history` class, not `surfaced`: it carries no question and no options,
  so it must not inflate the count of decisions `parked-decisions-surfaced` covers. It is added to
  the driver's `PARK_KINDS` and NOT to `PARK_KINDS_OWED`.
- **S5** — briefs land in `--status`'s EXISTING `· noted N` aggregate and no per-kind split is
  added. `park_kinds_unowed()` at `unattended.sh:2721` derives that aggregate as `PARK_KINDS`
  minus the owed set, so adding `brief` to `PARK_KINDS` in S9 puts it there with no further
  edit. This item is therefore satisfied BY S9 and states an expected consequence rather than
  new work; at rev-2 it asked for a split the driver deliberately does not produce.
- **S6** — the verb REFUSES a unit id that the build README's generated units region does not carry,
  and REFUSES a `--path` that is untracked. A brief naming a unit that does not exist records nothing
  about a build, and an untracked brief is not a record.
- **S7** — arms in `tools/unattended/unattended.test.sh` for each refusal and for the passing case.
- **S8** — THE VERB'S THREE PROSE CARRIERS LAND IN THIS UNIT, not at order 5. Check 26 of
  `tools/unattended/check-unattended.sh:2005-2058` joins every id in `VERBS_SLUG` to the driver's own
  `#   unattended.sh <verb> ` header line, to `tools/unattended/PROTOCOL.template.md` and to
  `tools/unattended/SKILL.template.md`, and `unattended.sh:91` makes `VERBS_SLUG` membership the
  dispatch itself. The `unattended kit gate` leg carries NO `guard` key, so it runs on every bar:
  adding the verb without its carriers reds the bar at this unit and keeps it red through units 3 and
  4 until unit 5 lands. Both rendered copies are regenerated in the same commit.
- **S9** — the `brief` kind is added to `PARK_KINDS` in the same commit as the `park()` call site
  that writes one. Check 27 at `check-unattended.sh:2077-2090` fails in BOTH directions, including
  "the driver declares a parked kind that no `park()` call site ever writes".

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

One parked line per brief, written by `park()` and therefore in `park()`'s grammar. That writer is
`tools/unattended/unattended.sh:3702-3711` and its format string is
`printf '
%s %s · item %s%s · reason %s
'`, so the call and the line it produces are:

```
park "$rel" brief "<unit-id>" "<sha256-12> <repo-relative path>"
2026-09-01T12:00:00Z brief · item TOOL-dBriefedPass-1 · reason a1b2c3d4e5f6 memory/builds/…
```

`reason` is LINE-FINAL and two live readers depend on that — `recorded_waivers` takes the token
between ` · item ` and ` · reason `, and the leg's check 17 recovers an item by stripping a trailing
reason — so the hash and path ride the reason field and nothing is appended after it. The `step`
field is not used. The timestamped shape is also what the `kinds_re` counters at `:2713` and `:3553`
match. Those two counters are keyed on `PARK_KINDS_OWED`, and a brief is NOT owed, so what they do
with a brief row is NOT match it — that non-match is precisely what S4 buys, because a matched row
would inflate the count `parked-decisions-surfaced` is compared against. The reader that DOES see a
brief is `park_kinds_unowed()` at `:2721`, whose alternation feeds the `· noted N` count at `:2726`.

A dash-led row was specified at rev-1 and could not be produced by this writer, could not be matched
by any of its readers, and would itself have tripped protocol section 2's anchor ban that the same
paragraph cited.

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

`tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`, and the four carrier files
S8 requires: `tools/unattended/PROTOCOL.template.md`, `tools/unattended/SKILL.template.md`, and
their renders `memory/guides/UNATTENDED-PROTOCOL.md` and `.claude/skills/unattended/SKILL.md`. The
templates and their renders are RENDER PAIRS — editing one half alone reds the parity legs, the same
shape `TOOL-dBriefedPass-1` S6 carries for the BUILD-METHOD pair.

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
- **AC5** — with one brief and one proposal recorded, `--status`'s `· noted N` count is 2 and its
  `· parked N` count is unchanged. One arm over the aggregate S5 names, rather than the per-kind
  split rev-2 asked for and the driver does not emit.
- **AC6** — in `tools/unattended/unattended.test.sh`, a brief recorded and then EDITED makes
  `bash tools/unattended/unattended.sh --status <slug>` print `STALE` against that row, and the arm
  asserts that word beside that unit id rather than merely a non-zero exit. `--status` is named
  because it is the command S3 puts in scope to emit it; at rev-1 this criterion asserted a message
  no unit produced.
- **AC7** — `bash tools/unattended/check-unattended.sh` is GREEN with `--brief` declared, which is
  checks 26 and 27 over the new verb and the new kind, AND `bash tools/check-wiring.sh --check`
  reports the installed Skill matching tracked, which is the `unattended skill wiring` leg over the
  RENDER half of S8's carriers. Two commands, because the carriers are two template-and-render pairs
  and check 26 reads only the templates.
- **AC8** — a recorded brief moves `--status`'s `· noted` count by one and leaves `· parked`
  unchanged. That PAIR is the observation: `noted` seeing it proves `PARK_KINDS` membership took
  effect, and `parked` not moving proves the kind stayed out of `PARK_KINDS_OWED`, which is what
  keeps a brief from inflating the surfaced-decision count.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · `unattended kit gate` · `unattended skill wiring` ·
`memory hygiene`. Every name resolves against `tools/gate-legs.json`; `unattended driver selftest`
was listed at rev-2 and resolves to nothing. The driver suite `tools/unattended/unattended.test.sh`
is not on the bar by the owner's 2026-08-23 ruling, so S7's arms are witnessed by running that file
directly and the verdict is owed in the landing report.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-01 · authored under the dBriefedPass mandate.
- rev-2 · 2026-09-01 · round-1 spec-audit fold. B1 (finding 1): the verb's three check-26 carriers
  were owned by unit 5 at order 5 while the `unattended kit gate` leg is unguarded, so this unit as
  written reds the bar and keeps it red through two later units — S8 brings the carriers here, S9
  does the same for the `PARK_KINDS` half of check 27, and AC7 observes both. H3 (finding 37): the
  §4 row was a bespoke dash-led shape `park()` cannot produce and none of its readers can match; §4
  now states the call and the line, and AC8 asserts the counter regex sees it. H4 (finding 38): AC6
  asserted staleness that nothing in scope computed — `--record-piece`'s staleness is produced by
  `check-playbook.sh` over a different artifact — so S3 now names `--status` as the reader that
  recomputes the hash, and AC6 asserts that command. S1 also settles the S1-versus-S3 contradiction
  found while reading the driver during the audit: the parked region is the store, not a piece record.
- rev-3 · 2026-09-01 · round-2 spec-audit fold. H5 (finding 15): the rev-2 fix moved the carrier
  requirement into S8 and left §4 Files touched and §7 naming neither the carriers nor the
  `unattended skill wiring` leg — B3's render-pair shape, one document over. H6 (finding 12): §4
  cited `:2713` and `:3553` as the readers that see a brief row, and both are keyed on
  `PARK_KINDS_OWED`, which a brief deliberately is not in; the sentence now states what those
  counters must NOT do and names `park_kinds_unowed()` at `:2721` as the reader that does, with AC8
  following it. H10 (finding 5): S5 asked for a per-kind `--status` split the driver does not
  produce and AC5 asserted that output, so neither could fail; briefs now land in the existing
  `noted` aggregate.

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
