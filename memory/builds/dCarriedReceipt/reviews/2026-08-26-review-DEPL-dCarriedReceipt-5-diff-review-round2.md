**Serves:** diff-review DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-15

# Closing diff review, ROUND 2 — the fold itself

**Range reviewed: `4ad677262f1e3ac2e0d0ba43b8fe4e8a04d0a2ea...HEAD`.**

**The base sha as handed to this reviewer does not resolve in this repo.** `git cat-file -t` refuses
it. The commit its first eight characters name is `4ad67726736c97bb873b21219100a6d9f53cb61d`
(`records(deployer): DEPL-dCarriedReceipt-13 evidenced against a REAL adopter`), and that is the
object actually diffed — three-dot, against tip `267b598f`. Two commits, thirteen files, 1475
insertions. If a later reader needs the exact tree, use the resolving sha, not the one in the
heading; a record that names an object git cannot look up is a record that points at nothing.

**ROUND: 2.** The base is round 1's recorded tip, so this diff is the FOLD — the fixes for round 1's
fourteen confirmed defects plus the arms written to hold them — and not a re-read of the original
work. It was read as such.

**Review shape:** raw 26 · confirmed 21 · refuted 5 · unverified 0 · precision 0.81. The five refuted
ids were 3, 6, 13, 16 and 20; they are not recorded here beyond their numbers, because a refuted
finding is not a finding.

## Verdict: BLOCKED

Two blockers, one high, five mediums, thirteen lows. The headline is not that the fold was sloppy —
most of the fourteen fixes do close their defect. The headline is that **D1, the blocker round 1
escalated, is still live under a different branch of the same verb**, and the artifact written to
prevent its recurrence asserts in prose that the branch is safe. Both routes were reproduced, not
theorised: a `PWNED` file appeared in a fixture target after a read-only `govkit check`.

The secondary theme is the arms. Six of the new selftest arms are satisfied by their own fixture
setup or by a source-shape substring rather than by the mechanism they name; four of them were
measured green with their fix reverted. That is this repo's own could-not-fail class, arriving inside
the arms written to close a could-not-fail finding.

---

## BLOCKERS

### B1 — `check` executes target-authored argv with no opt-in, via the kit `[check].argv` arm

`tools/govkit/govkit.py:2098` (`run_kit_check`), reached from `cmd_check`. Round-1 id 1.

The D1 fix closed `[[decline]].discharge` and left `check` executing target-authored code. Both of
`cmd_check`'s spawns resolve their argv through `target_context(target, deploy, ...)`, and
`target_context` (`govkit.py:545-551`) only does `.strip("/")` on the target-supplied `prefix` before
handing it to `resolve_tokens` as `{prefix}` and `{kit}`. Every shipped `[check].argv` and
`[[hole]].discharge.command` is built from those tokens.

**Reproduced.** A fixture target carrying only `prefix = "evilkit"` in `.governance/deploy.toml`, an
`install.json` claiming `agent-instructions` with one project-owned row, and its own
`evilkit/agent-instructions/adopt-agent-instructions.sh`, made
`python tools/govkit/govkit.py check --target <t>` execute that script, create `PWNED2` in the
target, print `govkit check — agent-instructions: adopted`, and exit 0.

Also reproduced through the `python -c` holes: `prefix = "x'); import pathlib; pathlib.Path('PWNED').write_text('owned'); ('"`
with `codebase-map` claimed makes the same read-only `check` run that Python and create `PWNED`.

No `--run-discharge`. No argv printed. No trace in the output. And it breaks the unit's own stated
security model — `apply` and `update --write` are supposed to be the only verbs that put bytes in the
target's working tree, and `check` wrote one.

**Fix.** Treat any argv whose tokens are resolved from `target_context` as target-authored. Preferred
(smaller, keeps the hole signal): validate at the boundary — refuse a `prefix` or answer value that
is not `[A-Za-z0-9_./-]+`, in `target_context`, before any `resolve_tokens` result reaches
`subprocess.run`. Alternative: put both spawns behind the same `--run-discharge` opt-in the fold
already added, printing the resolved argv first. Either way, re-label `run_kit_check` and `cmd_check`
`target` in `SHELL_EXEC_SITES`.

**Left-shift gate.** A selftest arm that plants a shell metacharacter and a quote-break in `prefix`,
runs `check`, and asserts no sentinel file appeared in the target. Plus the derived-label arm from
H1 below, which turns this class from "remember to check" into "reds on the next spawn".

### B2 — the same class one branch over: `cmd_check`'s `[[hole]].discharge` loop

`tools/govkit/govkit.py:1770` (the false `"cmd_check": "gov"` row) and `govkit.py:2366` (the spawn).
Round-1 id 22.

`cmd_check`'s hole loop (`govkit.py:2350-2366`) has no `run_discharge` guard at all. Each argv
element goes through `resolve_tokens(a, ctx)` with `ctx = target_context(...)`, and the shipped hole
`tools/drift-audit/kit.toml:80` is `["bash", "-c", "python {kit}/drift_report.py --check"]` —
target-chosen text interpolated into a `bash -c` string. `resolve_shell_argv` only rewrites `argv[0]`,
so it is no defense here.

**Reproduced.** Target with `prefix = "tools; touch PWNED-BY-CHECK ;"` and a receipt claiming
`drift-audit` with one seed row. `python tools/govkit/govkit.py check --target <evil>` — read-only, no
`--write`, no `--run-discharge` — created `PWNED-BY-CHECK` in the target.

The `python -c "...sys.path.insert(0, '{kit}')..."` holes at `tools/drift-audit/kit.toml:64,72` and
`tools/codebase-map/kit.toml:64` are the same class through a quote break.

Verified clean by contrast: `plan --coverage` no longer reaches this. `_cmd_apply:3648` has the same
token-injection shape but sits behind a writing verb, which is a different risk tier.

**Fix.** Same as B1 — the boundary check in `target_context` kills B1 and B2 together in one line. If
the opt-in route is taken instead, `cmd_check`'s hole loop needs a `probe-not-run` state so a
withheld probe is not silently read as discharged.

**Left-shift gate.** The same metacharacter fixture as B1, run against a target whose receipt claims
`drift-audit`, asserting no sentinel. It must be a fixture arm, not a source-shape arm: B1 and B2 both
survived a source-shape arm that was green the whole time.

---

## HIGH

### H1 — `SHELL_EXEC_SITES` labels by who authored the TEMPLATE, so the gate cannot fail on B1 or B2

`tools/govkit/govkit.py:1769`, arm at `tools/govkit/selftest.py:5583`. Round-1 id 2.

The arm filters `_tgt_sites = [k for k, v in SHELL_EXEC_SITES.items() if v == "target"]`, and the two
properties it enforces — announce the argv, do not be reachable from a default verb — are therefore
never asked of `run_kit_check` or `cmd_check`, which are declared `"gov"`. The both-directions arms
above it only assert declared-vs-spawning membership, which both sites already satisfy. So the gate
written to make this class un-recurrable is green over a live ACE.

Worse, the falsehood is now recorded twice as fact: `govkit.py:1933` ("The single pre-existing
target-authored spawn is `read_gate_verdicts`") and
`memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-5.md:130` (the rev-6
amendment). That is the same read-a-sentence-instead-of-the-call-graph mistake D1 was raised about,
re-recorded with a passing gate behind it.

**Fix.** Derive the label instead of typing it: a site is `target` when the argv it spawns passes
through `resolve_tokens` / `target_context`. Correct the comment at `govkit.py:1928-1934` and the §5
rev-6 bullet.

**Left-shift gate.** An arm that REDS any row declared `gov` whose function body references
`target_context` or `resolve_tokens`. Derived, so a future spawn cannot be mislabelled by hand.

---

## MEDIUM

### M1 — the `check` half of the D1 fix is ungated: the arm passes by finding nothing

`tools/govkit/selftest.py:5726`. Round-1 id 7.

The arm `[-5] D1 ...and 'check' does not execute it either` asserts `not _sent.exists()`. `_t5sent` is
built by `a5_target` (`selftest.py:5520-5537`), which writes only `.governance/deploy.toml` — no
`install.json`. `cmd_check` returns at `if not receipt_path.is_file()` (`govkit.py:2153-2158`) long
before the decline block at 2170-2178. Verified: the run prints `NOT LANDED (no
.governance/install.json)`, rc 1, decline block never entered.

So reverting `cmd_check`'s `run_discharge` threading — or hard-coding `run_discharge=True` — leaves
the whole suite green. This is how B1's second call site shipped.

**Fix.** Give the sentinel fixture a receipt before the `check` run (an `apply --kits demo`, or a
minimal `install.json` naming the kit) so the decline block is actually reached, and add the mirror
arm: `check --run-discharge` over the same fixture MUST create the sentinel.

**Left-shift gate.** The mirror arm is the gate. A negative arm with no positive twin proves nothing;
make the pairing the convention for every opt-in in this engine.

### M2 — the `SHELL_EXEC_SITES` census cannot see a spawn that skips the resolver, and `hook_probe` is a live undeclared one

`tools/govkit/selftest.py:5581` and `tools/govkit/govkit.py:1752`. Round-1 ids 14 and 23 — one defect
found twice, from the arm side and from the header side.

The declaration's header claims it lists "EVERY PLACE THIS ENGINE RUNS A SHELL COMMAND". The enforcing
arm walks the AST for `ast.Call` nodes whose func is the Name `resolve_shell_argv` and nothing else.
`grep -n subprocess.run tools/govkit/govkit.py` returns roughly 45 spawn sites; six route through the
resolver.

`hook_probe` (`govkit.py:2715-2734`) runs `subprocess.run(["git", "-C", str(target), "hook", "run",
"pre-commit"])` at line 2731 — that executes a script authored in the target repository. It is reached
on every `apply` (`govkit.py:3578`). It is neither declared nor detectable by the arm.

Impact is bounded today: `hook_probe`'s own argv is gov's, and it is apply-only, so declaring it grades
as a no-op row. The defect is the census's guarantee being narrower than the sentence selling it — any
future bare `subprocess.run(cmd)` lands undeclared and the arm stays green, which is the exact false
confidence that let D1 ship.

**Fix.** Walk `subprocess.run`/`Popen` calls instead of `resolve_shell_argv` calls; treat a call whose
first argument is a list literal beginning with `"git"` as the gov-internal allowlist; declare
`hook_probe` (`target`, apply-only). Keep the both-directions assertion over the wider population. If
the census is deliberately narrower, the header must say what it does NOT cover and stop writing
"EVERY PLACE" — §7's own rule.

**Left-shift gate.** The widened AST predicate IS the gate. Run it over the real tree before wiring
and print hits and near-misses, per §7.

### M3 — `adopt --re-adopt --write` dies with a traceback on a non-object `install.json`

`tools/govkit/govkit.py:5940-5947`. Round-1 ids 15, 4, 9 and 26 — the same one-line defect, found four
times independently, which is itself a signal about how reachable it is.

D2's carry-forward guards `json.loads` against `(OSError, json.JSONDecodeError)` and then does
`k in _prior` and `_prior[_k]` with no type check.

- `null` → `TypeError: argument of type 'NoneType' is not a container or iterable` at the `in` test.
- `123` / `true` → the same shape.
- `["orders"]` → list containment is True, then `_prior["orders"]` raises `TypeError: list indices
  must be integers`.
- a bare JSON string `"…orders…"` → substring membership is True, then string indexing raises.

`main` (`govkit.py:6278`) catches only `Refusal`, and the entrypoint is `raise SystemExit(main(...))`,
so the operator gets a raw traceback instead of a named refusal — on the one verb whose job is
repairing a broken receipt, and whose neighbouring refusal text steers them there. `install.json` is
committed in the target and text-mergeable, so a bad merge is the realistic producer.

Fail-closed: no receipt is written and `cmd_adopt`'s `finally` releases the lock correctly. Crash, not
data loss. Rated medium on reach rather than on blast radius.

Second, smaller half: the S10 comment at `govkit.py:5917-5920` still states that `orders`, `baseline`,
`after`, `hook_block` and `gate_runner` "are NOT written", four lines above the block that writes them.

**Fix.** `if not isinstance(_prior, dict): _prior = {}` immediately after the parse — or raise a
Refusal naming the file, the way `validate_gate_runner` refuses a non-list command. Amend the S10
comment to say the five keys are carried forward on `--re-adopt`.

**Left-shift gate.** Extend the existing "reds rather than raising a traceback" arm
(`selftest.py:5900`) to a table of target-supplied malformed inputs — `null`, `123`, `[]`, `["orders"]`,
`"orders"` — asserting a Refusal for each. Same table for every other target-controlled JSON read.

### M4 — the "announces its argv" arm is a `print(` substring scan over the whole function body

`tools/govkit/selftest.py:5607` and `:5614`. Round-1 ids 24 and 8.

`_inside = "print(" in _body`, over the entire function source. `decline_findings` spans
`govkit.py:1790-1971` and already contained an unrelated `print(` at 1861 (`is OUTSIDE this run's
selection`) BEFORE D1 added the announcement at 1961-1962.

Simulated the deletion via AST — removed the announcement statement, re-parsed, re-extracted the body:
announcement gone, `print(` still present, arm still green. The generic arm cannot RED for this site,
nor for any future `target` row whose function holds any print at all. Only the fixture-level arm at
`selftest.py:5731-5733`, which greps the actual `RUNNING a target-authored probe` string in stdout, has
teeth — and it is `decline_findings`-specific.

The stronger half: the comment at `govkit.py:1765-1767` claims "the arm asserts both" properties. The
second property — not reachable from a default verb — is asserted by no generic arm whatsoever. That
is precisely how B1 and B2 survived the fold.

**Fix.** Assert the observable, not the shape: for each `target` site, run the fixture and require the
resolved argv to appear in stdout, as the `--run-discharge` arm already does. Then add the missing
second arm — for each `target` row, assert the function is not reachable from `cmd_plan` / `cmd_check`
without an opt-in flag — or delete the claim from the header.

**Left-shift gate.** The behavioural arm is the gate. Ban source-substring assertions as evidence of a
runtime property in this suite; a comment beside the arm saying so is cheap and this file has already
paid for the lesson twice.

### M5 — `decline_findings`' signature and first docstring line still say `{dest: state}` after D8 re-keyed it

`tools/govkit/govkit.py:1790-1793`. Round-1 id 12.

The annotation reads `-> dict[str, str]` and the docstring's opening sentence says `return {dest:
state}`, while the body at 1832 is `out: dict[tuple[str, str], str] = {}`, the docstring paragraph
twenty lines below says `Returns {(kit, dest): state}`, and both call sites unpack the pair
(`cmd_check:2175` does `for (_kit, _dest), _st in ...`).

No runtime effect. But it is exactly the dest-keyed reading D8 was raised to eliminate, left standing
in the two places a reader looks first. Rated at the top of low / bottom of medium; it is filed here
because the fold's own stated purpose was to make that reading impossible.

**Fix.** `-> dict[tuple[str, str], str]`, and change the docstring's first line to `{(kit, dest):
state}`.

**Left-shift gate.** Run a type checker over `tools/govkit/` as a bar leg. This is one of the few
findings in the round that a mechanical tool would have caught for free.

---

## LOW

### L1 — D3's liveness assertion is on the HIT set, so the ratchet's own goal state reds forever

`tools/check-install-prefix.sh:193` (`--write-ratchet`) and `:213` (`--check`). Round-1 ids 5 and 10 —
the same defect at both call sites.

`rows=$(carried_rows)` is the population filtered to files with `n>0` hits. `carried_population`
(lines 129-155) is the derivation whose death the assertion means to catch. So a live derivation over a
repo that genuinely carries zero prefix literals is indistinguishable from a dead one.

**Reproduced with a positive control.** Stubbed kit-source fixture, one shipped file: with
`tools/govkit/govkit.py` in its body, `--write-ratchet` exits 0 and prints `wrote 1 carried-prefix
row(s)`. Change that one literal to the `{{TOOL_ROOT}}` placeholder form the gate's own arm 9 blesses,
and the identical run prints "the derivation produced no rows at all, which means it DIED rather than
that this repo ships nothing" and exits 1. `--check` is blocked the same way, so the correct verdict
never prints.

DEPL-dCarriedReceipt-15's stated direction is to shrink these counts to zero, and the awk at 229-246
already handles a per-file zero with `(delete the row)`. On the day the repo reaches the goal, this leg
reds with a false statement and no override short of editing the gate. Reach is the endpoint rather
than today's tree, hence low.

**Fix.** Assert liveness on the producer: `pop=$(carried_population | tr -d '\r')`, red when `$pop` is
empty, derive `rows` from `$pop`, and let `rows` reach zero freely. Both branches.

**Left-shift gate.** A test arm that runs the whole script against a fixture kit source carrying zero
literals and asserts exit 0 with a clean verdict — the goal state, gated.

### L2 — the D5 lock-ordering arm cannot observe the ordering it names

`tools/govkit/selftest.py:5976`. Round-1 ids 11 and 18.

The arm claims the lock is taken BEFORE the existence guard, and asserts `not (_t5l / '.governance' /
'install.json').is_file()`. `_t5l` comes from `a13_target` (`selftest.py:5009-5030`), which writes
`deploy.toml` plus the held files and no `install.json`. The existence guard at `govkit.py:5669` (`if
receipt_path.is_file() and not re_adopt`) is therefore inert for this fixture, and the receipt write
sits at the very end of the function — so with the lock held, EITHER ordering refuses at
`take_write_lock` and writes no receipt. Moving `take_write_lock` back below the guard leaves the arm
green. The check-then-mutate window D5 identified is guarded by nothing.

**Fix.** Run the ordering arm over a fixture that DOES carry a receipt: plant the lock, plant an
`install.json`, run `adopt --write` without `--re-adopt`, and assert WHICH refusal fires — the lock
one, not the "already carries a receipt" one. That is the only assertion that distinguishes the two
orderings.

**Left-shift gate.** Same arm. Generalise the rule: an ordering claim needs a fixture in which the two
orderings produce DIFFERENT observable output, and the arm must name which output it saw.

### L3 — the D8 "wrong kit for a destination" arm is satisfied by its own fixture

`tools/govkit/selftest.py:5924`. Round-1 id 17.

Both conjuncts pass with D8 reverted. `'GAP' in _p8.stdout` is satisfied by the unrelated `demo` gaps
the fixture creates — `_t8` holds only `scripts/demo/one.py`, so demo's other sources are genuine gaps.
And `'scripts/sib/one.py' in _p8.stdout.split('coverage:')[0]` is satisfied by the plan-row loop at
`govkit.py:1994-1999`, which prints every `write` row, including the sib one, BEFORE the summary line
that supplies the split token. Under the old dest-keyed map — which per the docstring at 1818-1823 hid
B's gap entirely — this arm would still have reported green.

Only the sibling arm at `selftest.py:5926` (`ships no such destination`) discriminates. The arm that
names the defect is not the arm that catches it.

**Fix.** Assert on the GAP line itself: `any(l.startswith('  GAP') and 'scripts/sib/one.py' in l for l
in _p8.stdout.splitlines())` — false under the dest-keyed map, true under the pair-keyed one.

**Left-shift gate.** Ban `X in stdout` as an arm predicate where `X` also appears in unrelated output
of the same run; anchor on the line prefix that only the mechanism produces.

### L4 — the D1 `_announced` window accepts one call site's print on behalf of every other

`tools/govkit/selftest.py:5611`. Round-1 id 19. Distinct expression from M4, distinct failure mode.

`_announced = any(any("print(" in _g5lines[j] for j in range(max(0, ln - 12), ln)) for ln in
_callsites)` — the outer `any` means ONE announcing call site satisfies the arm for every other, and
the inner test is a bare `print(` substring scan over source lines.

`read_gate_verdicts` is called twice: `govkit.py:3360` is preceded by the print at 3357-3358;
`govkit.py:3951`'s twelve-line window (3940-3951) holds only comments, a `for` loop and `r.fail` — no
print. The arm reports the property held while one of the two spawns is silent. The product is
arguably fine (the argv is announced once per run before both identical spawns), but the guard asserts
a code shape rather than the property.

**Fix.** Folded into M4's fix: assert the resolved argv reaches stdout in a live run, per target site,
and drop the source-window heuristic.

**Left-shift gate.** As M4.

### L5 — the `FILENAME == pinf` awk swap is unarmed; reverting it leaves the suite green

`tools/check-install-prefix.sh:235`. Round-1 id 25.

**Measured.** Replaced `FILENAME == pinf` with `NR==FNR` in the working tree and ran `bash
tools/check-install-prefix.test.sh`: all 22 arms ok, PASS, exit 0. Restored with `git checkout --`,
tree clean.

The unreachability is structural, not luck. The awk roles only diverge when file 1 has ZERO records,
and the sibling `-s` guard at line ~205 exits 1 on an empty ratchet before awk is ever invoked; a
comment-only or newline-only ratchet still has records, so `NR==FNR` distinguishes correctly there. The
test file admits this in its own prose at lines 188-192, and the two D4 arms only assert "no SLACK" and
"says run --write-ratchet once" — both satisfied by the `-s` guard alone.

Per §7, a gate change whose failing case has never been observed is an assertion about nothing, and the
next person tidying that awk can undo it silently.

**Fix.** Either give it a case only it can catch — invoke the awk directly with a zero-record first
file and assert the roles do not invert — or delete `-v pinf` and the rule and keep `NR==FNR`, since
`-s` already makes the divergent input unreachable. Do not leave a defended-by-nothing branch beside a
comment explaining why it is load-bearing.

**Left-shift gate.** Whichever way it goes, the arm is the gate: stage the break, confirm RED, unstage.

### L6 — the `_silenced` hoist re-introduced a second full index read in `_cmd_apply`

`tools/govkit/govkit.py:3768`. Round-1 id 21.

`set(tracked(target))` now runs at 3768 (inside the hoisted `_silenced` comprehension) and again at
3783. `tracked()` is `git ls-files -z` over the whole target (`govkit.py:115-116`), so the manifest
branch pays two full index walks for one question. Nothing between the two calls mutates the index —
JSON read and dict construction only — so both return the same answer. No correctness bug.

The S6 comment at 3780-3782 ("ONE index reader for the bar and for the guard branch … two spellings of
one question, in the one function where they have to agree") now describes a state the code no longer
holds, three lines above the second call. That is the misinforming half.

**Fix.** Compute `tracked_target = set(tracked(target))` once above the kind split and pass it into
`silenced_legs`.

**Left-shift gate.** Honestly, none worth building — a per-function duplicate-call linter would cost
more than it saves. The compensating check is that the comment and the code are now one edit apart, so
fixing the code fixes the comment.

---

## Checked and found clean

Stated because a review that reports only hits is indistinguishable from one that only looked at hits.

- **The `cmd_adopt` / `_cmd_adopt` split and its `finally`.** `release_write_lock` (`govkit.py:3188`)
  early-returns when the module-global `_HELD_LOCK` is `None`, and `_HELD_LOCK` is set only after a
  successful `O_EXCL` create (`govkit.py:3183`). So a read-only run cannot release a lock it never
  took, and no run can release another process's lock. The `finally` covers every exit including the
  three refusal paths. The specific suspicion raised against this fix does not hold.
- **`trap … EXIT` in `tools/check-install-prefix.sh:225`.** It is the only `trap` in the file, so it
  clobbers nothing. `mktemp` plus the trap does remove the D12 tree-dirtying defect it was written for.
- **`plan --coverage`.** No longer reaches the decline discharge spawn — verified separately while
  reproducing B2.
- **`_cmd_apply:3648`.** Carries the same token-injection shape as B1/B2 but sits behind a writing verb
  that already demands `--write` and the worktree preconditions. Not escalated; it becomes free to fix
  the moment B1's boundary check lands, since that check is upstream of every consumer.

## What this round says about the method

Four of the fourteen fixes shipped with an arm that was measured green after reverting the fix (M1, L2,
L3, L5). Two more (M4, L4) assert a source-code substring in place of a runtime property. The fold was
written under the correct instinct — every fix got an arm — and the arms were not run against their own
staged break. §7 already states the rule: **a new gate is not landed until its failing case has been
observed.** The cheapest change to this build's remaining work is to make that a mechanical step of the
fold rather than an intention: for every arm added, revert the fix, run the suite, confirm RED, restore.

The second lesson is narrower and sharper. `SHELL_EXEC_SITES` is a hand-typed trust label, and B1, B2,
H1 and M2 are all one defect wearing four hats: **a declared population whose labels a human types will
be wrong, and a gate that reads those labels inherits the error.** Derive the label from the call graph
and the whole cluster closes at once.

---

## FOLD RECORD — round 2 closed, 2026-08-26, node `a`

All twenty-one findings are folded. The blockers went first and were folded before this record was
written; what follows is the six that remained, and the method note above is why they are recorded
with the break each arm was watched to fail on rather than with a claim that they hold.

- **M4 + L4 — the source-substring arms are DELETED, not repaired.** Replacing the predicate with
  the question it was pretending to ask produced a measurement worth more than the fix: of the six
  `target` spawn sites, exactly ONE prints its resolved argv before spawning it. The generic arm was
  reporting a property five sites do not have. So the claim is narrowed to what is observed —
  `_D1_ANNOUNCED` names, per site, the live stdout needle that proves the announcement or `None`
  with the reason it is unasserted, asserted against the declaration in both directions, and the
  five unasserted sites are PRINTED on every run. The engine's own header claimed a `target` site
  "owes an announcement and an opt-in"; both halves were false — `cmd_check` is on that list and is
  reachable from the read-only `check` verb by design — and the header now says what actually bounds
  those sites, which is `demand_safe_token` at the token boundary.
- **L2 — the D5 lock-ordering arm now observes an ordering.** The old fixture carried no
  `install.json`, so the existence guard was inert and EITHER ordering refused at the lock. The new
  arm plants the lock AND a receipt and runs `--write` without `--re-adopt`, so both guards want to
  fire and WHICH message returns names the order.
- **L3 — anchored on the GAP line.** `'GAP' in stdout` was satisfied by the fixture's unrelated demo
  gaps and the dest-substring by the plan-row loop above the split token. Now: a line that starts
  `  GAP` and names the sib destination, which only the gap emitter produces.
- **L5 — the awk role rule is armed, and its failing case was OBSERVED.** The arm extracts the awk
  program from the gate rather than copying it, and feeds it the one input the two spellings disagree
  on: a zero-record file 1. Staged the break (`FILENAME == pinf` → `NR==FNR`), ran the suite, saw
  exit 1 with exactly that one arm RED and no other, restored, re-verified clean.
- **L6 — one index read.** `tracked_target` is hoisted above the kind split and both consumers read
  it, so the S6 comment asserting `ONE index reader` is true again three lines below itself.

**On the method note.** It is right, and the escape rate on this fold is the evidence: four separate
shell-heredoc quoting escapes reached disk while folding these six. A \r inside a `tr -d` became a
literal carriage return; an awk backreference \1 became byte 0x01; a `$rows` was read one line above
its own assignment under `set -u`; and a \n inside a Python string literal became a real newline and
broke the parse. Each was caught by compiling the file or reading its bytes back, never by trusting
the write. The cheap fix is the one now in force: author anything containing a backslash with a file
write, never through a shell heredoc.
