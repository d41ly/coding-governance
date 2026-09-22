**Serves:** research TOOL-dFramedEntrypoint-1

*Research lens for the `dFramedEntrypoint` design pass — what the generator already computes, and every consumer of what it renders. Produced 2026-08-24, node d, against base 9ddcc5c9. Findings in this record were subsequently adversarially verified; where the verification corrected a claim, the verification record wins.*

# Lens: the derivation surface — what already computes in `gen_build_index.py`

All paths repo-root-relative to `C:/projects/coding-governance/.claude/worktrees/build-readme-governance-18d6ea`.
Every count below names the command that produced it. Line numbers are from this worktree's HEAD (`9ddcc5c9`).

---

## 1. Inventory — what the generator already parses, and where each field goes

### The parse sites

| Site | File:line | What it extracts |
|---|---|---|
| `HDR_RE` | `tools/memory-tree/gen_build_index.py:104-108` | `token` `rev` `date` `node` `tier` `base` from a spec's `**Status:**` line |
| `H1_RE` | `tools/memory-tree/gen_build_index.py:109` | `id` `title` from the spec's `# <id> — <title>` heading |
| `ORDER_RE` | `tools/memory-tree/gen_build_index.py:110` | `· order <n>` anywhere on the same header line |
| `REQUIRED_KEYS` | `tools/memory-tree/gen_build_index.py:112` | `slug node opened streams roster ids` from build front matter |
| `parse_spec` | `tools/memory-tree/gen_build_index.py:253-287` | assembles the unit record |
| `parse_front_matter` | `tools/memory-tree/gen_build_index.py:213-250` | the front-matter dict; arbitrary extra keys admitted |
| `read_bindings` | `tools/memory-tree/gen_build_index.py:353-440` | `path -> {state, kind, ids, commissions, reason, bad}` from every record's `**Serves:**` / `**Commissions:**` head line |
| `collect` | `tools/memory-tree/gen_build_index.py:541-618` | per-build: `fm roster kinds docs parents units status` |
| `derive_status` | `tools/memory-tree/gen_build_index.py:477-496` | build status by `PRECEDENCE` over unit statuses |

### The field table — extracted vs. reaching the units table

`render_region` emits the units table at `gen_build_index.py:641-646`. Its row is:

```
| [{id} — {title}]({rel}) | {status} | rev-{rev} | {date} |
```

| Field | Captured by | In `parse_spec`'s dict? | Reaches the units table? | Cost to add |
|---|---|---|---|---|
| `id` | `H1_RE` | yes (`"id"`) | yes, as the link label | — |
| `title` | `H1_RE` | yes (`"title"`) | yes, as the link label | — |
| spec path | `parse_spec` | yes (`"path"`) | yes, as the link target | — |
| `status` | `HDR_RE` group `token` | yes (`"status"`) | yes | — |
| `rev` | `HDR_RE` | yes (`"rev"`) | yes | — |
| `date` | `HDR_RE` | yes (`"date"`) | yes, as *Last change* | — |
| **`tier`** | **`HDR_RE` group `tier`, line 106** | **NO — captured and DISCARDED** | **no** | **one dict key + one cell** |
| **`order`** | **`ORDER_RE`, line 110** | **yes (`"order"`), line 284** | **NO — it goes to `render_order` only** | **one cell** |
| `node` | `HDR_RE` group `node` | no (discarded) | no | one dict key + one cell |
| `base` | `HDR_RE` group `base` | no (discarded) | no | one dict key + one cell |
| `streams` | not in `HDR_RE` (it ends at `base`) | no | no | a second regex |

**The two questions settled, from source:**

- **Is `Tier-<n>` already captured? YES, and then thrown away.** `HDR_RE` at
  `gen_build_index.py:106` carries `· Tier-(?P<tier>[12])` as a named group. `parse_spec` at
  `gen_build_index.py:277-286` builds its return dict from `hdr.group(...)` for `token`, `rev` and
  `date` — and never for `tier`, `node` or `base`. The tier is matched on every spec, on every
  render, and dropped on the floor. **Adding it to the units table is a one-key, one-cell change
  with no new parsing.**
- **Is `· order <n>` already captured? YES.** `parse_spec:284` sets
  `"order": (lambda mo: int(mo.group(1)) if mo else None)(ORDER_RE.search(hdr.string))`.
  **Where it goes today:** `render_order` at `gen_build_index.py:700-724`, and nowhere else.
  `render_region` never reads `u["order"]`. So the value already exists on every unit record as an
  `int | None`, one dict lookup away from the units table.

### Two derived sets already computed inside `render_region`

`gen_build_index.py:669-678`:

```python
named   = {i for r in recs for i in r.get("ids", [])}
audited = {i for r in recs if r.get("kind") == "spec-audit" for i in r.get("ids", [])}
own     = [u["id"] for u in build["units"]]
gap     = [i for i in own if i not in named]
agap    = [i for i in own if i not in audited]
```

These are already an **id → records** projection, in aggregate form. See §4.

---

## 2. The `order` verb's real status — 100% unadopted, undocumented, unvalidated

### Adoption: zero

```
$ git grep -lE '·\s*order\s+[0-9]' -- memory/
memory/builds/aRuledFrontispiece/spec/2026-08-16-spec-TOOL-aRuledFrontispiece-2.md
```

One file, and it is the **spec that designed the verb**, quoting `· order 3` and `· order 0x2` inside
its own prose. Not one status header in the corpus carries the verb.

Measured through the generator itself (`plan()` over the real tree):

```
$ python3 <scratchpad>/probe.py
builds: 61   units(with status header): 260
units carrying order: 0
```

**All 61 build READMEs therefore render the empty-case sentence** (`gen_build_index.py:709-710`).
Verified: `grep -l "No spec under this build declares an .order. verb" memory/builds/*/README.md` → 61.

Region adoption is otherwise total:
`grep -l "gen:build-order" memory/builds/*/README.md | wc -l` → **61 of 61**; same for
`gen:build-units`, `gen:build-edges`, `gen:build-docs`. The authored `roster:units` pair sits in
**12 of 61** (`grep -l "roster:units" memory/builds/*/README.md`).

### Documentation: none, and the spec doc actively contradicts it

- `memory/TEMPLATE-SPEC.md:44` gives the header grammar as
  `**Status:** <TOKEN> · rev-<N> · <YYYY-MM-DD> · node <tag> · Tier-<1|2> · base <sha8>[ · streams <v>[+<v>]][ · <pointer tail>]`,
  and `memory/TEMPLATE-SPEC.md:59` says **"The tail holds POINTERS only — a review workflow id,
  `ratified <date>` — never prose."** `order` is not a pointer and is not named.
- `tools/memory-tree/SPEC-TEMPLATE.template.md` (the source `TEMPLATE-SPEC.md` is rendered from)
  never names it: `git grep -n "order" -- tools/memory-tree/SPEC-TEMPLATE.template.md` returns only
  the unrelated "sections in order" at `:7`.
- `memory/guides/BUILD-METHOD.md` never names it: `git grep -n "order" -- memory/guides/BUILD-METHOD.md`
  returns only `:62` ("no sub-spec depends on a unit sequenced after it"), `:79`, `:138`, `:198`.

The unit that *would* have documented it — `TOOL-aRuledFrontispiece-2` S7, which amends
`SPEC-TEMPLATE.template.md` — is **WONTDO**:
`memory/builds/aRuledFrontispiece/spec/2026-08-16-spec-TOOL-aRuledFrontispiece-2.md:3` reads
`**Status:** WONTDO · rev-3 · 2026-08-17 · node a · Tier-2 · base 96141aed · streams tooling · superseded by TOOL-aRuledFrontispiece-1`.
The shipped implementation is `TOOL-aRuledFrontispiece-1` S9 (`…-1.md:68-69`), which absorbed the
renderer and **did not absorb S6 (the refusal) or S7 (the doc amendment)**.

### Validation by hygiene check 12: none needed, and none present

Check 12's header predicate is at `tools/memory-tree/check-memory-hygiene.sh:797` and ends at
`· base [0-9a-f]×8` with **no `$` anchor**. Verified against source. A trailing `· order 3` parses
today and reds nothing. `HDR_RE` is unanchored the same way. **The verb is legal, and no check
anywhere asks anything about it.**

### What happens today for the cases you asked about — read from source, not guessed

`render_order`, `gen_build_index.py:700-724`:

| Case | Behaviour today | Where |
|---|---|---|
| Two specs share `order 3` | Both render at step `3`; `Parallel` reads `yes`. By design — the tie IS the parallel group. | `:706-707`, `:715` |
| Non-contiguous orders (1, 2, 7) | Rendered as-is, ascending. Gaps invisible, no refusal, no gap report. | `:711` `for n in sorted(steps)` |
| Some declare, some do not | Declarers render as steps; the rest render as a trailing `Unordered: \`id\`, \`id\`.` line. | `:717-721` |
| `order 0` | **Accepted.** `ORDER_RE` is `(\d+)`, so `0` is a legal step and renders as step `0`. | `:110` |
| `order 0x2` | **Silently renders step 0.** Probed: `ORDER_RE.search("… · order 0x2")` → `'0'`. `\d+` matches `0`; the `(?![0-9])` lookahead sees `x` and passes. | `:110` |
| `order 2x` | **Silently renders step 2.** Probed → `'2'`. | `:110` |

**FINDING — a live defect, not a gap.** `TOOL-aRuledFrontispiece-2` AC5 (`…-2.md:242-243`) specified
exactly these two as *named refusals*, and its §4 (`…-2.md:143-146`) argued the terminator is
"load-bearing and not decoration: without it `· order 2x` matches on its leading `2` and the region
renders a step the author never wrote." **That spec is WONTDO and the shipped `ORDER_RE` carries the
defect it named.** Nobody has hit it because the verb has zero adopters. Any unit that makes `order`
required must fix this first or ship the exact bug that spec predicted.

### The deferral's record — found, and it is not where the dossier points

The dossier (`memory/map/features/build-readme-surface.md:109`) says: *"Requiring it needs a dated
cutoff, which the owner deferred to a follow-up."* The record is the **fork-5 ruling** in the build
README's owner-decision table:

> `memory/builds/aRuledFrontispiece/README.md:36`
> `| 5 | verb rollout | permitted in this build, required in a follow-up commit |`

Restated in the spec that ships it (`…-2.md:14-16`):

> "The verb is PERMITTED and never required, which is fork 5's resolution: this unit ships no
> required-arm and no dated cutoff key."

And its Open questions (`…-2.md:269`): *"none — fork 5 resolved the rollout to permitted-now and
required-later."*

**No unit, backlog row or decision id owns that follow-up.** `git grep -n "dated cutoff" -- memory/`
returns five hits and none is a live row for this. The follow-up fork 5 promised was never opened.
**That is this build's opening.**

---

## 3. Consumers — the complete reader set, with selectors

Enumerated by marker name across the whole tree:

```
$ git grep -n "gen:build-docs"  -- . ':!memory/builds'   → 1 hit  (the generator's own GEN_REGIONS)
$ git grep -n "gen:build-order" -- . ':!memory/builds'   → 1 hit  (same)
$ git grep -n "gen:build-edges" -- . ':!memory/builds'   → 1 hit  (same)
```

**Three of the four generated regions have ZERO external readers.** Only `gen:build-index` and the
nested `gen:build-units` are consumed anywhere.

| # | Consumer | File:line | Reads | Selector | Breaks on +columns? | Breaks on removing `gen:build-docs`? |
|---|---|---|---|---|---|---|
| 1 | `check_authorization` — frozen scope | `tools/unattended/unattended.sh:1251-1268` | `gen:build-units` at BASE and HEAD | `_ids_of` = `grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+' \| sort -u` (`:1544`) over the slice, then `comm -23` | **NO — id SET only, never row bytes** | no |
| 2 | `roster_ids` | `unattended.sh:1487-1493` | AUTHORED `roster:units` | `grep -oE "[A-Z]+-$slug-[0-9]+"` | no | no |
| 3 | `unit_ids_of` | `unattended.sh:1496-1501` | `gen:build-units` | same id grep | no | no |
| 4 | `unit_rows` | `unattended.sh:1538-1542` | `gen:build-units` | **`grep -E '^\| \[.*\]\(spec/'`** — row must start `\| \[` and carry `](spec/` | **only if a column is inserted BEFORE the link cell** | no |
| 5 | `nonterminal_units` | `unattended.sh:1543` | `unit_rows` output | **`grep -vE '\| (CLOSED\|WONTDO) \|'`** — status must stay a whole `\|`-delimited cell | no | no |
| 6 | `--status` next unit | `unattended.sh:2226` | `nonterminal_units \| head -1 \| sed -e 's/^\| \[//' -e 's/\](spec\/.*//'` | first cell is the spec link | **only if inserted before the link cell** — but row ORDER becomes visible behaviour, see below | no |
| 7 | `units-at-landing` freeze | `unattended.sh:1871-1873` | `unit_rows \| sed -e 's/^\| \[//' -e 's/ —.*//'` | first cell, cut at the em dash | same | no |
| 8 | `--preflight` units-region validity | `unattended.sh:2041-2044` | well-formedness only | `region` exit status | no | no |
| 9 | `--preflight` index-pair validity | `unattended.sh:2093-2097` | well-formedness only | `region` exit status | no | no |
| 10 | DoD `run-state-current` | `unattended.sh:2469-2471` | `gen:build-index` well-formedness | `region` exit status | no | no |
| 11 | DoD `build-complete` | `unattended.sh:2693-2727` | region validity, `unit_rows`, `unit_ids_of`, `missing_units`, `nonterminal_units` | as rows 4/5 | as rows 4/5 | no |
| 12 | `baseline_units` | `tools/unattended/lib-unattended.sh:186-207` | `gen:build-units` at a historical blob | `grep -qxF` on the open marker, `region`, then id grep for emptiness | no | no |
| 13 | Leg check 24 (rescope) | `tools/unattended/check-unattended.sh:1490-1509` | region now vs baseline | id grep, plus **`grep -E '\| WONTDO \|'`** to select retired units | no | no |
| 14 | Leg check 2 (review runaway) | `check-unattended.sh:235-237` | region now vs BASE | id grep | no | no |
| 15 | Leg check 21 (pair presence) | `check-unattended.sh:1680-1687` | `grep -cxF` of both units markers | marker lines only | no | no |
| 16 | Leg checks 13/19 (authorization) | `check-unattended.sh:916-990` | build README **front matter** at BASE: `slug`, `authorized-by`, `playbook`, `pieces` | column-0 `key:` awk | no | no |
| 17 | Hygiene check 9 | `tools/memory-tree/check-memory-hygiene.sh:594-596` | delegates to `--check` | byte equality vs a fresh render | **re-render required in the same commit** | same |
| 18 | Hygiene check 21 | `check-memory-hygiene.sh:659-690` | delegates to `--print-bindings` | `A`/`B`/`S`/`N` rows | no | **no** — the bindings parser is independent of any region |
| 19 | Hygiene check 2 (links) | `check-memory-hygiene.sh:223-267` | every `](path)` in every tracked `.md` | link resolution | no | removing links can only shrink the population |
| 20 | Hygiene checks 6 / 7 (caps) | `check-memory-hygiene.sh:432-546` | build README bytes / per-line chars | `BUILD_README_CAP_BYTES=25600`, `BUILD_README_ENTRY_CAP_CHARS=350` (`:45`, `:54`) | see §6 | **removal DRAINS debt — see §4** |
| 21 | `drift_report.build_readme_mechanism_drift` | `tools/drift-audit/drift_report.py:923-1035` | **only the AUTHORED half**: `cut = first line starting with "<!-- gen:"` (`:956`; `_GEN_MARK` at `:870`) | backticked tokens in `lines[:cut]` + `git blame` | no | no — but shrinking authored prose shrinks its population |
| 22 | `drift_report.build_live_backlog_rows` | `drift_report.py:791-828` | backlog shards only, **not build READMEs** | `- ` rows | no | no |
| 23 | Gate leg `build README slot contract` | `tools/gate-legs.json` → `gen_build_index.py --check-format` | slot sequence over all build READMEs | `slot_violations` (`:995-1024`) | **`GEN_REGIONS` order is the contract** | **deleting a `GEN_REGIONS` entry while 61 READMEs still carry the pair = 61 slot violations, see §4** |
| 24 | `tools/memory-tree/marker-contract.test.sh:72` | imports the module, calls `apply_region` positionally | source-level | signature must not change | no |
| 25 | `tools/memory-tree/check-verdict-epoch.sh:69` | `gen_build_index.py` is a DELEGATE | any behaviour-bearing diff | **forces a kit version bump** | same |
| 26 | codebase-map | — | **does not read build READMEs.** `git grep -n "builds/" -- tools/codebase-map/*.py` → no hits | — | no | but `memory/map/features/build-readme-surface.md` claims `gen_build_index.py` and must be refreshed |
| 27 | Test fixtures | `tools/unattended/unattended.test.sh:116`; `check-unattended.test.sh:653,656`; `cross-component.test.sh:68` | hardcoded `\| Unit \| Status \| Rev \| Last change \|` and `\| # \| Unit \|` | literal fixture bytes | **fixtures need updating** | no |

### `check_authorization`'s frozen scope — verified, and new columns ARE safe

Source, `unattended.sh:1264-1268`:

```sh
miss=$(comm -23 <(printf '%s\n' "$ub" | _ids_of) <(printf '%s\n' "$uh" | _ids_of) …)
```

with `_ids_of() { grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+' | sort -u; }` at `:1544`.

The comment at `:1231-1237` states the reason verbatim: *"A row carries the unit's status, rev and
last-change date … A byte-level 'no row changed' test would refuse every run that BUILT anything."*

**Verdict: adding columns to the units table cannot break the authorization check**, because the
check reduces the region to an id set. The only way to break it would be to put an id-shaped token
into a new column. An order number (`3`) and a tier (`2`) are not id-shaped. **Safe.**

### The one real behaviour change: row ORDER

`--status` reports the next unit as `nonterminal_units | head -1` (`unattended.sh:2226`). Today
`render_region:642` sorts by `key=lambda x: x["path"]` — filename date, then lexical id, so `-10`
sorts before `-2`. Re-sorting the units table by build order makes **`--status` name the first
non-terminal unit in BUILD ORDER instead of in path order.** That is what the owner wants and it is
strictly better, but it is a visible driver behaviour change and must be stated, not slipped in.
`units-at-landing` (`:1871`) also re-orders; it is consumed as a set, so harmless.

---

## 4. Removing `gen:build-docs` — blast radius, and the two questions are separate

### Who reads it: nobody

`git grep -n "gen:build-docs" -- . ':!memory/builds'` returns exactly one hit: the `GEN_REGIONS`
tuple at `gen_build_index.py:73`. No driver, no leg, no check, no skill, no protocol names it. It is
rendered by `render_docs` (`:749-771`) and read by human eyes only.

### The blast radius is region-retirement mechanics, not readers

1. **`--check-format` (a merge-bar leg).** `slot_violations` (`:995-1024`) collects spans only for
   regions in `GEN_REGIONS`, then flags any non-blank line after the first generated open that is not
   inside a registered span. Delete the `build-docs` entry and the 61 READMEs still carrying
   `<!-- gen:build-docs -->` … `<!-- /gen:build-docs -->` become **61 files' worth of slot
   violations**, because those lines are now unregistered content after the first open marker.
   **The retirement must delete the markers from all 61 READMEs in the same commit** — and `--write`
   cannot do it for you: `plan()` only *creates* pairs (`:1084-1088`), never removes them.
2. **Hygiene check 9** (`--check`) reds until that render lands, in the same commit.
3. **`check-verdict-epoch.sh`** forces a memory-tree kit version bump (`gen_build_index.py` is in
   `DELEGATES`, `:69`).
4. **`memory/map/features/build-readme-surface.md`** claims `gen_build_index.py` and the
   `build README slot contract` gate leg, and names `GEN_REGIONS` as a reuse-affordance seam.
   Dossier refresh is a DoD item.
5. **`insert_region`** (`:1006-1024`) walks `GEN_REGIONS` backwards then forwards for an anchor.
   Dropping the LAST entry is the cheapest case — no other region's insertion anchor moves.

### The size dividend — the strongest argument for the owner's ask

Measured through `plan()` over the real tree (`<scratchpad>/probe2.py`):

```
record rows: 223   over 350 bytes: 17
OVER-CAP memory/builds/aBoundedVerdict/README.md:    total 44872 · records-table 3915 · build-docs 3026 · after removing both 37931
OVER-CAP memory/builds/aRuledFrontispiece/README.md: total 26947 · records-table 1521 · build-docs 1650 · after removing both 23776
OVER-CAP memory/builds/cBriefedPilot/README.md:      total 32023 · records-table 2006 · build-docs 2519 · after removing both 27498
OVER-CAP memory/builds/dUnstalledConvoy/README.md:   total 35745 · records-table 6731 · build-docs 5530 · after removing both 23484
```

`BUILD_README_CAP_BYTES=25600` (`check-memory-hygiene.sh:45`). **Removing both surfaces drops
`aRuledFrontispiece` and `dUnstalledConvoy` under the byte cap outright.** See §6 for the per-line
dividend and the debt rows that drain.

### The records table inside `gen:build-index` is a SEPARATE question — and the load-bearing one

`gen:build-docs` (a flat per-kind link list, `render_docs:749-771`) and the
`| Record | Kind | Serves |` table plus its two coverage joins (`render_region:660-678`) are **two
renderings of two different datasets**:

- `build["docs"]` (`collect:596-597`) — every tracked file under the build's four kind folders,
  filename parsed not at all. Pure inventory.
- `build["records"]` (`plan:1075-1078`) — only records whose `**Serves:**` line parsed to `bound` or
  `unbound`, carrying the resolved id set.

**Removing `gen:build-docs` costs nothing but the link list. Removing the records table costs the two
coverage joins**, at `gen_build_index.py:669-678`:

```python
gap  = [i for i in own if i not in named]     # "Ids no record names: …"
agap = [i for i in own if i not in audited]   # "Ids no `spec-audit` record has ever named: …"
```

**What they buy.** Hygiene check 21 gates the **record → spec** direction: every record must name a
spec that exists (`check-memory-hygiene.sh:659-690`, four fail branches). **Nothing gates the
spec → record direction.** These two rendered sentences are the *only* place in the repo where "this
unit has no evidence at all" and "this unit was never spec-audited" are visible.
`git grep -n "Ids no record names"` outside `memory/builds/` returns only the generator itself
(`:673`) and its own selftest arms (`:1634`, `:1646`) — so they are report-only, gated by nothing.

**What would replace them.** Two options, both derivable from the same `binds_all`:

- render the same two sentences into the per-spec records region — per-unit, so they degenerate to
  "this spec has no records" / "no spec-audit record names this spec"; or
- promote them to a real gate leg with a declared pin, in the shape check 21 already uses
  (`RECORD_UNBOUND_PIN`): a `SPEC_UNAUDITED_PIN` over `agap` across the corpus.

The second is what this repo's own §7 would demand. A rendered sentence nobody gates is a documented
check at best, and this one is not even written down as one.

### The `**Serves:**` binding, and whether the inverse is derivable — YES, exactly

Grammar, `memory/HYGIENE.md:261-262`:

```
**Serves:** <kind> <id> [<id> …]
**Serves:** none — <why this record serves no spec>
```

Parsed by `BIND_RE` at `gen_build_index.py:363-365` (optional leading comment marker, so a shell
script under `build/` can carry one); kinds `("spec-audit","diff-review","journal","research")` at
`:352`; ranges expanded at authoring time by `_expand_ids` (`:404-423`).

**The inverse is a one-line invert of a dict the generator already builds.** `plan()` computes
`binds_all` ONCE for the whole tree at `gen_build_index.py:1064-1065` — global, not per build. So:

```python
serving = {}                                   # unit id -> [record paths]
for p, rec in binds_all.items():
    if rec["state"] != "bound":
        continue
    for i in rec["ids"]:
        serving.setdefault(i, []).append(p)
```

Measured (`<scratchpad>/probe4.py`):

```
bound records: 213 · id->record edges: 789 · ids served: 248
edges whose id belongs to another build: 17
max records serving one id: TOOL-dScriptedRepeat-1 (11), TOOL-aBoundedVerdict-1 (10), TOOL-aBoundedVerdict-2 (9)
```

Two facts that matter for the design:

- **17 of 789 edges cross a build boundary.** A record housed under build X serves an id belonging to
  build Y. `plan()` files each record under the folder that HOUSES it (`:1074-1078`, comment: *"a
  cross-build record renders where a reader will look for it"*). A spec-side inversion keys on the
  **id**, so those 17 land on the right spec — a small correctness improvement, and a behaviour
  change worth naming.
- **The heaviest spec would carry 11 record links.** At ~90 bytes per line that is under 1 KB — and
  **spec files are not in the hygiene index set.** `index_set()` (`check-memory-hygiene.sh:400-422`)
  is: the memory root's four index files, ledger shards, map dossiers, backlog shards,
  `builds/*/STATUS.md`, `builds/*/README.md`, `builds/*/RUN*.md`. **Specs pay no byte cap and no
  entry budget.** Moving the record surface off the README and onto the spec moves it from a capped
  file into an uncapped one. That alone answers `TOOL-dUnstalledConvoy-13`.

**The cost of writing into specs.** It is a new write surface for a generator that today writes only
build READMEs, `LIVE.md` and the ledger shards. What I verified:

- Check 12's section canon compares `^## ` heading lines only (`check-memory-hygiene.sh:729-737` and
  the awk at `:839-841`), so an HTML-comment marker pair is not a section and does not break it.
- Check 12's header scan reads only the **first 5 unfenced lines** (`:800-802`), so a region below §1
  is out of its way.
- **UNVERIFIED:** I did not fully trace check 12's §9 revision-log range extraction (it "CLOSES on the
  next `## ` heading" per the comment at `:870`). A region placed *inside* §9 could interact with it.
  Place the region after §10 or at end-of-file and this is moot; a unit doing this must verify.
- `parse_spec` reads specs; if the generator also writes them, the read-your-own-output hazard that
  `rosters()` is built to avoid (`:508-518`) applies. The region's content derives from `binds_all`,
  which derives from **record** heads and not from spec bodies, so there is no cycle — but the
  exclusion must be written down the way `rosters()` writes its own.

---

## 5. The dependency question — `TOOL-aBoundedVerdict-7`

The row, verbatim (`memory/backlog/TOOL.md:117`):

> `- TOOL-aBoundedVerdict-7 · OPEN · nothing records inter-unit dependencies; a build README's authored order carries them in prose, so TOOL-aBoundedVerdict-3 S3's every-remaining-unit-depends-on-it test is the run's judgment. A front-matter dependency field would make it derivable — its own unit`

Neighbours (`memory/backlog/TOOL.md:110-124`) are unrelated: `-6` run-state spill, `-32` a false AC
claim, `-8` review disposal, `-9` check 10 inert, `-10` a hanging leg.

**Verdict: the ORDER # ask PARTLY satisfies it, does not conflict with it, and does not subsume it.**

- The row's stated *harm* is that the ordering "is the run's judgment" — unreadable by machine. A
  derived ORDER # column removes exactly that harm for the **sequencing** question: the driver could
  read a total order instead of a paragraph.
- The row's stated *remedy* is "a front-matter dependency field", i.e. an **edge set**. `order <n>`
  is a **total order with parallel ties** — a linear extension of a DAG, not the DAG.

**Corpus evidence that the distinction is real.** `memory/builds/dScriptedRepeat/README.md` carries a
hand-authored predecessor ("Must land after") framing, while
`memory/builds/aRuledFrontispiece/README.md:129-138` hand-authors the *other* shape,
`| # | Id | Tier | Mechanism |` with `#` as a step number, and states at `:107`:

> **"Below this line, every unit is named by ID, never as 'unit N'** — the `#` column is build ORDER
> and the id sequence is MINT order, and they stopped agreeing when the audit reordered the build."

The corpus already carries **both** encodings by hand, in two builds, and the owner's ask names the
aRuledFrontispiece one.

**Is `order <n>` expressive enough to replace a predecessor DAG? No, and here is the exact loss.** A
total order says "3 comes after 2". A DAG says "3 depends on 2 *and not on 1*". They diverge whenever
a unit is reordered: with a DAG, the move is checked against its edges; with a step number, the move
is unchecked and the only signal is that two numbers changed. `TOOL-aBoundedVerdict-3` S3's "every
remaining unit depends on it" test is a reachability question over edges, and a step number can only
answer "is anything numbered higher".

**Recommendation:** take `order <n>` now — it is already parsed, and it is what the owner asked for —
and **leave `TOOL-aBoundedVerdict-7` OPEN with a note that the step verb narrowed it without closing
it.** Closing it on the strength of a step column would be the "made true later and by another unit"
class that `TOOL-aBoundedVerdict-32` (`memory/backlog/TOOL.md:119`) exists to record.

---

## 6. The row-width problem — the premise is wrong, measured

### The two claims

- `memory/backlog/TOOL.md:20` — `TOOL-dUnstalledConvoy-13`: *"a build's **spec-audit record** cannot
  fit the generated **record-bindings row**… the row carries the record filename, its path and every
  id the record serves… Measured on dUnstalledConvoy - 13 units, 438 chars against the 350 tier."*
  **This row is about the RECORDS table, not the units table. It says so.**
- `memory/project/curation-debt.txt`, the `aRuledFrontispiece` block: *"11 units with long spec titles
  put three GENERATED **unit-table** rows over the per-line tier."* **This row is WRONG about which
  table.** The three over-cap lines in that file are `:319`, `:320`, `:321` — all three are
  `| [2026-08-1x-review-TOOL-aRuledFrontispiece-1-N.md](reviews/…) | spec-audit | …` rows. The units
  region in that same file spans `:298`–`:312`, and its widest unit row is **187 bytes**.

### The measurement

```
$ for f in memory/builds/*/README.md; do awk '…inside gen:build-units && /^\| \[/…' "$f"; done | sort -rn | head
230  memory/builds/dUnstalledConvoy/README.md   | [TOOL-dUnstalledConvoy-9 …
223  memory/builds/dUnstalledConvoy/README.md
219  memory/builds/dUnstalledConvoy/README.md
```
```
$ python3 <scratchpad>/probe2.py
record rows: 223   over 350 bytes: 17
```

| Population | Widest | Cap | Over cap |
|---|---|---|---|
| Generated **unit** rows (260 of them) | **230 bytes** | 350 | **0** |
| Generated **record** rows (223 of them) | **593 bytes** | 350 | **17** |
| Front-matter `ids:` line | 894 bytes | *exempt* (`check-memory-hygiene.sh:520-527`) | n/a |
| Authored table rows | 517 bytes | 350 | 6 |

**Not one generated unit row is over the cap. All 17 over-cap generated lines are record rows.**

### Projected cost of +order +tier

`<scratchpad>/probe.py` renders both shapes for every real unit:

```
cur 228  proj 236  dUnstalledConvoy TOOL-dUnstalledConvoy-9
cur 221  proj 229  dUnstalledConvoy TOOL-dUnstalledConvoy-11
cur 217  proj 225  dUnstalledConvoy TOOL-dUnstalledConvoy-33
```

(Python counts characters; the awk figures count bytes, and the row carries one em dash — hence 230
vs 228. The delta is what matters.)

**Two cells cost +8 bytes.** The worst row goes **230 → 238** against a 350 cap. **112 bytes of
headroom survive.** A third cell — node, or a records count — would still fit.

### The row shape that survives

The current unit row already survives. **The shape that does NOT survive is the records row, and the
owner's ask deletes it from this file.** Removing the records table drains all 17 over-cap generated
lines, and by byte total drains `aRuledFrontispiece` (26947 → 23776) and `dUnstalledConvoy`
(35745 → 23484) below the 25600 cap. `aDrainedSluice`'s single over-cap line (394 bytes, `:62`) is a
record row too, and its file is under the byte cap.

**Three of the six `curation-debt.txt` rows drain**: `aRuledFrontispiece`, `dUnstalledConvoy`,
`aDrainedSluice`. `aUnmannedHelm` stays (its over-cap line at `:78` is authored prose).
`aBoundedVerdict` (37931 after) and `cBriefedPilot` (27498 after) stay over on authored bulk.
**`TOOL-dUnstalledConvoy-13` closes outright** — its subject moves into a file with no cap.

**Recommendation on the row shape:** keep the current shape and add the two cells. Do **not**
abbreviate the title — it is what makes the table readable, and it is not the thing over cap. If a
future unit does need width, the cheapest cut is the date-prefixed filename in the link target, not
the title.

---

## 7. Recommendation — the exact output, and every consumer change it forces

### 7a. `render_region`'s units table

Replace `gen_build_index.py:641-646` with a six-column table sorted by order, then id sequence:

```python
out += ["| Unit | # | Tier | Status | Rev | Last change |", "|---|---|---|---|---|---|"]
for u in sorted(build["units"],
                key=lambda x: (x["order"] if x["order"] is not None else 10**6,
                               _seq(x["id"]), x["path"])):
    rel   = u["path"].split(f"/builds/{build['slug']}/", 1)[1]
    label = f"{u['id']} — {u['title']}" if u["title"] else u["id"]
    step  = u["order"] if u["order"] is not None else "—"
    out.append(f"| [{label}]({rel}) | {step} | {u['tier']} | {u['status']} | rev-{u['rev']} | {u['date']} |")
```

with `parse_spec` (`:277-286`) gaining one key: `"tier": hdr.group("tier")`.

**Literal rendered output for `memory/builds/aRuledFrontispiece/README.md`**, using the step numbers
its own authored table already carries at `:129-138` (generated by `<scratchpad>/probe3.py`; the
trailing byte counts are annotations, not part of the render):

```
| Unit | # | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aRuledFrontispiece-1 — the build README gets a slot contract and an immutable authored plan](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-1.md) | 1 | 2 | CLOSED | rev-4 | 2026-08-17 |     (193 B)
| [TOOL-aRuledFrontispiece-8 — check 8 stops judging a run it can no longer repair](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-8.md) | 2 | 2 | CLOSED | rev-2 | 2026-08-17 |     (176 B)
| [TOOL-aRuledFrontispiece-5 — the build README joins the hygiene index set at its own cap tier](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-5.md) | 3 | 2 | CLOSED | rev-2 | 2026-08-17 |     (189 B)
| [TOOL-aRuledFrontispiece-7 — the STATUS.md slot is retired](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-7.md) | 4 | 1 | CLOSED | rev-2 | 2026-08-17 |     (154 B)
| [TOOL-aRuledFrontispiece-9 — the build method's roster claim and its parallelism test are corrected](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-9.md) | 5 | 2 | CLOSED | rev-2 | 2026-08-17 |     (195 B)
| [TOOL-aRuledFrontispiece-11 — the corpus is conformed to the slot contract, by hand](spec/2026-08-17-spec-TOOL-aRuledFrontispiece-11.md) | 6 | 2 | CLOSED | rev-1 | 2026-08-17 |     (180 B)
| [TOOL-aRuledFrontispiece-10 — the corpus retrofit and the kit version bump](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-10.md) | 7 | 2 | CLOSED | rev-2 | 2026-08-17 |     (171 B)
| [TOOL-aRuledFrontispiece-6 — the slot contract becomes a leg of its own on the merge bar](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-6.md) | 8 | 2 | CLOSED | rev-2 | 2026-08-17 |     (184 B)
| [TOOL-aRuledFrontispiece-2 — build order and parallel groups become a header verb and a region](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-2.md) | — | 2 | WONTDO | rev-3 | 2026-08-17 |     (192 B)
| [TOOL-aRuledFrontispiece-3 — dependency edges between builds, declared once and rendered both ways](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-3.md) | — | 2 | WONTDO | rev-3 | 2026-08-17 |     (196 B)
| [TOOL-aRuledFrontispiece-4 — the build README gets a generated document inventory](spec/2026-08-16-spec-TOOL-aRuledFrontispiece-4.md) | — | 2 | WONTDO | rev-3 | 2026-08-17 |     (179 B)
```

Max 196 bytes against a 350 cap. This table **replaces** the hand-authored
`| # | Id | Tier | Mechanism |` block at `README.md:129-138` — four of the five columns the owner
asked for, authored today, in a file this generator already owns.

### 7b. `render_order`

With `#` on the units table, the standalone order region reduces to what the units table cannot show:
the **parallel groups**. Keep the region, drop the per-unit repetition:

```
<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 3 | `TOOL-x-4`, `TOOL-x-7` | yes |

Unordered: `TOOL-x-2`, `TOOL-x-3`.
<!-- /gen:build-order -->
```

i.e. render only the steps where `len(us) > 1`, plus the residual line. For a build with no ties the
region collapses to one sentence and the units table carries the whole order. If the owner would
rather have one surface, the region can be retired — but that is a `GEN_REGIONS` deletion with the
61-README marker surgery §4 describes.

### 7c. Forced consumer changes

**Must land in the same commit:**

1. `parse_spec` gains `"tier"` (`gen_build_index.py:277-286`).
2. `render_region`'s table head, row and sort key (`:641-646`).
3. `python3 tools/memory-tree/gen_build_index.py --write` over all 61 READMEs, or hygiene check 9
   (`check-memory-hygiene.sh:594-596`) reds.
4. `tools/unattended/unattended.test.sh:116` — the fixture's hardcoded
   `| Unit | Status | Rev | Last change |` header and its row.
5. `gen_build_index.py --selftest` arms asserting the units table (`:1466`, `:1498`, `:1510`,
   `:1626-1650`).
6. `check-verdict-epoch.sh` (`:69`) — the memory-tree kit version constant must bump.
7. `memory/map/features/build-readme-surface.md` — the dossier claims this file and this leg.

**Must be stated, not just done:**

8. `--status`'s "next unit" (`unattended.sh:2226`) changes from path order to build order.
9. `units-at-landing` (`unattended.sh:1871-1873`) freezes in a different order. Consumed as a set,
   so harmless — but the frozen bytes change on every future landing.

**Verified safe, no change needed:**

10. `check_authorization` (`unattended.sh:1251-1268`) — id set, not row bytes.
11. `unit_rows` (`:1540`) — `^\| \[.*\]\(spec/` still matches; the link cell stays first.
12. `nonterminal_units` (`:1543`) and check 24 (`check-unattended.sh:1505`) — `| CLOSED |` and
    `| WONTDO |` stay whole `|`-delimited cells.
13. `baseline_units` (`lib-unattended.sh:186-207`) and checks 2/13/19/21 — id sets and front matter.
14. Hygiene checks 6/7 — 238 bytes against 350; no new debt.

**Required BEFORE the verb can be made mandatory (fork 5's un-owned follow-up):**

15. Fix `ORDER_RE` (`:110`) so `order 0x2` and `order 2x` are named refusals rather than silent steps
    0 and 2 — the shape `TOOL-aRuledFrontispiece-2` §4 specified and that never shipped.
16. Amend `tools/memory-tree/SPEC-TEMPLATE.template.md`'s status-header section, which today says the
    tail holds pointers only, and re-render `memory/TEMPLATE-SPEC.md` via
    `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`.
17. Pick the dated cutoff. `SPEC_FORMAT_CUTOFF`, `STREAMS_CUTOFF`, `SPEC10_CUTOFF` and
    `UNITS_REGION_CUTOFF` are the four precedents; the last is at `.unattended.conf:95`.

### 7d. On the records surface

Retire `gen:build-docs` (zero readers) **and** move the `| Record | Kind | Serves |` table to a
per-spec region keyed on the id, derived by inverting `binds_all` (`plan:1064-1065`). Carry the two
coverage joins with it — per-spec, or better, promote `agap` to a pinned gate leg beside check 21's
`RECORD_UNBOUND_PIN`, since it is today the only spec→record signal in the tree and nothing gates it.
The dividend is measured: 17 over-cap generated lines gone, three curation-debt rows drained,
`TOOL-dUnstalledConvoy-13` closed, and 223 record links moved from a capped file into uncapped ones.

---

## Marked UNVERIFIED

- Check 12's §9 revision-log range extraction (`check-memory-hygiene.sh:~870`) vs. a generated marker
  region placed inside a spec body. I verified the section canon reads `^## ` only and the header
  scan reads lines 1–5 only; I did not trace the §9 range logic to a conclusion.
- Whether `tools/unattended/unattended.test.sh` asserts unit-row ORDER anywhere beyond the fixture at
  `:116`. I found the fixture; I did not audit every assertion in that file.
- Whether any adopter repo outside this tree consumes the units table. Out of reach from here.
