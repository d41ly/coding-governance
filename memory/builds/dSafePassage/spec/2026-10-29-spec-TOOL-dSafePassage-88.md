# TOOL-dSafePassage-88 — a renamed row whose new destination is its own path lands in place, so `update` carries a target across gov's tool-root move

**Status:** DEFERRED · rev-1 · 2026-10-29 · node a · Tier-2 · base 0f46b69d · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-prompt-TOOL-dSafePassage-88-1-spec-writer.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-88-1-spec-writer.md) | journal | — |
| [2026-10-29-prompt-TOOL-dSafePassage-88-2-spec-writer.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-88-2-spec-writer.md) | journal | — |
| [2026-10-29-prompt-TOOL-dSafePassage-88-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-88-spec-brief.md) | research | TOOL-dSafePassage-89 |
| [2026-10-29-prompt-TOOL-dSafePassage-88-third-stop-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-88-third-stop-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

This unit closes the third stop at a moved prefix, which TOOL-dSafePassage-89 §3 hands off. When gov
moves its tool root, every gov source is renamed, but a target keeps its own `prefix`. So `update`
resolves each renamed row back to the path it already holds. Its rename-destination guard then
finds the row's own file there, refuses the row, and holds back every kit. This unit lets a rename
whose destination is the row's own path land in place, keeps the guard for every other rename, and
adds a selftest arm that reds when the guard refuses the row's own file again.

## 2. Scope (IN)

- **S1** — The in-place rename. In `_cmd_update`'s `renamed` write arm (`tools/govkit/govkit.py:11061`),
  `in_place = new_dest == row["path"]` is set beside `new_src, new_dest` (`:11070`). The occupancy
  refusal (`:11101-11106`) runs only when `not in_place`. The move block, two staging lines and
  `git mv` (`:11159-11169`), runs only when `not in_place`. An in-place row's bytes are still decided
  and landed as they are now (`:11122-11151`, `:11175`), and its four fields are still rewritten
  (`:11195-11200`). It joins `changed`, not `renamed` (`:11201`), and prints an `in place` line in
  place of the `moved` line (`:11206-11207`). §4 "S1". Observed by AC1, AC2 and AC3.
- **S2** — The arm. The `DEPL-dCarriedReceipt-11` block of `tools/govkit/selftest.py` gains a
  `[dSP-88]` check after the occupied-destination checks (`:12990-13009`). It builds a scratch gov
  whose tool root is `pinned`, installs a target at `prefix = "pinned"`, moves gov's root to `moved`
  with an edit to the one source, and runs `update --write`. The check requires exit 0, no
  `ALREADY holds a file there`, gov's new bytes at the row's own path, the receipt row's `source`
  under `moved`, and nothing written under `moved` in the target. §4 "S2". Observed by AC4.

## 3. Non-goals (OUT)

- `resolve_renamed` (`govkit.py:9918-9960`) and `classify_row`'s rename branch (`:9054-9072`). Both
  answer correctly: the row is `renamed`, and its one destination is its own path (§4 "Which of the
  three").
- The walk's fixture. `fixtures/release-0/deploy.toml:8` keeps `prefix = "tools"`, and installing the
  target at the moved prefix meets the same refusal (§4 "Measured at writing time").
- The rollback snapshot's second path for a renamed row (`govkit.py:10744-10746`). For an in-place row
  it names the row's path twice, and the restore loop (`:8389-8420`) restores that one pre-run index
  entry twice. That is idempotent by reading, and was not measured.
- The `default-gained` note `update` prints at a moved tip, which reads gov's registry under the tip's
  tool root at the receipt's commit and says the default set there is unknown. It is a note, not a
  problem, and does not stop the walk.
- A green `upgrade-walk` row at `vendor/gov` and at the repo root. Only `scripts` was measured
  (§4 "Past this stop").

### Edges

- **consumes-from** `TOOL-dSafePassage-86` — `derive_release_engine`, without which AC2's moved-prefix
  walk stops at release-0's apply
- **consumes-from** `TOOL-dSafePassage-87` — S7's two roots, without which AC2's walk stops at the
  `engine-edit` plant
- **consumes-from** `TOOL-dSafePassage-89` — the uncached `derive_tool_root`, without which AC2's walk
  refuses at `read_steps` before the `up` case runs `update`

## 4. Design

Every cited line holds at `0f46b69d2`, and `tools/` there is byte-identical to the build head.

### The defect, at `0f46b69d2`

The walk's `up` case runs the tip clone's own `update --target <t> --to <tip> --write` in a child
(`tools/govkit/upgrade_walk.py:599`, `:478-495`). The target was installed at release-0 under the
prefix `fixtures/release-0/deploy.toml:8` spells, `tools`. The leg's move leaves that file alone:
`write_declarations` skips every file the move brought in that is not a render
(`tools/run-gates/foreign-prefix.gov.test.sh:519`). TOOL-dSafePassage-87's S7 resolves the plants
against the same `prefix`.

`update` diffs gov from the receipt's `gov_commit`, the pin, to the tip with rename detection
(`derive_rename_map`, `govkit.py:8917-8953`). The move makes every gov source a rename, from
`tools/<kit>/<file>` to `scripts/<kit>/<file>`. For a receipt row whose source is one of them,
`classify_row` asks the caller's resolver (`:9054`). `resolve_renamed` recomputes the new source's
destination through `resolve_entry` against the target's own answers (`:9882-9899`, `:9951-9960`).
The target's `prefix` is still `tools`, so the one destination is the row's own `path`, and the
verdict is `renamed` (`:9072`).

The write arm (`:11061`) then asks whether the target already holds `new_dest` (`:11101`). It does,
because `new_dest` is the row's own file. So `:11102-11106` refuses the row: `ALREADY holds a file
there`, and the remedy is to move or remove that file. Every refused row holds its kit back. Each
held path is a `tools` path no ordered plant names, so `check_walk_exit` (`upgrade_walk.py:305-323`)
returns problems and `run_up_walk` raises its `Stop` (`:631`).

### Which of the three

- **The target installed under `tools` while the tip declares the moved root.** That is the shape the
  `{prefix}` token exists for: a target's prefix is its own answer, and gov's tool root is gov's.
  `update` resolves the destination against the target's prefix, and the answer is right.
- **The walk's target installed at the moved prefix.** Measured: with `deploy.toml:8` set to
  `scripts` in the moved clone, `update` refused the same 159 rows. A source move is a rename whatever
  the target's prefix, and each destination still resolves to the row's own path.
- **`update` mis-resolving the target's own prefix.** It does not. The destination is correct. The
  fault is that the occupancy guard does not ask whether the occupant is the row itself. Its own
  message says the move "would be destroying another file's bytes", and when `new_dest` is the row's
  path there is no other file.

### Adopters meet it

An adopter pinned before gov moves its tool root, updating past the move with its own `prefix`
unchanged, takes this path for every row. Every kit is held back on every run. The refusal's remedy,
to move or remove the named file, would remove the adopter's own installed file. So `update` is wrong
for that adopter, and the fix is in `update`, not in the walk.

The guard fires on any rename whose recomputed destination is the row's own path. A source renamed
inside a `[[files]]` rule with one explicit `to` reaches it too, because `resolve_entry` answers the
rule's `to` and not the source's spelling. That case is reasoned from `resolve_renamed`, not measured.

### S1

At `govkit.py:11070`, after `new_src, new_dest = c["renamed_to"]`:

```python
            # TOOL-dSafePassage-88: the target's descriptor answers this row's own path, as it does for
            # every row when gov moves its tool root, so the file stays and only its source changes.
            in_place = new_dest == row["path"]
```

The containment check (`:11071-11080`) and the index read (`:11094-11100`) run as they do now. The
occupancy test at `:11101` becomes
`if not in_place and (new_dest in _at_dest or ndp.exists()):`. The byte decision (`:11122-11151`)
is unchanged. Its conflict order already says the file was left byte-identical at its old path, which
holds in place too.

The move block keeps `old_path` and `mv_err` (`:11157-11158`), and its `try`/`except` (`:11159-11169`)
moves one level in under `if not in_place:`. `land_through_index` (`:11175`) then lands the bytes at
`new_dest`, which is `old_path`, and reads the mode from `old_path`'s entry as it does now. The four
fields are rewritten as they are now (`:11195-11200`). At `:11201`:

```python
            if in_place:
                changed.append(new_dest)
            else:
                renamed.extend([old_path, new_dest])
```

So the closing count's `moved` stays a count of moved files, and an in-place row counts under `wrote`.
The destination line (`:11206-11207`) prints, for an in-place row,
`  in place         [<role>] <path> · source <new source> · bytes <arm>`. It ends in the byte arm, as
the `moved` line does, so `verdict_of`-style readers, which take a line ending in a path as a verdict
row (`selftest.py:10550-10555`), do not read it as one.

### S2: the arm

After the `[-11]` check `...and the row it refused is still at its old path, at its old vintage`
(`selftest.py:13006-13009`), and before the `mvfail` fixture (`:13011`). It reuses
`build_scratch_gov` and `build_target` (`:681`), `git` (`:583`), `settle` (`:587`), `read_bytes11`
(`:12092`), `GOVKIT`, `KIT_NAMES` and `_g11`'s registry:

```python
        # TOOL-dSafePassage-88: gov moves its tool root and the target keeps its prefix, so each renamed
        # row resolves to its own path and lands there, never refused as its own occupant.
        _g88 = build_scratch_gov(tmp / "rn-inplace-gov")
        _gk88 = _g88 / "pinned" / KIT_NAMES["govkit"]
        _gk88.mkdir(parents=True)
        for _f88 in ("govkit.py", "adopters.toml", "upgrade_steps.py"):
            shutil.copy2(GOVKIT.parent / _f88, _gk88 / _f88)
        shutil.copy2(_g11 / PFX / KIT_NAMES["govkit"] / "registry.toml", _gk88 / "registry.toml")
        (_g88 / "pinned" / "demo").mkdir()
        (_g88 / "pinned" / "demo" / "kit.toml").write_text(
            'id = "demo"\nhome = "demo"\nversion_from = { none = "fixture" }\n\n[check]\nnone = "a fixture kit"\n\n'
            '[[files]]\ninclude = "**"\nrole = "engine"\n\n[adopt]\nargv = []\nmutates_index = false\n',
            encoding="utf-8", newline="\n")
        (_g88 / "pinned" / "demo" / "keep.txt").write_text("one\ntwo\nthree\nfour\n", encoding="utf-8", newline="\n")
        git(_g88, "add", "-A")
        git(_g88, "commit", "-qm", "A")
        _t88 = build_target(tmp, 'gov_source = "local"\nprefix = "pinned"\nkits = ["demo"]\n', "rn-inplace-t")
        _ap88 = subprocess.run([sys.executable, str(_gk88 / "govkit.py"), "apply", "--target", str(_t88),
                                "--kits", "demo"], capture_output=True, text=True, encoding="utf-8", errors="replace")
        settle(_t88, "the install")
        git(_g88, "mv", "pinned", "moved")
        (_g88 / "moved" / "demo" / "keep.txt").write_text("one\ntwo\nthree\nFOUR\n", encoding="utf-8", newline="\n")
        git(_g88, "add", "-A")
        git(_g88, "commit", "-qm", "B")
        _up88 = subprocess.run([sys.executable, str(_g88 / "moved" / KIT_NAMES["govkit"] / "govkit.py"), "update",
                                "--target", str(_t88), "--write"],
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
        _row88 = [f.get("source") for f in json.loads((_t88 / ".governance" / "install.json").read_text(
            encoding="utf-8"))["files"] if f["path"] == "pinned/demo/keep.txt"]
        check("[dSP-88] a rename gov's tool-root move makes lands at the row's own path, under the new source",
              _ap88.returncode == 0 and _up88.returncode == 0
              and "ALREADY holds a file there" not in _up88.stdout
              and read_bytes11(_t88 / "pinned" / "demo" / "keep.txt") == b"one\ntwo\nthree\nFOUR\n"
              and _row88 == ["moved/demo/keep.txt"] and not (_t88 / "moved").exists(),
              f"apply {_ap88.returncode} update {_up88.returncode} {_row88} " + _up88.stdout[-1500:])
```

The roots are `pinned` and `moved`, so no literal spells a prefix the foreign-prefix leg moves gov
to, and the arm runs the same at every prefix. The engine copy is taken when the fixture is built,
as `build_rename_gov` takes it (`:12136-12146`), so a staged break reaches it. The existing `[-11]`
check at `:13001-13002` stays the arm that a rename onto an occupied different path is refused, and
S1 keeps it green: its destination, `renamed.txt`, is not its row's path.

### The probe

`p88_probe.py`, run from the repository root. Its one optional argument is the engine directory,
`tools/govkit` by default. It installs a target from a scratch gov at `pinned`, moves gov's root to
`moved` with an edit, and runs `update --write`. It then plants the adopter's own file at the path a
second rename resolves to, renames the source within `moved`, and runs `update --write` again.

```python
import json, pathlib, shutil, subprocess, sys, tempfile
eng = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "tools/govkit").resolve()
sys.path.insert(0, str(eng))
from fixture_target import build_scratch_gov, build_target
tmp = pathlib.Path(tempfile.mkdtemp(prefix="p88-"))
g = build_scratch_gov(tmp / "gov")
(g / "pinned" / "govkit").mkdir(parents=True)
for f in ("govkit.py", "adopters.toml", "upgrade_steps.py"):
    shutil.copy2(eng / f, g / "pinned" / "govkit" / f)
(g / "pinned" / "govkit" / "registry.toml").write_text(
    '[surface]\nglobs = ["{prefix}/*"]\n\n[selection]\ndefault = ["demo"]\n\n'
    '[[entry]]\nid = "demo"\ndescriptor = "{prefix}/demo/kit.toml"\n\n'
    '[[exempt]]\npath = "{prefix}/govkit"\nwhy = "the deployer itself"\n', encoding="utf-8", newline="\n")
(g / "pinned" / "demo").mkdir()
(g / "pinned" / "demo" / "kit.toml").write_text(
    'id = "demo"\nhome = "demo"\nversion_from = { none = "fixture" }\n\n[check]\nnone = "a fixture kit"\n\n'
    '[[files]]\ninclude = "**"\nrole = "engine"\n\n[adopt]\nargv = []\nmutates_index = false\n',
    encoding="utf-8", newline="\n")
(g / "pinned" / "demo" / "keep.txt").write_text("one\ntwo\nthree\nfour\n", encoding="utf-8", newline="\n")
def git(cwd, *a):
    return subprocess.run(["git", "-C", str(cwd), *a], capture_output=True, text=True, check=True).stdout
git(g, "add", "-A"); git(g, "-c", "user.email=t@e", "-c", "user.name=t", "commit", "-qm", "A")
t = build_target(tmp, 'gov_source = "local"\nprefix = "pinned"\nkits = ["demo"]\n')
def gk(root, *a):
    return subprocess.run([sys.executable, str(g / root / "govkit" / "govkit.py"), *a],
                          capture_output=True, text=True, encoding="utf-8", errors="replace")
ap = gk("pinned", "apply", "--target", str(t), "--kits", "demo")
print("apply exit", ap.returncode)
git(t, "add", "-A"); git(t, "-c", "user.email=t@e", "-c", "user.name=t", "commit", "-qm", "install")
git(g, "mv", "pinned", "moved")
(g / "moved" / "demo" / "keep.txt").write_text("one\ntwo\nthree\nFOUR\n", encoding="utf-8", newline="\n")
git(g, "add", "-A"); git(g, "-c", "user.email=t@e", "-c", "user.name=t", "commit", "-qm", "B")
up = gk("moved", "update", "--target", str(t), "--write")
row = [f for f in json.loads((t / ".governance/install.json").read_text(encoding="utf-8"))["files"]
       if f["path"] == "pinned/demo/keep.txt"]
print("update exit", up.returncode, "| refused in place:", "ALREADY holds a file there" in up.stdout,
      "| bytes:", (t / "pinned/demo/keep.txt").read_text(encoding="utf-8").split()[-1],
      "| source:", row[0].get("source") if row else None, "| moved dir in target:", (t / "moved").exists())
git(t, "add", "-A"); git(t, "-c", "user.email=t@e", "-c", "user.name=t", "commit", "-qm", "update", "--allow-empty")
(t / "pinned/demo/kept.txt").write_text("the adopter's own file\n", encoding="utf-8", newline="\n")
git(t, "add", "-A"); git(t, "-c", "user.email=t@e", "-c", "user.name=t", "commit", "-qm", "own file")
git(g, "mv", "moved/demo/keep.txt", "moved/demo/kept.txt")
git(g, "-c", "user.email=t@e", "-c", "user.name=t", "commit", "-qm", "C")
oc = gk("moved", "update", "--target", str(t), "--write")
print("occupied refused:", oc.returncode == 1 and "ALREADY holds a file there" in oc.stdout,
      "| own file kept:", (t / "pinned/demo/kept.txt").read_text(encoding="utf-8").startswith("the adopter"))
```

### Measured at writing time

These were measured on 2026-10-29 on node a. The moved clone was a `git clone --no-hardlinks` of
`0f46b69d2` under the temp root, checked out on a branch. `set_tool_root` and `write_declarations`
(`foreign-prefix.gov.test.sh:482-535`) were extracted with
`sed -n '/^set_tool_root() {/,/^# ---- ONE ROW/p'` and sourced with `TMPD`, `TROOT=tools` and
`PY=python` set. `set_tool_root scripts` re-spelled 227 declaration files and committed the move. Then
TOOL-dSafePassage-86's S1, -87's S7 and -89's S1 were staged as their specs state and committed. The
walk ran as `FOREIGN_PREFIX_PROBE=1 python scripts/govkit/upgrade_walk.py --case up`. `update`'s own
output was read by running the walk's `build_release_tree` and `run_child_walk` once, in process.

- **The moved walk, without S1.** It applied release-0 and the plants, and printed
  `pin 60d90cb71... · 3 step(s)`. It then printed
  `nothing measured: up · the walk to the tip did not return: exit 1 | a held path no ordered plant names:`
  followed by the target's `tools` paths, and exited 2.
- **`update`'s own output in that walk.** It printed `rename map: 407 gov source(s) moved` and a tally
  of `renamed 173`. 159 rows were refused with `ALREADY holds a file there`, each naming the row's own
  path as the destination. The other 14 `renamed` rows are `seed` rows, which `update` reports and
  never writes. 20 kits were held back, and the run ended `govkit: 179 problem(s)`, exit 1.
- **The same, with `deploy.toml:8` set to `scripts`.** 159 refusals, 20 kits held back,
  `govkit: 179 problem(s)`. Each destination was a `scripts` path, again the row's own.
- **The moved walk, S1 staged in the measurement shape.** Three lines
  `up · <step> · applied · witness ok`, for `govkit/receipt-schema-4`, `lib/python-floor-3.15` and
  `agent-cap/fanout-cap-to-agents-in-flight`, then `upgrade-walk: GREEN`, exit 0, in 262 s.
- **The probe, at `0f46b69d2`.** `update exit 1 | refused in place: True | bytes: four`, the source
  still under `pinned`, and `occupied refused: True | own file kept: True`. About 4 s.
- **The probe, S1 staged.** `update exit 0 | refused in place: False | bytes: FOUR`, the source under
  `moved`, no `moved` directory in the target, and `occupied refused: True | own file kept: True`.
- **The probe, with the occupancy test dropped altogether.** `occupied refused: False`.

The staged S1 differed from §4 "S1" in shape only: it skipped the move block by raising and catching a
local exception, not with an `if`, and it kept the `moved` line. The 262 s, 4 s, 407, 173, 159, 14,
20 and 179 figures are PINNED at that date on node a. S2's arm was not run inside the govkit
selftest. The probe runs the same steps.

### Past this stop

With S1 staged beside 86, 87 and 89, the walk's `up` case at `scripts` is GREEN and exits 0, so no
further stop was measured there. `vendor/gov` and the repo root were not run.

### Inventory

Minted: the local name `in_place`, the console line `in place`, the check label `[dSP-88]`, and the
scratch directories `rn-inplace-gov` and `rn-inplace-t`. No function, `Refusal` site, flag, conf key,
gate leg or receipt field. The refusal join's anchors do not move, because no refusal call site is
added or removed.

### Migration

None. An in-place row's receipt `path` is unchanged and its `source` is rewritten, as a moved row's
is now.

### Rollout

Live at landing, at order 16, after TOOL-dSafePassage-86, -87 and -89, which AC2's walk needs.
TOOL-dSafePassage-89 also edits `govkit.py` and `selftest.py`, so the builder re-reads each cited
line by content before editing.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Install the walk's target at the moved prefix.** Measured: the same 159 refusals (§4 "Measured at
  writing time"). It also leaves every adopter with the defect.
- **`resolve_renamed` answers None when the destination is the row's own path.** The row then falls
  to the grid at `t_state` absent and reads `withdrawn`. That is a report and an order, so no bytes
  land, and the receipt keeps a source gov no longer ships, so every later run withdraws it again.
- **Strip gov's tool root out of the rename map.** It covers the root move and not a rename inside a
  rule with one explicit `to`. The map is also one unscoped diff per run by design (`:8918-8934`).
- **Classify a same-path rename through the grid against the new source.** The grid's write arm
  rewrites `gov_oid`, `oid`, `sha256`, `commit` and `version` but not `source` (`:11053-11057`), so
  the next run would read the old source again.
- **Declare the walk's row red at a moved prefix.** It gates the instance, and the adopter keeps the
  defect.

## 5. Production-readiness checklist

- security: the occupancy guard still refuses every rename whose destination is not the row's own
  path (AC3). An in-place row writes only the path the receipt already claims, after the containment
  check (`govkit.py:11071-11080`) has run. No new write path, spawn or surface.
- perf / scale: an in-place row skips two staging lines and one `git mv`. The moved walk's `up` case
  measured 262 s with S1 staged.
- error / empty / loading states: a three-way conflict on an in-place row takes the existing conflict
  arm, whose order says nothing was moved and the file was left byte-identical. That is true in place.
- observability: the `in place` line names the row, its new source and its byte arm. The tally still
  counts the row as `renamed`.
- risks: a rolled-back kit restores an in-place row's one pre-run index entry twice (§3), which is
  idempotent by reading and not measured. The closing count's `moved` no longer counts in-place rows,
  which count under `wrote`.
- testing: §7's New arm and AC1 to AC4.
- migration: none.
- user docs: none. `grep -rln renamed help/` names only `help/step-gate.md`, whose line 4 is about a
  step whose installed file disappears. No page describes `update`'s rename lines or this refusal, so
  no page sentence changes.

## 6. Acceptance criteria

- **AC1** — When the probe of §4 "The probe" runs from the repository root with no argument, its
  second line reads `update exit 0 | refused in place: False | bytes: FOUR` and names its source
  under the `moved` root.
  Red when: the occupancy test still runs for an in-place row, so the line reads
  `update exit 1 | refused in place: True | bytes: four` and the source stays under `pinned`, as at
  `0f46b69d2`.
  cost: about 4 s.
  fixture: a scratch gov and target under the temp root. The tree holds none today.
- **AC2** — When `FOREIGN_PREFIX_PROBE=1 python upgrade_walk.py --case up` runs from the
  `scripts/govkit` directory of the moved clone of §4 "Measured at writing time", built from the build
  head with TOOL-dSafePassage-86, -87 and -89 landed, it prints `upgrade-walk: GREEN` and exits 0.
  Red when: the guard refuses the row's own file, so the run prints
  `nothing measured: up · the walk to the tip did not return: exit 1` and
  `a held path no ordered plant names:`, exit 2.
  cost: one clone of the repository, the leg's move, and the walk, about five minutes.
  fixture: the moved clone, built by the leg's own `set_tool_root` and `write_declarations`. The tree
  holds none today.
- **AC3** — When the probe of AC1 runs, its last line reads
  `occupied refused: True | own file kept: True`.
  Red when: the occupancy test is dropped for every rename rather than for the in-place one, so the
  line reads `occupied refused: False`.
  cost: inside AC1's run.
- **AC4** — When `git grep -n -F "[dSP-88]" -- tools/govkit/selftest.py` runs, it prints one line,
  the check's label inside the `DEPL-dCarriedReceipt-11` block.
  Red when: the arm is absent, so it prints nothing.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `upgrade-walk` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · the `[dSP-88]` check in the `DEPL-dCarriedReceipt-11` block, staged red by the occupancy test at `govkit.py:11101` kept unconditional, which refuses the row's own file and leaves gov's old bytes · none

The four `{prefix}/govkit/` legs and `policy fixtures` are the guard join's for the two files; their
other guards are broad. `upgrade-walk` runs the walk whose stop this closes. The foreign-prefix parity
leg is not on the line: only its `scripts` prefix was measured green (§4 "Past this stop"), and AC2
observes this unit's part of its `upgrade-walk` row directly.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-88-2-spec-writer.md` and its
  brief `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-88-third-stop-spec-brief.md`.
  The stop is the third at a moved prefix, which TOOL-dSafePassage-89's writer measured with 86, 87
  and 89 staged at `scripts` and handed off as external in 89 §3. A first candidate for this id, the
  CRLF checkout of a moved kit descriptor, was refused by 89's writer (89 §4 "The CRLF stop,
  re-measured"), and the id now names this stop. It was reproduced at the leg's own move in a clone of
  `0f46b69d2`, diagnosed as the occupancy guard refusing the row's own file, and S1 was staged and
  measured there (§4 "Measured at writing time").

## 10. Reuse audit

S1 changes `_cmd_update`'s existing `renamed` write arm (`tools/govkit/govkit.py:11061`) in place,
and keeps `resolve_renamed`, `land_through_index` and the conflict arm as they are. S2 extends the
`DEPL-dCarriedReceipt-11` block of `tools/govkit/selftest.py`, with `build_scratch_gov` and
`build_target` from `fixture_target.py`, `settle`, `read_bytes11` and `_g11`'s registry. No new seam.
`python tools/codebase-map/reuse_lookup.py "land a renamed row in place when gov's new source resolves to the row's own destination"`
ranked `resolve_entry` and `build_scratch_gov` as seams, beside name-stem matches (`rows`, `row`,
`resolve`, `resolve_kit_dir`) that do not decide a rename. The recall probe ranked
DEPL-dCarriedReceipt-11's backlog row and spec first, the unit that built the rename arm. Its spec
records the occupied-destination refusal as protecting another file's bytes, and no record decides a
destination that is the row's own path.

Recall terms used: `python tools/memory-recall/query.py "update refuses a renamed row whose new destination is its own path after gov moved its tool root" --terms "renamed rename map ALREADY holds destination resolve_renamed tool root prefix moved in place DEPL-dCarriedReceipt-11 HELD BACK update"`
