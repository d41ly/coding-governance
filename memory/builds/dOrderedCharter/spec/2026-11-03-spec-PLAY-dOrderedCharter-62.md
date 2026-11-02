# PLAY-dOrderedCharter-62 — the layer check resolves `{prefix}` in an optional row's part and refuses a part that spells the tool root

**Status:** CLOSED · rev-1 · 2026-11-03 · node d · Tier-2 · base 8bec4cef · streams playbook · order 3 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 |
| [2026-11-03-build-PLAY-dOrderedCharter-62-1-builder-return.md](../build/2026-11-03-build-PLAY-dOrderedCharter-62-1-builder-return.md) | journal | — |
| [2026-11-03-build-PLAY-dOrderedCharter-62-ledger.md](../build/2026-11-03-build-PLAY-dOrderedCharter-62-ledger.md) | journal | — |
| [2026-11-03-prompt-PLAY-dOrderedCharter-62-1-spec-writer.md](../prompts/2026-11-03-prompt-PLAY-dOrderedCharter-62-1-spec-writer.md) | journal | — |
| [2026-11-03-prompt-PLAY-dOrderedCharter-62-build-brief.md](../prompts/2026-11-03-prompt-PLAY-dOrderedCharter-62-build-brief.md) | journal | — |
| [2026-11-03-prompt-PLAY-dOrderedCharter-62-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dOrderedCharter-62-spec-brief.md) | research | PLAY-dOrderedCharter-17 |

<!-- /gen:spec-records -->

## 1. Goal

A flat govkit entry, `home = "."` under `tools/govkit/entries/`, can allow an edge today only with
`part = "tools/push-main.sh"`, and `tools/check-install-prefix.sh` bans that spelling in every
tracked `.toml`. This unit makes the check read `part = "{prefix}/push-main.sh"` through the one
`{prefix}` resolution the tree already gates, and refuse the literal by name, so the ban and the check
agree and PLAY-dOrderedCharter-17 can declare its flat-entry slots.

## 2. Scope (IN)

All lines are cited at HEAD `ca5be2eb9`.

- **S1** — One reader of the token. `tools/playbook/check_layers.py` carries the canonical
  `resolve_prefix_token` block of `tools/lib/resolve_prefix_token.py:11-22` inline, byte-identical,
  beside its `resolve_kit_dir` block (`check_layers.py:50-87`). The include resolution in
  `read_descriptors` (`:155`, `s = s.replace("{prefix}", tool_root)`) calls it in place of the
  hand-written replace. Observed by AC3.
- **S2** — The part resolution. `read_descriptors` (`:131-171`) resolves each `optional` row's `part`
  through the same function and carries the result as the descriptor's `parts` set. The allow test
  in `derive_edges` (`:320-323`) reads that set where it builds its own from the raw rows at `:321`.
  A flat entry's `{prefix}/<file>` then equals the edge's repo-relative path, which is what `:323`
  compares for a descriptor whose home is `None` (`:145-146`). Observed by AC1 and AC4.
- **S3** — The literal refused by name. `check_layers` (`:395-401`) reds every `optional` row whose
  raw `part` opens with the tool root and a slash, naming the descriptor, the part and the spelling
  to write, in the line §4 "### The reading" gives. It is a contract red, so the run exits 1 whatever
  the edges read. It binds every descriptor, homed kits included (§8 F1). Observed by AC2.
- **S4** — Two fixture plants, `flat-slotted` and `flat-literal`, in `PLANTS` (`:462-463`) and
  `build_layers_fixture` (`:466-519`), and as two rows of the plant table in
  `tools/playbook/adopt-playbook.sh:200-219`. Observed by AC1 and AC2.
- **S5** — The spelling, said. The module docstring (`check_layers.py:9-12`) and the `optional`
  paragraph of `tools/playbook/README.md` (`:162-164`) say a `part` is relative to the kit's home,
  and that a flat entry spells a file under the tool root `{prefix}/<file>`. Observed by AC5.

## 3. Non-goals (OUT)

- Relaxing the install-prefix ban. `GOVPFX` (`tools/check-install-prefix.sh:386`) is zero-tolerance
  by its header (`:24-28`), and `{prefix}/` is already one of its drained spellings (`:398`).
- Declaring any slot or curing any edge: PLAY-dOrderedCharter-17's.
- A root install, where the tool root is `.`. The token resolves there by the canonical's own rule,
  but `read_descriptors`' descriptor globs (`:134`) find no descriptor at that root today either.
- Resolving `{prefix}` in a homed kit's withheld `include` patterns (`:161-164`) or in `requires_if`.
- Units 16 and 61, which are CLOSED and stay frozen.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-61` — the repaired `tools/playbook/check_layers.py`, its fixture and `adopt-playbook.sh`'s plant table; without them the plants have no edge reading to allow
- **hands-off** `PLAY-dOrderedCharter-17` — the flat-entry `optional` rows spelled `{prefix}/<file>`, for `push-main.sh`, `push-main.test.sh`, `check-install-prefix.sh` and its suite, `check-kit-versions.sh`, `check-wiring.sh` and its suite, and `settings-merge.py`

## 4. Design

### The reading

`read_descriptors` already holds `tool_root`. Each kit dict gains one key:

```python
"parts": {resolve_prefix_token(o.get("part"), tool_root) for o in optional},
```

`derive_edges` replaces `parts = {o.get("part") for o in src["optional"]}` (`:321`) with
`parts = src["parts"]`; `:322-323` are unchanged. For a homed kit the bare `gen_build_index.py` form
still matches through `rel`, and a `{prefix}/memory-tree/gen_build_index.py` form would match
through `f`. Nothing in the tree declares an `optional` row today:
`grep -rn "optional = " tools --include=*.toml` prints none, so the tree's edges do not move (AC4)
and the plants are the coverage.

The refusal reads the raw row, never `parts`, since the resolved spelling of `{prefix}/x` is the
literal it refuses. In the loop at `:400-401`, beside the `check_point` call:

```python
if str(o.get("part") or "").startswith(tool_root + "/"):
    reds.append("descriptor %s's optional row part %r spells the tool root literally: spell it {prefix}/%s"
                % (k["path"], o.get("part"), str(o["part"])[len(tool_root) + 1:]))
```

A refused part still allows its edge, because the contract red already fails the run and a second
red on the same row would name a missing row that exists.

### Why the canonical block and not `:155`

The brief asks for the resolution `read_descriptors` applies to `include`. That line is a hand-written
`.replace("{prefix}"`, the form `tools/lib/resolve-python.test.sh` bans outside a marked block
(`scan_prefix_token`, `:856-868`, its form at `:864`, its population every tracked `*.py` at `:870`).
Grep with that form over `check_layers.py` prints `:155` at HEAD. UNVERIFIED that the
`python resolver (behaviour + inline parity + idiom ban)` leg reds on it: this writer ran no gate. Adding a second hand-written replace for `part`
would add a second hit, so S1 routes both through the canonical block. The parity table's
`resolve_prefix_token` row (`:360`) finds every marked copy by `git grep -l "^# >>> $stem"` (`:409`),
so the new copy is graded with no row added. At the tool root `tools` the block and `:155` return the
same string; they differ only at an empty or `.` root (§3).

### The plants

Both plants add one core flat entry to the fixture. Its shipped file is extensionless and run as
shell by `check_shell_file` (`:327-334`), because a `tools/<name>.<ext>` literal in the plant's
source or in the plant table is a hit of `GOVPFX` (`:386`, its extension class `EXT` at `:345`).
The register lists `govkit` in `shared`, so the entries directory is covered by the tool-directory
check (`:405-412`).

```
tools/govkit/entries/flatkit.kit.toml
  id = "flatkit"
  home = "."
  layer = "layer.core"
  optional = [{ part = "{prefix}/flatgo", point = "point.core.slot", fallback = "fixture" }]
  [[files]]
  include = ["flatgo"]
tools/flatgo
  #!/usr/bin/env bash
  bash "$ROOT/tools/expkit/go.sh"
```

`flat-literal` writes the same files with `part = "tools/flatgo"`. The plant table gains:

```
flat-slotted --list|0|layers: edge tools/flatgo:2 · shell · flatkit -> expkit · allowed
flat-literal|1|optional row part 'tools/flatgo' spells the tool root literally: spell it {prefix}/flatgo
```

### Inventory

Minted: the plants `flat-slotted` and `flat-literal`; the descriptor key `parts`; the refusal line of
S3; the fixture names `flatkit` and `flatgo`. No function is minted: `resolve_prefix_token` is a
copy of the canonical, whose name the tree already spells.

### Rollout

Live at landing. The tree's layer leg reads as PLAY-dOrderedCharter-61 left it, 40 red, until
PLAY-dOrderedCharter-17's pass declares the rows.

### Files touched (estimate)

- `tools/playbook/check_layers.py`
- `tools/playbook/adopt-playbook.sh`
- `tools/playbook/README.md`
- `memory/map/generated/symbols.json` (regenerated for the inlined function)

### Alternatives rejected

- **Give a flat entry the tool root as its home.** `home` feeds the home-word map (`:187-189`) and the
  tool-directory coverage (`:405`), so the tool root would read as a kit home; and a flat entry's
  `root_relative` files, such as push-main's `.githooks/pre-push`, sit outside it.
- **A second hand-written replace for `part`.** A copy at the kind's second instance (charter
  `[reuse]`), and a second hit of the resolve-python ban.
- **Accept `tools/<file>` in the check and waive it in the ban.** The ban has no waiver by design
  (`check-install-prefix.sh:24-28`), and the brief's non-goal keeps it unrelaxed.

## 5. Production-readiness checklist

- security: read-only over the tree; no new write path.
- perf / scale: one string resolution per `optional` row; no new file read.
- error / empty / loading states: a row with no `part` resolves to the string `None` and allows nothing, as today; an unreadable descriptor still exits 2.
- observability: the refusal names the descriptor, the part and the spelling to write.
- risks: the `.` root behaviour of `:155` changes to the canonical's, at a root the descriptor globs do not reach (§3).
- testing: AC1 to AC5, and the arms of §7.
- migration: none; an adopter receives `check_layers.py` with the playbook-render kit, and a part spelled the old literal way is named. The kit epoch leg decides whether `KIT_PLAYBOOK_RENDER_VERSION` (`tools/playbook/render_playbook.py:1887`) moves.
- user docs: `tools/playbook/README.md`, the `optional` paragraph (S5).

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/check_layers.py --fixture --plant flat-slotted --list` runs,
  it exits 0 and prints `layers: edge tools/flatgo:2 · shell · flatkit -> expkit · allowed`.
  Red when: the part is compared unresolved, as `:321` does at HEAD, and the edge prints red with
  exit 1.
- **AC2** — When `python tools/playbook/check_layers.py --fixture --plant flat-literal` runs, it
  exits 1 and prints `layers: RED descriptor` naming the fixture's flat entry, then
  `optional row part 'tools/flatgo' spells the tool root literally: spell it {prefix}/flatgo`.
  Red when: the literal is accepted silently, as at HEAD, where the same descriptor exits 0.
- **AC3** — When `grep -n 'replace("{prefix}' tools/playbook/check_layers.py` runs, it prints only
  the two lines inside the `resolve_prefix_token` block; and `sed -n '/^# >>> resolve_prefix_token/,/^# <<< resolve_prefix_token/p'`
  over `tools/lib/resolve_prefix_token.py` and over `tools/playbook/check_layers.py` prints the same
  bytes.
  Red when: the hand-written resolution at `:155` remains, or the inline block drifts from the
  canonical.
- **AC4** — When the builder saves the `layers: edge` lines of
  `python tools/playbook/check_layers.py --list` before the first edit and after the pass, `diff`
  of the two prints nothing.
  Red when: the resolution moves an edge of the tree, where no descriptor declares an `optional` row.
  figure: the edge set is DERIVED at both runs; 40 red is PINNED by PLAY-dOrderedCharter-61 at
  `20d02c59c`.
- **AC5** — When `grep -n '{prefix}/<file>' tools/playbook/README.md tools/playbook/check_layers.py`
  runs, it prints the README's `optional` paragraph and the docstring's register paragraph.
  Red when: neither says how a flat entry spells its part.

## 7. Gates

`layer dependencies (the core never depends on an expansion)` · `python resolver (behaviour + inline parity + idiom ban)` · `playbook render selftest` · `govkit acceptance matrix` · `install-prefix (shipped surface)` · `recall floor` · `recall floor arms` · `memory hygiene` · `kit epoch (shipped bytes move, the version moves)`

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 · the plant table's `flat-slotted` and `flat-literal` rows, each asserting its exit and its named line, red against the check with `:321` restored · none

## 8. Open questions

- **F1 — Whether the resolution and the refusal reach a homed kit's part, or only a flat entry's.**
  Options: (A) a flat entry only, the brief's wording, behind an `if k["home"] is None` branch;
  (B) every descriptor. The ban counts a `tools/<kit>/...` literal in a homed kit's `kit.toml` as it
  counts one in an entry (`GOVPFX`, `check-install-prefix.sh:386`), so under A the same disagreement
  stays silent for a homed kit. Neither option trips a veto. RESOLVED (agent, 2026-11-03, delegated):
  B, by M3's feature-rich rule, tie-broken by the smaller diff, since B needs no branch, by
  `2026-11-03-prompt-PLAY-dOrderedCharter-62-spec-brief`. widens: S2 and S3 reach homed descriptors ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, by `2026-11-03-prompt-PLAY-dOrderedCharter-62-spec-brief`.

## 10. Reuse audit

The seam extended is `resolve_prefix_token`, canonical at `tools/lib/resolve_prefix_token.py` and
carried inline under its marker by ten files under the tool root and by `WIRE-INTO-PROJECT.md`,
PINNED by `git grep -l "^# >>> resolve_prefix_token"` at HEAD. `python tools/codebase-map/reuse_lookup.py "resolve the prefix token in a descriptor path against the tool root"`
ranked it a SEAM, fan-in 11, installs 12, with `read_descriptors` (`tools/playbook/check_layers.py`,
`tools/govkit/govkit.py`, `tools/run-gates/regen.py`) and `derive_tool_root` beside it. The allow
test is unit 16's `optional` row as unit 61 left it (`check_layers.py:320-323`); the spelling the
check accepts is the ban's drained `{prefix}/` (`check-install-prefix.sh:398`). Where the brief and
the source disagree: the brief names `read_descriptors`' include resolution as the reader to share,
and that line (`:155`) is itself a hand-written form the resolve-python ban refuses, so the shared
reader is the canonical block and `:155` moves onto it; and the brief's plant file `x.sh` is
extensionless here, because a `tools/<name>.sh` literal in the plant's source is a ban hit.

Recall terms used: `python tools/codebase-map/reuse_lookup.py "resolve the prefix token in a descriptor path against the tool root"`
