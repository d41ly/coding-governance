# TOOL-aGradedMandate-3 — `gates-green` escalates onto held self-test legs by the run's own diff

**Status:** SPECCED · rev-1 · 2026-08-31 · node a · Tier-2 · base 396cd9db · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md](../build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md) | research | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 |

<!-- /gen:spec-records -->

## 1. Goal

`gates-green` runs the bare declared `GATE_CMD`, and `run-gates.sh` holds every leg whose
`subject = kit` or `chunk = selftests` unless `GATE_SELFTESTS` is set — 46 of 86 legs on this tree.
No carrier the run reads even names that variable. So a run that edits a checker lands with none of
that checker's own arms exercised. This unit makes the item escalate when, and only when, the run's
own diff touches a held leg's guard path.

## 2. Scope (IN)

- **S1** — In `dod_met`'s `gates-green` arm, before invoking `GATE_CMD`, compute the run's diff
  (`GIT diff --name-only <pinned BASE>..HEAD`) and intersect it with the `guard` arrays of every leg
  in `tools/gate-legs.json` that the runner would HOLD.
- **S2** — On any hit, `export GATE_SELFTESTS=1` for that invocation and print which leg and which
  path caused the escalation, so the escalation is never silent.
- **S3** — On no hit, behave exactly as today.
- **S4** — The escalation is skipped, with an announced reason, when the manifest cannot be read or
  the pinned BASE does not resolve — a fault on this side is reported, never converted into "no
  escalation is owed".
- **S5** — The arm's own header states what it does NOT reach: the unattended kit's own five suites
  are not legs in `tools/gate-legs.json` at all after the 2026-08-23 owner ruling, so no value of
  `GATE_SELFTESTS` reaches them and this unit does not pretend otherwise.

## 3. Non-goals (OUT)

- **Not `GATE_FULL`.** That bypasses the guard pass and not the self-test hold; setting it would
  change which guarded legs run without reaching one held leg.
- **Not the unattended kit's own suites.** `bash tools/unattended/run-unattended-gates.sh
  --selftests` measures 4611 s against a declared `GATE_BOUND` of 3600 s, so executing it inside
  `--close` produces a bound breach rather than a verdict. Closing that half needs a raised budget or
  a new record surface; both are owner turns and both are parked.
- **No change to the 2026-08-23 ruling.** This escalates by DIFF and never by default, so a run that
  touched no checker pays nothing.

## 4. Design

### Data model

No new fact. The two inputs are the run's own pinned `base:` and `tools/gate-legs.json`, which
already declares `guard`, `subject` and `chunk` per leg.

### Inventory

| Site | Change |
|---|---|
| `unattended.sh` `dod_met` `gates-green` | the escalation clause and its two announcements |
| `unattended.test.sh` | a hit arm, a no-hit arm, and an unreadable-manifest arm |
| `PROTOCOL.template.md` §4 · `memory/guides/UNATTENDED-PROTOCOL.md` §4 | the `gates-green` cell |

The held predicate is read from the manifest rather than restated: a leg is held when its `subject`
is `kit` OR its `chunk` is `selftests`, which is the runner's own condition at
`tools/run-gates/run-gates.sh:947`. Parsing is `python3` through the kit's resolver, matching how
other kit scripts read JSON, with a named refusal when the resolver or the file is absent.

### Rollout

The clause fires for this build itself, since its diff touches `tools/unattended/`, which carries
guarded legs. That is the intended first exercise.

### Alternatives rejected

Running the held legs individually. Rejected: `run-gates.sh` exposes no per-leg selection, and adding
one is a change to another kit's public surface.

## 5. Production-readiness checklist

- security — N/A. Reads a tracked manifest and the run's own diff.
- perf / scale — the escalated bar is the self-test-inclusive bar, which `.unattended.conf`'s own
  `GATE_BOUND` comment sizes at roughly 26 minutes of wall clock against a 3600 s bound. Inside it.
- a11y — N/A. No user surface.
- i18n — N/A. No user surface.
- error / empty / loading states — S4 covers the unreadable inputs, loudly.
- observability — the escalation prints the leg name and the path that triggered it.
- risks — a slower close for a run that edited a checker, which is the cost the finding prices. The
  bound breach path is already distinguished from a red leg by `TOOL-aBoundedCeiling-6`'s message.
- testing + left-shift gates — three arms, each observed RED first.
- migration / rollback — deleting the clause restores today's behaviour.
- user docs — `TOOL-aGradedMandate-8` names the escalation in the Skill's `--close` section.

## 6. Acceptance criteria

- **AC1** — When the run's `base..HEAD` diff touches a path in a held leg's `guard` array,
  `gates-green` invokes `GATE_CMD` with `GATE_SELFTESTS=1` in its environment, verified by an arm
  that captures the child's environment through a stub `GATE_CMD`.
- **AC2** — When the diff touches no such path, the child sees no `GATE_SELFTESTS`, verified by the
  same stub.
- **AC3** — When `tools/gate-legs.json` is unreadable, `--close` prints a named skip naming the
  manifest, and does not silently proceed unescalated.
- **AC4** — The escalation announcement names at least one leg from `tools/gate-legs.json` and at
  least one path from the run's own diff.
- **AC5** — `bash tools/unattended/run-unattended-gates.sh --checks` stays green.

## 7. Gates

`unattended kit gate` · `run-gates canary` · `bash tools/run-gates/run-gates.sh` ·
`bash tools/unattended/run-unattended-gates.sh --selftests`.

## 8. Open questions

- **The unattended kit's own five suites remain unreachable.** Options seen: (a) raise `GATE_BOUND`
  above 4611 s and execute them, which edits a declared budget for every adopter; (b) add a recorded
  verdict surface joined to the kit's tree state, which is a new public surface; (c) leave the half
  open, state it in the arm's header, and park the decision. RESOLVED (agent, 2026-08-31,
  delegated): (c). Both (a) and (b) trip the build method's M3 veto 2 — a declared budget and a new
  public surface respectively — so no resolver this mandate delegates exists, and the fork is parked
  through the verb rather than decided here.

## 9. Revision log

- rev-1 · 2026-08-31 · authored from finding F2 of
  `build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md`.

## 10. Reuse audit

The SET-level probes are recorded in `TOOL-aGradedMandate-1` §10.

The seam is `run_bounded` at `tools/unattended/unattended.sh:181`, which already wraps `GATE_CMD`
with the declared bound, the capture-to-file fix and the breach-versus-red distinction. This unit
adds an environment export before that call and changes nothing inside it.

The held-leg predicate is `tools/run-gates/run-gates.sh:947-949` and is READ rather than restated;
`tools/gate-legs.json` is the single source both this arm and the runner consult, so no second copy
of the leg population exists. `tools/lib/resolve-python.sh` is the existing resolver for the JSON
read and is reused rather than re-derived, because the MS-Store `python3` stub answers `command -v`
and exits 9009.
