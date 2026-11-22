# TOOL-dQuietDisk-13 deviation 1 — the widened rows carry their measured counts, a call onto a repository costs what today's commit costs, and the key is derived before the build

**Serves:** deviation TOOL-dQuietDisk-13

- **Departs from:** `TOOL-dQuietDisk-13@rev-4` [S7, AC1, the call half]
- **Hand-off:** spec-to-code
- **Before:**
  - S7 has the three rows widened through the ledger's door and never hand-edited.
  - AC1 has each `mk_repo` call onto a repository add 4 trace files.
  - The call half passes `$(derive_template_key …)` straight into `resolve_template`'s argument list.
  - The prologue names `$ROOT/<policy dir>/policy.py`.
- **After:**
  - The door ran once and wrote `2026-11-22-build-TOOL-dQuietDisk-13-widen-10`, raising each count by one. The pass then set the counts to the measured 1206, 69 and 245, and changed nothing else in those rows.
  - A call onto a repository runs today's builder unchanged in both modes. Its cost is 3 trace files where the repository has nothing new to commit and 4 where it does.
  - `mk_repo` derives the key, then `&&` builds the template, so a failed key returns 1 before any build.
  - When `resolve_kit_dir` refuses the policy kit, the prologue passes an empty path, so the reader prints `shared`.
- **Cause:** builder discovery
- **Reason:**
  - `tools/memory-tree/ratchet.py#run_widen` raises a count by exactly one per call, and units 7 and 28 set their rows the same way under one record each.
  - `_build_mk_repo` rewrites `gate-legs.json` to its committed text, so over a repository with no other change its `git commit -qm seed` has nothing to commit. That commit spawns no `git maintenance run --auto` and returns 1, which no call site reads, at this base as before it.
  - Nested, a failed `derive_template_key` hands `resolve_template` an empty key, and that call runs the builder before it refuses to place `<root>/`.
  - An empty policy dir would have named `$ROOT//policy.py`.
- **Evidence:** all probes ran in this pass, in the session scratch directory (PINNED):
  - `python tools/gate-lint/sh_hygiene.py --shell-role --measure` printed 1206, 69 and 245, and `git diff -- memory/project/shell-role.txt` changes those three rows only.
  - A replayed `mk_repo` onto a built repository wrote 3 trace files (`init`, `add`, `commit`) and returned 1 at `per-case`. With an uncommitted file added, it wrote 4 at both `shared` and `per-case`, and the destination stayed the first call's clone.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** report
- **Caused-by:** TOOL-dQuietDisk-13
