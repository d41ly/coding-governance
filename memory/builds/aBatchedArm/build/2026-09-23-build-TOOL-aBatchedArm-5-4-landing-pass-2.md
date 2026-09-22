**Serves:** journal TOOL-aBatchedArm-5 TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3

# aBatchedArm — landing pass two: the week unlanded, the reds cleared, the evidence retaken

The first landing pass closed on 2026-09-15 with the flip committed, the run at phase LANDING and the
landing handed to the owner. It was never run. The branch sat seven days; `main` advanced 523 commits
and then 11 more, and the owner asked on 2026-09-22 whether it had landed and then to land it, and to
fix the pre-existing reds rather than record them. This record is that second pass. The first pass's
record, `2026-09-15-build-TOOL-aBatchedArm-5-3-landing-ledger.md`, stands: nothing in it is withdrawn,
and every figure here supersedes its counterpart there by date.

## What the week cost

`origin/main` was `4cf0944d` when the first pass merged it and `2de31c7e` when this pass began — 523
commits, seventeen files touched by both sides. It moved again to `857a9781` during the repairs. Four
reconciles in total, every conflict additive:

- the third (`28eed132`) took nine conflicts. The kit descriptor's include list is the union at twelve
  suites; `selftest-budgets.txt` keeps this build's eight `--shard i/8` rows and DROPS main's re-added
  unsharded `unattended gate selftest` row, because one arity per script is the shard join's rule;
  `check-unattended.test.sh` keeps both fixture keys and the eight-shard floors; the adopter suite
  takes main's floor and terminal-exit guard ahead of this build's unconditional trailer.
- the fourth (`1827cd83`) took two, both records.
- main's three new kit suites — `stall-recorder`, `stop-guard`, `resume-tick` — printed their trailer
  only behind a green guard, which the pooled route reads as UNTRAILED. They take the one-line fix the
  five suites took at closing D4.

## The reds, and what they were

The owner's instruction was to fix them. Seventy-six failing assertions across three suites, and one
class: a staged break whose anchor text had been rewritten under it, so the fixture mutated zero bytes
and the assertion beneath read the absence as the product failing. The adopter suite's ten were
already gone — main had fixed them, and it runs green at 100 assertions on the merged tree.

**`check-unattended.test.sh`, 22 reds** (`a5d54fb6`). Eleven `fixture no-op` lines and the nine
`missing` assertions under them, plus two silent ones:

- the protocol's count sentence moved from "Ten kit-owned core items" to "Twelve"; both arms now match
  the count WORD rather than one spelling of it.
- `declared_list` and `declared_scalar` were rewritten from sed pipelines to parameter expansion, so
  five mutations aimed at `#.*$` hit nothing. Each is re-aimed at today's comment strip with the same
  intent: the strip disabled, the strip applied to the wrong text, the comma conversion removed in one
  copy only.
- the DoD-shrink fixture deleted `parked-decisions-surfaced:agent` as the last item of `DOD_CORE`;
  `reuse-probed:machine` had been appended after it. It deletes the last item whatever it is, through
  `mutate`, which announces a no-op instead of leaving the assertion to report it.
- the `timeout` stub matched the liveness probe's exact argv, which moved from `1 true` to `10 true`
  when the probe was lengthened against spawn latency. It matches the command, not the seconds.
- the sidecar-callers arm deleted one of what are now four call sites, so the ZERO-callers refusal
  never fired. It empties every call spelling.
- `--unit` and `--disposition` are flags of `--brief` and `--review` and were graded as verbs — a red
  the file's own comment recorded and deferred to a later unit. Both are denied and the floor is
  re-derived at 18 by this file's own derivation over the driver.

**`unattended.test.sh`, 54 reds** (`e197267e`, `8b3567fc`, `2ae12086`). The dispatch region's forty-odd
were one cause: the driver grew M2's hard floor — a pass for a unit no tracked spec defines is refused
as MISSING — and the fixture at UNIT0 carries no spec, so every arm was answered by that refusal
instead of the one it asserts. `build_audit_fixture` below it already carried a private copy of the
workaround and its header said why; `dspec_reset` lifts it out and the region's twenty `reset_tree`
calls use it. The rest:

- `mkconf` had TWO owners for positional 8, `RESUME_STALE_BOUND` and `SPEC_AUDIT_DEFAULT`, so every
  spec-audit arm set a seconds bound to a date and the driver refused at exit 2 before any verb ran.
  Nine slots, one key each, eight call sites re-aimed.
- two arms appended `GENERATED_INDEXES` through a single-quoted `printf`, so the fixture conf carried
  the literal `$KIT_REL` and the driver — which reads that conf under `set -u` — died unbound.
- the unborn-HEAD arm's fixture carried a run-state file and nothing else; it stages a spec now, which
  `ls-files` reads and HEAD cannot affect.
- the brief region inherited whatever run-state the dispatch arms left; it resets and preflights.
- the liveness AC3 block assumed HEAD was a commit the default branch does not carry and that unsetting
  `GOV_DEFAULT_BRANCH` left the ref unresolvable. It makes the commit and deletes `origin/HEAD` itself.
- AC7 iterated over two surfaces and the verb row it reads moved to a third when the protocol pair was
  split. Observed green, then RED with `--code` dropped from the Skill's invocation.

**One product change fell out of that set.** `verb_brief` joined its `--unit` to the roster BEFORE
validating the shape of what it was handed, so the newline, field-separator and bypass-flag forgery
refusals were unreachable through `--unit`: every forged value is also off the roster, and the roster
refusal answered first. Shape first, join second.

**Four more the calibrate surfaced** (`ceadeb66`), none of them a suite this build wrote:

- `cross-component` derives its fixture conf from the repository's own, which has declared
  `UNDECLARED_WRITE_CEILING="53"` since 2026-09-21, while its fixture tree holds no dispatched pass at
  all — so check 23's liveness branch fires exactly as designed. The filter already neutralises five
  keys the fixture cannot honour; the ceiling is the sixth. Verified failing identically on main's own
  tip `857a9781` before it was touched.
- `runlog-writer` printed `FAILED (n assertions)` on a red run, which is no trailer the pooled route
  recognises, so the calibrate read it UNTRAILED and wrote no reading at all.
- `stop-guard`'s AC19 and four `resume-tick` arms are wall-clock windows sized just under the sleeps
  they race — 2 s against a 3 s sleep, 5 s against 15. Under the eight-wide pool they read 2560 ms and
  14 s, so the rows went red for LOAD rather than behaviour, which would have flapped the parity
  verdict this build's DoD now rests on. The sleeps are 30 s and 60 s and the windows sit well inside.

**And one leg of this build's own.** `runlog-writer`'s AC9 asserts that no manifest leg runs a kit
suite of `tools/unattended/` — the owner's ruling of 2026-08-23, which took every such leg off
`tools/gate-legs.json`. This build's unit 2 added exactly one, for the arms-groups linter's suite. The
row is removed and the budget row carries the argv it had been taking from the leg; the suite still
runs, as row 2 of the pooled population, and the carried-prefix count rises 26 to 27 by hand for that
argv. **TOOL-aBatchedArm-2's AC6 is superseded**: "the leg appears in the manifest-derived leg list"
was observed at the first pass's gate run and is now contrary to the ruling. Its compensating coverage
is the pooled DoD pass below, which runs that suite and matches it against a calibrated baseline.

## Step 0 — the eight shard runs, twice

At `28eed132`, the merged tree before any repair: walls 677 to 922 s on an idle box, executed
83 · 69 · 49 · 102 · 64 · 78 · 95 · 94, FAIL union 22 lines — the 21-line oracle plus one arm main's
growth had broken. At `a5d54fb6`, after the repairs: every shard rc 0, ZERO FAIL, executed
86 · 69 · 49 · 102 · 64 · 78 · 95 · 94, sum 637. The nine floors are re-read from that run at ~3 %
under: 83 · 66 · 47 · 98 · 62 · 75 · 92 · 91 and the unsharded 617 (`1827cd83`). The fourteen pasted
`check_emitted` sets still match: no sentinel red in any run, and all 49 signatures still resolve
verbatim in the checker after main's 165-line growth of it.

## Steps 1 and 2 — the calibrate, twice

The first (at `2ae12086`) ran 6337 s and exited RED: nineteen readings written, three rows red and
`runlog-writer` UNTRAILED. Its readings are what named the four defects above; none of them was
visible to a shard run. The second (at `ceadeb66`, committed `509fb28e`) ran 4029 s under the 21670 s
serial-sum wall, tree fingerprint MATCHED, and reports `calibrated 20 row(s), 0 red, 0 walled,
0 untrailed`. Every suite in the kit's population exits 0 — the first time that has been true of this
kit. Two rows read 1 FAIL at rc 0, and that is correct: `stall-recorder` and `stop-guard` each print a
deliberate `FAIL` line while exercising their own payload-builder liveness guard, then reset their
counter. The parity triple records what the suite does, not what a grep thinks of it.

Readings, `pooled@8x1` on node a: driver 3982 s; shards 1611 · 1964 · 1474 · 2333 · 1225 · 1331 ·
1391 · 1443 s; playbook 499; resume-tick 334; cross-component 323; pass-order 269; brief-recorded 210;
adopter 209; runlog-writer 165; gate-guard 120; stop-guard 58; stall-recorder 23; arms-groups 10.

## Step 3 — the pooled DoD pass

`bash tools/unattended/run-unattended-gates.sh --pooled` at `509fb28e`, `ps before: 0`, 4076 s, rc 0:

```
run-selftests: SWEEP of 20 suite(s), width 8 (outer 8, inner 1), node a
run-selftests: condition: pooled@8x1
run-selftests: per-suite bound = max(budget, calibrated reading) + headroom max(120s, 1.0 x that); run wall 12600s; NO cost verdict is issued
run-selftests: tree fingerprint MATCHED before and after — no suite wrote outside its scratch
sweep GREEN — 20 suite(s) ran concurrently, every one to its own end and matching its baseline; killed 0 · walled 0 · unrun 0 · unstarted 0 · mismatched 0
unattended gates GREEN — 20 ran on demand; no self-test here runs on the merge bar · pooled, 20 cost verdicts withheld
```

Twenty rows, every one matched. This is S4's parity GREEN and S5's step (3): the observation that
licenses the flip.

## Step 4 — the flip, unchanged

The flip landed in the first pass at `3e7e7aae` and survived all four reconciles byte-intact. Re-read
at this tip: the carrier predicate yields the four POINTERS and nothing spelling `--serial` as a
criterion — `AGENTS.md:512`, `memory/guides/SESSION-KICKOFF.md:224`, `tools/unattended/README.md:138`,
`tools/unattended/run-unattended-gates.sh:246`. The four DoD carriers spell `--pooled`:
`.githooks/gate-env.sh`, `tools/unattended/run-unattended-gates.sh` and `kit.toml`'s two lines. No
second flip commit is owed; the GREEN above is the evidence the first one was waiting for.

## Reported to the owner, not fixed here

- The manifest's §B now carries a dated correction saying the kit's self-tests are green whole, and
  the pooled DoD line carries the new evidence date and population. Both rode the `ceadeb66` commit,
  which is where check 5 demanded them.
- `--rank` still refuses two of main's budget rows whose reason columns carry no ranked condition.
  Pre-existing and untouched.
- The left-shift this class deserves and this pass did NOT build: a check that no fixture edit in a kit
  suite uses a bare `sed -i` outside `mutate`. Every silent red above was a direct `sed -i`; every
  announced one went through `mutate`. It belongs in the tooling backlog, not in a landing.
