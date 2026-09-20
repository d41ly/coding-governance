**Serves:** diff-review TOOL-aDeferredBar-1 TOOL-aDeferredBar-2 TOOL-aDeferredBar-3

# aDeferredBar — closing diff review of the three-unit build, round 1

*Node `a`, 2026-09-14, unattended. A Tier-2 adversarial pass over the cumulative diff of the build:
four primed finder lenses, five batched skeptic passes prompted to REFUTE every finding, one
synthesis. Every claim below that names an exit code was re-run on this tree during synthesis —
`bash tools/check-install-prefix.sh` on the clean tip, the `BAR` regex out of `check-spec-tokens.py`
over the quoted-empty token, and seven commands fed to `tools/unattended/gate-guard.js` as Bash
tool-use payloads with this worktree's `cwd` while its `RUN.md` reads `phase: REVIEWING` — and the
figures are what those runs printed. The security model the units declare is read as given: the hook
is a hygiene guard, textual, fails open, exactly as `tools/hooks/scratch-guard.js` says of itself; a
runtime-assembled path walks past it by design and it is not a containment boundary. No finding
below argues with that ceiling; three of them sit inside it.*

**Reviewed range:** `b2a330be17b8e195981002f3a5aa4b07d2256bd8...HEAD`, HEAD being `9a47292d` (every unit
terminal, phase REVIEWING). The product commits in range are `48420340` (unit 1, the instruction at
every carrier), `d7caa426` + `26724f49` (unit 2, the spec gate's `bar` join and its Date gate) and
`7e9bbeff` (unit 3, the act refusal `gate-guard.js`); the records under
`memory/builds/aDeferredBar/` are part of the diff. **Round: 1.**

## Verdict: CLEAN WITH FIXES

No blocker, two highs, four mediums, five lows, after consolidating the fifteen confirmed arrivals
into the eleven distinct defects below. One of the highs is a red merge-bar leg at HEAD, so the fold
is not optional: nothing lands until `tools/install-prefix-carried.txt:126` is re-keyed, and the
bar itself refuses the landing until it is. It is a high and not a blocker because the review adds
nothing by holding the loop open on a defect a machine already refuses and a one-number row edit
clears; severity here follows the shape of the fix, not the colour of the bar. The other high is a
coverage gap against the owner's mandate: both new machine readers spell "self-test suite" as the
`.test.sh` filename convention, and the manifest's fourteen python `selftest.py` legs, the govkit one
at 3445 s among them, walk past both.

**Review shape.** Raw 18, confirmed 15, refuted 3, unverified 0, precision 0.83. The fifteen
confirmed arrivals collapse to eleven: the install-prefix row arrived three times (ids 3, 8, 15), the
quoted-empty `BAR` token twice (6, 18), and the missing UNWIRED arm twice (7, 17).

**Run integrity.** Lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates dropped by the harness.
The finding set is therefore complete for what four lenses can reach, and a zero below is evidence
within that coverage rather than an artefact of a dead lens. What no lens could reach is stated
where it matters: the PowerShell arm of the hook has one suite arm and it exercises D4, so F8 was
found by reading, not by a failing arm.

## Findings, severity-ranked

| # | Sev | Where | Defect |
|---|-----|-------|--------|
| F1 | HIGH | `tools/install-prefix-carried.txt:126` | Row pins 37 literals for `gate-guard.test.sh`; the suite carries 39; `install-prefix (shipped surface)` is RED at HEAD |
| F2 | HIGH | `tools/unattended/gate-guard.js:203`, `tools/check-spec-tokens.py:110` | Both readers spell "suite" as `*.test.sh`; fourteen `chunk = selftests` legs are `python … selftest.py` and pass both |
| F3 | MEDIUM | `tools/check-spec-tokens.py:84` | The `bar` join grades LIVE specs only; the unattended workflow closes every unit spec before the first bar, so its graded population is empty by construction |
| F4 | MEDIUM | `tools/check-spec-tokens.py:262` | The Date gate finds the setting commit with `git log -1 -G`, which a later move or requote of the line re-dates; the gate then refuses a value that was never re-set |
| F5 | MEDIUM | `tools/unattended/adopt-unattended.sh:340` | Wiring arm greps a hardcoded `$ROOT/.claude/settings.json`, ignoring `GOV_SETTINGS_JSON`, and accepts the marker under any event or matcher |
| F6 | MEDIUM | `tools/unattended/adopt-unattended.test.sh:48`, `:88` | The UNWIRED refusal has no regression arm; the seed comment promises one that does not exist |
| F7 | LOW | `tools/unattended/gate-guard.js:118`, `:228` | A double-quoted `$( … )` is blanked as string content; `timeout -k 5 120` and `stdbuf -oL` make the option the head — three corpus RUN shapes pass |
| F8 | LOW | `tools/unattended/gate-guard.js:195` | `FLAG_RE` matches only the POSIX spelling, so `$env:GATE_SELFTESTS=1; bash …` passes under the PowerShell tool the hook is wired on |
| F9 | LOW | `tools/check-spec-tokens.py:113` | `GATE_(?:FULL\|SELFTESTS)=\S` reads `GATE_FULL=""` as a HIT; the hook reads the same token as OFF |
| F10 | LOW | `tools/check-spec-tokens.py:167`, `:273` | A non-ISO `SPEC_DIRECT_CUTOFF` is neither refused nor able to arm a spec; the join reports as set while grading nothing |
| F11 | LOW | `tools/unattended/adopt-unattended.sh:337` | An absent `gate-guard.fragment.json` falls through to `in sync`, a skip that reads as a pass |

## F1 — the ratchet row is two literals behind the suite it counts (HIGH)

`bash tools/check-install-prefix.sh` on the clean tip prints `ROSE tools/unattended/gate-guard.test.sh
37 -> 39` and exits 1. The hand-written row at `tools/install-prefix-carried.txt:126` says 37; the
rev-5 `bash -n` / `bash -x tools/unattended/gate-guard.test.sh` arms at `gate-guard.test.sh:141-142`
carry two more, and `git show --stat 7e9bbeff` confirms row and arms landed in the one commit. The
leg at `tools/gate-legs.json:939` is `subject: repo`, `chunk: product`, no guard, so it runs on every
bar: the VERIFYING run the main loop owes and the lander's pre-push bar both red on this tip. The
unit-3 ledger's AC9 line records `exited 0` for a 37-literal tree the committed suite never had —
the amendment-leaves-its-other-half-standing class, and the same one round 2 of the spec audit
called out in the specs.

- **Fix.** Re-key the row to 39 by hand, appending the reason (the two rev-5 syntax-check payloads
  spell the suite path as a command string), re-run the checker to exit 0, and amend the AC9 ledger
  line to the count it now observes.
- **Left-shift.** The row is a ratchet and the bar caught it, which is the gate working. What let it
  land is the ledger asserting a leg's exit for a tree that moved afterwards: the memory-tree
  ledger grammar could carry the sha an observation was taken at, and the closing review's DoD could
  refuse a ledger line whose observed exit disagrees with the leg at HEAD. Cheaper and honest today:
  a `memory/gotchas/` entry for "an acceptance observation taken before the last fold of the same
  commit is an observation of nothing".

## F2 — "every self-test suite" means `*.test.sh` to both readers (HIGH)

Reproduced with `RUN.md` at REVIEWING on this branch: the hook exits 2 for `bash
tools/unattended/unattended.test.sh` and 0 for `python tools/govkit/selftest.py`; `BAR` at
`check-spec-tokens.py:110-113` matches only `run-gates|run-selftests|run-unattended-gates|*.test` +
`.sh`. `tools/gate-legs.json` declares 52 `chunk = selftests` legs and fourteen of them are python
whole-suite runs — govkit 3445 s, drift-audit 755 s, memory-recall 656 s, lexicon 637 s in the gate
ledger — the largest suites the manifest holds. Reachability is not hypothetical: 79 specs under
`memory/builds/*/spec` name one of them and 39 acceptance ledgers record running one. The hook's
header says "every self-test suite"; its stated ceilings are run-time assembly and heredocs, and
neither spec §3 nor the corpus record names this shape as excluded. Caveat kept: unit 1's child
prompt admits a bare `--selftest` flag as a direct check, which is right for the seconds-long
`sh_hygiene.py --selftest` class, but a whole-suite `selftest.py` file is not that class.

- **Fix.** Add a `selftest\.py` word shape to `resolveFileRow` (D4) and to `BAR`'s alternation,
  keeping bare `--selftest` flags admitted; one deny arm in `gate-guard.test.sh`, one HIT arm in
  `check-spec-tokens.test.sh`. Update the hook header's D4 row to say what it now spells.
- **Left-shift.** Derive the shape set rather than restate it: a parity arm that reads every
  `chunk = selftests` argv basename out of `tools/gate-legs.json` and asserts each is matched by
  the hook's deny rows and by `BAR`, so a new suite convention cannot drift out of both readers
  again. The manifest already owns the population; this is the two-readers-of-one-population class
  `tools/check-playbook-parity.sh` exists for.

## F3 — the join's population is empty for the workflow it was built for (MEDIUM)

The `bar` join reads specs matching `LIVE` (`OPEN|SPECCED|INPROGRESS|BLOCKED`,
`check-spec-tokens.py:84`, selected at `:223`). Its only invoker is the `spec tokens` leg; pre-commit
does not run it, and `unattended.sh` runs `$GATE_CMD` only inside `--close`. On this branch
`unattended-unit.js:156-162` forbids any bar in a unit pass and orders the spec header to CLOSED in
the unit's own commit, and `GROUND` says the bar runs once at the main loop after the last unit is
terminal. So for an unattended build every unit spec is frozen by the first bar that could grade it,
and the population the join was built for — "the writer, before any child agent reads it", spec 2
§1 — is empty by construction. What is left to it: an attended build, a BLOCKED unit, or a
discretionary plain bar between SPECCING and BUILDING. The spec's rejected-alternatives list never
prices this. Medium and not higher because the act refusal (unit 3) is the compensating control at
exactly the point the join goes dark, and the join still grades attended builds.

- **Fix.** Give the join a population that exists when it runs: grade a spec regardless of status
  when its path is in `git diff --name-only <merge-base>..HEAD -- memory/builds/*/spec/` (a spec this
  branch authored is not a frozen record from the branch's side); or have `unattended-build.js`
  run `python tools/check-spec-tokens.py` in `--dispatch` before handing a unit its brief — a direct
  check in seconds, allowed by the hook, and the one place that sees every live spec before its
  unit builds.
- **Left-shift.** A self-test arm for `check-spec-tokens.py` that stages a CLOSED post-cutoff spec
  carrying a bar token on a branch where that spec is in the merge-base diff, and asserts a HIT; the
  arm is the failing case the join has never had for its own workflow.

## F4 — `-G` re-dates the setting commit on any later touch of the line (MEDIUM)

`check-spec-tokens.py:262` finds the setting commit with `git log -1 --format=%cs -G'^SPEC_DIRECT_CUTOFF="?<value>"?$'`.
`-G` matches any hunk that adds OR removes a matching line, so a block move, a requote from quoted
to bare, or a trailing-whitespace cleanup re-dates the "setting commit" to that later day, and
`direct_cut <= set_on` at `:273` refuses with a `carried across a day boundary` diagnosis that is
false. Confirmed in a scratch repo: committed 2026-09-14, line moved 2026-09-20, checker refuses.
The leg is unguarded and on every bar; the only in-band exit is bumping the cutoff forward, which
silently drops every spec dated in between from the graded population. `.memory-tree.conf` has 171
commits; the four sibling cutoff lines each show one `-G` hit today, so this is deterministic and
moderately likely rather than imminent.

- **Fix.** Query the introduction, not the last touch: `git log -1 --format=%cs --pickaxe-regex
  -S'^SPEC_DIRECT_CUTOFF="?<value>"?$' -- .memory-tree.conf` (an occurrence-count change; a move or
  requote keeps the count and is not matched). Verified in the same scratch repo: 2026-09-14 after
  both the move and the requote.
- **Left-shift.** One suite arm that moves the line in a later-dated commit and asserts the gate
  still grades; it is the failing case the AC17 arm (genuine carried value) does not cover.

## F5 — the adopter's wiring arm reads one hardcoded path and any matcher (MEDIUM)

`adopt-unattended.sh:340` greps `$ROOT/.claude/settings.json` only. `tools/check-wiring.sh:57-84`
resolves `GOV_SETTINGS_JSON` first and documents an out-of-tree settings file as a legitimate
per-machine layout that is reported, not failed; its scratch, recall and agent-cap arms assert the
fragment's matcher group via `matchers_of`. At an adopter with settings declared out of tree the
unguarded `unattended skill wiring` leg (`kit.toml:170-175`) reds UNWIRED while check-wiring says
wired, and the printed remedy creates the in-tree decoy check-wiring's header warns about.
Conversely a marker parked under `PostToolUse` or another matcher passes this arm and never fires.
Weight kept honest: `tools/process-monitor/adopt-process-monitor.sh:192-205` already carries the
identical hardcoded grep on a bar leg, so this reproduces a class rather than inventing one, and
the any-matcher half needs a hand edit to reach.

- **Fix.** `SJ=${GOV_SETTINGS_JSON:-$ROOT/.claude/settings.json}`, and assert the marker inside a
  `PreToolUse` group whose matcher equals the fragment's, using the `matchers_of` shape
  `check-wiring.sh:157` already has.
- **Left-shift.** A check-wiring arm for the gate-guard fragment beside its scratch and recall
  siblings, so one resolver owns the settings path for every hook; then the adopter can delegate
  rather than re-implement, which also retires the process-monitor copy of the same defect.

## F6 — the UNWIRED refusal has no failing case, and the comment says it does (MEDIUM)

`adopt-unattended.test.sh:47-48` says "the UNWIRED arm below removes it and reads the refusal";
`grep -n UNWIRED` in that file finds only the comment. Both `--check` arms (`:88`, `:131`) run on
seeded, wired trees. `check-arms.py` discovers gates by a `fail() {` helper and `adopt-unattended.sh`
defines none, so the adopter sits outside that meta-gate too. Spec 3 §7 records `no new arm` and the
ledger's AC10 records the RED once, by hand. A regressed marker `sed` or a moved settings path would
report `in sync` over a hook that never fires, and nothing in the kit's suite would notice.

- **Fix.** Add the arm the comment promises, after arm 1: move `$A/.claude/settings.json` aside, run
  `--check`, assert rc 1 and stdout containing `gate-guard hook is UNWIRED`, restore; count it
  toward the suite's floor. Or reword the comment — but the arm is two lines and the observation
  already exists in the ledger, so add it.
- **Left-shift.** The `check-arms.py` population rule (`fail() {`) is what let a bar-leg script go
  ungraded; a second discovery signature for scripts that exit 1 with a printed reason would put
  every adopter's `--check` under the arms floor.

## F7 — three corpus RUN shapes pass the view (LOW)

Fed to the hook directly with this worktree's `cwd`, each exits 0 while the control
`bash tools/unattended/unattended.test.sh` exits 2: `printf 'rc=%s\n' "$(bash
tools/memory-tree/kit-dogfood-parity.test.sh …; echo $?)"` (a sidechain call, the population the
child prompt cannot reach), `timeout -k 5 120 bash tools/unattended/unattended.test.sh > …`, and
`(stdbuf -oL -eL bash tools/run-gates/run-gates.test.sh > …) &`. Causes: `buildCommandView` at
`:118-125` blanks a double-quoted `$( … )` as string content; the prefix grammar at `:228` admits
only `timeout <duration>`, so `-k` makes `timeout` the head; `stdbuf` is not a prefix word. The
corpus-measurement record (`build/2026-09-14-build-TOOL-aDeferredBar-3-2-corpus-measurement.md:64`)
says the post-rev-4 walk "finds ONE call"; that walk read only tokens surviving in the blanked view
and filed `-eL` and `120` as mention heads, so it undercounts the run-shaped near-misses it
certifies. Inside the header's stated ceiling (textual, fails open), so low.

- **Fix.** In the double-quote branch keep a `$(`…`)` span unblanked, tracking paren depth, so
  `scanSegments` reads the inner command; after `timeout`, skip `^-` words and `DURATION_RE` before
  looking for the launcher; add `stdbuf`, `nice`, `ionice` to the prefix words or skip `^-` options
  after them. Re-run the probe and correct the record's near-miss count and classification table.
- **Left-shift.** Three arms, one per shape, each asserting deny; and the corpus walk's own count
  asserted against a hand-classified sample, so the record cannot again certify a number the view
  could not see.

## F8 — the PowerShell-native flag spelling is not a hit (LOW)

`FLAG_RE` at `gate-guard.js:195` anchors on `^(GATE_FULL|GATE_SELFTESTS)=`. Under tool_name
PowerShell — the tool the hook is wired on, and this environment's primary shell — the POSIX
`NAME=value cmd` form is not valid syntax, so the one spelling that runs the flagged bar there is
`$env:GATE_SELFTESTS=1; bash tools/run-gates/run-gates.sh`, which exits 0 (reproduced, both `$env:`
forms) while the bare form exits 2. The header, README line 51 and the suite's own comment ("the
same act through the other shell") claim PowerShell coverage; the suite's only PowerShell arm
exercises D4. No live instance in the corpus, and not a runtime-assembled path: it is the second
tool's native shape.

- **Fix.** `FLAG_RE = /^(?:\$env:)?(GATE_FULL|GATE_SELFTESTS)=(.*)$/` — `readTokenAt` already strips
  the quotes, so `$env:GATE_FULL=""` still reads as the OFF spelling.
- **Left-shift.** Two arms under PowerShell: `$env:GATE_SELFTESTS=1; bash …` deny naming the token,
  `$env:GATE_FULL=""; bash …` allow.

## F9 — the two predicates disagree on the quoted-empty token (LOW)

`BAR.search('GATE_FULL=""')` and `BAR.search("GATE_FULL=''")` both return True — the quote satisfies
`\S` at `check-spec-tokens.py:113` — while `gate-guard.js` `readTokenAt` unquotes to `GATE_FULL=`
and allows, pinned at `gate-guard.test.sh:132`. The checker's own header says the empty assignment
is the OFF spelling, and spec 2 Fork E says the two predicates read the one token alike; both are
false for the quoted form. Reachable: a post-cutoff spec that backticks `GATE_FULL="" cat …` to
document the OFF form reds as `[bar]` with a message telling the author to remove a flag that is not
set. AC16 tests only the unquoted `GATE_FULL= cat …`.

- **Fix.** `GATE_(?:FULL|SELFTESTS)=["']?[^\s"']` so an empty quoted value is no hit and
  `GATE_FULL="1"` still is.
- **Left-shift.** The quoted-empty token beside AC16's bare-empty arm; better, one shared table of
  OFF spellings both suites read, since the disagreement is the two-readers class the spec claims
  it closed.

## F10 — a malformed cutoff is neither refused nor armed (LOW)

`read_conf_key` (`:167`) captures `[^"\n]*` and never asserts an ISO shape; the Date gate (`:273`)
and the arming test (`:284`) are raw string comparisons. With `SPEC_DIRECT_CUTOFF="2026-9-15"`
committed, `'2026-9-15' <= '2026-09-14'` is False (not refused) and `'2026-09-16' >= '2026-9-15'` is
False (never armed): exit 0, `0 token(s) examined in 0 live spec(s) at/after SPEC_DIRECT_CUTOFF
2026-9-15`, every carrier `predates`. The join reads as set while permanently off, the announced-zero
class the conf comment says it avoids, and the relation gate this unit added cannot fire on it.

- **Fix.** Right after the read, `REFUSING` when `direct_cut and not re.fullmatch(r"\d{4}-\d{2}-\d{2}",
  direct_cut)`.
- **Left-shift.** One arm committing `SPEC_DIRECT_CUTOFF="2026-9-15"` and asserting the refusal.
  The sibling cutoff keys in the conf deserve the same shape check; the preset block that refuses a
  future-dated `RECORD_SERVES_CUTOFF` is where it belongs.

## F11 — an absent fragment is a silent pass (LOW)

`adopt-unattended.sh:337` wraps the wiring arm in `if [ -f "$GG_FRAG" ]` and falls through to
`in sync` / exit 0. `KIT_DIR` is the script's own dirname, so the fragment is a sibling the `**`
engine rule and a `cp -r` both ship; absence is a broken copy, not a non-adoption. The five sibling
artifacts in the same `--check` branch (`:282-311`) each refuse with `<x> is missing`; check-wiring's
scratch and recall arms print an announced `skip … does not ship`; this arm is the only silent one,
and no other gate asserts the file's presence (`check-hook-destinations.sh` iterates tracked
fragments, so a missing one is not graded).

- **Fix.** Refuse — the fragment is part of the shipped surface — or at minimum print the announced
  skip the siblings print.
- **Left-shift.** Covered by F6's arm once the fragment is asserted rather than tested for; one
  arm that deletes the fragment from the installed copy and asserts a non-zero exit.

## What this review did not do

It did not run the merge bar or any self-test suite, per the mandate this build exists to enforce;
the only leg exercised is `check-install-prefix.sh`, a seconds-long direct check, and the hook was
exercised as a program on stdin rather than through a tool call. It did not re-open the three
refuted findings. It did not grade the records under `memory/builds/aDeferredBar/` beyond the two
ledger lines F1 and F6 cite. The `$env:` and `selftest.py` gaps (F8, F2) were found by reading the
predicates against the populations they claim, not by a failing arm — which is the point of F2's
left-shift: the population is declared in the manifest and both readers should be measured against
it rather than against a convention.

**Disposition.** Fold F1 first — the bar refuses everything until it moves — then F2 and F9 as one
edit to the two readers, F4 and F10 as two lines in the Date gate, F5, F6 and F11 as one pass over
the adopter and its suite, F7 and F8 as the view and the regex with their arms. Re-review the FIX,
not the diff again, per the method.
