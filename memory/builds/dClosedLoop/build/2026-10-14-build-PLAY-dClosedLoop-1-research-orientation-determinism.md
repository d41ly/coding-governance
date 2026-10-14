# Research: agent determinism — what bounds each role's and workflow's actions, and measured deviation

**Serves:** research PLAY-dClosedLoop-1

The gov-researcher's return for handoff `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-9-researcher.md`
(dispatch 14), verbatim. The harness escaped `<`, `>` and `&` in the returned text as HTML entities;
they are restored here, and nothing else is changed.

---

## 1. Inventory

**Roles.** The base files are `tools/roles/agents/*.agent.md`. Every `tools/roles/house/*.md` overlay is a 0-byte file, so each rendered `.claude/agents/*.md` is the base file alone. All typed spawns are refused unless they carry a rendered handoff (agent-cap.js:39-56, rule 6). Gate allowlists come from `policy.toml` and are rendered into `.claude/roles.json`; scratch-guard's role-gate arm (`checkRoleGate`, scratch-guard.js:1421) enforces them.
- **gov-orienter.** Trigger: kickoff opt-in. Brief: `question`, `prompt?`. Tools: Read/Grep/Glob/Bash. Refused: any gate. Output: card body. Check: `manifest-check.sh --card --append` checks the card's grammar, not the return.
- **gov-reuse-scout.** Trigger: kickoff asks for a scout. Brief: `question`, `task:in?`, `card:reuse?`. Tools: Read/Grep/Glob/Bash. Output: a seam. Unchecked (workflows.toml: `enforced-by = "none"`).
- **gov-spec-writer.** Trigger: spec-write stage. Brief: five `brief:` keys. Tools: adds Write/Edit. Write gate: spec class admitted (`checkRoleWrite`, :1064). Gates: memory hygiene and lexicon. Output: authored/present/refused, schema-checked in unattended-build.js; the specs themselves go to the hygiene leg.
- **gov-builder.** Trigger: one unit. Brief: `spec`, `card:route?`, `brief:non-goals?`. Tools: adds Write/Edit. Write gate: product class, only for a routed buildable unit. Gates: lexicon. Output: `UNIT_SCHEMA` (unattended-unit.js:206), checked for shape only. The sha is never resolved by the harness.
- **gov-spec-reviewer and gov-diff-reviewer.** No write tools. Output: `FINDING_SCHEMA` (tier2-review.js:561).
- **gov-skeptic.** No write tools. Output: `VERDICT_SCHEMA` (:603).
- **gov-synthesizer.** Has Write, class `review`, but that class is "read by nothing" (scratch-guard.js:103). Output: report path, joined by `check-review-join.sh`.
- **gov-researcher.** Read tools, Bash, Web tools; no Write. Output: prose. Unchecked; format-guard only requires a `returned` line.
- **gov-session.** `agent:false`. Output: a prompt file, checked by `handoff.py check` (hash re-derivation).

**Workflows** (workflows.toml):
- **orient** runs in the main loop; enforced only by the card writer.
- **reuse** has none.
- **spec-write and build** run in harnesses (unattended-build.js, unattended-unit.js), bound by the write gate's role arm plus routed commits.
- **spec-review and closing-review** run in tier2-review.js; the spawn guard binds the `Workflow` call only.
- **gate-bar** is bound by the pre-push hook.
- **research** is bound by the spawn guard.
- **handoff** has none.
- **bookkeeping** is bound by the memory hygiene leg.
- `roles/README.md:37`: "The checker grades that each entry names something, not that the thing exists."

**Skills:**
- **/build** (`.claude/skills/build/SKILL.md`) is a router to BUILD-METHOD.
- **/unattended** runs preflight, kickoff, then the driver verbs. gate-guard refuses the flagged bar before VERIFYING, and refuses `AskUserQuestion` under a live lease.
- **/session-kickoff** (Steps 0-5) ends at a READY card.
- format-guard (Stop) checks the BUILD/SPEC pair and the `agent`/`returned` lines.

## 2. Sequence

**Attended build** (/build):
- *Bound:* READY card and owner go; stage 3 harness call with `roles`/`efforts` from `handoff.py`; per unit: status flip, `--card --append` route, unit dispatch; a branch on `diverged`; tier2 closing review; one bar.
- *Left to the agent:* which files to read and how often, every probe, the builder's choice of "fixture or probe", the content of fix records, and when to re-review. Side edits outside the unit are left to the agent too: the write gate checks the route, not the item.

**Unattended run:**
- *Bound:* preflight, kickoff, driver verbs (`--plan`, recording), the harness stages, the no-ask arm, and stop-guard.
- *Left to the agent:* M3 fork judgement, the close's M9 derivation, the hold/park choice, and all probing.

## 3. Measurements

Corpus: 39 project dirs, 3,234 jsonl files (3,170 subagent), 369 workflow journals. Every probe streamed line by line, read-only.

1. **Agent-type census** (`.meta.json` agentType): workflow-subagent 2,582 · general-purpose 84 · gov-spec-writer 45 · gov-spec-reviewer 20 · gov-skeptic 20 · Plan 18 · gov-researcher 14 · gov-builder 13 · gov-synthesizer 4. Typed agents are 116 of 2,800 (4.1%).
2. **(a) Gate runs by role.** Predicate: per `&&`/`;`/`|` segment, a launcher (or none) followed by `run-gates.sh|run-selftests.sh|run-unattended-gates.sh|*.test.sh|selftest.py`, excluding `--help|--list|--render` and `bash -n`. Role resolved from meta, then journal label, then prompt opening.
   - Untyped builders before the arm (2026-10-12): 533 runs in 86 of 104 agents.
   - Typed roles after it: 34 runs at command position, **all passed** (builder 6, spec-writer 19, spec-reviewer 5, skeptic 3, researcher 1). In the same population the arm's deny text appears 9 times, on other commands.
3. **Replay of the arm** (synthetic `agent_type: gov-builder` payloads piped to scratch-guard.js). `run-gates.sh`, `cd <tree> && …test.sh`, a `| tail` form, and `GATE_JOBS=1 …run-gates.sh` **all exit 2**. The predicate refuses these shapes, so the field escape is in the payload or the wiring. Cause not determined.
4. **(a) Writes.**
   - Typed read-only roles (researcher, skeptic, both reviewers, scout, orienter): 0 Write/Edit calls.
   - Builder spec edits after the arm: 0 content edits, 10 status-line flips (which are admitted).
   - Before the arm: untyped builders 334 spec content writes; untyped skeptic-labelled agents 221.
   - Bash write-shaped commands (heuristic `tee|sed -i|> path`) from typed researchers: 6.
5. **(b) Journal returns.** started 2,699 · result 2,607 · failed 73 · no terminal entry 19 · string (unstructured) result 30. Unit-shaped returns: 113. Of those, `committed:true` 105, and `git cat-file -e` shows 105 of 105 shas exist. 5 `DIVERGENCE:` returns.
6. **(b) Researcher shape.** Population: 14 direct spawns whose prompt says "exactly six headings". Of 10 finished: 3 have six markdown headings, 2 six numbered/bold ones, and 5 never ended on a final text turn (last stop `tool_use`/none). 4 of 14 exceeded the word cap.
7. **(c) Main loop** (64 top-level transcripts, 28,727 tool calls):

   | Class | Share |
   |---|---|
   | ad-hoc shell probe | 40.4% |
   | protocol script | 26.0% |
   | git read | 10.8% |
   | scratch write | 5.1% |
   | build-record write | 4.5% |
   | product edit from the main loop | 3.7% |
   | dispatch/skill/ask | 3.0% |
   | Read/Grep/Glob | 2.7% |

   - Repeated `git status/log` per session beyond the first: 1,579.
   - Repeated Read/Grep/Glob of the same target: 186 of 779.
   - Probe first words after `cd`: grep 1,608, python 1,244, sed 1,137.
8. **(d) Static scan** (`grep` for `.indexOf/.match/.test/.startsWith` on return fields across `tools/workflows/*.js`): 1 site, unattended-unit.js:348, `diverged` derived from `why.indexOf('DIVERGENCE:') === 0`. Its consumer is `.claude/skills/build/SKILL.md:68`. Every other `agent()` call passes a `schema`.

## 4. Gaps

- **HIGH.** The role-gate arm does not bind in the field: 34 typed gate runs passed versus 9 denials, while a replay of the same shapes exits 2 (probes 2-3).
- **HIGH.** `writes: none` and `review` are unenforced outside product and spec paths: scratch-guard.js:103 and :1173 (`return null`). Bash writes are never seen (:85).
- **HIGH.** About 63% of main-loop calls have no protocol step behind them (probe 7).
- **MED.** `agent()` spawns inside a harness escape rule 6, and their briefs are strings the script builds (agent-cap.js:55 ceiling; unattended-unit.js:257).
- **MED.** A free-text branch: unattended-unit.js:348 feeds SKILL.md:68.
- **MED.** Commit claims are only shape-checked. Absent: `require`/`child_process` in unattended-*.js and tier2-review.js, so a harness cannot resolve a sha. Today 105 of 105 are real.
- **MED.** Researcher returns are unchecked: 5 of 10 finished without a final turn.
- **MED.** 92 harness agents (73 failed, 19 with no terminal entry) and 30 unstructured results.
- **LOW.** `enforced-by` is graded for being named, not for existing (roles/README.md:37). `reuse` and `handoff` read `none`.
- **Hand-offs:** re-orientation cost (probe 7's repeats) to the orientation researcher; trusting the sha claims to the trust researcher.

## 5. Candidates

**A. Per-item allowance at the tool call.**
- *Mechanism:* `roles.json` keys on (step, item) instead of role: a write glob, a gate list and a tool list per item. PreToolUse hooks read the active item from a hook-written record.
- *Seam:* `tools/hooks/scratch-guard.js` (`checkRoleWrite`, `checkRoleGate`) and `tools/roles/roles_lib.py`.
- *Losing test:* an allowance a hook already holds escapes in the field.
- *Result:* **loses as the sole mechanism.** 34 un-refused gate runs against an armed allowlist, and Bash writes are unseen.

**B. The checklist is a program.**
- *Mechanism:* each item is one schema-bound `agent()` with a typed role and a `handoff.py`-rendered brief. The driver resolves each return's witness (git object, file, verdict) before it starts the next item. The main loop only calls `next` and the harness.
- *Seam:* `tools/roles/workflows.toml` (`stages` becomes items), `tools/workflows/unattended-unit.js`, `tools/roles/handoff.py`.
- *Losing test:* a harness branch reads free text, or a return claim proves false.
- *Result:* survives with one repair. There is 1 free-text branch (make `diverged` an enum field), 0 false claims of 105, and 2,577 of 2,607 results (98.8%) are structured. Still unproven: that the main loop's 63% collapses to `next`. That is a design claim no probe can test today.

**C. Post-hoc witness.**
- *Mechanism:* agents act freely. A transition check reads the CLI transcript and git, and refuses the step until every item's witness holds and no out-of-allowance act is found.
- *Seam:* `tools/hooks/format-guard.js`, which already reads the turn transcript and the workflow journals.
- *Losing test:* the cost of a deviation is spent before it is detected.
- *Result:* **loses on prevention.** 533 gate runs in 86 of 104 builders would have been caught only after the hours were spent. It is still the right verifier of B's witnesses.

## 6. Pick

I recommend B: it is the only mechanism whose losing test it survives on the real tree. Schema returns are already 98.8% of results, the one free-text branch is a single field, and every claimed commit resolves. It turns "a set checklist with specific roles" into the program's control flow rather than an allowlist the agent can route around, and today's hook arm demonstrably is routed around. Cost:
- an item table in workflows.toml with per-item renders in handoff.py;
- a witness-resolving `next` step in the unattended driver;
- the `diverged` enum;
- more spawns than today's 7.3 per run, one per item.

Keep A's existing arms as the backstop and C's transcript reader as the verifier, but only after the escape in probe 3 is explained.
