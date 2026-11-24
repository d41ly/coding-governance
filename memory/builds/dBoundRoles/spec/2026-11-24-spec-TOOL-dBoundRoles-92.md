# TOOL-dBoundRoles-92 — the closing review's round-1 minors folded, and the reviewers step row declares the atomic resume unit 43 owed

**Status:** CLOSED · rev-1 · 2026-11-24 · node a · Tier-2 · base f3ec096a8 · streams tooling · order 46

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 TOOL-dBoundRoles-86 TOOL-dBoundRoles-87 TOOL-dBoundRoles-88 TOOL-dBoundRoles-89 TOOL-dBoundRoles-90 TOOL-dBoundRoles-91 |
| [2026-11-24-build-TOOL-dBoundRoles-92-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dBoundRoles-92-1-acceptance-ledger.md) | journal | — |
| [2026-11-24-build-TOOL-dBoundRoles-92-deviation-921.md](../build/2026-11-24-build-TOOL-dBoundRoles-92-deviation-921.md) | deviation | — |
| [2026-11-24-prompt-TOOL-dBoundRoles-92-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-92-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dBoundRoles-92-spec-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-92-spec-brief.md) | journal | — |
| [2026-11-24-review-TOOL-dBoundRoles-86-closing-diff-review-round2.md](../reviews/2026-11-24-review-TOOL-dBoundRoles-86-closing-diff-review-round2.md) | diff-review | TOOL-dBoundRoles-86 TOOL-dBoundRoles-87 TOOL-dBoundRoles-88 TOOL-dBoundRoles-89 TOOL-dBoundRoles-90 TOOL-dBoundRoles-91 |

<!-- /gen:spec-records -->

## 1. Goal

Close the minors of the closing diff review's round 1, M1 to M14 and L1 to L4 of
`memory/builds/dBoundRoles/reviews/2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1.md`.
Most of them leave a branch that reads correctly today with no check that fails when it breaks, and the
rest are small defects. The same batch declares `resume = "atomic"` on the reviewers step row, which the
landing freezes.

## 2. Scope (IN)

Each item takes the report's stated fix, the skeptic's class-level one where the report names it.

- **S1** — M1, finding 7. `scanInPlaceOperands` (`tools/hooks/scratch-guard.js@f71f3b8c:475`) stops a perl
  short cluster's walk at a value-taking switch, `M`, `m`, `I`, `F`, `C`, `D`, `x` or `V`, the rest of the
  word being its value; a bare `-I` consumes the next word. Observed by AC1.
- **S2** — M2, finding 8. The `--` branch of the same function marks the options ended and continues the
  operand logic, so the first word after it is the script while none was named. Observed by AC2.
- **S3** — M3, finding 12. `print_input_facts` (`tools/roles/handoff.py#print_input_facts`) prints each
  `text` fenced by `lib.render_handed_fence`, so `HANDED` in `tools/workflows/unattended-unit.js@ee9e2dbb:299`
  hands both documents inside a fence no line of theirs closes (§8 F2). `tools/roles/README.md` and
  `help/roles.md` say the text is fenced. Observed by AC5.
- **S4** — M4, finding 14. The `roles.retries` row of `tools/policy/catalogue.toml` declares `max = 4` (§8 F1),
  and a fixture case, `retries-attempts-join`, joins that maximum to the length less one of every `ATTEMPTS`
  literal the workflows kit's harness sources declare. `help/reference/policy.md` and
  `.governance/policy.json` are re-rendered by their own renderers; `help/roles.md` names the maximum.
  Observed by AC6 and AC7.
- **S5** — M5, finding 16. `check_stop_replay` (`tools/govkit/selftest.py#check_stop_replay`) gains a positive
  control: a marked direct-spawn stop with a malformed return, piped through the installed command, is
  blocked (§8 F3). Observed by AC8.
- **S6** — M6, finding 17. A position plant, `refusal-typed`, records a refusal with `--rule`, `--remedy` and
  `--actor` and asserts the three fields and the trimmed reason; `render_position_lines`
  (`tools/loop/position.py#render_position_lines`) prints the three on a typed refusal's line;
  `write_refusal` refuses an untyped reason that spells the typed tail (§8 F4). Observed by AC9 and AC10.
- **S7** — M7, finding 18. The driver's suite arms each refusal line of `write_refusal`
  (`tools/unattended/unattended.sh@d360a6b1:16891`) with the skeptic's corrected arms. Observed by AC11.
- **S8** — M8, finding 19. The spawn guard's suite plants every refusal of `checkFraming`
  (`tools/roles/spawn-guard.js#checkFraming`), each asserting its own text. Observed by AC14.
- **S9** — M9, finding 20. The same suite arms the three source forms of `checkFactKeys`
  (`tools/roles/spawn-guard.js#checkFactKeys`). Observed by AC15.
- **S10** — M10, finding 21. The `spawn-guard self-test` row of `tools/govkit/registry.toml` guards the files
  its suite reads (§8 F6), and `tools/gate-legs.json` is re-rendered from it. Observed by AC16.
- **S11** — M11, finding 22. The wiring checker's suite arms the return-check fragment branch at
  `tools/check-wiring.sh@d80db82f:1880`. Observed by AC17.
- **S12** — M12, finding 23. The F6 arm at `tools/memory-tree/check-memory-hygiene.test.sh@807b34a1:4725`
  resolves the playbook kit's `principles.toml` itself: where it resolves the refusal line is required and the
  note fails the arm, and where it does not the note alone passes. Observed by AC18.
- **S13** — M13, finding 24. The scratch guard's suite gains a work order under the harness-run transcript
  folder and a first record over `TRANSCRIPT_READ_BOUND`. Observed by AC3.
- **S14** — M14, finding 26. The driver's suite arms the FORKED hold's reader refusal, the answer outside the
  closed set, the absent roles kit, the `owner` answer, a `park-build` over two FORKED units, and a passing
  control that asserts `dispatch declared`. Observed by AC12.
- **S15** — L1, finding 10. The `park-item` and `park-build` answers at
  `tools/unattended/unattended.sh@d360a6b1:18587` park no row the run-state file already holds, and still
  refuse (§8 F5). Observed by AC13.
- **S16** — L2, finding 15. The comment above the `actor` row of `tools/loop/item-schema.toml@19a8f30a:50`
  says a patch naming a repository role is judged by `check_roles.py --check-actor-patch` and any other value
  is refused. Observed by AC19.
- **S17** — L3, finding 25. The scratch guard's suite gains a row per contract shape that has none, and the
  rows that make `checkDriverRead` throw. Observed by AC4.
- **S18** — L4, finding 30. `place` reads `outcome`, `rule`, `remedy` and `actor` from the return object before
  its key check, and refuses an `outcome: refused` by its own text naming `route-refusal`, on the JSON shape
  and the `key: value` shape alike. Stage 1 of `tools/roles/SKILL.template.md`, its render, the kit README's
  Skill paragraph and `help/roles.md` send a refused return through `route-refusal`, the scout spawned again
  only on a `self` route or a malformed return. Observed by AC20 and AC21.
- **S19** — The `roles/reviewers-to-gov-reviewer` row of `tools/roles/kit.toml` declares
  `resume = "atomic"`, as TOOL-dBoundRoles-43 S37 and its §8 F11 resolved and its ledger's AC37 answer owes.
  The row freezes at the landing, so this is its last pass. Observed by AC22.
- **S20** — Each suite's floor and each budget row moves with the arms above, in the one place §4 "Floors and
  budgets" states. Observed by AC23.

## 3. Non-goals (OUT)

- The parts of findings the H3 and H5 items carry, and every BLOCKER and HIGH of the report: the sibling
  units of this set own them.
- The left-shift gates the report proposes beside a fix: a refusal-text coverage walk of the spawn guard, a
  leg-guard derivation in `gate-leg conformance`, a re-run check over every `park` call, and a row set joined
  to a header's contract list. The arms here are the regression gates of their findings.
- `verb_propose` and `verb_park`, which keep their own exact-line compare.
- A clamp in any harness, and any change to `ATTEMPTS`.
- Any write of a landed step row, or of the `roles/house-overlays-to-instructions` row.

This unit is last in the order. `TOOL-dBoundRoles-89` gives `read_scout_return` the JSON reading S18 reads
through; the siblings that edit `scratch-guard.js`, `spawn-guard.js`, `unattended-unit.js` and `handoff.py`
land before it, so each cite here is re-read at the pass and a row a sibling's arm already holds is not added
twice. `TOOL-dBoundRoles-43` owed S19 and is CLOSED.

### Edges

none

## 4. Design

### Evidence

Probed at HEAD `c31769972`, whose `tools/` tree equals base `f3ec096a8`'s. Every defect still holds.

| item | probe | reading |
|---|---|---|
| M1 | `scanWriteTargets` over the report's three commands, in-process | each returns a `perl -i` target; `perl -I lib -pi -e 1 x.py` and `perl -pi -e 1 x.py` return `x.py` |
| M2 | the same over `sed -i -- s/a/b/ out.txt` and `perl -pi -- s/a/b/ out.txt` | each returns `s/a/b/` beside `out.txt` |
| M3 | `readWorkOrderAllowance` over a prompt holding an unfenced `## Task` and `### allowance` under `### input:prompt` | the handed entry is returned; the same text inside a four-backtick fence returns `why` and no entry |
| M4 | the row at `tools/policy/catalogue.toml@4d7897c8:273`; `ATTEMPTS` in the three harness sources | `min = 0` and no `max`; each literal is `[0, 1, 2, 3, 4]` |
| M5 | `grep -rl return-check.sh tools` over scripts, descriptors and Python | the shim, its fragment and `handoff.py`, no suite; the shim fed a direct-spawn stop in a scratch repository prints `decision: block` and writes the record |
| M6 | `REFUSAL_TAIL_RE.fullmatch` over `x · rule r · remedy m · actor owner` | splits as typed, actor `owner`; `render_position_lines` prints item, key and reason (`tools/loop/position.py@077196d1:742`) |
| M7 | grep of the driver's suite for a partial set and `--actor build` | no row |
| M8, M9 | fixed-string grep of `spawn-guard.test.sh` for each refusal text past the role refusal, and for `record:card/` | none occurs |
| M10 | the row at `tools/gate-legs.json@fc85cb7a:3092` | four guard paths; the suite reads `handoff.py` (`tools/roles/spawn-guard.test.sh@31658241:1006`), `roles_lib.READ_FAMILIES` through it, the policy kit and `spec-audit-optin.js` |
| M11 | `grep -c` of `return-check` and `SubagentStop` in `check-wiring.test.sh` | 0 |
| M12 | read of the arm and of the engine's reader (`tools/memory-tree/check-memory-hygiene.sh@09d1d1f8:2294`) | the note is printed on any non-zero exit of the reader, and the arm accepts it |
| M13 | grep of `scratch-guard.test.sh` for `runs past` and `subagents/workflows` | 0 |
| M14 | grep of the driver's suite for the reader's refusal words, the no-kit NOTE and `answers owner` | 0; the control asserts `miss` on `grades FORKED` alone |
| L1 | read of both answers | `park` is called with no compare |
| L2 | read of the comment against `check_actor_patches` (`tools/loop/loop_items.py#check_actor_patches`) | the function admits a conforming repository role |
| L3 | grep of `scratch-guard.test.sh` for `perl -`, `rename to`, `appendFileSync`, `AppendAllText`, `WriteAllBytes`, `write_bytes`, `--in-place` and the read arm's throw text | 0 each |
| L4 | `read_scout_return` over a refused return in both shapes, in-process | `line 2 is no key: value`, and `line 1` for JSON |
| atomic | `read_steps` at HEAD, in-process | the row's `resume` is `None`; `check_frozen` from `origin/main` to HEAD reports no problem, and `origin/main`'s descriptor holds no such row |

### Product changes

- **S1, S2.** In the cluster walk, for perl, a letter of `MmIFCDxV` ends the walk, and `I` as the word's last
  letter consumes the next word. The test sits before the `i` test, so `-Ilib` is a value and `-pi` is in
  place. The `--` branch sets a flag the option branches read and continues.
- **S3.** One call in `print_input_facts`, after the placeholder check, so the key and the class are unmoved.
  Nothing parses `text` but the unit harness's concatenation. `HANDED` and the harness's checks are
  unchanged, so a facts list an older roles kit printed is handed as today.
- **S4.** `allowed = { type = "retry-count", min = 0, max = 4 }`, a shape `runtime.refusal-repeats` already
  declares and `tools/policy/policy.py#check_value` already reads. The case reads
  `unattended-build.template.js`, `tier2-review.template.js` and `unattended-unit.js`, found by the fixture's
  `resolve_kit_dir`, takes every `const ATTEMPTS = [...]` literal, and is wrong where a length less one
  differs from the row's `max`, or where either template declares none. A harness with no literal is named in
  the case's line, so the unit harness, whose literal `TOOL-dBoundRoles-90` takes out, leaves the join. The `policy fixtures` row of
  `tools/govkit/registry.toml` gains the sources its guard lacks.
- **S6, driver half.** In `write_refusal`, where `--rule`, `--remedy` and `--actor` are all empty and the
  reason matches the glob `*" · rule "*" · remedy "*" · actor "*`, the malformed-refusal message is set and the
  one check-48 refusal fires. The glob is a superset of `REFUSAL_TAIL_RE`, which the loop kit owns.
- **S6, position half.** A refusal whose `actor` is non-empty prints
  `refusal — <item> · <key> · <reason> · rule <r> · remedy <m> · actor <a>`.
- **S10.** The guard is the standing rows plus `{prefix}/roles/handoff.py`, `{prefix}/roles/roles_lib.py`,
  `{prefix}/policy/`, `{prefix}/workflows/spec-audit-optin.js` and `{prefix}/lib/`. Rendered by
  `python tools/run-gates/leg_factory.py --write`, never by hand.
- **S15.** `check_row_recorded <run-state path> <row text after its timestamp>` is the exact-line compare
  `write_refusal` makes, moved out whole, and answers 0 where the row stands. `write_refusal` and both answers
  call it; the answers skip `park` and the stage and fall to the same check-49 refusal.
- **S18.** The refusal is made where the return is read into its object, before any key is compared:
  `the return's outcome is refused (rule <r> · actor <a>), so it carries no placement: route it with
  handoff.py route-refusal --return <file>`. `check_scout_return` still grades the refusal arm first, so a
  malformed refusal keeps its own defect lines.
- **S19.** One line in the row. `read_steps` reads the word as no argv
  (`tools/govkit/upgrade_steps.py@6bd6fbe4:934`), and `reviewer_merge.py` already restores on failure.

### Arms

- **S13.** The fixture's `sw7sess/subagents/workflows/wf_x/` holds an agent's transcript whose allowance a write
  falls outside, and a direct transcript's first record runs past the bound.
- **S17.** One scan row per alternative of `INTERPRETER_WRITES` and open mode with none: `write_bytes`,
  `appendFileSync`, `WriteAllBytes`, `AppendAllText`, and `open` in modes `a`, `x` and `r+`; `sed --in-place`
  and its suffix form; `perl -i`; a patch's `rename to` line; and the preloaded throw, the main loop's search
  at exit 2 naming the read arm and a worker's at exit 0.
- **S5.** The control writes `<session>/subagents/agent-<id>.jsonl`, its first `user` record opening with a
  `gov:handoff` marker, and a payload with a `last_assistant_message` that is no return object, then runs
  every `SubagentStop` command of the install with `GOV_DEFAULT_BRANCH` naming the target's branch. Exactly
  one prints a `decision: block` object at exit 0 and leaves the agent's record. Its failing case is the
  installed shim's last line replaced by `exit 0`. That the scratch target's landed revision resolves under
  that variable is UNVERIFIED; the policy kit is in the default selection.
- **S8.** The plants: two `framing:job` headings; zero and two `Framed by:` lines; a line before the block and
  one after it; a malformed spelling; a path outside `builds/<build>/prompts/` and one holding `..`; a missing
  file; a file with no marker and one with two; a mismatched task-sha. A plant another refusal reaches first
  is re-shaped until its own text prints.
- **S9.** A card fact unchanged is admitted; changed, and with the card absent, refused; a key with `..` under
  a slash and under a backslash, a leading-slash key and a drive-letter key each refused as naming no path
  inside the checkout; a removed source refused.
- **S7.** `--rule` with `--actor driver` and no `--remedy`; `--remedy` with `--actor driver` and no `--rule`; a
  full rule and remedy with no `--actor`; a separator-bearing rule and a separator-bearing remedy, each with a
  valid actor; `--actor build:` and `--actor build:a/b` refused; `--actor build:dX` admitted. Each refusal
  asserts its own words, a non-zero exit and unchanged bytes.
- **S14.** The driver copied beside a stub `handoff.py` that exits 2 naming words, then one printing an answer
  outside the set, each refused by check 49 with those words; beside no roles kit, the NOTE and the `resolve`
  answer; a landed policy value the real reader answers `owner` to; two FORKED specs under `park-build`, both
  ids in the row; and the control.
- **S11.** A scratch install holding the roles kit's fragment and shim, rendered: with no `SubagentStop` entry,
  `UNWIRED  roles` naming the fragment and exit 1; with it, an `ok` line.

### Floors and budgets

Each floor rises by the assertions this pass adds, counted off the block's own lines and said in the comment
above the pin; the value raised is the one HEAD holds at the pass, since siblings move the same pins.

| suite | floor | items |
|---|---|---|
| `tools/hooks/scratch-guard.test.sh` | `FLOOR_ASSERTIONS` | S1, S2, S13, S17 |
| `tools/workflows/unattended-build.test.sh` | `FLOOR_ASSERTIONS` | S3 |
| `tools/roles/spawn-guard.test.sh` | `FLOOR_ASSERTIONS` | S8, S9 |
| `tools/unattended/unattended.test.sh` | the effective `FLOOR_ASSERTIONS`, with `FLOOR_SHARD_3` for S6 and S7 and `FLOOR_SHARD_4` for S14 and S15 | S6, S7, S14, S15 |
| `tools/memory-tree/check-memory-hygiene.test.sh` | `FLOOR_ASSERTIONS`, unmoved unless the arm gains an assertion | S12 |
| `tools/check-wiring.test.sh`, `tools/govkit/selftest.py`, the policy fixture, the loop fixtures | none | S11, S5, S4, S6, S18 |

The rows of `tools/run-gates/selftest-budgets.txt` for those suites are re-priced as that file's PINNED proxy,
each saying what was added and that no suite ran; a row stating `plants=` moves that count. The main loop
re-prices from its first reading.

### Inventory

Minted: `check_row_recorded` (`sh.function`, asked of `python tools/lexicon/lexicon.py --suggest
check_row_recorded --as sh.function`, OK), the fixture case `retries-attempts-join`, and the plants
`refusal-typed` and `return-refused`.

### Migration

A policy file holding `roles.retries` above 4 now reads invalid and takes `policy-file.on-invalid`, where every
harness call already threw on it. A fenced `text` needs no step. The upgrade row is unlanded, so declaring
its resume moves no adopter.

### Rollout

Live at landing, at order 46. The catalogue is not on `tools/policy/guarded-paths.txt`, so it goes in the
unit's own pass commit. `.governance/policy.json` is on it and `mirror --write` refuses an uncommitted
catalogue, so the re-rendered mirror is the next commit alone, `Pass: none`, admitted on the live run's branch.
The `gate-legs.json` edit moves a path the kickoff manifest watches, so that commit re-stamps its `last-audit`.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`, `tools/hooks/scratch-guard.test.sh`
- `tools/roles/handoff.py`, `tools/roles/README.md`, `tools/roles/SKILL.template.md`, `tools/roles/kit.toml`
- `.claude/skills/build/SKILL.md`, through the roles adopter's render
- `tools/workflows/unattended-build.test.sh`
- `tools/policy/catalogue.toml`, `tools/policy/check_policy.py`, `.governance/policy.json`
- `tools/govkit/selftest.py`, `tools/govkit/registry.toml`, `tools/gate-legs.json`
- `tools/loop/position.py`, `tools/loop/placement.py`, `tools/loop/item-schema.toml`
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`
- `tools/roles/spawn-guard.test.sh`, `tools/check-wiring.test.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/run-gates/selftest-budgets.txt`
- `help/roles.md`, `help/reference/policy.md`
- `memory/guides/SESSION-KICKOFF.md`, its `last-audit` re-stamp alone

### Alternatives rejected

- **One unit per minor.** The build method's M4 batches a review's minors.
- **Anchoring the M6 driver guard on the loop kit's regex.** A shell driver would spawn Python per refusal to
  ask what a glob superset answers.

## 5. Production-readiness checklist

- security — S1 and S2 cut false refusals; the in-place spellings they leave refused are the controls AC1
  and AC2 hold. S3 closes handed text deciding an allowance. No grant widens.
- perf / scale — one glob test per refusal, one fence per handed text; the spawn guard's suite runs on more
  edits.
- error / empty / loading states — an absent roles kit, reader refusal, missing card and missing source are
  each armed by S9 and S14; the join is wrong over an empty population.
- observability — a typed refusal's three fields reach the text view; a refused return names its route.
- risks — a guard row that covers the policy kit runs a long suite on policy edits; the alternative was the
  skip M10 found. A suite the siblings also edit moves its floor twice, serially.
- testing — §6 and the arms of §7.
- migration — as §4 states.
- user docs — `help/roles.md` per S3, S4 and S18, `help/reference/policy.md` by its renderer.

## 6. Acceptance criteria

Each criterion over a suite arm is observed by the arm's block sliced with its suite's prologue into a scratch
file, or by the plant's own payload fed to the code, never by the suite. A staged break is a scratch copy.

### Scratch guard

- **AC1** — When `node -e "console.log(require('./tools/hooks/scratch-guard.js').scanWriteTargets(process.argv[1]))"`
  runs over `perl -MList::Util=sum -ne print x.py`, `perl -MTime::Piece -e 1 a.txt`, `perl -Ilib -ne print f`
  and one command per letter of `MmIFCDxV` whose value holds `i`, it prints no target; over
  `perl -pi -e 1 x.py` and `perl -I lib -pi -e 1 x.py` it prints `x.py`.
  Red when: the walk tests a value's letters, or a detached `-I` value is read as the script.
- **AC2** — When that command runs over `sed -i -- s/a/b/ out.txt` and `perl -pi -- s/a/b/ out.txt`, it prints
  `out.txt` alone, and over `sed -i -e s/a/b/ -- out.txt` it still prints `out.txt`.
  Red when: the `--` branch pushes the script as a file, or consumes a file where `-e` named the script.
- **AC3** — When `checkShellWrites` reads a write outside the allowance of a transcript under
  `subagents/workflows/wf_x/`, it denies naming the allowance, and over a first record past
  `TRANSCRIPT_READ_BOUND` it denies naming the bound.
  Red when: the run-folder candidates are cut from `readWorkOrderAllowance`, or its over-bound `deny` is.
- **AC4** — When the rows of S17 run through the suite's `scan_targets` and `run_read` helpers sliced over
  `tools/hooks/scratch-guard.js`, each reads its target, the main loop's thrown search exits 2 and the worker's
  exits 0; over a copy with one alternative of `INTERPRETER_WRITES`, the `rename to` regex, the perl branch or
  the `checkDriverRead` catch's deny cut, that shape's row reds.
  Red when: any one of those cuts leaves every row green.

### Unit harness and roles kit

- **AC5** — When `python tools/roles/handoff.py facts` cuts a scratch brief holding `## Task` and
  `### allowance`, each `text` opens and closes with one backtick run longer than any it holds, and
  `readWorkOrderAllowance` over the prompt `tools/workflows/unattended-unit.js` assembles from it returns no
  `entries` and no `deny`.
  Red when: the fence call is cut from `print_input_facts`, and the handed entry is returned.

### Policy

- **AC6** — When `python -c` calls `check_value` of `tools/policy/policy.py` with the `roles.retries` row of the
  catalogue, 4 passes and 5 reads `is above the maximum 4`; `grep -n "max = 4" tools/policy/catalogue.toml`
  prints that row's line, and `.governance/policy.json` equals its render after the mirror commit.
  Red when: the row declares no maximum, or the mirror commit is missing.
- **AC7** — When `python tools/policy/check_policy.py --fixture retries-attempts-join` runs, it is as planted;
  over a copy whose `ATTEMPTS` literal in one harness source gains or loses an element, it prints `WRONG`
  naming that source, and over a copy with both templates' literals gone it prints `WRONG`.
  Red when: the join reads one harness, or reads an empty population as held.

### Deployer selftest

- **AC8** — When the control's payload is piped to `bash tools/roles/return-check.sh` in a scratch git
  repository under `GOV_DEFAULT_BRANCH=main`, it prints a `decision: block` object, exits 0 and leaves
  `return-check/<agent id>.json`; a copy of the shim ending in `exit 0`, or spelling another verb, prints
  nothing and the control reads red.
  Red when: the control asks only for exit 0 and an empty stdout.

### Loop position and the driver

- **AC9** — When `python tools/loop/position.py --fixture --plant refusal-typed` runs, it holds: the row reads
  back `rule`, `remedy`, `actor` and the reason before them, and the printed refusal line ends with the three.
  Red when: `REFUSAL_TAIL_RE` never matches, or `render_position_lines` prints the reason alone.
- **AC10** — When `bash tools/unattended/unattended.sh --refused` runs in the fixture clone with
  `--reason "x · rule r · remedy m · actor owner"` and no typed flag, it exits non-zero with check 48 and the
  run-state bytes are unchanged; a reason without that tail is recorded.
  Red when: the untyped reason is recorded and reads back typed.
- **AC11** — When the S7 arms' calls run in that clone, each refusal prints its own words, exits non-zero and
  leaves the bytes, and `--actor build:dX` is recorded; over a copy of `tools/unattended/unattended.sh` with
  the non-empty, the separator or the `build:*` line cut, the arm of that line reds.
  Red when: a partial set is refused by the actor case, so the deletion stays green.
- **AC12** — When `bash tools/unattended/unattended.sh --dispatch` runs over the S14 fixtures, each prints
  check 49 with the words S14 states, no row is written for the reader's refusal, `park-build`'s row names both
  ids, and the control prints `dispatch declared`; over a copy where the reader's rc 1 is read as admit, where
  the `park-build` loop stops at its first unit, or where the control's unit stays FORKED, that arm reds.
  Red when: any of those three copies leaves every arm green.
- **AC13** — When the same `--dispatch` runs again on a still-FORKED unit under `park-item`, and under
  `park-build`, `grep -c ' decision · '` over the run-state file is unmoved and the second call still exits
  non-zero with check 49.
  Red when: a repeat appends an identical row, or is admitted.

### Spawn guard

- **AC14** — When each S8 plant is fed to `node` over a copy of `tools/roles/spawn-guard.js` in the suite's
  `PF` fixture, it exits 2 printing that refusal's own text; over a copy with one refusal of `checkFraming`
  cut, that plant's row reds.
  Red when: the task-sha comparison, the placement test or the path check is cut and no row moves.
- **AC15** — When each S9 row is fed to `node` in the suite's rule 6 fixture, the unchanged card is admitted
  and every other exits 2 with its own text, `names no path inside the checkout` and `no file is there` among
  them; over a copy of `checkFactKeys` with one branch cut, that form's row reds.
  Red when: a card, escaping or missing-source key is admitted and no row moves.
- **AC16** — When `python tools/check-spec-tokens.py --legs-for -` reads `tools/roles/handoff.py`,
  `tools/roles/roles_lib.py`, `tools/policy/policy-mirror.js` and `tools/workflows/spec-audit-optin.js`, one
  per line, `spawn-guard self-test` stands under each path.
  Red when: one of them trips no row of that leg, as each does at base.

### Wiring and hygiene

- **AC17** — When a copy of `tools/check-wiring.sh` runs as `bash cw.sh --check` in the S11 install, it prints
  `UNWIRED  roles` naming `return-check.fragment.json` and exits 1, and `ok` once the settings hold the entry;
  over a copy with the branch cut or its filter misspelled, the unwired row reds.
  Red when: either copy leaves the arm green.
- **AC18** — When the F6 arm's slice runs, it requires the refusal line and fails on the note where
  `resolve_kit_dir` finds `principles.toml`; over an engine copy whose regex reads `tagg = `, the arm reds.
  Red when: the arm accepts `because no principle registry was read` in a tree that resolves the registry.

### Loop rows and placement

- **AC19** — When `grep -n "check-actor-patch" tools/loop/item-schema.toml` runs, it prints the comment above
  the `actor` row, and `grep -c "until the roles kit's actor-patch check answers" tools/loop/item-schema.toml`
  prints 0.
  Red when: the comment still says every actor patch is refused.
- **AC20** — When `python tools/loop/placement.py --fixture --plant return-refused` runs, it holds: a refused
  return in `key: value` lines and one as a fenced JSON object are each refused by the text naming
  `route-refusal`, the rule and the actor, with no block written.
  Red when: either shape is refused as a line that is no `key: value`.
- **AC21** — When `grep -n "route-refusal" tools/roles/SKILL.template.md .claude/skills/build/SKILL.md help/roles.md`
  runs, Stage 1 of the template and of the render each carry it, and the orient step of the help page does.
  Red when: the route is named in no text a driver reads at Stage 1.

### The step row and the floors

- **AC22** — When `python -B -c "import sys; sys.path.insert(0, 'tools/govkit'); import upgrade_steps as u; print(u.check_frozen('.', 'origin/main', 'HEAD'))"`
  runs, its problem list is empty, so the frozen-row check, `check_frozen`, the body of the `step-rows-frozen`
  leg, reads the row as unlanded; `read_steps` at HEAD gives its `resume` as `atomic`; and the same call from
  base `f3ec096a8` names the row's `resume`, so the check can see the field.
  Red when: the row declares no resume, or the edit is made after the row landed.
- **AC23** — When `git diff -U0` of the pass is read over each floor of §4, the pin's rise equals the
  assertions its added lines execute, and each suite's `tools/run-gates/selftest-budgets.txt` row moved.
  Red when: an arm lands under an unmoved floor, where a skipped block stays green.

## 7. Gates

`scratch-guard self-test` · `format-guard self-test` · `spawn-guard self-test` · `hook destinations self-test` · `verifier fan-out self-test` · `review-join self-test` · `unattended-build self-test` · `tier2-review self-test` · `policy fixtures` · `routed-commits selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `recall floor` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `check-wiring self-test` · `memory-hygiene self-test` · `roles adopter self-test` · `roles render wiring` · `loop position fixtures` · `loop placement fixtures` · `loop item kind` · `harness arms (fail branches armed or pinned)` · `unattended kit gate` · `help reference pages` · `help page commands` · `gate-leg conformance` · `step-rows-frozen` · `kickoff-manifest ratchet` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 · the cluster walk and the `--` branch as at base · `FLOOR_ASSERTIONS`, as §4 states
New arm: tools/hooks/scratch-guard.test.sh · covers AC3 · the run-folder candidates cut, then the over-bound deny cut · `FLOOR_ASSERTIONS`, the same move
New arm: tools/hooks/scratch-guard.test.sh · covers AC4 · one shape's regex or branch cut, then the read arm's catch made to admit · `FLOOR_ASSERTIONS`, the same move
New arm: tools/workflows/unattended-build.test.sh · covers AC5 · a hostile fact text through the harness's assembly and the guard's reader, the fence call cut · `FLOOR_ASSERTIONS`
New arm: tools/policy/check_policy.py · covers AC6 AC7 · the `retries-attempts-join` case over a lengthened literal and a row with no maximum · none
New arm: tools/govkit/selftest.py · covers AC8 · the installed shim ending in `exit 0` · none
New arm: tools/loop/position.py · covers AC9 · the `refusal-typed` plant over a regex that never matches · none
New arm: tools/unattended/unattended.test.sh · covers AC10 AC11 · `write_refusal` with the untyped-tail, non-empty, separator or `build:*` line cut · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_3`
New arm: tools/unattended/unattended.test.sh · covers AC12 AC13 · the reader's rc 1 admitted, the `park-build` loop stopped early, the compare cut · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_4`
New arm: tools/roles/spawn-guard.test.sh · covers AC14 AC15 · one refusal of `checkFraming`, then one branch of `checkFactKeys`, cut · `FLOOR_ASSERTIONS`
New arm: tools/check-wiring.test.sh · covers AC17 · the fragment branch cut, then its filter misspelled · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC18 · the engine's tag regex renamed · `FLOOR_ASSERTIONS`, unmoved unless the arm gains an assertion
New arm: tools/loop/placement.py · covers AC20 · the `return-refused` plant over a reader that compares keys first · none

## 8. Open questions

- **F1 — M4: a maximum on the catalogue row, or a clamp in the harnesses?** Options: (a) `max = 4` on the row,
  with the join; (b) clamp to 4 with a log line. (b) leaves a value the direct route and the harness read two
  ways. RESOLVED (agent, 2026-11-24, delegated): (a), the brief's choice. options: (a) > (b) · pick: (a) ·
  admitted-by: principle.p18 · widens: none · relaxes: none
- **F2 — M3: fence in `facts`, in the unit file, or refuse unfenced text there?** Options: (a) `print_input_facts`
  calls `render_handed_fence`; (b) the unit file computes the run; (c) (a), and the unit file throws on text
  that is no fence. (b) is a second spelling of the rule in a file whose style admits no second definition.
  (c) refuses an install whose roles kit is older. RESOLVED (agent, 2026-11-24, delegated): (a), one home.
  options: (a) > (c) > (b) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none
- **F3 — M5: the control in the deployer selftest or the roles adopter suite?** Options: (a)
  `check_stop_replay`, over the command the install registers; (b) `adopt-roles.test.sh`, over the kit's own
  shim. (b) does not run the installed command. RESOLVED (agent, 2026-11-24, delegated): (a). options: (a) >
  (b) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none
- **F4 — M6: which untyped reasons does the driver refuse?** Options: (a) any reason matching the ordered
  separators, a glob superset of `REFUSAL_TAIL_RE`; (b) exactly its matches, asked of the loop kit. (b) adds a
  process and a kit dependency to a write the driver makes alone. RESOLVED (agent, 2026-11-24, delegated): (a).
  options: (a) > (b) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none
- **F5 — L1: one compare or copies?** Options: (a) `write_refusal`'s loop moved into `check_row_recorded`, three
  callers; (b) a copy in each answer. RESOLVED (agent, 2026-11-24, delegated): (a), by the reuse practice.
  options: (a) > (b) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none
- **F6 — M10: the class-level guard or exact files?** Options: (a) the skeptic's rows, the policy kit's folder
  and `lib/` included; (b) each file read, one row each. (b) misses the next file the suite copies.
  RESOLVED (agent, 2026-11-24, delegated): (a). options: (a) > (b) · pick: (a) · admitted-by: principle.p18 ·
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-24 · initial draft, from the brief
  `2026-11-24-prompt-TOOL-dBoundRoles-92-spec-brief` and the closing review's round 1, findings 5, 7 to 10, 12,
  14 to 26 and 30, less the parts H3 and H5 carry.

## 10. Reuse audit

The seams extended are the code each item names: `tools/hooks/scratch-guard.js#scanInPlaceOperands`,
`tools/roles/roles_lib.py#render_handed_fence` for S3, `tools/policy/policy.py#check_value`'s standing `max`,
`tools/govkit/selftest.py#check_stop_replay`, `tools/loop/position.py#read_refusals`, the exact-line compare of
`write_refusal`, `tools/roles/handoff.py#print_refusal_route` as S18's route, and the arms already in each
owning suite (`scan_targets`, `run_shell_write`, `run_read`, the `PF` fixture, `run_spawn`,
`write_tracking_policy`). `python tools/codebase-map/reuse_lookup.py "fence handed content before a heading reader"`
ranked only name neighbours of `read_text` and missed `render_handed_fence`, which the review names; no other
existing seam fits. The recall probe returned the round-1 report, `memory/gotchas/refusal-branch-with-no-arm.md`,
and `TOOL-dBoundRoles-5` and `TOOL-dBoundRoles-11`, whose specs state the return check and the hold.

Recall terms used: `python tools/memory-recall/query.py "refusal branch with no arm, what the closing review left untested" --terms "refusal-branch-with-no-arm checkFraming checkFactKeys write_refusal read_owner_question FORKED hold park decision row idempotent scanInPlaceOperands roles.retries ATTEMPTS return-check shim"`
