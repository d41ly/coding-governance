# DEPL-aScoutedSeam-1 — adopters get the scout and a resolved host tree, and the adopter-side gaps the research found are handed over

**Status:** SPECCED · rev-2 · 2026-10-11 · node a · Tier-2 · base d19938f3 · streams deployer+kickoff · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aScoutedSeam-1-1-failure-analysis.md](../build/2026-10-11-build-TOOL-aScoutedSeam-1-1-failure-analysis.md) | research | TOOL-aScoutedSeam-1 TOOL-aScoutedSeam-2 TOOL-aScoutedSeam-3 KICK-aScoutedSeam-1 |
| [2026-10-13-prompt-TOOL-aScoutedSeam-1-brief.md](../prompts/2026-10-13-prompt-TOOL-aScoutedSeam-1-brief.md) | research | TOOL-aScoutedSeam-1 KICK-aScoutedSeam-1 TOOL-aScoutedSeam-3 |

<!-- /gen:spec-records -->

## 1. Goal

Put the reuse scout where the measured reinventions happened: inCMS and NicoCares. A NicoCares page
builds with tokens and DSL vocabulary that live half in inCMS core. That package's lookup reads only
its own map and has zero symbols, so the scout must be handed the host tree, resolved per node. The
research also found adopter-side causes no gov tool can fix. This unit states them where an adopter
reads them.

## 2. Scope (IN)

- **S1** — Host-tree resolution, a kickoff checker verb `manifest-check.sh --reuse-hosts`. It prints
  one absolute path per line, or `hosts: none`, from the first rung that answers:
  1. the environment variable `GOV_REUSE_HOSTS`, absolute paths separated by the platform's path
     separator, the per-node rung;
  2. `git rev-parse --show-superproject-working-tree`, when the repository is checked out as a
     submodule of its host;
  3. `REUSE_HOST_TREES` in `.unattended.conf`, paths relative to the repository root, the
     project-wide rung.

  Every printed path must be a git work tree; one that is not refuses, naming it. The rung that
  answered is printed with the paths.
  - AC1 observes it.
- **S2** — The kickoff catalog line of `KICK-aScoutedSeam-1` passes the verb's output as `hostTrees`,
  and as one `--host` each to `TOOL-aScoutedSeam-1`'s house index, so the index lists the host's
  tokens, copies and kinds too. The role reads a host tree for its design system and its shared code,
  and never writes it.
  - AC2 observes it.
- **S3** — The adopter's example conf carries both keys blank, with comments: `REUSE_SCOUT_DEFAULT`
  (blank means kickoff asks) and `REUSE_HOST_TREES`. This repo's own `.unattended.conf` carries
  `REUSE_HOST_TREES` blank.
  - AC3 observes it.
- **S4** — `WIRE-INTO-PROJECT.md` gains a reuse-scout section. It says what the owner decides (the
  opt-in default and the host tree), what the scout costs as `TOOL-aScoutedSeam-1`'s calibration
  measured it, and the adopter's own checklist the research produced:
  - give every reusable component a dossier whose `## Reuse affordance` names the factory a caller
    uses, not its internals;
  - keep the charter from denying a design system the repository has;
  - never let a lint opt-out sanction the bypass of a shared seam;
  - extend a style gate from colour to the lengths and type a token layer owns;
  - declare the lint-rule directory and the DSL vocabulary in `.codebase-map.conf`'s
    `HOUSE_INDEX_DIRS` and `HOUSE_INDEX_KINDS`, so the house index lists them.
  - AC4 observes it.
- **S5** — The scout's files reach an adopter through the kits that already carry them: the
  review-harness kit renders `reuse-scout.js` at the adopter's fan-out cap, the kickoff kit carries
  the verbs, and the memory-tree kit carries the §10 join. No new kit and no new descriptor.
  - AC5 observes it.

## 3. Non-goals (OUT)

- Editing inCMS or NicoCares. The adopter-side findings are handed over below and in S4's checklist,
  never fixed from gov.
- A host-tree resolver that clones or fetches. A host that is not on the node is `hosts: none`,
  announced.
- Arming any adopter's `REUSE_SCOUT_DEFAULT`. That is each owner's opt-in.

### Edges

- **consumes-from** `KICK-aScoutedSeam-1` — the catalog line and the opt-in verb this unit's host
  verb sits beside.
- **consumes-from** `TOOL-aScoutedSeam-1` — the harness's `hostTrees` argument, and the calibration
  figures S4 quotes.
- **hands-off** external — to the NicoCares owner: its charter's "no design system of its own" claim,
  which predates the 101-token layer, and its design gates, which refuse palette literals but not
  lengths or type.
- **hands-off** external — to the inCMS owner: the media gallery has no dossier (its help key sits
  unclaimed in the map baseline), and `incms/focal-coverage` offers "a bare-URL image, no mediaId" as a
  sanctioned opt-out. Five image fields shipped as text boxes between 2026-07-03 and 07-20 are still
  at HEAD. The M1c trial's index read the custom lint rules and the DSL node kinds from inCMS paths
  it hardcoded; the deployed index reads them only once the inCMS owner declares the two
  house-index keys.

## 4. Design

### The ladder

The per-node rung comes first because the node registry says roots differ by node, so a path that is
right on one node is wrong on another. The superproject rung comes second because it answers with no
configuration wherever a package is checked out inside its host. Measured on node `a`: NicoCares'
checkout printed `C:/projects/incms/main`. The conf rung is last because a project-wide relative path
holds only on nodes sharing a layout.

### Inventory

| identifier | cell |
|---|---|
| `--reuse-hosts` | checker verb, no naming cell |
| `resolve_reuse_hosts` | sh.function |
| `GOV_REUSE_HOSTS` | environment variable |
| `REUSE_HOST_TREES` | conf key |

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `skills/session-kickoff/MANIFEST-TEMPLATE.md`
- `tools/unattended/.unattended.conf.example`
- `.unattended.conf`
- `WIRE-INTO-PROJECT.md`

### Rollout

Through `govkit update` like every kit change. An adopter that never opts in sees two blank conf keys
and one runbook section.

### Alternatives rejected

- **A per-repository host map in the codebase map's conf.** The verb lives in the kickoff kit, and a
  kit file names nothing outside itself.
- **Indexing the host's map into the package's lookup.** The benchmark found the design layer by
  reading, and the lookup is not the mechanism.

## 5. Production-readiness checklist

- security: host trees are read-only to the scout. The env rung takes absolute paths only, and each
  must be a git work tree.
- perf / scale: a host tree enlarges what the design lens may read. The role's tool-call budget
  bounds it, not the tree's size.
- error / empty / loading states: no host is `hosts: none`, printed. An unreadable env path refuses
  by name.
- observability: the rung that answered is printed with the paths.
- risks: a stale env path on one node points at an old host checkout. It must be a work tree, but its
  revision is not checked.
- testing: `manifest-check.test.sh` gains one fixture per rung, including a submodule fixture.
- migration: N/A — new blank keys.
- user docs: the runbook section (S4).

## 6. Acceptance criteria

- **AC1** — When `manifest-check.sh --reuse-hosts` runs in a fixture repository checked out as a
  submodule of a fixture host, it prints the host's path and the rung `superproject`. With
  `GOV_REUSE_HOSTS` set it prints that path and the rung `env`. With neither it prints `hosts: none`.
  Red when: a path that is not a git work tree is printed instead of refused.
- **AC2** — When the kickoff catalog line is read from `MANIFEST-TEMPLATE.md`, it passes the
  `--reuse-hosts` output as `hostTrees`.
  Red when: the catalog line passes an empty list unconditionally.
- **AC3** — When `govkit.py plan` runs for a fixture adopter, the planned `.unattended.conf.example`
  carries `REUSE_SCOUT_DEFAULT` and `REUSE_HOST_TREES`, both blank.
  Red when: either key ships armed.
- **AC4** — When `WIRE-INTO-PROJECT.md` is read, its reuse-scout section names the two owner
  decisions, the measured cost with its date, and the four checklist items.
  Red when: the cost is written without the date it was measured.
- **AC5** — When `govkit.py plan` runs for a fixture adopter selecting the review-harness kit,
  `reuse-scout.js` is planned as a rendered file at the adopter's fan-out cap.
  Red when: the harness ships as an engine file spelling the literal cap.

## 7. Gates

`kickoff-manifest ratchet` · `manifest-check self-test` · `govkit selfcheck` · `kit placeholders (a declared token its adopter substitutes)` · `memory hygiene` · `lexicon naming predicates` · `scratch-guard self-test`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 · a fixture host with a submodule checkout, staged per rung · none

## 8. Open questions

- **F1 — Should the superproject rung be ahead of the env rung?** It needs no configuration, but a
  node that checks the package out somewhere else, with the host elsewhere still, needs the env to
  win. Recommendation: env first, as written.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · S2 · S4 · §3 · `TOOL-aScoutedSeam-1` rev-4 added the house index. The host trees
  feed it, the adopter checklist gains the two listing keys, and the inCMS hand-off names them.

## 10. Reuse audit

The verb extends `skills/session-kickoff/manifest-check.sh` beside `KICK-aScoutedSeam-1`'s
`--reuse-opt-in`. The conf keys sit beside `SPEC_AUDIT_DEFAULT` in `.unattended.conf`. The runbook
section follows the shape of WIRE-INTO-PROJECT's codebase-map section, which already tells an adopter
to run the lookup before building. `tools/codebase-map/reuse_lookup.py "resolve the host repository a
package installs into"` ranked one candidate, `resolve` in `tools/memory-recall/recall_conf.py`. That
resolves the recall kit's conf, not a host or superproject tree, so no existing seam fits beyond the
checker this verb joins.

Recall terms used: host tree superproject submodule package incms nicocares adopter runbook conf key kickoff verb
