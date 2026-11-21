# TOOL-dPlacedRequest-99 — the closing review's minors: every plant on a gate, a resolver arm, honest re-fence and card outcomes, a re-priced row and three loose ends

**Status:** CLOSED · rev-2 · 2026-11-21 · node d · Tier-2 · base 95c3103a · streams tooling · order 37

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-21-build-TOOL-dPlacedRequest-99-1-acceptance-ledger.md](../build/2026-11-21-build-TOOL-dPlacedRequest-99-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-build-TOOL-dPlacedRequest-99-deviation-734.md](../build/2026-11-21-build-TOOL-dPlacedRequest-99-deviation-734.md) | deviation | — |
| [2026-11-21-build-TOOL-dPlacedRequest-99-red-fix-35.md](../build/2026-11-21-build-TOOL-dPlacedRequest-99-red-fix-35.md) | red-fix | — |
| [2026-11-21-build-TOOL-dPlacedRequest-99-red-fix-48.md](../build/2026-11-21-build-TOOL-dPlacedRequest-99-red-fix-48.md) | red-fix | — |
| [2026-11-21-build-TOOL-dPlacedRequest-99-red-fix-53.md](../build/2026-11-21-build-TOOL-dPlacedRequest-99-red-fix-53.md) | red-fix | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-95-audit-fold-text-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-95-audit-fold-text-brief.md) | research | TOOL-dPlacedRequest-95 TOOL-dPlacedRequest-98 |
| [2026-11-20-prompt-TOOL-dPlacedRequest-99-closing-review-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-99-closing-review-spec-brief.md) | research | — |
| [2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-95 TOOL-dPlacedRequest-96 TOOL-dPlacedRequest-97 TOOL-dPlacedRequest-98 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build confirmed two MEDIUM items in round 1
(`memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md`)
and three MEDIUM and three LOW items in round 2
(`memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md`).
Round 2's exit batched all eight into this one unit, as the severity rule of
`doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it` orders. None
ships a wrong result today except round 2's M1 and M2, an aborted run and a stale build card; the rest
are checks that cannot fail, a budget row priced for half its suite, dead plumbing and a usage line
that omits two exits. Each scope item below takes the record's fix, the skeptic's class-level fix where
the record gives one, and the record's left-shift where it fits this unit's write set, else a
bug-class checklist entry.

## 2. Scope (IN)

- **S1** — Round 1 M1, finding id 4, fix judged SOUND. The plant loop of
  `skills/session-kickoff/manifest-check.test.sh` reads its names from `card-store.fixture.sh --list`
  instead of a hand-typed list of 8, and a liveness row asserts the number of plants run equals the
  number `--list` prints, both under the suite's existing `[ -f "$cs_fx" ]` test. `FLOOR_ASSERTIONS`
  rises by the rows the loop gains, the floor comment's stale count is corrected, the suite's `TMP` is
  normalised to forward slashes before the plants read it, and the `manifest-check self-test` row of
  `tools/run-gates/selftest-budgets.txt` is re-priced for the whole suite with every plant `--list`
  prints once S4's four are in, with the leg's ceiling compared by S5's procedure, both by §4. A plant
  that misses once gated is fixed in this unit where its cause lies in the fixture or the kickoff
  engine; none missed when this spec was written.
  Observed by AC1.
- **S2** — Round 1 M2, finding id 5, the skeptic's class-level fix. An arm per resolver that
  `TOOL-dPlacedRequest-43` S20 changed: in `tools/run-gates/run-selftests.test.sh` a registry row whose
  user token is a strict substring of the user, its tag `s`, above the exact row `t`, asserting pooled
  evidence keyed on `t`; in `skills/session-kickoff/manifest-check.test.sh` a `--card` run with
  `USERNAME` set to the registry row's user in upper case, asserting the row's tag and not `UNKNOWN`.
  Each row's text names `TOOL-dPlacedRequest-99 S2`. The kickoff suite's floor rises by its row.
  Observed by AC2.
- **S3** — Round 2 M1, finding id 2, the skeptic's class-level fix. `read_fence_line` in
  `tools/push-main.sh` returns 1 only for an explicit `lease refused — <cause>` line other than
  `offline`, 3 for `offline`, and a new 4 for every non-answer: an unparsed, multi-line or empty read,
  every exit-2 `lease not written` line, the no-python branch, and a `check_fence_beat` failure on a
  fence line the driver did answer. `derive_push_failure` reads 1 as `fenced` and every other return
  but a fence as `unreachable`. Two arms in `tools/push-main.test.sh` assert `claim-lost` is never
  printed for an exit-2 `lease not written — x` answer and for a bad-beat fence line on the `--after`
  call. Their rows raise that suite's floor under `TOOL-dPlacedRequest-98`'s rule, and the
  `push-main self-test` budget row rises by their landings, by §4. Observed by AC3.
- **S4** — Round 2 M2, finding id 3, the skeptic's class-level fix. `read_card_stored` in
  `skills/session-kickoff/manifest-check.sh` picks the stored tail by freshness over the stores
  `card.store` selects, by the rule of §4, and four plants in
  `skills/session-kickoff/card-store.fixture.sh` observe it: a publish offline after an earlier
  lookup, then a follow; the same with the remote answering again at the follow; a foreign publish
  after this node cached a published sha, then a follow; and a foreign publish after an offline local
  write, then a follow. The last two also assert `resolve_build_card` answers the follow's card.
  Observed by AC4.
- **S5** — Round 2 M3, finding id 1, fix judged SOUND. The `loop placement fixtures` row of
  `tools/run-gates/selftest-budgets.txt` is re-priced from a reading over its 29 plants, its note naming
  the count and the base, and the leg's ceiling in `tools/gate-legs.json` is compared with that reading
  by §4's procedure. The left-shift the record names lands in `tools/run-gates/run-selftests.sh --check`:
  every budget row whose held leg runs a loop-kit module defining a module-level `PLANTS` carries a
  `plants=<n>` token equal to the number of plants that module holds once imported, the count the
  leg's self-test iterates. Every such row is given its token in this unit, and a row whose reading
  covered fewer plants is re-priced first. The checklist record
  `memory/gotchas/budget-row-not-remeasured-after-added-arms.md` names the check, and its fix paragraph
  is corrected to the ceiling procedure §4 states. Arms in `tools/run-gates/run-selftests.test.sh` red
  a mismatched token and a module that grows `PLANTS` after declaring it. Observed by AC5.
- **S6** — Round 2 L1, finding id 4, fix judged SOUND. `CARD_STORED_FROM` gains its reader: each
  `card —` success line `write_build_card` prints in `stored` mode carries ` · tail from
  <ref|cache|record>`. The class, a global assigned in a kit script and read nowhere, has no gate in
  this write set, so it lands as the checklist record `memory/gotchas/global-set-and-never-read.md`,
  claimed in the kickoff engine's codebase-map dossier. Observed by AC6.
- **S7** — Round 2 L2, finding id 6, fix judged SOUND. `FLOOR_ASSERTIONS` in
  `tools/hooks/scratch-guard.test.sh` rises by the one `TOOL-dPlacedRequest-34` AC28 row that runs on
  every host, and a comment line names both AC28 rows, the Windows-only one left out of the count by
  its skip elsewhere. S7 adds no row and moves no row's cost, so the `scratch-guard self-test` budget
  row is not re-priced for it. The class lands as a section of
  `memory/gotchas/floor-left-below-the-arms-it-guards.md`. Observed by AC7.
- **S8** — Round 2 L3, finding id 8, fix judged SOUND. The `--entry-claim` usage line of
  `tools/unattended/unattended.sh` lists `0 claimed, 1 refused, 2 not written, 3 spent, 4 waiting, 5
  a fresh slug owed`, the words of `run_entry_claim`'s header. The class lands as the checklist record
  `memory/gotchas/usage-exit-list-lags-its-function.md`, claimed in the unattended kit's codebase-map
  dossier, and the instance gains an arm in the unattended kit's suite: the usage line names every code
  `run_entry_claim`'s body returns, and every non-literal return in that body carries a comment pinning
  the codes it can pass through. Observed by AC8.

## 3. Non-goals (OUT)

- No change to what any card-store plant asserts beyond the four S4 adds; a plant fixed under S1 is
  fixed to hold its own stated observation.
- No shared selection function between `read_card_stored` and `resolve_build_card`: the class rule the
  record states admits a fixture asserting the two agree instead. S4's two foreign-publish plants are
  that fixture for every case where the ref is the newer card, a cached sha that differs from the ref
  and a foreign publish after an offline local write, where both readers answer the ref. Where the
  cache holds `local` and is the newer, the follow reads the cache while the lookup still reads the
  ref, because the lookup's trust rule is the loop kit's `claims.py verdict`, which this unit does not
  change; the S4 offline plants assert the follow alone.
- No re-pricing of a budget row that S1, S3 or S5 does not name.
- No new gate for the classes of S6, S7 and S8: each would live in another write set, the shell-hygiene
  checker, the testsuite counts leg and the unattended kit gate, and each lands as a checklist entry.
- No change to the lander's arms 42 to 54 beyond the two S3 adds, and no change to the fixture under
  them, which `TOOL-dPlacedRequest-98` owns.

### Edges

- **consumes-from** external — the card store, the node resolvers, the fenced landing, the placement
  suite and the entry claim this build's units built and CLOSED; each scope item corrects landed code,
  and those specs stay frozen
- **hands-off** `TOOL-dPlacedRequest-100` — S5's `plants=<n>` token on the `loop claim fixtures` row,
  which that unit raises by its `stale-holder` plant, and S8's arm over `run_entry_claim`'s returns,
  which that unit's new branch must satisfy with literal codes

## 4. Design

### S1 — the plant loop

```
if [ -f "$cs_fx" ]; then                # the existing skip, which ships to no adopter
  cs_list=$(bash "$cs_fx" --list) || FAIL "card-store.fixture.sh --list exited non-zero"
  for cs_plant in $cs_list; do ...as at the base, one ok or FAIL row per plant...; done
  check_eq "the suite ran every plant --list names" "$(printf '%s' "$cs_list" | grep -c .)" "$cs_ran"
fi
```

The count is `grep -c .` over the capture, never `wc -l` over a here-string, which counts an empty
capture as one; a `--list` that exits non-zero is a named failure, never an empty list.

Cited at the base: the hand list is `skills/session-kickoff/manifest-check.test.sh@f227fdc7:2383`, its
floor `skills/session-kickoff/manifest-check.test.sh@f227fdc7:2457`; the fixture's `--list` prints its
`PLANTS` at `skills/session-kickoff/card-store.fixture.sh@9d4246db:37`.

The plant inventory, measured by this spec's writer, one plant at a time by direct CLI with a
forward-slash `TMPDIR` on node d, 2026-11-20 (PINNED):

- `--list` prints 30 plants (DERIVED by `--list` piped to `wc -l`), and the suite runs 8 of them.
- Every one of the 30 held, each exiting 0 with no `MISSED` line, so gating them reds nothing today.
- The 30 runs took 781 seconds in all (PINNED, node d, 2026-11-20, one reading each).
- The 8 the suite already runs took 207 seconds of them (PINNED, the same readings).
- So the 22 added plants cost 574 seconds (DERIVED, the difference), read partly under a concurrent probe.

A `TMPDIR` spelled with backslashes reds every plant, an awk escape warning on each read. The suite
builds its `TMP` from the ambient `TMPDIR` (`skills/session-kickoff/manifest-check.test.sh@f227fdc7:7`),
MSYS `mktemp` keeps an inherited backslashed spelling, and the bar derives `TMPDIR` from the ambient
one, so the immunity holds only where the ambient `TMPDIR` is forward-slashed, as it is on node d. S1
therefore normalises `TMP` right after the suite makes it, by `cygpath -m` where `cygpath` exists, so
the plants never read a backslashed path.

The budget row (`tools/run-gates/selftest-budgets.txt@25b27c00:98`, 3820 from a worst whole-suite
reading of 2547 s, PINNED by that row) prices the whole suite, so it is re-priced for the whole suite,
never for the plants alone, and never by a suite run inside the pass
(`doc.build-method#m6-passes-commits-parallelism`). The reading is taken after S4's plants are in, over
every name `--list` prints then, 34 by this spec's count: the row's 2547 s (PINNED, that row), plus
the 22 added plants' 574 s (DERIVED above), plus S4's four plants read once each by direct CLI at build
time, x1.5. The row's note says it is a PINNED proxy, names the plant count and the base, and says it
is re-priced from the main loop's first reading of the leg alone, as its peers' notes do. The leg's
`ceiling` in `tools/gate-legs.json` is 4370 s (PINNED, at the base); it is compared with the reading,
about 3121 s (DERIVED, the row's reading plus the plants') plus S4's four, never with the budget, and moves only by S5's procedure where the reading leaves it too little
headroom.

### S2 — the resolver arms

`tools/run-gates/run-selftests.sh#resolve_node_tag` compares the lower-cased user with each registry
token for equality, and `skills/session-kickoff/manifest-check.sh#derive_node_tag` folds both sides
with `tolower`. The `run-selftests.test.sh` fixture writes one row whose token is exactly the user
(`tools/run-gates/run-selftests.test.sh@382f88e6:395`), which the substring rule matches too; the new
row is the user's first character at tag `s`, written above it. Each new row's text names
`TOOL-dPlacedRequest-99 S2`, so a criterion can find it. That suite pins no
`FLOOR_ASSERTIONS`, so its arm moves no floor; the record's "raise each suite's floor" holds for the
kickoff suite only.

### S3 — the re-fence outcome

```
read_fence_line -> 0 a fence, or none · 1 an explicit refusal by the lease · 3 offline · 4 no answer
derive_push_failure, the lease tip moved:
  0 with FENCE_REF  -> refenced          1 -> fenced, the claim-lost remedy
  anything else     -> unreachable, retry, no abort remedy
```

The two callers that read the first fence, at `tools/push-main.sh@7a142cb6:1733` and
`tools/push-main.sh@7a142cb6:1928`, test `if ! read_fence_line`, so 4 refuses the landing there as 1
does today. The function's header comment lists the four returns.

The two arms run inside the lander suite's fenced-landing block, so their rows count toward
`TOOL-dPlacedRequest-98`'s floor, the full-install count compared only where no dependency skip fired,
and they raise that pin by two. The `push-main self-test` budget row, re-priced by
`TOOL-dPlacedRequest-98` in its proxy shape, rises the same way by the arms' fixture makings and
landings, at the row's 14.7 s and 65.0 s, counted by `grep` over the two arms at build time. Cited at the base:
`tools/push-main.sh#derive_push_failure`, its `fenced` fall-through at `tools/push-main.sh@7a142cb6:334`;
`tools/push-main.sh#read_fence_line`; `tools/push-main.sh#check_fence_beat`; the driver's exit-2 lines in
`tools/unattended/unattended.sh#write_fence_beat`.

### S4 — the freshness rule

```
stores = read_card_policy card.store
cache  = local-clone selected and the cache file exists;  cref = its `# card-ref` line
refc   = remote-ref selected and refs/gov/remote/builds/<slug>/card resolves -> its commit
at(x)  = the `published <at>` field of card x's `card —` header line, as an instant
1. cache and cref = local and (no refc or at(cache) later than at(ref))  -> the cache   CARD_STORED_FROM=cache
2. refc                                                                    -> the ref     CARD_STORED_FROM=ref
3. cache                                                                   -> the cache   CARD_STORED_FROM=cache
4. build-folder selected and a card record                                 -> the record  CARD_STORED_FROM=record
5. none                                                                    -> return 1
```

`write_card_cache` stores `local` or the commit this node's own publish produced, so a sha `cref` that
differs from `refc` means the ref moved later to another writer's publish: the ref is the newer, and
rule 2 takes it, as `resolve_build_card` does. A `local` cache is not assumed newer either: a foreign
publish made after an offline local write wins by its stamp. The stamps are compared as instants,
each converted to epoch seconds, because `render_build_card` writes local time with its offset; a
stamp that does not parse loses to one that does, and two that do not parse fall to rule 2. Rule 1
holds whether or not this follow's `read_card_ref` answered, which is the case the record's instance
fix left standing. Cited at the base: `skills/session-kickoff/manifest-check.sh#read_card_stored`,
its fixed ref-first order at `skills/session-kickoff/manifest-check.sh@b25206f8:1921`;
`skills/session-kickoff/manifest-check.sh#write_card_cache` writes `local` or the ref's commit;
`skills/session-kickoff/manifest-check.sh#resolve_build_card` filters by `card.store` and trusts the cache
only when its card-ref is the fetched tip.

The four plants, `follow-offline-publish`, `follow-offline-publish-online`, `follow-foreign-after-cached`
and `follow-foreign-after-offline`, join the gate through S1's `--list` read with no further edit to the
suite. The last two each plant the foreign publish as a second writer's commit on the ref, newer than
the cache, then follow; each asserts the follow's card carries the foreign tail, and that
`resolve_build_card`, run after it, prints the same card.

### S5 — the plant-count token

Each loop-kit budget row's note gains one token, `plants=<n>`, beside its prose: the number of plants
its reading covered. `check_plant_tokens` in `run-selftests.sh --check` reads the `ok` lines of the
population `read_population` already computed as `$POP`, so it grades the argv a row resolves to, its
own or its held leg's, with `{prefix}` resolved, and never a second join of rows to legs. For an argv
naming `<tool root>/loop/<module>.py`, the count is the runtime size of the module's `PLANTS`: the
module is imported by path under `python -I` and `len(PLANTS)` read, which is the collection its
self-test iterates. A static count of the dict literal is refused, because
`tools/loop/budget.py@48d39278:268` grows `PLANTS` by `PLANTS.update(REQUEST_PLANTS)`, so its leg runs
41 plants while its literal holds 34. A module that fails to import is a finding naming it, never a
skip. A missing token or one that differs is a finding naming the row, the token and the count. A row
whose argv runs no such module is not graded, and the check's clean line says how many rows it graded.
The inventory at the base, read by an `ast` probe joining each row to its leg (DERIVED, re-derived by the
check's own runtime count, under which `loop budget fixtures` reads 41 and is among the rows to
re-price):

| rows graded | rows whose prose count already equals `PLANTS` | rows to re-price |
|---|---|---|
| 22 | 9 | at most 13, placement's among them |

A row whose note names the commit its reading was taken at takes its token from the runtime count of
`PLANTS` at that commit, read from that commit's `tools/loop` copied to a scratch directory by `git
archive`, and is re-priced only where that count differs from today's. Each row to re-price is read the
way its peers were, its plants one at a time by direct CLI, worst reading x1.5 floored at 60, its note
naming the reading's base and node.

The ceiling procedure, for S1's row and S5's alike, is the one TOOL-aClearedLedger-10 decided, and
`derive-ceilings.py --write` alone moves no ceiling: it distils run records into
`tools/run-gates/ceiling-evidence.txt`, and `--check` compares that file with `tools/gate-legs.json`.
Where a leg's reading, never its budget, approaches the leg's `ceiling`, the `ceiling` in
`tools/gate-legs.json` is edited and the reading recorded by `GOV_NODE=<tag> derive-ceilings.py --write
--observed '<leg>=<s>' --how '<direct CLI, base, node>'`, so `--check` holds it; then
`python tools/run-gates/pass_legs.py --apply` runs, and the `last-audit` line of
`memory/guides/SESSION-KICKOFF.md` is re-stamped, since that manifest watches `tools/gate-legs.json`.
No ceiling-at-least-budget relation is asserted: the budgets file keeps the two figures apart by
design. The checklist record's fix paragraph, which names `--write` alone
(`memory/gotchas/budget-row-not-remeasured-after-added-arms.md@252f41bb:31`), is corrected to this
procedure, so the next spec does not copy the wrong one. Cited at the base:
`tools/run-gates/selftest-budgets.txt@25b27c00:84`; `tools/loop/placement.py@a7f26e84`'s `PLANTS`,
29 keys (DERIVED by `ast`, and equal at runtime, since that module never grows it);
`tools/run-gates/run-selftests.sh#read_population`; `tools/run-gates/derive-ceilings.py@7d58ebdb:36`.

### S6 to S8

- **S6.** The suffix rides each success line, `remote-ref`, `local-clone` and the snapshot's, only in
  `stored` mode, where a tail was read; `session` and `none` modes read no store. Cited at the base:
  `skills/session-kickoff/manifest-check.sh@b25206f8:1815` declares it, and
  `skills/session-kickoff/manifest-check.sh#write_build_card` prints the lines.
- **S7.** The value is one above whatever the file holds when this unit builds, since
  `TOOL-dPlacedRequest-95` raises the same pin for its own rows. On a MINGW, MSYS or CYGWIN host both
  AC28 rows run (`tools/hooks/scratch-guard.test.sh@ff709691:1764` and the Windows-only row after it),
  so deleting the every-host row alone leaves one row of slack and stays green there. The staged break
  is therefore the every-host row deleted with `sg_win` forced empty, which reds the raised floor on
  any host, node d included. Cited at the base: `tools/hooks/scratch-guard.test.sh@ff709691:1842`.
- **S8.** The arm collects the `return <n>` codes inside `run_entry_claim`'s body by `awk` and asserts
  each appears in the usage line's exit list. It also fails on any `return "$<var>"` in the body whose
  line carries no comment pinning the codes the variable can hold; the four pass-throughs of
  `claim.py`'s exit at the base (`tools/unattended/unattended.sh@0e8038fd:4866`, 4880, 4942 and 4946)
  gain that comment, the codes read from the verb `claim.py` runs there. The usage line uses the
  header's own words, `3 spent`, and the arm compares the words of each listed code with the header's,
  not only the codes. The class rule across every mode belongs to the unattended
  kit gate, another write set, so it is the checklist record's. The unattended kit's own suites are
  waived for this build's landing (README rule 8), so the arm's clean reading is owed with
  PLAY-dClosedLoop-14 and AC8 observes by `grep`. Cited at the base:
  `tools/unattended/unattended.sh@0e8038fd:55`, the record's line 56 being one off;
  `tools/unattended/unattended.sh#run_entry_claim`.

### Inventory

| identifier | kind | cell that grades it |
|---|---|---|
| `check_plant_tokens` | the S5 check, a function of the self-test runner | `sh.function`, graded OK by `lexicon.py --suggest` |
| `plants=<n>` | S5's token in a budget row's note | none; the check reads it |
| `follow-offline-publish`, `follow-offline-publish-online`, `follow-foreign-after-cached`, `follow-foreign-after-offline` | S4's plant names in the fixture's `PLANTS` | none; plant names are data |
| `tail from` | S6's line suffix | none |
| 4 | S3's return of `read_fence_line` | none |

### Rollout

This unit shares files with its order-37 siblings: `tools/hooks/scratch-guard.test.sh` with
`TOOL-dPlacedRequest-95`, `tools/push-main.test.sh` with `TOOL-dPlacedRequest-98`,
`tools/unattended/unattended.sh` with `TOOL-dPlacedRequest-96` and `TOOL-dPlacedRequest-97`, and
`memory/gotchas/INDEX.md` with `TOOL-dPlacedRequest-95`. The dispatch sequences them by their recorded
write sets. Each floor rises over the value the file holds when the unit builds, and S3's two arms raise
the lander suite's floor whenever `TOOL-dPlacedRequest-98` has pinned one.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.test.sh`: S1's loop, liveness row, `TMP` normalisation and
  floor; S2's arm
- `skills/session-kickoff/card-store.fixture.sh`: S4's four plants, and S1's fixes to a plant that misses
- `skills/session-kickoff/manifest-check.sh`: S4's rule, S6's suffix, and S1's fixes in the engine
- `tools/run-gates/run-selftests.test.sh`: S2's arm, S5's arms
- `tools/run-gates/run-selftests.sh`: S5's check
- `tools/run-gates/selftest-budgets.txt`: S1's, S3's and S5's rows
- `tools/gate-legs.json`: a ceiling, only where a reading approaches it
- `tools/run-gates/ceiling-evidence.txt`: the `--observed` reading behind a moved ceiling, only then
- `memory/guides/SESSION-KICKOFF.md`: the `last-audit` re-stamp, only where `tools/gate-legs.json` or
  another watched path, `tools/run-gates/run-selftests.sh` or `skills/session-kickoff/manifest-check.sh`,
  changes
- `tools/push-main.sh`: S3's returns and classifier
- `tools/push-main.test.sh`: S3's arms
- `tools/hooks/scratch-guard.test.sh`: S7's floor and comment
- `tools/unattended/unattended.sh`: S8's usage line
- `tools/unattended/unattended.test.sh`: S8's arm
- `memory/gotchas/budget-row-not-remeasured-after-added-arms.md`: S5's check named, and its fix
  paragraph corrected to the ceiling procedure
- `memory/gotchas/global-set-and-never-read.md`: S6's class, new
- `memory/gotchas/floor-left-below-the-arms-it-guards.md`: S7's section
- `memory/gotchas/usage-exit-list-lags-its-function.md`: S8's class, new
- `memory/gotchas/INDEX.md`: rendered by `gotchas.py --write`
- `memory/map/features/session-kickoff.md`: claims `global-set-and-never-read.md` under its
  `gotcha-classes`
- `memory/map/features/unattended.md`: claims `usage-exit-list-lags-its-function.md` under its
  `gotcha-classes`
- `memory/map/generated/MAP.md`, `memory/map/generated/inventories.json`,
  `memory/map/generated/symbols.json` and `memory/map/generated/CARDS.md`: regenerated by the codebase
  map's generator, `gen_map.py --write`, the two new records and `check_plant_tokens` entering them
- each touched kit's version carrier, moved once by the kit-epoch rule

### Alternatives rejected

- **S3 by the finder's instance fix**, a separate code for the unparsed, `lease not written` and
  no-python reads only. It leaves a `check_fence_beat` failure classed `fenced`, which the skeptic named.
- **S4 by the finder's instance fix**, the cache preferred only when this follow's ref read did not
  answer. It leaves the stale ref winning whenever the remote answers again at the follow.
- **S4's rev-1 rule 1, the cache whenever `cref` is `local` or differs from the ref.** It serves an
  older cache over a newer foreign publish, the stale card S4 exists to close, moved to a new path.
- **S5 by a static count, refusing a module that grows `PLANTS`.** It leaves `loop budget fixtures`
  ungradeable; the runtime count grades it at the size its self-test runs.
- **S6 by removal.** The record offers it; with S4's rule the store a tail came from is the one fact a
  reader of a re-rendered card needs, so the variable gains its reader instead.

## 5. Production-readiness checklist

- security — none of the eight widens a surface; S3 narrows when a holder is told to abort.
- perf / scale — S1 adds 22 plants to the kickoff leg, about ten minutes by §4's readings, and S4 four
  more, so its budget row is re-priced; S5's check is one import per loop-kit module a row runs.
- error / empty / loading states — S3's non-answer is `unreachable`, a retry; S4 with no store holding a
  card still returns 1.
- observability — S6 prints the store a follow's tail came from.
- risks — a plant gated by S1 that misses for a cause outside this write set holds the unit open; it is
  parked with its cause, never waived. S5's re-pricing costs about half an hour of direct-CLI plant runs.
- testing — the probes of §6 and the arms in §7.
- migration — none; no data moves.
- user docs — none: no page under `help/` names the card store's lines, the lander's re-fence outcome or
  the budget rows; `help/loop.md` names `--entry-claim` without its exit codes.

## 6. Acceptance criteria

- **AC1** — When `bash skills/session-kickoff/card-store.fixture.sh --plant <name>` runs once for each
  name `--list` prints, every run exits 0 with no `MISSED` line; and with `K` naming the kickoff
  suite's file, `grep -c 'for cs_plant in publish publish-off' "$K"` prints 0,
  `grep -c 'cs_fx" --list' "$K"` prints at least 1, `grep -c 'the suite ran every plant --list names' "$K"`
  prints 1 and `grep '^FLOOR_ASSERTIONS=' "$K"` prints a value above 379; and the `manifest-check self-test`
  row of `tools/run-gates/selftest-budgets.txt` no longer reads 3820 and its note names the plant count
  that `bash skills/session-kickoff/card-store.fixture.sh --list | grep -c .` prints.
  Red when: the loop names a hand list, or the liveness row, the floor rise or the re-price is missing;
  at 95c3103ad the loop names 8 of the 30 plants `--list` prints, the second and third greps print 0,
  the floor reads 379 and the row reads 3820, its RED-first reading.
  cost: about fourteen minutes on node d for the thirty-four runs, by §4's readings.
- **AC2** — When `grep -c 'TOOL-dPlacedRequest-99 S2' tools/run-gates/run-selftests.test.sh` and
  `grep -c 'TOOL-dPlacedRequest-99 S2' skills/session-kickoff/manifest-check.test.sh` run, each prints at
  least 1, the first file's row writing tag `s` above tag `t` and the second's setting `USERNAME`
  upper-cased on a `--card` run, while the kickoff suite's `^FLOOR_ASSERTIONS=` line holds a value above
  379;
  and, under `env -u GOV_NODE` as both suites run, a probe evaluating `resolve_node_tag`, cut by `awk`
  from the run-gates kit's self-test runner, over a scratch root whose `AGENTS.md` registry holds the
  user's first character at tag `s` above the user at tag `t`, prints `t`, and a probe evaluating
  `derive_node_tag`, cut from `skills/session-kickoff/manifest-check.sh`, over a scratch registry naming
  the user, with `USERNAME` upper-cased, prints that row's tag and not `UNKNOWN`.
  Red when: an arm is missing, or a resolver matches by substring or case-sensitively; at 95c3103ad
  both greps print 0 and the floor reads 379, its RED-first reading. The build also runs the two probes
  against scratch copies staged with the pre-S20 `case` line and the case-sensitive compare, where they
  print `s` and `UNKNOWN`, the reading each new arm must red on.
- **AC3** — When a probe evaluates `read_fence_line` and `check_fence_beat`, cut from `tools/push-main.sh`
  by `awk`, against a stub driver answering `--lease fence build fx --after <tip>`, it returns 4 for an
  exit-2 `lease not written — x` line, 4 for a fence line whose beat is not parented on the tip, and 1
  for a `lease refused — live-holder` line; and when a probe evaluates `derive_push_failure`, cut by
  `awk` from `tools/push-main.sh` with the functions it calls, against a stub driver whose `--after`
  answer is the exit-2 `lease not written — x` line, and again against a bad-beat fence line, it prints
  `unreachable` each time and no `claim-lost` on stderr.
  Red when: a non-answer returns 1, or the classifier reads a non-answer as `fenced`; at 95c3103ad both
  non-answers return 1, and the classifier probe prints `fenced` with the `claim-lost` remedy, its
  RED-first reading.
- **AC4** — When `bash skills/session-kickoff/card-store.fixture.sh --plant follow-offline-publish` and
  `--plant follow-offline-publish-online` run, each exits 0 and its follow's card carries the offline
  publish's tail; and when `--plant follow-foreign-after-cached` and `--plant follow-foreign-after-offline`
  run, each exits 0, its follow's card carries the foreign publish's tail, and `resolve_build_card`
  prints that same card.
  Red when: the stored tail is read ref-first, or a cache is served over a newer foreign publish;
  staged by the fixture beside a copy of the engine at 95c3103ad, each offline plant prints `MISSED`
  with the older tail, and beside rev-1's rule 1 each foreign plant prints `MISSED` with the cache's
  tail, its RED-first reading.
- **AC5** — When a probe evaluates `check_plant_tokens`, cut by `awk` from the run-gates kit's self-test
  runner, over
  the tip's `tools/run-gates/selftest-budgets.txt` it reports no finding; over a scratch copy whose
  placement row reads `plants=15` it reports that row with 29; and over a scratch loop module declaring
  two plants and adding one more by `PLANTS.update`, under a row reading `plants=2`, it reports that row
  with 3; and `grep -c 'observed' memory/gotchas/budget-row-not-remeasured-after-added-arms.md` prints
  at least 1.
  Red when: a row's count differs from the plants its module's self-test runs; at 95c3103ad the
  placement row prices fifteen plants against 29, no check reads it, and the record names `--write`
  alone, its RED-first reading.
  figure: 29 and 3 are DERIVED by the runtime count at the probe; 15 and 2 are the staged breaks.
- **AC6** — When AC4's `follow-offline-publish` plant runs, its follow's `card —` line carries
  `tail from cache`; and `python tools/memory-tree/gotchas.py --for-paths skills/session-kickoff/manifest-check.sh`
  prints `global-set-and-never-read`; and `grep -c 'global-set-and-never-read.md' memory/map/features/session-kickoff.md`
  prints 1.
  Red when: `CARD_STORED_FROM` is assigned and read nowhere; at 95c3103ad
  `grep -rn CARD_STORED_FROM skills tools` prints only lines that assign it or name it in a comment,
  its RED-first reading.
- **AC7** — When `grep -n '^FLOOR_ASSERTIONS=' tools/hooks/scratch-guard.test.sh` runs, it prints a value
  one above the pin the file held before this unit, and `grep -c '^# [0-9]* = [0-9]* + .*AC28'
  tools/hooks/scratch-guard.test.sh` prints 1.
  Red when: the floor leaves AC28's rows out; at 95c3103ad the pin reads 396 and the second grep prints 0,
  its RED-first reading.
- **AC8** — When `grep -c '0 claimed, 1 refused, 2 not written, 3 spent, 4 waiting, 5 a fresh slug owed'
  tools/unattended/unattended.sh` runs, it prints 2, the usage line and `run_entry_claim`'s header;
  and `python tools/memory-tree/gotchas.py --for-paths tools/unattended/unattended.sh` prints
  `usage-exit-list-lags-its-function`; and `grep -c 'usage-exit-list-lags-its-function.md'
  memory/map/features/unattended.md` prints 1.
  Red when: the usage line omits a return or spells one in other words; at 95c3103ad the same grep
  prints 1, the header alone, its RED-first reading.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `manifest-check self-test` · `run-selftests self-test` · `every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `policy fixtures` · `codebase-map coverage + freshness` · `push-main self-test` · `scratch-guard self-test` · `agent-cap self-test` · `hook destinations self-test` · `verifier fan-out self-test` · `review-join self-test` · `unattended kit gate` · `tier2-review self-test` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `testsuite counts (every bar self-test prints one)` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC2 AC4 AC6 · the hand list of 8 restored, the case-sensitive node compare restored, and the engine of 95c3103ad under the four S4 plants · FLOOR_ASSERTIONS raised by the rows added
New arm: tools/run-gates/run-selftests.test.sh · covers AC2 AC5 · the substring case restored, a budget copy whose placement token reads 15, and a scratch module growing PLANTS by update under a token of 2 · none, the suite pins no floor
New arm: tools/hooks/scratch-guard.test.sh · covers AC7 · the every-host AC28 row deleted with sg_win forced empty, which reds the raised floor on any host, node d's MINGW64 included, where the Windows-only row would otherwise absorb the deletion · FLOOR_ASSERTIONS raised by one
New arm: tools/unattended/unattended.test.sh · covers AC8 · the usage line of 95c3103ad, which omits the returns 2 and 3, and a return of a variable with no pinning comment · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14
New arm: tools/push-main.test.sh · covers AC3 · the exit-2 answer and the bad-beat fence line on the after call, staged against the classifier of 95c3103ad that reads both as fenced · the floor TOOL-dPlacedRequest-98 pins, raised by the two rows

## 8. Open questions

- **F1 — What does S5's check compare a row against?** (a) A `plants=<n>` token every loop-kit row
  whose leg runs a module with `PLANTS` must carry, equal to that dict's size, each row re-priced where
  its reading covered fewer. (b) The same token, compared only where a row carries it, placement's row
  the first. (c) The prose count, read as an English number word. (c) reads a word list of mixed nouns,
  plants, cases and sums, and a false match is silent. (b) leaves the 12 other mismatched rows
  unchecked, the follow-up the record's "each loop row" asks to close. (a) is the record's fix as stated
  and trips no veto of `doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`; its cost is the re-pricing, stated under §5. RESOLVED (agent,
  2026-11-20, delegated): (a), the feature-rich survivor. widens: none · relaxes: none
- **F2 — `CARD_STORED_FROM`: print it or remove it?** (a) Print it on the stored-mode success lines;
  (b) remove the variable, its assignments and its mention. Both are judged SOUND by the skeptic. (a)
  satisfies the record and gives S4's plants a line to read; (b) is smaller. RESOLVED (agent,
  2026-11-20, delegated): (a), the feature-rich option, no veto tripped. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft, the minors batch of the closing diff review: round 1 M1 and M2
  (finding ids 4 and 5), round 2 M1, M2, M3, L1, L2 and L3 (finding ids 2, 3, 1, 4, 6 and 8), promoted by
  round 2's exit as one unit.
- rev-2 · 2026-11-20 · S1 · S2 · S3 · S4 · S5 · S6 · S7 · S8 · §3 · §4 · §5 · AC1 · AC2 · AC3 · AC4 ·
  AC5 · AC6 · AC8 · §7 · folded 2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit: finding id 1
  (H1), AC2 observes the two arms and the floor; ids 11 and 32 (H2), S4's rule 1 restricted to a
  `local` cache newer by its stamp, with two foreign-publish plants asserting agreement with
  `resolve_build_card`; ids 22 and 30 (H3), S3's floor raise follows `TOOL-dPlacedRequest-98`'s rule;
  id 31 (H5), S5 counts `PLANTS` at runtime and an arm reds a module that grows it; ids 2 and 16 (M1),
  AC2's probes run under `env -u GOV_NODE`; id 3 (M2), AC3 observes `derive_push_failure`; id 4 (M3),
  S1's reading covers S4's plants; id 5 (M4), S7's staged break reds on node d; id 8 (M7), AC1 decides
  S1; id 14 (M9), S1's row priced for the whole suite; ids 13 and 19 (M10), the ceiling procedure
  corrected in S5, in Files touched, on the §7 line and in the checklist record; id 23 (M12),
  `policy fixtures` on the §7 line; id 24 (M13), the two new records' dossiers and the map
  regeneration in Files touched; id 25 (M14), S3's `push-main self-test` row rise, and S7 saying why
  its row stands; id 26 (M15), the §3 bullet narrowed and S1 given the ceiling step; id 9 (L1), S8
  spells `3 spent`; id 15 (L3), S8's arm pins pass-through returns; ids 17 and 33 (L4), S1 normalises
  `TMP` and restates the immunity; id 20 (L5), S5 reads `read_population`; id 21 (L6), S1's liveness
  count and guard. §3 · the hands-off edge to `TOOL-dPlacedRequest-100`, the repair unit the same
  record promoted, whose plant and branch meet S5's token and S8's arm.
- rev-2 · 2026-11-20 · §1 · S1 · §8 · editorial, by
  2026-11-20-prompt-TOOL-dPlacedRequest-95-audit-fold-text-brief: each folded duration carries its mark
  on its own line, and each build-method section is cited by its alias tag.

## 10. Reuse audit

Every item extends a seam already in the tree: the fixture's own `--list` verb for S1, each suite's
existing registry fixture for S2, `tools/push-main.sh#read_fence_line`'s return codes for S3,
`skills/session-kickoff/manifest-check.sh#read_card_stored` for S4 with the fixture's plant table,
`tools/run-gates/run-selftests.sh --check`'s declaration walk for S5, and the gotchas catalogue's record
shape for S6 to S8. `python tools/codebase-map/reuse_lookup.py "the build card's stored tail chosen by
freshness over the selected stores"` and `python tools/codebase-map/reuse_lookup.py "a budget row's
plant count compared with the suite's plants"` ranked name stems only, `read`, `check` and
`resolve`, no seam beyond those named. The recall query below returned both round records and
`TOOL-dPlacedRequest-2`'s scout; where the records' line numbers disagree with the source, this spec
cites the source: the usage line is line 55, not 56, and the round-1 record's eight-plant count is the
source's, its finder's 33 is not.

Recall terms used: card-store.fixture.sh plants --list read_card_stored card.store read_fence_line derive_push_failure resolve_node_tag selftest-budgets FLOOR_ASSERTIONS entry-claim usage
