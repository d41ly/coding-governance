# DEPL-dCarriedReceipt-13 — `govkit adopt`, the receipt bootstrap

**Status:** SPECCED · rev-5 · 2026-08-25 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-review-DEPL-dCarriedReceipt-9-spec-precode.md](../reviews/2026-08-24-review-DEPL-dCarriedReceipt-9-spec-precode.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 |
| [2026-08-25-review-DEPL-dCarriedReceipt-9-round4.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round4.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 |

<!-- /gen:spec-records -->

## 1. Goal

`cmd_update` refuses without `<target>/.governance/install.json` (`govkit.py:2932`) and `cmd_check`
refuses the same way. Neither live target has one, so the entire update engine has moved zero rows
against a real adopter and everything in `VERDICT_GRID`, `three_way` and the write loop is exercised
only by fixtures. `adopt` is the unblocker: a read-only verb that measures an already-installed tree
against gov history and writes the receipt that measurement supports. Nothing else in this build
reaches either target without it.

## 2. Scope (IN)

- **S1** — the verb: `adopt --target <t> [--to <rev>] [--pin <path>=<rev>] [--re-adopt] [--write]`.
  Read-only unless `--write`, matching `update`'s default and for the same reason. `--to` and
  `--write` already parse; `--pin` and `--re-adopt` widen `parse_args` (`:3316`), which today returns
  a fixed 8-tuple. `USAGE` (`:3298`) and the verb tuple in `main` (`:3370`) each gain the name.
- **S2** — the destination set comes from `load_deploy` (`:553`), `target_context` (`:535`) and
  `resolve_entry` (`:270`), one entry at a time, and it takes BOTH of that function's row channels:
  the landable `writes` map (`:307`) and the `unlanded` list (`:309`). A `forked` rule's rows arrive
  in the second one, because `-10` gives the role a non-`write` kind and `LANDABLE_ROLES` (`:1254`)
  is derived from `ROLE_KINDS`; a destination set built from `writes` alone would make every forked
  row invisible to `adopt` and leave the receipt silent about the files that most need saying.
  `adopt` never invents a second path map: a second answer to "where does this file land" drifts the
  first time a descriptor changes, which is the class `-1` closes. Taking the `unlanded` list whole
  also takes its `merged` entries, which `apply` deliberately skips at `:2428-2429` before writing
  the real merged row in its own shape at `:2417`. `adopt` does the same, and S11 states what it
  writes for them: the stripped unlanded shape is the one row `cmd_check` cannot read.
- **S3** — attribution, per planned destination present in the target's INDEX. Walk `git -C <gov> log
  <to-rev> -- <src>`, **never `--all`**. At `9ddcc5c9` gov carries 8 commits reachable from a ref and
  not from `HEAD`; a walk that reaches them attributes a row to a vintage the adopter was never
  offered.
- **S4** — the attribution is **RUNG-MAJOR**: every commit in the walk is tested at `verbatim` first,
  then `eol`, then `relocate`, and the newest commit within the FIRST rung that matches wins. Rung
  order dominates recency because preferring a newer commit at a lossier rung selects a base whose
  delta was never applied, and the three-way then re-applies work the adopter already has.
- **S4a** — `adopt` derives `alpha` from the planned `(src, dest)` pairs `resolve_entry` returns for
  THIS run, lifted by `dirname` and deduplicated, with the ambiguity drop and the report line of `-9`
  S3. The receipt derivation `-9` F3 ratifies is unavailable before a receipt exists, and the
  descriptor pair is the only record of where a file would land. Without it the `relocate` rung has
  no map at bootstrap, the ladder collapses to `verbatim`/`eol`, and every relocated row — the five
  `-9` §4 measures on inCMS — bootstraps `evidence: "unattributed"` and is skipped by S7 forever.
- **S5** — the row written: `role`, `sha256`, `gov_oid`, `oid`, `commit`, `carry`, and a new
  `evidence` field reading `"vintage-match"`. `apply` writes `"apply"`. An INFERRED base must never be
  mistaken for one a write produced, and today no receipt row carries any provenance-of-provenance
  field at all.
  **`role` comes from the rule `resolve_entry` returned for that destination, NEVER from the
  attribution outcome.** A rule declaring `forked` writes `role: "forked"` carrying that rule's
  `direction` and `record` even when the walk finds a match, and whatever `commit` and `gov_oid` the
  walk found are recorded beside it as EVIDENCE — read by a human, read by no verb, because
  `UPDATE_ROLE` (`:2974`) dispatches on the role before any base is consulted and `-10` S4 maps
  `forked` to `report`. Taking the role from the outcome instead is destructive and not theoretically
  so: a fork has a common ancestor BY CONSTRUCTION, so S3's walk attributes it at its pre-fork
  vintage, S4 matches `verbatim` there, and the row adopts as `engine` with `oid == gov_oid` on an
  exact coincidental match — identities agreeing, raw-write arm OPEN, `-8`'s closure never reached.
  That is the memory-recall landmine `-10` measured, re-manufactured by the bootstrap that exists to
  record it.
- **S6** — `--pin <path>=<rev>` fixes one destination's base by operator assertion. Such a row records
  `evidence: "pinned"`, so an assertion is never read back as a proof.
- **S7** — a destination attributing to NO gov vintage gets its OWN state: `evidence:
  "unattributed"`, no `commit`, no `gov_oid`. Its `role` stays whatever its rule declared. An
  attribution failure is not a fork — `forked` is a descriptor's declaration about a file's
  provenance, and reusing it for the walk's report of its own failure gives one token two meanings,
  which is how `-10`'s printer and this unit's writer came to disagree about the same row. `cmd_update`
  gains one precondition inside its classification loop: a row carrying `evidence: "unattributed"`
  whose role resolves at `:2974` to the `table` disposition is printed, counted and skipped before
  `classify_row` at `:3014` — after `how` resolves, before the verdict table it feeds. Every writing
  disposition needs a base and this row has none. Written in neither direction until an operator
  supplies one with `--pin`.

  **`evidence: "unattributed"` is the SOLE predicate, and field-absence is deliberately not an
  equivalent form of it.** An earlier rev said "equivalently, a row carrying neither `commit` nor
  `gov_oid`", and that clause was false and destructive. Every row `apply` writes through the
  `unlanded` channel at `:2440` carries `path`, `role`, `kit`, `version`, `written`, `source` and
  `why` and NO `commit` and no hash — those are the rows `apply` writes at `:2440` —
  `project-owned`, `generated` and `rendered`. `UNLANDED_REASON` (`:236`) carries a fourth key,
  `merged`, and `resolve_entry`'s `unlanded` list carries merged entries too; `apply` skips them at
  `:2428-2429` and writes the real merged row at `:2417` instead. `-10` S3 adds a fifth key,
  `forked`. Under the field-absence reading this precondition would swallow all of them ahead of the
  dispatch and silently delete four dispositions that exist for exactly those roles: `skip` at
  `:3006-3008` (13 rows on inCMS alone), the `adopter` re-render report at `:3021`, `block`'s
  block-hash compare, and `-10`'s `report` — so `-10`'s printer would never run for the forked rows
  it was written for, and the operator would be told to `--pin` a base for a file that is report-only
  forever. `table` is the only disposition that can put bytes on disk (`:3063`), and this skip exists
  to stop a write against a base that does not exist. Every other disposition dispatches exactly as
  today: `skip` counts at `:3006-3008`, `block` runs its own compare at `:2996-3005`, `adopter` caps
  at `re-rendered` at `:3021`, `report-reseed` runs the seed override at `:3016-3020`, and `-2`'s
  `pins` and `-2`/`-10`'s `report` are report-only by
  construction. Three of those read a base and report against `base = None` on an unattributed row —
  `reseed-available`, a capped `re-rendered`, and `block-moved` — and the tally §5 requires is where
  an operator sees them. §4's own inventory already knew these were different things: it excludes the
  13 `project-owned` rows from the 41 unattributable ones.

  This precondition and `-7` S9's integrity assertion are SEQUENTIAL rather than competing. S9 runs
  first, in `cmd_update`'s preamble over the whole receipt, and is scoped by field presence,
  so it passes over a row carrying neither field rather than refusing on it; this precondition then
  catches that row inside the classification loop.
- **S8** — three refusals: `--target` resolving to the gov checkout (the form at `:2930`); an existing
  `install.json` without `--re-adopt`, on `cmd_intake`'s stated reasoning (`:3186-3191`) that a
  committed authorization is not something a verb silently rewrites; and a dirty target index.
- **S9** — `selftest.py` arms per branch and a `refusal_join.py` arm per refusal.
- **S10** — the receipt ENVELOPE, not just the rows. Every scope item above describes a `files` row,
  and three other units read fields OUTSIDE that array. `adopt` writes the envelope `cmd_apply`
  writes at `:2820-2827`, minus the keys that record an install this verb did not perform:

  | key | value `adopt` writes | who reads it |
  |---|---|---|
  | `schema` | `RECEIPT_SCHEMA`, whatever `-7` S6 set | `cmd_update`'s schema-1 role-distrust arm |
  | `gov_source` | the gov checkout's path | operator diagnostics |
  | `gov_commit` | the resolved `--to` | `-12` S7/S8's vintage refusals; `-11` S0/S1's rename base at `:2938` |
  | `prefix` | `deploy["prefix"]` | destination resolution on a later `apply` |
  | `kits` | the claimed selection | `-2`'s pins arm; `:2957`'s `claimed` list |
  | `files` | the rows S1–S7 describe | everything |

  `orders`, `baseline`, `after`, `hook_block` and `gate_runner` are NOT written: each records what an
  install DID, and this verb installs nothing. Every one of their readers already tolerates absence
  via `.get`, and S9's arms assert that a receipt without them classifies without refusal.

  **Why this is a scope item rather than an implementation detail.** Omit `gov_commit` and `-12` S7
  fails OPEN by its own words — "a receipt carrying no `gov_commit` skips the check" — on precisely
  the population the vintage guard was written for; `-11`'s rename diff has no base and the unit is
  inert; and `-2`'s pins arm and `:2957`'s `claimed` read an empty list, so every registry entry
  prints as "available (not installed)". Three units silently degrade on every receipt this verb
  writes, which is every real adopter.
- **S11** — the row classes `resolve_entry` does not produce. `adopt` writes the ONE `attributes` row
  `cmd_apply` synthesizes at `:2350`, recomputed by `lf_pins()` (`:1805`) over the claimed kits at
  `--to` and compared against the target's existing govkit-owned block: same keys (`block_id`,
  `marker_style`, `mode`, `normalized`, `block_sha256`, `patterns`), with `written: false` because
  this verb wrote no block. It also writes each `merged` row in `apply`'s shape (`:2417`), not the
  unlanded one — `block_id`, `marker_style` and `block_sha256` measured from the block the target
  actually holds — and skips merged entries in the unlanded channel exactly as `apply` does at
  `:2428-2429`. Without both, `-2`'s `pins` arm never dispatches and `cmd_check`'s merged loop raises
  on `row['block_id']` at `:1570`.

## 3. Non-goals (OUT)

- **Not** refusing when some rows fail to attribute. Partial attribution is the normal state of a
  hand-forked adopter, and a bootstrap that demands totality bootstraps nothing. Measured below.
- **Not** writing a single byte into the target's working tree. `adopt` writes `install.json` and
  `install.sums` under `--write` and nothing else. The first byte movement is `update`'s, after an
  operator has read the receipt.
- **Not** auto-resolving a base for a row matching no gov vintage. That is on the build's ratified
  cut list; such a row records `evidence: "unattributed"` and stays unattributed until an operator
  pins it. It is NOT relabelled `forked`: that role is a claim the DESCRIPTOR makes, and the walk
  does not get to make it on the descriptor's behalf.
- **Not** rename detection during attribution. A destination whose source moved in gov attributes at
  the source path the descriptor declares TODAY; `-11` owns renames on the update path.
- **Not** installing an unadopted kit, and **not** `--force` or `--yes`. Both are cut-list items.
- **Land-alone:** `adopt` needs `-1` (destinations), `-7` (two identities), `-9` (the rungs), `-10`
  (role `forked`) and `-12` (the S7 vintage guard AC11 observes) beneath it. It cannot land before
  them, and it is stated in section 8.

## 4. Design

### Data model

Each written row carries the receipt shape `apply` already produces at `:2458-2460` — `path`, `role`,
`kit`, `version`, `sha256`, `source`, `commit` — plus `-7`'s `gov_oid` and `oid`, `-9`'s `carry`, and
this unit's `evidence`. `evidence` takes exactly `"apply"`, `"vintage-match"`, `"pinned"` or
`"unattributed"`.

`sha256` is `_sha` of the TARGET's bytes at the moment the receipt is written — the same quantity
`apply` records at `:2459` and the quantity `cmd_check`'s integrity loop compares at `:1513-1518` —
so `install.sums` stays verifiable with `sha256sum -c` on a tree `adopt` did not touch. Without it,
`install.sums` (`:2828`) is empty, `cmd_check`'s sidecar join (`:1551`) compares zero rows against
zero lines and passes, and its integrity loop counts every row as verified without hashing anything.
Which bytes the field holds for a carried row is F5.

`role` is not measured. It is copied from the rule `resolve_entry` returned for that destination, so
the receipt's role and the descriptor's role are the same fact rather than two facts that agree until
they do not — and a `forked` rule's `direction` and `record` ride along with it, which is the shape
`-10` S4's printer reads. The attribution walk contributes `commit`, `gov_oid`, `carry` and
`evidence`, and nothing else.

**The safety argument rests on one field.** A bootstrapped row's `gov_oid` is the hash of the GOV blob
at `commit` — `blob_at(root, commit, src)` (`:2148`) — and never of the bytes on the target's disk.
Invert that and `gov_oid == oid` for every row, the identities agree, the local-delta predicate reads
false, and a repathed file classifies `("equal","differs")` → `stale` (`:2845`) → `dp.write_bytes(
c["theirs"])` (`:3071`) on the FIRST write. Every carried edit in the tree would be destroyed by the
first update, reported as a clean write with zero conflicts. The field is the whole difference between
a bootstrap and a silent overwrite.

### Inventory

Measured at `9ddcc5c9` against inCMS's own `.governance/install.index`, which is the only receipt-like
artefact either live target holds. Of its 92 rows, 38 carry a blob OID that exists in gov's object
database and 54 do not. Excluding the 13 `project-owned` rows — bytes gov never authored, which
`UPDATE_ROLE` skips (`:2860`) — **41 gov-authored rows do not attribute by verbatim identity**, and 16
of those are the deliberate divergences `.governance/kits.json` documents, each carrying a `record` id.
The `eol` and `relocate` rungs are what must reduce the remaining 25; whatever survives them is
`forked`. This is the measurement behind S3's non-goal: a bootstrap that refused on any unattributable
row would refuse on inCMS today.

### Migration

None of its own, and **the schema number does not move for this unit**. `RECEIPT_SCHEMA` (`:39`)
carries the standing rule that it is bumped by any unit adding a per-role row field, and `-7` S6
performs the one bump this build takes, 2 to 3. Schema 3 is DEFINED as the generation carrying
`-7`'s `gov_oid` and `oid`, `-9`'s `carry` and this unit's `evidence`, so that single bump covers all
four fields. The three units land inside one generation and no receipt is ever written at an
intermediate state, because this unit cannot land before `-7` (§8 F3). A second bump would mint a
schema number no writer ever writes and no reader could tell apart from the first, which is the drift
a version field exists to prevent. `adopt` itself creates a receipt where there was none and stamps
whatever `RECEIPT_SCHEMA` `-7` set; `--re-adopt` replaces one, which is why it is a flag rather than
the default.

### Alternatives rejected

- *Hash the target's bytes into `gov_oid`.* Rejected above; it is the inversion that makes the first
  update destructive.
- *Walk `git log --all`.* It reaches 8 commits off `HEAD` in this repo today, several of them on
  in-flight branches. An adopter attributed to an unmerged branch has a base nobody shipped.
- *Take the row's `role` from the attribution outcome.* The inversion of S5, and the same class of
  defect as hashing target bytes into `gov_oid`: a declared fork whose pre-fork ancestor still sits in
  gov's history attributes cleanly, adopts as `engine`, and is then overwritten by the first
  `update --write` with the bytes the descriptor exists to say are wrong for this target. Measured on
  the live pair: gov's `tools/memory-recall/extract.py` imports `recall_conf` at `:55` and calls
  `recall_conf.resolve()` at `:57`, and inCMS's `scripts/recall/` carries no `recall_conf` at all.
- *Prefer the newest matching commit across all rungs.* This is the rung-major decision inverted, and
  it is load-bearing: a newer `relocate` match beats an older `verbatim` one only if you are willing
  to treat a lossy transform as evidence, which then feeds a three-way base that was never real.
- *Fold `adopt` into `intake`.* `intake` writes the descriptor from operator answers and refuses to
  measure anything (`-3`). Measuring a tree and recording a decision are different verbs with
  different refusals, and merging them makes one refusal reachable through the other's flags.
- *Derive destinations from the target's tree instead of the descriptor.* That is a second path map,
  and it would classify any file the adopter happened to place under a kit directory as gov's.

### Files touched (estimate)

`tools/govkit/govkit.py` (~200 lines: `cmd_adopt`, the attribution walk, S4a's map derivation, S11's
two synthesized row classes, `parse_args`, `USAGE`, `main`), `tools/govkit/selftest.py` (20 arms,
derived in §5), one fixture family building a scratch gov with a multi-commit history and a target
holding verbatim, `eol`, `relocate`, unattributable and declared-forked copies — the last of them
byte-identical to gov at an old commit, which is the arm AC9 needs. The same family declares one
`[[lf_pin]]` and one merged rule for AC13, and a deliberately ambiguous gov directory for the drop
AC12 asserts.

## 5. Production-readiness checklist

- security — `adopt` is the field that decides whether the first `update --write` is a sync or a
  wipe. S5's `gov_oid` rule is the security content of this unit; every other line is bookkeeping
  around it.
- perf / scale — one `git log` walk per planned destination, bounded by that path's history. On
  NicoCares' 143 planned writes this is the run's dominant cost; the walk is capped at the first
  matching commit per rung and short-circuits on `verbatim`.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a target with `deploy.toml` and an empty tree bootstraps a receipt
  with zero rows and says so rather than exiting silently; a destination absent from the index is
  reported as not-installed and gets no row.
- observability — the run prints one line per destination with its role, its rung and its evidence,
  and a tally by rung, by `forked` and by `unattributed` — three counts, because a declared fork and
  a failed attribution are different facts and an operator acts differently on each. That tally is
  the operator's read on whether the tree is adoptable before a byte moves.
- risks — the real risk is a WRONG attribution that looks right: a path whose history contains a
  coincidentally identical blob at an old commit. On a FORKED destination that coincidence is not a
  noisy merge but a wipe, which is why S5 binds the role to the rule and not to the match.
  Rung-major plus newest-within-rung bounds it, and `--pin` is the operator's correction. A wrong
  base makes a later three-way noisier, never destructive, because the raw-write arm stays closed
  whenever `oid != gov_oid`.
- testing + left-shift gates — twenty `selftest.py` arms. S9 counts arms per BRANCH rather than per
  criterion, so the figure is derived rather than read off §6: the eleven §6 demanded while it ended
  at AC9, plus the nine branches this fold adds. Those nine are AC10's envelope key-set arm; AC10's
  sidecar arm, asserting `install.sums` is non-empty and that `check` compares N lines against N
  hashed rows; AC11's live-envelope arm, an `adopt --write` followed by a backwards `update --to`
  that must refuse by `-12` S7; S10's absent-optional-keys arm, asserting a receipt carrying none of
  `orders`, `baseline`, `after`, `hook_block`, `gate_runner` classifies without refusal; AC12's
  needle-map arm over S4a's derivation; AC13's two arms, one for the `attributes` row reaching
  `-2`'s `pins` dispatch and one for the merged row surviving `cmd_check`; and AC14's two arms, one
  per non-`table` role. It stays an estimate until the arms are written, and is re-derived then. Two
  classes are left-shifted, both as standing predicates rather than as fixes to one fixture. The
  inversion in S5: for every written row carrying a `commit`, `gov_oid` equals `git -C <gov>
  rev-parse <commit>:<src>`. And the role binding: for every destination whose rule declares
  `forked`, the written row's role is `forked`, whatever the walk returned.
- migration / rollback — the receipt is a new file; rollback is deleting it. `--re-adopt` is the only
  path that replaces an existing one and it refuses without the flag.
- user docs — `WIRE-INTO-PROJECT.md` gains an adoption section: `intake`, then `adopt`, then read the
  receipt, then `update`. This is the first documented path onto the engine for an existing tree.

## 6. Acceptance criteria

- **AC1** — At `9ddcc5c9`, `python tools/govkit/govkit.py adopt --target <t>` exits **2** with
  `unknown subcommand 'adopt'` from `main` (`:3387`). Observe this RED first; the verb does not exist.
- **AC2** — Without `--write`, a run against a fixture prints its per-destination rows and creates no
  `.governance/install.json` (`test ! -e`), and the target's index is unchanged
  (`git -C <target> status --porcelain` empty).
- **AC3** — With `--write` against a target holding gov's bytes verbatim at `--to`, every row records
  `carry: "verbatim"`, `gov_oid == oid`, and `evidence: "vintage-match"`.
- **AC4** — The inversion gate. For a target file that is a `relocate` of gov's blob, the written row's
  `gov_oid` equals `git -C <gov> rev-parse <commit>:<src>` and does **not** equal
  `git -C <target> rev-parse :<path>`; a subsequent `govkit.py update --to <same rev> --write` writes
  zero bytes to that path and `git -C <target> status --porcelain` stays empty.
- **AC5** — Rung-major. In a fixture where the newest commit in a path's history matches only at
  `relocate` while an older commit matches `verbatim`, the written row's `commit` is the older one and
  its `carry` is `"verbatim"`.
- **AC6** — Partial attribution proceeds, under its OWN state. A fixture carrying one destination
  that matches no gov vintage writes that row with `evidence: "unattributed"`, no `commit` and no
  `gov_oid`, keeps the `role` its rule declared, and the run exits **0**. A following `update --write`
  prints that row, writes zero bytes to it, and never reaches `classify_row` (`:3014`) for it. The
  row's role is asserted to be its rule's, NOT `forked` — the arm fails if the two states are
  collapsed back together.
- **AC7** — `--pin <path>=<rev>` overrides the walk for that path only, and the row records
  `evidence: "pinned"` rather than `"vintage-match"`.
- **AC8** — All three refusals fire by name: `--target` pointed at the gov checkout; a second `adopt`
  over an existing `install.json` without `--re-adopt`; and a run against a target whose index is
  dirty. `python tools/govkit/refusal_join.py` exits 0 with an arm for each.
- **AC9** — The role binding. A fixture whose descriptor declares a source `forked` while the
  target's copy is BYTE-IDENTICAL to gov's blob at an older commit adopts that row as `role:
  "forked"`, carrying the rule's `direction` and `record`, with the matching commit recorded as
  evidence rather than acted on — and a following `govkit.py update --write` writes ZERO bytes to that
  path (`git -C <target> status --porcelain` empty afterwards). Observe RED first: with the role taken
  from the attribution outcome the row adopts as `engine` at `carry: "verbatim"` with `oid ==
  gov_oid`, the raw-write arm is open on it, and the update lands gov's fork over the target's working
  program.

- **AC10** — The envelope. After `python tools/govkit/govkit.py adopt --write --target <fixture>`,
  `install.json` carries `schema`, `gov_source`, `gov_commit`, `prefix`, `kits` and `files`, and
  carries none of `orders`, `baseline`, `after`, `hook_block`, `gate_runner`. The value of
  `gov_commit` equals the resolved `--to`, and `install.sums` is non-empty, carrying one line per row
  that carries a `commit`, with `govkit.py check --target <fixture>` reporting N lines compared
  against N hashed rows for that same N.
- **AC11** — The envelope is LIVE, not merely present: immediately after that `adopt --write`,
  `govkit.py update --to <an older sha> --write` REFUSES by `-12` S7, naming both shas. Observe RED
  first: with `gov_commit` absent, `-12` S7 skips its own check by its own words and the run proceeds
  to raw-write every clean row backwards. This is the AC that stops the envelope from being written
  and never read.
- **AC12** — The needle map exists at bootstrap. Over the AC5 fixture, `adopt` derives `alpha` per
  S4a from the planned `(src, dest)` pairs, prints one line per dropped ambiguous gov directory
  NAMING it, and prints the pair count beside a needle count that is exactly twice it, because `-9`
  S4 emits both the `/` and the `~` form. That is the same derivation and the same arithmetic `-9`
  AC2 asserts over its own receipt fixture, observed here on the descriptor-side caller, so the two
  callers of one map cannot disagree; the counts are `-9` AC2's to state and are not restated here.
  Observe RED first: with no map the `relocate` rung cannot fire, the row AC4 is written for
  bootstraps `evidence: "unattributed"` instead, and S7 skips it forever.
- **AC13** — The row classes `resolve_entry` does not produce, per S11. On a fixture declaring one
  `[[lf_pin]]` and one merged rule, `adopt --write` then `update --write` prints one `pins` row and
  one `block` row rather than nothing, `install.json` carries exactly one row with `role:
  "attributes"` and `path: ".gitattributes"`, and `govkit.py check --target <fixture>` reports the
  merged block intact rather than raising. Observe RED first: with the rows taken from
  `resolve_entry`'s two channels alone, `install.json` carries no `attributes` row, `-2`'s `pins` arm
  never dispatches, and `check` raises `KeyError` on `row['block_id']` at `:1570`.
- **AC14** — S7's scoping, both ways. In a fixture whose bootstrapped receipt carries an
  unattributed `seed` row and an unattributed `attributes` row, `update --write` dispatches BOTH
  through `UPDATE_ROLE` (`:2974`) rather than skipping them: the `seed` row reaches the seed override
  at `:3016-3020` and reports, the `attributes` row reaches `-2`'s `pins` arm and reports, and
  neither writes a byte (`git -C <target> status --porcelain` empty). Observe RED first: under a skip
  scoped by field-absence, or by anything wider than the `table` disposition, both rows are printed,
  counted and skipped and neither disposition ever runs.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest` and `govkit
selfcheck` legs, plus `tools/govkit/refusal_join.py`. Adds twenty arms and the two standing
predicates — AC4's `gov_oid` identity and AC9's role binding — to `selftest.py`; adds no new leg
file. The `selfcheck` verb-coverage arm must also see the new verb, so its assertion over `USAGE` and
`main`'s dispatch stays honest.

## 8. Open questions

- **F1 — must `adopt` refuse on a dirty target WORKTREE, or only a dirty INDEX?** Index only. `adopt`
  reads the index and writes one file under `.governance/`; refusing over an unrelated unstaged edit
  in a repository gov does not own is the shape adopters learn to route around. `-12` owns the
  worktree preconditions on the verbs that write bytes.
  RESOLVED (agent, 2026-08-24, delegated): index only, under the full-scope approval.
- **F2 — should `--re-adopt` preserve anything the previous receipt recorded?** No. `--re-adopt`
  re-measures from scratch and re-reads every role from the descriptor; carrying a stale `commit`,
  `carry` or `evidence` forward is exactly the trusted-from-the-receipt shape the `carry` contract
  forbids. `role` is not preserved either, but for the opposite reason: after S5 it is never a
  measurement to preserve — it is re-read from the rule on every run, so an `unattributed` row that
  the descriptor has since declared `forked` comes back as `forked` without anyone editing a receipt.
  RESOLVED (agent, 2026-08-24, delegated): full re-measurement, roles re-read from the descriptor.
- **F3 — landing order.** This unit cannot land alone: it consumes `-1`'s destination resolution,
  `-7`'s two identities, `-9`'s rungs and `-10`'s `forked` role, and AC11 observes `-12` S7's vintage
  guard in both directions, so `-12` is a landing dependency of this unit's criteria rather than of
  its code. It lands after all five, which is the build README's step 5.
  RESOLVED (agent, 2026-08-24, delegated): lands after `-1`, `-7`, `-9`, `-10`, and after `-12`,
  whose S7 vintage guard AC11 observes. The fifth was added 2026-08-25 in the round-4 fold.
- **F4 — do `--re-adopt` and `--pin` pass the flag test `-11` and `-12` share?** That test reads: a
  scope flag enables a NARROWER class of action, defaults OFF, and overrides no refusal. `--pin`
  passes on all three arms — it narrows the attribution of ONE named destination, defaults OFF, and
  overrides nothing, since a pinned row is still recorded as an assertion (`evidence: "pinned"`)
  rather than as a proof. `--re-adopt` passes the first two and is the one place the test bites: it
  does release S8's existing-receipt refusal. Recorded rather than papered over, because that refusal
  guards a decision artefact rather than a byte, its stated purpose is to demand a second explicit
  invocation, and it is the ONLY refusal in this unit any flag may reach. No later flag may cite
  `--re-adopt` as precedent for switching off a safety refusal.
  RESOLVED (agent, 2026-08-24, delegated): both flags are held to the shared test; `--pin` passes
  clean, `--re-adopt` passes with the released refusal named here.
- **F5 — for a carried (`eol`/`relocate`) row, whose bytes does `sha256` hash: gov's at `commit`, or
  the target's on disk?** The TARGET's, at the moment the receipt is written. This row class is the
  first place the two diverge, and three instruments already read the field that way: `cmd_apply`
  hashes the bytes it wrote to the target (`data` at `:2459`), `-8`'s ratified Alternatives bullet
  keeps `_sha(merged)` for the same reason, and `cmd_check`'s integrity loop compares the field
  against the target's file (`:1513-1518`). It is also the only reading under which `install.sums`
  survives a plain `sha256sum -c` on a tree `adopt` did not touch. `gov_oid` stays gov's blob at
  `commit` per S5, so the two remain different facts and the inversion §4 warns about is untouched.
  RESOLVED (agent, 2026-08-25, round-4 fold): the target's bytes at receipt-write time. Recorded as
  the round-4 reviewer's inference from those three instruments rather than as a measured fact, and
  flagged there as a decision the owner should ratify.

## 9. Revision log

- rev-5 · 2026-08-25 · round-4 fold: B1 adds S4a — `adopt` derives `-9`'s `alpha` map from the
  planned `(src, dest)` pairs, because the receipt derivation `-9` F3 ratifies has no receipt to read
  at bootstrap — and AC12 observes it; without the map the `relocate` rung cannot fire and AC4 and
  AC5 are unbuildable. B2 adds S11, the two row classes `resolve_entry` never produces — the one
  synthesized `attributes` row and the merged row in `apply`'s shape — plus AC13; without them `-2`'s
  `pins` arm never dispatches on an adopted receipt and `cmd_check`'s merged loop raises on
  `row['block_id']`. H1 rescopes S7's skip to rows whose role resolves to the `table` disposition,
  after `how` resolves at `:2974` and before `classify_row` at `:3014`, propagates that into AC6, and
  gains AC14 over the two non-`table` roles S7 had left with no stated treatment. H2 restores
  `sha256` to S5 and to §4's quotation of `:2458-2460`, records the target-bytes reading as F5, and
  extends AC10 onto `install.sums`, which was otherwise written empty and graded zero against zero.
  M5 adds `-12` to §3's land-alone bullet and to F3, since AC11 observes its S7 guard in both
  directions. M6 replaces S7's `UNLANDED_REASON` gloss — the dict has four keys and `-10` adds a
  fifth — and carries `apply`'s merged `continue` into S2, which is the gloss that hid B2. L1's arm
  count is re-derived per BRANCH at twenty, moved in §4, §5 and §7, with §5 enumerating the nine
  branches this fold adds so the figure is checkable rather than asserted.
- rev-4 · 2026-08-25 · round-5 fold: S10 adds the receipt ENVELOPE, which no scope item covered
  while three units read it — without `gov_commit` the `-12` S7 vintage guard fails OPEN by its
  own words, `-11` has no rename base and `-2` no kit list, on every receipt this verb writes.
  AC10 and AC11 assert it, AC11 by requiring a backwards `--to` to refuse right after an adopt.
  S7's "equivalently, a row carrying neither field" clause is DELETED: it would have swallowed
  every `unlanded` row and deleted four dispositions.
- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass (5 lenses + fold). `cmd_update`'s
  no-receipt refusal, `resolve_entry`'s return shape, `blob_at`'s index-side contract, `parse_args`'
  8-tuple and `main`'s verb dispatch were each read in source at `9ddcc5c9`. **Two brief corrections.**
  The brief says gov carries 6 commits off `HEAD`; measured, `git rev-list --all --not HEAD --count`
  reports **8** at `9ddcc5c9`, which strengthens rather than weakens the no-`--all` rule. The brief
  says 28 of inCMS's 92 rows cannot attribute; that number does not reproduce from any instrument in
  either tree. Measured by blob identity against gov's object database, 54 of 92 do not attribute
  verbatim, or **41** excluding the 13 `project-owned` rows. The brief's other figure is exact: 16 of
  them are documented in `.governance/kits.json`, each with a `record` id.
- rev-2 · 2026-08-24 · folded the pre-code review: B3, role `forked` defined twice. S5 now binds a
  row's `role` to the rule `resolve_entry` returned rather than to the attribution outcome, and S7
  gives an attribution failure its own `evidence: "unattributed"` state instead of borrowing the role,
  so the token carries one meaning again; S2 takes both of `resolve_entry`'s row channels, since a
  non-landable role arrives in `unlanded` (`:309`) rather than `writes` (`:307`); AC6 is rewritten onto
  the new state and AC9 added for the coincidental-match case, whose RED is the fork adopting as
  `engine` with the raw-write arm open. §8 gains F4, holding `--re-adopt` and `--pin` to the flag test
  `-11` and `-12` share and naming the one refusal `--re-adopt` releases, and F2 is re-based off the
  pre-fold reading in which `forked` was a verdict the walk produced. The `-10` half of B3 — the
  printer tolerating an absent `direction` — lands in `-10` rev-2.
- rev-3 · 2026-08-24 · round-2 fold: §4 Migration now STATES the build's schema rule, which this unit
  owns — `-7` S6's single 2-to-3 bump covers every per-row field this build adds, `evidence`
  included, so "Migration: None" no longer reads as a unit adding a field while ignoring
  `RECEIPT_SCHEMA`'s own comment at `:39`. That comment is quoted as it reads in source, "per-role
  row field", rather than as the round-2 brief paraphrased it. S7 gains the ordering against `-7`
  S9's preamble assertion, so the two preconditions read as sequential rather than competing, and
  its parenthetical is tightened from "no `commit`" to "neither `commit` nor `gov_oid`" to match
  the field-presence scoping S9 is now built on. §5's observability and risks lines are rewrapped,
  a round-1 miss that had left two prose lines at 158 and 140 columns.

## 10. Reuse audit

Every input is an existing seam and none is duplicated: `load_deploy` (`:553`) for the descriptor,
`target_context` (`:535`) and `resolve_tokens` (`:516`) for the ctx, `resolve_entry` (`:270`) for the
destinations, `blob_at` (`:2148`) for gov-side bytes, and `-7`'s index-side reader for target-side
bytes. The receipt row shape is `cmd_apply`'s (`:2458-2460`) with the fields `-7`, `-9` and this unit
add, so `cmd_update` reads one row grammar rather than two. S11's two synthesized classes reuse
`cmd_apply`'s own producers rather than a second shape — `lf_pins` (`:1805`) for the `attributes`
row, `apply`'s merged row at `:2417` for the block — and S4a reuses `-9` S3's derivation, called with
the descriptor pairs instead of receipt rows, so `adopt` and `update` build one map by one rule. The
refusals reuse the `Refusal` class
(`:78`) and the `Report` findings channel (`:565`), and are counted by the existing `refusal_join.py`
contract rather than a new counter. One genuinely new mechanism exists — the attribution walk — and it
has no prior seam: nothing in this engine has ever asked git a question about a path's history. The
role binding in S5 is the opposite of a new mechanism: it reuses the role `resolve_entry` already
resolved under the descriptor's precedence rules, rather than deriving a second role from a
measurement and leaving the receipt to arbitrate between them.
