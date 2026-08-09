# TOOL-aMendedLedger-3 — U2: retire the authored session ledger and resolve the drift probe

**Status:** SPECCED · rev-2 · 2026-08-09 · node a · Tier-2 · base 663ca427 · streams tooling

## 1. Goal

Retire this repo's authored per-node session ledger to `memory/archive/ledger/` and resolve the
`drift-audit` probe that reads it, in ONE commit, so no revision of the default branch exists in
which a `gateable` drift signal is blind. Draining `memory/project/in-flight/` makes `signal_ledger`
report `live: False` while it stays `gateable: True`, and `drift_report.py --check` exits 1 on
exactly that state — `tools/drift-audit/drift_report.py:518` collects the dead gateable signals and
`:529` returns 1 for them. The master spec scopes this as S2 and S4 and its §4 Rollout binds the two
into one commit for that reason.

## 2. Scope (IN)

- **S1** `git mv memory/project/in-flight/{a,b,c}.md` to `memory/archive/ledger/{a,b,c}.md`,
  byte-identical, with git recording each as a 100% rename.
- **S2** Delete `memory/project/in-flight/.gitkeep`, and with it the directory.
- **S3** Resolve `signal_ledger` per the master's F3 exit: add `ledger_rows_contradicting_git` to
  `DECLARED_EMPTY` and retire its pin of 4, both in the PROJECT layer
  `tools/drift-audit/drift_signals.py`. The kit engine `drift_report.py` is not edited.
- **S4** Extend — never recreate — `memory/archive/ledger/README.md`, which U1 creates, with the
  retirement record for the three shards.
- **S5** Add a two-direction arm to `tools/drift-audit/selftest.py` asserting the signal reports
  empty by declaration on a drained fixture AND reports a value again on a fixture carrying a ledger
  row. This is master AC5 and the whole point of the unit: a declaration that could not be lifted
  would be the DEAD PROBE defect wearing a nicer label.
- **S5a** Regenerate `memory/map/generated/` in the SAME commit, because S5's new public top-level
  symbol makes the committed `symbols.json` stale and `codebase-map coverage + freshness`
  byte-compares it. Mechanical, but it is part of the one commit or the bar is red.
- **S6** Remove every ledger REFERENCE from `tools/workflows/drift-audit-state.js` — all ten sites,
  not the four the master's Files-touched row names — and re-key the surviving `work-state` lens on
  the generated build index. The lens itself stays; see §3.

## 3. Non-goals (OUT)

- **Editing `tools/drift-audit/drift_report.py`.** Both consumers of `DECLARED_EMPTY` already exist
  in the engine: `:490-493` picks the "empty by declaration" status line over "DEAD PROBE", and
  `:516-518` excludes declared signals from `--check`'s dead list. `ctx.ledger_dir` at `:406` stays
  `<memory_root>/project/in-flight`, which is correct for any adopter who still keeps a ledger.
- **F3's other two exits.** Deleting `signal_ledger` strands the selftest arms that ride it, and
  repointing `ctx.ledger_dir` at `memory/archive/ledger/` freezes the pin at 4 forever over an
  archive nobody may edit. The master's §8 F3 (`…-1.md:372-376`) is **RESOLVED (build, 2026-08-09)**
  on the `DECLARED_EMPTY` + retire-the-pin exit, naming AC5's two-direction arm as the control
  because the declaration alone only relabels the printed line; it rules the other two exits out on
  those same two reasons. Carried into §8 below so this unit's exit is not taken on trust.
- **`dangling_pointers_in_own_ledger`.** MEASURED at `dae7500`: it already prints
  `-1  0  DEAD PROBE`, because `_resolve_node_tag()` (`drift_report.py:424-438`) matches this
  machine's `USERNAME` against the charter registry and finds no row, returning before the ledger is
  ever read. That is a pre-existing, node-local, `gateable: False` condition this unit does not
  create and does not fix. Named here so it is not re-discovered; a follow-up owns it.
- **Deleting the `work-state` lens.** It answers the owner's literal question and `meta.whenToUse`
  at `drift-audit-state.js:7` promises five lenses. The ledger REFERENCES go; the lens stays.
  This DEPARTS from the master's §4 Rollout row for U2+U4 (`…-1.md:174`), which reads "the ledger
  lens deleted from `drift-audit-state.js`", so the reading is stated rather than assumed: the
  master's own §4 Files touched (`…-1.md:189-190`) scopes that file to `:38`, `:52`, the `${LEDGER}`
  clause at `:60` and the paragraph at `:178` — four line sites, not a lens deletion — and
  `ALL_LENSES` (`drift-audit-state.js:120-218`) holds no lens named "ledger" at all; its five slugs
  are `map-truth` (`:122`), `memory-rot` (`:140`), `charter-drift` (`:157`), `work-state` (`:175`)
  and `record-gate-integrity` (`:194`). The Files-touched line governs; the Rollout row is loose
  shorthand for the ledger-KEYED lens, which is `work-state`.
- **The hygiene gate's own ledger admissions** at `check-memory-hygiene.sh:228`, `:308` and
  `:345-346`, and the scaffolder at `adopt-memory-tree.sh:87, :94`. Those are U3, which also carries
  the kit version bump those edits force.
- **The three `.md` stubs, the two journals and the `bThriftyBellows` stub build folder** — U1.
- **Every governing doc** — U6. Two drift-audit docs need no edit at all and must not be swept into
  it: `tools/drift-audit/README.md:68` and `tools/drift-audit/SKILL.template.md:31` describe what
  `signal_ledger` DOES, and the signal survives, so both rows stay true.
- **`PLAY-aPrunedCeremony-5`**, whose subject retires with the ledger — U7.

## 4. Design

### Inventory

`git ls-files memory/project/in-flight` at `dae7500` returns four paths: `a.md`, `b.md`, `c.md` and
a 0 B `.gitkeep`. The three shards hold 6, 3 and 2 data rows.

`python tools/drift-audit/drift_report.py` at `dae7500` reports, with `--check` at rc 0:

| signal | value | of | pin | gateable | live |
|---|---|---|---|---|---|
| `ledger_rows_contradicting_git` | 4 | 11 | 4 | yes | yes |
| `non_terminal_specs_cited_by_product_source` | 2 | 15 | 2 | yes | yes |
| `shrink_only_lists_not_shrinking` | 3 | 4 | — | no | yes |
| `handkept_inventories_disagreeing_with_source` | 7 | 38 | 7 | yes | yes |
| `dangling_pointers_in_own_ledger` | -1 | 0 | — | no | no |

Row one is the probe this unit resolves. Row five is already dead for the unrelated reason in §3.

Row two's `of` is **15**, not the 10 an index-scoped reading would predict: `signal_spec_status`
globs the WORKTREE, not the index (`drift_report.py:241`, `ctx.root.glob(...)`), so the five
untracked sibling unit specs beside this one are already inside `of` before anyone stages them.
Its pin of 2 is therefore already at its value — see §7 coupling 6.

### Data model

The F3 exit is a PROJECT-LAYER declaration, not an engine change, and that is what makes it cheap
and correct. `drift_signals.py` gains one set member and loses one pin:

```python
DECLARED_EMPTY: set[str] = {
    # The authored per-node session ledger was RETIRED by the aMendedLedger U2 unit: its three shards
    # moved to memory/archive/ledger/ and memory/project/in-flight/ no longer exists, so this
    # probe's population is empty BY DESIGN rather than blind. The kit ENGINE is untouched —
    # drift_report.py still reads <memory_root>/project/in-flight/*.md for adopters who keep a
    # ledger — and the declaration is not a muzzle: put one row back and the probe goes live and
    # scores again. selftest.py asserts both directions over one fixture.
    "ledger_rows_contradicting_git",
}
```

```python
PINS: dict[str, int] = {
    # ledger_rows_contradicting_git carries NO pin. Its population is empty by declaration (above),
    # and a pin of 4 over an empty population is a ratchet that can never turn. If a ledger ever
    # returns, the default tolerance of 0 is the right bar — not a number measured against rows that
    # no longer exist.
    "non_terminal_specs_cited_by_product_source": 2,
    ...
}
```

The pin entry at `drift_signals.py:119` and its six-line comment at `:113-118` are deleted together;
the comment describes a measurement over rows that stop existing, so leaving it is a false record.

**The comment carries the build SLUG, never an id, and that is load-bearing rather than stylistic.**
`drift_signals.py` lives under `tools/`, which is `PRODUCT_GLOBS[0]` (`drift_signals.py:20-28`), and
`signal_spec_status` (`drift_report.py:235-271`) flags every non-terminal spec whose own H1 id
`git grep`s inside those globs — writing `TOOL-aMendedLedger-3` there would certify THIS spec as
shipped and push `non_terminal_specs_cited_by_product_source` off its pin of 2
(`drift_signals.py:128`), redding the `drift-audit records` leg on this unit's own commit. Measured
at `dae7500`: `git grep -l -F TOOL-aMendedLedger- -- tools skills .claude
parallel-coding-governance.template.md WIRE-INTO-PROJECT.md` returns nothing, and the signal reads
`2 15 ok (pin 2)`. AC13 keeps it that way. The same ban covers every other file this unit edits
under `tools/`.

Why the resulting state is green rather than merely quiet: `--check` builds `over` from signals that
are gateable AND live AND above pin (`drift_report.py:517`), and `dead` from gateable, not live and
NOT declared (`:518`). After the drain `signal_ledger` returns `value 0, of 0, live False`
(`:207-220`, since `ctx.ledger_dir.is_dir()` is false at `:176`), so it is absent from `over` by
liveness and from `dead` by declaration. The other two gateable signals are unmoved by this unit.

### Migration

| path | action | destination |
|---|---|---|
| `memory/project/in-flight/a.md` | `git mv` | `memory/archive/ledger/a.md` |
| `memory/project/in-flight/b.md` | `git mv` | `memory/archive/ledger/b.md` |
| `memory/project/in-flight/c.md` | `git mv` | `memory/archive/ledger/c.md` |
| `memory/project/in-flight/.gitkeep` | `git rm` | — (the directory goes with it) |

`git mv` renames the index entry and never re-reads the blob, so `* text=auto` in `.gitattributes`
cannot re-normalise the bytes and the similarity index is 100 by construction. Nothing else in the
commit may touch those three files.

Four hygiene properties were checked at source before choosing `memory/archive/ledger/` as the
destination, and each one holds:

- Check 3's root case at `check-memory-hygiene.sh:212` admits `D:archive`, and the root scan at
  `:209` is depth-2, so `archive/` is opaque and a nested `ledger/` folder under it is invisible to
  the structure lint. Check 3's project case at `:224-230` ADMITS `D:in-flight` rather than
  requiring it, so the directory's disappearance is not a finding either.
- Check 2 exempts `archive/` at `:163`, so the shards' links stop being scanned the moment they
  land. That is the reason the retirement README must cite paths in backticks and not as relative
  `.md` links: a link under `archive/` is policed by nothing and would rot in silence.
- Checks 6 and 7 read `INDEX_SET` (`:303-321`), whose only AUTHORED-ledger member is
  `^$M/project/in-flight/[^/]+\.md$` at `:308` (the `^$M/ledger/[^/]+\.md$` member at `:306` is the
  GENERATED monthly shard and is untouched here). That selector simply matches nothing afterwards,
  and the moved shards join no other member, so the 20 KiB / 250-line cap and the 300-char entry
  budget never see them. Several rows in `a.md` are far over 300 chars today and survive only
  through the `ex7` exemption at `:345-346` — `:345` is the no-map spelling and `:346` overwrites it
  unconditionally whenever `$MAP_SUB` is set, which it is here (`.codebase-map.conf` carries
  `MAP_ROOT=memory/map`), so the branch this repo actually takes is `:346`; both spellings keep the
  same `/in-flight/[^/]+\.md$` alternative, so the reasoning holds on either. Under `archive/` the
  rows need no exemption at all.
- Check 10 at `:430` scans `^$M/archive/[^/]+\.[0-9]{4}-[0-9]{2}-[0-9]{2}\.md$` — direct children
  with a rotation-dated name. `memory/archive/ledger/a.md` matches neither shape.

The id and path corpus is invariant under the move. `corpus_ids.py` collects anchors and citations
over every tracked file under `memory/` at `:208-221`, BEFORE the present-tense and append-only
guard at `:225`, so `defs` and `cites` do not change and checks 13 and 14 cannot move. The dead-path
harvest at `:227-257` can only SHRINK: `present` at `:198-201` admits `project/` and the append-only
ERE — read out of the hygiene engine at `corpus_ids.py:196` and DEFINED at
`check-memory-hygiene.sh:47` — excludes `archive/`, so `a.md`'s backticked `memory/builds/...`
citations leave the harvested population entirely. `DEAD_PATH_PIN` is `"0"` (`.memory-tree.conf:42`)
with an empty registry, and shrinking a population measured at 0 is a no-op. No registry file names
a moving path: `legacy-files.txt` lists five `memory/builds/` recordings, `curation-debt.txt` and
`corpus-path-unresolved.txt` are comment-only, so neither of the two stale-line guards at
`check-memory-hygiene.sh:669-674` can fire.

`memory/backlog/PLAY.md:5` cites `` `in-flight/b.md` ``. It is not a finding in either direction:
`corpus_ids.py:231` requires a token rooted at a real top-level directory of the repo, and
`in-flight/` is not one. U7 rewrites that row.

### Rollout

**S6, stated line by line** so the builder does not invent it. Line numbers verified against
`tools/workflows/drift-audit-state.js` at `dae7500`.

The population is `grep -nio ledger tools/workflows/drift-audit-state.js`: **twelve matches on nine
distinct lines** — 9, 38, 52 (×2), 60 (×2), 144, 178 (×2), 187, 189, 339 — plus `:191`, which
carries the ledger's vocabulary ("no row") without the word itself. Ten sites; the table below
covers every one of them (`:187-189` is one row spanning two, and `:179-181` names none of them but
is rewritten with its neighbours).
rev-1's table covered six of the nine ledger lines; the three it missed — `:9`, `:144`, `:339` — are
all lowercase, which is precisely what rev-1's AC7 selector (`LEDGER|ledgerGlob`) cannot see, so
that AC passed by finding nothing while three live instructions to audit a retired mechanism
survived. AC7 is restated in §6 for the same reason.

| line | action |
|---|---|
| `:9` | rewrite `meta.phases[0].detail` to `'primed lenses over the memory tree, charter and generated build index'` |
| `:38` | delete the `ledgerGlob:` line from the `args` documentation block |
| `:52` | delete `const LEDGER = a.ledgerGlob \|\| ...` |
| `:60` | rewrite: drop the `its per-node in-flight ledger \`${LEDGER}\`,` clause |
| `:144` | rewrite the `memory-rot` spec-status bullet to `cross-reference the generated build index, the decision indexes` |
| `:178` | rewrite: the `work-state` lens opens on the generated build index, not the ledger |
| `:179-181` | rewrite: the base-sha-versus-work-sha rule now reads over records, not ledger rows |
| `:187-189` | rewrite: worktree resolution and freshness, keyed on records rather than the ledger |
| `:191` | rewrite: "no row accurately says so" becomes "no record accurately says so" |
| `:339` | rewrite the Synthesize brief's STATE ANSWER to `how many build records contradict git` |

`:9` sits inside the `meta` object but well clear of `version: '1.0'` at `:3`, which
`tools/check-kit-versions.sh:57` reads — the phase label is prose and carries no version token.
`:144` and `:339` are the `memory-rot` lens and the Synthesize brief, NOT the `work-state` lens: both
instruct a session to cross-reference a mechanism that no longer exists, which is the same defect
the widened `work-state` rewrite exists to remove.

`:60` and `:178` are the only two `${LEDGER}` interpolations in the file, and both MUST go with the
const at `:52`. `check-workflow-syntax.js` constructs the file as an async function body and a
template literal naming an undeclared identifier PARSES — the failure would be a ReferenceError at
run time, which no gate here catches. The replacement body for the lens brief:

```
The GENERATED build index (\`${MEM}/LIVE.md\` and \`${MEM}/ledger/<month>.md\`) is the record of who
touched what. It is DERIVED from build front matter, so test it against git rather than trusting it.
 - For each build the index calls non-terminal: does git agree? Separate a record's BASE sha ("off
   \`X\`") from its WORK shas — the base is an ancestor by construction and proves nothing, and
   conflating them makes every record a false positive. Report the real count that contradicts git.
 - The inverse and more dangerous direction: work claimed as LANDED that is NOT an ancestor of
   ${BASE}, and work sitting on branches nobody tracks.
 - Say explicitly what is STRUCTURALLY UNKNOWABLE from this clone. Other nodes are other machines;
   their landed work is visible, their working trees are not. An audit that pretends to see them is
   worse than one that names the blind spot. Name the unknowables.
 - Do the branches and worktrees any record names still resolve? A pointer at a deleted worktree is
   work nobody can resume. Be careful to judge only THIS node's paths.
 - Is the index still a byte-identical render of its source, or has someone hand-edited it?
 - The bottom line the owner needs: is there work that is BUILT, GATED, REVIEWED and simply LOST —
   nobody merged it and no record accurately says so? Name it, or state plainly that there is none.
```

`${MEM}` and `${BASE}` stay declared at `:50` and `:48`. `ALL_LENSES` keeps all five entries, so the
`gov:fixed-verifiers` count the fan-out gate reads at `:222` and `:260` is unchanged and
`meta.whenToUse` at `:7` stays true. An adopter still passing `args.ledgerGlob` is unharmed: an
unread key is ignored.

**S5, the two-direction arm.** `make_repo` at `selftest.py:152` hardcodes `r = tmp / "repo"`, and
`test_signals_can_move` mutates that fixture through eight arms and finally unlinks its
`drift_signals.py` at `:324`. Rather than thread a ninth arm through that sequence, give `make_repo`
a `name: str = "repo"` parameter and build a SECOND fixture. Add `test_declared_empty(tmp)` and call
it from `main()` after `test_signals_can_move(tmp)`. It wires through the existing `run`, `report`
and `check` helpers — no new harness.

Direction one, drained and declared. Delete `memory/project/in-flight/*.md` and the directory, add
`ledger_rows_contradicting_git` to the fixture's `DECLARED_EMPTY`, commit, then assert three things:
the JSON signal reports `live is False` with `value == 0`; `--check` exits 0; and the human table's
`ledger_rows_contradicting_git` row contains `empty by declaration` and NOT `DEAD PROBE`. The third
assertion is the one that discriminates — the first two hold for a signal that is merely ignored.

Direction two, a row returns. Capture the short HEAD sha, recreate the directory with a single row
of the shape `make_repo` already writes at `:177-180` (`| \`aThing\` | \`feature/x\` off \`BASESHA\`
| in-flight — NOT merged, work at \`<sha>\` |`), drop the signal from `DECLARED_EMPTY`, commit, then
assert `live is True`, `value == 1`, and `--check` exiting 1 with the signal named on stderr. That
sha is an ancestor of the fixture's `main`, so the row is an open claim about landed work, which is
`signal_ledger`'s firing case at `drift_report.py:203-206`. `BASESHA` is deliberately not hex, so
`_SHA` at `:164` finds exactly one sha and the arm isolates the oracle.

The second direction is what makes the arm worth writing. A one-sided arm proves the declaration
silences the probe, which is exactly what a broken probe also does.

**S5a, the map artifacts, in the SAME commit.** `test_declared_empty` is a PUBLIC TOP-LEVEL Python
symbol, and `memory/map/generated/symbols.json` enumerates exactly those — it already carries nine
entries for this one file (`check`, `main`, `make_repo`, `report`, `resolve_posix_shell`, `run`,
`skip`, `test_conf_parser_matches_bash`, `test_signals_can_move`). `test_generated_artifacts_are_fresh`
(`tools/codebase-map/test_codebase_map.py:94-112`) byte-compares the committed artifact against a
fresh render and fails `STALE symbols.json` if it moved, which reds the `codebase-map coverage +
freshness` leg and therefore AC12. So: run `python tools/codebase-map/gen_map.py --write` and stage
`memory/map/generated/` in this unit's single commit. `make_repo`'s new `name` parameter is INVISIBLE
to the render — a symbol record holds `id`, `kind` and `file` only, no signature — so the one new
function is the whole delta, and `inventories.json` / `MAP.md` are expected not to move. Verify with
`python tools/codebase-map/gen_map.py --check` (rc 0) rather than by assumption; AC14 is the gate.

**S4, the retirement record.** U1 creates `memory/archive/ledger/README.md` and moves
`IN-FLIGHT.md`'s protocol prose into it. U2 APPENDS a section that states: the three shards, the
retirement date, the master decision that retired them (F2 and F5, retire everywhere), that they are
frozen because `archive/` is append-only territory under `check-memory-hygiene.sh:47`, and that work
state now comes from the generated `memory/LIVE.md` and `memory/ledger/<month>.md`. Paths in
backticks, no relative links, for the reason in the Migration sub-head above. The commit must show
this file as `M`, never `A`.

### Files touched (estimate)

Moved: `memory/project/in-flight/{a,b,c}.md`. Deleted: `memory/project/in-flight/.gitkeep`.
Edited: `tools/drift-audit/drift_signals.py`, `tools/drift-audit/selftest.py`,
`tools/workflows/drift-audit-state.js`, `memory/archive/ledger/README.md`,
`memory/map/generated/symbols.json` (REGENERATED, never hand-edited — S5a; add
`memory/map/generated/MAP.md` and `inventories.json` only if the render actually moves them).
Not edited, deliberately: `tools/drift-audit/drift_report.py`, `tools/drift-audit/README.md`,
`tools/drift-audit/SKILL.template.md`, `.claude/skills/drift-audit/SKILL.md`, `tools/gate-legs.json`,
`AGENTS.md`, `memory/map/features/*.md` (no dossier claim moves: this unit adds no gate leg, no kit,
no hook and no workflow script).

### Alternatives rejected

**Two commits, move then resolve.** Rejected because it is a red bar by construction: between them
`signal_ledger` is gateable, not live and not declared, which is precisely the `dead` list at
`drift_report.py:518`. The `.githooks/pre-push` hook runs the full bar on the pushed tip only, so
the red would be invisible to the push boundary and visible to anyone who checked out the middle
commit — the worst of both.

**Declaring `dangling_pointers_in_own_ledger` too.** Tempting, because after the drain its
population is empty on purpose on every node. Rejected: the master's F3 names one signal, the probe
is already dead at `dae7500` for a different and node-local reason, it is `gateable: False` so
nothing reds either way, and the fixture's charter carries no matching registry row so no portable
selftest arm could assert the declaration. An unassertable declaration is decoration.

**Deleting the `work-state` lens outright.** Rejected: the lens answers the commissioning question
the workflow exists for, and deleting it would drop `ALL_LENSES` (`:120-218`) to four while
`meta.whenToUse` (`:7`) and the `lenses` arg enum documented at `:43` still promise five.

## 5. Production-readiness checklist

- security — N/A. No auth, egress or sanitization surface; the change moves three tracked files and
  edits a declaration set.
- perf / scale — no measurable change. `signal_ledger` stops walking a directory that no longer
  exists; the selftest gains one throwaway fixture repo.
- a11y — N/A. No user interface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — the empty state IS the feature: an empty population must report
  as declared rather than as dead, which is direction one of the S5 arm.
- observability — `drift_report.py` is the instrument, and this unit's whole risk is leaving it
  unable to MOVE rather than merely silent. AC5 is the control.
- risks — data-loss on a `git mv` that is not byte-identical (AC2), and a permanently muzzled probe
  (AC5). Rollback is `git revert` of the single commit; there is no external state.
- testing + left-shift gates — no new gate leg. The existing `drift-audit selftest` leg
  (`tools/gate-legs.json`, argv `python tools/drift-audit/selftest.py`) already runs the file the
  new arm lands in, so coverage arrives without touching the manifest.
- migration / rollback — no adopter data moves and no adopter gate changes. The kit engine is
  untouched; an adopter who keeps a ledger keeps a working signal.
- user docs — none in this unit. The drift-audit README and Skill rows stay true (§3); every other
  doc surface is U6.

## 6. Acceptance criteria

- **AC1** When `git ls-files memory/project/in-flight` is run after this commit it returns nothing,
  and `test -d memory/project/in-flight` is false.
- **AC2** When `git log --follow --find-renames --name-status` is run over each of
  `memory/archive/ledger/{a,b,c}.md`, each shows `R100` from its `memory/project/in-flight/` path
  with no content change.
- **AC3** When `python tools/drift-audit/drift_report.py` is run, the
  `ledger_rows_contradicting_git` row reads `0  0  empty by declaration — nothing to measure here
  yet`, and the string `DEAD PROBE` appears on no `gateable` signal's row.
- **AC4** When `python tools/drift-audit/drift_report.py --check` is run it exits 0 and prints
  nothing on stderr.
- **AC5** When `tools/drift-audit/drift_signals.py` is read, `ledger_rows_contradicting_git` appears
  in `DECLARED_EMPTY` with the reason in a comment beside it, and appears nowhere in `PINS`.
- **AC6** When `python tools/drift-audit/selftest.py` is run it exits 0 with no SKIP for the new
  arm, and the arm asserts BOTH directions: on the drained fixture the signal is not live, `--check`
  exits 0 and the table row says `empty by declaration`; on the same fixture with one ledger row
  restored and the declaration dropped, the signal is live with `value == 1` and `--check` exits 1
  naming `ledger_rows_contradicting_git`.
- **AC7** When `git grep -nE 'LEDGER|ledgerGlob' -- tools/workflows/drift-audit-state.js` is run it
  returns nothing, AND when `git grep -niE 'ledger' -- tools/workflows/drift-audit-state.js` is run
  the only surviving hits are the lowercase `${MEM}/ledger/<month>.md` path citations inside the
  `work-state` lens brief — the GENERATED monthly shard, not the authored one. The uppercase-only
  selector on its own passes by finding nothing while `:9`, `:144` and `:339` still name the retired
  mechanism, which is why both clauses are required. `node tools/workflows/check-workflow-syntax.js`
  exits 0 and `ALL_LENSES` (`drift-audit-state.js:120-218`) still holds five entries.
- **AC8** When `git show --stat` is read for this unit's commit, it lists no change to
  `tools/drift-audit/drift_report.py`, and `bash tools/check-kit-versions.sh` exits 0 with
  `KIT_DRIFT_AUDIT_VERSION` still `"1.0"`.
- **AC9** When `git show --stat` is read for the same commit, `memory/archive/ledger/README.md`
  appears as modified rather than added, and its new section names all three shards.
- **AC10** When `git rev-list --count` is taken over this unit's work it is 1: the move, the
  deletion, the resolution and the selftest arm are one commit.
- **AC11** When `python tools/memory-tree/corpus_ids.py --report` is run after the commit, the
  orphan-id set is unchanged at the five pinned entries and `dead path cites` is 0.
- **AC12** When `bash tools/run-gates.sh` is run at this commit, all 38 legs are green.
- **AC13** When `git grep -F 'TOOL-aMendedLedger-' -- tools skills .claude
  parallel-coding-governance.template.md parallel-coding-governance.customize.md
  parallel-coding-governance.domain-rules.md WIRE-INTO-PROJECT.md` is run after this commit it
  returns nothing (rc 1). Those seven pathspecs are `PRODUCT_GLOBS` verbatim
  (`tools/drift-audit/drift_signals.py:20-28`); no `FAMILY-slug-seq` id of a non-terminal spec may
  appear inside them, so the retirement comment in `drift_signals.py` cites the build by SLUG.
- **AC14** When `python tools/codebase-map/gen_map.py --check` and
  `python tools/codebase-map/test_codebase_map.py` are run after this commit, both exit 0 —
  `test_generated_artifacts_are_fresh` included, so `memory/map/generated/symbols.json` is a
  byte-identical render of a tree that already holds `test_declared_empty`.

## 7. Gates

Existing legs that must stay green: `bash tools/run-gates.sh` in full, 38 legs at `dae7500`.
Load-bearing here, spelled as `tools/gate-legs.json` spells them — `memory hygiene (19 checks)`,
`drift-audit records`, `drift-audit selftest`, `drift-audit wiring`, `kit version markers`,
`workflow script syntax`, `verifier fan-out (≤5 verify agents per review)`,
`review-join ban (no ref-keyed join)`, `corpus-ids selftest`, `build-index selftest`,
`codebase-map coverage + freshness`.

No new gate leg. `tools/gate-legs.json` is not staged.

**The commit that LANDS this spec is not the build commit, and it has its own obligation.**
`gen_build_index.py` renders one row per spec under `memory/builds/aMendedLedger/`, so adding a
recording under `spec/units/` moves the `<!-- gen:build-index -->` block that hygiene check 9
byte-compares against a fresh render — measured in the closing review by `git add -N` on the spec
alone, which took the gate from rc 0 to rc 1 with `HYGIENE check 9 FAILED — generated build index
differs from a fresh render`. The landing commit must run
`python tools/memory-tree/gen_build_index.py --write` and stage the three paths that renderer owns:
`memory/builds/aMendedLedger/README.md`, `memory/LIVE.md` and `memory/ledger/2026-08.md`. None of
the three is a WATCHED pathspec, so this still carries no `last-audit` re-stamp (coupling 2).

The master's three §7 couplings, each checked against this unit's diff rather than assumed:

1. **`KIT_MEMORY_TREE_VERSION`** moves only for a non-comment change to
   `tools/memory-tree/check-memory-hygiene.sh`. This unit does not touch that file, so
   `check-verdict-epoch.sh` is not engaged. U3 owns the 1.7 to 1.8 bump.
2. **The kickoff manifest watches seven pathspecs**, read at `.claude/SESSION-KICKOFF.md:6`:
   `tools/memory-tree/check-memory-hygiene.sh`, `tools/check-template-size.sh`,
   `tools/run-gates.sh`, `tools/gate-legs.json`, `skills/session-kickoff/manifest-check.sh`,
   `.memory-tree.conf`, `parallel-coding-governance.template.md`. This unit stages NONE of them, so
   it carries no `last-audit` re-stamp. Do not add one defensively.
3. **A new gate leg needs an `AGENTS.md` bullet citing its argv script path** or
   `handkept_inventories_disagreeing_with_source` rises by one against its pin of 7. This unit adds
   no leg, so that signal is unmoved.

Three further couplings this unit's diff DOES touch, numbered on from the master's:

4. **`tools/check-kit-versions.sh:57`** requires `version: '<X.Y>'` inside `drift-audit-state.js`'s
   `meta` block. It sits at `:3` and must survive the S6 edits — including the `:9` phase-label
   rewrite, six lines below it inside the same `meta` object.
5. **`tools/workflows/check-review-join.sh`** bans a ref-keyed verdict join in any `tools/**/*.js`.
   The join at `drift-audit-state.js:303-308` is keyed on `typeof v.id === 'number'`, the sanctioned
   form, and S6 does not go near it.
6. **`tools/` is `PRODUCT_GLOBS[0]`** (`tools/drift-audit/drift_signals.py:20-28`). Any
   `FAMILY-slug-seq` spec id written into a tracked file under `tools/`, `skills/`, `.claude/`, the
   three `parallel-coding-governance.*.md` files or `WIRE-INTO-PROJECT.md` certifies the
   non-terminal spec carrying that id as SHIPPED, via `signal_spec_status`
   (`tools/drift-audit/drift_report.py:235-271`), and pushes
   `non_terminal_specs_cited_by_product_source` past its pin of 2 (`drift_signals.py:128`) — a pin
   already sitting at its measured value, so ONE citation reds the `drift-audit records` leg and
   takes AC4 and AC12 with it. This unit edits three files under `tools/`, so the rule binds it
   directly: cite the build by SLUG (`aMendedLedger U2`), never by id. AC13 is the assertion.

Run `python tools/memory-tree/gotchas.py --for-diff 663ca427..HEAD` before the review, not after.

## 8. Open questions

- **F3 — `signal_ledger`'s fate. RESOLVED (build, 2026-08-09) in the master, §8 F3
  (`…-1.md:372-376`).** Carried here rather than referenced, so a reviewer of this unit does not have
  to open the master to see what authorises S3. The master picks **`DECLARED_EMPTY` + retire the
  pin** over the two alternatives it enumerates — deleting the signal (17 selftest references ride
  it; re-measured here, `grep -c ledger tools/drift-audit/selftest.py` → 17) and repointing
  `ctx.ledger_dir` at `memory/archive/ledger/` (the pin would read 4 forever over
  an archive nobody may edit) — and names AC5's two-direction selftest arm as the control, because
  the declaration alone only relabels the printed line. S3 and S5 implement exactly that and nothing
  more. Nothing here is left for the owner; the entry is a record, not a question.
- **F-U2-1 — does `KIT_DRIFT_AUDIT_VERSION` move from 1.0?** This unit edits two files an adopter
  receives (`selftest.py` and `drift-audit-state.js`) alongside one they own (`drift_signals.py`),
  so a deployer reading the version constant cannot tell a kit with a ledger lens from one without.
  Nothing forces the bump: `tools/check-kit-versions.sh:47-55` only asserts that the constant in
  `drift_report.py` and the `gov:kit drift-audit@<X.Y>` marker in `tools/drift-audit/README.md`
  agree, and the master schedules no drift-audit bump anywhere.
  **Recommendation: no bump in this unit.** The behaviour change adopters actually see is the
  retirement itself, which U6 announces through the `WIRE-INTO-PROJECT.md` upgrade note (master
  S6b), and a version bump landed in the middle of a seven-unit chain would date the kit to a state
  the chain has not finished reaching. If the owner wants one, it belongs in U6 beside the note, and
  it costs the constant plus the README marker plus the four `gov:kit drift-audit@1.0` comment
  markers in `drift_report.py:4`, `drift_signals.py:3`, `selftest.py:4` and
  `drift-audit-state.js:15`. Absent an owner answer the builder takes the recommendation.

## 9. Revision log

- rev-1 · 2026-08-09 · initial draft, written to the master `TOOL-aMendedLedger-1`, whose header
  carries `ratified 2026-08-09`, and grounded on source at `dae7500`. Every line number cited was
  opened rather than recalled. The F3 exit was confirmed
  to need NO engine edit, which the master's brief framed as a `drift_report.py` change — the two
  `DECLARED_EMPTY` consumers already ship at `:490-493` and `:516-518`. `drift_report.py` was RUN
  rather than reasoned about, which found `dangling_pointers_in_own_ledger` already dead at HEAD for
  an unrelated node-local reason and kept it out of scope. The S6 edit was widened from the master's
  four line sites to the ledger-keyed bullets inside the same lens, because leaving them would have
  left a live agent brief instructing a session to audit a retired mechanism — the exact defect the
  `memory-rot` lens names three lines above at `:150-151`.
- rev-2 · 2026-08-09 · folded the closing sub-spec review (X1 + D2-1…D2-8), every cited line
  re-opened at `dae7500` rather than trusted from the review. **H1 (X1):** the id is now
  `TOOL-aMendedLedger-3`, one seq per unit with the `U2:` label after the em dash — rev-1's
  `# TOOL-aMendedLedger-1 U2 — …` did not match `gen_build_index.py:54`'s `H1_RE` at all (the id
  must be followed immediately by ` — `), so `parse_spec` fell back to the filename with an empty
  title, and six specs sharing one id reproduces the slug-keying shape `drift_report.py:228-231`
  records as over-flagging 107/126 upstream. **BLOCKING D2-1:** the `DECLARED_EMPTY` comment cited
  this spec's own id inside `tools/`, which is `PRODUCT_GLOBS[0]` — it now cites the build by slug,
  §7 gained coupling 6 and §6 gained AC13. **BLOCKING D2-2:** the new `test_declared_empty` is a
  public top-level symbol, so `memory/map/generated/symbols.json` goes stale in the same commit;
  S5a, the Files-touched row and AC14 close it. **D2-3:** the S6 table was six of nine ledger lines;
  `:9`, `:144` and `:339` are added and AC7 is restated, because the uppercase-only selector passed
  by finding nothing. **D2-4:** the LANDING commit must regenerate the build index. **D2-5:** the
  `of` cell for `non_terminal_specs_cited_by_product_source` was 10 and measures 15 — the signal
  globs the worktree, not the index. **D2-6:** rev-1 said "the master rejected both"; the master's
  §8 F3 now reads `RESOLVED (build, 2026-08-09)` at its fourth revision, all six master forks being
  resolved as of that revision, and that resolution is quoted in §3 and
  carried into §8. **D2-7:** the departure from the master's §4 Rollout row for U2+U4 is now stated
  and argued from its own §4 Files touched. **D2-8:** the `ex7` citation moved from `:345` to
  `:345-346`, since this repo takes the `MAP_SUB` branch. Four further precision fixes the review
  did not raise, each re-measured here: the review's own `drift_report.py:239` for the worktree glob
  is `:241`, and its `signal_spec_status` `:235-270` is `:235-271`; the bare `:47` for the
  append-only ERE read as a `corpus_ids.py` line and now names `check-memory-hygiene.sh` explicitly
  (read at `corpus_ids.py:196`); the INDEX_SET bullet now distinguishes the authored `:308` selector
  from the generated `:306` one; and §7's leg names are spelled as `tools/gate-legs.json` spells
  them.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py` over the map with `CODEBASE_MAP_ROOT` set to the repo
root (the prefixed-install workaround recorded in `memory/map/features/codebase-map.md` §Gaps), for
"declare a drift signal empty on purpose so its report does not call it a dead probe", returns 244
symbols and one seam above threshold that matters here: `report` in `tools/drift-audit/selftest.py`,
fan-in 13, SEAM. That is exactly the seam S5 wires through — the new arm calls the existing
`report(r, *extra)` helper at `selftest.py:219` and the existing `run` and `check` helpers rather
than standing up a second harness. `make_repo` is EXTENDED with a `name` parameter rather than
copied, for the same reason.

The other declared seams this unit rides, none of them invented here: `DECLARED_EMPTY` itself, which
`drift_report.py` already reads in both of its consumers; the `drift-audit selftest` leg already in
`tools/gate-legs.json`, which is why no manifest edit is needed; and `git mv` plus git's own rename
detection as the byte-identity mechanism, rather than a copy-and-delete that AC2 could not verify.

No seam fits the retirement record in `memory/archive/ledger/README.md`, and none is wanted: it is
prose, and U1 already owns the file.
