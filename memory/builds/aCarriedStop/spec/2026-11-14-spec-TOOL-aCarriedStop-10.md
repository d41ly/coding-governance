# TOOL-aCarriedStop-10 — the chain-packet door reaches the memory-tree kit through `resolve_kit_dir`, so the install-prefix leg reads no spelled kit path in it

**Status:** CLOSED · rev-1 · 2026-11-14 · node a · Tier-1 · base 0578adb7 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-13-build-TOOL-aCarriedStop-1-agent-ledger.md](../build/2026-11-13-build-TOOL-aCarriedStop-1-agent-ledger.md) | journal | TOOL-aCarriedStop-1 TOOL-aCarriedStop-2 TOOL-aCarriedStop-3 TOOL-aCarriedStop-9 |
| [2026-11-14-build-TOOL-aCarriedStop-10-1-acceptance-ledger.md](../build/2026-11-14-build-TOOL-aCarriedStop-10-1-acceptance-ledger.md) | journal | — |
| [2026-11-14-prompt-TOOL-aCarriedStop-10-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aCarriedStop-10-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aCarriedStop-10-2-builder.md](../prompts/2026-11-14-prompt-TOOL-aCarriedStop-10-2-builder.md) | journal | — |
| [2026-11-14-prompt-TOOL-aCarriedStop-10-brief.md](../prompts/2026-11-14-prompt-TOOL-aCarriedStop-10-brief.md) | research | — |
| [2026-11-14-prompt-TOOL-aCarriedStop-10-build-brief.md](../prompts/2026-11-14-prompt-TOOL-aCarriedStop-10-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The leg `install-prefix (shipped surface)` exits 1 on this build's tree, and on origin/main at
`0578adb73`, over three spelled `"memory-tree"` path segments: two in `tools/chain-packet.py` and one
in `tools/chain-packet.test.sh`. This unit makes the door find the kit through the canonical
`resolve_kit_dir` block and the suite load `tree_lib` through the door's answer. The leg then exits 0,
so the close's bar and the push bar can land this build on the owner's order of 2026-11-14: "raise
the routed-commits ceiling and land it".

## 2. Scope (IN)

- **S1** — `tools/chain-packet.py` carries the `resolve_kit_dir` block byte-identical to
  `tools/lib/resolve_kit_dir.py`, and sets a module-level `KIT_DIR` from it, `None` when the kit does
  not resolve. `main` tests `KIT_DIR` and loads `KIT_DIR / "tree_lib.py"`, and spells no kit segment.
  Observed by AC1, AC3, AC4 and AC5.
- **S2** — `tools/chain-packet.test.sh`'s CP8 probe loads `tree_lib` from `door.KIT_DIR`, and spells
  no kit segment. Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- What the door reads, batches or prints, beyond how it finds the kit. Both reason strings stay
  `tree_lib.py is not beside this script`, byte for byte, so the `shortcuts off` line is unchanged.
- `tools/check-install-prefix.sh`, its predicate, and any other file's kit spellings.
- The suite's arms, their count and their assertions. CP8 keeps its one assertion.
- Any kit version or adopter release. Both files are `[[exempt]]` rows of the registry
  (`tools/govkit/registry.toml@7738d2173931:263-274`), so no adopter receives them.
- Any help page. No page under `help/` names the door (grep over `help/`, 2026-11-14).
- Any path under `memory/builds/aBatchedPacket/` or `memory/builds/dDeclaredLoop/`.

## 4. Design

### Evidence

Read at `1f732d9ba`. Every file cited here has the same blob at the base `0578adb7`.

- The three hits are `tools/chain-packet.py@dc026a49e863:239`, `:245` and
  `tools/chain-packet.test.sh@d3447869774f:405`, each a quoted kit segment joined by `/`, which is the
  checker's rule 4 (`tools/check-install-prefix.sh@401a476dfb69:477-490`).
- A kit name passed as the first argument of `resolve_kit_dir(` is no hit. Rule 4's `/` branch needs a
  `/` beside the quoted segment, and its comma branch needs a quoted literal segment before it inside
  an open `join(`, `joinpath(` or `Path(` call (`:479-489`, `JOINCALL` at `:409`). Rule 3 needs a
  `<kit>/` literal (`:465-476`). `tools/check-spec-tokens.py@42905ba56b3e:496` already calls
  `resolve_kit_dir("memory-tree", "design_lib.py", HERE)`, and the main loop's run at `0578adb73`
  listed only the door's three lines.
- The resolver tries a receipt row, then `<here>/memory-tree`, then `<here>/../memory-tree`, and
  raises `LookupError` otherwise (`tools/lib/resolve_kit_dir.py@00b26e9490f0:17-54`). In this tree
  the receipt holds a row for the kit's `tree_lib.py` (`.governance/install.json@8a31de0da629:416-419`),
  so `KIT_DIR` is the same directory the spelled path named.
- The parity row `resolve_kit_dir` grades every tracked `*.py` carrying the block's opening marker
  (`tools/lib/resolve-python.test.sh@4b2fb1fb8c49:355`, population grep at `:429`). The door joins that
  population by carrying the block, with no table edit.
- The suite's probe loads the door as a module (`tools/chain-packet.test.sh@d3447869774f:388-390`),
  so `door.KIT_DIR` exists by the time line 405 runs.

### The change

In `tools/chain-packet.py`, after `HERE` (line 75):

```python
# >>> resolve_kit_dir — ... the canonical block, copied byte for byte ...
# <<< resolve_kit_dir
# The memory-tree kit is RESOLVED, never spelled (TOOL-aCarriedStop-10); None when it does not resolve.
try:
    KIT_DIR = resolve_kit_dir("memory-tree", "tree_lib.py", HERE)
except LookupError:
    KIT_DIR = None
```

In `main`, line 239 becomes `if KIT_DIR is None:` and line 245 loads
`load_module("tree_lib", KIT_DIR / "tree_lib.py")`. The two `reasons.append` lines stay as they are.
The docstring's fallback paragraph (line 35) says `tree_lib.py` not found by `resolve_kit_dir`
instead of not beside this script. No comment or docstring may write the kit name followed by `/`.

In `tools/chain-packet.test.sh`, line 405 becomes
`tree_lib = door.load_module("tree_lib", door.KIT_DIR / "tree_lib.py")`.

### What this does not check

- The printed reason says the kit is not beside the script when it resolved nowhere, the receipt
  included. The text is kept by the non-goal, not because it names every place looked.
- A forged receipt row chooses the `tree_lib.py` the door loads, as the canonical's docstring states
  for every caller that loads code from its answer.
- The door now finds a kit one folder up or through the receipt, where it used to turn the shortcuts
  off. No arm grades those two layouts for the door; the resolver's own rows grade them.
- Whether the checker's rule 4 would see a kit name moved into a variable. Its header names that
  blind spot, and this unit does not use it.

### Alternatives rejected

- A module constant holding the kit name, joined at run time. It passes the checker through its
  stated blind spot and still guesses the layout, which is the class the ban exists for.
- An import of `tools/lib/resolve_kit_dir.py`. The kit convention carries the block inline, and the
  parity row grades inline copies only.

### Files touched (estimate)

- `tools/chain-packet.py`
- `tools/chain-packet.test.sh`

## 5. Acceptance criteria

All commands run from the worktree root in Git Bash. AC1 and AC2 are the main loop's, after the pass
commit. AC3 to AC5 are the builder's, before the commit.

- **AC1** — When the main loop runs `bash tools/check-install-prefix.sh` at the pass commit, it exits 0
  and lists no line of `tools/chain-packet.py` or of the door's suite beside it.
  Red when: S1 or S2 leaves a spelled segment, and the checker names it as `<path>:<line>`.
  permission: the command is the `install-prefix (shipped surface)` leg's argv, and the role gate
  refuses it to `gov-builder`.
  figure: PINNED. That the door's three lines were the only hits is the main loop's run at `0578adb73`.
- **AC2** — When the main loop runs the same checker in a scratch clone detached at the pass
  commit's parent, it lists `tools/chain-packet.py:239`, `tools/chain-packet.py:245` and
  `tools/chain-packet.test.sh:405`, and exits 1.
  Red when: the clone is detached at the pass commit itself, or the checker no longer reads a quoted
  kit segment joined by `/`, and it exits 0.
  permission: as AC1.
  figure: PINNED. The line numbers are a grep for `"memory-tree"` over the two files at `1f732d9ba`.

  ```bash
  S=$(mktemp -d) && git clone -q . "$S/c" && git -C "$S/c" checkout -q --detach HEAD^
  (cd "$S/c" && bash tools/check-install-prefix.sh); echo "rc=$?"
  ```

- **AC3** — When `grep -c '"memory-tree"' tools/chain-packet.test.sh` runs it prints `0`, and
  `grep -n '"memory-tree"' tools/chain-packet.py` prints one line, the `resolve_kit_dir` call. When
  the block below runs it prints nothing and exits 0.
  Red when: a spelled segment survives, or the inline block differs from the canonical, so `diff`
  prints the drifted lines and exits 1.

  ```bash
  blk() { awk '/^# >>> resolve_kit_dir/,/^# <<< resolve_kit_dir/' "$1" | tr -d '\r'; }
  diff <(blk tools/lib/resolve_kit_dir.py) <(blk tools/chain-packet.py)
  ```

- **AC4** — When the probe `python -c "import importlib.util as u; s = u.spec_from_file_location('door', 'tools/chain-packet.py'); m = u.module_from_spec(s); s.loader.exec_module(m); print(m.KIT_DIR.relative_to(m.HERE.parent).as_posix())"`
  runs, it prints `tools/memory-tree`.
  Red when: the call names the wrong home or anchor, so `KIT_DIR` is `None` and the probe raises
  `AttributeError`.
- **AC5** — When the door runs alone in a scratch folder with no kit beside it or one folder up and
  no `.git` above it, over a stub instrument, by the block below, its stderr is the one line
  `chain-packet: shortcuts off, running the instrument as it stands — packet: blob 6bcb6f4b0b1e, read against cab3bff165a1; carries: no file; schedule: no file; tree_lib.py is not beside this script`,
  its stdout is `stub ran ['--check', 'x']`, and it exits 1.
  Red when: the `LookupError` escapes at import, so the door prints a traceback and runs nothing.
  fixture: built by the block, under the session's temp folder, which has no `.git` above it.
  figure: PINNED. The parent's door printed these exact lines on this fixture, run by this writer at
  `1f732d9ba`; the stub's blob follows from its bytes.

  ```bash
  S=$(mktemp -d) && mkdir -p "$S/door" "$S/repo/memory/builds/dClosedLoop/build"
  cp tools/chain-packet.py "$S/door/"
  printf 'import sys\nprint("stub ran", sys.argv[1:])\nsys.exit(1)\n' \
    > "$S/repo/memory/builds/dClosedLoop/build/2026-01-01-build-x-1-packet.py"
  (cd "$S/repo" && python "$S/door/chain-packet.py" --check x); echo "rc=$?"
  ```

## 6. Gates

`install-prefix (shipped surface)` · `chain-packet self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `foreign-prefix parity (every self-test at three prefixes)` · `spec tokens (a spec's own names resolve)`

`python tools/check-spec-tokens.py --legs-for` over the two files touched, run 2026-11-14 at
`1f732d9ba`, names only legs under the broad `tools/` guard. The five above read this change:
`install-prefix (shipped surface)` is AC1; `chain-packet self-test` re-runs CP8 through the edited
line 405 and CP1 through the door's fallback; the resolver leg's parity row grades the new inline
block as AC3 does; and the foreign-prefix leg runs the door's suite at three prefixes, where the
resolver's probe now finds the kit. No arm is added or moved.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-14 · initial draft from the unit brief `2026-11-14-prompt-TOOL-aCarriedStop-10-brief`,
  grounded at `1f732d9ba`, whose cited files match origin/main `0578adb73`.

## 9. Reuse audit

The seam is `tools/lib/resolve_kit_dir.py#resolve_kit_dir`, carried inline as
`tools/check-spec-tokens.py` carries it for the same kit, with `TOOL-dMindYourWords-24` the precedent
for moving a consumer onto it. Nothing is built.
`python tools/codebase-map/reuse_lookup.py "load a sibling kit module by its resolved directory instead of a spelled kit path"`
ranked `resolve_kit_dir` second, a SEAM with 111 installs. The handoff named `write_chain_round`,
`derive_chain_verdict` and `check_chain_dispatch` in `tools/unattended/unattended.sh` as reuse. They
write and read the spec-audit chain record of units 1 to 3 and find no kit, so they do not fit this
unit.

Recall terms used: `python tools/memory-recall/query.py "how does a tool reach a sibling kit without spelling its kit path" --terms "resolve_kit_dir install-prefix kit path spelled segment tree_lib chain-packet door sibling receipt probe"`
