# DEPL-dShippedRelease-22 — the ask tracker's one-way mirror, the adapter `integrations.tracker: mirror-out` selects

**Status:** OPEN · rev-2 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 30 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0432@e42728b4 whole
**Carries:** node:policy-key.integrations.tracker

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-3-reuse-scout-c.md](../build/2026-10-30-build-DEPL-dShippedRelease-3-reuse-scout-c.md) | research | DEPL-dShippedRelease-3 DEPL-dShippedRelease-6 DEPL-dShippedRelease-8 DEPL-dShippedRelease-15 DEPL-dShippedRelease-19 DEPL-dShippedRelease-26 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md](../reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-10 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-31 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-13 DEPL-dShippedRelease-4 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-6 DEPL-dShippedRelease-27 DEPL-dShippedRelease-5 DEPL-dShippedRelease-30 DEPL-dShippedRelease-3 DEPL-dShippedRelease-25 DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-20 DEPL-dShippedRelease-17 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-18 DEPL-dShippedRelease-24 DEPL-dShippedRelease-8 DEPL-dShippedRelease-26 DEPL-dShippedRelease-19 DEPL-dShippedRelease-9 |

<!-- /gen:spec-records -->

## 1. Goal

The ask backlog is the tracker, and an owner who also watches a tracker service has no way to see it
there. This unit adds the one-way mirror that `integrations.tracker: mirror-out` selects: an abstract
adapter row with a declared target, which projects every ask outward and reads nothing back. No service
is named and no external dependency arrives.

## 2. Scope (IN)

Build-run preconditions, specced and DEFERRED at base `f4597719`: TOOL-dWellOiledMachine-20's
`tools/runtime/points.toml`, TOOL-dWellOiledMachine-17's grant check, TOOL-dWellOiledMachine-59's
`point.cadence-items`, and TOOL-dDeclaredLoop-2's `[[selects]]` rows. `gen_build_index.py --asks --json` and
`policy.py get` are landed.

- **S1** — The key's row. `integrations.tracker` gains `summary` and `usage` on its one catalogue row
  (`tools/policy/catalogue.toml:1108`), and its name leaves `tools/policy/unsummarised-keys.txt` by
  `policy.py lists --write`. Allowed values `none` and `mirror-out` and the default `none` stay the row's.
  Observed by AC6.
- **S2** — The reader. `derive_ask_mirror(root)` in `tools/integrations/tracker_mirror.py` runs
  `gen_build_index.py --asks --all --json`, the kit found through the inline `resolve_kit_dir`, so the asks
  and their fold come from `tools/memory-tree/backlog.py` and no journal is read. It keeps `id`, `home`,
  `status`, `sev`, `filed`, `summary` and `pointer`, sorted by `id`. A non-zero exit, or no ask read from a
  tree holding a `BACKLOG.md`, is a dead probe and refuses. Observed by AC2 and AC4.
- **S3** — The program. `python tracker_mirror.py sync` asks `read_policy("integrations.tracker")`. Under
  `none` it prints `tracker mirror — none, nothing mirrored`, writes nothing and exits 0. Under `mirror-out`
  it writes the row's declared target and prints one line with the count and the HEAD SHA. The same tree
  writes the same bytes. `python tracker_mirror.py probe` prints the target and whether the spool's SHA
  is HEAD, and refuses a target it does not know. Observed by AC1, AC2, AC3 and AC5.
- **S4** — The adapter row. One `[[adapter]]` row at a new point `point.memory.ask-mirror` in
  `tools/runtime/points.toml`, `name = "mirror-out"`, made by `adapters.py new`, carrying the header
  `check_adapter_header` grades: `kind = "tracker"`, `grant` local with `secret = "anonymous"`,
  `witness-source`, `probe`, and `fallback = "the ask backlog"`, and one field of its own, `target =
  "spool"`. `tracker` joins `ADAPTER_KINDS` in `tools/integrations/adapters.py`, whose list
  DEPL-dShippedRelease-15 S2 leaves to each later kind. `spool` is the one value and writes
  `<git-common-dir>/tracker-mirror/asks.json`. A later service adapter reads that file. Observed by AC5.
- **S5** — The selection. One `[[selects]]` row in `tools/loop/loop.toml`, key `integrations.tracker`, value
  `mirror-out`, point `point.memory.ask-mirror`, and that word in the `declares` of `layer.memory` and
  the `uses` of `layer.integrations` in `tools/playbook/layers.toml`. Observed by AC7.
- **S6** — The cadence. One `[[adapter]]` row at `point.cadence-items`, `host-key = "kits.host"`, `period =
  "daily"`, `run` naming S3's verb and `events = []`, so a node with a host runs it. Observed by AC8.
- **S7** — One-way. The module opens no network and writes nothing under the memory root. Observed by AC9.
- **S8** — The docs. `help/tracker-mirror.md`, with its row in `help/README.md`, states what a value does,
  where the file lands and that nothing returns from a tracker. Observed by AC10.

## 3. Non-goals (OUT)

- Any named service, or a connector that pushes the spool to one. The owner was never shown a service, and
  `mirror-out` names none (scout C disagreement 9).
- Two-way sync, or an ask raised from an issue. Research rejected it: it breaks the one-door `record` rule,
  and an issue is not consent (`research-integrations-a.md:149`, `research-integrations-b.md:239`).
- A journal reader. The journal holds `driver`, `gates` and `pushes` only, so asks are not in it (§8 F1).
- The tracker adapter kind beyond this one row, and `kits.host`'s host rows, which DEPL-dShippedRelease-3
  registers and this unit only names.

### Edges

- **consumes-from** `DEPL-dShippedRelease-15` — `check_adapter_header`, which grades S4's row; without it the row has no header check
- **consumes-from** external — `tools/runtime/points.toml`, `point.cadence-items` and `[[selects]]`, each specced and unbuilt in dWellOiledMachine and dDeclaredLoop; without them S4, S5 and S6 have no home, while `tracker_mirror.py sync` still runs by hand
- **hands-off** `DEPL-dShippedRelease-78` — the cadence row and its adapter, which the minors batch repairs (review ids 13, 53, 55, 66)

## 4. Design

### The flow

```text
kits.host tick → tracker_mirror.py sync → read_policy("integrations.tracker")
  none        → one line, nothing written
  mirror-out  → gen_build_index.py --asks --all --json → sorted rows → the spool
```

The spool holds `{"sha": "<HEAD>", "asks": [ ... ]}`. It sits under the git common dir because a mirror is
machine state, so it dirties no tree, reaches no commit and passes no publishing boundary. It carries no
timestamp, which is what makes a re-run byte-identical. A write goes through a temporary file and a rename.

### Why an abstract row

The clause asks for "the adapter", and the records name no service. An HTTP call to a declared URL would add
an outbound surface that M3's veto 3 prices and that no reader of this repository could name a target for.
So `target` is a closed field whose one value is a local file. A service adapter, when one is chosen, is a new
`target` value or a row reading the spool, and neither changes this module.

### The missing-expansion case

`check_expansion_value` asks whether a core row of `tools/playbook/layers.toml` declares the point
(TOOL-dDeclaredLoop-2 S8), and this point must be core-declared because EX-1 reds an expansion using another
expansion's point, while integrations declares none. So `mirror-out` on a tree without the integrations kit
is not refused by that row today: the core declares the word whether or not a kit fills it. §8 F3 carries the
ask. Until it lands, the value does nothing on such a tree and `check_adapter_header` is never reached.

### The cadence

A daily row keeps the file near the backlog without any hook on a landing. At the default `kits.host`
`session-start`, the host row DEPL-dShippedRelease-3 registers runs it. No criterion rests on that row's host:
AC8 reads the row, and every other criterion calls the verb.

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `tracker_mirror.py`, `sync`, `probe` | module and verbs | `tools/integrations/` |
| `derive_ask_mirror`, `read_policy`, `write_replace` | functions | `tracker_mirror.py` |
| `point.memory.ask-mirror` | point | `tools/runtime/points.toml`, `tools/playbook/layers.toml` |
| `mirror-out` | adapter row | `tools/runtime/points.toml` |
| `tracker-mirror` | cadence row | `tools/runtime/points.toml` |
| `target = "spool"` | adapter field | the row |
| `tracker-mirror/asks.json` | spool file | the git common dir |

`lexicon.py --suggest derive_ask_mirror --as py.function` and `--suggest read_policy --as py.function` printed
OK on 2026-10-30, and `write_replace` is `held_halves.py`'s existing spelling.

### Migration

Additive. The default `none` writes nothing, so no tree moves.

### Rollout

Dark behind the default. `mirror-out` is set by the owner in `.governance/policy.toml`.

### Files touched (estimate)

- `tools/integrations/tracker_mirror.py`
- `tools/integrations/adapters.py`
- `tools/integrations/kit.toml`
- `tools/runtime/points.toml`
- `tools/loop/loop.toml`
- `tools/playbook/layers.toml`
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt`
- `help/tracker-mirror.md`
- `help/README.md`

### Alternatives rejected

- **A journal reader, as `layer-expansions.md:321` says.** The test: `read_journal`'s `PRODUCER_FILES`
  (`tools/runlog/runlog_lib.py:40`) lists three producers and asks are none of them, and
  TOOL-dWellOiledMachine-16 S7 limits a reader to it (§8 F1).
- **Calling `parse_file` from this kit.** The test: `parse_file` returns rows with no status, and the status
  fold is `derive_statuses`. `--asks --json` already publishes the fold, so a second caller of the fold would
  add a kit import for nothing.
- **A tracked export file.** The test: a landing would then carry a mirror's bytes, a generated file with no
  reader in the tree, and the first status change would dirty every node.

## 5. Production-readiness checklist

- security: no network, no secret, no write under the memory root. Ask summaries reach a file under the git
  common dir, readable by that node's user and never pushed. A connector that sends the file on is outside
  this unit and answers for its own grant.
- perf / scale: one `--asks --all --json` per day, seconds on a tree of about a thousand asks, PINNED at 1015 on
  2026-10-30, and one file write.
- error / empty / loading states: a refused index run, a zero read and an unwritable target each exit 1 by name,
  leaving the previous spool in place through the rename. A refused policy read exits 2.
- observability: the one line per run, with the count and the SHA, and `probe`, which prints the target and
  whether the last spool's SHA is HEAD.
- risks: the spool is stale between runs, and a reader outside gov may take it as current, so the file carries
  its SHA. On a tree without the kit the value is silently inert (§8 F3).
- testing: the probes of §6 and the module's in-file arms (§7).
- migration: §4 "### Migration".
- user docs: `help/tracker-mirror.md`, S8.

## 6. Acceptance criteria

- **AC1** — When `python tracker_mirror.py sync` runs in a fixture whose landed `.governance/policy.toml` sets
  `tracker = "none"` under `[integrations]`, it prints `nothing mirrored`, exits 0, and no spool exists. With the
  key unset it does the same.
  Red when: the default writes anything.
  fixture: a scratch repository under `%TEMP%` with one `BACKLOG.md`.
- **AC2** — When `python tracker_mirror.py sync` runs with `tracker = "mirror-out"` planted, the spool holds one
  row per ask of the fixture's backlog, each with `id`, `status` and `summary`, and its `sha` is HEAD.
  Red when: a row is dropped, or a status differs from `gen_build_index.py --asks --json`'s.
- **AC3** — When `python tracker_mirror.py sync` runs twice on one tree, the spool's bytes are equal, and after a
  disposition row closes one ask, only that row and `sha` change.
  Red when: a timestamp or an unstable order makes every run a change.
- **AC4** — When `python tracker_mirror.py sync` runs with a stub `gen_build_index.py` exiting 1, and again with
  every ask row removed from a tree still holding the `BACKLOG.md`, each exits 1 naming the dead probe, and a
  previous spool keeps its bytes.
  Red when: a failed read writes an empty mirror, which an outside reader takes as no open asks.
- **AC5** — When `python adapters.py --check` runs on the tree, the `mirror-out` row passes `check_adapter_header`.
  With its `target` planted as `http://x`, `python tracker_mirror.py probe` exits 2 naming the field.
  Red when: an unknown target is written to, or read as a place to send.
- **AC6** — When `grep -cx 'integrations.tracker' tools/policy/unsummarised-keys.txt` runs it prints `0`,
  `python tools/policy/policy.py lists --check` exits 0, and a grep of `tracker_mirror.py` for
  `read_policy("integrations.tracker")` prints the literal call.
  Red when: the key has no literal reader, which the policy kit's reader-coverage arm reds once this build is
  terminal.
- **AC7** — When `python -c` calls `check_expansion_value("integrations.tracker", "mirror-out")` on the tree, it
  answers with no refusal, and with the point's `declares` word removed from a scratch copy it exits 2 naming
  the key, the value and the point.
  Red when: the `[[selects]]` row is absent or names another point.
  fixture: TOOL-dDeclaredLoop-2 built.
- **AC8** — When `python cadence.py --check` runs on the tree, it counts the `tracker-mirror` row and refuses nothing.
  Red when: the row's `host-key` has no catalogue row, or its `run` is empty.
  fixture: TOOL-dWellOiledMachine-59 built.
- **AC9** — When `grep -cE 'urllib|http\.|socket|requests' tracker_mirror.py` runs, it prints `0`, and after a
  `sync` under `mirror-out`, `git status --porcelain` prints nothing.
  Red when: the module grows a network path, or the mirror touches the tree.
- **AC10** — When `grep -n 'tracker-mirror.md' help/README.md` runs, it prints the page's row.
  Red when: the value has no page.

## 7. Gates

`policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `govkit acceptance matrix` · `playbook render selftest`

New arm: tools/integrations/tracker_mirror.py · covers AC1 AC2 AC3 AC4 AC5 · a fixture backlog under each value of the key, a failing index run, an emptied backlog and a planted target · none

What these do not check: that any outside reader consumes the spool, that a summary is free of a secret, or that a
tree without the integrations kit refuses `mirror-out` (§8 F3).

## 8. Open questions

- **F1 — What does the mirror read, given `layer-expansions.md:321` says it registers as a journal reader?** Options:
  (a) a journal reader, which cannot see an ask; (b) a reader of the ask record, as research-integrations-a's option (b)
  put it, through the index's fold. The clause says only "the adapter". RESOLVED (agent, 2026-10-30, delegated): (b),
  rung 1. The design line is not the clause, and the journal holds no asks. widens: none · relaxes: none
- **F2 — What is the mirror's target, with no service named (scout C F8)?** Options: (a) a local spool; (b) an HTTPS POST to
  a declared URL; (c) a `command` argv. (b) adds an outbound surface with no named receiver (veto 3), and (c) runs a
  configured program under a cadence. The owner's pick was "argue away, mirror later". RESOLVED (agent, 2026-10-30,
  delegated): (a), rung 3, an abstract row with a declared target and no external dependency.
  widens: none · relaxes: none
- **F3 — How does `mirror-out` refuse on a tree without the integrations kit?** Options: (a) a core-declared point and the
  `[[selects]]` row as specified, which cannot red there; (b) the point declared by an expansion row, which EX-1 reds; (c)
  an ask of dDeclaredLoop. RESOLVED (agent, 2026-10-30, delegated): (a) with (c), rung 3: the row stands and the gap is
  stated. The ask, for dDeclaredLoop: accept `check_expansion_value` also refuses a `[[selects]]` value whose point has no
  adapter row filled by an installed kit, seen red on `integrations.tracker = "mirror-out"` on a fixture tree with no
  integrations kit. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft.
- rev-2 · 2026-10-30 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (units 78); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is the published fold of `tools/memory-tree/backlog.py`, read as `gen_build_index.py --asks --all
--json`, whose rows carry `id`, `home`, `status`, `sev`, `filed`, `summary` and `pointer` (run at `f4597719` on
2026-10-30: 1015 asks in 150 files). Scout C named `parse_file` at `tools/memory-tree/backlog.py:555`, which reads true, and
this spec takes one step up from it, for the status fold. `reuse_lookup.py "export asks one way to an outside tracker"`
ranked `export`, `tracked` and `ask_filed_in`, each a name-stem neighbour, and it does not reach the `--asks` verb, which
`gen_build_index.py:3235` holds. The recall probe found scout C's row and the clause, and research-integrations-a:149
and research-integrations-b:239 fix the shape. Candidates rejected and their tests are under §4 "### Alternatives
rejected". `write_replace` is `held_halves.py`'s atomic write, and each kit carries its own, no sibling import.

Recall terms used: `python tools/memory-recall/query.py "what is the one-way tracker mirror for asks" --terms "integrations.tracker mirror-out ask backlog journal reader adapter tracker issues one-way outbound"`
