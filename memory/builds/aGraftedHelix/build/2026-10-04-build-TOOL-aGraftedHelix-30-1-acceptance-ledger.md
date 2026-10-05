# Acceptance ledger — TOOL-aGraftedHelix-30

**Serves:** journal TOOL-aGraftedHelix-30

Node `a`, 2026-10-05. The build commit is `99b5dac2`, over the pass's parent `65b45487`; the spec
stayed at rev-1, because nothing built diverged from it. No merge bar and no self-test suite ran in
this pass. The driver suite's four new arms ran as a slice: the suite's prologue, its `scope` helper
and the borrowed-record block, generated into the session scratchpad with the kit dir pinned, its
fixture repositories under a short `%TEMP%` root. Every staged break was a scratch copy of the driver
beside a copy of its library, never an edit in the kit. The whole suite, and check 26 inside the
unattended kit gate, are the main loop's, at VERIFYING.

**Evidences:** TOOL-aGraftedHelix-30
- AC1 — `run --authorization tBr2` — the slice at `99b5dac2` printed `PASS (48 assertions)`: the call printed `unattended: authorization-reachable — met · base <the pushed tip> · anchor refs/heads/main at <sha>` and exited 0, and the three reads, `git status --porcelain`, `git hash-object` of the record and `git ls-remote origin`, were equal before and after; on `tAbsent` it printed check 10's refusal and exited 1.
- AC1 — `git hash-object` — a scratch driver whose met branch writes a fact with the driver's own `set_fact` redded `GH30 AC1 a met record moved nothing` alone; every other assertion in the slice held.
- AC2 — `run --authorization tBr` — the same slice: check 89's line holding `mode prompt; delete the line`, then exactly one line holding both `--abort tBr --code repo-state-out-of-mandate` and `--handoff tBr --code owner-decision`, no `owner-landing`, exit 1, and the three reads unchanged.
- AC2 — `run --authorization tBr` — against the parent's driver from `65b45487`, every call printed `UNATTENDED check 14 FAILED — unknown argument` and 17 of the 23 new assertions failed; the six that held are the ones a refusal that writes nothing and exits 1 also satisfies: the two moved-nothing reads, the two exit-1 reads, the `owner-landing` miss and the zero-count source read.
- AC3 — `run --close tBr` — the check 89 line the close printed and the one `run --authorization tBr` printed were byte-identical in the slice.
- AC3 — `print_authorization` — its body, cut at the next column-0 brace with comment lines dropped, holds one `dod_met "$slug" "$rel" authorization-reachable` call and no `check_authorization` or `trusted_base`; a scratch driver with that call replaced by the inlined chain redded both source assertions and nothing else.
- AC4 — `not evaluated` — with origin's URL at a path that does not exist, `run --authorization tBr2` printed check 27, then the not-evaluated line, no `--handoff`, exit 2; with the URL restored and `unit` deleted from origin, check 32, the same line, no exits, exit 2; pushed again at its old tip, met with exit 0. A scratch driver without the not-evaluated branch redded the four not-evaluated assertions and nothing else.
- AC5 — `grep -nF -e '--authorization'` — over the three files it printed the `VERBS_SLUG` line, the header line opening `#   unattended.sh --authorization`, the dispatch arm `--authorization) print_authorization "$SLUG" ;;`, the verbs entry at line 179 opening with the verb in code quotes and an em dash, and two Skill lines invoking `unattended.sh --authorization <slug>`; the suite calls `run --authorization` on non-comment lines. Check 26 itself runs in the `unattended kit gate` at VERIFYING.
- AC6 — `.claude/skills/unattended/SKILL.md` — `grep -n` printed lines 1003, 1004 and 1005: `--prepare --slug <slug>`, then `--authorization <slug>`, then `--close <slug>`; the reconcile paragraph opening at line 1196 names `git merge` and line 1201 of the same paragraph names `--authorization`. `bash tools/unattended/adopt-unattended.sh --check` printed `in sync` and exited 0.
- AC7 — `memory/guides/UNATTENDED-VERBS.md` — `diff` against `tools/unattended/VERBS.template.md`, carriage returns stripped, printed nothing; from `65b45487` the verbs template adds the one entry and moves line 1, and the protocol and stops templates each show one hunk, `@@ -1 +1 @@`.
- AC8 — `bash tools/check-kit-versions.sh` — at `99b5dac2` printed `kit-versions: clean — 16 declared carrier(s) under tools/`, and `python tools/govkit/govkit.py epoch --base 65b454876` printed `epoch: unattended · clean · 1.77`.
- AC9 — `python tools/memory-tree/gotchas.py --for-paths tools/unattended/unattended.sh` — its checklist carried `- [ ] a-merged-in-check-can-refuse-a-pinned-record`; `python tools/memory-tree/gotchas.py --check` exited 0, `--declares` printed `declares: yes`, and the index row counts 4 anchors.
- AC9 — `python tools/memory-tree/row_grammar.py --check-relations <the pass's parent sha>` — with `HEAD` before the commit it graded 1 added record against 370 at base: 1 near match, 1 satisfied, exit 0; the hit is `TOOL-aEvidencedLens-22`, which the record names. `python tools/codebase-map/test_codebase_map.py` printed only `ok` lines after `gen_map.py --write`.
- AC10 — `bash tools/unattended/unattended.sh --authorization aGraftedHelix` — in this worktree at `99b5dac2` it printed `unattended: authorization-reachable — met · base 65b4548763c1… · anchor refs/heads/main at 290d0d2d5ae8…` and exited 0, and `git status --porcelain` read empty before and after.
