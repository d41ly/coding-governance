**Serves:** research PLAY-dOrderedCharter-83

# Brief: spec PLAY-dOrderedCharter-83 — the reconcile merge with origin/main at 47ed57fab

## The prompt

> take forks' recommendations, land it

— owner, 2026-11-10. The close's lander refused: `push-main.sh --prepare` reported that merging the run branch onto
`origin/main` at `47ed57fa` CONFLICTS, and told the run to merge `origin/main` into the branch, resolve, commit, and prepare
again (`memory/guides/UNATTENDED-STOPS.md`, "A reconcile comes from the REMOTE's default branch").

## The brief

### Goal

Write spec PLAY-dOrderedCharter-83, the Tier-2 spec for one unit at order 45 that makes the `--no-ff` merge of `47ed57fab`
into `branch/unattended-dorderedcharter-725f52`, resolving every conflict by its kind. Model it on main's precedent,
`TOOL-aSmoothedDispatch-22` (read it with `git show origin/main:memory/builds/aSmoothedDispatch/spec/2026-11-11-spec-TOOL-aSmoothedDispatch-22.md`).

### Items

1. **Where you write.** Write the new spec only at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold83/2026-11-11-spec-PLAY-dOrderedCharter-83.md`;
   write nothing under the repository. Follow `memory/TEMPLATE-SPEC.md`; carry the `**Derived:**` binding line spec 82
   carries; status line `DEFERRED · rev-1 · 2026-11-11 · node a · Tier-2 · base <HEAD short sha> · streams playbook · order 45
   · advances PLAY-dOrderedCharter-38`.
2. **The conflict set.** Take it with `git merge-tree --write-tree --name-only HEAD 47ed57fab` (merge base `8bec4cefd`): fifty
   files, every one a content conflict, most one region. State the command and the tree it prints, and tell the builder to
   re-take it at the merge and record any difference.
3. **Dispositions by kind.** Read each region on both sides and the commits that moved it; give each file one disposition:
   - **Kit version markers** (`<!-- gov:kit <kit>@<v> -->` beside this build's level envelope line, in the unattended,
     memory-tree, roles and workflows templates): keep this branch's envelope line and main's higher version. The lander's
     mint re-bumps after landing; say whether any kit this branch touched owes a bump past main's.
   - **Rendered or generated outputs** (`AGENTS.md`, `.claude/agents/*.md`, `.claude/skills/*/SKILL.md`, `memory/guides/*.md`,
     `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `help/roles.md` if generated, `memory/backlog/PLAY.md`,
     `memory/map/generated/*`, `.governance/policy.json`'s `catalogue_blob`): re-rendered by their own generators after the
     sources are resolved, never hand-merged. Name each generator and the order they run in. Check whether `AGENTS.md` and
     `.governance/policy.json` are owner-only for an agent's commit under the policy guard, and what the builder does if so.
   - **Product sources with real two-sided edits** — `coding-governance-agents.template.md` (main's v4.5 marker and its
     retired memory-tree lookup line, against this branch's restructured charter), `tools/check-playbook-parity.sh` (main
     moved the lens bound to `check-verifier-fanout.js`, this branch moved the verify-total source to `practices.toml`),
     `tools/check-spec-tokens.py` (main's `--spec` mode against this branch's `check_live_header`), `tools/roles/handoff.py`,
     `tools/roles/render_agents.py` (two regions: docstring and main's arm 19 beside this branch's shape and ranked arms),
     `tools/workflows/tier2-review.js` and its template (two regions each), `tools/workflows/REVIEW-PROTOCOL.template.md` (two),
     `tools/workflows/kit.toml` (this branch's drive rows beside main's `lf_pin`), `.lexicon.conf` (the verb pin, re-measured
     over the merged tree): keep both sides' intent, and say for each what the merged lines are.
   - **Suite floors** (`tools/check-spec-tokens.test.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`,
     `tools/lib/resolve-python.test.sh`): keep both sides' arms and RAISED lines, add one MERGED line naming this unit, the
     floor recounted by reading.
   - **Records** (`memory/builds/dIndexedDesign/README.md`, `memory/builds/dShippedRelease/README.md` and its spec 78, the two
     `memory/gotchas/*.md`): additive, per `[reconcile]`; a generated region is re-rendered.
4. **After the merge.** The kickoff manifest re-stamp if a watched file moved; the build index, LIVE, the ledger and the
   codebase map re-rendered; the spec-token check over the merged tree. Main's commits may have added legs or checks that
   now grade this branch's files: name the ones the merge must leave green, and which legs the main loop runs afterwards.
5. Criteria observe: no conflict marker in the merged tree, two parents, each product file's merged lines present, the
   generators writing nothing on a second run. The spec-token check grades a live spec's acceptance bullets word by word: no
   acceptance command whose words include an untracked path, no `path#symbol`, no suite as the observation, each backticked
   span on one line, every tripped leg on the gates line. Every new fact pinned.

### Acceptance

- Spec 83 builds as written over HEAD, every conflicted file has a disposition, and no fork is left open.

### Gates

None run on the repository: this is a scratch write.

### Non-goals

- No code, no merge. No edit outside the scratch copy. No change past what the reconcile needs.
