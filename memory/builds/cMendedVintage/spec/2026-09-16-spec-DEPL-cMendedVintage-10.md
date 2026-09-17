# DEPL-cMendedVintage-10 — `update --write` writes the `.gitattributes` block, with the renormalize

**Status:** CLOSED · rev-3 · 2026-09-17 · node c · Tier-2 · base 859daa67 · streams deployer · order 17

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-17-build-DEPL-cMendedVintage-10-acceptance-ledger.md](../build/2026-09-17-build-DEPL-cMendedVintage-10-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |
| [2026-09-16-prompt-DEPL-cMendedVintage-10-2-build-brief.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-10-2-build-brief.md) | journal | — |
| [2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md) | spec-audit | TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 |

<!-- /gen:spec-records -->

## 1. Goal

`update`'s `pins` disposition recomputes gov's LF-pin block, compares it, prints `pins-moved` and
writes an order telling the operator to run `govkit apply`. That remedy overwrites engine bytes
unconditionally and ignores `deploy["inert"]`, so the printed advice destroys exactly the local forks
`update` declined to touch. Give `update --write` the four calls `apply` makes, plus `apply`'s
renormalize, so the pin block and the index normalization that depends on it land on the safe verb.

## 2. Scope (IN)

- **S1** In `tools/govkit/govkit.py`, at the write-phase site that writes `update-pins.md` today
  (`tools/govkit/govkit.py:6674`), a `pins-moved` verdict under `--write` performs `apply`'s four
  calls in `apply`'s order: `lf_pin_block(pins)`, `write_block(cur, om, cm, block_text, "append")`,
  `write_text(..., newline="\n")` and `git add -- .gitattributes`. The recomputation itself is
  unchanged — the `pins` arm at `tools/govkit/govkit.py:6386` keeps producing `_text` and keeps
  printing its verdict line. Observed by AC1.
- **S2** The `.gitattributes` row joins the pre-write snapshot BEFORE its bytes move, carrying its
  own `origin` value so the restore branch can tell it from a `table` row. The write therefore moves
  BELOW the snapshot block at `tools/govkit/govkit.py:6690`, which is the only ordering under which
  the snapshot records the target's own block rather than gov's new one. Observed by AC4.
- **S3** After the write loop and after the verify/rollback pass, a `--write` run performs `apply`'s
  renormalize: `eol_population(target)`, the whole-diff intersect against `git diff --name-only HEAD`
  with this run's own writes subtracted, a refusal when anything else is dirty, and otherwise
  `git_pathspec(target, ["add", "--renormalize"], lf_paths)`. Observed by AC2 and AC5.
- **S4** This run's own writes, for that subtraction, are the `written_paths` set the verify pass
  already derives — `changed`, both spellings in `renamed`, `deleted` and the landed destinations —
  plus `.gitattributes` itself. `missing_wt` is computed over the population with `deleted`
  removed, because a path this run withdrew under `--write-withdrawals` is legitimately
  absent and `apply`'s spelling would refuse the renormalize for it. Observed by AC5.
- **S5** `update-pins.md` is no longer written, and a stale one this run's write supersedes is
  unlinked. The order's entire body was the remedy that this unit removes; leaving it on disk leaves
  a file instructing the operator to run the destructive verb. Observed by AC6.
- **S6** The two shipped selftest arms at `tools/govkit/selftest.py:1745` and
  `tools/govkit/selftest.py:1747` — "`update` NEVER edits .gitattributes" and "it writes an ORDER
  instead" — are rewritten to assert the new behaviour rather than deleted. Observed by AC6.

## 3. Non-goals (OUT)

- No second dirty check for `.gitattributes`. It is a receipt-claimed path, so
  `demand_writable_target` at `tools/govkit/govkit.py:6013` already refuses a run whose
  `.gitattributes` carries an uncommitted local edit. Adding another is two answers to one question.
- No change to where gov's block is APPENDED inside the target's `.gitattributes`.
  `DEPL-dSettledRoster-1` is open against exactly that: `apply` appends last and last-match-wins, so
  gov silently overrides a target that set the opposite. This unit gives that behaviour a second
  carrier and does not fix it; the fork is owner-reserved and stays where it is recorded.
- No merge of a target edit INSIDE gov's block. The block is a gov-owned region and
  `write_block` replaces it wholesale, exactly as in `apply`.
- No renormalize on a read-only run, and no renormalize on a run whose `--kits` scope excludes every
  kit declaring an `[[lf_pin]]`. The population is derived from the target's own attributes file, so
  scoping it further would need a second declaration.
- Reaping the other `update-*.md` orders is `DEPL-cMendedVintage-14`'s, and it is deliberately
  scoped to conflict orders there.

### Edges

- **consumes-from** external — nothing in this build. The pins arm, `lf_pins`, `lf_pin_block`,
  `write_block`, `eol_population` and `git_pathspec` all exist at BASE.
- **hands-off** `DEPL-cMendedVintage-11` — that unit makes `cmd_check` grade the block this unit
  writes. Until it lands, a moved block is graded by nothing; after it lands without this unit,
  every adopter whose pins moved is red with only the destructive remedy.
- **hands-off** `DEPL-cMendedVintage-13` — that unit emits gate legs on the write stage this unit
  establishes, and is sequenced after it for that reason.
- **hands-off** external — none. `WIRE-INTO-PROJECT.md` was named here for a statement it does not
  carry; the measurement is rev-3's §9 line.

- **hands-off** `DEPL-cMendedVintage-15` — that unit makes the synthesized attributes entry restorable, closing the blocker the spec audit confirmed against the snapshot this unit adds.

- **hands-off** `DEPL-cMendedVintage-17` — that unit stops a target whose pins were withdrawn reaching the empty-marker write this unit introduces.
## 4. Design

### Data model

Nothing new is persisted. The `attributes` row already carries `block_id`, `marker_style`, `mode`,
`normalized`, `block_sha256` and `patterns`, written by `apply` at `tools/govkit/govkit.py:4627`.
A `--write` run that rewrites the block refreshes `mode` and `block_sha256` on that row in place, so
the receipt describes what is on disk. The `patterns` list is refreshed from the same `pins` value
the block was rendered from.

### The ordering that makes this correct

Three sites, and the order between them is the whole unit:

| # | site | what it does |
|---|---|---|
| 1 | the snapshot block at `tools/govkit/govkit.py:6690` | records `.gitattributes`'s pre-write index entry and the six `ROLLBACK_FIELDS` on its row |
| 2 | the former order site at `tools/govkit/govkit.py:6674`, moved below 1 | writes the block and stages it |
| 3 | after the verify/rollback pass, above the coverage tail at `tools/govkit/govkit.py:7797` | the renormalize |

Site 2 must follow site 1 because a snapshot taken after the write records gov's new block as the
state to restore, which turns the rollback into a no-op that reports success. Site 3 must follow the
rollback pass because `git add --renormalize` re-stages a population wider than anything this run
wrote, and the snapshot cannot undo a re-stage of a path it never recorded. `apply` places its
renormalize last for the sibling reason its own comment gives — before the adopters have run, the
pinned population is empty.

A run that reaches site 3 with `r.problems` set skips the renormalize and prints that it did,
naming the finding count. This matches the rule the receipt re-stamp at
`tools/govkit/govkit.py:7821` already follows: a run with findings does not hand the next run a tree
that says the guards were passed.

### Inventory

| identifier | kind | where |
|---|---|---|
| `_ga_written` | local bool in `_cmd_update` | `tools/govkit/govkit.py`, beside `_renormalized` in `apply` |
| `_pins_snap` | local dict in `_cmd_update` | the snapshot entry for `.gitattributes`, `origin` `"attributes"` |
| the dirty-refusal `r.fail` text | refusal branch | one new call site, which `tools/govkit/refusal_join.py` requires an arm for |

No flag, no config key, no public surface. The lexicon cell that grades these is the Python local
scope, which declares no naming rule.

### Migration

A target whose `.gitattributes` block is already current sees no change: the `pins` arm prints
`current` and nothing is written. A target reading `pins-moved` gets one write on its next
`update --write`, and the receipt row it already carries is refreshed rather than minted. No
receipt schema change, so no floor moves and no adopter needs to re-adopt.

A target holding a stale `update-pins.md` from an earlier govkit vintage has it unlinked by the run
that supersedes it. A target that never hit `pins-moved` has none and nothing is removed.

### Rollout

This is a new write on a verb that had none, so the rollback is the pre-write snapshot rather than a
flag: a kit whose `[check]` goes green-to-red takes `.gitattributes` back with it. There is no
`GOVKIT_*` gate here, deliberately — `DEPL-cMendedVintage-7` is promoting the one dark flag this
verb has, and adding a second one for a write whose bytes gov itself computes and whose rollback is
already built would be ceremony with a cost.

### Alternatives rejected

- **Keep writing an order, with the remedy sentence rewritten.** Two artifacts answering one
  question, one of which is a file on disk that nothing refreshes. The order's whole content was the
  remedy; with the write performed there is nothing left for it to say.
- **Write the block and skip the renormalize.** Measured in the class rather than the instance: a
  newly pinned path whose index blob is CRLF keeps it, and the only verb that repairs it is `apply`,
  which is the verb this unit exists to stop recommending. The pin without the renormalize is a
  declaration nothing acts on.
- **Renormalize with the paths as argv.** `TOOL-aFlaggedScaffold-4` measured a `WinError 206` on
  inCMS, whose `.gitattributes` is 28 KB. `git_pathspec` exists because of it and is the only
  spelling used here.
- **Run the renormalize before the write loop.** The population would then exclude every path this
  run is about to land, which is precisely the set whose index blob can be wrong.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/govkit.py` | the write at the order site, the snapshot entry, the renormalize block, the stale-order unlink |
| `tools/govkit/selftest.py` | the two arms at `:1745` and `:1747` rewritten, plus the new arms §7 names |

## 5. Production-readiness checklist

- security — the bytes are gov's own, rendered by `lf_pin_block` from gov-authored descriptors; the
  target supplies patterns to no part of it. The write is contained to `target/.gitattributes`, a
  path the receipt already claims, so no traversal surface is added.
- perf / scale — one `check-attr` over the tracked set and one `git diff --name-only HEAD`, both
  already paid by `apply`. `git_pathspec` removes the argv bound.
- error / empty / loading states — a target with no pins skips every site. A target whose
  `.gitattributes` is absent takes `write_block`'s create path, as in `apply`. A `find_block` miss
  means the block was removed by hand, and the append path restores it.
- observability — the write prints one line naming the mode and the pin count; the renormalize
  prints either the path count it re-staged or the reason it refused. A skipped renormalize on a run
  with findings says so, so a silent absence never reads as a clean pass.
- risks — the sharpest is `DEPL-dSettledRoster-1`: gov's block appends last and wins over a target's
  own opposite setting, and this unit puts that behaviour on a second verb. It is recorded, owner-
  reserved and NOT fixed here. Second: a rollback must restore `.gitattributes`, which is why S2 is
  a scope item rather than a detail.
- testing — AC1 through AC6, each against a scratch fixture target; gov holds no `install.json` of
  its own, so none of them can be observed against this repo.
- migration — none beyond the stale-order unlink described in §4.
- user docs — none owed. The claim rev-2 attributed to the runbook is not in it; see §9 rev-3.

## 6. Acceptance criteria

- **AC1** — When a scratch fixture target is installed with a kit declaring an `[[lf_pin]]`, its pin
  block is tampered with INSIDE the marker pair, and
  `python tools/govkit/govkit.py update --target <fixture> --write`
  runs, the file comes back byte-identical to what `lf_pin_block` renders and stdout names the write.
  Red when: the write is placed inside the classification loop rather than the write phase, so a
  read-only run reaches it and a preview writes bytes.
  fixture: a scratch fixture target built under the run's scratch root with `intake` then `apply`;
  gov does not dogfood govkit, so this repo carries no receipt of its own and cannot host any
  criterion in this section.
- **AC2** — When that fixture's index blob for a pinned path is forced to CRLF and
  `python tools/govkit/govkit.py update --target <fixture> --write` runs, `git ls-files --eol` in
  the fixture reports `i/lf` for that path afterwards.
  Red when: the renormalize is placed before the write loop, so a path this run lands is outside the
  population it re-stages and its CRLF index blob survives the run that pinned it.
- **AC3** — When `python tools/govkit/govkit.py update --target <fixture>` runs with no `--write` on
  a fixture reading `pins-moved`, the fixture's `.gitattributes` is byte-identical afterwards.
  Red when: the write is unconditional rather than under `write`, which makes the read-only preview
  a write and removes the operator's only way to look first.
- **AC4** — When a kit's `[check]` is staged to go green-to-red across the run and
  `python tools/govkit/govkit.py update --target <fixture> --write` rolls that kit back, the
  fixture's `.gitattributes` holds the block it held BEFORE the run.
  Red when: the snapshot entry is taken after the write, in which case the restore puts gov's new
  block back, reports a successful rollback and has restored nothing.
- **AC5** — When a pinned path this run did not write is left dirty in the fixture and
  `python tools/govkit/govkit.py update --target <fixture> --write` runs, the run reports a refusal
  naming that path, and `git diff --cached` in the fixture shows the pinned population was not
  re-staged.
  Red when: this run's own writes are not subtracted from the diff, in which case every normal run
  refuses its own renormalize and the arm passes for the wrong reason — the same defect `apply`'s
  `ours` set was measured to have.
- **AC6** — When `python tools/govkit/govkit.py update --target <fixture> --write` completes on a
  fixture reading `pins-moved`, no `update-pins.md` exists in the fixture's outbox, and one placed
  there beforehand is gone.
  Red when: the unlink is conditioned on the order having been written by this run, which is never
  true once S5 lands, so every stale order survives forever.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: `tools/govkit/selftest.py` · a fixture whose pin block is tampered with inside the markers,
asserted to be rewritten by `update --write`, beside a read-only run asserted to change nothing · no
assertion floor to move.

New arm: `tools/govkit/selftest.py` · a fixture with a CRLF index blob on a pinned path, asserted
`i/lf` after the run, and a fixture with an unrelated dirty pinned path, asserted to raise the new
refusal · the `govkit refusal join` anchor set gains that refusal's anchor.

## 8. Open questions

- **Q1 — does the renormalize run when the verify pass rolled a kit back?**
  RESOLVED (agent, 2026-09-16, delegated): no. It is skipped, with the reason printed, on any run
  where `r.problems` is non-empty. That is the rule the receipt re-stamp twenty lines below already
  follows, and re-staging a population wider than the snapshot on a run that just reverted writes is
  the one action the rollback cannot undo.
- **Q2 — FACT-QUESTION · is `.gitattributes` already covered by the run's dirty precondition?**
  RESOLVED (agent, 2026-09-16, delegated): yes, and therefore no second check is added. The probe is
  reading `demand_writable_target`'s call at `tools/govkit/govkit.py:6013` and the receipt row
  `apply` synthesizes at `tools/govkit/govkit.py:4627`: the path is a claimed path, and the
  precondition's population is the claimed paths. The probe can produce a negative — a receipt with
  no `attributes` row would leave the path unclaimed and the answer would be no — and on a target
  declaring no `[[lf_pin]]` that is exactly the state, which is also the state in which this unit
  writes nothing.
- **Q3 — should the write also correct where the block sits in the file?**
  RESOLVED (agent, 2026-09-16, delegated): no. `DEPL-dSettledRoster-1` is an open owner-reserved
  fork about append-last ordering, and deciding it inside this unit would resolve an owner's fork
  through a unit that was scoped to move a write between verbs.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-3 · 2026-09-17 · §2 S4, §3, §5 · TWO CORRECTIONS, both measured at build time, neither changing a criterion. FIRST: rev-2's `hands-off external` edge and its §5 user-docs line both said `WIRE-INTO-PROJECT.md` states that `update` never edits `.gitattributes`. It does not: `grep -n gitattributes WIRE-INTO-PROJECT.md` returns four hits and every one of them is about the ADOPTING repo's own EOL rules for the hygiene checker. The three shipped carriers of the never-writes claim are `tools/govkit/govkit.py`'s two comments in the pins arm and at the order site, both rewritten by this unit, and `skills/deploy-governance/SKILL.md`'s honest-limits line, which is about `apply` and was already false at BASE. A doc correction owed to a sentence that does not exist is a correction nobody can make, so the edge is withdrawn rather than left as a red handoff. SECOND: S4 enumerated this run's own writes as `changed` + `renamed` + `deleted` + `.gitattributes`, omitting the LANDED destinations. Those are `git add`ed by the landing loop, so every run that lands an unclaimed source into an lf-pinned path would have found its own landing in `git diff --name-only HEAD` and refused its own renormalize — the exact defect AC5's own `Red when` names one set over. S4 now names `written_paths`, the set the verify pass already derives for precisely this question. THIRD, editorial only: AC1's invocation span was wrapped across two lines, which put every backtick after it on the wrong parity and made hygiene check 23 read AC1 as carrying no token at all. Reflowed onto its own line; no word of the criterion changed.
- rev-2 · 2026-09-17 · §3 · RECIPROCAL EDGE, no scope or criterion changed. The spec-audit disposal authored DEPL-cMendedVintage-15, DEPL-cMendedVintage-17 naming this unit, and the edge was never written back — hygiene check 12 reds on a handoff one author declared and the other never saw. The edge is a fact about this build that became true when the promotion was created, so recording it completes the record rather than changing the design.

## 10. Reuse audit

The seam this unit extends is `_cmd_apply`'s attributes step at `tools/govkit/govkit.py:4620` and
its renormalize at `tools/govkit/govkit.py:4976`, read from source; every call this unit makes
already exists there and is called from exactly one place, which is what makes moving the call site
cheap. The map dossier says the same thing in the negative and it is worth quoting rather than
re-deriving: `memory/map/features/govkit.md` records that writing a gov-owned region into a
target-owned file has no seam anywhere in this repo, and that nothing here writes a `.gitattributes`
block or performs the renormalize that follows it. So the only seam is govkit's own, and
`python tools/codebase-map/reuse_lookup.py "write the govkit-owned gitattributes pin block and
renormalize the pinned population"` returned name-token neighbours — `write_text` in
`gen_build_index.py`, `eol_population` at fan-in 0 — none of which is reachable from this verb. The
recall probe contributed the two facts that changed the design: `DEPL-dSettledRoster-1` is open
against the append-last ordering this write inherits, and `TOOL-aFlaggedScaffold-4` is why the
renormalize must go through `git_pathspec` rather than an argv pathspec.

Recall terms used: `--terms "govkit update apply gitattributes lf_pin attributes receipt
renormalize outbox order pins-moved rollback snapshot"`, with the question "why does govkit update
report the gitattributes pin block as an order instead of writing it, and what owns the
renormalize".
