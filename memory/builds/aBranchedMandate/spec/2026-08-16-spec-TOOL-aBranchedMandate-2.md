# TOOL-aBranchedMandate-2 — a checkout artifact stops refusing every unattended run in a worktree

**Status:** SPECCED · rev-3 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling · ratified 2026-08-16

## 1. Goal

`tools/check-wiring.sh --check` exits non-zero when a worktree carries CRLF on an `eol=lf`-pinned
`.claude/` Skill render, and `.unattended.conf` declares that command as `WIRING_CHECK`, so
`--preflight` refuses there and — because the protocol forbids the driver from running the repairing
mode — cannot recover. Make the eol arm report without gating, and make the driver's refusal surface
the declared check's own output for the cases that still gate.

## 2. Scope (IN)

- **S1** — the eol arm of `tools/check-wiring.sh` no longer contributes to the exit status of
  `--check`. It keeps its line under the label `note`, distinct from `UNWIRED`, because the condition
  is a working-copy artifact and not dormant wiring.
- **S2** — `--fix` still rewrites those bytes, and `--session` still does not. Neither behaviour
  moves; only the exit status of `--check` does.
- **S3** — the arm at `tools/check-wiring.test.sh:248` moves from "eol alone gives rc 1 and an
  UNWIRED line" to "eol alone gives rc 0 and a `note` line", and a sibling arm asserts that a
  genuinely dormant item in the same run still gives rc 1. Without the sibling, S1 is
  indistinguishable from having deleted the arm. The arms also establish whether any consumer greps
  for the literal `UNWIRED` on this path, which is the one fact that would have argued for keeping
  the word.
- **S4** — `check_wiring` in `tools/unattended/unattended.sh` **surfaces the declared check's own
  output** on failure instead of discarding it. Today the call is
  `$WIRING_CHECK >/dev/null 2>&1` (`:419`), and the output it throws away already carries the remedy:
  `tools/check-wiring.sh:277` prints `Fix: bash tools/check-wiring.sh --fix`. The refusal message
  itself is unchanged.

  **S4 previously said the refusal should NAME the repair command, and that was wrong twice over.**
  Nothing the kit may read holds one — `.unattended.conf` declares no repairing counterpart, the
  protocol's key table has none, and `check_wiring`'s own allow-list refuses any `WIRING_CHECK` token
  outside `--check|--dry-run|--verify|-n`, so it cannot be derived from the declaration either. And
  `tools/unattended/unattended.test.sh:921` carries a source-level arm that FAILS the driver
  self-test if the driver source spells that command at all. A builder implementing the old S4 would
  have red a leg this spec's own §7 lists. Surfacing the declared check's output is the route §4
  never considered: it works for any adopter, needs no new declaration, and spells nothing.
- **S5** — the corresponding arm in `tools/unattended/unattended.test.sh` is CHECKED, and rewritten
  only if it actually moved. `signature()` in `tools/memory-tree/check-arms.py:104-113` splits on
  every interpolation and returns `max(parts, key=len)` — the longest surviving literal run — and S4
  no longer touches the message at all, so the existing signature and its arm at
  `unattended.test.sh:188` stand. `ARMS_FLOORS` in `.memory-tree.conf` is re-measured rather than
  assumed, but the expected outcome is now "unchanged", not "moved".

## 3. Non-goals (OUT)

- Letting the driver run a repairing wiring mode. `memory/guides/UNATTENDED-PROTOCOL.md` section 7
  forbids it and gives the reason — that mode sets git config and rewrites tracked bytes, and its
  past over-firing is the cautionary case the protocol cites. This unit does not relitigate it.
- Weakening check 4 itself. Every other thing `check-wiring.sh` reports still gates preflight, which
  is the point of S3's sibling arm.
- Changing `.gitattributes`, the render, or the eol arm's derived population.
- Changing the protocol text. The contract — delegate to a non-repairing check — is unchanged, so
  `PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md` do not move and their parity
  check is not in play.
- Bumping `KIT_UNATTENDED_VERSION`. Resolved in §8 F2: the version moves once, in node `c`'s build.

## 4. Design

The chain, each link measured in this worktree:

1. A live worktree carries CRLF on the `eol=lf`-pinned `.claude/` renders, and `git status` stays
   clean because the index normalises on commit. **The writer is not `git worktree add`** — a scratch
   worktree made that way measures CR=0 and both checks green. It is the agent harness's worktree
   creation; all five live worktrees carry it, the primary checkout does not, and the condition is
   confined to `.claude/`. The measurement and what remains UNVERIFIED about the writer are in the
   reproduction record under this build's `build/`.
2. The eol arm reports UNWIRED for the three pinned `.claude/skills/*/SKILL.md` renders and
   `--check` exits 1.
3. `.unattended.conf` declares `WIRING_CHECK="bash tools/check-wiring.sh --check"`.
4. `check_wiring` in the driver refuses with check 4, and `--preflight` writes nothing.

Observed against a build that is fully landed on the default branch, so the authorization rule is
not in play:

```
$ bash tools/unattended/unattended.sh --preflight aBatchedLintel --keepalive-id probe
UNATTENDED check 4 FAILED — the declared wiring check failed, and a dormant hook makes every
later green meaningless: bash tools/check-wiring.sh --check
```

The refusal's own reasoning is what makes the fix a severity change rather than an exemption: "a
dormant hook makes every later green meaningless". A CRLF working copy is not a dormant hook. It
disables nothing, and the committed bytes are already correct.

### Why the exit status is unfunded once `TOOL-aBranchedMandate-1` lands

The eol arm states its own harm: "a byte-comparing gate will report every line as drift". That harm
was real — one gate did. `TOOL-aBranchedMandate-1` gives the last of the three pinned renders the
normalising comparison its siblings have, after which no gate in this tree reds on CR. The arm then
reports a condition with no consequence, while setting an exit status that a downstream consumer
treats as a refusal.

**The dependency is hard and the order is total.** Landing S1 before
`TOOL-aBranchedMandate-1` would silence a signal that is still predicting a real red leg, which is
the opposite of this unit's argument.

### Why a working-copy CRLF is a working-copy condition and not a repository defect

**This argument was re-made after the spec audit refuted its first version**, which reasoned that
committed blobs are normalised on commit and therefore "a CRLF working copy only ever comes from the
checkout filter". Measurement refuted the premise: the checkout filter is not where this CRLF comes
from, so the derivation was unsound even though its conclusion survives.

What holds, and why: the committed bytes are LF on every node — verified in the primary checkout and
in a scratch `git worktree add` — so no repository state is wrong, no consumer reading the tracked
blob sees CRLF, and the condition is confined to the working copy of `.claude/` in harness-created
worktrees. `--fix` rewrites those bytes with no other effect. It is a condition worth reporting and
not worth refusing a run over.

**What is NOT claimed, because the writer is unidentified.** This does not assert that CRLF can never
signal a defect. If the unidentified writer is ever found to be a renderer emitting wrong bytes, this
argument is reopened, and S1 would have removed the exit status that reported it. That residual is
carried as F4 in §8 rather than argued away here — it is the honest cost of acting on a measurement
whose mechanism is only partly known.

### Data model

The script's report vocabulary today is `ok` / `skip` / `UNWIRED` / `fixed`. This unit adds `note`
for a condition that is true, worth printing, and not a refusal. `UNWIRED` is the only member that
gates, and reusing it here would make the one word that means "this gates" stop meaning it.

`skip` is NOT the answer for this condition and must not be reached for. It means the population was
empty — no `eol=lf`-pinned file under `.claude/` — and a population of zero and a population that is
all-CRLF are different answers the script already distinguishes.

### The declaration does not move

`.unattended.conf` keeps `WIRING_CHECK="bash tools/check-wiring.sh --check"` unchanged. With the eol
arm advisory, `--check` reports only gating items, so the declaration is correct as written and the
driver still delegates to the same non-repairing mode protocol section 7 requires. This is recorded
because it is the first thing an adopter will ask after reading S1, not because anything about it is
undecided.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/check-wiring.sh` | S1, and the header sentence that says why |
| `tools/check-wiring.test.sh` | S3, both arms |
| `tools/unattended/unattended.sh` | S4 |
| `tools/unattended/unattended.test.sh` | S5 |
| `.memory-tree.conf` | S5, the `ARMS_FLOORS` pair for the driver |

### Alternatives rejected

- **Declare a different `WIRING_CHECK` in `.unattended.conf`.** It fixes this repo and leaves every
  adopter with the trap, and it makes the project layer carry a workaround for a kit defect.
- **Make the driver tolerate a non-zero wiring exit.** That deletes check 4. The other things
  `check-wiring.sh` reports — an unset `core.hooksPath`, an unwired agent-cap hook — are exactly the
  dormant-gate class the check exists for.
- **Have the run repair before preflight.** Forbidden by protocol section 7, and the ordering makes
  it worse than it sounds: the repairing mode would run before any of the preconditions that decide
  whether the run may start at all.
- **Teach the eol arm to recognise a linked worktree and skip there.** It would still gate in the
  primary tree for a condition that is equally harmless there, and it adds a special case whose
  premise — that the primary tree cannot hold CRLF — is not enforced anywhere.

## 5. Production-readiness checklist

- security — the surface that changes is a *report severity*, not an authorization path. Nothing
  about what `--preflight` accepts as an authorization moves; that is
  `TOOL-aBranchedMandate-3`. The risk is the generic one of downgrading a check, which S3's sibling
  arm exists to bound.
- perf / scale — N/A. No new work in either mode.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the arm's existing `skip` path (no `eol=lf`-pinned file under
  `.claude/`) must remain a `skip` and must not become the new advisory label. A population of zero
  and a population that is all-CRLF are different answers and the script already distinguishes them.
- observability — improved on both sides: the wiring report stops crying wolf, and the driver stops
  discarding the declared check's diagnostics, which already carry a remedy the driver may not spell
  itself.
- risks — the real one is that S1 makes a future adopter's un-normalised byte-compare invisible in
  the wiring report. It does not: the report still prints. What is lost is the exit status, and the
  red would come from that adopter's own leg, which is where it belongs.
- testing + left-shift gates — S3 and S5. A severity downgrade with no arm asserting the *retained*
  refusal is indistinguishable from a deletion, and that is the single most likely way this unit goes
  wrong.
- migration / rollback — revert both commits together. Reverting this unit alone leaves the wiring
  report advisory-labelled with the leg it was warning about already fixed, which is harmless but
  incoherent.
- user docs — the header of `tools/check-wiring.sh` states the new severity rule and why.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-wiring.sh --check` runs in a tree whose pinned `.claude/` renders
  have been given CRLF **deliberately** and nothing else is unwired, it exits 0 and still prints one
  line per affected path. The fixture is constructed: a `git worktree add` tree measures CR=0, so the
  earlier wording named a fixture that does not produce the condition.
- **AC2** — When the same command runs with `core.hooksPath` unset in that same constructed tree, it
  exits 1 and names the hooks item. This is S3's sibling arm and it is what proves AC1 is a severity
  change rather than a deleted arm.
- **AC3** — When `bash tools/unattended/unattended.sh --preflight <slug> --keepalive-id <id>` runs in
  that constructed tree against a build that is on the default branch, it no longer refuses at
  check 4. Re-keyed for the same reason as AC1: against a plain `git worktree add` tree this was
  already true at BASE and observed nothing.
- **AC4** — When the declared `WIRING_CHECK` fails for a reason that is not the eol arm, check 4
  still refuses, **and the declared check's own output appears in the driver's output**. Proven with
  a `WIRING_CHECK` whose failure message is a distinctive literal, asserting that literal reaches the
  operator. The earlier wording — that the message names the repair command — is not implementable:
  see S4.
- **AC8** — When `grep -nE 'check-wiring[^"]*--fix'` runs over `tools/unattended/unattended.sh`
  excluding comments, it finds nothing, so `tools/unattended/unattended.test.sh:921` stays green.
  This is an explicit non-regression on the arm the earlier S4 would have broken.
- **AC5** — When `bash tools/check-wiring.test.sh` runs, both the changed arm and its sibling pass,
  and the sibling fails if S1 is applied to the hooks item by mistake.
- **AC6** — When `python tools/memory-tree/check-arms.py` runs, every branch of
  `tools/unattended/unattended.sh` is still armed, and the `ARMS_FLOORS` pair for that file in
  `.memory-tree.conf` matches a fresh measurement rather than the pre-change value.
- **AC7** — When `bash tools/check-wiring.sh --fix` runs in a fresh worktree, it still rewrites the
  CRLF paths to LF, and `bash tools/check-wiring.sh --session` still does not.

## 7. Gates

- `bash tools/run-gates.sh` — the full bar, with `GATE_FULL=1` at the push boundary.
- `bash tools/check-wiring.test.sh` — the wiring-health self-test leg, which S3 edits.
- `bash tools/unattended/unattended.test.sh` — the driver self-test leg, which S5 edits.
- `python tools/memory-tree/check-arms.py` — the harness meta-gate, and the `ARMS_FLOORS` pins in
  `.memory-tree.conf` that AC6 re-measures.
- `bash tools/check-kit-versions.sh` — reds if the driver's and the leg's version literals disagree,
  which is the failure mode F2 is about.

## 8. Open questions

F4 is OPEN. F1 and F2 are RESOLVED below, and a third was reclassified out of this section. F4 was
opened by the spec audit after those resolutions, so this spec is FORKED under M2 until it is
answered, and its status may not go terminal before then.

- **F1 — the label for the advisory line.** The report vocabulary is `ok` / `skip` / `UNWIRED` /
  `fixed`, all lowercase except the one that gates. Options: `note`, or `advisory`, or keeping
  `UNWIRED` and relying on the exit status alone. **RESOLVED (owner, 2026-08-16): `note`.** It is
  short enough to keep the existing column alignment, and reusing `UNWIRED` for a non-gating
  condition makes the one word that means "this gates" stop meaning it, which is how a report trains
  its readers to skip it. S3's arms still establish whether any consumer greps for the literal, which
  is the fact that would have argued the other way.
- **F2 — does this unit bump `KIT_UNATTENDED_VERSION`?** The gate asserts only that the driver's and
  the leg's literals agree, not that a change bumps them, so nothing forces it. Against bumping:
  node `c`'s in-flight build takes this kit to 1.5 across both literals and the shipped doc marker,
  and two builds moving one version is a merge conflict in a value whose whole purpose is to be
  unambiguous. **RESOLVED (owner, 2026-08-16): do not bump, and land without waiting on node `c`.**
  The version moves once, in the build that owns the move; this build's README records that the
  driver changed under 1.4. The owner accepted the merge cost on the shared files rather than
  sequencing behind an unrelated build.

**F3 was not a fork and has been reclassified.** It asked whether `WIRING_CHECK` is still the right
declaration afterwards. It presented no options and no trade — the answer is entailed by F1 — so it
belonged in §4 as a stated consequence rather than here as a decision. It now sits under "The
declaration does not move". Recorded rather than silently deleted, because a fork that disappears
between revisions is indistinguishable from one that was answered off the record.

- **F4 — UNRESOLVED, opened by the spec audit.** The CRLF writer is unidentified. Measurement
  establishes that it is not `git worktree add`, that it is confined to `.claude/`, that it is
  systematic across all five harness-created worktrees, and that the committed bytes are correct
  everywhere. It does not establish WHAT writes it. S1 removes the exit status that reports the
  condition, so if the writer is later found to be a renderer emitting wrong bytes, this unit will
  have silenced a real signal. Options: **(a) land S1 as specified** and accept that the report
  remains and only the gating goes, on the grounds that the committed bytes are measured correct;
  **(b) identify the writer first**, which is an unscoped investigation into tooling outside this
  repo; **(c) land S1 but keep the exit status non-zero in the PRIMARY checkout only**, where no
  harness writer operates — a special case whose premise nothing enforces, and the shape §4 already
  rejects. **Recommendation: (a).** The report survives, the gotcha class stays visible, and the
  alternative blocks a fix for a live deadlock on an investigation with no bounded end. This is an
  owner turn because it decides how much unexplained mechanism a severity downgrade may rest on.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft, from the reproduction recorded under this build's `build/`.
- rev-2 · 2026-08-16 · F1 and F2 resolved by the owner; the label `note` folded into S1, S3 and §4's
  data model; F3 reclassified out of §8 into §4 with the reclassification recorded in place.
- rev-3 · 2026-08-16 · folded the spec audit recorded under this build's `reviews/`. C10: S4 demanded
  a repair-command literal the kit cannot hold and that `unattended.test.sh:921` reds the driver for
  spelling — S4 now surfaces the declared check's own output instead, with AC4 re-keyed and AC8 added
  as an explicit non-regression on that arm. C13: the placement rule in S4 and the claim in §10 both
  inverted what `check-arms.py` does — it takes the LONGEST literal run, not the run before the first
  interpolation — so S5 becomes a check rather than a forced rewrite. C1: §4's chain step 1 and AC1
  and AC3 were keyed to `git worktree add`, which does not produce the condition; all three re-keyed
  to a constructed fixture, and §4's artifact argument re-derived after its premise was refuted. F4
  opened for the unidentified writer.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py` surfaced no seam for a report-severity change, which is
the honest answer: this unit adds no mechanism. It reuses two that exist. The report vocabulary and
its column layout are `tools/check-wiring.sh`'s own, and S1 adds a member rather than a second
reporting path. S4 reuses the driver's own `$WIRING_CHECK` invocation, dropping the `>/dev/null 2>&1`
that discards a diagnostic the declared check already produces — the smallest possible change, and
the one that needs no new declaration.

**An earlier revision of this section stated a rule that is false**, and it is corrected here rather
than deleted because it was the stated basis for a scope item. It claimed "a branch's literal
signature ends before its first interpolation". `signature()` at
`tools/memory-tree/check-arms.py:104-113` splits the message on EVERY interpolation and returns
`max(parts, key=len)` — the longest surviving literal run, wherever it sits. The real trap the
driver's own comments describe at `check_slug` and `stage_or_fail` is a different one: a bare
positional is not matched as an interpolation and so stays inside the literal run, which is why those
messages bind their values to names. This unit no longer edits the message at all, so neither rule
binds it.
