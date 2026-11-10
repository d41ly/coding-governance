# TOOL-aSmoothedDispatch-5 — the spec-token checker grades one named spec, so a spec writer can run it over its own

**Status:** CLOSED · rev-1 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 5 · advances TOOL-dFairHearing-54

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-build-TOOL-aSmoothedDispatch-1-1-acceptance-ledger.md](../build/2026-11-10-build-TOOL-aSmoothedDispatch-1-1-acceptance-ledger.md) | journal | TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-6 TOOL-aSmoothedDispatch-7 TOOL-aSmoothedDispatch-8 TOOL-aSmoothedDispatch-9 |
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-1-brief.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-1-brief.md) | research | TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-6 |
| [2026-11-10-review-TOOL-aSmoothedDispatch-1-closing-diff-round1.md](../reviews/2026-11-10-review-TOOL-aSmoothedDispatch-1-closing-diff-round1.md) | diff-review | TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-6 TOOL-aSmoothedDispatch-7 |

<!-- /gen:spec-records -->

## 1. Goal

A spec writer cannot run the spec-token check over the spec it just wrote, so every token miss costs a
main-loop round (TOOL-dFairHearing-54). This unit gives `tools/check-spec-tokens.py` a `--spec <path>`
scope that grades exactly one spec, tracked or not. The role-gate arm of `tools/hooks/scratch-guard.js`
already admits that scoped run to `gov-spec-writer` and still refuses the whole-tree leg, and this unit
pins both verdicts in the hook's suite.

## 2. Scope (IN)

- **S1** — `main` in `tools/check-spec-tokens.py` reads `--spec <path>`. It refuses with exit 2 and a
  `spec-tokens: REFUSING` line when the value is missing, when the path is not under
  `memory/builds/<slug>/spec/` with a `.md` suffix, when no file exists there, or when the file is not a
  live spec. Observed by AC3.
- **S2** — under `--spec`, the graded live population is that one file, read from disk whether or not
  git tracks it. Observed by AC1.
- **S3** — under `--spec`, every printed HIT and NEAR row names the scoped file. The carries and packet
  joins do not run, and each prints its report line saying so. Stale waiver rows and stale size
  high-water rows are not reported. One `scope ·` line names the file and what was skipped. Observed
  by AC2 and AC5.
- **S4** — under `--spec`, the hands-off join's uid map reads every live spec on disk under the scoped
  spec's own `spec/` folder, tracked or not, so a hand-off to a sibling still joins. Observed by AC4.
- **S5** — a run with no `--spec` grades exactly as before and prints no `scope ·` line. Observed by
  AC6.
- **S6** — `tools/hooks/scratch-guard.test.sh` gains the spec-token leg in its fixture manifest and three
  role-gate rows. `gov-spec-writer` running the checker with `--spec` exits 0 with an empty stderr. The
  same role running the bare leg exits 2 naming `G1 leg`, and its self-test suite exits 2 naming
  `G3 suite`. Observed by AC7.
- **S7** — the checker's module docstring names the scope and the joins it skips. Observed by AC8.

## 3. Non-goals (OUT)

- No change to `tools/hooks/scratch-guard.js`. Its role-gate arm already admits a scoped variant of a
  leg, and the probe in §4 shows it. Closing that ceiling is a different unit's work.
- No change to `gov-spec-writer`'s allowlist (`.claude/roles.json:61-69`,
  `tools/roles/house/policy.toml:27`). Allowlisting the leg would admit the whole-tree run, which the
  brief's acceptance 5 says must stay refused.
- No check that the scoped spec is the one the calling agent wrote. The hook holds no authorship
  record, and the run is read-only, so naming any one spec costs nothing a guard protects.
- No change to the role prompt. `tools/roles/agents/gov-spec-writer.agent.md:36` still says the writer
  may run only the hygiene gate and the lexicon. Telling the writer to run `--spec` is a separate
  document, so it is a separate unit, and this one only advances the ask.
- No change to the bar's whole-tree spec-token leg, and no `--build` or other scope. Unit
  TOOL-aSmoothedDispatch-4 decides its own scoping.
- No `help/` page. The checker ships to no adopter (`tools/govkit/registry.toml:226-233`).

### Edges

- **hands-off** external — the prompt line telling `gov-spec-writer` to run
  `python tools/check-spec-tokens.py --spec <its spec>` before it returns, in the writer's role prompt
  and the SPEC stage of `tools/workflows/unattended-build.js` (open ask TOOL-aDeferredBar-6). Without it
  the flag exists and the hook admits it, but no writer is told to use it.

## 4. Design

### What the tree does today, verified at `ae6735c1`

| Fact | Where |
|---|---|
| The leg's argv is the checker with no argument. | `tools/gate-legs.json:1757` |
| The role-gate arm refuses a G1 leg only on an exact word-for-word argv match. | `tools/hooks/scratch-guard.js:1373-1379` |
| A scoped variant of a leg with an extra argument passes the arm, a stated ceiling. | `tools/hooks/scratch-guard.js:122-127` |
| The hook's suite already pins scoped variants as allowed (`G-AC2` rows). | `tools/hooks/scratch-guard.test.sh:1229-1237` |
| The checker reads its spec population from `git ls-files` only. | `tools/check-spec-tokens.py:556-557`, `:1544-1558` |
| The checker reads no argument but `--list` and `--legs-for`. | `tools/check-spec-tokens.py:1529-1538` |

Probe, run 2026-11-10 against the repo's own `.claude/roles.json`: hook payloads with
`agent_type` set to `gov-spec-writer` were piped to `node tools/hooks/scratch-guard.js`. The checker with
`--spec <path>` exited 0 with an empty stderr. The bare checker exited 2, naming row `G1 leg` and the
leg `spec tokens (a spec's own names resolve)`. The checker's self-test suite exited 2, naming
`G3 suite`. So the hook is not the blocker. The real blocker has two halves. First, the checker has no
scope, so a writer could only run the whole-tree leg, which is refused. Second, a writer never commits,
so its spec is untracked and the checker would not grade it even unscoped.

### The scope (S1, S2)

`main` parses `--spec` after the `--legs-for` branch and before the population walk. The value is
resolved against the process cwd, made relative to the toplevel and spelled with forward slashes. It
must match the population regex `main` already uses at `tools/check-spec-tokens.py:1545`, and the file
must exist. Its text must match `LIVE` (`:365`). On any failure, `main` prints one
`spec-tokens: REFUSING — --spec <value>: <reason>` line and returns 2. Exit 2 is distinct from a hit's
exit 1, so a caller can tell a wrong scope from a spec with hits.

Under the scope, `specs` is `[path]` and `unretired` is `[path]` unless the file is WONTDO. `frozen` is
0. `files`, the tracked set, is unchanged, so the paths and cites joins still check against what git
tracks.

### What the scope filters and skips (S3)

| Join or report | Under `--spec` | Why |
|---|---|---|
| legs, paths, cites, bar, guards, claims, covers, source, ac-order | run over `[path]` | per-spec joins |
| hands-off | runs over `[path]`, uid map as S4 says | the target is a sibling |
| size | runs over `[path]`, its stale rows dropped | one file cannot show a row is stale |
| supersede, arm-labels | run over `[path]` | per-spec joins |
| carries, packet | not run, line reads `skipped under --spec` | their population is every chain spec or run, never one file |
| waiver STALE rows | not reported | a one-file run cannot see the hit a row waives elsewhere |
| HIT and NEAR rows | kept only where the row's file is `path` | a scoped run reports on its scope |

Waivers still apply to hits, so a waived hit stays waived. One line follows the first summary line:

```
spec-tokens: scope · --spec <path> · <tracked|untracked> · not run: carries, packet · stale rows not reported
```

### The sibling map (S4)

`read_spec_uids(root, specs)` (`tools/check-spec-tokens.py:806`) is called over every `.md` under
`memory/builds/<slug>/spec/` on disk, at any depth, whose text matches `LIVE`, with `path` included. A
hand-off target in the same build is then found when a concurrent writer has not committed it either.
A target in no live spec on disk stays silent and counted, as today.

### The hook's rows (S6)

`write_gate_manifest` (`tools/hooks/scratch-guard.test.sh:1176-1181`) gains a sixth leg,
`{"name":"spec tokens (a spec's own names resolve)","argv":["python","{prefix}/check-spec-tokens.py"]}`.
Three `run_role_bash` rows join the `G-AC1` and `G-AC2` blocks:

- `gov-spec-writer` runs `python kit/check-spec-tokens.py --spec memory/builds/x/spec/y.md`, which
  allows with an empty stderr.
- `gov-spec-writer` runs `python kit/check-spec-tokens.py`, which denies naming `G1 leg` and the leg
  name.
- `gov-spec-writer` runs `bash kit/check-spec-tokens.test.sh`, which denies naming `G3 suite`.

The other rows' verdicts do not move, because no row runs that leg's argv.

### Files touched (estimate)

`tools/check-spec-tokens.py` · `tools/check-spec-tokens.test.sh` · `tools/hooks/scratch-guard.test.sh`

### Rollout

The checker is gov-internal and has no kit version. The hooks kit's version moves through the lander's
`mint`, never by hand. TOOL-aSmoothedDispatch-4 may also edit `tools/check-spec-tokens.py` if it picks a
checker flag. In that case the two units share a write set and build one after the other, and this
unit's edits to `main` come first.

### Alternatives rejected

- **Allowlist the leg for `gov-spec-writer`.** This admits the whole-tree run, which acceptance 5 of
  the brief says stays refused, and the writer's spec is still untracked and ungraded.
- **A filter on the whole-tree output.** The writer would pay the full run, and the untracked spec
  would still not be graded.
- **A new hook arm naming the scoped run.** It changes no verdict, since the arm already admits it.
  The suite rows pin the same fact without new hook code.

## 5. Production-readiness checklist

- security — no write path. The checker only reads, and the hook's verdicts do not change. The scope
  is validated once, at `main`, against the population regex.
- perf / scale — a scoped run grades one spec and skips the carries and packet joins, which read
  every chain spec's history and run each live chain's packet instrument.
- error / empty / loading states — a malformed, absent, out-of-tree or terminal scope exits 2 with its
  reason. A scoped live spec always grades one file, so the run never passes on an empty population.
- observability — the `scope ·` line names the file, whether git tracks it, and what did not run.
- risks — a writer may read a scoped green as a whole-tree green. The scope line and the hands-off say
  otherwise, and the bar still grades the whole tree.
- testing — the arms declared in §7, observed RED then GREEN at the close, and the fixture probes in §6.
- migration — none. An unscoped run is unchanged.
- user docs — N/A: the checker ships to no adopter (`tools/govkit/registry.toml:226-233`). The
  docstring change is S7.

## 6. Acceptance criteria

- **AC1** — In a scratch repository made like the checker suite's `scratch` fixture, add an UNTRACKED
  live spec whose §7 leg line names a leg the manifest does not declare. Running
  `python tools/check-spec-tokens.py --spec <that spec>` there exits 1, and its output carries
  `[leg]` and the spec's path.
  Red when: `--spec` is ignored, so only tracked specs are graded and the run exits 0.
- **AC2** — In the same repository, with a hit planted only in the TRACKED spec, a `--spec` run over a
  clean untracked spec exits 0. Its output carries the `scope ·` line and `skipped under --spec`, and
  it does not carry the tracked spec's path.
  Red when: the HIT and NEAR rows are not filtered to the scope, or the carries join still runs.
- **AC3** — `python tools/check-spec-tokens.py --spec` exits 2 with `REFUSING` in four cases: with no
  value, with a path outside the builds' `spec/` folders, with a path to no file, and with a path to a
  CLOSED spec.
  Red when: any of the four is graded, or exits 0 or 1.
- **AC4** — In the scratch repository, an untracked live spec carries a `**hands-off**` bullet naming
  an untracked live sibling in the same `spec/` folder, and its payload token is absent from that
  sibling. The `--spec` run over the first spec exits 1 with a `[handoff]` hit. Once the token is added
  to the sibling, it exits 0.
  Red when: the uid map reads tracked specs only, so the bullet is silent.
- **AC5** — With a waiver row in `memory/project/spec-token-waivers.txt` that no spec produces, the
  unscoped run exits 1 with a `STALE` line. A `--spec` run over a clean spec exits 0 with no `STALE`
  line.
  Red when: stale waiver rows are still reported under the scope.
- **AC6** — `python tools/check-spec-tokens.py` with no `--spec`, in the checker suite's `scratch`
  fixture, prints no `scope ·` line and reports the same live-spec count as before.
  Red when: the scope logic changes an unscoped run.
- **AC7** — Piping a Bash payload whose `agent_type` is `gov-spec-writer` to
  `node tools/hooks/scratch-guard.js`, with the fixture manifest carrying the spec-token leg, gives
  three results. The checker with `--spec <path>` exits 0 with an empty stderr. The bare checker exits
  2 naming `G1 leg`. The checker's self-test suite exits 2 naming `G3 suite`.
  Red when: `checkGateLeg` matches a leg by prefix, so the scoped run is refused, or the leg is
  allowlisted for the role, so the bare run is admitted.
- **AC8** — `grep -n -- "--spec" tools/check-spec-tokens.py` finds the flag in the module docstring,
  above the first `import`, with the joins it skips named.
  Red when: the docstring does not name the scope.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `memory-hygiene self-test` · `build-index selftest` · `policy fixtures` · `scratch-guard self-test` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `memory hygiene` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers`

New arm: tools/check-spec-tokens.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the `--spec` arms, run through `ARM_ARGS`, read RED against the checker at `ae6735c1`, which ignores the flag · `FLOOR_ASSERTIONS` moves, the close confirms it

New arm: tools/hooks/scratch-guard.test.sh · covers AC7 · the three `gov-spec-writer` rows, the allow row staged by matching `checkGateLeg` on a prefix and the deny rows by allowlisting the leg in the fixture index · none

The leg line names every leg whose guard a path in Files touched trips, except those the checker
counts as broad. This spec's author may run only `memory hygiene` and the lexicon, so the main loop
runs every other leg and both arms at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft from the brief
  `2026-11-10-prompt-TOOL-aSmoothedDispatch-1-brief`, item 5, grounded at `ae6735c1`. The hook probe
  found the role-gate arm already admits a scoped run, so the mechanism moves to the checker's scope.
  The roster's wording for this unit names scratch-guard, and the hook's change is its suite rows.

## 10. Reuse audit

The seam is `main` in `tools/check-spec-tokens.py` (`:1529`). The flag follows `--legs-for`'s argv read,
and the population regex at `:1545` is reused, not copied. S4 reuses `read_spec_uids` (`:806`). The
suite arms reuse `scratch` and `arm` with `ARM_ARGS` (`tools/check-spec-tokens.test.sh:336-384`), and the
hook rows reuse `run_role_bash` (`tools/hooks/scratch-guard.test.sh:1186-1202`). `reuse_lookup.py "grade
one spec file with the spec token checker"` ranked only generic name stems such as `check` and
`resolve_prefix_token`, so no other seam fits. Recall ranked the record of TOOL-aOrientedCast-11, which
set the writer's allowlist, and TOOL-dFairHearing-54 and TOOL-aDeferredBar-6. Two build returns record a
writer refused on the bare leg (dOrderedCharter token-fix, dDeclaredLoop-68). The records and the code
disagree in one place. The brief says the hook's allowlist must be extended, but the probe in §4 shows
the hook already admits the scoped run.

Recall terms used: `python tools/memory-recall/query.py "how can a spec writer role agent run the spec token check on the one spec it wrote" --terms "spec-tokens checker scoped one spec writer role-gate allowlist scratch-guard leg untracked"`
