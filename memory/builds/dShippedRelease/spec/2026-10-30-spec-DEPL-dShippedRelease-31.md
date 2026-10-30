# DEPL-dShippedRelease-31 — the adopter register, and the word fleet left to node units

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 4 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0441@1aab6ce8 whole
**Carries:** node:record-kind.adopter-register
**Carries:** node:record-kind.adopters

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 |
| [2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md](../build/2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md) | research | DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-20 DEPL-dShippedRelease-25 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 |

<!-- /gen:spec-records -->

## 1. Goal

"Fleet" names more than one thing (`gap-deploy-29`), and the list of adopters is a name ban with no
remote, no branch and no grant, one row lacking even a `key`. This unit grows `adopters.toml` into the
adopter register, with one reader and a registration verb that probes before it writes, declares the
two record kinds gov's reading of an adopter needs, and leaves the word fleet to node units: its
adopter sense and its all-builds sense are renamed, a node's sense stays.

## 2. Scope (IN)

- **S1** — The register's rows (I6). `tools/govkit/adopters.toml` rows hold `key` (required, neutral),
  `names` (required), and `remote`, `branch` and `grant`, each absent until registered. The row with
  no `key` at `:20` gains one. `grant` is one of `read` or `branch-push`, the scope an adopter gave and
  never a value. Observed by AC1.
- **S2** — The one reader, `read_adopter_rows(root)` in `tools/govkit/govkit.py`, I6's `adopter_rows`
  (§8 F1): every row, or a refusal naming the row for a missing `key`, a repeated `key`, empty `names`,
  a key spelling a name, a `grant` off the set, or a `remote` carrying a credential. Each returned row
  carries `registered`, true only when `remote`, `branch` and `grant` are all present. Selfcheck arm
  10 (`tools/govkit/govkit.py:3731`) reads through it and drops its `an adopter` fallback, since every
  row now has a key. Observed by AC1 and AC2.
  **Readers:** by name: `tools/govkit/govkit.py` arm 10 and its `_akey` table, `tools/govkit/selftest.py`
  · by value: arm 10's scan, whose `names` population is unchanged.
- **S3** — The registration verb, the owner's FK-11-2 (layer-memory:438), `python
  tools/govkit/govkit.py register --key <k> --name <brand> --remote <url> --branch <b> --grant <scope>`,
  `cmd_register`. It refuses what S2 refuses, probes the remote with a one-ref read of `<b>` factored
  out of `resolve_measurer_currency` (`:612`) as `read_remote_tip`, refuses when that read fails or
  finds no such ref, and only then writes the row, adding to an existing `key` or appending one.
  Observed by AC3 and AC4.
- **S4** — The record kinds, one row each in `tools/memory-tree/record-kinds.toml` through
  `record_kinds.py new` (TOOL-dTotalRecall-1 S9): `adopter-register` (`rows`, home
  `tools/govkit/adopters.toml`, writer `govkit.py register`, reader `kits.adopters`) and `adopters`
  (`fields`, gov's reading of one adopter per release, home `refs/gov/adopters/<key>`, writer
  `kits.adopters`). Observed by AC5.
- **S5** — The adopter sense renamed to "adopters": `WIRE-INTO-PROJECT.md:545`,
  `tools/codebase-map/README.md:123`, `tools/codebase-map/map_lib.py:62` and `:1326`,
  `tools/codebase-map/test_codebase_map.py:194` and `tools/codebase-map/test_codebase_map.template.py:194`,
  and `tools/govkit/selftest.py:4183`. Observed by AC6.
- **S6** — The all-builds sense renamed, a parsed interface (§8 F2). The line
  `unattended: check 23 fleet —` (`tools/unattended/check-unattended.sh:4415`) becomes `unattended:
  check 23 builds —`, and its reader moves with it in one commit: `_FLEET_HEAD`, `_parse_fleet_line`,
  `measure_fleet_over_budget` and the signal `fleet_over_budget` in
  `tools/drift-audit/drift_report.py` become `_BUILDS_HEAD`, `_parse_builds_line`,
  `measure_builds_over_budget` and `builds_over_budget`. Observed by AC7 and AC8.
  **Readers:** by name: `tools/unattended/check-unattended.sh`, `tools/unattended/check-unattended.test.sh`,
  `tools/unattended/cross-component.test.sh`, `tools/unattended/.unattended.conf.example`,
  `tools/unattended/PROTOCOL.template.md` and its render `memory/guides/UNATTENDED-PROTOCOL.md`,
  `.unattended.conf`, `tools/drift-audit/drift_report.py`, `tools/drift-audit/selftest.py`,
  `tools/drift-audit/README.md` · by value: `_parse_fleet_line`'s three readings, the `over` field, the
  record count and the `at` sha, unchanged but for the head they anchor on. A run record written
  before the update holds the old head and reads DEAD PROBE until the next bar, which is the honest
  answer and needs no second spelling.
- **S7** — The stray senses a reader cannot take for a node: `tools/govkit/selftest.py:5510`, kits;
  `tools/process-monitor/README.md:7` and `tools/process-monitor/procmon-hook.js:10`, agents;
  `tools/codebase-map/reuse_lookup.py:802`, worktrees; `tools/unattended/check-unattended.sh:603` and
  `:4029`-`:4407`'s comments, runs and builds. A comment meaning this repository's nodes stays.
  NOT OBSERVED by a criterion: comment prose, read at the diff review.
- **S8** — The docs: `help/kits.md` gains the register and `register`; `WIRE-INTO-PROJECT.md` names
  the verb where an adopter is first added. NOT OBSERVED as behaviour: prose.

## 3. Non-goals (OUT)

- `kits.adopters` and `kits.currency`, the programs that read the register: DEPL-dShippedRelease-7.
- Filling the three rows' `remote`, `branch` and `grant`: those are facts of each adopter, no record
  in this tree holds them, and `register` is how an owner enters them.
- Probing a `branch-push` grant. A push cannot be tried without pushing; S3 proves the remote and
  branch are readable, and DEPL-dShippedRelease-16's first offer proves the rest.
- The file `tools/playbook/fleet.toml`, `FLEET_*` names, `.gitattributes` and every comment meaning
  the node set: a node's sense is the sense the clause keeps.
- Renaming ids such as `TOOL-aMendedFleet-42`, and any tracked record under `memory/builds/`.
- A gate on the word. Sense cannot be graded by a pattern, so no leg holds it; S6's parsed line is
  the one spot a test pins.

### Edges

- **hands-off** `DEPL-dShippedRelease-7` — `read_adopter_rows`, I6's `adopter_rows`, the one reader of the register that `kits.adopters` walks, and the `adopters` record's home and `registered` flag
- **consumes-from** external — TOOL-dTotalRecall-1 (`record-kinds.toml`, `record_kinds.py new`) and TOOL-dSafePassage-38 (`test_credential_bearing`), each specced and unbuilt at this base, so each is a build-run precondition

## 4. Design

### Evidence

Read at `5d1c82ac`; no product file differs from base `f4597719`.

- `tools/govkit/adopters.toml:15-25` holds three rows; two have `key` and `names`, one `names` alone.
  Arm 10 reads them at `tools/govkit/govkit.py:3742`, with the fallback "an adopter" at `:3753`.
- `git grep -i -w fleet` over `:!memory` finds the senses tabulated here, read line by line.

| Sense | Sites | Disposition |
|---|---|---|
| nodes | `tools/playbook/`, `.gitattributes`, `.governance/deploy.toml`, `.unattended.conf:122`, `tools/push-main.sh:1008`, `:1153`, most "this fleet" comments | stays |
| adopters | S5's seven sites | renamed |
| every build in a tree | `check 23 fleet`, `fleet_over_budget`, S6's readers | renamed |
| kits, agents, worktrees, runs | S7's sites | renamed |

- `_FLEET_HEAD` is `tools/drift-audit/drift_report.py:3197`, and a line that does not parse is detail,
  never a count, so an old-head record is a DEAD PROBE and not a green.
- `resolve_measurer_currency` (`:612`) is the one `ls-remote` read in govkit, and it never fetches.

### Data model

```toml
# tools/govkit/adopters.toml
[[adopter]]
key = "ic"
names = ["<brand>"]
remote = "https://example.invalid/owner/repo.git"
branch = "main"
grant = "read"
```

```python
def read_adopter_rows(root) -> list[dict]:
    # keys: key, names, remote, branch, grant, registered
```

The `adopters` record, one per (key, release), on the ref `refs/gov/adopters/<key>`, so a second node
reads it and no bar grades a cadence's write:

| Field | Holds |
|---|---|
| `key` | the register's neutral key, never a brand |
| `release` | the tag gov read against |
| `receipt-sha` | the adopter's tip the receipt was read at |
| `behind` | releases behind, per kit |
| `steps-pending` | its receipt's `steps` still pending |
| `reading` | `read`, `unverified` or `unregistered` |

`read_adopter_rows` is gov-side alone: `tools/govkit/` is not installable, so the register never
reaches an adopter, which is the file's own opening claim.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `read_adopter_rows`, `cmd_register`, `read_remote_tip` | functions, `tools/govkit/govkit.py` | `py.function`, each OK by `--suggest` at `5d1c82ac` |
| `register` | govkit verb | none |
| `refs/gov/adopters/<key>` | ref namespace | none |
| `_BUILDS_HEAD`, `_parse_builds_line`, `measure_builds_over_budget`, `builds_over_budget` | renames in `tools/drift-audit/drift_report.py` | `py.function`, OK by `--suggest` |
| `adopter-register`, `adopters` | record kinds | none |

`adopter_rows`, I6's proposed spelling, is refused: `--suggest` answers that `adopter` is no declared
verb. `read_adopter_rows` is the same name with the verb the cell asks for.

### Migration

Additive for the register. A new `key` on the keyless row moves the one spelling arm 10 prints. The
line rename ships in two kits, unattended and drift-audit, which `update` moves together.

### Rollout

Live at landing. `kits.adopters` reads every row `unregistered` until an owner runs `register`.

### Files touched (estimate)

- `tools/govkit/adopters.toml`, `tools/govkit/govkit.py`, `tools/govkit/selftest.py`: S1, S2, S3, S5, S7
- `tools/memory-tree/record-kinds.toml`: S4
- `tools/codebase-map/README.md`, `tools/codebase-map/map_lib.py`,
  `tools/codebase-map/test_codebase_map.py`, `tools/codebase-map/test_codebase_map.template.py`,
  `tools/codebase-map/reuse_lookup.py`: S5, S7
- `WIRE-INTO-PROJECT.md`, `help/kits.md`: S5, S8
- `tools/unattended/check-unattended.sh`, `tools/unattended/check-unattended.test.sh`,
  `tools/unattended/cross-component.test.sh`, `tools/unattended/.unattended.conf.example`,
  `tools/unattended/PROTOCOL.template.md`, `.unattended.conf`: S6
- `memory/guides/UNATTENDED-PROTOCOL.md`, rendered by `tools/unattended/adopt-unattended.sh` from its
  template
- `tools/drift-audit/drift_report.py`, `tools/drift-audit/selftest.py`, `tools/drift-audit/README.md`: S6
- `tools/process-monitor/README.md`, `tools/process-monitor/procmon-hook.js`: S7

### Alternatives rejected

- **Leaving `check 23 fleet` and reading the clause as adopters only.** The clause leaves the word to
  node units, so a third sense stays a defect; the cost is 46 tracked lines in ten files, PINNED at
  `5d1c82ac`, and each reader moves in one commit.
- **Reading both heads for a release.** A stale record already reads DEAD PROBE and never green, so a
  second spelling buys one bar's reading at the price of a shim with no deadline.
- **A separate register file for the new columns.** Two files for one row, and the file is already the
  ban's source; `[one-fact]`.
- **A committed `adopters` record.** A cadence program on a host cannot land a commit without the
  lander's bar, and C2 made the same call for the landing record.

## 5. Production-readiness checklist

- security — `remote` is written only through S2, which refuses a credential by
  `test_credential_bearing` (TOOL-dSafePassage-38 S1); `grant` is a scope name, never a value; the
  file never ships. `register` runs one read-only `ls-remote` under the operator's own environment.
- perf / scale — one network read per registration.
- error / empty / loading states — a row with no `remote` is `unregistered`, which a reader must
  report and never read green; an unreachable remote refuses the write.
- observability — `register` prints the tip it read; `read_adopter_rows`' refusals name the row.
- risks — the three rows stay unregistered until an owner acts, so `gap-deploy-04`'s watch reads
  nothing real on the day it lands; DEPL-dShippedRelease-7 reports that state, and it is named here.
- testing — the plants of §6, each against a local bare repository, never a real adopter.
- migration — §4.
- user docs — `help/kits.md`.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs on the tree it exits 0 with every row
  keyed; with a row's `key` removed, or a repeated one, in a scratch copy it exits 1 naming the row.
  Red when: a keyless row passes, which is the disagreement this unit closes.
  figure: DERIVED; three rows at `5d1c82ac`.
- **AC2** — When a scratch shipped file spells a row's `names` member, `selfcheck` exits 1 naming the
  file and printing that row's `key`, never the brand as the citation; with only the `key` spelled it
  exits 0.
  Red when: a shipped file can name an adopter. This is the fixture the clause's "never for an adopter"
  rests on.
  fixture: a scratch copy under `%TEMP%/<short-name>`.
- **AC3** — When `python tools/govkit/govkit.py register --key zz --name Brandzz --remote <bare>`
  with `--branch main --grant read` runs in a scratch copy against a local bare repository holding `main`, it exits 0,
  the row appears, and `read_adopter_rows` returns `registered` true.
  Red when: the verb writes no row, or a row with no probe.
- **AC4** — When `register` runs with a `--branch` the bare repository lacks, or an unreachable
  `--remote`, it exits non-zero and the file is byte-identical; with a `--remote` carrying userinfo it
  refuses before any network read and prints no password.
  Red when: a failed probe writes a row, or a credential is stored or printed.
- **AC5** — When `python record_kinds.py check` runs the registry holds `adopter-register` and
  `adopters`, tags `record.adopter-register` and `record.adopters`, and a row for each with `writer`.
  Red when: a kind has no writer or home, so the node is named and unbuilt.
- **AC6** — When `git grep -n -i "the fleet\b"` runs over the seven paths of S5 it prints no line.
  Red when: an adopter-sense site keeps the word.
  fixture: the paths are arguments to the grep.
- **AC7** — When `bash tools/unattended/check-unattended.sh` runs on a fixture holding a dispatch
  record, it prints a line opening `unattended: check 23 builds —`, and `git grep -c "check 23 fleet"
  -- tools` prints nothing.
  Red when: the old head survives anywhere a reader anchors.
- **AC8** — When `measure_builds_over_budget` reads a run record holding the new line it parses `over`
  and `at`, and on one holding the old head it reads DEAD PROBE and no count.
  Red when: the reader misses the new head, or an old line reads green.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `recall floor` · `recall floor arms` · `drift-audit selftest` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 · a scratch register and a local bare repository, its failing case a keyless row; a planted shipped name for arm 10 · none
New arm: tools/unattended/check-unattended.test.sh · covers AC7 · the line's head asserted, its failing case the old head · none
New arm: tools/drift-audit/selftest.py · covers AC8 · a fixture run record under each head, its failing case a stale line read as a count · none

## 8. Open questions

- **F1 — I6's reader spelling.** `adopter_rows` is refused by the naming lexicon. Options: (a)
  `read_adopter_rows`; (b) a lexicon verb for `adopter`. (b) changes a repo-wide table for one name.
  RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, the shared interface's proposed spelling
  refined by its owner. widens: none · relaxes: none
- **F2 — The third sense, `check 23 fleet`.** Options: (a) rename the line and its reader in one
  commit; (b) leave it and read the clause as adopters only; (c) read both heads. The clause says the
  word is left to node units, and a parsed line reading "fleet" for builds is neither. (c) adds a
  shim with no end. RESOLVED (agent, 2026-10-30, delegated): (a), rung 1. widens: none · relaxes: none
- **F3 — The keyless row.** Options: (a) mint a two-letter key in the file's style; (b) keep the
  fallback "an adopter". (b) leaves an `adopters` record unable to name it neutrally. RESOLVED (agent,
  2026-10-30, delegated): (a), rung 3. widens: none · relaxes: none
- **F4 — What `register` may prove of a grant.** Options: (a) a read-only probe of remote and branch,
  `branch-push` declared and proved at the first offer; (b) a dry-run push. A dry-run pack exchange
  needs a writable remote and proves no ref permission on every host. RESOLVED (agent, 2026-10-30,
  delegated): (a), rung 3, and §3 says what it does not check. widens: none · relaxes: none
- **F5 — The `adopters` record's home.** Options: (a) `refs/gov/adopters/<key>`, C2's form; (b) a
  tracked file; (c) a local journal. (b) needs a landing per reading and (c) no second node can read.
  RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, pin C2's reasoning, proposed to
  DEPL-dShippedRelease-7, its writer. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, from the packet's Items 31, `gap-deploy-29`, layer-memory:437-438,
  :499, layer-expansions:458-459, scout D's rows and disagreements 13 and 14, and the spec brief's I6.

## 10. Reuse audit

The seams extended are `tools/govkit/adopters.toml` with its reader at `tools/govkit/govkit.py:3742`,
`resolve_measurer_currency` (`:612`) for the probe, and `record_kinds.py new` for the two kinds.
`python tools/codebase-map/reuse_lookup.py "read an adopter's row from a register and probe its
remote"` ranked name-stem hits (`rows`, `read_text`, `probe`, `read_journal`); none holds a
register, and `tools/govkit/census.py:122` needs a checkout, so it is shape reference only. Scout D's
disagreement 13 holds with three additions found by reading each `git grep` hit: `map_lib.py:1326` and
`tools/govkit/selftest.py:4183` are adopter-sense sites it missed, and the kit, agent and worktree
senses of S7 are a fourth group. The packet's "the register of adopters" is, at source, a ban list:
no file calls it a fleet register, as the scout found.

Recall terms used: `python tools/memory-recall/query.py "how does the adopter register grow from a name ban and where does the word fleet belong" --terms "adopters.toml adopter register key names remote grant registration FK-11-2 fleet node units"`
