# TOOL-dSafePassage-90 — a case-only rename is refused by name where the filesystem folds case, so no rollback restores one file under two spellings

**Status:** DEFERRED · rev-2 · 2026-10-29 · node a · Tier-2 · base cbaaeebe · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-prompt-TOOL-dSafePassage-90-1-spec-writer.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-90-1-spec-writer.md) | journal | — |
| [2026-10-29-prompt-TOOL-dSafePassage-90-2-spec-writer.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-90-2-spec-writer.md) | journal | — |
| [2026-10-29-prompt-TOOL-dSafePassage-90-audit-fold-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-90-audit-fold-brief.md) | research | TOOL-dSafePassage-91 |
| [2026-10-29-prompt-TOOL-dSafePassage-90-build-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-90-build-brief.md) | journal | — |
| [2026-10-29-prompt-TOOL-dSafePassage-90-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-90-spec-brief.md) | research | TOOL-dSafePassage-91 |
| [2026-10-29-review-TOOL-dSafePassage-90-91-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dSafePassage-90-91-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-91 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 closing diff review's one high, H1 (id 3), is a rollback that deletes the file it has
just restored and reports it restored. The trigger is a case-only rename on a case-insensitive
filesystem. Three more of its findings, M1 (id 1), M2 (id 2) and M3 (id 5), share the cause:
TOOL-dSafePassage-88's `samefile` arm lets a case-only rename through the occupancy refusal to
`git mv`. This unit takes that arm out of the test, so a case-only rename on such a filesystem is
refused again, as it was at `b634d60e5`. The refusal now names the cause and a remedy, and no longer
tells the adopter to remove their own file. That closes H1 and M2, leaves M1 and M3 unreachable, and
reverts the round-1 spec audit's M5 (id 18).

## 2. Scope (IN)

- **S1** — The occupancy test reads the exact spelling only. In `_cmd_update`'s `renamed` write arm
  (`tools/govkit/govkit.py:11062`), the local `own_file` and its `samefile` arm (`:11078`) leave the
  test. The occupancy refusal (`:11109`) reads
  `if not in_place and (new_dest in _at_dest or ndp.exists()):`, so one predicate, `in_place`
  (`:11079`), decides both the refusal and the move block (`:11167`). The refusal keeps its one
  `r.fail` call, and its message is picked three ways. Where the destination is the row's own file
  by `samefile` and the two spellings are equal under `casefold`, it names a case-only rename and its
  remedy. Where `samefile` holds and they are not, it names the row's own file under another name,
  a link or a filesystem alias, and tells the adopter to take their link out of the way. Everywhere
  else it reads as it does now. The comment at `:11073-11076` says so. This closes H1 (id 3) and M2 (id 2): the row is refused before any byte
  moves, so the rollback has nothing to restore. It leaves M1 (id 1) unreachable: the index arm is
  skipped only in place. §4 "Each finding, after S1" gives the code lines. §4 "S1". Observed by AC1
  and AC2.
  **Readers:** by name: `tools/govkit/govkit.py` is the one file that spells `own_file`, at `:11078`
  and `:11109`, and this item rewrites both lines. by value: the occupancy test at
  `tools/govkit/govkit.py:11109` is the one reader of its value; `in_place` keeps deciding the move
  block at `:11167` and the arms at `:11194`, `:11212` and `:11220`.
- **S2** — The arm. The case-only check of the `DEPL-dCarriedReceipt-11` block of
  `tools/govkit/selftest.py` (`:13112-13124`) becomes a `[dSP-90]` check on the same fixture. On a
  filesystem that folds case it requires exit 1, the case-only refusal text, the target's index
  holding the one old spelling, and the row's bytes at that spelling. On one that does not, it
  requires exit 0 and the index at the new spelling. It reads the target's index and disk, never the
  receipt row the arm writes whether or not `git mv` ran (`govkit.py:11206`). That closes M3 (id 5)
  at its corrected fix's class. The in-place `[dSP-88]` check (`selftest.py:13106`) is not moved.
  §4 "S2". Observed by AC3.

## 3. Non-goals (OUT)

- The review's fix for H1 and M2, which keeps the case-only move and teaches the snapshot and the
  restore loop two spellings of one file. §4 "Which mechanism" weighs it, and §4 "Alternatives
  rejected" says why it is not built.
- A gov-side gate refusing a case-only rename in gov's own tree. Gov's history holds none (§4
  "Which mechanism"), so it would guard a change nobody has made.
- L1 (id 4), the in-place row's doubled snapshot path, and M4 (id 6) and L2 (id 7). The brief
  batches all three into TOOL-dSafePassage-91.
- TOOL-dSafePassage-88's spec. It is CLOSED and is not edited. Its §2 S1, §4 "Adopters meet it" and
  AC5 describe the `samefile` arm this unit takes out of the test.
- The coverage `GAP` line that `update` prints for the new spelling of a refused case-only row. It
  prints the same at `cbaaeebeb` with and without S1, and no review item names it.

### Edges

- **hands-off** `TOOL-dSafePassage-91` — the round-3 review's L1 (id 4), M4 (id 6) and L2 (id 7),
  which that unit batches; its L1 fix edits `govkit.py`'s pre-write snapshot (`:10745-10747`), which
  this unit does not touch, and its L1 check sits after this unit's `[dSP-90]` check in the
  `DEPL-dCarriedReceipt-11` block of `selftest.py`, which is the one block the two units share

## 4. Design

Every cited line holds at `cbaaeebeb`, the build head with TOOL-dSafePassage-86, -87, -89 and -88
landed. Outside `memory/`, HEAD of this branch matched it when this spec was written, and at rev-2
`git diff --stat cbaaeebeb a3ad798cf -- tools skills` printed nothing, so every line still holds
at `a3ad798cf`.

### Which mechanism

The brief offers two mechanisms.

- **(a) The review's fix.** Keep the case-only move. Teach the snapshot (`govkit.py:10745-10747`) and
  the restore loop (`:8390-8461`) to treat the two spellings as one path, by ordering the absent-before
  spelling first or by guarding the unlink at `:8426` with `samefile`. M1 needs its own fix at
  `:11109`, and M3 needs a stronger check.
- **(b) The arm out of the test.** A case-only rename is refused as an occupied destination again,
  as at `b634d60e5` (`:11101` there), with a refusal that names the case-only cause and a remedy.

This unit builds (b), for four reasons.

1. **It loses no data, measured.** With S1 staged, the probe's held-back kit keeps the row's file
   on disk with its pre-run bytes and one index entry. At `cbaaeebeb` the same run deletes the file
   and reports it restored (§4 "Measured at writing time").
2. **No gov commit has needed the move.**
   `git log --name-status --diff-filter=R --format= -M | awk -F'\t' 'tolower($2)==tolower($3) && $2!=$3'`
   printed nothing at `cbaaeebeb` on 2026-10-29, and so did the same over `git log --all` scoped to
   `tools`. The `samefile` arm serves a rename gov has never shipped.
3. **The arm reached three readers, and (a) fixes only those found.** The occupancy test's index arm
   (id 1), the snapshot and restore loop (ids 2 and 3), and the arm's own check (id 5) each assume
   that one row is one spelling. So do `written_paths` (`:11718`), the `_left` test (`:8524`) and the
   rollback's list removal (`:12288-12290`). Under (a) each of them must be audited for one file held
   under two spellings. Under (b) none of them meets that state.
4. **Its cost is bounded, and the refusal now says so.** M5's consequence returns, narrowed. On a
   case-insensitive filesystem the kit holding a case-only renamed row is held back until gov's
   spelling differs by more than case, or until `update` runs on a case-sensitive checkout. The
   message no longer tells the adopter to remove their own file.

The adopter's own `git mv` to the new spelling is not a remedy, measured: the next `update` exits 2
with `present in the target's WORKTREE and absent from its INDEX`, because the receipt still names
the old spelling. So the remedy does not name it. The case-sensitive remedy is reasoned from
`:11109`: there `ndp.exists()` is false and `ls-files` holds no entry at the new spelling, so the row
takes the ordinary rename path, which the `[-11]` move checks hold. It was not measured on this node,
which folds case.

This reverts the round-1 spec audit's M5 (id 18). Its left-shift, that a path-identity test uses
`samefile`, is kept: `samefile` and `casefold` now decide only which message the refusal prints.

### Each finding, after S1

- **H1 (id 3) and M2 (id 2), closed.** A case-only row is refused at `:11109`, before the byte
  decision (`:11116-11159`) and the move (`:11167`). It never reaches `renamed.extend` (`:11215`), so
  neither spelling joins `written_paths` (`:11718`). The restore loop marks both paths `untouched`
  (`:8407-8409`) and never reaches the absent-before branch's `git rm --cached` (`:8411-8424`) or its
  unlink (`:8426-8427`).
- **M1 (id 1), unreachable.** The index arm `new_dest in _at_dest` is skipped only when `in_place`,
  that is when `new_dest` is the row's own path string. Its `_at_dest` entry is then the row's own,
  because one index path is one entry. A case-only `new_dest` beside a colliding entry, such as
  `D/x` beside `d/x`, is not in place, so `new_dest in _at_dest` refuses it, as at `b634d60e5`.
- **M3 (id 5), closed by S2.** M3's mutant, `in_place = own_file`, separates two rules that S1 makes
  one: `in_place` decides both the refusal and the move. The rewritten check reads the target's
  index and bytes, not the receipt that `:11206` writes unconditionally.

### S1

At `govkit.py:11073-11079`:

```python
            # TOOL-dSafePassage-88: the target's descriptor answers this row's own path, as it does for
            # every row when gov moves its tool root, so the file stays and only its source changes.
            # TOOL-dSafePassage-90: only the exact spelling is the row's own path. A case-only rename on
            # a case-insensitive filesystem names the row's own file under a second spelling, and the
            # rollback restores a row's spellings as separate paths, so the move is refused, by name.
            _own = target / row["path"]
            in_place = new_dest == row["path"]
```

At `:11109-11114`, the one `r.fail` call takes a three-way message, so the refusal join's count
does not move:

```python
            if not in_place and (new_dest in _at_dest or ndp.exists()):
                _alias = ndp.exists() and _own.exists() and ndp.samefile(_own)
                _case = _alias and new_dest.casefold() == row["path"].casefold()
                r.fail(f"gov moved '{row.get('source')}' to '{new_src}', which resolves to "
                       f"'{new_dest}' — this row's own file '{row['path']}' under a second spelling, "
                       f"as a case-only rename is on a case-insensitive filesystem. Refusing the move: "
                       f"a rollback cannot restore one file held under two spellings. The file is "
                       f"untouched, so do not move or remove it; run `update` from a checkout on a "
                       f"case-sensitive filesystem, where the new spelling is a second path" if _case else
                       f"gov moved '{row.get('source')}' to '{new_src}', which resolves to "
                       f"'{new_dest}' — the row's own file '{row['path']}' under another name (a link "
                       f"or a filesystem alias). Refusing the move: a rollback cannot restore one file "
                       f"held under two names. The file is untouched. If '{new_dest}' is a link you "
                       f"made, remove the link and re-run" if _alias else
                       f"gov moved '{row.get('source')}' to '{new_src}', which resolves to "
                       f"'{new_dest}' — and this target ALREADY holds a file there. Refusing rather "
                       f"than overwriting it: `update` moves one row and would be destroying "
                       f"another file's bytes to do it. Move or remove '{new_dest}' and re-run")
                continue
```

`samefile` raises when either path is absent, so both are tested first, as 88 tested them. Neither
alias message carries `ALREADY holds a file there`, so the `[-11]` checks that read that text
(`selftest.py:13075-13076`) still read only the occupied-by-another-file refusal. The rest of the arm
is unchanged. A case-only row never reaches the move block, so `in_place` is the one test there too.

`samefile` is an `os.stat` identity, so it also holds for a symlink or hard link at `new_dest` that
names the row's file, on any filesystem, and for a macOS NFC/NFD alias. `ndp` is resolved
(`:11072`), so a symlink reads as its target. That is the round-1 spec audit's M5 (id 13). `_alias`
stays the identity test, and `casefold` only picks the wording: the case-only text is printed only
where the two spellings fold together, and every other alias reads the other-name text, whose remedy
is to take the link out of the way. One shape still reads the case-only text wrongly: a link whose
name differs from the row's only by case, on a case-sensitive filesystem. Its refusal still fires
and no byte moves.

### S2

The block at `selftest.py:13112-13124` reads:

```python
        # TOOL-dSafePassage-90: a case-only rename. Where the filesystem folds case the new spelling is
        # the row's own file, so the move is refused by name and nothing is written; where it does not,
        # the new spelling is a second path and moves. Either way the target's INDEX is read, never the
        # receipt row, which the arm writes whether or not `git mv` ran.
        settle(_t88, "the in-place update")
        _fold90 = (_t88 / "pinned" / "demo" / "KEEP.TXT").exists()
        git(_g88, "mv", "moved/demo/keep.txt", "moved/demo/Keep.txt")
        git(_g88, "commit", "-qm", "C")
        _cs90 = subprocess.run([sys.executable, str(_g88 / "moved" / KIT_NAMES["govkit"] / "govkit.py"), "update",
                                "--target", str(_t88), "--write"],
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
        _ix90 = [p for p in gout(_t88, "ls-files", "--", "pinned/demo").split()
                 if p.lower() == "pinned/demo/keep.txt"]
        check("[dSP-90] a case-only rename is refused by name where the filesystem folds case, and moves where it does not",
              (_cs90.returncode == 1 and "case-only rename is on a case-insensitive filesystem" in _cs90.stdout
               and _ix90 == ["pinned/demo/keep.txt"]
               and read_bytes11(_t88 / "pinned" / "demo" / "keep.txt") == b"one\ntwo\nthree\nFOUR\n")
              if _fold90 else (_cs90.returncode == 0 and _ix90 == ["pinned/demo/Keep.txt"]),
              f"fold {_fold90} update {_cs90.returncode} {_ix90} " + _cs90.stdout[-1500:])
```

It reuses `gout` (`selftest.py:9779`), `settle` (`:587`), `git` (`:583`) and `read_bytes11`
(`:12165`), all in scope at the block, as the `[-11]` checks use them. The bytes are the ones the
in-place check before it requires (`:13109`). On a node that folds case, as node a does, the check
observes S1. On one that does not, it observes the ordinary move and not S1.

### The probe

`p90_probe.py`, run from the repository root. Its one optional argument is the engine directory,
`tools/govkit` by default. It runs three updates, each in a fresh scratch gov at `pinned` and a
target installed there. The first renames only `keep.txt` to `Keep.txt`. The second also renames
`other.txt` onto `renamed.txt`, a path the adopter's own file holds, so the kit is held back and
rolled back. The third is M5's shape: the adopter commits a hard link `linked.txt` to `keep.txt`, and
gov renames `keep.txt` to `linked.txt`. A hard link stands in for a symlink because NTFS makes one
without a privilege, and `samefile` answers both alike.

```python
import os, pathlib, shutil, subprocess, sys, tempfile
eng = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "tools/govkit").resolve()
sys.path.insert(0, str(eng))
from fixture_target import build_scratch_gov, build_target
tmp = pathlib.Path(tempfile.mkdtemp(prefix="p90-"))
def git(cwd, *a):
    return subprocess.run(["git", "-C", str(cwd), "-c", "user.email=t@e", "-c", "user.name=t", *a],
                          capture_output=True, text=True, check=True).stdout
def run(tag):
    g = build_scratch_gov(tmp / f"gov-{tag}")
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
    (g / "pinned" / "demo" / "keep.txt").write_text("one\ntwo\n", encoding="utf-8", newline="\n")
    (g / "pinned" / "demo" / "other.txt").write_text("other\n", encoding="utf-8", newline="\n")
    git(g, "add", "-A"); git(g, "commit", "-qm", "A")
    t = build_target(tmp, 'gov_source = "local"\nprefix = "pinned"\nkits = ["demo"]\n', f"t-{tag}")
    gk = [sys.executable, str(g / "pinned" / "govkit" / "govkit.py")]
    subprocess.run(gk + ["apply", "--target", str(t), "--kits", "demo"], capture_output=True, check=True)
    git(t, "add", "-A"); git(t, "commit", "-qm", "install")
    if tag == "sibling":
        (t / "pinned/demo/renamed.txt").write_text("the adopter's own file\n", encoding="utf-8", newline="\n")
        git(t, "add", "-A"); git(t, "commit", "-qm", "own file")
        git(g, "mv", "pinned/demo/other.txt", "pinned/demo/renamed.txt")
    if tag == "link":
        os.link(t / "pinned/demo/keep.txt", t / "pinned/demo/linked.txt")
        git(t, "add", "-A"); git(t, "commit", "-qm", "own link")
        git(g, "mv", "pinned/demo/keep.txt", "pinned/demo/linked.txt")
    else:
        git(g, "mv", "pinned/demo/keep.txt", "pinned/demo/Keep.txt")
    git(g, "commit", "-qm", "B")
    up = subprocess.run(gk + ["update", "--target", str(t), "--write"],
                        capture_output=True, text=True, encoding="utf-8", errors="replace")
    disk = (t / "pinned/demo/keep.txt").read_bytes() if (t / "pinned/demo/keep.txt").is_file() else None
    kept = disk == b"one" + bytes([10]) + b"two" + bytes([10])
    if tag == "link":
        print(f"hard link: update exit {up.returncode} | case-only named: "
              f"{'case-only rename' in up.stdout} | other name named: {'under another name' in up.stdout} | bytes kept: {kept}")
        return
    idx = [p.rsplit("/", 1)[1] for p in git(t, "ls-files", "--", "pinned/demo").split() if p.lower() == "pinned/demo/keep.txt"]
    print(f"case-only {tag}: update exit {up.returncode} | second spelling named: "
          f"{'under a second spelling' in up.stdout} | index: {idx} | bytes kept: {kept}"
          + (f" | occupied refused: {'ALREADY holds a file there' in up.stdout}" if tag == "sibling" else ""))
print("case-insensitive:", (pathlib.Path(eng) / "GOVKIT.PY").exists())
run("alone")
run("sibling")
run("link")
```

### Measured at writing time

Measured on 2026-10-29 on node a, where `git config core.ignorecase` reads `true`. "S1 staged" is a
scratch copy of `tools/govkit` with §4 "S1" applied as written. At rev-1 the probe ran only its
first two updates, in about 15 s. At rev-2, with the third update added, it ran in about 20 s, and
the engine at `a3ad798cf` and the S1-staged engine were re-run, and each printed the same first
three lines as at rev-1.

- **The probe at `cbaaeebeb`.** `case-insensitive: True`, then
  `case-only alone: update exit 0 | second spelling named: False | index: ['Keep.txt'] | bytes kept: True`,
  then
  `case-only sibling: update exit 1 | second spelling named: False | index: ['keep.txt'] | bytes kept: False | occupied refused: True`.
  The sibling run's `git status --porcelain`, read in a first version of the probe, showed
  ` D pinned/demo/keep.txt`, while its verify line read `ROLLED BACK` and named both spellings
  restored. That is H1 reproduced. At rev-2 the fourth line read
  `hard link: update exit 1 | case-only named: False | other name named: False | bytes kept: True`.
- **The probe, S1 staged.** `case-insensitive: True`, then
  `case-only alone: update exit 1 | second spelling named: True | index: ['keep.txt'] | bytes kept: True`,
  then
  `case-only sibling: update exit 1 | second spelling named: True | index: ['keep.txt'] | bytes kept: True | occupied refused: True`.
  The sibling run's verify line read `ROLLED BACK · (no path restored)`. At rev-2 the fourth line
  read `hard link: update exit 1 | case-only named: False | other name named: True | bytes kept: True`.
- **S1 staged with rev-1's two-way message.** That is `_case = _alias`, so every alias prints the
  case-only text, which is M5 (id 13). The fourth line read
  `hard link: update exit 1 | case-only named: True | other name named: False | bytes kept: True`.
- **The bare string test staged without the message.** That is `own_file = new_dest == row["path"]`
  with the message unchanged, run alone and with the refused sibling. Each read `update exit 1`, the
  index `['keep.txt']` and `keep.txt` on disk, and the sibling run's verify line read
  `(no path restored)`. Then `git mv` of the row's file to the new spelling in the target, committed,
  and a second `update --write` exited 2 with `these receipt-claimed path(s) are present in the
  target's WORKTREE and absent from its INDEX`.

S2's check was not run inside the govkit selftest. The probe's first run is its fixture's step in
miniature, without the root move that precedes it there.

### Inventory

Minted: the locals `_alias` and `_case`, the case-only and other-name refusal messages, the check
label `[dSP-90]`, and the
locals `_fold90`, `_cs90` and `_ix90`. The local `own_file` goes from `govkit.py` (S1's readers). No
function, `Refusal` site, flag, conf key, gate leg or receipt field is added. The refusal join's
anchors do not move, because the occupancy refusal keeps its one `r.fail` call. The `[dSP-88]` label
then marks one check, the in-place one.

### Migration

None. No receipt field changes. A target that took a case-only move under 88 holds the new spelling
in its receipt and index, and S1 never revisits that row.

### Rollout

Live at landing, at order 16, after TOOL-dSafePassage-88. TOOL-dSafePassage-91 builds after this
unit. In `govkit.py` it edits the pre-write snapshot (`:10745-10747`), which this unit does not
touch. In `selftest.py` its L1 check sits after this unit's `[dSP-90]` check in the
`DEPL-dCarriedReceipt-11` block, the one block the two units share.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **(a), the review's fix, in either form.** Restoring the absent-before spelling first, or skipping
  the unlink when that spelling is `samefile` to one restored in the row, closes H1 and M2. It keeps
  a move no gov commit has needed, needs M1's and M3's fixes beside it, and leaves `written_paths`,
  `_left` and the rollback's list removal reasoning about one file under two spellings (§4 "Which
  mechanism").
- **Decide the alias by a lowercase compare.** That answers a string question about a filesystem
  fact. `samefile` is the filesystem's own answer, and it is the audit's left-shift. `casefold`
  only picks which alias message prints, after `samefile` has said the two names are one file.
- **One alias message for every alias, the case-only text.** That is rev-1's form. It tells an
  adopter whose own link sits at gov's new name that the cause is case folding, and sends them to
  a case-sensitive checkout they may already be on (M5, id 13).
- **Keep the bare message.** It tells the adopter to move or remove `'<new spelling>'`, which on a
  case-insensitive filesystem is their own installed file.

## 5. Production-readiness checklist

- security: the occupancy guard refuses every rename whose destination string is not the row's own
  path, case-only renames included, so `git mv` never overwrites an index entry through a folded
  spelling (M1). No new write path, spawn or surface.
- perf / scale: one `samefile` call and one `casefold` compare, and only on a row already being
  refused.
- error / empty / loading states: a case-only row on a case-insensitive filesystem is refused with a
  message naming the cause, the untouched file and a remedy. Its kit is held back, as any refused
  row's kit is.
- observability: the refusal names both spellings, and either the case-only cause or a link or
  filesystem alias.
- risks: an adopter past a gov case-only rename on Windows or macOS keeps that kit held back on every
  run until gov's spelling differs by more than case or the update runs on a case-sensitive checkout.
  No gov commit has made such a rename (§4 "Which mechanism").
- testing: §7's New arm, and AC1 to AC3.
- migration: none.
- user docs: none. `git grep -n -i -e "case-insensitive" -e "rename" -- help/` names only
  `help/step-gate.md:4`, which is about a step whose installed file disappears. No page describes
  `update`'s rename refusals.

## 6. Acceptance criteria

- **AC1** — When §4 "The probe", saved under the temp root as `p90_probe.py`, runs with `python` from the repository root on a
  node whose filesystem folds case, its second line reads
  `case-only alone: update exit 1 | second spelling named: True | index: ['keep.txt'] | bytes kept: True`,
  and its third reads
  `case-only sibling: update exit 1 | second spelling named: True | index: ['keep.txt'] | bytes kept: True | occupied refused: True`,
  and its fourth reads
  `hard link: update exit 1 | case-only named: False | other name named: True | bytes kept: True`.
  Red when: the `samefile` arm stays in the occupancy test, so the second line reads
  `update exit 0 | second spelling named: False | index: ['Keep.txt']` and the third reads
  `bytes kept: False`, as at `cbaaeebeb`; or `_alias` alone picks the case-only text, so the fourth
  reads `case-only named: True | other name named: False`, as measured with that form staged.
  cost: about 20 s.
  fixture: two scratch govs and targets under the temp root, and a case-insensitive filesystem, as
  on node a, where the probe's first line reads `case-insensitive: True`. The tree holds none today.
  On a case-sensitive filesystem the probe observes nothing of S1's case-only half. The fourth line
  needs `os.link`, which NTFS grants without a privilege.
- **AC2** — When `git grep -n -e "own_file" -e "samefile" -- tools/govkit/govkit.py` runs, it prints
  one line, the `_alias` test inside the occupancy refusal; and
  `git grep -n -F "case-only rename is on a case-insensitive filesystem" -- tools/govkit/govkit.py`,
  `git grep -n -F "casefold()" -- tools/govkit/govkit.py` and
  `git grep -n -F "under another name (a link" -- tools/govkit/govkit.py` each print one line.
  Red when: the arm stays in the test, so the first grep prints the `own_file` lines at `:11078` and
  `:11109` and the other three print nothing, as at `a3ad798cf`.
- **AC3** — When `git grep -n -F "[dSP-90]" -- tools/govkit/selftest.py` runs, it prints one line,
  inside the `DEPL-dCarriedReceipt-11` block, and `git grep -n -F "[dSP-88]" -- tools/govkit/selftest.py`
  prints one line, the in-place check.
  Red when: the arm is absent, so the first grep prints nothing and the second prints two lines, as
  at `cbaaeebeb`.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `upgrade-walk` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · the `[dSP-90]` check in the `DEPL-dCarriedReceipt-11` block, staged red on a case-insensitive node by the `samefile` arm kept in the occupancy test, which moves the row so the update exits 0 and the index holds the new spelling · none

The `{prefix}/govkit/` legs and `policy fixtures` are the guard join's for the two files; their other
guards are broad. `govkit refusal join` stays green with its pin unmoved, because no refusal call site
is added or removed. `upgrade-walk` runs the moved-prefix walk that the in-place half of the arm
serves, and S1 does not change the in-place path.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-90-1-spec-writer.md` and its
  brief `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-90-spec-brief.md`.
  It closes the round-3 closing diff review,
  `memory/builds/dSafePassage/reviews/2026-10-29-review-TOOL-dSafePassage-86-87-89-88-closing-diff-round3.md`,
  H1 (id 3) and M2 (id 2), and shows M1 (id 1) unreachable and closes M3 (id 5), which move here from
  TOOL-dSafePassage-91 as the brief directs. The brief's option (b) was chosen over the review's fix
  (§4 "Which mechanism"). H1 was reproduced at `cbaaeebeb`, and S1 was staged in a scratch copy of the
  engine and measured.
- rev-2 · 2026-10-29 · §2 S1 · §3 Edges · §4 S1, The probe, Measured, Inventory, Rollout,
  Alternatives rejected · §5 · AC1 · AC2 · folded the round-1 spec audit,
  `memory/builds/dSafePassage/reviews/2026-10-29-review-TOOL-dSafePassage-90-91-spec-audit-round1.md`,
  from its brief
  `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-90-audit-fold-brief.md`.
  M5 (id 13), at the skeptic's corrected fix: `_alias` stays the identity test and `casefold` picks
  the case-only or other-name wording; the probe gained a hard-link run, measured green with the fix
  and red with rev-1's wording. L1 (ids 3, 5), this unit's half: the Edges and Rollout notes name
  `selftest.py`'s `DEPL-dCarriedReceipt-11` block as the one block shared with TOOL-dSafePassage-91.
  Every cited line was re-verified at `a3ad798cf`. AC1 names its probe by its bare filename, so
  every backticked path in §6 is tracked.

## 10. Reuse audit

S1 changes `_cmd_update`'s existing `renamed` write arm (`tools/govkit/govkit.py:11062`) in place.
It keeps the occupancy refusal's one `r.fail` call and its `samefile` identity test, which now picks
the message. S2 rewrites the case-only check inside the `DEPL-dCarriedReceipt-11` block of
`tools/govkit/selftest.py` on 88's fixture, `build_rename_gov` (`selftest.py:12209`), and reads the
index through the block's `gout` (`:9779`), as the `[-11]` checks do. No new seam.
`python tools/codebase-map/reuse_lookup.py "refuse a case-only rename whose new spelling is the row's own file on a case-insensitive filesystem"`
ranked name-stem matches (`rows`, `row`, `extract_row`, `CensusRefused`), none of which decides a
rename, so no existing seam fits beyond the arm this unit edits. The recall probe ranked
DEPL-dCarriedReceipt-14 first, the unit that built the rollback. Its spec restores a renamed row
"under BOTH spellings" as two paths, which is the assumption S1 keeps true. Then it ranked this
build's round-3 review and the round-1 spec audit's M5, which S1 reverts.

Recall terms used: `python tools/memory-recall/query.py "update refuses or moves a case-only rename on a case-insensitive filesystem, and the rollback restores both spellings" --terms "case-only rename case-insensitive samefile own_file in_place occupancy refusal ALREADY holds rollback snapshot restored unlink DEPL-dCarriedReceipt-14"`
