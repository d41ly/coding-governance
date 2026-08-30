# Wave 1 — LENS 5: are the instruments lying?

**Serves:** research TOOL-aScouredKit-1

## Verdict: CLEAN WITH FIXES


**Subject:** whole repo at `093730e40355d6a04300966f791f2634379e8b45`
**Lens:** blind gates, vacuous assertions, numbers that cannot move, exemption lists used as silencers
**Node:** `a` · worktree `.claude/worktrees/kit-adversarial-review-15ed31`
**Method:** every claim below was produced by RUNNING the tool and, where the claim is "this can be
made to pass while blind", by staging the minimal break and observing the green. The tree was
restored after every probe (`git status --porcelain` verified clean at start and at finish).

---

## 0. What I ran

```
python tools/drift-audit/drift_report.py                       # 11 signals
python tools/drift-audit/drift_report.py --check               # exit 0
python tools/drift-audit/drift_report.py --json                # per-signal detail
python tools/codebase-map/test_codebase_map.py                 # 5 arms, all ok
python tools/lexicon/lexicon.py                                # + --measure
python tools/govkit/govkit.py selfcheck                        # 15 notes, rc 0
bash tools/check-testsuite-counts.sh                           # silent, rc 0
python tools/memory-tree/check-arms.py --check                 # silent, rc 0
bash tools/memory-tree/check-method-carriers.sh
bash tools/workflows/check-verifier-fanout.sh
bash tools/check-agent-cap-restatement.sh
bash tools/check-dead-paths.sh
bash tools/check-install-prefix.sh
bash tools/check-kit-versions.sh
GATE_LEGS=<fixture> bash tools/run-gates/run-gates.sh          # the hold-predicate demo
```

Plus reads of `tools/run-gates/run-gates.sh`, `.githooks/pre-push`, `tools/govkit/govkit.py`,
`tools/drift-audit/drift_report.py`, `tools/drift-audit/drift_signals.py`,
`tools/codebase-map/map_extractors.py`, `tools/workflows/check-review-join.sh`,
`tools/check-testsuite-counts.sh`, `tools/govkit/subject-pins.tsv`,
`<git-common-dir>/gate-full-green`, `<git-common-dir>/gate-last-summary.txt`,
`<git-common-dir>/gate-ledger.tsv`, and both backlog shards.

## 0b. Instruments I tried to break and could NOT — stated because a lens report that only lists
## failures is itself a biased instrument

- **codebase-map coverage ratchet CAN move.** Created `tools/zzz-probe-kit/`; the gate went RED with
  `UNCLAIMED {'kits': ['zzz-probe-kit']}` AND `STALE inventories.json`. Two independent arms fired.
  The `kits` extractor enumerates the tree, so tomorrow's kit needs no code patch.
- **The LANGS mode ratchet CAN move**, and my first hypothesis about it was WRONG. `TOOL-dScaffoldedMirror-6`
  (CLOSED) claims a "coverage floor plus a `LANGS` mode ratchet". There is no floor and no ratchet in
  `tools/lexicon/lexicon.py` — flipping `py:python-ast:parser` to `py::dark` collapses coverage from
  42.4% to 7.6%, drops the P1 graded population from 1007 to 97, and still prints `lexicon OK`, exit 0.
  I was about to report that as a closed-but-live defect. It is not: the ratchet lives in
  `tools/drift-audit/drift_report.py:243` (`LANG_MODE_RANK`) and `drift-audit records` (leg 53) reds
  on the same staged flip with `RATCHET WEAKENED — .lexicon.conf: LANGS .py moved parser -> dark`.
  Two kits, one guarantee. Verified both directions.
- **`check-review-join.sh`** refuses rather than passing on every environment failure it can name
  (no node, absent predicate, uninterpretable status), and excludes itself from its own population
  for a stated reason. It is the best-instrumented gate in the tree.
- **`check-dead-paths.sh` / `check-install-prefix.sh` / `check-agent-cap-restatement.sh`** each print
  a derived population count AND a waiver count on green, and each reds on a STALE waiver (a row
  whose subject now complies). `tools/dead-path-waivers.txt` holds 8 rows, keyed on matched TEXT plus
  an ordinal rather than a line number, and every row is one of three declared classes. That is an
  exemption list doing its job, not a silencer.
- **`govkit selfcheck` asserts the shipped surface in BOTH directions** and reports six live
  divergences between `tools/check-kit-versions.sh` and the registry as `reported, not repaired`.
  Honest.
- **Ceilings are LIVE on this node** — `gate-last-summary.txt` records `ceilings live`, so my
  hypothesis that `timeout` was missing and every ceiling was inert is refuted. See F3 for what is
  actually wrong with them.

---

## F1 — BLOCKER. `chunk` decides whether a leg runs, and nothing ratchets `chunk`

`tools/run-gates/run-gates.sh:947`:

```bash
if { [ "${subjects[$i]}" = kit ] || [ "${chunks[$i]}" = selftests ]; } \
   && [ -z "${GATE_SELFTESTS:-}" ]; then
  printf 'ondemand' > "$WORK/$i.rc"; continue
fi
```

TWO fields decide whether a leg runs on the automatic bar: `subject` and `chunk`. The ratchet that
exists to make that decision visible in a diff — `tools/govkit/subject-pins.tsv`, enforced by
`tools/govkit/govkit.py:1380-1413` — pins ONLY `subject`. Its own failure message states the
doctrine it does not implement: *"an unpinned leg is one whose side of the bar nobody chose."*

**Demonstrated.** I flipped `memory hygiene` (`tools/gate-legs.json:989`, the memory-tree hygiene
gate, `subject: repo`, ceiling 12720) from `"chunk": "records"` to `"chunk": "selftests"`:

```
$ python tools/govkit/govkit.py selfcheck
govkit: legs: 86 in the manifest · 68 claimed · 18 exempt
govkit: subject pins: 86 pinned · 40 held
...
rc=0                        # ← no complaint, and the "held" count did not move
```

And the hold itself, demonstrated on a two-leg fixture manifest through `GATE_LEGS`:

```
$ GATE_LEGS=$T/legs.json bash tools/run-gates/run-gates.sh
GATE ok    probe A repo-records
GATE held  probe B repo-selftests  (self-test, set GATE_SELFTESTS=1 to run)
gates GREEN — 1/1 legs passed (1 held: every self-test, GATE_SELFTESTS=1 runs them)
rc=0
```

Both fixture legs carry `subject: repo`. The only difference is `chunk`. The held one is reported as
GREEN 1/1.

**Reach.** `GATE_FULL=1` does NOT undo this — the hold is evaluated before the guard pass and
`GATE_FULL` means "ignore every guard", explicitly not "run the self-tests" (same file, lines
924-931). `.githooks/pre-push` never sets `GATE_SELFTESTS` (`govkit selfcheck` measures it:
`gate policy: 0 file(s) assign GATE_SELFTESTS`). So a one-word edit to `tools/gate-legs.json` removes
any leg from every bar this repo runs, at every boundary, and the only thing that would notice is a
human reading the diff — which is precisely the property `subject-pins.tsv` was built to stop
depending on.

The one arm that reads `chunk` at all is `tools/run-gates/run-gates.gov.test.sh:340`, and it only
asserts membership in a six-name vocabulary — `selftests` is a legal name, so it passes. That leg is
itself `chunk: selftests` and therefore held off every default bar.

**Fix:** add the `chunk` value to each row of `tools/govkit/subject-pins.tsv` and to the ratchet
comparison at `govkit.py:1404-1411`, so a leg leaving the bar by either field reds until the pin
moves in the same commit. Same regeneration verb, same failure text.

---

## F2 — HIGH. `govkit selfcheck` reports the wrong held count, and `subject-pins.tsv` states a rule
## the runner does not implement

`tools/govkit/govkit.py:1413`:

```python
r.note(f"subject pins: {len(pinned)} pinned · "
       f"{sum(1 for v in live.values() if v == 'kit')} held")
```

`held` is derived from `subject == "kit"` alone. The runner holds on `subject == kit OR chunk ==
selftests`. Measured:

```
$ python tools/govkit/govkit.py selfcheck | grep 'subject pins'
govkit: subject pins: 86 pinned · 40 held

$ cat <git-common-dir>/gate-last-summary.txt | tail -1
gates GREEN — 35/35 legs passed (5 skipped) (46 held: every self-test, GATE_SELFTESTS=1 runs them)
```

**40 vs 46.** The bar's own last recorded green ran 35 of 86 legs and held 46. The deployer's
self-check tells an operator 40. The six legs in the gap are all `subject: repo`, `chunk: selftests`:

```
branch-guard self-test · pre-push self-test · push-main self-test
recall floor arms · run-gates canary · run-gates gov canary
```

Two of those (`run-gates canary`, `run-gates gov canary`) are, by the runner's own comment at
`run-gates.sh:939-944`, *"the bar's own liveness assertion — the arms that catch a guard naming an
untracked path, which would otherwise skip forever and silently."*

The same wrong rule is written into the generated file's header, `tools/govkit/subject-pins.tsv:3-4`:

> ``# One row per gate leg in tools/gate-legs.json: <name>\t<subject>. `kit` legs are HELD off the``
> ``# automatic bar and run only under GATE_SELFTESTS=1; `repo` legs run on every bar.``

`repo` legs do not all run on every bar. Six of the 46 `repo` legs never run on any bar.

**Fix:** compute `held` from the same predicate the runner uses (`subject == kit or chunk ==
selftests`) and correct the header sentence. If F1 is taken, both fall out of pinning `chunk`.

---

## F3 — HIGH. Every leg ceiling is ≥10× its measured runtime, so §7's "cost is a verdict" cannot bite

Charter §7: *"every suite declares a wall-clock ceiling, a runner REDS on breach... Slowness that
annoys is never fixed; slowness that fails is fixed or re-declared with a reason."*

All 86 legs declare a ceiling (`run-gates.sh` correctly reports 0 unbounded). Joined against
`<git-common-dir>/gate-ledger.tsv`, which carries one measured-seconds row per leg, 85 legs have both
numbers:

| ratio (ceiling ÷ measured) | legs |
|---|---|
| minimum | **10.0×** |
| median | **37.8×** |
| worst 8 | 408× – **1229×** |

Extremes:

```
  10.0x  run-gates canary                    ceiling=13200  measured=1319.9
  10.0x  govkit selftest                     ceiling=11750  measured=1174.1
 565.2x  memory hygiene                      ceiling=12720  measured=22.5
 785.3x  playbook placeholder catalogue      ceiling=300    measured=0.4
 986.8x  workflow script syntax              ceiling=300    measured=0.3
1229.5x  agent-instructions wiring           ceiling=300    measured=0.2
```

The minimum ratio being **exactly 10.0×** across five different legs, with a 300 s floor under the
short ones, says the ceilings were derived as `max(300, 10 × measured)`. A bound that is a fixed
multiple of the measurement is not a budget — it is the measurement wearing a budget's clothes, and
it can only fire on a 10×-to-1230× regression. `memory hygiene` would have to run for **3 hours 32
minutes** before its ceiling reds; the incident this repo already recorded in its own memory
(hygiene's staged leg at 963 s against 54 s, an 18× blowup) would have passed under it.

This is the same shape `tools/check-testsuite-counts.sh` bans one file over, in its own words:
*"A FLOOR OF ZERO IS NOT A FLOOR... a pin nothing can fall below is exactly the decoration this leg
exists to remove."* The ceiling is the mirror image and nothing bans it.

Note `TOOL-aCollapsedScan-5` is OPEN and says *"no leg in `tools/gate-legs.json` declares a wall-clock
ceiling, and the manifest has no field for one across its 85 legs."* **That row's recorded
description is now wrong** — the field exists, all 86 legs carry one, and the live defect has moved
from absence to slack.

**Fix:** re-derive ceilings as `measured × small_factor + fixed_headroom` (e.g. 2× + 60 s) and let the
first breach be a conversation rather than an unreachable number; or declare the multiple in
`tools/run-gates/gate-profiles.txt` so it is a policy somebody chose rather than a constant somebody
generated.

---

## F4 — MEDIUM. `shrink_only_lists_not_shrinking` counts a fully-drained list as an offender forever

`tools/drift-audit/drift_report.py:496`:

```python
stalled = [r for r in rows if r["shrunk_by"] is not None and r["shrunk_by"] <= 0]
```

`shrunk_by = seed - now`, where `seed` is the entry count in the commit that ADDED the file
(`drift_report.py:487-493`). A list that was added EMPTY and is still empty has `seed = 0`,
`now = 0`, `shrunk_by = 0` — which is `<= 0`, so it is stalled, permanently, with no edit anyone can
make to clear it. Adding rows to it makes it worse; draining them returns it to 0.

Live instance, from `--json`:

```json
{"file": "memory/project/corpus-path-unresolved.txt",
 "what": "citations that cannot legally be repaired",
 "entries": 0, "seed": 0, "shrunk_by": 0}
```

Confirmed against git: `git log --diff-filter=A -- memory/project/corpus-path-unresolved.txt` →
`3e9249d4`, and the file's own header says *"Measured 0 at DEAD_PATH_PIN=0, so this file is empty and
the pin is a ratchet."* It has been empty since birth.

So `shrink_only_lists_not_shrinking 3/5 OUT OF TOLERANCE` is really 2 real offenders
(`curation-debt.txt` 0→4, `trace-waiver.txt` 5→7 — both genuinely grown) plus one that is
structurally un-drainable. The signal can never read 0 and therefore can never be promoted to
`gateable`. `drift_signals.py` names this exact failure one screen up, about a different signal:
*"a predicate that can legitimately reach zero offenders — which is the difference between a signal
and a permanently-red decoration."*

**Fix:** `shrunk_by < 0` for the offender test, with `shrunk_by == 0 and now > 0` reported separately
as "stalled, not shrinking" — a list at zero entries has nothing to shrink and is the success state.

---

## F5 — MEDIUM. `SHRINK_ONLY`'s prose disagrees with the file it describes

`tools/drift-audit/drift_signals.py:80`:

```python
"memory/project/unarmed-branches.txt": "fail branches with no arm; empty today and meant to stay so",
```

It is not empty. It holds three rows, all in `tools/unattended/unattended.sh` (checks 9, 27, 29),
each an unarmed fail branch:

```
tools/unattended/unattended.sh	9	1	cannot stage the run-state file, and the gate leg's whole per-run population is the index …
tools/unattended/unattended.sh	27	4	cannot derive an archive name for the finished record …
tools/unattended/unattended.sh	29	2	cannot retire the finished record …
```

The string is what `drift_report.py` prints in the `what` column of every `--json` detail row, so an
operator reading the signal's own output is told three live unarmed branches are "empty today". This
is charter §6's own rule — *"A value stated in prose beside the source that OWNS it rots between
changes"* — broken inside the tool whose job is to catch that class. The seed of 9 is recorded
correctly, which is why the row still scores as shrinking; only the human-readable half lies.

**Fix:** the gloss should describe the list's PURPOSE, not its cardinality — the count is already
derived and printed beside it.

---

## F6 — LOW. The `selftests` field on `gate-full-green` has no reachable reader in this repo

`.githooks/pre-push:215` is the sole consumer of the field `tools/run-gates/run-gates.sh:1435` writes:

```bash
if [ -z "$force" ] && [ -n "${GATE_SELFTESTS:-}" ] && [ "$rec_st" != "1" ]; then
  force="this push runs the kit self-tests and the recorded full green was earned with them HELD"
fi
```

The guard requires `GATE_SELFTESTS` to be set **in the pushing environment**. Nothing in the repo
sets it — `govkit selfcheck` measures exactly this and prints `gate policy: 0 file(s) assign
GATE_SELFTESTS`, and `AGENTS.md` states the ruling: *"ON DEMAND ONLY: no boundary sets it (owner,
2026-08-27)."* So predicate 8 is unreachable at every boundary this repo has, and the field it reads
is inert here — which the writing code's own comment says must not happen: *"written without that
reader it is an inert byte, which is what a spec audit caught rev-2 shipping."*

The live stamp confirms the state it describes:

```
$ cat -A <git-common-dir>/gate-full-green
sha^I7038bc2ca52717c74527f7a4deb5ed24944d50e9$
fingerprint^Ib4318f7c5f4490b160af6d269d29213913f62e56$
manifest_blob^If00f3ea0119c6e4501768b21bde1e7987222facc$
selftests^I$              ← empty: earned with 46 of 86 legs held
run_id^I20260830T070922Z-3299392$
```

A record named `gate-full-green`, certifying 40 of 86 legs, is accepted at the push boundary with no
qualification. The stamp's own write condition (`run-gates.sh:1425`) requires `skips == 0` but
deliberately excludes `ondemands` — documented at `run-gates.sh:1172`, and correct given the owner
ruling, but it means the word "full" in the filename is doing work the file cannot back.

This is a naming/observability defect rather than a safety one: for a SCOPED push, accepting a record
earned without the self-tests is the right coverage relation. It is listed because the field is the
only thing distinguishing the two records and nothing in this repo can ever read it.

**Fix:** either rename the stamp to say what it covers, or have `pre-push` compare `rec_st` against
the run it is ABOUT to perform rather than against an environment variable no boundary sets.

---

## Interrogation of the three supplied baselines

**`dangling_pointers_in_own_ledger -1/0 DEAD PROBE` — CAN IT MOVE? No, and it is honest about it.**
`drift_report.py:562-570` reads `ctx.ledger_dir / f"{tag}.md"`; `ledger_dir` is
`memory/project/in-flight/` (`drift_report.py:1352`), a directory deleted when the authored session
ledger was retired at `aMendedLedger` U2. The probe returns `value: -1, gateable: False, live: False`
with the note `no ledger file for node a`, and the report prints `DEAD PROBE — signal cannot move,
ignore its value`. It is the second signal off the same dead directory; the first
(`ledger_rows_contradicting_git`) is in `DECLARED_EMPTY` and this one is not, so `--check` ignores it
by `gateable: False` rather than by declaration. `TOOL-aUnmannedHelm-2` (OPEN) names the `ledger_dir`
root cause but describes the consequence in the singular — *"the probe stays DECLARED_EMPTY"* — which
covers one of the two probes. Not raised as a finding: a probe that prints "I cannot move" is the
correct behaviour this lens exists to demand, and the root cause is tracked.

**The two `EMPTY BY DECLARATION` rows — both are genuine declarations with reasons in place, and
both re-arm.** `drift_signals.py:100-102` carries a per-signal comment for each, and
`tools/drift-audit/selftest.py:1195-1290` drives both directions over one fixture (declare → drained
row is muzzled; undeclare → the same row fires). `handkept_inventories_disagreeing_with_source` is
empty because `HANDKEPT = []` at `drift_signals.py:158`, and its probe function
`_charter_mentions_every_leg` is deliberately left defined-and-unreferenced as the record of what was
being asked. This is the one place in the tree where "declared empty" is backed by an executable
proof that the declaration is not a muzzle. No finding.

**`live_backlog_rows_per_shard 217 / 89`.** The watermark has been overshot by 144% and the signal
correctly screams every run. It is `gateable: False`, so the overshoot blocks nothing; and because
nobody RAISES the pin, the `RATCHETS` justification guard that was built to price a raise
(`drift_signals.py:262-278`) never engages. The instrument is working — it is the response that is
absent. Not a lens-5 finding; it belongs to whoever owns the TOOL shard.

**`readme_mechanism_drift 24 / 79` (pin 19) and `lexicon_marginal_offense_rate 130 / 493`.** Both
report-only, both move (the lexicon rate moved to 2/42 under my staged `py::dark` flip, proving the
denominator tracks the corpus). No finding.

## Two things I checked and cleared

- **`tools/gate-lint/`** ships `ps-hygiene.py` and appears in no leg of `tools/gate-legs.json`. Its
  descriptor declares `why_no_adopter` explicitly and `git ls-files '*.ps1' '*.psm1'` returns **0**
  files, so the population is genuinely empty and the charter's own rule (*"adopted only where the
  language exists"*) is honoured. Not dead code, not a blind gate.
- **`bash tools/check-testsuite-counts.sh` prints nothing on green.** Its header declares
  `silent + exit 0 = good`, and its internals do refuse an empty population, a zero floor, an
  uncompared floor and a stale waiver. The python-suite selector gap is already
  `TOOL-cSettledDocket-10` (which says eleven; the manifest now names 19 python scripts, so the row
  has got slightly worse). Left as a known row rather than re-reported.
