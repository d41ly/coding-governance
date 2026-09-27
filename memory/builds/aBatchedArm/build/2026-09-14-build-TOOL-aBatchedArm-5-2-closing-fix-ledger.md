# aBatchedArm — closing-fix ledger, rounds 1 and 2

**Serves:** journal TOOL-aBatchedArm-5 TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3

The fix pass for the round-1 closing diff review
(`../reviews/2026-09-14-review-TOOL-aBatchedArm-1-closing-diff-round1.md`), under the brief
`../prompts/2026-09-14-prompt-TOOL-aBatchedArm-5-closing-fix-brief.md`. Seven commits, one per
brief step, each followed by `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD`; one
direct timed run of the runner's self-test on a frozen clone; nothing the brief forbids was run.
Every `.sh` edit went through the Edit tool or binary-mode Python, and every edited file reads
`i/lf w/lf` under `git ls-files --eol` at each commit.

## What this pass ran, and what it did not

Ran: `python tools/lexicon/lexicon.py`; `python tools/codebase-map/gen_map.py --write` and
`test_codebase_map.py`; `bash tools/run-gates/run-selftests.sh --check` (and `--list --kit
tools/unattended`); `bash tools/check-install-prefix.sh`; `bash tools/check-line-length.sh`;
`bash -n` over every edited script; `python tools/memory-tree/gen_build_index.py --check`,
`--check-format` and `--write`; `python tools/run-gates/derive-ceilings.py --check`;
`bash tools/check-kit-versions.sh`; the new linter's self-test
`bash tools/unattended/check-arms-groups.test.sh` (twice, PASS 35) and the linter itself over the
tracked suite; `bash tools/lib/lib-selftest.test.sh` (PASS 17) after its one edit — not on the
brief's list, seconds long, the self-test of a file this pass changed, and not on the forbidden
list either; a scratch harness (the suite's own header and fixture builder, lines 1 to
`build_fixture build_repo`, plus only the arms under observation, plus `run_arms`) to observe each
new or fixed arm against the pre-fix runner and then the fixed one; and the ONE direct timed
`bash tools/run-gates/run-selftests.test.sh` on a `git clone --local` at
`C:/Users/daily-agent/AppData/Local/Temp/cgrst`, tip `f23b71e0`, with `run_in_background`, output
to a file, the wall from `date +%s` around the suite alone. `run-unattended-gates.sh --checks
--pooled` and `--checks --serial` were invoked once each AFTER the D10 refusal was in place: both
exit 2 before any check runs, which is the observation D10 asks for; the pre-fix behaviour was
not reproduced here because reproducing it runs the checks, and that is the gate pass's.

Not run: `check-unattended.test.sh` in any mode or shard, `unattended.test.sh`,
`adopt-unattended.test.sh`, `cross-component.test.sh`, `check-playbook.test.sh`, the bar,
`run-unattended-gates.sh` in any mode that executes anything.

## The commits

1. `cb1f4541` — closing fix 1: D1.
2. `d3000f70` — closing fix 2: D2.
3. `72f9586d` — closing fix 3: D5 and D6, with the manifest re-stamp.
4. `1f739769` — closing fix 4: D4, with the manifest re-stamp.
5. `214b7183` — closing fix 5: D3(b) and D7, with the manifest re-stamp.
6. `f23b71e0` — closing fix 6: D8, D10, D11, D12, with the manifest re-stamp.
7. `ff549e63` — closing fix 7: D3(a).
8. `f51eefa7` — closing fix 3 (cont.): the ceiling and budget re-declaration from the direct
   run, and this ledger.
9. The last commit — the runner's `say_out` helper (commit 5) led with a verb the lexicon table
   does not hold, so the final `python tools/lexicon/lexicon.py` read 985 over pin 984; renamed
   `print_outlog` (11 sites, an identifier only — every printed byte unchanged), the lexicon back
   at 984, the D3/D7 arms re-observed `ok` on the scratch harness, `--check` clean. It post-dates
   the direct run's tip `f23b71e0`; the reading stands because the rename changes no behaviour.
10. `b5c51c45` — the kickoff manifest's C9 maintenance-stall check tripped at the FULL check
    (11 non-merge watched commits since its body-change baseline, 5 before this pass, threshold
    ten). §B's runner line now front-loads GOV_NODE-is-a-registry-tag and the per-row output
    path, byte-neutral under the 25600 B cap; `last-body-change` advances to `37f879ff`; the
    full `manifest-check.sh` reads 0 FAILED.

The manifest ratchet fires on EVERY commit that stages `tools/run-gates/run-selftests.sh` (C5s
compares the staged stamp with HEAD's), not only the first, so commits 3 through 6 each re-stamp
`last-audit` at the merge-base `fdd754bf` with a delta line; the brief's "first commit" reading
was the smaller of two and the gate decided.

## Each defect, its commit, and the observation that closed it

- **D1** (commit 1) — `replay_landed_main` → `run_landed_replay`, `topo_capture` → `read_topo`,
  `emitted` → `check_emitted`: 3 + 10 + 18 sites across the suite (definitions, 14 sentinel
  calls, 3 `FAIL check_emitted:` texts, 3 comments), the linter's rule-A regex and header (5), the
  linter test's locator, refusal texts and clean fixture (5). `python tools/lexicon/lexicon.py`
  rc 0, `P1 verb graded=2096 offenders=984` over pin 984 — the pin was not re-declared. The
  linter over the tracked suite still reports `batched 14 · sentinels 14` and `RED — 5 finding(s)
  · rule A 0 · rule B 4 · rule C 1`, the by-design starting figure, so rule A still keys. The
  phrase `expected set not yet observed` is byte-unchanged. Spec prose keeps the old names as
  history. One trap on the way: Python `re.subn` processes `\t` in its replacement, so the first
  pass turned the awk regex's `[ \t]` into a literal TAB; caught by `cat -A`, fixed with a
  `bytes.replace`, and the committed line reads `/^[ \t]*check_emitted[ \t]/` by `git cat-file`.
- **D2** (commit 2) — `unattended arms-groups selftest` added to the `gate-legs` claim in
  `memory/map/features/unattended.md`; `gen_map.py --write` regenerated `inventories.json` and
  `MAP.md`; `test_codebase_map.py` rc 0. The claim put the dossier 25 B over hygiene check 6's
  20480 B cap — the pre-commit hook refused — so 29 B of prose in its remote-bound paragraph were
  trimmed (20476 B). The review's left-shift (a fourth registry in the unit-2 ledger template) is
  recorded here rather than by editing a closed unit's ledger: a new leg row lives in FOUR places
  — `tools/gate-legs.json`, the kit's `kit.toml`, `subject-pins.tsv`, and the map dossier's
  `gate-legs` claim — and the map test is the gate for the fourth.
- **D5** (commit 3) — the calibrate arm's subject wrapped in `( … )`. Scratch harness: the old
  string `FAIL … the subject recorded no status (runner exit 0)`; the wrapped one `ok` (the
  calibrate completes in about 8 s). Left-shift in `tools/lib/lib-selftest.sh`: when the capture
  exists and the runner's status is not 124/137, the verdict says `the subject exited the harness
  body (status N) … wrap it in ( … )`; observed on the old string; `lib-selftest.test.sh` PASS 17.
  The review's static arm (a subject ending in a bare `exit` outside parentheses) was NOT added:
  the harness diagnosis fires on the class whenever it happens and names it, which the static
  arm would only approximate.
- **D6** (commit 3) — the refusal prints `so the run would be killed before its` on one line
  again; both arms' wants (`would be killed before its`, `population is 400s (an evidence
  bound)`) occur verbatim in the source and read `ok` on the scratch harness. The review's
  left-shift (every rc-2 want verbatim in the runner) was run as a candidate over the real suite
  first: 14 hits, 7 misses — every miss an interpolated want such as `NO pooled reading under
  pooled@2x1 on node t` — so as stated it reds innocent arms and is NOT wired. The
  `arm-literal-strands-on-message-edit` gotcha already records the class.
- **D4** (commit 4) — the five suites print `  ($n assertions executed)` unconditionally before
  their `[ "$st" = 0 ] && echo "PASS …"`; the linter self-test shows both lines. The evidence
  header named none of them, so it changed only to gain the declaration below. The review's
  `--check` arm as stated ("every row not declared no-trailer") was run as a candidate over the
  whole declaration first: 34 of 69 rows print no trailer at all because they are not on the
  pooled route, so it would red innocent rows. Scoped instead to the rows under each
  `# pooled-kit:` the evidence header declares (`tools/unattended`, one line, the same shape as
  `no-trailer:`); the arm skips declared no-trailer rows, announces `graded NOTHING` with no
  pooled-kit, reds a pooled-kit selecting no row, and its header states what it does not check
  (a trailer behind any other guard, a trailer printed by a sourced file, reachability). Over the
  fixed tree `--check` prints `trailer arm graded 13 row(s) under pooled-kit tools/unattended (2
  declared no-trailer)`; on a `git clone --local` carrying the five pre-fix suites it exits 1
  naming exactly those five. Three arms in `run-selftests.test.sh`, each `ok` on the scratch
  harness. Known pair: the pooled population is now spelled twice — this declaration, and the
  `--kit tools/unattended` argument `run-unattended-gates.sh` passes; a `--pooled --kit` over an
  undeclared kit is still caught at run time by the calibrate's UNTRAILED verdict, and refusing
  it statically is a follow-up, not this pass.
- **D3(b)** (commit 5) — `SWEEP_NOBASELINE_RX='expected set not yet observed'`; a hit is
  UNTRAILED at calibrate and MISMATCH under `--pooled` whatever the triple says; each row's
  `$d/out` is copied to `<git-dir>/gate-logs/selftests/<row>.out` before any verdict is read and
  the path printed on every non-`ok` row. Arms (scratch harness, RED against the pre-fix runner
  then `ok`): the calibrate over two sentinel rows exits 1 naming the refusal with the evidence
  file byte-unchanged (pre-fix: rc 99, the file rewritten); `--pooled` over a seeded matching
  triple renders MISMATCH (pre-fix: rc 0, parity GREEN over the refusal); the kept file carries
  the `observed:` line and the row prints its path (pre-fix: rc 99, no file).
- **D7** (commit 5) — `sound=1`, cleared by the three post-loop checks; the writer runs only
  when sound, else `readings NOT written: this calibrate was unsound — <why>` and exit 1; the
  RED summary names that cause. Arm: a `suite-dirty` calibrate exits 1 with that line and the
  evidence file byte-unchanged (pre-fix: rc 99, the file rewritten).
- **D8** (commit 6) — the calibrate branch takes rc 124/137/143 as KILLED before the declared-nt
  clause; `killed` counted and named in the RED summary. Arm: a declared trailer-less
  `suite-stubborn.sh` (traps TERM, keeps sleeping) under `SELFTEST_WALL=3` is KILLed by
  `timeout -k 5` after the grace; pre-fix rc 99 (its row written at the kill's rc), fixed `ok`
  with the row's seed absent from the file.
- **D10** (commit 6) — `run-unattended-gates.sh` refuses `--checks` with a mode, naming both.
  Observed directly: rc 2 for `--pooled` and for `--serial`, nothing run. Arm in
  `cross-component.test.sh` before its fixture (`FLOOR_ASSERTIONS` 19 → 21); that suite is the
  gate pass's to run.
- **D11** (commit 6) — `resolve_node_tag` validates `GOV_NODE` against `read_registry_tags`, the
  table `--check` enforces; refused by name, rc 2. Arm: `GOV_NODE=zz … --pooled --calibrate`
  pre-fix rc 99 (a row under node `zz` written), fixed `ok` with the file unchanged.
- **D12** (commit 6) — `unset GOV_NODE` at the top of `run-selftests.test.sh`. With `GOV_NODE=a`
  inherited, the calibrate arm reads `ok` on the scratch harness; the pre-fix 46-arm red is the
  review's own observation.
- **D3(a)** (commit 7) — the landing order in `RUN.md` (`## Landing order`) and in unit 5's S5
  as step (0) with a rev-8 §9 line; the build README's generated region re-rendered. The shard
  runs come first, the paste second, the calibrate only after no `FAIL check_emitted:` line
  remains.
- **D9** — see "The direct run": the `walled 1` arm's outcome in the one run decides whether its
  want is narrowed.
- **D13** — NOT closed here, by the brief: shard 8's `DERIVED, not measured` reading is
  re-measured at the direct shard runs the landing order owes, and `--rank` refuses until then.
  `RUN.md`'s Landing order block says so.

`SELFTEST_FLOOR` in `run-selftests.test.sh`: 99 → 108, nine arms added (three D4, three D3, one
D7, one D8, one D11); `grep -c '^arm '` reads 108.

## The direct run

Placed AFTER step 6 rather than inside step 3 where the brief lists it, deliberately: the brief
bounds this to ONE run, and a ceiling re-declared from a run that predates the nine arms steps 4
through 6 add is a number wrong on the next commit. Every fixed and new arm was observed on the
scratch harness first, so nothing was learned late that a step-3 run would have caught earlier.

- Clone: `git clone --local` of this worktree at `C:/Users/daily-agent/AppData/Local/Temp/cgrst`,
  tip `f23b71e0` (commit 6), frozen — nothing committed into it, and the worktree's later commits
  cannot reach it.
- Condition: direct, the suite alone, `SELFTEST_INNER_WIDTH` unset (width 1, which is also what
  the bar's leg row runs, since `run-gates.sh` exports no width to a leg), node `a`, 15 bash
  processes on the box before the run and 17 after. Started 16:43:28Z, ended 16:56:59Z.
- Verdict line, pasted from the output file: `PASS (108 arms, width 1)`. 108 `ok`, 0 `FAIL`,
  0 `ERR`. Wall from `date +%s` around the suite alone: **811 s** (rc 0).
- D9: the `walled 1` summary arm (`the summary counts a row the wall killed under 'walled'`) read
  `ok` in this run, so its want is NOT narrowed; the review's margin finding stands as a LOW and
  this is one observation of it holding at width 1 on a lightly loaded box, not a refutation.
- The 45 arms unit 5 marked `NOT YET OBSERVED RED` and every arm this pass added or fixed are in
  the 108 and read `ok`.

**Re-declared from it** (the eighth commit): `tools/gate-legs.json` — `run-selftests self-test`
ceiling 300 → **1217** (811 × 1.5 = 1216.5, rounded up); `tools/run-gates/selftest-budgets.txt`
— the row's budget 60 → **1217**, its reading column `measured 811s on node a 2026-09-14, direct
timed run of the suite alone on a frozen git clone --local at f23b71e0 (108 arms, inner width 1,
15 bash processes on the box before it started, PASS), x1.5 rounded up; …`. The 300 s it replaces
had never observed a wall: the leg was killed at `300.333` exit 124 on every bar since unit 5.
`--check` clean; `derive-ceilings.py --check` unchanged (the leg has no evidence row, since a
killed leg is not a reading); `--rank` still refuses on shard 8's DERIVED reading, which is D13
and the shard runs' to close. The reading is a width-1 figure; the bar runs this leg beside seven
others under the pool, and the review's lenses saw 15 min at width 6 — inside 1217 s, which is
why ×1.5 and not a tighter factor.

## Not closed here, and why

- **D13** — by the brief: re-measured at the direct shard runs the landing order owes.
- The two static left-shifts the review named for D5 and D6 are not wired, for the reasons under
  each row above (the harness now names D5's class at run time; D6's predicate reds seven
  interpolated wants on the real suite). Both are recorded, neither is silently dropped.
- The D4 arm is scoped to a declared pooled population rather than the whole declaration, and the
  declaration is a second spelling of the `--kit` argument the kit runner passes; a static refusal
  of an undeclared `--pooled --kit` is the follow-up that would collapse the pair.

## Round 2

The fix pass for the round-2 closing diff review
(`../reviews/2026-09-14-review-TOOL-aBatchedArm-1-closing-diff-round2.md`, CLEAN WITH FIXES, six
residues R1 to R6 of round 1's own fixes). ONE commit for all six, `baf97d8f`, subject
`aBatchedArm closing fix 8: round 2's six residues — …`; the same scratch harness as round 1 (the
suite's header and fixture builder, only the arms under observation, `run_arms`) run against the
pre-fix runner (a copy of `HEAD:tools/run-gates/run-selftests.sh` before the commit) and then the
fixed one; one direct timed run on a frozen clone. Every `.sh` edit through the Edit tool or
binary-mode Python; the committed blobs carry zero CR bytes by `git cat-file`. Ran afterwards:
`python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` (2 anchored classes, 5 universal,
each answered below), `python tools/lexicon/lexicon.py` (rc 0, offenders 984 at pin 984),
`bash tools/run-gates/run-selftests.sh --check` (clean, 69 rows, trailer arm graded 13),
`bash tools/check-install-prefix.sh` (clean, none rising), `bash tools/check-line-length.sh` (OK),
`bash tools/memory-tree/check-memory-hygiene.sh` (full, after the run, its line at the end of this section). Not run:
`check-unattended.test.sh` in any mode or shard, the other unattended suites, the bar,
`run-unattended-gates.sh` in any mode.

- **R1** (`baf97d8f`) — the per-row copy under `<git-dir>/gate-logs/selftests/` goes through the
  sibling runner's URL-userinfo mask, inlined (the two `sed -E` expressions compared byte-identical
  by extraction from both committed blobs), and `chmod 600`; every grep still reads `$d/out`. Arm:
  `suite-secret.sh` echoes `fatal: unable to access 'https://u:p@example.com/x'` and exits 1; the
  kept file lacks `u:p@`, keeps `example.com`, carries `***:***@`. Pre-fix rc 98 (the credential
  survived the bare `cp`); fixed `ok`. The file mode is not asserted: this node cannot observe it.
- **R2** (`baf97d8f`) — `NOBASE_RX` is extracted from the runner at the top of
  `run-selftests.test.sh` by the review's sed; the FIRST arm asserts it non-empty and greps
  `check-unattended.test.sh` for `echo "FAIL check_emitted: <rx>` verbatim; `suite-sentinel.sh`
  derives its line from the same value, so the third spelling is gone. Pre-fix rc 1 against a
  scratch copy of the owner with one word reworded (`observed` to `SEEN`); `ok` against the real
  owner. The reasoned RAISE of `tools/install-prefix-carried.txt:110` the review priced is NOT
  owed: the owner is reached as `$ROOT/tools/unattended/…`, and the carried-prefix predicate's
  lead class excludes `/`, so the literal is read as derived — observed both ways (the row raised
  to 6 redded the leg SLACK `6 -> 5`; reverted, `none rising`).
- **R3** (`baf97d8f`) — the WALL branch keys on rc 143 OR 137 under `WALL_BREACHED` at the
  calibrate site and the graded site; 124 stays KILLED; the RED summary reads `killed by a signal
  or its own bound`. The D8 arm's want is the WALL line
  `(killed by the 3s calibrate wall — NO reading written)` and its subject also asserts
  `run wall killed: free one` (rc 98 otherwise) beside the seed-absent check (rc 99). Pre-fix rc 98
  (the row rendered KILLED, no wall line); fixed `ok`.
- **R4** (`baf97d8f`) — the parser refuses `--check` given with `--kit`, by name, rc 2, beside the
  `--calibrate` refusal; the usage reads `takes no mode and no --kit`; no caller in the tree passes
  the pair (grepped). Arm: `# pooled-kit: tools/elsewhere/` declared, `--check --kit tools/suite-ok`
  selects both fixture rows and none under that kit. Pre-fix rc 1 `selects NO row, so the trailer
  arm graded nothing` — the review's false red, reproduced on the fixture; fixed rc 2.
- **R5** (`baf97d8f`) — `resolve_node_tag` and `--check`'s evidence reader compare the tag with
  `grep -qxF` over one tag per line. Reproduced on this repo's real registry first, with nothing
  executed (the no-reading refusal follows node resolution): the pre-fix runner accepted
  `GOV_NODE='a b'` and named `node a b` in its refusal; the fixed one refuses it by name, rc 2.
  Arm: the review's `GOV_NODE='t t'` cannot stage the defect on a one-tag fixture (` t ` holds no
  ` t t `), so the setup registers a second tag `u` and the subject uses `GOV_NODE='t u'`. Pre-fix
  rc 99 (a calibrate ran and wrote a reading under node `t u`); fixed rc 2, the file unchanged.
- **R6** (`baf97d8f`) — `unsound_why` accumulates with `; ` at the three sites. No arm, as the
  review ruled; this line is the documented check.

`SELFTEST_FLOOR` 108 to 112: four arms (R1, R2, R4, R5); `grep -c '^arm '` reads 112. The kickoff
manifest's `last-audit` re-stamped at the merge-base `fdd754bf` in the same commit with a delta
line (the runner is on its watch line; C5s compares the staged stamp with HEAD's).

The bug-class checklist, answered: `fixture-passes-by-finding-nothing` — every new or changed arm
observed RED first, above; `heredoc-escape-reaches-the-regex` — no heredoc authored any `.sh`
byte, and the R1 arm's `\*\*\*:\*\*\*@` reads as six escaped asterisks in the committed blob;
`staged-break-substitutes-a-synthetic-value` — the R2 arm reads the real owner and the real pin,
which is the fix; `two-answers-to-one-question` — the sentinel now has one owner and one pin,
and the mask regex is deliberately a second copy (the kit-file ban keeps it inline), compared once
here and gated by nothing else — recorded as the documented check; the remaining three classes
(inline fence, amendment's other half, empty-field collapse) were read against the diff and did
not fire.

### The direct run, round 2

- Clone: `git clone --local` of this worktree at `C:/Users/daily-agent/AppData/Local/Temp/cgrst2`,
  tip `baf97d8f`, frozen — nothing committed into it.
- Condition: direct, the suite alone, `SELFTEST_INNER_WIDTH` unset (width 1), node `a`, 18 bash
  processes on the box before the run; the seconds-long static gates above ran beside it.
- Verdict line, pasted from the output file: `PASS (112 arms, width 1)`. Wall from `date +%s` around the
  suite alone: **802 s** (rc 0).
- Against the declared ceiling of 1217 s (round 1's 811 s at ×1.5): inside it with 415 s to spare, and 9 s under round 1 with four more arms, so no re-declaration is owed (the review’s own ruling for these arms). 112 `ok`, 0 `FAIL`, 0 `ERR`; the D9 `walled 1` arm read `ok` a second time at width 1, still one observation per run and not a refutation.
