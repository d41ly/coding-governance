# TOOL-dSafePassage-72 — a before-image path is contained by one predicate govkit's destinations share, and refused where any segment on it is a link

**Status:** DEFERRED · rev-4 · 2026-10-28 · node a · Tier-2 · base 83817478 · streams tooling · order 16 · advances TOOL-dSafePassage-14 · ratified 2026-10-28

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-prompt-TOOL-dSafePassage-72-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-72-1-spec-writer.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-72-build-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-72-build-brief.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-72-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-72-spec-brief.md) | research | TOOL-dSafePassage-73 TOOL-dSafePassage-74 TOOL-dSafePassage-75 |
| [2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-73 TOOL-dSafePassage-74 TOOL-dSafePassage-75 TOOL-dSafePassage-76 TOOL-dSafePassage-77 TOOL-dSafePassage-78 TOOL-dSafePassage-80 TOOL-dSafePassage-81 TOOL-dSafePassage-82 TOOL-dSafePassage-83 |

<!-- /gen:spec-records -->

## 1. Goal

`check_contained` (`tools/govkit/upgrade_steps.py:1040-1045`) reads a before-image path only as
POSIX, and never tests a segment for a link. So a tampered committed image under
`.governance/steps/` can make `update --rollback` write outside the target, through a backslash
climb, a rooted or UNC path, or a junction or symlink inside the target, and an up can copy bytes
from outside the target into an image that is then staged. This unit closes H1 (id 1) and H2 (id 2)
of the closing diff review, round 1: one lexical predicate answers "does this path leave the
target" for both the step module and govkit's destinations, and `check_contained` refuses any link
or reparse point on the path through `test_path_linked` before anything is read, made, written or
unlinked.

## 2. Scope (IN)

- **S1** — The predicate. `derive_contained_rel(rel: str) -> str | None` in
  `tools/govkit/upgrade_steps.py`, above `check_contained`. It folds every `\` to `/`, applies
  `posixpath.normpath`, and returns that normalised form, or None where the path leaves the
  target or names no file under it: the form is `.` (from an empty path, `.` or `a/..`), is `..`
  or opens `../`, or `posixpath.isabs` holds on the form, which is what catches a rooted `\x` once
  it is folded; `ntpath.isabs` holds on `rel`, which catches the UNC `\\server\share\x` and the
  drive-absolute `C:\x` forms; or `rel` holds a `:` anywhere (§8 F1, resolved). The module gains
  `import ntpath` and `import posixpath`. Observed by AC1.
- **S2** — govkit decides through it. `demand_contained_dest` (`tools/govkit/govkit.py:1219-1253`)
  calls `upgrade_steps.derive_contained_rel(dest)` and refuses where it returns None, in place of
  its own test at `:1244-1246`. Its refusal keeps the words `leaves the target repository`, the
  `where` source and the `deploy.toml` hint, and quotes `dest` alone, since the predicate hands
  back no form for an escaping path. Its docstring (`:1238-1243`) is rewritten to say the
  decision is `upgrade_steps.derive_contained_rel`'s and that a colon anywhere is refused (§8 F1).
  The module-level import of ntpath at `tools/govkit/govkit.py:38` is not kept, since no code in
  govkit.py reads it after this change (`:1242` and `:6598` name it in prose only). govkit already
  loads the step module at import (`:142`), so no new load is added. Because the predicate is
  shared, govkit's destinations also refuse an empty path, `.` and `a/..`; each caller
  (`:805`, `:1326`, `:3758`, `:3827`, `:5769`) hands in a file path, and `:3757` already skips an
  empty `dest`. Observed by AC2 and AC7.
- **S3** — The lexical half of `check_contained`. It calls `derive_contained_rel(rel)`; None raises
  the refusal it raises today, `'<rel>' is not a path inside the target, so no step may write it`.
  It returns `pathlib.Path(target) / <the normalised form>`. Observed by AC1 and AC3.
- **S4** — The link half of `check_contained`. After the lexical half, it walks the normalised
  form's segments from the target down: `target / s1`, then `target / s1 / s2`, and so on. Each
  prefix is tested with `test_path_linked` (`tools/govkit/upgrade_steps.py:1417-1425`), and one
  that reads True raises `'<rel>': <prefix> is a link or other reparse point, which no step read or
  write follows, so where it leads is unknown`. An `OSError` or `ValueError` the prefix's test
  raises, from a name the node cannot open such as `a?b` or `a|b` on Windows, or from an embedded
  NUL on any node, raises `'<rel>': <prefix> does not read as a path on this node, so no step may
  read or write it`. That wrapper is `check_contained`'s own; `test_path_linked`'s contract is
  unchanged for its other callers. The walk ends at the first prefix that is not a directory, an
  absent one or a file, since nothing below it can be a link. The target root itself is not
  tested: every caller hands in a resolved target. Observed by AC3 and AC4.
- **S5** — The image path is contained. `derive_image_path`
  (`tools/govkit/upgrade_steps.py:1032-1037`) returns
  `check_contained(target, f"{IMAGE_DIR}/{entry}/{slug}.before.json")`, so `.governance`,
  `.governance/steps`, the entry directory and the image file are each tested before the image is
  read, its directory made, it is written or it is unlinked. Observed by AC4.
- **S6** — The held branch of `write_before_image` (`tools/govkit/upgrade_steps.py:1075-1083`)
  runs `check_contained` over every path the image lists before `derive_after` is handed their
  before bytes, as the fresh branch already does at `:1088-1089`. Observed by AC5.
- **S7** — The help. `help/upgrade-steps.md`'s `## Rolling back` section gains one bullet, opening
  `- **A before-image path outside the repository.**`. It says a path an image lists, or the
  image's own path, is refused where it climbs out (`..`, a backslash climb), is rooted, UNC or on a
  drive, holds a colon, or passes through a symlink, a junction or any other reparse point, and
  that the refusal names the path and the link before anything is read or written. Observed by AC6.

## 3. Non-goals (OUT)

- A `.git` segment in a before-image path, and a path under the resolved git directory. That is
  M1 (id 3), batched into TOOL-dSafePassage-76, which builds on this unit's `check_contained` and is
  dispatched after it.
- govkit's own write loops. `cmd_update`'s resolve-and-compare at `tools/govkit/govkit.py:10919-10926`
  and `:10544-10548` answers a different question, whether a resolved destination stays inside, and
  follows an inside link by design. Making every adopter-tree write path test its segments is a
  checklist row for the project's bug-class checklist, not this unit.
- The review's extra `(target/rel).resolve().is_relative_to(target.resolve())` assertion. §4,
  Alternatives rejected, says why.
- Windows device names (`CON`, `NUL`, `COM1`), a race between the test and the write, and a hard
  link. §4 states each as a gap.
- The upgrade-walk leg's own oracles (`tools/govkit/upgrade_walk.py`). TOOL-dSafePassage-77 owns
  that file's findings.

### Edges

none

Read and closed, so named here rather than joined: TOOL-dSafePassage-1's before-image helpers,
`check_contained` and `derive_image_path`; TOOL-dSafePassage-56's and TOOL-dSafePassage-59's
`test_path_linked`, the one lstat and its reparse tag; TOOL-dSafePassage-4's `write_from_before_image`
down; and the deployer's `demand_contained_dest`. The edge join counts CLOSED specs, and a CLOSED
spec cannot take the matching `hands-off` line.

## 4. Design

### Observed at base

A scratchpad probe on node a (Windows 11, Python 3.15) on 2026-10-28 imported
`tools/govkit/upgrade_steps.py` at `83817478` and ran each path through it.

| Input | At base |
|---|---|
| `check_contained(t, r"..\ESCAPED.txt")` | returned `<t>\..\ESCAPED.txt` |
| `check_contained(t, r"\x-rooted.txt")` | returned `C:\x-rooted.txt` |
| `check_contained(t, r"\\localhost\c$\x.txt")` | returned `\\localhost\c$\x.txt`, the share itself |
| `check_contained(t, "a:b")`, `check_contained(t, "C:x")` | refused |
| `check_contained(t, "")` | returned the target directory itself |
| `test_path_linked(t / "a?b")`, and the same with a NUL in the name | raised `OSError` (WinError 123), and `ValueError` |
| `write_from_before_image` over an image listing `lnk/planted.txt`, `lnk` a junction to `outside/` | returned `['lnk/planted.txt']`; `outside/planted.txt` was written |
| `write_before_image(t, "demo/second", ...)` naming `lnk/secret.txt` | returned; the image held `outside/secret.txt`'s bytes |

### One answer to one question

The question "does this repo-relative path leave the target" is asked by `check_contained` and by
`demand_contained_dest`, and today they answer differently: the first misses every backslash form
the second catches, and the second misses a colon past index 1, such as `ab:c` or `x/a:b`, which
the first catches; govkit refuses `a:b` only because its colon sits at index 1 (`:1246`). S1 gives
the decision one home, in the step module, because govkit already imports that module at load and
binds names from it (`tools/govkit/govkit.py:142-154`, TOOL-dSafePassage-35 S24). The step module
reaches govkit only lazily through `load_govkit()`. Each caller keeps its own refusal text, because
each names a different remedy: a before-image for the step module, a `deploy.toml` `prefix` for
govkit.

```
derive_contained_rel(rel):
    norm = posixpath.normpath(rel.replace("\\", "/"))
    if norm in (".", "..") or norm.startswith("../") or posixpath.isabs(norm) \
            or ntpath.isabs(rel) or ":" in rel:
        return None
    return norm

check_contained(target, rel):
    norm = derive_contained_rel(rel)
    if norm is None: refuse "'<rel>' is not a path inside the target, so no step may write it"
    cur = pathlib.Path(target)
    for seg in norm.split("/"):
        cur = cur / seg
        try:
            linked = test_path_linked(cur)
        except (OSError, ValueError):
            refuse "'<rel>': <cur> does not read as a path on this node, ..."
        if linked: refuse "'<rel>': <cur> is a link or other reparse point, ..."
        if not cur.is_dir(): break       # absent, or a file: nothing below it exists
    return pathlib.Path(target) / norm
```

`cur.is_dir()` follows a link, but `cur` has just read False for one. The walk tests the normalised
form, so `a/../b` is tested as `b`, the path that is actually opened.

### Where the refusal lands

| Caller | Site | What the refusal stops |
|---|---|---|
| `write_before_image`, fresh branch | `:1089` | the read of the path's bytes, then the image's `mkdir` and write |
| `write_before_image`, held branch (S6) | `:1075-1083` | `derive_after`, and so the step's own write of that path |
| `read_image_changes` | `:1111` | the `stat` of a listed path |
| `write_from_before_image` | `:1129` | every read in the plan loop, before any write or unlink |
| `read_image_paths` | `:1918` | the walk's staging list, before the down spawns |
| `derive_image_path` (S5) | `:1032-1037` | every image read, `mkdir`, write and unlink, in the walks and the step programs |

A step program such as `tools/govkit/steps/fanout_cap.py:187-194` writes only the paths
`write_before_image` returned, so the fresh branch's test already covers the step's own write.

### What it does not check

- A path whose segments change between the test and the write. The threat is committed content, not
  a concurrent process on the node.
- A hard link, which no lstat can tell from a file.
- A Windows device name such as `NUL` or `COM1`. Writing one does not leave the tree.
- The target root reached through a link. Callers resolve it first (`run_step_walk`,
  `run_reverse_walk`), and the operator chose it.

### Inventory

Minted: the function `derive_contained_rel` in `tools/govkit/upgrade_steps.py`, a top-level name
`memory/map/generated/symbols.json` maps, so this pass regenerates that file.
`python tools/lexicon/lexicon.py --suggest derive_contained_rel --as py.function` answered OK on
2026-10-28, leading with the declared verb `derive`. The arm tag `[dSP-72]` is minted. Two new
`raise Refusal` sites in `check_contained`, the link refusal and the unreadable-name refusal, each
reached by an arm row (AC3, AC4). `BRANCH_PIN` in
`tools/govkit/refusal_join.py:41` is a floor (`:296`), so a new branch leaves it green, and the arm
below is what reaches the branch. No conf key, gate leg, constant or receipt field is minted.

### Migration

None. No receipt or image changes shape.

### Rollout

Live at landing. TOOL-dSafePassage-73, -74 and -75 share order 16 and also write
`tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py`, so M6 sequences the four rather than
running them in parallel. TOOL-dSafePassage-76 builds after this unit. The pass runs
`python tools/codebase-map/gen_map.py --write` and commits `symbols.json` with the code, as
TOOL-dSafePassage-81 §4 Rollout does, so the pre-commit map gate passes.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Call `load_govkit().demand_contained_dest` from `check_contained`.** Its refusal names a
  `deploy.toml` `prefix` as the likely cause, which points a before-image's reader the wrong way,
  and catching it to re-raise is two refusals for one branch.
- **Copy govkit's normalisation into `check_contained`.** That is the two-answers class this unit
  closes, one copy over.
- **The review's added `resolve()` containment assertion.** Once the text is contained and every
  existing segment is lstat-tested, no path reaches a resolved form outside the target, so the
  branch is unreachable. An unreachable refusal is one `tools/govkit/refusal_join.py` cannot see an
  arm reach.
- **Refuse only a link that resolves outside the target**, as govkit's update loop does. The
  review's model is "never follow a link out of the target", and a link inside the target can be
  re-pointed by the next commit. Refusing every link is the narrower grant.

## 5. Production-readiness checklist

- security: this is the change. It closes a write outside the target on `update --rollback`, and
  a read outside it on an up, both from committed adopter content.
- perf / scale: one `lstat` per existing segment of each path an image lists. Images list a few
  paths.
- error / empty / loading states: an absent segment ends the walk, so a path the up will create
  passes. A dangling link reads True, so it is refused rather than read as absent. An empty path,
  `.` or `a/..` names the target itself and is refused by the predicate. A name the node cannot
  open, or one holding a NUL, is refused rather than raised as `OSError` or `ValueError`.
- observability: each refusal names the path and, for a link, the segment that is linked.
- risks: govkit's destinations now refuse a colon anywhere, where they refused only a drive colon
  (§8 F1, resolved). No tracked path in gov holds a colon (0 of 7957 at `83817478`, `git ls-files`).
- testing: the `[dSP-72]` arm in `check_upgrade_steps`, under §7's `New arm:` line.
- migration: none.
- user docs: `help/upgrade-steps.md`, S7.

## 6. Acceptance criteria

The probes run from the repository root. Each imports the module by path, which runs no arm.

- **AC1** — When
  `python -c "import sys; sys.path.insert(0, 'tools/govkit'); import upgrade_steps as us; b = chr(92); bad = ['..' + b + 'E.txt', b + 'Windows' + b + 'x', b + b + 'srv' + b + 'share' + b + 'x', 'C:x', 'C:/x', 'ab:c', 'x/a:b', '/x', '../x', 'a/../../x', '..', '', '.', 'a/' + '..']; print([r for r in bad if us.derive_contained_rel(r) is not None], [us.derive_contained_rel(r) for r in ('a/b', 'a' + b + 'b', 'a/../b')])"`
  runs, it prints `[] ['a/b', 'a/b', 'b']`.
  Red when: the predicate reads the path only as POSIX, so the backslash, rooted and UNC forms
  appear in the first list, as `check_contained` lets them through at base (§4); or `.` is
  returned, so the empty path, `.` and `a/..` appear.
- **AC2** — When the probe below calls `demand_contained_dest` over AC1's fourteen escaping paths and
  over the contained path a/b, it prints `True a/b`: each escaping path raises a `Refusal` carrying
  `leaves the target repository`, and the contained one is returned unchanged.
  Red when: govkit keeps its own test, so `ab:c`, `x/a:b`, the empty path and `.` are returned, as
  a probe at base showed on 2026-10-28.

  ```python
  import sys
  sys.path.insert(0, "tools/govkit")
  import govkit as gk
  b = chr(92)
  bad = [".." + b + "E.txt", b + "Windows" + b + "x", b + b + "srv" + b + "share" + b + "x", "C:x",
         "C:/x", "ab:c", "x/a:b", "/x", "../x", "a/../../x", "..", "", ".", "a/" + ".."]
  def refused(d):
      try:
          gk.demand_contained_dest(d, "probe")
          return False
      except gk.Refusal as e:
          return "leaves the target repository" in str(e)
  print(all(refused(d) for d in bad), gk.demand_contained_dest("a/b", "probe"))
  ```
- **AC3** — When the probe below writes one image per form, it calls `check_contained` and
  `read_image_paths` over each, which write nothing, and `write_from_before_image` over the
  backslash climb alone, whose escape lands inside the probe's scratch directory. Each call raises
  a `Refusal`: `is not a path inside the target` for the climb, the rooted and the UNC forms, and
  `does not read as a path on this node` for a name holding a NUL and, on Windows, for `a?b` and
  `a|b` as a directory name. The scratch directory holds no file outside the targets. It prints
  `True True`.
  Red when: `check_contained` lets the forms through, so a call returns or dies with `OSError` or
  `ValueError` and the first value prints False, and the climb's restore writes `ESCAPED.txt`
  beside its target, so the second prints False. The probe catches every exception, so a run at
  base reads red without writing to the drive root or a share.

  ```python
  import base64, json, pathlib, sys, tempfile
  sys.path.insert(0, "tools/govkit")
  import upgrade_steps as us
  b = chr(92)
  climb = ".." + b + "ESCAPED.txt"
  lexical = [climb, b + "rooted.txt", b + b + "localhost" + b + "c$" + b + "unc.txt"]
  odd = ["a" + chr(0) + "b" + "/x.txt"] + (
      ["a?b" + "/x.txt", "a|b" + "/x.txt"] if sys.platform == "win32" else [])
  def outcome(f, *args):
      try:
          f(*args)
          return "returned"
      except us.Refusal as e:
          return str(e)
      except Exception as e:
          return type(e).__name__
  with tempfile.TemporaryDirectory() as td:
      seen = []
      for n, rel in enumerate(lexical + odd):
          t = pathlib.Path(td) / f"c{n}" / "target"
          img = t / ".governance/steps/demo/first.before.json"
          img.parent.mkdir(parents=True)
          img.write_text(json.dumps({"step": "demo/first", "paths": {rel: {
              "before": base64.b64encode(b"pwned\n").decode(), "after": None}}}), encoding="utf-8")
          calls = [(us.check_contained, t, rel), (us.read_image_paths, t, "demo/first")]
          if rel == climb:
              calls.append((us.write_from_before_image, t, "demo/first"))
          want = ("is not a path inside the target" if rel in lexical
                  else "does not read as a path on this node")
          seen += [want in outcome(*c) for c in calls]
      stray = [p for p in pathlib.Path(td).rglob("*") if p.is_file() and "target" not in p.parts]
      print(all(seen), stray == [])
  ```

- **AC4** — When the probe plants a junction on Windows (`cmd /c mklink /J`), or a directory
  symlink elsewhere, at `<t>/lnk` pointing to a sibling `outside/`, and a second target whose
  `.governance` is such a link, then: `write_from_before_image` over an image listing a file
  planted.txt under lnk raises a `Refusal` naming `lnk` and `reparse point`; `write_before_image`
  for the step demo/second, its `derive_after` naming a file secret.txt under lnk, raises the same
  and writes no image; `derive_image_path` on the second target raises naming `.governance`; a
  dangling link at `<t>/gone`, listed with a file under it, is refused; and the control, an image
  listing a file under a plain directory, restores that file. `outside/` stays empty throughout.
  Red when: `check_contained` tests no segment, so planted.txt is written under outside and the
  image holds the bytes of the secret.txt under outside, as the base probe showed; or a
  refuse-everything walk fails the plain-directory control.
- **AC5** — When an image already lists a file secret.txt under `lnk`, a link, and
  `write_before_image` is called with a `derive_after` that appends to a list, it raises a
  `Refusal` naming `lnk`, and the list is empty.
  Red when: the held branch hands the before bytes to `derive_after` with no path tested.
- **AC6** — When
  `awk '/^## /{s=$0} /A before-image path outside the repository/{print s}' help/upgrade-steps.md`
  runs, it prints `## Rolling back`.
  Red when: the bullet is absent, or sits under another section.
- **AC7** — When `git grep -n -e "ntpath.isabs" -e "PurePosixPath(rel)" -- "tools/govkit/*.py"`
  runs, it prints one line, inside `derive_contained_rel`.
  Red when: `demand_contained_dest` or `check_contained` keeps a containment test of its own, so a
  second line prints, as `tools/govkit/govkit.py:1246` and `tools/govkit/upgrade_steps.py:1042` do
  at base.
  What this does not check: a containment test spelled another way, such as an inline `".." in`
  over `parts`.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `policy fixtures` · `codebase-map coverage + freshness` · `upgrade-walk` · `docs` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 AC5 · `check_upgrade_steps` gains `[dSP-72]` checks, each calling only `check_contained` and `read_image_paths` for a form that can leave the scratch tree, beside the `[dSP-1 S3]` containment check at `:3093-3094`, its junction plant shaped as `[dSP-56]`'s at `:4088-4092`; observed RED at base 83817478, where `check_contained` reads only `PurePosixPath` and tests no segment, and GREEN after the build · none

## 8. Open questions

- **F1 — Does the one predicate refuse a colon anywhere, for govkit's destinations too?**
  - (a) Yes. `check_contained` refuses any colon today, which keeps an NTFS alternate data stream
    `a:b` out of a before-image. govkit's destinations become stricter: today they refuse only a
    colon at index 1. No tracked path in gov holds a colon (0 of 7957 at `83817478`), and Windows
    admits a colon in no file name, so the cost is an adopter `prefix` that names a stream.
  - (b) No. The predicate keeps govkit's rule, a colon at index 1, and `check_contained` loosens to
    it, so a before-image may name `a:b` on Windows. That is a write inside the target, into a
    stream of `a`, and AC2's table loses `a:b`.
  - (c) The predicate keeps govkit's rule and `check_contained` keeps its own `":" in rel` beside
    it. That keeps two answers to one question, the class this unit closes.
  - Recommendation: (a). It denies by default, and no shipped path holds a colon.
  - RESOLVED (agent, 2026-10-28, delegated): (a), the shared containment test refuses a colon
    anywhere, govkit's install destinations included. Rung 3, the mandate delegates it: (a) meets
    every criterion and trips no veto, since it narrows a write surface rather than widening one,
    so no standing ruling is invoked and no `widens:` or `relaxes:` field applies.

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, closing H1 (id 1) and H2 (id 2) of
  `memory/builds/dSafePassage/reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md`,
  by `memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-72-1-spec-writer.md`.
- rev-2 · 2026-10-28 · §8 F1 · S1 · AC2 · F1 resolved as delegated by the coordinator, option (a): a
  colon anywhere is refused for both callers; AC2's note on option (b) is struck.
- rev-3 · 2026-10-28 · AC1 · AC2 · AC4 · AC5 · the scratch fixtures' file paths are respelled so no
  backticked token in a criterion reads as a repository path: AC1 and AC2 use the contained path
  a/b with no extension, and AC4 and AC5 name their planted files in prose.
- rev-4 · 2026-10-28 · S1 · S2 · S4 · §4 · §5 · §7 · AC1 · AC2 · AC3 · folded
  `memory/builds/dSafePassage/reviews/2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md`:
  M5, the colon forms past index 1 that govkit passes at base; M6, the UNC row corrected and AC3
  calling no write path with a form that can leave the scratch tree; M14, an unreadable name or a
  NUL refused, not raised; M15, an empty path, `.` and `a/..` refused; L7, the rooted form credited
  to the fold; L14, govkit's docstring and its unused ntpath import; and this spec's part of M11
  and L5, `symbols.json` in Files touched with `codebase-map coverage + freshness` and
  `recall floor` on the leg line. The header's node reads `a`, the host the probes ran on.

## 10. Reuse audit

The seams extended are two. `demand_contained_dest` (`tools/govkit/govkit.py:1219-1253`) already
answers the lexical question correctly for govkit, and S1 moves its decision into the step module,
which govkit binds from at load as TOOL-dSafePassage-35 S24 did for `demand_safe_token`.
`test_path_linked` (`tools/govkit/upgrade_steps.py:1417-1425`) is the walk's one link test, and S4
is its third caller. `python tools/codebase-map/reuse_lookup.py "refuse a repo-relative path that
escapes the target through backslash, drive or a link before writing"` ranked `write`, `before`,
`write_text`, `repo_root` and other name-token matches, none a containment helper, so neither seam
came from the map; both came from the review and the code. The recall probe ranked the review's H2
second and TOOL-dSafePassage-59's `test_path_linked` sixth, and its eighth hit, an aScouredKit
security lens, records govkit's update loop refusing a junction by resolve-and-compare, the rule §4
rejects for this caller.

Recall terms used: `python tools/memory-recall/query.py "how does govkit refuse a destination path that leaves the target repository, and how is a link or junction refused" --terms "containment demand_contained_dest check_contained backslash ntpath junction reparse test_path_linked before-image escape"`
