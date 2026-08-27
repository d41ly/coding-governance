## Verdict: BLOCKED

**Serves:** spec-audit TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-5 TOOL-aBoundedCeiling-6

One defect makes `TOOL-aBoundedCeiling-1` unbuildable as written: S8's diff and AC7 assert opposite things about the same code path. Everything else is repairable in place with the edits below.

Three finder findings (`ac7-inverted-budget-refusal`, `s8-budget-deletion-reds-checks`, `budget-deletion-reds-checks`, `ac7-refuted-by-run-one`) are one defect stated four times, and three more (`kit-version-bump-wrong-file`, `ceiling-floor-version-bump-wrong-file`, `version-bump-wrong-site`) are one defect stated three times. They are collapsed here.

---

## `TOOL-aBoundedCeiling-1`

### BLOCKER — S8 / AC7: the deletion causes exactly what AC7 says it prevents

S8 deletes `BUDGET_kit_gate`, `BUDGET_playbook_validity_gate` and `BUDGET_skill_wiring`. AC7 asserts that after this, `bash tools/unattended/run-unattended-gates.sh --checks` no longer prints `OVER BUDGET  <label> declares no ceiling`.

The code does the reverse. `tools/unattended/run-unattended-gates.sh:150` builds `bkey="BUDGET_$(printf '%s' "$label" | tr ' -' '__')"`, `:151` resolves it with `eval "budget=\${$bkey:-}"`, and `:159-163` read:

```
# A MISSING BUDGET IS ITSELF A FAILURE.
if [ -z "$budget" ]; then st=1; over=$((over + 1)); printf '      OVER BUDGET  %s declares no ceiling, so its cost is unbounded by construction\n' "$label"
```

The three labels are still invoked at `:170-172` as `run_one "kit gate" checks …`, `"playbook validity gate"`, `"skill wiring"`, and their bkeys resolve to exactly the three identifiers S8 deletes (`:45-47`). `:190-195` turn `over>0` into `unattended gates RED` and `exit "$st"`. So S8 makes `--checks` emit the forbidden string and exit 1 permanently — and `--checks` is the compensating command the kit's own header names (`run-unattended-gates.sh:22-25`) for legs held off the bar. Removing the three `run_one` rows instead is no better: `ran=0` gives "graded nothing at all" and `exit 2` at `:183-186`.

**Smallest fix:** drop S8 and AC7. Leave the three `BUDGET_*` lines where they are. §4's own Alternatives-rejected argues the two enforcements are non-unifiable (elapsed-vs-declared inside the suite runner, versus the manifest ceiling on the bar), and a leg that is both a manifest row and a `run_one` suite can carry a ceiling in each without contradiction. If the duplication must go, S8 has to also change the `[ -z "$budget" ]` refusal at `:161` and say so in the Inventory — that is a change to a shipped kit's refusal set, not a three-line deletion, and it needs its own scope item and its own AC.

### HIGH — §4 Design / F1: the derivation launders two live breaches

The rule `max(60, 3 × the leg's own current seconds in gate-ledger.tsv)` grants every leg a bound above its present cost. Two of the affected legs are over a declared ceiling *today*: the live ledger reads `unattended kit gate 533.000` and `playbook validity gate 161.780`, against `BUDGET_kit_gate=120  # measured 28 s` and `BUDGET_playbook_validity_gate=120  # measured 13 s` (`run-unattended-gates.sh:45-46`). The formula replaces 120 s with roughly 1599 s — a ~13× silent raise, in a file whose header at `:43-44` says "Raising one is fine; raising one silently is not."

The general "gate that cannot fail" framing is overstated — the ceiling's job is bounding a hang, F1 resolves 3× deliberately against `memory/gotchas/process-creation-is-the-suite-cost.md`, and AC1 stages an observed RED. The specific charge stands.

**Smallest fix:** add one sentence to §4: a leg that already carries a `BUDGET_*` value ships that value as its manifest ceiling, and raising it requires the reason written beside it. Derive from the last green-and-accepted cost, not the current one.

### MEDIUM — §10 Reuse audit: two governing records uncited

`grep -rn 'aCollapsedScan' memory/builds/aBoundedCeiling/` returns only `-5`. But `memory/DECISIONS.md:109` (`TOOL-aCollapsedScan-3`) is ratified and about the exact pin S8 deletes: "`BUDGET_kit_gate=120` was set 2026-08-23 against a 28 s reading; check 30 landed 2026-08-25 unmeasured and `--checks` then read 305 s. The ceiling worked and nothing on the bar reads it." And `memory/backlog/TOOL.md:226` (`TOOL-aCollapsedScan-4`) is OPEN against that same breach, offering "(2) re-declare the ceiling with the reason beside it."

**Smallest fix:** add both ids to §10 and state which of `-4`'s two candidates this unit takes. If neither, S8 must not delete the declaration `-4` is filed against.

### MEDIUM — §5 Production-readiness: AC5 and AC7 cannot live in the shipped canary

§5 says "AC1 through AC7 below, all in `run-gates.test.sh`". AC5 is a whole-bar `bash tools/run-gates/run-gates.sh` run — and `run-gates.test.sh` *is* the `run-gates canary` leg (`tools/run-gates/kit.toml:73`), so that recurses into the bar running it. AC7 observes a gov unattended path. `run-gates.test.sh:83-84` states the rule for itself: "A SCHEMA ARM, which is why it ships. It asserts a shape true of any manifest in any tree and names no leg of this repo's corpus." `kit.toml:21-35` withholds `run-gates.gov.test.sh` for exactly this reason. §7 already routes both correctly, so §5 contradicts §7.

**Smallest fix:** rewrite §5's sentence to route AC1–AC4 and AC6 to `run-gates.test.sh`, AC5 to the whole-bar run, and AC7 to `run-gates.gov.test.sh` — or delete AC7 with S8 per the blocker.

### MEDIUM — §4 Design / AC6: the reuse-cache benefit is false for 48 of 85 legs

AC6's trailing clause "so the reuse cache is not invalidated" is wrong. `run-gates.sh:795-796` gives an unguarded leg `comp="$FPRINT_START"`, and `:644` sets `FPRINT_START=$(fingerprint)`; `gate-fingerprint.sh` digests `HEAD^{tree}` plus the porcelain plus the dirty blobs, so any tracked edit to `tools/gate-legs.json` moves it whether dirty, staged or committed. Counted against the live manifest: 38 of 85 legs carry no `guard`, and 10 more carry a guard covering `tools/` or `tools/gate-legs.json` — 48 legs lose their key on the commit that moves a ceiling. A faithful test of AC6 as worded fails for every one of them.

**Smallest fix:** keep the runner-side decision, which is right for other reasons. Restate the §4 rationale as "the ceiling never reaches the child's command line" and narrow AC6 to what is true: `input_key` does not read `ceiling`, asserted with the tree held constant.

### LOW — §4 Inventory: the inertness line is sited before the manifest is read

The row `run-gates.sh liveness (~:349) | say so when timeout will not run and ceilings exist` names a site where the second half is unknowable. `:349-351` is the `PROF_TIMEOUT` probe; `LEGS_FILE` is defined at `:84` but not parsed until `:717`, with the parallel arrays loading at `:721-727`. S5 and AC4 say only "when `timeout` cannot run", which *is* answerable at `:349`.

**Smallest fix:** delete "and ceilings exist" from the Inventory row.

---

## `TOOL-aBoundedCeiling-5`

### HIGH — S5 / AC3 / §4 Inventory / F2: the parity check names two programs and the wrong manifest

Four sections give three answers.

- S5 says govkit's **selfcheck** gains it, "joining the name and subject comparison it already makes". That comparison is check 7h in `tools/govkit/govkit.py`: `:800` `def selfcheck(root, write=False)`, `:1208` `legs_path = root / "tools" / "gate-legs.json"`, `:1212` the subject map, with the arms at `:1224` and `:1235-1266`.
- The §4 Inventory has no row for `govkit.py` selfcheck at all; its only parity row is `tools/govkit/selftest.py`. AC3 also names `selftest.py` as the failing program. `selftest.py` holds no such comparison — its only `check_target_reads_subject` contact is the unit probe at `:1827-1842`.
- S5 calls the operand the "emitted manifest"; check 7h reads gov's own hand-maintained `tools/gate-legs.json`. §8 F2 then resolves on "gov's manifest is hand-maintained rather than emitted, so the two populations do not join" — false about the very check S5 routes to, which joins them in both directions.

The choice is material, not cosmetic: `govkit selfcheck` is subject `repo`, no guard, so it runs on every bar; `govkit selftest` is subject `kit`, chunk `selftests`, held unless `GATE_SELFTESTS=1`.

**Smallest fix:** implement the arm in `govkit.py` check 7h beside the subject arms at `:1235-1266`. Change the Inventory row to `tools/govkit/govkit.py` check 7h, keep a second row for `selftest.py` as the place the failing case is staged, and rewrite AC3 to name `govkit selfcheck` as the failing program over `tools/gate-legs.json`. Add `govkit selfcheck` to §7's gate list. Re-resolve F2 in one sentence: the populations do join, and say whether a kit-owned leg missing a descriptor `ceiling` reds there, mirroring the `d_sub is None` arm.

### HIGH — §10 Reuse audit / AC2: the seam being copied crashes on its below-floor path

§10 claims the `check_target_reads_subject` seam's whole shape "already exists" — "resolve the version, compare against a floor, withhold the key below it, and say so". Two parts of that are wrong.

`govkit.py:4305` is `row = {"name": nm, "argv": argv}`; `:4306-4307` set `row["subject"]` only when the predicate passes; `:4328-4329` then read it unconditionally — `emitted.append({… "subject": row["subject"] …})`, with no `try/except` covering it (the enclosing block from `:4228` guards only `JSONDecodeError`). The predicate returns False for a target below the floor or unreadable (`:2963-2974`), so `govkit apply` raises `KeyError` on that path today. `selftest.py:1823-1845` exercises the predicate directly only — its below-floor fixture writes `KIT_RUN_GATES_VERSION=1.0` at `:1830` and never runs a full apply — which is why the crash survives. And `:4306-4307` print nothing, so "and say so" describes a report that does not exist; §5's observability bullet ("reported the way `check_target_reads_subject`'s is") points at nothing.

Accuracy note: an AC2 fixture pinned at 1.1 would not crash, so AC2 is not necessarily unachievable — but a builder copying M6's shape walks into it, and copying the emitter shape verbatim for `ceiling` reproduces the `KeyError` for every target at 1.1, which is every current adopter.

**Smallest fix:** add a scope item — change `govkit.py:4329` to `row.get("subject")` and use `.get()` for the new ceiling field — and amend §10 to say the seam is copied minus a defect this unit repairs. Drop "and say so" from §10 or add the withhold-time report §5 promises.

### HIGH (dedupe of three findings) — S4 / §4 Inventory / N2: the version bump is routed to a file with no version

The Inventory sends the `KIT_RUN_GATES_VERSION` bump to `tools/run-gates/kit.toml`. That file holds only a pointer: `:14` `version_from = { file = "run-gates.sh", pattern = "^KIT_RUN_GATES_VERSION=" }`. The literal is `tools/run-gates/run-gates.sh:19` — `KIT_RUN_GATES_VERSION=1.1   # gov:kit run-gates@1.1` — mirrored at `tools/run-gates/README.md:3`. `tools/check-kit-versions.sh:52` requires the assignment, `:62` the same-line marker, `:63` the README marker; the `kit version markers` leg is subject `repo` with no guard, so a partial bump reds every bar. `govkit.py:2967` reads the version out of the target's `run-gates.sh`, never out of `kit.toml`.

Compounding it, N2 declares "nothing in `run-gates.sh` changes" — so the unit's own floor mechanism cannot be satisfied without breaking its own non-goal. Built as written, the version stays 1.1, a floor above it withholds the key from every target forever, and AC1 fails; setting the floor to `(1,1)` is what F1 explicitly rejects.

**Smallest fix:** replace the one Inventory row with two — `tools/run-gates/run-gates.sh:19` (constant plus inline `gov:kit` marker) and `tools/run-gates/README.md:3` (marker) — drop the `kit.toml` row, amend N2 to "run-gates.sh changes only by its version constant and marker, not by behaviour", and add the `kit version markers` leg to §7.

### MEDIUM — S1 / N1: an adopter on a slower node has no durable lever

The unit ships ceilings derived from node `a`'s ledger into every adopter's manifest with no override. §4's Alternatives-rejected disposes of the escape route with "Let adopters hand-write ceilings. They can, and nothing stops them — but a kit-owned leg whose ceiling is authored downstream drifts from the suite it bounds on the first kit update." It does not drift; it is silently clobbered. `govkit.py:4319` is `existing[by_name[nm]] = row` — the whole row is replaced for any leg the receipt claims — and the drift refusal at `:4314` compares only `prev.get("argv") != argv or prev.get("guard", []) != guards`, so a hand-edited `ceiling` is neither reported nor preserved. N1 covers only "an adopter's own project-authored legs". Spec-1's own N5 says the ledger "is per-clone and per-machine, so a verdict read from it would be a fact about the node" — that node-dependence is then baked into a shipped constant, and `memory/gotchas/process-creation-is-the-suite-cost.md` measures a 2.4× spread *within* one node.

**Smallest fix:** one scope item and one AC. Either a `GATE_CEILING_SCALE` multiplier the runner applies to every declared ceiling, or a project-owned per-leg override the emitter reads and never overwrites. Then correct §4's rejected-alternative sentence — hand-writing is clobbered, not drifted — and say in N1 which lever the slow-node adopter reaches for.

### LOW — §10 Reuse audit: `TOOL-aPacedTurnstile-12` uncited

`memory/backlog/TOOL.md:152` is OPEN and asks for the generalization S5 is about to bypass: "govkit's selfcheck joins a descriptor's `[[gate_leg]]` rows to the repo's `tools/gate-legs.json` by NAME only and never compares the two declared GUARDS … the general join is here." `ceiling` would be the third hand-written field branch; `guard` stays the one uncompared field. §10's own sentence ("It returned no record about carrying a leg FIELD to adopters") is literally true, which is why the probe missed it.

**Smallest fix:** cite the row in §10 and say in one clause whether this unit adds the third field branch or takes the general join. If the former, say why `guard` stays out.

---

## `TOOL-aBoundedCeiling-6`

### MEDIUM — §4 Inventory / S1: the prescribed edit set reds this unit's own gate, twice

Adding `GATE_BOUND` to `.unattended.conf` and `PROTOCOL.template.md` only fails two checks in `tools/unattended/check-unattended.sh`, which is the `unattended kit gate` leg §7 names as this unit's gate (ledger cost 533 s to learn it the hard way).

- Check 22 joins the **kit's example conf** against the **rendered** protocol: `:1142` `EXAMPLE_CONF="$HERE/.unattended.conf.example"`, `:1159` `doc_keys` from section 8 of `$LIVEDOC`, `:1166` `ex_keys` from the example, `:1168` `phantom=$(comm -13 …)`, failing at `:1177` with "documented but in no example". `tools/unattended/.unattended.conf.example` carries 25 keys and no `GATE_BOUND`; the sibling keys live there (`GATE_CMD`, `HALT_FLOOR`, `LANDER_MARKER`).
- `LIVEDOC="$M/guides/UNATTENDED-PROTOCOL.md"` at `:1110`, and check 10 at `:1109-1119` byte-diffs `PROTOCOL.template.md` against that rendered file — so editing the template alone reds too.

The word `.unattended.conf.example` appears nowhere in the spec.

Separately, the `check-unattended.sh` Inventory row is misleading: check 22 needs no edit at all, and the only hand-written key join in that file is the required-key loop at `:154` (`for k in LANDER BYPASS_BAN GATE_CMD WIRING_CHECK KEEPALIVE_CREATE KEEPALIVE_DELETE`) — which is exactly the "make it required" move §4 rejects at `:86-88`.

**Smallest fix:** add two Inventory rows — `tools/unattended/.unattended.conf.example` (the key with its default) and `memory/guides/UNATTENDED-PROTOCOL.md` (re-render after the template edit, same commit). Either delete the `check-unattended.sh` row or annotate it "no edit; listed because check 22 and check 10 read the three files above."

### MEDIUM — N1 / §10 Reuse audit: the sibling unbounded seam is left unnamed

S2 bounds `unattended.sh:2695` — `DOD_OUT=$($GATE_CMD 2>&1) && { DOD_OUT=""; return 0; }`. Its own comment at `:2691-2692` reads: "Sibling of the seam check_wiring already uses for $WIRING_CHECK -- TOOL-aBranchedMandate-2 fixed that call site and did not grep for this one." The sibling is `unattended.sh:988` `wout=$($WIRING_CHECK 2>&1) && return 0` — same unbounded command substitution over a project-declared command, no timeout anywhere in that function. `memory/backlog/TOOL.md:41` is `TOOL-aPromptedMandate-9`, OPEN, and already measured it: "nothing in the driver's precondition chain has a timeout … `check-wiring.sh --check` took 1m22s … so `--preflight` alone exceeds a two-minute budget." N1 excludes only `.githooks/pre-push`.

N1 as literally worded ("no other `$GATE_CMD` caller") is not false — `:988` is not a `$GATE_CMD` caller — so this is an omitted N-item, not a wrong source claim. It still reproduces the fix-one-call-site class the target line's own comment records, and spec-5 N4 shows this build knows how to dispose of an adjacent defect by naming it.

**Smallest fix (lazy one first):** widen S2 to a single bounded-run helper applied at both `unattended.sh:988` and `:2695` — one function, two call sites, and it closes `TOOL-aPromptedMandate-9`. Otherwise add an N-item naming `$WIRING_CHECK`, citing `TOOL-aPromptedMandate-9`, with the reason it stays unbounded.

### LOW — `gen:spec-records` / §1: the observation that forced this unit does not serve it

`memory/builds/aBoundedCeiling/build/2026-08-27-build-TOOL-aBoundedCeiling-1-live-hang-observed.md:3` reads `**Serves:** research TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-5`, while the same file's body says "That is `TOOL-aBoundedCeiling-6`, added to this build's roster by `--rescope` on the strength of this observation." Spec-6's `gen:spec-records` region (`:5-11`) accordingly lists only the prompt record, and §1 (`:19-20`) links the observation as the thing this unit would have ended.

**Smallest fix:** append `TOOL-aBoundedCeiling-6` to the record's `Serves:` line and regenerate the spec-records regions in the same commit.

---

## Build README

### LOW — the rejected `timeout=` alternative is argued with two numbers

`README.md:36-38` says the bound "has to sit near 2000 s — which converts an infinite hang into a thirty-three-minute hang"; spec-1 `:135-137` says "it must sit near 4000 s, which converts an unbounded hang into a sixty-six-minute one". Both derive from the same anchor, `<git-common-dir>/gate-ledger.tsv:71` `run-gates canary  1319.914`, at 1.5× and 3×. The README's implicit 1.5× is the factor spec-1 F1 explicitly rejects.

**Fix:** make the README point at spec-1's paragraph instead of restating the number.

### LOW — an identifier that matches nothing in the tree

`README.md:102` reads "The residue — three `BUILD_*` lines whose suites ARE legs — folds into `TOOL-aBoundedCeiling-1` S8". The identifiers are `BUDGET_*` (`run-unattended-gates.sh:45-47`), which spec-1 S8 spells correctly.

**Fix:** `BUILD_*` → `BUDGET_*`.

---

## What was checked and found sound

Source claims verified true, so the record shows what held:

- **Spec-1's `run-gates.sh` line citations.** `:349-351` is the `PROF_TIMEOUT` inertness probe, `:717` the manifest parse, `:721` the array load — all accurate at the cited numbers. Only the "and ceilings exist" condition on the `:349` row is misplaced.
- **Spec-1 F1's 3× headroom factor.** Deliberately resolved against `memory/gotchas/process-creation-is-the-suite-cost.md`, which measures a real 2.4× intra-node spread. AC1 stages an observed RED at a 2 s ceiling, so the ceiling mechanism itself is not a gate that cannot fail.
- **Spec-1's `input_key` design choice.** The ceiling genuinely never reaches the child's command line (`run-gates.sh:795-799`), so the runner-side decision is right; only AC6's cache-invalidation clause is wrong.
- **Spec-5 S5's identification of the existing join.** Check 7h at `govkit.py:1208-1266` really does compare descriptor `subject` against the manifest field-by-field, in both directions, and really is the right place to extend. The defect is that the Inventory and AC3 point elsewhere, not that S5 chose wrong.
- **Spec-5's `check_target_reads_subject` floor mechanism** exists and works as described for the pass path: `govkit.py:2963-2974` resolves the target's installed runner version from its own `run-gates.sh` and gates the key on it. Only the withhold path is defective.
- **Spec-6 §10's identification of `REMOTE_BOUND`** as the in-file precedent for a bounded seam is correct — `unattended.sh:130`, `:143`, `:177-178` — and it is the only bounded command seam in that file, which is exactly why copying it is the right move.
- **Spec-6 §4's rejection of making `GATE_BOUND` a required key** is sound; the required-key loop at `check-unattended.sh:154` is what it would mean, and forcing every adopter conf to declare it would break existing installs.
- **The three standing constraints hold.** No spec proposes returning `*.test.sh` legs to `tools/gate-legs.json`; no spec sets `PROF_TIMEOUT` non-zero on any profile row; the three dropped units are recorded in `README.md`.
- **No spec's cited line number was found off by more than one** anywhere in `run-gates.sh`, `run-unattended-gates.sh`, `unattended.sh`, `govkit.py`, `check-unattended.sh`, `check-kit-versions.sh` or `gate-legs.json`. The defects above are wrong *conclusions* about correctly-cited code, plus one file named that holds nothing.
- **The merge bar was not run**, per instruction. Every verdict here is from reading source, the live `gate-ledger.tsv`, and `tools/gate-legs.json`.