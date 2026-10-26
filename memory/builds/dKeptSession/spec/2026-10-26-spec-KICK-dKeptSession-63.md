# KICK-dKeptSession-63 — the round-3 promotions' audit's 26 minor findings, closed after every unit they land on is built

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 34 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-64 |
| [2026-10-26-build-KICK-dKeptSession-63-deviation-631.md](../build/2026-10-26-build-KICK-dKeptSession-63-deviation-631.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-63-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-63-spec-audit.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's six round-3 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-57-spec-audit.md`)
confirmed 17 findings at MEDIUM and 9 at LOW, with no blocker and no high. BUILD-METHOD M4 promotes
them into one batch, and this is it. Each finding is its own §2 item, named by report id beside its
report item:

- MEDIUM: ids 4, 10 and 24 (M1), 2 and 20 (M2), 3 (M3), 1 (M4), 11 (M5), 13 (M6), 12 (M7), 14
  (M8), 15 (M9), 18 (M10), 21 (M11), 25 (M12), 26 (M13), 27 (M14);
- LOW: ids 5 (L1), 7 (L2), 8 (L3), 9 (L4), 19 (L5), 22 (L6), 23 (L7), 30 (L8), 31 (L9).

Two pairs are one defect at two grades: id 19 is id 3's at LOW, and id 31 is id 11's at LOW. Each
pair takes two items, one edit closing both. The minors land on six units, 57 to 62, so this unit
is one write set and takes the order past every unit of the build (order 34): each item amends code
or a record its unit has built. Where an item supersedes a sibling spec's text, it does so by name,
and that unit's acceptance ledger answers the superseded text (AC27).

## 2. Scope (IN)

- **S1** — id 4, M1. The `# >>> files_touched_py` block of `KICK-dKeptSession-62` S22 also holds
  `CITE_TAIL` (`tools/check-spec-tokens.py:288`), which `check_path_shaped` reads at `:1135`. The
  rule is the class: the block holds every module-level name its functions read, other than a
  builtin or a module both hosts import. Observed by AC1.
- **S2** — id 10, M1. `KICK-dKeptSession-62` §4 Evidence's line list for `check-spec-tokens.py` and
  §5's "seven definitions" read as eight, `CITE_TAIL` at `:288` among them, and the block in
  `tools/memory-tree/gen_build_index.py` defines it once, inside the markers. Observed by AC2 and
  AC27.
- **S3** — id 24, M1. `KICK-dKeptSession-62` AC20's byte parity gains a run: the copy in
  `gen_build_index.py`, imported alone, gives the canonical's output over one spec's Files touched.
  Observed by AC3.
- **S4** — id 2, M2. THE RULE in `tools/policy/README.md`, as `KICK-dKeptSession-60` S1 writes it,
  is superseded by name: a repository-relative input joins `LEGACY_INPUTS` in `policy.py` and
  `MIRROR_LEGACY_INPUTS` in `policy-mirror.js`; a kit-relative input joins `derive_mirror_inputs` and
  `MIRROR_KIT_INPUTS`; and `mirror-input-parity` reds either pair apart. Observed by AC4.
- **S5** — id 20, M2. The comment above `LEGACY_INPUTS` in `tools/policy/policy.py`, which
  `KICK-dKeptSession-60` S2 points at THE RULE, names the tuple's JS copy `MIRROR_LEGACY_INPUTS`
  beside that pointer. Observed by AC5.
- **S6** — id 3, M3. The signature is `derive_mail_chain(rows, chain)` in
  `tools/loop/loop_transition.py`, `chain` required and with no default. Its callers are
  `write_consumed_acks`, which passes S11's sent rows of the parent, and unit 53's selftest case
  (S22). `KICK-dKeptSession-61` S2 and `KICK-dKeptSession-53` AC2 read as this item. Observed by
  AC6.
- **S7** — id 1, M4. The chain read gets a case in `tools/unattended/unattended.test.sh`, which a
  selftest leg runs when `tools/unattended/unattended.sh` changes. It reads S11's `--mail read
  <parent> --cached --sent` over `KICK-dKeptSession-61`'s two-dependent plant, and `FLOOR_ASSERTIONS`
  rises by the case's count. At the close the main loop stages a break that edits only
  `read_mailbox`'s awk in a scratch copy and observes the case red. Observed by AC7.
- **S8** — id 11, M5. `KICK-dKeptSession-59`'s `mirror-input-parity` finds each JS list by its
  declaration, `^(?:const|let|var)\s+MIRROR_KIT_INPUTS\s*=\s*(\[[^\]]*\])` under `re.M`, so a line of
  `policy-mirror.js`'s header comment that spells the list is never the one graded. The same anchor
  reads `MIRROR_LEGACY_INPUTS`. Observed by AC8.
- **S9** — id 13, M6. `KICK-dKeptSession-62` S1's population is derived, not listed: at this unit's
  pass, `python tools/check-spec-tokens.py --legs-for` runs over every unit's `### Files touched
  (estimate)`, and each unit whose paths trip `policy fixtures` or `loop selftest` gets one ledger
  line by `KICK-dKeptSession-57` S3's rule as S17 states it. At the least that is units 58, 59 and 60
  for `policy fixtures` and unit 61 for `loop selftest`. This unit's ledger records the derived
  population. Observed by AC9.
- **S10** — id 12, M7. `KICK-dKeptSession-60` AC1 is superseded by name: it reads THE RULE's
  paragraph, from `THE RULE:` to the next blank line, joined into one line, and never one physical
  line. AC4 is that read. Observed by AC10 and AC27.
- **S11** — id 14, M8. The one reader takes the chain read. `read_mailbox <who>
  soft|strict|cache [sent]` in `tools/unattended/unattended.sh` gains the `cache` mode, which runs
  no fetch and no `add_feed_sightings`, and the `sent` selection, which prints every row on
  `refs/gov/remote/mail/<who>/*` whatever its `to`. The collapse rule (`KICK-dKeptSession-5` S6) and
  the `seq`, `after` and `content-key` columns (`KICK-dKeptSession-27` S4) hold unchanged, because
  the same `git log` and the same `awk` print both selections. The verb is `--mail read <slug>
  --cached --sent`. `KICK-dKeptSession-61` S1's `read_mail_chain` and `--mail chain` are superseded
  by name and never minted. Observed by AC11.
- **S12** — id 15, M9. The one mail writer takes the chain. `write_mail_ref <ref> <tip read>
  <message> [<message> ...]` builds one `build_gov_commit` per message, each parented on the one
  before and the first on `<tip read>`, and lands the last with one `write_gov_ref`. Message k's tip
  read, for `KICK-dKeptSession-27` S1's `seq`, is the chain's commit k-1, so the k-th ack's `seq` is
  the tip's depth plus k. `KICK-dKeptSession-62` §4's ack-chain sketch, which calls `write_gov_ref`
  itself, reads as this item. Observed by AC12.
- **S13** — id 18, M10. The reconcile step. The pass that reconciles this build's branch onto a
  base whose `tools/gate-legs.json` declares `policy fixtures` adds that name to the backtick leg
  line of every non-terminal spec of this build whose Files touched trips its guard. Each edit is a
  rev bump with its §9 line. The specs are 58, 59, 60, 62 and this one at the least, and every
  sibling the guards join names. This unit's pass re-checks the step on its own tree. Observed by
  AC13.
- **S14** — id 21, M11. `KICK-dKeptSession-62` S26's environment arm takes its population from the
  import graph: every `tools/runlog/` module that `runlog.py` or `selftest.py` imports, which is
  `extract`, `model`, `prose`, `record` and `runlog_lib` at this base. `derive_kit_imports` derives it
  by `ast`. `GOV_REMOTE` and `GOV_DEFAULT_BRANCH`, which `model.py` reads at `:652` and `:673`, are
  unset by `build_arm_env` beside the `GIT_*` scrub. Observed by AC14.
- **S15** — id 25, M12. The batched `--mail ack <slug> [<id> ...]` dedupes its ids, keeping the
  first of each. Each id passes `KICK-dKeptSession-5` S8's addressed-to check, and its ack passes
  S5's `derive_message_id` and `check_mail_duplicate`, before any commit is built. One refusal
  refuses the batch with exit 2 and lands nothing. An id already acked is skipped and named on
  stderr as `mail — already acked <id>`. An empty list exits 0 and writes nothing. Observed by
  AC15.
- **S16** — id 26, M13. A chained landing appends one feed line per chained commit, oldest first,
  each carrying its own commit, so `KICK-dKeptSession-23` S1's one line per landed write holds per
  commit and `read_first_seen` prints a time for every ack on the writing node. The appender is
  `write_gov_ref`'s success exit, per §8 F1, and `write_mail_ref` adds no call of its own. Observed by
  AC16.
- **S17** — id 27, M14. `KICK-dKeptSession-57` S3's ledger line records the query's exit status and
  its whole output. A refusal, an `UNEVALUATED` row or a `(not tracked at HEAD)` path writes a line
  opening `GAP —` with that output, never a leg list. A line names `loop selftest` only when
  `tools/gate-legs.json` at that pass carries the leg; otherwise it opens `NOT RUN —` with the
  reason. `KICK-dKeptSession-62` S1 takes the same rule. Observed by AC17.
- **S18** — id 5, L1. `KICK-dKeptSession-62` AC25 first asserts its range is not empty: it opens
  with `def derive_context_window` and holds more than one line. Only then is it grepped for
  `expanduser|\.claude`. Observed by AC18.
- **S19** — id 7, L2. `KICK-dKeptSession-58` S3's answer is read: unit 54's ledger answers its S2
  and AC2 by `KICK-dKeptSession-58`. Observed by AC19.
- **S20** — id 8, L3. `KICK-dKeptSession-61` S3's answer is read: unit 53's ledger answers its S1's
  "over one parent's `read_mailbox` rows" by `KICK-dKeptSession-61`. Observed by AC20.
- **S21** — id 9, L4. `KICK-dKeptSession-62` S24's widened parity is `{derive_kit_rel(n) for n in
  MIRROR_KIT_INPUTS} | set(MIRROR_LEGACY_INPUTS) == set(derive_mirror_inputs())`, both JS literals
  read by S8's anchor, and a literal that is absent or does not parse reds the case. The legacy names
  never pass through `derive_kit_rel`. Observed by AC21.
- **S22** — id 19, L5. Unit 53's selftest case calls `derive_mail_chain(rows, chain)` in this unit's
  `tools/loop/selftest.py` edit, with the parent's sent rows as `chain`. `KICK-dKeptSession-61` §4's
  "`derive_mail_chain` and its caller" reads as both callers S6 names. Observed by AC22.
- **S23** — id 22, L6. `KICK-dKeptSession-62` S19 states that `measure_tree` and
  `measure_ready_tree`, which read `derive_main_transcripts` (`KICK-dKeptSession-56` S21), count a
  linked transcript out too. The docstring of `derive_main_transcripts` names all three callers.
  Observed by AC23.
- **S24** — id 23, L7. `KICK-dKeptSession-62` S31's reword covers the build-order verb comment at
  `tools/memory-tree/gen_build_index.py:202-203` and the dossier line
  `memory/map/features/build-readme-surface.md:109`, which is authored. Each says that units sharing
  an `order` value are candidates for one parallel group. Observed by AC24.
- **S25** — id 30, L8. `tools/lib/resolve-python.test.sh` holds one marker lead, `MARKER_LEAD`,
  matching `# ` or `// `. All three sites use it: the extractor `blk` (`:213`), the population grep
  (`:218`) and the `nblk` count (`:224`). `KICK-dKeptSession-62` S20 reads as this item. Observed by
  AC25.
- **S26** — id 31, L9. S8's anchored read takes `re.findall`, and the case reds unless each JS list
  has exactly one declaration. Observed by AC26.

## 3. Non-goals (OUT)

- Rewording sibling specs: each superseded text is named here and answered in its unit's ledger.
- The report's left-shift checklist entries and hygiene arms: no clause of this build names the
  bug-class checklist, and each arm is a separate gate, so a separate unit by M2.
- A free-name arm over every parity block: S1 is checked by AC1's probe over the one block it moves.
- Renumbering any order.

### Edges

- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox`'s modes and selection, `write_mail_ref`'s one-message signature and `--mail ack`, which S11, S12 and S15 extend (ids 14, 15, 25)
- **consumes-from** `KICK-dKeptSession-23` — S1's one feed line per landed write, which S16 holds per chained commit (id 26)
- **consumes-from** `KICK-dKeptSession-27` — S1's `seq` from the tip read, which S12 derives per chained message (id 15)
- **consumes-from** `KICK-dKeptSession-53` — `derive_mail_chain`'s AC2, its selftest arm and S1's ledger answer, which S6, S20 and S22 move to the two-argument form and read (ids 3, 8, 19)
- **consumes-from** `KICK-dKeptSession-57` — S3's ledger rule, whose population S9 derives and whose non-success outputs S17 records (ids 13, 27)
- **consumes-from** `KICK-dKeptSession-58` — S3's ledger answer for unit 54 and §7's leg line, which S19 reads and S13 completes (ids 7, 18)
- **consumes-from** `KICK-dKeptSession-59` — the `mirror-input-parity` case's literal read and §7's leg line, which S8 and S26 anchor and count and S13 completes (ids 11, 31, 18)
- **consumes-from** `KICK-dKeptSession-60` — S1's rule, AC1 and §7's leg line, which S4 widens, S10 reads by paragraph and S13 completes (ids 2, 12, 18)
- **consumes-from** `KICK-dKeptSession-61` — S1's chain read, S2's signature and §7's arm, which S11, S6, S7 and S22 settle on the one reader (ids 14, 3, 1, 19)
- **consumes-from** `KICK-dKeptSession-62` — S1, S15, S19, S20, S22, S24, S26, S31, AC20, AC25 and §7's leg line, S1 to S5, S8, S9, S12 to S18, S21 and S23 to S26 (ids 4, 10, 24, 2, 20, 11, 13, 15, 18, 21, 25, 26, 27, 5, 9, 22, 23, 30, 31)
- **consumes-from** external — TOOL-dPlacedRequest-13 S3's `write_gov_ref` success exit appending one feed line per first-parent commit it landed, the ask §8 F1 files
- **hands-off** external — the ask row for dPlacedRequest that S16 needs, filed in `memory/builds/dPlacedRequest/BACKLOG.md` (§8 F1)
- **hands-off** `KICK-dKeptSession-64` — the batched `--mail ack`, the `cache` and `sent` read, S9's population, S13's and S17's rules, S14's scrub, S24's reword, S25's marker lead and §8 F1's ask row, which the batch amends (all 20 ids of the round-4 minors batch's audit)

## 4. Design

### Evidence

Each item's evidence is the audit's appendix row for its id, re-read for this spec on 2026-10-26.
The claims re-verified at this base: `tools/check-spec-tokens.py` defines `CITE_TAIL` at `:288` and
reads it at `:1135` and `:1148`, `extract_files_touched` sits at `:530` and `check_path_shaped` at
`:1122`, and `gen_build_index.py` spells no `CITE_TAIL`; `print_legs_for` (`:637-674`) exits 2 with
`legs-for: REFUSING` when no path given is tracked, exits 1 when the manifest is absent or does not
parse, and prints `(not tracked at HEAD)`, `UNEVALUATED` and `no guarded leg` rows;
`resolve-python.test.sh` anchors `blk` (`:213`), the copy grep (`:218`) and `nblk` (`:224`) on `^#
>>> `; `model.py` reads `GOV_REMOTE` (`:652`) and `GOV_DEFAULT_BRANCH` (`:673`), and
`tools/run-gates/post-merge.sh:86` exports `GOV_REMOTE`; `runlog.py` imports `extract`, `model`,
`prose`, `record` and `runlog_lib` (`:67-71`); `extract.py` applies `_check_inside` (`:176`) in
`scan_preflights` only, while `measure_tree` (`:1131`) and `measure_ready_tree` (`:1204`) glob alone;
`gen_build_index.py:202-203` and `memory/map/features/build-readme-surface.md:109` say a shared
order is the parallel group. dGroundRules' files are read at `3c8c4718a`: `tools/policy/README.md`
holds THE RULE wrapped across `:290-291`, `policy.py:810-813` holds the comment and `LEGACY_INPUTS
= (LEGACY_FANOUT,)`, and `policy-mirror.js` opens with a 33-line header comment (`:2-34`) holding code-like lines.
TOOL-dPlacedRequest-13 S6's `check_feed` compares a ref's events to its chain in order, and S3
appends only the landed tip.

### The two selections of the one reader

| Call | Fetch | Rows printed |
|---|---|---|
| `read_mailbox <who> soft` | one bounded fetch, soft | every cached row addressed to `<who>` |
| `read_mailbox <who> strict` | one bounded fetch, strict | the same |
| `read_mailbox <who> cache` | none | the same, from the cache |
| `read_mailbox <slug> cache sent` | none | every row on `refs/gov/remote/mail/<slug>/*` |

### The ack chain

```
--mail ack <slug> a b             tip T at depth n
  check a, check b                -> any refusal: exit 2, nothing built
  write_mail_ref <ref> T <ack a> <ack b>
    c_a := build_gov_commit T   <ack a, seq n+1>
    c_b := build_gov_commit c_a <ack b, seq n+2>
    write_gov_ref <ref> T c_b     -> feed: c_a, then c_b (F1), or nothing on rc 1 or 2
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `cache` | `read_mailbox` mode | none |
| `sent` | `read_mailbox` selection | none |
| `--cached`, `--sent` | `--mail read` flags | none |
| `derive_kit_imports` | function, `tools/runlog/selftest.py` | `derive`, asked at the pass |
| `MARKER_LEAD` | variable, `tools/lib/resolve-python.test.sh` | none |

### Migration

None: no stored record changes shape. S12's acks are the records unit 5 already writes, and S16's
feed lines are the lines TOOL-dPlacedRequest-13 S1 defines.

### Files touched (estimate)

- `tools/check-spec-tokens.py`, `tools/memory-tree/gen_build_index.py`: S1 to S3, S24
- `tools/lib/resolve-python.test.sh`: S25
- `tools/policy/README.md`, `tools/policy/policy.py`: S4, S5, the text only
- `tools/policy/check_policy.py`: S8, S21, S26
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`,
  `tools/unattended/VERBS.template.md`: S7, S11, S12, S15, S16
- `tools/loop/loop_transition.py`, `tools/loop/selftest.py`: S6, S22
- `tools/runlog/extract.py`, `tools/runlog/selftest.py`: S14, S23
- `memory/map/features/build-readme-surface.md`: S24
- `memory/builds/dKeptSession/build/`: the ledger lines of S9, S17 and AC27
- `memory/builds/dKeptSession/spec/`: S13's leg lines, at reconcile
- `memory/builds/dPlacedRequest/BACKLOG.md`: §8 F1's ask row

### Alternatives rejected

- **Two batches.** S9 and S17 write ledger lines of units in both the policy set and the mail set,
  and AC27 reads ledgers of both, so the two halves' write sets cannot be written down as disjoint
  by M6's clauses.
- **A separate `read_mail_chain` beside `read_mailbox`, for S11.** It is a second parse of one ref
  set, the two-reader drift the one reader (I20) exists to prevent.
- **Each id posted by its own `write_mail_ref`, for S16.** A lost update after the first leaves
  that ack landed and the transition refused, the state `KICK-dKeptSession-55` AC2 names red.

## 5. Production-readiness checklist

- security — S15 checks every id before any commit; S11's `cache` mode writes nothing and fetches
  nothing.
- perf / scale — S11 adds no fetch; S16 appends N lines for N acks, one lock each.
- error / empty / loading states — S15's empty list exits 0 and writes nothing; S17 writes a `GAP`
  or `NOT RUN` line for every non-success query; S18 and S26 red an empty range or a missing literal.
- observability — S15 names each skipped id; S17's lines carry the query's exit and output.
- risks — S11 and S12 change two signatures of unit 5's code; every caller is a unit of this build,
  named in S6, S11 and S22.
- testing — the criteria of §6 and the arms of §7.
- migration — §4.
- user docs — `tools/unattended/VERBS.template.md`'s `--mail` section names `--cached --sent` and a
  batched `--mail ack`, S11 and S15.

## 6. Acceptance criteria

Fixtures are each repaired unit's own, named by that unit's spec, under `%TEMP%`.

- **AC1** — When a probe extracts the `files_touched_py` block of `tools/check-spec-tokens.py` and
  lists, by `ast`, every name its functions load that the block does not bind and that is neither a
  builtin nor a module both hosts import, it prints nothing.
  Red when: the block leaves out `CITE_TAIL`, and the probe prints it.
- **AC2** — When `awk '/^# >>> files_touched_py/,/^# <<< files_touched_py/'` runs over
  `tools/check-spec-tokens.py` and over `tools/memory-tree/gen_build_index.py`, each range holds one
  `CITE_TAIL = ` line, and `grep -c '^CITE_TAIL = ' gen_build_index.py` prints `1`.
  Red when: the copy defines it outside the markers, where the parity row never compares it.
- **AC3** — When a probe imports `gen_build_index` alone and calls its `extract_files_touched` over
  this spec's text and the tracked file set, the result equals the canonical's in
  `check-spec-tokens.py`.
  Red when: the copy raises `NameError` on its first path-shaped token.
- **AC4** — When `awk '/THE RULE:/,/^$/' README.md | tr '\n' ' '` runs in `tools/policy/`, the
  joined paragraph names `LEGACY_INPUTS`, `MIRROR_LEGACY_INPUTS`, `derive_mirror_inputs`,
  `MIRROR_KIT_INPUTS` and `mirror-input-parity`.
  Red when: any one is absent, so the rule names one list where two move.
- **AC5** — When `grep -n "MIRROR_LEGACY_INPUTS" policy.py` runs in `tools/policy/`, it prints a
  line of the comment above `LEGACY_INPUTS`.
  Red when: the comment names the Python tuple alone.
- **AC6** — When `python -c "import inspect, loop_transition as t;
  print(inspect.signature(t.derive_mail_chain))"` runs in `tools/loop/`, it prints `(rows, chain)`,
  and a call with one argument raises `TypeError`.
  Red when: `chain` carries a default, so a caller leaving it out keeps the filtered-only placement.
- **AC7** — When `bash unattended.sh --mail read <parent> --cached --sent` runs in
  `KICK-dKeptSession-61`'s two-dependent repository, it prints four rows carrying `seq` and `after`,
  the rows to both dependents among them.
  Red when: a scratch copy of `unattended.sh` whose `read_mailbox` awk keeps the address filter
  prints two rows and the new case still passes.
- **AC8** — When `python check_policy.py --fixture mirror-input-parity` runs over a scratch kit whose
  `policy-mirror.js` header comment spells `MIRROR_KIT_INPUTS = ["presets.toml"]` while the declared
  list holds a second name, it reds naming that name.
  Red when: the case grades the comment's list and passes.
- **AC9** — When the ledgers of units 58, 59 and 60 are read at this unit's pass, each carries one
  line naming `policy fixtures`, unit 61's names `loop selftest`, and this unit's ledger lists the
  population `check-spec-tokens.py --legs-for` derived.
  Red when: a unit whose Files touched trips either leg's guard has no line.
- **AC10** — When AC4's `awk '/THE RULE:/,/^$/'` read runs over a scratch `README.md` whose rule
  wraps across three lines with all five names, it passes, and over one whose rule paragraph names
  `LEGACY_INPUTS` alone while `MIRROR_KIT_INPUTS` sits in the next paragraph, it reds.
  Red when: a one-line `grep` passes the second README or reds the first.
- **AC11** — When `--mail read dA` and `--mail read <parent> --cached --sent` run over that
  repository, the sent rows addressed to `dA` equal `dA`'s rows in `id`, `ref`, `seq` and `after`,
  and `grep -c "read_mail_chain" unattended.sh` prints `0`.
  Red when: a second parse prints the chain, so the two reads can differ.
- **AC12** — When `--mail ack <slug> <a> <b>` lands on a session ref at depth n, `--mail read` shows
  the two acks with `seq` n+1 and n+2, and every `write_gov_ref` line `grep -n` prints in
  `unattended.sh` outside `write_mail_ref`'s range takes a ref `derive_mail_ref` did not name.
  Red when: both acks carry n+1, or a second path writes a mail ref.
- **AC13** — When `grep -c '"policy fixtures"' tools/gate-legs.json` prints `1` at a reconciled tip,
  each non-terminal spec of this build for whose Files touched `--legs-for` prints `policy fixtures`
  carries it on its §7 leg line.
  Red when: a spec whose paths trip the guard lacks the name.
  figure: DERIVED, the population re-derived by `--legs-for` at the reconcile.
- **AC14** — When the runlog selftest's environment arm runs over a copy of `model.py` adding
  `os.environ.get("RUNLOG_PLANTED")`, it reds naming `RUNLOG_PLANTED`, and `build_arm_env` under
  `GOV_REMOTE=planted` returns an environment without `GOV_REMOTE`.
  Red when: a variable `model.py` reads reaches a case from the machine.
- **AC15** — When `--mail ack <slug> <a> <a>` runs, `--mail read` shows one ack of `<a>`; a second
  `--mail ack <slug> <a>` prints `mail — already acked <a>`; `--mail ack <slug>` exits 0; and a
  batch holding an id not addressed to `<slug>` exits 2. The session ref's tip, read by `git
  rev-parse`, moves only on the first call.
  Red when: a repeated id lands two records, or an empty or refused batch moves the tip.
- **AC16** — When a two-id `--mail ack` lands on the writing node, `read_first_seen` prints a time
  for both commits, and `bash unattended.sh --feed check` exits 0.
  Red when: the lower ack reads `-`, or the feed's events are out of chain order.
  fixture: TOOL-dPlacedRequest-13 built with §8 F1's ask; without it the item parks by M6.
- **AC17** — When S17's step runs over a unit whose Files touched is untracked at the pass, so
  `--legs-for` exits 2, that unit's ledger line opens `GAP —` and carries `exit 2` and the
  `legs-for: REFUSING` line. When `tools/gate-legs.json` carries no `loop selftest`, a line owing it
  opens `NOT RUN —`.
  Red when: a refused query writes a line that reads as clean.
- **AC18** — When `KICK-dKeptSession-62` AC25's range check runs over a copy of `extract.py` whose
  `def derive_context_window` is renamed, it reds on the empty range before any grep.
  Red when: an empty range prints `0` and passes.
- **AC19** — When `grep -n "KICK-dKeptSession-58"` runs over unit 54's acceptance ledger, it prints
  the answers to unit 54's S2 and AC2.
  Red when: the ledger still expects the whole row.
- **AC20** — When `grep -n "KICK-dKeptSession-61"` runs over unit 53's acceptance ledger, it prints
  the answer to unit 53's S1.
  Red when: the ledger still certifies the filtered-rows chain.
- **AC21** — When `python check_policy.py --fixture mirror-input-parity` runs, it passes with
  `.agent-cap.conf` unprefixed on `MIRROR_LEGACY_INPUTS`, and over a scratch kit whose
  `MIRROR_LEGACY_INPUTS` literal is absent it reds.
  Red when: the case prefixes a legacy name with the kit path, or an absent literal passes.
- **AC22** — When unit 53's AC2 probe runs as `derive_mail_chain(rows, chain)`, the chain the
  parent's sent rows, it answers that `s1`'s row precedes, and `grep -n "derive_mail_chain("
  tools/loop/selftest.py` prints no one-argument call.
  Red when: unit 53's case still calls the one-argument form.
- **AC23** — When `measure_tree` and `measure_ready_tree` run over `KICK-dKeptSession-62` AC17's
  fixture root, each counts the linked session out.
  Red when: a measure still counts a transcript the window scan refuses.
- **AC24** — When `grep -c '^# the parallel group' gen_build_index.py` runs in `tools/memory-tree/`,
  it prints `0`, and `git grep -n "the parallel group" -- tools/memory-tree/gen_build_index.py
  memory/map/features/build-readme-surface.md` prints nothing.
  Red when: either text still says a shared order is the parallel group.
  figure: PINNED, the first count is `1` at base, line 203, read 2026-10-26.
- **AC25** — When the inline-parity arm runs over a scratch tree whose `mail-notice.js` holds two
  `// >>> read_card_js` blocks, the second one byte off, it reds naming block 2 of 2, and
  `grep -c 'MARKER_LEAD' resolve-python.test.sh` prints at least `4`.
  Red when: `nblk` counts no `//` block, so the second copy is never compared.
- **AC26** — When `python check_policy.py --fixture mirror-input-parity` runs over a scratch
  `policy-mirror.js` declaring `MIRROR_KIT_INPUTS` twice, it reds naming the count; and over one
  declaring `MIRROR_LEGACY_INPUTS` nowhere, it reds the same way.
  Red when: the first declaration is graded and the second ignored.
- **AC27** — When `grep -n "KICK-dKeptSession-63"` runs over the acceptance ledgers of units 53, 57,
  60, 61 and 62, it prints the answers to each text superseded by name here: unit 53's AC2 and arm;
  unit 57's S3; unit 60's S1 and AC1; unit 61's S1, S2 and Inventory; and unit 62's S1, S15's
  sketch, S20, S22, S24, S26, AC20, AC25 and §4 Evidence.
  Red when: a superseded text has no answer.

## 7. Gates

`build-index selftest` · `format-guard self-test` · `memory-hygiene self-test` · `pre-push run-log line` · `recall floor` · `recall floor arms` · `run-gates run-log line` · `runlog selftest` · `tier2-review self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `spec-tokens self-test` · `unattended kit gate` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The policy kit's `policy fixtures` leg runs its cases once dGroundRules has landed it, and the loop
kit's `loop selftest` leg its cases once dDeclaredLoop has landed it; S13 adds the first to the
line above at reconcile.

New arm: tools/unattended/unattended.test.sh · covers AC7 AC11 AC12 AC15 AC16 · the two-dependent plant read sent and cached, a chained ack pair, a repeated and an empty ack list, staged red by a scratch `unattended.sh` whose `read_mailbox` awk keeps the address filter · `FLOOR_ASSERTIONS` and its shard floor rise by the arm's count, counted off the diff
New arm: tools/policy/check_policy.py · covers AC8 AC21 AC26 · a scratch `policy-mirror.js` with a header-comment literal, a doubled declaration and an absent legacy literal · none
New arm: tools/runlog/selftest.py · covers AC14 AC23 · a copy of `model.py` reading a planted variable, and a linked transcript under both measures · none
New arm: tools/loop/selftest.py · covers AC6 AC22 · unit 53's case in the two-argument form, staged red by a `derive_mail_chain` whose `chain` defaults to `rows` · none
New arm: tools/lib/resolve-python.test.sh · covers AC25 · a second `//` block one byte off · none

## 8. Open questions

- **F1 — Which code appends the feed lines of S16's chained commits, id 26?** Options: (a)
  `write_gov_ref`'s success exit, which knows `<tip read>` and the landed tip, appends one line per
  first-parent commit between them, oldest first, the tip last, through an ask filed for
  TOOL-dPlacedRequest-13 S3; (b) `write_mail_ref` appends the lower commits after `write_gov_ref`
  returns 0; (c) each ack landed by its own `write_mail_ref`. (b) puts the tip's line before its
  parent's, which `check_feed` (TOOL-dPlacedRequest-13 S6) reds as out of chain order. (c) loses
  the all-or-nothing landing `KICK-dKeptSession-55` AC2 requires. (a) meets AC16, covers every
  multi-commit governance-ref write in the one writer, and needs only the ask row the build-level
  rules allow outside this folder, filed at this unit's pass or earlier where a pass may write it.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the round-3 promotions' audit's minors batch.
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-64` mirrored, the other ends of
  the edges the round-4 minors batch's audit's disposal declared

## 10. Reuse audit

Every item extends the seam its repaired unit names, and the cross-cutting ones extend existing
mechanisms: `read_mailbox` and `write_mail_ref` (`KICK-dKeptSession-5` S2 and S6), the one reader
and the one mail writer, for S11, S12 and S15; the `PARITY_ROWS` arm of
`tools/lib/resolve-python.test.sh` (`:213-224`) for S25; `print_legs_for`
(`tools/check-spec-tokens.py:637`) for S9 and S17; `build_arm_env` and `DECOY_VARS`
(`tools/runlog/selftest.py:348`, `:1515-1520`) for S14; and TOOL-dPlacedRequest-13's
`write_gov_ref` exit for S16. `python tools/codebase-map/reuse_lookup.py "read every message one
build's sessions wrote without fetching"` ranked `read`, `read_text` and `build_commit` by name stem
only; no mail code exists at this base, so no existing seam in the tree fits beyond the sibling
specs' readers and writers, which are the seams extended.

Recall terms used: `python tools/memory-recall/query.py "how is a batch of minor findings closed
over units already built" --terms "promoted batch minors ledger superseded reader writer chain feed
parity marker anchor"`
