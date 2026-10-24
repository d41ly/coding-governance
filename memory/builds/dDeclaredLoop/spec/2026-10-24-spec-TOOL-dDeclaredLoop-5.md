# TOOL-dDeclaredLoop-5 — the witness-class rule: every witness classed, the actor class refused

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 5 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0090@e3f362f0 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-26 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

Every witness the loop declares names its class, `history`, `hook-record` or `remote-verdict`; the
`actor` class, a fact the acting agent typed, is refused, and today's actor witnesses sit on a
shrink-only list, each row naming the build that removes it (walkthrough.md:45-47). Guards today read
agent-written state across stages (`gap-spine-02`), and the driver defaults an item with no declared
class to `machine` without saying so (`checker_of`, `tools/unattended/unattended.sh:1275`).

## 2. Scope (IN)

- **S1** — The classes, `[witnesses]` in `tools/loop/loop.toml`: `classes = ["history", "hook-record",
  "remote-verdict"]` and `refused = ["actor"]`, read by `read_witness_classes()` in
  `tools/loop/loop_lib.py` (shared interface I5). Observed by AC1.
- **S2** — Each witness the definition declares carries `witness = { class = "<class>", by = "<what>" }`;
  at this unit that is every `[[step]]` row of TOOL-dDeclaredLoop-1, each step's exit witnessed by its
  transition record, class `history`. `check_witness_classes()` refuses a witness with no class, a class
  in neither list, and an `actor` witness whose site is not on the list. Observed by AC1 and AC2.
- **S3** — The shrink-only list `tools/loop/actor-witnesses.txt`, one row per actor witness,
  `<site>\t<witness>\t<build>`, `<build>` the chain build that replaces it with a computed
  witness, whose `memory/builds/<build>/README.md` exists. A row added relative to the compare base, a
  row whose site holds no such actor witness, and a row naming no build folder are each refused.
  Observed by AC3 and AC5.
- **S4** — Today's classes mapped, `[[witness-alias]]` rows in `tools/loop/loop.toml`: `DOD_CORE`'s
  `machine` to `history` and `agent` to `actor` (`tools/unattended/unattended.sh:868`); the list seeded
  with the two `agent` items, `keepalive-reaped` and `parked-decisions-surfaced` (§8 F3). Observed by
  AC5.
- **S5** — No silent default: `checker_of` returns 1 and prints nothing for an item with no
  declared class, and `tools/unattended/check-unattended.sh` refuses a `DOD_EXTRA` entry with no
  `:<class>` or a class outside the alias words, and an `agent` item not on the list; the unattended
  descriptor gains `requires` `loop`. Observed by AC4.

## 3. Non-goals (OUT)

- Classing each item's witness: the item rows are TOOL-dDeclaredLoop-12's and their declaration check
  TOOL-dDeclaredLoop-9's, which read S1's classes.
- Computing a witness the actor used to type: TOOL-dDeclaredLoop-17's (the attest door, the
  executor's stand-ins).
- The floor invariant `floor.no-actor-witness`: TOOL-dDeclaredLoop-2's, which reads the `actor` class.
- Retiring `machine` and `agent` from `DOD_CORE`'s grammar: the alias maps them, and the driver's
  vocabulary stays until the build that removes each actor row.
- Removing either seeded actor witness: the list names the builds that do.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-1` — `loop_lib.py` and `loop.toml`, where the classes, the aliases and the check are added beside the steps
- **hands-off** `TOOL-dDeclaredLoop-9` — `read_witness_classes` and the refused class `actor`, against which each item's witness is declared
- **hands-off** `TOOL-dDeclaredLoop-2` — `actor`, the refused class the floor's `floor.no-actor-witness` reads
- **hands-off** `TOOL-dDeclaredLoop-17` — `actor`, the refused class a computed witness replaces
- **hands-off** `TOOL-dDeclaredLoop-41` — the actor-witness list graded by tree, and adopter agent items admitted, which that unit specifies (the round-1 spec audit's id 48)
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, id 16, a scope item of that unit

## 4. Design

### Data model

```toml
# tools/loop/loop.toml
[witnesses]
classes = ["history", "hook-record", "remote-verdict"]
refused = ["actor"]

[[witness-alias]]          # today's DoD checker words (tools/unattended/unattended.sh:868)
word = "machine"
means = "history"

[[witness-alias]]
word = "agent"
means = "actor"

[[step]]
tag = "step.plan"
witness = { class = "history", by = "the transition record into the next step" }
```

```
# tools/loop/actor-witnesses.txt — shrink-only: rows only leave
DOD_CORE	keepalive-reaped	dWellOiledMachine
DOD_CORE	parked-decisions-surfaced	dShippedRelease
```

| Class | What witnesses it (orientation.md `[trust]`, :184-201) |
|---|---|
| `history` | a commit, its trailers, a tracked file at a SHA, a ref |
| `hook-record` | a record a hook writes, which the acting agent cannot type |
| `remote-verdict` | a verdict keyed by tree fingerprint from the remote's runner |
| `actor` (refused) | a status word, a typed return, an attestation by the acting agent |

### The checks

`check_witness_classes(definition, actor_rows)` walks every table of the definition that carries a
`witness` and yields one refusal per witness with no `class`, a class in neither list, or class
`actor` at a site the list lacks. `check_actor_list(rows, base_rows, sites)` refuses a row absent from
`base_rows`, the list as it stands at the compare base read by `resolve_compare_base` (PLAY-dOrderedCharter-19
S9's `tools/lib/coverage_join.py`, the base the map's own shrink-only assert reads); a row whose site no
longer holds that actor witness; and a row whose build has no `memory/builds/<build>/README.md`. A list
absent at the base is no comparison and is printed so, never read as empty.

The `DOD_CORE` site is graded on the unattended side, which owns the declaration: the leg
`tools/unattended/check-unattended.sh` already reads `DOD_CORE` and `DOD_EXTRA` (:688). Its new arm asks
`loop_lib.py alias <word>` for each entry's class word, refuses an entry with no word or an unknown one,
and refuses an entry mapping to `actor` whose item is not a `DOD_CORE` or `DOD_EXTRA` row of the list.

### The silent default

```bash
# tools/unattended/unattended.sh:1275, today
checker_of()  { …; printf 'machine'; }
# after: an item whose entry declares no class has no checker
checker_of()  { local p; for p in $(dod); do case "$p" in "$1:"*) printf '%s' "${p#*:}"; return 0;; esac; done; return 1; }
```

Every caller already walks `dod()` or checks membership first (:6740, :10898, :11011, :12581), so only
an entry with no `:<class>` reaches the new return, and S5's leg arm refuses that entry before a run
reads it.

### Inventory

Minted: `[witnesses]` with keys `classes` and `refused`; `[[witness-alias]]` with keys `word` and
`means`; the `witness` inline table on a `[[step]]` row with keys `class` and `by`;
`read_witness_classes`, `check_witness_classes` and `check_actor_list` in `tools/loop/loop_lib.py` and
its verb `alias`; `tools/loop/actor-witnesses.txt`; the plants `witness-no-class`, `witness-bad-class`,
`witness-actor-unlisted`, `witness-actor-listed`, `actor-list-grown`, `actor-list-stale` and
`actor-list-no-build`. Naming cells: each function is asked of `python tools/lexicon/lexicon.py
--suggest <name> --as py.function` at the pass.

### Migration

An adopter's `DOD_EXTRA` entry with no class reads `machine` today and is refused after; the refusal
names the entry and the two words, and the upgrade is to append `:machine` or `:agent`. Gov's own conf
declares `DOD_EXTRA` empty (`.unattended.conf:290`, read 2026-10-24).

### Rollout

Live at landing.

### Files touched (estimate)

- `tools/loop/loop.toml`
- `tools/loop/loop_lib.py`
- `tools/loop/actor-witnesses.txt`
- `tools/loop/README.md`
- `tools/unattended/unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/kit.toml`

### Alternatives rejected

- **`DOD_CORE`'s checker words replaced by the three classes**: a vocabulary change across the driver,
  its leg, its protocol and every adopter's `DOD_EXTRA`, which the clause does not ask; the alias maps.
- **A per-item class row in the loop definition for each DoD item**: a second list of the DoD items
  beside `DOD_CORE`.

## 5. Production-readiness checklist

- security — no write path; the rule refuses the class an agent could forge, which is its purpose.
- perf / scale — one TOML read and one list read; the leg arm adds one interpreter start.
- error / empty / loading states — a witness with no class is a refusal naming its table and row; a
  list with no base is printed as no comparison.
- observability — `loop_lib.py --check` prints each witness with its class and each listed actor
  witness with its removing build.
- risks — an adopter's classless `DOD_EXTRA` entry is refused at its next update (§4 Migration).
- testing — the plants of §4 by a pass through the fixture; the unattended kit's suites are waived for
  this landing (README rule 8), so the driver side is observed by a probe (AC4).
- migration — §4 Migration.
- user docs — `help/loop.md` gains the classes and the list.

## 6. Acceptance criteria

- **AC1** — When `python loop_lib.py --check` runs in the loop kit, it prints the three classes, the
  refused `actor`, and each of the five step witnesses with class `history`, and exits 0.
  Red when: a `[[step]]` row carries no `witness`, so the check refuses it by name.
- **AC2** — When `python loop_lib.py --fixture --plant witness-no-class` runs, it exits 1 naming the
  step whose witness has no class; `--plant witness-bad-class` (class `agent-said`) exits 1 naming the
  class; `--plant witness-actor-unlisted` exits 1 naming the site; `--plant witness-actor-listed` exits
  0 printing the site with its removing build.
  Red when: an absent class is defaulted, the shape `checker_of`'s `machine` has today.
- **AC3** — When `python loop_lib.py --fixture --plant actor-list-grown` runs, its list carrying one
  row its fixture base lacks, it exits 1 naming the added row; `--plant actor-list-stale` exits 1 naming
  a row whose site declares no actor witness; `--plant actor-list-no-build` exits 1 naming
  `dNoSuchBuild`.
  Red when: the list is read without its base, so a grown list reads green.
- **AC4** — When a scratch probe defines `dod` and `checker_of` from `tools/unattended/unattended.sh`
  with `DOD_CORE="a:machine"` and `DOD_EXTRA="b"`, `checker_of b` prints nothing and returns 1, and
  `checker_of a` prints `machine`; and `python loop_lib.py alias agent` prints `actor` (README rule 8:
  the kit's suite is waived, so the probe observes the driver).
  Red when: `checker_of b` prints `machine`, as it does at base.
- **AC5** — When `cut -f2,3 actor-witnesses.txt` runs in the loop kit, it prints
  `keepalive-reaped` with `dWellOiledMachine` and `parked-decisions-surfaced` with `dShippedRelease`,
  and nothing else.
  Red when: an `agent` item of `DOD_CORE` is missing from the list, so the rule refuses the driver's
  own declaration.

## 7. Gates

The pass adds no leg: the loop checks run under TOOL-dDeclaredLoop-1's `loop definition` leg, and the
`DOD_CORE` arm under the unattended kit's gate.

`unattended kit gate` · `unattended skill wiring` · `pass-order history` · `brief-recorded` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_lib.py · covers AC1 AC2 AC3 · the `loop definition` leg's fixture plants, the failing case staged by the `witness-actor-unlisted` plant · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a legal
  status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:27`. Observation, 2026-10-24:
  `DRAFT` is not in the tuple. Liveness: the tuple would carry it if the vocabulary admitted it.
  RESOLVED (agent, 2026-10-24, delegated): `OPEN`, rung 2. widens: none · relaxes: none
- **F2 — What class does `DOD_CORE`'s `machine` map to?** Options: (a) `history`, every machine item
  being derived by the driver from the repository and its remote-tracking refs; (b) a class per item,
  a second list of the DoD items; (c) no mapping, `machine` left outside the rule. (b) types the DoD set
  twice and (c) leaves eleven witnesses unclassed. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3,
  orientation.md `[trust]` classes a ref as trusted for that commit. widens: none · relaxes: none
- **F3 — Which build removes each seeded actor witness?** No v2 line names one. Options for
  `keepalive-reaped`: dWellOiledMachine, whose supervisor beat retires the cron keepalive
  (research-tool-fates.md:111). For `parked-decisions-surfaced`: dShippedRelease, the Deploy stage
  build whose close the item belongs to, or dBoundRoles, whose `run.on-owner-question` resolves owner
  questions. The close's wrap-up is Deploy's, and walkthrough.md:46 assigns each row to "the stage
  build that removes it". RESOLVED (agent, 2026-10-24, delegated): `dWellOiledMachine` and
  `dShippedRelease`, rung 3. widens: none · relaxes: none
- **F4 — Does the unattended kit read the loop kit?** Options: (a) `requires` `loop`, the leg arm
  calling `loop_lib.py alias`; (b) the alias words typed in the leg. (b) is a second spelling of the
  map. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3; both kits are core (PLAY-dOrderedCharter-16
  §4) and the loop kit requires neither, so no cycle. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 5, the brief's shared interface I5,
  scout A's row for cl-0090, and `DOD_CORE`, `checker_of` and `verb_attest` read at base `ed497191`.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-41, a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md); no scope moved.

## 10. Reuse audit

The seams extended are `DOD_CORE`'s classed-witness vocabulary (`tools/unattended/unattended.sh:868`)
and the leg that reads it (`tools/unattended/check-unattended.sh:688`); the shrink-only base is
PLAY-dOrderedCharter-19 S9's `resolve_compare_base`, lifted from `tools/codebase-map/map_lib.py:1502`.
`python tools/codebase-map/reuse_lookup.py "classify each witness and refuse an actor-typed witness on
a shrink-only list"` ranked `classify` (`tools/govkit/census.py`), `CensusRefused` and `read_id_list`
by name stem and named no witness seam. Scout A found no shared shrink-only factory, and the map's
`derive_baseline_additions` (`map_lib.py:1530`) is bound to `baseline.toml`'s path, so only the base
resolver is reused. The recall probe returned scout A's and scout B's rows, which agree with source,
`checker_of` defaulting to `machine` included.

Recall terms used: `python tools/memory-recall/query.py "which witnesses are typed by the acting agent and how are they classed" --terms "witness class history hook-record remote-verdict actor DOD_CORE checker_of agent attested shrink-only"`
