# DEPL-cMendedVintage-12 — `apply`'s CONFIGURE honours `deploy["inert"]`

**Status:** SPECCED · rev-1 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 18

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |

<!-- /gen:spec-records -->

## 1. Goal

`deploy.toml`'s `inert` list is a posture the target declared: do not run this kit's adopter. Exactly
one place in the engine reads it — `update`'s re-render block — and `apply`'s CONFIGURE phase runs
every selected kit's `[adopt].argv` without consulting it. So the verb every runbook recommends as
the fallback flips the posture the operator wrote down. Make CONFIGURE read the key that already
exists.

## 2. Scope (IN)

- **S1** A one-function reader, `inert_kits(deploy)`, returns `{str(x) for x in (deploy.get("inert")
  or [])}`. The set comprehension at `tools/govkit/govkit.py:7389` is replaced by a call to it, so
  the two consumers cannot answer the question differently. Observed by AC1 and AC4.
- **S2** In `_cmd_apply`'s CONFIGURE loop, ahead of the argv resolution at
  `tools/govkit/govkit.py:4889`, a kit in that set is declined: one printed line naming the kit and
  the posture, the kit added to `configure_skipped`, and `continue`. The adopter is not resolved and
  not run. Observed by AC1 and AC2.
- **S3** An `inert_declined` set feeds the OBSERVE phase at `tools/govkit/govkit.py:4935`. A
  `rendered` destination absent because its adopter was declined is REPORTED with that reason, not
  failed — the existing branch does the same for a kit that stopped at an accepted outcome, and this
  is the second reason a render can be legitimately absent. Observed by AC3.
- **S4** The decline prints on every `apply` run that has an inert kit in its selection, including a
  run where nothing else happens. A posture that silently changes what a verb does must be visible
  in that verb's output. Observed by AC1.

## 3. Non-goals (OUT)

- No change to LAND. `inert` means the adopter does not run; the kit's bytes still land, which is
  what "landed but inert" has meant in this engine's own output since the hole-blocked skip was
  written. A target that wants no bytes removes the kit from its selection.
- No new key, no new spelling, no `--force-inert`. The key exists and is declared by targets today.
- No change to `update`'s re-render decline at `tools/govkit/govkit.py:7387`. That branch is
  correct, and `DEPL-cMendedVintage-1` depends on it staying out of the render-staleness set; this
  unit only makes it share its reader.
- No repair of `apply`'s unconditional engine-byte overwrite. That is the other half of why "just
  run apply" is not a safe remedy, it is recorded against `DEPL-dRetiredFork-2`, and it is a
  separate mechanism.
- No gate leg over descriptors. Whether a target's declared posture is honoured is a behavioural
  question about one verb, answered by a fixture, not by a predicate over declarations.

This unit takes nothing from, and leaves nothing for, any other unit in this build. It touches one
phase of one verb no other unit in the roster edits, and its only shared line —
`tools/govkit/govkit.py:7389` — is rewired rather than moved.

### Edges

none

## 4. Design

### Data model

`inert` is a list of entry ids in the target's `.governance/deploy.toml`. It is read, never written,
by both consumers. Nothing is added to the receipt: the receipt records what gov did to the tree,
and declining to run a target-owned posture flip is the absence of an action.

The one open question about the key's shape is that `intake` does not emit it — an operator adds the
line by hand — so its values are unvalidated against the registry today. A member naming an entry
that is not in the selection simply never matches, which is the same non-event as declaring it for a
kit that is not installed. Validating the list is a separate unit and §8 records why it is not this
one.

### Inventory

| identifier | kind | where |
|---|---|---|
| `inert_kits` | module-level function | `tools/govkit/govkit.py`, beside `check_target_reads_subject` |
| `inert_declined` | local set in `_cmd_apply` | beside `configure_skipped` and `stopped_ok` |

The lexicon cell for a Python module-level function in this repo grades the leading verb; `inert_kits`
is a noun-shaped accessor of a declared set and matches the spelling `lf_pins` and `tracked` already
use in this file, both of which are name-shaped readers rather than verbs.

### Why `configure_skipped` and not a new exemption

`exempt_leg` at `tools/govkit/govkit.py:3582` grants a `red_after_land` leg its exemption only while
that kit's configure phase was skipped THIS RUN, and its docstring says the scoping is deliberate. An
inert kit's configure phase is skipped this run, by the operator's own declaration, so the existing
window is exactly the right one and a second set would be a second answer to the same question. The
hole-blocked skip eleven lines above already puts its kit there for the same reason.

### Why OBSERVE needs its own set

`stopped_ok` means the adopter RAN and stopped at a declared, accepted outcome. An inert kit's
adopter did not run at all. Folding the two would make one message stand for two different facts, and
the message an operator reads would name an accepted stop that never happened. Two sets, two
sentences, one branch.

### Rollout

Effective immediately at every adopter that declares the key, and a no-op at every adopter that does
not, which is the whole current population minus those that added it by hand. There is no dark
landing because the behaviour change is a REFUSAL to act: the failure mode of shipping it wrong is
that an adopter's kit is not configured, which their own `check` reports, rather than a write nobody
asked for.

### Alternatives rejected

- **Copy the set comprehension into CONFIGURE.** Two spellings of one declaration, in a file whose
  comments name that as its recurring defect. The helper is two lines.
- **Skip the kit's whole entry rather than its CONFIGURE.** That would stop landing its bytes, which
  is a different posture and one the key has never meant.
- **Fail the run when a selected kit is inert.** An operator who declared the posture and then ran
  `apply` on a selection that includes it has done nothing wrong; the decline is the correct
  outcome and a refusal would make the key unusable with the default selection.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/govkit.py` | the reader, the CONFIGURE decline, the OBSERVE branch, `:7389` rewired |
| `tools/govkit/selftest.py` | the arms §7 names |

## 5. Production-readiness checklist

- security — this removes an execution, never adds one. The argv it declines to run is gov-authored,
  so no trust boundary moves; what moves is whether gov executes anything at all in a tree whose
  owner said not to.
- perf / scale — one set construction per run.
- error / empty / loading states — an absent `inert` key yields an empty set and every branch is
  inert itself; a non-list value would raise in the comprehension, which is the same behaviour the
  existing consumer has today and is not widened here.
- observability — S4's unconditional print, plus the OBSERVE reason. A kit declining to configure
  with no line in the output is indistinguishable from a kit that configured cleanly.
- risks — an adopter who declared `inert` for a kit and relied on `apply` to configure it anyway
  gets a kit that is no longer configured. That is the posture they declared, the decline names it,
  and removing the line is the remedy. UNVERIFIED whether any live adopter is in that state; the two
  known targets' descriptors were not read for this spec.
- testing — AC1 through AC4 on scratch fixture targets; gov keeps no receipt of its own, so none is
  observable against this repo.
- migration — none. No schema, no floor, no re-adoption.
- user docs — `WIRE-INTO-PROJECT.md` documents the key and which verbs honour it; the sentence
  naming the reader is corrected in the same commit.

## 6. Acceptance criteria

- **AC1** — When a scratch fixture target's descriptor declares a kit in `inert` and
  `python tools/govkit/govkit.py apply --target <fixture> --write` runs, stdout carries a decline
  naming that kit and the posture, and the marker that kit's adopter writes on a successful run is
  absent from the fixture.
  Red when: the decline is placed after the argv resolution, so the adopter runs and the line prints
  afterwards — the arm reads green on stdout while the posture was flipped.
  fixture: a scratch fixture target under the run's scratch root whose `deploy.toml` gains the key
  by hand, since `intake` does not emit it. This repo does not dogfood govkit and can host no
  criterion in this section.
- **AC2** — When the same fixture declares no `inert` key and the same command runs, that kit's
  adopter runs and its marker appears.
  Red when: the predicate matches on an empty declaration, in which case every adopter in the fleet
  silently stops being configured and the failing direction is the one nobody tests.
- **AC3** — When the declined kit ships a `rendered` row and
  `python tools/govkit/govkit.py apply --target <fixture> --write` runs, the absent render is
  reported with the inert reason and the run's exit code is unchanged by it.
  Red when: the inert set is folded into `stopped_ok`, which makes the message claim an accepted
  adopter stop that never happened and leaves the two facts indistinguishable in the output.
- **AC4** — When the same fixture is taken through
  `python tools/govkit/govkit.py update --target <fixture> --write`, its re-render decline still
  names that kit, showing both consumers read one reader.
  Red when: only one call site is rewired, leaving the second comprehension in place — the two then
  disagree the moment either is edited, which is the defect the helper exists to prevent.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit acceptance matrix`

New arm: `tools/govkit/selftest.py` · a fixture declaring one kit inert, asserted that its adopter
does not run and that the same fixture without the key does run it · no assertion floor to move.

## 8. Open questions

- **Q1 — should an `inert` member naming an unknown entry id be refused?**
  RESOLVED (agent, 2026-09-16, delegated): not here. A typo in the list is currently silent, which
  is a real gap, but refusing it is a validation of the target's descriptor and belongs beside the
  other descriptor refusals rather than inside a behaviour change to one phase. Recorded so the next
  reader does not have to rediscover it; it is not parked, because it is out of this unit's stated
  scope rather than undecidable within it.
- **Q2 — FACT-QUESTION · is `configure_skipped` the right set for a declined kit, or does the leg
  exemption it grants over-reach?**
  RESOLVED (agent, 2026-09-16, delegated): it is the right set. The probe is reading `exempt_leg` at
  `tools/govkit/govkit.py:3582` and its one `configure_skipped` consumer at
  `tools/govkit/govkit.py:3649`: the exemption is granted only for a leg declaring
  `red_after_land`, and only for the run in which that kit's configure was skipped. The probe can
  produce a negative — an unscoped or permanent exemption would have forced a separate set — and
  the docstring plus the consumer both show the window is per-run.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.

## 10. Reuse audit

The seam this unit extends is the re-render decline at `tools/govkit/govkit.py:7387`, read from
source: it is the only reader of `deploy["inert"]` in the engine, and this unit turns its inline set
into the shared reader both phases call. `python tools/codebase-map/reuse_lookup.py "emit gate legs
into the target gate runner manifest"` was the closest probe run for this build's govkit units and
returned no seam for a posture reader — its rows are name-token neighbours such as `target_context`
and `check_target_reads_subject`, the latter of which is the shape this unit's helper copies. The
recall probe supplied the decisive evidence: `DEPL-dRetiredFork-3`'s acceptance ledger records "a
kit named in `deploy.toml`'s `inert` list is declined without being run", and both
`DEPL-dRetiredFork-2` and `TOOL-aFlaggedScaffold-3` record that "just run apply" is not the
workaround precisely because it runs the kit's `[adopt]` and flips that posture. The defect is that
the second sentence was written about `apply` while only `update` was ever taught the rule.

Recall terms used: `--terms "govkit deploy.toml inert posture adopter argv configure apply update
regenerate descriptor kit receipt decline"`, with the question "what does the deploy.toml inert list
mean and which verbs must honour a posture the target declared".
