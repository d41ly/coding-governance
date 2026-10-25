# TOOL-dWitnessedBar-65 — the round-1 audit of unit 63, its 22 minors batched: one containment rule in three readers, plants a leg runs, a seed order that never stalls, honest seed and sweep failures, and readers that keep every normalisation

**Status:** OPEN · rev-3 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 37 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 |
| [2026-10-25-build-TOOL-dWitnessedBar-64-round5-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-64-round5-fix-return.md) | research | TOOL-dWitnessedBar-64 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-64-round5-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-64-round5-fix-brief.md) | research | TOOL-dWitnessedBar-64 |
| [2026-10-25-review-TOOL-dWitnessedBar-64-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-64-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-64 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of unit 63
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-63-spec-audit-round1.md`)
exited CONVERGED with 23 confirmed findings: one HIGH, which `TOOL-dWitnessedBar-64` takes, and 22
minors. BUILD-METHOD M4 batches every MEDIUM and LOW into one unit, or two only where they split into
disjoint write sets by M6's clauses so that both build concurrently. §4 "Why one unit" says why these
stay one. Each finding is named by report id and is its own scope item, including where the report
merged ids into one item. Every finding lands on `TOOL-dWitnessedBar-63`, so this unit repairs that
unit and builds after it (order 37, one step after `TOOL-dWitnessedBar-64`). The report's ids 4, 9 and 12 were refuted by the audit
itself and are no finding here.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 2, 7, 21 | S1, S2, S3 |
| M2 | MEDIUM | 3, 8 | S4, S5 |
| M3 | MEDIUM | 1 | S6 |
| M4 | MEDIUM | 15 | S7 |
| M5 | MEDIUM | 16 | S8 |
| M6 | MEDIUM | 23 | S9 |
| M7 | MEDIUM | 24 | S10 |
| M8 | MEDIUM | 22 | S11 |
| L1 | LOW | 5, 19 | S12, S13 |
| L2 | LOW | 17, 25 | S14, S15 |
| L3 | LOW | 10 | S16 |
| L4 | LOW | 26 | S17 |
| L5 | LOW | 6 | S18 |
| L6 | LOW | 11 | S19 |
| L7 | LOW | 13 | S20 |
| L8 | LOW | 14 | S21 |
| L9 | LOW | 18 | S22 |

That is 11 MEDIUM and 11 LOW findings by raw id.

## 2. Scope (IN)

- **S1** — id 2. One table of `exists:` forms is fed to all three readers by one arm, which fails on
  any disagreement. The table holds unit 63's AC5 forms `..\x`, `a\..\..\x`, `\x` and
  `\\server\share`, the forms the two rules split on, `a/../b`, `a\..\b`, `a/..`, `x/..` and `1:x`,
  then `C:x`, and the admitted controls `a/b`, `a..b/c` and `.x/y`. Each row states one expected
  outcome for all three readers. Observed by AC1.
- **S2** — id 7. The one rule, which makes unit 63's §5 "through one rule" true. With every `\` folded
  to `/`, a path is refused when it starts with `/`, when its second character is `:`, or when any `/`
  segment is exactly `..`. lib-unattended's form (unit 63 S9) widens `[A-Za-z]:*` to `?:*`:
  `case "${p//\\//}" in /*|?:*|..|../*|*/..|*/../*)`. Observed by AC1.
- **S3** — id 21. govkit selfcheck's `exists:` check (unit 63 S10) and regen's (unit 63 S11) apply S2's
  rule in Python, `p.startswith('/') or p[1:2] == ':' or '..' in p.split('/')` over the folded `p`, in
  place of `demand_contained_dest`'s normpath predicate. So unit 62 S22, "holds a `..` segment is
  refused", stands in all three readers. Observed by AC1.
- **S4** — id 3. `tools/run-gates/run-gates.gov.test.sh`, run by the `run-gates gov canary` leg,
  calls `verdict_backends.py --fixture --plant key-no-tab` and asserts unit 63 AC11's outcome.
  Observed by AC3.
- **S5** — id 8. The same suite calls the aged-signer case under `--plant peer-no-ssh-keygen` and
  asserts unit 63 AC12's outcome. Its `FLOOR_ASSERTIONS` (16 at the base,
  `tools/run-gates/run-gates.gov.test.sh:94`) is raised by these assertions, starting from the value
  the build's last earlier raise set. Observed by AC3.
- **S6** — id 1. `TOOL-dWitnessedBar-47` moves to order 6 and `TOOL-dWitnessedBar-61` stays at order 5,
  so unit 61 is CLOSED before unit 47 is handed out and the `--dispatch` edge refusal never fires on
  47. 47's consumers sit at orders 10, 32, 35 and 37, and no order-6 unit has an edge to it. This item
  is applied in the commit that lands this spec, as unit 47's rev-5 with its §9 line (§8 F3). It
  supersedes unit 63 S14's sequencing claim and, for unit 47, unit 63's §3 renumbering non-goal and
  its §8 F3 resolution. It also makes unit 61's Rollout sentence "It shares order 5 with
  `TOOL-dWitnessedBar-47`" stale. Unit 63's ledger answers S14 and unit 61's ledger answers that
  sentence, each naming this item. Observed by AC4.
- **S7** — id 15. Section `2l` of `tools/lib/resolve-python.test.sh` reads unit 61 AC1's
  `HEAD is unborn` from the seed's stderr capture, which unit 63 S32 moves it to. This unit's §7 names
  `memory-hygiene self-test`, `codebase-map adopter e2e`, `codebase-map kit selftest` and
  `drift-audit selftest`. Those legs run the arms of units 46, 47 and 53, which unit 63's seed changes
  reach. Observed by AC5.
- **S8** — id 16. The seed CLI resolves its SHA, and with it unit 63 S6's no-HEAD route, before it reads
  registrations or the home. On the no-HEAD route it prints `unarmed <name> no HEAD: <reason>` for each
  population `--population` names and writes nothing. Under `--all` where no repository root
  resolves, stdout is empty and stderr carries `seed: no HEAD: <reason>`. Observed by AC6.
- **S9** — id 23. Every git call of the seed's SHA resolution catches `OSError` and
  `subprocess.TimeoutExpired` into the no-HEAD route with the reason `git not runnable: <exception>`.
  A non-zero exit with empty stderr gives `git <verb> exit <rc>`, the form `TOOL-dWitnessedBar-64` S3
  spells for its own probes. `seed --all` goes on to the next population either way. Observed by AC7.
- **S10** — id 24. A given `--sha` passes unit 63 S33's hex grammar and then must resolve:
  `git rev-parse --verify --quiet <sha>^{commit}` exits 0. The seed stamps the full lowercase SHA that
  call prints, so case and abbreviation fold to one spelling (§8 F4). The null SHA is admitted only
  where the seed's unborn predicate holds, whichever form of it is built. Anything else exits 2 naming
  `--sha` and writes no home. Observed by AC8.
- **S11** — id 22. Unit 63 S20's sweep inside `read_peer_verdict` touches regular files only
  (`is_file(follow_symlinks=False)`). Each unlink catches `OSError`: `FileNotFoundError` is silent, and
  any other error writes one stderr line naming the file. The read goes on either way, and its verdict
  never depends on the sweep. Observed by AC9.
- **S12** — id 5. Unit 63's AC18 is graded on its ledger half alone. Its three `grep -c` probes print 1
  at the base, so they cannot red, and unit 63's AC18 ledger line names this item for that half.
  Observed by AC10.
- **S13** — id 19. The ledger half is checked. Unit 62's AC7 ledger line names each suite's own floor
  string: `run-gates evidence: executed`, `gov-canary: executed`, `adopt-e2e: executed`, and
  `FAIL executed` beside `check-memory-hygiene.test.sh` and no other suite. Observed by AC10.
- **S14** — id 17. Unit 63 S17's `read_record_keys` rewrite keeps the existing normalisations by name.
  It strips one trailing CR from the value, as `${_rk_v%$'\r'}` does today
  (`tools/run-gates/run-gates.sh:2393`), and on a repeated key the last line wins. Observed by AC11.
- **S15** — id 25. Unit 63 S19's readers strip one trailing CR and keep the last of a repeated key. The
  awk form stores the value and prints it at `END`, where today's hook readers print every match and
  keep the CR (`.githooks/pre-push:1354-1368`). The Python form overwrites on each match. Observed by
  AC12.
- **S16** — id 10. Unit 63 S1's `PM_SCRUB` reader strips the leading `PM_SCRUB="` as well as the
  closing quote. The arm asserts `GIT_DIR` as the list's first whole word and `GATE_TURNSTILE_HOLDER`
  as its last. Observed by AC13.
- **S17** — id 26. The reader runs from the line opening `PM_SCRUB="` to the first line, that opening
  line included, holding the closing quote. It is written in awk rather than as a `sed` range. Text
  after the closing quote is discarded, and the arm fails on any token not matching
  `^[A-Z_][A-Z0-9_]*$`. Observed by AC14.
- **S18** — id 6. This unit's §7 names `run-gates canary`, the suite that grades `regen.py`, and
  `pre-push bar self-test`, for the hook readers S15 changes. NOT OBSERVED: the item is this spec's
  declared gate set, which the close runs; no criterion of a unit observes its own §7.
- **S19** — id 11. The cites a builder of unit 63 needs, correct at base `cdfbd1cf`. The text-mode
  capture is `tools/govkit/selftest.py:831-832`. lib-unattended's TAB-joined print is
  `tools/unattended/lib-unattended.sh:869`, and its `IFS=$'\t'` reader and generator guard are
  `:880-882`. NOT OBSERVED: these are corrections to spec text, and no built artifact carries them.
  §4 Evidence gives the command that re-derives each.
- **S20** — id 13. Selfcheck's `exists:` failure is its own line, naming the descriptor, the row and
  the path. S3 takes `demand_contained_dest` out of this check, so its fixed `.governance/deploy.toml`
  hint (`tools/govkit/govkit.py:1332-1337`) cannot reach the operator. Observed by AC2.
- **S21** — id 14. The comment beside `PEER_SIGNERS_GRACE_S` in `tools/run-gates/verdict_backends.py`
  names `TAIL_GRACE_S` (`TOOL-dWitnessedBar-42`) as the same run-gates kit's bash constant for the
  tail sweep. It gives the constant's seven-day span and its bash side as the reasons it is not
  reused. `tools/run-gates/kit.toml` declares `id = "run-gates"` (:11) and `include = "**"` (:18).
  Observed by AC15.
- **S22** — id 18. Unit 62's 77-carriers are answered by name: S19 (spec-62:129) and its §4 probe
  comment (spec-62:252, :269) in unit 62's ledger beside AC13, with 77 named as the base figure only.
  The inventory is `grep -nw 77` over unit 62's spec, which prints lines 129, 130, 252, 269, 389,
  390, 392 and 404. Observed by AC16.

## 3. Non-goals (OUT)

- Re-wording unit 63's spec text, or any other unit's except unit 47's status header (S6). Each item is
  closed by what this pass builds or observes. A claim or criterion of unit 63 that an item replaces is
  answered in unit 63's ledger by name.
- The unborn predicate itself, which is `TOOL-dWitnessedBar-64`'s (id 20). S10 calls the seed's
  predicate in whichever form is built, so the two units build in either order.
- The spec lints, roster lint and checklist entries the report names as left-shift gates. No clause
  of this build names them. S1's shared-table arm and S17's token grammar are the regression arms
  this batch builds.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-63` — every item amends what unit 63 builds: its containment readers, plants, seed routes, sweep, record readers, `PM_SCRUB` reader and its AC18 (all 22 ids)
- **consumes-from** `TOOL-dWitnessedBar-47` — its pass commit at order 6, which S6 observes landing after unit 61's (id 1)
- **hands-off** `TOOL-dWitnessedBar-66` — AC12's hook half, which the round-1 audit of units 64 and 65 found planted on a key `read_green_file` never reads, replanted on `sha` (id 6)
- **hands-off** `TOOL-dWitnessedBar-67` — the round-1 audit of units 64 and 65's minors on this unit: the AC12 `fingerprint` line, the sweep's arm and every filesystem call, the `PM_SCRUB` arm graded on the built list and its single assignment, the seed's timeout, `--all` route and `--sha` prefix check, the unterminated record line, AC4's per-file read, the segment rule's bytes and its second Python spelling, and this unit's order (ids 1, 3, 5, 7, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 23)
- **hands-off** `TOOL-dWitnessedBar-69` — S15's one-CR strip and last-wins rule, which the round-1 spec audit of units 66 and 67 found unreachable on Git for Windows behind the hook's `$(awk ...)` reads and Python's default text-mode open, moved onto a whole-line bash read and a `newline=''` open (id 19)

## 4. Design

### Why one unit

M4 admits a second unit only so that the two halves build concurrently. Here no concurrency is
available to buy. Dispatch is strictly sequential, a shared order included
(`tools/workflows/unattended-build.js:76-80`). The seed half (ids 15, 16, 23 and 24) writes the three
`legacy_ledger.py` copies and `tools/lib/resolve-python.test.sh`, which `TOOL-dWitnessedBar-64` also
writes. When this spec was written both units sat at order 36, so a seed half split off from this unit
would have sat beside a unit holding its whole write set, and would never have built beside it.
`TOOL-dWitnessedBar-67` S16 has since moved this unit to order 37. One unit holds all 22 findings.

### Evidence

- The two rules part both ways. `read_gate_policy`'s pattern is `/*|[A-Za-z]:*|..|../*|*/..|*/../*`
  (`tools/unattended/unattended.sh:9566-9567`). `demand_contained_dest` normalises with
  `posixpath.normpath` and refuses only an escaping result (`tools/govkit/govkit.py:1329-1331`). The
  report's probe found `a/../b` refused by the first and admitted by the second, and `1:x` the other
  way round.
- S2's rule refuses every path the normpath rule refuses. An escaping normal form needs a `..`
  segment or a leading `/` in the folded text. `ntpath.isabs` holds only for a folded leading `/` or
  a second-character `:`. So one rule, read in two languages, replaces both.
- The hand-out sorts an order tie by id string (`tools/workflows/unattended-build.js:612`). The unit
  child stops on a `--dispatch` refusal (`tools/workflows/unattended-unit.js:246`). The edge refusal
  fails 49 and picks no next unit (`tools/unattended/unattended.sh:13746-13760`).
- `grep -n verdict_backends tools/gate-legs.json` prints nothing. The `run-gates gov canary` leg runs
  `run-gates.gov.test.sh` (`tools/gate-legs.json:1184-1188`).
- Unit 47's edges are `consumes-from` 15 (order 4) and 61 (order 5), and `hands-off` 46 (order 10),
  57 (order 32) and 63 (order 35). Unit 22, the one unit at order 6, writes none of unit 47's files.
- The runner's reader strips one CR and lets a later line overwrite an earlier one
  (`tools/run-gates/run-gates.sh:2387-2397`). The hook's reads are `awk -F'\t' '$1=="<key>"{print $2}'`
  (`.githooks/pre-push:1354-1368`).
- `PM_SCRUB` spans `tools/run-gates/post-merge.sh:35-38`, and `PM_DROPPED=""` is line 39.
- The base cites S19 corrects: `git show cdfbd1cf:tools/govkit/selftest.py | sed -n 831,832p` prints
  the `text=True` capture, and `git show cdfbd1cf:tools/unattended/lib-unattended.sh | sed -n '869p;880,882p'`
  prints the TAB-joined `print`, the `IFS=$'\t'` reader and its generator guard.
- AC18's three probes each print 1 at the base. So does `grep -c 'FAIL executed'
  tools/memory-tree/check-memory-hygiene.test.sh`.

### Inventory

Minted: the reasons `git not runnable: <exception>` and `seed: no HEAD: <reason>`, and the arm's table
of `exists:` forms. The form `git <verb> exit <rc>` is `TOOL-dWitnessedBar-64`'s, spelled the same here.
No function, constant, plant or flag is minted. Naming cells: none apply.

### Migration

None: no item changes stored data. S14 and S15 read records written before them unchanged, since the
runner escapes CR when it appends and writes each key once.

### Rollout

S6 is applied in the commit that lands this spec, before step 5 is dispatched. Every other item is
live at landing at order 37, after `TOOL-dWitnessedBar-63` (35) and `TOOL-dWitnessedBar-64` (36).
`TOOL-dWitnessedBar-67` S16 gave this unit its own order, applied in the commit that lands that spec,
because both units write the seed files and so fail BUILD-METHOD M6's first condition. Neither unit
consumes from the other. S1, S8, S9, S10, S11 and S14 to S17 stage the regression arms under §7. S6, S12, S13 and S22 are
observed by the main loop at the close.

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/run-gates/regen.py`
- `tools/run-gates/run-gates.gov.test.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/verdict_backends.py`
- `.githooks/pre-push`
- `tools/lib/legacy_ledger.py`
- `tools/memory-tree/legacy_ledger.py`
- `tools/gate-lint/legacy_ledger.py`
- `tools/lib/resolve-python.test.sh`

### Alternatives rejected

- **The normpath rule in all three readers (id 2's first option).** lib-unattended would need a
  `normpath` written in bash. It would also admit `a/../b`, which unit 62 S22 refuses (§8 F2).
- **Two batches, seed-side and the rest.** §4 "Why one unit".
- **Teach the hand-out to break an order tie by `consumes-from` edges (id 1).** That is new behaviour
  in the unattended kit, whose suites this build waives. Built at order 36, it would land after the
  step-5 stall it is meant to prevent (§8 F3).

## 5. Production-readiness checklist

- security — S1 to S3 make `exists:` containment one rule in three readers. S10 checks `--sha` for
  existence at the write boundary. S8 and S9 write nothing where HEAD is unknown.
- perf / scale — one `rev-parse` per given `--sha`, a 13-row table arm, and two more plant calls in
  the gov suite.
- error / empty / loading states — S8, S9 and S11 turn a missing repository, an unrunnable git and a
  failed unlink into named outcomes, never a traceback.
- observability — S9's reasons name the git verb and exit code, and S11 names a file it could not
  unlink.
- risks — S6 changes another unit's order. The id-string tie break and the edge refusal then agree,
  and AC4 observes the sequence at the close.
- testing — AC1 to AC16 by fixture, plant and probe. The arms under §7 at the close.
- migration — none.
- user docs — none under `help/`. No user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When the govkit selftest's `exists:` arm feeds S1's table to lib-unattended's generated-row
  reader, `regen.build_items` and `govkit.py selfcheck`, each reader refuses each of the first ten
  forms and admits each control. Refused means lib-unattended skips the row with unit 62 S21's line,
  regen raises `Refusal` naming the row, and selfcheck fails naming the row. The arm prints one line
  per form with the three outcomes.
  Red when: any two readers part on one form, or a reader admits a `..` segment or a second-character
  `:`.
  fixture: scratch trees under `%TEMP%/<short-name>`, built by the arm.
- **AC2** — When `govkit.py selfcheck` runs over the table's `a/../b` tree, its failure line names the
  descriptor, the row and `a/../b`, and `grep -c deploy.toml` over its output prints 0.
  Red when: selfcheck passes `demand_contained_dest`'s Refusal text through.
- **AC3** — When `grep -nE -- '--plant (key-no-tab|peer-no-ssh-keygen)' tools/run-gates/run-gates.gov.test.sh`
  runs on the built tree, it names both plants, and each call is followed by an assertion of its
  outcome. `python verdict_backends.py --fixture --plant peer-no-ssh-keygen`, run in `tools/run-gates/`
  with a `peer-signers-` file aged past 86400 seconds in the git dir, leaves no such file.
  Red when: the plants sit in a mode no named leg runs.
- **AC4** — When `sed -n 3p` runs over unit 47's and unit 61's specs, unit 47's header carries `order 6`
  and unit 61's carries `order 5`. At the close,
  `grep -nE ' dispatch · item [0-9a-f]+ TOOL-dWitnessedBar-(61|47) ' memory/builds/dWitnessedBar/RUN.md`
  prints 61's row above 47's. `git merge-base --is-ancestor` of unit 61's pass commit and unit 47's,
  each found by `build_commit`, exits 0.
  Red when: the run stopped at `--dispatch` for unit 47, or the two units share an order again.
- **AC5** — When the seed runs in a commitless `git init` with stdout and stderr captured apart,
  `HEAD is unborn` is in the stderr capture only. `grep -n 'HEAD is unborn' tools/lib/resolve-python.test.sh`
  names section `2l`'s assertion over the stderr capture.
  Red when: section `2l` looks for the unborn line on stdout, which unit 63 S32 has emptied of it.
- **AC6** — When `python legacy_ledger.py seed --population p` runs in a scratch directory with
  `GIT_CEILING_DIRECTORIES` set to its parent, stdout is one line opening `unarmed p no HEAD: `, stderr
  carries the reason and no `Traceback`, and nothing is written. With `--all` in its place, stdout is
  empty and stderr carries `seed: no HEAD: `.
  Red when: the seed reads registrations or the home first and fails with another message.
  fixture: a scratch directory under `%TEMP%/<short-name>`, built by section `2l`.
- **AC7** — When the seed runs with `PATH` naming only an empty scratch directory and python invoked by
  absolute path, stdout opens `unarmed p no HEAD: git not runnable: ` and stderr holds no `Traceback`.
  A probe importing `legacy_ledger.py` replaces `subprocess.run` for `rev-parse` calls, once with
  one raising `subprocess.TimeoutExpired` and once with one exiting 2 silently. Under `seed --all`
  over two registrations, each population then prints a no-HEAD line, the second reading
  `git rev-parse exit 2`.
  Red when: a spawn failure, a timeout or a silent non-zero exit raises out of the seed, prints an empty
  reason, or stops `--all` at its first population.
- **AC8** — When `seed --sha 0000000000000000000000000000000000000000` runs in a fixture holding one
  commit, it exits 2 naming `--sha` and writes no home. So does `seed --sha deadbeef` where
  `git rev-parse --verify --quiet deadbeef^{commit}` exits non-zero. `seed --sha` given HEAD's first 8
  hex characters in upper case arms the population, its rows carrying HEAD's full lowercase SHA. In a
  commitless `git init`, `seed --sha 0000000000000000000000000000000000000000` arms with null-SHA rows.
  Red when: a SHA naming no commit is stamped, or the null SHA is stamped in a repository with commits.
- **AC9** — When a probe importing `verdict_backends.py` runs the peer read with `os.unlink` replaced, two
  aged `peer-signers-` files present and an aged directory named `peer-signers-d`, the read returns the
  verdict it returns with no stale entry. The stand-in raises `FileNotFoundError` for one file and
  `PermissionError` for the other. Stderr names the second file once, and the directory survives.
  Red when: the sweep raises into the read, changes its verdict, or touches an entry that is not a
  regular file.
- **AC10** — When `grep -n 'AC7' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-62*acceptance-ledger*`
  runs at the close, the line names `run-gates evidence: executed`, `gov-canary: executed`,
  `adopt-e2e: executed` and `FAIL executed`, the last beside the memory-tree hygiene suite alone. Unit
  63's AC18 ledger line names this unit's S12 for its grep half.
  Red when: unit 62's AC7 is graded on `FAIL executed` for another suite, or unit 63's AC18 is recorded
  green on its grep half.
- **AC11** — When `read_record_keys`, cut by `awk '/^read_record_keys\(\)/,/^}/' tools/run-gates/run-gates.sh`
  and sourced in a probe, reads a record holding `verdict<TAB>GREEN<CR>`, `note<TAB>a<TAB>`, then
  `head<TAB>x` followed by `head<TAB>y`, it gives `verdict` as `GREEN`, `note` as `a<TAB>` and `head`
  as `y`.
  Red when: the rewrite drops the CR strip, or keeps the first of a repeated key.
- **AC12** — When the `key-no-tab` plant's record also holds `verdict<TAB>GREEN<CR>` and two `sha`
  lines, `read --backend local-hook` and the hook's `read_green_file`, cut by
  `awk '/^read_green_file\(\)/,/^}/' .githooks/pre-push`, each read `GREEN` and the second `sha`.
  Red when: the two readers part on a CRLF line or a repeated key.
- **AC13** — When unit 60's list arm reads `PM_SCRUB` from `tools/run-gates/post-merge.sh`, the list's
  first word is `GIT_DIR` and its last is `GATE_TURNSTILE_HOLDER`, each a whole word, and no word holds
  `=` or `"`.
  Red when: the first word reads `PM_SCRUB=GIT_DIR`.
- **AC14** — When the reader runs over a scratch copy of `tools/run-gates/post-merge.sh` with
  `  # note GATE_SELECTION` after the closing quote, and over one with the assignment on a single line,
  each reads exactly the base list. With `GATE_SELECTION` cut from the list while the comment still
  names it, the arm fails naming `GATE_SELECTION`. A planted token `bad-name` fails the grammar
  `^[A-Z_][A-Z0-9_]*$`.
  Red when: a trailing comment's words enter the name set, or the read runs past the closing quote.
- **AC15** — When `grep -n 'TAIL_GRACE_S' verdict_backends.py` runs in `tools/run-gates/` on the built
  tree, it names the comment beside `PEER_SIGNERS_GRACE_S`, which calls `TAIL_GRACE_S` the run-gates
  kit's own constant. `grep -nE 'another kit' verdict_backends.py`, run in the same directory, prints
  no line naming `TAIL_GRACE_S`.
  Red when: the comment places the constant in another kit, or is absent.
- **AC16** — When `grep -nw 77 memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-62.md`
  runs, it prints lines 129, 130, 252, 269, 389, 390, 392 and 404. At the close, unit 62's ledger line
  for AC13 names S19 and the §4 probe comment, with 77 as the base figure and the built tree's derived
  figure beside it.
  Red when: a 77-carrier of unit 62 is answered by no ledger line.
  figure: the eight lines are PINNED at `bc979397`, measured 2026-10-25.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `routed-commits selftest` · `measure-legs selftest` · `shell-hygiene selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `run-gates gov canary` · `run-gates canary` · `run-gates evidence` · `pre-push self-test` · `pre-push bar self-test` · `memory-hygiene self-test` · `codebase-map adopter e2e` · `codebase-map kit selftest` · `drift-audit selftest` · `memory hygiene`

The unattended kit's own suites are waived for this build's landing (README rule), so S2's bash
reader is observed through the govkit selftest arm, as unit 63's S9 is. The four kit legs and
`pre-push bar self-test` are held unless the main loop sets GATE_SELFTESTS at the close.

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the shared `exists:` table over the three readers, staged red by restoring `demand_contained_dest`'s normpath predicate in regen's copy, which admits `a/../b` · none
New arm: tools/run-gates/run-gates.gov.test.sh · covers AC3 AC12 AC13 AC14 · the `key-no-tab` and aged-signer plant calls, the CRLF and repeated-key record, and the `PM_SCRUB` reader's first-word, trailing-comment, one-line and token-grammar cases, staged red by deleting the sweep, by removing the hook's CR strip, and by restoring the `sed` range · FLOOR_ASSERTIONS raised by these assertions
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC11 · the `read_record_keys` CRLF and repeated-key cases, staged red by removing the CR strip · FLOOR_ASSERTIONS raised by these assertions
New arm: tools/lib/resolve-python.test.sh · covers AC5 AC6 AC7 AC8 · section `2l` gains the stderr read of the unborn line, the outside-any-repository seed, the empty-`PATH` and stand-in probe failures, and the four `--sha` cases, staged red by reading registrations before HEAD and by dropping the existence check · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 63 is itself derived
  and carries none, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which containment rule do the three `exists:` readers share (ids 2, 7, 21)?** Options: (a) the
  segment rule, refusing a leading `/`, a second-character `:` and any `..` segment after folding `\`;
  (b) `demand_contained_dest`'s normpath rule in all three. (b) admits `a/../b`, which unit 62 S22
  refuses, and needs a bash `normpath`. Veto 1 discards it against unit 62's AC2. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3. It refuses every form (b) refuses (§4 Evidence), and it is
  tie-broken by reuse of `read_gate_policy`'s pattern.
  widens: none · relaxes: none
- **F3 — How does unit 61 come to build before unit 47 (id 1)?** Options: (a) move unit 47 to order 6,
  applied in the commit that lands this spec; (b) the same move made in this unit's build pass;
  (c) teach the hand-out to break order ties by edges. (b) lands at order 36, after the step-5 stall,
  so AC4 cannot pass. (c) also lands at order 36, and needs the unattended kit's waived suites. Veto 1
  discards both. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the one survivor and the
  report's corrected fix. It is applied as unit 47's rev-5 with its §9 line.
  widens: none · relaxes: none
- **F4 — What does a given `--sha` stamp (id 24)?** Options: (a) the value as given, once it resolves;
  (b) the full lowercase SHA that `rev-parse --verify <sha>^{commit}` prints. (a) leaves the report's
  case question open and stamps abbreviations, which unit 14 S9's compare with the base's SHA would read
  as different. RESOLVED (agent, 2026-10-25, delegated): (b), rung 3. It meets the most criteria and
  leaves no open question, and the resolving call is the existence check S10 already makes.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of unit 63: 11 MEDIUM and
  11 LOW findings, batched.
- rev-2 · 2026-10-25 · §1 · §3 · §4 · S6 · the header's order moves from 36 to 37, applied as
  `TOOL-dWitnessedBar-67` S16 (id 14 of the round-1 audit of units 64 and 65), with §1, S6's consumer
  orders, §4 "Why one unit" and §4 Rollout restated to match. §3 gains the hands-off edges to units 66
  and 67. No scope item or criterion moves.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-69's
  consumes-from edge, promoted by the round-1 spec audit of units 66 and 67; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names. S2 and S3 reuse `read_gate_policy`'s pattern
(`tools/unattended/unattended.sh:9566-9567`), widened by one character class. S6 reuses the order verb
and the `--dispatch` edge refusal (`tools/unattended/unattended.sh:13746-13760`). S4 and S5 reuse the
gov suite's plant calls, which units 6 and 56 already make. S14 and S15 reuse the runner's CR strip
(`tools/run-gates/run-gates.sh:2393`). S16 and S17 reuse post-merge's own fold of `PM_SCRUB`
(`tools/run-gates/post-merge.sh:40-43`).

`python tools/codebase-map/reuse_lookup.py "refuse a repo-relative path holding a dot-dot segment"`
ranked `repo_root`, `CensusRefused`, `ScopeRefused` and `build_spec_path_re`. It missed both
containment rules, which reading `tools/unattended/unattended.sh:9566-9567` and
`tools/govkit/govkit.py:1304-1338` found, so the map and the source disagree here. No existing seam
fits beyond those two.

Recall terms used: `python tools/memory-recall/query.py "what did the round-1 audit of unit 63 find" --terms "exists containment segment rule normpath backslash PM_SCRUB range plant floor null sha unborn signer sweep CR"`
