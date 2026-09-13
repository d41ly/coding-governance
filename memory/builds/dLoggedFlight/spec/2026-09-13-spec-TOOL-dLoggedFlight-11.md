# TOOL-dLoggedFlight-11 — the unattended Skill renders the record at abort and after landing, and the keepalive becomes a heartbeat

**Status:** SPECCED · rev-1 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

A record nobody renders is a record nobody has. Put the render into the unattended Skill at the three
points a run ends: after `--abort`, after `--landed`, and, for a run that lands without the lander,
after `--close`. Place it where it can never wedge the landing check. And make every keepalive fire
leave a heartbeat line, so a stalled run is visible in its journal.

## 2. Scope (IN)

- **S1** A new conf key, `RUNLOG_CLI`, following the `RECALL_CLI` precedent. It names the runlog CLI's
  repo-relative invocation, and blank turns the render steps off. It is rendered into the Skill as a
  placeholder, so the Skill TEMPLATE names no other kit by literal. Observed by AC1.
- **S2** A Skill section, "Record the run". Observed by AC2. It covers:
  - rendering with `record <slug> --write`;
  - re-rendering the build index and staging what it touched;
  - committing with a subject that names the slug and no unit id, in three placements:
    - after `--abort`, in the ABORTED record commit;
    - after `--landed`, in the LANDED record commit the Skill already requires;
    - where the run lands without the lander, after `--close` and before the merge.
  - It states that a commit between the lander's push and `--landed` wedges check 34, and that the
    render never goes there.
- **S3** The keepalive section tells the scheduled job's prompt to run `--status <slug>` first once a
  slug exists, so each fire leaves a heartbeat in `driver.log`. Observed by AC3.
- **S4** The protocol's section 2 run-log paragraph from `TOOL-dLoggedFlight-2` gains one sentence
  saying where the record is rendered. Section 8 gains the `RUNLOG_CLI` row. Both go into the
  template and its installed copy, within the 3,625 bytes of headroom. Observed by AC4.
- **S5** This run renders and commits its own record by the landing-without-lander placement, and the
  schema leg of `TOOL-dLoggedFlight-10` grades it at the push. Observed by AC5.

## 3. Non-goals (OUT)

- A Definition-of-Done item for the record. It is circular inside `--close` and overridable, and a
  core item raises the floor for every adopter; the research record says so.
- Rendering from a hook. The render is an agent act at a named point, like every other close step.
- Changing any verb.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-9` — the `record` command and the index follow-up it prints.

## 4. Design

The placements follow the landing rule measured by the kit-fit review. A commit after `--close` and
before the lander's push is legal. A commit between the push and `--landed` fails check 34. A commit
after `--landed` is the established record commit. The render rides the commit each path already
makes, so no path gains a commit it did not have.

The Skill's keepalive section prescribes no job prompt today. The heartbeat sentence is the first, and
it is phrased so a prompt-mode run, which has no slug when it schedules, runs `--status` only once
preflight has minted one.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `RUNLOG_CLI` | conf key, rendered placeholder `{{RUNLOG_CLI}}` | protocol section 8 |

### Files touched (estimate)

`tools/unattended/{SKILL.template.md,PROTOCOL.template.md,.unattended.conf.example,adopt-unattended.sh,kit.toml}`,
`.unattended.conf`, `.claude/skills/unattended/SKILL.md`, `memory/guides/UNATTENDED-PROTOCOL.md`, and
this build's own record.

### Alternatives rejected

- Rendering inside `--close`: rejected, since the driver would then need the runlog kit, and a verb
  may not read a log it would then be judged by.

## 5. Production-readiness checklist

- security — the render step writes only the closed-schema record.
- perf / scale — one render and one index re-render per run end; seconds.
- error / empty / loading states — a blank `RUNLOG_CLI` skips the section and the Skill says so. A run
  with no spec-defined unit gets the `record` command's own no-record line.
- observability — the heartbeat lines, and the record itself.
- risks — a Skill step is followed, not enforced. The schema leg catches a malformed record, and
  nothing catches a missing one. `TOOL-dLoggedFlight-13` reports runs left non-terminal, which is
  where a skipped render is likeliest.
- testing — the skill-wiring leg's byte comparison, the kit gate's key join, and this run's own
  record as the end-to-end observation.
- migration — adopters get the section with `RUNLOG_CLI` blank, so it is inert until they declare it.
- user docs — the Skill itself.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/adopt-unattended.sh --check` runs, the rendered
  `.claude/skills/unattended/SKILL.md` carries the `RUNLOG_CLI` value this repo declares, and no
  surviving placeholder brace.
  Red when: the placeholder is not in `render()` or kit.toml's list.
- **AC2** — When `grep -n 'Record the run' .claude/skills/unattended/SKILL.md` runs, the section is
  present and names all three placements and the check 34 warning.
  Red when: a placement or the warning is missing.
- **AC3** — When the keepalive section of `tools/unattended/SKILL.template.md` is read, it tells the
  job's prompt to run `--status <slug>` once a slug exists.
  Red when: the sentence is absent from the rendered copy.
- **AC4** — When `bash tools/unattended/check-unattended.sh` runs, check 22 accepts `RUNLOG_CLI` and
  check 10 finds the protocol copy byte-identical to its template.
  Red when: the section 8 row or the example line is missing.
- **AC5** — When the push boundary's bar runs on this build's landing, the `runlog record schema` leg
  grades one record, this run's own, and passes.
  Red when: the run lands with no record, or with one the leg refuses.
  cost: the full bar at the push boundary.

## 7. Gates

`unattended skill wiring` · `unattended kit gate` · `kit version markers` · `memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

The seam is the Skill's existing Close, Land, Mark it landed and If it cannot finish sections, at
`tools/unattended/SKILL.template.md:688-808`, and its render, which substitutes the conf's declared
placeholders. The `RECALL_CLI` and `MAP_CLI` keys are the precedent for naming a sibling kit's CLI
through a declaration rather than a literal. `tools/codebase-map/reuse_lookup.py` cannot see the
Skill's prose.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
