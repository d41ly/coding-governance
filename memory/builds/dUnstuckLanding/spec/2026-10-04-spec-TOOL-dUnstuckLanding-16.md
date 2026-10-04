# TOOL-dUnstuckLanding-16 — an INHERITED red lands at any age, and the age escalates its ask

**Status:** CLOSED · rev-1 · 2026-10-04 · node d · Tier-2 · base 98926870 · streams tooling · order 4 · closes TOOL-dUnstuckLanding-6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-dUnstuckLanding-16-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-dUnstuckLanding-16-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md) | journal | TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-13-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-spec-brief.md) | journal | TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 |

<!-- /gen:spec-records -->

## 1. Goal

A red the default branch already carries stops an unattended run only because of its AGE. Once a
permanent red passes `INHERITED_RED_MAX_AGE`, every later run holds `inherited-red` until the owner
moves, and the hold's release re-runs a bar that stays red. Owner ruling `TOOL-dUnstuckLanding-22`
reverses that part of D12-i4: an INHERITED red lands at any age, the age raises the leg's ask to
BLOCKER in the closing build's own backlog, `memory/LIVE.md` shows it, and the kit default policy
becomes `land`. Build that ruling in all three readers of the policy, so that no reader still refuses
what another one admits.

## 2. Scope (IN)

- **S1 — the runner's landable predicate.** In the runner, `tools/run-gates/run-gates.sh`, every
  INHERITED leg counts into `land_n`, whatever its age reads: a number, `aged`, or `-` for unproven or
  not asked. `ATTR_LANDABLE` is set when every red leg reads INHERITED. The `gate-inherited-green`
  stamp is written under `land` and `ATTR_LANDABLE=1` with the full green's other preconditions, and
  it no longer requires an age bound. Its `max_age` field records the bound, or nothing when none was
  handed. The comment at the age probe that says aged is something "no policy lands" is rewritten to
  say the age decides escalation only. The `GATE attr` lines and the attribution row's columns do not
  change. Observed by AC1 and AC2.
- **S2 — the pre-push hook.** In `.githooks/pre-push`, `read_policy_at` reads the kit default `land`
  when `INHERITED_RED` is absent or blank, and when the policy file is absent at R. `land` with no
  positive `INHERITED_RED_MAX_AGE` reads `land` with no bound. A value outside `park land` still reads
  `park`. The policy line names which of these it read. `check_inherited_verdict` admits an INHERITED
  row whatever its age column reads. The stamp's admission rule is unchanged: its `base` must be the
  remote sha, and its `max_age` must equal the bound read at that sha, both possibly empty. Observed
  by AC3.
- **S3 — the driver's policy and decision table.** In `tools/unattended/unattended.sh`,
  `read_gate_policy` takes S2's reading table, and a blank or absent `GATE_POLICY_FILE` reads the kit
  default `land`, announced. `read_gates_record` returns `land` when every red leg reads INHERITED
  under `land`, at any age, and `hold` under `park`. It also returns the aged legs, comma-joined, for
  S4. The MET line under `land` names the aged legs instead of claiming every leg sits inside the
  bound. Observed by AC4 and AC6.
- **S4 — the escalation.** `write_inherited_asks` files the ask for an `aged` leg at SEV `BLOCKER`,
  with the ask text `inherited red: leg <leg> red at <R8>, older than the <n>-landing age bound`.
  Every other INHERITED leg keeps SEV `HIGH` and today's text, an unproven age included. The ask is
  filed where it is filed today, in the CLOSING build's `BACKLOG.md`, minted under the closing run's
  slug. `read_ask_back` takes the expected severity as an argument, and both its callers pass it.
  The reuse rule stays: an OPEN ask this build filed for the same leg at the same R, read back at the
  severity now owed, is named and nothing is written. With no age bound declared, no leg is ever
  `aged`, and the MET line says that nothing is escalated. Observed by AC4, AC5 and AC6.
- **S5 — the LIVE section.** `render_live` in `tools/memory-tree/gen_build_index.py` gains a section,
  `## Open BLOCKER asks`, rendered only when one exists. It lists every OPEN ask whose SEV is
  `BLOCKER`, one line per ask, each linking its home build's `BACKLOG.md` and carrying the ask's text
  excerpt, cut to the entry cap. An escalated ask's excerpt begins with the leg name, so LIVE names the
  leg. The section reads the generator's existing ask fold and never parses the driver's ask grammar.
  With no BLOCKER ask, `memory/LIVE.md` is byte-identical to today's render. Observed by AC7.
- **S6 — the carriers.** Each sentence that states the old policy is rewritten to the ruling, and the
  renders are re-copied by `bash tools/unattended/adopt-unattended.sh` in the same pass:
  - `tools/unattended/STOPS.template.md` §13: the three outcome bullets, the default, and the
    escalation. ABSORB's paragraph does not change, because the ask stays in the closing build.
  - `tools/unattended/SKILL.template.md`: the paragraph that says an aged red holds.
  - `tools/unattended/PROTOCOL.template.md` §8: the `GATE_POLICY_FILE` row, whose blank reading
    becomes `land`.
  - `tools/unattended/.unattended.conf.example`: the `GATE_POLICY_FILE` comment.
  - `.githooks/gate-env.sh`: the comment calling `park` the kit default. Gov's two declared lines,
    `land` and a bound of 10, do not change.
  - `tools/run-gates/README.md`: the age section, and `memory/map/features/run-gates.md`: the stamp
    paragraph, refreshed on touch.

  Observed by AC8.
- **S7 — the decision row.** `memory/DECISIONS.md` already carries `TOOL-dUnstuckLanding-22`, which
  supersedes part of `TOOL-dDerivedDocket-24` by id. This unit writes no second row. Observed by AC9.

## 3. Non-goals (OUT)

- ABSORB and check 23. The ask stays in the closing build, so ABSORB's fourth condition reads it
  where it reads it today. Ruling `TOOL-dUnstuckLanding-22` keeps D12-i5 unchanged.
- Bisecting past the age bound to find an aged leg's introducer. The age decides escalation only, and
  an unknown introducer is already a named arm of the ask text.
- The governance template's §7 line, "Keep the automated suite green at the push boundary". §8 F4
  says why this unit does not touch it.
- Ask 11's carriage of the policy into inCMS and NicoCares.
- The kit version. The orchestrator bumps once, at VERIFYING.

### Edges

- **hands-off** external — the owner's ruling on whether the governance template's §7 line changes,
  now that `TOOL-dDerivedDocket-73`'s reason for leaving it ("true under the kit default park") no
  longer holds.
- **hands-off** external — the version moves of the unattended, run-gates and memory-tree kits, to
  the orchestrator at VERIFYING, which the `kit epoch` leg on §7's line owes.

## 4. Design

### The reading table, shared by S2 and S3

| what the policy file says at R | reads | age bound |
|---|---|---|
| no file at R, or no policy file named | `land`, the kit default | none |
| `INHERITED_RED` absent or blank | `land`, the kit default | the declared bound, if positive |
| `INHERITED_RED=land` | `land` | the declared bound, if positive |
| `INHERITED_RED=park` | `park` | the declared bound, if positive, for the ask's owner |
| any other value | `park` | none |
| no tip for R on the remote | `park` | none |

The last two rows stay `park` on purpose. A typo must not land a red, and with no R nothing can read
INHERITED. The two readers keep their own copies of this table. Their shared parser,
`read_policy_key`, is byte-identical in both today and is not edited.

### The decision, after this unit

| record | policy | outcome |
|---|---|---|
| tree moved | any | UNMET, naming the move |
| no usable record | any | UNMET, as today |
| every red INHERITED, at any age | `land` | MET, `gates-inherited`; aged legs filed BLOCKER |
| every red INHERITED | `park` | UNMET, the `inherited-red` hold line |
| any OWN, MIXED, DEAD PROBE or CONTENDED | any | UNMET, the attribution lines |

### Why the stamp keeps `max_age` in its admission

The pre-push hook trusts a stamp only when the bound it reads at R equals the stamp's. After this unit
the bound decides nothing about landing, so the equality only protects against a policy file that
moved between the driver's bar and the push. A mismatch then forces the hook's own bar, which
attributes and lands by itself. Keeping the rule costs one forced bar in a rare case. Dropping it
would widen what a stamp admits, and nothing here needs that.

### Inventory

No identifier is minted. `read_ask_back` gains a third argument, the expected SEV. The LIVE section's
heading, `## Open BLOCKER asks`, is new text in a generated file.

### Rollout

Gov already declares `INHERITED_RED=land` with a bound of 10, so the only behaviour gov sees change is
that an aged INHERITED red lands with a BLOCKER ask, where it held before. An adopter that declares
nothing moves from `park` to `land`. Every reader announces the reading on its policy line, so the
change is visible on the first red push.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/README.md`
- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `.githooks/gate-env.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/STOPS.template.md`
- `tools/unattended/SKILL.template.md`
- `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/.unattended.conf.example`
- `memory/guides/UNATTENDED-STOPS.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `.claude/skills/unattended/SKILL.md`
- `tools/memory-tree/gen_build_index.py`
- `memory/map/features/run-gates.md`

### Alternatives rejected

- **The LIVE line parsed from the driver's ask text.** It would make the generator read a grammar the
  shell driver writes, a contract spelled in two kits with no parity gate. The SEV is already folded,
  and a BLOCKER ask belongs in front of the owner whatever filed it.
- **The escalated ask in the introducing build's backlog.** An aged leg has no introducer by
  construction, and the write would land in another run's folder. That is the closing review's H2
  and H5.
- **Dropping the age probe at the push boundary.** It would save up to five leg runs per inherited
  leg on a red push. It would also drop the age from the hook's attribution lines, which an owner
  reads, and it would force the `max_age` admission rule to change. Not taken.

## 5. Production-readiness checklist

- security — the policy is still read at R and never from the pushed tree, by both readers. A
  malformed value still reads `park`. The landing surface widens only as far as ruling
  `TOOL-dUnstuckLanding-22` decided: aged and unproven INHERITED reds, which the classifier already
  shows add no offender.
- perf / scale — unchanged. The age probe runs exactly as it does today.
- error / empty / loading states — the reading table's last two rows; an unproven age lands and is
  not escalated; with no bound, nothing escalates and the MET line says so.
- observability — the policy line on every red push and every close; the MET line naming aged legs;
  the BLOCKER ask; the LIVE section.
- risks — an adopter with no policy file now lands inherited reds on attended pushes too. That is
  the ruling's "kit default", and the hook announces it.
- testing — the arms under §7, each staged RED against today's code before it is flipped.
- migration — none. No record or conf key changes shape.
- user docs — the carriers S6 lists.

## 6. Acceptance criteria

Each criterion is observed on a scratch fixture repository built by hand under `%TEMP%`, the shape
the existing `TOOL-dDerivedDocket-24` arms already build. No criterion runs a suite or the bar.

- **AC1** — When the runner runs in a fixture whose one leg is red at R and red with the same
  offenders at R~2, exported `GATE_ATTRIBUTE` naming R, `GATE_INHERITED_RED=land` and
  `GATE_INHERITED_RED_MAX_AGE=2`, the attribution row reads INHERITED with age `aged`, and
  `gate-inherited-green` is written naming that leg with `max_age` 2.
  Red when: the stamp is absent, which is today's behaviour.
- **AC2** — When the same fixture runs with no `GATE_INHERITED_RED_MAX_AGE`, the stamp is written
  with an empty `max_age`. When its leg's far end cannot answer, the row reads `age unproven` and the
  stamp is still written. When a second leg reads OWN, no stamp is written.
  Red when: an unproven or unbounded INHERITED red writes no stamp, or an OWN leg is stamped.
- **AC3** — When a push runs through `.githooks/pre-push` to a fixture remote whose policy file at R
  declares only `INHERITED_RED_MAX_AGE=2`, over a tip whose bar is red on one aged INHERITED leg, the
  hook prints `inherited-red policy at <R8> reads land` naming the kit default, then
  `landing under INHERITED_RED=land`, and the push lands. The same push with `INHERITED_RED=park`
  declared is blocked, and with `INHERITED_RED=lnad` it is blocked, reading `park`.
  Red when: the undeclared default blocks, or a malformed value lands.
  fixture: the policy file read at R, never the pushed tree's copy.
- **AC4** — When `--close` evaluates `gates-green` on a fixture build with `INHERITED_RED` undeclared,
  a bound of 2 and one aged INHERITED leg, the item is MET with a `gates-inherited` fact, and the
  build's own `BACKLOG.md` gains one ask whose SEV row reads `BLOCKER`, read back through `ASKS_CMD`.
  `git diff --cached --name-only` then lists no path outside that build's folder and the run-state
  file.
  Red when: the item holds, the ask is HIGH, or a path in another build's folder is staged.
- **AC5** — When the same fixture's leg is red at R and green at R~2, the item is MET and the ask's
  SEV reads `HIGH`. When the leg's age is unproven, the item is MET and the ask reads `HIGH`.
  Red when: an under-bound or unproven leg is escalated.
- **AC6** — When `gates-green` runs twice over the same aged leg at the same R, the second run prints
  `already OPEN` and files nothing. When a second leg reads OWN or MIXED, the item is UNMET with the
  attribution lines and prints no hold line.
  Red when: a repeated close files a second BLOCKER, or a red of the run's own lands.
- **AC7** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, a new arm renders a
  fixture tree with one OPEN BLOCKER ask and finds `## Open BLOCKER asks` and that ask's id in
  `memory/LIVE.md`'s render. A tree whose asks are all HIGH renders no such heading.
  Red when: the section is missing for a BLOCKER ask, or present with none.
- **AC8** — When `grep -n "kit default" tools/unattended/STOPS.template.md` runs, §13 names `land` as
  the kit default and no line calls `park` the default. Then
  `bash tools/unattended/adopt-unattended.sh --check` exits 0, so the renders match their templates.
  Red when: a carrier S6 lists still states that an aged red holds, or a render differs from its
  template.
- **AC9** — When `grep -c "TOOL-dUnstuckLanding-22" memory/DECISIONS.md` runs, it prints at least 1,
  and that row names `TOOL-dDerivedDocket-24`.
  Red when: the superseding row is absent.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `run-gates canary` · `pre-push self-test` · `build-index selftest` · `memory hygiene` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `check-wiring self-test` · `recall floor` · `recall floor arms`

New arm: tools/run-gates/run-gates.test.sh · AC1 and AC2's fixtures; the arm `TOOL-dDerivedDocket-24` AC17 wrote, which asserts no stamp for an aged leg, is flipped and staged RED first · none
New arm: .githooks/pre-push.test.sh · AC3's undeclared, `park` and malformed readings · none
New arm: tools/unattended/unattended.test.sh · AC4 to AC6's BLOCKER, HIGH, reuse and OWN fixtures · none
New arm: tools/memory-tree/gen_build_index.py `--selftest` · AC7's BLOCKER and HIGH-only trees · none

## 8. Open questions

- **F1 — what does the kit default cover?** (a) Only an absent or blank `INHERITED_RED` in a policy
  file that exists. (b) That, and no policy file at all. RESOLVED (agent, 2026-10-04, delegated): (b).
  Ruling `TOOL-dUnstuckLanding-22` makes `land` the kit default, and an adopter that declares no file
  has declared nothing. A malformed value and a missing R stay `park`, the direction that does not
  land.
- **F2 — where does the LIVE line come from?** (a) Parse the driver's ask text for inherited-red
  rows. (b) List every OPEN BLOCKER ask from the generator's existing fold. RESOLVED (agent,
  2026-10-04, delegated): (b). It needs no new cross-kit grammar, and its excerpt names the leg.
- **F3 — a reused ask whose severity no longer matches.** The age at one R under one bound is fixed,
  so a mismatch needs an age probe that answered differently on two runs. (a) Reuse at any severity.
  (b) Reuse only at the owed severity, else file a new ask. RESOLVED (agent, 2026-10-04, delegated):
  (b). A BLOCKER that should exist is never hidden behind a HIGH, and the duplicate is visible.
- **F4 — the governance template's §7 line.** `TOOL-dDerivedDocket-73` kept "Keep the automated suite
  green at the push boundary" because it was "true under the kit default park". After this unit the
  default is `land`. (a) Edit the template here. (b) Leave it, and hand the question to the owner.
  Option (a) changes a governance carrier the design did not name, which M3's veto 2 discards.
  RESOLVED (agent, 2026-10-04, delegated): (b). The question is reported in the build's return and
  handed off in §3.
- **F5 — may S6 edit PROTOCOL §8 and the Skill?** Neither is in the design's owes list for §3. Both
  restate the default this ruling changes, and leaving them is the
  `amendment-leaves-its-other-half-standing` class. RESOLVED (agent, 2026-10-04, delegated): edit
  both. The substance is the owner's ruling `TOOL-dUnstuckLanding-22`. The edit only makes each
  carrier state it, and it adds no rule.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from design §3 at rev-2, ask 6, review items H2, H3, H5, M1 and
  M15, and ruling `TOOL-dUnstuckLanding-22`.

## 10. Reuse audit

The seams are the existing policy machinery of `TOOL-dDerivedDocket-24`, extended in place:
`read_gate_policy`, `read_gates_record`, `write_inherited_asks` and `read_ask_back` in
`tools/unattended/unattended.sh`; `read_policy_at` and `check_inherited_verdict` in
`.githooks/pre-push`; `derive_age` and the `land_n` count in the runner; and `render_live` with the
ask fold in `tools/memory-tree/gen_build_index.py`. No new mechanism is added. `python
tools/codebase-map/reuse_lookup.py "land a push over a red the default branch already carries"`
returned no symbol seam, because its scan does not cover `.sh`. It named `.unattended.conf` and the
runner's `LEGS_FILE` as affordance seams, which agree. The recall probe returned ruling
`TOOL-dUnstuckLanding-22`, the `TOOL-dDerivedDocket-24` spec's AC17 arm that this unit flips, and
ruling `TOOL-dDerivedDocket-73`, which is the source of §8 F4.

Recall terms used: INHERITED_RED inherited-red age bound aged land park gate-inherited-green pre-push attribution D12-i4 escalation BLOCKER
