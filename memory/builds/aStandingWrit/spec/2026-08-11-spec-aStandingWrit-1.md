# TOOL-aStandingWrit-1 — the run authorizes on a plan it did not write

**Status:** SPECCED · rev-1 · 2026-08-11 · node a · Tier-2 · base af6de231 · streams tooling+playbook+kickoff

## 1. Goal

Make `/unattended <slug>` the owner's only act by moving the unattended run's authorization off an
owner-authored block inside the file the run writes, and onto the build folder the owner already
creates. The run must still author none of its own inputs, and the driver must be able to say which
step of the build remains without re-reading prose.

## 2. Scope (IN)

**S1 — the authorization surface moves to the build README at BASE.** `check_mandate()` in
`tools/unattended/unattended.sh` is replaced by `check_authorization()`, which asserts that
`<MEMORY_ROOT>/builds/<slug>/README.md` exists at the pinned BASE, parses as build front matter, and
carries a `slug:` equal to the requested slug. The marker constants `MAN_OPEN` and `MAN_CLOSE`, the
mandate extraction on both sides, and every refusal keyed on them retire.

**S2 — `RUN.md` becomes wholly generated.** `--preflight` CREATES the run-state file when it is
absent, replacing the `fail 15` refusal. The authored region drops the mandate and carries four
facts: the phase with its witness, the keepalive id, parked decisions, and the run's BASE.

**S3 — the merge-base-equals-HEAD refusal is scoped by verb.** `trusted_base()` currently turns
`resolve_base` rc 2 into a refusal for every caller. It becomes a refusal for `--close` and for the
gate leg, and a legal state for `--preflight`, where it is the normal condition of a run that has
correctly built nothing yet.

**S4 — `--plan`, the derived gap list.** A fifth verb prints, per unit, whether it needs a spec, a
review, a build, or nothing, and names the next one. It derives this from tracked spec status
headers and tracked review-record filenames, reusing `tools/memory-tree/gen_build_index.py` rather
than re-parsing either.

**S5 — the authored plan region, and a build-README template.** An optional marker-delimited region
in the build README lists planned units by title. A new `memory/TEMPLATE-README.md` documents the
build README's shape, which closes the open backlog row recorded inline as TOOL-aUnmannedHelm-3 —
the build README is the entrypoint a session starts from and has had no template.

**S6 — the phase vocabulary gains members.** `SPECCING`, `REVIEWING` and `BUILDING` join the
kit-owned core between `PREFLIGHT` and `VERIFYING`, so a phase claim can name a position `--plan`
computes. `CORE_FLOOR` rises from `6:6` to `9:6`.

**S7 — the amendment set.** `memory/guides/UNATTENDED-PROTOCOL.md` §1, §2, §3 and §7;
`tools/unattended/PROTOCOL.template.md` and the kit-parity assertion that holds them equal;
`tools/unattended/SKILL.template.md` and its render; `AGENTS.md`; the playbook's domain-rules
companion §1; `.claude/SESSION-KICKOFF.md`; and Step 5b of `skills/session-kickoff/SKILL.md`, whose
first sentence conditions the hand-back on a mandate that will no longer exist.

## 3. Non-goals (OUT)

The instruction layer. How an agent writes a sub-spec, how it conducts the adversarial review, and
what "built" means for a given unit are being designed in a parallel session. This build defines the
seam — the gap list `--plan` emits and the phase members that name a position — and stops. A second
author of the same prose here would collide with that session.

`tools/hooks/agent-cap.js` and `memory/guides/REVIEW-PROTOCOL.md` are owned by another build and no
scope item may touch them.

The keepalive actor split is unchanged. It stays agent-attested, and this build does not make it
machine-checked, because nothing about the authorization change alters what a script can reach.

No migration is written for an adopter who installed the kit at 1.0. There is no such adopter — the
dossier records that nothing has travelled the adopter path — so a migration would be untested code
for a population of zero. Follow-up if one appears.

`push-main.sh` and `.githooks/pre-push` are read but not modified. The interaction found in §5 under
risks is resolved inside this kit or it is deferred, never by loosening the lander.

## 4. Design

### The property that must survive

The kit exists to replace a checkpoint with something a machine can check. The property doing that
work is not "the owner wrote a block". It is:

> Every input to the authorization comparison lies outside the run's reach.

The three blockers in the second Tier-2 on the prior build were one violation of that rule at three
layers. Any redesign is judged against the same rule, and the surface below is chosen because it
satisfies it, not because it is convenient.

A build folder committed on the default branch before the run's branch exists is outside the run's
reach in exactly the way the mandate block was: the run cannot make a commit it did not make contain
a file it did not write. The reachability test is unchanged in kind. Only the blob it reads moves —
from a file the driver splices into, to one the driver never writes.

That move also deletes a hazard rather than relocating it. The prior review found that a transposed
marker pair made `--preflight` truncate the run-state file from the open marker to EOF, destroying
the owner-authored mandate, and only then print an unrelated refusal. Under S1 there are no owner
bytes in that file at all, so the worst case of that bug is the loss of regenerable state. The
marker bug is still a bug and is not in this build's scope to leave unfixed if it survives.

### What the new check is, precisely

`check_authorization()` takes the slug and the pinned BASE and asserts four things in order, each
its own refusal:

| # | Assertion | Refuses when |
|---|---|---|
| 1 | the build README blob resolves at BASE | the folder was created on the run's own branch |
| 2 | the blob parses as build front matter | the file exists but is not a build README |
| 3 | its `slug:` equals the requested slug | a folder was renamed or a README copied between builds |
| 4 | the plan region, when present at BASE, is byte-equal in the working copy | the run rewrote the scope it is executing against |

Assertion 4 is conditional by design, and F1 in §8 is whether it stays that way. When the region is
absent at BASE the run is authorized on existence alone, which is precisely what the owner ratified;
when it is present the run additionally cannot edit its own scope mid-flight.

### What is lost, stated plainly

The old check compared two blobs for equality and could therefore assert integrity: the run had not
edited its authorization. The new one cannot make that assertion about the README as a whole,
because the README is a living document whose generated region the run legitimately re-renders. The
authorization degrades from **integrity** to **existence**, and assertion 4 buys back integrity only
over the plan region.

The second loss is selectivity. The old mandate named one build. The new predicate is satisfied by
every build folder in the tree, so the grant is a class grant: any build the owner has ever
committed a README for is unattended-eligible. The narrowing is the slug the owner types, and chat
is not machine-checkable. The owner was shown this at kickoff and ratified it as F0a. It is recorded
as a decision rather than buried in a diff, and F4 in §8 asks whether that record is written.

### Data model

The run-state file's authored region, after S2:

```
phase: BUILDING
witness: <sha>
base: <sha>
keepalive: <id>
parked: <one entry per line, each carrying question, options seen, and reason>
```

The mandate line is gone. `base` remains the fifth authored fact from the prior build minus the
mandate, and it is still a runtime observation nothing else in the tree holds.

The optional plan region in a build README, delimited by a marker pair in the same family as the
generated one:

```
<!-- plan:units -->
1. the run-state file, and the hygiene contract that admits it
2. the protocol document, and the authorization it rests on
3. the driver, and the four verbs it is allowed to have
<!-- /plan:units -->
```

Units are named by TITLE and never by id. Minting ids ahead of their specs would create ids that are
cited and never defined, which is what `ORPHAN_ID_PIN` counts, and that pin is at 5 and shrink-only.
It also matches the rule the protocol already states in §2: a planned unit is NAMED rather than
LINKED until its record exists.

### Inventory

`--plan` joins three sources and emits one row per unit.

| Source | Read via | Yields |
|---|---|---|
| planned units | the plan region of the build README, tracked | the titles the owner intends |
| specs and their statuses | `gen_build_index.py` `collect()` and `parse_spec()` | id, status token, rev |
| review records | tracked filenames under the build's `reviews/`, matched against the recording grammar check 5 enforces | which units have been reviewed |

The join key between a spec and its review record is the sequence number both filenames carry. That
is a filename join and it is fragile; F3 in §8 and the risks line in §5 both name it.

The derived state per unit, in the order the run consumes them:

| Condition | State |
|---|---|
| a planned title with no spec | `SPEC NEEDED` |
| a spec at a non-terminal status with no review record | `REVIEW NEEDED` |
| a spec reviewed and non-terminal | `BUILD NEEDED` |
| a spec at a terminal status | `DONE` |

`--plan` prints these rows and one `next:` line naming the first non-`DONE` unit and the phase that
corresponds to its state. It exits non-zero when it cannot join a source, because a gap list that
silently omits a unit is worse than no gap list.

### Migration

`memory/builds/aUnmannedHelm/RUN.md` does not exist, so no live run-state file carries a mandate
block to migrate. The prior build's units are all CLOSED. The only migration is textual: the four
places that state the explicit-ask rule, amended by the prior build to accept a committed standing
mandate, are amended again to accept a committed build plan. They are `AGENTS.md`, the playbook §1
and §8 by way of the domain-rules companion §1, and `.claude/SESSION-KICKOFF.md`.

### Rollout

Single commit series on this build's branch, landed through `tools/push-main.sh` like everything
else. There is no runtime state to roll forward and no adopter to coordinate with.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/unattended/unattended.sh` | S1, S2, S3, S4, S6 |
| `tools/unattended/unattended.test.sh` | arms for every branch added or moved |
| `tools/unattended/check-unattended.sh` | check 13 re-points to the new surface; check 9 keeps its refusal |
| `tools/unattended/check-unattended.test.sh` | arms, including the three reproduced attacks re-aimed |
| `tools/unattended/PROTOCOL.template.md` | S7 |
| `tools/unattended/SKILL.template.md` | S7 |
| `tools/unattended/.unattended.conf.example` | `CORE_FLOOR` and the phase members |
| `.unattended.conf` | `CORE_FLOOR` to `9:6` |
| `memory/guides/UNATTENDED-PROTOCOL.md` | S7 |
| `memory/TEMPLATE-README.md` | new, S5 |
| `memory/HYGIENE.md` | the new template joins the documented set |
| `.claude/skills/unattended/SKILL.md` | re-rendered |
| `AGENTS.md` | S7 |
| `parallel-coding-governance.domain-rules.md` | S7 |
| `.claude/SESSION-KICKOFF.md` | S7, plus the ratchet re-stamp |
| `skills/session-kickoff/SKILL.md` | Step 5b, S7 |
| `.memory-tree.conf` | `ARMS_FLOORS` for both unattended scripts |
| `memory/map/features/unattended.md` | the dossier's constraints and gaps both change |
| `memory/DECISIONS.md`, `memory/backlog/TOOL.md` | the rows this build defines and closes |

### Alternatives rejected

**A conf-declared policy key plus README existence.** Recommended at kickoff and rejected by the
owner as F0a. It would have kept an owner-authored, committed, un-forgeable artifact in the tree at
the cost of one line written once. The owner's bar was zero declarations and that is the ratified
answer.

**A front-matter key in the build README.** Also rejected as F0a. It preserved a genuine per-build
opt-in and named both actions, at the cost of one line per build.

**Keeping the mandate and generating it.** Considered and rejected on the rule at the top of §4: a
mandate the tooling generates is a mandate the run's own toolchain produces, which is the
self-authorization the whole kit exists to refuse. The generation step being in a script rather than
in the agent's output changes nothing about who supplies the input.

**Deriving the plan from the README's prose unit table.** Rejected. The prior build's own README
carries a unit table whose `ids:` front-matter key lists one id for a build that has seven, which is
the evidence the open backlog row cites. A parser over that prose would inherit its ambiguity, and
`gen_build_index.py` deliberately reads no prose for exactly this reason.

## 5. Production-readiness checklist

- **security** — the whole build is one security property. The threat is a run that authorizes
  itself; the control is that both inputs to `check_authorization()` come from a commit the run
  cannot have made. Every one of the three attacks reproduced in the prior Tier-2 must be re-aimed
  at the new surface and shown to fail, and that is AC7.
- **perf / scale** — `--plan` adds one `git ls-files` pass and one front-matter parse per build. The
  hygiene gate already does both on every build in the tree. Immaterial.
- **a11y** — N/A — a shell driver with no user interface.
- **i18n** — N/A — the repo is single-locale by charter.
- **error / empty / loading states** — three empty cases each need a defined answer rather than a
  crash: a build with no plan region, a plan region with no entries, and a build whose `spec/` is
  empty. The first authorizes on existence, the second is a refusal because an empty declaration is
  not a passing one, and the third is the ordinary first-run state where every planned unit reads
  `SPEC NEEDED`.
- **observability** — `--status` gains the derived position, so a compaction-resumed run reads its
  place instead of inferring it. Every refusal continues to name itself, which is the existing house
  rule and what makes an unattended refusal legible to nobody.
- **risks (concurrency, data-loss, rollback hazards)** — three, and the first is the one that
  worries me most.
  - **The lander moves the merge-base.** `tools/push-main.sh` reconciles origin BEFORE the gate. If
    that reconciliation brings the run's branch onto a newer `origin/<default>`, the derived
    merge-base advances past the recorded BASE and `fail 18` fires at close on a run that did
    nothing wrong. This is a live interaction between two shipped components and F2 in §8 is the
    fork for it. It is not hypothetical: the lander doing this is the reason it is mandatory.
  - **The filename join.** Matching a review record to a spec by their shared sequence number breaks
    the moment a build reviews two units in one record or reviews the build as a whole, which is
    what both of the prior build's own review records do. `--plan` would read seven units as
    unreviewed. F3 does not fix this and it needs an answer before S4 is built.
  - **Data loss.** Reduced, not eliminated. S2 removes owner bytes from the file the driver splices,
    so the truncation path found in the prior review can no longer destroy anything unrecoverable.
- **testing + left-shift gates** — every branch added or moved needs a positive assertion naming its
  own failure text, and `ARMS_FLOORS` pins both scripts one-sided upward. Deleting the mandate
  branches LOWERS a floor, which reds until the floor is lowered in the same commit with a reason.
  That is the intended friction and it must not be met by widening a pin.
- **migration / rollback** — no runtime state. Rollback is a revert of the series.
- **user docs** — the rendered skill and the protocol are the user docs, and both are in S7. The
  skill's "Find the mandate. Do not write one." step becomes wrong the moment S1 lands, and its
  wiring check compares the render to its template, so a stale render reds rather than misleads.

## 6. Acceptance criteria

**AC1** — When a build's README is committed on the default branch and a run branches from it and
invokes `--preflight <slug> --keepalive-id <id>` having authored nothing, preflight succeeds and
writes a run-state file it created itself.

**AC2** — When a run creates a build folder and README on its own branch and invokes `--preflight`
against it, preflight refuses, naming that the README does not resolve at the pinned BASE.

**AC3** — When the merge-base equals HEAD, `--preflight` proceeds and `--close` refuses. Both arms
run in `unattended.test.sh`, and the close arm asserts the existing refusal text is unchanged.

**AC4** — When a build carries a plan region at BASE and the working copy's region differs,
`--preflight` refuses, naming that the run edited the scope it is executing against.

**AC5** — When `--plan` runs over a build with one closed unit, one specced-and-unreviewed unit and
one planned-but-unspecced title, it prints exactly three rows reading `DONE`, `REVIEW NEEDED` and
`SPEC NEEDED`, and a `next:` line naming the review.

**AC6** — When `.unattended.conf` declares a `CORE_FLOOR` whose phase count is below the shipped
core set, `check-unattended.sh` refuses. The floor rising to nine is asserted, not assumed.

**AC7** — When each of the three attacks from the prior Tier-2 is re-aimed at the new surface — a
BASE read back from the run-written record, an anchor moved with a local branch force, and a
discarded error signal — `--preflight` refuses in all three cases, and `check-unattended.sh` refuses
independently in all three.

**AC8** — When `bash tools/unattended/adopt-unattended.sh --check` runs after the render, it exits 0
and the render carries no surviving placeholder, so template parity and placeholder completeness are
both observed.

**AC9** — When `python tools/codebase-map/test_codebase_map.py` runs, the unattended dossier claims
every gate leg this build adds or renames, and the generated map artifacts byte-compare against a
fresh render.

## 7. Gates

The full bar, `bash tools/run-gates.sh`, at the push boundary. The legs this build moves rather than
merely keeps green:

- `bash tools/unattended/check-unattended.sh` and its sibling `check-unattended.test.sh`
- `bash tools/unattended/unattended.test.sh`
- `bash tools/unattended/adopt-unattended.sh --check` and `adopt-unattended.test.sh`
- `python tools/memory-tree/check-arms.py`, against the lowered `ARMS_FLOORS` entries
- `bash tools/memory-tree/check-memory-hygiene.sh`, for the new template and the new build folder
- `bash tools/check-template-size.sh`, if any amendment reaches the template rather than the companion
- `bash skills/session-kickoff/manifest-check.sh`, since `.unattended.conf` is a watched pathspec
- `python tools/codebase-map/test_codebase_map.py`
- `python tools/drift-audit/drift_report.py`

No new gate leg is added. S4's verb is exercised by the driver's own self-test rather than by a
tenth leg, because a leg that only runs a verb duplicates the self-test that already runs it.

## 8. Open questions

**F1 — is the plan region's byte-equality a hard precondition or an opt-in?**
Hard makes the integrity property universal and reintroduces per-build authoring, which is the thing
this build removes. Opt-in honours F0a and leaves a build with no region authorized on existence
alone. **Recommendation: opt-in**, with the template shipping the region so new builds get it by
default and the ladder is a default rather than a choice anyone has to make.

**F2 — does the recorded-BASE assertion relax from equality to ancestry?**
As written, `fail 18` fires when the derived merge-base differs from the recorded one, and the
mandated lander can cause exactly that by reconciling origin mid-run. Relaxing to "the recorded BASE
is an ancestor of the derived merge-base" admits legitimate forward movement. The obvious objection
is that it lets the run record an arbitrary older ancestor — but every ancestor of the branch point
is also pre-run, and assertion 4 compares the plan region across whichever BASE is recorded, so a
run that reaches back to an older commit with a different plan fails that comparison rather than
passing this one. **Recommendation: relax to ancestry**, and say in the refusal text why ancestry
rather than equality is the honest test.

**F3 — does `--plan` read tracked files only?**
Tracked-only matches every other gate here and means an uncommitted spec is invisible until the run
commits it, which suits a run that commits as it goes. Reading the working tree would let `--plan`
see work in progress and would also let it see a spec the run has written but not committed, which
is a state the rest of the tooling treats as not existing. **Recommendation: tracked only.** Note
that this does NOT resolve the filename-join risk in §5, which is a separate defect and needs its
own answer before S4 is built.

**F4 — is the widening recorded as a decision row?**
F0a converts a per-build grant into a class grant over every build in the tree. The tree's
convention is that a ratified fork becomes a row in `memory/DECISIONS.md`.
**Recommendation: yes**, worded as the widening it is rather than as an ergonomics improvement, so a
future reader who finds an unattended run on a build nobody remembers authorizing can see it was
foreseen.

## 9. Revision log

- rev-1 · 2026-08-11 · initial draft. Two owner forks resolved at kickoff and recorded as F0a and
  F0b in the build README; four new forks opened as F1 through F4.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "derive per-unit build progress from spec status headers
and review records"` returns `parse_spec` and `derive_status` in `tools/memory-tree/gen_build_index.py`,
and `.unattended.conf` as the affordance seam for this kit's declarations.

The seam S4 wires through is `gen_build_index.py`. Its module docstring states that a build's status
is a pure function of the build front matter plus every status header under that build's `spec/`,
and that it reads no git history, no mtimes, and neither `build/` nor `reviews/`. `collect()` already
walks tracked spec paths per build and `parse_spec()` already extracts the status token and rev.
`--plan` calls those rather than re-parsing a status header, because two parsers for one header is
the assertion-between-two-derived-values shape one level up: they would agree until they did not,
and the gate that byte-compares the generated region would side with one of them arbitrarily.

The two sources `gen_build_index.py` deliberately does not read — the plan region and `reviews/` —
are new reads that belong to `--plan` and not to the renderer. Pushing them into `gen_build_index.py`
would change what the generated region contains, which would change what the hygiene gate
byte-compares, for the benefit of one verb in another kit. `--plan` composes; the renderer stays a
pure function of the two things it already reads.

`.unattended.conf` is read for `MEMORY_ROOT` and `CORE_FLOOR` and gains no key, which is F0a's
ratified shape.
