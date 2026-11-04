# PLAY-dConvergedCharter-16 — the `/session-kickoff` Skill retired: its kit homed under the tool root, a `[[retired]]` row, a forwarding stub and the dangling-link report

**Status:** OPEN · rev-1 · 2026-11-03 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 5 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0490@0c938e1f whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-build-PLAY-dConvergedCharter-11-reuse-scout-c.md](../build/2026-11-03-build-PLAY-dConvergedCharter-11-reuse-scout-c.md) | research | PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 |
| [2026-11-03-build-PLAY-dConvergedCharter-16-deviation-161.md](../build/2026-11-03-build-PLAY-dConvergedCharter-16-deviation-161.md) | deviation | — |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md) | research | PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-21 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |

<!-- /gen:spec-records -->

## 1. Goal

`/session-kickoff` reaches every repository on a machine through one link to gov's live checkout,
outside any repository and any receipt, and nothing sees that link dangle once the directory moves
(`gap-orient-21`, gap register :152). This unit retires the Skill once the orientation scout and
`kickoff.runs` have landed. The engine's files move to a kit home of their own under the tool root,
every reader is re-pointed, a `[[retired]]` row and a forwarding stub stand for
`install.deprecation-window` releases, and the node preflight reports a link whose target is gone.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build, each specced and unbuilt at base
`0d1c1dda`: the orientation scout, `gov-orienter` in a sidechain (TOOL-dFurnishedOrders-1 S7, S8);
`kickoff.runs` and the `kickoff —` line (TOOL-dRankedPlan-8 S1 to S4); `derive_readers` (unit 11's
I1); the `skill` member of `KINDS` and its render (unit 17's I3). The unattended kit's own readers
of the Skill leave with unit 12, which builds before this unit.

- **S1** — The kit home. `manifest-check.sh`, `manifest-check.test.sh`, `MANIFEST-TEMPLATE.md`,
  `orientation-card.fragment.json` and `orientation-replay.fragment.json` move by `git mv` from
  `skills/session-kickoff/` to `tools/kickoff-manifest/`. The entry keeps its id, `kickoff-manifest`,
  and its descriptor `tools/govkit/entries/kickoff-manifest.kit.toml` sets `home = "kickoff-manifest"`,
  joined to the tool root like every other home. Each `[[files]]` row keeps its `to`, so an adopter's
  installed paths do not move and no adopter step is owed for them. Observed by AC1.
- **S2** — The engine's procedure leaves the Skill. `SKILL.md`'s body below its front matter, the
  engine's Steps 0 to 5b and the scaffolding section, moves to `tools/kickoff-manifest/KICKOFF-ENGINE.md`,
  a new `[[files]]` row of the entry with role `engine` and `to = "{prefix}/KICKOFF-ENGINE.md"` (§8 F2).
  The orientation scout and an inline orientation read that file, never the Skill:
  `tools/roles/agents/gov-orienter.agent.md:30`, `tools/workflows/orient.agent.md:23` and
  `tools/workflows/orient-counterfactual.js:102` name the file, read through `resolve_kit_dir` with
  home `kickoff-manifest`. Observed by AC2.
- **S3** — The path readers re-pointed in the commit that moves the files, before the directory goes.
  `derive_readers(repo, "skills/session-kickoff/", "path")` (I1) at the pass is the list, and
  `**Readers:**` below is its reading at base. A frozen record under `memory/builds/`, `memory/ledger/`
  or `memory/archive/` is never edited, and the fixture receipts under `tools/govkit/fixtures/` keep
  the source paths of the install they model. `.governance/install.json` is re-written by `update`,
  never by hand. Observed by AC3.
  **Readers:** by name: `.claude/settings.json:38`, `.claude/settings.json:47`, `.githooks/pre-commit:238`,
  `.gitattributes:146-151`, `tools/gate-legs.json:6`, `tools/gate-legs.json:155`, `tools/gate-legs.json:309-312`,
  `tools/gate-legs.json:357`, `tools/gate-legs.json:1517`, `tools/gate-legs.json:1840`,
  `tools/govkit/registry.toml:29`, `tools/govkit/govkit.py:2316`, `tools/check-wiring.sh:1167`,
  `tools/check-kit-versions.sh:272`, `tools/check-kit-versions.sh:298-310`, `tools/check-playbook-parity.sh:396`,
  `tools/check-hook-destinations.sh:31`, `tools/settings-merge.py:731-733`, `tools/policy/caps.toml:53-57`,
  `tools/policy/caps.toml:271-327`, `tools/policy/check_policy.py:3492`, `tools/template-size-limits.txt:63`,
  `tools/template-size-highwater.txt:12`, `tools/lexicon/kit.toml:167`, `tools/roles/handoff.py:101`,
  `tools/lib/render-doc.sh:263`, `tools/memory-tree/adopt-memory-tree.sh:485`, `.memory-tree.conf:637`,
  `memory/project/method-carriers.txt:7`, `memory/project/spawn-idiom-sites.txt:41-50`,
  `memory/project/unarmed-branches.txt:23-25`, `memory/project/temp-name-sites.txt:20`,
  `memory/project/fork-ceilings.txt:20`, `memory/project/spec-token-waivers.txt:37`,
  `memory/guides/SESSION-KICKOFF.md:3`, `memory/guides/SESSION-KICKOFF.md:6`, `memory/guides/SESSION-KICKOFF.md:9`,
  `memory/guides/SESSION-KICKOFF.md:83`, `README.md:20`, `.claude/rules/product.md:18`,
  `.claude/rules/product.md:41`, `WIRE-INTO-PROJECT.md:12`, `WIRE-INTO-PROJECT.md:785`,
  `WIRE-INTO-PROJECT.md:804`, `.governance/deploy.toml:40`, `.governance/deploy.toml:42`,
  `.governance/deploy.toml:64`, and the suites `tools/check-wiring.test.sh`, `tools/hooks/scratch-guard.test.sh`,
  `tools/memory-tree/check-memory-hygiene.test.sh`, `tools/govkit/selftest.py`, `tools/memory-recall/selftest.py`,
  `tools/check-playbook-parity.test.sh`, `tools/workflows/check-protocol-parity.test.sh`,
  `tools/memory-tree/kit-dogfood-parity.test.sh` and `skills/session-kickoff/manifest-check.test.sh` ·
  by value: the registry glob `skills/session-kickoff/**` (`tools/govkit/registry.toml:29`), which
  claims every file under it; the `renamed` tuple at `tools/govkit/govkit.py:2316`; the floor
  `skills/session-kickoff/manifest-check.sh:32:29` of `ARMS_FLOORS` (`.memory-tree.conf:637`), keyed by
  the path; the 18432-byte row at `tools/template-size-limits.txt:63` and its cap row
  `tools/policy/caps.toml:53-57`, which compare the file's size; the guards of the six legs above,
  which select a run by the path; and `KICKOFF_ENGINE` at `.unattended.conf:171`, which unit 12
  retires with the kit.
- **S4** — The Skill's name re-pointed: each reader of `/session-kickoff` names the orientation scout
  and the card instead. The charter's two lines (`coding-governance-agents.template.md:115`, `:137`)
  read "The orientation scout opens every session: it runs the kickoff engine, loads this repository's
  kickoff manifest and appends the card whose `kickoff —` line says what the session runs" and "route
  the unit through the session's card first". The write gate's refusal text in
  `tools/hooks/scratch-guard.js` (`:734`, `:1183`, `:1188`, `:1200`) names `gov-orienter` and
  `manifest-check.sh --card --append`. `AGENTS.md` and `.claude/agents/*.md` are renders and are
  re-rendered, never edited. Observed by AC4.
  **Readers:** by name: `coding-governance-agents.template.md:115`, `coding-governance-agents.template.md:137`,
  `tools/hooks/scratch-guard.js:54`, `tools/hooks/scratch-guard.js:734`, `tools/hooks/scratch-guard.js:1183`,
  `tools/hooks/scratch-guard.js:1188`, `tools/hooks/scratch-guard.js:1200`, `tools/hooks/README.md:297`,
  `tools/hooks/README.md:359`, `tools/roles/workflows.toml:17`, `tools/roles/README.md:359`,
  `tools/memory-recall/SKILL.template.md:17`, `tools/memory-recall/README.md:186`,
  `tools/memory-tree/README.md:674`, `tools/memory-tree/check-verdict-epoch.sh:39`,
  `tools/lib/render-doc.sh:208`, `tools/memory-tree/adopt-memory-tree.sh:430`,
  `memory/guides/SESSION-KICKOFF.md:13`, `memory/guides/SESSION-KICKOFF.md:28`,
  `skills/session-kickoff/MANIFEST-TEMPLATE.md:13`, `skills/session-kickoff/MANIFEST-TEMPLATE.md:41`,
  `README.md:108-117`, `WIRE-INTO-PROJECT.md:71-87`, `WIRE-INTO-PROJECT.md:149-150`,
  `WIRE-INTO-PROJECT.md:882`, `WIRE-INTO-PROJECT.md:1284`, `WIRE-INTO-PROJECT.md:1357`, and
  `tools/roles/SKILL.template.md`, which unit 17 retires before this unit builds · by value: the
  `harness` field of the `orient` workflow (`tools/roles/workflows.toml:17`), which the roles render
  prints as the stage's driver, becomes `gov-orienter`'s sidechain; the write gate's remedy string,
  which `tools/hooks/scratch-guard.test.sh` compares; and check-wiring's install arm, S7.
- **S5** — The `[[retired]]` row in `tools/govkit/registry.toml`: `id = "command:session-kickoff"`, the
  `<class>:<name>` id form unit 17 S1 adds to `read_retired`, `successor = "none"`, and `surfaces`
  naming each member the step gate's RED line names vanished in the unit's range (§8 F1).
  Observed by AC5.
  **Readers:** by name: the readers S3 and S4 list, which spell the Skill, and the row's own readers
  `tools/govkit/upgrade_steps.py:890` and `tools/govkit/step_gate.py:207` · by value: `resolve_claim`
  (`tools/govkit/upgrade_steps.py:1002`), which no receipt reaches, since no receipt claims a Skill,
  and the step gate's witness read of `surfaces` (`read_witnessed_members`).
- **S6** — The forwarding stub, I3: one `[[shim]]` row in `tools/govkit/shims.toml`,
  `id = "kickoff-manifest/session-kickoff"`, `kind = "skill"`, `from = "skills/session-kickoff/SKILL.md"`,
  `to = "{prefix}/kickoff-manifest/KICKOFF-ENGINE.md"`, `closed = false`, rendered by
  `shims.py --write` through unit 17's `skill` template into `skills/session-kickoff/SKILL.md`, the
  one file left under the directory. A node's link keeps resolving through the window. The row takes
  unit 17's Skill-`to` form, a forwarder naming `to`; its `from` sits at the Skill's root-level home
  rather than under `{prefix}/<kit>/`, which unit 17 S2's reader must admit. Closing the row
  under `install.deprecation-window`, which `check_shim_windows` (`tools/govkit/shims.py:348`) allows only
  once that many releases are cut, deletes the stub, and the directory goes with it; unit 20's arm reds
  an open row its window allows to close. The engine text the stub replaces leaves with S2.
  Observed by AC5 and AC6.
  **Readers:** by name: `skills/session-kickoff/SKILL.md`, which the stub replaces, read by the
  junction `WIRE-INTO-PROJECT.md:75` lays, `tools/check-wiring.sh:1933`, and `tools/gate-legs.json:155` ·
  by value: the size row `tools/template-size-limits.txt:63`, which S3 moves to `KICKOFF-ENGINE.md`.
- **S7** — The node preflight reports a dangling link. `check_skill_install`
  (`tools/check-wiring.sh:1887`) gains a first test, `test_link_dangling`: an entry
  `~/.claude/skills/session-kickoff` that its parent directory lists and that does not resolve prints
  `UNWIRED  skill     — ~/.claude/skills/session-kickoff is a link whose target is gone` with the
  removal command for the platform, and counts as unwired. Today the `[ ! -d "$inst" ]` branch
  (`:1892-1903`) reads that entry as absent and prints a skip or the gate's remedy. The gate-needs-the-Skill
  arm (TOOL-aRoutedQuill-5 S9, `:1893-1900`) retires with S4, since the refusal no longer names the Skill,
  and the byte compare (`:1933-1945`) compares the stub alone through the window. Observed by AC7.
  **Readers:** by name: `tools/check-wiring.sh:1893-1900`, `tools/check-wiring.test.sh:624-628` ·
  by value: the `UNWIRED  skill` line that `tools/check-wiring.test.sh:628` greps.
- **S8** — `home_root_relative`, the descriptor flag whose one user S1 removes, is deleted with its
  reader branch. Observed by AC1.
  **Readers:** by name: `tools/govkit/entries/kickoff-manifest.kit.toml:10`, `tools/govkit/govkit.py:13661-13665`,
  `tools/govkit/fixtures/make_adopter_receipt.py:195`, `tools/govkit/fixtures/make_adopter_receipt.py:213`,
  `WIRE-INTO-PROJECT.md:1707` · by value: `resolve_descriptor_paths` (`tools/govkit/govkit.py:13653`),
  which keeps a flagged home as spelled; with no flag left every home is joined to the tool root.
- **S9** — The docs: `help/roles.md` ("How a task reaches an agent") and the runbook's §1 link step say
  the kickoff runs from the session's card, and give the command that takes a node's old link away;
  `help/upgrade-steps.md` names the succession row a Skill may now hold.
  NOT OBSERVED by a criterion: prose, read at the diff review.

## 3. Non-goals (OUT)

- The orientation scout, its sidechain and `kickoff.runs`: TOOL-dFurnishedOrders-1 and
  TOOL-dRankedPlan-8. This unit re-points readers to them and builds neither.
- The `skill` kind's forwarder template and the `KINDS` member: unit 17's. This unit writes one row.
- Rendering the engine's steps from units, or a protocol slice of them: units 1, 7 and 10 migrate
  every protocol text, `KICKOFF-ENGINE.md` among them, after this unit.
- Retiring the `{user_skills}` token and the `user_skills` answer of `deploy.toml`. After this unit no
  descriptor row spells the token, and its readers in `tools/govkit/govkit.py`, `matrix.py` and the
  renders are an adopter-visible answer; it is named here as a follow-up, the build run's AMEND to file.
- Removing a node's link. A link sits outside every repository, and the deployer writes nothing there;
  S7 prints the command and stops.
- Editing a frozen record, a fixture receipt, a render, or another build's spec.

### Edges

- **consumes-from** `PLAY-dConvergedCharter-11` — `derive_readers`, the reader inventory S3 and AC3 run; without it the inventory is a typed list nothing re-derives
- **consumes-from** `PLAY-dConvergedCharter-17` — `KINDS` gaining `skill` and its render, without which S6's row is refused by `read_shim_rows`, and the `<class>:<name>` id form of `read_retired` S5's row takes
- **consumes-from** external — TOOL-dFurnishedOrders-1 (the orientation scout) and TOOL-dRankedPlan-8 (`kickoff.runs`), each specced and unbuilt at base `0d1c1dda`, the clause's own preconditions

## 4. Design

### Evidence

Read at `d8a12f04`; no product file differs from base `0d1c1dda`.

- `skills/session-kickoff/` holds six tracked files; the entry ships all of them, `SKILL.md` as the
  machine-scoped link `{user_skills}/session-kickoff` and the rest at `{prefix}/`
  (`tools/govkit/entries/kickoff-manifest.kit.toml`). Its `home` is the one root-relative home
  (`:6-10`).
- `read_retired` (`tools/govkit/upgrade_steps.py:890-931`) reads an id as an entry or a step, and
  the Skill is neither; unit 17 S1 adds the `<class>:<name>` form, which this row uses.
- `read_shim_rows` (`tools/govkit/shims.py:60-104`) admits `command`, `hook` and `module` and paths
  ending `.sh`, `.js` or `.py`; a `.md` row is unit 17's widening.
- The orientation scout loads "the engine as the `session-kickoff` Skill"
  (`tools/roles/agents/gov-orienter.agent.md:30`), and TOOL-dFurnishedOrders-1 S8 keeps the Skill's
  steps as the engine. Retiring the Skill with its text would leave the scout with nothing to run,
  which §8 F2 settles.
- `check_skill_install` returns early when `$inst` is not a directory (`tools/check-wiring.sh:1892`),
  so a link whose target is gone prints `skip` or the gate's remedy, never the dangle (scout C
  finding 8).

### The dangling test

`test_link_dangling` reads the parent's listing through a bash glob, which returns every directory
entry, a dangling one included, and tests `[ -e "$entry" ]`, which follows the link and fails on a
missing target. It needs no python, which check-wiring keeps off its SessionStart path
(`tools/check-wiring.sh:227-228`). UNVERIFIED for an NTFS junction under MSYS until AC7's fixture runs
on a Windows node: the fixture lays a junction there with `cmd //c mklink /J` and a symlink elsewhere.

| State of `~/.claude/skills/session-kickoff` | Check S prints |
|---|---|
| listed, does not resolve | `UNWIRED  skill` naming the dangle and the removal command |
| absent | `skip`, no remedy, since nothing routes through the Skill |
| resolves, stub tracked here | the stub's byte compare, as today's compare over one file |
| resolves, stub not tracked here | `skip`, the install is machine-global (`:1909-1911`) |

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `test_link_dangling` | shell function, `tools/check-wiring.sh` | `sh.function`, OK by `--suggest` |
| `tools/kickoff-manifest/` | kit home of the `kickoff-manifest` entry | none |
| `KICKOFF-ENGINE.md` | engine text, shipped at `{prefix}/KICKOFF-ENGINE.md` | none |
| `kickoff-manifest/session-kickoff` | `[[shim]]` id | none |
| `command:session-kickoff` | `[[retired]]` id, unit 17's form | none |

### Migration

Additive at an adopter, but for one file: `KICKOFF-ENGINE.md` joins `{prefix}/` on the next `update`,
and the Skill's link is the node's to remove once S7 reports it. Every other destination keeps its
`to`. A receipt written before the move names the old `source`; `update` re-writes it in the walk that
ships the re-pointed `handoff.py`, whose `KICKOFF_HOME` becomes `kickoff-manifest`.

### Rollout

The move, the re-points, the engine file and S7 land first, in one commit, since a reader re-pointed
after the move reds in between. The stub, the `[[retired]]` row and the charter lines land once both
preconditions have, in the commit that replaces `SKILL.md` with the stub.

### Files touched (estimate)

- `skills/session-kickoff/` (moved out, then the stub), `tools/kickoff-manifest/`: S1, S2, S6
- `tools/govkit/entries/kickoff-manifest.kit.toml`, `tools/govkit/registry.toml`, `tools/govkit/shims.toml`,
  `tools/govkit/govkit.py`, `tools/govkit/selftest.py`, `tools/govkit/fixtures/make_adopter_receipt.py`: S1, S5, S6, S8
- `tools/roles/agents/gov-orienter.agent.md`, rendered to `.claude/agents/gov-orienter.md`;
  `tools/workflows/orient.agent.md`, `tools/workflows/orient-counterfactual.js`, `tools/roles/handoff.py`,
  `tools/roles/workflows.toml`, `tools/roles/README.md`: S2, S3, S4
- `coding-governance-agents.template.md`, rendered to `AGENTS.md` by `tools/playbook/`; `.governance/deploy.toml`,
  rendered into `AGENTS.md` and `.claude/agents/*.md`: S3, S4
- `tools/hooks/scratch-guard.js`, `tools/hooks/scratch-guard.test.sh`, `tools/hooks/README.md`: S4
- `tools/check-wiring.sh`, `tools/check-wiring.test.sh`: S3, S7
- `.claude/settings.json`, `.claude/rules/product.md`, `.githooks/pre-commit`, `.gitattributes`, `.memory-tree.conf`: S3
- `tools/gate-legs.json`, `tools/template-size-limits.txt`, `tools/template-size-highwater.txt`,
  `tools/policy/caps.toml`, `tools/policy/check_policy.py`, `tools/lexicon/kit.toml`: S3
- `tools/check-kit-versions.sh`, `tools/check-playbook-parity.sh`, `tools/check-playbook-parity.test.sh`,
  `tools/check-hook-destinations.sh`, `tools/settings-merge.py`, `tools/lib/render-doc.sh`,
  `tools/memory-tree/adopt-memory-tree.sh`, `tools/memory-tree/README.md`, `tools/memory-tree/check-verdict-epoch.sh`,
  `tools/memory-tree/check-memory-hygiene.test.sh`, `tools/memory-tree/kit-dogfood-parity.test.sh`,
  `tools/workflows/check-protocol-parity.test.sh`, `tools/memory-recall/SKILL.template.md`,
  `tools/memory-recall/README.md`, `tools/memory-recall/selftest.py`: S3, S4
- `memory/guides/SESSION-KICKOFF.md`, `memory/project/method-carriers.txt`, `memory/project/spawn-idiom-sites.txt`,
  `memory/project/unarmed-branches.txt`, `memory/project/temp-name-sites.txt`, `memory/project/fork-ceilings.txt`,
  `memory/project/spec-token-waivers.txt`: S3
- `README.md`, `WIRE-INTO-PROJECT.md`, `help/roles.md`, `help/upgrade-steps.md`: S3, S4, S8, S9

### Alternatives rejected

- **Leaving the engine files under `skills/` and retiring only the link.** The clause moves
  `manifest-check.sh` and its fragments to a kit home of their own before the directory goes, and the
  directory cannot go while it holds them. Rejected by reading the clause.
- **A new entry id for the moved kit.** Rejected by `git grep -c kickoff-manifest`: 53 files read the
  id, `.governance/install.json` and the default selection (`registry.toml:40`) among them, and the
  name stays accurate, since the manifest the kit ratchets is still the kickoff manifest.
- **A hand-written stub `SKILL.md`.** `shims.toml`'s header forbids it: a forwarder is rendered from
  its row, and `--check` holds it equal to its render.
- **The dangling test through `test_path_linked` (`tools/govkit/upgrade_steps.py:1492`).** It answers
  the question exactly, through `os.lstat`, but needs python on a hook path that runs without it.

## 5. Production-readiness checklist

- security — S7 writes nothing outside the repository and prints the removal command; the write
  gate's refusal still refuses the same writes, only its remedy text moves.
- perf / scale — one glob and one `-e` test per SessionStart.
- error / empty / loading states — a node with no link reads `skip`; a dangling one is UNWIRED with
  its remedy, never a skip.
- observability — S7's line names the link and the command; `upgrade_steps.py list` prints the
  `[[retired]]` row.
- risks — a reader the inventory misses breaks a hook at SessionStart; AC3's scratch-clone run is the
  check before the directory goes, and the stub keeps every old link resolving through the window.
- testing — the planted node of AC7, the scratch clone of AC3, the moved suite of AC1.
- migration — §4.
- user docs — `help/roles.md`, `help/upgrade-steps.md` and the runbook, S9.

## 6. Acceptance criteria

- **AC1** — When `git ls-files skills/session-kickoff` runs at the commit that moves the files, it
  prints `skills/session-kickoff/SKILL.md` alone, and `bash manifest-check.sh memory/guides/SESSION-KICKOFF.md`
  run from the kit home exits 0; `git grep -n home_root_relative` prints nothing outside frozen records.
  Red when: a file the entry ships is left under the Skill's directory, or the ratchet reads its old path.
- **AC2** — When `grep -n KICKOFF-ENGINE.md` runs over `gov-orienter.agent.md`, `orient.agent.md` and
  `orient-counterfactual.js`, each names the engine file, and `grep -n session-kickoff` over the three
  prints nothing.
  Red when: the scout still loads the Skill, so the retirement leaves it no engine.
- **AC3** — When `derive_readers` runs from `check_policy.py` with needle `skills/session-kickoff/` and kind
  `path` over a scratch clone at the unit's tip with the directory removed, it returns no reader outside
  frozen records and the two rows of S5 and S6; with one planted line `bash skills/session-kickoff/manifest-check.sh`
  in the clone's `.githooks/pre-commit`, it returns that line.
  Red when: the planted path reader survives the removal unreported.
  fixture: a clone under `%TEMP%/<short-name>`; the function is unit 11's.
- **AC4** — When `grep -n "/session-kickoff"` runs over `coding-governance-agents.template.md` and
  `scratch-guard.js` at the tip, it prints nothing, and the write gate's refusal on a scratch write with
  no routed unit names `gov-orienter`.
  Red when: the charter or the gate still sends a session to the retired Skill.
- **AC5** — When `python tools/govkit/upgrade_steps.py list` runs at the tip, it prints
  `upgrade-steps: retired · command:session-kickoff -> none`, and `python tools/govkit/shims.py --check` exits 0
  with the row `kickoff-manifest/session-kickoff` open and its stub equal to its render.
  Red when: the row is refused, or the stub is a hand edit `--check` reds.
- **AC6** — When the row is set `closed = true` in a scratch clone while `read_releases` returns no
  release, `check_shim_windows` prints `kickoff-manifest/session-kickoff is closed and held`.
  Red when: the stub, and with it the directory, could go before any release is cut.
- **AC7** — When `bash tools/check-wiring.sh --check` runs with `HOME` a scratch directory whose
  `.claude/skills/session-kickoff` is a link to a directory since removed, it prints
  `UNWIRED  skill     — ~/.claude/skills/session-kickoff is a link whose target is gone`; with the
  target present it prints no such line.
  Red when: the planted node's dangling link reads as a skip.
  fixture: a symlink, or under MINGW a junction laid by `cmd //c mklink /J`.

## 7. Gates

`kickoff-manifest ratchet` · `kickoff engine size <=18KiB` · `manifest-check self-test` · `scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `hook destinations self-test` · `check-wiring self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `playbook parity selftest` · `playbook render selftest` · `kit/dogfood doc parity` · `codebase-map kit selftest` · `lexicon selftest` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `govkit runbook parity` · `step-gate` · `docs` · `playbook render wiring` · `roles render wiring` · `policy fixtures` · `transition-audit arms` · `straggler-guard arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/check-wiring.test.sh · covers AC7 · a scratch HOME whose session-kickoff link targets a removed directory · none
New arm: tools/govkit/selftest.py · covers AC5 AC6 · the skill row closed with no release cut, its failing case the stub deleted under a held window · none

## 8. Open questions

- **F1 — What the `[[retired]]` row's `id` names.** The Skill is neither a registry entry nor a step,
  and the registry's comment names only those two. Options: (a) `command:session-kickoff`, the
  `<class>:<name>` form unit 17 S1 adds for `/build`; (b) the bare `session-kickoff`, which
  `read_retired` reads clean at base but which reads as an entry id no entry holds; (c) retire the
  entry `kickoff-manifest` to a new entry at the kit home, so the row names an entry. (c) renames an id
  53 files read for a name that stays accurate, and (b) spells one Skill retirement two ways in one
  build. RESOLVED (agent, 2026-11-03, delegated): (a), rung 3, tie-broken by reuse of unit 17's seam. widens: none · relaxes: none
- **F2 — Where the engine's procedure goes when the Skill retires.** The orientation scout loads the
  Skill's text (TOOL-dFurnishedOrders-1 S7, S8), so retiring the Skill with its text leaves the scout
  nothing to run. Options: (a) the text ships per repository in the kit, `{prefix}/KICKOFF-ENGINE.md`,
  read by the scout and by an inline orientation; (b) the text inlined into `gov-orienter`'s definition,
  which a repository without the roles kit never receives, so the inline orientation
  TOOL-dFurnishedOrders-1 S8 keeps loses its engine; (c) an ask on dFurnishedOrders, and wait, which
  parks the clause. (a) moves the text's install location from the machine's skills directory into each
  repository's prefix, a veto-2 change the clause does not name. RESOLVED (agent, 2026-11-03,
  delegated): (a), rung 5, the one option meeting every criterion, recorded as deviation 161.
  ER:388 · widens: the engine text's install location, a machine link to a per-repository file · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, from the packet's Items 16, `gap-orient-21`, v2:579 and :605, scout
  C's row for 0490 and its findings 2 and 8, and the spec brief's I1, I2, I3.

## 10. Reuse audit

The seams extended are the `kickoff-manifest` descriptor (`tools/govkit/entries/kickoff-manifest.kit.toml`),
`[[retired]]` read by `read_retired` (`tools/govkit/upgrade_steps.py:890`), a `[[shim]]` row read by
`read_shim_rows` (`tools/govkit/shims.py:60`) with its window `check_shim_windows` (`:348`), and
`check_skill_install` (`tools/check-wiring.sh:1887`). `python tools/codebase-map/reuse_lookup.py "retire a
skill directory and report a dangling machine link"` ranked `read_retired`, `RetiredRow`,
`test_path_linked` and `signal_dangling_pointers`; the first two are the seam, `test_path_linked` is
rejected in §4 for needing python, and `signal_dangling_pointers` grades record pointers, not links.
Scout C's row holds at HEAD with three corrections: the clause's `[[retired]]` row cannot name an entry
here, since the entry stays live (§8 F1); the scout's "about 50 more files" is 102 tracked files outside
`memory/builds/` and `memory/ledger/` by `git grep -l session-kickoff`, the readers S3 and S4 list; and
the orientation scout loads the Skill, a hole the record does not name (§8 F2).

Recall terms used: `python tools/memory-recall/query.py "how does the session-kickoff skill retire and what reports a dangling junction" --terms "session-kickoff junction retired shim forwarder manifest-check orienter kickoff.runs dangling check-wiring"`
