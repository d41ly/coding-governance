# KICK-cKeyedLaunchpad-7 — the engine's prose pass, and the three strings it must not touch

**Status:** OPEN · rev-3 · 2026-08-13 · node c · Tier-1 · base f006691f · streams kickoff+tooling

## 1. Goal

Correct the engine's remaining false claim, trim what U2 through U6 made redundant, and put the file
under a measured size gate — the artifact that instructs adopters to keep their manifest short is itself
15,604 bytes and ungated, in a repo that byte-gates its playbook at 32 KiB.

## 2. Scope (IN)

- S1. *(Dropped at rev-2.)* The spec-section count sat inside Step 3's Risk-tier bullet, which
  `KICK-cKeyedLaunchpad-4` deletes whole. Correcting a line another unit removes would have been a
  conflict, not a fix. That unit's §4 now records where the count and the no-tiers heuristic land.
- S2. Correct the Scaffolding section's check-script destination, and the runbook line that still
  contradicts its own installation step.
- S3. Trim the prose that U2 through U6 make redundant, and nothing else.
- S4. `tools/check-template-size.sh` accepts its limit as a POSITIONAL argument, falling back to the
  environment and then to its current default.
- S5. A second gate leg runs that script over the engine, with a limit MEASURED after S3's trim.
- S6. The three artifacts a new leg obliges: the charter's gate-suite citation, a dossier claim for
  the leg name, and a map regeneration.

## 3. Non-goals (OUT)

- **Three strings in this file are load-bearing for another kit and must not be touched.** §4 names
  them. This is the single largest risk in an otherwise cosmetic unit.
- **The memory-recall kit's dual-spelling resolution in Step 4 stays.** The adversarial review that
  opened this build listed it as drift to eliminate. That was wrong: both spellings ship, and the
  hedge is live waivered policy rather than an unresolved inconsistency. It is recorded here so the
  correction survives the review that caused it.
- **No new gate script.** §4 gives the arithmetic; a sibling script costs four things a second leg
  does not.
- **No reuse of the playbook's 32 KiB number.** A limit far above anything this file will reach is a
  vacuous gate, and this repo has a record for that exact failure.
- U2 owns the manifest-path corrections in this file; this unit owns the check-script path.

## 4. Design

### The remaining false claim

The spec-section count is NOT fixed here. It sits inside Step 3's Risk-tier bullet, which
`KICK-cKeyedLaunchpad-4` deletes whole, so correcting it here would be a conflict rather than a fix;
that unit's §4 records where the figure and the no-tiers heuristic land. One observation is kept
because it outlives the line: the claim survived two prior builds that fixed the same nine-against-ten
error elsewhere, because the phrase is hard-wrapped across two source lines and a single-line
`git grep` for it returns nothing — the absence-assertion class this repo has a record for, hiding a
claim from a review looking for exactly it.

The Scaffolding section directs the checker to a root-level script directory. The runbook installs it
under the kit prefix — and then, four hundred lines later, emits a pre-commit snippet pointing back at
the root-level path. Three spellings, one file, and the root-level one is the install-prefix class
this repo has a gate for that does not reach this text.

### The three strings that are not prose

The unattended kit's gate greps THIS file for three things, and a prose pass is exactly the kind of
change that breaks them while looking harmless:

| What is asserted | How a prose pass breaks it |
|---|---|
| the literal `Step 5b` | renaming or renumbering the section |
| the exact READY prompt sentence — the em-dash is U+2014, the apostrophe is straight ASCII | "restoring" a curly apostrophe, or rewording the hand-back |
| at least six lines matching a numbered bold `Step` prefix | reformatting the six interactive exits as a table, or renumbering them |

Each failure reports as an unattended-run defect, not as a prose defect, so the message would point
away from the edit that caused it. The trim must leave all three intact, and the acceptance criteria
assert them directly rather than trusting care.

**Exactly one byte in that sentence is multibyte.** Verified with `od -c` on both the engine and the
`grep -qF` that reads it: the dash is U+2014 and the apostrophe is straight ASCII `0x27`. rev-1 said
"curly apostrophe", which was false about source in the one paragraph telling a builder which bytes
are load-bearing — a pass that dutifully "restored" the curly form would have broken the very gate the
paragraph exists to protect.

### Why the size gate is a second leg, not a new script

`check-template-size.sh` already takes the file as its first argument, already measures LF-normalised
bytes, and is already a govkit entry. A sibling script would be pulled into the harness meta-gate by
its own discovery rule — any tracked shell file defining a fail helper — and would then need a test
file with a positive arm per branch, an arms-floor entry, and a govkit entry of its own. That is four
obligations to avoid reusing a script that already does the work.

The limit cannot arrive by environment. The gate runner execs its argument vector directly with no
shell, and its canary pins the first argument to a known interpreter, so neither an `env` prefix nor
a variable assignment is a legal leg. S4's positional is the one-line change that makes a second leg
possible at all.

### The limit is measured, not chosen

The file is 15,604 bytes before S3's trim. Reusing the playbook's 32 KiB would ship a gate at more
than double the file's size — always green, gating nothing, which is precisely the ported-pin failure
this repo has a record for. The limit is therefore set AFTER the trim, from the trimmed size plus a
stated margin, and the number lives beside the measurement rather than in prose that will rot.

The file also carries an `eol=lf` pin that nothing repairs: the wiring check's normalisation is scoped
to a different directory, and this engine has already come out of a worktree carrying CR bytes. The
reused script strips CR, which is a further argument for riding it rather than writing a counter.

### Files touched (estimate)

| File | Change |
|---|---|
| `skills/session-kickoff/SKILL.md` | S2 and S3 only; S1 is dropped and its line is deleted by unit 4 |
| `WIRE-INTO-PROJECT.md` | the contradicting pre-commit snippet |
| `tools/check-template-size.sh` | the positional limit |
| `tools/gate-legs.json` | the second leg |
| `AGENTS.md` | the gate-suite citation the drift signal requires |
| `memory/map/features/` + `generated/` | the leg claim and the regeneration |

### Alternatives rejected

- **A sibling size script.** Four extra obligations, listed above.
- **Reusing 32 KiB.** A vacuous gate.
- **Setting the limit before the trim.** Bakes in the slack the trim is meant to remove.
- **Rewording the hand-back for concision.** Breaks a gate in another kit and reports as an unrelated
  failure.

## 5. Production-readiness checklist

- security — N/A; prose and one reused byte counter.
- perf / scale — one additional leg, one file read, and the runner is concurrent.
- a11y — N/A. i18n — the counter measures LF-normalised bytes, as it already did.
- error / empty / loading states — the reused script already handles a missing file as an environment
  error.
- observability — the leg names the file and the measured size against the limit.
- risks — the three load-bearing strings; asserted in §6 rather than trusted.
- testing + left-shift gates — the new leg IS the left shift for F7; S2's correction is one-time and
  is covered by the leg only insofar as it bounds regrowth.
- migration / rollback — adopters are unaffected; the leg is gov-only and the positional argument is
  backward compatible with every existing call.
- user docs — the runbook's contradicting snippet is the doc fix.

## 6. Acceptance criteria

- AC1. *(Dropped at rev-2 with S1 — the line lives in a bullet `KICK-cKeyedLaunchpad-4` deletes.)*
- AC2. No path in this file or in the runbook's pre-commit snippet names a root-level script
  directory for the checker.
- AC3. `grep -F 'Step 5b'` over the engine matches. This is asserted after the trim, not before.
- AC4. `grep -F` for the exact READY prompt sentence matches, byte for byte — the em-dash preserved as
  U+2014 and the apostrophe left as straight ASCII.
- AC5. `grep -cE` for the numbered bold `Step` prefix returns at least six.
- AC6. `bash tools/unattended/check-unattended.sh` passes — the direct proof that AC3 through AC5 hold
  in the form that gate actually reads.
- AC7. `bash tools/check-template-size.sh <file> <limit>` honours the positional limit, and omitting
  it preserves the existing default for the playbook's own leg. Observed by a build-time scratch
  assertion, not by a gate leg: §7 names no carrier for it, because none exists and this unit does not
  fund one.
- AC8. The script exits non-zero when the named file exceeds the given limit — same build-time scratch
  assertion, a temporary file over the limit. `tools/run-gates.test.sh` cannot decide this: it is the
  manifest canary, parsing `gate-legs.json` for name and argv shape, and it never executes a leg.
- AC9. The configured limit is within a stated margin of the trimmed size — not a round number
  inherited from another file.
- AC10. `python tools/drift-audit/drift_report.py --check` passes with the new leg's script path cited
  in the charter's gate-suite section, the signal being pinned at zero with no tolerance.
- AC11. `python tools/codebase-map/test_codebase_map.py` passes with the new leg claimed by a dossier
  and the generated artifacts freshly rendered.
- AC12. `GATE_FULL=1 bash tools/run-gates.sh` is green.

## 7. Gates

- `bash tools/unattended/check-unattended.sh` — the gate this unit is most likely to break.
- `bash tools/check-template-size.sh` and the new leg over the engine.
- `bash tools/run-gates.test.sh` — the canary validates the new leg's SHAPE in `gate-legs.json`. It is
  named for that and nothing more: it never executes a leg, so it does not and cannot decide AC7 or
  AC8, which are build-time assertions by §6.
- `python tools/drift-audit/drift_report.py --check` · `python tools/codebase-map/test_codebase_map.py`
- `GATE_FULL=1 bash tools/run-gates.sh`.

## 8. Open questions

none. The size-gate shape and the limit's derivation are settled in §4 on measured grounds, and the
one claim this unit reverses — the memory-recall dual-spelling — is recorded in §3 rather than left as
an inconsistency between this spec and the review that opened the build.

## 9. Revision log

- rev-1 · 2026-08-13 · initial draft, grounded by workflow `wf_0aaecb50-a51`.
- rev-3 · 2026-08-13 · folded the M4 fix-verify pass. Dropping S1 and AC1 at rev-2 left four live
  references still instructing the edit unit 4 now performs: §1's "two false claims", the §4
  subsection arguing the correction, the Files-touched row, and §5's testing row. All four now
  match the dropped scope, and the one observation worth keeping — how the claim survived two prior
  builds — is retained without the instruction.
- rev-2 · 2026-08-13 · folded the M4 spec audit, review record 1. M6: §4 and AC4 claimed the READY
  sentence carries a curly apostrophe; `od -c` shows straight ASCII, with only the em-dash multibyte —
  a false statement about source in the one paragraph naming the load-bearing bytes, which would have
  had a builder break the gate by "restoring" it. M4: S1 and AC1 corrected a line inside a bullet
  `KICK-cKeyedLaunchpad-4` deletes whole; both dropped, and that unit records the disposition. M5: §7
  credited the run-gates canary with deciding AC7 and AC8, which it cannot — it never executes a leg;
  both are restated as build-time assertions and the gate claim is withdrawn. H7: the `--for-paths`
  call site returns to `TOOL-cKeyedLaunchpad-5`, which owns the verb.

## 10. Reuse audit

`tools/check-template-size.sh` is the seam and it is extended by one line rather than copied. It
already accepts a file argument, already normalises CR, already refuses to raise its own limit in its
remedy text, and is already a govkit entry — everything a second file needs except a parameterised
limit. The four obligations a new script would drag behind it, through the harness meta-gate's
discovery rule, are the concrete cost this audit avoided.

`reuse_lookup.py "gate a document's size and line length"` returned this same script as the top
candidate for U3, where it was the right mechanism in the wrong home. Here it is both, which is the
distinction worth recording: U3 needed the behaviour inside a kit that adopters re-pull, and this unit
needs a gov-only leg over a gov-only file. The same probe answered two units differently, and the
difference is who consumes the result.

Recall terms used: `kickoff manifest ratchet last-audit watch verify-paths SESSION-KICKOFF discovery
order traps accretion size gate prose`.
