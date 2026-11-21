# TOOL-dPlacedRequest-98 — the fenced-landing arms fail, never skip, when their fixture fails

**Status:** CLOSED · rev-2 · 2026-11-21 · node d · Tier-2 · base 2b4cc0bd · streams tooling · order 37

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-21-build-TOOL-dPlacedRequest-1-runlog-d54afa03.md](../build/2026-11-21-build-TOOL-dPlacedRequest-1-runlog-d54afa03.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 TOOL-dPlacedRequest-95 TOOL-dPlacedRequest-96 TOOL-dPlacedRequest-97 TOOL-dPlacedRequest-99 TOOL-dPlacedRequest-100 |
| [2026-11-21-build-TOOL-dPlacedRequest-98-1-acceptance-ledger.md](../build/2026-11-21-build-TOOL-dPlacedRequest-98-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-build-TOOL-dPlacedRequest-98-deviation-733.md](../build/2026-11-21-build-TOOL-dPlacedRequest-98-deviation-733.md) | deviation | — |
| [2026-11-21-build-TOOL-dPlacedRequest-98-red-fix-34.md](../build/2026-11-21-build-TOOL-dPlacedRequest-98-red-fix-34.md) | red-fix | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-95-audit-fold-text-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-95-audit-fold-text-brief.md) | research | TOOL-dPlacedRequest-95 TOOL-dPlacedRequest-99 |
| [2026-11-20-prompt-TOOL-dPlacedRequest-98-closing-review-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-98-closing-review-spec-brief.md) | research | — |
| [2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-95 TOOL-dPlacedRequest-96 TOOL-dPlacedRequest-97 TOOL-dPlacedRequest-99 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build, round 2
(`memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md`),
confirmed item **H2** at HIGH, finding id 5, and its exit promoted it to this unit. The lander suite's
fenced-landing block, arms 42 to 54, runs only when `write_fence_fixture` acquires a lease through the
real driver, which reads the live `fleet.toml` and the ambient `GOV_NODE`. When that acquire fails the
block prints a skip, sets no failure, and the suite still ends `all cases ok`, because it pins no
assertion floor. A broken `--lease acquire`, a roster without the fixture's user, or an adopter tree
whose registry lacks it turns every fenced-landing arm into a silent pass. This unit makes the fixture
read its own registry, fails the block when a fixture step fails, and pins the suite's floor.

## 2. Scope (IN)

- **S1** — H2, closed by the record's fix, which the skeptic judged SOUND. In `tools/push-main.test.sh`:
  the fenced-landing fixture reads a registry of its own, never the live one, and runs with
  `GOV_NODE` unset; its `else` branch is a failure whenever the unattended kit and a python launcher
  both resolved and `write_fence_fixture` still failed, the skip kept only for a lander with no kit
  beside it or no python, its text naming 42-54; and the suite counts its `ok` rows, prints the agreed
  `PASS (<n> assertions)` line and compares it to a `FLOOR_ASSERTIONS` pin, so the `push-main
  self-test` leg reds when a block's arms stop running. The compare runs only where no dependency
  skip fired, by the rule of §4, so an adopter whose install lacks a sibling kit is not red on a
  healthy lander. The `push-main self-test` row of `tools/run-gates/selftest-budgets.txt` is re-priced
  for the block this unit makes run, and its ceiling compared, by §4. The suite's row leaves
  `memory/project/testsuite-count-waivers.txt`, which the testsuite counts leg reds as stale once the
  suite complies. The class rule the record states for the `harness arms` leg, that a fixture skip is
  admissible only when the dependency is genuinely absent, sits in another write set, so it lands as a
  bug-class checklist entry: a section added to `memory/gotchas/fixture-inherits-ambient-machine-state.md`.
  Observed by AC1.

## 3. Non-goals (OUT)

- No change to `tools/push-main.sh` or to the driver: the arms' subject is unchanged, only the fixture
  under them and the suite's accounting move.
- No change to `harness arms (fail branches armed or pinned)`'s checker: the class rule is a checklist
  entry here, per the brief's rule for a left-shift that fits no single write set.
- No re-numbering of arms 42 to 54 and no change to what each asserts.

### Edges

- **consumes-from** external — the fenced-landing block this build's fenced-push and re-fence units
  wrote and CLOSED; this unit changes its fixture and the suite's accounting, and those specs stay
  frozen

## 4. Design

### The fixture's own registry

`write_fence_fixture` builds, under `$FX` and outside both clones, a scratch kit tree holding copies of
the kit directories the driver's lease verbs resolve beside it, the unattended kit and the playbook kit
among them, and writes the playbook copy's `fleet.toml` as two rows: `daily-agent` at tag `a` and
`agent5` at tag `b`. The launcher each clone commits at `<prefix>unattended/unattended.sh` execs that
copy rather than the live driver, so `resolve_fleet_tag` finds the scratch registry by its kit probe
and never the tree's. The launcher is `exec env -u GOV_NODE bash "<the copy>" "$@"`, so every driver
call made through it runs with `GOV_NODE` unset: the fixture's own acquire, the lander's fence reads
in arms 42 to 54, and the pre-push hook's take-over. The unset lives in that one place, inside what
`write_fence_fixture` writes, so the function is hermetic when called alone, as AC1 calls it, and the
block saves and restores nothing beyond the `USERNAME` and `CLAUDE_CODE_SESSION_ID` it already does.

### The branch and the count

```
if [ -n "$_fn_k" ] && [ -n "$_py_arms" ]; then
  if write_fence_fixture; then ...arms 42-54 as at the base...
  else bad "42-54 the fenced-push fixture could not be made: <the acquire's own line>"; fi
else
  echo "  skip — 42-54 no unattended kit beside this lander, or no python launcher, ..."
fi
```

`ok()` gains a counter beside `bad()`'s flag; the suite's last lines print `PASS ($n assertions)` when
`fail` is 0, and keep the existing `all cases ok` and `FAILURES` lines.

The floor rule, because the suite ships to adopters as the `push-main self-test` gate leg of a kit
declaring `requires = []`, and about a dozen of its blocks skip when a sibling kit or python is
absent (`tools/push-main.test.sh@56c95b47:575` is the first): every dependency skip, the 42-54
branch's included, sets `skipped=1` beside its `skip —` line. The suite compares `$n` with
`FLOOR_ASSERTIONS`, on its own anchored line, only where `skipped` is 0, the install where every block
runs; there a count below the pin is a failure. Where a dependency skip fired it prints `floor not
compared — a dependency skip fired` and takes its verdict from `fail` alone. The pin is the count the
suite prints with every block running, PINNED with that node and date in a comment, and every later
unit that adds an `ok` row that runs there raises it. A skip is admissible only for a dependency
genuinely absent, the class rule this unit records, so in gov, where every kit sits beside the lander,
a block that stops running either fails or drops the count below the pin.

### The budget row

The `push-main self-test` row (`tools/run-gates/selftest-budgets.txt@25b27c00:114`) is a PINNED proxy
of 688 s (PINNED, that row) read on 2026-10-28, before arms 42 to 54 landed, and this unit makes them
run. It is re-priced in its own proxy shape, never by a suite run inside the pass
(`doc.build-method#m6-passes-commits-parallelism`): the row's 688 s (PINNED, that row), plus each
fixture making in the block at the row's 14.7 s and each `--land` at its 65.0 s, the counts DERIVED by
`grep` over the block at build time, x1.5. Its note names the counts, this unit and that it is re-priced
from the main loop's first reading of the leg alone, as its peers' notes do. The leg's `ceiling` in
`tools/gate-legs.json` is 580 s (PINNED, at the base), and a hang bound is compared with a reading, never
with a budget. Where the proxy reading exceeds that ceiling, the acceptance ledger says so, and the
move is made from the main loop's measured reading of the leg alone: the `ceiling` edited, the reading
recorded by `GOV_NODE=<tag> derive-ceilings.py --write --observed 'push-main self-test=<s>' --how
'<direct CLI, base, node>'`, then `pass_legs.py --apply` and the `last-audit` re-stamp of
`memory/guides/SESSION-KICKOFF.md`. That move is the main loop's inline fix at its pass-leg run, never
this pass's, because only the main loop runs the suite.

Cited at the base: the guard is `tools/push-main.test.sh@56c95b47:1668`, the fixture
`tools/push-main.test.sh@56c95b47:1639`, the skip branch `tools/push-main.test.sh@56c95b47:1849`; the
fixture's acquire reads the registry through `tools/unattended/lib-unattended.sh#resolve_fleet_tag`,
which asks `tools/playbook/render_playbook.py#read_fleet_tag` with no fleet path, so the registry
beside the playbook kit answers; the helpers are `tools/push-main.test.sh@56c95b47:199` and the next
line.

### The checklist entry

A section `## It bit again in the lander's fenced-landing block` in
`memory/gotchas/fixture-inherits-ambient-machine-state.md`, in the shape of its four earlier sections:
the live registry and the ambient `GOV_NODE` under a fixture that looked hermetic, the skip that hid
it, and the rule that a skip is admissible only when the dependency is absent, never when a fixture
step failed.

### Files touched (estimate)

- `tools/push-main.test.sh`: the fixture's kit tree, the launcher's `GOV_NODE` unset, the branch, the
  `skipped` flag on each dependency skip, the counter, the count line and the floor
- `tools/run-gates/selftest-budgets.txt`: the `push-main self-test` row re-priced
- `memory/project/testsuite-count-waivers.txt`: the suite's row removed
- `memory/gotchas/fixture-inherits-ambient-machine-state.md`: the section
- the playbook kit's version carrier, moved once by the kit-epoch rule if the kit-epoch leg counts the
  suite as shipped bytes

### Alternatives rejected

- **Set `GOV_NODE` per clone to a planted tag.** The record offers it; the tag must still be a tag of
  the live registry, so an adopter whose registry carries other tags still loses the block.
- **Keep the skip and add only the floor.** The floor reds a block that stopped running, but a skip
  that names a fixture failure as an absent dependency still misleads the reader of the output.

## 5. Production-readiness checklist

- security — none: a test fixture under the suite's own scratch directory.
- perf / scale — one copy of two kit directories per fixture made, three per run, seconds; the block
  this unit makes run costs its landings, re-priced in §4's budget row.
- error / empty / loading states — a fixture that cannot be made is a named failure, with the acquire's
  own output.
- observability — the suite prints its count, so the testsuite counts leg reads it.
- risks — the copied kit tree misses a sibling the driver resolves for its lease verbs, and the acquire
  fails; that is now a red naming the cause, not a silent pass. The block's landings may take the leg
  past its 580 s ceiling (PINNED, at the base), killed rather than red; §4 routes that ceiling to the main loop's reading.
- testing — AC1's probe and the arm in §7.
- migration — none.
- user docs — none: no page under `help/` names the lander's suite.

## 6. Acceptance criteria

- **AC1** — When a scratch worktree of the tip has its `tools/playbook/fleet.toml` edited so no row
  names `daily-agent`, and a probe evaluates that worktree's `write_fence_fixture`, cut from the lander
  suite by `awk` as the card-store fixture evaluates the engine's resolvers, with the
  suite's variables set, `USERNAME=daily-agent` and a `GOV_NODE` exported naming no tag, the function
  returns 0 and the lease it acquired names fleet tag `a`; and over the tip,
  `grep -c '^FLOOR_ASSERTIONS=[0-9]*$' tools/push-main.test.sh` prints 1 and
  `grep -cx 'tools/push-main.test.sh' memory/project/testsuite-count-waivers.txt` prints 0; and a probe
  evaluating the suite's closing compare, cut by `awk`, with `n` one below the pin prints a `FAIL` line
  under `skipped=0` and `floor not compared` under `skipped=1`; and
  `grep -c 'TOOL-dPlacedRequest-98' tools/run-gates/selftest-budgets.txt` prints 1.
  Red when: the fixture reads the live registry or the ambient `GOV_NODE`, or the floor is compared on
  a partial install; the suite at 2b4cc0bd4 is that break, and there the same probe's function returns
  1 because the acquire is refused, with no floor line, no compare to cut, the waiver row present and
  the budget row naming no unit of this build, its RED-first reading.
  fixture: the scratch worktree and the fixture's clones, built by the probe; the tree holds none.
  cost: one fixture made, about a minute on node d (PINNED, 2026-11-20, an estimate from the block's
  three makings).

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `push-main self-test` · `every held leg is budgeted, every budget row resolves` · `recall floor` · `recall floor arms` · `testsuite counts (every bar self-test prints one)` · `harness arms (fail branches armed or pinned)` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates`

New arm: tools/push-main.test.sh · covers AC1 · the fixture's registry with daily-agent renamed, which the suite at 2b4cc0bd4 answers with the skip and all cases ok · FLOOR_ASSERTIONS pinned at the count the suite prints with every block running, compared only where no dependency skip fired

## 8. Open questions

- **F1 — Which registry does the fenced-landing fixture read?** (a) Its own: a scratch kit tree under
  `$FX` holding copies of the kits the driver resolves, its playbook copy's `fleet.toml` written with the
  fixture's two rows. (b) The live one, with `GOV_NODE` set per clone to a tag the live registry holds.
  (c) The live one as today, with only the skip turned into a failure. (b) still fails in an adopter
  whose registry carries other tags, the record's third case; (c) leaves cases 2 and 3 red rather than
  silent but never green. (a) satisfies all three cases the record names and adds no dependency, no
  public surface and no carrier change. RESOLVED (agent, 2026-11-20, delegated): (a), the record's first
  option, judged SOUND by the skeptic; the feature-rich survivor of the vetoes of
  `doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft, promoted from the closing diff review round 2, item H2 (HIGH,
  finding id 5), by its exit's disposition.
- rev-2 · 2026-11-20 · S1 · §4 · AC1 · §5 · §7 · folded
  2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit: finding id 6 (M5), the `GOV_NODE` unset moved
  into the fixture's launcher so `write_fence_fixture` is hermetic alone, as AC1 calls it; finding ids
  22 and 30 (H3), the floor compared only where no dependency skip fired, the rule stated in §4 and
  observed by AC1; finding id 25 (M14), the `push-main self-test` budget row re-priced as a proxy and
  its 580 s ceiling (PINNED, at the base) routed to the main loop's measured reading.
- rev-2 · 2026-11-20 · §4 · §5 · §8 · §9 · editorial, by
  2026-11-20-prompt-TOOL-dPlacedRequest-95-audit-fold-text-brief: each folded duration carries its mark
  on its own line, and each build-method section is cited by its alias tag.

## 10. Reuse audit

The seam extended is the suite's own `write_fence_fixture` and its `ok` and `bad` helpers in
`tools/push-main.test.sh`; the floor reuses the agreed count shape `tools/check-testsuite-counts.sh`
already grades, and the registry is the playbook kit's own reader found by its own probe, pointed at a
copy. `python tools/codebase-map/reuse_lookup.py "test fixture reads its own fleet registry instead of
the live one"` ranked name stems only, `read_fleet` among them, which is the reader the copy keeps. The
recall query below returned the round-2 record's H2 and the class record this unit extends; none
disagrees with the source read above.

Recall terms used: push-main.test.sh write_fence_fixture fleet.toml GOV_NODE skip all cases ok FLOOR_ASSERTIONS testsuite-count-waivers fenced landing arms ambient
