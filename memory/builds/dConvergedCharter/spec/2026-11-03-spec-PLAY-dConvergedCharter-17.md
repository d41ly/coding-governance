# PLAY-dConvergedCharter-17 — the `/build` Skill retired once the supervisor drives attended builds, its client held by a `skill` shim for the deprecation window

**Status:** OPEN · rev-2 · 2026-11-04 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 3 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0491@3aafd2a1 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-build-PLAY-dConvergedCharter-11-reuse-scout-c.md](../build/2026-11-03-build-PLAY-dConvergedCharter-11-reuse-scout-c.md) | research | PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-21 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-prompt-PLAY-dConvergedCharter-17-1-spec-writer.md](../prompts/2026-11-04-prompt-PLAY-dConvergedCharter-17-1-spec-writer.md) | journal | — |
| [2026-11-04-prompt-PLAY-dConvergedCharter-17-fold-brief.md](../prompts/2026-11-04-prompt-PLAY-dConvergedCharter-17-fold-brief.md) | research | — |
| [2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18 |

<!-- /gen:spec-records -->

## 1. Goal

`/build` carries its own procedure beside the flow (gap-found-13). dWellOiledMachine reduces it to a
client of `run` and leaves its retirement here (TOOL-dWellOiledMachine-25 §3, v2:584). This unit retires
it as SK-1 states: a `[[retired]]` row, its readers inventoried by value and re-pointed, and the client
kept for `install.deprecation-window` releases through a shim row of a new `skill` kind, so a Skill's
rename or retirement is held and closed by one declared row and never by a hand-kept file.

## 2. Scope (IN)

Build-run precondition, specced and unbuilt at base `0d1c1dda`: TOOL-dWellOiledMachine-25, whose S1 adds
`python tools/runtime/run.py <slug>` and whose S7 makes `/build` its client. With it unlanded the
supervisor does not drive attended builds and this unit does not build.

- **S1** — The `[[retired]]` row in `tools/govkit/registry.toml`: `id = "command:build"`, `successor =
  "none"`, `surfaces = ["command:build"]`, the member the step gate's `command` class reads for
  `.claude/skills/build/SKILL.md` (`tools/govkit/surface-classes.toml`). `read_retired`
  (`tools/govkit/upgrade_steps.py:890`) admits an id `<class>:<name>` whose class is a `[[class]]` row
  of `surface-classes.toml`, a retired surface member, and refuses one naming another class; the
  registry's succession comment (`registry.toml:190-195`) names the third id form. Observed by AC1.
  **Readers:** by name: `tools/govkit/registry.toml`, `tools/govkit/upgrade_steps.py`,
  `tools/govkit/step_gate.py`. by value: `tools/govkit/step_gate.py` (`:208-212`, which reads each
  row's `surfaces` as witnessed members) and `tools/govkit/govkit.py` (`:5463`, `check`'s line for a
  retired claimed kit, which no adopter's receipt reaches for a `<class>:<name>` id); the Skill's own
  readers are S4's.
- **S2** — The `skill` shim kind (shared interface I3). `KINDS` (`tools/govkit/shims.py:48`) gains
  `skill`. A `skill` row's `from` is a Skill's `.md` inside the tree: a kit's source under
  `{prefix}/<kit>/`, a Skill home `skills/<name>/SKILL.md`, or an installed Skill
  `.claude/skills/<name>/SKILL.md`, `{prefix}` resolved only where spelled. Its `to` is the successor,
  a `.md` an agent reads and follows (a Skill or an engine document) or a command `.sh`, `.js` or `.py`.
  With a `.md` `to`, `write_shims` renders at `from` the forwarder of §4 naming `to`, as it renders the
  other kinds; with a command `to`, the row holds `from`, the kit's own rendered client, open:
  `write_shims` writes nothing, and `check_shim_parity` holds an open row's `from` present and a closed
  row's `from` absent, with no install row of its kit naming it. `check_shim_windows` closes either form
  only under `install.deprecation-window`, unchanged. Observed by AC2, AC3.
- **S3** — The `/build` row in `tools/govkit/shims.toml`: `id = "roles/build-skill"`, `kind = "skill"`,
  `from = "{prefix}/roles/SKILL.template.md"`, `to = "{prefix}/runtime/run.py"`, `closed = false`. The
  client TOOL-dWellOiledMachine-25 S7 leaves stays as it renders, its description's first sentence
  naming the retirement and `run.py <slug>`, until the row closes. Observed by AC3.
- **S4** — Its readers by value re-pointed, found by `python check_policy.py --readers /build --kind
  value` and `--readers skills/build --kind path` (shared interface I1):
  - the charter's attended-build line (`coding-governance-agents.template.md:140`, rendered to
    `AGENTS.md:129`) becomes "- An attended code build runs through `run.py <slug>`, followed with
    `--follow`.", moved from the `kit:roles` fence to the `kit:runtime` fence;
  - the kickoff card's hand-off (`skills/session-kickoff/SKILL.md:210`) names `run.py <slug>`;
  - `WIRE-INTO-PROJECT.md:699,716-719,1353`, `help/roles.md:1,31,127-138`, `help/README.md:5`,
    `tools/roles/README.md:278-337`, `tools/roles/kit.toml:14,19` and the roles arm's lines of
    `tools/check-wiring.sh:1800-1871` name `run.py` where they name `/build` as the way to build;
  - `tools/govkit/usage.toml:69-72`'s `command:build` row and `tools/govkit/registry.toml:51`'s
    comment name the held client.
  **Readers:** by name: `coding-governance-agents.template.md`, `AGENTS.md`, `skills/session-kickoff/SKILL.md`,
  `WIRE-INTO-PROJECT.md`, `help/roles.md`, `help/README.md`, `tools/roles/README.md`,
  `tools/roles/kit.toml`, `tools/check-wiring.sh`, `tools/govkit/usage.toml`, `tools/govkit/registry.toml`.
  by value: the held set, kept until the row closes: `tools/roles/SKILL.template.md`,
  `tools/roles/adopt-roles.sh` (`:249`), `tools/roles/adopt-roles.test.sh`, `tools/roles/kit.toml`'s
  install row (`:55-57`), probe (`:88-92`) and `[[lf_pin]]` (`:145-147`), `.gitattributes:143`, the
  render checks of `tools/govkit/selftest.py:2872,2889` and `tools/check-wiring.sh:1844`.
  `tools/roles/SKILL.template.md` is this unit's held `/build` client until the `roles/build-skill` row
  closes, and for that reason PLAY-dConvergedCharter-9 AC2 counts only the five renamed kits' templates
  and excludes it. While the row is open the roles kit's `to`, `probe` and `pattern` rows naming
  `.claude/skills/build/SKILL.md` (`tools/roles/kit.toml:57`, `:90`, `:145`) stay, and
  PLAY-dConvergedCharter-9 S7 admits them as a held client's install rows, so `core skills conformance`
  stays green over gov's tree with both units built.
  Observed by AC3, AC4, AC5.
- **S5** — `help/shims.md` gains the `skill` kind: the two `to` forms, what a held client is, and that
  closing the row is a release-bound act of the kit the row's id names (PLAY-dConvergedCharter-20 S4).
  Observed by AC6.

## 3. Non-goals (OUT)

- `/build` as a client of `run`, and `run` itself: TOOL-dWellOiledMachine-25.
- Closing the row and removing the held set when the window closes: the roles kit's act, the kit the
  row's id `roles/build-skill` names, release-bound, in the first release after `check_shim_windows`
  allows it; PLAY-dConvergedCharter-20 S4 reds the row past that point naming the roles kit, and no
  unit of this build closes it. `shims.read_releases` reads no release at base (`shims.py:302-305`), so
  no window can close inside this build.
- Shipping the retirement to adopters as an upgrade step: PLAY-dConvergedCharter-20.
- `/session-kickoff` and `/unattended`: PLAY-dConvergedCharter-16 and -12.
- Renaming Skills to `gov-<name>`: PLAY-dConvergedCharter-9, which uses the `skill` kind's Skill form.

### Edges

- **consumes-from** `PLAY-dConvergedCharter-11` — `derive_readers`, the inventory by value whose `--readers` CLI lists and reds the readers of `/build`
- **hands-off** `PLAY-dConvergedCharter-16` — `KINDS`, the `skill` kind whose row holds or forwards a retired Skill for the window
- **hands-off** `PLAY-dConvergedCharter-9` — `KINDS`, the `skill` kind whose Skill form renders a forwarder at a renamed Skill's old source
- **hands-off** `PLAY-dConvergedCharter-20` — `shims.toml`, the `roles/build-skill` row, which that unit's S4 holds to its window and reds, naming the roles kit as the one that closes it, once a release lets the window close
- **consumes-from** external — TOOL-dWellOiledMachine-25, the supervisor driving attended builds and `/build` its client

## 4. Design

### Evidence

Read at `d8a12f046`; no product file differs from base `0d1c1dda`.

- `registry.toml` holds no `[[retired]]` row ("None has retired yet", `:195`) and `shims.toml` no
  `[[shim]]` row; `read_retired` reads an id with no `/` as an entry id and refuses only a live one
  (`upgrade_steps.py:890-925`), so `command:build` passes today with no class check.
- `read_shim_rows` requires exactly `id`, `kind`, `from`, `to`, `closed`, `from` and `to` two paths of
  one language among `.sh`, `.js`, `.py` (`shims.py:60-108`).
- The step gate's `command` class reads "each Skill a shipped survivor lands at
  `.claude/skills/<name>/SKILL.md`, by its name" (`surface-classes.toml`), and a vanished member needs a
  `[[retired]]` or `[[upgrade]]` row naming it in `surfaces` (`step_gate.py:208-212`, `:253`).
- `tools/govkit/usage.toml:69-72` already spells the Skill `command:build`.
- `/build` by value at base: the files of S4. `git grep` for `skills/build` adds `.gitattributes`,
  `tools/check-wiring.test.sh` and `tools/roles/adopt-roles.test.sh`.

### The forwarder a Skill-to-Skill row renders

```markdown
---
name: <the old Skill's name>
description: Renamed to <to's name>, held until install.deprecation-window closes. Use when you would run /<old name>; runs /<to's name>.
---
<!-- gov:shim <id> — rendered by shims.py from shims.toml; edit the row, never this file. -->
/<old name> has moved to /<to's name>. Read <to> and follow it.
```

The old name is `from`'s parent directory where `from` ends `/SKILL.md`, and otherwise the `name` of
`from`'s front matter at the commit before the row landed; `to`'s name is its own front matter's `name`,
or its file stem for a document with none, such as an engine document. A command `to` renders nothing,
because the client it holds already runs that command.

### Inventory

Minted: the shim kind `skill`; the `[[retired]]` id form `<class>:<name>`; the shim id
`roles/build-skill`; `render_skill_shim` in `shims.py`. Naming cell `py.function`: `OK` by `python
tools/lexicon/lexicon.py --suggest render_skill_shim --as py.function` at `d8a12f046`.

### Rollout

The `[[retired]]` row and the shim row land together with the re-points. The held client keeps working
for the window; the owner closes the row at a release under `install.deprecation-window`, and
PLAY-dConvergedCharter-20 removes the held set then.

### Files touched (estimate)

- `tools/govkit/registry.toml`, `tools/govkit/shims.toml`, `tools/govkit/shims.py`,
  `tools/govkit/upgrade_steps.py`, `tools/govkit/selftest.py`, `tools/govkit/usage.toml`
- `coding-governance-agents.template.md` (rendered to `AGENTS.md` by `tools/playbook/`)
- `skills/session-kickoff/SKILL.md`
- `tools/roles/SKILL.template.md` (rendered to `.claude/skills/build/SKILL.md` by
  `tools/roles/adopt-roles.sh`), `tools/roles/README.md`, `tools/roles/kit.toml`
- `tools/check-wiring.sh`
- `WIRE-INTO-PROJECT.md`, `help/roles.md`, `help/README.md`, `help/shims.md`

### Alternatives rejected

- **A generated forwarder in place of the client.** It drops the client's `## When run hosts in session`
  procedure (TOOL-dWellOiledMachine-25 S7), which `run.py` reaches whenever it prints `hosted in
  session`, and the clause keeps the client; §8 F2.
- **The client kept with no row.** Nothing would close it: the window is read only for a declared
  row (`check_shim_windows`), and "then removed" becomes a memory; §8 F2.
- **`build` as the `[[retired]]` id.** It reads as an entry id no registry entry holds; §8 F1.

## 5. Production-readiness checklist

- security — no new write path: the shim row is a declaration, `write_shims` writes nothing for a
  command-target row, and the row closes only under the window `govkit selfcheck` already enforces.
- perf / scale — one more row in each of two small tables.
- error / empty / loading states — a `skill` row whose `from` is absent while open is a parity finding
  naming it; an id of an unknown class is a refusal naming the class.
- observability — `shims.py --check` names each held row; the step gate reads the retired member.
- risks — an adopter's session that loads the held client during the window runs `run.py` as before;
  nothing changes for it until the row closes.
- testing — the fixtures of §6 and the arms of §7.
- migration — none in gov's tree; adopters: PLAY-dConvergedCharter-20.
- user docs — `help/shims.md` (S5) and `help/roles.md` (S4).

## 6. Acceptance criteria

The fixture is `python shims.py --fixture --plant <plant>`, the plants `shims.py` already stages in a
scratch repository (`run_fixture`, `shims.py:581`), with `skill-rename`, `skill-held` and `skill-closed`
added.

- **AC1** — When `python -c "import upgrade_steps as u; print(u.read_retired('.', None, None))"` runs from
  the govkit kit over gov's tree it prints the row `command:build` with successor `none`, and over a
  scratch registry whose row reads `id = "nope:build"` it refuses naming the unknown class `nope`.
  Red when: an id of no declared class is read as a retired surface.
- **AC2** — When `python shims.py --fixture --plant skill-rename` runs, `--write` renders the forwarder of §4 at
  `from` naming `to`'s Skill, and `--check` reds a hand edit to it; with `skill-held`, a command `to`,
  `--write` writes nothing and `--check` is green while `from` exists and reds once it is deleted.
  Red when: a held client is overwritten by a render, or a renamed Skill gets no forwarder.
- **AC3** — When `python shims.py --check` runs over gov's tree it grades the `roles/build-skill` row
  green, and with `skill-closed`, the row closed with its window not yet allowed by the plant's
  release count, `check_shim_windows` holds it naming `install.deprecation-window`. Over the same tree
  `git ls-files -- tools/roles/SKILL.template.md` prints the held client and `git grep -c
  '\.claude/skills/build/SKILL.md' -- tools/roles/kit.toml` prints `tools/roles/kit.toml:3`, its `to`,
  `probe` and `pattern` rows, all kept while the row is open.
  Red when: the row closes before the window, a `skill` row is refused as an unknown kind, or the held
  client or one of its install rows is gone while the row is open.
- **AC4** — When `python check_policy.py --readers /build --kind value --except <path>…` runs on a
  scratch clone of the tip with the row closed and the held set of S4 removed, each `--except` naming
  `registry.toml`, `shims.toml` or `usage.toml`, it exits 0; the same run with a planted line naming
  `/build` in `help/roles.md` exits 1 naming that file and line.
  Red when: a reader of `/build` survives the removal and the inventory passes.
  fixture: the scratch clone is built under `%TEMP%` with a short name.
- **AC5** — When `grep -n 'run.py' AGENTS.md coding-governance-agents.template.md` runs after the render,
  each names the attended-build line, and `grep -c '/build' SKILL.md` over the kickoff card prints 0.
  Red when: the charter or the kickoff card still sends an attended build to `/build`.
- **AC6** — When ``grep -n '`skill`' shims.md`` and `grep -n 'held client' shims.md` run over the help
  page after S5, each prints at least one line, and the same two greps over the page at base print
  nothing.
  Red when: the page omits the kind or the held client, so a grep that matched the page's existing
  `held` lines (`help/shims.md:16`, `:44`, `:48`) would read green before S5 is written.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `manifest-check self-test` · `scratch-guard self-test` · `transition-audit arms` · `straggler-guard arms` · `playbook render wiring` · `playbook render selftest` · `check-wiring self-test` · `roles render wiring` · `roles adopter self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the `skill` plants run with `skill` absent from `KINDS`, `write_shims` rendering over a held client, and `read_retired` skipping the class check · none

## 8. Open questions

- **F1 — What id does the `[[retired]]` row carry?** (a) `command:build`, the step gate's member
  spelling and the usage table's id, with `read_retired` admitting a `<class>:<name>` id of a declared
  class; (b) `build`, read as an entry id; (c) a step id such as `roles/build`. (b) names an entry no
  registry holds, and a later entry named `build` would collide; (c) is read against the step
  population and is no step. Rung 3, the option that reuses the step gate's own grammar. RESOLVED
  (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none
- **F2 — What does the `skill` kind do with a client kept for the window?** (a) A command `to` holds the
  kit's rendered client open and renders nothing, a Skill `to` renders a forwarder; (b) every `skill`
  row renders a generated forwarder, the client replaced by it; (c) no row, the client kept by hand.
  (b) fails the clause's "the client … kept", the hosted-in-session procedure leaving with it; (c)
  leaves "then removed" to memory, since no window is read without a row. Rung 1, the clause answers
  it, and (a) also gives PLAY-dConvergedCharter-9 its rename forwarder. RESOLVED (agent, 2026-11-03,
  delegated): (a). widens: none · relaxes: none
- **F3 — Where does the charter's attended-build line live?** (a) In a `kit:runtime` fence, since
  `run.py` ships in the runtime kit TOOL-dWellOiledMachine-25 declares; (b) left in `kit:roles`. (b)
  drops the line from a repository that installs the runtime kit without the roles kit, and keeps it
  where `run.py` is absent. Rung 3. RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft.
- rev-2 · 2026-11-04 · S4 S5 §3 AC3 AC6 · folded `2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1`
  findings 17 (AC6 greps the new kind and the held client and is red at base), 4 (closing the row is
  the roles kit's release-bound act, the non-goal and the hands-off edge to PLAY-dConvergedCharter-20
  saying so), 1 (the held `/build` client stays until the row closes, which is why
  PLAY-dConvergedCharter-9 AC2 excludes it) and 2 (the roles kit's `to`, `probe` and `pattern` rows stay
  while the row is open, admitted by PLAY-dConvergedCharter-9 S7 as a held client's install rows).

## 10. Reuse audit

The seams extended: the succession grammar and its reader (`tools/govkit/registry.toml:190-195`,
`read_retired` at `tools/govkit/upgrade_steps.py:890`), the shim table and its renderer, parity and
window checks (`tools/govkit/shims.py:48-108`, `:232-305`, `:348`), the step gate's `command` class
(`surface-classes.toml`), and PLAY-dConvergedCharter-11's `derive_readers` for the inventory. `python
tools/codebase-map/reuse_lookup.py "retire a Skill with a retired row and a forwarder held for the
deprecation window"` ranked `read_shim_rows`, `check_shim_windows` and `read_retired`, each extended
here, and no Skill-specific forwarder: the shim kinds stop at `command`, `hook` and `module` (`:48`).
Scout C's row holds at `d8a12f046`: the install row `tools/roles/kit.toml:55-57`, the probe at `:90`
(its block `:88-92`), the `[[lf_pin]]` at `:145`, and `adopt-roles.sh` writing the Skill at `:249`.

Recall terms used: `python tools/memory-recall/query.py "how is the build Skill retired with its client
kept for the deprecation window" --terms "/build Skill retired client run.py shim deprecation-window
retired row SK-1 roles kit"`
