# Acceptance ledger — TOOL-aGraftedHelix-27

**Serves:** journal TOOL-aGraftedHelix-27

Node `a`, 2026-10-05, git 2.54.0.windows.1. The build commit is `49621b14`, over the spec's rev-1
commit `72b04279`, the pass's parent; the spec needed no revision. No merge bar and no self-test
suite ran in this pass. The three new arms were observed by a slice under `tools/unattended/` of the
suite's prologue, `build_check_commit_fixture` and the new block, deleted after each run, with its
fixtures under `mktemp -d`. Green against the kit it executed 33 assertions against the prologue's
own 20. It was observed RED three ways: with the lib and the driver at the parent staged in place,
with a lib whose kit-dir derivation asked git again, and with a lib missing the announcement line.
This host made no symlink, so the linked-kit arm ran through a directory junction. The whole suite
is the main loop's at VERIFYING, and the slice count is the evidence for its floors, raised by 13.

**Evidences:** TOOL-aGraftedHelix-27
- AC1 — `commit-msg` — in the slice, a real `git commit` in the fixture's linked worktree ran a
  `commit-msg` hook that recorded `GIT_DIR` as set and ran `--check-commit "$1"`; the commit landed
  with exit 0, and `git show --name-only` of it listed `tools/hkgen/gen.sh` and `memory/HKGEN.md`
  under `Pass: ARCH-tRun-2`. A second commit staging `tools/stray.sh` under `Pass: ARCH-tRun-1` was
  refused, its remedy naming `bash tools/unattended/unattended.sh --dispatch tRun` for
  `ARCH-tRun-1`, repository-relative. With the parent's lib and driver staged, the first commit
  exited 1 printing `UNATTENDED check 49 FAILED` naming `memory/HKGEN.md` as outside the declared
  set, and the remedy read `bash /c/projects/coding-governance/...`, absolute.
- AC2 — `resolve_generated_indexes` — a scratch repository holding the library at `kits/unattended`
  beside `kits/onegen/kit.toml`: called in its linked worktree the resolver printed
  `memory/ONE.md:kits/onegen/g.sh`, and the same call with `GIT_DIR` exported to the worktree's
  absolute git dir printed the same bytes. Through a junction at `other/unattended` in a second
  repository it printed `memory/TWO.md:other/twogen/g2.sh`. With the git probe restored in a staged
  lib, the exported call and the linked call both printed nothing.
- AC3 — `resolve_generated_indexes` — from a library copy under a `mktemp -d` directory no `.git`
  sits above, the resolver exited 0, printed `a/X.md:a/g.sh` on stdout, and printed one stderr line,
  naming the copy's directory under `/tmp` and saying only the repository-root kits and the conf
  pairs were read. With that line deleted from a staged lib, the arm's two stderr assertions redded.
- AC4 — `verb_dispatch` — `git diff 72b042795 49621b14b -- tools/unattended/unattended.sh` printed
  two hunks, `@@ -48,7 +48,7 @@` for the version line and `@@ -10232,9 +10232,11 @@` inside
  `check_commit_message`, against `verb_dispatch` opening at line 10283; no changed line mentions
  `GENERATED_INDEXES`.
- AC5 — `derive_self_rel` — `diff` of the block cut between the `# >>>` and `# <<<` marker lines of
  `tools/lib/kit-rel.sh` and of `tools/unattended/lib-unattended.sh` printed nothing, over 12 lines
  each, and `git grep -l '^# >>> derive_self_rel'` listed the library.
- AC6 — `_top` — the spec's predicate over `tools/unattended/`, excluding the self-tests, printed four
  lines at the build commit: the comment in `tools/unattended/adopt-unattended.sh`, the `_top` probe
  in `tools/unattended/resume-tick.sh`, and the `ROOT` and `KIT_REL` probes in
  `tools/unattended/run-unattended-gates.sh`; none from the library or the driver.
- AC7 — `memory/gotchas/INDEX.md` — `gotchas.py --for-paths` over the library listed
  `inherited-git-dir-pins-the-work-tree-to-the-cwd` among nine anchored classes; `python tools/memory-tree/gotchas.py --check` exited 0;
  `--declares` over the record printed `declares: yes`;
  `test_codebase_map.py` printed six `ok` lines and nothing else.
- AC8 — `bash tools/check-kit-versions.sh` — at the build commit it printed
  `kit-versions: clean`, over 16 declared carriers, and `python tools/govkit/govkit.py epoch --base 72b042795`
  printed `epoch: unattended · clean · 1.67`. `git diff -U0` of the protocol, verbs and stops
  templates printed one `@@ -1 +1 @@` hunk each, the version marker.
- AC9 — `memory/gotchas/INDEX.md` — `git show --name-only --format= 49621b14b` listed
  `memory/gotchas/INDEX.md`, `memory/map/generated/MAP.md` and
  `memory/map/generated/inventories.json` beside the declared paths; the commit went through this
  worktree's own hooks with no `--no-verify`, its message carries `Pass: TOOL-aGraftedHelix-27`, and
  the unit's dispatch row in `memory/builds/aGraftedHelix/RUN.md` names none of the generated outputs.

The suite-only observations, left to the main loop's run at VERIFYING: the three arms inside the
whole driver suite, its two floors, the existing check 49 arms that AC4 leaves unmoved, and the
python-resolver leg's parity row over the library's new copy.
