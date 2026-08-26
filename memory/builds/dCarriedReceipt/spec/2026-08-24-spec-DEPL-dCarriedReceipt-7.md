# DEPL-dCarriedReceipt-7 — two identities, read index-side

**Status:** CLOSED · rev-8 · 2026-08-26 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-build-DEPL-dCarriedReceipt-7-acceptance-ledger.md](../build/2026-08-25-build-DEPL-dCarriedReceipt-7-acceptance-ledger.md) | journal | — |
| [2026-08-25-build-DEPL-dCarriedReceipt-7-merged-row-reproduction.md](../build/2026-08-25-build-DEPL-dCarriedReceipt-7-merged-row-reproduction.md) | research | DEPL-dCarriedReceipt-13 |
| [2026-08-24-review-DEPL-dCarriedReceipt-1-spec-precode.md](../reviews/2026-08-24-review-DEPL-dCarriedReceipt-1-spec-precode.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-8 |
| [2026-08-25-review-DEPL-dCarriedReceipt-1-round4.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-1-round4.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-8 |
| [2026-08-25-review-DEPL-dCarriedReceipt-1-round5.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-1-round5.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-8 |
| [2026-08-25-review-DEPL-dCarriedReceipt-1-round6.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-1-round6.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-8 |

<!-- /gen:spec-records -->

## 1. Goal

One receipt field is asked to be two different things at once. `classify_row` (`govkit.py:2874`)
compares `sha256` against the target's WORKTREE bytes — `dp.read_bytes()` at `:2884`, the comparison
at `:2889` — while `cmd_check`'s provenance loop compares that same field against GOV's blob at the
row's `commit` (`:1522-1531`). Both claims can hold only where the target's worktree bytes are
byte-identical to the blob gov shipped, and that is false for any adopter whose clone applies a
line-ending filter.

Measured here on 2026-08-24 at `9ddcc5c9`. A scratch target takes `govkit.py apply --kits
memory-tree`, which lands 24 files and writes 28 rows, and `update` against it reports `current 24 ·
missing 3`. The same target cloned with `git clone -c core.autocrlf=true` reports `current 1 ·
missing 3 · patched 23`. Twenty-three of twenty-four engine rows read as locally modified because
the worktree holds CRLF and gov shipped LF. The one survivor is the one engine row of that kit's
twenty-four that falls under one of its `lf_pin` blocks, and the shipped kits declare 22 `lf_pin`
patterns across 11 of the 25 registry entries, so nothing govkit installs makes an adopter immune.
An adopter on a default Windows clone therefore reads about 96% false divergence, achieves zero
automatic adoption, and is shown a plausible table while it happens.

The fix is the two identities. `gov_oid` is the git blob gov shipped at the row's `commit`, it
means that forever, and it is STORED in the receipt rather than recomputed on every read (owner
decision, 2026-08-24). `oid` is the git blob the TARGET holds, read from its INDEX and never from
its worktree. `sha256` is retained so a schema-2 reader keeps working, and stops being the comparator.

## 2. Scope (IN)

- **S1** — every receipt row gov writes for a LANDED file — the `writes` channel at
  `:2443-2460` — carries `gov_oid` and `oid`. A row written through the `unlanded` channel at
  `:2440` carries neither, as it carries no `commit` today, and this unit does not add them: there
  are no gov bytes at that destination to hash. There are TWO more producers, and neither carries
  either identity. The `merged` row `apply` writes at `:2417` carries `source` and `commit` but
  NEITHER identity — gov's bytes at that destination are a BLOCK inside a file the target owns, so
  there is no whole-file gov blob to hash, which is why the row carries `block_sha256` instead —
  written by `cmd_apply` at `:2417-2422` today and measured from the block the target holds by
  `-13` S11. `-8` is not its owner: that unit is the three-way merge of ENGINE rows at `:3097-3099`
  and leaves `UPDATE_ROLE` untouched. The `attributes` row `apply` synthesizes at `:2350` carries
  neither identity either, and no `commit` or `source` to derive one from: gov's bytes there are a
  block `lf_pins()` composes rather than a blob it shipped, which is why it carries `block_sha256`
  alone (`-13` S11). Those four are the whole producer set, observed on one six-row receipt in
  `memory/builds/dCarriedReceipt/build/2026-08-25-build-DEPL-dCarriedReceipt-7-merged-row-reproduction.md`.
  `sha256` is still written on the `writes` channel's rows, is still what `install.sums` lists, and
  decides no verdict.
- **S2** — `classify_row` reads ours as the target's INDEX blob, from one batched
  `git -C <target> ls-files -s -z --` over the receipt's paths, rather than `read_bytes` at `:2884`.
  `theirs` and `base` keep `blob_at` (`:2148`), which is already index-side by construction.
- **S3** — `gov_oid` is a STORED receipt field. It is written once per row, from gov's blob at
  that row's `commit`, and read back from the file on every later run; nothing recomputes it at read
  time. The OURS axis compares the target's LIVE index blob against that stored `gov_oid`, never
  against `sha256`. `oid != gov_oid` is the local-delta predicate, evaluated per run from the live
  read, and no boolean anywhere stores its answer. Stored field, live comparison — S9 is what keeps
  the stored half honest.
- **S4 — SCOPED TO TABLE-DISPATCHED ROWS at rev-8, by owner ruling 2026-08-26.** The predicate below
  applies to a row whose role dispatches to the `table` disposition, and to no other. It shipped
  UNQUALIFIED by role and this unit parked that: the raw-write hazard the sentence after it NAMES is
  reachable only from the table arm, so a `generated`, `project-owned`, `rendered` or `gate-leg` row
  whose destination happened to be present-but-untracked refused the ENTIRE run for a write that
  could never have happened -- and the operator's only route back to green was `git add` on a file
  gov will never write. No fixture in this build tripped it, so nothing would have warned first.
  What the narrowing gives up is stated rather than implied: an untracked file shadowing a non-table
  row now passes unremarked, exactly as it did before this unit landed. What it buys is that the
  refusal fires where the hazard is, which is the difference between a guard and a tax. Armed as a
  pair -- an engine row still refuses, a non-table row does not.

  A receipt-claimed path that is PRESENT IN THE WORKTREE and ABSENT FROM THE INDEX is a
  REFUSAL naming the path. Without it the index read's own `absent` routes to `missing` and then to
  the raw write at `:3069`, which would overwrite whatever untracked file the operator has there.
  The predicate is stated in those terms deliberately. An earlier rev said "tracked in the target but
  carries no index entry", which describes nothing: `tracked()` at `:111-112` IS `git ls-files`, a
  read of the index, so tracked-and-not-indexed is empty except for an unmerged path — and an
  unmerged path is `-12` S3's refusal, one step earlier. `-12` S4's dirty check carves this state out
  explicitly so the two units do not both refuse it with different messages. The predicate is
  evaluated in the PREAMBLE, over the same batched `ls-files -s` read S2 takes, before any row is
  classified — it is a whole-run refusal and must not depend on which rows the loop has already
  reached.
- **S5** — writes go `git hash-object -w --stdin`, then `git update-index --cacheinfo`, then
  `git checkout-index -f --`, so the TARGET's own filters decide its worktree bytes. The mode comes
  from the row's existing index entry, and from gov's tree entry at `commit` for a row with none.
- **S6** — `RECEIPT_SCHEMA` goes 2 to 3 (`:39`) and readers accept 1, 2 and 3. The schema-1
  role-distrust arm keeps its `schema < 2` bound and keeps firing. This is the build's ONLY schema
  move. `-13` §4 Migration states that rule and names every field schema 3 carries, `-9`'s and
  `-13`'s included, so no later unit in this build mints a second number.
- **S7** — `cmd_apply` records both identities on the `writes` channel's rows only: `gov_oid` from
  the gov blob it wrote, and `oid` read from that path's index entry after the `git add` at
  `:2477-2478` — which stages every channel's paths, so the read is per row and not per stage. The
  `:2440`, `:2417` and `:2350` rows take neither, per S1.
- **S8** — one selftest arm per acceptance criterion, plus the class gate AC6 describes.
- **S9** — `cmd_update`'s preamble gains a per-row integrity assertion, beside the existing
  unresolvable-commit refusal at `:2946`, running over the whole receipt before any row is
  classified. It is SCOPED BY FIELD PRESENCE, in three arms, plus one exemption by ROLE. A row
  carrying BOTH `commit` and `gov_oid` is asserted: `gov_oid == blob_at(root, row["commit"],
  row["source"])`, and a row that fails refuses by name, naming the path and both oids, rather than
  being classified against a field the file no longer earns. A row carrying NEITHER field is passed
  over here, because it is not a failed integrity check — there is nothing to compare. Note what
  that row is NOT: it is not necessarily `-13` S7's `evidence: "unattributed"` state. Every row
  `apply` writes through the `unlanded` channel also carries neither field: those are the rows
  `apply` writes at `:2440` — `project-owned`, `generated` and `rendered` — and the `attributes`
  row at `:2350`, which carries neither for the same reason and is passed over by this same arm.
  `UNLANDED_REASON` (`:236`) carries a fourth key, `merged`, and `resolve_entry`'s `unlanded` list
  carries merged entries too; `apply` skips them at `:2428-2429` and writes the real merged row at
  `:2417` instead. `-10` S3 adds a fifth key, `forked`. S9 passes over the `:2440` rows for the one
  reason that covers every case — no operand — and over a `merged` row by the role arm below; what
  happens next is the ROLE's business, in the classification loop, not this preamble's. A row
  whose `role` is `merged` is
  passed over whatever `commit` it carries. That `commit` names the vintage the BLOCK was taken
  from, `UPDATE_ROLE['merged']`'s own compare at `:2996-3005` is its reader, and S9 has no
  whole-file gov blob to assert against — so this is an exemption by ROLE, the one place this
  preamble is not scoped by field presence, and it is stated here rather than left to fall through
  the exactly-one branch. A row carrying exactly ONE of the two is its own REFUSAL. That pairing is
  the corruption shape this unit exists to catch, because `-11` rewrites `path`, `source`, `commit`
  and `gov_oid` together on a rename and a text merge of `install.json` is what splits them. **The
  ordering is fixed, and the two preconditions are sequential rather than competing.** S9 runs first,
  in the preamble, over every row. `-13` S7's skip runs later, inside the classification loop, after
  `how` resolves at `:2974` and before `classify_row` at `:3014`. S9 therefore cannot lean on that
  skip having already happened, which is exactly why it is scoped by field presence and not by
  `evidence`. The `merged` arm above is the one exception, and reading `role` there rather than
  `evidence` is deliberate: `role` is on every row `apply` and `adopt` write, so the arm needs no
  later precondition to have run, while `evidence` is `-13`'s field and is exactly what the in-loop
  skip keys on. That narrowing is §8 F4's ruling, not a softening of the scoping rule.
  Two refusal branches, each carrying its own `refusal_join.py` arm, under that file's contract that
  every refusal branch is reached by an arm asserting it.

## 3. Non-goals (OUT)

- **Not** the `carry` rungs. The `verbatim` / `eol` / `relocate` ladder and its needle map are
  `-9`'s. This unit makes the two identities readable and leaves any difference a plain local delta.
- **Not** changing what the merge branch stamps. `:3097-3098` keeps writing the merge result into
  BOTH identities under this unit, so the corruption is renamed rather than fixed. That is
  deliberate: `-8` owns the fix, and `-8`'s red-first observation must survive this unit landing.
- **Not** dropping `sha256`. It is read by `cmd_check`'s sidecar join (`:1544-1556`) and it is what
  `install.sums` carries, so removing it is a migration nobody asked for.
- **Not** normalizing, renormalizing or re-pinning the target's `.gitattributes`. A target whose
  pins are wrong is `-2`'s `pins` disposition and the operator's decision, and `lf_pins` (`:1805`)
  is untouched here.
- **Not** repairing the exec bit on rows `apply` already landed. This unit needs a mode to call
  `update-index` at all; it does not claim to fix what earlier installs wrote.
- **Land-alone:** no, and `-2` lands first. The dependency is stated here rather than defended by a
  fixture no acceptance criterion touches. Acceptance runs on TWO fixtures and both need it:
  `memory-tree` for AC1–AC6 and `push-main` for AC11. Each kit's `[[lf_pin]]` blocks become plan
  rows at `:1420-1424` — `cmd_plan`'s per-pattern `kind: "order"` rows, which never reach a
  receipt — and `cmd_apply` collapses them into ONE `role:"attributes"` receipt row at `:2350`,
  carrying every pattern in its `patterns` list. `UPDATE_ROLE["attributes"]` is `"refuse"` at
  `:2864`, so that single row takes `r.fail` + `continue` at `:3009-3012` — one is enough, and
  `if r.problems:` at `:3115` returns at `:3123` — before `receipt["schema"] = RECEIPT_SCHEMA` at
  `:3125`. AC5 therefore cannot read `"schema": 3` on that fixture until `-2` teaches `update` how
  to move an `attributes` row. AC11's exit-0 claim depends on the same landing.

## 4. Design

### Data model

| field | means | written by | read by |
|---|---|---|---|
| `gov_oid` | the blob gov shipped at this row's `commit`, STORED | `apply`, `update` | the OURS axis, and `check`'s provenance loop |
| `oid` | the blob the target's index held when the row was last written | `apply`, `update` | `check`'s integrity loop |
| `sha256` | sha256 of the bytes the row's destination holds in the TARGET at the moment the row is written — identical to gov's blob at `commit` for a `verbatim` row, the CARRIED bytes for an `eol`/`relocate` row (`-13` §8 F5), the merge result after `-8` | `apply`, `update` | `install.sums` and its join, and no verdict |

The live delta predicate reads the target's CURRENT index blob and compares it to the STORED
`gov_oid`. Both fields are stored and only the comparison is live: `gov_oid` is never recomputed at
read time, it is ASSERTED instead, on every row that carries it, by S9's preamble refusal, which is
what a stored field costs. The stored `oid` is that same quantity as of the last write, which is how
`check` sees a change nobody recorded. Two questions, two fields, and neither field answering both is
the whole unit.

Feeding the predicate into the grid's OURS axis is what keeps `VERDICT_GRID` (`:2843`) untouched.
Identities that agree give `equal`, which is the only axis value the raw-write verdicts sit on.
Identities that differ give `differs`, which reaches only `patched` and `diverged`.

S9's scoping is measured rather than assumed. On inCMS at `9ddcc5c9`, `.governance/install.index`
holds 92 rows, and 54 of them carry a blob absent from gov's object database. Excluding its 13
`project-owned` rows leaves 41 gov-authored rows that no verbatim walk attributes: 25 are `engine`
rows and 16 are the declared divergences `.governance/kits.json` documents, each with a `record` id.
Two of the 25 are `scripts/unattended/fixture-records/scripts~unattended~fixture-pieces~one~piece.md.md`
and its `~two~` sibling, which `.governance/kits.json` declares `engine` rather than diverged, so
they are the unattributed state rather than a declared fork. Whatever the `eol` and `relocate` rungs
recover, the residue reaches `update` carrying no `commit` and no `gov_oid`. An assertion demanding
both fields of EVERY row refuses on every one of them before a single row is classified, and no
update ever runs on that adopter. That is the composition this scoping exists to keep working.

### Alternatives rejected

- *Normalize line endings before hashing.* A rewrite rule with no proof behind it, forbidden by the
  build's cut list, and it would silently mask a real edit that differs only in whitespace.
- *Pin every installed path to `eol=lf` in the target.* That is gov's deployer dictating a repo-wide
  attributes policy in a repository gov does not own, and it fails outright for an adopter who
  declines the pin.
- *Store a `locally_modified` boolean.* A stored boolean about a comparison goes stale the moment
  either side moves; an operator who reverts an edit leaves it set forever.
- *Keep the worktree read and widen the tolerance.* A comparator that accepts two spellings of one
  file accepts them for a genuinely edited file too.

### Files touched (estimate)

`tools/govkit/govkit.py` (~90 lines), `tools/govkit/selftest.py` (~12 arms), and THREE anchors in
`tools/govkit/refusal_join.py`'s enumerated set: one for S4, and two for S9. That file keys an anchor
on a refusal CALL SITE, and S9's two arms are two sites. The mismatch and the half-populated pair
carry different messages and cannot share one. S9's `merged` exemption adds no fourth anchor: it
removes a row class from a refusal rather than adding a branch, so it is armed by AC11's negative
assertion beside the exactly-one anchor.

## 5. Production-readiness checklist

- security — S4 closes a real overwrite. Reading the index without it classifies a path with no
  index entry as `absent`, which the write loop turns into a raw write over an untracked local file.
- perf / scale — one batched `ls-files -s` per run replaces one worktree read per row, which is
  strictly fewer syscalls on any receipt holding more than one file.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a target with no index entry for a claimed path refuses by name.
  A `checkout-index` that fails reports and leaves the index entry rather than half-writing, with
  the rollback itself left to `-14`. A row carrying neither identity field is not an error state on
  this unit at all: S9 passes over it because there is nothing to compare, and what happens to it
  next is its ROLE's business in the classification loop — `skip`, `adopter`, `block` or `-10`'s
  `report`, each dispatching normally. It is NOT the same population as `-13` S7's skip, which is
  keyed solely on `evidence: "unattributed"` and scoped to the `table` disposition; S7 says in
  terms that field-absence is not an equivalent form of that predicate.
- observability — the printed table keeps its shape and its vocabulary. The header line at `:2967`
  moves from `receipt schema 2` to `receipt schema 3`, which is how an operator sees the migration.
- risks — the residual risk is a target whose index is stale against its worktree, where this unit
  reports a file as gov's while the operator's editor shows otherwise. Stated rather than solved:
  `-12`'s dirty-path precondition refuses that exact state before any write, and `-12` lands ahead.
  The second risk is the stored half of `gov_oid`, and it is the whole reason S9 exists.
  `install.json` is a committed file, and `-11` rewrites `path`, `source`, `commit` and `gov_oid`
  together on a rename, so a text merge can pair `commit` from one side with `gov_oid` from the
  other. A stale `gov_oid` that happens to equal the target's live index blob reads the delta
  predicate FALSE and opens the raw-write arm on a row carrying a local edit — the destruction `-8`
  exists to close, reached from the receipt instead of from the merge. S9's per-row assertion is the
  only thing standing between a text-merged receipt and that write.
- testing + left-shift gates — the class is "a receipt field asked to be two things at once", and
  AC6 gates it behaviourally by corrupting every `sha256` and asserting no verdict moves.
- migration / rollback — a schema-2 receipt upgrades in place on the first `update`, with both
  identities computed from evidence rather than carried over from `sha256`, and `gov_oid` STORED
  from that one computation rather than re-derived on any later run. A schema-3 receipt read by an
  older govkit is benign: it ignores unknown keys and still finds `sha256`.
- user docs — `WIRE-INTO-PROJECT.md`'s receipt section gains the two-identity paragraph and the
  schema-3 note.

## 6. Acceptance criteria

- **AC1** — A fixture installed by `govkit.py apply --kits memory-tree` and then cloned with
  `git clone -c core.autocrlf=true` reports the same tally as the uncloned original, `current 24 ·
  missing 3`, with zero `patched`. Observe RED first: measured 2026-08-24 at `9ddcc5c9`, that clone
  reports `current 1 · missing 3 · patched 23`.
- **AC2** — Both arms of the index read, because a fix that reads neither side is indistinguishable
  from one that reads the wrong side. With a claimed path edited in the clone's worktree and NOT
  staged, its row still reads `current`; after `git add` of that same edit, it reads `patched`.
- **AC3** — With a claimed path dropped from the index by `git rm --cached` and left on disk
  untracked, `update --write` refuses, names the path, and leaves the file's bytes unchanged. This
  arm is not red at `9ddcc5c9`: it guards a hazard S2 itself introduces, so its failing case is
  observed by staging S2 without S4, watching the overwrite, and then unstaging it.
- **AC4** — On the autocrlf clone, `update --write` of a genuinely stale row leaves the index blob
  byte-identical to `git -C <gov> rev-parse <to>:<source>`, and leaves the worktree file carrying
  the line endings that target's own filters produce. Observe RED first: `dp.write_bytes` at
  `:3071` lands LF, which is not what those filters produce for that path.
- **AC5** — After a `--write` run that ends with no findings — which on the `memory-tree` fixture
  means after `-2` lands, per §3 — `install.json` reads `"schema": 3` and every engine row carries
  `gov_oid`, `oid` and `sha256`. A hand-built schema-1 fixture and a schema-2 fixture both still
  classify without refusal, and the schema-1 role-distrust arm still fires on the schema-1 fixture.
- **AC6** — The class gate. An arm rewrites every row's `sha256` to one constant and asserts the
  printed verdict lines are byte-identical to the run before it. Observe RED first: at `9ddcc5c9`
  that corruption turns every row `patched`.
- **AC7** — `python tools/govkit/govkit.py selfcheck` exits 0, and `python
  tools/govkit/refusal_join.py` accounts for all THREE new refusal branches, with an arm that reaches
  each. They are S4's absent index entry, S9's `gov_oid` mismatch, and S9's half-populated pair.
- **AC8** — Hand-edit one row's `gov_oid` in a fixture receipt to any other valid blob oid and run
  `update`. It refuses by name, names the path, writes nothing, and leaves the receipt
  byte-identical. Observe RED first by staging S1 through S8 without S9: the same edited row is
  classified against the wrong identity and the run walks on to its write arm.
- **AC9** — The composition arm, which is what `-7` and `-13` landing together must not break. A
  fixture receipt carries one row with NEITHER `commit` nor `gov_oid`, written by `adopt` as a
  `forked` destination at `evidence: "unattributed"`, beside one genuinely stale `engine` row that
  carries both. `update --write` then runs to completion: the stale row's bytes move, the field-less
  row is printed BY NAME and written in neither direction, no refusal fires, and the run exits **0**. Observe RED first by
  staging S9 unscoped over every row, at which point the preamble refuses on the field-less row and
  the stale row never moves.
- **AC10** — The half-populated pair still refuses. A fixture row whose `role` is `engine` — any
  role S9's `merged` exemption does not cover — carrying `commit` and no `gov_oid` refuses by
  name, writes nothing, and leaves the receipt byte-identical. The mirrored row carrying `gov_oid`
  and no `commit` refuses the same way. Both arms run in the same fixture as AC9, because the
  scoping AC9 asserts must never be built as a blanket pass for any row missing a field. AC11 owns
  role `merged`, which is exempt by ROLE and does not refuse on this same field shape; the two
  criteria partition the population and neither generalizes to the other's half.
- **AC11** — The `merged` exemption is OBSERVED rather than assumed. A fixture target takes
  `python tools/govkit/govkit.py apply --kits push-main`, whose `.githooks/pre-commit` rule is
  `role = "merged"` at `marker_style = "hash-comment"` and therefore lands the `:2417` row shape,
  and a following `update` runs to completion: the merged row reaches `UPDATE_ROLE["merged"]`'s
  compare at `:2996-3005`, S9's preamble refuses nothing, and the run exits **0**. Observe RED
  first by staging S9 without its `merged` arm, at which point that row carries `commit` and no
  `gov_oid`, trips the exactly-one branch, and the whole run refuses before any row is classified.
  `python tools/govkit/refusal_join.py` still accounts for THREE branches: this arm asserts that a
  refusal is NOT reached and adds no anchor.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest`, `govkit selfcheck`
and `refusal_join` legs. Adds arms and three refusal anchors; adds no new leg.

## 8. Open questions

- **F1 — the mode for `update-index --cacheinfo` on a row with no existing index entry.** Gov's
  tree entry mode at `commit`, or a literal `100644`? Gov's tree entry: a hook that lands
  non-executable is a hook that does not run, and `-1` is about to make `.githooks/pre-push` a
  reachable destination.
  RESOLVED (agent, 2026-08-24, delegated): gov's tree entry mode, under the full-scope approval.
- **F2 — one batched `ls-files -s`, or one per row?** Batched over the receipt's path list, read
  into a dict before the classification loop. A per-row spawn is one process per file on a receipt
  that already knows every path it will ask about.
  RESOLVED (agent, 2026-08-24, delegated): batched.
- **F3 — retain `sha256` at schema 3, or drop it?** Retain. Dropping it breaks `install.sums` and
  the join that asserts the sidecar against the receipt, which is the artifact a target verifies
  with bash alone.
  RESOLVED (agent, 2026-08-24, delegated): retain.
- **F4 — does the `merged` row carry both identities, or is it exempt from S9 by ROLE?** The row
  `apply` writes at `:2417` carries `commit` and neither identity, which is S9's own exactly-one
  refusal shape, so the first `update` against any target that ever ran `apply` with a hash-comment
  merged rule would refuse everything the moment this unit lands. Two kits in gov reach that row
  today, `push-main` and `pytest-parallel-guardrails`. Either the row gains both identities or the
  preamble exempts the role.
  RESOLVED (agent, 2026-08-25, delegated): exempt by ROLE — S1's third channel and S9's fourth
  arm. The reasoning is not restated here; it is in
  `memory/builds/dCarriedReceipt/reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round5.md`,
  under "The fork B1 raises, and how it was resolved".

## 9. Revision log

- rev-8 · 2026-08-26 · node a · owner ruling: S4's shadow refusal is SCOPED to rows the update
  dispatch sends to the `table` disposition, which is the hazard the scope item's own text names.
  Closes the unqualified-by-role refusal this unit parked at build time.

- rev-7 · 2026-08-25 · round-6 fold: M1, M2, M3, L1, L2 and L3. M1 — S1 enumerated THREE of
  `cmd_apply`'s four row producers and now names all four, the `attributes` row at `:2350`
  included; the set was re-derived from the tree rather than copied, and the four are `:2350`,
  `:2417`, `:2440` and the `writes` channel whose one row shape at `:2458-2460` appends at both
  `:2466` and `:2471`. S9's neither-arm gloss carries the `:2350` row too. M2 — S7 said
  `cmd_apply` records both identities unqualified, which read over all four producers and broke
  `-13` S11's inheritance argument; it is scoped to the `writes` channel's rows, and the `git add`
  citation is corrected to `:2477-2478`, the single stage over every channel's paths. M3 — §3's
  land-alone paragraph named one fixture where acceptance uses two, read the per-pattern PLAN rows
  at `:1420-1424` as receipt rows, and typed a pin count in prose; it now separates the plan rows
  from the ONE `attributes` receipt row at `:2350`, states no count, and records AC11's dependency
  on `-2`. L1 — AC10's fixture row named no role, so it asserted the opposite outcome to AC11 for
  the same field shape; it is scoped to `engine` and partitioned against AC11, the same fix rev-6
  made in `-13` AC6. L2 — §5 told a builder that `-13` S7 skips any row missing both identity
  fields, which is the field-absence reading S7 exists to refuse. L3 — S1 credited `-8` with
  keeping `block_sha256`; `-8` never mentions the field, and the owners are `cmd_apply` at
  `:2417-2422` and `-13` S11.
- rev-6 · 2026-08-25 · round-5 fold: B1, resolved to Direction A and recorded as §8 F4. S1
  names the THIRD channel M4's two-channel enumeration left out — the `merged` row at `:2417`,
  which carries `source` and `commit` and neither identity — and S9 gains a fourth item, an
  exemption by ROLE for that row, placed immediately before the exactly-one refusal it would
  otherwise trip. M6's conclusion is narrowed to the `:2440` rows plus that arm, since a merged row
  has both `source` and `commit` and so is not passed over for want of an operand. S9's own "not
  by `role` or by `evidence`" sentence is NARROWED rather than left standing beside its exception,
  and says why the exemption reads `role`. AC11 observes the exemption over a `push-main` fixture,
  so the arm is run rather than assumed, and §4 records that it adds no fourth refusal anchor.
  H2 moves `sha256`'s definition onto the TARGET's bytes at write time, which is `-13` §8 F5's
  ratified reading, so one stored field stops carrying two live definitions.
- rev-5 · 2026-08-25 · round-4 fold: M4 scopes S1's quantifier to the `writes` channel at
  `:2443-2460` and says plainly that an `unlanded` row at `:2440` carries neither identity, so S1
  and S9 stop contradicting each other. M6 replaces S9's three-role gloss: `UNLANDED_REASON`
  (`:236`) carries a fourth key, `merged`, `-10` S3 adds `forked`, and `apply` reaches three only by
  skipping merged entries at `:2428-2429`. H1 moves S9's ordering sentence onto the scoped reading —
  `-13` S7's skip runs after `how` resolves at `:2974` and before `classify_row` at `:3014`, not
  ahead of `:2974`. M1 states in S4 that its predicate is evaluated in the PREAMBLE, which is the
  ordering `-12` §4's table now carries as step 5.
- rev-4 · 2026-08-25 · round-5 fold: S4's predicate was unsatisfiable as written — `tracked()` at
  `:111-112` IS `git ls-files`, so tracked-and-not-indexed is empty but for an unmerged path,
  which `-12` S3 refuses first. Restated as present-in-worktree/absent-from-index, and §10's false
  `tracked` seam claim removed. S9 no longer calls a field-absent row `-13` S7's state: every
  `unlanded` row at `:2440` carries neither field too.
- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass (5 lenses + fold). Every cited
  line was opened at `9ddcc5c9`. Three brief citations were off by a little and are corrected here:
  the OURS comparison is `:2889` and not `:2886`, the merge stamp is `:3098` and not `:3096`, and
  `Report` is `:565` while `Refusal` is `:78`, rather than the two together at `:566`. The
  23-patched measurement was reproduced end to end rather than taken on trust, and its complement
  was measured beside it: the same target uncloned reports `current 24 · missing 3`. One brief claim
  is narrowed. inCMS is immune through `core.autocrlf=false`, but NicoCares is immune for a
  different reason — a repo-wide `* text=auto eol=lf` baseline in its own `.gitattributes` — despite
  carrying `core.autocrlf=true` locally. Neither live target reproduces the defect, so the red-first
  observation runs on a constructed fixture and this spec says so rather than implying a live red.
- rev-2 · 2026-08-24 · folded the pre-code review: `gov_oid` is STORED and read by the OURS axis
  (owner decision, B2), S9 adds the per-row integrity refusal beside `:2946` with its
  `refusal_join.py` arm, AC7 now covers both refusal branches and AC8 observes the new one, and §5
  risks states once why a stored field needs that assertion. B5 is resolved the second way: the
  land-alone claim is dropped and `-2` is named as the dependency in §3, because AC1's red-first
  measurement is the `memory-tree` fixture's own and moving every criterion onto `check-wiring`
  would discard measured evidence in order to keep a claim. The `lf_pin` figure is corrected to 22
  patterns across 11 of the 25 registry entries — re-measured here — and the conclusion it served,
  that only one of the 24 memory-tree engine rows falls under a pin, is unchanged.
- rev-3 · 2026-08-24 · round-2 fold: S9's integrity assertion is SCOPED by field presence, so a row
  carrying neither `commit` nor `gov_oid` is passed over as `-13` S7's unattributed state while a row
  carrying exactly one of them still refuses, and S9 now states its ordering against that in-loop
  precondition so the two cannot be read as competing. AC9 and AC10 are added for the two halves of
  that scoping, and §5's error-states line says the same thing once. The refusal-anchor count is
  re-counted to THREE, and §4, §7 and AC7 are made to agree. §7 had said one, which is the direction
  that ships an unarmed branch. The §4 measurement is the corrected one. The round-2 brief said 19
  inCMS engine rows match no gov commit and that the two `piece.md.md` fixture records are the
  declared forked case; measured here it is 25 engine rows, and `.governance/kits.json` declares
  those two records `engine` rather than diverged, so they are the unattributed case while the 16
  documented divergences are the forked one. The figures now agree with `-13` §4's inventory,
  because both come off the same instrument.

## 10. Reuse audit

Wires through seams that already exist rather than adding any. `blob_at` (`:2148`) keeps answering
"what did gov ship", and its docstring already states the index-side rule this unit extends to the
target side; S9's per-row assertion calls that same function rather than adding a second reader of
gov's trees. The batched index read joins the `ls-files` form already spelled at `:112` (`tracked`),
`:1790`, `:2642` and `:2673` rather than adding a fourth spelling, and `tracked` itself is the seam
as the population reader it already is; S4's predicate is worktree-versus-index and needs no
distinction this function does not draw. `VERDICT_GRID` (`:2843`), `UPDATE_ROLE`
(`:2857`) and the `classify_row` (`:2874`) and `three_way` (`:2897`) pair are untouched in shape;
only which identity the OURS axis reads changes. Refusals reuse `Refusal` (`:78`) and `Report`
(`:565`) and are counted by the existing `refusal_join.py` contract rather than a new counter.
`resolve_entry` (`:270`), `target_context` (`:535`), `resolve_tokens` (`:516`), `load_deploy`
(`:553`) and `planned_writes` (`:1359`) are deliberately untouched: this unit changes what a row's
fields MEAN, never how a destination is resolved. `cmd_check`'s per-kit `[check].argv` runner
(`:1632-1652`) is untouched for the same reason — it measures adoption, not identity.
