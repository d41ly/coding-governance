# TOOL-dDeclaredLoop-8 — claims keyed and trusted by key and source

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 16 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0093@a21f7ad5 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-26 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

Every stored claim a session reads carries a key over what it was derived from, the commit or tree,
the base, the remote ref values and its age, and is trusted by that key and by its weakest source:
`fresh` when the key recomputes equal and no source is actor-typed, `re-derived` when the key moved
and a deriver exists, `evidence` otherwise. The startup card's cells and the driver's `--claims`
rows carry their keys, and the replay re-keys the card in the session's own tree, so a session can
tell a fresh claim from a stale one without re-deriving it (gap-orient-05; the orientation record's
`[trust]`, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md:184-201`).

## 2. Scope (IN)

- **S1** — The key, `derive_claim_key(sources)` in `tools/loop/claims.py`: `k1:` and the first 16 hex
  digits of the SHA-1 of the canonical form of the sources, `commit=<sha>` or `tree=<sha>`,
  `base=<sha>`, and each remote ref as `<ref>@<sha>`, sorted by ref name and joined by NUL. The age is
  never hashed: the derivation's UTC time is stored beside the key as `at`, and the class bound of S3
  reads it. A source the caller could not read is spelled `<name>=?`, which no recomputation equals.
  Observed by AC1, AC2.
- **S2** — The source classes, `CLAIM_CLASSES` in `tools/loop/claims.py`, the `[trust]` table's five
  rows as data: `history` (a commit and its trailers, a verdict keyed by tree, BASE: trusted for that
  commit or tree), `view` (the card's cells, `LIVE.md`, the plan view, generated regions: trusted while
  the key matches), `remote` (leases, mailbox entries, run claims: trusted while the key matches and
  `at` is inside the class's age bound), `provenance` (the owner's verbatim words, a ratification
  through the guarded command, the policy file: authoritative for intent) and `typed` (status words an
  agent typed, README status, READY text, session logs, a compaction summary, auto-memory: evidence
  only). A claim over several sources takes its weakest class, in the order the table lists from
  strongest to weakest, with `typed` weakest. Observed by AC3.
- **S3** — The verdict, `derive_claim_verdict(stored, recomputed, claim_class, at, now)`: `evidence`
  when the class is `typed`, or when no recomputed key is given because no deriver exists; `fresh`
  when the two keys are equal and, for `remote`, `now - at` is inside the bound; `re-derived` when the
  keys differ or the bound has passed and a recomputed key exists, the caller re-deriving the claim.
  The `remote` bound is the driver's own stale bound for run claims, read from the driver, never typed
  here. Observed by AC3, AC4.
- **S4** — The CLI, `python tools/loop/claims.py key …` printing a key, `verdict …` printing one of
  the three words, and `card-keys` printing the card's two class keys over the tree it runs in. A
  claim key printed anywhere is spelled `key <k> · <verdict>`, the form unit 7's engine prints for each
  claim it used. Observed by AC1 to AC5.
- **S5** — The card carries its keys: `render_card` in `skills/session-kickoff/manifest-check.sh`
  writes one `keys —` cell after the header, `keys — view <k> · remote <k> · at <iso>`, from
  `claims.py card-keys`, resolved with `resolve_kit_file loop claims.py` as the card resolves the
  driver. Each cell is joined to one key by its class, declared once in `CARD_CELL_CLASSES` in
  `tools/loop/claims.py`: `overlaps —` and `claims —` are `remote`, every other cell is `view`. With no
  loop kit the cell reads `keys — skipped: no loop kit resolves in this tree`, and the card still
  writes. Observed by AC5, AC6.
- **S6** — The replay re-keys: `print_replay` recomputes the view key with `claims.py card-keys` in
  the session's own tree, the toplevel the replay runs in, and names that toplevel on its `now —`
  line. An equal key prints `keys view fresh`; a moved key re-writes the card fresh under
  `--card --replay` and prints `keys view re-derived`; the remote key is never recomputed, because a
  replay reads no remote, and prints `keys remote evidence`. Observed by AC7.
- **S7** — The run claims carry keys: `print_claims` in `tools/unattended/unattended.sh` adds a sixth
  TAB field to each row, the claim's key over its claim ref's sha and the run-state blob at that
  claim's run branch on the remote-tracking ref, so a claim and its run record are joined; the card's
  `derive_claims_line` (`skills/session-kickoff/manifest-check.sh:645`) reads six fields and prints
  the key's first eight hex digits on each row. Observed by AC8.
- **S8** — The leg `loop claims fixtures` in `tools/gate-legs.json`, running
  `python tools/loop/claims.py --fixture`, and the help line for the `keys —` cell in
  `skills/session-kickoff/SKILL.md`'s card section. Observed by AC1 to AC5, AC9.

## 3. Non-goals (OUT)

- The position engine that prints each claim it used: unit 7, which reads this unit's functions.
- Which session acts on a claim, the `next` command and the executor: dWellOiledMachine's.
- Leases and mailbox entries, two of the `remote` class's members: dPlacedRequest's and
  dWellOiledMachine's. The class is declared here; their claims join when those builds land them.
- Changing the driver's run-claim verdict table (live, held, unknown, stale, terminal) or the
  `RUN_CLAIMS` switch. The key is a sixth field beside the verdict, never a replacement for it.
- A per-cell key suffix on every card cell: the `tree —` cell is parsed by the scratch guard's deny,
  so the cells keep their bytes and one `keys —` cell carries the class keys (§8 F1).

### Edges

- **hands-off** `TOOL-dDeclaredLoop-7` — the claim key: `claims.py` with `derive_claim_key` and `derive_claim_verdict`, and the printed form `key <k> · <verdict>`, which the position engine prints for every claim it used
- **consumes-from** external — the driver's `--claims` verb and its stale bound (`tools/unattended/unattended.sh`), and the card's `resolve_kit_file`, both in the tree at base
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 22, 26, 39, 41, 43, 60, each a scope item of that unit

## 4. Design

### Evidence

- `--claims` prints one TAB row per claim, slug, node, status, beat age and verdict, through
  `print_claims`; it decides nothing and is dark while `RUN_CLAIMS` is off
  (`tools/unattended/unattended.sh:2194-2205`, dispatched at :14489).
- The card's `claims —` cell reads the driver's `--claims` and never re-derives; its awk accepts a row
  only at five fields (`skills/session-kickoff/manifest-check.sh:630-700`, the `NF == 5` test).
- The replay prints the stored card and one `now —` line from `derive_head_state` in the process's
  working tree (`skills/session-kickoff/manifest-check.sh:721-725`); the gap records it reading the
  primary tree instead of the session's worktree.
- A key over resolved inputs, never a file's bytes, is the repository's pattern:
  `derive_cache_key` (`tools/memory-tree/transition_audit.py:693-715`), a 16-hex SHA-1 over the inputs
  a cached delta depends on.
- The card already resolves a sibling kit's file and degrades to a `skipped:` cell when it is absent
  (`derive_claims_line`, `skills/session-kickoff/manifest-check.sh:648-650`).

### The two card keys

| Key | Sources | Read by |
|---|---|---|
| view | `commit=` the session tree's HEAD, `base=` the default branch's remote-tracking sha, and the tree's dirty count folded in as `dirty=<n>` | every cell but two |
| remote | each `refs/remotes/<remote>/*` and claim ref the `overlaps —` and `claims —` cells read, as `<ref>@<sha>` | `overlaps —`, `claims —` |

`card-keys` runs `git` in its own working directory and nowhere else, so the replay's view key is the
session tree's by construction. Its output is two lines, `view <k>` and `remote <k>`.

### The run-claim key

For a claim on slug `<s>` at ref `<r>`: `derive_claim_key` over `<r>@<sha>` and
`runstate=<blob>`, the blob of `memory/builds/<s>/RUN.md` at the claim's `run-branch:` on its
remote-tracking ref, or `runstate=?` when that branch or file is absent. A claim whose run record
moved after its beat keys differently from the one the card stored, which is the join `[trust]`
asks for between a claim and its run record.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `derive_claim_key`, `derive_claim_verdict`, `derive_card_keys` | function | `tools/loop/claims.py` |
| `CLAIM_CLASSES`, `CARD_CELL_CLASSES` | constant | `tools/loop/claims.py` |
| `key`, `verdict`, `card-keys`, `--fixture` | CLI verbs and flag | `tools/loop/claims.py` |
| `keys —` | card cell | `skills/session-kickoff/manifest-check.sh` |
| the sixth field of a `--claims` row | output field | `tools/unattended/unattended.sh` |
| `loop claims fixtures` | gate leg | `tools/gate-legs.json` |

### The fixture cases

`claims.py --fixture` builds repositories under `%TEMP%` with a short prefix; `--plant <case>` runs
one.

| Case | Plant | Outcome |
|---|---|---|
| `key-stable` | the same sources keyed twice | equal keys |
| `key-moves` | the base sha changed | different keys |
| `key-unread` | one source spelled `?` | no recomputation equals it |
| `typed-evidence` | a `typed` claim with equal keys | `evidence` |
| `remote-aged` | a `remote` claim with equal keys past its bound | `re-derived` |
| `card-keys-worktree` | a worktree whose HEAD differs from its primary's | the worktree's view key, not the primary's |

### Rollout

The card's `keys —` cell lands with the loop kit. A tree without it prints the skipped form, so an
adopter without the loop kit sees one new line and no failure.

### Files touched (estimate)

- `tools/loop/claims.py`
- `tools/loop/kit.toml`
- `tools/loop/README.md`
- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `skills/session-kickoff/SKILL.md`
- `tools/unattended/unattended.sh`
- `tools/unattended/VERBS.template.md`
- `tools/gate-legs.json`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **A per-cell key suffix.** It moves the bytes of the `tree —` cell, which the scratch guard's deny
  compares, and repeats one of two keys on twelve lines.
- **A key over the card file's bytes.** It moves with the written time on every write and says
  nothing about the inputs, which is what goes stale.
- **Re-deriving every cell on every replay.** It costs a kickoff per resume, the cost the card exists
  to avoid; the key decides which class moved.

## 5. Production-readiness checklist

- security — no new write path: the card and `--claims` already write and print these lines; the key
  is a digest of ref values and blob ids, carrying no secret.
- perf / scale — one Python spawn per card write and per replay, each a few `git rev-parse` calls; the
  `--claims` key costs one `git rev-parse <branch>:<path>` per claim.
- error / empty / loading states — an unreadable source keys as `?` and never compares equal; an
  absent loop kit prints the skipped form; an absent run record keys `runstate=?`.
- observability — the `keys —` cell and the replay's `now —` verdicts name each class's state.
- risks — a reader of `--claims` that counts fields: the card is the one in the tree and moves in
  this unit; `.claude/skills/unattended/SKILL.md` names the verb and no field count.
- testing — the fixture cases, a card render probe and a replay probe in a scratch worktree.
- migration — none; the card is rewritten at the next session start.
- user docs — the card section of `skills/session-kickoff/SKILL.md` and the `--claims` row of
  `tools/unattended/VERBS.template.md`; no page under `help/` describes the card's cells.

## 6. Acceptance criteria

- **AC1** — When `python claims.py --fixture --plant key-stable` and `--plant key-moves` run, the
  first prints two equal `k1:` keys and the second two different ones.
  Red when: a moved base keeps the key, or equal sources key differently.
- **AC2** — When `python claims.py --fixture --plant key-unread` runs, the key with a `?` source
  never equals a recomputation.
  Red when: an unread source compares equal.
- **AC3** — When `python claims.py --fixture --plant typed-evidence` runs, `verdict` prints
  `evidence` though the keys are equal.
  Red when: an actor-typed claim reads `fresh`.
- **AC4** — When `python claims.py --fixture --plant remote-aged` runs, `verdict` prints
  `re-derived`.
  Red when: a `remote` claim past its bound reads `fresh`.
- **AC5** — When `python claims.py --fixture --plant card-keys-worktree` runs, `card-keys` in the
  worktree prints the worktree's view key and differs from the primary's.
  Red when: the key is computed in the primary tree.
- **AC6** — When `bash skills/session-kickoff/manifest-check.sh --card --write --session <sid>` runs in
  the repository, the card carries one `keys — view k1:` line after its header; with the loop kit's
  `claims.py` hidden it carries `keys — skipped:` and still writes.
  Red when: the card has no `keys —` cell, or fails to write without the loop kit.
  fixture: a scratch clone under `%TEMP%`, where the loop kit can be removed.
- **AC7** — When `manifest-check.sh --card --replay --session <sid>` runs after a commit moved HEAD in
  a worktree, the `now —` line names the worktree's toplevel and prints `keys view re-derived`, and an
  unmoved tree prints `keys view fresh`.
  Red when: the replay prints `fresh` over a moved HEAD, or names the primary tree.
  fixture: a scratch clone with one worktree under `%TEMP%`.
- **AC8** — When `bash tools/unattended/unattended.sh --claims` runs in a scratch clone whose bare
  remote holds one run claim and `RUN_CLAIMS=on`, the row has six TAB fields, the sixth a `k1:` key,
  and the card's `claims —` row prints its first eight hex digits.
  Red when: the row keeps five fields, or the card refuses the six-field row.
  fixture: a bare remote and a clone under `%TEMP%`; the unattended kit's own suites are waived for
  this landing (README rule 8), so this probe is the observation.
- **AC9** — When `grep -n 'keys —' skills/session-kickoff/SKILL.md` runs, the card section names the
  cell and its two classes.
  Red when: the documentation omits the cell.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/loop/claims.py · covers AC1 AC2 AC3 AC4 AC5 · each `--plant` case, and `key-moves` red with the base left out of the canonical form · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC6 AC7 · a card written with the loop kit present and hidden, and a replay after a worktree commit · the suite's assertion floor raised by the arms added

## 8. Open questions

- **F1 — How do the card's cells carry their keys?** (a) One `keys —` cell with the two class keys,
  each cell joined to one by `CARD_CELL_CLASSES`; (b) a ` · key <k>` suffix on every cell. (b) moves
  the `tree —` cell the scratch guard's deny compares and repeats one key on most lines. (a) keeps
  every cell's bytes and still keys every cell by its class. Recommendation (a). Rung 3. RESOLVED
  (agent, 2026-10-24, delegated): (a). grants: PLAY-dClosedLoop-3 the card's new `keys —` cell ·
  widens: none · relaxes: none
- **F2 — Is age hashed into the key?** The `[trust]` record lists age among the key's inputs. Hashing
  a clock makes every recomputation differ, so no claim could read `fresh`. (a) Age stored beside the
  key and read by the class bound; (b) age hashed. Rung 1, `[trust]`'s rule that a remote claim is
  trusted "while their remote and clock keys match", a bound and not an equality. RESOLVED (agent,
  2026-10-24, delegated): (a). widens: none · relaxes: none
- **F3 — Does `--claims` change its verdict table to join the run record?** (a) A sixth field, the
  key over the claim ref and the run record, the verdict table unchanged; (b) a new verdict for a
  claim whose run record disagrees. (b) changes a dark verb's decisions, which no clause here names.
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-24, delegated): (a). grants:
  PLAY-dClosedLoop-3 the `--claims` row's sixth field · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md); no scope moved.

## 10. Reuse audit

The seams extended are the card's `derive_claims_line`
(`skills/session-kickoff/manifest-check.sh:645`), which reads one more field and keeps its single
call to the driver; `print_claims` (`tools/unattended/unattended.sh:2200`), which adds a field and
keeps its verdict table; `print_replay` (`skills/session-kickoff/manifest-check.sh:721`), which gains
the re-key; and the key-over-resolved-inputs pattern of `derive_cache_key`
(`tools/memory-tree/transition_audit.py:693`), followed rather than imported, because it keys a merge
walk and sits in the memory-tree kit. For the key and verdict primitive itself no existing seam fits:
`python tools/codebase-map/reuse_lookup.py "key a stored claim over the commit base and remote refs
and judge it fresh or stale"` ranked name-stem hits only (`key`, `claims`, `resolve_compare_base`),
none a claim key. The scout's citations, `--claims` at :14489 and `derive_claims_line` at :645,
agreed with source; the scout gave the card's no-re-derive comment as :630-644, and it runs :630-644
as cited.

Recall terms used: `python tools/memory-recall/query.py "how does a session tell a fresh card claim
from a stale one" --terms "card claims cell stale freshness key replay now line run claims verdict
live stale"`
