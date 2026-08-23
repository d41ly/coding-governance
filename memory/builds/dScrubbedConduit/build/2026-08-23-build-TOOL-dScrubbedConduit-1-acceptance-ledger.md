# The acceptance ledger for TOOL-dScrubbedConduit-1

**Serves:** journal TOOL-dScrubbedConduit-1

Every line is OBSERVED, on this worktree at build time. Where a criterion was met by a measurement
rather than a command, the line names the measurement. Two lines record something that was observed
to be WRONG first, because that is the more useful half.

**Evidences:** TOOL-dScrubbedConduit-1

- AC1 — a `\x89PNG` byte sequence written to `memory/builds/dScrubbedConduit/reviews/probe.png`, then
  `python tools/memory-tree/gen_build_index.py --write`. Before S1: traceback,
  `UnicodeDecodeError: 'utf-8' codec can't decode byte 0x89 in position 0`. After S1 with only the
  decode widened: `--write` completed but the README gained a record ROW for the PNG and `LIVE.md`
  moved — so the binary was being treated as a record. After the exclusion: `LIVE.md` BYTE-IDENTICAL
  (`cmp -s` silent), README changed by exactly one line, `+  - [probe.png](reviews/probe.png)`, which
  is a folder-inventory link and not a record row. That one line is why AC1's byte-identity claim was
  narrowed at build time from "the artifacts" to LIVE.md and the ledger: listing a file that is
  genuinely in the folder is honest, and an AC that forbade it would have been wrong.
- AC2 — a scratch LINKED-WORKTREE fixture, no submodule: `git init w`, one commit,
  `git worktree add ../lw`. Running `git init` in a temp dir under `GIT_DIR=w/.git/worktrees/lw`
  flipped `w/.git/config` `core.bare` `false → true`. The same command with the hook's `unset` list
  applied left it `false`. Both directions observed, which is what separates a working scrub from a
  fixture that never reproduced the bug. Now permanent as arm 17 of `.githooks/pre-push.test.sh`.
- AC3 — three arms. `--check` with `memory/guides/BUILD-METHOD.md` absent: exit 1. `--render`: writes
  it, exit 0, `--check` then exit 0. And the arm that mattered — `memory/guides/` removed ENTIRELY,
  parent directory and all: `--render` recreated the directory and the file (23,636 bytes). Before
  S3, that case printed `No such file or directory`, then printed `kit-parity: rendered …` anyway,
  and exited 0 with no file.
- AC4 — `grep -qE '^KEEPALIVE_(CREATE|DELETE|INTERVAL)="<.*>"' .unattended.conf`, the narrowed
  predicate, run over four arms. All three keepalive values filled: PASS. Each of
  `KEEPALIVE_CREATE`, `KEEPALIVE_DELETE`, `KEEPALIVE_INTERVAL` replaced by `<placeholder-here>` in
  turn: FAIL, FAIL, FAIL. `KEEPALIVE_INTERVAL` is the one that matters: its shipped example value
  `<e.g. every 10 minutes (cron 3-59/10 * * * *)>` does not match the OLD `<[a-z-]+>` predicate at
  all, so it was undetectable. Also measured: the predicate says `discharged` for gov's own filled
  conf and `UNDISCHARGED` for a verbatim copy of `.unattended.conf.example`, which is the whole point.
- AC5 — `bash .githooks/pre-push origin git@x:y.git` run from a temp directory that is not a repo,
  with refspecs on stdin: **exit 1**, printing `pre-push: REFUSING — cannot resolve this repository's
  work tree`. Measured carefully, because the first attempt read `PIPESTATUS[0]` — which is
  `printf`'s exit, not the hook's — and reported 0. That is the same read-the-wrong-exit-code trap
  this class keeps producing. Now permanent as arm 18.
- AC6 — `bash tools/unattended/check-unattended.sh` exit 0, `bash tools/unattended/check-playbook.sh`
  exit 0, `bash tools/unattended/adopt-unattended.sh --check` exit 0, all three on this tree AFTER S4
  removed the `exempt_leg` blanket that had been suppressing them. They are green on their own merits
  rather than through the exemption.
- AC7 — `bash tools/run-gates/run-gates.sh` → `gates GREEN — 59/59 legs passed (26 skipped)`. Two legs
  went red first and both were mine: `codebase-map coverage + freshness` on a stale `symbols.json`
  (regenerated), and `install-prefix (shipped surface)`, because the waiver file keys on LINE NUMBERS
  and S2/S5 shifted `.githooks/pre-commit`'s dual-spelling probe from line 39 to line 48. The waiver
  row moved with it; the count did not rise, so the shrink-only rule holds.

## The rule this unit paid for twice

`S6`'s arms were each staged-broken before being called landed. The FIRST attempt at breaking arm 16
was a regex that did not match the hook's line continuation, so the arm passed over an unmodified
file and I nearly recorded that as a successful RED observation. It proved nothing. The second
attempt neutered the `unset` precisely and arm 16 failed, naming all eight variables. A staged break
that does not actually break anything is indistinguishable from a gate that works, which is the
failure mode the observe-the-RED rule exists to catch — and it caught me.
