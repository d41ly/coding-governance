**Serves:** diff-review TOOL-dUnstalledConvoy-26

# Spec audit rev-2 — the three blockers folded, and the fold opened six more in the same organ

**Reviewed range:** `02f8495e...HEAD` (HEAD = `b664339f`, one commit, one file: the rev-2 fold of
`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md`). **ROUND: 1.**

**Review shape:** raw 50 · confirmed 42 · refuted 8 · unverified 0 · precision 0.84. Deduplicated to
18 findings, because eleven lenses landed on two defects — the stamp's missing reader and the
separate counter's missing consumers — from every side each has.

Every citation below was re-read at base rather than taken from the brief or from round 1. Three of
round 1's own figures were re-derived and all three reproduce: 85 manifest legs, `selftests` 42, and
17 `[[exempt_leg]]` rows of which 8 carry `chunk = "selftests"`.

## Verdict: BLOCKED

**Six blockers, five highs, six mediums, one low.**

**What rev-2 got right, and it is most of the document.** B2 is closed properly: S1b derives the
population through `read_descriptors` and states no count, which is the correct instrument rather
than a bigger glob. B3 is closed: §7 is now `GATE_FULL=1 GATE_SELFTESTS=1`, so the unit's evidence is
no longer produced by the legs it disables. M5 is closed by S6, which now says `chunk` is touched by
construction. And S1's `subject` field is the right shape — a declared membership criterion is
checkable in both directions and survives a rename, which no pattern over `.test.sh` ever could.

**What blocks it is that B1 was folded by choosing its worse branch and then not building the
branch.** Round 1 gave two exits: make the on-demand skip suppress the `gate-full-green` stamp, or
keep the stamp writable and teach the push boundary what the stamp now means. rev-2 took the second
and wrote the field — and no scope item, no acceptance criterion and no docs row touches
`.githooks/pre-push`, whose parser reads three keys and whose seven predicates read nothing else. The
field is written and never read. `run-gates.sh:1085-1094`'s own comment says the stamp's
preconditions "are the whole of what makes its name true"; after this unit the record named
`gate-full-green` is earnable by a bar that executed 38 of 85 legs, and the boundary rests on it for
up to ten commits.

**And S4's "OWN counter, NOT `skips`" was folded without naming a single consumer of `skips`.** There
are four, all in the same file: the GREEN summary line, its durable copy in `gate-last-summary.txt`,
the run record's `ran` key, and `chunk_close`'s skipped-verdict predicate. A counter that reaches
none of them makes a switch-off bar print `gates GREEN — 85/85 legs passed` over 38 executed legs and
close the 42-leg `selftests` chunk as `green  (0 ran, 0 failed, 0 skipped, 0 reused)` — which the
comment three lines above that branch calls "the loudest possible green-by-absence, one altitude
above a single leg". rev-1's reuse of `skips` had this right by accident. rev-2's fix breaks it.

**The classification, which is the unit's entire product, is graded by nothing.** AC7 grades that
`subject` is present; AC8 grades that its two spellings agree — both sides authored by the same
builder. An implementation marking all 85 legs `repo` ships the field and changes nothing; one
marking all 85 `kit` switches the whole bar off. Both pass AC1–AC13. Round 1's H5 called this
circularity and asked for a second independent source; the fold reworded the criterion and dropped
the proxy.

---

## Derived populations (measured at `b664339f`, not taken from the brief or from round 1)

| Population | Value | How derived |
|---|---|---|
| Manifest legs | 85 | `len(json.load(open("tools/gate-legs.json")))` |
| Chunk split | selftests 42 · declarations 20 · product 9 · wiring 9 · records 3 · e2e 2 | `Counter(l["chunk"])` |
| Manifest keys in use | `argv` `chunk` `guard` `impure` `name` | set union over all 85 rows |
| Legs already carrying `subject` | 0 | — |
| `[[exempt_leg]]` rows | 17 | parsed from `tools/govkit/registry.toml` |
| …of those, `chunk = "selftests"` | 8 | joined against the manifest |
| `selftests` legs declaring NO guard | 4 | `template size gate selftest` · `method-carriers self-test` · `agent-cap restatement self-test` · `testsuite counts self-test` |

---

# BLOCKERS

## B1 — `gate-full-green` becomes earnable by a partial bar, and S5's mitigation is a field with no reader

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:36-41` (S5),
`:128-130` (AC5), against `.githooks/pre-push:133-196` and `tools/run-gates/run-gates.sh:1095-1105`.

The stamp is written on a five-way conjunction — `fails=0 && skips=0 && reuses=0 && tree_moved=no &&
TREE_CLEAN=yes` (`tools/run-gates/run-gates.sh:1095-1097`). S4 deliberately keeps the new skip OUT of
`skips`, and AC5 requires the stamp to be written anyway on a switch-off run. So a clean-tree
`GATE_FULL=1` run with `GATE_SELFTESTS` unset satisfies all five while every `kit`-subject leg went
unexecuted, and `run-gates.sh:1103-1105` stamps.

The reader does not care what else the record says. `.githooks/pre-push:136-140` awks exactly `sha`,
`fingerprint` and `manifest_blob` out of the file, and predicates 1–7 (`:143-196`) look at nothing
else. Predicate 1 is `[ -n "$rec_sha" ] || force=…`, so a stamp — whatever it declares about a
switch — can only ever produce the CHEAP path. The next push prints `scoped gate`, exports
`GATE_BASE=$rec_sha`, and keeps doing so for up to `GATE_FULL_MAX_LAG=10` commits
(`.githooks/pre-push:129`).

No scope item S1–S11 names `.githooks/pre-push`. F4 mentions it, which is a resolved open question
and not a scope item (see B2). So S5's claim — "a record named `gate-full-green` can never certify a
partial run without saying it was partial" — is true of the file's bytes and false of the decision
the file exists to make. This is round 1's B1 second branch, chosen deliberately and then not built.

**Fix.** Name the consumer. Add a scope item: an eighth forcing predicate in `.githooks/pre-push`
reading the stamp's `selftests` field, where absent-or-`0` FORCES — the direction the hook's own
comment mandates, "EVERY PREDICATE BELOW FORCES … this block can be wrong in one direction only"
(`.githooks/pre-push:117-119`). Add `.githooks/pre-push.test.sh` to the change set in the same
breath: its `stamp()` fixture at `:122-127` writes a three-field record and its control arm 9 asserts
that record chooses SCOPED, so it reds the moment the hook learns the field. The defensible
alternative is round 1's other branch — make `on_demand_skipped == 0` a sixth stamp precondition and
delete the field — but the spec must PICK one and name the file that implements it. Note the
interaction with B2: if gov's pre-push sets the switch, every gov stamp reads `1` and the new
predicate can never fire in this tree, so it needs arming in a fixture rather than in gov's own
record.

**Left-shift gate.** A sixth negative control in `tools/run-gates/run-gates.evidence.test.sh`, beside
the five that already exist there (`:277-342`) precisely so an implementation that forgets one still
reds: an on-demand-skipped leg does not suppress the stamp, a guard-skipped leg still does, and the
stamp carries the switch field. Plus one arm per direction in `.githooks/pre-push.test.sh`, in the
shape arms 9–16 already use.

## B2 — F4 sets the switch in a file this repo does not own: `.githooks/pre-push` is govkit engine payload, shipped verbatim

`…-26.md:163-165` (F4) against `tools/govkit/entries/push-main.kit.toml:19-24`.

F4 resolves the default as "off, like every adopter, with the switch set in this repo's own
pre-push". There is exactly one copy of that file and it is not this repo's own:

```toml
[[files]]
include = [".githooks/pre-push", ".githooks/pre-push.test.sh"]
role = "engine"
root_relative = true
to = "{relpath}"
```

An `engine` write is a byte-for-byte copy of the gov blob with no content templating
(`tools/govkit/govkit.py:2200-2216`). So `export GATE_SELFTESTS=1` placed in gov's hook per F4 lands
verbatim in every target that took `push-main`, on its next `govkit apply` — and every one of them
then runs the whole kit-subject population at its own push boundary. That is the exact run S2
(`:28-30`) identifies as "the push boundary an adopter feels", and it makes §5's perf claim ("an
adopter's full gate loses the kit-subject legs") false at the one invocation that binds. Narrowing,
in fairness: `push-main` is not in the default selection (`tools/run-gates/run-gates.test.sh:533-536`
records that), so the blast radius is adopters of `push-main` — which is also the only population
that has a push-boundary hook at all, i.e. the whole population the claim is about.

The other branch is bad in the other direction and equally unspecced: leave the hook untouched and
F4 is a false claim on the record, gov's own boundary never runs a kit self-test again, and AC6 (H1)
has no mechanism. No S-item and no AC scopes an edit to that file, so an unattended builder picks a
branch by coin-flip.

**Fix.** Decide it in F4 against the shipping fact, citing `tools/govkit/entries/push-main.kit.toml:20`
so the next reader cannot mistake the hook for a local file. Either (a) drop the pre-push half — the
DoD invocation alone carries `GATE_SELFTESTS=1`, and gov then gets exactly an adopter's behaviour,
which is what F4's own last sentence demands — or (b) add a scope item stating that the hook sets it
only under a gov-only condition, and name the tracked file that carries that condition given the hook
itself travels.

**Left-shift gate.** A `tools/govkit/matrix.py` arm: a target installed with `push-main` receives a
`.githooks/pre-push` that does NOT set `GATE_SELFTESTS`. That gates the class — any gov-only
environment decision smuggled into shipped engine payload — rather than this instance.

## B3 — no acceptance criterion grades the VALUE of `subject`; uniform assignments in both directions pass AC1–AC13

`…-26.md:133-147` (AC7, AC8, AC13) against `…-26.md:19-22` (S1) and `:160-162` (F3).

AC7 grades presence ("every leg in `tools/gate-legs.json` carries `subject`"). AC8 grades agreement
between a descriptor and the manifest — two artifacts the same builder writes in the same commit.
AC1–AC4 and AC10 are driven over synthetic fixtures. AC13 runs the bar under
`GATE_FULL=1 GATE_SELFTESTS=1`, which executes everything and is therefore green whatever the
classification is. So:

- an implementation marking all 85 legs `repo` passes every criterion and switches nothing off;
- an implementation marking all 85 `kit` passes every criterion and switches the entire bar off.

Which legs are `kit` is the whole product of this unit and it is the one thing nothing observes. This
is round 1's H5 circularity surviving the rewrite in a new shape: `subject` is still read only from
itself. F3 defers the answer to S1's prose and §3 pins four legs as non-goals; neither is graded.

The ambiguity is not hypothetical at base. Under S1's words — "a `kit`-subject leg tests the kit's own
source" — these are all arguable in both directions: `check-wiring self-test` (guard `.claude/`,
`tools/`), `settings-merge selftest` and `install-prefix self-test` (guard `tools/`),
`run-gates evidence` (guard `tools/`), `dead-path carriers self-test` (guard `tools/`), and
`recall floor arms` (guard includes `memory/`, and its own header says it is keyed on THIS repo's
record ids).

**Fix.** Grade the value against a SECOND independent source, which is what round 1's H5 asked for.
Add an AC asserting the `subject = "kit"` set equals gov's manifest `chunk == "selftests"` set minus
an explicitly listed, reasoned exception set, armed in `tools/govkit/selftest.py`. Restore round 1's
machine-checkable proxy as a second arm — no leg carrying `subject = "kit"` declares a guard pathspec
outside its own `{kit}/`/`{prefix}` home — or state on the record why the proxy is refused and what
replaces it.

**Left-shift gate.** The proxy arm IS the gate, and it is the one that keeps working after this unit:
it reds on any future leg whose declared subject disagrees with the tree it actually reads. Add
beside it a default-bar arm asserting `GATE ok` for `run-gates canary`, `kit/dogfood doc parity`,
`marker contracts` and `review-protocol parity (kit vs dogfood)` — §3 asserts those four stay on the
bar and nothing currently observes it.

## B4 — §3's repo-subject list omits every leg that tests the push boundary, and S1's criterion puts them on the wrong side

`…-26.md:68-70` (§3's OUT list) against `tools/gate-legs.json`,
`tools/govkit/entries/push-main.kit.toml:20-40` and `tools/run-gates/run-gates.gov.test.sh:155-175`.

§3 names four legs as repo-subject and reads as an exhaustive enumeration. Four more are missing, and
they are the arms that verify the surface this very unit weakens:

- **`pre-push self-test`** (`argv: bash .githooks/pre-push.test.sh`, guard
  `['.githooks/','tools/lib/']`). `push-main.kit.toml:20-24` claims `.githooks/pre-push.test.sh` as
  `role = "engine"` kit payload, so by S1's literal criterion this leg tests the kit's own source and
  goes on-demand — while in gov that file IS the live push boundary. AC6 (H1) then depends on a hook
  whose only behavioural self-test this unit switches off.
- **`branch-guard self-test`** (`argv: bash .githooks/pre-commit.test.sh`). Same shape:
  `push-main.kit.toml:29-40` claims `.githooks/pre-commit` as a merged-role write.
- **`push-main self-test`**, guard `['.githooks/','tools/','tools/lib/']`.
- **`run-gates gov canary`** — the genuinely ambiguous one the brief asks about. It is a DISTINCT leg
  from the `run-gates canary` §3 does name. It reads `$ROOT/.githooks/pre-push`
  (`run-gates.gov.test.sh:168-173`), `$ROOT/tools/gate-legs.json` (`:249-258`) and this repo's
  `AGENTS.md` (`:196+`), which makes it `repo` by S1's own words while wearing a self-test name and
  `chunk: selftests`. It is `project-owned` and gov-only, so switching it off RETIRES the check
  rather than moving it.

`run-gates.gov.test.sh:168-175` holds the only two executable statements anywhere that
`.githooks/pre-push` still has a forcing path at all and that `GATE_FULL_MAX_LAG` is a source
constant rather than an environment knob. Its own comment (`:159-162`) names this exact move:
"removing the arm that guards a property in the same commit that weakens the property is gating the
instance rather than the class."

**Fix.** Name all four in §3's OUT list with their reason, and state the sharper criterion S1 is
missing: **a leg whose verdict depends on the ENFORCEMENT SURFACE of this change — `.githooks/`,
`tools/gate-legs.json`, the `gate-full-green` record — is `repo` regardless of whose source ships it,
because it is the check on the thing being weakened.** Record a disposition for `recall floor arms`
and `dead-path carriers self-test` too, so the field is not a coin-flip at build time. Add an AC
observing that the boundary's forcing predicates and the branch guard still fire on a DEFAULT bar.

**Left-shift gate.** Extend B3's proxy arm with the enforcement-surface clause: a leg whose guard
names `.githooks/` or `tools/gate-legs.json` may not declare `subject = "kit"`. That is derivable
from the manifest and reds on the next such leg, not just these four.

## B5 — the separate counter never reaches the pass arithmetic: `gates GREEN — 85/85 legs passed` over 38 executed legs

`…-26.md:32-35` (S4) against `tools/run-gates/run-gates.sh:895`, `:1075`, `:1077`, `:1055-1056`,
`:1125-1126`.

`report_one()` increments `n` for EVERY leg it reports, whatever the verdict (`:895`). Every reported
pass figure is `$((n-skips))`:

- `:1126` — `echo "gates GREEN — $((n-skips))/$((n-skips)) legs passed$skipnote"`
- `:1125` — the same string written to `gate-last-summary.txt`
- `:1075` — `printf 'ran\t%s\n' "$((n-skips))"` in the durable run record, with `skipped` at `:1077`
- `:1055-1056` — `skipnote` is built from `$skips` and `$reuses` alone

S4 mandates a counter that is explicitly NOT `skips`, S5 requires it to stay out of `skips` so the
stamp survives, and no scope item and no AC names a single one of these four sites. AC3 grades the
per-leg verb, the counter's existence and the absent `unchanged vs` tail — all three of which a
broken implementation satisfies while the headline still says 85/85. The runner's own precedent
points the wrong way: `reuses` is also a separate counter and is deliberately NOT subtracted, so an
implementer copying the nearest example produces exactly this.

**Fix.** S4 states the arithmetic: the new tally is subtracted wherever `skips` is — the derived
`ran`, the GREEN and RED summary lines, and `$sfile` — and the run record gains its own key
(`ondemand_skipped`) beside `skipped` rather than folding into it. `skipnote` gains its own clause
naming the on-demand tally separately. Extend AC3 to assert the summary line's numerator equals the
count of legs that actually executed, derived at emission time and never typed.

**Left-shift gate.** An arm in `tools/run-gates/run-gates.evidence.test.sh` asserting the GREEN line's
numerator equals the number of `GATE ok` + `GATE reuse` rows in the same stdout — derived from the
output rather than from a fixture count. That gates every future verb, not this one.

## B6 — the separate counter never reaches `chunk_close`, so a chunk of zero executed legs closes `green`

`…-26.md:32-35` (S4) and `:45-47` (S7) against `tools/run-gates/run-gates.sh:965-976`.

```sh
elif [ "$c_ran" = 0 ] && [ "$c_reuse" = 0 ] && [ "$c_skip" -gt 0 ]; then verdict="skipped"
else verdict="green"; fi
```

`c_skip` is incremented only in `report_one`'s `rc = skip` branch (`:902`). A tally that is none of
those three terms leaves all three at zero and control falls to `else`, printing
`---- chunk selftests: green  (0 ran, 0 failed, 0 skipped, 0 reused)` for the largest chunk in the
manifest — 42 of 85 rows — and writing the same row into `CHUNK_ROLLUP` and `gate-last-summary.txt`.
The comment directly above that branch (`:965-967`) refuses this outcome by name: calling it green
"would be the loudest possible green-by-absence, one altitude above a single leg."

It is worse in an adopter. `tools/govkit/govkit.py:2451` emits `row = {"name": nm, "argv": argv}` and
never a `chunk`, so an emitted manifest parses as one chunk named `default`
(`run-gates.sh:703`, `chunks+=("${ch:-default}")`). A target that adopted only `tools/hooks/` — two
legs, both self-tests — or `tools/pytest-parallel-guardrails/` — one, a self-test — prints
`---- chunk default: green  (0 ran, 0 failed, 0 skipped, 0 reused)` on every bar. This is a distinct
code site and a distinct fix from B5: subtracting in the run-level arithmetic does not widen this
predicate.

**Fix.** S4 names `chunk_close` as a consumer: the on-demand tally is a per-chunk counter too, the
skipped-verdict condition becomes `c_ran = 0 && c_reuse = 0 && (c_skip + c_ondemand) > 0`, and the
new tally joins the four printed in the roll-up and in `CHUNK_ROLLUP`. Add an AC driving the runner
over a fixture whose whole chunk is `kit`-subject with the switch off, asserting that chunk does not
close `green`.

**Left-shift gate.** The same arm, generalised in `tools/run-gates/run-gates.test.sh`: a chunk whose
printed `ran` and `reused` tallies are both zero must not close `green`, asserted over the printed
row rather than over the counters — so it holds for any verb added later.

---

# HIGH

## H1 — AC6 is ambiguous in both directions and is assigned to a harness that structurally cannot drive the hook

`…-26.md:131-132` (AC6) against `.githooks/pre-push:117-119`,
`tools/run-gates/run-gates.test.sh:533-536` and `tools/run-gates/run-gates.gov.test.sh:164-166`.

"`.githooks/pre-push` does not force a full run on the strength of a stamp written with the switch
off" reads two ways: (a) the hook must not REST on such a stamp, i.e. it forces — round 1's B1 fix;
(b) the hook does not force when such a stamp exists, i.e. it accepts it — today's behaviour, making
S5's field decorative. Reading (b) is satisfied by an implementation that changes nothing, and every
predicate in the hook FORCES (`:118-119` says so explicitly, and `:143` forces on the record's
ABSENCE), so the negative phrasing is vacuously true of the unmodified file. There is no owner turn
in this run to disambiguate.

The named observer is wrong by construction. `tools/run-gates/run-gates.test.sh` is the SHIPPED
canary whose contract is that every assertion holds in ANY tree, and `:533-536` records that the gov
pre-push arm was MOVED OUT for exactly that reason — "red on arrival in every default install".
`run-gates.gov.test.sh:164-166` states that the behavioural half "lives in
`.githooks/pre-push.test.sh`, where the hook is really driven". A builder can satisfy AC6 as written
with a grep-for-a-string arm in a harness that never executes the hook — and doing so re-lands the
pin-copied-from-another-corpus defect in the very file that names it.

**Fix.** Rewrite AC6 in the positive and in ONE direction: "a recorded green whose `selftests` field
is absent or `0` makes `.githooks/pre-push` print `FULL gate` and export `GATE_FULL=1`; one whose
field is `1` lets it choose scoped." Observe it in `.githooks/pre-push.test.sh` (leg
`pre-push self-test`), which already stages a stamp at `:122-127`, or in
`tools/run-gates/run-gates.gov.test.sh` — the two places gov-tree facts are allowed to live.

**Left-shift gate.** No new gate needed: `.githooks/pre-push.test.sh` already runs one arm per forcing
predicate with a control proving a scoped run is ever chosen. The gate is that the new predicate joins
that population, and its control arm 9 reds until the fixture learns the field.

## H2 — the deployer has a SECOND closed verb set, unnamed in scope; a new verb refuses every upgrade re-apply

`…-26.md:32-35` (S4) against `tools/run-gates/kit.toml:110-123`, `tools/govkit/govkit.py:1691-1717`,
`:2510-2512` and `:2954-2955`.

S4 names `profile_bar.py`'s closed verb set and stops. The verb vocabulary is declared in three
places across two languages: the runner's `printf`s, `[gate_runner_seed]`'s `observed_*` templates in
`tools/run-gates/kit.toml:114-123`, and the seed emitter's own key list at `govkit.py:2954-2955`.
`read_gate_verdicts` (`:1708-1709`) classifies a target's output by iterating exactly three of those
templates and matching each as a byte-anchored line PREFIX. A line printed with a new verb matches
none, so the leg is ABSENT from the returned map.

The consequence is not a missing row, it is a refused install. On an upgrade re-apply over a target
whose kit legs read green in the baseline pass, `govkit.py:2510-2512` fires
`leg '<n>' was green before this install and is gone after — a leg that vanished is not a leg that
passed`, once per migrated leg, naming the wrong cause. That is a HARDER branch than the
green→skipped one §5's migration row (`:112-114`) is written against. The green-before state is
reachable: `changed()` returns 0 whenever `BASE` is unresolvable (`run-gates.sh:148`), and govkit
drops a guard that matches no tracked path and emits the row UNGUARDED with a printed notice
(`govkit.py:2445-2452`, `:2469-2471`), so unguarded kit legs are a normal adopter shape.

The other direction is silent rather than loud: on a fresh target whose legs are all `kit`,
`before_map` comes back EMPTY, which slips past the DEAD-PROBE refusal at `govkit.py:2042-2048`
because that guard is written `if before_map and not any(...)`. The deployer's own liveness assertion
is bypassed by the shape this unit creates.

Worth noting as evidence the class is live: `observed_reused` is declared in
`tools/run-gates/kit.toml:123` and appears in NEITHER `read_gate_verdicts`'s state loop NOR the seed
emitter's key list at `govkit.py:2954` — the same defect, one instance early.

**Fix.** Add a scope item: `[gate_runner_seed]` gains an `observed_<newverb>` template array,
`GR_REQUIRED` (`govkit.py:1637`) learns it or the spec records why not, the seed emitter's key list at
`:2954` learns it, and `read_gate_verdicts` maps it to a state. Then decide explicitly whether that
state is `skipped` or a fifth state, and teach the after-map check that the transition is EXPECTED
when the emitted row declares `subject = "kit"` (the field is already in scope in `emitted`). State
the verb's byte width too: the four verbs are padded so the NAME starts in one column
(`run-gates.sh:897-907`) and the template head is a literal prefix. Add an AC covering a re-apply over
a target that already had the leg green.

**Left-shift gate.** A `tools/govkit/selftest.py` arm asserting that the runner's emitted verb set and
`[gate_runner_seed]`'s template heads are the SAME set, derived from both sources — a parity gate over
a cross-language catalogue, which is what §7 already demands for every contract duplicated across
layers. Second arm: make the DEAD-PROBE refusal fire on an EMPTY `before_map` for a
`kind = "manifest"` target, so the silent direction stops being silent.

## H3 — AC4 grades only that the verb renders; `profile_bar.py`'s arithmetic then refuses on every switch-off run

`…-26.md:126-127` (AC4) against `tools/run-gates/profile_bar.py:65`, `:361-368`, `:198-212`,
`:429-431`.

The minimal implementation that satisfies AC4 is widening
`VERDICT = re.compile(r"^GATE (ok|skip|FAIL|reuse)\s+(.*)$")` at `:65`. That is not enough, because
the row's arithmetic consumer treats every verb that is not literally `skip` as executed:

```python
executed = [l["sec"] for l in legs if l["verdict"] != "skip" and l["sec"] is not None]
```

A new verb therefore takes the else branch at `:365-366`, picks up each on-demand leg's duration from
the carried-forward timing ledger, inflates `work` and `floor`, and drives wall/ideal below 1.0 —
whereupon `check_packing` (`:198-212`) returns "packing … is below 1.0, which is arithmetically
impossible for a real run" and the profiling verb refuses on every switch-off run. `print_summary`
(`:429-431`) partitions on `verdict != "skip"` as well, so the skipped legs are reported as executed.
AC4 is satisfied by the broken build.

**Fix.** AC4 states both halves: the verb parses, AND on-demand rows are excluded from `executed` at
`:368` and counted with the skipped population at `:429-431`. Make the predicate a named set of
NON-EXECUTING verbs derived once, rather than a second `!= "skip"` comparison, so the next verb cannot
repeat this. Retarget the AC to `tools/run-gates/profile_bar.test.sh` (see M6).

**Left-shift gate.** An arm in `tools/run-gates/profile_bar.test.sh` asserting that every verb the
runner can print appears in the non-executing set or the executing set and in exactly one — derived
from `VERDICT`'s alternation rather than typed. `check_packing` is already reachable from the
self-test by design (`:202-205` says so), so the refusal has a home.

## H4 — the manifest key set is a CLOSED pin, hardcoded twice in the SHIPPED canary; the first `subject` commit reds the bar

`…-26.md:133` (AC7) and `:181` (§10) against `tools/run-gates/run-gates.test.sh:96`, `:106-110`,
`:125-127`, `:55`.

```
 96: KNOWN = {"name", "argv", "guard", "impure", "chunk"}
125: KNOWN = {"name", "argv", "guard", "impure", "chunk"}
```

The first is the arm, which exits 1 listing every stray key; the second is its arming control's
`keyset_probe`. Both are graded against the tree's real manifest through `LEGS_FILE` (`:55`). AC7 puts
`subject` on all 85 rows, so `run-gates canary` prints 85 stray-key rows and exits 1 — and §3
(`:68-70`) deliberately keeps that leg ON the bar as `subject = "repo"`. AC13's
`GATE_FULL=1 GATE_SELFTESTS=1` bar cannot go green until both copies move.

Nothing in S6 (which addresses the runner's `\x1e` wire row, a different format), S8, or the AC set
names either site, and §10's "already carries optional fields and this adds one in the same shape"
actively points a builder away from looking. Round 1's M4 named both `KNOWN` sites and the missing
near-miss control; rev-2 folded neither. Second-order: the arming control at `:116-133` arms only the
`impur` near-miss, so a `subjekt`/`Subject` typo — whose failure direction is silent, since it reads
as "not kit" and leaves the leg running — gets no arming case of its own.

**Fix.** Name both `KNOWN` sites in the change set, derive the set ONCE in that file so the predicate
and its arming control cannot diverge again, and add the `subject` near-miss beside the existing
`impur` one. Rewrite §10's reuse claim to name these two sites rather than assert the shape.

**Left-shift gate.** The single derived `KNOWN` constant IS the gate — one constant consumed by both
the predicate and its control removes the divergence class for every future field.

## H5 — S8's cross-check cannot reach the exempt rows it names, and its count is both wrong and forbidden

`…-26.md:48-51` (S8) and `:136-137` (AC8) against `tools/govkit/govkit.py:862-905` and
`tools/govkit/registry.toml`.

Both directions of the existing cross-check compare NAMES only: `claimed_legs` from descriptors
against the manifest name set (`:871-875`), `exempt_legs` from `registry.toml` against the same set
(`:891-894`), then `manifest - claimed - exempt` (`:900-902`). An `[[exempt_leg]]` row carries `name`
and `why` and nothing else — all 17 rows read at base, none carries a third key — and is by
construction claimed by no descriptor. So "a descriptor and the manifest disagreeing about `subject`"
is UNDEFINED over that population, and AC8's "the check reaches the EXEMPTED legs" is satisfiable by
iterating them and asserting nothing. That is round 1's H4 reworded rather than folded.

The count is wrong in the other direction too. S8 says "the eight legs the descriptors EXEMPT";
`registry.toml` carries 17 exempt rows, of which 8 happen to carry `chunk = "selftests"` — round 1's
subset, not the population. A builder who adds the field to eight rows leaves nine manifest legs whose
`subject` no declaration can ever be checked against, which is the direction S8 says it is closing.
And it is a count of a derived population in prose, four lines after S1b bans exactly that: "No count
of this population appears anywhere in this spec."

The eight include `run-gates gov canary` and `govkit selftest` — the legs asserting that the boundary
can still force and that the deployer's own cross-check is armed.

**Fix.** Delete the number. S8 says `[[exempt_leg]]` gains a REQUIRED `subject` key on every row, and
selfcheck section 7h refuses both (a) a manifest leg whose exempt row declares a different subject and
(b) an exempt row declaring a subject the manifest does not carry. Restate AC8 as two STAGED
mismatches, one per direction, armed in `tools/govkit/selftest.py`.

**Left-shift gate.** The refusal that already exists one line up is the model: `exempt_leg '<nm>' names
a leg that is no longer in the manifest`. Add its sibling for the field, so a row that goes quiet about
`subject` reds the same way a stale exemption does.

---

# MEDIUM

## M1 — S7 pins the pass but not the position inside it, and the literal reading never reaches an unguarded leg

`…-26.md:45-47` (S7) against `tools/run-gates/run-gates.sh:710-715`.

The guard pre-pass is five lines:

```sh
for ((i=0; i<total; i++)); do
  [ -z "${names[$i]}" ] && continue
  [ -z "${guards[$i]}" ] && continue      # :712
  IFS=, read -ra gp <<<"${guards[$i]}"
  changed "${gp[@]}" || printf 'skip' > "$WORK/$i.rc"    # :714
done
```

"The decision sits in the GUARD PRE-PASS" read literally means "add the term to that loop body" — which
never executes for an UNGUARDED leg, because `:712` continues two lines before the sentinel write. Four
`selftests` legs in the live manifest declare no guard at all: `template size gate selftest`,
`method-carriers self-test`, `agent-cap restatement self-test`, `testsuite counts self-test`. They keep
running on every default bar, silently. It is worse in an adopter, where govkit drops a guard that
resolves to no tracked path and emits the row unguarded — so an unguarded kit leg is a NORMAL adopter
shape, and under this reading it keeps running on every adopter bar, which is the exact outcome the
unit exists to remove. AC1 catches it only if its fixture leg happens to be unguarded, which nothing
requires.

**Fix.** S7 states that the on-demand decision is its OWN serial loop, or explicitly precedes the
`[ -z "${guards[$i]}" ]` early-continue at `:712`, and sits ahead of the reuse pass at `:806`. AC1
gains an arm over an UNGUARDED `kit`-subject fixture leg.

**Left-shift gate.** That AC1 arm is the gate. Make the fixture manifest carry both a guarded and an
unguarded kit leg so a single-shape fixture can never certify both paths.

## M2 — no declared meaning for an ABSENT `subject`, and one of the two defaults is silent coverage loss

`…-26.md:42-44` (S6) and `:48-51` (S8) against `tools/run-gates/run-gates.sh:691-693`, `:703` and
`tools/govkit/govkit.py:2451-2470`.

The manifest reader emits an absent field as the empty string (`str(l.get(...) or "")`) and the bash
side chooses the default — there is an established idiom two characters away,
`chunks+=("${ch:-default}")` at `:703`. The spec never says what a row with no `subject` means, in the
runner or in the shipped canary.

The absent-field population is not hypothetical and does not close: gov's own manifest carries zero
`subject` keys today, every already-emitted adopter manifest lacks it until that target re-applies,
and `govkit.py:2451-2470` rewrites only rows the receipt owns, leaving TARGET-AUTHORED rows untouched
forever. If the builder defaults to `kit`, every target-authored leg silently stops running the moment
the runner is upgraded, with nothing red anywhere. If `repo`, nothing breaks. AC7 grades presence in
gov's post-migration manifest only, so neither branch is observed.

The symmetric lesson is already recorded in the canary's own comment (`run-gates.test.sh:92-95`): "an
arm that reds on its ABSENCE is an arm that reds in every adopting tree on arrival."

**Fix.** S6 (or S8) states the default explicitly: an absent or unrecognised `subject` is `repo` — the
leg RUNS — because the other branch fails silently. State whether the "every leg carries it"
requirement is gov-only or shipped in the canary, and say which of the two AC7 grades.

**Left-shift gate.** An arm in `tools/run-gates/run-gates.test.sh` driving the runner over a fixture
manifest with no `subject` key anywhere, asserting every leg executes. That is the adopter-on-arrival
shape and it holds in any tree.

## M3 — the receipt and its drift comparison do not learn the field, so a hand-flip is invisible

`…-26.md:52-54` (S9) against `tools/govkit/govkit.py:2457-2458` and `:2466-2469`.

The drift comparison is exactly `prev.get("argv") != argv or prev.get("guard", []) != guards`, and the
`emitted` receipt entry records name/kit/argv/guard/guard_dropped/history_depth. `subject` appears in
neither. That comparison exists specifically for the class its own message names — "ownership of the
NAME is not ownership of the ROW" — so adding a field that DECIDES EXECUTION outside both the receipt
and the comparison opens a tamper channel of exactly the shape the check was built to close: one word
edited in a target's `gate-legs.json` turns off a govkit-installed gate (the memory-tree hygiene gate,
the codebase-map coverage gate) and the next apply silently overwrites the row without reporting that
it had been changed. The receipt then records a row the deployer did not fully emit. Round 1's M3 named
all three sites; rev-2 folded the emission one.

**Fix.** S9 covers all three: the emitted row, the `emitted` receipt entry at `:2466-2469`, and the
drift comparison's field list at `:2458`. AC9 asserts the receipt carries the field, not only the
manifest.

**Left-shift gate.** A `tools/govkit/matrix.py` arm that hand-flips `subject` in an installed target and
expects a REPORTED drift rather than a silent replacement — the same shape the argv/guard arms already
use, so the gate is one row in an existing table.

## M4 — the zero-leg refusal has no scope item, and its condition is stated over the manifest while its observable is a run

`…-26.md:103-105` (§5) and `:140-141` (AC10) against `tools/run-gates/run-gates.sh:1126` and the exit
paths at `:25`, `:65`, `:569`, `:696`.

No scope item S1–S11 builds a zero-leg refusal, and the runner has none: its only exit-2 paths are a
missing repo, python, scratch dir or unparseable manifest, and an all-skipped bar prints
`gates GREEN — 0/0 legs passed (85 skipped)` and exits 0 today. An acceptance criterion with no scope
item is built by improvisation, and the two natural improvisations differ:

- keyed on the on-demand tally alone, the identical all-guard-skipped zero-leg green stays green — one
  zero-executed bar refuses and an identical one reports green, which is a worse signal than either
  rule alone;
- keyed on the run outcome, every legitimate diff-scoped run in which no guard fired goes red.

And the condition as written is a MANIFEST property ("a manifest whose every leg is `kit`-subject")
while the sentence beside it says the observable is a run outcome, so the MIXED route — 84 kit legs
plus one guarded repo leg whose guard does not fire — meets neither. Round 1's M1 asked for the
condition to be stated over the RUN and for an explicit ruling on the existing all-guard-skipped green;
rev-2 moved the observable and left the condition, and answered neither.

Related and still unaddressed from round 1 (M2): `tools/hooks/kit.toml` declares exactly two legs, both
self-tests, and `tools/pytest-parallel-guardrails/kit.toml` exactly one. A target adopting either gets
a manifest whose every row is `kit`, so under §5 its bar refuses on every invocation — permanently,
where a guard at least fires situationally — with nothing in the refusal path naming
`GATE_SELFTESTS=1`.

**Fix.** Add the scope item. State the predicate over the RUN and over non-sentinel rows — zero executed
AND zero reused is a refusal whatever mixture produced it — say explicitly whether today's
all-guard-skipped green becomes a refusal too, and require the refusal message to name
`GATE_SELFTESTS=1`. Restate AC10 against that and add the mixed-source negative control.

**Left-shift gate.** `tools/run-gates/run-gates.test.sh` arms for all three zero-leg routes — guards
only, switch only, mixed — so no future mechanism can reach the state through an unguarded door.

## M5 — `govkit apply` refuses the upgrade re-apply, and §5 delegates the fix to a scope item that does not contain it

`…-26.md:111-114` (§5 migration/rollback) against `…-26.md:55-56` (S10),
`tools/govkit/govkit.py:2503-2512`, and `tools/govkit/matrix.py:222-240`.

§5 says the refusal "is named in S10 rather than discovered". S10 is entirely about the install summary
and says nothing about migration — and the summary is printed by an apply that has already refused:
`r.problems` non-empty means the manifest write is skipped (`:2472`) and `r.emit()` returns a failed
install. Round 1's H7 asked for a code fix; rev-2 downgraded it to a doc row and then pointed the row
at the wrong item. (Which branch fires is H2's subject: `green → skipped` at `:2508` if the new verb is
mapped, `green → gone` at `:2510` if it is not. Both fail.)

The declared observer cannot see it either: `matrix.py:228-232` builds a fresh `git init` scratch repo
with no `[gate_runner]`, so `before_map` is empty and the before/after join never executes on that path.
A defect named in a prose row, with no scope item and no reachable arm, ships.

**Fix.** Either scope the code fix — the after-map check treats the transition as EXPECTED when the
emitted row declares `subject = "kit"`, the field already being in scope in `emitted` — or state on the
record that upgrades require a named manual step, and say which. Add a matrix shape that applies TWICE,
the second time over an already-adopted target.

**Left-shift gate.** That double-apply matrix shape. It is the upgrade path, and the matrix currently
covers it for NO field, so the gate pays for itself beyond this unit.

## M6 — AC4, AC5 and AC6 all name an observer that does not hold the machinery they grade

`…-26.md:126-132` against measured reference counts at base.

| AC | Names as observer | Where the machinery actually is |
|---|---|---|
| AC4 (`profile_bar.py`) | `run-gates.test.sh` — 0 `profile_bar` references | `tools/run-gates/profile_bar.test.sh` — 24 |
| AC5 (`gate-full-green`) | `run-gates.test.sh` — 0 `gate-full-green` references | `tools/run-gates/run-gates.evidence.test.sh` — 13 |
| AC6 (`.githooks/pre-push`) | `run-gates.test.sh` — the arm was MOVED OUT (`:533-536`) | `.githooks/pre-push.test.sh` |

An AC pointed at a harness that cannot observe the artifact is satisfied by an arm written anywhere in
the named file. The stamp's five preconditions each have their own negative control in the evidence
harness BY DESIGN — `run-gates.sh:1085-1094` says so — and one of them is live at
`run-gates.evidence.test.sh:298-304`, "full-green stamped despite a skipped leg", which pins today's
meaning of the stamp that S5 changes. That file is named nowhere in the spec, so a builder meets it as
a red rather than as a reconciliation.

**Fix.** Retarget AC4 to `tools/run-gates/profile_bar.test.sh`, AC5 to
`tools/run-gates/run-gates.evidence.test.sh`, AC6 to `.githooks/pre-push.test.sh`, and add
`tools/run-gates/run-gates.evidence.test.sh:298-304` to the change set with what it must assert after
the change.

**Left-shift gate.** None worth building — this is a documented check on spec authoring, not a code
class. The compensating discipline is that every AC names the harness that already references the
artifact, which is grep-checkable by the author in one command.

---

# LOW

## L1 — `run_all_env = "GATE_FULL=1"` becomes a false declaration the deployer seeds into every adopter

`…-26.md:115-116` (§5 help/docs) and `:158-159` (F2) against `tools/run-gates/kit.toml:105-108`,
`tools/govkit/govkit.py:1637`, `:1662`, `:2954`.

```toml
# The environment that makes a run TOTAL. Required by the deployer for a complete `manifest`
# promotion; a partial one is refused rather than silently accepted.
run_all_env = "GATE_FULL=1"
```

F2 rules that `GATE_FULL` does NOT unlock kit-subject legs, so that sentence goes false. `GR_REQUIRED`
lists the key and `:1662` refuses a promotion missing it — but checks PRESENCE only, never truth — and
`:2954` copies the claim verbatim into every target's `deploy.toml`. §5's help/docs row names govkit's
install summary, `tools/run-gates/README.md` and `AGENTS.md`, not this file, and no scope item touches
it. Round 1's L1, unaddressed. Rated low because grep finds no execution site for the value: this is
declaration rot that travels, not legs going unrun.

**Fix.** Set `run_all_env = "GATE_FULL=1 GATE_SELFTESTS=1"` in the seed, or rewrite the comment to say
what "total" now excludes and why. Add `tools/run-gates/kit.toml` to §5's help/docs row either way.

**Left-shift gate.** None worth building — a truth check on `run_all_env` would have to run a target's
whole bar twice. Documented check: the descriptor comment is the record, and govkit's existing presence
check stays as it is.

---

## Round-1 findings: what rev-2 folded, and what it did not

| Round 1 | rev-2 disposition | Verdict |
|---|---|---|
| B1 stamp/`skips` | Branch chosen (own counter + switch in stamp), reader never built | **Oversight** → B1, B5, B6 |
| B2 population from one descriptor root | S1b derives through `read_descriptors`, no count | Closed |
| B3 DoD skips its own evidence | §7 is `GATE_FULL=1 GATE_SELFTESTS=1` | Closed |
| H1 repo-subject legs swept in, no criterion | Criterion declared (S1); it does not resolve the `.githooks/` legs or `run-gates gov canary`, and the machine-checkable proxy was dropped | **Oversight** → B3, B4 |
| H2 wrong seam named | S7 names the guard pre-pass; position within it unstated | **Oversight** → M1 |
| H3 verb unchosen, downstream reader breaks | S4 names `profile_bar.py` only — one of three verb sites and none of four counter consumers | **Oversight** → H2, H3, B5, B6 |
| H4 cross-check cannot reach exempt legs | Reworded into S8; `[[exempt_leg]]` still gains no field | **Oversight** → H5 |
| H5 AC6 circular — population read from itself | Not addressed; AC7/AC8 grade presence and agreement | **Oversight** → B3 |
| H6 AC9 unobservable, prose count | S1b bans counts; S8 writes one four lines later | **Oversight** → H5 |
| H7 `govkit apply` refuses the upgrade | Downgraded to a §5 prose row pointing at S10, which does not contain it | **Oversight** → M5 |
| H8 nothing durable records the switch | Half folded: the stamp records it; the run header/verdict keys are not in scope and the stamp field has no reader | **Partial** → B1, B5 |
| M1 empty-population refusal | Observable moved to a run outcome; the CONDITION left over the manifest, still no scope item, the explicit ruling still unmade | **Partial** → M4 |
| M2 two kits un-adoptable standalone | Not addressed; §5's refusal rule makes it permanent rather than situational | **Oversight** → noted in M4 |
| M3 emitter drops every field but three | Emission half folded (S9); receipt and drift comparison dropped | **Partial** → M3 |
| M4 `KNOWN` pinned twice | Not addressed; §10 still asserts the shape and names no site | **Oversight** → H4 |
| M5 `chunk` is the last wire field | S6 says it is touched by construction | Closed |
| L1 `run_all_env` falsified | Not addressed | **Oversight** → L1 |

Four closed, three partial, ten not folded. No round-1 finding was declined ON THE RECORD — there is no
sentence anywhere in rev-2 accepting an omission with a reason, which is what makes the ten oversights
rather than decisions.

## New defects rev-2 introduces that rev-1 did not have

Two, and both are the fold's own doing rather than inherited:

- **B5 and B6 are created by the fix to B1.** rev-1 reused `skips`, which was wrong for the stamp and
  right for the arithmetic and the chunk verdict. Moving to a separate counter fixes the first and
  breaks the other two, and no scope item follows the counter to its consumers.
- **B4's `.githooks/` classification is created by S1.** rev-1 had no criterion, so nobody could have
  applied one to `pre-push self-test`. S1 supplies a criterion that, read literally against
  `push-main.kit.toml`, puts gov's push- and commit-boundary self-tests on the on-demand side.

H5's count in S8 is a third, smaller one: rev-1 had no such sentence, and S1b — written in the same
revision — forbids it.

## Is rev-2 buildable end to end?

No, and the trace stops in four places. Reader emission (`run-gates.sh:691-693`) and the six-variable
read (`:701`) are fine — S6 handles them. The guard pre-pass reaches only guarded legs (M1). The
dispatch loop and the reporting pass are fine: `report_one` is still called for a sentinel-decided leg,
so result indices stay 1:1 and there is no "(no result)" hole — S7's stated reason is correct. Then it
fails: the derived pass arithmetic (B5), the chunk verdict (B6), `profile_bar.py`'s `executed`
predicate (H3), and the deployer's template set (H2). The drop sentinel and the timing cache survive
untouched — the cache is keyed on leg NAME by the python side, which an added field does not disturb.

## Recommendation

Return to rev-3. The mechanism is still right and S1 is still the right instrument; what is missing is
that two of the three folds were written as one-line edits to a document when they were changes to a
system. Priority order:

1. **Follow the counter to every consumer of `skips`** (B5, B6). Four sites, one file, and the current
   spec names none of them.
2. **Name the stamp's READER or delete the field** (B1, H1). Either branch is defensible; a written
   field with no consumer is not.
3. **Decide `.githooks/pre-push`'s ownership before writing another sentence about it** (B2, B4). It is
   shipped engine payload, and both F4 and AC6 are written as if it were local.
4. **Grade the classification against something other than itself** (B3), and let the exempt rows carry
   the field like every other row (H5).

Nothing here argues against the owner's ruling, and nothing here argues against `subject` as the
instrument. It argues that switching legs off changes what a green bar MEANS, and that every artifact
which reads that meaning — the stamp, the hook, the summary line, the chunk verdict, the deployer's
before/after join — has to be named in the scope that changes it.
