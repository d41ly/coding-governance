# Research: size caps, today and advisory

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 134's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-15-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md`.

---

I found 24 size caps on documents and records. 18 of them refuse a commit, push or render. My pick is the owner's direction with four additions: warnings shown even when the gate passes, an automatic over-budget record, a trend review that acts as the brake, and two classes of check kept out of the switch.

I wrote nothing in the repository. The temporary clone at `C:\Users\d41ly\AppData\Local\Temp\capsprobe-1424` is deleted. One thing to know: before I learned that `gov-researcher`'s gate allowlist is empty, I ran `check-template-size.sh` six times on that clone. The scratch-guard hook then blocked my next gate run, `gen_build_index.py --check-format`. Those six runs wrote nothing, but they were gate runs, and I ran no other gate after that. Outside sources were read on 2026-10-19.

## 1. Inventory of size caps today

"Refuse" means a non-zero exit. That blocks a commit wherever pre-commit runs the leg (`.githooks/pre-commit`: memory hygiene `--staged`, the manifest ratchet `--staged`, template size when the template is staged). It blocks a push or landing through the bar (`tools/gate-legs.json`), and it blocks remote CI.

| # | Subject | Cap | Enforcer | Mode | Set by |
|---|---|---|---|---|---|
| 1 | Charter template | 49152 B | `tools/check-template-size.sh:100,141-144`; row `tools/template-size-limits.txt:48` | refuse; growth past the recorded high-water only warns (`:221`) | declared row, falling back to the constant 49152 |
| 2 | `AGENTS.md` (rendered charter) | 20480 B | same gate; row `:85` | refuse, plus high-water warning | declared row |
| 3 | Kickoff engine `skills/session-kickoff/SKILL.md` | 18432 B | same gate; row `:60` | refuse | declared row |
| 4 | `memory/guides/BUILD-METHOD.md` | 30720 B (its 400-line half is read by nothing) | same gate; row `:126` | refuse; check 6 reds if the file's `**Budget:` prose disagrees with the row | declared row |
| 5 | `memory/guides/UNATTENDED-PROTOCOL.md` | 66860 B, pinned with no headroom | same gate; row `:143` | refuse | declared row |
| 6 | `.claude/skills/unattended/SKILL.md` | 10240 B | same gate; row `:151` | refuse | declared row |
| 7 | Every live spec | 49152 B (class row) | `tools/check-spec-tokens.py:921-944`; row `:167` | refuse; a spec held at its high-water may shrink, never grow | declared row |
| 8 | Charter and template line length | 450 chars | `tools/check-line-length.sh:53,154,182`; `tools/line-length-limits.txt:23-24` | refuse | declared row, falling back to `HARD_DEFAULT=450` |
| 9 | Guides (prose) | 98304 B / 1200 lines | `tools/memory-tree/check-memory-hygiene.sh:144`, check 6 at `:1027-1075` | refuse, unless listed in `curation-debt.txt` (`:431`) | constant, overridable in conf |
| 10 | Index and row documents | 61440 B, line axis retired | `check-memory-hygiene.sh:133`, overridden at `.memory-tree.conf:483-484` | refuse, unless listed in curation debt | conf (gov ships 20480 / 250) |
| 11 | Build README | 25600 B of authored bytes | `check-memory-hygiene.sh:145` | refuse, unless listed in curation debt | constant |
| 12 | Codebase-map dossier | 20480 B | `check-memory-hygiene.sh:150`; `.memory-tree.conf:495` | refuse (the remedy is a split) | conf |
| 13 | Index entry line | 300 chars (350 for a build README) | `check-memory-hygiene.sh:154`, check 7 at `:1164` | refuse, unless listed in curation debt | constant, overridable in conf |
| 14 | Build README slots (5) | 900 / 500 / 500 / 1800 / 1800 B | `tools/memory-tree/gen_build_index.py:1977-1981`; `build-readme-slot-limits.txt:27-31` | refuse; growth past the slot high-water is advisory only | declared file |
| 15 | Role bodies (10 roles) | 1536 to 4096 B | `tools/roles/check_roles.py:85-89,218-223` (R5) | refuse | constant dict |
| 16 | One-line charter rule | 200 chars | `tools/playbook/render_playbook.py:126,690` | refuse at render | constant |
| 17 | Roster line | 200 chars | `tools/roles/handoff.py:113,528` | refuse | constant |
| 18 | Session-kickoff manifest | 25600 B; 400 B per line; 400 B per traps bullet | `skills/session-kickoff/manifest-check.sh:1312-1316` (says "must be trimmed, not have the limit raised"), `:1336`, `:1544` | refuse | constant (the env override is for tests only) |
| 19 | Orientation card | 8192 B | `manifest-check.sh:216,710,1180-1181` | refuse; nothing is written | constant |
| 20 | Count of universal gotcha records | 6 | `tools/memory-tree/gotchas.py:543-548`; `.memory-tree.conf:561` | refuse | conf |
| 21 | Charter-cited file with no byte cap | must be capped or waived | `tools/memory-tree/corpus_ids.py:770-774` (`READ_PATH_WAIVER`) | refuse | conf |
| 22 | Recall export | 20480 B | `tools/memory-recall/query.py:177,1290-1294` | refuse | constant |
| 23 | Codex instruction size | 32768 B | `tools/agent-instructions/adopt-agent-instructions.sh:31,66` | warn only | constant (mirrors Codex) |
| 24 | Fitted outputs: runlog record 24576 B, feature card 1024 B, hook context 10000 chars | `tools/runlog/record.py:74,1165`; `tools/codebase-map/map_lib.py:1666`; `tools/hooks/scratch-guard.js:1456` | fit: shrink and state what was cut | constant (the 10000 is the harness's own cap) |

Also found:
- Prompts and help pages have no size cap. I searched `tools/` for a prompt byte cap and found none, and no leg reads `help/`.
- The charter's `[cost]` rule (`AGENTS.md:28`) caps a suite's wall-clock time, not a document's size. It does not belong to this inventory.
- `tools/unattended/adopt-unattended.sh:479` prints a note when the protocol renders over the adopter's guide cap.

Current headroom, in the gate's own output: `UNATTENDED-PROTOCOL.md` "66859 / 66860 bytes (1 under)", unattended `SKILL.md` "10237 / 10240 (3 under)", kickoff `SKILL.md` "18310 / 18432 (122 under)", `BUILD-METHOD.md` "29326 / 30720 (1394 under)".

## 2. History (repository span 2026-07-01 to 2026-10-19, 5562 non-merge commits)

| Cap | Movements | Commits |
|---|---|---|
| Read-path ceiling (retired) | 26 movements in 17 days (20 up, 4 down), 24150 to 161120 B, then retired. The limits file's own header: "27 movements bought no trim". | first `3e9249d44` 2026-08-08; retired `47f9ba6b3` 2026-08-25 |
| Template | 32 KiB "never raise" (`541c5b783` 07-12), then 48 KiB on owner order with 86 B free and "every edit funded by externalizing prose" | `1640f6808` 08-16 |
| `AGENTS.md` | seeded 64512, lowered to 16384, raised to 20480 (it had breached at 16729) | `e1919b284`, `c8ed3dd38`, `04f77d6c8` 10-13 |
| `BUILD-METHOD.md` | 4 raises, all owner calls: 20 KB/250 → 24 KB/310 (08-21; commit not found, merge-borne, the file's own history at `BUILD-METHOD.md:10-14`) → 350 lines → 27648 → 30720/400. The 08-21 raise came from a merge overflow. | `b73665492`, `f13c071ab`, `5da7d8ad2` |
| Unattended protocol (pinned, no headroom) | 3 raises in 3 days | `ff0b3dc32`, `1d1136209`, merge `63a43402c` |
| Guide class | 20 KB → 60 KB (3x), then 98304/1200 after a merge-induced overflow carried as curation debt | `a9ccc4c18`, `f632fbde4` |
| Row class | line axis retired; 61440 B declared | merge `7761bbf23` 08-18 |
| Universal records | 3 → 4 → 5 → 6 | `30d1e963b`, `b3f8ca91c`, `8364d9ec9` |
| Curation-debt waivers | 7 rows added, 10 removed (non-merge) across 9 commits. Drains came from raises or re-pricing, not trims (`f632fbde4`, `6e88655eb`). | |
| Never moved | kickoff 18432, line length 450, entries 300/350, manifest 25600/400, role bodies, one-line 200, unattended `SKILL.md` 10240, slot ceilings | |

Where a cap bit and forced a cut: the manifest trim (`beb5fce43`: "+1240 B put the manifest 936 B over … TRIMMED"), the traps eviction (`d816c30be`), and the 32 KiB template externalization (`541c5b783`).

Slot ceilings: `beb5fce43` blanked all five, but through a scaffolder bug, not an agent loosening them. The bar stayed green because a blank ceiling is legal (`54bb62769`).

How often a cap blocked: not derivable exactly.
- Pre-commit refusals are not logged.
- `.git/runlog/gates.log` covers only 80 bar runs on this node (2026-09-14 to 10-16). It shows "memory hygiene" failing in 19 runs and "build README slot contract" in 7, but it does not name the check inside the leg.
- The raises above are a lower bound on blocks.

## 3. What the design already decides

- **Caps are re-derived from evidence.** v2 `[principles]` P9 (`architecture-v2.md:704-705`). Walk R4: the owner said "Caps often get in the way of work but it's clear caps are needed" (`walkthrough.md:745-748`). The revision defines a soft cap as one "that warns and asks for a recorded reason" (`walkthrough.md:752-758`).
- **`budgets.*`** is "each cap's value and its mode, hard or soft" (v2 `[policies]` `:1101`). The presets (v2 `[presets]` `:1386`) are: velocity, every cap soft; standard (the default) and guarded, each cap's evidence-derived mode; strict, every cap hard.
- **Render budget.** `instructions.checks`: refuse, warn or record, default refuse; velocity sets warn (`:1017`, `:1302`). P27 refuses an over-budget load set *and* one missing a required unit under that same switch (`:787-797`; `layer-instruction.md:444-466` R-C). R-C extends `template-size-limits.txt` and keeps the summed budget retired. The adopter render "refuses, naming the largest contributors" (`adopter-instructions.md:170-172`).
- **Already advisory or degrading:** `orient.budget` record-only (`:966`), `memory.over-budget` report (`:1125`), `memory.map-overflow` degrade with a 32k map (`:1127-1128`; `project-map.md [fit]` `:605-614`). `annotations.budget` defaults to refuse (`:1109`).
- **Who builds it:** dCalibratedLens owns the value ledger, the Loop Review and the cap re-derivation (`:1501`).

## 4. Prior art

- **Severity levels, warn exits 0.** Lighthouse CI off/warn/error, where warn is "printed to stderr, but failure will not result in a non-zero exit code" (https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/configuration.md). ESLint, where warn "doesn't affect exit code" and is "typically used when introducing a new rule that will eventually be set to 'error'" (https://eslint.org/docs/latest/use/configure/rules). webpack `performance.hints` is warning in production mode and recommends error for production builds (https://webpack.js.org/configuration/performance/). The page also lists a `stats` mode; I could not confirm it, so treat it as uncertain.
- **Warnings become effective through a count threshold.** ESLint `--max-warnings` exits 1 on "more linting warnings than allowed" (https://eslint.org/docs/latest/use/command-line-interface). ESLint's `max-lines` defaults to 300 (https://eslint.org/docs/latest/rules/max-lines).
- **Hard limit only.** size-limit "throws an error if the cost exceeds the limit"; its action comments on PRs and rejects them (https://github.com/ai/size-limit, https://github.com/andresz1/size-limit-action). bundlesize has `maxSize` and no warn level (https://github.com/siddharthkp/bundlesize).
- **Ratchets.** betterer fails "if it gets worse", and in CI fails on any difference (https://phenomnomnominal.github.io/betterer/docs/introduction, …/running-betterer). ESLint bulk suppressions in `eslint-suppressions.json` hold the existing errors and enforce the rule on new code (https://eslint.org/docs/latest/use/suppressions).
- **Plain warnings get ignored.** Google: "developers ignore compiler warnings … We either enable a compiler check as an error … or don't show it", and "Code review is a sweet spot" (https://abseil.io/resources/swe-book/html/ch20.html). web.dev says over budget, optimize, remove or don't add; the page is dated 2018-11-05 (https://web.dev/articles/performance-budgets-101).
- **Agent context.** Claude Code: CLAUDE.md "target under 200 lines … Longer files … reduce adherence"; auto-memory loads only the first 200 lines or 25 KB (https://code.claude.com/docs/en/memory). Codex "stops adding files once the combined size reaches" 32 KiB (https://learn.chatgpt.com/docs/agent-configuration/agents-md). Anthropic: context is "a finite resource with diminishing marginal returns" (2025-09-29, https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). Chroma: performance "varies significantly as input length changes, even on simple tasks" (2025-07-14, https://www.trychroma.com/research/context-rot). IFScale: the best models reach about 68% at 500 instructions (https://arxiv.org/abs/2507.11538).

## 5. Candidates, each with its losing test and result

- **A. The owner's direction taken literally: one switch, default warn, every cap prints a warning.**
  - Test A1, does a warning in a passing leg reach anyone? **Lost.** `tools/run-gates/run-gates.sh:4041` prints only `GATE ok <name>`. Two warnings are firing today that nobody has seen: "TEMPLATE-SIZE WARN — BUILD-METHOD.md … 28351 -> 29326 (+975)" and "SKILL.md … 10059 -> 10237 (+178)". The slot high-water file already says "an advisory inside a green leg reaches nobody".
  - Test A2, can one switch flip every cap safely? **Lost.** `instructions.checks` also controls the missing-required-unit refusal, which is a correctness check, not a size cap. Rows 19, 23 and 24 mirror limits set by the consumer (harness 10000 chars, Codex 32 KiB). Exceeding those silently loses text rather than just costing reads.
- **B. A completed: advisory caps that are visible, priced and trended.**
  - Mechanism: owner-set values in policy, `budgets.enforce` defaulting to warn, and per-cap overrides. Every breach is printed even on a passing run and in the landing record. It is journaled automatically, keyed by unit, so no tracked file is written by a gate (per `[class]`). The value ledger prices it as bytes times reads. The Loop Review raises an owner item when a breach persists or keeps growing. Consumer limits (fit or refuse) and correctness checks stay outside the switch.
  - Test B1, do non-blocking recorded breaches get drained? **Partial loss.** The curation-debt rows drained only through raises or re-pricing, and the 38 KB `aBoundedVerdict` README row (`memory/project/curation-debt.txt`) still stands. So the review step is the only brake, and B does no better than its Loop Review.
  - Test B2, does a planted over-budget document make a passing bar print the breach, and does the next Loop Review item name it? This is the build's test; I did not build it.
  - Advisory mode also removes the merge-overflow blocks (`check-memory-hygiene.sh:136-139`; the 08-21 method raise), where the person merging was blocked by bytes neither branch alone exceeded.
- **C. Ratchet or high-water, with no absolute level.** Test: does a refusing ratchet cost fewer blocks than a cap with headroom? **Lost.** The no-headroom protocol pin moved 3 times in 3 days, against 1 move in 64 days for the 48 KiB template row. Run in warn mode it is just A. It survives only as the "what grew" filter inside B.
- **D. Fit at the reader: degrade at render, never refuse.** Test: does each capped instruction document have a declared order for degrading that drops no binding text? **Lost** for prose: every one-line rule binds, and M7 re-reads the method whole (`BUILD-METHOD.md:6-8`). It **wins** only for generated outputs, which already do it (row 24, the map's `[fit]`).
- **E. Review only, nothing per change.** Test: has a report-only size signal ever produced a trim here? **Lost.** The existing high-water warnings went unacted on. Google's finding is that unseen warnings are ignored, and the author never learns at write time.
- **F. Keep hard caps but make raising cheap (status quo plus `TOOL-aOrientedCast-23`).** Test: does a breach still red the bar? **Lost** by definition. It turns the owner's complaint, agents relaxing caps, into a ritual.

I stopped there: a further candidate, such as "one in, one out" offsets, is a refusing ratchet (C) under another name.

## 6. My pick: B

`budgets.enforce` defaults to warn. Values are owner-defined per cap, and a cap can be pinned to refuse. Three classes stay outside the switch:
- consumer limits (Codex 32 KiB, the harness's 10000-char hook context, the 8192 B card), which fit or refuse;
- correctness checks, which means splitting `instructions.checks` into a size key and a missing-unit key;
- grammar limits that define a format (the one-line 200 chars, entry lengths). These never moved, so they cost nothing to keep.

An advisory cap needs four things to bite:
1. It is shown even when the run passes (fix `run-gates.sh:4041`).
2. Each breach is attributed to its unit.
3. It is priced by how often the document is read.
4. Trend reviews turn persistent growth into an owner item, counting only new or grown breaches so the warnings don't become noise.

Where an advisory cap still fails:
- under velocity or any adopter that has no Loop Review;
- in unattended runs, where nobody reads the output;
- at consumer limits.

Record-versus-code disagreements I found:
- `layer-instruction.md:292` says "the charter's 32 KiB cap". The code has 20480 for `AGENTS.md`; 32 KiB is only Codex's limit, which gov warns on.
- Walk R4's "charter's 48 KiB" is the template's cap, not the charter's.
- `build-readme-slot-limits.txt` says its values "bind nothing today", yet `memory/project/readme-contract.txt` binds 98 READMEs.
- The handed fact lists `[cost]` as a cap, but it is a wall-clock ceiling, not a size cap.

Files: `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\template-size-limits.txt`, `…\tools\check-template-size.sh`, `…\tools\memory-tree\check-memory-hygiene.sh`, `…\tools\run-gates\run-gates.sh`, `…\memory\builds\dClosedLoop\build\2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
