**Serves:** research PLAY-dOrderedCharter-84

# Brief: spec PLAY-dOrderedCharter-84 — no file is owner-only to a run under its mandate

## The prompt

> What are you talking about, this whole process is unattended, how can there be files only the owner can commit.

> where did this rule come from at all? Fix it.

— owner, 2026-11-12. The ruling and what the main loop found are in
`memory/builds/dOrderedCharter/build/2026-11-12-build-PLAY-dOrderedCharter-1-owner-guard-ruling.md`; the hold that raised it is
`memory/builds/dOrderedCharter/build/2026-11-12-build-PLAY-dOrderedCharter-1-owner-landing.md`.

## The brief

### Goal

Write spec PLAY-dOrderedCharter-84, the Tier-2 spec for one unit at order 46 that lets this run land itself: the policy guard
admits a guarded change an agent commits on the run branch of a live unattended run, and the lander's `--prepare` commits what
its upgrade steps write before it regenerates.

### Items

1. **Where you write.** Write the new spec only at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold84/2026-11-12-spec-PLAY-dOrderedCharter-84.md`;
   write nothing under the repository. Follow `memory/TEMPLATE-SPEC.md`; carry the `**Derived:**` binding line spec 83 carries;
   status line `DEFERRED · rev-1 · 2026-11-12 · node a · Tier-2 · base <HEAD short sha> · streams tooling · order 46 · advances
   PLAY-dOrderedCharter-38`.
2. **The guard.** `tools/policy/guard.py --staged`, called from `.githooks/pre-commit` when a guarded path is staged and stderr
   is not a terminal. Add one admission: the commit is made on a branch that is the `run-branch:` of a run-state file
   (`memory/builds/<slug>/RUN.md`) whose phase, read at HEAD, is not terminal. Design it as TOOL-dDeclaredLoop-2's
   `agents-within-mandate` row states the mandate condition (that spec, section 4, "The verdict"), but read no policy key: the
   minimal guard stays key-free, so the admission holds in every repository whatever `policy-file.guard` says, by the owner's
   ruling. Say how a run-state file is found and its phase derived without importing the unattended kit (the guard is the policy
   kit's), what a refusal prints, and whether a decision row or change record is still demanded. Name how dDeclaredLoop-2 reads
   this unit when it builds: a Readers edge, never an edit to that build's spec.
3. **The lander.** `tools/push-main.sh --prepare` runs gov's upgrade steps (around its `upgrade steps` block) and then
   `run_regen`; the policy mirror's `policy.py mirror --write` refuses while `.governance/instructions.toml` is uncommitted, so a
   step that writes it stops every lander. Make the prepare commit the steps' output before the regeneration, or name the
   narrower seam you find; the commit lands on the run branch under item 2's admission.
4. **Docs.** `help/policy.md`'s section "Who may change the policy file" states the new admission.
5. **Arms.** The guard's fixture cases live in `tools/policy/check_policy.py`; declare each new arm on a `New arm:` line,
   including one where a run in a terminal phase, or a branch that no run-state file names, is still refused.
6. Criteria observe the guard admitting the run branch's staged guarded change and refusing the other two shapes, and the
   prepare's order. The spec-token check grades a live spec's acceptance bullets word by word: no acceptance command whose words
   include an untracked path, no `path#symbol`, no suite as the observation, each backticked span on one line, every tripped leg on
   the gates line. Every new fact pinned; every minted function passes the lexicon's `--suggest`.

### Acceptance

- Spec 84 builds as written over HEAD, and after it this run's `--prepare` commits the adopter-rules step's output and regenerates.

### Gates

None run on the repository: this is a scratch write.

### Non-goals

- No code. No edit outside the scratch copy. No `policy-file.guard` reader, no TTY policy command, no floor: those stay
  TOOL-dDeclaredLoop-2's.
