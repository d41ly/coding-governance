# TOOL-aUnblockedFleet-1 — the driver stops refusing a run because another build is live

**Status:** SPECCED · rev-1 · 2026-08-31 · node a · Tier-2 · base 117de044 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aUnblockedFleet-1-1.md](../prompts/2026-08-31-prompt-TOOL-aUnblockedFleet-1-1.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`--preflight` refuses to start any run while another build in the tree holds a non-terminal
run-state file. The refusal's stated justification names a consumer that does not exist, and the
refusal itself has wedged this fleet three separate times. Replace it with an ANNOUNCEMENT of the
concurrent runs, so a second unrelated build starts instead of being blocked.

## 2. Scope (IN)

- **S1** — `check_single_live()` (`tools/unattended/unattended.sh:1224`) stops calling `fail 5`. It
  keeps enumerating every tracked `RUN.md` and `RUN.*.md`, keeps classifying each by phase, and
  PRINTS what it found instead of refusing on it.
- **S2** — the announcement names each concurrent run by file, phase and witness, one per line, so an
  operator reading a preflight can tell an abandoned record from a genuinely running sibling.
- **S3** — the announcement is SILENT when this run is the only live one. Nothing is printed at zero
  concurrent runs, because a line printed on every ordinary preflight is a line nobody reads.
- **S4** — the `LANDING`-witness exclusion (`TOOL-aPrimedKeepalive-7`) is KEPT and keeps its notice.
  An excluded record is not a concurrent run and must not be announced as one; the notice stays
  because it is the only evidence the exclusion is still armed.
- **S5** — refusal 5's exit code is retired from the driver's refusal vocabulary, and its
  corresponding arm in `unattended.test.sh` is rewritten to assert the announcement rather than
  deleted, because a deleted arm and a passing one are indistinguishable.

## 3. Non-goals (OUT)

- The LEG's check 7 — that is `TOOL-aUnblockedFleet-2`, deliberately a separate unit, because the
  driver grades the RUN and the leg grades the TREE and they are two mechanisms.
- A STALENESS bound that reds on an abandoned record whose own last commit is past a declared age.
  That is `TOOL-aReapedTicket-5`'s candidate fix, it needs a declared bound this build has no basis
  to pick, and it is a refusal — the thing this unit exists to remove. The row stays OPEN with its
  scope narrowed to staleness alone.
- `TOOL-aBranchedMandate-8`, the same-slug clobber: a second `--preflight` against a live own-slug
  record overwrites it and loses the keepalive id. It stays OPEN. This unit must not make it worse,
  which is why the announcement is scoped to OTHER slugs and this one changes no write path.
- The lander-marker race between two runs landing from one clone. Fails closed today; gets a row.

## 4. Design

### Alternatives rejected

**A liveness signal (a recorded pid, a record-age bound), keeping the tree-wide refusal.** This is
`TOOL-aReapedTicket-5`'s own candidate and it was tested against the owner's stated problem, which is
what rejected it: it only reaches DEAD runs. A genuinely live unrelated run on node `b` still blocks
node `a`, and the owner's instruction is that unrelated builds must not impair each other at all.
It also adds a field and a declared bound to buy a weaker version of what deletion buys free.

**Partitioning the count by node tag.** Two runs collide only where they share a clone, so refusing
only within a node is narrower and defensible. Rejected on measurement against this repository's own
layout: the charter's §3 says feature work happens ONLY in sibling worktrees of ONE primary tree, so
same-node concurrency is the COMMON case here, not the edge. This option blocks exactly the traffic
the owner is asking to unblock.

**Refuse only within the run's own slug.** Rejected as vacuous: a build folder holds exactly one
`RUN.md`, and leg check 4 already refuses an archived record carrying a non-terminal phase, so the
per-slug count is structurally ≤1 and the check could never fire. That is the vacuous-selector class
the charter names, and a gate that cannot fail is worse than no gate.

### The measurement that decided it

The refusal's header claims that without it "the run" is ill-defined and anything keyed on it must OR
the phases together or pick one arbitrarily. That was tested by construction rather than read, in a
scratch copy of this repository with both enforcement points neutered and two genuinely live
run-state records for unrelated builds (`aThawedCorpus` at `BUILDING`, `aUnblockedFleet` at
`RESEARCHING`):

| probe | result |
|---|---|
| the full leg `check-unattended.sh` | exit 0, green, no check other than the neutered 7 reported anything |
| `--status`, `--plan`, `--resume` on each of the two slugs | each resolved its own build correctly |
| `--park` on one slug | landed in that record, 0 occurrences in the other |
| `--phase` on the other slug | wrote only that record |
| `--review` on one slug | counted that subject's rounds only |

All fourteen driver verbs take a `<slug>` (`unattended.sh:4248-4261`). All three of the leg's
tree-wide loops over `builds/*/RUN*.md` (`:247`, `:332`, `:448`) grade per file. The consumer the
refusal protects does not exist, and the refusal's only consumers are the two checks that enforce it.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/unattended.sh` | `check_single_live()` — the `fail 5` line becomes a printed announcement; the function's header rewritten to state what it now does and does NOT claim |
| `tools/unattended/unattended.test.sh` | the check-5 arm asserts the announcement and the non-refusal; a new arm asserts silence at zero concurrent runs |

### Rollout

No migration and no data shape changes. A record written by an older driver reads identically; a
record written by this one is byte-identical to before, because this unit changes a refusal path and
writes no new fact. An adopter on an older kit keeps the refusal until they re-copy the kit.

## 5. Production-readiness checklist

- security — the refusal was never a security control. It bounds nothing an attacker could reach:
  the authorization is the pushed build folder and the anchor comparison, both untouched here.
- perf / scale — the enumeration is unchanged; one `git ls-files` either way.
- a11y — N/A, a shell driver with no user interface.
- i18n — N/A, this repository's tooling is English-only by declaration.
- error / empty / loading states — the zero-concurrent-run case is S3 and is the silent one. The
  no-anchor case keeps its existing UNAVAILABLE notice, because an exclusion that stops excluding
  must not be mistaken for one that found nothing to exclude.
- observability — the announcement IS the observability, and it is what the refusal's diagnostic
  value degrades into. It prints on the default channel for the reason the leg's header at `:23`
  already gives about its sibling notice: a notice routed through a gated reporter is invisible on
  every ordinary run, which is a check quietly deleted.
- risks — the one real concurrency hazard admitted by this change is two runs landing from one clone
  racing on the shared lander marker. It fails CLOSED today: `--landed` requires the marker to name
  HEAD exactly and refuses on a mismatch, naming both shas. Filed as a row by unit 5, not fixed here.
- testing + left-shift gates — unit 4 owns the arms. Both halves stage their break and observe RED.
- migration / rollback — revert the commit; nothing persists.
- user docs — unit 3 owns the two carriers.

## 6. Acceptance criteria

- **AC1** — When two tracked run-state files for different builds are non-terminal and neither is an
  excludable `LANDING` record, `bash tools/unattended/unattended.sh --preflight <third-slug>` exits 0
  and creates the run-state file, where before it exited non-zero and wrote nothing.
- **AC2** — When that same preflight runs, its stdout names each concurrent run's file, phase and
  witness, asserted by a `hit` arm in `unattended.test.sh` against the announcement's own text.
- **AC3** — When the run is the only live one, the preflight output contains no concurrency
  announcement, asserted by a `miss` arm — the silent-at-zero case, which distinguishes an
  announcement from a banner.
- **AC4** — When a `LANDING` record whose witness is an ancestor of the observed anchor is present, it
  is still EXCLUDED and its existing notice still prints, asserted by the existing arm text.
- **AC5** — When the driver's refusal inventory is re-derived, exit code 5 no longer names a live-run
  refusal, and `bash tools/memory-tree/check-arms.py` still finds every remaining branch armed.

## 7. Gates

`bash tools/run-gates/run-gates.sh`. The legs that bind: `unattended kit gate`, `unattended skill
wiring`, `memory hygiene`, and the `check-arms` armed-branch floor for
`tools/unattended/unattended.test.sh`, whose pin must still be met after an arm is rewritten.

## 8. Open questions

none — the one fork this unit had was which mechanism replaces the refusal, and it was decided by
the measurement in §4 rather than by preference. RESOLVED (agent, 2026-08-31, delegated): announce
the concurrent runs, refuse none of them.

## 9. Revision log

- rev-1 · 2026-08-31 · authored under the aUnblockedFleet mandate, after the §4 measurement.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "refuse a new unattended run when another run-state file
is still live"` returned no seam for this behaviour — the ranked candidates were name-stem matches
(`run`, `tracked_files`, `corpus_files`) with no relation to the run registry.

The seam this unit EXTENDS is `check_single_live()` itself, at `tools/unattended/unattended.sh:1224`,
and the pattern it copies is the `LANDING`-witness exclusion already inside that same function
(`TOOL-aPrimedKeepalive-7`) — an unconditional printed notice on the default channel, with an
explicit UNAVAILABLE sibling when the signal cannot be computed. This unit generalises that notice
from one phase to all of them and drops the refusal it was working around.

Recall terms used: `unattended preflight live-run exclusion non-terminal phase LANDING witness anchor
concurrent slug run-state deadlock check7 refusal`. It returned `TOOL-aReapedTicket-5`,
`TOOL-aFusedCharter-4`, `TOOL-aBoundedVerdict-24`, `TOOL-aBranchedMandate-8` and
`TOOL-aPrimedKeepalive-4`/`-7`. All were read; the first three are this defect from three angles and
are closed or narrowed by unit 5, the fourth is an out-of-scope sibling defect named in §3, and the
last is the precedent this design copies.

**A hit can be stale**, so every line/behaviour claim above was verified against source at writing
time: the verb dispatch table at `:4248-4261`, the three leg loops at `:247`/`:332`/`:448`, and leg
check 4's archived-record-must-be-terminal refusal. The two disagreed nowhere.
