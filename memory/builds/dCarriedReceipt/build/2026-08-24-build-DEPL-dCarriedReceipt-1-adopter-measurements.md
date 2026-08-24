# DEPL-dCarriedReceipt-1 dossier — what the adopters measured in this tree, and what it buys

**Serves:** research DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-12

Carried in from `d41ly/incms` on 2026-08-24, the way `aFerriedDossier` carried its predecessor. That
dossier filed the asks; this one supplies the numbers they lacked and adds two defects it could not
have seen, because both only appear on a **second** run.

Everything below was measured against this repo at `9ddcc5c9` against the adopters' pin `ce5dca99`.

## 1. The state that motivates the build

`cmd_update` refuses without `<target>/.governance/install.json` (`:2932`), and `cmd_check` refuses
the same way. **Neither live adopter has one.** NicoCares has `deploy.toml` only; inCMS has neither
and hand-rolled `.governance/kits.json` + `install.index` + `scripts/check_kit_sync.py` instead.

So the update engine this repo built has, to date, **run against zero real adopters** and moved zero
rows. Everything in `VERDICT_GRID`, `three_way` and the write loop is unexercised outside fixtures.

## 2. Two defects the dossier could not see

Both verified in source here, both on the second run rather than the first.

**A merge result is stamped as gov's own.** On `diverged`, `:3096` sets `row["sha256"] =
_sha(merged)`. `classify_row` compares the target's bytes to that field (`:2886`), so on the next
gov commit touching the file the row reads `("equal","differs")` → `stale` (`:2845`) → raw overwrite
(`:3071`). **Every hand-edit the three-way preserves is destroyed one update later, reported as a
clean write with zero conflicts.** The code contradicts its own docstring here: `:2878` says the
receipt's hash is what gov actually wrote, and `:3096` writes what the merge produced. → `-8`.

**The in-progress guard cannot fire in a linked worktree.** `:2334` stats
`target/.git/MERGE_HEAD` as a path; in a linked worktree `.git` is an 80-byte file, so the marker is
at `<primary>/.git/worktrees/<name>/MERGE_HEAD` and the probe misses it. The guard also sits inside
`if pins:`, so a target declaring no `lf_pin` is unguarded even where the path form works. And
`cmd_update` has no guard of any kind. `--git-path` is already used correctly at `:2019`. → `-12`.

Both matter because adopters are told to work in linked worktrees, and because NicoCares is a
submodule — a bad write there dirties the parent's submodule pointer.

## 3. A third defect, self-documenting

`{relpath}` has two resolutions. `rule_relpath` (`:172`) resolves it against the rule's base and its
docstring names the basename form **a measured defect**, citing push-main's hook rule. `resolve_dests`
(`:2085`) — the seam `plan`, the write loop and the wildcard exclusion all call — *is* that basename
form. Its own docstring opens by claiming to be "ONE spelling". Today `apply` would write this repo's
`pre-push` hook to the target **root**. → `-1`.

## 4. Why a receipt alone is not enough — the repath measurement

`apply` writes gov bytes **verbatim**: `blob_at` → `write_bytes` (`:2453`, `:2469`).
`resolve_tokens` reaches destinations, argv, lf-pin patterns and gate legs — **never file bodies**.

**59 files under `tools/` contain a literal `tools/<kit>/` path inside them.** An adopter at any
other prefix must hand-edit them, which is exactly what manufactured inCMS's divergence and what
would re-manufacture it after every sync.

Measured on inCMS: of 19 `engine` rows matching no gov commit in that path's history, **9 are pure
mechanical repath** with zero behavioural residual, and only 4 are genuinely undeclared local
content. Nine rows of false divergence, produced by this repo's own shipped bytes. → `-9` carries
them; `-15` stops producing them.

## 5. What the build buys, per target

**Before: zero rows auto-syncable in either repo.**

- **NicoCares** — 143 planned writes, 136 engine. **120 of 136 auto-syncable (88%)**: 87 already
  current, **33 move on the first `update --write`**. Coverage gap **zero** — it took every file
  this repo ships for its 15 kits.
- **inCMS** — 92 declared rows, **48 auto-syncable**: 42 already current, 6 move on the first write.
  Two independent attribution passes with different scripts both landed on 48. Coverage separately
  reports **55 planned destinations it does not hold**, of which 2 are the `-1` resolver bug, 11 are
  declarable renames or consumes, 1 is a landed merged-role snippet, and **41 are genuinely absent**.

NicoCares' zero gap is the calibration: partial adoption is a hand-forking symptom, not a govkit gap.
The honest headline is that this build mostly rescues the repo that was installed correctly.

## 6. Two things this repo should know regardless of the build

**A shipped kit can be silenced by a file the adopter commits.** `tools/unattended/check-unattended.sh`
at the adopters' pin sources the tracked `.unattended.conf` in the main shell, after `status` and
`fail()` are defined; appending `fail() { :; }` takes the leg green with no output. This repo
**already fixed it** at `HEAD` and ships the regression arm at `check-unattended.test.sh:242`. Both
adopters still carry the vulnerable copy, which is a direct argument for the whole build: the fix
exists and cannot reach them.

**A kit can move without its version.** `KIT_UNATTENDED_VERSION` reads `1.8` at both `ce5dca99` and
`9ddcc5c9`, while 12 files under `tools/unattended/` changed across 1,131 lines. Any adopter-side
check comparing constants reports that kit in sync. `check-kit-versions.sh` is the Phase-0
version-detectability contract, and this is the case it cannot see — worth a `DEPL` row of its own if
the owner agrees it is in scope.

## 7. Provenance, stated because it cuts both ways

For three shipped files this repo is the **derivative**, not the origin —
`tools/memory-recall/extract.py`, `query.py` and `recall-opened.js` each carry a `FORKED from inCMS`
header. An automatic update on the adopter's `scripts/recall/extract.py` would replace the adopter's
own upstream with this repo's fork of it, and that file imports `recall_conf`, which the adopter's
recall directory does not have. → `-10` makes those rows report-only in both directions.

## Method note

The adopter-side audit these numbers come from carries its own instrument defect on the record: its
first pass computed "behind" from the two gov blob OIDs and ignored the installed bytes measured one
statement later, over-reporting by three rows. The numbers here are the corrected ones, after five
default-refute skeptics and a synthesis pass (5 of 5 returned) re-derived them.
