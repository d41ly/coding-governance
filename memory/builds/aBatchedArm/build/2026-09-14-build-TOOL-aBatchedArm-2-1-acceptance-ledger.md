# TOOL-aBatchedArm-2 — acceptance ledger

**Serves:** journal TOOL-aBatchedArm-2

One pass under the two owner rulings — 2026-09-13 (no self-test per step) and 2026-09-14 (no gate
until every unit of the build is built). This unit's product is a STATIC linter: one `awk` pass over
one text file, seconds, no subprocess per group, no suite executed. So this pass ran the linter over
the tracked suite and over scratch copies with planted violations, and ran the linter's own
`.test.sh`, which is a handful of such runs — the same class as the static scans the earlier units
observed with. What it did NOT run: `check-unattended.test.sh` in any mode or shard, the bar,
`run-unattended-gates.sh`. What else it ran, because each executes no suite and costs seconds:
`bash -n` over both `.sh` files; `bash tools/check-install-prefix.sh`; `bash tools/check-line-length.sh`;
`python tools/lexicon/lexicon.py` before and after (offenders 987 both times, so the two new files add
none); `bash tools/run-gates/run-selftests.sh --check` and `--list --kit tools/unattended`;
`bash tools/check-testsuite-counts.sh`; `python tools/govkit/govkit.py selfcheck`;
`bash skills/session-kickoff/manifest-check.sh`; `bash tools/check-dead-paths.sh`;
`python tools/check-kit-placeholders.py`; `python tools/check-spec-tokens.py`;
`bash tools/unattended/adopt-unattended.sh --check`; `python tools/memory-tree/gen_build_index.py
--check-format`; and the record gates the pre-commit hook runs. All green at the closing commit.

## What the pass built

- **S1–S4 — `check-arms-groups.sh`**, beside the suite it grades. The delimiter set is RESOLVED
  from the file: every function whose body performs a hard reset (`git reset --hard`) or calls one
  that does, closed over callers to a fixpoint, plus every `if in_shard k` seam; an empty resolution
  REFUSES. Function bodies are brace-balanced over lines stripped of quoted strings, `${…}`
  expansions and comment tails, and every line of a body is skipped. Groups are cut at each
  boundary; inside a group the linter reads each `hit`/`miss`/`same` call with its helper name and
  its text (the last quoted argument of a `hit`/`miss`, the label of a `same`), each `emitted` call
  (counting the `"?"` sentinel), and each `NAME=$(… run)` capture with optional env-prefix
  assignments. Rule A reds a `miss` or `same` inside a group carrying an `emitted` call; rule B reds
  a text carried by two arms in one group, naming every line; rule C reds a capture assigned to a
  name other than `out`. The header states what is not graded (adequacy, the `emitted` set, the
  checker, inline `n=$((n+1))` arms, function bodies, comments; existing violations reported and
  never waived), and the liveness line prints boundaries, seams, groups, groups with arms, arms,
  batched groups and sentinels; zero groups or zero arms REFUSES with exit 2.
- **S5 — the leg row.** `tools/gate-legs.json` gains `unattended arms-groups selftest`
  (`bash tools/unattended/check-arms-groups.test.sh`, `chunk = selftests`, `subject = kit`, guard
  `tools/unattended/`, ceiling 300). The manifest's own gates demanded three carriers the brief did
  not list: a `[[gate_leg]]` claim in `tools/unattended/kit.toml` (govkit selfcheck reds a manifest
  leg no descriptor claims), a row in `tools/govkit/subject-pins.tsv` (the subject ratchet reds an
  unpinned leg), and a `last-audit` re-stamp of `memory/guides/SESSION-KICKOFF.md` (the manifest is
  a watched file; sha unchanged at the merge-base `fdd754bf`). `tools/run-gates/selftest-budgets.txt`
  gains an argv-EMPTY row, so the budget file carries no new path literal and
  `tools/install-prefix-carried.txt` is untouched: `60` seconds, floored — the suite measured 11 s
  wall (2 s user) on node a while another session held the box. The kit descriptor's `include` list
  names the new test file, and `run-selftests.sh --list --kit tools/unattended` now prints 15 rows.
- **The `.test.sh`**, 35 assertions, `FLOOR_ASSERTIONS=35`, the classic count shape
  `check-testsuite-counts.sh` grades. Its own failing case was observed: with rule A's condition
  changed to `NE[q] > 99` in a scratch copy of the linter, the suite printed four `FAIL` lines
  naming AC1 and exited 1.

## The linter over the tracked suite — the starting figures, pasted from its own run

Suite at `025c76c0` (its last change), linted at the closing commit:

```
check-arms-groups: does NOT grade adequacy, the emitted set, the checker, inline arms, function bodies or comments — linkage only (rules A, B, C; header above)
check-arms-groups: delimiter set resolved from the file: reset_tree anchor_break anchor_restore wreset seed_ros (5 helper(s), root = git reset --hard, closed over callers) plus every `if in_shard` seam
check-arms-groups: boundaries 318 (8 seams) · groups 318 · with arms 257 · arms 378 · batched 14 · sentinels 14
RED rule C · group at line 613 · line 614: capture `_f1_clean` is not this group's own `out` — a baseline read from another name is poisoned
RED rule B · group at line 716 · lines 721 727: 2 arms carry one text "a run-state file's generated markers are malformed"
RED rule B · group at line 1365 · lines 1368 1386: 2 arms carry one text "the recorded BASE equals HEAD at a phase that claims work was done, so the run authored every byte an authorization comparison would read"
RED rule B · group at line 1365 · lines 1373 1383: 2 arms carry one text "the recorded BASE equals HEAD at a phase that claims work was done"
RED rule B · group at line 1394 · lines 1402 1410 1417: 3 arms carry one text "a record claims LANDED with a witness that is not an ancestor of the anchor"
check-arms-groups: RED — 5 finding(s) · rule A 0 · rule B 4 · rule C 1
```

Exit 1. **Starting figures: rule A 0 · rule B 4 (three groups) · rule C 1.** Read, not waived:

- The rule-C hit is the `_f1_clean=$(run)` equality baseline the brief and rev-3 §9 named — a solo
  block whose capture two later groups compare against. `TOOL-aBatchedArm-1` S3 keeps it as is.
- The four rule-B hits are three SOLO groups that mutate one tree in sequence and re-assert one text
  after each mutation (a `hit` then a `miss` on one sentence at 721/727; a `hit`, two `miss` and a
  `for` loop at 1368–1386; a `hit` and three `miss` at 1402–1417). Under the rule as written —
  identical text, one group — they are hits; whether each re-assertion after a further mutation is a
  second arm or a second answer is a reader's question the header disclaims. None sits in a batched
  group. They are recorded here as the figure this linter starts from, per §3.
- The independent cross-check: an `awk` over the regions counting lines whose first `;`/`&&`/`||`
  segment leads with one of the five resolved names, plus the eight seams, also reads 318; and the
  only such lines outside the regions are the five definitions themselves, inside function bodies.
  Arms 378 = the 376 column-0 `hit`/`miss`/`same` lines plus the two indented ones (the `for _hijack`
  loop's `same`, the `for ph` loop's `hit`) that a column-0 grep misses.

## The self-test, verbatim

```
     tracked verdict (reported, not graded): check-arms-groups: RED — 5 finding(s) · rule A 0 · rule B 4 · rule C 1 · exit 1
ok   T0 the header names what the linter does NOT grade (AC5)
ok   T0 the delimiter set is resolved from the file and names reset_tree
ok   T0 the liveness line reports the boundary and group counts (S4)
ok   T0 the tracked suite parses into groups (318)
ok   T0 the region seams are boundaries (8)
ok   T0 the tracked run is a verdict (exit 1), not a refusal
ok   T0 a run with findings or a green one never prints REFUSED
     starting figures over the tracked suite: rule A 0 · rule B 4 · rule C 1
ok   AC1 a miss inside a batched group is RED
ok   AC1 exactly one rule-A finding is added
ok   AC1 the finding names the arm's line, the helper and rule A
ok   AC1 the finding names the planted line
ok   AC1 a same inside a batched group is rule A too
ok   AC1 a miss inside a solo group adds no rule-A finding
ok   AC2 a duplicated assertion text in one group is RED
ok   AC2 exactly one rule-B finding is added
ok   AC2 the finding names both line numbers
ok   AC3 a capture under a foreign name is RED
ok   AC3 exactly one rule-C finding is added
ok   AC3 the finding names the capture, its line and rule C
ok   AC3 the finding names the planted line and name
ok   AC3 a capture into the group's own out adds no rule-C finding
ok   AC4 zero groups exits 2
ok   AC4 zero groups says it graded nothing
ok   AC4 zero groups never prints GREEN
ok   AC4 an empty delimiter set exits 2
ok   AC4 an empty delimiter set is named as the refusal
ok   AC4 an empty delimiter set never prints GREEN
ok   AC4 a missing file exits 2
ok   AC4 a missing file is refused by name
ok   GREEN a clean file exits 0
ok   GREEN a clean file prints GREEN with its counts
ok   GREEN the batched group and its non-sentinel set are counted
ok   DELIM a planted hard-reset helper joins the resolved set
ok   DELIM a helper that calls it joins the set transitively
ok   DELIM the wrapper's call opens a new group, so the control after it is not rule A
PASS (35 assertions)
```

The plants are one line inserted after the first `emitted` call of the tracked suite (line 946 at
`025c76c0`, so every planted line is 947), each into its own scratch copy, each copy discarded; the
expected counts are the tracked run's figures plus exactly one, so no starting figure is typed into
the test. The tracked verdict is PRINTED and never graded by the suite — rev-3 §9 (6) says why.

**Evidences:** TOOL-aBatchedArm-2
- AC1 — `check-arms-groups.sh` — OBSERVED: a `miss "$out" "…"` planted after the first `emitted`
  call (line 947 of a scratch copy) reds with exit 1 and one added line `RED rule A · group at line
  941 · line 947: miss …`; a planted `same` reds the same way; the same `miss` planted after the first
  solo `reset_tree` adds no rule-A finding. Staged and observed RED on the copies before the leg row
  was written; the copies were discarded.
- AC2 — `check-arms-groups.sh` — OBSERVED: the `hit` at line 947 duplicated at 948 in a scratch copy
  reds with exit 1 and one added line `RED rule B · group at line 941 · lines 947 948: 2 arms carry
  one text …`, both line numbers named.
- AC3 — `check-arms-groups.sh` — OBSERVED: `_foreign=$(GOV_UNATTENDED_REPORT=1 run)` planted at
  line 947 reds with exit 1 and one added line `RED rule C · group at line 941 · line 947: capture
  _foreign is not this group's own out …`; `out=$(GOV_UNATTENDED_REPORT=1 run)` planted there
  adds none. The rule grades the ASSIGNMENT site, as S3 and the rules table say; the live
  `_f1_clean` instance at line 614 is the one pre-existing hit, pasted above and not waived.
- AC4 — `check-arms-groups.sh` — OBSERVED: a file holding only a reset helper's definition exits 2
  with `REFUSED — parsed 0 group(s) and 0 arm(s), so it graded nothing; this is not a clean
  verdict`; a file whose only helper performs no hard reset exits 2 naming the EMPTY delimiter set;
  a missing path exits 2; none prints `GREEN`.
- AC5 — `check-arms-groups.sh` — OBSERVED: over the tracked suite the second output line reads
  `does NOT grade adequacy, the emitted set, the checker, inline arms, function bodies or comments —
  linkage only (rules A, B, C; header above)`, and the file's own header enumerates each gap.
- AC6 — amended rev-3 — NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate
  pass by `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, whose manifest-derived
  leg list must carry `unattended arms-groups selftest` and report its verdict (green at this
  commit, by the run above). Red when the leg is absent from that list or reports no verdict. Static
  halves observed now: `run-selftests.sh --check` resolves the row, `--list --kit tools/unattended`
  prints it, `govkit selfcheck` finds it claimed and pinned, `check-testsuite-counts.sh` accepts the
  suite's count shape.
