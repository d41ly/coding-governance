# TOOL-aRepatriatedFork-49 — the push bar takes no manifest or interpreter from the environment

**Status:** CLOSED · rev-2 · 2026-09-30 · node a · Tier-2 · base ce8a78f5 · streams tooling · order 21 · ratified 2026-09-30

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-30-build-TOOL-aRepatriatedFork-49-1-acceptance-ledger.md](../build/2026-09-30-build-TOOL-aRepatriatedFork-49-1-acceptance-ledger.md) | journal | — |
| [2026-09-30-prompt-TOOL-aRepatriatedFork-49-build-brief.md](../prompts/2026-09-30-prompt-TOOL-aRepatriatedFork-49-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review's round 2 found item H1, and M4 promoted it to this unit. `TOOL-aRepatriatedFork-24`'s
round-1 fold vets the install receipt and the runner the default bar runs. The runner still reads
its leg manifest from `GATE_LEGS` and its python from `GOV_PYTHON`, and it reads an untracked or
ignored manifest file like a tracked one. Each of those lets a RED tracked bar land with `git status`
empty. This unit makes the bar that certifies a default-branch push read only the tracked manifest,
through a python the environment did not name.

## 2. Scope (IN)

- **S1** — The environment's interpreter overrides are dropped beside `GOV_KITROOT`, before the
  vetted `.githooks/gate-env.sh` runs. The dropped set is `GOV_PYTHON` and every exported name ending
  `_PY`, which is the resolver's published per-kit override convention. `gate-env.sh` may declare one
  again, the way it declares `GOV_KITROOT`, and it is vetted before it runs. Observed by AC2 and AC7.
  **Readers:** by name: `.githooks/pre-push`, `tools/run-gates/run-gates.sh` and
  `tools/lib/resolve-python.sh`, whose resolver takes `GOV_PYTHON` as its second candidate.
  by value: the hook's sibling-kit resolver call that finds the runner, and the runner's `PYBIN`,
  which parses the manifest and runs every python leg.
- **S2** — The runner's selection knobs, `GATE_LEGS` and `GATE_REUSE`, are unset before any bar
  that is not labelled STUB runs. A bar labelled STUB keeps them, so the hook's own fixtures still
  drive a runner copy over a fixture manifest. Observed by AC1, AC4 and AC5.
- **S3** — Before the bar runs, the leg manifest the runner reads is vetted with
  `check_reviewed_file`, the one predicate that already vets `gate-env.sh`, the receipt and the
  runner. That manifest is the sibling of the runner's kit directory. A manifest that is not the
  blob tracked at the pushed sha is refused as `bar-refused`. Observed by AC3.
- **S4** — A default-branch push that dropped or unset any S1 or S2 name says so in one stderr line
  before the bar runs, naming each one. Observed by AC1.
- **S5** — The class gets its own arm. Every `GATE_` or `GOV_` name `run-gates.sh` reads through `$` is
  in exactly one of three sets: the names S1 clears, the names S2 clears, or the suite's declared
  inert set, which carries a reason for each member. A name in none reds by name, and so does an S2
  or inert member the runner does not read. The S1 set is exempt from that second half, because it
  also serves the hook's own resolver. Observed by AC6.
- **S6** — The hook's "what this does not close" paragraph names the environment the bar still
  inherits: `PATH`, the language runtimes' own variables such as `PYTHONPATH` and `NODE_OPTIONS`,
  and the leg-level knobs an adopter's own legs read. Observed by AC8.
- **S7 (rev-2)** — The run-log suite's exit table counts the hook's `bar-refused` sites as five.
  It has read three since `baa7289a` added the kit-root refusal, and `07b238ee` added the
  runner-miss refusal, so the `pre-push run-log line` leg this unit names has been red since. This
  unit adds no exit site. Observed by AC9.

## 3. Non-goals (OUT)

- The branch bar. It can only add a refusal to a push that is ungated without it, so an
  environment knob there cannot land a RED default-branch tree.
- Scrubbing the language runtimes' own variables, `PYTHONPATH`, `PYTHONHOME` and `NODE_OPTIONS` (§8 F3).
- The planted `gate-fingerprint.sh` beside a tracked runner, which round 1's fold record leaves as
  main's behaviour. It can only force a full bar, never skip one.
- `tools/push-main.sh`'s own environment. The lander reads the vetted bar record this hook writes.

### Edges

- **consumes-from** `TOOL-aRepatriatedFork-24` — `check_reviewed_file` and the resolved runner
  `GATE_RUNNER` from its S2c. Without them there is no vetted runner whose manifest S3 can name.

## 4. Design

### Evidence

Read at `ce8a78f5`. `tools/run-gates/run-gates.sh` sets
`LEGS_FILE="${GATE_LEGS:-$(dirname "$KITREL")/gate-legs.json}"` and resolves `PYBIN` through
`resolve_python`, whose second candidate is `$GOV_PYTHON`. It runs every leg whose first argv word
is `python` or `python3` under `PYBIN`. The hook passes its whole environment to `$gate`. It unsets
`GOV_KITROOT` and nothing else the runner reads. Its own `resolve_python`, which runs the sibling-kit
resolver that finds the runner, reads `GOV_PYTHON` as well. The runner reuses a green ledger row for
a leg whose input key matches when `GATE_REUSE` is set, and its header says the hook never sets that
knob. The hook never unsets it either.

The runner reads 21 `GATE_` or `GOV_` names through `$`. That count is PINNED at `ce8a78f5`, and
S5's arm re-derives it on every run.

### Mechanism

- **S1.** The existing `unset GOV_KITROOT` becomes `unset $ENV_DROPPED_KNOBS`, where the constant
  holds `GOV_KITROOT GOV_PYTHON`, followed by a loop over `compgen -e` that unsets each exported
  name ending `_PY`. Both happen before `gate-env.sh` is sourced, so only the vetted file can
  declare one again.
- **S2.** A constant, `BAR_SCRUBBED_KNOBS="GATE_LEGS GATE_REUSE"`, is unset after the bar command
  is vetted and after the two runner-miss refusals, unless `bar_class` is `stub`. Keying on the
  label, and not on `GOV_GATE_CMD_TEST`, is deliberate. That escape does not mark the default bar,
  so `GOV_GATE_CMD_TEST=1` with the default bar would otherwise keep a planted manifest under a
  `default` label and a lander marker.
- **S3.** In the same block, the manifest path is derived from `GATE_RUNNER`: its directory's parent,
  or the root when the kit directory is one segment. Where a file exists there,
  `check_reviewed_file` vets it at `main_local`. A tracked file that is missing from the working copy
  is already the dirty-tree refusal.
- **S4.** The names S1 and S2 removed are collected as they go, and the block prints one line when
  the list is not empty.
- **S5.** A block in `.githooks/pre-push.test.sh` derives the runner's `$GATE_*` and `$GOV_*`
  names by grep, reads the two hook constants by `sed`, and joins them against its own inert list.

### Inventory

This unit mints two shell constants in `.githooks/pre-push`, `ENV_DROPPED_KNOBS` and
`BAR_SCRUBBED_KNOBS`, plus one in `.githooks/pre-push.test.sh`, `BAR_INERT_KNOBS`. It mints no
function. `.lexicon.conf` declares no shell-variable cell. Each name follows the hook's existing
upper-case constants, such as `GATE_FULL_MAX_LAG`.

### Files touched (estimate)

- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `.githooks/gate-env.sh`
- `.githooks/pre-push.runlog.test.sh`

### Alternatives rejected

- Refusing the push when `GATE_LEGS` or `GATE_REUSE` is set. It blocks an operator who exported a
  fixture knob in an earlier session, and it buys nothing that unsetting does not (§8 F1).
- Running the bar under `env -i` with an allow-list. Every adopter's own legs would lose their
  environment, and `PATH` would still have to be inherited (§8 F3).
- Vetting `GOV_PYTHON` by shape. A launcher name that is one word still resolves through `PATH`, and
  a path cannot be vetted, because an interpreter is not a file this repository tracks (§8 F2).

## 5. Production-readiness checklist

- security — the unit narrows the push boundary. Every route it closes was reproduced by the round-2
  review, and S6 names the routes it leaves open.
- perf / scale — one `compgen -e` loop, one `git rev-parse` and one `git hash-object`, once per
  default-branch push.
- error / empty / loading states — an untracked manifest is refused with `check_reviewed_file`'s
  message. A missing one reaches the runner, which exits 2 naming it, as it does today.
- observability — S4's line names every knob the push did not honour.
- risks — a node that relies on an exported `GOV_PYTHON` now resolves `python3`, `python` or `py`
  on a default-branch push. If none runs, the bar fails RED naming the resolver. The fix is a
  declaration in `.githooks/gate-env.sh`.
- testing — AC1 to AC8. The arms run the real runner in a scratch repository.
- migration — none. `push-main` declares no kit version, so no carrier moves.
- user docs — `.githooks/gate-env.sh`'s key list gains `GOV_PYTHON`. No `help/` page describes it.

## 6. Acceptance criteria

- **AC1** — A scratch fixture in the pre-push suite tracks a copy of the real runner over a
  `gate-legs.json` holding one RED python leg. When it pushes with `GATE_LEGS` naming an untracked manifest of one
  leg that writes a marker file, the push is refused as `gate-red`, no marker is written, and stderr
  names `GATE_LEGS`.
  Red when: the push lands or the marker exists. The `ce8a78f5` hook lands it.
- **AC2** — When the same fixture pushes with `GOV_PYTHON` naming a planted interpreter that exits
  0 for the red leg and writes a marker, the push is refused as `gate-red` and no marker is written.
  Red when: the push lands or the marker exists. The `ce8a78f5` hook lands it.
- **AC3** — When the fixture tracks the runner and no manifest, and an ignored `gate-legs.json`
  beside the kit holds one green leg that writes a marker, the push is refused as `bar-refused`
  naming `gate-legs.json`, and no marker is written.
  Red when: the push lands or the marker exists. The `ce8a78f5` hook lands it.
- **AC4** — When a direct green run of the fixture's runner has written a ledger row for the red leg
  and the push sets `GATE_REUSE=1`, the push is refused as `gate-red`.
  Red when: the push lands on a reused row. The `ce8a78f5` hook lands it.
- **AC5** — Two controls. With nothing planted, the fixture's push reaches the tracked RED leg and is
  refused as `gate-red`. A bar labelled STUB still honours `GATE_LEGS`, which the existing AC4 arm of
  the pre-push run-log suite drives through a runner copy under `GOV_GATE_CMD_TEST`.
  Red when: the first push lands, or the runlog arm's runner no longer sees its fixture manifest.
  permission: the runlog suite is observed as a slice, the prologue plus its AC4 block.
- **AC6** — The S5 arm passes on the built tree and names its derived knob count. With a
  runner copy carrying an unclassified `${GATE_PLANTED:-}`, the arm reds naming
  `GATE_PLANTED`. With `GATE_LEGS` removed from the copy, it reds naming a stale member.
  Red when: either staged break passes, or the derived set does not contain `GATE_LEGS`.
  figure: DERIVED at observation time.
- **AC7** — When `.githooks/gate-env.sh` is read, its key list names `GOV_PYTHON`, and says it must
  be exported to reach the bar. The hook's bar mutation self-test exits 0 on the built hook, which
  still carries its `set +f` anchor exactly once.
  Red when: the key is undocumented, or the mutation self-test loses its anchor.
- **AC8** — When `git grep -n 'PYTHONPATH' -- .githooks/pre-push` runs, it prints a line in the
  hook's "what this does not close" paragraph, and that paragraph also names `PATH` and
  `NODE_OPTIONS`.
  Red when: the paragraph is unchanged.
- **AC9** — rev-2. When the run-log suite's `EXITS` arm runs as a slice over the built hook, its
  site count and every row's count hold, with `refuse-bar` at five sites.
  Red when: the table still reads three, which the `ce8a78f5` slice fails naming five sites.

## 7. Gates

`pre-push self-test` · `pre-push bar self-test` · `pre-push run-log line` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: `.githooks/pre-push.test.sh` · a real-runner fixture pushed four ways, `GATE_LEGS`, `GOV_PYTHON`, an ignored manifest and `GATE_REUSE`, each landing on the `ce8a78f5` hook · none

New arm: `.githooks/pre-push.test.sh` · the runner's knob set joined against the hook's two constants and the suite's inert list, red on a planted unclassified knob · none

## 8. Open questions

- **F1 — unset the runner's selection knobs, or refuse the push?** Option (a): unset `GATE_LEGS` and
  `GATE_REUSE` before a bar that is not STUB, and name them on stderr. Option (b): refuse the push as
  `bar-refused` when either is set. Recommendation: (a). Both close the route. (a) also lands an
  operator whose shell still exports a fixture knob, and it runs a strictly stronger bar than the
  one asked for.
  RESOLVED (agent, 2026-09-30, delegated): (a). It satisfies every criterion (b) does, leaves no
  follow-up, and S4 keeps the choice visible.
- **F2 — what happens to an exported `GOV_PYTHON`?** Option (a): drop it and every `*_PY` name
  beside `GOV_KITROOT`, and let the vetted `gate-env.sh` declare one. Option (b): refuse the push
  when one is set. Option (c): keep it when it is a single bare word. Recommendation: (a). (b)
  refuses a push the resolver can serve without the override. (c) still resolves the word through
  `PATH`, so it vets nothing.
  RESOLVED (agent, 2026-09-30, delegated): (a). It is the mechanism the hook already uses for
  `GOV_KITROOT`, so it adds no new surface.
- **F3 — does the bar also lose the language runtimes' own variables?** Option (a): name
  `PYTHONPATH`, `PYTHONHOME`, `NODE_OPTIONS`, `BASH_ENV` and `PATH` as open in the hook's header,
  beside `BASH_ENV`, which is already named there. Option (b): unset the first three before the bar.
  Recommendation: (a). (b) changes the environment every adopter's own legs receive from a hook that
  ships verbatim, which is a public surface (M3 veto 2), and `PATH` stays inherited either way, so
  the class stays open under both.
  RESOLVED (agent, 2026-09-30, delegated): (a). Option (b) is discarded under veto 2 and left to the
  owner as a follow-up, not decided here.

## 9. Revision log

- rev-1 · 2026-09-30 · initial draft, promoted under BUILD-METHOD M4 from the round-2 closing diff
  review's H1, adopted by the run's rescope entry of 2026-09-30.
- rev-2 · 2026-09-30 · S7, AC9, §4 · during the build, before its code: the run-log suite's exit
  table has under-counted the hook's `bar-refused` sites since `baa7289a`, which keeps a leg this
  unit names red. The table moves to five and the file joins the estimate.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "vet a file the push hook trusts against the tracked
blob"` ranked `tracked`, `blob_oid` and `blob_at` in `tools/govkit/govkit.py`, none of which the hook
can call. The probe reports `.sh` as an unscanned layer, so it cannot see the seam. The seam is
`check_reviewed_file` in `.githooks/pre-push`, found by reading. `TOOL-aRepatriatedFork-24` built it
as the hook's one predicate for a file it trusts without a bar over it, and S3 is its fourth caller.
S1 extends the `unset GOV_KITROOT` line beside it.

Recall terms used: `pre-push GOV_KITROOT GOV_GATE_CMD environment refuse select bar-refused
check_reviewed_file gate-env tracked blob stub escape`, with the question "why does the pre-push hook
drop environment overrides before it runs the bar". The hits were `TOOL-aStandingWrit-4`, which calls
a classifier that takes its selector from the environment a fail-open, the round-2 review's H1, and
`TOOL-aRepatriatedFork-5`'s spec.
