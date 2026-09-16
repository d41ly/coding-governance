# DEPL-cMendedVintage-4 — the unattributed remedy names a command that works, and the override retires

**Status:** SPECCED · rev-1 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |

<!-- /gen:spec-records -->

## 1. Goal

`update --write` withholds the receipt's `gov_commit` re-stamp while any row carries
`evidence: "unattributed"`, and the remedy it prints — `govkit adopt --re-adopt --write` — re-runs
the same attribution walk over the same bytes and produces the same rows. Print the form that
actually clears them, and retire the `--allow-ungraded` override that exists only to advance the base
away from rows nothing graded.

## 2. Scope (IN)

- **S1** The remedy at `tools/govkit/govkit.py:7853` names `govkit adopt --re-adopt --pin <path>=<rev> --write`,
  the same form the sibling remedy at `:6487` already names. Observed by AC1.
- **S2** The `USAGE` sentence at `tools/govkit/govkit.py:8539` is corrected to the same form, so the
  two operator-facing carriers agree. Observed by AC1 and AC4.
- **S3** `--allow-ungraded` is removed entirely: the `USAGE` line at `tools/govkit/govkit.py:8522`,
  its sentence at `:8535`, the argv arm at `:8601`, the `parse_args` return element and its unpack at
  `:8958`, the two function parameters at `:5930` and `:5940`, the `and not allow_ungraded` at
  `:7847`, and the `over` clause at `:7866`. Observed by AC2 and AC3.
- **S4** The prose-grep arm at `tools/govkit/selftest.py:8126` is replaced by two arms: one that runs
  the remedy the verb printed and observes the rows clear, and one that asserts the CLASS — every
  operator-facing string naming both `unattributed` and `--re-adopt` also names `--pin`. Observed by
  AC1 and AC4.
- **S5** The two `--allow-ungraded` arms at `tools/govkit/selftest.py:691-697` are deleted with the
  flag, and the arm at `:689` is kept and re-pointed at the corrected remedy string. Observed by AC2.

## 3. Non-goals (OUT)

- No change to what makes a row `unattributed`. `derive_attribution` and the adoption walk are
  untouched; this unit changes only the sentence that tells an operator what to do about the result.
- No new way to clear a row. `--re-adopt --pin` already works and already sets `evidence = "pinned"`
  at `tools/govkit/govkit.py:8179`; nothing here builds an alternative.
- No automatic pin, no heuristic guess at a revision. A pin is an operator's assertion about which
  vintage bytes came from, and a tool that guesses it writes provenance nobody verified.
- No replacement override. `--allow-ungraded` is retired, not renamed.

### Edges

- **consumes-from** external — `adopt --pin` and the `evidence = "pinned"` write at
  `tools/govkit/govkit.py:8179`, landed by `DEPL-dCarriedReceipt-13` and present at this build's
  BASE. The remedy this unit prints is only correct because that path exists.
- **hands-off** `TOOL-cMendedVintage-7` — that unit reports `unattributed` rows on an adopter's own
  bar and is blocked on this one, because reding an adopter for a state whose printed remedy is a
  no-op hands them a failure with no exit. After this unit the printed exit works.

## 4. Design

### Why `--re-adopt --write` cannot clear the rows

`evidence: "unattributed"` is written only by `cmd_adopt`, for a row whose bytes matched no gov
vintage. `--re-adopt --write` re-runs that identical walk over identical bytes against identical
history and reaches the identical answer. Nothing in the loop is stateful, so the second run is the
first run. `--pin <path>=<rev>` is the only input that changes the outcome: it is the operator
asserting the vintage the walk could not find, and it is what sets `evidence = "pinned"`.

`--re-adopt` is still required, because a target holding an `unattributed` row has `install.json` on
disk by construction and `adopt` refuses over an existing receipt before `--pin` is ever consulted.
So the working form is all three flags, and that is exactly what the sibling remedy at
`tools/govkit/govkit.py:6487` already prints — this unit makes the two agree.

### Why the prose-grep passes today

`tools/govkit/selftest.py:8126` asserts that `--re-adopt --pin` appears SOMEWHERE in the source and
that one specific broken spelling does not. Both hold at BASE: the sibling remedy supplies the first
and the refusing form was fixed at the second. Meanwhile two other operator-facing copies name the
no-op form and the arm cannot see them, because it grades the file's vocabulary rather than any
particular sentence. That is the instance-versus-class defect the charter names, and the replacement
is written one level up.

The class predicate: read `tools/govkit/govkit.py`, take every string literal that contains both
`unattributed` and `--re-adopt`, and assert each also contains `--pin`. Scoping on `unattributed` is
what keeps the two legitimate bare-`--re-adopt` remedies — the ones at `:8021` and `:8312`, which
answer "a receipt already exists" and for which `--re-adopt` alone IS the fix — out of the
population. A predicate over `--re-adopt` alone would red those and be widened until it graded
nothing.

### Retiring the override

`--allow-ungraded` has exactly one reader, the `and not allow_ungraded` at `tools/govkit/govkit.py:7847`.
Setting it does not write a byte that would otherwise be withheld — the byte-level work above is kept
either way, and the comment at `:7840` says so. All it does is advance `gov_commit` past rows nothing
graded, which moves the base those rows must be attributed FROM further away every time it is used.
It is an override whose only effect is to make the condition it overrides harder to clear.

The consequence of retiring it is stated rather than implied: an adopter carrying `unattributed` rows
now has exactly one exit from the withheld stamp, which is to clear the rows. That is acceptable only
because S1 and S2 make the printed exit a working one, which is why the two halves are one unit and
not two.

### Inventory

This unit MINTS nothing. It deletes one flag name, one `parse_args` return element, two function
parameters and one module-level constant, and rewrites two strings. The new selftest arms are the
only additions and they are test-local.

### Files touched (estimate)

`tools/govkit/govkit.py` — about 25 lines, all deletions and two string rewrites, spread over the ten
sites S3 enumerates. `tools/govkit/selftest.py` — two arms deleted, one re-pointed, two added.
`WIRE-INTO-PROJECT.md` — the maintenance paragraph if it names the flag; derived at build time with
`grep -rn 'allow-ungraded' --include='*.md' .` rather than pinned here.

### Alternatives rejected

- **Keep the flag and fix only the remedy.** The flag's use is what makes the rows permanently
  unattributable, so leaving it is leaving the trap whose sign this unit is correcting.
- **Make `--re-adopt --write` clear the rows by widening the match.** That would attribute bytes to a
  vintage they did not come from, which is the one thing `evidence` exists to prevent.
- **Assert the two known sentences by content.** That is the instance fix: it certifies the two
  copies that exist today and says nothing about the third somebody adds next month.

### Migration

A target whose receipt was stamped under `--allow-ungraded` keeps that stamp; nothing rewrites it.
Its rows stay `unattributed` and now print a remedy that works. No receipt field or descriptor key
changes shape.

### Rollout

Lands directly. The flag has no adopter-side configuration to unwind — it is passed on a command
line or it is not — so retiring it can only turn an invocation that used it into an argv refusal,
which is a visible failure and not a silent one.

## 5. Production-readiness checklist

- **security** — retiring the override narrows what a run may do to the receipt; nothing widens.
- **perf / scale** — no runtime change. The new class arm reads one file once.
- **error / empty / loading states** — a target with zero `unattributed` rows never reaches either
  string; an invocation still passing the retired flag gets the existing unknown-argument refusal.
- **observability** — the withheld-stamp line still prints its count and now ends with a command the
  operator can run. The `over … --allow-ungraded` clause disappears with the flag it reported.
- **risks** — the real one is that retiring the override wedges an adopter who cannot determine a
  revision to pin. That is a documented operator task and not a tool failure, and it is why S1 ships
  in the same commit; it is recorded here so a later build does not re-add the flag without reading
  this paragraph.
- **testing** — one behavioural arm that runs the printed remedy end to end, one class arm over every
  operator-facing string, and the existing withheld-stamp arm kept green.
- **migration** — nothing stored changes shape; a stamp already advanced under the flag is left alone.
- **user docs** — `WIRE-INTO-PROJECT.md` loses the flag wherever it names it and gains the working
  remedy; the `USAGE` block in `tools/govkit/govkit.py` is the other user-facing carrier and S2 and
  S3 both land in it.

## 6. Acceptance criteria

- **AC1** — When a fixture target carries one `evidence: "unattributed"` row,
  `python tools/govkit/govkit.py update --target <fixture> --write` prints a remedy naming
  `--re-adopt`, `--pin` and `--write`, and running exactly that printed command leaves the row's
  `evidence` as `pinned`.
  Red when: the remedy is corrected in one carrier and the arm reads the other, or the printed
  command is run and the row is still `unattributed`, which is what the shipped sentence produces.
  fixture: the ungraded-row fixture at `tools/govkit/selftest.py:689` already stages the state; this
  arm extends it to execute the remedy.
- **AC2** — When `python tools/govkit/govkit.py update --target <fixture> --write --allow-ungraded`
  runs, it is refused as an unknown argument.
  Red when: the flag is removed from `USAGE` and left in `parse_args`, so it keeps working while the
  documentation says it does not exist.
- **AC3** — When `grep -c 'allow_ungraded' tools/govkit/govkit.py` runs, it returns 0.
  Red when: one of the ten sites S3 enumerates is missed — most likely the `parse_args` return
  element, whose removal is the one that changes an unpack in a different function.
  figure: DERIVED by that grep at observation time; the ten sites are enumerated in S3 and are
  re-derived rather than trusted.
- **AC4** — When the class arm runs over `tools/govkit/govkit.py`, every string literal containing
  both `unattributed` and `--re-adopt` also contains `--pin`, and staging a break — adding one such
  string without `--pin` — turns the arm RED.
  Red when: the predicate is scoped to `--re-adopt` alone, which reds the two legitimate bare-form
  remedies and gets widened back into a grep that grades nothing.
- **AC5** — When the withheld-stamp arm at `tools/govkit/selftest.py:689` runs, it still asserts that
  the receipt is NOT re-stamped and now asserts the corrected remedy string.
  Red when: the two `--allow-ungraded` arms beside it are deleted and this one is deleted with them,
  which would remove the only coverage of the withholding itself.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/govkit/selftest.py · the class predicate over `tools/govkit/govkit.py`'s string
literals, staged by adding one remedy string naming `unattributed` and `--re-adopt` without `--pin` ·
none

New arm: tools/govkit/selftest.py · the behavioural arm that runs the remedy the verb printed and
re-reads the row's `evidence` · none

`govkit refusal join` is named because S3 deletes a branch: `and not allow_ungraded` guards a return
that is not a refusal channel, but the removal touches `parse_args`, and if the deployer's branch pin
or anchor set moves, that is this commit's to record with both values beside it.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.

## 10. Reuse audit

The seam this unit extends is `tools/govkit/govkit.py:6487`, the sibling remedy that already prints
`govkit adopt --re-adopt --pin <path>=<rev> --write` — found by recall rather than by
`python tools/codebase-map/reuse_lookup.py`, whose ranked hits for this behaviour are rendering and
kit-path helpers and contain no remedy-string seam, which is a miss to record rather than a phrasing
to retry. Recall returned the record that owns the correction: the `DEPL-dCarriedReceipt-13` round-1
diff review, which traced the refusing form to `cmd_adopt` refusing over an existing receipt before
`--pin` is consulted, and `DEPL-dGaugedVintage-8`, whose own inventory table asserts the remedy site
"names `adopt --re-adopt --pin … --write`" and marks it unchanged. Verified against source rather
than against that record, and the two disagree: the site that table describes is `:6487`, while
`:7853` and the `USAGE` sentence at `:8539` both name the no-op form, so the record's claim is true
of one carrier and false of the corpus.

Recall terms used: `coverage gap decline refusal reason unclaimed source landing unattributed
evidence remedy re-adopt pin allow-ungraded stamp`
