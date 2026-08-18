# TOOL-aPacedTurnstile-1 — the gate runner becomes a deployable kit

**Status:** OPEN · rev-3 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

## 1. Goal

`tools/run-gates.sh` is exempt from govkit because it sources `tools/lib/`, which never travels, and
exits 2 with zero legs run when that path is absent. Move it into `tools/run-gates/`, inline the one
block it borrows, and give it the full kit shape, so `govkit apply` installs a working merge bar
instead of wiring legs into a runner the target is assumed to already own.

## 2. Scope (IN)

- **S1** — create `tools/run-gates/` and `git mv` three files into it: `run-gates.sh`,
  `run-gates.test.sh`, `run-gates.evidence.test.sh`. `tools/gate-legs.json` does NOT move.
- **S2** — cut the `tools/lib/` dependency in EVERY shipped file that has one. The runner's source
  line becomes the marker-delimited canonical block, byte-identical; `run-gates.test.sh` carries one
  too, because it sources the resolver itself and a kit that ships a harness which cannot start
  without `tools/lib/` has not been made deployable. Both copies enrol themselves in the parity
  population, which is grep-derived. The scratch-builder lines that copy the resolver into a
  `tools/lib/` the kit no longer needs are dropped.
- **S3** — derive the manifest default from the kit dir's own position rather than hardcoding
  `tools/gate-legs.json`, so a one-segment install at either prefix resolves its sibling. `GATE_LEGS`
  still outranks the derivation.
- **S4** — add `KIT_RUN_GATES_VERSION` with its same-line `gov:kit` marker, a
  `tools/run-gates/README.md` carrying the same marker, and the paired assertion in
  `tools/check-kit-versions.sh`.
- **S5** — widen the tail separator to TWO spaces on every tailed report line, and add a canary arm
  forbidding a double space inside any leg NAME. This is the output contract
  `TOOL-aPacedTurnstile-2`, `-3` and `-5` all extend, and this unit owns it.
- **S6** — write `tools/run-gates/kit.toml`: id, home, version_from, file rules, adopt, check,
  outcome, FOUR `[[gate_leg]]` rows, the LF pin, and the `[gate_runner_seed]` table. FOUR, not five:
  only the two repointed legs plus S7's adopter e2e and its `--check` exist when this unit lands.
  `TOOL-aPacedTurnstile-4`'s turnstile suite is the fifth and that unit owns its row in BOTH
  carriers — a descriptor row naming a leg the manifest does not carry reds the deployer's selfcheck
  at this unit's own landing.
- **S7** — write `tools/run-gates/adopt-run-gates.sh` with `--check`, plus
  `tools/run-gates/adopt-run-gates.test.sh` gated on EFFECTS, printing its executed assertion count
  against a floor so it needs no waiver row.
- **S8** — registry surgery in `tools/govkit/registry.toml`: add the entry, delete the three exempt
  path rows and the two exempt-leg rows naming run-gates, and correct the `tools/lib` exemption's
  now-false clause about the runner sourcing it. The `tools/gate-legs.json` exemption STAYS.
- **S9** — teach `cmd_intake` to emit the target's `[gate_runner]` block from the selected entry's
  `[gate_runner_seed]`, resolving the path tokens only and passing the runner's own `{name}`
  placeholder through verbatim.
- **S10** — repoint every live spelling of the old path: `.githooks/pre-push`, `.unattended.conf`,
  `tools/unattended/.unattended.conf.example`, `tools/lib/pyrun.sh`'s docstring, `AGENTS.md`'s gate
  suite bullets, and the two moved harnesses' self-references.
- **S11** — the two obligations a new kit dir creates on day one: a row in
  `tools/playbook-kit-waivers.txt` or coverage in the playbook trio, and the two repointed rows in
  `memory/project/testsuite-count-waivers.txt`.
- **S12** — author `memory/map/features/run-gates.md` claiming the `kits` key and the gate-leg keys
  THIS unit creates, and drop the now-claimed row from `memory/map/baseline.toml`. It does not claim
  `TOOL-aPacedTurnstile-4`'s turnstile leg, which does not exist for four more units and would red
  the map's stale-claim predicate; that unit adds its own key to this dossier when it lands.

## 3. Non-goals (OUT)

- Moving `tools/gate-legs.json`. It is repo DATA, not kit payload. Its exemption row states the
  reason and stays true: a target's leg list is emitted from descriptors, never copied. Seeding an
  adopter with gov's 70 leg names is the class `memory/gotchas/pin-copied-from-another-corpus.md`
  exists for; the adopter seeds an empty list instead.
- Implementing the gate-runner kinds that are refused by name today. They stay refused.
- Emitting the CI workflow. That key is validated and read by nothing, a pre-existing gap.
- Repairing `run_all_env`, a required key no code path reads. Recorded as a risk, not fixed here.
- Retiring `tools/lib/`. It stays gov-internal and permanently exempt; only the runner stops
  sourcing it.
- Rewriting the roughly forty historical records under `memory/builds/` that quote the old path. The
  corpus is append-only; the moved path is noted in the build ledger instead.
- Anything the sibling units own: profiles, chunks, the beacon, the record, the push boundary.

## 4. Design

### Why the exemption exists, verified against source

The registry gives two reasons and both are exact. `run-gates.sh` has exactly one gov-internal
dependency, the resolver source line. With `tools/lib/` absent, bash sourcing a missing file under
`set -u` and no `set -e` continues, `resolve_python` is undefined, the assignment fails, and the
`|| { …; exit 2; }` on the next line fires. Zero legs run.

### The parity requirement enlists the new copy by itself

`tools/lib/resolve-python.test.sh` derives its copy population by grepping for the opening marker
across tracked shell files, rather than from a hardcoded list. Pasting the marker-delimited region
into the moved runner therefore enrolls it automatically: **no table row, no gate edit.** The
matching ban on the retired `command -v python3` idiom and the bare-invocation ban are both already
satisfied by the current runner and stay satisfied by a verbatim paste.

### Kit dir layout

```
tools/run-gates/
  run-gates.sh                    the runner, carrying the version constant and its marker
  run-gates.test.sh               the canary
  run-gates.evidence.test.sh      the evidence arm
  adopt-run-gates.sh              + --check
  adopt-run-gates.test.sh         the adopter e2e, effects-gated
  gate-profiles.txt               TOOL-aPacedTurnstile-2's table, a kit seed file
  kit.toml
  README.md                       carries the gov:kit marker
```

`gate-profiles.txt` lands here rather than at depth 1 because the kit's file rule claims the whole
directory, which means it needs no exemption row of its own — and unlike the leg manifest its
content is hardware-generic rather than gov-specific, so it is payload.

### The report-line tail contract

The deployer reads a target's verdicts by matching a declared line head and then splitting the
remainder. Today's single-spaced tails make that split return a truncated leg name for any leg
whose name contains a space, which is most of them. Two spaces before every tail fixes it in three
`printf` edits with no deployer change, and the canary gains the arm that keeps a leg NAME from
containing a double space, so the hazard is closed rather than inherited.

Every verb the sibling units add conforms to this contract: two spaces before any parenthesised
tail, on every verb.

### Data model — the leg manifest's known key set

The canary pins the set of keys a leg row may carry. After this build that set is
`name`, `argv`, `guard`, `chunk`, `impure` — `chunk` from `TOOL-aPacedTurnstile-3` and `impure` from
`TOOL-aPacedTurnstile-5`. This unit adds no key of its own; it records the closed set so whichever
sibling lands second edits one pinned list rather than discovering it.

### Who writes the target's runner declaration

A declaration written at configure time cannot reach the same run's leg-emission step, so leaving
it to the operator means the first `apply` after adopting the runner silently takes the
"ORDERED, not emitted" branch and exits 0. That is the silent-green direction this deployer refuses
by name everywhere else, so `cmd_intake` emits the block. `--check` stays regardless: it is the arm
that catches the declaration drifting from the runner's actual output strings.

### Rollout

One commit for the move plus its repoints, because a half-moved runner has no green state. The
manifest row edits this unit makes are additive; `TOOL-aPacedTurnstile-3`'s whole-file reorder is
sequenced last in the build for that reason.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/run-gates.sh` and the two harnesses | moved, resolver inlined, manifest default derived, tails widened |
| `tools/run-gates/adopt-run-gates.sh`, `adopt-run-gates.test.sh`, `kit.toml`, `README.md` | new |
| `tools/govkit/registry.toml` | entry added, five rows deleted, one `why` corrected |
| `tools/govkit/govkit.py` | `cmd_intake` emits the runner declaration |
| `tools/check-kit-versions.sh` | the new constant and marker pair |
| `tools/gate-legs.json` | two argv repoints, TWO new legs — the adopter e2e and the wiring check |
| `.githooks/pre-push`, `.unattended.conf` and its example, `tools/lib/pyrun.sh` | path repoints |
| `AGENTS.md` | gate-suite bullets and their script paths |
| `tools/playbook-kit-waivers.txt`, `memory/project/testsuite-count-waivers.txt` | the day-one rows |
| `memory/map/features/run-gates.md`, `memory/map/baseline.toml` | the dossier and its shrink |

### Alternatives rejected

- **Fix the tail truncation in the deployer's reader instead of the runner.** Rejected: larger diff,
  and it would keep gov's runner non-conforming to a contract four other harnesses already assume.
- **Move the leg manifest into the kit.** Rejected in the fork below.
- **Ship the version marker in the script only, no README.** Rejected: the kit-version gate asserts
  a marker/constant PAIR for the comparable kits, and an adopter greps the README.

## 5. Production-readiness checklist

- security — no new credential path; the adopter writes only inside the target it was pointed at,
  and refuses before writing when the resolved tree is not the operator's tree.
- perf / scale — the move is free at runtime; the derived manifest default is one string operation.
- a11y — N/A: no user interface.
- i18n — N/A: operator-facing English in shell, as everywhere else here.
- error / empty / loading states — the absent-`deploy.toml` and declared-none paths report NOT
  ADOPTED and exit 0 writing nothing; both carry arms.
- observability — the two-space tail is the observability fix: a verdict line becomes parseable.
- risks (concurrency, data-loss, rollback hazards) — a half-applied move is the only data hazard and
  is avoided by one commit. Rollback is `git revert` of that commit.
- testing + left-shift gates — the adopter e2e is effects-gated, and the double-space canary arm
  left-shifts the truncation class.
- migration / rollback — historical records keep the old path by design; `git log --follow` spans
  the move.
- user docs — `AGENTS.md` bullets, the kit README, and the runbook gap already recorded as
  `DEPL-aSealedCaravan-3`.

## 6. Acceptance criteria

- **AC1** — When a scratch repo carrying only `tools/run-gates/` and a two-leg manifest is built
  with no `tools/lib/` directory at all, `bash tools/run-gates/run-gates.sh` exits 0 and prints
  `GATE ok` for both legs, AND every `*.test.sh` the kit ships also runs to completion in that same
  `tools/lib`-free tree — the runner starting alone is not evidence the KIT starts alone.
- **AC2** — When `bash tools/lib/resolve-python.test.sh` runs, its parity stage enumerates
  `tools/run-gates/run-gates.sh` among the discovered copies and reports it byte-identical, with no
  edit to that file's own row table.
- **AC3** — When `python tools/govkit/govkit.py selfcheck` runs after the surgery, it exits 0 with
  `run-gates` among the entries and reports no stale exemption.
- **AC4** — When a leg fails, the runner prints its name followed by two spaces and the tail, and
  splitting the remainder on a double space yields the bare leg name — asserted in
  `tools/run-gates/adopt-run-gates.test.sh` in those exact terms.
- **AC5** — When `bash tools/run-gates/adopt-run-gates.sh --check` runs against a target whose
  declared `observed_ran` head no longer prefixes any `printf` in the installed runner, it exits 1
  and the message names `observed_ran`.
- **AC6** — When `bash tools/run-gates/adopt-run-gates.sh --check` runs in this repo, which declares
  no target, it exits 0 reporting NOT ADOPTED and writes no file. Its control is the mutation arm in
  `adopt-run-gates.test.sh` that edits the runner's `printf` and asserts the red; the two are kept
  together because this criterion alone is satisfied by a `--check` that does nothing.
- **AC7** — When `bash tools/run-gates/adopt-run-gates.test.sh` runs, it prints its executed
  assertion count at or above its declared floor, and `bash tools/check-testsuite-counts.sh` exits 0
  with no waiver row naming it.
- **AC8** — When `GATE_LEGS` names a fixture manifest, it overrides the derived sibling default even
  where the real manifest exists — asserted by a new arm in `tools/run-gates/run-gates.test.sh`, so
  the nested runs the canary and the evidence arm spawn cannot re-enter the real bar.
- **AC9** — When `python tools/govkit/govkit.py intake` selects this kit, the written declaration's
  command names `tools/run-gates/run-gates.sh` and its `observed_ran` still carries the runner's
  `{name}` placeholder intact.
- **AC10** — When `python tools/codebase-map/test_codebase_map.py` runs, the `kits` and `gate-legs`
  inventories are fully claimed and `memory/map/baseline.toml` no longer carries the row this
  dossier claims.
- **AC11** — When `bash tools/check-playbook-parity.sh` runs, the new kit dir is either named in the
  playbook trio or carries its row in `tools/playbook-kit-waivers.txt`, and the gate exits 0.
- **AC12** — When `python tools/drift-audit/drift_report.py --check` runs after `AGENTS.md` is
  repointed, it exits 0: every leg whose script path the charter names is spelled at its new path.
- **AC13** — When `KIT_RUN_GATES_VERSION` is deleted, or bumped in the constant without its marker,
  `bash tools/check-kit-versions.sh` exits 1 naming that constant — the red-proof the comparable kit
  pairs already carry, without which S4's named gate passes on a marker nobody checks.

## 7. Gates

`bash tools/lib/resolve-python.test.sh` · `python tools/govkit/govkit.py selfcheck` ·
`python tools/govkit/selftest.py` · `python tools/govkit/matrix.py` ·
`python tools/govkit/refusal_join.py` · `bash tools/run-gates/run-gates.test.sh` ·
`bash tools/run-gates/run-gates.evidence.test.sh` · `bash tools/run-gates/adopt-run-gates.test.sh` ·
`bash tools/run-gates/adopt-run-gates.sh --check` · `bash tools/check-kit-versions.sh` ·
`bash tools/check-install-prefix.sh` · `bash tools/check-testsuite-counts.sh` ·
`python tools/codebase-map/test_codebase_map.py` · `bash tools/check-playbook-parity.sh` ·
`python tools/drift-audit/drift_report.py --check` · `bash .githooks/pre-push.test.sh` ·
`bash tools/push-main.test.sh` · `bash tools/unattended/check-unattended.sh`.

## 8. Open questions

none — the forks below are RESOLVED. Every pick is the M3 ratification of the fork's own
recommendation; the reason each survived the veto order is recorded with it.

- **Where the leg manifest lives.** Options: keep it at its current path with the runner deriving it
  as the kit dir's sibling, or move it inside the kit. Recommendation: keep it. Moving it would
  invalidate its exemption row, break its LF pin, and touch four other consumers for no gain, while
  the sibling derivation already gives an adopter the same shape at either prefix.
  RESOLVED (agent, 2026-08-18, delegated): keep it at its current path, with the runner
  deriving it as the kit dir's sibling. The other option does not reach the feature-richness
  test - M3 veto 1 discards it first, because section 3 puts moving `tools/gate-legs.json` OUT
  by name and an option that violates a written non-goal is discarded before it is compared.
- **How the pre-push hook's dependence on the runner is enforced.** A `requires` edge only ORDERS a
  selection; it does not pull a missing kit in, so a target can still receive a merge-bar hook
  without the merge bar. Options: add the runner to the default selection, add a selfcheck arm that
  an entry spelling another entry's command must hard-depend on it, or rely on the wiring leg to red
  in the target. Recommendation: the default-selection line here, with the selfcheck arm filed as
  its own govkit unit rather than built into this spec.
  RESOLVED (agent, 2026-08-18, delegated): the default-selection line in this unit, with the
  selfcheck arm filed as its own govkit unit rather than built here. Adding the arm inside this
  spec would change another kit's contract mid-unit, which M3 veto 2 reaches as a governance
  carrier change. The follow-up is filed as `TOOL-aPacedTurnstile-11` so the deferral is a row
  in the backlog and not a sentence in a spec nobody re-reads.
- **Whether the `tools/gate-legs.json` exemption also comes out.** Recommendation: no — its stated
  reason survives the promotion unchanged.
  RESOLVED (agent, 2026-08-18, delegated): no. Its stated reason survives the promotion
  unchanged, and section 3 already carries the same disposition as a non-goal.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded the spec audit: `kit.toml` declares FOUR gate-leg rows, not five —
  the fifth names a leg that does not exist for four more units and would red the deployer's
  selfcheck at this unit's own landing (BLOCKER F1); S2 inlines the resolver into the shipped canary
  too, which otherwise kept the gov-internal dependency this unit exists to cut, and AC1 widens to
  run every shipped harness in the dependency-free tree (F7); AC13 red-proves the version marker,
  whose named gate was a hand-kept list nothing tested (F6); S12 stops claiming a sibling's map key
  four units early (F31).
- rev-3 · 2026-08-18 · swept section 8 under the standing mandate: every fork RESOLVED in
  place per M3, and the section's first non-blank line made machine-legal so the classifier
  reads this unit as READY instead of FORKED.

## 10. Reuse audit

Seams this extends, each cited by path. `tools/lib/resolve-python.sh` — the marker-delimited block,
pasted byte-identically and never edited. `tools/lib/resolve-python.test.sh` — its parity stage
derives the copy population by grep, so the new copy enlists itself.
`tools/drift-audit/adopt-drift-audit.sh` — the reference adopter: kit-dir-derived root, the prefix
derivation reused verbatim for the manifest default, and the render-then-diff `--check` shape.
`tools/unattended/adopt-unattended.test.sh` — the effects-gated e2e pattern with per-arm scratch
repos and refusal arms that assert nothing was written.
`tools/govkit/entries/push-main.kit.toml` — the precedent for a descriptor shipping `.githooks/`
files and for declaring an absent check with a reason. `tools/drift-audit/kit.toml` — the descriptor
template being followed. `tools/check-kit-versions.sh` — the marker/constant PAIR assertion, where
presence-only is already recorded as insufficient.

No seam fits the declaration emission: `cmd_intake` writes a fixed literal body today and reads
nothing per-kit beyond its answer set, which is why S9 is a code change rather than a declaration.

Recall terms used: gate, leg, verdict, reuse, cache, lock, beacon, queue, concurrent, session,
worktree, scoped, diff, GATE_FULL, guard, skip. The probe returned `TOOL-aTimedTurnstile-1` through
`-3` and the aTimedTurnstile review's F6; the deployability constraints came from
`tools/govkit/registry.toml` read directly, and `TOOL-aSealedCaravan-1` S9 is the recorded precedent
for giving a kit its own launcher so nothing under `tools/lib/` travels.
