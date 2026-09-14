# TOOL-dLoggedFlight-11 — the unattended Skill renders the record at abort and after landing, and the keepalive becomes a heartbeat

**Status:** CLOSED · rev-5 · 2026-09-14 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-14-build-TOOL-dLoggedFlight-11-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-dLoggedFlight-11-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md](../prompts/2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md) | journal | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

A record nobody renders is a record nobody has. Put the render into the unattended Skill at the points
a run ends, where it rides a commit the run already makes and can never wedge the landing check. And
make every keepalive fire leave a heartbeat line, so a stalled run is visible in its journal.

## 2. Scope (IN)

- **S1** The Skill names the runlog CLI through the render token it already uses for a sibling kit,
  `{{TOOL_ROOT}}`, as it names `{{TOOL_ROOT}}workflows/unattended-build.js` at
  `tools/unattended/SKILL.template.md:558`. The section tells the agent to run the step where
  `{{TOOL_ROOT}}runlog/runlog.py` exists in the repository, and to skip it where it does not. No conf
  key and no `render()` change are added, so an adopter without the runlog kit gets a Skill whose
  section announces the skip. Observed by AC1.
- **S2** A Skill section, "Record the run". It gives three placements, each riding a commit the run
  already makes. Observed by AC2.
  - After `--abort`: render, re-index and stage, in the ABORTED record commit.
  - Every run that lands: render after `--close` and before the merge, in the close's records commit,
    so the record travels with the merge and the push-boundary bar grades it.
  - After `--landed`: re-render into the SAME file, which `record --write` finds by its runkey, in the
    LANDED record commit the Skill already requires. The landing push is made from the primary tree and
    joins this run by what it pushed (`TOOL-dLoggedFlight-8` S3), so the record gains the landing push
    and the landing bar's verdict.

  Each render is followed by the build-index re-render and a commit subject naming the slug and no unit
  id. The section states that a commit between the lander's push and `--landed` wedges check 34, so no
  render goes there.
- **S3** The keepalive section tells the scheduled job's prompt to run `--status <slug>` first once a
  slug exists, so each fire leaves a heartbeat in `driver.log`. The Resume section, which the
  keepalive section says it does not bind, gives the replacement job it schedules the same prompt.
  Observed by AC3.
- **S4** The protocol's section 2 run-log paragraph from `TOOL-dLoggedFlight-2` gains one sentence
  saying where the record is rendered, in the template and its installed copy, within the headroom
  `GUIDE_CAP_BYTES` leaves: 2,281 bytes at `9d1c87b9`, because unit 2's paragraph spent part of the
  3,625 this spec was written against. Observed by AC4.
- **S5** This run renders its own record at the second placement, after `--close` and before the
  merge, keyed `2f11f32d`, the commit that started its run. The `runlog record schema` leg of
  `TOOL-dLoggedFlight-10` grades that record on the merged tree BEFORE the push, run directly, and the
  full bar runs there as well. After `--landed`, the record is re-rendered into the same file. Observed
  by AC5.
- **S6** The landing route this build takes. The pre-push hook refuses a raw default-branch push that
  lacks the lander's marker (`.githooks/pre-push:157-160`, since TOOL-aLeasedGauntlet-1). It also
  refuses a push whose tree is not the pushed tip. So a push from this worktree's detached head,
  the route approved on 2026-09-13, cannot run without a bypass, and the protocol bans the bypass. The
  build therefore lands through the protocol's own route. It merges into `main` in the primary tree
  and runs `tools/push-main.sh` there, when that tree is idle and on `main`, and then runs `--landed`.
  If the primary tree is busy, the landing is parked, not forced. The build README records the change.
  Observed by AC6.

## 3. Non-goals (OUT)

- A Definition-of-Done item for the record. It is circular inside `--close` and overridable, and a
  core item raises the floor for every adopter; the research record says so.
- Rendering from a hook, and rendering from any driver verb: a verb may not read a log it would then
  be judged by.
- Changing any verb, `render()` or `.unattended.conf`.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-2` — the protocol section 2 paragraph this unit extends.
- **consumes-from** `TOOL-dLoggedFlight-8` — the push join by what was pushed, which lets the re-render
  after `--landed` see the landing push.
- **consumes-from** `TOOL-dLoggedFlight-9` — the `record` command, its re-render by runkey and the index
  follow-up it prints.
- **consumes-from** `TOOL-dLoggedFlight-10` — the schema leg that grades this run's own record.

## 4. Design

The placements follow the landing rule measured by the kit-fit review. A commit after `--close` and
before the lander's push is legal. A commit between the push and `--landed` fails check 34. A commit
after `--landed` is the established record commit. The render rides the commit each path already
makes, so no path gains a commit it did not have. Rendering every landing run before the merge is what
lets the push-boundary bar grade the record, and the re-render after `--landed` adds only the landing
facts to the same file.

A conf key was considered and rejected twice. A rendered placeholder would print an empty command span
to every adopter with no runlog kit, the failure TOOL-aWrittenMethod-1 records. An agent-read key has
no precedent in the Skill: the recall and map CLIs are read by the driver alone. The existing
`{{TOOL_ROOT}}` token plus an existence test needs neither.

The Skill's keepalive section prescribes no job prompt today. The heartbeat sentence is the first, and
it is phrased so a prompt-mode run, which has no slug when it schedules, runs `--status` only once
preflight has minted one. A resumed session schedules a replacement job under a section the keepalive
section names as outside its reach, so Resume carries the same instruction in one sentence. Without
it the heartbeat would stop at the first resume, and a resumed run is the longest-lived kind.

The section sits between Close and Land. The placement every landing run takes falls there in reading
order. The Mark it landed and If it cannot finish sections each carry a one-line pointer to it,
because an agent follows the verb sections in order and would otherwise read the other two placements
only after the commit each one rides.

### Files touched (estimate)

`tools/unattended/{SKILL.template.md,PROTOCOL.template.md}`, `.claude/skills/unattended/SKILL.md`,
`memory/guides/UNATTENDED-PROTOCOL.md`, `memory/builds/dLoggedFlight/README.md`, and this build's own
record.

### Alternatives rejected

- Landing with `--no-verify` or a hand-made lander marker: rejected. The first is banned by protocol
  section 6 and `BYPASS_BAN`. The second manufactures the evidence the hook exists to observe.
- A `RUNLOG_CLI` conf key, rendered or agent-read: rejected in §4.

## 5. Production-readiness checklist

- security — the render step writes only the closed-schema record.
- perf / scale — one render and one index re-render per placement; seconds.
- error / empty / loading states — a repository without the runlog CLI skips the section and the Skill
  says so. A run with no spec-defined unit gets the `record` command's own no-record line.
- observability — the heartbeat lines, and the record itself.
- risks — a Skill step is followed, not enforced. The schema leg catches a malformed record, and
  nothing catches a missing one. `TOOL-dLoggedFlight-13` reports runs left non-terminal, which is
  where a skipped render is likeliest.
- testing — the skill-wiring leg's byte comparison, anchored presence greps, and this run's own record
  graded before its landing.
- migration — adopters get the section on their next unattended update, inert until the runlog kit is
  present.
- user docs — the Skill itself.

## 6. Acceptance criteria

`<kit>` below is `tools/runlog`, named in placeholder form because it does not exist until unit 1 lands.

- **AC1** — When `bash tools/unattended/adopt-unattended.sh --check` runs, it is green with no new
  placeholder, and the rendered `.claude/skills/unattended/SKILL.md` names the runlog CLI through the
  rendered `{{TOOL_ROOT}}` value with an existence test and a stated skip.
  Red when: a conf key is introduced, a brace survives, or the render drifts.
- **AC2** — When `grep -n 'Record the run' .claude/skills/unattended/SKILL.md` runs, the section is
  present and names all three placements, the re-render into the same file, and the check 34 warning.
  Red when: a placement, the same-file rule or the warning is missing.
- **AC3** — When the keepalive section of `tools/unattended/SKILL.template.md` is read, it tells the
  job's prompt to run `--status <slug>` once a slug exists, and the Resume section gives its
  replacement job the same prompt.
  Red when: the sentence is absent from the rendered copy, or Resume's replacement job carries none.
- **AC4** — When `grep -n` searches `memory/guides/UNATTENDED-PROTOCOL.md` for the render sentence this
  unit adds to the section 2 run-log paragraph, it finds it, and check 10 of
  `tools/unattended/check-unattended.sh` finds the copy byte-identical to its template.
  Red when: the sentence is absent from both copies, which byte identity alone would pass.
- **AC5** — When `python <kit>/runlog.py check-records` runs on the merged tree before the push, it
  grades this run's own record, keyed `2f11f32d`, and exits 0, and the full bar on that tree is green.
  Red when: the run reaches its landing with no record, or with one the leg refuses.
  cost: the full bar on the merged tree.
  fixture: this criterion is observed at the end of the build.
- **AC6** — When the build lands, `pushes.log` in the primary clone's common dir holds a START with
  `lander=1` naming the merge commit's sha, and an END with `decision=full` or `decision=scoped` and
  `rc=0`. The build README's landing rule names the route taken. If the primary tree was busy, the
  run-state file carries a parked decision instead.
  Red when: no push line exists for the merge sha, which is the `--no-verify` signature. A hand-made
  marker cannot be told apart in `pushes.log`, and this criterion says so rather than claiming it.

## 7. Gates

`unattended skill wiring` · `unattended kit gate` · `kit version markers` · `memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · S1 S2 S5 S6 · §4 · AC1 AC2 AC5 AC6 · folded round-1 spec audit M19, B2, M20 and L2.
- rev-3 · 2026-09-13 · S1 S2 S4 S5 · §4 · AC1 AC2 AC4 AC6 · folded round-2 spec audit H5 (no conf key:
  the Skill names the CLI through the existing `{{TOOL_ROOT}}` token, and the false recall-CLI
  precedent is struck), H2 (every landing run renders before the merge and re-renders into the same
  file after `--landed`, which is the placement this run takes), M11 (the landing is observed in
  `pushes.log`, which can tell a bypass apart) and M13 (an anchored presence grep for the protocol
  sentence).
- rev-4 · 2026-09-13 · S2 · folded round-3 spec audit H3: the landing push from the primary tree joins
  this run through unit 8's push join, which the third placement relies on.
- rev-5 · 2026-09-14 · S3 S4 · §4 · AC3 · the build pass, before its code. S3 reaches the Resume
  section's replacement job, because the keepalive section says it does not bind that path and a
  heartbeat that stops at the first resume leaves the longest-lived jobs silent. S4's headroom figure
  is re-measured, since unit 2 spent part of it. §4 places the section between Close and Land, with a
  pointer from each of the two later placements.

## 10. Reuse audit

The seam is the Skill's existing Close, Land, Mark it landed and If it cannot finish sections, at
`tools/unattended/SKILL.template.md:688-808`, and its existing `{{TOOL_ROOT}}` naming of a sibling kit
at `:558`. `tools/codebase-map/reuse_lookup.py` cannot see the Skill's prose.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
