# Acceptance ledger — TOOL-aBriskDeclaration-1

**Serves:** journal TOOL-aBriskDeclaration-1

Built against spec rev-1 in one pass commit, on node a. The observations below are each criterion's
own command, or the changed functions called directly, run over the worktree with the change in place
before the commit. No suite, gate leg or bar ran in the pass. The role gate refused
`check-arms.py --check` to the builder as the `harness arms (fail branches armed or pinned)` leg. Owed
to the main loop at the close: AC3, AC4 and AC11 as the criteria state them; every new arm of §7
observed red at base `846d51d39` and then green; and the legs of the spec's Gates section, that one
included.

The spec stays INPROGRESS in this pass. The pre-commit hook's hygiene check 12 refused it CLOSED,
because §8's F1 and F2 carry no resolution mark. The role gate admits only the status cell to the
builder and refuses the marks, which are the spec writer's to write. The build took each fork's
recommendation, (a): it lands live with no switch, and it adds no separate generator-pairing arm. The
marks, then the CLOSED flip, are owed before the close.

One reading of the spec was taken in the build. The header comment on `order_verb_of` in §4's code
block spells `_order_verb` in backticks, and AC1 requires the function's slice, with comment lines
removed, to hold no backtick. The header line is not a comment line, so AC1 decides it: the name is
written there without backticks.

A second pass built against spec rev-2, on node a, 2026-11-14. Rev-2 records the owner's picks: F1 (a),
live with no switch, which the code at `4fed38fe1` already follows; F2 (b), arm A6 and AC12. That pass
added arm A6 to region 3 of `tools/unattended/unattended.test.sh`, after A3 and before A4. No driver
code moved. Owed to the main loop at the close: AC12 as the criterion states it, and A6 observed red at
base `846d51d39` and at `4fed38fe1` with the pairing refusal's `remove_spec_token_check` call deleted,
then green. With F1 and F2 marked RESOLVED, that pass also set the spec CLOSED, as its last change.

**Evidences:** TOOL-aBriskDeclaration-1
- AC1 — `order_verb_of` — the criterion's probe ran with `PATH=/nonexistent` over the ten §4 plants and
  over three extra files: a directory, a header with no final newline, and a missing path. It ran under
  `LC_ALL=C` and `LC_ALL=C.UTF-8`. Each of the ten rows left the table's answer in `_order_verb`, and
  the printed answer matched it. Against the base reader run first over the same files, the only
  difference was the `\xff` plant that §4's "does not check" section names: empty before,
  `MALFORMED · order 7` after, under `C.UTF-8` only. The slice with comment lines removed: `grep -c`
  for `$(` or a backtick printed `0`.
- AC2 — `grep -c 'order_verb_of "$_[do]_spec" >/dev/null'` — it printed `2`. `grep -c '$(order_verb_of'`
  printed `0`.
- AC3 — `bash -x tools/unattended/unattended.sh --dispatch tRun --pass ARCH-tRun-5` — not run over the
  suite's tRun fixture in the pass. The new arm A2 grades it, and its run is owed to the main loop at
  the close. As a direct probe instead, the driver was sourced into a scratch git repository holding a
  stub that sleeps 3 s, prints an own-build hit and exits 1. `init_spec_token_check tRun` left <!-- PINNED 2026-11-14 -->
  `ST_STATE=run` and a handle and returned in 2 s. `run_spec_token_check tRun` printed the cache-off <!-- PINNED 2026-11-14 -->
  line and then `the declared spec-token checker reds over the live tree (stub.py exited 1 in 3s)`.
  It returned 1 at 5 s in all and left `ST_STATE` empty. <!-- PINNED 2026-11-14 -->
- AC4 — `two passes claiming one file are not disjoint` — not run over the suite's fixture in the
  pass. The new arm A3 grades it, owed to the main loop. As a direct probe in the same scratch
  repository, a started checker was still running when `remove_spec_token_check` was called. The call
  printed nothing on either stream, the child was gone after it, and it emptied `ST_HANDLE` and
  `ST_STATE`.
- AC5 — `MISSING` — the criterion's awk over `tools/unattended/unattended.sh` printed `2` and no
  `MISSING` line.
- AC6 — `RESOLVER-DIAG` — the driver was sourced in the scratch repository, with a `resolve_python`
  double that prints `RESOLVER-DIAG` on stderr and returns 1. `init_spec_token_check tRun` wrote
  nothing to a capture of both streams and left `ST_STATE=nopython`. `run_spec_token_check tRun` then
  printed `RESOLVER-DIAG` and next the line `UNATTENDED check 49 FAILED — --dispatch: the inline resolver
  found no usable python`. It returned 1. The suite arm A5, after `load_driver_conf` over tRun, is owed
  to the main loop.
- AC7 — `git diff --exit-code` — the criterion's `python -c` probe listed 40 check-49 branches before
  the change and after it. `diff` of the two listings printed nothing. `git diff --exit-code` over
  `tools/unattended/unarmed-branches.txt` printed nothing.
- AC8 — `It runs last because it costs a tree-wide scan` — `grep -c` printed `0` for each copy, and
  `started just before the open-pass reader` printed `1` for each. The `diff` of the two files past
  line 1 printed nothing.
- AC9 — `remove_spec_token_check` — `grep -c` printed `0` for `Both call sites read this through`,
  `0` for `IT RUNS LAST AMONG THE LOCAL REFUSALS` and `4` for `remove_spec_token_check`.
- AC10 — `memory/map/generated/symbols.json` — `lexicon.py --suggest` printed `OK — init_spec_token_check
  leads with init` and `OK — remove_spec_token_check leads with remove`. After `gen_map.py --write`,
  the index gained one function entry for each of the two names, in `tools/unattended/unattended.sh`,
  and nothing else.
- AC11 — `GIT_TRACE` — not run in the pass; the main loop ran it on node a, 2026-11-14, after the pass.
  Clone `dm` is the live tip `bc42f13ca` merged with `846d51d39`, reset and its spec-token key record
  removed; clone `db` is the same merge with the driver of `fc4c62bfa` applied, which `git apply` took
  cleanly. One `--dispatch dDeclaredLoop --pass TOOL-dDeclaredLoop-9 --writes tools/loop/loop_lib.py`
  under `bash -x` with `GIT_TRACE` on each, after first, then before, back to back. Before: rc 0, 200.1
  s, 192 git processes, 727 other traced processes (PINNED 2026-11-14). After: rc 0, 125.4 s, 193 git
  processes, 233 other traced processes (PINNED 2026-11-14). `diff` printed nothing for the stdout, for
  the stderr lines that are not trace lines, and for the staged run-state row with its UTC stamp
  masked. In the after trace, `init_spec_token_check` precedes `read_open_passes`, and the wait in
  `read_bounded` fell from 108.9 s to 58.9 s (PINNED 2026-11-14).
- AC12 — `--dispatch declares a generated index together with its generator` — not run over the suite's
  tRun fixture in the pass. The new arm A6 grades it, and its run is owed to the main loop at the
  close. `bash -n` over the suite printed nothing. As a direct probe, A6's trace awk ran over three
  `bash -x` traces of stub functions that print the driver's own `fail 49` line, single-quoted as in
  the real trace. With a start, the refusal and a remove, it printed `started refused read kills=0`.
  With the remove deleted, it printed `started refused unread kills=0`. With no start, it printed
  `unstarted no-refusal read kills=0`.
