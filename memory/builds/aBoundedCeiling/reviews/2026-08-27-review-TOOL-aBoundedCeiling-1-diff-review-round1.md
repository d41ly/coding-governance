## Verdict: BLOCKED

**Serves:** diff-review TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-5 TOOL-aBoundedCeiling-6

Three things are red or dead on this branch today. The first kills the kit's own self-test suite on its first executed line; the second reds an unguarded merge-bar leg; the third breaks two pre-existing arms by construction. None can land as-is.

---

### 1. BLOCKER — the new run_bounded arms abort the whole unattended suite
`tools/unattended/unattended.test.sh:4531`

`GATE_BOUND_LIVE=1 GATE_BOUND=2 . "$rb_fn"` is a prefix assignment on the `.` builtin. Bash outside POSIX mode does not persist those. Verified on this box:

```
$ bash -c 'set -u; V=9 . ./rbx.sh; f'
live=[UNSET]
```

`run_bounded`'s body (`tools/unattended/unattended.sh:180`) then expands `"$GATE_BOUND_LIVE"` with no default, the file sets `set -u` at :11, and the shell exits at the first call on :4536. The arm's own `>/dev/null 2>&1` swallows the `unbound variable` diagnostic, so the suite dies with **no FAIL line, no `PASS (n assertions)` line**, and the `FLOOR_ASSERTIONS` comparison at :4632 — the stranded-arm detector this file exists to carry — never executes. REGION TWO runs both unsharded and as shard 2, so this fires on every normal invocation, including `bash tools/unattended/run-unattended-gates.sh --selftests`, the gate spec-6 §7 names as its own.

Even with the abort fixed, `GATE_BOUND` would still be unset, `${GATE_BOUND:-0}` would be `0`, and all six timing arms would run the 60 s sleeper unbounded and fail their elapsed assertions.

**Fix:** plain assignments on their own line — `GATE_BOUND_LIVE=1; GATE_BOUND=2; . "$rb_fn"`. Same for the INERT arm at :4560 (`GATE_BOUND_LIVE=0` as a call prefix on a *function* does persist, but set it explicitly with a restore for symmetry). Then run the suite once: a green `PASS (n)` line is the only evidence any of this graded anything.

*(One sub-claim from the finder pool is wrong and should not go into the fix: `RB_OUT`/`RB_TOOK` do **not** need hoisting. The sed range excludes their initialisation, but the function body assigns both before returning, so `hit "$RB_OUT" "alive"` at :4552 runs after a completed call.)*

---

### 2. BLOCKER — the merge bar is red: unarmed `fail` branch
`tools/unattended/unattended.sh:1075`

Ran the leg exactly as `tools/gate-legs.json` declares it:

```
$ python tools/memory-tree/check-arms.py --check
HYGIENE check-arms: tools/unattended/unattended.sh:1075 check 4 branch 3 has no POSITIVE
assertion naming its own failure text ('the declared wiring check did not answer within the
declared') and is not pinned in memory/project/unarmed-branches.txt
EXIT=1
```

That leg carries no `guard` key, so it runs on every bar including a records-only one. Line 1075 is new in this diff and it is the *only* complaint, so this diff introduced the red.

The gate is reporting a genuine hole, not a false positive: spec-6 AC5 asks for exactly the arm that would satisfy it. The sibling breach at :2793 does not appear only because it sets `DOD_OUT` rather than calling `fail` — it is equally unexercised and simply unreported.

**Fix:** write the AC5 arm (see finding 4). Pinning it in `memory/project/unarmed-branches.txt` would green the gate while leaving the second call site — the entire reason `run_bounded` is one helper — unexercised.

---

### 3. BLOCKER — the defaulted-GATE_BOUND NOTE becomes line 1 of every driver capture
`tools/unattended/unattended.sh:292`

The NOTE is emitted at script init, before argv is parsed, unconditional on verb. `mkconf` (`unattended.test.sh:87-99`, called by `reset_tree` at :332) writes a fixture conf with **no** `GATE_BOUND`, and `run()` at :334 is `bash "$SCRIPT" "$@" 2>&1`. Nothing sets `UNATT_QUIET`. Reproduced against a mkconf-shaped conf: `--status`, `--plan` and even `--version` all return the NOTE as line 1.

Two arms break:

- `:1710` — `same "--plan lists the region's FIRST row first…"` does `head -1 | awk '{print $1}'` and now gets `unattended:` instead of `ARCH-tPlan-2`. Hard FAIL.
- `:1667` — `same "--status selects the same first row…"` pipes through `sed 's/.*· next //'`; the NOTE carries no `· next ` so sed passes it through, and a two-line string is compared against a one-line `want_unit`. Hard FAIL.

And one arm silently vacuates: `:838` greps `rout` for the first line of `sout`, which is now the NOTE in both captures — it passes by matching boilerplate and no longer compares the status line at all.

Gov's own tree is immune (`.unattended.conf:32` declares `GATE_BOUND="3600"`), so this lands entirely on the fixture population and on every adopter who has not edited their conf.

**Fix:** add `GATE_BOUND="3600"` to `mkconf` so the fixture matches a configured project, and cover the default-announcement path with one dedicated arm that expects the NOTE — that arm is spec-6 AC3, currently unasserted either way.

*(Sub-claim refuted: the Skill does not instruct adopters to capture `2>&1` — `grep 2>&1 tools/unattended/SKILL.template.md` is empty. The adopter-parsing impact is real but not something the kit told them to do.)*

---

### 4. HIGH — spec-6 AC1/AC3/AC4/AC5 have no arm; neither call site is driven
`tools/unattended/unattended.test.sh:4519-4564`

The whole new block sources `run_bounded` out of the driver with `sed -n '/^run_bounded() {/,/^}$/p'` and grades it standalone. Neither `--close` nor `--preflight` appears in it. `grep -n GATE_BOUND unattended.test.sh` returns only :4531 and :4560.

AC5 spells out why this matters in its own text: *"the helper has one exercised call site and one asserted only by inspection, which is how the sibling seam went unbounded the first time."* As built, **both** call sites are asserted only by inspection. Unexercised: that `local _grc=$?` / `local _wrc=$?` really capture `run_bounded`'s status after `&& { …; return 0; }` (`unattended.sh:1071-1073`, `:2785-2789`); that `DOD_OUT` carries the breach message rather than the bar's output; and that word-split `run_bounded $GATE_CMD` still executes the declared command line the way `$GATE_CMD 2>&1` did. A wrong variable name or an inverted 124/137 test ships green.

**Fix:** two verb-level arms with `GATE_BOUND=2` — a `--close` whose `GATE_CMD` sleeps past it (assert elapsed < 20 s and that the UNMET message names the bound), and a `--preflight` whose `WIRING_CHECK` does the same (assert elapsed and `"did not answer within the declared"`). The second also clears finding 2.

---

### 5. HIGH — nothing asserts run-gates.sh applies a ceiling at all
`tools/run-gates/run-gates.test.sh:116-162`, guarding `tools/run-gates/run-gates.sh:927-935`

Stage the deletion: replace :934's `timeout -k 5s "$bound"` branch with the unbounded else-branch. Then —

- arm 1c still passes: it runs its own `timeout` literal in the test's own process and never invokes the runner (its own header admits *"WHAT IT DOES NOT CHECK: that run-gates.sh USES this construct"*);
- arm 1d still passes: its regex `^[[:space:]]*[^#]*=\$\(timeout ` is a negative search that matches nothing when there is no timeout at all;
- gov G6 still passes: all 85 manifest rows still declare a ceiling.

Every leg runs unbounded and the bar is green. `grep -n timeout` over `run-gates.evidence.test.sh`, `run-gates.gov.test.sh` and `run-gates.turnstile.test.sh` finds no assertion over the runner's bounding.

Same hole from the spec side: no fixture manifest anywhere declares a `ceiling` — `grep -n ceiling tools/run-gates/*.test.sh` hits only the two pinned KNOWN key-set literals (:96, :172) and the gov JSON-shape predicate. So spec-1 AC1 (a `"ceiling": 2` leg over a 30 s sleeper reported `GATE FAIL <leg> (timed out after 2s)`, elapsed measured at the bar), AC3 (a mixed fixture, count named, tree not refused) and AC6 (`input_key` unchanged by a ceiling edit — `grep -n input_key tools/run-gates/*.test.sh` returns nothing) are all unasserted. A field-order slip in `IFS=$'\x1e' read -r nm gd_ av im ch sj ce` at :729 would unbound every leg with every arm green.

The sibling kit already has the arm this one lacks: `unattended.test.sh:3485` greps the driver for `timeout -k 5s "$REMOTE_BOUND"`.

**Fix:** one positive arm over the runner — give an existing fixture leg `"ceiling": 2` and a 30 s sleeper and reuse arm 4h's shape, which already asserts `GATE FAIL stubborn (timed out after 3s)`; add a second fixture with one ceiling'd and one bare row for AC3.

*(Correction to the pool: the `.bound` file write and `report_one`'s `fired` read **are** exercised — arm 4h now runs through the new code on the `PROF_TIMEOUT` fallback branch. The uncovered surface is the ceiling half, not the whole path.)*

---

### 6. MEDIUM — arm 1c reds the shipped canary on a host with no working `timeout -k`
`tools/run-gates/run-gates.test.sh:140-149`

With no usable `timeout`, :131 fails instantly (`_took`=0) and :137's control also returns instantly (`_ctltook`=0); `[ "$_took" -gt 20 ]` is false, so the `elif [ "$_ctltook" -le 20 ]` fires and sets `fail=1` with *"this host does not reproduce the pipe defect"*. Same for a build that rejects `-k` (exit 125).

This contradicts the suite's own established handling: `HAVE_TIMEOUT=0; timeout 1 true … && HAVE_TIMEOUT=1` at :957, whose header says asserting a timeout on such a host *reds an adopter's bar*, with arms 4g/4h printing an explicit SKIP instead. Arm 4m at :1136 proves the runner itself supports that host. Arm 1c sits ~830 lines above where `HAVE_TIMEOUT` is defined, so it has no gate available.

**Fix:** hoist the `HAVE_TIMEOUT` probe above arm 1c and wrap 1c in it, with the same SKIP shape arms 4g/4h use.

---

### 7. MEDIUM — the driver selftest budget was not re-declared
`tools/unattended/run-unattended-gates.sh:49`

`BUDGET_driver_selftest=970  # measured 906 s`, and :175 runs the suite unsharded, so REGION TWO's new arms are paid on every invocation. The dominant added cost is deterministic by construction: the control at `unattended.test.sh:4546` is `_ctl=$(timeout -k 5s 2 bash -c 'sleep 60 & exit 0' 2>&1)`, which blocks until the 60 s grandchild closes the pipe — `unattended.sh:161-164` states the same measurement (62 s) — and the arm *fails* if it returns in under 20 s, so the cost cannot be optimised away.

906 + ~62 = ~968 against 970. It does not red at exactly the measured baseline, so "fails on any box no faster" overstates it by a hair; it reds on ~0.3% variance, which is effectively any run. `run_one` at :162-166 sets `st=1` and prints `OVER BUDGET … fix it or raise the ceiling with a reason beside it`. The file's own header argues at length that a ceiling nobody re-declares is how a suite goes quiet.

**Fix:** raise the budget with the reason beside it (the file's own convention), or shrink the control — a 6 s sleeper against a 2 s bound discriminates the pipe class exactly as well and costs a tenth as much.

I did not run the suite, per the read-only brief; this is arithmetic from the declared measurement plus the arm's own construction.

---

### 8. MEDIUM — no liveness line for GATE_BOUND (spec-6 S5 / AC4 unbuilt)
`tools/unattended/unattended.sh:146, :180`

`GATE_BOUND_LIVE=$REMOTE_BOUND_LIVE`, and :180 silently takes the unbounded branch when it is 0. `grep -n INERT tools/unattended/unattended.sh` returns three hits, only one of which is an emission (:209) — and its text names only the remote observation. So on a host without a runnable `timeout -k`, `--close` runs `$GATE_CMD` completely unbounded while the conf, `PROTOCOL.template.md:499` and the rendered Skill all tell the operator the bar is bounded at 3600 s. The kit's own comment at :138-141 states the rule this breaks.

Downgraded from HIGH because :209 does fire on the same probe and names the root cause (*"this node has no working 'timeout -k'"*) — the operator gets a signal, just about the wrong bound.

**Fix:** a second stderr NOTE beside :209 when `GATE_BOUND_LIVE` is 0, naming `GATE_BOUND` and the two seams it covers, plus an arm.

---

### 9. LOW — two assertion floors left behind
`tools/run-gates/run-gates.test.sh:45` · `tools/unattended/unattended.test.sh:4625`

Against BASE: `git show 1d83cc94:tools/run-gates/run-gates.test.sh | grep FLOOR_ASSERTIONS` → 129, HEAD → 129, while arms 1c and 1d each add `n=$((n+1))`. `FLOOR_SHARD_2=471` at BASE and at HEAD, while all 8 new arms sit inside `if in_shard 2`. Shard 2 therefore carries 8 arms of extra slack. The convention is proven in this same diff: `run-gates.gov.test.sh:72` went 14→15 for one new arm.

**Fix:** `FLOOR_ASSERTIONS=131` and `FLOOR_SHARD_2=479` after re-measuring.

Note in passing: the `FLOOR_ASSERTIONS=508` edit at `unattended.test.sh:4572` is on a dead assignment, overwritten by `FLOOR_ASSERTIONS=667` at :4603. It was equally dead at BASE (500 → 659), so the diff neither created nor worsened it — leave it or delete it separately.

---

### 10. LOW — the run's own knob line and durable header both say the bar is unbounded
`tools/run-gates/run-gates.sh:382-384, :749-760, :858`

`gate-profiles.txt` sets `timeout=0` on all three shipped rows, and spec-1 N1 keeps it that way, so `PROF_TIMEOUT` is 0 on every real run. `:382` appends the ceilings annotation to `prof_t` only when `CEILINGS_LIVE=0`, so a healthy gov bar headlines `width 8, timeout off` while `timeout -k 5s 3960` wraps the canary leg — and when one fires, `report_one` prints `(timed out after 3960s)` under a line that said `timeout off`. `:858` writes `leg_timeout 0` into the durable header whose own comment (:851-855) says a later reader needs *"the per-leg timeout"*.

Three smaller pieces of the same reporting gap:

- The unbounded count went to a standalone stderr line at :759, ~370 lines after `PROF_LINE` is echoed. Spec-1 S6 says *"The profile line names how many of this run's legs carry no ceiling"* and AC3 says *"its profile line NAMES the unbounded count"*. The comment at :742-746 asserts the opposite of what the code does — the two-answers-to-one-question class this diff's own gotcha checklist selected. It is structurally unfixable as written: `PROF_LINE` is built ~330 lines before the manifest is parsed.
- The count block runs at :753, before the guard pass at :763 and the reuse pass at :885, so a diff-scoped run reports legs as "run unbounded this run" that it will skip, hold or reuse.
- `run-gates.evidence.test.sh:435-439` cannot catch any of this: it only tests `-n "$ht"`, and `0` is non-empty.

Gov emits none of it (count 0), so this lands on adopters, whose govkit-emitted rows carry no `ceiling` key at all (`tools/govkit/govkit.py:4326-4336`).

**Fix:** fold the ceiling regime into `prof_t` (`timeout off, ceilings N legs 60-3960s`), move the count emission after the guard/reuse passes, and either move it onto the profile line or correct the comment and S6/AC3.

*(Two sub-claims refuted: the denominator/sentinel divergence is unreachable — the only write to `names` is `names+=("$nm")` at :741, so the sentinel population is empty today. And the ponytail remedy at :410-412 is not inert: setting `timeout=` still raises `TS_TTL`. What **is** now stale there is its precondition clause "with no per-leg deadline configured" — gov legs now carry deadlines up to 3960 s while `TS_TTL` falls back to 1800, and `run-gates.turnstile.test.sh:180` greps that sentence and certifies it current.)*

---

### 11. LOW — the ceilings-INERT notice goes to stdout, not stderr
`tools/run-gates/run-gates.sh:382, :384`

Spec-1 S5 says *"the ceilings are announced INERT on stderr"*. The built announcement is a parenthetical on `prof_t`, emitted by `echo "$PROF_LINE"`. The pre-existing stderr INERT message at :354-357 is still gated on `[ "$PROF_TIMEOUT" -gt 0 ]`, unreachable under any shipped profile. So on a `timeout`-less host, the only notice that all 85 ceilings are dead is a stdout suffix nobody reads for warnings.

**Fix:** emit it on stderr beside :355, independent of `PROF_TIMEOUT`.

---

### 12. LOW — the Skill tells every adopter something false
`tools/unattended/SKILL.template.md:558-559` and its byte-compared render `.claude/skills/unattended/SKILL.md:558-559`

*"`GATE_BOUND` seconds, declared by the project or defaulted by the kit and announced on stderr either way."* `unattended.sh:290-292` puts the echo inside the `"")` arm only; a declared value prints nothing. `.unattended.conf:32` declares `GATE_BOUND="3600"`, so on gov itself the announced state is the silent one.

**Fix:** reword both halves in one commit (the pair is byte-compared by the kit gate) to "announced when it is the kit default", or announce in both arms naming the source. `PROTOCOL.template.md:499` and `memory/guides/UNATTENDED-PROTOCOL.md:499` are already correct and need no edit — two files, not four.

---

### 13. LOW — the `ceiling` key is undocumented for adopters
`tools/run-gates/README.md`

Absent from `git diff --stat`; `grep -n ceiling` returns nothing. The README documents `subject`, `impure` and `guard` but not the one field an adopter must now supply per leg. Spec-1 §5 named this deliverable explicitly, including re-reading the TTL sentence at ~:97 — which is still literally true of the code (`TS_TTL` derives from `PROF_TIMEOUT`) but now misleads by omission, since the bound that actually fires is the manifest ceiling.

**Fix:** add the field and the `max(60, 3x measured)` derivation rule; qualify the TTL sentence.

---

### 14. LOW — `UNATT_QUIET` is an undocumented escape hatch
`tools/unattended/unattended.sh:292`

`grep -rn UNATT_QUIET` over the tree returns exactly one hit — this one. Nothing sets it, no spec item scopes it, it is absent from `.unattended.conf.example`, from the protocol's binding key table (which check 22 joins in both directions), and from the rendered Skill. An unset knob that silently falsifies a documented behaviour.

**Fix:** delete it. Nothing in this build asked for a quiet mode.

---

### 15. LOW — the wiring-check breach path discards the check's own output
`tools/unattended/unattended.sh:1073-1077`

`wout=$RB_OUT` is assigned, then the 124/137 branch calls `fail 4` and `return 1` before reaching the shared printer at :1085, whose comment four lines above says the declared check's output is *"indented under the refusal rather than discarded"* — true on the ordinary-failure path, false on the breach path this unit added. An operator debugging a hung wiring check gets no indication of which arm hung, which is precisely what the 1m22s measurement in TOOL-aPromptedMandate-9 was about.

**Fix:** print `$wout` before the `return 1`, or fall through to the shared printer.

---

## What the diff got right

- **`run_bounded`'s capture-through-a-file is correct, and correct for the right reason.** `_f=$(mktemp)` + `>"$_f"` avoids the command-substitution EOF trap that `bounded-through-a-pipe-is-unbounded.md` names, and the header records the 1 s vs 62 s measurement that proves it rather than asserting it. `</dev/null` on both branches is there too.
- **One helper at both seams, not one seam patched twice.** The comment at `unattended.sh:155-160` names the prior instance (`TOOL-aBranchedMandate-2` fixed `$WIRING_CHECK` and did not grep for the sibling) and refuses to repeat it. That is the class-not-instance rule applied correctly.
- **Breach is distinguished from a red bar.** `DOD_OUT` carries "the bar never answered" wording distinct from "a leg failed" (`:2793-2795`), and the breach test requires `GATE_BOUND_LIVE=1` so an INERT bound can never be misread as a breach.
- **The INERT path runs the command rather than skipping it.** `:180-184` falls through to `"$@"` unbounded — a bound may cost speed, it may not turn a check into a skip. Exit status is preserved.
- **A malformed `GATE_BOUND` is a refusal, not a coerced fallback.** `*[!0-9]*|0)` exits 2 with a message that explains why `0` is not "no bound" — the failure lands loudly on whoever tried to configure it.
- **The ceiling read is field-order-safe against the emitter.** `IFS=$'\x1e' read -r nm gd_ av im ch sj ce` matches the python emitter's write order, and `${ceilings[$i]:-}` with the `PROF_TIMEOUT` fallback keeps a ceiling-less manifest working unchanged — arm 4h still exercises that branch end to end.
- **The manifest itself is complete and gated.** All 85 rows carry an integer `ceiling`, `run-gates.gov.test.sh` grades that as a G-arm, and its floor was correctly raised 14→15 for the new arm — the one floor in this diff that was handled right.
- **`CEILINGS_LIVE` is probed by running `timeout`, not by testing for the binary** — the same discipline as `REMOTE_BOUND_LIVE`, which is the only probe shape that survives the MS-Store-stub class this repo has been bitten by.
- **The declaration requirement lives in `run-gates.gov.test.sh`, withheld from the kit payload** — an adopter is not reded for a key they have not adopted, which is the correct split.
- **The govkit `row["subject"]` → `.get()` change is sound** and narrowly scoped to the emitted-row read.
- **The new arms source the function from the shipped file** rather than retyping it, citing `staged-break-substitutes-a-synthetic-value.md`. The intent is exactly right — it is the sourcing *mechanics* that are broken, not the design.

The two audit rounds visibly moved this code. What did not get the same attention is the test layer: the pattern across findings 1, 2, 4, 5 and 6 is that the bounding *mechanism* was built carefully and the arms that would prove it either do not run, do not touch the code they name, or red the wrong host.