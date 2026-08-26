# DEPL-dCarriedReceipt-9 — `carry` rungs, recomputed, over a derived needle map

**Status:** CLOSED · rev-10 · 2026-08-26 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-build-DEPL-dCarriedReceipt-9-acceptance-ledger.md](../build/2026-08-25-build-DEPL-dCarriedReceipt-9-acceptance-ledger.md) | journal | — |
| [2026-08-24-review-DEPL-dCarriedReceipt-9-spec-precode.md](../reviews/2026-08-24-review-DEPL-dCarriedReceipt-9-spec-precode.md) | spec-audit | DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 |
| [2026-08-25-review-DEPL-dCarriedReceipt-9-round4.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round4.md) | spec-audit | DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 |
| [2026-08-25-review-DEPL-dCarriedReceipt-9-round5.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round5.md) | spec-audit | DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 |
| [2026-08-25-review-DEPL-dCarriedReceipt-9-round6.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round6.md) | spec-audit | DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 |

<!-- /gen:spec-records -->

## 1. Goal

After `-7` a receipt row carries two identities, `gov_oid` and `oid`, and `oid != gov_oid` is the
local-delta predicate. On its own that predicate is too blunt to install anything. An adopter at a
non-default `prefix` differs from gov on every file that spells a path, so those rows read as local
deltas forever: the raw-write arm is closed to every one of them, and each is handed to a three-way
whose `base` still spells gov's prefix where the target's own copy does not, so gov's change reaches
only the hunks whose context does not name the path. That is the state both live targets are in.
Measured on inCMS at `2cff5855` against each row's own recorded gov commit: of the 52 rows whose
commit resolves, 21 are byte-identical, 6 differ only in line endings, and 5 differ only by the
prefix relocation. Eleven rows carry no local edit at all and the blunt predicate calls every one a
local delta.
This unit explains the difference with a per-row `carry` rung — `verbatim`, `eol` or `relocate` —
recomputed by proof on every run and never read back from the receipt. A proven rung does not open
the raw-write arm. It corrects what the three-way is handed, so such a row RECONCILES automatically
to the carried bytes with no operator turn (S9), and what the row is stamped with afterwards is S12.

## 2. Scope (IN)

- **S1** — `classify_row` (`govkit.py:2874`) computes `carry` before it computes a verdict, over
  three rungs tried in order, cheapest first: `verbatim` (ours == base), `eol` (equal after CRLF to
  LF applied to both sides), `relocate` (ours == relocate(base, alpha)). The first that proves itself
  wins; none proving itself means there is a local delta.
- **S2** — `carry` is RECOMPUTED on every run and never trusted from the receipt. It is written into
  the row for reporting, and the reader is the print loop only. No branch in either verb may read a
  stored `carry`, which is asserted by an arm rather than left to discipline.
- **S3** — `alpha` is DERIVED, never authored, and the derivation takes a SEQUENCE OF PAIRS
  rather than a receipt, because it has two callers. `cmd_update` feeds it the receipt: each row
  contributes one pair, `(dirname(source), dirname(path))`. `adopt` feeds it the planned
  `(src, dest)` pairs of its own run, lifted the same way — `-13` S4a, and §8 F3 records
  why that is not a re-opening of the fork. The pairs are deduplicated; any gov directory that
  yields two DIFFERENT target directories is DROPPED and reported by name. There is no override
  key and no AUTHORED descriptor field: a hand-written map is a second answer to a question the
  caller's own pairs already answer.
- **S4** — needles emit in both the `/` form and the `~` form, because gov flattens paths into
  fixture filenames. Substitution is a single left-to-right pass, longest needle first, and the
  output is never rescanned, so one substitution can never feed another.
- **S5** — WHOLE-FILE equality decides a rung. One residual byte and the rung does not match, the
  row keeps exactly the verdict it has today, and nothing is written.
- **S6** — for a row that DID match a rung and later diverges, the rung is applied to BOTH `base`
  and `theirs` before `three_way` (`:2897`), so the substitution cancels in the base-to-theirs diff
  and `git merge-file` sees only gov's semantic change.
- **S7** — the run prints one line per dropped ambiguous gov directory and one line naming the pair
  count and the needle count, so a map that silently collapsed is visible rather than inferred.
- **S8** — `selftest.py` arms: one per rung, one for the ambiguity drop, one for the `~` form, one
  for the no-rescan property, one asserting the three-way sees only the semantic change, one
  asserting a stored `carry` in a fixture receipt is ignored, one over a reconciled `relocate` row's
  resulting INDEX blob (AC8), one over a DELETED `relocate` row's restore (AC9) and one over the ROW
  that restore leaves behind (AC10) — ten arms.
- **S9** — a proven rung sets `carry` and does NOT change `o_state`. The ours-vs-receipt comparison
  (`:2889`) is untouched, the verdict still comes from the UNCHANGED `VERDICT_GRID` (`:2843-2853`),
  and no rung may move a row into the raw-write arm at `:3069-3071`. A rung row that diverges lands
  on `diverged` and RECONCILES through the three-way per S6: the rung is applied to `base` and
  `theirs`, it cancels in the base-to-theirs diff, and `git merge-file` sees only gov's semantic
  change. Reconciliation to the CARRIED bytes is the outcome; a raw write of gov's un-carried bytes
  is not, so a stale rung can never revert a target's spelling. The reconciled row is stamped per
  S12.
- **S10** — reporting. A rung row whose gov copy did NOT move classifies `("differs","equal")` =
  `"patched"` (`:2847`), which is a LIE for a `relocate` row: the target edited nothing. The verdict
  print (`:3024`) labels such a row `carried (relocate)`, sourced from `carry` and from nothing else,
  and the tally counts it under the label it printed.
- **S11** — the `missing` restore arm carries too. `classify_row` returns `o_state = "absent"`
  (`:2887-2888`), both `("absent", …)` cells are `"missing"` (`:2850-2851`), and `missing` shares the
  raw arm at `:3069-3071` — so a rung-carrying row the target DELETED would be restored with gov's
  un-carried bytes, because there are no `ours` bytes to prove a rung against. The restore derives
  `relocate` from the row's OWN `(dirname(source), dirname(path))` pair, which needs no bytes and is
  exactly S3's derivation, applies THAT ONE pair's needles rather than the whole map, and writes the
  carried form. The restored row is stamped per S12, and NOT with the stamp `-8` gives the rest of
  that arm — gov's blob into BOTH identities — which over carried bytes would leave the receipt
  claiming the target holds gov's copy while it holds the target's own spelling.
- **S12** — ONE stamping rule, covering both arms of this unit that write bytes gov does not hold:
  S9's reconcile and S11's restore. `oid` records the blob ACTUALLY WRITTEN — the merged bytes on
  S9's arm, the carried form on S11's — and `gov_oid` keeps the meaning `-8` gives it, gov's blob at
  the row's `commit`, which either write advances to `to_commit`. So `oid != gov_oid` holds
  afterwards, and it reads "this row carries a rung": the state a `relocate` row is in after any
  normal reconcile, and NOT a local delta, because `carry` is re-proved on the next run (S2) and
  re-explains the difference. This NARROWS one cell of `-8`'s write table rather than contradicting
  it. That table's raw arm puts gov's blob into both identities for `stale` and `missing` alike, and
  a `missing` row this unit restores in the carried form is the one row on that arm whose written
  bytes are not gov's. Taking the un-narrowed stamp is the corrupt pairing: two identities recorded
  EQUAL over bytes gov never shipped, which the next run reads as a clean gov-owned row and
  raw-overwrites back to gov's prefix.
- **S13 — BUILT at rev-10, on node `a`, by owner ruling 2026-08-26.** It asks for a committed
  receipt of the 52 rows measured at inCMS `2cff5855`, generated once by a script recorded beside
  it, so AC1's and AC2's counts are re-runnable without either live target. That is what now ships:
  `tools/govkit/fixtures/incms-2cff5855.receipt.json` (52 rows, 30 KiB) and its generator
  `tools/govkit/fixtures/make_incms_receipt.py`.

  **It was DEFERRED at rev-9 and the reason was real** — the unit was built on node `d`, where the
  inCMS checkout is not reachable, so no run there could generate it. Node `a` has both live adopter
  checkouts and the pinned revision resolves, which is the precondition the rev-9 park named.

  **inCMS carries no govkit receipt, so the fixture is RECONSTRUCTED.** At `2cff5855` its
  `.governance/` holds a GENERATED `install.index` written by its own `check_kit_sync.py` — the same
  evidence in a different shape, under a different owner. Each row's gov SOURCE is resolved through
  gov's own `registry.toml` at the recorded commit rather than by a basename guess; the first cut
  used the guess and left 13 of 54 rows unresolved, because five kits do not live at `tools/<kit>/`.
  Measured: 92 index rows, 38 carrying `unverified`, 54 with a resolvable commit, and exactly **52**
  of those also resolving a gov source. S13's own figure, arrived at independently.

  **The fixture stores identities, never answers.** `verbatim` and `relocate` are proved by
  transforming gov's bytes and comparing the resulting blob oid to the target's recorded `oid`.
  `eol` cannot be — the rung normalises BOTH sides and an oid cannot be un-hashed — so each row also
  carries `lf_oid`, one measurement of the target taken where inCMS was reachable, which the arm
  reproduces from gov's side. That is what keeps the fixture at 30 KiB instead of a 540 KiB pack of
  another project's source vendored into this repo, and it is not circular: the same function is
  applied to opposite inputs, which is exactly the equality the rung claims. Cross-checked at build
  time against inCMS's real object store — all 52 rows agree, zero disagreements.

## 3. Non-goals (OUT)

- **Not** a write-time transform, with ONE bounded exception. `alpha` is a PROOF instrument: it is
  applied to gov's bytes only to compare them, never to produce bytes that get landed on the strength
  of the map alone. That alternative was measured and is rejected in §4. The exception is S11's
  `missing` restore, where the target holds no bytes to prove anything against and the alternative is
  writing gov's prefix into a target that does not use it; it applies the row's own single pair,
  never the derived map.
- **Not** an authored, overridable or descriptor-declared map, and **not** a free-form rewrite rule
  or line-level partial application. All three sit on the build-wide cut list.
- **Not** rename detection. A row whose target path moved is `-11`, and this unit must not grow a
  second answer to it: `alpha` explains a difference in BYTES, never a difference in the row's path.
- **Not** composing rungs. `relocate` is proved on raw bytes, not on eol-normalised ones. See §8 F2.
- **Land-alone caveat:** this unit CANNOT land alone. It reads `gov_oid` and `oid`, which `-7`
  introduces, and it would re-open the integrity hole `-8` closes if a merged result could still
  overwrite `gov_oid`. It lands after both, in that order.

## 4. Design

### Data model

One new row field, `carry`, holding `verbatim`, `eol`, `relocate`, or absent. It is output, not
input. No other row field changes; the only other on-disk move is the schema stamp below, and a
schema-3 receipt written before this unit still READS identically here — every rung is recomputed
from the two identities the row already carries.

### Inventory

The derivation, measured over inCMS at `2cff5855` against gov `9ddcc5c9`, reconstructed from
`.governance/kits.json` plus `.governance/install.index` because neither target has a govkit receipt
yet:

| Quantity | Value |
|---|---|
| rows in the reconstructed population | 92 |
| rows whose gov source resolves | 86 |
| gov directories after the dirname lift | 15 |
| gov directories dropped as ambiguous | 2 — `tools/memory-recall` and `tools/workflows` |
| surviving directory pairs | 13 |
| needles emitted, 13 pairs in 2 forms | 26 |

Rung distribution over the 52 rows carrying a resolvable recorded gov commit:

| Rung | Rows |
|---|---|
| `verbatim` | 21 |
| `eol` | 6 |
| `relocate` | 5 |
| none, a local delta | 20 |

The five `relocate` rows are `scripts/unattended/adopt-unattended.sh`, `check-playbook.test.sh`,
`cross-component.test.sh`, `playbook.fixture.md` and `run-unattended-gates.sh`. All five prove on
RAW bytes, and zero of them need `eol` composed with `relocate`, which is what §8 F2 rests on.

`tools/memory-recall` being dropped is the derivation working, not failing. It maps to
`scripts/recall` for `query.py` and to `.claude/hooks` for `recall-opened.js`, so it names two
different destinations and cannot be a needle. `tools` survives as a single pair here only because
the dirname lift keeps `tools/hooks` to `.claude/hooks` separate from it.

### Alternatives rejected

- *Apply the map at WRITE time, rewriting gov's bytes through `alpha` and landing the result.*
  Measured and rejected. On `tools/unattended/adopt-unattended.test.sh` at `ce5dca99` it corrupts six
  lines: four occurrences of the fixture literal `bash tools/land.sh`, which the `tools` needle
  rewrites although it names no prefix at all, and lines 132-133, where the fixture builds a
  directory literally named `my tools/unattended` and the needle turns it into `my scripts`. Under
  the proof gate this row simply matches no rung and stays a local delta, and none of those six
  lines is ever written. The wider blast-radius figure this bullet used to carry — "27 rows green by
  identity, 17 flipped" — is WITHDRAWN as unsourced: the pre-code review could not reproduce it under
  eight populations and the fold could not under two more, and no population is named that would. The
  rejection does not need it. It rests on the six lines above, re-opened at `ce5dca99` while folding:
  the four `bash tools/land.sh` occurrences are lines 34, 63, 83 and 91, and the `my tools/unattended`
  construction is lines 132-133. A blast-radius count, if one is ever wanted, comes from the shipped
  derivation rather than from a reconstruction of it.
- *Lift each row to a directory pair by stripping EQUAL trailing segments.* Measured and rejected;
  it is also the form the design brief carries, and it is wrong. Stripping `unattended` as an equal
  segment collapses `tools/unattended` into the bare gov directory `tools`, which then collides with
  the hooks kit's `tools` and is dropped as ambiguous — taking the whole unattended kit's relocation
  with it. Measured on the same population: 5 gov directories, 3 surviving pairs, and zero
  `relocate` rows. The dirname lift yields 13 pairs and 5 rows.
- *Rescan the output, or substitute longest-match-anywhere rather than left-to-right.* Either lets
  one substitution feed another, so rewriting `tools` inside a path already rewritten to `scripts`
  becomes reachable and the transform stops being a function of its input.
- *Store `carry` and trust it.* A stored rung is a claim about bytes that have moved since. The whole
  point of the two identities is that no stored boolean stands between the tool and the blobs.

### Migration

**The schema number does not move for this unit.** `-7` S6 performs the one bump this build takes,
2 to 3, and `-13` §4 Migration defines schema 3 as the generation carrying every field this build
adds — `gov_oid`, `oid`, `carry` and `evidence` — so no later unit mints a second number. The
constant's own comment at `:39` reads "bumped by any unit that adds a per-**role** row field";
`carry` adds no role, and a build that bumped once per contributing unit would ship three numbers for
one generation, which is the drift the single-owner rule exists to prevent.

There is no migration CONTENT either: `carry` is derived output, recomputed on the first run whatever
the row holds, so a schema-3 receipt written before this unit lands reads identically after it.

### Files touched (estimate)

`tools/govkit/govkit.py` (~90 lines: the derivation, the substituter, the rung ladder inside
`classify_row`, S10's label, S11's restore arm, S12's stamp on both carried arms, the two report
lines), `tools/govkit/selftest.py` (10 arms), and TWO fixtures. The first is a hand-built receipt
carrying a non-default prefix, a deliberately ambiguous gov directory, a `relocate` row whose gov
copy moved, and a `relocate` row the target deleted. The second is S13's committed inCMS-derived
receipt of the 52 resolvable rows, checked in beside the script that generated it.

## 5. Production-readiness checklist

- security — the rung ladder does NOT widen the automatic-write arm, and that is the point. A proven
  rung sets `carry` only; `o_state`, the verdict grid and the raw arm at `:3069-3071` are untouched
  (S9). What a rung buys is the MERGE path: with the rung applied to `base` and `theirs` (S6),
  `git merge-file` applies gov's change cleanly, emits the carried spelling, and costs the operator
  no turn — zero conflicts rather than a new class of raw write. S5 still bounds it: a rung is proved
  on WHOLE-FILE equality against bytes gov holds, and a row that proves no rung keeps exactly the
  verdict it has today. S11's restore is the ONE arm that writes carried bytes without a bytes-proof,
  and it fires only where the target holds no bytes at all.
- perf / scale — one extra whole-file comparison per non-identical row, and at most one substitution
  pass per such row. The measured population is 92 rows, and the blob reads that dominate the run
  already happen. No new subprocess.
- a11y — N/A: CLI.
- i18n — N/A. The substituter operates on bytes decoded as UTF-8 and returns its input unchanged on a
  decode failure, so a binary row is never mangled into a false rung; asserted by AC6.
- error / empty / loading states — a receipt whose rows yield NO surviving pair produces an empty
  `alpha`, which makes `relocate` degenerate to `verbatim` rather than raising. A row with no
  `source` contributes no pair and is skipped, not refused.
- observability — S7's two lines. A dropped gov directory is printed by name with both destinations,
  because a silently collapsed map is indistinguishable from a target that genuinely relocated
  nothing, and that is the failure mode that would waste the most time.
- risks — the residual risk is a FALSE rung: two files that happen to be equal after substitution
  while the target genuinely edited one of them. That requires the edit to be exactly the
  substitution, in which case the bytes are gov's answer anyway. The larger risk runs the other way
  and is accepted by design: a row like `adopt-unattended.test.sh` will never take an automatic
  write, and that is the correct outcome rather than a gap. S11's restore carries a residual of its
  own: a literal inside a restored file that happens to spell the row's own directory pair is
  rewritten with it. That is accepted because the alternative on that arm is writing gov's prefix
  into a target that does not use it, and the arm fires only on a file the target deleted.
- testing + left-shift gates — ten `selftest.py` arms (S8). The classes left-shifted are "a
  substitution that chains", "a map with an ambiguous key", "a rung row reverted to gov's spelling by
  the raw arm", "a deleted carried row restored un-carried" and "carried bytes stamped as though gov
  wrote them", all gated directly rather than through the row that exposed them.
- migration / rollback — the schema stamp does not move for this unit; `-7` S6 owns the build's only
  bump and schema 3 already names `carry`. A rollback that drops the field therefore leaves a
  schema-3 receipt every reader still accepts.
  Otherwise a pure addition: the field is derived, and dropping it returns every row to the `-7` and
  `-8` behaviour with no other on-disk change.
- user docs — `WIRE-INTO-PROJECT.md` gains one paragraph beside the update step naming the three
  rungs and stating that a row with no rung is never written automatically.

## 6. Acceptance criteria

- **AC1** — Over S13's committed fixture receipt, built from the 52 rows of inCMS at `2cff5855`
  whose recorded gov commit resolves against gov `9ddcc5c9`, `classify_row` reports `verbatim` on
  21, `eol` on 6 and `relocate` on 5. Observe RED first: at `9ddcc5c9` the returned dict has no
  `carry` key at all and all 31 non-identical rows classify with `o_state` as `differs` — 52
  resolvable rows less the 21 §4 records as `verbatim`, which is the same 6 + 5 + 20 that table
  sums.
- **AC2 — RESTATED at rev-10 against the 86-row population, as this criterion's own text
  instructed.** The derivation over the rows whose gov SOURCE resolves — 86 of inCMS's 92 at
  `2cff5855` — yields exactly `13` directory pairs and **`25`** needles, and DROPS
  `tools/memory-recall` and `tools/workflows` by name in the printed report.

  **Two populations, because they answer different questions**, and conflating them is why this
  criterion's figures never reproduced. AC1 grades the 52 rows whose recorded COMMIT resolves,
  because a rung is proved against gov's bytes AT that commit. The needle map needs no commit at all
  — it derives from `(source, destination)` pairs — so its population is the 86 whose SOURCE
  resolves. §4's Inventory measured over the 86; the criterion was written against the 52. Over the
  52 the derivation gives 14 pairs and 27 needles, and drops nothing.

  **`26` was wrong by exactly one, and this build derived why before it measured it.** Needles emit
  in a `/` form and a `~` form; for a gov directory carrying NO slash those two strings are the
  SAME, so such a pair contributes one needle rather than two. Exactly one of the 13 — `tools` —
  carries no slash, so `2×13 − 1 = 25`. The arm asserts that RELATION rather than the literal, which
  is also what `-13`'s AC12 was warned not to inherit.
- **AC3** — `scripts/unattended/adopt-unattended.test.sh` matches NO rung, keeps its current verdict,
  and its bytes are unchanged after a `govkit.py update --write` against the fixture, asserted with
  `git diff --exit-code` over that path. This is the `my tools` row; a build that "fixes" it has
  re-introduced the rejected write-time alternative.
- **AC4** — A needle map containing both `tools/unattended` and `tools` rewrites
  `tools/unattended/fixture-records/tools~a~b.md` to
  `scripts/unattended/fixture-records/scripts~a~b.md` in ONE pass, and rewrites a string already
  reading `scripts/unattended` not at all. The `~` arm is load-bearing at gov HEAD:
  `tools/unattended/check-playbook.test.sh` spells `tools~` at lines 365, 479, 523, 570 and 582 while
  inCMS's fixture records are named `scripts~unattended~fixture-pieces~one~piece.md.md`.
- **AC5** — For a row that matched `relocate` and then diverged, `three_way` is called with the rung
  applied to both `base` and `theirs`, and the merged output carries gov's semantic change with the
  target's spelling intact. Asserted on CONTENT and never on the exit code, per `three_way`'s own
  docstring.
- **AC6** — A fixture row whose blob is not valid UTF-8 returns unchanged from `relocate` and
  classifies exactly as it does at `9ddcc5c9`.
- **AC7** — A fixture receipt carrying a hand-written `"carry": "relocate"` on a row that provably
  matches no rung classifies as a local delta anyway, and `python tools/govkit/govkit.py update`
  never reads the stored value. After `--write` that receipt reads `"schema": 3` — this unit moves no
  schema number, `-7` S6 owns the build's only move — and a schema-1 and a schema-2 fixture both
  still classify without refusal.
- **AC8** — A fixture `relocate` row whose gov copy MOVED between the row's `commit` and `to_commit`
  RECONCILES rather than reverts: after `python tools/govkit/govkit.py update --write`, the blob the
  TARGET's index holds for that path — read with `git -C <target> rev-parse :<path>` — spells the
  target's `scripts/` prefix AND carries gov's new semantic line. Observe RED first: at `9ddcc5c9`
  that row takes the raw arm at `:3069-3071`, lands gov's `tools/` spelling verbatim, and exits 0.
- **AC9** — A fixture `relocate` row the target deleted AND COMMITTED classifies `missing` and is
  restored in the
  CARRIED form: the restored file spells `scripts/`, and its index blob is NOT gov's blob for that
  source. Observe RED first: at `9ddcc5c9` the same row is restored from `c["theirs"]` at `:3071`
  with gov's `tools/` spelling, because `o_state` is `absent` (`:2887-2888`) and there are no `ours`
  bytes to prove a rung against.
  The deletion is COMMITTED in the fixture on purpose: `-12` S4 refuses a run over a dirty claimed
  path, and a path absent from the index, the worktree AND HEAD falls outside that definition, so
  this cell stays reachable — a STAGED but uncommitted deletion is dirty by `-12` S4, refuses at its
  step 2, and this AC could never go red over one.
- **AC10** — the STAMP that restore leaves, over the AC9 fixture, asserting both halves together.
  After `python tools/govkit/govkit.py update --write` the restored file spells the target's
  `scripts/` prefix and spells gov's `tools/` nowhere, AND the row it left behind reads
  `"carry": "relocate"` with `oid` equal to `git -C <target> rev-parse :<path>` and `gov_oid` equal
  to gov's blob at the row's `commit`, so `oid != gov_oid` holds. The arm fails against a draft that
  writes the carried bytes and then takes `-8`'s raw-arm stamp: the two identities come back EQUAL
  over bytes gov never shipped, and the NEXT run reads that row as clean and raw-overwrites it back
  to `tools/`. Observe RED first: at `9ddcc5c9` there is no `carry` key at all and the single
  `sha256` field holds gov's own bytes.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest` and `govkit
selfcheck` legs. Adds ten arms and two fixtures; adds no new leg file. It adds NO refusal branch —
the ambiguity drop reports through `r.note` and a print rather than `r.fail` — so
`tools/govkit/refusal_join.py` and its `BRANCH_PIN` are unmoved. That constant is a shrink-only
FLOOR, so it is re-derived at landing rather than pinned to a literal here, and that pin
staying untouched in the diff is itself the assertion.

## 8. Open questions

- **F1 — should an ambiguous gov directory drop silently, drop loudly, or refuse the run?** Drop
  loudly. Refusing would make a perfectly installable target unupdatable over a map entry it never
  asked for, and a silent drop is indistinguishable from a target that relocated nothing, which is
  the exact confusion §5's observability line exists to prevent.
  RESOLVED (agent, 2026-08-24, delegated): drop and report by name, under the full-scope approval.
- **F2 — should the rungs compose, so a row may be `relocate` AND `eol` at once?** No: a ladder, not
  a lattice. Measured on the live target, all five `relocate` rows prove on raw bytes and zero need
  the composition, so composing today buys nothing and adds a fourth rung's worth of surface. The
  cost is stated rather than hidden: an adopter whose checkout is CRLF and whose prefix is also
  non-default falls to local delta on those rows and gets the three-way instead of a raw write.
  RESOLVED (agent, 2026-08-24, delegated): a strict three-rung ladder, with composition left as a
  later unit's ask if a target ever needs it.
- **F3 — derive `alpha` from the RECEIPT, or re-resolve it from the descriptors?** From the receipt.
  The descriptor says where gov would put a file today; the receipt says where the target actually
  took it, and `update`'s whole job is to move what was taken. Re-resolving would also make the map
  drift the moment a descriptor's `to` changes, which is the class `-1` closes elsewhere.
  `adopt` is the derivation's SECOND caller and reads the descriptor pairs instead, because at
  bootstrap there is no receipt to read; the drift objection above is about `update`, where a
  receipt exists.
  RESOLVED (agent, 2026-08-24, delegated): from the receipt.

## 9. Revision log

- rev-10 · 2026-08-26 · node a · S13 BUILT, and AC2 RESTATED. Reopened by owner ruling after the
  rev-9 park recorded that its blocking precondition -- an inCMS checkout in hand -- is satisfied on
  node `a`. The committed fixture and its recorded generator now ship under
  `tools/govkit/fixtures/`, and AC1's 21 verbatim / 6 eol / 5 relocate REPRODUCES exactly over the
  real 52-row population, cross-checked against inCMS's own object store at zero disagreements. AC2
  did NOT reproduce and was restated rather than fitted, which is what its own text asked for: its
  population is the 86 rows whose gov SOURCE resolves, not the 52 whose COMMIT does, and the needle
  count there is 25 rather than 26. The missing one is the `/` and `~` forms of `tools` coinciding
  because that directory carries no slash -- the derivation this build recorded as a park before it
  had any way to measure it, now measured.

- rev-9 · 2026-08-25 · built. S13 is DEFERRED: the inCMS-derived fixture cannot be generated from
  this tree, so AC1 and AC2 run over a synthetic fixture whose distribution is MEASURED (4 verbatim
  / 1 eol / 2 relocate / 3 no rung) rather than over the spec's 21/6/5, which belong to S13's
  fixture and are reproduced nowhere. AC2's `13` pairs and `26` needles were NOT asserted anywhere:
  the spec already disclaimed them, and building DERIVED that `26` is wrong even over the 86-row
  population — the `/` and `~` forms of a gov directory carrying no slash are the SAME string, and
  §4's own Inventory says `tools` survives as a single pair, so 13 pairs cannot yield 26 distinct
  needles. `-13` must re-derive rather than inherit either figure. Also corrected: §5's "No new
  subprocess" is wrong — `eol` is a question about bytes, so a row whose index blob is not gov's
  own now pays one `git cat-file`; the code says so at the site. And AC8's predicted red describes
  `9ddcc5c9` and is unreachable on `-8`'s tip, the same correction `-8`'s own ledger recorded.
- rev-8 · 2026-08-25 · round-6 fold: L5 — §10's reuse audit still summarised the derivation as
  reading the RECEIPT, after rev-7 rewrote S3 to take a SEQUENCE OF PAIRS because it has two
  callers. The polarity was reversed by that fold rather than pre-existing it, so the two
  sentences answered one question two ways. §10 now says `alpha` reads what its CALLER supplies:
  the receipt from `cmd_update`, the run's own planned pairs from `adopt`. Same
  one-sentence-left-behind shape rev-7's own M4 filed, one section over.
- rev-7 · 2026-08-25 · round-5 fold: M4 — S3 still said the map is derived from the RECEIPT
  after the round-4 fold gave the derivation a second caller in §8 F3 and §10. It is the
  normative scope item `-13` S4a cites, so a builder read it and wrote a helper taking receipt
  rows, which `adopt` has none of. S3 now states the input as a SEQUENCE OF PAIRS with the two
  callers named, and its closing sentence forbids what it actually forbids — an AUTHORED map,
  not the caller's own pairs.
- rev-6 · 2026-08-25 · round-4 fold: B1's half lands in §8 F3 and §10 — `adopt` is the derivation's
  SECOND caller and reads the descriptor pairs, because at bootstrap there is no receipt, and §10
  now names both callers instead of one. M2 corrects AC1's RED-first population from 32 to 31, with
  the derivation stated. M3 adds S13, the COMMITTED inCMS-derived fixture and its generator script,
  names the vintage inside AC1 and AC2, moves §4 Files touched and §7 to two fixtures, and records
  that AC2's `13` pairs and `26` needles were measured over §4's 86 source-resolving rows rather
  than the 52 this criterion names — so they are UNVERIFIED over its own population and must be
  re-measured before the arm is written. AC9's justification is restated to match `-12` S4 after
  H5: a committed deletion is outside `dirty` because HEAD does not carry it either, and a staged
  one refuses.
- rev-5 · 2026-08-25 · round-5 fold: AC7 still demanded `"schema": 4`, the one surviving instance
  of the bump rev-4 withdrew everywhere else — it now asserts schema 3. AC9's fixture COMMITS its
  deletion, because `-12` S4 would otherwise refuse the run before the `missing` cell is reached.
- rev-4 · 2026-08-24 · round-3 fold: the schema bump is WITHDRAWN. `-7` S6 owns the build's single
  move, 2 to 3, and `-13` §4 defines schema 3 as the generation carrying every field this build adds,
  `carry` included. Three rev-3 specs disagreed about the number and two acceptance criteria were
  mutually unsatisfiable on one tree; the constant's own comment reads "per-**role** row field", and
  `carry` adds no role. §4 Migration, §5 migration/rollback and the §9 summary all say so now.
- rev-3 · 2026-08-24 · round-2 fold: the composition of S11 with `-8`. S12 states ONE stamping
  rule for both arms that write bytes gov does not hold — `oid` is the blob actually written,
  `gov_oid` keeps `-8`'s meaning — so a carried restore stops inheriting `-8`'s raw-arm stamp of
  gov's blob into BOTH identities, and `oid != gov_oid` afterwards reads "carries a rung" rather
  than "local delta". S9 and S11 both point at it, AC10 asserts the restored bytes and the resulting
  row together, and the arm count goes 9 to 10. §1 no longer says those rows "never take an
  automatic write", which S9 answers with reconciliation.
- rev-2 · 2026-08-24 · folded the pre-code review: a proven rung now sets `carry` only and never
  `o_state`, so a rung row reconciles THROUGH the three-way (S9) instead of widening the raw-write
  arm — §5's security bullet claimed the opposite and is replaced. The `missing` restore arm carries
  too, from the row's own directory pair (S11), which is the one bounded exception §3 now names. A
  rung row whose gov copy did not move prints `carried (relocate)` rather than the grid's lying
  `patched` (S10). The schema number does NOT move: `-7` S6 owns the build's single bump and schema 3
  already names `carry`, which is the rev-4 correction below. Two RED-first ACs land
  — AC8 on the index blob after a reconciliation, AC9 on a deleted `relocate` row — and the arm count
  goes 7 to 9. §4's unsourced "27 green by identity / 17 flipped" is WITHDRAWN, with the six
  corrupted lines re-opened at `ce5dca99` and cited by line number in its place.
- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass (5 lenses + fold). Every line
  number cited was opened at `9ddcc5c9`, and every count in §4 was re-measured against inCMS at
  `2cff5855` rather than carried from the brief. Four corrections to the brief are folded in.
  First: the lift is a DIRNAME pair per row, not "stripping equal trailing segments" — the latter
  yields 5 gov directories and 3 surviving pairs and kills every unattended relocation, measured both
  ways, and §4 records the rejected form. Second: the needle count derived from the 13 pairs is 26,
  not 178; 178 is 2 times 89, the shape of a per-ROW needle set rather than the per-directory map the
  architecture specifies, so S4 pins the per-directory derivation and §4 pins 26. Third: the
  `my tools/unattended` hazard is real and verified at lines 132-133, and there is a SECOND instance
  in the same file the brief does not name — four `bash tools/land.sh` lines hit by the bare `tools`
  needle. Fourth: the blanket-rewrite blast radius measures at 17 currently-green rows here against
  the brief's 18; the reconstruction excludes 6 rows whose gov source does not resolve and 34 whose
  recorded commit reads `unverified`, either of which accounts for the one. Two line numbers in the
  brief's reuse list are also off by one and are cited correctly above: `three_way` is at `:2897`,
  and `Report` is at `:565` with `Refusal` at `:78`.

## 10. Reuse audit

Wires through `classify_row` (`:2874`) rather than adding a second classifier beside it, and through
`blob_at` (`:2148`) for every byte it compares, which is what keeps a rung a claim about the git
index rather than about a worktree. The three-way arm reuses `three_way` (`:2897`) unchanged; S6
changes only what is handed to it.

One seam is deliberately NOT reused, and that decision is the reuse result. `resolve_dests` (`:2067`)
and `rule_relpath` (`:172`) already know how a source maps to a destination, and calling them here
would look like reuse. They answer for the descriptor as it reads TODAY, while `alpha` must answer
for what the target actually installed, possibly at a different gov commit and a different `prefix`.
Reusing them would make the map drift with the registry — the same two-spellings-of-one-fact class
`-1` exists to close, re-created one layer down. `alpha` therefore reads what its CALLER supplies
rather than re-resolving the descriptors — the receipt from `cmd_update`, since it is the only
record of what was taken, and the run's own planned pairs from `adopt`, which has no receipt yet
(S3). No new seam is created: the derivation is a private helper with two callers. The first is
`cmd_update` (`:2918`), which feeds it the receipt. The second is the `adopt` verb `-13` adds,
which feeds it the planned descriptor pairs of that run, because at bootstrap no receipt
exists yet — §8 F3 records why that is not a re-opening of the fork.
