# TOOL-aOrientedCast-25 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-25 TOOL-aOrientedCast-21 TOOL-aOrientedCast-22

Direct checks only: no gate, suite, slice or self-test ran in this pass. What ran: two bash probes
in the run's scratch path that scaffold fixture F the way `build_fixture` does (a `git init`
repository under `%TEMP%/t25c` and `%TEMP%/t25d` holding a copy of the kit, the repository's
`AGENTS.md` as its charter, scaffolded by `adopt-roles.sh --scaffold`), run arm 9's `A9_WRITE`
cut out of the suite by text, and drive `handoff.py agents`, `handoff.py render --stand-in`,
`check_roles.py`, the hooks kit's `agent-cap.js` and format-guard's `readCharterShapes` through
every step §4 names; the same verbs over the base `handoff.py` and `roles_lib.py` (`git show
HEAD:`) for the red halves of AC1 and AC6; the `sh_hygiene.scan_file` probe of AC13 over the gate
and over a scratch copy carrying rev-4's heredoc-fed loop; a `bash -c` probe of `fail 9`'s `case`
alone; the greps and searches each criterion names; `lexicon.py --suggest extract_prompt_marker
--as py.function`, which answered OK; `gotchas.py --write`; and `gen_map.py --write`, which moved
`symbols.json` alone. Owed to the main loop at the close (M8): every leg §7 lists; AC7's three runs
of `tools/check-microformats.sh`, which are the `micro-format definitions` leg; AC11's rendered
`.claude/skills/build/SKILL.md`, re-rendered by `bash tools/roles/adopt-roles.sh --scaffold` in the
second pass; and the RED-first observation of each of §7's five `New arm:` lines, on its staged
break and green once restored.

**Evidences:** TOOL-aOrientedCast-25
- AC1 — `toolu_A` — in F, with `toolu_A`'s prompt prefixed with one `\n`, `handoff.py agents --handoff <H> --session <S>` exited 0 and printed exactly arm 9's two lines; the base `handoff.py` over the same session exited 1, "no Agent call … opens its prompt with the marker line", so the criterion discriminates. `grep -n "extract_prompt_marker"` printed the matcher's call at `tools/roles/handoff.py:820`, its docstring at `:43`, and the README's sentence at `tools/roles/README.md:88`.
- AC2 — `agent-cap.js` — over the task part of a `gov-researcher` render in F, the spawn guard and `extract_prompt_marker` both admitted v1, v2 and v3 and both refused v4 and v5, the guard exiting 2 with rule 6's "carries 0 gov:handoff marker lines".
- AC3 — `role-stand-in-waiver.txt` — in F: step 1 exit 0 with `0 stand-in waiver(s), 0 stand-in declaration(s)`; step 2 exit 1 naming `role-stand-in-waiver.txt`, the prompts folder empty; step 3 exit 0 printing `memory/builds/tFix/prompts/2026-10-13-prompt-TOOL-tFix-1-1-researcher-stand-in.md`; step 4 exit 0 with one `roles: note: stand-in waiver` line and `1 stand-in waiver(s), 1 stand-in declaration(s)`; step 5 exit 1 with one `R15` line naming that declaration, `gov-researcher` and `tFix`; step 6 exit 1 with one `R15` line carrying `stale`; step 7 exit 1 with eight `R15` lines naming registry lines 2 to 9 once each.
- AC4 — `gov-orienter.agent.md` — in F: step 8 exit 1 with one `R13` line naming `tools/roles/agents/gov-orienter.agent.md`; step 9 exit 1 with one `R14` line naming `{{MEMORY_ROOT}}/builds/<slug>/spec/`; step 10, the conf holding its `CHARTER` line alone, exit 2 naming `MEMORY_ROOT`.
- AC5 — `FLOOR_ASSERTIONS=33` — in F after arm 9's two `--handoff --write` runs, `handoff.py agents --run wf_00000001-aaa --session <S> --write` exited 0 and printed exactly A9L3, A9L4 and A9L5; the agent ledger then held five `- ` lines, each of arm 9's two and these three once, the links re-rooted to `../prompts/`; the grep printed 1.
- AC6 — `readCharterShapes` — over the three copies in `%TEMP%/t25d`, `extract_microformat_shapes` and `readCharterShapes` printed the same `agent` and `returned` for each: the charter's own for c1, D2 for c2, `none` twice for c3. The base reader kept the charter's own `agent` for c2 and found the part-line opener of c3, so both of the criterion's red cases are live. `grep -n "whole line"` printed `tools/roles/roles_lib.py:8` and `:224` and `tools/roles/README.md:84`.
- AC7 — `tools/check-microformats.sh:9:9` — the §4 `uniq -d` probe over `coding-governance-agents.template.md` printed nothing, with 13 definition lines selected and one whole-line opener; `grep -c "^FLOOR_ASSERTIONS=20$"` printed 1, and the conf search printed 1. The `bash -c` probe of the new `case` over the heads `agent gates agent returned agent gates a* "a b"` printed `fail 9` once for `agent` and once for `gates`, nothing for the third `agent` or for the glob `a*`. The three gate runs are owed to the main loop, as the criterion's `permission:` states.
- AC8 — `checkAgentLines` — the `git grep -c` over `memory/builds/aOrientedCast/build` printed this record alone with the count 2; the §4 node probe printed `[]`, then the charter-shape message for `direct/a1`, then `no agent line for agent a1, which this turn dispatched`; the old-marker search printed nothing, and the twin, `v` read as `1.106` from `tools/unattended/unattended.sh`, listed the kit's files and rendered copies, that file among them.
- AC9 — `its own records break by quoting the pattern` — after `gotchas.py --write`, the count printed 1 for the record and 1 for `memory/gotchas/INDEX.md`; the `TOOL-aOrientedCast-2[12]` count printed 2.
- AC10 — `the only contract` — the count printed 0; the term grep printed a line for each of its eight terms inside `## Shared seams`, at lines 128 to 141. It also printed line 52, a `gate manifest` sentence in the feature's own prose that predates this unit and is no outside-read entry.
- AC11 — `KIT_ROLES_VERSION = "1.4"` — the count printed 1; `gov:kit roles@1.4` counted 1 in `tools/roles/README.md` and in `tools/roles/SKILL.template.md`, and 0 in `.claude/skills/build/SKILL.md`, which the 1.3 search lists alone: that render is the main loop's second pass, as the criterion's `permission:` states.
- AC12 — `--write` — in F, AC1's command left `git hash-object` of the ledger unchanged and its stderr named `--write`, as did `--run` without the flag, the `build/` listing unchanged too; with `--write` the ledger gained its three lines (AC5); the doc count printed at least 1 for `tools/roles/README.md`, `help/roles.md` and `tools/roles/SKILL.template.md`.
- AC13 — `['EOF', 'EOF']` — the probe printed `['EOF', 'EOF']` for `tools/check-microformats.sh`; over a scratch copy carrying rev-4's heredoc-fed loop over `sort | uniq -d` it printed a third `EOF`, so the criterion discriminates.

## Criteria amended in closed specs

These correct two criteria of CLOSED specs that misstate what was built, review items L5 and L6 of
the second closing review, round 1. Neither spec is reopened; each correction lives here, one hop
from the criterion through that spec's records region.

### TOOL-aOrientedCast-21 AC2

As written (spec 21, `:278-281`): with its last field cut, the agent line blocks and the reason
carries "does not match its charter shape". What the code does, by `checkAgentLines`
(`tools/hooks/format-guard.js:429-450`): a line still ending `/a1` with only the `run ` label cut,
`· direct/a1`, gets the shape message; a line with the run field cut whole names no agent, so it
gets "no agent line for agent a1, which this turn dispatched". The observation of record is the
suite's staged break, `${A1/run direct/direct}` in `tools/hooks/format-guard.test.sh`, and the
deviation was recorded only in a Decided trailer of commit `6fb62ffa5`. The probe that stands,
observed at this unit's build as `[]`, then the shape message, then the no-agent message:

```bash
node -e "
const g = require('./tools/hooks/format-guard.js')
const { shapes } = g.readCharterShapes('.')
const req = [{ head: 'agent', agentId: 'a1', why: 'dispatched' }]
const A = '- agent — gov-builder · effort high · model m · TOOL-tBuild-1 · prompt [x.txt](x.txt) · writes product · gates none'
for (const t of [A + ' · run direct/a1', A + ' · direct/a1', A]) console.log(JSON.stringify(g.checkAgentLines(g.scanMessageLines(t), shapes, req)))
"
```

### TOOL-aOrientedCast-22 AC6

As written (spec 22, `:263-267`): a search for the old version marker with no pathspec prints
nothing. That never holds for a correct build: the search spans the spec and its ledger, which
quote the pattern. The observation that stands, the first search printing nothing and the second
listing the kit's files and their rendered copies, `tools/unattended/unattended.sh` among them:

```bash
git grep -l "gov:kit unattended@1.104" -- ':!memory/builds'
v=$(sed -n 's/^KIT_UNATTENDED_VERSION=\([0-9.]*\).*/\1/p' tools/unattended/unattended.sh)
git grep -l "gov:kit unattended@$v" -- ':!memory/builds'
```

The second search is the liveness twin, since a pathspec excluding everything would print nothing
for both; its `v` is the bare version, because the constant's line ends in a `# gov:kit` comment
that would otherwise ride into the pattern and match nothing.
