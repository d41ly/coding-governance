# TOOL-dQuietDisk-14 — the kit attestation: gov's green held run of a kit's self-tests, recorded by content and carried in the adopter's receipt

**Status:** CLOSED · rev-3 · 2026-11-22 · node d · Tier-2 · base e4699ee7 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-build-TOOL-dQuietDisk-14-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-14-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dQuietDisk-14-deviation-1.md](../build/2026-11-22-build-TOOL-dQuietDisk-14-deviation-1.md) | deviation | — |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-reground-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-9 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-14-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-14-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-14-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-14-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Adopters re-run gov's kit self-tests on every bar, re-proving bytes that only change on upgrade
(`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`, row G2, rework
K4). This unit makes gov say, by content, which kit bytes its own green held runs proved. Each
receipt `govkit` writes into a target then carries that statement, so TOOL-dQuietDisk-15 can hold
an adopter's leg whose vendored bytes match it. Nothing in an adopter's bar changes in this unit.

## 2. Scope (IN)

- **S1** — The digest. For an entry `K` at gov commit `C`, the attested set is every `(source,
  gov_oid)` pair of `K`'s epoch survivors, and of every entry `K` requires, transitively. A
  survivor is an epoch survivor when its role is in `EPOCH_ROLES`, as `cmd_shipped --epoch`
  filters it. `source` is spelled as the receipt row's `source` field spells it, and `gov_oid` is
  that source's blob at `C`. The digest is the SHA-256 of the sorted lines `<source>TAB<gov_oid>LF`.
  Observed by AC1.
- **S2** — The evidence. `K`'s legs are the `[[gate_leg]]` rows its descriptor declares with
  `subject = "kit"`. Each must have a record `<git common dir>/gate-selftest-last/<name key>`, the
  file `run-gates.sh` writes after a first-attempt green on a clean, unmoved tree
  (`tools/run-gates/run-gates.sh@e4699ee75:5955`). The name key is the first 16 hex of the SHA-1 of
  the leg's name. The record's `row` must equal the runner's row hash of the leg's current row in
  `tools/gate-legs.json`: the SHA-1 of that row less the keys `DECLARATIVE_LEG_KEYS` names,
  serialised as `json.dumps(row, sort_keys=True)`. The tuple is read from its one home,
  `tools/run-gates/held_halves.py`, loaded by path from gov's tree. Where it cannot be loaded, the
  whole row is hashed, the runner's own fallback, so a record earned under the tuple reads stale and
  the entry goes unattested. Every pair of the attested set must hold the same blob at the record's
  `sha` as at `C`. Observed by AC1, AC2, AC3 and AC8.
- **S3** — `derive_kit_attestations(root, to_commit)` in `tools/govkit/govkit.py` returns one
  attestation per entry whose every leg holds S2, sorted by entry. An entry with no `kit` leg, a
  leg with no record, a stale row, or a moved blob gets none. It answers an empty list unless
  `to_commit` is gov's HEAD, because the survivor set is resolved from the working tree's
  descriptors, as `cmd_shipped` resolves it. Observed by AC2 and AC5.
- **S4** — The record. An attestation is `{"kit", "digest", "gov_commit", "sources", "legs"}`.
  `sources` is the sorted pair list the digest hashed. `legs` holds one `{"name", "sha", "row"}`
  per leg, the run evidence S2 read. Observed by AC1.
- **S5** — The carry. `write_install_receipt` takes an optional `attest=(root, to_commit)`. When it
  is given, the writer sets the receipt's top-level `attestations` key from S3 before it writes,
  replacing any it held. `apply`, `update --write` and `adopt --write` pass it, so every receipt
  `govkit` writes carries gov's attestations at the vintage it installed. Without it the document
  is written as given. `install.sums` is unchanged, since it is derived from `files` alone.
  Observed by AC4 and AC5.
- **S6** — `WIRE-INTO-PROJECT.md`'s receipt section names the `attestations` key, what proves an
  entry into it, and that a missing or unmatched attestation changes nothing in an adopter's bar.
  Observed by AC6.

## 3. Non-goals (OUT)

- No hold in any bar. Reading an attestation and holding a leg is TOOL-dQuietDisk-15's, in
  `verdict_flow.py`'s selection.
- No new record writer in `run-gates.sh` and no run id. The held-tier record holds `sha` and `row`
  only, and adding a field writes a file dWitnessedBar's branch changes. The `sha` and `row` pin the
  inputs the green was earned on, which is what the attestation claims.
- No tracked attestation file in gov. A committed file would need a records commit after every green
  run, and the held-tier records already hold the evidence; deriving it at write time keeps it one
  fact.
- No host class. The records are this repository's, on the node that ran them. An adopter receives
  gov's statement for that node and runs its legs whenever its own bytes differ.
- No attestation for `--to` other than HEAD. That run carries none, and every leg runs as today.
- No policy key. The attestation is a record, not a saving; the switch for the skip it enables is
  TOOL-dQuietDisk-15's.

### Edges

- **hands-off** `TOOL-dQuietDisk-15` — holding an adopter's kit self-test leg when its vendored
  bytes match an attestation the receipt carries, and running it as today otherwise

## 4. Design

### Where the code was read

Every citation is at `e4699ee75`, the build base: the merge that brought dWitnessedBar's land tip
`ed833f684` into this run, as the owner ruled on 2026-11-22. A citation is by symbol or
`<path>@e4699ee75:<line>`.

### Which hash both ends can compute

govkit renders kit literals at the install prefix, so gov's tree id is not the adopter's bytes, and
the adopter's bytes are not gov's. The receipt already records both sides of each row
(`tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json`, every row carrying `source`,
`gov_oid`, `oid` and `sha256`). `gov_oid` is gov's blob at the row's `commit`; `oid` is the blob the
target's clean filter made of the bytes that landed (`tools/govkit/govkit.py#classify_row`'s docstring).

So the digest is over `(source, gov_oid)`, which gov computes from its own history and the adopter
reads from its own receipt, and neither side needs the other's bytes. Whether the adopter's file
still holds what landed is a separate question that the receipt's `oid` and `sha256` already
answer, through the run-gates kit's `check-receipt.py` in every adopter bar. That second half is
TOOL-dQuietDisk-15's. A rendered row is covered the same way: its `gov_oid` names gov's template and
its `oid` names what rendering wrote.

### Why the required entries join the set

A kit's suite can read a sibling kit's files at run time. An adopter whose sibling copy differs from
gov's would then run the suite against other bytes than gov proved. Joining the closure of `requires`,
which `read_requires_at` already resolves, makes such an adopter unattested for `K` too.

### The derivation

1. Resolve the shipped descriptors once (`read_shipped_descriptors`) and each entry's survivors
   with `resolve_entry`, keeping `EPOCH_ROLES` (`tools/govkit/govkit.py@e4699ee75:14048`).
2. Read every attested source's blob at `to_commit` and at each distinct record `sha` through one
   `git cat-file --batch-check` process, asked `<sha>:<source path>` per line.
3. Read each leg's record and compare its `row` with the manifest row's hash, computed the way the
   runner's leg reader computes it (`tools/run-gates/run-gates.sh@e4699ee75:3086`). Since
   TOOL-dWitnessedBar-51 S48 that hash leaves out `DECLARATIVE_LEG_KEYS`, which the runner imports
   from `tools/run-gates/held_halves.py@e4699ee75:68` and falls back to an empty tuple without
   (`tools/run-gates/run-gates.sh@e4699ee75:2942`). govkit loads that file through
   `importlib.util.spec_from_file_location`, as it already loads gov's `regen.py`
   (`tools/govkit/govkit.py@e4699ee75:2429`), so the tuple keeps one spelling.

A failure at any step costs that entry its attestation, never the receipt write.

### Data model

```json
"attestations": [
  {"kit": "check-wiring",
   "digest": "<64 hex>",
   "gov_commit": "<40 hex>",
   "sources": [["<source>", "<gov_oid>"], ...],
   "legs": [{"name": "check-wiring self-test", "sha": "<40 hex>", "row": "<40 hex>"}]}
]
```

`check-receipt.py` reads `files` alone (`tools/run-gates/check-receipt.py#derive_source_rows`), so
the key is inert to it.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `attestations` | receipt top-level key | none | the probes of section 6 |
| `derive_kit_attestations` | Python function | none | the probes of section 6 |
| `attest` | keyword of `write_install_receipt` | none | the probes of section 6 |

No verb, flag, conf key, policy key or refusal number is minted.

### Files touched (estimate)

`tools/govkit/govkit.py` · `WIRE-INTO-PROJECT.md`

The kickoff manifest's `watch:` line names neither.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| gov's kit tree id | govkit renders literals at the prefix, so no adopter holds those bytes. |
| A hash of the adopter's installed bytes | gov cannot compute it without each adopter's filters and prefix. |
| A committed `attestations.tsv` shipped with a kit | A row's commit moves the kit's epoch, or needs a role outside it, and needs a records commit after every green run. |
| A new store under the common dir | The held-tier records already are the per-leg evidence; a second store is a second fact. |
| The suites named by argv, as the held selection derives them | The descriptor's `[[gate_leg]]` rows already say which legs a kit ships, so the argv parse would be a second spelling. |
| The `held-green` stamp `tools/run-gates/held_halves.py` writes | It certifies a whole held tier's paired native and WSL combine at one sha, never one kit, and no boundary reads it yet (its docstring). |
| A copy of `DECLARATIVE_LEG_KEYS` in govkit | A second spelling of the tuple; a key added on one side would make every record read stale or every change read fresh. |

## 5. Production-readiness checklist

- security: the key is written only by `govkit` through `write_atomic`. A hand-edited attestation
  can only hold a leg whose bytes it names, which TOOL-dQuietDisk-15 must re-check against the
  receipt rows and the installed files, so a forged key holds nothing that differs from what landed.
- perf / scale: one `cat-file --batch-check` and one manifest read per receipt write.
- error / empty / loading states: no attestation, never a refusal. An empty list is written as `[]`.
- observability: `update` and `apply` print one line, `attestations: <n> kit(s) attested at
  <sha8>`, beside the receipt's own lines.
- risks: the gotcha `test-oracle-read-from-a-historical-sha` applies. The record's `sha` is read for
  blob identity only and never as a verdict. A rename of a leg changes its name key and so drops its
  record, which reads as unattested.
- testing: the probes of section 6.
- migration: additive; a receipt without the key reads as unattested.
- user docs: `WIRE-INTO-PROJECT.md` (S6). The help page for the held behaviour is
  TOOL-dQuietDisk-15's, the change an adopter sees.

## 6. Acceptance criteria

- **AC1** — When a probe builds a scratch gov under `%TEMP%/<short-name>` in the shape of the
  govkit self-test's own scratch gov, with `govkit.py`, `upgrade_steps.py`, a registry and
  `tools/run-gates/held_halves.py` copied in, and an entry `demo` declaring one `kit` leg, and
  plants a held-tier record holding HEAD and the leg row's runner hash, `derive_kit_attestations` returns
  one attestation for `demo`. Its digest equals the SHA-256 of the sorted lines built from
  `git ls-tree -r HEAD` over `demo`'s epoch sources, and its `legs` holds the planted `sha` and `row`.
  Red when: the digest is taken over a different set or form, so the two differ.
- **AC2** — When the probe removes the record, plants it with a different `row`, or plants it at a
  commit where one `demo` source differs, `derive_kit_attestations` returns no attestation for
  `demo`, in each case. When `demo` requires a second entry whose source differs at the record's
  `sha`, it returns none either.
  Red when: an absent, stale or moved record still attests.
- **AC3** — When the record's `sha` is an older commit that changed only a file outside the attested
  set, the attestation holds and its `legs` names that older `sha`.
  Red when: the record must equal HEAD, so a green earned before an unrelated commit is lost.
- **AC4** — When `python govkit.py apply --target <t>` and `update --target <t> --write` run in the
  probe's scratch shape with the record planted, `.governance/install.json` carries the
  `attestations` key. With that key removed, the receipt is byte-identical to the one the base
  code writes for the same run, and `install.sums` is byte-identical outright.
  Red when: the key is missing, or the carry moves any other byte of either file.
- **AC5** — When `update --target <t> --to HEAD~1 --write` runs in the probe, the receipt carries
  `"attestations": []`. When `write_install_receipt` is called without `attest`, the document is
  written exactly as given.
  Red when: a `--to` behind HEAD carries an attestation resolved from the working tree.
- **AC6** — When `grep -n "attestations" WIRE-INTO-PROJECT.md` runs, it prints the receipt section's
  lines naming the key, its evidence and its fallback. When
  `python tools/govkit/govkit.py check --target C:/projects/incms/main` and the same against
  `C:/projects/nicocares/main` run read-only from gov before and after the unit, each prints the
  same bytes and exit code.
  Red when: the runbook does not name the key, or a check reads differently.
  permission: read-only against the adopters' main checkouts, never their `gov-upgrade` worktrees.
- **AC7** — When the probe derives attestations for three entries with `GIT_TRACE2_EVENT` set to an
  empty directory, the directory holds at most one file whose `cmd_name` event names `cat-file`.
  Red when: a blob is asked per source, so the count grows with the attested set.
  figure: PINNED, one batch process per derivation.
- **AC8** — When the probe rewords the `demo` leg row's `purpose` after planting the record, which
  is a declarative key, `derive_kit_attestations` still returns the attestation. When it changes
  the row's `argv` instead, it returns none. With the probe's `held_halves.py` removed from the
  scratch gov, a record planted with the runner's declarative-less hash attests nothing.
  Red when: govkit hashes the whole row, so a reworded `purpose` drops a green the runner would
  still hold, or it hashes less than the runner, so an `argv` change still attests.

No verdict moves in this unit: no bar reads the key until TOOL-dQuietDisk-15 lands. `update` and
`apply` keep every receipt row, write and printed line, plus the one count line S5's caller prints.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `govkit runbook parity` · `recall floor arms` · `policy fixtures` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `line length`

The bar runs once at the close. This unit adds no suite arm: its criteria are probes of the
function and of the verbs in a scratch gov.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft. Order 1, as briefed. TOOL-dQuietDisk-16 also writes
  `tools/govkit/govkit.py` and was briefed at order 1, so it moved to order 4 rather than this unit,
  because TOOL-dQuietDisk-15 consumes this one at order 2. TOOL-dQuietDisk-17 (order 2) and
  TOOL-dQuietDisk-18 (order 3) write the same file after it.
- rev-2 · 2026-11-22 · re-grounded at e4699ee75 (dWitnessedBar's land tip merged), under
  `2026-11-22-prompt-TOOL-dQuietDisk-1-reground-task`. What moved: the runner's row hash now leaves
  out `DECLARATIVE_LEG_KEYS` (TOOL-dWitnessedBar-51 S48), so S2 and derivation step 3 read that
  tuple from `tools/run-gates/held_halves.py` rather than hashing the whole row, and AC8 observes
  it. Citations moved: the held-tier writer to 5955, the `changed` selection's leg loop to 3345,
  the row hash to 3086, `EPOCH_ROLES` to 14048, and `check-receipt.py`'s read to
  `derive_source_rows`; the base is `e4699ee7`. The record's shape, `sha` and `row`, did not move.
- rev-3 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. The
  four symbol citations naming the bare basename `govkit.py`, one in section 4 and three in
  section 10, now name `tools/govkit/govkit.py`. No figure was unpinned and no build-method
  section was cited by number. Design, scope and acceptance unchanged.

## 10. Reuse audit

The seams extended: the held-tier last-run records (`<git common dir>/gate-selftest-last/`, written
at `tools/run-gates/run-gates.sh@e4699ee75:5955` and read by the `changed` selection at
`tools/run-gates/run-gates.sh@e4699ee75:3345`), the runner's row hash and its one tuple of
declarative keys (`tools/run-gates/held_halves.py@e4699ee75:68`), the epoch survivor set of
`tools/govkit/govkit.py#cmd_shipped`, the descriptor's `[[gate_leg]]` rows
(`tools/govkit/entries/check-wiring.kit.toml@e4699ee75:36`),
`tools/govkit/govkit.py#read_requires_at`, and the receipt's one writer
`tools/govkit/govkit.py#write_install_receipt`, which `apply`, `update` and `adopt` already share.
No existing seam records an attestation: the receipt has no such key, and
`git grep -n -i "attest" e4699ee75 -- tools/govkit/ tools/run-gates/` prints nothing.

`python tools/codebase-map/reuse_lookup.py "record that a kit tree passed its self-tests and carry it to adopters"`
ranked `tree`, `resolve_kit_dir`, `records` and `remove_tree`, name-token neighbours of which none
records a test result. Recall returned TOOL-dWitnessedBar-5's reuse scout, the hold
predicate this unit's consumer extends, TOOL-aFlaggedScaffold-3 and TOOL-aProbedToolkit-2 on kit
self-tests at adopters, and DECISIONS row TOOL-bQuiltedLantern-3; none records one. The owning chain
build is dWitnessedBar (Test: held legs), and dSafePassage (Supersession) for the receipt writer.
dSafePassage's CLOSED units 5, 10 and 25 to 27 define the walk, the steps and the one blob reader;
none defines a receipt key this contradicts.

The re-ground at `e4699ee75` read `git log 609cd40b1..ed833f684` over `tools/govkit/govkit.py`,
`tools/run-gates/run-gates.sh`, `tools/run-gates/held_halves.py` and `tools/run-gates/check-receipt.py`,
and the dWitnessedBar specs added since, units 106 to 110. No unit there writes a self-test
attestation, a held-leg record beyond `sha` and `row`, or a kit tree hash. Two overlaps are named
for the merge. TOOL-dWitnessedBar-51 S48 changed the row hash this unit compares, which S2 now
follows. TOOL-dHomeGraded-1, landed on main inside the base, added `tools/lib/home_graded.py`,
whose `derive_home_graded` answers which installed `engine` rows still hold gov's bytes
(`oid` equal to `gov_oid`, re-hashed through one `git hash-object --stdin-paths`). That is the
adopter-side half TOOL-dQuietDisk-15 needs, and its spec should extend that block rather than
re-hash the rows itself. This unit's own half, the gov-side digest, is untouched by it.

Recall terms used: attestation kit selftest adopter held receipt gov_oid install.json gate-selftest-last kit tree hash vendored
