# TOOL-dSafePassage-89 — the tool root is read from the tree on every call, so `read_steps` finds the registry at a moved tip

**Status:** DEFERRED · rev-1 · 2026-10-29 · node a · Tier-2 · base b634d60e · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

This unit closes the second stop TOOL-dSafePassage-87's writer measured past the plants at a moved
prefix (87 §4 "Past the plants, measured"). `derive_tool_root` is memoised on its `root` argument,
and the upgrade walk asks it about one clone twice: once at the pin, which holds `tools`, and once at
the tip, which holds the moved root. The memo gives the second call the first call's answer. So
`read_steps` looks for the registry under `tools` at a tip that has none, and refuses with exit 1.
This unit makes the function read its tree on every call, and adds a selftest arm that reds when
the memo returns.

## 2. Scope (IN)

- **S1** — `derive_tool_root` (`tools/govkit/govkit.py:191`) becomes a plain function, without the
  `@functools.lru_cache(maxsize=None)` line at `:190`. Each call then globs the `root` it is handed
  (`:205-206`). Its docstring (`:192-199`) gains one sentence: the answer is not memoised, because a
  caller may move the tree under one root between two calls, as the upgrade walk's clone does
  (TOOL-dSafePassage-89). §4 "S1". Observed by AC1, AC2 and AC3.
- **S2** — The arm. `check_upgrade_steps` (`tools/govkit/selftest.py:2916`) gains a `[dSP-89]` check
  after its last check (`:3317-3318`). The check lays out a scratch tree holding a registry under one
  tool root, and reads `steps.read_registry_at(t, None)`. It then renames that root's directory and
  reads again. The check requires each read to name the root the tree held at that moment, with no
  refusal. §4 "S2". Observed by AC4.

## 3. Non-goals (OUT)

- The first stop of the brief, the moved kit descriptor checking out CRLF. That stop does not occur
  at the foreign-prefix leg's own move, which re-spells `.gitattributes:222` with the tool root
  (§4 "The CRLF stop, re-measured"). No unit closes it, and the brief's first item is refused.
- The walk clone's `core.eol`. `build_release_tree` pins `core.autocrlf=false` and leaves `core.eol`
  at git's native default (`tools/govkit/upgrade_walk.py:197`). So on Windows a text path with no eol
  pin checks out CRLF in the clone. The one byte-level edit the walk makes in the clone,
  `withdraw-one`, reads a pinned path at every prefix the leg moves to (§4), so this unit leaves it.
- The other three memos in the kit, `read_tree_modes` (`govkit.py:6703`), `read_git_dir`
  (`upgrade_steps.py:1102`) and `read_shipped_survivors` (`tools/govkit/step_gate.py:258`). Each is
  keyed by a sha or documents its ceiling in a `ponytail:` note, and none was measured stale.
- `upgrade_walk.py`. Its three calls (`:124`, `:207`, `:225`) keep their order and their answers.
- A green `upgrade-walk` row in the foreign-prefix parity leg. With TOOL-dSafePassage-86, -87 and this
  unit staged, the walk at `scripts` reads its steps and then stops in the `up` case (the hands-off
  below).

### Edges

- **consumes-from** `TOOL-dSafePassage-86` — `derive_release_engine`, without which AC2's moved-prefix
  walk stops at release-0's apply and never reaches `read_steps`
- **consumes-from** `TOOL-dSafePassage-87` — S7's two roots, without which AC2's walk stops at the
  `engine-edit` plant before the clone moves to its tip
- **hands-off** external — the third stop at a moved prefix, measured on 2026-10-29 with all three
  units staged at `scripts`. The `up` case's walk to the tip exits 1, holding back every kit and
  naming each installed file under the target's `tools` as a held path no ordered plant names. It
  was not diagnosed here, and the build's coordinator promotes it.

## 4. Design

Every cited line holds at `b634d60e5`.

### The defect, at `b634d60e5`

`derive_tool_root` (`govkit.py:190-211`) is decorated with `@functools.lru_cache(maxsize=None)`. For
a root other than gov's own checkout (`:201-204`), it globs that root for its one
`govkit/registry.toml` (`:205-206`) and returns the directory above it.

`build_release_tree` checks its clone out at the pin (`upgrade_walk.py:198`) and calls
`gk.derive_tool_root(clone)` there (`:207`, `:225`). The pin holds `tools/govkit/registry.toml`, so
the memo stores `tools` under the key `clone`. At `:234` the clone checks out the tip, whose tool root
is the moved one. `main` then calls `us.read_steps(ctx["clone"], ...)` (`:1095`). That reaches
`read_registry_at` (`upgrade_steps.py:816`), which calls `gk.derive_tool_root(root)` with the same
path (`:755`). The memo answers `tools`, `read_file_at` finds no such blob at the tip, and `:759-760`
raises `Refusal`. That is not a `Stop`, so it leaves `main` as a traceback, exit 1.

The walk and the reader share one memo. `load_engine` imports `govkit` and returns its
`upgrade_steps` (`upgrade_walk.py:88-93`). `load_govkit` returns the `govkit` module already in
`sys.modules` when its file is this kit's (`upgrade_steps.py:2668-2683`). At gov's own prefix the pin
and the tip both hold `tools`, so the stale answer is the right one and the leg is green there.

No record says why the function is memoised. Commit `f6f41cc32` (TOOL-aRepatriatedFork-29) added the
decorator with the function, and neither its message nor its spec gives a reason. The kit's other
three memos each state why their key is sound.

### S1

`govkit.py:190` is not carried into the edit, and `:191` reads `def derive_tool_root(...)` as it does
now. The docstring's new sentence follows its refusal sentence (`:197-198`). `functools` stays
imported for `read_tree_modes` (`:6703`). Every caller keeps its call: `shims.py:71` and `:324`,
`upgrade_steps.py:755`, `:1015` and `:1471`, the three walk calls, and the twelve calls on eleven lines of `govkit.py`.
Each now reads the tree as it stands.

### S2: the arm

After the `[dSP-1 AC5]` check at `selftest.py:3317-3318`, reusing `steps` (`:3072`), `read_refusal`
(`:3074-3079`) and `gkn`:

```python
    # TOOL-dSafePassage-89: one root whose tool root moves between two reads reads the moved registry.
    t89 = tmp / "dsp89"
    (t89 / "pinned" / gkn).mkdir(parents=True)
    (t89 / "pinned" / gkn / "registry.toml").write_text("", encoding="utf-8")
    got89 = [steps.read_registry_at(t89, None)[:2]]
    (t89 / "pinned").rename(t89 / "moved")
    msg89 = read_refusal(lambda: got89.append(steps.read_registry_at(t89, None)[:2]))
    check("[dSP-89] a root whose tool root moved between two reads reads the moved registry",
          got89 == [("pinned", f"pinned/{gkn}/registry.toml"), ("moved", f"moved/{gkn}/registry.toml")]
          and not msg89, f"{got89} {msg89}")
```

The two roots are named `pinned` and `moved`, so no literal in the check spells a prefix the
foreign-prefix leg moves gov to. `read_registry_at` with `sha` None reads the working tree
(`upgrade_steps.py:731-733`), so the check needs no git. An empty registry parses to no rows
(`:738-747`).

### The probe

`root_probe.py`, run from the repository root:

```python
import pathlib, sys, tempfile
sys.path.insert(0, "tools/govkit")
import govkit as gk
us = gk.upgrade_steps
t = pathlib.Path(tempfile.mkdtemp(prefix="p89-"))
(t / "tools" / "govkit").mkdir(parents=True)
(t / "tools" / "govkit" / "registry.toml").write_text("", encoding="utf-8")
for when in ("before the move", "after the move"):
    try:
        print(when, "->", us.read_registry_at(t, None)[:2])
    except us.Refusal as e:
        print(when, "-> refused:", str(e)[:60])
    if when == "before the move":
        (t / "tools").rename(t / "scripts")
```

### Measured at writing time

These were measured on 2026-10-29 in a `git clone --no-hardlinks` of `b634d60e5` under the temp root,
checked out on a branch as the leg does. The move ran through the leg's own functions.
`set_tool_root` and `write_declarations` (`tools/run-gates/foreign-prefix.gov.test.sh:482-535`) were
extracted with `sed -n '/^set_tool_root() {/,/^# ---- ONE ROW/p'` and sourced with `TMPD`,
`TROOT=tools` and `PY=python` set, and `set_tool_root scripts` committed the move. It re-spelled 227
declaration files. TOOL-dSafePassage-86's S1 and -87's S7 were staged and committed on top. The walk
ran as `FOREIGN_PREFIX_PROBE=1 python scripts/govkit/upgrade_walk.py --case up`.

| Observation | Memo kept | S1 staged |
|---|---|---|
| `root_probe.py`, at the build head | `after the move -> refused: tools/govkit/registry.toml: no registry at the working tree` | `after the move -> ('scripts', 'scripts/govkit/registry.toml')` |
| the moved walk | release-0 applied, plants applied, then a traceback ending `upgrade_steps.Refusal: tools/govkit/registry.toml: no registry at 4170f6c4`, exit 1 | `pin 60d90cb71... · 3 step(s)`, then exit 2 on the §3 hands-off |
| `derive_tool_root` calls in the walk's own process | — | 5, 17 ms in total |
| one uncached call | — | 0.14 ms on gov's own tree, 3.9 ms on a clone |

The 0.14 ms, 3.9 ms, 5-call and 17 ms figures are PINNED at that date on node a.

### The CRLF stop, re-measured

87's writer moved with a bare `git mv tools scripts`, which re-spells nothing, so
`.gitattributes:222` still read `tools/*/kit.toml`. The leg's `write_declarations` re-spells every
tracked text file outside the record corpus. In the clone above, `.gitattributes:222` read
`scripts/*/kit.toml text eol=lf`, and `git check-attr eol -- scripts/hooks/kit.toml` answered `lf`.
The walk applied `withdraw-one` and reached `read_steps`. The leg's other two prefixes re-spell the pin
to `vendor/gov/*/kit.toml` and `*/kit.toml` (`foreign-prefix.gov.test.sh:651`). In a scratch repository
`git check-attr` answered `lf` for the hooks descriptor under each.

Adopters do not meet the stop. An adopter receives `{prefix}/hooks/kit.toml` (`tools/hooks/kit.toml:38-41`),
but its `.gitattributes` holds govkit's generated `lf_pin` block (`govkit.py:5629-5643`,
`:5670-5691`), never gov's own file. And `withdraw-one` is a `[[gov_plant]]`, an edit to gov's clone
that no adopter path makes. So neither the walk's clone setup nor the pin is at fault, and no unit
closes the stop.

### Inventory

Minted: the check label `[dSP-89]` and its scratch directory `dsp89`. No function, `Refusal` site,
flag, conf key, gate leg or receipt field.

### Migration

None. No stored shape changes.

### Rollout

Live at landing, at order 16, after TOOL-dSafePassage-86 and -87, which AC2's walk needs.
TOOL-dSafePassage-87 also edits `check_upgrade_steps`, so the builder re-reads each cited line by
content before editing.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Clear the memo in `build_release_tree` after the checkout to the tip (`:234`).** It closes the
  walk's instance and keeps the memo. Any later caller that moves a tree under one root meets the same
  stale answer, and the arm would then have to sit in the walk, because govkit's own function would
  still be wrong. That gates the instance, not the class.
- **Key the memo on something that changes with the layout.** The function reads the working tree, not
  a commit, so no key short of the glob's own result is sound. An uncached call costs 3.9 ms on a
  clone.
- **Read the registry's tool root through git at `sha` inside `read_registry_at`.** It changes that
  reader's contract for the working-tree case, and leaves the memo stale for the other callers.
- **A grader in `check_graders`, as TOOL-dSafePassage-86 adds.** The defect is govkit's, so its arm
  sits in govkit's selftest, which the foreign-prefix leg also runs at every prefix.

## 5. Production-readiness checklist

- security: no new write path, spawn or surface. The function reads the directory it read before.
- perf / scale: an uncached call globs the root at three depths, measured at 0.14 ms on gov's own
  tree and 3.9 ms on a clone. The walk's own process makes 5 calls, 17 ms in total. Call counts in
  govkit's other runs were not measured, and most of those pass gov's own root.
- error / empty / loading states: a root with no registry, or more than one, refuses as it does now
  (`govkit.py:207-209`), on every call rather than once.
- observability: the `[dSP-89]` check prints its two reads on a red.
- risks: a caller that relied on the memo to keep a pin-time answer after a move would now see the
  tip's answer. The walk's calls at `:207` and `:225` run at the pin, and TOOL-dSafePassage-86's
  `derive_release_engine` runs there too.
- testing: §7's New arm and AC1 to AC4.
- migration: none.
- user docs: none. No command, flag, message or page sentence changes.

## 6. Acceptance criteria

- **AC1** — When §4 "The probe", `python <scratch>/root_probe.py`, runs from the repository root, its
  first line reads `before the move -> ('tools',` and its second reads `after the move -> ('scripts',`.
  Red when: the memo is kept, so the second line reads `after the move -> refused:` and names
  `no registry at the working tree`, as at `b634d60e5`.
  fixture: a scratch tree under the temp root. The tree holds none today.
- **AC2** — When `FOREIGN_PREFIX_PROBE=1 python upgrade_walk.py --case up` runs from the
  `scripts/govkit` directory of the moved clone of §4 "Measured at writing time", built from the build
  head with TOOL-dSafePassage-86 and -87 landed, it prints a line starting `upgrade-walk: pin` and
  ending `step(s)`, and no line holding `no registry at`. The run then exits 2 on the §3 hands-off.
  Red when: the memo is kept, so the run ends in a traceback holding `upgrade_steps.Refusal:` and
  `no registry at`, exit 1.
  cost: one clone of the repository, the move, and one release-0 apply, about three minutes.
  fixture: the moved clone of §4, built by the leg's own move. A bare `git mv` leaves the kit
  descriptor pin naming `tools`, and on Windows the walk then stops at `withdraw-one` first.
- **AC3** — When
  `python -c "import sys; sys.path.insert(0, 'tools/govkit'); import govkit; print(hasattr(govkit.derive_tool_root, 'cache_info'))"`
  runs from the repository root, it prints `False`.
  Red when: the `@functools.lru_cache(maxsize=None)` line is kept above `derive_tool_root`, so it
  prints `True`, as at `b634d60e5`.
- **AC4** — When `git grep -n -F "[dSP-89]" -- tools/govkit/selftest.py` runs, it prints one line, the
  check's label inside `check_upgrade_steps`.
  Red when: the arm is absent, so it prints nothing.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `upgrade-walk` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · the `[dSP-89]` check of `check_upgrade_steps`, staged red by the `@functools.lru_cache(maxsize=None)` line kept above `derive_tool_root`, which answers the second read with the first read's root · none

The four `{prefix}/govkit/` legs and `policy fixtures` are the guard join's for the two files; their
other guards are broad. `upgrade-walk` runs the walk whose stop this closes. The foreign-prefix parity
leg is not on the line: it stays red after this unit (§3), and AC2 observes this unit's part of its
`upgrade-walk` row directly.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-88-1-spec-writer.md` and its
  brief `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-88-spec-brief.md`.
  The stop is the one TOOL-dSafePassage-87's writer measured past the plants and left undiagnosed, at
  87 §4 "Past the plants, measured", with TOOL-dSafePassage-86 and 87's S7 staged at `scripts`. It is
  re-measured here at the leg's own move, diagnosed as the memo, and S1 was staged and measured in a
  clone of `b634d60e5` (§4 "Measured at writing time"). The brief's first item, the CRLF stop, is
  refused, for the reason in §4 "The CRLF stop, re-measured".

## 10. Reuse audit

S1 changes the existing tool-root primitive, `derive_tool_root` (`tools/govkit/govkit.py:191`), in
place, so every caller gets the fix through the function they already call. S2 extends
`check_upgrade_steps` (`tools/govkit/selftest.py:2916`), with its `steps` binding and `read_refusal`.
No new seam.
`python tools/codebase-map/reuse_lookup.py "derive the tool root of a tree whose layout moves between two reads, uncached"`
ranked `derive_tool_root` as a seam at fan-in 8, beside `read_steps` at fan-in 5 and name-stem
matches (`read_text`, `read`, `tree`, `repo_root`) that do not derive a tool root. The recall probe
ranked this brief and its handoff first, then the round-2 review's H1, which records that
`derive_tool_root(clone)` resolves `tools` at the pin. No record names the memo.

Recall terms used: `python tools/memory-recall/query.py "read_steps refuses no registry at the tip after the clone moved its tool root; a cached tool root" --terms "derive_tool_root lru_cache read_registry_at read_steps tool root prefix moved clone tip foreign-prefix upgrade-walk stale cache"`
