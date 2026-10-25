# TOOL-dGroundRules-79 — govkit selfcheck green over this build: the policy fixtures guard's two root-level lines get a declared class, and four policy-kit sentences stop failing the re-render rule

**Status:** DEFERRED · rev-1 · 2026-10-25 · node d · Tier-1 · base fae6e637 · streams tooling · order 27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-prompt-TOOL-dGroundRules-79-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-79-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-79-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-79-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

At the close, the `govkit selfcheck` leg exits 1 over this repository, and the govkit selftest fails
70 arms that each start from a green selfcheck. Six problem lines fail it, and this unit clears all
six. Two are check 7c. The `policy fixtures` guard lines `AGENTS.md` and `help/policy.md` fall into
no declared guard class. Four are check 7l. A sentence in each of four policy-kit files says
`update` re-renders without naming `GOVKIT_RERENDER`. This unit gives each of the two guard lines
exactly one class by the taxonomy's own rule, and respells the four sentences. No checker changes.

## 2. Scope (IN)

- **S1** — Two `[[exempt]]` rows in `tools/govkit/registry.toml`, one for `AGENTS.md` and one for
  `help/policy.md`. They go after the last `[[exempt]]` row, `.githooks/straggler-guard.test.sh`
  (`tools/govkit/registry.toml:323-325`), and before the first `[[exempt_leg]]`
  (`tools/govkit/registry.toml:327`), in the text §4 "The rows" gives. Observed by AC1 and AC2.
- **S2** — Four sentences respelled in the text §4 "The sentences" gives, and no other prose. They
  are the `[[regenerate]]` sentence under the `## The adopter` heading of `tools/policy/README.md`,
  the same sentence in the header comment of `tools/policy/adopt-policy.sh`, the comment above
  `[[regenerate]]` in `tools/policy/kit.toml`, and the landing-order comment in the
  `mirror-landed-merge` branch of `run_mirror_landed` in `tools/policy/check_policy.py`. Observed by
  AC1, AC3 and AC4.

## 3. Non-goals (OUT)

- `tools/govkit/govkit.py`. Check 7c's six classes and check 7l's predicate stay as they are. This
  unit only gives them input they accept.
- `tools/gate-legs.json`. Both guard lines stay in the `policy fixtures` guard, for the reason §4
  "Why the guard lines stay" gives.
- `help/policy.md` and `AGENTS.md` themselves. S1 classes them and edits neither.
- The selfcheck's `reported, not repaired` version-constant lines, which do not fail it. Also any kit
  version move: `kit epoch` prints it as owed at the lander.
- Any other spec. `TOOL-dGroundRules-73` and `-78` also edit `tools/policy/README.md`, and `-73`,
  `-75`, `-76` and `-77` edit `tools/policy/check_policy.py`. None of them edits the sentences S2
  names, so S2 locates each one by heading or symbol, not by line.

### Edges

none

This unit carries out the follow-through of `TOOL-dGroundRules-67` (CLOSED), which added `AGENTS.md`
to the `policy fixtures` guard, and of the units that wrote the policy kit's re-render prose. It
changes nothing those units built.

## 4. Design

### Evidence

Measured at `fae6e637f`. The `govkit selfcheck` leg is a gate this role may not run (scratch-guard
refuses it by its row in `tools/gate-legs.json`). So the two checks that red were run by the probe
§5 gives, `p79.py`. It imports `tools/govkit/govkit.py` and executes the source of check 7c
(`tools/govkit/govkit.py:2544-2584`) and of check 7l's prose half
(`tools/govkit/govkit.py:3612-3668`), read from that file at run time, over gov's registry and
descriptors. It printed the same six problems the main loop's selfcheck printed at `fce5603f8`, and
`6 problem(s)`.

Check 7c gives each guard pathspec of gov's own manifest the classes it matches
(`tools/govkit/govkit.py:2564-2579`). The classes are `memory-root-relative` (under `memory/`),
`verbatim-repo-root` (under `.githooks/` or `.claude/`), `renamed` (under `skills/session-kickoff/`),
`exempt` (an `[[exempt]]` row's path, or under it), `kit-relative` (under a kit directory or the
tool root `tools/`, `:2560`) and `root-conf` (a member of `derive_root_confs`,
`tools/govkit/govkit.py:1653-1667`). It reds any count but one (`:2580-2584`). `AGENTS.md` and
`help/policy.md` match none of the prefixes. No `[[exempt]]` row names them. `derive_root_confs`
over gov's descriptors is `.codebase-map.conf`, `.lexicon.conf`, `.memory-tree.conf`,
`.process-monitor.conf` and `.unattended.conf`. So both count zero.

Check 7l walks every tracked file of each kit declaring `[[regenerate]]`, plus its descriptor. It
joins each paragraph with comment leaders stripped, splits it into sentences, and reds a sentence
that names `update` and a re-render word but not `GOVKIT_RERENDER` (`:3612-3616`, `:3648-3665`).

### Why the guard lines stay

The brief allows showing that a guard line belongs elsewhere. It does not. `check_guard_trace` in
`tools/policy/check_policy.py` reds every source file a `--fixture` case reads that trips no
`policy fixtures` guard. The cases read both files: `derive_role_body_plant` reads `AGENTS.md` from
the source top, and `run_fresh_target` reads `help/policy.md` for its deferral line. With either
line out of the guard, the leg reds on its own trace. So the guard lines are right, and the taxonomy
needs a class for them.

### Which class

`exempt`, through the declaration that class already reads. A registry `[[exempt]]` row carries a
non-empty reason (the comment above the rows, `tools/govkit/registry.toml:189-191`), and the rows'
reasons each say why the path is gov's own and deliberately not shipped (for example
`tools/govkit/registry.toml:194-195` and `:304-305`). Both files are exactly that. `AGENTS.md` is gov's own rendered
charter: the playbook kit renders each adopter its own (`tools/playbook/kit.toml:53-55`, its
`[[regenerate]]` writing `AGENTS.md`), and no descriptor ships gov's. `help/policy.md` is gov's own
help page, and no descriptor ships anything under `help/`. The class predicts the emitter correctly.
The leg is an `[[exempt_leg]]` (`tools/govkit/registry.toml:686-688`), so no descriptor carries it
and the emitter never reads these guards. Were it emitted, the emitter keeps a guard only where it
matches a tracked path in the target (`tools/govkit/govkit.py:4384-4392`), which a gov-only path
never does.

Neither file is `root-conf`. That class is the set of root files a kit declares as the `file` of its
`[config]` table, and check 7c2 makes every guarded bar leg whose argv reads one name it
(`tools/govkit/govkit.py:2586-2591`). Widening it to `AGENTS.md` would grade every such leg on a
file that is no conf.

### Every reader of the declaration

The registry's `[[exempt]]` rows are read in five places. None of the others changes its verdict
for these two rows.

- `load_registry` (`tools/govkit/govkit.py:260-264`) resolves the `{prefix}` token in each path. These
  paths carry none, so they pass through unchanged.
- Check 7c (`tools/govkit/govkit.py:2561`, `:2574-2576`): the class this unit is for.
- Check 7i (`tools/govkit/govkit.py:3378`, `:3394`) skips an exempt path among the files inside a
  non-flat entry's home. Neither file is inside any home.
- Check 8 (`tools/govkit/govkit.py:3684-3708`) reds an exemption with no reason or a missing path, and
  subtracts exemptions from the surface. Both rows carry a reason, and both paths are tracked. Neither
  path is in the surface globs (`tools/govkit/registry.toml:25-31`), so the unclaimed count does not
  move. The note's exemption count goes from 28 to 30.
- `tools/check-playbook-parity.sh:184-185` reads only rows whose path starts `{prefix}/`, so it skips
  both.

The playbook kit ships `tools/govkit/registry.toml` to adopters as an engine file
(`tools/playbook/kit.toml:36-40`). Its renderer reads no `[[exempt]]` row, so the two rows reach an
adopter's copy and change nothing it does.

### The rows

S1 inserts these lines, blank line included, directly above the first `[[exempt_leg]]`:

```
[[exempt]]
path = "AGENTS.md"
why = "gov's own rendered charter, deliberately not shipped: the playbook kit renders each adopter its own. It lies outside the declared surface, so this row narrows nothing there. It is the class selfcheck's guard taxonomy (check 7c) gives the `policy fixtures` guard line naming it, a gov-only leg (its `[[exempt_leg]]` row) whose cases read the file. TOOL-dGroundRules-79."

[[exempt]]
path = "help/policy.md"
why = "gov's own help page for the policy kit, deliberately not shipped: an adopter writes its own pages under its own help directory. It lies outside the declared surface, so this row narrows nothing there. It is the class selfcheck's guard taxonomy (check 7c) gives the `policy fixtures` guard line naming it, a gov-only leg (its `[[exempt_leg]]` row) whose cases read the file. TOOL-dGroundRules-79."

```

### The sentences

Three sentences claim the regenerate runs on every update, and with `GOVKIT_RERENDER=0` exported it
does not. Each gains the condition in the words `tools/playbook/README.md` and
`tools/branch-reconcile/README.md` already use, and keeps its meaning and its citation.

Under `## The adopter` in `tools/policy/README.md`, the line that holds the sentence's verb and its
`(TOOL-dGroundRules-21 S37)` citation becomes two lines. The line before it, ending
`` `kit.toml`'s ``, stays:

```
`[[regenerate]]` runs the same verb on every update unless `GOVKIT_RERENDER=0` is exported
(TOOL-dGroundRules-21 S37). `--check [--target
```

In the header comment of `tools/policy/adopt-policy.sh`, the two lines from the one citing
`(TOOL-dGroundRules-34 S20)` to the one naming `check_policy.py --repo <repo>` become:

```
# file invalid, which exits 2 printing its findings (TOOL-dGroundRules-34 S20). `[[regenerate]]` in
# kit.toml runs this same verb on every update unless `GOVKIT_RERENDER=0` is exported
# (TOOL-dGroundRules-21 S37). `--check` is `check_policy.py --repo <repo>`, whose exit it returns.
```

In `tools/policy/kit.toml`, the two comment lines directly above `[[regenerate]]` become:

```
# `--scaffold` IS the re-render: on every update, unless GOVKIT_RERENDER=0 is exported, it re-runs
# the settings render over a kept policy file, so a changed renderer reaches every adopter
# (TOOL-dGroundRules-21 S37).
```

The fourth hit is not a claim about `govkit update`. Check 7l's paragraph runs across the whole
`mirror-landed-merge` branch of `run_mirror_landed`, which has no blank line. So one "sentence" spans
the comment's `the mirror regenerated over the merge` and the code's `"update-ref"` many lines below,
and `\bupdate\b` matches inside `update-ref`. Naming `GOVKIT_RERENDER` in a comment about the
lander's landing order would put a false statement there. So that comment's word `regenerated`
becomes `written again`, which is what the step does (`policy.py mirror --write` over the merge).
The comment line reads:

```
            # --no-ff onto main detached, the mirror written again over the merge, the merge rewritten by
```

### What this does not check

AC1 runs only checks 7c and 7l. The `govkit selfcheck` leg and the govkit selftest, which the close
runs, grade everything else, including whatever the units built before this one add to the policy
kit's prose or to `tools/gate-legs.json`. Check 7l does not grade a sentence's truth, only that it
names the flag. The `exempt` class does not check that a gov-only path is really absent from every
adopter.

### Alternatives rejected

- A seventh, derived class in check 7c. One option is root files a kit's `[[regenerate]]` writes.
  That set holds `.memory-tree.conf` (`tools/memory-tree/kit.toml:231`), which is already
  `root-conf`, so the class would need a carve-out. It would also leave `help/policy.md` with no
  class, and adding the playbook's help-directory default instead would make an adopter's own
  placeholder a gov class. Either way it is a code change, plus a selftest arm, for two gov-only
  paths the existing class already describes.
- Taking the two lines out of the guard. `check_guard_trace` reds the leg (§4 "Why the guard lines
  stay").
- Naming `GOVKIT_RERENDER` in the `check_policy.py` comment. It would satisfy the predicate with a
  false sentence.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.
No help page changes: nothing a user runs behaves differently.

### Files touched (estimate)

- `tools/govkit/registry.toml`
- `tools/policy/README.md`
- `tools/policy/adopt-policy.sh`
- `tools/policy/kit.toml`
- `tools/policy/check_policy.py`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree. The criteria use two scratch
scripts. `p79.py` imports govkit from the tree it is given, and executes check 7c and check 7l's
prose half from `tools/govkit/govkit.py` itself, cut by their own comment anchors, so it runs the
selfcheck's code and not a copy. It prints each problem, then the count. A missing anchor raises, so
a moved block reds the probe rather than passing it.

```
cat > "$TEMP/p79.py" <<'EOF'
import pathlib, sys, textwrap
root = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root / "tools" / "govkit"))
import govkit
src = (root / "tools" / "govkit" / "govkit.py").read_text(encoding="utf-8")
def block(a, b):
    i = src.index(a); j = src.index(b, i)
    return textwrap.dedent(src[src.rindex("\n", 0, i) + 1:j])
reg = govkit.load_registry(root)
r = govkit.Report()
ns = dict(vars(govkit), root=root, reg=reg, exempts=reg.get("exempt", []), r=r,
          descs=govkit.read_descriptors(root, reg, govkit.Report()))
exec(block("# ---- 7c: every guard pathspec", "# ---- 7c2:"), ns)
exec(block("_rr_lead = re.compile", "# ---- 8: the SURFACE"), ns)
for p in r.problems:
    print(p[:120])
print(f"{len(r.problems)} problem(s)")
EOF
```

`f79.sh` copies the worktree's tracked `tools`, `.governance`, `AGENTS.md` and `help` into the
scratch repository it is given, and stages them, because check 7l lists a kit's files from the
index. A second argument stages one break: `a` points the `AGENTS.md` row at another path, which
takes its class away. `k` puts back `tools/policy/kit.toml`'s old sentence, and `c` the old
`check_policy.py` comment. It then runs `p79.py` there and cuts each line at its first ` — ` or
` (kit `:

```
cat > "$TEMP/f79.sh" <<'EOF'
d="$1"; rm -rf "$d"; mkdir -p "$d"
git ls-files -z -- tools .governance AGENTS.md help | tar --null -T - -cf - | tar -xf - -C "$d"
case "${2:-}" in
  a) sed -i 's#^path = "AGENTS.md"#path = "AGENTS.md.x"#' "$d/tools/govkit/registry.toml" ;;
  k) sed -i 's/on every update, unless GOVKIT_RERENDER=0 is exported, it re-runs/on every update it re-runs/' "$d/tools/policy/kit.toml" ;;
  c) sed -i 's/the mirror written again over the merge/the mirror regenerated over the merge/' "$d/tools/policy/check_policy.py" ;;
esac
git -C "$d" init -q; git -C "$d" config core.longpaths true; git -C "$d" config core.autocrlf false
git -C "$d" add -A 2>/dev/null
python "$(dirname "$0")/p79.py" "$d" | sed 's/ — .*//; s/ (kit .*//'
EOF
```

The `govkit selfcheck` leg and the govkit selftest are gates this pass may not run. The main loop
runs both at the close: the selfcheck exits 0, and the selftest prints none of the 70 failures it
printed at `fce5603f8`.

- **AC1** — When `python "$TEMP/p79.py" .` runs, it prints exactly one line, `0 problem(s)`.
  At `fae6e637f` it printed the two check-7c lines naming `AGENTS.md` and `help/policy.md`, the four
  check-7l lines naming `tools/policy/README.md`, `tools/policy/adopt-policy.sh`,
  `tools/policy/check_policy.py` and `tools/policy/kit.toml`, and `6 problem(s)`.
  Red when: the class is taken away. Then `bash "$TEMP/f79.sh" "$TEMP/r79" a` prints the line `guard pathspec 'AGENTS.md' (leg 'policy fixtures') falls into 0 declared classes [], not exactly one` and `1 problem(s)`.
  Red also when a respelled sentence goes back: `bash "$TEMP/f79.sh" "$TEMP/r79" k` prints `'tools/policy/kit.toml'` and `1 problem(s)`, and `bash "$TEMP/f79.sh" "$TEMP/r79" c` prints `'tools/policy/check_policy.py'` and `1 problem(s)`.
  With no break, `bash "$TEMP/f79.sh" "$TEMP/r79"` prints `0 problem(s)`. All four were measured on a
  scratch copy of `fae6e637f` with S1 and S2 applied.
- **AC2** — When `grep -cx -e 'path = "AGENTS.md"' -e 'path = "help/policy.md"' tools/govkit/registry.toml` runs, it prints `2`.
  At `fae6e637f` it printed `0`.
  Red when: either row is missing, or the class came from somewhere other than the `[[exempt]]`
  declaration S1 names.
- **AC3** — When `grep -c 'GOVKIT_RERENDER=0 is exported' tools/policy/README.md tools/policy/adopt-policy.sh tools/policy/kit.toml` runs, it prints `1` for each file.
  At `fae6e637f` it printed `0` for each.
  Red when: a sentence S2 names was not respelled, or was respelled in other words than §4 gives.
- **AC4** — When `grep -c 'the mirror written again over the merge' tools/policy/check_policy.py` runs, it prints `1`, and `grep -c 'the mirror regenerated over the merge' tools/policy/check_policy.py` prints `0`.
  At `fae6e637f` they printed `0` and `1`.
  Red when: the comment still reads `regenerated`, or was respelled to name the flag.

## 6. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `policy check` · `playbook parity` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

Run through `derive_guarded_legs` at `fae6e637f`, `python tools/check-spec-tokens.py --legs-for`
names these non-broad guarded legs. `tools/govkit/registry.toml` trips `govkit selftest`,
`govkit refusal join`, `govkit acceptance matrix` and `recall floor arms` through `tools/govkit/`, and
`policy fixtures` through its own exact line. Each of the four policy-kit files trips
`policy fixtures` through `tools/policy/`. Every other leg it prints trips only on the broad `tools/`.

Four legs named beside them carry no guard and read what this unit changes. `govkit selfcheck` is the
leg this unit makes green. `policy check` runs `tools/policy/check_policy.py` in its live mode.
`playbook parity` reads the registry's `[[exempt]]` rows, and skips these two. `kit epoch` reads the
shipped bytes of the policy kit and of the playbook kit, which ships the registry, and prints the
move as owed at the lander.

No arm is added or moved, so this unit declares no new suite arm. The red is the main loop's run of
the `govkit selfcheck` leg at `fce5603f8`, and AC1's staged breaks red the two checks again. No floor
moves.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from this unit's spec brief, grounded at `fae6e637f`. The
  selfcheck could not be run by this role, so its two failing checks were run from their own source
  by `p79.py`, at the worktree and on a scratch copy with S1 and S2 applied. That reproduced the six
  lines, then zero, then one line per staged break. The guard lines were kept because the leg's own
  guard trace reds without them, and they were classed through the existing `exempt` declaration
  rather than a new class (§4 "Which class"). The brief asked for all four sentences to name
  `GOVKIT_RERENDER`. The `check_policy.py` hit is a code comment about the lander that 7l joins to a
  far-off `update-ref` call, so naming the flag there would be false. Its claim word is respelled
  instead, which clears the line and keeps the comment true. The brief assumed the pass may run the
  selfcheck. Scratch-guard refuses it to role agents, so AC1 is the probe and the leg runs at the
  close. The brief, untracked when this draft was written:

```
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-79-spec-brief.md
```

## 9. Reuse audit

This unit builds no mechanism. S1 extends the declaration check 7c already reads for its `exempt`
class, the registry's `[[exempt]]` rows (`tools/govkit/registry.toml:189-325`), with two rows in the
existing shape. S2 reuses the condition other kits already use in these sentences,
`unless GOVKIT_RERENDER=0 is exported` (`tools/playbook/README.md:136`,
`tools/branch-reconcile/README.md:167`). The probe runs the selfcheck's own source and does not
retype a predicate.
`python tools/codebase-map/reuse_lookup.py "classify a guard pathspec into exactly one declared class for a root file no kit ships"`
ranked only name stems (`repo_root`, `resolve_kit_dir`, `kit_rel`, `classify`), and none of them
classes a guard pathspec. The seam is check 7c's own declaration. The recall probe returned
`TOOL-aWalkedCorpus-5` and `TOOL-dDerivedDocket-21`, which added the `root-conf` class for kit
confs, plus this unit's own brief and run row. No record classes a gov-only root file.

Recall terms used: `python tools/memory-recall/query.py "guard pathspec falls into declared classes exempt root-conf AGENTS.md help page GOVKIT_RERENDER sentence" --terms "7c root-conf exempt derive_root_confs GOVKIT_RERENDER 7l policy fixtures guard"`
