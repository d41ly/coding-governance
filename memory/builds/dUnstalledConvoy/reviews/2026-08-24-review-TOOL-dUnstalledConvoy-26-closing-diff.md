**Serves:** journal TOOL-dUnstalledConvoy-26 TOOL-dUnstalledConvoy-27 TOOL-dUnstalledConvoy-28 TOOL-dUnstalledConvoy-29 TOOL-dUnstalledConvoy-30 TOOL-dUnstalledConvoy-31 TOOL-dUnstalledConvoy-32 TOOL-dUnstalledConvoy-33

# Closing diff review — the hold mechanism lands, and it takes four repository-subject gates off the bar with it

**Reviewed range:** `b164a29603cb4fa3e5533721252de164853f948d...HEAD` (HEAD = `553e2836`, three
commits). **Tier 2, closing review.**

**Review shape:** the adversarial fan returned 30 findings, deduplicated to 18 after eleven lenses
landed on the same six defects from different sides; 8 were refuted by the skeptic pass and are
enumerated below. Every citation in this document was re-opened and re-read at HEAD before it was
written up. Nothing was taken from a commit message or from a finder's summary. Where a finding
claimed a measurement, the measurement was re-run.

## Verdict: BLOCKED

**Three blockers, five highs, seven mediums, three lows.**

The `subject` field is the right instrument and it is built correctly. A declared membership
criterion stated once, ratcheted by a committed pin, cross-checked between descriptor and manifest,
and read by the push boundary as coverage rather than equality — that is a better answer than any
pattern over `.test.sh` could have been, and the run-total arithmetic, the chunk rollup and the
all-held refusal all reason about the right population. What blocks the close is that the same
commit that built the mechanism used it on four legs whose failure means *this repository drifted*,
not *this kit's source moved* — so `memory/guides/REVIEW-PROTOCOL.md`, `memory/HYGIENE.md`,
`memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` can now drift from the templates that
ship them with nothing on any automatic bar noticing, in gov and in every adopter. Beside that,
`GATE held` was added as the runner's fifth verb without an `observed_held` template, so the
deployer reads every held leg as VANISHED and false-reds every upgrading adopter's `apply`; and a
`baseline_units` refactor in the unattended kit turned a bare-id list into a haystack that a
`| WONTDO |` grep is asked to match, killing check 24's own exemption clause. Three of the arms this
build wrote to prove its mechanism cannot fail the leg they live in, which is the house
green-by-absence class arriving inside the arm written to close a green-by-absence class.

---

## B1 — `GATE held` has no `observed_held` template, so the deployer reads every held leg as VANISHED

**`tools/run-gates/kit.toml:120-129`** · **`tools/govkit/govkit.py:1883`, `:2218`, `:2715`**

`[gate_runner_seed]` declares one observation template per runner verb: `observed_ran` (120),
`observed_failed` (121), `observed_skipped` (124), `observed_reused` (129). This build added a fifth
verb at `tools/run-gates/run-gates.sh:936` —
`printf 'GATE held  %s  (kit self-test, set GATE_SELFTESTS=1 to run)\n'` — and no template for it.
`grep -rn observed_held` over the tree returns nothing. `read_gate_verdicts` (govkit.py:1866-1893)
iterates exactly three keys and matches by line-anchored prefix; the heads are `GATE ok    `,
`GATE FAIL  `, `GATE skip  `, none of which prefixes `GATE held  `. It is run deliberately WITHOUT
the run-everything escape (docstring at 1869-1873), so on any adopter every kit-subject leg prints
`GATE held` and lands in NO state — absent from the returned map, not `skipped`.

**What breaks.** Two things, both in `cmd_apply`.

1. **False red on every upgrading adopter.** The transition table at govkit.py:2708-2717 fires
   `r.fail(f"leg '{nm}' was green before this install and is gone after — a leg that vanished is not
   a leg that passed")` on `b == "green" and a2 is None`. On an adopter already carrying a
   govkit-owned leg from an older gov, the baseline read (2216) sees `GATE ok    <leg>` and records
   green; the emitter then replaces the row in place (2643) with
   `row = {..., "subject": leg.get("subject") or "repo"}` (2631); the after read (2707) now sees
   `GATE held  <leg>`, gets nothing, and that `r.fail` fires. 42 of the 85 rows in
   `tools/gate-legs.json` are `subject: "kit"` today, and the shipped descriptors carry the same
   split, so a run-gates + memory-tree adopter gets a fistful of failures whose message names the
   wrong cause. `matrix.py`'s AC9 arms grade the FRESH-emission case only, where `b is None` and no
   arm fires — nothing in the diff covers the upgrade path.
2. **A hole in the dead-probe refusal.** govkit.py:2218 guards
   `if before_map and not any(v in ("green", "red") for v in before_map.values())`. An EMPTY map
   skips the refusal entirely. Before this change a target whose legs all guard-skipped produced a
   map full of `skipped` and tripped the refusal; now a target whose legs are all kit-subject
   produces an EMPTY map, the refusal is bypassed, and — in the words of its own message — "every
   leg after the install would land in the row that carries the exemptions".

The comment at `tools/run-gates/kit.toml:125-128` states the exact rule this omission breaks, about
`observed_reused`: "without a template the deployer has no state for a leg a target reused, so that
outcome is structurally unreachable". Note the asymmetry that makes `held` far worse: `GATE reuse`
only appears under the opt-in `GATE_REUSE`, which this read never sets, so that template was never
load-bearing. `GATE held` appears on EVERY default run.

**The exact fix.** Add `observed_held = ["GATE held  {name}"]` to `[gate_runner_seed]` in
`tools/run-gates/kit.toml` beside the other four. Give it a distinct `"held"` state in
`read_gate_verdicts` (govkit.py:1883) rather than folding it into `"skipped"` — the two have
different remedies, which is the same argument run-gates.sh:1012-1014 makes for keeping the tally
separate. Add the transition arm at govkit.py:2708-2717: `b == "green" and a2 == "held"` is the
EXPECTED upgrade outcome and must report informationally, never fail. Widen the dead-probe guard at
2218 so an empty `before_map` on a manifest-kind runner is refused or explicitly reported rather
than silently accepted. Existing adopters need the key backfilled into their
`.governance/deploy.toml`, so `cmd_intake`'s key list at 3160 needs it too.

---

## B2 — check 24's "already WONTDO at the baseline" exemption became unreachable when `baseline_units` started returning bare ids

**`tools/unattended/check-unattended.sh:1505`** · **`tools/unattended/lib-unattended.sh:181-186`**

At the base sha, `rs_was` was the baseline README's units-REGION TEXT:
`git show b164a296:tools/unattended/check-unattended.sh` line 1495 reads
`rs_was=$(printf '%s\n' "$rsb" | region - '<!-- gen:build-units -->' ...)` — markdown table rows,
`| WONTDO |` column and all. TOOL-dUnstalledConvoy-33 replaced that derivation with `baseline_units`
(check-unattended.sh:1485), whose last statement is
`_bu_ids=$(printf '%s\n' "$_bu_was" | grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+' | sort -u)` followed by
`printf '%s\n' "$_bu_ids"` (lib-unattended.sh:181-186) — bare ids, one per line, no pipes anywhere.

Line 1505 was not updated and still asks a table question of a bare-id list:

```sh
      id_rows "$rs_was" "$rsid" | grep -q '| WONTDO |' && continue
```

`id_rows` (lib-unattended.sh:34) returns the matching LINES of its haystack; over a bare-id list
those lines are the id and nothing else, so the `| WONTDO |` grep can never match and the `continue`
is dead. The sibling `id_in "$rs_was" "$rsid"` on the ADDED-ids loop (line 1499) still works, which
is why the refactor's own arms pass.

**What breaks.** False RED on `unattended kit gate`, a subject=repo leg that runs on every bar and in
every adopter's bar. Any build whose units region already carried a `| WONTDO |` row at the run's
live-phase-entry commit, and which has no `item retire` / `item supersede` rescope row for it —
correctly, because nothing was retired *during* the run — now fails with "a unit went WONTDO after
this run entered BUILDING and no rescope row retires or supersedes it". There is no legal repair: the
run cannot write a retire row for a transition it did not make. This tree hides it because
dUnstalledConvoy's one WONTDO unit (TOOL-dUnstalledConvoy-25) went WONTDO DURING the run and carries
a matching `retire` row at RUN.md:40, so the *second* `continue` fires instead. A build like
aRuledFrontispiece (three WONTDO units) reds the moment a run opens over it.

**No arm covers it.** `tools/unattended/check-unattended.test.sh:2135-2146` has exactly two WONTDO
arms: "goes WONTDO AFTER the baseline" (must red) and "the same transition WITH a retire row" (must
not). Nothing exercises a unit that was ALREADY WONTDO at the baseline, which is the branch that
died.

**The exact fix.** Have `baseline_units()` return the baseline region ROWS — `printf '%s\n'
"$_bu_was"` — and keep `_bu_ids` only for the non-empty liveness test, since every call site already
extracts ids from whatever it gets. Alternatively add a second function, `baseline_wontdo`, returning
the WONTDO id set. Then add the missing arm beside check-unattended.test.sh:2143: seed a roster whose
unit is WONTDO at the baseline commit, commit, and assert `miss "$(run)" "check 22 FAILED"`. The
exemption has never been observed firing.

---

## B3 — `profile_bar.test.sh`'s three new arms sit BELOW the verdict block, so their failures never reach the exit code

**`tools/run-gates/profile_bar.test.sh:300-304`, arms at `:305-355`**

The suite's ONLY verdict on `bad` is lines 300-304:

```sh
# ---------------------------------------------------------------------------------------- verdict
if [ "$bad" -ne 0 ]; then
  echo "FAIL ($bad of $n assertions failed)"
  exit 1
fi
```

The three arms this build added — verb-set agreement (305-329), held-parse (331-343), NOT_RUN
(345-355) — are all written AFTER it, and `bad` is never re-tested. What follows them is only the
`FLOOR_ASSERTIONS` check (357-360) and `echo "PASS ($n assertions)"` (361). There is no `set -e`;
`chk()` (28-34) increments `bad`, prints, and `return 0`.

**Verified by staged break.** I copied `tools/run-gates/` to a scratch dir, changed
`NOT_RUN = ("skip", "held")` to `NOT_RUN = ("skip",)` in `profile_bar.py`, and ran the suite:

```
  ASSERT FAILED: not-run arm: NOT_RUN returned GOT:('skip',)
PASS (38 assertions)
exit=0
```

That break was chosen because it is invisible to every earlier arm — no fixture emits a `GATE held`
line — so nothing else could red the suite. Breaking `PINNED_VERBS` instead does red it, but only as
collateral: `profile_bar.py` then refuses every fixture run with exit 2 and 26 unrelated assertions
fail. Neither of the three new arms can, by itself, make this suite non-zero.

**What breaks.** `profile-bar selftest` is a gate leg. The three arms written precisely because a
silently-dropped verb cost 42 of gov's 85 legs from every profile are structurally incapable of
failing it. `held` can be dropped from `NOT_RUN`, or its alternation dropped from `VERDICT`, and the
leg stays green with an `ASSERT FAILED` line scrolled past. Because the leg is itself `subject = "kit"`
and now held by default, the only run that would ever print that line is a `GATE_SELFTESTS=1` run
whose output nobody greps. The floor is loose too: the suite executes 38 assertions against
`FLOOR_ASSERTIONS=36`, so two of the three new arms could be deleted without tripping it. This is
§7's "a check that cannot fail", and it means the red-first evidence for these three arms cannot have
been an exit-code observation.

**The exact fix.** Move the verdict block (300-304) to sit after the last new arm (after line 355)
and before the floor check at 357. Raise `FLOOR_ASSERTIONS` from 36 to 38. Re-stage the
`NOT_RUN = ("skip",)` break and confirm the suite exits 1 before landing.

---

## H1 — four gate legs whose failure means THIS repository drifted were assigned `subject = "kit"`, so their parity coverage is now held on every bar and in every adopter

**`tools/gate-legs.json:173`, `:251`, `:442`, `:903`** · **`tools/memory-tree/kit.toml:127`** ·
**`tools/workflows/kit.toml:33`**

Four legs moved from no-subject (i.e. run) to `subject: "kit"` (i.e. held) in this diff. Verified by
diffing the manifest at base against HEAD:

| leg | manifest line | guard | verdict changed by |
|---|---|---|---|
| `python resolver (behaviour + inline parity + idiom ban)` | 173 | `tools/`, `tools/lib/` | any `.sh` in the tracked tree |
| `kit/dogfood doc parity` | 251 | `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md`, `tools/…` | three repository documents |
| `review-protocol parity (kit vs dogfood)` | 442 | `memory/guides/REVIEW-PROTOCOL.md`, `tools/…` | one repository document |
| `marker contracts` | 903 | **none** — deliberately on every bar | the two `region()` copies |

`kit-dogfood-parity.test.sh`'s own header reads: "the two documents this kit SHIPS, RENDERED for this
install, must equal the two documents this repo RUNS ON". `check-protocol-parity.test.sh`'s reads
"the review protocol this repo RUNS ON must equal the one this kit SHIPS". Under -30's criterion as
written at `tools/run-gates/run-gates.sh:697-706` — ask what a FAILURE MEANS, "this repository is
misconfigured" gives `repo` — all four are `repo`. A guard naming a path outside `{kit}/` is *by
construction* a declaration that a repo-only edit can flip the leg's verdict, which contradicts
holding it until somebody edits the kit. `marker contracts` had no guard at base, which is the
strongest possible statement that it belongs on every bar.

`tools/lib/resolve-python.test.sh:80-108` is not a kit self-test either: its `PARITY_ROWS` table and
its §3/§3b idiom bans quantify over `git grep … -- '*.sh'` across the whole tracked tree.

**Verified armed and now unreachable.** Appending one line to `memory/guides/REVIEW-PROTOCOL.md`
makes `bash tools/workflows/check-protocol-parity.test.sh` print `protocol-parity: DRIFT` and exit 1.
File restored; `git status --porcelain` clean.

**What breaks.** `memory/guides/REVIEW-PROTOCOL.md`, `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`
and `memory/guides/BUILD-METHOD.md` can drift from the templates that ship them with nothing on any
automatic bar reporting it — including a full pre-push bar in an adopter's tree, since these are
shipped `[[gate_leg]]` rows. A new drifted inline copy of `resolve_python`, or a new
`command -v python3`, likewise reds nothing. `tools/check-agent-cap-restatement.sh:22` records that
the line `check-protocol-parity.test.sh` freezes is "the most important carrier in the corpus" — the
§8 verify-stage total. §7's rule that a parity leg is never exempted to unblock a landing is defeated
here without an exemption ever being written.

The contradiction is stated in the file itself. The comment at `tools/memory-tree/kit.toml:118-126`,
immediately above the new `subject = "kit"`, says a missed guard on this leg "would cost a wrong
merge verdict — which is why the unit that removes the force closes this hole in the same commit
rather than filing it". -30's spec §3 puts "re-subjecting any leg not named here" OUT of scope and
names only the push/commit boundary self-tests, so these four were never considered.

**The exact fix.** Set `subject = "repo"` on all four: `tools/memory-tree/kit.toml:127`,
`tools/workflows/kit.toml:33`, the `marker contracts` descriptor row, and the resolver leg's
`[[exempt_leg]]`/descriptor carrier. Mirror all four in `tools/gate-legs.json` and run
`python tools/govkit/govkit.py selfcheck --write` in the same commit to move the pins. More durably:
add a govkit selfcheck arm that reds on any `subject = "kit"` leg whose declared guard contains a
path that is not under `{kit}/` — the value is mechanically suspect whenever the leg declares it
reads outside its own kit. If any must stay held, write its compensating check into the kit
descriptor the way `tools/unattended/kit.toml:76-77` does, because an exemption is not coverage.

---

## H2 — the `selftests` stamp writer has no negative control: an unconditional `1` passes every arm in the diff and silently disables the push boundary's predicate 8

**`tools/run-gates/run-gates.sh:1174`** · **`tools/run-gates/run-gates.test.sh:579`**

Line 1174 writes `printf 'selftests\t%s\n' "${GATE_SELFTESTS:+1}"`. The only arm anywhere that reads
a runner-WRITTEN stamp is run-gates.test.sh:579, and it asserts the switch-ON case only:

```sh
grep -q '^selftests	1$' "$S/.git/gate-full-green" 2>/dev/null \
  || { echo "canary: a switch-ON green did not record the switch in its stamp"; fail=1; }
```

There is no arm asserting what a switch-OFF full green stamps. `.githooks/pre-push.test.sh` does not
close the gap either: its `stamp()` helper (125-135) hand-writes the record, so arms 19-23 grade the
READER over synthetic stamps and never touch the writer.

**Verified by staged break.** Rewrote line 1174 as `printf 'selftests\t1\n'` in a scratch copy of the
runner, built the same three-leg fixture case 3h2 uses, and ran it switch-OFF then switch-ON:

```
after [GATE_SELFTESTS= ]: selftests\t1     <- the lie
after [GATE_SELFTESTS=1]: selftests\t1
>>> the 3h2 stamp arm STILL PASSES with the break staged
```

**What breaks.** This is the one byte TOOL-dUnstalledConvoy-27 exists to consume.
`.githooks/pre-push:215` forces a full bar only when `[ "$rec_st" != "1" ]`; a writer that always
says `1` makes that predicate dead, and a green earned with 42 of 85 legs held would satisfy a push
that runs them — the boundary trusting a partial bar as a whole one, which is verbatim the failure
the unit's own comment names. Every arm in the build stays green while it happens.

**The exact fix.** Add the missing half beside run-gates.test.sh:579, in the same `$S` fixture: after
the switch-OFF run, assert the stamp does NOT carry `^selftests\t1$` and DOES carry the key with an
empty value. One extra `n=$((n+1))` and one grep. Re-stage the unconditional-`1` break to confirm it
now reds.

---

## H3 — `profile_bar`'s new verb guard compares the runner against `PINNED_VERBS` but never against `VERDICT`, so the drift it was written to stop still passes

**`tools/run-gates/profile_bar.py:70-71`, guard at `:328-345`**

The verb set is spelled twice in this file:

```python
VERDICT = re.compile(r"^GATE (ok|skip|FAIL|reuse|held)\s+(.*)$")
PINNED_VERBS = ("ok", "skip", "FAIL", "reuse", "held")
```

The guard added at 328-345 computes `_unknown = sorted(_emitted - set(PINNED_VERBS))` and refuses on
that alone. `VERDICT` is never compared to anything. Reproduced in-process: with `PINNED_VERBS`
extended by a sixth verb and `VERDICT` left alone, `_emitted - set(PINNED_VERBS)` is `[]` (guard
PASSES) while `parse_verdicts("GATE stale  some leg  (tail)\n")` returns `[]` — the line is dropped
silently. That is byte-for-byte the failure the file's own comment at 55-69 records twice, once for
`reuse` and once for `held`, one level up. The guard's message at 343 even instructs the reader to
"Add them to PINNED_VERBS and to VERDICT" — prose where a derivation belongs.

**What breaks.** The next verb added to `run-gates.sh` gets added to `PINNED_VERBS`, because the
guard names it; the developer forgets `VERDICT`; every line carrying that verb vanishes from the
profile. Under-counted bar, complete-looking output, guard green. The leg that would catch it,
`profile-bar selftest`, is itself `subject = "kit"` and held.

**The exact fix.** Delete the duplication instead of policing it. Keep `PINNED_VERBS` as the single
source and build the regex from it, immediately after line 71:

```python
VERDICT = re.compile(r"^GATE (%s)\s+(.*)$" % "|".join(re.escape(v) for v in PINNED_VERBS))
```

Then the two cannot disagree and the guard's remaining job is only runner-vs-pin.

---

## H4 — `AGENTS.md` still tells every session that `GATE_FULL=1` is "what pre-push runs, and what a DoD needs". Both clauses are now false.

**`AGENTS.md:482`** and **`AGENTS.md:226`**, unchanged by this build:

```
GATE_FULL=1 bash tools/run-gates/run-gates.sh     # ignore every leg guard; what pre-push runs, and what a DoD needs
```

Three ways it is now wrong, each verified:

1. `.githooks/pre-push:135-137` sources `.githooks/gate-env.sh`, which exports `GATE_SELFTESTS=1`, so
   what pre-push runs on this repo is `GATE_FULL=1 GATE_SELFTESTS=1`. Verified end to end with a
   scratch repo carrying a stub gate: with `gate-env.sh` present the gate observed
   `GATE_SELFTESTS=[1] GATE_FULL=[1]`; with it removed, `GATE_SELFTESTS=[<unset>] GATE_FULL=[1]`.
2. `GATE_FULL=1` alone holds 42 of the 85 legs in `tools/gate-legs.json` (counted from the file:
   43 repo, 42 kit). run-gates.sh:738 checks `GATE_SELFTESTS` and never `GATE_FULL`, deliberately,
   and `tools/run-gates/run-gates.test.sh:563` asserts exactly that ("GATE_FULL unlocked the
   kit-subject legs, which is the bypass this replaced").
3. A stamp written by a `GATE_FULL`-only run records `selftests\t` (empty, line 1174), which pre-push
   predicate 8 (.githooks/pre-push:215) then rejects, forcing a FULL run anyway.

Compounding it, `AGENTS.md:505-513` still describes the kit-self-test hold as the unattended-only
manifest deletion ("Its seven `*.test.sh` legs left both `tools/gate-legs.json` and the kit's own
`kit.toml`"), and `grep -c GATE_SELFTESTS AGENTS.md` is zero. This same diff DID add the correct
instruction to `memory/guides/SESSION-KICKOFF.md:118` — "GATE_FULL does NOT unlock them. A DoD needs
BOTH" — which is loaded only by `/session-kickoff`, while `AGENTS.md` is the always-loaded charter.

**What breaks.** A session following the charter runs `GATE_FULL=1 bash tools/run-gates/run-gates.sh`,
sees `gates GREEN — 43/43 legs passed (42 held: …)`, records a Definition of Done against a bar that
executed half its legs, and writes a stamp the push boundary will refuse. Two documents give two
answers to one question and the authoritative one is wrong. Someone has already paid for this line
once: a human's memory note reads "a DoD needs `GATE_FULL=1 GATE_SELFTESTS=1`; GATE_FULL alone says
nothing about the kits". This is the charter's own "a value stated in prose beside the source that
owns it" rule, broken by the build that moved the source.

**The exact fix.** Replace AGENTS.md:482 with two lines:

```
GATE_FULL=1 bash tools/run-gates/run-gates.sh                       # ignore every leg GUARD — not the kit holds
GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh      # what pre-push runs here, and what a DoD needs
```

Mirror the correction into AGENTS.md:226's everyday-command catalog string. Replace the
unattended-specific paragraph at AGENTS.md:505-513 with the general rule — a leg's `subject` field
decides, kit-subject legs are held, `GATE_SELFTESTS=1` asks for them — and state explicitly that the
unattended kit's own suites are NOT in that population and still need
`bash tools/unattended/run-unattended-gates.sh`, otherwise `GATE_SELFTESTS=1` reads as "every kit's
self-tests" and is not.

---

## H5 — the RED summary line's denominator still counts held legs, so a failing bar reports `1/85` when 43 legs ran

**`tools/run-gates/run-gates.sh:1202`, `:1208`, `:1211`**

Unit -31 introduced `ran=$((n-skips-${ondemands:-0}))` at line 1109 under a comment that reads "THE
COUNT THAT RAN, computed ONCE and read by the verdict record, the durable summary and stdout". It is
read by the verdict record (1141) and by both GREEN emissions (1199, 1200). It is read by no RED
line: 1202, 1208 and 1211 all still print `gates RED — %s/%s legs failed` with `"$fails" "$n"`, and
`n` is incremented once per REPORTED leg at line 924 — ran plus skipped plus held.

**Reproduced** in a scratch repo (manifest: 2 repo legs, one exiting 1, plus 3 kit legs):

```
---- chunk default: RED  (2 ran, 1 failed, 0 skipped, 0 reused, 3 held)
gates RED — 1/5 legs failed (3 held: kit self-tests, GATE_SELFTESTS=1 runs them)

verdict record for the same run:  ran 2 · failed 1 · skipped 0 · held 3 · reused 0
```

GREEN says `2/2` and RED says `1/5` for the same population.

**What breaks.** On today's manifest, every bar not launched with `GATE_SELFTESTS=1` — including the
documented `bash tools/run-gates/run-gates.sh` and `GATE_FULL=1 bash …` — prints
`gates RED — x/85 legs failed` while 43 legs executed. A reader subtracts and concludes 84 legs
passed; 42 of them never ran. Before this build the two denominators coincided on the authoritative
run because `GATE_FULL=1` forced skips to 0; that property is gone, so the overstatement is now ~49%
on the authoritative path. The line lands in three durable places: stdout, `gate-last-summary.txt`,
and `gate-last-failure.txt` — the file AGENTS.md instructs sessions to read instead of piping the bar
through `tail`. It is also the exact arithmetic unit -31's own comment forbids: "counting it in the
total is the green-by-absence class stated as arithmetic". The only RED-total assertion in the suite
is run-gates.test.sh:316, over a fixture with no held legs.

**The exact fix.** Replace `"$n"` with `"$ran"` in all three RED emissions (1202, 1208, 1211); `ran`
is already in scope from 1109. Add an arm beside the existing 3h3 block: the `$S2` heldmath fixture
with one repo leg swapped for a failing one must print
`gates RED — 1/2 legs failed (3 held: …)`, observed RED before the fix.

---

## M1 — govkit's descriptor-vs-manifest subject cross-check exempts the one case it exists to catch: a manifest row with no `subject`

**`tools/govkit/govkit.py:898`**

```python
                    elif m_sub is not None and d_sub != m_sub:
```

Inside the `else:` branch that has already established `nm in manifest`, `m_sub` is `None` only when
the manifest row omits `subject` entirely. The agreement arm is guarded on `m_sub is not None`, so
omission is silently exempted — while the sibling exempt-leg path at line 933 DOES fail on exactly
that omission (`if _x_sub is None: r.fail(...)`). The runner meanwhile defaults a missing key to
`repo` (run-gates.sh:717, `subjects+=("${sj:-repo}")`) and `cmd_apply` emits the DESCRIPTOR's value
to every adopter (govkit.py:2631).

**Reproduced end to end on the live tree.** Appended
`{"name":"probe leg","argv":["bash","tools/check-microformats.test.sh"]}` (no subject) to
`tools/gate-legs.json` and a matching `[[gate_leg]] name = "probe leg" … subject = "kit"` to
`tools/govkit/entries/check-microformats.kit.toml`. First `selfcheck` → rc=1, "gate leg 'probe leg'
has no row in tools/govkit/subject-pins.tsv … Regenerate with `selfcheck --write`". Ran the
prescribed `--write`; the pin was written as `probe leg\trepo` (govkit.py:964,
`live = {nm: (manifest_subject.get(nm) or "repo") …}`). The next `selfcheck` → **rc=0, fully green**,
with the descriptor saying `kit` and the manifest saying nothing. All three files restored; tree
clean. The same happens for an EXISTING leg: delete the key, and the -29 ratchet reds once, then the
prescribed `--write` erases the evidence and the disagreement is permanently green.

No arm covers the line-899 refusal either: grepping `selftest.py` and `matrix.py` for "disagree about
whether this leg runs" returns nothing.

**What breaks.** gov runs the leg on every bar (manifest default `repo`) while every adopter holds it
forever (descriptor `kit`), with the deployer's own two-spellings check green — exactly the drift the
block's comment says it forbids ("two spellings of one fact, drifting exactly where nobody is
reading"), arriving through the one input value the arm does not quantify over, and with the
ratchet's remediation instruction as the path that makes it permanent.

**The exact fix.** Drop the guard and compare against the same default every reader applies:
`elif d_sub != (m_sub or "repo"):`, wording the message for the null case ("the manifest declares no
subject, which every reader defaults to repo"). Better still, mirror line 933 with a standalone
positive requirement: every leg present in `tools/gate-legs.json` must carry an explicit `subject`.
Add an arm in `selftest.py`'s ratchet fixture staging a descriptor `kit` against a manifest row with
the key deleted, asserting rc=1.

---

## M2 — `run-gates.test.sh`'s assertion floor still reads 102 while the suite now executes 123, so the entire 21-assertion subject block is unprotected

**`tools/run-gates/run-gates.test.sh:45`**

`FLOOR_ASSERTIONS=102` is byte-identical at base and at HEAD
(`git show b164a296:tools/run-gates/run-gates.test.sh | grep -n FLOOR_ASSERTIONS` → `45:FLOOR_ASSERTIONS=102`).
Its own comment at 43-44 states the purpose: "an EXECUTED assertion count, incremented at each
assertion rather than written as a literal. A hardcoded count is the recorded failure this leg exists
for."

**Measured.** I ran the suite in this worktree: `PASS (123 assertions)`, exit 0. Static
`n=$((n+1))` sites went 84 at base to 105 at HEAD, and
`awk 'NR>=517 && NR<=700 && /n=\$\(\(n\+1\)\)/{c++}'` counts 21 in the new block. 123 − 21 = 102,
exactly the floor. The sibling harness DID bump its floor in this same build:
`tools/run-gates/profile_bar.test.sh:21` moved 33 → 36 for three new arms.

**What breaks.** Cases 3h2, 3h3 and 3h4 — every arm proving the hold mechanism, the `GATE_FULL`
non-bypass, the held arithmetic and the all-held refusal — can be deleted wholesale and the leg still
passes at exactly the floor. The one guard written to catch "arms went missing" now sits precisely at
the boundary where the newest arms went missing.

**The exact fix.** `FLOOR_ASSERTIONS=123`, in the same commit, the way profile_bar.test.sh did. (And
36 → 38 in profile_bar.test.sh, per B3.)

---

## M3 — `baseline_units` was added to the one-spelling library but calls `region()`, which the library does not define and which is spelled twice — and both gates comparing those spellings were held in the same commit

**`tools/unattended/lib-unattended.sh:177`**

The library's header (1-15) states its whole purpose: "the predicates the driver and the gate leg
must answer IDENTICALLY… Two spellings of one rule is `two-answers-to-one-question`, and the fix for
it is one spelling, which is this file." The new `baseline_units()` (147) calls
`region - '<!-- gen:build-units -->' …` at line 177, and `region()` is defined nowhere in this file.
It is defined twice — `tools/unattended/check-unattended.sh:91` and
`tools/unattended/unattended.sh:467` — and resolves late-bound from whichever caller sourced the
library. (`grep -n "^region()"` confirms both, and confirms its absence from the library.)

The two awk bodies are semantically identical today, but nothing on the default bar asserts it any
more. Only two gates compare them: `marker contracts`
(`tools/memory-tree/marker-contract.test.sh:102-103` slices `r_check` out of check-unattended.sh and
`r_unatt` out of unattended.sh and runs a case table over both) and the `kickoff_region` row of
`tools/lib/resolve-python.test.sh:91` — and BOTH were set `subject = "kit"` in this same diff (see
H1). Worse, the driver's copy is not even in the parity population: `grep -rn ">>> kickoff_region"`
finds the marker in `skills/session-kickoff/manifest-check.sh:143` and
`tools/unattended/check-unattended.sh:90` and nowhere else, so `resolve-python.test.sh:88`'s
`git grep -l` never reaches `unattended.sh`.

**What breaks.** The unit that exists to give "what roster did this run start with" ONE answer routes
it through a predicate with two implementations, and the gates that assert those two agree were taken
off the bar in the same commit. A divergence makes check 24 and the driver's check 48 disagree again
— the exact wedge TOOL-dUnstalledConvoy-33 was written to remove.

**The exact fix.** Move `region()` into `tools/unattended/lib-unattended.sh` — it already holds
`GIT()`, `id_rows()` and `normpath()` for this reason — and delete both copies, leaving
`unattended.sh`'s `splice()` where it is. If the copies must stay for the copy-install story, at
minimum wrap `unattended.sh:467-474` in `# >>> kickoff_region` / `# <<< kickoff_region` so the
existing `PARITY_ROWS` row covers it, and make at least one repo-subject leg run that assertion.

---

## M4 — the all-held refusal exits 2 between the run header and the verdict record, manufacturing the documented crash signature and leaving a stale GREEN in `gate-last-summary.txt`

**`tools/run-gates/run-gates.sh:1116-1123`**

The refusal `exit 2`s after the reporting pass and the ledger merge, but BEFORE the verdict record
(1136-1152) and before either summary-file write (1199 / 1202). The verdict block's own header at
1137-1139 says: "WRITTEN LAST, and its ABSENCE is the crash signal — the only one needed. A run that
dies anywhere between the header and here leaves a directory with a header and no verdict, which is
unambiguous". `tools/run-gates/run-gates.evidence.test.sh:246-247` arms exactly that property after a
hard kill: `[ -f "$d/verdict" ] && nope "a verdict exists after a hard kill, so its absence is not
the crash signal" || ok "no verdict after a hard kill (absence IS the crash signal)"`.

**Reproduced.** Scratch repo, first an ordinary partial bar (1 repo leg + 2 kit legs) to populate the
records, then the manifest reduced to two kit legs:

```
run-gates: … so this run executed NOTHING. Refusing to report a green over an empty population.
rc=2
--- run dir contents:   header          <- no `verdict`
--- gate-last-summary.txt:
    gates GREEN — 1/1 legs passed (2 held: kit self-tests, GATE_SELFTESTS=1 runs them)   <- the PREVIOUS run
```

The refusal itself is correctly narrow. I confirmed it does not fire when anything was guard-skipped,
when anything was reused (`GATE_REUSE=1` with one repo leg reused: rc=0,
`1/1 legs passed (1 reused) (2 held…)`), when a repo leg exists, or with the switch on.

**What breaks.** Two different states now produce the identical durable signature "header present,
verdict absent": a crashed run and a deliberate configuration refusal. That is
two-answers-to-one-question landing on the one signal the runner declares unambiguous. Separately, a
refusing run leaves `gate-last-summary.txt` holding the previous run's `gates GREEN` line, so the
durable record says GREEN for a run that refused. Reachable for any adopter whose installed kits are
all subject=kit, which is the population unit -26 exists to serve.

**The exact fix.** Either hoist the refusal above the RUNDIR verdict block and let the existing
writer run with a distinct token (`gate_verdict=REFUSED`, `ran 0`, `held N`), or, before `exit 2` at
1123, write the verdict record and overwrite `$sfile` with a `gates REFUSED — 0 ran, N held` line.
Add the assertion to the existing 3h4 arm block: after the refusal,
`.git/gate-run/<id>/verdict` must exist and `gate-last-summary.txt` must not still carry the prior
run's GREEN.

---

## M5 — the 7h3 gate-policy predicate misses a bare assignment carrying a trailing comment, and the `${VAR:=1}` default form

**`tools/govkit/govkit.py:1044`**

```python
    policy_re = re.compile(r"^[ \t]*(?:export[ \t]+)?GATE_SELFTESTS=\S*[ \t]*$")
```

The trailing `[ \t]*$` means anything after the value kills the match.

**Staged three breaks**, appending one line to `.githooks/pre-push` and running
`python tools/govkit/govkit.py selfcheck`, restoring each time. The control `export GATE_SELFTESTS=1`
REDS as designed ("'.githooks/pre-push' carries a bare GATE_SELFTESTS assignment AND is shipped by
kit 'push-main'"). But `export GATE_SELFTESTS=1  # this repo edits kits` produced 0 hits, and
`: "${GATE_SELFTESTS:=1}"` produced 0 hits. Both set the variable for every consumer of that file.

The check's header (1039-1042) justifies the bare-assignment shape only against INVOCATIONS
(`GATE_SELFTESTS=1 bash …`); a trailing explanatory comment is neither an invocation nor an exotic
construct, and it is the house style everywhere else in this tree. The arms in
`tools/govkit/selftest.py:1350-1394` cover exactly three shapes — bare assignment in payload (reds),
bare assignment outside payload (green), invocation in payload (green) — so neither gap is armed.

**What breaks.** This predicate is the entire assertion behind TOOL-dUnstalledConvoy-28;
`.githooks/gate-env.sh:11-13` states outright that the not-shipped property is "ASSERTED rather than
trusted". The most likely future edit is precisely the evading one: somebody moves the switch back
into `.githooks/pre-push` with a comment explaining why. That file is emitted verbatim to every
push-main adopter (`push-main.kit.toml:20-25`, `root_relative = true`), so the line turns the kit
self-tests back on at every adopter's push boundary — the exact defect -26 exists to remove — with
selfcheck green.

**The exact fix.** Two explicit alternatives rather than one loosened pattern: keep the current shape
with an optional trailing comment, `^[ \t]*(?:export[ \t]+)?GATE_SELFTESTS=\S*[ \t]*(?:#.*)?$`, and
add a second pattern matching `GATE_SELFTESTS[:]?=` inside a `${…}` expansion (the `${VAR:=…}` /
`${VAR=…}` default-assignment forms). Add one arm per new shape beside selftest.py:1360-1394, and
re-run the predicate over the tracked tree to confirm the 54 near-miss invocation lines still pass.

---

## M6 — `apply` writes a `subject` key into every adopter's leg manifest while the run-gates kit ships a pin of the allowed key set, with no version coupling between them

**`tools/govkit/govkit.py:2631`** · **`tools/run-gates/run-gates.test.sh:96` and `:125`**

```python
                row = {"name": nm, "argv": argv, "subject": leg.get("subject") or "repo"}
```

The key is emitted unconditionally, on every leg, for every kit. The allowed key set is pinned in
`tools/run-gates/run-gates.test.sh:96`, a file the run-gates kit ships (`include = "**"`) and wires
as the adopter-facing leg `run-gates canary` (`tools/run-gates/kit.toml:73-79`, `subject = "repo"`,
so it runs on their bar). At the base sha that pin is `{"name", "argv", "guard", "impure", "chunk"}`
(verified via `git show b164a296:tools/run-gates/run-gates.test.sh`, lines 96 and 125).

Neither version constant moved in this diff: `KIT_GOVKIT_VERSION = "1.9"` before and after
(govkit.py:37), `KIT_RUN_GATES_VERSION=1.0` before and after (run-gates.sh:19). So the
incompatibility cannot even be expressed, and nothing in the LEGS step checks the target's installed
run-gates version.

**What breaks.** An operator running this govkit with a partial selection —
`govkit apply <target> --kits memory-tree` — onto a tree whose run-gates kit predates this commit
leaves that tree with a red bar:
`canary: leg row(s) carry a key outside the pinned set […]: <leg> -> subject`. The deployer breaks
the target's own gate as a side effect of a routine apply.

**The exact fix.** Bump `KIT_RUN_GATES_VERSION` and its `gov:kit` markers in `run-gates.sh` and
`tools/run-gates/README.md` (which `tools/check-kit-versions.sh` asserts), so the key change is
versioned. Have the LEGS step refuse — or omit `subject` — when the target's installed run-gates
README declares a version below that floor. A `requires` edge from the emitting path to the
run-gates kit version is the honest form.

---

## M7 — nothing arms the pre-push hook actually sourcing `.githooks/gate-env.sh`; unit -28's mechanism half has no test anywhere

**`.githooks/pre-push:135-137`**

```sh
_gate_env="$(git rev-parse --show-toplevel 2>/dev/null)/.githooks/gate-env.sh"
# shellcheck source=/dev/null
[ -f "$_gate_env" ] && . "$_gate_env"
```

A repo-wide grep for `gate-env` outside `.git` returns: the file itself, this line,
`memory/map/generated/inventories.json`, `tools/govkit/registry.toml:223` (the exemption row),
build/spec records, and `tools/govkit/selftest.py:1376` — which writes a fixture
`.githooks/gate-env.sh` to exercise govkit's SHIPPED-PATH policy check, never the hook.
`.githooks/pre-push.test.sh` builds its fixture with a bare `git init -q "$tmp/work"` (lines 20-30)
and a hooks dir at `$tmp/hooks`, so `$tmp/work/.githooks/gate-env.sh` does not exist and the
`[ -f … ]` guard is false in every one of its 23 arms. Its new arms 19-23 supply `GATE_SELFTESTS`
through the environment (`decide_on`, `GATE_SELFTESTS=1 GOV_GATE_CMD=… git push`), not through the
hook's sourcing, and its `stamp()` helper hand-writes the record.

I verified the mechanism works today with a hand-built fixture (gate-env.sh present → stub gate saw
`GATE_SELFTESTS=[1]`; removed → `[<unset>]`), so this is a coverage gap and not a live break.

**What breaks.** gov's push boundary is now the ONLY place its 42 kit-subject legs run automatically.
If those two lines regress — a path-resolution change under MSYS, a rename, a `.` portability issue
in the hook's `sh` — govkit selfcheck still passes (the assignment lives on a path no kit claims,
which is all check 7h3 grades), pre-push.test.sh still passes, and the full bar still prints GREEN
while executing half of it. Nothing in the repo would report the loss. §7's rule is that a new gate
is not landed until its failing case has been observed; here the failing case cannot be produced by
any suite. The -26 ledger records AC1 as "the hook sources it when present" — an assertion, not a
check that exercises it.

**The exact fix.** Add an arm to `.githooks/pre-push.test.sh`: write
`$tmp/work/.githooks/gate-env.sh` containing `export GATE_SELFTESTS=1`, point `GOV_GATE_CMD` at a
stub that records `${GATE_SELFTESTS:-unset}` to a file, push, assert the file reads `1`; then remove
the file and assert `unset`. Both halves, since the negative alone passes against a hook that never
sources anything. About six lines each.

---

## L1 — six of the twelve refusal branches this build adds to `govkit.py` are reached by no arm, and the mechanism meant to catch that has never run its join half

**`tools/govkit/govkit.py:888`, `:895`, `:899`, `:934`, `:939`, `:967`, `:991`, `:1001`** ·
**`tools/govkit/refusal_join.py:41`**

Grepping `selftest.py`, `matrix.py` and the govkit `*.test.sh` files for each refusal's distinctive
text finds **zero** hits for all of:

- `:888` "declares gate leg '{nm}' with no `subject`"
- `:895` "outside the closed set kit|repo" (descriptor arm)
- `:899` "disagree about whether this leg runs by default"
- `:934` "is a leg in tools/gate-legs.json that declares no `subject`"
- `:939` "declares subject '{_x_sub}', outside the closed set"
- `:967` "carries a TAB in its name", `:991` "the subject ratchet has no pin", `:1001` "has a row with no tab"

The repo's guard against exactly this is `tools/govkit/refusal_join.py`, whose docstring is "every
refusal branch in the deployer is reached by an arm that asserts it". Run as the bar runs it:

```
refusal-join: 160 branch(es) across 2 module(s) — enumeration only; pass a reached-set to join
rc=0
```

Nothing in the tree ever passes a reached-set — grepping for `refusal_join` outside `memory/` returns
only the leg's own argv and the file itself — so the join half has never executed. Its shrink-only
`BRANCH_PIN = 141` (refusal_join.py:41) was already 19 short of the current 160, against its own
stated convention ("Raised rather than left slack, because a floor that trails the population stops
catching the matcher going blind").

**What breaks.** Six new refusal messages are unverified text: any of them can be misspelled,
unreachable, or emit the wrong operator instruction with nothing reporting it. **M1 above is a live
instance** — the `:899` refusal has no arm and turns out to be skippable. The inertness of
`refusal_join` predates this build; this build is the one that widened the unarmed set.

**The exact fix.** Raise `BRANCH_PIN` to 160 in the same commit, per the file's own convention. Add
five cheap arms in `selftest.py`'s ratchet fixture: a descriptor leg with no subject, one with
`subject = "Kit"`, a manifest/descriptor mismatch, an exempt_leg with no manifest subject, and a pin
row with no tab. Separately, wire `refusal_join`'s join half to a reached-set (a trace hook in
selftest.py writing the anchors, the way `corpus_ids.py` already does) so "enumeration only" stops
reading as coverage.

---

## L2 — the run-gates kit README ships to every adopter and never mentions the held verb or the switch

**`tools/run-gates/README.md`**

`tools/run-gates/kit.toml:17-19` declares `[[files]] include = "**"`, so `README.md` lands in every
target. `grep -c GATE_SELFTESTS` returns **0** in `tools/run-gates/README.md`, **0** in
`WIRE-INTO-PROJECT.md`, and **0** in `coding-governance-agents.template.md` — the shipped charter an
adopter's `AGENTS.md` is rendered from. The only adopter-facing statements are the transient
`govkit apply` prints (govkit.py:2666-2683) and the per-run leg line
`GATE held  <leg>  (kit self-test, set GATE_SELFTESTS=1 to run)`. gov's own
`memory/guides/SESSION-KICKOFF.md` was updated; the shipped equivalents were not.

**What breaks.** An adopter's durable documentation says `GATE_FULL=1 … what a DoD needs` (the
pre-change wording, inherited from the same charter line H4 names) while roughly half their manifest
is held and `GATE_FULL` does not unlock it. The install-time print is seen once, by whoever ran
apply, and is gone. The leg line is self-describing, which caps the damage — but nothing an adopter
can re-read tells them a complete bar needs both variables.

**The exact fix.** Add a short section to `tools/run-gates/README.md` covering the fifth verb, the
`subject` field's two values, and `GATE_SELFTESTS=1` — stating explicitly that `GATE_FULL` does not
imply it. Mirror the one-line command into the charter template's merge-bar block so a rendered
`AGENTS.md` carries it, and keep the pair honest with the existing playbook-parity gate.

---

## L3 — ten `subject` keys sit under a comment block that documents the table that FOLLOWS them

**`tools/memory-tree/kit.toml:191`** · **`tools/workflows/kit.toml:70`** ·
**`tools/govkit/entries/push-main.kit.toml:68`** · **`tools/govkit/entries/kickoff-manifest.kit.toml:65`**
· and the same shape in `tools/codebase-map/kit.toml:87`, `tools/drift-audit/kit.toml:90`,
`tools/memory-recall/kit.toml:64`, `tools/playbook/kit.toml:58`, `tools/run-gates/kit.toml:60` and
`:70`, `tools/unattended/kit.toml:92`.

In `push-main.kit.toml` the `[[gate_leg]]` for `pre-push self-test` runs 63-66 (name, argv, guard).
Lines 67-70 then read: a four-line comment beginning "Line-ending pins this kit needs in a TARGET…",
then `subject = "repo"`, then `[[lf_pin]]`. Parsed with `tomllib`, all ten currently attach to the
intended preceding `gate_leg` — verified — so this is a placement hazard, not a live defect. But the
sibling leg in the very same file puts `subject` immediately after `name` (line 49), so two rows in
one file do not agree on placement.

**What breaks.** A reviewer reading `push-main.kit.toml` sees a `[[gate_leg]]` with no subject and a
stray `subject` under the lf_pin heading. Any future insertion of an `[[lf_pin]]` row above that
line, or a move of the comment block with the pins it describes, silently reparents the key and the
leg loses its declaration. That fails closed — govkit.py:888 reds with "declares gate leg … with no
`subject`" — so the cost is a confusing red on an unrelated edit, not a wrong bar. Cheap to remove.

**The exact fix.** Move each `subject = …` up so it sits with its leg's `name`/`argv`/`guard`, above
the blank line and the comment that introduces the next table — the shape already used at
`tools/run-gates/kit.toml:80` and `tools/govkit/entries/push-main.kit.toml:49`.

---

# What was REFUTED, and why

A review listing only survivors hides its own precision. Eight findings were killed by the skeptic
pass; none was resurrected on my own read, and **nothing in the confirmed list was dropped** — all
eighteen survived byte-level re-verification, and the four that carried measurements
(the profile_bar staged break, the RED-denominator reproduction, the `selftests` unconditional-`1`
break, and the 123-assertion count) were re-run rather than trusted.

1. **"Two durable records of one run both carry a field named `ran` and disagree."** Entirely
   pre-existing. `git show b164a296:tools/run-gates/run-gates.sh` line 1075 already carried
   `printf 'ran\t%s\n' "$((n-skips))"` — same field name, same reuse-inclusive value — while `c_ran`
   already excluded reuses in favour of `c_reuse`. The build's only change was subtracting
   `ondemands`, applied consistently on both sides. Both records also carry `reused` separately, so
   the decomposition is not lost. The label is overloaded; this diff neither introduced nor
   aggravated it.

2. **"The receipt's new `subject` field is written but never compared, so a target that flips a held
   self-test back on shows no drift."** The field is not inert: govkit.py:2670 reads `subject` back
   out of the receipt rows to drive the adopter-facing HELD-legs message. And the comparison at
   2636-2640 is not a receipt-vs-target comparison for ANY field — `prev` is the receipt row while
   `argv`/`guards` are freshly rendered from the descriptor, so a target's hand-edit of `argv` is
   equally unreported. `subject` is not special, and the proposed fix would red a legitimate
   descriptor-side change rather than catch the target edit described.

3. **"A descriptor flipping repo→kit silently removes a leg from every adopter's bar."** Not silent.
   run-gates.sh:936 prints `GATE held  <leg name>  (kit self-test, …)` for every held leg on every
   run and 1103 appends the count to the verdict line, so the adopter's own bar names the leg each
   time. govkit.py:2670-2683 prints the count plus the exact `GATE_SELFTESTS=1 <their runner>`
   command at install time. On the gov side the -29 pin ratchet reds until the pin moves in the same
   commit, so the change is a reviewed diff before any adopter sees it.

4. **"Check 7h3 re-implements `resolve_rule_pool`, silently dropping every non-`**` glob include."**
   (Raised twice, refuted twice.) The claimed divergence does not exist: `resolve_rule_pool`
   (govkit.py:2017) special-cases only `**`, and its fallback at 2037 is literally
   `return rule_sources(desc, rule)`, which itself skips any include containing `*`, `?` or `[`. So
   an `include = ["*.sh"]` rule ships NOTHING through `apply` either, making 7h3's derived set
   correct rather than under-derived. In the `**` branch 7h3 is if anything MORE inclusive, since
   `resolve_rule_pool` additionally subtracts sibling-claimed destinations — a superset, the safe
   direction for a ban check. 7h3 also cannot call it as written: that function needs a target
   `ctx`, and selfcheck has no target.

5. **"A derived leg count is written in prose beside the file that owns it."** The line sits inside a
   dated ceiling LEDGER (`# RAISED 132600 -> 132760 on 2026-08-24 (TOOL-dUnstalledConvoy-26)`), whose
   established convention is that every entry quotes the measurements taken at its own date. A dated
   record of what justified a raise is a historical fact, not a live claim. The live claim it paid
   for, `memory/guides/SESSION-KICKOFF.md:118`, carries no number at all. The ledger is also on the
   BY DESIGN list.

6. **"The manifest KNOWN key set is pinned twice in `run-gates.test.sh`."** The duplicate predates
   this diff — `git show b164a296:tools/run-gates/run-gates.test.sh` carries the set at both line 96
   and line 125; the diff only added `subject` to each. And there is no bad outcome: a key MISSING
   from line 96's set reds loudly on the real manifest, and a key wrongly ADDED requires a deliberate
   author edit to the pin, at which point the pin is the broken thing. The control never certified
   the key set, so it cannot silently certify a wrong one. (The *versioning* half of this area is a
   real finding and survives as M6.)

7. **"Nothing asserts that this repo's gate policy is still ON."** The mechanical half is true —
   emptying `.githooks/gate-env.sh` reds nothing — but the stated impact rests on a misreading. The
   note at govkit.py:1079 is `gate policy: {len(policy_files)} file(s) assign GATE_SELFTESTS`, and
   `policy_files` counts files that ASSIGN the variable, not files that ship it. I re-derived it over
   the tracked tree: it is 1 today and becomes 0 the moment the export is lost, and `Result.emit`
   prints every note unconditionally — so the good and the claimed-bad states print DIFFERENT
   numbers. The bar is not silent either: 1103 appends `(N held: …)` to every summary and 1146 writes
   `held\tN` into the run record. The check's own header at 1033-1035 declares this scope boundary,
   which is §7's required disclosure rather than a hidden gap. (The *predicate* half is a real
   finding and survives as M5; the *arm* half survives as M7.)

8. **"The -27 arms grade a `selftests` value the producer cannot emit."** The byte-level claim checks
   out — `stamp()` writes `0` or nothing where the producer writes an empty string — but the named
   house class (`staged-break-substitutes-a-synthetic-value`) requires the substituted value to
   REMOVE a property the mechanism depends on. The sole consumer, `.githooks/pre-push:215`, is
   `[ "$rec_st" != "1" ]`: `0` and the empty string land on the same branch, so the arms exercise the
   forcing branch with a value in the same equivalence class as the real one. Arm 21 separately
   covers the absent-key shape. (The genuinely missing half — no arm on the PRODUCER at all —
   survives as H2.)

---

# What this review could not check

Named honestly, because a review that does not say where it stopped is claiming coverage it does not
have.

- **The unattended kit's own seven `*.test.sh` suites were not run.** A standing owner instruction
  forbids running them, and this review honoured it. B2 was therefore verified by reading
  `baseline_units` and `check-unattended.sh:1505` against the base blob and by a hermetic probe
  sourcing `lib-unattended.sh` alone, never by executing `check-unattended.test.sh`. Whether any
  *other* arm in those suites reds against the -33 refactor is unknown to this review. The build's
  own spec states the same gap for -33.

- **`govkit`'s full `apply` was never executed against a real target.** B1 and M6 are derived by
  reading `read_gate_verdicts`, the transition table, the emitter and the shipped `[gate_runner_seed]`
  templates, plus the base blob for the pinned key set. No adopter tree was upgraded to observe the
  false red directly. The reasoning is closed on the bytes, but the failure has not been *seen*.

- **`matrix.py` was read only for its AC9 arms.** The rest of the deployer's matrix harness, and
  `selftest.py` beyond the ratchet fixture and the gate-policy arms at 1350-1394, went unread.

- **No full bar was run.** `run-gates.test.sh` was executed (123 assertions, green);
  `check-protocol-parity.test.sh` was executed as a staged break and restored; `refusal_join.py` and
  `govkit.py selfcheck` were executed. The other ~80 legs were not, so this review says nothing about
  whether the tree is green.

- **`tools/codebase-map/`, `tools/drift-audit/`, `tools/memory-recall/`, `tools/playbook/`,
  `tools/agent-instructions/` and `tools/pytest-parallel-guardrails/` were read only where the diff
  touched them** — i.e. their `kit.toml` `subject` rows. Whether any of those legs is *correctly*
  subjected under -30's criterion was not audited leg by leg; H1 reports the four whose guards
  visibly name repository paths, and a per-leg audit of the remaining 38 kit-subject rows is owed.

- **The memory/build records, the RUN.md front matter and the map dossiers were not reviewed.** This
  was a code and configuration review. The two records-only items on the BY DESIGN list (the ceiling
  ledger raise and the lexicon stamp move) were taken on trust as instructed.

- **Windows-specific behaviour of the new code paths was not exercised** beyond what the executed
  suites cover — in particular the `. "$_gate_env"` sourcing under MSYS `sh`, which M7 flags as
  unarmed and which I verified only by hand on this node.
