# TOOL-dWitnessedBar-63 — the round-1 audit of units 58 to 62, its 34 minors batched: readers that read the whole list and every path form, criteria graded on what the built tree derives, honest failure paths, and observed sequences

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 35 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 |
| [2026-10-25-build-TOOL-dWitnessedBar-63-round4-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-63-round4-fix-return.md) | research | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-63-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-63-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-63-round4-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-63-round4-fix-brief.md) | research | — |
| [2026-10-25-review-TOOL-dWitnessedBar-63-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-63-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 58 to 62
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-58-spec-audit-round1.md`)
exited CONVERGED with 34 confirmed findings, none a blocker or a high. BUILD-METHOD M4 batches every
MEDIUM and LOW into one unit, two only where they split into disjoint write sets by M6's clauses; these
do not (§4 "Why one unit"). Each finding is named by report id and is its own scope item, where the
report merged ids into one item too. The minors land on several units, so this unit repairs none in
particular and builds after every unit (order 35). The report's id 18 was refuted by the audit itself,
a duplicate of id 15, and is no finding here.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 9, 15, 26 | S1, S2, S3 |
| M2 | MEDIUM | 4, 21 | S4, S5 |
| M3 | MEDIUM | 5, 13, 31 | S6, S7, S8 |
| M4 | MEDIUM | 11, 17, 29 | S9, S10, S11 |
| M5 | MEDIUM | 12, 28 | S12, S13 |
| M6 | MEDIUM | 2 | S14 |
| M7 | MEDIUM | 3 | S15 |
| M8 | MEDIUM | 8 | S16 |
| M9 | MEDIUM | 20 | S17 |
| M10 | MEDIUM | 22 | S18 |
| M11 | MEDIUM | 27 | S19 |
| M12 | MEDIUM | 30 | S20 |
| M13 | MEDIUM | 33 | S21 |
| M14 | MEDIUM | 35 | S22 |
| L1 | LOW | 1 | S23 |
| L2 | LOW | 6 | S24 |
| L3 | LOW | 7, 25 | S25, S26 |
| L4 | LOW | 10 | S27 |
| L5 | LOW | 14 | S28 |
| L6 | LOW | 16 | S29 |
| L7 | LOW | 19 | S30 |
| L8 | LOW | 23 | S31 |
| L9 | LOW | 24 | S32 |
| L10 | LOW | 32 | S33 |
| L11 | LOW | 34 | S34 |

That is 22 MEDIUM and 12 LOW findings by raw id.

## 2. Scope (IN)

- **S1** — id 9. `TOOL-dWitnessedBar-60` S4's arm in `tools/run-gates/run-gates.gov.test.sh` reads
  `PM_SCRUB` as a range, from the line opening `PM_SCRUB="` to the line closing the quote
  (`sed -n '/^PM_SCRUB="/,/"$/p'`), strips the quotes and folds newlines to spaces. The three one-line
  lists, `BAR_SCRUBBED_KNOBS`, `BAR_CLEARED_KNOBS` and `_gknobs`, keep the one-line cut. Observed by AC1.
- **S2** — id 15. The reader is the fold `PM_SCRUB`'s only consumer applies,
  `${PM_SCRUB//$'\n'/ }` (`tools/run-gates/post-merge.sh:40-43`); the arm's comment names that line as
  its seam, and says the driver suite's one-line cut does not fit a multi-line assignment.
  Observed by AC1.
- **S3** — id 26. The arm prints the count of names it read from each of the four lists. On the built
  tree `PM_SCRUB` reads non-empty, holds `GIT_DIR` and `GATE_TURNSTILE_HOLDER`, names from its first and
  last physical lines at the base, and counts at least 30. Unit 60's AC2 staged cut of `GATE_SELECTION` then fails naming the
  knob and `PM_SCRUB`. Observed by AC1 and AC2.
- **S4** — id 4. `TOOL-dWitnessedBar-62`'s AC13 is graded on a figure the built tree re-derives: unit
  62's §4 probe total equals `refuse-wrong-shell.sh --coverage`'s population on the built tree. 77 is
  the figure measured at the base, and no criterion requires it of the built tree. Unit 62's AC13
  ledger line names this item. Observed by AC3.
- **S5** — id 21. Unit 62's AC17 reads: each of the five spelling fixtures is a member, and the built
  tree's `--coverage` count equals the probe's total. Unit 62's AC17 ledger line names this item.
  Observed by AC3.
- **S6** — id 5. `TOOL-dWitnessedBar-61`'s "any other failure" row takes `TOOL-dWitnessedBar-15` S2's
  refused-home branch: no home is written, the reason `no HEAD: <first stderr line>` goes to stderr, and
  stdout carries the population's `unarmed` line with that reason. No `# unarmed` line is written with an
  empty or a null SHA on this path. Observed by AC4.
- **S7** — id 13. Unit 61 S1's "every `# unarmed` line that run writes carries it" binds the runs whose
  SHA resolved: given, HEAD, or the null SHA on an unborn HEAD. The no-HEAD path writes no such line, so
  unit 61 S3's and `TOOL-dWitnessedBar-14` S7's unarmed readers never meet a line lacking its SHA.
  Observed by AC4.
- **S8** — id 31. The unborn predicate is `git rev-parse --verify --quiet HEAD` exiting 1 with empty
  stdout and empty stderr. Exit 128, or any stderr text, is the no-HEAD path of S6: a non-repository and a
  dubious-ownership refusal never stamp the null SHA. Observed by AC4.
- **S9** — id 11. lib-unattended's `exists:` containment (unit 62 S22) folds every `\` to `/`
  (`${p//\\//}`) before testing `read_gate_policy`'s pattern (`tools/unattended/unattended.sh:9566-9567`),
  so `..\x`, `a\..\..\x`, `\x` and `\\server\share` are skipped with unit 62 S21's line.
  Observed by AC5.
- **S10** — id 17. govkit selfcheck's `exists:` check grades the token-stripped path through
  `demand_contained_dest` (`tools/govkit/govkit.py:1304`), catching its `Refusal` into the selfcheck
  failure, so govkit keeps one containment rule and S22's pattern is not a second one beside it.
  Observed by AC5.
- **S11** — id 29. regen's `exists:` check, copy-installed and unable to import govkit, applies
  `demand_contained_dest`'s rule (`tools/govkit/govkit.py:1329-1331`): the path is refused when
  `posixpath.normpath` of it with `\` folded to `/` is `..`, starts `../` or is absolute, when
  `ntpath.isabs` holds, or when its second character is `:`. Unit 62's AC2 trees gain `..\x`, `\x` and
  `\\server\share`. Observed by AC5.
- **S12** — id 12. Unit 62 S35's seed-home containment reads a `ValueError` from `os.path.commonpath`,
  raised for paths on different drives or for one absolute and one relative, as outside the tree:
  unarmed `outside the tree <path>`, no traceback, and `seed --all` goes on to the next population.
  Observed by AC6.
- **S13** — id 28. Unit 62's AC18 gains a cross-drive case. The arm calls the containment test with a
  stand-in for `os.path.commonpath` that raises `ValueError`, on every host; on a Windows host it also
  runs `seed --home Z:/x` with the fixture on another drive letter. Observed by AC6.
- **S14** — id 2. Unit 61 builds before `TOOL-dWitnessedBar-47` inside order 5. The hand-out breaks an
  order tie by id string (`tools/workflows/unattended-build.js:608-613`) and lists 47 first; the
  `--dispatch` edge refusal (`tools/unattended/unattended.sh:13691-13764`) refuses 47 while 61 is neither
  CLOSED nor WONTDO, so 61 is dispatched first. At the close, unit 61's pass commit is an ancestor of
  unit 47's, each found by `build_commit`. That observation answers unit 61's Rollout sentence, which no
  tool reads. Observed by AC7.
- **S15** — id 3. `TOOL-dWitnessedBar-59`'s AC2 is answered for what unit 59 owns: the whole physical
  line holding the lone CR is removed as one line, and `witness` counts one assignment. Its half
  "every other byte of the file is unchanged" is `TOOL-dWitnessedBar-57`'s AC12, observed at the close
  after unit 57's pass, and unit 59's AC2 ledger line names it. Observed by AC8.
- **S16** — id 8. The policy parity arm of unit 62 S37 and unit 59 AC3 reads bash's stdout as bytes,
  `capture_output=True` with no `text=True`, and decodes it as UTF-8 itself, so a CR in bash's value
  reaches the compare. It departs from `check_conf_reader_parity`'s text-mode capture
  (`tools/govkit/selftest.py:827-828`) on that one point. Observed by AC9.
- **S17** — id 20. Unit 62 S24's reader rule reaches the runner: `read_record_keys`
  (`tools/run-gates/run-gates.sh:2387-2397`) reads each line whole with `IFS= read -r` and takes the
  value after the first TAB. The awk readers of run records in `tools/unattended/unattended.sh`
  (`:9619-9622`, `:10302-10304`, `:10421-10424`) and `tools/run-gates/post-merge.sh` (`:318`) stay out
  of scope: each reads `verdict`, `failed`, `tree_moved`, `wall_breach`, `head` or `tree_clean`, which
  the runner writes as one scalar after the key (`run-gates.sh:3483`, `:3487`, `:5370`, `:5556-5563`).
  Observed by AC16.
- **S18** — id 22. Unit 62's AC18 arm lives in `tools/lib/resolve-python.test.sh` section `2l`, run by
  the leg `python resolver (behaviour + inline parity + idiom ban)`, and not in a
  `legacy_ledger.py --fixture` mode that no leg runs. Unit 62's AC15 and AC20 plants are run by
  `ratchet selftest`, the leg `TOOL-dWitnessedBar-14` adds; §7 names it in prose. Observed by AC10.
- **S19** — id 27. In every reader unit 62 S24 binds and in S17's `read_record_keys`, a key line with no
  TAB reads as an absent key with an empty value. The awk form is
  `$1==k && index($0,"\t") {sub(/^[^\t]*\t/, ""); print}`; the Python form is `partition('\t')`, a line
  whose separator is empty being skipped. Observed by AC11 and AC16.
- **S20** — id 30. Unit 62 S39's `try`/`finally` is claimed for normal exits, exceptions, subprocess
  timeouts and `KeyboardInterrupt` only; a process kill can leave the file. The allowed-signers temp is
  made with the fixed prefix `peer-signers-` under the git dir, and each peer read first unlinks any
  such temp older than `PEER_SIGNERS_GRACE_S`, 86400 seconds (§8 F5). Observed by AC12.
- **S21** — id 33. Unit 59 S1's LF-only split is observed on both files it names. A fixture whose
  `.unattended.conf` holds `GATE_POLICY_FILE=pol-a<CR>GATE_POLICY_FILE=pol-b<LF>` resolves, in the step,
  the same path `read_policy_key` reads, and the step never reads `pol-b`; a conf naming a policy file
  whose `INHERITED_RED` holds a lone CR maps as unit 59's AC1 maps it. Observed by AC13.
- **S22** — id 35. lib-unattended's generated-row reader splits the four fields without loss: each
  record line is read whole with `IFS= read -r` and cut at each TAB by parameter expansion, so an empty
  generator stays empty (`tools/unattended/lib-unattended.sh:878-880`). Unit 62's S21 and S22 `when`
  refusals run on every row carrying a path, before the generator guard, so a generator-less row with a
  malformed `when` prints S21's line. Observed by AC14.
- **S23** — id 1. Units 58 and 60 share order 33 and both write
  `tools/run-gates/run-gates.evidence.test.sh`. They build one after the other, as the strictly
  sequential dispatch already does (`tools/workflows/unattended-build.js:76-80`), and their two floor
  raises chain: the later `RAISED` line starts from the value the earlier one set. Observed by AC15.
- **S24** — id 6. The runner-side read S17 changes is observed: `read_record_keys`, cut from the runner
  by `awk '/^read_record_keys\(\)/,/^}/'`, reads a value with an empty last field and a line with no
  TAB as S17 and S19 state. Observed by AC16.
- **S25** — id 7. Unit 62 S32's new wording is grepped for: `root confs in the working tree` names the
  memory-tree README's adopter-receives table and each conf-set docstring of `ratchet.py`.
  Observed by AC17.
- **S26** — id 25. Unit 62's AC22 negative grep is widened to every spelling units 14, 17, 46 and 52
  used: `grep -rniE 'tracked root confs?|tracked confs' tools/memory-tree/` prints nothing.
  Observed by AC17.
- **S27** — id 10. Unit 62's AC7 names each suite's own floor line: `run-gates evidence: executed`,
  `gov-canary: executed`, `adopt-e2e: executed`, and `FAIL executed` for the hygiene suite. Unit 62's AC7
  ledger line quotes the line each suite printed. Observed by AC18.
- **S28** — id 14. Unit 58 S1's capturing stub writes `${GATE_BASE_FROM-unset}` to a suite scratch file
  named by an environment variable, as `docstub` writes `"$DOCS_ENV"`
  (`.githooks/pre-push.test.sh:1821-1823`), and not under the fixture's git dir. Observed by AC19.
- **S29** — id 16. The comment above `_gknobs` (`tools/unattended/unattended.sh:11153-11158`) says the
  list carries every name in the hook's `BAR_SCRUBBED_KNOBS` and `BAR_CLEARED_KNOBS`, and names unit 60
  S4's arm in `tools/run-gates/run-gates.gov.test.sh` as its guard. Observed by AC20.
- **S30** — id 19. The canonical `# >>> selection_row` block and the `flakes` caller's `--selection` of
  unit 62 S17 and S18 sit in `verdict_flow.py`, a path this unit's write set carries; this pass writes
  whichever of the two unit 62's pass left out. Observed by AC21.
- **S31** — id 23. `tools/run-gates/README.md` names the knobs post-merge scrubs from the environment
  it inherits by pointing at `PM_SCRUB` (`:555-557`), and names post-merge and the driver beside the
  hook as scrubbing `GATE_REGEN_CHECK` (`:250-252`). Observed by AC22.
- **S32** — id 24. Unit 61's line `seed: HEAD is unborn, rows carry the null SHA` goes to stderr, so
  stdout keeps unit 15's one line per population. Observed by AC23.
- **S33** — id 32. A given `--sha` is checked against `TOOL-dWitnessedBar-13`'s SHA grammar, 8 to 40 hex;
  on a mismatch `seed` exits 2 naming `--sha` and writes no home. Observed by AC23.
- **S34** — id 34. Unit 58's AC2 decline half gains its positive twin: the same scoped run with
  `GATE_BASE_FROM` unset writes exactly one `.scoped` file for the tree under
  `<common-dir>/gate-verdict/`. A second staged break, a scratch copy with `TOOL-dWitnessedBar-40`'s
  decline taken out, reds the arm. Observed by AC24.

## 3. Non-goals (OUT)

- Re-wording another unit's spec text: each item is closed by what this pass builds or observes, and a
  criterion of an earlier unit that this pass replaces is answered in that unit's ledger by name.
- Renumbering any unit's `order` (ids 1 and 2): S14 and S23 observe the sequence the existing dispatch
  refusal and the sequential dispatch already hold (§8 F3).
- The spec lints, generator refusals and checklist entries the report names as left-shifts: each is a
  gate no clause of this build names. S1, S9, S16, S21, S22 and S34 stage the regression arms this
  batch builds.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-58` — S1's capturing stub, AC2's decline arm and its floor raise (ids 1, 14, 34)
- **consumes-from** `TOOL-dWitnessedBar-59` — AC2, AC3 and S1's reads of the policy file and `.unattended.conf` (ids 3, 8, 33)
- **consumes-from** `TOOL-dWitnessedBar-60` — S4's list arm, the `_gknobs` comment, the README's scrub sentences and its floor raise (ids 1, 9, 15, 16, 23, 26)
- **consumes-from** `TOOL-dWitnessedBar-61` — the unborn rule, its other-failure row, its unborn line and the `--sha` row (ids 2, 5, 13, 24, 31, 32)
- **consumes-from** `TOOL-dWitnessedBar-62` — S22, S24, S35, S37, S39, the `selection_row` block and AC7, AC13, AC17, AC18 and AC22 (ids 4, 6, 7, 8, 10, 11, 12, 17, 19, 20, 21, 22, 25, 27, 28, 29, 30, 35)
- **consumes-from** `TOOL-dWitnessedBar-57` — AC12's byte preservation in `up`, which answers unit 59's AC2 byte half (id 3)
- **consumes-from** `TOOL-dWitnessedBar-47` — its pass commit, which S14 observes landing after unit 61's (id 2)
- **consumes-from** `TOOL-dWitnessedBar-15` — S2's refused-home branch, which the no-HEAD path takes (ids 5, 13)
- **consumes-from** `TOOL-dWitnessedBar-40` — the scoped decline, which S34's second staged break removes (id 34)
- **hands-off** `TOOL-dWitnessedBar-64` — S8's unborn predicate, narrowed to a HEAD that names a branch which does not exist, with its corrupt-state fixtures (id 20)
- **hands-off** `TOOL-dWitnessedBar-65` — the round-1 audit's 22 minors on this unit: one `exists:` rule, the plants a leg runs, the order of units 47 and 61, the seed's routes and `--sha`, the sweep, the record readers, the `PM_SCRUB` reader and AC18 (ids 1, 2, 3, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26)

## 4. Design

### Why one unit

M6 admits two units only when both write sets, contracts and shared records are disjoint. Every group
of findings here meets unit 62's write set. The seed items (ids 5, 13, 24, 31, 32) and unit 62's
containment items (ids 12, 28, 22) write the three `legacy_ledger.py` copies and
`tools/lib/resolve-python.test.sh`. The policy items (ids 3, 8, 33) and the `exists:` items (ids 11, 17,
29) write `tools/govkit/selftest.py`. Unit 58's and 60's items (ids 1, 9, 14, 15, 16, 23, 26, 34) write
`tools/run-gates/run-gates.evidence.test.sh`, `tools/run-gates/run-gates.gov.test.sh` and
`tools/run-gates/README.md`, which unit 62's record items (ids 6, 10, 20, 27) also write. One unit holds
them, building after every other unit.

### Evidence

- `PM_SCRUB` spans `tools/run-gates/post-merge.sh:35-38`; the range read above prints those four lines,
  which hold 23 names at the base. The driver suite's cut is one-line
  (`tools/unattended/unattended.test.sh:4337`, `:4341`).
- `demand_contained_dest` folds `\` to `/`, normalises, and refuses `..`-leading, absolute, `ntpath`
  absolute and drive-lettered destinations (`tools/govkit/govkit.py:1304-1338`).
- `check_conf_reader_parity` captures bash with `text=True` (`tools/govkit/selftest.py:827-828`).
- `read_record_keys` splits with `IFS=$'\t' read -r _rk_k _rk_v` (`tools/run-gates/run-gates.sh:2392`),
  and the hook's record reads are `awk -F'\t' '$1=="<key>"{print $2}'` (`.githooks/pre-push:1354-1368`).
- lib-unattended's awk prints `f`, `p`, `g` and `w` TAB-joined with `g` possibly empty, and its reader
  splits with `IFS=$'\t'` and guards on a non-empty generator
  (`tools/unattended/lib-unattended.sh:868`, `:878-880`).
- The floor lines: `tools/run-gates/run-gates.evidence.test.sh:2451`,
  `tools/run-gates/run-gates.gov.test.sh:459`, `tools/run-gates/adopt-run-gates.test.sh:193`,
  `tools/memory-tree/check-memory-hygiene.test.sh:4371`.
- `build_commit` is `tools/unattended/lib-unattended.sh:1186`; the `--dispatch` edge refusal reads the
  dispatched unit's `consumes-from` edges and refuses it while a producer of its build is open
  (`tools/unattended/unattended.sh:13691-13764`).

### Inventory

Minted: the temp prefix `peer-signers-`; the constant `PEER_SIGNERS_GRACE_S`; the plant `key-no-tab`.
Naming cells: none, since the lexicon declares cells for functions and types only;
`python tools/lexicon/lexicon.py --suggest PEER_SIGNERS_GRACE_S --as py.constant` reports `py.constant`
undeclared.

### Migration

None: no item changes stored data. S17 and S19 read records written before them unchanged, a no-TAB
line being one no writer emits.

### Rollout

Live at landing, after every other unit of the build. S4, S5, S7, S14, S15, S23 and S27 are observed by
the main loop at the close, on the tree they grade.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/regen.py`
- `tools/run-gates/verdict_backends.py`
- `tools/run-gates/verdict_flow.py`
- `tools/run-gates/README.md`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/govkit/steps/inherited_red.py`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.sh`
- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `tools/lib/legacy_ledger.py`
- `tools/memory-tree/legacy_ledger.py`
- `tools/gate-lint/legacy_ledger.py`
- `tools/lib/resolve-python.test.sh`
- `tools/memory-tree/README.md`
- `tools/memory-tree/ratchet.py`

### Alternatives rejected

- **Two batches, seed-side and record-side.** Unit 62's containment and record items join the halves
  (§4 "Why one unit").
- **Keep 77 and exclude `refuse-wrong-shell.sh` from the coverage population (id 21's second option).**
  It adds a second named exclusion to unit 50's population to keep a stale number true (§8 F4).
- **Stamp the null SHA on the no-HEAD unarmed line (id 5's first option).** It says "seeded before any
  commit" of a tree git refused to read (§8 F2).
- **Reuse `TAIL_GRACE_S` for the signer sweep.** It is the runner's bash constant in another kit, and
  seven days keeps a stray signer file far longer than any read holds one (§8 F5).

## 5. Production-readiness checklist

- security — S9 to S11 contain `exists:` paths on Windows path forms through one rule; S8 and S6 stamp
  nothing in a tree git refuses to read; S33 validates `--sha` at the write boundary; S20 sweeps a killed
  read's signer file.
- perf / scale — a few more fixture trees and plants, a range `sed`, one directory scan per peer read.
- error / empty / loading states — S6, S12, S19 and S22 turn a missing HEAD, a cross-drive home, a
  no-TAB line and an empty field into named outcomes, never a traceback or a shifted field.
- observability — S3 prints each list's count; S32 keeps the unborn line off the status stream.
- risks — S4 and S5 drop a pinned figure from a criterion, so the probe and the tool must agree on the
  built tree instead.
- testing — AC1 to AC24 by fixture, plant and probe; the arms under §7 at the close.
- migration — none.
- user docs — S31 and S25 edit kit READMEs; no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When unit 60's list arm runs over the built tree, it prints a count for each of the four
  lists, `PM_SCRUB`'s at least 30, and no missing name; `sed -n '/^PM_SCRUB="/,/"$/p' tools/run-gates/post-merge.sh`
  prints the whole assignment, from the line opening `PM_SCRUB="GIT_DIR` to the line closing
  the quote, and the arm's `PM_SCRUB` holds `GATE_TURNSTILE_HOLDER`.
  Red when: the arm reads `PM_SCRUB` with a one-line cut and fails on an empty list.
  figure: 23 names at the base is PINNED at `cdfbd1cf`, measured 2026-10-25; 30 is that plus the seven
  unit 60 S2 adds.
- **AC2** — When the arm runs over a scratch copy of `tools/run-gates/post-merge.sh` with
  `GATE_SELECTION` cut from `PM_SCRUB`, it fails naming `GATE_SELECTION` and `PM_SCRUB`; with the
  assignment removed, it fails naming the empty list.
  Red when: a short or an empty `PM_SCRUB` passes the arm.
- **AC3** — When unit 62's §4 coverage probe and `bash refuse-wrong-shell.sh --coverage` run on the
  built tree, the probe's third number equals the tool's population, and the coverage arm lists each of
  the five spelling fixtures as a member.
  Red when: the two figures part, or a criterion holds the built tree to 77.
  figure: DERIVED at the close by the probe; 77 is PINNED at `8229ea5f` for the base alone.
- **AC4** — When `python legacy_ledger.py seed --population p` runs in a scratch directory outside any
  repository, it prints a line opening `unarmed p no HEAD: fatal: not a git repository`, writes no
  home, and no file under the directory holds forty `0` characters; in a commitless
  `git init` beside it the seed still prints `armed p 2` with null-SHA rows.
  Red when: the seed stamps the null SHA where git refused to read HEAD, or writes an unarmed line with
  an empty SHA field.
  fixture: two scratch directories under `%TEMP%/<short-name>`, one with `GIT_CEILING_DIRECTORIES` set
  to its parent, built by section `2l`.
- **AC5** — When each tree whose `exists:` path is `..\x`, `a\..\..\x`, `\x` or `\\server\share` is
  read, `regen.build_items` raises `Refusal` naming the row, lib-unattended's stderr names the
  descriptor and the `when` and keeps the conf-true row, and `govkit.py selfcheck` fails naming the row;
  with lib-unattended's backslash fold removed in a scratch copy, the arm reds on `..\x`.
  Red when: any of the three readers admits a backslash path.
  fixture: scratch trees under `%TEMP%/<short-name>`, built by the arm.
- **AC6** — When the seed-home containment test runs with `os.path.commonpath` replaced by one raising
  `ValueError`, it reads `outside the tree` with no traceback, and under `seed --all` the next
  population is still seeded; on a Windows host `seed --home Z:/x` with the fixture on another drive
  letter prints `outside the tree`.
  Red when: a cross-drive home raises out of the seed.
- **AC7** — When `build_commit` runs at the close over `cdfbd1cf..HEAD` for `TOOL-dWitnessedBar-61` and
  `TOOL-dWitnessedBar-47` with `tools/unattended/lib-unattended.sh` sourced, and
  `git merge-base --is-ancestor <61's sha> <47's sha>` runs, it exits 0.
  Red when: unit 47's pass landed before the unborn rule it consumes.
- **AC8** — When `grep -rn 'TOOL-dWitnessedBar-57' memory/builds/dWitnessedBar/build/` runs at the close,
  unit 59's AC2 ledger line names unit 57's AC12 for the byte half; and `python inherited_red.py up` over
  the lone-CR fixture on the built tree leaves the file equal, by `cmp`, to the input with that one
  physical line removed.
  Red when: unit 59's AC2 is recorded observed at step 23 by a byte compare its writer could not pass.
- **AC9** — When the govkit selftest's policy parity arm runs, its `lone-cr` row reads
  `park<CR>INHERITED_RED=land` on both sides and passes; with the bash capture switched to `text=True`
  in a scratch copy, the row reds against a correct step reader.
  Red when: a text-mode capture turns the CR into LF, or a normalising compare hides the difference.
- **AC10** — When `grep -n 'outside the tree' tools/lib/resolve-python.test.sh` runs on the built tree,
  it names section `2l`'s `.git`-home and cross-drive cases, and `grep -n 'resolve-python.test.sh' tools/gate-legs.json`
  names the leg `python resolver (behaviour + inline parity + idiom ban)`.
  Red when: unit 62's containment arm lives in a host no leg runs.
- **AC11** — When `python verdict_backends.py --fixture --plant key-no-tab` runs in `tools/run-gates/`,
  over a record holding a bare `reused` line, `read --backend local-hook` reads `reused` as absent with no
  traceback, and the hook's `read_green_file` leaves `rec_reused` empty over the same record.
  Red when: a no-TAB line yields its key as its value, or a reader raises.
- **AC12** — When a file `peer-signers-<x>` aged past 86400 seconds sits in the git dir and
  `--plant peer-no-ssh-keygen` runs, `ls <git-dir>` afterwards shows neither it nor the read's own
  signer temp; a prefixed temp younger than the grace survives.
  Red when: a killed read's signer file is never swept, or the sweep takes a live read's file.
- **AC13** — When `python inherited_red.py up <target>` runs over the S21 fixture, the path it resolves
  equals, byte for byte, the value `read_policy_key` extracted from `.githooks/pre-push` reads from the
  same conf, and `pol-b` is never opened; with only the conf read switched to text mode in a scratch
  copy, the arm reds.
  Red when: the step resolves a different policy file than the driver enforces.
- **AC14** — When a tree whose row carries `path` and `when = "exists:"` and no `generator` is read,
  lib-unattended prints S21's line naming the descriptor and the `when`, and its output holds only the
  conf-true row; `printf 'd\tp\t\tw\n'` read by the new split yields an empty generator and `w`.
  Red when: the `when` is taken as the generator and the row is kept.
- **AC15** — When `grep -nE 'RAISED .* by TOOL-dWitnessedBar-(58|60)' tools/run-gates/run-gates.evidence.test.sh`
  runs at the close, it prints two lines whose numbers chain, and
  `git log --merges --oneline cdfbd1cf..HEAD -- tools/run-gates/run-gates.evidence.test.sh` prints
  nothing.
  Red when: both raises start from one value, or two passes edited the suite concurrently.
- **AC16** — When `read_record_keys`, cut by `awk '/^read_record_keys\(\)/,/^}/' tools/run-gates/run-gates.sh`
  and sourced in a probe, reads a record holding `note<TAB>a<TAB>` and a bare `reused` line, `note` is
  `a<TAB>` and `reused` is unset.
  Red when: the runner strips the empty last field or takes a no-TAB line's key as its value.
- **AC17** — When `grep -n 'root confs in the working tree' README.md ratchet.py` runs in
  `tools/memory-tree/`, it names the adopter-receives table and each conf-set docstring, and
  `grep -rniE 'tracked root confs?|tracked confs' tools/memory-tree/` prints nothing.
  Red when: unit 62 S32 stays unbuilt, or a retired spelling survives.
- **AC18** — When `grep -c 'run-gates evidence: executed' tools/run-gates/run-gates.evidence.test.sh`,
  `grep -c 'gov-canary: executed' tools/run-gates/run-gates.gov.test.sh` and
  `grep -c 'adopt-e2e: executed' tools/run-gates/adopt-run-gates.test.sh` run, each prints at least 1,
  and unit 62's AC7 ledger line quotes each suite's own floor line.
  Red when: unit 62's AC7 is graded on `FAIL executed` for a suite that never prints it.
- **AC19** — When `grep -n 'GATE_BASE_FROM-unset' .githooks/pre-push.test.sh` runs on the built tree,
  the stub's redirect target is a variable rooted at the suite's `$tmp`, as `"$DOCS_ENV"` is.
  Red when: the stub writes under the fixture's git dir.
- **AC20** — When `grep -n 'BAR_CLEARED_KNOBS' tools/unattended/unattended.sh` and
  `grep -n 'run-gates.gov.test.sh' tools/unattended/unattended.sh` run, each names the comment above
  `_gknobs`.
  Red when: the comment still points only at the waived driver-suite arm.
- **AC21** — When `grep -n '^# >>> selection_row' verdict_flow.py` and `grep -n -- '--selection' verdict_flow.py`
  run in `tools/run-gates/`, each names its line, and the `--dispatch` row of the pass that wrote them names the file.
  Red when: the selection block or the `flakes` flag is missing, or written outside a declared set.
- **AC22** — When `grep -n 'PM_SCRUB' tools/run-gates/README.md` and
  `grep -n 'GATE_REGEN_CHECK' tools/run-gates/README.md` run, the first names the post-merge paragraph and
  the second names post-merge and the driver beside the hook.
  Red when: the README lists fewer dropped knobs than post-merge drops.
- **AC23** — When the seed runs in a commitless `git init`, every stdout line opens with `armed`,
  `present`, `widened` or `unarmed` and stderr carries `HEAD is unborn`; `seed --sha HEAD` exits 2
  naming `--sha` and writes no home.
  Red when: the unborn line lands on the status stream, or a symbolic `--sha` is stamped.
- **AC24** — When the runner runs scoped over unit 58's one-leg fixture manifest with `GATE_BASE_FROM`
  unset, `ls <common-dir>/gate-verdict/` shows exactly one `.scoped` file for the tree; with unit 40's
  decline removed in a scratch copy, the inherited run writes one and the arm reds.
  Red when: the absence half passes over a run that writes no `.scoped` file at that path either way.
  fixture: the scratch clone of unit 58's AC2 under `%TEMP%/<short-name>`.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `measure-legs selftest` · `routed-commits selftest` · `shell-hygiene selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `run-gates gov canary` · `run-gates evidence` · `pre-push self-test` · `kit/dogfood doc parity` · `memory hygiene`

The unattended kit's own suites are waived for this build's landing (README rule), so S9 and S22 are
observed by the govkit selftest arm. `ratchet selftest`, which `TOOL-dWitnessedBar-14` adds to the
manifest, runs unit 62's AC15 and AC20 plants once it exists.

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC2 · unit 60's list arm reading `PM_SCRUB` as a range and printing four counts, staged red by restoring the one-line cut · FLOOR_ASSERTIONS raised by these assertions
New arm: tools/govkit/selftest.py · covers AC5 AC9 AC13 AC14 · the backslash trees, the bytes capture, the lone-CR conf and the generator-less row, staged red by removing the backslash fold, a `text=True` capture and a text-mode conf read · none
New arm: tools/lib/resolve-python.test.sh · covers AC3 AC4 AC6 AC10 AC23 · section `2l` gains the no-HEAD, cross-drive, `.git`-home, unborn-stderr and `--sha` cases, staged red by a string-prefix compare and by stamping the null SHA on exit 128 · none
New arm: tools/run-gates/verdict_backends.py · covers AC11 AC12 · the `key-no-tab` plant and the aged signer temp, staged red by unpacking two fields and by deleting the sweep · none
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC16 AC24 · the `read_record_keys` probe and unit 58's positive twin, staged red by restoring the `IFS=$'\t'` split and by removing unit 40's decline · FLOOR_ASSERTIONS raised by these assertions

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of each repaired unit's clause. The repaired units are
  themselves derived and carry none, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Where does unit 61's no-HEAD path go (ids 5, 13, 31)?** Options: (a) an unarmed line carrying
  the null SHA; (b) unit 15 S2's refused-home branch: no file, the reason on stderr. (a) writes "seeded
  before any commit" into a tree git refused to read, the conflation id 31 names, and a rerun reads that
  line as a seeded state's SHA. (b) reuses a branch unit 15 already defines and writes nothing where
  HEAD is unknown. RESOLVED (agent, 2026-10-25, delegated): (b), rung 3, the most criteria met with no
  new line shape, tie-broken by reuse of unit 15's branch. widens: none · relaxes: none
- **F3 — How are the two order defects closed (ids 1, 2)?** Options: (a) renumber units 47, 61, 58 and
  60; (b) make the index generator refuse a step whose units share an edge or a written file; (c)
  observe at the close the sequence that `--dispatch`'s edge refusal and the sequential dispatch
  already hold. (a) re-words specs this batch does not write, a §3 Non-goal; veto 1 discards it. (b) reds
  this build's own steps 2, 5 and 33 on the real tree, whose units share
  `tools/lib/resolve-python.test.sh`, an edge, and the evidence suite, and is a left-shift gate no clause
  names; veto 1 discards it against `memory hygiene`. RESOLVED (agent, 2026-10-25, delegated): (c),
  rung 3, the one survivor. widens: none · relaxes: none
- **F4 — Which coverage figure does unit 62 grade (ids 4, 21)?** Options: (a) a figure the built tree
  re-derives, the probe and the tool agreeing; (b) keep 77 and exclude `refuse-wrong-shell.sh` in both
  the probe and `--coverage`. (b) shrinks a population to keep a number and leaves the next tracked
  caller to break it again. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the most criteria met
  with no new exclusion, as unit 57's AC1 already words its figure. widens: none · relaxes: none
- **F5 — How old is a stale signer temp (id 30)?** Options: (a) one day, a module constant; (b)
  `TAIL_GRACE_S`'s seven days; (c) any age. (c) races a concurrent peer read's live file; (b) borrows a
  bash constant of another kit and keeps a stray file a week. RESOLVED (agent, 2026-10-25, delegated):
  (a), rung 3, sweeping within a day while no live read holds its file that long.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 58 to 62: 22 MEDIUM
  and 12 LOW findings, batched.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring TOOL-dWitnessedBar-64's
  and TOOL-dWitnessedBar-65's consumes-from edges, promoted by the round-1 spec audit of this unit;
  nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names: post-merge's own fold of `PM_SCRUB`
(`tools/run-gates/post-merge.sh:40-43`) for S1 to S3, `demand_contained_dest`
(`tools/govkit/govkit.py:1304`) for S10 and S11, `read_gate_policy`'s pattern
(`tools/unattended/unattended.sh:9566-9567`) for S9, unit 15 S2's refused-home branch for S6,
`build_commit` (`tools/unattended/lib-unattended.sh:1186`) and the `--dispatch` edge refusal for S14, the
`docstub` capture (`.githooks/pre-push.test.sh:1821-1823`) for S28, and section `2l` of the resolver
suite for S18. `python tools/codebase-map/reuse_lookup.py "read a multi-line quoted shell list and fold
its newlines"` ranked `read`, `read_text`, `read_conf` and `read_journal`, none a reader of a multi-line
shell assignment, so no existing seam fits beyond post-merge's fold. `python
tools/codebase-map/reuse_lookup.py "refuse a destination path that escapes the repository"` ranked
`CensusRefused`, `ScopeRefused` and `build_spec_path_re` and missed `demand_contained_dest`, which reading
`tools/govkit/govkit.py:1288-1338` found; that probe's miss is recorded here, where the map and the
source disagree.

Recall terms used: `python tools/memory-recall/query.py "what did the round-1 audit of units 58 to 62 find" --terms "PM_SCRUB multi-line cut coverage figure null SHA exists containment backslash commonpath lone CR bytes capture floor line"`
