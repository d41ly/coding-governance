**Serves:** journal TOOL-dWitnessedBar-91

# Build brief — TOOL-dWitnessedBar-91

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dWitnessedBar's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This unit is build order 48.
- Built so far through order 43: every unit up to and including 4, 25, 40, 23, 42, 3, 44, 5, 41, 55, 8, 1, 59, 30, 29,
  7, 21, 6, 2, 43, 51, 56, 57, 58, 60, 62, 63, 64, 65, 66, 69 (`298369174`: `read_green_file` reads with one `IFS= read -r` loop and strips one CR, `read_tag_lines` splits on LF and strips one CR), 68 (`14f441638`), 67 (`e1d569fc9`: section `2o` fixtures built with `-c init.defaultBranch=master init --ref-format=files` under exported `GIT_CONFIG_NOSYSTEM`/`GIT_CONFIG_GLOBAL`), 70 (`09718851e`: the AC12 canary), 71 (`ced984440`), 72 (`e0cf5fa91`), 74 (`7c579ad47`: `check_cr_reached` and its liveness variant, with `rgf_why`), 75 (`1b3295a52`: the canary's failure line names `rgf_what`), 73 (`71f212ad1`), 76 (`bdc10a4df`: `CANARY_KEYS`, `check_canary_keys` and one liveness loop over the keys), 77 (`7228b0a9a`), 79 (`08f226f3d`: `check_key_variant`, called for a tail and a length variant), 80 (`a967359a8`: the tail call passes `${_rg_v%?}x`), 81 (`dc1205950`: records only), 78 (`253e21771`: `read_inherited_green`; the gov canary guard in `tools/govkit/registry.toml` names `.githooks/pre-push`), 87 (`d2a1d891d`: records only), 82 (`47ab62ebf`: `FLOOR_ASSERTIONS=74`, its `# RAISED` comment on the line below the constant), 83 (`d21afc3fd`: records only; the line directly above `FLOOR_ASSERTIONS=` is kept for the derived owner, `TOOL-dWitnessedBar-90`), 84 (`e1ad4ef32`: honest return codes, counted visits, `FLOOR_ASSERTIONS=76`), 85 (`0a5a198f6`: each variant call adds one to `a` on return 0, `FLOOR_ASSERTIONS=80`; the gov suite's shell-role row is 850), 86 (`30917b91b`: records only), 88 (`7f1e87a6d`: `check_canary_keys` returns `0`, `1` or `2`; the five-spelling `<key>)` match; the canary guard gains `.githooks/`), 89 (`0c2f7e195`: return code `3` on a failed visited count; the whole-token `<key>)` match) and 90 (`da3fbc953`: the owner line above `FLOOR_ASSERTIONS=80`, the floor history deleted; shell-role row `853`). Unit 28 (order 30) is deferred
  against asks TOOL-dWitnessedBar-101 to -103 and is not built. This spec, rev-3, was re-grounded at `6b0ef7f7c`; it writes records only: at its pass, its own acceptance ledger with AC1 and AC2 owed to the close; S2's note in unit 90's ledger and the clone counts follow at the close. It mints no function and touches no code file; any probe or clone runs under the scratch directory or %TEMP%/<short-name>.
- This unit builds first at order 48; unit 92 consumes it and is re-grounded after it lands; nothing else is in flight in this working tree: commit directly here.
- The full `memory hygiene` leg is red at base on checks 13 and 15 from other records, and whole-tree spec tokens on one
  aMendedLedger spec; the main loop owns those at the close. Any other red is this unit's to fix.
- Cite code lines in every record you write as `path#symbol` or blob-pinned, never a bare `path:line`, fixture text
  included. Write no numeric fact without an id, a path:line, PINNED or DERIVED on its line.
- On this node bash 5.3.9 turns a `$'\r'` written inside `$(...)` into an empty string: a CR test inside a subshell
  uses a variable set outside it, as unit 70's `rgf_crb` does. Widen a shell-role row with `ratchet.py widen`, never
  by hand, and keep its TAB-separated columns.
- Every roster spec was re-grounded at `e4ac7c40c` so `check-spec-tokens.py --spec` admits it; the spec's base is still
  older than the run's `9e21ac76`. Verify each claim about current code against source before building on it, and hand
  a claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dWitnessedBar-91`, its trailer block carrying `Pass: TOOL-dWitnessedBar-91`
  beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dWitnessedBar/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-91-1-acceptance-ledger.md` in the pass commit:
  one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger excepted) needs its own `--dispatch` with `--writes` for it before you stage it. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
