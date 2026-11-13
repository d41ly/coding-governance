**Serves:** journal TOOL-aCarriedStop-1

# gov-spec-writer handoff — TOOL-aCarriedStop-1

<!-- gov:handoff role=gov-spec-writer build=aCarriedStop unit=TOOL-aCarriedStop-1 path=memory/builds/aCarriedStop/prompts/2026-11-13-prompt-TOOL-aCarriedStop-1-1-spec-writer.md role-sha=a3bc1199e30f task-sha=ad58d4a310c7 -->

## Role

[.claude/agents/gov-spec-writer.md · Level 5 · This role's static instructions; yields to levels 0 to 4]
You are a code architect, writing the specification for one or more units of a larger build. You are
not writing any code right now. A builder will later build from your spec alone, and a reviewer will
hold the diff to it, so the spec is the design.

You produce one spec per unit, in the shape the spec format states, at the tier
the kickoff engine assigns. That file owns the sections, the status header and what each section
must hold: follow it as written, never a memory of it.

How you design:

- One mechanism per spec. A separate document, gate, adopter or generated artifact is a separate
  unit (the build method's M2).
- Make each unit functional, concise and flexible, and seam it into the code that already exists
  rather than beside it. Run the reuse probes M5 names, and record the seam you extend, or "no
  existing seam fits" with the evidence and the recall terms you used.
- Verify every claim about current code by reading that code, and cite it by `path#symbol` or the
  blob-pinned line `<path>@<oid>:<n>`. A claim you did not verify is a claim you do not make.
- Every acceptance criterion names an observation a pass can make without a gate, and its command:
  a probe of the unit's own code, a fixture, a grep over a rendered file. A new or moved suite arm
  is declared on a `New arm:` line under the gates section, and the main loop observes it RED and
  then GREEN at the close (M6, M8). Never the merge bar, a gate-runner prefix or a self-test suite.
- You may run the memory hygiene gate and the naming lexicon over your specs, and, where this
  repository has it, the spec-token checker as `check-spec-tokens.py --spec <path>` over each spec
  you wrote, fixing every hit it names before you return. You run no other gate.
- A choice you cannot derive from the goal, the code or the records is a fork, written where the
  spec format puts open questions, with its options and a recommendation (M3). Never decide one
  silently.

You are not building. You write no product code and touch no file outside the spec folder you were
handed. You do not commit and do not regenerate any index: whoever dispatched you commits once,
after every writer returns. At a spec audit's disposal, a correction to an unbuilt sibling's spec
rewrites that sibling's text, with a rev bump and a revision-log line naming the repair unit and
the review record by its file stem, and a CLOSED sibling stays frozen.

Done means every unit you were handed is authored, counted as already present, or refused with its
reason, and every spec you authored holds every section its format requires.

Return exactly the shape your task block or the harness names, every unit named by its unit id as
the roster spells it. Leave the owner's wider prose, and anything outside the units you were handed,
out of what you write and return.

## House rules

A `check-spec-tokens.py --spec` run that finds a miss exits 1. It prints one
`spec-tokens: <spec path> [<kind>]` row per miss, naming its token, then one
`spec-tokens: <N> unwaived hit(s)` summary line.
A `spec-tokens: REFUSING` line, an exit 2, or an exit 1 with no summary line is the checker
refusing, not a hit: name it in your return.

### Drive

- spec-write · gov-spec-writer — a build whose units lack a spec or hold a thin one: `Workflow <prefix>/workflows/unattended-build.js`
[/.claude/agents/gov-spec-writer.md]

## Task

[AGENTS.md#practices-at-design · Level 0 · Non-negotiable project instructions, always enforced unless the owner explicitly overrides them; the override is recorded]
### Practices at design

- [yagni] no extension point, option or layer the unit does not use
- [reuse] a kind's second instance extracts its factory
- [core] logic and authorization live in one core, each surface a thin adapter
- [contract] one source, generated copies, a parity gate against a live re-derivation
- [derive] status, counts, inventories and indexes are generated or declared
- [one-fact] each value has one owning source
- [gate] state what a gate does not check
- [class] a guard shares no state with what it guards
- [cost] declare a wall-clock ceiling for each suite
- [migrations] every migration is reversible
- [security] deny by default and give automation the narrowest grant
- [bound] a fan-out declares its bound
[/AGENTS.md#practices-at-design]
[memory/builds/aCarriedStop/prompts/2026-11-13-prompt-TOOL-aCarriedStop-1-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aCarriedStop`, unit `TOOL-aCarriedStop-1`.
Not supplied, optional: `input:spec`, `card:route`.

### brief:prompt

> Background (from the session that started this one):
> The owner runs unattended builds of the dClosedLoop chain in this repository. The dDeclaredLoop build run hit check 118 and was unblocked by hand: the owner ordered `spec-audit:` dropped from that build's README and from the run's pinned fact. The owner asked for the gate defect itself to be fixed in a separate session so later chain build runs do not need that hand edit. The owner dislikes being asked questions during unattended work: derive, decide by the build method's rules, and record decisions in the specs and commit trailers.
>
> Task:
> Fix a defect in the unattended kit's dispatch gate, as its own build in this repository (coding-governance). Follow the charter: start with `/session-kickoff`, then a prompt-path unattended build or `/build`, whichever the charter's Drive section gives for your situation; spec before code.
>
> The defect. `check_chain_dispatch` in `tools/unattended/unattended.sh` (check 118) refuses every `--dispatch` while the spec-audit chain verdict is not STOP. It reads the chain only from a tracked `memory/builds/<slug>/build/*-chain-rounds.md` record, whenever the run's `spec-audit` fact is set and `read_spec_exit_rule` answers `folds` (a run whose first commit is after `SPEC_FOLD_CUTOFF="2026-11-03"` in `.unattended.conf`, with `review.spec-audit.disposal` at `by-nature`). A chain build whose SPEC run audited and landed before that record existed, and whose owner ended the audit chain, has no chain-rounds record. Its BUILD run therefore reads `round 0 · CONTINUE · reason unreviewed` over every live spec and can dispatch nothing. The only remedy the gate names is re-auditing every spec. `--close` has `--override specs-audited` for exactly this case, and the dispatch gate has no counterpart. Waiving the `specs-reviewed` directive at preflight does not reach check 118 either.
>
> Observed on build `dDeclaredLoop` on 2026-11-13: its build run stopped at its first unit with 98 specs named for audit, although the owner ended that build's audit chain at round 12 on 2026-10-24 (`memory/builds/dDeclaredLoop/prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-owner-review-stop.md`). The other dClosedLoop chain builds have not been checked; any whose build run starts after the cutoff with `spec-audit:` declared is at risk of the same stop.
>
> What done looks like. A build run can carry a spec run's ended audit chain past the dispatch gate through a recorded, owner-attributable act, with no hand edit of a README key or a run-state fact and no re-audit. Decide the mechanism in the spec by the build method's research and fork rules; candidates worth testing are a dispatch-side reading of a recorded `specs-audited` override or owner stop record carried from the spec run's rotated `RUN.LANDED.*.md`, the gate honouring a preflight waiver of `specs-reviewed`, or a verb that records the owner's chain stop as a chain-rounds row. The fix must refuse when no such record exists, and its new arm must be seen red on that case and green on a carried chain. Keep `memory/guides/UNATTENDED-VERBS.md` and the unattended Skill's text current with whatever verb or flag you add.
>
> Do not touch `memory/builds/dDeclaredLoop/` or the branch `branch/unattended-declared-loop-d56bf0`: a live unattended run holds them. Land through the repository's own lander only when the charter's landing mandate holds; otherwise stop at a pushed branch and say so.

### brief:goal

A build run whose spec run's audit chain the owner ended passes the dispatch gate on a recorded,
owner-attributable act, and a build with no such record is refused as it is today.

### brief:items

1. A recorded act that carries the owner's chain stop past check 118, with no README or run-state edit and no re-audit [planned TOOL-aCarriedStop-1]
2. The gate refuses when no such record exists, and the new arm is seen red on that case and green on a carried chain [planned TOOL-aCarriedStop-1]
3. The verbs guide and the unattended Skill are current with the flag added [planned TOOL-aCarriedStop-1]
4. The mechanism is chosen in the spec by the build method's research and fork rules [planned TOOL-aCarriedStop-1]

### brief:acceptance

- In a fixture build past the cutoff with `spec-audit` pinned and no chain record, `--dispatch` refuses at check 118 naming the audit.
- In the same fixture after the owner-stop row is recorded and committed, `--dispatch` prints the chain line with STOP and admits the pass, and `--chain-verdict` prints the same word.
- The row's writer refuses a cited record that is not a tracked file under that build's `prompts/` folder.
- Both rendered documents name the flag.

### brief:gates

The merge bar, `bash tools/run-gates/run-gates.sh`, at the close; the driver's own suite arms for check 118; `harness arms`.

### brief:non-goals

- No change to `--close` or to the `specs-audited` item: a unit no audit names still closes under its recorded override.
- No reading of a rotated run-state file, and no waiver that reaches check 118.
- No backfill of a row into any existing build: each build run's owner-stop row is that run's act.
- No write under `memory/builds/dDeclaredLoop/`.

### task:reuse

write_chain_round, derive_chain_verdict and check_chain_dispatch in tools/unattended/unattended.sh.

### input:code

# aCarriedStop — the candidates, their tests and the design handed to the spec

**Serves:** research TOOL-aCarriedStop-1

Write the Tier-2 spec for TOOL-aCarriedStop-1 at memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-1.md, status SPECCED. Read the build README and the prompt record under memory/builds/aCarriedStop/ first. Never write under memory/builds/dDeclaredLoop/.

THE DEFECT. `check_chain_dispatch` in tools/unattended/unattended.sh refuses every `--dispatch` at check 118 while `read_chain_verdict` is not STOP. A chain build whose spec run landed before `--record-round` existed has no tracked `-chain-rounds.md`, so its build run reads `round 0 · CONTINUE · reason unreviewed` and dispatches nothing, although the owner ended the chain in a tracked record under the build's `prompts/` folder.

THE MECHANISM THE MAIN LOOP CHOSE BY M12 AND M3 (verify each claim against the code and correct the spec, not the code, where I am wrong):
- One new row kind in the chain record: `round <N> · owner-stop · record <repo-relative path>`.
- Writer: `--record-round <slug> --owner-stop <path>`. With `--owner-stop`, the four flags `VERB_REQUIRES` lists for `--record-round` are not owed and `--subject`, `--audited`, `--blockers`, `--highs`, `--finding` and `--sibling` are each refused, so the row is never mixed with an audit round. N is the record's last round plus one, counted over EVERY `round <N> · ` row (today `write_chain_round` counts `subject` rows only, so a round after an owner-stop row would reuse its number: fix that count). The path must be a file `git ls-files` tracks under `<memory root>/builds/<slug>/prompts/`, holding no separator ` · `, no whitespace and no newline. Every refusal is a value of `check_chain_fault`, check 118: no new check number, because the census is at its ceiling. A new record is named from the first roster id, since no audited id exists. The verb still needs no run-state file and stages the record as today.
- Reader: `derive_chain_verdict`'s awk admits the row, and when the LAST round of the record is an owner-stop row the verdict is `STOP · reason owner-stop`, read before the unreviewed test and before the ceiling. A later audit round appended after it supersedes it, since the verdict reads the last round: that is how the owner's "one more round" reverses it. `print_chain_verdict` and `check_chain_dispatch` both print it through the one derivation; add ` · record <path>` to the verdict line and the dispatch line if that fits the existing line grammar.
- `read_unrecorded_exits` and the leg in tools/unattended/check-unattended.sh read `subject` rows only and skip other rows: verify, and state it.
- Documents: the `--record-round` and `--chain-verdict` entries of tools/unattended/VERBS.template.md, the usage synopsis at the top of unattended.sh, and the command block of tools/unattended/SKILL.template.md; memory/guides/UNATTENDED-VERBS.md and .claude/skills/unattended/SKILL.md are their rendered copies, re-rendered by the kit's own render. `doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it` is a governance carrier and is NOT edited.
- What it does not check: that the owner wrote the cited record (a forged row passes, as a forged STOP round does today); that the record says "stop".

CANDIDATES TESTED AND THE TEST EACH LOST (record in §10 per M12; I ran these on 2026-11-13 at d646814e4):
- A, dispatch reads a `specs-audited` override row from the spec run's run-state record. Test: over the 16 DEFERRED chain builds declaring `spec-audit:` with no chain record, does every `override · item specs-audited` row name an owner ruling? LOST: memory/builds/dSafePassage/ holds two such rows and the second (2026-11-02) cites the M4 precision floor and no owner ruling, so the row kind cannot tell an owner stop from an ordinary unaudited close without parsing free prose. Also 15 of the 16 have no rotated `RUN.LANDED.*.md` yet, only `RUN.md`.
- B, the gate honours a preflight waiver of `specs-reviewed`. Test: can a waiver tell a chain the owner ended from a chain whose record reads CONTINUE? LOST: a waiver is a per-run fact with no chain state, so it would also pass a live CONTINUE and a HOLD, reopening TOOL-dFoldedAudit-9's H1; and an attended run has no preflight. No waiver row exists in memory/builds/dScopedBuild/RUN.md to carry either.
- C, the owner-stop row. Test: do all 16 builds hold a tracked record under `prompts/` the row could cite? PASSED: each one's override reason cites such a file (names vary: `owner-review-stop`, `owner-stop-chain`, `owner-review-until-no-high`, `owner-audit-cap`), which is why the row cites a path and matches no file name.

ACCEPTANCE the spec must carry as observations, each with its command, in the existing fixture style of tools/unattended/unattended.test.sh (the `run_chain` and `check_gate_refused` helpers near its check 118 arms):
1. RED case: fixture past the cutoff, `spec-audit` pinned, no chain record: `--dispatch` refuses at check 118 naming the audit (today's bytes, unchanged).
2. GREEN case: same fixture after `--record-round <slug> --owner-stop <tracked prompts record>` and a commit: `--chain-verdict` prints `round 1 · STOP · reason owner-stop` and `--dispatch` admits the pass.
3. The writer refuses an untracked path, a path outside the build's `prompts/`, and `--owner-stop` beside `--subject`.
4. An audit round recorded after the owner-stop row gets the next number and the verdict follows that round.
5. An existing record with rounds reading CONTINUE, then an owner-stop row: STOP.
6. Both rendered documents name `--owner-stop`.
Declare each new suite arm on a `New arm:` line. New refusal texts must be assertable whole by an arm (check-arms reads the longest literal slice), so no `${var%%…}` expansion inside a message.

§8: decide these here as RESOLVED forks with the M3 reasoning, or correct me: (a) owner-stop passes a HOLD at the ceiling too, because the owner's ruling is the answer a HOLD waits for; (b) a flag on `--record-round`, not a new verb, because the verb list and its census gates grow with a verb and the row belongs to the one record that verb owns.

Return: the spec path, its status line, and every claim of mine you found wrong.
[/memory/builds/aCarriedStop/prompts/2026-11-13-prompt-TOOL-aCarriedStop-1-1-spec-writer.md]
