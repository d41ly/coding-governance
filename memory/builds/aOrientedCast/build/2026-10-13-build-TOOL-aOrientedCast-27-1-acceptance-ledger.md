# TOOL-aOrientedCast-27 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-27

Direct checks only: no gate, suite, slice or self-test ran in this pass. What ran: `handoff.py
render` twice in this repository (AC1); fixture H, a scratch directory holding an empty `.git`, this
repository's role index and two rendered prompt files, piped to `tools/hooks/agent-cap.js` (AC2 to
AC4); fixture F, the roles suite's `build_fixture` repeated by hand under `%TEMP%/oc27f` and arm 6's
render, payloads and hook calls run in it (AC5); stub T, the build suite's `run_wf` copied into the
scratch path with the section 4 split, over both rendered build harnesses and the unit harness
(AC6, AC7, AC14, AC15, and the fixtures of the suite's new OC27 block); stub R, the review suite's
`runReview` copied the same way, over the rendered review harness (AC8, AC16); AC9's `python -c`
probe and arm 12's own snippet; `check-protocol-parity.test.sh --render`, whose `--check` the role
gate refuses, so freshness was observed as AC10's diff comparison instead; `node --check` over the
review suite's embedded JS, the build suite's runner and the hook, an `AsyncFunction` compile of the
three harnesses and `bash -n` over scratch copies of the four suites; `lexicon.py --suggest` for
`render_spawn_name`, `extract_label_unit`, `renderSpawnName` and `renderAgentLabel`, each OK; and
`gen_map.py --write`. Owed to the main loop at the close (M8): every leg section 7 lists, the four
edited suites among them, and the RED-first observation of each of section 7's seven `New arm:`
lines on its staged break, then green once restored; AC12's rendered `.claude/skills/build/SKILL.md`,
which the main loop's second pass re-renders with `bash tools/roles/adopt-roles.sh --scaffold`.

**Evidences:** TOOL-aOrientedCast-27
- AC1 — `handoff: description` — the render with `--unit` exited 0, its stdout opening with the marker line and holding no `handoff: description` line, its stderr holding one line, `handoff: description — aOrientedCast · TOOL-aOrientedCast-27 · closing-review`; without `--unit` the line read `handoff: description — aOrientedCast · closing-review`; `git status --porcelain` printed the same before and after both runs.
- AC2 — `node tools/hooks/agent-cap.js` — in fixture H, P1 with `bx · TOOL-bx-1 · spec-write` and P2 with `bx · spec-write` each exited 0 with empty stderr, and the slot ledger under H's `.git` held each call's `tool_use_id`.
- AC3 — `rule 6` — P1 with no description, `Fold two specs, spec three units`, `bx · TOOL-bx-1 · spec-trim`, `bx · TOOL-bx-2 · spec-write` and `bx · spec-write`, and P2 with `bx · - · spec-write`, each exited 2 naming rule 6, the call's description (`null` for none) and `"bx · TOOL-bx-1 · spec-write"`, or `"bx · spec-write"` for P2, and no slot held a refused call's id; P1 one character off with `Fold two specs` named `prompt line 9 differs` and not the description.
- AC4 — `gov-spec-writer` — with `workflow` deleted from H's index entry for `gov-spec-writer`, the right-named P1 payload exited 2: `declares no workflow for gov-spec-writer, so this spawn's name cannot be derived`.
- AC5 — `bx · TOOL-bx-1 · researcher` — in fixture F the render exited 0 and printed `"bx · TOOL-bx-1 · research"` as the name; its task part with that description exited 0 with empty stderr, and with `bx · TOOL-bx-1 · researcher` exited 2, the refusal naming `"bx · TOOL-bx-1 · research"`.
- AC6 — `tB · specs · commit` — stub T over the audit-OFF units, every unit authored and committed once, printed one `label:tB · A-tB-1 A-tB-2 · spec-write`, one `label:tB · A-tB-3 · spec-write` and one `label:tB · specs · commit`; unattended with `specAudit`, the subjects stripped and returns keyed `spec-write`, `subjects`, `record` and `dispose`, it printed `tB · audit round 1 · subjects`, `tB · audit round 1 · record` and `tB · audit round 1 · dispose`, one each.
- AC7 — `tB · A-tB-1 · build` — stub T over `unattended-unit.js` with `CHILD_ARGS` printed one `label:tB · A-tB-1 · build` in each mode.
- AC8 — `["find:seams"]` — stub R over the `DIFF` args with `reviewDir` `memory/builds/tB/reviews` gave 12 labels, every one opening `tB · diff-review round 1 · `, one ending `resume:probe`, five `find:<lens>`, five `verify:ids-<a>-<b>` and one `synth`; with `memory/reviews` all 12 opened `diff-review round 1 · `; over `SPEC` all 12 opened `spec-audit round 1 · `; with `find:seams` dead the result's `pending` was `["find:seams"]`.
- AC9 — `extract_label_unit` — the probe printed `['TOOL-aOrientedCast-27', None, None, 'TOOL-tFix-1']`; the grep printed the definition at `tools/roles/handoff.py:145` and its call in `print_agent_lines` at `:886`.
- AC10 — `tools/workflows/tier2-review.js` — the added and removed lines of `git diff -U0` against the parent were identical for `tier2-review.template.js` and `tier2-review.js` (51 lines) and for `unattended-build.template.js` and `unattended-build.js` (28 lines), observed on the working tree this commit carries.
- AC11 — `grep -n "one unit id" tools/roles/README.md` — the five-file count printed 2, 1, 1, 1 and 2; the `## How agents are named` and `## Agent labels` counts printed 1 each; the grep printed the field table's unit row at `tools/roles/README.md:110`.
- AC12 — `KIT_AGENT_CAP_VERSION` — `1.37` at the parent, `1.38` now, and `gov:kit agent-cap@1.38` lists `agent-cap.js`, `format-guard.js` and `scratch-guard.js`; `KIT_ROLES_VERSION` moved `1.4` to `1.5`, `gov:kit roles@1.5` counting 1 in `tools/roles/README.md` and `tools/roles/SKILL.template.md` and 0 in `.claude/skills/build/SKILL.md`, which the main loop's second pass re-renders, as the criterion's `permission:` states; `version: '1.50'` counted 1 in both review-harness files.
- AC13 — `grep -c "TOOL-aOrientedCast-27" memory/map/features/roles.md` — it printed 2; the label-shape count printed 1 for `memory/map/features/review-harnesses.md` and for `tools/workflows/README.md`; `git diff --quiet` against the parent over `memory/map/features/agent-cap.md` exited 0.
- AC14 — `log:tB · A-tB-1 · build` — stub T over `unattended-unit.js` in each mode printed `log:tB · A-tB-1 · build` as its first line, ahead of `phase:Unit`, and a RESULT line opening `RESULT {"identity":"tB · A-tB-1 · build",`.
- AC15 — `log:tB · unattended round 1 · spec, audit, disposal, hand-out` — stub T over `UNITS` with `SPEC_OK` and `DEF` printed it first, ahead of every `roles:` line and `phase:Spec`, and a RESULT opening `RESULT {"identity":` with that text; over `A_UNITS` it read `attended`, and over `OFF_UNITS` `log:tB · unattended round 1 · spec, hand-out`, each return leading with it.
- AC16 — `logs[0]` — stub R's `logs[0]` was `tB · diff-review round 1 · review` and the result's first key `identity`, holding it; over `SPEC` it was `spec-audit round 1 · review`; the grep printed `log(identity)` at `tools/workflows/tier2-review.js:304`, above `phase('Resume')` at `:934`.
- AC17 — `grep -c "title" help/roles.md tools/roles/README.md` — it printed 1 for each file, and the `first log line` count printed 1 for each of its three files.
