# Build journal — TOOL-aCollapsedScan

**Serves:** journal TOOL-aCollapsedScan-1

Node `a` · branch `branch/unattended-check-plan-27c557` · base `da9e4cd2`.

## Why this was measured before it was built

An adopter reported `check-unattended.sh` at over 600 s and attributed it to check 30's liveness
guard. The attribution was wrong, which is the only reason this unit exists in this shape. Measured
on node `a` at `da9e4cd2`, over the 70 tracked builds of this repo:

| Subject | Seconds |
|---|---|
| the whole `unattended kit gate` leg | 289 |
| check 30's `--plan` walk alone | 235 |
| `unattended.sh --version`, the fixed driver startup | 0.28 |

Per-build cost rose with SPEC count, not with anything check 30 does:

| Build | Specs | Before | After (rev-2) |
|---|---|---|---|
| `aNamedGesture` | 1 | 1533 ms | 1842 ms |
| `aRuledFrontispiece` | 11 | 5937 ms | 2126 ms |
| `cBriefedPilot` | 23 | 15956 ms | 2556 ms |
| `dUnstalledConvoy` | 24 | 16599 ms | 3060 ms |

THE SHAPE IS THE RESULT, not any single row. Before, cost rose 10.8x from the one-spec build to
the 24-spec build; after, it rises 1.7x. The superlinear term is gone. A one-spec build is 300 ms
SLOWER, because `spec_ids` keeps its own `git ls-files` and awk after the rev-2 correctness fix,
and that is the trade: a fixed cost on the smallest builds against 5.4x on the largest.

`verb_plan` resolved a region id to its spec with an `awk` per (unit, spec) pair, and read each
spec's status and heading with two more per spec in the pass above it. The diagnosis and the fix are
both already recorded in this kit for a different suite: `run-unattended-gates.sh` carries
`TOOL-dNarrowedAnchor-1`'s measurement that one process creation costs 0.019–0.039 s on a node with
an on-access scanner, and that cutting spawns is the only term in that product this repo owns.

## What the budget already said, and nobody had run

`bash tools/unattended/run-unattended-gates.sh --checks` at `da9e4cd2`:

```
ok    kit gate                         305s
      OVER BUDGET  kit gate took 305s against a declared 120s ceiling — fix it or raise the ceiling
ok    playbook validity gate            33s
ok    skill wiring                       1s
----
unattended gates RED — 3 ran on demand, 1 over budget
```

`BUDGET_kit_gate=120` was declared 2026-08-23 against a 28 s reading on node `d`. Check 30 landed
2026-08-25 in `1ce89563` and the ceiling was never re-measured. The mechanism the charter demands
existed, fired correctly, and was read by nobody, because nothing on the merge bar runs it.

## What landed

`tools/unattended/unattended.sh` only. Two new functions and six call-site rewrites.

| Site | Before | After |
|---|---|---|
| `spec_facts` | did not exist | 1 awk over all of a build's specs, printing one row each |
| `load_spec_facts` | did not exist | fills three maps from `spec_facts`, for `verb_plan` only |
| the `NOT A UNIT` pass | `2n` awk, plus a `basename` per row | map reads and `${spec##*/}` |
| `_renderable` | 1 git, `n` awk, 1 sort, 1 grep | a bash count over the maps |
| region id extraction | a printf, a grep and a head PER ROW | 1 awk with `match` over the region |
| id to spec resolution | up to `u` × `n` awk | one `SPEC_PATH` read |
| per-unit status re-read | `u` awk | one `SPEC_ST` read |
| `missing_units` | 1 git, `n` awk, 1 sort | 1 git, 2 awk, 1 sort — contract unchanged, see below |
| `plan_state` | `u` awk | unchanged, and deliberately |

`plan_state` was left alone because `tools/memory-tree/marker-contract.test.sh:218` and
`tools/unattended/unattended.test.sh:3675` both slice its body out of the shipped bytes and evaluate
it as a standalone function of one spec path. Folding it into the single pass would buy `u` spawns
and break a cross-kit contract.

## What my own diff review caught, and the one it missed

**The renderable count changed its aggregation, and the comment claimed it had not.** `spec_ids`
deduplicates and so counted distinct IDS; the bash replacement counts SPECS carrying both fields.
The two differ only where two specs claim one id, and the sole reader asks `-gt 0`, on which they
cannot differ. The comment now says that, rather than the false "same predicate" it said first.

**Iterating an empty associative array is the one bash-version-sensitive spelling in here**, and the
state is reachable when every tracked spec is zero-length. `verb_plan`'s count loop tests
`${#SPEC_ID[@]}` first and the maps are assigned at declaration, because the kit is
copy-installed into repos whose bash this one has never seen. The rev-2 fix below made the
second half of this moot by taking `spec_ids` off the maps entirely.

## The regression, and how it was found

The first cut of S6 made `spec_ids` read the shared maps and made `missing_units` take a roster
`verb_plan` had already derived. `--close`'s build-complete term at `unattended.sh:2922` is a
SECOND caller of `missing_units`, with no `verb_plan` frame above it. It got the slug where the
roster ids belonged, it read maps nobody had filled, and it lost the exit 3 whose propagation
that call site's own comment records as a previously-fixed defect. `bash tools/unattended/unattended.test.sh`
returned exit 1 with 12 FAIL arms, every one of them carrying the same line:

```
unattended.sh: line 1598: SPEC_ID: unbound variable
UNATTENDED check 13 FAILED — a machine-checked DoD item is unmet, so --close blocks: build-complete
```

MY REVIEW OF MY OWN DIFF DID NOT FIND IT, and the reason is worth more than the fix. I grepped
for the call sites and piped the grep through `head -20`; the output ended at line 1715 and
line 2922 was below the cut. A truncated enumeration read as a complete inventory is the
vacuous-selector class this repo gates against everywhere, committed in the diff that removes
an instance of it.

The fix splits the awk into a pure `spec_facts` emitter, restores `spec_ids`'s `dir` argument
and `missing_units`'s two-argument contract, and assigns the maps at declaration with `=()`.
Verified by slicing `spec_facts`, `spec_ids`, `roster_ids` and `missing_units` out of both
drivers and running the join with no `verb_plan` frame, over four fixtures:

The fixture ids are spelled with a lowercase family below on purpose: the shape a real id
carries would be an id CITED and never defined, which hygiene check 14 refuses and whose
waiver registry is empty and shrink-only.

| Case | Base | Patched |
|---|---|---|
| `spec_ids` over a well-formed build | prints `tool-good-1`, rc 0 | same |
| `missing_units`, nothing missing | rc 0, no output | same |
| `missing_units`, MALFORMED roster pair | rc 3 | same |
| `missing_units`, roster names an unspecced unit | rc 0, prints `tool-gap-2` | same |

## Result

**Evidences:** TOOL-aCollapsedScan-1

- AC1 — `diff` — MET, and re-run after the rev-2 fix. `--plan` captured from the driver at
  `da9e4cd2` and from the patched driver, over all 70 builds tracked at that base, comparing
  stdout, stderr and exit code: 0 differing files out of 210.
- AC2 — `unattended.test.sh` — MET for the driver suite, PARTIAL for the criterion as written.
  `bash tools/unattended/unattended.test.sh` returned exit 0, `PASS (849 assertions)`, 0 FAIL lines.
  The `gate selftest` suite was NOT run: the owner stopped it mid-run and instructed that only the
  driver suite be run. Its subject is `check-unattended.sh`, which this diff does not touch, but it
  does carry check-30 arms that invoke `--plan` against fixture builds, so that coverage is genuinely
  absent and is stated here rather than implied away. The other three selftest suites were not run
  either, for the same instruction.
- AC3 — `235 s` — MISSED against its stated threshold. The walk went 235 s to 109 s, a 2.2× cut
  (94 s at rev-1, before correctness cost back the second roster derivation), and
  the criterion asked for at most a third of 235 s, which is 78 s. The remaining cost is one `awk`
  per graded unit for `plan_state`, which §3 rules out, plus roughly 14 externals of region and
  `git ls-files` work per build and 0.28 s of driver startup per invocation. Recorded as a miss
  rather than re-priced, and the threshold was a figure chosen before the measurement existed.
- AC4 — `check-unattended.sh` — MET. `bash tools/unattended/run-unattended-gates.sh --checks`
  reports `ok    kit gate    187s`, so the leg exits 0 and check 30's `_pv_seen` liveness assertion
  is satisfied over the same population. The leg went 305 s to 187 s, a 118 s cut.
- AC5 — `run-gates.sh` — MET. `gates GREEN — 39/39 legs passed (7 skipped) (39 held: kit
  selftests, GATE_SELFTESTS=1 runs them)`, 645 s. The seven skips are all `unchanged vs main`
  guards. THREE legs redded on the way there and each was a real obligation rather than noise:
  the new build README was named by no row in `memory/project/readme-contract.txt` (bound, not
  exempted); three `DECISIONS.md` rows ran past the 300-char index cap and the fixture ids in the
  table above were ids cited and never defined; and `drift-audit records` refused a CLOSED spec
  with no product commit until the work was committed.

### The budget, after

```
ok    kit gate                         187s
      OVER BUDGET  kit gate took 187s against a declared 120s ceiling — fix it or raise the ceiling
ok    playbook validity gate            55s
ok    skill wiring                       2s
----
unattended gates RED — 3 ran on demand, 1 over budget
```

`--checks` exits 1 on that breach, which also settles a question the base run left open: the first
reading was taken through a `tail` pipe, so its exit 0 was the pipe's and not the script's. The
ceiling still binds and is still missed, by 67 s.

The driver suite's own ceiling was missed too, at 2103 s against `BUDGET_driver_selftest=970`. That
ceiling is a node `d` figure and this is node `a`. NOT MEASURED DIRECTLY, and said so: separating
node speed from this change needs a base run of the same suite, which was not done. The supporting
arithmetic is that the `kit gate` leg costs 70 s on node `a` with check 30 removed against 28 s
recorded on node `d`, a 2.5x ratio, and 906 s x 2.5 is 2265 s against the 2103 s measured. That is
consistent with node speed and inconsistent with a cost regression, but it is a derivation.

Because AC3 missed, the build README's parked change-scoping of check 30 is reopened by the rule the
spec's F3 states: the leg is still expected above `BUDGET_kit_gate` after this unit.
