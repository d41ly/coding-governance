# TOOL-dLoggedFlight-11 — the unattended Skill renders the record at abort and after landing, and the keepalive becomes a heartbeat

**Status:** SPECCED · rev-2 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

A record nobody renders is a record nobody has. Put the render into the unattended Skill at the three
points a run ends: after `--abort`, after `--landed`, and, for a run whose record stays at LANDING,
after `--close`. Place it where it can never wedge the landing check. And make every keepalive fire
leave a heartbeat line, so a stalled run is visible in its journal.

## 2. Scope (IN)

- **S1** A new optional conf key, `RUNLOG_CLI`, naming the runlog CLI's repo-relative invocation. It
  follows the `RECALL_CLI` and `MAP_CLI` precedent exactly: a declared value the agent reads at run
  time, and NOT a rendered placeholder. So `render()` in `tools/unattended/adopt-unattended.sh` is
  unchanged, and an adopter who declares nothing gets a Skill that says to skip the section. It is
  documented by a protocol section 8 row and an example line. Observed by AC1 and AC4.
- **S2** A Skill section, "Record the run". Observed by AC2. It tells the agent:
  - where `.unattended.conf` declares `RUNLOG_CLI`, to render with `<RUNLOG_CLI> record <slug> --write`,
    re-render the build index, stage what both touched, and commit with a subject that names the slug
    and no unit id;
  - to do that in one of three places:
    - after `--abort`, in the ABORTED record commit;
    - after `--landed`, in the LANDED record commit the Skill already requires;
    - where the run's record stays at LANDING, after `--close` and before the merge;
  - that a commit between the lander's push and `--landed` wedges check 34, so the render never goes
    there;
  - where no `RUNLOG_CLI` is declared, to skip the section.
- **S3** The keepalive section tells the scheduled job's prompt to run `--status <slug>` first once a
  slug exists, so each fire leaves a heartbeat in `driver.log`. Observed by AC3.
- **S4** The protocol's section 2 run-log paragraph from `TOOL-dLoggedFlight-2` gains one sentence
  saying where the record is rendered. Section 8 gains the `RUNLOG_CLI` row. Both go into the
  template and its installed copy, within the 3,625 bytes of headroom. Observed by AC4.
- **S5** This run renders and commits its own record. Its key is `2f11f32d`, the commit that created
  its run-state file. The `runlog record schema` leg of `TOOL-dLoggedFlight-10` grades that record on
  the merged tree BEFORE the push, run directly, and the full bar runs there as well. Observed by AC5.
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
- Changing any verb, and changing `render()`.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-2` — the protocol section 2 paragraph this unit extends.
- **consumes-from** `TOOL-dLoggedFlight-9` — the `record` command and the index follow-up it prints.
- **consumes-from** `TOOL-dLoggedFlight-10` — the schema leg that grades this run's own record.

## 4. Design

The placements follow the landing rule measured by the kit-fit review. A commit after `--close` and
before the lander's push is legal. A commit between the push and `--landed` fails check 34. A commit
after `--landed` is the established record commit. The render rides the commit each path already
makes, so no path gains a commit it did not have.

A rendered placeholder was rejected. `render()` substitutes only `KIT_DIR`, `TOOL_ROOT`, `MEMORY_ROOT`,
`LANDER`, the keepalive keys, `ANCHOR_SCOPE` and `AUTH_PARAM`. A blank rendered key would print an
empty command span to every adopter who has no runlog kit, the failure TOOL-aWrittenMethod-1 records.
Reading the declared value at run time, as the Skill already does for the recall and map CLIs, has
no such failure.

The Skill's keepalive section prescribes no job prompt today. The heartbeat sentence is the first, and
it is phrased so a prompt-mode run, which has no slug when it schedules, runs `--status` only once
preflight has minted one.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `RUNLOG_CLI` | optional conf key, read by the agent | protocol section 8 |

### Files touched (estimate)

`tools/unattended/{SKILL.template.md,PROTOCOL.template.md,.unattended.conf.example}`, `.unattended.conf`,
`.claude/skills/unattended/SKILL.md`, `memory/guides/UNATTENDED-PROTOCOL.md`,
`memory/builds/dLoggedFlight/README.md`, and this build's own record.

### Alternatives rejected

- Landing with `--no-verify` or a hand-made lander marker: rejected. The first is banned by protocol
  section 6 and `BYPASS_BAN`. The second manufactures the evidence the hook exists to observe.

## 5. Production-readiness checklist

- security — the render step writes only the closed-schema record.
- perf / scale — one render and one index re-render per run end; seconds.
- error / empty / loading states — an undeclared `RUNLOG_CLI` skips the section and the Skill says so.
  A run with no spec-defined unit gets the `record` command's own no-record line.
- observability — the heartbeat lines, and the record itself.
- risks — a Skill step is followed, not enforced. The schema leg catches a malformed record, and
  nothing catches a missing one. `TOOL-dLoggedFlight-13` reports runs left non-terminal, which is
  where a skipped render is likeliest.
- testing — the skill-wiring leg's byte comparison, the kit gate's key join, and this run's own
  record graded before its landing.
- migration — adopters get the section with no `RUNLOG_CLI`, so it is inert until they declare one.
- user docs — the Skill itself.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/adopt-unattended.sh --check` runs, it is green with no new
  placeholder, and the rendered `.claude/skills/unattended/SKILL.md` names `RUNLOG_CLI` as a declared
  value to read, not as a brace.
  Red when: the key is rendered, or the render drifts.
- **AC2** — When `grep -n 'Record the run' .claude/skills/unattended/SKILL.md` runs, the section is
  present and names all three placements, the check 34 warning and the skip when nothing is declared.
  Red when: a placement, the warning or the skip is missing.
- **AC3** — When the keepalive section of `tools/unattended/SKILL.template.md` is read, it tells the
  job's prompt to run `--status <slug>` once a slug exists.
  Red when: the sentence is absent from the rendered copy.
- **AC4** — When `bash tools/unattended/check-unattended.sh` runs, check 22 accepts `RUNLOG_CLI` and
  check 10 finds the protocol copy byte-identical to its template.
  Red when: the section 8 row or the example line is missing.
- **AC5** — When `python <kit>/runlog.py check-records` runs on the merged tree before the push,
  it grades this run's own record, keyed `2f11f32d`, and exits 0, and the full bar on that tree is
  green.
  Red when: the run reaches its landing with no record, or with one the leg refuses.
  cost: the full bar on the merged tree.
  fixture: `<kit>` is `tools/runlog`, which does not exist until unit 1 lands; this criterion is
  observed at the end of the build.
- **AC6** — When the build lands, `git log` on `main` shows a `--no-ff` merge of the run branch pushed
  by `tools/push-main.sh`, and the build README's landing rule names the route taken. If the primary
  tree was busy, the run-state file carries a parked decision instead.
  Red when: the push used `--no-verify` or a hand-made marker.

## 7. Gates

`unattended skill wiring` · `unattended kit gate` · `kit version markers` · `memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · S1 S2 S5 S6 · §4 · AC1 AC2 AC5 AC6 · folded round-1 spec audit M19
  (`RUNLOG_CLI` becomes an optional key the agent reads, as `RECALL_CLI` is, so `render()` gains no
  blank placeholder), B2 (this run's record is keyed by its run-state file's creating commit), M20 (the
  schema leg and the bar are observed on the merged tree before the push, and the landing route moves to
  the protocol's lander because the hook refuses a raw worktree push) and L2 (the edges to units 2 and
  10).

## 10. Reuse audit

The seam is the Skill's existing Close, Land, Mark it landed and If it cannot finish sections, at
`tools/unattended/SKILL.template.md:688-808`. The `RECALL_CLI` and `MAP_CLI` keys are the precedent
for naming a sibling kit's CLI through a declaration rather than a literal.
`tools/codebase-map/reuse_lookup.py` cannot see the Skill's prose.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
