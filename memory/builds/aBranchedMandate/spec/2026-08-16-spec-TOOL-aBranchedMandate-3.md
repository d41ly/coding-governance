# TOOL-aBranchedMandate-3 — a build published on the run's own branch may authorize the run

**Status:** SPECCED · rev-1 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

The unattended authorization requires the build README to be reachable from the merge-base with the
tip the remote advertises for its own HEAD, so a build specced and committed on a unit branch cannot
start a run until it is landed. Admit a second anchor — the tip the remote advertises for the run's
own branch — as a declared, recorded, strictly weaker alternative, and state what it costs in the
document that already states what the first one costs.

## 2. Scope (IN)

- **S1** — `resolve_base` in `tools/unattended/unattended.sh` gains a fallback: when the build README
  does not resolve at the default-branch merge-base, and the project declares the wider scope, the
  BASE is pinned to the tip the remote advertises for the run's current branch. The observation uses
  the same `ls-remote --symref --exit-code` discipline and the same `GIT()` dereference pin as the
  existing one.
- **S2** — the fallback tip must be an ancestor of HEAD. A tip that is not is a branch the run is not
  building on, and pinning to it would measure the authorization against history this run does not
  contain.
- **S3** — `check_authorization` is unchanged. It already takes the base as an argument and asserts
  shape at it; the fallback changes which commit it is handed, not what it asks.
- **S4** — the run-state file records `anchor-kind`, plus the branch ref and tip that were observed.
  Protocol section 2's authored-fact count moves from seven to eight in both copies of the document.
- **S5** — a new declaration in `.unattended.conf` selects the scope, defaulting to today's
  behaviour. An adopter who declares nothing keeps the strict anchor.
- **S6** — check 9 of `tools/unattended/check-unattended.sh` stops asking "is the recorded BASE an
  ancestor of the anchor" and asks "is the recorded BASE **published on the remote**": an ancestor of
  the advertised HEAD tip, or equal to a tip the remote advertises for any ref. The leg does **not**
  read `anchor-kind` and does **not** read a branch name.
- **S7** — the rendered Skill states the new precondition, so an operator starting a run on an
  unlanded build is told to publish the branch first rather than meeting a refusal.
- **S8** — protocol sections 1, 2, 8 and 9 gain the second anchor, its declaration, and its cost, in
  `tools/unattended/PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md` in lockstep.
- **S9** — the two sibling self-tests gain arms for the fallback: it fires only when declared, it
  refuses an unadvertised branch, it refuses a tip that is not an ancestor of HEAD, and the leg
  accepts a branch-anchored record while still refusing a BASE that is on no advertised history.

## 3. Non-goals (OUT)

- Any anchor that is not an observation of the remote. A local ref, a reflog entry, a commit date, a
  committer identity and the environment are all inside the run's reach, and
  `memory/gotchas/inputs-inside-the-subjects-reach.md` records what that cost the last time.
- Closing the self-authorization class. Protocol section 9 already says this kit does not prevent an
  unauthorized landing, only makes it a visibly deliberate act and records which act was taken. This
  unit lowers the price of that act and is honest about it; it does not claim to raise it.
- Repairing the gate leg's anchor generally. `TOOL-aStandingWrit-6` is the tracked OPEN row for the
  leg computing BASE from `GOV_DEFAULT_BRANCH` and a remote-tracking ref rather than an observation.
  S6 makes the leg observe **for its own predicate**; it does not repair every other consumer of that
  derivation in the same file.
- Changing `--landed`, the lander, or the pre-push hook. Landing still happens on the default branch
  and is still gated exactly as today.
- Changing the phase vocabulary or the Definition-of-Done set. `CORE_FLOOR` does not move.
- Bumping `KIT_UNATTENDED_VERSION` independently of node `c`'s in-flight move to 1.5. See §8 F3.

## 4. Design

### What fails today, and why it is not a bug

Reproduced by `build/repro-c3.sh` under this build, against a bare origin that advertises a HEAD
symref so the anchor observation succeeds and only the authorization comparison fails:

```
UNATTENDED check 6 FAILED — no build README at the pinned BASE, so nothing committed before this
run branched authorizes it, and a build folder the run created on its own branch authorizes
nothing: <merge-base>:memory/builds/aTestBuild/README.md
```

Protocol section 1 states this as ratified design, and the four costs of the current model were
enumerated and accepted by the owner. So this unit is a **rule change**, priced as one.

Two facts about the current predicate that shape the fix. It reads only `README.md` — specs are
never consulted, so landing the specs would change nothing. And it is not worktree-specific; any
branch reproduces it. The worktree is where this repo keeps branches, which is why the symptom is
seen there.

### The second anchor

```
observe HEAD symref  ->  advertised default ref + tip        (today, unchanged)
BASE := merge-base(advertised tip, HEAD)
    build README resolves at BASE?  -> authorized, anchor-kind: default-branch
    otherwise, and only when declared:
observe refs/heads/<current branch>  ->  advertised branch tip
    tip is an ancestor of HEAD?      (S2)
    build README resolves at tip?    -> authorized, anchor-kind: run-branch
                                        BASE := that tip
```

Both anchors are observations of the same endpoint the landing push goes to. The existing
same-endpoint, single-remote, no-substitution-lever and no-injected-config guards run before either
and are not duplicated.

### What is preserved, and what is spent

**Preserved.** The anchor is never a local ref and never a name from the environment, so the two
reproduced offline forgeries stay inert by construction. The recorded observation still lets a party
off this machine re-derive the pin without trusting a byte the run wrote.

**Spent, and this is the whole price of the unit.** Under the default-branch anchor the authorizing
commit had passed the pre-push hook, which runs the full bar. `.githooks/pre-push` classifies on the
remote ref and runs the bar only for a default-branch push, so **a branch push is an ungated
publish**. The consequence, stated flatly:

> Today a run can authorize its SUCCESSOR — protocol section 1, cost 4, already accepted. Under the
> second anchor a run can authorize ITSELF, in two ordinary commands: commit a build folder on its
> branch, push the branch, preflight.

Nothing in this design closes that, and no wording in the protocol may imply otherwise. What the
design does instead is make it visible: `anchor-kind: run-branch` is on the record, the branch ref
and tip are on the record, and an off-machine verifier sees which anchor a run leaned on. That is
section 9's stated posture applied rather than abandoned — but applying it here is a real reduction
in the price of self-authorization, and the owner is the one who gets to decide whether it is worth
being able to run a build from a branch.

Two guards were considered for the gap and both rejected as theatre: requiring the advertised branch
tip to differ from HEAD (defeated by one empty commit) and requiring a minimum commit distance
(defeated by the same). A guard the subject satisfies trivially is worse than no guard, because it
reads as protection in a document whose value is that its claims are exact.

### Why the leg must not read `anchor-kind`

`anchor-kind` is written by the run. A leg branching on it would be a security check whose
discriminator is supplied by its subject, which is the class
`memory/gotchas/inputs-inside-the-subjects-reach.md` records and the class three of this kit's
authorization defects belonged to. So S6 gives the leg a single predicate that covers both anchors
and needs no discriminator:

> the recorded BASE is an ancestor of the advertised HEAD tip, **or** it equals a tip the remote
> advertises for some ref.

Equality against an advertised tip is exactly "this commit is published on the remote", which is the
property both anchors are trying to express. It also keeps the leg free of any branch NAME: route 2
of the reproduced bypass was a branch name supplied through the environment, and a leg that never
reads one cannot be walked through that way. `anchor-kind` stays in the record as EVIDENCE for a
human and for an off-machine verifier, exactly as the anchor ref, tip and URL already do.

The driver does read its own branch name, and that is sound: a forged local name merely selects a
different remote ref to observe, and the authorization still requires the remote to advertise it and
a conforming build README to resolve there.

### Data model

| Run fact | Today | After |
|---|---|---|
| `base` | the pinned merge-base | the pinned base, from whichever anchor |
| `anchor-ref` · `anchor-sha` · `anchor-url` | the observed default-branch advertisement | unchanged |
| `anchor-kind` | absent | `default-branch` or `run-branch` |
| `branch-ref` · `branch-sha` | absent | the second observation, when it was used |

Protocol section 2 states an authored-fact count. It moves, and it moves in both copies.

### Inventory — every consumer of the authorization

| Site | Change |
|---|---|
| `unattended.sh` `resolve_base` | S1, S2 |
| `unattended.sh` `trusted_base` | the recorded-BASE cross-check must accept a base equal to the derived one on the branch path |
| `unattended.sh` `check_authorization` | none (S3) |
| `unattended.sh` `verb_preflight` | records the new facts |
| `unattended.sh` `dod_met` → `authorization-reachable` | none; it re-derives through `trusted_base` |
| `unattended.sh` `verb_landed` | none; landing is still measured against the default-branch tip |
| `check-unattended.sh` check 9 | S6 |
| `check-unattended.sh` check 13 | none; it reads the README at the recorded BASE, which S6 has already validated |

### Migration

None for an existing record. A run-state file with no `anchor-kind` is a default-branch run, and S6's
predicate accepts its BASE by the first clause exactly as check 9 does today. No committed record is
retroactively red, which is the property that lets this land without a sweep.

### Rollout

Total order, and the reason is the leg. S6 must land in the same commit as S1: a driver that can pin
a branch anchor while the leg still demands ancestry of the default tip writes a record that reds the
bar on the next push, on the one path the run is required to take.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/unattended/unattended.sh` | S1, S2, S4 |
| `tools/unattended/check-unattended.sh` | S6 |
| `tools/unattended/SKILL.template.md` + the rendered Skill | S7 |
| `tools/unattended/PROTOCOL.template.md` · `memory/guides/UNATTENDED-PROTOCOL.md` | S8 |
| `.unattended.conf` + `tools/unattended/.unattended.conf.example` | S5 |
| `tools/unattended/unattended.test.sh` · `tools/unattended/check-unattended.test.sh` | S9 |
| `.memory-tree.conf` | the `ARMS_FLOORS` pairs for both files, re-measured |
| `AGENTS.md` | the leg's check count, if S6 adds an ordinal rather than changing one |

### Alternatives rejected

- **Anchor on the commit that introduced the build folder, read locally.** One ordinary commit
  authorizes the run, with no push and nothing published. It deletes the property rather than
  weakening it, and leaves no record that anything was weakened.
- **Keep the strict anchor and require the owner to land the build first.** This is today's
  behaviour and it is what the commissioning report rejects. Recorded because it remains a legitimate
  answer if the owner decides the price in the section above is too high — in which case the
  deliverable is `TOOL-aBranchedMandate-1` and `TOOL-aBranchedMandate-2` alone, which between them
  fix every worktree failure that is not the authorization rule.
- **A signed tag or a secret the owner holds.** It is the one construction that would genuinely close
  the class, and this kit can neither issue nor manage a secret. Protocol section 9 already names the
  remote-side required check as the thing that actually binds.
- **Widen the first anchor's merge-base to any ancestor of the advertised tip that carries the
  README.** It sounds weaker-but-simpler and is neither: a build landed and later deleted would keep
  authorizing runs forever, and it does nothing for a build that was never landed, which is the case
  the report is about.

## 5. Production-readiness checklist

- security — this is the unit's entire subject. The change is a deliberate reduction in the cost of
  self-authorization, priced in §4, defaulted off in S5, recorded in S4, and stated in the protocol
  in S8. The one hard rule it must not break: no input to the authorization may come from inside the
  run's reach, which is why S6 refuses to read `anchor-kind`.
- perf / scale — one additional `ls-remote` per preflight, and one per leg run, both only on the
  fallback path. The leg's existing per-record loop does not gain a network call per record; the
  advertisement is fetched once.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a remote that answers but advertises nothing for the branch is a
  refusal naming the branch, distinct from a remote that does not answer at all, which the existing
  `--exit-code` discipline already distinguishes. An empty declaration must select the strict anchor,
  never the wide one: protocol section 8's rule is that an empty declaration is a refusal rather than
  a pass, and the safe reading of a blank scope key is today's behaviour.
- observability — the run-state file gains the three facts that make the weaker anchor legible, and
  the wrap-up surfaces `anchor-kind` because an owner reading a landed run should not have to
  reconstruct which anchor it used.
- risks — the named one is self-authorization, above. The second is the leg and the driver drifting
  into two different predicates, which is what wedged this kit twice before; S6 answers it by giving
  both one property (published on the remote) rather than two spellings of one procedure.
- testing + left-shift gates — S9, and the fixture must build a real bare origin that advertises a
  HEAD symref. `build/repro-c3.sh` under this build is the working fixture shape and the arms reuse
  it. An arm keyed on the exit code alone would pass on any refusal, which is the
  `fixture-passes-by-finding-nothing` class this repo tracks by name.
- migration / rollback — no record migrates. Reverting restores the strict anchor and makes any
  branch-anchored run's record unverifiable, so a rollback must be paired with closing or aborting
  any live run — worth stating in the commit, not worth mechanising.
- user docs — S7 and S8. The Skill gains the precondition; the protocol gains the cost.

## 6. Acceptance criteria

- **AC1** — When `--preflight` runs on a build committed and pushed on the run's own branch, with the
  wide scope declared, it succeeds and the run-state file records `anchor-kind: run-branch` together
  with the observed branch ref and tip.
- **AC2** — When the same command runs with the scope undeclared or blank, it refuses with the check
  6 message, exactly as `build/repro-c3.sh` reproduces today.
- **AC3** — When the build folder is committed on the branch but the branch has **not** been pushed,
  `--preflight` refuses and its message names the branch that the remote does not advertise.
- **AC4** — When the remote advertises the branch but its tip is not an ancestor of HEAD,
  `--preflight` refuses, and the arm proving it uses a fixture where the tip is a real advertised
  commit rather than a missing one.
- **AC5** — When a build README is present at the branch tip but declares a different `slug:`,
  `--preflight` refuses through the existing shape check, proving `check_authorization` was reached
  rather than bypassed.
- **AC6** — When `bash tools/unattended/check-unattended.sh` runs over a branch-anchored record, it
  passes; when it runs over a record whose BASE is on no advertised history, it reds naming that
  BASE.
- **AC7** — When the leg runs over an existing default-branch record that carries no `anchor-kind`,
  it passes unchanged, proving no committed record is retroactively red.
- **AC8** — When `grep` is run over `tools/unattended/check-unattended.sh` for `anchor-kind`, there is
  no hit, proving the leg branches on nothing the run wrote.
- **AC9** — When `bash tools/unattended/adopt-unattended.sh --check` runs, the rendered Skill matches
  the template plus the conf and carries no surviving placeholder, with S7's precondition present.
- **AC10** — When `bash tools/unattended/check-unattended.sh` runs its shipped-equals-installed check,
  `PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md` agree after S8.
- **AC11** — When `python tools/memory-tree/check-arms.py` runs, both unattended files are fully
  armed and the `ARMS_FLOORS` pairs in `.memory-tree.conf` match a fresh measurement.
- **AC12** — When `bash tools/unattended/adopt-unattended.test.sh` runs, the adopter e2e is green,
  including its junction arm, proving S5's new key did not break the render for an adopter.

## 7. Gates

- `bash tools/run-gates.sh`, and `GATE_FULL=1 bash tools/run-gates.sh` at the push boundary.
- `bash tools/unattended/check-unattended.sh` — the kit gate, which S6 edits.
- `bash tools/unattended/check-unattended.test.sh` and `bash tools/unattended/unattended.test.sh` —
  the two sibling legs, which S9 edits.
- `bash tools/unattended/adopt-unattended.sh --check` and `bash tools/unattended/adopt-unattended.test.sh`.
- `python tools/memory-tree/check-arms.py` with the `ARMS_FLOORS` pins in `.memory-tree.conf`.
- `python tools/codebase-map/test_codebase_map.py` — the unattended dossier under `memory/map/features/`
  must be re-derived for the new anchor, and the generated artifacts re-rendered.
- `bash tools/check-playbook-parity.sh` — reds if a value the playbook STATES stops equalling the
  source that owns it, which the leg's check count is.

## 8. Open questions

- **F1 — the declaration's name and value set.** Options: a boolean-ish key naming the behaviour
  (`ALLOW_BRANCH_ANCHOR=1`), or a scope key with a closed value set
  (`ANCHOR_SCOPE=default-branch|published`). **Recommendation: the scope key.** It names the property
  rather than the mechanism, it leaves room for a third scope without a second boolean, and a closed
  value set means a typo is a refusal instead of a falsy string that silently selects the strict path.
  A boolean whose absence and whose misspelling produce the same behaviour is the shape that hides a
  misconfiguration.
- **F2 — does S6 need `TOOL-aStandingWrit-6` first?** That row records that the leg's anchor is not
  observed. S6 makes the leg observe for its own predicate, which repairs that gap along the path
  this unit uses and leaves it open elsewhere in the file. Options: land S6 as specified and close
  the row partially, or block on the row and land the leg's anchor wholesale. **Recommendation: land
  S6 as specified, and update the row to name what remains rather than closing it.** Blocking couples
  this unit to an unspecced one, and a partially observed leg is strictly better than a wholly
  unobserved one. This is a scope question and therefore an owner turn.
- **F3 — the kit version.** Node `c`'s in-flight `cBriefedPilot` takes this kit to 1.5 across the
  driver literal, the leg literal and the shipped doc marker, and it holds twenty-two open rows on
  the same files this unit edits. Options: bump here, ride theirs, or coordinate an order.
  **Recommendation: do not bump, and sequence this build after theirs if both are live.** Two builds
  moving one version literal is a conflict in the value whose entire purpose is to be unambiguous,
  and the file overlap is large enough that the merge cost dominates either way. This is an owner
  turn because it is a cross-node sequencing decision.
- **F4 — should a branch-anchored run be allowed to reach `LANDED` at all?** A defensible stricter
  position is that the weaker anchor authorizes building and merging but not the final landing
  observation. Against it: `--landed` already requires HEAD to be an ancestor of the advertised
  default tip, so the work IS on the default branch by the time it is claimed, and refusing there
  would strand a run that has already landed its work. **Recommendation: no additional restriction.**
  Recorded because it is the first thing a reviewer will ask.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft, from the reproduction recorded under this build's `build/`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "unattended run authorization anchor observed from the
remote"` returned no symbol-level seam, which is the correct answer and not an absence of diligence:
the anchor machinery is a set of file-local functions in one copy-installed kit, so it has a fan-in of
one and never reaches the map's seam threshold. The seams this unit wires through are named directly.

`observe_anchor` in `tools/unattended/unattended.sh` already carries every precondition the second
observation needs — one remote, the same fetch and push endpoint, no injected git config, no
object-substitution lever, and the `GIT()` dereference pin — so S1 extends that function's result
rather than opening a second, differently-guarded path to the remote. Reusing it is what keeps the
new observation from becoming the weaker of two spellings.

`check_authorization` is reused verbatim (S3): it already takes the base as a parameter and asserts
shape at it, which is why a second anchor needs no second authorization predicate. The region and
roster comparisons inside it apply to the branch anchor unchanged.

The fixture shape is reused from `build/repro-c3.sh` under this build, which itself follows the bare
origin with an advertised HEAD symref that `tools/unattended/unattended.test.sh` established. No new
test harness is introduced.
