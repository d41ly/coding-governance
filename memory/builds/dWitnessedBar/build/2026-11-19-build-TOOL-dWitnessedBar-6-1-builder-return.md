**Serves:** journal TOOL-dWitnessedBar-6

# TOOL-dWitnessedBar-6 — builder return 1 (run `wf_ceedcefd-a16`), committed 1533b56d4

## Why

TOOL-dWitnessedBar-6 is built and committed, and its spec is closed. The checks on whether the spec could be built held against the tree before any code was written: every citation (run-gates.sh:6224-6244, unattended.sh:11114 and 12251-12254, test.sh:16800/16832, catalogue.toml:895/986-990, push-main.sh's two landing pushes, guard.py#check_staged/check_run_mandate, policy.py#DerivedDefault, verdict_flow/leg_factory seams, remote-ci.yml job `bar` and its step name) matched, and no section contradicted another. So there was no divergence to return.

## Summary

I built TOOL-dWitnessedBar-6 in two commits, both carrying `Pass: TOOL-dWitnessedBar-6`. All ten criteria were observed with fixtures or probes of my own code. No gate, suite or bar ran, and the three new arms and their red-first observations are owed at the close.

**Commits**
- `aecf1c95a` (feat) is the pass commit. It moves the spec to CLOSED and adds the acceptance ledger at `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-6-1-acceptance-ledger.md`. It also carries the staged RUN.md rows and the index rewrites (LIVE.md, backlog/TOOL.md, the build README and the spec's generated records table).
- `1533b56d4` (fix) is a follow-up the bug-class checklist asked for. The fixture now drops any inherited git variable (such as a hook's `GIT_DIR`) before its plants run. The peer plant still held with `GIT_DIR` pointed at this checkout.

**What was built**
- **Two new modules:**
  - `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/verdict_backends.py` holds the registry, `check_backend`, `read_verdict` with the five states, the local and peer readers, `verify-peer`, and 12 fixture plants.
  - `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/remote_verdict.py` holds `read_api`, the remote-ci witness rule, `derive_pin` and the `pin` verb, and `read_held_runs`, the held reader moved whole from `unattended.sh`.
- **Edited files:**
  - `tools/run-gates/kit.toml` gains the three backend rows.
  - `tools/push-main.sh` gains `check_landing_verdict`, called before both landing pushes.
  - `tools/unattended/unattended.sh`: `read_held_reds` is gone, `write_held_asks` calls the moved reader, and a new `write_pin_ask` runs at the dod_met site.
  - `tools/loop/guard.py` gains `OWNER_ONLY_KEYS` and a new plant, `pin-owner-only`.
  - The policy catalogue has summaries and usages for the four keys. `unsummarised-keys.txt` was drained with `policy.py lists --write`, and `help/reference/policy.md` was re-rendered.
  - Docs: the new page `help/verdict-backends.md`, its entry in `help/README.md`, and a section in `tools/run-gates/README.md`.
  - `symbols.json` was regenerated.

**Checks that ran, and the gate each stands in for**
- **All 12 plants of `verdict_backends.py --fixture`** held, each with its owed exit. They stand in for the gov arm, `push-main self-test` case 43, the `remote literals` leg, and `policy fixtures` / `policy check`.
  - AC1: a duplicate row is refused, naming both descriptors.
  - AC2: an unregistered or undeclared value refuses both `read` and a real copy of the lander, and the remote's refs are unchanged.
  - AC3: `local-hook` reads GREEN, RED and NONE correctly, and a scoped-only slot reads NONE.
  - AC4: a peer tag from node b reads GREEN; the same tag from the reading node, or one naming another tree, reads NONE.
  - AC5 and AC6: the remote plants read GREEN, NONE, NONE and DEAD PROBE as owed; the swapped workflow reads HELD naming the workflow file, and GREEN with witness `claimed` under app-only.
  - AC7: the `held` plant printed two rows and the liveness line the criterion names.
  - AC9: under peer-node with no peer verdict, the lander published the candidate ref, exited 1 naming NONE, and left main unmoved.
- **`verify-peer` end to end**, over a scratch remote with a stub bar: it published the verdict tag, skipped it on a second run, and node a then read GREEN.
- **AC7's driver half**, by sourcing `unattended.sh` in a probe (stands in for the `unattended kit gate`). `write_held_asks` calls `remote_verdict.py held <anchor> <workflow>`, and prints one DEAD PROBE line when no kit resolves. `write_pin_ask` files a `pin held: backend remote-ci` ask under remote-ci and stays silent under local-hook. `git grep 'read_held_reds()' tools/unattended` prints nothing, and `check-arms --emit-floors` shows `unattended.sh:343:339`, so the ceiling is unmoved.
- **AC8**: `remote_verdict.py pin` with `dispatch-closure` printed four blobs equal to `git rev-parse` and an id equal to `git hash-object --stdin`, and wrote nothing. The guard plant `pin-owner-only` exited 1 naming the key. This stands in for `loop guard fixtures`.
- **AC10**: all four greps hold. The lexicon answered OK for every new function name.

**Owed at the close**
- Three new arms need their runs and red-first observations:
  - The plant loop in `run-gates.gov.test.sh`.
  - Case 43 in `push-main.test.sh`.
  - The re-pointed h9 arm in `unattended.test.sh`.
- The guard plant `pin-owner-only` is an extra arm inside `loop guard fixtures` that §7 does not declare, so it also needs a red-first observation.
- Every leg in §7, including `kit epoch`, `codebase-map freshness`, `help reference pages` and the parity rows of `resolve-python.test.sh`. The parity check now covers a new inline copy of the `resolve_bash_py` block in `verdict_backends.py`.
- The `docs` leg should also run over the new help page. I kept it free of `python …` command spans so it would not trip UNROWED.

**Decisions to be aware of** (also recorded as `Decided:` trailers)
- **No kit version was bumped and `SESSION-KICKOFF.md` was not re-stamped.** The lander mints versions at landing, units 29, 7 and 21 bumped none, and `run-gates.sh` was not touched. If `kit epoch` names a kit at the close, its version line moves then.
- **The node tag is `GOV_NODE`**, the variable the run-gates kit already uses. With it unset, a peer read is DEAD PROBE and `verify-peer` refuses.
- **The fixture lander also needs the policy kit's `budgets.py` and `caps.toml`**, because `validate` imports them.

**Left alone**
- `help/reference/drive.md` and `help/reference/units.md` were already modified in the worktree. They are byte-identical to what the reference renderer writes, are not mine, and I left them unstaged.

**Not covered by any arm**
- The lander's refusal when no backend reader resolves.
- A real GitHub API answer.
- `verify-peer` running the real bar.

**For the owner, outside this unit**
- The policy grammar cannot set `verdict` to a string beside the `[verdict]` table that gov's own `.governance/policy.toml` already holds (`blocks`). Choosing a non-default backend in this repository therefore needs a policy-kit answer.
