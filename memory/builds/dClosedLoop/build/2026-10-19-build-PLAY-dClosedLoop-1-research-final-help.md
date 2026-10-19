# Research: Human-readable help: today's docs, the plan as designed, and when its gate lands

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 158's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-31-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-final-questions.md`.

---

**Q4, human-readable help: research return**

Measured at `930120e45`. I wrote nothing in the repository. I ran probes only in my own scratch folder (`…/scratchpad/d158/`) and deleted it afterwards; `git status` shows the same five untracked prompt files as at the start. I ran no gate leg; the one leg-shaped measurement I reproduced on my own.

**Short answer:** the design plans the right end state but switches it on last. `help/` pages rendered from each user-facing unit's `usage` field, with render parity and a docs leg, all land in dConvergedCharter, build 21 of 21. Builds 1 to 20 ship every user-facing surface while only the prose `[docs]` rule applies, and that rule has demonstrably not kept pages current. The recommendation is to keep the end state and move the gate to the second chain build.

## 1. Today

**What exists:**

| Home | Measured | Currency enforcement |
|---|---|---|
| `help/` | 2 pages: `help/README.md` (5 lines) and `help/roles.md` (135 lines), created `bb0159546` on 2026-10-13 | Only the prose rule: `AGENTS.md:38` and `coding-governance-agents.template.md:37` (`[docs]`), with `HELP_DIR` defaulting to `help/` at `tools/govkit/entries/playbook.kit.toml:252-255`. No code reads `help/` (a grep over `tools`, `skills` and `.claude` finds only that placeholder), and no leg in `tools/gate-legs.json` names it. |
| `README.md` | 121 lines | None; it has no link to `help/` (0 hits). |
| Kit READMEs | 17 kits, 6,767 lines. `tools/govkit/` and `tools/lib/` have no README. | Fact-pair checks only: README markers equal code constants (`tools/check-kit-versions.sh:225-393`, `tools/check-playbook-parity.sh:266-269`, `tools/drift-audit/drift_signals.py:216`). |
| `WIRE-INTO-PROJECT.md` | 2,177 lines, an agent runbook | Runbook parity (`tools/govkit/check_runbook_parity.py`, leg at `gate-legs.json:1577`) holds an equality pin, `PROBLEM_PIN = 18` (`:60`). My recount: 29 registry entries, 11 anchored, 18 unanchored. The pin landed `cf435ccee` on 2026-09-20 and has never moved: new entries get sections, the old 18 never drained. |
| `memory/guides/` + `TEMPLATE-SPEC.md` + `HYGIENE.md` | 12 files, 406,322 bytes; agent-facing | Kit/dogfood parity covers the two templates (`gate-legs.json:421`), not the guides. |
| `--help` | Of 152 non-test entrypoints, 32 mention help handling or argparse. `run-gates.sh`, `push-main.sh`, `gen_build_index.py` and `check-spec-tokens.py` have none; their usage is a header comment. | None |
| Role carriage | `[docs]` is carried only by `tools/roles/agents/gov-spec-writer.agent.md:9`. The builder, spec reviewer and diff reviewer lines (each `:9`) omit it. `TEMPLATE-SPEC.md` and `BUILD-METHOD.md` never mention `help/` or `[docs]`. | n/a |
| Rationale | `memory/DECISIONS.md` (229 lines) has no entry on `help/` or `[docs]`. | n/a |

**The prose rule does not hold** (measured over git history since the rule landed in `c8ed3dd38`, 2026-10-09):
- 216 non-merge commits touched `tools/` or `skills/`; 6 of them touched `help/`.
- 21 non-merge commits bumped a kit's `kit.toml`; none touched `help/`.
- Examples of new user-facing surfaces with no page:
  - the `/cleanup` Skill (`13cc354ff`);
  - the format-guard Stop hook (`0a2162b94`);
  - the write gate wired into a default install (`5a2f6aefb`).
- `tools/process-monitor/README.md` never contains the word "hook" (0 hits), yet `procmon-hook.js` is wired at `.claude/settings.json:60` and `:80`.
- The gotcha `rule-stated-with-no-check-that-fails` (10 hits) is the class this belongs to; the shape audit names the docs rule an instance of it (`shape-reviews-compared [help-docs]`, line 269).

**Surfaces with no `help/` page** (a presence probe, so a lower bound on what is missing, never proof of coverage):

| Surface | Count | With a `help/` page |
|---|---|---|
| Skills | 7 under `.claude/skills/` plus `/session-kickoff` | 1: `/build`, in `roles.md` |
| Wired hooks | 13 entries across 10 scripts | 0 named. `procmon-hook.js` is named in no README; `stall-recorder.js` only in the unattended README. |
| Gate legs | 140 | 4 legs' scripts are named in `help/`. 22 leg names and 103 leg scripts appear in any human doc. |
| Kits | 17 | 1 (`roles`) |
| Commands | `run-gates.sh`, `push-main.sh`, `govkit.py`, `handoff.py` | `handoff.py` only |
| Conf files | 5 `.conf` files plus `.governance/deploy.toml` | 0 |

The docs are also islands: across `help/`, `README.md`, the 17 kit READMEs and `WIRE-INTO-PROJECT.md` there are 2 relative markdown links in total. Paths are cited in backticks, not linked.

## 2. The plan as designed, and when each part lands

- **Rendered pages and the docs leg (dConvergedCharter, #21).** v2 `[chain]` clause 15 (`architecture-v2.md:1604`): pages rendered from a `usage` field on each user-facing unit; the `help` field keeps rationale out of every page; a hand edit to a page is red at render parity; a docs leg reds a landing that changes a member of the step gate's population without changing its unit's `usage`.
  - The owner chose "Rendered from units" (`shape-reviews-compared [SA-5]`), and `[open]` (`v2:1686`) still lists the name `usage` for confirmation.
  - Also recorded at `fates:198`, `memory-plan:121`, and gap `gap-found-27`, which `v2:1604` gives to dConvergedCharter.
- **Rationale (dConvergedCharter, #21).** Clause 7: the hand-written guides retire, and their rationale moves into the units' `help` fields, "never into `help/`'s feature pages". `systems:383-394` defines `help` as rationale that "never loads", and SA-5 says it "never renders into a page".
- **Runbook and release notes (dShippedRelease, #18).** Clause 7 is "a derived runbook" (v1 called it "a runbook derived from descriptors"); clause 2 is "kit release notes". Neither clause names a losing test. `fates:180` says the govkit runbook "becomes derived".
- **Charter and Skills (dOrderedCharter, #3 and dConvergedCharter, #21).** The charter front door states "what gov is and how it works and is used", plus a drive section built from kit descriptors (`v2 [front-door]:934-960`, dOrderedCharter clause 6). Level 4 holds kit runbooks and Skills as thin entries generated from drive rows (`v2:960`), converged by dConvergedCharter clause 9. All of this is agent-facing, inside a 32 KiB charter.
- **Upstream of the docs leg (dSafePassage, #2).** The step gate (clause 10) diffs the adopter-visible population from base to tip: files, installable paths, hooks, commands, agents, conf keys, policy keys, CLI verbs and registry entries. Each later class joins when its owning build lands it. It deliberately ignores "a content-only edit".

**Timing.** All 256 catalogue rows I parsed are owned by builds 1 to 20, and none by #21 (the instruments' `[final]` count is 261 keys). Ahead of the docs leg, the following ship ungated:
- `gov tag` (#3), `gov map` (#10), `gov map code` and `gov code show` (#11);
- attend and unattend, and 39 keys (#13);
- presets (#7), the leg factory (#14), the record-kind registry (#10);
- 20 hook mentions on dWellOiledMachine's row alone.

In short, every chain build except dConvergedCharter ships user-facing surfaces before any docs gate exists.

## 3. What an owner needs, against the plan

Diátaxis sorts docs by two questions, action or cognition and acquisition or application, into tutorials, how-to guides, reference and explanation (https://diataxis.fr/compass/, read 2026-10-19). Docs-as-code means version control, review, automated tests, and teams that "can block merging of new features if they don't include documentation" (https://www.writethedocs.org/guide/docs-as-code/, read 2026-10-19). Doc tests run documented examples "to check that a module's docstrings are up-to-date" (https://docs.python.org/3/library/doctest.html) and to make sure "examples within your documentation are up to date and working" (https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html), both read 2026-10-19. Generated reference: sphinx-argparse "automatically generates documentation for command-line tools from their Python argparse definitions" (https://sphinx-argparse.readthedocs.io/en/latest/, read 2026-10-19). Offline link checking: lychee `--offline` (https://github.com/lycheeverse/lychee, read 2026-10-19).

| Need (quadrant) | What the design gives | Human page planned? |
|---|---|---|
| Concepts: the loop, stages, roles, records, policies, presets, leases, nodes (explanation) | Charter front door (agent-loaded); `help` fields (#21) | No. Rationale never renders. |
| Adopt gov (tutorial) | Derived runbook (#18, untested) | No tutorial |
| Choose a preset; attend or leave; read why a build stopped; answer an owner item; recover (how-to) | `preset` (#7), attend/unattend (#13), `next`'s closed answer set and its failure route (#5, clauses 7 and 14), `run.on-owner-silence` (#13) | Only as `usage` at #21 |
| Every command, key, preset, leg, kind, hook, extension point (reference) | Registries: schema (#1), drive table (#3), kinds (#3, #10), legs (#14) | Only via `usage` at #21. Today's registries carry no human sentence (section 4). |

## 4. Gaps

1. **Timing.** The docs leg lands last (section 2). Losing test: count owner-facing surfaces landed before the leg. Result: 256 of 256 catalogue rows.
2. **Explanation renders nowhere.** The guides (406 KB) retire into agent slices and their rationale goes into `help` fields that "never render". After #21 an owner cannot read why anything is as it is without opening registry source. Instruction review B's L3 fix ("a check that no guide is deleted while a section maps to no view") was never folded into clause 7.
3. **`usage` has no home for most of the leg's population.** `help` and `usage` live on instruction units (`systems:383`), but the leg's population is the step gate's: policy keys, hook entries, receipt files, legs. Most of those are not instruction units, so they have nowhere to carry `usage`. Separately, dOrderedCharter's field list (clause 9, `v2:1586`) names neither field, so a spec writer working from the chain row would not add them.
4. **No fate rows** for the 17 kit READMEs, root `README.md` or `WIRE-INTO-PROJECT.md`. Only `help/` (`fates:198`) and govkit's runbook parity (`fates:180`) have one. Convergence's `git ls-files` exit check would first find them at #21.
5. **The registries cannot generate reference text today:**
   - `gate-legs.json`: 0 of 140 legs carry a description field (21 names have a parenthetical gloss);
   - hook fragments: 0 of 9 carry a purpose (fields are name, event, matcher, marker, hook_path);
   - kit descriptors: 0 of 29 carry a summary;
   - the v2 catalogue's Source column is provenance, not explanation.
6. **No principle.** None of P1 to P40 covers human documentation, and the docs rule reaches one role of ten.
7. **Untested clauses.** dShippedRelease's derived runbook and release notes have no losing test. Runbook parity's 18 missing sections have no owner to drain them.
8. **Record disagreements:**
   - `v2:210`, a revision note, says the guides' rationale moves "to `help/`"; `v2:1604` clause 7 says "never into `help/`'s feature pages". `layer-instruction:507` agrees with the note; `systems:393-394` supersedes both.
   - Every row in the gap register's Owner column reads `—` (378 of 378). That is by design (`gap-register:8`); ownership lives in `[chain]`.

## 5. Candidates (they differ in mechanism)

| # | Mechanism | Losing test, written before running | Result |
|---|---|---|---|
| C1 | Prose `[docs]` rule plus hand-written pages (today's mechanism until #21) | Do pages move with user-facing commits? | **Rejected.** 0 of 21 kit bumps and 6 of 216 product commits touched `help/`; the process-monitor README omits its own hook; the 18-section pin has not drained. |
| C2 | As designed: rendered from `usage`, render parity, docs leg, all at #21 | Count surfaces landed before the leg | **Rejected as to timing** (256 of 256 rows ungated). Kept as the end state. |
| C3 | Co-change rule: a commit touching an entrypoint must touch some `help/` page | Synthetic changesets | **Rejected.** A renamed flag plus a whitespace-only page edit passes green; an internal refactor reds. |
| C4 | Membership docs leg on the step gate's population, each member mapped to a page anchor (reusing govkit's `<!-- govkit:entry -->` anchors and shrink-only pin, run over the whole population rather than the diff) | A content change that leaves membership unchanged (a renamed flag, a changed default) | **Rejected on its own.** The step gate excludes content-only edits by design (dSafePassage clause 10), so the leg stays green. Kept as the presence half of C5. |
| **C5** | **Fingerprinted docs leg.** Each member declares its usage as a row (verb and flags, key with allowed values and default, hook event and matcher, leg name and argv). A page is rendered from that row or names it; the leg reds when the fingerprint moves and the page or `usage` does not. Page commands are doc-tested against the declared row; an offline link check runs alongside. | A planted stale page must go red, and the real page must stay green | **Survives.** Prototype over `help/roles.md`: 9 `handoff.py` examples, 0 red; with `--part` planted as `--section`, exit 1. Link check: real docs 2 links, 0 broken; a planted `role.md` is red. My first prototype false-reddened 4 real examples because parsing source missed argparse's mutually exclusive groups. The fingerprint must therefore come from a declared row, never from reverse-parsing code. |
| **C6** | **Generated reference** from registries (policy schema, presets, drive table, legs, hook fragments, kind registry, role definitions), each row gaining required `summary` and `usage` fields, through one render-parity factory | Does a generated page say anything without those fields? | **Survives only with the fields.** Today's rows yield names and argv only (gap 5). |
| **C7** | **Rendered explanation:** units' `help` fields rendered into a separate tree, `HELP_DIR/why/`. It sits outside every load set, because no code loads `help/`, and stays apart from feature pages, which answers review finding L10 (`systems-retrofit:433-437`). Paired with a no-lost-rationale arm. | At build: plant a guide deletion whose section maps to no unit's `help` field; it must go red | Not runnable today (no units). It is the test the build must run. |

## 6. Proposal

**Recommendation: C5 + C6 + C7, with C2 kept as the end state.**

**Generated vs authored, under `[one-fact]`:**
- Generated: reference pages for commands, policy keys, presets, legs, hooks, record kinds, roles and extension points.
- Authored: concept pages for the loop, stages and leases; one tutorial; and how-to pages for the six owner tasks, each with doc-tested commands.
- The adopt tutorial runs in an adopter fixture, reusing the existing adopter end-to-end legs such as `run-gates adopter e2e`.

**Per-build placement:**

| Build | Carries |
|---|---|
| dGroundRules (#1) | The policy schema gains `summary` and `usage` per key, and the keys' reference page is generated from it. The four `docs.*` keys below. |
| dSafePassage (#2) | The docs leg as an arm of the step gate: same population, graded whole, today's undocumented members on a shrink-only legacy list (C4 + C5). Fingerprints, doc tests and the offline link check; a planted stale page red. Each later class's join planted red by its own build. |
| dOrderedCharter (#3) | `usage` and `help` named on the unit registry (gap 3) and on drive rows; the page renderer in "the one renderer". |
| Each of builds 4–20 | Its own pages and its class's join. |
| dLinkedLibrary (#11) | The atlas↔help link arm (below). |
| dShippedRelease (#18) | A losing test for the derived runbook and release notes, and draining runbook parity's 18. |
| dConvergedCharter (#21) | Keeps the migration of hand pages and guides, C7's explanation render, the no-lost-rationale arm, and fate rows for kit READMEs, `README.md` and `WIRE-INTO-PROJECT.md`. |

**Before speccing starts:**
- v2 amended along those rows, and the clause 7 disagreement resolved.
- A baseline inventory of the population of user-facing surfaces, which seeds the legacy list.
- A decision on whether to add P41 ("every user-facing surface is documented from the fact that defines it") or rewrite `[docs]` to name its gate.
- Optionally, one unit with today's tools adding `docs` to the builder, spec-reviewer and diff-reviewer `rules:` lines.

**Policy keys:**

| Key | Allowed values | Default | Note |
|---|---|---|---|
| `docs.enforce` | refuse, warn, off | refuse | The owner set `budgets.enforce` to warn; refuse is recommended here because the prose rule measurably failed. |
| `docs.surfaces` | any non-empty subset of the step gate's classes | all | |
| `docs.examples` | checked, unchecked | checked | |
| `docs.explanation` | rendered, registry-only | rendered | |

**Owner forks:**
- **H1:** the leg at #2 (recommended), #3, or #21.
- **H2:** rendering rationale, which departs from SA-5's "never renders into a page". This conflicts with a recorded owner answer, so it needs your explicit ruling.
- **H3:** the `docs.enforce` default.
- **H4:** P41, or a rewrite of the `[docs]` rule.
- **H5:** the fate of the kit READMEs (reshape into generated reference plus authored how-to, or keep).

**Linking to the atlas.** The shared key is the tag (dOrderedCharter's tag grammar). Every rendered page carries its unit's tag anchor; every user-facing node in the atlas links to `HELP_DIR/<page>#<tag>`; the page links back to the node. One link check grades both directions. The atlas is rendered "from the same node table" (dLinkedLibrary clause 14), and its design belongs to the Q5 researcher.

**For other researchers:**
- **Q1/Q2:** later classes carry no join clause to the step gate on their own rows (`folds-closing-a:332`), so the docs leg's population is only as complete as those joins.

Relevant paths:
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-shape-reviews-compared.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/govkit/check_runbook_parity.py`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles/agents/gov-spec-writer.agent.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/help/roles.md`
