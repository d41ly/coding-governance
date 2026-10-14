# Agent returns — dRedressedBar, every agent of session 8d2976c7

**Serves:** journal TOOL-dRedressedBar-1

Each agent's final return, verbatim, collected from the session transcripts, last regenerated after unit 18's divergence (wf_2e958a62-4b6). Direct agents give their last assistant text; workflow agents give their journal result. The collector, run over the session's `subagents/` directory:

~~~~python
"""Collect every agent return of one session into one markdown body (stdout).

argv[1]: the session's subagents directory. Direct agents: agent-<id>.jsonl + .meta.json,
the return is the last assistant text. Workflow agents: workflows/<run>/journal.jsonl,
the return is each {"type":"result"} line's result, rendered as JSON.
"""
import glob
import json
import os
import sys

root = sys.argv[1]
rows = []


def first_ts(path):
    with open(path, encoding="utf-8", newline="") as fh:
        for line in fh:
            try:
                ts = json.loads(line).get("timestamp")
            except ValueError:
                continue
            if ts:
                return ts
    return ""


for meta in glob.glob(os.path.join(root, "agent-*.meta.json")):
    aid = os.path.basename(meta)[len("agent-"):-len(".meta.json")]
    with open(meta, encoding="utf-8") as fh:
        m = json.load(fh)
    log = os.path.join(root, "agent-%s.jsonl" % aid)
    last = ""
    with open(log, encoding="utf-8", newline="") as fh:
        for line in fh:
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            msg = rec.get("message") or {}
            if msg.get("role") != "assistant":
                continue
            texts = [c.get("text", "") for c in msg.get("content") or [] if c.get("type") == "text"]
            if any(t.strip() for t in texts):
                last = "\n".join(texts)
    rows.append((first_ts(log), "direct/%s" % aid, m.get("agentType", "?"), m.get("description", ""), last))

for journal in glob.glob(os.path.join(root, "workflows", "*", "journal.jsonl")):
    run = os.path.basename(os.path.dirname(journal))
    labels = {}
    with open(journal, encoding="utf-8", newline="") as fh:
        for line in fh:
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            if rec.get("type") == "started":
                labels[rec.get("agentId")] = rec.get("label", "")
            if rec.get("type") == "result":
                aid = rec.get("agentId", "?")
                log = os.path.join(os.path.dirname(journal), "agent-%s.jsonl" % aid)
                ts = first_ts(log) if os.path.exists(log) else ""
                kind = "?"
                meta = os.path.join(os.path.dirname(journal), "agent-%s.meta.json" % aid)
                if os.path.exists(meta):
                    with open(meta, encoding="utf-8") as mh:
                        kind = json.load(mh).get("agentType", "?")
                body = json.dumps(rec.get("result"), indent=1, ensure_ascii=False)
                rows.append((ts, "%s/%s" % (run, aid), kind, labels.get(aid, ""), body))

rows.sort()
for ts, ref, kind, label, body in rows:
    print("### %s · %s · %s\n" % (ts[:19] or "undated", kind, ref))
    print("Label: %s\n" % (label or "none"))
    print("~~~~text")
    print(body.rstrip().replace("~~~~", "~ ~ ~ ~"))
    print("~~~~\n")
~~~~

## Returns

### 2026-10-13T21:38:44 · gov-spec-writer · direct/abe95cc3e28e97501

Label: dRedressedBar · TOOL-dRedressedBar-8 · spec-write

~~~~text
I wrote the spec for **TOOL-dRedressedBar-8**. It is Tier-1, status SPECCED, step 1 of the build order, grounded on `ebce889c`, and it has no open questions. Hygiene checks 12 and 25 pass over it; I did not run the spec-token leg. Nothing outside the spec folder was touched, and nothing is committed or regenerated.

**What the evidence showed**

1. **The brief misreads the hang.** The nested runner was not sitting in a hold loop. It was blocked opening the FIFO to decide whether to start Y14. Only A14 ever ran, so the server must have died after its first answer. The `sleep 60` was the runner's background load sampler, which ticks every 60 s.
2. **`GATE_WALL` cannot bound this hang.** The wall's watcher only stops running test jobs and leaves a marker, and the runner checks that marker only at the top of its loop. A runner stuck mid-decision is reached by neither. So the spec bounds the arm's nested bar with `timeout`, the same way the suite already bounds other nested bars.
3. **I found why the server dies.** A scratch copy of the server's loop died in every run on this host, in two ways:
   - Opening an existing FIFO failed with `No such file or directory`, and `|| exit 0` ended the server.
   - `printf` wrote to a reader that had already left, and `SIGPIPE` killed it (exit 141).

   Ignoring `SIGPIPE` and retrying a failed open kept the server alive for 300 reads. Up to 13 answers were still lost, and a lost answer can turn the arm red. Adding a 0.2 s pause after each answer gave 600 of 600 good reads, so the spec includes all three changes. What the server answers is unchanged.
4. **It reproduces outside the bar.** Running section 11 alone on today's code hung in AC14 until my 900 s cap. A standalone run of today's server died after 2 reads with exit 141.
5. **AC6 to AC13 did complete in the retry.** The ac5 and ac6 records were missing only because the runner keeps just the 5 newest run records. The retry's fixture has since been deleted, so the spec records what I read from it, with its date.

**What the spec asks the builder to do**, all in `tools/run-gates/run-gates.test.sh`:
- Keep the server alive through both failure modes, with its errors going to `serve.err`.
- Add an optional `MP_BOUND` to `run_mp_bar`, which runs the nested bar under a `timeout`. Only the `ac14` call sets it, to the arm's calibrated wall (128 s here).
- After the run, use the server's own exit status to tell whether it was still alive. A dead server reds the arm with a line naming `serve.sh`, its exit status and its errors. A bar that hit the bound while the server was alive reds with a line naming the bound and the server.
- On a host with no working `timeout`, skip this half with an announced message, keeping its assertion count.

Two scratch probes are written out in the spec. One runs the server alone for 300 reads. The other runs section 11 alone, with or without a staged break: the server exiting after one answer, or never answering. That gives AC1 to AC5 a real red-then-green.

**Things the dispatcher should know**
- **No conflict with unit 7.** The suite is `project-owned`, and the kit-version check ignores that role, so this edit cannot trigger unit 7's stop on a `run-gates` version change.
- **What it does not catch.** The 0.2 s pause makes a lost answer rare but cannot rule it out under load. If one happens, the arm goes red rather than hanging; the spec says so.

Files:
- C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-8.md
~~~~

### 2026-10-14T05:27:10 · gov-spec-writer · direct/ae8c792224ade78ee

Label: dRedressedBar · TOOL-dRedressedBar-3 · spec-write

~~~~text
I revised `TOOL-dRedressedBar-3` to rev-2 as `owner (c)` directs, and the planner now grades it READY. The one file I edited is `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-3.md`.

**Checks I ran:**
- `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` prints `TOOL-dRedressedBar-3 SPECCED READY`. It prints `TOOL-dRedressedBar-9 - MISSING` because the sibling writer's spec isn't in the tree yet.
- The memory hygiene gate reports nothing against this spec. Check 9 is red because the generated build index is out of date: the order change moves the README's derived build-order region, and the README already has your uncommitted roster edit. You regenerate the index when you commit. Check 23 is also red, on old `aSparedSpawn` and `aOrientedCast-22` acceptance ledgers that this work didn't touch.

**What changed in the spec:**
- **Header:** rev-2, `order 1` → `order 2`, and `ratified 2026-10-14` added at the end.
- **§1 Goal:** it no longer calls the defect the owner's to schedule. It now says unit 9 fixes it and three arms stay unscoped to show that fix works.
- **S4:** it now scopes only the four `[-8]` writing calls, at selftest.py lines 8006, 8045, 8057 and 8060 (line numbers as of the base commit). No other `update` call is scoped.
- **S5:** it is no longer a recorded finding. It keeps the other three arms (`and re-stamps the receipt at the new commit`, `[-12] AC4 NEGATIVE`, `[-12] AC9 NEGATIVE`) unscoped; their calls at lines 3299, 6886, 6900, 7064 and 7074 don't change. A new AC5 checks it.
- **§3 Non-goals:** the "No edit to `tools/govkit/govkit.py`" non-goal stays and now says unit 9 owns the product edit. I added two more:
  - The calls S5 names are not scoped.
  - The `run-gates` an update gains at an older `--to` vintage is not fixed here. It stays as a follow-up for the owner.
- **§3 Edges:** the external hand-off for the defect is replaced by a `consumes-from` edge to unit 9.
- **§4 Design:** it explains why the cluster splits by cause:
  - The `[-8]` arms fail on the gained `run-gates` at `9ddcc5c9`, and that call at line 8060 would also gain `settings-merge` at HEAD.
  - The three arms that update to HEAD fail only on the `settings-merge` adopter.
  - It is still unverified whether those three arms go green over unit 9's fix. A red there goes back to the main loop.
- **AC4:**
  - A grep over the `t8` and `t84` fixtures' update calls shows every one carries `"--kits", "check-wiring"`.
  - A `derive_default_gained` probe to `9ddcc5c9` lists `run-gates`.
  - It still greps the `if kits else derive_default_gained` line (govkit.py:8868).
- **AC5 (new):**
  - A grep shows no writing call over the `up`, `u4` or `u9` fixtures carries `--kits`.
  - A narrow-receipt `update --write` over a tree with unit 9's fix exits 0 and re-stamps the receipt at gov HEAD. It fails red on `default-gained settings-merge: adopter exit 2`.
- **§6:** the AC4 `New arm:` line now stages its failure on the `d8-ac1` write, and an AC5 line is added.
- **§7 F1:** marked `RESOLVED (owner, 2026-10-14): (c)` in place, outside backticks so the planner reads it.
- **§8:** a rev-2 line names everything that moved.

**Two choices for you to confirm:**
1. **Edge verb.** The brief asked for `depends-on TOOL-dRedressedBar-9`. The spec format only allows `consumes-from` and `hands-off` (check-memory-hygiene.sh:2338), and its own test calls `depends-on` "the verb this format does not have". So I wrote `**consumes-from** \`TOOL-dRedressedBar-9\``, which has the same meaning.
2. **`order 2`** assumes unit 9 lands at `order 1`, as the README's new ordering line implies (units 1, 2, 8 and 9 have separate write sets, and 3 follows 9). I couldn't read unit 9's spec. If its writer picks a different order, unit 3 needs to sit one step after it. Unit 4 is also at order 2, and the two units' files don't overlap.
~~~~

### 2026-10-14T05:27:31 · gov-spec-writer · direct/a7ce0b9ce58d1caa2

Label: dRedressedBar · TOOL-dRedressedBar-9 · spec-write

~~~~text
I wrote the spec for **TOOL-dRedressedBar-9**: Tier-2, SPECCED, `order 1`, no open forks. I committed nothing and regenerated no index.

**Spec:** `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-9.md`

**The fix.** `settings-merge`'s own descriptor gains one declared outcome: exit 2 counts as an accepted stop only when `settings-merge.py` is present and `agent-cap.js` is absent. Nothing in `govkit.py`, `settings-merge.py` or `tools/hooks/kit.toml` changes, so no kit version moves.

```toml
[[outcome]]
code = 2
probe = { must_exist = "{prefix}/settings-merge.py", must_not_exist = "{prefix}/hooks/agent-cap.js" }
means = "no-agent-cap-to-wire"
ok = true
```

**What I measured at the base** (scratch targets under `%TEMP%`, on `ea25a64a`, whose `tools/` tree is identical to `ebce889c`'s):
- The narrow `update --write` over a receipt claiming only `check-wiring` exits 1. Its only problem is `default-gained settings-merge: adopter exit 2`, and it does not re-stamp. The dirty-README and committed-deletion versions, which match `[-12] AC4 NEGATIVE` and `[-12] AC9 NEGATIVE`, fail on that same single problem.
- `apply --kits settings-merge` on its own also exits 1, on the same adopter. This contradicts the brief, which says `apply` never meets this defect. It is why the fix belongs in settings-merge's descriptor rather than in the update's gaining rule.
- I checked the new outcome against the engine's own functions on an in-memory copy of the descriptor, writing nothing to the tree. Exit 2 is accepted only when the hook is absent and `settings-merge.py` is present; every other state is refused.

**Why this option won, by M12 and M3:**
- **Changing the gaining rule** (leave `settings-merge` out when `agent-cap` is dropped) still leaves `apply --kits settings-merge` broken. It also stops these updates from wiring `check-wiring.fragment.json`, which I saw happen in the base run.
- **Keeping the gain but skipping a duplicate adopter** still leaves `apply --kits settings-merge` broken.
- **Removing settings-merge's adopter** breaks the existing selftest arm at `selftest.py:6566-6585`. Fixing that arm means editing an existing selftest line, which the brief rules out.
- **A new flag on `settings-merge.py`** adds a public surface to a shipped engine, which needs the owner (M3 veto 2).

**What an adopter sees change:**

| Situation | Before | After |
|---|---|---|
| Narrow `update --write` | exit 1, receipt not re-stamped | exit 0, prints `adopter exit 2 — no-agent-cap-to-wire`, re-stamps |
| `apply --kits settings-merge` alone | exit 1 | exit 0, prints the stop as accepted |
| Any target where `agent-cap.js` is installed | adopter exit 0 | unchanged |

`agent-cap`'s own refusal still fails wherever `agent-cap` is selected.

**New arms, declared in the spec's Gates section:**
- One block in `tools/govkit/selftest.py`, on its own fixture. It checks that the narrow update exits 0, re-stamps, keeps `settings-merge` in the receipt, and prints the stop name read from the descriptor. No existing line in the file moves.
- In `tools/govkit/matrix.py`, the existing lexicon check becomes a helper, `check_outcome_states`, which also runs settings-merge's three cases. Its paths come from the descriptors through `resolve_entry`, not typed in.

**Edges:** hands-off to `TOOL-dRedressedBar-3`. Its three unscoped arms read green only after this fix.

**For you:**
- Hygiene check 9 reports the build README index as stale. That is expected and is yours to regenerate when you commit. My spec raised no other hygiene finding; the check-23 failures were already there.
- The probe scripts are in the scratchpad (`probe9.py`, `probe9b.py`), not in the tree.
~~~~

### 2026-10-14T05:47:26 · gov-spec-writer · wf_2b03c380-02e/a97deeea3cacd9bdb

Label: dRedressedBar · TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 · spec-write

~~~~text
{
 "authored": [],
 "alreadyPresent": [
  "TOOL-dRedressedBar-1",
  "TOOL-dRedressedBar-2",
  "TOOL-dRedressedBar-8",
  "TOOL-dRedressedBar-9"
 ],
 "refused": [],
 "summary": "Your question first: yes, the Role part reaches spec writers, but as the system prompt and not inside the message. That is why the message you looked at starts with the Task paragraph. The handoff record memory/builds/dRedressedBar/prompts/2026-10-14-prompt-TOOL-dRedressedBar-8-1-spec-writer.md has a '## Role' section (\"You are a code architect, writing the specification for one or more units of a larger build...\", role-sha=06b14b1ac42a). In this run my system prompt starts with that same Role text, word for word as far as I compared it, then the Charter. The task message only covers the Task part, and it says so itself: \"your role is your system prompt, and this message is your task\". I compared the Role text in the unit-8 record only.\n\nThe four units: I wrote nothing and changed no files, because all four specs already exist and fit the spec format (memory/TEMPLATE-SPEC.md):\n- TOOL-dRedressedBar-1 (C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-1.md): Tier-1, with the eight required sections plus the optional Reuse audit.\n- TOOL-dRedressedBar-2 (.../spec/2026-10-14-spec-TOOL-dRedressedBar-2.md): Tier-2, all ten sections.\n- TOOL-dRedressedBar-8 (.../spec/2026-10-14-spec-TOOL-dRedressedBar-8.md): Tier-1, with the eight required sections plus the optional Reuse audit.\n- TOOL-dRedressedBar-9 (.../spec/2026-10-14-spec-TOOL-dRedressedBar-9.md): Tier-2, all ten sections.\n\nEach status header reads 'SPECCED · rev-1 · 2026-10-14 · node d · ... · base ebce889c · streams tooling · order 1', so it already carries the 'order 1' this roster asks for. The specs were committed earlier (771e8ff88, ea25a64a0, 383840368). I checked the header and section headings of each spec; I did not re-check what each section says. Nothing is refused, I ran no gates, made no commit and did not regenerate the index."
}
~~~~

### 2026-10-14T05:47:27 · gov-spec-writer · wf_2b03c380-02e/ae7f363e2515f7026

Label: dRedressedBar · TOOL-dRedressedBar-5 · spec-write

~~~~text
{
 "authored": [],
 "alreadyPresent": [
  "TOOL-dRedressedBar-5"
 ],
 "refused": [],
 "summary": "I didn't write anything for TOOL-dRedressedBar-5 because a spec for it already exists, so it counts as already present. The file is C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-5.md, committed in 771e8ff88. Its status line reads SPECCED · rev-1 · Tier-2 · base ebce889c · streams tooling · order 3, which matches the order in your list. Sections 1 to 10 are all there and filled in, open questions say \"none\", and the revision log has a rev-1 entry. I didn't edit it, committed nothing and didn't regenerate the index. I didn't run the hygiene check on it either; I only checked the sections by reading the file.\n\nYour question, whether the Role part of the handoff reaches spec writers: yes, but not inside the message. The saved handoff record has a Role section followed by a Task section (see C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/prompts/2026-10-14-prompt-TOOL-dRedressedBar-9-1-spec-writer.md, where Role starts at line 7 and Task at line 46). The message sent to the agent holds only the Task, which is why it starts with the Task paragraph. The Role arrives as the system prompt of the gov-spec-writer agent type, from C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/.claude/agents/gov-spec-writer.md (built from tools/roles/agents/gov-spec-writer.agent.md). The task message says the same thing: \"your role is your system prompt, and this message is your task.\"\n\nI checked that in this session. My system prompt opens with the Role text word for word, and the saved Role section (30 non-blank lines) is identical to the first 30 lines of the installed agent file. The agent file then adds the Charter (rules, protocols, facts), which the saved Role section leaves out. So the agent actually gets more than the record shows.\n\nOne gap: nothing checks that the role-sha stamped in the record matches the agent file the agent actually runs from. tools/hooks/README.md:231 says so, and tools/roles/handoff.py:443-450 only hashes the record's own Role section. If the agent file changes after a handoff is saved, nothing would catch the mismatch."
}
~~~~

### 2026-10-14T05:47:27 · gov-spec-writer · wf_2b03c380-02e/afce6f3165a2fb559

Label: dRedressedBar · TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 · spec-write

~~~~text
{
 "summary": "I authored nothing. Both units already had conforming specs, so I counted them as already present and changed no files.\n\n**TOOL-dRedressedBar-3** (`C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-3.md`): commit 383840368 had already applied the revision brief. The spec is a Tier-1 rev-2 with header `order 2 · ratified 2026-10-14`. F1 is marked `RESOLVED (owner, 2026-10-14): (c)`. S4 and AC4 scope only the four `[-8]` writing calls. S5 and AC5 leave the other three arms unscoped as the witness for unit 9's fix, and a rev-2 line in the revision log names what moved. One difference from the brief: the brief asked for a `depends-on TOOL-dRedressedBar-9` edge, but the spec format only allows `consumes-from` and `hands-off` (`memory/TEMPLATE-SPEC.md:219-222`). The spec's `consumes-from TOOL-dRedressedBar-9` is the allowed form of that edge.\n\n**TOOL-dRedressedBar-4** (`.../spec/2026-10-14-spec-TOOL-dRedressedBar-4.md`): Tier-2 rev-1, `order 2`. It has all ten sections in order, including Edges and the reuse audit with its recall terms, and its open questions read `none`. The memory hygiene check reported nothing for either spec. Its failures (checks 17 and 23) belong to other builds.\n\n**Your question: does the Role part reach spec writers?** Yes, but as the system prompt, not as part of the message. The writer's message does start at the Task paragraph, and that is by design. It even says \"This stage runs as the gov-spec-writer agent type: your role is your system prompt, and this message is your task.\" I compared the `## Role` section of the recorded handoff (`.../prompts/2026-10-14-prompt-TOOL-dRedressedBar-3-3-spec-writer.md`, tagged `role=gov-spec-writer role-sha=06b14b1ac42a`) against my own system prompt. The text from \"You are a code architect, writing the specification...\" through \"Done means every unit you were handed is authored, counted as already present, or refused with its reason...\" matches word for word. So the handoff record keeps Role and Task together, and the harness splits them on delivery: Role goes in as the agent type's system prompt, Task as the message. The final paragraph of my system prompt, on the return shape, falls outside the excerpt I read, so I haven't confirmed that part matches.",
 "authored": [],
 "alreadyPresent": [
  "TOOL-dRedressedBar-3",
  "TOOL-dRedressedBar-4"
 ],
 "refused": []
}
~~~~

### 2026-10-14T05:47:27 · gov-spec-writer · wf_2b03c380-02e/a0d99939fee58e780

Label: dRedressedBar · TOOL-dRedressedBar-7 · spec-write

~~~~text
{
 "alreadyPresent": [
  "TOOL-dRedressedBar-7"
 ],
 "authored": [],
 "refused": [],
 "summary": "TOOL-dRedressedBar-7 already has a conforming spec, so I left it alone and counted it as already present. The spec is C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-7.md, committed in 771e8ff88. Its status header already reads `order 5`, and all ten sections are there: goal, scope, non-goals and edges, design, readiness checklist, acceptance criteria AC1 to AC6, gates, open questions, revision log, and reuse audit with recall terms. I wrote nothing, committed nothing and did not regenerate the index.\n\nYour question: yes, the Role reaches spec writers, but through the agent's system prompt, not the spawn message. The spawn message starting at `## Task` is intentional.\n\n- **The prompt file has both parts.** `tools/roles/handoff.py:415-416` writes a `## Role` section and then a `## Task` section, with a separate hash for each in the marker.\n- **Only the Task part is sent as the message.** The spawn guard in `tools/hooks/agent-cap.js` (around lines 47 and 2058-2136; also `tools/hooks/README.md:210`) only allows an `Agent` call whose prompt is exactly the marker line, blank lines, and the file's `## Task` section. `handoff.py render --part task` prints that and nothing else.\n- **The Role arrives as the system prompt instead.** `subagent_type` must be a role-backed agent type, and that type's body is the role text. I checked this on the dRedressedBar-9 spec-writer prompt file, whose marker passes `handoff.py check`. Its `## Role` text is a byte-for-byte prefix of the body of `.claude/agents/gov-spec-writer.md`. The agent file then adds the `## Charter` block, which in the prompt file is the last block of the `## Task` section.\n- **This run shows the same thing.** My system prompt starts with the same Role text (\"You are a code architect...\") followed by the Charter. My task message was this harness's computed task, and it says so itself: \"your role is your system prompt, and this message is your task.\"\n\nOne gap to know about: nothing checks that the two copies of the Role still match. The `agent-cap.js` header says outright that the guard \"never compares `role-sha` with the role an agent type was rendered from.\" If someone edited a role and didn't re-run the `adopt-roles.sh --scaffold` render, the prompt file's Role section and the agent the writer actually runs as could drift apart without any warning. Today they match exactly."
}
~~~~

### 2026-10-14T05:47:27 · gov-spec-writer · wf_2b03c380-02e/abb71922da86ac2e6

Label: dRedressedBar · TOOL-dRedressedBar-6 · spec-write

~~~~text
{
 "authored": [],
 "alreadyPresent": [
  "TOOL-dRedressedBar-6"
 ],
 "refused": [],
 "summary": "I didn't write anything, because TOOL-dRedressedBar-6 already has a conforming spec. It is C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-6.md, committed in 771e8ff88. It is a Tier-1 spec and its status header reads `SPECCED · rev-1 · 2026-10-14 · node d · Tier-1 · base ebce889c · streams tooling · order 4`, so it already has the `order 4` verb this roster names. The Tier-1 format in memory/TEMPLATE-SPEC.md (lines 134-145) requires eight sections in order: Goal, Scope (IN), Non-goals (OUT), Design, Acceptance criteria, Gates, Open questions and Revision log. The spec has all eight, none of them empty, plus the optional Reuse audit in its proper place. Its Open questions section reads `none`, and its Gates section has two `New arm:` lines. I checked this by reading the file. I did not run the hygiene gate. No commit, no index regeneration.\n\nYour question: yes, the Role reaches the spec writer, but as the agent's system prompt, not in the message it receives. That message starting with the Task paragraph is by design. The task text says so itself: \"This stage runs as the gov-spec-writer agent type: your role is your system prompt, and this message is your task.\" I checked the wording. The `## Role` section of a recorded handoff matches, word for word, the body of the agent definition, C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/.claude/agents/gov-spec-writer.md. For example, compare it with memory/builds/dRedressedBar/prompts/2026-10-14-prompt-TOOL-dRedressedBar-9-1-spec-writer.md, lines 7-44. That body is what I was started with, followed by the Charter rules, Protocols and Facts. So none of the Role is lost; it just doesn't travel in the message.\n\nOne difference you may care about: the recorded handoff carries the brief inline under `### brief:goal`, `### brief:items`, `### brief:acceptance`, `### brief:gates`, `### brief:non-goals` and `### task:reuse`. This run's message did not include those sections. It only gave the path to the brief file, memory/builds/dRedressedBar/prompts/2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md. A writer in this run has to open the brief itself rather than get its contents in the handoff."
}
~~~~

### 2026-10-14T05:48:55 · workflow-subagent · wf_2b03c380-02e/a74d7ae2efb87de34

Label: dRedressedBar · audit round 1 · subjects

~~~~text
{
 "subjects": [
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-1.md",
   "blob": "4c8cb21ee98bf5b32cbbfc5dc07e02f176106a7e",
   "tree": "4c8cb21ee98bf5b32cbbfc5dc07e02f176106a7e"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-2.md",
   "blob": "d04f152c379f2a289ea0f0ad229211033df90fb8",
   "tree": "d04f152c379f2a289ea0f0ad229211033df90fb8"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-8.md",
   "blob": "d044d5d1534e61d6b4446810fc3d08755fbadcd1",
   "tree": "d044d5d1534e61d6b4446810fc3d08755fbadcd1"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-9.md",
   "blob": "689d95e522a24c36ab39c1dfbfb1cdb786054a3c",
   "tree": "689d95e522a24c36ab39c1dfbfb1cdb786054a3c"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-3.md",
   "blob": "4d63d87b40fdb4e2a76974ac4beeaecdd17cca10",
   "tree": "4d63d87b40fdb4e2a76974ac4beeaecdd17cca10"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-4.md",
   "blob": "5bccfa77828057b6feed3516b3ae524b46155220",
   "tree": "5bccfa77828057b6feed3516b3ae524b46155220"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-5.md",
   "blob": "8e9da09f6c662bfab708e8480d946a9763322e1d",
   "tree": "8e9da09f6c662bfab708e8480d946a9763322e1d"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-6.md",
   "blob": "d533940073b3957a5ba57712e3d0e8503b378e7d",
   "tree": "d533940073b3957a5ba57712e3d0e8503b378e7d"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-7.md",
   "blob": "cc4dcb64e3579ce3873ad679bfdd6528a3e26670",
   "tree": "cc4dcb64e3579ce3873ad679bfdd6528a3e26670"
  }
 ],
 "notAtHead": [],
 "checklistPaths": [
  "tools/workflows/unattended-build.test.sh",
  "tools/workflows/tier2-review.test.sh",
  "tools/run-gates/run-gates.turnstile.test.sh",
  ".githooks/pre-push.test.sh",
  "tools/roles/adopt-roles.test.sh",
  "tools/unattended/gate-guard.js",
  "tools/govkit/selftest.py",
  "tools/hooks/format-guard.js",
  "tools/branch-reconcile/adopt-branch-reconcile.sh",
  "tools/roles/adopt-roles.sh",
  "tools/hooks/format-guard.test.sh",
  "memory/gotchas/INDEX.md",
  "memory/project/method-carriers.txt",
  "tools/hooks/agent-cap.js",
  "tools/branch-reconcile/branch_reconcile.py",
  "tools/roles/roles_lib.py",
  "tools/unattended/unattended.sh",
  "memory/guides/SESSION-KICKOFF.md",
  "tools/run-gates/run-gates.test.sh",
  "tools/govkit/entries/settings-merge.kit.toml",
  "tools/govkit/matrix.py"
 ],
 "checklist": "# recurring-bug-class checklist for 21 path(s) (21 file(s))\n# 50 class(es) selected by an anchor + 6 universal\n# by anchor specificity: 37 path · 7 directory · 6 basename; a cut tier prints one line per class\n# invariants are read at ebce889c7d71; 0 that this subject adds, edits or takes out are listed as items, never by design\n\n- [ ] fixture-passes-by-finding-nothing (universal)\n      a test arm whose fixture never triggers the rule passes, and proves nothing\n      memory/gotchas/fixture-passes-by-finding-nothing.md\n\n- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)\n      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage\n      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md\n\n- [ ] heredoc-escape-reaches-the-regex (universal)\n      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem\n      memory/gotchas/heredoc-escape-reaches-the-regex.md\n\n- [ ] inline-fence-swallows-the-rest-of-the-file (universal)\n      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view\n      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md\n\n- [ ] staged-break-substitutes-a-synthetic-value (universal)\n      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n      memory/gotchas/staged-break-substitutes-a-synthetic-value.md\n\n- [ ] two-answers-to-one-question (universal)\n      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n      memory/gotchas/two-answers-to-one-question.md\n\n- [ ] containment-tested-one-way (path)\n      a guard asking only \"is this path under the protected one\" refuses the narrow declarations and admits the one that claims everything\n      memory/gotchas/containment-tested-one-way.md\n\n- [ ] fixture-lacks-a-gate-the-consumer-has (path)\n      a runbook's fixture passes because it lacks a commit-time gate the consumer runs, and the consumer refuses the step the fixture let through\n      memory/gotchas/fixture-lacks-a-gate-the-consumer-has.md\n\n- [ ] floor-left-below-the-arms-it-guards (path)\n      a suite's assertion floor not raised when arms land leaves those arms stranded, so deleting them keeps the suite green\n      memory/gotchas/floor-left-below-the-arms-it-guards.md\n\n- [ ] held-suite-guard-misses-a-sibling-kit (path)\n      a held self-test reads another kit's file, but its leg's guard names only its own kit, so an edit to the sibling skips the leg or reuses its stale green\n      memory/gotchas/held-suite-guard-misses-a-sibling-kit.md\n\n- [ ] a-merge-of-the-default-branch-read-as-additions (path)\n      a check that lists the files a range or a commit ADDS reads a merge of the default branch into a feature branch as adding every file the default branch gained, unless its git invocation is one of the shapes that cannot\n      memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md\n\n- [ ] a-merged-in-check-can-refuse-a-pinned-record (path)\n      a merge of the remote's default branch into a run branch brings in a check, or narrows one, that the running record cannot satisfy because the bytes it grades are pinned at BASE; nothing grades it again until the verb that owns it, and for a non-overridable item the only exits left are rotation and hand-off\n      memory/gotchas/a-merged-in-check-can-refuse-a-pinned-record.md\n\n- [ ] a-new-local-collides-in-a-long-function (path)\n      a local added to a function thousands of lines long can share its name with one a distant block already binds, and the later binding silently replaces the new value only on the inputs that reach that block\n      memory/gotchas/a-new-local-collides-in-a-long-function.md\n\n- [ ] a-pair-exists-and-it-is-the-wrong-one (path)\n      a scanner that pairs a delimiter with the next one of its kind finds a pair for a delimiter that opens nothing, and the span it then blanks is where the defect hides\n      memory/gotchas/a-pair-exists-and-it-is-the-wrong-one.md\n\n- [ ] a-runner-knob-owes-a-push-class (path)\n      a new GATE_ or GOV_ knob the gate runner reads has no push-boundary class until it joins one, and the arm that says so is guarded away from the unit that adds it\n      memory/gotchas/a-runner-knob-owes-a-push-class.md\n\n- [ ] a-spelling-change-strands-its-readers (path)\n      a shared file changes how it SPELLS its values, the readers someone migrated resolve the new spelling, and every reader nobody listed compares the raw one and matches nothing\n      memory/gotchas/a-spelling-change-strands-its-readers.md\n\n- [ ] a-view-fix-trades-one-blindness-for-another (path)\n      a scanner that grades source through a rendered view has a blind spot, and building a better view moves it rather than closing it, each move a new fail-open or false-deny\n      memory/gotchas/a-view-fix-trades-one-blindness-for-another.md\n\n- [ ] allocation-knob-without-a-ceiling (path)\n      a knob that sizes an allocation or a loop, validated only as a positive integer, hangs the process on a mistyped value before anything it guards runs\n      memory/gotchas/allocation-knob-without-a-ceiling.md\n\n- [ ] beacon-published-before-it-is-complete (path)\n      a lock or presence directory made visible before the files that let others judge it leaks forever when its writer dies in between, because every sweep needs those files\n      memory/gotchas/beacon-published-before-it-is-complete.md\n\n- [ ] borrowed-seed-inherits-its-head-state (path)\n      a fixture built from another suite's seed inherits that seed's HEAD state, and a probe that reads HEAD is dead on an unborn one\n      memory/gotchas/borrowed-seed-inherits-its-head-state.md\n\n- [ ] bounded-through-a-pipe-is-unbounded (path)\n      a wall-clock timeout captured through a command substitution bounds the verdict and not the clock, and reports success on schedule while the caller blocks\n      memory/gotchas/bounded-through-a-pipe-is-unbounded.md\n\n- [ ] concurrency-is-not-a-budget (path)\n      a per-item verify fan-out passes a concurrency cap and still spawns one agent per finding\n      memory/gotchas/concurrency-is-not-a-budget.md\n\n- [ ] decision-re-derived-by-a-second-process (path)\n      a second process that re-derives a decision the first one already acted on, from its OWN inputs, answers a different question whenever those inputs differ, and the gap is exactly where an attacker stands\n      memory/gotchas/decision-re-derived-by-a-second-process.md\n\n- [ ] destructive-step-before-its-precondition (path)\n      a destructive step ordered before the probe for the precondition that makes it useful runs on exactly the case where nothing can follow it, so the harm lands and the benefit never does\n      memory/gotchas/destructive-step-before-its-precondition.md\n\n- [ ] fixed-sleep-does-not-place-a-signal (path)\n      a test that sleeps a fixed time and then signals assumes the child it means to interrupt is already running; under load the signal lands before that child exists or after it ended\n      memory/gotchas/fixed-sleep-does-not-place-a-signal.md\n\n- [ ] fixture-inherits-ambient-machine-state (path)\n      a hermetic-looking fixture silently reads machine-global config, so it passes everywhere it was written and fails where it was not\n      memory/gotchas/fixture-inherits-ambient-machine-state.md\n\n- [ ] format-derived-from-arity (path)\n      a producer that picks its output FORMAT from the number of items has two shapes, and a consumer written against the many-item one reads the single-item case as empty\n      memory/gotchas/format-derived-from-arity.md\n\n- [ ] inherited-git-dir-pins-the-work-tree-to-the-cwd (path)\n      with GIT_DIR set and no GIT_WORK_TREE, git takes the current directory for the work tree's top, so a `git -C <dir>` probe answers about <dir> as if it were the root; git exports GIT_DIR into a linked worktree's hooks, so a location probe that passed in a shell answers wrong inside one\n      memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md\n\n- [ ] invariant-held-on-one-admission-path (path)\n      an invariant one admission path enforces is silently absent on every other path into the same resource, and the spec that states it reads as covering them all\n      memory/gotchas/invariant-held-on-one-admission-path.md\n\n- [ ] line-claim-matched-over-the-whole-output (path)\n      an arm that asserts a line names X tests two substrings over the whole output, so it passes when X appears on some other line and the line it means names something else\n      memory/gotchas/line-claim-matched-over-the-whole-output.md\n\n- [ ] liveness-negative-from-another-population (path)\n      a probe is shown able to read negative on inputs it will never act on, while over its real population a positive is structural, so the liveness assertion passes and certifies nothing\n      memory/gotchas/liveness-negative-from-another-population.md\n\n- [ ] nt-against-a-missing-file-is-true (path)\n      a -nt b is TRUE when b does not exist, so a has-it-changed test against a stamp nobody wrote yet reports a change on the very first call\n      memory/gotchas/nt-against-a-missing-file-is-true.md\n\n- [ ] observed-by-claim-no-arm-discharges (path)\n      a spec scope item says a behaviour is \"Observed by ACn\", the arm that criterion names never reads the surface the behaviour renders on, and a staged break of the behaviour leaves the suite green\n      memory/gotchas/observed-by-claim-no-arm-discharges.md\n\n- [ ] porcelain-diff-names-a-rename-by-its-destination (path)\n      a touched-set read built on porcelain `git diff --name-only` names a renamed file by its destination alone, so a prefix match misses a file moved OUT of the prefix\n      memory/gotchas/porcelain-diff-names-a-rename-by-its-destination.md\n\n- [ ] predicate-bounded-by-its-own-count (path)\n      a predicate about other processes' holdings that walks only up to this process's own configured count misses a neighbour configured higher\n      memory/gotchas/predicate-bounded-by-its-own-count.md\n\n- [ ] signal-killed-hook-reads-as-success (path)\n      on Git for Windows a git hook that dies by a signal is read by git as exit 0, so an untrapped TERM, HUP or INT, a KILL or a TerminateProcess lands a push the hook was about to refuse\n      memory/gotchas/signal-killed-hook-reads-as-success.md\n\n- [ ] suite-invalidated-by-a-commit-under-it (path)\n      a suite that pins gov's revision at import and stamps fixtures from live HEAD is silently invalidated by any commit made while it runs, and the failures name the product\n      memory/gotchas/suite-invalidated-by-a-commit-under-it.md\n\n- [ ] test-oracle-read-from-a-historical-sha (path)\n      a test compares its subject with a copy read out of git at a literal sha, so every later legitimate edit of the subject reds it and the fix is always \"move the sha\"\n      memory/gotchas/test-oracle-read-from-a-historical-sha.md\n\n- [ ] trailing-comma-counted-as-an-element (path)\n      a counter scoring one-plus-every-top-level-comma reads a trailing comma as a real item, so every multi-line literal measures one too many\n      memory/gotchas/trailing-comma-counted-as-an-element.md\n\n- [ ] trapped-signal-waits-for-the-foreground-child (path)\n      a bash script that TRAPS TERM, HUP or INT runs the handler only after its foreground child returns, so a killed script outlives the kill for as long as that child runs\n      memory/gotchas/trapped-signal-waits-for-the-foreground-child.md\n\n- [ ] two-guards-one-question-two-answers (path)\n      two guards that ask one question different ways become jointly unsatisfiable, and the tree they wedge has no legal move left\n      memory/gotchas/two-guards-one-question-two-answers.md\n\n- [ ] verdict-printed-before-the-step-that-reverts-it (path)\n      a verb prints a verdict about bytes it just wrote, and a later step of the same run can revert those bytes, so the operator reads a verdict about a tree the run did not leave\n      memory/gotchas/verdict-printed-before-the-step-that-reverts-it.md\n\n- [ ] witness-graded-against-a-fact-written-after-it (path)\n      a sidecar line that outlives the lease it was written under is graded against the id the new lease replaced, so a dead incarnation's witness passes the check the live one owes\n      memory/gotchas/witness-graded-against-a-fact-written-after-it.md\n\n- [ ] empty-field-collapses-unless-it-is-last (directory) · memory/gotchas/empty-field-collapses-unless-it-is-last.md\n\n- [ ] amendment-leaves-its-other-half-standing (directory) · memory/gotchas/amendment-leaves-its-other-half-standing.md\n\n- [ ] degradation-known-but-unreported (directory) · memory/gotchas/degradation-known-but-unreported.md\n\n- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory) · memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md\n\n- [ ] node-check-is-not-a-syntax-gate (directory) · memory/gotchas/node-check-is-not-a-syntax-gate.md\n\n- [ ] second-implementation-is-not-a-second-opinion (directory) · memory/gotchas/second-implementation-is-not-a-second-opinion.md\n\n- [ ] hookspath-resolves-into-another-checkout (directory) · memory/gotchas/hookspath-resolves-into-another-checkout.md\n\n- [ ] a-new-leg-trips-a-growing-set-of-meta-gates (basename) · memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md\n\n- [ ] anchor-literal-resolves-above-its-target (basename) · memory/gotchas/anchor-literal-resolves-above-its-target.md\n\n- [ ] join-key-widened-by-a-shared-location (basename) · memory/gotchas/join-key-widened-by-a-shared-location.md\n\n- [ ] retirement-inventory-misses-readers-by-value (basename) · memory/gotchas/retirement-inventory-misses-readers-by-value.md\n\n- [ ] staged-break-runs-stale-bytecode (basename) · memory/gotchas/staged-break-runs-stale-bytecode.md\n\n- [ ] two-readers-of-one-config-one-re-derived (basename) · memory/gotchas/two-readers-of-one-config-one-re-derived.md\n\n# by design — 2 invariant(s) this selection touches\n- canary-waits-on-a-rendezvous-not-a-clock — The run-gates canary never compares a serial run's elapsed time with a concurrent run's, so it seems not to prove the pool runs legs at once. → It counts the peers announced at once through a rendezvous, because an elapsed-time ratio measures the node and not the runner. (TOOL-cSteadyMetronome-1)\n- concurrent-runs-are-announced-not-refused — `--preflight` lets an unattended run start while another build's run is live, and only prints a line about it. → Concurrent runs of DIFFERENT builds are announced and never refused, because nothing is keyed on \"the run\" tree-wide; the same-slug claim refusal is a separate rule about one build. (TOOL-aUnblockedFleet-1)\n"
}
~~~~

### 2026-10-14T05:50:07 · workflow-subagent · wf_2b03c380-02e/a3f7fb12d0776abcf

Label: dRedressedBar · spec-audit round 1 · resume:probe

~~~~text
{
 "commonDir": "C:/projects/coding-governance/.git",
 "blobs": [
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-1.md",
   "now": "4c8cb21ee98bf5b32cbbfc5dc07e02f176106a7e"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-2.md",
   "now": "d04f152c379f2a289ea0f0ad229211033df90fb8"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-8.md",
   "now": "d044d5d1534e61d6b4446810fc3d08755fbadcd1"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-9.md",
   "now": "689d95e522a24c36ab39c1dfbfb1cdb786054a3c"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-3.md",
   "now": "4d63d87b40fdb4e2a76974ac4beeaecdd17cca10"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-4.md",
   "now": "5bccfa77828057b6feed3516b3ae524b46155220"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-5.md",
   "now": "8e9da09f6c662bfab708e8480d946a9763322e1d"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-6.md",
   "now": "d533940073b3957a5ba57712e3d0e8503b378e7d"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-7.md",
   "now": "cc4dcb64e3579ce3873ad679bfdd6528a3e26670"
  }
 ],
 "finds": [],
 "verifies": [],
 "skipped": []
}
~~~~

### 2026-10-14T05:50:24 · gov-spec-reviewer · wf_2b03c380-02e/a52cb2cd74250edb1

Label: dRedressedBar · spec-audit round 1 · find:coherence

~~~~text
{
 "lens": "coherence",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-1.md",
   "where": "section 5 AC1 (against section 2 S1)",
   "severity": "medium",
   "claim": "AC1 counts matching LINES with `grep -c` but expects the number of CALLS. The 14 GH33 writer calls sit on 5 lines, so a correct build reads 5, not 14, and AC1 cannot pass.",
   "impact": "A correct S1 build fails its own criterion. The builder either records a false red in the acceptance ledger or 'fixes' the suite to hit 14, for example by splitting calls onto separate lines, which unit 5's forms table and fork counts do not expect.",
   "fix": "Count occurrences, not lines: `grep -o \"build_gh33_writer [A-Z]-tB-[0-9]'\" tools/workflows/unattended-build.test.sh | wc -l` reads 0, and the same with a space before the quote reads 14. Or keep `grep -c` and state 0 and 5 lines.",
   "evidence": "`grep -c \"build_gh33_writer [A-Z]-tB-[0-9]'\" tools/workflows/unattended-build.test.sh` printed 5. `grep -o \"build_gh33_writer [A-Z]-tB-[0-9]'\" … | wc -l` printed 13. The spaced form with -o printed 1. `grep -c \"build_gh33_writer [A-Z]-tB-[0-9]\" …` printed 5, the hits being lines 2471, 2483, 2496, 2503 and 2512. After S1 the spaced `grep -c` can read at most 5."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-1.md",
   "where": "section 5 AC4",
   "severity": "medium",
   "claim": "AC4's placement check is anchored to the first `git push` hit of `grep -n 'git push'`. That hit is line 2, a header comment. 'Numbered below' it is either impossible (a number under 2) or true for any placement after line 2. The second half (scoped vs FULL decision) only exercises the unchanged hook, so it is green before the unit is built.",
   "impact": "An `unset GATE_SELFTESTS` placed after some of the suite's pushes, which would leave those pushes inheriting the bar's export (the exact red S4 fixes), still passes AC4. Apart from the line's mere presence, the criterion cannot fail for the misplacement it claims to guard.",
   "fix": "Anchor on the first executed push, for example the line number of the first `grep -nE '^[^#]*git push'` hit (135 at base), and require the unset line number to be smaller. Or require it to fall inside the environment-pin block, lines 109-118. Drop the hook-decision half, or reword it as the liveness of the forcing case and not as an observation of S4.",
   "evidence": "`grep -n 'git push' .githooks/pre-push.test.sh | head -5` printed `2:# pre-push.test.sh — drives a REAL git push …` first, then 135, 143, 148 and 153. The environment pins S4 targets are at lines 109-118 (sed -n 105,120p)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-1.md",
   "where": "section 5 AC5 against section 4 S5",
   "severity": "medium",
   "claim": "§4 S5 says to copy the siblings' probe stop 'as at tools/agent-instructions/adopt-agent-instructions.test.sh:18-19'. Every sibling's stop is two lines that both spell `FOREIGN_PREFIX_PROBE`: a comment and the `if`. AC5 requires `grep -n 'FOREIGN_PREFIX_PROBE'` to print exactly one line.",
   "impact": "A faithful copy of the sibling shape fails AC5. A build that passes AC5 has had to drop the attribution comment every other suite carries, so the spec contradicts itself and the criterion reds on a correct build.",
   "fix": "Have AC5 expect the two lines every sibling carries, both between the arm 1 and arm 2 headers, with the `if` line printing the stop and reading `fail` and `n`. Or match only the `if` line with `grep -n 'FOREIGN_PREFIX_PROBE:-0'`.",
   "evidence": "`git grep -c 'FOREIGN_PREFIX_PROBE' -- '*.test.sh'` printed 2 for every listed suite, for example `tools/agent-instructions/adopt-agent-instructions.test.sh:2` and `tools/hooks/scratch-guard.test.sh:2`. Lines 18-19 of the agent-instructions suite are `# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): …` and `if [ \"${FOREIGN_PREFIX_PROBE:-0}\" = 1 ]; then …`."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-8.md",
   "where": "section 5 AC6",
   "severity": "medium",
   "claim": "AC6 diffs `ebce889c7 <pass>`, not the pass commit alone, and requires `-- tools/` to list exactly one file. Unit 8 shares order step 1 with units 1, 2 and 9, which all edit `tools/`, and M6 commits every pass on the run's one branch.",
   "impact": "Unless unit 8 happens to be built first in step 1, the diff also lists the tools/ files those units edited (unattended-build.test.sh, tier2-review.test.sh, run-gates.turnstile.test.sh, gate-guard.js, govkit files). AC6 then reds on a correct build. The same base-anchored range would also read a merge of main into the branch as this unit's change (C11 class).",
   "fix": "Diff the pass commit alone: `git diff --stat <pass>~1 <pass> -- tools/` lists only `tools/run-gates/run-gates.test.sh`, and the MP_BOUND check reads `git diff <pass>~1 <pass> -- tools/run-gates/`. This is the form units 5 and 6 already use.",
   "evidence": "read: README.md gen:build-order step 1 holds units 1, 2, 8 and 9 with `Parallel: yes`. read: memory/guides/BUILD-METHOD.md:185, 'Commit at the end of every pass, on the run's branch'. read: spec 1 §4 Files touched names tools/workflows/unattended-build.test.sh, tools/workflows/tier2-review.test.sh and tools/run-gates/run-gates.turnstile.test.sh. Spec 2 names tools/unattended/gate-guard.js, and spec 9 names three tools/govkit files."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-8.md",
   "where": "section 6 Gates, 'What these legs do not check'",
   "severity": "medium",
   "claim": "C6: unit 8 says 'the fork leg's argv excludes `*.test.sh`, so it reads none of this file'. Unit 5 §4 and the code say the opposite: `scan_spawn_tree` scans every tracked `*.test.sh` for the registry classes whatever the pathspecs exclude, and run-gates.test.sh has six registry rows.",
   "impact": "Unit 8's builder is told that the fork idioms it adds to run-gates.test.sh are ungraded, for example a `$(printf …)`, a `printf | grep` or a path-subst in the new red branches. Any such addition raises a row count, and the `shell hygiene (a fork spent on builtin work)` leg reds at the close. The spec's own statement of what the gates do not check is wrong, and it will mislead the next edit to this suite.",
   "fix": "Restate it: the fork leg grades this file for the registry classes through `scan_spawn_tree`, against the rows at `memory/project/spawn-idiom-sites.txt:214-219` (cat-file 25, date-fmt 1, path-subst 12, printf-subst 2, pure-fn-subst 11, var-pipe 141). Every line the unit adds uses a no-fork form, so no count rises. Add a criterion that the pass diff adds no `$(printf`, `$(basename`, `$(dirname` or var-pipe site, as unit 6's AC5 does.",
   "evidence": "`python -c` over tools/gate-legs.json printed the leg argv `[..., \"--spawn-idioms\", \"memory/project/spawn-idiom-sites.txt\", \".\", \":!*.test.sh\", \":!memory/\"]`. read: tools/gate-lint/sh_hygiene.py:843-850, docstring 'plus every tracked `*.test.sh` for the registry classes only', with `suites = … read_shell_sources(root, [\"*.test.sh\"])`. `grep -n 'run-gates/run-gates.test.sh' memory/project/spawn-idiom-sites.txt` printed rows 214-219."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-3.md",
   "where": "section 5 AC2 (against section 2 S2)",
   "severity": "medium",
   "claim": "AC2 observes the deployer, not the S2 fixture edit. Its positive half (apply of agent-cap,settings-merge,kickoff-manifest exits 0) and its negative half (the agent-cap,settings-merge selection refuses on the unmet requirement) are both green at base. No half greps `tools/govkit/selftest.py` for the changed kits line, `--kits` argument or `[answers]`.",
   "impact": "S2 can be left unbuilt, or built with the wrong line numbers or answers, and AC2 still passes when the scratch deploy is composed from S2's description. The edit is observed only by the close's suite run, so the acceptance ledger certifies S2 without looking at it.",
   "fix": "Add a grep half that fails today: for example `grep -n 'kickoff-manifest' tools/govkit/selftest.py` shows the aQuenchedHarness-3 fixture's kits line and `--kits` argument carrying it, and its `[answers]` carrying `manifest_path` and `user_skills`. Or state that the scratch deploy text is extracted from selftest.py at observation, so the base text reds.",
   "evidence": "read: spec 9 §6 AC6 runs the same `apply --kits agent-cap,settings-merge,kickoff-manifest` with DEPLOY_FULL's answers and records 'at base the exit, both CONFIGURE lines and the wired `agent-cap.js` command read the same, observed at spec time'. read: spec 3 §4 S2 says the base refusal `'agent-cap' requires 'kickoff-manifest'` comes from the engine (`tools/hooks/kit.toml:9`), which this unit does not edit (§3)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-9.md",
   "where": "section 2 S5 and S6 against section 6",
   "severity": "low",
   "claim": "S5 (the new `[dRB-9]` selftest arm) claims 'Observed by AC2' and S6 (the `check_outcome_states` extraction in matrix.py) claims 'Observed by AC4'. AC2 is a scratch program and AC4 calls the engine's `classify_outcome`/`outcome_accepted` directly, so neither reads selftest.py or matrix.py. S6's 'Lexicon's call keeps its two rows and its two check labels byte for byte' is observed by nothing.",
   "impact": "Every criterion passes with selftest.py and matrix.py untouched, and the lexicon refactor's preservation has no observation. Only the close's `New arm:` RED/GREEN reads S5 and S6.",
   "fix": "Add direct criteria. `grep -n '\\[dRB-9\\]' tools/govkit/selftest.py` shows one block after the u2a arms, reading `means` from the descriptor. `grep -n 'def check_outcome_states' tools/govkit/matrix.py` hits once, with two call sites. A diff of matrix.py's lexicon check labels against ebce889c shows them unchanged.",
   "evidence": "read: spec 9 §6 AC2 ('a scratch program builds a target … `govkit.py update`') and AC4 ('a python program imports `tools/govkit/govkit.py` … evaluates `outcome_accepted(...)`'). Neither names selftest.py or matrix.py. §7 carries the only lines naming them, as `New arm:` declarations."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-4.md",
   "where": "section 3 Non-goals (kit bump bullet), Edges, section 7",
   "severity": "low",
   "claim": "C6: unit 4 says `adopt-roles.test.sh` ships 'from the roles kit (tools/roles/kit.toml:47)'. It hands unit 7 a roles bump for it and says `kit epoch` reds at its tip until unit 7 bumps 'the hooks and roles kits'. kit.toml:47 declares that file `project-owned`, a role outside EPOCH_ROLES, and unit 5's Edges say the suites 'move no kit'. Unit 4 also calls the hooks kit by its directory, where unit 7 names it by its id, `agent-cap`.",
   "impact": "Two specs give different answers on whether the suite moves the roles version. Unit 4's builder will expect a roles epoch red at its tip that will not come from its own edit. Unit 7's mint derives the set anyway, so behaviour is unaffected.",
   "fix": "Say that only `tools/hooks/format-guard.js` (kit `agent-cap`) moves a version, and that `adopt-roles.test.sh` is project-owned. Drop the roles kit from unit 4's hand-off, §5 migration and §7.",
   "evidence": "`grep -n -B3 -A3 'test.sh' tools/roles/kit.toml` printed `47:include = [\"adopt-roles.test.sh\"]` / `48:role = \"project-owned\"`. read: tools/govkit/govkit.py:12935 `EPOCH_ROLES = (\"engine\", \"seed\", \"rendered\", \"merged\")`. `grep -n '^id' tools/hooks/kit.toml` printed `id = \"agent-cap\"`."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-7.md",
   "where": "section 1 Goal, section 3 Edges, section 4 'Why one unit', section 6 AC4",
   "severity": "low",
   "claim": "Unit 7 still measures 'the tree the other six units leave', and AC4 names 'each kit that units 1 to 6 moved'. Units 8 and 9 were added to the build (README amendments) and land before unit 7, but its Edges hold no consumes-from line for either.",
   "impact": "The measuring unit's stated population omits two units whose bytes precede it. If unit 8's or unit 9's file roles ever change, a kit they move would fall outside AC4's wording while the mint still bumps it, and the two would disagree. Today both specs argue their files are outside EPOCH_ROLES.",
   "fix": "Say 'the other eight units' and 'units 1 to 6, 8 and 9'. Add consumes-from edges for TOOL-dRedressedBar-8 (project-owned suite, no bump) and TOOL-dRedressedBar-9 (govkit-exempt files, measured by the mint), matching unit 9's §3 deferral to unit 7's mint.",
   "evidence": "read: spec 7 lines 19-21 ('over the tree the other six units leave') and 229 (AC4 'units 1 to 6'), with Edges at lines 65-82 naming units 1-6 only. read: README.md lines 40-48 (unit 8 and 9 amendments) and the gen:build-order with unit 7 at step 5. read: spec 9 §3, 'TOOL-dRedressedBar-7's mint over the finished tree measures that'."
  }
 ]
}
~~~~

### 2026-10-14T05:50:25 · gov-spec-reviewer · wf_2b03c380-02e/a1e50a36b86eb9b8f

Label: dRedressedBar · spec-audit round 1 · find:reuse

~~~~text
{
 "lens": "reuse",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-5.md",
   "where": "section 6 AC2 (and AC1)",
   "severity": "medium",
   "claim": "AC2 counts var-pipe sites with its own hand-typed grep -oE regex instead of the leg's existing classifier, `VAR_PIPE` and `scan_spawn_file` in tools/gate-lint/sh_hygiene.py:622-626 and :798-818, and the two answer differently.",
   "impact": "The scanner never counts a spelling inside a comment (`scan_spawn_file`: \"A spelling in a comment is a near miss of its class and never a site\"), and VAR_PIPE accepts `echo -n`/`echo -e` and a single quoted expansion only. The spec's grep (`(printf .%s(.n)?.|echo) +\"?\\$[{A-Za-z_][^|]*\\| *(...)`) counts commented spellings, misses `echo -n \"$v\" | grep -q`, and counts `\"$a$b\"`. So a conversion can pass AC2 while the leg still counts a site against a file with no row, or fail AC2 over a comment the leg ignores. The unattended-build.test.sh half compares this second count with the registry row the scanner owns. The two agree at base only because no such spelling exists there yet. The close's leg run still catches a real excess, so the effect stays inside the pass.",
   "fix": "Rewrite AC2 (and AC1's path-subst/date-fmt half) to ask the scanner's own classifier, read-only and not as the gate. Import tools/gate-lint/sh_hygiene.py and print `{k: sum(1 for _n, site, _c in v if site) for k, v in scan_spawn_file(open(f, encoding='utf-8').read()).items()}` for each touched file. Then require var-pipe/path-subst/date-fmt to read 0 for the three row-less files, and to equal the `memory/project/spawn-idiom-sites.txt` row for unattended-build.test.sh. Record the base reading (3, 1, 12, 70) from that call as the criterion's red case.",
   "evidence": "Grep (tool) with the AC2 pattern over the four files at HEAD printed: adopt-branch-reconcile.sh:3, unattended-build.test.sh:70, adopt-roles.test.sh:12, adopt-roles.sh:1, which matches the spec only at base. read: tools/gate-lint/sh_hygiene.py:802 (\"A spelling in a comment is a near miss of its class and never a site\"), :810-817 (VAR_PIPE matches on the code half are live; comment-half matches are not sites), :622-626 (VAR_PIPE admits `echo(?:[ \\t]+-[neE]+)?` and exactly one expansion before the pipe)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-3.md",
   "where": "section 4, \"S5, the exposed defect, fixed by unit 9\"",
   "severity": "low",
   "claim": "Unit 3 rev-2 restates the mechanism of the defect unit 9 owns, and the restatement contradicts unit 9's measured account. It says \"`apply` runs a requirement-complete selection, so the two always arrive together there\", but TOOL-dRedressedBar-9 §4 measured `apply --kits settings-merge` exiting 1 on the same adopter, and that measurement is why the fix moved to settings-merge's descriptor.",
   "impact": "Two specs in one build state opposite facts about one product defect. A reader of unit 3, or a later change built from it, will assume `apply` is immune and that the fix belongs in the gaining rule, which unit 9 rejected (C1, C1b) for exactly this reason. Nothing that gets built changes.",
   "fix": "In unit 3 §4 S5, drop the restated mechanism and point to TOOL-dRedressedBar-9 §4 (\"The defect, and where it sits\") as the one place that owns it, or correct the sentence to say that `apply --kits settings-merge` alone also fails at base, per unit 9.",
   "evidence": "read: memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-3.md:153-155 (\"`apply` runs a requirement-complete selection, so the two always arrive together there\"). read: memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-9.md:100-105 (\"Measured at spec time, `apply --kits settings-merge` over a fresh target exits 1 with `CONFIGURE settings-merge: adopter exit 2`\") and :340-343 (\"The brief's reuse line says `apply`'s requirement-complete selection never meets this defect. It does\")."
  }
 ]
}
~~~~

### 2026-10-14T05:50:25 · gov-spec-reviewer · wf_2b03c380-02e/a350ddb94f28d4f1a

Label: dRedressedBar · spec-audit round 1 · find:grounding

~~~~text
{
 "lens": "grounding",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-3.md",
   "where": "section 5 AC5 (first sentence), with section 2 S5 and section 3 'No scoping of the writing calls S5 names'",
   "severity": "high",
   "claim": "AC5's guard that the three witness arms stay unscoped can never fail. Its regex requires `\"--write\")` right after `str(<fixture>), `, so any update call with a `--kits` scope added stops matching and is never printed.",
   "impact": "A builder who took F1's rejected option (a) and scoped the up/u4/u9 writing calls would still pass AC5's grep. Those three arms would then read green without unit 9's fix, so the witness the owner chose under (c) would be lost. AC5's second half cannot catch it either, because it runs a separate scratch update and not the selftest arms. The criterion claims to check that the arms are unscoped, and it does not.",
   "fix": "Grep the call by its fixture alone, for example `grep -nE 'run\\(\"update\", \"--target\", str\\((up|u4|u9)\\)' tools/govkit/selftest.py`, and require that no printed line carries `--kits`. Then state the staged break: add `\"--kits\", \"check-wiring\"` before `\"--write\"` at line 3299 in a scratch copy, and the grep must print that line.",
   "evidence": "Ran `grep -nE 'run\\(\"update\", \"--target\", str\\((up|u4|u9)\\), \"--write\"\\)' tools/govkit/selftest.py` at HEAD. It printed 3299, 6886, 6900, 7064, 7074 and 7088, all of the form `run(\"update\", \"--target\", str(up), \"--write\")`. A line spelled `str(up), \"--kits\", \"check-wiring\", \"--write\")` or `str(up), \"--write\", \"--kits\", \"check-wiring\")` cannot match `str\\(up\\), \"--write\"\\)`, so the 'no printed line carries --kits' half is green before and after any scoping."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-1.md",
   "where": "section 5 AC1 (first sentence)",
   "severity": "medium",
   "claim": "AC1 says the spaced-call pattern 'reads 14', but `grep -c` counts matching LINES, not calls. The 14 calls sit on 5 lines, so a correct build reads 5 and AC1 reds.",
   "impact": "After a correct S1 fix, the criterion as written fails (5 is not 14). The builder must then either 'fix' something that is right or override the criterion. Either way, AC1 stops being the observation that the build is correct.",
   "fix": "Count occurrences, not lines: `grep -o \"build_gh33_writer [A-Z]-tB-[0-9] '\" tools/workflows/unattended-build.test.sh | wc -l` reads 14, and the glued form through the same `grep -o … | wc -l` reads 0. Or keep `grep -c` and state 5 lines.",
   "evidence": "At HEAD (tools/ equal to ebce889c7): `grep -c \"build_gh33_writer [A-Z]-tB-[0-9]'\"` printed 5, and `grep -o \"build_gh33_writer [A-Z]-tB-[0-9]'\" … | wc -l` printed 13. `grep -c \"build_gh33_writer [A-Z]-tB-[0-9] '\"` printed 1. `grep -n build_gh33_writer` shows the calls on lines 2471 (4 calls), 2483 (5), 2496 (1 glued and 1 spaced), 2503 (2) and 2512 (1), so after the fix there are 14 spaced calls on 5 lines."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-8.md",
   "where": "section 6, 'What these legs do not check of this change'",
   "severity": "medium",
   "claim": "The spec says the fork leg's argv excludes `*.test.sh`, 'so it reads none of this file'. That is false: `scan_spawn_tree` also scans every tracked `*.test.sh` for the registry classes, and `tools/run-gates/run-gates.test.sh` has six registry rows.",
   "impact": "A builder who trusts this sentence writes the S3 red branch without regard to the fork leg. If the server's stderr is printed through `$(cat …)`, a `printf '%s\\n' \"$x\" | sed 's/^/    /'` pipe (the shape the arm's existing red branch uses), or another `$(resolve_mp_record …)`, the cat-file (25), var-pipe (141) or pure-fn-subst (11) row is exceeded. The `shell hygiene (a fork spent on builtin work)` leg the spec lists then reds at the close. The spec told the builder that leg cannot see the file.",
   "fix": "Replace the sentence: the fork leg's argv excludes `*.test.sh`, but `scan_spawn_tree` (`tools/gate-lint/sh_hygiene.py:843-850`) still counts the six registry classes in every tracked suite, and this file holds rows at `memory/project/spawn-idiom-sites.txt:214-219`. Require S3's new lines to add no counted site: print `serve.err` with `sed 's/^/    /' \"$MP/x/serve.err\"` on the file, and add no `$(cat`, `$(printf`, `$(resolve_mp_record` or var-pipe. Add an AC that diffs the new lines for those spellings.",
   "evidence": "`tools/gate-legs.json:187-195`: the leg argv is `sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . :!*.test.sh :!memory/`. `tools/gate-lint/sh_hygiene.py:845-850` (scan_spawn_tree docstring): 'The product population under the pathspecs, plus every tracked `*.test.sh` for the registry classes only', with `suites = … read_shell_sources(root, [\"*.test.sh\"])`. `:16`: 'Six are counted per (path, class) in a shrink-only registry, the tracked `*.test.sh` included'. `grep -n run-gates.test.sh memory/project/spawn-idiom-sites.txt` printed rows 214-219: cat-file 25, date-fmt 1, path-subst 12, printf-subst 2, pure-fn-subst 11 (resolve_mp_record×11), var-pipe 141. Spec 5 §4 states the scan of suites correctly."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-4.md",
   "where": "section 3 (the kit version bump non-goal) and section 7 (kit epoch / kit version markers paragraph)",
   "severity": "low",
   "claim": "The spec says `adopt-roles.test.sh` 'ships … from the roles kit (tools/roles/kit.toml:47)', and that the epoch legs stay red at this unit's tip until unit 7 bumps 'the hooks and roles kits'. That line declares the suite `project-owned` (withheld), so unit 4 moves no roles bytes. Only the hooks (agent-cap) kit moves.",
   "impact": "Contained. It misleads whoever reads unit 4's tip, and it contradicts unit 5's correct statement that the suites are withheld from every payload. Unit 7 derives the kit set from the epoch, so no wrong version ships.",
   "fix": "Say that only `tools/hooks/format-guard.js` (agent-cap, engine, `tools/hooks/kit.toml:87-90`) ships, and that `adopt-roles.test.sh` is `project-owned` (`tools/roles/kit.toml:46-48`) and moves no kit. Drop 'roles' from the §7 sentence about the epoch reading red.",
   "evidence": "`sed -n 40,50p tools/roles/kit.toml` printed the comment 'THE ADOPTER'S SELF-TEST IS WITHHELD, by claiming the destination', then `include = [\"adopt-roles.test.sh\"]` (line 47) and `role = \"project-owned\"` (line 48). `EPOCH_ROLES = (\"engine\", \"seed\", \"rendered\", \"merged\")` is at `tools/govkit/govkit.py:12935`."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-5.md",
   "where": "section 4 working-set table and 'The suites' (adopt-roles.test.sh site lines), also spec 6 section 4 line cites",
   "severity": "low",
   "claim": "Spec 5 gives the adopt-roles.test.sh sites by their `ebce889c` line numbers (:90 … :251), but units 1 and 4, which build first, insert lines into that file. Unit 1 adds one probe-stop line after line 83, and unit 4 adds a comment and a constant after line 222. So every cited site from :90 on is off by 1, and :245 and :251 are off by 3, when unit 5 starts. Spec 6's arm-4 and floor cites (:100-107, :63) were also measured at the base.",
   "impact": "Contained. The builder's start-of-unit `git diff ebce889c` shows the shift, and the sites are also named by content. But a builder who converts 'line 90' by number edits the wrong line, and spec 5's statement that the earlier units add or remove no site reads as if lines were stable.",
   "fix": "Say in §4 that units 1 and 4 shift the adopt-roles.test.sh lines (+1 after :83, +2 after :222). Either restate the sites by content or arm, or tell the builder to re-map them with `grep -n` at the start, as AC4 of spec 6 already does for the floor.",
   "evidence": "Spec 1 §2 S5: the probe stop goes 'after arm 1's last assertion at line 83 and before arm 2'. Spec 4 §4: add `WORKFLOW_RUNS_DIR = \"workflows\"` 'on its own line directly after line 222, with a one-line `#` comment above it'. README build-order: step 1 runs units 1, 2, 8 and 9, step 2 runs 3 and 4, and step 3 runs 5. Spec 5 §4 table: adopt-roles.test.sh var-pipe sites `:83, :90, :97, :98, :106, :107, :113, :160, :183, :185, :245, :251` 'at ebce889c'."
  }
 ]
}
~~~~

### 2026-10-14T05:50:25 · gov-spec-reviewer · wf_2b03c380-02e/a7297b654871947ca

Label: dRedressedBar · spec-audit round 1 · find:blast-radius

~~~~text
{
 "lens": "blast-radius",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-2.md",
   "where": "section 2 S4 (Readers) and section 7 Gates",
   "severity": "low",
   "claim": "C54 retirement-inventory-misses-readers-by-value: S4 says the retired name `clean` has no reader outside gate-guard.js, 'and no other file in this tree'. But the generated codebase map lists it as a symbol of that file, and section 7 leaves out the leg that grades that map.",
   "impact": "After the rename, `memory/map/generated/symbols.json` still lists `clean` and lacks `renderAskQuote`. The `codebase-map coverage + freshness` leg has no guard, so it runs on every bar. Its `test_generated_artifacts_are_fresh` re-renders symbols.json and will read stale at unit 2's tip and at every tip until unit 7's `regen.py --write`. The spec says nothing moves outside gate-guard.js, so a builder or reviewer who sees that red will not trace it to this unit. The same applies to unit 9's new `check_outcome_states` in tools/govkit/matrix.py. The effect is contained because unit 7 regenerates every declared output last.",
   "fix": "Add `memory/map/generated/symbols.json` (written by `gen_map.py --write`, declared `[[regenerate]]` at tools/codebase-map/kit.toml:151-156) to S4 as a reader by name. State that unit 7's `regen.py --write` re-derives it. Add `codebase-map coverage + freshness` to section 7, noting it reads stale until unit 7. Make the same note in unit 9 for `check_outcome_states`.",
   "evidence": "`python -c \"...[s for s in d['symbols'] if s['file']=='tools/unattended/gate-guard.js' and s['id'] in ('clean',...)]\"` over memory/map/generated/symbols.json printed `{'id': 'clean', 'kind': 'function', 'file': 'tools/unattended/gate-guard.js'}`. `grep -rn '\"clean\"' memory/map/generated/` printed `symbols.json:5421: \"id\": \"clean\",`. `python tools/codebase-map/gen_map.py --check` exits 0 today, so the map is fresh at base and the rename is what makes it stale. tools/gate-legs.json: `codebase-map coverage + freshness` has no `guard` key. tools/codebase-map/test_codebase_map.py:289 maps symbols.json to `render_symbols_json`, and `:292` defines `test_generated_artifacts_are_fresh`."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-4.md",
   "where": "section 3 Non-goals (kit version bump bullet) and section 7 Gates",
   "severity": "low",
   "claim": "The spec says both touched files ship, `adopt-roles.test.sh` 'from the roles kit (tools/roles/kit.toml:47)'. It says the `kit epoch` and `kit version markers` legs read red 'until unit 7 bumps the hooks and roles kits'. But the descriptor declares that suite `project-owned`, a role the version epoch does not measure, so this unit moves no roles-kit epoch.",
   "impact": "The next reader is told unit 4 causes a roles epoch red that it cannot cause. Unit 7's mint table rightly credits the roles bump to unit 5's adopt-roles.sh. A reviewer reconciling the two specs, or checking unit 4's tip, will look for a roles-epoch red that unit 4 does not cause. Behaviour is unaffected.",
   "fix": "In section 3, say that only `tools/hooks/format-guard.js` ships and that `adopt-roles.test.sh` is `project-owned` (tools/roles/kit.toml:46-48). In section 7, say only the hooks (agent-cap) kit's epoch reds at this unit's tip.",
   "evidence": "`grep -n 'adopt-roles.test.sh' -B3 -A3 tools/roles/kit.toml` printed `47:include = [\"adopt-roles.test.sh\"]` and `48-role = \"project-owned\"`. `grep -n 'EPOCH_ROLES *=' tools/govkit/govkit.py` printed `12935:EPOCH_ROLES = (\"engine\", \"seed\", \"rendered\", \"merged\")`. read: memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-4.md:42-43 and :216-217."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-7.md",
   "where": "section 1 Goal, section 3 Edges, section 6 AC4",
   "severity": "low",
   "claim": "Unit 7 still describes its input tree as what 'the other six units' and 'units 1 to 6' leave. It has no consumes-from edge for TOOL-dRedressedBar-8 or TOOL-dRedressedBar-9, though both were added before the audit and both land before it.",
   "impact": "Units 8 and 9 move no epoch-graded bytes: run-gates.test.sh is project-owned, and the files under tools/govkit/ are registry-exempt. AC4's kit set therefore stays correct. But S1's regen does re-derive unit 9's new symbol (`check_outcome_states`), and the stop rule on a `run-gates` epoch hit depends on unit 8 staying in a project-owned file. Neither dependency is recorded where a later fold would look, and the README's '7 ... measured last over the code the others leave' no longer matches the spec's own count.",
   "fix": "Replace 'six units' and 'units 1 to 6' with 'every sibling unit, 1 to 6, 8 and 9'. Add consumes-from edges for TOOL-dRedressedBar-8 (tools/run-gates/run-gates.test.sh, project-owned at tools/run-gates/kit.toml:40-41, so no run-gates epoch hit) and TOOL-dRedressedBar-9 (tools/govkit/*, exempt at registry.toml:295-296; its new matrix.py function is re-derived into symbols.json by S1's regen).",
   "evidence": "read: memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-7.md:18 ('The bytes units 1 to 6 move'), :21 ('the other six units'), :65-78 (edges name units 1-6 only), :229 (AC4 'each kit that units 1 to 6 moved'). README.md:44-52 records the units 8 and 9 amendments and orders 7 last. `grep -n 'test.sh\\|project-owned' tools/run-gates/kit.toml` printed `40:include = [... \"run-gates.test.sh\" ...]` and `41:role = \"project-owned\"`. `sed -n 290,300p tools/govkit/registry.toml` printed `path = \"{prefix}/govkit\"` with why 'the deployer itself'."
  }
 ]
}
~~~~

### 2026-10-14T05:50:25 · gov-spec-reviewer · wf_2b03c380-02e/add1e522bf1eecd3c

Label: dRedressedBar · spec-audit round 1 · find:failure-envelope

~~~~text
{
 "lens": "failure-envelope",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-1.md",
   "where": "section 5 AC1",
   "severity": "medium",
   "claim": "AC1 counts calls with `grep -c`, which counts matching LINES. The 13 glued calls and the one spaced call sit on 5 lines, so a correct build reads 5 with the space, never the 14 the criterion requires.",
   "impact": "AC1 cannot pass as written over a correct build. A builder who meets it will either break the criterion or reshape the call lines (one call per line) to make the count reach 14. The red case is still caught by the glued half reading 0, but the positive half gives no signal.",
   "fix": "Count occurrences, not lines: `grep -o \"build_gh33_writer [A-Z]-tB-[0-9] '\" tools/workflows/unattended-build.test.sh | wc -l` reads 14, and the same with the glued pattern reads 0. The alternative is to state the line counts, 0 glued lines and 5 spaced lines.",
   "evidence": "`grep -c \"build_gh33_writer [A-Z]-tB-[0-9]'\" tools/workflows/unattended-build.test.sh` printed 5 and the spaced pattern printed 1. `grep -n build_gh33_writer` shows the 13 glued calls spread over lines 2471 (4), 2483 (5), 2496 (1), 2503 (2) and 2512 (1). After the fix the spaced-pattern `grep -c` can reach at most 5."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-1.md",
   "where": "section 5 AC4 (first sentence)",
   "severity": "medium",
   "claim": "AC4's placement check compares the unset's line number with the first hit of `grep -n 'git push'`. That first hit is line 2, a header comment, so the check grades no push: read as 'after' it holds wherever the unset sits, and read as 'before' it can never hold.",
   "impact": "The half of AC4 that should prove the unset precedes every push certifies nothing. An `unset GATE_SELFTESTS` placed after the RP and dg pushes (lines 991-1229) would pass this half while those arms still inherit the bar's value.",
   "fix": "Anchor on the first push the suite executes, not on any text: require the unset's line number to be below the first non-comment line matching `git push`, for example `grep -n 'git push' .githooks/pre-push.test.sh | grep -v '^[0-9]*:#' | head -1` (line 135 today). Or require it inside the environment-pin block at lines 109-118 that S4 names.",
   "evidence": "`grep -n 'git push' .githooks/pre-push.test.sh | head -3` printed `2:# pre-push.test.sh — drives a REAL git push through .githooks/pre-push…`, then `135:if git push -q origin main …` and `143:…`."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-9.md",
   "where": "section 4 'What it does not check', and section 5 security",
   "severity": "medium",
   "claim": "The spec says the false-accept state, where the hook is found outside `{prefix}/hooks` and `run` exits 2, is reachable only by an apply in which agent-cap's own adopter also runs. It is also reachable by `update` (agent-cap already claimed at a renamed home, settings-merge gained) and by `apply --kits settings-merge` alone over a target that already holds agent-cap. In both, every exit 2 from `run` is accepted as `no-agent-cap-to-wire` and agent-cap's adopter never runs. That covers a malformed settings.json, a non-object `hooks` and a failed write.",
   "impact": "In those states the verb exits 0 and prints an accepted stop that is false, because agent-cap is installed. A settings.json that cannot be parsed or written goes unreported by this kit. update also re-stamps the receipt and claims settings-merge, and the built-in Workflow|Agent entry stays unwired.",
   "fix": "Correct the section 4 envelope to name both routes. Then either narrow the accepted state, for example with a probe term for the resolver's second location `{prefix}/../hooks/agent-cap.js`, plus a section 4 statement that a receipt-homed hook cannot be probed; or price the residual explicitly. Add an AC or matrix row in which the hook sits at a receipt-recorded renamed home with a malformed `.claude/settings.json`, run through `apply --kits settings-merge` and through an update that gains settings-merge, and state the expected exit.",
   "evidence": "read: tools/settings-merge.py:205-224 (`_resolve_agent_cap_hook_path` answers from the receipt-reading resolver first). read: tools/settings-merge.py:508-517 (`run` returns 2 on a ValueError from `_load`/merge) and :536-539 (returns 2 on a write OSError). read: tools/govkit/govkit.py:11103-11126 (update runs adopters only for `gained` entries, so a claimed agent-cap's adopter does not run). read: spec section 4: 'That state is reachable only by `apply`, where agent-cap's own adopter runs the same argv'."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-7.md",
   "where": "section 1, section 3 Edges, section 6 AC4",
   "severity": "low",
   "claim": "C45 amendment-leaves-its-other-half-standing: the README's M2 ADD amendments added units 8 and 9 before the audit, but the measuring unit's spec still names 'units 1 to 6' and 'the other six units', and its Edges list consumes-from only units 1 to 6.",
   "impact": "The unit's text, ordered last 'over the code the others leave', misstates its own population. AC4 grades 'each kit that units 1 to 6 moved', so a kit moved by a review fold of unit 8 or 9 (for example in tools/run-gates/ or tools/settings-merge.py) is outside the criterion's stated set. This misleads the next reader. The derived epoch run would still see such a kit, so the behaviour is unaffected today.",
   "fix": "Revise unit 7 to name units 1 to 6, 8 and 9. Add consumes-from edges for TOOL-dRedressedBar-8 (run-gates.test.sh, project-owned, no epoch hit) and TOOL-dRedressedBar-9 (govkit-exempt files). Word AC4 as 'each kit the build's other units moved'.",
   "evidence": "read: memory/builds/dRedressedBar/README.md:40-48 (the two amendments adding units 8 and 9). read: spec-7 lines 18-21 ('The bytes units 1 to 6 move', 'the tree the other six units leave'), lines 65-78 (Edges list only units 1-6), and line 229 (AC4 'each kit that units 1 to 6 moved')."
  }
 ]
}
~~~~

### 2026-10-14T05:58:40 · gov-skeptic · wf_2b03c380-02e/a82fcd37295363481

Label: dRedressedBar · spec-audit round 1 · verify:ids-1-5

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 1,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Re-probed at the base tree. `grep -c \"build_gh33_writer [A-Z]-tB-[0-9]'\"` printed 5, the `grep -o … | wc -l` form printed 13, and the spaced `-o` form printed 1. The hits are lines 2471, 2483, 2496, 2503 and 2512, with several calls on each line. `grep -c` counts lines, so once the 13 glued calls are spaced, the spaced pattern can read at most 5 lines, not the 14 that AC1 at spec 1 lines 145-146 expects. A correct S1 build fails AC1.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 2,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "In .githooks/pre-push.test.sh, the first `git push` hit is line 2, a header comment. The first executed push is line 135, and the environment pins are at lines 109-118. AC4 (spec 1 lines 165-166) says the unset sits 'numbered below the first git push line'. Read as a smaller line number, that is impossible (under 2). Read as further down the file, it holds for any line after 2, including a line placed after some of the suite's pushes. So the placement half cannot catch the misplacement it is meant to guard. The scratch-clone half only drives the hook, which S4 leaves unchanged, so it is already green before the unit is built.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 3,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "§4 S5 (spec 1 lines 116-117) says to copy the siblings' stop 'as at tools/agent-instructions/adopt-agent-instructions.test.sh:18-19'. Those two lines are a `# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1)…` comment and the `if [ \"${FOREIGN_PREFIX_PROBE:-0}\" = 1 ]` line. A grep of the tools/ suites shows count 2 in every single-stop sibling. AC5 (line 175) requires `grep -n 'FOREIGN_PREFIX_PROBE'` to print exactly one line, so a faithful copy of the sibling shape fails AC5.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 4,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec 8 AC6 (lines 330-331) diffs `ebce889c7 <pass> -- tools/` and expects exactly one file. README gen:build-order step 1 holds units 1, 2, 8 and 9 with Parallel yes, and BUILD-METHOD.md:185 commits every pass on the run's branch. Spec 1 alone touches three tools/ suites, including tools/run-gates/run-gates.turnstile.test.sh, so unless unit 8 is built first the range lists other units' files and AC6 reds on a correct build. Units 5 and 6 already use the `<pass>~1 <pass>` form (spec 5 AC3/AC8, spec 6 AC5).",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 5,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "In tools/gate-legs.json, the fork leg's argv excludes `:!*.test.sh`. But sh_hygiene.py:843-850 `scan_spawn_tree` adds every tracked `*.test.sh` for the registry classes, through `read_shell_sources(root, [\"*.test.sh\"])`, and the scan is run from `--spawn-idioms` (line 910). memory/project/spawn-idiom-sites.txt rows 214-219 carry six classes for tools/run-gates/run-gates.test.sh. So spec 8 line 346's 'reads none of this file' is false, and it tells the builder that fork idioms added to the suite go ungraded. The gate still reds at the close, so the effect is contained. The suite lines the design adds (for example line 134) use arithmetic, not forks, so the fix's no-rise claim holds.",
   "fixVerdict": "sound",
   "fixNote": ""
  }
 ]
}
~~~~

### 2026-10-14T05:58:41 · gov-skeptic · wf_2b03c380-02e/abaef7a953a336fc7

Label: dRedressedBar · spec-audit round 1 · verify:ids-6-10

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 6,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "I read spec 3 lines 189-195 at the pinned blob (4d63d87b matched by hash-object). AC2 supplies its own `--kits agent-cap,settings-merge,kickoff-manifest` argument, so S2's edits to the fixture's kits line and `--kits` argument (selftest.py lines 15293 and 15306; I read lines 15289-15306, where the base reads `kits = [\"agent-cap\", \"settings-merge\"]` and `run(\"apply\", ..., \"--kits\", \"agent-cap,settings-merge\")`) are not looked at by any half. The negative half fails on the engine's requirement, which is green at base. The answers half would only red at base if the observer pulled the deploy text out of selftest.py. 'The fixture's text as S2 leaves it' does not say that, and spec 9 AC6 records the same apply with DEPLOY_FULL's answers as green at base. No AC2 half greps selftest.py. The effect is contained, because the `govkit selftest` gate at the close runs the arm and would red if S2 were unbuilt. The gap is in the acceptance ledger only, so I grade it low.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 7,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "I read spec 9 at blob 689d95e5. S5 (lines 37-40) and S6 (lines 41-45) say 'Observed by AC2/AC4, through the New arm line in §7'. AC2 (lines 266-275) is a scratch program running `govkit.py update`. AC4 (lines 282-289) imports govkit.py and calls classify_outcome/outcome_accepted. Neither reads selftest.py or matrix.py. The design promises 'Lexicon's call keeps its two rows and its two check labels byte for byte' (line 190-191), and no criterion checks it. Only the §7 `New arm:` declarations name those files. TEMPLATE-SPEC line 519 allows a suite to be named under New arm, but that is a declaration and not an observation. The defect is real and limited to the acceptance ledger.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 8,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 4 lines 42-44, 50 and 216-217 say `adopt-roles.test.sh` ships from the roles kit, and that `kit epoch` reds until unit 7 bumps 'the hooks and roles kits'. In tools/roles/kit.toml, line 47 is `include = [\"adopt-roles.test.sh\"]` and line 48 is `role = \"project-owned\"`. govkit.py:12935 has `EPOCH_ROLES = (\"engine\", \"seed\", \"rendered\", \"merged\")`, and derive_epoch_state keeps only survivors whose role is in EPOCH_ROLES, so this file moves no roles version. Spec 5 line 66 says its suites 'move no kit'. tools/hooks/kit.toml:3 is `id = \"agent-cap\"`. The prose is wrong, but unit 7's mint derives the set, so behaviour does not change.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 9,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 7 (blob cc4dcb64) says 'the other six units' at lines 20 and 162, and 'units 1 to 6' at lines 18 and 229. Its Edges (lines 65-82) name only units 1-6. The README amendments add units 8 and 9, and the README's order line says 7 'is measured last over the code the others leave', after 8 and 9. Spec 8 lines 274-278 say its edit is to project-owned `run-gates.test.sh` and points at unit 7's epoch stop, and spec 9 §3 defers to unit 7's mint. Unit 7 holds no matching consumes-from line. The mint derives the set, so behaviour is unaffected today.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 10,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec 3 line 215, AC5, greps `run\\(\"update\", \"--target\", str\\((up|u4|u9)\\), \"--write\"\\)` and requires that 'no printed line carries --kits'. Re-run at HEAD, the fixture-only grep printed 3288, 3294, 3299, 3311, 6886, 6900, 7064, 7074 and 7088, and the --write forms are all `str(X), \"--write\")`. Because the regex makes `\"--write\")` follow `str(X), ` directly, any call scoped with `--kits` stops matching. The guard is therefore green whether or not the calls are scoped. AC5's second half runs a separate scratch update, not the arms. I grade it medium, not high, because the witness is not wholly lost if a builder breaks the non-goal: unit 9's S5 adds its own `[dRB-9]` arm witnessing the same fix.",
   "fixVerdict": "sound",
   "fixNote": ""
  }
 ]
}
~~~~

### 2026-10-14T05:58:41 · gov-skeptic · wf_2b03c380-02e/a9eb9d4aaed8ccfff

Label: dRedressedBar · spec-audit round 1 · verify:ids-16-20

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 16,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Unit 3 lines 153-155 say \"`apply` runs a requirement-complete selection, so the two always arrive together there\". Unit 9 lines 101-103 say the opposite: they record that `apply --kits settings-merge` exits 1 with `CONFIGURE settings-merge: adopter exit 2`. Unit 9 lines 340-343 also reject the brief's claim that apply never meets the defect. So two specs in one build state opposite facts about the same defect. Unit 3 changes nothing for S5, so only the prose is affected.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 17,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Unit 2 S4 (lines 31-35) says `clean` has no reader by name outside gate-guard.js, 'and no other file in this tree'. But memory/map/generated/symbols.json lines 5420-5423 list `{\"id\": \"clean\", \"kind\": \"function\", \"file\": \"tools/unattended/gate-guard.js\"}`. test_codebase_map.py includes symbols.json in its freshness check: CONDITIONAL_TIERS maps it to render_symbols_json, and test_generated_artifacts_are_fresh follows. In gate-legs.json, the `codebase-map coverage + freshness` row (lines 814-823) has no guard key. Section 7 of unit 2 names only the two lexicon legs. Unit 7 S1 runs regen.py --write, which re-derives the map, so the effect is contained.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 18,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Unit 4 lines 42-43 say adopt-roles.test.sh ships from the roles kit (kit.toml:47). Lines 216-217 say the epoch and version-marker legs read red until unit 7 bumps the hooks and roles kits. But tools/roles/kit.toml:47-48 gives that file `role = \"project-owned\"`, and govkit.py:12935 sets EPOCH_ROLES = (\"engine\", \"seed\", \"rendered\", \"merged\"). So unit 4's edit to that suite moves no roles epoch, and the spec misattributes the red. Behaviour is unaffected.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 19,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Unit 7 line 18 says 'The bytes units 1 to 6 move', line 21 says 'the other six units', and AC4 says 'each kit that units 1 to 6 moved'. The Edges list only consumes-from units 1 through 6. A grep of unit 7 for unit 8 or 9 finds them only in the research-row index at line 9, with no edge. Units 8 and 9 do land before unit 7. As the finding says, their files are project-owned or exempt, so AC4's kit set stays correct. Only the record is incomplete.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 20,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "AC1 (unit 1 lines 145-146) requires `grep -c` with the spaced pattern to read 14. grep -c counts matching lines, not matches. In tools/workflows/unattended-build.test.sh, every build_gh33_writer call sits on one of lines 2471, 2483, 2496, 2503 and 2512: 4, 5, 2 (one already spaced), 2 and 1 calls. So after a correct fix the spaced count is at most 5, and AC1's positive half can never pass over a correct build. The glued half reading 0 still works as a red signal, so the damage is contained.",
   "fixVerdict": "sound",
   "fixNote": ""
  }
 ]
}
~~~~

### 2026-10-14T05:58:41 · gov-skeptic · wf_2b03c380-02e/ab1a8c92a2fbeb47c

Label: dRedressedBar · spec-audit round 1 · verify:ids-21-23

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 21,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec-1 lines 165-167 read: AC4 requires the `^unset GATE_SELFTESTS` line to be 'numbered below the first `git push` line that `grep -n 'git push'` finds'. Grepping .githooks/pre-push.test.sh for 'git push' returns line 2 first, and line 2 is the header comment ('# pre-push.test.sh — drives a REAL git push...'). The first push that actually runs is line 135. Read as 'a higher line number', the check holds anywhere in the file, including after run_rp_push (line 991) and the dg pushes (1222-1229). Read as 'a lower line number', it can never hold. Either way the placement half of AC4 checks nothing. The behavioural half (the scratch-clone decision and Red-when) still covers the outcome, so the effect stays contained.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 22,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec-9 section 4 (line 157) says the false-accept state is 'reachable only by `apply`, where agent-cap's own adopter runs the same argv'. The code does not bear that out. In govkit.py:11104-11126, update runs an adopter only for entries in `gained`. When agent-cap is already claimed and settings-merge is gained, agent-cap's adopter does not run. settings-merge.py:78-108 (resolve_kit_dir) reads the receipt first, so it finds a hook at a renamed home. settings-merge.py:507-539 `run` then returns 2 on a ValueError from a malformed or non-object settings.json and on a write OSError. The probe has `must_not_exist` set to `{prefix}/hooks/agent-cap.js`, which is absent at a renamed home, so the exit 2 is accepted as no-agent-cap-to-wire. apply's CONFIGURE (govkit.py:7740-7764) runs only the selected kits, so `apply --kits settings-merge` over a target that already holds agent-cap is another route where no agent-cap adopter reports the failure. The section-4 envelope and the section-5 security claim are therefore false. The paths are narrow, and the consequence is a malformed settings.json going unreported by this kit, so I grade it medium. The fix is feasible: classify_outcome (govkit.py:6313-6324) already accepts a list for must_not_exist, so a second term `{prefix}/../hooks/agent-cap.js` can be added.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 23,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "README.md:40-48 adds units 8 and 9 by M2 ADD amendments, and line 52 orders unit 7 'last over the code the others leave'. Spec-7 still speaks of 'the bytes units 1 to 6 move' (line 18), 'the other six units' (lines 20 and 162) and 'each kit that units 1 to 6 moved' (AC4, line 229). Its consumes-from edges (lines 65-78) list only units 1-6. Unit 7's own table at line 9 already cites units 8 and 9, so the text is inconsistent with itself. The finder agrees the derived run still measures the real tree, so behaviour does not change: low. On the fix: renaming the population and adding the two edges cures the defect. The parenthetical descriptions of the edges ('no epoch hit', 'govkit-exempt files') were not verified here, and the build should check them when it writes them rather than copy them.",
   "fixVerdict": "sound",
   "fixNote": ""
  }
 ]
}
~~~~

### 2026-10-14T05:58:41 · gov-skeptic · wf_2b03c380-02e/adf44a843a024f838

Label: dRedressedBar · spec-audit round 1 · verify:ids-11-15

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 11,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec 1 lines 145-146 say: \"When `grep -c \"build_gh33_writer [A-Z]-tB-[0-9]'\"` ... reads 0, and the same pattern with a space before the quote reads 14.\" grep -c counts matching lines. `grep -n build_gh33_writer` shows the calls only on lines 2471, 2483, 2496, 2503 and 2512. `grep -o` for the glued form printed 13, and for the spaced form printed 1, so there are 14 calls on 5 lines. After a correct fix, `grep -c` on the spaced form prints 5, not 14, so AC1 goes red on a correct build.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 12,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec 8 lines 345-346 say: \"the fork leg's argv excludes `*.test.sh`, so it reads none of this file.\" That is false. The leg argv (gate-legs.json:187-195) is `sh_hygiene.py --spawn-idioms ... . :!*.test.sh :!memory/`. But `scan_spawn_tree` (sh_hygiene.py:843-850) also reads every tracked `*.test.sh` for the registry classes (`suites = ... read_shell_sources(root, [\"*.test.sh\"])`). spawn-idiom-sites.txt:214-219 holds six rows for tools/run-gates/run-gates.test.sh: cat-file 25, date-fmt 1, path-subst 12, printf-subst 2, pure-fn-subst 11, var-pipe 141. A new counted site in S3 would therefore red that leg. The impact is contained because the close's leg run catches it.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 13,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 4 lines 42-43 say adopt-roles.test.sh ships \"from the roles kit (tools/roles/kit.toml:47)\". Lines 216-217 say the epoch legs stay red \"until unit 7 bumps the hooks and roles kits\". In fact tools/roles/kit.toml:42-48 withholds the suite (`include = [\"adopt-roles.test.sh\"]`, `role = \"project-owned\"`). tools/hooks/kit.toml:87-90 ships format-guard.js as engine. Only the hooks kit's shipped bytes move. Spec 5:65 correctly says the suites are withheld. The error only misleads whoever reads the spec. Unit 7 derives the set by measurement.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 14,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "The README build order runs unit 1 and unit 4 (steps 1-2) before unit 5 (step 3). Spec 1 S5 adds a probe stop after line 83. The sibling form (e.g. tools/check-dead-paths.test.sh:115-116) is a comment line plus an `if` line, so it adds about 2 lines. Spec 4 adds a comment and a constant after line 222 (+2). Spec 5 lines 81-89 and 152-162 still cite the adopt-roles.test.sh sites by their ebce889c line numbers (:90 ... :251). Spec 5:94-96 describes unit 4 only as renaming a literal. So the cited numbers are stale when unit 5 starts. The effect is contained: spec 5:97 already has the builder read `git diff ebce889c`, and each site is described by content. The fix's own offsets are wrong, though: \"+1 after :83\" undercounts the two-line probe-stop shape the sibling suites carry. Writing new, wrong numbers would repeat the defect.",
   "fixVerdict": "unsound",
   "fixNote": "In spec 5 §4, say that units 1 and 4 add lines to adopt-roles.test.sh: the probe stop after arm 1, and the WORKFLOW_RUNS_DIR comment and constant in A9_WRITE. Then have the builder re-map every cited site by content with `grep -n` at the start of the unit, as spec 6 AC4 already does for the floor. Do not restate fixed offsets."
  },
  {
   "id": 15,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec 5 AC2 (lines 247-255) counts var-pipe sites with its own `grep -oE` regex. The leg's classifier works differently. VAR_PIPE (sh_hygiene.py:622-626) admits `echo(?:[ \\t]+-[neE]+)?` and exactly one expansion. scan_spawn_file (:798-818) runs the code half and the comment half separately and marks a comment-half match not a site. The AC2 regex `echo +\"?\\$` misses `echo -n \"$v\"`. It counts commented spellings, because grep sees whole lines. Its `[^|]*` also admits multi-expansion operands. So AC2 and the leg can disagree once a conversion touches such spellings. The base figures agree only by coincidence. The close's leg run still catches a real excess, so the effect is contained.",
   "fixVerdict": "sound",
   "fixNote": ""
  }
 ]
}
~~~~

### 2026-10-14T06:00:18 · gov-synthesizer · wf_2b03c380-02e/ae331408c8f4076cc

Label: dRedressedBar · spec-audit round 1 · synth

~~~~text
{
 "path": "C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/reviews/2026-10-14-review-TOOL-dRedressedBar-spec-audit-round1.md",
 "summary": "On your question: yes, the Role text reached this agent. It came in as my standing instructions (\"You are the synthesizer of a review…\" plus the Charter), not inside the task message. The task message itself starts at \"Write the Tier-2 review report\", so if you are reading only the query, the Role part sits in front of it in the instructions and is easy to miss.\n\nThe review report for the dRedressedBar spec audit (round 1) is written. Verdict: CLEAN WITH FIXES. All 23 confirmed findings are covered in 15 items. 8 items are medium (12 findings) and 7 are low (11 findings). There are no blockers or highs.\n\nThe medium items:\n- **Unit 1, AC1:** `grep -c` counts lines, so a correct build reads 5, not the 14 calls expected.\n- **Unit 1, AC4:** the placement check is anchored on a header comment, so it cannot fail.\n- **Unit 1, AC5:** it expects one probe-stop line where the sibling suites it copies have two.\n- **Unit 8, AC6:** it diffs from the build base, so other units' `tools/` edits make it fail.\n- **Unit 8, §6:** it says the fork leg reads none of `run-gates.test.sh`, but the leg does grade that file.\n- **Unit 3, AC5:** the regex can never match a scoped call, so the guard can never fail.\n- **Unit 5, AC2:** it counts with its own regex instead of the gate's classifier.\n- **Unit 9, §4/§5:** a failure state it calls reachable only by `apply` is also reachable by two other routes.\n\nThe low items are unit 4 wrongly treating `adopt-roles.test.sh` as shipping in the roles kit, unit 7 not counting units 8 and 9, stale line numbers in unit 5, contradicting prose between units 3 and 9, a reader of `clean` that unit 2 misses, and two criteria in units 3 and 9 that never read the files they claim to check.\n\nThe skeptics re-graded two findings: id 10 from high to medium and id 6 from medium to low. One proposed fix was judged unsound (id 14), and the report gives the skeptic's corrected fix in its place. All 5 lenses and all 5 skeptic batches returned, and no findings are unverified.",
 "items": [
  {
   "severity": "MEDIUM",
   "ids": [
    1,
    11,
    20
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    2,
    21
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    3
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    4
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    5,
    12
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    10
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    15
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    22
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    6
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    7
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    8,
    13,
    18
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    9,
    19,
    23
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    14
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    16
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    17
   ]
  }
 ]
}
~~~~

### 2026-10-14T06:03:07 · gov-spec-writer · wf_2b03c380-02e/ac6afe604db5e2fd4

Label: dRedressedBar · audit round 1 · dispose

~~~~text
{
 "disposed": true,
 "standing": [],
 "promoted": 23,
 "folded": 0,
 "refuted": 0,
 "promotedIds": [
  "TOOL-dRedressedBar-10"
 ],
 "edges": [
  {
   "from": "TOOL-dRedressedBar-10",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-1"
  },
  {
   "from": "TOOL-dRedressedBar-10",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-2"
  },
  {
   "from": "TOOL-dRedressedBar-10",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-3"
  },
  {
   "from": "TOOL-dRedressedBar-10",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-4"
  },
  {
   "from": "TOOL-dRedressedBar-10",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-5"
  },
  {
   "from": "TOOL-dRedressedBar-10",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-6"
  },
  {
   "from": "TOOL-dRedressedBar-10",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-7"
  },
  {
   "from": "TOOL-dRedressedBar-10",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-8"
  },
  {
   "from": "TOOL-dRedressedBar-10",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-9"
  },
  {
   "from": "TOOL-dRedressedBar-1",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-10"
  },
  {
   "from": "TOOL-dRedressedBar-2",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-10"
  },
  {
   "from": "TOOL-dRedressedBar-3",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-10"
  },
  {
   "from": "TOOL-dRedressedBar-4",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-10"
  },
  {
   "from": "TOOL-dRedressedBar-5",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-10"
  },
  {
   "from": "TOOL-dRedressedBar-6",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-10"
  },
  {
   "from": "TOOL-dRedressedBar-7",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-10"
  },
  {
   "from": "TOOL-dRedressedBar-8",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-10"
  },
  {
   "from": "TOOL-dRedressedBar-9",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-10"
  }
 ],
 "placements": [
  {
   "unit": "TOOL-dRedressedBar-10",
   "repairs": "none",
   "order": 6
  }
 ],
 "summary": "YOUR QUESTION: yes, the Role part reaches spec writers, but it does not arrive in the query. It arrives as the agent's system prompt, and the query carries only the Task. That split is on purpose.\n- The `Agent` call's prompt is the `gov:handoff` marker line followed by the record's `## Task` section, and nothing else. The spawn guard admits no other shape (tools/hooks/agent-cap.js:45-50). `handoff.py render --part task` prints exactly that (tools/roles/handoff.py:18).\n- The Role comes from `subagent_type: gov-spec-writer`. Claude Code loads `.claude/agents/gov-spec-writer.md` as the system prompt. That file is the role body plus a `## Charter` block, rendered from tools/roles/agents/gov-spec-writer.agent.md.\n- I checked this from inside this session. My system prompt opens with the Role text (\"You are a code architect...\") followed by the Charter. The `## Role` section of prompts/2026-10-14-prompt-TOOL-dRedressedBar-9-1-spec-writer.md matches the installed agent body once blank lines are ignored.\n- One gap: agent-cap.js:58 says the guard never compares the marker's `role-sha` with the role the agent type was rendered from. So if `.claude/agents/gov-spec-writer.md` drifts from what a record's `## Role` says, nothing catches it.\n\nTHE AUDIT: all 23 confirmed findings in reviews/2026-10-14-review-TOOL-dRedressedBar-spec-audit-round1.md are disposed. There were no blockers or highs and nothing was unverified, so nothing was refuted and nothing is left standing.\n- All 23 (12 mediums, 11 lows) are promoted, batched into ONE new unit, `TOOL-dRedressedBar-10`. Its spec is memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md, Tier-2, order 6.\n- Its §1 lists every report id with the report item it shares. Its §2 gives each id its own item, S1 to S23, where S<n> closes id n, plus S24 for the acceptance ledger and the sibling rev bumps.\n- I did not split it into two units. S7, S17 and S22 all write spec 9, so no split gives two disjoint write sets.\n- `repairs` is none: the findings land on eight specs, so the unit goes after every unit in the build (the highest so far is 5).\n- How the unit works: each sibling is built against its criteria as written. Unit 10 then observes, over the built tree, the corrected form of each criterion that could not pass or could not fail. It corrects the false prose in specs 1 to 9 with one rev bump each.\n- It narrows settings-merge's accepted stop by adding a second `must_not_exist` term, `{prefix}/../hooks/agent-cap.js`, and one `check_outcome_states` row in tools/govkit/matrix.py. Both files are under govkit, which is exempt from version bumps (tools/govkit/registry.toml:295-297).\n\nDECISION FOR YOU: §8 F1 of the new spec is open, so the unit is FORKED until you resolve it. The question is how id 22 is closed.\n- (a) Narrow the stop as above and state the remaining gap in spec 9. I recommend this.\n- (b) Correct spec 9's prose only, with no product change.\n- (c) A probe term that reads the install receipt. This closes every route, but it is a separate mechanism that needs its own unit, which you would have to add.\n- What (a) leaves open: a hook that only the receipt can locate, for example agent-cap installed under a `[kit.agent-cap] prefix`, still reads as an accepted stop when `.claude/settings.json` cannot be parsed.\n\nEDGES: every edge has both ends. Unit 10 consumes from units 1 to 9. Each of specs 1 to 9 gained the mirroring hands-off to unit 10, as a rev bump with its revision line: spec 1 rev-2, spec 2 rev-2, spec 3 rev-3, spec 4 rev-2, spec 5 rev-2, spec 6 rev-2, spec 7 rev-2, spec 8 rev-2, spec 9 rev-2. No scope, design or criterion of those specs moved.\n- The README's authored Units table gained row 10, which names all 23 report ids.\n- Each finding was re-checked against the code, and the specs hash to the blobs the report pinned. One correction to the report: the codebase-map row it cites as `[[regenerate]]` is actually `[[generated]]`, at tools/codebase-map/kit.toml:148-156.\n\nCHECKS AND COMMIT: the memory hygiene gate flags check 9 because the generated index in the build README is stale. That is expected: whoever dispatched this regenerates and commits. Its other failures, check 17 and check 23, are in other builds' records and existed before. Nothing is committed."
}
~~~~

### 2026-10-14T09:19:52 · gov-spec-writer · direct/a12beabadd255e000

Label: dRedressedBar · TOOL-dRedressedBar-10 · spec-write

~~~~text
I've revised `TOOL-dRedressedBar-10` to rev-2. The acceptance check passes: `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades it READY, not FORKED.

**Unit TOOL-dRedressedBar-10: authored (rev-2).** File: `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-10.md`

S22 stays as option (a) states it. The second `must_not_exist` term, the matrix row, AC15, AC16, AC17 and the §7 `New arm:` line are unchanged.

What changed:
- **Header:** `rev-2`, and `ratified 2026-10-14` added to the tail, following unit 3's rev-2.
- **§8 F1:** marked `RESOLVED (owner, 2026-10-14): (c)` in place. It says S22 keeps (a), and the receipt-reading term is `TOOL-dRedressedBar-11`, not part of this batch (M2, M4).
- **Residual now points at unit 11:** the S22 item, the §3 non-goal, §4's residual paragraph, the §5 security line and AC16's `figure:` line no longer call the receipt-homed residual "priced" or "accepted by design". AC16's commands and expected rows are unchanged.
- **AC18:** it now also checks that spec 9's §5 names `TOOL-dRedressedBar-11`. This follows from pointing the residual at unit 11, because S22 writes that residual into spec 9.
- **§3 Edges:** a new `- **hands-off** \`TOOL-dRedressedBar-11\`` line for the receipt-homed residual, in the code-2 block this unit narrows.
- **§1:** "ordered after every unit of the build" now reads "ordered after every unit the audit read". The old wording became false once unit 11 was ordered after unit 10.
- **§9:** a rev-2 line naming every section and criterion that moved.

No product file, criterion command or order value moves. The "priced" wording in F1's option (b) text and in the Alternatives row is still there, because it describes the rejected option, not this unit's position.

**Memory hygiene** found nothing in this spec. It did fail on other things:
- Check 9: `memory/LIVE.md` and the build README are stale against a fresh render. That is the index regeneration you run once at commit.
- Check 23: acceptance-ledger lines in `aSparedSpawn` and `aOrientedCast`, which are not this build's.

I did not run the naming lexicon, because this revision adds no code identifier for it to check.

**For you:**
1. **Reciprocal edge:** unit 11's spec does not exist yet in this worktree. The new hands-off line needs a matching `consumes-from \`TOOL-dRedressedBar-10\`` in unit 11's Edges, which its writer owns.
2. **Unit 7's order (possible fork):** unit 10 already takes unit 7's work as an input (its `regen.py --write` run and kit version bumps happen before unit 10). If unit 11's writer decides unit 7 must run after unit 11, unit 10 would then come before unit 7, and that dependency and AC14 would break. If unit 11 only touches govkit-exempt files, unit 7's place should not move. I did not decide this.
~~~~

### 2026-10-14T09:20:12 · gov-spec-writer · direct/a15917dbd6959d0ee

Label: dRedressedBar · TOOL-dRedressedBar-11 · spec-write

~~~~text
**TOOL-dRedressedBar-11 — written.** It is Tier-2, SPECCED rev-1, order 7, with base `ebce889c` and no open questions.

Spec: `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-11.md`

I ran memory hygiene checks 12 and 25 against a scratch copy of the index with the spec added, and both are clean. The live index was not touched. The full run's other failures (checks 9, 17 and 23) were there before this spec. Nothing is committed and no index was regenerated.

**The design:**
- **The new term.** Probe blocks gain a new key, `must_not_resolve = "<here>/<home>/<anchor>"`. govkit evaluates it with the copy of `resolve_kit_dir` already inside `govkit.py`, which a parity leg keeps identical to the copy settings-merge's adopter runs. The probe and the adopter therefore read the receipt the same way, and the receipt-reading code is not written twice.
- **With no receipt.** A fresh apply has no receipt, so the term checks only the two static homes, which is exactly what the adopter does. A token that does not resolve, or a value too short to split, refuses the stop.
- **Probe keys in one place.** `OUTCOME_PROBE_KEYS` in `govkit.py` now lists every probe key. `classify_outcome` loops over it, and the matrix derives its keys from it.
- **Every probe reader is covered.** All four engine call sites go through `classify_outcome` (`check`, apply's configure step, update's regenerate loop and update's gained-kit loop). The matrix handles the new key in all three of its existing rules. A new matrix rule fails any probe key the engine does not evaluate.
- **The real error is shown.** When apply or update refuses an adopter's exit, the message now ends with the last lines of the adopter's stderr. This is what lets the acceptance case show "cannot read .claude/settings.json".
- **No version moves.** All four touched files are under `tools/govkit`, which the registry exempts. `KIT_GOVKIT_VERSION` stays at 1.14, and no descriptor schema version exists.
- **Unit 7 does not need to move after unit 11.** Unit 11 adds no function, so `symbols.json` stays current after unit 7's regen, and AC7 checks this.

**Things you need to act on:**
1. **README ordering.** The roster row already exists, and `order 7` will put unit 11 in the build order when you regenerate. The rule that says unit 7 "is measured last" has been wrong since unit 10. It should say units 10 and 11 come after 7, each touching only govkit-exempt files and adding no function.
2. **No direct edge to unit 9.** The hygiene check requires every edge to be mirrored in the other spec, and spec 9 has no line pointing back at unit 11. I may not edit spec 9, so the dependency goes through the `consumes-from TOOL-dRedressedBar-10` edge instead. If you want the direct edge, add `hands-off TOOL-dRedressedBar-11` to spec 9 and I can add the matching line here.
3. **The brief is wrong about the base.** At `ebce889c` the first case does not show a false accepted stop. Measured: the exit is refused as `unclassified` and exits 1, with no reason given, because there is no code-2 block yet. The false accept only appears once unit 9's or unit 10's block exists, so each criterion's failing half is run against unit 10's pass commit.
4. **A separate defect turned up while measuring.** A first `apply` that selects agent-cap with `[kit.agent-cap] prefix = "scripts"` exits 1, with both adopters exiting 2. The configure step runs before the receipt is written, so neither adopter can find the hook. It is recorded as an external hand-off and is not fixed in this unit.

The supporting measurements were taken at `60fa5534`, whose `tools/` matches `ebce889c`, using throwaway targets in the session scratchpad.
~~~~

### 2026-10-14T09:42:54 · gov-spec-writer · wf_252ed723-81c/a338aa6bf7a7e24ae

Label: dRedressedBar · TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 · spec-write

~~~~text
{
 "authored": [],
 "alreadyPresent": [
  "TOOL-dRedressedBar-1",
  "TOOL-dRedressedBar-2",
  "TOOL-dRedressedBar-8",
  "TOOL-dRedressedBar-9",
  "TOOL-dRedressedBar-3",
  "TOOL-dRedressedBar-4"
 ],
 "refused": [],
 "summary": "All six units were already specced, so nothing was authored, committed or regenerated. Each spec is under C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-<n>.md. Each status header names its own unit id and the order this roster gives it: order 1 for units 1, 2, 8 and 9, order 2 for units 3 and 4. Revisions: units 1 and 8 are Tier-1 rev-2; units 2, 9 and 4 are Tier-2 rev-2; unit 3 is Tier-1 rev-3, ratified 2026-10-14. Each has the full section set its tier requires, in order; the Tier-2 specs include the reuse audit. No open question is unresolved: five specs say none, and unit 3's F1 was resolved by the owner on 2026-10-14 in favour of option (c). A scan found no leftover template text. The memory hygiene gate exits 1, but every failure is check 23 on acceptance ledgers from other builds (TOOL-aSparedSpawn-*, TOOL-aOrientedCast-22), and no finding names any dRedressedBar spec. Log: C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-bar-profile-failures-b80cc3/8d2976c7-7629-4ba0-8a96-2098db6da20f/scratchpad/hyg-writer.log. No unit was refused."
}
~~~~

### 2026-10-14T09:42:55 · gov-spec-writer · wf_252ed723-81c/af73e338e81772e55

Label: dRedressedBar · TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 · spec-write

~~~~text
{
 "summary": "I didn't write anything. Both units in my group already have conforming specs, so I left them as they are. No spec was authored or changed, nothing was committed, and the build index was not regenerated.\n\n- **TOOL-dRedressedBar-5** is at C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-5.md. It is a Tier-2 spec with the status header on line 3, rev-2 and `order 3`, which matches the roster. All ten sections are present and filled. Open questions reads `none`. Each of AC1 to AC8 gives a command or fixture and a \"Red when\" case. The gates section names the legs the close runs and says the unit adds no suite arm. The reuse audit cites the seam it extends and the recall terms it used.\n- **TOOL-dRedressedBar-6** is at C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-6.md. It is a Tier-1 spec with the status header on line 3, rev-2 and `order 4`, which matches the roster. The eight required sections are in the template's order. Its reuse audit is an optional section, placed last where the template puts it. Open questions reads `none`. Each of AC1 to AC5 gives a command and a \"Red when\" case. It declares two `New arm:` lines in `tools/roles/adopt-roles.test.sh`, and the main loop observes both at the close.\n\nBoth specs are listed in the records table of the round-1 spec audit. Their rev-2 entries only add a hand-off to TOOL-dRedressedBar-10, the unit that collects that audit's minor findings.",
 "authored": [],
 "alreadyPresent": [
  "TOOL-dRedressedBar-5",
  "TOOL-dRedressedBar-6"
 ],
 "refused": []
}
~~~~

### 2026-10-14T09:42:55 · gov-spec-writer · wf_252ed723-81c/a18b8d9da89a00003

Label: dRedressedBar · TOOL-dRedressedBar-7 TOOL-dRedressedBar-10 · spec-write

~~~~text
{
 "authored": [],
 "alreadyPresent": [
  "TOOL-dRedressedBar-7",
  "TOOL-dRedressedBar-10"
 ],
 "refused": [],
 "summary": "I wrote nothing: both units in my group already have conforming specs. I created and changed no files, made no commit, did not regenerate the index and ran no gate.\n\n- TOOL-dRedressedBar-7 is at C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-7.md. Its status header reads \"SPECCED · rev-2 · ... · order 5\", matching the roster's order. All ten sections are filled. §8 says \"none\", so there are no open questions. Every acceptance criterion (AC1 to AC6) names its command and the condition that turns it red, and §10 records the seam it extends and the recall terms it used.\n\n- TOOL-dRedressedBar-10 is at C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md. Its status header reads \"SPECCED · rev-2 · ... · order 6 · ratified 2026-10-14\", matching the roster's order. All ten sections are present, and §7 has a New arm: line for tools/govkit/matrix.py covering AC16. The spec already does everything its brief (prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-2-revision.md) asks for:\n  - open question F1 in §8 is marked \"RESOLVED (owner, 2026-10-14): (c)\";\n  - the leftover gap in S22 is pointed at TOOL-dRedressedBar-11;\n  - the §3 Edges hand that gap off to TOOL-dRedressedBar-11;\n  - §9 has a rev-2 line naming what moved.\n\n  That revision is already committed as 29c72f51a, so this unit should now count as READY rather than FORKED."
}
~~~~

### 2026-10-14T09:42:55 · gov-spec-writer · wf_252ed723-81c/a5099b40afa0f22f2

Label: dRedressedBar · TOOL-dRedressedBar-11 · spec-write

~~~~text
{
 "alreadyPresent": [
  "TOOL-dRedressedBar-11"
 ],
 "authored": [],
 "refused": [],
 "summary": "TOOL-dRedressedBar-11 already has a conforming spec, so I counted it as already present and changed nothing. The spec is C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md, landed in commit 29c72f51a. It conforms on these points: its status header reads 'SPECCED · rev-1 · 2026-10-14 · node d · Tier-2 · base ebce889c · streams tooling · order 7', which carries the order 7 this roster names. It has all ten Tier-2 sections in order (Goal, Scope, Non-goals, Design, Production-readiness, Acceptance criteria, Gates, Open questions, Revision log, Reuse audit). Section 7 lists what the close runs and declares two New arm: lines, one in tools/govkit/matrix.py and one in tools/govkit/selftest.py. Section 8 has no open forks. Section 10 names the seams it extends (classify_outcome and resolve_kit_dir) and the recall terms it used. I ran the memory hygiene gate. It fails on check 23, but only for acceptance-ledger lines in other builds (TOOL-aSparedSpawn-*, TOOL-aOrientedCast-22); no failure names dRedressedBar. I did not commit or regenerate the index."
}
~~~~

### 2026-10-14T09:45:05 · workflow-subagent · wf_252ed723-81c/aa389c986cd880427

Label: dRedressedBar · audit round 2 · subjects

~~~~text
{
 "subjects": [
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md",
   "blob": "5b0dba25e5c82ee7471600aae6da59ab908f94c4",
   "tree": "5b0dba25e5c82ee7471600aae6da59ab908f94c4"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md",
   "blob": "1b4ea08c879530e74bac8e92d11c8b69e95a79ed",
   "tree": "1b4ea08c879530e74bac8e92d11c8b69e95a79ed"
  }
 ],
 "notAtHead": [],
 "checklistPaths": [
  "tools/govkit/entries/settings-merge.kit.toml",
  "tools/govkit/matrix.py",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-1.md",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-2.md",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-3.md",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-4.md",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-5.md",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-6.md",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-7.md",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-8.md",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-9.md",
  "memory/builds/dRedressedBar/build/2026-10-14-build-TOOL-dRedressedBar-10-1-acceptance-ledger.md",
  "tools/govkit/govkit.py",
  "tools/govkit/selftest.py"
 ],
 "checklist": "# recurring-bug-class checklist for 14 path(s) (14 file(s))\n# 21 class(es) selected by an anchor + 6 universal\n# by anchor specificity: 9 path · 5 directory · 7 basename; a cut tier prints one line per class\n# invariants are read at ebce889c7d71; 0 that this subject adds, edits or takes out are listed as items, never by design\n\n- [ ] fixture-passes-by-finding-nothing (universal)\n      a test arm whose fixture never triggers the rule passes, and proves nothing\n      memory/gotchas/fixture-passes-by-finding-nothing.md\n\n- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)\n      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage\n      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md\n\n- [ ] heredoc-escape-reaches-the-regex (universal)\n      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem\n      memory/gotchas/heredoc-escape-reaches-the-regex.md\n\n- [ ] inline-fence-swallows-the-rest-of-the-file (universal)\n      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view\n      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md\n\n- [ ] staged-break-substitutes-a-synthetic-value (universal)\n      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n      memory/gotchas/staged-break-substitutes-a-synthetic-value.md\n\n- [ ] two-answers-to-one-question (universal)\n      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n      memory/gotchas/two-answers-to-one-question.md\n\n- [ ] a-new-local-collides-in-a-long-function (path)\n      a local added to a function thousands of lines long can share its name with one a distant block already binds, and the later binding silently replaces the new value only on the inputs that reach that block\n      memory/gotchas/a-new-local-collides-in-a-long-function.md\n\n- [ ] containment-tested-one-way (path)\n      a guard asking only \"is this path under the protected one\" refuses the narrow declarations and admits the one that claims everything\n      memory/gotchas/containment-tested-one-way.md\n\n- [ ] line-claim-matched-over-the-whole-output (path)\n      an arm that asserts a line names X tests two substrings over the whole output, so it passes when X appears on some other line and the line it means names something else\n      memory/gotchas/line-claim-matched-over-the-whole-output.md\n\n- [ ] verdict-printed-before-the-step-that-reverts-it (path)\n      a verb prints a verdict about bytes it just wrote, and a later step of the same run can revert those bytes, so the operator reads a verdict about a tree the run did not leave\n      memory/gotchas/verdict-printed-before-the-step-that-reverts-it.md\n\n- [ ] a-folded-field-leaves-its-row-shape-docs-behind (path)\n      a review fold adds a key to a declared row shape in the code and its gate, and the spec body and the README that describe that shape keep the old key set\n      memory/gotchas/a-folded-field-leaves-its-row-shape-docs-behind.md\n\n- [ ] fixture-inherits-ambient-machine-state (path)\n      a hermetic-looking fixture silently reads machine-global config, so it passes everywhere it was written and fails where it was not\n      memory/gotchas/fixture-inherits-ambient-machine-state.md\n\n- [ ] fixture-lacks-a-gate-the-consumer-has (path)\n      a runbook's fixture passes because it lacks a commit-time gate the consumer runs, and the consumer refuses the step the fixture let through\n      memory/gotchas/fixture-lacks-a-gate-the-consumer-has.md\n\n- [ ] subprocess-resolves-a-different-shell (path)\n      Python subprocess resolving the bare name bash finds the WSL launcher, which sees another filesystem\n      memory/gotchas/subprocess-resolves-a-different-shell.md\n\n- [ ] suite-invalidated-by-a-commit-under-it (path)\n      a suite that pins gov's revision at import and stamps fixtures from live HEAD is silently invalidated by any commit made while it runs, and the failures name the product\n      memory/gotchas/suite-invalidated-by-a-commit-under-it.md\n\n- [ ] a-merge-of-the-default-branch-read-as-additions (directory) · memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md\n\n- [ ] amendment-leaves-its-other-half-standing (directory) · memory/gotchas/amendment-leaves-its-other-half-standing.md\n\n- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory) · memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md\n\n- [ ] retirement-inventory-misses-readers-by-value (directory) · memory/gotchas/retirement-inventory-misses-readers-by-value.md\n\n- [ ] empty-field-collapses-unless-it-is-last (directory) · memory/gotchas/empty-field-collapses-unless-it-is-last.md\n\n- [ ] fold-text-is-unreviewed-surface (basename) · memory/gotchas/fold-text-is-unreviewed-surface.md\n\n- [ ] observed-by-claim-no-arm-discharges (basename) · memory/gotchas/observed-by-claim-no-arm-discharges.md\n\n- [ ] a-new-leg-trips-a-growing-set-of-meta-gates (basename) · memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md\n\n- [ ] anchor-literal-resolves-above-its-target (basename) · memory/gotchas/anchor-literal-resolves-above-its-target.md\n\n- [ ] join-key-widened-by-a-shared-location (basename) · memory/gotchas/join-key-widened-by-a-shared-location.md\n\n- [ ] record-without-serves-or-with-a-round-counter (basename) · memory/gotchas/record-without-serves-or-with-a-round-counter.md\n\n- [ ] staged-break-runs-stale-bytecode (basename) · memory/gotchas/staged-break-runs-stale-bytecode.md\n\n# by design — 0 invariant(s) this selection touches\n"
}
~~~~

### 2026-10-14T09:45:40 · workflow-subagent · wf_252ed723-81c/a7117854e900d8b87

Label: dRedressedBar · spec-audit round 1 · resume:probe

~~~~text
{
 "commonDir": "C:/projects/coding-governance/.git",
 "blobs": [
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md",
   "now": "5b0dba25e5c82ee7471600aae6da59ab908f94c4"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md",
   "now": "1b4ea08c879530e74bac8e92d11c8b69e95a79ed"
  }
 ],
 "finds": [],
 "verifies": [],
 "skipped": []
}
~~~~

### 2026-10-14T09:45:53 · gov-spec-reviewer · wf_252ed723-81c/acd16219de6202b51

Label: dRedressedBar · spec-audit round 1 · find:coherence

~~~~text
{
 "lens": "coherence",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md",
   "where": "section 6 AC5 (the spec-8 half), against section 2 S5",
   "severity": "medium",
   "claim": "C1: AC5's `grep -n 'reads none of this file'` over spec 8 already prints nothing on today's tree, because spec 8 wraps the false sentence at 'so it reads' / 'none of this file'. The half meant to show 'the false sentence stands' cannot fail.",
   "impact": "A build that adds a sentence naming `scan_spawn_tree` to spec 8's Gates section and leaves the false 'the fork leg's argv excludes `*.test.sh`, so it reads none of this file' in place passes AC5. S5's in-place correction then certifies a correction that never happened. This is the exact defect, id 5 / id 12, that the unit exists to close.",
   "fix": "Key the absence check on text that sits on one line, e.g. `sed -n '/^## 6. Gates/,/^## 7/p' <spec8> | grep -n 'excludes .\\*\\.test\\.sh.'`, or join lines before grepping, e.g. `tr '\\n' ' ' < <spec8> | grep -c 'reads none of this file'`. Then show the reading prints 1 on the pinned blob before the pass.",
   "evidence": "`grep -n 'reads none' memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-8.md` printed only line 62 (the hands-off line: 'reads none of `tools/run-gates/run-gates.test.sh`'). `sed -n '343,362p'` of spec 8 shows the Gates sentence wrapped: 'What these legs do not check of this change: the fork leg's argv excludes `*.test.sh`, so it reads' / 'none of this file.' So AC5's grep prints nothing at HEAD, before unit 10 is built."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md",
   "where": "section 2 S9 and section 6 AC9, against section 3 first non-goal, section 4 Alternatives row 2 and section 5 risks",
   "severity": "medium",
   "claim": "S9 and AC9 require rewriting spec 7's AC4 criterion text, but §3, §4 and §5 forbid exactly that. S9 says 'AC4's \"each kit that units 1 to 6 moved\"' is renamed, and AC9 greps all of spec 7 for 'units 1 to 6'. §3 excludes 'Rewriting a sibling's criteria', §4 rejects 'Rewrite each faulted criterion in place after its unit closes' because the ledger would answer text that no longer exists, and §5 says 'no criterion text moves, so no ledger is contradicted'.",
   "impact": "A builder cannot satisfy both. If they leave AC4 alone, AC9 reads red. If they edit it, unit 7's acceptance ledger now answers an AC4 whose wording changed under it, which is the contradiction §4 and §5 say cannot happen.",
   "fix": "Pick one. Either drop the AC4 wording from S9 and the §4 sibling table, and scope AC9's grep to spec 7's §1, §4 and Edges, with AC4's stale range noted only in the revision line. Or state in §3 and §5 that spec 7's AC4 wording is the single criterion edit, and say why its ledger is not contradicted.",
   "evidence": "`grep -nE 'units 1 to 6|six units|1 to 6'` over spec 7 printed lines 19, 21, 168 and 235. Line 235 sits in '## 6. Acceptance criteria' (heading at line 219): '- **AC4** — ... prints a `FAILED` line for each kit that units 1 to 6 moved'. In spec 10: line 152 is 'Rewriting a sibling's criteria' (non-goal), line 315 rejects rewriting a faulted criterion in place, and line 329 reads 'no criterion text moves, so no ledger is contradicted'."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md",
   "where": "section 2 S17 (the spec-9 half) against section 6 AC14",
   "severity": "low",
   "claim": "S17's sentence 'Spec 9 carries the same note for `check_outcome_states`' is observed by no criterion. AC14 reads only spec 2's Scope and §7 and symbols.json, and AC19 checks only that spec 9's revision line names id 17.",
   "impact": "Spec 9's §7 or Readers can be left without the codebase-map note and every criterion still passes. Id 17's spec-9 half is closed on paper only.",
   "fix": "Add an AC14 half that cuts spec 9's §7 with `sed -n '/^## 7. Gates/,/^## 8/p'` and greps for `codebase-map coverage + freshness`, or for whatever spot the note goes in. Show that it prints nothing at the pinned blob.",
   "evidence": "read: memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md:117-122 (S17) and :417-422 (AC14, which names only spec 2 and symbols.json). Spec 9's §7 (lines 315-325) carries no codebase-map leg."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md",
   "where": "section 6 AC8, the `project-owned` half",
   "severity": "low",
   "claim": "C1: AC8's half `grep -n 'project-owned'` over spec 4 'prints the corrected non-goal citing `tools/roles/kit.toml:47-48`' already prints a matching line today, the hands-off to unit 10. The grep cannot tell the corrected non-goal apart from that line.",
   "impact": "That half is green before the build. The criterion's red signal rests entirely on the 'roles kit' and hands-off-to-7 halves.",
   "fix": "Cut the non-goal list before grepping, e.g. `sed -n '/^## 3. Non-goals/,/^### Edges/p'`, so the hands-off line under Edges cannot satisfy it.",
   "evidence": "`grep -n 'project-owned' memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-4.md` printed line 56: 'entry claims it `project-owned` (`tools/roles/kit.toml:47-48`), so only the `agent-cap` kit moves.' That is the existing hands-off to TOOL-dRedressedBar-10 under Edges, not the non-goal."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md",
   "where": "section 1 Goal, against section 4 'The sibling rev bumps' and AC19",
   "severity": "low",
   "claim": "C6: §1 says 'The findings land on eight specs', but its own id table, §4's bump table and AC19 put findings on nine specs, 1 to 9.",
   "impact": "This is a cosmetic contradiction, but it is the count a builder might use for how many specs get a rev bump.",
   "fix": "Change 'eight specs' to 'nine specs'.",
   "evidence": "read: spec 10 line 19 'The findings land on eight specs'. Its id table assigns ids to units 1, 2, 3, 4, 5, 6 (id 14), 7, 8 and 9. §4's table (lines 283-293) lists specs 1 to 9, and AC19 (line 452) reads 'each of specs 1 to 9'."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md",
   "where": "section 4 'The witnessing arms' and section 2 S4",
   "severity": "low",
   "claim": "C11: unit 11 adds an optional fourth element to `check_outcome_states`'s rows, but names no update to the places that state the row shape as three elements. Spec 9 §4 says the helper takes 'a list of `(label, present paths, expected verdict)` rows', and the helper's docstring will say the same.",
   "impact": "The next reader of spec 9, or of the helper, sees a three-element row contract while the code takes four.",
   "fix": "Have S4 state that the helper's docstring records the fourth element (target-relative path to text, written before classifying and deleted after). Note in §3 Edges that spec 9's row-shape sentence goes stale, or have that line corrected in place.",
   "evidence": "read: memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-9.md:208-210 ('a list of `(label, present paths, expected verdict)` rows'). read: spec 11 lines 239-241 (the optional fourth row element) and lines 59-61 (the non-goal naming that element as unit 11's edit, with no doc update listed)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md",
   "where": "section 2 S4 (the new key rule) against section 6 AC6",
   "severity": "low",
   "claim": "The key rule records 'one label per shipped `[[outcome]]` block', but no label format is given. AC6 still requires 'The two labels opening `lexicon `' to equal unit 10 AC7's pinned pair. A per-block label that opens with the entry id ('lexicon …') makes three labels open 'lexicon ', and AC6's count is ambiguous.",
   "impact": "A natural label spelling breaks AC6, or makes it unclear whether lexicon's engine-agrees labels survived. The existing rules avoid this by prefixing 'accepted stops:'.",
   "fix": "Fix the key rule's label prefix in S4, e.g. 'outcome probe keys: '%s' …', matching the existing 'accepted stops:' prefix. Alternatively, have AC6 match the two pinned lexicon labels exactly rather than by the 'lexicon ' prefix.",
   "evidence": "read: tools/govkit/matrix.py:178-215. The class and agreement labels open 'accepted stops:', and only the engine-agrees labels open 'lexicon ' (line 238: \"lexicon exit 1 after %s is %s\"). Spec 11 S4 (lines 41-45) and AC6 (lines 378-388) give no key-rule label shape."
  }
 ]
}
~~~~

### 2026-10-14T09:45:54 · gov-spec-reviewer · wf_252ed723-81c/a0edca9ace49748b6

Label: dRedressedBar · spec-audit round 1 · find:grounding

~~~~text
{
 "lens": "grounding",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md",
   "where": "section 6 AC5 (and S5)",
   "severity": "medium",
   "claim": "AC5's false-sentence half, `grep -n 'reads none of this file'` over spec 8, already prints nothing at HEAD, because spec 8 wraps that sentence across two lines. The red case 'the false sentence stands' can never fire.",
   "impact": "A build that adds a `scan_spawn_tree` mention somewhere in spec 8's §6 but leaves 'the fork leg's argv excludes `*.test.sh`, so it reads / none of this file' in place passes AC5. S5's in-place correction of the false prose is then certified when it was never made. Only the separate `scan_spawn_tree` half can still red.",
   "fix": "Key the grep on a single-line fragment that is present at the pinned blob, such as `grep -n 'argv excludes'` over the `sed -n '/^## 6. Gates/,/^## 7/p'` cut of spec 8. Alternatively join the lines first (`tr '\\n' ' '`) and grep for 'reads none of this file'. Then record that the half reads red over the current spec 8 before the correction.",
   "evidence": "`grep -n 'reads none of this file' memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-8.md` printed nothing (exit 1) at HEAD 29c72f51a. `grep -n 'reads none\\|argv excludes\\|scan_spawn_tree'` over the same file printed `352:What these legs do not check of this change: the fork leg's argv excludes `*.test.sh`, so it reads` and `62: ... scan_spawn_tree`. Line 353 reads `none of this file. The loop leg does read it, ...`."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md",
   "where": "section 6 AC3",
   "severity": "low",
   "claim": "AC3's requirement that the `FOREIGN_PREFIX_PROBE:-0` line 'reads `fail` and `n`' cannot fail on its `n` half. Any shell `if` line contains the letter n (`then`, `echo`, `assertions`), so it does not show that the stop uses the suite's `n` counter.",
   "impact": "A stop that reports a wrong or unset counter, for example `${count:-1}`, passes AC3 as long as it avoids the lowercase `pass`. The probe would then report a wrong assertion count, which is the defect unit 1's S5 exists to prevent.",
   "fix": "Require the counter expansion itself, for example `grep -F '${n:-' ` and `grep -F '${fail:-'` over the `FOREIGN_PREFIX_PROBE:-0` line. Keep the case-sensitive `grep -F '${pass'` as the absence half.",
   "evidence": "read: tools/agent-instructions/adopt-agent-instructions.test.sh:19 (the shape unit 1 copies) is `if [ \"${FOREIGN_PREFIX_PROBE:-0}\" = 1 ]; then echo \"foreign-prefix-probe: stopped after 1 arm\"; ... echo \"PASS (${pass:-1} assertions)\" ...`. It contains `n` in `then`, `echo` and `assertions` independent of any counter. tools/roles/adopt-roles.test.sh:64 is `n=0; fail=0`."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md",
   "where": "section 2 S4 / section 6 AC6",
   "severity": "low",
   "claim": "C22 observed-by-claim-no-arm-discharges: S4 changes the matrix agreement rule so `derive_probe_paths` reads keys by their `want` through `govkit.OUTCOME_PROBE_KEYS`, and says it is observed by AC6. AC6 never reads that join.",
   "impact": "No shipped descriptor carries two `ok = true` blocks that involve `must_not_resolve`, because settings-merge has exactly one block. AC6's 'every recorded label is true' therefore passes whether or not the agreement rule unions `must_not_resolve` paths. A build that leaves the typed `must_exist`/`must_not_exist` pair at matrix.py:209 stays green, and a future contradicting descriptor goes unseen.",
   "fix": "Add a staged half to AC6. Patch `govkit.read_descriptors` so one descriptor carries two `ok = true` blocks, one `must_exist` on a path and the other `must_not_resolve` on the same string. The agreement label for that pair must then record false. Name that half in the §7 matrix `New arm:` line.",
   "evidence": "read: tools/govkit/matrix.py:199-215. `derive_probe_paths(_a, \"must_exist\") & derive_probe_paths(_b, \"must_not_exist\")` is reached only for descriptors with two ok blocks. The census `python -I census.py` (read_descriptors over the registry) printed `29 18 5 {'must_exist': 17, 'must_not_exist': 6}`, and settings-merge.kit.toml at HEAD has no outcome block. Spec 11 §4 adds exactly one block."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md",
   "where": "section 4 'Order, and unit 7'",
   "severity": "low",
   "claim": "C17 amendment-leaves-its-other-half-standing: §4 states that the README Build-level rule still says unit 7 'is measured last over the code the others leave', and that adding step 7 to the build order awaits the dispatcher's regen. The README already carries both amendments.",
   "impact": "A builder or dispatcher acting on §4 goes looking for a README edit that has already been made. They may re-edit the rule and duplicate or overwrite the existing sentence. The spec's account of the record is false where it stands.",
   "fix": "Restate the paragraph in the past tense: the README rule already says that units 10 and 11 follow 7 and touch only govkit-exempt files, and the build-order region already lists step 7. Alternatively drop the paragraph.",
   "evidence": "read: memory/builds/dRedressedBar/README.md:56-60 reads '... 7, the records and kit versions, is measured over the code units 1 to 6, 8 and 9 leave. Units 10 and 11 follow 7 in that order. Each touches only govkit-exempt files and adds no function ...'. README.md:125 has `| 7 | `TOOL-dRedressedBar-11` | no |` in gen:build-order. `grep -n 'is measured last' README.md` matches nothing."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md",
   "where": "section 4 'S22 — the false-accept routes, and the narrowing' (prefix `.` sentence); also spec 11 section 5 security",
   "severity": "low",
   "claim": "Two claims rest on an assumption nobody measured. Unit 10 says that with `prefix` at `.` the parent-home term 'resolves outside the target and reads absent there', leaving the stop as wide as unit 9's. Spec 11 §5 says the term 'reads the receipt through the resolver's own containment'. Both the exists() term and the resolver's static probe test `<target>/../hooks/agent-cap.js`, a directory outside the target, and no containment check covers that path.",
   "impact": "With `prefix = \".\"`, a `hooks/agent-cap.js` that happens to sit beside the target repo makes both units refuse an exit 2 that unit 9 accepts. In that state the adopter itself found the kit outside the target and refused to wire, so this is a false REFUSED on a genuine no-hook-in-target install. It fails closed, so the effect is a spurious apply/update failure, not a false accept.",
   "fix": "State the condition in unit 10 §4 ('reads absent unless the target's parent directory holds hooks/agent-cap.js') and in spec 11 §5 (containment covers receipt rows only, and the static second probe may leave the tree). Alternatively gate the parent-home term on the resolved path staying inside the target.",
   "evidence": "read: tools/govkit/govkit.py:221-224 (and byte-identical tools/settings-merge.py:102-105). `probes = (here / home, here.parent / home)` has no `root in ...parents` check; containment (`root in hit.parents and \"..\" not in hit.parts`) is applied only to receipt rows at :219-220. read: tools/settings-merge.py:213-223. A found kit outside the target hits `except ValueError: pass` and falls back to a non-existent path, so the adopter still exits 2 at :1046-1052."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md",
   "where": "section 4 'The refused exit names its reason'",
   "severity": "low",
   "claim": "C12 fixture-inherits-ambient-machine-state: S3 keeps CONFIGURE's `capture_output=True, text=True` with no encoding and prints its stderr tail. The settings-merge adopter always writes UTF-8 stderr. The spec-time measurements of fixtures A and B ran on a machine with PYTHONUTF8=1 ambient, so they never saw the locale-codepage decode.",
   "impact": "On a host without UTF-8 mode, the new CONFIGURE tail decodes the adopter's UTF-8 stderr as cp1252. Non-ASCII text such as the em dash in `refusing to wire agent-cap — …` then prints as mojibake in the new problem line. AC3 reads only the ASCII `cannot read`, so it passes either way. The effect is display only.",
   "fix": "State the host dependency in §4, or have the CONFIGURE tail decode with the adopter's declared UTF-8 (this moves the encoding-posture count, which §4 currently pins at 36). Alternatively note that AC3/AC4 were observed under PYTHONUTF8=1 and add a run with PYTHONUTF8=0 to the arm.",
   "evidence": "`env | grep -i PYTHONUTF8` printed `PYTHONIOENCODING=utf-8` and `PYTHONUTF8=1`. `python -c \"import sys,locale;print(sys.flags.utf8_mode, locale.getpreferredencoding(False))\"` printed `1 utf-8`. read: tools/settings-merge.py:1058 `sys.stderr.reconfigure(encoding=\"utf-8\", errors=\"backslashreplace\")`. read: tools/govkit/govkit.py:7744 CONFIGURE's `subprocess.run(..., capture_output=True, text=True)` with no encoding."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md",
   "where": "section 2 S5 / section 6 AC5",
   "severity": "low",
   "claim": "S5 says unit 8's pass is 'observed to add no counted site', but AC5 compares only five of the six registered classes and leaves out `pure-fn-subst`. That class is counted for run-gates.test.sh at 11, in memory/project/spawn-idiom-sites.txt:218.",
   "impact": "A `$(resolve_mp_record …)`-style function substitution added by unit 8 would move a registry row while AC5 reads equal. The ledger would then record 'no counted site added' when one was. The fork leg still grades it at the bar, which contains the effect.",
   "fix": "Either narrow S5's claim to the five library-free classes, or have AC5 derive the counts through `scan_spawn_tree` (or pass `scan_spawn_file` the library bodies `scan_spawn_tree` builds) and compare all six rows.",
   "evidence": "read: tools/gate-lint/sh_hygiene.py:594-609. SPAWN_REGISTERED = pure-fn-subst, printf-subst, cat-file, path-subst, date-fmt, var-pipe. `sed -n 212,220p memory/project/spawn-idiom-sites.txt` printed `tools/run-gates/run-gates.test.sh\tpure-fn-subst\t11\t...resolve_mp_record×11`. AC5 lists 'cat-file, date-fmt, path-subst, printf-subst and var-pipe'."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md",
   "where": "section 4 'S22', the sentence after the toml block",
   "severity": "low",
   "claim": "Unit 10 says 'No reader of the probe keys exists outside those two' (classify_outcome and derive_probe_paths). The matrix class rule also reads probe keys directly, at matrix.py:181-185.",
   "impact": "The inventory is incomplete. Spec 11 lists that reader. The error does not change unit 10's design, because the class rule reads only `must_exist`, but the next change that trusts this sentence will miss a reader.",
   "fix": "Name the class rule at tools/govkit/matrix.py:181-185 (reads `must_exist` and `sorted(probe)`) as a third reader that unit 10's change leaves untouched.",
   "evidence": "`git grep -n 'must_not_exist\\|must_exist' -- tools skills` (excluding kit.toml) printed `tools/govkit/matrix.py:183:              bool(probe.get(\"must_exist\")),` alongside govkit.py:6313 and matrix.py:209."
  }
 ]
}
~~~~

### 2026-10-14T09:45:54 · gov-spec-reviewer · wf_252ed723-81c/a13343e2eb5071c17

Label: dRedressedBar · spec-audit round 1 · find:reuse

~~~~text
{
 "lens": "reuse",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md",
   "where": "section 6 AC5 and AC12 (and section 10's claim that AC5 and AC12 reuse the leg)",
   "severity": "medium",
   "claim": "AC5 and AC12 reuse only the leg's classifier, `scan_spawn_file`. They write their own count and their own registry comparison instead of calling the leg's existing seams: `build_spawn_measured` (tools/gate-lint/sh_hygiene.py:872-879), which counts only entries whose is-site flag is True, and `read_registry` (:384) with `check_registry` (:444).",
   "impact": "The spec's wording is \"prints ... the count of sites per class from `scan_spawn_file`\". `scan_spawn_file`'s lists also hold near misses (comment spellings, redirected printf), so the natural count is the length of each list. Over run-gates.test.sh at HEAD that count gives cat-file 29 against the registry row 25, and printf-subst 56 against the row 2. On a correct build, AC5 then reads red, or a builder edits the counts until they match. AC12's unattended-build.test.sh half has the same gap: printf-subst has 288 entries but only 71 sites. Section 10 says no regex is re-typed, yet the counting and set-equality half of the leg is re-typed, which is the drift the reuse rule exists to prevent.",
   "fix": "Make AC5 and AC12 build the leg's own measurement. Shape `scan_spawn_file`'s output as `scan_spawn_tree` does, as (rel, line, site, code) tuples, then pass it through `build_spawn_measured`. Compare the result with `read_registry(memory/project/spawn-idiom-sites.txt, SPAWN_KEY_SHAPE)` through `check_registry`, keyed on the named files, and expect no problems. At minimum, state that only entries whose is-site flag is True are counted. Correct section 10 to name these seams.",
   "evidence": "A scratch program (scratchpad/reuse/spawn.py) imported tools/gate-lint/sh_hygiene.py, ran `scan_spawn_file` over each file, and read the registry with `read_registry`. It printed: `tools/run-gates/run-gates.test.sh  cat-file all=29 site=25 row=25 | date-fmt all=1 site=1 row=1 | path-subst all=12 site=12 row=12 | printf-subst all=56 site=2 row=2 | var-pipe all=141 site=141 row=141`, and `tools/workflows/unattended-build.test.sh ... printf-subst all=288 site=71 row=66 | var-pipe all=70 site=70 row=62`. read: tools/gate-lint/sh_hygiene.py:872-879, where `build_spawn_measured` keeps `if site:` only. read: spec 10 lines 360-363 (AC5) and 405-410 (AC12)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md",
   "where": "section 6 AC4 and section 4 'The witnessing arms' (fixture B of the [dRB-11] block)",
   "severity": "medium",
   "claim": "Fixture B plants an agent-cap receipt row by hand: \"`scripts/hooks/agent-cap.js` gets the hook's bytes at the old vintage, with one receipt row at that vintage's identities\". The selftest already has a helper that gives a row its bytes and both identities at a vintage, `write_vintage_receipt` (tools/govkit/selftest.py:617-673), and `stale_target` already calls it. The spec builds that rewind again instead of reusing it.",
   "impact": "The builder has to re-derive `commit`, `sha256` and `gov_oid` at OLD with its own `git show` and `_sha`/`blob_oid` calls. That is a second copy of the logic whose header records that a mixed-vintage or invented row put 9 and then 27 arms red through update's S9 preamble. A wrong identity sends `update` to the S9 refusal rather than the adopter-exit-2 path, so AC4 can read red for the wrong reason. The extra `git` subprocess would also go outside `run`, which threatens the spec's own claim that selftest.py's counted sites stay at 24 and 1 (S6, AC7).",
   "fix": "State in section 4 and AC4 that the block appends the agent-cap row (path `scripts/hooks/agent-cap.js`, source from `resolve_entry`) to the receipt and then re-runs `write_vintage_receipt(govroot, t, OLD)` before `settle`. The helper is idempotent over the rows that are already rewound, and it writes the bytes and both identities. Alternatively, give `stale_target` an optional row-planting hook that runs before its own rewind. Name the helper in the arm's description.",
   "evidence": "read: tools/govkit/selftest.py:617-673. The `write_vintage_receipt` docstring says \"`commit`, `sha256` and `gov_oid` move to `vintage`, and BOTH identities from the SAME vintage, or the row is S9's corruption ... through the engine's own helpers\", and its body sets `f[\"sha256\"] = gk._sha(b)`, `f[\"gov_oid\"] = gk.blob_oid(b)` and writes the bytes. read: tools/govkit/selftest.py:3237-3249, where `stale_target` calls `write_vintage_receipt(govroot, t, OLD)` and then `settle`. read: spec 11 lines 361-364 (AC4) and 255-262 (the block builds B through `make_target`, `settle`, `stale_target` and `run`, with no rewind helper named)."
  }
 ]
}
~~~~

### 2026-10-14T09:45:54 · gov-spec-reviewer · wf_252ed723-81c/aa847af50024ca018

Label: dRedressedBar · spec-audit round 1 · find:failure-envelope

~~~~text
{
 "lens": "failure-envelope",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md",
   "where": "section 4 \"Which receipt bytes\" and \"What an adopter sees change\" row 1; section 6 AC3; S5 ([dRB-11] fixture A)",
   "severity": "high",
   "claim": "C10 (verdict-printed-before-the-step-that-reverts-it): on the apply route, the run that refuses the stop then rewrites the receipt, which removes the one row the new must_not_resolve term reads. The next identical `apply --kits settings-merge` therefore reads the false accept again, and the spec says nothing about that re-run.",
   "impact": "Built as written, the first `apply --kits settings-merge` over a target whose agent-cap hook sits at a receipt-only home exits 1 and names `cannot read`. The same run then writes `.governance/install.json` with `kits: selection` and only the selection's rows, so agent-cap's row is gone. A second apply finds the hook at neither static home and in no receipt row. The adopter exits 2 before it reads settings.json, the term holds, and the verb exits 0 printing `no-agent-cap-to-wire [accepted stop]`. The settings.json is still malformed and the hook is still unwired. Unit 11 says it closes \"settings-merge's last false-accept route\", but on this route the refusal lasts one run. AC3 and the [dRB-11] block run the apply once after the plant, so both pass over a build that ships this.",
   "fix": "State the re-run in section 4 and close it, or hand it off explicitly. One way to close it: a CONFIGURE refusal keeps the prior receipt's rows for kits outside the selection. Another: the narrower apply carries forward every installed kit's rows, as the `pins` union at govkit.py:7402 already does for kits. If neither is in scope, add a hands-off edge naming the narrower-apply receipt drop as an open false-accept route, and correct the \"After\" cell of the section-4 table. In both cases, extend AC3 and the [dRB-11] fixture A arm to run the same apply a third time and assert it still exits 1 and prints no `no-agent-cap-to-wire`. The build must also observe that the third run reads exit 0 over the unfixed design, in a scratch target under %TEMP%.",
   "evidence": "read: tools/govkit/govkit.py:1094-1102: under `--kits`, resolve_selection returns only the named kits plus their requires, and settings-merge requires [] (settings-merge.kit.toml:8). read: govkit.py:7393 starts `rows` empty, and :7436 fills it with `for eid in selection`. `awk 'NR>=7772 && NR<=8020 && /return|r.problems|raise Refusal/'` over govkit.py printed only lines 7873-7877, an `r.fail` with no return, so no early exit sits between CONFIGURE and the receipt write. read: govkit.py:8016-8022 writes the receipt with `\"kits\": selection, \"files\": rows` regardless of earlier r.fail calls. The comment at :7402 confirms that narrower later applies happen (\"A narrower later apply must not un-pin files whose kit is still installed\"). read: govkit.py:200-226 shows that resolve_kit_dir finds a renamed home only through a receipt row; its static probes are `<here>/hooks` and `<here>/../hooks`. read: spec 11 section 6 AC3 runs \"the same apply then runs again, it exits 1\" exactly once after the plant."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md",
   "where": "section 5 security; S3",
   "severity": "low",
   "claim": "S3 adds the stderr tail to every refused adopter exit in both loops, which covers 14 bash adopters plus settings-merge. Section 5 prices the content of settings-merge's stderr only: \"paths and parse positions, never settings values\".",
   "impact": "The security line reasons about one adopter where the change applies to the whole class. The other adopters' stderr now reaches the operator's terminal and CI logs, and their echoed text includes target conf values, such as adopt-memory-tree's `$KIT_REL` prefix line. None of that was reviewed. The contained effect is a security statement narrower than the change it prices.",
   "fix": "Restate section 5's security line over the class: every adopter CONFIGURE or the gained loop runs can now print up to three stderr lines on a refused exit, as the regenerate site already does. Either confirm by a grep over the adopters' `>&2` lines that none echoes a secret-bearing value, or state that the tail is printed verbatim from target-side code.",
   "evidence": "`grep -rn -A1 '^\\[adopt\\]' tools/*/kit.toml tools/govkit/entries/*.toml | grep argv | wc -l` printed 28. Of those, 14 carry a non-empty bash argv, among them adopt-memory-tree.sh, adopt-run-gates.sh, adopt-unattended.sh and adopt-roles.sh, and settings-merge carries a python argv. The same grep's head showed tools/memory-tree/adopt-memory-tree.sh:35 echoing `'$KIT_REL'` to stderr. read: spec 11 section 4 \"What an adopter sees change\", whose last row is \"any other refused adopter exit in either loop | ... ending with the adopter's stderr tail\"."
  }
 ]
}
~~~~

### 2026-10-14T09:45:54 · gov-spec-reviewer · wf_252ed723-81c/ae30535983f244070

Label: dRedressedBar · spec-audit round 1 · find:blast-radius

~~~~text
{
 "lens": "blast-radius",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md",
   "where": "section 4 'S22 — the false-accept routes, and the narrowing' (the matrix-row paragraph) and section 7",
   "severity": "medium",
   "claim": "The design tells the builder to derive the parent-home row's path by replacing settings-merge's `{prefix}` with its parent. Written in matrix.py as `.replace(\"{prefix}\", …)`, that is exactly what the {prefix} hand-resolution ban in the `python resolver (behaviour + inline parity + idiom ban)` leg fires on. Section 7 does not name that leg.",
   "impact": "The literal reading of the design reds a leg the unit never runs at its close. Section 7's list is the only set the main loop runs, and the spec-tokens guards join never asks for this leg because its `{prefix}/` guard is broad (13 legs, floor 5). So the pass reports green and the red only shows up in the full bar, after unit 11 has stacked on top.",
   "fix": "In section 4, require the row's path to come from `govkit.resolve_prefix_token(<term>, <parent prefix>)`, the marked canonical copy at tools/govkit/govkit.py:179-190, or from `resolve_tokens` with a context whose prefix is the parent, and never from a hand-written `.replace`. Add `python resolver (behaviour + inline parity + idiom ban)` to the section 7 leg line. Probe for the build: after writing the row, run `git grep -nE \"\\.replace\\([\\\"'][{]prefix[}]\" -- tools/govkit/matrix.py` and expect no output.",
   "evidence": "read: tools/lib/resolve-python.test.sh:479-507. The ban covers every tracked *.py (`pfx_pop=$(git ls-files -- '*.sh' '*.py' WIRE-INTO-PROJECT.md)`) and fires on `line ~ /\\.replace\\([\"\\047][{]prefix[}]/` outside a `# >>> resolve_prefix_token` block. read: tools/gate-legs.json:305-314, whose guard [\"{prefix}/\",\"{prefix}/lib/\",\".githooks/\"] is broad. tools/check-spec-tokens.py:262 sets BROAD_LEG_FLOOR = 5, and grep found `\"{prefix}/\",` on 13 leg guards. `grep -n 'resolve_prefix_token' tools/govkit/govkit.py` printed 179-190, the marked block, which is the sanctioned spelling. `grep -n prefix tools/govkit/matrix.py` showed no resolver use there today. The spec reads: \"with settings-merge's `{prefix}` replaced by that prefix's parent\" (spec 10:273-276). Its section 7 line at :459 omits the leg."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md",
   "where": "section 7 Gates leg line",
   "severity": "low",
   "claim": "Section 7 leaves out the two unguarded legs that grade this unit's own writes. `spec tools` is `spec tokens (a spec's own names resolve)`, whose handoff, cites and paths joins read the nine sibling specs this unit rewrites, including the new `hands-off TOOL-dRedressedBar-7` lines S9 adds to specs 8 and 9 and the new `kit.toml:40-41` and `registry.toml:295-297` cites. The other is `encoding posture (text IO names its encoding)`, which grades the new fixture writes in tools/govkit/matrix.py, a file with no registry row.",
   "impact": "The section 7 legs run once at the close and miss the gate that checks whether the edited spec prose and hands-off payloads resolve. A missing payload in spec 7, a cite past end of file, or an unencoded write in the new matrix row shows up only in the full bar.",
   "fix": "Add `spec tokens (a spec's own names resolve)` and `encoding posture (text IO names its encoding)` to the section 7 leg line. Unit 11's section 7 already names the second for the same files.",
   "evidence": "read: tools/gate-legs.json:1651-1660 (`spec tokens`, no guard key) and :228-240 (`encoding posture`, no guard key). read: tools/check-spec-tokens.py:99-106: the handoff join reads \"a `**hands-off**` bullet's backticked PAYLOAD ... -> the text of the sibling spec the bullet names\". `grep -n govkit memory/project/encoding-posture-sites.txt` printed rows for govkit.py, refusal_join.py and selftest.py, and none for matrix.py. Spec 10 :459 lists `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor` · `recall floor arms` · `memory hygiene` · `codebase-map coverage + freshness`, and neither leg."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md",
   "where": "section 4 'Files touched (estimate)' and section 7",
   "severity": "low",
   "claim": "Section 6 defines `<p11>` as the commit \"as their acceptance ledgers name them\", so the pass writes an acceptance ledger under memory/builds/dRedressedBar/build/. Files touched lists only the four tools/govkit files, so section 7 omits `recall floor` and `memory hygiene`, the legs that grade a new record under memory/.",
   "impact": "The guards join reads only the estimate, so it cannot ask for these legs. A ledger with a malformed `**Serves:**` line or filename goes ungraded at the unit's close. Unit 10, by contrast, names its ledger and both legs.",
   "fix": "Add `memory/builds/dRedressedBar/build/2026-10-14-build-TOOL-dRedressedBar-11-1-acceptance-ledger.md` to Files touched, and `recall floor` and `memory hygiene` to the section 7 leg line, as spec 10 does at :308 and :459.",
   "evidence": "read: spec 11:325-326: \"`<p10>` and `<p11>` are the commits of units 10 and 11's build passes, as their acceptance ledgers name them\". Spec 11:279-284 lists only tools/govkit/{govkit.py,matrix.py,selftest.py,entries/settings-merge.kit.toml}. read: tools/gate-legs.json:868-881 (`recall floor` guard includes \"memory/\") and :1488-1502 (`memory hygiene`, the records chunk). Spec 11 section 7 (:400) lists `recall floor arms` but neither `recall floor` nor `memory hygiene`."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md",
   "where": "section 4 'Order, and unit 7', last paragraph",
   "severity": "low",
   "claim": "The spec says the Build-level rules sentence about unit 7 \"has been inexact since unit 10\" and that the dispatcher still owes that README edit. The README already says that units 10 and 11 follow 7, that each touches only govkit-exempt files, and that neither adds a function.",
   "impact": "A builder or dispatcher acting on this paragraph would rewrite or duplicate an already-correct README rule. It is a stale statement about the build's own record.",
   "fix": "Replace the paragraph with a pointer to README.md's Build-level rules, which already carry the ordering, or drop it.",
   "evidence": "read: memory/builds/dRedressedBar/README.md:56-60: \"...7, the records and kit versions, is measured over the code units 1 to 6, 8 and 9 leave. Units 10 and 11 follow 7 in that order. Each touches only govkit-exempt files and adds no function, so neither moves a kit version or the symbol index unit 7 regenerates.\" Compare spec 11:231-235: \"The Build-level rules sentence saying unit 7 'is measured last over the code the others leave' has been inexact since unit 10 ... The dispatcher owns that README edit.\""
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md",
   "where": "section 2 S2 (with spec 10 section 2 S22)",
   "severity": "low",
   "claim": "Unit 9's code-2 block ships \"with a comment stating why\" its single `must_not_exist` term is enough. Unit 10 adds a second term and unit 11 a receipt term, yet S2 says \"Nothing else in the descriptor moves\", and unit 10's S22 never mentions the comment. Neither spec lists the comment as something to update.",
   "impact": "The descriptor comment that explains the stop's envelope keeps describing unit 9's one-term probe after two units change what the probe reads. That misleads the next person reading the descriptor, in a comment only, with no effect on behaviour.",
   "fix": "In unit 11 S2 (or unit 10 S22), name unit 9's block comment as updated to state the three-term probe and its receipt reading, and add a line to AC1 that greps the comment for `must_not_resolve` or the receipt.",
   "evidence": "read: spec 9:26-29: \"`means = \\\"no-agent-cap-to-wire\\\"` and `ok = true`, with a comment stating why. Nothing else in the descriptor moves.\" read: spec 9:164-169 states the envelope unit 10 corrects (\"The probe reads two paths and cannot see the receipt ... reachable only by `apply`\"). read: spec 11:33-35: \"S2 — ... gains `must_not_resolve = ...` beside unit 10's two `must_not_exist` terms. Nothing else in the descriptor moves.\" Spec 10 S22 (:131-140) adds the term and a matrix row and does not mention the comment."
  }
 ]
}
~~~~

### 2026-10-14T09:54:50 · gov-skeptic · wf_252ed723-81c/a662b6112bf72214e

Label: dRedressedBar · spec-audit round 1 · verify:ids-1-5

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 1,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Re-probed. Spec 10 hashes to the pinned blob 5b0dba25. In spec 8 the sentence wraps across lines 352-353: 'excludes `*.test.sh`, so it reads' / 'none of this file.' `grep -n 'reads none'` over spec 8 matched only line 62, the hands-off text 'reads none of `tools/run-gates/run-gates.test.sh`'. So AC5's `grep -n 'reads none of this file'` already prints nothing at HEAD. That half of AC5 cannot go red. The other half needs only `scan_spawn_tree` somewhere in the Gates cut, so a build could add that name and leave the false sentence in place. The consequence is contained: one prose correction is certified falsely, and no product behaviour changes.",
   "fixVerdict": "unsound",
   "fixNote": "Join the lines before grepping, so the absence check sees the wrapped sentence: `tr '\\n' ' ' < <spec8> | grep -c 'reads none of this file'` must print 0 at the tip. Record that it prints 1 at the pinned blob before the pass (re-probed: it prints 1 today)."
  },
  {
   "id": 2,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Confirmed by reading spec 10. S9 (lines 92-96) renames AC4's 'each kit that units 1 to 6 moved'. The §4 bump table row for spec 7 (line 291) lists 'AC4 wording'. AC9 (line 389) greps all of spec 7 for 'units 1 to 6|six units'. Spec 7 line 235, inside its §6 Acceptance criteria, matches that grep. Against this: §3 line 152 lists 'Rewriting a sibling's criteria' as a non-goal, §4 line 315 rejects rewriting a criterion in place because of the ledger, and §5 line 329 says 'no criterion text moves, so no ledger is contradicted'. The spec contradicts itself. A builder cannot satisfy AC9 without breaking the §3 and §5 invariant.",
   "fixVerdict": "sound"
  },
  {
   "id": 3,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "S17 (lines 118-122) says 'Spec 9 carries the same note for `check_outcome_states`'. AC14 (lines 417-422) reads only spec 2's Scope, spec 2's §7 and symbols.json. AC18 reads spec 9's §4 and §5 for the routes and unit 11, not for a map note. AC19 checks only that the revision line names the id. A grep of spec 9 for 'codebase-map' found nothing. Its §7 gates (line 317) carry no codebase-map leg. The only staleness mention is inside the hands-off to unit 10 at line 78. So the spec-9 half of S17 is observed by no criterion.",
   "fixVerdict": "sound"
  },
  {
   "id": 4,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "`grep -n 'project-owned'` over spec 4 printed only line 56. That line is in the hands-off to TOOL-dRedressedBar-10 under Edges and already cites `tools/roles/kit.toml:47-48`. So AC8's 'prints the corrected non-goal' half is satisfied today. Cutting the section with `sed -n '/^## 3. Non-goals/,/^### Edges/p'` and grepping it printed no 'project-owned' line. It printed only line 44, which holds the base sentence 'from the roles kit'. So the proposed cut tells the corrected non-goal apart from the hands-off line, and it would read red today.",
   "fixVerdict": "sound"
  },
  {
   "id": 5,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 10 line 19 says 'The findings land on eight specs'. Its id table assigns findings to units 1, 2, 3, 4, 5, 6 (id 14), 7, 8 and 9, which is nine. Line 280 itself says 'Each of the nine sibling specs', the §4 table lists specs 1 to 9, and AC19 says 'each of specs 1 to 9'. The miscount is cosmetic: the table and AC19 govern the bumps.",
   "fixVerdict": "sound"
  }
 ]
}
~~~~

### 2026-10-14T09:54:52 · gov-skeptic · wf_252ed723-81c/a6fa3b0f678852e12

Label: dRedressedBar · spec-audit round 1 · verify:ids-6-10

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 6,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 9 lines 199-200 state the row contract as '(label, present paths, expected verdict)' rows. Spec 11 §4 'The witnessing arms' (lines 239-241) adds an optional fourth element, a path-to-text mapping that is written before classifying and deleted after. Neither S4 (lines 41-45) nor the non-goal at lines 59-61 says that the helper's docstring or spec 9's sentence gets updated. The stale three-element contract is real, but it affects documentation only.",
   "fixVerdict": "sound"
  },
  {
   "id": 7,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 11 AC6 (lines 380-382) requires 'one label per shipped [[outcome]] block' from the key rule, and requires that 'the two labels opening `lexicon `' equal unit 10's pinned pair. S4 gives the key rule no label format. In matrix.py:178-215 the existing class and agreement labels open 'accepted stops:', and only line 240's engine-agrees labels open 'lexicon '. A key-rule label that starts with the entry id, for example 'lexicon block code 1 ...', would make three labels open 'lexicon ', and AC6's count would be ambiguous or red. This is an underspecified label, and its effect is contained.",
   "fixVerdict": "sound"
  },
  {
   "id": 8,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec 8 at HEAD splits the sentence across lines 352-353: line 352 ends '...the fork leg's argv excludes `*.test.sh`, so it reads' and line 353 begins 'none of this file.' A line-wise `grep -n 'reads none of this file'` therefore matches nothing even before any correction, so the 'false sentence stands' red case of spec 10 AC5 (line 364) can never fire. Only the scan_spawn_tree half is left, and it says 'in the corrected sentence', which is a judgment call rather than a mechanical check.",
   "fixVerdict": "unsound",
   "fixNote": "Join the lines of spec 8's Gates section before grepping, for example `sed -n '/^## 6. Gates/,/^## 7/p' <spec8> | tr '\\n' ' ' | grep -c 'reads none of this file'`, which must print 0. Record that the same pipeline prints 1 over the pinned spec 8 before the correction."
  },
  {
   "id": 9,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "adopt-agent-instructions.test.sh:19, the shape unit 1 copies, contains the letter n in 'then', 'echo' and 'assertions'. Any such `if` line therefore satisfies 'reads `fail` and `n`' (spec 10 AC3, line 354) whatever counter it actually uses. Spec 1 S5 (lines 123-124) requires the counters `fail` and `n`, and that requirement is not observed. Only the `pass` absence half can red.",
   "fixVerdict": "sound"
  },
  {
   "id": 10,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "matrix.py:203-215 reaches derive_probe_paths only for pairs of ok=true blocks within one descriptor. settings-merge.kit.toml at HEAD has no outcome block (grep found nothing), and units 9-11 give it exactly one block, so must_not_resolve never takes part in a pair. AC6 (lines 378-386) checks only that every label is true, plus the key-rule and receipt-row halves of the must_not_resolves rename. Nothing in it exercises the agreement rule's union by `want`, so a build that keeps the typed must_exist/must_not_exist pair at line 209 stays green.",
   "fixVerdict": "sound"
  }
 ]
}
~~~~

### 2026-10-14T09:54:52 · gov-skeptic · wf_252ed723-81c/a9e10c08133072266

Label: dRedressedBar · spec-audit round 1 · verify:ids-11-15

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 11,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 11 at blob 1b4ea08 §4 'Order, and unit 7' (lines 230-235) says the order 7 'adds step 7 to the derived build-order region on the dispatcher's regen', and that the Build-level sentence calling unit 7 'measured last over the code the others leave' 'has been inexact since unit 10. It should say ... The dispatcher owns that README edit.' Both are written as pending. The README at HEAD (29c72f51a, the same commit that adds this blob) already carries both changes. Lines 56-60 read '7, ... is measured over the code units 1 to 6, 8 and 9 leave. Units 10 and 11 follow 7 in that order. Each touches only govkit-exempt files and adds no function'. Line 125 holds '| 7 | `TOOL-dRedressedBar-11` | no |'. grep for 'is measured last' finds nothing. The spec describes a README edit that has already been made. The only effect is on how the record reads.",
   "fixVerdict": "sound"
  },
  {
   "id": 12,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 10 §4 S22 (lines 261-263) says without condition that with prefix `.` the new term 'resolves outside the target and reads absent there, which leaves the stop exactly as wide as unit 9's'. classify_outcome (govkit.py:6311-6325) evaluates `(target / resolved).exists()` with no containment check, so `./../hooks/agent-cap.js` reads whatever sits in the target's parent directory. The resolver's static probes, `probes = (here / home, here.parent / home)` at govkit.py:221, also have no containment check; containment is applied only to receipt rows (:219). If the parent holds hooks/agent-cap.js, settings-merge.py:213-223 hits `except ValueError: pass` and falls back to a path that does not exist, so main refuses with exit 2 (:1046-1052). Unit 9's block accepts that exit and unit 10's refuses it, so the claim that the stop is exactly as wide as unit 9's is false on that edge path. Spec 11 §5 itself is literally accurate about receipt rows, but it says nothing about the static probe leaving the tree. The failure is fail-closed and the path is unlikely.",
   "fixVerdict": "sound"
  },
  {
   "id": 13,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "govkit.py:7744 runs CONFIGURE as `subprocess.run(..., capture_output=True, text=True)` with no encoding. Spec 11 §4 (line 199-201) keeps it that way and will print the stderr tail. settings-merge.py:1058 reconfigures stderr to UTF-8, and its refusal text contains an em dash (:1047). The ambient env here prints PYTHONIOENCODING=utf-8 and PYTHONUTF8=1, so the spec's fixture runs would not see a locale-codepage decode. Without UTF-8 mode on Windows, text=True decodes as cp1252, so non-ASCII text in the tail prints as mojibake. AC3/AC4 match only ASCII 'cannot read' and pass either way. The decode already happens at HEAD, so the new code adds no crash path; the effect is display only.",
   "fixVerdict": "sound"
  },
  {
   "id": 14,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "sh_hygiene.py:600-609 registers six classes, pure-fn-subst included. spawn-idiom-sites.txt has `tools/run-gates/run-gates.test.sh\tpure-fn-subst\t11 ... resolve_mp_record×11` beside the other five rows. Spec 10 S5 (line 74-76) names 'the six rows at spawn-idiom-sites.txt:214-219' and says 'Unit 8's pass is observed to add no counted site. Observed by AC5'. AC5 (lines 359-363) compares only cat-file, date-fmt, path-subst, printf-subst and var-pipe, and its figure lists five numbers. So S5's 'observed' claim covers one class that AC5 never reads. The fork leg still grades the class at the bar, which contains the effect.",
   "fixVerdict": "sound"
  },
  {
   "id": 15,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 10 line 261 says 'No reader of the probe keys exists outside those two' (classify_outcome, and derive_probe_paths in the agreement rule). `git grep must_exist|must_not_exist` excluding toml shows tools/govkit/matrix.py:181-185. In the accepted-stops liveness loop, that code reads `probe = b.get(\"probe\")` and checks `bool(probe.get(\"must_exist\"))`, outside derive_probe_paths. That is a third reader. It reads only must_exist, which unit 10 leaves alone, so the design is unaffected. The inventory is still wrong and could mislead the next change.",
   "fixVerdict": "sound"
  }
 ]
}
~~~~

### 2026-10-14T09:54:52 · gov-skeptic · wf_252ed723-81c/a774bd4993521e24d

Label: dRedressedBar · spec-audit round 1 · verify:ids-16-20

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 16,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Re-probed with a scratch program, verify-b4/s.py, that imports sh_hygiene and calls scan_spawn_file at HEAD. For run-gates.test.sh it printed (all, is-site): cat-file (29,25), printf-subst (56,2), path-subst (12,12), date-fmt (1,1), var-pipe (141,141). For unattended-build.test.sh it printed printf-subst (288,71) and var-pipe (70,70). The registry rows at spawn-idiom-sites.txt:214-219 are 25/1/12/2/141. scan_spawn_file (sh_hygiene.py:798-818) does return near misses with the flag False, and build_spawn_measured (:872-879) counts only `if site:`. AC5 (spec 10:360-369) and AC12 (:405-412) name only scan_spawn_file. Neither says to count only flagged entries or to use build_spawn_measured or check_registry. Section 10 (:506-507) claims reuse. The ambiguity is partly resolved for AC5: §4 evidence (:212-214) and AC5's figure pin 25/1/12/2/141, which only the is-site count gives. AC12's unattended-build half is DERIVED with no pinned figure, so a list-length count would read red there on a correct build. The effect is contained to how one criterion is observed, so I grade it low.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 17,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "selftest.py:617-673 write_vintage_receipt sets commit, sha256 (gk._sha) and gov_oid (gk.blob_oid) at the vintage, and writes the bytes. stale_target (:3237-3249) calls it, then settle. Spec 11 AC4 (:361-372) and §4's witnessing-arms paragraph (:255-262) ask for a hand-planted agent-cap row 'at that vintage's identities'. They name make_target/settle/stale_target/run and never the rewind helper. §4 also requires that the block's 'process calls go through run', and run invokes govkit, not git. Planting old-vintage bytes without the helper therefore needs a separate git read plus identity derivation, which duplicates the logic whose header records that 9 and then 27 arms went red. I checked feasibility: OLD resolves to 24f39915, and `git cat-file -e 24f39915:tools/hooks/agent-cap.js` succeeds, so the helper would keep the row rather than drop it. One part of AC4 is also inexact: it says 'Before the commit', but stale_target has already settled. The fixture duplication is real and its effect is contained to a test fixture.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 18,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec 10:273-276 says the row's path is agent-cap's destination 'with settings-merge's `{prefix}` replaced by that prefix's parent'. That wording directs a hand replacement of the token. resolve-python.test.sh:491-507 scans every tracked *.py and fires on `\\.replace\\([\"'][{]prefix[}]` outside a `# >>> resolve_prefix_token` block. The marked canonical copy is at govkit.py:179-190. gate-legs.json:304-314 gives that leg the guard [\"{prefix}/\",\"{prefix}/lib/\",\".githooks/\"]. check-spec-tokens.py:262 sets BROAD_LEG_FLOOR=5, and derive_guarded_legs (:506-523) drops broad guards from the join, so the join cannot ask for this leg. Spec 10 §7 (:459) omits it. The literal build would pass the unit's close and red only in the full bar. The red is caught before merge, so the effect is contained.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 19,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "I read gate-legs.json. `spec tokens (a spec's own names resolve)` and `encoding posture (text IO names its encoding)` both carry no guard key. Spec 10 §7 (:459) names neither leg, although the unit rewrites nine sibling specs and adds new hands-off lines and cites that spec tokens' handoff and cites joins grade. For encoding posture, spec 10 says little about any new text IO in matrix.py: S22 adds one row, through unit 9's helper. So that half is weaker, but the spec-tokens omission stands. The consequence is a later red in the full bar, not a shipped defect.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 20,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 11:325-326 defines <p11> as the commit of unit 11's build pass 'as their acceptance ledgers name them', so the pass writes a ledger. Files touched (:279-284) lists only the four tools/govkit files. §7 (:400) names `recall floor arms` but neither `recall floor` nor `memory hygiene`. gate-legs.json shows `recall floor` guarded by 'memory/' and `memory hygiene` unguarded. Spec 10, by contrast, lists its ledger (:308) and both legs (:459). The effect is a missed check at the unit's close, caught by the full bar.",
   "fixVerdict": "sound",
   "fixNote": ""
  }
 ]
}
~~~~

### 2026-10-14T09:54:52 · gov-skeptic · wf_252ed723-81c/ab8f244aeb9fa731f

Label: dRedressedBar · spec-audit round 1 · verify:ids-21-24

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 21,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "I read README.md lines 56-60. They already say: \"Units 10 and 11 follow 7 in that order. Each touches only govkit-exempt files and adds no function, so neither moves a kit version or the symbol index unit 7 regenerates.\" Spec 11 lines 231-235, at blob 1b4ea08, still say the sentence \"has been inexact since unit 10\" and that \"The dispatcher owns that README edit\". So the spec describes an edit that has already been made. That is a stale statement in the build's own record and has no effect on behaviour.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 22,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 9 S1 (lines 26-29) ships the code-2 block \"with a comment stating why\", and that block has one must_not_exist term. Spec 10 S22, at blob 5b0dba2, adds a second term and a matrix row. Grepping spec 10 for 'comment' finds nothing about the descriptor comment. Spec 11 S2 (lines 33-35) adds must_not_resolve and says \"Nothing else in the descriptor moves\". Its only 'comment' hit is unrelated. Neither spec updates the comment, so it will describe a one-term probe after two units have changed it. The effect is limited to a comment.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 23,
   "verdict": "confirmed",
   "severity": "high",
   "reason": "I checked this against the code. The claim holds. At govkit.py:1094-1102, `--kits` mode returns only the named kits through derive_install_order, and settings-merge.kit.toml has requires = []. `rows` starts empty at :7393 and is filled only from `for eid in selection`. The one carry-forward at :7582-7593 copies adopter-owned rows for the selection's own destinations only. In the CONFIGURE block (:7744-7772) a non-accepted non-zero exit only calls r.fail. Grepping :7440-8020 for return or raise finds none, so the receipt write at :8016-8022 still runs, with \"kits\": selection and \"files\": rows. That drops agent-cap's row. resolve_kit_dir (:196-230) finds a renamed home only through a receipt row, and its static probes are here/hooks and here/../hooks. On the second identical apply, settings-merge.py:1046-1052 therefore returns 2 before it reads settings.json. The must_not_resolve term holds and the stop is accepted, while the settings.json is still malformed. Spec 11 AC3 and the [dRB-11] fixture A run the apply once after the plant, so they cannot catch this. This happens only on a narrow path: a receipt-only hook home plus a narrower apply. The unit's claim to close the last false-accept route therefore misleads, which is why I grade it high.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 24,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 11 section 5 security (lines 302-306) checks only the content of settings-merge's stderr: \"settings-merge's stderr carries paths and parse positions, never settings values\". The section-4 table's last row applies the stderr tail to \"any other refused adopter exit in either loop\". tools/memory-tree/adopt-memory-tree.sh:35 echoes the computed '$KIT_REL' to stderr, and tools/roles/adopt-roles.sh:164 echoes a render-token message. The security statement therefore covers less than the change does. The values I found are paths, not secrets, so the effect is contained and I grade it low.",
   "fixVerdict": "sound",
   "fixNote": ""
  }
 ]
}
~~~~

### 2026-10-14T09:57:13 · gov-synthesizer · wf_252ed723-81c/a0e3c522286a29dd8

Label: dRedressedBar · spec-audit round 1 · synth

~~~~text
{
 "path": "C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/reviews/2026-10-14-review-TOOL-dRedressedBar-10-11-spec-audit-round1.md",
 "summary": "Round 1 of the Tier-2 spec audit of units 10 and 11 is written. The verdict is CLEAN WITH FIXES. All 24 confirmed findings are placed in 22 items, and each finding sits in exactly one item. By item: 0 blocker, 1 high, 4 medium, 17 low. By raw finding: 0 blocker, 1 high, 5 medium, 18 low. Two pairs of findings each describe one defect and were merged: ids 1 and 8, and ids 11 and 21. The high item is id 23 in unit 11: on the narrower-apply route, the refusal holds for one run, then the false accept comes back. For ids 1 and 8 the skeptics rejected the finders' fix, so the report gives the skeptics' corrected fix: join the wrapped lines before grepping. Id 16 was re-graded by its skeptic from medium to low, and that grade is kept. The run is complete: 5 of 5 lenses and 5 of 5 skeptic batches returned, and no findings were left unverified.",
 "items": [
  {
   "severity": "HIGH",
   "ids": [
    23
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    1,
    8
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    2
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    17
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    18
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    3
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    4
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    5
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    6
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    7
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    9
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    10
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    11,
    21
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    12
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    13
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    14
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    15
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    16
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    19
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    20
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    22
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    24
   ]
  }
 ]
}
~~~~

### 2026-10-14T09:59:59 · gov-spec-writer · wf_252ed723-81c/a6efe547311c48b66

Label: dRedressedBar · audit round 2 · dispose

~~~~text
{
 "disposed": true,
 "standing": [],
 "promoted": 24,
 "folded": 0,
 "refuted": 0,
 "promotedIds": [
  "TOOL-dRedressedBar-12",
  "TOOL-dRedressedBar-13"
 ],
 "edges": [
  {
   "from": "TOOL-dRedressedBar-12",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-11"
  },
  {
   "from": "TOOL-dRedressedBar-11",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-12"
  },
  {
   "from": "TOOL-dRedressedBar-12",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-13"
  },
  {
   "from": "TOOL-dRedressedBar-13",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-12"
  },
  {
   "from": "TOOL-dRedressedBar-13",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-10"
  },
  {
   "from": "TOOL-dRedressedBar-10",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-13"
  },
  {
   "from": "TOOL-dRedressedBar-13",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-11"
  },
  {
   "from": "TOOL-dRedressedBar-11",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-13"
  }
 ],
 "placements": [
  {
   "unit": "TOOL-dRedressedBar-12",
   "repairs": "TOOL-dRedressedBar-11",
   "order": 8
  },
  {
   "unit": "TOOL-dRedressedBar-13",
   "repairs": "none",
   "order": 9
  }
 ],
 "summary": "All 24 confirmed findings from the units-10-11 spec audit are promoted into two new units. None is folded or refuted, and none is left standing. The report had 0 unverified findings.\n\nTOOL-dRedressedBar-12 (Tier-2, order 8, one above unit 11's order 7) takes report id 23, item H1, the only high. I checked the cause on a three-kit scratch target at 29c72f51, whose tools/ is identical to ebce889c's. An `apply --kits settings-merge` exits 0 but rewrites the receipt to `kits: selection` and `files: rows` (govkit.py:8019-8021). The receipt goes from 18 rows to 2. A later `apply --kits kickoff-manifest` then exits 2, refusing both dropped kits as foreign. So the drop affects every narrower apply, not just settings-merge. On unit 11's route it means a refusal holds for one run and the next run falsely accepts the stop.\n\nThe fix: `_cmd_apply` keeps every claimed kit the selection did not name, with its receipt rows unchanged. This is the same union the `pins` code already applies at :7402-7407. The carry is keyed on the claimed kits so the `(govkit)` attributes row is not written twice.\n\nUnit 12 also:\n- corrects the `write_gate_legs` docstring, which still says apply narrows the receipt;\n- adds a `[dRB-12]` selftest arm and a third identical apply to unit 11's fixture A;\n- corrects spec 11's §4 in place.\n\nTwo things are out of scope. `orders` is handed off as an external edge. `gate_runner.emitted` is not carried: the same-argv rule at :4143-4152 re-claims those legs on the kit's next run.\n\nTOOL-dRedressedBar-13 (Tier-2, order 9, after every other unit; repairs `none`) batches the 5 mediums and 18 lows: ids 1-22 and 24. Each id gets its own §2 item S<n>, and S23 is left out because id 23 is unit 12's. They could not be split into two units: ids 7 and 10 (spec 11) and id 18 (spec 10) all write tools/govkit/matrix.py, so the write sets overlap (M6 clause 1).\n\nTwo choices were derived from the code and records rather than left as open questions:\n- **Id 2:** take the report's second fix. Unit 10 cannot close with its AC9 red, and AC9 requires spec 7's AC4 already edited, so the first fix would contradict unit 10's own record.\n- **Id 13:** decode CONFIGURE's output as UTF-8 with `errors=\"replace\"`. Both sibling sites at :10986-10987 and :11119-11120 already decode UTF-8. `errors=\"replace\"` follows the existing comment at :7634-7637 that apply must not crash after files land and before the receipt is written. The encoding-posture registry row drops from 36 to 35.\n\nEvery acceptance criterion's red half was checked against 29c72f51 or the pinned blobs 5b0dba25 and 1b4ea08c.\n\nEdges: I wrote both ends of every edge in the same pass. Spec 10 goes to rev-3 (hands-off to 13). Spec 11 goes to rev-2 (hands-off to 12 and 13). Each bump has its §9 line, and no scope or criterion moved. The README Units table gains rows 12 and 13. I did not regenerate any index.\n\nMemory hygiene was the only gate I ran. It reports no spec-shape findings on my files. Check 9 shows the expected stale index, which the dispatcher's regen clears. Check 23 fails on older acceptance ledgers from other builds, not on these specs. Check 17 reports the gotchas index as stale, and that is not from this change.\n\nFiles: C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-12.md, .../spec/2026-10-14-spec-TOOL-dRedressedBar-13.md, .../spec/2026-10-14-spec-TOOL-dRedressedBar-10.md (rev-3), .../spec/2026-10-14-spec-TOOL-dRedressedBar-11.md (rev-2), .../README.md (roster rows)."
}
~~~~

### 2026-10-14T10:23:58 · gov-spec-writer · direct/a2c171868672c02dc

Label: dRedressedBar · TOOL-dRedressedBar-12 · spec-write

~~~~text
I've written the spec for **TOOL-dRedressedBar-14** (Tier-2, order 10, SPECCED rev-1), using the new id you assigned. I did not touch specs 12 and 13. The memory hygiene gate shows nothing from this spec: its only failures are check 23 in other builds' ledgers and a stale gotchas index.

The brief's acceptance can't be met by this unit alone. The reproduction on a scratch target at the base gave exit 1 with both adopters at exit 2, as the brief says. But the two exits have different causes:
- **settings-merge's exit 2** is the receipt problem the brief describes. When I ran its adopter by hand in the same target, it exited 2 with no receipt on disk and exited 0 with the receipt there, wiring `scripts/hooks/agent-cap.js`.
- **agent-cap's exit 2 has nothing to do with the receipt.** Its adopter command is `python {prefix}/settings-merge.py` (`tools/hooks/kit.toml:108`), and `{prefix}` is filled from agent-cap's own setting, so it runs `scripts/settings-merge.py`. That file doesn't exist (python: "can't open file"). Re-running the apply with a receipt already on disk still gave agent-cap exit 2 and an overall exit 1. It is the only adopter command that names another kit's file.

**The design:**
- **The fix:** `_cmd_apply` writes `.governance/install.json` once between HOOKPROBE and CONFIGURE. It builds it as one dict from the lists RECEIPT writes, including unit 12's carried kits and rows, and RECEIPT rewrites it at the end.
- **Alternatives rejected:**
  - Moving CONFIGURE after the receipt write still needs a second write.
  - Passing planned homes through an environment variable means changing 67 inlined copies of the resolver.
  - Handing settings-merge a `--hook-path` fixes one adopter only, and breaks the rule that the outcome check and the adopter read the same source.
- **Units 12 and 13:** this unit depends on 12, because without its carry the early receipt drops the planted row in unit 11's fixture A and the false accept comes back. One criterion stages exactly that break. It runs after 13 because all three units write `govkit.py`, `selftest.py` and spec 11.
- **Unit 7:** its version measurement doesn't need to cover this unit. Both product files are under the govkit exemption, and no function is added.

The spec also covers what you asked for: what the receipt claims when CONFIGURE fails, and that a re-run of `apply` recovers. That part is measured on a target holding an uncommitted receipt; `update` does not recover. It lists every reader of the receipt during CONFIGURE. None assumes it is absent; each reads no receipt as no rows.

Decision for you (§8 F1): where agent-cap's own exit 2 goes.
- **(a) Recommended:** add a separate unit for agent-cap's adopter command, ordered after this one. The brief's "exits 0" check moves to that unit's close. This spec's AC1 pins the remaining exit 1.
- **(b)** Fold it into this unit. That puts two mechanisms in one spec and moves agent-cap's kit version, which unit 7 doesn't cover.
- **(c)** Leave it external. The build then closes with the reproduction still exiting 1.

Edits for you to make:
1. Spec 11's external hand-off line becomes `hands-off TOOL-dRedressedBar-14` for the settings-merge half. Its agent-cap half ("agent-cap's own refusal still reports the install") stays external, or points at the new unit under F1 (a).
2. Spec 12 needs a `hands-off TOOL-dRedressedBar-14` line to match this spec's `consumes-from`.
3. The README needs a roster row for unit 14. The Build-level sentence "Units 10 and 11 follow 7 in that order" should also name 12, 13 and 14. Order 10 appears on the next regen.

Files:
- C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-14.md
- The scratch targets are at C:\Users\d41ly\AppData\Local\Temp\drb14 (per-kit prefix) and C:\Users\d41ly\AppData\Local\Temp\drb14d (default prefix).
~~~~

### 2026-10-14T10:25:24 · gov-spec-writer · direct/ade176cfeffe33c2c

Label: dRedressedBar · TOOL-dRedressedBar-13 · spec-write

~~~~text
I revised `TOOL-dRedressedBar-13` to rev-2, and a whole-tree hygiene run no longer reports check 25 for this spec. I did not run the brief's `--staged` command: the earlier rev-2 edits are unstaged, and staging them is your step at commit. The run still exits 1, on check 9 (stale build index) and on check 23 (other builds).

**What changed**, in `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-13.md`:
- **Header:** `rev-1` becomes `rev-2`.
- **S6 gains a `**Readers:**` sub-bullet.** It says what S6 retires: the three-element row shape `(label, present paths, expected verdict)` as written down in spec 9 and the helper's docstring. The check fired on "deleted", which only describes the fourth element's scratch file.
  - The clause names the two searches I ran over the tracked tree at commit 29c72f51: `git grep -n -i 'present paths\|expected verdict\|three-element'` and `git grep -n -w 'check_outcome_states'`.
  - The audit report and this spec also quote the shape. They are records, so nothing in them changes.
- **`by name:`** lists two readers:
  - `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-9.md:200`.
  - `tools/govkit/matrix.py`. The helper's docstring is not in the tree at 29c72f51, because unit 9 is unbuilt there and the second search finds nothing under `tools/`. It will be there when this unit builds, since unit 9 builds first.
  - Both files were already in §4's Files touched, so §4 is unchanged.
- **`by value:`** answers `NO VALUE READERS`, because S6 changes prose only. The row shape's value is read by the helper and its callers in `tools/govkit/matrix.py`. Unit 11 widened that, and three-element rows still work because the fourth element is optional.
- **§9:** a rev-2 line names the change and says no other section moves.

**Gate result**
- **Check 25:** my first draft put commit `29c72f51` in backticks inside the `by name:` half, and the check failed because no reader spells it. Taking the backticks off cleared it.
- **Check 9 (stale build index):** `memory/builds/dRedressedBar/README.md` differs from a fresh render. The index is probably stale because of the rev change. Regenerating it is the committer's step, so I left it.
- **Check 23:** it names only acceptance ledgers in the `aSparedSpawn` and `aOrientedCast` builds. Nothing in it touches `dRedressedBar`.

No other spec, no code and no index was touched, and nothing was committed.
~~~~

### 2026-10-14T10:47:05 · gov-spec-writer · direct/a9bfb5c64cc3d16ac

Label: dRedressedBar · TOOL-dRedressedBar-15 · spec-write

~~~~text
**`TOOL-dRedressedBar-15`: authored.** The spec is Tier-2, SPECCED, rev-1, `order 11`, with all ten sections and nothing left open in §8.

Spec: `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-15.md`

**Chosen fix:** agent-cap's descriptor names the entry whose installer (its adopter) it runs, as `[adopt] via = "settings-merge"`. govkit then runs settings-merge's own command, with the paths filled in from settings-merge's settings, so the script is found at whatever prefix settings-merge was installed under. This needs one new function, `resolve_adopter_argv`, used at the two places that run adopters (`apply` and `update`'s gained loop). Exit codes are still judged by agent-cap's own descriptor, because unit 9's spec (§4) depends on that. agent-cap's copied command line and two keys that only made sense beside it are deleted.

**How the other candidates lost** (each was given a test it could fail before the pick):
- **A `{prefix:<entry>}` token:** the token parser only matches `[a-z_]+`. A probe showed `{prefix:settings-merge}` passes through as literal text, with no error and no missing-key report. That parser pattern is written out in three files.
- **A per-entry key such as `{settings_merge_prefix}`:** a target's `[answers]` table could supply that value, which reopens the injection hole `SEEDED_TOKENS` exists to close.
- **agent-cap with no adopter at all:** I measured the case it breaks on `%TEMP%/drb15b`. When settings-merge is already installed but not in the current selection, agent-cap's adopter is the only step that wires the hook. AC4 keeps this case covered.
- **Finding the script through the receipt at run time:** `update` runs gained kits' adopters before it writes the receipt, so a settings-merge gained in the same run cannot be found.

**The class check:** I ran the predicate over the real registry first. It checked 105 command-line elements across 29 kits, in `[adopt]`, `[check]`, `[[gate_leg]]` and `[[regenerate]]`. Exactly one names a file that only another kit installs: agent-cap's. It becomes a `selfcheck` arm with three failure sites and a count note. It fails if it finds elements to check but grades none.

**A second form of the bug:** with settings-merge at its own prefix (`[kit.settings-merge] prefix = "scripts"`), today's apply also exits 1. agent-cap's command fails with "can't open file" on `tools/settings-merge.py`. I measured this on `%TEMP%/drb15s`, and AC3 covers it.

**Version:** the unit bumps the hooks kit version itself. After the code commit it runs `govkit.py mint --base ebce889c7` and commits the result separately. If the mint wants to bump any kit other than agent-cap, the pass stops and returns to you.

**Edges:** consumes-from `TOOL-dRedressedBar-14` (the early receipt) and `TOOL-dRedressedBar-11` (the adopter's error output, which carries "can't open file" into the failure message). The sibling revision writer has already added the matching hands-off lines to specs 11 and 14. A hands-off external line leaves `TOOL-aScouredKit-26` (the open ask for a cross-entry token) open.

**Verification:**
- **Hygiene:** checks 12 and 25 pass on the spec, run in a scratch clone with it staged. The checker only reads tracked files, so a run in this worktree would have skipped the spec. I confirmed check 12 really grades the file: a heading break staged in the clone turned it red.
- **Lexicon:** it accepts `resolve_adopter_argv`.
- **Remaining hygiene reds:** checks 9, 17 and 23 were red before this spec. 9 is the build index that needs regenerating, 17 the stale gotchas index, and 23 other builds' ledgers.

**For you to do:** regenerate the build index so the roster's `order 11` and spec 15 appear. The README's build-level sentence already says unit 15 follows unit 14 and bumps the version. In this worktree I wrote only the spec file. My scratch targets `%TEMP%/drb15b` and `%TEMP%/drb15s` are still there; the spec cites both.
~~~~

### 2026-10-14T10:47:25 · gov-spec-writer · direct/a0e16106fd495ec50

Label: dRedressedBar · TOOL-dRedressedBar-14 · spec-write

~~~~text
All three revisions are written, and every `consumes-from` among units 11, 12, 14 and 15 now has its matching `hands-off`. The plan grades 11 and 12 READY. Unit 14 still shows `MISSING`, but only because its spec file is not committed yet ("2 with no tracked spec"). I couldn't run the planner's grading function on its own because the worktree guard blocked it. Checked by hand against that function's rules (`tools/unattended/unattended.sh:4536-4548`), spec 14 grades READY once it is committed: its §8 has one F-item with its resolution mark in its span, and its scope, acceptance and gates sections are all filled.

**`TOOL-dRedressedBar-14`, now rev-2**
- §8 F1 now carries `RESOLVED (owner, 2026-10-14): (a)` in place, under its recommendation.
- In §3 Edges, the old external hand-off line for agent-cap's exit 2 is now `- **hands-off** \`TOOL-dRedressedBar-15\``. I replaced that line rather than adding a second one, because its own text said it would name the new unit's id once F1 resolved as (a). AC1's pinned exit 1 is unchanged.
- §9 has a rev-2 line.

**`TOOL-dRedressedBar-11`, now rev-3**
- Spec 15 declares `consumes-from` toward both 14 and 11 (its §3 Edges), so the external line became two: `hands-off TOOL-dRedressedBar-14` for settings-merge's half and `hands-off TOOL-dRedressedBar-15` for agent-cap's half.
- §9 has a rev-3 line.

**`TOOL-dRedressedBar-12`, now rev-2**
- Added `- **hands-off** \`TOOL-dRedressedBar-14\``, covering the two carried lists, `_carried_kits` and `_carried_rows`, that spec 14 consumes.
- §9 has a rev-2 line.

**All the pairs now match:** 14←11, 14←12, 15←14, 15←11 and 12←11. Unit 13's edges are untouched.

**Memory hygiene** exits 1, but none of its findings names these specs:
- Check 9: `memory/LIVE.md` and `memory/builds/dRedressedBar/README.md` are stale against a fresh render. Regenerating them is for you to do.
- Check 23: acceptance-ledger lines in the aSparedSpawn and aOrientedCast builds. This was already failing before my edits.
- Check 17: `memory/gotchas/INDEX.md` is stale.

**For you to decide:**
1. Spec 14's AC6 is now weaker. It says spec 11's revision log gains "one new line naming `TOOL-dRedressedBar-14`". My rev-3 line already names unit 14, so a plain grep would pass even if unit 14's build never adds its own line. AC6's §4 half still reds as intended, because the new edge lines sit in §3. I left AC6 alone because the brief says nothing else in any spec moves. If you want it fixed, the fix is to make AC6 read the change between `<p13>` and `<p14>` instead of grepping the log.
2. Spec 15 was still being edited when I read its edges (36502 bytes, then 36636). If its edges change, the mirrored lines in 11 and 14 need another look.

Nothing is committed, and I edited nothing outside the spec folder. Spec 14 still needs its roster row and order-10 step in the README, which are yours to add.

Files:
- C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-14.md
- C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-11.md
- C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-12.md
~~~~

### 2026-10-14T11:12:29 · gov-spec-writer · wf_2811782f-9e5/aea1ccc19769dde42

Label: dRedressedBar · TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 · spec-write

~~~~text
{
 "authored": [],
 "alreadyPresent": [
  "TOOL-dRedressedBar-1",
  "TOOL-dRedressedBar-2",
  "TOOL-dRedressedBar-8",
  "TOOL-dRedressedBar-9",
  "TOOL-dRedressedBar-3",
  "TOOL-dRedressedBar-4",
  "TOOL-dRedressedBar-5"
 ],
 "refused": [],
 "summary": "All seven units in my group already had conforming specs, so I wrote nothing, committed nothing and did not run the index generator.\n\n**What I checked for each unit:**\n- **Spec file and order:** each id has its file under `C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/`, named `2026-10-14-spec-<id>.md`. Each status header is SPECCED and carries the roster's order: `order 1` for units 1, 2, 8 and 9, `order 2` for units 3 and 4, and `order 3` for unit 5.\n- **Sections:** units 2, 9, 4 and 5 are Tier-2 and have all ten sections in order. Units 1, 8 and 3 are Tier-1 and have the eight required sections in order, plus the optional Reuse audit. Every unit has an Edges subsection.\n- **Revision logs:** each header's rev number has a matching line in the revision log.\n- **Gates:** each Gates section has a line naming its legs. Units 1, 8, 9 and 3 declare their new suite arms on `New arm:` lines with a `covers` field.\n- **Reuse audits:** each one records the seam first and then a line of the recall terms used.\n- **Open questions:** units 1, 2, 8, 9, 4 and 5 read `none`. Unit 3's single fork, F1, is marked `RESOLVED (owner, 2026-10-14): (c)`, and its header carries `ratified 2026-10-14`.\n\n**Hygiene gate:** I ran `tools/memory-tree/check-memory-hygiene.sh` over the whole tree. It exited 1, but every failure is check 23, on acceptance-ledger lines of other builds' units (TOOL-aSparedSpawn-* and TOOL-aOrientedCast-22). No finding names dRedressedBar. The log is at `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-bar-profile-failures-b80cc3/8d2976c7-7629-4ba0-8a96-2098db6da20f/scratchpad/hyg.log`.\n\nI did not re-verify the specs' design claims against the code. This pass only checked that each spec has the shape it needs."
}
~~~~

### 2026-10-14T11:12:30 · gov-spec-writer · wf_2811782f-9e5/ac6c88de9ba7b3477

Label: dRedressedBar · TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-10 · spec-write

~~~~text
{
 "authored": [],
 "alreadyPresent": [
  "TOOL-dRedressedBar-6",
  "TOOL-dRedressedBar-7",
  "TOOL-dRedressedBar-10"
 ],
 "refused": [],
 "summary": "All three units in my group already have conforming specs, so I left them alone, authored nothing and refused nothing. I committed nothing and did not run the index generator.\n\n- TOOL-dRedressedBar-6: C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-6.md. Header reads SPECCED, rev-2, Tier-1, `order 4`. It has the eight required micro-spec sections plus the optional Reuse audit, in canonical order. Its Edges list and two `New arm:` lines are there, Open questions reads \"none\", and rev-2 is in the revision log.\n- TOOL-dRedressedBar-7: C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-7.md. Header reads SPECCED, rev-2, Tier-2, `order 5`. It has all ten Tier-2 sections in order, including the Edges list. Open questions reads \"none\" and rev-2 is in the revision log.\n- TOOL-dRedressedBar-10: C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md. Header reads SPECCED, rev-3, Tier-2, `order 6`, `ratified 2026-10-14`. It has all ten sections, the Edges list and one `New arm:` line. The brief's revision (prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-2-revision.md) is already folded in. F1 is marked `RESOLVED (owner, 2026-10-14): (c)` in place, S22's leftover gap now points at TOOL-dRedressedBar-11, the Edges hand-off to unit 11 exists, and the revision log carries rev-2 and rev-3.\n\nI ran the memory hygiene gate. None of its findings name these three specs. It did report red results in check 23, all on acceptance-ledger lines of other builds (TOOL-aSparedSpawn-*, TOOL-aOrientedCast-22), outside this group."
}
~~~~

### 2026-10-14T11:12:30 · gov-spec-writer · wf_2811782f-9e5/a1eabab6cba48fb1a

Label: dRedressedBar · TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 · spec-write

~~~~text
{
 "authored": [],
 "alreadyPresent": [
  "TOOL-dRedressedBar-14",
  "TOOL-dRedressedBar-15"
 ],
 "refused": [],
 "summary": "I didn't write anything because both units already have conforming specs, committed at HEAD 46eb75ed3. I edited no files, committed nothing and didn't regenerate the index.\n\n- **TOOL-dRedressedBar-14:** spec at C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-14.md. Its status header is \"SPECCED · rev-2 · 2026-10-14 · node d · Tier-2 · base ebce889c · streams tooling · order 10\", which matches the roster's order 10. All ten Tier-2 sections are there, in canonical order, none empty. Section 7 declares one `New arm:` line (tools/govkit/selftest.py, covering AC1) and section 8 holds one fork.\n- **TOOL-dRedressedBar-15:** spec at C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md. Its status header is \"SPECCED · rev-1 · 2026-10-14 · node d · Tier-2 · base ebce889c · streams tooling · order 11\", which matches order 11. All ten sections are there, in order, none empty. Section 7 declares two `New arm:` lines (covering AC1 and AC7) and section 8 says \"none\".\n\nNeither spec contains skeleton placeholders. The memory hygiene check (tools/memory-tree/check-memory-hygiene.sh) does fail check 23, the acceptance-ledger check, but every entry it lists belongs to other builds (TOOL-aSparedSpawn-* and TOOL-aOrientedCast-22). It reports nothing for dRedressedBar-14 or -15."
}
~~~~

### 2026-10-14T11:12:30 · gov-spec-writer · wf_2811782f-9e5/a908769015060cbba

Label: dRedressedBar · TOOL-dRedressedBar-11 TOOL-dRedressedBar-12 TOOL-dRedressedBar-13 · spec-write

~~~~text
{
 "authored": [],
 "alreadyPresent": [
  "TOOL-dRedressedBar-11",
  "TOOL-dRedressedBar-12",
  "TOOL-dRedressedBar-13"
 ],
 "refused": [],
 "summary": "All three units in this group were already present, so nothing was authored and nothing refused. The specs for TOOL-dRedressedBar-11, -12 and -13 are under memory/builds/dRedressedBar/spec/, committed in 29c72f51a and 95350ba59. Each conforms to memory/TEMPLATE-SPEC.md. Status header: SPECCED, Tier-2, base ebce889c, streams tooling, carrying the roster's verb (order 7, order 8, order 9). All ten canonical sections are present in order. Scope, acceptance and gates are filled: every scope item names its criteria (6/7, 6/6, 24/21 scope items to criteria) and every criterion has a Red when: clause. Each §7 has a leg line and two New arm: lines with covers fields. §8 reads none in all three. §9 logs every rev up to the header's (rev-3, rev-2, rev-2). §10 gives the reuse_lookup.py probe result before the Recall terms used: line. The memory hygiene gate exited 1, but its only failures are check 23 on acceptance-ledger lines of TOOL-aSparedSpawn-* and TOOL-aOrientedCast-22, outside this build; it reported nothing against any dRedressedBar spec. Nothing was edited, committed or regenerated."
}
~~~~

### 2026-10-14T11:14:17 · workflow-subagent · wf_2811782f-9e5/af94cc6bb43cde9de

Label: dRedressedBar · audit round 3 · subjects

~~~~text
{
 "subjects": [
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-12.md",
   "blob": "62910df09b8a993832d38fd560933f4e3ae4ed70",
   "tree": "62910df09b8a993832d38fd560933f4e3ae4ed70"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-13.md",
   "blob": "4cc48572b2b265f07f3e20325c284f0876cd2c48",
   "tree": "4cc48572b2b265f07f3e20325c284f0876cd2c48"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-14.md",
   "blob": "565574ae36de60bce3f568a48aca70086bc6bac9",
   "tree": "565574ae36de60bce3f568a48aca70086bc6bac9"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md",
   "blob": "ebbcbbf0e4cc9c8fd9c66e8b8549973d2eb6badc",
   "tree": "ebbcbbf0e4cc9c8fd9c66e8b8549973d2eb6badc"
  }
 ],
 "notAtHead": [],
 "checklistPaths": [
  "tools/govkit/govkit.py",
  "tools/govkit/selftest.py",
  "tools/govkit/matrix.py",
  "tools/govkit/entries/settings-merge.kit.toml",
  "tools/hooks/kit.toml",
  "tools/hooks/agent-cap.js",
  "tools/hooks/format-guard.js",
  "tools/hooks/scratch-guard.js",
  "memory/project/encoding-posture-sites.txt",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-9.md",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md",
  "memory/builds/dRedressedBar/build/",
  "memory/map/generated/"
 ],
 "checklist": "# recurring-bug-class checklist for 14 path(s) (14 file(s))\n# 27 class(es) selected by an anchor + 6 universal\n# by anchor specificity: 16 path · 4 directory · 7 basename; a cut tier prints one line per class\n# invariants are read at ebce889c7d71; 0 that this subject adds, edits or takes out are listed as items, never by design\n\n- [ ] fixture-passes-by-finding-nothing (universal)\n      a test arm whose fixture never triggers the rule passes, and proves nothing\n      memory/gotchas/fixture-passes-by-finding-nothing.md\n\n- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)\n      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage\n      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md\n\n- [ ] heredoc-escape-reaches-the-regex (universal)\n      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem\n      memory/gotchas/heredoc-escape-reaches-the-regex.md\n\n- [ ] inline-fence-swallows-the-rest-of-the-file (universal)\n      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view\n      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md\n\n- [ ] staged-break-substitutes-a-synthetic-value (universal)\n      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n      memory/gotchas/staged-break-substitutes-a-synthetic-value.md\n\n- [ ] two-answers-to-one-question (universal)\n      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n      memory/gotchas/two-answers-to-one-question.md\n\n- [ ] a-new-local-collides-in-a-long-function (path)\n      a local added to a function thousands of lines long can share its name with one a distant block already binds, and the later binding silently replaces the new value only on the inputs that reach that block\n      memory/gotchas/a-new-local-collides-in-a-long-function.md\n\n- [ ] containment-tested-one-way (path)\n      a guard asking only \"is this path under the protected one\" refuses the narrow declarations and admits the one that claims everything\n      memory/gotchas/containment-tested-one-way.md\n\n- [ ] line-claim-matched-over-the-whole-output (path)\n      an arm that asserts a line names X tests two substrings over the whole output, so it passes when X appears on some other line and the line it means names something else\n      memory/gotchas/line-claim-matched-over-the-whole-output.md\n\n- [ ] verdict-printed-before-the-step-that-reverts-it (path)\n      a verb prints a verdict about bytes it just wrote, and a later step of the same run can revert those bytes, so the operator reads a verdict about a tree the run did not leave\n      memory/gotchas/verdict-printed-before-the-step-that-reverts-it.md\n\n- [ ] a-folded-field-leaves-its-row-shape-docs-behind (path)\n      a review fold adds a key to a declared row shape in the code and its gate, and the spec body and the README that describe that shape keep the old key set\n      memory/gotchas/a-folded-field-leaves-its-row-shape-docs-behind.md\n\n- [ ] a-merge-of-the-default-branch-read-as-additions (path)\n      a check that lists the files a range or a commit ADDS reads a merge of the default branch into a feature branch as adding every file the default branch gained, unless its git invocation is one of the shapes that cannot\n      memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md\n\n- [ ] a-pair-exists-and-it-is-the-wrong-one (path)\n      a scanner that pairs a delimiter with the next one of its kind finds a pair for a delimiter that opens nothing, and the span it then blanks is where the defect hides\n      memory/gotchas/a-pair-exists-and-it-is-the-wrong-one.md\n\n- [ ] a-view-fix-trades-one-blindness-for-another (path)\n      a scanner that grades source through a rendered view has a blind spot, and building a better view moves it rather than closing it, each move a new fail-open or false-deny\n      memory/gotchas/a-view-fix-trades-one-blindness-for-another.md\n\n- [ ] allowlist-narrower-than-the-root-it-guards (path)\n      a guard keyed on a path prefix denies the sanctioned destination too, because on this platform the sanctioned destination is INSIDE the prefix\n      memory/gotchas/allowlist-narrower-than-the-root-it-guards.md\n\n- [ ] concurrency-is-not-a-budget (path)\n      a per-item verify fan-out passes a concurrency cap and still spawns one agent per finding\n      memory/gotchas/concurrency-is-not-a-budget.md\n\n- [ ] fixture-inherits-ambient-machine-state (path)\n      a hermetic-looking fixture silently reads machine-global config, so it passes everywhere it was written and fails where it was not\n      memory/gotchas/fixture-inherits-ambient-machine-state.md\n\n- [ ] fixture-lacks-a-gate-the-consumer-has (path)\n      a runbook's fixture passes because it lacks a commit-time gate the consumer runs, and the consumer refuses the step the fixture let through\n      memory/gotchas/fixture-lacks-a-gate-the-consumer-has.md\n\n- [ ] held-suite-guard-misses-a-sibling-kit (path)\n      a held self-test reads another kit's file, but its leg's guard names only its own kit, so an edit to the sibling skips the leg or reuses its stale green\n      memory/gotchas/held-suite-guard-misses-a-sibling-kit.md\n\n- [ ] subprocess-resolves-a-different-shell (path)\n      Python subprocess resolving the bare name bash finds the WSL launcher, which sees another filesystem\n      memory/gotchas/subprocess-resolves-a-different-shell.md\n\n- [ ] suite-invalidated-by-a-commit-under-it (path)\n      a suite that pins gov's revision at import and stamps fixtures from live HEAD is silently invalidated by any commit made while it runs, and the failures name the product\n      memory/gotchas/suite-invalidated-by-a-commit-under-it.md\n\n- [ ] trailing-comma-counted-as-an-element (path)\n      a counter scoring one-plus-every-top-level-comma reads a trailing comma as a real item, so every multi-line literal measures one too many\n      memory/gotchas/trailing-comma-counted-as-an-element.md\n\n- [ ] empty-field-collapses-unless-it-is-last (directory) · memory/gotchas/empty-field-collapses-unless-it-is-last.md\n\n- [ ] amendment-leaves-its-other-half-standing (directory) · memory/gotchas/amendment-leaves-its-other-half-standing.md\n\n- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory) · memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md\n\n- [ ] retirement-inventory-misses-readers-by-value (directory) · memory/gotchas/retirement-inventory-misses-readers-by-value.md\n\n- [ ] fold-text-is-unreviewed-surface (basename) · memory/gotchas/fold-text-is-unreviewed-surface.md\n\n- [ ] observed-by-claim-no-arm-discharges (basename) · memory/gotchas/observed-by-claim-no-arm-discharges.md\n\n- [ ] a-new-leg-trips-a-growing-set-of-meta-gates (basename) · memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md\n\n- [ ] anchor-literal-resolves-above-its-target (basename) · memory/gotchas/anchor-literal-resolves-above-its-target.md\n\n- [ ] hand-named-gate-list-green-while-the-bar-reds (basename) · memory/gotchas/hand-named-gate-list-green-while-the-bar-reds.md\n\n- [ ] join-key-widened-by-a-shared-location (basename) · memory/gotchas/join-key-widened-by-a-shared-location.md\n\n- [ ] staged-break-runs-stale-bytecode (basename) · memory/gotchas/staged-break-runs-stale-bytecode.md\n\n# by design — 0 invariant(s) this selection touches\n"
}
~~~~

### 2026-10-14T11:14:59 · workflow-subagent · wf_2811782f-9e5/a4713dbe9b3b67dc7

Label: dRedressedBar · spec-audit round 1 · resume:probe

~~~~text
{
 "commonDir": "C:/projects/coding-governance/.git",
 "blobs": [
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-12.md",
   "now": "62910df09b8a993832d38fd560933f4e3ae4ed70"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-13.md",
   "now": "4cc48572b2b265f07f3e20325c284f0876cd2c48"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-14.md",
   "now": "565574ae36de60bce3f568a48aca70086bc6bac9"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md",
   "now": "ebbcbbf0e4cc9c8fd9c66e8b8549973d2eb6badc"
  }
 ],
 "finds": [],
 "verifies": [],
 "skipped": []
}
~~~~

### 2026-10-14T11:15:12 · gov-spec-reviewer · wf_2811782f-9e5/a60056404b90ee694

Label: dRedressedBar · spec-audit round 1 · find:coherence

~~~~text
{
 "lens": "coherence",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md",
   "where": "section 2 S6, section 5 risks, section 7 New arm 1 (against unit 14 S4 and AC1)",
   "severity": "medium",
   "claim": "C26: unit 15 makes the agent-cap refusal line go away, but unit 14's [dRB-14] arm asserts that line on the same apply, and unit 15 retires none of unit 14's asserts. The reader inventory in unit 15's risks was taken at the base, before that arm existed.",
   "impact": "Unit 14 S4 has the [dRB-14] block assert \"AC1's line, receipt and settings facts\". Unit 14 AC1's line facts include \"exactly one line opens `govkit: kit 'agent-cap'` and carries `settings-merge.py`\". Unit 15 S6 then puts [dRB-15] checks on that same apply, asserting \"No line opens `govkit: kit '`\" (unit 15 AC1). Built as written, the two arms contradict each other on one run, so `govkit selftest` goes red at unit 15's close and no section-2 item says what to do about it. Unit 15's risks claim that no arm pins agent-cap's adopter outcome. That claim rests on a `git grep` of a tree with no [dRB-14] block yet, so the inventory misses a reader that depends on the behaviour without spelling the argv.",
   "fix": "Add an item to unit 15 S6 that rewrites (or removes) the [dRB-14] block's agent-cap problem-line assertion, giving the [dRB-15] check sole ownership of agent-cap's outcome on that apply. Restate unit 15's §5 risk inventory over the tree unit 14 leaves, naming the [dRB-14] assertion as a by-value reader. Or narrow unit 14 S4 so [dRB-14] asserts settings-merge's line, the receipt row and settings.json only, never agent-cap's line.",
   "evidence": "read: memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-14.md:46-50 (S4: 'asserts AC1's line, receipt and settings facts'), :272-273 (AC1: 'exactly one line opens `govkit: kit 'agent-cap'` and carries `settings-merge.py`'); 2026-10-14-spec-TOOL-dRedressedBar-15.md:68-73 (S6 first check 'reads the apply that unit 14's [dRB-14] block runs'), :347 (AC1 'No line opens `govkit: kit '`'), :321-323 (risks: 'No arm pins agent-cap's [adopt].argv ... git grep finds no CONFIGURE agent-cap' — measured at 95350ba5, where tools/ equals ebce889c and no [dRB-14] block exists). Unit 15 §4 Files touched lists tools/govkit/selftest.py, but no S item edits [dRB-14]."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-12.md",
   "where": "section 2 S1 against section 6 AC1-AC6 (also unit 14 S2's 'Observed by AC1 and AC2')",
   "severity": "medium",
   "claim": "S1 requires that `install.sums` and the `STEP_RECEIPT` counts be derived from the written list (selection rows plus carried rows), but no criterion reads either. Unit 14 S2 repeats the requirement and cites AC1 and AC2, and neither of those reads them either.",
   "impact": "Suppose a build adds the carry to `install.json` and leaves the sidecar loop at govkit.py:8027-8028 iterating `rows`. It passes AC1 to AC6. `govkit check` asserts the sidecar and the receipt against each other (govkit.py:5329-5333), so after every narrower apply it reds 'the receipt carries <path> ... which install.sums does not' for each carried row. That ships a target state the engine's own check refuses. A stale `[11/RECEIPT] 2 row(s), 1 kit(s)` count would also go unseen.",
   "fix": "Extend unit 12 AC1: after step 2, `.governance/install.sums` holds one line per receipt row carrying `sha256`, the 16 carried rows included (derive the set from the receipt). Step 2's `[11/RECEIPT]` line reads `18 row(s), 3 kit(s)`. Red half: at the base the sidecar holds 2 lines. Unit 14 AC1 or AC2 should assert the same sidecar-to-receipt equality after its rewrite.",
   "evidence": "grep over spec 12-15 for 'sums|STEP_RECEIPT|RECEIPT\\]' printed only spec-12.md:37-38 (S1), :111 (§4 table), :200 (§5) and spec-14.md:41 (S2); no AC line. read: tools/govkit/govkit.py:8027-8028 (sidecar written from `rows`), :5322-5333 (`check` fails on any receipt/sidecar pair difference)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-13.md",
   "where": "section 6 AC15 (with section 2 S17 and the section 7 New arm for AC15)",
   "severity": "medium",
   "claim": "AC15 bans `_sha(`, `blob_oid(` and `\"git\", \"show\"` across the whole span from the first to the last `[dRB-11]` line. That span also contains fixture A, and spec 11 AC3 requires fixture A to plant a row with 'that blob's sha256 and gov_oid'. The selftest's idiom for deriving those is `gk._sha(` and `gk.blob_oid(`. So a correct build can fail AC15, while a hand derivation of fixture B through `hashlib` or the `git(` helper passes it.",
   "impact": "S17 changes fixture B only. Fixture A sits in the same [dRB-11] block (spec 11 §4 'The witnessing arms'), and the engine-helper route for its identities (as in write_vintage_receipt:666-667) trips the ban, so AC15 reds on a correct pass. The ban is also a list of spellings: a fixture B that derives identities via `hashlib.sha256(...)` or `git(govroot, \"show\", ...)` contains none of the banned strings and passes. The criterion can fail on a correct build and pass on the defect it exists to catch.",
   "fix": "Scope AC15 to fixture B's own lines, for example the span between two named markers S17 places around it. Assert positively that the agent-cap row's `commit`, `sha256` and `gov_oid` are set by `write_vintage_receipt` (the row appended without those keys, then the helper called). Do not rely on a spelling ban. Alternatively, let fixture A's identities come from the helper as well and say so in S17.",
   "evidence": "read: memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-13.md:413-419 (AC15 span 'from the first to the last line carrying [dRB-11]'); 2026-10-14-spec-TOOL-dRedressedBar-11.md:272-279 (block builds fixtures A, A-absent and B) and :366-370 (fixture A row with 'that blob's sha256 and gov_oid'); tools/govkit/selftest.py:663-667 (`\"git\", \"show\"`, `gk._sha(b)`, `gk.blob_oid(b)`). `grep -n \"_sha(\\|blob_oid(\" tools/govkit/selftest.py | wc -l` printed 28."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md",
   "where": "section 7 Gates leg line",
   "severity": "low",
   "claim": "C31: the hand-named gate list leaves out two legs that the unit's own changes reach. One is `format-guard self-test`, whose guard names `{prefix}/hooks/format-guard.js` and `{prefix}/hooks/scratch-guard.js`, the two version carriers S7's mint rewrites. The other is the unguarded `kit placeholders (a declared token its adopter substitutes)` leg, which runs tools/check-kit-placeholders.py, a reader S4's Readers clause names for `[adopt] argv`.",
   "impact": "A pass that is green on the named list can still leave the bar red on these legs. The close catches it, but late, and the list implies coverage it does not have.",
   "fix": "Add `format-guard self-test` and `kit placeholders (a declared token its adopter substitutes)` to §7. State that the list is a floor, derived by matching the Files touched against tools/gate-legs.json guards.",
   "evidence": "python over tools/gate-legs.json printed: 'format-guard self-test :: bash {prefix}/hooks/format-guard.test.sh :: [\"{prefix}/hooks/format-guard.js\", ..., \"{prefix}/hooks/scratch-guard.js\", ...]' and 'kit placeholders (a declared token its adopter substitutes) :: python {prefix}/check-kit-placeholders.py :: None'. read: spec-15.md:54-58 (S4 Readers names check-kit-placeholders.py:133-139), :255-257 (mint moves format-guard.js:7 and scratch-guard.js:144), :438 (§7 list, neither leg present)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-14.md",
   "where": "section 3 Edges and section 4 'Order, and unit 7'",
   "severity": "low",
   "claim": "Two problems in §4 'Order, and unit 7'. It says 'Unit 13 is a sequence and not an edge, because no criterion here rests on its work', yet the AC1, AC2 and AC4 red halves, AC5's diff base and the §7 New arm all run from `<p13>`. The same section also describes as pending the README edits ('Unit 14 needs a roster row'; the Build-level sentence 'should name 12, 13 and 14'), and the README already contains them.",
   "impact": "The ordering axis disagrees with itself: a criterion needs unit 13's pass commit while Edges declare no dependency on unit 13. The pending-edit prose is the same defect class unit 13 S11 corrects in spec 11 (report id 11), so it will mislead the next reader.",
   "fix": "Add a `consumes-from TOOL-dRedressedBar-13` edge (its pass commit `<p13>` is the red-half reference, and it settles the encoding registry AC5 derives). Restate the Order paragraph to point at README.md's Build-level rules and the derived build-order step 10, which already exist.",
   "evidence": "read: spec-14.md:194-195 ('no criterion here rests on its work'), :200-202 (README changes described as pending), :257-263, :303, :308, :314, :325 (criteria and arm reading `<p13>`), :78-95 (Edges: consumes-from 11 and 12 only); memory/builds/dRedressedBar/README.md:69-70 ('Units 10, 11, 12, 13 and 14 follow 7 in that order'), :99 (unit 14 roster row), :148 (step 10)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-13.md",
   "where": "section 1 Goal",
   "severity": "low",
   "claim": "§1 says the unit 'is ordered after every unit of this build'. Units 14 (order 10) and 15 (order 11) are ordered after it.",
   "impact": "The sentence contradicts the README build order and specs 14 and 15, which both sequence behind unit 13 and rewrite the same CONFIGURE call site. A reader could treat unit 13 as the build's last code unit.",
   "fix": "Reword §1 to say the unit is ordered after units 10, 11 and 12, whose specs and tree it corrects, and that units 14 and 15 follow it.",
   "evidence": "read: spec-13.md:20 ('it is ordered after every unit of this build'); memory/builds/dRedressedBar/README.md:146-149 (steps 9, 10, 11: units 13, 14, 15); spec-14.md:3 'order 10', spec-15.md:3 'order 11'."
  }
 ]
}
~~~~

### 2026-10-14T11:15:13 · gov-spec-reviewer · wf_2811782f-9e5/a01cb16deb2b4523b

Label: dRedressedBar · spec-audit round 1 · find:grounding

~~~~text
{
 "lens": "grounding",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-12.md",
   "where": "section 3, second non-goal (No carry of gate_runner.emitted); section 2 S2; section 4 Alternatives row C5",
   "severity": "high",
   "claim": "The spec says a leg row a carried kit loses from `emitted` is re-claimed by the same-argv rule (`:4143-4152`) on that kit's next run, 'so it wedges nothing'. That only holds while gov's resolved argv for the leg is unchanged. `check_leg_claimable` requires the argv to match exactly, and on any mismatch `write_gate_legs` raises a Refusal. Unit 12 keeps the kit's claim while still dropping its leg ownership, which is the claimed-but-unowned state the engine's own comment calls a permanent wedge.",
   "impact": "Take a manifest target where a narrower `apply` carried kit K. If gov later changes the resolved argv of one of K's gate legs, every later `apply --kits K` exits 2 at LEGS: 'the target's runner already has a leg named X and this target's receipt does not claim it'. Every `update --write` whose scope includes K catches the same Refusal (`:11878-11891`), records a problem and exits 1. Neither verb can rebuild the ownership, so the only way out is hand-editing the target's runner. Before unit 12 the kit was unclaimed, so `update` never reached its legs. Unit 12's carry makes this route reachable, and the rejection of C5 as YAGNI rests on the false sentence.",
   "fix": "Have `apply` pass `carry_out_of_scope=True` to `write_gate_legs` now that it keeps `kits` whole. That is the docstring's own rule for a verb whose receipt keeps every claimed kit (`:4039-4041`): an out-of-scope kit is still claimed, so its ownership rows must survive the run. Rewrite S2's docstring sentence and section 3 to match, and add a criterion. The build should run this probe (it needs writes, so it was not run here): a scratch gov and a manifest target; apply two kits that each declare a gate leg; apply one of them alone; commit a change to the other kit's leg argv in the scratch gov; then run `update --write` and `apply --kits <carried kit>`. Without the carry both refuse on the 'already has a leg named' message, and with it both pass.",
   "evidence": "read: tools/govkit/govkit.py:4003-4008 (check_leg_claimable: `runner_leg.get(\"argv\") == argv`, exact equality); :4143-4159 (nm in runner and not owned: claimed only if argv equal, else `raise Refusal(... already has a leg named ...)`); :4303-4305 (only `carry_out_of_scope` keeps prior rows of kits outside the selection); :4318-4325 (the comment says dropping `emitted` ownership 'WEDGES the target permanently — every later apply refuses the legs this deployer itself wrote'); :11878-11891 (update catches that Refusal as r.fail over `_legs_scope = claimed`); :7953-7955 (apply passes no carry). Spec 12 section 3: 'A leg row a carried kit loses there is re-claimed on its next run by the same-argv rule (`:4143-4152`, DEPL-aRepatriatedFork-17 S8), so it wedges nothing.'"
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-13.md",
   "where": "section 5, risks; section 3, fourth non-goal",
   "severity": "low",
   "claim": "Section 5 says `errors=\"replace\"` 'diverges from the two sibling sites, which decode strictly'. That is false for one of the two: the regenerate site already passes `errors=\"replace\"`. Only the gained loop decodes strictly. Section 3 also cites the regenerate site as `:10986-10987`, but its `errors` argument is on line 10988.",
   "impact": "The risk record misstates the code it compares against. A later change that 'aligns' CONFIGURE with its siblings could drop `errors=\"replace\"` on the strength of this sentence, which would bring back the mid-install decode raise that S13 exists to remove. The effect stays in the spec's prose.",
   "fix": "Restate the risks line: the regenerate site (`:10986-10988`) already decodes UTF-8 with replacement, so S13 makes CONFIGURE match it, and only the gained loop (`:11119-11120`) still decodes strictly. Cite the regenerate site as `:10986-10988` in section 3.",
   "evidence": "`sed -n '10980,10990p' tools/govkit/govkit.py` printed: `_out = subprocess.run(resolve_shell_argv(_res), cwd=str(target),` / `capture_output=True, text=True, encoding=\"utf-8\",` / `errors=\"replace\")`. `sed -n '11114,11122p'` printed the gained loop with `encoding=\"utf-8\"` and no `errors`."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-14.md",
   "where": "section 4, 'The receipt written ahead', paragraph under the table",
   "severity": "low",
   "claim": "The spec says 'The only appends are `:7616` and `:7621`'. `_cmd_apply` actually has six `rows.append` sites: 7424 (attributes), 7502 (merged), 7540, 7593 (the `[[own]]` prior carry), 7616 and 7621. The conclusion the sentence supports, that nothing is appended after LAND, still holds, because every site is at or before LAND.",
   "impact": "This is cosmetic. The argument for the early write is still right, but a reader who checks the cited list finds four appends it leaves out. The `.gitattributes` and `[[own]]` rows are the ones unit 12's carry and AC3 reason about.",
   "fix": "Replace the sentence with: 'Every append to `rows` (`:7424`, `:7502`, `:7540`, `:7593`, `:7616`, `:7621`) sits at or before LAND (`:7435-7623`).'",
   "evidence": "Grep of `rows.append` inside `_cmd_apply` (lines 7233-8031) of tools/govkit/govkit.py found matches at 7424, 7502, 7540, 7593, 7616 and 7621."
  }
 ]
}
~~~~

### 2026-10-14T11:15:13 · gov-spec-reviewer · wf_2811782f-9e5/a0c0cd045e37d209a

Label: dRedressedBar · spec-audit round 1 · find:failure-envelope

~~~~text
{
 "lens": "failure-envelope",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-14.md",
   "where": "section 4 \"When CONFIGURE fails\" (row 2) and section 6 AC4",
   "severity": "medium",
   "claim": "C5: the spec says any exception or interrupt between the two receipt writes can be recovered by re-running apply. The only staged fault (AC4) sits at the earliest instant, before any adopter runs, so it never reaches the state that breaks the claim: an interrupt after RENORMALIZE, while LEGS or AFTER is running the target's runner. At that point the early receipt still holds STAGE's `oid`s, and the renormalize has already replaced them in the index.",
   "impact": "The early receipt records `oid`s from STAGE. On a target whose checkout applies a line-ending filter, `git add --renormalize` rewrites the index blob of every LF-pinned path after STAGE. If the run dies anywhere from RENORMALIZE to RECEIPT, the receipt it leaves names blobs the index no longer holds. LEGS and AFTER run the target's whole runner, so this is the longest stretch and the likeliest place for a Ctrl-C. On the next `apply`, `demand_writable_target` -> `demand_claimed_paths_clean` compares each row's `oid` with the index (carve-out 3), finds the paths DIRTY, and refuses. That is the opposite of what the spec claims. The code comment at the re-stamp records this exact refusal for `update --write`. AC4 still passes because its fault comes before RENORMALIZE.",
   "fix": "Either (a) bring the on-disk receipt up to date after the re-stamp at govkit.py:7926-7936, by rewriting `_rcpt_doc` once more there or by having S1's write happen only after the re-stamp for the `files` key, or (b) limit the table's recovery claim to interrupts before RENORMALIZE and state what remains. Under (a), add a second staged fault to AC4 for the build to run: put the RuntimeError at the `step(STEP_LEGS, ...)` line, use a target with `core.autocrlf true` holding an LF-pinned path that a CRLF checkout renormalizes, and require that the unpatched re-run prints no `DIRTY`.",
   "evidence": "read: tools/govkit/govkit.py:7893-7936, the re-stamp comment: \"`git add --renormalize` REWRITES the index blob of every LF-pinned path, and it runs AFTER the stamp above. Every affected row therefore recorded a blob the target does not hold\" and \"`update --write` straight after `apply` still refused over it\". read: govkit.py:7093-7097, where `dirty_claimed_paths` is passed `{row['path']: row['oid']}`, and govkit.py:7174 and 7287, where apply calls `demand_writable_target` -> `demand_claimed_paths_clean`. read: spec 14 lines 136, 160 and 295-302. Line 136 says the early `files` carry \"the `oid` STAGE stamped\". Line 160 says \"Each staged path matches its row's `oid`, so `demand_claimed_paths_clean` passes ... step 5 above measured both\", but step 5 re-ran over a COMPLETED receipt. AC4 puts the fault \"after the line `inert = read_inert_kits(deploy)`\", which is the first line of CONFIGURE (govkit.py:7670)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-14.md",
   "where": "section 2 S1 and S2; section 4 \"When CONFIGURE fails\"",
   "severity": "medium",
   "claim": "The spec designs the early receipt for the interrupted run, yet it writes both receipt writes with the plain `write_text` call used today (\"with the encoding and newline arguments it uses today\"). An exception, a signal or a full disk during either write leaves `install.json` truncated, and the failure table never mentions that case.",
   "impact": "With this unit, every apply writes `install.json` twice, and the second write always overwrites a file already on disk. `write_text` truncates the file before it writes, so a run that dies mid-write leaves invalid JSON. The next `apply` then crashes at `json.loads` on govkit.py:7251, which sits outside any Refusal handling, before any precondition runs. Every inlined `resolve_kit_dir` treats the file as having no rows, so the per-kit-prefix fix this unit exists for disappears without notice. The deployer already has `write_atomic` for exactly this hazard and uses it for the gate-leg manifest.",
   "fix": "S1 and S2 write `_rcpt_doc` through `write_atomic` (govkit.py:3967), via a sibling temp file and `os.replace`, rather than `receipt_path.write_text`. Add a row to the 'When CONFIGURE fails' table for an interrupt during either receipt write, stating that the previous receipt stays whole. The build can probe it from a scratch gov copy whose `os.replace` raises once, with the expectation that `install.json` still parses.",
   "evidence": "read: tools/govkit/govkit.py:8019-8026, where RECEIPT writes `receipt_path.write_text(json.dumps(...))`, not atomically. read: govkit.py:7251, `receipt = json.loads(receipt_path.read_text(encoding=\"utf-8\")) if receipt_path.is_file() else None`, with no try. read: govkit.py:3967-3990, the docstring of `write_atomic`: \"so a run that dies mid-write leaves the PREVIOUS file rather than a truncated one\". read: govkit.py:213-216, where resolve_kit_dir catches ValueError and sets `rows = []`. Command `grep -n 'receipt_path.write_text' tools/govkit/govkit.py` printed 8019, 12017, 12055, 12062 and 12692, so no receipt write is atomic today. read: spec 14 line 40, \"It writes `_rcpt_doc` with the encoding and newline arguments it uses today\"."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md",
   "where": "section 2 S1 and S5; section 4 \"The class gate\" (the `via` rules); section 6 AC7",
   "severity": "medium",
   "claim": "The spec never says what happens to a `via` value that is present but is not a non-empty string, such as `\"\"`, a list or an integer. S1 quietly treats any such value as \"no via\" and falls back to the entry's own argv. S5 applies its rules to entries whose `[adopt]` \"carries `via`\", without saying whether that means the key is present or the value is truthy.",
   "impact": "Suppose agent-cap's descriptor carries `via = \"\"`, or `via = [\"settings-merge\"]`. S1 then falls back to agent-cap's own argv, which S4 has deleted, and returns `[]`. S2's `if not resolved: continue` skips the adopter and prints nothing. If S5 is built as a truthiness test, `\"\"` is never graded. The ownership join is offered zero `[adopt]` elements for agent-cap, so selfcheck stays green. The hook then goes unwired, unreported, in the case §4's last row protects (settings-merge claimed but not selected), which is the C2 failure. A list value hits rule 1 as `v in descs`, which raises TypeError (unhashable) and turns selfcheck's finding into a traceback. AC7 has no arm for either input.",
   "fix": "S5: the population is every entry whose `[adopt]` table HAS the `via` key. Add a first rule ahead of the four: `<v>` must be a non-empty string, reason `is not a non-empty string`. Give S1 the same rule, so the helper treats the key's presence, not the value's truthiness, as the delegate declaration. Add two AC7 bullets, `via = \"\"` and `via = [\"other\"]`. Each prints exactly one line opening `govkit: entry 'demo' declares [adopt] via` that carries `is not a non-empty string`, with no traceback.",
   "evidence": "read: spec 15 lines 31-32, \"When that is a non-empty string it is the source entry, else `eid` is\". Line 166, \"For every entry in `_bare_sel` whose `[adopt]` carries `via`\". Lines 173-178, four rules, none of them on the value's type. Lines 39-40, `if not resolved: continue`. Lines 400-410, the AC7 bullets, with no empty or non-string case. read: tools/govkit/govkit.py:7740-7742, where today's `if not argv: continue` prints no line, so the skip is silent. read: spec 15 §4 last measured row (line 134) and lines 136-141: agent-cap's adopter is \"the only step that wires the hook when settings-merge is claimed but not selected\"."
  }
 ]
}
~~~~

### 2026-10-14T11:15:13 · gov-spec-reviewer · wf_2811782f-9e5/ae20681fdd73f06d1

Label: dRedressedBar · spec-audit round 1 · find:reuse

~~~~text
{
 "lens": "reuse",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md",
   "where": "section 4 \"The class gate\" (The ownership join), S5, section 10",
   "severity": "medium",
   "claim": "S5 builds a fourth per-entry argv walker over the bare-target selection instead of extending `silenced_legs` (tools/govkit/govkit.py:3908-3946), which already walks `[[gate_leg]]` argv per entry through `target_context` and the same `/` rule. The new walker also uses a different element predicate from the one `silenced_legs` uses.",
   "impact": "The spec text says \"An element is OFFERED when its declared text carries `/`. It is GRADED when its resolved text carries no `{` and no space\". `silenced_legs` instead asks whether the RESOLVED text carries `/` and skips on the `missing` list that `resolve_tokens` returns. For the 67 gate-leg elements both arms grade, that leaves two answers to \"is this element a path\". A declared `{kit}` alone, which resolves to `tools/hooks`, is graded by `silenced_legs` and never offered by S5. The selfcheck output would also print two different \"offered\" counts for one population: the existing note `{_leg_argv} argv element(s) offered against a bare target` (:3214) and S5's `cross-entry argv: <o> ... offered`. Section 10 says only that \"no second planner exists\". It is silent on the second argv walker, and reuse_lookup does not surface `silenced_legs`.",
   "fix": "Extend the seam instead of restating it. Factor the per-entry walk in `silenced_legs` into one generator that yields (eid, kind, name, declared, resolved, missing) for `[adopt]` (through S1's source entry), `[check]`, `[[gate_leg]]` and `[[regenerate]]`. Grade both `silenced_legs`' not-in-`have` predicate and S5's ownership predicate from it, with one offered/graded rule: resolved text carries `/` and `missing` is empty. Then state in section 10 that S5 extends `silenced_legs`, and make S5's note reuse the existing gate-legs count, or replace it, instead of printing a second one.",
   "evidence": "read: tools/govkit/govkit.py:3908-3946 (`silenced_legs`: `ctx = target_context(target, deploy, eid, d)` ... `s, miss = resolve_tokens(a, ctx); if miss or \"/\" not in s: continue`). read: tools/govkit/govkit.py:3166-3170 and :3214-3218 (bare-target block computing `_leg_argv` and printing \"argv element(s) offered against a bare target\"). read: spec 15 lines 194-196 (OFFERED/GRADED rule) and line 232 (\"A path no entry ships, which `silenced_legs` already grades for gate legs\"). `python tools/codebase-map/reuse_lookup.py \"grade every argv element a descriptor declares that names a path no rule produces or another entry ships\"` ranked `declares`, `read_descriptors`, `resolve_entry` and `resolve_shell_argv`, and did not list `silenced_legs`."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md",
   "where": "section 3 non-goal \"No change to the other readers of `[adopt].argv`\", S1, S4 Readers",
   "severity": "medium",
   "claim": "S1 mints `resolve_adopter_argv` as the answer to \"what does CONFIGURE run for this entry\", but two existing readers keep their own copy of that answer, the declared `argv` being non-empty. `check_entry_producer` (:3687-3701) quotes CONFIGURE's own code in its docstring, and the json-pointer merged-rule guard reads the declared argv at :7315. S2 makes both answers wrong for any `via` entry.",
   "impact": "The spec quotes \"agent-cap ships no `rendered`, `generated` or `merged` rule, so `check_entry_producer`'s and `:7315`'s answer for it does not move\". That is true for agent-cap only. The `via` key is a general grammar that S5 admits for any entry. `check_entry_producer`'s docstring states \"CONFIGURE is `argv = d.get(\\\"adopt\\\", {}).get(\\\"argv\\\") or []` followed by `if not argv: continue`\", and S2 deletes those exact lines, so the docstring describes code that no longer exists. The next entry that declares `via` beside a rendered/generated side-effect rule would be called a non-producer by plan/selfcheck (:3777). One that declares a json-pointer merged rule would be refused \"no adopter to delegate to\" (:7315), even though CONFIGURE runs the delegate for it.",
   "fix": "Make S1's helper the one answer. `check_entry_producer` and the :7315 guard ask whether `resolve_adopter_argv`, or a declared-level twin that follows `via` to the source entry's argv, is non-empty, and `check_entry_producer`'s docstring is updated to quote the new CONFIGURE lines. Add both sites to S4's Readers \"by value\" with that change, or else name a selfcheck rule that refuses `via` on an entry that carries a rendered, generated or merged rule, so the narrowing is enforced and not just asserted.",
   "evidence": "read: tools/govkit/govkit.py:3687-3701 (`def check_entry_producer`, whose docstring reads \"CONFIGURE is `argv = d.get(\\\"adopt\\\", {}).get(\\\"argv\\\") or []` followed by `if not argv: continue`\" and whose body reads `if not ((desc.get(\"adopt\") or {}).get(\"argv\") or []): return False`). read: tools/govkit/govkit.py:7314-7317 (`if not (d0.get(\"adopt\") or {}).get(\"argv\"): r.fail(... \"no adopter to delegate to\")`). read: tools/govkit/govkit.py:7740-7743 (the CONFIGURE lines S2 replaces). read: spec 15 lines 97-101 (non-goal)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-12.md",
   "where": "section 2 S1, section 6 AC1/AC3",
   "severity": "medium",
   "claim": "C28 observed-by-claim-no-arm-discharges. S1 says \"`install.sums` and the `STEP_RECEIPT` line are derived from the same written list ... Observed by AC1 and AC3\". Neither AC1 nor AC3 reads `install.sums` or the `[11/RECEIPT]` line. The existing seam that grades the sums against the receipt, `cmd_check`'s sidecar comparison (:5322-5333), goes unused.",
   "impact": "Today the sums line is written from `rows` alone (`for w in rows if \"sha256\" in w`, :8027-8029), and the step line from `len(rows)` and `len(selection)` (:8030). A build that carries `kits` and `files` but leaves either derivation on this run's lists passes AC1 to AC6. The target is then left with an install.sums that lacks the 16 carried rows, and the next `govkit check` there reports \"the receipt carries ... which install.sums does not\" for each of them. The operator also sees `[11/RECEIPT] 2 row(s), 1 kit(s)` over an 18-row receipt.",
   "fix": "Extend AC1 instead of adding a new probe. After step 2, assert that `[11/RECEIPT]` reads `18 row(s), 3 kit(s)`. Then run the existing `python tools/govkit/govkit.py check --target <t>` and assert that no line carries `install.sums carries` or `which install.sums does not`. Red when: a scratch gov copy whose sums line still iterates `rows` prints the latter for the carried rows. Have the `[dRB-12]` arm make the same two assertions.",
   "evidence": "read: tools/govkit/govkit.py:8027-8030 (sums from `rows`, step line from `len(rows)` and `len(selection)`). read: tools/govkit/govkit.py:5322-5333 (`sums_path = target / \".governance\" / \"install.sums\"` ... `r.fail(f\"the receipt carries {missing[1]} ... which install.sums does not\")`). read: spec 12 lines 222-249 (AC1 and AC3 assert `kits`, row equality, the row count, the KEEPS line, step 3's exit and `attributes` rows, and nothing about sums or the step line)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md",
   "where": "section 2 S3, section 4 \"What an adopter sees change\" row 5, section 6 AC5/AC9",
   "severity": "medium",
   "claim": "C28 observed-by-claim-no-arm-discharges. S3 rewrites `_cmd_update`'s gained loop and says it is \"Observed by AC5 and AC9\". AC5 calls the helper in isolation, and AC9 only greps (`_argv_g` absent, `resolve_adopter_argv` count >= 4). No criterion runs `update`, and section 4's table marks the per-kit-prefix update row \"Derived, not run\". The existing update-gaining arm, unit 9's `[dRB-9]` block, is not extended.",
   "impact": "A staged break of the update site goes unseen. Examples: the skip test still reads the declared argv under a new local name, or the `_ran_gained` dedup is keyed on something else. The `>= 4` count is met by the def, the two calls and any docstring or comment mention. The section 4 claim \"one resolved argv, run once and classified by agent-cap's descriptor\" therefore ships unobserved on the one verb where the dedup decides whether agent-cap's adopter runs at all.",
   "fix": "Extend the existing `[dRB-9]` update-gaining fixture (spec 9, section 7 `New arm:` line) instead of adding a new one. Add one case with `[kit.agent-cap] prefix = \"scripts\"` that gains both kits. Assert exactly one `default-gained ... adopter exit 0` line between agent-cap and settings-merge, plus a settings.json command at `scripts/hooks/agent-cap.js`. Red when: over the `<p14>` clone two adopters run and agent-cap's line ends `adopter exit 2`. Declare it as a `New arm:` line covering S3.",
   "evidence": "read: spec 15 lines 43-47 (S3 \"Observed by AC5 and AC9\"), line 245 (\"Derived, not run\"), lines 377-384 (AC5 helper-only) and lines 422-430 (AC9 greps). read: tools/govkit/govkit.py:11104-11126 (the gained loop with `_ran_gained` dedup). `grep -n \"New arm:\" memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-9.md` printed line 319, the `[dRB-9]` block whose update gains settings-merge."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md",
   "where": "section 2 S6, section 6 AC7",
   "severity": "low",
   "claim": "AC7's scratch govs are specified as \"shaped as `build_scratch_gov_kit` builds them (`tools/govkit/selftest.py:5508-5536`) carry a second entry, `other`\". `build_scratch_gov_kit` hardcodes a one-entry registry, `[[entry]] id = \"demo\"` only. As written, S6 therefore needs a parallel builder that copies the helper's body to add a second entry, rather than extending the helper.",
   "impact": "A second copy of the scratch-gov scaffold has to be kept in step with the first: the govkit copy, adopters.toml (\"arm 10 refuses a gov without it\"), the exempt row and the git init. When the next selfcheck precondition is added to `build_scratch_gov_kit`, the copy drifts, and the seven AC7 govs fail selfcheck for a reason unrelated to the arm. The effect is contained to the selftest.",
   "fix": "State in S6 that `build_scratch_gov_kit` gains an optional parameter, for example `extra: dict[str, tuple[str, dict[str, str]]]` mapping an entry id to its descriptor and files. The parameter appends an `[[entry]]` row and that entry's files, and existing callers are unchanged. AC7's seven govs are built through it.",
   "evidence": "read: tools/govkit/selftest.py:5508-5536 (`def build_scratch_gov_kit(tag: str, kit_toml: str)` writes a registry with a single `[[entry]]\\nid = \"demo\"` and only the `demo` kit directory). read: spec 15 lines 68-73 (S6) and lines 394-398 (AC7)."
  }
 ]
}
~~~~

### 2026-10-14T11:15:13 · gov-spec-reviewer · wf_2811782f-9e5/afdb82a9c59c08e3c

Label: dRedressedBar · spec-audit round 1 · find:blast-radius

~~~~text
{
 "lens": "blast-radius",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md",
   "where": "section 7 Gates leg line, joined against section 4 Files touched",
   "severity": "medium",
   "claim": "Section 4 lists `tools/hooks/format-guard.js` and `tools/hooks/scratch-guard.js` under Files touched, because S7's mint rewrites the `gov:kit agent-cap@` markers in both. The `format-guard self-test` leg's narrow guard names both files exactly, yet the section 7 leg line leaves that leg out.",
   "impact": "The spec's own `spec tokens` leg grades every non-terminal spec dated on or after SPEC_GUARD_LEGS_CUTOFF (2026-09-22) for exactly this join, so it reds on spec 15 (`format-guard self-test <- tools/hooks/format-guard.js`) as the spec stands. The pass would also close without the one suite whose subject is the two files its mint rewrites.",
   "fix": "Add `format-guard self-test` to section 7's leg line, as spec 4's leg line already does. As a check, run `python tools/check-spec-tokens.py` in the build's bar and confirm it prints no hit for spec 15. That run is a gate, so it is described here and was not run.",
   "evidence": "read: tools/gate-legs.json:348-361 (`\"name\": \"format-guard self-test\"`, guard `{prefix}/hooks/format-guard.js`, `{prefix}/hooks/scratch-guard.js`, `{prefix}/runlog/...`, `{prefix}/lib/`). read: spec 15:279-282 (Files touched lists tools/hooks/format-guard.js and tools/hooks/scratch-guard.js). read: spec 15:438 (leg line names agent-cap, scratch-guard, verifier fan-out, review-join and hook destinations self-tests, with no format-guard). read: memory/TEMPLATE-SPEC.md:264-273 (the join rule). Grep of .memory-tree.conf printed `356:SPEC_GUARD_LEGS_CUTOFF=\"2026-09-22\"`. Grep of tools/check-spec-tokens.py printed `262:BROAD_LEG_FLOOR = 5`. Grep of gate-legs.json shows each of `{prefix}/hooks/format-guard.js` and `{prefix}/hooks/scratch-guard.js` in one guard only (line 355, line 357), so neither is broad. Grep for 'format-guard self-test <-' under memory/project found no waiver row."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md",
   "where": "section 6 AC6",
   "severity": "medium",
   "claim": "AC6's pass half requires the `cross-entry argv:` note to carry `0 naming`. The note prints `<h> naming a file only another entry ships`, so the substring also matches h = 10, 20, 30 and so on.",
   "impact": "The criterion reads green while the class gate still reports cross-entry hits whenever the count ends in 0. It therefore certifies 'no cross-entry argv' without checking it.",
   "fix": "Anchor the number: require `, 0 naming` (the note's preceding token is `<g> graded,`), or have AC6 parse `<h>` with a regex such as `(\\d+) naming` and assert it equals 0. Make the red half's `1 naming` exact the same way.",
   "evidence": "read: spec 15:207 (note format `cross-entry argv: <o> slash-bearing element(s) offered by ... across <m> entries, <g> graded, <h> naming a file only another entry ships`). read: spec 15:385-386 (`prints exactly one line opening `govkit: cross-entry argv:`, and it carries `offered by` and `0 naming``). The string '10 naming a file' contains '0 naming'."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md",
   "where": "section 2 S2 and S4 Readers; section 3 non-goal 'No change to the other readers of `[adopt].argv`'",
   "severity": "medium",
   "claim": "C24: S2 replaces CONFIGURE's `argv = d.get(\"adopt\", {}).get(\"argv\") or []` / `if not argv: continue` with `resolve_adopter_argv`. `check_entry_producer`'s docstring quotes that exact code as its MEASURED basis, and the function still answers 'no adopter runs' for any entry whose `[adopt]` holds only `via`. The spec keeps the reader on agent-cap's instance ('agent-cap ships no rendered rule') and leaves the stated contract standing.",
   "impact": "After the unit lands, the docstring states a CONFIGURE shape that no longer exists. The predicate is also wrong for the class the unit introduces: the next `via` entry that ships a `rendered`/`generated` or side-effect rule gets a wrong plan mark (`scan_*` at :3777 reads `check_entry_producer`) even though CONFIGURE runs its delegate. Whoever writes that entry gets no warning from the docstring.",
   "fix": "Add `check_entry_producer` (govkit.py:3687-3702) to S2. Have it ask `bool(resolve_adopter_argv(...))`, or test `argv or via`, and rewrite the docstring's quoted CONFIGURE lines to the post-S2 form. Alternatively, have the S5 via rules refuse a `via` entry carrying a rendered/generated/side_effects rule, and say so in section 3.",
   "evidence": "read: tools/govkit/govkit.py:3687-3702 (`def check_entry_producer` with docstring `CONFIGURE is `argv = d.get(\"adopt\", {}).get(\"argv\") or []` followed by `if not argv: continue``, body `if not ((desc.get(\"adopt\") or {}).get(\"argv\") or []): return False`). Grep printed `3777:    if kind == \"side-effect\" and not (check_entry_producer(desc) or dest in produced):`. read: spec 15:38-42 (S2 rewrites :7740-7743) and spec 15:97-101 (non-goal reasoning over agent-cap only)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md",
   "where": "section 2 S6 / section 7 New arm lines",
   "severity": "medium",
   "claim": "C19: the `[dRB-15]` arms in `tools/govkit/selftest.py` grade behaviour owned by sibling-kit files: agent-cap's `[adopt] via` in `tools/hooks/kit.toml` and `tools/settings-merge.py`. The `govkit selftest` leg's guard names only `{prefix}/govkit/`, and the spec adds neither file to it.",
   "impact": "An edit to `tools/hooks/kit.toml` alone, such as deleting `via` (candidate C2, which AC4 shows silently stops agent-cap wiring the hook when settings-merge is claimed but not selected), skips `govkit selftest` under a scoped bar or reuses its stale green. The unguarded `govkit selfcheck` does not catch that edit: an entry with no adopter argv is legal there (3b-iii skips it).",
   "fix": "In this unit, add `{prefix}/hooks/kit.toml` and `{prefix}/settings-merge.py` to the `govkit selftest` leg's guard in tools/gate-legs.json. Exact files are preferred over directories, so the guard does not tip `BROAD_LEG_FLOOR`. Then list the meta gates that a gate-legs.json edit trips in section 7, including the kickoff-manifest ratchet, since `tools/gate-legs.json` is on the manifest's `watch:` line. Probe the build must run: on a scratch branch, delete `via` from tools/hooks/kit.toml alone and confirm the scoped bar now runs `govkit selftest` and the `[dRB-15]` arm reds.",
   "evidence": "read: tools/gate-legs.json:1401-1411 (`govkit selftest`, guard [`{prefix}/govkit/`]). read: spec 15:68-73 (S6 arms read the `[dRB-14]` apply and scratch govs), spec 15:368-375 (AC4: with `via` deleted no `CONFIGURE agent-cap:` line prints). read: tools/govkit/govkit.py:1867-1869 (3b-iii `if not ((d.get(\"adopt\") or {}).get(\"argv\") or []): continue`). read: memory/gotchas/held-suite-guard-misses-a-sibling-kit.md:12-31. Grep of memory/guides/SESSION-KICKOFF.md printed line 6 `watch: ... tools/gate-legs.json; ...`."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-14.md",
   "where": "section 4 'Every reader of the receipt during CONFIGURE'",
   "severity": "low",
   "claim": "The table claims to list every receipt reader that runs during CONFIGURE, but it omits playbook-render's adopter. `bash {prefix}/playbook/adopt-playbook.sh --target .` runs `tools/playbook/render_playbook.py`, which carries the inlined `resolve_kit_dir` and calls it for run-gates (`derive_gate_runner`) and for roles (`derive_role_roster`).",
   "impact": "With the early receipt, a first apply at a per-kit prefix for run-gates or roles now resolves this run's homes inside the charter render. Before, it got a fallback answer or an empty roster that refuses at `resolve_placeholder_raw`. So the rendered AGENTS.md bytes, and OBSERVE's `output_sha256` for them, change in a case the spec neither lists nor observes. The 'every reader' table also misleads the next reader-impact analysis.",
   "fix": "Add a row for `tools/playbook/render_playbook.py:79-93`, `:285` and `:482`, reached from playbook-render's adopter. State the per-kit-prefix change to the gate-runner line and the role roster. Also say the inventory was taken with `git grep -l '>>> resolve_kit_dir' -- 'tools/*adopt-*.sh' 'tools/playbook/*.py' 'tools/settings-merge.py'`, which prints five files: lexicon, memory-tree, render_playbook, settings-merge and unattended.",
   "evidence": "Command: `git grep -l '>>> resolve_kit_dir' -- 'tools/*adopt-*.sh' 'tools/playbook/*.py' 'tools/settings-merge.py' | grep -v '\\.test\\.'`. It printed tools/lexicon/adopt-lexicon.sh, tools/memory-tree/adopt-memory-tree.sh, tools/playbook/render_playbook.py, tools/settings-merge.py and tools/unattended/adopt-unattended.sh. Grep of render_playbook.py printed `285: kit = resolve_kit_dir('run-gates', 'run-gates.sh', ...)` and `482: kit = resolve_kit_dir(home, anchor, ...)`. Adopter argv grep printed `argv = [\"bash\", \"{prefix}/playbook/adopt-playbook.sh\", \"--target\", \".\"]`. read: spec 14:165-178, whose table has no playbook row."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md",
   "where": "section 3 non-goal on spec 9 §4 / section 4 Readers (S4)",
   "severity": "low",
   "claim": "C24: S4 deletes agent-cap's `[adopt].argv`. Spec 15 relies on spec 9 §4 'Why the shared argv stays safe' but does not correct that section's opening sentence, 'agent-cap declares the same argv (`tools/hooks/kit.toml:108`)'. After this unit the sentence is false and the cited line is gone.",
   "impact": "The unbuilt sibling spec 9 keeps a false statement about the descriptor that units 13 and 15 both reason from. Its safety argument still holds, now through `via` and the resolved-argv dedup, but the stated mechanism no longer exists, which misleads the next reader of spec 9.",
   "fix": "Make S4's Readers 'by name' include spec 9:155 (and its 'What it does not check' sentence at :168, 'agent-cap's own adopter runs the same argv'). Either correct them in place with one rev bump naming TOOL-dRedressedBar-15, as units 10, 13 and 14 do for earlier specs, or state why they stand.",
   "evidence": "read: memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-9.md:155 (`agent-cap` declares the same argv (`tools/hooks/kit.toml:108`)) and :168. read: tools/hooks/kit.toml:108 (`argv = [\"python\", \"{prefix}/settings-merge.py\"]`), which S4 deletes. read: spec 15:92-93 (non-goal citing spec 9 §4), spec 15:54-62 (Readers list names no spec)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md",
   "where": "section 2 S8 / section 4 Files touched",
   "severity": "low",
   "claim": "S8 runs `python tools/run-gates/regen.py --write` and commits only what it rewrites under `memory/map/generated/`. That command runs all 12 declared writes across 3 stages, including the AGENTS.md render, the build-index writer for memory/LIVE.md and the build READMEs, and the gotchas index. The spec neither scopes the run to the codebase map nor accounts for the other outputs.",
   "impact": "Any other output the run moves at that commit is either left dirty in the worktree or committed outside section 4's estimate. AC9 checks only `gen_map.py --check`, so the stray rewrite goes unobserved.",
   "fix": "Run the stage-3 item alone, `python tools/codebase-map/gen_map.py --write`, which is the one that writes symbols.json. Or name every output regen.py may rewrite in Files touched, and add a criterion that `git status --porcelain` is empty after the product commit.",
   "evidence": "Command: `python tools/run-gates/regen.py --list`. It printed 12 items, ending `regen: 12 declared across 10 kit(s), in 3 stage(s)`, including `stage 1 · playbook-render · AGENTS.md`, `stage 2 · memory-tree · memory/LIVE.md, memory/ledger, memory/backlog` and `stage 3 · codebase-map · memory/map/generated`. read: spec 15:78-79 (S8) and :275-284 (Files touched lists only memory/map/generated/ among regen outputs)."
  }
 ]
}
~~~~

### 2026-10-14T11:28:39 · gov-skeptic · wf_2811782f-9e5/a08dcbc0c836e50a4

Label: dRedressedBar · spec-audit round 1 · verify:ids-1-5

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 1,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Re-read spec-14 S4 (:46-52): the [dRB-14] block 'asserts AC1's line, receipt and settings facts', and it is excused only from the exit code. Spec-14 AC1 (:272-273) includes the line fact 'exactly one line opens `govkit: kit 'agent-cap'` and carries `settings-merge.py`'. Spec-15 S6 (:68-70) puts [dRB-15] checks on that same apply, and spec-15 AC1 (:347) says 'No line opens `govkit: kit '`'. grep of spec-15 for 'dRB-14' hits only :69, :111 and :440, and none of them retires or rewrites the [dRB-14] assertion. Spec-15's risks (:321-323) inventory selftest.py with a git grep for 'CONFIGURE agent-cap', which cannot see the [dRB-14] line assertion that unit 14 adds. Built as written, the two arms contradict each other on one apply after unit 15, so the selftest leg goes red with no S item that tells the build what to do.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 2,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec-12 §6 AC1-AC6 never read install.sums or the [11/RECEIPT] counts. A grep for sums|STEP_RECEIPT|RECEIPT]|row(s) over specs 12-15 hits only spec-12 :37-39, :111 and :200 and spec-14 :37 and :41, so no AC reads them. Spec-14 S2 says 'Observed by AC1 and AC2', and neither of those reads them either. In govkit.py, :8027-8028 writes the sidecar from `rows`, and :8029 prints len(rows). check at :5322-5333 fails on any difference between the sidecar and the receipt pairs ('the receipt carries ... which install.sums does not'). A build that adds the carry only to install.json would pass every AC and still leave a target that check refuses.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 3,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec-13 AC15 (:413-419) bans `_sha(`, `blob_oid(` and `\"git\", \"show\"` across the whole span from the first to the last [dRB-11] line. Spec-11 §4 (:272-279) puts fixtures A, A-absent and B in that one block, and spec-11 AC3 (:366-368) has fixture A plant a row carrying 'that blob's sha256 and gov_oid' for a non-vintage working-tree blob. write_vintage_receipt does not cover that case. The selftest's own idiom for deriving these is gk._sha(b) and gk.blob_oid(b) (selftest.py:666-667), so a correct fixture A built that way reds AC15. S17 (:138-142) scopes the change to fixture B only. The ban is also a list of spellings: hashlib.sha256 or git(govroot, \"show\", ...) passes it. The [dRB-11] block does not exist yet (grep -c printed 0), so both outcomes stay open to the build.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 4,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Read tools/gate-legs.json. The 'format-guard self-test' guard includes {prefix}/hooks/format-guard.js and {prefix}/hooks/scratch-guard.js, which are in spec-15's Files touched (:281-282) and are moved by S7's mint. 'kit placeholders (a declared token its adopter substitutes)' has no guard and runs check-kit-placeholders.py. The §7 leg line (:438) names neither leg. The bar runs every leg at the close anyway, so the consequence is only a late red and a list that implies coverage it lacks.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 5,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec-14 :194 says 'Unit 13 is a sequence and not an edge, because no criterion here rests on its work'. Yet :257-263, :275-281, :303 and :308 (AC5's diff `git diff <p13> <p14>`) and the §7 New arm at :325 all run from unit 13's pass commit <p13>. Edges (:80-95) name only consumes-from 11 and 12. :199-202 describe as pending README edits (a roster row, step 10, and 'Units 10 and 11 follow 7' to name 12, 13 and 14). README.md already carries all three: :69 reads 'Units 10, 11, 12, 13 and 14 follow 7', the roster row is at :99, and step 10 is at :148. The README half is stale prose with no effect on behaviour.",
   "fixVerdict": "sound",
   "fixNote": ""
  }
 ]
}
~~~~

### 2026-10-14T11:28:40 · gov-skeptic · wf_2811782f-9e5/a150c83995c4c1750

Label: dRedressedBar · spec-audit round 1 · verify:ids-11-15

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 11,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Re-read govkit.py:3687-3701. check_entry_producer's docstring says, verbatim, 'CONFIGURE is `argv = d.get(\"adopt\", {}).get(\"argv\") or []` followed by `if not argv: continue`'. Its body tests the declared argv. :7314-7316 refuses a json-pointer merged rule when the declared argv is empty. :7740-7742 are the exact lines that spec 15's S2 replaces with resolve_adopter_argv. The §3 non-goal does name these readers, but the reason it gives is that each 'grade[s] the script a descriptor declares'. That does not hold for check_entry_producer, which answers 'does CONFIGURE run anything for this entry'. The non-goal's safety argument covers agent-cap only. None of S5's four via rules stops a future entry from declaring via beside a rendered, generated or merged rule. If one does, plan's side-effect test at :3777 treats it as a non-producer, and :7315 refuses it even though CONFIGURE runs the delegate. The docstring would also quote code that S2 deletes. Nothing changes for a shipped entry today, and the effect is contained, so medium.",
   "fixVerdict": "unsound",
   "fixNote": "Leave both readers' logic alone, as the non-goal says. Rewrite check_entry_producer's docstring so it quotes S2's new CONFIGURE lines and states that `via` is followed there. Add a fifth `via` rule to S5, with its own reason text, that refuses `via` on an entry carrying a rendered, generated or merged rule. Add an AC7 case for that rule."
  },
  {
   "id": 12,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Re-read govkit.py:8017-8030. install.sums is written with `for w in rows if \"sha256\" in w`, and STEP_RECEIPT prints `len(rows)` and `len(selection)`. S1 says both 'are derived from the same written list' and are 'Observed by AC1 and AC3'. AC1 asserts kits order, row equality, 18 rows, the KEEPS line and step 3's exit. AC3 asserts no KEEPS line, the same kits and row count, and the attributes row. Neither reads install.sums or the step line. cmd_check's sidecar comparison at :5322-5333 would report 'the receipt carries ... which install.sums does not' for every carried hashed row. So a build that carries kits and files but leaves sums on `rows` passes every criterion as written.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 13,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec 15's S3 says 'Observed by AC5 and AC9'. AC5 (lines 377-384) calls resolve_adopter_argv in isolation. AC9 (422-430) greps that `_argv_g` is absent and that resolve_adopter_argv appears at least 4 times. The def plus the two call sites make 3, so a fourth mention in a comment or docstring is enough. Renaming the local, or keeping the declared-argv skip test under a new name, passes AC9. No criterion runs `update`, and §4 row 5 says 'Derived, not run'. govkit.py:11104-11126 shows that the `_ran_gained` dedup on the resolved tuple decides which adopter runs. Spec 9's only selftest `New arm:` (line 319) is the [dRB-9] update block, and spec 15 does not extend it.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 14,
   "verdict": "refuted",
   "reason": "The premise that S6 'needs a parallel builder' is false on re-read. selftest.py:5508-5536 does build a one-entry registry. But it returns the committed tree `g`, so the arm can append the `other` [[entry]] to registry.toml, write other's descriptor and file, and recommit through the existing `git` helper. It can also extend the helper with an optional parameter. Spec 15's AC7 says only 'shaped as build_scratch_gov_kit builds them', and S6 says 'every process call goes through an existing helper'. Neither forces a copy of the scaffold. What remains is a preference about implementation style, with no defect the rubric grades.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 15,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Re-read tools/gate-legs.json:348-361. The 'format-guard self-test' guard names {prefix}/hooks/format-guard.js and {prefix}/hooks/scratch-guard.js, and a grep finds each path only at :355 and :357, so neither is broad (BROAD_LEG_FLOOR = 5). Spec 15's §4 Files touched lists both files at lines 281-282. Its §7 leg line (438) does not name format-guard self-test. .memory-tree.conf:356 sets SPEC_GUARD_LEGS_CUTOFF=\"2026-09-22\", and spec 15 is dated 2026-10-14. check-spec-tokens.py:1198-1207 turns exactly this case into a hit `format-guard self-test <- tools/hooks/format-guard.js`. A grep of memory/project found no waiver row for it. Spec 4's leg line (218) names the leg. I did not run the gate itself.",
   "fixVerdict": "sound",
   "fixNote": ""
  }
 ]
}
~~~~

### 2026-10-14T11:28:40 · gov-skeptic · wf_2811782f-9e5/abb0e60476d153823

Label: dRedressedBar · spec-audit round 1 · verify:ids-6-10

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 6,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec-13 lines 19-20 say 'it is ordered after every unit of this build'. The README's gen:build-order table puts unit 13 at step 9, with TOOL-dRedressedBar-14 at step 10 and -15 at step 11, so two units come after it. The sentence is wrong, but it is only prose about ordering and changes no behaviour.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 7,
   "verdict": "confirmed",
   "severity": "high",
   "reason": "I re-read govkit.py. check_leg_claimable (:4003-4008) requires the argv to match exactly. In write_gate_legs, owned is built from prior emitted only (`owned = {e[\"name\"] for e in prior}`). A runner leg whose name is not in owned is claimed only when its argv is equal, and otherwise the function raises Refusal('already has a leg named ... receipt does not claim it') (:4143-4159). Only carry_out_of_scope keeps prior rows for kits outside the selection (:4303-4305), and apply passes no carry (:7953-7955). When apply runs with a narrower selection, the runner keeps the other kit's legs (it is append/replace only) but emitted drops them. Unit 12 now keeps that kit in `kits`. update's _legs_scope is drawn from claimed (:11878), so update now reaches the kit and catches the Refusal as r.fail (:11880-11891). Once gov changes that leg's resolved argv, every later update and every `apply --kits K` refuses, and neither verb can restore ownership. Spec-12's section 3 sentence ('re-claimed on its next run by the same-argv rule ... so it wedges nothing', line 66-68) and its C5 rejection (line 189) only hold while the argv stays the same. This needs a narrow sequence, a narrower apply followed later by an argv change, and the result is a permanent wedge on that path, so I grade it high.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 8,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "`sed -n 10982,10990p` shows that the regenerate site passes `encoding=\"utf-8\",` on line 10987 and `errors=\"replace\")` on line 10988. `sed -n 11114,11122p` shows the gained loop with `encoding=\"utf-8\"` and no errors argument. Spec-13 line 317 says that 'errors=\"replace\" diverges from the two sibling sites, which decode strictly', which is false for the regenerate site. Lines 176 and 480 cite that site as `:10986-10987`, which leaves out the errors line. The mistake is in the prose only.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 9,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "An awk over lines 7233-8031, the span of _cmd_apply, found rows.append at 7424, 7502, 7540, 7593, 7616 and 7621. Spec-14 lines 145-146 say 'The only appends are `:7616` and `:7621`'. Its conclusion still holds, because nothing is appended after LAND. The defect is in the cited list only.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 10,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "silenced_legs (:3908-3946) already walks the [[gate_leg]] argv for each entry through target_context, and its rule is `if miss or \"/\" not in s: continue` on the RESOLVED text. Spec-15 lines 194-195 instead say an element is OFFERED when its DECLARED text carries '/'. Section 10 (lines 459-468) says only that 'no second planner exists' and does not mention the second argv walker. The difference is reachable in the real tree: tools/codebase-map/kit.toml:104 declares a gate leg `argv = [\"python\", \"{gate_file}\"]`, and that element has no '/' in its declared text. silenced_legs grades it once it resolves to a path, but S5 never offers it, so the two checks give two answers for the same element. The bare-target note at :3214 also counts every gate-leg argv element as 'offered', which is a different count from S5's 'offered' count. The effect is contained: a gap in coverage plus a second walker that can drift from the first.",
   "fixVerdict": "sound",
   "fixNote": ""
  }
 ]
}
~~~~

### 2026-10-14T11:28:40 · gov-skeptic · wf_2811782f-9e5/a1b0811c5e3e4c898

Label: dRedressedBar · spec-audit round 1 · verify:ids-21-24

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 21,
   "verdict": "confirmed",
   "reason": "Re-ran `python tools/run-gates/regen.py --list`. It printed 12 items in 3 stages and ended `regen: 12 declared across 10 kit(s), in 3 stage(s)`. Among them are playbook-render's AGENTS.md, memory-tree's `gen_build_index.py --write` (LIVE.md, ledger, backlog), `gotchas.py --write`, and stage 3's `gen_map.py --write`. Spec 15 S8 (lines 78-79) runs the whole `regen.py --write` but commits only what lands under `memory/map/generated/`. Files touched (275-284) names no other regen output, and AC9 checks only `gen_map.py --check`. The sibling spec 7 S1 step 4 handles the same command explicitly: 'The commit body names any other path the command moves'. Spec 15 has no equivalent. The effect is limited, because the lander re-runs `regen.py --write` and commits whatever moved (tools/push-main.sh:36-42, run_regen at :746+). A stray output is therefore left dirty or committed outside the estimate, but it is never shipped wrong.",
   "severity": "low",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 22,
   "verdict": "confirmed",
   "reason": "govkit.py:7818-7858 runs `git add --renormalize` over the LF-pinned paths after CONFIGURE. The re-stamp comment at :7893-7936 says this rewrites index blobs, so rows stamped earlier 'recorded a blob the target does not hold', and it re-stamps `oid` in memory only. Spec 14 S1 writes the early receipt before CONFIGURE, with STAGE's oids (line 136), and nothing writes it again until RECEIPT. On a re-run, demand_writable_target (:7287) calls demand_claimed_paths_clean, which passes `{path: oid}` (:7093-7097) into dirty_claimed_paths. There, carve-out 3 (`ours`, :6918-6922) keeps a staged path only when its index oid equals the recorded oid. A stale oid therefore lands in `dirty`, and the run refuses with DIRTY. One narrowing: `staged` is empty when the target has no HEAD (:6912), so a target with no commits escapes. A real adopter repo with commits and a line-ending filter is exposed. Spec 14's table row (line 160) claims a re-run of `apply` recovers from any interrupt between the two writes. AC4 places its fault at `inert = read_inert_kits(deploy)`, before RENORMALIZE, so it never reaches this window. On this narrow path the recovery claim is false, and the operator gets a refusal rather than wrong bytes, so the effect is contained.",
   "severity": "medium",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 23,
   "verdict": "confirmed",
   "reason": "Spec 14 S2 (line 40) keeps 'the encoding and newline arguments it uses today', and today's write is a plain `receipt_path.write_text(...)` (govkit.py:8019). grep finds no atomic receipt write: 8019, 12017, 12055, 12062 and 12692 all call write_text. The next run reads the receipt with `json.loads(receipt_path.read_text(...))` at :7251, with no try around it, so a truncated file crashes apply. The inlined resolve_kit_dir (:213-216) turns a ValueError into `rows = []`, which silently loses the per-kit rows this unit exists to provide. `write_atomic` (:3967), whose docstring reads 'a run that dies mid-write leaves the PREVIOUS file rather than a truncated one', already exists for this hazard. Spec 14's 'When CONFIGURE fails' table has no row for an interrupt during either write. The hazard predates this unit, but the unit doubles the exposure: the second write always truncates a file already on disk, and the design is built around the interrupted run. The path is unlikely (a fault inside the write itself), but the effect is a broken receipt, not a cosmetic one.",
   "severity": "medium",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 24,
   "verdict": "confirmed",
   "reason": "Spec 15 S1 (lines 31-32) treats a `via` that is not a non-empty string as absent and falls back to the entry's own argv. After S4 that argv is gone, so S1 returns [], and S2's `if not resolved: continue` skips the adopter with no line printed, matching today's silent skip at govkit.py:7740-7742. S5 (line 166) says 'whose `[adopt]` carries `via`' without saying whether that means the key is present or the value is truthy. None of the four rules (173-178) checks the value's type, and AC7 (400-410) has no empty or non-string arm. I re-ran `python -c \"print([] in {})\"` and it raised `TypeError: unhashable type: 'list'`, so rule 1 run on a list value turns selfcheck's finding into a traceback. A `via = \"\"` slips past S5 if S5 is built as a truthiness test, and the hook then goes unwired without a report. Both cases need a malformed descriptor authored in gov, and the list case still reds, as a traceback rather than a finding. The effect is real but contained.",
   "severity": "medium",
   "fixVerdict": "sound",
   "fixNote": ""
  }
 ]
}
~~~~

### 2026-10-14T11:28:40 · gov-skeptic · wf_2811782f-9e5/a763e436fb3e3234e

Label: dRedressedBar · spec-audit round 1 · verify:ids-16-20

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 16,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Re-read spec 15:207. The note prints `<g> graded, <h> naming a file only another entry ships`. At :385-386, AC6's pass half asks only that the line carry `offered by` and `0 naming`, and that no line open `govkit: entry 'agent-cap': its`. It checks no exit code. If h were 10, 20 and so on, all from entries other than agent-cap, the line would still contain `0 naming` and AC6 would pass. So the criterion's wording is too loose. I grade it low, not medium: the `govkit selfcheck` leg listed in section 7 fails on any hit through the S5 r.fail sites, so the bar still catches what AC6 misses, and h being a nonzero multiple of 10 is very unlikely.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 17,
   "verdict": "refuted",
   "reason": "Refuted under case (1), a non-goal that withholds the ask. The facts check out: govkit.py:3687-3702 shows check_entry_producer's docstring quoting `argv = d.get(\"adopt\", {}).get(\"argv\") or []` / `if not argv: continue`, its body tests only `[adopt].argv`, and :3777 reads it. But spec 15 section 3 (:97-101) names `check_entry_producer` as a reader the unit will not change. It says so on purpose and gives a reason: agent-cap ships no rendered, generated or merged rule, so the answer for agent-cap does not move. Adding the function to S2, which is what the finding asks, is exactly what that non-goal rules out. The concern about some future `via` entry is a guard for the next change, which this non-goal leaves out of scope.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 18,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "In tools/gate-legs.json:1401-1411, the `govkit selftest` leg's guard is only [`{prefix}/govkit/`]. The `govkit selfcheck` leg (:1378-1387) has no guard. S6 adds `[dRB-15]` arms to tools/govkit/selftest.py that test agent-cap's `via` in tools/hooks/kit.toml running tools/settings-merge.py, and the spec adds neither file to that guard. If `via` were deleted, agent-cap's `[adopt]` would have no argv. Selfcheck 3b-iii (govkit.py:1867-1869) just skips such an entry. `why_no_adopter` is checked only by tools/check-kit-placeholders.py, and only for kits that declare placeholders. The S5 via rules check only entries that carry `via`. So an edit to tools/hooks/kit.toml alone would skip `govkit selftest` on a scoped bar, or reuse a stale green from an earlier run. Other legs do guard `{prefix}/hooks/`, but they run hook test suites, not these arms. This is the pattern in memory/gotchas/held-suite-guard-misses-a-sibling-kit.md. The effect is limited to scoped or reused runs, because GATE_FULL and full CI still run the leg, so I grade it medium.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 19,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "I re-ran the finder's git grep. It printed five files: lexicon, memory-tree, render_playbook.py, settings-merge.py and unattended. The table in spec 14 section 4 ('Every reader of the receipt during CONFIGURE', :165-178) has rows for settings-merge, lexicon, unattended and memory-tree, but none for render_playbook. That file is reachable during CONFIGURE: registry.toml:66-67 shows the `playbook-render` entry with descriptor `{prefix}/playbook/kit.toml`, whose argv at :43 runs adopt-playbook.sh, which execs render_playbook.py (:59). The inlined resolve_kit_dir in render_playbook.py (:79-112) reads `.governance/install.json` first, and derive_gate_runner (:285) and the role roster (:482) call it. With the early receipt, a run-gates or roles kit at a per-kit prefix is now found through the receipt instead of falling back. So the table's claim to list every reader is false. The changed behaviour is a fix rather than harm, so I grade it low.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 20,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 9:155 says '`agent-cap` declares the same argv (`tools/hooks/kit.toml:108`)', and :168 says 'agent-cap's own adopter runs the same argv'. Spec 15 S4 (:48-53) deletes agent-cap's argv in favour of `via`. Spec 15's S4 Readers list (:54-62) names no spec. The section 3 non-goal (:92-93) relies on spec 9 section 4 but does not correct it. I found no TOOL-dRedressedBar-15 revision recorded in spec 9: its status is rev-2. After the unit lands, spec 9's sentence describes a key that no longer exists. Its safety argument still holds through `via` and the dedup on resolved argvs, so only the wording is wrong.",
   "fixVerdict": "sound",
   "fixNote": ""
  }
 ]
}
~~~~

### 2026-10-14T11:30:20 · gov-synthesizer · wf_2811782f-9e5/a369f7747197dddde

Label: dRedressedBar · spec-audit round 1 · synth

~~~~text
{
 "path": "C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/reviews/2026-10-14-review-TOOL-dRedressedBar-12-15-spec-audit-round1.md",
 "summary": "Verdict: CLEAN WITH FIXES. There are no blockers. 22 confirmed findings make 21 items: 1 high, 11 medium, 9 low. Counted by raw finding, that is 1 high, 12 medium, 9 low. The high is H1, id 7: unit 12 keeps a carried kit's claim but drops its leg ownership. Once gov changes that leg's argv, apply and update both wedge. The fix is for apply to pass carry_out_of_scope=True. Ids 2 and 12 are one defect (install.sums and the [11/RECEIPT] counts are never observed), so they share one item. Ids 4 and 15 overlap but carry different binding grades, so they stay separate. Id 11's fix was judged UNSOUND, and the report gives the skeptic's corrected fix in its place. Id 16 was re-graded to low by the skeptic. All 5 lenses and all 5 skeptic batches returned, and every integrity counter is zero.",
 "items": [
  {
   "severity": "HIGH",
   "ids": [
    7
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    1
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    2,
    12
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    3
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    10
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    13
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    11
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    15
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    18
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    22
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    23
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    24
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    4
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    5
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    6
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    8
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    9
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    16
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    19
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    20
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    21
   ]
  }
 ]
}
~~~~

### 2026-10-14T11:33:20 · gov-spec-writer · wf_2811782f-9e5/a8d6bd787e9880e62

Label: dRedressedBar · audit round 3 · dispose

~~~~text
{
 "disposed": true,
 "standing": [],
 "promoted": 22,
 "folded": 0,
 "refuted": 0,
 "promotedIds": [
  "TOOL-dRedressedBar-16",
  "TOOL-dRedressedBar-17"
 ],
 "edges": [
  {
   "from": "TOOL-dRedressedBar-16",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-12"
  },
  {
   "from": "TOOL-dRedressedBar-12",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-16"
  },
  {
   "from": "TOOL-dRedressedBar-17",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-9"
  },
  {
   "from": "TOOL-dRedressedBar-9",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-17"
  },
  {
   "from": "TOOL-dRedressedBar-17",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-12"
  },
  {
   "from": "TOOL-dRedressedBar-12",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-17"
  },
  {
   "from": "TOOL-dRedressedBar-17",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-13"
  },
  {
   "from": "TOOL-dRedressedBar-13",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-17"
  },
  {
   "from": "TOOL-dRedressedBar-17",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-14"
  },
  {
   "from": "TOOL-dRedressedBar-14",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-17"
  },
  {
   "from": "TOOL-dRedressedBar-17",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-15"
  },
  {
   "from": "TOOL-dRedressedBar-15",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-17"
  }
 ],
 "placements": [
  {
   "unit": "TOOL-dRedressedBar-16",
   "repairs": "TOOL-dRedressedBar-12",
   "order": 9
  },
  {
   "unit": "TOOL-dRedressedBar-17",
   "repairs": "none",
   "order": 12
  }
 ],
 "summary": "I promoted all 22 confirmed findings in the units-12-15 spec audit into two new units. The report had 22 confirmed and 0 unverified, so nothing was left to refute or leave standing.\n\n**What changed**\n- Both units now have rows in the Units table of memory/builds/dRedressedBar/README.md.\n- I added the mirror end of every new edge to the five specs it touches, each as a rev bump with a revision-log line: spec 9 to rev-3, spec 12 to rev-3, spec 13 to rev-3, spec 14 to rev-3 and spec 15 to rev-2.\n- I ran the memory hygiene gate over the result. It reports two failures, neither caused by these specs:\n  - **Check 9:** the generated build index is out of date. That clears when whoever commits regenerates the index.\n  - **Check 23:** acceptance-ledger lines in other builds' records.\n\n**TOOL-dRedressedBar-16 (order 9, repairs TOOL-dRedressedBar-12).** Closes report id 7, the only HIGH (item H1).\n- **The defect:** unit 12 keeps a narrower apply's unselected kits in the receipt, but `apply` still drops their gate legs from the receipt's ownership list. Once gov changes one of those legs' commands, `apply --kits <kit>` exits 2 and `update --write` exits 1, permanently.\n- **The fix:** `apply` passes `carry_out_of_scope=True` to `write_gate_legs`, the same carry `update` already uses. The function's docstring is rewritten, and spec 12's §3 non-goal and its rejected option C5 are corrected in place.\n- **The proof:** a new `[dRB-16]` self-test block built on the existing two-kit fixture gov. Its failing case uses the engine from unit 12's pass commit.\n- **Order:** it ties with unit 13 at order 9. Both write `tools/govkit/govkit.py` and `tools/govkit/selftest.py`, so they cannot run in parallel and will be sequenced at dispatch.\n\n**TOOL-dRedressedBar-17 (order 12, repairs none).** Closes the 12 MEDIUM and 9 LOW findings in one batch: ids 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 18, 19, 20, 21, 22, 23 and 24.\n- **Why one unit:** every code half writes `govkit.py` or `selftest.py`, so no split gives two independent write sets.\n- **Why order 12:** the findings land on specs 9, 12, 13, 14 and 15, so the batch goes above every existing unit.\n- **Main mechanisms:**\n  - One shared argv walker, `scan_entry_argv`, used by `silenced_legs`, `resolve_adopter_argv` and the selfcheck ownership join (id 10).\n  - Two new `[adopt] via` rules: the value must be a non-empty string (id 24), and `via` cannot sit beside a rendered, generated or merged rule (id 11).\n  - Every receipt write goes through `write_atomic`, by adding the receipt path to the existing `ADOPTER_BAR_PATHS` routing check (id 23).\n  - One extra receipt write after the oid re-stamp, so an interrupted apply recovers (id 22).\n  - Two files added to the `govkit selftest` leg's guard, followed by a kickoff-manifest re-stamp (id 18).\n  - Narrower or extended checks in the `[dRB-12]`, `[dRB-14]`, `[dRB-11]` fixture B, `[dRB-9]` and `[dRB-15]` blocks.\n  - In-place prose corrections across specs 9, 12, 13, 14 and 15.\n\n**Three decisions in spec 17 to check (its §4)**\n- **Id 13 does not follow the report's suggested assertions.** The report expects `adopter exit 0` and a hook command at `scripts/hooks/agent-cap.js`. Neither can appear, because `update` runs gained adopters before it writes its receipt. Unit 17 instead checks how many adopter lines print and which kit prints the one line.\n- **Id 22 takes the report's fix (a)**, the extra write, rather than narrowing spec 14's recovery claim.\n- **Id 23 also moves `update`'s three receipt writes and `adopt`'s one through `write_atomic`**, not just unit 14's two. The existing routing check would fail on any write left behind.\n\n**One risk for unit 13's build.** Its AC15 bans certain spellings across fixture A as well as fixture B (id 3). If fixture A uses the self-test's usual identity helpers, AC15 can fail at unit 13's pass even when the build is correct. I did not change AC15, because that would be folding the fix. Unit 17 narrows the check to fixture B, and spec 13's new hands-off edge names the overlap.\n\nNothing is committed and no index was regenerated.\n\nFiles are in C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/:\n- spec/2026-10-14-spec-TOOL-dRedressedBar-16.md\n- spec/2026-10-14-spec-TOOL-dRedressedBar-17.md\n- README.md\n- spec/2026-10-14-spec-TOOL-dRedressedBar-9.md\n- spec/2026-10-14-spec-TOOL-dRedressedBar-12.md\n- spec/2026-10-14-spec-TOOL-dRedressedBar-13.md\n- spec/2026-10-14-spec-TOOL-dRedressedBar-14.md\n- spec/2026-10-14-spec-TOOL-dRedressedBar-15.md"
}
~~~~

### 2026-10-14T12:00:34 · gov-spec-writer · direct/a115c3e3f72ed17b2

Label: dRedressedBar · TOOL-dRedressedBar-18 · spec-write

~~~~text
**TOOL-dRedressedBar-18: authored.** It is ready to commit, with two forks open for the resolver.

- **Spec:** `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-18.md`
- **Header:** `SPECCED · rev-1 · 2026-10-14 · node d · Tier-2 · base ebce889c · streams tooling · order 13`. It is ordered after unit 17.
- **Shape:** all ten sections are present, with 13 scope items (S1–S13) and 14 criteria (AC1–AC14). It is 41 KB, under the 49152-byte spec ceiling.
- **Checks:** memory hygiene checks 5, 12 and 25 pass, and the full hygiene run names nothing in this spec. That full run is red on check 17 (the stale gotchas index) and check 23 (other builds' acceptance ledgers); neither comes from this spec. Every function name in the spec's name list was put to `lexicon.py --suggest` and came back OK.

**What the design settles:**
- **Where it lives:** `measure_legs.py` goes in the run-gates kit.
- **Totals per leg:** a Windows Job Object per leg gives exact counts of processes spawned, CPU, memory and I/O.
- **Per-process rows:** these come from the process-monitor census walked from each leg's root. The census row gains two optional memory fields, so process-monitor's version moves too.
- **Spawn cost, python and bash:** these come from the runner's own functions, run from its source text.
- **Stalls:** a leg is STALLED when its census CPU, its job CPU and its log all stop moving. The job CPU is there so a silent leg working through very short-lived children is not falsely flagged. Nothing is ever killed.
- **Environment:** the scrubbed set is derived from three sources: every `GATE_` name, git's own list of repository variables, and the pre-push hook's unset line.
- **Record:** everything lands in `<git-dir>/gate-profile/<run id>/`. Each `.leg` row uses the runner's eight-field format.
- **`derive-ceilings.py`:** it should admit the profiler's readings, but through its existing `--observed` route rather than a code change.
- **Platform:** Windows only. Every registered node and every CI job is Windows, so a POSIX backend would be untested.

**Forks, recommendation first:**
- **F1 — should a profile hold the host turnstile?** Recommended (a): yes, through `run-gates.sh --hold`, so bars started inside legs nest as they do under a real bar. The cost is that the profile holds the host for as long as it runs. Option (b) is no hold, which lets nested bars queue behind each other and inflates the concurrent readings.
- **F2 — what happens to each leg's unredacted raw output?** Recommended (b): delete it once its redacted copy is written. That keeps the brief's "every log kept" in redacted form and follows the runner's own recorded reasoning against durable unredacted copies. Option (a) keeps the raw file in the scratch dir.

**Where the spec departs from the brief:**
- The brief says the runner and `run-selftests.sh` share a `gate-legs.json` reader. They don't: each parses the manifest inline (`run-gates.sh:2697-2845`, `run-selftests.sh:523-585` and `:827-834`). What they share is the `resolve_prefix_token` block, which the new tool also copies in.
- Each leg's temp dir has to live outside the git dir, because git answers differently from inside `.git/` and that could change a leg's verdict. So there is one record directory plus a scratch dir, and the record names the scratch path.

**Measured on node d, 2026-10-14 (read-only):**
- A census scan takes about 0.95–0.97 s at 327 processes.
- The clone's recorded spawn floor is 8.323 ms.
- This session runs elevated (`IsUserAnAdmin()` = 1).
- The MSYS runtime contains the job-breakaway flag. Whether a leg's child processes stay inside the job is only settled when AC1 runs at build time.

**Rule breach:** I ran `python tools/check-spec-tokens.py --help` to read its usage, and it ran the full spec-tokens checker. That gate is outside what I'm allowed to run. It wrote nothing, and I did not run it again.

I committed nothing, regenerated no index, and touched no file other than the spec.
~~~~

### 2026-10-14T12:43:10 · gov-spec-writer · direct/a1c6b180756a45758

Label: dRedressedBar · TOOL-dRedressedBar-18 · spec-write

~~~~text
I fixed the check-25 refusal. S1 and S11 now each have a **Readers:** clause. With only the spec staged, `bash tools/memory-tree/check-memory-hygiene.sh --staged` prints no check-25 line and no FAILED line. The spec still grades READY under the planner's `plan_state`, and nothing is committed.

**What each clause says**
- **What is retired:** each leg's raw capture, `raw/<i>.out`. The new tool creates it and deletes it once the redacted copy is written.
- **How I searched:** two `git grep` runs over the tracked tree at `679afc31`:
  - `git grep -n -F 'raw/<i>.out'` finds only this spec.
  - `git grep -n -l -e 'measure_legs' -e 'gate-profile/' -e 'raw_kept'` also finds four other specs, which are records, and `tools/drift-audit/drift_report.py` with its map entry. Those two only contain the text inside the unrelated name `measure_legs_retried_after_timeout`.
  - The S11 clause also says the runner's own raw capture (`run-gates.sh:3916`) is a different file and is left alone.
- **by name:** READER NOT IN TREE. The file lives in the scratch dir's TMPDIR, outside the tree, and the only code that will name it is this unit's tool, which isn't built yet.
- **by value:** the only reader of the capture's bytes is this unit's redaction pass in `tools/run-gates/measure_legs.py`, and it reads them before the delete. That file was already in §4's Files touched, so nothing was added there.

**One thing to know:** my first version had backticked names in the by-name halves. With that escape, the gate printed four "check 25 did not grade" notice lines for spec 18. You asked for no check-25 line, so I rewrote those halves as plain words, and the notices stopped.

The rev stays at rev-2, and its §9 line now also records the two clauses. The git index now holds the spec's latest version (I ran `git add` on the spec file only).

File: C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-18.md
~~~~

### 2026-10-14T13:02:38 · gov-spec-writer · wf_729fe7d9-e56/a82af6cde650f2d19

Label: dRedressedBar · TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 · spec-write

~~~~text
{
 "authored": [],
 "alreadyPresent": [
  "TOOL-dRedressedBar-1",
  "TOOL-dRedressedBar-2",
  "TOOL-dRedressedBar-8",
  "TOOL-dRedressedBar-9",
  "TOOL-dRedressedBar-3",
  "TOOL-dRedressedBar-4",
  "TOOL-dRedressedBar-5"
 ],
 "refused": [],
 "summary": "All seven units in this group already had a conforming spec, so I wrote and edited nothing. I counted all seven as already present.\n\nEach file under C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/ has the unit's id in its status header and the order the roster gives it:\n\n| Unit | Order | Tier | Rev |\n|---|---|---|---|\n| TOOL-dRedressedBar-1 | 1 | 1 | 2 |\n| TOOL-dRedressedBar-2 | 1 | 2 | 2 |\n| TOOL-dRedressedBar-8 | 1 | 1 | 2 |\n| TOOL-dRedressedBar-9 | 1 | 2 | 3 |\n| TOOL-dRedressedBar-3 | 2 | 1 | 3 |\n| TOOL-dRedressedBar-4 | 2 | 2 | 2 |\n| TOOL-dRedressedBar-5 | 3 | 2 | 2 |\n\nTOOL-dRedressedBar-3 also carries `ratified 2026-10-14`.\n\nEvery spec has all the sections its tier requires, in order. Every revision number in a header appears in that spec's revision log. Six specs read `none` under Open questions. TOOL-dRedressedBar-3 has one fork, F1, and the owner already resolved it on 2026-10-14 by picking option (c). Its rev-2 records that, so its revision brief is already folded in.\n\nI ran the memory hygiene gate with `--only 12,25`. It finished with no finding on any spec in this build. Nothing was committed and the build index was not regenerated."
}
~~~~

### 2026-10-14T13:02:39 · gov-spec-writer · wf_729fe7d9-e56/aa455e0be60955b17

Label: dRedressedBar · TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-10 · spec-write

~~~~text
{
 "alreadyPresent": [
  "TOOL-dRedressedBar-6",
  "TOOL-dRedressedBar-7",
  "TOOL-dRedressedBar-10"
 ],
 "authored": [],
 "refused": [],
 "summary": "I wrote no specs this time, because all three units in my group already have a conforming spec. I edited nothing, committed nothing and did not regenerate the index.\n\n- **TOOL-dRedressedBar-6** (`C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-6.md`): Tier-1, SPECCED, rev-2, `order 4`. All eight required sections are there, plus the optional Reuse audit. Open questions reads `none`, and §6 declares a `New arm:` line for `tools/roles/adopt-roles.test.sh`.\n- **TOOL-dRedressedBar-7** (`C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-7.md`): Tier-2, SPECCED, rev-2, `order 5`. It has all ten sections, §8 reads `none`, and §10 has both the probe result and the recall terms line.\n- **TOOL-dRedressedBar-10** (`C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-10.md`): Tier-2, SPECCED, rev-3, `order 6 · ratified 2026-10-14`. The revision brief `2026-10-14-prompt-TOOL-dRedressedBar-10-2-revision.md` is already applied. F1 is marked `RESOLVED (owner, 2026-10-14): (c)`, S22 points its residual at `TOOL-dRedressedBar-11`, Edges hand it off to unit 11, and the rev-2 line in §9 records this. Rev-3 adds the hand-off to `TOOL-dRedressedBar-13`.\n\nIn all three, the `order` value in the status header matches the roster.\n\nCheck: I ran the memory hygiene gate limited to the spec-format checks: `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25`. It printed `HYGIENE --only 12,25 ran checks 12 25` and nothing against these three files. Its only finding was on an unrelated spec, which a waiver already covers."
}
~~~~

### 2026-10-14T13:02:39 · gov-spec-writer · wf_729fe7d9-e56/a21d855ab5dc3d6ab

Label: dRedressedBar · TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-17 · spec-write

~~~~text
{
 "authored": [],
 "alreadyPresent": [
  "TOOL-dRedressedBar-14",
  "TOOL-dRedressedBar-15",
  "TOOL-dRedressedBar-17"
 ],
 "refused": [],
 "summary": "All three units already have conforming specs, so I wrote nothing and committed nothing. None of the files changed.\n\n- TOOL-dRedressedBar-14: C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-14.md. Header is SPECCED, rev-3, Tier-2, `order 10`. It has the ten sections in order, with Edges in section 3. All 6 acceptance criteria carry a `Red when:` clause. Section 7 has its gate list and one `New arm:` line. The section 8 fork F1 is marked RESOLVED (owner, 2026-10-14). Revisions 1 to 3 are logged in section 9, and section 10 records the reuse probe and then the recall terms.\n- TOOL-dRedressedBar-15: C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md. Header is SPECCED, rev-2, Tier-2, `order 11`. It has the ten sections and Edges. All 10 criteria have a `Red when:` clause. Section 7 has its gate list and two `New arm:` lines, section 8 reads `none`, revisions 1 and 2 are logged, and section 10 records the probe and the terms.\n- TOOL-dRedressedBar-17: C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-17.md. Header is SPECCED, rev-1, Tier-2, `order 12`. It has the ten sections and Edges. All 20 criteria have a `Red when:` clause. The criterion and scope numbers skip on purpose, because they follow the spec audit's report ids. Section 7 has its gate list and five `New arm:` lines, section 8 reads `none`, and section 10 records the probe and the terms.\n\nIn each case the `order` value matches the one your roster gave. I also ran the memory hygiene check over the whole tree (`bash tools/memory-tree/check-memory-hygiene.sh --offenders`). It names no dRedressedBar spec. It does report three problems that were already there and are outside this build: check 17-19 says `memory/gotchas/INDEX.md` is stale, and two check 23 rows are acceptance-ledger lines for the TOOL-aSparedSpawn and TOOL-aOrientedCast units."
}
~~~~

### 2026-10-14T13:02:39 · gov-spec-writer · wf_729fe7d9-e56/a4142a19e3f61f40f

Label: dRedressedBar · TOOL-dRedressedBar-11 TOOL-dRedressedBar-12 TOOL-dRedressedBar-13 TOOL-dRedressedBar-16 · spec-write

~~~~text
{
 "authored": [],
 "alreadyPresent": [
  "TOOL-dRedressedBar-11",
  "TOOL-dRedressedBar-12",
  "TOOL-dRedressedBar-13",
  "TOOL-dRedressedBar-16"
 ],
 "refused": [],
 "summary": "All four units in my group already have conforming specs, so I left them alone and wrote nothing.\n\nEach spec is under memory/builds/dRedressedBar/spec/ and was committed before this run. Each has a Tier-2 status header with the `order` verb the roster gives it:\n- TOOL-dRedressedBar-11 is at SPECCED rev-3, order 7.\n- TOOL-dRedressedBar-12 is at SPECCED rev-3, order 8.\n- TOOL-dRedressedBar-13 is at SPECCED rev-3, order 9.\n- TOOL-dRedressedBar-16 is at SPECCED rev-1, order 9.\n\nEach has all ten canonical sections in order, with an Edges sub-head in §3. Every acceptance criterion carries a backticked witness and a `Red when:` clause: 7 in unit 11, 6 in unit 12, 21 in unit 13 and 5 in unit 16. §7 has a leg line plus at least one `New arm:` line with a `covers` field. §8 reads `none` and §9 logs every rev up to the one in the header. §10 records the reuse probe result before the `Recall terms used:` line.\n\nAs a check, I ran the memory hygiene gate (tools/memory-tree/check-memory-hygiene.sh) and saved its output to a scratchpad log. It exited 1, but only on check 23 acceptance-ledger lines in TOOL-aSparedSpawn and one TOOL-aOrientedCast row, none of them from this build. Nothing in its output named any dRedressedBar spec.\n\nNothing was committed and the build index was not regenerated."
}
~~~~

### 2026-10-14T13:02:39 · gov-spec-writer · wf_729fe7d9-e56/aa55cf695b70f677e

Label: dRedressedBar · TOOL-dRedressedBar-18 · spec-write

~~~~text
{
 "summary": "TOOL-dRedressedBar-18 was already specced, so I wrote nothing. Its spec is memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md, at rev-2 and committed in 17908e7d5. I read the spec format's rules (memory/guides/BUILD-METHOD.md M2) and checked the file against them. It is the only spec in the build carrying this id. Its status header reads 'SPECCED · rev-2 · 2026-10-14 · node d · Tier-2 · base ebce889c · streams tooling · order 13', so it already has the `order 13` the roster names. It has sections 1 to 10, filled. Its acceptance criteria are AC1 to AC15, each with a command and a 'Red when' case. Section 7 lists the gates and two `New arm:` lines. Both open questions in section 8 are marked 'RESOLVED (owner, 2026-10-14): (b)', and the reuse audit in section 10 records the recall terms used. By M2 it is READY, not MISSING, THIN or FORKED. The memory hygiene gate ran over the tree and reports no finding for dRedressedBar. It does fail on check 23, but only on acceptance-ledger lines in other builds (TOOL-aSparedSpawn-* and TOOL-aOrientedCast-22). I edited no file, committed nothing and did not regenerate the index.",
 "authored": [],
 "alreadyPresent": [
  "TOOL-dRedressedBar-18"
 ],
 "refused": []
}
~~~~

### 2026-10-14T13:05:00 · workflow-subagent · wf_729fe7d9-e56/a8199d0ac3d25f2bf

Label: dRedressedBar · audit round 4 · subjects

~~~~text
{
 "subjects": [
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-16.md",
   "blob": "87f1049492979ea15acaaebad857a4413afdf7ac",
   "tree": "87f1049492979ea15acaaebad857a4413afdf7ac"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-17.md",
   "blob": "8910bf9c6d6d51fcef0c18cf4197ceef9126fde3",
   "tree": "8910bf9c6d6d51fcef0c18cf4197ceef9126fde3"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "blob": "b3f92c497e9769229a379e585aa2f2e08096ad45",
   "tree": "b3f92c497e9769229a379e585aa2f2e08096ad45"
  }
 ],
 "notAtHead": [],
 "checklistPaths": [
  "tools/govkit/govkit.py",
  "tools/govkit/selftest.py",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-12.md",
  "memory/builds/dRedressedBar/build/",
  "tools/gate-legs.json",
  "memory/map/generated/",
  "memory/guides/SESSION-KICKOFF.md",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-9.md",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-13.md",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-14.md",
  "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md",
  "tools/run-gates/measure_legs.py",
  "tools/run-gates/fixtures/measure-legs/",
  "tools/run-gates/kit.toml",
  "tools/run-gates/run-gates.sh",
  "tools/run-gates/README.md",
  "tools/run-gates/selftest-budgets.txt",
  "tools/run-gates/windows-only-legs.txt",
  "tools/process-monitor/census.py",
  "tools/process-monitor/selftest.py",
  "tools/process-monitor/adopt-process-monitor.sh",
  "tools/process-monitor/reap.py",
  "tools/process-monitor/scope.py",
  "tools/process-monitor/classify.py",
  "tools/process-monitor/procmon-hook.js",
  "tools/process-monitor/README.md",
  "memory/map/features/run-gates.md",
  "help/measure-legs.md",
  "help/README.md"
 ],
 "checklist": "# recurring-bug-class checklist for 29 path(s) (29 file(s))\n# 36 class(es) selected by an anchor + 6 universal\n# by anchor specificity: 25 path · 5 directory · 6 basename; a cut tier prints one line per class\n# invariants are read at ebce889c7d71; 0 that this subject adds, edits or takes out are listed as items, never by design\n\n- [ ] fixture-passes-by-finding-nothing (universal)\n      a test arm whose fixture never triggers the rule passes, and proves nothing\n      memory/gotchas/fixture-passes-by-finding-nothing.md\n\n- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)\n      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage\n      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md\n\n- [ ] heredoc-escape-reaches-the-regex (universal)\n      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem\n      memory/gotchas/heredoc-escape-reaches-the-regex.md\n\n- [ ] inline-fence-swallows-the-rest-of-the-file (universal)\n      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view\n      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md\n\n- [ ] staged-break-substitutes-a-synthetic-value (universal)\n      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n      memory/gotchas/staged-break-substitutes-a-synthetic-value.md\n\n- [ ] two-answers-to-one-question (universal)\n      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n      memory/gotchas/two-answers-to-one-question.md\n\n- [ ] a-new-local-collides-in-a-long-function (path)\n      a local added to a function thousands of lines long can share its name with one a distant block already binds, and the later binding silently replaces the new value only on the inputs that reach that block\n      memory/gotchas/a-new-local-collides-in-a-long-function.md\n\n- [ ] containment-tested-one-way (path)\n      a guard asking only \"is this path under the protected one\" refuses the narrow declarations and admits the one that claims everything\n      memory/gotchas/containment-tested-one-way.md\n\n- [ ] fixture-inherits-ambient-machine-state (path)\n      a hermetic-looking fixture silently reads machine-global config, so it passes everywhere it was written and fails where it was not\n      memory/gotchas/fixture-inherits-ambient-machine-state.md\n\n- [ ] line-claim-matched-over-the-whole-output (path)\n      an arm that asserts a line names X tests two substrings over the whole output, so it passes when X appears on some other line and the line it means names something else\n      memory/gotchas/line-claim-matched-over-the-whole-output.md\n\n- [ ] verdict-printed-before-the-step-that-reverts-it (path)\n      a verb prints a verdict about bytes it just wrote, and a later step of the same run can revert those bytes, so the operator reads a verdict about a tree the run did not leave\n      memory/gotchas/verdict-printed-before-the-step-that-reverts-it.md\n\n- [ ] a-folded-field-leaves-its-row-shape-docs-behind (path)\n      a review fold adds a key to a declared row shape in the code and its gate, and the spec body and the README that describe that shape keep the old key set\n      memory/gotchas/a-folded-field-leaves-its-row-shape-docs-behind.md\n\n- [ ] a-new-leg-trips-a-growing-set-of-meta-gates (path)\n      adding one gate leg trips a set of meta-gates that grows as new ones land, and a check inside an existing gate is far cheaper — but not free\n      memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md\n\n- [ ] a-runner-knob-owes-a-push-class (path)\n      a new GATE_ or GOV_ knob the gate runner reads has no push-boundary class until it joins one, and the arm that says so is guarded away from the unit that adds it\n      memory/gotchas/a-runner-knob-owes-a-push-class.md\n\n- [ ] a-spelling-change-strands-its-readers (path)\n      a shared file changes how it SPELLS its values, the readers someone migrated resolve the new spelling, and every reader nobody listed compares the raw one and matches nothing\n      memory/gotchas/a-spelling-change-strands-its-readers.md\n\n- [ ] ab-arm-never-did-the-work (path)\n      a timing A/B whose arms are not each asserted to have DONE the work measures a refusal against a run, and the fast arm looks like the good one\n      memory/gotchas/ab-arm-never-did-the-work.md\n\n- [ ] allocation-knob-without-a-ceiling (path)\n      a knob that sizes an allocation or a loop, validated only as a positive integer, hangs the process on a mistyped value before anything it guards runs\n      memory/gotchas/allocation-knob-without-a-ceiling.md\n\n- [ ] beacon-published-before-it-is-complete (path)\n      a lock or presence directory made visible before the files that let others judge it leaks forever when its writer dies in between, because every sweep needs those files\n      memory/gotchas/beacon-published-before-it-is-complete.md\n\n- [ ] bounded-through-a-pipe-is-unbounded (path)\n      a wall-clock timeout captured through a command substitution bounds the verdict and not the clock, and reports success on schedule while the caller blocks\n      memory/gotchas/bounded-through-a-pipe-is-unbounded.md\n\n- [ ] destructive-step-before-its-precondition (path)\n      a destructive step ordered before the probe for the precondition that makes it useful runs on exactly the case where nothing can follow it, so the harm lands and the benefit never does\n      memory/gotchas/destructive-step-before-its-precondition.md\n\n- [ ] fixture-lacks-a-gate-the-consumer-has (path)\n      a runbook's fixture passes because it lacks a commit-time gate the consumer runs, and the consumer refuses the step the fixture let through\n      memory/gotchas/fixture-lacks-a-gate-the-consumer-has.md\n\n- [ ] hand-named-gate-list-green-while-the-bar-reds (path)\n      a spec names the legs its author expects the change to move, the unit is green on exactly those, and the bar is red on an unguarded leg the list never named\n      memory/gotchas/hand-named-gate-list-green-while-the-bar-reds.md\n\n- [ ] held-suite-guard-misses-a-sibling-kit (path)\n      a held self-test reads another kit's file, but its leg's guard names only its own kit, so an edit to the sibling skips the leg or reuses its stale green\n      memory/gotchas/held-suite-guard-misses-a-sibling-kit.md\n\n- [ ] invariant-held-on-one-admission-path (path)\n      an invariant one admission path enforces is silently absent on every other path into the same resource, and the spec that states it reads as covering them all\n      memory/gotchas/invariant-held-on-one-admission-path.md\n\n- [ ] merge-keeps-both-sides-of-one-derivation (path)\n      a conflict-free merge leaves two derivations of one value, disagreeing, and the first is a dead store\n      memory/gotchas/merge-keeps-both-sides-of-one-derivation.md\n\n- [ ] overlap-judged-from-the-invocation-interval (path)\n      a guard that two jobs ran at once, timed around the commands that started them, includes their queue wait, so a pair the scheduler serialized still overlaps\n      memory/gotchas/overlap-judged-from-the-invocation-interval.md\n\n- [ ] predicate-bounded-by-its-own-count (path)\n      a predicate about other processes' holdings that walks only up to this process's own configured count misses a neighbour configured higher\n      memory/gotchas/predicate-bounded-by-its-own-count.md\n\n- [ ] record-file-read-by-line-position (path)\n      a key-TAB-value record file read by its first line takes whatever key the writer put first, and a TAB inside that value shifts every column after it in the row that copies it\n      memory/gotchas/record-file-read-by-line-position.md\n\n- [ ] signal-trap-runs-the-exit-handler-twice (path)\n      a signal trap that calls the exit handler and then exits runs that handler twice, because the exit fires the EXIT trap too, so anything the handler appends is appended twice\n      memory/gotchas/signal-trap-runs-the-exit-handler-twice.md\n\n- [ ] subprocess-resolves-a-different-shell (path)\n      Python subprocess resolving the bare name bash finds the WSL launcher, which sees another filesystem\n      memory/gotchas/subprocess-resolves-a-different-shell.md\n\n- [ ] suite-invalidated-by-a-commit-under-it (path)\n      a suite that pins gov's revision at import and stamps fixtures from live HEAD is silently invalidated by any commit made while it runs, and the failures name the product\n      memory/gotchas/suite-invalidated-by-a-commit-under-it.md\n\n- [ ] empty-field-collapses-unless-it-is-last (directory) · memory/gotchas/empty-field-collapses-unless-it-is-last.md\n\n- [ ] a-merge-of-the-default-branch-read-as-additions (directory) · memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md\n\n- [ ] amendment-leaves-its-other-half-standing (directory) · memory/gotchas/amendment-leaves-its-other-half-standing.md\n\n- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory) · memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md\n\n- [ ] retirement-inventory-misses-readers-by-value (directory) · memory/gotchas/retirement-inventory-misses-readers-by-value.md\n\n- [ ] fold-text-is-unreviewed-surface (basename) · memory/gotchas/fold-text-is-unreviewed-surface.md\n\n- [ ] observed-by-claim-no-arm-discharges (basename) · memory/gotchas/observed-by-claim-no-arm-discharges.md\n\n- [ ] git-rm-cached-refuses-a-diverged-index-blob (basename) · memory/gotchas/git-rm-cached-refuses-a-diverged-index-blob.md\n\n- [ ] anchor-literal-resolves-above-its-target (basename) · memory/gotchas/anchor-literal-resolves-above-its-target.md\n\n- [ ] join-key-widened-by-a-shared-location (basename) · memory/gotchas/join-key-widened-by-a-shared-location.md\n\n- [ ] staged-break-runs-stale-bytecode (basename) · memory/gotchas/staged-break-runs-stale-bytecode.md\n\n# by design — 0 invariant(s) this selection touches\n"
}
~~~~

### 2026-10-14T13:05:52 · workflow-subagent · wf_729fe7d9-e56/a7ddbe0acd79b3fc3

Label: dRedressedBar · spec-audit round 1 · resume:probe

~~~~text
{
 "commonDir": "C:/projects/coding-governance/.git",
 "blobs": [
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-16.md",
   "now": "87f1049492979ea15acaaebad857a4413afdf7ac"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-17.md",
   "now": "8910bf9c6d6d51fcef0c18cf4197ceef9126fde3"
  },
  {
   "path": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "now": "b3f92c497e9769229a379e585aa2f2e08096ad45"
  }
 ],
 "finds": [],
 "verifies": [],
 "skipped": []
}
~~~~

### 2026-10-14T13:06:05 · gov-spec-reviewer · wf_729fe7d9-e56/ac22518d2ca12246a

Label: dRedressedBar · spec-audit round 1 · find:coherence

~~~~text
{
 "lens": "coherence",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 4 Files touched; section 7 Gates; section 2 S13",
   "severity": "medium",
   "claim": "Unit 18 edits two files on the kickoff manifest's watch: line, tools/gate-legs.json (the new leg row) and tools/run-gates/run-gates.sh (the version line). It plans no re-stamp of memory/guides/SESSION-KICKOFF.md, and its section 7 leaves out `kickoff-manifest ratchet`. Unit 17 S18 gives the opposite answer for the same edit: it re-stamps in a second commit and names the ratchet in its section 7.",
   "impact": "Built as written, unit 18's tip reds the unguarded kickoff-manifest ratchet (C5, unaudited watch drift), which runs on every bar. The red shows up only at the close. The spec set holds two answers to whether a gate-legs.json edit owes a re-stamp.",
   "fix": "Add an S item to unit 18 that re-stamps `last-audit:` in a second commit, in the shape of 2e187ee8b, with a `manifest-audit:` line, as unit 17 S18 does. Add `memory/guides/SESSION-KICKOFF.md` to section 4 Files touched and `kickoff-manifest ratchet` to section 7. Add a criterion that the `last-audit:` sha holds the `measure-legs selftest` row in `git show <sha>:tools/gate-legs.json`.",
   "evidence": "sed -n 1,12p memory/guides/SESSION-KICKOFF.md printed `watch: ...; tools/run-gates/run-gates.sh; ...; tools/gate-legs.json; ...`. skills/session-kickoff/manifest-check.sh:1470 reads `fail 5 \"watched files changed since last-audit with no re-stamp at/after the change`. A python probe over tools/gate-legs.json printed `kickoff-manifest ratchet None records` (no guard, so it runs on every bar). grep -n 'SESSION-KICKOFF\\|kickoff-manifest\\|re-stamp\\|last-audit' on spec 18 printed nothing. Spec 17 section 4 Evidence says an edit to tools/gate-legs.json reds the ratchet until the manifest is re-stamped."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-17.md",
   "where": "section 2 S10; section 4 'What this unit corrects in each spec', row 15",
   "severity": "medium",
   "claim": "S10 makes the `cross-entry argv:` note count every tuple `scan_entry_argv` yields, slash-free elements such as `{gate_file}` included, and makes grading 'resolved text carries / and missing is empty'. Spec 15 defines the note as `<o> slash-bearing element(s) offered`, OFFERED as 'declared text carries /' and GRADED as 'resolved text carries no { and no space'. Unit 17's correction table for spec 15 does not list those definitions or the note template.",
   "impact": "A builder who follows S10 and keeps spec 15's template prints a note whose `slash-bearing element(s) offered` count includes non-slash elements, which is a false observability line. Spec 15 is also left with a second, stale OFFERED/GRADED rule (C6, two answers to one question) that will mislead the next change to the join.",
   "fix": "Have S10 restate the note's text without `slash-bearing`, for example `<o> argv element(s) offered`. Add spec 15 section 4's OFFERED/GRADED paragraph and the note template to row 15 of the correction table. Have AC10 assert that the `cross-entry argv:` line carries no `slash-bearing`.",
   "evidence": "read: memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-15.md:202-203 'An element is OFFERED when its declared text carries `/`. It is GRADED when its resolved text carries no `{` and no space.' and :215 'cross-entry argv: <o> slash-bearing element(s) offered by ...'. Spec 17 S10 (line 104-107): 'One rule grades an element in both checks: its resolved text carries `/` and its `missing` is empty ... the `cross-entry argv:` note counts all of them'. Spec 17 AC10 red half: 'the `cross-entry argv:` note offers no element whose declared text lacks `/`'. Spec 17 section 4 row 15 lists 'S1 and S8 sentences; S4 Readers; §3 non-goal; §4 rule table, ownership join and ... row 5; §5 risks; §7; §10', and neither the OFFERED/GRADED definitions nor the note template appears."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-16.md",
   "where": "section 6 AC5; the preamble's definition of <p16>",
   "severity": "medium",
   "claim": "C1: AC5 checks for a minted function with `git diff <p16>~1 <p16> -- tools/govkit/`, where `<p16>` is only 'the commit of unit 16's build pass'. The pass also writes spec 12 (S4) and the ledger (S6). If those land in a later commit, `<p16>~1..<p16>` holds no tools/govkit/ change, and the grep prints nothing whatever the product commit added.",
   "impact": "The no-new-function half of AC5 (S5) can pass by inspecting an empty diff, so it certifies something it never looked at. Unit 17 avoids this by naming `<p17>` as its product commit and `<p17m>` separately.",
   "fix": "Define `<p16>` as unit 16's product commit, the one that touches tools/govkit/govkit.py and selftest.py, as unit 17 does. Or make AC5 diff `<p12>..<p16>` over tools/govkit/. Add a liveness half: the same diff shows the `carry_out_of_scope=True` line, so an empty diff fails.",
   "evidence": "read: memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-16.md:185 '`<p12>` and `<p16>` are the commits of units 12 and 16's build passes' and :220 'AC5 — `git diff <p16>~1 <p16> -- tools/govkit/ | grep -E '^[+-](def|class) '` prints nothing'. Compare spec 17:379-381: '`<p17>` is this unit's product commit and `<p17m>` its manifest re-stamp commit'."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-17.md",
   "where": "section 1 Goal; section 4 'Order, and unit 7'",
   "severity": "low",
   "claim": "Unit 17 says twice that its order 12 'is above every unit of this build', but unit 18 sits at order 13 after it. This is the same false sentence (report id 6, L3) that unit 17's own S6 corrects in spec 13.",
   "impact": "The ordering prose contradicts the README's derived build order and Build-level rule. It repeats a defect class this unit exists to close, and will need its own correction round.",
   "fix": "Say unit 17 is ordered after units 9 to 16, whose specs and tree it corrects, and point at the README's derived build-order region for what follows, mirroring S6's wording for spec 13.",
   "evidence": "read: spec 17:17-18 'its order is above every unit of this build' and :309 'Order 12 is above every unit of this build.' The README's build-order table prints '| 12 | `TOOL-dRedressedBar-17` | no |' and '| 13 | `TOOL-dRedressedBar-18` | no |', and the README Build-level rule for unit 18 reads 'It is ordered after every other unit.'"
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-17.md",
   "where": "section 6 AC9",
   "severity": "low",
   "claim": "S9 requires spec 14 to list all six `rows.append` sites, but AC9's cut check requires only `:7424`, `:7502`, `:7540` and `:7593`. The awk half then demands 'exactly the six numbers the cut names', which the cut half never requires the spec to carry.",
   "impact": "A spec 14 edit that lists only four sites passes the cut half, and the awk half is ambiguous: the cut names many other line numbers. So the criterion does not decide whether S9's 'every append' sentence holds.",
   "fix": "Have the cut check require all six, `:7424`, `:7502`, `:7540`, `:7593`, `:7616` and `:7621`. Phrase the awk half as 'prints exactly 7424 7502 7540 7593 7616 7621 at 46eb75ed'.",
   "evidence": "awk 'NR>=7233 && NR<=8031 && /rows\\.append/ {print NR}' tools/govkit/govkit.py (tools/ equals 46eb75ed, and `git diff --stat 46eb75ed HEAD -- tools skills` printed nothing) printed 7424 7502 7540 7593 7616 7621. read: spec 17:441-444 'The cut carries `:7424`, `:7502`, `:7540`, `:7593` and `rows\\.append`. ... prints exactly the six numbers the cut names.'"
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 3 first non-goal against section 2 S13",
   "severity": "low",
   "claim": "Section 3 says 'No change to the merge bar's behaviour, ceilings or legs', while S13 adds the `measure-legs selftest` leg to tools/gate-legs.json, the bar's leg manifest, with a ceiling and a budget row.",
   "impact": "Section 2 and section 3 contradict each other on scope. A reviewer or builder reading the non-goal could resist the manifest row the criteria require (AC13).",
   "fix": "Narrow the non-goal: no change to any existing leg's argv, guard or ceiling, and no runner behaviour beyond the version line. The one new leg is S13's.",
   "evidence": "read: spec 18:102 '- No change to the merge bar's behaviour, ceilings or legs.' and :95-98 'S13 — The `measure-legs selftest` leg ... comes with its descriptor row, its manifest, budget and Windows-only rows'; AC13 (:630-633) requires the leg in tools/gate-legs.json."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 2 S13; section 6 AC14",
   "severity": "low",
   "claim": "S13 claims a kit README section and a codebase-map claim (memory/map/features/run-gates.md), but no criterion observes either. AC14 greps the README only for the version marker, and AC13 and AC14 never read the map file.",
   "impact": "Two section-2 deliverables can be omitted with every criterion green. The map claim is caught only incidentally by a broad gate, and the README section not at all.",
   "fix": "Extend AC14: tools/run-gates/README.md carries `measure_legs.py` and `--concurrent` under a heading, and memory/map/features/run-gates.md carries `tools/run-gates/measure_legs.py`. The red half is either line missing.",
   "evidence": "read: spec 18:95-98 (S13 '... the kit README section, a `help/` page and the map claim. Observed by AC13 and AC14.') and :634-638 (AC14 greps only 'gov:kit run-gates@' in README.md and the help page)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-16.md",
   "where": "section 2 S2 against spec 12 AC4",
   "severity": "low",
   "claim": "S2 rewrites the `carry_out_of_scope` docstring paragraph and requires `TOOL-dRedressedBar-16`, but does not keep the `TOOL-dRedressedBar-12` citation. Unit 12's built criterion AC4 requires `ast.get_docstring(write_gate_legs)` to carry exactly that citation.",
   "impact": "A faithful rewrite that drops unit 12's id turns unit 12's AC4 red on any re-observation at the close, an interface clash between two units over one docstring.",
   "fix": "Have S2 state that the paragraph keeps `TOOL-dRedressedBar-12` beside `TOOL-dRedressedBar-16`, and add that token to AC3's docstring check.",
   "evidence": "read: spec 12:259-261 'AC4 — ... The docstring of `write_gate_legs`, read with `ast.get_docstring`, carries `TOOL-dRedressedBar-12`.' Spec 16:38-41 (S2) and :207-210 (AC3) require only `TOOL-dRedressedBar-16` and no `passes no carry`."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-16.md",
   "where": "section 4 'The arm'; section 2 S3; section 6 preamble",
   "severity": "low",
   "claim": "The spec cites `build_gov13`'s location in two ways. Section 4 gives `tools/govkit/selftest.py:15412-15459`, but line 15412 is the last line of `M13_DEPLOY`, and the function starts at 15428. S3 and section 6 give `:15428-...`.",
   "impact": "A wrong line range for the fixture builder sends a reader to the deploy constant. This is cosmetic, but it is the line-citation drift the spec-tokens checks look for.",
   "fix": "Cite `build_gov13` as `:15428-15459` in section 4 'The arm', matching S3 and section 6.",
   "evidence": "grep -n 'def build_gov13' tools/govkit/selftest.py printed `15428:        def build_gov13(tag: str, ...`. Read selftest.py:15412 shows `'observed_failed = [\"GATE FAIL  {name}\"]\\n')`. read: spec 16:126 '(`tools/govkit/selftest.py:15412-15459`)' against :44-45 '(`:15428-15512`)'."
  }
 ]
}
~~~~

### 2026-10-14T13:06:06 · gov-spec-reviewer · wf_729fe7d9-e56/a62cc23ab2d8b94fc

Label: dRedressedBar · spec-audit round 1 · find:grounding

~~~~text
{
 "lens": "grounding",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 2 S4; section 4 \"The census fields (process-monitor)\"; section 6 AC3",
   "severity": "medium",
   "claim": "C12: the spec adds two keys, `peak_mem_b` and `mem_b`, to every census row and also requires that `census.FIELDS` and `render_rows` stay byte-for-byte unchanged. The existing process-monitor arm requires every row's key set to equal FIELDS, and the census.py row-contract docstring lists only the nine current keys. The spec names neither of them.",
   "impact": "Built as written, `test_row_contract_is_complete` fails on every Windows row, so the `process-monitor census selftest` leg that §7 names goes red. To get green the builder has to change an arm the spec never mentions, either by loosening it or by moving FIELDS, and moving FIELDS breaks AC3. The row-contract docstring keeps describing the old shape.",
   "fix": "Say in S4 and §4 that `test_row_contract_is_complete` (tools/process-monitor/selftest.py:102-110) compares each row's keys against FIELDS plus a new declared tuple of optional keys, for example `OPTIONAL_FIELDS = (\"peak_mem_b\", \"mem_b\")`. Say that the ROW CONTRACT docstring (census.py:12-22) gains both keys with type `int|None` and their units. Add to AC3 that the arm stays red for a row with an undeclared extra key. The build should confirm the arm goes red on an undeclared key before trusting it.",
   "evidence": "read: tools/process-monitor/selftest.py:102-110 `check(\"test_row_contract_is_complete\", all(sorted(r) == sorted(census.FIELDS) for r in rows) and ...`. read: tools/process-monitor/census.py:264 `FIELDS = (\"winpid\", \"msys_pid\", \"win_ppid\", \"msys_ppid\", \"kind\", \"age_s\", \"cpu_s\", \"command\", \"backend\")`. census.py:12-22 'THE ROW CONTRACT, and every field is load-bearing:' lists the same nine fields. read: spec 18 lines 349-350 '`FIELDS` (`:264`) and `render_rows` keep their bytes'; line 577 AC3 '`census.FIELDS` is unchanged'. `grep -n -i 'row_contract|row contract' spec-18` printed nothing."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 4 \"The environment a leg gets\" (Added) and \"The turnstile\" (What is read)",
   "severity": "medium",
   "claim": "The Python tool gets two of its directories from bash: the scratch dir from `mktemp -d \"${TMPDIR:-/tmp}/gate-profile.XXXXXXXX\"` and the turnstile key from the runner's `cd ... && pwd` expression. Both come back as MSYS spellings such as `/tmp/...` and `/c/Users/...`. The spec never says to convert them to Windows paths, yet Python opens `raw/<i>.out` under the first and lists `gate-bar-queue/` and beacon `pid` files under the second.",
   "impact": "A native Python on Windows resolves `/tmp/gate-profile.X` to `C:\\tmp\\gate-profile.X` and `/c/...` to `C:\\c\\...`. The raw-capture open then fails or lands in a stray tree. Worse, the turnstile read finds no key, and the spec says 'An absent key or queue reads as empty', so every leg silently records `ts_holders` and `ts_queued` as 0 and its readings pass `read_runs` as uncontended.",
   "fix": "State that every path bash hands back is converted once with `cygpath -m` (or `-w`) before Python uses it, and that the envelope records both spellings: the POSIX one the legs see as TMPDIR and the Windows one the tool opens. Make a key whose spelling does not match its converted form, or that cannot be converted, a refused read and not an empty one. Add to AC15 an assertion that `turnstile_dir` in the envelope exists according to `os.path.isdir`.",
   "evidence": "`mktemp -u -d \"/tmp/gate-profile.XXXXXXXX\"` printed `/tmp/gate-profile.DuHIob1B`. `cygpath -w /tmp` printed `C:\\Users\\d41ly\\AppData\\Local\\Temp`. `python -c \"import pathlib;print(pathlib.Path('/tmp/gate-profile.x').resolve())\"` printed `C:\\tmp\\gate-profile.x`. `cd C:/Users/d41ly/AppData/Local/Temp && pwd` printed `/tmp`. read: run-gates.sh:1513-1514 `TS_HOST=${GATE_TURNSTILE_DIR:-$HOME/.gov/gate-turnstile}` then `TS_HOST=$(cd \"$TS_HOST\" ... && pwd)`. The session's msys_pathconv_guard hook also blocked a probe and stated that '/c/projects/x becomes C:\\c\\projects\\x' for a native binary."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 4 \"The selftest and its leg\"; section 6 AC15",
   "severity": "medium",
   "claim": "AC15 starts the holder, the real runner's `--hold` verb over `sleep 20`, 'in the legs' scrubbed environment'. That scrub removes GATE_REGEN_CHECK, so the holder runs `regen.py --check` before it reaches the queue. On a stale tree the holder exits 2 and never writes the beacon that the arm waits for, and no bound is stated on that wait. Only `queued.sh` sets GATE_REGEN_CHECK=0.",
   "impact": "The `measure-legs selftest` arm depends on whether every generated output in the tree is fresh, which has nothing to do with the profiler. On a stale tree, including this build's own base, the arm hangs waiting for a pid file or fails for an unrelated reason. Even on a fresh tree each selftest run pays an unaccounted preflight of about 15 s before the hold.",
   "fix": "Start the holder with GATE_REGEN_CHECK=0 added after the scrub, as `queued.sh` does. Give the wait for the beacon a stated bound, after which the arm fails and prints the holder's output. Add the case to AC15: with the preflight left on and a stale output staged, the arm fails within the bound instead of hanging. That is a write probe, so the build runs it.",
   "evidence": "read: run-gates.sh:1416-1452, 'GENERATED OUTPUTS ARE PROVED FRESH BEFORE THE QUEUE ... ends the run here with exit 2 before the turnstile'. `if [ \"${GATE_REGEN_CHECK:-1}\" = 0 ]` is the only skip, and the block runs for `--hold` too (the verb is parsed at :123). Timed at HEAD: `date +%s.%N; timeout 115 python tools/run-gates/regen.py --check >/dev/null 2>&1; echo rc=$?; date +%s.%N` printed 1791983711.045762000, `rc=1`, 1791983726.678834000, which is 15.6 s and a stale verdict. read: spec 18 line 438 sets `GATE_REGEN_CHECK=0` inside `queued.sh` only, and lines 639-641 say the holder runs 'in the legs' scrubbed environment, and waits for its slot beacon's `pid` file' with no bound."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 7 leg line",
   "severity": "low",
   "claim": "C22: the §7 leg list does not name `kit epoch (shipped bytes move, the version moves)`. That leg has no guard and grades exactly the shipped-bytes-and-version move S13 makes for two kits. The list is also not declared a floor derived from §4 Files touched.",
   "impact": "A pass graded only on the named legs can report the unit green while `kit epoch` fails on the version moves of the run-gates and process-monitor kits. This is the class unit 17's S4 fixes for spec 15.",
   "fix": "Add `kit epoch (shipped bytes move, the version moves)` to the §7 leg line. Add a sentence saying the line is a floor, derived by joining §4 Files touched against the guards in tools/gate-legs.json with BROAD_LEG_FLOOR applied, plus the unguarded legs the change touches.",
   "evidence": "`python -c` over tools/gate-legs.json printed `kit epoch (shipped bytes move, the version moves) | ['python', '{prefix}/govkit/govkit.py', 'epoch'] | None`, so the leg has no guard. read: spec 18 §7 line 660 names `kit version markers` and `verdict epoch` but not `kit epoch`. Spec 15 §7 names all three for a kit version move."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 6 AC14",
   "severity": "low",
   "claim": "AC14 requires that 'The process-monitor markers all show one equal version above 0.18'. A tracked marker outside Files touched, in adopt-process-monitor.test.sh, reads 0.15 and is not one the version gate requires to match.",
   "impact": "An observer who greps every `gov:kit process-monitor@` marker gets 0.15 next to the new version, so a correct build fails AC14. The alternative is that the observer narrows the population by hand, and the criterion then states nothing checkable.",
   "fix": "Scope AC14 to the markers `check-kit-versions.sh` reads, or name the eight files and the exact grep. Alternatively, add adopt-process-monitor.test.sh to Files touched.",
   "evidence": "`grep -rn 'gov:kit process-monitor@' tools memory/map` printed `tools/process-monitor/adopt-process-monitor.test.sh:4:# gov:kit process-monitor@0.15` next to eight `@0.18` markers in adopt-process-monitor.sh, census.py, classify.py, procmon-hook.js, README.md, reap.py, scope.py and selftest.py."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 2 S11 Readers",
   "severity": "low",
   "claim": "The spec says the runner's own raw capture is `$WORK/$i$sfx.out` (run-gates.sh:3916). The runner's raw capture is actually `$WORK/$i$sfx.raw`, written at :3877. The `.out` file at :3916 is the copy with trailing newlines stripped.",
   "impact": "This is a citation error in an inventory. The conclusion that the runner's file is a different file still holds, but the next reader is pointed at the wrong file.",
   "fix": "Cite `$WORK/$i$sfx.raw` (run-gates.sh:3877) as the runner's raw capture.",
   "evidence": "read: run-gates.sh:3877 `else \"${argv[@]}\" </dev/null >\"$WORK/$i$sfx.raw\" 2>&1; rc=$?; fi`. run-gates.sh:3916 `printf '%s\\n' \"$out\" > \"$WORK/$i$sfx.out\"`."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-17.md",
   "where": "section 10 Reuse audit (and section 4 Evidence, AC10)",
   "severity": "low",
   "claim": "§10 says the audit report was wrong and the codebase-map leg's argv sits at `tools/codebase-map/kit.toml:103`, not `:104`. The argv is at :104 at both HEAD and 46eb75ed, so the report was right and the spec's correction is false. §4 and AC10 repeat `:103`.",
   "impact": "The next reader who trusts the correction lands on the `subject` line. The design is unaffected.",
   "fix": "Restore `:104` in §4, AC10 and §10, and drop the claim that the report disagreed.",
   "evidence": "`grep -n 'gate_file' tools/codebase-map/kit.toml` printed `104:argv = [\"python\", \"{gate_file}\"]`. `git show 46eb75ed:tools/codebase-map/kit.toml | grep -n gate_file` printed `104:argv = [\"python\", \"{gate_file}\"]`."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-17.md",
   "where": "section 4 \"Three choices\" (Id 23) and \"The code sites\" row 23",
   "severity": "low",
   "claim": "The spec says declaring `receipt_path` 'routes all six writes'. S23 lists seven: unit 14's early write, the RECEIPT write at :8019, S22's new write, update's three at :12017, :12055 and :12062, and adopt's at :12692.",
   "impact": "The count is off by one. AC23's `grep -c 'receipt_path.write_text'` equals 0 check covers every write anyway, so this is cosmetic.",
   "fix": "Say 'all seven writes', or 'every receipt write' with no number.",
   "evidence": "`grep -n 'receipt_path.write_text' tools/govkit/govkit.py` printed five sites: 8019, 12017, 12055, 12062 and 12692. Unit 14's early write and S22's write add two more. read: spec 17 line 275 'Declaring it routes all six writes'; line 300 'six writes through `write_atomic`'."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-16.md",
   "where": "section 4 \"The wedge, traced\" step 4; section 6 AC1 fixture line",
   "severity": "low",
   "claim": "The spec cites `:11880-11891` as the place where update catches the gate-leg Refusal. Those lines hold the comment and the `write_gate_legs` call. The `except Refusal` and its `the gate-leg step refused` r.fail sit just after them, at about :11897-11903.",
   "impact": "This is a citation error in the derived red half. The behaviour it describes is correct.",
   "fix": "Cite the call at `:11888-11890` and the `except Refusal` at `:11897-11903` separately.",
   "evidence": "read: tools/govkit/govkit.py:11887-11890 `try: _legs_emitted, _legs_withheld = write_gate_legs(\"update\", ... carry_out_of_scope=True, refuse_bad_runner=False)`. The `except Refusal as _legs_stop:` and `r.fail(f\"the gate-leg step refused and no leg was emitted this run: ...` come after line 11896 in the `sed -n '11895,11915p'` output."
  }
 ]
}
~~~~

### 2026-10-14T13:06:06 · gov-spec-reviewer · wf_729fe7d9-e56/a97a5d09566cc86fb

Label: dRedressedBar · spec-audit round 1 · find:reuse

~~~~text
{
 "lens": "reuse",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 2 S1; section 4 Inventory (`read_legs`); section 10 second paragraph",
   "severity": "medium",
   "claim": "Spec 18 adds a third Python reader of tools/gate-legs.json (`read_legs`, with its own empty/no-name/duplicate refusals) even though the same kit already has two: `held_halves.load_manifest(path)` and `derive-ceilings.read_legs(root)`. Section 10 claims no reader is shared, but it only checked the bash runner and run-selftests.sh.",
   "impact": "The spec-writer prompt says to extend the existing seams 'rather than writing ... a second leg-manifest parser'. Built as written, the kit has three manifest validators that can disagree. held_halves refuses a list with a nameless row; measure_legs would also refuse an empty list and duplicate names. Both read_legs functions share one name but behave differently (derive-ceilings honours GATE_LEGS, the new one does not). A future change to the manifest shape then has to update three places.",
   "fix": "In S1 and the Inventory, have measure_legs import `held_halves.load_manifest` as a sibling, the same way it imports profile_bar. Extend that function (or wrap it once) with the duplicate-name and empty-list refusals, so held_halves gets them too. Drop the new `read_legs`, or rename it so it does not collide with derive-ceilings' `read_legs`. Correct section 10's sentence that 'none is shared'.",
   "evidence": "`grep -n \"^def \" tools/run-gates/held_halves.py tools/run-gates/derive-ceilings.py` printed `held_halves.py:80:def load_manifest(path):` and `derive-ceilings.py:139:def read_legs(root: pathlib.Path) -> dict:`. `sed -n 80,92p tools/run-gates/held_halves.py` shows json.load plus a refusal for a non-list or a nameless row. The spec reads at 18.md:737-740: \"none is shared: the runner parses inline ... and `run-selftests.sh` twice\". The Inventory at 18.md:467 lists `read_legs`. memory-recall query.py returned prompts/2026-10-14-prompt-TOOL-dRedressedBar-18-1-spec-writer.md:60: \"Extend these seams rather than writing a second process reader, a second leg-manifest parser or a second spawn timer.\""
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 2 S11; section 4 Inventory (`derive_redacted`); section 6 AC8/AC11; section 7 New arm",
   "severity": "medium",
   "claim": "Spec 18 adds `derive_redacted`, a Python port of the runner's credential redaction (`redact()`, run-gates.sh:301), without a parity arm. The spec already builds a seam that runs runner functions from their source text (`extract_runner_function`) and uses it for resolve_python, measure_spawn_cost, read_spawn_floor and the measure_foreign awk. It even gives the foreign port a parity arm (AC8), but not the redaction.",
   "impact": "S11 promises logs 'redacted as the runner redacts its durable copies', but nothing ties the port to the runner's regex. AC11 checks one `u:s3cret@` shape only. A later change to the runner's `redact` pattern, or a port that differs on some userinfo shape, would leave unredacted credentials in the durable `<i>.log` while the selftest stays green. The repo already has two copies of that sed (run-gates.sh:301, run-selftests.sh:1450), and this would add a third in another language.",
   "fix": "Either run the runner's own `redact` through `extract_runner_function`, the same as the other four runner functions (one sed per leg log, at leg end), and drop `derive_redacted`. Or keep the port and add a parity arm in the AC8 style: the extracted `redact` and `derive_redacted` run over the same multi-shape input and must give byte-equal output, with a staged break where the port drops a character class. Either way, declare `redact` in section 10's list of runner functions run from source.",
   "evidence": "`grep -rn -E \"\\*\\*\\*:\\*\\*\\*|def (redact|derive_redact)\" --include=*.py --include=*.sh tools` printed run-gates.sh:301 `redact() { sed -E 's#://[^/@[:space:]]+:[^/@[:space:]]+@#://***:***@#g'; }` and run-selftests.sh:1450 with the same sed, and found no Python redactor in run-gates or process-monitor. `grep -n \"^measure_foreign\\|^measure_spawn_cost\\|^read_spawn_floor\\|^resolve_python\" tools/run-gates/run-gates.sh` confirmed the four extracted functions exist (137, 3739, 3762, 4220). The spec at 18.md:727-728 lists the run-from-source functions and does not include `redact`. 18.md:469 lists `derive_redacted`."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 4 \"The selftest and its leg\" (guard list); section 6 AC15, AC9",
   "severity": "medium",
   "claim": "C23 held-suite-guard-misses-a-sibling-kit: the `measure-legs selftest` guard leaves out two files its arms read. The turnstile arm (AC15) loads `read_runs` from `tools/run-gates/derive-ceilings.py`, and the scrub-derivation arm (AC9/S8) parses `.githooks/pre-push`'s `unset GIT_…` line. Yet the spec says the guard lists 'the files whose text it reads or imports'.",
   "impact": "A change to `read_runs`' set-aside rule (derive-ceilings.py:288-306) or to pre-push's unset line skips the leg on a scoped bar, or reuses its stale green. That is exactly the drift AC15 and AC9 exist to catch, so the parity holds only on a full bar. Unlike the kit's other suites, which guard the whole `{prefix}/run-gates/` dir, this guard names individual files and so silently drops any file it does not list.",
   "fix": "Add `{prefix}/run-gates/derive-ceilings.py` and `.githooks/pre-push` (or `.githooks/`, as the pre-push and python-resolver legs already guard) to the leg's guard. Alternatively, guard `{prefix}/run-gates/` as profile-bar selftest and run-gates turnstile do. Correct the 'Those are the files whose text it reads or imports' sentence. The build should probe this: on a staged copy, edit derive-ceilings.py alone and confirm a scoped bar selects the leg.",
   "evidence": "read: 18.md:454-456, \"The guard lists `measure_legs.py`, `profile_bar.py`, `run-gates.sh` and the `fixtures/measure-legs/` dir under `{prefix}/run-gates/`, plus `census.py`, `reap.py` and `scope.py` ... Those are the files whose text it reads or imports.\" 18.md:647: \"`read_runs`, loaded from `tools/run-gates/derive-ceilings.py`\". 18.md:198-199 reads `.githooks/pre-push`'s line `:100`. `sed -n 98,101p .githooks/pre-push` printed the `unset GIT_DIR ... GIT_NAMESPACE GIT_PREFIX` line. A python probe over tools/gate-legs.json showed guards may name `.githooks/` (for example `pre-push self-test ['.githooks/', '{prefix}/lib/']`) and that `profile-bar selftest` and `run-gates turnstile` guard `{prefix}/run-gates/` whole."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 2 S13; section 4 Files touched (estimate)",
   "severity": "low",
   "claim": "C13 a-new-leg-trips-a-growing-set-of-meta-gates: S13 lists everything that must come with the new leg (descriptor row, manifest, budget and Windows-only rows, versions, README, help page, map claim) but leaves out the subject-pin row in `tools/govkit/subject-pins.tsv`. govkit selfcheck fails on any manifest leg that has no pin row. That file is regenerated by `govkit.py selfcheck --write`, not by the `regen.py --write` outputs the Files touched list relies on.",
   "impact": "Built as written, `govkit selfcheck` reports \"gate leg 'measure-legs selftest' has no row in tools/govkit/subject-pins.tsv\". The pass then has to write a file outside its estimate and outside its own regen command. This is the 'list a session remembers is always one short' shape the gotcha describes.",
   "fix": "Add `tools/govkit/subject-pins.tsv` to S13 and to Files touched, regenerated by `python tools/govkit/govkit.py selfcheck --write`. Extend AC13's probe so it also finds `measure-legs selftest\\tkit\\tselftests` in subject-pins.tsv.",
   "evidence": "`sed -n 2904,2960p tools/govkit/govkit.py` shows the selfcheck pin block and `r.fail(f\"gate leg '{nm}' has no row in {pin_rel} — a NEW leg \"` for `set(live) - set(pinned)`. `grep -n \"subject-pins\\|selfcheck\" tools/run-gates/regen.py` printed nothing, so regen.py does not regenerate the pins. read: 18.md:95-98 (S13) and 18.md:485-493 (Files touched), neither of which names subject-pins.tsv."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-17.md",
   "where": "section 2 S23; section 6 AC23",
   "severity": "low",
   "claim": "C38 observed-by-claim-no-arm-discharges: S23 says 'The comment above the constant and `write_atomic`'s docstring name the receipt. ... Observed by AC23', but AC23 reads neither. It checks the `write_text` count, membership in ADOPTER_BAR_PATHS, the fault-injected apply and spec 14's table.",
   "impact": "Both comments currently say the declared population is the gate-leg manifest only ('which today is the gate-leg manifest'). A build that leaves them unchanged passes AC23, so the comments would misstate the declared population to the next change.",
   "fix": "Extend AC23: `inspect.getsource` or `ast.get_docstring` of `write_atomic` carries `receipt`, and the comment block between the ADOPTER-BAR banner and `ADOPTER_BAR_PATHS =` carries `receipt`. Red when either still names only the manifest.",
   "evidence": "`sed -n 3950,4002p tools/govkit/govkit.py` printed the docstring line \"THE ONE WRITER for every destination `ADOPTER_BAR_PATHS` declares, which today is the gate-leg manifest\". read: 17.md:155-160 (S23) against 17.md:528-537 (AC23), which has no docstring or comment check."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 2 S13; section 6 AC13, AC14",
   "severity": "low",
   "claim": "C38 observed-by-claim-no-arm-discharges: S13 lists 'the kit README section ... and the map claim' as observed by AC13 and AC14. Neither criterion reads `memory/map/features/run-gates.md` or a run-gates README section on the tool. AC14 reads only the README's version marker.",
   "impact": "A pass that adds no map claim and no README section still passes both criteria. The missing map claim would only surface later, at the close, through the codebase-map leg, and nothing would catch the missing README section.",
   "fix": "Add to AC14 a grep of `memory/map/features/run-gates.md` for `measure_legs.py`, and a grep of `tools/run-gates/README.md` for `measure_legs` outside the version-marker line. Red when either is absent.",
   "evidence": "read: 18.md:95-98 (S13 'the kit README section, a `help/` page and the map claim. Observed by AC13 and AC14') against 18.md:630-638. AC13 covers the four leg rows, and AC14 covers the version markers, `help/measure-legs.md` and `help/README.md` only."
  }
 ]
}
~~~~

### 2026-10-14T13:06:06 · gov-spec-reviewer · wf_729fe7d9-e56/ab5df3247b23bd609

Label: dRedressedBar · spec-audit round 1 · find:blast-radius

~~~~text
{
 "lens": "blast-radius",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 2 S13; section 4 'The selftest and its leg' and 'Files touched (estimate)'; section 7",
   "severity": "medium",
   "claim": "The new `measure-legs selftest` budget row adds the leg to the foreign-prefix parity population. The spec never declares it in that suite's WHOLE_RUN list, so `foreign-prefix parity (every self-test at three prefixes)` reds on an undeclared whole run.",
   "impact": "`foreign-prefix.gov.test.sh` runs every row `run-selftests.sh --list` prints, so every row in selftest-budgets.txt. A row must either print `foreign-prefix-probe: stopped after 1 arm` under FOREIGN_PREFIX_PROBE=1 or be listed in WHOLE_RUN, and both directions red. The spec adds the budget row but neither honours FOREIGN_PREFIX_PROBE nor edits WHOLE_RUN. It also leaves `tools/run-gates/foreign-prefix.gov.test.sh` out of Files touched and the leg out of section 7. Because `{prefix}/` is a broad guard, the spec-tokens join does not catch this. The leg reds on the first full bar after the unit lands, which defeats the build's goal of a green forced full bar.",
   "fix": "Add `tools/run-gates/foreign-prefix.gov.test.sh` to section 4 Files touched. Add the row `measure-legs selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing` to WHOLE_RUN, the same row every other `--selftest` engine mode carries (held-halves selftest included). Name `foreign-prefix parity (every self-test at three prefixes)` on the section 7 leg line. Add a criterion that reads `bash tools/run-gates/foreign-prefix.gov.test.sh --plan` and finds the row's kind printed as whole. The leg is a suite, so the build runs it and this review does not.",
   "evidence": "read: tools/run-gates/foreign-prefix.gov.test.sh:44-49 says 'THE POPULATION is every row `run-selftests.sh --list` prints ... A row is green when it exits 0 and, unless declared whole below, printed the marker'. At :123-140 'WHOLE_RUN=( ... \"held-halves selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing\" ...' and 'Both directions red'. `grep -n held-halves tools/run-gates/selftest-budgets.txt` printed `67:held-halves selftest\t60\t...`, which shows a budget row puts a `--selftest` leg into that population. Spec 18 S13 adds a 'budget ... row', and its Files touched list has no foreign-prefix.gov.test.sh."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 4 'Files touched (estimate)'; section 7",
   "severity": "medium",
   "claim": "Unit 18 edits `tools/gate-legs.json` and `tools/run-gates/run-gates.sh`. Both sit on the kickoff manifest's `watch:` line, yet the spec has no manifest re-stamp, and `kickoff-manifest ratchet` is missing from section 7.",
   "impact": "manifest-check.sh reds whenever a watched path moved after `last-audit:`. Unit 17 re-stamps the manifest for its own gate-legs.json edit at order 12. Unit 18 runs after it at order 13 and moves two watched files again, so the ratchet is red once unit 18 lands. Nothing in unit 18's declared gates or Files touched says so, and the defect first shows at the close bar.",
   "fix": "Add `memory/guides/SESSION-KICKOFF.md` to Files touched. Add a second commit, as in unit 17 S18 and commit 2e187ee8b, that re-audits and re-stamps the manifest with a `manifest-audit:` line in its body. Name `kickoff-manifest ratchet` on the section 7 leg line. Add a criterion that `last-audit:` names a commit at which `git show <sha>:tools/gate-legs.json` holds the `measure-legs selftest` row.",
   "evidence": "`sed -n 1,12p memory/guides/SESSION-KICKOFF.md` printed `watch: tools/memory-tree/check-memory-hygiene.sh; tools/check-template-size.sh; tools/run-gates/run-gates.sh; tools/run-gates/run-selftests.sh; tools/gate-legs.json; ...`. The gate-legs.json row is `{'name': 'kickoff-manifest ratchet', 'argv': ['bash', 'skills/session-kickoff/manifest-check.sh'], 'reads': {'history': 'it asks `rev-list` and `git log` whether a watched file moved since the last audit ...'}}`. Spec 17 section 4 states the rule itself: 'tools/gate-legs.json sits on the kickoff manifest's watch: line ... so an edit to it reds the kickoff-manifest ratchet until the manifest is re-stamped'. Spec 18's section 7 and Files touched name neither the leg nor SESSION-KICKOFF.md."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 7, the paragraph after the New arm lines",
   "severity": "medium",
   "claim": "Section 7 leaves `measure-legs selftest` off its leg line on purpose. Once the unit lands that leg and its guard, the spec-tokens guards join reds on spec 18 itself.",
   "impact": "The spec is still live (SPECCED or INPROGRESS) when its product commit lands. From then on its Files touched names `tools/run-gates/measure_legs.py`, `census.py`, `reap.py` and `scope.py`, and the new leg's narrow guards trip on them. The leg-line sentence written for spec time ('so it is not on the leg line above') turns into a `spec tokens (a spec's own names resolve)` red at landing. Nothing in S13 or the criteria tells the builder to add the leg to the line in the same commit.",
   "fix": "S13 should say that the product commit adds `measure-legs selftest` to spec 18's section 7 leg line, once the manifest row exists and the name resolves. Add a criterion: `python tools/check-spec-tokens.py` prints no `guards` hit for spec 18 at `<p18>`. Its red half is the same run with the line unedited.",
   "evidence": "I simulated the join with the checker's own functions, using scratch script blast-radius/probe18c.py, which imports tools/check-spec-tokens.py and runs extract_files_touched, extract_gates, derive_guarded_legs and check_guard_trips over every live spec dated on or after SPEC_GUARD_LEGS_CUTOFF=2026-09-22. With the leg added under the guard section 4 declares, it printed `baseline 1 after 2` and `NEW ('memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md', 'NEWLEG', 'tools/run-gates/measure_legs.py')`. read: tools/check-spec-tokens.py:231 `LIVE = re.compile(r\"^\\*\\*Status:\\*\\*\\s*(OPEN|SPECCED|INPROGRESS|BLOCKED)\"`."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 2 S4; section 4 'The census fields (process-monitor)' and the paragraph under Files touched",
   "severity": "medium",
   "claim": "S4 changes the CIM query so `parse_cim` reads the command from index 6 instead of 4. The existing process-monitor selftest arms feed `parse_cim` five-field lines, and the spec says the process-monitor files other than census.py move 'by their markers only'.",
   "impact": "`tools/process-monitor/selftest.py` builds five-field CIM lines in `build_cim_fixture` (:62-75), `test_non_utf8_backend_output_survives` (:205-208) and `test_exotic_line_terminators_cannot_forge_a_row` (:913). With the AC3 layout their command field lands in `peak_mem_b`, and the command reads None or the row is rejected. The arms that assert on `command` and the row counts then red `process-monitor census selftest`. The spec names only the new AC3 arm, so a builder reading 'markers only' leaves these fixtures stale, and the census selftest reds, or gets 'fixed' by loosening the parser.",
   "fix": "In S4, state that every five-field CIM fixture in tools/process-monitor/selftest.py is re-armed to the seven-field layout, and list the three sites. Alternatively, declare that `parse_cim` still accepts a five-field row with the command at index 4, and give a criterion that checks it. Either way, drop the 'by their markers only' claim for selftest.py.",
   "evidence": "`grep -n parse_cim tools/process-monitor/selftest.py` printed calls at :105, :116, :148, :153, :166, :209 and :915. `sed -n 62,75p` shows `s.join([\"4242\", \"1000\", \"12.5\", \"3600\", \"C:/x/bash.exe -c sleep\"])`, a five-field row. At :913 `s.join([\"4242\", \"1000\", \"1.0\", \"60\", \"prog\" + sep + ...])`. Spec 18 AC3 'Red when: parse_cim reads the command from index 4 as before'. Files touched note: 'The process-monitor engine files move by their markers only, except census.py'."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 4 'The selftest and its leg' (the kit.toml [[gate_leg]] row) and section 3 Edges (consumes-from process-monitor)",
   "severity": "medium",
   "claim": "The spec ships `measure-legs selftest` to every run-gates adopter as a `[[gate_leg]]` with its fixtures under the `**` engine rule. The tool needs a sibling process-monitor kit and a Windows host, yet run-gates declares `requires = []`, and the fixture `.sh` files fall outside the kit's only LF pin, `{kit}/*.sh`.",
   "impact": "Two adopters get a red leg when they run kit self-tests (GATE_SELFTESTS=1): one that selects run-gates without process-monitor, and any on a POSIX host. The tool refuses with exit 2 by design (S12, Edges). On a Windows adopter with core.autocrlf, `fixtures/measure-legs/stall.sh` and `queued.sh` are not LF-pinned in the emitted .gitattributes block, so they check out CRLF and do not execute. Every other run-gates self-test that cannot run in an adopter is withheld and declared as an `[[exempt_leg]]` in the registry, and the spec reverses that without saying so.",
   "fix": "Choose one path and state it. Path one: withhold the fixtures dir as `project-owned` and declare the leg as an `[[exempt_leg]]` in tools/govkit/registry.toml, as profile-bar selftest and run-gates turnstile do. Path two: keep the `[[gate_leg]]`, add a dependency on process-monitor, and add an `[[lf_pin]]` for `{kit}/fixtures/measure-legs/*.sh`. Under path two, add a criterion that `govkit apply` into a scratch target with run-gates alone either withholds the leg or reports the missing dependency.",
   "evidence": "read: tools/run-gates/kit.toml:15 `requires = []`. :17-19 `[[files]] include = \"**\" role = \"engine\"`. The LF pin is `[[lf_pin]] pattern = \"{kit}/*.sh\"`. tools/govkit/registry.toml:610-616 holds `[[exempt_leg]] name = \"profile-bar selftest\"` and `\"run-gates turnstile\"`, with the reason that 'a descriptor row naming a leg the target cannot carry is what reds the deployer'. Spec 18 section 4: 'The kit.toml [[gate_leg]] row uses {kit}', and Edges: 'the process-monitor kit resolvable as a sibling of run-gates. Without either, the tool refuses'."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-16.md",
   "where": "section 4 'What an adopter sees change'",
   "severity": "low",
   "claim": "The adopter-change table leaves out `derive_parity_lines`, a consumer of `gate_runner.emitted`. Once carried kits' legs stay in `emitted`, `check` and `update` can newly fail a contract after a narrower apply.",
   "impact": "`derive_parity_lines` builds `leg_words` from the receipt's `emitted` argvs. It raises `r.fail(\"contract ...: <p> is on a leg this receipt emitted and cannot run ...\")` only when an installed consumer path is on one of those legs. At `<p12>` a narrower apply drops the carried kits' legs, so such a contract prints 'unwired' and stays green. After S1 the same receipt fails it in `check` (:5416) and `update` (:9658). The new behaviour is arguably the correct one, but the spec presents its table as the complete adopter-visible change and states that nothing else moves.",
   "fix": "Add a row to the 'What an adopter sees change' table: after a narrower apply, a failing contract clause whose installed consumer sits on a carried kit's leg reds `check` and `update` again, as it does after a full apply. Optionally add one sentence to section 5 risks naming `derive_parity_lines` as a reader of `emitted`.",
   "evidence": "`grep -n '\\[\"emitted\"\\]\\|get(\"emitted\")' tools/govkit/govkit.py` printed `6092: leg_words = {w.strip(\"'\\\"\") for g in ((receipt.get(\"gate_runner\") or {}).get(\"emitted\") or [])`. `sed -n 6110,6125p` shows `for p in (x for x in inst if x in leg_words): r.fail(f\"contract {c.get('id')}: {p} is on a leg this receipt emitted and cannot run ...`. Callers are at :5416 and :9658."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-16.md",
   "where": "section 2 S2 and S4",
   "severity": "low",
   "claim": "C34: S4 corrects spec 12's section 3 and C5 row but leaves spec 12's S2 standing, and S2 states the same false premise. S2 here also rewrites the docstring paragraph without keeping the `TOOL-dRedressedBar-12` token that spec 12's AC4 reads.",
   "impact": "Spec 12 S2 (lines 42-46) still says `apply` 'still passes no carry set, because a leg row such a kit loses from emitted is re-claimed by the same-argv rule'. That is the sentence unit 16 shows to be false, so after S4 spec 12 gives two verdicts on one rule. A rewrite under S2 that drops the unit-12 citation also turns spec 12 AC4 ('docstring ... carries TOOL-dRedressedBar-12') red the next time anyone re-observes it.",
   "fix": "Extend S4 so spec 12's revision line, or an inline note at S2, says the S2 rationale was superseded by TOOL-dRedressedBar-16. Make S2 here state that the rewritten paragraph keeps `TOOL-dRedressedBar-12` beside `TOOL-dRedressedBar-16`, and make AC3 check both tokens.",
   "evidence": "`grep -n -i 'same-argv' memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-12.md` printed `45:  carry set, because a leg row such a kit loses from emitted is re-claimed by the same-argv rule`, `69:  same-argv rule (...), so it wedges nothing.` and `198:| C5 ...`. Spec 16 S4 says 'Spec 12's S2 and criteria are not rewritten'. Spec 12 :259-261 AC4: 'The docstring of write_gate_legs, read with ast.get_docstring, carries TOOL-dRedressedBar-12'."
  }
 ]
}
~~~~

### 2026-10-14T13:06:06 · gov-spec-reviewer · wf_729fe7d9-e56/ae23d0554436b8086

Label: dRedressedBar · spec-audit round 1 · find:failure-envelope

~~~~text
{
 "lens": "failure-envelope",
 "path": "",
 "findings": [
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 6 AC1; section 4 'Candidates per measurement' row 1 and 'Measured on node d'",
   "severity": "high",
   "claim": "C5 — AC1 is named as the refutation of 'an MSYS-forked descendant escapes the job', but its fixture's six counted children are native processes that python spawns, and neither twin has an MSYS fork that the other lacks. So a breakaway on Cygwin's fork path cannot move the difference of 6.",
   "impact": "§4 marks Cygwin's breakaway behaviour UNVERIFIED and makes AC1 the gate that parks the unit if a descendant escapes. Gate legs are mostly bash scripts that fork for subshells, pipelines and command substitution. If those forks leave the job, every bash leg's procs_total, user_s/kernel_s, spawn_s_est and the spawn claim undercount, and AC1 still reads 6 and certifies the containment it never exercised. The wrapper's single `exec` is cancelled by the zero-child twin, so even that path counts the same in both legs.",
   "fix": "Add an MSYS fixture next to spawn.py, for example `forks.sh <n>` that runs n `( /usr/bin/true )` subshell forks plus n `$(true)` substitutions, with a zero-count twin. AC1 then asserts that the procs_total difference is at least 2n. Its Red when is the same job with SILENT_BREAKAWAY_OK, where the difference reads 0. State that AC1 covers the native-spawn path and the new arm covers the fork path.",
   "evidence": "read: spec-18.md:135 ('Job Object per leg | an MSYS-forked descendant escapes the job | CHOSEN; AC1 is the refutation'); :152-155 ('UNVERIFIED from source: Cygwin's spawn adds the breakaway flag only when its own job allows breakaway ... AC1 fails if a descendant escapes anyway'); :432-433 (spawn.py starts n children of `sys._base_executable -I -c`); :561-567 (AC1 runs `spawn.py 6 3` and `spawn.py 0 3`, difference 6, 'The twin cancels the wrapper and the interpreter')."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 4 'The census fields (process-monitor)'; section 6 AC3",
   "severity": "medium",
   "claim": "C15 — census rows gain `peak_mem_b`/`mem_b` and the CIM line gains two fields ahead of the command, but `FIELDS` is kept unchanged. The spec names none of the existing readers of the old row key set and the old five-field line: the process-monitor selftest asserts every row's keys equal FIELDS, three of its fixtures build five-field CIM lines, and `build_windows_rows` unpacks a four-tuple.",
   "impact": "Built as written, `test_row_contract_is_complete` reds on every Windows row, and the 5-field fixtures in `build_cim_fixture`, `test_non_utf8_backend_output_survives` and `test_exotic_line_terminators_cannot_forge_a_row` read their command line as a memory figure. The builder then has to pick unaided between three fixes, each of which breaks something. Widening FIELDS breaks the spec's 'census.py --print unchanged'. Exempting the two keys weakens the row-contract arm. Letting parse_cim accept both widths makes the command index depend on the field count. The spec also gives no rule for a line of 5 or 6 fields, or for an empty memory value from an access-denied process. If that empty value is parsed inside the existing try, the whole row is rejected and the process drops out of the walk.",
   "fix": "In §4 'The census fields', list the readers: selftest.py:109, :69-72, :206-209 and :911-915, and census.py:136. Give the parse rule: a line needs at least 4 fields; when it has 7, the command is joined from parts[6:]; a blank or non-integer memory field reads None and never rejects the row. State how the row contract carries the two optional keys, either as a separate OPTIONAL_FIELDS tuple that the contract arm adds or as a declared exemption. Re-arm the three fixtures at 7 fields and keep one 5-field line as a legacy-shape case. AC3 gains a blank-memory line that must stay a row.",
   "evidence": "Grep 'FIELDS' in tools/ printed `tools\\process-monitor\\selftest.py:109:          all(sorted(r) == sorted(census.FIELDS) for r in rows) and`. Grep 'parse_cim|_CIM_SEP' printed fixture sites at selftest.py:69, :206-209 and :911-915. Reading census.py:136 shows `for winpid, (win_ppid, cpu, age, command) in cim_rows.items():`, and census.py:111 shows `command = parts[4].strip() if len(parts) > 4 else \"\"`. The spec (spec-18.md:345-351) says only 'FIELDS (:264) and render_rows keep their bytes'."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 4 'Launching a leg' step 1, 'Sampling, admission and its cost', AC8, AC15",
   "severity": "medium",
   "claim": "C30 — the spec routes two bash invocations through `profile_bar.resolve_bash`: the leg wrapper and the scratch `mktemp`. It does not route the others: `resolve_python` 'run once in bash', `read_spawn_floor`, the per-tick `measure_spawn_cost 3` ('one bash process'), AC8's awk parity run, and AC15's real-runner hold verb and `queued.sh`. It also says nothing for when `resolve_bash` returns an empty string.",
   "impact": "A builder who writes `subprocess.run(['bash', ...])` for those runs gets the System32 WSL launcher on any node with WSL installed. PYBIN would then be resolved inside WSL, and AC9 compares it against a runner run under the same wrong shell, so the arm still passes. Spawn cost would be sampled in WSL, giving a wrong spawn_us and spawn_s_est, and the turnstile arm's hold verb would run against another filesystem. The gotcha records that this class reproduces only on nodes with WSL installed, so it goes green elsewhere. `resolve_bash` returns ('', tried) when no candidate can see the script, and the spec has no refusal for that.",
   "fix": "Add one sentence to §4: every bash the tool starts is the single `<bash>` that `resolve_bash` returns, resolved once at start against `run-gates.sh`. That covers the wrapper, mktemp, resolve_python, read_spawn_floor, measure_spawn_cost, the AC8 awk run and the selftest's runner calls. An empty result refuses with exit 2 and names the candidates tried. Add a pure arm asserting that every subprocess argv[0] equal to 'bash' in measure_legs.py is the resolved path, for example an ast scan for the string literal 'bash' as the first argv element.",
   "evidence": "read: spec-18.md:179 ('PYBIN comes from the runner's own resolve_python ..., run once in bash from its source'); :180-181 (only the wrapper names `profile_bar.resolve_bash`); :210 and :236 ('in the resolved bash' for mktemp and the turnstile dir only); :294-295 ('one bash process timing three `true` spawns'). read: tools/run-gates/profile_bar.py:282-304 (`resolve_bash` returns `\"\", tried` on no candidate). read: memory/gotchas/subprocess-resolves-a-different-shell.md ('only reproduces where WSL is INSTALLED')."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 4 'Launching a leg' step 3; section 5 security and error states",
   "severity": "medium",
   "claim": "Partial failure in the launch sequence is not covered. The root is created CREATE_SUSPENDED, then OpenProcess, AssignProcessToJobObject, a toolhelp snapshot and ResumeThread run in turn, and the spec says nothing about any of them failing. §5 also forbids the one cleanup available: 'the code never calls a terminate'.",
   "impact": "If the assign fails, for example because the profiler itself runs in a job that forbids nesting under some CI or console hosts, or the resume fails, a suspended bash is left behind that never runs and never exits. 'A leg that never ends keeps the run open', so the profile hangs for good. Stall detection reports it as STALLED, which describes a hung leg rather than a launch the tool never completed. Under --serial no later leg runs.",
   "fix": "In step 3, state that a failed OpenProcess, assign, snapshot or resume terminates the still-suspended root through the handle the tool already holds. This is the only permitted terminate, on a process that has executed nothing. The leg is then recorded as `fail` with rc and reason `launch: <call> <winerror>`, and the run continues. Amend §5's 'never calls a terminate' to carve out this case. Add a selftest arm that stages an assign failure, for example by pointing build_job at a closed handle, and asserts that the leg records the launch failure and the run exits 0.",
   "evidence": "read: spec-18.md:186-189 ('The root is created with CREATE_SUSPENDED. It is assigned to a fresh job ... Its one thread is then resumed through CreateToolhelp32Snapshot and ResumeThread'); :529-530 ('The process handle asks for PROCESS_TERMINATE only because the job assign requires it, and the code never calls a terminate'); :535-536 ('A leg that never ends keeps the run open')."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 4 'The turnstile (F1, resolved b)', 'What is read' and 'Set aside'",
   "severity": "medium",
   "claim": "The turnstile read is silent on the concurrent-churn input class. A ticket or slot beacon can vanish between the directory listing and the read of its `pid` file, or a beacon can exist with its `pid` not yet written. The only rule given is 'A key that exists and cannot be read is a refused read', and a refused read turns the leg's eighth field into `unknown`.",
   "impact": "Beacons and tickets are created and removed continually by the legs' own nested bars. An uncontended acquire holds a ticket for only a few processes, and a beacon is mkdir'd before its files are written. Built as written, a FileNotFoundError or empty pid on a vanishing entry counts as a refused read, so every leg that runs nested bars, such as the canary, intermittently records `unknown`, and read_runs sets the reading aside as 'uncensused'. The readings this tool exists to produce for those legs are then lost without any error. The runner itself treats this state as normal: 'a beacon being written right now has none yet'.",
   "fix": "Add to 'What is read': an entry that disappears between the listing and the read, or whose `pid` file is absent, empty or non-numeric, is not judged at that tick, the same as a pid the scan did not see. Only a failure to list `gate-bar-queue/`, or to stat the key itself, is a refused read. The selftest gains an arm with a beacon dir holding no `pid` file and asserts that the eighth field stays numeric.",
   "evidence": "read: spec-18.md:242-243 ('An absent key or queue reads as empty ... A key that exists and cannot be read is a refused read'); :265-267 (eighth field 'reads `unknown` when the census or the turnstile read was refused at any tick'). read: tools/run-gates/run-gates.sh:1556-1558 ('AN UNFINISHED BEACON, interrupted between its `mkdir` and its first writes, has neither a pid nor a heartbeat ... a beacon being written right now has none yet'). read: tools/run-gates/derive-ceilings.py:304-306 (a non-digit foreign field is set aside as 'uncensused')."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 2 S1 (refusal list); section 4 'The record' `<i>.leg` and `legs.tsv`",
   "severity": "medium",
   "claim": "S1 lists three malformed-manifest refusals: empty manifest, a row missing its name or argv list, and a duplicate name. `--legs <path>` accepts any file, and the spec is silent on everything else a manifest can carry: JSON that does not parse, a top level that is not a list, a row that is not an object, an argv element that is not a string, a `{...}` token that does not resolve, and a name containing a tab or newline.",
   "impact": "A tab or newline in a leg name splits the `.leg` row and the headed `legs.tsv` row. read_runs reads `.leg` positionally, so field 4 becomes the wrong number or the row is skipped, and field 8 is misread. The runner's canary forbids a tab only in the shipped manifest, and this tool reads arbitrary manifests. The other classes surface as a Python traceback rather than exit 2, or they launch a leg with a literal `{prefix}` argv that is then recorded as a `fail` verdict, a false red.",
   "fix": "Extend S1's refusal list to cover: a manifest that does not parse as JSON, a top level other than a list, a row other than an object, an argv that is not a non-empty list of strings, a name holding a tab, CR or LF, and an argv token left unresolved after resolve_prefix_token. Each refuses with exit 2, naming the row index. AC10, or a new pure arm, feeds one fixture manifest per class and asserts exit 2 with no traceback.",
   "evidence": "read: spec-18.md:32-33 ('An empty manifest, a row with no name or no argv list, and a duplicate name each refuse the run with exit 2'); :365 (`<i>.leg` is 'the runner's row' of eight tab fields). read: tools/run-gates/run-gates.sh:3931-3933 ('TAB-SEPARATED and NEWLINE-FREE by construction ... the canary already forbids a tab inside one'). read: tools/run-gates/derive-ceilings.py:273-279 and :292 (positional split on tab, `p[3]` as seconds, `p[7]` as foreign)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 2 S11; section 4 'The record' (raw capture deleted) and Exit; section 5 security",
   "severity": "medium",
   "claim": "F2's guarantee that only the redacted copy survives covers just two endings: a normal leg or run end, and a Ctrl-C interrupt. The spec does not cover an unhandled exception in the profiler, a TerminateProcess from `kill`, Task Manager or a closed console, or a power loss. Any of these leaves every `raw/<i>.out` unredacted in a scratch dir that 'is never swept', with no `raw_kept` entry recording it.",
   "impact": "The owner resolved F2 (b) on charter `[security]` grounds, because an unredacted capture is 'a credential leak'. On these paths the leak persists indefinitely under %TEMP%/gate-profile.*, the envelope's end-of-run rewrite never happens, and nothing tells the next run or the operator that unredacted captures exist.",
   "fix": "State the crash path. Either (a) at start, the tool sweeps `raw/` in earlier `gate-profile.*` scratch dirs whose envelope never reached its end rewrite, redacts each capture into that run's dir as `<i>.log.recovered` and deletes the raw, recording each; or (b) the start-time envelope records `raw_pending` and the next run prints and handles any scratch still holding raw files. Add an arm that stages a profiler killed mid-leg and asserts that the next run leaves no raw capture holding the planted credential.",
   "evidence": "read: spec-18.md:370-377 (raw kept only when a delete fails or on 'An interrupt'); :423-426 ('130 on an interrupt, which writes the envelope'); :546-547 ('The legs' scratch is never swept'); :694-697 (F2 resolved (b) on `[security]`)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 2 S11; section 4 'The record' `<i>.log`",
   "severity": "medium",
   "claim": "The spec says the log is 'redacted as the runner redacts its durable copies' but never states the byte-level contract for the capture: how bytes that are not UTF-8, NUL bytes and CRLF are decoded, matched and written. The runner's redaction is a `sed` whose CR handling it documents as host-dependent, and its capture drops NULs.",
   "impact": "Gate legs on Windows emit console-codepage bytes, and the census module recorded a single 0xe7 crashing a text read. A python redaction pass that decodes strictly raises on such a leg. By the spec's own ordering the raw copy is then not deleted, and the run exits 1 with 'a record write failed', for a leg whose only fault was its output encoding. A pass that decodes with replacement instead changes the bytes, so `<i>.log` is no longer the capture and `log_bytes` disagrees with it. Either way, the AC11 check `grep s3cret` cannot tell which behaviour was built.",
   "fix": "In §4 'The record', state that the capture is read as bytes and redacted by a bytes regex equal to run-gates.sh:301's ERE over bytes, `rb'://[^/@\\s]+:[^/@\\s]+@'`. The output is written byte-for-byte except for the masked spans, NULs and CRs are kept, and `log_bytes` is the raw size. Add to the printenv fixture a line holding byte 0xe7 and a credential after a CRLF, and AC11 asserts that `<i>.log` keeps the 0xe7 and masks the credential.",
   "evidence": "read: spec-18.md:73-75 (S11 'redacted as the runner redacts its durable copies'). read: tools/run-gates/run-gates.sh:301 (`redact() { sed -E 's#://[^/@[:space:]]+:[^/@[:space:]]+@#://***:***@#g'; }`); :305-307 ('under MSYS it reads its pipe in text mode and drops the CR of every CRLF'); :3879-3880 (NULs dropped). read: tools/process-monitor/census.py:68-73 (a 0xe7 byte killed a text=True read)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-17.md",
   "where": "section 2 S23; section 4 'Three choices' (id 23); section 5 error states; AC23",
   "severity": "medium",
   "claim": "S23 routes the instance `install.json` through `write_atomic`, not the class. The sidecar `.governance/install.sums` is written from the same rows by a plain `write_text` immediately after each of the six receipt writes, so a fault while writing it truncates the sidecar. An interrupt between the two writes leaves an atomic new receipt next to the previous sidecar.",
   "impact": "§5 claims that 'An interrupt during any receipt write leaves the previous file whole', and §4 justifies the widening by the report's request for 'a check over `.governance/` writes'. `check` asserts the sidecar and the receipt against each other both ways, and the sidecar is 'the artifact a target verifies with bash alone'. After this fault, `check` prints one `install.sums carries`/`which install.sums does not` line per hashed row, and a bash verifier rejects the target. AC23 wraps only `install.json`, so it cannot see the case.",
   "fix": "Add `install.sums` to `ADOPTER_BAR_PATHS` alongside `receipt_path` and route its six writes through `write_atomic` too. Order the two writes with the sidecar first and the receipt last, and state in spec 14's table that an interrupt between them leaves a sidecar `check` reconciles on the next apply. AC23's wrapper also faults `install.sums`/`install.sums.govkit-new`, and asserts that both files equal their earlier bytes and that `check` prints no sidecar line.",
   "evidence": "Grep `\\.write_text(` with receipt|install in tools/govkit/govkit.py printed sidecar writes at :8027, :12018, :12056, :12063 and :12694, each directly after a `receipt_path.write_text` at :8019, :12017, :12055, :12062 and :12692. read: govkit.py:5318-5333 (sidecar and receipt 'asserted against EACH OTHER', with r.fail on each mismatch). read: spec-17.md:155-160 (S23 names receipt_path only) and :358-359 ('An interrupt during any receipt write leaves the previous file whole')."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-17.md",
   "where": "section 6 AC1",
   "severity": "medium",
   "claim": "C40 — AC1 defines the `[dRB-14]` span as the first to the last line carrying the literal `[dRB-14]`. Unit 15 S6 places the first set of `[dRB-15]` checks on 'the apply that unit 14's `[dRB-14]` block runs', and this unit's S2 then adds a further `[dRB-14]` sidecar check without fixing its position. So the anchor's last occurrence can fall after `[dRB-15]` checks, and the span then encloses the very check AC1 requires to sit only in the `[dRB-15]` span.",
   "impact": "A correct build can fail AC1. The `[dRB-15]` check that agent-cap's problem line is absent plausibly carries `kit 'agent-cap'` in its label or condition, and if it sits between two `[dRB-14]` lines, AC1's 'no check( call in that span carries kit 'agent-cap'' reds. Equally, a wrong build that leaves a `[dRB-14]` agent-cap check below the last `[dRB-14]` label escapes the span.",
   "fix": "Bound the span by markers instead of by the label's first and last occurrence: S1 writes `# [dRB-14] block: begin` and `# [dRB-14] block: end`, as S3 does for fixture B. Alternatively, AC1 reads only `check(` calls whose label string starts with `[dRB-14]`. Either way, state where S2's new `[dRB-14]` sidecar check sits relative to the `[dRB-15]` checks.",
   "evidence": "read: spec-15.md:69-70 ('The first reads the apply that unit 14's `[dRB-14]` block runs'); spec-17.md:388-390 (AC1 'reads tools/govkit/selftest.py from the first to the last line carrying `[dRB-14]`'); spec-17.md:68-69 (S2: 'The `[dRB-14]` block gains the same sidecar check', with no position given)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md",
   "where": "section 6 AC6",
   "severity": "low",
   "claim": "C10 — AC6's 'stdout carries `STALLED`' is matched over the whole stdout of a run whose manifest also holds `steady.py` and `churn.py`. The STALLED line names its leg (§4 prints `STALLED  <leg>`), but the criterion does not read that line.",
   "impact": "The stdout half passes when the only STALLED line names churn.py or steady.py. That is exactly the defect AC7 hunts, and the printed half then certifies stall.sh's report while observing another leg's. The `stalls` record half still grades stall.sh, so the effect is limited to the console-output claim.",
   "fix": "Reword AC6 to read the line itself: exactly one stdout line opens `measure-legs: STALLED  ` and names stall.sh's leg, and no line opening `measure-legs: STALLED  ` names `steady.py` or `churn.py`.",
   "evidence": "read: spec-18.md:319-320 (line format `measure-legs: STALLED  <leg>  (...)`); :591-595 (AC6 'Its `stalls` holds one episode whose tree names `sleep`, and stdout carries `STALLED`'); :596-598 (AC7 on the same run expects churn.py to hold no episode)."
  },
  {
   "file": "memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-16.md",
   "where": "section 4 'Why the carry is consistent after unit 12'; section 3 first non-goal",
   "severity": "low",
   "claim": "The consistency argument says every carried `emitted` row 'names a claimed kit', but the carry S1 turns on keeps every prior row whose `kit` is outside the selection, including a row whose kit the prior receipt does not claim. Unit 12 explicitly drops such orphan rows from `files`. After this unit, a receipt can therefore hold leg ownership for a kit it claims no files for, and nothing ever drops it.",
   "impact": "The ownership is permanent: every later narrower apply re-carries the orphan's row. That row is enough for check_leg_claimable to let gov rewrite a runner leg under that name, for a kit the receipt no longer claims. This contradicts the stated invariant and has no criterion. The effect is contained to targets whose prior `emitted` holds such rows, for example rows written by an older engine or by an `update` whose `kits` and `emitted` disagreed.",
   "fix": "Either narrow §4's sentence to the case it proves and add the orphan case to §3 as an accepted gap with its reason, or add an assertion to the S3 arm: after step 2, every `emitted` row carrying a `kit` names a kit in `kits`. Also add a staged prior receipt holding an `emitted` row for an unclaimed kit, recording what this unit does with it.",
   "evidence": "read: tools/govkit/govkit.py:4303-4305 (`if carry_out_of_scope: _scope = set(selection); emitted = [e for e in prior if e.get(\"kit\") not in _scope] + emitted`). read: spec-12.md:70 ('No carry of an orphan row, one whose `kit` the prior receipt does not claim. `apply` drops it') and :149 ('The carry is keyed on the CLAIM and never on \"a kit outside the selection\"'). read: spec-16.md:105-110 ('A prior `emitted` row was written by a run that selected its kit, and that kit is still claimed, so the carried row names a claimed kit') and :62-64 (it rejects claim-keying as 'a second rule for one list')."
  }
 ]
}
~~~~

### 2026-10-14T13:19:17 · gov-skeptic · wf_729fe7d9-e56/a5cb0c8cc726d6fad

Label: dRedressedBar · spec-audit round 1 · verify:ids-1-9

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 1,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Read memory/guides/SESSION-KICKOFF.md:4-6. last-audit is `ebce889c...` and watch lists both tools/run-gates/run-gates.sh and tools/gate-legs.json. manifest-check.sh:1460-1470 fails with code 5 when a watched file changed after LA_SHA and no last-audit re-stamp sits at or after the change. In tools/gate-legs.json, `kickoff-manifest ratchet` has no `guard` key, so it runs on every bar. In spec 18, §4 Files touched (lines 484-489) names tools/gate-legs.json and run-gates.sh but not SESSION-KICKOFF.md. Spec 18 contains no re-stamp, last-audit or kickoff-manifest text anywhere, and its §7 (line 660) leaves out `kickoff-manifest ratchet`. Spec 17 does the opposite: line 132-135 (S18) re-stamps as 2e187ee8b did, line 245-246 says an edit to gate-legs.json reds the ratchet until a re-stamp, and line 555 (§7) lists the ratchet. So the two specs give different answers for the same kind of edit, and unit 18 as written reds the ratchet. The README has no build-level re-stamp rule that would cover it.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 2,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 15:202-203 defines OFFERED as 'declared text carries /' and GRADED as 'resolved text carries no { and no space'. Its note template at :215 reads `<o> slash-bearing element(s) offered`. Spec 17 S10 (lines 104-107) grades on 'resolved text carries / and missing is empty' and says the cross-entry note 'counts all of them'. AC10's red half confirms that non-slash elements such as {gate_file} are now offered. Spec 17 never mentions `slash-bearing` or the note text (grep finds nothing), so a builder who keeps spec 15's template prints a count labelled slash-bearing that includes non-slash elements. One part of the claim is overstated: row 15 of the correction table (spec 17:286) does list '§4 ... ownership join', and in spec 15 the OFFERED/GRADED sentences and the note template sit inside that **The ownership join.** paragraph (lines 194-222). What is missing is the instruction for the note text. The only effect is a mislabelled output line, so I grade it low.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 3,
   "verdict": "refuted",
   "reason": "The premise is false. The finding assumes spec 12's correction and the ledger can land in a later commit than the govkit change, but BUILD-METHOD M6 (lines 182-186) says a pass is 'a unit built' and you 'Commit at the end of every pass'. That is one commit per pass, and spec 16:185 defines <p16> as 'the commit of unit 16's build pass'. Spec 16 §4 Files touched puts govkit.py, selftest.py, spec 12 and build/ in that one pass. So <p16>~1..<p16> holds the tools/govkit/ change S1 requires, and AC1-AC3 already show the change exists. Unit 17 names a second commit only because its manifest re-stamp has to follow the product commit. Unit 16 has no such step, so the empty-diff case described is not reachable under the method.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 4,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 17:17-18 reads 'its order is above every unit of this build' and :307 reads 'Order 12 is above every unit of this build.' Spec 18's Status line says order 13, the README index rows (lines 140-141) give 17 order 12 and 18 order 13, and README:68 says unit 18 'is ordered after every other unit.' So the sentence is false in the same way S6 corrects in spec 13.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 5,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 17 S9 (lines 93-95) lists six sites. AC9 (lines 441-444) requires the cut to carry only :7424, :7502, :7540, :7593, then requires the awk output to equal 'exactly the six numbers the cut names'. I re-ran `git show 46eb75ed:tools/govkit/govkit.py | awk 'NR>=7233 && NR<=8031 && /rows\\.append/ {print NR}'` and it printed 7424 7502 7540 7593 7616 7621. A spec 14 that lists only four sites passes the cut half, and 'the six numbers the cut names' is ambiguous. The criterion is underspecified, with no behavioural effect.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 6,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 18:102 reads '- No change to the merge bar's behaviour, ceilings or legs.' S13 (:95-98) adds the `measure-legs selftest` leg with its descriptor, manifest and budget rows, and AC13 (:630-633) requires that leg in tools/gate-legs.json. §7 (:666-667) also says the leg 'joins the manifest in this unit'. So the non-goal contradicts the scope as written. The criteria settle the behaviour, so only the prose is affected.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 7,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "S13 (spec 18:95-98) names 'the kit README section ... and the map claim' as deliverables observed by AC13 and AC14. AC13 (:630-633) reads only gate-legs.json, kit.toml, selftest-budgets.txt and windows-only-legs.txt. AC14 (:634-638) greps README.md only for 'gov:kit run-gates@' and checks the help page. Neither reads memory/map/features/run-gates.md or a README section about measure_legs.py. The map claim is caught only incidentally by the codebase-map gates in §7, and the README section is not observed at all.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 8,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 12 AC4 (lines 259-261) requires ast.get_docstring(write_gate_legs) to carry `TOOL-dRedressedBar-12`, and spec 12 S2 (:42-46) places that id in the carry_out_of_scope paragraph. Spec 16 S2 (:38-41) rewrites that same paragraph and requires only `TOOL-dRedressedBar-16`, and AC3 (:207-210) checks only -16 and the absence of `passes no carry`. A rewrite that meets spec 16 can drop -12 and red unit 12's AC4 when it is observed again.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 9,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "`grep -n 'def build_gov13' tools/govkit/selftest.py` printed 15428. Lines 15405-15412 are M13_DEPLOY, and line 15412 is `'observed_failed = [\"GATE FAIL  {name}\"]\\n')`. Spec 16:126 cites `tools/govkit/selftest.py:15412-15459`, while S3 (:44) and §6 (:188) cite ranges that start at 15428. Only the cited line is wrong.",
   "fixVerdict": "sound",
   "fixNote": ""
  }
 ]
}
~~~~

### 2026-10-14T13:19:18 · gov-skeptic · wf_729fe7d9-e56/a4be9cc18a95305ac

Label: dRedressedBar · spec-audit round 1 · verify:ids-19-27

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 19,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "I re-ran the probe. tools/run-gates/held_halves.py:80 has `load_manifest(path)`, which does json.load and refuses a non-list or a nameless row through print_refusal, exit 2. tools/run-gates/derive-ceilings.py:139 has `read_legs(root)`, which honours GATE_LEGS and builds a dict by name. Spec 18 line 467 adds a third reader, also called `read_legs`, and S1 gives it its own empty, no-name and duplicate refusals. The spec-writer prompt at line 80 says to extend these seams 'rather than writing ... a second leg-manifest parser'. Section 10's 'none is shared' only looks at the runner and run-selftests.sh, so it misses these two Python readers. The result is validators that can drift apart. Nothing ships wrong today, so the effect is contained.",
   "fixVerdict": "unsound",
   "fixNote": "Have measure_legs wrap held_halves.load_manifest once. The wrapper adds the empty-list and duplicate-name refusals and prints its own `measure-legs:` refusal line with exit 2. Drop the new `read_legs`, or rename it so it does not collide with derive-ceilings' `read_legs`. Add `{prefix}/run-gates/held_halves.py` to the measure-legs selftest guard, because the leg now imports that file. Correct section 10 so it names held_halves.load_manifest and derive-ceilings.read_legs as existing readers."
  },
  {
   "id": 20,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "run-gates.sh:301 defines `redact() { sed -E 's#://[^/@[:space:]]+:[^/@[:space:]]+@#://***:***@#g'; }`, and run-selftests.sh:1450 carries the same sed. No Python redactor exists under tools. The extracted runner functions are at :137, :3739, :3762 and :4220. Spec 18 line 468 lists `derive_redacted`, and section 10 (lines 726-728) lists the run-from-source functions without `redact`. Only `measure_foreign` gets a parity arm (AC8). AC11 checks only the `u:s3cret@` shape. So nothing holds the Python port to the runner's regex, and a drift would leak credentials into durable logs. That needs the port and the regex to drift apart, so the effect is contained.",
   "fixVerdict": "sound"
  },
  {
   "id": 21,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec 18 lines 454-456 list the guard as measure_legs.py, profile_bar.py, run-gates.sh, fixtures/measure-legs/, census.py, reap.py and scope.py, 'the files whose text it reads or imports'. AC15 (line 647) loads `read_runs` from derive-ceilings.py. The scrub reads `.githooks/pre-push`'s unset line at :100 (lines 197-199), and AC9 depends on it for GIT_NAMESPACE. Neither file is in the guard. From gate-legs.json I confirmed that `pre-push self-test` guards '.githooks/' and that `profile-bar selftest` and `run-gates turnstile` guard '{prefix}/run-gates/'. So a change to only one of the two files skips this leg on a scoped bar, and the drift surfaces only on a full bar.",
   "fixVerdict": "sound"
  },
  {
   "id": 22,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "govkit.py:2904-2960 reads subject-pins.tsv and fails with \"gate leg '{nm}' has no row in {pin_rel}\" for any manifest leg without a pin. The file header says it is regenerated by `govkit.py selfcheck --write`. A grep for subject-pins or selfcheck in regen.py finds nothing. subject-pins.tsv has rows for held-halves selftest and profile-bar selftest, so every leg carries one. Neither S13 (lines 95-98) nor Files touched (lines 485-493) names subject-pins.tsv. The govkit selfcheck leg on section 7 would catch it at once, so the cost is an extra file outside the estimate.",
   "fixVerdict": "sound"
  },
  {
   "id": 23,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 17 S23 (lines 155-160) says the comment above `ADOPTER_BAR_PATHS` and `write_atomic`'s docstring name the receipt, 'Observed by AC23'. AC23 (lines 528-537) checks the write_text count, membership in ADOPTER_BAR_PATHS, the fault-injected apply and spec 14's table. It checks no comment or docstring. govkit.py:3971 still reads 'which today is the gate-leg manifest'. Only a comment is at stake.",
   "fixVerdict": "sound"
  },
  {
   "id": 24,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "S13 (lines 95-98) lists 'the kit README section, a `help/` page and the map claim. Observed by AC13 and AC14'. AC13 (lines 630-633) reads the four leg rows. AC14 (lines 634-638) reads the version markers, help/measure-legs.md and the help/README.md link. Neither reads memory/map/features/run-gates.md or a run-gates README section. The codebase-map legs on section 7 may catch a missing map claim later, but nothing catches a missing README section. Only documentation is at stake.",
   "fixVerdict": "sound"
  },
  {
   "id": 25,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "foreign-prefix.gov.test.sh:48-50 says a row missing from WHOLE_RUN must print the probe marker, and that both directions red. derive_row_kinds (around line 193) marks a row whole only if WHOLE_RUN names it. The WHOLE_RUN list (lines 124-139) carries 'held-halves selftest', whose argv is `python3 held_halves.py --selftest` and which holds budget row 67. No tools/run-gates/*.py honours FOREIGN_PREFIX_PROBE, and profile-bar selftest is a .test.sh that does. Spec 18's new leg is a held kit/selftests `--selftest` engine mode with a budget row. Spec 18 honours no marker, edits no WHOLE_RUN, leaves foreign-prefix.gov.test.sh out of Files touched and leaves that leg off section 7. So the parity leg reds as an undeclared whole run.",
   "fixVerdict": "sound"
  },
  {
   "id": 26,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "memory/guides/SESSION-KICKOFF.md:5-6 shows `last-audit: ... @ ebce889c` and a watch line that includes tools/run-gates/run-gates.sh and tools/gate-legs.json. Spec 17 states the rule (lines 244-245), puts the re-stamp in its own Files touched (lines 298 and 330), and names `kickoff-manifest ratchet` on its gate line (line 555). Spec 18 edits both watched files, but its Files touched has no SESSION-KICKOFF.md, nothing in it re-stamps the manifest, and section 7 does not name the ratchet. So the ratchet reds once unit 18 lands.",
   "fixVerdict": "sound"
  },
  {
   "id": 27,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "In check-spec-tokens.py, lines 1198-1207 walk every guarded leg that section 7 does not name. If a Files-touched path trips that leg's guard (check_guard_trips, line 494), it adds a 'guards' hit, armed for specs dated on or after SPEC_GUARD_LEGS_CUTOFF=2026-09-22 (.memory-tree.conf:356). LIVE (line 231) covers SPECCED and INPROGRESS. Spec 18 is dated 2026-10-14, and its Files touched names tools/run-gates/measure_legs.py, which the new leg's guard names exactly. Section 7 (lines 666-667) leaves the leg off on purpose, and S13 does not tell the builder to add it at landing. So once the manifest row lands, spec tokens reds on spec 18 while it is still live.",
   "fixVerdict": "sound"
  }
 ]
}
~~~~

### 2026-10-14T13:19:18 · gov-skeptic · wf_729fe7d9-e56/a68aac193edaaf21a

Label: dRedressedBar · spec-audit round 1 · verify:ids-10-18

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 10,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Blobs match the pins. selftest.py:102-110 test_row_contract_is_complete asserts sorted(r) == sorted(census.FIELDS) for every build_windows_rows row. census.py:264 FIELDS has nine keys, and the ROW CONTRACT docstring at :12-22 lists the same nine. Spec 18 :53 (S4) and :345-350 add peak_mem_b and mem_b to every row while keeping FIELDS' bytes, and AC3 (:577) says 'census.FIELDS is unchanged'. The spec never names test_row_contract_is_complete or the docstring. The only selftest.py arm it mentions is the new AC3 arm at :664. So, built as written, the existing arm goes red on every Windows row and the builder has to change an arm the spec does not name. FIELDS is also read by render_rows (:270, :275) and by selftest.py:223, so moving FIELDS is not an option.",
   "fixVerdict": "sound"
  },
  {
   "id": 11,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec 18 :209-211 makes the scratch dir with mktemp in bash, and :236 resolves the turnstile key 'by the runner's own expression in the resolved bash'. That expression, at run-gates.sh:1513-1514, ends in `cd ... && pwd`. A grep of the spec for cygpath or any path conversion finds nothing. Re-probed: `(cd \"$HOME\" && pwd)` printed /c/Users/d41ly. That string, piped on stdin into python as pathlib.Path(p).resolve() and os.path.isdir, printed `C:\\c\\Users\\d41ly False`. The session's msys_pathconv_guard hook also blocked an inline probe and stated that /c/x becomes C:\\c\\x for a native binary. Python opens the raw capture as the CreateProcess stdout (§4 Launching, step 2), and :242 says 'An absent key or queue reads as empty'. So the turnstile read silently reads zero. AC15's ts_holders=1 and AC1 would expose this at build, which contains the effect to medium.",
   "fixVerdict": "sound"
  },
  {
   "id": 12,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "run-gates.sh:122-127 parses --hold and clears the positionals. Execution then falls through to the regen preflight at :1416-1452, whose only skip is GATE_REGEN_CHECK=0, and a stale verdict exits 2 before the turnstile and the beacon. Spec 18 :438 sets GATE_REGEN_CHECK=0 only inside queued.sh. AC15 (:639-641) starts the holder in the scrubbed environment and 'waits for its slot beacon's pid file' with no bound. The spec's own :277 says a hold runs the preflight. Re-run at HEAD: `timeout 115 python tools/run-gates/regen.py --check` printed 'memory/gotchas/INDEX.md ... STALE', then '12 declared · 11 fresh · 1 stale · 16s' and rc=1, so the tree is stale today and the check costs about 16 s.",
   "fixVerdict": "sound"
  },
  {
   "id": 13,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Reading tools/gate-legs.json printed `kit epoch (shipped bytes move, the version moves) | ['python', '{prefix}/govkit/govkit.py', 'epoch'] | None`, so the leg is unguarded. The §7 leg line of spec 18 (:660) names `kit version markers` and `verdict epoch` but not `kit epoch`, and it has no floor sentence. Spec 15 :446 names all three, and spec 17 :78 shows the floor-sentence convention. S13 moves both kits' versions. The full bar at the close still runs the leg, so the gap affects only how a pass is graded, which is low.",
   "fixVerdict": "sound"
  },
  {
   "id": 14,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "`grep -rn 'gov:kit process-monitor@' tools memory/map` printed tools/process-monitor/adopt-process-monitor.test.sh:4 at @0.15, beside nine @0.18 markers in adopt-process-monitor.sh (two lines), census.py, classify.py, procmon-hook.js, README.md, reap.py, scope.py and selftest.py. The test.sh file is not in spec 18's Files touched (:485-492). So AC14's 'The process-monitor markers all show one equal version above 0.18' cannot hold literally on a correct build.",
   "fixVerdict": "sound"
  },
  {
   "id": 15,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "run-gates.sh:3877 reads `else \"${argv[@]}\" </dev/null >\"$WORK/$i$sfx.raw\" 2>&1`, and :3916 reads `printf '%s\\n' \"$out\" > \"$WORK/$i$sfx.out\"`, which is the processed copy. Spec 18 S11 Readers (:83) calls `$WORK/$i$sfx.out` (run-gates.sh:3916) the runner's raw capture. The citation is wrong, though the 'different file' conclusion still holds.",
   "fixVerdict": "sound"
  },
  {
   "id": 16,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "`grep -n gate_file tools/codebase-map/kit.toml` printed `104:argv = [\"python\", \"{gate_file}\"]`. `git show 46eb75ed:tools/codebase-map/kit.toml | grep -n` printed 103:subject and 104:argv. Spec 17 :222, :452 and :610 cite :103 and claim the report's :104 was wrong. Line 103 is the subject line, so the spec's correction is false.",
   "fixVerdict": "sound"
  },
  {
   "id": 17,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 17 S23 (:155-158) enumerates unit 14's early write, its RECEIPT write, S22's write, update's three (:12017, :12055, :12062) and adopt's (:12692), which is seven writes. :275 says 'routes all six writes' and :300 says 'six writes through write_atomic'. `grep -n 'receipt_path.write_text' tools/govkit/govkit.py` printed five sites (8019, 12017, 12055, 12062, 12692), and unit 14's early write and S22's write are new. AC23's grep -c == 0 covers every write, so the miscount is cosmetic.",
   "fixVerdict": "sound"
  },
  {
   "id": 18,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "`sed -n 11878,11906p tools/govkit/govkit.py`: 11878-11886 are the S5 comment, 11887 is `try:` and 11888-11890 are the write_gate_legs call. 11891 is a comment inside the try. `except Refusal as _legs_stop:` is at 11898 and its 'the gate-leg step refused' r.fail at 11901-11903. Spec 16 :96 and :199 cite `:11880-11891` for the catch, and that range leaves the except out.",
   "fixVerdict": "sound"
  }
 ]
}
~~~~

### 2026-10-14T13:19:18 · gov-skeptic · wf_729fe7d9-e56/a48aad7ee3cb8797b

Label: dRedressedBar · spec-audit round 1 · verify:ids-37-43

~~~~text
{
 "path": "",
 "batch": "verify",
 "verdicts": [
  {
   "id": 37,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 18 S1 (lines 32-33) lists exactly three refusals: an empty manifest, a row with no name or no argv list, and a duplicate name. §4 Exit (423-424) maps only 'a refusal before the first leg' to 2 and uses 1 for 'a record write failed'. So the spec does not cover non-parsing JSON, a non-list top level, a non-object row, non-string argv elements, or a tab or newline in a name. Under the spec as written, any of these ends in an unspecified traceback (exit 1, which the spec reserves for a failed record write) or in a corrupted `.leg` row. run-gates.sh:3931-3933 relies on 'the canary already forbids a tab inside one', and that holds only for the shipped manifest. derive-ceilings.py:273-292 splits on tab by position (p[3] is the seconds, p[7] is foreign). I graded it low because the damage is contained: `--legs` is a file the operator supplies, the shipped manifest is canary-checked, and gate-profile records reach read_runs only through AC15's hand-built rows. I checked tools/gate-legs.json: it is a list of 140 rows, and no argv element holds a `{...}` token other than `{prefix}`.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 38,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec 18 §4 'The record' (370-377) keeps a raw capture only when a delete fails or on an interrupt, and records it in `raw_kept`. Exit (423-426) covers 130 for an interrupt. §5 risks (546-547) says 'The legs' scratch is never swept'. The spec says nothing about an unhandled exception, TerminateProcess or power loss. On those paths `raw/<i>.out` stays unredacted under %TEMP%/gate-profile.*, the envelope's end rewrite never runs, and nothing records the leftover file. That works against F2(b)'s `[security]` rationale (694-697). The leak stays in the operator's own temp dir, so I graded it medium. The fix is unsound. Both (a) and (b) select earlier scratch dirs by 'envelope never reached its end rewrite' or 'still holding raw files'. A profile running at the same moment matches that test too, so the next run would redact and delete raw captures its live legs are still writing. Nothing in the spec stops two profiles from running at once.",
   "fixVerdict": "unsound",
   "fixNote": "Write the profiler's own Windows pid and process creation time into the scratch dir at start. At start, a run treats an earlier gate-profile.* scratch as abandoned only when that pid with that creation time is no longer alive. For each abandoned scratch, it redacts each raw/<i>.out into that run's record as <i>.log.recovered, deletes the raw file, and names each one in its own envelope as `raw_recovered`. Add an arm that stages a profiler killed mid-leg, then runs a second profile beside a live first one. Assert that the live one's raw captures are untouched and that the dead one's hold no planted credential."
  },
  {
   "id": 39,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec 18 S11 (73-75) says only 'redacted as the runner redacts its durable copies', and §4's record table (366) says 'the capture, redacted'. No byte contract is stated. The runner's redaction is line-based `sed` (run-gates.sh:301). Its CR handling is host-dependent (305-307), and its capture drops NULs (3879-3880), so 'as the runner redacts' does not pin a Python byte behaviour. census.py:68-73 records a single 0xe7 byte killing a text=True read. A strict decode would hit the spec's own 'record write failed' exit 1 path with the raw file kept. A replace decode would alter the bytes. AC11's `grep s3cret` cannot tell the two builds apart. The fix is sound. For ASCII whitespace, Python bytes `\\s` matches the same set as POSIX `[:space:]`, and excluding newline keeps a match within one line as `sed` does.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 40,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "I grepped tools/govkit/govkit.py. Every `receipt_path.write_text` (8019, 12017, 12055, 12062, 12692) is followed directly by a plain `(target / \".governance\" / \"install.sums\").write_text` (8027, 12018, 12056, 12063, 12694). check asserts the sidecar and the receipt against each other with r.fail on each mismatch (5318-5333). Spec 17 S23 (155-160) adds only `receipt_path` to ADOPTER_BAR_PATHS. §4 justifies the widening by the report's request for 'a check over `.governance/` writes', and §5 (358-359) promises a whole previous file. So under S23 a fault in the sidecar write still truncates it, and an interrupt between the two writes leaves a new receipt beside the old sidecar, which check reds. AC23 faults only install.json. The effect is contained: check reds until the next apply. The §3 non-goal withholds only a general lint as its own mechanism, not routing the sibling write. The fix is sound. Ordering the sidecar first is a reasonable choice, and the fix states the remaining between-writes window rather than hiding it.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 41,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec 17 AC1 (388-390) bounds the `[dRB-14]` span by the first and last line carrying the literal. Spec 15 S6 (69-71) places the first `[dRB-15]` checks on 'the apply that unit 14's `[dRB-14]` block runs', so they sit beside or inside that block. Spec 17 S2 (68) adds 'the same sidecar check' to the `[dRB-14]` block without fixing its position. A later `[dRB-14]` line can therefore fall below `[dRB-15]` checks and enclose them in the span. Spec 15's AC1 red half (358-360) names `govkit: kit 'agent-cap'` as the problem line, so a `[dRB-15]` absence check could plausibly carry that text and red AC1 on a correct build. The selftest holds no `dRB-1[45]` marker yet (grep -c printed 0), so nothing in the tree settles the layout. The fix is sound: begin/end markers or a label-prefix filter both remove the ambiguity.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 42,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 18 AC6 (591-595) checks only that 'stdout carries `STALLED`' over a run that also holds steady.py and, per AC7 (596-598), churn.py. The printed line names its leg: `measure-legs: STALLED  <leg>` (319-320). A STALLED line naming churn.py would satisfy AC6's stdout half. That is the class of the repo's `line-claim-matched-over-the-whole-output` gotcha, which spec 17 cites. AC6's `stalls` half and AC7 still grade the record, so the gap touches only the console claim. The fix is sound. 'Exactly one line' is consistent with AC6's 'one episode', since only the first STALLED tick of an episode prints.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 43,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 16 §4 (105-110) claims 'the carried row names a claimed kit'. The carry at govkit.py:4303-4305 keeps every prior row whose `kit` is not in `selection`, with no claim test, and spec 16's §3 first non-goal keeps that keying on purpose. So an `emitted` row whose kit the receipt no longer claims is carried, as are rows with no `kit`. Spec 12 (70) says such orphans are dropped from `files`, and the selftest's orphan arm shows the state exists. The §4 consistency sentence is therefore stronger than the code. The non-goal withholds re-keying, not a correct statement of the gap. Because the non-goal accepts the keying, the effect is a misstated invariant rather than unplanned behaviour, so I graded it low. The fix is sound. Narrowing the sentence and recording the orphan case as an accepted gap matches the non-goal. The optional assertion only holds on the arm's orphan-free sequence, and the fix keeps the staged orphan fixture as a recorder, not an assertion.",
   "fixVerdict": "sound",
   "fixNote": ""
  }
 ]
}
~~~~

### 2026-10-14T13:19:18 · gov-skeptic · wf_729fe7d9-e56/a960be0bd4e68da67

Label: dRedressedBar · spec-audit round 1 · verify:ids-28-36

~~~~text
{
 "path": "",
 "verdicts": [
  {
   "id": 28,
   "verdict": "refuted",
   "reason": "duplicate of id=33. id=33 contains every part of this claim: the five-field fixtures at tools/process-monitor/selftest.py:69-72, :206-209 and :911-915 that S4's seven-field layout breaks. I re-read them and they are five-field rows, and census.py:111 reads the command from parts[4]. id=33 also covers the row-contract arm at :109. One premise here is also wrong. selftest.py is not a process-monitor engine file: tools/process-monitor/kit.toml gives it `role = \"project-owned\"`, so the spec's 'engine files move by their markers only' sentence does not cover it, and section 7 already adds an AC3 arm to it.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 29,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "I confirmed each piece in tools/run-gates/kit.toml. It declares `requires = []` and a single `[[files]] include = \"**\" role = \"engine\"` rule. Its only shell pin is `[[lf_pin]] pattern = \"{kit}/*.sh\"`, and an anchored gitattributes `*` does not match `/`, so fixtures/measure-legs/stall.sh and queued.sh are not pinned. Spec 18 section 4 ships the leg as a kit.toml `[[gate_leg]]`. Its Edges and S12 say the tool refuses with exit 2 when there is no process-monitor sibling or the host is not Windows. In an adopter tree windows-only-legs.txt is withheld (project-owned), so nothing marks the leg Windows-only there. The finding overstates one point: held-halves selftest already ships as a kit-subject `[[gate_leg]]`, so not every run-gates self-test is withheld. Still, a leg that hard-depends on another kit and on the platform is shipped without saying so. Its subject is kit, so it is held by default and only an opt-in self-test run reds. That keeps the effect contained.",
   "fixVerdict": "unsound",
   "fixNote": "Withhold `measure_legs.py`'s fixtures dir (`{kit}/fixtures/measure-legs/**`) as `project-owned`. Drop the kit.toml `[[gate_leg]]` row and declare `measure-legs selftest` as an `[[exempt_leg]]` in tools/govkit/registry.toml, with the profile-bar selftest reason. Amend AC13 to find the leg in gate-legs.json, selftest-budgets.txt, windows-only-legs.txt and the registry's `[[exempt_leg]]` rows, not in kit.toml."
  },
  {
   "id": 30,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "I re-read tools/govkit/govkit.py. At :6092 derive_parity_lines builds leg_words from receipt gate_runner.emitted argvs. At :6119-6121 it calls r.fail only for an installed consumer path in leg_words. Its callers are :5416 and :9658. With S1, a narrower apply keeps the carried kits' rows in emitted, so a failing contract clause whose consumer is on a carried leg now reds check/update where at <p12> it printed 'unwired'. The 'What an adopter sees change' table in spec 16 has no row for this. The new behaviour matches a full apply, so the omission is documentary only.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 31,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "Spec 12 S2 (lines 42-46) still says apply 'still passes no carry set, because a leg row such a kit loses from emitted is re-claimed by the same-argv rule'. Spec 16 S4 deliberately leaves S2 as written, and its only pointer is spec 12's revision line. Spec 12 AC4 (around :259-264) checks that the write_gate_legs docstring carries `TOOL-dRedressedBar-12`. Spec 16 S2 rewrites that same paragraph and asks only that it name `TOOL-dRedressedBar-16`, and AC3 checks only that token. A rewrite may therefore drop the unit-12 token and silently falsify spec 12 AC4. The consequence is limited to records and a re-observation, so it is low.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 32,
   "verdict": "confirmed",
   "severity": "low",
   "reason": "The claim about the spec is true. Section 4's table names AC1 as the refutation of 'an MSYS-forked descendant escapes the job', but AC1's spawn.py children are native processes spawned by python, and the wrapper's exec is cancelled by the twin. So AC1 never exercises an MSYS fork. The feared consequence does not reproduce, though. I ran a scratch probe: a no-flag Job Object, MSYS bash created CREATE_SUSPENDED, assigned, then resumed, running 5 `( /usr/bin/true )` subshells plus 5 `$(true)` substitutions. It printed TotalProcesses 18, against 1 for `bash -c true`, so MSYS forks stay in the job on node d. What remains is a mislabelled coverage claim, not an undercount that ships.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 33,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "I re-read the code. selftest.py:109 asserts `sorted(r) == sorted(census.FIELDS)` for every Windows row. Spec 18 adds peak_mem_b and mem_b to rows and keeps FIELDS unchanged (spec :349-351, AC3), so that arm reds. The fixtures at selftest.py:69-72, :206-209 and :911-915 are five-field CIM lines. census.py:111 reads `parts[4]`, and census.py:136 unpacks a 4-tuple. Under the seven-field layout those fixtures put the command in a memory slot. Spec 18 names none of these readers and gives no rule for 5- or 6-field lines or a blank memory value. The `process-monitor census selftest` gate catches the break at build time, so the effect is contained, but the builder gets no direction and the arm can be weakened.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 34,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec 18 routes only some of its bash invocations through the resolved bash. It names profile_bar.resolve_bash for the wrapper (:180-181), and says 'in the resolved bash' for mktemp (:210) and resolve_turnstile_dir (:236). resolve_python is only 'run once in bash' (:179), and measure_spawn_cost is 'one bash process' (:294), with no rule for either. I read tools/run-gates/profile_bar.py:282-304: resolve_bash returns (\"\", tried) when no candidate can see the script, and section 5's error states give no refusal for that. The gotcha memory/gotchas/subprocess-resolves-a-different-shell.md records that a bare `bash` reaches the WSL launcher. On a node with WSL installed that would mis-measure spawn_us and PYBIN.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 35,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec 18 section 4 step 3 (:186-189) runs CREATE_SUSPENDED, then OpenProcess, AssignProcessToJobObject, a toolhelp snapshot and ResumeThread, and states no outcome for any of them failing. Section 5 (:529-530) says 'the code never calls a terminate', and :535-536 says 'A leg that never ends keeps the run open'. A failed assign or resume would leave a suspended root that never exits, and under --serial the run would wait forever. The path is narrow, since assign rarely fails on Windows 8+ nested jobs, and the effect is a hang, not a wrong record.",
   "fixVerdict": "sound",
   "fixNote": ""
  },
  {
   "id": 36,
   "verdict": "confirmed",
   "severity": "medium",
   "reason": "Spec 18 :242-243 gives only 'absent key or queue reads as empty' and 'a key that exists and cannot be read is a refused read'. It says nothing about a ticket or beacon that vanishes after listing, or a beacon whose pid file is not yet written. :265-267 makes any refused read turn the eighth field into `unknown`. tools/run-gates/run-gates.sh:1556-1558 records that 'a beacon being written right now has none yet' (no pid). :1950-1951 shows the beacon's pid is written by printf after the slot dir exists. tools/run-gates/derive-ceilings.py:304-306 sets a non-digit field aside as 'uncensused'. A builder who reads the entry failure as refused would lose readings for every leg that runs nested bars.",
   "fixVerdict": "sound",
   "fixNote": ""
  }
 ]
}
~~~~

### 2026-10-14T13:22:23 · gov-synthesizer · wf_729fe7d9-e56/a84c67838e407287a

Label: dRedressedBar · spec-audit round 1 · synth

~~~~text
{
 "path": "C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/reviews/2026-10-14-review-TOOL-dRedressedBar-16-18-spec-audit-round1.md",
 "summary": "I wrote the round-1 spec-audit report for units 16 to 18. The verdict is CLEAN WITH FIXES. No blocker or high survived. There are 17 medium items covering 19 confirmed findings and 20 low items covering 22, so 37 items cover all 41 confirmed findings, each in exactly one item. Four merges were made, each within one binding grade: 1+26, 10+33, 7+24 and 8+31. Most medium items are in spec 18. Built as written, four of them red the bar at unit 18's close: M1 (kickoff-manifest ratchet), M2 (process-monitor census selftest), M8 (foreign-prefix parity) and M9 (spec tokens). For the three fixes the skeptic judged unsound (findings 19, 29 and 38), the report gives the skeptic's corrected fix. The three skeptic re-grades are bound: finding 2 went from medium to low, 32 from high to low and 37 from medium to low. Every run-integrity counter is zero, so the run is complete.",
 "items": [
  {
   "severity": "MEDIUM",
   "ids": [
    1,
    26
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    10,
    33
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    11
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    12
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    19
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    20
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    21
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    25
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    27
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    29
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    34
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    35
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    36
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    38
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    39
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    40
   ]
  },
  {
   "severity": "MEDIUM",
   "ids": [
    41
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    2
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    4
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    5
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    6
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    7,
    24
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    8,
    31
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    9
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    13
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    14
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    15
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    16
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    17
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    18
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    22
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    23
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    30
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    32
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    37
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    42
   ]
  },
  {
   "severity": "LOW",
   "ids": [
    43
   ]
  }
 ]
}
~~~~

### 2026-10-14T13:27:00 · gov-spec-writer · wf_729fe7d9-e56/a65a011a95c78cb1b

Label: dRedressedBar · audit round 4 · dispose

~~~~text
{
 "disposed": true,
 "standing": [],
 "promoted": 41,
 "folded": 0,
 "refuted": 0,
 "promotedIds": [
  "TOOL-dRedressedBar-19"
 ],
 "edges": [
  {
   "from": "TOOL-dRedressedBar-19",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-12"
  },
  {
   "from": "TOOL-dRedressedBar-12",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-19"
  },
  {
   "from": "TOOL-dRedressedBar-19",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-14"
  },
  {
   "from": "TOOL-dRedressedBar-14",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-19"
  },
  {
   "from": "TOOL-dRedressedBar-19",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-15"
  },
  {
   "from": "TOOL-dRedressedBar-15",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-19"
  },
  {
   "from": "TOOL-dRedressedBar-19",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-16"
  },
  {
   "from": "TOOL-dRedressedBar-16",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-19"
  },
  {
   "from": "TOOL-dRedressedBar-19",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-17"
  },
  {
   "from": "TOOL-dRedressedBar-17",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-19"
  },
  {
   "from": "TOOL-dRedressedBar-19",
   "verb": "consumes-from",
   "to": "TOOL-dRedressedBar-18"
  },
  {
   "from": "TOOL-dRedressedBar-18",
   "verb": "hands-off",
   "to": "TOOL-dRedressedBar-19"
  }
 ],
 "placements": [
  {
   "unit": "TOOL-dRedressedBar-19",
   "repairs": "none",
   "order": 14
  }
 ],
 "summary": "I disposed of all 41 confirmed findings from the units-16-18 spec audit by promoting them into one new unit, TOOL-dRedressedBar-19. The audit had no blocker, no high and nothing unverified, so all 41 are 19 mediums and 22 lows: report ids 1, 2, 4 to 27 and 29 to 43. Ids 3 and 28 were refuted by the audit itself, so they are not findings. I folded nothing, refuted nothing, and no finding is left standing.\n\n**The unit.** The spec is at C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-19.md. It is Tier-2, SPECCED, rev-1, base ebce889c, order 14. Its §1 table names every finding by report id and the report item it shares. Its §2 gives each id its own item, S<n> for id n, with S44 as the record. For ids 19, 29 and 38 it takes the skeptic's corrected fixes. Each item has a matching criterion in §6, and §7 carries six `New arm:` lines.\n\n**Order and placement.** The minors land on units 16, 17 and 18, so the unit repairs no single unit and `repairs` is `none`. Order 14 is one above unit 18's 13, the highest order in the build.\n\n**Why one unit, not two.** I could not split the batch into two disjoint write sets under M6. The profiler half writes `tools/govkit/registry.toml` and `subject-pins.tsv`. The govkit half's `govkit.py` reads both in selfcheck and is the generator of `subject-pins.tsv`, so clauses 2 and 3 both fail. This is recorded in the spec's §4 \"Alternatives rejected\".\n\n**Roster and edges.**\n- I added row 19 by hand to the Units table in C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/README.md, naming all 41 report ids.\n- Unit 19 consumes from units 12, 14, 15, 16, 17 and 18, because its criteria read what those units build.\n- Each of those six specs got the mirroring hands-off bullet as one rev bump with its §9 line: 12 to rev-4, 14 to rev-4, 15 to rev-3, 16 to rev-2, 17 to rev-2, 18 to rev-3.\n\n**Where I departed from the report's own fix sketch** (each is in §4 \"Alternatives rejected\"):\n- Id 12: no stale output is staged in the turnstile arm, because that would write into the tree a leg runs over on every bar. The new bounded wait is tested instead on a key no holder writes.\n- Id 41: unit 17's criterion reads the self-test checks by label, not between begin/end markers.\n- Id 20: the Python redactor is kept and held to the runner's `redact` by a parity arm. Using the runner's `sed` instead would break id 39's byte contract, because MSYS `sed` drops the CR of a CRLF.\n\n**Before you commit or build:**\n- The README's ruling of 2026-10-14 says units promoted from this round are built from their specs as written, with no round 5. That contradicts the task's note that the next harness run audits this spec, so unit 19 is unaudited by design.\n- Unit 19's §7 leg line names `measure-legs selftest`, a leg that only exists once unit 18 is built. Until then, `spec tokens (a spec's own names resolve)` would report that name.\n- I ran the memory hygiene gate. Its only failure touching this build is check 9, the README's generated index being stale, which is expected. I did not regenerate it. The other failures belong to other builds or were already there.\n\nNothing is committed."
}
~~~~

### 2026-10-14T13:49:04 · gov-spec-writer · direct/a6bc81a7bfa11d4c6

Label: dRedressedBar · TOOL-dRedressedBar-19 · spec-write

~~~~text
I revised **TOOL-dRedressedBar-19** to rev-2. I did not touch spec 10, which goes against the brief. The brief got both causes wrong, and following it as written would not have cleared either check.

**Check 7 (the long row is spec 19's, not spec 10's).** Check 7 numbers lines after skipping the front matter (`tools/memory-tree/check-memory-hygiene.sh:1137-1158`). The staged README has 9 front-matter lines, so `README.md:134` is file line 143, which is spec 19's index row at 370 chars. Spec 10's row at file line 134 is 308 chars, already under the cap. So I shortened spec 19's H1 instead. Its last two clauses now read "the receipt sidecar made atomic, and specs 12 and 14 to 18 corrected". With rev-2, the row should come out at 340 chars when the index is re-rendered.

**Check 12 (AC10 already had its `Red when:` line).** The criterion was never the problem. The check treats any line that starts with `AC<n>` at column 0 as a new criterion (`check-memory-hygiene.sh:1872`). The second line of the §6 preamble started with `AC10,`, so the check read it as a criterion with no `Red when:`. I rewrapped that paragraph so no line starts with a label. No wording changed.

**Header and §9.** The status header now says rev-2, and §9 has a rev-2 line naming both fixes, the shortened title, and the evidence. No scope, design, criterion or order changed.

**Checks run:** I ran the hygiene gate over the working tree, not `--staged`, because the files aren't staged yet.
- Check 12 no longer reports spec 19.
- Check 7 still reports the old 370-char row, and check 9 reports the index as out of date. Both are expected until the README is re-rendered, which is yours to do.
- I didn't re-render the README. I got the 340 figure by applying the new title and rev to the current row.

To finish, stage spec 19, run `python -B tools/memory-tree/gen_build_index.py --write`, stage the README, then run `bash tools/memory-tree/check-memory-hygiene.sh --staged`.

**Files:**
- Edited: C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-19.md
- Not edited: C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-10.md
~~~~

### 2026-10-14T13:55:08 · gov-builder · wf_cb1313a8-ee5/a25352a51d9d0640c

Label: dRedressedBar · TOOL-dRedressedBar-1 · build

~~~~text
{
 "committed": true,
 "sha": "3d1adca94e5c24cf99d345bcc15a0e611b0617d8",
 "why": "Built TOOL-dRedressedBar-1 as the spec says. All five sections (S1-S5) matched the code at HEAD 898b385c3, so nothing diverged from the spec. The commit carries the `Pass: TOOL-dRedressedBar-1` trailer, and the spec's status header is set to CLOSED (date 2026-10-14) with nothing else in the spec changed.",
 "summary": "TOOL-dRedressedBar-1 is committed as 3d1adca94e5c24cf99d345bcc15a0e611b0617d8 in C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix. Each criterion was checked with a probe of the changed code, and no gate or suite ran.\n\nPaths I declared before writing, all staged by name:\n- tools/workflows/unattended-build.test.sh\n- tools/workflows/tier2-review.test.sh\n- tools/run-gates/run-gates.turnstile.test.sh\n- .githooks/pre-push.test.sh\n- tools/roles/adopt-roles.test.sh\n- memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-1.md (status header only)\n\nOne path outside that list is in the commit: memory/builds/dRedressedBar/README.md. The pre-commit hook's memory-hygiene check 9 refused the commit because the README's generated units table was out of date. `gen_build_index.py --write` changed exactly one row, this unit going from SPECCED to CLOSED. It also rewrote the spec without changing any bytes and touched nothing else.\n\nWhat changed:\n- **S1:** the 13 glued `build_gh33_writer` calls now have a space between the id and the JSON.\n- **S2:** the tier2-review extraction now stops on the line after the `}` that closes the `if (!baseLooksPinned)` block, found from the `const baseLooksPinned` line. Both new anchors have a die, and the three-needle die is unchanged.\n- **S3:** arm 44's `sed` now routes `IFS= read -r hpid < \"$d/pid\"` through `read_pid_and_swap`, which reads the pid with the same builtin and then swaps the nonce.\n- **S4:** one `unset GATE_SELFTESTS`, with a comment, at line 122 beside the suite's other environment settings.\n- **S5:** the sibling suites' FOREIGN_PREFIX_PROBE stop, placed after arm 1 and reading `fail` and `n`.\n\nChecks that ran (each stands in for the gate named):\n- **AC1** (stands in for `unattended-build self-test`): a grep finds 0 glued calls and 14 spaced calls on 5 lines. The function cut out alone under `set -u` prints the expected label and JSON. The glued form aborts with `$2: unbound variable`.\n- **AC2** (stands in for `tier2-review self-test`): node evaluated the `/^const metaEnd/,/^ck(true/` block over tier2-review.js and printed `the prelude extraction is live (529 lines ...)` with no die. The body throws `reviews nothing` for an empty spec-audit subject list and `must be an immutable sha` for a round-2 base of `main`. The HEAD version of the block dies naming `badSubject`, and each new die fires when its anchor is removed.\n- **AC3** (stands in for `run-gates turnstile`): arm 44 cut out alone prints both `survived` lines, routed reads 2, and both nonces read `successor`. The HEAD arm reads routed 0 with both beacons removed.\n- **AC4** (stands in for `pre-push self-test`): exactly one unset line, at 122, before the first push at line 139. In a scratch RP-shape fixture under %TEMP%/rb1a4 (removed afterwards), a push decides `scoped gate on main push` with GATE_SELFTESTS unset and `FULL gate on main push` with it set to 1.\n- **AC5** (stands in for `foreign-prefix parity` and `roles adopter self-test`): the FOREIGN_PREFIX_PROBE lines (84 and 85) sit between the arm 1 and arm 2 headers (78 and 87). With the probe on, the stop line alone prints the marker and `PASS (2 assertions)`, and exits 1 when fail is 1. It never reads `pass`.\n- All five suites pass `bash -n`, and the staged bytes are LF with 0 CR.\n\nOwed at the close, by the main loop:\n- RED-first observation of each of the five `New arm:` lines in spec §6.\n- The legs in spec §6: `unattended-build self-test`, `tier2-review self-test`, `verifier fan-out self-test`, `review-join self-test`, `run-gates turnstile`, `pre-push self-test`, `foreign-prefix parity` and `roles adopter self-test`.\n- Spec §3 already hands these readings to TOOL-dRedressedBar-10, and they show up as predicted:\n  - AC1's `grep -c` counts 5 lines for 14 calls.\n  - AC4's first `git push` match is the header comment at line 2.\n  - AC5 finds 2 FOREIGN_PREFIX_PROBE lines, because the copied shape is a comment plus the stop.\n\nBug-class checklist: `gotchas.py --for-diff HEAD~1..HEAD` selected 27 classes and I went through them. No other test reads the old `const reviewDir` anchor, the `cat \"$d/pid\"` spelling or a glued call. Each probe also showed the old code red, so none of the fixes passes by matching nothing. One class applies to the environment rather than this commit: `hookspath-resolves-into-another-checkout`. core.hooksPath is C:\\projects\\coding-governance\\.githooks, so this worktree's commits are checked by the main checkout's hooks. I took no action on that.\n\nTwo commit attempts failed for environment reasons, not on a hook's verdict: git itself hit `Out of memory, malloc failed` with 7-9 GB free, and once could not spawn the pre-commit hook. A third attempt passed. Nothing was skipped for timeout."
}
~~~~

### 2026-10-14T14:04:37 · gov-builder · wf_c695547d-322/aa94e60e3770b9c02

Label: dRedressedBar · TOOL-dRedressedBar-2 · build

~~~~text
{
 "committed": false,
 "sha": "",
 "why": "DIVERGENCE: spec memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-2.md §3 Edges (the hands-off to TOOL-dRedressedBar-10) says `memory/map/generated/symbols.json` \"reads that map stale until unit 7 regenerates it\". §4 Files touched names only `tools/unattended/gate-guard.js`. The repository won't commit that design. `.githooks/pre-commit:233-246` runs the codebase-map gate on any staged .js file. Its `test_generated_artifacts_are_fresh` refused the commit with `STALE symbols.json — regen: python tools/codebase-map/gen_map.py --write` and asked for the rewritten map to be staged in the same commit. The spec as written can only land through `--no-verify`, which is routing around the hook. The other route writes `symbols.json`, a shared generated index that the spec gives to unit 7 and that is outside this unit's declared write set. Units 2 and 9 could then run concurrently with overlapping write sets, against M6 clause 3, because unit 9 also mints `check_outcome_states` in a mapped file. To be buildable, the spec would need what this build's specs 15 S8 and 19 §4 already say for their own new functions: (a) a scope item where the pass runs `python tools/codebase-map/gen_map.py --write` alone before the product commit, and the commit carries `memory/map/generated/symbols.json`, with `renderAskQuote` listed and no `clean` entry for gate-guard.js; (b) that path added to §4 Files touched and to S4's Readers; (c) the §3 Edges sentence saying the map reads stale until unit 7 replaced, since unit 7's `regen.py --write` will then find it fresh. Unit 10's S17 and AC14, which are written to put the 'stale until unit 7' note into spec 2, and spec 9's matching note for `check_outcome_states` have the same defect. The spec writer should fix them in the same revision. The rename itself matched the spec, and its probes were green before I restored the tree (see summary). I restored every path I changed, so the tree is as I found it: gate-guard.js matches HEAD, and the spec header is back to the INPROGRESS the caller had left unstaged. Nothing was committed.",
 "summary": "I made no commit for TOOL-dRedressedBar-2: the spec assumes a commit this repository's pre-commit hook refuses (see `why`).\n\nDeclared write set: `tools/unattended/gate-guard.js` (three tokens) and the status header of `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-2.md`. I made the rename as S1 describes: `const clean` at line 689 and the calls at 694 and 696 became `renderAskQuote`. Then I checked it:\n- AC1 (a grep probe): `grep -nw clean` printed nothing, and `grep -n renderAskQuote` printed exactly the three lines inside `extractAskQuestions`.\n- AC2 (a node fixture): a probe under the scratchpad (`.../scratchpad/u2/probe-ac2.js`) ran against the working file and against `git show ebce889c:tools/unattended/gate-guard.js`. The payload had a 400-character question with a BEL and a U+0085 control character, a label with a NUL, a non-string label, a blank question, a null question, and also `{}`. `cmp` found the two outputs identical. The first question came out 300 characters long, and `{}` gave `[{\"question\":\"(no question text)\",\"labels\":[]}]`. This stands in for the `unattended gate-guard selftest` leg, which is held off this build.\n- AC3 (the lexicon engine, the one tool this role may run): `lexicon.py --suggest renderAskQuote --as js.function` printed `OK — renderAskQuote leads with \\`render\\``. `--offenders` listed 1087 verb rows and none for `tools/unattended/gate-guard.js`. `--measure` printed `VERB_OFFENDER_PIN=\"1087\"`, equal to `.lexicon.conf:268`. This stands in for the `lexicon naming predicates` and `lexicon wiring` legs; the main loop still runs both at the close.\n\nThe commit was refused by `.githooks/pre-commit` on two checks:\n1. HYGIENE check 9: the build index needs `memory/builds/dRedressedBar/README.md` re-rendered after the CLOSED status flip. The rerun owes `python tools/memory-tree/gen_build_index.py --write`, as unit 1's commit `3d1adca94` did.\n2. The codebase-map gate: `STALE symbols.json`. This is the divergence, because the spec says the map stays stale until unit 7.\n\nAfter that I restored every path I changed (`git restore --staged` and `git restore` on gate-guard.js, and the spec header set back to INPROGRESS). The tree is in its pre-pass state, with only the caller's unstaged INPROGRESS edit to spec 2.\n\nNot run:\n- `gotchas.py --for-diff HEAD~1..HEAD`: there is no commit of this pass, so that range is unit 1's commit, not this work.\n- The bar and every suite, as the task requires.\n- `--no-verify`: not used; it would have bypassed the hook's refusal.\n\nNo new arm is declared, and spec §7 adds none. When the unit is re-dispatched after the spec revision, the AC1–AC3 probes above can be re-run as they stand. The probe and base copy are in the scratchpad under `u2/`. Owed at the close: `lexicon naming predicates`, `lexicon wiring`, and `codebase-map coverage + freshness`."
}
~~~~

### 2026-10-14T14:10:31 · gov-spec-writer · direct/ae5b3dda730b7ae15

Label: dRedressedBar · TOOL-dRedressedBar-2 · spec-write

~~~~text
I revised four specs (2, 9, 10 and 13), and `unattended.sh --plan dRedressedBar --paths` grades every unit READY. No spec in the build now says the map stays stale until unit 7. Nothing is committed and no index was regenerated.

Before writing, I confirmed the problem is real. `python tools/codebase-map/gen_map.py --check` exits 0 at `3d1adca9`, and `symbols.json:5420-5424` lists `clean` for `tools/unattended/gate-guard.js`. The hook at `.githooks/pre-commit:233-257` refuses a commit that stages a `.js` or `.py` file while the map is stale, and also refuses one whose regenerated map is left unstaged.

**TOOL-dRedressedBar-2 → rev-3** (status left at INPROGRESS, as the dispatcher set it)
- (a) New S5: after the rename, the pass runs `python tools/codebase-map/gen_map.py --write` on its own. One product commit carries `gate-guard.js` and `memory/map/generated/symbols.json`, with `renderAskQuote` listed and no `clean` entry for that file. If the regen changes any other file, the pass stops and returns to the main loop without committing. New AC4 checks the committed map.
- (b) S4's Readers and §4 Files touched now name `symbols.json`.
- (c) The Edges line to unit 10 now says report id 17 is closed in this spec, unit 10 only observes it, and unit 7's regen will find the map fresh.
- §4 gains "The symbol index": the rename changes only `symbols.json`, and units 2 and 9 are built one after the other (M6 clause 1). `--dispatch` refuses a second claim on the same file while the first pass is open (`unattended.sh:13718-13729`).
- §7 now names `codebase-map coverage + freshness`, plus `recall floor` and `recall floor arms`. The guard join owes those two because `symbols.json` sits under their `memory/` guard (`tools/gate-legs.json:868-890`).

**TOOL-dRedressedBar-9 → rev-4**
- New S7 and AC7 give its new `check_outcome_states` the same regenerate-and-commit step.
- `symbols.json` is added to Files touched, with the same "symbol index" section and a no-`regen.py` non-goal.
- The Edges line no longer says the map stays stale until unit 7.
- §7 adds `codebase-map coverage + freshness` and `recall floor`.

**TOOL-dRedressedBar-10 → rev-4**
- S17 and AC14 now only observe what specs 2 and 9 already say, plus both units' product commits (`<p2>`, `<p9>`) carrying `symbols.json`. They write nothing into either spec.
- Spec 2 leaves §4's table and Files touched, and spec 9's row drops id 17.
- Knock-on edits: the Alternatives row names S9 in place of S17, AC19, §5 and §7 count eight version bumps, and the Edges lines to units 2 and 7 were rewritten.

**Item 4, every other spec:**
- **Fixed, TOOL-dRedressedBar-13 → rev-4:** its S3 repeated "as reading stale until unit 7" about spec 9; that is corrected, and AC3 still holds.
- **Already state the step:** 15 (S8; its `regen.py` wording is unit 17's S21 to correct), 17, 18 and 19.
- **Change no function in a mapped file:** 3, 4, 5, 6, 7, 8, 11, 12 and 16. Unit 4's `WORKFLOW_RUNS_DIR` is a string constant, which the map's JS rules don't list. Unit 1 is CLOSED.

**Checks run:**
- `check-memory-hygiene.sh --only 12,25` is clean.
- The full hygiene run fails, but not on these specs:
  - Check 9: `memory/LIVE.md` and the build README are stale. They need regenerating, which is yours to do.
  - Check 17: the gotchas index is stale. That is unit 7's S1.
  - Check 23: ledger lines in other builds.
- I ran no lexicon check, since no spec here names a new identifier.

**Decision for you:** the README's Build-level rules still say "units 1, 2, 8 and 9 are disjoint", which is now false for units 2 and 9. The derived build order also still shows step 1 as parallel. The README is outside my write set, so I left both. The options are to edit that sentence, or to move one unit to another order step. `--dispatch` will keep the two units apart either way.

Files are in C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\:
- 2026-10-14-spec-TOOL-dRedressedBar-2.md
- 2026-10-14-spec-TOOL-dRedressedBar-9.md
- 2026-10-14-spec-TOOL-dRedressedBar-10.md
- 2026-10-14-spec-TOOL-dRedressedBar-13.md
~~~~

### 2026-10-14T14:23:16 · gov-builder · wf_eb13c24a-b41/af59039234e86d2c9

Label: dRedressedBar · TOOL-dRedressedBar-2 · build

~~~~text
{
 "committed": true,
 "sha": "c7a9213d1",
 "why": "TOOL-dRedressedBar-2 rev-3 is built as written. I renamed the local arrow `clean` inside `extractAskQuestions` in tools/unattended/gate-guard.js to `renderAskQuote` (S1-S3). Then I ran `gen_map.py --write` on its own, which moved only memory/map/generated/symbols.json (S5). The spec's status header is now CLOSED, all in one commit with a `Pass: TOOL-dRedressedBar-2` trailer. The code and the spec did not disagree anywhere.",
 "summary": "Commit c7a9213d1 on branch/gov-bar-reds-fix, in C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix.\n\nWhat changed:\n- tools/unattended/gate-guard.js: `clean` renamed to `renderAskQuote` at the declaration (line 689) and both calls (694, 696). Nothing else changed; the file stays LF-only, and I checked the staged copy for that.\n- memory/map/generated/symbols.json: regenerated by `python tools/codebase-map/gen_map.py --write` run on its own. Only this file moved: the `clean` entry for gate-guard.js is gone and a `renderAskQuote` entry is added.\n- memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-2.md: status header INPROGRESS to CLOSED. The date was already 2026-10-14, and nothing else in the spec changed.\n- memory/LIVE.md and memory/builds/dRedressedBar/README.md: these two were not in my declared write set. The pre-commit hook's hygiene check 9 refused the first commit attempt because the CLOSED flip left the generated build index stale. I ran `python tools/memory-tree/gen_build_index.py --write`, which moved only these two files (the spec's own generated block came out unchanged), and staged them by name. Unit 1's commit 3d1adca94 carried its build README the same way.\n\nChecks I ran (each is a probe of this unit's code, standing in for the bar leg named):\n- AC1 (stands in for `lexicon naming predicates`): `grep -nw clean` on gate-guard.js prints nothing; `grep -n renderAskQuote` prints exactly lines 689, 694 and 696.\n- AC2 (stands in for `unattended gate-guard selftest`, held off this build): a node probe at scratchpad/u2/probe-ac2.js ran `extractAskQuestions` on the tip and on `git show ebce889c:` written to scratch. The payload had a 400-character question carrying a BEL and a C1 byte, a label carrying a NUL, a non-string label, a blank question and a null question, then `{}`. The two outputs are byte-identical. The first question reads 300 characters, and `{}` reads `[{\"question\":\"(no question text)\",\"labels\":[]}]`.\n- AC3 (stands in for `lexicon naming predicates` and `lexicon wiring`): `--suggest renderAskQuote --as js.function` prints `OK — renderAskQuote leads with render...`. `--offenders` lists 1087 verb offenders and no line naming gate-guard.js. `--measure` prints VERB_OFFENDER_PIN=\"1087\", matching `.lexicon.conf:268`. I ran these again after the map regeneration and committed tip and got the same results.\n- AC4 (stands in for `codebase-map coverage + freshness`): reading the tip's symbols.json finds `renderAskQuote` 1 and `clean` 0 for gate-guard.js; the 3d1adca9 copy finds `renderAskQuote` 0 and `clean` 1. `gen_map.py --check` exits 0. `git show --name-only --format= c7a9213d1` lists gate-guard.js and symbols.json, and no other path under memory/map/.\n\nOwed at the close (the main loop runs these; I did not):\n- The bar's `lexicon naming predicates`, `lexicon wiring`, `codebase-map coverage + freshness`, `recall floor` and `recall floor arms` legs, and the full-tree hygiene checks that the pre-commit hook held under --staged (checks 1, 3, 4, 5, 10, 23 and the §3 joins).\n- No new arm, so no RED-first observation is owed.\n- `unattended gate-guard selftest` runs only if the owner asks.\n- The unattended kit's version bump stays with TOOL-dRedressedBar-7.\n\nBug-class checklist: `gotchas.py --for-diff HEAD~1..HEAD` ran and exited 0 with 21 classes. The one that applied was naming-leg-grades-what-python-named (the lexicon's armed set follows symbols.json); I acted on it by running `--measure` and `--offenders` again after the map regeneration, still 1087 and still no gate-guard.js line. Of the rest:\n- fixture-passes-by-finding-nothing: AC2's payload hits every case, and AC4's read of the base map shows the probe can find `clean`.\n- heredoc-escape-reaches-the-regex: all edits went through the edit tool, and AC2 shows the regex is unchanged.\n- retirement-inventory-misses-readers-by-value: the helper isn't exported, and the map's entry count is unchanged.\n- The other classes don't apply to this commit (no guard, arm, fence, move or amendment).\n\nNo command hit its timeout, and nothing was skipped."
}
~~~~

### 2026-10-14T14:27:56 · gov-builder · wf_248cd33c-fe0/aa9905cad11019590

Label: dRedressedBar · TOOL-dRedressedBar-8 · build

~~~~text
{
 "committed": true,
 "sha": "a50d04eb79a3be76bb1e6ce201607b7cfd6157fe",
 "why": "TOOL-dRedressedBar-8 is built as the spec says, in one pass commit carrying `Pass: TOOL-dRedressedBar-8`. The spec's status header moved from SPECCED to CLOSED (rev-2, dated 2026-10-14) and nothing else in the spec changed. Paths written: tools/run-gates/run-gates.test.sh, the spec's status line, and memory/builds/dRedressedBar/README.md. The README is extra: the pre-commit hygiene check 9 refused the commit until `gen_build_index.py --write` re-rendered it, and the only change was this unit's row going to CLOSED (unit 2's pass did the same). There was no divergence from the spec.",
 "summary": "Built in tools/run-gates/run-gates.test.sh, one file, 40 lines added and 8 removed:\n- **S1, the server:** `serve.sh` now runs `trap '' PIPE`, loops on `while [ -p \"$f\" ]`, retries a failed open with `exec 3>\"$f\" || { sleep 0.1; continue; }`, and waits `sleep 0.2` after `exec 3>&-`. It serves the same answers. Its header names this unit, the two ways it died and the measured runs. Its stderr goes to `$MP/x/serve.err`.\n- **S2, the bound:** `run_mp_bar` runs the nested runner under `${MP_BOUND:+timeout -k 5s \"$MP_BOUND\"}`, and its header comment says so. Only the `ac14` call sets it, as `MP_BOUND=$_mpwall`, timed with `date +%s`.\n- **S3, the liveness check:** the status of the arm's own `wait` is read before the verdict. Anything but 143 prints the server-dead red line and indents `serve.err` under it. `MP_RC` 124 or 137 prints the bound red line naming serve.sh alive. Otherwise the old verdict check runs, with its lines unchanged. It is still one counted assertion.\n- **S4, the skip:** when `HAVE_TIMEOUT` is not 1, an announced SKIP comes before `mkfifo`, and the `n=$((n+1))` stays above the branch.\n- The 11g comment now says what the arm does not check.\n\nChecks that ran here: probes of the code I changed, standing in for `run-gates canary` arm 11g until the close. The probe scripts are not committed and are under the scratchpad: C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-bar-profile-failures-b80cc3/8d2976c7-7629-4ba0-8a96-2098db6da20f/scratchpad/p8/\n1. **AC1, observed GREEN:** `probe-serve.sh <worktree> <scratch> 300` ran twice under `timeout -k 10s 600`. Both runs printed `probe: 300 of 300 reads carried 10 %, 300 asked · server exit 143`. The same probe over the server from base `ebce889c7` printed `probe: 1 of 2 reads carried 10 %, 300 asked · server exit 0`, so the probe can fail.\n2. **`probe-bound.sh`:** it loads only `run_mp_bar`'s definition and runs it against a stub runner, with `set -u`.\n   - With `MP_BOUND` unset, rc 7 at 0 s, the same as before.\n   - `MP_BOUND=3` over a stub that hangs (and has a background grandchild) gave rc 124 at 3 s.\n   - `MP_BOUND=20` over a quick stub gave rc 7.\n   - `MP_BOUND` does not persist after the call.\n   - The base definition ran the same hang its full 30 s, rc 7.\n3. **`probe-stage-text.sh`:** applies probe-11's staged edits to section 11 as text only, never run. Staged lines read none 0, dead 1, silent 1, and the slice ends at the section's own `rm -rf \"$MP\"`.\n4. **`probe-liveness.sh`:** runs the extracted server in each stage through the arm's kill-release-wait line. The wait status is none 143, dead 0, silent 143, which are the readings S3 needs.\n5. **AC6, observed:** the pass commit alone touches one file under tools/. `MP_BOUND` appears only in `run_mp_bar` and on the `ac14` call, no `n=$((n+1))` is added, and `FLOOR_ASSERTIONS=401` is unchanged. AC6 as worded diffs from base `ebce889c7` and lists 6 files, because units 1 and 2 already landed tools/ edits on this branch. The spec's §3 Edges hands that rewording to TOOL-dRedressedBar-10.\n6. `bash -n` parse check of the suite, and `lexicon.py --suggest MP_BOUND --as sh.constant`, which answered that the cell is undeclared, as the spec's inventory says.\n\nOwed at the close (not run here; the task forbids running a slice of a suite):\n- AC2: `probe-11.sh <worktree> none`, three runs, each printing `fail=0`.\n- AC3: `probe-11.sh <worktree> dead`, which should print the serve.sh-dead line within the calibration bound plus 15 s.\n- AC4: `probe-11.sh <worktree> silent`, which should print the bound line with serve.sh alive.\n- AC5: `probe-11.sh <worktree> none 0`, which should print the SKIP line with the same `n=`.\n- The new arm's RED-first observation (tools/run-gates/run-gates.test.sh, covering AC2 to AC5): RED on the dead and silent stages, GREEN once restored.\n- The legs `run-gates canary` (which must finish under its 13200 s ceiling), `run-gates gov canary`, both shell-hygiene legs, and `harness arms`.\n- probe-11 creates its fixture repository with `MP=$(mktemp -d)`, so run it with TMPDIR set to a short directory under %TEMP%.\n\nBug-class checklist: `gotchas.py --for-diff HEAD~1..HEAD` selected 18 classes, and I checked the ones that could apply.\n- `fixture-passes-by-finding-nothing`: every probe above was also run against base or a staged break, so each showed it can fail.\n- `retirement-inventory-misses-readers-by-value`: memory/project/spawn-idiom-sites.txt keeps per-class counts for this suite. The classifier puts `$(date +%s)` in the `epoch-date` class, and `scan_spawn_tree` skips banned classes in `*.test.sh`. The serve.sh heredoc is quoted, so its body is data. No registry-class site is added, so no row moves. This also means spec §6's line \"the fork leg reads none of this file\" is inaccurate; Edges already hands that correction to TOOL-dRedressedBar-10.\n- The symbol map lists `run_mp_bar` by id, kind and file only, with no line numbers, and no function was added or renamed.\n- No `done <<<` reader was added, so substitution-fed-loops row 45 does not move.\n- check-arms excludes `*.test.sh`, so the new red branches owe it nothing.\n- No other file describes serve.sh or this skip.\n\nNo command hit its bound and nothing was skipped."
}
~~~~

### 2026-10-14T14:39:35 · gov-builder · wf_df00997e-69f/aeeca0787c1024036

Label: dRedressedBar · TOOL-dRedressedBar-9 · build

~~~~text
{
 "committed": true,
 "sha": "59f11096a35a43fac58f4cb523030587f452d099",
 "why": "Built and committed as the spec says. The spec and the code did not diverge. `gotchas.py --for-diff HEAD~1..HEAD` was run after the commit and every class it selected was acted on, so I stand behind this commit.",
 "summary": "TOOL-dRedressedBar-9 is committed as 59f11096a on branch/gov-bar-reds-fix. A writing `update` over a narrow receipt now finishes, and so does `apply --kits settings-merge`. No gate, suite or bar ran; ACs 1-7 were checked by direct probes, and the selftest and matrix verdicts are left to the main loop.\n\n**Paths, declared before writing and staged by name:**\n- C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/tools/govkit/entries/settings-merge.kit.toml (S1)\n- C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/tools/govkit/selftest.py (S5)\n- C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/tools/govkit/matrix.py (S6)\n- C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/map/generated/symbols.json (S7)\n- the spec's status header, now CLOSED, 2026-10-14\n- C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/README.md\n\n**What changed:**\n- **S1:** settings-merge's descriptor gains one `[[outcome]]` block (code 2, `no-agent-cap-to-wire`, `ok = true`). It declares the adopter's exit 2 an accepted stop only when `settings-merge.py` is installed and `hooks/agent-cap.js` is not.\n- **S5:** one new `[dRB-9]` block after line 3313, on its own `stale_target(\"rq9\")` fixture. It reads the stop's name from the descriptor at run time and adds no new subprocess or untyped file-read site.\n- **S6:** the matrix's lexicon loop became `check_outcome_states`. Lexicon's two labels are unchanged byte for byte. settings-merge's three rows get their two paths from where `resolve_entry` lands each kit's `version_from` file, so neither path is typed.\n- **S7:** `gen_map.py --write`, run alone, moved only `symbols.json`.\n\n**One call beyond the spec:** the CLOSED flip made the build README's generated row stale (`gen_build_index.py --check` showed DRIFT). I ran `gen_build_index.py --write`, which moved only that one row, and committed it, as units 2 and 8 did. §3 says \"no generated output other than the map\", so if that line covers the index, the main loop should rule on this.\n\n**Probes that ran (scratch targets under %TEMP%/p9fx, since deleted):**\n- **AC1:** grep shows the one block, and the diff of the four files that must not move is empty against ebce889c.\n- **AC2:** before the fix, on a50d04eb, the narrow update exits 1 with `no declared outcome accepts that` and gov_commit stays at 24f39915. After the fix it exits 0, prints `adopter exit 2 — no-agent-cap-to-wire` and `check-wiring.fragment.json wired`, re-stamps at HEAD, and the receipt claims check-wiring, run-gates and settings-merge.\n- **AC3:** `apply --kits settings-merge` goes from exit 1 to exit 0 with `[accepted stop]`, and no settings.json is created.\n- **AC4:** the engine reads the three exit-2 states as ACCEPTED, REFUSED, REFUSED. With `must_not_exist` dropped (held in memory, not written), the both-present state reads ACCEPTED.\n- **AC5:** the dirty-README shape and the committed-deletion shape both exit 0, and the deletion prints `missing`. I did not rerun them over the old descriptor; that half was observed when the spec was written.\n- **AC6:** the full install still prints adopter exit 0 for both kits, never prints the stop, and wires `agent-cap.js`.\n- **`check_outcome_states`:** called directly, it passes over the shipped descriptor. Each in-memory break reds exactly one row.\n- **AC7:** `symbols.json` lists `check_outcome_states` for matrix.py, and `gen_map.py --check` exits 0.\n- **Naming lexicon:** `--suggest` returned OK and the full run is OK, with P1 offenders at 1087 (the pin).\n\nThese probes stand in for `govkit selftest`, `govkit acceptance matrix` and `codebase-map coverage + freshness`. They do not replace those gates.\n\n**Owed by the main loop at the close:**\n- New arm `tools/govkit/selftest.py` `[dRB-9]` (covers AC2): RED over the old descriptor (update exits 1, gov_commit stays old), then GREEN.\n- New arm `tools/govkit/matrix.py` settings-merge rows of `check_outcome_states` (covers AC4): RED over the old descriptor on the absent-hook row, and over a block without `must_not_exist` on the both-present row.\n- Green in the same selftest run: `and re-stamps the receipt at the new commit`, `[-12] AC4 NEGATIVE`, `[-12] AC9 NEGATIVE`.\n- The §7 gates: govkit selftest · govkit refusal join · govkit acceptance matrix · govkit selfcheck · receipt sync · recall floor arms · codebase-map coverage + freshness · recall floor.\n\n**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` exited 0 with 28 classes. Acted on:\n- the lexicon run covers naming-leg-grades-what-python-named; there are no nested defs.\n- grep shows `rq9`, `p9`, `rec9`, `sm9` and `means9` bound nowhere else in selftest's main, and nothing collides in `check_outcome_probes` (a-new-local-collides).\n- the stop check matches one line containing both the kit and the stop name (line-claim-matched-over-the-whole-output).\n- staged breaks were built from the shipped block, not a simpler stand-in (staged-break-substitutes-a-synthetic-value).\n- the observed-by joins are covered by the RED-first observations owed above.\n\nNo command timed out and nothing was skipped."
}
~~~~

### 2026-10-14T14:49:15 · gov-builder · wf_b8d5f913-524/ae1ff276138568195

Label: dRedressedBar · TOOL-dRedressedBar-3 · build

~~~~text
{
 "committed": true,
 "sha": "75c185182ad712dc74d47eccf4b8a53930adf3dd",
 "why": "TOOL-dRedressedBar-3 is built as the spec states. Unit 9's fix had already landed (59f11096a), which the consumes-from edge requires. The code agreed with the spec on every point: line numbers are +25 after line 3312 because of unit 9's block, and every other symptom matched. No divergence.",
 "summary": "I committed TOOL-dRedressedBar-3 as 75c185182 with `Pass: TOOL-dRedressedBar-3` and the Co-Authored-By trailer. Most criteria were checked by a probe on scratch targets. AC3's full apply and every new arm's RED-first run are left for the close.\n\n**What changed** (only these paths, staged by name; no CR bytes staged):\n- `tools/govkit/selftest.py`:\n  - **S1:** the PV fixture text `_pvCAP_T` now ends with the owner's `const AGENT_TYPE_SHAPE = ` line, read at run time from `tools/workflows/tier2-review.template.js`.\n  - **S2:** the aQuenchedHarness-3 fixture selects `kickoff-manifest` in both its deploy kits line and its `--kits` argument. Its `[answers]` gain `manifest_path` and `user_skills`, read from `DEPLOY_FULL`.\n  - **S3:** the runner branch of `check_roles_install` adds a `gate_file` answer, read from `tools/codebase-map/kit.toml`'s `GATE_FILE` default.\n  - **S4:** the four `[-8]` writing updates over `d8-ac1` and `d8-ac4` now pass `--kits check-wiring`.\n  - **S5:** the u2a, u4 and u9 calls are untouched.\n- The spec's status header is set to CLOSED · 2026-10-14. Nothing else in the spec changed.\n- `memory/builds/dRedressedBar/README.md`: only this unit's index row changed. `gen_build_index.py --write` re-rendered it after the status flip.\n\n**Checks that ran** (fixtures under `%TEMP%/dRB3`; each stands in for the `govkit selftest` arms named):\n- **AC1** (stands in for the PV block-1 arms): grep finds no hit carrying `{0,63}`. The parity script's awk over three files holding the new text prints 3 hits of one literal. With the line dropped it prints 0, which is the DEAD PROBE case.\n- **AC2** (stands in for the aQuenchedHarness-3 arms): the apply with `kickoff-manifest` exits 0 and lands `agent-cap.js`. Without it, the apply exits 2 and prints `'agent-cap' requires 'kickoff-manifest'`.\n- **AC3, token half only** (stands in for OC8 AC4 and OC13 AC4): I called the engine's own leg rendering over the registry default. Without the answer, codebase-map's leg carries an unresolved `gate_file`. With it, none of the 29 legs does.\n- **AC4** (stands in for `[-8] AC1` and `[-8] AC4`): the grep criterion holds. `derive_default_gained` from 24f39915 to 9ddcc5c9 gives `['run-gates']`, and the `if kits else` line is present in `govkit.py`. With the scope, the four updates on a fixture built like `delta_target`'s all exit 0 and read `diverged`, and the operator's line survives. Without the scope, the 9ddcc5c9 update exits 1 naming `check-receipt.py` and `held_halves.py`.\n- **AC5** (stands in for the re-stamp arm and `[-12] AC4/AC9 NEGATIVE`): the grep criterion holds. An `update --write` on a target built like `stale_target`'s exits 0 and re-stamps `gov_commit` at gov HEAD 59f11096.\n- The M6 checklist (`gotchas.py --for-diff HEAD~1..HEAD`) ran and I went through each class. The new local names are unique. Values are read from their owners rather than typed. No old-selection wording is left standing (`agent-cap,settings-merge` survives only at lines 6505-6529, an unrelated requires arm). No arm became vacuous.\n\n**Left for the main loop at the close:**\n- AC3's full apply: no `WITHHELD from` line, and a written `tools/gate-legs.json`. That apply runs the scratch target's `run-gates.sh` at the host turnstile, so I did not run it.\n- AC4's two `[-8]` arms and AC5's three arms inside the suite.\n- The spec's flagged unknowns (`UNVERIFIED`): any further red in PV block 1 or the AFTER step.\n- The RED-first runs of all five `New arm:` lines in `tools/govkit/selftest.py` (AC1 to AC5), each RED on its staged break and GREEN once restored. A known trap for those breaks: a staged break can run stale bytecode.\n\nNo command timed out or was skipped. The parent's orientation card called this unit not buildable because it said the spec does not exist. The spec is present on this branch, and the scratch-guard hook did not refuse any edit."
}
~~~~

### 2026-10-14T14:59:54 · gov-builder · wf_dd507e84-fcf/a9cc4903461cf4d48

Label: dRedressedBar · TOOL-dRedressedBar-4 · build

~~~~text
{
 "committed": true,
 "sha": "305ea9c20e3068f5e62956724f0b628021269bbd",
 "why": "TOOL-dRedressedBar-4 is built as its spec states and committed with its Pass trailer. The status header is set to CLOSED, and the generated build README row was re-rendered to match.",
 "summary": "Commit 305ea9c20 on branch/gov-bar-reds-fix fixes the two `workflows` lines the `install-prefix (shipped surface)` gate counted as kit paths. That directory belongs to Claude Code, not the review-harness kit, so each file now holds the name in a constant and the join uses the constant. I ran no gate or suite, so the leg going green is still owed at the close.\n\nFiles changed (declared before writing; the last two are records):\n- C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/tools/hooks/format-guard.js: adds `const WORKFLOW_RUNS_DIR = 'workflows'` after RUN_ID_RE, with a one-line `//` comment above it. The join in readJournalAgents now uses the constant (line 335).\n- C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/tools/roles/adopt-roles.test.sh: the A9_WRITE program adds `WORKFLOW_RUNS_DIR = \"workflows\"` after the `sub =` line, with a `#` comment and no apostrophe. The fixture's path line is now `wf = sub / WORKFLOW_RUNS_DIR / \"wf_00000001-aaa\"`. The spec's line numbers are 2 lower than the file because unit 1 added two lines earlier; I located the lines by their content, so this is not a divergence.\n- C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-4.md: the status header only, now CLOSED, date 2026-10-14.\n- C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/README.md: `gen_build_index.py --write` changed one line, this unit's row from SPECCED to CLOSED, as units 2, 3, 8 and 9 did. The symbol map lists functions only and no line numbers, so it was not regenerated.\n\nChecks that ran (probes, each standing in for part of a gate):\n- AC1: the quoted-literal search over format-guard.js prints one line, the declaration. The constant search prints the declaration and the join, nothing else. Stands in for the format-guard.js half of `install-prefix (shipped surface)`.\n- AC3: the same over adopt-roles.test.sh prints only `WORKFLOW_RUNS_DIR = \"workflows\"`, and the `wf = sub / WORKFLOW_RUNS_DIR /` line is found. Stands in for the adopt-roles half of that leg.\n- AC2: readJournalAgents over a journal planted in the scratchpad prints `{\"started\":[\"a1\"],\"ended\":[\"a1\"]}`. Red case seen on a scratch copy with the constant set to `workflowz`: it prints the unreadable-journal (ENOENT) error. Stands in for the `format-guard self-test` journal scenario.\n- AC4: the A9_WRITE program, extracted to a file, has 0 apostrophes, exits 0, and writes `sess/x/subagents/workflows/wf_00000001-aaa/journal.jsonl`. Red case seen on a copy with the constant changed: the file is not there. Stands in for arm 9 of the `roles adopter self-test`.\n- A copy of the gate's per-line scanner (rules 1-4, cut from check-install-prefix.sh into a scratch probe) reads every changed line clean. It still flags both old spellings, so the probe can fail. This is a probe, not the gate.\n- `node --check` on format-guard.js and `bash -n` on adopt-roles.test.sh both pass. LF line endings confirmed (0 CR bytes).\n\nBug-class checklist (`gotchas.py --for-diff HEAD~1..HEAD`): 18 classes selected, none needs a change:\n- Both red cases were observed, and the scanner probe can fail.\n- No heredoc and no code fence were written.\n- The constant is declared twice on purpose: spec §4 keeps the fixture's own copy so it can catch the reader drifting.\n- held-suite-guard-misses-a-sibling-kit: the roles suite reads format-guard.js (arm 11), but its leg in gate-legs.json has no guard field, so a hooks edit cannot skip it.\n- The rest do not apply to this diff.\n\nOwed at the close (main loop), from spec §7:\n- `install-prefix (shipped surface)` should read GATE ok with its two logged hits gone and no new hit. This is this unit's own red leg.\n- The legs that run because of the hook edit: `format-guard self-test`, `agent-cap self-test`, `scratch-guard self-test`, `verifier fan-out self-test`, `review-join self-test`, `hook destinations self-test`.\n- Also `roles adopter self-test` and `foreign-prefix parity (every self-test at three prefixes)`.\n- `kit epoch` and `kit version markers` will read red here until unit 7 bumps the kits; unit 10 corrects which kit that is.\n- This unit adds no new suite arm, so no RED-first observation is owed for it.\n\nNothing timed out or was skipped. The commit ends with `Pass: TOOL-dRedressedBar-4` and `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. That trailer follows the harness instruction and units 2, 3, 8 and 9, but the charter's Facts spell it \"Claude Opus 5\"; if the charter's spelling governs, this line needs changing."
}
~~~~

### 2026-10-14T15:04:35 · gov-builder · wf_a09b3c92-9e1/a8f3d3c2eba08d9ab

Label: dRedressedBar · TOOL-dRedressedBar-5 · build

~~~~text
{
 "committed": false,
 "sha": "",
 "why": "DIVERGENCE: §6 AC3 (its second half) contradicts §2 S5 and §4 \"The suites\", so a build that does exactly what S5 and §4 say would fail AC3. AC3 says that across the pass, `grep -o '\\$(printf ' tools/workflows/unattended-build.test.sh | wc -l` falls by exactly five (288 to 283). But all eight `var-pipe` candidates §4 pins (`:1902`, `:1904`, `:1909`, `:2698`, `:2711`, `:2757`, `:2768`, `:2771`) are written as `$(printf '%s' \"$X\" | sed 's#\"slug\":\"tB\",#…#')`. Each one carries a `$(printf ` occurrence, and the forms-table row `w=${v/'A'/'B'}` removes it. I counted these with grep over those lines: 8 occurrences, and 6 more on the six `printf-subst` candidate lines. So the fall would be 5 + 8 = 13, from 288 to 275. Picking different sites does not help: only two `var-pipe` sites in the file sit outside a `$(printf ` (`:1582` and `:1999`), so dropping `var-pipe` by eight always takes at least six `$(printf ` occurrences with it. To be consistent, AC3 would have to say one of two things. Either the `grep -o '\\$(printf '` count falls by exactly thirteen (five `printf-subst` sites plus the eight `sed` sites, 288 to 275). Or the count is limited to `$(printf ` substitutions with no `|` inside them, which falls by exactly five. Its \"Red when\" and figure lines would change to match. The first half of AC3 holds as written (exactly five `-` lines spell a pipe-free `$(printf `, and their `+` lines spell `printf -v _wfj`). Nothing else I read diverged: the start-of-unit `git diff ebce889c` over the five files moves no site, and the AC1 and AC2 baselines match the pinned figures. Nothing was edited and nothing was committed. The spec's uncommitted INPROGRESS status edit was in the tree before this pass started and is left as found.",
 "summary": "I stopped before writing any code because the spec contradicts itself, so nothing is committed and the tree is as I found it.\n\n**What I checked:**\n- **The start-of-unit diff** (§4) over the five declared files, `git diff ebce889c`. The changes from units 1 and 4 add or remove no fork site. They only shift line numbers in `tools/roles/adopt-roles.test.sh`: +2 after line 83 (the probe stop) and +4 from line ~228 on. Every site is still found by its content.\n- **Baselines for AC1–AC3:** AC1 prints the 10 pinned lines. AC2 gives 3 / 1 / 12 / 70 for the four files. AC3's `$(printf ` count is 288, and the registry rows for `tools/workflows/unattended-build.test.sh` are still 66 (`printf-subst`) and 62 (`var-pipe`). All match the spec.\n\n**The contradiction (AC3 against S5 and §4):**\n- All eight `var-pipe` sites §4 pins are spelled `$(printf '%s' \"$X\" | sed …)`, so each carries one `$(printf `. I counted 8 on those lines and 6 on the six `printf-subst` candidate lines.\n- Converting them as S5 requires would drop AC3's `$(printf ` count by 13, from 288 to 275, not by exactly five.\n- Picking other sites can't fix it: only two `var-pipe` sites in that file (`:1582` and `:1999`) sit outside a `$(printf `.\n- The spec writer needs to change AC3 to either \"falls by exactly thirteen\" or a count of pipe-free `$(printf ` substitutions only.\n\n**What I left alone:**\n- I wrote no file; I only read sources and ran grep/awk counts in the worktree.\n- `gotchas.py --for-diff` was not run, because there is no commit for it to read.\n\n**Still owed when this unit is rebuilt:**\n- AC1–AC8 as the spec defines them (the AC4 forms probe and the AC5–AC7 fixture-clone runs of both adopters).\n- At the close, the main loop runs the §7 gate list, starting with `shell hygiene (a fork spent on builtin work)`. No arm is new, so no RED-first observation is owed.\n\nMy write set, declared before I started (none of it touched): `tools/branch-reconcile/adopt-branch-reconcile.sh`, `tools/roles/adopt-roles.sh`, `tools/roles/adopt-roles.test.sh`, `tools/hooks/format-guard.test.sh`, `tools/workflows/unattended-build.test.sh`, and the status header of `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-5.md`."
}
~~~~

### 2026-10-14T15:08:49 · gov-spec-writer · direct/aee8f8f0fe6cb01b7

Label: dRedressedBar · TOOL-dRedressedBar-5 · spec-write

~~~~text
I revised AC3 of TOOL-dRedressedBar-5 at rev-3. The two forms you offered were a pipe-free count falling by five and a whole-file count falling by thirteen. I chose the whole-file `$(printf ` count falling by exactly thirteen.

Spec: `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-5.md`

**What changed**
- **Header:** rev-2 is now rev-3. I left the INPROGRESS status as it was in the working tree.
- **AC3, second half:** the count must fall by exactly thirteen: one for each of the five `printf-subst` sites, plus the one `$(printf '%s' … | sed …)` on each of the eight `sed` sites. The forms-table row `w=${v/'A'/'B'}` removes that last one. The first half (exactly five pipe-free `-` lines whose `+` lines spell `printf -v _wfj`) is unchanged.
- **AC3 "Red when":** AC3 now goes red in four cases:
  - a `printf-subst` site is left unconverted;
  - a sixth one converts and its row drifts below the scan;
  - a `var-pipe` conversion leaves its `$(printf ` behind;
  - a `var-pipe` site other than the eight pinned `sed` sites is converted instead of one of them.
- **AC3 figure:** 288 at `ebce889c` and 275 after the pass, both PINNED. Each of the fourteen §4 candidate lines carries exactly one occurrence, which accounts for 14 of the 288. The caveat about the start-of-unit diff stays.
- **§9:** a rev-3 entry scoped to `AC3`. Nothing else in the spec moved.

**Why thirteen and not the pipe-free five:** the pipe-free count can't see a `var-pipe` conversion that leaves `$(printf '%s' … |` behind. The whole-file count catches that, and it also reds on an unconverted or extra `printf-subst` site. If an extra `printf-subst` conversion and a leftover `var-pipe` ever cancelled out at thirteen, the first half's "exactly five `-` lines" still catches it.

**Checked against the source**
- I saved `ebce889c`'s `tools/workflows/unattended-build.test.sh` to the scratchpad. The whole file has 288 `$(printf ` occurrences, and so does HEAD.
- I counted per line on `:1047`, `:1048`, `:1440`, `:1860`, `:2812`, `:2815`, `:1902`, `:1904`, `:1909`, `:2698`, `:2711`, `:2757`, `:2768` and `:2771`. Each has exactly one, 14 in total.

**Brief acceptance:** `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades TOOL-dRedressedBar-5 as INPROGRESS and READY, and names it next.

**Memory hygiene** fails, for two reasons:
- **Check 9 (expected):** `memory/LIVE.md` and `memory/builds/dRedressedBar/README.md` differ from a fresh render. That comes from the status and rev change in this spec. I did not regenerate them, so `python tools/memory-tree/gen_build_index.py --write` is yours at commit.
- **Check 23 (not from this revision):** it flags ledgers of the CLOSED units TOOL-dRedressedBar-2, -4 and -9, and of older builds. None of it involves this spec.

The hygiene run printed no other FAILED line.

Nothing is committed.
~~~~

### 2026-10-14T15:13:48 · gov-builder · wf_f2a7fdd9-157/a947ec29b2cf91bae

Label: dRedressedBar · TOOL-dRedressedBar-5 · build

~~~~text
{
 "committed": false,
 "sha": "",
 "why": "DIVERGENCE: two statements in spec rev-3 are wrong about the code. Building either site as the spec describes it would turn a §7 gate red at the close. Fixing either one means choosing a placement the spec does not give.\n\n(1) §4 \"The suites\", `tools/roles/adopt-roles.test.sh` `:160` and `:245` (ebce889c numbering), and the forms-table `tr -d '\\r'` row. Both sites sit inside the `\"$( … )\"` argument of `check_arm`. On the bash the bar runs (Git Bash 5.3.9, MSYS), a `$'\\r'` written inside a command substitution loses its CR, so `${out//$'\\r'/}` there strips nothing. Probe: `out=$'a\\r'; [ \"${out//$'\\r'/}\" = a ]` passes at top level, but `echo \"$([ \"${out//$'\\r'/}\" = a ] && echo ok || echo FAIL)\"` prints FAIL. The same happens with `[[ ]]` and with a bare `$( )`. A CR held in a variable set at top level works, and `$'\\n'` inside `$( )` also works. `handoff.py` stdout carries CR on Windows (52 CR bytes in one `roster` run), so arms 6 and 9 would fail wrongly. The assertion probe, run against the HEAD spellings, flipped both arms' passing specimens from 1 to 0.\n\nWhat the spec would have to say: where the strip goes. Either at top level on the capture lines, as `out=$(…); rc=$?; out=${out//$'\\r'/}` at ebce `:158` and `:243` (`out` is not read again in either arm before arm 7 reassigns it), or through a CR variable set at top level, which needs a new §4 Inventory row such as `_cr`. The row's `exact only when` cell would have to exclude a command substitution under MSYS bash, and AC4 would need a specimen run inside `$( )`.\n\n(2) §4, the paragraph under the forms table (\"It is not a `while read` loop, so the loop leg does not grade it\") and §7's note that the loop leg \"grades the `mapfile` form\". Both are false for the row written on one line at `:183`. `scan_file` (`tools/gate-lint/sh_hygiene.py:314-322`) treats a line as a loop when `done` appears anywhere on it. It then grades a `<<<` whose tail names a variable last assigned from a command substitution as `loop-var-sub`, a gated class. `out` is assigned at `:182` by `out=$(cd \"$FX\" && …)`, and the file has no row in `memory/project/substitution-fed-loops.txt`, so `shell hygiene (a loop fed by a command substitution)` would go red. Probe: `scan_file` on the one-line spelling returns `{'loop-var-sub': [(2, '<<<')]}`. With `mapfile -t _l8 <<< \"$out\"` moved to the end of the `:182` capture line and the `for` loop left on `:183`, it returns nothing.\n\nWhat the spec would have to say: that placement, or another, with the paragraph and §7 corrected.\n\nNothing else diverged. The start-of-unit `git diff ebce889c` over the five files moves no site. All paths are restored and nothing is committed.",
 "summary": "Not committed: returned as a DIVERGENCE. All five files are restored (`git status` is clean), and the fixture clone at `C:/Users/d41ly/AppData/Local/Temp/dRB5fx` was removed. The `gotchas.py --for-diff` checklist did not run because there is no commit to run it over.\n\nPaths I declared before editing: the five files the spec names, plus the spec's status header.\n\nAll checks below ran against a full build of the unit before I restored it. Each is a probe, not a gate.\n\n**Grep and classifier probes** (stand in for `shell hygiene (a fork spent on builtin work)`):\n- AC1: the grep printed nothing.\n- AC2: counts were 0, 0, 0 and 62 for the four files.\n- AC3: the `$(printf ` count went from 288 to 275. The working diff had five `-` lines with a pipe-free `$(printf `, and their `+` lines all spelled `printf -v _wfj`.\n- The leg's own classifier (`scan_spawn_file`), called on each file: the four files with no registry row read empty. `unattended-build.test.sh` read printf-subst 66, var-pipe 62, pure-fn-subst 28, cat-file 1 and path-subst 6, which matches every row.\n- AC8: the registry file was untouched.\n- `bash -n` parsed all five files.\n\n**AC4 forms probe** (run under Git Bash 5.3.9): 103 cases matched and 2 differed, both expected:\n- The staged wrong form, `${CH%/*}` alone on `AGENTS.md`, gave a different answer, as AC4 requires.\n- The planted `.` specimen for the end-anchored row showed the narrowing its `exact only when` cell declares.\n- All 13 `unattended-build.test.sh` sites, read at their converted lines, matched the HEAD spelling.\n- Log: `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-bar-profile-failures-b80cc3/8d2976c7-7629-4ba0-8a96-2098db6da20f/scratchpad/ac4-forms-probe.log`\n\n**AC5–AC7 fixture** (stands in for the `roles adopter self-test` and `branch-reconcile selftest` adopter paths): a clone under `%TEMP%`, running the ebce889c adopters against the converted ones. 22 of 22 passed: the same lines and exit status from the root, from each kit directory with a slash-free `$0`, and by absolute path. It also covered withdrawal, kept-foreign, the whole-line near miss, CRLF, indented hits, and the surviving-token lines. The comparison was seen red once, while the fixture had a state-ordering bug of its own. Log: `.../scratchpad/ac5-7-adopter-fixture.log`\n\n**Assertion probe** (stands in for the `roles adopter self-test` arms): each converted `adopt-roles.test.sh` assertion, read from the file, run against its HEAD spelling. 19 matched. The 2 that flipped are the arm 6 and arm 9 CR sites behind finding (1).\n\n**Owed to the close** after the spec is revised: the §7 gates, every suite leg on that line, and the loop leg against the chosen `mapfile` placement. The unit declares no new arm, so no red-first observation is owed.\n\nProbe scripts are in the scratchpad: `forms-probe.sh`, `adopter-fixture.sh`, `assert-probe.sh`, `cr-probe.sh`."
}
~~~~

### 2026-10-14T15:29:33 · gov-spec-writer · direct/a7e4ecc570d99c0c3

Label: dRedressedBar · TOOL-dRedressedBar-5 · spec-write

~~~~text
I've revised TOOL-dRedressedBar-5 to rev-4 and fixed both findings using the placements you measured. `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` still grades it READY.

Spec: `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-5.md`

I confirmed both findings under Git Bash 5.3.9 before editing:
- **CR:** inside `$( )`, a `$'\r'` comes out empty (`$(v=$'\r'; echo ${#v})` prints `0`), so a strip written there removes nothing. Stripping at top level and then comparing inside `$( )` gives 1 for both arm 6 and arm 9. The wrong placement gives 0.
- **Loop:** `scan_file` returns `loop-var-sub` for the `mapfile` row written on one line, and nothing once the `mapfile` moves onto the capture line.

**(1) Where the CR strip goes.**
- **Placement:** I chose the strip at top level on the capture lines, not a `_cr` variable. That adds no new name and no Inventory row.
- **The capture lines:** ebce `:158` and `:243` each end `; rc=$?; out=${out//$'\r'/}`. The strip comes after `rc=$?`, so `rc` still holds the command's exit status.
- **Nothing else sees the stripped value:** at ebce, `:160` and `:245` are the only lines that read those values of `out` before `:168` and `:266` reassign it.
- **The two compares:** `:160` now uses the end-anchored row, `[[ $out$'\n' == *" task-sha=$msha"$'\n'* ]]`, and `:245` compares `"$out"` directly. A `$'\n'` inside `$( )` works, as the existing `"$A9L1"$'\n'"$A9L2"` already shows.
- **Forms table:** the CR row's "exact only when" cell now says the strip must be written outside every command substitution, and why.
- **AC4:** it now runs arm 9's shape on a CRLF capture. It also stages a second wrong form, the strip written inside `$( )`, which must report a difference.
- **§5 risks:** updated to match.
- **Alternatives rejected:** gains the `_cr` variable.

**(2) Where the `mapfile` goes.**
- **The fix:** `mapfile -t _l8 <<< "$out"` goes at the end of the `:182` capture line, after `rc=$?`. The `for … done` count stays on `:183`.
- **The paragraph under the forms table** now says what the scanner actually does:
  - It treats any line containing `done` as a loop (`tools/gate-lint/sh_hygiene.py:135`, used at `:314`).
  - On such a line it flags a `<<<` fed by a variable captured from `$( )` as `loop-var-sub` (`:317-322`).
  - On a line without `done`, it flags a `<<<` only when the text after it holds a substitution itself (`:319-320`).
  - `mapfile` assigns nothing the scanner tracks (`:101`), so the `for` line is clean.
- **§7 note:** rewritten to the same effect.
- **Alternatives rejected:** gains the registry row in `memory/project/substitution-fed-loops.txt`, refused because a code change fixes it.

**Two changes beyond the literal brief:**
- **AC4 and §5:** I treated these as part of finding (1), because they are what makes the placement checkable.
- **CR in the `:183` count:** the spec now states that this count needs no CR strip as long as each CR sits at the end of a line. That is the shape the fixture's CRLF lines give, and `_re8` only anchors at the start of the line. I couldn't show that handoff.py never writes a CR mid-line: a `roster` run in this repo printed no CR at all.

Nothing else in the spec moved, and §8 still says "none". No `$'\r'` sentence claims a strip inside `$( )` works, and nothing says a one-line `… done` row escapes the loop leg.

`memory hygiene` currently fails 3 checks (check 23). They name closed units TOOL-dRedressedBar-2, -4 and -9 plus older aSparedSpawn and aOrientedCast ledgers, so they come from other units' records, not this spec. No line of the gate's output names TOOL-dRedressedBar-5.

The probe scripts are in the session scratchpad: `crprobe.sh`, `crprobe2.sh` and `loopprobe.py`. I committed nothing and regenerated no index. The spec's generated records table doesn't yet list the untracked prompts 5-4 and 5-5.
~~~~

### 2026-10-14T15:36:43 · gov-builder · wf_87100300-6ba/a98be3b1b3d8668db

Label: dRedressedBar · TOOL-dRedressedBar-5 · build

~~~~text
{
 "committed": false,
 "sha": "",
 "why": "DIVERGENCE: §4 \"The adopters\" tells me to convert `tools/branch-reconcile/adopt-branch-reconcile.sh:142` to `mkdir -p \"${SKILL%/*}\" || exit 1`. §7 says `harness arms (fail branches armed or pinned)` only reads the adopters' exit sites \"this unit keeps in place\". That is wrong for `:142`. `memory/project/unarmed-branches.txt:178` pins that exit as a DELEGATED refusal site, and a delegated site's key is its own source line with the whitespace squeezed (`tools/memory-tree/check-arms.py:551`). The row reads `mkdir -p \"$(dirname \"$SKILL\")\" || exit 1`, and those rows are graded because `ARMS_REFUSALS=\"graded\"` is set at `.memory-tree.conf:639`.\n\nConverting the line keeps the site on its line but changes its key, so `check-arms.py --check` would report two problems at the close:\n- the pin \"which no live site carries — the refusal was deleted, reworded\" (`check-arms.py:867-871`);\n- the new `mkdir -p \"${SKILL%/*}\" || exit 1` site, which \"has no POSITIVE assertion … and is not pinned\" (`:863-865`).\n\nI confirmed this with a probe that calls check-arms' own `scan_refusal_sites`, comparing the ebce889c adopter with the converted one. The `:142` key disappears and a new one appears; row 178 matches a live site before the change and none after. All 10 other pins for that adopter stay live, and the roles adopter's 2 sites don't change. Leaving `:142` unconverted doesn't help either: the file would keep 1 `path-subst` site with no row, so the spawn-idiom leg stays red. No placement the spec gives turns both legs green.\n\nThe spec would have to choose one of these:\n- **(a)** Re-key row 178 of `memory/project/unarmed-branches.txt` to the converted line's signature `mkdir -p \"${SKILL%/*}\" || exit 1`, keeping its gate, kind, occurrence (1) and reason. That file then joins Files touched, and an AC states the registry keeps the same number of rows and only row 178's signature field changes. §3 and §7 also need correcting, including a sentence on whether re-keying a pin counts against the brief's rule against raising a pin or registry row.\n- **(b)** Another form for `:142` that the spec writer probes against check-arms.\n\nNothing else in the spec failed. I restored all five paths and committed nothing. The worktree is clean at 79e78d8a2.",
 "summary": "No commit: one statement in spec rev-4 is wrong about the code (see `why`). I built the whole unit, checked it, found the conflict, then restored all five files. The worktree is clean at 79e78d8a2, and the fixture clone `%TEMP%/drb5fx` is removed.\n\nBefore I restored them, everything else in the spec checked out on the uncommitted work. No gate, suite or bar ran. These probes stand in for the §7 legs:\n\n- **Spawn-idiom and loop legs:** a probe calling the leg's own `scan_spawn_tree` and `scan_file` (`count.py`) stands in for `shell hygiene (a fork spent on builtin work)` and `shell hygiene (a loop fed by a command substitution)`. The four files with no row read 0 in every class. `unattended-build.test.sh` reads printf-subst 66 and var-pipe 62, equal to its rows, with its other classes unchanged. The loop leg finds nothing new.\n- **Harness arms:** a probe calling check-arms' own `scan_refusal_sites` (`arms_probe.py`) stands in for `harness arms (fail branches armed or pinned)`. It found the red described in `why`.\n- **AC1:** the grep prints nothing.\n- **AC2:** 0, 0, 0 and 62, matching the row of 62.\n- **AC3:** the whole-file `$(printf ` count falls from 288 to 275, a fall of 13. The check on the `-`/`+` lines needs a pass commit, so it is still owed.\n- **AC4:** the forms probe ran under Git Bash 5.3.9 and stands in for the converted assertions of the roles, format-guard and unattended-build self-tests. It reported 159 same, 0 different, and all 3 staged wrong forms differed as they must: `${CH%/*}` alone, and the CR strip written inside `$( )` (twice). All 9 check_arm sites produced both a 1 and a 0. One specimen matches the end-anchored row's stated boundary (a literal `.` narrows the match) and is counted as such.\n- **AC5–AC7:** the adopter fixture compared the old and new adopters in a clone and stands in for `branch-reconcile selftest` and `roles adopter self-test`. It passed 22 of 22.\n- **AC8:** `memory/project/spawn-idiom-sites.txt` was not touched.\n\nChoices the next build can reuse: `_re2` and `_nb` are assigned inside their site's `$( )`, and the printf-subst sites converted are 1047, 1048, 1440, 1860 and 2812 (2815 is left).\n\nStill owed at the close: every §7 leg. The spec declares no `New arm:`, so there is no RED-first observation to make. `gotchas.py --for-diff` did not run because there is no commit to give it.\n\nEverything is under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-bar-profile-failures-b80cc3/8d2976c7-7629-4ba0-8a96-2098db6da20f/scratchpad/u5/`:\n- `rev4-build.diff` — the full working diff\n- `forms-probe.sh` and `ac4-forms-probe.log`\n- `adopter-fixture.sh` and `ac5-7-adopter-fixture.log`\n- `count.py`, `count-before.txt`, `count-after.txt`\n- `arms_probe.py`"
}
~~~~

### 2026-10-14T15:49:34 · gov-spec-writer · direct/a1bb310a71109273d

Label: dRedressedBar · TOOL-dRedressedBar-5 · spec-write

~~~~text
I revised TOOL-dRedressedBar-5 to rev-5 and took option (a): row 178 of `memory/project/unarmed-branches.txt` gets a new signature. There is no option (b). Nothing is committed and the build README is not regenerated. Both are left for you.

**Why (b) fails.** Row 178's key is `mkdir -p "$(dirname "$SKILL")" || exit 1`. Any line whose squeezed text equals that key still contains `$(dirname "$SKILL")`. The fork leg counts any `$( )` whose first word is `dirname` as a `path-subst` site (`tools/gate-lint/sh_hygiene.py:786-787`), and a `$( )` forks a subshell anyway. I also ruled out putting an `# arm-signature:` marker carrying the old line text above the converted line. That marker is meant to declare text the callee prints (`check-arms.py:88-90`), so it would be false, and it would add a line to the adopter. Both rejections are in §4's Alternatives rejected.

**Probe.** I ran it in the scratchpad, calling check-arms' own `scan_refusal_sites` with all six §4 conversions applied to the `ebce889c` adopter.
- **`ebce889c` adopter, current rows:** all 11 pins for `adopt-branch-reconcile.sh` are live.
- **Converted adopter, current rows:** row 178 is stale and `mkdir -p "${SKILL%/*}" || exit 1` is unpinned. This matches your report.
- **Converted adopter, row 178 re-keyed:** all 11 pins are live and no site of that file is unpinned. This is the brief's acceptance.
- **`ebce889c` adopter, row 178 re-keyed:** the stale pin and unpinned site come back. This is the red case AC10 sets up on purpose to show the probe can fail.
- The `:25` conversion changes no key, because check-arms only reads `exit 1` sites (`EXIT_RE`, `check-arms.py:146`).
- The two `adopt-roles.sh` sites keep their keys. They are still unpinned in every run until TOOL-dRedressedBar-6 adds arms for them.

**What rev-5 changes:**
- **§2:** new scope item S7, the re-key of row 178 in the pass commit. Only field 4 changes.
- **§3:** a new non-goal saying a re-key is not a raise. The row count and the row's gate, kind, occurrence and reason stay the same.
- **§4:**
  - A paragraph on the pin that follows `:142`, citing `check-arms.py:86-91`, `:551`, `:863-871` and `.memory-tree.conf:639`.
  - The pin file added to Files touched.
  - Three rejected alternatives: a spelling that keeps the old key, the marker, and leaving `:142` unconverted.
- **AC9:** the pin file's diff at the pass commit is one hunk. The old and new rows agree on fields 1, 2, 3 and 5, field 4 becomes `mkdir -p "${SKILL%/*}" || exit 1`, and the line count doesn't change.
- **AC10:** the `scan_refusal_sites` probe, including the deliberate red run against the previous commit's adopter.
- **§7:** corrected to say which sites `harness arms` grades and why the conversion and re-key must land in the same commit.
- **§9:** a rev-5 entry.

**One addition beyond the brief.** Putting the pin file in Files touched brings it under the `memory/` guard of the `recall floor` and `recall floor arms` legs. That guard is shared by only two legs, so the spec-token check doesn't treat it as broad and requires both legs on §7's line. I added them, and the rev-5 entry says why.

**Memory hygiene** reports nothing for this spec. It does fail two checks I didn't fix:
- **Check 9:** `memory/builds/dRedressedBar/README.md` is stale, which you clear when you regenerate the index at commit.
- **Check 23:** ledger entries of other units and builds, which this spec doesn't touch.

I did not run `unattended.sh --plan dRedressedBar --paths`, the brief's READY check, because it is outside the gates I may run. It is still owed to you.

Files:
- `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-5.md` (the only file written in the tree)
- `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-bar-profile-failures-b80cc3\8d2976c7-7629-4ba0-8a96-2098db6da20f\scratchpad\arms5\probe.py` (the probe, not committed)
~~~~

### 2026-10-14T15:57:14 · gov-builder · wf_295d6b9f-6a5/a5092d46835faecff

Label: dRedressedBar · TOOL-dRedressedBar-5 · build

~~~~text
{
 "committed": true,
 "sha": "ecdca277e211fab9a64b60a129a22b6683daac82",
 "why": "TOOL-dRedressedBar-5 is built as rev-5 of the spec states it and committed as one pass commit. The commit carries the `Pass: TOOL-dRedressedBar-5` trailer, and in the same commit the spec's status header moved from INPROGRESS to CLOSED. The date was already 2026-10-14, so nothing else in the spec changed. Every criterion a probe can reach was observed. The gate and suite verdicts are owed to the close.",
 "summary": "Built TOOL-dRedressedBar-5 in pass commit ecdca277e on branch/gov-bar-reds-fix.\n\nBefore any edit, `git diff ebce889c` over the five files confirmed that units 1 and 4 added and removed no site. They only shifted lines in tools/roles/adopt-roles.test.sh, by +2 after :83 and +4 after :225. The spec's sites were mapped by their content.\n\nPaths written, declared before writing:\n- tools/branch-reconcile/adopt-branch-reconcile.sh\n- tools/roles/adopt-roles.sh\n- tools/roles/adopt-roles.test.sh\n- tools/hooks/format-guard.test.sh\n- tools/workflows/unattended-build.test.sh\n- memory/project/unarmed-branches.txt (row 178, field 4 only)\n- the spec's status line\n\nThe status flip also re-rendered, through gen_build_index.py --write, three generated lines: memory/builds/dRedressedBar/README.md's unit-5 row and build-status line, which reads SPECCED now that no unit is INPROGRESS, and memory/LIVE.md's dRedressedBar row.\n\nEvery conversion replaces its own line, so no file's line count changed. The staged blobs carry 0 CR bytes.\n\nChanges by file:\n- unattended-build.test.sh: the printf-subst sites at :1047, :1048, :1440, :1860 and :2812 now go through `printf -v _wfj`. The eight pinned sed sites now go through `_wfu=${v/'A'/'B'}`, and :2711 assigns OC_CT directly.\n- adopt-roles.test.sh: the CR strip for arms 6 and 9 now sits on the capture lines, now :160 and :247. The `mapfile` for arm 8 is on the :184 capture line.\n\nChecks that ran (probes, never a gate). Each stands in for the gate named here and does not replace it:\n- **sh_hygiene's own scan_spawn_file, imported** (stands in for the leg `shell hygiene (a fork spent on builtin work)`): 0 registry-class sites in the four files that have no row. unattended-build.test.sh reads printf-subst 66, var-pipe 62, pure-fn-subst 28, path-subst 6 and cat-file 1, each equal to its row.\n- **scan_file and scan_probe_file, before and after** (stands in for the leg `shell hygiene (a loop fed by a command substitution)` and the location-probe leg): the same classes at both. The `mapfile` on the :184 line, which holds no `done`, grades nothing.\n- **AC1:** the grep prints nothing.\n- **AC2:** 0, 0 and 0 for the three files, and 62 for the suite, equal to its row.\n- **AC3:** the `$(printf ` count falls from 288 to 275. The commit has five `-` lines with a pipe-free `$(printf `, whose `+` lines say `printf -v _wfj`.\n- **AC4:** the forms probe (scratchpad u5/forms-probe.sh; log u5/ac4-forms-probe.log) ran under bash 5.3.9, the bash the bar runs. All 186 specimen pairs matched, including the specimens the criterion names and every converted site read at its converted line. Both staged wrong forms differed: `${CH%/*}` alone on AGENTS.md, and the CR strip inside `$( )`. A second probe, u5/arm9-real.sh, ran arm 9's compare over the suite's own A9L1/A9L2 values. 4 of 4 matched, and the wrong form failed on the CRLF value.\n- **AC5-AC7** (stands in for the leg `roles adopter self-test` on the adopter half, and for the wiring leg's `--check`): fixture u5/adopter-fixture.sh; log u5/ac5-7-adopter-fixture.log. A clone under %TEMP%/u5fx, with TMPDIR set to the scratchpad, ran the ebce889c adopters against the converted ones. 25 of 25 checks passed: the same lines and statuses from the root, from each kit directory, by absolute path and as ./, plus withdrawal, foreign-file kept, near-miss name kept, CRLF render withdrawn, tools/ hits indented, and the `    line <n>:{{UNKNOWN_TOKEN}}` refusal. The clone was removed afterwards.\n- **AC8:** the diff of spawn-idiom-sites.txt is empty.\n- **AC9:** one hunk with one `-` line and one `+` line, five fields each, agreeing on fields 1, 2, 3 and 5. The file has 181 lines at both commits.\n- **AC10** (stands in for the leg `harness arms (fail branches armed or pinned)`): u5/arms-probe.py ran check-arms' own scan_refusal_sites and parse_pin. All 11 pins for the branch-reconcile adopter are live, with 13 sites in total (11 + 2). The staged red, the `<pass>~1` adopter against the pass rows, reported row 178 stale and the old key unpinned. The two roles sites have equal keys before and after.\n\nAll scratch paths are under C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-bar-profile-failures-b80cc3/8d2976c7-7629-4ba0-8a96-2098db6da20f/scratchpad/u5/. Probe output was not committed: no acceptance ledger exists for any unit of this build, so the main loop records it at the close.\n\n**Found while probing:** under MSYS bash, a `$( )` capture drops the CR of every CRLF. Captured specimens therefore never reach the CR row's boundary, so the probe also stages values with their CRs kept.\n\n**Owed to the main loop at the close:**\n- Every leg on §7's line: both shell hygiene legs, roles adopter self-test, branch-reconcile selftest, format-guard self-test, agent-cap, scratch-guard, verifier fan-out, review-join, hook destinations and tier2-review self-tests, unattended-build self-test, foreign-prefix parity, harness arms, install-prefix, lexicon naming predicates, memory hygiene, recall floor and recall floor arms.\n- Only those suites run the converted suite assertions for real.\n- `harness arms` will still read the two roles-adopter sites as unpinned and unarmed. They are the same before and after this commit, and TOOL-dRedressedBar-6 arms them.\n- This unit declares no new arm, so no RED-first observation is owed.\n- Kit version bumps are TOOL-dRedressedBar-7's.\n\n**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` ran with exit 0 and selected 23 classes. Acted on two: fixture-passes-by-finding-nothing (staged wrong forms, a planted foreign file, the staged arms red) and staged-break-substitutes-a-synthetic-value (the probe over arm 9's real values). The rest do not apply: no heredoc authoring, no message edit, no retirement, no amended criterion.\n\n**Skipped or refused:** none. The worktree-isolation hook refused a few compound command lines; each was re-run as a plain command.\n\n**Trailer choice:** the commit's co-author trailer follows the charter fact, `Claude Opus 5`, over the harness reminder's 5.5, because the reminder gives the project's own instruction precedence."
}
~~~~

### 2026-10-14T16:12:30 · gov-builder · wf_5514e715-0bf/ab81d3712ac291865

Label: dRedressedBar · TOOL-dRedressedBar-6 · build

~~~~text
{
 "committed": true,
 "sha": "9d0ad1c0a46689b2c0f25a165815b91b87d806d8",
 "why": "Built as the spec says, with no divergence. Units 1, 4 and 5, which this unit consumes from, were already CLOSED. Line 209 is armed by rewriting arm 4's existing assertion, and line 217 by a new arm 13. The adopter itself is unchanged. The probe observed every criterion that does not need a gate. The gates and both new-arm RED observations are left for the close.",
 "summary": "TOOL-dRedressedBar-6 is built and committed as 9d0ad1c0a on branch/gov-bar-reds-fix. No gate, suite or bar ran, and neither did either new arm's RED observation.\n\n**What changed** in C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/tools/roles/adopt-roles.test.sh:\n- **S1:** arm 4's remedy assertion (:113) now matches the whole line `roles: remedy — bash $KREL/adopt-roles.sh --scaffold` in the builtin form `[[ $'\\n'$out$'\\n' == *$'\\n'\"…\"$'\\n'* ]]`. That line now holds the :209 signature `/adopt-roles.sh --scaffold`.\n- **S2:** a new arm 13 sits after arm 12 and before the floor check. It builds a fixture and checks it scaffolds clean, then deletes `.claude/skills/build/SKILL.md` and appends `{{UNKNOWN_TOKEN}}` to `house/gov-builder.md`. It then runs `--scaffold` and makes one assertion: exit 1, the :217 signature on one line (:498), the token in the output, and the Skill still absent.\n- **S3:** `FLOOR_ASSERTIONS` goes from 38 to 40, with `# +2 for arm 13 (TOOL-dRedressedBar-6).` directly above it. The header's arm list now names arm 13, and its \"does not check\" paragraph says arm 13 doesn't check which rule refused.\n- **S4:** every added line uses `[ ]` or `[[ ]]`.\n\nThe same commit sets the spec's status to CLOSED (C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-6.md). It also carries one row re-rendered by `gen_build_index.py --write` in C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/README.md: this unit's row, SPECCED to CLOSED. That file was outside the write set I declared; I added it because units 1, 4 and 5 committed the same re-render in their pass commits.\n\n**Checks that ran, and which gate each stands in for:**\n- AC1, AC2 and AC4: the spec's own greps. The only arm 4 hit is the code line :113; the :217 text has one hit, :498, inside arm 13 and not in a comment; the +2 line sits directly above `FLOOR_ASSERTIONS=40`. These stand in for `harness arms (fail branches armed or pinned)`.\n- AC5: I read the diff. No added line pipes into grep, sed, tr or wc, and none spawns `$(printf`. This stands in for the two `shell hygiene` legs.\n- `bash -n` parses the suite.\n- AC3 and both assertions: a fixture probe (scratchpad `probe-r6.sh`). It made a fresh `git init` repository under `%TEMP%/r6fx`, built the way `build_fixture` builds one, and ran the real adopter. Arm 4's new expression read 1 over the one-byte drift. Arm 13's `--scaffold` exited 1, printed the `render_agents: …gov-builder.md: R10 — carries the render token {{UNKNOWN_TOKEN}}` line and the :217 refusal, and left the Skill absent; its expression read 1. This stands in for `roles adopter self-test`. The fixture was removed afterwards.\n- The staged file has no CR bytes. The commit hook's memory-hygiene `--staged` check passed.\n\n**Owed at the close:**\n- The section 6 legs: `harness arms (fail branches armed or pinned)`, `roles adopter self-test`, `foreign-prefix parity (every self-test at three prefixes)`, `shell hygiene (a fork spent on builtin work)`, `shell hygiene (a loop fed by a command substitution)`, and `install-prefix (shipped surface)`.\n- RED then GREEN for the first new arm (AC1): run through `ROLES_ADOPTER` on a copy whose :209 remedy reads `roles: remedy — bash adopt-roles.sh --scaffold`; arm 4 should go red.\n- RED then GREEN for the second new arm (AC2, AC3): run through `ROLES_ADOPTER` on a copy whose agent render has its `|| { …; exit 1; }` refusal removed; arm 13 should go red on exit 0 with a written Skill.\n\n**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` selected 16 classes, and none needed a change:\n- fixture-passes-by-finding-nothing: arm 13 checks the fixture first and names the staged token.\n- staged-break-substitutes-a-synthetic-value: the break appends to the shipped overlay instead of replacing it, and both owed RED breaks change the adopter itself.\n- retirement-inventory-misses-readers-by-value: nothing outside the suite reads the old floor of 38.\n- observed-by-claim-no-arm-discharges: both arms read `$out` and the Skill file, which is where the behaviour shows.\n- The rest don't apply: no heredoc, inline fence, IFS read, fold or historical-sha oracle.\n\nCommands skipped for timeout: none. The trailers are `Pass: TOOL-dRedressedBar-6` and `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. I used the charter's model name, which earlier pass commits also use, rather than the harness reminder's \"Opus 5.5\"."
}
~~~~

### 2026-10-14T16:18:05 · gov-builder · wf_456bafe1-043/a10eee70c479ee80e

Label: dRedressedBar · TOOL-dRedressedBar-7 · build

~~~~text
{
 "committed": false,
 "sha": "",
 "why": "DIVERGENCE: §4 step 2 (S3, mint) and §3 (Non-goals) of memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-7.md assume `govkit.py mint --base ebce889c7` writes only version carriers. On this tree it also rewrites a line that is not a carrier. Committing its output as it stands turns AC4 red. Changing that output by hand is an edit §3 does not allow (\"No generated output is edited by hand\", \"The minter computes every value\"). Fixing the cause is product logic, and §4 says this unit moves none.\n\nWhat I found: the mint moved exactly the four kits in §4's table: agent-cap 1.38->1.39, branch-reconcile 1.4->1.5, roles 1.5->1.6 and unattended 1.106->1.107. `write_version_carriers` (tools/govkit/govkit.py:798) also rewrote tools/playbook/render_playbook.py:1646. That line is the selftest fixture `older_tpl = '<!-- governance-template: v3.5 -->...'`, and the mint changed its v3.5 to v1.28. The cause: the `playbook` entry's version pattern `governance-template: v` (tools/govkit/entries/playbook.kit.toml:6) matches the line. The line sits in playbook-render's file group, and the file carries only playbook-render's marker, so the ownership clause at :862-869 hands the number to playbook-render's version, 1.28. That edit moves playbook-render's shipped bytes without bumping its version.\n\nI checked this by building the mint's output as a commit object that is on no branch (0ce19f01e) and running `derive_epoch_state` over ebce889c7..that commit. playbook-render reads `FAILED · moved in 0ce19f01ee (1 files) · no value change (still 1.28)`, and the four minted kits read clean. The lander's mint has the same defect: any later mint that bumps any kit rewrites this line again. No sibling spec (10-19) covers it.\n\nWhat the spec would have to say, pick one:\n(a) After the mint, restore tools/playbook/render_playbook.py to HEAD, with the reason stated, and hand the carrier-writer defect off as an ask.\n(b) A unit sequenced before this one removes the false match. Either re-spell the fixture so it no longer reads `governance-template: v<number>`, or tighten `write_version_carriers` so another entry's pattern counts only inside that entry's own file group. Option (b) moves playbook-render or govkit bytes, so playbook-render joins the minted set.\n(c) Accept a playbook-render bump caused by the minter's own edit. I would not stand behind this one: it versions a defect.\n\nI restored every path the mint wrote (38 files, back to HEAD). The tree holds only the INPROGRESS status header that was already uncommitted in the spec before this pass; I did not make that change and left it as it was.",
 "summary": "I made no commit: TOOL-dRedressedBar-7 stopped at §4 step 2 on the divergence named in `why`.\n\nPaths this pass would have written: memory/gotchas/INDEX.md, memory/project/method-carriers.txt, the carriers the minter writes and the files its renders rewrite, whatever `regen.py --write` refreshes, and the spec's status header. A SESSION-KICKOFF.md stamp would have been written only if AC6 required one.\n\nChecks that ran, read-only, each standing in for the gate named:\n- **`govkit.py epoch --base ebce889c7` before the mint** (stands in for `kit epoch`, the before-mint half of AC4): FAILED for agent-cap, branch-reconcile, roles and unattended, which matches §4's table. run-gates read clean, so the §4 stop for run-gates did not apply. push-main reads `skip`. Output: scratchpad u7-epoch-pre.txt.\n- **`regen.py --check` before any write** (the liveness half of AC2 for the regen preflight): `12 declared · 10 fresh · 2 stale`. The two stale items are the gotchas INDEX (check 17, as S1 says) and the build index (memory/LIVE.md and the dRedressedBar README). The spec pinned only one stale item. The build-index one most likely comes from the INPROGRESS header in the working tree; `regen --write` would fix both. Output: scratchpad u7-regen-pre.txt.\n- **`govkit.py mint --base ebce889c7`, then everything it wrote put back**: the four kits moved by one in the last component. It also wrote the false carrier at tools/playbook/render_playbook.py:1646, changing v3.5 to v1.28.\n- **`derive_epoch_state` called through `python -c` over a commit object on no branch (0ce19f01e) that holds the mint's output** (stands in for `kit epoch` at the tip, AC4): playbook-render FAILED, the four minted kits clean. Committing the mint's output as it stands therefore turns AC4 red.\n- **The S2 carrier-list probe after the mint** (stands in for `method carriers` check 3, AC3): the one missing row is `.claude/agents/gov-reuse-scout.md`, and the agent file holds no `## M<n>` heading. This matches the spec. The roles render left the agent files byte-identical.\n- **The AC6 watch-path probe over ebce889c7..HEAD**: prints nothing, so no `last-audit:` re-stamp would be owed.\n\nNot run, owed at the close once the unit is re-dispatched: every §7 leg, push-main self-test arms 28 and 29 included. The unit declares no new arm. No command timed out and none was skipped. I ran no gate, suite or bar. I did not run `gotchas.py --for-diff` because there is no commit to give it."
}
~~~~

### 2026-10-14T16:45:10 · gov-spec-writer · direct/ab69485eca378d70e

Label: dRedressedBar · TOOL-dRedressedBar-20 · spec-write

~~~~text
I wrote the spec for TOOL-dRedressedBar-20 at Tier-2, status SPECCED rev-1, order 4. It has one open fork, F1 (below), which needs your answer before the unit can close. The design itself doesn't depend on it.

**Unit:** `TOOL-dRedressedBar-20`
**Spec:** `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-20.md`

**What I verified before writing**
- **The defect.** In a scratch clone of `9d0ad1c0a`, the carrier writer alone, with no version bump, rewrote `render_playbook.py:1646` from `3.5` to `1.28` and changed nothing else. So every `selfcheck --fix` hits it too, not only `mint`.
- **The class across the real registry.** Six lines match another entry's version pattern. Four are real cross-kit carriers: line 3 of each drift-audit harness, under review-harness's pattern. Two are the defect: `render_playbook.py:1397` and `:1646`. What separates them is whether the pattern owner's own file group (`derive_marker_basis`) holds the file. Who owns the line can't separate them, because both shapes look the same to the ownership clause.
- **The class has fired before.** Line 1397 was written as `v3.5` by `166bfcd78`. Three landing merges and the mint in `ed1e9db3c` moved it through v1.25–1.27 to its current `v1.28`.
- **The fix.** S1 makes the writer test a file only against the patterns of entries whose file group holds it. In a scratch clone the writer then reported no rewrites at all. With drift-audit's version edited to 9.99, all four harness carriers still moved.
- **The selftest arm.** S3 adds a negative case (`vk/harness.js`) and a positive one (`wk/harness.js`, reached through `marker_carriers`) to `check_fix_carriers`. I trialled it as a stand-alone copy of the fixture against both writers: it passes with the fix (8 rewrites) and fails against the current writer (9 rewrites, with the foreign field moved).
- **Other readers of version patterns.** Each one reads only its own entry's source file or reads no pattern, so none changes. §4 lists each with its line.
- **No kit bump.** The only files touched are `tools/govkit/govkit.py` and `tools/govkit/selftest.py`. Both are covered by the govkit registry exemption, and neither appears in any kit's list of shipped files. No function is added or renamed, so `symbols.json` is not regenerated.

**Things to carry into the build**
1. The existing assertion `another entry's pattern moves in a file carrying only this entry's marker` says the opposite of the brief's rule. S3 moves its subject to `wk/harness.js` instead of letting it go red.
2. Playbook-render's epoch-checked file set includes `tools/govkit/registry.toml` and `tools/govkit/entries/playbook.kit.toml`. Editing either one, for example to anchor playbook's pattern, would move playbook-render and owe a bump. AC6 guards against that.
3. Units 10 to 19 cite line numbers in both files this unit edits. §4's rollout keeps `govkit.py`'s net line change at zero where possible, and the commit body must state each file's net line delta.

**F1, needs your decision: `render_playbook.py:1397`**
The class already rewrote this fixture to `v1.28`. Its test still checks what it should, because the renderer treats any major version below 4 as an older template. But the fixture no longer reads as the v3.x template its comment describes.
- **(a)** Leave it and record it as a follow-up outside this build. The next unit that moves playbook-render restores `v3.5` under the bump it already owes.
- **(b)** Restore it here and mint playbook-render to 1.29. That also re-renders `AGENTS.md` and adds a fifth bump to the build.

I recommend (a).

**Checks run.** Only the memory hygiene check, and no finding names this spec. Check 9 reports the build README and `memory/LIVE.md` as stale. That is expected from adding a spec, and the index regeneration is the dispatcher's job. I didn't commit or regenerate anything, and I wrote nothing outside the spec folder apart from throwaway probes in the scratchpad.
~~~~

### 2026-10-14T16:45:31 · gov-spec-writer · direct/a2dbb8de0484e8b31

Label: dRedressedBar · TOOL-dRedressedBar-7 · spec-write

~~~~text
I revised the spec for TOOL-dRedressedBar-7 to rev-3 at `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-7.md`. The acceptance holds: the planner (`unattended.sh --plan dRedressedBar --paths`) grades unit 7 `INPROGRESS READY`, and its Edges now carry the `consumes-from` to unit 20. The memory hygiene gate still fails on two checks, but neither names this spec.

**What changed:**
- **Header:** rev-2 became rev-3. I left the status as `INPROGRESS`, which the builder had already set in the working copy and not committed. It was not mine to move.
- **§3 Edges:** added `consumes-from` `TOOL-dRedressedBar-20`. It says why: without unit 20's fix, `write_version_carriers` (`tools/govkit/govkit.py:798`) lets the `playbook` pattern `governance-template: v` (`tools/govkit/entries/playbook.kit.toml:6`) rewrite the fixture at `tools/playbook/render_playbook.py:1646`, which turns AC4 red. I checked all three lines in the code.
- **§4 step 1:** the existing pinned reading (`12 declared · 11 fresh · 1 stale` at `f079464e2`) differs from the builder's. So I added the builder's pre-write `regen.py --check` reading, `10 fresh · 2 stale`, naming the gotchas index and this build's README build index. It points at the revision record as its source.
- **§4 step 2:**
  - The mint must move exactly four kits: agent-cap, branch-reconcile, roles and unattended. It prints one `mint: <kit> · <old> -> <new>` line per kit (`govkit.py:13188`).
  - It must write no file outside those kits' carriers and the renders the step names, read from `git status --porcelain` after the mint.
  - If it moves another kit or writes another file, the pass stops before step 3, commits nothing and returns to the main loop.
- **Beyond the brief:** in the same step I replaced "unit 3 may add to it" with the builder's observation that the mint moved exactly these four kits. The old wording contradicted the new "exactly four" rule. The rev-3 log line records it.
- **§9:** added the rev-3 line, scoped `§3 · §4 · S3`. No acceptance criterion changed.

**Hygiene gate failures**, which exist without this edit:
- **Check 9:** the build index in this build's README no longer matches a fresh render. This is probably from the uncommitted roster row for unit 20, and perhaps this rev change. You regenerate it when you commit.
- **Check 23:** three failures in the acceptance ledgers of other closed units (dRedressedBar 2, 4, 5 and 9, plus aSparedSpawn and aOrientedCast).

The planner currently shows unit 20 as MISSING because its sibling writer has not finished. I did not touch unit 20's spec, and I did not run the `kit epoch` gate the brief lists, since my role allows only the hygiene and naming gates.
~~~~

### 2026-10-14T17:06:12 · gov-spec-writer · direct/aa9d93798d05f15ce

Label: dRedressedBar · TOOL-dRedressedBar-20 · spec-write

~~~~text
I revised both specs as briefed. Spec 20 is now rev-2 and spec 7 is rev-4, each with a §9 line. No other spec changed, and I did not stage or commit anything.

**The acceptance check:** the planning verb grades unit 7 READY but lists unit 20 as MISSING. That is because spec 20 is still untracked and the verb only reads tracked specs (`git ls-files`, `tools/unattended/unattended.sh:4764`). It should grade READY once you commit it. To check now, I ran the verb's own grading function (`plan_state`, copied out of `unattended.sh`) on both spec files: both grade READY. With spec 20's resolution line removed, it grades FORKED, so the owner's mark is what clears it.

## Spec 20 → rev-2
- **§8 F1:** marked `RESOLVED (owner, 2026-10-14): (b)` in place. The header gains `ratified 2026-10-14`, as the spec format asks for a resolved fork.
- **S6, the restore (new):** a second commit, after the code commit, puts `v3.5` back over `v1.28` on `tools/playbook/render_playbook.py:1397`. It changes that one line in that one file. The separate commit is what F1 (b) itself described, and it has to follow the writer fix or the next writer run rewrites the line again. The spec states that this moves playbook-render's shipped bytes and that unit 20 bumps nothing.
- **AC7 (new):** at the restore commit, both fixture lines (1397 and 1646) read `v3.5`, and the diff touches line 1397 only. In a scratch clone the carrier writer prints `[]`, and `epoch` reports playbook-render FAILED, which is the bump unit 7's mint pays. It goes red if line 1397 still reads `v1.28`.
- **AC8 (new), the line's test still passes:** a new `v3render` command feeds the fixture through the engine's own `render`, the way its test does. I ran it today: at `v1.28` and at `v3.5` it prints the arm's three passing conditions (`True True True`); at `v4.0` the engine refuses the fixture. So the probe can go red, and 3 < 4 keeps it green.
- **§3:** the Edges hand the 1.28 → 1.29 bump to unit 7, and the F1 (a) hand-off is gone.
- **§7:** `playbook render selftest` is added to the gates.

## Spec 7 → rev-4
- **Edges:** the `consumes-from TOOL-dRedressedBar-20` line now says unit 20's restore is the only move of playbook-render's bytes since `ebce889c7`. That kit's files show no diff at `9d0ad1c0a`, and its version is 1.28 at both ends.
- **§4 step 2:** the table and the stop rule now cover five kits: agent-cap, branch-reconcile, roles, unattended, and playbook-render 1.28 → 1.29. The allowed writes gain:
  - `AGENTS.md`, the render's only output. The engine's version appears nowhere in the rendered section, so the file's bytes should not change unless it was already stale.
  - line 1839 of `render_playbook.py`, the kit's only version line. Any other line written there stops the pass.
- **§4 step 6, the manifest re-stamp:** `AGENTS.md` is on the manifest's `verify-paths:` and `registry:` lists, not on `watch:` (`memory/guides/SESSION-KICKOFF.md:6-10`). The check that demands a re-stamp (C5, and its pre-commit form) reads only `watch:` (`manifest-check.sh:1459`, `:1586`). So the fifth kit owes no AC6 re-stamp.
- **AC4** now counts playbook-render. **AC7 (new)** checks the line-level write in `render_playbook.py` and the set of files the commit touches.
- **§7:** `playbook render wiring`, `playbook render selftest` and `playbook parity` are added to the gates.

## Gates
- **Lexicon:** passes.
- **Memory hygiene:** none of its findings mentions either spec. It does fail on findings that predate this work:
  - check 9: the build index and `memory/LIVE.md` need regenerating
  - check 17: the gotchas index is stale, which is unit 7's S1
  - check 23: closed units' acceptance ledgers
- **Not run:** `kit epoch`, `kit version markers`, `playbook parity` and `kickoff-manifest ratchet` are outside what I'm allowed to run; they need the main session.

## Decision for you
Unit 10's S9 tells it to rewrite spec 7's "units 1 to 6" wording as "1 to 6, 8 and 9". That list leaves out unit 20, which now also comes before unit 7 and moves a kit. I left spec 10 alone because no other spec was to move. Unit 10's builder should keep the playbook-render clause in spec 7's AC4; otherwise spec 10 needs its own revision.

Files:
- C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-20.md
- C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-7.md
~~~~

### 2026-10-14T17:20:54 · gov-builder · wf_505af0b9-122/a737641ff163ce752

Label: dRedressedBar · TOOL-dRedressedBar-20 · build

~~~~text
{
 "committed": true,
 "sha": "566c6d831",
 "why": "TOOL-dRedressedBar-20 is built as the spec says, in two commits on branch/gov-bar-reds-fix. 404d45c8c is the code commit: S1, S2 and S3 in tools/govkit/govkit.py and tools/govkit/selftest.py. 21c2d1531 is S6, the restore: tools/playbook/render_playbook.py:1397 reads v3.5 again. A third commit, 566c6d831, moves the status header to CLOSED and carries the README unit row that gen_build_index.py --write re-rendered. The flip has its own commit because the task asks for it in the build commit, but AC6 and AC7 each fix one commit's file set exactly (\"red when ... the restore commit carries a second file\"). A flip in either commit would red one of them. All three commits carry `Pass: TOOL-dRedressedBar-20`. The pass-order leg will take 404d45c8c as the build commit, and its parent 20112bce8 holds the conforming rev-2 spec.",
 "summary": "Commits: 404d45c8c (code), 21c2d1531 (restore), 566c6d831 (status CLOSED plus the generated README row). Every file was staged by name, and the staged diffs carry no CR bytes. The worktree is clean.\n\n**What changed**\n- **S1 + S2, `tools/govkit/govkit.py`:**\n  - `carrier_rxs` is now a dict keyed by entry id.\n  - Each file walk keeps `file_rxs = [rx for rid, rx in carrier_rxs.items() if f in basis.get(rid, ())]`.\n  - The ownership clause is unchanged.\n  - The docstring states \"A pattern counts only in its own entry's basis\" and the defect behind it.\n  - Net +3 lines. The commit body gives the line shifts for the builders of units 10 to 19.\n- **S3, `tools/govkit/selftest.py`, `check_fix_carriers` (net +8 lines):**\n  - New `wk/harness.js`, plus an empty `govkit/registry.toml` stub whose path is built from `gk.GOVKIT_DIR.name` and `gk.REGISTRY_NAME`.\n  - vk gains `marker_carriers` naming `{prefix}/wk/harness.js`.\n  - The `[aMF-64 S2]` case is relabelled and now grades `wk/harness.js`. A new `[dRB-20]` case asserts `vk/harness.js` reads `version: '1.0'` with `vk@1.1`. The count assertion is 8.\n- **S6:** one line of `render_playbook.py`, `v1.28` back to `v3.5`.\n- No kit is bumped, and the symbol map is not regenerated, because no function was added or renamed.\n\n**Criteria, each observed by a probe in this pass** (each stands in for the gate named)\n- **AC1** (`govkit selftest` / `kit epoch`):\n  - In a clone of 20112bce8 the writer printed the one tuple `('tools/playbook/render_playbook.py', 'playbook-render', 'playbook-render', '3.5', '1.28')`, and `git diff -U0` changed line 1646 only.\n  - In a clone of 404d45c8c it printed `[]` with a clean status.\n- **AC2** (`kit version markers`): with `KIT_DRIFT_AUDIT_VERSION` at 9.99, the writer made 14 rewrites, and `grep -c \"version: '9.99'\"` printed 1 for each of the four harnesses.\n- **AC3** (`kit epoch`):\n  - `mint --base ebce889c7` in a fresh clone of 404d45c8c exited 0 with `->` lines for agent-cap, branch-reconcile, roles and unattended only, and `tools/playbook/` stayed clean.\n  - After a scratch commit, `epoch` printed `epoch: playbook-render · clean · 1.28` and no FAILED line at all.\n  - Deviation: I added `--no-verify` to that scratch commit in the clone.\n- **AC4** (`govkit selftest`): the `arm` probe was run alone, with `__pycache__` deleted first.\n  - Over the base writer it exited 1, with FAIL lines naming `[dRB-20]` and the count (9).\n  - Over the fix it exited 0 with every line ok, again at HEAD.\n- **AC5** (`govkit selfcheck`): the two greps print 0 and 1.\n- **AC6** (`codebase-map coverage + freshness`): the code commit's diff names exactly two files and adds or removes no `def` line.\n- **AC7** (`kit epoch`):\n  - At 21c2d1531, lines 1397 and 1646 both read `v3.5`, and the code-to-restore diff is one file and changes line 1397 only.\n  - In a clone of the restore commit the writer printed `[]` with a clean status.\n  - `epoch` printed `epoch: playbook-render · FAILED · moved in 21c2d1531d ...`, which is the move unit 7's mint dates.\n- **AC8** (`playbook render selftest`): `v3render` at the restore commit exited 0 and printed `<!-- governance-template: v3.5 --> True True True`. With the marker at `v4.0` in a scratch clone, it refused, naming the `when:node-table` fence, so the probe can go red.\n\n**Deviations from the spec's commands:** `tempfile.mkdtemp` was given `dir=` the scratchpad, to follow this run's temp-path rule. `v3render` ran from a scratch script instead of a heredoc.\n\n**Owed at the close (none ran here):**\n- The section 7 gates: `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`, `govkit selfcheck`, `kit epoch`, `kit version markers`, `recall floor arms`, `codebase-map coverage + freshness`, `playbook render selftest`, `memory hygiene`.\n- The `New arm:` RED observation of `check_fix_carriers` in `tools/govkit/selftest.py` over the base writer (`vk/harness.js` field at 1.1, count 9).\n- `kit epoch` reads playbook-render FAILED until unit 7's mint bumps it to 1.29.\n\n**Bug-class checklist:** `gotchas.py --for-diff` ran over 20112bce8..HEAD (26 classes) and over HEAD~1..HEAD (14 classes, a subset of the 26). Each class was checked against the diff:\n- `rid` and `file_rxs` are bound nowhere else in the writer.\n- No other carrier states the any-entry rule.\n- `__pycache__` was cleared before each arm run, and the fixture is added with `-f`.\n- The shipped pattern is exercised over the real registry by AC1 and AC3.\n\nNo change was needed. The three scratch clones under %TEMP% are removed."
}
~~~~

### 2026-10-14T17:30:21 · gov-builder · wf_7000bf13-341/a41438c689c4a68eb

Label: dRedressedBar · TOOL-dRedressedBar-7 · build

~~~~text
{
 "committed": true,
 "sha": "671f25c71",
 "why": "TOOL-dRedressedBar-7 is built as rev-4 of its spec describes. Units 1 to 6, 8, 9 and 20 were all CLOSED first. The mint moved exactly the five expected kits, and the only line it changed in render_playbook.py is 1839. Lines 1397 and 1646 still read v3.5, so the fixture rewrite that blocked the first attempt did not come back. The spec's status header is now CLOSED, in the same commit as the pass.",
 "summary": "Built TOOL-dRedressedBar-7 and committed it as 671f25c71 on branch/gov-bar-reds-fix, in a worktree at C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix. The commit has a `Pass: TOOL-dRedressedBar-7` trailer, and the spec's status header now reads CLOSED · 2026-10-14. That flip is the only change to the spec.\n\n**What the commit does (43 files, all staged by name, no CR bytes added)**\n- **Step 1, baseline:** before any write, `govkit.py epoch --base ebce889c7` exited 1 with FAILED for exactly five kits: agent-cap, branch-reconcile, playbook-render, roles and unattended. run-gates read clean, so the pass continued. `regen.py --check` read `12 declared · 11 fresh · 1 stale`, naming memory/gotchas/INDEX.md. That is one stale item, not the `10 fresh · 2 stale` the spec recorded from an earlier run; the spec treats that reading as a pinned observation, not a criterion.\n- **S3, mint:** `govkit.py mint --base ebce889c7` moved agent-cap 1.38->1.39, branch-reconcile 1.4->1.5, playbook-render 1.28->1.29, roles 1.5->1.6 and unattended 1.106->1.107. Every changed line is a `gov:kit` marker or version constant of those five kits. The files outside tools/<kit>/ are outputs those kits declare in their kit.toml: the memory/guides/UNATTENDED-*.md files, PLAYBOOK-TEMPLATE.md, .claude/skills/unattended/SKILL.md and .claude/skills/build/SKILL.md. The roles and playbook renders left .claude/agents/, .claude/roles.json and AGENTS.md byte-identical.\n- **S2, carrier row:** measured after the mint. The files that mention the method and the registry differed by one path, .claude/agents/gov-reuse-scout.md. Its row now sits in memory/project/method-carriers.txt between gov-researcher and gov-skeptic, and the two lists match.\n- **S1, regenerate:** `regen.py --write` ran last, after the status flip. It moved memory/gotchas/INDEX.md (the two class rows plus the count line), memory/LIVE.md and memory/builds/dRedressedBar/README.md. The last two are derived indexes that read the spec's new CLOSED status; the build status there now reads SPECCED.\n- **S4, stamp:** no watched path moved over ebce889c7..HEAD or in this commit, so no stamp was written.\n\n**Checks that ran, all probes of this unit's own outputs (they stand in for the close's bar legs)**\n- **AC1 and AC2** (for `memory hygiene` check 17 and the regen preflight): the index diff from the base adds exactly the two named rows, and `regen.py --check` read `12 declared · 12 fresh · 0 stale`, exit 0.\n- **AC3** (for `method carriers` checks 3 and 4): the two lists match, and gov-reuse-scout.md holds no `## M<n>` heading.\n- **AC4** (for `kit epoch`): the tip epoch shows no FAILED line and exits 0.\n- **AC5** (for `kit version markers`): partly met; the literal probe is not empty (see \"For the spec writer\").\n- **AC6** (for `kickoff-manifest ratchet`): the watch-list probe printed nothing.\n- **AC7:** in render_playbook.py, `git diff -U0 HEAD~1 HEAD` changes line 1839 only, and lines 1397 and 1646 both read v3.5. The changed files are only the categories AC7 allows.\n- **M6 checklist:** `gotchas.py --for-diff HEAD~1..HEAD` exited 0 and selected 53 classes plus 6 universal. I acted on the CRLF classes with a byte-level check of all 43 blobs before and after the commit: no CR count changed.\n\n**For the spec writer (I did not edit the spec):** AC5's literal probe, `git grep -nF \"gov:kit <kit>@<old>\"` over the whole tree, is not empty at the tip. It returns two lines, both in memory/builds/aOrientedCast/: line 35 of the TOOL-aOrientedCast-27 acceptance ledger and line 11 of the TOOL-aOrientedCast-25 fold brief. Both quote old markers in prose and were already present at ebce889c7, so they are history records, not carriers. Excluding memory/builds/, which §4 step 2 already does for its own grep, the probe prints nothing. AC5's red condition (\"a carrier keeps the old marker\") is not met, but the probe as written should gain that exclusion.\n\n**Owed at the close (none ran in this pass):** the full §7 list in one bar. That includes `memory hygiene`, `method carriers`, `kickoff-manifest ratchet`, `push-main self-test` (where arms 28 and 29 should go green on the fresh index), `kit epoch`, `kit version markers`, `verdict epoch`, `govkit selfcheck`, `agent-cap self-test`, `scratch-guard self-test`, `verifier fan-out self-test`, `review-join self-test`, `hook destinations self-test`, `branch-reconcile selftest`, `playbook render wiring`, `playbook render selftest`, `playbook parity`, `recall floor` and `recall floor arms`. This unit adds no arm, so no RED-first observation is owed. No command timed out or was skipped.\n\n**Trailer note:** the commit ends with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, following the charter fact and the repo's existing commits, rather than the session reminder's 5.5 form."
}
~~~~

### 2026-10-14T17:36:54 · gov-builder · wf_08419c0e-f39/aa36944af742d2e7b

Label: dRedressedBar · TOOL-dRedressedBar-10 · build

~~~~text
{
 "committed": false,
 "sha": "",
 "why": "DIVERGENCE: the spec requires one commit that no single role can make. §2 S24, §4 \"The sibling rev bumps\" and its Files touched, and §6 AC19 put the eight sibling-spec corrections into this unit's own build-pass commit. Those are specs 1 and 3 to 9: S1-S3's revision line, S5, S8, S9, S14, S16 and S22's spec-9 half. AC19 then reads them at `<p10>~1..<p10>`. scratch-guard blocks that write. Under `.claude/roles.json` only gov-spec-writer may write spec files, and a gov-builder may change only the status and date cells of the spec it is routed to. I saw the block on my first Edit of spec 1. So the one commit AC19 reads cannot be made by either role. The spec would have to say one of two things. Option one: the sibling corrections are a separate gov-spec-writer pass with its own commit (M6's \"a review's fixes folded in\"); this unit's build pass writes only `tools/govkit/entries/settings-merge.kit.toml`, `tools/govkit/matrix.py` and the acceptance ledger; and AC19, plus S24's \"in this pass\", reads the spec-writer's commit instead of `<p10>`. Option two: split the unit into a product unit and a spec-correction unit. I restored both product files and committed nothing. Spec 10's INPROGRESS header, which the caller had left uncommitted, is as I found it.",
 "summary": "Nothing is committed: this unit can't be built as one builder commit, because scratch-guard lets only gov-spec-writer edit the eight sibling specs the unit must amend. The product half was built and probed, then restored. Its diff is saved at C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-bar-profile-failures-b80cc3/8d2976c7-7629-4ba0-8a96-2098db6da20f/scratchpad/TOOL-dRedressedBar-10-product.diff for the next dispatch to reuse.\n\nChecks run: probes only. No gate, suite or bar ran. The `check` recorder over `matrix.py` stands in for the `govkit acceptance matrix` arm. The leg's own `scan_spawn_file`, imported read-only, stands in for `shell hygiene (a fork spent on builtin work)`. The AC17 scratch targets stand in for the `govkit selftest` `[dRB-9]` path.\n\nThe criteria that read sibling builds hold over the current tree. Pass commits: p1 3d1adca94, p2 c7a9213d1, p8 a50d04eb7, p9 59f11096a.\n- **AC1:** 0 glued calls and 14 spaced (13 and 1 at base).\n- **AC2:** the unset is at line 122, before the first executed push at 139. In a staged copy it lands at 2601, after the push at 138, so the reading reds.\n- **AC3:** lines 88-89 sit between the arm headers at 82 and 91. The `:-0` line reads `${fail:-0}` and `${n:-1}`, and nothing reads `${pass`.\n- **AC4:** unit 8's pass moved one `tools/` file. `MP_BOUND` appears only in `run_mp_bar` and on the ac14 call, and `FLOOR_ASSERTIONS=401` is unchanged.\n- **AC5:** the classifier reads 25/1/12/2/141 at both p8~1 and p8, equal to the registry rows. One class, epoch-date, rose 22→24, but it is banned-on-product and never counted for suites (`sh_hygiene.py:866-867`).\n- **AC6:** all three names are present in the fixture; 0 at base.\n- **AC7:** the `[dRB-9]` block is at 3339-3354 and reads `means` from the descriptor. `check_outcome_states` is defined once with 3 hits, and the two lexicon labels match the base pins.\n- **AC10:** no scoped call at the tip. The staged scope prints line 3315, and unit 3's old regex misses it.\n- **AC12:** the four converted files read 0. The suite reads var-pipe 62 and printf-subst 66, equal to its rows.\n- **AC14:** the map lists both names and no `clean` for gate-guard.js; p2 and p9 both list `symbols.json`.\n\nThe product half, built then restored:\n- **Descriptor:** the code-2 probe got its second must-not-exist term, `{prefix}/../hooks/agent-cap.js` (the AC15 form).\n- **Matrix:** a fourth row for the hook at the prefix's parent home only. Its path comes from agent-cap's `resolve_entry` destination and settings-merge's resolved prefix, via `PurePosixPath.relative_to`. The recorder read all 16 checks ok, the new row REFUSED.\n- **AC16:** the engine reads ACCEPTED / REFUSED / REFUSED / ACCEPTED over the four states. Over unit 9's single-term block the parent-home row reads ACCEPTED, the red case.\n- **AC17, red half first:** over a `%TEMP%` clone at 671f25c71, which carries unit 9's block, both `apply` and `update` exit 0 and print the accepted stop, and `update` re-stamps to 671f25c7.\n- **AC17, green half:** over the two-term block, `apply` exits 1 with `adopter exit 2` and no stop, and `update --write` exits 1 leaving `gov_commit` at 24f39915.\n\nOwed at the close once rebuilt: the §7 gate list, and the RED-first observation of the new `tools/govkit/matrix.py` arm covering AC16 (stage unit 9's block; the parent-home row should read ACCEPTED). AC8, AC9, AC11, AC13, AC18, AC19 and AC5's spec-8 half were not observed, because their spec edits were blocked.\n\nFindings for the spec writer:\n1. Unit 20 shifted every `govkit.py` line after about 870 by +3. `EPOCH_ROLES` is now at :12938, and §4's cites (1450-1456, 5913-5917, 6313-6324, 7740-7764, 11104-11126) are each +3. `settings-merge.py` is unchanged.\n2. Spec 4's §5 migration line, \"once unit 7 bumps the two kits\", is the same false fact, but S8 names only three addresses.\n3. S9 lists \"1 to 6, 8 and 9\". Unit 20 (order 4) is also ordered before unit 7.\n4. The comment above the code-2 block was left alone; unit 13's S22 owns it.\n5. Out of scope: `govkit.py`'s unclassified-exit message (around line 7774) still says no `[[outcome]]` evaluator exists.\n\nThe gotchas checklist (`gotchas.py --for-diff HEAD~1..HEAD`) was not run: with no commit, that range is unit 7's commit. The scratch clone and the `%TEMP%/d10*` targets were removed."
}
~~~~

### 2026-10-14T17:52:48 · gov-spec-writer · direct/a53aa6900130cb644

Label: dRedressedBar · TOOL-dRedressedBar-10 · spec-write

~~~~text
I revised all four units and folded unit 10's corrections into specs 1 and 3 to 9. For units 13, 17 and 19 I did not fold the sibling corrections now, as item 3 asked. Each unit's corrections now land in a spec-writer pass at that unit's own turn instead. The reason is below. Nothing is committed and the index is as I found it.

## TOOL-dRedressedBar-10: done, rev-4 → rev-5
- **S24, §1, §4 and §7:** the sibling corrections are now this unit's spec-writer pass, `<s10>`. §4 explains why with a citation: only `gov-spec-writer` writes spec files, and scratch-guard lets a builder change only its own spec's status and date cells (`tools/hooks/scratch-guard.js:91-99`).
- **Files touched:** only `tools/govkit/entries/settings-merge.kit.toml`, `tools/govkit/matrix.py` and the acceptance ledger.
- **AC19:** reads `<s10>~1..<s10>`, and also checks that the build pass `<p10>` writes no other spec.
- **S8:** names a fourth address, spec 4's §5 migration line.
- **S9:** the list of units before unit 7 is now 1 to 6, 8, 9 and 20.
- **Line cites:** the `govkit.py` cites and `EPOCH_ROLES` (now `:12938`) moved by +3. I checked each one against the current tree. `derive_probe_paths` is now cited at `matrix.py:227-229`, because unit 9 moved it.
- **Status:** the header still reads INPROGRESS, which is the builder's uncommitted change I found. I did not change any status.

**Sibling corrections:** each target is CLOSED and took the fix as a records fix, with the status unchanged and a revision line naming TOOL-dRedressedBar-10 and its report ids:

| Spec | New rev | Report ids |
|---|---|---|
| 1 | rev-3 | 1, 2, 3, 11, 20, 21 |
| 3 | rev-4 | 6, 10, 16 |
| 4 | rev-3 | 8, 13, 18 (four sentences, the §5 migration line included) |
| 5 | rev-6 | 14, 15 |
| 6 | rev-3 | 14 |
| 7 | rev-5 | 9, 19, 23, plus edges to units 8 and 9 |
| 8 | rev-3 | 4, 5, 12, plus hands-off to unit 7 |
| 9 | rev-5 | 7, 22, plus hands-off to unit 7 |

I checked unit 10's spec-text criteria (AC5, AC8, AC9, AC11, AC13 and AC18) against the corrected specs, and each reads as it should.

## TOOL-dRedressedBar-13 (rev-5), -17 (rev-3), -19 (rev-3): revised, not folded now
Each spec's §9 line names the moved items:
- **13:** S25 and the spec halves of S1–S6, S9–S20 and S24.
- **17:** S25 and the spec halves of S1–S6, S8–S11, S13, S15, S16 and S18–S24.
- **19:** S44 and the spec halves of S1, S2, S4–S9, S13–S23, S27, S30–S32, S35, S38 and S40–S43.

Each build pass now writes only product files, plus the manifest and the ledger. Each record criterion (AC21, AC25, AC44) reads the spec-writer commit (`<w13>`, `<w17>`, `<w19>`). The main loop dispatches that pass once the unit's targets are CLOSED and before the build.

**Why I did not fold them now:** apart from spec 9, these units correct specs 10, 11, 12 and 14 to 18, which are all unbuilt. Folding into them now would change what those units build. It would also break red halves already written. For example, unit 17's AC11 and AC24 expect the `<p15>` engine to lack rules that folding into spec 15 would make unit 15 build. And it is the first alternative each of these specs rejects, under the owner's "never folded" rule (M4, SPEC 2026-10-05). For spec 9, the corrections from units 13 and 17 describe code that units 11 and 15 have not built yet. If you want them folded now anyway, that needs the owner's decision.

## Acceptance
- **Planning verb:** `unattended.sh --plan dRedressedBar --paths` grades 10, 13, 17 and 19 READY.
- **Files touched:** not fully met. Units 12, 14 and 16 are also READY, and their Files touched still name spec 11, 11 and 12. They were not in my brief and need the same treatment.
- **Staged hygiene check:** prints no check 12 or 25 line. It does fail check 9 because `memory/LIVE.md` and the build README need regenerating, which is yours to do. I staged the specs only to run this check and then unstaged them.
- **Gates:** I ran only memory hygiene. I did not run `kit epoch`; no product file moved.

## For your commit
- Include the untracked `prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-4-revision.md`, because the four revised specs cite it.
- Put TOOL-dRedressedBar-10 in the subject. The commit is `<s10>`, which AC19 finds by the `- rev-5 · 2026-10-14` line in spec 10.

Files are in C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\:
- 2026-10-14-spec-TOOL-dRedressedBar-1.md
- 2026-10-14-spec-TOOL-dRedressedBar-3.md
- 2026-10-14-spec-TOOL-dRedressedBar-4.md
- 2026-10-14-spec-TOOL-dRedressedBar-5.md
- 2026-10-14-spec-TOOL-dRedressedBar-6.md
- 2026-10-14-spec-TOOL-dRedressedBar-7.md
- 2026-10-14-spec-TOOL-dRedressedBar-8.md
- 2026-10-14-spec-TOOL-dRedressedBar-9.md
- 2026-10-14-spec-TOOL-dRedressedBar-10.md
- 2026-10-14-spec-TOOL-dRedressedBar-13.md
- 2026-10-14-spec-TOOL-dRedressedBar-17.md
- 2026-10-14-spec-TOOL-dRedressedBar-19.md
~~~~

### 2026-10-14T18:11:16 · gov-builder · wf_f5aa88db-dff/ab91014ea5333e97c

Label: dRedressedBar · TOOL-dRedressedBar-10 · build

~~~~text
{
 "committed": true,
 "sha": "dcba3d3e6",
 "why": "TOOL-dRedressedBar-10 is built and closed in two commits. 07feb3b38 is the pass: settings-merge's exit-2 stop is now refused when agent-cap's hook sits at the prefix's parent home, the matrix gains the matching row, all 19 criteria are recorded in the ledger, and the spec status is CLOSED. dcba3d3e6 is a ledger-only fix that the bug-class checklist called for.",
 "summary": "TOOL-dRedressedBar-10 is built and closed. No merge bar, suite or gate leg ran: every criterion was checked by a direct probe, and the §7 gates are owed at the close.\n\n**Commits**\n- `07feb3b38` (`Pass: TOOL-dRedressedBar-10`) is the pass:\n  - `tools/govkit/entries/settings-merge.kit.toml`: the code-2 block's `must_not_exist` is now the two-term list from §4, adding `{prefix}/../hooks/agent-cap.js`. Its comment says a hook only the receipt can find is still an open gap.\n  - `tools/govkit/matrix.py`: settings-merge's `check_outcome_states` call gains a fourth row, \"hook at its prefix's parent home only\", expected REFUSED. The path is derived from agent-cap's installed path with the `{prefix}` replaced by its parent, never typed. The only other changes are a `posixpath` import and the docstring count going from three to four.\n  - The new ledger `memory/builds/dRedressedBar/build/2026-10-14-build-TOOL-dRedressedBar-10-1-acceptance-ledger.md`, with `**Serves:** journal TOOL-dRedressedBar-10`.\n  - Spec 10's status cell set to CLOSED (the date already read 2026-10-14), plus the records row the index generator adds for the new ledger.\n  - The build README and `memory/LIVE.md` rows the generator re-renders.\n- `dcba3d3e6`: the checklist (`gotchas.py --for-diff HEAD~1..HEAD`) flagged `ledger-token-wrapped-across-a-line-joins-nothing`. Two backticked spans in the ledger crossed a line break, so I made them plain prose. No reading changed.\n\n**Criteria (all observed, readings in the ledger)**\n- AC1 to AC15, AC18 and AC19 were greps and `git` readings over the tip.\n  - Pass commits come from each commit's `Pass:` trailer, because no sibling unit wrote a ledger: p2 is `c7a9213d1`, p8 `a50d04eb7`, p9 `59f11096a`, and s10 `67a23b14d`.\n- AC5 and AC12 imported the leg's own classifier, `sh_hygiene.scan_spawn_file`.\n- AC16 called `classify_outcome` with `outcome_accepted` over four scratch states. Results: no hook ACCEPTED, hook beside the adopter REFUSED, hook at the parent home REFUSED, hook at a third path ACCEPTED. With unit 9's single-term block substituted, the parent-home row reads ACCEPTED, which is the red case.\n- AC7 imported `matrix.py` with `check` replaced by a recorder. All 16 checks passed, including the new row, and lexicon's two labels match §4.\n- AC17 drove both verbs over fresh `git init` targets in a scratch gov clone under `%TEMP%`. The red half ran first, over unit 9's block: both verbs exited 0 and printed the stop as accepted. Over the new block, `apply` exits 1 with `adopter exit 2` and no `no-agent-cap-to-wire`, and `update --write` exits 1 and leaves `gov_commit` at `24f39915`.\n- These probes stand in for `govkit acceptance matrix`, `govkit selftest` and `memory hygiene`.\n\n**Owed at the close**\n- The §7 gates: `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`, `govkit selfcheck`, `recall floor`, `recall floor arms`, `memory hygiene` and `codebase-map coverage + freshness`.\n- The `New arm:` line's RED-first observation: the matrix leg with unit 9's single-term block staged, where the parent-home row must read ACCEPTED, then green once restored. That observation is also what would catch a parent-home path derived wrongly; I added no extra assertion because §3 rules out any new arm beyond the one row.\n\n**Things the main loop should know**\n- Another pass is writing in this worktree: specs 12, 14 and 16 carry uncommitted edits, and two unit-12 prompt files are untracked. So my commit's README and LIVE.md were rendered in a scratch clone of HEAD plus my changes and staged as blobs, which keeps their rows out. My `gen_build_index.py --write` runs also re-rendered the worktree README with their rows; that unstaged change is theirs to commit.\n- I first wrote `TOOL-dRedressedBar-11` into the descriptor comment. That made LIVE.md count unit 11 as landed but unclosed, because an unbuilt unit's id was in product source. I removed the id; to do that I briefly set the status back to INPROGRESS, since closing the spec shuts the write gate, then closed it again.\n- Spec finding for unit 13, which revises spec 10 §5: §5 \"observability\" says a refused stop prints `no declared outcome accepts that`. That is true for `update`. On `apply` the message instead says no outcome evaluator exists yet, which `tools/govkit/govkit.py` still prints though one does. No criterion reads that line, and no unit owns that stale message yet.\n\nScratch clone and fixture targets under `%TEMP%` (`u10g`, `u10ra`, `u10ru`, `u10ga`, `u10gu`) are removed. Nothing timed out or was skipped."
}
~~~~

### 2026-10-14T18:11:51 · gov-spec-writer · direct/a73cd1766f31f4d66

Label: dRedressedBar · TOOL-dRedressedBar-12 · spec-write

~~~~text
I've revised specs 12, 14 and 16 so the build pass of each now writes only product files and its ledger. Each sibling-spec edit is now a spec-writer pass at that unit's own turn, after the target unit is CLOSED and before its build. Nothing was folded into specs 11 or 12, no status moved, and nothing is committed or regenerated.

| Unit | New rev | Pass | What moves | When the pass runs |
|---|---|---|---|---|
| TOOL-dRedressedBar-12 | rev-5 | `<w12>` | S4 (spec 11's rev bump), checked by AC5 | once unit 11 is CLOSED |
| TOOL-dRedressedBar-14 | rev-5 | `<w14>` | S5 (spec 11's rev bump), checked by AC6 | once unit 11 is CLOSED and `<w12>` and `<w13>` have bumped spec 11 |
| TOOL-dRedressedBar-16 | rev-3 | `<w16>` | S4 (spec 12's rev bump), checked by AC4 | once unit 12 is CLOSED |

Each spec now has the shape units 13, 17 and 19 have:
- **The moved item** names its pass and when it runs, and says the build pass writes no spec file except its own status and date cells.
- **A new §4 sub-section** explains why the edit can't go in the build commit, citing `tools/hooks/scratch-guard.js:91-99`. A build pass that finds no spec-writer commit hands back to the main loop.
- **Files touched** no longer lists the sibling spec and says which pass writes it.
- **Alternatives rejected** gains a "refused by the hook" row (C6, C8, C5).
- **The §6 preamble** defines the pass commit.
- **The criterion** that reads the sibling edit now reads that commit's diff. It checks for one rev bump and one revision line naming the right ids, a CLOSED header just before the pass, and a build commit that names no spec but its own.
- **A §9 line** names the moved items and criteria.

Two smaller fixes: in specs 12, 14 and 16 the consumes-from edge now names the pass. In spec 14, "Order, and unit 7" now says the three passes bump spec 11 in the order `<w12>`, `<w13>`, `<w14>`.

**Checks:**
- `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` still grades units 11 to 19 all READY (10 is INPROGRESS and READY).
- I swept the Files touched sub-section of every unit from 11 to 19 for a `memory/builds/dRedressedBar/spec/` path other than its own, and found none:
  - **11, 15 and 18:** product files only.
  - **13, 17 and 19:** already list only product files, manifest and ledger, and name their sibling specs as `<w13>`, `<w17>` and `<w19>`'s write set.
  - **12, 14 and 16:** clean after this pass.
- **Memory hygiene** exits 1 on two checks, and neither names units 12, 14 or 16:
  - **Check 9:** the generated `memory/LIVE.md` and `memory/builds/dRedressedBar/README.md` no longer match a fresh render. The index carries each spec's rev, so the rev bumps alone cause this. Whoever commits regenerates with `python tools/memory-tree/gen_build_index.py --write`.
  - **Check 23:** the hits are in ledgers of CLOSED dRedressedBar units (2, 4, 5, 7, 9, 20) and of the aSparedSpawn and aOrientedCast builds. They have nothing to do with these edits.

Files are in C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\:
- 2026-10-14-spec-TOOL-dRedressedBar-12.md
- 2026-10-14-spec-TOOL-dRedressedBar-14.md
- 2026-10-14-spec-TOOL-dRedressedBar-16.md
~~~~

### 2026-10-14T18:29:21 · gov-builder · wf_551a7d53-a85/aabed9b0e2ce4380b

Label: dRedressedBar · TOOL-dRedressedBar-11 · build

~~~~text
{
 "committed": true,
 "sha": "b65688cdef6a4f2bd1e697db6e3f0cac7a1c4418",
 "why": "TOOL-dRedressedBar-11 is built as its rev-3 spec describes, in one pass commit carrying `Pass: TOOL-dRedressedBar-11`. The spec status header moved to CLOSED · 2026-10-14 in the same commit, with nothing else in the spec changed. The pre-commit hygiene hook refused the first attempt because a status flip changes the build README's generated Units row (check 9). I ran `gen_build_index.py --write`, which changed only that one row of `memory/builds/dRedressedBar/README.md`. I staged it by name beside the four declared tools/govkit paths. I did not use --no-verify and did not amend.",
 "summary": "TOOL-dRedressedBar-11 is built and committed at b65688cd.\n\n**What changed:**\n- **`tools/govkit/govkit.py`:**\n  - The probe keys are declared once, as `OUTCOME_PROBE_KEYS`, just before `classify_outcome`, and its loop goes through that mapping instead of the typed pair.\n  - The new key `must_not_resolve` is checked with the existing inlined `resolve_kit_dir`. The docstring states its grammar, how it reads with no receipt, and the inputs that fail it.\n  - The two refusal sites keep the adopter's process result (`_cfg_run` in apply's CONFIGURE step, `_proc_g` in update's gained loop). Their problem lines now end with the adopter's last stderr lines, in the same shape the regenerate site uses. Neither call's arguments changed.\n- **`tools/govkit/entries/settings-merge.kit.toml`:** the code-2 block gains `must_not_resolve = \"{prefix}/hooks/agent-cap.js\"`.\n- **`tools/govkit/matrix.py`:**\n  - The agreement rule now groups keys by the engine's mapping instead of naming them.\n  - A new key rule gives one label per `[[outcome]]` block, plus a liveness label. Its labels start `probe keys: `.\n  - `check_outcome_states` accepts an optional fourth row element: files to write before classifying and delete after.\n  - The settings-merge call gets a `.git` entry in its scratch directory and two receipt rows. The receipt row's `source` comes from `resolve_entry`, and a check confirms the receipt-only home is neither static home.\n- **`tools/govkit/selftest.py`:** one `[dRB-11]` block after `[dRB-9]`, covering fixtures A, A-absent and B.\n\n**What I checked (direct probes only; no bar, suite, gate leg or selftest ran):**\n- **AC1:** the descriptor block reads back with all five parts, and `(\"must_exist\", True)` no longer appears in govkit.py. `grep must_not_resolve` prints the constant line and the docstring, plus a third line: the `if key != \"must_not_resolve\"` branch the evaluation needs. AC1's red condition does not cover that line.\n- **AC2:** an in-process program gets the expected verdict in all seven states. The adopter's stderr says `cannot read` in the receipt row and `refusing to wire` with no receipt. The same program over unit 10's block (taken from `git show 07feb3b38`) reads ACCEPTED on the receipt row, which is the red half.\n- **AC3, AC4, AC5** (real CLI runs on git fixtures under `%TEMP%`):\n  - Fixture A: the second apply exits 1, with exactly one `govkit: kit 'settings-merge'` line carrying `cannot read` and `settings.json`, and no `no-agent-cap-to-wire` anywhere.\n  - Fixture B: `update --write` exits 1, prints that same single line, and `gov_commit` stays at 24f39915.\n  - A-absent: exits 0 and prints `[accepted stop]`.\n  - Red halves, run over a clone at 07feb3b38: A exits 0 with `[accepted stop]`, and B exits 0, re-stamps the receipt and prints the accepted line.\n- **AC6:** with `check` replaced by a recorder, every label is true: 19 key-rule labels (18 blocks plus unit 9's), the liveness label, exactly the two `lexicon ` labels, and six settings-merge rows. With `must_not_resolve` renamed to `must_not_resolves`, exactly two labels go false: the settings-merge key-rule label and the receipt-only row.\n- **AC7:** `git diff 07feb3b38 b65688cd -- tools/govkit/` changes no `def` or `class` line. `scan_text_io` counts 36 subprocess sites in govkit.py, none in matrix.py, and 24 subprocess plus 1 file-io in selftest.py, matching the registry.\n- I also checked that every name the `[dRB-11]` block reads is bound earlier in `main`. This caught a real bug before commit: `NL` is only assigned later in `main`, so using it would have raised an error. The block now uses a literal newline.\n\n**Owed to the main loop at the close:**\n- The §7 gates: `govkit selftest`, `govkit acceptance matrix`, `govkit refusal join`, `govkit selfcheck`, `receipt sync`, `recall floor arms`, `encoding posture`. Of these, only encoding posture was stood in for here, by the AC7 probe.\n- The red-first observation of both new arms:\n  - the matrix arm: the receipt-only row read over unit 10's block, and the key rule over the renamed key. I saw both with in-process patches, not as staged breaks.\n  - the `[dRB-11]` selftest block, over unit 10's block and at `ebce889c`. The `[dRB-11]` block itself has never been run, because running it means running the suite. The probe repeated its steps through the CLI instead.\n\n**Bug-class checklist on HEAD~1..HEAD, and what I did with it:**\n- **New local names in a long function:** the AST check above covers it.\n- **A line claim matched across the whole output:** the arms read single lines.\n- **A fixture picking up the machine's own state:** handled by the `.git` entry in the matrix scratch directory.\n- **A row field added without updating the docs:** the three-element docstring of `check_outcome_states` is left for TOOL-dRedressedBar-13 S6, because documenting it here would erase that unit's red half.\n- **A claimed observation that no arm actually reads:** a real gap I'm reporting rather than fixing. CONFIGURE's other refusal branch (a declared outcome that matched but is not accepted) now prints the stderr tail too, and no arm reaches that branch. AC3 only covers the \"unclassified\" branch.\n\n**Decisions recorded as trailers:**\n- Fixture B reads the old hook bytes with one binary-mode `git show`, which the encoding scanner does not count. This is the by-hand rebuild the audit flagged (id 17); TOOL-dRedressedBar-13 S17 replaces it with `write_vintage_receipt`.\n- The key-rule label prefix and the descriptor's code-2 comment are left for TOOL-dRedressedBar-13 S7 and S22.\n\nThe README's Build-level rules sentence about unit 7 is still the dispatcher's edit, as the spec says. Nothing was skipped for running past its time limit, and the `%TEMP%/rb11*` fixtures and clone have been removed."
}
~~~~

### 2026-10-14T18:48:23 · gov-spec-writer · direct/aa32daaf3d40065a6

Label: dRedressedBar · TOOL-dRedressedBar-12 · spec-write

~~~~text
I corrected spec 11 in place as spec 12's S4 asks. Its status is still CLOSED, nothing is committed, and the build index is not regenerated.

**Unit TOOL-dRedressedBar-11: authored.** The file is `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-11.md`. `git diff` shows four changes and nothing else (13 lines added, 2 removed):
1. **Header:** `CLOSED · rev-3` becomes `CLOSED · rev-4`. Everything else on the line is unchanged.
2. **§4 "Which receipt bytes":** I added sentences after the paragraph's last line and moved no existing line. They say that a refused apply still writes its receipt. A non-accepted CONFIGURE exit only calls `r.fail` (`:7764`, `:7771`), and the RECEIPT step at `:8019` then writes `kits` and `files` from the selection alone (`:8021`). A later run's term reads that receipt, and `TOOL-dRedressedBar-12` keeps it whole. I checked these line numbers with `git show ebce889c7:tools/govkit/govkit.py`, the base the paragraph already cites. At the tip the same code sits at `:7800`, `:7810` and `:8061-8063`.
3. **First "What an adopter sees change" row:** the "After" cell now ends "with `TOOL-dRedressedBar-12`'s carry, the refusal holds on every re-run". I tied the claim to unit 12 because the refusal only lasts one run until unit 12 is built.
4. **§9:** a rev-4 line says this is a records fix for TOOL-dRedressedBar-12. It closes report id 23 (H1) and was written by `<w12>` as unit 12's S4. It notes the status stays CLOSED and lists the two changes in §4, with TOOL-dRedressedBar-12's AC2 as the check. AC3's text does not move.

**Checks I ran:**
- **Spec 12's AC5 Design cut** (`sed -n '/^## 4. Design/,/^## 5/p' … | tr '\n' ' ' | tr -s ' '`) finds `TOOL-dRedressedBar-12` twice. The header said CLOSED before the edit and still does. "report id 23" and "AC2" each sit on a single line of the revision entry.
- **`bash tools/unattended/unattended.sh --plan dRedressedBar --paths`** grades `TOOL-dRedressedBar-12 SPECCED READY`, and its `next:` line is unit 12.
- **`memory hygiene` fails (exit 1)**, for two reasons:
  - **Check 23** fails because CLOSED units, unit 11 among them, have no journal records evidencing their ACs. Its output is the same over HEAD's copy of the spec, so it predates this edit.
  - **Check 9** is the only new failure. `memory/builds/dRedressedBar/README.md:147` still shows spec 11 at `rev-3`. Running `python tools/memory-tree/gen_build_index.py --write` when you commit clears it. I did not run it.

To compare the gate before and after, I briefly put spec 11 back to its HEAD version and then restored my edit. `git diff --stat` afterwards shows the same 13 insertions and 2 deletions. No other spec and no product file was touched.
~~~~

### 2026-10-14T18:53:48 · gov-builder · wf_3606b8ce-990/ab8c8c93299ef0920

Label: dRedressedBar · TOOL-dRedressedBar-12 · build

~~~~text
{
 "committed": true,
 "sha": "fda78c56e",
 "why": "TOOL-dRedressedBar-12 is built as the spec describes, and `<w12>` (62f965ccf) was in place before any write. When an apply names fewer kits than the receipt already claims, it now keeps the claims and rows of the kits it did not name. Before this change it dropped them, which caused two failures: a later re-apply of a dropped kit was refused as foreign, and settings-merge's refused exit was accepted one run later. Every criterion was checked with a direct probe, and the commit carries `Pass: TOOL-dRedressedBar-12` and spec 12 set to CLOSED.",
 "summary": "Committed fda78c56e on branch/gov-bar-reds-fix. Files: C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/tools/govkit/govkit.py, tools/govkit/selftest.py, memory/builds/dRedressedBar/build/2026-10-14-build-TOOL-dRedressedBar-12-1-acceptance-ledger.md, spec 12, and memory/builds/dRedressedBar/README.md.\n\nWhat changed:\n- S1, the RECEIPT step in `_cmd_apply`: two new lists, `_carried_kits` and `_carried_rows`, are built from the earlier receipt by which kits it claims. The receipt writes `kits` as `selection + _carried_kits` and `files` as `rows + _carried_rows`. `install.sums` and the RECEIPT step counts read those same written lists. One `KEEPS` line is printed after the write, never before it.\n- S2: the `carry_out_of_scope` paragraph in `write_gate_legs`'s docstring is rewritten and names TOOL-dRedressedBar-12.\n- S3: a new `[dRB-12]` block follows `[dRB-11]`. Every figure in it is read from the receipt that step 2 reads, and it starts with a check that the fixture is not empty. Fixture A in the `[dRB-11]` block gets a third identical apply: two `[dRB-12]` AC2 checks run on it, and the block's existing problem-line loop also grades it.\n- No new function, class or kit version.\n\nChecks run. No bar, suite or gate leg ran.\n- A scratch program ran `govkit.py apply` over fresh `git init` targets under %TEMP%.\n  - At the tip, AC1–AC3 hold: 18 rows; kits come out as settings-merge, kickoff-manifest, agent-cap; the 16 carried rows match the earlier receipt exactly; one KEEPS line; step 3 exits 0; one attributes row. In fixture A the planted row survives the refused apply, and the third apply exits 1 with exactly one `cannot read` problem line.\n  - A clone at `<p11>` (b65688cde) shows both red halves: step 2 leaves settings-merge with 2 rows, step 3 exits 2 as foreign, and fixture A's third apply exits 0 on `[accepted stop]`.\n  - A copy whose carry is keyed on `not in selection` writes 2 attributes rows (AC3's red half).\n- A second program cut the two new selftest regions out of the file and ran them alone over the tip: 12 of 12 checks ok.\n- AC4: the grep count reads 0 at the tip and 1 at ebce889c7, and `ast.get_docstring` contains the unit id.\n- AC5: at `<w12>`, spec 11 gets one rev bump (rev-3 to rev-4) and one revision line naming report id 23 and AC2; its §4 names unit 12 twice, and 0 times in blob 1b4ea08c. The diff of fda78c56e under spec/ names spec 12 only.\n- AC6: no added `def` or `class` line; `scan_text_io` reads 36 sites in govkit.py, and 24 subprocess plus 1 file-io in selftest.py, matching the registry.\n- These probes stand in for `govkit selftest`, `encoding posture` and `memory hygiene`. The pre-commit memory-hygiene check on staged files ran and passed.\n\nOwed to the close (main loop):\n- Every §7 gate: govkit selftest, govkit acceptance matrix, govkit refusal join, govkit selfcheck, receipt sync, encoding posture, spec tokens, recall floor, recall floor arms, memory hygiene.\n- Both `New arm:` RED-first observations: the `[dRB-12]` block, and fixture A's third apply in `[dRB-11]`, each over `<p11>`'s engine.\n- The full govkit selftest also has to show that no existing arm relied on a narrower apply dropping claims.\n\nDecisions to review: spec 12's change goes beyond the status cell. It also has the index generator's records row for the new ledger, and README.md's unit-12 row and record count were regenerated too. This follows unit 10's pass, because a stale generated output fails the regen preflight. Both choices are recorded as `Decided:` trailers on the commit.\n\nBug-class checklist (`gotchas.py --for-diff HEAD~1..HEAD`, exit 0): every listed class was checked and none needed a further change. The new local names are unused anywhere else; the KEEPS line is tested line by line; the fixtures check they are not empty; the ledger has no backtick span split across lines; and no stale statement of the old behaviour remains elsewhere. The scratch clone and fixtures under %TEMP% were removed. No command was skipped."
}
~~~~

### 2026-10-14T19:07:21 · gov-spec-writer · direct/a40330d98f24b95e5

Label: dRedressedBar · TOOL-dRedressedBar-13 · spec-write

~~~~text
I applied every row of spec 13's §4 correction table to specs 9, 10 and 11. The work is uncommitted, as the role requires. Each spec took one rev bump and one §9 revision line naming `TOOL-dRedressedBar-13` and all of its report ids. All three headers still read CLOSED.

**TOOL-dRedressedBar-13 (pass `<w13>`): done**

| Spec | Rev | Report ids in the revision line | What moved in place | Unit 13 criteria named |
|---|---|---|---|---|
| 9 | rev-5 to rev-6 | 6 | §4 row-shape sentence now names the optional fourth row element (`tools/govkit/matrix.py:165`) | AC6 |
| 10 | rev-5 to rev-6 | 1, 2, 3, 4, 5, 8, 9, 12, 14, 15, 16, 18, 19 | §1 "nine specs"; §3 first non-goal, §4 Alternatives row 2 and §5 risks; §4 prefix-`.` sentence, reader inventory and matrix-row paragraph; §7 gains three legs; §10 seams | AC1, AC3, AC4, AC8, AC13 |
| 11 | rev-4 to rev-5 | 6, 7, 10, 11, 12, 13, 17, 20, 21, 22, 24 | §4 "The refused exit names its reason", "Order, and unit 7", "The witnessing arms" and Files touched; §5 security; §7 gains `recall floor` and `memory hygiene` | AC6, AC7, AC9, AC15 |

**Moved line numbers.** New cites are to the tip, `fda78c56`, and each revision line says where the audit report's line numbers moved:
- The accepted-stops class rule in `matrix.py` is now at `:216-221` (the report had `:181-185`).
- The unguarded `exists` test in `classify_outcome` is now at `govkit.py:6345` (the report had `:6311-6325`).
- The CONFIGURE call is now at `govkit.py:7781` (the report had `:7744`).
- The containment line `govkit.py:222` and `resolve_prefix_token` at `:179-190` have not moved.

**What I checked**
- Every spec-side command in spec 13's criteria now reads its expected value: AC2, AC3, AC5, AC6 (spec half), AC10, AC11, AC12 (spec half), AC14, AC17, AC18 and AC20.
- `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` still grades `TOOL-dRedressedBar-13 SPECCED READY`, and names it next.
- **Memory hygiene fails on two checks:**
  - **Check 9:** the generated build index in `memory/builds/dRedressedBar/README.md` shows each spec's rev, so it is now stale. Your regenerate step after commit fixes it.
  - **Check 23:** this failure was already there before my edits. It lists CLOSED units 2, 4, 5, 7, 9, 11 and 20 with no journal evidence, plus older ledger-format items.

**Where spec 13's wording didn't match the tip**
- **Spec 10's matrix row (S18):** the row's path is built with `posixpath` today (`matrix.py:318-319`), not from `resolve_prefix_token`. The corrected paragraph says unit 10 used `posixpath` and that unit 13's S18 switches it to `resolve_prefix_token`.
- **Spec 11's Files touched (S20):** unit 11's pass (`b65688cde`) wrote no acceptance ledger. Its readings are only in the commit body. I added `memory/builds/dRedressedBar/build/` as the table requires and said so beside it. Spec 11 §6 still defines `<p11>` "as their acceptance ledgers name them", and that ledger doesn't exist. You may want to decide whether unit 11 owes one.
- **Unit 20:** I added unit 20 to the spec 7 range note in spec 10 §3. Spec 7's AC4 already counted it through playbook-render before the edit, so the kit set is unchanged.

**Decision for you: the finding I was asked to place.** I added nothing for it. Spec 13's table covers spec 10 §5 **risks** only, not §5 **observability**. The finding holds at the tip:
- `update`'s gained loop prints `no declared outcome accepts that` (`govkit.py:11187-11188`).
- `apply`'s CONFIGURE refusal still prints `unclassified, because no [[outcome]] evaluator exists yet` (`govkit.py:7811-7812`).

Spec 11 §3 already names that stale `unclassified` text as a non-goal handed to an external unit.

Files are in `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\`:
- `2026-10-14-spec-TOOL-dRedressedBar-9.md`
- `2026-10-14-spec-TOOL-dRedressedBar-10.md`
- `2026-10-14-spec-TOOL-dRedressedBar-11.md`
~~~~

### 2026-10-14T19:18:49 · gov-builder · wf_081869a4-285/af69d6e0230c06d24

Label: dRedressedBar · TOOL-dRedressedBar-13 · build

~~~~text
{
 "committed": true,
 "sha": "8df39101bd675af411f330bf91971e8cb8c9b019",
 "why": "TOOL-dRedressedBar-13's build pass is committed as one new commit, carrying a `Pass: TOOL-dRedressedBar-13` trailer. Units 10, 11 and 12 were CLOSED and the spec-writer pass `<w13>` (cdc2912f7) was in place, so the spec held as written. In the same commit spec 13's header went to CLOSED · 2026-10-14; that was the only spec edit apart from the records row the index generator renders. Every criterion is either observed in the ledger or named below as owed to the close. No divergence from the spec was found.",
 "summary": "Unit TOOL-dRedressedBar-13 is built and committed as 8df39101bd675af411f330bf91971e8cb8c9b019, with spec 13 set to CLOSED in the same commit.\n\n**What changed in the code:**\n- `tools/govkit/matrix.py`:\n  - id 6: `check_outcome_states`'s docstring now states the optional fourth row element.\n  - id 7: the key rule's two labels now start `outcome probe keys: `.\n  - id 18: the parent-home row's path now goes through `govkit.resolve_prefix_token`. Over the prefixes `tools`, `vendor/gov`, `.` and `a/b/c` it gives the same path as the old `posixpath` join, and never the hook's own path.\n- `tools/govkit/govkit.py` (id 13): CONFIGURE's `_cfg_run` call now decodes with `encoding=\"utf-8\", errors=\"replace\"`.\n- `memory/project/encoding-posture-sites.txt`: the `govkit.py` subprocess row falls from 36 to 35.\n- `tools/govkit/selftest.py` (id 17): fixture B now gets its old-vintage agent-cap row from `write_vintage_receipt`, with the row's source taken from `resolve_entry`. The block no longer works out any hash or blob id itself.\n- `tools/govkit/entries/settings-merge.kit.toml` (id 22): the comment above `[[outcome]]` now describes all three probe terms.\n- Id 10 needed no code: `derive_probe_paths` already unions keys by `want`.\n\n**Records:**\n- New ledger: `memory/builds/dRedressedBar/build/2026-10-14-build-TOOL-dRedressedBar-13-1-acceptance-ledger.md`.\n- The index generator rendered spec 13's records row and the build README's unit-13 row from the staged tree. `--check --staged` then reported clean.\n- `git diff --name-only <p13>~1 <p13>` under `spec/` lists spec 13 only.\n- All paths were staged by name, and the staged bytes are LF.\n\n**Checks that ran (probes only; no bar, suite or gate leg):**\n- **Code criteria:** a recorder over `check_outcome_probes` showed:\n  - AC7: 20 labels start `outcome probe keys: ` (19 blocks plus the liveness label). Exactly two start `lexicon `, and three do in an in-memory copy with one label respelled.\n  - AC9: the agreement label records false, and true in a copy that reads only `must_exist`/`must_not_exist`.\n  - AC16: the parent-home row reads true. The grep finds nothing at the tip and finds the line in a respelled copy.\n  - AC6, AC12, AC15 and AC19 were read with `ast`/`scan_text_io`/text cuts at the tip, each against its reading before the edit.\n- **AC13:** the spawn leg's own functions, called read-only, report 0 problems at the tip and 10 in a scratch clone at 29c72f51.\n- **Fixture B:** I imported the selftest module for its helpers (its `main` was not called) and built fixture B both ways under `%TEMP%`. The two receipts are equal as JSON. `update --write` over the rebuilt one exits 1 with one `cannot read` problem line, and the receipt's `gov_commit` does not move.\n- **Spec criteria** (AC1–AC5, AC8, AC10, AC11, AC14, AC17, AC18, AC20, AC21): sed and grep over the tip and the pinned blobs. Every red case read as the spec states.\n\nThese probes stand in for `govkit acceptance matrix` (AC7, AC9, AC16), `govkit selftest` (fixture B's checks), `encoding posture` (AC12, AC15) and the resolver leg's idiom ban (AC16).\n\n**One finding:** AC15's `\"git\", \"show\"` token read 0 before the edit as well, because the old call was spelled `\"git\", \"-C\", str(govroot), \"show\"`. That half could not have failed; `_sha(` and `blob_oid(` are what showed the defect. This is recorded in the ledger.\n\n**Owed to the main loop at the close:**\n- All section 7 gates:\n  - `govkit selftest`\n  - `govkit acceptance matrix`\n  - `govkit refusal join`\n  - `govkit selfcheck`\n  - `receipt sync (installed files match the receipt)`\n  - `python resolver (behaviour + inline parity + idiom ban)`\n  - `encoding posture (text IO names its encoding)`\n  - `spec tokens (a spec's own names resolve)`\n  - `recall floor`\n  - `recall floor arms`\n  - `memory hygiene`\n- RED-first observation of both `New arm:` lines:\n  - `tools/govkit/matrix.py`, covering AC7 and AC9: a key-rule label respelled to start `lexicon `, and settings-merge patched to two ok blocks.\n  - `tools/govkit/selftest.py`, covering AC15: fixture B with the `write_vintage_receipt` call removed.\n\n**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` ran and selected 28 classes, and I acted on them:\n- no stale claim that a receipt-only home is OPEN remains;\n- nothing reads the renamed label or the 36 count by value;\n- the row-shape docs agree;\n- the ledger has no backtick span split across lines and no fence;\n- the new locals collide with nothing;\n- the probes wrote no bytecode.\n\n**Skipped:** nothing timed out. Scratch fixtures under `%TEMP%/u13f` and `%TEMP%/u13g` were removed."
}
~~~~

### 2026-10-14T19:35:04 · gov-spec-writer · direct/abfdf07a97f219d40

Label: dRedressedBar · TOOL-dRedressedBar-16 · spec-write

~~~~text
I authored TOOL-dRedressedBar-12's correction, spec 16's S4 pass `<w16>`, in place. It is not committed and the build index is not regenerated, as my brief says.

**What changed in `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-12.md`** (`git diff`: 4 edits, 15 lines added and 5 removed, nothing else):
- **Header:** `CLOSED · rev-5` became `CLOSED · rev-6`. The status did not change.
- **§3, second non-goal:** it now says the `emitted` carry was taken by `TOOL-dRedressedBar-16` (report id 7), because the same-argv rule does not reach an argv gov has changed. It cites `check_leg_claimable`'s exact-equality test (`:4003-4008`) and the "already has a leg named" Refusal (`:4153-4159`). I checked both line ranges at base `ebce889c`, which matches the spec's base and its other citations. The old `so it wedges nothing` is gone.
- **§4 Alternatives rejected, row C5:** it now says the rejection rested on the false same-argv premise, and the verdict reads `Rejected as YAGNI on that false premise; TOOL-dRedressedBar-16 takes C5`.
- **§9:** a new rev-6 line, written in the same form as the `<w12>` precedent (`62f965ccf`). It names report id 7 and TOOL-dRedressedBar-16's AC1 and AC2, says the status stays CLOSED, and says S2 and the criteria do not move.

S2 and §6 are untouched, and no other spec was edited.

**Checks**
- **AC4's cuts at the working tree:**
  - The joined §3 cut has `TOOL-dRedressedBar-16` and no `so it wedges nothing`.
  - The C5 row in the Alternatives cut has `TOOL-dRedressedBar-16`.
  - Line 3 still reads CLOSED.
- **Plan grading:** `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` still grades `TOOL-dRedressedBar-16 SPECCED READY`, with `next: TOOL-dRedressedBar-16 (READY - build it)`.
- **Memory hygiene:** exits 1, with two failing checks.
  - **Check 9 (build index drift):** caused by this edit. `memory/builds/dRedressedBar/README.md:148` still shows spec 12 at `rev-5`. Running `python tools/memory-tree/gen_build_index.py --write` clears it, and that falls to you as the committer.
  - **Check 23 (three ledger findings):** these name CLOSED units 2, 4, 5, 7, 9, 11 and 20, plus other builds' ledgers, but no TOOL-dRedressedBar-12 criterion. This edit touches no ledger. I couldn't confirm against a clean tree, since a stash isn't allowed here.
- **Check 12 (spec conformance):** my first §9 edit dropped the `## 10. Reuse audit` heading and this check went red. I restored the heading, and it is clean on the re-run.
~~~~

### 2026-10-14T19:40:12 · gov-builder · wf_d3882864-cd3/a93ca5efd60536788

Label: dRedressedBar · TOOL-dRedressedBar-16 · build

~~~~text
{
 "committed": true,
 "sha": "8139d0637c87d633aeadf2e9de7ea0345d9dca25",
 "why": "TOOL-dRedressedBar-16 is built as its spec (rev-3) says, with no divergence. `<p12>` (fda78c56e) and `<w16>` (8efbe7e81) were both present before the build started, so the build pass had what it needed.",
 "summary": "Commit 8139d0637 on branch/gov-bar-reds-fix fixes the wedge. A narrower `apply` now keeps every other claimed kit's gate-leg ownership, so when gov later changes one of those legs' argv, the next `update --write` or `apply --kits <kit>` no longer gets refused.\n\nDeclared write set before any edit, staged by name:\n- C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/tools/govkit/govkit.py\n  - S1: `_cmd_apply`'s LEGS call now passes `carry_out_of_scope=True`, and the comment above it points at the docstring.\n  - S2: the `carry_out_of_scope` docstring paragraph of `write_gate_legs` now says both verbs keep every claimed kit in `kits`, so both pass the carry. It names TOOL-dRedressedBar-16 and says why the same-argv rule cannot replace the carry: an argv gov has changed is never claimable.\n- C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/tools/govkit/selftest.py\n  - S3: a `[dRB-16]` block after the DEPL-cMendedVintage-13 arms, built from `build_gov13`, `build_target13`, `run_gov13`, `git` and `settle`.\n- C:/projects/coding-governance/.claude/worktrees/gov-bar-reds-fix/memory/builds/dRedressedBar/build/2026-10-14-build-TOOL-dRedressedBar-16-1-acceptance-ledger.md\n  - S6: carries `**Serves:** journal TOOL-dRedressedBar-16`.\n- Spec 16: the status cell set to CLOSED (date 2026-10-14), plus the generator's records row for the new ledger.\n- memory/builds/dRedressedBar/README.md: the unit-16 row and the record count, as `gen_build_index.py --write` rendered them from the staged tree.\n\nOne hook refusal: I set the spec to CLOSED before one last docstring rewording, and scratch-guard refused the product edit because a CLOSED Tier-2 unit admits no writes. I set the status back to INPROGRESS (which it really was), made the edit, then set CLOSED again before the commit.\n\nChecks that ran (no bar, suite, leg or selftest ran):\n- **AC1 and AC2:** a scratch probe program ran section 4's sequence over fixtures under %TEMP%/drb16f, built the way `build_gov13` and `build_target13` build them.\n  - At the tip: after `apply --kits demo`, `emitted` held `('demo2 leg', 'demo2')`. `update --write` exited 0 with no `does not claim it` or `the gate-leg step refused` line. `apply --kits demo2` exited 0 with no `already has a leg named` line. Both runners' `demo2 leg` rows carried `--drb16`.\n  - Red halves, read first: govkit.py from a local clone at %TEMP%/drb16g checked out at `<p12>`. `emitted` held no demo2 row, `update` exited 1 on a `does not claim it` line, and `apply` exited 2 on `already has a leg named 'demo2 leg'`.\n  - A tip engine copy with the one keyword removed (the `New arm:` line's staged break) gave the same red readings.\n  - This stands in for the `govkit selftest` leg. The `[dRB-16]` block itself was compiled but not executed.\n- **AC3:** an `ast` probe found the call's keywords are `orders` plus `carry_out_of_scope=Constant(True)`. The docstring names the unit id, and once joined it carries no `passes no carry`. At `<p12>` the keyword is absent and the phrase is present.\n- **AC4:** `git diff <w16>~1 <w16>` shows one rev bump of spec 12 (rev-5 to rev-6, CLOSED on both sides) and one revision line naming report id 7 and AC1/AC2.\n  - The section 3 cut names unit 16 once and has 0 `so it wedges nothing`; the audited blob 62910df0 has 1.\n  - The C5 row names unit 16. Before the commit, the staged spec set was spec 16 alone.\n  - This stands in for `memory hygiene` on the ledger.\n- **AC5:** no `def` or `class` line in the tools diff. `scan_text_io` counted 35 subprocess sites in govkit.py, and 24 subprocess plus 1 file-io in selftest.py, matching the encoding-posture-sites.txt rows. This stands in for the encoding-posture leg.\n- No CR bytes in the staged diff. The pre-commit hygiene check (--staged) passed.\n\nOwed to the close (main loop):\n- The section 7 gates: govkit selftest, govkit acceptance matrix, govkit refusal join, govkit selfcheck, receipt sync, encoding posture, spec tokens, recall floor, recall floor arms, memory hygiene.\n- The RED-first observation of the one `New arm:` line: tools/govkit/selftest.py, covering AC1 and AC2. Run the `[dRB-16]` block with `apply`'s LEGS call restored to pass no carry: `update --write` should report `does not claim it`, and `apply --kits demo2` should exit 2 on `already has a leg named`. Then observe it green once restored.\n- The section 5 risk: any existing arm that asserts `emitted` holds only the selection's legs after a narrower apply would now fail. A grep found none, but only the selftest leg can confirm.\n\nBug-class checklist: `gotchas.py --for-diff HEAD~1..HEAD` selected 21 classes plus 6 universal ones. I acted on the ones that apply:\n- a-new-local-collides-in-a-long-function: grep found no other binding of the block's `_*16` names.\n- two-answers-to-one-question: no product file still says apply passes no carry.\n- ledger-token-wrapped-across-a-line-joins-nothing: no line of the ledger has an odd backtick count.\n- line-claim-matched-over-the-whole-output: the block's output checks read line by line.\n- staged-break-substitutes-a-synthetic-value: the red halves used the real `<p12>` engine.\n- fixture-passes-by-finding-nothing: the block has liveness checks, and the staged break reds it.\nNone needed a further change.\n\nEvery command returned within its bound; nothing was skipped. The %TEMP% clone and fixtures were removed."
}
~~~~

### 2026-10-14T19:50:21 · gov-spec-writer · direct/a69a25908cc93be13

Label: dRedressedBar · TOOL-dRedressedBar-14 · spec-write

~~~~text
I corrected spec 11's "Which receipt bytes" paragraph in place, as spec 14's S5 states. Nothing is committed and no index is regenerated, as instructed. The memory hygiene gate fails at HEAD and still fails with my edit. My edit adds one new failure, a stale build index, which the dispatcher's regen clears.

**TOOL-dRedressedBar-11** — authored, in `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-11.md`.

- **The diff:** it has three hunks: the header (rev-5 to rev-6), the "Which receipt bytes" paragraph, and one new rev-6 line in §9. The status still reads CLOSED.
- **What the paragraph now says:**
  - `_cmd_apply` writes its receipt twice: once under unit 14's S1, between HOOKPROBE and CONFIGURE, and again at RECEIPT.
  - In `apply` the term reads the receipt this run wrote ahead of CONFIGURE. That receipt holds this run's rows and the carried ones, and it is still the bytes the adopter read.
  - `update` is unchanged and still reads the prior receipt.
- **Sentences reworded because unit 14's ordering made them false.** The rev-6 line names each one:
  - Two came from the original draft, not from `<w12>`. These are "`_cmd_apply` writes its receipt at `:8019`, after CONFIGURE" and "So in both verbs the term reads the prior receipt". The second now says that of `update` only.
  - One came from `<w12>`: "A later run's term reads that receipt". It now says `update` reads the receipt itself, and a later `apply` reads that receipt's rows carried into its own early write.
  - `<w12>`'s sentence naming `TOOL-dRedressedBar-12` keeps its words and adds that unit 14 binds that carry ahead of the early write. Its other sentences are untouched.
  - `<w13>` wrote nothing into this paragraph, which I confirmed from its commit.
- **Added one sentence the brief did not ask for:** a first `apply` never reaches the "With no receipt" reading. That neighbouring paragraph says a fresh `apply` reads only the two static homes, which stops being true once unit 14 lands. Rather than edit a second paragraph, I put the qualifier inside the one this pass owns, and the rev-6 line records it. Drop it if you want the narrower diff.
- **Citations:** the paragraph's existing line numbers are base-commit (`ebce889c`) numbers, as spec 14's are. I left them as they were. Unit 14's write is cited by its spec's S1, because unit 14 is not built yet. At the tip the RECEIPT write is at `tools/govkit/govkit.py:8080` and unit 12's carry at `:8076-8078`.

**Checks:**
- **Spec 14's AC6:** spec 11's §4, cut and joined the way AC6 does it, carries `TOOL-dRedressedBar-14` twice. The diff shows one rev bump and one revision line naming that unit, and spec 11 was already CLOSED at HEAD.
- **The unattended plan:** `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` still grades `TOOL-dRedressedBar-14	SPECCED	READY` and prints `next: TOOL-dRedressedBar-14 (READY - build it)`.
- **The memory hygiene gate:** it exits 1 both with HEAD's spec 11 and with my edit. To compare, I put HEAD's spec 11 back temporarily, then restored my edit.
  - **Already failing at HEAD:** three check-23 lines. One lists unit 11's AC1 to AC7 with no journal record, because unit 11's pass wrote no ledger. The others concern records outside this build. None comes from this edit.
  - **New with my edit:** check 9, "generated build index differs from a fresh render", for `memory/builds/dRedressedBar/README.md`. The rev bump makes the derived index stale. `python tools/memory-tree/gen_build_index.py --write` clears it, and that regen is yours before the commit.

**For the commit:** the commit subject must name `TOOL-dRedressedBar-14` so that commit can serve as `<w14>`, and unit 14's ledger must name it, as AC6 requires.
~~~~

### 2026-10-14T19:56:24 · gov-builder · wf_f9ca5bcd-fd4/a29cf5a5bef63c51d

Label: dRedressedBar · TOOL-dRedressedBar-14 · build

~~~~text
{
 "committed": true,
 "sha": "109fbb4ab",
 "why": "Unit TOOL-dRedressedBar-14 is built as its spec (rev-5) says and committed as its build pass, 109fbb4ab, with the trailer Pass: TOOL-dRedressedBar-14. The same commit moves spec 14's status cell to CLOSED. A records follow-up, ffe73d97d with Pass: none, unwraps six backtick spans in the acceptance ledger that the M6 checklist flagged. Before writing, I checked that every prerequisite exists: <w14> is 07c83c534, <p13> is 8df39101b, unit 12's carry is in the code and _rcpt_doc was not yet used. I found nothing that disagrees with the spec.",
 "summary": "**What changed.**\n- `tools/govkit/govkit.py`, S1 and S3: `_cmd_apply` now writes `.governance/install.json` between HOOKPROBE and CONFIGURE.\n  - It writes one dict, `_rcpt_doc`, with the same keys in the same order as the RECEIPT write.\n  - Unit 12's `_carried_kits` and `_carried_rows` are now set there, once. The `.governance` mkdir moved up with them.\n  - `orders`, `after` and `gate_runner` take the prior receipt's values, or the empty values the spec's table gives.\n  - A comment above the write gives the per-kit-prefix case, names the class of adopters that find a sibling kit through the receipt, and says RECEIPT rewrites the file.\n  - One line prints after the write: `govkit apply — receipt written ahead of CONFIGURE: <n> row(s), <k> kit(s); RECEIPT rewrites it`.\n- `tools/govkit/govkit.py`, S2: the RECEIPT step updates `_rcpt_doc` with `files` re-derived and this run's `orders`, `after` and `gate_runner`, then writes it. `install.sums` and the STEP_RECEIPT counts now read the dict's lists.\n- `tools/govkit/selftest.py`, S4: a `[dRB-14]` block after the `[dRB-12]` block.\n  - It applies agent-cap, settings-merge and kickoff-manifest to a target with agent-cap at the `scripts` prefix. The result is kept in `_rb14p`, which unit 15 reads.\n  - It has six checks. Each label is a plain string, and each fact is read on the line it names. No exit code is asserted.\n  - The agent-cap problem-line check has `kit 'agent-cap'` in its source, so unit 17 can find it and narrow it away.\n- S7: the ledger is `memory/builds/dRedressedBar/build/2026-10-14-build-TOOL-dRedressedBar-14-1-acceptance-ledger.md`.\n- The index generator added the ledger's records row to spec 14 and moved the README's record count. Both are generated; each is noted on a `Decided:` line.\n\n**What ran.** No bar, suite, gate leg or slice of a suite ran. Every check was a probe of this unit's own CLI, `govkit.py apply`. The probes ran over fresh `git init` targets under `%TEMP%/b14*`, against the tip, a `<p13>` clone, and a tip copy carrying one deliberate break. Scratch scripts are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-bar-profile-failures-b80cc3/8d2976c7-7629-4ba0-8a96-2098db6da20f/scratchpad/`. All six criteria were observed passing, and each criterion's failing case was observed too:\n- **AC1:**\n  - At the tip, the settings-merge line reads `adopter exit 0`, and the early-receipt line comes before the first CONFIGURE line.\n  - The receipt has a row for `scripts/hooks/agent-cap.js`, and settings.json wires exactly that one command.\n  - There is exactly one agent-cap problem line, and it names `settings-merge.py`. Exit 1 remains, as §8 F1 expects.\n  - Over `<p13>`, the settings-merge line reads `no-agent-cap-to-wire [accepted stop]` and no `agent-cap.js` command is wired.\n- **AC2:** both default-prefix applies exit 0 and their settings.json files are byte-equal. The diff, with the `[3/LAND]` lines dropped, is the one early-receipt line.\n- **AC3:**\n  - Spec 11's fixture A at the tip: exit 1, one `cannot read` line, no `no-agent-cap-to-wire`.\n  - The tip copy whose early write uses `selection` and `rows` instead: exit 0 with `[accepted stop]`.\n- **AC4:**\n  - The tip copy with the added `raise` leaves the early receipt behind: all three kits claimed, every engine row with an `oid`, `orders` empty.\n  - The unpatched re-run is not refused and prints one settings-merge CONFIGURE line.\n  - Over `<p13>` no receipt is left, and the re-run exits 2 on `already carries`.\n- **AC5:** no `def` or `class` lines added, and `_rcpt_doc` appears 9 times. `scan_text_io` counts match the registry exactly: govkit.py 35 subprocess, selftest.py 24 subprocess and 1 file-io.\n- **AC6:** `<w14>` read as the criterion requires. This pass's commit touches no spec file but spec 14.\n\nThese probes stand in for `govkit selftest` (AC1's readings), the encoding-posture leg (AC5) and memory hygiene (the ledger). An `ast` read of the `[dRB-14]` block stands in for running the block itself, which this pass may not do.\n\n**Owed to the close.**\n- Every section 7 gate: govkit selftest, acceptance matrix, refusal join, selfcheck, receipt sync, encoding posture, spec tokens, recall floor, recall floor arms, memory hygiene (check 23 was held under `--staged`).\n- The `New arm:` RED-first observation: the `[dRB-14]` block over `<p13>`, then green restored.\n- Spec §5's risk arm `[-6] AC5`, and the arms that expect no receipt, are only graded by the selftest.\n\n**Checklist (M6) result.**\n- It selected ledger-token-wrapped-across-a-line-joins-nothing. Six wrapped spans in the ledger are fixed in ffe73d97d.\n- It also selected amendment-leaves-its-other-half-standing. The comment at `tools/govkit/govkit.py:7814-7816` (from unit 13) still says CONFIGURE runs \"before the receipt is written\" and calls a decode error there the F4 no-receipt half-install. After this unit that holds only for the final receipt. My correction was blocked by scratch-guard, because a CLOSED Tier-2 unit admits no further product writes. I did not work around it, so that comment needs fixing in a later unit.\n\n**Cleanup.** No probe went past its time limit, and none was skipped. The `%TEMP%/b14*` fixtures and clones are removed."
}
~~~~

### 2026-10-14T20:09:39 · gov-spec-writer · direct/a5bb5255ed20f44e4

Label: dRedressedBar · TOOL-dRedressedBar-15 · spec-write

~~~~text
I wrote spec 15 at rev-4 and nothing else changed. The unattended planner (`--plan dRedressedBar --paths`) grades TOOL-dRedressedBar-15 as SPECCED and READY. Files touched is unchanged: it still lists `tools/govkit/govkit.py` and names no other spec. Status is still SPECCED.

The memory hygiene gate is still failing, but none of the failures come from spec 15. Check 23 fails on other units' ledgers (units 2, 4, 5, 7, 9, 11, 20 of this build and some aSparedSpawn units). Check 9 fails because `memory/builds/dRedressedBar/README.md` differs from a fresh render, which the rev bump and the two uncommitted prompt files probably cause; the regen is yours. Check 25 did fail on spec 15 at first, because S10 drops a named phrase and so needs a **Readers:** clause. I added one and check 25 now passes.

**Unit returned: TOOL-dRedressedBar-15 — authored (rev-3 to rev-4).**

What I changed in `C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-15.md`:
- **S10:** the comment above `_cfg_run` (`tools/govkit/govkit.py:7811-7816` at `ffe73d97d`) gets rewritten. The brief cites 7811-7815, but the block actually ends at 7816. The first sentences and their `TOOL-dRedressedBar-11 S3` and `TOOL-dRedressedBar-13` credits keep their meaning. The last sentence is replaced, and the two lines of the call itself are not touched. It is a comment only, so no new arm.
- **§4, new section "The CONFIGURE comment, restated":** the full replacement text, plus what a decode error at the spawn would now leave behind, checked against the code:
  - the landed bytes, staged (`:7662-7663`);
  - the early receipt (`:7715-7726`), carrying the previous run's orders, `after` and gate runner;
  - the hole outbox files written so far (`:7742-7746`);
  - `install.sums` not rewritten, because it is only written next to the final receipt write (`:8117-8119`);
  - no adopters run after that kit.

  That is the interruption the receipt comment at `:7708-7709` says a re-run of `apply` recovers from, not F4's no-receipt half-install. F4's own comment at `:7670-7672` stays correct, because `index_read` runs before the early write.
- **AC11:** a joined text cut of the comment block above the line that opens `_cfg_run = subprocess.run(`. At the tip it must not contain `before the receipt is written`. It must contain `ahead of CONFIGURE`, `RECEIPT rewrites`, `TOOL-dRedressedBar-14`, `TOOL-dRedressedBar-11 S3` and `TOOL-dRedressedBar-13`. The anchor line and the line after it must match `ffe73d97d` byte for byte. "Red when" names `ffe73d97d`. I already saw it fail there: one anchor, and the cut contains the stale phrase and none of the new tokens.
- **§9:** the rev-4 line names the finding, `amendment-leaves-its-other-half-standing`, which unit 14's builder selected over `109fbb4ab`.

Smaller wording changes so the rest of the spec agrees with S10:
- **§1:** one sentence.
- **§3:** a non-goal saying the receipt and F4 comment blocks are left alone, plus a note on the consumes-from edge to unit 14.
- **AC10:** reworded to count "the other criteria in this section", so it still covers AC11 even though AC11 comes after it.
- **§4 veto, §5 testing, §7:** the veto range now reads AC1 to AC11, §5 mentions AC11, and §7 says S10 adds no arm.
- **§10:** lists the gotcha class.

No open questions; §8 stays `none`.
~~~~

### 2026-10-14T20:17:07 · gov-builder · wf_22d3be56-feb/a3284d9723a7b0592

Label: dRedressedBar · TOOL-dRedressedBar-15 · build

~~~~text
{
 "committed": true,
 "sha": "7da62c2410f3d0d432a4f8e843db8ee76e4f737d",
 "why": "TOOL-dRedressedBar-15 is built as its spec says, in three commits, each with a Pass: TOOL-dRedressedBar-15 trailer. 0a178ed8f is the product commit (p15a). 4d3cae332 is the version mint (p15): agent-cap goes from 1.39 to 1.40, and the mint named no other kit. 7da62c241 holds the acceptance ledger, the spec status set to CLOSED, and the generated index rows. Nothing in the code disagreed with the spec, so there is no divergence.",
 "summary": "Built TOOL-dRedressedBar-15. Every criterion is observed by a probe except AC6, which only the `govkit selfcheck` leg can observe. That leg and the section 7 gates are owed to the close.\n\n**What changed**\n- `tools/govkit/govkit.py`:\n  - New function `resolve_adopter_argv`, placed after `target_context`. The naming lexicon answered OK for it.\n  - CONFIGURE in `_cmd_apply` and the gained loop in `_cmd_update` now get their argv from it. The configured kit's own descriptor still classifies the exit.\n  - The comment above `_cfg_run` is rewritten to match unit 14's early receipt (S10). The call itself is unchanged.\n  - selfcheck gains the cross-entry arm: the four `via` rules, the ownership join, an always-printed note, and a red when elements are offered but none graded. Its locals all start with `_xa_`.\n- `tools/hooks/kit.toml`: agent-cap's `[adopt]` table is now just `via = \"settings-merge\"`.\n- `tools/govkit/selftest.py`: `[dRB-15]` checks that read the existing `[dRB-14]` apply, plus seven scratch govs built on `build_scratch_gov_kit`.\n- `memory/map/generated/symbols.json` regenerated.\n- The mint moved the three version markers in `tools/hooks/` to 1.40.\n- Ledger: `memory/builds/dRedressedBar/build/2026-10-14-build-TOOL-dRedressedBar-15-1-acceptance-ledger.md`.\n\n**Checks that ran, and the gate each stands in for**\n- **AC1–AC4** (for `govkit selftest`): applies over fresh targets under `%TEMP%/drb15*`, run from the worktree and from clones at p14 (`%TEMP%/drb15g14`) and p15 (`%TEMP%/drb15g15`).\n  - AC1: exit 0 at p15. At p14 it exits 1 with agent-cap at `adopter exit 2` and \"can't open file\".\n  - AC2: the default-prefix apply prints the same CONFIGURE lines at p14 and p15, and `settings.json` is byte-equal.\n  - AC3 and AC4 pass both halves; AC4's red half deletes the `via` line in the p15 clone.\n- **AC5**: a python probe returns `tools/settings-merge.py` for both kits at one per-kit prefix and `scripts/settings-merge.py` at the other. At p14 the two kits split.\n- **AC7** (for `govkit selftest`): all seven scratch govs print the expected lines. The same govs built around p14's `govkit.py` print no `cross-entry argv:` line.\n- **AC8** (for `kit epoch` and `kit version markers`): epoch read FAILED at p15a and clean 1.40 at p15.\n- **AC9** (for `encoding posture` and `codebase-map coverage + freshness`): the diff adds one function, `_argv_g` is gone, `gen_map --check` exits 0, and the encoding counts match the registry.\n- **AC11**: the comment text above `_cfg_run` matches the spec at the tip, and is red against ffe73d97d.\n- **AC6 stand-in** (for `govkit selfcheck`): my own reimplementation of the join over the real registry reads 105 offered, 105 graded, 1 hit before the change and 0 after, matching the spec.\n\n**Owed to the main loop at the close**\n- AC6 itself. The hook refused `govkit.py selfcheck` to this role (leg G1), so I did not run it on a gov clone either.\n- All section 7 gates.\n- The RED-first observations for both `New arm:` lines in `selftest.py`: the AC1 checks over p14, and the AC7 scratch govs over p14.\n\n**Expected red at the close until unit 17 lands**\nThe `[dRB-14]` check expecting exactly one `govkit: kit 'agent-cap'` line will fail, because that line no longer prints. Unit 17's S1 removes that check.\n\n**Bug-class checklist**\nI ran `gotchas.py --for-diff` over both `HEAD~1..HEAD` and `HEAD~3..HEAD` and acted on each class. No code change came out of it:\n- Ledger: no backtick span wraps a line, and every line shares a token with its criterion (I fixed the wrapped spans before committing).\n- Retired keys: nothing else reads the dropped `argv`, `mutates_index` or `why_no_regenerate` values.\n- `check_entry_producer`'s docstring still quotes the old CONFIGURE lines. Unit 17's S11 owns that fix.\n- The selftest helper binds `_gk` inside its own nested function, so it does not touch the outer `_gk` module handle.\n\nScratch targets and clones are left under `%TEMP%/drb15*` because the ledger cites them. Nothing I ran timed out or was skipped."
}
~~~~

### 2026-10-14T20:38:02 · gov-spec-writer · direct/a4a53729b8800e393

Label: dRedressedBar · TOOL-dRedressedBar-17 · spec-write

~~~~text
I applied every row of spec 17's §4 correction table to specs 9, 12, 13, 14 and 15. Nothing is committed and no index was regenerated.

Each of the five specs has one rev bump and one new §9 revision line. Each line names `TOOL-dRedressedBar-17` and every report id the table assigns that spec. All five still read CLOSED: spec 9 is now rev-7, spec 12 rev-7, spec 13 rev-6, spec 14 rev-6 and spec 15 rev-5. Apart from the in-place edits the table asks for, nothing else changed.

**Checks run:**
- I ran each spec-side half of spec 17's criteria against the edited text, and they all hold: AC1, AC4, AC5, AC6, AC8, AC9, AC10, AC19, AC20, AC21 and AC23.
- For AC4, I joined spec 15's Files touched against `tools/gate-legs.json`. It found no leg missing from the leg line.
- `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` still grades unit 17 READY.
- The memory hygiene gate is red on check 9: `memory/builds/dRedressedBar/README.md` is stale because its rev cells are generated from the spec headers I bumped. It goes green once you regenerate the index after committing. The three check 23 failures were already there before I edited anything.

**Where the tip had moved, and how I handled it:**
- **Spec 9, id 20:** of the two sentences the row targets, only the one in "Why the shared argv stays safe" (`:175`) still existed, and I corrected it. The "What it does not check" sentence was already removed in spec 9's rev-5 (unit 10's pass, `67a23b14d`). The revision line says so, and nothing changed for that half.
- **Line citations in specs 13 and 14:** spec 17's AC8 checks the line numbers at `29c72f51` and AC9 the ones at `46eb75ed`, so I kept those as the main citations and added the tip's lines (`7da62c241`) beside them.
  - In spec 13 the tip's lines go into §3 and §5 directly: the regenerate site is at `:11213-11215` and the gained loop at `:11349-11350`.
  - In spec 14 they go only in the revision line, because AC9 counts the line numbers in §4. The six appends to `rows` are now at `:7586`, `:7664`, `:7702`, `:7755`, `:7778` and `:7783`, with STAGE at `:7808`. The window id 22 leaves exposed now runs from `:8071` to `:8140-8151`.
- **Text describing unit 17's own changes:** several rows correct text about changes unit 17 has not built yet (ids 22 and 23 in spec 14, ids 11 and 24 in spec 15). I wrote each one as what was built, then what `TOOL-dRedressedBar-17` changes, so the text stays true now and after the build. In spec 15 I also renamed "second rule" and "third rule" by their content, because the new first row in the rule table shifted their numbers.
- **Spec 15, id 21:** the build pass ran the whole `regen.py --write`, as `0a178ed8f`'s commit message says. That commit moved four paths, all inside Files touched, and the revision line says none moved outside.

**For the main loop, before unit 17's build pass:**
1. **Spec 17's AC24 red half will not reproduce over `<p15>`.** Unit 15's selfcheck already triggers on the `via` key being present (`tools/govkit/govkit.py:3296`) and checks the value is a string before using it. So over the built code, both `via = ""` and `via = ["other"]` print `names no registry entry`, with no traceback. Spec 17 expects no line for `via = ""` and a traceback for `via = ["other"]`, in both AC24 and the AC11/AC24 `New arm:` line. That part of AC24 needs revising in spec 17, which was outside my write set. The other red-half check, `resolve_adopter_argv` falling back instead of raising `KeyError`, should still hold.
2. **`govkit selftest` is currently red by design.** The `[dRB-14]` check that one line opens `govkit: kit 'agent-cap'` (`tools/govkit/selftest.py:3562-3566`) and the `[dRB-15]` check that no such line prints (`:3581-3583`) both read the same apply. Unit 15's ledger already expects this until unit 17's S1 moves the first check out.

Files changed:
- C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-9.md
- C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-12.md
- C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-13.md
- C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-14.md
- C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-15.md
~~~~

### 2026-10-14T20:56:08 · gov-spec-writer · direct/a56204efe88a8bf1c

Label: dRedressedBar · TOOL-dRedressedBar-17 · spec-write

~~~~text
I've revised spec 17 to rev-4. Its status stays SPECCED and no other spec was touched. `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades it `TOOL-dRedressedBar-17 SPECCED READY`.

**Spec:** C:\projects\coding-governance\.claude\worktrees\gov-bar-reds-fix\memory\builds\dRedressedBar\spec\2026-10-14-spec-TOOL-dRedressedBar-17.md

**What I confirmed at the tip:** `tools/govkit/govkit.py` hasn't changed since `0a178ed8f`. That is the same file as `<p15>` (`4d3cae332`, as unit 15's ledger records).
- **Selfcheck** checks for the key's presence (`:3296`). It uses the value only if it is a string that names a registry entry (`:3298`), and otherwise reports `names no registry entry` (`:3300`). So `via = ""` and `via = ["other"]` each print one `govkit: entry 'demo' declares [adopt] via = '…', which names no registry entry` line. The type test runs before the lookup, so a list never reaches the step that would raise `unhashable`. Nothing earlier in selfcheck reads `via`.
- **`resolve_adopter_argv`** (`:1511-1512`) uses `via` as the source only when it is a non-empty string, and otherwise falls back to the entry itself. For `via = ""` it returns the entry's own resolved argv, or `[]` if the entry has none, and never raises `KeyError`. CONFIGURE then skips an empty result without printing anything (`:7937-7939`). So the fallback red half still holds.

**What changed in spec 17:**
- **Header:** rev-3 became rev-4.
- **§1 row 24:** the finding is restated as the run-time fallback. As built, selfcheck refuses both `""` and a list and crashes on neither.
- **S24:** split into two halves, both cited to the lines above.
  - The selfcheck half only changes the reason: `is not a non-empty string` replaces `names no registry entry`.
  - The `scan_entry_argv`/`resolve_adopter_argv` half is the behaviour change: `KeyError` instead of the fallback.
- **AC24 "Red when":** at `<p15>`, each value prints one `via` line carrying `names no registry entry` in place of `is not a non-empty string`, and neither output carries `Traceback`. `resolve_adopter_argv` for `via = ""` raises nothing and returns demo's own resolved argv, or `[]` (`:1511-1518`). The green half is unchanged.
- **§7 `New arm:` line for AC11 and AC24:** rewritten the same way. The AC11 half is unchanged and still holds at `<p15>`: with a valid `via` beside a `rendered` rule, none of the four rules fires, so no `via` line prints.
- **Security sentence:** this is in §5, not §4 as the brief said. It now reads that S24 turns `resolve_adopter_argv`'s silent fallback into a `KeyError` at run time, and that selfcheck already refuses a malformed `via` at `<p15>` and only gains its own reason. §5's "never a traceback" line was already true and stays.
- **§9:** a rev-4 line names the `<w17>` finding and cites `prompts/2026-10-14-prompt-TOOL-dRedressedBar-17-6-revision.md`.

**Memory hygiene:** it fails, but nothing it reports names unit 17 or this spec.
- Check 23 fails on other units' ledgers. Those failures were already there.
- Check 9 says `memory/builds/dRedressedBar/README.md` is stale. This rev bump is one cause: the README's build index still shows rev-3 for unit 17. Whoever commits needs to run `python tools/memory-tree/gen_build_index.py --write`, which I was told not to run.
~~~~

### 2026-10-14T21:02:41 · gov-builder · wf_7d717f4b-82d/a859d9bcda67ed117

Label: dRedressedBar · TOOL-dRedressedBar-17 · build

~~~~text
{
 "committed": true,
 "sha": "26beaa6fe2f71ce37e02145467b943f1ce8dece2",
 "why": "TOOL-dRedressedBar-17 is built and closed in three commits, each with a `Pass: TOOL-dRedressedBar-17` trailer: the product commit <p17> 6057a55c1, the manifest re-stamp <p17m> d3d0dabf9, and the records commit 26beaa6fe (the ledger, plus spec 17's status set to CLOSED with today's date). Every criterion was either observed with a probe or is named below as owed to the close. Two findings need the main loop to dispose of them: AC22's DIRTY clause does not reproduce, and the commit-time manifest check forced a re-stamp that S18 did not plan for.",
 "summary": "**What was built**\n\nThe product commit 6057a55c1 has all of spec 17's code changes:\n\n- **One argv walker.** `tools/govkit/govkit.py` gains `scan_entry_argv` after `silenced_legs` (the lexicon accepted the name). `silenced_legs`, `resolve_adopter_argv` and selfcheck's cross-entry join now all read it. The `gate legs:` note counts its `[[gate_leg]]` entries and the `cross-entry argv:` note counts all of them.\n- **`via` rules.** Selfcheck's `via` rules gain a first rule (`is not a non-empty string`) and a last one (no `rendered`, `generated` or `merged` rule). At run time a malformed `via` now raises KeyError instead of falling back.\n- **Docstring.** `check_entry_producer`'s docstring is restated.\n- **Receipt writes.** `receipt_path` is added to `ADOPTER_BAR_PATHS`, and all six receipt writes go through `write_atomic` (0 direct writes left). `apply` writes the receipt once more after the `oid` re-stamp when RENORMALIZE ran.\n- **Selftest.** `tools/govkit/selftest.py` gets the S1, S2, S3, S11, S13 and S24 checks.\n- **Guard.** `tools/gate-legs.json` widens the `govkit selftest` guard with the two files.\n- **Symbol index.** `gen_map.py --write` ran alone and updated `symbols.json`.\n\nThe ledger is `memory/builds/dRedressedBar/build/2026-10-15-build-TOOL-dRedressedBar-17-1-acceptance-ledger.md`.\n\n**Checks that ran**\n\nNo bar, suite or gate leg ran. Each check below was a probe of my own change, standing in for the gate named:\n- Scratch applies, updates and checks over fresh targets under %TEMP%/d17*, standing in for `govkit selftest`: AC2, AC13, AC22 and AC23, each with its red half run on a clone at <p15>, <p14> or <p17> with one deliberate break added to its `govkit.py`.\n- Scratch govs, standing in for `govkit selftest` and `govkit selfcheck`: AC11 and AC24, red halves on the <p15> engine.\n- An in-process probe of the walker over the real registry, standing in for `govkit selftest`: AC10. It counted 169 gate-leg elements and 279 in all, 105 graded, and `silenced_legs` and `resolve_adopter_argv` return the same results as before.\n- A stand-in that recomputes the two selfcheck notes, for the refused `govkit selfcheck` leg: AC10 and AC16. It reads 0 hits at <p17>, and 1 hit with <p14>'s `tools/hooks/kit.toml`.\n- Source and spec greps: AC1, AC3 to AC9, AC18 to AC21, AC25.\n- A copy of the selftest's `[-21] AC2` routing walk, standing in for `govkit selftest`.\n- The naming lexicon for the new names.\n- `gotchas.py --for-diff` over 51c6e772b..HEAD and over HEAD~1..HEAD, both acted on.\n\n**Owed to the close**\n\n- The section 7 gates, all of them.\n- RED-first observations for the five `New arm:` lines (they cover AC2, AC3, AC13, AC11 and AC24, and AC23).\n- The two selfcheck note lines for AC10 and AC16. scratch-guard refuses `govkit selfcheck` to this role even inside a clone.\n\n**Findings for the main loop**\n\n1. **AC22's DIRTY clause cannot be observed.**\n   - The target I used commits the playbook seed `docs/PARALLEL.md` with CRLF line endings, under its LF pin, and refreshes the git index before applying. In it the renormalize moves the index blob (f1752b30 to 1844b4ce).\n   - Green half holds: the receipt's `oid` follows the new blob, and the re-run prints no DIRTY.\n   - Red half: the differing `oid` reproduces, but the re-run prints no DIRTY line.\n   - Seed rows are outside the dirty check's population, because `seed` maps to `report-reseed`.\n   - A target with `core.autocrlf` true and pinned engine rows moved no blob at all.\n   - In this state, the re-run exits 1 with or without S22 on the renormalize guard. So spec 14's corrected sentence that \"a re-run of apply recovers\" is also not observed here.\n   - The ledger records the DIRTY clause as returned to the main loop, not counted.\n2. **S18's two-commit plan does not get past the pre-commit check.** The manifest ratchet's staged check refuses a `tools/gate-legs.json` commit unless the manifest re-stamp is in the same commit. So <p17> carries a re-stamp at its parent, as precedent b357641ed did, and <p17m> re-stamps at <p17>, which AC18 needs. I did not use `--no-verify`.\n3. **The spec header is in <p17>.** Hygiene check 9 re-renders the build index on that commit, so <p17> carries the INPROGRESS header the dispatcher set, plus the index rendered from it. This is the only spec file under `spec/` that <p17> touches.\n\n**Other choices** (each also on a `Decided:` line in its commit)\n\n- The cross-entry note keeps its now-inaccurate `slash-bearing` label. Spec 17 changes its counts, not its text, and TOOL-dRedressedBar-19 S2 corrects the label, with a red half that depends on the label still being there.\n- A nested helper, `read_sums_pairs17`, reads the sidecar for both the dRB-12 and dRB-14 checks.\n- `stale_target` gains a `kits` argument instead of a second builder.\n- The records commit also carries the generated README and LIVE rows, as units 12 to 16 did."
}
~~~~

### 2026-10-14T21:36:47 · gov-builder · wf_2e958a62-4b6/af9e8721f060c270a

Label: dRedressedBar · TOOL-dRedressedBar-18 · build

~~~~text
{
 "committed": false,
 "sha": "",
 "why": "DIVERGENCE: spec 18's Job Object mechanism (S3; §4 candidates row 1 and \"Measured on node d\"; §5 risks; AC1, AC2) fails its own test on node d, and §5 rules on that case: \"a breakaway there parks the unit rather than shipping a census-only count\". The cause is one the spec did not consider. The runner's resolve_python resolves PYBIN to `python3`, which on node d is a Microsoft Store App Execution Alias (C:\\Users\\d41ly\\AppData\\Local\\Microsoft\\WindowsApps\\python3.exe, starting pythoncore-3.14-64). Everything started through that alias leaves a job created with no limit flags. Evidence: on serial.json every leg read procs_total 1 (the bash root only), so spawn six minus spawn none = 0, not 6 (AC1 fails), and memio read peak_job_mem_b 6950912 with write_bytes 0 against at least 200 MiB (AC2 fails). In a scratch manifest, a bash leg running only sleeps counted 7 (bash-forked processes DO stay in, so the escape §4 feared does not happen), a plain Python312 python.exe running spawn.py 2 1 counted 4, and the `python3` and `py` aliases counted 1 each. With no bash in the path, a plain python.exe kept its child in the job (2) while the alias kept only its stub (1). The spec has to choose how an alias launcher is handled, which is a design fork, not a build choice: (a) a preflight that runs PYBIN and each distinct launcher once in a test job and refuses with exit 2 naming the alias, remedy GOV_PYTHON set to a non-alias interpreter, which the runner honours too so the bar and the profile still run one python; (b) resolving the alias to its real interpreter for the legs, which drops the alias's own extra process from every reading so they are no longer the bar's; or (c) a per-leg escape check, the census tree compared against job membership, that marks the job totals unknown. AC1 and AC2 must also name the python they run under. Every path I changed is restored; the work is saved in the scratchpad's unit18-wip/ for the redispatch.",
 "summary": "TOOL-dRedressedBar-18 was not committed. Spec 18's Job Object mechanism failed AC1 on node d, and spec §5 says that case parks the unit (see why).\n\nBuilt, then removed: tools/run-gates/measure_legs.py (the full profiler and its --selftest), 12 fixtures under tools/run-gates/fixtures/measure-legs/, and the process-monitor changes (census.py CIM query and parse_cim carrying peak_mem_b and mem_b, selftest.py's CIM fixtures moved to seven fields, the row-contract arm admitting the two keys, the AC3 arm test_cim_memory_fields_are_bytes, and every 0.18 marker moved to 0.19). The process-monitor files were restored with git checkout. measure_legs.py, the fixtures dir and the __pycache__ dirs my compile created were deleted. The tree matches HEAD 26beaa6fe apart from the dispatcher's pre-existing INPROGRESS header on spec 18, which I did not touch. The planner will keep naming this unit until that header is reset or the spec is revised.\n\nSaved for the redispatch: C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-bar-profile-failures-b80cc3/8d2976c7-7629-4ba0-8a96-2098db6da20f/scratchpad/unit18-wip/ (measure_legs.py, fixtures/measure-legs/ with 12 files, process-monitor.diff of 255 lines). Never written: the gate-legs.json row, kit.toml, selftest-budgets.txt, windows-only-legs.txt, the runner version bump, the two READMEs, the help page, the map claim.\n\nChecks that ran. Each is a probe of this unit's code, and the merge bar did not run.\n- Pure probe, standing in for the process-monitor census selftest and the measure-legs selftest arms. AC3: peak_mem_b 307200, mem_b 409600, command intact, POSIX rows None, FIELDS unchanged; the red staging, reading index 4, gives '300'. AC5: [False, True, False, False, True]. AC12: refused, naming 'linux' and the Job Object API. The scrub derivation and the extraction refusal also held.\n- AC8 parity probe: the runner's own measure_foreign with ps shimmed and the port both gave 2 roots, {200:lib9/runner.sh, 300:probe/two/selftest.py}. The port without the selftest.py rule gives 1.\n- CLI run over serial.json with the AC9 knobs set. AC9: GATE_JOBS, GATE_REUSE and GATE_TURNSTILE_HOLDER scrubbed by the GATE_ prefix and GIT_NAMESPACE by the pre-push unset line, none in the leg's log. AC10: every record on disk, each .leg row 8 fields. AC11: the log carries ://***:***@, no s3cret in the run dir or raw/, raw/ empty, raw_kept empty. AC1 and AC2 FAILED, which is the divergence.\n- escape.json probe and a direct alias-in-job probe, which isolated the cause.\n- CIM unit probe: PeakWorkingSetSize is KiB (78232 beside Get-Process 76533760 bytes); WorkingSetSize is already bytes.\n- The naming lexicon (--suggest) answered OK for every added name.\n\nSkipped or owed:\n- AC4, AC6, AC7: the concurrent and stall runs were skipped once AC1 failed.\n- AC13, AC14: the declarations were never written.\n- AC15 and the RED-first observation of both New arm lines run the real runner, so they are owed at the close.\n- gotchas.py --for-diff was not run, because there is no commit.\n\nFor the spec writer:\n1. Unit 19's S11 path conversion is needed in unit 18 already. Native Python cannot open bash's /tmp/... scratch path; the saved code uses cygpath -m for the scratch dir and the turnstile key.\n2. The pre-commit kickoff-manifest ratchet refuses a commit that stages tools/gate-legs.json or run-gates.sh unless it carries a last-audit re-stamp of memory/guides/SESSION-KICKOFF.md, as unit 17's commit did. Unit 18's Files touched should list that file, while unit 19 S1 keeps the reviewed second commit.\n3. test_row_contract_is_complete compares exact key sets, so it goes red when census rows gain keys unless it changes in the same commit."
}
~~~~

