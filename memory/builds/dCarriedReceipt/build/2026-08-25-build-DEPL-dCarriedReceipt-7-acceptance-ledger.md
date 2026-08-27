# Acceptance ledger — DEPL-dCarriedReceipt-7, two identities, read index-side

**Serves:** journal DEPL-dCarriedReceipt-7

**Evidences:** DEPL-dCarriedReceipt-7
- AC1 — `tools/govkit/selftest.py` — RED observed at HEAD: a memory-tree install read
  `current 27 · missing 3`, and its own `git clone -c core.autocrlf=true` read
  `current 4 · missing 3 · patched 23`. GREEN: both read the same tally. The arm asserts EQUALITY
  between clone and original rather than literal counts, because the population moved with the tree.
- AC2 — `tools/govkit/selftest.py` — an unstaged worktree edit leaves the row `current`; `git add`
  of that same edit moves it to `patched`. Both halves red under separate staged breaks.
- AC3 — `tools/govkit/selftest.py` — RED observed by staging S2 without S4: an operator's untracked
  file was overwritten with gov's bytes at exit 0. GREEN: refuses by name, bytes byte-identical.
- AC4 — `tools/govkit/selftest.py` — RED observed, and WORSE than the spec predicted: on an
  autocrlf clone the untouched tree read `diverged`, the three-way CONFLICTED, the run exited
  non-zero, and the index kept the old blob. GREEN: the row reads `stale` and the index blob equals
  gov's blob at `--to` exactly.
- AC5 — `tools/govkit/selftest.py` — a clean `--write` re-stamps schema 3 and every engine row
  carries both identities plus `sha256`; the attributes row carries neither. Hand-built schema-1 and
  schema-2 receipts classify with no refusal, and the schema-1 role-distrust guard still fires.
- AC6 — `tools/govkit/selftest.py` — RED observed by staging the worktree/`sha256` comparator back
  in: rewriting every `sha256` to one constant moved 26 verdict lines from `current` to `patched`.
  GREEN: 0 lines move.
- AC7 — `python tools/govkit/refusal_join.py` — exit 0 at 174 branches against a shrink-only pin of
  161. Each of the three named refusals is reached by an arm. NOT a machine-verified join: nothing
  in this tree passes `refusal_join` a reached-set, so its join half still never executes, and that
  is stated rather than implied by a green.
- AC8 — `tools/govkit/selftest.py` — RED observed on a fixture whose `gov_oid` was poisoned with the
  target's own blob: an operator's COMMITTED edit classified as `equal` to gov and `update --write`
  overwrote it at exit 0. GREEN: refuses naming the path and both oids.
- AC9 — `tools/govkit/selftest.py` — RED observed by staging S9 unscoped over every row: the
  preamble refused on the field-less row and the stale row never moved. GREEN: the run completes,
  the stale row moves, the field-less row prints by name.
- AC10 — `tools/govkit/selftest.py` — both half-populated shapes refuse by name, write nothing, and
  leave the receipt byte-identical. Six arms red under the exactly-one break.
- AC11 — `tools/govkit/selftest.py` — THE KEYSTONE, and the reason §8 F4 exists. The fixture
  reproduces the recorded six-row `push-main` receipt exactly, merged row carrying `commit`,
  `source`, `block_sha256` and neither identity. GREEN: both `update` and `update --write` exit 0
  and the merged row reaches its block compare. RED observed by staging the F4 exemption out: the
  whole run refuses before any row is classified, at rc=2.

## Arms with NO observed red, named rather than implied

- AC3's NEGATIVE arm. Its failing case is an over-firing S4, which no break produced.
- AC9's "written in NEITHER direction". A source-less row has no `theirs` and cannot reach any write
  arm under any break; it guards a future unit widening the write arms, not a live discriminator.
- The pure fixture-assertion arms, whose failing case is a fixture that stops triggering the rule.
  Two of them DID red when an upstream refusal emptied their population, which is the shape they
  exist to catch.

## What this unit does NOT close

`cmd_check` is untouched, though §4's data model names its provenance and integrity loops as readers
of the two identities. No scope item asks for it, and it was MEASURED: `check` reds on an autocrlf
clone with the HEAD engine as well as with this one, so that half of §1's goal is pre-existing and
unchanged here.

The diverged arm still stamps the merge result into `gov_oid`, so `gov_oid` there names bytes gov
never shipped. §3's non-goals require exactly that, so `-8`'s red-first survives; the code says so at
the site.

S9 adds one `git show` per identity-carrying row and recomputes what `classify_row` later reads as
`base`. §5's "strictly fewer syscalls" holds for the index read alone, not for the run as a whole.

## The user-facing half, closed here rather than in the unit

`skills/deploy-governance/SKILL.md` now documents the two identities and schema 3. The builder could
not write it — the file was outside its permitted edit set — and the charter makes a user-facing
change undone until its page is updated. An adopter reads that page to learn what lands in their
repo, and a receipt whose schema moved is exactly that kind of change.

## Owner ruling 2026-08-26 — S4's shadow refusal is scoped to the table, and the park is closed

S4 refuses a receipt-claimed path present in the WORKTREE and absent from the INDEX. Its own text
names the hazard: without it the index read's `absent` routes to `missing` and then to the raw write
at `:3069`, which would overwrite an operator's untracked file. Only rows the update dispatch sends
to the `table` disposition reach that write. The predicate was UNQUALIFIED by role, so a
`generated`, `project-owned`, `rendered` or `gate-leg` row whose destination happened to be
present-but-untracked refused the ENTIRE run — for a write that could never have happened, and with
the operator's only route back to green being `git add` on a file gov will never write.

**Scoped to `UPDATE_ROLE[role] == "table"`**, one condition, matching the stated hazard exactly.
What the narrowing gives up is recorded rather than implied: an untracked file shadowing a non-table
row now passes unremarked, as it did before this unit landed.

**Armed as a pair.** The positive half already existed — `[-12] S4 ...it is `-7` S4's refusal that
owns that tree now`, on an engine row. The negative half is new and is the one that was missing:
- `[-12] RULING-B` — a NON-table receipt row shadowed by an untracked file does not refuse the run,
  with two liveness arms first (the fixture really carries such a row on disk; it really is out of
  the index and still present).

Nothing in this build's fixtures tripped the unqualified form, which is why nothing warned first —
recorded here because that absence is the finding, not the reassurance.
