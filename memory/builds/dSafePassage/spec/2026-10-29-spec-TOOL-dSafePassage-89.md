# TOOL-dSafePassage-89 — the tool root is read from the tree on every call, so `read_steps` finds the registry at a moved tip

**Status:** CLOSED · rev-3 · 2026-10-29 · node a · Tier-2 · base cba885c5 · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dSafePassage-89-ledger.md](../build/2026-10-29-build-TOOL-dSafePassage-89-ledger.md) | journal | — |
| [2026-10-29-prompt-TOOL-dSafePassage-87-audit-fold-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-87-audit-fold-brief.md) | research | TOOL-dSafePassage-87 TOOL-dSafePassage-88 |
| [2026-10-29-prompt-TOOL-dSafePassage-88-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-88-spec-brief.md) | research | TOOL-dSafePassage-88 |
| [2026-10-29-prompt-TOOL-dSafePassage-89-build-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-89-build-brief.md) | journal | — |
| [2026-10-29-review-TOOL-dSafePassage-86-87-89-88-closing-diff-round3.md](../reviews/2026-10-29-review-TOOL-dSafePassage-86-87-89-88-closing-diff-round3.md) | diff-review | TOOL-dSafePassage-86 TOOL-dSafePassage-87 TOOL-dSafePassage-88 |
| [2026-10-29-review-TOOL-dSafePassage-86-87-89-88-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dSafePassage-86-87-89-88-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-86 TOOL-dSafePassage-87 TOOL-dSafePassage-88 |

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
  at git's native default (`tools/govkit/upgrade_walk.py:204`). So on Windows a text path with no eol
  pin checks out CRLF in the clone. The one byte-level edit the walk makes in the clone,
  `withdraw-one`, reads a pinned path at every prefix the leg moves to (§4), so this unit leaves it.
- The other three memos in the kit, `read_tree_modes` (`govkit.py:6703`), `read_git_dir`
  (`upgrade_steps.py:1102`) and `read_shipped_survivors` (`tools/govkit/step_gate.py:258`). Each is
  keyed by a sha or documents its ceiling in a `ponytail:` note, and none was measured stale.
- `upgrade_walk.py`. With TOOL-dSafePassage-86 and -87 landed, the walk calls `derive_tool_root` at
  three places, cited at `cba885c58`. `read_fixture_rows` calls it at `:124`, only for a
  `[[gov_plant]]` row once 87's S7 lands, and on gov's own root. `build_release_tree` calls it at
  `:214`, at the pin. `derive_release_engine` (`:183-187`) calls it through `resolve_tool_path` once
  87's S12 lands, at the pin. 87's S7 replaces the fourth, `:232`, with `read_target_prefix`. The
  three keep their order and their answers.
- `check_shim_paths` (`upgrade_walk.py:553-579`), which reads at the tip and whose answer this unit
  changes. It reads gov's own shim rows through `shims.read_shim_rows(ctx["clone"])` (`:565`), whose
  `derive_tool_root(clone)` (`shims.py:71`) resolves each row's `from` and `to`. With the memo, that
  call answers the pin's `tools`, so the tip read of `shims.toml` refuses at a moved prefix. Without
  it, the call answers the moved root, and the rows' `from` would be compared with a receipt
  installed under `tools` at `:572-574` and could never match: a silently vacuous check (round-1 spec
  audit, M4). TOOL-dSafePassage-87's S11 roots gov's rows at the target's install prefix before this
  unit lands, so the comparison reads one root (the consumes-from edge below). This unit leaves the
  function alone.
- A green `upgrade-walk` row in the foreign-prefix parity leg. With TOOL-dSafePassage-86, -87 and this
  unit staged, the walk at `scripts` reads its steps and then stops in the `up` case (the hands-off
  below).

### Edges

- **consumes-from** `TOOL-dSafePassage-86` — `derive_release_engine`, without which AC2's moved-prefix
  walk stops at release-0's apply and never reaches `read_steps`
- **consumes-from** `TOOL-dSafePassage-87` — S7's two roots, without which AC2's walk stops at the
  `engine-edit` plant before the clone moves to its tip. And S11's root for gov's own shim rows,
  without which the walk's `shims` case is silently vacuous at a moved prefix once this unit drops
  the memo
- **hands-off** `TOOL-dSafePassage-88` — the third stop at a moved prefix, measured on 2026-10-29
  with all three units staged at `scripts`. The `up` case's walk to the tip exits 1, holding back
  every kit and naming each installed file under the target's `tools` as a held path no ordered
  plant names. TOOL-dSafePassage-88 diagnoses it as `update`'s rename-destination guard refusing
  the row's own file, and closes it.

## 4. Design

Every cited line holds at `cba885c58`, the build head with TOOL-dSafePassage-86 landed. Outside
`memory/` it differs from `b634d60e5` only in `tools/govkit/upgrade_walk.py`, whose lines are cited
at `cba885c58`. TOOL-dSafePassage-87 builds before this unit and moves them again, so the builder
reads each by content.

### The defect, at `cba885c58`

`derive_tool_root` (`govkit.py:190-211`) is decorated with `@functools.lru_cache(maxsize=None)`. For
a root other than gov's own checkout (`:201-204`), it globs that root for its one
`govkit/registry.toml` (`:205-206`) and returns the directory above it.

`build_release_tree` checks its clone out at the pin (`upgrade_walk.py:205`) and calls
`gk.derive_tool_root(clone)` there (`:214`, `:232`, and `:187` through `derive_release_engine`). The
pin holds `tools/govkit/registry.toml`, so the memo stores `tools` under the key `clone`. At `:241`
the clone checks out the tip, whose tool root is the moved one. `main` then calls
`us.read_steps(ctx["clone"], ...)` (`:1115`). That reaches
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
imported for `read_tree_modes` (`:6703`). Every caller keeps its call and now reads the tree as it
stands. The callers are the grep's, verbatim at `cba885c58`, 30 lines: the `def` at `govkit.py:191`
and 29 call lines, one of them (`govkit.py:1930`) holding two calls.

```text
$ git grep -n "derive_tool_root(" -- tools/govkit
tools/govkit/docs_leg.py:214:    troot = gk.derive_tool_root(root)
tools/govkit/docs_leg.py:453:            verdict, what = check_page_command(cmd, by_entry, tracked, gk.derive_tool_root(root))
tools/govkit/fixtures/retired_edits.py:32:PFX = govkit.derive_tool_root(govkit.repo_root())
tools/govkit/govkit.py:191:def derive_tool_root(root: pathlib.Path | str) -> str:
tools/govkit/govkit.py:301:    tr = derive_tool_root(root)
tools/govkit/govkit.py:319:    tr = derive_tool_root(root)
tools/govkit/govkit.py:580:    tr = derive_tool_root(repo_root())
tools/govkit/govkit.py:854:    troot = (derive_tool_root(root)
tools/govkit/govkit.py:1058:    tr = derive_tool_root(root)
tools/govkit/govkit.py:1122:            path = resolve_prefix_token(carrier, derive_tool_root(root))
tools/govkit/govkit.py:1930:        _k = (derive_tool_root(root) + "/") if derive_tool_root(root) else ""
tools/govkit/govkit.py:2311:        _tr = derive_tool_root(root)
tools/govkit/govkit.py:13592:    tr = derive_tool_root(root)
tools/govkit/govkit.py:13617:    return resolve_descriptor_paths(desc, derive_tool_root(root))
tools/govkit/govkit.py:13718:    ctx = {**canonical_ctx(eid), "kit": (desc.get("home") or "").rstrip("/") or derive_tool_root(root)}
tools/govkit/selftest.py:5278:    _tr = step_gate.gk.derive_tool_root(clone)
tools/govkit/shims.py:71:    troot = govkit.derive_tool_root(root)
tools/govkit/shims.py:324:    tr = govkit.derive_tool_root(root)
tools/govkit/step_gate.py:102:    path = (pathlib.Path(root) / gk.resolve_prefix_token(path_s, gk.derive_tool_root(root))).resolve()
tools/govkit/step_gate.py:272:    tr = gk.derive_tool_root(root)
tools/govkit/step_gate.py:278:    tr = gk.derive_tool_root(root)
tools/govkit/step_gate.py:398:    return "file:" + derive_member_path(rows[0], gk.derive_tool_root(clone))
tools/govkit/step_gate.py:409:    return "installable:" + derive_member_path(srcs[0], gk.derive_tool_root(clone))
tools/govkit/upgrade_steps.py:755:    tr = gk.derive_tool_root(root)
tools/govkit/upgrade_steps.py:1015:    tr = load_govkit().derive_tool_root(root)
tools/govkit/upgrade_steps.py:1471:    tr = gk.derive_tool_root(gov_root)
tools/govkit/upgrade_walk.py:124:    troot = gk.derive_tool_root(gk.repo_root())
tools/govkit/upgrade_walk.py:187:    return clone / gk.resolve_prefix_token("{prefix}/govkit/govkit.py", gk.derive_tool_root(clone))
tools/govkit/upgrade_walk.py:214:                                         gk.derive_tool_root(clone)).replace("{scratch}", root.as_posix())
tools/govkit/upgrade_walk.py:232:        p = subprocess.run([gk.resolve_bash(), (gk.resolve_kit_dir("policy", adopter, t / gk.derive_tool_root(clone)) / adopter).as_posix(), "--scaffold", "--target", t.as_posix()],
```

The same grep over `tools` also prints `tools/policy/budgets.py`, `tools/policy/check_policy.py` and
`tools/roles/render_agents.py`. Each calls a function of the same name defined in its own kit
(`budgets.py:100`, `render_agents.py:105`), not govkit's, so this unit does not reach them.

Whether a caller's tree can move under one root between two of its calls decides whether the memo
ever gave it a stale answer:

| Callers | The root they pass | Can its tree move between two calls? |
|---|---|---|
| `upgrade_walk.py:124`, `govkit.py:580`, `fixtures/retired_edits.py:32` | gov's own checkout, `repo_root()` | No. Gov's own root takes the branch at `govkit.py:201-204`, which never globs. |
| `upgrade_walk.py:187` and `:214`, and `:232` until 87's S7 | the walk's clone, at the pin | Yes. Each runs before the clone checks out its tip (`:241`), so each reads the pin. |
| `upgrade_steps.py:755`, through `read_steps` (`upgrade_walk.py:1115`); `shims.py:71` and `:324`, through `check_shim_paths` (`upgrade_walk.py:565`) | the walk's clone, at the tip | Yes. This is the stale answer S1 closes, and §3 weighs `check_shim_paths`. |
| `step_gate.py:398` and `:409`, the file and installable plant writers | a fixture clone | The tree changes: each stages a README `git rm` or `git mv` (`:397`, `:408`) before its call. No registry moves, so the answer is the same. |
| `docs_leg.py:214` and `:453` | the tree the docs leg checks | No. The leg reads one tree. `:453` runs once per page command. |
| `step_gate.py:102`, `:272` and `:278`; `selftest.py:5278`; `upgrade_steps.py:1015` and `:1471`; `govkit.py`'s other ten lines | the root a command, fixture or arm hands in | Not measured. No move of a registry between two reads of one root was found at these sites. |

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
tracked text file outside the record corpus that the move did not bring in, plus the renders the
install-prefix gate lists (`tools/run-gates/foreign-prefix.gov.test.sh:519`). The moved list is the
staged additions (`:506`), and its comment says nothing else the move brought in is touched
(`:500-502`). So `.gitattributes`, which the move does not bring in, is re-spelled, and a moved file
that is not a render, such as the release-0 `deploy.toml`, keeps its text. In the clone above,
`.gitattributes:222` read
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

- **Clear the memo in `build_release_tree` after the checkout to the tip (`:241`).** It closes the
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
  govkit's other runs were not measured. Callers that pass gov's own root never glob (§4 "S1"). The
  step gate's callers pass a fixture clone, so each of their calls globs, at about 3.9 ms; the two
  plant writers (`step_gate.py:398`, `:409`) run once per plant. `docs_leg.py:453` calls once per page
  command, and globs only where the leg checks a tree that is not gov's own, as its fixture is.
- error / empty / loading states: a root with no registry, or more than one, refuses as it does now
  (`govkit.py:207-209`), on every call rather than once.
- observability: the `[dSP-89]` check prints its two reads on a red.
- risks: a caller that relied on the memo to keep a pin-time answer after a move would now see the
  tip's answer. §4 "S1" says, per caller, whether its tree can move. The walk's calls at `:214` and
  through `derive_release_engine` run at the pin, so they read the pin either way. The step gate's
  plant writers stage a README `git rm` or `git mv` before their call and move no registry, so their
  answer is unchanged. The one tip-time reader whose answer changes in kind is `check_shim_paths`
  (§3): it moves from a loud refusal to a comparison, which TOOL-dSafePassage-87's S11 roots at the
  target's prefix.
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
  AC2 is observed at this unit's own pass, before TOOL-dSafePassage-88 builds. That exit 2 is the
  stop 88 removes, and once 88 has landed the same run prints `upgrade-walk: GREEN` and exits 0
  (88's AC2).
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

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `upgrade-walk` · `docs` · `step-gate` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · the `[dSP-89]` check of `check_upgrade_steps`, staged red by the `@functools.lru_cache(maxsize=None)` line kept above `derive_tool_root`, which answers the second read with the first read's root · none

The four `{prefix}/govkit/` legs and `policy fixtures` are the guard join's for the two files; their
other guards are broad. `upgrade-walk` runs the walk whose stop this closes. `docs` and `step-gate`
run `docs_leg.py` and `step_gate.py`, whose calls §4 "S1" lists. Both legs carry no guard in
`tools/gate-legs.json`, so the guard join does not owe them and they are named here. The
foreign-prefix parity
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
- rev-2 · 2026-10-29 · §3 · from the brief
  `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-88-third-stop-spec-brief.md`.
  §3's hands-off external edge, the third stop at a moved prefix, now points at
  TOOL-dSafePassage-88, which closes it and declares the mirroring consumes-from.
- rev-3 · 2026-10-29 · §3 §4 §5 §6 §7 · S1 · AC2 · folds the round-1 spec audit,
  `memory/builds/dSafePassage/reviews/2026-10-29-review-TOOL-dSafePassage-86-87-89-88-spec-audit-round1.md`,
  from the brief
  `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-87-audit-fold-brief.md`.
  M4's half for this unit: §3 weighs `check_shim_paths` as a tip-time reader whose answer changes,
  and the consumes-from edge to TOOL-dSafePassage-87 names its S11. L1: §4 "S1" pastes the caller
  grep verbatim and says per caller whether its tree can move, §3 restates the walk's calls with 86
  and 87 landed, §5 records the step gate's clone callers, and §7 adds `docs` and `step-gate`. The
  record's sub-claim that `govkit.py` holds twelve call lines is not borne out: its own list names
  eleven, the grep's twelfth `govkit.py` line being the `def`. L6: §4 "The CRLF stop, re-measured"
  cites `write_declarations`' skip at `foreign-prefix.gov.test.sh:519`. AC2 states it is observed
  before TOOL-dSafePassage-88 builds. The base moves to `cba885c5`, with 86 landed, and
  `upgrade_walk.py`'s lines are re-cited there.

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
