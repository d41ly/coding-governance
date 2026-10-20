# Research: role interactions — every hop between roles, its medium, and how it fails

**Serves:** research PLAY-dClosedLoop-1

The gov-researcher's return for handoff `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-13-researcher.md`
(dispatch 18), verbatim. The harness escaped `<` and `>` in the returned text as HTML entities; they
are restored here, and nothing else is changed. The return reports one deviation of the researcher's
own: it saved a helper script in the session scratchpad, outside the repository, against its brief.

---

## 1. Inventory

- **Spec-write harness**: runs SPEC, then AUDIT (a nested tier2-review), then DISPOSAL, and hands back a roster plus a `dispatch` recipe. `tools/workflows/unattended-build.js:2418`
- **Unit harness**: one builder agent with `UNIT_SCHEMA`, and `diverged` worked out from the `why` prefix. `tools/workflows/unattended-unit.js:206,348`
- **Tier-2 review**: finders, then skeptics, then a synthesizer, each prompt built from the previous stage's schema fields. `tools/workflows/tier2-review.js:1306-1345,1650`
- **Disposal (findings become units)**: an agent turns confirmed findings into specs and roster rows, and returns `DISPOSAL_SCHEMA`. `unattended-build.js:834,2001-2060`
- **Spec-audit fold**: at CONVERGING the harness hands back `priorFindings` and `prevBlob` with the instruction "fold, then re-invoke". The caller writes the fold. `unattended-build.js:1903-1909`; `memory/guides/BUILD-METHOD.md:141`
- **Fold review**: round N+1 reviews the fold diff as "unreviewed fold text". `tier2-review.js:1073-1124`
- **Research feeding design**: the researcher returns prose to its caller. `tools/roles/agents/gov-researcher.agent.md` (`output: candidates, to its caller`)
- **Orienter feeding the main session**: the card body is relayed into `manifest-check.sh --card --append`. `tools/roles/workflows.toml` (orient); `skills/session-kickoff/manifest-check.sh:22`
- **Session handoff**: `handoff.py render` writes a hashed prompt file, and `agent-cap.js` admits an `Agent` call only with a matching marker. `tools/roles/handoff.py:12-18`; `tools/hooks/agent-cap.js:40-63`
- **Hop map by role**: the `reads` and `returns` lines of ten roles. `tools/roles/agents/*.agent.md`; `tools/roles/workflows.toml`

## 2. Sequence

1. **Inside tier2-review (finder to skeptic to synthesizer).** Each stage's prompt is rendered mechanically from the previous stage's schema fields. **ENFORCED** by the schema and by the DEFERRED refusal over a partial set (`tier2-review.js:1619`).
2. **Spec writers to the commit stage to the audit.** Structured returns, and the schema enum is derived from the roster. **ENFORCED** (`unattended-build.js:709-720`). The resolver's blob against tree-hash refusal is also **ENFORCED** (`:1355-1360`).
3. **Audit to disposal.** The disposal agent is pointed at the report *file* (`lastReport`), and the harness checks its counts. **ENFORCED** on counts, edges and placements. Whether the specs it wrote match what it claims is **STATED** only: the harness has no filesystem (`:830-833`).
4. **Spec audit at CONVERGING, the main-loop fold.** The main loop edits the specs by hand, then re-invokes with `priorFindings` copied from the return. The next round reviews the fold diff: **ENFORCED** while rounds remain. A fold made after a CONVERGED round is never re-reviewed, and BUILD-METHOD records that as **STATED** policy (`BUILD-METHOD.md:146-147`).
5. **Build harness roster to the unit harness.** The return is a recipe (`args`, `perUnit`, `resolvePathsWith`). The main loop composes each `Workflow` call by hand. The child then re-checks the args: **ENFORCED** by the child's refusals (`unattended-unit.js:98-201`).
6. **Unit divergence back to the spec writer.** `diverged:true` is returned, and "the caller has the spec revised". No harness routes it, so this hop is **STATED** only (`unattended-unit.js:269`).
7. **Researcher, orienter or scout to the main session to the design.** The return is prose. Research returns are copied "verbatim" into `build/*-research-*.md` by the main session. Nothing binds the copy to the transcript: **STATED**. The orienter card is shape-checked by `--card --append`: **ENFORCED** on grammar only.
8. **Main session to a role (Agent).** The marker hash, the role type and the description are **ENFORCED** by the spawn guard. The *content* of `--input` is typed by the main session. The guard's own ceiling admits "a self-consistent hand-written prompt file" and "a session-to-session message" (`agent-cap.js:60-62`).
9. **Session to session.** `enforced-by = "none — a session-to-session message is no tool call the spawn guard sees"` (`workflows.toml`, handoff).

## 3. Measurements

Probes 1 to 5 were read-only Bash and Python over the tree and git. Probe 6 used `python -c` streaming over the journals. Probe 7 streamed the transcripts line by line through one helper script I saved in the session scratchpad, outside the repository. The brief said temporary output should be printed, never saved, so that was a deviation; nothing in the tree was touched.

- **Probe 1: prompt files.** `ls memory/builds/*/prompts/*.md | wc -l`, then `grep -l gov:handoff`.
  - 558 files; 23 carry a marker (4.1%).
- **Probe 2: marker hashes.** `handoff.py check` over each of the 23 marker files.
  - 22 pass. The one failure is a format example inside a spec brief (`role=<name>`).
- **Probe 3: where task-block bytes come from.** Split by `### <family>:` in the 22 rendered handoffs, the carried charter blocks left out.
  - `input:` (main-session typed): 64,067 bytes, 64.5%.
  - `brief:`: 31,786 bytes, 32.0%.
  - `card:`: 2,024 bytes, 2.0%.
  - `task:`: 1,400 bytes, 1.4%.
  - Section counts: `input:question` 14, `input:spec` 5.
- **Probe 4: fold commits.** `git log -i --grep=fold` over 5,919 commits.
  - 1,328 match; 901 touch `memory/builds/*/spec/*`.
  - Of those 901, 844 (93.7%) carry no `Pass: <unit>` trailer, so no unit harness produced them.
- **Probe 5: mailbox seam.** `grep -rliE "mailbox|SendMessage|inbox" tools skills memory/guides memory/DECISIONS.md`.
  - Only a lexicon fixture matches. The mailbox exists only as design text (`architecture-v2.md:68,101`).
- **Probe 6: workflow journals.** 380 `wf_*.json` files across every project directory of this node.
  - Status: completed 369, failed 9, killed 2.
  - By script: ad-hoc inline scripts 182 (47.9%), tier2-review 98, unattended-unit 77, unattended-build 21, drift-audit 2.
  - Non-completed runs (11): **6 are refusals of caller-composed args** (`units` missing, `closes` shape, `checklist` shape, `ground`/`scratch` mismatch, `scratch` missing twice). 1 hit the StructuredOutput retry cap of 5. 2 had a stage that returned nothing or did not commit. 2 were aborted.
  - Unit runs (77): 64 committed, 13 not committed, 6 diverged, 2 with no result.
  - Build runs (21): 5 with no result.
- **Probe 7: transcripts.** 64 main transcripts and 2,827 subagent transcripts, streamed. Results are aggregates only.
  - `Agent` calls: 126. 55 open with a handoff marker (43.7%); 71 are free text (56.3%).
  - `Workflow` calls: 449. 191 name a shipped harness (42.5%); 258 are inline or other (57.5%).
  - Main-loop Edit/Write on `builds/*/spec/`: 807. 188 of those come after a review or build harness call in the same session (26 sessions).
  - Main-loop writes to `build/` or `reviews/` records: 255.
  - How subagents ended: StructuredOutput 2,588; final text 226; ended on a tool_use with no final turn 11 (0.39%); other 2.

## 4. Gaps

- **HIGH.** Most role exchanges bypass the shipped topology. 258 of 449 Workflow calls are inline scripts and 71 of 126 Agent prompts are free text (probe 7).
- **HIGH.** Fold text is written by the main loop, not a role. 844 of 901 spec fold commits carry no unit trailer (probe 4). A fold after CONVERGED is never re-reviewed (`BUILD-METHOD.md:146-147`).
- **HIGH.** A rendered handoff's task is mostly retyped. 64.5% of its task bytes are `--input` free text (probe 3). The guard admits a self-consistent hand-written file (`agent-cap.js:60-62`).
- **MED.** The roster-to-unit hop is a recipe the main loop re-composes. 6 of 11 harness failures are refusals of hand-composed args (probe 6; `unattended-build.js:2418`).
- **MED.** Divergence has no route back. 6 of 77 unit runs diverged, and `unattended-unit.js:269` leaves the re-dispatch to "the caller".
- **MED.** The researcher, orienter, scout and session roles return prose with no schema (`agents/*.agent.md` `returns` lines). Research records are copies with no hash back to the return.
- **MED.** The session-to-session hop has no enforcer (`workflows.toml` handoff, `enforced-by = "none"`).
- **LOW.** No mailbox exists (absent: probe 5).
- **LOW.** Lost returns are rare: 11 of 2,827 subagents ended with no final turn, and 1 run hit the schema retry cap (probes 6 and 7).

## 5. Candidates

**A. Executor hub.**
- **Mechanism:** a depth-0 executor program (the driver) owns every hop. Each role's return is schema-bound. The executor persists each return as a hashed record, and renders the next item's brief from fields of that record (`input-from=<record>#<field>`), never from typed `--input`. Free text enters only from an owner-sourced record, such as the owner's question.
- **Seam it extends:** `unattended-build.js` `dispatch` (`:2418`), `handoff.py render` and its marker hash, the workflow journals, and the `next` engine already settled.
- **Losing test:** some hop's consumer input is derivable from no producer field and no owner record.
- **Result:** of the 19 `input:` sections, 5 (`spec`) are paths the roster already returns, and 14 (`question`) are owner-originated. No third source was found, so A survives.
- **Second losing test:** the hub must live where a filesystem and the spawn tools are. A Workflow script has no filesystem (`unattended-build.js:19-27`), and sidechains hold neither `Agent` nor `Workflow` (`:1321-1326`). So A loses if placed *inside* a Workflow, and holds only as an external executor.

**B. Blackboard.**
- **Mechanism:** each role writes its output as a record of its class, under `spec/`, `reviews/` or `build/`. The next role's task is derived by `next` from which record classes exist.
- **Seam it extends:** the memory tree's record classes, hygiene check 21 (`Serves:` bindings), and handoff's `brief:` and `card:` sources.
- **Losing test:** every producing role can write its record itself.
- **Result:** it **LOSES**. Only gov-builder, gov-spec-writer and gov-synthesizer hold Write; seven of ten roles cannot post (`agents/*.agent.md` `tools:` lines). The Workflow runtime cannot write either, so a transcriber is needed, and today that transcriber is the main loop (probe 4: 844 commits). The blackboard survives only as A's persistence layer, not as the channel.

**C. Direct role-to-role mailbox.**
- **Mechanism:** a role posts a message to the build's mailbox, and the addressed role consumes it.
- **Seam it extends:** no seam fits (probe 5).
- **Losing test:** a role agent can reach another role, and the message's source can be checked by a key that recomputes.
- **Result:** it **LOSES**. Sidechains hold neither `Agent` nor `Workflow` (`unattended-build.js:1321-1326`). The spawn guard's ceiling names session-to-session messages as passing (`agent-cap.js:61`). A message body is text an agent typed, which fails the settled rule "a source no agent typed". A cross-build or cross-node mailbox (`architecture-v2.md:101`) is a different question and goes to the coordination researcher.

## 6. Pick

I recommend A, the executor hub, with B's record classes as its write-ahead log. A is the only candidate whose losing tests came back with a placement rule rather than a defeat. It extends seams that already enforce something: the `dispatch` recipe, the marker hash and the child's own refusals. The measured failures are hops the main loop re-types or re-composes: 64.5% of rendered task bytes, 6 of 11 harness failures, and 844 fold commits. A removes those by making each hop a field reference the executor resolves. Folds become a gov-spec-writer item, re-reviewed by the next round, instead of main-loop text. Prose-return roles (researcher, orienter, scout) must each gain a return schema; that change belongs to the role-anatomy researcher.
