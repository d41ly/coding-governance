**Serves:** journal TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 TOOL-aOrientedCast-19 PLAY-aOrientedCast-2

# Spec handoff — the roles join the v4.3 charter as a rendered section

## Role

You are a code architect writing the specification for five units of one design the owner has
already decided. You are not writing any code. A builder will build from your spec alone. Each
unit's design is the narrowest change that delivers its mechanism and seams into the code this build
and the playbook kit already hold. Verify every claim about current code by reading it, and cite path
and line. A choice you cannot derive is a fork, resolved by M3 of the build method and marked
`RESOLVED (agent, 2026-10-13, delegated)`; the owner's four answers below are not forks and are not
re-opened. You run no gate and no self-test; the only checks you may run are memory hygiene and the
lexicon. You write only the spec files of the units your roster names; the table below shows all
five so you see the interfaces between them, and a sibling writer may hold the rest. Spell every
name, path and key another unit defines exactly as that unit's row does. You do not commit, and you
do not regenerate any index.

## Task

**Repository:** `C:/projects/coding-governance/.claude/worktrees/deterministic-attended-workflows-943570`.

**The design, decided by the owner:**
`memory/builds/aOrientedCast/prompts/2026-10-13-prompt-TOOL-aOrientedCast-1-4-owner-addendum.md`.
Read it whole. Its four answers are settled:
1. a role cites section 1 rule TAGS, and its agent type carries those rules verbatim;
2. every agent type carries the rendered `## Protocols` section whole, and no role file names a
   protocol path;
3. an inline stand-in for a role is legal only where the tool or run cannot spawn a sub-agent at
   all, AND it needs an owner waiver row graded like the other waiver registries;
4. these units build in this run.

**Also read:** `memory/guides/BUILD-METHOD.md`; the "Invariants for every unit" section of
`memory/builds/aOrientedCast/prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md`, which
binds you except for its order table, replaced below; `memory/TEMPLATE-SPEC.md`; `tools/roles/README.md`;
`tools/playbook/README.md`. Then the CLOSED specs whose code each unit changes: TOOL-aOrientedCast-1,
-2, -3, -8, -10, -13 and PLAY-aOrientedCast-1, under `memory/builds/aOrientedCast/spec/`.

**Facts already verified on this tree**, so you start from them rather than re-derive them:
- Main's charter is template v4.3: `coding-governance-agents.template.md`, rendered into `AGENTS.md`.
  It has no `## §<n> — ` heading. Section 1 is `## 1. Governing practices`: one-line rules, each
  opening with a bracketed tag such as `- [land] `, inside a `<!-- one-line -->` region. Section 3
  holds `## Tools to rely on` and `## Protocols — read the one whose trigger holds`, whose bullets
  sit in `kit:<name>` fences.
- `tools/roles/roles_lib.py` reads charter sections only by `SECTION_RE` (line 49) in
  `extract_charter_sections` (line 134), called from `check_roles.py:117`, `handoff.py:323` and
  `render_agents.py:115`. On this tree `check_roles.py` reports one R4 defect per role `charter` id
  and `render_agents.py --check` refuses on the first. `handoff.py render` refuses too; its
  `harness-args` and `stage-efforts` verbs still answer.
- The playbook renderer's derived placeholders are the `PROBES` table at
  `tools/playbook/render_playbook.py:528`, `derive_node_table` at line 421 the nearest example, and
  each is declared as a `[[placeholder]]` with `class = "derived"` in
  `tools/govkit/entries/playbook.kit.toml`; a `kit =` key there makes one reachable only when that
  kit's block survives. A one-line region refuses a rule past 200 characters
  (`render_playbook.py:126`).
- An adopter's template is a SEED that `govkit update` never rewrites (the comment above the
  LEGACY placeholders in `playbook.kit.toml`). An adopter may therefore render a v3.x charter, with
  `§` headings and no tagged rules, under the newest roles kit. Each unit that reads the charter
  must state what it does on such a charter. That is a fork if the design does not decide it.

**The five specs**, all under `memory/builds/aOrientedCast/spec/` named
`2026-10-13-spec-<unit id>.md`. Each is status `OPEN`, `rev-1`, `node a`, base
`646d4a73581393acbf42f33864a9808c96d00a0c`, Tier-2, with the `order` verb shown:

| Unit | Order | Streams | Mechanism |
|---|---|---|---|
| TOOL-aOrientedCast-16 | 16 | tooling | A role's `charter` key is replaced by `rules`, naming section 1 tags. `roles_lib` becomes the one reader of the tagged rules and of the `## Protocols` section. Agent types and handoffs carry the cited rules verbatim and the Protocols section whole. The checker's R4 is re-keyed to tags. Choose each role's tags from the rules' text, and name them in the spec. |
| TOOL-aOrientedCast-17 | 17 | tooling | Two role front-matter fields, `mandatory` and `output`, and their checker rules. A role called mandatory must belong to a workflow whose `enforced-by` names a hook, unless its line says it is unenforced. A writer role's `output` must name its write class's folder. A `roster` verb prints one line per role: what it does, when it is mandatory, and where its output goes. It refuses a line past 200 characters. |
| TOOL-aOrientedCast-18 | 18 | tooling | A derived `ROLE_ROSTER` placeholder, declared with `kit = "roles"`, whose probe runs the roles kit's `roster` verb. The probe names the roles kit by a render token, never by literal path; the hooks README states that ban. |
| TOOL-aOrientedCast-19 | 19 | tooling | The owner waiver registry for an inline stand-in: a row grammar that is dated, attributed, reasoned and names the role, and its grader, beside the other registries under `memory/project/`. Also how a stand-in is declared so the grader has something to join. |
| PLAY-aOrientedCast-2 | 20 | playbook | The template's `[roles]` rule in section 1, inside the `kit:roles` fence. It names the no-spawning exception and the waiver registry. Add a `## Agent roles — hand the work to its role` subsection between Tools and Protocols, holding `{{ROLE_ROSTER}}` in a one-line region inside the `kit:roles` fence. The roles line under Tools shrinks to its `/build` clause. Then the template version, the re-render, the kickoff manifest's `last-audit`, the template-size high-water and `help/roles.md`. |

**Kit versions:** one bump per touched kit, in the last unit of this set that moves that kit. Name
each carrier: read `tools/check-kit-versions.sh` and `tools/govkit/govkit.py` to find them, without
running either.

Each new arm names its staged break. Its red-first observation belongs to the main loop at the close,
because builders run no gate. Each §6 command is one a builder may run: a fixture, a probe, or a
checker on its own scratch copy.

**Return:**
- `authored`: the paths you wrote;
- `forks`: each fork with the option taken;
- `refused`: anything you could not specify, with why;
- the memory hygiene exit status over your files, if you ran it.
