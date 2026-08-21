# TOOL-dScriptedRepeat-4 — the declaration seam: README names the path, playbook holds the globs

**Status:** CLOSED · rev-4 · 2026-08-21 · node d · Tier-2 · base d2a40aa8 · streams tooling · ratified 2026-08-20

## 1. Goal

Bind a run to a playbook: the build README's front matter at the pinned BASE names the playbook PATH
and the requested piece count; the gate reads the output globs and the piece grain from that playbook,
also at BASE. Fork 8's hybrid, which is what keeps the playbook self-describing across runs.

## 2. Scope (IN)

- **S1.** Two new build-README front-matter keys, read at BASE: `playbook:` (a repo-relative path) and
  `pieces:` (a positive integer, the count the owner asked for). Both are read only when the mode is
  `recipe` mode; absent under any other mode is legal and means nothing.
- **S2.** THE FRONT-MATTER SCAN GAINS TWO KEY-TAGGED EMISSIONS, in the driver's awk at
  `unattended.sh:783-790` and in the leg's independent copy at `check-unattended.sh:444-471`. That awk
  emits `slug=` and `mode=` and nothing else today, so `playbook:` and `pieces:` have no reader at all
  without this edit and AC1 is unimplementable. The one-blob-one-parse property is PRESERVED: two more
  key-tagged lines out of the same scan, never a second pass over the same blob.
- **S2b.** A SECOND blob read, of a DIFFERENT file, in the driver and independently in the leg:
  `GIT show "$base:$playbook"`, parsed for the declaration block's `outputs` and `grain`. The
  `No second GIT show: one blob, one parse` comment bounds THAT front-matter scan and is not a rule
  against reading a second file; this spec records that because the comment reads like one.
- **S3.** REFUSALS, each with its own message: `playbook:` naming a path that does not resolve at BASE;
  a playbook at BASE whose declaration block does not parse; `outputs` empty or absent; `grain` absent
  or unresolvable; `pieces:` absent, zero, or non-numeric.
- **S4.** The GRAIN. `grain` is a glob whose every MATCH is exactly one piece. The research measured a
  factor of three on a single three-file diff — three paths, two directories, one new piece — so a
  seam that does not declare grain cannot count pieces at all. The gate refuses a grain it cannot
  resolve rather than picking one.
- **S5.** The leg's independent re-derivation. The merge bar re-reads both blobs and compares its own
  answer against the recorded one, the way the mode is already second-opinioned — never trusting the
  driver's record.
- **S6.** Arms for every refusal in S3, each staged and observed RED, plus an arm that the leg's
  independent read DISAGREEING with the record reds.

## 3. Non-goals (OUT)

- No change to `check_authorization`'s existing parse, to `resolve_base`, or to the anchor.
- No conf key. The declarations are per-run and per-playbook, not per-project; a project-level output
  root would be wrong for a repo with several playbooks, which is the ordinary case.
- The gate does not verify that the playbook is VALID here. Unit 3 owns validity; this unit owns the
  binding. Two mechanisms.
- No writing. This seam reads.

## 4. Design

### Why the path is in the README and the globs are in the playbook

The path must come from somewhere the run cannot have written, which on the default-branch anchor means
the README at BASE. The globs must travel with the playbook, because a playbook re-run next month must
not depend on a run author retyping its outputs correctly — that retyping is the structural regression
the README-only option carries and which two research lenses recommended without noticing.

The cost is honest and stated: a second `GIT show`. Against it, the alternative costs a
non-self-describing artifact in a mode whose premise is repeatability, and the driver comment that
looked like a prohibition is about bounding one front-matter scan.

### On the second anchor, this buys less

Under the published anchor the BASE is a tip the run itself pushed, so the run can author both blobs.
Protocol §1 already prices this as cost 1 and §9's reduction applies unchanged. What the seam buys
there is a RECORD of which playbook bound the run, not a proof — and this spec says so rather than
letting a reader infer strength the mechanism does not have.

### Inventory

| Thing | Where | Read by |
|---|---|---|
| `playbook:` | build README front matter at BASE | driver and leg, independently |
| `pieces:` | build README front matter at BASE | driver and leg; unit 6 consumes it |
| `outputs` | playbook declaration block at BASE | unit 8's scope refusal |
| `grain` | playbook declaration block at BASE | unit 6's piece count |

### Alternatives rejected

**Everything in the README.** Two lenses recommended it; the third's justification for the alternative
was false against source. Rejected on the repeatability argument above.

**Everything in the playbook, including the path.** Circular: the path to the playbook cannot be
declared inside the playbook.

**A conf key naming an output root.** Rejected: wrong grain, and a working-tree file the run can
commit, which the leg cannot trust — the same argument protocol §1 cost 2 already makes about
`ANCHOR_SCOPE`.

## 5. Production-readiness checklist

- security — this is the unit that most invites overclaiming. Reading a second blob at BASE does NOT
  make the declaration trustworthy under the published anchor; §9's reduction is unchanged and is
  restated in the driver comment beside the read.
- perf / scale — one extra `git show` per preflight and per leg run.
- a11y — N/A.
- i18n — paths and globs are ASCII; a non-ASCII path is refused rather than mishandled.
- error / empty / loading states — every one of S3's five refusals is a distinct message. A single
  ANDed verdict would send a reader to diff a parse against a path, which is the defect the DoD
  evaluation code already fixed once by splitting its terms.
- observability — the resolved playbook path, its blob sha, and the resolved grain are recorded in Run
  facts, so a later reader can tell which playbook bound the run without re-deriving it.
- risks — a grain glob that matches too broadly silently inflates the piece count. Unit 6's vacuity
  guard is the compensating control and the two units must be read together.
- testing + left-shift gates — S6, every refusal staged RED.
- migration / rollback — additive keys under one mode. Every existing README parses unchanged, and the
  index renderer is unaffected: `gen_build_index.py`'s `parse_front_matter` validates only its required
  keys, so additive ones ride through. Measured by the research rather than assumed.
- user docs — the template documents the declaration block; the Skill (unit 10) documents the two
  README keys.

## 6. Acceptance criteria

- **AC1** — When a build README at BASE declares `playbook:` and `pieces:`, `--preflight` records the
  resolved playbook path and its blob sha in Run facts.
- **AC2** — When `playbook:` names a path absent at BASE, `--preflight` REFUSES with a message naming
  the path and the BASE sha. Staged and observed.
- **AC3** — When the playbook at BASE carries no parseable declaration block, `--preflight` REFUSES
  with a message distinct from AC2's.
- **AC4** — When `grain` is absent, `--preflight` REFUSES rather than defaulting. Observed, because a
  defaulted grain is a piece count nobody declared.
- **AC5** — When `pieces:` is absent, zero, or non-numeric, `--preflight` REFUSES, with a distinct
  message for each of the three.
- **AC6** — When the leg re-derives the binding independently and its answer differs from the recorded
  one, `bash tools/unattended/check-unattended.sh` REDS. Staged by editing the record after preflight.
- **AC7** — When the mode is not `recipe` mode, a README carrying `playbook:` and `pieces:` is
  accepted and the keys are ignored, verified by an arm rather than assumed.

## 7. Gates

`bash tools/unattended/check-unattended.sh` · `bash tools/unattended/unattended.test.sh` ·
`bash tools/unattended/check-unattended.test.sh` · `bash tools/unattended/cross-component.test.sh` —
this last one specifically, because the driver-then-leg-over-one-tree arm is exactly the shape S5's
independent re-derivation needs and the kit had zero such arms until it was built.

## 8. Open questions

none — every fork below is RESOLVED in place.

- **F1 — RAISING `READ_PATH_CEILING`.** RESOLVED (owner, 2026-08-20): raised 112987 to 131892, which
  is 106292 measured plus the same 25,600 headroom every movement uses. The fifth movement's allowance
  was consumed to 6,695, which this build's protocol rows and decision appends exceed. The conf carries
  the argument beside the number and tells whoever merges to re-derive there.
- **F2 — whether `pieces:` belongs in the README at all**, given that it is the one value the owner
  changes per run while the playbook stays fixed. RESOLVED (agent, 2026-08-20, delegated): YES, and for
  exactly that reason — it changes per run, so it must sit at BASE where the run cannot have written it
  after the fact. Recorded because it looks misplaced beside `playbook:` and is not.

## 9. Revision log

- rev-4 · 2026-08-21 · CLOSED: built and landed on main at c8e0436, full bar GREEN 90/90 before
  the merge and again over the merged tree.
- rev-4 · 2026-08-20 · pre-code fork sweep under the mandate (M3). Every §8 fork RESOLVED in
  place with its resolver and authority named, and §8's first non-blank line made machine-legal —
  the driver classified nine of eleven specs FORKED on that line alone.
- rev-3 · 2026-08-20 · owner ratified `recipe` as the authorization mode value; every reference to
  the mode (never to the playbook DOCUMENT, which keeps its name) renamed. Unit 1 S3b states the
  distinction once.
- rev-1 · 2026-08-20 · initial draft. The hybrid was ruled by the owner on 2026-08-20 after the
  research found the fork-2 wording and the driver's own comment in conflict; S4's grain comes from a
  measured factor-of-three ambiguity on a single diff.
- rev-2 · 2026-08-20 · folded the M4 spec audit. F16 split S2: the README half of fork 8's hybrid had
  no reader at all, because the existing awk emits only `slug=` and `mode=`, and the previous revision
  had said that scan stays untouched. The §10 reuse claim naming `parse_front_matter` was false on this
  unit's path and moved to the migration row, where it is a true compatibility statement.

## 10. Reuse audit

`check_authorization`'s existing blob read at BASE is the seam: this unit adds a second read beside it
using the same `GIT show "$base:$path"` form, the same failure handling, and the same
record-then-second-opinion pattern the mode declaration already uses — where the driver records and the
leg re-derives independently rather than reading the driver's answer. That pattern is the reason a
recorded binding is worth anything at all, and reusing it is what keeps this unit from being a second
implementation that confirms the driver rather than checking it. The reused front-matter seam is the driver's own KEY-TAGGED awk idiom, extended by two emissions in
both readers. `gen_build_index.py`'s `parse_front_matter` is NOT on this unit's path — it is Python,
its only caller is the index renderer, and no shell reader here touches it; that additive keys do not
break the index render is a compatibility observation, and it now sits in the migration row rather than
standing in for a reuse decision. Recall terms used: build
README front matter base blob show authorization mode record second opinion leg independent derive
glob grain output path declaration anchor published.
