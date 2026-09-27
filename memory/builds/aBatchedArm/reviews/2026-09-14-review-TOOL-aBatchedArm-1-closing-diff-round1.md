**Serves:** diff-review TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3 TOOL-aBatchedArm-4 TOOL-aBatchedArm-5

# Tier-2 closing diff review — aBatchedArm, ROUND 1

*The closing review of the build, over the cumulative diff of its five CLOSED units at the
integration boundary. It is the ONLY reader between the build and its one gate pass: by two owner
rulings (2026-09-13, no self-test per step; 2026-09-14, no gate until every unit is built) nothing in
units 5, 1 and 2 has been executed against the real suite — `run-selftests.test.sh` carries 45 arms
never observed, the eight shards were never run after unit 1's conversion, the parity verdict never
ran over a real row, and the calibrate never ran. Unit 3's verification ran partially before the
ruling and its ledger says which halves. So this round reads the CODE as code, and weights a finding
by whether it reds the pass, or worse, lets it pass vacuously, on a node where one checker
invocation costs 47 to 60 s idle and the unsharded suite is about 5.8 h. Node `a`, 2026-09-14, ROUND
1. Every finding below survived a skeptic prompted to REFUTE it, and every cited line, count and
exit path was re-read or re-run in the tree by the author of this report rather than transcribed
from a lens: `python tools/lexicon/lexicon.py` (rc 1, `verb offenders 987 over pin 984`),
`python tools/codebase-map/test_codebase_map.py` (two FAILs, named below),
`bash tools/run-gates/run-selftests.sh --rank` (refuses on shard 8), `--kit tools/unattended --list`
(15 rows, 20590 s), `bash tools/unattended/check-arms-groups.sh` over the tracked suite (RED 5, by
design — see Observations), the `emitted` helper at `check-unattended.test.sh:93-104`, the calibrate
branch at `run-selftests.sh:1052-1071`, the evidence writer at `:1176-1237`, the parity branch at
`:1091-1110`, the `sw_missing` refusal at `:794-800`, the EXIT trap at `:864`, the refusal text at
`:855-858`, the harness body at `tools/lib/lib-selftest.sh:126-131`, the three arms at
`run-selftests.test.sh:334-336`, `:620-623` and `:829-832`, and the five green-only trailer prints
named under D4. Each row carries its address, the fix, and the gate that would have caught it
before a reviewer had to.*

**Reviewed range:** c2db2f5d2d6100af08a09da113086d114c67b603...7ee8395eacfb52a7be1e4bc0a48185c1672c7188
— base c2db2f5d is the run's pinned BASE (`RUN.md`), head 7ee8395e is the VERIFYING commit. The
orchestrator scoped the review to 17 files, 2022 insertions, 429 deletions (the code and config
surface; the range's full stat, records included, is 50 files). ROUND 1.

## Verdict: BLOCKED

Four rows at BLOCKER, two at HIGH, one at MEDIUM, six at LOW — thirteen distinct defects, into
which the twenty confirmed lens rows collapse (the table names which rows share one). Two of the
blockers red the bar before any self-test starts and cost minutes to fix; the other two are in the
LANDING ORDER, not in the bar, and are the ones that matter most: as unit 5's S5 is written, the
landing's calibrate either baselines the fourteen `emitted "?"` sentinel refusals as the parity
oracle — so `--pooled` prints GREEN over a suite that refused by name in fourteen groups, the exact
vacuity the sentinel was built to prevent — or cannot reach parity at all, because five of the
seven non-shard rows print their only trailer under `[ "$st" = 0 ]` and three of them are red by
design. Neither is a bar red. Both are a wasted multi-hour pass, and both are fixable before it
starts.

**Review shape:** raw 21 · confirmed 20 · refuted 1 · unverified 0 · precision 0.95.

**Run integrity:** lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0
contradictory verdict(s) demoted to unverified, 0 spurious verdict(s) discarded, 0 duplicate(s)
reported by the orchestrator's dedup pass. Those counts are stated as delivered. Reading the twenty
confirmed rows, three carry one defect each three times or twice — rows 3, 7 and 17 are one dead
arm; rows 4, 6 and 18 are one stranded literal; rows 1, 9 and 19 are one landing-order defect seen
from three angles; rows 8 and 14 are one trailer defect — so the dedup pass's zero is not what the
set holds, and this report merges them. No lens died, so a class this round reports nothing under
is the review's own nothing, not a hole in coverage; it is still not proof of absence.

## The findings, severity-ranked

| # | Severity | Lens rows | Where | Defect |
|---|---|---|---|---|
| D1 | BLOCKER | 12 | `.lexicon.conf:154`; `tools/unattended/check-unattended.test.sh:93`, `:520`, `:531` | The `lexicon naming predicates` leg is RED at HEAD: 987 verb offenders over the pin 984, the three arrivals being this diff's `emitted`, `replay_landed_main` and `topo_capture`. |
| D2 | BLOCKER | 13 | `tools/gate-legs.json:820`; `memory/map/features/unattended.md`; `memory/map/generated/` | The `codebase-map coverage + freshness` leg is RED at HEAD: the new `unattended arms-groups selftest` manifest row is claimed nowhere in the map tree and `inventories.json` is stale. |
| D3 | BLOCKER | 1, 19, 9 | `tools/run-gates/run-selftests.sh:1042`, `:864`; spec 5 S5; unit 1 ledger AC8 | The landing's calibrate baselines the fourteen sentinel `FAIL emitted:` lines as the parity oracle, or — if the paste lands first — has already discarded the `observed:` lines the paste needs. The two landing recipes are unordered relative to each other. |
| D4 | BLOCKER | 8, 14 | `tools/run-gates/run-selftests.sh:182`; five suites' `PASS (` lines | Five of the seven non-shard kit rows print their only trailer green-only; three are red at HEAD; the calibrate renders them UNTRAILED, writes no reading, and every later `--pooled --kit tools/unattended` refuses the whole population. S5 step (3) is unreachable. |
| D5 | HIGH | 3, 7, 17 | `tools/run-gates/run-selftests.test.sh:620-623` | The `--pooled --calibrate … grades nothing` arm ends in a bare `exit $rc` at the top level of the harness body, so no `.rc` is ever written and the arm reports `recorded no status` on every run. |
| D6 | HIGH | 4, 6, 18 | `tools/run-gates/run-selftests.sh:856-857`; `run-selftests.test.sh:334-336` | Unit 5 re-wrapped the below-largest-bound refusal so `would be killed before its` now straddles two `echo` lines with a `run-selftests: ` prefix between; the pre-existing arm wanting that substring reds on every run. |
| D7 | MEDIUM | 2 | `tools/run-gates/run-selftests.sh:1176` | An UNSOUND calibrate (fingerprint not taken, fingerprint changed, pool ran wider than OUTER) still writes its readings, and the RED summary blames walled/untrailed rows with both at 0. |
| D8 | LOW | 20 | `tools/run-gates/run-selftests.sh:1055-1058` | The calibrate WALL branch keys on rc 143 only; a declared trailer-less row killed via `timeout -k` (rc 137) or its own bound (rc 124) is written as a baseline of that rc. |
| D9 | LOW | 10 | `tools/run-gates/run-selftests.test.sh:829-832` | The `walled 1` summary arm pins an exact count on a 5 s suite against a 10 s wall and a 10 s bound; under the width-8 bar it lands under `killed` or `unrun`. |
| D10 | LOW | 11 | `tools/unattended/run-unattended-gates.sh:136-140` | `--checks --pooled` is accepted and the mode silently dropped, against the usage text and the refusal at `:189` that say `--checks` takes no mode. |
| D11 | LOW | 5 | `tools/run-gates/run-selftests.sh:201` | `resolve_node_tag` returns `GOV_NODE` verbatim, unchecked against the registry table `--check` enforces on the same field. |
| D12 | LOW | 16 | `tools/run-gates/run-selftests.test.sh:81` | The fixture keys every evidence row on tag `t` but never clears an inherited `GOV_NODE`; `GOV_NODE=a` in the environment turns 46 arms red. |
| D13 | LOW | 15 | `tools/run-gates/selftest-budgets.txt:114` | Shard 8's reading column is `DERIVED, not measured: …`, which matches neither CONDS pattern, so `--rank` refuses the whole ranking — the verb the build README calls one command away. |

### D1 — BLOCKER — the lexicon leg is RED before the pass starts

- **Where:** `.lexicon.conf:154` (`VERB_OFFENDER_PIN="984"`); the arrivals are
  `tools/unattended/check-unattended.test.sh:93` (`emitted`), `:520` (`replay_landed_main`), `:531`
  (`topo_capture`).
- **What:** `python tools/lexicon/lexicon.py` at HEAD exits 1 with `verb offenders 987 over pin
  984`. The base-to-head definition diff adds exactly three unruled names, all in the unit-3 and
  unit-1 edits of the suite; none of their leading tokens (`emitted`, `replay`, `topo`) is in the
  declared VERBS table. Every other new function in the diff leads with a table verb.
- **Impact:** the leg is `subject: repo` with guard `tools/`, which the diff touches, so it runs on
  the branch bar and on the final `GATE_FULL=1 GATE_SELFTESTS=1` pass — a certain red on a records
  defect, hours into the run.
- **Fix:** rename the two unit-3 helpers to table verbs (`replay_landed_main` → `run_landed_replay`,
  `topo_capture` → `read_topo`, updating their call sites in the same file) and re-stamp the pin
  for the owner-named `emitted`; or re-measure and re-declare `VERB_OFFENDER_PIN` with a dated,
  attributed line naming the three by file:line, per that file's own precedent. Read the number off
  the tool on the tree, never predict it.
- **Left-shift:** the gate exists and is seconds long. What was missing is the split between the
  rulings' "no gate until every unit is built", which defers the KIT self-tests, and the repo-subject
  legs that cost seconds. State in `memory/guides/BUILD-METHOD.md` that a build under that ruling
  still runs `bash tools/run-gates/run-gates.sh` without `GATE_SELFTESTS` before the expensive pass,
  so a records red never rides a multi-hour run.

### D2 — BLOCKER — the codebase-map leg is RED before the pass starts

- **Where:** `tools/gate-legs.json:820` (the new row `unattended arms-groups selftest`);
  `memory/map/features/unattended.md` (its `gate-legs = [...]` claim list); `memory/map/generated/`.
- **What:** `python tools/codebase-map/test_codebase_map.py` at HEAD: `FAIL
  test_every_inventory_key_is_claimed_or_baselined` with UNCLAIMED `{'gate-legs': ['unattended
  arms-groups selftest']}` and `FAIL test_generated_artifacts_are_fresh` (STALE `inventories.json`).
  `grep -rn arms-groups memory/map/` finds nothing. Unit 2 claimed the row in `kit.toml` and
  `subject-pins.tsv` and not in the map tree, and did not regenerate.
- **Impact:** the leg is `subject: repo` with no guard, so it runs on every bar on every node; the
  charter §1 DoD names both halves (claim new keys; regenerate in the same commit).
- **Fix:** add `unattended arms-groups selftest` to the `gate-legs` claim in
  `memory/map/features/unattended.md`, run `python tools/codebase-map/gen_map.py --write`, commit the
  regenerated artifacts in the same commit, and re-run the test (seconds) to see it green.
- **Left-shift:** same as D1 — the gate is right and fast; the process skipped it. The unit-2
  ledger's "wired, not listed" paragraph names three registries the new leg row must appear in
  (`kit.toml`, `subject-pins.tsv`, the leg manifest) and omits the map claim; add the fourth to that
  ledger template so the next leg row cannot forget it.

### D3 — BLOCKER — the landing's calibrate baselines the sentinel, or discards what the paste needs

- **Where:** `tools/run-gates/run-selftests.sh:1042` (`fails=$(grep -c '^FAIL' "$d/out")`), `:1058-1066`
  (the READ branch prints rc/FAIL/executed and nothing of the output), `:864` (the EXIT trap `rm -rf
  "$SWEEP_ROOT"`), `:1069` and `:1108` (`grep -E '^(FAIL|nope|.*FAILED)' | head -4`);
  `tools/unattended/check-unattended.test.sh:100-101` (the sentinel prints `FAIL emitted: expected set
  not yet observed …` un-indented, then the `    observed:` lines indented); spec 5 S5 (landing order:
  calibrate → commit → `--pooled` GREEN → flip); unit 1 ledger AC8 (the golden-writing step: run each
  shard directly, paste the sets from the `observed:` lines, re-run until no `FAIL emitted:` line).
- **What:** the suite carries fourteen `emitted "?"` sentinels, in shards 1, 2, 3, 4, 6, 7, 8 (2 · 1
  · 2 · 1 · 0 · 3 · 2 · 3, the unit-1 ledger's AC3 figure, re-counted here at 14). Each prints one
  `FAIL emitted:` line that `^FAIL` counts, and the shard still prints its `assertions executed`
  trailer on every run (`:3339`), so the calibrate records a READ row for every shard with the
  sentinels folded into `fails`. The next `--pooled` compares only (rc, fails, executed) and prints
  parity GREEN. Nothing downstream distinguishes a sentinel FAIL from a red-by-design one:
  `check-arms-groups.sh`'s own header says the sentinel is COUNTED and never graded. S5 orders the
  calibrate as step (1) with no paste before it, and unit 1's AC8 paste is owed "at the final pass"
  with no order pinned relative to S5. The calibrate's READ branch prints none of the suite's output
  and the trap deletes `$SWEEP_ROOT/<k>/out`, so the `    observed:` lines the paste is taken from
  are unobtainable from step (1); the two render paths that do print output cap at 4 lines and
  exclude the indented ones.
- **Impact:** either outcome is a wasted pass. Calibrate first: 7 of 8 shard rows are baselined with
  their 14 sentinel FAILs, step (3) prints parity GREEN, step (4) flips the DoD to `--pooled` over a
  suite that refused by name in fourteen groups; when the sets are pasted afterwards those 7 rows
  MISMATCH and the pooled DoD stays red until a second calibrate. Paste first: the eight direct
  shard runs the unit-1 ledger prescribes are the paste's only source, and the calibrate that follows
  cannot reuse their output. Reproduced by a lens on a fixture: a shard printing the sentinel line
  calibrates to `rc 1, 3 FAIL, 81 executed` and matches GREEN on the next `--pooled`.
- **Fix:** two halves, both before the pass. (a) ORDER: state in `RUN.md` and in S5 that the
  golden-writing step precedes step (1) — the eight direct shard runs the unit-1 ledger already owes,
  the paste, the re-runs until no `FAIL emitted:` line — and only then calibrate. That costs no new
  pass; the shard runs are owed either way. (b) MECHANISM, so the order can never matter again: add
  `SWEEP_NOBASELINE_RX='expected set not yet observed'` beside `SWEEP_TRAILER_RX` at `:182`, treat a
  hit as `untrailed` at calibrate (no reading, run RED, the row named) and as `MISMATCH` under
  `--pooled`; and persist each row's `$d/out` before the trap fires — `cp` it to
  `$(git rev-parse --git-dir)/gate-logs/selftests/<row>.out` in the render loop, the pattern
  `run-gates.sh` already uses for per-leg logs — and print that path on every non-`ok` row, so a
  calibrate leaves the artifact the paste needs and a pooled red has a debug surface larger than
  four lines.
- **Left-shift:** an arm in `run-selftests.test.sh` whose fixture suite prints `FAIL emitted:
  expected set not yet observed` and the executed-count trailer: `--pooled --calibrate` must exit
  RED naming it untrailed and leave the evidence file byte-unchanged (`git diff --quiet -- $E ||
  exit 99`), and `--pooled` against a seeded row must render MISMATCH. Class:
  `fixture-passes-by-finding-nothing`, applied to the oracle itself.

### D4 — BLOCKER — green-only trailers make the kit calibrate unreachable to GREEN

- **Where:** `tools/run-gates/run-selftests.sh:182` (`SWEEP_TRAILER_RX='PASS \(|assertions
  executed|this leg ran shard'`), `:1058` (a reading only for `trailer=1` or a declared no-trailer
  row), `:1067-1070` (UNTRAILED, st=1, no reading), `:794-800` (`sw_missing` refuses the whole run);
  `tools/unattended/adopt-unattended.test.sh:290`, `cross-component.test.sh:238`,
  `check-playbook.test.sh:793`, `check-arms-groups.test.sh:126`, `unattended.test.sh:5463` — each
  `[ "$st" = 0 ] && echo "PASS ($n assertions)"`, and the driver's `this leg ran` line at `:5462` is
  gated on `SH_I != 0`; `tools/run-gates/selftest-pooled-evidence.txt:22-23` declares only
  `brief-recorded` and `pass-order` trailer-less.
- **What:** the trailer rule treats a trailer as an unconditional artifact of the work, and for the
  eight shards it is (`check-unattended.test.sh:3339` prints on every run). For five of the seven
  non-shard rows the only trailer is green-only, and three of those rows are red at HEAD:
  `unattended adopter e2e` (run here: rc 1, 22 `^FAIL` lines, zero `PASS (` lines — a pre-existing
  fixture gap the unit-4 ledger and `TOOL-aQuenchedHarness-9` record), and `cross-component` and the
  driver suite (`TOOL-aTracedSpawn-1` records its 54 pre-existing failures). At S5 step (1) each is
  rendered UNTRAILED with no reading and the calibrate exits RED; every later `--pooled --kit
  tools/unattended` then hits `sw_missing` and runs nothing. The usage text at `:88-89` promises
  "a red-by-design suite that completed and matched is GREEN here"; that holds for the shards and the
  two declared rows only.
- **Impact:** S5's steps (3) and (4) are structurally unreachable, not merely walled — the spec's
  fallback anticipates walled rows and the build "lands without the flip", but the calibrate pass
  itself buys nothing and the pooled route is dead for the kit population until the trailers are
  fixed, which is the build's stated goal. The unit-5 ledger's "fourteen rows … 20530 s" is also one
  row stale: `--list` resolves 15 rows at 20590 s since unit 2 added its leg.
- **Fix (design-consistent):** give the five suites an unconditional executed-count line before
  their PASS line — one `echo "  ($n assertions executed)"` each, the alternative the regex already
  recognises — so the trailer rule holds for red-by-design rows too. **Fix (smallest):** declare
  them `# no-trailer:` in the evidence file's header (rc-plus-FAIL reading, gap printed), and say in
  that header that a green-only `PASS (` is the same class. Do not start the calibrate until
  `--pooled --calibrate --kit tools/unattended` can report `0 untrailed`.
- **Left-shift:** a `--check` arm that, for every row not declared `no-trailer`, greps the row's
  script for a trailer print outside a `[ "$st" = 0 ] &&` guard and reds by name when none exists —
  static, seconds, and it would have named these five before a 5.7 h serial-sum wall was declared
  over them. Class: `ab-arm-never-did-the-work` inverted — the work was done and the artifact
  withheld.

### D5 — HIGH — the calibrate's only end-to-end arm can never pass

- **Where:** `tools/run-gates/run-selftests.test.sh:620-623`; `tools/lib/lib-selftest.sh:126-131`
  (`eval "$4" > "$3.out" 2>&1; printf %s "$?" > "$3.rc"`).
- **What:** the subject string ends `… printf '%s\n' "$out"; exit $rc` with no enclosing `( … )`.
  `eval` runs it in the `bash -c "$_ST_BODY"` process itself, so the `exit` terminates the body
  before the `printf … > "$3.rc"`, and `_st_run_one` files `the subject recorded no status (runner
  exit 0) — it was cut off at the 120s arm bound, or could not start`. Its siblings at `:598` and
  `:646` wrap the same shape in a subshell precisely to avoid this. Reproduced standalone by a lens
  with the harness body: `x.out` written, no `x.rc`; the calibrate itself completes green in about
  7 to 10 s.
- **Impact:** deterministic FAIL in the `run-selftests self-test` leg — the one arm that observes the
  calibrate's grade-nothing property is dead and misreports its cause as a timeout. The leg is killed
  at its 300 s ceiling today (`tools/gate-legs.json:1312-1325`; the unit-5 ledger records `300.333
  fail`, exit 124) and the ledger plans to re-declare the ceiling "from the observed wall" at the
  final pass — but a leg killed at its ceiling observes no wall. The two lenses that ran the suite
  directly measured 11 min at width 1 and 15 min at width 6 for 99 arms; that direct run is where
  this red lands. Class: `status-set-in-a-subshell`, mirrored — the status is lost because the
  subject IS the shell.
- **Fix:** wrap the subject exactly as the marker arms do:
  `"( out=\$($R --pooled --calibrate); rc=\$?; printf '%s\n' \"\$out\" | grep -qE 'OVER BUDGET|TIMEOUT|sweep (GREEN|RED)' && exit 99; printf '%s\n' \"\$out\"; exit \$rc )"`.
  A lens verified this green against the real runner in a scratch harness.
- **Left-shift:** two, both cheap. In `lib-selftest.sh`, when `$3.rc` is absent but `$3.out` exists
  and the runner exited 0, say `the subject exited the harness body — wrap it in ( … )` instead of
  the timeout diagnosis, so the class names itself. And a static arm over the suite's own `arm`
  registrations: a subject string ending in a bare `exit …` outside parentheses reds at commit time.

### D6 — HIGH — a stranded literal: the refusal moved, its arm did not

- **Where:** `tools/run-gates/run-selftests.sh:855-858` (the four `echo … >&2` lines);
  `tools/run-gates/run-selftests.test.sh:334-336` (want `would be killed before its`, rc 2).
- **What:** at BASE the refusal printed `… so the run would be killed before its` on one line
  (`git show c2db2f5d:tools/run-gates/run-selftests.sh`, line 486). Unit 5 inserted `(an evidence
  bound)` and re-wrapped, so HEAD prints `… so the run would be` / `run-selftests: killed before its
  longest suite …`. The harness grades `case "$out" in *"$want"*` over the raw capture, and the
  wanted substring cannot span the newline plus prefix. The arm's string is byte-identical to BASE.
  `--sweep` still routes to `MODE=sweep` and `SELFTEST_WALL=5` still reaches the refusal, so rc 2 is
  right and the arm is dead on the message alone. Class: `arm-literal-strands-on-message-edit`;
  `amendment-leaves-its-other-half-standing`.
- **Impact:** the second deterministic FAIL in the `run-selftests self-test` leg, and it is the arm
  guarding the refusal that stops a wall from killing a legitimate sweep.
- **Fix:** keep the phrase contiguous — `:856` ending `… (an evidence bound), so the run would be
  killed before its` and `:857` starting `longest suite could legitimately finish. Raise` (the
  unit-5 arm wanting `population is 400s (an evidence bound)` still matches) — or change the arm's
  want to `so the run would be`.
- **Left-shift:** a static arm: every want-string of an rc-2 refusal arm in `run-selftests.test.sh`
  must occur verbatim (`grep -F`) in `run-selftests.sh`'s source. Milliseconds at commit time, and it
  catches every re-wrap of a refusal sentence before a 15-minute run does.

### D7 — MEDIUM — an unsound calibrate still writes its readings

- **Where:** `tools/run-gates/run-selftests.sh:1176` (`if [ "$CALIBRATE" = 1 ]` around the Python
  writer), after `:1147-1152` (peak over OUTER, `st=1`), `:1160-1164` (fingerprint not taken, `st=1`)
  and `:1165-1171` (`THE SWEEP IS UNSOUND`, `st=1`); the RED summary at `:1242-1245`.
- **What:** the writer is conditioned on `CALIBRATE`, not on `st`. A run that declared itself
  unsound — "every reading above is suspect", in its own words at `:1151` — writes those readings
  anyway; seconds become the monotone bound only `--reset` lowers, and the (rc, fails, executed)
  triple becomes the parity baseline every later `--pooled` is graded against. The RED summary then
  says `a walled or untrailed row wrote NO reading` with `walled 0` and `untrailed 0`. A lens
  observed it on a fixture: a suite appending to a tracked file produced `THE SWEEP IS UNSOUND`, exit
  1, and a rewritten evidence file. Spec S2 conditions the write on the wall and the trailer and is
  silent on soundness. Class: `one-value-field-records-a-mixed-outcome`.
- **Impact:** at the landing, reach needs a kit suite to write outside its scratch during the
  calibrate; the unit-3 ledger observed pool safety for the shards under one run, not the whole kit
  population under the calibrate. If it happens, the operator is told nothing was recorded while a
  contaminated baseline is committed at step (2).
- **Fix:** `sound=1`; `sound=0` in the three branches; wrap the writer in `if [ "$sound" = 1 ]`,
  else print `readings NOT written: this calibrate was unsound` and exit 1; make the RED summary
  name the actual cause.
- **Left-shift:** an arm whose fixture suite appends to a tracked file under `--pooled --calibrate`:
  exit 1, `UNSOUND` printed, and `git diff --quiet -- $E` (the evidence file unchanged) — the inverse
  of the existing `fingerprint MATCHED` arm at `:646`.

### D8 — LOW — a declared trailer-less row killed at rc 124 or 137 is recorded as a completion

- **Where:** `tools/run-gates/run-selftests.sh:1055` (WALL keys on `WALL_BREACHED=1 && rc=143`),
  `:1058` (a reading for any rc when `EV_NOTRAILER[name]=1`); the non-calibrate branch at
  `:1087` already treats 124/137 as TIMEOUT.
- **What:** `run_sweep_one` wraps each worker in `timeout -k 5`; a child that outlives TERM exits
  137 after the grace, and one that hits its own bound exits 124. Under the calibrate a declared-nt
  row (`brief-recorded`, `pass-order` in the real file) with either rc is written as a baseline of
  that rc; `walled` never names it; the next `--pooled` MISMATCHes a healthy run and names
  `--calibrate` as the remedy, which re-records whatever it sees. Reach needs a suite to survive
  TERM for 5 s, which is why this is LOW.
- **Fix:** before the declared-nt clause, `elif [ "$rc" = 124 ] || [ "$rc" = 137 ] || [ "$rc" = 143 ]`
  → st=1, walled/killed, no reading — the asymmetry with `:1087` closed.
- **Left-shift:** an arm with a declared-nt fixture row that traps TERM and sleeps past a 3 s
  wall: no reading written, the row named.

### D9 — LOW — the `walled 1` summary arm is a timing margin, not a mechanism

- **Where:** `tools/run-gates/run-selftests.test.sh:829-832`; the fixture margin `1\t1.0` at `:87`.
- **What:** budget 5 on both rows gives a per-suite bound of 10 s against `SELFTEST_WALL=10` and
  `OUTER=1`; the watchdog sleep starts before the dispatch loop, and `suite-mid` sleeps 5 s behind a
  subshell, `mkdir`, `read_now_ms`, `timeout` and two bash spawns. Past about 10 s wall-clock the
  row renders TIMEOUT (`killed 1`) or WALL with `suite-long` never dispatched (`walled 1 · unrun 1`),
  and the pinned `killed 0 · walled 1 · unrun 0` misses. A lens saw it fail once on this contended
  node and pass idle (`walled 1`, 19 s). The final pass runs this leg at width 8 beside the whole
  bar, which is the loaded case.
- **Fix:** assert only the `walled 1` token (as the pre-existing WALL arm asserts `run wall
  killed`), or size the fixture at wall 20 s / bound 10 s / long suite 60 s so a 5 s suite cannot
  cross its own bound under a 3x slowdown.
- **Left-shift:** none beyond the fix; the arm is the gate. Its margin is the finding.

### D10 — LOW — `--checks --pooled` drops the mode silently

- **Where:** `tools/unattended/run-unattended-gates.sh:136-140` (the mode case), `:189-191` (the
  refusal only for `ONLY != checks`), `:177` (usage: `Takes no mode.`), the summary at `:338`.
- **What:** `--checks --pooled` sets `MODE=pooled`, `ONLY=checks` skips both the refusal and the
  self-test block, `MODE_TOKEN` stays empty, and the summary prints `unattended gates GREEN — 5 ran
  on demand` with no mode token. The parser's own comment names silent last-wins as the class it
  refuses; the sibling runner refuses `--calibrate` under the wrong verb.
- **Fix:** after the loop, `if [ "$ONLY" = checks ] && [ -n "$MODE" ]; then echo "…--checks takes no
  mode; --$MODE was given" >&2; exit 2; fi`.
- **Left-shift:** an arm `run-unattended-gates.sh --checks --pooled` → rc 2 naming the pair.

### D11 — LOW — `GOV_NODE` is trusted on the write path and refused on the read path

- **Where:** `tools/run-gates/run-selftests.sh:201`; `--check` at `:588-599` reds any evidence row
  whose node is not a registry tag; the refusal at `:704-710` tells the operator to `set GOV_NODE=<tag>`.
- **What:** `resolve_node_tag` returns `GOV_NODE` verbatim without a lookup against
  `read_registry_tags`. `GOV_NODE=A` or a tab-bearing value makes the calibrate write a row that the
  unguarded `--check` leg then reds on every bar on every node until the tracked file is hand-edited.
  `GOV_NODE=b` on node `a` reading node b's bounds is arguably by design (spec S3, "GOV_NODE when
  set"); the unvalidated write is not.
- **Fix:** after reading `GOV_NODE`, require it in `read_registry_tags` output and refuse by name
  otherwise — one `case` line.
- **Left-shift:** an arm `GOV_NODE=zz $R --pooled --calibrate` → rc 2 naming the registry, evidence
  file unchanged.

### D12 — LOW — the fixture inherits `GOV_NODE`

- **Where:** `tools/run-gates/run-selftests.test.sh:81` (the fixture charter maps the current user to
  `t`); no `GOV_NODE` anywhere in the file; `run-selftests.sh:201` short-circuits on it.
- **What:** a lens reproduced `GOV_NODE=a SELFTEST_INNER_WIDTH=6 bash run-selftests.test.sh` going
  from 3/99 to 49/99 FAIL, 44 verdicts naming `on node a`. Nothing in `.githooks/`, `tools/` or the
  charter exports `GOV_NODE` today, and it is unset in this session, which is why this is LOW.
  Sibling suites scrub ambient state with `env -u` (`run-gates.evidence.test.sh:209`,
  `unattended.test.sh:475`). Class: `fixture-inherits-ambient-machine-state`. One lens sub-claim was
  wrong and is dropped: the registry-row-deleted arm at `:611` FAILS under `GOV_NODE=a` rather than
  passing for the wrong reason.
- **Fix:** `unset GOV_NODE` once at the top of the suite.
- **Left-shift:** the fix is the gate; the class is already recorded in `memory/gotchas/`.

### D13 — LOW — shard 8's derived reading kills `--rank`

- **Where:** `tools/run-gates/selftest-budgets.txt:114`; the CONDS patterns at
  `run-selftests.sh:306-308`; `memory/builds/aBatchedArm/README.md:20` ("one command away").
- **What:** `bash tools/run-gates/run-selftests.sh --rank` at HEAD exits 1, `NO share was computed`,
  naming `unattended gate selftest shard 8/8` whose fourth column reads `DERIVED, not measured: …
  893s scaled …`. At the merge base the same command ranks 61 rows. The refusal is correct — an
  unmeasured row must not rank — so the defect is the README pointer and the row's promise to be
  re-measured at the final pass.
- **Fix:** re-measure at the direct shard run D3(a) already owes and write the column in the closed
  vocabulary (`measured <n>s on node a <date>, direct serial run …`); do not re-phrase a derived
  number as measured.
- **Left-shift:** none needed — `--rank`'s refusal is the gate and it fired.

## The bug-class checklist, run over the diff

`python tools/memory-tree/gotchas.py --for-diff c2db2f5d..HEAD` selected 12 classes by anchor plus
5 universal. Where a class produced a finding it is named on the row above; the rest is the review's
own nothing, stated so a zero is never misread as coverage.

- `fixture-passes-by-finding-nothing` — D3 (the parity oracle passes over a refusing suite).
- `amendment-leaves-its-other-half-standing` — D6 (the message moved, the arm stayed).
- `one-value-field-records-a-mixed-outcome` — D7, D8 (a kill or an unsound run recorded as a reading).
- `status-set-in-a-subshell` — D5, mirrored: the subject is the shell and its status leaves with it.
- `two-answers-to-one-question` — D3 (the recorded golden and the pasted sets), D4 (the ledger's
  fourteen rows / 20530 s against `--list`'s 15 / 20590 s).
- `fixture-inherits-ambient-machine-state` (not on the selected list, but named by a gotcha) — D12.
- `id-matched-as-a-substring` — nothing found; the evidence key is a three-field tuple and the
  registry match is a whole-token compare.
- `empty-field-collapses-unless-it-is-last` — nothing found; the writer refuses a row that is not
  nine fields and the reader splits on tab with `executed="-"` as the empty spelling.
- `bounded-through-a-pipe-is-unbounded` — nothing found; the readings go through a file, not the
  heredoc's stdin (the writer's own comment at `:1185`).
- `heredoc-escape-reaches-the-regex`, `inline-fence-swallows-the-rest-of-the-file`,
  `staged-break-substitutes-a-synthetic-value`, `assertion-between-two-derived-values`,
  `fold-text-is-unreviewed-surface`, `hookspath-resolves-into-another-checkout`,
  `line-keyed-registry-reds-on-a-file-that-grew`, `process-creation-is-the-suite-cost`,
  `second-implementation-is-not-a-second-opinion` — nothing found by four lenses and this reader.
  Not proof of absence: nothing in units 5, 1 and 2 has run against the real suite, and the shard
  cut's region seams and unit 1's mutations-in-sequence were read, not executed.

## Observations, not findings

- `bash tools/unattended/check-arms-groups.sh` over the tracked suite exits 1 with `RED — 5
  finding(s) · rule A 0 · rule B 4 · rule C 1`. That is by design: the linter's header says
  existing violations are reported and never waived, and the unit-2 ledger records the same five as
  the starting figure. Only its self-test is a leg; the linter over the real suite is a documented
  check, and the five are unit 1's debt, not this review's. Worth one line in the landing record so
  the next reader does not file it as a red.
- The `run-selftests self-test` leg's ceiling is 300 s and the suite costs 11 to 15 min at widths 1
  and 6. The final pass will kill it at the ceiling (exit 124) exactly as before, and a killed leg
  yields no observed wall to re-declare from. Re-declare the ceiling from a direct timed run made
  AFTER D5 and D6 are fixed, before the pass, or the leg's row on the pass is a ceiling red that says
  nothing about the 45 unobserved arms.
- The unit-5 ledger's "fourteen rows" and "serial-sum wall of 20530 s" predate unit 2's leg row;
  the population is 15 rows at 20590 s. The spec says "the list's number", so the figure is derived
  and the ledger line is the copy that rotted — re-derive it in the landing record.

## What must precede the one gate pass, in order

1. D1 and D2 — minutes, verified by the two seconds-long commands named on their rows.
2. D5 and D6 — two edits; then a direct timed `bash tools/run-gates/run-selftests.test.sh`, from
   which the leg's ceiling and budget row are re-declared (D9's margin is fixed in the same edit if
   the run shows it flaking).
3. D4 — the five trailers, or the five declarations; `--pooled --calibrate --kit tools/unattended`
   must be able to report `0 untrailed` before anyone pays for it.
4. D3 — the sentinel refusal and the per-row log retention in the runner, and the landing order
   re-stated: the eight direct shard runs → the paste → re-run until no `FAIL emitted:` → the
   calibrate → commit → `run-unattended-gates.sh --pooled` GREEN → the flip. D7 rides the same
   runner edit.
5. Then `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, then S5's landing order as
   re-stated. D8, D10, D11, D12 and D13 can land with the fold or after it; none reds the pass.

**Unverified findings:** none — every lens row received a skeptic verdict.
