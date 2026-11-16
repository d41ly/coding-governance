# Brief — aCarriedStop: the owner's ended audit chain, carried past the dispatch gate

**Serves:** research TOOL-aCarriedStop-1

The prompt arrived as prose from the session that started this one, on the owner's instruction, and is quoted whole.

## The prompt

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

## The brief

### Goal
A build run whose spec run's audit chain the owner ended passes the dispatch gate on a recorded,
owner-attributable act, and a build with no such record is refused as it is today.

### Items
1. A recorded act that carries the owner's chain stop past check 118, with no README or run-state edit and no re-audit [planned TOOL-aCarriedStop-1]
2. The gate refuses when no such record exists, and the new arm is seen red on that case and green on a carried chain [planned TOOL-aCarriedStop-1]
3. The verbs guide and the unattended Skill are current with the flag added [planned TOOL-aCarriedStop-1]
4. The mechanism is chosen in the spec by the build method's research and fork rules [planned TOOL-aCarriedStop-1]

### Acceptance
- In a fixture build past the cutoff with `spec-audit` pinned and no chain record, `--dispatch` refuses at check 118 naming the audit.
- In the same fixture after the owner-stop row is recorded and committed, `--dispatch` prints the chain line with STOP and admits the pass, and `--chain-verdict` prints the same word.
- The row's writer refuses a cited record that is not a tracked file under that build's `prompts/` folder.
- Both rendered documents name the flag.

### Gates
The merge bar, `bash tools/run-gates/run-gates.sh`, at the close; the driver's own suite arms for check 118; `harness arms`.

### Non-goals
- No change to `--close` or to the `specs-audited` item: a unit no audit names still closes under its recorded override.
- No reading of a rotated run-state file, and no waiver that reaches check 118.
- No backfill of a row into any existing build: each build run's owner-stop row is that run's act.
- No write under `memory/builds/dDeclaredLoop/`.

### Limitations
- The driver's check census sits at its ceiling, so every new refusal is a value of check 118's one site.
- The verdict stays one derivation with two readers.
- The row proves that a tracked record is cited, never that the owner wrote it.

### Reuse
- `write_chain_round`, `derive_chain_verdict` and `check_chain_dispatch` in `tools/unattended/unattended.sh` are the seam: the row joins the record those three already write and read.
- The reuse probe ranked name stems only and named no closer seam.
- Recall returned TOOL-dFoldedAudit-5 and TOOL-dFoldedAudit-9, which built the record and the gate, and the owner-stop records of dScopedBuild and dDeclaredLoop.
- Recall terms used: chain-verdict record-round dispatch chain-rounds specs-audited override owner stop spec-audit folds ceiling HOLD

## Drawn from the session

none

## Owner confirmation

not asked — the brief draws on nothing outside the prompt
