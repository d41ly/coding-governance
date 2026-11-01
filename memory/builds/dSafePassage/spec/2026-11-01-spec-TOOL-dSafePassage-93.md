# TOOL-dSafePassage-93 — the round-4 closing review's two minors: an arm that triggers the link-or-alias refusal, and the set_environ claim narrowed

**Status:** CLOSED · rev-2 · 2026-11-01 · node a · Tier-2 · base 2e6d4845 · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dSafePassage-1-runlog-0a000b40.md](../build/2026-11-01-build-TOOL-dSafePassage-1-runlog-0a000b40.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-74 TOOL-dSafePassage-75 TOOL-dSafePassage-76 TOOL-dSafePassage-77 TOOL-dSafePassage-78 TOOL-dSafePassage-80 TOOL-dSafePassage-81 TOOL-dSafePassage-82 TOOL-dSafePassage-83 TOOL-dSafePassage-84 TOOL-dSafePassage-86 TOOL-dSafePassage-87 TOOL-dSafePassage-88 TOOL-dSafePassage-89 TOOL-dSafePassage-90 TOOL-dSafePassage-91 TOOL-dSafePassage-92 TOOL-dSafePassage-94 TOOL-dSafePassage-95 TOOL-dSafePassage-96 TOOL-dSafePassage-97 TOOL-dSafePassage-98 TOOL-dSafePassage-99 TOOL-dSafePassage-100 TOOL-dSafePassage-101 TOOL-dSafePassage-102 |
| [2026-11-01-build-TOOL-dSafePassage-93-ledger.md](../build/2026-11-01-build-TOOL-dSafePassage-93-ledger.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-91-close-arms-g-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-91-close-arms-g-brief.md) | research | TOOL-dSafePassage-91 TOOL-dSafePassage-92 TOOL-dSafePassage-94 TOOL-dSafePassage-95 TOOL-dSafePassage-96 |
| [2026-11-01-prompt-TOOL-dSafePassage-92-audit-fold-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-92-audit-fold-brief.md) | research | TOOL-dSafePassage-92 |
| [2026-11-01-prompt-TOOL-dSafePassage-92-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-92-spec-brief.md) | research | TOOL-dSafePassage-92 |
| [2026-11-01-prompt-TOOL-dSafePassage-93-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-93-build-brief.md) | journal | — |
| [2026-11-01-review-TOOL-dSafePassage-92-93-closing-diff-round5.md](../reviews/2026-11-01-review-TOOL-dSafePassage-92-93-closing-diff-round5.md) | diff-review | TOOL-dSafePassage-92 |
| [2026-11-01-review-TOOL-dSafePassage-92-93-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dSafePassage-92-93-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-92 |

<!-- /gen:spec-records -->

## 1. Goal

The round-4 closing diff review confirmed two minors that TOOL-dSafePassage-92 does not take. First,
the refusal text TOOL-dSafePassage-90 added for a link or filesystem alias at gov's new name is
triggered by no gate, medium id 2. Second, the record claims `set_environ` holds every environment
use in `selftest.py`, and two hand-typed copies remain, low id 4. This unit closes both at the fixes
the review's skeptic judged sound. For id 2 that is the finder's fix: a `[dSP-90]` sibling arm on
p90's hard-link case. For id 4 it is the skeptic's corrected fix: the claim narrowed in this unit's
record. BUILD-METHOD M4 batches the minors into one unit. It builds after TOOL-dSafePassage-92,
which edits the same file. Rev-2 folds the round-1 spec audit: the arm reads a would-be write and
the link's identity, runs gov through `run_in_gov`, and reports a failed setup as its own red. The
narrowed claim cites each hold by content and names all three carriers.

## 2. Scope (IN)

- **S1** — id 2, an arm that triggers the link-or-alias text. In the `DEPL-dCarriedReceipt-11` block
  of `tools/govkit/selftest.py`, a `[dSP-93]` check sits after `[dSP-91 L1]` (`:13168`) and before
  the `mvfail` fixture (`:13173`). The fixture is a fresh `build_rename_gov` at `pinned` and its
  installed target, whose `keep.txt` holds `[dSP-88]`'s four lines. In that target, the adopter
  commits a hard link `pinned/demo/linked.txt` to `pinned/demo/keep.txt`. Gov then renames
  `keep.txt` to `linked.txt` and changes its last line, and `update --write` runs. The check asserts
  exit 1, `under another name (a link` in stdout, `case-only rename is on a case-insensitive
  filesystem` absent from stdout, both names still holding the adopter's four lines, and
  `os.path.samefile` still true of the two. Both `govkit.py` runs go through `run_in_gov`
  (`:8441`), which gains a keyword `root` defaulting to `PFX`. A failed `os.link` or a failed apply
  is reported in the check's detail as a `FAIL [dSP-93]`, and the update runs only after both
  succeed. §4 "S1". Observed by AC1, AC2 and AC4.
- **S2** — id 4, the claim narrowed. This unit's acceptance ledger states that `set_environ` holds
  the three copies in `check_step_isolation` and the new `check_floor_bash`. It names each hold by its
  check label, never by line: the `[dSP-45]` parent hold and the `[dSP-75]` fakes hold in
  `check_step_isolation`, and the `[dSP-87 AC5]` and `[dSP-91 L2]` holds in `check_floor_bash`. At
  `f9b39338f` they sit at `selftest.py:3787`, `:4422`, `:4452` and `:4462`, and TOOL-dSafePassage-92
  moves the last. It states that the `GOVKIT_NO_REMOTE_PROBE` copy (`:6358-6366`) and the `GOV_BASH`
  copy (`:18418-18432`) in `main()` are still typed by hand. And it names the three carriers it
  corrects: the TOOL-dSafePassage-91 commit message (`2e6d48453`), spec 91's rev-2 L3 note
  (`memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-91.md:591-592`) and that unit's
  ledger (`memory/builds/dSafePassage/build/2026-10-29-build-TOOL-dSafePassage-91-ledger.md:10-11`).
  Each says `set_environ` holds all four environment uses. None is edited. §4 "S2". Observed by AC3.

## 3. Non-goals (OUT)

- Ids 1 and 3 of the review. TOOL-dSafePassage-92 closes both with one predicate.
- Moving `:6358` and `:18418` onto `set_environ`. The skeptic's correction marks this optional. The
  review blames nothing in this range on those two copies, which sit at the base, and the brief keeps
  this unit to a test-arm correction. A follow-up can take it, with the `_BASH` restore at `:18418`
  kept beside it, as the correction says.
- A pattern guard over the tree for hand-typed environment restores. The correction marks it optional,
  and a guard would need an allow-list for the deliberate suite-wide sets at `:5407` and `:6373`.
- Editing spec 91 or its ledger. Spec 91 is CLOSED, and a commit message cannot be edited.
- Moving the `[dSP-88]`, `[dSP-90]` and `[dSP-91 L1]` invocations onto `run_in_gov`. The audit's L5
  fix leaves them to a follow-up, and the `root` keyword is what such a follow-up needs.
- A symlink in place of the hard link. NTFS makes a hard link without a privilege, and `samefile`
  answers both alike (spec 90 §4 "The probe").
- The checklist entries the review's left-shift notes name, and the round-1 spec audit's. Both
  records note that no checklist is present, so the main loop owns those entries, and S1's arm is id
  2's gate.

### Edges

- **consumes-from** `TOOL-dSafePassage-92` — that unit takes ids 1 and 3, which this unit's scope
  leaves out, and it rewrites `check_floor_bash`, which S2's narrowed claim names. Both units edit
  `selftest.py`, and this one builds second, so every line it cites is re-read after 92 lands.

## 4. Design

Every cited line holds at `2e6d48453`, the build head with TOOL-dSafePassage-90 and -91 landed. At
rev-2 every cited line was re-read at `f9b39338f`, where `tools/` is unchanged from `2e6d48453`.
TOOL-dSafePassage-92 adds lines inside `check_floor_bash` (`selftest.py:4430`) before this unit
builds. So every line after `:4467` moves, and the builder finds each anchor by its content. Each
measurement was taken on 2026-11-01 on node a, where `core.ignorecase` reads `true`.

### S1: the hard-link arm

The refusal at `tools/govkit/govkit.py:11111-11128` picks its text from `_alias`, which is
`samefile` (`:11112`), and `_case`, which is `_alias` plus a case-folded match (`:11113`). A hard link
at a name that differs by more than case is `_alias` and not `_case`, so it reads the "under another
name (a link or a filesystem alias)" text (`:11120-11124`). `[dSP-90]` (`selftest.py:13142-13147`)
runs only a case-only rename, so nothing in the bar reaches that branch.

`run_in_gov` (`selftest.py:8441-8443`) gains a keyword parameter, and no current caller moves:

```python
        def run_in_gov(g: pathlib.Path, *args: str, root: str = PFX) -> subprocess.CompletedProcess:
            return subprocess.run([sys.executable, str(g / root / KIT_NAMES["govkit"] / "govkit.py"), *args],
                                  capture_output=True, text=True, encoding="utf-8", errors="replace")
```

The arm, between the `[dSP-91 L1]` check and `_g11c = build_rename_gov("mvfail")`:

```python
        # TOOL-dSafePassage-93: the adopter's own hard link at gov's new name. The new name is the row's
        # own file under another name, never a second spelling, so the move is refused naming the link.
        # Gov's B changes the last line, so a write through either name moves bytes the check reads, and
        # the two names must still be one file. A hard link stands in for a symlink: NTFS makes one
        # without a privilege, and `samefile` answers both alike.
        _g93 = build_rename_gov("link", _kit88, "pinned", {"keep.txt": "one\ntwo\nthree\nfour\n"})
        _t93 = build_target(tmp, 'gov_source = "local"\nprefix = "pinned"\nkits = ["demo"]\n', "rn-link-t")
        _ap93 = run_in_gov(_g93, "apply", "--target", str(_t93), "--kits", "demo", root="pinned")
        _keep93, _link93 = (_t93 / "pinned" / "demo" / n for n in ("keep.txt", "linked.txt"))
        try:
            os.link(_keep93, _link93)
            _ln93 = ""
        except OSError as _e93:
            _ln93 = f"os.link failed: {_e93}; "
        settle(_t93, "the install and the adopter's own link")
        git(_g93, "mv", "pinned/demo/keep.txt", "pinned/demo/linked.txt")
        (_g93 / "pinned" / "demo" / "linked.txt").write_text("one\ntwo\nthree\nFOUR\n", encoding="utf-8", newline="\n")
        git(_g93, "add", "-A")
        git(_g93, "commit", "-qm", "B")
        _up93 = (run_in_gov(_g93, "update", "--target", str(_t93), "--write", root="pinned")
                 if _ap93.returncode == 0 and not _ln93 else None)
        check("[dSP-93] a rename onto the adopter's own link to the row's file is refused naming the link, not case folding",
              _up93 is not None and _up93.returncode == 1 and "under another name (a link" in _up93.stdout
              and "case-only rename is on a case-insensitive filesystem" not in _up93.stdout
              and all(read_bytes11(f) == b"one\ntwo\nthree\nfour\n" for f in (_keep93, _link93))
              and os.path.samefile(_keep93, _link93),
              f"{_ln93}apply {_ap93.returncode} update {_up93 and _up93.returncode} "
              + (_up93 or _ap93).stdout[-1500:])
```

It reuses `build_rename_gov` (`selftest.py:12228`), whose scratch directory `rn-link-gov` no other
fixture takes, and `_kit88` (`:13106`). It also reuses `run_in_gov` (`:8441`), which is in scope
because it and the rename block both sit in `main()`'s `with tempfile.TemporaryDirectory()` block
(`:5416`). It reuses `build_target` (`fixture_target.py:60`), `settle` (`selftest.py:608`), `git`
(`:604`) and `read_bytes11` (`:12184`) too. `os` is imported at `:24`. The arm is the same on every
node: `linked.txt` and `keep.txt` differ by more than case, so the filesystem's case folding does not
choose the branch. The arm sits inside `main()` (`:5402`), so no command runs it outside the suite,
and its red and green ride §7's New arm line and AC4.

The four lines and the changed last line are the audit's M4 fix, at the skeptic's corrected form.
Three of four lines survive, so `git diff --find-renames=50%` (`govkit.py:8915`, `:8938`) still
reports the move as a rename, and the refusal at `:11111` runs before any byte is chosen (`:11131`).
A write of gov's bytes through either name now changes what `read_bytes11` reads, and a replace that
breaks the link turns `samefile` false. `samefile` runs last, after both byte terms have found both
files. The `try` around `os.link` is the audit's L8 fix. The selftest's `git` helper is
`check=False` (`:604-605`), so `os.link` is the arm's one call that can raise. It reports into the
detail, as `read_bytes11` does for a missing file (`:12183-12186`).

### S1's probe

`p93_probe.py`, run from the repository root. Its one optional argument is the engine directory,
`tools/govkit` by default. It is the hard-link update of spec 90's `p90_probe.py`, alone, built with
`fixture_target`'s factories. At rev-2 it carries the arm's four lines, its changed last line and
its link term:

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
(g / "pinned" / "demo" / "keep.txt").write_text("one\ntwo\nthree\nfour\n", encoding="utf-8", newline="\n")
git(g, "add", "-A"); git(g, "commit", "-qm", "A")
t = build_target(tmp, 'gov_source = "local"\nprefix = "pinned"\nkits = ["demo"]\n')
gk = [sys.executable, str(g / "pinned" / "govkit" / "govkit.py")]
subprocess.run(gk + ["apply", "--target", str(t), "--kits", "demo"], capture_output=True, check=True)
git(t, "add", "-A"); git(t, "commit", "-qm", "install")
keep, linked = t / "pinned/demo/keep.txt", t / "pinned/demo/linked.txt"
os.link(keep, linked)
git(t, "add", "-A"); git(t, "commit", "-qm", "own link")
git(g, "mv", "pinned/demo/keep.txt", "pinned/demo/linked.txt")
(g / "pinned/demo/linked.txt").write_text("one\ntwo\nthree\nFOUR\n", encoding="utf-8", newline="\n")
git(g, "add", "-A"); git(g, "commit", "-qm", "B")
up = subprocess.run(gk + ["update", "--target", str(t), "--write"],
                    capture_output=True, text=True, encoding="utf-8", errors="replace")
four = b"one" + bytes([10]) + b"two" + bytes([10]) + b"three" + bytes([10]) + b"four" + bytes([10])
kept = all(p.is_file() and p.read_bytes() == four for p in (keep, linked))
link = keep.is_file() and linked.is_file() and os.path.samefile(keep, linked)
print(f"hard link: update exit {up.returncode} | other name named: {'under another name (a link' in up.stdout}"
      f" | case-only named: {'case-only rename is on a case-insensitive filesystem' in up.stdout}"
      f" | bytes kept: {kept} | link kept: {link}")
```

Measured at rev-2, 3 to 10 s each, with the engine a scratch copy of `tools/govkit` where a row is
staged:

| Engine | Line |
|---|---|
| `f9b39338f` | `hard link: update exit 1 \| other name named: True \| case-only named: False \| bytes kept: True \| link kept: True` |
| `:11113` staged as `_case = _alias`, rev-1 of spec 90's message and its M5 | `hard link: update exit 1 \| other name named: False \| case-only named: True \| bytes kept: True \| link kept: True` |
| the link-or-alias text cut, its `if _alias else` staged as `if False else` | `hard link: update exit 1 \| other name named: False \| case-only named: False \| bytes kept: True \| link kept: True` |
| the refusal's `continue` (`:11129`) cut, so the row goes on to its move | the `f9b39338f` line |

The refusal fires and the bytes stay in every row. Only the text differs, which is why the review
grades the item medium. The last row shows what the byte and link terms cannot be seen red by. With
the refusal's `continue` cut, the move's own `git mv` refuses with `fatal: destination exists`, and
the kit is held back with nothing written. No one-line break reaches a write through the link, so
those two terms guard a write that two refusals already stop. They were not seen red.

### S2: the narrowed claim

The ledger's S2 sentence, written without backticks so that AC3 greps one spelling. The builder
keeps each phrase AC3 greps on one line:

```text
set_environ holds the three copies in check_step_isolation and the new check_floor_bash:
the [dSP-45] parent hold and the [dSP-75] fakes hold in check_step_isolation, and the
[dSP-87 AC5] and [dSP-91 L2] holds in check_floor_bash. The GOVKIT_NO_REMOTE_PROBE copy and the
GOV_BASH copy in main() are still typed by hand. This corrects the TOOL-dSafePassage-91 commit
message, spec 91's rev-2 L3 note and its ledger, each of which says set_environ holds all four
environment uses.
```

The sentence cites each hold by its check label and no line, the audit's L3 fix, because
TOOL-dSafePassage-92 moves the `[dSP-91 L2]` hold. 92 adds no `set_environ` call, so the count
stays four. Spec 91's S3 body was already precise. Only the commit message, spec 91's rev-2 L3 note
(`2026-10-29-spec-TOOL-dSafePassage-91.md:591-592`) and its ledger generalised it, and the sentence
names all three, the audit's L6 fix. Spec 91's AC7 guard, the literal
`os.environ.get(k) for k in`, backs the narrowed claim as written, because the claim names only
the loop.

### Inventory

Minted in `selftest.py`: the check label `[dSP-93]`, the `root` keyword of `run_in_gov`, the
locals `_g93`, `_t93`, `_ap93`, `_keep93`, `_link93`, `_ln93`, `_up93`, `_e93`, `n` and `f`, and the
scratch directories `rn-link-gov` and `rn-link-t`. Minted in the tree: this unit's ledger sentence.
No function, `Refusal` site, flag, conf key, gate leg or receipt field.

### Migration

None.

### Rollout

Live at landing, at order 16, after TOOL-dSafePassage-92.

### Files touched (estimate)

- `tools/govkit/selftest.py`
- `memory/builds/dSafePassage/build/2026-11-01-build-TOOL-dSafePassage-93-ledger.md` — the
  acceptance ledger, which carries S2's sentence and which AC3 greps

### Alternatives rejected

- **id 14: the finder's fix.** The skeptic judged it unsound, and S1's four lines with a changed last
  line are the corrected fix.
- **id 10: AC3 also matches `with set_environ(` line numbers against the ledger.** Citing by content
  leaves no number to go stale, and the audit judged both forms sound.
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
- perf / scale: one more `apply` and `update` fixture in the selftest, 3 to 10 s by its probe on
  node a, measured at rev-2.
- error / empty / loading states: N/A — the arm reads one refusal and adds no state.
- observability: the `[dSP-93]` FAIL carries both exits and the update's stdout tail.
- risks: `os.link` needs a filesystem that makes hard links. NTFS and the runners' filesystems do,
  and spec 90's probe measured it on node a. Where it cannot, or the apply fails, the arm reports
  `FAIL [dSP-93]` with the cause in its detail and runs no update. The byte and link terms were not
  seen red, because no one-line break gets past both the refusal and `git mv` (§4 "S1's probe").
- testing: §7's New arm, and AC1 to AC3.
- migration: none.
- user docs: none. No page under `help/` describes the update refusal's link text.

## 6. Acceptance criteria

- **AC1** — When §4 "S1's probe", saved under the temp root as `p93_probe.py`, runs with `python`
  from the repository root, it prints
  `hard link: update exit 1 | other name named: True | case-only named: False | bytes kept: True | link kept: True`.
  This is a preservation check: the line reads the same at `f9b39338f`.
  Red when: `_case` regresses to `_alias` at `tools/govkit/govkit.py:11113`, so it prints
  `other name named: False | case-only named: True`; or the link-or-alias text is cut, so it prints
  `other name named: False | case-only named: False`. Both were staged in a scratch engine (§4).
  cost: 3 to 10 s, measured at rev-2.
  fixture: a scratch gov and target under the temp root. The tree holds none today.
- **AC2** — When `git grep -n -F "[dSP-93]" -- tools/govkit/selftest.py` runs, it prints one line,
  inside the `DEPL-dCarriedReceipt-11` block, after `[dSP-91 L1]`. And
  `git grep -n -F "os.link(" -- tools/govkit/selftest.py` prints one line, in the same arm.
  Red when: the arm is absent, so both greps print nothing, as at `2e6d48453`.
- **AC3** — When
  `git grep -n -E "three copies in check_step_isolation and the new check_floor_bash" -- memory/builds/dSafePassage/build/`
  runs, it prints one line, in this unit's acceptance ledger. And
  `git grep -n -F "rev-2 L3 note" -- memory/builds/dSafePassage/build/` prints one line, in the same
  ledger.
  Red when: the ledger repeats the four-use claim or carries no correction, so the first grep prints
  nothing, as at `f9b39338f`. Or the correction omits spec 91's note, so the second prints nothing,
  as at `f9b39338f`.
  fixture: the ledger the build writes. The tree holds none for this unit today.
- **AC4** — When §7's New arm is observed at the close with `_case = _alias` staged at
  `tools/govkit/govkit.py:11113` in a scratch tree, the `[dSP-93]` check reads `FAIL`. With the line
  restored it reads `ok`, and the unit's ledger records both lines.
  Red when: the staged break leaves `[dSP-93]` reading `ok`, so the arm's text terms miss the
  regression AC1's probe shows, or the restored tree reads `FAIL`.
  permission: the arm sits inside `main()`, so only the suite reaches it. BUILD-METHOD gives that
  observation to the main loop at the close (`memory/guides/BUILD-METHOD.md:280-281`), not to a
  build pass.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `policy fixtures` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC4 · the `[dSP-93]` check in the `DEPL-dCarriedReceipt-11` block, staged red by `_case = _alias` at `govkit.py:11113`, which names case folding for the link, and separately by the link-or-alias text cut · none

The four `{prefix}/govkit/` legs and `policy fixtures` are the guard join's for `selftest.py`. Its
other guard, `{prefix}/`, is broad. `recall floor` and `recall floor arms` are the `memory/`
guard's, which the ledger trips (`tools/gate-legs.json:887-895`). No refusal call site is added, so `govkit refusal join`'s pin
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
- rev-2 · 2026-11-01 · §1 S1 S2 §3 §4 §5 AC1 AC3 AC4 §7 §10 · folded the round-1 spec audit,
  `memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-92-93-spec-audit-round1.md`,
  under its brief `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-92-audit-fold-brief.md`.
  M4 (id 14): the four lines and a changed last line, both names' bytes and `samefile`, at the
  skeptic's corrected fix. L3 (ids 4, 10): the ledger sentence cites each hold by content. L4 (id
  5): AC4 names the staged red, and the arm covers AC1 and AC4. L5 (id 8): the arm runs gov through
  `run_in_gov` and its new `root` keyword. L6 (id 9): the sentence names spec 91's rev-2 L3 note,
  and AC3 greps for it. L7 (id 11): the ledger is in Files touched and `recall floor` is in §7. L8
  (id 15): `os.link` is guarded and the update is gated on it and on the apply. The probe and three
  staged engines were measured at `f9b39338f`, and a fourth row records the break the new terms
  could not be seen red by.

## 10. Reuse audit

S1 extends the `DEPL-dCarriedReceipt-11` block of `tools/govkit/selftest.py` through that block's
factory, `build_rename_gov` (`selftest.py:12228`), and the kit text `_kit88` that the `[dSP-88]` and
`[dSP-91 L1]` fixtures already share. It runs gov through `run_in_gov` (`selftest.py:8441`), the
suite's one helper for a `govkit.py` invocation, extended by a keyword so that no copy is typed. It copies the hard-link case of spec 90's `p90_probe.py` into
the suite, so the case is not typed a second way. S2 writes no code. Its claim points at
`set_environ` (`selftest.py:288`) and its four calls.
`python tools/codebase-map/reuse_lookup.py "a selftest arm that makes a hard link at a rename destination and expects the refusal to name the link"`
ranked `arm`, `Refusal` and `run_arms`, which are the shell-suite arm helpers and the refusal class.
None of them builds an update fixture, so the block's own factory is the seam. The recall probe
ranked this review's item 2 and TOOL-dSafePassage-59, whose link refusal is a different walk.

Recall terms used: `python tools/memory-recall/query.py "a refusal text the update verb adds for a link at the rename destination is never triggered by a selftest arm" --terms "dSP-90 samefile alias link refusal case-only rename hard link set_environ GOV_BASH hand-typed copy"`
