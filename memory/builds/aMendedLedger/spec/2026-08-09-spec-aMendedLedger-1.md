# TOOL-aMendedLedger-1 — finish the memory rework: drain the ledger, drive the merge, re-true the docs

**Status:** SPECCED · rev-1 · 2026-08-09 · node a · Tier-2 · base 663ca427 · streams tooling+playbook

## 1. Goal

Close the four items `TOOL-aFoldedQuarry-1` left open when it ported upstream `ARCH-dQuarriedLedger-1`,
so this repo's memory tree, its merge path and its governing docs describe the same system. The port
declared draining `<MEMORY_ROOT>/project/` out of scope in writing, and nothing has claimed it since.

## 2. Scope (IN)

- **S1** Relocate both journals under upstream's relocate-not-delete rule, and give `bThriftyBellows`
  the stub build folder its slug has no home for today.
- **S2** Retire the authored session ledger to `memory/archive/ledger/{a,b,c}.md` byte-identically,
  and remove the three `.md` stubs and two `.gitkeep` files that exist only to serve it.
- **S3** Make the hygiene gate match the drained tree, including a population guard so the emptied
  `project/` sub-lint cannot pass by selecting nothing.
- **S4** Resolve the `drift-audit` ledger probe, which is `gateable` and dies the moment
  `memory/project/in-flight/` empties.
- **S5** Port upstream U9: a row-keyed merge driver for `memory/DECISIONS.md` and
  `memory/backlog/*.md`, its `.gitattributes` entries, its per-node wiring, and its replay test.
- **S6** Re-true every governing doc this work falsifies, plus the doc claims already false today
  that contradict a BINDING rule.
- **S7** Close `PLAY-aPrunedCeremony-5`, whose subject retires with the ledger, and repair its dead
  build pointer in the same change.
- **S8** Record the decisions in `memory/DECISIONS.md`, including a row that supersedes the now-dead
  journal pointer at `:19` rather than editing an append-only record.

## 3. Non-goals (OUT)

- **Node-specific backlogs.** Upstream never adopted them; its five shards are FAMILY shards exactly
  like this repo's four. S5 is upstream's actual answer to backlog merge conflicts.
- **`merge=union`.** Upstream measured it introducing a duplicate in 147 of 151 `DECISIONS.md`
  conflicts. Rejected with evidence, not preference.
- **Deleting any journal or ledger shard.** See §4 Migration.
- **Re-homing the five waiver registries.** See §4 Alternatives rejected — the evidence reversed the
  recommendation this unit opened with.
- **Editing any ratified id or any append-only record.** `memory/DECISIONS.md` is appended to, never
  rewritten.
- **Fixing the codebase-map prefixed-install defect.** Recorded in `memory/map/features/codebase-map.md`
  §Gaps and spun off; it is a kit-engine change with its own adopter blast radius.
- **`memory/HYGIENE.md` rule 5's wider vacuity sweep.** S3 guards the one population this unit
  empties. `tools/memory-recall/extract.py:104-108` `DURABLE` is separately vacuous today (matches 0
  of 131 tracked files, a pre-flatten shape); it is named here so it is not re-discovered, and left
  to its own unit.

## 4. Design

### Inventory

Measured at `663ca42` by the research pass, re-measured where the codebase-map adoption on this
branch (`f9cf666`) moved a number. `git ls-files memory/project` → **15 tracked paths, 13 non-empty,
13 400 B total**. Upstream moved 118 loose files, 129 journals and 9 ledger shards; this repo has 13
files. Any plan shaped like a bulk migration is mis-sized.

| population | count | today |
|---|---|---|
| journals | 2 | `memory/project/journal/*.md` |
| live ledger shards | 3 | `memory/project/in-flight/{a,b,c}.md`, 11 data rows |
| `.md` stubs | 3 | `IN-FLIGHT.md`, `MEMORY.md`, `README.md` |
| `.gitkeep` | 2 | under `in-flight/` and `journal/` |
| waiver registries | 5 | `*.txt`, read by three gates and the drift kit |

Three of the five registries hold **zero data rows** today. Every reader treats "file missing" and
"file present and empty" identically, so a move that forgets to repoint them is indistinguishable
from a correct move until someone adds the first row. That is why §4 Alternatives rejected matters.

Ledger state, measured: **every sha named anywhere in the 11 rows is an ancestor of `origin/main`.
Zero rows describe unlanded work.** Nine of eleven slugs are fully represented in the generated
`memory/LIVE.md` / `memory/ledger/<month>.md`; where an authored row and the derived index disagree,
the derived index is right in every case.

### Data model

The merge driver treats a file as **three regions** — preamble, row block, trailer — and key-merges
only the row block. The split is load-bearing, not a refinement: `memory/DECISIONS.md` opens with a
title, a bolded rotation note and routing prose, so an unconditional "a line the grammar cannot key
conflicts" rule conflicts on every merge and the auto-resolve is unreachable.

A row is its lead-in plus its anchor. The anchor grammar is imported from
`tools/memory-recall/extract.py`, never vendored — that file's four anchor regexes are already
byte-identical to upstream's, and its `grammar_for(root)` reads `FAMILIES` from `.memory-tree.conf`,
which is what makes the driver work in an adopting repo with different families.

| case | result |
|---|---|
| id in `%B` only | append |
| id in `%A` only | keep |
| id in both, text identical | keep once |
| id in both, one side equals `%O` | take the side that changed |
| id in both, both changed | CONFLICT with markers |
| id in `%O` and one side, other side untouched | honour the delete |
| id deleted one side, MODIFIED the other | CONFLICT, both directions |
| preamble / trailer | ordinary three-way text merge |

Two rows above correct the upstream spec, which the shipped upstream code contradicts: the delete
case splits five ways rather than two, and the specced "unkeyable line inside the row block →
CONFLICT" is not implemented — the line attaches to the following anchor and upstream's own fixture
asserts exit 0 with position preserved. **The code is the authority; AC7 is worded from the code.**

Failure is closed: any exception becomes a whole-file conflict rather than a silent take-ours, and
the grammar import is deferred into the anchor call so an unreadable `extract.py` lands in that
handler instead of exiting before `%A` is written. Bytes are written with `write_bytes` — `write_text`
retranslates newlines on Windows.

### Migration

Per-file destinations. Upstream's transferable lesson is that a spec must carry a per-file map, not a
count: "no migration can derive a destination from a count."

| path | destination | why |
|---|---|---|
| `journal/2026-07-16-bThriftyBellows.md` | `memory/builds/bThriftyBellows/build/2026-07-16-build-bThriftyBellows-1.md` (new stub folder) | **sole carrier** of the 9-bullet optimization inventory, the three-target golden-diff protocol, `2647.5s → 33.9s`, and the banked negative result "cache-and-grep is SLOWER" |
| `journal/2026-07-15-aRuledParchment.md` | `memory/builds/aRuledParchment/build/2026-07-15-build-aRuledParchment-1.md` | build exists; two facts are sole-carried (template size at edit, upstream review provenance) |
| `in-flight/{a,b,c}.md` | `memory/archive/ledger/{a,b,c}.md`, byte-identical `git mv` | status content is redundant and where it differs it is wrong, but worktree names, `wf_*` review ids and session narrative are sole-carried |
| `IN-FLIGHT.md` | delete; its protocol prose moves to `memory/archive/ledger/README.md` | its only durable content is the vocabulary, which retires with the ledger |
| `MEMORY.md` | delete, after its digest folds into the relocated journal's header | one entry, duplicating `memory/DECISIONS.md:19` |
| `project/README.md` | delete | describes only files that are moving, and already omits the five registries |
| `in-flight/.gitkeep`, `journal/.gitkeep` | delete with their directories | 0 B |
| the five `*.txt` | **stay at `memory/project/`** | see Alternatives rejected |

`memory/DECISIONS.md:45` states that the bThriftyBellows measurement "lives in the bug-class
catalogue". Measured: `memory/gotchas/` has zero hits for it. **That claim is false and the journal is
the only copy.** The record is append-only, so S8 appends a correcting row rather than editing it.

Relocated journals are named `<date>-build-<slug>-<seq>.md`. Upstream's `-journal` suffix is illegal
here: `check-memory-hygiene.sh:255` allows nothing after `<seq>`.

The stub folder needs a `README.md` with front matter **and** a spec carrying a parseable
`**Status:**` header, or `gen_build_index.py` errors by name — a `build/` recording alone gives it no
status. Adding it also writes a row into `memory/ledger/2026-07.md`, a generated-file diff.

### Rollout

Order is a dependency chain, not a preference. **U2 and U4 must be one commit**: draining
`in-flight/` kills a `gateable` drift signal, so any gap between them is a red bar.

| unit | work | must precede |
|---|---|---|
| U1 | journals relocate; `bThriftyBellows` stub build folder; regenerate the build index | U2 |
| U2+U4 | ledger to `archive/ledger/`; stubs deleted; `signal_ledger` resolved; `drift-audit-state.js` ledger glob repointed; drift selftest fixtures | U3 |
| U3 | hygiene gate matches the drained tree; `pop_guard` over `project/`; kit 1.7 → 1.8; `HYGIENE.md` + template parity; `adopt-memory-tree.sh` stops scaffolding the machinery; hygiene test fixtures | U6 |
| U5 | the merge driver, its wiring, its replay test, its gate leg | — |
| U6 | doc truth across nine files | — |
| U7 | `PLAY-aPrunedCeremony-5` → WONTDO + pointer repair; `memory/DECISIONS.md` rows | last |

### Files touched (estimate)

Gates and kit: `check-memory-hygiene.sh` (13 decider sites), `check-memory-hygiene.test.sh`,
`hygiene-parity.test.sh`, `adopt-memory-tree.sh`, `drift_signals.py`, `drift_report.py`,
`drift-audit/selftest.py`, `tools/workflows/drift-audit-state.js`, `tools/check-wiring.sh`,
`tools/gate-legs.json`, `.gitattributes`. New: `tools/memory-tree/merge-rows.py`,
`tools/memory-tree/merge-rows.test.sh`, `memory/archive/ledger/README.md`.
Docs: `AGENTS.md`, `.claude/SESSION-KICKOFF.md`, `parallel-coding-governance.template.md`,
`README.md`, `WIRE-INTO-PROJECT.md`, `memory/README.md`, `memory/HYGIENE.md`,
`tools/memory-tree/HYGIENE.template.md`, `tools/memory-tree/README.md`.

Three budgets constrain the doc work and each is one-sided: the template's **22 free bytes** of its
32 768 gate, the read-path ceiling, and the kit/dogfood parity pair that forces every `memory/HYGIENE.md`
edit into `HYGIENE.template.md` in the same commit.

### Alternatives rejected

**Re-homing the five waiver registries — rejected on evidence, reversing this unit's opening
recommendation.**

- *Into `tools/memory-tree/`*: `WIRE-INTO-PROJECT.md:394` tells adopters to overwrite kit files
  wholesale on a kit update. Putting adopter DATA — their waivers, their pin — inside a kit directory
  means a kit update deletes their registries. Upstream's `scripts/` is not a copied kit dir, so
  upstream's placement does not transfer.
- *Into a new `memory/registry/`*: every already-adopted repo's `memory/project/*.txt` becomes an
  unexpected entry under check 3 while the new paths do not exist, so their grandfather lists
  silently empty. `adopt-memory-tree.sh` refuses to touch an already-scaffolded tree, and the kit
  ships no migration script.

Keeping them where they are costs one prose correction — `memory/HYGIENE.md:81` currently calls
`memory/project/` session machinery, and after this unit it holds only registries.

**Deleting the ledger shards** is rejected for the reason upstream reversed its own spec at build
time: the shards are the only source for live-cited ids and session narrative, and rev-6 of upstream's
U7 records them as "RELOCATED, not deleted".

## 5. Production-readiness checklist

- security — N/A. No auth, egress or sanitization surface; the merge driver reads three local blobs.
- perf / scale — the driver runs per conflicted file during a merge; upstream measured it over 765
  merges with no perf note. The hygiene gate's runtime is unchanged (no new walk).
- a11y — N/A. No user interface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — the driver's empty-anchor case (no anchors → everything is
  preamble) and its fail-closed exception path are both fixture-covered by AC7.
- observability — `drift_report.py` is the instrument; S4 must leave it able to move, not merely
  silent. A signal that cannot move prints DEAD PROBE by design.
- risks — **data-loss is the live risk**, in two places: a `git mv` that is not byte-identical, and a
  merge driver that drops a row. AC2 and AC7 are the controls. Rollback is `git revert`; no external
  state changes.
- testing + left-shift gates — one new gate leg (the driver's replay test); every edited gate keeps
  its `fail` branches armed or pinned.
- migration / rollback — one repo, no adopters migrate: the drained files are this repo's own. The
  adopter-facing change is that the kit stops scaffolding a ledger, which §8 F2 asks about.
- user docs — S6 is the doc work; `WIRE-INTO-PROJECT.md` is the adopter-facing surface.

## 6. Acceptance criteria

- **AC1** When `git ls-files memory/project` is run after U3, it lists exactly the five `*.txt`
  registries and nothing else.
- **AC2** When `git log --follow --find-renames` is run over each of `memory/archive/ledger/{a,b,c}.md`,
  each shows the rename from `memory/project/in-flight/` with a 100% similarity index, and
  `git diff <base> -- <old> <new>` shows no content change.
- **AC3** When `python tools/memory-tree/gen_build_index.py --check` is run after U1, it exits 0 and
  `memory/builds/bThriftyBellows/README.md` carries a derived status.
- **AC4** When `memory/project/` is emptied of session machinery and the `project/` structure sub-lint
  is run over a tree containing a stray file, check 3 still reports it — proving the sub-lint was
  guarded rather than left to select an empty population.
- **AC5** When `python tools/drift-audit/drift_report.py --check` is run after U2+U4, it exits 0 and
  no signal reports `DEAD PROBE` for a `gateable` signal.
- **AC6** When `git check-attr merge -- memory/DECISIONS.md memory/backlog/TOOL.md` is run, each
  reports `merge: rows`.
- **AC7** When `bash tools/memory-tree/merge-rows.test.sh` is run, it passes fixtures covering:
  disjoint appends, the same id edited both sides, a row deleted one side and untouched the other, a
  row deleted one side and modified the other, an unkeyable line inside the row block, and a file
  with no anchors at all.
- **AC8** When a two-branch merge is constructed where each branch appends a distinct row to
  `memory/backlog/TOOL.md`, the merge auto-resolves with both rows present and no duplicate id.
- **AC9** When `grep -rn "memory/project/in-flight\|IN-FLIGHT.md" AGENTS.md .claude/SESSION-KICKOFF.md
  parallel-coding-governance.template.md WIRE-INTO-PROJECT.md memory/README.md memory/HYGIENE.md` is
  run after U6, it returns no hit that describes the ledger as live.
- **AC10** When `bash tools/run-gates.sh` is run at the end of every unit's commit, it is green.
- **AC11** When `memory/backlog/PLAY.md` is read after U7, `PLAY-aPrunedCeremony-5` leads with
  `WONTDO` and its pointer resolves to `memory/builds/aPrunedCeremony/`.

## 7. Gates

Existing legs that must stay green: `bash tools/run-gates.sh` in full (38 legs at `f9cf666`).
Specifically load-bearing here — `memory hygiene`, `harness arms`, `verdict epoch` + its self-test,
`kit/dogfood doc parity`, `build-index selftest`, `corpus-ids selftest`, `check-arms selftest`,
`drift-audit records` + `selftest`, `kickoff-manifest ratchet`, `codebase-map coverage + freshness`.

New leg: `bash tools/memory-tree/merge-rows.test.sh`, added to `tools/gate-legs.json` — the runner
single-sources its legs from that manifest and `tools/run-gates.test.sh` forbids a hardcoded leg
command.

Three couplings a builder will otherwise discover the hard way:

1. **Any non-comment change to `check-memory-hygiene.sh` forces `KIT_MEMORY_TREE_VERSION`** (now 1.7,
   bumped by the codebase-map adoption) to move in the same diff, in three places, plus a `--render`.
2. **`.memory-tree.conf` and `tools/gate-legs.json` are WATCHED paths** in the kickoff manifest, so
   any unit touching them must re-stamp `last-audit` in the same commit. Stamp from `date`, not by
   hand — the previous stamp was written 6.5 h ahead of the node clock.
3. **Every new gate leg pushes `handkept_inventories_disagreeing_with_source` up by one** unless
   `AGENTS.md`'s gate-suite section gains a bullet citing that leg's argv script path. The signal
   matches on the argv path, not the display name.

Run `python tools/memory-tree/gotchas.py --for-diff 663ca42..HEAD` before the review, not after.
The classes this diff can hit are named in §10.

## 8. Open questions

- **F1 — the `F:*.md` catch-all at `check-memory-hygiene.sh:229`.** With the machinery gone it is
  what would let a stray `.md` creep back into `project/`. Tightening it turns two of the hygiene
  test's own fixtures (`kickoff-prompt.md`, `links.md`) into check-3 findings, and there is no
  `cnot 3` for them — so the self-test would stay green while its fixtures changed meaning.
  **Recommendation: tighten it to the five registry names and repoint the two fixtures in the same
  commit**, because a catch-all guarding a directory that should hold only registries is the hole.
- **F2 — does the kit keep scaffolding a session ledger for ADOPTERS?** Dropping it from
  `adopt-memory-tree.sh` while check 3 stops admitting `IN-FLIGHT.md` / `in-flight/` / `journal/`
  makes an adopter who kept the sharded ledger go red on their next hygiene run, and that contract is
  stated to them in `WIRE-INTO-PROJECT.md:119` and `:389`. **Recommendation: retire it for adopters
  too, in the same version bump, and say so in the runbook** — two shapes for one question is the
  defect this whole unit is closing. Needs the owner, because it is a breaking kit change.
- **F3 — `signal_ledger`'s fate.** Three exits: delete it (upstream did, but 17 selftest references
  and 4 named assertions ride it); add it to `DECLARED_EMPTY` and retire its pin of 4; or repoint it
  at `memory/archive/ledger/` (where the pin would then read 4 forever and the "drain it" ratchet
  becomes permanent). **Recommendation: `DECLARED_EMPTY` + retire the pin**, which the code
  explicitly sanctions and which keeps the selftest's assertions meaningful.
- **F4 — `adopt-memory-tree.sh` scaffolds 2 of the 5 registries.** `id-orphan-waiver.txt`,
  `corpus-path-unresolved.txt` and `unarmed-branches.txt` are named by three gates and created by
  none, so a fresh adopter who arms `ORPHAN_ID_PIN` reds with a message pointing at a file the kit
  never wrote. Pre-existing, adjacent, cheap. **Recommendation: close it in U3** — the same function
  is already being edited.

## 9. Revision log

- rev-1 · 2026-08-09 · initial draft. Grounded on upstream `ARCH-dSiftedGranary-1` and
  `ARCH-dQuarriedLedger-1` (units U4, U6, U6a, U7, U9) read in `C:/projects/incms/main`, and on a
  six-lens measured sweep of this repo. Two owner premises corrected in §3: upstream never adopted
  node-specific backlogs, and memory-recall is both wired here and documented in
  `WIRE-INTO-PROJECT.md` §3c. The registry re-home recommendation was REVERSED against the evidence
  in §4 Alternatives rejected.

## 10. Reuse audit

`reuse_lookup.py` over the newly-populated map returns, for "three-way merge index rows keyed by
record id": `records` (`tools/memory-tree/gotchas.py`, fan-in 6, SEAM) and `merge`
(`tools/settings-merge.py`, fan-in 5, SEAM). Neither fits — `gotchas.records` parses front matter and
`settings-merge.merge` does a recursive dict union for JSON settings, not a three-way text merge with
conflict markers.

The seam this unit DOES wire through is `tools/memory-recall/extract.py`'s anchor grammar, imported
rather than reimplemented, which is the single-source rule upstream's driver already follows. That is
the reuse decision: **no seam fits for the merge itself; the grammar is reused and must not be
vendored.**

Two caveats stated rather than hidden. The map's corpus is `bash`-recall-dark, and this repo's gates
are bash — a shell seam cannot appear in that shortlist. And 69 of 71 inventory keys are still
baselined, so the map ratchets coverage without yet describing the system. Both are recorded in
`memory/map/features/codebase-map.md` §Gaps.
