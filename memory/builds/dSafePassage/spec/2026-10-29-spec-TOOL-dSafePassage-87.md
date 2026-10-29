# TOOL-dSafePassage-87 — the round-2 closing review's seven mediums and two lows, each closed at the fix its skeptic judged sound

**Status:** CLOSED · rev-4 · 2026-10-29 · node a · Tier-2 · base cba885c5 · streams tooling · order 16 · advances TOOL-dSafePassage-14 · ratified 2026-10-29

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dSafePassage-87-ledger.md](../build/2026-10-29-build-TOOL-dSafePassage-87-ledger.md) | journal | — |
| [2026-10-29-prompt-TOOL-dSafePassage-86-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-86-spec-brief.md) | research | TOOL-dSafePassage-86 |
| [2026-10-29-prompt-TOOL-dSafePassage-87-1-spec-writer.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-87-1-spec-writer.md) | journal | — |
| [2026-10-29-prompt-TOOL-dSafePassage-87-audit-fold-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-87-audit-fold-brief.md) | research | TOOL-dSafePassage-89 TOOL-dSafePassage-88 |
| [2026-10-29-prompt-TOOL-dSafePassage-87-build-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-87-build-brief.md) | journal | — |
| [2026-10-29-review-TOOL-dSafePassage-86-87-89-88-closing-diff-round3.md](../reviews/2026-10-29-review-TOOL-dSafePassage-86-87-89-88-closing-diff-round3.md) | diff-review | TOOL-dSafePassage-86 TOOL-dSafePassage-89 TOOL-dSafePassage-88 |
| [2026-10-29-review-TOOL-dSafePassage-86-87-89-88-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dSafePassage-86-87-89-88-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-86 TOOL-dSafePassage-89 TOOL-dSafePassage-88 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 closing diff review confirmed nine minor defects in the round-1 fix units. Each is a
guard weaker than its spec, a refusal whose remedy does not apply, or a guard no arm holds. This
unit closes all nine, M1 to M7 and L1 to L2 (ids 1, 3, 4, 8, 9, 10, 14, 11, 12), each at the fix the
skeptic judged sound. For M1 that is the skeptic's corrected fix. Each fix is held by an arm that is
red against the break the review names. The review batches them into one unit because their write
sets overlap (BUILD-METHOD M4), and the batch builds after TOOL-dSafePassage-86.

The round-1 spec audit of units 86 to 89 adds two more items here, S11 and S12. S11 roots gov's own
shim rows at the target's prefix. S12 points `derive_release_engine` at the shared tool-path seam.
TOOL-dSafePassage-86 was built before that audit, so its one item lands in this unit, which edits the
same file after it.

## 2. Scope (IN)

- **S1** — M1 (id 1), a `..` key is refused before containment is tested. `check_contained`
  (`tools/govkit/upgrade_steps.py:1068`) refuses a `rel` that has a `..` segment once `\` is folded to
  `/`. The test runs after `derive_contained_rel`'s `None` refusal (`:1076-1077`) and before the link
  walk (`:1079`). `derive_contained_rel` (`:1056-1065`) stays govkit's shared destination predicate,
  as it is (`govkit.py:1243`). The `[dSP-72]` block of `check_upgrade_steps` (`selftest.py:3144`)
  gains `[dSP-87 AC1]` checks for `a/../b` and for `lnk/../x` through a planted link. `BRANCH_PIN`
  (`tools/govkit/refusal_join.py:41`) rises by the measured delta. The before-image bullet of
  `help/upgrade-steps.md` (`:322-326`) names the segment. §4 "S1". Observed by AC1 and AC2.
- **S2** — M2 (id 3), the dirty-engine refusal sees both sides of a move. `check_tree_clean`
  (`tools/govkit/upgrade_walk.py:927-939`) runs `git status --porcelain -z --no-renames` and grades
  every NUL-separated entry, so a staged rename reads as its own `D` and `A` rows.
  `check_grade_tree_clean` (`:1000-1015`) gains a staged `git mv` of an engine file into
  `fixtures/release-0` and requires the old path back. §4 "S2 and S3". Observed by AC3.
- **S3** — M5 (id 9), the `lib` half of the pathspec is graded. `check_grade_tree_clean` also commits
  a file under the sibling `lib` directory, edits it, and requires exactly that path back. §4 "S2 and
  S3". Observed by AC4.
- **S4** — M3 (id 4), the floor stub resolves bash as the parent did. `STEP_ENV_KEEP`
  (`upgrade_steps.py:179-181`) gains `GOV_BASH`, with a reviewed comment beside 75's
  (`:176-178`). `tools/govkit/steps/python_floor.py` (`:35`) builds its argv with
  `steps.resolve_shell_argv(["bash", ...])` in place of `[steps.resolve_bash(), ...]`. That honours
  the override, and it falls back to bare `bash` on a `Refusal`, as the parent's argv did before
  TOOL-dSafePassage-82. Its docstring (`:6-8`) says so. `check_step_isolation` gains a
  `[dSP-87 AC5]` check beside `[dSP-75]` (`selftest.py:4361-4380`). The clean-environment bullet of
  `help/upgrade-steps.md` (`:39-41`) names `GOV_BASH`. §4 "S4". Observed by AC5.
- **S5** — M4 (id 8), the quote-widened mutant has an arm. The `[dSP-74]` block of
  `check_upgrade_steps` (`selftest.py:3128-3142`) gains a third commit holding an escaped-id row, its
  slash spelled as a TOML unicode escape, and a multi-line literal-string row. Both must read that
  commit's sha. A staged copy of the engine
  carrying the quote-widened pre-filter, loaded the way `[dSP-53]` loads one (`selftest.py:4150-4165`),
  must read both rows as unlanded. §4 "S5". Observed by AC6.
- **S6** — M6 (id 10), the forward walk's image refusal names a remedy that applies. The
  working-tree refusal of `read_image_paths` (`upgrade_steps.py:2003-2005`) names a remedy for an
  image with no committed copy, beside the committed-copy remedy, per §8 F1. A walk plant
  `truncated-image-held` joins `WALK_PLANTS` (`:3632-3633`). It puts a cut-short image under a step
  whose witness holds, with no committed copy, and pins the refusal and the remedy's re-run. Its row
  joins the selftest's fixture table (`selftest.py:4469`), and the tagger (`:4542`) tags it `dSP-87`.
  The skip bullet of `help/upgrade-steps.md` (`:205-209`) names the refusal. §4 "S6". Observed by AC7.
- **S7** — M7 (id 14), one `{prefix}` token per tree. `read_fixture_rows` (`upgrade_walk.py:118-128`)
  resolves a `[[gov_plant]]` row against the working gov's tool root, which is the clone tip's
  layout. Every other kind (`plant`, `condition`, `arm`) names an adopter-target path, and it resolves
  against the target's install prefix, the `prefix` of `fixtures/release-0/deploy.toml`. The docstring
  (`:119-121`) states the two roots and makes no claim that they are equal. One new function,
  `read_target_prefix`, is the one reader of that `prefix` (audit L8, id 13). `read_fixture_rows`
  calls it, and so does `build_release_tree`, for the policy adopter's directory in the target
  (`:232`), where it read `derive_tool_root(clone)`. A `{prefix}` token in that field is a `Stop`.
  §4 "S7". Observed by AC8 and AC9.
- **S8** — L1 (id 11), the docs leg's `{prefix}` resolution runs off `tools`. `build_docs_fixture`
  (`tools/govkit/docs_leg.py:555`) gains the plant `scripts-prefix`. It lays the fixture out under
  `scripts`, spells the `[[usage]]` ids and entries `{prefix}/fx/...`, and spells the guide page's
  two commands `<prefix>/fx/...`. Its row joins `_docs_cases` (`selftest.py:19430-19456`) expecting
  `commands 2 tested`. §4 "S8". Observed by AC10.
- **S9** — L2 (id 12), the no-`<to>` control asserts its outcome. The gov-tree arm of
  `tools/lib/resolve-python.test.sh` (`:337-338`) asserts `rc = 1`, `python-floor down: mode`, the
  planted `planted.toml:` finding, and no `Traceback`, in place of `rc != 2`. §4 "S9". Observed by
  AC11.
- **S10** — The three page edits of S1, S4 and S6, in `help/upgrade-steps.md`. Each phrase AC12
  greps sits on one source line of the page. Observed by AC12.
- **S11** — Audit M4 (ids 19 and 15), gov's own shim rows are compared at the target's root.
  `check_shim_paths` (`upgrade_walk.py:553-579`) tests gov's rows against the target receipt
  (`:570-574`). It reads them with `shims.read_shim_rows(ctx["clone"], read_target_prefix())`.
  `read_shim_rows` (`tools/govkit/shims.py:60`) gains an optional `troot`, the tool root its
  `{prefix}` resolves against in place of the root's own (`:71`). `check_graders` gains a `shim-root`
  grader. §4 "S11". Observed by AC13.
- **S12** — Audit L7 (id 12), the release engine through the shared tool-path seam.
  `derive_release_engine` (`upgrade_walk.py:183-187`) returns
  `gk.resolve_tool_path(clone, gk.GOVKIT_DIR.name, "govkit.py")` (`tools/govkit/govkit.py:299-302`).
  TOOL-dSafePassage-86's `release-engine` grader (`upgrade_walk.py:1040-1049`) is not edited and stays
  green. §4 "S12". Observed by AC14.

## 3. Non-goals (OUT)

- A green `upgrade-walk` row in the foreign-prefix parity leg. With TOOL-dSafePassage-86 and S7 both
  staged, the walk at `scripts/` applies release-0 and its plants, and then stops at `read_steps`,
  which TOOL-dSafePassage-89 closes (§4 "Past the plants, measured"). Neither unit claims the row
  green.
- The bug-class checklist lines each finding's left-shift gate proposes, in either review. Both
  reviews record that no checklist exists, and each item's persisted arm here is its gate.
- The walked-target form of S11's observation: a `[[shim]]` row added to a moved clone's
  `shims.toml`, its forwarder deleted, read by the walk's `shims` case. At this unit's place in the
  build order the moved walk stops at `read_steps` first (the hands-off below), so it is observable
  only once TOOL-dSafePassage-89 has landed. The `shim-root` grader is this unit's observation.
- `derive_contained_rel`'s normalisation. The skeptic rejected the finder's fix, which changed the
  shared predicate, and govkit's `demand_contained_dest` keeps it.
- M6's other outcome, `write_before_image`'s tolerance in move 1. §8 F1 resolves against it.
- Spec 72's line 161, which says `a/../b` is "the path that is actually opened". Spec 72 is CLOSED and
  is not edited. S1 makes the claim moot.
- Passing the resolved bash to the floor stub as an argument (S4). It changes the step row's argv
  contract (§4 "Alternatives rejected").

### Edges

- **consumes-from** `TOOL-dSafePassage-86` — `derive_release_engine`, without which AC9's
  moved-prefix walk stops at release-0's apply and never reaches the plants S7 resolves
- **hands-off** `TOOL-dSafePassage-89` — the stop past the plants at a moved prefix (§4 "Past the
  plants, measured"): `read_steps` reads the registry under the pin's `tools` at a tip that holds
  `scripts`, because `derive_tool_root` answers the clone's first read. The same memo makes the
  `shims` case's tip read of gov's `shims.toml` refuse at a moved prefix until 89 lands, and S11
  keeps that comparison at one root once it does
- **hands-off** `TOOL-dSafePassage-88` — the moved-prefix walk past `read_steps`, whose `up` case
  needs S7's plant paths to reach `update`, where TOOL-dSafePassage-88 closes the third stop

## 4. Design

Every cited line holds at `cba885c58`, the build head with TOOL-dSafePassage-86 landed. Outside
`memory/` it differs from `b634d60e5` only in `tools/govkit/upgrade_walk.py`, so every other file's
lines are the same at both. Each break in the tables below was staged in a `git clone --no-hardlinks`
of `b634d60e5` under the temp root on 2026-10-29, and each fix was staged and measured green there.
The exceptions are the rows naming `cba885c58`. Those were measured on 2026-10-29 in a shallow clone
of `cba885c58` with `tools` moved to `scripts` by `git mv`, with S7, S11 and S12 staged as written
below.

### S1: the `..` refusal

In `check_contained`, between `:1077` and `cur = pathlib.Path(target)` (`:1078`):

```python
    if ".." in rel.replace("\\", "/").split("/"):
        raise Refusal(f"'{rel}' holds a '..' segment, which a step's own write resolves through any link "
                      f"on the segment before it, so no step may write it")
```

It sits after the `None` refusal so that an escaping form keeps the message
`is not a path inside the target`. The `[dSP-72] AC3` check (`selftest.py:3164-3176`) reads that
message for `..\ESCAPED.txt`, and a `..` test placed first would answer it with this one. It tests the
raw string, the one a step's own write `(target / p)` opens. The kernel resolves `lnk` before applying
`..`, so the normalised form is not what is opened.

The `[dSP-87 AC1]` checks sit after `[dSP-72] AC5` (`selftest.py:3221-3223`) and reuse that block's
`t72`, whose `lnk` is a link to `outside/` made by `write_link72` (`:3178-3182`), a junction on
Windows and `os.symlink` elsewhere:

```python
for rel87 in ("a/../b", "lnk/../planted.txt"):
    got87 = [read_refusal(lambda: steps.check_contained(t72, rel87))]
    write_image72(t72, "demo/dotdot", {rel87: pwned})
    got87.append(read_refusal(lambda: steps.read_image_paths(t72, "demo/dotdot")))
    check(f"[dSP-87 AC1] {rel87!r} is refused by check_contained and read_image_paths for its '..' segment",
          all("holds a '..' segment" in g for g in got87), str(got87))
```

The check carries no no-write conjunct (audit L5, id 9). `t72`'s `lnk` resolves before `..`, so the
second key names `planted.txt` directly under `root72` (`selftest.py:3184-3189`), not a file under
`outside/`. Neither `check_contained` nor `read_image_paths` writes. A test that `outside/` gained no
`planted.txt` could not fail, so the refusal message is the whole arm.

`[dSP-72] AC1`'s check of `derive_contained_rel("a/../b") == "b"` (`:3150-3154`) stays, since the
predicate does not change. `[dSP-72] AC4`'s last check, that `outside/` holds only `secret.txt`
(`:3215-3216`), runs before these and is not moved.

`BRANCH_PIN` counts refusal call sites (`refusal_join.py:305`). S1 adds one, so the pin rises from
334 to 335, with a comment in the shape of the 76 entry (`:42-50`): the matcher's count at this
unit's base and on the tree it leaves, and the `[dSP-87 AC1]` check that reaches the new site. S6
changes a message and adds no site. The builder re-derives the delta at both ends rather than
trusting this +1.

The page sentence at `help/upgrade-steps.md:322-324` reads, with `holds a ..` kept on one source line:

> A path a before-image lists, or the image's own path, is refused where it climbs out (`..`, or a
> backslash climb such as `..\x`), holds a `..` segment even one that stays inside, is rooted, UNC or
> on a drive, holds a colon, or passes through a symlink, a junction or any other reparse point.

The probe for AC1, `contain_probe.py`, run from the repository root:

```python
import os, pathlib, subprocess, sys, tempfile
sys.path.insert(0, "tools/govkit")
import upgrade_steps as s
root = pathlib.Path(tempfile.mkdtemp(prefix="p87c-"))
t, out = root / "target", root / "outside" / "deep"
t.mkdir()
out.mkdir(parents=True)
if os.name == "nt":
    subprocess.run(["cmd", "/c", "mklink", "/J", str(t / "lnk"), str(out)], capture_output=True, check=True)
else:
    os.symlink(out, t / "lnk", target_is_directory=True)
for rel in ("a/../b", "lnk/../x", "lnk/x", "..\\ESCAPED.txt", "a/b"):
    try:
        print(rel, "->", s.check_contained(t, rel).relative_to(t).as_posix())
    except s.Refusal as e:
        print(rel, "-> refused:", str(e).split(": ", 1)[-1][:70])
```

| `check_contained` over a target whose `lnk` is a junction | At `b634d60e5` | S1 staged |
|---|---|---|
| `a/../b` | returns `b` | refused, `holds a '..' segment` |
| `lnk/../x` | returns `x` | refused, `holds a '..' segment` |
| `lnk/x` | refused, a reparse point | the same |
| `..\ESCAPED.txt` | refused, `is not a path inside the target` | the same |
| `a/b` | returns `a/b` | the same |

### S2 and S3: the tree-clean grader

`check_tree_clean`'s command (`upgrade_walk.py:934`) becomes
`["git", "-C", str(gov_root), "status", "--porcelain", "-z", "--no-renames", "--untracked-files=no", "--", kit, lib]`,
and `:938` becomes `paths = [e[3:] for e in out.split("\0") if len(e) > 3]`. A `-z` entry is
unquoted, so the `.strip('"')` goes with the v1 parse. With `--no-renames`, no entry carries a second
path.

`check_grade_tree_clean` lays out two more files. One is `libf`, spelled as `check_tree_clean` spells
its `lib` (`:932`) plus `/x.sh`. The other is `engine`, `f"{kit}/engine.py"`. After the steps edit
(`:1012-1015`) it runs, in order:

1. `git checkout -q -- .`; append to `libf`; require `check_tree_clean(t, LEG_OWN) == [libf]`.
2. `git checkout -q -- .`; `git mv <engine> <kit>/fixtures/release-0/engine.py`; require
   `[engine]`.

The rename runs last because `checkout -- .` does not undo a staged move.

| `check_graders()` at `tools/` | Prints |
|---|---|
| S2 and S3 staged | `grader · tree-clean · ok`, `[]` |
| S3's grader, `lib` left out of the pathspec | `RED · tools/lib/x.sh edited, it returned []` |
| S2's grader, the v1 parse kept | `RED · tools/govkit/engine.py renamed into fixtures/release-0, it returned []` |

The grader row reads `ok` at `cba885c58` too, because the `tree-clean` grader is already wired
(`:1054`), so its run cannot tell whether S2 or S3 was built (audit M1, id 1). AC3 and AC4 therefore
observe each case by its own text: `--no-renames`, `engine.py` and `x.sh`. No line of
`upgrade_walk.py` holds any of the three at `cba885c58`, measured by `git grep`. The grader run is
their preservation half. The last two table rows are the build's probes: each is staged against the
built grader and must print its `RED ·` line.

### S4: the floor stub

`STEP_ENV_KEEP` ends `"GOV_PYTHON", "GOV_BASH")`. The comment after 75's sentence reads: `GOV_BASH`
joins (TOOL-dSafePassage-87). It names the bash `resolve_bash` tries first, so the floor stub runs
the shell the parent's `resolve_shell_argv` ran before TOOL-dSafePassage-82 moved the row to a
python argv. It carries no credential and is the same class of name as `PATH`.

`python_floor.py:35` becomes:

```python
    return subprocess.run(steps.resolve_shell_argv(["bash", (kit / FLOOR_SCRIPT).as_posix(), *argv])).returncode
```

`resolve_shell_argv` (`upgrade_steps.py:422-437`) catches `Refusal` and returns the argv unchanged, so
the stub no longer dies on an uncaught `Refusal`. The isolation fixture's allowlist reads
`STEP_ENV_KEEP` itself (`upgrade_steps.py:2929`), so `GOV_BASH` reaching a step's environment is not a
leak there.

The `[dSP-87 AC5]` check follows `[dSP-75]` and uses its `floor_row`, held and restored the same way.
It sets `PATH` to a scratch directory holding a `bash` and a `bash.exe` that are text files and do not
run. That directory is followed by every `PATH` entry that holds no `bash` or `bash.exe`, with a
`System32` or `WindowsApps` entry kept, since `resolve_bash` skips those (`:411-413`). It sets
`GOV_BASH` to the parent's `resolve_bash()` and `GOV_PYTHON` to `sys.executable`, and requires
`run_step_isolated(floor_row, "witness", GOV_ROOT, GOV_ROOT)` to read verdict `ok`, rc 0.

The probe for AC5 is the same body as a script, `floor_probe.py`, run from the repository root:

```python
import os, pathlib, sys, tempfile
sys.path.insert(0, "tools/govkit")
import upgrade_steps as us
G = pathlib.Path(".").resolve()
row = next(r for r in us.read_steps(G, None, None) if r.id == "lib/python-floor-3.15")
bash = us.resolve_bash()
fake = pathlib.Path(tempfile.mkdtemp(prefix="p87b-"))
for n in ("bash", "bash.exe"):
    (fake / n).write_bytes(b"not a program\n")
    (fake / n).chmod(0o755)
launcher = lambda d: any(s in d.replace("\\", "/").lower() for s in ("/system32", "/windowsapps"))
keep = [d for d in os.environ["PATH"].split(os.pathsep) if d and (launcher(d) or not any(
    os.path.isfile(os.path.join(d, n)) for n in ("bash", "bash.exe")))]
os.environ.update(PATH=os.pathsep.join([str(fake)] + keep), GOV_BASH=bash, GOV_PYTHON=sys.executable)
got = us.run_step_isolated(row, "witness", G, G)
print(got["verdict"], got["rc"], repr(got["tail"][-240:]))
```

| `floor_probe.py`, node a, Windows | Prints |
|---|---|
| at `b634d60e5` | `failed 1`, a tail ending `upgrade_steps.Refusal: govkit: no usable bash on PATH ... Set GOV_BASH.` |
| S4 staged | `ok 0 ''` |
| the stub changed, `GOV_BASH` not kept | `failed 127`, `/bin/bash: ...python-floor.sh: No such file or directory`, the WSL launcher |

The page's clean-environment bullet (`help/upgrade-steps.md:39-41`) reads "plus `GOV_PYTHON` and
`GOV_BASH`, the interpreter and shell overrides the resolvers read, so a step resolves the
interpreter and the bash gov's gates and hooks resolve on the same node".

### S5: the quote-widened arm

After the two `[dSP-74] AC2` checks (`selftest.py:3136-3142`), a third commit appends two rows to
`demo/kit.toml` in the scratch gov `g`. Their id lines are, as the file must hold them:

```toml
id = "demo/esc"
id = '''
demo/ml'''
```

The file holds the six characters `/` literally, a TOML unicode escape for the slash, so its raw
text never contains `"demo/esc"` and the widened filter cannot find the row (audit M3, id 8). A
literal `\/` is not a valid TOML escape. In `selftest.py`'s Python source the replacement is spelled
`'id = "demo\\u002Fesc"'`, with the backslash doubled. A single backslash lets Python decode the
escape to `/` before TOML sees the text, and the row is then the plain spelling: measured at writing
time, a probe written that way read both rows at `third` under the mutant below.

Each row is `render_row("demo/esc")` and `render_row("demo/ml")` with its id line replaced. The
newline after the opening `'''` is load-bearing. TOML trims it, so the id reads `demo/ml`, and the raw
text then holds no `'demo/ml'`. A one-line `'''demo/ml'''` holds `'demo/ml'` as a substring, and the
widened filter would find it. `settle(g, ...)` commits, and `third` is the new head.

The probe for AC6, `esc_probe.py`, imports the engine and asks `derive_introduced`
(`upgrade_steps.py:930`), the function `read_steps` reads `introduced` through and the one the mutant
sits in, about a scratch commit holding exactly the block above (audit L2, id 2). Its one optional
argument is the engine directory, `tools/govkit` by default. It is run from the repository root.

```python
import pathlib, subprocess, sys, tempfile
eng = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "tools/govkit").resolve()
sys.path.insert(0, str(eng))
import upgrade_steps as us
g = pathlib.Path(tempfile.mkdtemp(prefix="p87e-"))
git = lambda *a: subprocess.run(["git", "-C", str(g), *a], capture_output=True, text=True, check=True).stdout.strip()
git("init", "-q")
(g / "demo").mkdir()
(g / "demo" / "kit.toml").write_text('[[upgrade]]\nid = "demo\\u002Fesc"\n\n[[upgrade]]\nid = \'\'\'\ndemo/ml\'\'\'\n',
                                     encoding="utf-8", newline="\n")
git("add", "-A")
git("-c", "user.email=t@e", "-c", "user.name=t", "commit", "-qm", "third")
third = git("rev-parse", "HEAD")
got = us.derive_introduced(g, "HEAD", ["demo/kit.toml"], "upgrade", ["demo/esc", "demo/ml"])
print([(i, "third" if got.get(i, ("",))[0] == third else us.UNLANDED) for i in ("demo/esc", "demo/ml")])
```

| `esc_probe.py`, node a, 2026-10-29 | Prints |
|---|---|
| at `cba885c58` | `[('demo/esc', 'third'), ('demo/ml', 'third')]` |
| its argument a scratch copy of `upgrade_steps.py` carrying the mutant below | `[('demo/esc', 'unlanded'), ('demo/ml', 'unlanded')]` |

The engine at `cba885c58` already reads both spellings (TOOL-dSafePassage-74), so the first row is a
preservation check. The second is the red the probe can show: the engine with the pre-filter back.

```python
check("[dSP-87 AC6] an escaped id and a multi-line literal id each read the commit that added them",
      [(r.id, r.introduced) for r in steps.read_steps(g, "HEAD", "main")][-2:]
      == [("demo/esc", third), ("demo/ml", third)], ...)
```

The mutant inserts one line before the `try:` that parses `held` (`upgrade_steps.py:983`), at its
indentation:

```python
                if not any(f'"{i}"' in text or f"'{i}'" in text for i in want): continue
```

`build_staged_copy(tmp / "dsp87-quote-widened", src.replace(anchor, mutant + anchor))` writes it, and
it is loaded through `importlib.util.spec_from_file_location("us87_widened", ...)` as `[dSP-53]` loads
its copy. A second `[dSP-87 AC6]` check requires `src.count(anchor) == 1` and requires the copy's
`read_steps(g, "HEAD", "main")` to give `demo/esc` and `demo/ml` the introduced value `UNLANDED`
(`upgrade_steps.py:150`). So the arm holds the class: with the pre-filter back, the first check
reds.

### S6: the move-1 refusal

`read_image_paths`' working-tree message (`upgrade_steps.py:2004-2005`) reads:

```
<step id>: its before-image <rel> does not parse or lists no paths, so which paths its step wrote is
unknown; put back its committed copy, or where none is committed, remove it, which gives up the
before bytes it held; then run again
```

It keeps the prefix `does not parse` that the `[dSP-76]` check reads (`selftest.py:3114-3116`). Its
callers are move 1 (`:2089`), move 5 (`:2107`) and the down (`:2255`). The remedy is true at each: a
down run again with no image restores nothing, and `derive_down_verdict` reads that case already
(`:2183`). `git grep` finds no reader of the old words outside `upgrade_steps.py`.

The plant `truncated-image-held`, in `run_walk_fixture` (`upgrade_steps.py:3834`) beside
`witness-holds` (`:3892-3901`):

1. `t = build_case_target("t", files={"s2.txt": "s2\n"})`, so s2's witness holds.
2. Write s2's image cut short, as `truncated-image` cuts s3's (`:4020-4027`). It is not committed.
3. `rc, out = scan(t)`. Print `walk: held · rc <rc> · remedy <named|absent>`, and require rc 1, `out`
   naming `s2.before.json does not parse`, and `where none is committed, remove it`.
4. Unlink the image, run `rc, out = scan(t)` again, and print `walk: held · after the remedy · fx/s2 <state> · rc <rc>`.
   Require rc 0 and `step fx/s2 · skipped (witness holds)`.

The table row is
`("walk", "truncated-image-held", 0, ("walk: held · rc 1 · remedy named", "walk: held · after the remedy · fx/s2 applied · rc 0"))`,
and the tagger gains `else "dSP-87" if plant == "truncated-image-held"`.

The skip bullet (`help/upgrade-steps.md:205-209`) gains: "Where a step's before-image does not parse
and its witness holds, the walk stops with exit 1 naming the image: put back its committed copy, or
where none is committed, remove it, then run again."

### S7: the two roots

One reader of the target's install prefix, above `read_fixture_rows` in the rows section
(`upgrade_walk.py:117`):

```python
def read_target_prefix() -> str:
    """TOOL-dSafePassage-87 S7: the release-0 target's install prefix, `prefix` in FIXTURE's
    `deploy.toml`, the one reader of that field: the target's plants, gov's own shim rows and the
    policy adopter's directory in the target all resolve against it. A literal: the plants are read in
    `main` before the clone a `{prefix}` token would resolve against exists, so a token is a Stop."""
    prefix = tomllib.loads((FIXTURE / "deploy.toml").read_text(encoding="utf-8")).get("prefix")
    if not isinstance(prefix, str) or "{" in prefix:
        raise Stop(f"{FIXTURE.name}/deploy.toml: prefix {prefix!r} is not a literal path, and the target's "
                   "plants resolve against it before any tool root exists to resolve a token")
    return prefix
```

In `read_fixture_rows`, `:124` becomes:

```python
    # S7: a [[gov_plant]] edits gov's tree, at the clone tip's tool root, HEAD's own; every other kind
    # names a path in the target, installed at deploy.toml's `prefix`.
    troot = gk.derive_tool_root(gk.repo_root()) if kind == "gov_plant" else read_target_prefix()
```

In `build_release_tree`, the policy adopter's directory (`:232`) reads
`gk.resolve_kit_dir("policy", adopter, t / read_target_prefix())`, where it read
`t / gk.derive_tool_root(clone)`. That is a directory in the target, so it reads the target's root.
Both answer `tools` at every prefix the leg moves to, because the pin holds `tools` and the leg moves
only the tip.

`read_target_prefix` reads `FIXTURE`'s `deploy.toml` (`upgrade_walk.py:44`), the file
`build_release_tree` installs the target from (`:213-214`), and not the `fixture` argument. The
`fixture-keys` grader passes a scratch fixture with no `deploy.toml` (`:1023-1038`), and a read of
`fixture / "deploy.toml"` measured `grader · fixture-keys · RED · it raised FileNotFoundError`.

`build_release_tree`'s read at `:213-214` stays the reader of the target's answers. It resolves their
`{prefix}` against the pin's tool root. The `prefix` field it also carries is a literal, because
`read_target_prefix` stops on a token, and `main` reads the plants through it before
`build_release_tree` runs (`:1110-1112`). So the install and the plants read one value (audit L8).
`deploy.toml:8` spells `prefix = "tools"` today. The `Stop` is not a refusal site:
`refusal_join.py` counts only `raise Refusal(...)` and `.fail(...)` (`:268-278`).

Every target-path comparison in the walk reads one root, the target's install prefix (audit M4):

| Comparison | One side | The other side |
|---|---|---|
| `check_walk_exit` (`:312-330`) | the held paths `update` prints, the target's receipt paths | `ctx["ordered"]` (`:1113`), the plants' paths by S7 |
| `check_plant_rows` (`:506-548`) | the walked target and its outbox orders | each plant's `path` by S7 |
| `check_shim_paths` (`:570-574`) | the target receipt's `path`s | the arms' shim `from` by S7, and gov's own rows' `from` by S11 |
| `resolve_arm_rows` (`:907`) | an arm step's command, run in the target | `{shim:<arm>}`, the arm's shim `from` by S7 |

| AC8's `python -c`, from the moved `scripts/govkit` | Prints |
|---|---|
| at `cba885c58` | `README.md` under `scripts/memory-tree`, then `kit.toml` under `scripts/hooks` |
| S7 staged | `tools/memory-tree/README.md`, then `kit.toml` under `scripts/hooks` |

| At `scripts/`, with 86 staged | Prints |
|---|---|
| `--case up`, at `b634d60e5`'s `read_fixture_rows` | `nothing measured: plant engine-edit: scripts/memory-tree/README.md is absent at release-0` |
| `--case up`, S7 staged | `release-0 · the policy adopter's re-run committed .governance/policy.json`, which `:238-239` prints after `write_plant_edits(t, plants)` (`:229`) |

The two `--case up` rows were measured in a clone of `b634d60e5` before this revision. The
`read_target_prefix` form gives the same `tools` at `:124` and `:232`, so they hold.

### Past the plants, measured

With 86 and S7 staged at `scripts/`, the walk stops at `plant withdraw-one: scripts/hooks/kit.toml
holds no '[[files]]\ninclude = ["README.md"]...' to replace`. The blob is LF. But `.gitattributes:2`
sets `* text=auto` and `:222` pins `tools/*/kit.toml text eol=lf` only, and the walk's clone sets
`core.autocrlf=false` and no `core.eol` (`upgrade_walk.py:204`). So on Windows the moved file checks
out CRLF. With `-c core.eol=lf` also staged, as a measurement only, the walk stops at
`upgrade_steps.Refusal: tools/govkit/registry.toml: no registry at <tip>` from `read_steps` over the
clone tip (`upgrade_walk.py:1115`, `upgrade_steps.py:756-760`), exit 1.

Re-measured for TOOL-dSafePassage-89 on 2026-10-29: the CRLF stop came from this measurement's bare
`git mv`, which re-spells nothing. The foreign-prefix leg moves with `set_tool_root` and
`write_declarations` (`tools/run-gates/foreign-prefix.gov.test.sh:482-535`), which re-spell
`.gitattributes:222` with the tool root, and in that shape the walk passes `withdraw-one` and stops
at `read_steps` alone. That stop is the §3 hands-off to TOOL-dSafePassage-89, which diagnoses it.

So `--list` prints no plant line in either moved clone at this unit's place in the build order
(audit M2, id 7). `build_release_tree` writes the `withdraw-one` plant whether or not the walk is
listing (`:242-245`), and `main` runs `read_steps` (`:1115`) before the listing (`:1118-1124`).
AC8 reads the two rows without a walk. Rev-2's record that `--list` printed them in a bare-moved
clone does not match this code path.

### S8: the docs fixture at `scripts`

`PLANTS` (`docs_leg.py:77-80`) gains `scripts-prefix`. In `build_docs_fixture`, a local
`pre = "scripts" if plant == "scripts-prefix" else FIXTURE_PREFIX` takes `FIXTURE_PREFIX`'s place in
the layout (`:563-566`, `:573`, `:608`). The three `tools/fx/*.py` files (`:567`) become
`{pre}/fx/*.py`. For the plant, the usage text is `FIXTURE_USAGE` with `"tools/fx/` and
`script:tools/fx/` spelled `{prefix}/fx/`. The guide page's two commands read
`python <prefix>/fx/run.py go --part task` and `python <prefix>/fx/tool.py render --role builder`.
Each usage marker names its row's id as the leg resolves it at `scripts`. Every other plant is
byte-identical. The `_docs_cases` row is
`(["scripts-prefix"], 0, r"^docs: \d+ classes · .* commands 2 tested, 1 skipped, 0 unrowed")`.

With `:310` spelling `tools/` in place of `troot`, both commands resolve to `tools/fx/...`, which is
not tracked at `scripts`. They read `skipped` (`:312-313`), the count reads 0 tested, and the leg
refuses with `no page command was tested` (`:464-465`), exit 2.

### S9: the control

`resolve-python.test.sh:337-338` become:

```bash
out=$(bash "$FD/$KIT_REL/python-floor.sh" down 3.11 "$FD" 2>&1); rc=$?; out=${out//$'\r'/}
{ [ "$rc" = 1 ] && [[ $out == "python-floor down: mode "* ]] && [[ $out == *"planted.toml:"* ]] && [[ $out != *Traceback* ]]; } \
  || bad "the down over gov's own tree with no <to> did not grade its HEAD default: exit 1 naming planted.toml, no traceback: rc=$rc $out"; ok
```

FD's HEAD carries the planted TOML 1.1 table from `:324`, which `:325-326` grade at rc 1 naming
`planted.toml`. With no `<to>`, the down defaults to that HEAD (`tools/lib/python_floor.py:421-422`),
so the same finding is the expected outcome. `python-floor down: mode` is the down's first stderr line
(`python_floor.py:429`), and `:299` reads it the same way.

### S11: gov's own shim rows

`check_shim_paths` (`upgrade_walk.py:553-579`), called by the `shims` case after the clone checks out
its tip (`:241`, `:695`), reads gov's own rows with `shims.read_shim_rows(ctx["clone"])` (`:565`). That
resolves each row's `from` and `to` against `derive_tool_root(clone)` (`shims.py:71`, `:89`), the
clone's tool root. Then `:572-574` tests `r["from"] in installed` against the target receipt, whose
paths sit under `deploy.toml`'s `prefix`. At a moved prefix gov's rows are `scripts` paths and the
receipt holds `tools` paths, so no gov row can match, and a vanished gov forwarder reads green. The
defect is latent: `tools/govkit/shims.toml` declares no `[[shim]]` row today. It is reachable once
TOOL-dSafePassage-89 drops the memo. Until then, the tip read of `shims.toml` under the memo's `tools`
refuses at a moved prefix.

`read_shim_rows` gains a keyword, its default the present behaviour, so its other callers
(`govkit.py:3537`, `shims.py:269`, `:285`, `:349`) are untouched:

```python
def read_shim_rows(root, troot: str | None = None) -> list[dict]:
    ...
    troot = govkit.derive_tool_root(root) if troot is None else troot
```

Its docstring gains one sentence: where `troot` is given, `{prefix}` resolves against it rather than
the root's own tool root, for a reader comparing the rows with an install at another prefix. The file
is still found at the root's own tool root (`:66`). `:565` becomes
`rows = shims.read_shim_rows(ctx["clone"], read_target_prefix())`. The same rows feed the `closed`
test at `:567-569`, which reads only `id` and `closed`.

`check_graders` gains the `shim-root` grader, after `release-engine` in its tuple (`:1053-1056`). Its
scratch gov's tool root is `moved`, so no literal spells a prefix the foreign-prefix leg moves gov to:

```python
    def check_grade_shim_root() -> str:
        gkn = load_engine()[2].GOVKIT_DIR.name
        row = ('[[shim]]\nid = "demo/old"\nkind = "command"\nfrom = "{prefix}/demo/old.sh"\n'
               'to = "{prefix}/demo/new.sh"\nclosed = false\n')
        c = build_repo("shim-gov", {f"moved/{gkn}/registry.toml": "", f"moved/{gkn}/shims.toml": row})
        t, old = scratch / "shim-target", f"{read_target_prefix()}/demo/old.sh"
        (t / ".governance").mkdir(parents=True)
        (t / RECEIPT).write_text(json.dumps({"files": [{"path": old}]}), encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            got, _n = check_shim_paths({"clone": c}, t, [])
        return "" if any(f"its forwarder {old} is gone from the walked target" in g for g in got) else (
            f"gov's own row, its forwarder {old} gone, read no red: {got}")
```

`check_shim_windows` returns at once for a row that is not `closed` (`shims.py:349-351`), and
`read_releases` returns none (`:300-303`), so the grader needs only a repository and the two files.

| Measured on node a, 2026-10-29 | Prints |
|---|---|
| `check_shim_paths` over that scratch gov and receipt, at `cba885c58` | `[]`, the vanished forwarder unread |
| the same, S11 staged | `shims · demo/old · its forwarder tools/demo/old.sh is gone from the walked target` |
| `check_graders()`, S7, S11 and S12 staged | seven rows reading `ok`, then `[]` |
| the same, with `:565` left as it is | `grader · shim-root · RED · gov's own row, its forwarder tools/demo/old.sh gone, read no red: []` |

### S12: the release engine through `resolve_tool_path`

```python
def derive_release_engine(clone) -> pathlib.Path:
    ...
    _us, _shims, gk = load_engine()
    return gk.resolve_tool_path(clone, gk.GOVKIT_DIR.name, "govkit.py")
```

`resolve_tool_path` (`govkit.py:299-302`) joins a root to its derived tool root, dropping an empty
one, and then to kit-relative parts. `derive_registry_path` (`:305-307`) already calls it with
`GOVKIT_DIR.name`. The body it replaces spelled the same join a second time, with the kit directory
typed as `govkit`. The function stays, because 86's `release-engine` grader observes it by name
(`upgrade_walk.py:1040-1049`). Measured at `cba885c58` over the grader's three pin-shaped trees,
`tools`, `scripts` and the repository root, both bodies returned the same path for each.

### Inventory

Minted: the walk plant `truncated-image-held`, the docs plant `scripts-prefix`, the arm tags
`[dSP-87 AC1]`, `[dSP-87 AC5]`, `[dSP-87 AC6]` and `dSP-87`, and the scratch names `dsp87-quote-widened`
and `us87_widened`. S7's function `read_target_prefix` and its one `Stop`. S11's keyword `troot` on
`read_shim_rows`, its grader `shim-root` and the grader's scratch names `shim-gov` and `shim-target`.
One `Refusal` site, S1's. `STEP_ENV_KEEP` gains one member. No flag, conf key, gate leg or receipt
field.

### Migration

None. No stored shape changes.

### Rollout

Live at landing, at order 16. TOOL-dSafePassage-61 holds order 16 and stays DEFERRED. This unit
builds after TOOL-dSafePassage-86, which edited `upgrade_walk.py` first and is built at `cba885c58`.
AC9 needs 86's `derive_release_engine`, and S12 re-points it. The builder re-reads each cited line by
content before editing.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/upgrade_walk.py`
- `tools/govkit/shims.py`
- `tools/govkit/selftest.py`
- `tools/govkit/refusal_join.py`
- `tools/govkit/steps/python_floor.py`
- `tools/govkit/docs_leg.py`
- `tools/lib/resolve-python.test.sh`
- `help/upgrade-steps.md`

### Alternatives rejected

- **S1: refuse `..` before `derive_contained_rel`.** `..\ESCAPED.txt` would then read the new message,
  and `[dSP-72] AC3` reds.
- **S1: change `derive_contained_rel`.** That was the finder's fix, and the skeptic rejected it, because
  govkit's destination predicate shares it.
- **S4: pass the resolved bash to the stub as an argument or a token.** It changes the floor row's
  argv in `steps.toml` and its witness, up and down together. `resolve_shell_argv` in the child is the
  parent's own function, so it restores the pre-82 behaviour without touching the row.
- **S4: catch `Refusal` and exit 2.** On a node that needs no `GOV_BASH`, that stops where the old argv
  fell back to bare `bash` and ran.
- **S7: resolve the plants inside `build_release_tree` against `derive_tool_root(clone)`.** The plants
  are read in `main` (`:1110`) before the clone exists, and `ctx["ordered"]` (`:1113`) reads their
  paths. The answer is the same `tools` at this pin.
- **S7: resolve a `{prefix}` in `deploy.toml`'s `prefix` against the pin's tool root, read through
  `git ls-tree` on gov.** No govkit function derives a tool root at a commit: `derive_tool_root`
  (`govkit.py:191-211`) globs a working tree. It would be a second spelling of that glob. A literal
  with a `Stop` single-sources the value with no new derivation.
- **S11: compare gov's rows and the receipt in the `{prefix}`-relative spelling.** The walk would
  strip two roots from resolved paths. A `troot` keyword resolves gov's rows once, through the shims
  reader's own resolver, as the arm rows already are resolved.
- **S12: drop `derive_release_engine` and call `resolve_tool_path` at `:219`.** 86's grader observes
  the function by name, so keeping it keeps that arm.
- **S8: a second fixture function.** Every plant but one would be a copy. A local `pre` keeps one
  layout.

## 5. Production-readiness checklist

- security: S1 narrows the write surface. S4 adds one allowlist name, `GOV_BASH`, which names an
  executable, carries no credential, and is the class of `PATH` and `GOV_PYTHON`. S11 changes what a
  read compares, and writes nothing. No new write path, spawn or surface.
- perf / scale: the graders add a handful of git calls in a scratch repository, and `shim-root` adds
  one more scratch repository. The `govkit selftest` leg gains one walk plant of two scans, one docs
  plant and one staged-copy load, under two minutes together.
- error / empty / loading states: a `..` key is refused with its own message. An unparsable image under
  a holding witness is refused with a remedy that applies when nothing is committed. A `{prefix}`
  token in the fixture's `prefix` is a `Stop` naming the file, exit 2.
- observability: each refusal names its path and its remedy. Each grader prints its own row.
- risks: S6's remedy wording moves for every caller of `read_image_paths`, and §4 "S6" checks each
  caller. S7's read at `:232` moves from the clone's tool root to the target's prefix, which answer
  the same `tools` at every prefix the leg runs. S11's keyword defaults to the present behaviour for
  the shims reader's four other callers. The moved-prefix row stays red past this unit (§3).
- testing: §7's New arms, and AC1, AC5, AC6 and AC9's probes.
- migration: none.
- user docs: S10's three edits to `help/upgrade-steps.md`.

## 6. Acceptance criteria

- **AC1** — When §4 "S1"'s probe, `python <scratch>/contain_probe.py`, runs from the repository root,
  it prints `a/../b -> refused: 'a/../b' holds a '..' segment` and `lnk/../x -> refused: 'lnk/../x' holds a '..' segment`,
  and it prints `a/b -> a/b`. The probe builds a scratch target whose `lnk` is a junction on Windows or
  a symlink elsewhere, and prints `check_contained` over `a/../b`, `lnk/../x`, `lnk/x`,
  `..\ESCAPED.txt` and `a/b`.
  Red when: `check_contained` tests only the normalised form, so it prints `a/../b -> b` and
  `lnk/../x -> x`, as at `b634d60e5`.
  fixture: a scratch target under the temp root. The tree holds none today.
- **AC2** — When `git grep -n "^BRANCH_PIN = 335" -- tools/govkit/refusal_join.py` runs, it prints
  one line, and `git grep -n -F "TOOL-dSafePassage-87" -- tools/govkit/refusal_join.py` prints the
  delta's comment.
  Red when: the pin stays at 334, so the floor at `refusal_join.py:305` stays green when S1's site is
  gone.
  figure: 335 is DERIVED, `BRANCH_PIN` at `b634d60e5` plus S1's one site, and the builder re-measures it.
- **AC3** — When `git grep -n -F -- '--no-renames' -- tools/govkit/upgrade_walk.py` runs, it prints
  one line, `check_tree_clean`'s status command; and when
  `git grep -n -F 'engine.py' -- tools/govkit/upgrade_walk.py` runs, every line it prints sits inside
  `check_grade_tree_clean`, and it prints at least one. Preservation half: when
  `python -c "import sys; sys.path.insert(0, 'tools/govkit'); import upgrade_walk as u; print(u.check_graders())"`
  runs, it prints `upgrade-walk: grader · tree-clean · ok`, and its last line is `[]`, as it does at
  `cba885c58`.
  Red when: S2 is not built, so both greps print nothing, as at `cba885c58`. The build's probe:
  `check_tree_clean` staged with the v1 parse kept prints `RED ·`, the grader's scratch engine file
  under `tools/govkit`, and `renamed into fixtures/release-0, it returned []`.
- **AC4** — When `git grep -n -F 'x.sh' -- tools/govkit/upgrade_walk.py` runs, it prints one line,
  inside `check_grade_tree_clean`, the `libf` it lays out. Preservation half: the `check_graders`
  command of AC3 reads `ok` on its `tree-clean` row.
  Red when: S3 is not built, so the grep prints nothing, as at `cba885c58`. The build's probe: `lib`
  left out of `check_tree_clean`'s pathspec prints `RED ·`, the grader's scratch shell file under
  `tools/lib`, and `edited, it returned []`, which no grader prints at `cba885c58`.
- **AC5** — When §4 "S4"'s `python <scratch>/floor_probe.py` runs from the repository root, it prints
  `ok 0 ''`.
  Red when: `GOV_BASH` is not in `STEP_ENV_KEEP`, so it prints `failed 127` through the WSL launcher.
  At `b634d60e5` it prints `failed 1` and `Set GOV_BASH.`
  fixture: a node whose PATH bash is the only usable bash. On a node with no `System32` launcher, the
  127 reads as `bash` not found.
- **AC6** — When `git grep -n -F "[dSP-87 AC6]" -- tools/govkit/selftest.py` runs, it prints two
  lines inside `check_upgrade_steps`. Preservation half: when §4 "S5"'s
  `python <scratch>/esc_probe.py` runs from the repository root, it prints
  `[('demo/esc', 'third'), ('demo/ml', 'third')]`, as it does at `cba885c58`.
  Red when: the arm is absent, so the grep prints nothing, as at `cba885c58`. Or the engine's
  pre-filter is quote-widened, so the probe prints `unlanded` for both rows, measured with a staged
  copy of `upgrade_steps.py` as its argument. The probe's fixture text is S5's block byte for byte, so
  a row respelled where the widened filter finds it, such as the escape decoded to `/`, reads `third`
  under that copy.
- **AC7** — When `python tools/govkit/upgrade_steps.py fixture walk --plant truncated-image-held`
  runs, it exits 0, prints `walk: held · rc 1 · remedy named` and
  `walk: held · after the remedy · fx/s2 applied · rc 0`, and prints no `walk: FAILED`.
  Red when: the refusal names only `put back its committed copy`, so it prints `remedy absent` and
  `walk: FAILED`. Under §8 F1's option B, the first scan exits 0 and it prints `walk: FAILED`.
  cost: one scratch gov and two walks, under a minute.
- **AC8** — When
  `python -c "import upgrade_walk as u; print(next(r['path'] for r in u.read_plant_rows() if r['id'] == 'engine-edit')); print(next(r['path'] for r in u.read_fixture_rows('gov_plant') if r['id'] == 'withdraw-one'))"`
  runs from the `scripts/govkit` directory of the leg-moved clone, its first line is
  `tools/memory-tree/README.md`, and its second names `kit.toml` under `scripts/hooks`. No walk runs, so
  no stop on the walk's path is met first (§4 "Past the plants, measured").
  Red when: `read_fixture_rows` resolves `[[plant]]` against the working gov's root, so the first line
  names `README.md` under `scripts/memory-tree`, as at `cba885c58`.
  cost: one clone of the repository and the leg's move, about two minutes.
  fixture: the leg-moved clone, built from the build head with this unit landed by the leg's own
  `set_tool_root scripts` and `write_declarations` (`tools/run-gates/foreign-prefix.gov.test.sh:482-535`),
  extracted and sourced as TOOL-dSafePassage-89 §4 "Measured at writing time" states. The tree holds
  none today.
- **AC9** — When `FOREIGN_PREFIX_PROBE=1 python upgrade_walk.py --case up` runs from the same directory
  of the same clone, with TOOL-dSafePassage-86 landed, it prints
  `upgrade-walk: release-0 · the policy adopter's re-run committed` and no `is absent at release-0`.
  Observed at this unit's pass: the walk then stops at `read_steps`, the §3 hands-off to
  TOOL-dSafePassage-89.
  Red when: the plants resolve against the working gov's root, so it prints
  `nothing measured: plant engine-edit:`, then `README.md` under `scripts/memory-tree`, then
  `is absent at release-0`.
  cost: one release-0 apply in AC8's clone, about 70 seconds.
- **AC10** — When `python tools/govkit/docs_leg.py --fixture --plant scripts-prefix` runs, it exits 0
  and prints a line matching `commands 2 tested, 1 skipped, 0 unrowed`.
  Red when: `check_page_command` (`docs_leg.py:310`) spells `tools/` in place of `troot`, so both
  commands read skipped, and it exits 2 with `no page command was tested`.
- **AC11** — When `git grep -n -F 'Traceback' -- tools/lib/resolve-python.test.sh` runs, it prints
  the gov-tree control's assertion line; and
  `git grep -n -F '[ "$rc" != 2 ] || bad "the down over gov' -- tools/lib/resolve-python.test.sh`
  prints nothing.
  Red when: the control still asserts only `rc != 2`, so a traceback, which exits 1, passes it.
- **AC12** — When `git grep -n -F "segment even one" -- help/upgrade-steps.md`,
  `git grep -n -F "GOV_BASH" -- help/upgrade-steps.md` and
  `git grep -n -F "where none is committed" -- help/upgrade-steps.md` run, each prints one line. S10
  pins each phrase to one source line, so a wrap cannot split it.
  Red when: a page edit is absent, so its grep prints nothing, as each does at `cba885c58`.
- **AC13** — When the `check_graders` command of AC3 runs, it prints
  `upgrade-walk: grader · shim-root · ok`, and its last line is `[]`.
  Red when: `check_shim_paths` reads gov's own rows at the clone's tool root, so it prints
  `grader · shim-root · RED ·` and `read no red: []`, measured with `:565` left as it is. At
  `cba885c58` no `shim-root` row prints.
- **AC14** — When
  `git grep -n -F 'resolve_tool_path(clone, gk.GOVKIT_DIR.name, "govkit.py")' -- tools/govkit/upgrade_walk.py`
  runs, it prints one line, inside `derive_release_engine`. Preservation half: the `check_graders`
  command of AC3 prints `upgrade-walk: grader · release-engine · ok`, as it does at `cba885c58`.
  Red when: the function keeps its own join, so the grep prints nothing, as at `cba885c58`.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `upgrade-walk` · `docs` · `python resolver (behaviour + inline parity + idiom ban)` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · the two `[dSP-87 AC1]` checks of `check_upgrade_steps`, staged red by a `check_contained` with no `..` test, which returns `b` and `x` · none
New arm: tools/govkit/upgrade_walk.py · covers AC3 AC4 · the `tree-clean` grader of `check_graders`, staged red by the v1 rename parse and, separately, by `lib` left out of the pathspec · none
New arm: tools/govkit/selftest.py · covers AC5 · the `[dSP-87 AC5]` check of `check_step_isolation`, staged red by a `STEP_ENV_KEEP` without `GOV_BASH` · none
New arm: tools/govkit/selftest.py · covers AC6 · the two `[dSP-87 AC6]` checks of `check_upgrade_steps`; the second is itself the staged break, a copy carrying the quote-widened pre-filter, and the first reds when that pre-filter lands in the engine · none
New arm: tools/govkit/upgrade_steps.py · covers AC7 · the `walk` family's `truncated-image-held` plant, run by its `dSP-87` row in the selftest's fixture table, staged red by the refusal text at `b634d60e5` · none
New arm: tools/govkit/docs_leg.py · covers AC10 · the `scripts-prefix` plant, run by its `_docs_cases` row, staged red by `check_page_command` spelling `tools/` · none
New arm: tools/lib/resolve-python.test.sh · covers AC11 · the gov-tree no-`<to>` control, staged red by a `python_floor.py` whose HEAD-default path raises, which exits 1 with a traceback · none
New arm: tools/govkit/upgrade_walk.py · covers AC13 · the `shim-root` grader of `check_graders`, staged red by `check_shim_paths` reading gov's own rows at the clone's tool root, which reads no red · none

The `govkit` and `policy fixtures` legs are the guard join's. `upgrade-walk`, `docs` and
`python resolver (behaviour + inline parity + idiom ban)` run the suites S2, S3, S7, S8, S9, S11 and
S12 touch. S12 adds no arm: TOOL-dSafePassage-86's `release-engine` grader already holds
`derive_release_engine` across three pin-shaped trees, and this unit does not move it.
The foreign-prefix parity leg is not on the line, for the reason §3 gives. AC2's floor moves from 334
to 335, which is the only floor this unit moves.

## 8. Open questions

- **F1 — Which outcome does the forward walk pin for an unparsable before-image under a step whose
  witness holds (M6)?**
  - **A, the refusal, with a remedy that applies when no copy is committed (recommended).** Move 1
    keeps refusing through `read_image_paths`. The message names the committed-copy remedy and, where
    none is committed, removing the image and giving up its before bytes. It changes one string, and
    the walk still writes nothing it did not write before.
  - **B, `write_before_image`'s tolerance in move 1.** An unparsable image whose listed paths did not
    change since it was written reads absent and is removed, and the walk passes the step. It recovers
    without a hand step. But it adds a removal of a before-image to the witness-holds branch, which
    today stages and records only. Where a committed copy exists, it would also leave an unstaged
    deletion of a tracked file beside a row recorded `applied` with no image.
  - Recommendation: A. By BUILD-METHOD M3, B is the more feature-rich option, and veto 3 discards it:
    it widens a write surface, the deletion of a step's only record of its before bytes, beyond what a
    batch of fail-closed minors priced. A survives, and it is the only survivor. B can be its own unit
    with its committed-copy case designed.
  - RESOLVED (agent, 2026-10-29, delegated): A, under the run's standing mandate, by M3's veto 3.

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-86-1-spec-writer.md` and its
  brief `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-86-spec-brief.md`.
  It closes M1 to M7, L1 and L2 (ids 1, 3, 4, 8, 9, 10, 14, 11, 12) of the round-2 closing diff
  review,
  `memory/builds/dSafePassage/reviews/2026-10-29-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-84-closing-diff-round2.md`,
  at the skeptic's fixes, its corrected fix for M1. S1, S2, S3, S4 and S7 were staged and measured
  in clones of `b634d60e5` (§4). §8 F1 was resolved by this spec's writer under the delegated mandate,
  by M3's rule.
- rev-2 · 2026-10-29 · AC3 AC4 AC8 AC9 §3 §4 · from the brief
  `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-88-spec-brief.md`. The
  seven backticked paths the spec-token check read as untracked are reworded: AC3 and AC4 name the
  grader's scratch file by its directory, AC8 and AC9 run `upgrade_walk.py` from the moved clone's
  `scripts/govkit` directory and name each moved file by its directory. `--list` run from there on
  2026-10-29 printed the two lines AC8 names. §3's hands-off external edge now points at
  TOOL-dSafePassage-89. §4 "Past the plants, measured" records that the CRLF stop does not occur
  at the leg's own move, so no unit closes it.
- rev-3 · 2026-10-29 · §3 · from the brief
  `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-88-third-stop-spec-brief.md`.
  §3 gains the hands-off edge to TOOL-dSafePassage-88, the mirror of its consumes-from: 88's AC2 walk
  reaches `update` at a moved prefix only through S7's plant paths.
- rev-4 · 2026-10-29 · §1 §2 §3 §4 §5 §6 §7 §10 · S2 S5 S7 S10 S11 S12 · AC3 AC4 AC6 AC8 AC9 AC12 AC13
  AC14 · folds the round-1 spec audit,
  `memory/builds/dSafePassage/reviews/2026-10-29-review-TOOL-dSafePassage-86-87-89-88-spec-audit-round1.md`,
  from the brief
  `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-87-audit-fold-brief.md`.
  M1: AC3 and AC4 observe S2 and S3 by greps that print nothing at the base, the grader run kept as
  their preservation half. M2, at the skeptic's corrected fix: AC8 reads the two rows by `python -c`
  in the leg-moved clone, and rev-2's `--list` record is corrected in §4. M3: S5's escaped id is the
  unicode escape. M4's half for this unit becomes S11. L2: AC6's probe imports the engine. L4: AC12
  greps short tokens, pinned to one line by S10. L5: the `[dSP-87 AC1]` check loses its no-write
  conjunct. L8: S7's `read_target_prefix`. TOOL-dSafePassage-86's L7 becomes S12. The base moves to
  `cba885c5`, with 86 landed, and `upgrade_walk.py`'s lines are re-cited there. S7, S11 and S12 were
  staged and measured in a moved clone of it.

## 10. Reuse audit

Each item extends the function the review names, so no new seam is built. S1 extends
`check_contained` (`tools/govkit/upgrade_steps.py:1068`), and its checks reuse the `[dSP-72]` block's
`t72`, `write_link72` and `write_image72`. S2 and S3 extend `check_grade_tree_clean` and its
`build_repo` (`tools/govkit/upgrade_walk.py:966`). S4 reuses `resolve_shell_argv`
(`upgrade_steps.py:422`), the parent's own resolution, and extends `STEP_ENV_KEEP` as
TOOL-dSafePassage-75 did. S5 reuses `build_staged_copy` (`tools/govkit/selftest.py:3579`) and
`[dSP-53]`'s in-process load. S6 extends `run_walk_fixture`'s plant family and the selftest's fixture
table. S7 adds `read_target_prefix`, the one reader of the `prefix` field of the `deploy.toml` that
`build_release_tree` already reads (`tools/govkit/upgrade_walk.py:213-214`), and both callers use
it. S8 extends `build_docs_fixture` and `_docs_cases`. S11 extends `read_shim_rows`
(`tools/govkit/shims.py:60`) with one keyword, and `check_graders` with one grader. S12 extends
`resolve_tool_path` (`tools/govkit/govkit.py:299-302`), the seam that joins a root to its tool root
and kit-relative parts, which `derive_registry_path` (`:305-307`) already uses with `GOVKIT_DIR.name`.
`python tools/codebase-map/reuse_lookup.py "read a target install prefix once; resolve shim rows from and to against another tool root; join a root to its tool root and kit-relative parts"`
ranked `derive_tool_root`, `resolve_prefix_token` and `resolve_kit_dir` as seams, beside name-stem
matches. It did not rank `resolve_tool_path` or `read_shim_rows`. They were found by
`git grep -n "def resolve_tool_path\|def read_shim_rows\|ls-tree" -- tools/govkit`, which also showed
that no govkit function derives a tool root at a commit (§4 "Alternatives rejected").
`python tools/codebase-map/reuse_lookup.py "a containment check, a dirty-tree refusal, a step environment allowlist and a fixture plant, each extended by a grader arm"`
ranked name-stem seams only, `tree`, `check`, `arm`, `refusal`, `fixture` and `build_fixture`. None is
a containment, refusal or allowlist primitive this unit does not already extend. The recall probe
ranked TOOL-aMendedFleet-111, a batch of closing-review minors with a rename-safe diff, then this
review, TOOL-dSafePassage-76's and -77's specs, which built S1's, S2's and S6's sites, and 72's ledger.

Recall terms used: `python tools/memory-recall/query.py "round-2 closing review minors: dotdot containment, staged rename dirty engine, GOV_BASH step env, quote-widened mutant, truncated image walk, docs prefix fixture" --terms "check_contained derive_contained_rel check_tree_clean porcelain no-renames STEP_ENV_KEEP GOV_BASH resolve_shell_argv derive_introduced read_image_paths WALK_PLANTS build_docs_fixture"`
