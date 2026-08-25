# TOOL-aMendedLedger-1 — finish the memory rework: drain the ledger, drive the merge, re-true the docs

**Status:** SPECCED · rev-5 · 2026-08-09 · node a · Tier-2 · base 663ca427 · streams tooling+playbook · ratified 2026-08-09

> **rev-5** — §4's U5 decision table is amended from the shipped code, in both places it appears
> (here and in the U5 sub-spec). `| id in %B only | append |` was ratified and is WRONG: measured
> against git's own three-way merge, appending an incoming row past the row block files it under
> whatever `## FAMILY` heading happens to be last. Two review rounds reproduced silent corruption of
> `memory/DECISIONS.md` at rc 0 through that rule and the first two repairs of it. The table below
> now states the splice, its `%A`-only skip, and the two POSTCONDITIONS that judge what a splice
> cannot decide. A ratified table that no longer describes the code is the exact drift class this
> repo gates for, so the rule change is recorded here and not only in a commit message.

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-10-build-TOOL-aMendedLedger-1-1-driver-repro-corpus.md](../build/2026-08-10-build-TOOL-aMendedLedger-1-1-driver-repro-corpus.md) | journal | TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 |
| [2026-08-09-review-TOOL-aMendedLedger-1-1-closing-diff.md](../reviews/2026-08-09-review-TOOL-aMendedLedger-1-1-closing-diff.md) | diff-review | TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 |
| [2026-08-09-review-TOOL-aMendedLedger-1-2-repair.md](../reviews/2026-08-09-review-TOOL-aMendedLedger-1-2-repair.md) | diff-review | TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 |
| [2026-08-09-review-TOOL-aMendedLedger-1-3-regression.md](../reviews/2026-08-09-review-TOOL-aMendedLedger-1-3-regression.md) | diff-review | TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 |
| [2026-08-10-review-TOOL-aMendedLedger-1-4-u9-redesign.md](../reviews/2026-08-10-review-TOOL-aMendedLedger-1-4-u9-redesign.md) | diff-review | TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 |

<!-- /gen:spec-records -->

## 1. Goal

Close the four items `TOOL-aFoldedQuarry-1` left open when it ported upstream `ARCH-dQuarriedLedger-1`,
so this repo's memory tree, its merge path and its governing docs describe the same system. The port
declared draining `<MEMORY_ROOT>/project/` out of scope in writing, and nothing has claimed it since.

## 2. Scope (IN)

- **S1** Relocate both journals under upstream's relocate-not-delete rule, give `bThriftyBellows` the
  stub build folder its slug has no home for, and delete the three `.md` stubs in the same commit.
- **S2** Retire the authored session ledger to `memory/archive/ledger/{a,b,c}.md` byte-identically.
- **S3** Make the hygiene gate match the drained tree, including a selector-integrity guard so a
  mis-segmented `project/` path expression reds instead of reporting nothing.
- **S4** Resolve the `drift-audit` ledger probe, which is `gateable` and dies the moment
  `memory/project/in-flight/` empties.
- **S5** Port upstream U9: a row-keyed merge driver for `memory/DECISIONS.md` and
  `memory/backlog/*.md`, its launcher shim, its `.gitattributes` entries, its per-node `git config`
  wiring, and its replay test.
- **S6** Re-true every governing doc this work falsifies, in both layers: this repo's own docs, and
  the adopter-facing product docs, which the owner ratified as **retire everywhere** (F2, F5).
- **S6b** Ship the adopter upgrade note that retirement obliges. Retiring the ledger in the product
  is a breaking change for an adopter still carrying one, and it must not land silently.
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
- **Re-homing the five waiver registries.** See §4 Alternatives rejected.
- **Editing any ratified id or any append-only record.** `memory/DECISIONS.md` is appended to.
- **Fixing the codebase-map prefixed-install defect.** Recorded in `memory/map/features/codebase-map.md`
  §Gaps and spun off; it is a kit-engine change with its own adopter blast radius.
- **A repo-wide vacuity sweep.** S3 guards the one population this unit touches.
  `tools/memory-recall/extract.py:104-108` `DURABLE` is separately vacuous today — its regex requires
  a pre-flatten `memory/<x>/…` shape and matches 0 of 131 tracked files. Named here so it is not
  re-discovered, and left to its own unit.
- **Any fix outside the units below.** `check-memory-hygiene.sh:346`'s `ex7` rewrite was OUT at rev-2
  pending F6; F6 is now resolved and the fix is IN, in U3.

## 4. Design

### Inventory

Measured at `663ca427`, re-measured at `f9cf666` where the codebase-map adoption moved a number.
`git ls-files memory/project` → **15 tracked paths, 13 non-empty, 13 400 B**. Upstream moved 118 loose
files, 129 journals and 9 ledger shards; this repo has 13. Any plan shaped like a bulk migration is
mis-sized.

Three of the five registries hold **zero data rows**. Every reader treats "file missing" and "file
present and empty" identically, so a move that forgets to repoint one is indistinguishable from a
correct move until someone adds the first row. That asymmetry drives §4 Alternatives rejected.

Ledger state: **every sha named in the 11 rows is an ancestor of `origin/main`. Zero rows describe
unlanded work.** Nine of eleven slugs are already in the generated `memory/LIVE.md` /
`memory/ledger/<month>.md`; where an authored row and the derived index disagree, the derived index is
right in every case.

### Data model

The merge driver treats a file as **three regions** — preamble, row block, trailer — and key-merges
only the row block. The split is load-bearing: `memory/DECISIONS.md` opens with a title, a bolded
rotation note and routing prose, so an unconditional "a line the grammar cannot key conflicts" rule
conflicts on every merge and the auto-resolve is unreachable.

A row is its lead-in plus its anchor. The anchor grammar is imported from
`tools/memory-recall/extract.py`, never vendored — that file's four anchor regexes are already
byte-identical to upstream's, and its `grammar_for(root)` reads `FAMILIES` from `.memory-tree.conf`,
which is what makes the driver work in an adopting repo with different families.

| case | result |
|---|---|
| id in `%B` only | SPLICE after the last surviving key preceding it in `%B`, and after the `%A`-only keys already following that key — never append past the block |
| id in `%A` only | keep, in the position `%A` gave it |
| id in both, text identical | keep once |
| id in both, one side equals `%O` | take the side that changed |
| id in both, both changed | CONFLICT with markers |
| id in `%O` and one side, other side untouched — *row* untouched, i.e. lead-in AND anchor | honour the delete |
| id deleted one side, MODIFIED the other — including content filed ADJACENT to it | CONFLICT, both directions |
| a line the grammar cannot key, inside the row block | attaches to the FOLLOWING anchor, rc 0 |
| preamble / trailer | ordinary three-way text merge |
| **postcondition** — a row line, or the id a row LEADS with, written more often than any one input carries it | REFUSE (whole-file conflict) |
| **postcondition** — a row filed under a `#` heading no input filed it under | REFUSE (whole-file conflict) |

The last four rows correct the upstream *spec* from the shipped upstream *code*: the delete case splits
five ways rather than two, and the specced "unkeyable line → CONFLICT" is not implemented — upstream's
own fixture asserts rc 0 with position preserved. **The code is the authority.**

**Why the `%B`-only rule is a splice and not an append (rev-5).** Appending was ratified from
upstream and is a REGRESSION against the merge it replaces: `memory/DECISIONS.md` says of itself
"Grouped by family for reading", and git's own three-way merge places the same incoming row in the
right section on inputs where the append rule does not. The `%A`-only skip is the second half of the
same defect — without it, ours' newly appended row lands under the `## FAMILY` heading theirs' new row
carries as its lead-in. And because no splice rule can be right in every shape, the two postconditions
are the terms that make the table SAFE rather than merely better: whatever the placement rule cannot
decide, the driver refuses instead of guessing. A conflict is an acceptable outcome for an
append-only record; silently wrong content never is.

Failure is closed: any exception becomes a whole-file conflict rather than a silent take-ours, the
grammar import is deferred into the anchor call so an unreadable `extract.py` lands in that handler
instead of exiting before `%A` is written, and bytes go out via `write_bytes` — `write_text`
retranslates newlines on Windows.

**The wiring is one literal command**, and it needs a shim this repo does not have:

```bash
git config merge.rows.driver 'bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py %O %A %B %P'
```

`git ls-files | grep -i pyrun` returns nothing here, and `tools/lib/resolve-python.sh` is
source-and-call — `resolve_python()` prints a name and returns, it executes nothing. Git never goes
through `run-gates.sh`, so `$PYBIN` substitution does not reach it. **New file `tools/lib/pyrun.sh`**:
source the resolver, then `PY=$(resolve_python) || exit 2; exec "$PY" "$@"`. Hardcoding `python`
instead is the MS-Store-stub failure the resolver exists for and is banned repo-wide by
`tools/lib/resolve-python.test.sh:114-152`.

**The selector-integrity guard for S3**, stated as the call the builder writes:

```bash
PRE_REGISTRY=$(printf '%s\n' "$FILES" | grep -cE '\.txt$')
pop_guard 3 "no registry under $M/project/" \
  "$(printf '%s\n' "$FILES" | grep -cE "^$M/project/[^/]+\.txt$")" "$PRE_REGISTRY"
```

`pop_guard` fires only when the population is 0 and the precondition is > 0, so the precondition must
be an **un-segmented** count — the one shape that can differ from the population when the path
expression is wrong. `project/` after this unit is *drained of session machinery*, not emptied: the
five registries stay, so the population is 5 and the guard's job is catching a mis-segmented selector,
not an empty directory.

### Migration

Per-file destinations **and the unit that performs each**. Upstream's transferable lesson is that a
spec must carry a per-file map, not a count: "no migration can derive a destination from a count."

| path | unit | destination | why |
|---|---|---|---|
| `journal/2026-07-16-bThriftyBellows.md` | U1 | `memory/builds/bThriftyBellows/build/2026-07-16-build-bThriftyBellows-1.md` (new stub folder) | **sole carrier** of the 9-bullet optimization inventory, the golden-diff protocol, `2647.5s → 33.9s`, and the banked negative result "cache-and-grep is SLOWER" |
| `journal/2026-07-15-aRuledParchment.md` | U1 | `memory/builds/aRuledParchment/build/2026-07-15-build-TOOL-aRuledParchment-1-1.md` | build exists; two facts are sole-carried |
| `MEMORY.md` | U1 | delete, after its digest folds into the relocated journal's header | its line 4 links INTO `journal/`; see the atomicity rule below |
| `IN-FLIGHT.md` | U1 | delete; its protocol prose moves to `memory/archive/ledger/README.md` | its only durable content is the vocabulary, which retires with the ledger |
| `project/README.md` | U1 | delete | describes only files that are moving, and already omits the five registries |
| `in-flight/{a,b,c}.md` | U2 | `memory/archive/ledger/{a,b,c}.md`, byte-identical `git mv` | status content is redundant and where it differs it is wrong, but worktree names, `wf_*` review ids and session narrative are sole-carried |
| `in-flight/.gitkeep`, `journal/.gitkeep` | U1 (journal), U2 (in-flight) | delete with their directories | 0 B |
| the five `*.txt` | — | **stay at `memory/project/`** | see Alternatives rejected |

**Atomicity rule, general:** no commit may leave a `memory/**.md` relative link pointing at a path
that same commit moved. Hygiene check 2 is full-tree at the push boundary, not diff-scoped, and
`legacy-files.txt` does not grandfather `MEMORY.md`. That is why the three `.md` deletions sit in U1
beside the journal move rather than in U2.

`memory/DECISIONS.md:45` states that the bThriftyBellows measurement "lives in the bug-class
catalogue". Measured: `memory/gotchas/` has zero hits. **That claim is false and the journal is the
only copy.** The record is append-only, so S8 appends a correcting row.

**The stub build folder gets a `README.md` and NO spec.** Front matter carries `slug: bThriftyBellows`,
`node: b`, `opened: 2026-07-16`, `streams: tooling`, `roster: TOOL`,
`ids: TOOL-bThriftyBellows-1/-2`, plus an authored **`status: CLOSED`** and the
`<!-- gen:build-index -->` marker pair. `gen_build_index.py:185-193` sanctions the authored-status
route when no spec carries a header, and `:194-199` makes a spec header alongside `status:` a hard
error. Authoring a spec instead would fabricate provenance for work that shipped on 2026-07-16.
Because `opened` is a July date, a row is also written into `memory/ledger/2026-07.md`.

Relocated journals are named `<date>-build-<slug>-<seq>.md`. A `-journal` tail would be **legal** —
check 5 at `:294` interpolates `REC_TAIL` (`:109`) — and the plain form is chosen only so the name
matches every other recording in the tree. Check 4's `rre` at `:255` does not govern this: it builds
`F:` entries for direct children of `builds/<slug>/` only.

### Rollout

Order is a dependency chain. **U2 and U4 must be one commit**: draining `in-flight/` kills a
`gateable` drift signal, so any gap between them is a red bar.

| unit | work | stages a WATCHED path? |
|---|---|---|
| U1 | journals relocate; stub build folder; the three `.md` stubs deleted; build index regenerated | no |
| U2+U4 | ledger to `archive/ledger/` (its README is created in U1, per the Migration table — U2 must not re-create it); `signal_ledger` resolved per F3; the ledger lens deleted from `drift-audit-state.js`; drift selftest fixtures | no |
| U3 | hygiene gate matches the drained tree; the `pop_guard` call above; check 6's arm re-fixtured; kit 1.7 → 1.8; `HYGIENE.md` + template parity; `adopt-memory-tree.sh` stops scaffolding the ledger AND check 3 stops admitting it; hygiene test fixtures | **yes** — `check-memory-hygiene.sh` |
| U5 | `pyrun.sh`; the merge driver; `.gitattributes`; `check-wiring.sh` case; replay test; gate leg | **yes** — `tools/gate-legs.json` |
| U6 | doc truth; the template edit above; the S6b upgrade note | **yes** — `parallel-coding-governance.template.md` |
| U7 | `PLAY-aPrunedCeremony-5` → WONTDO + pointer repair; `memory/DECISIONS.md` rows | no |

Both forks that gated U3 and U6 are resolved (§8 F2, F5: retire everywhere), so no step now waits on
an answer. U3 carries the whole retirement in the kit layer — scaffolder and gate together — because
scaffolding a shape the gate rejects, or rejecting a shape the scaffolder writes, is a red bar in
either direction.

### Files touched (estimate)

Gates and kit: `check-memory-hygiene.sh` (13 decider sites), `check-memory-hygiene.test.sh`,
`hygiene-parity.test.sh`, `adopt-memory-tree.sh`, `drift_signals.py`, `drift_report.py`,
`drift-audit/selftest.py`, `tools/workflows/drift-audit-state.js` (`:38`, `:52`, the `${LEDGER}`
clause at `:60`, the paragraph at `:178`), `tools/check-wiring.sh`, `tools/gate-legs.json`,
`.gitattributes`.
**New:** `tools/lib/pyrun.sh`, `tools/memory-tree/merge-rows.py`,
`tools/memory-tree/merge-rows.test.sh`, `memory/archive/ledger/README.md`.
Docs: `AGENTS.md`, `.claude/SESSION-KICKOFF.md`, `parallel-coding-governance.template.md`,
`README.md`, `WIRE-INTO-PROJECT.md`, `memory/README.md:23`, `memory/HYGIENE.md:5, :28, :60-61, :74,
:81, :93`, `tools/memory-tree/HYGIENE.template.md` (parity mirror), `tools/memory-tree/README.md`.

`memory/HYGIENE.md:81` carries a separate defect worth landing with F4: "Two plain sorted path lists
in `memory/project/`" is stale at five registries.

**The template edit, stated line by line** (F5 resolved: retire). Byte counts measured on the
LF-normalised file, which is 32 746 of 32 768 with **22 free**:

| lines | action | bytes |
|---|---|---|
| `:86-88` | **delete** — the shard rule, the row shape, and the `{in-flight \| merged:<sha>}` vocabulary | −954 |
| `:31` | rewrite: the Locate step reads the decision log + backlog and the GENERATED build index, not the ledger | ~−40 |
| `:68` | rewrite: the slug-collision scan keeps its all-time grep and its live-row scan, now over the generated index | ~−60 |
| `:101` | rewrite: keep "never a shared mutable index every session edits… append-only or generated", drop the per-node-ledger clause | ~−120 |
| `:102` | rewrite: status lives in the generated build index, not the ledger | ~−60 |
| `:211` | rewrite: the wrap-up writes build front matter and shas, not a ledger row | ~−30 |

The deletion at `:86-88` is what makes the rest affordable: it frees roughly a kilobyte against a
22-byte margin, so U6's other corrections fund themselves. **`:101`'s surviving clause is the point
of the change** — a shared mutable index is still forbidden; the answer is now a generated index plus
S5's row-keyed driver for the two indexes that must stay authored, rather than sharding by node.

**S6b, the upgrade note.** `WIRE-INTO-PROJECT.md` gains a short migration section: the sharded
authored ledger is retired at kit 1.8; an adopter carrying one moves its shards to
`<MEMORY_ROOT>/archive/ledger/` and gets its work state from `gen_build_index.py` instead, which
requires build README front matter. Measured on the one adopter found on this node (`swydee`): it
runs kit **1.4** on a pre-flatten tree with three live rows, no `LIVE.md`, no `ledger/` and zero
build READMEs carrying front matter — so for that repo the note is a prerequisite list, not a
one-liner, and the migration itself is its own unit in its own repo.

Three budgets constrain the doc work, each one-sided: the template's 22 free bytes (relieved by the
deletion above), the read-path ceiling, and the kit/dogfood parity pair that forces every
`memory/HYGIENE.md` edit into `HYGIENE.template.md` in the same commit via `--render`.

### Alternatives rejected

**Re-homing the five waiver registries — rejected, reversing this unit's opening recommendation.**

- *Into `tools/memory-tree/`*: `WIRE-INTO-PROJECT.md:450-451` says memory-tree kit updates "never
  carry project data … those stay in the project", and scopes the overwrite to `memory-tree/*.sh` +
  `HYGIENE.template.md`. That scope cannot reach a `.txt`, so a kit update would not in fact delete an
  adopter's registries — rev-1 argued from `:394`, which is a line inside a tree diagram and carries
  no instruction. The correct reading still rejects the placement, but on the weaker ground that
  `:450` states project data belongs outside the kit dir. **The decision does not rest on this bullet.**
- *Into a new `memory/registry/`*: every already-adopted repo's `memory/project/*.txt` becomes an
  unexpected entry under check 3 while the new paths do not exist, so their grandfather lists silently
  empty. `adopt-memory-tree.sh` refuses to touch an already-scaffolded tree, and the kit ships no
  migration script. **This bullet carries the decision on its own.**

Keeping them where they are costs one prose correction at `memory/HYGIENE.md:5` and `:28`, mirrored
into the kit template.

**Deleting the ledger shards** is rejected for the reason upstream reversed its own spec at build
time: the shards are the only source for live-cited ids and session narrative, and rev-6 of upstream's
U7 records them as "RELOCATED, not deleted".

## 5. Production-readiness checklist

- security — N/A. No auth, egress or sanitization surface; the merge driver reads three local blobs.
- perf / scale — the driver runs per conflicted file during a merge; the hygiene gate adds no walk.
- a11y — N/A. No user interface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — the no-anchor case (everything is preamble) is AC7(d); the
  fail-closed exception path is AC7(c).
- observability — `drift_report.py` is the instrument; S4 must leave it able to MOVE, not merely
  silent, which is why AC5 requires a selftest arm in both directions.
- risks — **data-loss is the live risk**, in two places: a `git mv` that is not byte-identical (AC2)
  and a merge driver that drops a row (AC7a/AC7b). Rollback is `git revert`; no external state.
- testing + left-shift gates — one new gate leg; every edited gate keeps its `fail` branches armed,
  and U3 must re-arm check 6 rather than pin it.
- migration / rollback — no adopter data moves. The adopter-facing change is F2.
- user docs — S6; `WIRE-INTO-PROJECT.md` is the adopter-facing surface.

## 6. Acceptance criteria

- **AC1** When `git ls-files memory/project` is run after U3, it lists exactly the five `*.txt`
  registries and nothing else.
- **AC2** When `git log --follow -p --find-renames -- <path> | grep -m1 'similarity index'` is run over
  each relocated file, it prints `similarity index 100%`. `git log` alone prints commit subjects and
  cannot distinguish a rename from a delete-plus-add, so the `-p` is the criterion, not decoration.
- **AC3** When `python tools/memory-tree/gen_build_index.py --check` is run after U1, it exits 0,
  `memory/builds/bThriftyBellows/README.md` carries `status: CLOSED` in front matter, and no spec
  exists under that folder.
- **AC4a** When the gate runs over a fixture whose `project/` path expression is deliberately
  mis-segmented — registries present, selector matching none — the empty-population report names
  **check 3**; and it is silent on a correctly-segmented tree.
- **AC4b** When the gate runs over a tree holding the five registries plus one stray file, check 3
  reports the stray by name.
- **AC5** When `python tools/drift-audit/drift_report.py --check` is run after U2+U4, it exits 0, no
  `gateable` signal reports `DEAD PROBE`, the F3 exit taken is recorded in §4 with its reason, and
  `tools/drift-audit/selftest.py` gains an arm asserting the signal reports empty on a drained fixture
  **and a value again** on a fixture carrying a ledger row.
- **AC6** When `git check-attr merge -- memory/DECISIONS.md memory/backlog/TOOL.md` is run, each
  reports `merge: rows`.
- **AC7** When `bash tools/memory-tree/merge-rows.test.sh` is run it passes, asserting:
  (a) id-set equality between the union of the inputs and the output on **every** rc-0 case;
  (b) the printed kept/took/dropped counts reconcile against the written file's anchored-row count,
  including a fixture where kept < the `%A` row count;
  (c) an unreadable `tools/memory-recall/extract.py` yields conflict markers **containing the incoming
  row**, never a truncated take-ours;
  (d) an identity merge of the real `memory/DECISIONS.md` and each `memory/backlog/*.md` is
  byte-identical, and a file with no anchors at all round-trips unchanged.
- **AC8** When a two-branch merge is constructed where each branch appends a distinct row to
  `memory/backlog/TOOL.md`, the merge auto-resolves with both rows present and no duplicate id.
- **AC9** When `git config --get merge.rows.driver` is run on a wired node it returns the command
  string in §4 Design, and `bash tools/check-wiring.sh --check` reports it when it is unset.
- **AC10a** When `grep -rniE "in-?flight|journal" AGENTS.md .claude/SESSION-KICKOFF.md README.md
  memory/README.md memory/HYGIENE.md tools/memory-tree/HYGIENE.template.md tools/memory-tree/README.md`
  is run after U6, every surviving hit is listed in the commit message with its reason. Measured
  baseline at `f9cf666`: 0 · 1 · 0 · 1 · 6 · 6 · 0. A zero-hit result on a file whose baseline is 0
  proves nothing and is not evidence of work.
- **AC10b** When the same grep is run over `parallel-coding-governance.template.md` (baseline 8) and
  `WIRE-INTO-PROJECT.md` (baseline 6) after U6, the only surviving hits are in the S6b upgrade section
  of `WIRE-INTO-PROJECT.md`, and each one describes the ledger as RETIRED and names the migration.
  Template hits go to 0: `:86-88` are deleted and `:31`, `:68`, `:101`, `:102`, `:211` are rewritten.
- **AC10c** When `bash tools/check-template-size.sh` is run after U6 it exits 0, and the reported byte
  count is **lower** than the 32 746 measured at `f9cf666` — the `:86-88` deletion must land, not be
  traded away for additions elsewhere.
- **AC10d** When a fresh scaffold is run in a throwaway repo after U3
  (`bash tools/memory-tree/adopt-memory-tree.sh`), the resulting tree contains no `IN-FLIGHT.md`, no
  `in-flight/` and no `journal/`, and `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 over
  it. Scaffolder and gate are asserted together because a shape one writes and the other rejects is a
  red bar in either direction.
- **AC11** When `bash tools/run-gates.sh` is run at the end of every unit's commit, it is green.
- **AC12** When `memory/backlog/PLAY.md` is read after U7, `PLAY-aPrunedCeremony-5` leads with
  `WONTDO` and its pointer resolves to `memory/builds/aPrunedCeremony/`.
- **AC13** When `python tools/memory-tree/check-arms.py --check` is run after U3, both gates are at or
  above their `ARMS_FLOORS`, with check 6 armed by a real over-cap fixture rather than a pin row.

## 7. Gates

Existing legs that must stay green: `bash tools/run-gates.sh` in full (38 legs at `f9cf666`).
Load-bearing here — `memory hygiene`, `harness arms`, `verdict epoch` + self-test, `kit/dogfood doc
parity`, `build-index selftest`, `corpus-ids selftest`, `check-arms selftest`, `drift-audit records` +
`selftest`, `kickoff-manifest ratchet`, `codebase-map coverage + freshness`.

New leg: `bash tools/memory-tree/merge-rows.test.sh` in `tools/gate-legs.json` — the runner
single-sources its legs from that manifest and `tools/run-gates.test.sh` forbids a hardcoded leg
command.

Three couplings a builder will otherwise discover the hard way:

1. **Any non-comment change to `check-memory-hygiene.sh` forces `KIT_MEMORY_TREE_VERSION`** (now 1.7)
   to move in the same diff, in three places, plus a `--render`.
2. **The kickoff manifest's watch list is exactly seven pathspecs**:
   `tools/memory-tree/check-memory-hygiene.sh`, `tools/check-template-size.sh`, `tools/run-gates.sh`,
   `tools/gate-legs.json`, `skills/session-kickoff/manifest-check.sh`, `.memory-tree.conf`,
   `parallel-coding-governance.template.md`. **Three units stage one** — U3, U5 and U6. The pre-commit
   runs `manifest-check.sh --staged`, whose C5s leg accepts only a re-stamp bundled in **that same
   commit**, so each of those three commits carries its own `last-audit` re-stamp. Stamp from `date`.
3. **Every new gate leg pushes `handkept_inventories_disagreeing_with_source` up by one** unless
   `AGENTS.md`'s gate-suite section gains a bullet citing that leg's argv script path. The signal
   matches on the argv path, not the display name.

Run `python tools/memory-tree/gotchas.py --for-diff 663ca427..HEAD` before the review, not after.

## 8. Open questions

- **F1 — the `F:*.md` catch-all at `check-memory-hygiene.sh:229`.** With the machinery gone it is what
  would let a stray `.md` creep back. Tightening it turns two hygiene-test fixtures
  (`kickoff-prompt.md`, `links.md`) into check-3 findings with no `cnot 3` covering them, **and** a
  third fixture is affected: `memory/project/in-flight/tnode.md` is check 6's SOLE arm, so dropping
  `in-flight/*.md` from `index_set()` unarms it and drops the gate below its 14/14 floor. Pinning
  instead reds the drift leg, because `unarmed-branches.txt` is a `SHRINK_ONLY` member.
  **RESOLVED (build, 2026-08-09): tighten the catch-all to the five registry names, repoint the two
  fixtures, and replace check 6's arm with a >250-line `memory/guides/tfixture.md`** — `index_set()` already selects
  `guides/*.md`, so the arm keeps firing without touching the pin.
- **F2 — does the kit keep scaffolding a session ledger for ADOPTERS?** Dropping it from
  `adopt-memory-tree.sh` while check 3 stops admitting `IN-FLIGHT.md` / `in-flight/` / `journal/` makes
  an adopter who kept the sharded ledger go red on their next hygiene run, and that contract is stated
  to them at `WIRE-INTO-PROJECT.md:119` and `:389`.
  **RESOLVED (owner, 2026-08-09): retire it for adopters too, in the same version bump.** Taken with
  the measured break in front of us: the one adopter found on this node (`swydee`) runs kit 1.4 on a
  pre-flatten tree with three live rows and no generated index to fall back on, so retirement obliges
  the S6b upgrade note rather than a silent break. A migration of that repo is its own unit in its own
  repo and is not this unit's work.
- **F3 — `signal_ledger`'s fate.** Three exits: delete it (upstream did, but 17 selftest references
  ride it); add it to `DECLARED_EMPTY` and retire its pin of 4; or repoint it at
  `memory/archive/ledger/` (where the pin reads 4 forever and the ratchet becomes permanent).
  **RESOLVED (build, 2026-08-09): `DECLARED_EMPTY` + retire the pin**, with AC5's two-direction selftest arm as the
  control, because `DECLARED_EMPTY` alone only relabels the printed line.
- **F4 — `adopt-memory-tree.sh` scaffolds 2 of the 5 registries.** `id-orphan-waiver.txt`,
  `corpus-path-unresolved.txt` and `unarmed-branches.txt` are named by three gates and created by
  none. **RESOLVED (build, 2026-08-09): close it in U3**, landing the `memory/HYGIENE.md:81` correction with it.
- **F5 — does the PLAYBOOK keep mandating a sharded per-node in-flight ledger?** The template is the
  product ruleset: `:86-88` mandates "Shard the in-flight ledger per node … NEVER one shared table",
  `:101-102` says journals and the ledger are per-node files, `:211` requires a ledger row before
  wrap-up, and `:31` and `:68` reference it. Whether adopters keep that ruleset is a product decision,
  not a builder's. Byte direction matters: the gate reports **32 746 / 32 768, 22 free**, so deleting
  `:86-88` frees roughly a kilobyte while any added clause fails outright.
  **RESOLVED (owner, 2026-08-09): retire it, in lockstep with F2.** The rule's own justification is
  that a shared mutable index "forces a conflict on every land" — which is the question S5's row-keyed
  driver and the generated build index now answer two other ways. Carrying all three would be three
  answers to one question. The line-by-line edit and its byte deltas are in §4 Files touched.
- **F6 — `check-memory-hygiene.sh:346`.** The `MAP_SUB` branch rewrites `ex7` wholesale and drops the
  `guides/` alternative. Dormant until 2026-08-09; this repo now has `.codebase-map.conf` with
  `MAP_ROOT=memory/map`, so it is live, and F1's recommendation puts a `guides/` fixture straight into
  its path. **RESOLVED (build, 2026-08-09): fix it in U3** — append rather than replace — since U3 edits that
  expression anyway and the two spellings of `ex7` are already a two-answers-to-one-question site.

## 9. Revision log

- rev-1 · 2026-08-09 · initial draft. Grounded on upstream `ARCH-dSiftedGranary-1` and
  `ARCH-dQuarriedLedger-1` (units U4, U6, U6a, U7, U9) read in `C:/projects/incms/main`, and on a
  six-lens measured sweep of this repo. Two owner premises corrected in §3. The registry re-home
  recommendation was reversed against the evidence in §4 Alternatives rejected.
- rev-2 · 2026-08-09 · folded the closing spec review (11 agents, 34 raw findings, 28 confirmed,
  precision 0.82; verdict NOT READY at rev-1). Fixed eight blocking defects: the stub build folder
  takes an authored `status:` and NO spec (rev-1 directed fabricating a spec for work that shipped
  2026-07-16); check 6's sole arm gets a named replacement fixture; the merge driver gained its
  literal `git config` string and the `tools/lib/pyrun.sh` shim it needs, which this repo lacks; the
  `pop_guard` call is stated with both counts and S3's "emptied" premise corrected to "drained of
  session machinery"; the playbook-layer ledger fork was raised as F5; §7 coupling 2 now names the
  real seven-pathspec watch list and the three units that stage one; the three `.md` stub deletions
  moved into U1 so no commit orphans `MEMORY.md`'s link; and AC7 became assertions rather than a list
  of fixture shapes. AC4 split into AC4a/AC4b because rev-1's wording passed on a tree where the guard
  was never written. AC9 was blind to the two files it most needed and is now AC10a/AC10b with
  measured per-file baselines. Six non-blocking corrections folded, including the `WIRE-INTO-PROJECT.md`
  citation in §4 Alternatives rejected, which was a tree-diagram line carrying no instruction — the
  decision now rests on the bullet that carries it. F6 added: the `MAP_SUB` `ex7` defect went live
  when this repo adopted codebase-map earlier today.
- rev-3 · 2026-08-09 · owner ratified F2 and F5 as **retire everywhere**, both marked RESOLVED in
  place and the header tail stamped `ratified 2026-08-09`. The template edit is now stated line by
  line with measured byte deltas rather than named as an intention — `:86-88` deleted (−954 B), five
  lines rewritten — which was the last of the review's three invent-it-yourself defects. S6b added:
  retirement in the product is a breaking change for an adopter still carrying a ledger, so the
  runbook gains a migration section. Measured the blast radius rather than assuming it: one adopter
  on this node (`swydee`), kit 1.4, pre-flatten tree, three live rows, no generated index to fall
  back on. AC10b became determinate and AC10c/AC10d were added, so the deletion cannot be traded away
  for additions elsewhere and the scaffolder and gate are asserted together. Migrating `swydee` is
  its own unit in its own repo.
- rev-4 · 2026-08-09 · folded the sub-spec review (11 agents, 47 verdicts, 8 blocking). Ratified the
  four forks the owner did not rule on — F1, F3, F4 and F6 — each to its recommended, most
  feature-rich option, marked `RESOLVED (build, …)` to keep them distinguishable from the owner's F2
  and F5. F6's fix moved from §3 Non-goals into U3, where it belongs now that it is ratified. AC2 was
  unfalsifiable as written: `git log --follow` prints commit subjects, and `similarity index 100%`
  only appears under `-p`/`--summary`, so a builder could not have told a rename from a
  delete-plus-add — the one thing that AC exists to prove. The Rollout row for U2+U4 claimed
  `memory/archive/ledger/README.md`, which the Migration table assigns to U1; U1 creates it and U2
  must not re-create it. Unit ids are per-file (`-2`..`-6`) rather than six specs sharing `-1`:
  `gen_build_index.py:54` requires the id to be followed immediately by the em-dash, and one id
  across six specs reproduces the over-flagging shape `drift_report.py:228-231` records at 107/126.
- rev-5 · 2026-08-09 · §4 Data model's U5 decision table amended from the shipped code, in both
  places it is stated (here and the U5 sub-spec, which moves to rev-3 in the same edit). The ratified
  row `| id in %B only | append |` was WRONG and stayed wrong through two repairs: measured against
  `git merge-file` — the merge this driver replaces — appending an incoming row past the row block
  files it under whatever `## FAMILY` heading is last, and a third review round reproduced a `PLAY`
  decision auto-committed under `## KICK` through this repo's own wiring at rc 0. The table now
  carries the splice, its `%A`-only skip, the ROW-scoped (lead-in + anchor) delete comparison whose
  anchor-only form silently discarded a correction row filed above a deleted one, and the two
  POSTCONDITIONS — no row line or leading id written more often than any one input carries it, and no
  row filed under a heading no input filed it under — that refuse what no placement rule can decide.
  A ratified table that no longer describes the code is the drift class this repo gates for, so the
  rule change is recorded here rather than only in a commit message.

## 10. Reuse audit

`reuse_lookup.py` over the newly-populated map returns, for "three-way merge index rows keyed by
record id": `records` (`tools/memory-tree/gotchas.py`, fan-in 6, SEAM) and `merge`
(`tools/settings-merge.py`, fan-in 5, SEAM). Neither fits — `gotchas.records` parses front matter and
`settings-merge.merge` does a recursive dict union for JSON settings, not a three-way text merge with
conflict markers.

The seams this unit DOES wire through are `tools/memory-recall/extract.py`'s anchor grammar, imported
rather than reimplemented, and `tools/lib/resolve-python.sh`, sourced by the new `pyrun.sh` rather
than re-solved. That is the reuse decision: **no seam fits for the merge itself; the grammar and the
launcher resolver are reused and must not be vendored.**

Two caveats stated rather than hidden. The map's corpus is `bash`-recall-dark and this repo's gates
are bash, so a shell seam cannot appear in that shortlist. And 69 of 71 inventory keys are still
baselined, so the map ratchets coverage without yet describing the system. Both are recorded in
`memory/map/features/codebase-map.md` §Gaps.
