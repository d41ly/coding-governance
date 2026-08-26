# The owner's prompt — the bar is slow, it hangs, and a landing pays for it twice

**Serves:** research TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-2 TOOL-aBoundedCeiling-3 TOOL-aBoundedCeiling-4

Handed to `/unattended --prompt` on 2026-08-27, node `a`. The value carried whitespace and named no
readable file, so it is the prompt itself and is recorded here verbatim. The bytes travel rather than
the reference: the build folder is the authorization and may not point at a file the run can edit.

## Verbatim

> unattended self-check gates are extremely slow and often hang. The owner had to move them off the
> main bar because they kept clogging/blocking builds. They also separately exist on unattended.sh
> --close execution. Review the problem, build a systemic solution to it that will apply both to this
> repo and its adopters.

## What the orientation pass measured, before any unit was written

Every figure below is from this tree at base `f5dff6ae`, node `a`. The leg timings are
`<git-common-dir>/gate-ledger.tsv`, which the runner writes one row per leg; nothing here is authored.

- **85 legs in `tools/gate-legs.json`. 45 of them are kit-subject or `selftests`-chunk, and they are
  7969 s of leg-time. The other 40 — the ones whose subject is the REPOSITORY — are 1742 s.** So the
  self-tests are 82% of the bar's leg-seconds, and the owner's "extremely slow" is measured, not felt.
- **No per-leg deadline is armed anywhere.** `tools/run-gates/gate-profiles.txt` declares a
  `timeout=<s>` knob, the runner implements it correctly (file-captured, `-k` kill-after, RED naming
  the leg), and the canary grades it — and **every one of the three profile rows sets `timeout=0`.**
  The mechanism is built, tested, and inert. A hung leg wedges the whole bar with no bound.
- **That is a known, still-open defect.** `TOOL-aBoundedVerdict-10` records `unattended driver
  selftest` hanging inside its first `--preflight`, zero output at 240 s, wedging the bar at 46/65.
  Its anchor half landed 2026-08-20. Its own words on the rest: *"The PER-LEG DEADLINE half is not,
  and stays open here; it belongs to `run-gates.sh`, which is a different kit and a different owner."*
- **The charter already states the rule nobody implemented at the bar.** §7: *"every suite declares a
  wall-clock ceiling, a runner REDS on breach, and one arriving without a ceiling reds by that fact."*
  That rule is implemented in `tools/unattended/run-unattended-gates.sh` for eight kit suites, and it
  is absent from `tools/run-gates/run-gates.sh`, where all 85 legs actually run. The discipline exists
  in the wrong place, and the kit script's own header says why that matters: *"A suite added here
  without one would be exempt from the rule by the act of arriving."*
- **A landing pays two bars, and the first one cannot satisfy the second.** `--close` evaluates the
  `gates-green` DoD item by running `$GATE_CMD`, which `.unattended.conf` declares as a plain
  `bash tools/run-gates/run-gates.sh` — no `GATE_SELFTESTS`. It records a green stamped
  `selftests` = held. Then `tools/push-main.sh` fires `.githooks/pre-push`, which sources
  `.githooks/gate-env.sh`, gets `GATE_SELFTESTS=1`, and hits its predicate 8: *"this push runs the kit
  self-tests and the recorded full green was earned with them HELD."* That sets `GATE_FULL=1`.
- **`GATE_FULL=1` bypasses every guard.** 47 of the 85 legs carry a `guard` naming the kit dir they
  exercise, which is the mechanism that keeps a records-only commit from running kit self-tests. The
  forced run switches all of them off. So an unattended landing that touched nothing but `memory/`
  still pays all 45 self-test legs, because of a mismatch between two bar runs rather than because of
  anything it changed.
- **The cost is process creation, not work**, and that is already catalogued as a class in
  `memory/gotchas/process-creation-is-the-suite-cost.md`: 469 spawns per invocation of one leg, 243
  invocations per suite, ~114,000 process creations, 93% of wall spent waiting on an on-access
  antivirus scanner. The gotcha states plainly that no portable machine gate for this class can exist,
  and that what replaces it is a declared ceiling per suite — the thing the bar does not have.

## What is NOT in scope, and why it is written down here

**Re-adding the unattended kit's seven `*.test.sh` legs to `tools/gate-legs.json` is out.** Removing
them was an owner ruling dated 2026-08-23, recorded in `AGENTS.md` and in the kit's own gate-runner
header. Nothing in this build overturns it, and no unit may put those legs back.

**Per-leg spawn-count engineering is out.** It is real work with a measured lever — one leg already
went 469 spawns to 220 — but it is instance work, one leg at a time, and it is what a ceiling FORCES
rather than what a ceiling IS. This build makes the cost a verdict; the verdicts then name the legs
worth the surgery.
