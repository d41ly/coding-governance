# DEPL-cMendedVintage-13 — `update --write` emits gate legs

**Status:** CLOSED · rev-3 · 2026-09-17 · node c · Tier-2 · base 859daa67 · streams deployer · order 23

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-17-build-DEPL-cMendedVintage-13-acceptance-ledger.md](../build/2026-09-17-build-DEPL-cMendedVintage-13-acceptance-ledger.md) | journal | — |
| [2026-09-17-build-DEPL-cMendedVintage-21-acceptance-ledger.md](../build/2026-09-17-build-DEPL-cMendedVintage-21-acceptance-ledger.md) | journal | DEPL-cMendedVintage-21 |
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |
| [2026-09-17-prompt-DEPL-cMendedVintage-13-2-build-brief.md](../prompts/2026-09-17-prompt-DEPL-cMendedVintage-13-2-build-brief.md) | journal | — |
| [2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md) | spec-audit | TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-14 |
| [2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md](../reviews/2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md) | diff-review | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 TOOL-cMendedVintage-10 |

<!-- /gen:spec-records -->

## 1. Goal

Gate legs are emitted by `apply` and by `adopt` and by nothing else, so every `[[gate_leg]]` gov
starts shipping reaches an adopter only when they re-run the verb that overwrites engine bytes
unconditionally. That is the residual cap on "an adopter pulls a new vintage with one safe verb".
Give the emission to `update --write`, from one shared implementation rather than a third copy of
the ownership rules.

## 2. Scope (IN)

- **S1** `_cmd_apply`'s manifest-emission core is extracted into one module-level function in
  `tools/govkit/govkit.py`: read the declared runner file, resolve each selected kit's legs, apply
  the silenced-leg bar, resolve guards, decide ownership, and either write the manifest back or
  withhold it. `apply` calls it in place of its inline block and keeps its own `step` prints, its
  before/after verdict maps and its kit-subject advice. Observed by AC1 and AC6.
- **S2** `_cmd_update` calls that function under `--write`, after the write loop AND after the
  verify/rollback pass, so a kit whose writes were reverted does not have its legs emitted by the
  same run. Observed by AC5.
- **S3** The emission population is the receipt's claimed kits narrowed by the run's `--kits` scope,
  minus the kits this run rolled back. A leg is a DECLARATION, not a file, so a claimed kit whose
  bytes did not move this run is still in the population — that is the case this unit exists for.
  Observed by AC1.
- **S4** Ownership is MERGED, never replaced: the receipt's `gate_runner.emitted` becomes this run's
  rows for in-scope kits UNION the previous receipt's rows for every kit outside the scope. A scoped
  run that replaced the whole list would revoke gov's claim on an out-of-scope leg, after which every
  later run refuses the leg gov itself wrote. Observed by AC2.
  The union rule lives in the shared function and the CALLER selects it, because the two verbs keep
  different receipts. `update` narrows which rows it classifies and leaves the receipt's `kits` list
  whole, so an out-of-scope kit is still claimed and its ownership must survive. `apply` rewrites
  `kits` and `files` to its own selection, so carrying rows for kits its receipt no longer claims
  would make `emitted` name kits `kits` does not — a new inconsistency, and a behaviour change in
  the verb S1 exists to leave alone. `apply` therefore passes no carry set and is unchanged.
- **S5** A target runner file that is absent, unparseable or not a JSON list is an `r.fail` in the
  update path, never a `Refusal`. `apply` raises, and raising is correct there because nothing has
  been written yet; in `update` the bytes are already on disk, so an abort would leave the target
  updated with an un-restamped receipt and no emission — the wedge shape twice recorded against this
  step. Observed by AC4.
  S5 IS A CLASS, not that one branch, and the difference was measured during the build. The shared
  function raises on a second condition the spec never named: a leg whose NAME the target's runner
  carries and this receipt does not claim, which any hand-edit made after the install can produce.
  In `apply` that raise is correct for S5's own reason; in `update` it is the identical wedge. So the
  update call site catches every `Refusal` the emission can raise and reports it verbatim with the
  bytes kept and the receipt un-restamped, and the named `r.fail` above survives for the one case
  whose message is worth writing. Gating one branch and leaving its sibling is the shape §7 names.
- **S6** The manifest write-back is `write_text` to a sibling temp path followed by `os.replace`, in
  the shared function, so both verbs stop being able to leave a truncated runner file. Observed by
  AC6.
- **S7** For a target whose `[gate_runner].kind` is not `manifest`, the shared function refreshes the
  same `gate-legs.md` order path `apply` writes, with the same WITHHELD section. `update` does not
  touch the receipt's `orders` list, which `apply` owns; the path is unchanged, so a recorded order
  stays true. Observed by AC7.

## 3. Non-goals (OUT)

- No fix for `TOOL-dRetiredFork-27`, the duplicate row a manifest whose `dedupe_key` is `name` keeps
  when the receipt already claims a name the target also carries. This unit gives that behaviour a
  second caller and does not widen it; the row is open and stays open.
- No emission from a read-only `update`, and NO PREVIEW OF ONE EITHER. rev-1 and rev-2 said the
  preview "prints what it would emit"; measured at rev-3, the read-only run RETURNS hundreds of
  lines above where this step sits, and its own closing line already says nothing was written.
  Printing a preview would mean resolving every leg on a path that writes nothing, for no criterion,
  so the clause is withdrawn rather than half-built. The same measurement is why the call site
  carries no `if write:` guard: that condition cannot be false there.
- No new leg, no change to any shipped `[[gate_leg]]`, no change to `subject` defaulting or to
  `check_target_reads_subject`'s floor.
- No receipt `orders` bookkeeping in `update`. `update` maintains no such list at BASE and minting
  one here would put a second writer on a field `apply` owns.
- No change to the silenced-leg bar's predicate. It is called with `update`'s own index read, which
  is the caller's parameter by design.

### Edges

- **consumes-from** `DEPL-cMendedVintage-10` — the write stage. That unit establishes that
  `update --write` performs install effects and where in the run they sit relative to the snapshot
  and the rollback; without it this unit would be introducing both the stage and its first tenant.
- **hands-off** external — an adopter's bar gains gov's new legs on a safe verb; nothing else in
  this build consumes the emission.

- **hands-off** `DEPL-cMendedVintage-21` — that unit makes the atomic write one helper with something that fails when it is absent, closing the criterion this unit names but cannot observe.
## 4. Design

### Where the call sits, and why there

`apply` places its emission after its stage step because the silenced-leg bar reads the target's
index and this run's own writes must count as present; its own comment records that the identical
predicate at preflight would red every first install. `update` inherits the constraint and adds one:
the verify pass can revert a kit's writes, and a leg emitted for a reverted kit records coverage for
files that are no longer there. So the call site is after both, immediately before the coverage tail
that `TOOL-aWeldedTribunal-6` introduced — and after the renormalize as well, which rev-2 did not
say and which the build measured: `git add --renormalize` refuses when the pinned population is
dirty relative to HEAD, so a manifest written above it is gov refusing its own write. Its `have`
argument is a fresh index read taken at that point. Located by SYMBOL, never by line: rev-1 and rev-2
both carried a line number here and five units moved the file underneath it.

### Data model

| field | source | note |
|---|---|---|
| `existing` | the target's `[gate_runner].file`, parsed | unchanged rows are preserved by name |
| `owned` | `receipt["gate_runner"]["emitted"]` | gov's claim on a NAME, not on a row |
| `subject` | `leg.subject` or `repo` | written only when `check_target_reads_subject` is true |
| `guard` | resolved, dropped when it matches no tracked path | omitted, never `[]`, when all drop |

The merge in S4 is keyed on the kit, not on the leg name: a row whose `kit` is outside this run's
scope is carried through untouched, and a row whose `kit` is in scope is replaced by what this run
built for it. Keying on the name instead would silently drop a leg whose kit was renamed between
vintages, which is a rename this engine handles elsewhere and must not undo here.

### Inventory

| identifier | kind | where |
|---|---|---|
| `write_gate_legs` | module-level function | `tools/govkit/govkit.py`, beside `silenced_legs` |
| `_legs_scope` | local list in `_cmd_update` | the claimed-minus-rolled-back population |
| `_rolled_kits` | local set in `_cmd_update` | the kits the verify pass reverted this run |

The name is `write_gate_legs` and NOT `emit_gate_legs`. `emit` is the verb the receipt field and both
call sites spell in prose, and it is in no row of `.lexicon.conf`'s table, so a definition leading
with it raises `VERB_OFFENDER_PIN` — a two-sided equality, which is a red rather than a drift.
`python tools/lexicon/lexicon.py --suggest write_gate_legs --as py.function` answers OK; the same
question asked about `emit_gate_legs` routes to `print`, which is wrong for a function whose job is a
file. `write` is the table's own row for persisting to a store, which is what this does.

`update` also validates the target's `[gate_runner]` through `validate_gate_runner` before calling,
against a throwaway `Report`, and reports rather than emits when that validation has anything to
say. `apply` validates in its pre-write pass; `update` never did, and `[gate_runner].file` is a
target-supplied path this function joins onto the target root and WRITES — the escape site that
function's own header records. The throwaway report is `update`'s established shape for a probe that
must not fail a verb after its bytes have landed.

### Migration

None for the receipt: `gate_runner.emitted` exists and its shape is unchanged. A target whose runner
already holds every declared leg sees an idempotent rewrite — the same rows, written back — which is
what `apply` does today on a re-run.

The extraction moves refusal branches between functions without changing their count, so
`tools/govkit/refusal_join.py`'s anchor computation follows them automatically; S5's new `r.fail`
sites raise the live count and the `BRANCH_PIN` floor is moved with them, per that file's own
convention that a floor which trails the population stops catching a blind matcher.

### Rollout

The risk this unit owes an explicit answer to is a half-written leg manifest, because it puts a
second verb on a file an adopter's whole bar reads. The answer is S6: the write becomes temp-file
plus `os.replace`, so a crash mid-write leaves the previous file rather than a truncated one, and
the failure mode disappears rather than gaining a recovery procedure. The residue is a runner file
that is malformed for some OTHER reason — hand-edited, or truncated by a prior vintage of this code
— and S5 is that case: reported by name, no emission, the run's byte writes kept, the receipt not
re-stamped, and the two remedies named in the message, which are restoring the file from the
target's own history and re-running.

### Alternatives rejected

- **A second emitter inside `_cmd_update`.** The ownership rules are the whole difficulty here, and
  they have been got wrong twice in this engine's recorded history — once by blanking `emitted` on
  the withheld path, once on the non-manifest branch. A second copy is a third occasion.
- **Emit only for kits whose bytes moved.** A new leg over an unchanged file would never reach the
  adopter, which is exactly the gap this unit closes, one degree smaller.
- **Emit before the verify pass, next to the writes.** A rolled-back kit would keep the leg, so the
  target's bar would run a leg whose engine was reverted in the same run.
- **Raise a `Refusal` on a malformed runner, as `apply` does.** It aborts after bytes have been
  written. The two verbs differ precisely in what has already happened when the step is reached.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/govkit.py` | the extraction, `apply` rewired to it, the `update` call site, the temp-file write |
| `tools/govkit/refusal_join.py` | the `BRANCH_PIN` floor raised to the live count |
| `tools/govkit/selftest.py` | the arms §7 names |

## 5. Production-readiness checklist

- security — the legs are gov-authored argv, resolved against gov-authored descriptors; the target
  supplies only token VALUES, which is unchanged from `apply`. Nothing new executes: emission writes
  a manifest, it does not run a leg.
- perf / scale — one runner read, one index read, one write per run. The index read is the same
  `tracked()` call `apply` makes.
- error / empty / loading states — no `[gate_runner]` at all takes S7's branch; an empty leg set
  writes nothing and says so; an absent runner file is created by the write-back as `apply` does.
- observability — the emitted count, the withheld count and the silenced legs each print by name.
  A run that emitted nothing prints the reason rather than staying silent, because silence here is
  indistinguishable from a kit declaring no legs.
- risks — the half-written manifest, answered by S6 above. Second: a scoped run revoking ownership,
  answered by S4 and observed directly by AC2 because it is the failure this engine has actually
  had. Third: the extraction is the largest refactor in this build and lands under a unit whose own
  subject is elsewhere, which is why S1 is a scope item with its own criterion.
- testing — AC1 through AC7 on scratch fixture targets. Gov does not dogfood govkit, so no criterion
  in §6 is observable against this repo.
- migration — none; §4 states why.
- user docs — `WIRE-INTO-PROJECT.md` says gate legs arrive with `apply`; that sentence gains
  `update`.

## 6. Acceptance criteria

- **AC1** — When a scratch fixture target is installed with a kit declaring a `[[gate_leg]]`, that
  leg's row is deleted from the target's runner file by hand, and
  `python tools/govkit/govkit.py update --target <fixture> --write` runs with no other change, the
  row is present in the runner file afterwards.
  Red when: the population is keyed on the rows this run WROTE rather than on the selected kits'
  descriptors, in which case a run that moves no bytes emits nothing and the leg stays missing —
  which is the whole defect, one level in.
  fixture: a scratch fixture target under the run's scratch root, built with `intake` then `apply`.
  Gov keeps no receipt of its own, so no criterion here is observable against this repo.
- **AC2** — When that fixture holds legs from two kits and
  `python tools/govkit/govkit.py update --target <fixture> --write --kits <one-kit>` runs, the other
  kit's leg is still in the runner file and still claimed by the receipt's `gate_runner.emitted`.
  Red when: the emitted list is replaced by this run's rows, which revokes gov's claim on the
  out-of-scope leg; every later run then refuses a leg gov itself wrote and the target is wedged.
- **AC3** — When a kit declares a leg whose argv names a path the fixture does not hold and
  `python tools/govkit/govkit.py update --target <fixture> --write` runs, that leg is absent from the
  runner file, the run names it, and the other kits' legs ARE written.
  Red when: the silenced finding is raised before the write-back, in which case one defective leg
  suppresses the healthy ones — the measured shape this step already had once.
- **AC4** — When the fixture's runner file is replaced with bytes that are not a JSON list and
  `python tools/govkit/govkit.py update --target <fixture> --write` runs, the run reports the file by
  name, exits with findings, keeps the bytes it wrote earlier in the run, and leaves the receipt
  un-restamped.
  Red when: the malformed file raises instead of reporting, which aborts the verb after its writes
  and leaves a tree gov updated and a receipt that says it did not.
- **AC5** — When a kit's `[check]` is staged to go green-to-red so the verify pass rolls it back and
  `python tools/govkit/govkit.py update --target <fixture> --write` runs, that kit's legs are not
  written into the runner file.
  Red when: the call sits before the verify pass, so the run records coverage for a kit whose engine
  it reverted three lines later.
- **AC6** — When `python tools/govkit/govkit.py apply --target <fixture> --write` runs against a
  fixture after the extraction, the runner file it produces is byte-identical to the one the same
  command produced before it.
  Red when: the extraction changes the row order or drops a field, which is invisible to every
  behavioural arm and reds an adopter's byte-comparing parity leg instead.
  figure: DERIVED — the comparison is between two runs of the same command, not against a literal
  recorded in this spec.
- **AC7** — When a fixture whose `[gate_runner]` declares no manifest is taken through
  `python tools/govkit/govkit.py update --target <fixture> --write`, the `gate-legs.md` order in its
  outbox is refreshed with the current argv and the run names it.
  Red when: the non-manifest branch is skipped in the update path, which leaves those targets with
  an order describing whichever vintage last ran `apply`.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `run-gates canary`

New arm: `tools/govkit/selftest.py` · a fixture whose runner row is deleted by hand, asserted
restored by `update --write`, beside a scoped run asserted not to revoke the other kit's ownership ·
the `BRANCH_PIN` floor in `tools/govkit/refusal_join.py` is raised to the live count in the same
commit.

New arm: `tools/govkit/selftest.py` · a fixture whose runner file is replaced with non-JSON bytes,
asserted to report rather than abort, and a rolled-back kit asserted to have no leg written · no
further floor to move.

## 8. Open questions

- **Q1 — does `update` refresh the `gate-legs.md` order for a non-manifest target, or only report?**
  RESOLVED (agent, 2026-09-16, delegated): refresh it. The path is `apply`'s and is unchanged, so a
  receipt row recording it stays true and `check`'s outbox arm is unaffected; the alternative leaves
  the one class of target that cannot receive legs automatically reading an order from whichever
  vintage last ran `apply`. It is the shared function's own branch, so it costs nothing to keep.
- **Q2 — FACT-QUESTION · does extracting the emission change what
  `tools/govkit/refusal_join.py` requires?**
  RESOLVED (agent, 2026-09-16, delegated): it changes the anchors and not the obligation. The probe
  is reading `enumerate_branches` and the two pins in that file: anchors are computed per enclosing
  function on every run and are stored nowhere, `FILE_PIN` counts modules and this extraction adds
  none, and `BRANCH_PIN` is shrink-only so a moved branch is neutral to it. The probe can produce a
  negative — a stored anchor list would have made this a migration — and there is none.
- **Q3 — should the emission be scoped to kits whose declared legs actually changed?**
  RESOLVED (agent, 2026-09-16, delegated): no. Deciding "changed" needs the legs gov declared at the
  receipt's own `gov_commit`, which is a second descriptor read at a second vintage for a write that
  is already idempotent. The rewrite of an unchanged row costs one line of JSON.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-2 · 2026-09-17 · §3 · RECIPROCAL EDGE, no scope or criterion changed. The spec-audit disposal authored DEPL-cMendedVintage-21 naming this unit and never wrote the edge back; hygiene check 12 reds on a handoff one author declared and the other never saw. Recording it completes the record rather than changing the design.
- rev-3 · 2026-09-17 · §2 §3 §4 · FIVE AMENDMENTS, measured during the build, no criterion changed.
  S5 is widened from one branch to its CLASS: the shared function raises on a second condition this
  spec never named, and gating one branch while its sibling stays is the failure §7 names by name.
  §3's read-only clause is WITHDRAWN rather than half-built, because the preview it describes returns
  before this step and printing one would buy no criterion.
  The extracted function is `write_gate_legs`: `emit` is in no row of the declared verb table and a
  definition leading with it reds two unguarded merge-bar legs, which rev-2's inventory asserted the
  opposite of. S4's union is caller-selected rather than unconditional, because `apply` rewrites its
  receipt's `kits` list to its own selection and carrying out-of-scope rows there would be a
  behaviour change in the verb this unit must not touch. And `update` validates the target's
  `[gate_runner]` before emitting, which rev-2 never said and which `[gate_runner].file`'s own escape
  history requires of any verb that joins it onto the target root and writes. §4's call-site
  sentence loses its line number and gains the renormalize, both measured on this tree.

## 10. Reuse audit

The seam this unit extends is `_cmd_apply`'s gate-runner step at `tools/govkit/govkit.py:5096`,
read from source, together with `silenced_legs` at `tools/govkit/govkit.py:2395` and
`check_target_reads_subject` at `tools/govkit/govkit.py:3526`, both of which are already shared by
more than one caller and are called rather than copied here.
`python tools/codebase-map/reuse_lookup.py "emit gate legs into the target gate runner manifest"`
returned no seam — its ranked rows are name-token neighbours such as `read_gate_verdicts`,
`target_context` and `resolve_gate_path` in the codebase-map kit, none of which emits anything — so
the citation above comes from the file. The recall probe is what shaped S4 and S5 rather than
confirming them: `TOOL-aScouredKit-27` records that this fix "is NOT a one-liner and half-building
it is worse than the gap", and the aScouredKit closing rounds record both ownership-blanking
defects, one on the withheld path and one on the non-manifest branch, which are the two failure
modes S4 is written against.

Recall terms used: `--terms "govkit gate_leg gate_runner emitted manifest silenced_legs receipt
apply update subject guard ownership adopter"`, with the question "why does govkit update never emit
gate legs and who owns the emitted ownership set in the receipt".
