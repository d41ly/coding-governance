# TOOL-dFurnishedOrders-1 — the orientation scout composing the card in a sidechain at session start, its recall re-verified once at entry and a moved-source record handed as stale

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 2193e25d · streams tooling · order 5 · advances TOOL-dFurnishedOrders-21

**Carries:** cl-dClosedLoop-0192@e52307f5 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-a.md) | research | TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-b.md) | research | TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-c.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-c.md) | research | TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-fix-return.md) | research | TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md) | research | TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-1-reuse-scout.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-1-reuse-scout.md) | journal | — |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-1-spec-writer.md) | journal | — |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-2-reuse-scout.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-2-reuse-scout.md) | journal | — |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-3-reuse-scout.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-3-reuse-scout.md) | journal | — |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md) | research | TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-fix-brief.md) | research | TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 |

<!-- /gen:spec-records -->

## 1. Goal

The orientation scout the design relies on has never run: 0 of 3,283 recorded subagents is a
`gov-orienter`, and the main loop runs the kickoff inline (gap-orient-15,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:146`). Recall
prints a banner telling every reader to re-verify (`EVIDENCE_BANNER`,
`tools/memory-recall/query.py:172`), and nothing compares a recalled record with the sources it
cites. This unit moves orientation into a sidechain at session start, re-verifies the card's recalled
records once, at the card's append, by the rule `measure_dossier_staleness` already applies to
dossiers, and hands a record whose source moved as stale, naming the source, on the card and on the
fact line (P29 items 3 and 8, `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md:260-262`
and `:314-316`).

## 2. Scope (IN)

- **S1** — One staleness rule. `measure_claim_staleness(commits, owner, claimed)` in
  `tools/codebase-map/map_lib.py`, extracted from `measure_dossier_staleness` (`map_lib.py:1812-1858`),
  which then calls it once per dossier with the dossier's path and its claimed paths: `owner` is
  STALE when a commit touching a path of `claimed` is not an ancestor of `owner`'s own last commit.
  It returns the record `{refreshed, stale, behind, newest, newest_path}`, `newest_path` the claimed
  path the newest such commit touched. Ancestry, never dates, as the docstring states today.
  Observed by AC3.
- **S2** — A record's cited sources. `read_cited_paths(root, record, refreshed)` in `map_lib.py`:
  every code span of the record's text (`_CODE_SPAN_RE`, `map_lib.py:1208`), its `:<lo>[-<hi>]` tail
  cut off, that names a path tracked at the record's last commit (`git ls-tree -r --name-only
  <refreshed>`), so a source gone from HEAD since is still a cited source. Observed by AC1 and AC2.
- **S3** — The verb. `python tools/codebase-map/map_diff.py --stale-records <record>…` reads the
  history once through `read_commit_paths` (`tools/codebase-map/map_diff.py:130`), applies S1 to each
  record over S2's paths, and prints one line per record: `<record> fresh`, `<record>
  stale=<source path>@<blob12>` (`blob12` the first 12 hex digits of the source's blob at HEAD, or
  the word `absent` when HEAD holds none), or `<record> unmeasured: <why>` (untracked, never
  committed, or a shallow clone). It runs before `require_adopted_root`, because it reads no map.
  Exit 0 on answers, 1 when git cannot print the history, 2 on usage. Observed by AC1 and AC2.
- **S4** — Recall re-verified once, at the append. `check_card_recall` in
  `skills/session-kickoff/manifest-check.sh`, called by `add_card_body` (`:1141`) after
  `check_card_citations`: every path token of the body's `## records` section that is tracked under
  the tree's `MEMORY_ROOT` is handed to S3's verb, found by `resolve_kit_file codebase-map
  map_diff.py` (`:854`) and bounded as the `overlaps —` cell bounds its probe. Each stale record gets
  the annotation line `RECALL — stale <record> stale=<source path>@<blob12>` beneath the row citing
  it, as `UNVERIFIED — ` lines sit beneath theirs; the `appended —` line gains `· <n> stale`. No
  kit, no Python or a verb that fails writes one `RECALL — unchecked: <why>` line under the
  `## records` heading and the append proceeds: unknown, never clean. Observed by AC4 and AC5.
- **S5** — The annotation is not a citation. `extract_card_tokens` (`:886`) blanks a line opening
  `RECALL — ` as it blanks `UNVERIFIED — `, so `--card --check` never judges the `stale=` token as a
  path. Observed by AC6.
- **S6** — The stale mark on the fact line (shared interface J6). `FACT_RE` in
  `tools/roles/roles_lib.py` and its JavaScript copy (TOOL-dBoundRoles-13 S3 and S4) admit one optional
  attribute after the class, ` stale=<source path>@<blob12>` (or `@absent`). `render_handoff`
  (`tools/roles/handoff.py:312`) runs S3's verb once over every `record:` fact of class `claimed`
  whose id is a tracked path, and writes the attribute on each stale one. The key and the class are
  unchanged, so the spawn guard's re-cut compares what it compares today. Observed by AC7.
- **S7** — The scout in a sidechain. `tools/roles/workflows.toml`'s `orient` entry gets `driver =
  "agent"` and the trigger "once per session, at session start, in a sidechain, before the first
  work-unit is opened"; `gov-orienter.agent.md` gets `mandatory: at session start — unenforced —
  <why>` (§8 F2) and a job that runs the engine's Steps 0 to 4, composes the card body, appends it
  with `--card --append --session <sid>` and returns the appended card. Observed by AC8.
- **S8** — The engine says who runs it. `skills/session-kickoff/SKILL.md` gains one paragraph under
  its posture: where the tree ships the roles kit's `gov-orienter`, the main loop spawns it at
  session start with the owner's message and the session id from the `orientation —` header, puts
  the returned card's `## open` rows to the owner and gives Step 5's hand-back; a session where the
  card already carries a READY line returns the stored card through `--card --check`. Where no
  `gov-orienter` ships, the steps run inline as today. Observed by AC8.
- **S9** — The user page. `help/roles.md`, "How a task reaches an agent" step 1, says the
  orientation scout writes the card in a sidechain and that a recalled record whose source moved is
  marked `RECALL — stale`. NOT OBSERVED by a criterion: prose, graded by the memory hygiene leg's
  link checks at the close.

## 3. Non-goals (OUT)

- A gate refusing a session that orients inline (§8 F2): the clause asks for the composition, and no
  clause names an enforcer.
- The scout's placement return and the driver's record of it: TOOL-dBoundRoles-12's.
- Re-cutting a moved key at the spawn: TOOL-dBoundRoles-13 S4's. This unit marks a `claimed`
  record whose cited source moved; a `blob:` key that moved is re-cut there, never marked.
- Re-judging a stale record. Its producer re-judges it only when an item routes it back
  (`layer-roles.md:260-262`); a repair's ask going stale is TOOL-dFurnishedOrders-7's.
- The card's project-map cell: TOOL-dFurnishedOrders-13.
- Recall's own ranking and its banner: `query.py` is unchanged; the re-verification is the append's.
- A record cited only by its id: the verb needs a path, and the Skill's recall step already prints
  `id · path:line`.

### Edges

- **hands-off** `TOOL-dFurnishedOrders-13` — `gov-orienter`, the orientation scout now spawned in a sidechain at session start, whose composed card body unit 13's map cell joins
- **hands-off** `TOOL-dFurnishedOrders-7` — `stale=`, the fact line's stale attribute, which a repaired fact carries once a source its repairing return read moves
- **hands-off** `TOOL-dFurnishedOrders-14` — `stale=`, the fact line's stale attribute, which the repaired fact handed while its ask is open carries when its source moves
- **consumes-from** external — TOOL-dBoundRoles-13's fact line, `FACT_RE`, its JavaScript copy and `render_handoff`'s fact cut, specced and DEFERRED at base `2193e25d`

## 4. Design

### The rule, once

`measure_dossier_staleness` keeps its signature and its rows. Its per-dossier body becomes one call
of `measure_claim_staleness(commits, dossier, claimed)`, where `claimed` is the set of paths
`attribute_paths` gives the dossier's feature. `touched_by` stays the per-commit set it is today for
the dossier loop; the new function recomputes the touches for its own `claimed`, so a lone record
pays one pass over the commit list.

```
measure_claim_staleness(commits, owner, claimed) -> {"refreshed", "stale", "behind", "newest", "newest_path"}
```

`refreshed` is the first commit in topological order naming `owner`; `None` means never committed,
which the verb prints as `unmeasured`.

### The verb's lines

```
memory/builds/tFix/spec/2026-10-01-spec-TOOL-tFix-1.md stale=tools/x/x.py@3b18e512cc0f
memory/builds/tFix/build/2026-10-02-build-TOOL-tFix-1-notes.md fresh
memory/scratch.md unmeasured: not tracked
```

### The card, after the append

```
## records
- memory/builds/tFix/spec/2026-10-01-spec-TOOL-tFix-1.md:40 — the unit's design
RECALL — stale memory/builds/tFix/spec/2026-10-01-spec-TOOL-tFix-1.md stale=tools/x/x.py@3b18e512cc0f
- `TOOL-tFix-2` — an ask
```

The verb runs once per append over every record path the section cites, and never at `--card
--write`: the SessionStart write stays inside its budget, and a body with no `## records` path costs
nothing. The bound and the stderr capture follow `derive_overlaps_line` (`manifest-check.sh:555`):
a kill into a file, never a `$( )` capture.

### The sidechain

The main loop's first act is one `Agent` call, `subagent_type: gov-orienter`, whose prompt names the
owner's message and the session id. The scout holds Bash, so it runs the engine's commands and the
append, whose card lives under `<git-common-dir>/orientation/`, outside the tree; scratch-guard's role
arm already admits a `gov-orienter` running `manifest-check.sh --card`
(`tools/hooks/scratch-guard.test.sh:1117`). The scout never asks: each question becomes an `## open`
row, as its job says today, and the main loop asks them. A card already READY is refreshed by
`--card --check` and returned; the recall marks it carries stand from its one append, which is what
"once at entry" means.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `measure_claim_staleness`, `read_cited_paths` | functions, `map_lib.py` | `py.function`, OK |
| `--stale-records` | flag, `map_diff.py` | none |
| `check_card_recall` | function, `manifest-check.sh` | `sh.function`, OK |
| `RECALL — stale`, `RECALL — unchecked:` | card annotation lines | none |
| ` stale=<source path>@<blob12>` | fact-line attribute (J6) | none |

### Migration

Additive. A card appended before this unit carries no `RECALL —` line and is read as today. A fact
line without the attribute matches the widened `FACT_RE` unchanged.

### Rollout

Live at landing. The kit epoch leg needs the version constants to move with their kits' shipped
bytes: `KIT_CODEBASE_MAP_VERSION` (`map_lib.py`), `KIT_MANIFEST_VERSION` (`manifest-check.sh`),
`KIT_ROLES_VERSION` (`roles_lib.py`) and `KIT_AGENT_CAP_VERSION` (`agent-cap.js`). The engine
measures 18310 of its 18432-byte row (`tools/template-size-limits.txt:63`, PINNED 2026-10-26 by
`wc -c`); a pass whose edit takes it past the row raises the row to 19456 under that file's
run-may-raise terms (§8 F3), argued in place, with the unit's row in `memory/DECISIONS.md`.

### Files touched (estimate)

- `tools/codebase-map/map_lib.py`
- `tools/codebase-map/map_diff.py`
- `tools/codebase-map/selftest.py`
- `tools/codebase-map/README.md`
- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `skills/session-kickoff/SKILL.md`
- `tools/template-size-limits.txt`
- `memory/DECISIONS.md`
- `tools/roles/agents/gov-orienter.agent.md`, rendered to `.claude/agents/gov-orienter.md`,
  `.claude/roles.json`, the catalogue region of `tools/roles/README.md` and the role line of `AGENTS.md`
- `tools/roles/workflows.toml`
- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/adopt-roles.test.sh`
- `tools/hooks/agent-cap.js`
- `help/roles.md`

### Alternatives rejected

- **A `git rev-list` predicate in the kickoff script.** It answers the same question and is a second
  copy of the rule the map already owns (§8 F1).
- **Marking every recall hit in `query.py`.** Every later query would re-verify, which is what P29
  item 8 moves to one boundary, and the recall kit may not import the map kit.

## 5. Production-readiness checklist

- security — no new write path in the tree: the append writes the card it writes today, outside the
  tree. The verb reads git only; a record path reaches git as an argument after `--`, never a shell
  string.
- perf / scale — one `git log --name-only` over the history per append and per render; 0.82 s over
  7,085 commits on node d (PINNED 2026-10-26, `time git log --topo-order --name-only HEAD`).
- error / empty / loading states — every failure is one `RECALL — unchecked: <why>` line; a shallow
  clone is `unmeasured`, never fresh.
- observability — the `appended —` line counts stale records; the verb names the source and blob.
- risks — a record citing a path in a code span it only mentions is marked stale when that path
  moves; the mark is evidence for the reader, never a refusal.
- testing — AC1 to AC8 by a pass over scratch fixtures; the arms of §7 at the close.
- migration — additive, as §4 says.
- user docs — `help/roles.md`, step 1 (S9).

## 6. Acceptance criteria

- **AC1** — When `python map_diff.py --stale-records rec.md` runs in a scratch repository where
  `rec.md` cites `a.py` in a code span and a later commit changes `a.py`, it prints
  `rec.md stale=a.py@` followed by the first 12 hex digits `git rev-parse HEAD:a.py` prints,
  and exits 0.
  Red when: the verb reads the record as fresh though its source moved after it.
  fixture: a scratch repository under `%TEMP%`, built by the pass; the tree holds none today.
- **AC2** — When the AC1 repository gains a commit that edits `rec.md` after the source change, the
  same command prints `rec.md fresh`; when a later commit takes `a.py` out of the tree instead, it prints
  `rec.md stale=a.py@absent`.
  Red when: a record refreshed after its source moved still reads stale, or a source gone from HEAD is not
  cited.
- **AC3** — When `python -c` calls `map_lib.measure_claim_staleness` on the commit list
  `[("c", ("b",), ("a.py",)), ("b", ("a",), ("rec.md",)), ("a", (), ("a.py", "rec.md"))]`
  with owner `rec.md` and claimed `{"a.py"}`, `stale` is true and `newest_path` is `a.py`; with
  the first two commits' paths swapped, `stale` is false.
  Red when: the predicate reads dates or order instead of ancestry.
- **AC4** — When `bash manifest-check.sh --card --append --session s1` runs in a scratch adopter
  holding the kickoff and codebase-map kits and the AC1 history, with a READY body whose
  `## records` row cites `rec.md`, the stored card carries
  `RECALL — stale rec.md stale=a.py@<12 hex>` beneath that row and the `appended —` line reads
  `1 stale`.
  Red when: the planted stale recall is appended unmarked, which is the clause's seen case.
  fixture: the scratch adopter under `%TEMP%`, its `MEMORY_ROOT` holding `rec.md`.
- **AC5** — When the AC4 adopter has no `map_diff.py`, the same append exits 0 and the card carries
  one `RECALL — unchecked:` line under `## records` naming the absent kit.
  Red when: a tree that cannot verify recall reads as verified.
- **AC6** — When `bash manifest-check.sh --card --check --session s1` runs over the AC4 card, it
  reports no `UNVERIFIED` line for the `RECALL — stale` annotation.
  Red when: the annotation's `stale=` token is judged as a cited path.
- **AC7** — When `python handoff.py render --role gov-spec-writer --build tFix --unit TOOL-tFix-1
  --input spec=<a scratch spec citing a.py> --stdout` runs after `a.py` moved, the
  `input:spec` block's fact line ends ` stale=a.py@<12 hex>`, and `roles_lib.FACT_RE` matches it.
  Red when: a claimed record whose source moved is handed with no mark.
  fixture: TOOL-dBoundRoles-13's fact cut, built before this unit by the chain's order (§8 F4).
- **AC8** — When `python -c` reads `roles_lib.load_workflows` and the orienter's front matter, the
  `orient` entry's driver is `agent` and its `mandatory` value carries `unenforced — `; and
  `grep -n 'gov-orienter' SKILL.md` in `skills/session-kickoff/` prints the sidechain paragraph.
  Red when: the engine still has the main loop run Steps 0 to 4 inline where the scout ships.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `manifest-check self-test` · `scratch-guard self-test` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `check-wiring self-test` · `lexicon naming predicates` · `policy fixtures` · `kickoff engine size <=18KiB` · `roles catalogue` · `roles render wiring` · `roles adopter self-test` · `kit epoch (shipped bytes move, the version moves)` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/codebase-map/selftest.py · covers AC1 AC2 AC3 · a scratch history whose cited source moves after the record, then a refresh, then a deletion · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC4 AC5 AC6 · a READY body citing a record whose source moved, appended with and without the map kit · none
New arm: tools/roles/adopt-roles.test.sh · covers AC7 · a render of a scratch spec whose cited source moved · none

## 8. Open questions

- **F1 — Where does the staleness rule live, when the card is the kickoff kit's and the rule the map
  kit's?** Options: (a) extract `measure_claim_staleness` in `map_lib.py`, reached by subprocess
  through `map_diff.py --stale-records`, the route `drift_report.py`'s `build_stale_dossiers` already
  takes to `--stale-dossiers` (`tools/drift-audit/drift_report.py:3441`); (b) a `git rev-list
  HEAD ^<refreshed> -- <path>` predicate inside `manifest-check.sh`; (c) every recall hit marked by
  `query.py`. (c) re-verifies at every query, not once at entry, and the recall kit may not import the
  map kit. (a) and (b) satisfy the same criteria; (b) writes the rule twice. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, tie-broken by reuse of the seam M5 found. widens: none ·
  relaxes: none
- **F2 — Is the sidechain enforced?** Options: (a) `mandatory` with R13's `unenforced — <why>`
  escape (`tools/roles/check_roles.py:51-53`), the spawn counted by the agent ledger as gap-orient-15
  counts it; (b) scratch-guard refuses the main loop's first commit until the session transcript
  shows a `gov-orienter` return. (b) adds a refusal to every session's write gate, which no clause
  names and the unit's tier did not price (veto 3). RESOLVED (agent, 2026-10-26, delegated): (a),
  rung 3. widens: none · relaxes: none
- **F3 — The engine's ceiling has 122 bytes free.** Options: (a) raise
  `skills/session-kickoff/SKILL.md`'s row to 19456 under `tools/template-size-limits.txt:16-26`'s
  run-may-raise terms, only if the pass measures past 18432; (b) fund the paragraph by cutting
  engine prose other units own; (c) put the sidechain only in the role file, so the main loop never
  learns to spawn it, which fails AC8 (veto 1). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3:
  the file states the terms, so the raise changes no governance carrier (BUILD-METHOD M3). widens:
  none · relaxes: none
- **F4 — The parent this unit calls.** S6 extends TOOL-dBoundRoles-13 S3 and S4, DEFERRED at base.
  RESOLVED (agent, 2026-10-26, delegated): the build run re-grounds on TOOL-dBoundRoles-13's fact
  line and stops this unit if that section is still absent then, rung 3, the brief's parent rule.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 1, the brief's J6 and J7, scout A's
  row for cl-0192, P29 items 3 and 8, and the source at `2193e25d`.

## 10. Reuse audit

The seam extended is `measure_dossier_staleness` (`tools/codebase-map/map_lib.py:1812`), whose
per-dossier body becomes `measure_claim_staleness`, reached through `map_diff.py`'s
`read_commit_paths` (`:130`) and a new verb beside `--stale-dossiers`, the route `drift_report.py`
already takes by subprocess. The card side extends `add_card_body` and `extract_card_tokens`
(`skills/session-kickoff/manifest-check.sh:1141`, `:886`) and the sibling resolver
`resolve_kit_file` (`:854`). `python tools/codebase-map/reuse_lookup.py "mark a recalled record stale
when a source it cites changed after the record was last committed"` ranked `records`
(`gotchas.py`), `resolve_cited_paths` (`tools/roles/roles_lib.py:632`, which resolves a role file's
kit citations, not a record's sources) and `build_stale_dossiers`
(`tools/drift-audit/drift_report.py:3441`, the subprocess precedent above); no record-staleness
function exists to extend, so S1 is an extraction, not a new rule. The recall probe returned this
build's brief row, scout A's row and the night pass's clause revision; scout A's
`check_card_citations :916` is the function's line at base and agreed with source.

Recall terms used: `python tools/memory-recall/query.py "how is recall re-verified at session start
and a stale record marked" --terms "orientation scout sidechain card recall stale record source moved
ancestry dossier staleness kickoff"`
