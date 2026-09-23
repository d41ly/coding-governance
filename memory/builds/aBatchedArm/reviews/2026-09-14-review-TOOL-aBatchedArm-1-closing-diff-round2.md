**Serves:** diff-review TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3 TOOL-aBatchedArm-4 TOOL-aBatchedArm-5

# Tier-2 closing diff review — aBatchedArm, ROUND 2

*The second round of the build's closing review, over the FIX commits that answered round 1
(`2026-09-14-review-TOOL-aBatchedArm-1-closing-diff-round1.md`, BLOCKED, thirteen defects) — eleven
commits, 18 files, 353 insertions, 80 deletions on the code and config surface; the range's full
stat, records included, is 28 files. This round asks two questions of each fix: did it close its
defect, and did it open another; and one of the range: did it bring in anything new. Node `a`,
2026-09-14. What the fix pass ran, by the rulings and its own ledger
(`../build/2026-09-14-build-TOOL-aBatchedArm-5-2-closing-fix-ledger.md`): the seconds-long static
gates, the arms-groups linter and its self-test, and ONE direct timed
`bash tools/run-gates/run-selftests.test.sh` on a frozen `git clone --local` at `f23b71e0` — PASS,
108 arms, width 1, wall 811 s. What has still NOT run: `check-unattended.test.sh` in any mode or
shard, the other unattended suites, the bar, `run-unattended-gates.sh` in any executing mode. One
checker invocation costs 47 to 60 s on this node idle. Every finding below survived a skeptic
prompted to REFUTE it, and every cited line was re-read in the tree by the author of this report,
who also re-ran what costs seconds: `python tools/lexicon/lexicon.py` (rc 0, `lexicon OK`),
`python tools/codebase-map/test_codebase_map.py` (rc 0), `bash tools/run-gates/run-selftests.sh
--check` (clean: 69 rows, trailer arm graded 13 under `pooled-kit tools/unattended`, 2 declared
no-trailer), `--check --kit tools/lib` (rc 1 — finding R4, reproduced), the linter over the tracked
suite (`RED — 5 · rule A 0 · rule B 4 · rule C 1`, the by-design figure), and the node-tag predicate
against this repo's real registry (`GOV_NODE='a b'` ACCEPTED — finding R5, reproduced). The
bug-class checklist for the range, `python tools/memory-tree/gotchas.py --for-diff
7ee8395e..1d87952c`, named 13 anchored classes and 5 universal; the section below says which fired.*

**Reviewed range:** 7ee8395eacfb52a7be1e4bc0a48185c1672c7188...1d87952c9399a9d3f257fef307284f51104a226c
— base 7ee8395e is round 1's recorded tip, head 1d87952c is the worktree HEAD at review time.
ROUND 2.

## Verdict: CLEAN WITH FIXES

Zero rows at BLOCKER, zero at HIGH, two at MEDIUM, four at LOW — six distinct defects, into which
the nine confirmed lens rows collapse (rows 3, 6 and 11 are one ungated pair; rows 5 and 13 are
one misattributed kill). Every one of the six is a residue of a round-1 fix rather than a new
surface: the durable copy D3(b) added skips the redaction its sibling applies; the sentinel phrase
D3(b) pinned is spelled three times and gated nowhere; D8's KILLED branch takes the wall's own
grace-kill; D4's static arm grades a filtered population against a whole-file declaration; D11's
validator is a substring match; D7's cause line is overwritten. None reds the one gate pass that
follows, and none makes it vacuous today: the bar's `--check` leg passes no `--kit`, the 108 arms
observed green are the arms the pass will run, and the sentinel pair is byte-identical at HEAD.
All thirteen round-1 defects are closed or deferred by ruling (the table below says which); the
fixes land with the fold, and four of the six are one-line edits to the runner that belong in ONE
commit with the D8 arm's want updated beside them, because R3's fix changes the line that arm
asserts.

**Review shape:** raw 15 · confirmed 9 · refuted 6 · unverified 0 · precision 0.60.

**Run integrity:** lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0
contradictory verdict(s) demoted to unverified, 0 spurious verdict(s) discarded, 0 duplicate(s)
reported by the orchestrator's dedup pass. Stated as delivered. Reading the nine confirmed rows,
three carry the sentinel pair (ids 3, 6, 11) and two carry the D8 kill (ids 5, 13), so the dedup
pass's zero is not what the set holds, and this report merges them. No lens died, so a class this
round reports nothing under is the review's own nothing rather than a hole in coverage; it is
still not proof of absence, and the kit suites remain unexecuted.

## Round 1's thirteen, each with its disposition at HEAD

| # | Round-1 severity | Fix commit | Disposition at 1d87952c |
|---|---|---|---|
| D1 | BLOCKER | `cb1f4541` | CLOSED. Three helpers renamed to table verbs; `python tools/lexicon/lexicon.py` rc 0 at HEAD, re-run here. The pin 984 was not re-declared. |
| D2 | BLOCKER | `d3000f70` | CLOSED. The leg row is claimed in `memory/map/features/unattended.md`; `test_codebase_map.py` rc 0 at HEAD, re-run here. |
| D3 | BLOCKER | `214b7183` (b), `ff549e63` (a) | CLOSED, with two residues. (a) the landing order is stated in `RUN.md` and in spec 5 S5 step (0): shards → paste → re-run → calibrate. (b) `SWEEP_NOBASELINE_RX` at `run-selftests.sh:199`; a hit is UNTRAILED at calibrate (`:1173`) and MISMATCH under `--pooled` (`:1236`); each row's `$d/out` is copied durable (`:1119`). Residues: R1 (the copy is unredacted), R2 (the phrase is ungated). |
| D4 | BLOCKER | `1f739769` | CLOSED, with one residue. All five suites print `  ($n assertions executed)` unconditionally (verified by grep at HEAD: `adopt-unattended.test.sh:293`, `check-playbook.test.sh:795`, `cross-component.test.sh:249`, `unattended.test.sh:5465`, `check-arms-groups.test.sh:128`); `--check` holds the rule statically under the `# pooled-kit:` declaration. Residue: R4. |
| D5 | HIGH | `72f9586d` | CLOSED. The calibrate arm's subject is wrapped in `( … )` (`run-selftests.test.sh:639-642`); the harness now names the class (`lib-selftest.sh:166-172`); observed `ok` in the direct run. The review's static arm was not wired, for a stated reason; recorded, not dropped. |
| D6 | HIGH | `72f9586d` | CLOSED. `so the run would be killed before its` is one line again (`run-selftests.sh:930`); both arms `ok` in the direct run. The review's left-shift was run as a candidate first, redded 7 interpolated wants, and was not wired; recorded. |
| D7 | MEDIUM | `214b7183` | CLOSED, with one residue. `sound=1` cleared by the three post-loop checks; the writer runs only when sound (`:1320-1322`); the RED summary names the cause (`:1383`). Residue: R6. |
| D8 | LOW | `f23b71e0` | CLOSED for the reading, with one residue. rc 124/137/143 is KILLED before the declared-nt clause (`:1164-1172`); no reading written; the fixture `suite-stubborn.sh` observed `ok`. Residue: R3 — the wall's own grace-kill is attributed to a bound. |
| D9 | LOW | — | OPEN as recorded. The `walled 1` arm read `ok` once, at width 1 on a lightly loaded box; the ledger says that is one observation, not a refutation. Stands as a LOW margin finding. |
| D10 | LOW | `f23b71e0` | CLOSED. `run-unattended-gates.sh:198-204` refuses `--checks` with a mode, rc 2, observed directly; the arm in `cross-component.test.sh:26-28` is the gate pass's to run. |
| D11 | LOW | `f23b71e0` | CLOSED for an unregistered tag, with one residue. `GOV_NODE=zz` is refused by name (arm observed `ok`). Residue: R5 — the predicate is a substring match. |
| D12 | LOW | `f23b71e0` | CLOSED. `unset GOV_NODE` at `run-selftests.test.sh:19`. |
| D13 | LOW | — | DEFERRED by the brief. Shard 8's `DERIVED, not measured` reading is re-measured at the direct shard runs the landing order owes; `--rank` refuses until then and `RUN.md` says so. |

## The findings, severity-ranked

| # | Severity | Lens rows | Where | Defect |
|---|---|---|---|---|
| R1 | MEDIUM | 1 | `tools/run-gates/run-selftests.sh:1119` | The durable per-row copy is a bare `cp` — no URL-userinfo redaction, no `chmod 600` — where its sibling `run-gates.sh:117`, `:1404-1405`, `:1418-1420` masks and restricts every durable leg log and its own comment names the unmasked copy a credential leak. |
| R2 | MEDIUM | 3, 6, 11 | `tools/run-gates/run-selftests.sh:199`; `tools/unattended/check-unattended.test.sh:100`; `tools/run-gates/run-selftests.test.sh:86` | `SWEEP_NOBASELINE_RX` is a prose pin of a phrase the suite owns, spelled three times and gated nowhere; a reword reopens D3 silently while every D3 arm stays green on its own copy. |
| R3 | LOW | 5, 13 | `tools/run-gates/run-selftests.sh:1160`, `:1164`, `:1381`; same key at `:1202` | The WALL branch keys on rc 143 only, so a row the wall TERMed and `timeout -k 5` KILLed (rc 137, `WALL_BREACHED=1`) is counted `killed`, `walled` stays 0, the `run wall killed:` line never prints, and the summary says `under a bound rather than the wall` — false in the only scenario that reaches it under `--calibrate`. |
| R4 | LOW | 8 | `tools/run-gates/run-selftests.sh:659-673` | The static trailer arm iterates the `--kit`-FILTERED `$POP` against a whole-file `# pooled-kit:` declaration; `--check --kit <dir outside tools/unattended>` reds with `selects NO row`. Its sibling ORPHAN arm at `:630-632` reads the whole declaration for exactly this reason. |
| R5 | LOW | 12 | `tools/run-gates/run-selftests.sh:223`; same shape at `:627` | `resolve_node_tag` validates `GOV_NODE` with `case " $tags " in *" $GOV_NODE "*)`, a substring match over the space-joined list, so `GOV_NODE='a b'` is accepted and written as a node; `--check`'s reader has the identical shape and certifies the row. |
| R6 | LOW | 9 | `tools/run-gates/run-selftests.sh:1278`, `:1291`, `:1296` | `unsound_why` is assigned with `=` at three independent sites, so a calibrate that ran wide AND saw the tree change records one cause on the two summary lines. |

### R1 — MEDIUM — the kept output skips the masking its sibling applies

- **Where:** `tools/run-gates/run-selftests.sh:1119` (`cp "$d/out" "$outlog" 2>/dev/null || outlog=""`),
  into `SWEEP_LOGDIR="$_gd/gate-logs/selftests"` (`:949`, the directory is `chmod 700`).
- **What:** the D3(b) fix keeps every pooled row's stdout under `<git-dir>/gate-logs/selftests/`
  so the `observed:` lines can be pasted. It copies the bytes raw and at the umask's mode. The
  sibling that established the pattern, `run-gates.sh`, defines `redact()` at `:117` (URL userinfo
  → `***:***`), pipes both of its durable copies through it and `chmod 600`s them (`:1404-1405`,
  `:1418-1420`), and its comment at `:1414-1417` says why in these words: a durable copy that skips
  the masking its sibling applies is a credential leak the old scratch-dir lifetime was merely
  hiding. `grep -n 'redact\|userinfo' tools/run-gates/run-selftests.sh` finds nothing.
  `run-gates.evidence.test.sh:140-150` (arm 5) gates the redaction for `run-gates` only; no arm in
  `run-selftests.test.sh` covers this copy. The same self-test suites therefore get two treatments
  for identical output bytes: redacted as bar legs, raw as pooled rows.
- **Impact:** before this range a credential a suite echoed (the exact case the sibling's comment
  names — a `fatal: unable to access 'https://user:token@host/…'` from a git call under the
  operator's global config) died with the mktemp scratch at the trap. Now every `--pooled` and
  `--calibrate` run, including the landing order's calibrate and `run-unattended-gates.sh --pooled`,
  persists it unmasked. The fixtures the kit suites drive are local-path remotes, so no such URL is
  expected in THIS landing's output; the class is what the sibling gates, and MEDIUM prices a
  security-class gap with no live instance and a POSIX-only directory mode as its mitigation.
- **Fix:** replace the `cp` with the sibling's masking, inline (the kit-file literal ban means it
  cannot be sourced): `sed -E 's#://[^/@[:space:]]+:[^/@[:space:]]+@#://***:***@#g' "$d/out"
  > "$outlog" 2>/dev/null && chmod 600 "$outlog" 2>/dev/null || outlog=""`. Keep every grep
  (`fails`, `trailer`, `nobase`, `executed`) reading `$d/out`, so no verdict changes.
- **Left-shift:** one arm in `run-selftests.test.sh` in the shape of `run-gates.evidence.test.sh`
  arm 5: a fixture suite that echoes `https://u:p@example.com` and exits 1; assert the kept file
  under `gate-logs/selftests/` lacks `u:p@` and keeps `example.com`. Stage the break (leave the
  `cp`), see RED, then wire. `SELFTEST_FLOOR` 108 → 109.

### R2 — MEDIUM — the sentinel phrase is three spellings and one comment

- **Where:** `tools/run-gates/run-selftests.sh:199` (`SWEEP_NOBASELINE_RX='expected set not yet
  observed'`, its comment at `:198` asserting `verbatim`); the owner,
  `tools/unattended/check-unattended.test.sh:100` (`echo "FAIL check_emitted: expected set not yet
  observed — owed at the final pass · call at line ${BASH_LINENO[0]}"`); the fixture copy,
  `tools/run-gates/run-selftests.test.sh:86` (`suite-sentinel.sh`).
- **What:** `git grep -n 'expected set not yet observed' -- tools/` finds exactly those three
  producers and nothing joins them: the constant is read only inside the runner (`:1148`, `:1178`,
  `:1236`); `check-arms-groups.sh` counts sentinels by the `"?"` argument, not the phrase;
  `check-playbook-parity.sh`'s PAIRS are template-versus-source and do not cover it. The line IS
  edit-live: commit `cb1f4541` in this very range reworded the prefix of that owner line (`FAIL
  emitted:` → `FAIL check_emitted:`), and the pinned substring survived because the rename stopped
  one word short of it. The D3 arms at `run-selftests.test.sh:811-829` exercise the fixture rather
  than the real helper, so they cannot notice a reword of the owner.
- **Impact:** a one-word reword of the refusal's tail — the lexicon, a fold, a tidy — makes
  `nobase` never fire. A sentinel-carrying shard still has rc 1, FAIL ≥ 1 and the executed-count
  trailer, so the calibrate at `:1173-1180` READs it as a baseline and the next `--pooled` prints
  parity GREEN over a group that refused by name in every batched group, while every D3 arm stays
  green on its own copy and `--check` stays green throughout. That is D3 returning silently — the
  hole the constant was written to close, held shut by a comment. Two checklist classes:
  `two-answers-to-one-question` and `staged-break-substitutes-a-synthetic-value` (the fixture is a
  typed copy, not a read of the suite). Latent today: verified byte-identical at HEAD.
- **Fix:** gate the pair where the pin lives. One arm at the top of `run-selftests.test.sh`, before
  the fixture: extract the constant with `sed -n "s/^SWEEP_NOBASELINE_RX='\(.*\)'$/\1/p"` from
  `$ROOT/tools/run-gates/run-selftests.sh`, assert it is non-empty, and assert `grep -qF -- "echo
  \"FAIL check_emitted: $rx"` over `$ROOT/tools/unattended/check-unattended.test.sh`. Then derive the
  fixture's line 86 from the same `$rx` instead of retyping it, which kills the third spelling. A
  reword of either side reds a seconds-long arm rather than the next calibrate.
- **Left-shift:** the arm IS the gate; stage the break (edit one word in the owner line), confirm
  RED, unstage. Cost to name: the arm adds one `tools/unattended/…` literal to a `tools/run-gates/`
  file, so `tools/install-prefix-carried.txt:110` (`run-selftests.test.sh`, count 5) takes a
  reasoned RAISE to 6 in the same commit — the registry's own header allows a human's reason and
  nothing else. The kit-side alternative (an arm in `cross-component.test.sh` beside the D10 arm)
  raises `:125` from 1 to 2 for the same reason; either is one line, and the runner-side one also
  collapses the fixture copy.

### R3 — LOW — the wall's grace-kill is reported as a bound

- **Where:** `tools/run-gates/run-selftests.sh:1160` (`[ "$WALL_BREACHED" = 1 ] && [ "$rc" = 143 ]`),
  `:1164-1172` (the KILLED branch, rc 124/137/143), `:1250` (`run wall killed:` prints only when
  `walled` is non-empty), `:1380-1381` (the summary and its `under a bound rather than the wall`
  sentence). The graded branch at `:1202` keys on 143 the same way.
- **What:** under `--calibrate` every ok row's bound is `SWEEP_WALL + 5` (`:899`), so `timeout`'s own
  alarm can never fire before the watchdog's TERM at `SWEEP_WALL` (`:1052-1058`). A suite that
  ignores TERM is KILLed by the worker's `timeout -k 5` (`:1032`) after the grace and exits 137 —
  GNU timeout reports the child's signal plus 128 when the signal was not its own alarm. That row
  falls to the KILLED branch: `killed` is incremented, `walled` and `walled_n` stay 0, the `run wall
  killed:` line never prints, the summary reads `0 walled`, and `:1381` states the row was killed
  `under a bound rather than the wall`. The D8 fixture (`suite-stubborn.sh`,
  `run-selftests.test.sh:91-94`, `SELFTEST_WALL=3`) and the D8 arm at `:843-846` exercise exactly
  this path, and the arm's want (`is a kill, not a completion — NO reading written`) pins the
  misattributing line.
- **Impact:** no reading is written either way, so parity and the baseline are unaffected. The
  operator is told the wrong cause and pointed at the wrong knob: the remedy for a wall kill is
  `SELFTEST_WALL` or `--reset`, and the summary names neither. On the landing calibrate a
  TERM-ignoring kit suite that breaches the serial-sum wall would be reported as a suite-side kill.
  Class: `one-value-field-records-a-mixed-outcome`, loosely — the row's fact is `walled` and the
  branch chose `killed`.
- **Fix:** widen the WALL branch's key to the wall's whole signal path: `if [ "$WALL_BREACHED" = 1 ]
  && { [ "$rc" = 143 ] || [ "$rc" = 137 ]; }; then` at `:1160` and `:1202` (the wall's TERM escalated
  to KILL by `-k` is still the wall); keep 124 in KILLED. Reword `:1381` to `killed by a signal or
  its own bound`. **In the same commit** change the D8 arm's want at `:844` to the WALL line, or the
  `run-selftests self-test` leg reds on the gate pass with a fixed runner and a stale want — the
  D6 class, one round later.
- **Left-shift:** extend the D8 arm's want to also assert `run wall killed: free one` in the output,
  so the counter and the line are pinned together and a future 143-only key reds by name.

### R4 — LOW — the static trailer arm grades a filtered population against a whole-file declaration

- **Where:** `tools/run-gates/run-selftests.sh:659-673` (the loop reads `$POP`), `:517`
  (`POP=$(read_population)`, filtered by `FILTER` from `--kit` at `:143`), `:630-632` (the ORPHAN
  arm reads `$BUDGETS` unfiltered, with the comment `a row outside a filter is declared all the
  same, and reading it as an orphan would red a true file`).
- **What:** reproduced at HEAD: `bash tools/run-gates/run-selftests.sh --check --kit tools/lib`
  exits 1 printing only `pooled-kit tools/unattended selects NO row, so the trailer arm graded
  nothing`; `--check --kit tools/unattended` and bare `--check` are green. The parser accepts
  `--kit` with `--check` (`:140-162`) and the usage does not forbid the pair. The sibling arm two
  screens up follows the rule this one misses.
- **Impact:** a false red on a manual invocation. No caller in the tree passes `--kit` to `--check`
  and the bar's `--check` leg passes none, so the gate pass is unaffected. The same split is the
  pair the fix ledger already records as known: the `# pooled-kit:` declaration and
  `run-unattended-gates.sh`'s hard-coded `--kit tools/unattended` (`:302`, `:320`, `:329`) are two
  substring filters on argv that happen to select the same 15 rows today.
- **Fix:** the one-line version that matches the usage text: refuse `--check` given with `--kit` by
  name in the parser, beside the `--calibrate` refusal at `:163`. The version that matches the
  sibling: feed the arm `FILTER= read_population` into its own variable and iterate that (bash
  scopes the prefix assignment to the call). Either; not both.
- **Left-shift:** one arm in `run-selftests.test.sh`: `--check --kit tools/lib` exits 0 (or 2 with
  the refusal by name, per the fix chosen), never 1.

### R5 — LOW — the node-tag validator is a substring match

- **Where:** `tools/run-gates/run-selftests.sh:223` (`case " $(read_registry_tags | tr '\n' ' ')" in
  *" $GOV_NODE "*)`); the identical shape in `--check`'s reader at `:627` (`case "$ev_tags" in
  *" $c "*)`).
- **What:** reproduced against this repo's registry with the script's own `read_registry_tags` and
  pattern: tags `a b c d`; `GOV_NODE='a b'` ACCEPTED, `'b c d'` ACCEPTED, `'zz'` refused, `'a  b'`
  refused. The guard's contract at `:219-222` is `set but not a tag → return 2`, and any
  space-joined run of adjacent registered tags breaks it. Downstream nothing catches it:
  `SWEEP_NODE` lands verbatim in the evidence key and the writer; `read_evidence` requires only a
  non-empty node field; and `--check` at `:627` accepts the row by the same predicate, so both
  readers agree on a node the registry does not have. Class: `id-matched-as-a-substring`, count 3
  in `memory/gotchas/INDEX.md` — the class D11 was meant to close.
- **Impact:** misconfiguration-only reachability; the result is a tracked evidence row keyed under a
  node no real node's `--pooled` will read, that `--check` certifies well-formed. A dead row rather
  than a wrong verdict. LOW.
- **Fix:** an anchored comparison at both sites: `read_registry_tags | grep -qxF -- "$GOV_NODE"` in
  `resolve_node_tag`, and the same `grep -qxF -- "$c"` for the `ev_tags` test.
- **Left-shift:** extend the D11 arm (`run-selftests.test.sh:849-853`) with a second invocation under
  `GOV_NODE='t t'` (two copies of the fixture's one tag) expecting rc 2 and the evidence file
  unchanged.

### R6 — LOW — the unsound cause is overwritten, not accumulated

- **Where:** `tools/run-gates/run-selftests.sh:1278` (pool wider than OUTER), `:1291` (fingerprint
  not taken), `:1296` (fingerprint changed); consumers at `:1322` and `:1383`.
- **What:** the width check is an independent `if` and the two fingerprint checks are an
  `if/elif`, so a run that oversubscribed the box AND saw the tree change sets `unsound_why` twice
  with `=`; the two summary lines name the fingerprint only. Both full explanation blocks still
  print above, so the fact is on screen — it is the one line an operator greps that records a
  mixed outcome as one value.
- **Impact:** requires two independent anomalies in one calibrate; both demand the same
  disposition (unsound, nothing written, st 1), so nothing is written wrongly. LOW. The cited
  checklist class (`one-value-field-records-a-mixed-outcome`) is a loose fit for the same reason.
- **Fix:** accumulate at the three sites: `unsound_why="${unsound_why:+$unsound_why; }<reason>"`.
- **Left-shift:** none owed beyond the edit; a two-anomaly fixture would cost more than the
  defect. Recorded here as the documented check.

## The bug-class checklist, run over the diff

`python tools/memory-tree/gotchas.py --for-diff 7ee8395e..1d87952c` selected 13 anchored classes
and 5 universal. Fired, with the row that carries each:

- `two-answers-to-one-question` — R2 (the phrase, three spellings); also the known pair R4 names
  (`# pooled-kit:` versus the kit runner's `--kit`), recorded in the fix ledger and not re-filed.
- `staged-break-substitutes-a-synthetic-value` — R2 (the fixture's typed copy of the owner line).
- `id-matched-as-a-substring` — R5.
- `one-value-field-records-a-mixed-outcome` — R3 and R6, both loose fits, both said so on the row.
- `fold-text-is-unreviewed-surface` — the whole range is fold text, and every one of the six
  findings is in it; that is the class doing its job, not a seventh finding.

Checked and not fired, by four lenses and this reader: `fixture-passes-by-finding-nothing` (the
nine new arms each red against the pre-fix runner on the scratch harness, per the ledger, and the
direct run observed all 108 `ok`), `heredoc-escape-reaches-the-regex` (the ledger's `\t` trap was
caught by `cat -A` and the committed awk regex reads `[ \t]` by `git cat-file`),
`inline-fence-swallows-the-rest-of-the-file` (no inline fence in the range's records),
`amendment-leaves-its-other-half-standing` (spec 5's S5 step (0) and `RUN.md`'s Landing order
agree; the old `FAIL emitted:` prefix survives only in ledgers as history),
`assertion-between-two-derived-values`, `bounded-through-a-pipe-is-unbounded` (the calibrate arm's
`out=$(…)` capture is inside the D5 parentheses and the watchdog is disowned with stdout closed),
`containment-tested-one-way`, `empty-field-collapses-unless-it-is-last` (the evidence reader's
nine tab fields are all non-empty by shape), `fixture-inherits-ambient-machine-state` (D12's
`unset GOV_NODE` is the fix for that class), `format-derived-from-arity`,
`process-creation-is-the-suite-cost` (the ceiling was re-declared from a measured wall, not
predicted), `second-implementation-is-not-a-second-opinion`, `status-set-in-a-subshell` (every
new `st=1` is at the loop's own level; the D10 arm's `$?` is read outside the substitution). Not
proof of absence: the kit suites have not run, and R2 is the reminder that a green arm on a
fixture proves the fixture.

## Observations, not findings

- The D8 arm's want and R3's fix are one edit: whoever lands R3 must change
  `run-selftests.test.sh:844` in the same commit or the `run-selftests self-test` leg reds on the
  pass. Said on the row and repeated here because it is the one way this round's fixes could red
  the gate pass.
- Every runner edit re-stamps the kickoff manifest (C5s compares the staged stamp with HEAD's on
  every commit that touches `run-selftests.sh`, per the ledger), so R1, R3, R5 and R6 in one commit
  cost one re-stamp rather than four.
- The `run-selftests self-test` ceiling of 1217 s is a width-1 figure from a box with 15 bash
  processes; the pass runs the leg beside seven others under the pool. The ledger prices the ×1.5
  against the lenses' 15 min at width 6. If R1's new arm and R2's arm land before the pass, the
  reading grows by seconds and the margin holds; a re-declaration is not owed for them.
- The arms-groups linter over the tracked suite still reads `RED — 5 · rule A 0 · rule B 4 ·
  rule C 1`, the by-design figure round 1 recorded; rule A at 0 is the observation that D1's rename
  kept the regex keyed. Unit 1's debt, not this round's.

## What precedes the one gate pass

1. One commit to the runner: R1 (the masked copy), R3 (the WALL key at `:1160` and `:1202`, the
   `:1381` sentence, the D8 arm's want), R5 (`grep -qxF` at `:223` and `:627`), R6 (the three
   appends); plus R1's redaction arm and R2's parity arm in `run-selftests.test.sh` with
   `SELFTEST_FLOOR` raised and the one reasoned RAISE in `tools/install-prefix-carried.txt`. Then
   `bash tools/run-gates/run-selftests.sh --check` (seconds) and the two new arms plus the D8 arm
   on the scratch harness, RED against the pre-fix runner first.
2. R4 can ride the same commit (one line either way) or land after the pass; it reds no leg.
3. Then `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, then the landing order in
   `RUN.md`: the eight shard runs, the paste, the re-runs, the calibrate, the evidence commit,
   `run-unattended-gates.sh --pooled` GREEN, the flip. D13's re-measure rides the shard runs.

**Unverified findings:** none — every lens row received a skeptic verdict.
