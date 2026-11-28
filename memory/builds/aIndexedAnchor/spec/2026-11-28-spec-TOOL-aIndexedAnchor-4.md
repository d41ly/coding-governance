# TOOL-aIndexedAnchor-4 — the attended lander's marker is a registered record

**Status:** CLOSED · rev-1 · 2026-11-28 · node a · Tier-1 · base 9dcc07a9 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-28-build-TOOL-aIndexedAnchor-1-agent-ledger.md](../build/2026-11-28-build-TOOL-aIndexedAnchor-1-agent-ledger.md) | log | TOOL-aIndexedAnchor-1 TOOL-aIndexedAnchor-2 |
| [2026-11-28-build-TOOL-aIndexedAnchor-4-acceptance-3.md](../build/2026-11-28-build-TOOL-aIndexedAnchor-4-acceptance-3.md) | acceptance | — |
| [2026-11-28-build-TOOL-aIndexedAnchor-4-override-1.md](../build/2026-11-28-build-TOOL-aIndexedAnchor-4-override-1.md) | override | — |
| [2026-11-28-prompt-TOOL-aIndexedAnchor-4-1-spec-writer.md](../prompts/2026-11-28-prompt-TOOL-aIndexedAnchor-4-1-spec-writer.md) | log | — |
| [2026-11-28-prompt-TOOL-aIndexedAnchor-4-2-builder.md](../prompts/2026-11-28-prompt-TOOL-aIndexedAnchor-4-2-builder.md) | log | — |
| [2026-11-28-prompt-TOOL-aIndexedAnchor-4-brief.md](../prompts/2026-11-28-prompt-TOOL-aIndexedAnchor-4-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-tree/record-kinds.toml` gains one witness row whose home is
`<git-common-dir>/push-main-active`. An attended landing from the primary tree then no longer reds
`record-kinds` on the lander's own marker, which was the leg's one unmatched pocket of 82.

## 2. Scope (IN)

- **S1** — One `[[record-kind]]` row, `lander-marker`, appended after the `session-registry` row
  of `tools/memory-tree/record-kinds.toml`, in the shape of the common-dir witness rows. Observed
  by AC1.
- **S2** — The `gen:record-kinds` region of `tools/memory-tree/HYGIENE.template.md` re-rendered
  by `record_kinds.py --write`, and the same region carried byte for byte into the dogfood copy
  `memory/HYGIENE.md`. Observed by AC2.

## 3. Non-goals (OUT)

- `tools/push-main.sh`, and where it writes its marker.
- The `record causes` red.
- Any other row of the table, the `gate-ledger` row's home list included.
- A purpose text. The row's purpose pends on the open ask TOOL-dTotalRecall-110, and that ask's
  `BACKLOG.md` row is not edited.
- A suite arm. The pocket arm and its `pocket-stray` and `pocket-registered` plants already exist.

## 4. Design

### The row

```toml
[[record-kind]]
name = "lander-marker"
tag = "record.lander-marker"
layer = "layer.flow"
home = ["<git-common-dir>/push-main-active"]
id-rule = ""
schema = { form = "generated", fields = [] }
writer = "push-main.sh"
readers = []
readers-none = "a cache or a mechanic is read by its own writer, never filled into a work order"
lifecycle = "out"
check = "record-kinds"
purpose = { pending = "TOOL-dTotalRecall-110" }
```

Each cell is derived, not chosen:

| Cell | Value | Read from |
|---|---|---|
| `home` | `<git-common-dir>/push-main-active` | `tools/push-main.sh@4e6124cf:216` sets `marker="$gd/push-main-active"` |
| `layer` | `layer.flow` | `tools/govkit/entries/push-main.kit.toml` declares `layer = "layer.flow"` |
| `schema.form` | `generated` | the marker is an empty file, `touch`ed at `tools/push-main.sh@4e6124cf:2144` and `:2357`; `request-records` and `session-registry`, the newest witness rows, use the same form |
| `readers-none`, `lifecycle`, `check` | as above | the `gate-ledger` row, `tools/memory-tree/record-kinds.toml@9eae1608:589` |
| `purpose` | pending TOOL-dTotalRecall-110 | every common-dir witness row pends there; under `memory.map-purpose` `review` (`.governance/policy.json`, the catalogue default) a pending id must be an open ask, and `memory/builds/dTotalRecall/BACKLOG.md` holds that ask open |

The pocket arm, `tools/memory-tree/record_kinds.py#check_pockets`, matches each top-level entry of
the common dir against the first segment of every `<git-common-dir>/` home glob, so the literal
`push-main-active` matches the marker and nothing else. The marker lives in
`git rev-parse --git-dir`, so a landing from a linked worktree writes it under
`<common dir>/worktrees/`, which `GIT_OWN` skips. The row matters only for the primary tree, which
is the case observed.

The builder hand-appends the row and then runs `record_kinds.py --write`, which re-renders the
template region. The region's count line moves from `57 kinds · 28 purposes pending` to
`58 kinds · 29 purposes pending`, DERIVED by `--write` from the registry. The region is then copied
into `memory/HYGIENE.md`, which carries it verbatim as fix 5600dabfc did.
`record_kinds.py new` is not used, because it writes `purpose.source = "owner"` and the owner gave
no purpose text.

### Files touched (estimate)

- `tools/memory-tree/record-kinds.toml`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`

### Alternatives rejected

- Adding `<git-common-dir>/push-main-active` to the `gate-ledger` row's home list: a non-goal, and
  `run-gates.sh` does not write the marker, so that row's `writer` would be false for it.
- A purpose text cited at `tools/push-main.sh:<line>`: the owner's open ask TOOL-dTotalRecall-110
  is where every witness row's purpose is answered, and one answered out of band splits that review.

## 5. Acceptance criteria

- **AC1** — When `python -c "import pathlib,subprocess,sys,tempfile,tomllib; sys.path.insert(0,'tools/memory-tree'); import record_kinds as rk; rows=tomllib.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))['record-kind']; d=tempfile.mkdtemp(); subprocess.run(['git','init','-q',d],check=True); pathlib.Path(d,'.git','push-main-active').touch(); l,r=rk.check_pockets(d,rows); print(chr(10).join(l+r))" tools/memory-tree/record-kinds.toml`
  runs at the repo root under the interpreter `tools/lib/resolve-python.sh` resolves, it prints
  `pocket · push-main-active · lander-marker` and `0 unmatched`, and no
  `pocket push-main-active: no row` red.
  Red when: the row is absent, so it prints `pocket · push-main-active · no row` and
  `1 unmatched`, observed 2026-11-28 over registry blob 9eae1608.
  fixture: the probe builds a fresh `git init` repo under the temp dir; the tree holds none.
- **AC2** — When `python tools/memory-tree/record_kinds.py --write` runs and then
  `git diff --exit-code -- tools/memory-tree/HYGIENE.template.md` runs, the diff exits 0. When
  `grep -c 'lander-marker' tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md` runs, it
  prints 1 for each file, and both files carry `58 kinds · 29 purposes pending`.
  Red when: the region is not re-rendered, or the dogfood copy is not carried, so the diff exits 1
  or a count prints 0.
  figure: 58 and 29 are DERIVED by `--write` from the registry; a row landing first moves both.

## 6. Gates

`record-kinds` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-28 · initial draft.

## 9. Reuse audit

The seam is the common-dir witness rows of `tools/memory-tree/record-kinds.toml`, which the pocket
arm's refusal names as the remedy: `gate-ledger`, `history-verdicts`, `health-logs`,
`request-records` and `session-registry`. The row copies their cells, and the pocket arm needs no
change. No existing seam fits a wider change, and none is made.

Recall terms used: record-kinds pocket common dir witness row push-main-active marker attended lander
