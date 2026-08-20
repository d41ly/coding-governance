# TOOL-dUnstalledConvoy-9 — the driver records a dispatch's declared write sets, and refuses the two disjointness conditions a machine can decide

**Status:** SPECCED · rev-2 · 2026-08-20 · node d · Tier-2 · base 2dc9df35 · streams tooling · ratified 2026-08-20

## 1. Goal

M6 requires two path lists written down before a concurrent dispatch, and nothing has ever read one.
This unit gives the declaration a verb, keys it so a later check can join it to what was committed,
and refuses at declaration time the two of M6's three conditions a machine can actually decide.

## 2. Scope (IN)

- **S1** — `--dispatch <slug> --pass <unit-id> --writes "<paths>"` records one row per concurrently
  dispatched pass, through the existing `park` helper with a new kind token `dispatch`.
- **S2** — the GROUP is the run's `HEAD` at declaration time, recorded automatically. Two passes
  declared at the same `HEAD` are one parallel group. There is no group flag, because a flag is one
  more thing to spell wrong and the anchor is already unambiguous.
- **S3** — `--pass` takes a UNIT ID, not a free label. M6 already requires the unit id in a pass's
  commit subject, so an id is the join `TOOL-dUnstalledConvoy-10` needs and a label would not be.
- **S4** — **M6 condition 1 is enforced here.** A declared path set that intersects a sibling's in the
  same group is REFUSED, naming both passes and the intersecting paths. Two passes claiming the same
  file are not disjoint, and this is decidable at declaration time.
- **S5** — **M6 condition 3 is enforced here, WITH its qualifier.** M6 names the run-state file, the
  decision log and the backlog shards outright, and names a generated index only TOGETHER WITH its
  generator. The first three are a flat refusal. A generated index is refused ONLY when the same
  declaration, or a sibling's in the same group, also names its GENERATOR. Review fold: H5. Dropping
  the qualifier refused the ORDINARY declaration: hygiene check 9 reds when the generated build index
  differs from a fresh render, so every pass touching a spec status header must regenerate and commit
  the live index, the month ledger shard and the build README region. A flat ban makes the truthful
  declaration illegal and the untruthful one redded by the sibling check, and it un-makes a retraction
  M6 records in the paragraph directly beneath the condition. S4's intersection test already catches
  two passes rendering one artifact, so the flat ban bought nothing and cost the declaration.
- **S5a** — the shared-record set is DECLARED, not guessed. Review fold: H6. `.unattended.conf` is the
  only conf this kit reads and its sole layout value is the memory root; it declares no backlog path
  and no generated-index names, `.memory-tree.conf` declares neither either, and the loader §10 once
  cited does not exist in this tree. So this unit adds one declared key listing the shared records —
  the decision log, the backlog root, the live index and the ledger root — shipped with a default and
  documented in the conf, the shipped example and the protocol's key table. An undeclared value is a
  refusal, never a guess. Hardcoding this repo's paths would be the hardcoded-prefix class this spec's
  own last line forbids, and sourcing the memory-tree conf would contradict the standalone-install
  rule the sibling unit established.
- **S6** — **M6 condition 2 is NOT enforced**, and the verb's header says so. Whether a file is a
  contract the other pass reads is a judgement about meaning, and a verb that pretended to decide it
  would be a check that cannot fail.
- **S7** — paths are repo-relative. An absolute path, a path escaping the repo with `..`, an empty
  `--writes`, and **a path containing whitespace** are each refused. Review fold: M5. The row grammar
  puts the path list in a whitespace-delimited field with no quoting defined, so a path with a space
  would word-split into two tokens naming nothing — and the sibling check's subset test would then red
  a CORRECT dispatch with a message naming paths nobody declared. This repo has hit that class twice
  already, both times as a green skip over a population of zero.
- **S9** — the Skill gains a `--dispatch` section and the protocol's verb list gains its row, both in
  SCOPE with their own criteria, and the protocol edit re-measures the read-path budget. Review fold:
  M4. The first draft edited both documents from the Files-touched table alone, so a builder could
  pass every criterion while shipping a verb neither document mentions.
- **S8** — every `verb_park` refusal is inherited verbatim, and the row is idempotent by the same
  exact-line compare.

## 3. Non-goals (OUT)

- Performing the dispatch. The verb records a declaration; the agent dispatches. Same separation as
  `TOOL-dUnstalledConvoy-5`, and for the same reason — a record derived from the act it describes is
  a summary, and gives a later check nothing independent to compare.
- Deciding condition 2. S6 is explicit.
- Bounding HOW MANY passes may be dispatched. That ceiling belongs to the review protocol and is
  enforced by the fan-out hook at the tool call. This verb bounds WHICH work, never how much.
- Refusing a dispatch of one pass. A group of one is a sequential pass that recorded its write set,
  which is harmless and occasionally useful.

## 4. Design

### Data model

```
<timestamp> dispatch · item <head-sha8> <unit-id> · reason <path> <path> ...
```

The kind token joins `decision`, `waiver`, `abort` and `rescope` in the region's existing grammar.
The `reason` field carries the declared paths, which reads oddly until stated plainly: the reason a
pass may run concurrently IS its write set, and the field is holding exactly what it is named for.

### Why the group key is HEAD and not an ordinal

An ordinal has to be chosen, and a resumed run after a compaction does not know which ordinal it was
using. `HEAD` at declaration time is derivable at any moment, is identical for two passes declared
before either commits, and changes as soon as either does — which is precisely the boundary a group
should have. It also gives `TOOL-dUnstalledConvoy-10` the commit range to search.

### Which of M6's conditions a machine can decide

| Condition | Decidable | Where |
|---|---|---|
| 1 — write sets do not intersect | yes, given two declared sets | S4, at declaration |
| 2 — neither writes a contract the other reads | **no** | S6, stated as not enforced |
| 3 — the three records M6 names outright | yes, once DECLARED | S5 and S5a |
| 3 — a generated index together with its generator | yes, and only in that pairing | S5, review fold H5 |

Condition 3's members are DECLARED by S5a, not derived and not spelled. The audit measured that the
derivation this spec first claimed has no source: `.unattended.conf` declares only the memory root,
`.memory-tree.conf` declares no backlog path and no index names, and the live index and ledger paths
are constructed inside the generator. A hardcoded prefix in a shipped tool is a recorded defect class
in this repo whose worst form lands a dead path in an adopter's tree, so the answer is a declaration
with a default rather than a constant or a guess. Review fold: H6.

### What the verb cannot buy

It refuses a DECLARATION that is self-evidently wrong. It cannot refuse a declaration that is merely
untrue — a pass declaring one path and writing three passes this verb and is caught, if at all, by
`TOOL-dUnstalledConvoy-10` comparing the declaration against the commit. The verb's header states
this, in the same terms the sibling units use, so the pair's division of labour is readable from
either end.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/unattended/unattended.sh` | `verb_dispatch`, its flag parsing, one dispatch row, the derived shared-record set |
| `tools/unattended/unattended.test.sh` | the cases in §6 and the `ARMS_FLOORS` bump per new `fail` call site |
| `.memory-tree.conf` | the `ARMS_FLOORS` entry this unit moves — a BUILD-WIDE shared write, review fold M7 |
| `tools/unattended/SKILL.template.md` and its render | one section |
| `memory/guides/UNATTENDED-PROTOCOL.md` and its template | one row in the verb list |

### Alternatives rejected

- **A `--writes` flag on an existing verb.** Rejected: no existing verb is called at dispatch time,
  and adding a flag to `--phase` would fire it on every phase move including the sequential ones.
- **Recording the declaration in the build README.** Rejected: the README is a committed artifact
  compared at BASE for authorization, and a per-dispatch append would churn the file the
  authorization comparison reads.
- **Spelling the shared-record set as a constant.** Rejected in §4, on a recorded defect class.

## 5. Production-readiness checklist

- security — S5 is the security content: it is the mechanical bar between a concurrent dispatch and
  two passes racing the decision log. The bypass-flag refusal is inherited in both fields.
- perf / scale — one append and one scan of the same file's existing rows per call.
- a11y — N/A — a shell verb with no user surface.
- i18n — N/A — the same.
- error / empty / loading states — the refusals in S4, S5, S7 and S8, each naming itself and the
  paths involved.
- observability — the rows ARE the observability, and they reach the wrap-up through M9.
- risks (concurrency, data-loss, rollback hazards) — this verb is the control FOR the concurrency
  risk. Its own writes are one append to one file.
- testing + left-shift gates — the cases in §6. Every interpolation in a `fail` message is bound to a
  name and placed after the sentence, because a positional cannot be armed.
- migration / rollback — none. Existing run-state files carry no `dispatch` rows and no run has ever
  dispatched concurrently.
- user docs — the Skill section and the protocol verb row.

## 6. Acceptance criteria

- **AC1** — `bash tools/unattended/unattended.sh --dispatch <slug> --pass <id> --writes "a/b c/d"`
  appends one row whose kind token is `dispatch` and whose item field carries the current `HEAD`
  abbreviated sha and the unit id.
- **AC2** — A second `--dispatch` at the same `HEAD` declaring a path already declared by the first
  refuses, naming both unit ids and the intersecting path.
- **AC3** — A second `--dispatch` at the same `HEAD` with a disjoint set succeeds.
- **AC4** — `--writes` naming the run-state file, the decision log, a backlog shard or a generated
  index refuses in each of those four cases, with the path named.
- **AC5** — An absolute path, a path containing `..`, and an empty `--writes` each refuse.
- **AC6** — The same invocation twice appends ONE row, matching `verb_park`'s idempotence.
- **AC7** — The shared-record set is read from the DECLARED key, observed by pointing a fixture's
  conf at different backlog and index names and seeing the refusal name THOSE paths, not this repo's,
  observed in `tools/unattended/unattended.test.sh`. Review fold: H6.
- **AC9** — A declaration naming a generated index ALONE is ACCEPTED; the same index named together
  with its generator, in the same declaration or a sibling's, is REFUSED. Both observed in
  `tools/unattended/unattended.test.sh`. Review fold: H5, so the retraction cannot be un-made later.
- **AC10** — A declared path containing a space is refused, observed in
  `tools/unattended/unattended.test.sh`. Review fold: M5.
- **AC11** — `grep` finds `--dispatch` in the rendered `.claude/skills/unattended/SKILL.md` and in the
  verb list of `memory/guides/UNATTENDED-PROTOCOL.md`, and
  `bash tools/unattended/adopt-unattended.sh --target . --check` exits 0. Review fold: M4, H13.
- **AC12** — The new conf key appears in `.unattended.conf`, in
  `tools/unattended/.unattended.conf.example` and in the protocol's key table, each asserted
  separately rather than through a pairing check that does not exist. Review fold: H6, M9.
- **AC13** — The verb's header STATES what it cannot buy, observed by `grep` over
  `tools/unattended/unattended.sh`. Review fold: L1.
- **AC8** — Each new refusal is observed RED against a fixture before the unit lands, observed in `tools/unattended/unattended.test.sh`.

## 7. Gates

`unattended driver selftest` · `unattended kit gate` · `unattended skill wiring` · `harness arms` ·
`memory-tree hygiene` (check 16, the read path) · the full bar at the push boundary. `ARMS_FLOORS`
moves for `tools/unattended/unattended.sh`, and that constant lives in `.memory-tree.conf`, which is
therefore in this unit's write set. Review fold: M4, M7, H13.

## 8. Open questions

- **F1 — RESOLVED (agent, 2026-08-20, delegated): do NOT refuse outside `BUILDING`. The spec-audit fan this repo already performs is a concurrent dispatch during `SPECCING`, so refusing there would forbid the one parallel dispatch in daily use. The phase is RECORDED in the row instead, so the wrap-up can tell a spec-audit fan from a build fan without the verb policing the difference.**

  The question this settles: should the verb refuse when the current phase is not `BUILDING`? A dispatch during
  `SPECCING` is legitimate — M6's pass set includes "a spec authored" and "a spec reviewed", and M4
  already dispatches spec audits concurrently. Refusing outside `BUILDING` would forbid the one
  concurrent dispatch this repo already performs. **Recommendation: do not refuse.** Record the phase
  in the row instead, so the wrap-up can tell a spec-audit fan from a build fan without the verb
  having to police the difference.

## 9. Revision log

- rev-2 · 2026-08-20 · folded the spec audit: H5 (M6 condition 3 keeps its together-with-its-generator
  qualifier), H6 (the shared-record set becomes a DECLARED conf key — the derivation seam cited did
  not exist), M5 (a whitespace-bearing path is refused), M4 (the Skill section and protocol verb row
  promoted into scope), M7, M9, L1. Seven new criteria.
- rev-1 · 2026-08-20 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "declare the paths a build pass will write before
dispatching it"` returns the `unattended` affordance seam and `agent-cap.topLevelArgs`, the latter
bounding the fan-out this declaration accompanies but not overlapping it. The seams extended are the
`park` helper and its kind token, and the memory-tree conf loader that already resolves the memory
root and the backlog location for other checks.

`python tools/memory-recall/query.py "what makes two build passes safe to run at the same time and
which of those conditions can a program decide" --terms "M6 write set disjoint condition shared
mutable record decision log backlog generated index contract dispatch declaration"` returns the
record correcting M6's condition 3, the parallelism verdict, and the hardcoded-prefix defect class
that S5's derivation avoids. All three were read; the first is why S4 and S5 quote conditions 1 and
3 rather than restating them in the verb's own words.

Recall terms used: M6 write set disjoint condition shared mutable record decision log backlog
generated index contract dispatch declaration.
