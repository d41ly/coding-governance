# TOOL-dLinkedLibrary-48 — the marker registry in an adopter: a reader resolved through the install, and "appears nowhere" graded only on this repository's own rows

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 4 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 |
| [2026-10-26-build-TOOL-dLinkedLibrary-48-deviation-481.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-48-deviation-481.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
finding **id 59 at HIGH**, report item **R12**. No other id shares the item.

`TOOL-dLinkedLibrary-12`'s `tools/memory-tree/marker-words.toml` holds gov's 21 words with readers at gov
paths, and ships as `engine` through the memory-tree kit's `include = "**"` rule
(`tools/memory-tree/kit.toml:20-22`). Its S1 refuses a row whose reader is untracked, and its S3 refuses a
registered word no file carries. The spec never addresses adopters. In an adopter without the unattended
kit, or where gov-only suites such as `tools/lib/resolve-python.test.sh` are withheld, the `markers` arm,
and so the unguarded `annotations` leg, is red from install on.

This unit states the adopter envelope: a row's reader is resolved through the install, an absent reader
reads `not installed`, and the "appears nowhere" direction grades only rows this repository's own builds
own. It repairs `TOOL-dLinkedLibrary-12` and builds one step after it (order 4).

## 2. Scope (IN)

- **S1** — The reader, resolved. A row's `reader` keeps gov's spelling, `tools/<home>/<file>` or
  `tools/<file>`. `read_marker_words` (`tools/memory-tree/annotations.py`) resolves it in this install
  with `resolve_kit_dir(<home>, <file>, here)` (`tools/memory-tree/backlog.py:1758`), or, for a file at
  the tool root, `<here>/../<file>`; a reader that resolves to nothing reads `not installed`, and the
  row stays registered. A `reader` that is neither `none` nor that shape is refused, naming the row.
  Observed by AC1 and AC2.
- **S2** — "Appears nowhere", owned rows only. `check_marker_words` reds a registered word no file
  carries only when the row's `owner` names a unit of a build whose folder this repository's memory
  root holds; every other row prints one line, `annotations: markers: <n> row(s) owned outside this
  repository — appears-nowhere not graded`. Observed by AC2 and AC3.
- **S3** — "Unregistered" stays live everywhere. A `gov:` word no row declares reds in any install,
  since every word a shipped kit file carries has a row. Observed by AC4.
- **S4** — The announcements. Each `not installed` reader prints `annotations: markers: not installed —
  <word>: <reader>` once per run, never as a green count. Observed by AC1.
- **S5** — The plant. `annotations.py --fixture --plant adopter-memory-tree-only` builds a scratch
  adopter holding only the memory-tree kit's files, a `.governance/install.json` naming them and one
  tracked file carrying `gov:kit`; `check --only markers` exits 0 printing S2's and S4's lines.
  Observed by AC2.

## 3. Non-goals (OUT)

- An adopter's own `gov:` words: the prefix is gov's, and S3 refuses one as it refuses any unregistered
  word.
- The registry's shipping role: it stays `engine`, gov's vocabulary, overwritten on update.
- The `legacy`, `note`, `feature` and `end` rows: `TOOL-dLinkedLibrary-40`'s and
  `TOOL-dLinkedLibrary-4`'s, read by S1 and S2 as every other row.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-12` — `read_marker_words`, `check_marker_words` and `marker-words.toml`, whose reader resolution S1 and owned-row rule S2 change (id 59)
- **hands-off** `TOOL-dLinkedLibrary-62` — S1's `not installed` reading and S2's owned-row split, which unit 62 joins so an owned row's missing reader stays red (id 26 of the spec audit of units 37 to 53)
- **hands-off** `TOOL-dLinkedLibrary-64` — `adopter-memory-tree-only` and the README sentence, which unit 64 re-hosts and completes (ids 5, 21 of the spec audit of units 37 to 53)

## 4. Design

### Evidence

- `tools/memory-tree/kit.toml:20-22` ships `include = "**"` as `engine`, and the kit declares `requires =
  []` (:7): an adopter may hold memory-tree alone.
- `TOOL-dLinkedLibrary-12` §4's census puts readers in the unattended kit, the hooks kit,
  `tools/lib/resolve-python.test.sh` (gov-internal), `tools/memory-tree/check-memory-hygiene.test.sh` and
  `tools/workflows/unattended-build.test.sh`, and its S1 and S3 refuse both an untracked reader and a word
  no file carries.
- `resolve_kit_dir` (`tools/memory-tree/backlog.py:1758`) reads the install receipt, then probes
  `<here>/<home>/<anchor>` and `<here>/../<home>/<anchor>`, and raises `LookupError` naming the places
  looked, never a guessed prefix.

### The verdicts after S1 and S2

| Row | Reader resolves | Owner's build in this tree | Word carried | Verdict |
|---|---|---|---|---|
| any | yes | yes | no | red: registered and appears nowhere |
| any | yes | no | no | counted under "owned outside" |
| any | no | any | any | `not installed`, announced |
| any | any | any | yes | registered |
| none | — | — | a word with no row | red: unregistered |

### Files touched (estimate)

- `tools/memory-tree/annotations.py`: S1 to S5

### Alternatives rejected

- **A project-owned registry shipped empty.** Every `gov:kit` marker a shipped kit file carries would
  then be unregistered in every adopter, unless the install seeded it per kit, a second registry beside
  gov's.
- **A `kit` column on each row.** The reader's path already names its home; a second column can
  disagree with it.

## 5. Production-readiness checklist

- security — read-only; the resolver reads the receipt and probes, and follows no path outside the tree.
- perf / scale — one resolver call per row, 21 rows and the rows later units add.
- error / empty / loading states — S4 announces each absent reader; an unreadable receipt falls back to
  the probe, as `resolve_kit_dir` does.
- observability — one line per absent reader and one count of unowned rows.
- risks — a stale row owned outside the repository is never graded "appears nowhere" in an adopter; gov
  grades it in its own tree.
- testing — the plants of §6.
- migration — none.
- user docs — none under `help/`: `tools/memory-tree/README.md`'s registry paragraph gains the two
  sentences.

## 6. Acceptance criteria

- **AC1** — When `python annotations.py check --only markers` runs in this repository at the pass tip, it
  exits 0 and prints no `not installed` line.
  Red when: a reader gov tracks reads as absent.
- **AC2** — When `python annotations.py --fixture --plant adopter-memory-tree-only` runs, it exits 0,
  prints `not installed` for the unattended kit's readers and the owned-outside count line.
  Red when: the memory-tree-only adopter reds on an absent reader or an unowned row.
- **AC3** — When a row `word = "never-written"` owned by a unit of a build this tree holds is planted in a
  scratch clone, the check exits 1 naming it; owned by `TOOL-dElsewhere-1`, it is counted and not red.
  Red when: an owned stale row passes, or an unowned one reds.
- **AC4** — When the adopter plant gains a tracked file carrying `gov:planted-word`, composed at runtime
  so no tracked file spells it, the check exits 1 naming it.
  Red when: the adopter envelope disarms the unregistered direction.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/annotations.py · covers AC2 AC3 AC4 · the `adopter-memory-tree-only` plant with its stale-row and planted-word variants, the failing case staged by `read_marker_words` refusing an unresolved reader · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 12 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — What is the adopter envelope?** Options: (a) readers resolved through the install and
  "appears nowhere" graded on owned rows; (b) a project-owned registry seeded per installed kit; (c) a
  `kit` column per row. (b) needs a seeding step in every installer, a write surface the clause does not
  price (veto 3); (c) spells a fact the reader's path already holds. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the most feature-rich survivor, tie-broken by reuse of `resolve_kit_dir`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, id 59
  (HIGH, item R12).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-62, TOOL-dLinkedLibrary-64, promoted from the spec audit of units 37 to 53; nothing else moved.

## 10. Reuse audit

The seam extended is `resolve_kit_dir` (`tools/memory-tree/backlog.py:1758`), the one reader of where an
installed kit's file sits, inlined in memory-tree; S1 calls it rather than probing paths of its own.
`python tools/codebase-map/reuse_lookup.py "find which kit directory an installed file lives in"` ranked
`resolve_kit_dir`, `kit_rel` and `kit_dir`, and the first is that seam.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`
