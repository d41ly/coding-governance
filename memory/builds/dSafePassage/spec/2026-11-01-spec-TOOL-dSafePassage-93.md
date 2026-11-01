# TOOL-dSafePassage-93 — the round-4 closing review's two minors: an arm that triggers the link-or-alias refusal, and the set_environ claim narrowed

**Status:** DEFERRED · rev-1 · 2026-11-01 · node a · Tier-2 · base 2e6d4845 · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-prompt-TOOL-dSafePassage-92-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-92-spec-brief.md) | research | TOOL-dSafePassage-92 |
| [2026-11-01-prompt-TOOL-dSafePassage-93-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-93-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-4 closing diff review confirmed two minors that TOOL-dSafePassage-92 does not take. First,
the refusal text TOOL-dSafePassage-90 added for a link or filesystem alias at gov's new name is
triggered by no gate, medium id 2. Second, the record claims `set_environ` holds every environment
use in `selftest.py`, and two hand-typed copies remain, low id 4. This unit closes both at the fixes
the review's skeptic judged sound. For id 2 that is the finder's fix: a `[dSP-90]` sibling arm on
p90's hard-link case. For id 4 it is the skeptic's corrected fix: the claim narrowed in this unit's
record. BUILD-METHOD M4 batches the minors into one unit. It builds after TOOL-dSafePassage-92,
which edits the same file.

## 2. Scope (IN)

- **S1** — id 2, an arm that triggers the link-or-alias text. In the `DEPL-dCarriedReceipt-11` block
  of `tools/govkit/selftest.py`, a `[dSP-93]` check sits after `[dSP-91 L1]` (`:13168`) and before
  the `mvfail` fixture (`:13173`). The fixture is a fresh `build_rename_gov` at `pinned` and its
  installed target. In that target, the adopter commits a hard link `pinned/demo/linked.txt` to
  `pinned/demo/keep.txt`. Gov then renames `keep.txt` to `linked.txt`, and `update --write` runs.
  The check asserts exit 1, `under another name (a link` in stdout, `case-only rename is on a
  case-insensitive filesystem` absent from stdout, and `keep.txt`'s bytes unchanged. §4 "S1".
  Observed by AC1 and AC2.
- **S2** — id 4, the claim narrowed. This unit's acceptance ledger states that `set_environ` holds
  the three copies in `check_step_isolation` and the new `check_floor_bash`, at `selftest.py:3787`,
  `:4422`, `:4452` and `:4462`. It states that the `GOVKIT_NO_REMOTE_PROBE` copy (`:6358-6366`) and
  the `GOV_BASH` copy (`:18418-18432`) are still typed by hand. And it names what it corrects: the
  TOOL-dSafePassage-91 commit message (`2e6d48453`) and that unit's ledger
  (`memory/builds/dSafePassage/build/2026-10-29-build-TOOL-dSafePassage-91-ledger.md:10-11`), each of
  which says `set_environ` holds all four environment uses. Neither is edited. §4 "S2". Observed by AC3.

## 3. Non-goals (OUT)

- Ids 1 and 3 of the review. TOOL-dSafePassage-92 closes both with one predicate.
- Moving `:6358` and `:18418` onto `set_environ`. The skeptic's correction marks this optional. The
  review blames nothing in this range on those two copies, which sit at the base, and the brief keeps
  this unit to a test-arm correction. A follow-up can take it, with the `_BASH` restore at `:18418`
  kept beside it, as the correction says.
- A pattern guard over the tree for hand-typed environment restores. The correction marks it optional,
  and a guard would need an allow-list for the deliberate suite-wide sets at `:5407` and `:6373`.
- Editing spec 91 or its ledger. Spec 91 is CLOSED, and a commit message cannot be edited.
- A symlink in place of the hard link. NTFS makes a hard link without a privilege, and `samefile`
  answers both alike (spec 90 §4 "The probe").
- The checklist entries the review's left-shift notes name. The review records that no checklist is
  present, and S1's arm is id 2's gate.

### Edges

- **consumes-from** `TOOL-dSafePassage-92` — that unit takes ids 1 and 3, which this unit's scope
  leaves out, and it rewrites `check_floor_bash`, which S2's narrowed claim names. Both units edit
  `selftest.py`, and this one builds second, so every line it cites is re-read after 92 lands.

## 4. Design

Every cited line holds at `2e6d48453`, the build head with TOOL-dSafePassage-90 and -91 landed.
TOOL-dSafePassage-92 adds lines inside `check_floor_bash` (`selftest.py:4430`) before this unit
builds. So every line after `:4467` moves, and the builder finds each anchor by its content. Each
measurement was taken on 2026-11-01 on node a, where `core.ignorecase` reads `true`.

### S1: the hard-link arm

The refusal at `tools/govkit/govkit.py:11111-11128` picks its text from `_alias`, which is
`samefile` (`:11112`), and `_case`, which is `_alias` plus a case-folded match (`:11113`). A hard link
at a name that differs by more than case is `_alias` and not `_case`, so it reads the "under another
name (a link or a filesystem alias)" text (`:11120-11124`). `[dSP-90]` (`selftest.py:13142-13147`)
runs only a case-only rename, so nothing in the bar reaches that branch.

The arm, between the `[dSP-91 L1]` check and `_g11c = build_rename_gov("mvfail")`:

```python
        # TOOL-dSafePassage-93: the adopter's own hard link at gov's new name. The new name is the row's
        # own file under another name, never a second spelling, so the move is refused naming the link
        # and nothing is written. A hard link stands in for a symlink: NTFS makes one without a
        # privilege, and `samefile` answers both alike.
        _g93 = build_rename_gov("link", _kit88, "pinned", {"keep.txt": "one\ntwo\n"})
        _t93 = build_target(tmp, 'gov_source = "local"\nprefix = "pinned"\nkits = ["demo"]\n', "rn-link-t")
        _ap93 = subprocess.run([sys.executable, str(_g93 / "pinned" / KIT_NAMES["govkit"] / "govkit.py"), "apply",
                                "--target", str(_t93), "--kits", "demo"],
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
        os.link(_t93 / "pinned" / "demo" / "keep.txt", _t93 / "pinned" / "demo" / "linked.txt")
        settle(_t93, "the install and the adopter's own link")
        git(_g93, "mv", "pinned/demo/keep.txt", "pinned/demo/linked.txt")
        git(_g93, "commit", "-qm", "B")
        _up93 = subprocess.run([sys.executable, str(_g93 / "pinned" / KIT_NAMES["govkit"] / "govkit.py"), "update",
                                "--target", str(_t93), "--write"],
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
        check("[dSP-93] a rename onto the adopter's own link to the row's file is refused naming the link, not case folding",
              _ap93.returncode == 0 and _up93.returncode == 1 and "under another name (a link" in _up93.stdout
              and "case-only rename is on a case-insensitive filesystem" not in _up93.stdout
              and read_bytes11(_t93 / "pinned" / "demo" / "keep.txt") == b"one\ntwo\n",
              f"apply {_ap93.returncode} update {_up93.returncode} " + _up93.stdout[-1500:])
```

It reuses `build_rename_gov` (`selftest.py:12228`), whose scratch directory `rn-link-gov` no other
fixture takes, and `_kit88` (`:13106`). It also reuses `build_target` (`fixture_target.py:60`),
`settle` (`selftest.py:608`), `git` (`:604`) and `read_bytes11` (`:12184`). `os` is imported at
`:24`. The arm is the same on every node: `linked.txt` and `keep.txt` differ by more than case, so the
filesystem's case folding does not choose the branch. A staged copy of the arm compiled under
`python -m py_compile`. The arm sits inside `main()` (`:5402`), so no command runs it outside the
suite, and its red and green ride §7's New arm line.

### S1's probe

`p93_probe.py`, run from the repository root. Its one optional argument is the engine directory,
`tools/govkit` by default. It is the hard-link update of spec 90's `p90_probe.py`, alone, built with
`fixture_target`'s factories:

```python
import os, pathlib, shutil, subprocess, sys, tempfile
eng = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "tools/govkit").resolve()
sys.path.insert(0, str(eng))
from fixture_target import build_scratch_gov, build_target
tmp = pathlib.Path(tempfile.mkdtemp(prefix="p93-"))
def git(cwd, *a):
    return subprocess.run(["git", "-C", str(cwd), "-c", "user.email=t@e", "-c", "user.name=t", *a],
                          capture_output=True, text=True, check=True).stdout
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
(g / "pinned" / "demo" / "keep.txt").write_text("one\ntwo\n", encoding="utf-8", newline="\n")
git(g, "add", "-A"); git(g, "commit", "-qm", "A")
t = build_target(tmp, 'gov_source = "local"\nprefix = "pinned"\nkits = ["demo"]\n')
gk = [sys.executable, str(g / "pinned" / "govkit" / "govkit.py")]
subprocess.run(gk + ["apply", "--target", str(t), "--kits", "demo"], capture_output=True, check=True)
git(t, "add", "-A"); git(t, "commit", "-qm", "install")
os.link(t / "pinned/demo/keep.txt", t / "pinned/demo/linked.txt")
git(t, "add", "-A"); git(t, "commit", "-qm", "own link")
git(g, "mv", "pinned/demo/keep.txt", "pinned/demo/linked.txt")
git(g, "commit", "-qm", "B")
up = subprocess.run(gk + ["update", "--target", str(t), "--write"],
                    capture_output=True, text=True, encoding="utf-8", errors="replace")
kept = (t / "pinned/demo/keep.txt").read_bytes() == b"one" + bytes([10]) + b"two" + bytes([10])
print(f"hard link: update exit {up.returncode} | other name named: {'under another name (a link' in up.stdout}"
      f" | case-only named: {'case-only rename is on a case-insensitive filesystem' in up.stdout} | bytes kept: {kept}")
```

Measured, about 3 s each, with the engine a scratch copy of `tools/govkit` where a row is staged:

| Engine | Line |
|---|---|
| `2e6d48453` | `hard link: update exit 1 \| other name named: True \| case-only named: False \| bytes kept: True` |
| `:11113` staged as `_case = _alias`, rev-1 of spec 90's message and its M5 | `hard link: update exit 1 \| other name named: False \| case-only named: True \| bytes kept: True` |
| the link-or-alias text cut, its `if _alias else` staged as `if False else` | `hard link: update exit 1 \| other name named: False \| case-only named: False \| bytes kept: True` |

The refusal fires and the bytes stay in every row. Only the text differs, which is why the review
grades the item medium.

### S2: the narrowed claim

The ledger's S2 sentence, written without backticks so that AC3 greps one spelling:

```text
set_environ holds the three copies in check_step_isolation and the new check_floor_bash, at
selftest.py:3787, :4422, :4452 and :4462. The GOVKIT_NO_REMOTE_PROBE copy and the GOV_BASH copy in
main() are still typed by hand. This corrects the TOOL-dSafePassage-91 commit message and its
ledger, which say set_environ holds all four environment uses.
```

The builder writes the four use lines as they read after TOOL-dSafePassage-92 lands. 92 adds no
`set_environ` call, so the count stays four. Spec 91's S3 body was already precise. Only the commit
message, spec 91's rev-2 L3 note and its ledger generalised it. Spec 91's AC7 guard, the literal
`os.environ.get(k) for k in`, backs the narrowed claim as written, because the claim names only
the loop.

### Inventory

Minted in `selftest.py`: the check label `[dSP-93]`, the locals `_g93`, `_t93`, `_ap93` and `_up93`,
and the scratch directories `rn-link-gov` and `rn-link-t`. Minted in the tree: this unit's ledger
sentence. No function, `Refusal` site, flag, conf key, gate leg or receipt field.

### Migration

None.

### Rollout

Live at landing, at order 16, after TOOL-dSafePassage-92.

### Files touched (estimate)

- `tools/govkit/selftest.py`

### Alternatives rejected

- **id 4: the finder's fix.** The skeptic rejected it, and the corrected fix is S2.
- **id 4: fold the two copies so the original claim comes true.** The correction marks this optional,
  and §3 says why this unit leaves it.
- **id 2: assert the `ALREADY holds a file there` text is absent too.** The branch order at
  `govkit.py:11114-11127` already excludes it whenever `_alias` holds, so the case-only absence is the
  one that separates the M5 regression.
- **id 2: grade the index as `[dSP-90]` does.** The probe's bytes and exit already show that nothing
  moved, and the review's fix names exit, text and bytes.

## 5. Production-readiness checklist

- security: no write path, spawn or surface. The arm makes a hard link inside its own scratch target.
- perf / scale: one more `apply` and `update` fixture in the selftest, about 3 s by its probe.
- error / empty / loading states: N/A — the arm reads one refusal and adds no state.
- observability: the `[dSP-93]` FAIL carries both exits and the update's stdout tail.
- risks: `os.link` needs a filesystem that makes hard links. NTFS and the runners' filesystems do,
  and spec 90's probe measured it on node a.
- testing: §7's New arm, and AC1 to AC3.
- migration: none.
- user docs: none. No page under `help/` describes the update refusal's link text.

## 6. Acceptance criteria

- **AC1** — When §4 "S1's probe", saved under the temp root as `p93_probe.py`, runs with `python`
  from the repository root, it prints
  `hard link: update exit 1 | other name named: True | case-only named: False | bytes kept: True`.
  This is a preservation check: the line reads the same at `2e6d48453`.
  Red when: `_case` regresses to `_alias` at `tools/govkit/govkit.py:11113`, so it prints
  `other name named: False | case-only named: True`; or the link-or-alias text is cut, so it prints
  `other name named: False | case-only named: False`. Both were staged in a scratch engine (§4).
  cost: about 3 s.
  fixture: a scratch gov and target under the temp root. The tree holds none today.
- **AC2** — When `git grep -n -F "[dSP-93]" -- tools/govkit/selftest.py` runs, it prints one line,
  inside the `DEPL-dCarriedReceipt-11` block, after `[dSP-91 L1]`. And
  `git grep -n -F "os.link(" -- tools/govkit/selftest.py` prints one line, in the same arm.
  Red when: the arm is absent, so both greps print nothing, as at `2e6d48453`.
- **AC3** — When
  `git grep -n -E "three copies in check_step_isolation and the new check_floor_bash" -- memory/builds/dSafePassage/build/`
  runs, it prints one line, in this unit's acceptance ledger.
  Red when: the ledger repeats the four-use claim or carries no correction, so the grep prints
  nothing, as at `2e6d48453`.
  fixture: the ledger the build writes. The tree holds none for this unit today.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the `[dSP-93]` check in the `DEPL-dCarriedReceipt-11` block, staged red by `_case = _alias` at `govkit.py:11113`, which names case folding for the link, and separately by the link-or-alias text cut · none

The four `{prefix}/govkit/` legs and `policy fixtures` are the guard join's for `selftest.py`. Its
other guard, `{prefix}/`, is broad. No refusal call site is added, so `govkit refusal join`'s pin
does not move.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-92-1-spec-writer.md` and
  its brief `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-92-spec-brief.md`.
  It batches the round-4 closing diff review's minors,
  `memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-90-91-closing-diff-round4.md`,
  medium id 2 at the finder's sound fix and low id 4 at the skeptic's corrected fix. Ids 1 and 3 are
  TOOL-dSafePassage-92's. The arm was compiled staged, and its probe and both staged breaks were
  measured in scratch engines from `2e6d48453`.

## 10. Reuse audit

S1 extends the `DEPL-dCarriedReceipt-11` block of `tools/govkit/selftest.py` through that block's
factory, `build_rename_gov` (`selftest.py:12228`), and the kit text `_kit88` that the `[dSP-88]` and
`[dSP-91 L1]` fixtures already share. It copies the hard-link case of spec 90's `p90_probe.py` into
the suite, so the case is not typed a second way. S2 writes no code. Its claim points at
`set_environ` (`selftest.py:288`) and its four calls.
`python tools/codebase-map/reuse_lookup.py "a selftest arm that makes a hard link at a rename destination and expects the refusal to name the link"`
ranked `arm`, `Refusal` and `run_arms`, which are the shell-suite arm helpers and the refusal class.
None of them builds an update fixture, so the block's own factory is the seam. The recall probe
ranked this review's item 2 and TOOL-dSafePassage-59, whose link refusal is a different walk.

Recall terms used: `python tools/memory-recall/query.py "a refusal text the update verb adds for a link at the rename destination is never triggered by a selftest arm" --terms "dSP-90 samefile alias link refusal case-only rename hard link set_environ GOV_BASH hand-typed copy"`
