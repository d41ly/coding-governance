# TOOL-dDeclaredLoop-2 — the guard, the TTY policy command and the default floor

**Status:** CLOSED · rev-5 · 2026-11-15 · node d · Tier-2 · base ed497191 · streams tooling · order 15 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0087@5eb8d36a whole

**Carries:** node:policy-key.floor

**Carries:** node:policy-key.policy-file.guard

**Carries:** node:policy-key.policy-file.proof

**Carries:** node:policy-key.policy-file.on-missing-expansion

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-26 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-25-build-TOOL-dDeclaredLoop-2-deviation-21.md](../build/2026-10-25-build-TOOL-dDeclaredLoop-2-deviation-21.md) | deviation | — |
| [2026-11-05-build-TOOL-dDeclaredLoop-2-deviation-22.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-2-deviation-22.md) | deviation | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-2-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-2-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-2-deviation-23.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-2-deviation-23.md) | deviation | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-2-deviation-24.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-2-deviation-24.md) | deviation | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-2-red-fix-21.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-2-red-fix-21.md) | red-fix | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-56 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-2-1-spec-reviewer.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-2-1-spec-reviewer.md) | journal | — |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-56 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade.md) | research | TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-2-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-2-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-2-2-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-2-2-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-2-build-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-2-build-brief.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-2-f9-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-2-f9-brief.md) | research | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-2-reground-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-2-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |

<!-- /gen:spec-records -->

## 1. Goal

The policy file gets its real guard: a verdict that reads `policy-file.guard` and `policy-file.proof`,
a policy command that writes only after an interactive terminal confirms it, or on a live run's branch,
and stamps a `Gov-Policy:` trailer, a push arm that checks the trailer, and the default floor's four
invariants, each switched by `floor` and only under the guard. The guarded command admits one agent
write outside a run, a raise of one measured-file cap under `budgets.*` on the four conditions the
paragraph "WHEN A RUN MAY RAISE A ROW" of `tools/template-size-limits.txt` states, and refuses every
other agent write as `policy-file.guard` says. The owner ruled on 2026-11-12 that no file is
owner-only to a run working under its build's mandate, and the minimal guard admits that run since
PLAY-dOrderedCharter-84; this unit keeps that admission under every value and ahead of the floor's
guard-self, each change a run makes recorded (gap-spine-02, gap-spine-07; v2 `[floor]` and
`[witnesses]`; the whole-design audit's C2-F9; the owner's FK-7-1).

## 2. Scope (IN)

- **S1** — The guard verdict, `tools/loop/guard.py --staged`, which wraps dGroundRules-6's minimal
  guard rather than copying it. It reads `policy-file.guard` at the landed revision through the policy
  kit's `resolve`, the kit found by `tools/loop/loop_parents.py#read_policy_kit`, and, for a staged
  change to any path `tools/policy/guarded-paths.txt` lists at HEAD, applies §4's steps. Its
  `owner-only` and `agents-within-mandate` arms are the minimal guard itself, run as a subprocess of
  that kit's `guard.py --staged`, so the cap raise and the live-run admission each have one
  implementation. Observed by AC1, AC2, AC3, AC5, AC6, AC7.
- **S2** — The floor, `tools/loop/floor.py`: `FLOOR_INVARIANTS`, the four member names
  `verdict-before-move`, `record-changes`, `guard-self` and `no-actor-witness` (I11), and
  `read_floor(repo, rev=None)`, which reads the `[floor]` table through the policy kit's
  `read_revision`, an invalid file read as `policy-file.on-invalid` says. Every absent member reads
  `on` (v2's "all on"), and an unknown member or a value other than `on` and `off` is refused. Where
  the policy kit does not resolve or its reader refuses, every member reads `on` and the reason is
  printed once. Its CLI `floor.py get <member>` prints `on` or `off`. Observed by AC4, AC12.
- **S3** — The guard's own switch (`floor.guard-self`): a staged change that alters
  `policy-file.guard`, `policy-file.proof`, any `floor` member, or `tools/policy/guarded-paths.txt`
  is refused for every agent commit off a live run's branch, under every value of `policy-file.guard`.
  On a live run's branch the run admission precedes it, as the owner's ruling reads (§8 F9): a run
  may change those keys and that list, each with its change record, which the verdict's step 3
  checks. Observed by AC4.
- **S4** — The TTY policy command, `python tools/loop/policy_edit.py <verb>`, with the write verbs
  `set <key> <value>` and `raise <cap> <new>`, each taking `--build <slug> --unit <id>`, and the read
  verb `propose`. A write checks the value against its catalogue row with dGroundRules-1's
  `check_value`, writes `.governance/policy.toml`, writes the change record for the same commit
  through `tools/memory-tree/build_records.py#write_change`, stages both, and prints the `Gov-Policy:`
  trailer line the commit must carry. `set` writes when S5's terminal proof holds and the typed
  confirmation follows, or when the branch is a live run's branch as the minimal guard's
  `check_run_mandate` reads it (§8 F8, F9); otherwise it prints the proposal and writes nothing.
  `raise` is admitted without either, and only on the four conditions of §4. Observed by AC8, AC9.
- **S5** — The shared guarded-write factory, extracted at its second instance (I12): the terminal
  proof, `check_terminal_proof`, standard error an interactive terminal, and the write-then-record
  step, `write_guarded`, canonical in `tools/lib/guarded_write.py` and carried inline, between
  `# >>> guarded_write_py` and `# <<< guarded_write_py`, in `tools/loop/policy_edit.py` and
  `tools/playbook/instructions_edit.py`, held by a `guarded_write_py` row of
  `tools/lib/resolve-python.test.sh`'s `PARITY_ROWS`. In `instructions_edit.py`, `run_write`'s
  terminal test, `sys.stderr.isatty()` (dOrderedCharter-15 S5, the owner's settlement of its §8 F4),
  and `write_candidate`'s record write with its restore of the manifest's prior bytes, are re-pointed
  to the inline block, which tests the same stream and keeps that restore. Observed by AC10.
- **S6** — The push arm, `tools/loop/guard.py --push-range <base>..<tip>`, called from
  `.githooks/pre-push` beside the merge-loss check: every commit in the range whose parent holds
  `.governance/policy.toml` and whose diff changes a leaf of it carries one `Gov-Policy:` trailer line
  per changed leaf, naming its old and new value, and adds a change record naming each changed key's
  row; one that does not is refused, naming the commit and the key. The trailers are read through
  the memory-tree kit's `read_commits` with that key. A commit adding the file is not graded (§8 F11).
  Observed by AC11, AC19.
- **S7** — `policy-file.proof`'s values: `tty-cli` is S5's proof; `signed` and `both` select the
  layered proof v2 places in `[planned]`, which no component implements, and are read as
  `policy-file.on-missing-expansion` says. Observed by AC12.
- **S8** — `policy-file.on-missing-expansion`, its rule as one function,
  `check_expansion_value(key, value, points)` in `tools/loop/guard.py`, over `[[selects]]` rows of
  `tools/loop/loop.toml`, each naming a key, a value and the layer point that value needs. When
  `points`, the points the core rows of the playbook kit's `layers.toml` declare, lacks that point,
  `refuse` (the default) exits 2 naming the key, the value and the point, and `fallback-reported`
  reads the catalogue default and prints one line naming the substitution. The five rows at landing
  are §4's. `tools/playbook/instructions_edit.py#read_load`'s two refusals of an absent component are
  re-pointed to the same function. Observed by AC12.
- **S9** — The layer point `point.instruction.guard`, added to the `declares` list of the `layer.flow`
  row of `tools/playbook/layers.toml`, which `instructions_edit.py`'s `GUARD_POINT` names, so the
  instruction command's write verbs stop refusing for the guard's absence. Observed by AC13.
- **S10** — The harness refusal: a policy-file arm in `tools/hooks/scratch-guard.js#checkRouted`
  denies an Edit, Write, MultiEdit or NotebookEdit whose target is the policy file, naming
  `policy_edit.py` as the door (§8 F10). The path is the one `tools/policy/policy-mirror.js` exports as
  `POLICY_REL`, found through `agent-cap.js`'s `resolvePolicyHelper`; with no policy kit beside the
  hook the arm does not fire. It sits inside the write gate's one evaluation order, whose caller in
  `main` fails closed. Observed by AC14.
- **S11** — The pre-commit block of dGroundRules-6 S4 re-pointed: its staged-path test over the list
  at HEAD and its terminal admission stay, and the verdict it runs becomes the loop kit's `guard.py
  --staged` wherever `resolve_kit_gate` finds it, the minimal guard where it does not.
  Observed by AC15.
- **S12** — The leg `loop guard fixtures` in `tools/gate-legs.json`, running
  `python {prefix}/loop/guard.py --selftest`, whose plants stage every admitted and refused shape of
  §4, carrying `enforces = ["principle.p10"]` (dOrderedCharter-7 S2), gov's own `[[exempt_leg]]` in
  `tools/govkit/registry.toml` as `loop parent routes` is. No v2 `[enforcement]` row names
  `cl-dClosedLoop-0087`, so the tag is settled by TOOL-dDeclaredLoop-3 §8 F7's rule, what the leg
  checks: the policy file's admitted and refused writes, which P10's "One policy file, one reader, one
  guard" governs. This pass deletes the `principle.p10` row of `tools/playbook/core-pending.txt`,
  which the meta-check reds stale once the leg enforces the tag. Observed by AC18.
  **Readers:** by name: `tools/playbook/core.py`, its meta-check verb, the one reader of the pending
  list's rows, which reds a row whose item is enforced · by value: NO VALUE READERS — a pending row's
  value is its arming build, `dGroundRules` here, which the meta-check prints only in its pending
  count.
- **S13** — The section "Who may change the policy file" of `help/policy.md` rewritten for the guard
  values, the command, the push arm and the floor. Observed by AC16.
- **S14** — The switch readers: each invariant's enforcing site reads its member through
  `read_floor` and, at `off`, prints `floor: <member> off` and reports instead of refusing. The sites:
  `.githooks/pre-push`'s `gate RED` refusal (`verdict-before-move`); step 3 of the verdict, S6's push
  arm and `tools/loop/loop_transition.py#check_transition_channels` (`record-changes`); step 2 of the
  verdict (`guard-self`); and the two refusals of an actor witness no list row
  names, in `tools/loop/loop_lib.py#check_site_witnesses` and in `loop_lib.py`'s `--check` over
  `check_actor_list` (`no-actor-witness`). Observed by AC17, AC19.

## 3. Non-goals (OUT)

- The policy file, its catalogue, its reader and the minimal guard's admitted shapes: dGroundRules'
  (`TOOL-dGroundRules-1`, `-2`, `-6`) and PLAY-dOrderedCharter-84's run admission. This unit reads
  through them, adds no parser beside the policy kit's `parse_policy`, and changes no catalogue row
  (I10): `policy-file.guard` keeps its three values.
- The change-record kind, its name grammar and its fields: dOrderedCharter's (I13).
- The layered proof behind `signed`. It waits in v2's `[planned]`; until then the key's value reads
  as S8 says. The threat `tty-cli` accepts, a pty wrapper giving an agent a terminal, stays accepted
  (SA-1) and is printed in the command's help.
- Harness refusals of agent writes to hooks, verdict refs, and the three other guarded paths, and
  `hooks.bypass`: no clause of this build names them (§8 F5, F10).
- The enforcement behind `floor.verdict-before-move` and `floor.no-actor-witness`: the pre-push bar
  run and unit 5's class rule enforce them; this unit gives each its switch and the switch's reader.
- Condition 2 of the four, a comment block's stated rule, is checked only for an explicit
  `reserved: owner` line; any other stated rule is left to the change record's argument, as
  dGroundRules-6 leaves it.
- The ask TOOL-dDeclaredLoop-101, a `[[selects]]` row whose point is a core point that an expansion
  must attach: S8 refuses only an undeclared point, and that ask keeps its own acceptance.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-23` — `read_commits`, the one trailer reader S6 reads `Gov-Policy:` through, and the key's `[[trailer]]` row in the playbook kit's `edges.toml`; without it the push arm would be another trailer parser
- **consumes-from** `TOOL-dDeclaredLoop-5` — the refused witness class `actor`, the actor-witness list and its two refusals, which `floor.no-actor-witness` switches; without it the invariant names nothing to refuse
- **consumes-from** `TOOL-dDeclaredLoop-3` — the `Gov-Transition` trailer and `check_transition_channels`, which `floor.record-changes` switches for stage transitions as S6 holds `Gov-Policy:` for policy changes
- **consumes-from** external — dGroundRules' policy kit (`tools/policy/policy.py` `resolve`, `read_revision`, `check_value`, `parse_policy`, `tools/policy/guard.py` `--staged` and its helpers, `tools/policy/guarded-paths.txt`, `tools/policy/policy-mirror.js`), PLAY-dOrderedCharter-84's `check_run_mandate`, dOrderedCharter-15's `instructions_edit.py`, dOrderedCharter-16's `tools/playbook/layers.toml` and dOrderedCharter's `change` record kind, each landed before this unit
- **hands-off** external — the layered proof behind `signed`, and harness refusals of agent writes to hooks and verdict refs, to the builds that own them
- **hands-off** `TOOL-dDeclaredLoop-43` — the guarded write's sibling-temp atomic write; the restore of each path's prior bytes moves into the factory here from `write_candidate`, where it stands at HEAD (the round-1 spec audit's id 49)
- **hands-off** `TOOL-dDeclaredLoop-44` — the push arm's merge and new-branch rule, which that unit completes (the round-1 spec audit's id 50)
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 21, 26, 31, 39, 46, each a scope item of that unit

## 4. Design

### Evidence

Read at `c91665355`.

- The minimal guard, `tools/policy/guard.py#main`, admits two agent shapes and reads neither key: one
  `budgets.*` cap raised with its `RAISED` line and a decision row (`check_raise_shape`,
  `check_decisions_row`), and the mirror equal to its render (`check_mirror_render`). When those
  refuse, `check_run_mandate` admits the commit where HEAD's branch is the `run-branch` of a run-state
  file at HEAD whose `phase` is outside the driver's `PHASES_TERMINAL`, asking no decision row
  (PLAY-dOrderedCharter-84). Its `run_git` exits 2 on a git failure.
- The owner's ruling (`memory/builds/dOrderedCharter/build/2026-11-12-build-PLAY-dOrderedCharter-1-owner-guard-ruling.md`):
  "No file is owner-only to a run working under its build's mandate." PLAY-dOrderedCharter-84 S1 hands
  this unit the inversion it leaves: the default `owner-only` admits a live run's branch with no
  reason, while rev-4's `agents-within-mandate` demanded one.
- `tools/loop/loop_parents.py#read_policy_kit` inserts the policy kit's directory at the head of
  `sys.path` and imports its modules `policy` and `guard` by those names; `loop_transition.py` reads
  `transitions.record` through it. The loop kit's `kit.toml` records that it takes no edge to the
  policy kit, each such reader exiting 2 `unarmed` where it does not resolve.
- The catalogue rows: `policy-file.guard` `owner-only`, `agents-with-reason`, `agents-within-mandate`;
  `policy-file.proof` `tty-cli`, `signed`, `both`; `policy-file.on-missing-expansion` `refuse`,
  `fallback-reported`; `floor` a `map` of `on` and `off` whose default is `{ derived = "all on" }`.
  `tools/policy/policy.py#read_default_value` refuses a derived default as `DerivedDefault`, and
  `parse_policy` descends the `[floor]` table into member leaves, so `resolve("floor")` answers no
  file value: `read_floor` reads the members from `read_revision`'s table itself.
- `check_policy.py`'s reader-coverage arm counts a call whose first argument is the key in quotes,
  once the owning build has landed (`help/policy.md`, "Every key whose build has landed has a reader").
- The change kind: `tools/memory-tree/build_records.py#write_change` validates `Unit` as a tag,
  `Before` and `After` as `none` or `<tag>@<hash8>`, `Action` in `CHANGE_ACTIONS` and `Proof` as
  `tty-cli` or `none — <value>`. The `policy` namespace's extractor, `tag_index.py`'s
  `extract_policy`, mints `policy.<name>` per literal row and one family tag per placeholder prefix,
  so a cap's row tag is `policy.budgets`.
- The trailer: `Gov-Policy` is a `[[trailer]]` row of `tools/playbook/edges.toml` and one of
  `commit_trailers.py`'s `FLOOR_KEYS`; `read_commits` refuses an unregistered key.
- The four raise conditions, the one statement of them: the paragraph "WHEN A RUN MAY RAISE A ROW" of
  `tools/template-size-limits.txt`. `tools/policy/budgets.py#check_budgets` refuses a `budgets.<cap>`
  naming no census row of `caps.toml`, and `resolve_caps` refuses a cap held in both homes.
- `instructions_edit.py`: `GUARD_POINT = "point.instruction.guard"`, `FLOW_POINT` and `SIGNED_POINT`
  are spelled `point.instruction.*`; `read_load` refuses `instructions.edit = "flow-only"` without
  `point.instruction.flow` and `instructions.proof` `signed` or `both` without
  `point.instruction.signed-proof`; `run_write` refuses every write while `GUARD_POINT` is undeclared
  and tests `proof == TTY_PROOF and sys.stderr.isatty()`; `write_candidate` restores the manifest's
  prior bytes when the record write refuses. Its fixture stages the owner with a `Terminal` standard
  error whose `isatty` is true.
- `layer.flow`'s `declares` holds four `point.flow.*` points and no instruction point.
- The write gate's one evaluation order is `checkRouted`; `main` wraps its call and denies on a throw.
  The red-fix lane reads a policy key through `require('./agent-cap.js').resolvePolicyHelper()`.
- The pre-commit block resolves the policy kit's `guard.py` by `resolve_kit_gate "$pg_kit" guard.py`,
  `pg_kit=policy` named once (TOOL-dGroundRules-84), reads the list at HEAD beside it, admits on
  `[ -t 2 ]`, and runs the guard under `with_hook_index`.
- `.githooks/pre-push`: the merge-loss block resolves a Python launcher and a kit by
  `resolve_kit_dir` over the top and the hook's parent, runs it over `$main_remote..$main_local`, and
  refuses through `write_refusal`; the bar's red refuses at the `gate RED` line after the
  inherited-red arm; `check_reviewed_file` is the one predicate for a file the hook trusts.
- The pending list `tools/playbook/core-pending.txt` holds `principle	principle.p10	dGroundRules`.
- An agent's shell has no terminal: dGroundRules-6 §4 measured `[ -t 0 ]`, `[ -t 1 ]` and `[ -t 2 ]`
  false on 2026-10-23. The owner's proof is one stream, stderr (dOrderedCharter-15 S5 rev-5).

### The verdict — `guard.py --staged`

Run by the pre-commit block only when a guarded path is staged and stderr is not a terminal, so
every call is an agent's commit. In order:

1. The touch set, as the minimal guard reads it: its `read_guarded_paths` intersected with the staged
   names, less a merge's parent sides (`check_parent_sides`). Empty: exit 0.
2. Guard-self (S3): when `read_floor` reads `guard-self` `on`, a staged change of the list file, or a
   leaf of `policy-file.guard`, `policy-file.proof` or `floor` among the minimal guard's
   `derive_leaf_changes` of the policy file at HEAD and staged, is refused naming the key and
   `floor.guard-self`, unless `check_run_mandate` admits the commit's branch: the run admission
   precedes guard-self, as the owner's ruling reads (§8 F9). It runs before the value's rule, so no
   value admits such a change off a live run's branch.
3. Record (`floor.record-changes` at `on`): a changed leaf of the policy file needs a staged change
   record whose `Unit` is that leaf's row tag, and a staged change of the list file one whose `Unit`
   is `kit.policy`, the tag of the kit that holds it; one missing is refused naming the key or the
   list file.
4. The value's rule, `resolve("policy-file.guard")` at the landed revision:

| Value | An agent's staged write is admitted when |
|---|---|
| `owner-only` (default) | the minimal guard exits 0: the one `budgets.*` raise with its `RAISED` line and decision row, the mirror's render, or a live run's branch |
| `agents-within-mandate` | the same, the ruling having widened the default to it (§8 F8) |
| `agents-with-reason` | the minimal guard exits 0, or only `.governance/policy.toml` is touched and `check_decisions_row` holds |

5. Every refusal prints `loop-guard: refused · <path> · <why>` and the remedy: the owner commits from
   a terminal, or an agent writes through `policy_edit.py`. Admission prints
   `loop-guard: admitted · <rule>`; the minimal guard's own lines pass through.

The value is read from the landed revision, never the staged file, so a commit cannot loosen the
rule that judges it. An invalid policy file reads as `policy-file.on-invalid` says, through the
reader. The minimal guard runs as a subprocess so its `run_git` exit cannot end the verdict
mid-step; its helpers are called in process through `read_policy_kit`.

### The push arm — `guard.py --push-range`

`check_push_range(base, tip)` reads every non-merge commit `git rev-list --no-merges <base>..<tip>`
names, through `read_commits` with the key `Gov-Policy`. A commit whose parent holds the policy file
is graded on `derive_leaf_changes(parent blob, commit blob)`: each changed leaf needs one trailer line
`Gov-Policy: policy.<key> <old> -> <new>` equal to it, and the commit adds a change record whose `Unit`
is the leaf's row tag. Exit 1 names the commit's sha8 and the key; exit 2 names a reader or git that
did not answer. At `record-changes` `off` each finding prints after `floor: record-changes off` and
the exit is 0.

In `.githooks/pre-push`, beside the merge-loss block and under its `--decide` and remote-branch
conditions, the hook resolves the loop kit's `guard.py` as that block resolves its kit, vets it with
`check_reviewed_file`, and runs it over `$main_remote..$main_local`. Exit 1 refuses through
`write_refusal policy-unrecorded`, a token with no run-log decision; exit 2 refuses naming the reason
(deny by default); no launcher or no loop kit prints one line naming the miss, never silence.

### The command — `policy_edit.py`

| Verb | Proof | Writes |
|---|---|---|
| `set <key> <value> --build <slug> --unit <id>` | `check_terminal_proof` then the typed confirmation `yes`; or `check_run_mandate` | the leaf, the change record, both staged; prints the trailer |
| `raise <cap> <new> --build <slug> --unit <id> --argument <text>` | none, the agent door | the cap, its RAISED comment, the change record, both staged; prints the trailer and the decision row line for the caller |
| `propose <key> <value>` | none | nothing; prints the row diff and the command that would apply it |

`set` of `policy-file.proof` reads the value through `check_expansion_value` first. A `set` with no
proof prints the proposal and exits 1. The change record's fields: `Unit` the leaf's row tag,
`policy.<row name>` or a family tag such as `policy.budgets`; `Action` `edit`, or `add` for a key the
file did not set; `Before` and `After` that tag at the policy file's blob id before and after, eight
hex; `Mark` `semantic`; `Proof` `tty-cli`, `none — run mandate <run-state path>` or
`none — budgets raise`.

`raise` admits only when all hold, checked in this order and each refusal named:

1. The cap is a leaf under `budgets`, neither `budgets.enforce` nor `budgets.pinned`, set in the
   policy file at HEAD, its last segment a file tracked at HEAD, and `<new>` an integer larger than
   the value at HEAD. A cap whose value sits in its legacy home is the owner's to move into the file.
2. Condition 1 of the four: the working tree's file, measured CR-stripped in bytes, exceeds the old
   value.
3. Condition 2: the comment block directly above the cap carries no `reserved: owner` line.
4. Condition 3: the command writes `# RAISED <old> -> <new>, <date>, <unit>, measured <n> bytes,
   <argument>` directly above the cap, the shape the minimal guard checks.
5. Condition 4: the change record names the cap's row tag, and the command prints the decision row
   the caller must add to `memory/DECISIONS.md` in the same commit; the minimal guard refuses the
   commit without it.

The trailer is `Gov-Policy: policy.<key> <old> -> <new>`, one line per changed leaf, the key spelled
by `render_dotted`, each value rendered as compact JSON, `none` for a leaf the file did not set.

### The factory — `guarded_write.py`

`check_terminal_proof()` returns the proof `tty-cli` when `sys.stderr.isatty()` holds, else `None`,
the one stream dOrderedCharter-15 S5 tests. The typed confirmation `yes` is `policy_edit.py`'s own
step after the proof holds, outside the parity block, so `instructions_edit.py` gains no prompt.
`write_guarded(path, new_text, record)` reads the path's prior bytes, or that it did not exist, writes
`new_text`, or calls it where it is a callable writing the path itself, as the overlay's adder
`overlay.write_overlay_units` does, then calls `record`, the caller's record writer, for the record's
path; when either step raises, it restores the prior bytes, removing the path only where it did not
exist, and re-raises. The three-argument form is the one TOOL-dDeclaredLoop-67 S46 keeps. Both commands
carry the block inline because `tools/lib/` ships to no install; the parity row holds each copy to
the canonical.

### The floor

| Member | What it keeps | Its reader |
|---|---|---|
| `verdict-before-move` | a binding verdict runs before the default branch moves | `.githooks/pre-push`, at the `gate RED` refusal: `off` prints `floor: verdict-before-move off — the bar's red is advisory`, lets the push through with its allow record and writes no `gate-bar-green` for it |
| `record-changes` | every policy change and stage transition recorded | the verdict's step 3 and S6's push arm for `Gov-Policy:`; `check_transition_channels` for `Gov-Transition`, whose findings, `pending` and `unstored` lines then report and exit 0 |
| `guard-self` | the guard protects its own switch off a live run's branch | the verdict's step 2 |
| `no-actor-witness` | no stage witness reads actor-typed state | `check_site_witnesses` and `loop_lib.py --check`, whose refusal of an actor witness no list row names then reports |

Every member defaults `on`. Switching one `off` is a staged change to a `floor` member, which S3
refuses for every agent off a live run's branch: the owner's terminal commit lands it, and so does a
live run's commit carrying its change record, which step 3 and S6's push arm check (§8 F9). The
pre-push hook vets the loop kit's `floor.py` with `check_reviewed_file` before it reads it, and reads
it only on a red bar.

### Data model

```toml
# tools/loop/loop.toml — rows this unit adds
[[selects]]
key = "policy-file.proof"
value = "signed"
point = "point.instruction.signed-proof"

[[selects]]
key = "policy-file.proof"
value = "both"
point = "point.instruction.signed-proof"

[[selects]]
key = "instructions.proof"
value = "signed"
point = "point.instruction.signed-proof"

[[selects]]
key = "instructions.proof"
value = "both"
point = "point.instruction.signed-proof"

[[selects]]
key = "instructions.edit"
value = "flow-only"
point = "point.instruction.flow"
```

A row missing a string `key`, `value` or `point` is a `LoopError` naming it. `instructions_edit.py`
loads `guard.py` by file path under the module name `loop_guard`, so it never shadows the policy kit's
`guard` module that `read_policy_kit` imports by name. Each key this unit reads has a reader of the
shape the reader-coverage arm counts: `resolve("policy-file.guard")`, `resolve("policy-file.proof")`,
`resolve("policy-file.on-missing-expansion")` and `parse_key("floor")`.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `check_staged`, `check_push_range`, `check_expansion_value`, `main` | function | `tools/loop/guard.py` |
| `--staged`, `--push-range`, `--fixture`, `--plant`, `--selftest` | CLI flags | `tools/loop/guard.py` |
| `FLOOR_INVARIANTS`, `read_floor` | constant, function | `tools/loop/floor.py` |
| `set`, `raise`, `propose` | CLI verbs | `tools/loop/policy_edit.py` |
| `check_terminal_proof`, `write_guarded` | function | `tools/lib/guarded_write.py` |
| `guarded_write_py` | parity row and block marker | `tools/lib/resolve-python.test.sh` |
| `[[selects]]` | table | `tools/loop/loop.toml` |
| `POLICY_REL` | export | `tools/policy/policy-mirror.js` |
| `policy-unrecorded` | refusal token | `.githooks/pre-push` |
| `loop guard fixtures` | gate leg | `tools/gate-legs.json` |

Each function leads with a verb `.lexicon.conf` declares, in `py.function`'s snake case.

### The fixture cases

`guard.py --fixture --plant <case>` builds one scratch repository per case under the host temp
directory with `loop_witness.py`'s `write_fixture_files` and `run_fixture_git`, holding a branch `main`
with no remote, a tracked `AGENTS.md` of 118 bytes PINNED 2026-11-15 and a policy file whose `[budgets]`
sets `"AGENTS.md" = 100`, a census row of the policy kit's `caps.toml`. The kits are this tree's,
found beside the loop kit; a live run is planted as `check_policy.py`'s `guard-run-live` case plants
one. `--selftest` runs every plant through `loop_lib.py`'s `run_selftest_cases`.

| Case | Plant | Outcome |
|---|---|---|
| `raise-admitted` | `policy_edit.py raise AGENTS.md 120` and its decision row | exit 0; a refusal is RED |
| `raise-no-record` | the cap raised by hand with its `RAISED` line and decision row, no change record | exit 1 naming the change record |
| `raise-lowered` | the cap set to 90 by hand | exit 1, "a lowering" |
| `floor-off-agent` | `floor.no-actor-witness = "off"` staged under each guard value on a branch no run names | exit 1 naming `floor.guard-self`, three times |
| `floor-off-run` | under `owner-only` on a live run's branch, `floor.no-actor-witness = "off"` and a line dropped from the list file, staged with their change records, then without them | exit 0, then exit 1 naming each missing record |
| `other-write-owner-only` | `review.max-rounds` set with a change record | exit 1 naming `policy-file.guard` |
| `with-reason-admitted`, `with-reason-no-row` | `agents-with-reason`, a key set with its record, with and without the decision row | exit 0, then exit 1 |
| `mandate-live`, `mandate-none`, `owner-only-live` | `agents-within-mandate` on a live run's branch, then on a branch no run names; `owner-only` on a live run's branch | exit 0, exit 1, exit 0 |
| `push-no-trailer` | a commit changing the policy file with no `Gov-Policy:` line, graded by `--push-range` | exit 1 naming the commit |
| `proof-signed-refuse`, `proof-signed-fallback` | `policy_edit.py set policy-file.proof signed` under each value of `policy-file.on-missing-expansion` | exit 2 naming the point, then the substitution line |
| `set-run-live` | `policy_edit.py set review.max-rounds 4`, stderr a file, on a live run's branch, then `set floor.guard-self off` there | each leaf and its record written with the run-mandate proof, exit 0 twice |
| `floor-readers` | an actor witness no list row names and a transition with one channel missing, under the floor all `on`, then with `no-actor-witness` and `record-changes` `off` at the landed revision | both refuse, then both report and pass |

### Alternatives rejected

- **Extending `tools/policy/guard.py` in place.** One file, but the floor, the command and the push
  arm are the loop's, and the policy kit would then read the loop's floor.
- **The guard's own copy of the raise shape or the run admission.** Two implementations of one
  admitted shape; the minimal guard runs as a subprocess instead.
- **The floor members as catalogue rows.** I10 forbids a row; the map type carries their values.
- **`resolve("floor")` for the members.** It refuses the derived default and reads no member leaf.
- **Importing `guard.py` by name from the playbook kit.** It would shadow, or be shadowed by, the
  policy kit's `guard` module in one process.

### Files touched (estimate)

- `tools/loop/guard.py`
- `tools/loop/floor.py`
- `tools/loop/policy_edit.py`
- `tools/loop/loop.toml`
- `tools/loop/loop_lib.py`
- `tools/loop/loop_transition.py`
- `tools/loop/kit.toml`: the comment naming each new module's policy-kit read, no edge
- `tools/loop/README.md`
- `tools/lib/guarded_write.py`
- `tools/lib/resolve-python.test.sh`
- `tools/playbook/instructions_edit.py`
- `tools/playbook/layers.toml`
- `tools/playbook/core-pending.txt`: the `principle.p10` row
- `tools/policy/policy-mirror.js`: the `POLICY_REL` export
- `tools/policy/README.md`: "The guard", the verdict it now serves
- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `.githooks/pre-commit`
- `.githooks/pre-commit.test.sh`
- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `tools/gate-legs.json`: the leg `loop guard fixtures`, its `enforces` holding `principle.p10`
- `tools/govkit/registry.toml`: its `[[exempt_leg]]` row
- `tools/govkit/subject-pins.tsv`: its pin
- `tools/govkit/usage.toml`: one row per verb `help/policy.md` shows
- `tools/run-gates/selftest-budgets.txt`: its budget row
- `help/policy.md`
- `memory/guides/SESSION-KICKOFF.md`: the manifest-audit stamp, since its watch list holds `tools/gate-legs.json`
- `memory/map/generated/symbols.json`
- `memory/map/generated/inventories.json`

## 5. Production-readiness checklist

- security — the change narrows agent writes: the harness arm denies tool writes to the policy file,
  the verdict reads its rule from the landed revision, guard-self runs before every value off a live
  run's branch, and every policy change carries a record. The run admission is the owner's ruling,
  kept, and precedes guard-self (§8 F9). What that leaves unchecked: a live run can switch a floor
  member off, or change `policy-file.guard` or `policy-file.proof`, and only its change record and the
  push check witness it; a run's change to the list file has its change record alone, the push arm
  grading the policy file only. The other accepted residual is SA-1's pty wrapper,
  `git commit --no-verify` and `git push --no-verify`, each printed; the pre-push hook vets `guard.py`
  and `floor.py` but not the policy kit modules they import.
- perf / scale — one Python spawn per commit that stages a guarded path, as today, plus the minimal
  guard's subprocess; one spawn per default-branch push for the push arm, reading trailers once per
  range; the floor read on a red bar alone.
- error / empty / loading states — an absent list exits 0 as nothing guarded; an unparsable policy
  file reads as `policy-file.on-invalid` says; a missing launcher refuses, as dGroundRules-6's block
  does; a floor the reader cannot read reads all `on`.
- observability — one `loop-guard:` line per verdict naming the rule and each failed condition; the
  fallback line under `fallback-reported`; one `floor: <member> off` line per switched site.
- risks — a broken verdict blocks the owner's commits too only where stderr is not a terminal; the
  owner's terminal path does not run it. Guard-self binds off a live run's branch alone, so a run's
  own switch of the floor is caught only after the fact, by its record (§8 F9).
- testing — the fixture cases above, a parity row, a scratch-guard payload probe, a pre-commit
  stand-in arm and a pre-push stand-in arm.
- migration — none for data; the pre-commit block's verdict path moves in one commit; the repository's
  policy file sets no `floor` and no `policy-file.guard`, so every default holds.
- user docs — `help/policy.md`, its section "Who may change the policy file".
- write set — the new leg is gov's `[[exempt_leg]]` with a `subject-pins.tsv` row and a budget row in
  `tools/run-gates/selftest-budgets.txt`, priced by the builder's proxy reading PINNED with its date,
  held by `every held leg is budgeted, every budget row resolves`; the registry and budget rows trip
  `policy fixtures`. `help/policy.md` gains a usage marker per verb it shows, each with a
  `tools/govkit/usage.toml` row, held by `help page commands` and `docs`. The map's
  `symbols.json` and `inventories.json` regenerate with `python tools/codebase-map/gen_map.py --write`,
  held by `codebase-map coverage + freshness`, and trip `recall floor` and `recall floor arms`. The
  kickoff manifest's watch list holds `tools/gate-legs.json`, so the commit carries a `manifest-audit:`
  line and the stamp moves. The verdict-epoch delegate list names no file this unit writes. The loop,
  policy, playbook and hooks kits' shipped bytes move, so `kit epoch (shipped bytes move, the version
  moves)` owes each kit's version bump, minted by the lander. New shipped code spells `<prefix>` or a
  kit word, never `tools/`, for `install-prefix (shipped surface)`; the pre-commit block names the loop
  kit once, as `pg_kit` names the policy kit.
- existing arms — `policy fixtures`: the `guard-*` cases run the minimal guard, unchanged, and
  `policy-mirror.js` gains an export alone. `branch-guard self-test`: its stand-in guard sits under
  `policy/` with no `loop/` beside it, so the block runs the minimal guard as before. `pre-push
  self-test`, `pre-push run-log line` and `pre-push bar self-test`: a fixture with no loop kit prints
  one skip line, the arm sits under `--decide`'s skip, and the new token pairs with no run-log
  decision. `scratch-guard self-test`: no arm writes the policy file. `instruction edits selftest`: each
  case builds its own layer register and stages the owner through `Terminal`, which the inline block
  reads the same way; the load-refusal cases keep their lines. `instruction edits (manifest checks)`:
  `check_guard_witness` returns nothing once the point is declared. `core meta-check`: the pending row
  leaves in the commit the leg's `enforces` lands in. `loop definition`: `[[selects]]` is a table no
  check reads. `loop transition record`: at `on` every plant reads as today.

## 6. Acceptance criteria

- **AC1** — When `python guard.py --fixture --plant raise-admitted` runs in the loop kit, the staged
  single-cap raise written by `policy_edit.py raise` exits 0.
  Red when: the verdict refuses it, the arm the clause requires red if the guard refuses.
- **AC2** — When `python guard.py --fixture --plant raise-no-record` runs, it exits 1 naming the
  missing change record.
  Red when: a raise with no change record is admitted.
- **AC3** — When `python guard.py --fixture --plant raise-lowered` runs, it exits 1 with "a
  lowering".
  Red when: a lowered cap is admitted.
- **AC4** — When `python guard.py --fixture --plant floor-off-agent` runs, each of the three guard
  values refuses the staged `floor.no-actor-witness = "off"` on a branch no run names, naming
  `floor.guard-self`; and `python guard.py --fixture --plant floor-off-run` exits 0 with the change
  records staged, then exits 1 naming each missing record.
  Red when: any value admits an invariant switched off by an agent off a live run's branch, a live
  run's recorded change to the guard's own keys is refused, or an unrecorded one is admitted.
- **AC5** — When `python guard.py --fixture --plant other-write-owner-only` runs, it exits 1 naming
  `policy-file.guard`.
  Red when: an agent write other than the raise is admitted under `owner-only` off a run's branch.
- **AC6** — When `python guard.py --fixture --plant with-reason-admitted` and then
  `--plant with-reason-no-row` run, the first exits 0 and the second exits 1.
  Red when: `agents-with-reason` admits a write with no recorded reason, or refuses one that has it.
- **AC7** — When `python guard.py --fixture --plant mandate-live`, `--plant mandate-none` and
  `--plant owner-only-live` run, they exit 0, 1 and 0.
  Red when: a write outside a live run is admitted under `agents-within-mandate`, or the owner's
  ruling's run admission is lost under the default.
- **AC8** — When `python policy_edit.py set review.max-rounds 4 --build tFix --unit TOOL-tFix-1
  2>stderr.txt` runs in a fixture repository on a branch no run names, it prints the proposal, writes
  nothing and exits 1; and `python guard.py --fixture --plant set-run-live` prints each written leaf with
  `Proof: none — run mandate` and exits 0 twice.
  Red when: a `set` with no proof writes the policy file off a live run's branch, or a run's `set` of
  a guard key is refused, against the owner's ruling.
- **AC9** — When `python policy_edit.py raise AGENTS.md 120 --build tFix --unit TOOL-tFix-1 --argument
  probe` runs in a fixture repository whose `AGENTS.md` measures 118 bytes PINNED 2026-11-15, it writes
  the RAISED comment and the change record and prints one `Gov-Policy:` line; with `AGENTS.md` at 90
  bytes PINNED 2026-11-15 it refuses naming condition 1.
  Red when: the raise is admitted with the file under its old cap.
  fixture: a scratch repository planted as the `raise-admitted` case plants its own; the tree holds none.
- **AC10** — When the blocks are cut with
  `sed -n '/# >>> guarded_write_py/,/# <<< guarded_write_py/p'` from `instructions_edit.py`, from
  `policy_edit.py` and from the canonical `guarded_write.py`, `cmp` finds each copy equal to the
  canonical; and in the canonical's block `grep -c 'sys.stderr.isatty()'` prints 1 and `grep -c 'stdin'`
  prints 0.
  Red when: a copy differs from the canonical, or the block tests stdin, which would move
  dOrderedCharter-15's owner-settled proof to another stream.
- **AC11** — When `python guard.py --fixture --plant push-no-trailer` runs, it exits 1 naming the
  commit and the policy file `policy.toml`.
  Red when: a policy change with no `Gov-Policy:` trailer passes the push arm.
- **AC12** — When `python guard.py --fixture --plant proof-signed-refuse` and then
  `--plant proof-signed-fallback` run, the first exits 2 naming `point.instruction.signed-proof` and
  the second prints the substitution of `tty-cli`; and `python floor.py get guard-self` prints `on` in
  a repository whose policy file holds no `[floor]` table.
  Red when: a value selecting an absent component is read silently, or an absent member reads `off`.
- **AC13** — When `grep -n point.instruction.guard layers.toml` runs in the playbook kit, it prints
  the `layer.flow` row's `declares` line; and `python instructions_edit.py add --manifest overlay --tag
  repo.probe --type directive --level 3 --trigger always --text "MUST probe." 2>err.txt`, standard
  error a file, exits 1 printing `not proven` and writing nothing, where it printed `every write waits
  on the guard` before.
  Red when: the point is absent and the instruction command still refuses for the guard.
- **AC14** — When `node scratch-guard.js` in the hooks kit is fed a PreToolUse Write payload for the
  policy file `policy.toml`, it prints a deny naming `policy_edit.py`.
  Red when: the write gate admits a tool write to the policy file.
- **AC15** — When `grep -n 'lg_kit' .githooks/pre-commit` runs, it prints the loop kit named once and
  its `resolve_kit_gate "$lg_kit" guard.py` call, ahead of the minimal guard's.
  Red when: the block still runs the minimal guard where the loop kit's guard resolves.
- **AC16** — When `grep -n policy_edit.py policy.md` runs under `help/`, it names the command under
  "Who may change the policy file".
  Red when: the page is not current.
- **AC17** — When `python guard.py --fixture --plant floor-readers` runs, `check_site_witnesses()` and
  `check_transition_channels` each refuse their planted case under the floor all `on`, and each prints
  `floor: <member> off` and passes once the landed revision sets that member `off`.
  Red when: a switch has no reader, so turning it off changes nothing, or `on` stops refusing.
- **AC18** — When `python -m json.tool gate-legs.json` runs in the tools folder, the row named
  `loop guard fixtures` carries `enforces` holding `principle.p10`, and
  `python tools/playbook/core.py meta-check` on this unit's pass exits 0, naming neither that leg nor a
  stale pending row.
  Red when: the leg carries no `enforces`, which dOrderedCharter-7 S3's meta-check reds, or the
  `principle.p10` pending row stays.
- **AC19** — When `.githooks/pre-push` runs a default-branch push in a scratch repository holding a
  stand-in loop kit, a stand-in `guard.py` exiting 1 refuses the push and writes the token
  `policy-unrecorded` to `pre-push-refusal`; and over a STUB bar exiting 1, a stand-in `floor.py`
  printing `off` lets the push through printing `floor: verdict-before-move off` with no
  `gate-bar-green` written, while `on` refuses as today.
  Red when: the push arm is not called, or `off` changes nothing, or a red writes a green record.
  fixture: the scratch repository the new arm of §7 stages; the tree holds none.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `loop definition` · `loop transition record` · `loop parent routes` · `policy fixtures` · `policy check` · `instruction edits (manifest checks)` · `instruction edits selftest` · `layer dependencies (the core never depends on an expansion)` · `core meta-check` · `scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `routed-commits selftest` · `branch-guard self-test` · `pre-push self-test` · `pre-push run-log line` · `pre-push bar self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `hook destinations self-test` · `govkit acceptance matrix` · `govkit selftest` · `govkit refusal join` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `playbook render selftest` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `every held leg is budgeted, every budget row resolves` · `docs` · `help page commands` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `line length`

New arm: tools/loop/guard.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC11 AC12 AC17 · each `--plant` case staged in its scratch repository, and `raise-admitted` red with the verdict forced to refuse · none

New arm: tools/hooks/scratch-guard.test.sh · covers AC14 · a Write payload for the policy file · the suite's assertion floor raised by the arms added

New arm: tools/lib/resolve-python.test.sh · covers AC10 · the `guarded_write_py` row with one copy edited · none

New arm: .githooks/pre-commit.test.sh · covers AC15 · a stand-in loop kit `guard.py` beside the stand-in policy guard, which must run instead of it · none

New arm: .githooks/pre-push.test.sh · covers AC19 · a stand-in loop kit whose `guard.py` exits 1, and whose `floor.py` prints `off` over a STUB bar exiting 1 · none

## 8. Open questions

- **F1 — Where does the guard verdict live?** (a) `tools/loop/guard.py`, wrapping the minimal guard by
  subprocess; (b) `tools/policy/guard.py` extended in place; (c) a loop module importing the policy
  kit's shape check. (c) breaks the rule that a kit never imports a sibling. (b) puts the run-state
  grammar inside the policy kit. (a) keeps one implementation of the admitted shape and follows I1
  and I12. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-24, delegated): (a).
  grants: PLAY-dClosedLoop-3 the pre-commit block's verdict re-pointed to the loop guard ·
  widens: none · relaxes: none
- **F2 — Where does the shared terminal proof live?** (a) `tools/lib/guarded_write.py`, carried
  inline in both commands under a `PARITY_ROWS` row; (b) in the playbook kit, imported by the loop;
  (c) a second copy. (b) is a sibling import and (c) is the copy the [reuse] rule forbids at a second
  instance. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-24, delegated): (a).
  grants: PLAY-dClosedLoop-3 the instruction command's terminal check re-pointed to the inline block
  · widens: none · relaxes: none
- **F3 — The floor members' names.** v2's `[floor]` and R5.1 state the four invariants in prose; I11
  spells them `verdict-before-move`, `record-changes`, `guard-self` and `no-actor-witness`. Rung 1, the
  invariants as v2 states them, spelled as the brief fixes. RESOLVED (agent, 2026-10-24, delegated):
  I11's four. widens: none · relaxes: none
- **F4 — What do `agents-with-reason` and `agents-within-mandate` admit?** R4.2 offers "agents with a
  recorded reason" and "agents within a mandate". (a) A recorded reason is a change record plus a
  decision row in the same commit; a mandate is a live run whose `run-branch:` is the commit's
  branch. (b) A free-text reason in the trailer. (b) is text anyone types and records nothing a gate
  reads. Recommendation (a). Rung 1, R4.2's words. RESOLVED (agent, 2026-10-24, delegated): (a).
  widens: none · relaxes: none
- **F5 — Does the harness arm cover hooks and verdict refs too?** v2's `[witnesses]` lists all three;
  this clause names the policy file's guard. Covering hooks would refuse tool writes to `.githooks/`,
  a write surface no clause of this build prices. Recommendation: the guarded paths list only, the
  rest handed off. Rung 3. RESOLVED (agent, 2026-10-24, delegated): the guarded paths list only.
  grants: PLAY-dClosedLoop-3 the scratch-guard write gate's policy-path arm · widens: none ·
  relaxes: none
- **F6 — Where are the values that select an absent component declared?** (a) `[[selects]]` rows of
  the loop definition, one function reading them; (b) a field on each catalogue row; (c) each
  reader's own refusal, as dOrderedCharter-15 does today. (b) edits rows I10 says this unit leaves
  alone, and (c) is the per-reader copy gap-spine-07 names. Recommendation (a), re-pointing
  dOrderedCharter-15's two refusals. Rung 3. RESOLVED (agent, 2026-10-24, delegated): (a).
  grants: PLAY-dClosedLoop-3 the instruction command's two load refusals re-pointed · widens: none ·
  relaxes: none
- **F7 — Which layer row declares `point.instruction.guard`?** dOrderedCharter-15 S4 reads any core
  row; the guard is the flow's, and `layer.flow` is a core row. Rung 1. RESOLVED (agent, 2026-10-24,
  delegated): `layer.flow`. widens: none · relaxes: none
- **F8 — How do the three values meet the owner's 2026-11-12 run admission?** The minimal guard now
  admits a live run's branch under the default, which F4 (a)'s mandate row made stricter than the
  default. (a) The run admission holds under every value, as PLAY-dOrderedCharter-84 says the ruling
  wants; `agents-within-mandate` reads as `owner-only`, which the ruling widened to it, and
  `agents-with-reason` adds a recorded write off a run's branch; `set` writes on a live run's branch
  without the terminal, so a run has the recorded door. (b) `owner-only` drops the run admission and
  this repository sets `agents-within-mandate`, which reverses the ruling for every adopter. (c)
  `agents-within-mandate` demands a reason on a run's branch, a value stricter than the default.
  Recommendation (a): it keeps the ruling, keeps F4's reason rule, and leaves no value stricter than
  the default. Rung 3. widens: none · relaxes: none
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 1: the owner's 2026-11-12 ruling that no file is owner-only to a run
  widens: none · relaxes: none
- **F9 — Does guard-self bind on a live run's branch?** (a) Yes: S3 runs before the run admission, so
  a run may change any key but `policy-file.guard`, `policy-file.proof`, the `floor` members and the
  list file, which stay the owner's terminal's. (b) No: the run admission precedes it, and a run may
  change those keys and the list file, each with its change record, so it may switch its own floor
  off. v2's `[floor]` says each invariant is switchable only under the guard, and the run admission
  is part of the guard. (a) narrows an owner ruling, which an unattended run does not do.
  Recommendation (b): the owner's 2026-11-12 ruling reads "No file is owner-only to a run working
  under its build's mandate", and (b) keeps it whole, the record and the push check witnessing what a
  run switches. Rung 3. widens: none · relaxes: none
  RESOLVED (agent, 2026-11-15, delegated): (b), rung 1: the owner's 2026-11-12 ruling that no file is owner-only to a run
  widens: none · relaxes: none
- **F10 — Which paths does the harness arm deny?** F5 settled the guarded paths list, and since then
  the ruling admits a run's hand edits of `.governance/deploy.toml` and
  `.governance/instructions.toml`, whose writers are other tools. (a) The policy file alone, the one
  path whose door this unit builds and the one v2's `[witnesses]` names. (b) Every listed path, which
  denies a run the edits the ruling admits. Recommendation (a). Rung 3. widens: none · relaxes: none
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: the ruling leaves deploy.toml and instructions.toml to runs
- **F11 — Does the push arm grade a commit that adds the policy file?** The kit's scaffold writes it
  with four set keys, and an adopter's first default-branch push would need four trailers. (a) No: a
  commit whose parent lacks the file is printed and not graded, and the pre-commit verdict refuses an
  agent's adding commit off a live run's branch. (b) Yes, every leaf a change. Recommendation (a).
  Rung 3. widens: none · relaxes: none
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: an adopter's scaffold commit adds the file

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-43, a hands-off TOOL-dDeclaredLoop-44, a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.
- rev-3 · 2026-10-25 · S5 · §4 Evidence, The command, The factory · AC8 · AC10 · re-grounded on
  dOrderedCharter-15 rev-5 by `build/2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md`
  row 12: `check_terminal_proof` tests stderr, as that unit's S5 and the owner's pick of its §8 F4 do; the
  typed `yes` is `policy_edit.py`'s alone, outside the parity block; AC8 redirects stderr, not stdin.
- rev-4 · 2026-11-05 · S12 · §4 Files touched · AC18 · TOOL-dDeclaredLoop-56 §8 F5 (a), per the brief
  `2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade`: the leg `loop guard fixtures` carries
  `principle.p10`, settled here by TOOL-dDeclaredLoop-3 §8 F7's rule; its own pass writes it, so the core
  meta-check never reds the leg.
- rev-5 · 2026-11-15 · §1 · S1 S2 S3 S4 S5 S6 S8 S9 S10 S11 S12 S13 S14 · §3 · §4 · §5 · AC1 AC4 AC5
  AC7 AC8 AC9 AC10 AC12 AC13 AC14 AC15 AC17 AC18 AC19 · §7 · §8 F8 F9 F10 F11 · §10 · re-grounded at
  HEAD `c91665355` by the brief 2026-11-15-prompt-TOOL-dDeclaredLoop-2-reground-brief; mechanism,
  carries, order and status kept. PLAY-dOrderedCharter-84 made the minimal guard admit a live run's
  branch on the owner's 2026-11-12 ruling: F8 keeps it under every value, `set` writes on a run's
  branch, F9 follows the owner's ruling, the run admission preceding guard-self and a run's change
  to the guard's own keys or the list file carrying its change record (the brief
  2026-11-15-prompt-TOOL-dDeclaredLoop-2-f9-brief), F10 narrows the harness arm to the policy file. The policy
  kit is read through `read_policy_kit`; `floor`'s derived default makes `read_floor` read the table
  itself; the points are `point.instruction.*`; the change record's tag is the row's; the fixture cap
  is `AGENTS.md`, a census row; the factory keeps `write_candidate`'s prior-bytes restore; five
  `[[selects]]` rows, since the re-pointed refusals need theirs; the no-actor-witness readers are
  `check_site_witnesses` and the list check; the leg is gov's `[[exempt_leg]]` and the `principle.p10`
  pending row, now in the tree, goes with its readers clause; the pre-push push arm and floor read sit
  beside the merge-loss block and at the `gate RED` refusal, observed by AC19; the commit-time record
  check names AC2's missing record; the write set gained the registry, pin, usage, budget, map,
  kickoff and test rows, and §7 the legs they trip. Code cited by symbol.

## 10. Reuse audit

The seams extended: dGroundRules-6's minimal guard, `tools/policy/guard.py --staged`, run as the
`owner-only` and `agents-within-mandate` arms, with its `derive_leaf_changes`, `check_decisions_row`,
`check_parent_sides` and `check_run_mandate` called in process through
`tools/loop/loop_parents.py#read_policy_kit` and never re-implemented; the policy kit's `resolve`,
`read_revision` and `check_value`; `tools/memory-tree/build_records.py#write_change`, which
`python tools/codebase-map/reuse_lookup.py "refuse an agent write to the policy file unless an
interactive terminal confirms it"` ranks as a seam, for every change record; the memory-tree kit's
`read_commits` for the trailer; `instructions_edit.py`'s `write_candidate` and `run_write`, whose
rollback and terminal test become the factory at their second instance; the write gate's evaluation
order, `tools/hooks/scratch-guard.js#checkRouted`, which gains one arm, and `resolvePolicyHelper`,
which finds the path it guards; the pre-commit block dGroundRules-6 S4 places, whose verdict path
moves; the pre-push merge-loss block, whose resolution and refusal the push arm copies in shape; the
`PARITY_ROWS` table of `tools/lib/resolve-python.test.sh`; and `loop_witness.py`'s fixture helpers
with `loop_lib.py`'s `run_selftest_cases`. For the floor's map read and the expansion rule no existing
seam fits: the same probe ranked only name-stem hits (`write`, `read_policy_value`, `PolicyRefused`),
and `resolve("floor")` refuses the derived default.

Recall terms used: `python tools/memory-recall/query.py "who may raise a measured file cap and how is
the policy file guarded" --terms "policy guard minimal guard RAISED budgets cap template-size-limits
owner terminal TTY proof floor run-branch mandate"`
