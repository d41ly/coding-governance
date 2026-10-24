# TOOL-dDeclaredLoop-86 — the round-6 spec audit's 22 minors, batched

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 42 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-86-deviation-861.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-86-deviation-861.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-6 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit.md`)
exited CONVERGED with 25 confirmed findings over units 80 to 82, the round-5 promotions. Its three highs
are units 83, 84 and 85, one per id. This unit is the batch BUILD-METHOD M4 makes of the rest, every
MEDIUM and every LOW, each by its report id and each its own scope item, where the report merged ids into
one item too. The minors land on several units, so this unit repairs none in particular and builds after
every unit (order 42). Where a minor is the medium grade of a defect a high unit closes, the item here is
what that grade's fix asks beyond the high unit's mechanism.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 18 | S1 |
| M2 | MEDIUM | 9 | S2 |
| M3 | MEDIUM | 4 | S3 |
| M4 | MEDIUM | 11, 17 | S4, S5 |
| M5 | MEDIUM | 3 | S6 |
| M6 | MEDIUM | 15 | S7 |
| M7 | MEDIUM | 14 | S8 |
| M8 | MEDIUM | 23 | S9 |
| M9 | MEDIUM | 25 | S10 |
| M10 | MEDIUM | 26 | S11 |
| M11 | MEDIUM | 27 | S12 |
| M12 | MEDIUM | 28 | S13 |
| L1 | LOW | 10 | S14 |
| L2 | LOW | 5 | S15 |
| L3 | LOW | 6 | S16 |
| L4 | LOW | 12 | S17 |
| L5 | LOW | 13 | S18 |
| L6 | LOW | 16 | S19 |
| L7 | LOW | 19 | S20 |
| L8 | LOW | 21 | S21 |
| L9 | LOW | 29 | S22 |

That is 13 MEDIUM and 9 LOW findings by raw id. M1 and M2 are the medium grades of H1 and H2, whose
mechanisms are units 83, 84 and 85. M3 and L1 are one defect at two grades, fixed once across S3 and S14.
The report's four refuted findings, ids 2, 8, 20 and 22, are not in the disposal population.

## 2. Scope (IN)

- **S1** — id 18. `TOOL-dDeclaredLoop-81` §4 Evidence's last bullet stops quoting 75 S27's retired
  fallback clause: it says that 75 S27, as restated, sends no exit but 0 and 1 to the parents. The edit
  is a rev bump of 81 with its §9 line. Observed by AC1.
- **S2** — id 9. `check_write_tree_usage(rc, text)` in `tools/loop/guard.py`, as
  `TOOL-dDeclaredLoop-85` S2 defines it, requires `rc` 0 or 129 and a line opening
  `usage: git merge-tree` on either stream for both `supported` and `unsupported`. Any other outcome is
  `probe failed`, a text that names `--write-tree` with no usage line or another exit code included.
  Observed by AC2.
- **S3** — id 4. `TOOL-dDeclaredLoop-80` §4 Files touched records that `TOOL-dDeclaredLoop-67` writes
  `tools/loop/budget.py` and `tools/loop/breakpoints.py` at order 38 too, dispatched in sequence with 67
  first where both are dispatched, as 82 S14 records for step 39. The edit is a rev bump of 80 with its
  §9 line. Observed by AC3.
- **S4** — id 11. `TOOL-dDeclaredLoop-76` AC1's exit-0 half is owed at 80's pass commit, where 80 S2 has
  moved the conf-writing plants inside the fixture boundary. At 76's own pass the plant's exit and every
  hit it names are recorded, and each hit names a line inside a plant 80 S2 moves. The edit is a rev bump
  of 76 with its §9 line. Observed by AC4.
- **S5** — id 17. `TOOL-dDeclaredLoop-79` S10 and AC10 are amended, as a rev bump of 79 with its §9 line:
  at 76's pass commit the exits of `loop budget fixtures` and `loop breakpoints fixtures` are recorded,
  and a non-zero exit there whose only failing plant is `no-own-conf-read` is re-observed at 80's pass
  commit, where it must be 0. This pass runs the pass-commit probe for both legs at 80's pass commit and
  records both exits. Observed by AC5.
- **S6** — id 3. 81 S3 names C's states once, `present`, `absent`, `conflicted`, `uncomputable` and
  `failed`, and says which read the parents: `conflicted`, `uncomputable` and `failed`. Under `failed` and
  under `conflicted`, a parent blob that does not parse refuses with 78 S3's
  `does not parse at parent <sha8>` line, never a traceback and never a keyless parent. The plant
  `push-merge-tree-fatal-unparseable-parent` joins `guard.py --fixture`: a two-parent merge,
  `run_merge_tree` answering 128, one parent's policy blob unparseable. 78 S3's "at a parent the
  `uncomputable` branch reads" becomes "at a parent any branch reads". The edits are rev bumps of 81 and
  78. Observed by AC6.
- **S7** — id 15. `TOOL-dDeclaredLoop-59` S3 is restated, as a rev bump of 59 with its §9 line: the
  missing feature is detected by 81 S1's usage probe, never by an exit code, and a re-merge exit 129 from
  a git the probe found capable is 81's `failed` state. Observed by AC7.
- **S8** — id 14. `TOOL-dDeclaredLoop-82` S6 is restated, as a rev bump of 82 with its §9 line: at each
  pass commit the probe reads that commit's `tools/gate-legs.json` with `held_halves.load_manifest`
  (`tools/run-gates/held_halves.py:80`) and looks the row up by name. No match records
  `leg absent at pass commit`. A match goes to `derive_leg_argv(row, ...)` for its argv. A refusal from
  `load_manifest` is recorded as its own line, never as an absent leg. 82 §10 names `load_manifest`.
  S5's probe at this pass reads the manifest that way. Observed by AC8.
- **S9** — id 23. The `url-forms` plant of `tools/loop/position.py` runs its fetch with every credential
  helper cleared and prompting off: `git -c credential.helper= fetch`, with `GIT_TERMINAL_PROMPT=0` and
  `GCM_INTERACTIVE=never` in that call's environment alone. 82 §5 security names the OS credential store
  as a write surface the plant never reaches, in S8's rev bump of 82. Observed by AC9.
- **S10** — id 25. The `conf-read-forms` plant of `tools/loop/budget.py`, its rows (82 AC1, AC10, AC13's
  forms below and AC16's docstring module) and 82 AC15's two root-source trees are built inside
  functions 80 S1 bounds, never as a module-level table. 80 S4 is widened from "the plants of 75 and 79"
  to every plant a later unit adds to either module, 82 and this unit included, in S3's rev bump of 80.
  Observed by AC10.
- **S11** — id 26. 82 S6 says, in S8's rev bump: where no later pass commit holds the row, the probe
  writes `leg absent at every later pass commit` and fails. 82 AC6 and AC21 require each absent-leg line
  to be followed by exactly one recorded exit. Observed by AC11.
- **S12** — id 27. 82 AC5 gains its population floor, in S8's rev bump: the `loop selftest` and
  `loop breakpoints fixtures` rows exist in `tools/gate-legs.json`, each carries `{prefix}/loop/` among
  its guards, and at least one live spec trips each. This pass runs that probe. Observed by AC12.
- **S13** — id 28. `derive_conf_constants(loop_lib_path)` in `tools/loop/loop_lib.py` answers the
  module-level names bound in that file by an `Assign` or `AnnAssign` whose value is a str `Constant`, a
  `JoinedStr`, a `BinOp` of strings, or a `Path(...)` or `PurePath(...)` call over one, any of them
  containing a conf name. `derive_conf_reads` reads it from the `loop_lib.py` beside the scanned module,
  counts `from loop_lib import *` as importing every such name, and refuses naming the file where it is
  missing or does not parse. `conf-read-forms` gains an annotated binding, a `Path` binding and a star
  import. 82 S1 is restated, in S8's rev bump. Observed by AC13.
- **S14** — id 10. 82 S14 and AC14 are extended to step 38, in S8's rev bump: the build README's
  build-order region, rendered by `TOOL-dDeclaredLoop-66`'s `render_order`, prints step 38's Parallel cell
  opening `no`. Observed by AC14.
- **S15** — id 5. 82 S1 says the bindings come from the `loop_lib.py` beside the scanned module, S13's
  rule, and 82 AC1's scratch module and scratch `loop_lib.py` are siblings in one scratch directory, in
  S8's rev bump. Observed by AC15.
- **S16** — id 6. 80 AC4's population guard is three greps over `tools/loop/budget.py`, one per plant,
  each printing at least 1, in S3's rev bump of 80. This pass runs them. Observed by AC16.
- **S17** — id 12. 76 S2 and 76 §4's sketch say a string constant that contains a conf name, citing 80's
  boundary and 82 S1's conf-constant kind, in S4's rev bump of 76. Observed by AC17.
- **S18** — id 13. 82 §4 Evidence, S19 and AC22 are re-pinned to `tools/unattended/check-unattended.sh:3769`
  and `tools/unattended/unattended.sh:1116-1140`, in S8's rev bump. Observed by AC18.
- **S19** — id 16. 82 S6 keys each probe line by unit id, leg name and probed commit sha; a re-run
  replaces the line with the same key, and AC6 and AC21 read the latest line per key, AC21 adding that no
  key appears twice, in S8's rev bump. S5's probe lines at this pass carry the key. Observed by AC19.
- **S20** — id 19. 82 §7's sibling-leg paragraph names `loop breakpoints fixtures` and says S5 puts it
  and `loop selftest` on the leg line, in S8's rev bump. Observed by AC20.
- **S21** — id 21. `derive_conf_reads` resolves `tree_lib` through
  `resolve_kit_dir("memory-tree", "tree_lib.py", here)` inside the function only, never at module import.
  Where the resolved `tree_lib` lacks `derive_docstring_ids`, the `no-own-conf-read` plant exits non-zero
  printing `govkit update --kits memory-tree`. 82 S8 and §5 risks say so, in S8's rev bump.
  Observed by AC21.
- **S22** — id 29. The `failed` refusal of 81 S3 spells three cases in place of `<rc> <stderr first line>`:
  a re-merge that fails to start prints `start failed: <strerror>`, a death by a signal prints
  `signal <n>` with n the positive signal number, and an empty stderr prints `(no stderr)`. The
  `push-merge-tree-fatal` plant gains a row in which `run_merge_tree` raises `OSError`. 81 S2 and S3 say
  so, in S1's rev bump of 81. Observed by AC22.

## 3. Non-goals (OUT)

- The three highs' mechanisms: units 83, 84 and 85, each its own unit.
- The report's left-shift gates and checklist entries: each class is recorded at the close, and each item
  above carries the observation that discharges its own defect.
- The refuted findings 2, 8, 20 and 22.
- Deleting the credential-store entries the round-6 skeptic's own probe left on node `d`: a write to the
  owner's environment outside the repository, which this unit does not price.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-59` — S3's missing-feature sentence (id 15)
- **consumes-from** `TOOL-dDeclaredLoop-66` — `render_order`, whose step-38 Parallel cell S14 observes (id 10)
- **consumes-from** `TOOL-dDeclaredLoop-76` — AC1's exit-0 observation, S2 and §4's sketch (ids 11, 12)
- **consumes-from** `TOOL-dDeclaredLoop-78` — S3's parent-side parse refusal (id 3)
- **consumes-from** `TOOL-dDeclaredLoop-79` — S10's probe and AC10 (id 17)
- **consumes-from** `TOOL-dDeclaredLoop-80` — the fixture boundary, S4's plant population, §4 Files touched and AC4 (ids 4, 6, 25)
- **consumes-from** `TOOL-dDeclaredLoop-81` — the `failed` state, its refusal text, S3's state names and §4 Evidence (ids 3, 18, 29)
- **consumes-from** `TOOL-dDeclaredLoop-82` — `derive_conf_reads`'s conf-constant kind, the `conf-read-forms` and `url-forms` plants, the pass-commit probe of S6 and S21, S14, AC5, §4, §5, §7 and §10 (ids 5, 10, 13, 14, 16, 19, 21, 23, 25, 26, 27, 28)
- **consumes-from** `TOOL-dDeclaredLoop-85` — `check_write_tree_usage`'s three answers, which S2 narrows (id 9)

## 4. Design

### Write set

This pass writes `tools/loop/guard.py` (S2, S6, S22), `tools/loop/position.py` (S9),
`tools/loop/budget.py` (S10, S13) and `tools/loop/loop_lib.py` (S13, S21). Inside this build's folder it
amends the specs of 59, 76, 78, 79, 80, 81 and 82 as rev bumps, one per spec, each with its §9 line; the
build README's regions are the generator's render. S5, S8, S12, S16 and S19 also observe and record.

### The conf-constant kind, after this unit (S13, S15, S21)

```
derive_conf_reads(path):
    tree    = ast.parse(read(path))
    tl      = resolve_kit_dir("memory-tree", "tree_lib.py", here)       # inside the call, never at import
    docs    = tl.derive_docstring_ids(tree)    # missing -> refuse: govkit update --kits memory-tree
    consts  = derive_conf_constants(sibling(path, "loop_lib.py"))      # missing or unparseable -> refuse naming it
    star    = "from loop_lib import *" in tree -> every member of consts is a local name
    ... 82 S10's walk, outside docs and 80 S1's boundary, unchanged

derive_conf_constants(loop_lib_path):
    module-level Assign | AnnAssign, value one of:
        Constant str | JoinedStr | BinOp of str | Path(<one of these>) | PurePath(<one of these>)
    whose text contains ".memory-tree.conf" or ".unattended.conf"
```

### Evidence

Read or probed 2026-10-24 at the worktree tip on node `d`: PINNED, that date.

- `derive_leg_argv(row, troot, pybin, aliases=None)` resolves a row its caller hands it
  (`tools/run-gates/measure_legs.py:503`); the manifest's reader is `load_manifest`
  (`tools/run-gates/held_halves.py:80`), wrapped by `read_profile_legs` (`measure_legs.py:473`).
- `git config --show-origin --get-all credential.helper` printed `manager` from
  `C:/Program Files/Git/etc/gitconfig`, so a fetch from a URL carrying `user:tok@` reaches Git Credential
  Manager unless the helper is cleared. 75 S34 runs `position.py --fixture`'s git with
  `GIT_CONFIG_GLOBAL` and `GIT_CONFIG_SYSTEM` at empty files (75 §2 S34), which keeps that helper out only
  where a call inherits that environment; 82 S23 does not say its fetch does.
- `tools/unattended/check-unattended.sh:3765` is a comment line and the `pdod=` extraction is at :3769;
  `norm_endpoint()` opens at `tools/unattended/unattended.sh:1116`.
- `check_guard_trips(path, guard)` compares one path with one guard (`tools/check-spec-tokens.py:581`),
  so with no manifest row nothing trips.
- The loop kit reaches `tree_lib` through `resolve_kit_dir` (`tools/lib/resolve_kit_dir.py`), as 75 S35
  states (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md`, line 179), and
  `tools/memory-tree/kit.toml` records that govkit cannot express a version floor.
- The build README prints `| 38 |` with four units and Parallel `yes`
  (`memory/builds/dDeclaredLoop/README.md`, the build-order region); 67's Files touched holds both
  `tools/loop/budget.py` and `tools/loop/breakpoints.py`; 66 and 67 are DEFERRED at this writing.
- `git merge-tree -h` exited 129 with its usage on stdout alone, as 85 §4 records.

### Files touched (estimate)

- `tools/loop/guard.py`
- `tools/loop/position.py`
- `tools/loop/budget.py`
- `tools/loop/loop_lib.py`
- `memory/builds/dDeclaredLoop/spec/`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **One unit per minor.** M4 forbids it.
- **Two batch units, the guard items and the rest.** The halves are not disjoint by M6 clause 1: S4 and
  S17 both write the 76 spec, S3, S10 and S16 the 80 spec, and S1, S6 and S22 the 81 spec, while S6 also
  writes 78. A guard half of S2, S6 and S22 still writes 81, which S1 writes; a split along any spec
  boundary leaves `tools/loop/budget.py` in both S10 and S13.
- **An explicit `loop_lib_path` argument for `derive_conf_reads` (L2's other option).** The plant's
  scratch copy already puts the two files side by side, and a sibling rule needs no caller to pass the
  kit's own path; the argument would be a second way to say the same thing.
- **A version floor in `tools/loop/kit.toml` for S21.** govkit cannot express one; a named refusal at the
  one call that needs the function is the route the memory-tree kit's own `requires_if` rows take.

## 5. Production-readiness checklist

- security — S9 keeps a planted credential out of the OS credential store and off any prompt; S13 widens
  what the no-own-conf-read rule sees; S6 and S22 keep a failed re-merge refusing with no traceback.
- perf / scale — S5 and S12 cost one scratch worktree and one manifest read, once at this pass.
- error / empty / loading states — S6, S13, S21 and S22 each name a missing or broken input instead of
  raising; S11 refuses an empty absent-leg population.
- observability — every probe line carries its key (S19); each refusal names its file or case.
- risks — the amendments land on specs whose units are built, as 82 amends its siblings; each is a rev
  bump with its §9 line. S4 and S5 move where 76 AC1 and 79 AC10 observe one plant, never what passes.
  S14's observation rests on 66, DEFERRED at this writing.
- testing — AC1 to AC22 as plants, probes and greps; the arms under §7, observed at the close.
- migration — none: every reader is unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `grep -c "any other exit code grades against the parents alone"` runs over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-81.md`, it prints 0.
  Red when: 81's Evidence still quotes the retired fallback as a live sentence.
- **AC2** — When a `python -c` probe imports `guard` from `tools/loop/` and calls
  `check_write_tree_usage` on `(0, "usage: git merge-tree [--write-tree] [<options>] <branch1> <branch2>")`,
  `(0, "usage: git merge-tree <base-tree> <branch1> <branch2>")`,
  `(128, "error: unknown option --write-tree")` and `(129, "see --write-tree")`, it answers `supported`,
  `unsupported`, `probe failed` and `probe failed`.
  Red when: a text naming the option with no usage line, or under another exit code, answers `supported`.
- **AC3** — When `awk '/^### Files touched/,/^### Alternatives/'` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-80.md` is piped to
  `grep -c "TOOL-dDeclaredLoop-67"`, it prints at least 1.
  Red when: 80 still records no shared write at step 38.
- **AC4** — When `awk '/^- \*\*AC1\*\*/,/^- \*\*AC2\*\*/'` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-76.md` is piped to
  `grep -c "TOOL-dDeclaredLoop-80"`, it prints at least 1.
  Red when: 76 AC1 still owes exit 0 at 76's own pass, where the plant is red by design.
- **AC5** — When the pass-commit probe runs `loop budget fixtures` and `loop breakpoints fixtures` at 80's
  pass commit, this unit's acceptance ledger holds both exits and each is 0, and
  `awk '/^- \*\*S10\*\*/,/^- \*\*S11\*\*/'` over the 79 spec piped to `grep -c "80's pass commit"` prints
  at least 1.
  Red when: 79 AC10 reads a non-zero exit at 76's pass commit with no re-observation after 80.
  cost: one scratch worktree.
- **AC6** — When `python guard.py --fixture --plant push-merge-tree-fatal-unparseable-parent` runs in
  `tools/loop/`, it exits 1 printing `does not parse at parent ` and no `Traceback`, and
  `grep -c "the .uncomputable. branch reads"` over the 78 spec prints 0.
  Red when: the `failed` branch raises on the parent, or treats it as holding no keys.
- **AC7** — When `grep -c "it exits 129"` runs over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-59.md`, it prints 0, and
  `awk '/^- \*\*S3\*\*/,/^- \*\*S4\*\*/'` over it piped to `grep -c "TOOL-dDeclaredLoop-81"` prints at
  least 1.
  Red when: 59 S3 still maps exit 129 to the parents.
- **AC8** — When `awk '/^- \*\*S6\*\*/,/^- \*\*S7\*\*/'` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-82.md` is piped to
  `grep -c "load_manifest"`, it prints at least 1, and `grep -c "derive_leg_argv. finds no manifest row"`
  over the same file prints 0.
  Red when: the probe still credits `derive_leg_argv` with a lookup by name.
- **AC9** — When `cmdkey /list` is read before and after `python position.py --fixture --plant url-forms`
  in `tools/loop/`, no new credential target for the fixture's loopback `git:` URL appears, and `grep -c "credential.helper="`
  over `position.py` prints at least 1; with the helper clearing staged out, a new target appears, and the
  build deletes it with `cmdkey /delete`.
  Red when: the plant's fetch runs with the node's credential helpers active.
  permission: the staged break writes one dummy entry to the OS credential store, which the build makes
  and removes; a reviewer does not.
  fixture: a node with Git for Windows' `manager` helper; elsewhere both halves read no new entry.
- **AC10** — When `python budget.py --fixture --plant no-own-conf-read` and the same plant of
  `breakpoints.py --fixture` run in `tools/loop/` at this pass, each exits 0 and prints a
  `fixture boundary:` line; in a scratch copy whose `conf-read-forms` rows sit in a module-level table,
  the first exits non-zero naming `conf name`; and `awk '/^- \*\*S4\*\*/,/^## 3/'` over the 80 spec piped
  to `grep -c "every plant"` prints at least 1.
  Red when: a forms table outside the boundary turns the rule red at the close.
- **AC11** — When `grep -c "leg absent at every later pass commit"` runs over the 82 spec, it prints at
  least 1, and `awk '/^- \*\*AC21\*\*/,/^- \*\*AC22\*\*/'` over it piped to `grep -c "exactly one"` prints
  at least 1.
  Red when: a ledger of absent-leg lines alone passes AC21 with no exit recorded.
- **AC12** — When a probe loads `tools/check-spec-tokens.py` by `importlib` and reads
  `tools/gate-legs.json`, the rows `loop selftest` and `loop breakpoints fixtures` both exist, each guard
  list holds `{prefix}/loop/`, and `check_guard_trips` finds at least one spec under this build's `spec/`
  folder, not CLOSED or WONTDO, whose Files touched trips each; and the 82 AC5 bullet names both rows'
  existence.
  Red when: either row is absent or trips no spec, and AC5 passes over an empty set.
  fixture: the rows are minted by sibling units before order 42; at HEAD neither exists.
- **AC13** — When `python budget.py --fixture --plant conf-read-forms` runs, its rows reading
  `ll.UNATTENDED_CONF_PATH` bound as `UNATTENDED_CONF_PATH = Path(".unattended.conf")`, a name bound as
  `CONF: str = ".memory-tree.conf"`, and a name reached through `from loop_lib import *` each answer one
  `conf constant` hit; with the sibling `loop_lib.py` deleted from its scratch directory, the plant exits
  non-zero naming `loop_lib.py`.
  Red when: only a plain `Assign` of a `Constant` counts, or a missing loop_lib yields an empty set.
- **AC14** — When `grep -n "^| 38 |"` runs over `memory/builds/dDeclaredLoop/README.md` at this pass, the
  Parallel cell opens `no`.
  Red when: step 38 still reads `yes` over two units sharing `budget.py`.
  fixture: the cell is `render_order`'s as `TOOL-dDeclaredLoop-66` rebuilds it; 66 is DEFERRED at this
  writing, and today's `render_order` prints `yes` for any group of two or more.
- **AC15** — When `awk '/^- \*\*S1\*\*/,/^- \*\*S2\*\*/'` over the 82 spec is piped to
  `grep -c "beside the scanned module"`, it prints at least 1, and the AC1 range
  `awk '/^- \*\*AC1\*\*/,/^- \*\*AC2\*\*/'` piped to `grep -c "sibling"` prints at least 1.
  Red when: S1 still fixes `loop_lib.py` while AC1 reads a scratch one.
- **AC16** — When `grep -c "unset-driver-root"`, `grep -c "trailing-slash-agree"` and `grep -c "no-confs"`
  run over `budget.py` in `tools/loop/`, each prints at least 1, and
  `awk '/^- \*\*AC4\*\*/,/^## 7/'` over the 80 spec piped to `grep -c "grep -c"` prints at least 3.
  Red when: one grep over an alternation still counts three lines naming one plant.
- **AC17** — When `grep -c "ending .\.memory-tree.conf\|Constant str ending"` runs over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-76.md`, it prints 0.
  Red when: 76 still tells its reader a mid-string conf name is not a read.
- **AC18** — When `grep -c "unattended.sh:1117\|:3765"` runs over the 82 spec, it prints 0, and
  `grep -c "check-unattended.sh:3769"` prints at least 1.
  Red when: a pin still lands on a comment line or one line past the function's opening.
- **AC19** — When the probe lines this unit's journal record writes under its `**Evidences:**` block are
  read, each names a unit id, a leg name and a commit sha, and no such key appears twice; and
  `awk '/^- \*\*S6\*\*/,/^- \*\*S7\*\*/'` over the 82 spec piped to `grep -c "probed commit"` prints at
  least 1.
  Red when: a re-run appends a second line for one key and an old red line keeps AC6 red.
- **AC20** — When `awk '/^## 7/,/^## 8/'` over the 82 spec is piped to
  `grep -c "loop breakpoints fixtures"`, it prints at least 1.
  Red when: 82 §7 still reads as complete without the breakpoints leg its Files touched trips.
- **AC21** — When a scratch copy of `tools/loop/`, `tools/lib/` and `tools/memory-tree/` has
  `derive_docstring_ids` removed from its `tree_lib.py`, `python -c "import loop_lib"` in its `loop/`
  exits 0, and `python budget.py --fixture --plant no-own-conf-read` there exits non-zero printing
  `govkit update --kits memory-tree` and no `Traceback`.
  Red when: the loop kit imports the function at module load, or raises `AttributeError` at the call.
- **AC22** — When `python guard.py --fixture --plant push-merge-tree-fatal` runs, its `OSError` row prints
  `the clean re-merge failed: start failed` and its empty-stderr row prints `(no stderr)`, with no
  `Traceback`.
  Red when: a start failure propagates, or the refusal line differs by builder.

## 7. Gates

`recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted loop legs this pass keeps green, outside the base manifest, each declared by the unit
that mints it: `loop budget fixtures`, `loop breakpoints fixtures`, `loop position fixtures`, the leg
`loop guard fixtures` and the leg `loop selftest`, none of them a leg at HEAD.

New arm: tools/loop/guard.py · covers AC2 AC6 AC22 · the usage-line-less and exit-128 probe rows, the tree-fatal unparseable-parent plant and the start-failure and empty-stderr rows, each staged as its criterion's Red when · none
New arm: tools/loop/budget.py · covers AC10 AC13 AC21 · the conf-read-forms rows moved inside the boundary, the annotated, Path and star-import bindings, and the tree_lib lacking derive_docstring_ids, each staged as its criterion's Red when · none
New arm: tools/loop/position.py · covers AC9 · the url-forms fetch with the credential helper clearing staged out · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Repair M4 by folding the boundary into 76, building 80 in 76's pass, or moving the observation
  (ids 11, 17)?** (a) fold 80 into 76 as a rev bump; (b) one pass for 76 and 80; (c) move 76 AC1's exit-0
  half and 79 AC10's re-observation to 80's pass commit. (a) and (b) rewrite two audited units' scope or
  dispatch from a batch that builds after both; (c) is id 11's own alternative, judged sound for AC1, and
  S5 extends it to 79 AC10 as the skeptic's correction requires. RESOLVED (agent, 2026-10-24, delegated):
  (c), S4 and S5. widens: none · relaxes: none
- **F3 — Where does `derive_conf_reads` find loop_lib (ids 5, 28)?** (a) the `loop_lib.py` beside the
  scanned module; (b) an explicit `loop_lib_path` argument defaulting to the kit's own. Both satisfy
  AC13 and AC15; (b) adds a parameter every caller can mis-pass, and (a) is M12's fix. RESOLVED (agent,
  2026-10-24, delegated): (a), S13 and S15. widens: none · relaxes: none
- **F4 — Clear the credential helpers on the fetch call itself, or rely on 75 S34's empty system and
  global configs (id 23)?** (a) `-c credential.helper=` with prompting off on the fetch; (b) state that
  the fetch inherits 75 S34's environment. Both keep the store untouched when built as stated. (b) rests
  the guarantee on another scope item's environment reaching one call, which is the gap the finding
  measured; (a) holds wherever the fetch runs and AC9 observes the store. RESOLVED (agent, 2026-10-24,
  delegated): (a), S9. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-6 spec audit's 22 minors batched (13 MEDIUM, 9 LOW).

## 10. Reuse audit

Each item extends the seam its finding names, never a parallel copy: 85's `check_write_tree_usage` (S2),
81's `failed` grade and `push-merge-tree-fatal` plant (S6, S22), 76's and 82's `derive_conf_reads` and
80's boundary (S10, S13, S21), 77's and 82's `url-forms` plant (S9), the run-gates kit's
`held_halves.load_manifest` and `derive_leg_argv` for the pass-commit probe (S8), `check_guard_trips`
(S12), and the loop kit's existing `resolve_kit_dir` route to `tree_lib` (S21).
`python tools/codebase-map/reuse_lookup.py "probe whether a git subcommand supports an option, distinguishing a failed probe"`
ranked `git`, `probe`, `run_git` and `LaunchFailed`, none a three-way capability answer, so S2 extends
85's predicate. The run-gates manifest reader was found by reading `measure_legs.py:472-480`, whose
docstring calls `load_manifest` the kit's one manifest reader; no second reader is minted.
No existing seam fits `derive_conf_constants`: the conf-name constant kind is 82's and lives beside
`derive_conf_reads`.

Recall terms used: spec-audit minors batch derive_conf_reads conf constant load_manifest credential helper probe failed pass-commit probe
