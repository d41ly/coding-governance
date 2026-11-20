# TOOL-dPlacedRequest-98 — the fenced-landing arms fail, never skip, when their fixture fails

**Status:** DEFERRED · rev-1 · 2026-11-20 · node d · Tier-2 · base 95c3103a · streams tooling · order 37

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-prompt-TOOL-dPlacedRequest-98-closing-review-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-98-closing-review-spec-brief.md) | research | — |

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
  self-test` leg reds when a block's arms stop running. The suite's row leaves
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
and never the tree's. The block saves `GOV_NODE` beside `USERNAME` and `CLAUDE_CODE_SESSION_ID`,
unsets it for the block, and restores it after, as it already restores those two.

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
`fail` is 0, compare `$n` with `FLOOR_ASSERTIONS` on its own anchored line, and keep the existing
`all cases ok` and `FAILURES` lines. The floor is the count the suite prints on the build's node with
every block running, PINNED with that node and date in a comment, and every later unit that adds an
`ok` row raises it.

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

- `tools/push-main.test.sh`: the fixture's kit tree, the `GOV_NODE` save and restore, the branch, the
  counter, the count line and the floor
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
- perf / scale — one copy of two kit directories per fixture made, three per run; seconds against the
  leg's ceiling.
- error / empty / loading states — a fixture that cannot be made is a named failure, with the acquire's
  own output.
- observability — the suite prints its count, so the testsuite counts leg reads it.
- risks — the copied kit tree misses a sibling the driver resolves for its lease verbs, and the acquire
  fails; that is now a red naming the cause, not a silent pass.
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
  `grep -cx 'tools/push-main.test.sh' memory/project/testsuite-count-waivers.txt` prints 0.
  Red when: the fixture reads the live registry or the ambient `GOV_NODE`; the suite at 95c3103ad is
  that break, and there the same probe's function returns 1 because the acquire is refused, with no
  floor line and the waiver row present, its RED-first reading.
  fixture: the scratch worktree and the fixture's clones, built by the probe; the tree holds none.
  cost: one fixture made, about a minute on node d (PINNED, 2026-11-20, an estimate from the block's
  three makings).

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `push-main self-test` · `recall floor` · `recall floor arms` · `testsuite counts (every bar self-test prints one)` · `harness arms (fail branches armed or pinned)` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates`

New arm: tools/push-main.test.sh · covers AC1 · the fixture's registry with daily-agent renamed, which the suite at 95c3103ad answers with the skip and all cases ok · FLOOR_ASSERTIONS pinned at the count the suite prints with every block running

## 8. Open questions

- **F1 — Which registry does the fenced-landing fixture read?** (a) Its own: a scratch kit tree under
  `$FX` holding copies of the kits the driver resolves, its playbook copy's `fleet.toml` written with the
  fixture's two rows. (b) The live one, with `GOV_NODE` set per clone to a tag the live registry holds.
  (c) The live one as today, with only the skip turned into a failure. (b) still fails in an adopter
  whose registry carries other tags, the record's third case; (c) leaves cases 2 and 3 red rather than
  silent but never green. (a) satisfies all three cases the record names and adds no dependency, no
  public surface and no carrier change. RESOLVED (agent, 2026-11-20, delegated): (a), the record's first
  option, judged SOUND by the skeptic; the feature-rich survivor of BUILD-METHOD M3's vetoes.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft, promoted from the closing diff review round 2, item H2 (HIGH,
  finding id 5), by its exit's disposition.

## 10. Reuse audit

The seam extended is the suite's own `write_fence_fixture` and its `ok` and `bad` helpers in
`tools/push-main.test.sh`; the floor reuses the agreed count shape `tools/check-testsuite-counts.sh`
already grades, and the registry is the playbook kit's own reader found by its own probe, pointed at a
copy. `python tools/codebase-map/reuse_lookup.py "test fixture reads its own fleet registry instead of
the live one"` ranked name stems only, `read_fleet` among them, which is the reader the copy keeps. The
recall query below returned the round-2 record's H2 and the class record this unit extends; none
disagrees with the source read above.

Recall terms used: push-main.test.sh write_fence_fixture fleet.toml GOV_NODE skip all cases ok FLOOR_ASSERTIONS testsuite-count-waivers fenced landing arms ambient
