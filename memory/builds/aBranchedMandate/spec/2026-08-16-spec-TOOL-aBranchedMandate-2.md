# TOOL-aBranchedMandate-2 — a checkout artifact stops refusing every unattended run in a worktree

**Status:** SPECCED · rev-1 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

`tools/check-wiring.sh --check` exits non-zero when a `git worktree` checkout lands CRLF on an
`eol=lf`-pinned Skill render, and `.unattended.conf` declares that command as `WIRING_CHECK`, so
`--preflight` refuses in every fresh worktree and — because the protocol forbids the driver from
running the repairing mode — cannot recover. Make the eol arm report without gating, and make the
driver's refusal name its remedy for the cases that still gate.

## 2. Scope (IN)

- **S1** — the eol arm of `tools/check-wiring.sh` no longer contributes to the exit status of
  `--check`. It keeps its line, under a label distinct from `UNWIRED`, because the condition is a
  working-copy artifact and not dormant wiring.
- **S2** — `--fix` still rewrites those bytes, and `--session` still does not. Neither behaviour
  moves; only the exit status of `--check` does.
- **S3** — the arm at `tools/check-wiring.test.sh:248` moves from "eol alone gives rc 1 and an
  UNWIRED line" to "eol alone gives rc 0 and the advisory line", and a sibling arm asserts that a
  genuinely dormant item in the same run still gives rc 1. Without the sibling, S1 is
  indistinguishable from having deleted the arm.
- **S4** — check 4's refusal in `tools/unattended/unattended.sh` names the repair command, so an
  attended operator who meets a wiring refusal is told what to run. The remedy goes BEFORE the
  interpolation, because a literal word after it lands inside the branch signature `check-arms.py`
  matches and no assertion can then arm the branch.
- **S5** — the corresponding arm in `tools/unattended/unattended.test.sh` is updated to the new
  literal signature in full, and `ARMS_FLOORS` in `.memory-tree.conf` is re-measured for
  `tools/unattended/unattended.sh` rather than assumed unchanged.

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
- Bumping `KIT_UNATTENDED_VERSION`. See §8 F2.

## 4. Design

The chain, each link measured in this worktree:

1. `git worktree add` lands CRLF on paths `.gitattributes` pins `eol=lf`. `tools/check-wiring.sh:194`
   states this in its own source, and `git status` stays clean because the index normalises on
   commit.
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

### Why a working-copy CRLF is always an artifact and never a defect

Committed blobs are normalised by the index on commit, so a pinned path's committed bytes are LF on
every node. A CRLF working copy therefore only ever comes from the checkout filter. The arm cannot
observe a case where CRLF means something is broken, which is precisely what makes it a diagnostic.

### Data model

The script's report vocabulary today is `ok` / `skip` / `UNWIRED` / `fixed`. This unit adds one
member for a condition that is true, worth printing, and not a refusal. The label is F1.

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
- observability — improved on both sides: the wiring report stops crying wolf, and the driver's
  refusal starts naming a remedy.
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

- **AC1** — When `bash tools/check-wiring.sh --check` runs in a fresh worktree whose only finding is
  CRLF on pinned Skill renders, it exits 0 and still prints one line per affected path.
- **AC2** — When the same command runs with `core.hooksPath` unset in that same worktree, it exits 1
  and names the hooks item. This is S3's sibling arm and it is what proves AC1 is a severity change
  rather than a deleted arm.
- **AC3** — When `bash tools/unattended/unattended.sh --preflight <slug> --keepalive-id <id>` runs in
  a fresh worktree against a build that is on the default branch, it no longer refuses at check 4.
- **AC4** — When the declared `WIRING_CHECK` fails for a reason that is not the eol arm, check 4
  still refuses, and its message names the repair command.
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

- **F1 — the label for the advisory line.** The report vocabulary is `ok` / `skip` / `UNWIRED` /
  `fixed`, all lowercase except the one that gates. Options: `note`, or `advisory`, or keeping
  `UNWIRED` and relying on the exit status alone. **Recommendation: `note`.** It is short enough to
  keep the existing column alignment, and reusing `UNWIRED` for a non-gating condition makes the one
  word that means "this gates" stop meaning it, which is how a report trains its readers to skip it.
  Keeping `UNWIRED` is the option to pick only if some consumer greps for that literal, which S3's
  arms will reveal.
- **F2 — does this unit bump `KIT_UNATTENDED_VERSION`?** The gate asserts only that the driver's and
  the leg's literals agree, not that a change bumps them, so nothing forces it. Against bumping:
  node `c`'s in-flight build takes this kit to 1.5 across both literals and the shipped doc marker,
  and two builds moving one version is a merge conflict in a value whose whole purpose is to be
  unambiguous. **Recommendation: do not bump here.** Let the version move once, in the build that
  owns the move, and note in this build's README that the driver changed under 1.4. Revisit if this
  unit lands after that one, in which case it rides 1.5 and this fork is moot.
- **F3 — is `.unattended.conf`'s `WIRING_CHECK` still the right declaration afterwards?** With the
  eol arm advisory, `--check` in this repo reports only gating items, so the declaration is correct
  as written. Recorded rather than resolved because it is the question an adopter will ask when they
  read S1 and then read their own conf. **Recommendation: no change.**

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft, from the reproduction recorded under this build's `build/`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py` surfaced no seam for a report-severity change, which is
the honest answer: this unit adds no mechanism. It reuses two that exist. The report vocabulary and
its column layout are `tools/check-wiring.sh`'s own, and S1 adds a member rather than a second
reporting path. The refusal-message shape in S4 reuses the driver's established rule that a branch's
literal signature ends before its first interpolation — stated in `tools/unattended/unattended.sh` at
`check_slug` and at `stage_or_fail`, and enforced by `tools/memory-tree/check-arms.py`. No new file
is created by this unit, which is the strongest available evidence that nothing needed inventing.
