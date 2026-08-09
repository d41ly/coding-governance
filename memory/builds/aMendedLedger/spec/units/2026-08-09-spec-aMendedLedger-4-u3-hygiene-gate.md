# TOOL-aMendedLedger-4 — U3: make the hygiene gate and the adopter scaffold match the drained tree

**Status:** SPECCED · rev-2 · 2026-08-09 · node a · Tier-2 · base 663ca427 · streams tooling

## 1. Goal

Move the memory-tree KIT CONTRACT to the tree U1 and U2 leave behind: `memory/project/` holds the
five waiver registries and nothing else. The gate stops admitting the retired session machinery, the
scaffolder stops writing it, the scaffolder starts writing the three registries three gates name and
nothing creates, and the prose that describes both is re-trued in the same commit that changes the
verdicts.

## 2. Scope (IN)

- **S1** Tighten check 3's `project/` sub-lint in `tools/memory-tree/check-memory-hygiene.sh:225-230`
  to the five registry names only, deleting the `F:*.md` catch-all, `F:README.md`, `F:MEMORY.md`,
  `F:IN-FLIGHT.md` and `D:journal|D:in-flight` (master F1).
- **S2** Add the selector-integrity guard for that population — the `pop_guard 3` call the master
  states verbatim in its §4 Design, copied byte for byte.
- **S3** Drop the two session-ledger lines from `index_set()` at `:307-308`, so the index-cap and
  entry-budget populations stop naming files the tree no longer has.
- **S4** Drop the `IN-FLIGHT` / `in-flight` alternatives from BOTH spellings of `ex7` at `:345` and
  `:346`, and fix the `MAP_SUB` spelling so it APPENDS to the base rather than rewriting it — the
  live F6 defect that silently drops the `guides/` exemption on any repo carrying a
  `.codebase-map.conf`, which this repo now does.
- **S5** Re-fixture `tools/memory-tree/check-memory-hygiene.test.sh`: repoint `kickoff-prompt.md`
  (`:199`) and `links.md` (`:203`) out of `memory/project/`, and replace check 6's sole arm
  `memory/project/in-flight/tnode.md` (`:212-216`, asserted `:330`) with an over-cap
  `memory/guides/tfixture.md` (master F1).
- **S6** Arm what S1, S2 and S4 change. Three arms, and only one of them needs a new tree:
  a check-3 finding for a stray **`.md`** under `project/` — only a `.md` tells the two engines
  apart, because a stray `.txt`, an extensionless file or a subdirectory already falls through to
  `*) echo "$M/project/${e#*:}"` at `:230` on the PRE-edit engine, so a non-`.md` fixture would pass
  before the edit and prove nothing; a mis-segmented-selector arm for the new `pop_guard`, grown
  from the EXISTING half-migrated tree at `check-memory-hygiene.test.sh:491-499` rather than a new
  one; and ONE new scratch tree carrying a `.codebase-map.conf` — the only place the `MAP_SUB`
  spelling of `ex7` is reachable — plus a source-level assertion that `ex7` keeps exactly one
  spelling of the `guides/` exemption.
- **S7** Retire the session machinery from `tools/memory-tree/adopt-memory-tree.sh` (`:38`, `:55`,
  `:74-88`, `:93`, `:94`) and close master F4 by scaffolding all five registries, not two. Assert
  scaffolder and gate together, inside the hygiene self-test, by running the real scaffolder into a
  throwaway repo and running the gate over its output.
- **S8** Move `KIT_MEMORY_TREE_VERSION` 1.7 → 1.8 in all three places
  (`check-memory-hygiene.sh:13` carries two of them — the constant and the `gov:kit` marker on the
  same line — and `memory/HYGIENE.md:1` is the third, rendered into the shipped template).
- **S9** Re-true `memory/HYGIENE.md` at `:5`, `:28`, `:46`, `:58-62`, `:74`, `:81` and `:93`, mirror
  it into `tools/memory-tree/HYGIENE.template.md` through the kit's own `--render` path, and record
  the RUNNING engine version on `AGENTS.md:62` as an ADDED clause. The `kit 1.5` token already on
  that line is not stale and is not moved — see §3; the replacement line is stated verbatim in §4
  Migration so no builder has to invent it.

## 3. Non-goals (OUT)

- **Deleting or renumbering any `fail` branch.** `check-arms.py` floors are per-gate and one-sided
  (`ARMS_FLOORS="… tools/memory-tree/check-memory-hygiene.sh:14:14"`, `.memory-tree.conf:62`), so a
  deleted guard reds the bar. Nothing in this unit is a `fail` call site; see §7.
- **Pinning a branch in `memory/project/unarmed-branches.txt`.** That file is a `SHRINK_ONLY` member
  (`tools/drift-audit/drift_signals.py:45`), so adding a row reds the drift-records leg. Re-fixture
  instead — master F1's whole point.
- **The ledger relocation, the drift signal and the merge driver.** U1, U2+U4 and U5 own those. This
  unit assumes `memory/project/` already holds only the five `.txt` files when it lands (§4 Rollout).
- **`memory/README.md:23`, `.claude/SESSION-KICKOFF.md` §B, `WIRE-INTO-PROJECT.md`, the playbook
  template and `tools/memory-tree/README.md`.** Doc truth is U6's row. U3 takes only
  `memory/HYGIENE.md` (which it must, for parity with the version bump) and one ADDED clause on
  `AGENTS.md:62`.
- **Substituting `1.8` for the `kit 1.5` token on `AGENTS.md:62`.** Nothing at `:62` is stale.
  Measured, the line reads ``- `memory/` hygiene (19 checks, kit 1.5 flat tree) — …``, and that `1.5`
  names the kit release that FLATTENED the tree, not the running engine. It agrees with seven sites
  this unit does not touch — `check-memory-hygiene.sh:17` ("Since 1.5 the tree is FLAT"), `:112`,
  `:206`, `:243`, `:429`, `:534` and `adopt-memory-tree.sh:12` ("(kit 1.5). The tree is flat."). A
  substitution would assert the flatten happened at 1.8, which is false, and would manufacture the
  exact `two-answers-to-one-question` divergence §7 says this unit is instrumented against. S9
  therefore APPENDS the running version beside the flatten token instead of overwriting it, and
  AC13 grades both halves.
- **`tools/memory-tree/hygiene-parity.test.sh`.** The master's §4 Files touched lists it; it needs no
  edit. Its baseline floor is DERIVED from the constant at `:51-53`, so the bump repoints it for
  free, and it is not a gate leg.
- **`memory/HYGIENE.md:136`** ("the flatten left four of them in the live ledger"). That is a
  historical rationale for why a DIRECTORY citation counts under check 15, not a live claim about the
  tree, and `DEAD_PATH_PIN="0"` already records that the population drained.
- **Pinning the two unpinned registries in `.gitattributes`.** `id-orphan-waiver.txt` and
  `corpus-path-unresolved.txt` are read only by `corpus_ids.py`, whose `read()` normalizes CRLF, so
  there is no live defect — unlike the three that ARE pinned, which are read by shell.

## 4. Design

### Inventory

Measured at `dae75003` on branch `branch/cd-memory-rework-alignment-005661`.

| fact | measured value |
|---|---|
| `.txt` files under `memory/` | 5, all at `memory/project/` — so the guard's precondition equals its population today |
| hygiene `fail` branches / armed | 14 / 14, floor `14:14` |
| `.codebase-map.conf` | present, `MAP_ROOT=memory/map` — F6 is LIVE, not dormant |
| `memory/guides/` | one file, `REVIEW-PROTOCOL.md` |
| `memory/HYGIENE.md` vs shipped template | byte-identical after stripping the `tools/` install prefix |
| `in-?flight|journal` hits in `memory/HYGIENE.md` | 6, at `:28 :46 :60 :61 :74 :93` |
| charter read path (check 16) | 3 files, 29 624 B against a 37 060 B ceiling; `memory/HYGIENE.md` is NOT a member |
| gate legs | 38 |

Two of those numbers redirect the work. `memory/HYGIENE.md` is not in the check-16 read path, so this
unit's prose edits cannot move that ceiling in either direction. And the scratch tree in
`check-memory-hygiene.test.sh` writes no `.codebase-map.conf`, so `MAP_SUB` is empty throughout the
existing self-test and the `:346` spelling of `ex7` is unreachable by every arm in the file — which is
how F6 shipped dormant and went live without a single assertion moving.

### Data model

Six edits to the engine. Line numbers are the pre-edit ones.

**`:13` — the verdict epoch.** `KIT_MEMORY_TREE_VERSION=1.7` and the `gov:kit memory-tree@1.7` marker
in the trailing comment both become `1.8`. `check-kit-versions.sh:30-34` asserts the constant equals
the marker in `tools/memory-tree/HYGIENE.template.md`, and `kit-dogfood-parity.test.sh` forces that
template to equal `memory/HYGIENE.md`, so the third literal is `memory/HYGIENE.md:1` and the shipped
copy is regenerated, never hand-edited (§4 Migration).

**`:224-230` — check 3's `project/` sub-lint, plus the guard.** The guard is inserted between the
`p1=` assignment and the `bp=` loop, verbatim as the master states it:

```bash
PRE_REGISTRY=$(printf '%s\n' "$FILES" | grep -cE '\.txt$')
pop_guard 3 "no registry under $M/project/" \
  "$(printf '%s\n' "$FILES" | grep -cE "^$M/project/[^/]+\.txt$")" "$PRE_REGISTRY"
```

`pop_guard` (`:123-128`) fires only when the population is 0 AND the precondition is above 0, which is
why the precondition must be the UN-SEGMENTED count: it is the one shape that can differ from the
population when the path expression is wrong. `project/` after this unit is drained of session
machinery, not emptied — the five registries stay, the population is 5, and the guard's job is
catching a mis-segmented selector rather than an empty directory. The `bp` case list then becomes:

```bash
bp=$(printf '%s\n' "$p1" | grep . | while IFS= read -r e; do case "$e" in
  F:legacy-files.txt|F:curation-debt.txt) ;;
  F:id-orphan-waiver.txt|F:corpus-path-unresolved.txt|F:unarmed-branches.txt) ;;
  *) echo "$M/project/${e#*:}";; esac; done)
```

`F:README.md` goes with the rest: the master's Migration table deletes `memory/project/README.md` in
U1 and F2 stops the scaffolder writing one, so an admitted-but-never-written name is a third answer to
a question this unit is closing.

**`:307-308` — `index_set()`.** Both lines are deleted: the `MEMORY.md` / `IN-FLIGHT.md` pair and the
`in-flight/[^/]+\.md$` glob with its trailing comment. Nothing else in the function moves; `guides/`
(`:318`) is what carries check 6's replacement arm.

**`:343-346` — check 7's exemption.** The header comment is re-trued (it still names `TREE.md`, which
`ex7` has never matched, and `IN-FLIGHT.md`), and the expression becomes ONE base plus an append:

```bash
ex7='/guides/[^/]+\.md$'
[ -n "$MAP_SUB" ] && ex7="$ex7|/$MAP_SUB/FOUNDATION\.md\$|/$MAP_SUB/features/[^/]+\.md\$"
```

The call site at `:357` is left byte-for-byte alone: `grep -vE "$ex7"` takes a top-level alternation
and needs no parentheses. Re-adding them would recreate the two-spellings shape this edit exists to
remove. The `\$` escapes are deliberate — inside double quotes a bare `$|` and a trailing `$` are both
literal, but relying on that reads as a bug to the next reader.

That append is the F6 fix. Before it, any tree with a `.codebase-map.conf` naming a direct child of
the memory root got an `ex7` with no `guides/` alternative at all, so every guide entered check 7's
population — a loosening in the other direction that nothing asserts and that F1's new `guides/`
fixture would have walked straight into.

### Migration

Fixture and scaffolder moves, per file, with the reason each destination is the only one that works.

| what | from | to | why |
|---|---|---|---|
| check 1's red arm | `memory/project/kickoff-prompt.md` (`:199`) | `memory/guides/kickoff-prompt.md` | must stay outside `builds/*/prompts/` and `archive/` to keep arming check 1; `guides/` contents are unconstrained by check 3 |
| check 2's link pair | `memory/project/links.md` (`:203`) | `memory/guides/links.md` | moves WITH its live target so the resolving half stays resolving; `decisions/` and `archive/` are impossible — check 2 exempts them, which would silence both arms |
| check 6's sole arm | `memory/project/in-flight/tnode.md` (`:212-216`) | `memory/guides/tfixture.md`, >250 lines | `index_set()` already selects `guides/*.md` (`:318`), so the arm fires without touching the shrink-only pin |
| the five registries | 1 present in the scratch tree | all 5 written at `memory/project/` | models the post-U3 shape, and is the precondition AC3's stray finding is measured against |
| scaffolder: `journal/` | `adopt-memory-tree.sh:38`, `:93` | deleted; `:38` becomes `mkdir -p "$M/project" …` | `project/` still needs creating — the registry `printf` redirects cannot create their own directory |
| scaffolder: `in-flight/` | `:94` | deleted | — |
| scaffolder: `MEMORY.md`, `IN-FLIGHT.md`, `project/README.md` | `:74-88` | deleted | check 3 no longer admits any of the three |
| scaffolder: `README.md` prose | `:55` | rewritten to name the five registries | `memory/README.md` is written by the scaffolder itself; leaving it would ship a doc describing a shape the same script no longer produces |
| scaffolder: 3 missing registries | — | written beside `legacy-files.txt` and `curation-debt.txt` (`:89-92`) | master F4 |

**The AC6 arm's three preconditions, because the scaffolder refuses three ways before it writes
anything.** Build the throwaway repo the way `check-memory-hygiene.test.sh:511-524` builds the
young tree — `git init -q`, `git config user.email` / `user.name`, and a written `.memory-tree.conf`
(`adopt-memory-tree.sh:20-24` copies `.memory-tree.conf.example` into the repo and **exits 1** when
the conf is absent, so an arm that forgets it sees rc 1 *and* a mutated fixture). The repo must carry
**no** pre-existing `memory/`: `:30-36` exits 0 with "already scaffolded — nothing to do" when
`$M/HYGIENE.md` carries the `gov:kit memory-tree@` marker (`:31`) and exits 1 refusing to overwrite
otherwise — so a pre-seeded `memory/` gives a green rc over an unwritten tree, which is the
`fixture-passes-by-finding-nothing` shape §7 names. Then run
`bash "$HERE/adopt-memory-tree.sh" --scaffold` (the flag is mandatory — `:17` exits 2 without it) and
`bash "$SCRIPT"` from inside that repo. The arm also needs a usable python launcher on `PATH`:
`:142` runs `gen_build_index.py` through `_PY`, resolved at `:141` by the inline `resolve_python`
block the kit carries verbatim, which `exit 2`s when no launcher runs — the same dependency the
young-tree arm already carries as `$_PY` at `check-memory-hygiene.test.sh:519`.

`memory/HYGIENE.md` is edited by hand and `tools/memory-tree/HYGIENE.template.md` is NEVER edited by
hand: run `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, which rewrites the shipped
copy from the live one with the `tools/` install prefix stripped (`kit-dogfood-parity.test.sh:44`,
`:54`). The two are therefore identical modulo that prefix, not byte-identical.

The seven prose sites, and what each becomes:

| line | today | after |
|---|---|---|
| `:5` | "…per-build folders, session machinery, and long-lived guides" | "…per-build folders, the gate's own waiver registries, and long-lived guides" |
| `:28` | the tree-diagram row for `project/` naming the ledger, journals and notes | `project/` holds the five waiver registries (`*.txt`) and nothing else |
| `:46` | "Delete cold journals; file a feature's plan/review writeups…" | "Delete cold scratch notes; file a feature's plan/review writeups…" |
| `:58-62` | the entry-budget bullet, listing `MEMORY.md` and exempting `IN-FLIGHT.md` + `in-flight/*.md` | same bullet without `MEMORY.md`, exempting `guides/*.md` — which is what `ex7` actually implements |
| `:74` | "Distinct from the session-ledger vocabulary…" | sentence deleted; the dash form follows the slot rule directly |
| `:81` | "Two plain sorted path lists in `memory/project/`, read with exact-match `grep -qxF`" | five lists, read as exact-key set membership — the engine replaced the per-call `grep` fork with associative arrays at `:57-61` |
| `:93` | check 3's catalogue entry, listing `journal/ in-flight/` as unconstrained | `decisions/ guides/ archive/` unconstrained; `project/` holds ONLY the five registries and its selector carries rule 5's guard |

`:46` and `:58` are NOT in the master's line list (it names `:5, :28, :60-61, :74, :81, :93`). `:46` is
a sixth `journal` hit and `:58` is the `MEMORY.md` half of the entry-budget sentence, whose clause
actually runs `:60-62`. Both are folded here, because master AC10a's baseline for this file is 6 hits
and the master's list reaches only 5 of them. `:81` grows by three bullets (F4's three registries),
which is safe: `memory/HYGIENE.md` is not a check-16 read-path member and is not in `index_set()`.

**`AGENTS.md:62`, stated verbatim so nobody invents a string.** The line becomes, exactly:

```
- `memory/` hygiene (19 checks, flat tree since kit 1.5; engine at kit 1.8) — `tools/memory-tree/check-memory-hygiene.sh`; checks 9, 13-16 and 17-19 delegate to `gen_build_index.py`, `corpus_ids.py` and `gotchas.py`
```

Both facts now have exactly one home on that line: the flatten release and the running engine. Two
properties make this edit inert against the gates that read `AGENTS.md`. The argv path
`tools/memory-tree/check-memory-hygiene.sh` is unchanged, so
`handkept_inventories_disagreeing_with_source` — which counts legs whose script path the charter's
gate-suite section fails to cite (`drift_signals.py:129-136`, pin 7 of 38) — cannot move. And the
added clause introduces no new `memory/<path>` token, so check 16's read set is unchanged: `read_set`
(`corpus_ids.py:277-305`) admits only charter tokens starting with `memory/`, the bare `` `memory/` ``
in the leading cell fails `cand.startswith("memory/")` after its trailing slash is stripped, and the
byte sum (`corpus_ids.py:392-397`) stays at the measured 29 624 B against `READ_PATH_CEILING="37060"`
(`.memory-tree.conf:46`).

### Rollout

**Hard precondition: U1 and U2+U4 have landed.** This unit's check 3 rejects `MEMORY.md`,
`IN-FLIGHT.md`, `project/README.md`, `journal/` and `in-flight/`; all five are still tracked at
`dae75003`. Landing U3 first turns the gate red on the very tree it is supposed to describe.

One commit. Scaffolder and gate move together because scaffolding a shape the gate rejects, and
rejecting a shape the scaffolder writes, are both red bars — and because the version bump that dates
the new verdicts is the same bump the doc parity pair reads.

Order inside the commit is fixed by two tools that read each other: edit the engine and
`memory/HYGIENE.md:1` first, then run `--render`, then run the gate suite. Re-stamp `last-audit` in
`.claude/SESSION-KICKOFF.md` last, taking the datetime from `date` and the sha from the manifest's own
stamp rule (`HEAD` on the default branch, else `git merge-base origin/main HEAD`).

### Files touched (estimate)

| path | change |
|---|---|
| `tools/memory-tree/check-memory-hygiene.sh` | 6 edit sites: `:13`, `:224-230`, `:307-308`, `:343-346` |
| `tools/memory-tree/check-memory-hygiene.test.sh` | fixture repointing, 3 new arms, 1 new source-level assertion, **1 new scratch tree (the `.codebase-map.conf` tree, AC5) plus two edits to the EXISTING `$TMP/halfmigrated` tree at `:491-499` — it gains `memory/architecture/project/legacy-files.txt` so `PRE_REGISTRY` is non-zero there, and its assertion loop at `:502` becomes `for c in 3 4 5 8 12`**, recount the trailing assertion total |
| `tools/memory-tree/adopt-memory-tree.sh` | `:38`, `:55`, `:74-88`, `:89-92`, `:93`, `:94` |
| `memory/HYGIENE.md` | `:1` (marker) + the seven prose sites above |
| `tools/memory-tree/HYGIENE.template.md` | GENERATED by `--render`; never hand-edited |
| `AGENTS.md` | `:62` only, and ADDITIVE — the replacement line is stated verbatim in §4 Migration; the `kit 1.5` flatten token and the argv path both survive |
| `.claude/SESSION-KICKOFF.md` | `last-audit` re-stamp, nothing else |

New files: none.

### Alternatives rejected

**Keeping `F:*.md` and pinning the two affected fixtures instead of repointing them.** Rejected on
measurement, not taste: the catch-all is exactly what would let a stray `.md` creep back into a
directory this unit is defining as five files, and the only cheaper alternative — a
`memory/project/unarmed-branches.txt` row — reds `drift_report.py --check`, because that file is a
`SHRINK_ONLY` member seeded at "empty today and meant to stay so".

**Rewriting `ex7` in the `MAP_SUB` branch and simply adding `guides/` back.** Rejected: that leaves
two full spellings of one expression, which is the `two-answers-to-one-question` class this repo
gates on and the exact mechanism by which the `guides/` alternative was lost the first time. The
append form has one spelling of the base and one of each map alternative.

**Leaving AC10d as a manual step in a throwaway repo.** Rejected under the same rule that put the
scaffolder and the gate in one commit: an acceptance check nobody can run twice is not a check. The
scaffolder runs INSIDE `check-memory-hygiene.test.sh`, against a scratch repo, so the assertion is a
gate leg rather than a memory of one afternoon.

**A hand-built imitation of the scaffolder's output.** Rejected: a hand-built tree asserts what the
test file BELIEVES the scaffolder emits, and that belief is the copy that drifts. The existing
"freshly scaffolded tree" arm (`:511-524`) already builds by hand; the new arm runs
`adopt-memory-tree.sh --scaffold` for real and keeps the hand-built one as the young-tree control.

## 5. Production-readiness checklist

- security — N/A. No auth, egress or sanitization surface; every edit is a path selector, a case list
  or prose.
- perf / scale — neutral. The new `pop_guard` adds two `grep -c` passes over an in-memory file list
  already held in `$FILES`; `index_set()` loses two producers.
- a11y — N/A. No user interface.
- i18n — N/A. No user-facing strings beyond gate messages, which stay in the existing register.
- error / empty / loading states — the empty case IS the subject: a `project/` selector that matches
  nothing must report check 3 (AC2), and a genuinely young tree with no `.txt` anywhere must stay
  silent, which the precondition arm at `:511-524` continues to prove.
- observability — the gate's own output is the instrument. The new guard reports through the existing
  `POP_MISSING` block (`:680-686`), which names every disarmed selector rather than the first.
- risks — the live risk is a CONTRACT break for adopters, not data loss: after this bump an adopter
  who kept `MEMORY.md`, `IN-FLIGHT.md`, `project/README.md`, `journal/` or `in-flight/` reds on their
  next hygiene run. That is the owner-ratified F2 outcome and it obliges U6's S6b upgrade note. This
  unit's rollback is `git revert`; no external state.
- testing + left-shift gates — no new gate leg. Every edited branch keeps its arm; three new arms and
  one source-level assertion are added; the scaffolder gains its first executable assertion.
- migration / rollback — no data in this repo moves. The adopter-facing migration is F2 and its note
  is U6's.
- user docs — `memory/HYGIENE.md` plus its rendered mirror, in this commit. The adopter runbook is
  U6's.

## 6. Acceptance criteria

- **AC1** When `git ls-files memory/project` is run after this unit's commit, it lists exactly
  `corpus-path-unresolved.txt`, `curation-debt.txt`, `id-orphan-waiver.txt`, `legacy-files.txt` and
  `unarmed-branches.txt`, and nothing else.
- **AC2** When the self-test's half-migrated scratch tree carries a registry at a PRE-flatten path
  (`memory/architecture/project/legacy-files.txt`), the empty-population report contains a line
  beginning `    check 3: `; and the main scratch tree, whose registries sit at the expected depth,
  contains no such line.
- **AC3** When the main scratch tree holds all five registries plus one stray **`.md`** file
  `memory/project/tstray.md`, check 3's own output slice names `memory/project/tstray.md` — asserted
  through `chit 3`, so a finding from check 1, 2, 5, 9 or 12 cannot satisfy it. The extension is
  load-bearing, not decoration: a stray `.txt`, an extensionless file or a subdirectory already falls
  through to `*)` at `check-memory-hygiene.sh:230` on the PRE-edit engine, so only a `.md` fixture
  distinguishes the two engines. S5 is what makes the fixture necessary — it moves the only two `.md`
  residents of `memory/project/` (`:199`, `:203`) out.
- **AC4** When `bash tools/memory-tree/check-memory-hygiene.test.sh` is run, check 6's output slice
  names `memory/guides/tfixture.md`, and
  `grep -c 'project/in-flight' tools/memory-tree/check-memory-hygiene.test.sh || true` returns 0
  (baseline 3, at `:214`, `:216` and `:330`). The path argument and the `|| true` are both required:
  `grep -c` with no file argument reads stdin and hangs, and it exits 1 on a **zero** count — the
  passing state — so any `&&` chain or `set -e` caller reads success as failure. The test file itself
  is `set -u` and not `set -e` (`:10`), so an in-file arm survives without the guard; the AC carries
  it anyway because the AC is run standalone.
- **AC5** When the gate runs over a scratch tree carrying `.codebase-map.conf` with
  `MAP_ROOT=memory/map`, check 7's slice reports the over-cap row in `memory/map/README.md` and does
  NOT report the over-cap rows in `memory/guides/tguide.md` or `memory/map/features/tdoss.md`; and a
  source-level assertion in the same test fails if any second `ex7=` assignment carries a literal
  `/guides/` instead of appending to `"$ex7"`.
- **AC6** When the self-test runs `bash tools/memory-tree/adopt-memory-tree.sh --scaffold` into a
  throwaway repo, the resulting tree contains no `memory/project/IN-FLIGHT.md`, no
  `memory/project/MEMORY.md`, no `memory/project/README.md`, no `memory/project/in-flight/` and no
  `memory/project/journal/`; it contains all five registry files; and
  `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 over it.
- **AC7** When `bash tools/check-kit-versions.sh`, `bash tools/memory-tree/check-verdict-epoch.sh` and
  `bash tools/memory-tree/kit-dogfood-parity.test.sh` are run after the commit, each exits 0; and
  `grep -no '1\.8' tools/memory-tree/check-memory-hygiene.sh` prints exactly two records, both
  prefixed `13:` (the constant and the `gov:kit` marker sharing line 13); and `sed -n 1p
  memory/HYGIENE.md` and `sed -n 1p tools/memory-tree/HYGIENE.template.md` each contain
  `gov:kit memory-tree@1.8`. `grep -c` is the wrong instrument here and `grep -o | wc -l` is the
  fragile one: `-c` counts LINES, so two literals on one line return 1 and never 2, and a bare
  occurrence count over the old token already reads 3, not 2 — `:470` carries `81.77s`, whose `1.7`
  the pattern matches. `grep -no` asserts the count and the line in one command and is immune to
  both. Measured today: `grep -o '1\.7' … | wc -l` → 3; `grep -n '1\.8' …` → no match.
- **AC8** When `grep -ciE "in-?flight|journal"` is run over `memory/HYGIENE.md` and
  `tools/memory-tree/HYGIENE.template.md`, both return 0. Measured baseline at `dae75003`: 6 and 6.
- **AC9** When `python tools/memory-tree/check-arms.py --check` is run it exits 0, and `--report`
  shows `tools/memory-tree/check-memory-hygiene.sh` at 14 branches and 14 armed against its
  `ARMS_FLOORS` entry of `14:14`, with `memory/project/unarmed-branches.txt` still holding no
  hygiene-gate row.
- **AC10** When `git show --stat` is run on this unit's commit, it stages
  `tools/memory-tree/check-memory-hygiene.sh` and `.claude/SESSION-KICKOFF.md` together, the manifest
  diff changes `last-audit`, and `bash skills/session-kickoff/manifest-check.sh` exits 0 afterwards.
- **AC11** When `bash tools/run-gates.sh` is run at this commit, all 38 legs are green.
- **AC12** When `bash tools/memory-tree/check-memory-hygiene.test.sh` is run it exits 0 and its final
  line reports an assertion count equal to the number of assertions the file makes — the count is
  hand-kept at `check-memory-hygiene.test.sh:528` and reads `PASS (101 assertions)` at `dae75003`.
- **AC13** When `sed -n 62p AGENTS.md` is read after this commit it contains `kit 1.8`, still
  contains `flat tree since kit 1.5`, and still carries the argv path
  `tools/memory-tree/check-memory-hygiene.sh`; `grep -rn 'FLAT (1.5)' tools/memory-tree/` still
  returns **3** hits (`check-memory-hygiene.sh:206`, `:243`, `:429` — measured 3, not 2); and
  `python tools/drift-audit/drift_report.py --check` exits 0 with
  `handkept_inventories_disagreeing_with_source` still at 7 of 38.
- **AC14** After this commit
  `git grep -l -F 'TOOL-aMendedLedger-' -- tools skills .claude parallel-coding-governance.template.md
  parallel-coding-governance.customize.md parallel-coding-governance.domain-rules.md
  WIRE-INTO-PROJECT.md` returns nothing, and `python tools/drift-audit/drift_report.py --check` exits
  0 with `non_terminal_specs_cited_by_product_source` still at 2 of 15. Measured today: zero hits,
  `2 15 ok (pin 2, drain it)`, `--check` rc 0.

## 7. Gates

Existing legs that must stay green: `bash tools/run-gates.sh` in full, 38 legs. Load-bearing for this
unit, by leg name: `memory hygiene (19 checks)`, `memory-hygiene self-test`, `harness arms (fail
branches armed or pinned)`, `check-arms selftest`, `verdict epoch (kit version dates the engine)`,
`verdict-epoch self-test`, `kit version markers`, `kit/dogfood doc parity`, `build-index selftest`,
`corpus-ids selftest`, `gotchas selftest`, `kickoff-manifest ratchet`, `drift-audit records`,
`codebase-map coverage + freshness`.

New leg: none. This unit adds no entry to `tools/gate-legs.json`, so the master's §7 coupling 3 — a
new leg needs an `AGENTS.md` bullet citing its argv script path, or
`handkept_inventories_disagreeing_with_source` ratchets past its pin of 7 — does not bind here. The
one-clause `AGENTS.md:62` edit adds prose beside an argv path that does not move, so that signal is
untouched (AC13).

Five couplings this unit must honour:

1. **The verdict epoch.** Any non-comment change to `tools/memory-tree/check-memory-hygiene.sh`
   forces `KIT_MEMORY_TREE_VERSION` to move in the same diff, in three places, plus a `--render`
   (`check-verdict-epoch.sh:134-140`). The rule is topological, not per-commit: the bump must sit at
   or after the newest engine-moving commit in the range. Consequence for the units after this one —
   no later unit may touch the engine or its three delegates (`gen_build_index.py`, `corpus_ids.py`,
   `gotchas.py`) without its own bump, because this unit's bump cannot date a change that comes after
   it.
2. **The kickoff manifest.** Its watch list is exactly seven pathspecs and this commit stages one of
   them, `tools/memory-tree/check-memory-hygiene.sh`. `manifest-check.sh` check C5s accepts only a
   re-stamp bundled in THAT SAME commit, so `last-audit` moves here, with the datetime from `date`.
3. **The arms floor.** `check-arms.py` floors are PER GATE and ONE-SIDED
   (`.memory-tree.conf:62` pins this gate at `14:14`). Deleting a `fail` branch reds; so does dropping
   a positive assertion. Do not delete branches and do not add a pin row — re-fixture instead. No edit
   in §4 touches a `fail` call site: `pop_guard` appends to `POP_MISSING`, and the report block at
   `:680-686` sets `status=1` directly rather than through `fail`, so the count stays 14.
4. **The build index.** Landing this sub-spec file changes what `gen_build_index.py` renders into
   `memory/builds/aMendedLedger/README.md`. Whichever commit adds the file must re-render it, or
   hygiene check 9 reds on a file nobody edited.
5. **No product-source file may cite this build's id while the spec is non-terminal.** `tools` is
   `PRODUCT_GLOBS[0]` (`drift_signals.py:20-28`), and `signal_spec_status`
   (`drift_report.py:235-271`) flags every non-terminal spec whose own H1 id `git grep`s inside those
   globs, against a pin of 2 that is already at its value (`drift_signals.py:128`; measured `2 15`).
   This unit edits four files under `tools/`, and the engine's own habit is the trap: the comment at
   `check-memory-hygiene.sh:348` cites `TOOL-aBatchedLintel-1` three lines below the `ex7` expression
   S4 rewrites, and `:472` and `check-memory-hygiene.test.sh:129` do the same. Those citations are
   not a precedent to copy — they ARE the pin. `drift_signals.py:120-123` names
   `TOOL-aBatchedLintel-1` and `TOOL-aGuardedTally-1` as the two INPROGRESS specs whose ids sit in
   tracked kit source, which is the whole of the measured `2`. There is no headroom: a provenance
   comment naming `TOOL-aMendedLedger-4` makes it 3 and reds the `drift-audit records` leg on this
   unit's own commit. Cite the build by SLUG (`aMendedLedger U3`) in any comment written under
   `tools/`, `skills/`, `.claude/`, the playbook template or its two companions, or
   `WIRE-INTO-PROJECT.md`. AC14 grades it.

Run `python tools/memory-tree/gotchas.py --for-diff 663ca427..HEAD` BEFORE the review. Measured on the
current range it selects five classes, and four of them are this unit's subject matter:
`vacuous-selector-empty-population` (S2), `two-answers-to-one-question` (S4),
`fixture-passes-by-finding-nothing` (S5, S6) and `gate-green-by-accident-on-generated-bytes` (the
rendered template).

## 8. Open questions

none — but the resolution KIND differs per fork, and rev-1 misstated it, so each is named with its
marker. All four master forks this unit executes carry an explicit `RESOLVED` line in
`memory/builds/aMendedLedger/spec/2026-08-09-spec-aMendedLedger-1.md` §8 as of that spec's rev-4:

- **F1** (`:354-362`) — tighten the `F:*.md` catch-all to the five registry names, repoint the two
  fixtures, replace check 6's arm with a >250-line `memory/guides/tfixture.md`.
  `RESOLVED (build, 2026-08-09)`.
- **F2** (`:363-371`) — retire the ledger for adopters too, in the same version bump. This is the
  ONE of the four the owner ruled on: `RESOLVED (owner, 2026-08-09)`. It is what obliges U6's S6b
  upgrade note (§5 risks).
- **F4** (`:377-379`) — scaffold all five registries, closed in U3 with the `memory/HYGIENE.md:81`
  correction. `RESOLVED (build, 2026-08-09)`.
- **F6** (`:390-394`) — fix the `MAP_SUB` `ex7` branch by appending rather than replacing.
  `RESOLVED (build, 2026-08-09)`. Master §3 `:47-48` now records the consequence in the same
  direction: the `check-memory-hygiene.sh:346` rewrite was OUT at master rev-2 pending F6 and is IN,
  in U3, now that F6 is ratified. S4 therefore executes a resolved fork, not a Non-goal.

rev-1 claimed "two of them owner-ratified"; measured, exactly one of the four is (F2), and the other
three carry the `(build, …)` marker the master rev-4 introduced precisely to keep the two kinds
distinguishable. The count matters because it says who may still overturn S4's verdict change.

The choices left open INSIDE those resolutions are ratified above rather than deferred: `F:README.md`
leaves the sub-lint with the rest (§4 Data model), `ex7` is rebuilt as base-plus-append (§4 Data
model), and AC10d is mechanized inside the self-test (§4 Alternatives rejected).

## 9. Revision log

- rev-1 · 2026-08-09 · initial draft, written to master rev-3 (`base 663ca427`, ratified 2026-08-09).
  Every line citation re-verified against source at `dae75003`. Four things the master left implicit
  are pinned here: the `F:README.md` entry leaves check 3's `project/` case list with the rest of the
  session machinery; `ex7` is rebuilt as one base plus one append rather than two spellings; AC10d is
  mechanized as an arm inside `check-memory-hygiene.test.sh` instead of a manual throwaway-repo run;
  and `memory/HYGIENE.md:46` and `:58` join the master's six named prose sites, because the master's
  list reaches 5 of the file's 6 measured hits.
- rev-2 · 2026-08-09 · folded the sub-spec review (items X1 and D3-1…D3-6), re-measured against the
  master at rev-4. H1 identity (X1): the id is now per-file `TOOL-aMendedLedger-4` with the unit
  label after the em-dash, so `gen_build_index.py:54`'s `H1_RE` matches instead of falling back to
  the basename, and six specs no longer share one id. §8 rewritten (D3-1): rev-1 said the four forks
  were "resolved … two of them owner-ratified", which was false in both directions — exactly one
  (F2) is owner-ratified, and at master rev-3 three of them were not resolved at all. Master rev-4
  ratified F1/F4/F6 as `RESOLVED (build, …)` and moved the `:346` `ex7` rewrite out of §3 Non-goals
  into U3, so §8 stays `none` and now names each fork with its marker and its master line range.
  The `AGENTS.md:62` edit (D3-2) was mandated three times with no target value; measured, nothing at
  `:62` is stale — its `1.5` names the FLATTEN release and agrees with seven other sites — so the
  edit became ADDITIVE, the replacement line is stated verbatim in §4 Migration, and AC13 grades
  both halves plus the argv path the `handkept` signal reads. AC3 (D3-3) now names a stray **`.md`**:
  a `.txt` or extensionless stray already falls through to `*)` at `:230` on the pre-edit engine, so
  the old fixture passed on both engines. AC7 and AC4 (D3-4) were unsatisfiable as written —
  `grep -c` counts lines, so two literals on line 13 can never return 2, and both ACs gave `grep -c`
  no path argument; AC7 now uses `grep -no`, which asserts count and line together and is immune to
  the `81.77s` substring at `:470` that already makes a bare occurrence count read 3. §4 Files
  touched and S6 (D3-5) over-counted the new scratch trees: the half-migrated tree AC2 targets
  already exists at `check-memory-hygiene.test.sh:491-499` and needs two edits — a
  `memory/architecture/project/legacy-files.txt` so `PRE_REGISTRY` is non-zero, and `3` added to its
  assertion loop at `:502` — while only the `.codebase-map.conf` tree is new. §4 Migration (D3-6)
  now states the AC6 arm's three scaffolder preconditions. §7 gained a fifth coupling: no file under
  `tools/`, `skills/`, `.claude/`, the playbook template or `WIRE-INTO-PROJECT.md` may carry this
  build's non-terminal id, graded by AC14 — a live trap here, since `check-memory-hygiene.sh:348`
  cites a spec id three lines below the `ex7` block S4 rewrites. Three review numbers were corrected
  against measurement rather than copied: `grep -rn 'FLAT (1.5)' tools/memory-tree/` returns 3 hits,
  not 2; the half-migrated tree starts at `:491`, not `:488` (`:488-490` are comment); and the test
  file is `set -u`, not `set -e` (`:10`).

## 10. Reuse audit

`CODEBASE_MAP_ROOT="$(git rev-parse --show-toplevel)" python tools/codebase-map/reuse_lookup.py "empty
population guard for a path selector over the project registries"` returns no seam: the top-ranked
symbol hits are fan-in 0-1 helpers in `map_lib.py`, `query.py` and `gotchas.py`, and the only SEAM in
the shortlist is `gotchas.Problem` as a same-file neighbour. That is the expected answer and not
evidence of absence — `RECALL_DARK_LAYERS="bash"` in `.codebase-map.conf` declares that this repo's
gates carry no symbol extractor, so a shell seam cannot appear in that list at all. The lookup's
useful output here is its inventory arm, which surfaces
`memory/gotchas/vacuous-selector-empty-population.md` — the class S2 exists to instrument.

The seams this unit wires through, all of them already in the engine or the kit, none reimplemented:

- `pop_guard` (`check-memory-hygiene.sh:123-128`) — the two-granularity empty-population guard, used
  by checks 4, 5, 8 and 12. S2 adds a fifth caller and writes no new guard.
- `index_set()` (`:303-320`) — the single population checks 6 and 7 share. Check 6's replacement arm
  rides its existing `guides/*.md` producer rather than adding one.
- `kit-dogfood-parity.test.sh --render` (`:54`) — the one path that writes
  `tools/memory-tree/HYGIENE.template.md`. S9 uses it; nothing hand-edits the shipped copy.
- `cblock` / `chit` / `cnot` (`check-memory-hygiene.test.sh:283-288`) — per-check output slicing, so
  every new path assertion is attributed to the check that must report it.
- `adopt-memory-tree.sh --scaffold` itself — used as the fixture GENERATOR for AC6, so the scaffolder
  is asserted against the gate rather than against a second description of the scaffolder.
