**Serves:** diff-review TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7

# aReapedSpinner — Tier-2 closing diff review, round 2

*Adversarial pass over THE FOLD round 1 produced, not over the original diff. Node `a`, 2026-09-08. Four finder lenses, five skeptic batches, one synthesis. Round 1 returned 3 blockers and 4 highs across 19 defects at precision 0.92; this round reads the single commit that answered them and asks whether the answers are right. A round-1 finding is re-reported below only where the repair is INCOMPLETE or INTRODUCED something new, and each such row says which.*

**Range — ROUND 2**, `ed127313834f9cb9ca2d06996c361c1be221bf12...HEAD` (one build commit, `1b41afe9`; 22 files, 571 insertions, 60 deletions; 10 of those files are the code and the rest are records).

## Verdict: BLOCKED

Three blockers, and the shape of the round is worth stating before the table. **The repairs to the RUNNING code are good.** The `killable` flag now crosses every boundary it was dropped at, the type guard that enforces it has an observed failing case, the exotic-terminator fix is real and I staged the pre-fold parser to prove it, and `build_self_chain`'s new refusal is caught cleanly by all four of its callers. Round 1's D1, D4 and D5 are closed, and I checked each of them rather than taking the fold's word.

**What is not closed is everything the fold added AROUND that code.** All three blockers below live in `adopt-process-monitor.sh`, in the twenty-six lines the fold appended to it, and all three are the same defect class this build has now hit in four consecutive rounds: a check that reports rather than decides, or decides on something other than what it names. The new hook-wiring check computes the right number and then exits 0 with it. The new engine delegation cannot fail in the direction it was written for and fails in a direction nobody intended. And it reaches the engine through a bare `python`, the one launcher idiom this repo has a gate banning, on a leg that runs on every bar.

D3 is the fourth: it is repaired in two halves and a user profile passes both. `check_root_shape(['C:/Users'])` returns `['c:/users']` — absolute, and exactly `MIN_ROOT_LEN` long — and `C:/Users/daily-agent` is a real directory, so the adopter's `[ -d ]` test admits it too. The comment the fold wrote at `adopt-process-monitor.sh:92-95` says the `-d` test "is what refuses it". That is true only of the `John Doe` example it was written from.

Nothing here needs a unit re-scoped. Every fix is local and most are one or two lines. But three of them have to land before this build can, and four merge-bar legs are red independently of anything in this report.

### Review shape

Raw 31 · confirmed 26 · refuted 5 · unverified 0 · precision 0.84.

**Run integrity — all clean.** Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates discarded by the pipeline. No arm of this run failed to report, so the zero counts here are positive evidence rather than an absence of evidence, and the finding set is complete as far as four lenses reach. **This run is complete.**

**Consolidation.** The pipeline discarded no duplicates, but the 26 confirmed findings describe **15 distinct defects**: four lenses landed on the unwired-hook exit code from four sides, three on the bare `python`, two each on five more. Every row below carries its raw ids so nothing is lost, and a merged row takes the MAXIMUM severity in its cluster. One row, **R7, is NEW** — it came out of the fixture-weakening hunt rather than from a lens, and it has no raw id.

**Adjudicated totals across the 16 rows: 3 blockers, 3 highs, 6 mediums, 4 lows.** Severities are the ones adjudicated HERE, not the ones the lenses proposed. Two lens severities were lowered with the reason argued in place (R8, R11), and one raw claim was corrected outright (R14 — the arithmetic on that line does close; it is the label that lies).

| # | Sev | Address | Defect | Raw ids |
|---|-----|---------|--------|---------|
| R1 | BLOCKER | `scope.py:93` · `adopt:96` | The D3 repair is incomplete: a user-profile root passes BOTH new halves, and the fold's own comment certifies that it cannot | 1 |
| R2 | BLOCKER | `adopt:143-153` | The new hook-wiring check reports and never decides — the `process-monitor wiring` leg exits 0 with zero hook entries, and an arm PINS that exit | 4, 9, 16, 25 |
| R3 | BLOCKER | `adopt:157` | The new engine delegation gates on a bare `command -v python`, the retired idiom, and reports a launcher fault as a conf defect on an unguarded bar leg | 10, 18, 26 |
| R4 | HIGH | `adopt.test.sh` · `selftest.py:686` | The `[ -d ]` guard has no arm anywhere, and shipped prose in a sibling file certifies that the arm exists | 17, 27 |
| R5 | HIGH | `adopt:157-163` · `scope.py:271` | A declaration-grading leg now reds on LIVE MACHINE STATE and on path SPELLING, inside a ceiling smaller than the census it invokes | 5, 11 |
| R6 | HIGH | `adopt:159` · `scope.py:272` | The delegation's liveness assertion is satisfied by the checker being its own subject, so it cannot fail for the declaration the kit documents | 2, 19 |
| R7 | MEDIUM | `adopt.test.sh:38` | The fold narrowed the base fixture from two roots to one, so no arm grades a multi-root declaration any more — and multi-root is what makes R5 survivable | — |
| R8 | MEDIUM | `procmon-hook.fragment.json:3` | The new fragment declares `PostToolUse` only, so a fragment-wired adopter never gets the `SessionStart` entry the throttle bypass needs | 3 |
| R9 | MEDIUM | `adopt:16,151` | The fold added install-prefix literals to a file whose own header says none appear in it, one of them in operator-facing runtime output | 21, 28 |
| R10 | MEDIUM | `adopt.test.sh:85` | `test_short_root_refuses` now trips the new `[ -d ]` guard as well, so it can no longer isolate the length rule it is named for | 29 |
| R11 | MEDIUM | `census.py:172` | `parse_posix` was switched to `split("\n")` without the blank-line guard its two siblings kept, so the POSIX backend's `rejected` count is permanently ≥ 1 | 12, 22 |
| R12 | MEDIUM | `adopt.test.sh:53` | The delegation's FAILING side has no arm, and `FLOOR_ASSERTIONS` was pinned at exactly the count the suite already had | 6 |
| R13 | LOW | `scope.py:98` | The absoluteness test was inserted ABOVE the too-broad test, making the `norm in ("", "/", "c:")` tuple dead and giving drive roots a false reason | 14 |
| R14 | LOW | `reap.py:183` | `render_kill`'s `in scope` field prints the KILLABLE subset, so the withheld rows read as having been outside the fence | 24, 30 |
| R15 | LOW | `scope.py:210` · `selftest.py:700` | The docstring leads with LAST-WINS, which the refusal two lines below makes unreachable, and the arm named for it grades something else | 8 |
| R16 | LOW | `README.md:67` | The "What this kit does NOT check" bullet now disclaims a check that runs and exits 1 | 23 |

---

## State of the bar

Four merge-bar legs are RED on this tip. **All four were red at `ed127313` as well**, so none is a regression from this fold — but two of them the fold made worse, and the build cannot land with any of them red.

| Leg | Subject / guard | Status | This fold's contribution |
|---|---|---|---|
| `python resolver (behaviour + inline parity + idiom ban)` | kit, guard `tools/` | RED | Added a third ban hit — R3. The other two (`run-selftests.sh:37`, `run-gates.test.sh:1598`) predate the range; I confirmed both with `git show ed127313:`. |
| `install-prefix (shipped surface)` | repo, unguarded | RED — `UNRECORDED tools/process-monitor/adopt-process-monitor.sh 5` plus five sibling files | Widened the adopter's count — R9. The kit has ZERO rows in `tools/install-prefix-carried.txt` and that file is not in the diff, so the leg was red at base. |
| `codebase-map coverage + freshness` | repo, unguarded | RED — `kits: ['process-monitor']` and three `gate-legs` keys UNCLAIMED, `generated/inventories.json` STALE | None. The committed `memory/map/generated/inventories.json` carries zero process-monitor entries and is not in this diff, so this is an open DoD item the fold did not touch. |
| `memory hygiene` | repo, unguarded | RED — `TOOL-aReapedSpinner-6` §3 declares **hands-off** `-7` with no matching **consumes-from** back, and check 23 reports every AC of all seven units as evidenced by no journal record | None, and both are records-side DoD items rather than code. |

**One thing this record itself owes.** Adding this file drifts the derived build index — `gen_build_index.py` only sees TRACKED files, so the drift appears the moment it is `git add`ed and not before. Whoever commits it runs `python tools/memory-tree/gen_build_index.py --write` in the same commit, or `memory hygiene` gains a fifth reason to be red that this review created.

Green and verified by me on this tip: `process-monitor census selftest` (57 passed, 0 failed), `process-monitor adopter selftest` (26 passed, 0 failed, floor 26), `lexicon` (coverage 99.4%, P2 offenders 0), and `process-monitor wiring` — which exits 0 in 1.7 s and, per R2 and R6, is a leg two of whose three assertions cannot fail.

---

## What I checked and found CLEAN

Stated because a closing review that reports only defects tells the reader nothing about the repairs it was sent to grade.

**The `run_kill` signature change is complete.** `scope_set` → `scope` at `reap.py:86`. Both real call sites (`reap.py:232` in `run_sweep`, `reap.py:322` on the explicit `--kill` path) pass the mapping. Nothing anywhere in `tools/` still passes a set: the only surviving `scope_set` token in the tree is the arm NAME `test_member_outside_the_scope_set_is_dropped` and prose in the round-1 record and the specs. All fourteen selftest call sites route through the new `build_scope` helper, and the type guard at `reap.py:98-102` has its own arm with an observed failing case.

**The `withheld` key breaks no reader.** Its only consumer is `render_kill`, which reads it through `.get(…, ())`. `render_sweep` renders each report through `render_kill`, so the sweep path — the one the hook actually drives — surfaces the count per target rather than swallowing it. No external consumer parses that header line: `procmon-hook.js` matches only `/^(ORPHAN|SPIN|IDLE|UNKNOWN)\s/`, and `run-gates.sh`'s `run_leg_reap` pipes the whole thing through `sed`. The only defect here is the label, R14.

**The three renames are complete.** `touch` → `writeStamp` (`procmon-hook.js`), `reap_leg_tree` → `run_leg_reap` and `reap_outstanding_legs` → `run_outstanding_reap` (`run-gates.sh`), `_hookrun` → `run_hook` (the adopter suite). Grepped the whole tree for all four old spellings: no stale caller, no stale reference in a dossier under `memory/map/`, and — the one that would have been silent — the run-gates canary's `sed -n '/^run_leg_reap() {/,/^}/p;…'` extraction at `run-gates.test.sh:1603` was updated for both names, so the arm still eval-loads real function bodies rather than an empty string. The lexicon leg grades all three and is green.

**`build_self_chain`'s new refusal breaks no legitimate caller.** Four callers: `classify.py:103` (catches `ScopeRefused` at `:105` and refuses with its own message), `scope.py:265` (caught at `:267`), and `reap.py:219` / `reap.py:319`, both inside `main`'s try, which catches `ReapRefused`, `OSError`, `ValueError` and then `Exception`. No caller previously got a USEFUL empty set — the old code returned a singleton `{winpid}` containing an id the census does not know, which is precisely the silent-wrong-direction failure the refusal replaces. Strictly an improvement.

**Round 1's D1 is COMPLETE.** I traced every path that can reach a signal, not just the two the fold names.

- `run_kill` grades the walk ROOT on `killable` at `reap.py:110-115` and partitions the walked set at `:120-124`, so a non-killable descendant is withheld rather than signalled. Staged: a four-row tree with node 3 marked unkillable returns `kill_set [4, 2, 1]`, `withheld [3]`.
- `run_sweep` filters its target list on `killable` at `reap.py:227-228`, as it already did, and now hands the mapping through.
- `--kill` and `--kill-msys` at `reap.py:322` both pass the mapping, so the comment at `:321` — "The explicit path bypasses the MODE, never the FENCE" — is now true, which round 1 recorded that it was not.
- `run-gates.sh`'s delegation reaches the reaper as `--kill-msys "$_rlt_pid"` at `run_leg_reap:1573/1576`. A leg is a SIBLING of the `reap.py` the teardown spawns, never an ancestor, so it grades killable and the gate runner's own reaping is unaffected by the new refusal. I checked this rather than assuming it, because a fence that refused the runner's own legs would have been a silent regression in the one path this build exists to fix.
- `remove_descendants` still runs unconditionally after the delegation at `run_leg_reap:1580` and does NOT consult the fence. That is unchanged in this range and is bounded by construction — it walks only a pid the runner itself wrote to `$WORK/*.pid` — so it is noted, not filed.

**Round 1's D5 is COMPLETE and is the one repair in this fold with a genuinely observed failing case.** I staged the pre-fold parser inline and ran both against the same forged input across all eight separators `str.splitlines()` breaks on that the CIM query does not emit. Under `splitlines()`, every one of the eight forges a row for winpid 9999 with `rejected` still 0. Under `text.replace("\r","").split("\n")`, none of them does. The arm `test_exotic_line_terminators_cannot_forge_a_row` tables all eight rather than testing one, which is the right shape.

---

## Blockers

### R1 — the D3 repair is incomplete: a user profile passes both halves

**BLOCKER** · `tools/process-monitor/scope.py:93` and `tools/process-monitor/adopt-process-monitor.sh:96` · raw id 1

The fold split D3's fix across the two readers: the engine refuses a non-absolute root, the adopter refuses a non-directory one. There is a root shape that passes both.

Reproduced on this node. `check_root_shape(['C:/Users'])` returns `['c:/users']` — it starts with `[a-z]:/` so the new absoluteness test admits it, and it is exactly eight characters, so `len(norm) < MIN_ROOT_LEN` is false by one. `check_root_shape(['C:/Users/daily-agent'])` and `check_root_shape(['C:/Users/john'])` pass for the same reason with room to spare. And a profile directory is a real directory, so `[ -d "$_r" ]` is true.

I staged the whole adopter against `PROCMON_ROOTS="C:/Users/daily-agent"` in a scratch repo carrying the engine. It prints `declaration ok`, then `the engine's own reader agrees, and those roots admit live work on this machine`, and exits 0.

The consequence is the property this build exists for. The shipped conf's default is `PROCMON_REAP_MODE="reap-orphans"`, and the conf's own prose records 18 parentless rows over an hour old on this machine including Spotify and msedge — Spotify lives under `C:/Users/<u>/AppData`. A fence declared at the profile makes every one of those an irreversible kill target once it clears the 4 h ceiling.

What makes this a blocker rather than a high is the comment. `adopt-process-monitor.sh:92-95` states that the `-d` test "is what refuses it". That is true of `C:/Users/John` — a fragment left behind by whitespace-splitting a name WITH a space — and false of every profile directory whose owner's name has none. The repair certifies coverage it does not have, in the file that performs it, which is the class §7 calls a gate satisfied by its own comment prose.

**Fix.** In `check_root_shape`, after the absoluteness test, refuse a root that is equal to or an ancestor of the user profile — `build_normalized(os.path.expanduser('~'))`, plus `%USERPROFILE%` and `$HOME` where set — and require at least two path segments below the drive or UNC root, which `c:/users` does not have. Leave the adopter delegating rather than restating the rule. Then rewrite the comment at `:92-95` to say what the `-d` test actually catches, which is the relative fragment, not the prefix.

**Left-shift.** A `selftest.py` arm feeding `check_root_shape` a table of profile-shaped roots — `C:/Users`, `C:/Users/<name>`, `os.path.expanduser('~')`, and the UNC and `$HOME` spellings — asserting the refusal SUBSTRING per input rather than "something refused" (see R13, which is the same arm's existing weakness). The arm belongs in the engine because the engine is where the rule can be stated once for both readers.

### R2 — the wiring leg reports and never decides, and an arm pins the permissive exit

**BLOCKER** · `tools/process-monitor/adopt-process-monitor.sh:143-153` · raw ids 4, 9, 16, 25

`_hook_n` is computed at `:143-147`, and when it is zero `:151` calls `print_note` — which writes to stdout and touches nothing else. `FAIL` is never set. Control falls through `declaration ok` to `exit 0`.

Staged twice, in scratch repos with no `.claude/settings.json` at all:

```
process-monitor: the engine is configured but the HOOK IS NOT WIRED — nothing will report a hung process to a session. …
process-monitor: declaration ok — … hook entries 0
EXIT=0
```

The leg is `{"name": "process-monitor wiring", "chunk": "records", "subject": "repo", "ceiling": 60}` with no guard, so it runs on every bar and prints a green row whose NAME promises the wiring is present. Three separate statements in the tree contradict that: the file's own exit contract at `:22` says `1 = unwired or refused`; the block's own comment at `:141-142` says "A leg whose name overstates what it checks is worse than no leg"; and `kit.toml`'s new comment says declaring the fragment "moves this kit into a gate that exists" — but that gate is `check-hook-destinations.sh`, whose header at `:14-17` explicitly disclaims the question, and `tools/check-wiring.sh` has no procmon token anywhere in it.

This is round 1's D6 with the message repaired and the verdict left alone. It is a blocker for a second reason: the new check has never been observed failing, and one arm actively certifies the failing state as acceptable. `run_against` (`adopt-process-monitor.test.sh:52-59`) creates a scratch repo with no `.claude/settings.json`, so `_hook_n` is 0 on **every** `run_against` arm, and `test_valid_conf_is_accepted` asserts exit 0 against exactly that state. The only two arms that see a settings.json read gov's real one and live in the kit's own suite, which is `subject: kit`, `chunk: selftests` — held by default and never shipped to an adopter. So in an adopter's repo an unwired hook reds nothing, ever.

**Fix.** Call `add_problem` rather than `print_note` when `_hook_n -eq 0`, and move the block above the `if [ "$FAIL" -ne 0 ]` report at `:134` so the existing exit path carries it. If declining the hook is meant to be legal, then change `:22` instead and rename the leg in `tools/gate-legs.json` to `process-monitor declaration` — but one of the two has to move.

**Left-shift.** Two arms, and the second is the one that matters. First, a `run_against` variant that writes a `.claude/settings.json` with no procmon entry and asserts exit 1 plus the message. Second, change `test_valid_conf_is_accepted` to write a settings.json that DOES carry the entry, so the happy path stops asserting that the unwired state is fine. Stage the break once against the current adopter to confirm the first arm reds.

### R3 — the delegation gates on a bare `python` and blames the conf for a launcher fault

**BLOCKER** · `tools/process-monitor/adopt-process-monitor.sh:157` · raw ids 10, 18, 26

```sh
if [ -f "$KIT_DIR/scope.py" ] && command -v python >/dev/null 2>&1; then
  if PROCMON_ROOT="$ROOT" python "$KIT_DIR/scope.py" --check-conf >/dev/null 2>&1; then
```

Mechanically: `bash tools/lib/resolve-python.test.sh` exits 1 and names this exact line — `FAIL the retired python-launcher idiom is back: tools/process-monitor/adopt-process-monitor.sh:157`. The base carried no `command -v python` in this file at all, so the fold added the hit. Every sibling adopter — codebase-map, drift-audit, lexicon, memory-recall, memory-tree, playbook — inlines the `resolve_python` block instead; this is the only one that does not.

Functionally, and this is the half that makes it a blocker rather than a lint. `tools/lib/resolve-python.sh` exists because the MS-Store stub answers `command -v` and then exits 9009 without running. On such a host the guard is satisfied, the child exits non-zero, and the else branch at `:161-162` prints "the engine's reader REFUSES this conf, or its roots admit nothing live here" and `exit 1`. An unguarded merge-bar leg reds, and the operator is sent to re-read a declaration that is correct. Because the call carries `>/dev/null 2>&1`, the actual error is discarded and cannot be recovered without re-running by hand.

There is a third state the same branch collapses. When `command -v python` is FALSE the else at `:165` prints "the engine is not installed here" — naming the wrong cause for a `scope.py` sitting in the same directory. Three distinct faults, two messages, and neither names the real one.

**Fix.** Inline the gated `resolve_python` block the sibling adopters carry (canonical copy `tools/lib/resolve-python.sh`; `resolve-python.test.sh` gates every inline copy byte-for-byte), then `PY=$(resolve_python) || PY=""`, gate on `[ -n "$PY" ]`, and invoke `"$PY" "$KIT_DIR/scope.py" --check-conf`. Drop the `2>&1` half of the redirect and print the child's stderr in the failure note. Give "no engine", "no usable python" and "the engine refused" three distinct messages.

**Left-shift.** The gate already exists and already reds — `python resolver (behaviour + inline parity + idiom ban)`. Nothing new is needed for the idiom. What IS missing is an arm asserting the three-way message split; add it to the adopter suite alongside R12's arm, with `PATH` shimmed to a `python` that exits 9009, and assert the message names the launcher rather than the conf.

---

## Highs

### R4 — the `[ -d ]` guard has no arm, and a sibling file certifies that it does

**HIGH** · `tools/process-monitor/adopt-process-monitor.test.sh` (absent) · `tools/process-monitor/selftest.py:685-688` · raw ids 17, 27

I read all 26 arms. They stage a blank root, the temp root, `/`, `/c/x`, a real deeper directory, the closed value sets, an absent conf, version markers, README presence, the shipped conf and the hook seam. None declares an absolute, ≥ 8-character path that is not a directory. Grepping the suite for `not a directory`, `nonexist`, `john`, `Doe` or `space` returns nothing.

The guard itself works — I staged `PROCMON_ROOTS="C:/Users/no-such-dir-here-at-all"` and it refuses with exit 1 and the right message. Nothing in the suite observes that, which is §7's rule verbatim: a new gate is not landed until its failing case has been observed. Deleting the `[ ! -d ]` block leaves all 26 arms green, because every remaining fixture is either a created directory or already refused by an earlier rule.

What raises this above an ordinary coverage gap is `selftest.py:685-688`, which states in shipped prose that the profile-prefix half "is the adopter's `[ -d ]` test that catches it, and that arm lives in adopt-process-monitor.test.sh". It does not. The declared engine/adopter split is a good design; the destination it names is empty, and the sentence makes the whole of D3 read as covered.

**Fix.** Add the arm and correct the prose:

```sh
check_equal "test_non_directory_root_refuses" \
    "$(run_against "$(build_base_conf | awk -v r="$REALROOT/does-not-exist" \
        '/^PROCMON_ROOTS=/{print "PROCMON_ROOTS=\"" r "\""; next} {print}')")" 1
```

plus a `grep -q "is not a directory"` reason arm, and raise `FLOOR_ASSERTIONS` accordingly. Stage the break by deleting the guard once, confirm both arms red, restore.

**Left-shift.** The class, not the instance: a sentence in a shipped file asserting that an arm exists elsewhere is unverifiable by construction. Prefer a comment naming the arm by its exact name and a suite-level check that every arm name cited in kit prose exists in the suite that claims it — one grep, and it catches this whole class rather than this one occurrence.

### R5 — a declaration-grading leg now reds on live machine state, and on path spelling

**HIGH** · `tools/process-monitor/adopt-process-monitor.sh:157-163` · `tools/process-monitor/scope.py:271-276` · raw ids 5, 11

`scope.py --check-conf` returns 1 when `not scope` — when the declared roots match no live process — and `scope.main` calls `census.scan_processes`, which raises `CensusRefused` when PowerShell is absent, when the CIM query errors, or on a timeout. The fold routed both of those into the exit code of a leg that is `subject: repo` with no guard, and whose name and message both say "declaration".

Staged: a conf declaring `<repo>/memory/archive` — a real, correctly-shaped, perfectly valid root that simply has nothing running under it — exits 1 with "the engine's reader REFUSES this conf, or its roots admit nothing live here".

And a second, sharper form nobody found. **The verdict turns on path SPELLING.** A scratch repo declaring its own kit directory in MSYS form (`/tmp/…/tools/process-monitor`) refuses, because the census's command lines carry Windows spellings that never match. The same declaration in Windows form (`C:/projects/…`) passes. gov survives only because `.process-monitor.conf` declares BOTH spellings of one root. An adopter who declares one — the obvious thing to do — gets a leg that reds forever with a message blaming their conf. This is why R7 matters.

The ceiling arithmetic is wrong in the same place. `gate-legs.json` declares this leg at 60 s; `census.BACKEND_TIMEOUT_S` is 90, and the `windows-join` backend makes two bounded calls (`census.py:232`, `:237`). The engine's own timeout refusal can therefore never surface through this path — the leg wall kills it first. Measured cost here was 1.7 s against the 60 s ceiling, so this is a construction fault rather than a live one, but it means the fold turned a pure-shell records leg into one that depends on live CIM state on every bar.

**Fix.** Separate the three outcomes instead of collapsing them into one exit 1. A `ScopeRefused` on the DECLARATION is a failure. A census refusal or an empty live match is machine state — print it as a note and do not fail the leg. If the empty-match case is meant to fail, re-declare the ceiling above `2 × BACKEND_TIMEOUT_S`. Either way, capture the child's stderr into the note (see R3).

**Left-shift.** An arm that copies `scope.py` and `census.py` into the scratch repo, declares a real directory nothing runs under, and asserts the chosen behaviour — the same arm R12 asks for, doing double duty. Plus one arm declaring a single-spelling root and asserting whichever verdict the fix chooses, so the spelling dependency is graded rather than discovered by an adopter.

### R6 — the liveness assertion is satisfied by the checker being its own subject

**HIGH** · `tools/process-monitor/adopt-process-monitor.sh:159` · `tools/process-monitor/scope.py:272` · raw ids 2, 19

The other direction of the same delegation cannot fail.

`check_is_root` admits any row whose command line carries a path token under a declared root. The adopter spawns `python "$KIT_DIR/scope.py"` with an ABSOLUTE path, so when the declared root contains the kit — the shipped declaration, and the only one the README describes — the checking process and the shells that spawned it seed the scope themselves. The `if not scope` branch then has no reachable failing case.

Decisive staging. I created `C:/projects/procmon-scratch-selfsat` seconds before the run, copied in the adopter and the engine and nothing else, declared that directory as the sole root, and ran `--check`:

```
process-monitor: declaration ok — … 1 declared root(s) … hook entries 0
process-monitor: the engine's own reader agrees, and those roots admit live work on this machine
EXIT=0
```

`scope.py` on the same root reports `3 of 331 in scope · 1 killable`. All three rows are the checker's own tree. There is no live work under that directory and there never was.

`killable > 0` does not rescue the assertion either: the census's own PowerShell child is a DESCENDANT of the checker, not an ancestor, so it grades killable. I confirmed that on gov's real conf — of 11 in-scope rows, 5 are the self chain and two more (the CIM PowerShell and a conhost) are the checker's own descendants marked killable.

The half that actually binds for gov's declaration is `check_root_shape`. The note credits the half that does not.

**Fix.** Either drop the liveness clause from `:159` and claim only what `check_root_shape` proves, or make `--check-conf` exclude the caller's own tree before testing emptiness — `derive_scope` already receives the self chain, and `build_walk(rows, os.getpid())` gives the descendants — so the answer is about the tree rather than about the process asking.

**Left-shift.** This is §7's could-not-fail class, and the general check already exists in principle: run a candidate gate predicate over the real tree before wiring it and print hits AND near-misses. Concretely, an arm asserting that `--check-conf` REFUSES a freshly created empty directory declared as the sole root. That arm fails today, which is exactly the point.

---

## Mediums

### R7 — the base fixture was narrowed from two roots to one

**MEDIUM** · `tools/process-monitor/adopt-process-monitor.test.sh:38` · NEW, no raw id

At `ed127313` the suite's base conf declared `PROCMON_ROOTS="C:/projects/somewhere-real /c/projects/somewhere-real"` — the two-spelling shape. At HEAD it declares a single `$REALROOT`, because the new `[ -d ]` guard would have refused the old literal. That is a fixture changed to make a repair pass, and it took real coverage with it: no arm grades a multi-root declaration any more, and `_roots_n` is 1 in every one of the 26 arms.

The two-spelling declaration is not incidental. It is what gov's own shipped conf uses, and per R5 it is the reason gov's `--check-conf` passes at all. The suite now grades the single-root case exclusively while the product ships the multi-root one.

**Fix.** Restore a second root to `build_base_conf` — `$REALROOT` plus a second created directory, or the MSYS and Windows spellings of the same path — and assert `2 declared root(s)` in the accepted arm's output.

**Left-shift.** Assert `_roots_n` in the happy-path arm rather than only the exit code. A count in the output that no arm reads is a count that can silently become 1.

### R8 — the fragment declares one event, and the throttle bypass needs the other

**MEDIUM** · `tools/process-monitor/procmon-hook.fragment.json:3` · raw id 3

`settings-merge.py`'s fragment schema is `{name, event, matcher, marker, hook_path}` — one event per fragment — and only three fragments are tracked, one per kit. So the command the adopter now prints at `:151` produces exactly one entry, `PostToolUse`.

`procmon-hook.js:107-110` disables the throttle on `SessionStart` deliberately, and its own comment says why: a fresh session inherits another session's stamp "and would otherwise report nothing, which is precisely how a two-day-old orphan goes unseen". A fragment-wired adopter never reaches that path. This repo hides it — `.claude/settings.json` carries both events, hand-wired before the fragment existed, and the kit's arm `test_session_start_ignores_the_throttle` invokes the hook directly rather than through the wiring, so it certifies a path no fragment-wired adopter has.

**Lowered from the lens's reading.** The loss is a DELAYED first report, bounded by `PROCMON_THROTTLE_S` (300 s in the shipped conf), not permanent blindness — the next `PostToolUse` past the window reports normally.

**Fix.** Ship a second fragment declaring `SessionStart`, add it to `kit.toml`'s `[[files]]` block, and name both in the remediation line. Alternatively have the adopter parse `settings.json` for the two events and report each separately, which R2's fix needs anyway.

**Left-shift.** Once R2 makes the check decide, make it decide per event: `hook entries 2/2` with the missing event named. A single count cannot express "wired for the wrong event".

### R9 — install-prefix literals added to a file whose header says none appear

**MEDIUM** · `tools/process-monitor/adopt-process-monitor.sh:16` and `:151` · raw ids 21, 28

`bash tools/check-install-prefix.sh` exits 1 reporting `UNRECORDED tools/process-monitor/adopt-process-monitor.sh 5`. The fold added two of those sites: the header at `:16` spells `tools/settings-merge.py` and `tools/process-monitor/procmon-hook.fragment.json` in full, and the runtime note at `:151` mixes the derived `$KIT_REL` for the fragment with a literal `tools/settings-merge.py` **in the same sentence**. An adopter installed at any other one-segment prefix is handed a command whose first half resolves and whose second half names nothing — the exact failure the file's own comment at `:39-41` claims cannot happen here.

§12 gates this as a BAN, not a ratchet: the writer may lower a count, never add one. Two corrections to the raw findings, neither of which overturns it — the verdict word is UNRECORDED rather than ROSE (the kit has zero rows in `tools/install-prefix-carried.txt`), and the leg was already red at base for this kit, so the fold widened a violation rather than creating the red.

**Fix.** `$(dirname "$KIT_REL")/settings-merge.py` at both sites — the sibling-kit prefix is derivable from `$KIT_REL`, and `check-wiring.sh:299` already solves the same problem with `first_of tools/settings-merge.py settings-merge.py`. Then add the kit's rows to the ratchet.

**Left-shift.** The gate exists and reds. What is missing is the kit's rows in `tools/install-prefix-carried.txt`, without which the ratchet grades a subset of itself and this file's count can rise again unnoticed.

### R10 — `test_short_root_refuses` can no longer isolate the rule it names

**MEDIUM** · `tools/process-monitor/adopt-process-monitor.test.sh:85` · raw id 29

Staged directly: `/c/x` now emits BOTH refusals — "is shorter than 8 characters" and "is not a directory" — and the arm asserts only the exit code. Neuter `MIN_ROOT_LEN` entirely and the arm still passes, certifying coverage of a guard it no longer exercises. Its two siblings, `test_blank_roots_names_the_key` and `test_temp_root_names_the_reason`, already grep their messages for precisely this reason.

**Fix.** One line, in the shape the suite already uses: a `grep -q "shorter than"` assertion beside the exit-code check. Or point the fixture at a real short directory so only the length rule can fire.

**Left-shift.** The general rule this arm violates is that an exit-code-only assertion cannot distinguish two refusals. Where a checker has more than one independent `add_problem` reachable from one fixture, the arm asserts the MESSAGE.

### R11 — `parse_posix` lost the blank-line guard its two siblings kept

**MEDIUM** · `tools/process-monitor/census.py:172-173` · raw ids 12, 22

Confirmed by execution against the current file. `parse_posix(header + row + "\n")` returns one row with `rejected=1`; the same text without the trailing newline returns `rejected=0`. Real `ps` output always ends in a newline, so on the POSIX backend the reported rejection count is permanently ≥ 1.

The pre-fold code used `text.splitlines()[1:]`, which drops the trailing empty element, so this is a regression introduced by the D5 terminator fix — the fix was correct and its blank-line guard was applied to two of the three parsers. `parse_cim:91` and `parse_ps_w:122` both kept `if not line.strip(): continue`; `parse_posix` never had one because it never needed one. The empty line now falls into the `len(parts) < 4` branch at `:174`.

`rejected` flows through `measure_rows` into `render_rows`' summary, so a genuine malformed row is indistinguishable from the artifact — the same "trains the operator to ignore the field that matters" argument `reap.py` makes for its own `already_gone` branch, in a kit whose stated discipline is that no count it reports is authored.

**Lowered from the lens's reading.** Nothing gates on the figure and the parsed rows are correct; the harm is a permanently wrong derived number on the POSIX path.

**Fix.** `if not line.strip(): continue` as the first statement of the loop body, matching `:91` and `:122`. Then append `"\n"` to the fixture in `test_posix_fixture_collapses_both_namespaces` (`selftest.py:138-143`) so the arm grades real `ps` output shape and still expects `rejected == 1` from its deliberate junk row.

**Left-shift.** An arm that runs all three parsers over the same trailing-newline-terminated input and asserts `rejected == 0` for each — a table, not three separate arms, so a fourth parser cannot be added without joining it.

### R12 — the delegation's failing side is unarmed, and the floor was pinned at the existing count

**MEDIUM** · `tools/process-monitor/adopt-process-monitor.test.sh:53` · raw id 6

`run_against` copies only `$ADOPT` into each scratch repo, so `[ -f "$KIT_DIR/scope.py" ]` is false on every fixture arm and all of them take the "NOT CHECKED" path — I reproduced that output. `test_shipped_conf_is_accepted` (`:130`) runs from `$ROOT` and DOES exercise the delegation's success side, so the branch is not entirely dark; it is the FAILING case, and the new `exit 1` at `:162`, that has never been observed.

Sharper than the raw finding, and worth recording: with `scope.py` copied into a scratch repo, the happy-path arm's own fixture — a conf declaring the freshly created, empty `$REALROOT` — makes the adopter exit 1. `test_valid_conf_is_accepted` is green only because the engine is absent from the scratch repos. Fix R5 or R6 and that arm starts failing for a reason nobody put there.

`FLOOR_ASSERTIONS=26` is exactly the count the suite already executes, so the floor detects a truncated run but ratchets nothing new.

**Fix.** One arm that copies `scope.py` and `census.py` alongside the adopter, points `PROCMON_ROOTS` at a real directory nothing runs under, and asserts the behaviour R5's fix chooses. Raise the floor with it, and stage `test_valid_conf_is_accepted` with the engine present once, to see which way it goes.

**Left-shift.** A structural arm asserting that at least one `run_against` fixture carries the engine — otherwise the suite's coverage of every engine-gated branch is zero and nothing says so.

---

## Lows

### R13 — the absoluteness test was inserted above the too-broad test

**LOW** · `tools/process-monitor/scope.py:93-101` · raw id 14

Confirmed by execution: `check_root_shape` raises "is not an absolute path" for `/`, `c:`, `C:/` and `C:\`. `build_normalized` rstrips trailing separators so nothing can normalize to `"/"`, and `""` and `"c:"` fail the new test first — the entire `norm in ("", "/", "c:")` tuple at `:98` is dead. For a drive root the emitted reason is factually false (`C:/` IS absolute) and the message then talks about whitespace-splitting, pointing the operator away from the real objection, which is breadth.

All four still refuse, so the impact is a wrong message and a tuple that reads as coverage it no longer provides. `test_root_that_claims_everything_refuses` (`selftest.py:351-359`) records only "refused"/"admitted" and passed straight through the change.

**Fix.** Move the absoluteness test BELOW the length test so a drive root gets the breadth message, and drop the tuple members the length test already covers.

**Left-shift.** Extend that arm to assert the refusal SUBSTRING per input rather than the fact of refusal — the same change R1's left-shift needs, in the same arm.

### R14 — `render_kill`'s `in scope` field prints the killable subset

**LOW** · `tools/process-monitor/reap.py:183-186` · raw ids 24, 30

Staged: `reap: DRY RUN target 1 · walked 4 · in scope 3 · dropped 0 · withheld 1`.

**Correcting raw id 30, which claimed the arithmetic no longer closes.** It closes — 4 = 3 + 0 + 1. What is wrong is the LABEL. `withheld` rows are in scope by construction (`:123`: in scope and not killable), so a line that prints the killable subset under the name "in scope" tells the reader those rows were outside the fence when they were inside it and deliberately spared. The word also collides with the sibling module: `scope.py:197` defines `in_scope` as every admitted row and reports `killable` as a separate field, so one term names two populations inside one kit.

This is the one line a human reads before deciding whether a reap did what they expected, which is why it is filed rather than ignored.

**Fix.** Rename the field to `killable` in the format string, so `walked = killable + dropped + withheld` reads as an identity and the kit's two modules agree on what `in scope` means.

**Left-shift.** An arm asserting the identity on the rendered STRING — parse the four integers out of the header and check they sum — so the label and the arithmetic cannot drift apart again.

### R15 — LAST-WINS is unreachable, and the arm named for it grades something else

**LOW** · `tools/process-monitor/scope.py:210` · `tools/process-monitor/selftest.py:698-701` · raw id 8

`hits` collects every line starting with `PROCMON_ROOTS=`; `len(hits) > 1` raises. So `hits[0]` is always the sole element and last-of-many is unreachable by construction — verified by execution. The docstring at `:210` nonetheless opens with "LAST-WINS", describing behaviour the refusal two lines below makes impossible, in the module whose entire subject is two readers disagreeing.

`test_read_roots_is_last_wins` feeds one comment plus one assignment, so it grades comment-skipping and single-assignment parsing. The parse is correct; the name and the docstring are not.

**Fix.** Drop "LAST-WINS" from the docstring — the refusal IS the behaviour — and rename the arm to `test_read_roots_skips_comments_and_takes_the_single_assignment`.

**Left-shift.** Ungateable in general, so it belongs on the §10 checklist as a class: when a refusal is added above a behaviour, the docstring that described the behaviour is now a claim the code contradicts.

### R16 — the README disclaims a check that now runs and reds

**LOW** · `tools/process-monitor/README.md:67` · raw id 23

The bullet reads: "The adopter's `--check` grades the DECLARATION, not the result. Whether your roots actually admit your own work is a separate arm, because answering it needs a census and a closure." That is exactly what `--check` was just made to do — `scope.py --check-conf` runs the full census and closure and returns 1 when the roots admit nothing. The README is untouched by the fold; its last commit is `ed127313`.

The bullet sits under "What this kit does NOT check", the section an adopter reads to decide what a green wiring leg proves, so it now disclaims a check that runs and can red the bar, and says nothing about the liveness claim's self-satisfying shape (R6). An adopter under-trusts a refusal and over-trusts the pass.

**Fix.** Rewrite it to say that `--check` delegates the roots question to the engine's own reader and exits 1 on a refusal, and state what that answer does NOT prove — that the checker is itself in scope. Add the `settings-merge.py --fragment` step to the "Adopting it" block at `:30-37`, which still lists no wiring step at all.

**Left-shift.** A doc-freshness check cannot read prose, so this is a §10 checklist entry rather than a gate: when a `--check` gains a behaviour, the kit README's "does NOT check" section is part of the diff.

---

## Method and evidence

Four finder lenses over the fold's diff at an immutable SHA, five skeptic batches prompted to refute, one synthesis. Raw 31, confirmed 26, refuted 5, unverified 0 — precision 0.84, down from round 1's 0.92, which is the expected direction over a small repaired surface: the lenses were re-reading code another pass had already hardened, and the refuted five were all claims about behaviour the fold had already fixed.

Everything asserted above was re-derived here rather than taken from a lens. In particular I staged, on this node:

- `check_root_shape` over nine root shapes, and the full adopter against five confs, including the user-profile widening and the non-directory refusal.
- The unwired-hook exit code, twice — engine absent and engine present.
- The self-satisfying liveness assertion, against a directory created seconds earlier containing nothing but the kit.
- `parse_posix` and `parse_cim` with and without a trailing newline.
- The pre-fold `splitlines()` parser inline against all eight exotic separators, to confirm the terminator fix has a real failing case.
- `render_kill` over a four-row tree with one withheld member.
- `bash tools/lib/resolve-python.test.sh`, `bash tools/check-install-prefix.sh`, `python tools/codebase-map/test_codebase_map.py`, `python tools/lexicon/lexicon.py`, `python tools/process-monitor/selftest.py`, `bash tools/process-monitor/adopt-process-monitor.test.sh`, and the `process-monitor wiring` leg itself.

Two claims I could NOT settle and am not asserting. I did not run the full bar, so the four red legs above are the ones I ran individually and not necessarily the complete red set. And I established that all four were red at `ed127313` by reading the base blobs, the ratchet files and the committed generated artifacts rather than by checking the base tree out and running the legs there — the reasoning is stated per leg in the table so a later reader can disagree with it.
