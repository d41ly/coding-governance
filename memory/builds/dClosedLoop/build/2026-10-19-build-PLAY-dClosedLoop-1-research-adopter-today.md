# Research: how an adopter adds to or changes gov's instructions today, and what an update does to the change

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 118's return, verbatim, except that a title line would be demoted to keep one H1 per record, and that an id of another build that led a list item carries the word "id" before it, so hygiene check 13 does not read it as defined here. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-1-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-adopter-instructions.md`.

---

The edit-survival question is answered for every instruction-bearing artifact. Today an adopter's edit survives a gov update only when it sits outside the bytes gov's renderers rewrite. Nothing in gov reads an edit tag. Edits to rendered files are overwritten under a single word, `re-rendered`, and no line of the update output names the lost edit. Gov's own repository never runs this path, because it has no install receipt and is never `update`d.

**Fixture.** I cloned the repo into the scratchpad under the system temp root and installed into empty git repos with `govkit intake --all` and `apply --all` at gov `b61ec1c49`, with a custom `[charter] adopter_rules` line. I committed one sentinel edit per artifact, then ran `govkit update` (read-only) and `update --write` from `a0b1a06c4` (HEAD). Separate copies tested a conflicting edit (tC), a tagged edit (tE) and pre-existing files (tA). All fixtures are deleted. `git status` shows no change of mine; the two untracked research records under `memory/builds/dClosedLoop/build/` are other researchers'.

Getting a full install needed manual steps first; these are side findings:
- The kickoff seed created `memory/` before memory-tree's adopter ran, which then refused (`memory/ exists without a memory-tree marker`).
- agent-instructions ran before the charter render existed and exited 2.
- At `9df98d1eb` the roles render refused (`charter §3 names no section`), which is why I based on `b61ec1c49`.

## 1. Population, and the command that derived it

```
python3 tools/govkit/govkit.py plan --target <fixture> --all
  | grep -E '^\s+(write|SIDE|ORDER|COVER|BLOCK)' | grep -v '\[attributes\|\[hole\|\[project-owned\|\[generated'
  | grep -E '\.md |\.agent\.md|hooks/.*\.js|policy\.toml|\.claude/' | grep -v -E 'README\.md|fixture|INVENTORY'
```

I added each descriptor's `[[regenerate]] writes`, `[[generated]]` and adopter outputs, which `plan` does not print as rows. Plan totals were `252 write(s), 129 order(s), 19 side-effect(s), 2 covered, 3 blocked, 0 forked`.

| Class (role) | Members |
|---|---|
| Written by an adopter, **no receipt row** | `AGENTS.md` (playbook-render `[[regenerate]] writes = ["AGENTS.md"]`); `CLAUDE.md`, `GEMINI.md` or `.gemini/settings.json`, `.github/copilot-instructions.md`, `.cursorrules`, `.windsurfrules` (`alias_path()` in `adopt-agent-instructions.sh`); `.claude/agents/*.md` and `.claude/roles.json` (roles `[[generated]]`, written by `render_agents.py`) |
| `seed` | `coding-governance-agents.template.md`; `memory/guides/SESSION-KICKOFF.md` (from `MANIFEST-TEMPLATE.md`); `tools/roles/house/gov-*.md` ×10 and `policy.toml` |
| `rendered` | `.claude/skills/{cleanup,drift-audit,lexicon,memory-recall,runlog,build,unattended}/SKILL.md`; `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `memory/guides/{BUILD-METHOD,ANNOTATION-STYLE}.md`; `memory/guides/REVIEW-PROTOCOL.md`; `memory/guides/UNATTENDED-{PROTOCOL,VERBS,STOPS,ASKS}.md` and `PLAYBOOK-TEMPLATE.md` |
| `engine` (the instruction sources) | every `*.template.md` and `SKILL.template.md`; `tools/roles/agents/*.agent.md` ×10; `review-harness/orient.agent.md`; `codebase-map/reuse-lookup.agent.md`; `lexicon/LEXICON.md`; hook refusal text in `tools/hooks/{agent-cap,scratch-guard,format-guard}.js`, `tools/unattended/{gate-guard,stop-guard,stall-recorder}.js`, `process-monitor/procmon-hook.js` (from the 12 `*.fragment.json` rows) |
| machine scope, `link = true` | `skills/session-kickoff/SKILL.md` → `{user_skills}/session-kickoff`, one junction shared by every adopter on a machine |
| `merged` (no writer) | `.claude/settings.json` |
| Not shipped by any kit | path rules: no file under `tools/` or `skills/` ships one under `.claude/rules` (grep hits only `check-playbook-parity.sh:336`). Handoff prompts are composed in code (`handoff.py`), not a template file. No "work-order" template exists (grep for `work.order` over `tools` and `skills` returns nothing). |

## 2. One row per artifact

The update result column is measured on the fixture unless marked "read".

| Artifact | Source → renderer | Seams today | Direct edit at next update |
|---|---|---|---|
| `AGENTS.md` inside `<!-- gov:playbook -->` | seed template + overlay → `render_playbook.py` (`build_region`) | `[answers]` for asked placeholders; `[charter] adopter_rules` → section 2; `drop_blocks`; `kits` | **Overwritten, silently.** `CUSTOM-AGENTS-IN` was removed and no line of the update output names `AGENTS.md`. Before an update, the `playbook render wiring` leg reds on the drift (read: `--check` prints `DRIFT`). |
| `AGENTS.md` outside the region | adopter's own text | authored prose above or below the region | **Survives** (`CUSTOM-AGENTS-OUT`). |
| `coding-governance-agents.template.md` | seed copy of gov's template | edit the seed | **Survives and renders** (`CUSTOM-TEMPLATE` reached `AGENTS.md`). But the row reads `reseed-available` and the charter stays `<!-- governance-template: v4.3 -->` while gov ships 4.4. Every seeded charter freezes, edited or not (`govkit.py:9611-9613`). |
| `CLAUDE.md` | agent-instructions adopter | any text beside an `@AGENTS.md` line counts as wired (`is_import`) | **Survives** (`CUSTOM-CLAUDE`). Rendered role agents carry `omitClaudeMd: true` (`render_agents.py:132`), so text here does not reach them through CLAUDE.md. |
| `.github/copilot-instructions.md` | copy of `AGENTS.md` | none | **Survives**, but it is now stale against the new `AGENTS.md` (`cmp` differs). The update printed `verify agent-instructions: not-run — this run moved no path this kit owns`. Its leg reds with "stale copy — re-run with --force", and `--force` destroys the edit (measured: `PRE-COPILOT` gone). |
| `.claude/skills/*/SKILL.md` | `SKILL.template.md` → each kit's adopter | conf values only, e.g. `.lexicon.conf` VERBS → `{{VERBS_TABLE}}` | **Overwritten when the kit is touched.** `CUSTOM-SKILL-BUILD` and `CUSTOM-SKILL-UNATT` were gone. The edited lexicon skill survived only because lexicon was not touched, yet the update printed `re-rendered` for it anyway. |
| `.claude/agents/*.md` | base `agents/*.agent.md` + `house/*.md` + `policy.toml` → `render_agents.py` | house overlay (append-only, under `## House rules`); `policy.toml` (effort, gates) | **Overwritten** (`CUSTOM-AGENT:` absent). No line names it. Its `roles render wiring` leg byte-compares these files (read: descriptor). |
| `tools/roles/house/*.md` | seed | the seam itself | **Survives**, reported `patched [seed]`, and was rendered into `.claude/agents/gov-builder.md` (`CUSTOM-HOUSE`). |
| `tools/roles/agents/*.agent.md` | engine | edit gov's file | Non-conflicting edit: `diverged`, three-way merged, survived and rendered (`CUSTOM-ROLEBASE`). Conflicting edit (tC): `the three-way conflicts — left untouched, order written` and `kit 'roles' was HELD BACK … ROLLED BACK`, so the whole kit stops updating. |
| `memory/HYGIENE.md`, `TEMPLATE-SPEC.md`, `guides/BUILD-METHOD.md`, `ANNOTATION-STYLE.md` | `*.template.md` → `adopt-memory-tree.sh --render` (`render_doc`, writes the whole file) | conf: `READINESS_ROWS`, `INDEX_CAP_LINES`, `ENTRY_CAP_UNIT` (one line each; a newline is refused) | **Overwritten**, labelled `re-rendered` (`CUSTOM-HYGIENE`, `-SPECTPL`, `-METHOD` gone). memory-tree's `[check]` is `none`, so nothing reds before the update. |
| `memory/guides/UNATTENDED-*.md`, `PLAYBOOK-TEMPLATE.md` | unattended templates → `adopt-unattended.sh` | `.unattended.conf` keys | **Overwritten** (`CUSTOM-UPROTO`, `-PLAYTPL` gone). |
| `memory/guides/REVIEW-PROTOCOL.md` | template → `check-protocol-parity.test.sh --render` | none | **Overwritten** (the diff shows `-- CUSTOM-RPROTO` removed). |
| `tools/*/…template.md` (gov's instruction sources) | engine | edit gov's file | Non-conflicting edit: merged, survived and flowed into the render (`CUSTOM-HYG-TPL` reached `HYGIENE.md`; `CUSTOM-UNATT-TPL` reached the unattended skill). Conflicting edit: kit held back, as above. |
| `memory/guides/SESSION-KICKOFF.md` | seed | the seam itself (its §B is the adopter's) | **Survives** (`patched [seed]`). |
| `session-kickoff/SKILL.md` | machine junction into gov's checkout | none | Not measured. An edit is an edit to gov's checkout, shared by every adopter on the machine. |
| hook `.js` refusal text | engine | `.agent-cap.conf` cap value only | Non-conflicting: merged and survived (`CUSTOM-HOOK`). Conflicting: kit held back (by the same mechanism). |
| `.claude/rules/*.md` | adopter only | owner-written file | **Survives** (`CUSTOM-RULE`); gov never touches it. |
| `[charter]` / `[answers]` | adopter's overlay | the seam itself | **Survives and re-renders** (`ADOPTER-RULE-ONE` in `AGENTS.md` after the update). |

Two more measured results:
- **Tagged edit (tE).** I edited `BUILD-METHOD.md` with a `<!-- carve-out house-1 -->` tag and a registry row, per the runbook's carve-out contract. After `update --write` the grep count was `0`, and the update printed the row as `re-rendered`.
- **Edits are recoverable but not named.** `update --write` leaves the renders as unstaged worktree changes, so a committed edit can be recovered from git. Read-only `update` printed the same `re-rendered` word for edited and unedited rows. The code confirms it (`govkit.py:9624-9625`: `if how == "adopter" and v in ("diverged","stale"): v = "re-rendered"`).

## 3. Pre-existing instructions at install (tA, apply at HEAD)

The fixture held its own `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.claude/rules/api.md`, `.claude/agents/my-agent.md` and `.claude/settings.json`. `plan` printed none of the first four. The results:

- **`AGENTS.md`:** kept. The region was appended below the authored text (`PRE-AGENTS` at line 3, the region opening at line 5).
- **`CLAUDE.md`, `GEMINI.md`, copilot instructions:** kept but unwired. Apply printed `CONFIGURE agent-instructions: adopter exit 1`, and the re-run printed `AGENT-INSTR wire FAILED — CLAUDE.md exists and is not AGENTS.md wiring — pass --force to replace it`, and the same for the other two. So Claude reads only the old `CLAUDE.md` and never sees the charter until wired.
  - Adding an `@AGENTS.md` line to `CLAUDE.md` gave `= CLAUDE.md (pointer, current)` and kept the authored text.
  - `--force` overwrote the copilot file, losing `PRE-COPILOT`. It wrote `.gemini/settings.json` and left `GEMINI.md` in place.
- **`.claude/rules/api.md` and `my-agent.md`:** untouched.
- **`settings.json`:** merged; `"Bash(make:*)"` was kept alongside gov's hooks.

## 4. Gov's own seams, and what the records say

**Gov's own seams:**
- `.governance/deploy.toml`: 14 `[answers]` and 9 `[charter] adopter_rules` lines. It has no `playbook_path`, so gov renders from its root template, which it edits directly as the source.
- `AGENTS.md` is the region alone (lines 1–177), and `CLAUDE.md` is just `@AGENTS.md`.
- `.claude/rules/product.md` is a hand-authored path rule (`paths:` front matter); no kit ships it.
- `.lexicon.conf` holds the VERBS vocabulary and pins, which feed the lexicon skill.
- `policy.toml` holds effort and gate allowlists.
- All ten house overlays are 0 bytes, so gov uses none.
- `.governance/` holds `deploy.toml` and nothing else: no `install.json`. Gov never exercises update-survival for its own customizations.

**Records:**
- **TOOL-aScouredKit-14** (cited in a comment in `entries/playbook.kit.toml`): "a hand-edit of the rendered AGENTS.md was reverted by the next render."
- **id PLAY-aDistilledCharter-4:** gov's authored wrapper around the region was folded into `[charter] adopter_rules`, "so gov's charter is the region alone." Gov moved off the outside-the-region seam.
- **id DEPL-aRepatriatedFork-1:** "Both adopters forked this file" for `PROJECT_NAME`; this was retired by making it an asked answer.
- **id TOOL-aRepatriatedFork-10:** nc carried tagged carve-outs that touch the memory-tree kit (its table runs `1/24`, `2/24`, …), including a note in its forked `scripts/HYGIENE.template.md:63-69`. They were moved into config and renders. The runbook's carve-out ledger (`WIRE-INTO-PROJECT.md:1139-1198`) came from this. It is adopter-side only; govkit's only hits for `carve-out` are code comments, and nothing parses the tags.
- **aRepatriatedFork README:** one pull left "27 and 32 engine rows `unattributed`", merged by hand, and the merge "silently stripped 16 CR bytes."
- **dPolishedVitrine round-2 review:** NicoCares' rendered memory docs were stuck one vintage back, graded `re-rendered`, then `patched`.
- **dRetiredFork-3:** nine rendered rows were stale at NicoCares.
- **dUnstuckLanding census:** "nc's `CLAUDE.md:59` limits unattended landing to nodes `a` and `d`, and nothing" (in gov's tooling reads it); the rule lives in the adopter's prose.
- **aRatchetForge:** an "inCMS-tuned SKILL.md" sat in the user skills directory, so "the generic engine never fires."

**Self-tests:** they cover engine three-way merges (`selftest.py:9583`, "the adopter's edit survived") and seed or project-owned preservation (`:6263`). They pin the `re-rendered` label (`:14750`). A grep for edited-rendered cases (`rendered.*(patched|edit)|edit.*rendered`) returned only lines 9106 and 14750. I found no arm that protects or reports an edited rendered output.

## 5. Candidates: existing seams a custom-instruction design could extend

| # | Mechanism (existing instance) | Test that would make it lose | Result |
|---|---|---|---|
| A | Overlay **slot**: the overlay keeps the text and the renderer fills a declared placeholder; the output is wholly generated (`[charter] adopter_rules` → `{{ADOPTER_RULES}}`) | (1) survives the update and reaches the render; (2) can change an existing gov rule; (3) reaches any artifact besides `AGENTS.md` | (1) passed. (2) **lost**: `render-playbook: REFUSED — [charter] reuse names no declared [[placeholder]]`. (3) **lost**: only `render_playbook.py` reads `[charter]`; the other renderers take one-line conf values. |
| B | Overlay **file**: a seed per artifact, appended by the renderer (`house/<role>.md`) | same three | (1) passed (`CUSTOM-HOUSE` survived and rendered). (2) **lost**: `render_role` appends `## House rules` after the base. (3) **lost**: roles kit only. |
| C | **Region**: the renderer owns marked bytes and leaves the rest (`gov:playbook`). The owner's "tag every edit and render around it" belongs here. | (1) an edit inside the region survives; (2) a tagged edit in a whole-file render survives; (3) other renderers have regions | (1) **lost, silently** (`CUSTOM-AGENTS-IN`). (2) **lost** (tE count `0`). (3) **lost**: `render_all` writes whole files. Text outside the region did survive. |
| D | Edit gov's **source** and rely on the verdict grid's three-way merge | an adopter edit to a line gov later changes | **Lost**: kit `HELD BACK`, rolled back, order written (tC). Non-conflicting edits did merge. |
| E | **Whole-file ownership** (`[[own]]`, or an edited seed) | (1) covers rendered artifacts; (2) gov's later changes still arrive | (1) **lost**: `names a source gov ships as rendered` for `HYGIENE.md` and the build skill. (2) **lost**: an owned file is never written, and the seed template stays at 4.3 under `reseed-available`. |
| F | **Adopter-only files** gov never touches (`.claude/rules`, own agents, `CLAUDE.md` beside the import) | (1) survives; (2) changes a gov rule; (3) reaches role agents | (1) passed. (2) **lost**: it can only add competing text. (3) not through `CLAUDE.md` (`omitClaudeMd: true`); path rules unmeasured. |

A and B are one mechanism (adopter text composed by gov's renderer, never edited in the output) with two existing instances. C, D, E and F are distinct mechanisms; another candidate would differ only in where the text is stored.

## 6. Pick, and what it leaves uncovered

**Pick: A and B as one composition mechanism, extracted into a single factory every renderer calls.** The charter's `[reuse]` rule asks for this at a kind's second instance, and two exist now.
- It is the only mechanism whose text survived an update and reached the regenerated output (`ADOPTER-RULE-ONE`, `CUSTOM-HOUSE`).
- It is what gov itself uses (its 9 `adopter_rules` lines).
- It is graded against a declared slot set: a misspelt `[charter]` key refuses.
- C lost silently in two measured cases, D halts a kit, and E freezes gov's updates.

**What it leaves uncovered:**
- **Changing or removing a gov line.** A and B both lost test (2); no existing seam does it. A design that adjusts by rule tag must add a test: does update report when gov changes a rule an overlay overrides?
- **Hook refusal text and engine code,** which only D reaches, with the held-kit failure.
- **The alias copies.** In copy mode the copilot file goes stale on every charter change, the update does not run its check, and `--force` destroys edits.
- **The machine-scope kickoff skill:** no per-adopter home.
- **Reporting.** Update prints `re-rendered` for edited, unedited and not-re-rendered rows alike. No guard or self-test catches an edited render being lost; only git history keeps it.
- **Seed freezing.** Every seeded charter template, edited or not, stays at its install vintage until reseeded by hand.
- **Pre-existing `CLAUDE.md`, `GEMINI.md` and copilot files** stay unwired until `--force`, which overwrites them.

One limit on the evidence: the scratch-guard hook refused me as a role agent running gate legs, so wherever I say a leg (`playbook render wiring`, `roles render wiring`, `agent-instructions wiring`) reds on an edit, that is read from code and descriptors, not run. The main session can run those legs on a fixture to confirm.
