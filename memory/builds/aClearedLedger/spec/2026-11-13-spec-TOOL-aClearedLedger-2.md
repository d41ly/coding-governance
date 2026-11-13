# TOOL-aClearedLedger-2 — the protocol's section 12 says why a red fix's record is the next commit and cannot ride its own fix

**Status:** CLOSED · rev-1 · 2026-11-13 · node a · Tier-2 · base 8db6f4be · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-13-build-TOOL-aClearedLedger-2-1-acceptance-ledger.md](../build/2026-11-13-build-TOOL-aClearedLedger-2-1-acceptance-ledger.md) | journal | — |
| [2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md](../prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md) | research | TOOL-aClearedLedger-1 TOOL-aClearedLedger-3 TOOL-aClearedLedger-4 TOOL-aClearedLedger-5 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-9 TOOL-aClearedLedger-10 |

<!-- /gen:spec-records -->

## 1. Goal

The unattended protocol's section 12 says a red fix's typed record is the next commit, where the
prompt that built the lane allowed the same commit or the next. The owner ruled on 2026-11-13 that
the record stays the next commit, so this unit adds the reason to that sentence: the record names
its fix commit's sha, and a commit cannot hold its own sha.

## 2. Scope (IN)

- **S1** — In section 12 of `tools/unattended/PROTOCOL.template.md`, the paragraph that opens
  `**Two switches act BETWEEN passes` gains the clause of §4, "The sentence". No other sentence of
  the protocol moves. Observed by AC1 and AC2.
- **S2** — The protocol's render, `memory/guides/UNATTENDED-PROTOCOL.md`, takes the same edit and
  stays byte-identical to the template. Observed by AC1.
- **S3** — The protocol's row in `tools/template-size-limits.txt` is raised to the render's
  measured bytes, argued above the row in the `RAISED <old> -> <new>` shape. Observed by AC3.
- **S4** — One row in `memory/DECISIONS.md` records that raise. The main loop writes it in a
  `Pass: none` records commit ahead of this unit's pass commit, and the builder writes nothing to
  that file. Observed by AC3.

## 3. Non-goals (OUT)

- A record that rides its own fix commit. The owner ruled against it, and the door could not write
  one: it reads the sha from a commit that must already exist.
- Any change to `tools/memory-tree/build_records.py`, its door or its join. The sentence states
  what they already do.
- `help/red-fix-lane.md`. It already says the record is the next commit, and its field table says
  the `Commit` field is the fix commit's sha.
- The other sentences of the paragraph, and the rest of section 12.
- `tools/unattended/SKILL.template.md` and the three other copied guides of the unattended kit.
  The clause names no verb, key or path, so none of them owes a row.
- The charter's `[spec]` line, which is the ask's first sentence.
- The kit version marker on the protocol's first line, which the lander's `mint` moves once.

### Edges

- **consumes-from** `TOOL-aClearedLedger-1` — the `closes` verb for ask TOOL-aNimbleMend-24, which
  that unit's header carries for both sentences. This unit's header carries no backlog verb, so
  without that unit the ask has no closing spec.
- **hands-off** external — the main loop writes S4's row before the pass, and runs the legs of §7
  at the close.

## 4. Design

### Evidence

Read at 82ceaab5, which adds only records to 8db6f4be.

| Fact | Where |
|---|---|
| The sentence reads "the fix's typed record is the next commit", with no reason. | `tools/unattended/PROTOCOL.template.md@b48ad9f5:726-727` |
| The record's `Commit` field is the full sha the door resolves from `--commit`, never a flag's text. | `tools/memory-tree/build_records.py#write_red_fix` |
| The door refuses a rev that names no commit reachable from `HEAD`, so the fix is committed first. | `tools/memory-tree/build_records.py@b854dda5:396-401` |
| The join prints a fix at `HEAD` with no record as owed, because its record is the next commit. | `tools/memory-tree/build_records.py@b854dda5:464` |
| The template and its render are the same bytes: the pair holds no placeholder. | `cmp` of the two files, silent at 82ceaab5 |
| The render measures 68022 bytes CR-stripped against a row of 68022, and the block's rule is no headroom (PINNED, 2026-11-13). | `tools/template-size-limits.txt@a7cfff29:162-166` |
| A run may raise a measured-file row on four terms. | `tools/template-size-limits.txt@a7cfff29:16-28` |
| No suite or gate pins the sentence. | `git grep -n "record is the next commit" -- . ':!memory/builds'` finds the pair, one code comment and one gate comment |
| `memory/DECISIONS.md` is a declared shared record. | `.unattended.conf`, key `SHARED_RECORDS` |

### The sentence

In the template and in the render, these two lines:

```text
record is the next commit, and the commit grader holds the fix to its limits. Every other product
write keeps the route above; either key `off` restores it for that mechanism.
```

become these three:

```text
record is the next commit, because it names the fix commit's sha and so cannot ride that commit,
and the commit grader holds the fix to its limits. Every other product write keeps the route above;
either key `off` restores it for that mechanism.
```

The clause adds 70 bytes and one line, and the longest new line is 99 characters (PINNED,
2026-11-13, the replacement applied in memory to the template at 82ceaab5). The rest is a reflow
of the same words.

### The row

The render sits exactly on its row, so the clause takes it past. The four terms hold as they held
for TOOL-aNimbleMend-11: this unit's change takes the render past the row; the row's block reserves
nothing to the owner and states no headroom, so the new value is the measured render exactly; the
movement is argued above the row; and S4's row lands before the raise. The terms open with "a unit
of a build the owner mandated". This build is one: the owner's prompt orders it and names this
sentence and this carrier, as the build's brief quotes. The comment added above the row:

```text
# RAISED 68022 -> <measured>, 2026-11-13, by TOOL-aClearedLedger-2: section 12's reason that a red
# fix's record is the next commit, which the owner ruled the protocol states. The render measures
# <measured> CR-stripped, and the row is that figure because this block's rule is no headroom. A
# run's raise, on the four terms above (memory/DECISIONS.md, TOOL-aClearedLedger-2).
```

`<measured>` is DERIVED at the pass by `tr -d '\r' < memory/guides/UNATTENDED-PROTOCOL.md | wc -c`.
It is 68092 with the replacement applied in memory at 82ceaab5 (PINNED, 2026-11-13).

S4's row takes the shape of the row for TOOL-aNimbleMend-11 in `memory/DECISIONS.md`: the unit id,
that section 12's reason raises the protocol's no-headroom size row to its render's measured bytes,
`agent, 2026-11-13, under TOOL-aOrientedCast-23's four raise terms`, and `Detail builds/aClearedLedger/`.

### Rendering

The builder applies the edit to the template and to the render. The pair holds no placeholder, so
the render of the edited template is the edited file. Where the pass's hook admits it,
`bash tools/unattended/adopt-unattended.sh` writes the same bytes.

### What it does not check

- That the sentence is true of a future door. Two legs byte-compare the pair to each other, so a
  claim false in both copies is green, as the protocol's own opening says.
- The row at the pass. The size gate's reader takes the limits file at the landed revision, so the
  `unattended protocol size` leg warns between the pass and the landing; AC3 holds the figure.

### Inventory

Nothing is minted: no key, verb, flag, leg or file.

### Migration

None. An adopter receives the sentence when its next update copies the protocol.

### Rollout

No switch. The sentence describes what the door and the join already do.

### Files touched (estimate)

- `tools/unattended/PROTOCOL.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `tools/template-size-limits.txt`

### Alternatives rejected

- **Trimming the paragraph to fund the clause.** The protocol has no free byte, so the trim would
  cut another sentence of the same paragraph, which the owner's earlier prompt asked it to state.
  Each of the last three raises of this row paid with the ceiling on the four terms.
- **Leaving the row and letting the leg warn.** The block's rule is that the row equals the render,
  and a row left behind makes every later unit's first raise term false.
- **Stating the reason in the help page instead.** The ask names the protocol's sentence, and the
  owner ruled that the carrier that states the rule says what was ruled.
- **A longer account of the door and the join.** The protocol points; `help/red-fix-lane.md` and
  the kit README hold the detail.

## 5. Production-readiness checklist

- security — No write path, hook or input boundary. The clause explains an order the door already
  enforces.
- perf / scale — The protocol grows 70 bytes, read whole by a run at its own boundary (PINNED,
  2026-11-13).
- error / empty / loading states — A sibling that moves the same paragraph first makes §4's two
  lines not match. The builder then returns the gap and does not rewrite the paragraph from memory.
- observability — The size row's comment records the movement, and the decision row names the unit.
- risks — The reading that this attended build is one "the owner mandated" is this spec's. If the
  owner reads the raise terms otherwise, S3 and S4 become an owner's raise and the sentence stands.
- testing — AC1 to AC3 are a `cmp`, greps, a `git diff` and a byte count. The close's size and
  parity legs grade the whole.
- migration — None (§4, "Migration").
- user docs — `help/red-fix-lane.md` already states the rule, so no page moves.

## 6. Acceptance criteria

- **AC1** — When `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md`
  runs it prints nothing and exits 0, and `grep -c "because it names the fix commit's sha"` over
  each file prints 1, on a line between the headings `## 12.` and `## 13.`.
  Red when: one file took the edit and the other did not, or the reason landed outside section 12.
- **AC2** — When `git diff --numstat 8db6f4be -- tools/unattended/PROTOCOL.template.md` runs it
  prints one row, three lines added and two removed, and
  `grep -c "Two switches act BETWEEN passes" tools/unattended/PROTOCOL.template.md` still prints 1.
  Red when: the edit moved another sentence of the protocol, or the paragraph's opening changed and
  the ask's own probe no longer finds it.
  figure: three and two are PINNED, from §4's replacement applied in memory at 82ceaab5.
- **AC3** — When `tr -d '\r' < memory/guides/UNATTENDED-PROTOCOL.md | wc -c` runs, the figure it
  prints equals the second field of the row
  `grep -P '^memory/guides/UNATTENDED-PROTOCOL\.md\t' tools/template-size-limits.txt` prints,
  `grep -c "RAISED 68022 -> " tools/template-size-limits.txt` prints 1 on a line naming this unit,
  and `git log --format=%H -1 -S"TOOL-aClearedLedger-2" -- memory/DECISIONS.md` names an ancestor
  of the commit that moved the row.
  Red when: the row keeps headroom, the movement is not argued in place, or the raise landed with
  no decision row before it.
  figure: the row's new value is DERIVED at the pass; 68022 is PINNED at 82ceaab5.
  permission: the decision row is the main loop's write, in a `Pass: none` commit before the pass.

## 7. Gates

`unattended protocol size` · `kit/dogfood doc parity` · `unattended skill wiring` · `unattended kit gate` · `policy fixtures` · `recall floor` · `recall floor arms` · `line length` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The close's bar runs these once, after the last unit. `unattended skill wiring` and
`kit/dogfood doc parity` compare the render to its template. `unattended protocol size` grades S3
under `budgets.enforce`, which reads `warn` in this repository, so a breach there prints and does
not refuse: AC3 is the check that holds the figure.

This unit adds no arm. The one class it could break, a render that differs from its template, is
the two parity legs' own.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-13 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "render the unattended protocol template into its
rendered copy"` names the seam this unit extends: `render` in `tools/unattended/adopt-unattended.sh`,
which copies the protocol because it carries no placeholder. The unit adds a clause to one existing
paragraph and one comment block to an existing row, and adds no code. The recall probe returned
TOOL-aNimbleMend-11, whose spec wrote the paragraph and raised the same row on the same terms, and
its decision row, the shape S4 follows. The probes and source agree.

Recall terms used: `practice catalogue spec line red-fix lane inline record next commit protocol size row raise one-line`
