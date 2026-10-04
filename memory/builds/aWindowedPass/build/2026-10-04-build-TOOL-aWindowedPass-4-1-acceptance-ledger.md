# TOOL-aWindowedPass-4 — acceptance ledger

**Serves:** journal TOOL-aWindowedPass-4

Kits declare the outputs their generators write as `[[generated]]` rows, and one resolver in the kit
library adds the conf's `GENERATED_INDEXES` pairs to them for check 23 and `--dispatch`. The readings
below were re-taken by the main loop at the close of the build, after commit 75cd13f7 and every later
unit had landed on the branch. The check-23 arms ran on a slice of `check-unattended.test.sh` holding
its prologue and the generated-render block, eight arms at exit 0.

**Evidences:** TOOL-aWindowedPass-4
- AC1 — `resolve_generated_indexes` — sourced over this repo with an empty conf value it printed six
  pairs, among them `memory/map/generated` with `gen_map.py` and `memory/gotchas/INDEX.md` with
  `gotchas.py`.
- AC2 — `GENERATED_INDEXES` — given a new pair and a duplicate of a declared one as its conf value,
  the resolver printed the six declared pairs, then the new pair once, and the duplicate not again.
- AC3 — `check-unattended.sh` — the fixture kit declaring `{memory_root}/derived` left
  `memory/derived/out.json` uncounted and printed `a generated render, the memory/derived index`.
- AC4 — `GENERATED_INDEXES=""` — the grep over `.unattended.conf` printed 1.
- AC5 — `python tools/govkit/govkit.py selfcheck` — exit 0 with six `[[generated]]` rows; with the
  codebase-map row's generator staged to `gen_map_missing.py` it exited 1 naming entry
  `codebase-map` and that file, and the descriptor was restored byte-identical.
