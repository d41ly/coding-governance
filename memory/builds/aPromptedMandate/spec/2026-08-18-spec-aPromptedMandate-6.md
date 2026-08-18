# TOOL-aPromptedMandate-6 — the driver-then-leg cross-component arm

**Status:** CLOSED · rev-3 · 2026-08-18 · node a · Tier-1 · base 6517579f · streams tooling

## 1. Goal

Add the arm that runs the driver and THEN the gate leg over one tree, so the prompt path is proved
end to end by the bar rather than by hand — and close `TOOL-aStandingWrit-8`, which is open on
exactly this gap.

## 2. Scope (IN)

- **S1** — one fixture: a bare origin advertising its own HEAD, a clone, a unit branch, the full
  installed kit. Built once and reused by every arm in the file.
- **S2** — the measurements this build made by hand become arms: unpushed branch refused · pushed
  branch accepted with the run-branch anchor recorded · the leg green over that same tree · the
  roster pair below · **and a fifth, prompt-mode arm**, because two other specs bank coverage on this
  unit that rev-1's closed four did not contain.
- **S2b** — the **roster arms are a PAIR, keyed on the DoD verdict**, not on close output. Rev-1's
  single arm asserted "no roster refusal in the close output" and could never fail: `--close`
  evaluates the item as `check_authorization "$slug" "$TB" >/dev/null 2>&1`, and the redirection binds
  the whole call, so `fail 20` and every other message it emits is discarded. The pair: roster grown
  and re-pushed → `--close` reports `authorization-reachable` MET; grown and NOT re-pushed → `--close`
  BLOCKS naming that item. Two directions, because one cannot tell the mechanism from a fixture that
  happened to re-push.
- **S2c** — the **prompt-mode arm**: a fixture whose build README at BASE carries `authorized-by:
  prompt`, driven through `--preflight` and then the leg, asserting `mode: prompt` in Run facts AND
  the leg's independent re-derivation agreeing. This is the driver/leg SEAM for the new mode bit —
  the gap `TOOL-aStandingWrit-8` is open on — and without it spec 1 §5 and spec 5 §5 name a
  left-shift gate that does not cover them.
- **S3** — the arms assert a MESSAGE or an on-disk effect, never an exit code alone.
- **S4** — the suite prints an executed assertion count in the agreed shape, and joins the derived
  population in `tools/gate-legs.json`.
- **S5** — the backlog row `TOOL-aStandingWrit-8` closes, naming this unit.

## 3. Non-goals (OUT)

- **Not a replacement for the existing suites.** The driver suite and the leg suite keep their arms;
  this one exists for the seam BETWEEN them, which is where both halves can agree with themselves and
  disagree with each other.
- **No new gate leg where a check would do**, in general — but this one IS a new leg, because it runs
  two components against a live remote and neither existing suite's fixture can host it. The
  manifest's trap about a new leg tripping a growing SET of meta-gates applies and is priced in
  section 5.
- Not a fix for `TOOL-aBoundedVerdict-10` (the driver's untimed `ls-remote` wedging the bar). Named
  as a risk below because this leg makes another remote-touching suite, and left as its own unit.

## 4. Design

### Why one fixture and not one per arm

Every arm needs the same expensive setup (a bare repo, a symref, a clone, a push). The existing
driver suite already uses a build-once-and-`reset_tree` shape, and this reuses it: a hard reset to a
pinned unit-branch commit, plus a force-push to restore the advertised tip. Force-push is required
and is not a shortcut — the arms deliberately move the branch, and an arm that inherited the previous
arm's advertised tip would pass or fail for the wrong reason.

### The four arms, and their observed evidence

Each was measured by hand on node `a` on 2026-08-18 and is recorded with its output in
`build/2026-08-18-build-TOOL-aPromptedMandate-1-anchor-reuse-reproduction.md`. The arms assert the same
strings:

| Arm | Condition | Asserted |
|---|---|---|
| 1 | build folder authored by the run, branch unpushed | the check-32 refusal text, and the run-state file byte-unchanged |
| 2 | same tree, branch pushed | preflight OK, and `anchor-kind: run-branch` in the record |
| 3 | the leg over arm 2's tree | exit 0 AND no output — because a leg that fails silently and a leg that passes are the same exit code only if nothing is printed |
| 4 | roster grown after preflight | no roster refusal in the close output, distinguished from the ordinary unmet-DoD blocks by name |

Arm 3's "no output" half is the load-bearing one. This build's first leg runs over an incomplete
fixture returned exit 0 for one arm and failing checks for others; asserting the exit code alone
would have scored a fixture gap as a pass.

### The fixture-completeness trap

Measured during this build: an incomplete fixture (missing the protocol pair, the Skill template, or
the real build method rather than a stub) makes the leg fail on checks that have nothing to do with
the subject — and a naive arm reading "the leg failed" would call that a correct refusal. The fixture
therefore installs the real files, and the suite asserts the fixture is complete (the leg is green on
the untouched tree) BEFORE any arm perturbs it. That is the `fixture-passes-by-finding-nothing` class
inverted: here the fixture fails by finding the wrong thing.

### Files touched (estimate)

`tools/unattended/cross-component.test.sh` (new) · `tools/gate-legs.json` (one leg, with its guard) ·
`tools/unattended/kit.toml` (govkit requires a gate-leg entry per leg) ·
`memory/project/testsuite-count-waivers.txt` (only if the count shape cannot be met, which it can —
and note the path: `check-testsuite-counts.sh` reads it from `memory/project/`, not from `tools/`,
where rev-1 spelled it. A waiver written at the wrong path is one the gate never reads while it sits
visibly in the diff) · `memory/backlog/TOOL.md` (close the row).

### Why the roster arm could not fail

`--close` discards `check_authorization`'s output entirely. An arm keyed on absence of a message in
that output is green whether the roster is legal, illegal, or the comparison is deleted from the
driver — the recurring class this repo gates for elsewhere, and the house `miss` helper is spelled so
`check-arms.py` scores such negatives as unarmed. S2b re-keys on the verdict, which is the only
channel that can differ.

## 5. Production-readiness checklist

- security — N/A; the fixture is hermetic and builds its own origin under `mktemp -d`
- perf / scale — a remote-touching leg on a bar that already times out on a node with a crowded
  TMPDIR; the fixture uses one `mktemp -d` and cleans up, and the leg is guarded so a records-only
  commit skips it
- a11y / i18n — N/A
- error / empty / loading states — an arm that cannot create the fixture must skip LOUDLY, the way
  the adopter suite's junction arm does, because a silent skip scores a missing capability as a pass
- observability — the suite prints its assertion count, and the runner persists per-leg output
- risks — the untimed `ls-remote` (`TOOL-aBoundedVerdict-10`) wedging the bar from one more place;
  the meta-gate set a new leg trips (map coverage, govkit selfcheck, the run-gates canary, the
  testsuite count) — run the full bar, not a list
- testing + left-shift gates — this unit IS the left-shift; its own correctness rests on arm 3's
  no-output assertion and the fixture-completeness precondition
- migration / rollback — additive; removing the leg is deleting one manifest row
- user docs — the kit README's leg list, and a dossier claim for the map's coverage inventory

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/cross-component.test.sh` runs, every arm passes and it
  prints an executed assertion count in the shape `bash tools/check-testsuite-counts.sh` accepts.
- **AC2** — When the fixture is deliberately left incomplete, `bash tools/unattended/cross-component.test.sh`
  fails on the fixture-completeness precondition and names it, rather than on an arm.
- **AC3** — When the branch is not pushed, arm 1 observes the check-32 refusal text AND
  `git hash-object` on the run-state file is unchanged.
- **AC4** — When arm 3 runs `bash tools/unattended/check-unattended.sh`, it asserts both exit 0 and
  empty output.
- **AC5** — When `bash tools/run-gates.test.sh` runs, the new leg is well-formed in
  `tools/gate-legs.json` and its guard names a tracked path.
- **AC6** — When `python tools/codebase-map/test_codebase_map.py` runs, the new leg is claimed by a
  dossier.
- **AC7** — When `memory/backlog/TOOL.md` is read, `TOOL-aStandingWrit-8` is closed and names this
  unit.
- **AC8** — When the roster is grown and re-pushed, `bash tools/unattended/unattended.sh --close`
  reports `authorization-reachable` met; when grown and NOT re-pushed, the same command BLOCKS naming
  that item. Both directions, asserted on the DoD verdict and never on close output.
- **AC9** — When the prompt-mode fixture runs through `--preflight` and then
  `bash tools/unattended/check-unattended.sh`, Run facts carries `mode: prompt` and the leg's own
  re-derivation from the BASE blob agrees with it.

## 7. Gates

`bash tools/unattended/cross-component.test.sh` · `bash tools/run-gates.test.sh` ·
`bash tools/check-testsuite-counts.sh` · `python tools/codebase-map/test_codebase_map.py` ·
`python tools/govkit/govkit.py selfcheck` · `bash tools/run-gates.sh`

## 8. Open questions

none — the fork below is RESOLVED.

- **A new leg, or arms inside the existing driver suite** — RESOLVED (agent, 2026-08-18): a new leg.
  The driver suite's fixture pins a single unit-branch commit and never pushes; the arms here move
  the advertised tip, and retrofitting that into a shared fixture would perturb every existing arm in
  a file of 1673 lines. The manifest's new-leg trap is the accepted cost.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-3 · 2026-08-18 · built, six arms at 13 assertions. S2c's arm 5b as SPECCED could not work:
  it said to drop the key from the README and re-preflight, but `mode:` and `base:` are both pinned
  once, so neither moves and no disagreement is producible. The arm forges the RECORD instead — the
  third fixture in this build that could not trigger its own rule, and the reason the suite asserts
  fixture completeness before any arm perturbs it.
- rev-2 · 2026-08-18 · folded the M4 spec audit. Arm 4 asserted on output `--close` discards and
  could never fail (ids 22, 36) — replaced by the verdict-keyed pair S2b. A fifth prompt-mode arm
  added, because spec 1 §5 and spec 5 §5 banked coverage the closed four did not contain (id 20).
  The testsuite waiver path was wrong: it lives under `memory/project/` (ids 17, 27).

## 10. Reuse audit

Satisfied for the SET in unit 1's reuse audit. The seam extended is the driver suite's own fixture
bootstrap in `tools/unattended/unattended.test.sh` — the bare-origin-plus-symref shape, the
`ORIGIN_DIR` placed OUTSIDE the work tree so `git clean -qfd` cannot delete it, and the
`reset_tree` / `fixture` helper pair. All four are copied in shape and not in bytes, because the two
suites differ in exactly the property that matters (this one pushes). The loud-skip discipline for an
arm the host cannot run is reused from `tools/unattended/adopt-unattended.test.sh`'s junction arm.
`TOOL-aStandingWrit-8` is the prior record that specifies this unit, found by the recall pass in
unit 1's reuse audit.
