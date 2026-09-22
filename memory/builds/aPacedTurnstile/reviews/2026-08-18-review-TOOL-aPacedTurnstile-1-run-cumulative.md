# Tier-2 cumulative review — the aPacedTurnstile unattended run

**Reviewed range:** `497d25d0ab47e29b29f08189473adf05f926399f..HEAD` (HEAD = `27ce5c3`, 11 commits).

**Serves:** diff-review TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7

**Date:** 2026-08-18 · **Tier:** 2 · **Streams:** tooling · **Round:** cumulative (post-run)

**Review shape:** raw 27 · confirmed 24 · refuted 3 · unverified 0 · **precision 0.89**.
Every finding below survived an adversarial skeptic pass that defaults to refute; three raw lenses
(ids 5, 12, 20) did not survive and are not reported. Nothing is outstanding.

**Subject — two halves.**
(1) **RECORDS:** the fork sweep across the seven specs, three adversarial spec-audit rounds
(round 2 BLOCKED on 29, round 3 BLOCKED on 23, round 4 CLEAN WITH FIXES on 7) and their folds.
(2) **CODE:** `TOOL-aPacedTurnstile-1`, the promotion of `tools/run-gates.sh` from a gov-internal
script to a deployable govkit kit (`25842ea`, `237fd62`, `27ce5c3`).

## Verdict: BLOCKED

**Records half: clean.** No finding survived on the records half. The three prior rounds and their
folds are the audit; this pass re-read the folds only far enough to confirm the round-4 verdict
still stands against the spec set as it landed. The round-4 observation that the multi-carrier
partial-fold pattern has not stopped is recorded context, not a new finding — it is already carried
in that round's report.

**Code half: two blockers and twelve highs, in a kit that now ships.** The finding-level tally is
2 BLOCKER · 12 HIGH · 8 MEDIUM · 2 LOW; deduplicated across verifier lenses that landed on the same
line, that is **12 distinct defects: 1 blocker, 6 high, 3 medium, 2 low**.

The headline is not any one defect. It is that **the full bar is GREEN at 73/73 on this tip while
two blockers and six highs are live in the shipped payload.** Every one of them lives on the far
side of a seam the bar does not cross: what the kit does in an adopter's tree, at an adopter's
prefix, read by the deployer's own reader. The kit's own legs run in gov's tree at gov's prefix
against hand-written fixtures, so they cannot see any of it. That is the same silent-green direction
this deployer refuses by name in a dozen other places, reintroduced by the file that promotes the
bar itself.

Three families account for eleven of the twelve distinct defects:

1. **Type divergence on the `[gate_runner]` declaration** (D1 blocker, D2, D8, D11). The emitter
   writes scalars, the reader iterates lists, the adopter's drift check parses only scalars, and the
   deployer's only executable fixture is hand-written in the third shape. Whichever shape the seed
   settles on, at least one consumer reads garbage or nothing — and both directions fail *green*.
2. **Gov's prefix and gov's corpus spelled inside shipped files** (D4, D5, D6, D12). Three shipped
   harnesses hardcode `tools/run-gates/` or grep gov's own `.githooks/pre-push`. Any adopter not at
   the `tools` prefix — and any default `govkit apply`, which does not ship `push-main` — receives a
   merge bar that is red on arrival and stays red. `check-install-prefix.sh` excludes `*.test.sh` by
   design, so nothing catches it.
3. **Regressions the kit promotion introduced into the runner itself** (D3, D7, D9). A gate leg that
   guards a file `apply` itself creates and wedges the target on the second run; an adopter CLI that
   spins forever on `--help`; and a manifest derivation that collapses to `./gate-legs.json` when the
   runner is invoked by relative path — the exact zero-legs-exit-2 failure mode this promotion was
   written to eliminate.

---

## Findings

Severity-ranked, blockers first. Each defect lists the raw finding ids that landed on it.

### D1 · BLOCKER · `tools/run-gates/kit.toml:91` + `tools/govkit/govkit.py:2860` — the `observed_*` declaration is a TOML **string**; its only consumer iterates it as a **list**

*(raw ids 1, 15)*

`[gate_runner_seed]` declares `observed_ran = "GATE ok    {name}"` / `observed_failed = "GATE FAIL  {name}"`
as scalars (`kit.toml:91-92`), and `cmd_intake` emits every allowlisted seed key through
`f'{k} = "{resolve_seed_value(seed[k])}"'` (`govkit.py:2859`), so a target's `deploy.toml` carries
scalars. The sole consumer, `read_gate_verdicts`, does `for tmpl in (gr.get(key) or [])`
(`govkit.py:1618`) — which walks a `str` **character by character**.

**Reproduced live.** `govkit intake --kits run-gates` into a fresh repo, then the reader against real
runner output: `{'ATE ok': 'green', 'ATE FAIL': 'green', 'ATE skip': 'green'}`. The head is the
single character `G`, no real leg name ever appears, and a **FAILING** leg's line is classified
`green`. Because `observed_ran` is scanned first and `setdefault` wins, **no key can ever be `red`**.
A real `govkit apply --kits run-gates` into a fresh target recorded
`after = {'ATE FAIL': 'green', 'ATE ok': 'green', 'grep: …/.githooks/pre-push: No such file or directory': 'green', …}`
and **exited 0 while the target's `run-gates canary` leg was genuinely RED**.

Everything downstream is therefore garbage: `before_map`/`after_map` in `cmd_apply`
(`govkit.py:2404-2426`), the `on_baseline_red` report, the DEAD-PROBE guard, and all four regression
branches — `leg was green before and is red after`, `…did not execute after`, `…is gone after`,
`did not exist before and is red after` — are unreachable. `validate_gate_runner` only tests
truthiness (`missing = [k for k in GR_REQUIRED if not gr.get(k)]`) and type-checks only `command`,
so nothing refuses the scalar. `run-gates` is in `registry.toml`'s `[selection].default`, so this is
the shape **every** intake-written target carries.

Nothing on the bar can see it: `selftest.py:831` and `matrix.py:141` both hand-write the **array**
form, and every intake arm (`selftest.py:1149`, `:1159`, `:1303`) selects `check-wiring`/`playbook`/
`drift-audit` — never `run-gates`. The emitter and the reader have never met.

**Fix.** Declare arrays in the seed (`observed_ran = ["GATE ok    {name}"]`), teach `cmd_intake` to
emit a list value as a TOML array instead of quoting every value, **and** add a type assertion in
`validate_gate_runner` so a scalar `observed_*` is a named refusal rather than a silent character
walk. Do all three: the assertion is what stops the next kit repeating it.

**Left-shift gate.** A seed→emit→read round-trip arm in `tools/govkit/selftest.py`, parameterised
over **every registry entry declaring a `[gate_runner_seed]`** — run `cmd_intake`, feed the emitted
`deploy.toml` to `read_gate_verdicts` against a line the runner really prints, and assert the bare
leg name and the right state come back. Written generically it is one arm and it retires this whole
family, including for kits that do not exist yet.

---

### D2 · HIGH · `tools/run-gates/adopt-run-gates.sh:89` — the drift check parses only the scalar form and fails **open** on the shape the deployer actually consumes

*(raw ids 2, 10, 17)*

`read_declared` is `sed -n 's/^[[:space:]]*KEY[[:space:]]*=[[:space:]]*"\(.*\)"[[:space:]]*$/\1/p'` —
quoted-scalar only. Against `observed_ran = ["GATE ok    {name}"]` it returns empty, both keys read
absent, and lines 94-98 print `NOT ADOPTED — … declares no [gate_runner] observation strings` and
**exit 0**, without ever opening the runner.

**Reproduced in a scratch target.** With the array form declared, `--check` exits 0 on the NOT
ADOPTED path. I then rewrote *both* printf heads in the installed runner to `XXXXXXX  ` / `YYYYY  `
— total drift, the deployer can now match nothing — and `--check` still exited 0 with the same line.
The `grep -qF` against the runner sits *after* the NOT ADOPTED return, so it is never reached.

This is the one join the kit exists to assert (S7 / AC5), carried by the `run-gates wiring` gate leg
whose `guard = []` means it runs on **every** target's bar. It is dead for exactly the declaration
shape `read_gate_verdicts` needs. Combined with D1: whichever shape the seed settles on, one of the
two consumers reads nothing, and a `NOT ADOPTED` exit 0 is indistinguishable from a target that
genuinely declares no runner. The e2e (`adopt-run-gates.test.sh:49`, `:110`) bakes in the scalar
form, so no arm covers the divergence.

**Fix.** Parse both shapes — strip an optional `[`/`]` and take the first quoted element — and make
a `[gate_runner]` table that is **present but unparseable** a refusal (rc 1) with a named message.
`NOT ADOPTED` must mean the table is absent, never that it is present in a shape this reader does
not understand. Assert the key was found inside the `[gate_runner]` section, not anywhere in the
file.

**Left-shift gate.** Stop hand-writing the fixture: `adopt-run-gates.test.sh` should build its
`.governance/deploy.toml` by **running `govkit intake`**, never by `write_decl`. A fixture written by
hand can only test the shape its author imagined; a fixture written by the emitter tests the shape
the target actually receives. Add one arm that writes the array form explicitly and asserts the same
DRIFT red as arm 3.

---

### D3 · HIGH · `tools/run-gates/kit.toml:58` — the `run-gates canary` leg guards on `{prefix}/gate-legs.json`, a file this same `apply` creates, and the target ends permanently wedged

*(raw id 16)*

`guard = ["{kit}/", "{prefix}/gate-legs.json"]`. `tracked_target` is computed at `govkit.py:2328`,
**before** the manifest is written and `git add`ed at `:2382-2384`.

**Reproduced end to end** against a scratch target:

- **apply #1** — the guard entry matches no tracked path, so it is silently dropped; the receipt
  records `guard: ['tools/run-gates/']` with
  `guard_dropped: [{'spec': 'tools/gate-legs.json', 'why': 'matches no tracked path in the target'}]`.
- **apply #2** — the manifest now exists, both guard entries resolve, `prev.get('guard')` mismatches
  the receipt, and govkit exits 1 with
  `leg 'run-gates canary' in the target differs from what the receipt recorded`. The receipt is
  nonetheless **re-stamped** (the write at `:2426` is unconditional) with the canary missing from
  the emitted names.
- **apply #3** — hard refusal:
  `the target's runner already has a leg named 'run-gates canary' and this target's receipt does not claim it`.

The kit is a one-shot install and the target is permanently wedged for it. It also means the canary
never re-runs when the target's manifest changes — the one file it grades. No other `kit.toml` in
the registry guards a path `apply` itself produces.

**Fix.** Drop `{prefix}/gate-legs.json` from the guard — `{kit}/` already covers the canary's own
sources — or move govkit's `tracked_target` refresh so leg guards resolve *after* the manifest is
written and staged. Prefer the second: it fixes the class, not the row.

**Left-shift gate.** `tools/govkit/matrix.py` gains a shape: **apply the default selection twice into
the same target.** The second apply must be a clean no-op, not a refusal and not a drift report.
That single arm is idempotence, which is the property `apply` needs and never asserts.

---

### D4 · HIGH · `tools/run-gates/run-gates.test.sh:118` — the SHIPPED canary hardcodes gov's install prefix in the one line that reads the real runner

*(raw ids 6, 23)*

The file derives `KITDIR`/`ROOTN`/`KITREL` at lines 52-55 and uses `$KITREL` everywhere else — then
arm 3 reads the installed runner as `cp "$ROOT/tools/run-gates/run-gates.sh" …`.

**Reproduced at a non-gov prefix.** Installed the kit at `vendor/run-gates` in a scratch repo:
`cp: cannot stat '<root>/tools/run-gates/run-gates.sh'`, then arms 3a-3j all red against empty output
(`expected 4 GATE lines from the scratch bar, got 0`; `width-4 produced 0 rendezvous record(s)`;
five `GATE_JOBS` clamp arms each `bash: tools/run-gates/run-gates.sh: No such file or directory`).
There is no `set -e`, so the failed `cp` is silent.

The prefix is genuinely operator-editable — `target_context` reads
`prefix = (deploy.get("prefix") or "tools").strip("/")` (`govkit.py:460`) and this kit's own e2e
installs at `vendor` on purpose. This file ships (`kit.toml [[files]] include = "**"`, role engine)
and is emitted as the `run-gates canary` `[[gate_leg]]` into every adopter's manifest, so any target
not at `tools` gets a merge bar red from the first run. `check-install-prefix.sh:48` excludes
`\.test\.sh$` by design, so nothing catches it.

The later `tools/run-gates` spellings (lines 166, 261, 277-278, 312-313) are the scratch fixture's
own self-consistent layout and are **not** the defect. Line 118 alone is, and `$KITDIR` is already
in scope.

**Fix.** `cp "$KITDIR/run-gates.sh" "$SCRATCH/tools/run-gates/run-gates.sh"`.

**Left-shift gate.** See D6 — one gate covers D4, D5, D6 and D12.

---

### D5 · HIGH · `tools/run-gates/run-gates.evidence.test.sh:19` — the shipped evidence harness spells gov's prefix, and the parity arm written to catch this does not cover the file

*(raw ids 7, 24)*

`RUNNER="$ROOT/tools/run-gates/run-gates.sh"` — the file's only `tools/` spelling, with no
derivation, while its sibling `run-gates.test.sh:52` derives `KITDIR` through `cd "$(dirname "$0")" && pwd`
under a comment saying a hardcoded prefix "would be a gov spelling in a harness that now ships
(S1/S3)".

**Reproduced at a `vendor/` prefix:** 10 of 11 assertions FAIL, every `run()` at rc=127
(`an absent git dir was not refused cleanly (rc=127)`, `an unreadable GATE_LEGS did not fail cleanly (rc=127)`),
and the one assertion that "passes" —
`gate-last-summary.txt carries a pointer, not raw leg output` — passes **vacuously**, because it is a
negative assertion over a file that was never written. `kit.toml` ships this as the `run-gates evidence`
`[[gate_leg]]`, so an adopter's merge bar carries a leg that can never be green.

The gov canary's source-parity arm G2 iterates exactly
`for f in "$KITREL/run-gates.test.sh" "$KITREL/run-gates.gov.test.sh"` — so the one shipped file that
spells gov's prefix sits **outside** the parity population that exists to catch this.

**Fix.** `KITDIR=$(cd "$(dirname "$0")" && pwd); RUNNER="$KITDIR/run-gates.sh"`, and add this file to
G2's parity loop.

**Left-shift gate.** See D6.

---

### D6 · HIGH · `tools/run-gates/run-gates.test.sh:368` — arm 3j in the SHIPPED half asserts a fact about **gov's** tree, in the half whose contract is that every assertion be true in any tree

*(raw ids 8, 25)*

`grep -q '^export GATE_FULL=1$' "$ROOT/.githooks/pre-push"` with no existence guard and no `set -e`.
A missing file gives grep exit 2 → `fail=1` → the leg exits 1.

`.githooks/pre-push` is claimed **only** by the `push-main` entry
(`tools/govkit/entries/push-main.kit.toml:20`), which is **absent** from
`registry.toml:37 [selection].default`, while `run-gates` is present — and
`tools/run-gates/kit.toml:15` declares `requires = []`. run-gates ships no pre-push of its own.
Confirmed on a scratch target: no `.githooks/` exists, grep exits 2, the canary exits 1. **A default
`govkit apply` therefore lands a gate leg that is red on arrival and forever**, and the leg's own
guard is satisfied by the install itself so it runs immediately.

This is `memory/gotchas/pin-copied-from-another-corpus.md` sitting in the half created to prevent it:
`tools/run-gates/README.md:31` and the gov harness header both state that every assertion in the
shipped canary is true in any tree.

**Fix.** Move arm 3j verbatim into `tools/run-gates/run-gates.gov.test.sh` (bump its
`FLOOR_ASSERTIONS`) and drop it from the shipped canary, adjusting `FLOOR_ASSERTIONS=35` there. The
gov-only half is the right home: the claim is about gov's own push boundary.

**Left-shift gate (covers D4, D5, D6, D12).** `tools/govkit/matrix.py` gains a shape: **install the
default selection into an empty repo at a NON-default prefix (`vendor`), then run the emitted bar and
require it green.** One arm, and it is the only thing that would have caught all four — plus D3 and
D7 as a side effect. Secondarily, widen `check-install-prefix.sh`'s population: `*.test.sh` is
excluded wholesale today, but a `*.test.sh` that a kit **ships** (per its `[[files]] include`) should
be in scope, and the alternation should include `gate-legs.json` as well as kit directories.

---

### D7 · HIGH · `tools/run-gates/adopt-run-gates.sh:36-37` — `--help` and any unknown flag call an undefined `usage` and spin forever

*(raw ids 22 · 3, 9, 18)*

The function defined at line 20 is `print_usage`; lines 36 (`-h|--help) usage ;;`) and 37
(`*) echo "…unknown argument…"; usage ;;`) call bare `usage`. `set -u` is set, `set -e` is not, so
the command-not-found is non-fatal — and **neither branch shifts**, so `while [ $# -gt 0 ]` never
advances. Line 35's `print_usage` call is correct, which is what hides it.

**Reproduced.** `timeout 6 bash tools/run-gates/adopt-run-gates.sh --help` exited 124 after emitting
408 lines of `line 36: usage: command not found`; `--bogus` exited 124 with 778 lines alternating the
unknown-argument message and `line 37: usage: command not found`.

Two separate blast radii. (a) This is the kit's only CLI and both `[adopt].argv` and `[check].argv`
invoke it — an operator's `--help` or typo hangs instead of exiting 2, and under an unattended driver
it hangs the *run* rather than failing it. (b) It is also a **bar leg** (`run-gates wiring`), and
`runleg` in `run-gates.sh:191` captures leg output with `out=$(…)` and applies **no timeout** — so one
stray argv token in an emitted manifest hangs the whole pool forever while the command substitution
grows unbounded. On the push boundary that is a hang, not a red: the same class the `GATE_JOBS`
length clamp at `run-gates.sh:170-177` was written to eliminate.

**Fix.** Rename both call sites to `print_usage` (it already `exit 2`s, so no shift is needed). Two
words.

**Left-shift gate.** Two, and both are cheap. (1) A govkit selfcheck predicate: every entry's
`[adopt].argv` / `[check].argv` script must answer an unknown flag under `timeout` with rc 2 and
usage text on stderr — an unbounded-loop branch that no arm exercises is exactly how this shipped.
(2) Give `runleg` a per-leg timeout so a hung leg reds with a named message instead of hanging the
bar. The bar should not be able to hang, whatever a leg does.

---

### D8 · MEDIUM · `tools/run-gates/kit.toml:92` — no `observed_skipped` is declared, so the deployer's `skipped` state is unreachable and its DEAD-PROBE refusal is structurally dead

*(raw ids 4, 13)*

The runner emits `GATE skip  %s  (unchanged vs %s)` (`run-gates.sh:219`), but `[gate_runner_seed]`
declares only `observed_ran`/`observed_failed` — the key `observed_skipped` appears at
`govkit.py:1617` and **nowhere else in the repo**. `cmd_intake`'s emission loop (`govkit.py:2859`)
iterates a fixed 7-key tuple, so a descriptor author who adds the key gets no emission **and no
error**.

`read_gate_verdicts`'s own docstring says the baseline is run **without** the run-everything escape
precisely so legs *can* report `skipped` — and the DEAD-PROBE refusal (`govkit.py:1950`) fires only
when `before_map` is non-empty and entirely non-green/red. With the key undeclared an all-skipped
baseline produces an **empty** map, the guard is false, and that refusal is unsatisfiable for every
run-gates target. Measured with a corrected array declaration: a runner printing
`GATE skip  gamma  (unchanged vs main)` yields `{'alpha':'green','beta':'red'}` — gamma silently
vanishes, so a guarded-and-skipped leg is indistinguishable from a vanished one. Guards are live in
a real target (every shipped `[[gate_leg]]` carries a `{kit}/` guard), so this is the normal case,
not the corner. `cmd_apply:2415`'s `b == 'green' and a2 == 'skipped'` branch ("the install broke its
guard") is dead code, and that case instead reports the wrong `is gone after` diagnostic.

**Fix.** Add `observed_skipped = ["GATE skip  {name}"]` to `[gate_runner_seed]` **and** include the
key in the emitter's tuple at `govkit.py:2858` — the seed alone would not reach a target. Make the
emitter **refuse** an unknown seed key rather than dropping it.

**Left-shift gate.** The same round-trip arm as D1, extended by one predicate: every state
`read_gate_verdicts` supports must be declared by an entry that declares any of them, or carry an
explicit waiver naming why the runner cannot produce it.

---

### D9 · MEDIUM · `tools/run-gates/run-gates.sh:68` — `KITDIR` is derived after `cd "$ROOT"`, so a relative invocation from a subdirectory collapses the manifest to `./gate-legs.json` and runs ZERO legs

*(raw ids 11, 19)*

Line 15 does `cd "$ROOT"`; line 68 then computes `KITDIR=$(cd "$(dirname "$0")" && pwd)` from a `$0`
that is now relative to the wrong directory.

**Reproduced.** From `memory/`: `bash ../tools/run-gates/run-gates.sh` prints
`line 68: cd: ../tools/run-gates: No such file or directory`, `LEGS_FILE` collapses to
`./gate-legs.json`, then `run-gates: cannot parse ./gate-legs.json`, **exit 2 with zero legs run** —
the named failure mode this promotion was written to eliminate. `git show 25842ea~1` confirms the
pre-move runner used `LEGS_FILE="${GATE_LEGS:-tools/gate-legs.json}"` relative to `ROOT` and was
cwd-independent, so this is a regression for any wrapper, CI step or operator invoking by relative
path.

Severity is capped at medium because it fails loudly (exit 2) and the repo-root and absolute-path
invocations still work. The aggravating detail is that the identical four-line block is copied into
`run-gates.test.sh:52-55` and `run-gates.gov.test.sh:73-77`, and gov canary G2 pins those lines
**byte-for-byte** across exactly those files — so **the parity arm certifies the copy rather than the
correctness**, in all three carriers at once.

**Fix.** Capture `KITDIR` before the `cd "$ROOT"`, in all three files so G2 stays satisfied, and
refuse loudly (`exit 2`, naming `$0`) if that `cd` fails instead of letting an empty `KITDIR` degrade
into `.`.

**Left-shift gate.** A canary arm that invokes the runner **by relative path from a subdirectory** and
asserts the manifest resolved. More generally: a byte-parity arm needs a behaviour arm beside it, or
it certifies three copies of one bug — worth a line in the review protocol.

---

### D10 · MEDIUM · `tools/run-gates/run-gates.test.sh:107, 177, 187, 295, 299` — five assertion counters sit **inside** the failure branch, so the executed count under-reports on every green run

*(raw ids 14, 26)*

Line 107 sits inside the `if grep -qF …` body (hardcoded-leg-path scan), 177 inside
`if [ "$s1" != "$s4" ]` (width-1 vs width-4 report equality), 187 inside `if [ "$ordered" != "$want" ]`
(manifest order), and 295/299 inside the two arm-3g failure bodies — the latter two within a
4-iteration loop, so ten executed assertions contribute zero on the green path.

**Measured.** The green run prints `PASS (35 assertions)` against `FLOOR_ASSERTIONS=35` (line 45) —
**zero slack**, and the floor exactly equals the set of correctly-placed increments. Summing only
those with their loop multiplicities gives precisely 35. So arm 3a, the manifest-order arm, the
hardcoded-path arm and both 3g arms could be **deleted** with the printed count unchanged and the
shrink-only floor still green. That directly contradicts the counter's own contract at lines 43-44
("an EXECUTED assertion count, incremented at each assertion rather than written as a literal") and
is the same ratchet-that-does-not-ratchet class `tools/check-testsuite-counts.sh` was written for
after a suite printed a hardcoded `PASS (130 assertions)` for its whole life. A corollary: a **red**
run reports a *higher* count than a green one, which is incoherent for a floor.

**Fix.** Move each of the five increments above its `if`/`||`/loop body so it runs on both paths, then
re-measure and raise `FLOOR_ASSERTIONS` to the new green count.

**Left-shift gate.** Make the increment impossible to misplace: a single `ok()`/`assert()` shell
helper that evaluates the condition and increments in one place, and a `check-testsuite-counts.sh`
predicate rejecting a bare `n=$((n+1))` outside that helper. A counter you can put on one branch is a
counter that will be put on one branch.

---

### D11 · LOW · `tools/govkit/selftest.py:808` — the deployer's only executable model of a runner still prints the RETIRED single-space tail

*(raw id 21)*

The fixture emits `GATE FAIL  %s (exit %d)`; the shipped runner emits two spaces before every tail
(`run-gates.sh:219-222`), and `git log -S` confirms the widening landed in this build's `25842ea`.
The widening exists so `read_gate_verdicts`'s `split("  ")[0]` recovers the bare leg name from a
variable tail — and **that split now has zero consumer-side coverage**, because the only fixture that
exercises the parse emits a tail the split cannot separate. The fixture is internally broken under
its own declaration too: with `observed_failed = ['GATE FAIL  {name}']` (`selftest.py:832`) and output
`GATE FAIL  control (exit 1)`, the reader returns the leg name `'control (exit 1)'`. The only other
model, `matrix.py:135`, emits no tail at all. A mis-parsed name would defeat `exempt_leg`'s name match
in the `b is None and a2 == 'red'` branch (`govkit.py:2421`).

**Fix.** `'GATE FAIL  %s  (exit %d)'`, plus an arm asserting the parsed red key equals the **bare** leg
name.

**Left-shift gate.** Same root as D1/D2: fixtures that model a runner should derive their format from
the shipped runner's declared tail contract rather than restating it. One declared constant, two
readers.

---

### D12 · LOW · `tools/run-gates/run-gates.sh:6` and `:54` — the header and the no-python refusal still name `tools/gate-legs.json`, contradicting the derivation 14 lines below

*(raw id 27)*

Line 6 states "Legs live in tools/gate-legs.json (single source)" and the refusal reads
`run-gates: no usable python — required to parse tools/gate-legs.json`, while lines 61-71 derive
`LEGS_FILE` as the kit dir's sibling under a comment explicitly saying a hardcoded
`tools/gate-legs.json` "resolves to nothing at any other prefix". Two answers to one question inside
one file. The refusal is reachable in exactly the tree where it matters — an adopter with no usable
launcher, the case `resolve_python` exists for — and sends them to a path that does not exist there.
`check-install-prefix.sh:38` derives its alternation from `git ls-files -- 'tools/*/*'` directories
only, so a bare file path is outside it and carries no waiver row.

**Fix.** Move the `PYBIN` guard below the derivation and interpolate: `…required to parse $LEGS_FILE`.
Reword line 6 to say the manifest is the kit dir's sibling.

**Left-shift gate.** Covered by D6's widened `check-install-prefix.sh` population — add
`gate-legs.json` to the derived alternation so a spelled manifest path in a shipped file needs a
waiver row like every other spelled kit path.

---

## Raw finding id → defect map

Every id in the confirmed set is accounted for; no id was dropped.

| Defect | Severity | Raw ids | Site |
|---|---|---|---|
| D1 | blocker | 1, 15 | `tools/run-gates/kit.toml:91` · `tools/govkit/govkit.py:2860` |
| D2 | high | 2, 10, 17 | `tools/run-gates/adopt-run-gates.sh:89` |
| D3 | high | 16 | `tools/run-gates/kit.toml:58` |
| D4 | high | 6, 23 | `tools/run-gates/run-gates.test.sh:118` |
| D5 | high | 7, 24 | `tools/run-gates/run-gates.evidence.test.sh:19` |
| D6 | high | 8, 25 | `tools/run-gates/run-gates.test.sh:368` |
| D7 | high | 22, 3, 9, 18 | `tools/run-gates/adopt-run-gates.sh:36-37` |
| D8 | medium | 4, 13 | `tools/run-gates/kit.toml:92` |
| D9 | medium | 11, 19 | `tools/run-gates/run-gates.sh:68` |
| D10 | medium | 14, 26 | `tools/run-gates/run-gates.test.sh:107,177,187,295,299` |
| D11 | low | 21 | `tools/govkit/selftest.py:808` |
| D12 | low | 27 | `tools/run-gates/run-gates.sh:6,54` |

Finding-level tally: 2 blocker · 12 high · 8 medium · 2 low = 24.

---

## The four gates that would have caught 22 of 24

Ranked by findings retired per unit of work.

1. **A non-default-prefix acceptance shape in `tools/govkit/matrix.py`** — install the default
   selection into an empty repo at `vendor`, then run the emitted bar and require it green.
   Retires D3, D4, D5, D6, D12, and surfaces D7 and D9. This is the single highest-value change in
   the report: eight of twelve defects exist only because no arm has ever run the emitted bar in a
   target that is not gov.
2. **A seed→emit→read round trip in `tools/govkit/selftest.py`**, parameterised over every entry
   declaring a `[gate_runner_seed]`. Retires D1 (blocker), D8, D11 and half of D2. The emitter and
   the reader of `[gate_runner]` have never been run against each other in this repo's history.
3. **Fixtures built by running the deployer, not by hand.** `adopt-run-gates.test.sh`'s `write_decl`
   and `selftest.py`'s fixture runner both hand-write shapes their authors imagined; both imagined
   wrong, in opposite directions. Retires the rest of D2 and hardens D11.
4. **A `runleg` timeout, and a shipped-CLI `--help` predicate.** Retires D7 and makes the bar
   structurally unable to hang.

Beyond the four: D9's byte-parity arm certifying three copies of one bug is worth a standing line in
`memory/guides/REVIEW-PROTOCOL.md` — a parity arm without a behaviour arm beside it proves the copies
agree, never that they are right.

## What the green bar did and did not buy

The bar is GREEN at 73/73 on `27ce5c3`, and that is an honest result for what it grades: gov's own
tree, at gov's prefix, with hand-written fixtures. It is not evidence about the payload. The
promotion moved `run-gates.sh` across the boundary from "a script this repo runs" to "a kit other
repos receive", and the leg population did not move with it. Until gate 1 above exists, a green bar
on this kit means the kit works **here** — which is the one place it was already known to work.
