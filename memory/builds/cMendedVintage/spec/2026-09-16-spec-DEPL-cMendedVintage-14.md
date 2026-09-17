# DEPL-cMendedVintage-14 — stale conflict orders are reaped, and keyed on the full path

**Status:** CLOSED · rev-3 · 2026-09-17 · node c · Tier-2 · base 859daa67 · streams deployer · order 25

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-17-build-DEPL-cMendedVintage-14-acceptance-ledger.md](../build/2026-09-17-build-DEPL-cMendedVintage-14-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |
| [2026-09-17-prompt-DEPL-cMendedVintage-14-2-build-brief.md](../prompts/2026-09-17-prompt-DEPL-cMendedVintage-14-2-build-brief.md) | journal | — |
| [2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md) | spec-audit | TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 |

<!-- /gen:spec-records -->

## 1. Goal

`update` writes a conflict order into the target's outbox and nothing ever removes one, so an
operator who resolves a conflict keeps reading the order that says it is still open. The same
writers key the filename on the path's BASENAME, so two conflicts over two files called `kit.toml`
produce one order and one of them is silently lost. Key the filename on the full path, and let an
unscoped write run reap the conflict orders it did not write.

## 2. Scope (IN)

- **S1** A `render_order_slug(path)` helper renders an order filename component from a full receipt path:
  every run of non-alphanumeric bytes collapsed to `-`, trimmed, capped at 60 characters, then a
  `-` and the first 8 hex of the sha256 of the FULL path. Observed by AC2.
- **S2** All three writers key on it: the rename-conflict order, the withdrawal order and the
  diverged-conflict order, all three in `_cmd_update` and all three located BY SYMBOL — rev-1's line
  numbers were stale before the build opened. The withdrawal writer has the same collision and is
  re-keyed with them. Observed by AC2 and AC3.
- **S3** Each conflict order's path is collected into a set as it is written. At the end of a
  `--write` run whose `--kits` scope is EMPTY, every `update-conflict-*.md` in the outbox that is
  not in that set is unlinked, its index entry unstaged with it, and the run prints how many it
  removed and their names. Observed by AC1 and AC5.
- **S4** A run carrying a `--kits` scope reaps nothing and says so in one line. A scoped run
  classifies a subset of the receipt's rows, so an order belonging to an out-of-scope row is not
  stale — it is unexamined, and deleting it would destroy the only record that the row is still
  conflicted. Observed by AC4.
- **S5** Withdrawal orders are not reaped, and the reason is written into the code beside the glob:
  a withdrawal order records an action that happened or was withheld, and its row LEAVES the receipt,
  so no later run can re-derive it. A conflict order records a STATE that every run re-derives, which
  is what makes its absence information. Observed by AC5.

## 3. Non-goals (OUT)

- **No counting-threshold refusal.** A cap that aborts the run once N orders exist converts a backlog
  into a wedge, which is the recorded reason `report` replaced `refuse` for the forked role. The reap
  is the mechanism; there is no second one.
- No change to the order BODIES. Their text is correct; only their names and their lifetime move.
- No reaping of `update-rollback-*.md`, `update-preexisting-red-*.md` or the machine and hole orders
  `apply` writes. The first two are event records with the same property as a withdrawal, and the
  last are recorded in the receipt's `orders` list, which `check` asserts against disk — a glob
  scoped to `update-conflict-*.md` cannot reach any of them, and that scoping is the guard.
- No retro-keying of `apply`'s order filenames. Those paths are recorded in the receipt, so renaming
  them would orphan a recorded row to buy consistency nobody reads.
- No receipt bookkeeping for conflict orders. `update` maintains no `orders` list at BASE; minting
  one so the reap could consult it would put a second writer on a field `apply` owns.

### Edges

none

## 4. Design

### Data model

Nothing is persisted. The reap's state is one `set[pathlib.Path]` local to `_cmd_update`, populated
at the three write sites and read once at the end of the run. The filename is the only durable
artifact and its grammar is S1's.

### Why the digest, and what it still cannot do

A 60-character cap on the slug alone re-opens the collision this unit exists to close: two deep
paths sharing a 60-character prefix collapse to one order exactly as two `kit.toml` rows do today.
The 8-hex digest of the full path is what makes the key injective, and the readable slug in front of
it is what keeps the file identifiable by a human in the outbox listing.

What it still cannot do, stated rather than implied away — and rev-3 corrected this paragraph after
MEASURING it, because rev-2 stated the opposite and was wrong. Two paths differing only in case do
NOT collide on a case-insensitive filesystem: the digests differ, so the two filenames differ by more
than case and Windows keeps both. Measured on `tools/demo/Kit.toml` against `tools/demo/kit.toml`,
which render `tools-demo-kit-toml-14ccee6f` and `tools-demo-kit-toml-5e5e7d00`.

The residue that IS real is the 32 bits. Two distinct paths whose lowercased 60-character slugs AND
whose first 8 hex both agree still produce one filename, and nothing detects it. It is pinned here
and not closed; closing it is a wider digest, which buys nothing against a birthday bound no fleet
this size will reach. The readability residue is the one an operator will actually meet: two
case-variant paths render the same readable half and are told apart only by the hex.

### The reap's scoping, in one place

| condition | reaped |
|---|---|
| `--write`, no `--kits` | every `update-conflict-*.md` this run did not write |
| `--write`, with `--kits` | nothing, and the run says so |
| read-only | nothing; the run wrote no orders, so its set is empty and a reap would delete them all |

The read-only case is the one that would be silently catastrophic, which is why it is a row in this
table and a scope item rather than an implicit consequence of sitting inside the write branch.

It is NOT spelled as an `if write:` guard, and rev-3 settled that after reading the function. The
read-only branch RETURNS hundreds of lines before the outbox is even bound, so such a guard is a
condition that cannot be false — the could-not-fail shape this engine bans, and the same reasoning
the gate-leg step below the reap already records about its own missing guard. What replaces it is a
STRUCTURAL assertion in the arm: the last `if not write:` before the outbox bind returns, and `write`
is never rebound. If that return ever moves, the arm reds rather than the outbox emptying.

### Inventory

| identifier | kind | where |
|---|---|---|
| `render_order_slug` | module-level function | `tools/govkit/govkit.py`, beside `marker_pair` |
| `_orders_written` | local set in `_cmd_update` | beside `_reaped` |
| `_reap_names` | local list in `_cmd_update` | in the reap block |

rev-1 named this helper `order_slug`, and `order` leads no row of the verb table. `--suggest` was
asked and answered: `render_order_slug` satisfies `py.function`. `slug` stays the noun the
machine-order writer already uses for the same computation.

`_orders_written` sits beside `_reaped` rather than beside `changed` and `deleted`, because `_reaped`
is the set the renormalize below already consults and the reaped orders join it — see the migration
note.

### Migration

An order written by an earlier vintage carries the basename key and is therefore not in this run's
set, so the first unscoped `--write` after this lands removes every one of them — including any whose
conflict is still open, which are then rewritten under the new key by the same run, because the
classification loop reaches the write sites before the reap. The order of those two steps is the
whole of the migration and is why the reap is at the END of the run rather than at its start.

rev-3 adds the half rev-2 missed: the reaped order's INDEX entry is unstaged with it, by the same
`git rm --cached --ignore-unmatch` the `update-pins.md` reap above already performs, and its path
joins `_reaped`. Without it a target that COMMITS its outbox hands the renormalize below a pinned
path missing from the worktree, and gov refuses the renormalize over a deletion gov itself made.
That failure is already measured and recorded at that earlier reap; shipping the same unlink without
the same treatment would have re-earned it.

### Alternatives rejected

- **Reap at the start of the write phase.** Every order would be deleted and only the still-open
  ones rewritten, which is the same end state through a window in which the target has none. The
  window matters because a run can fail between the two.
- **Key on the path with separators replaced and nothing else.** A path is not a filename: `..`,
  a leading dot and a path longer than the filesystem's component limit each break it, and the
  existing machine-order writer already solved this with a slug.
- **Record orders in the receipt and reap from that list.** It makes the reap exact, and it puts
  `update` on a field `apply` owns and `check` asserts. The glob is scoped enough to be safe and
  needs no coordination between two writers.
- **Reap every `update-*.md`.** It would take the withdrawal and rollback records with it, which is
  S5's whole point.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/govkit.py` | the slug helper, three re-keyed writers, the collection set, the reap |
| `tools/govkit/selftest.py` | the arms §7 names |

## 5. Production-readiness checklist

- security — the reap unlinks inside `target/.governance/outbox` only, over a glob gov's own writers
  own. The filenames it matches are derived from receipt paths through a slug that strips every
  separator, so no receipt value can steer the unlink outside that directory.
- perf / scale — one directory listing per unscoped write run, plus one sha256 of a short string per
  order written.
- error / empty / loading states — an outbox with no conflict orders reaps zero and prints zero; an
  absent outbox is created by the existing `mkdir` above the write loop; an unlink that raises
  `OSError` is reported by name and does not abort the run.
- observability — the count prints on every unscoped write run including the zero, because a silent
  reap is indistinguishable from a reap that never ran. A scoped run prints why it reaped nothing.
- risks — the sharpest is deleting an order whose conflict is still open. It is structurally
  prevented rather than checked: the write sites run before the reap in the same function, so an
  open conflict is in this run's set by construction. The second is a read-only run reaching the
  reap, which S3's write guard and AC5 both address.
- testing — AC1 through AC5 on scratch fixture targets. Gov does not dogfood govkit and carries no
  receipt, so no criterion here is observable against this repo.
- migration — §4 states it: one run removes the old-key orders and rewrites the open ones.
- user docs — `WIRE-INTO-PROJECT.md` describes the outbox. rev-3: there is NO sentence there saying
  orders are never removed — the file was grepped and rev-2 invented it. The one adjacent sentence,
  about gate-leg rows arriving as an order that nothing removes for you, is still true and is out of
  this glob's reach. What the runbook gains instead is a paragraph documenting the reap, because a
  verb that DELETES a file in a repository gov does not own has to be written down somewhere the
  operator reads.

## 6. Acceptance criteria

- **AC1** — When a scratch fixture target is driven into a three-way conflict on one row,
  `python tools/govkit/govkit.py update --target <fixture> --write` writes a conflict order for it,
  the conflict is then resolved so the row no longer conflicts, and the same command runs again, the
  order file is gone and the run reports one reaped.
  Red when: the reap is keyed on the orders that EXIST rather than on the set this run wrote, in
  which case nothing is ever stale and the arm passes over a reap that removes nothing.
  fixture: a scratch fixture target under the run's scratch root, built with `intake` then `apply`
  and then edited to force the conflict. This repo keeps no receipt and can host no criterion here.
- **AC2** — When two receipt rows whose paths share a basename both conflict in one
  `python tools/govkit/govkit.py update --target <fixture> --write` run, the fixture's outbox holds
  TWO conflict orders afterwards and each names its own full path in its body.
  Red when: the filename still keys on the basename, so the second write overwrites the first and
  one conflict has no order — the defect, observed rather than argued.
- **AC3** — When a row is withdrawn in a
  `python tools/govkit/govkit.py update --target <fixture> --write` run where another withdrawn row
  shares its basename, the outbox holds two withdrawal orders.
  Red when: only the two conflict writers are re-keyed, which leaves the third with the collision
  the unit was opened to close and makes the fix an instance fix.
- **AC4** — When the same fixture is run with
  `python tools/govkit/govkit.py update --target <fixture> --write --kits <one-kit>` while another
  kit's conflict order is on disk, that order is still there afterwards and the run says it reaped
  nothing because the run was scoped.
  Red when: the reap ignores the scope, which deletes the only record that an out-of-scope row is
  still conflicted and does it silently.
- **AC5** — When `python tools/govkit/govkit.py update --target <fixture>` runs with no `--write`
  while a conflict order and a withdrawal order are on disk, both are still there afterwards.
  Red when: the reap sits outside the write guard; its set is empty on a read-only run, so a preview
  deletes every order in the outbox.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: `tools/govkit/selftest.py` · a fixture conflicted on two rows sharing a basename, asserted
to produce two orders, then resolved and re-run and asserted to have them reaped.

rev-3: `BRANCH_PIN` does NOT move. Q3 resolved the failed unlink to a `print` rather than an
`r.fail`, so this commit adds no refusal branch and removes none — and the pin is a FLOOR, redding
only when the count DROPS below it, so an addition could not red it either way.

## 8. Open questions

- **Q1 — should the reap also remove `update-pins.md`?**
  RESOLVED (agent, 2026-09-16, delegated): no, and it does not need to.
  `DEPL-cMendedVintage-10` stops writing that file and unlinks a stale one at the site that
  supersedes it, which is a targeted removal by the unit that owns the state. Widening this glob to
  reach it would give two units one deletion.
- **Q2 — FACT-QUESTION · can the reap's glob collide with an order `check` asserts against the
  receipt?**
  RESOLVED (agent, 2026-09-16, delegated): no. The probe is reading `cmd_check`'s outbox arm at
  `tools/govkit/govkit.py:3196`, which iterates `receipt["orders"]`, against every `orders.append`
  call site in the engine: all of them are in `_cmd_apply` and write `hole`, `machine` or
  `gate-legs` order paths, none of which matches `update-conflict-*.md`. The probe can produce a
  negative — one `orders.append` in the update path, or one recorded path with that prefix, would
  make the answer yes — and there is neither.
- **Q3 — should a failed unlink fail the run?**
  RESOLVED (agent, 2026-09-16, delegated): no. It is reported by name and the run continues. A stale
  order left on disk is the state the target was already in, and failing the run over it would
  withhold the receipt re-stamp for a file whose only reader is a human.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-2 · 2026-09-16 · AC2 and AC3 named no backticked witness, which HYGIENE check 12 refuses at
  this file's date; each now spells the `update --write` run it observes. Acceptance unchanged.
- rev-3 · 2026-09-17 · six corrections, all made during the build and all but the first measured.
  (a) S1's `order_slug` is `render_order_slug`: `order` leads no row of the verb table and
  `--suggest` answered `render`. (b) §4's case-collision residue was BACKWARDS — the digests differ,
  so two case-variant paths keep two files on a case-insensitive filesystem; the real residue is the
  32-bit digest, and the paragraph now says so with the two rendered names. (c) S3 gains the index
  unstage, without which a target that commits its outbox has its renormalize refused over gov's own
  deletion. (d) §4 records that the read-only case takes no `if write:` guard, because the read-only
  branch returns before the outbox is bound and the guard could never be false; a structural arm
  replaces it. (e) S2 drops rev-1's three line numbers, which were stale. (f) §5's user-docs line
  named a sentence `WIRE-INTO-PROJECT.md` does not contain. Acceptance criteria are UNCHANGED: every
  one of AC1..AC5 was observed as written.

## 10. Reuse audit

The seam this unit extends is the outbox write region of `_cmd_update`, read from source: the
directory is created once at `tools/govkit/govkit.py:6661` and the three writers below it already
share a filename shape, which is what makes one slug helper a replacement rather than an addition.
The slug computation itself is reused from the machine-order writer at
`tools/govkit/govkit.py:4867`, which already collapses a resolved destination to a filename
component. `python tools/codebase-map/reuse_lookup.py "write the govkit-owned gitattributes pin
block and renormalize the pinned population"` — the probe run for this build's outbox-adjacent units
— returned no seam for order lifetime, only name-token neighbours such as `write_text` in the
memory-tree kit. The recall probe supplied the constraint in §3 rather than the mechanism:
`DEPL-dCarriedReceipt-2` records that the outbox order shape was reused from the three-way conflict
writer, and the `report`-replaced-`refuse` ruling for the forked role is why no counting threshold
ships here.

Recall terms used: `--terms "govkit update outbox order conflict three-way withdrawn basename
collision reap stale receipt orders"`, with the question "how does govkit update name the conflict
order files it writes into the outbox and does anything remove a stale one".
