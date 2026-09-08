**Serves:** diff-review TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7

# aReapedSpinner — Tier-2 closing diff review, round 1

*Adversarial pass over the shipped code for `tools/process-monitor/` and the `run-gates.sh` change that drives it. Node `a`, 2026-09-08. Four finder lenses, five skeptic batches, one synthesis. The three spec audits that preceded this one graded documents; this one grades what was built from them, and every defect below is in software that runs. Findings already folded and recorded in the specs' §9 are not re-reported here — the two places where a FOLD is itself wrong are called out as such.*

**Range — ROUND 1**, `e2b82a53dd8e9e422aea96bd57bcf6e63b5eb96c...HEAD` (45 files, ~6000 insertions, seven build commits `3f798808`..`ed127313`).

## Verdict: BLOCKED

Three blockers. One of them is arithmetic rather than judgement: `bash tools/check-testsuite-counts.sh` exits 1 on this diff, so the merge bar is RED and the push boundary blocks regardless of anything else in this report. The other two are the question this review was sent to ask. **The fence does not hold at the only place that signals.** `derive_scope` computes a per-row `killable` flag and every `run_kill` call site throws it away by passing `set(scope)` — the dict KEYS — so the self-chain protection, the single property standing between `reap-orphans` and the caller's own session, is read in exactly one function and is absent from the explicit `--kill`/`--kill-msys` path that `run-gates.sh` drives programmatically from a pid file. Reproduced live on this node: 4 self-chain rows in scope with `killable=False`, all four accepted as walk roots, the calling python's own winpid in `kill_set` every time. Separately, the root tokenizer splits a declared root on whitespace and `check_root_shape` never tests absoluteness, so an ordinary Windows profile with a space in it — `C:/Users/John Doe/...` — silently widens the fence to the real ancestor prefix `c:/users/john`, and the adopter's own `--check` word-splits identically and passes both halves.

The three safety defects compound rather than stack independently. D3 widens the fence, D1 removes the one exclusion inside it, and D4 makes the caller's protection collapse to a singleton on any MSYS python — which `tools/lib/resolve-python.sh` reaches first by trying `python3`. Each is individually a small fix; together they are the kit's entire safety argument.

Nothing here needs a unit re-scoped or an architecture revisited. Every fix is local, most are one or two lines, and the four defects that matter most are all the same shape: **a property computed in one module and discarded at the boundary into the next.** `killable` is computed and dropped, the conf is parsed by two readers that disagree, the census is produced with one line terminator and consumed with another, and the hook is written but never wired. The design survives this review; the seams do not.

### Review shape

Raw 36 · confirmed 33 · refuted 3 · unverified 0 · precision 0.92.

**Run integrity — all clean.** Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates discarded by the pipeline. No arm of this run failed to report, so the zero counts here are positive evidence rather than an absence of evidence, and the finding set is complete as far as four lenses reach. **This run is complete.**

**Consolidation.** The pipeline discarded no duplicates, but the 33 confirmed findings describe **19 distinct defects**: three lenses landed on the discarded `killable` flag from three sides, three on the `unattributable` miscount, three on the conf's two readers, three on the unbounded teardown reap, and two each on five more. Each row below carries its raw ids so nothing is lost. A merged row takes the MAXIMUM severity in its cluster, with one deliberate promotion, marked and argued in place: D7 (raw 5, 13, 33 — all medium) is promoted to HIGH because the merged picture is strictly worse than any member, the adopter grades one text while the engine enforces another AND the only probe that would catch the divergence has zero callers anywhere in the tree.

**Adjudicated totals across the 19 rows: 3 blockers, 4 highs, 7 mediums, 5 lows.** Severities are the ones adjudicated HERE, not the ones the lenses proposed.

| # | Sev | Address | Defect | Raw ids |
|---|-----|---------|--------|---------|
| D1 | BLOCKER | `reap.py:97,104,210,300` | `killable` is discarded at every `run_kill` call site, so a self-chain row is an acceptable walk root and kill-set member on the documented `--kill` path | 1, 17, 27 |
| D2 | BLOCKER | `adopt-process-monitor.test.sh:177` | The new bar suite prints no assertion count against a floor and is not waived — `check-testsuite-counts.sh` exits 1 | 26 |
| D3 | BLOCKER | `scope.py:89` | A root containing a space splits into two shorter roots and `check_root_shape` accepts both — it never tests absoluteness | 2 |
| D4 | HIGH | `scope.py:215` | `build_self_chain` never asserts the calling pid is in the census, so on an MSYS python the chain collapses to a singleton and every ancestor becomes killable | 7 |
| D5 | HIGH | `census.py:86` | `parse_cim` splits on `str.splitlines()` while the producer strips only `[\r\n]`, so a command line carrying `\v`/`\x1c`/`U+2028` forges a census row for an arbitrary winpid, with `rejected` still 0 | 3 |
| D6 | HIGH | `adopt-process-monitor.sh:129` | Nothing in the kit ever wires `procmon-hook.js`, and `--check` prints "wiring ok" anyway; no bar leg asserts the settings.json entries | 18, 34 |
| D7 | HIGH | `adopt-process-monitor.sh:64` | The conf has two readers with different semantics — the adopter `source`s it, the engine line-matches it — and the compensating probe `scope.py --check-conf` has no caller | 5, 13, 33 |
| D8 | MEDIUM | `reap.py:225` | `run_sweep` re-walks overlapping trees against the same stale census, so `counts['killed']` counts one winpid once per enclosing target | 9 |
| D9 | MEDIUM | `reap.py:157` | `unsignalable` winpids stay in `kill_set`, so any that are gone at rescan land in `report["killed"]` — the exact claim `check_survivors` exists to prevent | 20, 35 |
| D10 | MEDIUM | `scope.py:190` | `unattributable` counts rows with NO command line — the complement of the population the docstring, the README and the sweep line all say it reports | 10, 19, 28 |
| D11 | MEDIUM | `tools/gate-legs.json:732` | The census selftest guard names 2 of the 5 files the suite grades, so editing `scope.py`, `classify.py` or `reap.py` runs no arm at all | 11, 31 |
| D12 | MEDIUM | `run-gates.sh:1576` | `GATE_REAP_BOUND` is checked only BETWEEN legs and the `CEILINGS_LIVE=0` branch is unbounded; the wall path has no aggregate bound at all | 12, 22, 29 |
| D13 | MEDIUM | `reap.py:257` | `reap.py` has no unknown-flag refusal, so `--dryrun` or `--dry_run` falls through to a LIVE `reap-orphans` sweep | 21 |
| D14 | MEDIUM | `run-gates.test.sh:1608` | The teardown arm's liveness precondition `_tdgc >= 1` is satisfied by the outer wrapper's own argv, so it cannot fail | 32 |
| D15 | MEDIUM | `procmon-hook.js:105` | The throttled fast path spawns `git` and parses the conf BEFORE the throttle test, contradicting its own header — and a null stamp disables the throttle entirely | 15, 30 |
| D16 | LOW | `procmon-hook.js:117` | The hook invokes a bare `python`, bypassing this repo's RUN-the-candidate resolver and the `pyrun.sh` shim written for exactly this consumer | 16, 23 |
| D17 | LOW | `reap.py:103` | `dropped` can never be non-empty in production, and the arm grading it hand-builds a set `derive_scope` cannot emit | 14 |
| D18 | LOW | `run-gates.sh:989` | `cleanup` calls `reap_outstanding_legs` ~600 lines before its definition, past two `exit 2` paths | 24, 36 |
| D19 | LOW | `tools/govkit/subject-pins.tsv:81` | `process-monitor wiring` is pinned to chunk `records` while all seven sibling `<kit> wiring` legs are pinned to `wiring` | 25 |

---

## The blockers

### D1 — BLOCKER — `tools/process-monitor/reap.py:97`, `:104`, `:210`, `:300` — the fence's one exclusion is discarded at the only place that signals

`derive_scope` returns a mapping `{winpid: {"killable": bool, ...}}` and computes `killable=False` for every self-chain row. Every `run_kill` call site passes `set(scope)` — the KEYS — so the flag never crosses the boundary. `run_kill`'s two refusals test census membership (`:95`) and scope-key membership (`:97`); neither is the `killable` property, and `kill_set = [w for w in walked if w in scope_set]` (`:104`) has the same hole. `run_sweep` filters its target list on `killable` at `:204-205`, which is the ONLY reader of the flag in the codebase; `main`'s explicit `--kill`/`--kill-msys` path at `:300` does not, and its comment there — "The explicit path bypasses the MODE, never the FENCE" — is false, because `killable` is part of what the fence computed.

Reproduced three ways. Synthetic: `derive_scope(rows, ROOTS, self_chain={1,2})` marks both `killable=False`, and `run_kill(1, rows, set(sc), dry_run=True)` returns `kill_set [2, 1]` with `dropped []` and no refusal. Live on this node: scope held 17 of 334 rows, 4 self-chain members were in scope with `killable=False`, and all four were ACCEPTED as walk roots, with the calling python's own winpid present in `kill_set` on all three tried.

Reachable two ways. The documented operator command `reap.py --kill <winpid>` (spec S7), pointed at any winpid in the caller's own ancestry, walks DOWN through the reaper itself, taskkills the session shell, and dies mid-walk — leaving the rest of the tree unsignalled and unverified, because the verification census never runs. And `run-gates.sh:1573/1576` calls `--kill-msys` with a pid read from a `.pid` file; MSYS pids are small recycled integers, so a stale leg pid reused by the runner's own ancestor kills the session doing the reaping.

**Round 3's fold for this is a no-op and should be re-opened.** Spec unit 2 S4 states self-chain rows "are never KILL TARGETS and never WALK ROOTS. Unit 4 S3 enforces the second half"; unit 4 S3 defines membership purely as `scope_set`, of which self-chain rows are members. The delegated half is enforced by nothing.

**Fix.** Pass the scope MAPPING into `run_kill`, not `set(scope)`. Refuse a target whose `killable` is false — `if not scope.get(target, {}).get("killable"): raise ReapRefused(...)` — and build `kill_set` as `[w for w in walked if scope.get(w, {}).get("killable")]`, reporting non-killable walked members alongside `dropped` (which also gives D17's dead filter something real to withhold). Fix both call sites, `:210` and `:300`.

**Left-shift gate.** A `selftest.py` arm that calls `run_kill` on a self-chain winpid and asserts `ReapRefused`, plus a second asserting a non-killable descendant is dropped from `kill_set`. The existing arms cannot catch this: `test_self_chain_is_in_scope_but_not_killable` (`selftest.py:335`) exercises `derive_scope` only, and `test_out_of_scope_root_refuses_before_the_walk` (`:552`) passes `{2,3,4}` — a set the root is ABSENT from — so no arm has ever handed `run_kill` an in-scope non-killable target. Beyond the arm, the durable gate is a grep-class check refusing `run_kill(` called with a bare `set(` argument, since the defect is a type erasure at a call boundary and will recur the next time someone adds a third caller.

### D2 — BLOCKER — `tools/process-monitor/adopt-process-monitor.test.sh:177` — the merge bar is RED on this diff

`bash tools/check-testsuite-counts.sh` exits 1, verified twice (once through `tail`, which reports its own status — the real exit was captured separately):

```
TESTSUITE-COUNTS FAILED — a self-test on the bar prints no executed assertion count against a
floor ... tools/process-monitor/adopt-process-monitor.test.sh
```

The suite's tail prints `adopt-process-monitor: %d passed, %d failed (%d assertions)`, which matches neither anchored pattern in the gate's `compliant()` nor `check_harness_form()`. It pins no `FLOOR_ASSERTIONS` and no `SELFTEST_FLOOR`, and `memory/project/testsuite-count-waivers.txt` holds no row for it. The leg's population is derived from `gate-legs.json`, where this suite is named at line 744, so it is in scope by construction and cannot be argued out of the population.

**Fix.** Add `FLOOR_ASSERTIONS=<the measured arm count>` at column 0, replace the trailing printf with the shape the gate's anchored pattern accepts — `[ "$FAIL" = 0 ] && echo "PASS ($((PASS+FAIL)) assertions)"` — and compare the executed count against `${FLOOR_ASSERTIONS}` before exiting.

**Left-shift gate.** None needed: the gate exists, it works, and it caught this. The left-shift is procedural — a new `*.test.sh` added to `gate-legs.json` in the same commit that adds the suite means this leg reds at the first local bar rather than at the push boundary. Worth a line in the kit-authoring notes: a suite is not landed until `check-testsuite-counts.sh` has been run once against it.

### D3 — BLOCKER — `tools/process-monitor/scope.py:89` — a root with a space in it silently widens the fence to its own parent

`read_roots` does `.split()` on whitespace, so `PROCMON_ROOTS="C:/Users/John Doe/proj/repo"` yields `['C:/Users/John', 'Doe/proj/repo']`. `check_root_shape` tests only `len(norm) >= MIN_ROOT_LEN` and `norm not in ("", "/", "c:")` — never absoluteness — so a bare profile prefix and a relative fragment both pass at 13 and 13 characters.

Because `parse_tokens` also splits argv on whitespace, any process whose command line carries an unquoted path in that profile produces the token `C:/Users/John`, which matches the fragment root exactly. Verified: `check_token_under('C:/Users/John/AppData/Local/Programs/Spotify.exe', 'c:/users/john')` returns True; a planted parentless row over four hours old with that command line enters scope with `killable=True`, grades ORPHAN, and is killable under the template's own default `PROCMON_REAP_MODE="reap-orphans"`.

This is precisely the blast radius the conf's temp-root rule and the adopter's step 4 exist to prevent, and neither fires. The adopter word-splits identically (`for _r in $PROCMON_ROOTS`, `adopt-process-monitor.sh:70`) and its length test clears the fragment too, so the merge-bar arm named "process-monitor wiring" grades the widened fence as fine. The trigger is an ordinary Windows home directory.

**Fix.** In `check_root_shape`, refuse any entry that is not absolute (`^/` or `^[A-Za-z]:/`) — that kills the `doe/proj/repo` half. In the adopter's step-3 loop add `[ -d "$_r" ] || add_problem` — that kills the `C:/Users/John` half, since the fragment is not a directory. Both spellings in the shipped conf pass both tests. State in the conf header that a root may not contain whitespace, since the tokenizer on both sides of the comparison is whitespace-delimited and that is not going to change.

**Left-shift gate.** Two arms in `selftest.py`: one asserting `ScopeRefused` for a relative root, one asserting a space-bearing declaration is refused rather than split. The stronger left-shift is in `adopt-process-monitor.test.sh` — an arm that plants `PROCMON_ROOTS="C:/Users/John Doe/x"` in a scratch conf and asserts `--check` exits non-zero, which turns the adopter into the thing that catches this class rather than the thing that certifies it.

---

## The highs

### D4 — HIGH — `tools/process-monitor/scope.py:215` — the caller's own protection collapses silently on an MSYS python

`build_self_chain(rows, os.getpid())` never asserts that the pid it is handed is a winpid present in the census. Under an MSYS/Cygwin python, `os.getpid()` returns an MSYS pid — a different namespace from the winpid-keyed map this walk indexes. `edges.get(<msys pid>)` returns nothing, the chain is the singleton `{that integer}`, and `derive_scope` marks the session's own bash shell and all its ancestors `killable=True`.

Reproduced: `build_self_chain(rows, 987654)` over a winpid-keyed census returns `{987654}`, and `derive_scope` with that chain marks every in-scope row `killable=True`, including the row standing in for the session's own shell. Under `reap-all` — and under `reap-orphans` whenever the launcher has exited — `reap.py --sweep` then kills the session that ran it. On an integer collision it also protects an unrelated winpid.

The authors know the namespaces disagree: `scope.py:253`'s `--explain` refuses an MSYS id by name for exactly this reason. This is the one place the same hazard is not validated, and it is the place with the most at stake. `tools/lib/resolve-python.sh` tries `python3` FIRST, which in an MSYS2 tree with python installed is `/usr/bin/python3`, i.e. exactly that build. On node `a` python is native so this does not reproduce today, and no runtime arm would notice if it started to — `test_live_scope_is_not_empty` asserts only `len(sc) > 0`, which still passes with the chain collapsed.

**Fix.** In `build_self_chain`, refuse when the pid is absent from the census: `if winpid not in {r["winpid"] for r in rows}: raise ScopeRefused(...)`, naming the namespace the way `--explain` does. A self chain the census cannot see is a refusal, not an empty set. This is the charter's "a probe that cannot move says so" rule applied to the kit's own safety property.

**Left-shift gate.** An arm asserting `ScopeRefused` when `build_self_chain` is handed a pid absent from the corpus, and a second asserting the live chain over the real tree has length > 1 (a real process always has at least one ancestor in a census that saw it). The second is the one that would fire on a real MSYS host.

### D5 — HIGH — `tools/process-monitor/census.py:86` — producer and consumer disagree on what terminates a line, so a command line can forge a census row

`parse_cim` iterates `str.splitlines()` while `_CIM_QUERY` strips only `[\r\n]+`. Python's `splitlines` also breaks on `\v`, `\f`, `\x1c`, `\x1d`, `\x1e`, `\x85`, `U+2028` and `U+2029`. A process whose own command line embeds any of those splits across rows, and the well-formed second fragment OVERWRITES `rows[<whatever winpid it names>]`.

Reproduced with `rejected=0` for every one of `\x0b \x0c \x1c \x1d \x1e \x85` and `U+2028`: a command line carrying the separator plus `<pid>\x01999999\x010\x01999999\x01C:/projects/coding-governance/x` replaces the census row for an arbitrary pid with a forged parent (dead → ORPHAN), a forged age (past the ceiling) and a forged command naming a declared root (→ in scope, as a ROOT). `reap.py --sweep` then issues `taskkill /PID <victim> /F` against a process unrelated to this repo, and the row guard's counter stays at 0, so nothing reports it.

The row guard's own comment cites this exact class — "feeds arbitrary text to `kill -9`" — and claims to close it. The anchored numeric test blocks garbage; it does not block a well-formed forgery, because the hole is upstream of the test. The ASCII control characters survive any console codepage, so the transcoding argument does not save it. `parse_ps_w` (`:117`) has the same split and forges the `winpid→msys_pid` join that `kill -9` uses, though its COMMAND column carries no arguments, so that half is the weaker one.

**Fix.** Split on the producer's own terminator only: `text.split("\n")` in `parse_cim`, `parse_ps_w` and `parse_posix` (`:86`, `:117`, `:168`), stripping `\r` per line. Optionally also reject a CIM line carrying more than five fields, since the query emits exactly five.

**Left-shift gate.** A `selftest.py` arm that feeds `parse_cim` a corpus row whose command line contains `\x0b` and asserts the census row count and the target row's parent are unchanged. Generalise it as a table over all seven separators — the defect is a set-membership disagreement, and an arm testing one character certifies the wrong thing.

### D6 — HIGH — `tools/process-monitor/adopt-process-monitor.sh:129` — nothing wires the hook, and `--check` says "wiring ok" anyway

The adopter's header line 10 claims it wires hooks and line 11 that `--check` verifies wiring. It does neither. There is no `procmon-hook.fragment.json` (only `tools/hooks/scratch-guard.fragment.json` and `tools/memory-recall/recall-opened.fragment.json` are tracked); the adopter never touches `settings.json` — its six sections grade the conf's existence, the roots shape, the temp-root rule and three closed value sets, then print "wiring ok" naming only the conf; `check-wiring.sh` contains zero occurrences of `procmon`; and `check-hook-destinations.sh` quantifies over tracked `*.fragment.json`, which this kit contributes nothing to. `kit.toml:62-64` ships `procmon-hook.js` with `role="engine"` and no destination, under a comment claiming the destination is declared.

In THIS repo the hook works only because `.claude/settings.json` was hand-edited in `79d45dde`, and that file is in this branch's diff. An adopter running `govkit apply` plus `adopt-process-monitor.sh --check` gets the hook on disk, nothing invoking it, and a green line. The hook's whole stated reason to exist — "the verdict has to arrive without being asked for" — is silently absent.

The bar cannot see it either. The only assertion over the two settings.json entries is `test_wiring_is_idempotent` (`adopt-process-monitor.test.sh:171-172`), whose leg is `chunk=selftests` + `subject=kit`, held under the default bar AND under `GATE_FULL=1` per the 2026-08-23 ruling, reachable only via `GATE_SELFTESTS=1`, which no boundary sets. Delete both settings.json entries — the sole automatic trigger for the monitor — and every default-bar leg stays green. That is the state the kit was built to end.

**Fix.** Ship `procmon-hook.fragment.json` beside the hook in the `recall-opened.fragment.json` shape and declare it in `kit.toml`, which gives `check-hook-destinations.sh` a subject. Then either have the adopter merge it via `settings-merge.py --fragment`, or at minimum make `--check` grep the target's `settings.json` for the hook command and report UNWIRED. Fix line 10's usage comment either way — it currently describes two things the script does not do, since line 62 explicitly REFUSES to create the conf.

**Left-shift gate.** The fragment declaration IS the left-shift: it moves this kit into the population `check-hook-destinations.sh` already quantifies over, so the class is gated for every future kit rather than patched for this one. Add to `adopt-process-monitor.sh --check` — already the repo-subject leg named "process-monitor wiring" — a count of `procmon-hook` references in the target's settings.json, so the leg's name stops overstating what it grades.

### D7 — HIGH — `tools/process-monitor/adopt-process-monitor.sh:64` — one declaration, two readers, and the probe that would catch it has no callers

*(Promoted from the cluster maximum. Raw 5, 13 and 33 were each rated medium; merged, the picture is strictly worse than any member.)*

The adopter `source`s the conf (`. "$CONF"`, shell expansion, last-assignment-wins). The engine line-matches it as literal text (`scope.py:198`, first-`PROCMON_ROOTS=`-wins). Three consequences, all reproduced:

1. `PROCMON_ROOTS="$HOME/projects/repo"` passes every adopter check — expanded, absolute, over `MIN_ROOT_LEN`, not temp — while `read_roots` hands the fence the literal `$HOME/projects/repo`, which clears `check_root_shape` at 19 characters, matches nothing, and yields an EMPTY scope with NO refusal. `derive_scope` returned `{}` with `in_scope 0`, and `run_sweep` then reports a clean tree it never examined. That is the exact green-by-absence the conf header says a blank roots list exists to refuse, discharged by a probe that cannot see it. The hook's clean path is silent, so the outcome is indistinguishable from a healthy machine.
2. First-wins versus last-wins is real and internally inconsistent inside `reap.py` itself: over a conf with two `PROCMON_ROOTS` and two `PROCMON_REAP_MODE` lines, `read_roots` took the FIRST (blank → refusal) while the mode loop took the LAST (`reap-all`). The template ships `PROCMON_ROOTS=""` at line 31, so an adopter who appends their own line below rather than editing it gets a green `--check` over a fence that refuses on every run; the reverse edit order gives a green check over a fence WIDER than the one graded.
3. The compensating arm the adopter's own line 130 points at — `scope.py --check-conf`, spec S9/AC15, which refuses when the roots admit nothing — has **zero callers anywhere in the tree.** It is in no `gate-legs.json` leg. The disclaimer points at a check nothing on the bar runs.

**Fix.** Have `--check` delegate the roots question to the engine's own reader — `"$PYBIN" "$KIT_DIR/scope.py" --check-conf`, which also exercises the live admission and gives that dead entry point its caller — or, at minimum, make the adopter read the conf with the same literal parser the engine uses instead of sourcing it. One text, one reader. Drop the early `return` in `read_roots` so it is last-wins like every other reader, and refuse a conf carrying more than one `PROCMON_ROOTS=` assignment. D3's absoluteness test turns the `$HOME` case into a loud refusal rather than a silent empty fence.

**Left-shift gate.** Wire `scope.py --check-conf` into the "process-monitor wiring" leg — a dead entry point that would have caught two of this report's findings is the strongest available left-shift, and it costs one argv. Add an arm asserting that a conf whose roots admit zero live rows REFUSES rather than reporting clean.

---

## The mediums

### D8 — MEDIUM — `tools/process-monitor/reap.py:225` — the sweep double-counts overlapping trees and claims kills it did not make

`run_sweep` re-runs every target against the SAME stale census, so a nested tree is walked once per enclosing target. Verified on a synthetic `10 -> 11 -> 12` tree, all three flagged under `reap-all`: the three per-target walks are `[12,11,10]`, `[12,11]`, `[12]`, `check_survivors` against an empty rescan credits all three, and `counts['killed']` prints **6 killed for 3 processes**.

The second half is worse than the arithmetic. `check_survivors` derives `killed` purely as "in `kill_set` and absent from the second census", so a descendant already dead from an earlier target's cascade — or one that exited on its own — is claimed as a kill this run made. That is the "claim a kill it did not make" class the reaper's verification was built to close, moved one level up into the sweep.

**Fix.** Track a `reaped` set across the loop: skip a target already in it, and after each `check_survivors` add `rep["killed"]`. Derive the summary from `len(reaped)`, not from a sum over overlapping reports. Re-censusing between targets is the more correct fix and costs a bounded subprocess per target.

**Left-shift gate.** An arm running `run_sweep` over a nested three-row fixture and asserting `counts["killed"] == 3`. The criterion is a strict equality against the fixture's own row count, which is the only form that catches a double count.

### D9 — MEDIUM — `tools/process-monitor/reap.py:157` — an unsignalable row is counted killed if it exits on its own

`unsignalable` winpids are appended at `:116`, inside the loop over a `kill_set` that was fixed at `:104`, so `kill_set` is never narrowed. `check_survivors` computes `killed` as `kill_set` minus the rescan, which includes any unsignalable pid absent at rescan. Reproduced: `kill_set=[5]`, `unsignalable=[5]`, empty rescan → `killed=[5]`, and `render_kill` emits both `reap: killed 1 ... unsignalable 1` and `reap: UNSIGNALABLE 5 — neither probe can address it; not claimed killed` in the same output. `counts['killed']` (`:216`) inherits the overstatement.

This contradicts `reap.py:22`, `render_kill`'s own per-row line, and spec unit 4 AC11. The AC's second clause is graded by nothing: `test_unaddressable_row_is_reported_not_claimed` (`selftest.py:593-602`) asserts only `(len(rep["unsignalable"]), rep["signalled"]) == (4, [])` and never calls `check_survivors`. Every `check_survivors` caller was checked; none exercises an unsignalable row. Reachable on the posix-ps backend the kit ships and documents, where `taskkill` resolves to None and a descendant already dead from the leaves-first cascade becomes unsignalable rather than `already_gone`.

**Fix.** Subtract the unsignalable set before computing killed and survivors: `attempted = [w for w in report["kill_set"] if w not in set(report["unsignalable"])]`, and derive both lists from `attempted`. Report vanished-but-unsignalable rows in their own field.

**Left-shift gate.** Extend the existing arm to call `check_survivors` with a rescan that omits the unsignalable row and assert it is NOT in `killed` — the arm already exists and already stops one assertion short of the clause that matters.

### D10 — MEDIUM — `tools/process-monitor/scope.py:190` — `unattributable` counts a different population than every document says it does

`unattributable` is `r["winpid"] not in scope and not r.get("command")` — rows with NO command line. The module docstring (`:21-23`) and `README.md:50-53` define the population as "command line names no declared root AND whose ancestry is dead", citing `sleep 27200` and `tail -f /tmp/...` — rows that DO carry a command and are therefore structurally excluded from the number.

Reproduced: over a corpus holding a `sleep 27200` and a `tail -f /tmp/x.log` with dead parents plus one command-less row, `counts["unattributable"]` is 1 and the row it counted is the command-less one. Measured live on this node: census 334, scope 17, unattributable 117 — so 200 command-bearing unscoped rows are named by no figure at all, while the 117 that ARE printed as "unattributable row(s) this kit cannot see" are the protected/system population `README.md:54-58` documents as a SEPARATE limit and `census.py --print` already reports as `no_command`.

So the accepted limit the design records as "reported as a count" is reported by no number, and the number that IS printed describes rows the kit sees fine. An operator reading it learns nothing about the hole it exists to expose.

**Fix.** Count the real population — `sum(1 for r in rows if r["winpid"] not in scope and not any(p in by_win for p in edges.get(r["winpid"], ())))` — and report the command-less figure separately under its own name. Renaming the existing field to `no_command_out_of_scope` and adding the real one is the honest two-line version.

**Left-shift gate.** An arm asserting a corpus row with a non-matching command AND a dead parent lands in the count, and that a command-less row does not. Both directions, because the current defect is exactly the one a single-direction arm cannot see.

### D11 — MEDIUM — `tools/gate-legs.json:732` — the guard names the file the leg is titled after, not the population it grades

The "process-monitor census selftest" leg guards on `census.py` and `selftest.py` only, while `selftest.py` is the SOLE coverage for `scope.py` (16 arms), `classify.py` (9 arms) and `reap.py` (10 arms) — `grep 'scope.py|classify.py|reap.py' tools/gate-legs.json` returns nothing else. `run-gates.sh:1181-1183` writes `skip` when the guard paths did not change, so a commit touching only `reap.py` — the one file in this kit that irreversibly kills processes — runs no arm at all. Reaching it needs `GATE_SELFTESTS=1` AND `GATE_FULL=1`, since the selftests hold at `:1177` is deliberately not lifted by `GATE_FULL`. `kit.toml:42` declares the same guard, so adopters inherit it.

The one suite that could catch a fence regression is silent for exactly the edits that would cause one.

**Fix.** Name every file the suite exercises in both guards: `["tools/process-monitor/census.py", "tools/process-monitor/scope.py", "tools/process-monitor/classify.py", "tools/process-monitor/reap.py", "tools/process-monitor/selftest.py"]`, and `{kit}/...` in `kit.toml`.

**Left-shift gate.** This is a class, not an instance: any leg whose guard is narrower than the files its suite imports has the same hole. A checker that parses each self-test's `import`/`source` set and asserts the leg's guard covers it would catch every future instance, and this repo has enough guarded legs for that to pay. Failing that, at least assert guard-vs-`kit.toml` parity so the two catalogs cannot drift apart while both stay wrong.

### D12 — MEDIUM — `tools/run-gates/run-gates.sh:1576` — the declared reap bound cannot preempt the one thing it was written to preempt

`reap_leg_tree` wraps `reap.py` in `timeout -k 5s 60` only when `CEILINGS_LIVE=1` (`:1572`); the else branch at `:1576` runs it with no wrapper. `CEILINGS_LIVE=0` is a real, handled host state, set at `:371` with its own operator notice at `:493`. `reap_outstanding_legs` tests `EPOCHSECONDS >= deadline` only at the TOP of each loop iteration, so it cannot preempt a call already in flight. In the fallback branch that call is bounded only by `reap.py`'s internals: `BACKEND_TIMEOUT_S=90` per subprocess, two censuses per call (pre-kill and verification, each spawning powershell CIM plus `ps -W`), plus `SIGNAL_TIMEOUT_S=20` per `kill -0` probe and per signal, per walked row. That is minutes per leg tree, taken while `cleanup` holds the turnstile, before `ts_release`/`ts_drop_ticket` run.

`arm_wall`'s breach loop (`:1546-1553`) is worse: it now calls `reap_leg_tree` per stuck leg with NO deadline at all, where it previously called `remove_descendants` (one `ps -ef`, milliseconds). The declared `wall` — the knob whose whole job is to bound the run — can be overrun by up to `GATE_JOBS x 65s`, and by minutes on the no-`timeout` hosts.

The comment at `:1583-1585` asserts the teardown reap is "BOUNDED as a whole" so "a hung monitor cannot strand a turnstile ticket and queue every later bar on this host behind it". The fallback branch does not deliver that. Magnitude caveat worth recording: one reap invocation measured 0.78 s wall on this healthy node, so the overshoot is a pathological-case defect — which is the only case the wall exists for.

**Fix.** Bound the unbounded branch: a background `reap.py` plus a shell-level `kill` after `GATE_REAP_BOUND`, or skip the delegation entirely when `CEILINGS_LIVE=0` and fall back to `remove_descendants`, which already always runs at `:1580`. Check the deadline INSIDE `reap_leg_tree` as well as between legs, and give `arm_wall`'s loop the same deadline `reap_outstanding_legs` uses. State whichever choice in the comment so it stops claiming a bound it does not have.

**Left-shift gate.** The current arm greps for the string `GATE_REAP_BOUND` (`run-gates.test.sh:1591`) and the functional arm sets `PROCMON_OK=0`, so the `reap.py` path is never exercised: the arm certifies that the bound EXISTS, not that it BINDS. Replace it with a timed arm — stub `PROCMON_REAP` with a script that sleeps past the bound, run the teardown with `CEILINGS_LIVE=0`, and assert the elapsed wall is under `GATE_REAP_BOUND + slack`. That is the only form that fails when the wrapper is missing.

### D13 — MEDIUM — `tools/process-monitor/reap.py:257` — a mistyped `--dry-run` runs a live sweep

`main` recognises only `--dry-run`, `--kill` and `--kill-msys`, and has no unknown-flag refusal. `--dryrun` and `--dry_run` both yield `dry_run=False` and fall through to a LIVE sweep in the conf's mode, which the repo's own `.process-monitor.conf:70` declares as `reap-orphans`. `--sweep` itself is accepted and ignored, which trains the habit that flags here are free-form — and `procmon-hook.js:147` prints exactly that shape as advice: `reap.py --sweep   (--dry-run to look first)`.

The asymmetry is the argument. `PROCMON_BACKEND` (`census.py:214-218`), `PROCMON_REAP_MODE` (`reap.py:269-271`), `--explain` (`scope.py:252-255`) and `--kill`'s argument (`reap.py:277-279`) all validate against a closed set and refuse. The one input whose failure is irreversible does not.

**Fix.** Validate argv against a closed set at the top of `main` and refuse anything outside it, the way `PROCMON_REAP_MODE` is refused two lines below. Make `--sweep` a required verb for the sweep path so a bare or mistyped invocation cannot kill.

**Left-shift gate.** An arm asserting `reap.py --sweep --dryrun` exits non-zero and signals nothing. Generalisable across the kit as a single arm per entry point asserting an unknown flag refuses — three entry points, three assertions, and the class is closed.

### D14 — MEDIUM — `tools/run-gates/run-gates.test.sh:1608` — the teardown arm's liveness precondition cannot fail

The fixture is `bash -c "bash -c 'sleep 300 # $_tdm-gc' & sleep 300 # $_tdm-leg"`, so the OUTER bash's own command line already contains `$_tdm-gc`. Reproduced verbatim: `ps -ef | grep -F "$_tdm-gc"` returns exactly ONE row, and it is the outer bash — the leg pid itself. The inner `bash -c` never appears as its own tagged row. So `[ "$_tdgc" -ge 1 ]`, written to refuse a fixture that staged no grandchild, counts the wrapper and always passes.

It is worse than stated. `sleep 300 # tag` puts the tag in the shell's command line only, so after killing the tagged rows the probe left two orphaned `sleep 300` processes reparented to ppid 1 — meaning `_tdgc2` and `_tdlg2` both go to 0 the moment the single outer bash dies, and the arm reports green with every actual descendant still running. The comment at `:1609` asserting the arm "proves nothing" without the precondition is itself the could-not-fail shape it names.

**Fix.** Require `[ "$_tdgc" -ge 2 ]` (outer plus inner), or give the grandchild a marker that does not appear in the parent's argv — `exec -a` or an env-var-bearing child — and assert on that marker alone. The second is the real fix, because the first still counts a `sleep` whose tag rides on a shell that is about to die.

**Left-shift gate.** The generalisable rule: a liveness precondition must be verified to FAIL when the thing it asserts is absent. Stage the break — remove the `&` that spawns the grandchild — and confirm the arm reds. That is §7's own "a new gate is not landed until its failing case has been observed", applied to a test's precondition rather than to a gate.

### D15 — MEDIUM — `tools/process-monitor/procmon-hook.js:105` — the throttled fast path does the two things its header says it does not

`main()` calls `resolveStamp(root)` at `:105` — an `execFileSync` of `git -C <root> rev-parse --git-common-dir` — and `readThrottleSeconds(root)` at `:106` — a `readFileSync` plus regex over the conf — BEFORE the throttle test at `:108/110`. The header at `:21-24` states "THE THROTTLE CHECK IS ONE `stat` AND NOTHING ELSE" and that "the early-exit path parses no conf". Parsing the conf is exactly what `readThrottleSeconds` does, and a git spawn is added on top.

Measured here: the git spawn 55-57 ms, a full throttled hook run 110-146 ms, paid on the overwhelming majority of `Bash|PowerShell` tool calls — the exact population the header claims to have optimised for. (This repo's recorded gotcha prices a git spawn at 751 ms on a contended box, so the ceiling is much higher than the healthy-node measurement.)

The second half is the one that matters: `:110` is `if (!sessionStart && stamp && checkThrottled(...))`, so a NULL stamp — git absent, non-repo root, or the 10 s git timeout — skips the throttle entirely and every matching tool call pays the full census the header says it avoids. Fail-open in the expensive direction.

**Fix.** Resolve the stamp without spawning git: read `<root>/.git`, using it directly when it is a directory and parsing the `gitdir:` line when it is a file. Move `readThrottleSeconds` below the stamp `stat` so a fresh stamp exits before any file parse. When the stamp cannot be resolved, fall back to a per-root path rather than disabling the throttle.

**Left-shift gate.** An arm asserting the throttled path performs no `git` spawn — stub `git` on PATH with a script that writes a sentinel file and assert the file is absent after a throttled invocation. That gates the header's claim rather than restating it.

---

## The lows

### D16 — LOW — `tools/process-monitor/procmon-hook.js:117` — the hook names a python launcher literally

`execFileSync(process.env.PROCMON_PYTHON || 'python', ...)` — the only `.js` file in the repo that actually executes python. `tools/lib/resolve-python.sh` is this repo's declared single resolver precisely because it RUNS each candidate (the Windows App Execution Alias stub answers a lookup and exits 9009 without executing), and `tools/lib/pyrun.sh` exists specifically for non-shell consumers that cannot source it — its header names "naming a launcher literally" as the failure it exists to prevent. `run-gates.sh:75` uses the resolver for `PYBIN` when it invokes the very same `reap.py`. The repo-wide invocation ban in `resolve-python.test.sh` is scoped to `*.sh` by a recorded decision, so no gate can see this call. On a host where `python` is the stub, the hook prints `process-monitor: could NOT run — …` on every SessionStart and every expired 300 s window. It fails open, so this is permanent noise rather than a block — which the header itself names as the state that gets a hook removed.

**Fix.** Spawn `bash tools/lib/pyrun.sh <reap.py> …` when that file is present in the resolved root, falling back to the current literal only when it is not (the kit can copy-install standalone). Keep `PROCMON_PYTHON` as the override and document it — it currently appears nowhere but the hook and its own test.

**Left-shift gate.** Widen `resolve-python.test.sh`'s ban to `*.js` for the `execFileSync`/`spawnSync` argv position specifically. The recorded decision rejected widening to `.githooks/`, `*.json` and `*.md` on false-positive grounds; a `.js` file that literally spawns an interpreter is not that class, and there is exactly one of them.

### D17 — LOW — `tools/process-monitor/reap.py:103` — `dropped` is a fence that can never withhold anything

`derive_scope` closes scope over ALL descendants and `build_walk` walks that same children map from the same `build_edges(rows)` call, so every descendant of an in-scope target is in scope by construction and `dropped` is always empty for both production callers. `render_kill` nonetheless prints "in scope N · dropped 0" as if it were a second per-member fence, which is the reassurance a reader takes for the reaper's safety check. The arm that grades it (`selftest.py:571`) hand-builds `{1, 2, 4}` — a set omitting an interior node, which `derive_scope` cannot emit — so the criterion passes over an impossible input. This is the same shape `run_kill`'s own docstring faults rev-2 for: a refusal with no reachable failing case.

**Fix.** Give the filter something the fence can actually withhold by testing `killable` here (D1's fix does exactly that, and this line becomes real as a side effect). If that fix is not taken, state in the header that membership is guaranteed by the closure and make the line RAISE rather than silently dropping, so it is an assertion rather than a decoration.

**Left-shift gate.** Covered by D1's arm. The generalisable rule is §7's: run a candidate predicate over real data and confirm it can fire; a filter observed only over hand-built impossible inputs is not covered.

### D18 — LOW — `tools/run-gates/run-gates.sh:989` — `cleanup` calls a function defined 600 lines later

`cleanup` is defined at `:989` and its traps installed at `:990-993`; `reap_outstanding_legs` is not defined until `:1587`. Two `exit 2` paths fire inside that window: `:1042` ("cannot create the run record") and `:1131` ("cannot parse $LEGS_FILE"). The script sets only `set -u`, so the trap continues: bash prints `reap_outstanding_legs: command not found`, returns 127, and execution proceeds with the script's exit status preserved. No ticket is stranded and the scratch dir is still released. The noise appears AFTER the real message (the echo runs before the exit that fires the trap), on precisely the two failure paths where the operator is reading stderr for the cause.

**Fix.** Move the `reap_leg_tree` / `GATE_REAP_BOUND` / `reap_outstanding_legs` definitions above `cleanup`, or guard the call with `declare -F reap_outstanding_legs >/dev/null && reap_outstanding_legs`.

**Left-shift gate.** A shellcheck-class or grep-class arm asserting every function called from a trap handler is defined above the `trap` line. One rule, one file, and it catches the next reorder.

### D19 — LOW — `tools/govkit/subject-pins.tsv:81` — the wiring leg is filed under `records`

`process-monitor wiring` is pinned to chunk `records`, while all seven sibling `<kit> wiring` legs are pinned to `wiring`. Chunks bound REPORTING, not dispatch (`run-gates.sh:1443`), so the leg still runs — it lands in the wrong verdict block, and a reader scanning the wiring chunk for "is every kit wired" sees seven of eight. `gate-legs.json:719` carries the same pin, so the two catalogs agree with each other and not with the convention.

**Fix.** Repin to `wiring` in `subject-pins.tsv` and regenerate `tools/gate-legs.json` in the same commit.

**Left-shift gate.** A parity check asserting every leg whose name ends in ` wiring` sits in chunk `wiring`. The convention is machine-checkable from the leg name alone, which is the cheapest kind of gate this repo has.

---

## What was refuted, and what this review did not cover

Three raw findings were refuted by the skeptic pass and are not reported. Precision 0.92 is high enough that no scope tightening is indicated for a follow-up round; per §8 that ratio says the lenses were well primed, not that the surface is exhausted.

**Not covered, stated so a green here is not misread.** The four lenses were pointed at safety, kill-accounting, the `run-gates.sh` change, could-not-fail criteria, and the shell/python/node boundary. They were NOT pointed at: the classifier's rate arithmetic beyond its use as a label, the README's prose accuracy outside the two places a defect turned on it, `kit.toml`'s descriptor completeness beyond the hook destination, or the census backends' behaviour on a non-Windows host, which nothing in this range can exercise here. The 47 defects folded across the three spec audits were treated as closed except where a fold is itself wrong; D1 names the one place a fold was a no-op (round 3's self-chain repair delegated to a criterion that does not enforce it), and that should be re-opened in unit 2 §9 rather than silently re-fixed.

**One measured fact for the fix pass.** D1, D3, D4 and D7 are all the same defect shape — a safety property computed in one place and lost at the boundary into the next — and three of the four are one-line fixes. Fixing them individually will feel like four unrelated patches. The durable left-shift is a single arm asserting the LIVE fence, on the real tree, refuses to mark the calling session killable; that one arm fails on all four.
