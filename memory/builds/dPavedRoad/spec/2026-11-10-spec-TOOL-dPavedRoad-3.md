# TOOL-dPavedRoad-3 — the handoff carries the brief's prompt as a `brief:prompt` block

**Status:** CLOSED · rev-1 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-build-TOOL-dPavedRoad-3-ledger.md](../build/2026-11-10-build-TOOL-dPavedRoad-3-ledger.md) | journal | — |
| [2026-11-10-prompt-TOOL-dPavedRoad-1-brief.md](../prompts/2026-11-10-prompt-TOOL-dPavedRoad-1-brief.md) | research | TOOL-dPavedRoad-1 TOOL-dPavedRoad-2 TOOL-dPavedRoad-4 |
| [2026-11-10-review-TOOL-dPavedRoad-1-closing-diff-round1.md](../reviews/2026-11-10-review-TOOL-dPavedRoad-1-closing-diff-round1.md) | diff-review | TOOL-dPavedRoad-1 TOOL-dPavedRoad-2 TOOL-dPavedRoad-4 |

<!-- /gen:spec-records -->

## 1. Goal

A spec writer spawned with a rendered handoff gets the brief's `## The prompt` section, the owner's
own words or the finding a run's brief records there, as a `brief:prompt` block in its Task section.
In dSafePassage three writers needed that text sent by SendMessage after the spawn, because the
renderer reads only the `### <sub-head>` blocks under `## The brief` and drops the prompt.

## 2. Scope (IN)

Line numbers are read at `ae6735c1`.

- **S1** — `READ_KEYS` in `tools/roles/roles_lib.py:36-40` gains `brief:prompt`, so the catalogue
  checker's R3 (`tools/roles/check_roles.py:201-207`) admits it in a role's `reads`. Observed by AC3.
- **S2** — `render_handoff` reads `brief:prompt` from the brief record's `## The prompt` section,
  through the existing `extract_card_section`. Every other `brief:` key still reads its
  `### <sub-head>` under `## The brief`. An empty prompt section refuses a required key by name, as
  any empty `brief:` value does today. Observed by AC1 and AC2.
- **S3** — `tools/roles/agents/gov-spec-writer.agent.md:7` reads `brief:prompt` first and REQUIRED,
  ahead of `brief:goal`. Observed by AC1 and AC3.
- **S4** — The roles catalogue region of `tools/roles/README.md` is re-rendered, so the
  `gov-spec-writer` row's reads cell carries `brief:prompt`. Observed by AC4.
- **S5** — Three documents say where `brief:prompt` comes from: the module docstring of
  `tools/roles/handoff.py`, the renderer prose of `tools/roles/README.md` and step 3 of
  `help/roles.md`. Observed by AC5.
- **S6** — `tools/roles/adopt-roles.test.sh` gains arm 22, and `FLOOR_ASSERTIONS` moves from 51 to
  53. NOT OBSERVED by a pass: it is a suite arm, declared on a `New arm:` line, which the main loop
  observes RED and then GREEN at the close.

## 3. Non-goals (OUT)

- No other role gains `brief:prompt`. The measured cost was the spec writer's. A builder or a spec
  reviewer that needs it later adds one key to its `reads` line.
- No key for `## Drawn from the session` or `## Owner confirmation`. The brief names only
  `## The prompt`.
- No change to the build harness's spec-writer prompt in `tools/workflows/unattended-build.js`. That
  stage hands each writer the brief's path, and the writer reads the whole file, prompt included.
  This unit serves direct spawns, whose prompt is a rendered handoff.
- No change to `resolve_brief_record`, to `extract_brief_section`, or to what
  `extract_card_section` returns for a card.
- No secret scan of the copied text. The module docstring already states that the renderer does not
  check for one (`tools/roles/handoff.py:71-74`), and the prompt comes from a committed record.
- No kit version moves on the branch. The lander's `mint` moves it.

### Edges

none

## 4. Design

### Where the text comes from

The brief record is the file `resolve_brief_record` picks (`tools/roles/handoff.py:283-294`): the
`--input prompt=` path, else the one file under the build's `prompts/` that carries both a
`## The prompt` line and a `## The brief` line. So every record the renderer reads already holds the
prompt heading. Its shape is the kickoff checker's `BRIEF_SKELETON`
(`skills/session-kickoff/manifest-check.sh:119-167`), where `## The prompt` is a `##` section of its
own, above `## The brief`.

`extract_brief_section` (`tools/roles/handoff.py:210-222`) reads only a `### ` sub-head under
`## The brief`. So today `brief:prompt` would look for a `### prompt` sub-head, find none, and
refuse. A direct `render_handoff` call whose `reads` was `brief:prompt`, against a scratch brief
holding a filled prompt, refused that way at `ae6735c1`.

`extract_card_section` (`tools/roles/handoff.py:152-163`) already does what this key needs. It
returns the lines under the last `## <heading>`, up to the next `## ` heading or READY line,
verbatim, with blank edges trimmed, and returns None when the heading is absent. Called on the
brief's text with the heading `The prompt`, it returns the prompt's body.

### The change

**S1.** The `brief:` list at `tools/roles/roles_lib.py:39` becomes
`("prompt", "goal", "items", "acceptance", "gates", "non-goals")`.

**S2.** The brief loop at `tools/roles/handoff.py:374-378` dispatches on the field name:

```python
        for k in reads:
            if k.startswith("brief:") and brief:
                # TOOL-dPavedRoad-3: the owner's words are the record's own `## The prompt` section,
                # read as a card section is; every other brief key is a sub-head of `## The brief`.
                field = k.rstrip("?")[6:]
                section = (extract_card_section(brief_text, "The prompt") if field == "prompt"
                           else extract_brief_section(brief_text, field))
                if section is not None:
                    values[k.rstrip("?")] = section
```

The value then takes the path every value takes (`tools/roles/handoff.py:382-396`). A filled prompt
becomes a `### brief:prompt` block. An empty one refuses the required key with the existing
`brief:prompt — the brief record <path> carries no single filled value for it` line, and the
handoff is not written. The docstring of `extract_card_section` gains one clause: it also reads a
brief record's `## The prompt` (TOOL-dPavedRoad-3).

**S3.** Line 7 of `tools/roles/agents/gov-spec-writer.agent.md` becomes:

```text
reads: brief:prompt, brief:goal, brief:items, brief:acceptance, brief:gates, brief:non-goals, input:spec?, task:reuse?, card:route?
```

The key is REQUIRED, like every other `brief:` key this role reads. Of 383 records under the tree's
`prompts/` folders that carry both headings, none has an empty prompt section and none has a READY
line inside it (PINNED, read at `ae6735c1` on 2026-11-10). So making it required refuses no record
the tree holds. It comes FIRST, because the brief's other blocks distil it.

**S4.** `python tools/roles/check_roles.py --write` re-renders the catalogue region
(`tools/roles/check_roles.py:4`, `tools/roles/check_roles.py:114`). The role-gate hook compares a
command with a leg's argv word for word and by length (`tools/hooks/scratch-guard.js:1378`), so
this `--write` form is not the `roles catalogue` leg and a builder may run it.
`python tools/roles/render_agents.py --write` moves nothing: neither
`.claude/agents/gov-spec-writer.md` nor `.claude/roles.json` carries `reads`, read at `ae6735c1`,
and its drift check compares bytes (`tools/roles/render_agents.py:229-242`).

**S5.** Three sentences:

- The docstring at `tools/roles/handoff.py:59-60` reads: `brief:` the `### <sub-head>` under the
  brief record's `## The brief`, and `brief:prompt` that record's `## The prompt` section.
- `tools/roles/README.md:47-48` reads: a `brief:` key from the build's brief record, `brief:prompt`
  from its `## The prompt` section and every other one from its `### <sub-head>` under
  `## The brief`.
- `help/roles.md:22-24` gains a sentence after the one that ends with the `--input` values: "A
  spec writer's task also carries the brief's `## The prompt`, the owner's own words, as its
  `brief:prompt` block."

Every new line stays within 100 columns.

**S6.** Arm 19 follows arm 18 (`tools/roles/adopt-roles.test.sh:723-729`) and runs in a fresh
`build_fixture` (`tools/roles/adopt-roles.test.sh:86-95`). It writes a brief record under
`$FX/$MR/builds/bx/prompts/` holding the five sub-heads and a two-line prompt, one quoted line and
one unquoted attribution line. It then imports the fixture's own `handoff.py` and calls
`render_handoff` with the fixture charter. The keys are the fixture kit's `gov-spec-writer` reads,
read through `roles_lib.load_roles` and filtered to the `brief:` family, so the arm proves the
shipped role and not a typed key set. The filter exists because the `task:` family needs the kickoff
checker, which a roles-kit fixture does not hold. Two assertions:

- `arm 22 the spec writer's handoff carries the brief's prompt verbatim`: the task part holds
  `### brief:prompt`, a blank line, then both prompt lines exactly, before `### brief:goal`.
- `arm 22 an empty prompt refuses by name`: with the prompt section emptied, `render_handoff`
  raises, and the first line opens `brief:prompt — `.

The floor comment gains `+2 for arm 22 (TOOL-dPavedRoad-3)`, and `FLOOR_ASSERTIONS` moves from 51
to 53 (`tools/roles/adopt-roles.test.sh:82`, PINNED at `ae6735c1`).

### The two probes

Both run from the repository root and write nothing under it. Each is saved under the run's scratch
directory and removed after the pass.

`tdp3-render.sh` renders the real role against this build's brief, printing the block alone:

```bash
B=memory/builds/dPavedRoad/prompts/2026-11-10-prompt-TOOL-dPavedRoad-1-brief.md
python tools/roles/handoff.py render --role gov-spec-writer --build dPavedRoad --unit TOOL-dPavedRoad-3 \
  --input "prompt=$B" --stdout --part task | sed -n '/^### brief:prompt$/,/^### brief:goal$/p'
```

At `ae6735c1` it prints nothing, because the role reads no `brief:prompt`.

`tdp3-probe.py` takes the repository and a scratch fixture directory as its two arguments. It calls
`render_handoff` directly, so the fixture needs no git repository:

```python
import pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
repo, fx = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve()
sys.path.insert(0, str(repo / "tools" / "roles"))
import handoff, roles_lib as lib
reads = lib.load_roles(handoff.KIT_DIR)["gov-spec-writer"]["keys"]["reads"].split(", ")
print("vocabulary %s, first read %s" % ("brief:prompt" in lib.READ_KEYS, reads[0]))
keys = {"reads": ", ".join(k for k in reads if k.startswith("brief:"))}
brief = fx / "memory" / "builds" / "bx" / "prompts" / "2026-11-10-prompt-TOOL-bx-1-brief.md"
brief.parent.mkdir(parents=True, exist_ok=True)
body = "".join("### %s\n\n%s text\n\n" % (h, h) for h in ("Goal", "Items", "Acceptance", "Gates", "Non-goals"))
for prompt in ("> owner words, verbatim\n— owner, 2026-11-10\n", ""):
    brief.write_text("# Brief\n\n## The prompt\n\n%s\n## The brief\n\n%s" % (prompt, body), encoding="utf-8")
    try:
        task = handoff.render_handoff(fx, "memory", lib.resolve_charter_path(repo), "gov-spec-writer", keys,
                                      "bx", "TOOL-bx-1", None, {}, None)[2]
        i = task.find("### brief:prompt\n")
        print("rendered " + (repr(task[i:task.index("\n###", i + 1)]) if i >= 0 else "no brief:prompt block"))
    except lib.RolesError as e:
        print("refused " + str(e).split("\n")[0][:40])
```

Run at `ae6735c1`, it printed `vocabulary False, first read brief:goal`, then
`rendered no brief:prompt block` twice.

### Inventory

No new function, type or module. The arm's shell locals take the `19` suffix the suite's arms use,
as `_v18` does, and no naming cell grades a suite local. The arm label opens `arm 22`.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/agents/gov-spec-writer.agent.md`
- `tools/roles/README.md`
- `help/roles.md`
- `tools/roles/adopt-roles.test.sh`

### Rollout

One pass. The write set is the six files above, and it holds no generator together with its output
other than `check_roles.py --write` rewriting its own README region. Siblings 1 and 2 of this build
also work under `tools/roles/`; whether their write sets meet this one is the dispatch's question,
and a shared file sequences the passes.

The handoff's `task-sha` for a spec writer moves, because its Task section gains a block. A
handoff rendered before this unit still checks clean, since `check` hashes the file's own bytes.

### Alternatives rejected

- A new extractor for `##` sections in the brief. `extract_card_section` already returns exactly
  that, and a second copy would be a second answer to one question.
- Reading `brief:prompt` as a `### prompt` sub-head. No brief record carries one, and
  `BRIEF_SKELETON` puts the prompt in its own `##` section.
- An OPTIONAL key. Every brief record the renderer can pick holds the heading, and none of the 383
  holds it empty. An optional key would hide the one case worth refusing: a brief whose prompt was
  never filled.

## 5. Production-readiness checklist

- security — N/A: no new write path or surface. The renderer already writes its handoff under the
  build's `prompts/` folder, beside the brief it now copies from, so no text reaches a place it was
  not already committed.
- perf / scale — one more scan of a brief text already loaded. The largest prompt section of the
  383 records is 25505 bytes, in aTrimmedHook's brief, PINNED at `ae6735c1`. A writer's Task
  section grows by its own brief's prompt and nothing more.
- error / empty / loading states — an empty prompt refuses the required key by name and writes no
  handoff. An absent brief record refuses as it does today.
- observability — the refusal names `brief:prompt` and the record's path on stderr.
- risks — a prompt holding a column-0 `READY — ` line is cut there, because `extract_card_section`
  stops at one. None of the 383 records holds one. A prompt left as the skeleton's `> <...>` line
  passes as filled, because the placeholder test matches only a bare `<slot>`.
- testing — arm 22, observed RED then GREEN at the close, and the probes of the acceptance criteria.
- migration — none. A brief record needs no change, and a role that does not read the key renders
  as before.
- user docs — `help/roles.md` step 3 names the block (S5).

## 6. Acceptance criteria

Each probe is the Design section's fenced block of that name. No probe runs a gate or a suite.

- **AC1** — When `bash tdp3-render.sh` runs from the repository root, it prints a
  `### brief:prompt` line, a blank line, then the brief's prompt line opening
  `> Can we analyze this build for any refusals/problems`, and ends at `### brief:goal`.
  Red when: the role does not read the key, or the key reads a `### prompt` sub-head, and the probe
  prints nothing, as it does at `ae6735c1`.
- **AC2** — When `python -B tdp3-probe.py <repo> <scratch fixture>` runs, its second line is
  `rendered '### brief:prompt\n\n> owner words, verbatim\n— owner, 2026-11-10\n'` and its third
  opens `refused brief:prompt — the brief record`.
  Red when: the dispatch is reverted, so both lines read `rendered no brief:prompt block`, or the
  extraction runs past `## The brief`, so the second line carries `### Goal`.
- **AC3** — When `python -B tdp3-probe.py <repo> <scratch fixture>` runs, its first line is
  `vocabulary True, first read brief:prompt`.
  Red when: `READ_KEYS` lacks the key or the role's `reads` does not open with it, as at
  `ae6735c1`, where it prints `vocabulary False, first read brief:goal`.
- **AC4** — When `grep -c 'spec | brief:prompt, brief:goal' tools/roles/README.md` runs after the
  catalogue is re-rendered, it prints `1`.
  Red when: the region was not re-rendered, so it prints `0` and the `roles catalogue` leg reds at
  the close.
- **AC5** — When `grep -c 'brief:prompt' help/roles.md tools/roles/handoff.py` runs, each file
  counts at least `1`.
  Red when: the help page or the docstring does not name the key, as at `ae6735c1`, where both
  count `0`.

## 7. Gates

`policy fixtures` · `roles catalogue` · `roles adopter self-test` · `roles render wiring` · `docs` · `memory hygiene`

New arm: tools/roles/adopt-roles.test.sh · covers AC2 · arm 22, staged by reverting the dispatch so `brief:prompt` reads a `### prompt` sub-head, which renders no block and lets the empty prompt pass · `FLOOR_ASSERTIONS` 51 to 53

`policy fixtures` is owed because its guard names `tools/roles/handoff.py` and
`tools/roles/roles_lib.py`. The guards on `{prefix}/` are broad and excluded. `roles catalogue`
re-observes AC3 and AC4 through R3 and its region compare. This spec's author may run only
`memory hygiene` and the lexicon, so every other verdict is the close's.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft.

## 10. Reuse audit

The seam is `extract_card_section` (`tools/roles/handoff.py:152-163`), reused unchanged for the
prompt's `##` section, inside the brief loop of `render_handoff` (`tools/roles/handoff.py:368-378`).
The key joins the one vocabulary, `READ_KEYS` (`tools/roles/roles_lib.py:36-40`), which R3 already
grades. `python tools/codebase-map/reuse_lookup.py "render the brief record's owner prompt section
into a role handoff task block"` ranked generic name stems only (`records`, `render`), and named no
brief reader, so the seams above were found by reading `tools/roles/handoff.py`. Recall returned
`TOOL-aOrientedCast-2`, whose spec defines a `brief:` key as a sub-head under `## The brief` and
says nothing about the prompt, and the dBoundRoles reuse scouts, which cite the brief loop. No
record rules against reading the prompt. One hit was stale: `TOOL-dBoundRoles-13` cites the
reads walk of `render_handoff` as lines 330 to 396, and at `ae6735c1` it runs from 337 to 409.

Recall terms used: `python tools/memory-recall/query.py "should a role handoff carry the brief's owner prompt into its task section" --terms "handoff brief record prompt task section reads key spec-writer render_handoff brief:goal extract_brief_section owner"`
