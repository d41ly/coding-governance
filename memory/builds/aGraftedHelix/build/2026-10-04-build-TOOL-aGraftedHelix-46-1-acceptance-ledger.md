# Acceptance ledger — TOOL-aGraftedHelix-46

**Serves:** journal TOOL-aGraftedHelix-46

Node `a`, 2026-10-07. The build commit is `a2807562`, over the pass's parent `c3926703`, the spec's
rev-3 commit. No merge bar and no self-test suite ran in this pass. Every reading below ran in this
worktree, whose tree was clean after the build commit, so the bytes read are the commit's. The one
staged break was an edit of `tools/govkit/govkit.py` saved to the session scratchpad first and
copied back from it after the reading. Each slice's temp root came from `tempfile.mkdtemp` under
`%TEMP%`, never the scratchpad.

**Evidences:** TOOL-aGraftedHelix-46
- AC1 — `check_conf_reader_parity` — AC1's slice printed one `ok` line per table row naming the spelling, from `K='--no-verify'` to `K=plain`, the row-count `ok` line, and `FAILURES []`, in about 3 s rather than the 45 s the spec estimated. Re-run at `a2807562`, it printed 15 `ok` lines, the table's rows plus the three verdicts and the count.
- AC2 — `parse_conf_assignment` — with its body set back to the prior one-layer peel, the `v[0] == v[-1]` test, the slice printed `FAIL` for `K="<your-tool>"   # fill me` (`parse_conf_assignment '"<your-tool>"   # fill me'`), `K=""   # left blank` and `K=   # note` (`parse_conf_assignment '# note'`). It also failed the three other commented rows and all three verdicts, which read `{}`. Restored from the scratchpad copy, the file's diff against `c3926703` was the build's own.
- AC3 — `read_conf_key_gaps` — the slice printed `ok   [aGH-46 AC3] read_conf_key_gaps reads KEEPALIVE_CREATE as placeholder`, the same for `BYPASS_BAN` as `empty` and `LANDER` as `empty`. On AC2's prior peel all three printed `FAIL` with no gap at all, the behaviour the spec's evidence pins at `e1f4d8c0`.
- AC4 — `s.govkit_module().resolve_shell_argv = lambda a: ['g46-no-such-bash'] + a[1:]` — with that set before the call, the slice printed exactly one `FAIL`, naming the sentinel, the argv `['g46-no-such-bash', '-c', ...]` and `FileNotFoundError`. It printed no `ok` line, and `FAILURES` held that one label.
- AC5 — `grep -n "keeps any trailing comment" tools/govkit/govkit.py` — printed nothing and exited 1. The docstring of `read_conf_key_gaps` names `parse_conf_assignment` and says it does not read an unterminated quote, an escaped quote or adjacent concatenation.
- AC6 — `python tools/codebase-map/gen_map.py --check` — exited 0 after `--write` added `parse_conf_assignment` and `check_conf_reader_parity` to `memory/map/generated/symbols.json`, and again at `a2807562`. `python tools/lexicon/lexicon.py --suggest parse_conf_assignment --as py.function` printed `OK`, as did the same for `check_conf_reader_parity` and the nested `read_bash_value`. The full `python tools/lexicon/lexicon.py` printed `lexicon OK` and exited 0.
