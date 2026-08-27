# TOOL-aPrimedKeepalive-1 — the keepalive is scheduled as the run's FIRST act, on every start path

**Status:** INPROGRESS · rev-4 · 2026-08-27 · node a · Tier-2 · base b4e1d5be · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md](../build/2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md) | journal | TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 TOOL-aPrimedKeepalive-8 TOOL-aPrimedKeepalive-9 |
| [2026-08-27-prompt-TOOL-aPrimedKeepalive-1-1.md](../prompts/2026-08-27-prompt-TOOL-aPrimedKeepalive-1-1.md) | research | TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 |
| [2026-08-27-review-TOOL-aPrimedKeepalive-1-6-spec-audit-round1.md](../reviews/2026-08-27-review-TOOL-aPrimedKeepalive-1-6-spec-audit-round1.md) | spec-audit | TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 |
| [2026-08-27-review-TOOL-aPrimedKeepalive-1-7-spec-audit-round2.md](../reviews/2026-08-27-review-TOOL-aPrimedKeepalive-1-7-spec-audit-round2.md) | spec-audit | TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 |
| [2026-08-27-review-TOOL-aPrimedKeepalive-1-7-spec-audit-round3.md](../reviews/2026-08-27-review-TOOL-aPrimedKeepalive-1-7-spec-audit-round3.md) | spec-audit | TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 |

<!-- /gen:spec-records -->

## 1. Goal

Three of the kit's four start paths orient, research and decide before they ever schedule a
keepalive, so the longest unattended stretch a run has is also the one stretch nothing can wake it
from. Move the obligation to the run's first act and state it once, where every path reaches it.

## 2. Scope (IN)

- **S1** — `tools/unattended/PROTOCOL.template.md` section 5 states the obligation as the run's FIRST
  act, before any orientation and before `--preflight`, on every start path — replacing *"before the
  run leaves `PREFLIGHT`"*, which is satisfied by scheduling at preflight time.
- **S2** — the same section states the ORPHAN duty: a start path that refuses before a run exists
  still owes the reap, because the store is session-scoped and a job left by a run that never began
  is orphaned exactly like one left by a run that ended.
- **S3** — `tools/unattended/SKILL.template.md` hoists the keepalive out of the slug path's step 3
  into a section that binds all four paths, placed BEFORE the path-routing table so no path can be
  entered without passing it. **`## Resume` is a FIFTH path and the section names it explicitly**: a
  resumed session's keepalive is presumed alive, not dead. `TOOL-aPromptedMandate-11` MEASURED the
  opposite of the intuition — a run asserted twice that two jobs died with their processes and the
  scheduler's own listing showed both still firing — so Resume REAPS the recorded id first, reads the
  result back, and only then schedules a replacement. "Every path" meaning "the four rows of the routing table"
  was the first draft's silent definition and it missed the only path where the job is provably gone.
- **S4** — the slug path's numbered steps are renumbered around the removal, and the two paths that
  reach preflight through "exactly as the slug path does" are checked to make sure that phrase now
  carries what it claims.
- **S5** — `memory/guides/BUILD-METHOD.md` M10's keepalive bullet stops saying "Create it before
  preflight", which reads as "immediately before preflight". It remains a POINTER at protocol §5 and
  gains no rule of its own — M1 forbids a rule stated both there and in a carrier it points at.
- **S6** — both rendered halves are regenerated in the same commit: `memory/guides/UNATTENDED-PROTOCOL.md`
  and `.claude/skills/unattended/SKILL.md`, each of which a leg byte-compares against its template.
- **S7** — `memory/guides/SESSION-KICKOFF.md` is a FOURTH carrier, not a bookkeeping afterthought:
  the charter's Definition of Done obliges a manifest update when a unit changes a governing doc, and
  the manifest is byte-capped at 25 600 by `skills/session-kickoff/manifest-check.sh`, whose refusal
  text says the limit is trimmed against and never raised. The §B bullet this build adds is priced
  against that cap and pays for itself by trimming its own first draft.

## 3. Non-goals (OUT)

- Any driver change. `--preflight` already refuses without `--keepalive-id`, which is the machine
  half and is correct; what is missing is when the agent is told to create it.
- Making the driver schedule or reap. Protocol §5 states why it cannot: the store is in-memory and
  session-scoped, and a verb claiming that effect would be claiming one it cannot produce.
- The keepalive CADENCE. `KEEPALIVE_INTERVAL` already declares it and this unit does not touch it.
- A machine check that the agent actually scheduled one before orienting. Nothing in this kit
  observes an agent's tool calls, and a check that cannot see its subject is worse than a rule that
  says so — recorded as an accepted gap, not an oversight.

## 4. Design

### The defect, verified at BASE

`SKILL.template.md:134` is the only place the keepalive is scheduled, and it is step 3 of the slug
path. The PROMPT path's steps run orient → decide-whether-to-ask → write the build folder → commit
and push → *"Preflight, exactly as the slug path does"*. The PLAYBOOK path has the same shape. That
phrase resolves to the slug path's step 4, so the step 3 before it is never reached by either.

`PROTOCOL.template.md` section 5 makes the same error in the contract: *"The **agent** schedules the
keepalive before the run leaves `PREFLIGHT`."* A run enters `PREFLIGHT` only when `--preflight`
writes that phase, so the sentence is true of a run that schedules at preflight time — and M12's
research-then-test loop, which the prompt path is obliged to run, happens before that instant.

### Where the rule goes

ONE statement in the protocol, ONE render of it in the Skill placed before the routing table. The
Skill's four paths already share nothing else, which is why the obligation went missing from three of
them: a step written inside one path is a step the other three do not execute. Hoisting it above the
table makes "every path" structural instead of remembered.

### The orphan duty

A start path can refuse after the keepalive exists: the `--prompt` value may not resolve, the anchor
scope may not be `published`, preflight may refuse on a dirty tree. Today the Skill's refusal
branches say "stop" with no mention of the job. Scheduling first makes that reachable, so the
obligation is stated in the same section rather than discovered later.

### Files touched (estimate)

`tools/unattended/PROTOCOL.template.md` · `tools/unattended/SKILL.template.md` ·
`tools/memory-tree/BUILD-METHOD.template.md` · the three installed copies each of those renders to ·
and `memory/guides/SESSION-KICKOFF.md`, the fourth carrier S7 adds. No script changes.

**The BUILD-METHOD pair has TWO capped halves and the TEMPLATE is the tighter one.** The render
substitution shrinks the file by 11 B, so a criterion grading only `memory/guides/BUILD-METHOD.md`
prices the looser half and passes over a breached constraint. That is exactly what happened: at one
point the guide read 24 573 and the template 24 584, 8 B over a budget this run may not raise.

### Alternatives rejected

**Repeat the step in each of the four paths.** Four copies of one rule, and the defect being fixed is
that one of four copies went missing. Rejected on the kit's own pointer-not-copy design.

**Make `--preflight` refuse when the keepalive id was created after the run's first commit.** The
driver cannot see when a cron job was created; the id is an opaque string it records. A check that
cannot observe its subject would be an assertion about nothing.

## 5. Production-readiness checklist

- security — N/A. No new surface; the keepalive is a local scheduler entry.
- perf / scale — N/A.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the orphan duty (S2) IS the error state, and it is specified.
- observability — the run-state file already records the keepalive id at preflight; unchanged.
- risks — the rule moves earlier, so a run that refuses at a start path now holds a job it must
  reap. S2 covers it. No concurrency or data-loss surface.
- testing + left-shift gates — the two byte-comparing parity legs cover the renders. The rule itself
  is prose an agent reads and has no machine half, stated in §3 as an accepted gap.
- migration / rollback — documentation only; revert is the rollback.
- user docs — the Skill IS the user doc, and it is in scope.

## 6. Acceptance criteria

- **AC1** — When `memory/guides/UNATTENDED-PROTOCOL.md` section 5 is read, it obliges the agent to
  schedule the keepalive as the run's FIRST act on every start path, and the only surviving
  occurrence of `before the run leaves` is the bullet that names that wording as SUPERSEDED and says
  why it was the weaker claim.
- **AC2** — When `.claude/skills/unattended/SKILL.md` is read, the keepalive instruction appears
  ABOVE the `## Which path` routing table, and `grep -n` places its line number below that heading's
  for no path section.
- **AC3** — When `.claude/skills/unattended/SKILL.md` is read, the slug path's numbered steps run
  0,1,2,3,4 with no gap and no duplicate, and `grep -c "Schedule the keepalive yourself"` inside any
  path body returns 0.
- **AC4** — When `bash tools/unattended/check-unattended.sh` runs, check 10 (protocol parity) and the
  `unattended skill wiring` leg are both green, proving both renders were regenerated.
- **AC5** — When `memory/guides/UNATTENDED-PROTOCOL.md` section 5 is read, it states the orphan-reap
  duty for a start path that refuses before a run exists.
- **AC6** — When `memory/guides/BUILD-METHOD.md` M10 is read, its keepalive bullet no longer reads
  "Create it before preflight", still points at protocol §5, and states no rule of its own.
- **AC7** — When `wc -c` runs over BOTH halves of the pair — `memory/guides/BUILD-METHOD.md` AND
  `tools/memory-tree/BUILD-METHOD.template.md` — each is at or below `24576`, M1's stated budget. The
  template is the binding half.
- **AC8** — When `wc -c memory/guides/SESSION-KICKOFF.md` runs, the result is at or below the
  `MAX_MANIFEST_BYTES` value `skills/session-kickoff/manifest-check.sh` declares, and the build's own
  §B bullet is the trim that paid for it.
- **AC9** — When `.claude/skills/unattended/SKILL.md`'s `## Resume` section is read, it instructs the
  resumed session to issue `CronDelete` against the recorded `keepalive` id FIRST and report what it
  returned, THEN schedule a replacement, and it cites the measurement that forbids assuming the old
  job is dead. It also states that `--keepalive-id` is recordable only at `--preflight`, so the close
  attestation covers both jobs and the wrap-up says which.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `memory tree hygiene` · `kit version markers`,
and `bash tools/run-gates/run-gates.sh` at the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-27 · initial draft.
- rev-4 · 2026-08-27 · folded spec-audit round 2, finding 20. S3 and AC9 rested on "a resumed
  session's keepalive is dead by construction", which `TOOL-aPromptedMandate-11` records as MEASURED
  FALSE, and the rendered prose went further and told the agent no delete could reach it — the orphan
  leak S2 exists to close, reintroduced on the path the previous fold added. Resume now reaps first.
- rev-3 · 2026-08-27 · folded spec-audit round 1, findings 24 and 28: the `## Resume` path was
  outside "every path" and is now named in S3 and AC9; `SESSION-KICKOFF.md` was an unpriced fourth
  carrier and is now S7 and AC8; AC7 grades BOTH halves of the BUILD-METHOD pair, because the
  template is 11 B tighter than the render and only the looser half was priced.
- rev-2 · 2026-08-27 · AC1's observable was wrong: the superseded wording is deliberately QUOTED in
  the new section, so a zero-count grep could never pass over a correct implementation. Rewritten to
  grade the obligation and to name the one legitimate survivor.

## 10. Reuse audit

The seam is the Skill's existing shared preamble position: `SKILL.template.md` already places the
routing table and the "one thing to understand first" paragraph above every path, so a rule that
binds all four has a home that needs no new structure. The protocol's section 5 is the existing
statement of the actor split and is amended in place rather than joined by a second section — one
fact, one home.

`python tools/codebase-map/reuse_lookup.py "scheduling the keepalive before an unattended run begins
orienting"` returned `UNATTENDED-PROTOCOL.md` and `.unattended.conf` as the affordance seams and no
competing mechanism. `python tools/memory-recall/query.py` with terms `keepalive preflight
orientation park discovery scope rescope amend mandate delegated fork veto stall unattended
directive` returned `aUnmannedHelm-4`'s protocol spec, whose "The keepalive, split by actor" section
is the origin of the sentence this unit corrects, and `cBriefedPilot`'s step-B design, which is where
the slug path's step 3 came from. Both confirm the obligation was always meant to precede the run;
neither anticipated a path that orients before preflight.
