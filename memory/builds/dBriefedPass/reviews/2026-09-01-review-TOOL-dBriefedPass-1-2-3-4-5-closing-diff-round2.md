**Serves:** diff-review TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5

# Closing diff review, round 2 — the round-1 FOLD

*Node d, 2026-09-01, unattended prompt-mode run under a standing mandate. This round reads the FOLD and not the original diff, per BUILD-METHOD M8. The range is one commit, `898dc78c`, which disposed of round 1's twenty-five confirmed findings across twenty-three files. The fold is the hunting ground, and this corpus records that 65-72% of a round-2 audit's findings are caused by the previous round's fold; that ratio held here. Every citation below was re-derived against the tree, and every behavioural claim was REPRODUCED on a fixture rather than argued from the source.*

**Reviewed range:** `0c1ce54b14ce1c01dfe924c06ef93a1a70d3f4b5...HEAD` — one commit (`898dc78c`), 651 insertions across 23 files. **ROUND 2.**

## Verdict: BLOCKED

Four blockers stand, which is one more than round 1 and does not re-arm the loop. Two of them are the two fixes the brief named as highest-risk, and both failed in the way the brief anticipated. The spliced conf-import block (B1) can be disarmed by one ordinary-looking line in the tracked file it exists to defend against, and the leg then prints its own FAILED line and exits 0 — byte-for-byte the "worse shape" the block's own comment says is now impossible. The new shared reader `order_verb_of` raises its refusal inside a command substitution (B2), so `--dispatch` exits 0 with zero bytes of output on a malformed order verb: a machine refusal reporting as a pass, in the verb that is M2's hard floor. B3 is that the merge bar is still RED and cannot be pushed. B4 is that the fold's headline fix — the widened record-surface exclusion — was widened to exactly what round 1 enumerated and stopped there, so the false verdict it exists to remove still fires on this corpus's dominant conforming shape.

**The pattern under all four: the fold fixed the instances round 1 named and not the classes they belonged to.** Three of the four blockers are gate-the-class-not-the-instance (§7), and two of the three highs are the same shape one level down. Where the fold added a test arm it added one covering the reported instance, and each of those arms passes while the class stays open.

**Round 1's own closing observation repeated itself.** Round 1 noted that a full lens fan read the range without running the gate the range redded. This round ran `bash tools/run-gates/run-gates.sh` first: still RED, 3/41 legs, and all three fail on files this build added. The fold ran none of them.

**Review shape.** Raw 32 · confirmed 29 · refuted 3 · unverified 0 · precision 0.91. The 29 confirmed inputs consolidate to **13 distinct defects**; the `filed as` column shows the consolidation rather than performing it silently.

## The findings

| # | Sev | Site | Defect | Filed as |
|---|---|---|---|---|
| B1 | blocker | `tools/unattended/check-pass-order.sh:82` | The spliced conf import assigns every uppercase key the conf declares, so a tracked conf can overwrite `DRIVER` and get arbitrary code eval'd in the leg's own shell; a conf-defined `printf` can forge names into the stream. Leg prints FAILED, exits 0. | 1, 22 |
| B2 | blocker | `tools/unattended/unattended.sh:1789` | `order_verb_of`'s `fail 49` fires inside a command substitution, so the message is captured and `status=1` dies in the subshell. `--dispatch` exits 0 with no output on a malformed order verb. | 2, 16, 25 |
| B3 | blocker | `tools/run-gates/run-gates.sh` | The merge bar is RED at HEAD — 3/41 legs — all three on files this build added. `.githooks/pre-push` blocks the push, so the range cannot land. | 8, 26, 27 |
| B4 | blocker | `tools/unattended/check-pass-order.sh:196` | The widened exclusion covers the build folder and `GENERATED_INDEXES` but not `SHARED_RECORDS`, so a conforming spec-first run that writes the mandated backlog row is still reported as built-before-specced. | 17 |
| H1 | high | `tools/unattended/run-unattended-gates.sh:173` | Both legs the fold registered arrive with no `BUDGET_*` ceiling, and a missing ceiling is itself a failure here — the kit's DECLARED compensating check is RED by construction. | 10, 18, 28 |
| H2 | high | `tools/unattended/check-pass-order.sh:186` | The B4-class fix depends on `GENERATED_INDEXES`, which no gate requires and which defaults to empty. Undeclared, the leg silently reverts to the pre-fix false verdict. | 9, 29 |
| H3 | high | `tools/unattended/check-pass-order.sh:186` | The same key is read from the tracked conf the graded run commits and spliced straight into the exclusion, so a one-word widening takes a violating tree from RED to GREEN, reported only as `unbuilt-in-range`. | 11 |
| M1 | medium | `tools/unattended/unattended.sh:1782` | `order_verb_of` ports the generator's regex pair but not its duplicate-verb refusal, so the two readers still disagree on a doubled `order` verb, under a comment claiming one reader shape. | 3, 12, 19, 30 |
| M2 | medium | `tools/workflows/unattended-build.js:308` | The disposal prompt quotes a `--rescope` command with no `--reason`, which `verb_rescope` hard-refuses. It is the harness's only PROMOTE instruction. | 20 |
| L1 | low | `tools/unattended/check-pass-order.sh:186` | `GENERATED_INDEXES` is word-split unquoted and each half is interpolated as an unanchored regex, so a declared value is glob-expanded against the repo root and its `.` matches any character. | 4 |
| L2 | low | `tools/unattended/kit.toml:67` | The comment amendment left both halves standing, and two counts in the same block went stale. This is the block that records the self-test exemption as deliberate. | 5, 14, 23, 31 |
| L3 | low | `tools/unattended/run-unattended-gates.sh:61` | Two hand-typed counts of the runner's own leg sets are stale, in the help block that spends fifteen lines deriving the budget rather than typing it. | 13, 24, 32 |
| L4 | low | `memory/builds/dBriefedPass/build/2026-09-01-build-TOOL-dBriefedPass-3-1-pass-order.md:84` | The build record still certifies the suite at "14 arms" in the same commit that took it to 17. | 15 |

---

## B1 — blocker — the spliced conf import hands the leg's own `DRIVER` to its subject

**`tools/unattended/check-pass-order.sh:82`** (the arm), with the block spanning `:76-97`. Identical block and identical hole at **`tools/unattended/check-unattended.sh:150`**.

The brief flagged this splice as highest-risk because it was lifted verbatim from a sibling with different variable names. That is exactly what broke. The import assigns every name matching the unanchored glob `[A-Z][A-Z0-9_]*`, but the leg sets `ROOT`, `HERE`, `DRIVER` and `CONF` at `:49-53`, **above** the import. `DRIVER` is then read at `:105` and its `plan_state` slice is eval'd at `:110` in the leg's top-level shell.

Reproduced end to end against HEAD, twice, on a fixture that reds honestly (control rc=1, names `ARCH-tOrder-1`):

- **Vector A, one declaration.** Add `DRIVER="tools/unattended/evil.sh"` to the tracked `.unattended.conf` plus a tracked `evil.sh` whose first line is `plan_state() { printf 'READY'; }; trap 'exit 0' EXIT; {`. Result: the leg printed `pass-order FAILED — a unit was BUILT before a conforming spec` and **exited 0**. `run-gates` reads the exit code, so that is GATE ok.
- **Vector B, name forgery.** Only the conf's sourcing is redirected, not the emitter, so a conf-defined `printf` function survives into the process-substitution body. Running the block's verbatim bytes against a conf carrying such a function: `conf_ok=1` (the sentinel WAS delivered), `MEMORY_ROOT` and `PASS_ORDER_CUTOFF` both erased, the injected `trap` fired, `EXIT=0`.

Both falsify the block's own comment at `:76-78`: "nothing from that file executes in this shell" and "the stream cannot introduce a name this leg does not expect". It cannot introduce a name the leg does not expect; it overwrites the names the leg already computed, and forgery defeats even that. The sentinel is not the whole verdict, because the attacker also writes the sentinel.

The block's comment draws the line itself — "PROTOCOL §1 cost 2 concedes that a leg reading this conf reads its subject's ANSWER. It does not concede code execution that suppresses the leg's own return code and output." That line is the contract this is graded against, and vector A crosses it with a single line that does not read as an attack in review.

The two arms the fold added (`check-pass-order.test.sh:149-171`) cover an appended `exit 0` and a `trap ... EXIT` inside the conf. Neither is either vector here. This is gate-the-class-not-the-instance: the fold gated the two instances round 1 named.

**Fix.** Assign only the three keys this leg reads. Replace the open arm at `:82` with a closed alternation over `MEMORY_ROOT|PASS_ORDER_CUTOFF|GENERATED_INDEXES` and drop `[A-Z][A-Z0-9_]*` entirely. If a generic reader is genuinely wanted, anchor the name test with a full-string match AND assign into a `CONF_`-prefixed namespace so no leg-owned variable is reachable. Emit through `command printf` inside the process substitution so a conf-defined function cannot forge the stream. Apply the same two changes to `check-unattended.sh:150`.

**Left-shift gate.** Add two arms to `check-pass-order.test.sh`: a conf declaring `DRIVER` must not change which file the classifier is sliced from, and a conf defining a `printf` function must refuse rather than deliver a forged stream. Then gate the CLASS: a bar leg asserting that, for every script carrying this import block, the assignable-name arm is a closed alternation and not an open glob — the block is now in two files and will be in three.

## B2 — blocker — `order_verb_of` refuses inside a command substitution, so `--dispatch` exits 0

**`tools/unattended/unattended.sh:1789`**, called at `:4540` and `:4545`.

`fail()` at `:327` is an `echo` followed by `status=1` — it does not exit. Both call sites capture the function in a command substitution and follow it with `|| return 1`, so on a malformed verb the `echo` lands in the caller's variable and the `status=1` is set in a subshell that is then discarded. `verb_dispatch` does return 1, but the dispatcher's `case` arm at `:4841` drops that rc, there is no `set -e` anywhere in the file (only `set -u` at `:41`), and `:4842` runs `exit "$status"` — still 0.

Reproduced with the function's exact bytes: rc 1 from the function, the diagnostic captured into the caller's variable rather than printed, and `status` still 0 in the parent. End to end on a fixture repo, a spec header spelling `· order 2` prints `dispatch declared` and exits 0; changing only that field to `· order 2x` produces **0 bytes of output, rc 0, and no dispatch row**.

Every other refusal in `verb_dispatch` (`:4502`, `:4519`, `:4524`, `:4559`, `:4566-4584`) calls `fail 49` in the function's own shell and therefore exits 1 with a message. This is the only one routed through a command substitution, and it is the one guarding M2's hard floor. The fold turned round 1's "an empty read silently skips the order gate" into "the whole verb silently no-ops at green" — and the THIN refusal five lines earlier still works when called directly, so one verb now has two guards giving two answers to the same question.

Independently corroborated by the bar: `python3 tools/memory-tree/check-arms.py --check` names `tools/unattended/unattended.sh:1789 check 49 branch 1` as an unarmed, unpinned fail branch. The refusal has never been observed at its call site, which is why nobody saw this.

**Fix.** Do not raise from inside the substitution. Either have `order_verb_of` print only the integer on stdout and send the diagnostic to stderr, with each caller re-raising in its own shell, or assign to a global and call it as a plain command so `order_verb_of ... || return 1` runs in the caller. The second is safer: it removes the substitution rather than working around it.

**Left-shift gate.** Arm the branch with a positive assertion naming its own failure text — a `--dispatch` run against a spec spelling `order 2x` must exit non-zero AND print the check-49 line. That arm makes `check-arms.py` green honestly instead of by a pin. Then gate the class: a predicate that refuses any `fail` call reachable from inside a command substitution, because the arity error is invisible at every call site and this is the second reader of that pattern to ship.

## B3 — blocker — the merge bar is RED at HEAD and the range cannot be pushed

**`tools/run-gates/run-gates.sh`**, run at HEAD rather than reasoned about.

```
gates RED — 3/41 legs failed (46 held: every self-test, GATE_SELFTESTS=1 runs them)
GATE FAIL  install-prefix (shipped surface)                (exit 1)
GATE FAIL  method carriers (every pointer declared)        (exit 1)
GATE FAIL  harness arms (fail branches armed or pinned)    (exit 1)
```

All three fail on files this build itself added — `git cat-file -e main:<path>` fails for all four of `tools/unattended/check-pass-order.sh`, `check-pass-order.test.sh`, `tools/workflows/unattended-build.js` and `unattended-build.test.sh`.

- `install-prefix` reports four UNRECORDED carrying files with no ratchet row. The fold widened this: `check-pass-order.test.sh` went from 6 root-install literals at the round-1 tip to 9 at HEAD.
- `method carriers` names `tools/workflows/unattended-build.js`, which mentions `BUILD-METHOD.md` at `:192` and has no row in `memory/project/method-carriers.txt`. The fold edited this file twice in range and added a further `BUILD-METHOD M4` reference at `:301-310` without adding the declaration.
- `harness arms` names 15 unpinned check-49 branches in `unattended.sh`, including `:1789` (B2 above), the `--brief` block at `:4099-4125`, and `:4519`, `:4524` and `:4559`.

Round 1 reported the bar RED and fixed only the roster-ids cause it named. `.githooks/pre-push` runs the full bar on a default-branch push and blocks a red one, so this range cannot land.

**Fix.** Three mechanical registry edits. Re-run `bash tools/check-install-prefix.sh --write-ratchet` and commit the four rows — or better, derive the path in the new test arms from the `$SCRIPT` and `$KIT` variables already in scope at `check-pass-order.test.sh:11-12` instead of spelling `tools/unattended/...`. Add a `tools/workflows/unattended-build.js` row to `memory/project/method-carriers.txt` classifying it as a pointer. Arm the new check-49 branches, or pin them in `memory/project/unarmed-branches.txt` with reasons — noting that `:1789` must be ARMED and not pinned, because B2 is a real defect behind it.

**Left-shift gate.** No new gate is needed; three existed and were not run. The gate that is missing is procedural and belongs in the harness: `tools/workflows/unattended-build.js` should run the bar at the start of a closing-review stage and refuse to open the round against a red tree, so a review can never again be filed against a tree that cannot land. Round 1 found this by execution and round 2 found it again by execution — twice is a class.

## B4 — blocker — the widened exclusion omits `SHARED_RECORDS`, so a conforming spec-first run still reds

**`tools/unattended/check-pass-order.sh:196`**, with the exclusion built at `:186-189`.

The fold widened the build-commit exclusion from `spec/` and `reviews/` to the build's whole folder plus the index halves of `GENERATED_INDEXES`. It did not add `SHARED_RECORDS`, which `.unattended.conf` declares as `memory/DECISIONS.md memory/backlog` and which `check-pass-order.sh:58` does not even initialise. A spec pass is REQUIRED by §1's Definition of Done to update the decision log and backlog. Those paths sit outside both exclusions, so a conforming spec commit still wins the build-commit selection, step 2 grades ITS parent where no spec yet exists, and the leg reports the exact false verdict the fix exists to remove.

Reproduced on the kit's own fixture shape. Control, spec-first with only the spec and the regenerated index: rc 0, `graded 1 closed unit(s)`. Same fixture, spec commit additionally writing `memory/backlog/ARCH.md`:

```
rc=1
pass-order FAILED — a unit was BUILT before a conforming spec for it existed:
  ARCH-tOrder-1 — BUILT at 92bb165 with NO tracked spec at that commit's parent 174f72e;
  the spec was written after the code, which is the same act with the record written last
```

The shape is this corpus's norm, not a corner. Scanning 400 commits for `spec(...)` subjects naming a unit id, four touch nothing outside the new exclusion except a shared record: `613132c0`, `79d08224` and `23730008` write only `memory/backlog/TOOL.md`; `96ae4f14` adds `memory/DECISIONS.md`. Each would win the selection today.

This build escapes only because its own spec commit `c5ceb93e` is subject `spec(dBriefedPass): ...` and names no unit id — the escape the code comment at `:174-181` records in its own words. With `red_after_land = true` (`kit.toml:112`) and history append-only, the next conforming run whose spec commit names a unit id is unlandable short of a bypass. That is the same consequence that made round 1's B2 a blocker, unfixed.

The fold's fixture was extended to write `memory/LIVE.md` — the one path round 1 named — and not the backlog. The arm passes by finding nothing.

**Fix.** Read `SHARED_RECORDS` from the conf beside `GENERATED_INDEXES`: initialise it at `:58` and resolve the `__kit-default__` sentinel the way `unattended.sh:315` does, then add each declared path to the exclusion.

**Left-shift gate.** Extend the `spec-first` fixture so its spec commit writes a backlog row, which makes the existing green arm fail without the widening. Then gate the class rather than the path: the exclusion set should be DERIVED from the conf keys that name record surfaces, and a new record-surface key that no leg excludes should red — otherwise the next key added to the conf reopens this for a third time.

## H1 — high — the kit's declared compensating check is RED by construction

**`tools/unattended/run-unattended-gates.sh:173`** and `:180`.

`run_one` derives its budget key from the leg's label at `:150` and sets `st=1` at `:162-164` when it resolves to nothing, with the comment "A MISSING BUDGET IS ITSELF A FAILURE." The declaration block at `:45-52` holds exactly the eight pre-fold names. `BUDGET_pass_order_history` and `BUDGET_pass_order_selftest` are both absent.

Observed:

```
ok    pass-order history                 9s
      OVER BUDGET  pass-order history declares no ceiling, so its cost is unbounded by construction
unattended gates RED — 4 ran on demand, 2 over budget
```

`tools/unattended/kit.toml:73-79` names a GREEN verdict from this runner as THE compensating check for the 2026-08-23 ruling that took the kit self-tests off the merge bar, and as the Definition of Done for any work touching `tools/unattended/` — which is this entire build. So the DoD is unmeetable, the exemption's only evidence reds for a bookkeeping reason, and a real red from this runner is now indistinguishable from this one. `--selftests` and `--all` red the same way on the second leg.

This is round 1's M7 one level up: M7's fix added the legs and not their declarations — amendment-leaves-its-other-half-standing.

The same run also showed `kit gate` at 121s against its declared 120s ceiling. That is pre-existing and outside this diff, but it also blocks a GREEN and needs a decision before the landing report can quote one.

**Fix.** Declare both ceilings beside the other eight with the measured reading in the trailing comment, as every sibling does: `BUDGET_pass_order_history=60` with `measured 9 s` beside it, and `BUDGET_pass_order_selftest` with its own measurement — the suite ran 17 arms here, so time it and give it headroom.

**Left-shift gate.** The runner already reds on a missing ceiling, so the mechanism works; what failed is that nobody ran it. Add `bash tools/unattended/run-unattended-gates.sh --checks` to the harness's own DoD stage in `unattended-build.js`, so a build touching `tools/unattended/` cannot reach its closing review without the compensating check having been executed and its verdict recorded.

## H2 — high — the exclusion depends on a key nothing requires and which defaults to empty

**`tools/unattended/check-pass-order.sh:186`**, initialised empty at `:58`.

`GENERATED_INDEXES` defaults to the EMPTY SET on purpose (`unattended.sh:283-284` says so in as many words), and `check-unattended.sh:165`'s required-key loop is `LANDER BYPASS_BAN GATE_CMD WIRING_CHECK KEEPALIVE_CREATE KEEPALIVE_DELETE` — this key is not in it. Nothing anywhere in the tree requires it.

Reproduced on the kit's own `spec-first` fixture: with the key declared, rc 0 and `graded 1 closed unit(s)`. With the `GENERATED_INDEXES=` line deleted, the identical conforming history yields rc 1 and `the spec was written after the code`. **The three-count liveness line is byte-identical in both runs.** Nothing announces that the exclusion set was empty.

So an adopter who wrote their conf before this key existed gets the unlandable-conforming-run defect back, under `red_after_land = true`, with no signal. Every other value this leg reads announces its absence — a blank `PASS_ORDER_CUTOFF` prints `the ORDER term is OFF` and exits 0 at `:131-134`. This one degrades in silence, which is the degradation-known-but-unreported class the leg's own cutoff term was written to avoid.

There is a second problem in the same choice: `UNATTENDED-PROTOCOL.md:551` defines this key purely as index-and-generator pairs for the concurrent-dispatch refusal at `unattended.sh:4661`. It now has two meanings, so an adopter tuning it for the documented purpose silently changes what this leg excludes.

**Fix.** Do not silently accept an empty exclusion set. Either refuse with `exit 2` when it resolves to nothing, naming the key and why the exclusion needs it, or add a term to the liveness line saying that no exclusion was declared and a spec commit may therefore win the build-commit selection. Given the double meaning, the cleaner fix is a key that means this — a `RECORD_SURFACE` declaration read alongside `SHARED_RECORDS` per B4.

**Left-shift gate.** Add an arm running the `spec-first` fixture with the key deleted, asserting the announcement is present. Then gate the class: every conf key a leg reads should be either in a required-key loop or announced when blank, and a leg that reads a key satisfying neither should red — this is the third round in which a silently-defaulted conf value has changed a verdict.

## H3 — high — the same key is inside the graded run's reach and widening it is silent

**`tools/unattended/check-pass-order.sh:186`**.

`GENERATED_INDEXES` is read from `.unattended.conf`, a tracked file the graded run commits, and spliced verbatim into the exclusion at `:186-189` with no validation of what it names. Widening it by one word takes a violating tree from RED to GREEN.

Reproduced on the `build-first` fixture. Control: rc 1, names the violation. Rewriting the conf line to `GENERATED_INDEXES="tools:g memory:g"`:

```
rc=0
pass-order: graded 1 closed unit(s) · 0 build(s) skipped by the 2026-01-01 cutoff ·
0 with no pinned run BASE · 1 unit(s) unbuilt-in-range
```

Nothing in that output distinguishes an evasion from a resumed build — and the leg's own comment at `:253-256` explicitly teaches the reader that a non-zero `unbuilt` is the ordinary resumed-build shape.

PROTOCOL §1 cost 2 concedes that this leg reads its subject's answers. The cutoff term pays that cost by ANNOUNCING itself. This input does not, which is the same shape round 1 filed as M1 against the cutoff skip, reintroduced by the fold on a new key.

**Fix.** Either bound the exclusion — refuse an entry whose index half is a directory prefix of tracked product code, and require the generator half to exist as a tracked file — or make a non-zero `unbuilt` announce its cause by printing the excluded prefix set alongside the count. Both are cheap; do the second regardless, because it is what makes the first auditable.

**Left-shift gate.** Add an arm that widens the key on the `build-first` fixture and asserts the leg either still reds or names the exclusion in its output. Left-shift the class: any conf-supplied value that can only ever narrow what a leg grades must appear in that leg's liveness line, and a bar leg should assert that property over every check in the kit.

## M1 — medium — the two readers still disagree on a duplicated `order` verb

**`tools/unattended/unattended.sh:1782`** against **`tools/memory-tree/gen_build_index.py:326`**.

`_parse_order` refuses a header carrying the verb more than once when the loose regex finds more than one hit, and its own comment records that placing that check ABOVE the early return was itself a caught bug, armed in the suite at line 2290. `order_verb_of` ports `ORDER_OK_RE` and `ORDER_LOOSE_RE` faithfully but not the count.

Verified on both sides with `**Status:** SPECCED · rev-1 · base ab · order 2 · order 3 · streams s`: the shell reader returns `2` at rc 0; the generator raises `status header carries the 'order' verb more than once, so which step this unit occupies has two answers`.

I checked the six shapes the fold set out to reconcile — the verb at end of line, doubled space, no space, mid-header, `order 2x`, and `order 0x2` — and the two readers agree on all six. The regex port is correct. The missing piece is a count, which is not a regex, and it is the one branch of `_parse_order` left behind.

That makes both of the fold's new claims false for this input: the function header at `:1775-1781` says it reads the header the way the generator's own regex pair reads it, and the call site comment at `:4535-4539` says "ONE READER SHAPE, the generator's own". `--dispatch` runs during the build, before the index is regenerated, so the run sequences on the silent wrong answer and discovers the disagreement later as a failed regen.

Bounded and non-silent — the generator raising means a doubled-verb build cannot land quietly — which is why this is medium and not high. But it is the assertion round 1's M10 was told had been fixed, and a header amended twice by a rev-N bump is exactly how the shape arises.

**Fix.** Mirror the generator's ordering: before the OK match, count loose hits and refuse on more than one, with the generator's own message. Route the refusal through whatever call-site shape B2's fix establishes, or it will be as invisible as B2's is.

**Left-shift gate.** One arm asserting `--dispatch` refuses a doubled-verb header, in the same suite as B2's malformed-verb arm. The durable gate is the class: a bar leg that feeds one corpus of header shapes to both readers and asserts they return the same verdict — three rounds have now filed a divergence between these two readers, each time on a shape the previous fix did not enumerate.

## M2 — medium — the harness's only PROMOTE instruction quotes a command the driver refuses

**`tools/workflows/unattended-build.js:308`**.

The disposal block hands the build agent `--rescope <slug> --act add --item <id>` and stops. `verb_rescope` at `unattended.sh:4405` hard-refuses an empty reason with check 48, "an amendment recording no reason is indistinguishable from one nobody meant", and that `fail` is at top level, so it genuinely refuses. The driver's usage header at `unattended.sh:14`, `.claude/skills/unattended/SKILL.md:526` and `memory/guides/UNATTENDED-PROTOCOL.md:681` all spell the verb with `--reason "<text>"`.

This is the file's only `--rescope` mention, and it is reached on exactly the two verdicts the block exists for, NON-CONVERGENT and CEILING — the moments where promoting the item is the whole point. The agent's first attempt is rejected. The flag name `--item` is correct; only the mandatory argument is missing.

**Fix.** Append `--reason "<what the audit found>"` to the quoted command at `:308`.

**Left-shift gate.** A bar leg that extracts every driver invocation quoted inside `tools/workflows/*.js` and the shipped skill text, and asserts each satisfies that verb's required-flag set as the driver declares it. Prose that quotes a command is a second reader of the driver's arity, and this corpus has now filed that class more than once.

## L1 — low — the exclusion value is word-split unquoted and interpolated as a regex

**`tools/unattended/check-pass-order.sh:186`** and `:188`.

The `for` loop over `GENERATED_INDEXES` is an unquoted expansion, so a value containing a glob metacharacter is pathname-expanded against the repo root — verified: a value of `memory/*` yields the words `memory/builds` and `memory/ledger`. And the exclusion pattern is built by interpolating the path into a `grep` regex, so the live declaration's `memory/LIVE.md` also matches `memory/LIVEXmd` — verified, the unescaped dot matches. A declaration of `.*` followed by any generator half excludes every path.

`unattended.sh:4661` splits the same value the same way, so this is consistent rather than divergent. It is just unsafe in both. Low because the misgrade surfaces in the `unbuilt-in-range` count rather than being wholly invisible, and because anyone who can edit the conf already has full code execution via B1.

**Fix.** Escape the path before using it as a pattern, and build the exclusion as an array expanded quoted, so neither globbing nor option-splitting reaches `grep`. Disable pathname expansion around the split, or read the pairs with `read -ra`.

**Left-shift gate.** A shellcheck-class predicate over the kit: an unquoted expansion of a conf-supplied value in a `for` list or a `grep` pattern position reds. This is mechanically detectable and the tree currently has two instances.

## L2 — low — the kit descriptor's amendment left both halves standing, and two counts went stale

**`tools/unattended/kit.toml:67`**, verbatim:

`# THE LEGS BELOW STAY, and the difference is their SUBJECT, and the difference is their subject: they read the REPOSITORY - its`

The replacement clause and the original both survived the edit that dropped the numeral from "THE THREE LEGS". Two counts in the same block also went stale as the fold grew the sets: `:77` reads `--all      # and the three legs beside them` while the file itself now carries four `[[gate_leg]]` blocks (`:83`, `:93`, `:100`, `:107`) and the runner registers four `checks` legs. Line `:126`'s "all three unattended gate legs" is a past-tense account of a prior defect, so it is a weaker instance of the same drift and may be left as history.

This block is where the 2026-08-23 self-test exemption is recorded as deliberate — charter §7's "an exemption is not coverage" makes it load-bearing prose. It is the paragraph a reader consults to learn why the self-tests are off the bar, and a reader counting from it undercounts what the exemption covers. No gate reads comment prose, so nothing catches it.

Dropping the numeral from `:67` was correct and should stay dropped; only the doubled clause needs removing.

**Fix.** Collapse `:67` to a single clause, and change `:77` to a count-free phrase such as "the record/wiring legs beside them".

**Left-shift gate.** Two cheap predicates, both mechanical: a repeated-clause detector over tracked comment blocks (an identical run of five-plus words within one line, case-insensitively), and a numeral-beside-a-derived-population check for the small closed set of files that enumerate their own legs. The second is the §7 rule this file keeps breaking.

## L3 — low — the runner's own help text miscounts its own leg sets

**`tools/unattended/run-unattended-gates.sh:61`** and `:85`.

`:61` reads `--selftests  the five suites that stage breaks into this kit` while `run_one` is invoked six times with kind `selftests` (`:175-180`). `:85` reads `--checks     the three record/wiring checks` while it is invoked four times with kind `checks` (`:170-173`) — confirmed empirically by the `--checks` run reporting `4 ran on demand`. The hand-list at `:7-10` names three merge-bar legs and omits `pass-order history`, which `kit.toml:107-112` registers with `subject = "repo"` like the other three.

The aggravator is location: `:63-84` of the same help block spends fifteen commented lines deriving the budget sum from the file's own declarations rather than typing it, citing round 7's low 2, round 8's low 4 and round 9's low 10 — all filed against a typed number in this file. These counts are hand-typed twelve lines from the `run_one` calls that own them.

**Fix.** Derive both from the file's own text the way the budget sum already is — count the `run_one` lines by kind out of the script itself — or drop the numerals and write "the suites" and "the record/wiring checks".

**Left-shift gate.** Same predicate as L2's second: for the files that enumerate their own populations, assert no cardinal numeral appears in prose describing a set the file itself lists. Four rounds have now filed this class in this one file, which is the definition of a class worth gating.

## L4 — low — the build record certifies an arm count the same commit changed

**`memory/builds/dBriefedPass/build/2026-09-01-build-TOOL-dBriefedPass-3-1-pass-order.md:84`**, which reads `run: 14 arms, exit 0.`

Ran the suite at HEAD: `--- 17 arms, exit 0`. `git show 898dc78c` on that file shows the fold rewrote the four lines immediately preceding the figure and left the figure untouched, in the same commit that added the hostile-conf control plus two hostile-conf arms. Amendment-leaves-its-other-half-standing, in the record whose entire job is to be the evidence a reader trusts instead of re-running. A reader diffing 14 against 17 cannot tell whether three arms were added or three were lost.

**Fix.** Restamp to `17 arms, exit 0` and add one clause naming what the three new arms cover, so the count and its subject move together.

**Left-shift gate.** The memory-tree hygiene gate already parses build records; add a check that a record stating an arm count for a named suite agrees with that suite's own reported count. The suite prints the number on its last line, so this is a derivation and not a second hand-kept copy.

---

## What round 2 says about the loop

Round 1 returned 3 blockers; round 2 returns 4. The loop does not re-arm.

The useful signal is not the count but the shape. **Eleven of the thirteen defects above exist inside a fix the fold made**, and the two exceptions — B3's registry rows and M2's quoted command — are things the fold should have run or read and did not. The fold's failure mode was uniform: it repaired every instance round 1 named, added an arm for each named instance, and did not ask what class the instance belonged to. B1 gated two conf shapes and left the name-assignment surface open. B4 excluded the one record path round 1 named and left `SHARED_RECORDS` out. M1 ported the regexes and left the count. H1 added the legs and left the ceilings. Each of those is gate-the-class-not-the-instance (§7), and the reason it recurs is that a round-1 finding names an instance, so a fold that reads the finding rather than the rule fixes exactly what it was shown.

Three findings also share a narrower shape worth naming for the next round: **`check-pass-order.sh` reads three values out of a file its own subject writes** — `DRIVER` via the import hole, `GENERATED_INDEXES` for the exclusion, `PASS_ORDER_CUTOFF` for the skip. Only the third announces itself. A leg whose subject supplies its inputs is a conceded cost under PROTOCOL §1, but the concession is only honest while every such input is visible in the leg's own output. Two of three currently are not.

**Two arms in the new suite pass by finding nothing** — the hostile-conf pair, and the `spec-first` fixture that omits the mandated backlog write. Both were written against the reported instance. That is the fixture-passes-by-finding-nothing entry on this range's checklist, and it is the reason B1 and B4 survived a fold that believed it had closed them.

One methodological note against this round's own checklist. My first two attempts to reproduce B1's forgery vector failed because a heredoc-fed payload lost an escape level and turned a literal backslash-zero into a NUL byte — this repo's own recorded `heredoc-halves-backslashes` trap, and the heredoc-escape-reaches-the-regex bug class, landing in the probe rather than in the code. The vector is real; the first two runs were measuring my quoting. Carrying the payload as base64 removed every escaping level and reproduced it cleanly. A probe that fails for a reason inside the probe is indistinguishable from a refuted finding, which is the argument for running each vector two ways before calling it clear.

## Gates, run rather than reasoned about

- `bash tools/run-gates/run-gates.sh` at HEAD — **RED**, 3/41 legs failed, 46 held. Failing: `install-prefix (shipped surface)`, `method carriers (every pointer declared)`, `harness arms (fail branches armed or pinned)`. Profile `capable`, width 8.
- `bash tools/check-install-prefix.sh` — rc 1, four UNRECORDED carrying files.
- `bash tools/memory-tree/check-method-carriers.sh` — rc 1, names `tools/workflows/unattended-build.js`.
- `python3 tools/memory-tree/check-arms.py --check` — rc 1, 15 unarmed unpinned check-49 branches including `unattended.sh:1789`.
- `bash tools/unattended/run-unattended-gates.sh --checks` — rc 1, `4 ran on demand, 2 over budget`.
- `bash tools/unattended/check-pass-order.test.sh` — `17 arms, exit 0`.
- Kit self-tests were NOT run, per the standing owner instruction; `--checks` was.
