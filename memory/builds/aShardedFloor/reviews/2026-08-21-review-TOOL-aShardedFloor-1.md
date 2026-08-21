## Verdict: BLOCKED
**Serves:** spec-audit TOOL-aShardedFloor-1 TOOL-aShardedFloor-2 TOOL-aShardedFloor-3 TOOL-aShardedFloor-4

Two confirmed defects would make the first code pass wrong on the two units the brief sequences first, so the set does not proceed as written. Neither is a rewrite: F1 is one acceptance criterion restated, F2 is one guard added to a scope item. Everything below was re-verified against source in this worktree at a687462.

### Lenses and refutation

M2's four cross-read axes (scope, interface, ordering, acceptance) run over the four specs, the build README and the design brief, plus the M4 lens catalogue — underspecification, contradiction, unstated assumption, prior art — with every claim each spec makes about existing code re-read in `tools/`. **25 candidate findings were refuted** by skeptics and are not carried. The refuted set has a shape worth naming: most were confident readings of a spec sentence that the *source* then contradicted, which is the same failure mode this audit exists to catch, one level up. Two refuted claims were re-established on narrower grounds and appear below as F10 and F17.

---

## Blocking

### F1 · BLOCKER · spec 2 AC2's floor identity is false by 60 and reds every mode on day one

`memory/builds/aShardedFloor/spec/2026-08-21-spec-TOOL-aShardedFloor-2.md:80-82` requires that `FLOOR_SHARD_1 + FLOOR_SHARD_2 = FLOOR_ASSERTIONS + 4` be "asserted in EVERY mode … a tripwire over three authored constants, not a measurement". The constants: `tools/unattended/unattended.test.sh:2241` is `FLOOR_ASSERTIONS=338`; the spec pins 196 and 206. **196 + 206 = 402; 338 + 4 = 342.** The `+4` relation is true of the MEASURED executed counts — the spec's own §4 at `:47-48` writes `196 + 206 = 398 + 4` correctly — and AC2 then swaps the measured total 398 for the pinned floor 338. Built literally, the tripwire fires on the unsharded run too.

The obvious repair is the dangerous one: raising `FLOOR_ASSERTIONS` to 402 pins the floor at 100 % of observation and destroys the ~15 % headroom the existing 338/398 pin deliberately carries, against a comment at `:2237-2240` that reads "Lower it in a reviewed diff or not at all" with provenance to id `TOOL-cBriefedPilot-23`.

**Fix (spec 2, rev-2, §9 line naming the conflation).** Split AC2 into two claims. (a) Per-shard floors `FLOOR_SHARD_1`/`FLOOR_SHARD_2` compared to that mode's executed `n`, set at the same proportional discount the existing pin uses rather than at the measured 196/206. (b) A duplication tripwire over EXECUTED counts, `n(shard 1) + n(shard 2) = n(unsharded) + PROLOGUE_ARMS`, with `PROLOGUE_ARMS=4` declared as its own named constant beside the seam constant. Keep the runtime floor relation in spec 3's inequality form so both files spell ONE rule. Correct the brief's pin row at `build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md:81`, or a reground re-imports it.

### F2 · BLOCKER · spec 1's fidelity fix flakes the arm spec 1 forbids touching

`spec-…-1.md:21-23` (S4) incorporates the brief's Unit D by reference, and `design-brief.md:317` prescribes it unconditionally: "Add `TS_WAITED=$(( $(ts_now) - ts_start ))` immediately before the `break` at `:483`". Traced in source: `tools/run-gates/run-gates.sh:459` takes `ts_start`, the first loop iteration then spawns `ls`, `sort`, `head`, `basename` and `mkdir` before the claim resolves at `:464-465`, and `ts_now()` is `date +%s`, which truncates. On an uncontended acquire that window sometimes crosses a second boundary, so `TS_WAITED` becomes 1 rather than 0 — and `:518` echoes it into the line that `tools/run-gates/run-gates.turnstile.test.sh:306` asserts as `^gate queue: waited 0s$`. Spec 1 §3 at `:29-33` says of that arm: "if either needs editing, this unit has been violated." A measured probe on this node put the boundary crossing at 4 of 60 first-iteration acquires, before load; `run-gates.sh:479-480` records process creation measured 25x slower under contention, and this leg runs inside a concurrent bar.

**Fix (spec 1, rev-2).** Write the guard into S4 rather than leaving it to the builder: refresh only when the run actually queued, using `ts_announced` (set to 1 at `run-gates.sh:500`) as the predicate. Add an AC arm asserting a first-iteration acquire still reports 0 across repeated runs. Name the residual in S4 rather than hiding it — when the first iteration reaps, `ts_try_reap && continue` at `:485` skips both the refresh and the announce, so the one-tick understatement S4 exists to fix survives in that path.

### F3 · HIGH · spec 3's AC7 is unsatisfiable by spec 3's own §4

`spec-…-3.md:50-51` states "the git-operation weight splits ~2:1 — and the bar's floor is the LARGER shard". `:89-90` (AC7) then requires `max(shard one, shard two)` at most **55 %** of the unsharded wall. 2:1 is 66.7 %. The brief's underlying derivation at `design-brief.md:161` is harder still: `git ` tokens split 89 before line 576 against 41 from it, i.e. 68/32. I confirmed both candidate boundaries sit after the git-heavy region — `tools/unattended/check-unattended.test.sh:574` is `git checkout -q unit; reset_tree` and `:587` is the check-14 control — so neither can move that weight forward, and §3 at `:25-26` forbids a physical split or a third shard. 55 % is an authored constant nothing in the spec derives.

**Fix (spec 3).** Derive AC7's threshold from the two candidate timings the spec already requires recording, or keep 55 % as a target and state what happens when both candidates miss it: accept the imbalance and re-price the headline (see F5). §4 and §6 currently answer one question twice.

---

## High

### F4 · The build's only observation of its own objective states no number

`spec-…-3.md:103-107` (AC15) asks for a mean span "at least the predicted margin below the recorded pre-change mean". Neither the margin, the baseline, nor the run count is stated anywhere in unit 3. The brief's version at `design-brief.md:203` carried explicit placeholders ("over N `GATE_FULL` bars at the same profile row and width … at least X s below"), so X and N were dropped rather than filled. All the candidates exist and disagree: `README.md:21` gives 292 s (27.6 %) and 282 s (30.5 %) on two different bars; the charter's `AGENTS.md:498` figure is a single 873 s reading, machine-pinned in both directions at `tools/run-gates/run-gates.gov.test.sh:210-215`; the report's four-run mean is 1001.3 s (`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:56`, `:525`). As written the threshold is chosen after measuring.

**Fix (spec 3).** Three literals: the baseline (the 1001.3 s four-run mean is the only candidate that IS a mean — name it and its record), the minimum margin in seconds, and N with a floor of 3 at the same profile row and width. Add the retention note: `run-gates.sh:550` sets `GATE_RUN_KEEP=5` and the sweep prunes older run dirs, so copy `<git-dir>/gate-run/<id>/*.leg` aside before the sixth bar or the evidence is gone before it is read.

### F5 · The README's headline is not implied by the union of the specs' acceptance criteria

`README.md:21-24` claims 292 s (27.6 %) and 282 s (30.5 %). On M2's acceptance axis, no criterion in the set implies it. AC15 is the only candidate and carries no number (F4). Spec 2's nearest thing, `spec-…-2.md:103-104` (AC12), requires both shard legs to be "below the ~766 s throughput bound" — that is a SPAN figure used as a per-leg cap, and spec 2's own measured shard 1 at 242 s (`:47-48`) clears it by more than 3x, so AC12 cannot fail on any plausible build. Spec 2 has no balance criterion at all, and its measured split is 242/145 = 62.5 %, above the 55 % its sibling holds itself to. The report's simulation row at `…aScannedThrottle-1.md:190` models each leg at exactly half.

**Fix.** Spec 2 AC12 states the balance the measured seam actually achieves rather than a bound it clears threefold; spec 3 AC15 carries the number and names its bar; the README's headline is re-derived from the accepted 63/37 driver split. Do NOT push a `<= 55 %` criterion onto spec 2 — `spec-…-2.md:37-38` forbids per-arm assignment because the file has fixture epochs that must run contiguously, so that seam is not free to rebalance.

### F6 · Units 2 and 3 change the argv of two already-emitted legs, which breaks `govkit apply` for every existing adopter

`tools/unattended/kit.toml:92-95` and `:97-100` declare both suites as emitted gate legs. The emitter compares the receipt's recorded row against the FRESH RENDER — `govkit.py:2450-2453` — never against the target's current row, so a kit-side argv change is indistinguishable from target drift and hits `r.fail` at `:2454`; the manifest write is gated on `if not r.problems:` at `:2467`, so one drifted leg blocks the write for **every** kit in that apply. This class is not novel: `memory/builds/aPacedTurnstile/reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-run-cumulative.md:154` reproduced it end to end against a scratch target and already asked for the left-shift arm. Gov's own tree is unaffected — `tools/gate-legs.json` is hand-authored here — so the failure lands only in an adopter re-applying after the change, which is exactly where nobody is watching.

**Fix (spec 2, the contract's author).** An adopter-transition item in §2 and an AC that applies the kit twice ACROSS the change on a scratch target and observes the second apply succeed; pick the mechanism in §8 (new names for both shards, or a receipt-supersede path in govkit) rather than in the diff. `spec-…-2.md:73`'s "revert is one manifest edit plus four lines" is true of gov and silent about adopters — say so.

### F7 · Spec 3's AC2 does not discharge the justification written beside it, and the artifact it compares does not exist

`spec-…-3.md:75-80` replaces a count with a per-arm PASS/FAIL vector, justified because the count "passes even when a leaked ref makes a shard-two arm pass for a different reason". A vector has the same blindness to that case: an arm that passes for the wrong reason is PASS in both runs and the vectors compare equal. It is strictly stronger than a count — it localises which arm moved — but it does not answer its own stated hazard. The artifact is also not producible: `tools/unattended/check-unattended.test.sh:16-18` defines `hit`/`miss`/`same` to print only on failure, so a green run emits one PASS line and there is no per-arm vector to slice. The hazard itself is real and confirmed: `:556` pushes `refs/heads/ahead` to the fixture origin and nothing deletes it, and `reset_tree` at `:118-124` touches only `refs/remotes/` and `refs/replace/` in the local clone.

**Fix (spec 3).** Compare STATE, not verdicts: capture `git ls-remote --heads "$ORIGIN"` and `git for-each-ref refs/heads refs/remotes` at the boundary and at the end of each mode, and require shard 2's capture to equal the unsharded run's at the same point, failing with both listings named. Add the named negative — run `--shard 2/2` with `refs/heads/ahead` planted and again with it absent and require a DIFFERENCE, or the arms do not read the leak and AC2 protects nothing. Name the specific arm to break, so two builders do not break two different ones. Spec 2's `:97-98` (AC9) already carries the per-arm byte comparison that belongs here too.

### F8 · The co-landing rule is witnessed from one side only

`spec-…-3.md:101-102` (AC14) requires the sibling to ship in the same landing, witnessed by both pairs of rows in `tools/gate-legs.json` at one commit. Spec 2 carries no mirror: its co-landing statement is prose at `:9` and `:123-124`, and every one of AC1–AC13 is satisfiable by unit 2 standing alone. The cost is measured at `memory/backlog/TOOL.md:123` — the driver alone buys 38.9 s (3.7 %) because the gate selftest becomes the new floor — and `README.md:22` calls the rule binding. Stated in three documents, enforced in one.

**Fix (spec 2).** Add the mirror criterion. Separately, settle who carries the charter figure: the brief rules at `:403` that the `AGENTS.md:498` pair moves exactly once in the LAST span-moving landing and at `:398` puts unit 4 last, yet unit 4 moves span by 16 % and names no charter edit at all — `spec-…-4.md:68-69` points at a different charter sentence. Resolve the carrier across units 2, 3 and 4 in the same rev.

### F9 · The build states no order, and the generated block points at an authored plan that does not exist

`README.md:63-66` reads verbatim "*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*" The README authors none: `:19-32` and `:34-38` carry no sequence. The brief does, at `design-brief.md:398` — `S1 -> (S2 + S3, one landing) -> S4` — with the reason at `:401`, that landing S4 first makes the shard rename penalty worse. The mechanism is real: `tools/run-gates/run-gates.sh:637` sorts by negative cached duration and the runner's own comment at `:617-618` states "A leg the cache does not know scores 0 and sorts last", so on a warm ledger a new shard name dispatches dead last — and unit 4's whole job is warming every worktree's ledger. Grepping spec 4 for its siblings returns only `:110`'s bare "As the sibling units".

**Fix.** An authored order line in the README (1, then 2+3 as one landing, then 4) AND the 2+3 prerequisite named in spec 4 §2 or §8, citing the mechanism rather than only the sequence. Under M2 the README's authored table is the roster; under M2's ordering axis, a spec depending on a unit sequenced after it is the spec's defect too. Both documents owe the line.

### F10 · The README's "what this build does" omits a unit that claims 16 % of span

`README.md:21` says sharding "is the whole win" and the section that follows covers only units 1, 2 and 3. Unit 4's mechanism appears nowhere in "What this build does"; its only mention is at `:37-38`, inside "What this build does NOT do". Against that, `spec-…-4.md:58` claims "16 % of span on any cold worktree", and `memory/backlog/TOOL.md:147` measures 15.6–16.3 % with a controlled pair (floor-leg dispatch rank 55/87 to 1/87, span 970.0 s to 925.5 s).

**Fix (the README, the roster document).** Re-scope the headline to "sharding is the whole win on the measured bar's span at the floor" and state unit 4's scope as a separate, additive scheduling win — the two wins are measured over different populations and adding them is not honest.

---

## Medium

### F11 · Three specs self-resolve forks under a standing mandate that does not exist for this build

`git ls-files memory/builds/aShardedFloor/` returns exactly six paths — the README, the brief and the four specs. There is no `RUN.md` and no mandate. The only live run mandate in the tree is `memory/builds/aScannedThrottle/RUN.md`, which is LANDED and authorizes that build. M3 (`memory/guides/BUILD-METHOD.md`) is explicit: "With no mandate, forks go to the owner", and a mandate never delegates SCOPE. Yet `spec-…-1.md:104-110` and `spec-…-2.md:117-125` both cite "the standing authority to settle forks the specs already state", and spec 2's fork (2) — shard 1's name — is fork #1 under the brief's own heading "Scope forks for the owner" at `:427-429`; its options differ in which leg names exist in `tools/gate-legs.json`, which map keys are claimed and retired in `memory/map/features/unattended.md:11`, which `tools/unattended/kit.toml` rows change, and what an adopter's emitted manifest carries. `spec-…-3.md:118` writes a bare "Resolver: this session." None of the three carries the marker `TEMPLATE-SPEC.md:97-102` mandates — `RESOLVED (agent, <date>, delegated): <pick>` plus a `ratified <date>` header tail; all four headers stop at `· streams tooling`.

**Fix.** Park spec 2 §8 fork (2) for the owner, or land a mandate and cite it by path. Re-mark the resolved forks in specs 1, 2 and 3 in the template's grammar. Note for whoever greps: spec 1's citation wraps across `:106-107`, so a phrase search finds only spec 2.

### F12 · The kit-version fork reaches no spec, and neither sharding spec names the descriptor it must edit

`design-brief.md:429-430` asks whether `KIT_UNATTENDED_VERSION` bumps 1.7 to 1.8, noting "Eight spellings across six files plus a re-render" and "My read is bump". I verified the eight: `tools/unattended/unattended.sh:33` and `tools/unattended/check-unattended.sh:18` (each a constant plus its same-line `gov:kit unattended@1.7` marker), `tools/unattended/PROTOCOL.template.md:1`, `tools/unattended/SKILL.template.md:5`, `memory/guides/UNATTENDED-PROTOCOL.md:1`, `.claude/skills/unattended/SKILL.md:5`, paired by `tools/check-kit-versions.sh:123-151`. This is the ONLY one of the brief's eight scope forks that reached no spec §8 — forks 1 and 3 land in spec 2, 7 and 8 in spec 3, 5 and 6 in spec 4, 4 is resolved in spec 4 §3. Neither sharding spec names `tools/unattended/kit.toml` in §2 either, though both must add a `[[gate_leg]]` row: `govkit.py:901-903` reds on any manifest name claimed by no descriptor.

**Fix.** Add `tools/unattended/kit.toml` to both §2s, and re-open the version fork in spec 2 §8 as an OWNER item — a kit whose declared leg set grows is an adopter-visible contract change, which is M3's veto 2.

### F13 · New arms in three units are strandable: no floor is required to rise

Unit 1 adds four arms to a suite pinned at `tools/run-gates/run-gates.turnstile.test.sh:26` (`FLOOR_ASSERTIONS=28`, compared with `-ge` at `:341`); the brief named the hole at `:329` and its AC10 at `:370` required "PASS at or above a raised floor", and `spec-…-1.md:67-93` dropped it. Unit 2's S7 at `:29-30` adds gov-canary cover and reverse-direction arms against `tools/run-gates/run-gates.gov.test.sh:70` (`FLOOR_ASSERTIONS=12`), which the brief's pin table at `:90` says must rise; no bullet in spec 2 names it. `grep -n FLOOR_ASSERTIONS` over spec 4 returns nothing, against a brief pin table at `:245-248` moving four run-gates floors. The backstop does not close it: `tools/check-testsuite-counts.sh:48-61` grades three shape facts only and never compares the pin to the arm population.

**Fix.** One AC per unit naming the raised floor as an absolute value, not a delta — `run-gates.turnstile.test.sh:26` is raised by both unit 1 and unit 4, so whichever lands second must state the number it expects. This is green-by-absence in the unit whose entire subject is observability.

### F14 · Spec 1 declares a closed four-word vocabulary and arms three states

`spec-…-1.md:18` declares `queued_from` a "CLOSED four-word vocabulary: `held` · `expired` · `unresolved` · `off`" and `:24-25` promises "four arms … one per state", repeated at `:63`. The criteria at `:69-80` arm `held` twice (contended and uncontended, on different fixtures, so they cannot collapse), plus `off` and `expired`. Nothing observes `unresolved`. I probed its reachability: it needs `run-gates.sh:391-392` to fail while the runner is already past its own repo guard at `:25`, and breaking a linked worktree's `commondir` makes `git rev-parse --show-toplevel` fail too, so the runner exits 2 before it ever reaches `:391`. No fixture in that suite can produce it. The spec legislates the remedy one bullet earlier — AC4 at `:75-80` requires an unreachable state to be "named as an unarmed arm in the header's own 'does NOT check' section" — and does not apply it here.

**Fix (spec 1).** S5 and §5 read "four arms over three reachable states"; a bullet beside AC4 names `unresolved` UNARMED with the reason. The brief's Unit D heading at `:343` ("Four arms, four states") carries the same counting error and needs the same correction, or a reground reintroduces it.

### F15 · Spec 3 never names its two leg names, and AC10 presupposes a retired one

Grepping spec 3 for its own leg names returns only `:7` (the existing name), `:93` and `:144`. `:93` (AC10) reads "`govkit selfcheck` green and any retired leg name absent from the manifest" — but spec 2 resolves naming at `:119-123` by keeping the existing name and appending a letter to shard 2, under which one key arrives and none departs. There is no retired name. Spec 3's S1 at `:13-15` enumerates what it adopts — flag grammar, parse-before-scratch-dir, refusal set, mode-selected floor, cover arm — and naming is not on that list, so AC10 is a live signal that spec 3 may intend the symmetric rename spec 2 rejected. The names are load-bearing twice: warm-ledger dispatch rank (`run-gates.sh:637`) and the map key swap at `memory/map/features/unattended.md:11`. `govkit.py:879` forbids a digit-bearing parenthetical.

**Fix (spec 3).** State both names in §2 and say whether the sibling's naming resolution binds this file.

### F16 · Spec 3 adopts five refusals and tests three, dropping the two a shard bug produces

`spec-…-3.md:58` says "the sibling's five refusals, adopted" and S1 says the same; `:83-84` (AC4) then exercises `--shard 3/2`, `--shard two`, and a bare `--shard`. The brief's set at `:104` is five and includes `--shard 1/3` (wrong arity against the declared `SHARD_ARITY=2`) and `--shard 0/2` (zero index) — the two that a manifest edit or an off-by-one in the dispatcher produces, as opposed to the two a typist produces. Since S1 requires refusal before the first `mktemp -d`, an unarmed arity check means a shard that silently runs the wrong region rather than one that refuses. The brief's Unit B acceptance at `:190` copies the same three, so both documents carry it.

**Fix.** Restore `1/3` and `0/2` in spec 3 AC4 and in the brief. The `two` versus `banana` spelling is the same refusal class and is not the load-bearing half.

### F17 · Spec 4 reverses the read precedence of the backlog row it discharges, with no supersession recorded

`spec-…-4.md:10` discharges id `TOOL-aScannedThrottle-8`; S1 at `:16-20` orders the candidates "per-worktree ledger, common-dir ledger, then both legacy filenames — merged first-wins per leg name". `memory/backlog/TOOL.md:147` — that row — prescribes the opposite: "Read the ledger from the git COMMON dir with a per-worktree fallback". The brief flagged it and instructed the spec to close it, at `:422`: "Record the choice explicitly; do not leave two rules in the corpus." The spec states its rule and never says it supersedes the row's. The two are not equivalent: under first-wins-per-worktree a stale local row shadows a fresher shared one, which is exactly what S4's coverage count exists to expose.

**Fix.** Re-word the backlog row at discharge, not only add a spec sentence. Fixing one carrier and leaving the other is the two-answers-to-one-question class this repo already tracks.

### F18 · Spec 4's closed five-word vocabulary and two header keys are unspelled

`spec-…-4.md:25-26` (S4) declares "a source token … over a CLOSED five-word vocabulary" and `:27` (S5) "two header keys recording the resolved source and the coverage". §4 at `:48-50` gives four English descriptions and one token; only `legacy` (AC2, `:80`) and `NONE` (AC3, `:81-82`) are ever spelled. The brief has the key names at `:234` — `dispatch_source` and `dispatch_known`, joining `dispatch` at `run-gates.sh:736` — and neither reaches the spec, while AC3 refers to "the source header key" as though it had been named. `TEMPLATE-SPEC.md:71` requires naming by repo identifier. Spec 1 at `:16-18` shows the contrast done right.

**Fix (spec 4 §2).** Spell all five tokens and both key names in backticks. A closed vocabulary written as prose descriptions cannot be armed.

### F19 · Spec 4 states a worktree population that expired the night it was measured

`spec-…-4.md:119-120` reads "Today 24 of 26 worktrees were ACCIDENTALLY protected by having no hint". `git worktree list` in this tree returns **six**. The row spec 4 discharges carries the correction inside itself (`memory/backlog/TOOL.md:147`): "re-derive with `git worktree list` before pricing, the population MOVES and the cleanup at 49aea26 took it to 6 the same night" — and 49aea26 is in this branch's history. The figure is load-bearing: 24/26 is how §8's owner fork is priced, and it is the quantification holding the unit at BLOCKED.

**Fix.** Re-derive at write time and quote the derivation command beside the number, or drop the count and state the property.

### F20 · The byte-identical-guard invariant both sharding units rest on is unenforceable by the gate they cite

Spec 2 S5 at `:26-27` names the exact consequence of divergent guards — "a diff runs one half and skips the other while the summary reads green" — and spec 3 S4 and AC6 make the invariant load-bearing. `govkit.py:861` builds the manifest as a set of NAMES; the join at `:863-903` never reads a `guard` field in either direction. The divergence is live today: `tools/gate-legs.json:593-597` gives `unattended gate selftest` a three-entry guard while `tools/unattended/kit.toml:95` declares two, and `:606-609` gives the driver two while `kit.toml:100` declares one. The backlog row recording this is id `TOOL-aPacedTurnstile-12` at `memory/backlog/TOOL.md:128`. Neither spec §5 cites it.

**Fix.** Cite the row in both §5s and state that descriptor-side guard identity is a documented manual check until it lands, per the charter's exemption-ships-with-its-compensating-check rule.

### F21 · Spec 1 discharges no backlog row while its subject is one verbatim, and the set is net-additive under 1,284 B of headroom

`memory/backlog/TOOL.md` measures 60,156 B against `INDEX_CAP_BYTES="61440"` (`.memory-tree.conf:147`), and `memory/project/curation-debt.txt:22-27` states that the debt row silences "checks 6, 7 AND 8 on TOOL.md, not just the byte cap". Specs 2 and 3 jointly discharge id `TOOL-aPacedTurnstile-8` and spec 4 discharges id `TOOL-aScannedThrottle-8`. Spec 1 declares none, though its subject is id `TOOL-aScannedThrottle-2` at `:148` verbatim — I counted the header printfs at `run-gates.sh:710-736` and there are exactly the 19 that row names — and `spec-…-1.md:107-108` instead OWES a new row for the `schema` field. The brief instructed at `:330` to "Close the row rather than restating the number".

**Fix (spec 1 §2).** Name the discharged row. The set's net backlog effect is currently additive with the overflow check switched off.

---

## Low

### F22 · Both sharding specs' §7 say they add no gate leg while their own scope adds a manifest row

`spec-…-3.md:111` reads "This unit adds no gate leg and no gate arm beyond its own floors", against its own S4 at `:18-19` (two manifest rows) and AC12 at `:96-98` (both shard legs as separate rows). `spec-…-2.md:113` has the same shape in softer words. `TEMPLATE-SPEC.md:161` defines §7 as the legs to keep green "plus any new gate it adds", so a builder reading §7 alone concludes no manifest row and no descriptor row is owed. Low because each unit's own ACs correct it before it can land — spec 3 AC10 reds until a descriptor claims the name, AC11 until the dossier does. **Fix:** one clause in each §7 saying the unit adds a second manifest ROW on an existing script plus its descriptor row, and no new checking surface.

### F23 · Spec 1 AC6 states a false fact about the profile table

`tools/run-gates/gate-profiles.txt` declares THREE rows — `capable` at `:46`, `modest` at `:54`, `minimal` at `:61`. The two-ness belongs to the arm: `tools/run-gates/run-gates.evidence.test.sh:411` loops `for prof in capable minimal`. `spec-…-1.md:84-85` attributes it to the file. The brief has it right at `:367`. **Fix:** name the arm — "the four-key envelope arm at `run-gates.evidence.test.sh:408-428` passes unmodified for both profile rows it exercises, `capable` and `minimal`" — and add that `modest` is deliberately not exercised, which turns an omission into a stated skip.

### F24 · The `i/n` shard token collides with the run-gates canary's leg-path heuristic, latently

`tools/run-gates/run-gates.test.sh:157-161` collects every argv token containing `/` as a pseudo-path and greps `run-gates.sh` for each at `:166-171`, reporting "leg script path '$p' is hardcoded". `LEGS_FILE` is the real manifest, so `--shard 1/2` joins that population. I confirmed the arm stays green today — `grep -nF "1/2"` and `grep -nE "[0-9]/[0-9]"` over `run-gates.sh` return nothing. What it buys is a false-positive channel whose failure message names a leg script path that does not exist. **Fix (cheapest, canary-side, named in spec 2's scope):** narrow the predicate to tokens ending `.sh`/`.py` or resolving to a tracked path. Changing the grammar to `1of2` is the alternative and costs spec 3 AC4 a rewrite.

### F25 · Spec 3 leaves a fixture-comment suspicion as a builder errand; it reproduces from source in one read

`spec-…-3.md:118-122` asks a builder to confirm in a scratch repo whether `git clean -qfd` removes the copied kit. It does not, and the file proves it: the kit is copied at `tools/unattended/check-unattended.test.sh:24`, committed at `:88`, and `PRISTINE` at `:112` is a later commit on the same history, so the file is TRACKED; `reset_tree` at `:118-119` runs `clean -qfd` without `-x`. The independent proof is at `:153-154`, where an arm resets and seds `tools/unattended/unattended.sh` with no re-copy and asserts green. So the comment at `:167-168` is wrong and the `cp` at `:169` is dead. **Fix:** fold the resolution into §8 so the minute is spent once, and keep the surrounding warning that this comment's neighbours are not trustworthy.

### F26 · The build README carries no owner decision menu

`TEMPLATE-SPEC.md:88-90` puts "the master overview and the owner decision menu" in the build-root README for a multi-spec build. `README.md:19-38` has no decision section, while `spec-…-4.md:116-125` is an explicit scope fork — wait for the undesigned id `TOOL-aMeteredTurnstile-5`, or ship a measured 669.1 s versus 5.1 s time-to-first-signal regression — which M3 makes an owner turn. Both numbers check out against `memory/backlog/TOOL.md:14`. Low because the information is one link away and the spec's BLOCKED status is what actually stops the unit. **Fix:** a short authored "Owner decision" section carrying spec 4 §8.1's two options and the 669.1 s / 5.1 s pair.

---

## Per-unit readiness

**Unit 1** (id `TOOL-aShardedFloor-1`) — **NOT READY.** Blocking: F2 (write the `ts_announced`-guarded refresh into S4, name the reap-path residual, add the still-zero arm). Also owed before code: AC1 graded as a range the harness observed and AC8's fixture parameters named (F2), `unresolved` declared unarmed (F14), the turnstile floor raise (F13), AC6 restated against the arm (F23), the discharged backlog row named (F21), and the §8 resolutions re-marked in the template's grammar (F11).

**Unit 2** (id `TOOL-aShardedFloor-2`) — **NOT READY.** Blocking: F1 (AC2 split into a per-shard floor claim and an executed-count tripwire, in the inequality form its sibling already uses). Also owed: the mirror co-landing criterion (F8), the adopter-transition item and its double-apply AC (F6), `tools/unattended/kit.toml` in §2 with the version fork re-opened as the owner's (F12), the gov-canary floor raise (F13), AC12 restated as a balance rather than a bound it clears threefold (F5), the §7 manifest-row clause (F22), the guard-parity backlog citation (F20), the canary predicate edit (F24), and the fork markers (F11).

**Unit 3** (id `TOOL-aShardedFloor-3`) — **NOT READY.** Blocking: F3 (settle AC7 against §4 — derive the threshold from the two recorded candidate timings, or state the fallback). Also owed: AC15's three literals plus the run-retention note (F4), both leg names stated and AC10's retired-name clause resolved (F15), AC2 rebuilt as a state comparison with its named negative (F7), the five refusals restored (F16), the §7 clause (F22), the guard-parity citation (F20), and the fork marker (F11).

**Unit 4** (id `TOOL-aShardedFloor-4`) — **NOT READY, and correctly BLOCKED.** Its §8.1 fork is genuinely the owner's and must reach the README's decision menu (F26). Also owed: the 2-and-3 prerequisite named in the spec (F9), the backlog row's read precedence superseded in the row itself (F17), the five tokens and two header key names spelled (F18), the worktree count re-derived or dropped (F19), the legacy-fallback-expiry fork (brief `:432`) added to §8 (F12's sibling), the four run-gates floor raises (F13), and a decision on whether this unit carries the charter's measured pair (F8).

**The README** — three edits of its own: the authored build order (F9), unit 4's scope in "What this build does" (F10), a re-priced headline once F5 settles the balance, and the owner decision section (F26).
