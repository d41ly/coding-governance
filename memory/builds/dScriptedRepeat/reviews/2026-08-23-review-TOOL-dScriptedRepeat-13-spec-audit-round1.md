**Serves:** diff-review TOOL-dScriptedRepeat-13 TOOL-dScriptedRepeat-14 TOOL-dScriptedRepeat-15

# dScriptedRepeat — spec audit of units 13, 14 and 15, round 1

**Range:** `abd0f026...23ddfb72` — three new spec documents plus the regenerated build index in
`memory/builds/dScriptedRepeat/README.md`. 317 insertions, 3 deletions. **No product code moved in
this range**, so every finding below is a defect in a specification, not in an implementation.
**ROUND 1.**

**Review shape:** raw 44 · confirmed 35 · refuted 9 · unverified 0 · precision 0.80. The 35 confirmed
findings collapse to **22 distinct defects**. Six clusters were filed independently by two to four
lenses each; that corroboration is recorded per defect rather than counted twice. Every mechanism
below was re-reproduced against the working tree before it was written down.

**What was audited.** Not "is this code correct" — there is no code. The questions were the spec
ones: is the goal the real problem, is the scope the right cut, are the non-goals load-bearing, are
the acceptance criteria observable, would passing them mean the unit is done, and are the resolved
forks resolved on evidence rather than convenience.

## Verdict: BLOCKED

Three blockers, six highs, eleven mediums, two lows.

**The grading rule, stated so you can disagree with it.** A spec finding is a BLOCKER when building
the unit as written would produce the defect the unit exists to prevent, or when a load-bearing claim
in the spec is false about the tree. Everything else is graded as its strongest surviving filing,
except HIGH 6, where I overrode three lower filings upward and say why at that entry.

**The standing pattern of this build held into the spec layer.** Six review rounds each found the
previous round's fix reintroducing its own defect one level up. These three specs are written against
that history — they name the classes, they quote them, unit 15 makes profiling the first build step
because the cost model has been wrong twice. And all three then commit the same classes in their
acceptance criteria. Nine of the twenty-two defects below are one shape: **an acceptance criterion
whose subject is empty, unmeasured, or unreachable, guarding the exact property the unit promises.**

---

## Read this first — the cost model, all four numbers

Unit 15's whole case rests on S1's corrected arithmetic, and S1 is presented under the heading
"What IS measured". Four numbers live in that bullet and its neighbours. **One is a quotient
presented as a measurement, one is contradicted by this build's own ledger by 42%, one does not
reproduce on this node, and one was taken on a different population from the one it is used to
size.** Details are BLOCKER 3, MEDIUM 2 and LOW 1; the summary is here because the spec asks to be
judged on these numbers and a reader who takes only one thing should take this.

| Claim in spec 15 | Where | Status |
|---|---|---|
| 243 invocations × ~13.2 s each | S1, line 20 | 13.2 = 3199 ÷ 243. An identity, not a reading. |
| 3199 s total | S1, line 21 | The build's own ledger records the same suite as 1565.4 + 692.6 = 2258 s. 941 s unreconciled. |
| a reset is 59 ms | S1, line 19 | Replayed on this node: ~120–150 ms for the same four spawns, in a one-file repo. |
| `--only`/`--skip` "halves an invocation" | S2, line 27 | Measured out-of-fixture on a leg that hits the network. In-fixture is unmeasured; on the real repo `--skip 28` keeps ~60%, not 50%. |

The conclusions mostly survive — resets are still not the dominant term, invocations still are — but
**S1 is the first build step precisely because two prior claims were wrong, and it ships three more
unsound ones.** That is the same defect one level up, for the seventh time on this build.

---

# BLOCKERS

## BLOCKER 1 — spec 13 is written against the wrong file: `GITLS`, the playbook enumeration and the `records` parse are all in `check-playbook.sh`, and check 11 is not

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-13.md:18`** (S1),
**`:24`** (S3), **`:43`** (§4), **`:96`** (§10). Filed independently by four lenses.

S1 says "the leg already parses every tracked playbook's declaration block, so the roots are derivable
where it stands; nothing new is declared". §4 says the widened pass "gains a second pass over
`GITLS "$rr/*.md"` for each declared root `$rr`, which is the same enumeration the census reader
already performs". §10 says "Nothing new is introduced". All three are false about the file every
acceptance criterion names.

Verified in the tree:

- Check 11 is `tools/unattended/check-unattended.sh:960` — the only `fail 11` in a checker.
- `GITLS()` is defined at `tools/unattended/check-playbook.sh:105` and used only there (`:127`,
  `:375`, `:459`, `:479` — including the exact `GITLS "$rr/*.md"` idiom §4 quotes).
  `grep -n GITLS tools/unattended/check-unattended.sh` returns **nothing**.
- `declared_scalar()` is defined in exactly two files, `tools/unattended/unattended.sh:2917` and
  `tools/unattended/check-playbook.sh:206`. `rr=$(declared_scalar "$body" records)` is
  `check-playbook.sh:357`.
- `check-unattended.sh` defines eight top-level functions — `fail`, `region`, `core_of`, `fact_of`,
  `phase_of`, `report`, `observe_remote`, `is_published` — and touches `declared_scalar` only to
  extract its **text** for check 28's byte comparison (`:1841-1842`), inside the block gated by
  `[ "$SCOPE" != skip28 ]` at `:1834`, some 880 lines below check 11. It enumerates no playbooks.
- `lib-unattended.sh` supplies neither: its exports are `GIT`, `id_rows`, `id_in`, `normpath`,
  `covers`, `overlaps`, `is_repo_root`, `pass_commit`, `next_anchor`.
- The two files are two different merge-bar legs — `unattended kit gate` and `playbook validity gate`
  in `tools/gate-legs.json` — and each kit script installs standalone and cannot import the other.

So building this unit where the spec puts it forces a **third inlined copy** of `declared_scalar`
plus a new playbook enumeration inside `check-unattended.sh`. Check 28's parser comparison is strictly
pairwise — `$DRIVER` against `$HERE/check-playbook.sh`, refusals at `:2107-2116` — so the third copy
would be **unpoliced**. That is the two-answers-to-one-question class S3 exists to forbid, created
inside the security check written to close a hole, and it is exactly the desync check 28 was built
after (round 3's `piece_checks` third spelling without the comment strip).

**Fix.** Decide the location in §4 and re-point the ACs at it.
(a) Move the widened bypass scan into `check-playbook.sh`, where the census, `GITLS`, `$PLAYBOOKS`
and the `records` parse already sit; restate AC1/AC2/AC5 against `bash tools/unattended/check-playbook.sh`
and add a scope item for reading `BYPASS_BAN` there — that leg reads `.unattended.conf` only for
`PLAYBOOK_GLOB` today. Or
(b) keep it in check 11 and add explicit scope items for inlining `declared_scalar` + `GITLS` into
`check-unattended.sh` **and** widening check 28's comparison from a pair to the derived kit-source
set — `KIT_SH` is already derived at `:2124`, so the population exists. Then delete §10's "Nothing new
is introduced", because that is three new things.

**Left-shift gate.** Make check 28's parser comparison derive its file population from `KIT_SH`
instead of naming two paths, and stage a third divergent copy to observe it RED. A pairwise
comparison over a population that can grow is the instance-gate shape round 5 already filed once.

## BLOCKER 2 — spec 15's scoping blinds the 109 negative arms, and neither AC2 nor AC4 can see it

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-15.md:29`** (S3),
**`:32`** (S4), **`:72`** (AC2), **`:79`** (AC4). Filed independently by four lenses.

The unit's entire promise is S4: "a scoped invocation must run the same arms, not fewer". The
protection it names is the executed-assertion count. That counter is structurally incapable of moving
for the change being specced.

`tools/unattended/check-unattended.test.sh:50-52`:

```
hit()  { n=$((n+1)); grep -qF -- "$2" <<<"$1" || { echo "FAIL missing: $2"; st=1; }; }
miss() { n=$((n+1)); if grep -qF -- "$2" <<<"$1"; then echo "FAIL unexpected: $2"; st=1; fi; }
same() { n=$((n+1)); [ "$2" = "$3" ] || { echo "FAIL $1: expected [$3], got [$2]"; st=1; }; }
```

`n` increments **before** any inspection of what the run emitted, and `mutate` increments at `:195`.
The tail at `:2466` compares only `n` against `FLOOR_ASSERTIONS=392` (`:2445`), `FLOOR_SHARD_1=83`
and `FLOOR_SHARD_2=309`. §4 changes only `run()`'s argv. Assertion **sites** executed cannot change,
so AC2's ">= its count at `abd0f026`" is satisfied exactly, by construction, whatever the scoping does.

What that leaves unguarded is the negative direction — the whole population that fails silently. The
suite carries **87 `miss` arms and 22 `same` arms**, several of the latter asserting empty output
(`:234`, `:493`, `:505`, `:532`, `:775`, `:803`, `:970`, `:1311`, `:1357`, `:1370`, `:1447`,
`:1457`). Scope an arm away from the region its expectation belongs to and the string is absent
**because the check never ran** — the arm goes vacuously green, `n` does not move, every floor holds.
AC4 stages one break per direction and expects RED, i.e. it arms only the `hit` direction, which is
the half that already fails loudly.

The concrete case is `:2315-2317`:

```
same "check 23 reports without failing the leg, exit code" "$rc" "0"
...
miss "$out" "FAILED"
```

Its in-source claim is that the **whole leg** is green on that fixture — and the fixture copies
`check-playbook.sh`, `unattended.sh` and `PLAYBOOK-TEMPLATE.template.md` into the scratch repo
specifically so check 28 runs (`:60-66`), so that absence assertion covers check 28 today. Under S3's
rule it asserts no check-28 message and takes `--skip 28`, making both `rc=0` and the absence of
`FAILED` true by construction over the skipped region. 109 assertions stop covering check 28 at once,
and the comment above them becomes broader than what they check.

This is the build's own recorded "fixture that passes by finding nothing" class, reintroduced one
level up, in the unit whose stated risk (§5, line 62) is "a scoped invocation silently running FEWER
arms, which S4's floors catch". They cannot catch it.

**Fix.** Three changes, and the third is the one that matters.

1. Classify on what the arm asserts about **absence**, not on the message it names. Any arm carrying
   a `miss` or an exit-code `same` keeps the full unscoped run, or takes an explicit paired
   `--only 28` companion run.
2. Delete "its `FLOOR_ASSERTIONS` is re-measured to the new count" from AC2. A floor derived from its
   own subject is not a floor.
3. Replace AC2 with a criterion the scoping can fail. Either (a) a preflight in the suite that runs
   each `miss`/`same` needle against the unscoped output of a deliberately broken fixture and reds on
   any needle the arm's declared scope makes unreachable — class-level, not AC4's one-of-each sample;
   or (b) make `run()` assert coverage: the checker emits a scope banner, `run()` reds when an arm's
   expected string belongs to a region the banner says was skipped, and an AC stages a deliberately
   mis-scoped arm and observes it RED.

**Left-shift gate.** A gotcha class plus a suite-level rule: **an absence assertion is evidence only
if the thing that could have emitted the string actually ran.** Mechanise it as the preflight above so
it binds every future arm, not the 109 that exist today.

## BLOCKER 3 — spec 15's "What IS measured" is a quotient, and its divisor is contradicted by this build's own ledger by 941 s

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-15.md:20`**. Two lenses.

S1 corrects two wrong cost claims and then writes: "What IS measured: **243 checker invocations at
~13.2 s each inside the fixture** (3199 s ÷ 243), which is essentially the whole cost."

13.2 is literally `3199 / 243 = 13.16`. Dividing the total by the count and then attributing the
total to the count is an arithmetic identity — it cannot be falsified, and it is presented under a
heading claiming it was measured. `3199` appears nowhere in the repo outside this spec line.

The divisor is contradicted three ways.

- **This build's own ledger record.**
  `memory/builds/dScriptedRepeat/build/2026-08-23-build-TOOL-dScriptedRepeat-5-bar-cost-measurement.md`
  lists `unattended gate selftest shard B` at 1565.4 s and `unattended gate selftest` (shard A) at
  692.6 s = **2258 s**. Both were `--shard 1/2` and `2/2` of this same script (confirmed at
  `f5f4732a~1:tools/gate-legs.json`), and the suite's own tail pins the shards as a clean partition
  (405 = 86 + 319, "no prologue arm"). The sharded pair ran under bar concurrency and should be
  *slower*, not 941 s faster.
- **The checker's own header**, `tools/unattended/check-unattended.sh:61`, records a direct
  measurement of 22.7 s whole and 11.7 s with the check-28 region cut off, node d, same day.
- **The bar-cost record's own prose**: "One check run was 13 s **before** the round-6 gate rewrite."
  13 s is the pre-rewrite number, not the current one.

Per-invocation is somewhere in 8–13 s under the sharded reading and ~13 s under the unsharded one,
and the reduction AC1's 900 s ceiling demands is 2.5× or 3.6× depending on which total is real. The
same record's own model — "roughly eighty arms, 80 × 22 s" — is wrong by 3× against the 246
invocation sites the spec counted, so the record and the spec already disagree about the suite's
shape before anything is built.

**Fix.** Before the profile: re-run the suite unsharded and as `--shard 1/2` + `--shard 2/2` on a
quiescent tree at one commit, and record all three wall readings side by side. State in S1 which
total AC1 is judged against and why the other differs. Present 13.2 s as "derived average, to be
replaced by the S1 profile", not as "What IS measured". Measure the per-arm non-checker git work
alongside one invocation — the suite makes 101 `sed -i` and 263 bare `git` calls outside `reset_tree`,
and none of it is in the model. Fold the record's stale "80 arms × 22 s" correction into AC3.

**Left-shift gate.** Extend this repo's existing "no count of a derived population is written in
prose" rule to build records: a cost figure that is a quotient of two other figures in the same record
is flagged as derived, not measured. Cheaper and stronger — require every number in a bar-cost record
to carry the command that produced it, and red on one that does not.

---

# HIGHS

## HIGH 1 — spec 15's AC5 compares the empty string to the empty string

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-15.md:83`**. Two lenses.

AC5: "`bash tools/unattended/check-unattended.sh` with no argument is byte-identical in output to
today's, so the merge-bar leg is untouched by this unit."

Measured on this worktree: that command exits 0 and emits **0 bytes**. The leg's own contract at
`check-unattended.sh:12` is "Exit 0 + no output = clean", and the REPORT channel is off by default.
So AC5's verification procedure is diffing empty against empty, and it passes identically for a
refactor that disarmed every check — which is the failure it names as its own purpose. §4 line 51 and
F1 both explicitly contemplate editing `check-unattended.sh` itself, so this is not a theoretical
exposure.

The suite's 209 `hit` arms would catch a wholesale disarm through other paths, which is why this is
high rather than a blocker. But the AC written to guard the merge-bar leg is unfalsifiable as written.

**Fix.** Assert byte-identity over a RED corpus. The control already exists in this unit's backlog
row: `--only 28` + `--skip 28` reproduce the full run's failure count, 0 + 41 = 41. Make AC5 "the
unscoped run over a fixture carrying one staged break in the 1–27 region and one in the 28 region
emits a byte-identical failure set and exit status before and after", and record the fixture.

**Left-shift gate.** A documented review check, since it cannot be gated generically: **an AC whose
observable is "identical output" must name the non-empty output it compares.** Add it to the memory
kit's spec-template AC guidance.

## HIGH 2 — spec 15's AC1 ceiling is unreachable by the spec's own arithmetic, and no fallback is declared

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-15.md:69`**.

AC1 demands a reading under the declared 900 s ceiling. S3 is the only concrete lever in scope, and it
explicitly leaves arms asserting both regions on the full run (`:31`).

Measured on this worktree, warm: `check-unattended.sh` whole 30.8 s, `--only 28` 10.0 s (32%),
`--skip 28` 19.0 s (62%). Even a favourable arm mix blends to roughly 46–51% of the total — about
1500–1900 s, i.e. **1.7–2.1× over the ceiling**. Reaching 900 s therefore depends entirely on S2's
first candidate, subprocess count inside the checker, which S1 has by construction not measured yet.

Sibling unit 14 does this properly: S5 declares an honest fallback for a predicate that may not
survive contact with the corpus. Unit 15 declares none, and AC1 as written forecloses the outcome the
runner itself sanctions — `run-unattended-gates.sh:65-66`, "Raising one is fine; raising one silently
is not." If the profile finds no 3.5× lever, this unit has no defined done state and the compensating
check for seven removed merge-bar legs stays unaffordable.

**Fix.** Put the residual arithmetic in S1 so the gap is visible before building, and add the
14-shaped fallback: either the checker-level fix in S2 becomes mandatory rather than conditional, or
the unit may re-declare the ceiling with the measurement recorded beside it — and say which outcome
AC1 accepts.

**Left-shift gate.** A spec-template rule: **a unit whose acceptance criterion is a number someone
else declared must state the arithmetic from its own scope to that number, or declare the fallback.**
Weakly gateable as a fold-checklist item; the arithmetic itself is a human read.

## HIGH 3 — spec 13's S3 ("the derivation is LIVE, not a second copy") has no acceptance criterion that can fail

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-13.md:24`** (S3),
**`:71`** (AC5). Two lenses.

S3 is the scope item the spec itself flags as the one that must not become two answers to one
question. AC5 is its only guard: "a fixture whose playbook declares a root reachable only through the
declaration block is covered by `check-unattended.sh`, proving the derivation is live rather than a
path convention re-implemented."

AC5 tests **behaviour** — the root is reached through the declaration block rather than a path glob.
Any independently written declaration-block reader satisfies it identically, **including a freshly
inlined third copy of `declared_scalar`**. That is precisely the defect S3 names and precisely what
check 28 exists to prevent, and check 28's byte comparison is pairwise (`$DRIVER` vs
`$HERE/check-playbook.sh`, `:2107-2116`) so it never sees a third definition. Check 28a's call-site
rule would police the new call site's refusal handling; nothing compares the new definition's bytes.

So the AC is green under both the good implementation and the bad one. This is distinct from BLOCKER
1: even with S1's placement corrected, S3 would still have no failing case.

**Fix.** Assert sharing, not liveness. Either extend check 28's byte comparison to every kit script
that inlines the parser (derived from `KIT_SH`, with a staged divergence observed RED), or add an arm
that feeds one fixture playbook to check 11 and to the census reader and reds unless the two return an
identical root list.

**Left-shift gate.** The `KIT_SH`-derived parser comparison from BLOCKER 1's left-shift covers this
one too — one gate, two findings.

## HIGH 4 — spec 13's acceptance criteria are armed in a suite whose fixture contains no playbook at all

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-13.md:64`** (AC1, and
AC2/AC4/AC5 alongside it).

AC1, AC2, AC4 and AC5 are all armed in `tools/unattended/check-unattended.test.sh`. That suite's
prologue (`:60-66`) copies `check-unattended.sh`, `unattended.sh`, `lib-unattended.sh`,
`PROTOCOL.template.md`, `SKILL.template.md`, `check-playbook.sh`, `PLAYBOOK-TEMPLATE.template.md` and
`.unattended.conf.example`. It never copies `playbook.fixture.md`, `fixture-pieces/` or
`fixture-records/` — those are copied only by `check-playbook.test.sh:42-47`. And
`check-playbook.sh`'s population derivation explicitly skips the shipped template.

So the fixture tree carries **zero playbooks with a declaration block**. The only `playbook:` the
suite ever writes is a build-README pointer at `:1593` (`playbook: content/pb.md`) with no such file
on disk. The widened population is empty there.

- AC4's negative half — "a playbook declaring no `records` root contributes no population" — grades
  nothing.
- The suite's opening green control, `same "a conforming tree prints nothing" "$out" ""` at `:234`,
  exercises the widened pass over an empty population and reports clean.
- AC1/AC2/AC5 require fixture scaffolding that no scope item names, while §10 asserts nothing new is
  needed.

**Fix.** Add a scope item: `check-unattended.test.sh` grows a tracked playbook with a declaration
block and a tracked evidence record under its declared root, committed into the scratch repo. Restate
AC5's fixture against it explicitly.

**Left-shift gate.** A liveness assertion in the shape `check-playbook.sh:100` already uses — the
widened pass reports its graded population and the suite reds if a fixture meant to exercise it grades
zero. See MEDIUM 6; one gate closes both.

## HIGH 5 — spec 14's F2 resolves the tolerance by citing a GATEABLE precedent, which contradicts S3's REPORT ONLY

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-14.md:91`** (F2), against
**`:21`** (S3).

F2: "a pin to drain, matching `non_terminal_specs_cited_by_product_source` and its siblings."

That signal is `"gateable": True` at `tools/drift-audit/drift_report.py:371`. In that file the two
mechanisms are mutually exclusive:

- the renderer branches on `s["gateable"]` and only a gateable signal is compared against `pin`
  (`:954-957`); a non-gateable one compares against `s["tolerance"]` and prints "out of tolerance
  (report only)";
- `--check`'s `over` and `dead` lists both filter on `gateable` (`:978-979`);
- `drift-audit records` is `python tools/drift-audit/drift_report.py --check` with **no guard**
  (`tools/gate-legs.json:569-576`) — a merge-bar leg on every bar.

So following F2 as written makes the new signal block the merge bar the day its pin is exceeded — the
hard gate over English that S3 and §3 both forbid. AC4 compounds it: a gateable non-live signal lands
in the `dead` list and exits 1 unless it is added to `DECLARED_EMPTY`, which no scope item or AC
covers, so "a repo with no builds gets a DEAD PROBE row" becomes "a repo with no builds reds the bar".

Conversely, keeping S3's report-only shape means `s["pin"]` is set at `:937` and never read for this
signal, so F2's "pin to drain" does not exist for it at all. The fork is resolved on a precedent that
contradicts the scope item three bullets above it.

**Fix.** Cite the report-only precedent instead: `live_backlog_rows_per_shard`
(`drift_report.py:811-826`) is `gateable: False` and reads its threshold as
`"tolerance": ctx.pins.get(<name>, 0)`. Restate F2 as that shape. Add a scope item declaring the
signal in the shipped conf template's PINS, so an adopter absent from it does not silently fall back
to tolerance 0 — the failure that signal's own comment warns about.

**Left-shift gate.** A drift-audit self-test assertion: **every signal declared report-only in its own
spec is `gateable: False` in code**, and every gateable signal appears in `RATCHETS`. Both are
one-line checks over `SIGNALS` and both are currently unwritten.

## HIGH 6 — spec 14's only ship/no-ship rule has no acceptance criterion, and the AC that appears to test it passes by writing a number down

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-14.md:53`** (§4),
**`:68`** (AC2). Three lenses, filed at medium and low.

**I graded this up, and here is the rule I applied.** The unit's stated purpose is to ship a *precise*
predicate or to refuse and take S5's fallback, and this is the only criterion standing between those
two outcomes. A decision rule with no reader is not a medium in a spec whose sibling defect list is
nine unfalsifiable ACs.

§4 lines 51-53: "A predicate that fires on `dScriptedRepeat` alone is tuned to one incident; one that
fires on every build is noise. **Neither ships.**" No AC encodes it.

AC2's second sentence: "Measured over the real corpus too: the false-positive count is written into
the record **whatever it is**." Satisfied by any value. It grades nothing.

The remaining ACs push the wrong way: AC1 is a synthetic agreeing/disagreeing fixture pair, and AC3
*requires* the reconstructed `dScriptedRepeat` README to fire. A predicate hand-fitted to the
`--counts` FACTS-versus-BASE-sha instance satisfies AC1, AC2 and AC3 in full while being exactly the
one-incident predicate §4 forbids. S5's fallback covers a predicate that cannot be made precise, not
one that is precise about a single instance — and nothing measures the condition that would trigger it
either way.

Partial mitigation: the "fires on every build" half is blocked by AC2's agreeing fixture and AC3's
second clause. The over-tuned half is entirely unguarded.

**Fix.** Give §4's rule an AC with numbers in it: run the candidate over every build in
`memory/builds/` and record hits **and** near-misses per build (§4 already asks for this); the unit
ships only if it fires on at least one build other than `dScriptedRepeat` and on no more than a stated
fraction of the corpus. Outside that band, S5's fallback is the required outcome. Keep AC2's "write
the count down" sentence as reporting, not as the acceptance test.

**Left-shift gate.** Spec-template rule, checkable at fold: **every "neither ships" / "must not"
sentence in §4 names an AC id.** It is greppable — a §4 paragraph containing "ships", "must not" or
"neither" with no `AC` token in it.

---

# MEDIUMS

## MEDIUM 1 — spec 15 gives two different mechanisms for the same change, and the difference is load-bearing

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-15.md:29`** (S3) against
**`:47`** (§4).

S3: "`run()` gains an optional scope argument … every call site passes the scope matching what its arm
asserts." §4: "`bash "$SCRIPT" ${RUN_SCOPE:-} 2>&1` with `RUN_SCOPE` set **per arm-block** rather than
per arm."

Under §4 no call site passes anything and an arm's scope is decided by its neighbours. Shell has no
block scope and §4 states no reset discipline, so a block that forgets to clear `RUN_SCOPE` leaks its
scope into every following arm. Any arm whose expectation crosses regions — a `miss` inside a
checks-1..27 block asserting that a check-28 message is *also* absent, or the reverse — receives the
wrong scope and goes vacuously green. Nothing detects either: see BLOCKER 2 for why the counter
cannot.

Two answers to one question, in the spec that has to be unambiguous because six rounds have broken
here.

**Fix.** Pick one and delete the other. The per-arm argument form matches S3's rule and cannot leak.
If the block form is kept for readability, state that `RUN_SCOPE` is reset at the top of every block
and add an AC that a deliberately un-reset block is caught.

**Left-shift gate.** If the block form survives: make `reset_tree` clear `RUN_SCOPE`, and add an arm
that sets it, calls `reset_tree`, and asserts the next run is unscoped.

## MEDIUM 2 — "which halves an invocation" transfers an out-of-fixture, network-touching reading onto the in-fixture population it is used to size

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-15.md:27`**.

The 22.7 s / 11.7 s pair was taken on the **real repo**, where `check-unattended.sh` is a declared
IMPURE leg that runs `ls-remote` against the real origin (`tools/gate-legs.json`, the `unattended kit
gate` row). The suite's fixture builds its own bare origin under `mktemp -d`
(`check-unattended.test.sh:145`), so the two runs do not measure the same work, and **no in-fixture
split is offered at all.**

Measured on this worktree: whole 30.8 s, `--only 28` 10.0 s (32%), `--skip 28` 19.0 s (62%). The
direction most arms take saves ~38%, not the 50% the spec claims. AC1's ceiling arithmetic rests on
this transfer.

**Fix.** Move the split into S1's profile — measure it **inside** the suite's own fixture, once each —
and state S2's expected saving from that reading. Mark the 22.7/11.7 pair as a real-repo measurement
that includes the remote observation, so nobody transfers it again.

**Left-shift gate.** Covered by BLOCKER 3's "every number carries the command that produced it" rule;
the command line makes the population visible without anyone having to remember.

## MEDIUM 3 — spec 15's third candidate lever has no consumer left

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-15.md:28`**.

S2 lists "the shard split, measured at 1565 s against 692 s" as a candidate. AC1 measures
`run-unattended-gates.sh --selftests`, and that runner invokes the suite **unsharded on purpose**:
`:119` is `run_one "gate selftest" selftests bash "$HERE/check-unattended.test.sh"` with no `--shard`,
and `:53` states "The suites are run UNSHARDED on purpose." Rebalancing shards moves AC1 by zero
seconds.

The consumers are gone too: the `--shard 1/2` and `2/2` rows existed in `tools/gate-legs.json` only up
to `f5f4732a~1`, and no tracked file outside the suite's own argument parser passes `--shard` today.
So a builder told to "pick the lever the profile names, and only that one" is choosing from a list
whose third entry cannot affect the criterion.

**Fix.** Drop it, or keep it with one sentence saying it served the removed bar legs, cannot affect
AC1's unsharded measurement, and is out of scope for this unit.

**Left-shift gate.** The drift audit's dead-code lens already asks this question elsewhere: a declared
mechanism with no caller is dead plumbing. A `--shard` call-site census would have flagged it the day
the legs were deleted.

## MEDIUM 4 — spec 15's AC3 supersedes two wrong claims and leaves a third, which is also re-typed in the runner header

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-15.md:75`**.

The bar-cost record states "That suite carries roughly eighty arms. 80 × 22 s is the leg, near enough"
— wrong by 3× against the 246 `$(run` sites and 405 measured assertions, and internally inconsistent
too (80 × 22 = 1760 s against the ~3200 s the runner records). The identical claim is re-typed at
`tools/unattended/run-unattended-gates.sh:78`: "each of its ~80 arms stages a break and re-runs the
whole 23 s leg". That is where every future reader meets the OVER BUDGET red.

AC3 names only S1's two claims. After this unit lands, the corrected number lives in the build record
and the wrong one still lives in the runner — two answers to one question, in a spec written because
the cost model has been wrong twice. The runner's "OVER ITS BUDGET ON PURPOSE" note also stops being
true the moment AC1 passes, and nothing updates it.

**Fix.** Add the arm-count and per-arm-cost claim to AC3's supersede list, and add an AC that
`run-unattended-gates.sh`'s header carries the corrected figures — or better, that it stops restating
them and points at the bar-cost record.

**Left-shift gate.** This repo already gates "no count of a derived population is written in prose".
Extend the predicate to the kit's shell headers: a comment stating an arm count or a per-arm second
figure beside a suite it does not derive reds. Run the candidate over the tree first and print
near-misses — several kit headers carry legitimate readings, and the rule must distinguish a
measurement carrying a date and node from a model.

## MEDIUM 5 — spec 13 derives its population from HEAD; the driver derives it from the run's pinned BASE

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-13.md:18`**.

S1's population is "every tracked playbook" and §4 uses `GITLS`, i.e. `git ls-files` at HEAD. The
driver reads the root from the **pinned BASE blob**: `unattended.sh:3414` and `:3444` are both
`declared_scalar "$(GIT show "$(fact "$rel" base):$pb")" records`, and the `records-current` DoD census
does the same at `:2590` — it even reds when the playbook does not resolve there.

Change `records = "a"` to `records = "b"` in any later commit and every evidence record already
committed under `a` leaves the check's population. The widened pass then greps a wrong or empty set
and prints nothing — byte-identical to clean. That is AGENTS.md's own "a stale exemption silently
widens the surface it was written to narrow", applied to a security check.

**Fix.** Derive the population from the union of the roots declared at HEAD and the roots declared at
every non-terminal run's pinned BASE blob. Add an AC: a tracked evidence record under a root the
current playbook no longer declares still reds.

**Left-shift gate.** An arm that edits a fixture playbook's `records =` line after a record has landed
under the old root, and reds if the check stops seeing it.

## MEDIUM 6 — spec 13's widened pass has no liveness assertion, and AC4 explicitly blesses the empty population

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-13.md:69`**.

§4 and all six ACs describe what the widened pass reds **on**. None asserts it graded anything. AC4
makes "a playbook declaring no `records` root contributes no population" an explicitly PASSING
outcome. Union that with MEDIUM 5's HEAD pinning and HIGH 4's empty fixture and you get a check whose
coverage can silently reach zero while the leg stays green.

The neighbouring leg already refuses exactly this: `check-playbook.sh:100` reds with "no tracked file
carries a playbook declaration block…" because a green over an empty population means the opposite of
what it looks like. The new pass copies the population idea without the guard — and this repo's
charter rule is that a probe which cannot move says so.

**Fix.** Add an AC: the widened pass reports on the REPORT channel how many roots and how many records
it graded, and a run that finds a declared non-empty root but enumerates zero tracked records under it
announces that case rather than passing silently.

**Left-shift gate.** The report line itself, plus a suite arm asserting the graded count is non-zero
in the fixture HIGH 4 asks for. One gate closes HIGH 4 and this.

## MEDIUM 7 — the driver's second evidence-record writer takes an arbitrary caller-supplied root, which the read-back check structurally cannot reach

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-13.md:33`** (the non-goal),
**`:52`** (§5's claim).

`record_piece`/`record_set` have two callers. The slug path derives the root from the pinned BASE and
refuses an undeclared one. The `--records-root` path (`unattended.sh:3405-3406`, `:3436-3437`, argv at
`:3779`) passes `$RP_ROOT` straight through — no containment test, no declaration check. Both writers
guard the FIELDS (newline, the ` · ` separator, `BYPASS_BAN`) and then `mkdir -p` and write wherever
the root points, staging the result.

§5 line 52 claims "the write-time guard prevents it and this detects it after the fact, which is the
pair the charter asks for". The pair is asymmetric: the field guard covers both callers, but a record
can land **outside every declared root**, where the read-back never looks. The non-goal at line 33
rules out the wide fix without offering a narrow one. §9's rule is one composite guard on every path
that stores parseable content.

The practical exposure is narrower than a total hole, because the field-level bypass guard does cover
both callers — which is why this is medium. The spec's stated justification is still inaccurate.

**Fix.** Either refuse at write time — validate `$RP_ROOT` against the declared roots using
`covers`/`normpath`, already in `lib-unattended.sh:45-71` — or derive the read-back population by
record SHAPE (a tracked `*.md` carrying a `piece:`/`run:` field), which is a derived population and not
the "arbitrary tracked files" the non-goal rejects. Give whichever is chosen an AC.

**Left-shift gate.** An arm that calls `record_piece --records-root <path outside every declared root>`
and asserts the driver refuses. Two lines, and the write path is already fixtured.

## MEDIUM 8 — spec 13's "`BYPASS_BAN` may be empty" premise is false about the file it edits, which makes AC4's first half vacuous

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-13.md:47`**.

§4: "`BYPASS_BAN` is a declared conf value and may be empty … a project that declares no flag gets no
new work and no new red." `check-unattended.sh:113-117` lists `BYPASS_BAN` among the six required keys
and reds check 1 when it is empty.

So AC4's scenario — "a repo declaring no `BYPASS_BAN` reds nothing new" — describes a tree the checker
**already refuses**, and the criterion is satisfied trivially by that pre-existing red while proving
nothing about the widened guard. Worse, `fail()` at `:82` is `{ echo …; status=1; }` with no exit, so
the leg runs on with `BYPASS_BAN` empty and check 11 plus the new pass are **unarmed for the rest of
that run**. The spec records that state as benign; it is the disarmed one. Check 1 does red loudly and
names the key, so this is not silent — only mis-described.

**Fix.** Drop the "may be empty" claim. Restate AC4's first half against real behaviour: an empty
`BYPASS_BAN` reds check 1, and the widened pass must not report a false clean in that run. If the
disarmed-but-continuing path is to stay, add a scope item making check 1's failure exit the leg, as
the missing-conf branch already does.

**Left-shift gate.** An arm asserting that after a check-1 refusal of a key later checks depend on, the
leg does not emit a clean verdict for those checks. Generically: **a checker that continues past a
refused precondition marks every dependent check unarmed, not clean.**

## MEDIUM 9 — spec 13's perf baseline cites the wrong leg's reading, and the cross-unit consequence goes unstated

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-13.md:57`**.

§5: "if it moves the leg's **13 s** reading at all, that is reported rather than absorbed."
`run-unattended-gates.sh:68-69` declares `BUDGET_kit_gate=120 # measured 28 s` for
`check-unattended.sh` and `BUDGET_playbook_validity_gate=120 # measured 13 s` for `check-playbook.sh`,
bound to those scripts at `:115-116`. Check 11 lives in the 28 s leg; `check-unattended.sh:61`
independently says "~23 s". 13 s is the other leg's number — the same file-confusion as BLOCKER 1,
which makes this a symptom rather than a typo.

The cross-unit consequence is real and unstated: the same file is invoked ~243 times inside the suite
unit 15 must bring from ~3200 s under 900 s, so a per-record grep added here lands directly on unit
15's AC1. Neither spec references the other.

**Fix.** Cite the leg's own recorded reading (28 s per the runner, ~23 s per its header) and name where
it comes from. Add an AC: the before/after per-invocation cost of `check-unattended.sh` is recorded in
the bar-cost record, and the delta × 243 is stated against unit 15's 900 s ceiling, so the two units
are sequenced deliberately rather than by accident. §5's promise that the measurement is "reported
rather than absorbed" is held by none of AC1–AC6 — give it one.

**Left-shift gate.** The runner already prints per-leg seconds against a named ceiling. Make the fold
require a before/after row for any unit whose scope touches a leg named in another in-flight unit's
acceptance criterion; the cheap version is a fold-checklist item.

## MEDIUM 10 — spec 14's AC5 measures the audit against a time budget that does not exist

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-14.md:75`**. Three lenses.

AC5: "`python tools/drift-audit/drift_report.py` stays under its own time budget."

There is no budget. `tools/drift-audit/` holds no `BUDGET_*` constant, `drift_report.py` contains no
timing code at all, `tools/gate-legs.json` carries no timeout for `drift-audit records`, and every row
of `tools/run-gates/gate-profiles.txt` declares `timeout=0`. `.memory-tree.conf`'s `UNIVERSAL_BUDGET`
and `READ_PATH_CEILING` are index and byte budgets, not time. The only statements are prose:
`drift_report.py:34` "It runs in seconds; there is nothing to invalidate", and `README.md:141`
"seconds, 0 agents".

So AC5's first clause has no referent and is satisfied by any runtime. That matters because §5's perf
bullet is the only thing standing between "a signal reading every spec of every build" and the
seconds-and-no-agents property the audit's whole Tier-0 position depends on — and it is how the
sibling suite reached 53 minutes without any single change looking expensive. Unit 15 gets this right
by naming `BUDGET_gate_selftest=900`; unit 14 points at nothing.

**Fix.** Either declare the ceiling as part of this unit, in the shape `run-unattended-gates.sh`
already uses — a named constant with the measured reading beside it and a red on breach — and have AC5
cite the number; or replace AC5 with the recorded-reading form: this signal's added seconds are
measured before and after, written into the bar-cost record, with a stated threshold above which it
does not ship.

**Left-shift gate.** Give the drift audit the same `BUDGET_* # measured N s` treatment the unattended
runner has, and red on breach. That single change turns AC5 from unfalsifiable into observable and
protects the property the audit is sold on.

## MEDIUM 11 — spec 14 puts the liveness assertion on the population that cannot go blind

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-14.md:25`**.

S4: "This one's liveness is that it found at least one README/spec pair to compare at all." Fourteen
build folders satisfy that permanently, through any layout change to spec front matter, revision-log
headings or backtick conventions.

The stage that actually goes dark is the inner one — §4's backticked-token scan and revision-log
parse. When it stops matching, the signal reports `live=True` with value 0, which renders as `ok`
rather than DEAD PROBE. That is the failure the kit's own README documents at
`drift_report.py:335-338`: a pre-flatten glob left `--check` green over a blind oracle for a whole
session. The kit's convention is liveness on the **judgeable** population — `:308-312` spells it out,
and `:372` is `"live": checked > 0` where `checked` counts specs whose status and own id actually
parsed, with unparseable ones counted as `unkeyed` rather than assumed clean.

AC4 only exercises the no-build-folder case, so the blind-extraction state has no arm either.

**Fix.** The signal is live only when it parsed at least one README line carrying a backticked token
AND at least one spec revision-log entry. Report both sub-counts in `of`/detail so a reader can see
which half went empty, and arm both directions in the drift-audit self-test.

**Left-shift gate.** A drift-audit self-test rule over `SIGNALS`: every signal's `live` expression must
reference the same variable its `value` is computed from. Mechanical, cheap, and it would have caught
the pre-flatten glob incident too.

---

# LOWS

## LOW 1 — the 59 ms reset figure does not reproduce on this node

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-15.md:19`**.

`reset_tree` (`check-unattended.test.sh:171-177`) is `git reset -q --hard` + `git clean -qfd` +
`git for-each-ref` piped through a grep into `git update-ref --stdin --no-deref` — four MSYS process
spawns. Replayed here in a freshly-initialised **one-file** repo, 10 then 3×20 iterations: 115, 121,
136, 117 ms per reset. That is ~2× the claimed 59 ms, and a real fixture repo cannot be faster than a
one-file one. The arithmetic confirms 59 ms is what the "~14 s" came from: `grep -c reset_tree` = 248,
and 248 × 0.059 = 14.6 s.

The bullet's **conclusion survives** — 248 resets at ~120 ms is ~30 s, ~1% rather than 0.4%, still not
the dominant term — which is why this is low. It is filed because S1's entire rhetorical weight is that
it corrected two unmeasured claims, and it carries an unreproducible third.

**Fix.** Re-time `reset_tree` inside the suite's own fixture with the loop count printed, record the
method beside the number, and state the percentage from that measurement.

**Left-shift gate.** Same as BLOCKER 3's: a cost figure in a record carries the command that produced
it, or it is marked derived.

## LOW 2 — spec 14's F2 adopts its cited precedent halfway: no `RATCHETS` entry

**`memory/builds/dScriptedRepeat/spec/2026-08-23-spec-dScriptedRepeat-14.md:91`**.

`tools/drift-audit/drift_signals.py:257-268` registers exactly three signal pins in `RATCHETS` —
`non_terminal_specs_cited_by_product_source`, `handkept_inventories_disagreeing_with_source` and
`live_backlog_rows_per_shard`, the precedent F2 names and its two siblings. The block's own comment
(`:229-236`) says why: every gate compares only `value > pin`, so raising the pin and draining the
population are indistinguishable without a `<old> -> <new>` justification inside
`RATCHET_LOOKBACK = 14` lines.

Registration is not automatic — `PINS` also carries `closed_specs_with_no_product_commit`,
`lexicon_verbs_declared_but_unused` and `lexicon_ratified_older_than_language_surface` with no
`RATCHETS` entry — so this is a gap rather than a broken universal rule. But F2 names the ratcheted
trio specifically, and no scope item or AC requires the entry, so the new pin would be raisable
silently: the drain-forever mode the ratchet exists to prevent.

**Fix.** Add to S3 or the ACs: the new signal's pin is registered in `RATCHETS` with `weakens: up`, and
an AC that raising it without a justification line inside the lookback window reds the ratchet gate. If
an exemption is intended, say so and name the compensating check.

**Left-shift gate.** Fold into HIGH 5's self-test rule — every signal with a `PINS` entry either
appears in `RATCHETS` or carries a declared exemption naming its compensating check.

---

# Left-shift summary

Eight gates would close nineteen of the twenty-two defects. Ranked by defects closed:

1. **An absence assertion is evidence only if the thing that could emit the string ran.** Mechanise as
   the suite preflight in BLOCKER 2. Closes BLOCKER 2 and bounds MEDIUM 1.
2. **Check 28's parser comparison derives its population from `KIT_SH`** instead of naming two paths,
   with a third divergent copy staged RED. Closes BLOCKER 1's ungated-third-copy consequence and
   HIGH 3.
3. **Every number in a bar-cost record carries the command that produced it**, or is marked derived.
   Closes BLOCKER 3, MEDIUM 2, MEDIUM 4 and LOW 1.
4. **The widened pass reports its graded population and reds on a declared-but-empty root.** Closes
   HIGH 4 and MEDIUM 6.
5. **A drift-audit self-test over `SIGNALS`**: report-only in the spec means `gateable: False` in code;
   a gateable signal is in `RATCHETS` or carries a named exemption; a signal's `live` expression
   references the variable its `value` is computed from. Closes HIGH 5, MEDIUM 11 and LOW 2.
6. **`BUDGET_* # measured N s` for the drift audit**, redding on breach. Closes MEDIUM 10.
7. **A checker that continues past a refused precondition marks dependent checks unarmed, not clean.**
   Closes MEDIUM 8.
8. **Spec-template rules**: every "neither ships" / "must not" sentence in §4 names an AC id, and every
   AC whose observable is "identical output" names the non-empty output it compares. Closes HIGH 6 and
   HIGH 1's class.

HIGH 2, MEDIUM 3, MEDIUM 5, MEDIUM 7 and MEDIUM 9 stay human reads; each names its own arm in its Fix
paragraph.

# What the three specs get right, because a report of only defects is not an audit

- **Unit 15's goal is the real problem.** A compensating check nobody can afford to run is worse than
  the seven legs it replaced, and the spec says so in its first paragraph. Making profiling the first
  build step rather than a note is the correct response to two wrong cost claims — BLOCKER 3 attacks
  the execution of that step, never the decision to take it.
- **Unit 15's non-goals are load-bearing.** "Not removing or merging arms to hit the number" and "not
  restructuring the checker into independently runnable checks" both name real temptations with real
  reasons, and the second cites `--only 14`'s existing refusal as its evidence rather than asserting.
- **Unit 14's S5 is the best paragraph in the diff.** Declaring the honest fallback in the spec rather
  than discovering it during the build is exactly right, and unit 15's lack of one is HIGH 2.
- **Unit 14's F1 is resolved on evidence**, not convenience: a git mtime moves when a typo is fixed,
  the spec's own revision log does not. Right clock, right reason. (F2, three lines below it, is
  HIGH 5 — the contrast is instructive.)
- **Unit 13's goal is correct and its round-2 history is stated honestly.** The build took the cheaper
  repair, the spec says so, and S4's "that sentence is currently true only because it stopped making
  the claim" is the kind of sentence that makes a spec worth auditing. Every defect in unit 13 is in
  where and how, none in whether.
