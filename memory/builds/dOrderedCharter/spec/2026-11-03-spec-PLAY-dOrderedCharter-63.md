# PLAY-dOrderedCharter-63 — the spec-token checker reads a spec's liveness from its status header, never from a fenced example

**Status:** CLOSED · rev-1 · 2026-11-03 · node d · Tier-2 · base 8bec4cef · streams playbook · order 7 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-64 |
| [2026-11-03-build-PLAY-dOrderedCharter-63-1-builder-return.md](../build/2026-11-03-build-PLAY-dOrderedCharter-63-1-builder-return.md) | journal | — |
| [2026-11-03-build-PLAY-dOrderedCharter-63-ledger.md](../build/2026-11-03-build-PLAY-dOrderedCharter-63-ledger.md) | journal | — |
| [2026-11-03-prompt-PLAY-dOrderedCharter-63-1-spec-writer.md](../prompts/2026-11-03-prompt-PLAY-dOrderedCharter-63-1-spec-writer.md) | journal | — |
| [2026-11-03-prompt-PLAY-dOrderedCharter-63-build-brief.md](../prompts/2026-11-03-prompt-PLAY-dOrderedCharter-63-build-brief.md) | journal | — |
| [2026-11-03-prompt-PLAY-dOrderedCharter-63-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dOrderedCharter-63-spec-brief.md) | research | PLAY-dOrderedCharter-24 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-spec-tokens.py` builds its graded population with `LIVE.search` over a spec's whole text
(`:356`, `re.M`; the read at `:1501`), so any column-0 `**Status:** OPEN` line anywhere grades the
spec live. `memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-12.md` reads
`DEFERRED` at its header and holds a fenced example status line reading OPEN at `:110`, so the checker
graded a parked spec and refused every dispatch of this build. This unit makes the checker read a
spec's liveness from its status header alone: the first `**Status:**` line outside any fenced block.

## 2. Scope (IN)

All lines are cited at HEAD `4e14dd8ab`; the base `8bec4cef` holds the same lines in this file.

- **S1** — The header read. A new predicate `check_live_header(text)` in
  `tools/check-spec-tokens.py` finds the first line opening `**Status:**` in
  `render_unfenced(text)` (`:1172-1188`) and returns whether `LIVE` (`:356`, unchanged) matches that
  line. A spec with no such line outside a fence is not live, as a spec with no match is today. The
  population loop in `main` (`:1499-1504`) calls it where it calls `LIVE.search`; `LIVE` keeps its
  token set, so a DEFERRED spec stays ungraded. Observed by AC1, AC2 and AC3.
- **S2** — The rule, said. The module docstring's sentence "LIVE here is `LIVE` below" (`:156-157`)
  and the comment above `LIVE` (`:353-355`) say that liveness is the status header's token, the first
  `**Status:**` line outside a fenced block, read by `check_live_header`, and that a fenced example
  line is never read. Observed by AC4.
- **S3** — Three suite arms in `tools/check-spec-tokens.test.sh`, one per plant of §4 "### The
  plants", placed after arm 10, the frozen-spec arm (`:545-549`), and `FLOOR_ASSERTIONS` (`:60`) raised
  215 to 218 with a `RAISED` line in the house form above it (`:36-59`). Observed by AC1, AC2 and AC3,
  which the arms re-run.
- **S4** — `memory/map/generated/symbols.json` regenerated for the new function; the file lists the
  checker's functions today (`grep -c 'check-spec-tokens.py'` prints 37 at HEAD). Observed by AC4.

## 3. Non-goals (OUT)

- Grading a DEFERRED spec. That is the whitelist question of ask TOOL-dGatedProse-11; `LIVE`'s token
  set is unchanged.
- The header's grammar, its five-line window (`memory/TEMPLATE-SPEC.md:55`) and its fields: hygiene
  check 12 grades those, and the generator reads them through `HDR_RE`
  (`tools/memory-tree/tree_lib.py:376-380`).
- The other status readers. `tools/drift-audit/drift_report.py:559` and
  `tools/memory-tree/deviation_join.py:455-461` take the first status line of the whole text, so they
  differ from this rule only for a fence above the header, which no tracked spec holds (§6 AC5's
  measure). They are not this class: the defect here is a later line winning.
- Any edit of TOOL-dIndexedDesign-12 or another spec. Its §7 repair is an outside write of this run,
  made before this unit is built.

### Edges

none

## 4. Design

### The read

```python
STATUS_HEAD = re.compile(r"^\*\*Status:\*\*.*$", re.M)


def check_live_header(text):
    """True when the spec's status header, its first `**Status:**` line outside a fenced block,
    carries a LIVE token. A fenced example's status line is never read."""
    head = STATUS_HEAD.search(render_unfenced(text))
    return bool(head) and bool(LIVE.match(head.group(0)))
```

`render_unfenced` is the checker's own fence machine, the one its supersede and claims joins read
through (`:1206`, `:1223`), and it states its parity with the hygiene engine's `_unfenced`
(`:1173-1177`). It blanks a fenced line in place, so the first match is the first unfenced status
line. `main` at `:1501` becomes:

```python
        if check_live_header((root / f).read_bytes().decode("utf-8", "replace").replace("\r\n", "\n")):
```

### The plants

Each plant is the suite's `scratch` repo (`tools/check-spec-tokens.test.sh:336-363`), whose one
spec `TOOL-tOne-1` is OPEN and clean, plus the change in the table. The bad witness is the suite's
own: a §6 token spelled `${PFX}nope.sh`, which the paths join reds with
`not tracked by git ls-files` (`:393-396`). A fenced example below is a backtick fence of three
lines: the opening fence marker, the status line named, the closing marker.

| Plant | Change to the scratch repo | Exit, and what the output carries |
|---|---|---|
| deferred-fenced | adds `2026-09-02-spec-TOOL-tOne-2.md`: H1, a DEFERRED header, a `## 4. Design` holding a fenced example whose status line reads OPEN, a `## 6. Acceptance criteria` naming `${PFX}nope.sh` | 0 · `1 live spec(s) · 1 terminal spec(s) not graded`; `nope.sh` absent |
| fence-above-header | the same second spec, its fenced OPEN example placed between its H1 and its DEFERRED header | 0 · `1 live spec(s) · 1 terminal spec(s) not graded`; `nope.sh` absent |
| live-fenced-closed | `TOOL-tOne-1` keeps its OPEN header, gains a fenced example whose status line reads CLOSED, and its AC1 token becomes `${PFX}nope.sh` | 1 · `not tracked by git ls-files` and `1 live spec(s)` |

At HEAD the first two plants exit 1 with `2 live spec(s)` and the `nope.sh` hit. The third is the
guard against the over-correction: it passes at HEAD, and reds if a fenced terminal example can
freeze a live spec.

This spec writes no column-0 status line inside a fence, so the checker at HEAD reads it as
DEFERRED. The plants are described here and spelled by the arms.

### The measure

The probe AC5 runs, from the repo root at the pass tip. It loads the checker by path and prints
every tracked spec whose liveness differs between the whole-text read and the header read:

```bash
python -c "
import importlib.util as u, pathlib, re, subprocess as s
sp = u.spec_from_file_location('cst', 'tools/check-spec-tokens.py'); m = u.module_from_spec(sp); sp.loader.exec_module(m)
fs = [f for f in s.run(['git', 'ls-files', 'memory/builds'], capture_output=True, text=True).stdout.split() if re.match(r'memory/builds/[^/]+/spec/.*\.md$', f)]
t = lambda f: pathlib.Path(f).read_bytes().decode('utf-8', 'replace').replace('\r\n', '\n')
print(len(fs), [f for f in fs if bool(m.LIVE.search(t(f))) != m.check_live_header(t(f))])
"
```

This writer ran it at `4e14dd8ab` with a stand-in for `check_live_header` of the same two lines. It
printed 2822 tracked specs and one flip, TOOL-dIndexedDesign-12: 37 live under the whole-text read,
36 under the header read. The first-line rule of §8 F1's option A gave the same 36. Five tracked specs
carry no status line at all and read not live under every rule.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_live_header` | Python function, `tools/check-spec-tokens.py` | `py.function`, graded OK by `lexicon.py --suggest` |
| `STATUS_HEAD` | module constant, `tools/check-spec-tokens.py` | none |
| `deferred-fenced`, `fence-above-header`, `live-fenced-closed` | suite arm scratch dirs | none |

### Migration

None. The checker is a repo-root tool and ships in no kit descriptor
(`grep -l check-spec-tokens tools/*/kit.toml` prints nothing), so no kit version moves.

### Rollout

Live at landing. The tree's live population drops from 37 to 36 specs, the one spec AC5 names.

### Files touched (estimate)

- `tools/check-spec-tokens.py`: S1, S2
- `tools/check-spec-tokens.test.sh`: S3
- `memory/map/generated/symbols.json`: S4, regenerated

### Alternatives rejected

- **The generator's `parse_spec_text`** (`tools/memory-tree/gen_build_index.py:495-551`), the units
  table's header read, which the carries join already calls (`check-spec-tokens.py:949`). It
  would load `gen_build_index` on every run, where the checker loads it only while the carries key
  is set (`:452-456`). It also needs the conf's family alternation, and it raises `Problem` on a
  refused verb, so the population read could refuse. Its strict `HDR_RE` and five-line window give
  the same 36 live specs on the tree.
- **Dropping `re.M` from `LIVE`.** A spec's header is its third line, never its first, so a
  non-multiline pattern grades nothing and the checker refuses on an empty population.
- **A waiver row for TOOL-dIndexedDesign-12's leg hit.** It cures one instance; the next DEFERRED
  spec with a fenced example and a tripped guard refuses the next dispatch.

## 5. Production-readiness checklist

- security: read-only over the tree; no new write path, input or surface.
- perf / scale: one `render_unfenced` pass per tracked spec, linear in its lines. 2822 specs at
  `4e14dd8ab`; the supersede join already renders each one this way.
- error / empty / loading states: a spec whose only status line is fenced reads not live; an empty
  live population still refuses (`:1505-1508`); an unclosed fence blanks to the end, as every other
  fence-aware join reads it.
- observability: the population line `N live spec(s) · M terminal spec(s) not graded` (`:1831`)
  moves by the flipped specs, and AC5 names them.
- risks: a spec that wrote its status line inside a fence and nowhere else is dropped from grading.
  None does at `4e14dd8ab` (AC5).
- testing: AC1 to AC5 by a pass, and the three arms of §7 at the close.
- migration: none.
- user docs: N/A, no page under `help/` covers the spec-token checker; S2 is its own text.

## 6. Acceptance criteria

- **AC1** — When `python tools/check-spec-tokens.py` runs in the `deferred-fenced` scratch repo of §4,
  it exits 0 and prints `1 live spec(s) · 1 terminal spec(s) not graded`, with no line naming
  `nope.sh`.
  Red when: the fenced OPEN example below the DEFERRED header is read, as `LIVE.search` reads it at
  HEAD, and the run exits 1 with `2 live spec(s)` and the `nope.sh` hit.
- **AC2** — When `python tools/check-spec-tokens.py` runs in the `fence-above-header` scratch repo of
  §4, it exits 0 and prints `1 live spec(s) · 1 terminal spec(s) not graded`, with no line naming
  `nope.sh`.
  Red when: the first status line is read whether fenced or not, §8 F1's option A, which grades the
  fenced OPEN example above the header and exits 1.
- **AC3** — When `python tools/check-spec-tokens.py` runs in the `live-fenced-closed` scratch repo of
  §4, it exits 1, prints `not tracked by git ls-files` for `nope.sh`, and prints `1 live spec(s)`.
  Red when: a fenced CLOSED example freezes the OPEN spec, so the run refuses an empty population
  instead of naming the hit.
- **AC4** — When `grep -n 'check_live_header\|LIVE.search' tools/check-spec-tokens.py` runs, it prints
  the definition, the call in `main`, and the docstring and comment lines stating the rule, and no
  `LIVE.search`; and
  `grep -c 'check_live_header' memory/map/generated/symbols.json` prints at least 1.
  Red when: the population still reads the whole text, the docstring keeps the old rule, or the
  symbol map is not regenerated.
- **AC5** — When the §4 "### The measure" probe runs from the repo root at the pass tip, it prints the
  tracked spec count and a list holding
  `memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-12.md` and no other spec.
  Red when: the list is empty, which means the header read still grades the fenced example; or it
  names a spec whose header and whole-text reads should agree.
  figure: PINNED at `4e14dd8ab`, 2822 specs, 37 live under the whole-text read and 36 under the
  header read, one flip; the list is DERIVED at the pass tip, and a spec changing status or gaining
  a fenced example since then moves it.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `memory-hygiene self-test` · `build-index selftest` · `policy fixtures` · `recall floor` · `recall floor arms` · `memory hygiene`

The three guarded legs `tools/check-spec-tokens.py` trips are `memory-hygiene self-test`,
`build-index selftest` and `policy fixtures`; `memory/map/generated/symbols.json` trips
`recall floor` and `recall floor arms`. `check-spec-tokens.py --legs-for` printed every other tripped
leg as a broad guard, which the guards join excludes.

New arm: tools/check-spec-tokens.test.sh · covers AC1 · the `deferred-fenced` plant, red against the checker with `LIVE.search` restored at `:1501` · FLOOR_ASSERTIONS 215 to 218
New arm: tools/check-spec-tokens.test.sh · covers AC2 · the `fence-above-header` plant, red against a first-status-line read that ignores fences · FLOOR_ASSERTIONS 215 to 218
New arm: tools/check-spec-tokens.test.sh · covers AC3 · the `live-fenced-closed` plant, red against a read that takes a fenced status line as the header · FLOOR_ASSERTIONS 215 to 218

## 8. Open questions

- **F1 — Which status line is the header: the first `**Status:**` line of the text, or the first
  one outside any fenced block?** Options: (A) the first status line, fenced or not, the reading
  `drift_report.py:559` and `deviation_join.py:455-461` already use; (B) the first status line outside
  a fenced block, through `render_unfenced`. The tree does not decide it: §4's measure gives both
  the same 36 live specs over 2822, and they differ on no tracked spec. So the M3 rule decides. (A)
  reads a fenced example placed above the header, which the brief's "never from a fenced example"
  refuses and which AC2's plant stages. (B) agrees with the format's own placement, a header within
  the first five unfenced lines (`memory/TEMPLATE-SPEC.md:55`), and with the units table's read of
  unfenced lines (`gen_build_index.py:510-512`). Neither trips a veto. RESOLVED (agent, 2026-11-03,
  delegated): B, the more feature-rich option, tie-broken by reuse of `render_unfenced`, by
  `2026-11-03-prompt-PLAY-dOrderedCharter-63-spec-brief`. The loser's test is AC2: under (A) the
  `fence-above-header` plant exits 1 with `2 live spec(s)`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, by `2026-11-03-prompt-PLAY-dOrderedCharter-63-spec-brief`, every
  line re-read at HEAD `4e14dd8ab`.

## 10. Reuse audit

The seam extended is the checker's own `render_unfenced` (`tools/check-spec-tokens.py:1172-1188`),
which the supersede and claims joins already read through; `LIVE` (`:356`) is kept as the token set
and is matched against the header line only. `python tools/codebase-map/reuse_lookup.py "read a spec's status header outside fenced blocks"`
ranked general readers, `read_text`, `read`, `parse_spec_h1` and `read_spec_revisions`, none of which
reads a status line, so no ranked seam fits the read itself. The tree's two header readers that do
read one were weighed in §4 "### Alternatives rejected" and §8 F1: `parse_spec_text`
(`tools/memory-tree/gen_build_index.py:495`) and `tree_lib.unfenced_lines`
(`tools/memory-tree/tree_lib.py:149`), the latter reached only through the kit and duplicating
`render_unfenced` here. The recall query returned ask TOOL-dGatedProse-11, the DEFERRED whitelist
question this unit leaves alone (§3), and the run log's line naming this defect
(`memory/builds/dOrderedCharter/RUN.md:90`). Where the brief and the source disagree: none found;
the brief's `:356` and `:110` citations hold at HEAD.

Recall terms used: `python tools/memory-recall/query.py "how does the spec-token checker decide which specs are live and graded" --terms "LIVE status header DEFERRED fenced unfenced render_unfenced parse_spec_text terminal frozen spec-tokens population"`
